# UniNotas Fiscal Note Documents — Delivery Review Package

Derived, non-authoritative review package. The approved tactical TODO remains the source of truth.

## Frozen scope

- TODO: `todos/completed/features/TODO-uninotas-fiscal-note-documents.md`
- Product baseline: `release/uninotas-smart-notas@f2984b42010e63d61ccd6e63d47a6c2f63bbcd03`
- Foundation approval commit: `e5de4a3`
- Product topology: principal checkout, single code writer; no worktree or auxiliary checkout.
- Delivery adds authenticated, read-only, ephemeral SmartNotas PDF/XML URL resolution and a React disclosure on list/detail pages. It also enlarges the existing settings trigger to at least `44x44` with a glyph of at least `20px`.
- Out of scope: persistence, proxying document bytes, cache, new dependency, environment variable, Railway/Docker change, deploy, merge, and settings behavior changes beyond trigger geometry.

## Public contract

| Producer | Authentication/authorization | Success contract | Consumer |
| --- | --- | --- | --- |
| `GET /api/v1/notas/:noteId/documentos/pdf` | valid JWT plus `ADMIN|GESTOR|ANALISTA|LEITOR`; signed context-bound note ID | `200 {documentType:"pdf",availability:"available",url}` or `202 {documentType:"pdf",availability:"pending",url:null}` | `AcoesDocumento` on list and detail |
| `GET /api/v1/notas/:noteId/documentos/xml` | valid JWT plus `ADMIN|GESTOR|ANALISTA|LEITOR`; signed context-bound note ID | `200 {documentType:"xml",availability:"available",url}` or `202 {documentType:"xml",availability:"pending",url:null}` | `AcoesDocumento` on list and detail |

Both routes return `Cache-Control: private, no-store`, `Pragma: no-cache`, and `X-Content-Type-Options: nosniff`. Provider URLs must be HTTPS, default port only, contain neither userinfo nor fragment, be no longer than 8 KiB, and have the exact origin `files.smart-notas.com` or `storage.smart-notas.com.br`. Provider response bodies are bounded to 16 KiB. URLs are not logged, cached, persisted, or rendered as text.

## Frontend / Consumer Matrix

| Producer surface | Consumer status | Evidence |
| --- | --- | --- |
| PDF resolution route | implemented on fiscal list and detail | `frontend/src/componentes/AcoesDocumento.tsx`; browser journey in `frontend/e2e/notas.mjs` |
| XML resolution route | implemented on fiscal list and detail | `frontend/src/componentes/AcoesDocumento.tsx`; browser journey in `frontend/e2e/notas.mjs` |
| `available` response | opens a new context with `noopener,noreferrer`; offers a safe fallback link when blocked | component assertions and browser popup-blocked case |
| `pending` response | visible pending feedback without external effect | browser pending case |
| provider/application error | stable user-facing feedback without exposing upstream payload/URL | controller/adapter tests and browser error case |
| settings trigger geometry | existing consumer preserved; only size changed | desktop/mobile browser geometry assertions |

No producer in this package is intentionally consumer-less; no waiver is used.

## Changed implementation surfaces

- Backend: `backend/src/fiscal-notes/**`, plus `backend/README.md`.
- Frontend: `frontend/src/api/notas.ts`, `frontend/src/componentes/AcoesDocumento.tsx`, `frontend/src/notas/documentoFiscal.ts`, list/detail pages, `frontend/src/estilos/layout.css`, frontend tests, and `frontend/README.md`.
- No Prisma, environment, Docker, Railway, dependency-manifest, or CI change.

## Verification performed

| Boundary | Command/result |
| --- | --- |
| Backend focused | `npm test -- --runInBand fiscal-documents.spec.ts fiscal-notes.contract.spec.ts fiscal-notes.application.spec.ts` — 108 passed |
| Backend full | `npm test -- --runInBand` — 15 suites passed, 1 skipped; 341 tests passed, 2 skipped |
| Backend static/build | `npm run lint`; `npm run build` — passed |
| Frontend unit | `npm run test:notas` — passed |
| Frontend race | `npm run test:notas:race` — passed |
| Frontend static/build | `npm run lint`; `npm run build` — passed |
| Browser | fresh Vite build served at `127.0.0.1:4180`, then `npm run e2e:notas` with Chrome — `OK mocked fiscal/cache/privacy/session and legacy PATCH flows` |
| Diff hygiene | `git diff --check` — passed |

The browser journey explicitly covers one open disclosure, no prefetch, duplicate bursts of 5/10/20 with one accepted request/effect per burst, popup-blocked fallback, pending/error feedback, Escape and late-response suppression, row navigation separation, detail actions, keyboard focus, responsive list layout, and settings geometry.

## Test-first and failure evidence

- The new adapter document test was introduced before the implementation and failed compilation because the document port/adapter operation did not exist (`TS2352`), then passed after implementation.
- The fresh browser run found an inaccessible keyboard-focus selector and a mobile grid regression. Both were corrected before the final fresh browser pass.
- Fixtures are synthetic and local. There is no fallback to a live SmartNotas service or production data.

## Performance and concurrency position

- Backend lookup is exactly one direct provider call using the already decoded provider ID. It does not list, page-walk, filter in memory, call detail, or retry.
- UI policy is `drop duplicate`: while one document request is active, all document actions in that disclosure are disabled; repeated synchronous activations produce one request and at most one external effect.
- Closing, navigating, unmounting, or losing the owning disclosure aborts the request and suppresses late effects/messages.
- Residual operational risk: actual provider latency/quota remains a cutover concern; browser popup blocking is handled by a safe fallback link.

