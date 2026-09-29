# TODO — Cancelar nota fiscal pelo MonitorNotes

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Draft / Pending Approval`
- **Created:** `2026-09-29`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário

## Context

O detalhe fiscal permite leitura e abertura de PDF/XML, mas não executa a operação oficial de cancelamento do SmartNotas. A evolução introduz uma mutação fiscal explicitamente confirmada e autorizada, preserva o `noteId` assinado como autoridade de rota e atualiza o read model derivado após sucesso conhecido.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md`
- **Primary story ID:** `ST-FISCAL-CANCEL-01`
- **Why this is the right current slice:** cancelamento, feedback, autorização, cache e posicionamento das ações formam um único fluxo de usuário; emissão, lote e reprocessamento permanecem histórias independentes.
- **Lane:** `Tactical TODO`

## Contract Boundary

- Este TODO define **WHAT** deve ser entregue; não autoriza implementação antes de `APROVADO`.
- SmartNotas permanece a autoridade fiscal e recebe exatamente uma tentativa por ação confirmada.
- O frontend nunca envia `idInterno`, CNPJ ou token; o backend decodifica o `noteId` opaco e escolhe credenciais pelo contexto assinado.
- Descobertas locais podem ser absorvidas somente se preservarem o mesmo fluxo, risco e superfície de aprovação.

## Implementation Intent

