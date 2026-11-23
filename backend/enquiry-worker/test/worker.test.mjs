// Run: node --test test/worker.test.mjs
// ALL provider calls are MOCKED (global fetch replaced). This proves server logic only —
// it does NOT prove that any real email was delivered.
import test from "node:test";
import assert from "node:assert/strict";
import worker, { _resetMemoryForTests, NOTIFY_TO, NOTIFY_CC } from "../worker.js";

const ORIGIN = "https://www.hmunique.com";
const ENV = { RESEND_API_KEY: "test_key_not_real", ENQUIRY_FROM: "HM UNIQUE <enquiries@example.test>", ALLOWED_ORIGINS: ORIGIN };
const realFetch = globalThis.fetch;
let sent;
function mockProvider(behaviour = () => ({ ok: true })) {
  sent = [];
  globalThis.fetch = async (url, init) => {
    const body = JSON.parse(init.body);
    sent.push({ url, body, headers: init.headers });
    const r = behaviour(body, sent.length);
    return r.ok ? new Response(JSON.stringify({ id: "mock" }), { status: 200 }) : new Response("provider error", { status: 500 });
  };
}
test.afterEach(() => { globalThis.fetch = realFetch; _resetMemoryForTests(); });

const base = () => ({ form: "quote", name: "Asha Rao", company: "Rao Traders", email: "asha@example.com", mobile: "+91 98765 43210", city: "Chennai", state: "Tamil Nadu", category: "electricals", product: "", quantity: "", message: "Need MCB quote", privacy: true, hp_url: "", startedAt: Date.now() - 10000, submissionId: crypto.randomUUID() });
const post = (body, { env = ENV, origin = ORIGIN, headers = {}, raw } = {}) =>
  worker.fetch(new Request("https://api.test/api/enquiry", { method: "POST", headers: { "content-type": "application/json", ...(origin ? { origin } : {}), "cf-connecting-ip": "203.0.113.7", ...headers }, body: raw ?? JSON.stringify(body) }), env);

