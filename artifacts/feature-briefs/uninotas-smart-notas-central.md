# UniNotas Smart Notas Central — Feature Brief / Story Decomposition

## Artifact Role

- **Why this brief exists now:** transforming Monitor de Notas into UniNotas combines product identity, external API adoption, fiscal-account separation, secret handling, data ownership, user experience, and high-risk fiscal write operations. Those concerns require decomposition before any tactical implementation TODO can be safe.
- **What this brief is not:** a canonical module document, project constitution, system roadmap, tactical TODO, approval gate, or implementation authority.

## Source Idea / Request

- Expand the current monitor into **UniNotas**, using the Smart Notas API as the complete note-data source while retaining PostgreSQL only for integration failures.
- Support two fiscal contexts from the outset: **Unifast** and **Prosperar**.
- Prepare a local environment surface for the corresponding API credentials without persisting secret values in Foundation or Git.

## Problem / Desired Outcome

- **Problem:** the canonical product reconstructs its note experience from PostgreSQL `logs`, while the desired UniNotas product must read every fiscal note and document from Smart Notas and use `logs` only to diagnose integration failures.
- **Desired outcome:** establish a coherent UniNotas architecture in which Smart Notas is the complete note-data source, PostgreSQL is a separate failed-attempt evidence source, and users always know which fiscal emitter and source they are viewing.
- **Why now:** this source split and Unifast/Prosperar credential isolation must be designed before API adapters, persistence changes, routes, or UI are implemented.

## Confirmed Direction

- **Fiscal context:** Unifast and Prosperar are separate `FiscalIssuerContext` values only, not business tenants or organizations.
- **Delivery:** capabilities will be introduced in stages, beginning with read-only note/report access.
- **Confirmed flow:** FastPay (Routerfy) originates the sale/emission request, n8n performs the automation, and Smart Notas processes it. UniNotas reads notes directly from the Smart Notas API; PostgreSQL retains integration failures only.
- **Source ownership:** Smart Notas API owns the complete note read model—list, detail, status, fiscal fields, PDF/DANFE, XML, and approved reports. PostgreSQL `logs` owns only failed-attempt evidence that may not have produced a provider note.
- **Note identity:** UniNotas maps an opaque `noteId` to `(provider, fiscalContext, idInterno)`. `ref_id` belongs only to error occurrences; `idTransacao`/`idCompra` is secondary correlation, never note identity.
- **Projection/cache:** the first target has no persistent local note mirror. It reads Smart Notas and keeps only a bounded in-memory session cache so `Geral -> Erros -> Geral` can restore recent rows immediately and revalidate stale entries in the background.
- **Context-first navigation:** the first delivery requires one active fiscal context, Unifast or Prosperar, and has no aggregate “Todos” list. Provider pagination remains isolated per selected context.
- **State separation:** Smart Notas fiscal status, integration-error category, document readiness, and UniNotas workflow are independent states. `OperationalCase` is the sole owner of `ABERTO|RESOLVIDO|IGNORADO` and treatment history, containing one optional API note and zero or more integration-error occurrences while requiring at least one source anchor.
- **Integration errors:** FastPay/n8n/Smart Notas validation, duplicate/already-issued, transport, and provider failures captured in PostgreSQL remain permanent scope. Deterministically linked errors appear separately on note detail; unlinked errors remain in a dedicated operational queue.
- **Current versus target truth:** canonical Foundation continues to describe the running `logs`-based system until a separate canonical change and tactical implementation are approved. This brief records product direction, not completed migration or implementation authority.

## Constraints / Non-Goals

- **Constraints:** preserve current running behavior until superseded by approved decisions; never store tokens in tracked files or Foundation; call Smart Notas only from the backend; verify list/detail/document shapes rather than inferring them; keep Unifast and Prosperar data, credentials, cache keys, audit records, and UI context distinguishable.
- **Non-goals:** this brief does not rename the product canonically, perform fiscal mutations, migrate data, implement API clients, create database schema, or redesign the external FastPay/n8n automation.