- Expor `POST /api/v1/notas/:noteId/cancelar` para `ADMIN|GESTOR|ANALISTA`.
- Chamar `POST /notas/{idInterno}/cancelar` no SmartNotas sem corpo e sem retry automático.
- Aceitar somente o envelope limitado `{cancelada:boolean,mensagem:string}` e projetar uma resposta pública pequena.
- Coordenar chamadas por `{contextoFiscal,providerIdInterno}` no backend, compartilhar a operação em voo e aplicar fence temporário quando o resultado externo for incerto.
- Atualizar o status local para `Cancelada` quando `cancelada=true` e impedir atomicamente que uma página antiga do rolling sync rebaixe esse estado terminal.
- Recarregar o detalhe após resultado conhecido ou incerto e invalidar o estado cliente relacionado.
- Organizar o cabeçalho como `[dados flexíveis] [Cancelar nota] | [⋮]`, com os três pontos no extremo direito.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Draft / approval required`
- **Next exact step:** congelar e publicar o baseline documental, executar os guards de planejamento e solicitar `APROVADO`.

## Active Work State

- **State:** `planning`
- **Implementation authority:** not granted
- **Execution topology:** `primary-checkout-single-writer`

## Scope

- `SCOPE-CAN-01`: contrato interno e adapter SmartNotas para cancelamento direto por contexto.
- `SCOPE-CAN-02`: endpoint autenticado com autorização apenas para `ADMIN|GESTOR|ANALISTA`.
- `SCOPE-CAN-03`: confirmação, single-flight, feedback e recarga segura no detalhe React.
- `SCOPE-CAN-04`: atualização best-effort da projeção local após sucesso fiscal confirmado.
- `SCOPE-CAN-05`: layout desktop/mobile com botão antes da divisória e menu no extremo direito.
- `SCOPE-CAN-06`: testes de contrato, autorização, concorrência, corrida, falhas externas e regressão de detalhes/documentos.
- `SCOPE-CAN-07`: documentação e evidência de entrega.
- `SCOPE-CAN-08`: decisão canônica limitada `FISC-CAN-01`, que abre exceção ao guardrail de provider writes somente para este cancelamento aprovado.

## Out of Scope

- Cancelamento em lote, motivo livre ou payload não publicado pelo SmartNotas.
- Cancelar notas cujo detalhe atual não esteja em `Autorizada`.
- Retry automático, promessa de exactly-once ou chave de idempotência inexistente no provider.
- Emissão, reprocessamento, edição, procedimento manual de prefeitura ou mudança de quota/credencial.
- Persistência de mensagem bruta, payload externo, token ou documento adicional.
- Deploy, promoção, alteração de Railway/CI ou escala horizontal.
- Garantia distribuída entre réplicas; a coordenação aprovada é process-local enquanto a topologia permanecer em uma réplica.

## Definition of Done

- [ ] `POST /api/v1/notas/:noteId/cancelar` usa o ID opaco assinado e rejeita `LEITOR`.
- [ ] O adapter envia `POST` sem body para o path oficial, com contexto/headers internos corretos, sem redirect/retry e com timeout interno não cancelado por disconnect posterior ao despacho.
- [ ] Somente resposta `200` com envelope exato, body de até 16 KiB e mensagem normalizada de 1..2048 code points cruza o trust boundary; falhas têm códigos públicos estáveis.
- [ ] Duplo clique, duas abas/clientes, resposta tardia, navegação, logout e unmount produzem no máximo um POST simultâneo por nota e nenhum efeito visual tardio.
- [ ] Timeout/reset/`5xx`/`2xx` inválido após envio é comunicado como resultado incerto, cria fence process-local de 60 segundos e nunca dispara retry automático.
- [ ] `cancelada=true` atualiza o cache local para `Cancelada` em best effort; o rolling sync não pode rebaixar esse estado terminal e o detalhe é recarregado pelo provider.
- [ ] `cancelada=false` preserva o status e mostra uma orientação textual limitada, inclusive procedimento manual.
- [ ] O botão aparece somente para perfil editor e detalhe `Autorizada`; confirmação explícita precede a chamada.
- [ ] O cabeçalho mantém `[dados] [Cancelar nota] | [⋮]`, com menu no extremo direito e comportamento móvel acessível.
- [ ] Lista, exportação, detalhe, PDF e XML não sofrem regressão.
- [ ] O endpoint usa `Cache-Control: private, no-store`, `Pragma: no-cache` e `X-Content-Type-Options: nosniff`.
- [ ] Confirmação e feedback obedecem ao estado `idle -> confirming -> submitting -> known-success|known-false|uncertain|failed -> reloading`, com foco, Escape, retorno de foco e anúncio acessível.
- [ ] Testes, lint, builds, guards e documentação passam sem segredo ou PII real nas evidências.

## Validation Steps

1. Executar testes fail-first do adapter, coordenador de cancelamento, service/controller, autorização e cache update monotônico.
2. Executar testes frontend do parser, confirmação, single-flight e lifecycle abort/late-result.
3. Executar suíte backend completa, Prisma validate, lint e build.
4. Executar testes, lint e build frontend.
5. Executar fluxo browser com APIs interceptadas para sucesso, `cancelada=false`, erro, timeout e mobile.
6. Executar BCI com 5/10/20 chamadas concorrentes de clientes distintos, disconnect/timeout/reset e interleavings de sync; executar FRC para navegação/logout/unmount.
7. Executar revisão de segurança, diff guard, authority guard e completion guard.

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **Comparison mode:** `working_tree`
- **User validation:** required for material deviation

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `C:/Unifast/MonitorNotas/MonitorNotes` | `6ad3a25b65720b78c9f0ae77e904c907167c813a` | `working_tree` |
| `uninotas-foundation` | `C:/Unifast/uninotas-foundation` | `4e1d51099e62d1b9a34cee051443ffe5ec0be6e1` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M, A` | mutation port, adapter, endpoint, service, cache reconciliation and tests |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | cancel API contract |
| `MonitorNotes` | `frontend/src/paginas/DetalheNota.tsx` | `M` | confirmation, lifecycle and result UI |
| `MonitorNotes` | `frontend/src/auth/SessaoContexto.tsx` | `M` | semantic `podeCancelarNota` permission |
| `MonitorNotes` | `frontend/src/componentes/**` | `M, A` | accessible confirmation/action component if extracted |
| `MonitorNotes` | `frontend/src/estilos/layout.css` | `M` | action placement and responsive layout |
| `MonitorNotes` | `frontend/e2e/**` | `M, A` | deterministic UI/browser evidence |
| `MonitorNotes` | `delphi-ai` | `M` | pre-existing approved workspace link; excluded from product staging |
| `MonitorNotes` | `foundation_documentation` | `M` | pre-existing Foundation workspace link; excluded from product staging |
| `MonitorNotes` | `uninotas-foundation` | `T` | pre-existing tracked-gitlink versus workspace-symlink topology; excluded from product staging |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md` | `A, M` | framing source |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-cancellation.md` | `A, M` | governing execution contract and evidence |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | stable endpoint/mutation contract consolidation |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A, M, D, R` | credentials and local environment are excluded |
| `MonitorNotes` | `backend/prisma/**` | `A, M, D, R` | existing composite key is sufficient; monotonic upsert requires no schema change |
| `MonitorNotes` | `backend/src/logs/**` | `A, M, D, R` | external logs are outside this mutation |
| `MonitorNotes` | `Dockerfile` | `A, M, D, R` | deployment topology is excluded |
| `MonitorNotes` | `railway.json` | `A, M, D, R` | deployment topology is excluded |
| `MonitorNotes` | `.github/**` | `A, M, D, R` | CI changes are excluded |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| workspace links `delphi-ai`, `foundation_documentation`, `uninotas-foundation` | noise / governed support topology | links predate this feature and are versioned in their owning repositories | retain locally; exclude from MonitorNotes staging | already authorized during workspace setup |

## Complexity

- **Classification:** `medium`
- **Checkpoint cadence:** backend contract, mutation orchestration, frontend lifecycle/layout, full validation.
- **Why:** external irreversible mutation, role boundary, stale cache reconciliation and asynchronous UI lifecycle cross two stacks.

## Canonical Module Anchors

- `foundation_documentation/project_constitution.md`
- `foundation_documentation/modules/fiscal-notes-and-documents.md`
- `foundation_documentation/modules/access-control-and-users.md`
- `foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md`
- `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md`

## Decision Pending

- None. The user confirmed editor profiles; the official OpenAPI defines no request body.

## Decisions

| ID | Decision | Rationale |
| --- | --- | --- |
| `D-CAN-01` | Only `ADMIN|GESTOR|ANALISTA` may cancel. | Existing editor catalog; `LEITOR` is read-only. |
| `D-CAN-02` | UI offers cancellation only for detail status `Autorizada`; backend still treats provider as final authority. | Avoid guaranteed invalid actions without trusting stale UI as authorization. |
| `D-CAN-03` | One confirmed click produces at most one local upstream attempt; no automatic retry. | Provider publishes no idempotency key and timeout may be outcome-ambiguous. |
| `D-CAN-04` | Public success response is bounded `{cancelled,message}`; provider message is text-only, not logged or persisted. | Municipal manual instructions must remain visible without widening data retention. |
| `D-CAN-05` | On `cancelled=true`, update cached status best-effort and refetch detail; cache failure cannot reverse or relabel provider success. | SmartNotas mutation is authoritative and irreversible. |
| `D-CAN-06` | Header layout is `[detail] [cancel] | [documents menu]`; menu aligns to far right. | Matches requested hierarchy and keeps documents secondary. |
| `D-CAN-07` | `FISC-CAN-01` supersedes the module's `provider writes` guardrail only for the approved single-note cancellation endpoint. | Keeps the canonical exception narrow and reviewable. |
| `D-CAN-08` | A process-local coordinator shares one in-flight promise per `{context,providerId}`; every caller is independently authenticated/rate-admitted, and uncertain outcomes fence new writes for 60 seconds. | Covers tabs/clients without pretending provider or multi-replica exactly-once support. |
| `D-CAN-09` | Once locally observed as `Cancelada`, the cache status is terminal; all page upserts preserve it atomically while other fields may refresh. | Prevents stale rolling pages from resurrecting an authorized action. |
| `D-CAN-10` | Client disconnect may suppress the response/UI, but cannot abort an already dispatched provider mutation; the internal operation retains its own bounded timeout and reconciliation. | Avoids converting a browser lifecycle event into an unsafe repeatable unknown write. |
| `D-CAN-11` | The frontend owns an explicit cancellation state machine and a semantic `podeCancelarNota` permission. | Prevents scattered flags, stale effects and accidental coupling to occurrence-treatment permission. |

## Decision Baseline (Frozen Before Implementation)

- **State:** proposed, pending `APROVADO`.
- Material changes to roles, retry/idempotency/fence semantics, accepted statuses, terminal-cache precedence, public response or cache failure behavior require renewed approval.

## Architecture Change Governance

- **Applicability:** `required`
- **Rationale:** the implementation preserves the existing port/adapter/service/controller shape, but `FISC-CAN-01` deliberately and narrowly supersedes the canonical `provider writes` exclusion for one irreversible operation.
- **Decision:** `FISC-CAN-01` becomes `Current` only after explicit TODO approval; before product implementation, the fiscal module must publish the endpoint, roles, strict response/error contract, uncertain-result policy and monotonic cache rule.
- **Supersession boundary:** no other SmartNotas write, bulk mutation, issue/reprocess path or client-supplied provider ID is authorized.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** pending fresh no-context opinion on the narrow `FISC-CAN-01` supersession and its protection harness.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** pending delivery review proving the implementation stayed inside `FISC-CAN-01` and its protection harness.
- **No-go handling:** an unresolved objection to the supersession boundary returns the TODO to planning; implementation cannot begin.

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| contract test | cancellation endpoint | Nest application test through JWT + `RolesGuard` | `LEITOR` or unauthenticated access and controller metadata precedence failure | implement-in-this-todo | backend integration suite |
| adapter contract test | SmartNotas POST | exact method/path/headers/no-body/envelope/size/error matrix | redirect, retry, oversized or malformed external response | implement-in-this-todo | adapter tests |
| concurrency test | cancellation coordinator | 5/10/20 callers for one signed note | more than one simultaneous provider POST or premature fence release | implement-in-this-todo | BCI artifact |
| data-integrity test | cache upsert | stale sync before/during/after direct cancellation update | downgrade from terminal `Cancelada` | implement-in-this-todo | cache integration test |

## External Dependency Readiness

| Dependency | Required contract | Evidence | Readiness | Failure handling |
| --- | --- | --- | --- | --- |
| SmartNotas | `POST /notas/{idInterno}/cancelar`, no body, `200 {cancelada,mensagem}`, `401/403/404` | official OpenAPI inspected 2026-09-29 | ready for mocked implementation; live smoke deferred | mapped errors, no retry, detail refresh |
| PostgreSQL read model | context + provider ID cache row may be updated and `Cancelada` cannot regress | existing Prisma composite key and cache service | ready without migration | best-effort direct update; atomic rolling upsert preserves terminal cancellation |

## Cancellation Public Contract

- Request: `POST /api/v1/notas/:noteId/cancelar`, no query and no body; route identity is the signed opaque `noteId` only.
- Provider response admission: HTTP `200`, body at most 16 KiB, exactly properties `cancelada:boolean` and `mensagem:string`; message is trimmed, normalized to LF, 1..2048 code points, and rejects NUL/unsupported control characters.
- Public success: HTTP `200` exact `{cancelled:boolean,message:string}` with private/no-store headers. `cancelled=false` is a known business result, not a transport failure.
- Every request is authenticated and actor-rate-admitted before joining/creating the process-local per-note operation.

| Condition | HTTP | Public code / response | Retry policy | Reconciliation |
| --- | --- | --- | --- | --- |
| provider `200`, exact `cancelada=true` | `200` | `{cancelled:true,message}` | none | terminal cache update best-effort + detail refetch |
| provider `200`, exact `cancelada=false` | `200` | `{cancelled:false,message}` | only a new explicit action if detail still authorizes it | no cache status update + detail refetch |
| no JWT | `401` | existing auth envelope | none automatic | none |
| `LEITOR` | `403` | existing role envelope | forbidden | zero service/adapter call |
| invalid/tampered `noteId` | `400` | existing invalid-note-ID code | none automatic | none |
| provider `401|403` | `502` | `SmartNotasCredencialRejeitada` | none automatic | operational correction |
| provider `404` | `409` | `CancelamentoFiscalNaoDisponivel` | no automatic retry | detail refetch; may already be canceled |
| provider `429` | `503` | `SmartNotasLimiteExterno` + bounded `Retry-After` when available | no automatic retry | retain current detail |
| local concurrent call | shared result | same bounded result/error from the single in-flight operation | no second POST | per-caller UI ownership still applies |
| active uncertain fence | `503` | `CancelamentoFiscalResultadoIncerto` + remaining bounded `Retry-After` | write forbidden during 60 s fence | read-only detail refetch allowed |
| timeout/reset/disconnect from provider, provider `5xx`, redirect, malformed/oversized successful response after dispatch | `503` | `CancelamentoFiscalResultadoIncerto` | no automatic retry; 60 s fence | detail refetch without claiming failure or success |
| local admission saturation before dispatch | `503` | `SmartNotasOcupado` | new explicit action later | known zero provider POST |

The operation checks the caller abort signal before dispatch. After dispatch it uses an internal bounded signal and completes independently of client disconnect; only delivery of its result and UI effects remain caller-owned. After an uncertain fence expires, a new explicit confirmation is allowed only if a fresh provider detail still reports `Autorizada`; this is risk reduction, not an exactly-once claim.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-CAN-01` | `cancelada=false` may carry a manual municipal procedure. | `artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md` records the official operation description; `C:/Unifast/MonitorNotas/MonitorNotes/frontend/src/paginas/DetalheNota.tsx` is the existing bounded detail-feedback surface. | UI guidance copy and false-result path would simplify. | High | Keep as Assumption |
| `A-CAN-02` | Provider `404` cannot distinguish missing, non-authorized or already canceled. | `artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md` records the official combined response description; `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/smart-notas.adapter.ts` owns current provider error normalization. | Public error mapping could become more specific. | High | Keep as Assumption |
| `A-CAN-03` | Timeout after dispatch has unknown mutation outcome. | `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/smart-notas.adapter.ts` owns the abortable external fetch and `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/smart-notas.port.ts` exposes no provider idempotency key or result token. | Automatic retry could be considered only under a new provider guarantee. | High | Keep as Assumption |
| `A-CAN-04` | Current runtime uses one API replica. | `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/fiscal-rate-coordinator.ts` explicitly owns only in-process coordination; `modules/fiscal-notes-and-documents.md` preserves that limit and `C:/Unifast/MonitorNotas/MonitorNotes/railway.json` declares no replica topology. | Distributed lease/idempotency design becomes approval-material. | Medium | Keep as Assumption |
| `A-CAN-05` | A matching cache row may be absent. | `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/fiscal-note-cache.service.ts` treats the read model as derived and `todos/active/features/TODO-uninotas-fiscal-note-read-model.md` preserves provider-backed detail during partial bootstrap/resume. | Cache update can be mandatory but provider success semantics stay unchanged. | High | Keep as Assumption |

## Execution Plan

### Touched Surfaces

- NestJS fiscal port, adapter, service, controller, errors, dedicated cancellation coordinator and cache service.
- React API client, semantic session permission, detail state machine, accessible confirmation component, layout CSS and fiscal tests.
- Foundation fiscal module and this TODO.

### Ordered Steps

1. Publish approved `FISC-CAN-01` and the complete mutation contract in the fiscal module before product code.
2. Add fail-first adapter/port tests for method, path, headers, body absence, 16 KiB/2048-code-point limits, exact envelope and closed error matrix.
3. Add a bounded process-local cancellation coordinator and fail-first BCI tests for shared in-flight work, per-actor admission, uncertain fence and cleanup/cardinality.
4. Add application-level JWT/`RolesGuard` tests and service/cache tests, including zero adapter calls for unauthorized users and monotonic cache interleavings.
5. Implement provider cancellation with a pre-dispatch caller-abort check, then an internally bounded non-retried POST and non-sensitive audit event.
6. Add frontend parser/state-machine tests for confirmation, duplicate click, uncertain fence guidance, ownership generation, logout/navigation/unmount and failed refetch.
7. Implement semantic permission, status-gated accessible confirmation/result feedback, refetch and three-column responsive header.
8. Run browser/mobile flow, full suites, BCI/FRC/security reviews and deterministic TODO guards.

### Test Strategy

- Test-first for every mutation boundary.
- No live cancellation in automated tests.
- Synthetic opaque IDs and `.test` data only.
- Validate success true/false, properties extra/absent, invalid types/control characters, body/message limits, 401/403/404/429/5xx/redirect/timeout/reset/disconnect, denied role, multi-client duplicate submission and cache-update failure/delay.

### Flow Evidence Planning Matrix

| Flow | Actor / Preconditions | Action | Expected Outcome | Evidence Lane | Status |
| --- | --- | --- | --- | --- | --- |
| authorized success | editor + `Autorizada` detail | confirm cancel | one POST, success feedback, detail reload, local status update | integration + browser | planned |
| manual procedure | editor + provider returns `cancelada=false` | confirm cancel | bounded provider guidance, no cache status change | integration + browser | planned |
| read-only | `LEITOR` | inspect authorized detail / attempt endpoint | no button; backend 403 | integration + browser | planned |
| duplicate/race | editor; request pending | click repeatedly / navigate / logout | one upstream attempt; no late state effect | BCI + FRC + browser | planned |
| uncertain outcome | provider timeout/abort after dispatch | confirm cancel | no auto retry; neutral uncertain message and detail refresh path | integration + browser | planned |
| stale rolling page | sync overlaps confirmed cancellation | finish sync before/during/after cache mark | `Cancelada` remains terminal in local projection | cache integration + BCI | planned |
| authorization boundary | no JWT, `LEITOR`, then each editor role | call endpoint through Nest guards | `401`, `403` with zero adapter call, and editor admission | application integration | planned |
| responsive layout | desktop and mobile detail | inspect actions | cancel before divider; menu at far edge; no overflow | browser | planned |

### Frontend / Consumer Matrix

| Producer | Consumer | Contract | Compatibility / Invalidation | Planned Evidence |
| --- | --- | --- | --- | --- |
| `POST /api/v1/notas/:noteId/cancelar` | `DetalheNota` | `{cancelled:boolean,message:string}` | additive endpoint; no existing consumer break | parser + application + browser |
| cache status update | list/export local readers | `providerStatus=Cancelada` for context + provider ID | confirmed true is terminal; stale sync cannot downgrade | cache/service integration |
| detail refetch | `DetalheNota` | existing detail DTO | invalidate current screen generation after mutation | FRC/browser |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Behavior / Scenario | Preconditions | Command | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| backend full | mutation plus fiscal regressions | mocked provider and local dependencies | `cd backend && npx jest --runInBand` | planned | pending implementation |
| backend static/build | Nest wiring and types | dependencies installed | `cd backend && npx prisma validate && npx eslint "src/**/*.ts" && npm run build` | planned | pending implementation |
| frontend full | parser, async lifecycle and bundle | dependencies installed | `cd frontend && npm run test:notas && npm run lint && npm run build` | planned | pending implementation |
| browser | success/false/error/timeout/role/layout | fresh local build and intercepted APIs | project-owned fiscal browser runner | planned | pending implementation |

