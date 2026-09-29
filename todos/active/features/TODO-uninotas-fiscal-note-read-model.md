# TODO — Estabelecer read model local para notas fiscais e exportações

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Draft / Provisional`
- **Created:** `2026-09-29`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário
- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-read-model.md`
- **Story:** `ST-FISCAL-READ-MODEL`

## Lane and authority

- **Lane:** `Tactical TODO`
- **Complexity:** `big`
- **Primary profile:** `Operational / Coder`
- **Technical scope:** `nestjs, react, vite, postgresql, prisma`
- **Current work state:** `implementation`
- **Implementation authority:** concedida para o escopo original e para a evolução de bootstrap histórico único, reconciliação diária e fallback local, conforme evidências de aprovação abaixo.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented / Validated`
- **Implementation status:** bootstrap histórico, reconciliação diária, fallback local e divulgação de frescor implementados e validados localmente.
- **Qualifiers:** `Approved — local implementation validated; deployment smoke pending`
- **Next exact step:** versionar a entrega na branch de release e validar o primeiro bootstrap no ambiente de stage.

## Approval

- **Approval status:** `APROVADO`
- **Approved by:** usuário responsável pelo workspace
- **Approval evidence:** `APROVADO o escopo e as premissas recomendadas do TODO.`
- **Approval date:** `2026-09-29`
- **Approval scope:** `persistência derivada, sincronização resumível, leitura local condicionada para listagem/exportação, testes e documentação/evidência deste TODO; nenhuma mudança de deploy, credencial ou logs foi aprovada por esta evidência`.
- **Renewed approval evidence:** `APROVADO o fluxo de carga histórica única e reconciliação diária do TODO.`
- **Renewed approval date:** `2026-09-29`
- **Renewed approval scope:** bootstrap histórico único e resumível por contexto, reconciliação de hoje/ontem, fallback para a última projeção local completa, metadados de frescor, listagem/exportação local e manutenção de detalhe/PDF/XML no Smart Notas.

## Decision Baseline — Frozen After Approval

| ID | Decision | Baseline |
| --- | --- | --- |
| `D-RM-01` | Fiscal authority | Smart Notas remains the authoritative source; PostgreSQL stores a derived, rebuildable projection only. |
| `D-RM-02` | Read consumers | List and export may use local data only when coverage and freshness are valid; otherwise the system exposes an explicit unavailable/stale state. |
| `D-RM-03` | Detail | Full note detail remains provider-backed on demand in this slice; no silent detail fallback to stale local data. |
| `D-RM-04` | Context isolation | The unique identity is scoped by `FiscalIssuerContext + provider internal ID`; Unifast and Prosperar are never aggregated. |
| `D-RM-05` | Persistence | Store normalized fields required by list/export and synchronization metadata; do not store PDF/XML, ephemeral document URLs or unrestricted raw payloads. |
| `D-RM-06` | Synchronization | Use resumable, idempotent synchronization with bounded retry/backoff and per-context coordination. Initial full coverage may be slow; repeated covered reads are local. |
| `D-RM-07` | Freshness | A coverage snapshot is fresh for 15 minutes after a complete sync; requests outside that window revalidate through Smart Notas before local data is presented as current. |
| `D-RM-08` | Migration owner | Prisma 6.5.0 is the application schema owner, subject to migration-state verification and an explicit production migration owner before deployment. |
| `D-RM-09` | Existing logs | The external `logs` table is not written, copied into, reconciled with or used to populate this read model. |

## Approved evolution - provider failure fallback

The current provider-first contract is insufficient when Smart Notas returns a temporary `429`. The proposed evolution keeps Smart Notas as the fiscal authority and allows list/export to serve the last valid local projection while a controlled revalidation is pending.

This material change to freshness and failure semantics was approved by the user on `2026-09-29`.

| ID | Proposed decision | Boundary |
| --- | --- | --- |
| `D-RM-E01` | Stale fallback | List and export may return the last complete local coverage when the provider fails with a temporary limit/unavailability error; an empty cache must still return the provider error. |
| `D-RM-E02` | Background revalidation | Provider synchronization must not block the interactive list/export request after a valid local coverage exists; only one sync may run per context/date window. |
| `D-RM-E03` | Freshness disclosure | Responses using stale local data must expose source and cache age through an explicit contract/header; the UI must not present stale data as current. |
| `D-RM-E04` | Retry/cooldown | A provider `429` must trigger bounded backoff and a persisted cooldown, preventing immediate repeated full traversals after a failed sync. |
| `D-RM-E05` | Detail ownership | Detail, PDF and XML remain provider-backed and do not silently fall back to the summary projection. |

## Approved evolution - bootstrap plus rolling reconciliation

The proposed synchronization policy is narrowed to avoid traversing the entire historical period on every request:

- **Bootstrap:** perform one complete historical load per fiscal context, with resumable pages and an explicit `bootstrap_complete` state. Historical list/export reads are allowed only after this state is complete.
- **Rolling reconciliation:** after bootstrap, query Smart Notas only for the current date and the previous date, using the application timezone (`America/Sao_Paulo`), and upsert returned records to capture new notes and status changes.
- **Local consumers:** list and export read the complete locally stored projection, applying the requested filters in PostgreSQL. They do not re-traverse historical provider pages after bootstrap.
- **Provider-backed consumers:** detail, PDF and XML continue to call Smart Notas directly and do not use the summary projection as a silent fallback.

This proposal replaces the current per-request/per-period full coverage strategy and was approved for implementation on `2026-09-29`.

### Bootstrap and rolling acceptance criteria

- A context cannot be presented as historically complete until every bootstrap page has been persisted and the sync is marked complete.
- A failed bootstrap resumes from the last durable page checkpoint without deleting successful pages.
- After bootstrap, normal list/export requests do not call Smart Notas for historical date ranges.
- The rolling window upserts new records and status changes for today and yesterday without duplicating notes.
- A provider failure during rolling reconciliation preserves and serves the last complete local projection, with stale/source metadata.
- Contexts remain isolated; bootstrap and rolling state are independent for Unifast and Prosperar.
- Details, PDF and XML remain provider-backed even when list/export uses local data.

### Proposed acceptance criteria

- A provider `429` during revalidation does not fail list/export when a complete prior projection exists.
- An empty or incomplete projection never produces a successful empty result that hides the provider failure.
- The response identifies local/stale origin and cache age when fallback is used.
- Repeated requests during provider cooldown do not create repeated upstream page walks.
- The last valid projection is never deleted or replaced by a partial failed sync.
- Tests cover provider failure, stale fallback, empty cache, concurrent requests, cooldown and context isolation.

### Proposed scope expansion

- Backend: sync state machine, fallback read path, cooldown metadata and response metadata.
- Frontend: explicit stale/synchronizing provider state, only if the public response contract requires visual disclosure.
- Database: additive synchronization metadata only; no raw payload, PDF/XML or `logs` writes.
- Out of scope: changing the Smart Notas authority, changing credentials/quota, or silently using stale data for note detail/documents.

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-luna`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree authorization:** not requested; no worktree or auxiliary checkout may be created.
- **Profile:** `Operational / Coder`
- **Scope:** `nestjs, react, vite, postgresql, prisma`
- **Package-first result:** Delphi package query attempted, but unavailable because the environment has no executable `bash/WSL`; no new dependency will be introduced. Node capability audits for NestJS and Prisma returned `ready`.
- **Guard outcome:** `go`
- **Guard evidence:** `agent_role_routing_guard.py` executed with routine-executor, medium effort and primary-checkout-single-writer.

