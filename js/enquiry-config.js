/**
 * enquiry-config.js — the ONLY place the enquiry endpoint is set.
 *
 * ENQUIRY_ENDPOINT is the full https:// URL of the deployed enquiry Worker
 * (backend/enquiry-worker, e.g. "https://hmunique-enquiry.<account>.workers.dev/api/enquiry"
 * or a custom route). It is a public URL, not a secret. Leave it "" until the backend is deployed:
 * while empty, the forms never claim to have sent anything — they show an honest
 * "not connected" message and keep the visitor's entries.
 */
export const ENQUIRY_ENDPOINT = "https://hm-unuique.hmunitecenterprises02.workers.dev/api/enquiry";