### Runtime / Rollout Notes

- No migration or environment variable is planned.
- The cancellation coordinator is intentionally process-local and bounded; deploying more than one API replica requires a new approved distributed fence/idempotency design.
- Stage smoke must use a disposable authorized test note explicitly approved for cancellation; automated/live production cancellation is forbidden.
- After deploy, confirm one successful mutation, cache/list convergence and provider/manual-false handling without recording PII.

## Plan Review Gate

- **Review state:** completed against frozen baseline
- **Primary risks:** irreversible side effect, unknown timeout outcome, duplicate submission, role bypass, cache divergence and untrusted provider message.
- **Preferred design:** direct mutation through signed context-bound ID, one attempt, strict response, explicit confirmation, best-effort projection update and provider detail refetch.
- **Rejected design:** optimistic `Cancelada` before provider response; automatic retry; raw provider ID from browser; allowing `LEITOR`; hiding `cancelada=false` guidance.

### Review Sections

- [x] Architecture — existing port/adapter/service/controller ownership is preserved.
- [x] Code Quality — one mutation method and one public DTO; no alternate direct fetch path.
- [x] Tests — fail-first adapter, authorization, cache, BCI, FRC and browser lanes are planned.
- [x] Performance — one direct upstream call; no list scan or historical traversal.
- [x] Security — editor-only endpoint, signed context identity, no client credentials/raw ID.
- [x] Elegance — documents remain in the overflow menu; cancellation is a first-class destructive action.
- [x] Structural Soundness — provider success is never reclassified by a downstream cache failure.

