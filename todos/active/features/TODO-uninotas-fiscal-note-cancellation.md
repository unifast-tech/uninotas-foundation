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
- Coordenar chamadas por `{contextoFiscal,providerIdInterno}` com um registro durável no PostgreSQL, eleição atômica de líder e estado incerto fail-closed sem expiração automática.
- Usar o registro durável confirmado como tombstone e impedir atomicamente que uma página antiga do rolling sync crie ou rebaixe a nota como `Autorizada`.
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
- `SCOPE-CAN-04`: operação/tombstone durável e atualização monotônica da projeção local após sucesso fiscal confirmado.
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
- Retry automático ou nova tentativa pelo Monitor para uma operação marcada `uncertain`; a resolução é leitura/reconciliação ou procedimento operacional manual.

## Definition of Done

- [ ] `POST /api/v1/notas/:noteId/cancelar` usa o ID opaco assinado e rejeita `LEITOR`.
- [ ] O adapter envia `POST` sem body para o path oficial, com contexto/headers internos corretos, sem redirect/retry e com timeout interno não cancelado por disconnect posterior ao despacho.
- [ ] Somente resposta `200` com envelope exato, body de até 16 KiB e mensagem normalizada de 1..2048 code points cruza o trust boundary; falhas têm códigos públicos estáveis.
- [ ] Duplo clique, duas abas/clientes, resposta tardia, navegação, logout e unmount produzem no máximo um POST simultâneo por nota e nenhum efeito visual tardio.
- [ ] Timeout/reset/`5xx`/`2xx` inválido após envio ou lease vencido é persistido como `uncertain`, bloqueia novos writes em qualquer réplica e nunca expira/reexecuta automaticamente.
- [ ] `cancelada=true` persiste `cancelled` e atualiza o cache na mesma transação; rolling upserts consultam o tombstone atomicamente, inclusive quando a linha de cache ainda não existe.
- [ ] A transação de `cancelled` e toda transação de upsert adquirem a mesma advisory lock por nota antes de consultar/escrever tombstone/cache; lotes ordenam chaves para evitar deadlock.
- [ ] O detalhe consulta o estado durável após o provider: tombstone `cancelled` força `providerStatus=Cancelada`, e `cancellationState` impede reapresentar a ação para `in_progress|uncertain|not_cancelled|cancelled`.
- [ ] `cancelada=false` preserva o status e mostra uma orientação textual limitada, inclusive procedimento manual.
- [ ] O botão aparece somente para perfil editor e detalhe `Autorizada`; confirmação explícita precede a chamada.
- [ ] O cabeçalho mantém `[dados] [Cancelar nota] | [⋮]`, com menu no extremo direito e comportamento móvel acessível.
- [ ] Lista, exportação, detalhe, PDF e XML não sofrem regressão.
- [ ] O endpoint usa `Cache-Control: private, no-store`, `Pragma: no-cache` e `X-Content-Type-Options: nosniff`.
- [ ] Query, body (inclusive `{}`) ou content type de payload são rejeitados com `400 CancelamentoFiscalRequisicaoInvalida` antes do service.
- [ ] Confirmação e feedback obedecem ao estado `idle -> confirming -> submitting -> known-success|known-false|uncertain|failed -> reloading`, com foco, Escape, retorno de foco e anúncio acessível.
- [ ] Rollback desativa somente rota e UI; migração, linhas terminais, overlay do detalhe e barreira tombstone-aware dos upserts permanecem ativos.
- [ ] `SMART_NOTAS_CANCEL_ENABLED=false` é o kill switch padrão: rota falha antes do claim, detalhe retorna ação indisponível, mas overlay/tombstone/upserts continuam ativos.
- [ ] Testes, lint, builds, guards e documentação passam sem segredo ou PII real nas evidências.

## Validation Steps