## Execution Plan — Approved Boundary

1. Verify current package, Prisma schema/migration state, fiscal module ownership and existing tests.
2. Add the derived relational contract and migration with context-scoped uniqueness, freshness/sync metadata and workload indexes.
3. Implement a backend synchronization application service with bounded pages, resume state, idempotent upsert, per-context coordination and explicit partial/failure states.
4. Route list/export through the read model only after coverage/freshness checks; preserve provider-backed detail and document flows.
5. Add contract, integration, concurrency and performance evidence; update frontend only for explicit stale/sync states required by the public contract.
6. Run project-owned build/lint/test and database migration checks, then update this TODO with evidence and residual risks.

### Scope-change rule

Changing detail ownership, adding a queue/worker platform, changing provider quotas, writing `logs`, adding raw-payload retention, or changing deployment topology requires renewed TODO approval.

## Context

Exportações grandes percorrem o Smart Notas e podem receber `429` do provedor. O projeto já possui PostgreSQL conectado, mas o Foundation estabelece que Smart Notas é a autoridade das notas e que `logs` é externo, somente leitura e destinado a evidências de integração. Este TODO avalia uma projeção derivada independente, sem transformar PostgreSQL em fonte fiscal primária.

## Contract boundary

- Smart Notas permanece a autoridade fiscal.
- A projeção local só pode servir dados com contexto, cobertura e frescor conhecidos.
- Ausência, atraso, lacuna, erro de sincronização ou status possivelmente desatualizado devem ser expostos como estado operacional; não podem produzir sucesso vazio.
- Unifast e Prosperar permanecem `FiscalIssuerContext` independentes.
- `logs` não participa da carga, reconciliação ou preenchimento da projeção.