### Issue Cards

- **Issue ID:** `PR-CAN-01`
  - **Severity:** medium
  - **Evidence:** provider publishes no idempotency key and existing adapter can time out after dispatch.
  - **Why it matters now:** retrying can repeat an irreversible operation while reporting failure can also be false.
  - **Option A (Recommended):** one attempt, no automatic retry, neutral uncertain-result feedback and authoritative detail reload.
  - **Option B:** retry automatically once after timeout; rejected because outcome is unknown.
  - **Option C:** report failure without reload; rejected because it can lie about provider state.
  - **Recommendation:** Option A; prove with BCI/FRC and integration tests.
- **Issue ID:** `PR-CAN-02`
  - **Severity:** medium
  - **Evidence:** provider mutation and PostgreSQL cache update cannot share a transaction.
  - **Why it matters now:** cache failure after provider success cannot roll back the cancellation.
  - **Option A (Recommended):** return provider success, attempt context-scoped cache update, reload provider detail and let rolling sync repair residual drift.
  - **Option B:** return server error when cache update fails; rejected because it encourages unsafe retry.
  - **Option C:** ignore local projection entirely; rejected because list may remain visibly stale for 15 minutes.
  - **Recommendation:** Option A; log only aggregate reconciliation outcome.

### Failure Modes & Edge Cases