1. Executar testes fail-first do adapter, coordenador de cancelamento, service/controller, autorização e cache update monotônico.
2. Executar testes frontend do parser, confirmação, single-flight e lifecycle abort/late-result.
3. Executar suíte backend completa, Prisma validate, lint e build.
4. Executar testes, lint e build frontend.
5. Executar fluxo browser com APIs interceptadas para sucesso, `cancelada=false`, detalhe provider atrasado, erro, timeout e mobile.
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
| `MonitorNotes` | `backend/prisma/schema.prisma` | `M` | durable cancellation-operation/tombstone model |
| `MonitorNotes` | `backend/prisma/migrations/**` | `A` | additive cancellation-operation migration |
| `MonitorNotes` | `backend/package.json` | `M` | project-owned disposable PostgreSQL migration test command |
| `MonitorNotes` | `backend/src/config/**` | `M` | cancellation-specific fail-closed feature flag and tests |
| `MonitorNotes` | `backend/.env.example` | `M` | document disabled-by-default cancellation flag |
| `MonitorNotes` | `backend/README.md` | `M` | local runtime and forward-only rollback contract |
| `MonitorNotes` | `frontend/src/api/cliente.ts` | `M` | POST signal plus bounded public error code and Retry-After |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | cancel API contract |
| `MonitorNotes` | `frontend/src/paginas/DetalheNota.tsx` | `M` | confirmation, lifecycle and result UI |
| `MonitorNotes` | `frontend/src/auth/SessaoContexto.tsx` | `M` | semantic `podeCancelarNota` permission |
| `MonitorNotes` | `frontend/src/contextos/NotasFiscaisContexto.tsx` | `M` | invalidate list cache after confirmed cancellation |
| `MonitorNotes` | `frontend/src/notas/cacheFiscal.ts` | `M` | bounded list-cache invalidation primitive |
| `MonitorNotes` | `frontend/src/notas/normalizacaoFiscal.ts` | `M` | strict detail cancellation-state parser |
| `MonitorNotes` | `frontend/src/componentes/**` | `M, A` | accessible confirmation/action component if extracted |
| `MonitorNotes` | `frontend/src/estilos/layout.css` | `M` | action placement and responsive layout |
| `MonitorNotes` | `frontend/e2e/**` | `M, A` | deterministic UI/browser evidence |
| `MonitorNotes` | `delphi-ai` | `M` | pre-existing approved workspace link; excluded from product staging |
| `MonitorNotes` | `foundation_documentation` | `M` | pre-existing Foundation workspace link; excluded from product staging |
| `MonitorNotes` | `uninotas-foundation` | `T` | pre-existing tracked-gitlink versus workspace-symlink topology; excluded from product staging |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md` | `A, M` | framing source |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-cancellation.md` | `A, M` | governing execution contract and evidence |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | stable endpoint/mutation contract consolidation |
| `uninotas-foundation` | `policies/scope_subscope_governance.md` | `M` | planned `fiscal_note_cancellation` capability ownership |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A, M, D, R` | credentials and local environment are excluded |
| `MonitorNotes` | `backend/src/logs/**` | `A, M, D, R` | external logs are outside this mutation |
| `MonitorNotes` | `Dockerfile` | `A, M, D, R` | deployment topology is excluded |
| `MonitorNotes` | `railway.json` | `A, M, D, R` | deployment topology is excluded |
| `MonitorNotes` | `.github/**` | `A, M, D, R` | CI changes are excluded |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| workspace links `delphi-ai`, `foundation_documentation`, `uninotas-foundation` | noise / governed support topology | links predate this feature and are versioned in their owning repositories | retain locally; exclude from MonitorNotes staging | already authorized during workspace setup |

## Complexity

- **Classification:** `big`
- **Checkpoint cadence:** backend contract, mutation orchestration, frontend lifecycle/layout, full validation.
- **Why:** irreversible external mutation, additive relational state machine/migration, cross-replica election, role boundary, cache monotonicity and asynchronous UI lifecycle cross both stacks.

## Canonical Module Anchors

- `foundation_documentation/project_constitution.md`
- `foundation_documentation/modules/fiscal-notes-and-documents.md`
- `foundation_documentation/modules/identity-and-team.md`
- `foundation_documentation/policies/scope_subscope_governance.md`
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
| `D-CAN-05` | On `cancelled=true`, atomically persist the durable tombstone and update any cache row, then refetch detail; client response never precedes this local commit. | SmartNotas remains fiscal authority while local readers receive monotonic projection state. |
| `D-CAN-06` | Header layout is `[detail] [cancel] | [documents menu]`; menu aligns to far right. | Matches requested hierarchy and keeps documents secondary. |
| `D-CAN-07` | `FISC-CAN-01` supersedes the module's `provider writes` guardrail only for the approved single-note cancellation endpoint. | Keeps the canonical exception narrow and reviewable. |
| `D-CAN-08` | PostgreSQL atomically elects one leader per `{context,providerId}`; same-process joiners may share its promise, other replicas receive `EmAndamento`, and expired leases transition fail-closed to durable `uncertain`. | Covers tabs, clients, restarts and replicas without pretending provider exactly-once support. |
| `D-CAN-09` | Durable `cancelled` is a terminal tombstone; cancellation commit and every page upsert preserve it atomically even when no cache row existed. | Prevents stale rolling pages from creating/resurrecting an authorized action. |
| `D-CAN-10` | Client disconnect may suppress the response/UI, but cannot abort an already dispatched provider mutation; the internal operation retains its own bounded timeout and reconciliation. | Avoids converting a browser lifecycle event into an unsafe repeatable unknown write. |
| `D-CAN-11` | The frontend owns an explicit cancellation state machine and a semantic `podeCancelarNota` permission. | Prevents scattered flags, stale effects and accidental coupling to occurrence-treatment permission. |
| `D-CAN-12` | Actor admission is charged once per caller; context/upstream quota is charged exactly once by the elected leader. | Prevents joiners from bypassing actor limits or multiplying provider quota accounting. |
| `D-CAN-13` | `uncertain` and `not_cancelled` are durable fail-closed states for Monitor writes; only confirmed provider `Cancelada` reconciliation or an out-of-scope audited operator resolution changes them. | Time alone cannot prove the outcome of an irreversible provider write. |
| `D-CAN-14` | Public detail adds bounded `cancellationState`; durable `cancelled` overrides stale provider status and all non-available states suppress the action. | Detail refetch cannot regress the UI or reoffer a terminal/ambiguous mutation. |
| `D-CAN-15` | Rollback is forward-only for persistence/projection safety: disable route/UI, retain migration, terminal rows, detail overlay and tombstone-aware sync. | Reverting cache writers would invalidate already recorded cancellation facts. |
| `D-CAN-16` | Cancellation commit and every cache upsert serialize per note with the same transaction-scoped PostgreSQL advisory lock; batch locks use canonical key order. | READ COMMITTED snapshots alone do not close the cache-absent insert race. |
| `D-CAN-17` | `SMART_NOTAS_CANCEL_ENABLED` defaults false and independently gates only new cancellation claims/UI availability; durable safety readers/writers ignore the flag. | Provides an executable forward-only kill switch without disabling fiscal reads or erasing prior facts. |

## Decision Baseline (Frozen Before Implementation)

- **State:** proposed, pending `APROVADO`.
- Material changes to roles, retry/idempotency/fence semantics, accepted statuses, terminal-cache precedence, public response or cache failure behavior require renewed approval.

## Architecture Change Governance

- **Applicability:** `required`
- **Rationale:** the implementation preserves the existing port/adapter/service/controller shape, but `FISC-CAN-01` deliberately and narrowly supersedes the canonical `provider writes` exclusion for one irreversible operation.
- **Why this applies:** a new provider write, durable relational state machine and cross-replica coordination become canonical module behavior.
- **Deviation / debt being retired:** provider writes were categorically excluded and no durable idempotency/fence contract existed.
- **Target steady-state after closeout:** exactly one allowlisted cancellation write guarded by signed context identity, PostgreSQL leader/tombstone state and monotonic consumers.
- **Temporary exceptions allowed:** none; process-local-only coordination, timed uncertainty expiry and cache-regressing writes are forbidden.
- **Cutover / removal condition:** migration is applied before `SMART_NOTAS_CANCEL_ENABLED=true` and all backend/frontend consumers pass the protection harness; rollback sets the flag false while preserving operation/tombstone rows and all safety projections.
- **Decision:** `FISC-CAN-01` becomes `Current` only after explicit TODO approval; before product implementation, the fiscal module must publish the endpoint, roles, strict response/error contract, uncertain-result policy and monotonic cache rule.
- **Supersession boundary:** no other SmartNotas write, bulk mutation, issue/reprocess path or client-supplied provider ID is authorized.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `no_material_findings`
- **Decision review evidence / resolution:** fresh round-5 reviewer `Codex-Architecture-Round5` found no material findings at baseline `6b92f716744bdc287ac7f730406d33efbaffb3ef`; all prior architecture findings remain integrated.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** pending delivery review proving the implementation stayed inside `FISC-CAN-01` and its protection harness.
- **No-go handling:** an unresolved objection to the supersession boundary returns the TODO to planning; implementation cannot begin.

| Architecture Finding | Resolution | Evidence |
| --- | --- | --- |
| `ARCH-CAN-01` | Integrated | process-local fence replaced by durable PostgreSQL election, lease-to-uncertain fail-closed state and no temporal write re-enable |
| `ARCH-CAN-02` | Integrated | durable tombstone is consulted atomically by sync upserts even when the cache row was absent |
| `ARCH-CAN-03` | Integrated | protection harness now rejects every provider write outside the exact cancel POST |
| `ARCH-CAN-04` | Integrated | consumer matrix includes central client, semantic permission and fiscal list-cache invalidation |
| `ARCH-CAN-05` | Integrated | per-caller actor admission is separated from one leader context/upstream charge |
| `ARCH-FINAL-CAN-01` | Integrated | exact `200 false` persists terminal `not_cancelled`; no later Monitor write is permitted |
| `ARCH-FINAL-CAN-02` | Integrated | rollback is forward-only and retains migration, rows, detail overlay and tombstone-aware sync |
| `ARCH-FINAL-CAN-03` | Integrated | quota harness asserts every actor admission and exactly one leader context/upstream charge |
| `ARCH-R4-01` | Integrated | cancellation/tombstone and every cache upsert now share a transaction advisory lock; deterministic cache-absent interleavings are required |
| `ARCH-R4-02` | Integrated | `SMART_NOTAS_CANCEL_ENABLED` is the real independent kill switch; durable overlay/locks/writers remain unconditional |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| contract test | cancellation endpoint | Nest application test through JWT + `RolesGuard` | `LEITOR` or unauthenticated access and controller metadata precedence failure | implement-in-this-todo | backend integration suite |
| adapter contract test | SmartNotas POST | exact method/path/headers/no-body/envelope/size/error matrix | redirect, retry, oversized or malformed external response | implement-in-this-todo | adapter tests |
| concurrency test | durable cancellation coordinator | 5/10/20 callers across two service instances, crash/lease expiry | more than one provider POST or transition from expired lease back to write-ready | implement-in-this-todo | PostgreSQL BCI artifact |
| data-integrity test | cancellation tombstone + cache upsert | stale sync before/during/after cancellation with cache row present/absent | create/downgrade from terminal `Cancelada` | implement-in-this-todo | PostgreSQL cache integration test |
| negative contract test | SmartNotas port/adapter | explicit allowlist of existing GETs plus exact cancel POST path | any future issue/edit/reprocess/bulk/provider write | implement-in-this-todo | port/adapter architecture test |
| identity binding test | signed note ID and credentials | tampered ID, context swap and both configured contexts | caller-controlled provider ID/CNPJ/token or cross-context write | implement-in-this-todo | application + adapter tests |
| quota-accounting test | rate coordinator + durable leader | same/cross-process 5/10/20 callers including rejected actors | joiner bypass or more than one context/upstream charge | implement-in-this-todo | BCI raw-state assertions |
| migration test | PostgreSQL + Prisma | apply from empty DB and baseline schema; inspect constraints/indexes | unapplied/invalid migration, missing unique key/state/lease indexes or endpoint startup before migration | implement-in-this-todo | `npm run test:fiscal-migration` against disposable PostgreSQL |
| rollback-mode test | route/UI + detail/cache writers | cancellation disabled with existing terminal rows and stale pages | rollback deletes state or allows status downgrade | implement-in-this-todo | integration + browser evidence |
| serialization test | advisory lock + tombstone/cache transactions | force cache-absent sync and cancellation in both commit orders | snapshot-before-tombstone/insert-after-commit writes stale `Autorizada` or batch deadlock | implement-in-this-todo | deterministic PostgreSQL interleaving test |

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| one durable leader per context + provider ID | `D-CAN-08` | cancellation coordinator | unique relational claim prevents duplicate provider writes across callers/replicas |
| fail-closed uncertainty | `D-CAN-13` | operation state machine | elapsed time or restart never re-enables an outcome-ambiguous write |
| terminal cancellation tombstone | `D-CAN-09` | cache and detail projections | stale provider data cannot resurrect `Autorizada` or the action |
| exact provider-write allowlist | `FISC-CAN-01` | SmartNotas port/adapter | all provider writes except the exact cancel POST remain forbidden |
| shared per-note serialization | `D-CAN-16` | cancellation/cache DB transactions | tombstone and cache-present/absent writers cannot cross unsafely under READ COMMITTED |
| independent kill switch | `D-CAN-17` | route/detail UI availability | rollback blocks new claims without disabling durable safety behavior |

### Prohibited Anti-Patterns

| Prohibited Path | Detection Signal | Why Forbidden | Exception |
| --- | --- | --- | --- |
| in-memory-only mutation fence | provider POST protected only by Map/React flag | fails across restart and replicas | none |
| uncertain state expires to write-ready | time-based delete/retry transition | elapsed time does not prove provider outcome | none |
| cache update without tombstone check | unconditional status upsert | stale page can recreate `Autorizada` | none |
| new provider POST/PATCH/DELETE outside exact cancel path | port/adapter method/path diff | broadens the approved fiscal-write authority | new approved canonical decision only |
| rollback that reverts schema/tombstone-aware writers | migration/diff/runtime test | preserved terminal rows would no longer protect projections | none |

## External Dependency Readiness

| Dependency | Required contract | Evidence | Readiness | Failure handling |
| --- | --- | --- | --- | --- |
| SmartNotas | `POST /notas/{idInterno}/cancelar`, no body, `200 {cancelada,mensagem}`, `401/403/404` | official OpenAPI inspected 2026-09-29 | ready for mocked implementation; live smoke deferred | mapped errors, no retry, detail refresh |
| PostgreSQL cancellation operation + read model | one durable row per context + provider ID, leader lease, fail-closed state and terminal tombstone | additive Prisma model/migration plus existing cache composite key | planned | DB outage blocks new writes before provider dispatch; atomic tombstone/cache/sync rules prevent regression |

## Cancellation Public Contract

- Request: `POST /api/v1/notas/:noteId/cancelar`, no query and no body; route identity is the signed opaque `noteId` only. Any query, parsed body including `{}`, or payload content type maps to `400 CancelamentoFiscalRequisicaoInvalida`.
- Activation: `SMART_NOTAS_CANCEL_ENABLED=false` is the default and returns `503 SmartNotasCancelamentoDesabilitado` before durable claim/rate charge; detail exposes `cancellationState=unavailable` unless a terminal/active row requires a stronger state.
- Provider response admission: HTTP `200`, body at most 16 KiB, exactly properties `cancelada:boolean` and `mensagem:string`; message is trimmed, normalized to LF, 1..2048 code points, and rejects NUL/unsupported control characters.
- Public success: HTTP `200` exact `{cancelled:boolean,message:string}` with private/no-store headers. `cancelled=false` is a known business result, not a transport failure.
- Every request is authenticated and actor-rate-admitted before observing/creating the durable per-note operation; only the atomically elected leader consumes one context/upstream quota unit.

| Condition | HTTP | Public code / response | Retry policy | Reconciliation |
| --- | --- | --- | --- | --- |
| provider `200`, exact `cancelada=true` | `200` | `{cancelled:true,message}` | none | atomic durable `cancelled` tombstone + cache update, list-cache invalidation and detail refetch |
| provider `200`, exact `cancelada=false` | `200` | `{cancelled:false,message}` to original callers | no later Monitor write; durable `not_cancelled` | detail exposes `cancellationState=not_cancelled`; no button |
| no JWT | `401` | existing auth envelope | none automatic | none |
| `LEITOR` | `403` | existing role envelope | forbidden | zero service/adapter call |
| invalid/tampered `noteId` | `400` | existing invalid-note-ID code | none automatic | none |
| provider `401|403` after dispatch | `502` | `SmartNotasCredencialRejeitada` to original caller | persist `uncertain`; no later Monitor write | operational correction/reconciliation |
| provider `404` after dispatch | `409` | `CancelamentoFiscalNaoDisponivel` to original caller | persist `uncertain`; no later Monitor write | detail reconciliation may confirm already canceled |
| provider `429` after dispatch | `503` | `SmartNotasLimiteExterno` + bounded `Retry-After` to original caller | persist `uncertain`; no later Monitor write | operational reconciliation |
| same-process concurrent call | shared result | same bounded result/error from the leader promise | no second POST | per-caller UI ownership still applies |
| other-replica call while lease active | `409` | `CancelamentoFiscalEmAndamento` + bounded `Retry-After` | no POST | read-only detail refetch allowed |
| durable `uncertain` or expired `in_flight` lease | `503` | `CancelamentoFiscalResultadoIncerto` | no retry by Monitor and no temporal expiry | provider reads/reconciliation or audited external resolution only |
| durable `not_cancelled` | `409` | `CancelamentoFiscalNaoDisponivel` | no retry by Monitor | show the bounded message only to original caller; later calls use neutral text |
| timeout/reset/disconnect from provider, provider `5xx`, redirect, malformed/oversized successful response after dispatch | `503` | `CancelamentoFiscalResultadoIncerto` | persist `uncertain`; no automatic/manual Monitor retry | detail refetch without claiming failure or success |
| local admission saturation before dispatch | `503` | `SmartNotasOcupado` | new explicit action later | known zero provider POST |
| cancellation kill switch disabled | `503` | `SmartNotasCancelamentoDesabilitado` | no claim/POST | detail hides action; safety overlay/upserts remain active |

The operation checks the caller abort signal before durable claim/provider dispatch. After dispatch it uses an internal bounded signal and completes independently of client disconnect; only delivery of its result and UI effects remain caller-owned. `in_flight` uses a bounded lease for crash detection, but lease expiry transitions to `uncertain`, never back to write-ready. The operation row persists no provider message, token, actor or recipient data.

### Durable cancellation state machine

`absent -> in_flight -> cancelled|not_cancelled|uncertain`. The composite key is `{contextoFiscal,providerIdInterno}`. `in_flight` stores only an opaque owner token, lease timestamps and nullable `dispatchStartedAt`. A second process cannot claim an active row; an expired lease is atomically changed to `uncertain`. If actor admission, leader/context admission, DB readiness or caller abort fails before claim, the state stays `absent`. If leader admission fails after claim but before dispatch, only that owner token may conditionally delete the row while `dispatchStartedAt IS NULL`. Immediately before network dispatch, the leader atomically stamps `dispatchStartedAt`; every subsequent exception/`401|403|404|429|5xx`/invalid response becomes `uncertain`, except exact `200 true -> cancelled` and exact `200 false -> not_cancelled`. `cancelled`, `not_cancelled` and `uncertain` are fail-closed for future Monitor POSTs. Reconciliation may promote `uncertain|not_cancelled` to `cancelled` only when an authoritative provider read reports `Cancelada`; no automatic transition returns any terminal state to `absent`.

The `cancelled` transition and update of an existing cache row occur in one DB transaction. It and every rolling/bootstrap upsert acquire the same transaction-scoped PostgreSQL advisory lock derived from `{contextoFiscal,providerIdInterno}` before reading/writing operation/cache state. A hash collision may serialize unrelated notes but cannot weaken correctness. Batch upserts acquire locks in canonical key order, then use a status expression that checks both existing cache status and the durable cancellation row. Thus either sync commits first and cancellation updates its row, or cancellation commits first and sync observes the tombstone; cache-present and cache-absent races are closed under READ COMMITTED.

After every provider detail read, one indexed composite-key lookup projects `cancellationState=available|unavailable|in_progress|uncertain|not_cancelled|cancelled`. A durable `cancelled` row overrides stale provider status to `Cancelada`; every non-`available` state suppresses the cancel action. No history scan is allowed.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-CAN-01` | `cancelada=false` may carry a manual municipal procedure. | `artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md` records the official operation description; `C:/Unifast/MonitorNotas/MonitorNotes/frontend/src/paginas/DetalheNota.tsx` is the existing bounded detail-feedback surface. | UI guidance copy and false-result path would simplify. | High | Keep as Assumption |
| `A-CAN-02` | Provider `404` cannot distinguish missing, non-authorized or already canceled. | `artifacts/feature-briefs/uninotas-fiscal-note-cancellation.md` records the official combined response description; `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/smart-notas.adapter.ts` owns current provider error normalization. | Public error mapping could become more specific. | High | Keep as Assumption |
| `A-CAN-03` | Timeout after dispatch has unknown mutation outcome. | `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/smart-notas.adapter.ts` owns the abortable external fetch and `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/smart-notas.port.ts` exposes no provider idempotency key or result token. | Automatic retry could be considered only under a new provider guarantee. | High | Keep as Assumption |
| `A-CAN-04` | All API replicas for one environment use the same PostgreSQL database. | `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/prisma/prisma.service.ts` centralizes the configured `DATABASE_URL`, while `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/fiscal-note-cache.service.ts` already relies on that database for shared fiscal projection state. | Durable election would not coordinate replicas and deployment must block. | High | Keep as Assumption |
| `A-CAN-05` | A matching cache row may be absent. | `C:/Unifast/MonitorNotas/MonitorNotes/backend/src/fiscal-notes/fiscal-note-cache.service.ts` treats the read model as derived and `todos/active/features/TODO-uninotas-fiscal-note-read-model.md` preserves provider-backed detail during partial bootstrap/resume. | Cache update can be mandatory but provider success semantics stay unchanged. | High | Keep as Assumption |

## Execution Plan

### Touched Surfaces

- Prisma additive migration/model; NestJS fiscal port, adapter, service, controller, errors, durable cancellation coordinator, rate accounting and cache service.
- React central HTTP client, fiscal list-cache context, API client, semantic session permission, detail state machine, accessible confirmation component, layout CSS and fiscal tests.
- Foundation fiscal module and this TODO.

### Ordered Steps

1. Publish approved `FISC-CAN-01` and the complete mutation contract in the fiscal module before product code.
2. Add fail-first adapter/port tests for method, path, headers, body absence, 16 KiB/2048-code-point limits, exact envelope and closed error matrix.
3. Add the Prisma operation/tombstone model and a durable coordinator with atomic leader election, owner-token pre-dispatch release, dispatch marker, lease-to-uncertain recovery and separate actor versus leader/context admission; add fail-first BCI tests across independent service instances.
4. Add application-level JWT/`RolesGuard`/empty-request tests, detail-overlay tests and transactional cache tests, including zero adapter calls for unauthorized users, delayed provider detail and cache-present/cache-absent interleavings.
5. Implement provider cancellation with a pre-dispatch caller-abort check, then an internally bounded non-retried POST and non-sensitive audit event.
6. Extend the central HTTP client to carry `AbortSignal`, an allowlisted public error code and bounded `Retry-After`; add frontend parser/state-machine tests for confirmation, duplicate click, durable uncertain guidance, ownership generation, logout/navigation/unmount and failed refetch.
7. Implement semantic permission, list-cache invalidation after known success, status-gated accessible confirmation/result feedback, refetch and three-column responsive header.
8. Apply the migration against disposable empty and baseline PostgreSQL databases, inspect the unique key/state/lease indexes, then run browser/mobile flow, full suites, BCI/FRC/security reviews and deterministic TODO guards.

### Test Strategy

- Test-first for every mutation boundary.
- No live cancellation in automated tests.
- Synthetic opaque IDs and `.test` data only.
- Validate success true/false, properties extra/absent, invalid types/control characters, body/message limits, 401/403/404/429/5xx/redirect/timeout/reset/disconnect, denied role, multi-client duplicate submission and cache-update failure/delay.

### Flow Evidence Planning Matrix

| Flow | Actor / Preconditions | Action | Expected Outcome | Evidence Lane | Status |
| --- | --- | --- | --- | --- | --- |
| authorized success | editor + `Autorizada` detail | confirm cancel | one POST, success feedback, detail reload, local status update | integration + browser | planned |
| manual procedure | editor + provider returns `cancelada=false` | confirm cancel | bounded provider guidance, terminal `not_cancelled`, no cache status change or later button | integration + browser | planned |
| read-only | `LEITOR` | inspect authorized detail / attempt endpoint | no button; backend 403 | integration + browser | planned |
| duplicate/race | editor; request pending | click repeatedly / navigate / logout | one upstream attempt; no late state effect | BCI + FRC + browser | planned |
| uncertain outcome | provider timeout/abort after dispatch | confirm cancel | no auto retry; neutral uncertain message and detail refresh path | integration + browser | planned |
| stale rolling page | sync overlaps confirmed cancellation, cache row present or absent | finish sync before/during/after tombstone commit | `Cancelada` remains terminal in local projection | PostgreSQL integration + BCI | planned |
| delayed provider detail | durable `cancelled`; provider still returns `Autorizada` | reload detail | public status remains `Cancelada`, cancellation state is terminal and button stays absent | service + browser | planned |
| cross-instance claim | two service instances share PostgreSQL | race 5/10/20 callers and expire leader lease | one leader POST; other replicas get in-progress; expired lease becomes durable uncertain | PostgreSQL integration + BCI | planned |
| authorization boundary | no JWT, `LEITOR`, then each editor role | call endpoint through Nest guards | `401`, `403` with zero adapter call, and editor admission | application integration | planned |
| responsive layout | desktop and mobile detail | inspect actions | cancel before divider; menu at far edge; no overflow | browser | planned |

### Frontend / Consumer Matrix

| Producer | Consumer | Contract | Compatibility / Invalidation | Planned Evidence |
| --- | --- | --- | --- | --- |
| `POST /api/v1/notas/:noteId/cancelar` | `DetalheNota` | `{cancelled:boolean,message:string}` | additive endpoint; no existing consumer break | parser + application + browser |
| cache status update | list/export local readers | `providerStatus=Cancelada` for context + provider ID | confirmed true is terminal; stale sync cannot downgrade | cache/service integration |
| detail refetch | `DetalheNota` | existing detail DTO | invalidate current screen generation after mutation | FRC/browser |
| durable cancellation state | detail API + `DetalheNota` | added `cancellationState` allowlist | terminal/ambiguous operations never reoffer action; cancelled overrides stale status | service/parser/browser |
| cancellation result/error | central HTTP client + `DetalheNota` | allowlisted `erro`, bounded `Retry-After`, abort ownership | distinguishes uncertain/in-progress/known failure without message matching | client/parser/FRC |
| confirmed cancellation | `NotasFiscaisContexto` / `CacheFiscal` | invalidate cached fiscal pages | returning to Geral cannot show the pre-cancel page | context/cache/browser |
| session profile | `SessaoContexto` / detail | semantic `podeCancelarNota` | independent from occurrence-treatment semantics | auth/UI tests |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Behavior / Scenario | Preconditions | Command | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| backend full | mutation plus fiscal regressions | mocked provider and local dependencies | `cd backend && npx jest --runInBand` | planned | pending implementation |
| backend migration | additive durable state from empty and baseline schema | disposable PostgreSQL; no production credentials | `cd backend && npm run test:fiscal-migration` | planned | runner added in this TODO; asserts deploy/constraints/indexes/startup fail-closed |
| backend static/build | Nest wiring and types | dependencies installed | `cd backend && npx prisma validate && npx eslint "src/**/*.ts" && npm run build` | planned | pending implementation |
| frontend full | parser, async lifecycle and bundle | dependencies installed | `cd frontend && npm run test:notas && npm run lint && npm run build` | planned | pending implementation |
| browser | success/false/error/timeout/role/layout | fresh local build and intercepted APIs | project-owned fiscal browser runner | planned | pending implementation |

