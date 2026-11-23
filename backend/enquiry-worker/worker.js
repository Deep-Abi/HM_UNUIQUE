/**
 * HM UNIQUE enquiry endpoint — Cloudflare Worker (ES module).
 *
 * Receives JSON from the Request a Quote modal and the Contact form, validates it on the
 * server, and sends two emails through the Resend HTTP API:
 *   1. Notification   To: hmunitecenterprises02@gmail.com   CC: business@hmunique.com
 *                     Reply-To: the customer's validated address
 *   2. Acknowledgement To: the customer                       (separate message)
 * Both are sent FROM a verified company sender (env ENQUIRY_FROM) — never from the customer.
 *
 * Recipients are fixed in this file; nothing in the request can change them.
 * No secret is stored in the website or in this repository: see README.md for the variables.
 *
 * Contract with js/forms.js:
 *   200 {ok:true, accepted:true, acknowledgement:"sent"|"failed"|"skipped", duplicate?:true}
 *   400 {ok:false, code:"validation", errors:{field:message}}
 *   403 {ok:false, code:"forbidden"}            (origin not allowed)
 *   413/415 {ok:false, code:"bad_request"}
 *   429 {ok:false, code:"rate_limited"}
 *   503 {ok:false, code:"not_configured"}       (secrets/sender missing — nothing sent)
 *   502 {ok:false, code:"delivery_failed"}      (notification could not be sent — NOT accepted)
 * An acknowledgement failure never turns an accepted enquiry into an error.
 */

// ---- Fixed server-side recipients (not configurable from the request) -------------------
export const NOTIFY_TO = "hmunitecenterprises02@gmail.com";
export const NOTIFY_CC = "business@hmunique.com";
export const COMPANY_PHONE = "+91 97101 81944";
export const COMPANY_EMAIL = "business@hmunique.com";