- Status changes between detail render and click: provider decides; frontend handles conflict and reloads.
- Provider returns `200 cancelada=false`: no success claim or local status mutation.
- Provider succeeds and cache update fails: return fiscal success, log only aggregate cache reconciliation failure and refetch detail; a later non-stale sync may converge, while no sync may downgrade an existing `Cancelada`.
- Client disconnects after upstream dispatch: suppress caller response/effects, but let the internally bounded shared operation finish; do not retry.
- Two tabs/clients cancel the same note concurrently: both join one process-local operation after independent authorization/admission and observe the same bounded result.
- A second API replica would bypass the in-memory fence: deployment topology change is approval-material and forbidden in this TODO.
- Message overflow/malformed body: fail closed as provider contract error.

## Security Risk Assessment

- **Risk level:** `high`
- **Why this risk level:** authenticated irreversible fiscal mutation using tenant-specific external credentials.
- **Attack surface in scope:** authorization, signed route identity, context isolation, external response trust boundary, double submission and audit logging.
- **Attack simulation decision:** `required`
- **Review evidence:** planned `security-adversarial-review` after implementation.
- **Residual security risk:** provider cannot offer client-visible exactly-once confirmation after ambiguous timeout.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** non-idempotent external write plus asynchronous UI lifecycle; throughput is small but duplicate effects are material.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | endpoint-performance-scrutiny | recommended | low | EPS-EXACT-LOOKUP-SURFACE-CHANGED | before_local_implemented | EPS-E1 | pending | none | none |
| `FRC` | frontend-race-condition-validation | required | high | FRC-DUPLICATE-MUTATION | before_local_implemented | FRC-POLICY, FRC-E1, FRC-E2, FRC-E3 | pending | unknown provider completion after abort | U-ASYNC-SURFACE-UNKNOWN |
| `BCI` | backend-concurrency-idempotency-validation | required | high | BCI-IRREVERSIBLE-SIDE-EFFECT | before_local_implemented | BCI-INV, BCI-POLICY, BCI-E1, BCI-E2, BCI-E3 | pending | no provider idempotency key | U-WRITE-OVERLAP-UNKNOWN |
| `RLS` | runtime-load-stress-validation | not_needed | low | n/a | before_local_implemented | n/a | not_applicable | one bounded provider call per action | none |