### Runtime / Rollout Notes

- One additive Prisma migration, project-owned `test:fiscal-migration` runner and `SMART_NOTAS_CANCEL_ENABLED` variable are required; the variable defaults to `false`.
- Coordination is PostgreSQL-backed and safe across restarts/replicas that share the environment database. DB unavailability fails before provider dispatch.
- Stage smoke must use a disposable authorized test note explicitly approved for cancellation; automated/live production cancellation is forbidden.
- After deploy, confirm one successful mutation, cache/list convergence and provider/manual-false handling without recording PII.
- Emergency rollback is forward-only: set `SMART_NOTAS_CANCEL_ENABLED=false`; never roll back the schema, terminal rows, detail overlay, advisory locks or tombstone-aware cache writes.

## Plan Review Gate

- **Review state:** completed against frozen baseline
- **Primary risks:** irreversible side effect, unknown timeout outcome, duplicate submission, role bypass, cache divergence and untrusted provider message.
- **Preferred design:** signed context-bound ID, durable DB leader/tombstone state, one elected provider attempt, strict response, explicit confirmation, monotonic projection update and provider detail refetch.
- **Rejected design:** optimistic `Cancelada` before provider response; automatic retry; raw provider ID from browser; allowing `LEITOR`; hiding `cancelada=false` guidance.

