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

- **Current delivery stage:** `Pending`
- **Implementation status:** evolução aprovada; implementação de bootstrap/reconciliação em andamento.
- **Qualifiers:** `Approved — implementation in progress`
- **Next exact step:** executar o intake determinístico e implementar o contrato renovado com testes fail-first.

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

- **Contract status:** `approved`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on material deviation`
- **Comparison mode:** `working_tree against frozen root baseline`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `671aa2266e3585bb3121fba81f731c8976de69c9` | `working_tree` |
| `uninotas-foundation` | `foundation_documentation` | current untracked tactical TODO/feature-brief workspace state | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/schema.prisma` | `M` | durable bootstrap/rolling sync metadata |
| `MonitorNotes` | `backend/prisma/migrations/**` | `A` | additive compatibility migration |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | bootstrap, rolling reconciliation, fallback, response metadata and tests |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | public freshness/source metadata |
| `MonitorNotes` | `frontend/src/notas/normalizacaoFiscal.ts` | `M` | validate freshness/source metadata |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | disclose stale/local state |
| `MonitorNotes` | `frontend/src/**/*.spec.ts*` | `A|M` | frontend contract/render regression evidence if required |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-read-model.md` | `M` | approval, decisions and delivery evidence |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-note-read-model.md` | `M` | stable scope synchronization if needed |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A|M|D|R` | secrets/local environment are excluded |
| `MonitorNotes` | `backend/src/logs/**` | `A|M|D|R` | external logs remain outside the read model |
| `MonitorNotes` | `backend/src/fiscal-notes/smart-notas.adapter.ts` | `M` | provider route/auth contract is unchanged |
| `MonitorNotes` | `Dockerfile`, `railway.json`, `.github/**` | `A|M|D|R` | deployment/CI topology is outside this evolution |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| none at approval | n/a | strict expected paths frozen above | classify before delivery | required for material expansion |

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

- `backend/prisma/schema.prisma`: models `FiscalNoteCache` and `FiscalNoteSync`.
- `backend/prisma/migrations/20260929120000_fiscal_note_read_model/migration.sql`: additive tables and workload indexes.
- `backend/src/fiscal-notes/fiscal-note-cache.service.ts`: per-context/date coverage, resumable sequential sync, idempotent batched upserts and local list/export reads.
- `backend/src/fiscal-notes/fiscal-notes.service.ts`: local cache path for list/export without document filter; detail/document and document-filtered operations remain provider-backed.
- `backend/src/fiscal-notes/fiscal-note-cache.service.spec.ts`: fresh coverage reuse and provider-call reduction test.
- No frontend, `logs`, credentials or deploy files changed.

## Validation Evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Prisma client generation | passed | `npm run prisma:generate` — Prisma Client 6.19.3 |
| Prisma schema validation | passed | `npx prisma validate` |
| Backend build | passed | `npm run build` |
| Backend lint | passed | `npx eslint "src/**/*.ts"` |
| Backend test suite | passed | `npx jest --runInBand` — 16 passed suites, 358 passed tests, 2 expected skips |
| Cache behavior | passed | `fiscal-note-cache.service.spec.ts` |
| Diff whitespace | passed | `git diff --check` |
| Real PostgreSQL migration | pending | requires an explicitly authorized representative database |
| Local PostgreSQL migration | passed | `prisma db execute` + `prisma migrate resolve`; `prisma migrate status` reports schema up to date |
| Query plan/load benchmark | pending | requires representative redacted data and approved runtime |

## Current Closeout Status

- Local implementation is complete and provisional.
- Next exact step: after renewed approval, refine the fallback contract and execute the provider-failure/load evidence before implementation delivery.
- Deployment remains outside this TODO.

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| backend behavior | cache reuse and existing fiscal contracts | `cd backend && npx jest --runInBand` | implementation | `passed` | 16 passed suites, 358 passed tests, 2 expected skips | no real provider claim |
| backend static/build | Prisma schema, Nest wiring and TypeScript output | `cd backend && npx prisma validate && npx eslint "src/**/*.ts" && npm run build` | implementation | `passed` | exit 0 | lint is non-mutating |
| database | migration against representative PostgreSQL and query plans | approved database runner | Local-Implemented | `pending` | environment/owner not provided; no live mutation executed | required before delivery |
| runtime | repeated export after completed sync | authorized runtime load probe | Local-Implemented | `pending` | representative redacted dataset and provider smoke required | no production traffic |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| local implementation checkpoint | no PR, merge, deploy or promotion claim | `n/a` | no pipeline invocation in this turn | none | promotion remains outside this TODO checkpoint |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| source authority | `logs` used as fiscal cache/source | `passed` | cache service imports Smart Notas port and Prisma-owned tables only | none | `logs` remains external/read-only |
| freshness | silent stale fallback | `passed` | cache requires complete coverage within 15-minute freshness | none | stale coverage is revalidated |
| context isolation | cross-context identity collision | `passed` | Prisma compound unique key and context-scoped queries | none | no aggregation |
| provider traversal | unbounded traversal | `passed` | sync limits 20,000 rows/200 pages and is sequential | none | bounded implementation |
| database/runtime evidence | migration/load proof | `pending` | authorized PostgreSQL/runtime environment required | pending | blocks final delivery claim |

## Next exact step

Revisar a proposta de evolução com o usuário, registrar aprovação renovada e executar o `todo_authority_guard.py --pre-approval`. Até a aprovação renovada, não alterar código, schema, migrations, endpoints, jobs ou runtime.

## Blockers (Current)

- `PENDING_DATABASE_EVIDENCE`: migration, query plan, pool/connection budget, backup/restore and load evidence require an explicitly authorized PostgreSQL environment.
- `PENDING_PROVIDER_SMOKE`: first real sync/export must prove provider quota behavior without production PII in tests or logs.

## Historical Framing Notes

- `PENDING_APPROVAL`: o usuário ainda não aprovou o escopo, a autoridade do read model, a política de frescor e o caminho de sincronização.
- `PENDING_TOPOLOGY`: owner de migration, capacidade do PostgreSQL e estratégia de execução do sync ainda não estão confirmados.