## Audit Trigger Matrix

- **Latest audit derivation:** `audit_escalation_guard.py` returned `go` on 2026-09-29 with fingerprint `584a99faf1f8`.
- **Derived delivery floor:** critique `required`; architecture decision/adherence reviews `required`; test-quality audit `required`; final review `required`; dedicated triple review `required`; security review `required`; verification-debt audit `required`; performance/concurrency validation `recommended` with BCI/FRC mandatory from the risk matrix.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | Cross-stack external mutation with explicit failure semantics. |
| `blast_radius` | `cross-stack` | NestJS producer, React consumer and local read model. |
| `behavioral_change_or_bugfix` | `yes` | Adds a user-visible fiscal mutation. |
| `changes_public_contract` | `yes` | Adds an authenticated POST endpoint and response DTO. |
| `touches_auth_or_tenant` | `yes` | Changes role authorization and context-bound provider credentials. |
| `touches_runtime_or_infra` | `no` | No queue, worker, migration or deploy change. |
| `touches_tests` | `yes` | New contract, integration, race and browser tests. |
| `critical_user_journey` | `yes` | Fiscal cancellation is business-critical and irreversible. |
| `release_or_promotion_critical` | `yes` | Incorrect behavior blocks safe release of the feature. |
| `high_severity_plan_review_issue` | `no` | Both issue cards are medium and have selected mitigations. |
| `explicit_three_lane_request` | `no` | User did not request the dedicated three-lane protocol. |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** medium, cross-stack, authenticated, irreversible fiscal mutation with a new public endpoint.
- **Impact signals in scope:** `cross-module blast radius|public API|auth|critical user journey`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen TODO, feature brief, fiscal module contract, service/errors/rate/auth/cache anchors and directly touched frontend anchors.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** required; reviewer must differ from the implementing agent and return findings before implementation advice.
- **Canonical multi-lane audit protocol:** `n/a` for planning critique; dedicated triple review remains a delivery gate.
- **Audit session / round evidence:** `n/a`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `findings_integrated`; convergence confirmation pending a fresh no-context pass after refreshed baseline.
- **Findings summary:** seven findings identified canonical-authority, per-note concurrency/uncertainty, cache monotonicity, closed error bounds, real guard evidence, explicit UI state/accessibility and validation-package gaps; all were integrated into decisions, contract, DoD and validation.
- **Resolution ledger:** findings, if any, will be classified below as `Integrated|Challenged|Deferred`.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `CRIT-CAN-01` | Integrated | useful | yes | project | `FISC-CAN-01` | Architecture governance now requires a narrow canonical supersession published before product code. |
| `CRIT-CAN-02` | Integrated | useful | yes | project | `D-CAN-08,D-CAN-10` define shared process-local in-flight work, independent actor admission, 60 s uncertain fence and disconnect semantics. |
| `CRIT-CAN-03` | Integrated | useful | yes | project | `D-CAN-09` and the protection harness require atomic terminal-status preservation across all sync interleavings. |
| `CRIT-CAN-04` | Integrated | useful | yes | project | Cancellation Public Contract closes body/message limits, exact envelope, headers and HTTP/public-code mapping. |
| `CRIT-CAN-05` | Integrated | useful | yes | project | Application-level JWT/`RolesGuard` matrix proves method metadata override and zero downstream calls for denied roles. |
| `CRIT-CAN-06` | Integrated | useful | partial | project | `D-CAN-11` freezes semantic permission, explicit UI states, lifecycle ownership and accessibility evidence. |
| `CRIT-CAN-07` | Integrated | useful | no | none | Bounded review/validation anchors now include service, errors, coordinator, rate, auth and concrete concurrent/interleaving scenarios. |