## Scope candidates — pending decision baseline

- [ ] Definir a tabela/modelo derivado e a chave `(contextoFiscal, idInterno)`.
- [ ] Definir campos, nulabilidade, normalização, PII, retenção e eventual JSONB redigido.
- [ ] Definir sincronização inicial, incremental/resumível, retry/backoff e idempotência.
- [ ] Definir frescor, cobertura por filtro/período e critério de leitura local segura.
- [ ] Fazer listagem/exportação consultarem a projeção somente quando o contrato permitir.
- [ ] Manter detalhe completo e PDF/XML sob demanda, salvo decisão explícita em contrário.
- [ ] Definir migrations, índices, planos, pool, timeout, roles, backup e restauração.
- [ ] Cobrir concorrência entre sincronizações, exportações e mudanças de status.
- [ ] Medir ganho de latência e redução de chamadas ao provedor com dados representativos redatados.

## Out of scope

- Emissão, cancelamento, alteração ou qualquer endpoint mutável do Smart Notas.
- Escrita, normalização ou mudança de semântica da tabela externa `logs`.
- Cache de URLs de PDF/XML ou armazenamento indiscriminado de payloads com dados pessoais.
- Agregação entre contextos fiscais.
- Deploy Railway, mudança de credenciais/quota ou alteração do cutover Smart Notas já aberto.

## Canonical anchors

- `foundation_documentation/project_constitution.md`
- `foundation_documentation/modules/fiscal-notes-and-documents.md`
- `foundation_documentation/modules/events-and-classification.md`
- `foundation_documentation/modules/operational-monitoring.md`
- `foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-read-model.md`

## Architecture correction

- **Required:** `yes`.
- **Deviation being retired:** exportação/listagem dependem diretamente de paginação do provedor em toda operação.
- **Target steady state:** projeção local derivada e descartável, com Smart Notas como autoridade, sincronização observável e fallback fail-closed quando a cobertura não for válida.
- **Protection harness:** constraints/índices e migrations; testes de isolamento por contexto e idempotência; testes de frescor/lacuna; testes de plano e carga; guards de TODO e revisão de segurança/performance.

## Definition of Done — draft

- [ ] Decision Baseline congelada e aprovada.
- [ ] Ownership, schema, migration owner, retenção e rollback documentados.
- [ ] Sincronização resumível e idempotente implementada com limites e observabilidade.
- [ ] Listagem/exportação local só ocorre com cobertura/frescor válidos.
- [ ] Falha do provedor durante sync não apaga a última projeção válida nem a apresenta como atual.
- [ ] Contextos não vazam dados entre si.
- [ ] Migrations, testes, build, lint e validações de carga/planos passam.
- [ ] Evidências e guards de entrega do TODO passam; nenhuma alteração de deploy fica implícita.

## Validation plan — draft

- Contrato: unidade, integração, RLS/isolamento de contexto e regressão dos endpoints.
- PostgreSQL/Prisma: migration forward, estado limpo, backfill controlado, índices e `EXPLAIN` seguro.
- Concorrência: duas sincronizações do mesmo contexto, sync versus export e retry após interrupção.
- Performance: exportação pequena, média e grande usando dataset redatado representativo; medir chamadas upstream, duração, memória e conexões.
- Frontend: estados de carregando, stale, cobertura parcial, erro e exportação sem download incorreto.
- Segurança: PII, payload bruto, logs, autorização e ausência de segredo/identificador real nas evidências.