test("not configured -> 503 and nothing sent", async () => {
  mockProvider(); const r = await post(base(), { env: { ALLOWED_ORIGINS: ORIGIN } });
  assert.equal(r.status, 503); assert.equal((await r.json()).code, "not_configured"); assert.equal(sent.length, 0);
});
test("origin not allowed -> 403", async () => { mockProvider(); const r = await post(base(), { origin: "https://evil.example" }); assert.equal(r.status, 403); assert.equal(sent.length, 0); });
test("preflight allowed only for allow-listed origin", async () => {
  const ok = await worker.fetch(new Request("https://api.test/api/enquiry", { method: "OPTIONS", headers: { origin: ORIGIN } }), ENV);
  const bad = await worker.fetch(new Request("https://api.test/api/enquiry", { method: "OPTIONS", headers: { origin: "https://evil.example" } }), ENV);
  assert.equal(ok.status, 204); assert.equal(bad.status, 403);
});
test("validation: missing/invalid fields -> 400 with field errors, nothing sent", async () => {
  mockProvider(); const b = base(); b.name = ""; b.email = "not-an-email"; b.privacy = false; b.category = "weapons";
  const r = await post(b); const j = await r.json();
  assert.equal(r.status, 400); assert.deepEqual(Object.keys(j.errors).sort(), ["category", "email", "name", "privacy"]); assert.equal(sent.length, 0);
});
test("validation: contact form requires allow-listed subject", async () => {
  mockProvider(); const b = { ...base(), form: "contact", phone: "9876543210", subject: "hack" }; const r = await post(b);
  assert.equal(r.status, 400); assert.ok((await r.json()).errors.subject);
});
test("limits: over-long message rejected", async () => { mockProvider(); const b = base(); b.message = "x".repeat(3001); const r = await post(b); assert.equal(r.status, 400); assert.ok((await r.json()).errors.message); });
test("body too large -> 413; wrong content-type -> 415; bad JSON -> 400", async () => {
  mockProvider();
  assert.equal((await post(null, { raw: "x".repeat(20000) })).status, 413);
  assert.equal((await post(base(), { headers: { "content-type": "text/plain" } })).status, 415);
  assert.equal((await post(null, { raw: "{bad" })).status, 400);
});
test("honeypot -> silent success, nothing sent", async () => { mockProvider(); const b = base(); b.hp_url = "http://spam"; const r = await post(b); assert.equal(r.status, 200); assert.equal(sent.length, 0); });
test("time trap: too fast / too old -> 400", async () => {
  mockProvider(); const fast = base(); fast.startedAt = Date.now() - 500; assert.equal((await post(fast)).status, 400);
  const old = base(); old.startedAt = Date.now() - 7 * 3600e3; assert.equal((await post(old)).status, 400); assert.equal(sent.length, 0);
});
test("success: notification To/CC/Reply-To/From correct; separate acknowledgement to customer", async () => {
  mockProvider(); const r = await post(base()); const j = await r.json();
  assert.equal(r.status, 200); assert.deepEqual([j.ok, j.accepted, j.acknowledgement], [true, true, "sent"]); assert.equal(sent.length, 2);
  const [n, a] = sent.map((s) => s.body);
  assert.deepEqual(n.to, [NOTIFY_TO]); assert.deepEqual(n.cc, [NOTIFY_CC]); assert.equal(n.reply_to, "asha@example.com"); assert.equal(n.from, ENV.ENQUIRY_FROM);
  assert.deepEqual(a.to, ["asha@example.com"]); assert.equal(a.from, ENV.ENQUIRY_FROM); assert.equal(a.cc, undefined);
  assert.ok(!n.from.includes("asha@") && !a.from.includes("asha@"));
  assert.equal(a.subject, "We’ve received your enquiry — HM UNIQUE");
  assert.ok(a.text.startsWith("Hello Asha Rao,\n\nThank you for contacting HM UNIQUE."));
  assert.ok(a.text.includes("For assistance, contact business@hmunique.com or +91 97101 81944.")); assert.ok(a.text.endsWith("Regards,\nHM UNIQUE Technology Enterprises\n"));
});
test("recipients cannot be changed from the request", async () => {
  mockProvider(); const b = { ...base(), to: "attacker@evil.test", cc: "x@evil.test", bcc: "y@evil.test", from: "ceo@hmunique.com", reply_to: "z@evil.test" };
  await post(b); const n = sent[0].body; assert.deepEqual(n.to, [NOTIFY_TO]); assert.deepEqual(n.cc, [NOTIFY_CC]); assert.equal(n.reply_to, "asha@example.com"); assert.equal(n.bcc, undefined);
  assert.ok(!JSON.stringify(sent).includes("evil.test"));
});
test("escaping + header-injection: HTML escaped, subjects single-line", async () => {
  mockProvider(); const b = base(); b.name = 'Eve <img src=x onerror=alert(1)>\r\nBcc: v@evil.test'; b.message = "<script>alert(1)</script> & \"quotes\"";
  const r = await post(b); assert.equal(r.status, 200); const [n, a] = sent.map((s) => s.body);
  assert.ok(!n.html.includes("<script>") && !n.html.includes("<img") && n.html.includes("&lt;script&gt;")); assert.ok(!a.html.includes("<img"));
  assert.ok(!/[\r\n]/.test(n.subject) && !/[\r\n]/.test(a.subject)); assert.equal(n.bcc, undefined);
});
test("acknowledgement failure: enquiry still accepted, acknowledgement=failed, no resubmission needed", async () => {
  mockProvider((body) => ({ ok: !body.to.includes("asha@example.com") })); const r = await post(base()); const j = await r.json();
  assert.equal(r.status, 200); assert.deepEqual([j.accepted, j.acknowledgement], [true, "failed"]);
});
test("notification failure: 502, NOT accepted, acknowledgement never sent, retry with same id allowed", async () => {
  const b = base(); mockProvider(() => ({ ok: false })); const r = await post(b); assert.equal(r.status, 502); assert.equal((await r.json()).code, "delivery_failed"); assert.equal(sent.length, 1);
  mockProvider(); const r2 = await post(b); assert.equal(r2.status, 200); assert.equal(sent.length, 2);
});
test("duplicate submission (same id, or same content with new id) sends nothing twice", async () => {
  mockProvider(); const b = base(); await post(b); assert.equal(sent.length, 2);
  const again = await post(b); assert.equal((await again.json()).duplicate, true);
  const b2 = { ...b, submissionId: crypto.randomUUID() }; const again2 = await post(b2); assert.equal((await again2.json()).duplicate, true); assert.equal(sent.length, 2);
});
test("rate limit: 6th distinct submission from one IP -> 429", async () => {
  mockProvider(); for (let i = 0; i < 5; i++) { const b = base(); b.message = "msg " + i; assert.equal((await post(b)).status, 200); }
  const b = base(); b.message = "msg 6"; const r = await post(b); assert.equal(r.status, 429); assert.equal(r.headers.get("retry-after"), "600");
});
test("secrets never appear in responses", async () => { mockProvider(); const r = await post(base()); assert.ok(!(await r.text()).includes("test_key_not_real")); });