- **Evidence / reference:** fresh reviewer `Leibniz` (`01a0ee41-ca9b-7c62-93f8-03f04bf106b7`), verdict `findings_require_integration`, 2026-09-29; follow-up convergence review pending refreshed baseline.
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** medium cross-stack mutation requires a stable review packet before planning guards.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `feature/uninotas-fiscal-note-cancellation`
- **Baseline commit:** `b20cd3124bbc684ab19c4872666fb7144407700c`
- **Baseline push reference:** `origin/feature/uninotas-fiscal-note-cancellation`
- **Gate status:** `no_material_findings`
- **Findings summary:** refined feature brief/TODO decisions, assumptions, execution plan and review-gate floor were committed and pushed before the independent critique.
- **Evidence / reference:** `b20cd3124bbc684ab19c4872666fb7144407700c` pushed to `origin/feature/uninotas-fiscal-note-cancellation`.
- **Waiver authority / reference:** `n/a`
- **Scope-neutral evidence update:** this freeze record and guard outcomes may be committed after the baseline without changing the frozen feature scope.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** provider semantics, cache absence and single-replica coordination are live assumptions that influence failure handling.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-CAN-01,A-CAN-02,A-CAN-03,A-CAN-04,A-CAN-05`
- **Guard command:** `python delphi-ai/tools/assumption_code_coherence_guard.py --todo <todo-path>`
- **Gate status:** `not_run`
- **Findings summary:** pending guard execution after audit-floor derivation.
- **Evidence / reference:** pending
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** approval must use the same mutation, permission, retry and cache semantics reviewed at freeze.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python delphi-ai/tools/review_scope_drift_guard.py --todo <todo-path>`
- **No-go handling rule:** return to review, revalidate material scope with the user and refresh the baseline when necessary.
- **Gate status:** `not_run`
- **Findings summary:** pending review convergence.
- **Evidence / reference:** pending
- **Waiver authority / reference:** `n/a`