### Review Sections

- [x] Architecture — existing port/adapter/service/controller ownership is preserved.
- [x] Code Quality — one mutation method and one public DTO; no alternate direct fetch path.
- [x] Tests — fail-first adapter, authorization, cache, BCI, FRC and browser lanes are planned.
- [x] Performance — one leader upstream write; O(1) composite-key DB claims/updates and no list scan or historical traversal.
- [x] Security — editor-only endpoint, signed context identity, no client credentials/raw ID.
- [x] Elegance — documents remain in the overflow menu; cancellation is a first-class destructive action.
- [x] Structural Soundness — durable election prevents duplicate dispatch and a local post-dispatch failure becomes fail-closed uncertain, never a retryable false failure.

### Issue Cards

- **Issue ID:** `PR-CAN-01`
  - **Severity:** high
  - **Evidence:** provider publishes no idempotency key and existing adapter can time out after dispatch.
  - **Why it matters now:** retrying can repeat an irreversible operation while reporting failure can also be false.
  - **Option A (Recommended):** durable leader election, one provider attempt, permanent fail-closed `uncertain` on ambiguous completion, neutral feedback and read-only detail reload.
  - **Option B:** retry automatically once after timeout; rejected because outcome is unknown.
  - **Option C:** report failure without reload; rejected because it can lie about provider state.
  - **Recommendation:** Option A; prove with BCI/FRC and integration tests.