// ====================================================================================================
// Retry / duplicate / rate-limit behaviour (Batch 29 correction).
// The provider is MOCKED, but it emulates Resend's documented Idempotency-Key semantics: same key + same
// payload -> original result, nothing delivered again; same key + different payload -> 409. This proves the
// Worker sends byte-identical retries; it does NOT prove how the real provider behaves.
// ====================================================================================================
let delivered;
function mockResend(plan = () => "ok") {
  sent = []; delivered = []; const seen = new Map();
  globalThis.fetch = async (url, init) => {
    const key = init.headers["idempotency-key"]; const body = init.body; const parsed = JSON.parse(body);
    sent.push({ key, body: parsed });
    const mode = plan(parsed, key, sent.length);
    if (mode === "4xx") return new Response("rejected", { status: 422 });
    if (mode === "5xx") return new Response("error", { status: 500 });
    if (seen.has(key)) {
      const e = seen.get(key);
      return e.body === body ? new Response(JSON.stringify({ id: e.id }), { status: 200 }) : new Response(JSON.stringify({ name: "invalid_idempotent_request" }), { status: 409 });
    }
    const id = "id" + delivered.length; seen.set(key, { body, id }); delivered.push({ key, body: parsed });
    if (mode === "drop-after-send") throw new TypeError("network reset after the provider accepted the message");
    return new Response(JSON.stringify({ id }), { status: 200 });
  };
}
const kinds = () => delivered.map((d) => (d.body.cc ? "notification" : "acknowledgement"));
function kvMock({ failPrefixes = [] } = {}) {
  const m = new Map();
  return { m, async get(k) { return m.has(k) ? m.get(k) : null; }, async put(k, v) { if (failPrefixes.some((p) => k.startsWith(p))) throw new Error("kv unavailable"); m.set(k, v); } };
}