## Canonical Touchpoints

- **Constitution impact:** `yes` — the desired direction establishes Smart Notas as the note authority, narrows PostgreSQL to integration errors, corrects the external pipeline topology, and introduces fiscal issuer context without business tenancy.
- **Roadmap impact:** `yes` — the transformation requires staged discovery, canonical correction, API-backed note reads/documents, error-boundary migration, UI context, guarded mutations, and rollout.
- **Primary module candidates:** boundaries pending; likely distinct fiscal-notes, integration-occurrences, and operational-cases owners, subject to explicit scope-policy approval.
- **Secondary module candidates:** `foundation_documentation/modules/events-and-classification.md`, `foundation_documentation/modules/treatments-and-history.md`, `foundation_documentation/modules/identity-and-team.md`, `foundation_documentation/modules/runtime-and-deployment.md`, and `foundation_documentation/modules/operational-monitoring.md`.

## Evidence / References

- User direction recorded on 2026-09-24: UniNotas central using Smart Notas with separate Unifast and Prosperar accounts.
- User decisions confirmed on 2026-09-25: fiscal contexts only, staged read-only-first delivery, and separation among API fiscal state, integration-error state, and UniNotas workflow state.
- User clarification confirmed on 2026-09-25: the operating flow is `FastPay (Routerfy) -> n8n -> Smart Notas`; the complete UniNotas note base comes from the API, and PostgreSQL is retained only for integration failures.
- User confirmation recorded on 2026-09-25: the source-ownership consequences were accepted explicitly, including API-only note data, error-only PostgreSQL use, non-note `ref_id`, deterministic-only error correlation, and no persistent local note mirror in the first target.
- User decision recorded on 2026-09-25: the first delivery uses two selectable fiscal contexts without an aggregate list; API data loads on entry/manual refresh, while a transient navigation cache preserves recent `Geral` data when the operator visits `Erros` and returns shortly afterward.
- User confirmation recorded on 2026-09-25: pipeline attempt errors remain operationally valuable, and `OperationalCase` groups fiscal problems and/or pipeline occurrences while owning the independent UniNotas workflow state.
- Official documentation: `https://app.smart-notas.com/api/docs`.
- Official OpenAPI document: `https://app.smart-notas.com/docs/api-docs.json` (`OpenAPI 3.0.0`, API version `1.0.0`).
- OpenAPI SHA-256 observed on 2026-09-24 America/Sao_Paulo: `cc2a415962dcff00b7d91d3a1bfe99544ec3bd1543b2e5f9d93df1b8ce686502`.
- OpenAPI fingerprint rechecked unchanged on 2026-09-25 while completing the current-consumer and API-note/error-store matrices.
- Redacted live read evidence recorded on 2026-09-25: both token/CNPJ contexts returned `200` for company, note list, note detail, PDF, and NFS-e fiscal report probes; each company response matched its configured CNPJ; no credential, identifier, business value, personal value, document URL, or response payload was persisted.
- Live shapes confirm numeric pagination; string-heavy note DTOs; nullable fiscal fields; `DD/MM/YYYY` dates; ISO-like nullable competence; decimal values encoded as strings; and endpoint-specific wire-type differences for report `modelo`/`finalidade`.
- Current product authority: `foundation_documentation/project_mandate.md`, `domain_entities.md`, `project_constitution.md`, `system_roadmap.md`, and the existing module set.

## Ambiguities To Resolve Before TODO