// ---- Limits and allow-lists --------------------------------------------------------------
const MAX_BODY_BYTES = 16 * 1024;
const LIMITS = { name: 100, company: 150, email: 254, phone: 20, city: 80, state: 80, product: 150, quantity: 60, message: 3000 };
const CATEGORIES = {
  electricals: "Electricals",
  electronics: "Electronics Components",
  hardwares: "Hardware",
  industrial: "Industrial & Commercial Equipments",
  "safety-packing": "Industrial Safety & Packing Materials",
};
const SUBJECTS = { general: "General Enquiry", product: "Product Enquiry", support: "Support", partnership: "Partnership", other: "Other" };
const EMAIL_RE = /^[^\s@<>()",;:\\]+@[^\s@<>()",;:\\]+\.[^\s@<>()",;:\\]{2,}$/;
const PHONE_RE = /^[0-9+\-\s()]{7,15}$/;
const MIN_FILL_MS = 3000;            // a person cannot complete the form faster than this
const MAX_FORM_AGE_MS = 6 * 3600e3;  // stale pages are rejected
const RATE_LIMIT = { max: 5, windowSec: 600 };
const DEDUPE_WINDOW_SEC = 120;
const IDEMPOTENCY_TTL_SEC = 86400;

// ---- Small helpers -----------------------------------------------------------------------
export function escapeHtml(value) {
  return String(value).replace(/[&<>"'`]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;", "`": "&#96;" }[c]));
}
/** Single-line text safe for email headers and subjects: no CR/LF/control characters. */
export function singleLine(value) {
  return String(value).replace(/[\u0000-\u001f\u007f\u2028\u2029]+/g, " ").replace(/\s+/g, " ").trim();
}
function cleanText(value, max, { multiline = false } = {}) {
  if (typeof value !== "string") return "";
  let v = value.normalize("NFC").replace(/\u0000/g, "");
  v = multiline ? v.replace(/\r\n?/g, "\n").replace(/[\u0001-\u0008\u000b\u000c\u000e-\u001f\u007f]/g, "") : singleLine(v);
  return v.trim().slice(0, max);
}
function json(body, status = 200, headers = {}) {
  return new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...headers } });
}
async function sha256Hex(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

// ---- Validation --------------------------------------------------------------------------
/** Returns {values, errors}. Never trusts the client: every field is re-checked here. */
export function validateEnquiry(input) {
  const errors = {};
  const src = input && typeof input === "object" ? input : {};
  const form = src.form === "quote" ? "quote" : src.form === "contact" ? "contact" : null;
  if (!form) errors.form = "Unknown form.";

  const v = {
    form,
    name: cleanText(src.name, LIMITS.name),
    company: cleanText(src.company, LIMITS.company),
    email: cleanText(src.email, LIMITS.email).toLowerCase(),
    phone: cleanText(src.mobile ?? src.phone, LIMITS.phone),
    city: cleanText(src.city, LIMITS.city),
    state: cleanText(src.state, LIMITS.state),
    category: cleanText(src.category, 40),
    product: cleanText(src.product, LIMITS.product),
    quantity: cleanText(src.quantity, LIMITS.quantity),
    subject: cleanText(src.subject, 40),
    message: cleanText(src.message, LIMITS.message, { multiline: true }),
    consent: src.privacy === true || src.privacy === "true" || src.privacy === "on",
  };

  if (!v.name) errors.name = "Please enter your name.";
  if (!EMAIL_RE.test(v.email)) errors.email = "Please enter a valid email.";
  if (!PHONE_RE.test(v.phone) || v.phone.replace(/\D/g, "").length < 7) errors.phone = "Please enter a valid phone number.";
  if (!v.message) errors.message = "Please enter your message.";
  if (!v.consent) errors.privacy = "Please agree to the privacy policy to continue.";
  if (form === "quote") {
    if (!v.company) errors.company = "Please enter your company name.";
    if (!v.city) errors.city = "Please enter your city.";
    if (!v.state) errors.state = "Please enter your state.";
    if (!CATEGORIES[v.category]) errors.category = "Please select a category.";
  }
  if (form === "contact") {
    if (!SUBJECTS[v.subject]) errors.subject = "Please select a subject.";
  }
  // Reject over-long originals instead of silently truncating names/messages the person typed.
  for (const [k, max] of [["name", LIMITS.name], ["company", LIMITS.company], ["message", LIMITS.message], ["product", LIMITS.product]]) {
    const raw = src[k];
    if (typeof raw === "string" && raw.trim().length > max) errors[k] = `Please keep this under ${max} characters.`;
  }
  return { values: v, errors };
}

// ---- Email templates (all customer content is escaped) -----------------------------------
function rowsFor(v) {
  const rows = [["Form", v.form === "quote" ? "Request a Quote" : "Contact page"], ["Name", v.name], ["Company", v.company || "—"], ["Email", v.email], ["Phone", v.phone]];
  if (v.form === "quote") {
    rows.push(["City", v.city], ["State", v.state], ["Category", CATEGORIES[v.category]], ["Product", v.product || "—"], ["Quantity", v.quantity || "—"]);
  } else {
    rows.push(["Subject", SUBJECTS[v.subject]]);
  }
  return rows;
}
export function buildNotification(v, meta) {
  const rows = rowsFor(v);
  const subject = singleLine(`New ${v.form === "quote" ? "quote request" : "website enquiry"} — ${v.name}${v.form === "quote" ? " (" + CATEGORIES[v.category] + ")" : ""}`).slice(0, 180);
  const html = `<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;color:#0B2338">
<h2 style="margin:0 0 12px">${escapeHtml(subject)}</h2>
<table cellpadding="6" cellspacing="0" style="border-collapse:collapse">${rows.map(([k, val]) => `<tr><td style="border-bottom:1px solid #e3e8ee;font-weight:bold;vertical-align:top">${escapeHtml(k)}</td><td style="border-bottom:1px solid #e3e8ee">${escapeHtml(val)}</td></tr>`).join("")}</table>
<h3 style="margin:16px 0 6px">Message</h3>
<div style="white-space:pre-wrap;border:1px solid #e3e8ee;padding:10px;border-radius:6px">${escapeHtml(v.message)}</div>
<p style="color:#5b6b7a;font-size:12px;margin-top:16px">Reference ${escapeHtml(meta.ref)} · reply to this email to answer the customer.</p></div>`;
  const text = `${subject}\n\n${rows.map(([k, val]) => `${k}: ${val}`).join("\n")}\n\nMessage:\n${v.message}\n\nReference ${meta.ref}\n`;
  return { subject, html, text };
}
export function buildAcknowledgement(v) {
  const name = singleLine(v.name);
  const subject = "We’ve received your enquiry — HM UNIQUE";
  const text = `Hello ${name},\n\nThank you for contacting HM UNIQUE. We’ve received your enquiry, and our team will contact you shortly to discuss your requirements.\n\nFor assistance, contact ${COMPANY_EMAIL} or ${COMPANY_PHONE}.\n\nRegards,\nHM UNIQUE Technology Enterprises\n`;
  const html = `<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.5;color:#0B2338">
<p>Hello ${escapeHtml(name)},</p>
<p>Thank you for contacting HM UNIQUE. We’ve received your enquiry, and our team will contact you shortly to discuss your requirements.</p>
<p>For assistance, contact <a href="mailto:${COMPANY_EMAIL}">${COMPANY_EMAIL}</a> or <a href="tel:+919710181944">${COMPANY_PHONE}</a>.</p>
<p>Regards,<br>HM UNIQUE Technology Enterprises</p></div>`;
  return { subject, html, text };
}

// ---- Provider: Resend HTTP API (swap this one function for another provider) -------------
export async function sendViaResend(env, message, idempotencyKey) {
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { authorization: `Bearer ${env.RESEND_API_KEY}`, "content-type": "application/json", "idempotency-key": idempotencyKey },
    body: JSON.stringify(message),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => "");
    const err = new Error(`provider ${res.status} ${detail.slice(0, 300)}`);
    err.status = res.status; // only set when the provider actually answered; a network failure has no status
    throw err;
  }
  return res.json().catch(() => ({}));
}