test("retry after an in-doubt send (response lost): identical request + same provider key -> one notification delivered", async () => {
  const b = base(); mockResend((body, key, n) => (n === 1 ? "drop-after-send" : "ok"));
  const r1 = await post(b); assert.equal(r1.status, 502); // person sees "not received" and retries
  assert.equal(delivered.filter((d) => d.body.cc).length, 1); // ...but the provider did send it
  const r2 = await post(b); assert.equal(r2.status, 200);
  assert.equal(kinds().filter((k) => k === "notification").length, 1, "provider de-duplicated the retry");
  assert.equal(sent[0].key, sent[1].key); assert.deepEqual(sent[0].body, sent[1].body); // byte-identical payload (no timestamp/attempt data)
  assert.ok(!sent.some((s) => s.key.includes("undefined")));
});
test("provider 5xx (outcome unknown): retry keeps the SAME key", async () => {
  const b = base(); mockResend((x, k, n) => (n === 1 ? "5xx" : "ok")); assert.equal((await post(b)).status, 502);
  assert.equal((await post(b)).status, 200); assert.equal(sent[0].key, sent[1].key); assert.equal(kinds().filter((k) => k === "notification").length, 1);
});
test("provider 4xx (definitely rejected): retry uses a FRESH provider key, then succeeds", async () => {
  const b = base(); mockResend((x, k, n) => (n === 1 ? "4xx" : "ok")); assert.equal((await post(b)).status, 502);
  assert.equal((await post(b)).status, 200); assert.notEqual(sent[0].key, sent[1].key); assert.equal(kinds().filter((k) => k === "notification").length, 1);
});
test("notification sent, acknowledgement failed: accepted; a retry sends NOTHING more and returns the stored result", async () => {
  const b = base(); mockResend((body) => (body.cc ? "ok" : "5xx")); const r1 = await (await post(b)).json();
  assert.deepEqual([r1.accepted, r1.acknowledgement], [true, "failed"]); const calls = sent.length;
  const r2 = await (await post(b)).json(); assert.equal(r2.duplicate, true); assert.equal(sent.length, calls); assert.equal(kinds().filter((k) => k === "notification").length, 1);
});
test("storage fails AFTER the notification was sent: still accepted; retry skips/dedupes the notification", async () => {
  const kv = kvMock({ failPrefixes: ["idem:", "fp:"] }); const env = { ...ENV, ENQUIRY_KV: kv }; const b = base(); mockResend();
  const r1 = await post(b, { env }); assert.equal(r1.status, 200); // a storage hiccup is not reported as a failure
  const r2 = await post(b, { env }); assert.equal(r2.status, 200);
  assert.equal(kinds().filter((k) => k === "notification").length, 1, "progress record made the retry skip the notification");
  assert.equal(kinds().filter((k) => k === "acknowledgement").length, 1, "identical acknowledgement de-duplicated by the provider");
});
test("ALL storage writes fail: retry re-sends an identical request and the provider de-duplicates it", async () => {
  const kv = kvMock({ failPrefixes: ["idem:", "fp:", "st:", "rl:"] }); const env = { ...ENV, ENQUIRY_KV: kv }; const b = base(); mockResend();
  assert.equal((await post(b, { env })).status, 200); assert.equal((await post(b, { env })).status, 200);
  assert.equal(kinds().filter((k) => k === "notification").length, 1); assert.equal(kinds().filter((k) => k === "acknowledgement").length, 1);
});
test("edited retry after a failure is a NEW enquiry (new key, new content) — never a 409 from the provider", async () => {
  const b = base(); mockResend((x, k, n) => (n === 1 ? "5xx" : "ok")); assert.equal((await post(b)).status, 502);
  const edited = { ...b, message: "Need MCB quote - 200 pcs" }; assert.equal((await post(edited)).status, 200);
  assert.notEqual(sent[0].key, sent[1].key);
});
test("rate limit is not consumed by delivery failures: 5 failed attempts, the 6th still goes through", async () => {
  const b = base(); mockResend((x, k, n) => (n <= 5 ? "5xx" : "ok"));
  for (let i = 0; i < 5; i++) assert.equal((await post(b)).status, 502);
  assert.equal((await post(b)).status, 200);
});
test("LIMITATION (memory fallback): a restart/new instance forgets rate-limit counts and duplicate records", async () => {
  mockResend(); const b = base(); assert.equal((await (await post(b)).json()).duplicate, undefined);
  _resetMemoryForTests(); // = a different isolate or a restart
  const again = await (await post(b)).json(); assert.equal(again.duplicate, undefined, "Worker no longer recognises it...");
  assert.equal(kinds().filter((k) => k === "notification").length, 1, "...only the provider's idempotency key stopped the second email");
  _resetMemoryForTests(); mockResend(); for (let i = 0; i < 5; i++) { const x = base(); x.message = "m" + i; await post(x); }
  _resetMemoryForTests(); const y = base(); y.message = "after restart"; assert.equal((await post(y)).status, 200, "rate-limit counter was lost");
});
test("KV bound (shared across instances/restarts): duplicates recognised and rate limit enforced after a 'restart'", async () => {
  const kv = kvMock(); const env = { ...ENV, ENQUIRY_KV: kv }; mockResend(); const b = base();
  await post(b, { env }); _resetMemoryForTests();
  assert.equal((await (await post(b, { env })).json()).duplicate, true);
  for (let i = 0; i < 4; i++) { const x = base(); x.message = "k" + i; assert.equal((await post(x, { env })).status, 200); }
  _resetMemoryForTests(); const z = base(); z.message = "kz"; assert.equal((await post(z, { env })).status, 429);
});