- **Issue ID:** `PR-CAN-02`
  - **Severity:** high
  - **Evidence:** provider mutation and PostgreSQL cache update cannot share a transaction.
  - **Why it matters now:** cache failure after provider success cannot roll back the cancellation.
  - **Option A (Recommended):** atomically commit durable `cancelled` plus cache update before returning success; all sync writers consult the tombstone.
  - **Option B:** return success before local commit and rely on rolling repair; rejected because stale/absent-row races can resurrect `Autorizada`.
  - **Option C:** return server error after provider success when DB commit fails; rejected because it encourages unsafe retry; instead persist/complete local state as part of the still-running internal operation and emit an operational alert if reconciliation is required.
  - **Recommendation:** Option A; prove cache-present and cache-absent interleavings.

### Failure Modes & Edge Cases

- Status changes between detail render and click: provider decides; frontend handles conflict and reloads.
- Provider returns `200 cancelada=false`: persist terminal `not_cancelled`, make no cache-status success claim and never reoffer the Monitor write.
- Provider succeeds and the first local commit attempt fails: do not relabel the external result or re-POST; the detached internal operation retries only the idempotent local DB reconciliation within its bounded deadline and emits a non-sensitive critical event if durable state still cannot be recorded. The client receives uncertain, never a false failure/success claim.
- Client disconnects after upstream dispatch: suppress caller response/effects, but let the internally bounded shared operation finish; do not retry.
- Two tabs/clients on the same process may join the leader; callers on another replica receive `CancelamentoFiscalEmAndamento`; neither path dispatches a second POST.
- Process death after durable claim converts the expired lease to `uncertain`; time never re-enables the write.
- Provider detail lags after confirmed cancellation: backend overlays the durable tombstone, returns `Cancelada/cancelled` and never reoffers the action.
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

