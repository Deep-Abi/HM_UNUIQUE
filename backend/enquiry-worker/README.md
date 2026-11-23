# HM UNIQUE enquiry endpoint (Cloudflare Worker)

This is the server side of the **Request a Quote** modal and the **Contact** form. The website itself
is static, so it needs one small server-side piece to send email without exposing any secret in the
browser. **This folder is not part of the public website — do not upload `backend/` to the web host**
(`robots.txt` also disallows it).

## What it does
For every accepted enquiry it sends two separate emails through the Resend HTTP API:

| Email | To | CC | Reply-To | From |
|---|---|---|---|---|
| Notification | hmunitecenterprises02@gmail.com | business@hmunique.com | the customer's validated address | `ENQUIRY_FROM` (verified company sender) |
| Acknowledgement | the customer | – | business@hmunique.com | `ENQUIRY_FROM` |

* Recipients are constants in `worker.js`; nothing in the request can change them.
* The customer's address is **never** used as From.
* Acknowledgement wording and subject are exactly as approved (`We’ve received your enquiry — HM UNIQUE`).
* An enquiry counts as *accepted* only when the notification email was handed to the provider successfully.
  If the **acknowledgement** fails, the enquiry is still reported as accepted (`acknowledgement:"failed"`) and the
  customer is told the enquiry was received, plus that a confirmation email could not be sent — they are never asked to resubmit.
* Server-side validation and limits (name 100, company 150, email 254, phone 7–15 chars, city/state 80, product 150,
  quantity 60, message 3000; category/subject allow-lists; 16 KB body cap), HTML escaping of all customer text,
  header-injection stripping, honeypot field, minimum-fill-time check, per-IP rate limit (5 per 10 min),
  duplicate protection (idempotency key + content fingerprint), optional Cloudflare Turnstile.