| ID | Ambiguity | Why It Matters | Current Evidence | Handling (`resolve now\|carry as TODO assumption\|block`) |
| --- | --- | --- | --- | --- |
| `AMB-01` | Exact Smart Notas company binding for the independent Unifast and Prosperar credential contexts | Determines credential isolation, rotation, and adapter validation | Distinct token identities are validated; both configured context pairs returned `200` from `GET /empresa`, and each normalized response CNPJ matched its configured CNPJ | `resolved` — maintain independent backend-only token/CNPJ resolution per `FiscalIssuerContext` |
| `AMB-02` | Smart Notas versus PostgreSQL source ownership | Changes every note read, error view, and module boundary | User confirmed that all UniNotas note data comes from Smart Notas API and PostgreSQL remains only for integration failures | `resolved` — API is the complete note source; `logs` is the error-evidence source |
| `AMB-03` | Whether “account” is a fiscal emitter, organization, credential profile, or user-visible workspace | Prevents accidental tenancy and authorization design | User confirmed that Unifast and Prosperar are different fiscal contexts only | `resolved` — use `FiscalIssuerContext`, not tenancy |
| `AMB-04` | Read-only first release versus immediate issue/cancel capability | Write operations carry fiscal, authorization, idempotency, and audit risk | User confirmed staged delivery and agreed to proceed in parts | `resolved` — read-only first; mutations are separately approved slices |
| `AMB-05` | Polling, rate limits, idempotency, sandbox, and webhook availability | Determines reliability and operational cost | Published API exposes asynchronous issuance and no webhook or rate-limit contract | `carry as TODO assumption` and request provider confirmation |
| `AMB-06` | Canonical product rename and repository identity | A rename affects mandate, modules, runtime labels, branding, and delivery topology | Current canonical identity remains Monitor de Notas / `MonitorDeNotas` | `block` until a dedicated strategic decision is approved |
| `AMB-07` | Product mapping for context-scoped Smart Notas `idInterno` | Current routes use error `ref_id`, while target note/detail/document routes must use API identity safely | Public API uses `idInterno` under token+CNPJ scope | `resolve now` — define opaque `noteId` mapping and context-safe route behavior without relying on `logs` |
| `AMB-08` | Whether Smart Notas exposes every note field required by the target UI | The API must now supply customer, sale, issuer, status, and document data instead of successful log payloads | Redacted list/detail/report shapes are captured for both contexts; nullable fields and endpoint-specific type differences are recorded | `partially resolved` — normalized DTO candidate exists; confirm target UI field selection and keep defensive decoding |
| `AMB-09` | API refresh, pagination, DANFE readiness, and URL lifetime | Determines context list behavior, freshness, retry, cache safety, and user-visible errors | selected-context pagination, no initial aggregate list, manual refresh, and bounded in-memory stale-while-revalidate cache are confirmed; API has no webhook, PDF may return `202`, and URL lifetime is unspecified | `partially resolved` — tactical TTL/cap and request-race guards remain; polling, persistent cache, and document proxy choice stay deferred |
| `AMB-10` | Whether pipeline failures that never created a provider note remain product scope | The Smart Notas API cannot return failures that occurred elsewhere in the automation | User confirmed the external pipeline remains long-lived and these errors are operationally valuable | `resolved` — retain as permanent integration-error occurrences, separate from API note and document state |
| `AMB-11` | Which component persists integration failures and which rows qualify | Affects error completeness, ownership, observability, schema change coordination, and incident diagnosis | PostgreSQL is confirmed as error-only target scope, but this repository does not evidence the external writer or exact failure filter | `carry as labeled target unknown` — it does not block the canonical Current/Target split while no writer/filter is asserted; it blocks the later error-adapter implementation contract |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision (`create-now\|defer\|split-further\|merge-with-other`) | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ST-01` | Complete provider discovery and the API-note/error-store separation contract | `pending boundary decision` | identity, runtime, events, treatments | Versioned endpoint/auth matrix, fiscal-context model, API note identity/DTO/pagination/freshness, error-only PostgreSQL boundary, source ownership, and unresolved questions exist without secrets | Official spec fingerprint, current-consumer inventory, redacted API probes for both contexts, and redacted failed-row shapes | `create-now` | quotas, UX field selection, tactical cache bounds, URL lifetime, and error-writer ownership remain follow-up evidence | Context-first navigation and transient caching are confirmed; current strategic capped TODO still owns the no-code slice |
| `ST-02` | Redefine the product canonically as UniNotas and correct the source topology | project-level strategic authority | all modules | Mandate, constitution, roadmap, entities, scope policy, and modules distinguish current runtime from target architecture and agree only on evidenced FastPay, n8n, Smart Notas, PostgreSQL, and UniNotas responsibilities | Foundation validation and decision review | `create-now` | confirmed source split and fiscal contexts; the unknown external error writer/filter must remain explicitly unknown | No runtime implementation; governed by `todos/active/process/TODO-uninotas-canonical-foundation-transition.md` |
| `ST-03` | Read notes and documents safely from both fiscal contexts | future Smart Notas note integration owner | identity, runtime, UI consumer | Backend exposes API-backed list/detail/PDF contracts, rejects cross-context access, and handles provider pagination plus `200/202/401/403/404`; frontend uses bounded session-memory stale-while-revalidate cache without successful-log fallback or persistent note storage | Contract/unit/integration tests plus browser/race journeys for list, detail, context switch, tab return, stale failure, repeated refresh, logout during request, and DANFE | `split-further` | `ST-01`, `ST-02`, quotas, note identity, UI field selection, URL-lifetime, authorization, and proxy/redirect decisions | Context binding and representative live shapes are evidenced; read-only API note delivery remains the first implementation stage |
| `ST-04` | Let operators recognize and switch Unifast versus Prosperar | future UniNotas UI owner | identity, integration | Every list/detail/report view has an unambiguous active issuer; no initial aggregate list exists; cache/request keys cannot leak state across contexts | Browser journey proves switch, URL/back behavior, filter preservation, cache isolation, and error states | `defer` | `ST-03` and selector/default-context design | Visual distinction must supplement, not replace, textual identity |
| `ST-05` | Issue, track, download, and cancel fiscal notes | future fiscal operations owner | identity, audit, runtime | Each mutation has authorization, idempotency, audit, confirmation, asynchronous status, and recovery contracts | Provider sandbox/controlled integration plus mutation browser journey | `split-further` | Provider sandbox, idempotency and cancellation rules | High-risk separate approval conversation |
| `ST-06` | Operate UniNotas reliably in deployed environments | runtime and deployment | monitoring, integration | Secret injection, rotation, timeouts, retries, circuit behavior, observability, and rollout are explicit | CI-equivalent, deployment, and operational evidence | `defer` | Earlier stories and Railway topology | Tokens never enter client bundles or tracked artifacts |
| `ST-07` | Preserve actionable integration failures without corrupting API note state | future integration-occurrence owner | notes, treatments, runtime, monitoring, UI | Only failed rows enter the error boundary; sanitized issues are deduplicated, context-resolved, deterministically linked or explicitly unlinked, actionable through local cases, and never overwrite Smart Notas fiscal/document state | Synthetic/controlled failed-attempt fixtures plus success-row exclusion, cross-context correlation, quarantine, deduplication, case workflow, and UI journey tests | `split-further` | Correlation evidence, writer/filter ownership, and retention/raw-access policy | Long-term capability while FastPay/n8n originate and automate emissions |
| `ST-08` | Let operators manage one coherent work case across API notes and integration errors | future operational-cases owner | notes, integration occurrences, identity, audit, UI | A case owns `ABERTO|RESOLVIDO|IGNORADO`, treatment history, optional API-note link, error membership, authorship, and safe merge/split behavior without changing source facts | Domain/unit tests plus browser journeys for linked note, unlinked failure, repeated failures, reopen, merge/split, and cross-context rejection | `split-further` | `ST-03`, `ST-07`, authorization policy, and existing-treatment migration | Confirmed domain boundary; implementation requires its own approved TODO |

## Retire This Brief When

- The strategic discovery ledger has resolved the provider/account questions and the initiative has been decomposed into approved tactical TODOs with canonical module ownership.