// ---- Storage: Workers KV when bound (ENQUIRY_KV), otherwise per-isolate memory (best effort) ----
const memory = new Map();
const store = {
  async get(env, key) {
    if (env.ENQUIRY_KV) return env.ENQUIRY_KV.get(key);
    const e = memory.get(key);
    if (!e) return null;
    if (e.exp < Date.now()) { memory.delete(key); return null; }
    return e.val;
  },
  async put(env, key, val, ttlSec) {
    if (env.ENQUIRY_KV) return env.ENQUIRY_KV.put(key, val, { expirationTtl: Math.max(60, ttlSec) });
    memory.set(key, { val, exp: Date.now() + ttlSec * 1000 });
    if (memory.size > 2000) memory.delete(memory.keys().next().value);
  },
};
export function _resetMemoryForTests() { memory.clear(); }
/** Best-effort write: a storage hiccup AFTER an email was sent must never turn into an error response. */
async function safePut(env, key, val, ttlSec) {
  try { await store.put(env, key, val, ttlSec); } catch (err) { console.error("storage write failed", key.split(":")[0], String((err && err.message) || err)); }
}
function parseJson(text) { try { return text ? JSON.parse(text) : null; } catch { return null; } }

// ---- CORS / origin -----------------------------------------------------------------------
function allowedOrigins(env) {
  return String(env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
}
function corsHeaders(origin, env) {
  return origin && allowedOrigins(env).includes(origin)
    ? { "access-control-allow-origin": origin, vary: "origin", "access-control-allow-methods": "POST, OPTIONS", "access-control-allow-headers": "content-type" }
    : { vary: "origin" };
}

async function verifyTurnstile(env, token, ip) {
  const body = new URLSearchParams({ secret: env.TURNSTILE_SECRET, response: token || "" });
  if (ip) body.set("remoteip", ip);
  const res = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", body });
  const data = await res.json().catch(() => ({}));
  return data.success === true;
}

// ---- Request handler ---------------------------------------------------------------------
export default {
  async fetch(request, env, ctx) {
    const origin = request.headers.get("origin") || "";
    const cors = corsHeaders(origin, env);
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return origin && cors["access-control-allow-origin"] ? new Response(null, { status: 204, headers: cors }) : new Response(null, { status: 403 });
    }
    if (url.pathname !== "/" && url.pathname !== "/api/enquiry") return json({ ok: false, code: "not_found" }, 404, cors);
    if (request.method !== "POST") return json({ ok: false, code: "method_not_allowed" }, 405, { ...cors, allow: "POST, OPTIONS" });

    // Origin check: browsers always send Origin on cross-origin POST; reject anything not allow-listed.
    if (origin && !cors["access-control-allow-origin"]) return json({ ok: false, code: "forbidden" }, 403, cors);
    if (!origin && env.REQUIRE_ORIGIN === "true") return json({ ok: false, code: "forbidden" }, 403, cors);

    // Configuration: refuse (and send nothing) unless the secrets and verified sender exist.
    if (!env.RESEND_API_KEY || !env.ENQUIRY_FROM) return json({ ok: false, code: "not_configured" }, 503, cors);

    if (!(request.headers.get("content-type") || "").toLowerCase().includes("application/json")) return json({ ok: false, code: "bad_request" }, 415, cors);
    const declared = Number(request.headers.get("content-length") || 0);
    if (declared > MAX_BODY_BYTES) return json({ ok: false, code: "bad_request" }, 413, cors);
    const raw = await request.text();
    if (new TextEncoder().encode(raw).length > MAX_BODY_BYTES) return json({ ok: false, code: "bad_request" }, 413, cors);
    let input;
    try { input = JSON.parse(raw); } catch { return json({ ok: false, code: "bad_request" }, 400, cors); }
    if (!input || typeof input !== "object" || Array.isArray(input)) return json({ ok: false, code: "bad_request" }, 400, cors);

    const ip = request.headers.get("cf-connecting-ip") || "unknown";

    // Spam protection 1: honeypot — bots fill the hidden field. Pretend success, send nothing.
    if (typeof input.hp_url === "string" && input.hp_url.trim() !== "") return json({ ok: true, accepted: true, acknowledgement: "skipped" }, 200, cors);
    // Spam protection 2: time trap.
    const age = Date.now() - Number(input.startedAt || 0);
    if (!Number.isFinite(age) || age < MIN_FILL_MS || age > MAX_FORM_AGE_MS) {
      return json({ ok: false, code: "validation", errors: { form: "Please wait a moment and try sending again." } }, 400, cors);
    }
    // Spam protection 3 (optional): Cloudflare Turnstile when TURNSTILE_SECRET is set.
    if (env.TURNSTILE_SECRET && !(await verifyTurnstile(env, input.turnstileToken, ip))) {
      return json({ ok: false, code: "validation", errors: { form: "Verification failed. Please try again." } }, 400, cors);
    }

    const { values, errors } = validateEnquiry(input);
    if (Object.keys(errors).length) return json({ ok: false, code: "validation", errors }, 400, cors);

    // ---- Duplicate protection ---------------------------------------------------------------
    // One enquiry = (client submissionId, content hash). Retrying the SAME enquiry reuses the key; if the
    // person edits the text after a failure it is a new enquiry (new key) and is sent again.
    const idemRaw = typeof input.submissionId === "string" ? input.submissionId : "";
    const idem = /^[A-Za-z0-9-]{16,64}$/.test(idemRaw) ? idemRaw : await sha256Hex(`${ip}|${raw}`);
    const contentHash = await sha256Hex(JSON.stringify([values.form, values.name, values.company, values.email, values.phone, values.city, values.state, values.category, values.product, values.quantity, values.subject, values.message]));
    const key = `${idem}.${contentHash.slice(0, 16)}`;
    const idemKey = `idem:${key}`;   // final result of a finished enquiry
    const stKey = `st:${key}`;       // progress of an unfinished enquiry (survives a failed/aborted attempt)

    const prior = parseJson(await store.get(env, idemKey));
    if (prior) return json({ ...prior, duplicate: true }, 200, cors);
    // ...and a content fingerprint, so a double click that produced two different keys is also caught.
    const fpKey = `fp:${await sha256Hex([values.form, values.email, values.phone, values.message].join("|"))}`;
    const fpPrior = parseJson(await store.get(env, fpKey));
    if (fpPrior) return json({ ...fpPrior, duplicate: true }, 200, cors);

    // Rate limit per IP (counted only for well-formed, non-duplicate submissions).
    const rlKey = `rl:${ip}`;
    const count = Number((await store.get(env, rlKey)) || 0);
    if (count >= RATE_LIMIT.max) return json({ ok: false, code: "rate_limited" }, 429, { ...cors, "retry-after": String(RATE_LIMIT.windowSec) });
    await safePut(env, rlKey, String(count + 1), RATE_LIMIT.windowSec);
    // A failure that is OUR/the provider's fault must not use up the person's allowance for their retry.
    const refund = () => safePut(env, rlKey, String(count), RATE_LIMIT.windowSec);

    // ---- Send --------------------------------------------------------------------------------
    // Progress state: {ref, notified, attempt}. The reference is derived from the key and the message bodies
    // contain nothing time- or attempt-dependent, so a retry produces a byte-identical request. Combined with
    // the provider Idempotency-Key that means a retry should not create a second notification (provider behaviour is documented, not verified here).
    const state = parseJson(await store.get(env, stKey)) || { ref: `HMU-${(await sha256Hex(key)).slice(0, 10).toUpperCase()}`, notified: false, attempt: 0 };
    const note = buildNotification(values, { ref: state.ref });

    // 1) Notification — this is what "accepted" means. If it fails, nothing is accepted and the client may retry.
    if (!state.notified) {
      try {
        await sendViaResend(env, {
          from: env.ENQUIRY_FROM,
          to: [NOTIFY_TO],
          cc: [NOTIFY_CC],
          reply_to: values.email,
          subject: note.subject,
          html: note.html,
          text: note.text,
        }, `notify-${key}-${state.attempt}`);
        state.notified = true;
        await safePut(env, stKey, JSON.stringify(state), IDEMPOTENCY_TTL_SEC); // a retry now skips this step entirely
      } catch (err) {
        console.error("notification failed", state.ref, String((err && err.message) || err));
        // Definite provider rejection (a 4xx answer, other than "another identical request is in progress"):
        // nothing was sent, so use a fresh provider key next time rather than risk the provider replaying the
        // rejection. A network error / timeout / 5xx may or may not have sent, so the SAME key is kept and the
        // provider de-duplicates the identical retry.
        if (err && err.status >= 400 && err.status < 500 && err.status !== 409) {
          state.attempt += 1;
          await safePut(env, stKey, JSON.stringify(state), IDEMPOTENCY_TTL_SEC);
        }
        await refund();
        return json({ ok: false, code: "delivery_failed" }, 502, cors);
      }
    }

    // 2) Acknowledgement — separate message; its failure never un-accepts the enquiry and is not retried.
    let acknowledgement = "sent";
    try {
      const ack = buildAcknowledgement(values);
      await sendViaResend(env, { from: env.ENQUIRY_FROM, to: [values.email], reply_to: COMPANY_EMAIL, subject: ack.subject, html: ack.html, text: ack.text }, `ack-${key}`);
    } catch (err) {
      acknowledgement = "failed";
      console.error("acknowledgement failed", state.ref, String((err && err.message) || err));
    }

    const result = JSON.stringify({ ok: true, accepted: true, acknowledgement });
    await safePut(env, idemKey, result, IDEMPOTENCY_TTL_SEC);
    await safePut(env, fpKey, result, DEDUPE_WINDOW_SEC);
    return json(JSON.parse(result), 200, cors);
  },
};