## What YOU must configure (nothing is configured yet)
1. **Email provider account.** The code uses [Resend](https://resend.com) (`RESEND_API_KEY`). Another provider
   can be used by replacing the single function `sendViaResend()`. *Choosing/paying for a provider is your decision.*
2. **A verified sender on your domain**, e.g. `HM UNIQUE <enquiries@hmunique.com>`. The provider will give you
   DNS records (SPF/DKIM) to add for `hmunique.com`. **This is a DNS change — it was deliberately not made.**
   Do it only when you decide on DNS/Cloudflare; mail from an unverified sender will be rejected or land in spam.
3. **Deploy the Worker** (Cloudflare account required):
   ```
   cd backend/enquiry-worker
   cp wrangler.toml.example wrangler.toml      # edit ALLOWED_ORIGINS
   npx wrangler secret put RESEND_API_KEY
   npx wrangler secret put ENQUIRY_FROM         # or put ENQUIRY_FROM in [vars]
   npx wrangler deploy
   ```
4. **Variables**

   | Name | Type | Required | Meaning |
   |---|---|---|---|
   | `RESEND_API_KEY` | secret | yes | Provider API key. Never put it in website files. |
   | `ENQUIRY_FROM` | var/secret | yes | Verified sender, e.g. `HM UNIQUE <enquiries@hmunique.com>` |
   | `ALLOWED_ORIGINS` | var | yes | Exact site origin(s), comma-separated, e.g. `https://www.hmunique.com` (add the apex/preview origin if used) |
   | `ENQUIRY_KV` | KV binding | recommended | Makes rate limiting + duplicate protection work across Worker instances |
   | `TURNSTILE_SECRET` | secret | optional | Enables Cloudflare Turnstile verification (also needs the widget added to the forms — a separate decision) |
   | `REQUIRE_ORIGIN` | var | optional | `"true"` rejects requests that carry no Origin header |

   Until `RESEND_API_KEY` and `ENQUIRY_FROM` exist the Worker answers `503 not_configured` and sends nothing.
5. **Point the website at it**: edit `js/enquiry-config.js` and set `ENQUIRY_ENDPOINT` to the Worker URL
   (e.g. `https://hmunique-enquiry.<account>.workers.dev/api/enquiry`, or a custom route). While it is `""` the forms
   honestly say submission is not connected and never show success.
6. **Test with owner-approved addresses only**: submit once from each form with your own test address and confirm
   (a) the Gmail notification, (b) the CC at business@hmunique.com, (c) the acknowledgement at the test address,
   (d) that Reply on the notification goes to the test address.

## Tests in this folder
`node --test test/worker.test.mjs` — 27 tests with the provider **mocked** (the mock emulates Resend's documented
Idempotency-Key behaviour). They verify the server logic only; they do not prove any real email was delivered or how the
real provider behaves.

## Known limits
* Rate limiting and duplicate protection are only as strong as their storage — see the next section. **Bind `ENQUIRY_KV` before launch.**
* Privacy policy and Terms pages are not published; the forms keep the existing consent checkbox. Resolve before production launch.
* Replies/bounces go to whatever mailbox receives the notification; no inbound processing is implemented.

## Rate limiting, duplicate protection and retries — what actually holds

Both depend on where the Worker keeps its small records (`rl:` counters, `idem:`/`fp:` results, `st:` progress).

| Situation | Without `ENQUIRY_KV` (default fallback) | With `ENQUIRY_KV` bound |
|---|---|---|
| Storage | In memory of one Worker isolate | Workers KV, shared by all instances/locations |
| Across several Worker instances / data centres | **No.** Each instance has its own counters and its own record of past enquiries | Yes, subject to KV's eventual consistency (a write can take up to ~60 s to be visible in other locations) |
| After a restart, redeploy or idle eviction | **Lost.** Counters reset and past enquiries are forgotten | Kept until the TTL (rate limit 10 min, content fingerprint 2 min, finished enquiry 24 h) |
| Rate limit (5 per IP per 10 min) | Best effort only; an attacker who reaches different instances is not limited | Enforced per IP, but approximate: KV has no atomic increment, so a burst of simultaneous requests can slip a few extra through |
| Duplicate double-click / re-send of the same enquiry | Caught only if it hits the same instance | Caught across instances (after KV propagation) |

For stronger guarantees than KV can give, add a Cloudflare **WAF rate-limiting rule** on the endpoint (edge-enforced,
dashboard setting — not configured) or move the counter to a Durable Object (not implemented). Neither is required to launch.

**Independent of the Worker's own storage, the email provider is the last line of defence against duplicate notifications.**
Every send carries an `Idempotency-Key`. Resend documents that the same key with the same payload returns the original
result without sending again (keys are kept 24 h), the same key with a different payload returns 409, and a concurrent
request with the same key returns 409 until the first finishes. Resend's page does not say whether *failed* requests are
cached under a key — that is **unverified**, and the logic below is written not to depend on it.

### How a retry avoids a second notification
An *enquiry* is identified by the browser's one-per-enquiry `submissionId` **plus a hash of the content**. The browser keeps the
same `submissionId` for every retry of the same unsent enquiry and makes a new one after a confirmed success.

* Notification and acknowledgement bodies contain **nothing that changes between attempts** (the reference is derived from the
  key; there is no timestamp), so a retry is a byte-identical request and the provider can recognise it. (An earlier version
  embedded a per-attempt time, which would have made every retry of an in-doubt send fail with 409 — fixed.)
* After the notification is handed over, a progress record (`st:`) says so. If anything later goes wrong (acknowledgement fails,
  the final record cannot be written, the Worker dies), a retry **skips the notification**.
* If even that record is missing, the retry re-sends the *identical* request under the *same* provider key, so the provider
  does not deliver it again.
* Provider answered with a definite **4xx** (nothing was sent): the next attempt uses a **fresh** provider key, so a cached
  rejection cannot block it. **5xx / network error / timeout** (outcome unknown): the **same** key is kept, because the email may
  already have gone out.
* **Acknowledgement fails after the notification succeeded:** the enquiry is answered `accepted` with `acknowledgement:"failed"`,
  the result is stored, and a retry returns that stored result without sending anything. The acknowledgement is **not** retried
  automatically (there is no queue); the failure is written to the Worker log with the reference.
* A storage error *after* an email was sent is logged and swallowed — it never turns an accepted enquiry into an error.
* If the person **edits** the text after a failure it is treated as a new enquiry (new key) and is sent; if the first attempt
  had in fact been delivered, the team may receive two similar emails. That is intentional (different content).
* A delivery failure (502) **refunds** the rate-limit slot, so failed attempts do not lock a customer out of retrying.
* Residual risks: two identical requests arriving truly simultaneously on different instances are only separated by the
  provider's 409; and if Resend does cache a rejected request under a key, a retry after a 5xx can keep failing until the
  24 h key expiry (the customer then sees the retry message with the phone/email fallback).