- **Latest audit derivation:** `audit_escalation_guard.py` returned `go` on 2026-09-29 with fingerprint `67f57b20cb75`.
- **Derived delivery floor:** critique `required`; architecture decision/adherence reviews `required`; test-quality audit `required`; final review `required`; dedicated triple review `required`; security review `required`; verification-debt audit `required`; performance/concurrency validation `required` with BCI/FRC mandatory from the risk matrix.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | Cross-stack external mutation with durable DB state machine and explicit failure semantics. |
| `blast_radius` | `cross-stack` | NestJS producer, React consumer and local read model. |
| `behavioral_change_or_bugfix` | `yes` | Adds a user-visible fiscal mutation. |
| `changes_public_contract` | `yes` | Adds an authenticated POST endpoint and response DTO. |
| `touches_auth_or_tenant` | `yes` | Changes role authorization and context-bound provider credentials. |
| `touches_runtime_or_infra` | `yes` | Adds a PostgreSQL migration and cross-replica coordination contract; no deploy-config change. |
| `touches_tests` | `yes` | New contract, integration, race and browser tests. |
| `critical_user_journey` | `yes` | Fiscal cancellation is business-critical and irreversible. |
| `release_or_promotion_critical` | `yes` | Incorrect behavior blocks safe release of the feature. |
| `high_severity_plan_review_issue` | `yes` | Duplicate external writes and cache-absent resurrection were high findings now addressed by the durable design. |
| `explicit_three_lane_request` | `no` | User did not request the dedicated three-lane protocol. |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** big, cross-stack, authenticated, irreversible fiscal mutation with a new public endpoint and durable relational state machine.
- **Impact signals in scope:** `cross-module blast radius|public API|auth|critical user journey`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** frozen TODO, feature brief, fiscal module contract, service/errors/rate/auth/cache anchors and directly touched frontend anchors.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** required; reviewer must differ from the implementing agent and return findings before implementation advice.
- **Canonical multi-lane audit protocol:** `n/a` for planning critique; dedicated triple review remains a delivery gate.
- **Audit session / round evidence:** `n/a`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `no_material_findings`
- **Findings summary:** round-5 fresh no-context critique found no objective material blockers; all earlier findings remain integrated and D-CAN-16/D-CAN-17 were explicitly accepted.
- **Resolution ledger:** findings, if any, will be classified below as `Integrated|Challenged|Deferred`.

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `CRIT-CAN-01` | Integrated | useful | yes | project | `FISC-CAN-01` | Architecture governance now requires a narrow canonical supersession published before product code. |
| `CRIT-CAN-02` | Integrated | useful | yes | project | Initial process-local mitigation was superseded after follow-up review by `D-CAN-08,D-CAN-10,D-CAN-12,D-CAN-13`: durable leader/uncertain state, split admission and disconnect-safe completion. |
| `CRIT-CAN-03` | Integrated | useful | yes | project | `D-CAN-09` and the protection harness require atomic terminal-status preservation across all sync interleavings. |
| `CRIT-CAN-04` | Integrated | useful | yes | project | Cancellation Public Contract closes body/message limits, exact envelope, headers and HTTP/public-code mapping. |
| `CRIT-CAN-05` | Integrated | useful | yes | project | Application-level JWT/`RolesGuard` matrix proves method metadata override and zero downstream calls for denied roles. |
| `CRIT-CAN-06` | Integrated | useful | partial | project | `D-CAN-11` freezes semantic permission, explicit UI states, lifecycle ownership and accessibility evidence. |
| `CRIT-CAN-07` | Integrated | useful | no | none | Bounded review/validation anchors now include service, errors, coordinator, rate, auth and concrete concurrent/interleaving scenarios. |
| `CRIT2-CAN-01` | Integrated | useful | yes | project | Durable cancellation state is the tombstone consulted atomically even when the cache row is absent. |
| `CRIT2-CAN-02` | Integrated | useful | yes | project | Lease expiry transitions permanently to `uncertain`; no timed cleanup can re-enable writes. |
| `CRIT2-CAN-03` | Integrated | useful | partial | project | Central client is in scope for signal, allowlisted error code and bounded Retry-After. |
| `CRIT2-CAN-04` | Integrated | useful | yes | project | Single-replica assumption was removed; PostgreSQL election coordinates shared-database replicas and restarts. |
| `CRIT2-CAN-05` | Integrated | useful | yes | project | Canonical anchor corrected and `fiscal_note_cancellation` capability is added to the module/policy proposal. |
| `CRIT2-CAN-06` | Integrated | useful | yes | project | Empty query/body/content-type rejection and application tests are now explicit. |
| `CRIT2-CAN-07` | Deferred | useful | yes | paced | Delphi skill scope forbids an unapproved tooling edit in this product-planning turn. The unmodified guard is executed through a transparent in-process path-separator compatibility shim; permanent tool fix is a separate Delphi follow-up and does not alter product scope. |
| `CRIT3-CAN-01` | Integrated | useful | yes | project | Complete transition table now separates no-claim/pre-dispatch owner release from every post-dispatch terminal outcome and removes the false-result retry contradiction. |
| `CRIT3-CAN-02` | Integrated | useful | yes | paced | Canonical pattern schema and routing enum were corrected; review/assumption/drift statuses are resolved only after their real runs. |
| `CRIT3-CAN-03` | Integrated | useful | yes | project | Detail now projects indexed durable cancellation state, overlays stale authorized status after confirmed cancellation and suppresses non-available actions. |
| `CRIT3-CAN-04` | Integrated | useful | yes | project | Disposable empty/baseline PostgreSQL migration runner validates application, constraints, indexes and fail-closed startup. |

