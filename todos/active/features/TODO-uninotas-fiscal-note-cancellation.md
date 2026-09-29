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
- Atualizar o status local para `Cancelada` quando `cancelada=true`, sem transformar o PostgreSQL em autoridade fiscal.
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

## Out of Scope

- Cancelamento em lote, motivo livre ou payload não publicado pelo SmartNotas.
- Cancelar notas cujo detalhe atual não esteja em `Autorizada`.
- Retry automático, promessa de exactly-once ou chave de idempotência inexistente no provider.
- Emissão, reprocessamento, edição, procedimento manual de prefeitura ou mudança de quota/credencial.
- Persistência de mensagem bruta, payload externo, token ou documento adicional.
- Deploy, promoção, alteração de Railway/CI ou escala horizontal.

## Definition of Done

- [ ] `POST /api/v1/notas/:noteId/cancelar` usa o ID opaco assinado e rejeita `LEITOR`.
- [ ] O adapter envia `POST` sem body para o path oficial, com contexto/headers internos corretos, sem redirect/retry.
- [ ] Somente resposta `200` com envelope exato e limitado cruza o trust boundary; falhas têm códigos públicos estáveis.
- [ ] Duplo clique, resposta tardia, navegação, logout e unmount não produzem segunda mutação nem efeito visual tardio.
- [ ] Timeout/abort após envio é comunicado como resultado incerto e nunca dispara retry automático.
- [ ] `cancelada=true` atualiza o cache local para `Cancelada` em best effort e o detalhe é recarregado pelo provider.
- [ ] `cancelada=false` preserva o status e mostra uma orientação textual limitada, inclusive procedimento manual.
- [ ] O botão aparece somente para perfil editor e detalhe `Autorizada`; confirmação explícita precede a chamada.
- [ ] O cabeçalho mantém `[dados] [Cancelar nota] | [⋮]`, com menu no extremo direito e comportamento móvel acessível.
- [ ] Lista, exportação, detalhe, PDF e XML não sofrem regressão.
- [ ] Testes, lint, builds, guards e documentação passam sem segredo ou PII real nas evidências.

## Validation Steps