## Test Decisions — Frozen

| ID | Decision | Evidence lane |
| --- | --- | --- |
| `D-T01` | Test-first | Add fail-first cache-service tests for completed bootstrap reuse, failed-bootstrap resume, rolling today/yesterday reconciliation, stale fallback and empty-cache failure. |
| `D-T02` | Integration | Preserve Nest module wiring and service contract tests; detail/PDF/XML must continue to exercise the provider port directly. |
| `D-T03` | Concurrency | Concurrent requests for the same context share one in-process synchronization; durable sync checkpoints and compound database keys preserve idempotency across retries. |
| `D-T04` | Real infrastructure | Prisma validate/generate and the authorized local PostgreSQL are required; live Smart Notas traffic is excluded from automated tests. |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on material deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `671aa2266e3585bb3121fba81f731c8976de69c9` | `working_tree` |
| `uninotas-foundation` | `C:/Unifast/uninotas-foundation` | `a6d22e7` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/schema.prisma` | `M` | durable bootstrap/rolling sync metadata |
| `MonitorNotes` | `backend/prisma/migrations/**` | `A` | additive compatibility migration |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | bootstrap, rolling reconciliation, fallback, response metadata and tests |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | public freshness/source metadata |
| `MonitorNotes` | `frontend/src/notas/normalizacaoFiscal.ts` | `M` | validate freshness/source metadata |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | disclose stale/local state |
| `MonitorNotes` | `frontend/e2e/notas-unit.ts` | `M` | freshness/source parser regression evidence |
| `MonitorNotes` | `frontend/src/**/*.spec.ts*` | `A, M` | frontend contract/render regression evidence if required |
| `MonitorNotes` | `delphi-ai` | `M` | pre-existing workspace link reflects the separately approved Delphi helper commit; excluded from product staging |
| `MonitorNotes` | `foundation_documentation` | `M` | pre-existing Foundation workspace link reflects TODO evidence; excluded from product staging |
| `MonitorNotes` | `uninotas-foundation` | `T` | pre-existing tracked-gitlink versus workspace-symlink topology; excluded from product staging |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-read-model.md` | `M` | approval, decisions and delivery evidence |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-note-read-model.md` | `M` | stable scope synchronization if needed |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A, M, D, R` | secrets/local environment are excluded |
| `MonitorNotes` | `backend/src/logs/**` | `A, M, D, R` | external logs remain outside the read model |
| `MonitorNotes` | `backend/src/fiscal-notes/smart-notas.adapter.ts` | `M` | provider route/auth contract is unchanged |
| `MonitorNotes` | `Dockerfile`, `railway.json`, `.github/**` | `A, M, D, R` | deployment/CI topology is outside this evolution |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| workspace links `delphi-ai`, `foundation_documentation`, `uninotas-foundation` | noise / governed support topology | links predate this product implementation; Delphi and Foundation changes were separately authorized and versioned in their owning repositories | retain links locally; exclude them from MonitorNotes staging | already authorized by user during this TODO session |

## Assumptions preview