- **Evidence / reference:** prior findings from `Leibniz`, `Noether`, `Curie` and architecture rounds were integrated; final `manual-bounded/fiscal-cancellation-final-critique-round5` returned empty findings at baseline `6b92f716744bdc287ac7f730406d33efbaffb3ef`.
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** medium cross-stack mutation requires a stable review packet before planning guards.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `feature/uninotas-fiscal-note-cancellation`
- **Baseline commit:** `6b92f716744bdc287ac7f730406d33efbaffb3ef`
- **Baseline push reference:** `origin/feature/uninotas-fiscal-note-cancellation`
- **Gate status:** `no_material_findings`
- **Findings summary:** the complete state machine plus per-note advisory serialization and the executable cancellation-specific kill switch were committed and pushed before final convergence confirmation.
- **Evidence / reference:** `6b92f716744bdc287ac7f730406d33efbaffb3ef` pushed to `origin/feature/uninotas-fiscal-note-cancellation`.
- **Waiver authority / reference:** `n/a`
- **Scope-neutral evidence update:** this freeze record and guard outcomes may be committed after the baseline without changing the frozen feature scope.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** provider semantics, shared-database topology and cache absence are live assumptions that influence failure handling.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-CAN-01,A-CAN-02,A-CAN-03,A-CAN-04,A-CAN-05`
- **Guard command:** `python delphi-ai/tools/assumption_code_coherence_guard.py --todo <todo-path>`
- **Gate status:** `no_material_findings`
- **Findings summary:** all five live assumptions resolve to concrete code/doc anchors; no wrong-code assumption remains.
- **Evidence / reference:** `assumption_code_coherence_guard.py` final run at baseline `6b92f716744bdc287ac7f730406d33efbaffb3ef`.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** approval must use the same mutation, permission, retry and cache semantics reviewed at freeze.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python delphi-ai/tools/review_scope_drift_guard.py --todo <todo-path>`
- **No-go handling rule:** return to review, revalidate material scope with the user and refresh the baseline when necessary.
- **Gate status:** `no_material_findings`
- **Findings summary:** zero material section changes after the pushed baseline; only review/freeze evidence changed.
- **Evidence / reference:** unmodified `review_scope_drift_guard.py` logic executed under `PYTHONUTF8=1` with a separator-only Windows compatibility shim against `6b92f716744bdc287ac7f730406d33efbaffb3ef`.
- **Waiver authority / reference:** `n/a`