1. Executar testes fail-first do adapter, service/controller, autorização e cache update.
2. Executar testes frontend do parser, confirmação, single-flight e lifecycle abort/late-result.
3. Executar suíte backend completa, Prisma validate, lint e build.
4. Executar testes, lint e build frontend.
5. Executar fluxo browser com APIs interceptadas para sucesso, `cancelada=false`, erro, timeout e mobile.
6. Executar BCI para dupla submissão/resultado incerto e FRC para navegação/logout/unmount.
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
| `MonitorNotes` | `frontend/src/componentes/**` | `M, A` | accessible confirmation/action component if extracted |
| `MonitorNotes` | `frontend/src/estilos/layout.css` | `M` | action placement and responsive layout |
| `MonitorNotes` | `frontend/e2e/**` | `M, A` | deterministic UI/browser evidence |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md` | `A, M` | framing source |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-cancellation.md` | `A, M` | governing execution contract and evidence |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | stable endpoint/mutation contract consolidation |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A, M, D, R` | credentials and local environment are excluded |
| `MonitorNotes` | `backend/prisma/**` | `A, M, D, R` | existing cache schema is sufficient |
| `MonitorNotes` | `backend/src/logs/**` | `A, M, D, R` | external logs are outside this mutation |
| `MonitorNotes` | `Dockerfile` | `A, M, D, R` | deployment topology is excluded |
| `MonitorNotes` | `railway.json` | `A, M, D, R` | deployment topology is excluded |
| `MonitorNotes` | `.github/**` | `A, M, D, R` | CI changes are excluded |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| none at freeze | n/a | strict expected paths above | classify before changing contract | required for material expansion |

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

## Decision Baseline (Frozen Before Implementation)

- **State:** proposed, pending `APROVADO`.
- Material changes to roles, retry/idempotency semantics, accepted statuses, public response or cache failure behavior require renewed approval.

## Architecture Change Governance

- **Applicability:** `not_needed`
- **Rationale:** adds one bounded mutation through the existing fiscal adapter/service/controller architecture; it does not establish a new shared architecture.

## External Dependency Readiness

| Dependency | Required contract | Evidence | Readiness | Failure handling |
| --- | --- | --- | --- | --- |
| SmartNotas | `POST /notas/{idInterno}/cancelar`, no body, `200 {cancelada,mensagem}`, `401/403/404` | official OpenAPI inspected 2026-09-29 | ready for mocked implementation; live smoke deferred | mapped errors, no retry, detail refresh |
| PostgreSQL read model | context + provider ID cache row may be updated | existing Prisma model and cache service | ready | best-effort update; rolling sync repairs |

## Assumptions Preview

- The provider operation is synchronous at HTTP level, but `cancelada=false` may carry a manual municipal procedure.
- `404` cannot distinguish missing, non-authorized or already canceled; public messaging must avoid asserting which one occurred.
- A network timeout after request transmission has unknown outcome; UI must direct the user to refresh rather than retry automatically.
- Current deployment uses one API replica; frontend and backend guards prevent duplicate local submission but do not claim distributed exactly-once semantics.
- The existing cache row may be absent; provider success remains success and detail reload is authoritative.

## Execution Plan

### Touched Surfaces

- NestJS fiscal port, adapter, service, controller, errors and cache service.
- React API client, detail screen, optional confirmation component, layout CSS and fiscal tests.
- Foundation fiscal module and this TODO.

### Ordered Steps

1. Add fail-first adapter/port tests for method, path, headers, body absence, strict envelope and error mapping.
2. Add service/controller authorization and single-attempt tests, including cache success/failure semantics.
3. Implement provider cancellation through the existing concurrency/rate boundaries and non-sensitive audit event.
4. Add frontend response parser and fail-first lifecycle tests for confirmation, duplicate click, abort and stale completion.
5. Implement the status-gated button, confirmation/result feedback, refetch and three-column responsive header.
6. Run browser/mobile flow, full suites, BCI/FRC/security reviews and deterministic TODO guards.
7. Consolidate the final stable mutation contract into the fiscal module documentation.

### Test Strategy

- Test-first for every mutation boundary.
- No live cancellation in automated tests.
- Synthetic opaque IDs and `.test` data only.
- Validate success true/false, malformed envelope, 401/403/404/429/5xx/redirect/timeout/abort, denied role, duplicate submission and cache-update failure.

### Flow Evidence Planning Matrix

| Flow | Actor / Preconditions | Action | Expected Outcome | Evidence Lane | Status |
| --- | --- | --- | --- | --- | --- |
| authorized success | editor + `Autorizada` detail | confirm cancel | one POST, success feedback, detail reload, local status update | integration + browser | planned |
| manual procedure | editor + provider returns `cancelada=false` | confirm cancel | bounded provider guidance, no cache status change | integration + browser | planned |
| read-only | `LEITOR` | inspect authorized detail / attempt endpoint | no button; backend 403 | integration + browser | planned |
| duplicate/race | editor; request pending | click repeatedly / navigate / logout | one upstream attempt; no late state effect | BCI + FRC + browser | planned |
| uncertain outcome | provider timeout/abort after dispatch | confirm cancel | no auto retry; neutral uncertain message and detail refresh path | integration + browser | planned |
| responsive layout | desktop and mobile detail | inspect actions | cancel before divider; menu at far edge; no overflow | browser | planned |

### Frontend / Consumer Matrix

| Producer | Consumer | Contract | Compatibility / Invalidation | Planned Evidence |
| --- | --- | --- | --- | --- |
| `POST /api/v1/notas/:noteId/cancelar` | `DetalheNota` | `{cancelled:boolean,message:string}` | additive endpoint; no existing consumer break | parser + application + browser |
| cache status update | list/export local readers | `providerStatus=Cancelada` for context + provider ID | update only after confirmed true | cache/service unit |
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
- Stage smoke must use a disposable authorized test note explicitly approved for cancellation; automated/live production cancellation is forbidden.
- After deploy, confirm one successful mutation, cache/list convergence and provider/manual-false handling without recording PII.

## Plan Review Gate

- **Review state:** prepared-pre-freeze
- **Primary risks:** irreversible side effect, unknown timeout outcome, duplicate submission, role bypass, cache divergence and untrusted provider message.
- **Preferred design:** direct mutation through signed context-bound ID, one attempt, strict response, explicit confirmation, best-effort projection update and provider detail refetch.
- **Rejected design:** optimistic `Cancelada` before provider response; automatic retry; raw provider ID from browser; allowing `LEITOR`; hiding `cancelada=false` guidance.

### Failure Modes & Edge Cases

- Status changes between detail render and click: provider decides; frontend handles conflict and reloads.
- Provider returns `200 cancelada=false`: no success claim or local status mutation.
- Provider succeeds and cache update fails: return fiscal success, log only aggregate cache reconciliation failure, refetch detail; rolling sync repairs list.
- Client disconnects after upstream dispatch: abort local work but do not claim cancellation failed or retry.
- Two tabs cancel the same note: second may receive provider `404`; reload reveals authoritative status.
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

| Trigger | Result | Rationale | Required Lane |
| --- | --- | --- | --- |
| external irreversible mutation | yes | cancellation cannot be rolled back locally | security + BCI |
| frontend async user flow | yes | duplicate/late result and navigation races | FRC |
| shared/public API contract | yes | new authenticated mutation endpoint | test-quality + final review |
| architecture correction | no | existing boundaries are reused | n/a |
| cutover/legacy retirement | no | additive endpoint only | n/a |

## Gate: Review Baseline Freeze

- **Status:** pending-freeze
- **Authoritative repository:** `C:/Unifast/uninotas-foundation`
- **Planned branch:** `feature/uninotas-fiscal-note-cancellation`
- **Baseline:** pending commit/push of this brief and TODO.

## Gate: Assumption Code Coherence

- **Status:** pending-freeze
- **Evidence:** run after baseline publication and planning review.

## Gate: Review Scope Drift

- **Status:** pending-freeze
- **Evidence:** run after review convergence.

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

- `PENDING_REVIEW_BASELINE`: feature brief and TODO must be committed and pushed before authoritative planning guards.
- `PENDING_APPROVAL`: implementation requires explicit `APROVADO` after preflight-go.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planning contract awaiting freeze/review/approval.
- **Post-commit/push status:** `pending`
- **Next path/status action:** publish review baseline and complete approval gates.