## Delivery Review Gates

### Verification Debt Assessment

- **Audit decision:** `required before Completed`
- **Audit status:** `not_run`
- **Why this decision:** medium behavior change with live external-state uncertainty must account for any unexecuted validation.
- **Evidence / reference:** planned `verification-debt-audit` after implementation and primary validation.
- **Accepted residual debt:** none approved.

### Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** behavior-defining API/UI change and critical fiscal journey require independent validation of test efficacy.
- **Package mode:** `bounded-file-set`
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `fresh internal no-context reviewer`
- **Audit status:** `not_run`
- **Audit focus:** product/test alignment, fail-first evidence, bypasses, assertion efficacy and failure-mode coverage.
- **Evidence / reference:** required after implementation and primary validation.

### Dedicated Triple Review Audit Gate

- **Audit decision:** `required`
- **Why this decision:** audit escalation requires the delivery-side Performance + Test Quality lanes; cutover-integrity remains not applicable unless implementation introduces a compatibility bridge.
- **Canonical protocol:** `audit-protocol-triple-review`
- **Audit status:** `not_run`
- **Evidence / reference:** required after implementation and before final review.

### Security Adversarial Review Gate

- **Review decision:** `required`
- **Why this decision:** tenant-context credentials and an irreversible role-protected fiscal mutation are in scope.
- **Review status:** `not_run`
- **Review focus:** authorization bypass, signed-ID/context isolation, external message trust, duplicate submission and sensitive logging.
- **Evidence / reference:** required after implementation and primary validation.

### Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** medium cross-stack public API/auth change with irreversible external side effect.
- **Package mode:** `bounded-file-set`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Final review status:** `not_run`
- **Review focus:** approval adherence, regressions, evidence strength, security/performance residuals, elegance and structural soundness.
- **Evidence / reference:** required after all delivery audits and before `Completed`.

## Approval

- **Approval status:** `PENDING`
- **Required response:** `APROVADO o escopo e as premissas do TODO de cancelamento fiscal.`
- The user's `Perfeito` confirms the role decision only; it is not recorded as implementation authority for the complete TODO.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies | Execution Impact | Status |
| --- | --- | --- | --- |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | controller/service/adapter mutation | preserve Nest ownership and explicit failures | planned |
| `delphi-ai/skills/wf-nestjs-change-application-boundary-method/SKILL.md` | new application endpoint | contract-first implementation | planned |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | detail UI mutation | explicit async state and accessible layout | planned |
| `delphi-ai/skills/wf-react-change-ui-boundary-method/SKILL.md` | action/confirmation consumer | consumer lifecycle evidence | planned |
| `delphi-ai/skills/backend-concurrency-idempotency-validation/SKILL.md` | irreversible write | prove duplicate policy and uncertain outcome | planned |
| `delphi-ai/skills/frontend-race-condition-validation/SKILL.md` | abort/navigation/late response | deterministic race scenarios | planned |
| `delphi-ai/skills/security-adversarial-review/SKILL.md` | authenticated fiscal mutation | adversarial auth/context/message review | planned |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | behavior-defining tests | fail-first and boundary coverage | planned |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-luna`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree authorization:** not requested; no worktree or auxiliary checkout may be created.
- **Scope:** `nestjs, react, vite`
- **Guard outcome:** pending review baseline and pre-approval guards.

## Blockers (Current)

- `PENDING_APPROVAL`: implementation requires explicit `APROVADO` after preflight-go.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planning contract awaiting freeze/review/approval.
- **Post-commit/push status:** `complete`
- **Next path/status action:** complete planning guards and request explicit approval.