- O PostgreSQL atual é o banco da aplicação, mas a autoridade de migração e os limites de produção ainda precisam ser confirmados.
- Smart Notas não oferece snapshot transacional; uma sincronização não garante fotografia histórica sem contrato adicional.
- Status podem mudar no provedor; um cache estático não é aceitável sem política de revalidação.
- A tabela `logs` permanece fora deste modelo.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/skills/rule-postgresql-postgresql-data-integrity-always-on/SKILL.md` | schema, constraints, queries, indexes, transactions, pool, roles and recovery | keys, null semantics, bounded resources, safe SQL | guessed ownership, weak constraints, unbounded retries | load before schema/query implementation |
| `delphi-ai/skills/wf-postgresql-change-relational-contract-method/SKILL.md` | PostgreSQL relational contract and migration planning | owner, workload, rollout and rollback evidence | irreversible migration without compatibility plan | resolve before approval |
| `delphi-ai/skills/rule-prisma-prisma-schema-migration-always-on/SKILL.md` | Prisma schema/client may own the application model | pinned major, immutable history and generated state | mixed versions or reset-based delivery | verify owner/version before implementation |
| `delphi-ai/skills/wf-prisma-change-schema-migration-contract-method/SKILL.md` | Prisma model/migration/query boundary | expand/backfill/switch/contract and release ordering | treating generate/sync as production migration proof | classify path before implementation |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | backend sync/read/export application boundary | module ownership and explicit failure states | hidden provider fallback or cross-context access | ingest before backend changes |
| `delphi-ai/skills/wf-nestjs-change-application-boundary-method/SKILL.md` | NestJS module, service, job and endpoint changes | producer/consumer contracts and tests | bypassing application boundaries | ingest before backend changes |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | frontend freshness/export states may change | explicit stale/loading/error state and lifecycle safety | presenting stale data as current | conditional; ingest if UI changes |
| `delphi-ai/skills/wf-react-change-ui-boundary-method/SKILL.md` | React consumer/UI contract changes | consumer matrix and race-safe behavior | unbounded client cache or silent empty state | conditional; ingest if UI changes |
| `delphi-ai/skills/endpoint-performance-scrutiny/SKILL.md` | list/export query and provider-call performance | workload, latency, memory and call budgets | claiming speed without representative evidence | required before delivery |
| `delphi-ai/skills/runtime-load-stress-validation/SKILL.md` | representative sync/export load validation | bounded concurrency and failure behavior | production load or real PII fixtures | required before delivery claim |

## Implementation Evidence

- `backend/prisma/schema.prisma` and migration `20260929120000_fiscal_note_read_model` were reused without a new schema change; their compound identity and workload indexes already support the approved evolution.
- `backend/src/fiscal-notes/fiscal-note-cache.service.ts`: one resumable 365-day bootstrap per context, durable page checkpoint, shared fiscal-rate lease/pacing, 60-second persisted provider cooldown, 15-minute rolling reconciliation of today/yesterday, idempotent upserts and bounded local list/export reads.
- `backend/src/fiscal-notes/fiscal-notes.service.ts`: list/export use PostgreSQL when no document filter is present; detail, PDF, XML and document-filtered operations remain provider-backed.
- `backend/src/fiscal-notes/fiscal-notes.controller.ts`: CSV responses disclose local source, stale state and cache age through headers.
- `frontend/src/api/notas.ts`, `frontend/src/notas/normalizacaoFiscal.ts` and `frontend/src/paginas/ListaNotas.tsx`: metadata contract validation plus explicit partial/stale notices.
- `backend/src/fiscal-notes/fiscal-note-cache.service.spec.ts`: seven scenarios cover concurrent deduplication, one-time history, context isolation, 20,000-row local export, checkpoint resume after `429`, rolling reconciliation, cooldown fallback and empty-cache failure.
- No `logs`, credentials, provider adapter, deployment or CI files changed.

## Validation Evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Prisma client generation | passed | `npm run prisma:generate` — Prisma Client 6.19.3 |
| Prisma schema validation | passed | `npx prisma validate` |
| Backend build | passed | `npm run build` |
| Backend lint | passed | `npx eslint "src/**/*.ts"` |
| Backend test suite | passed | `npx jest --runInBand` — 16 passed suites, 364 passed tests, 2 expected skips |
| Cache behavior | passed | `fiscal-note-cache.service.spec.ts` — 7/7, including 20,000-row export in 55 ms in the deterministic in-memory harness |
| Frontend parser/cache checks | passed | `npm run test:notas` |
| Frontend build/lint | passed | `npm run build`; `npm run lint` |
| Diff whitespace | passed | `git diff --check` |
| Local PostgreSQL migration | passed | `prisma db execute` + `prisma migrate resolve`; `prisma migrate status` reports schema up to date |
| Local PostgreSQL query plan | passed | indexed backward scan on `(contexto_fiscal, scheduled_issue_date)` plus incremental sort for bounded export query |
| Capability audits | passed | NestJS, Prisma, React and Vite surfaces report `Overall outcome: ready` |
| Live stage load/provider smoke | pending | requires deployed stage runtime; no production/provider load was generated locally |

## Current Closeout Status

- Local implementation and CI-equivalent validation are complete.
- The first stage request may still traverse the 365-day bootstrap and can receive `429`; successful pages remain durable and the next attempt resumes after the cooldown instead of restarting at page 1.
- After `bootstrap_complete`, list/export are PostgreSQL-backed and only today/yesterday are reconciled every 15 minutes.
- Deployment remains outside this TODO; stage smoke and live provider quota evidence remain post-deploy checks.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `AC-RM-01` | `Bootstrap acceptance` | Context is complete only after every provider page is persisted. | unit contract | completed-bootstrap and pagination invariants in `fiscal-note-cache.service.spec.ts` | NestJS local | `passed` | completion is written after row-count validation |
| `AC-RM-02` | `Bootstrap acceptance` | Failed bootstrap resumes from the durable page checkpoint. | negative unit | `429` resume test proves provider pages `[1, 2, 2]` | NestJS local | `passed` | page 1 is not replayed |
| `AC-RM-03` | `Bootstrap acceptance` | Repeated historical list/export reads are local after bootstrap. | unit contract | one-time history test plus local export assertion | NestJS local | `passed` | provider call count remains two bootstrap pages |
| `AC-RM-04` | `Bootstrap acceptance` | Rolling reconciliation reads only today and yesterday every 15 minutes. | scheduler/unit | rolling test asserts `2026-09-28..2026-09-29`; `@Interval(900000)` wiring | NestJS local | `passed` | response remains nonblocking |
| `AC-RM-05` | `Fallback acceptance` | Provider failure preserves the last complete projection and discloses stale metadata. | negative unit+consumer | cooldown fallback test; frontend metadata parser/notices | NestJS/React local | `passed` | empty cache still propagates provider failure |
| `AC-RM-06` | `Isolation acceptance` | Fiscal contexts never aggregate. | schema+unit | compound unique key; foreign `prosperar` row excluded from `unifast` list/export | PostgreSQL/NestJS local | `passed` | every query includes `contextoFiscal` |
| `AC-RM-07` | `Provider ownership` | Detail, PDF and XML stay provider-backed. | regression suite | full fiscal contract/document suites | NestJS local | `passed` | cache is called only by list/export without document filter |
| `DOD-RM-01` | `Definition of Done` | Synchronization is bounded, resumable, idempotent and coordinated per context in the current single-replica topology. | unit+schema | 20,000 rows/200 pages; batched upsert; checkpoint; concurrent-read test | NestJS/PostgreSQL local | `passed` | distributed lease is required before horizontal scaling |
| `DOD-RM-02` | `Definition of Done` | Failure never deletes or silently presents the prior projection as current. | negative unit+UI | rolling failure/cooldown tests and stale UI notice | NestJS/React local | `passed` | partial bootstrap is explicitly labeled |
| `DOD-RM-03` | `Definition of Done` | Migration state, builds, lint, tests and indexed access path pass. | CI-equivalent | commands and results in Validation Evidence and local matrix | local | `passed` | no new migration was required for this evolution |
| `VAL-RM-01` | `Validation` | Backend full regression suite. | command | `npx jest --runInBand`: 16 passed suites, 364 passed tests, 2 expected skips | Node local | `passed` | includes detail/documents regressions |
| `VAL-RM-02` | `Validation` | Backend static, build and Prisma checks. | command | ESLint, Nest build, Prisma validate/generate/status all exit 0 | Node/PostgreSQL local | `passed` | schema is up to date |
| `VAL-RM-03` | `Validation` | Frontend parser, lint and production build. | command | `npm run test:notas`; `npm run lint`; `npm run build` | React/Vite local | `passed` | metadata malformed-shape rejection covered |
| `VAL-RM-04` | `Validation` | Bounded local export and indexed query path. | performance | 20,000 rows, zero provider calls, 55 ms harness; local PostgreSQL `EXPLAIN` | Node/PostgreSQL local | `passed` | HTTP stage p95/p99 deferred until deployment |
| `VAL-RM-05` | `Validation` | Security/privacy boundary remains unchanged. | manual adversarial review | diff review: no raw payload/PDF/XML/document field or secret persistence; no `logs` writes | local | `passed` | recipient document filter remains provider-backed |

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes | Gate Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| backend behavior | cache reuse and existing fiscal contracts | `cd backend && npx jest --runInBand` | implementation | `passed` | executed: 16 passed suites, 364 passed tests, 2 contract-defined skips | `passed` | full local fiscal regression |
| backend static/build | Prisma schema, Nest wiring and TypeScript output | `cd backend && npx prisma validate && npx eslint "src/**/*.ts" && npm run build` | implementation | `passed` | executed with exit 0 | `passed` | non-mutating static validation |
| frontend consumer | metadata parser, stale notices and production bundle | `cd frontend && npm run test:notas && npm run lint && npm run build` | implementation | `passed` | executed: parser checks, lint and Vite production build | `passed` | deterministic consumer contract evidence |
| database | migration state and local query plan | local PostgreSQL / Prisma | Local-Implemented | `passed` | executed: schema up to date and indexed export plan | `passed` | local PostgreSQL at `localhost:55432` |
| runtime | repeated export after completed sync | deterministic synthetic harness | Local-Implemented | `passed` | executed: 20,000 rows, zero provider calls, 55 ms | `passed` | bounded service-level workload |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes | Gate Status |
| --- | --- | --- | --- | --- | --- | --- |
| local implementation checkpoint | correctness, concurrency, privacy, performance and likely CI failures | `passed` | full diff review plus CI-equivalent commands | none | single-replica coordination constraint is accepted by design | `passed` |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes | Gate Status |
| --- | --- | --- | --- | --- | --- | --- |
| source authority | `logs` used as fiscal cache/source | `passed` | cache service imports Smart Notas port and Prisma-owned tables only | none | `logs` remains external/read-only | `passed` |
| freshness | silent stale fallback | `passed` | cache service and frontend metadata tests | none | stale coverage is disclosed and revalidated | `passed` |
| context isolation | cross-context identity collision | `passed` | Prisma compound unique key plus foreign-context unit fixture | none | no aggregation | `passed` |
| provider traversal | unbounded traversal | `passed` | sync limits 20,000 rows/200 pages and is sequential | none | bounded implementation | `passed` |
| database/runtime evidence | indexed query and bounded export | `passed` | local PostgreSQL `EXPLAIN`; deterministic 20,000-row export | no local HTTP p95/p99 | stage HTTP metrics are post-deploy evidence, not local implementation scope | `passed` |
| heuristic scan | hard-coded target and source bypass heuristics | `passed` | `rule_spirit_anti_pattern_scan.sh` over backend fiscal and frontend source | 20 review-only matches | `.test` emails and `127.0.0.1` are synthetic test fixtures; `dia.test` is a regular expression; zero warning/blocker | `passed` |

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `RM-REVIEW-01` | low | `by-design/no-action` | Keep in-process synchronization deduplication for current single-replica topology. | Approved scope did not change Railway topology; database upserts/checkpoints remain retry-idempotent. | closed | Add a distributed lease before horizontal scaling. |
| `RM-HEURISTIC-01` | info | `by-design/no-action` | Retain synthetic `.test` emails, ephemeral loopback servers and date regex. | Scanner matches test fixtures and regex syntax, not runtime domain configuration or personal data. | closed | Rule-Spirit scan manual classification, 2026-09-29. |

## Next exact step

Versionar a implementação na branch `release/uninotas`; depois do deploy de stage, observar o primeiro bootstrap e confirmar que listagem/exportação passam a operar localmente, sem nova travessia histórica.

## Blockers (Current)

- No blocker for local delivery.
- `PENDING_PROVIDER_SMOKE`: the first real stage bootstrap/export must prove provider quota behavior without exposing PII in logs.
- `PENDING_STAGE_LOAD`: record HTTP p95/p99 and error rate on stage after the projection is complete.
- Horizontal scaling is not part of the current Railway topology contract; synchronization deduplication is in-process and durable idempotency is database-backed. Introduce a distributed lease before running multiple API replicas.

## Historical Framing Notes

- `PENDING_APPROVAL`: o usuário ainda não aprovou o escopo, a autoridade do read model, a política de frescor e o caminho de sincronização.
- `PENDING_TOPOLOGY`: owner de migration, capacidade do PostgreSQL e estratégia de execução do sync ainda não estão confirmados.