## Security position

- Risk is high because the feature handles fiscal-document capabilities, PII-adjacent identifiers, two account contexts, credentials, and external URLs.
- Controls under review: JWT/role guards, signed context-bound ID, credential isolation in backend, exact response envelopes, byte/URL bounds, strict URL allowlist, no-store/no-log/no-persistence, stable error mapping, rate/saturation/timeout/abort behavior, and `noopener,noreferrer` sinks.
- Review must challenge confused-deputy/context bypass, SSRF/open-redirect-like sinks, credential/URL leakage, body-size bypass, late effects, and rate/duplicate abuse.

## Deliberate exclusions and residual boundary

- No live provider smoke test is claimed; real credentials/provider latency/quota belong to cutover.
- No deployed Railway result is claimed; this package closes local implementation only.
- No database or RLS path changes; backend concurrency/idempotency and runtime load-stress lanes are not applicable under the approved pcv-1 classification.

## Round-01 resolutions

- The backend now rejects shorthand, single-slash, backslash, whitespace/control and other non-explicit HTTPS-authority document URLs, then returns only canonical `parsed.href`. The destination suite covers these forms and canonical default port behavior.
- Rejected frontend requests now apply feedback only while their signal and controller ownership remain current. Close, external close and unmount abort/release the request.
- Browser coverage now observes exact external URL/target/features, one request/effect for bursts 5/10/20, late resolve/reject suppression across close/reopen, navigation/unmount suppression, current-feedback preservation, and list/detail mobile disclosure bounds/focus.
- Fresh validation after fixes: focused backend document/contract/application suite passed 113 tests; backend lint/build passed; frontend lint/unit/build passed; fresh Chrome journey passed; formal race probe passed 9/9 attempts across burst levels 5/10/20 with three repetitions each.
- Resolution record: `triple-audit/round-01/resolution.md`.

## Round-02 resolution and security close

- Test-quality finding `TQA-DOC-R2-001` was resolved with measured, otherwise-valid JSON at exactly 16,384 and 16,385 bytes. The over-limit case crosses the boundary in multiple chunks without `Content-Length` and asserts stream cancellation; the focused 26-test adapter suite and lint pass.
- Security findings `SEC-DOC-01`, `SEC-DOC-02`, and `SEC-DOC-03` are resolved. In addition to strict/canonical URL parsing, the adapter bounds the canonical URL after percent-encoding; a Unicode-expansion regression proves that the public URL cannot exceed 8 KiB.
- The independent security gate is clean for local delivery. Provider content/latency/quota and actual deployed behavior remain cutover boundaries.
- Resolution record: `triple-audit/round-02/resolution.md`.

## Round-03 and delivery-gate state

- Round 03 found no performance issue and no blocking test-quality issue. Its only low assertion improvement now directly proves that initial render and disclosure open/switch perform zero document requests; a fresh Chrome journey passed afterward. Resolution: `triple-audit/round-03/resolution.md`.
- Full backend suite after URL/lifecycle corrections: 15 suites passed, 1 skipped; 346 tests passed, 2 skipped. Backend lint/build passed. Focused final adapter boundary suite: 26/26 passed with exact 16 KiB valid JSON, streamed overflow cancellation and canonical Unicode URL expansion.
- Frontend unit/lint/build and the existing cache/export race suite passed. Fresh browser journey passed after lifecycle/mobile/no-prefetch changes. Formal document race probe passed 9/9 attempts across levels 5/10/20 with three repetitions each.
- pcv-1 artifacts and canonical hashes: `artifacts/tmp/uninotas-fiscal-documents/pcv/eps.json` (`02da47841a3359aa0d9c3cfc0c7ebd28b52d2ccf063c44b7db04eae3aa7c3e9b`) and refreshed `frc.json` (`6e1c2212a1496a7e87b24ef6090ad180d42be424cd0fc56884d9ff3892fa6f59`).
- NestJS and React capability owners/scripts are ready; deterministic test-quality scan is low with no bypass. Rule-Spirit warnings are synthetic `.test`/loopback/parameterized-browser-runner literals, not product runtime targets. Verification-debt lexical high was manually adjudicated: no unchecked item, inline cleanup debt, waiver, or unowned residual exists; production smoke remains explicitly owned by cutover.
- Independent security confirmation is clean for local delivery. No unresolved P1/P2-equivalent finding or accepted debt remains from the multi-lane/security reviews.

## Final review round 01 and resolution

- The fresh final reviewer reproduced two medium lifecycle/accessibility defects: a delayed document request survived browser history navigation when both cached queries retained the same note, and Escape attempted to focus the trigger before its disabled state had committed to false.
- Both findings were fixed within the approved React lifecycle boundary. List ownership is now navigation-generation-bound and remounts the action owner on location changes; the disclosure/active owner is cleared after each transition. Focus restoration is deferred until the trigger is enabled.
- Browser coverage now warms two cached pages sharing the same note, starts delayed PDF resolution, navigates Back/Forward, and proves closure plus zero late external effect. It separately proves that Escape during a pending request aborts the active signal and restores focus.
- Fresh frontend lint/unit/build, the complete mocked browser journey, and the required race suite passed after these fixes. Resolution record: `final-review.round-01.resolution.md`.
- Fresh independent final-review round 02 returned zero findings and independently matched the served preview assets to the principal checkout before rerunning the complete intercepted browser journey. The final review supports `Local-Implemented / Provisional` and found no open P1/P2-equivalent issue. Evidence: `final-review.round-02.result.json`.