## Delivery Review Gates

### Verification Debt Assessment

- **Audit decision:** `required before Completed`
- **Audit status:** `not_run`
- **Why this decision:** big behavior/runtime change with live external-state uncertainty must account for any unexecuted validation.
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
- **Why this decision:** big cross-stack public API/auth/runtime change with irreversible external side effect and durable coordination.
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

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | controller/service/adapter mutation | Nest ownership and explicit failures | direct controller/provider coupling | planned ingestion after approval |
| `delphi-ai/skills/wf-nestjs-change-application-boundary-method/SKILL.md` | new application endpoint | contract-first boundary | implicit request/error semantics | planned ingestion after approval |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | detail/list-cache UI mutation | explicit state ownership and accessible layout | scattered mutation flags | planned ingestion after approval |
| `delphi-ai/skills/wf-react-change-ui-boundary-method/SKILL.md` | action/confirmation consumer | consumer lifecycle evidence | stale effects and message matching | planned ingestion after approval |
| `delphi-ai/skills/rule-prisma-prisma-schema-migration-always-on/SKILL.md` | additive operation-state model | migration/schema compatibility | schema-only or deploy-unsafe change | planned ingestion after approval |
| `delphi-ai/skills/rule-postgresql-postgresql-data-integrity-always-on/SKILL.md` | durable election/tombstone | atomic unique-key transitions | read-then-write races | planned ingestion after approval |
| `delphi-ai/skills/backend-concurrency-idempotency-validation/SKILL.md` | irreversible write | one leader and fail-closed uncertainty | retries or per-process-only fence | planned BCI |
| `delphi-ai/skills/frontend-race-condition-validation/SKILL.md` | abort/navigation/late response | generation ownership | late UI effects | planned FRC |
| `delphi-ai/skills/security-adversarial-review/SKILL.md` | authenticated fiscal mutation | auth/context/message trust boundary | credential/raw-ID leakage | planned security review |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | behavior-defining tests | fail-first boundary coverage | weak status-only assertions | planned test matrix |

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
- **Guard outcome:** `go`
- **Authority preflight evidence:** `todo_authority_guard.py --pre-approval` returned `Overall outcome: preflight-go` with no violations on 2026-09-29.

## Blockers (Current)

- `PENDING_APPROVAL`: implementation requires explicit `APROVADO` after preflight-go.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planning contract awaiting freeze/review/approval.
- **Post-commit/push status:** `complete`
- **Next path/status action:** request the exact explicit approval phrase; implementation remains unauthorized until received and recorded.
