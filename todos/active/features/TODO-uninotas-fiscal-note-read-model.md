# TODO — Estabelecer e estabilizar o read model local de notas fiscais

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Active / Provisional`
- **Created:** `2026-09-29`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário
- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-read-model.md`
- **Story:** `ST-FISCAL-READ-MODEL`

## Lane and authority

- **Lane:** `Tactical TODO`
- **Complexity:** `big`
- **Primary profile:** `Operational / Coder`
- **Technical scope:** `nestjs, react, vite, postgresql, prisma`
- **Current work state:** `planning`
- **Implementation authority:** `pending renewed APROVADO`; as aprovações anteriores cobrem apenas a baseline já entregue e não autorizam esta evolução corretiva.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** executar audit escalation, critique no-contexto, assumption-code coherence, scope-drift e authority preflight a partir da baseline publicada `fe1157216fa43f016685014d117068663e47deb5`.

## Active Work State

- **Work state:** `implementation`
- **Why this state now:** o TODO está sendo refinado para uma nova implementação corretiva após o smoke de stage revelar bootstrap que não converge e exportação bloqueada.
- **Exit condition:** baseline corretiva revisada, aprovada, implementada e validada na branch `release/uninotas`.

## Provisional Notes

- **Missing for production-ready:** bootstrap histórico imutável e segmentado, cobertura por intervalo, leitura não bloqueante, exportação local condicionada ao período e reparação do estado de stage.
- **Revisit criteria:** todos os critérios `DOD-RM-C*` e `VAL-RM-C*` aprovados e evidenciados, incluindo smoke de stage com revisão exata em execução.
- **Dependencies unblocked:** o TODO de cancelamento pode continuar em planejamento, mas sua implementação não deve preceder a estabilização deste read model.

## Implementation Intent

- **Current delivery:** estabilizar o read model implantado para que listagem/paginação sejam sempre locais e não bloqueantes, exportações locais dependam somente da cobertura do intervalo solicitado e a sincronização histórica converja em janelas fechadas.
- **Planned next steps:** após esta correção, retomar o TODO independente de cancelamento fiscal; isso não está autorizado aqui.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** mantém Smart Notas como autoridade e reutiliza PostgreSQL/Nest scheduler existentes, sem introduzir fila, réplica ou armazenamento fiscal adicional.

## Execution Lane Tracking

- **Local implementation branches:** `MonitorNotes:release/uninotas`, `uninotas-foundation:main`
- **Promotion lane path:** `release/uninotas -> PR definido pelo usuário`; Foundation permanece na autoridade canônica `main` e sua publicação segue governança própria.
- **Lane-promoted threshold for this TODO:** PR da branch `release/uninotas` aprovado/mesclado no alvo informado pelo usuário.
- **Production-ready threshold for this TODO:** revisão exata implantada em Railway Stage, reparação concluída e smoke autenticado/list-export aprovado.

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| corrective read model | `release/uninotas@pending` | `pending` | `n/a until target lane is confirmed` | `n/a until target lane is confirmed` | `not implemented` |
| canonical Foundation contract | `main@pending review baseline` | `n/a` | `n/a` | `n/a` | `planning diff only` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** schema/state concretization needed for approved interval coverage, tests/fixtures, exact UI copy, non-destructive legacy-row repair and bounded observability that serve the same list/export correction.
- **Must update or split the TODO:** storing new PII/detail data, partial export, deep historical reconciliation policy, new worker/queue/replica, provider quota/credential changes, cancellation or any Smart Notas mutation.

## Approval

- **Approved by:** `pending`
- **Approval scope:** `pending renewed APROVADO for the corrective evolution defined in D-RM-C01..D-RM-C10`
- **Execution not authorized by approval:** nenhuma implementação corretiva, alteração de banco, reparação de stage, deploy, credencial, quota ou topologia está autorizada enquanto este campo permanecer pendente.
- **Renewed approval required when:** mudar janela histórica, semântica de cobertura/exportação, contrato público, estratégia de recuperação, schema, topologia, limites, riscos ou evidências obrigatórias.

## Historical Approval Evidence — Delivered Baseline Only

- **Original approval:** `APROVADO o escopo e as premissas recomendadas do TODO.` (`2026-09-29`).
- **Original scope:** persistência derivada, sincronização resumível, leitura local condicionada, testes e documentação; sem deploy, credenciais ou escrita em `logs`.
- **Prior renewed approval:** `APROVADO o fluxo de carga histórica única e reconciliação diária do TODO.` (`2026-09-29`).
- **Prior renewed scope:** bootstrap de 365 dias, reconciliação de hoje/ontem, fallback local, metadados de frescor e detalhe/PDF/XML no provedor.
- **Authority boundary:** estas evidências explicam a baseline instalada em stage, mas foram explicitamente encerradas para a nova evolução porque o comportamento observado invalida premissas materiais de convergência e exportação.

## Historical Decision Baseline — Delivered 2026-09-29

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

## Corrective Evolution — Pending Renewed Approval

### Observed Symptoms and Evidence

- Stage keeps returning `readModel.coverage=partial`, which makes the React list continuously show `Carga histórica em andamento. Exibindo as notas já armazenadas.`
- CSV export returns the public `SmartNotasIndisponivel` message even when PostgreSQL already contains notes for the requested period.
- `FiscalNoteCacheService.list()` awaits `ensureBootstrap()` before the local query; `exportAll()` rejects every state other than `bootstrap_complete` before reading cached rows.
- The 365-day bootstrap includes the current day, freezes `total`, `totalPages` and `perPage`, and rejects any later page whose totals changed. New notes arriving during a long traversal can therefore make the checkpoint permanently incompatible with the provider's next response.
- The persisted-error mapper preserves only `SmartNotasLimiteExterno`; pagination inconsistency, timeout and unexpected failures are collapsed into `SmartNotasIndisponivel`, hiding the actual reason.
- The existing seven cache-service tests pass but keep provider totals immutable. They do not cover a changed total after checkpoint resume, a stale `bootstrap_running` record after process restart, interval-complete export during global partial coverage, or truthful error mapping.
- The local `DATABASE_URL` inspected on `2026-09-29` contained zero read-model sync/cache rows, so the exact stage `erroCodigo` remains runtime evidence to collect. This does not invalidate the code-level failure path above.

### Decision Baseline (Frozen Before Implementation)

| ID | Decision | Corrective baseline | Prior decision relationship |
| --- | --- | --- | --- |
| `D-RM-C01` | Stable historical horizon | Historical bootstrap covers the configured 365-day horizon only through `D-2` in `America/Sao_Paulo`; today and yesterday never belong to a historical page walk. | Refines `D-RM-06`; intentionally supersedes the delivered moving 365-day window ending today. |
| `D-RM-C02` | Windowed bootstrap | Divide the historical horizon into durable, non-overlapping calendar-month windows. Each window has independent page/checkpoint/error/completion state; a changed provider total restarts only that idempotent window, never the full history. | Refines `D-RM-06`; no prior module decision defines window ownership. |
| `D-RM-C03` | Rolling independence | Reconcile `D-1..D` every 15 minutes from application startup even while historical windows remain incomplete. Historical progress cannot prevent current notes/statuses from being refreshed. | Supersedes the delivered `bootstrap_complete` prerequisite for rolling sync. |
| `D-RM-C04` | Non-blocking list | `GET /api/v1/notas` without `documento` reads PostgreSQL immediately and may only trigger/nudge synchronization in background; it never awaits a historical provider traversal. | Intentionally supersedes the request-blocking implementation while preserving `D-RM-E02`. |
| `D-RM-C05` | Interval-aware coverage | Coverage is evaluated for the requested fiscal context and date interval, not from one global bootstrap flag. A fully covered interval may return a valid empty page; a partially covered interval may return stored rows with explicit partial/progress metadata, but cannot masquerade as complete. | Refines `D-RM-02` and `D-RM-E03`. |
| `D-RM-C06` | Complete-only CSV | `GET /api/v1/notas/exportar` without `documento` reads PostgreSQL when the exact requested interval is fully covered, regardless of unrelated incomplete windows. Partial intervals fail before CSV generation with `409 ExportacaoFiscalCoberturaIncompleta`; partial CSV is forbidden. | Intentionally supersedes global `bootstrap_complete` gating and module `FISC-EX-02`. |
| `D-RM-C07` | Truthful failure semantics | Read-model incompleteness is never mapped to `SmartNotasIndisponivel`. That code remains reserved for a real provider operation/failure. List/export expose explicit sync/coverage states and retain the last sanitized internal sync reason for observability without leaking provider payloads. | Refines `D-RM-E03`; preserves the common error envelope. |
| `D-RM-C08` | Stage recovery | Preserve all cached rows. Do not mark coverage complete from row count alone and do not delete/reset the whole cache. Retire the legacy moving-window sync record, seed stable windows, and verify each incomplete window through bounded provider reads before marking it complete. | Preserves `D-RM-01`, `D-RM-05` and the no-data-loss intent of `D-RM-E01`. |
| `D-RM-C09` | Provider-owned detail/documents | Detail, PDF, XML and `documento`-filtered reads remain provider-backed; this correction does not persist recipient document or expand the summary projection. | Preserves `D-RM-03`, `D-RM-E05`, `FISC-DOC-*` and PII boundaries. |
| `D-RM-C10` | Runtime boundary | Use the existing NestJS process and scheduler in the current single-replica topology. No queue, worker service, Railway topology, provider quota or credential change is authorized. | Preserves the prior topology limitation and requires a separate TODO before horizontal scaling. |

### Corrective Acceptance Criteria

- A list request over cached data returns from PostgreSQL without waiting for Smart Notas, including while historical windows are pending or failed.
- Rolling `D-1..D` starts independently and remains idempotent while historical windows run.
- A provider total change after a checkpoint cannot trap the entire history; only the affected closed window is restarted and eventually converges.
- Coverage is queryable by context/date interval, and an interval-complete empty result is distinguishable from an unknown/incomplete interval.
- Export over a covered interval performs zero provider calls; export over an incomplete interval returns `409 ExportacaoFiscalCoberturaIncompleta` and produces no CSV bytes.
- Stored rows survive every bootstrap failure/retry and the legacy stage state is repaired without blind completion or full-cache deletion.
- The UI no longer shows a permanent generic historical warning after the requested interval is covered and presents an actionable synchronization message when it is not.
- `SmartNotasIndisponivel` is emitted only for an actual provider call that returned that condition.
- Detail, PDF, XML and document-filtered paths retain their existing provider-backed contracts.

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
- **Current governed action:** `todo-approval`
- **Selected role:** `primary-chat`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `max`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree authorization:** not requested; no worktree or auxiliary checkout may be created.
- **Profile:** `Operational / Coder`
- **Scope:** `nestjs, react, vite, postgresql, prisma`
- **Package-first result:** Delphi package query attempted, but unavailable because the environment has no executable `bash/WSL`; no new dependency will be introduced. Node capability audits for NestJS and Prisma returned `ready`.
- **Guard outcome:** `pending`
- **Guard evidence:** rerun required after the corrective baseline is committed/pushed and before approval review.

## Historical Execution Plan — Delivered Baseline

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

## Contract Boundary

- Smart Notas permanece a autoridade fiscal.
- A projeção local só pode servir dados com contexto, cobertura e frescor conhecidos.
- Ausência, atraso, lacuna, erro de sincronização ou status possivelmente desatualizado devem ser expostos como estado operacional; não podem produzir sucesso vazio.
- Unifast e Prosperar permanecem `FiscalIssuerContext` independentes.
- `logs` não participa da carga, reconciliação ou preenchimento da projeção.

## Scope

- [ ] Substituir o bootstrap móvel de 365 dias por janelas mensais fechadas até `D-2`, com checkpoint e estado durável por janela/contexto.
- [ ] Executar reconciliação `D-1..D` independentemente do bootstrap histórico e sem bloquear listagem/exportação.
- [ ] Calcular cobertura do intervalo solicitado a partir das janelas concluídas e da janela rolling aplicável.
- [ ] Fazer listagem/paginação sem `documento` lerem PostgreSQL imediatamente, divulgando cobertura, sincronização, frescor e progresso de modo explícito.
- [ ] Fazer exportação sem `documento` ler PostgreSQL quando o intervalo estiver coberto e rejeitar cobertura incompleta com erro próprio antes de gerar CSV.
- [ ] Preservar e reaproveitar as notas já armazenadas; migrar/aposentar com segurança o registro legado de bootstrap sem declarar cobertura não comprovada.
- [ ] Corrigir o mapeamento de erros para separar indisponibilidade real do provedor de projeção incompleta/inconsistente.
- [ ] Atualizar o contrato React e os avisos de lista/exportação para os estados corretos, sem download parcial.
- [ ] Atualizar o módulo canônico `fiscal-notes-and-documents.md` para substituir a travessia histórica por requisição descrita em `FISC-EX-02/FISC-EX-04` pela leitura local coberta.
- [ ] Adicionar regressões fail-first, integração PostgreSQL, planos/limites e smoke autenticado de stage com revisão exata atestada.

## Out of Scope

- Emissão, cancelamento, alteração ou qualquer endpoint mutável do Smart Notas.
- Escrita, normalização ou mudança de semântica da tabela externa `logs`.
- Cache de URLs de PDF/XML ou armazenamento indiscriminado de payloads com dados pessoais.
- Agregação entre contextos fiscais.
- Deploy Railway, mudança de credenciais/quota ou alteração do cutover Smart Notas já aberto.
- Exportação parcial, botão para “baixar o que já existe” ou qualquer CSV apresentado como completo sem cobertura integral do intervalo.
- Fila/worker externo, nova réplica, lease distribuído, alteração do scheduler de infraestrutura ou operação destrutiva direta no banco de stage.
- Persistência de documento do tomador, payload bruto, PDF, XML ou URL efêmera.

## Historical Canonical Anchors — Delivered Baseline

- `foundation_documentation/project_constitution.md`
- `foundation_documentation/modules/fiscal-notes-and-documents.md`
- `foundation_documentation/modules/events-and-classification.md`
- `foundation_documentation/modules/operational-monitoring.md`
- `foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-read-model.md`

## Architecture Change Governance

- **Applicability:** `required`.
- **Why this applies:** a baseline entregue criou dependência request→bootstrap, um checkpoint global incompatível com totais móveis e um gate global de exportação; o TODO também precisa superseder decisões canônicas de exportação ainda orientadas ao provedor.
- **Deviation / debt being retired:** bootstrap histórico móvel terminando no dia atual, rolling condicionado ao bootstrap, listagem aguardando sync, exportação bloqueada por estado global e erro de cobertura disfarçado como indisponibilidade externa.
- **Target steady-state after closeout:** PostgreSQL é a projeção derivada usada imediatamente por listagem e por exportações de intervalos cobertos; Smart Notas alimenta janelas históricas fechadas e rolling recente em background e continua autoridade de detalhe/documentos.
- **Temporary exceptions allowed:** durante a reparação inicial, intervalos ainda não verificados podem ser listados como parciais, mas nunca exportados como completos.
- **Cutover / removal condition:** todos os contextos possuem janelas históricas/rolling coerentes, o registro legado está aposentado, o módulo canônico descreve o novo caminho e o smoke de stage comprova lista não bloqueante e exportação local.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| autoridade externa + projeção derivada | `P-6`, `D-RM-C01..C09` | Smart Notas/PostgreSQL | evita transformar cache em autoridade fiscal |
| cobertura por intervalo antes de exportar | `D-RM-C05/C06` | list/export | impede sucesso vazio ou CSV incompleto |
| sync idempotente fora da requisição | `D-RM-C02..C04` | NestJS scheduler/read path | remove latência e quota do caminho interativo |
| erro público fiel ao estado | `D-RM-C07` | API/React | impede diagnóstico falso de indisponibilidade |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| aguardar bootstrap em `list()`/`exportAll()` | teste observa chamada provider antes do DB read | recoloca paginação e quota no request | none |
| congelar total móvel em janela que inclui `D-1` ou `D` | histórico termina depois de `D-2` | pode impedir convergência permanente | none |
| usar `bootstrap_complete` global como autorização de intervalo | export coberto falha por janela alheia | mistura cobertura não relacionada | none |
| mapear projeção incompleta para `SmartNotasIndisponivel` | erro público sem chamada provider | mensagem operacionalmente falsa | none |
| marcar cobertura por contagem local ou SQL manual | estado completo sem travessia/critério comprovado | pode esconder lacunas/duplicidades | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| unit test | cache/sync state machine | `fiscal-note-cache.service.spec.ts` | total muda após checkpoint, restart de janela e rolling independente | `implement-in-this-todo` | fail-first + suite completa |
| integration test | Prisma/PostgreSQL coverage | real local PostgreSQL fixture | gaps/overlaps, contexto cruzado, aposentadoria legada e export coberto | `implement-in-this-todo` | migration/schema check + query assertions |
| contract test | list/export errors and metadata | Nest application specs | cobertura incompleta disfarçada de provider error ou CSV parcial | `implement-in-this-todo` | exact status/code/body/header assertions |
| browser test | React list/export | existing frontend E2E/unit runner | aviso permanente, erro incorreto ou download parcial | `implement-in-this-todo` | source-owned test + stage smoke |
| performance/load | DB pagination/export + sync pacing | EPS/RLS artifacts | provider call on covered export, query regression or sync storm | `implement-in-this-todo` | machine-checkable `pcv-1` evidence |

## Definition of Done

- [ ] `DOD-RM-C01` Histórico é particionado em janelas mensais fechadas até `D-2`, com retomada/restart local e sem perda das notas já armazenadas.
- [ ] `DOD-RM-C02` Rolling `D-1..D` executa a cada 15 minutos independentemente da conclusão histórica.
- [ ] `DOD-RM-C03` Listagem/paginação sem `documento` nunca aguarda provider e representa corretamente intervalos completos, parciais e vazios.
- [ ] `DOD-RM-C04` Exportação sem `documento` usa somente PostgreSQL para intervalo coberto e retorna `409 ExportacaoFiscalCoberturaIncompleta` sem bytes CSV quando incompleto.
- [ ] `DOD-RM-C05` Estado legado de stage possui caminho idempotente e não destrutivo de reparação; nenhuma cobertura é marcada completa por inferência de contagem.
- [ ] `DOD-RM-C06` Erros públicos distinguem provider real de sincronização/cobertura local, e a UI apresenta mensagens acionáveis.
- [ ] `DOD-RM-C07` Detalhe, PDF, XML e filtro `documento` continuam provider-backed e os contextos fiscais permanecem isolados.
- [ ] `DOD-RM-C08` Módulo canônico, testes, builds, lint, Prisma/PostgreSQL, EPS/BCI/RLS e evidência de stage estão coerentes com a decisão aprovada.

## Validation Steps

- [ ] `VAL-RM-C01` Executar fail-first para total alterado após checkpoint, processo reiniciado, rolling concorrente, intervalo coberto/incompleto e mapeamento fiel de erro.
- [ ] `VAL-RM-C02` Executar suites completas backend/frontend, lint, builds e validação/generação Prisma.
- [ ] `VAL-RM-C03` Em PostgreSQL local real, validar janelas sem gap/overlap, isolamento, migração/reparação legada e planos de paginação/exportação.
- [ ] `VAL-RM-C04` Validar concorrência entre bootstrap, rolling, listas e exports sem duplicidade, perda de checkpoint ou tempestade upstream.
- [ ] `VAL-RM-C05` Medir exportações pequena/média/20.000 linhas e paginação DB, comprovando zero chamadas Smart Notas no intervalo coberto.
- [ ] `VAL-RM-C06` Validar no React aviso parcial/progresso, remoção do aviso após cobertura e ausência de download em `409`.
- [ ] `VAL-RM-C07` Após deploy autorizado, atestar `branch@sha`, consultar estado agregado redatado, reparar sem destruição e executar smoke autenticado de lista/exportação no stage.
- [ ] `VAL-RM-C08` Executar guards TODO/diff/completion, auditoria de qualidade de testes, revisão final no-contexto e consolidação do módulo.

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
| `MonitorNotes` | `.` | `release/uninotas@5cd1d5bc0c91c784ac4be985baba8a21fdc702f4` | `working_tree` |
| `uninotas-foundation` | `C:/Unifast/uninotas-foundation` | `main@9d2f6b03b16bbf8c97b1a61c689dbaca92a6b68a` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/schema.prisma` | `M` | interval coverage/state contract if the current model cannot encode the approved windows safely |
| `MonitorNotes` | `backend/prisma/migrations/**` | `A` | additive, non-destructive compatibility migration if schema changes are required |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `A, M` | windowed bootstrap, rolling independence, local reads, truthful errors and regression tests |
| `MonitorNotes` | `backend/src/common/filters/**` | `M` | public error mapping for incomplete read-model coverage if centrally owned there |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | interval coverage/progress contract and export error handling |
| `MonitorNotes` | `frontend/src/notas/**` | `A, M` | metadata normalization/cache/export controller regression coverage |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | actionable partial/complete synchronization state |
| `MonitorNotes` | `frontend/e2e/**` | `A, M` | browser-visible list/export regressions when this is the source-owned runner |
| `MonitorNotes` | `frontend/src/**/*.spec.ts*` | `A, M` | frontend contract/render regressions |
| `MonitorNotes` | `delphi-ai` | `M` | pre-existing workspace link reflects the separately approved Delphi helper commit; excluded from product staging |
| `MonitorNotes` | `foundation_documentation` | `M` | pre-existing Foundation workspace link reflects TODO evidence; excluded from product staging |
| `MonitorNotes` | `uninotas-foundation` | `T` | pre-existing tracked-gitlink versus workspace-symlink topology; excluded from product staging |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-read-model.md` | `M` | approval, decisions and delivery evidence |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | canonical local-read/export/coverage contract and superseded provider traversal decisions |
| `uninotas-foundation` | `artifacts/dependency-readiness.md` | `M` | redacted stage/provider readiness evidence via DevOps handoff if runtime status is refreshed |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A, M, D, R` | secrets/local environment are excluded |
| `MonitorNotes` | `backend/src/logs/**` | `A, M, D, R` | external logs remain outside the read model |
| `MonitorNotes` | `backend/src/fiscal-notes/smart-notas.adapter.ts` | `M` | provider route/auth contract is unchanged |
| `MonitorNotes` | `Dockerfile`, `railway.json`, `.github/**` | `A, M, D, R` | deployment/CI topology is outside this evolution |
| `uninotas-foundation` | `project_constitution.md`, `system_roadmap.md` | `M` | no strategic stage or constitutional invariant change is authorized |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| workspace links `delphi-ai`, `foundation_documentation`, `uninotas-foundation` | noise / governed support topology | links predate this product implementation; Delphi and Foundation changes were separately authorized and versioned in their owning repositories | retain links locally; exclude them from MonitorNotes staging | already authorized by user during this TODO session |

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-read-model.md`
- **Primary story ID:** `ST-FISCAL-READ-MODEL-CORRECTION`
- **Why this is the right current slice:** uma única experiência operacional — listar, paginar e exportar notas pelo read model sem ficar presa ao bootstrap — reúne a correção de sincronização, cobertura, erros e aviso React na mesma aprovação.
- **Direct-to-TODO rationale:** `n/a`; o feature brief existente continua válido e esta evolução corrige sua entrega.

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `nestjs, react, vite, postgresql, prisma, cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality` para critique/auditorias e `operational-devops` somente para atestação/deploy/smoke de stage.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-tester-quality` | TODO `big`, bugfix arquitetural e contrato público | bounded TODO/code/test/evidence packages | `planned before approval and delivery` |
| `operational-coder` | `operational-devops` | deploy/revision attestation, read-only stage sync-state capture and authenticated smoke are forbidden to normal coder execution | Railway Stage / dependency readiness | `planned; no runtime mutation authorized by this TODO alone` |

## Complexity

- **Level:** `big`
- **Checkpoint policy:** `section-by-section`
- **Why this level:** altera state machine, semântica de cobertura, consultas/exportação, contrato público, UI e reparação de dados derivados já implantados.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `foundation_documentation/modules/events-and-classification.md` apenas para preservar a transição de ownership de `note_read_model`; nenhum contrato de `logs` muda.
- **Planned decision promotion targets:** `Canonical Decision Register`, `Purpose, Owned Entities, and Workflows`, `Locally implemented filtered CSV export boundary`, `API Endpoint Definitions`, `Export success and transport boundary`, `Export traversal`, `Errors`, `Limits and admission`, `Observability`, `Invariants`.
- **Module decision consolidation targets:** novas decisões `FISC-RM-*` para janelas/cobertura/leitura local e supersessão explícita de `FISC-EX-02/FISC-EX-04` onde elas exigem travessia direta do provedor.

## Decision Pending

- [ ] `none`; as opções materiais foram comparadas no Plan Review e a direção recomendada está congelada em `D-RM-C01..C10`, aguardando apenas aprovação humana e reviews obrigatórios.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `fiscal-notes-and-documents#FISC-EX-01` | export aplica um contexto e todos os filtros | `Preserve` | `Canonical Decision Register` |
| `fiscal-notes-and-documents#FISC-EX-02` | backend percorre páginas do provedor para cada export | `Supersede (Intentional)` | `D-RM-C04/C06`; local covered export becomes canonical |
| `fiscal-notes-and-documents#FISC-EX-03` | Buffer completo antes da resposta | `Preserve` | CSV atomic application boundary remains |
| `fiscal-notes-and-documents#FISC-EX-04` | consistência detectável da paginação provider, sem snapshot | `Supersede (Intentional)` | provider checks move to sync windows; export consistency becomes DB coverage/query based |
| `fiscal-notes-and-documents#FISC-EX-05..10` | HTTP/CSV/security/limits/coordinator contracts | `Preserve`, adapting only provider-page admission no longer used by covered local export | module sections cited above |
| `fiscal-notes-and-documents#FISC-VIS-01..03` | positive response allowlists and signed IDs | `Preserve` | no summary/detail field expansion beyond read-model metadata |
| `fiscal-notes-and-documents#FISC-DOC-01..03` | PDF/XML provider-backed | `Preserve` | `D-RM-C09` |
| `fiscal-notes-and-documents#FISC-CAN-01` | proposed cancellation | `Out of Scope` | cancellation TODO remains independently gated |
| `events-and-classification#note_read_model transition` | legacy module remains current owner until cutover | `Preserve` | scope policy `note-read-model-001` stays planned |

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-RM-C01` | Smart Notas has no transactional snapshot/cursor/stable-order contract for list pagination. | canonical module `FISC-EX-04`; current adapter/list contract | provider-native delta/snapshot could simplify sync and would require contract refresh | `High` | `Keep as Assumption` |
| `A-RM-C02` | The moving total can change because the delivered bootstrap includes the current day and freezes metadata across pages/retries. | `fiscal-note-cache.service.ts:164-181,249-303,326-358` | if provider guarantees immutable totals, windowing remains bounded and safer but root cause may be another stored error | `High` | `Keep as Assumption` |
| `A-RM-C03` | Existing sync/cache schema may encode per-window rows through `(contextoFiscal,dataInicio,dataFim)` without a destructive migration. | `schema.prisma:91-109` | add an expand-only migration and validate both baseline/empty schemas | `Medium` | `Keep as Assumption` |
| `A-RM-C04` | Stage runs one API replica. | dependency readiness records `replicas=1` | distributed lease becomes required before deployment | `Medium` | `Block deployment, not planning` |
| `A-RM-C05` | The exact stage failure row/error code is unknown from the local DB. | local read-only query returned empty sync/cache; user supplied public stage symptoms | operational repair branch may differ, but list/export contract remains valid | `High` | `Keep as Assumption` |
| `A-RM-C06` | Historical statuses older than `D-1` may change externally, but broad periodic deep reconciliation is outside this correction. | Smart Notas authority + no changed-since contract | stale older status remains residual risk; cancellation overlay covers only Monitor-owned cancellation | `Medium` | `Keep as Assumption; document residual risk` |

## Execution Plan

### Touched Surfaces

- `backend/src/fiscal-notes/**`, conditional `backend/src/common/filters/**`
- conditional `backend/prisma/schema.prisma` and additive migration
- `frontend/src/api/notas.ts`, `frontend/src/notas/**`, `frontend/src/paginas/ListaNotas.tsx`, source-owned tests
- `foundation_documentation/modules/fiscal-notes-and-documents.md` and this TODO

### Ordered Steps

1. Add fail-first tests for moving totals/checkpoint restart, non-blocking list, independent rolling, interval coverage, complete-only local export and truthful errors.
2. Model deterministic monthly windows through `D-2`, including gap/overlap validation, legacy-state retirement and per-window restart/backoff.
3. Decouple sync triggering from list/export request completion and start rolling/background historical work under the existing scheduler.
4. Implement interval coverage queries and local list/export semantics, preserving context/filter/order/20,000-row CSV bounds.
5. Update public read-model/error contract and React notices/download lifecycle.
6. Implement non-destructive legacy-state repair and verify against empty/baseline PostgreSQL databases; do not mutate stage directly from this lane.
7. Update the canonical fiscal module, run CI-equivalent/performance/concurrency/security gates, then hand off deployment/smoke to DevOps.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** production-like stage symptoms passed all existing immutable-total unit tests; regression must be proven before changing the state machine.
- **Fail-first targets:** provider total changes after page 1/resume; stale running/failed checkpoint after process restart; rolling while history incomplete; covered empty list; covered export with unrelated incomplete window; incomplete export exact `409`; no provider call on covered reads; exact provider-error preservation.

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Why now:** code/test inspection already demonstrates the missing cases and the user requested TODO refinement, not test changes before approval.
- **Target symptom:** `n/a`
- **Allowed surfaces:** `none before APROVADO`
- **Forbidden surfaces reaffirmed:** `production code|tests|runtime/config/deploy|canonical docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status:** `not_run`
- **Findings summary:** existing 7/7 unit suite passes while omitting moving-total and interval-coverage scenarios.

## Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fiscal list/pagination during partial history | visible warning/results/pagination | `web-only` | Playwright readonly + authenticated stage smoke | `no` | `yes` | source-owned browser spec plus revision-attested stage request | n/a |
| covered/partial/empty interval semantics | backend projection consumed by list | `web-only` | Playwright readonly + API integration | `no` | `yes` | deterministic DB fixture and stage period with known data | n/a |
| CSV export covered vs incomplete | visible download/error | `web-only` | Playwright readonly/download + API integration | `no` | `yes` | assert download only for covered interval and zero-byte/error for incomplete | n/a |
| detail/PDF/XML/document filter regression | provider-backed unchanged contract | `web-only` | existing integration/browser regression | `no` | `no` for automated; stage smoke only if safe | existing mocked provider tests | n/a |

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend cache focused | state machine correction | moving total, restart, rolling, coverage/export/error semantics | deterministic provider pages + sync rows | `cd backend && npx jest fiscal-note-cache.service.spec.ts --runInBand` | `Local-Implemented` | `planned` | pending | diagnostic plus fail-first evidence |
| backend full | API/error/provider regressions | all fiscal endpoints and common error envelope | normal test env, no live provider | `cd backend && npx jest --runInBand` | `Local-Implemented` | `planned` | pending | broad regression |
| backend static/build | Nest/TypeScript/Prisma | compile and schema/client coherence | installed dependencies | `cd backend && npx prisma validate && npm run prisma:generate && npx eslint "src/**/*.ts" && npm run build` | `Local-Implemented` | `planned` | pending | use repo-owned versions |
| PostgreSQL real integration | relational window/coverage/repair path | gaps, overlaps, legacy row and indexed list/export | disposable empty + baseline schema fixtures | project-owned local PostgreSQL runner/Prisma commands resolved during execution | `Local-Implemented` | `planned` | pending | no stage mutation |
| frontend unit/build | metadata/messages/download lifecycle | partial/complete notices and incomplete export | deterministic API fixtures | `cd frontend && npm run test:notas && npm run lint && npm run build` | `Local-Implemented` | `planned` | pending | add source-owned spec if current runner lacks rendering |
| browser flow | actual list/export UX | partial notice disappears when covered; incomplete export downloads nothing | locally published exact checkout + deterministic backend fixture | project-owned browser runner discovered during execution | `Local-Implemented` | `planned` | pending | freshness attestation required |

## Runtime / Rollout Notes

- Default rollout is expand/repair/switch without deleting cache rows. If schema expansion is unnecessary, code must still handle legacy sync rows deterministically.
- Feature flags or deploy topology changes are not assumed. Stage repair runs only after the exact deployed revision and target database are attested through the DevOps handoff.
- A rollback must disable new scheduling/read switching without erasing coverage/cache metadata. No manual `UPDATE ... bootstrap_complete` is an acceptable rollback or repair.
- The stage provider is currently `rate-limited/degraded` from user-visible evidence; validation must use bounded calls and redacted aggregate logs.

## Plan Review Gate

- **Status:** `prepared-pre-freeze`; these cards are planning material and must be rerun/confirmed from the committed review baseline before they become gate-satisfying.

### Review Sections

- [ ] Architecture — prepared pre-freeze
- [ ] Code Quality — prepared pre-freeze
- [ ] Tests — prepared pre-freeze
- [ ] Performance — prepared pre-freeze
- [ ] Security — prepared pre-freeze
- [ ] Elegance — prepared pre-freeze
- [ ] Structural Soundness — prepared pre-freeze

### Issue Cards

- **Issue ID:** `ARCH-RM-C01`
  - **Severity:** `high`
  - **Evidence:** `backend/src/fiscal-notes/fiscal-note-cache.service.ts:164-181,249-303,326-358`
  - **Why it matters now:** a mutable end date plus frozen totals can make the global checkpoint permanently non-convergent.
  - **Option A (Recommended):** closed monthly historical windows through `D-2`, with restart limited to the changed window.
    - **Effort:** medium; **Risk:** low; **Blast radius:** module; **Maintenance:** medium; **Performance:** improves; **Elegance:** improves; **Structural soundness:** improves.
  - **Option B:** keep one 365-day window but restart it whenever totals change.
    - **Effort:** low; **Risk:** high; **Blast radius:** module; **Maintenance:** high; **Performance:** regresses; **Elegance:** regresses; **Structural soundness:** regresses.
  - **Option C (Do Nothing):** keep resuming the incompatible checkpoint.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-stack; **Maintenance:** high; **Performance:** regresses; **Elegance:** regresses; **Structural soundness:** regresses.
  - **Recommendation:** Option A; it bounds retry cost and removes current-day mutation from historical pagination.

- **Issue ID:** `API-RM-C02`
  - **Severity:** `high`
  - **Evidence:** `backend/src/fiscal-notes/fiscal-note-cache.service.ts:92-111,442-445`
  - **Why it matters now:** export is blocked by unrelated global coverage and reports a false provider outage.
  - **Option A (Recommended):** export from DB when the exact interval is covered; otherwise fail with `409 ExportacaoFiscalCoberturaIncompleta` before CSV generation.
    - **Effort:** medium; **Risk:** low; **Blast radius:** cross-stack; **Maintenance:** low; **Performance:** improves; **Elegance:** improves; **Structural soundness:** improves.
  - **Option B:** allow an explicitly labeled partial CSV.
    - **Effort:** medium; **Risk:** high; **Blast radius:** cross-stack; **Maintenance:** high; **Performance:** improves; **Elegance:** regresses; **Structural soundness:** regresses.
  - **Option C (Do Nothing):** block all export until global completion.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-stack; **Maintenance:** medium; **Performance:** neutral; **Elegance:** regresses; **Structural soundness:** regresses.
  - **Recommendation:** Option A; it preserves CSV completeness without coupling unrelated periods.

- **Issue ID:** `OPS-RM-C03`
  - **Severity:** `medium`
  - **Evidence:** `backend/src/fiscal-notes/fiscal-note-cache.service.ts:61-65,115-127,184-216`
  - **Why it matters now:** synchronization runs in an interactive request and rolling does not start until bootstrap completes.
  - **Option A (Recommended):** existing Nest scheduler/startup trigger owns background sync; requests only nudge and read local state.
    - **Effort:** medium; **Risk:** medium; **Blast radius:** module; **Maintenance:** low; **Performance:** improves; **Elegance:** improves; **Structural soundness:** improves.
  - **Option B:** introduce a dedicated queue/worker.
    - **Effort:** high; **Risk:** medium; **Blast radius:** cross-stack/runtime; **Maintenance:** high; **Performance:** improves; **Elegance:** neutral; **Structural soundness:** improves only if scale requires it.
  - **Option C (Do Nothing):** keep request-owned sync.
    - **Effort:** low; **Risk:** high; **Blast radius:** cross-stack; **Maintenance:** medium; **Performance:** regresses; **Elegance:** regresses; **Structural soundness:** regresses.
  - **Recommendation:** Option A for the verified single-replica topology; queue/worker remains a separately approved scale decision.

- **Issue ID:** `DATA-RM-C04`
  - **Severity:** `medium`
  - **Evidence:** stage shows partial data while the local environment cannot inspect its sync row; cache rows are derived but operationally valuable.
  - **Why it matters now:** blind completion can hide gaps and full deletion wastes already imported pages/provider quota.
  - **Option A (Recommended):** preserve cache, retire legacy sync metadata and reverify only incomplete stable windows.
    - **Effort:** medium; **Risk:** low; **Blast radius:** database/module; **Maintenance:** medium; **Performance:** improves versus full reload; **Elegance:** improves; **Structural soundness:** improves.
  - **Option B:** mark complete when local count appears plausible.
    - **Effort:** low; **Risk:** high; **Blast radius:** database; **Maintenance:** high; **Performance:** improves; **Elegance:** regresses; **Structural soundness:** regresses.
  - **Option C (Do Nothing/full reset):** delete and rebuild all cache rows.
    - **Effort:** low; **Risk:** high; **Blast radius:** database/provider; **Maintenance:** medium; **Performance:** regresses; **Elegance:** regresses; **Structural soundness:** neutral.
  - **Recommendation:** Option A; coverage must be proven without discarding useful projection data.

### Failure Modes & Edge Cases

- [ ] Provider total changes inside a closed month: invalidate/restart only that month with bounded attempts/backoff.
- [ ] Application restarts with `running` row: detect stale ownership and resume/restart deterministically without concurrent duplicate traversal.
- [ ] Month/year/leap-day and timezone boundaries: generate non-overlapping ISO date windows in `America/Sao_Paulo`.
- [ ] Requested interval spans complete and incomplete windows: list is explicitly partial; export is rejected.
- [ ] Requested covered interval has zero matches after status/idCompra filters: valid empty response/export `204`, not unknown coverage.
- [ ] Sync and rolling upsert the same note: idempotent context-scoped identity preserves one row and latest observed data.
- [ ] Provider 429/5xx during background work: persist sanitized reason/cooldown, keep serving stored rows and avoid request-triggered retry storms.
- [ ] Stage legacy row is malformed/incompatible: fail closed for coverage, preserve rows, expose repair telemetry and require bounded revalidation.
- [ ] Document filter is applied: retain provider-backed path and do not claim DB-only list/export.

### Residual Unknowns / Risks

- [ ] Exact stage `erroCodigo`, checkpoint and row counts remain unknown until DevOps collects redacted aggregate evidence from the revision-attested target.
- [ ] Smart Notas may backfill/change closed historical months; without a changed-since contract, periodic deep reconciliation remains outside this correction.
- [ ] Multi-replica scheduling remains unsupported; topology change requires distributed coordination before rollout.
- [ ] Exact browser runner and stage test identity must be resolved from project-owned runtime surfaces before flow evidence.

## Additional Architectural Opinions

- **Needed:** `no beyond the mandatory independent critique`
- **Why ambiguity remains:** the recommended direction dominates the alternatives; a fresh no-context reviewer is still mandatory because this is a `big` architecture correction with public contract impact.
- **Opinion count:** `0`
- **Package mode:** `bounded-file-set`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md`
- **Latest TEACH evidence / artifact:** `pending review baseline freeze`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | state machine, API, UI, persistence and stage repair |
| `blast_radius` | `cross-stack` | NestJS + React + PostgreSQL/Prisma |
| `behavioral_change_or_bugfix` | `yes` | stage regression correction |
| `changes_public_contract` | `yes` | coverage metadata and `409 ExportacaoFiscalCoberturaIncompleta` |
| `touches_auth_or_tenant` | `no` | existing auth/roles/context isolation preserved |
| `touches_runtime_or_infra` | `yes` | in-process scheduler/startup behavior; no infrastructure files |
| `touches_tests` | `yes` | fail-first and full regression coverage required |
| `critical_user_journey` | `yes` | fiscal list/pagination/export |
| `release_or_promotion_critical` | `yes` | current stage behavior is degraded |
| `high_severity_plan_review_issue` | `yes` | `ARCH-RM-C01` and `API-RM-C02` |
| `explicit_three_lane_request` | `no` | no explicit user request |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `blocked only on review baseline freeze; no review has been claimed`
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-summary`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** big architecture correction needs a committed/pushed immutable TODO packet before independent review.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `uninotas-foundation:main`
- **Baseline commit:** `fe1157216fa43f016685014d117068663e47deb5`
- **Baseline push reference:** `origin/main@fe1157216fa43f016685014d117068663e47deb5`
- **Gate status:** `no_material_findings`
- **Findings summary:** corrective contract frozen as a single-file TODO commit; no product/module/runtime file was included.
- **Evidence / reference:** `https://github.com/unifast-tech/uninotas-foundation/commit/fe1157216fa43f016685014d117068663e47deb5`
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** any post-review change to windows, coverage, errors, repair or evidence can alter the approved risk conversation.
- **Trigger stage:** `after planning review/critique convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md`
- **Gate status:** `not_run`
- **Findings summary:** pending frozen baseline and review convergence.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** `big`, cross-stack, public contract/runtime-sensitive behavior, intentional module supersede and high-severity findings.
- **Impact signals in scope:** `cross-stack blast radius|public API|runtime scheduler|intentional module supersede|high-severity issue cards`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** this TODO, fiscal module, cache service/spec, fiscal service/types/errors and React list/API normalization files.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after baseline freeze; reviewer cannot be implementing agent`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** pending baseline freeze.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** the correction depends on exact checkpoint, error-map and schema capabilities observed in code.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-RM-C01..A-RM-C06`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md`
- **Gate status:** `not_run`
- **Findings summary:** pending baseline freeze and critique.
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas API | feeds historical/rolling windows | `rate-limited/degraded` | `2026-09-29` | user-observed stage `429/503` and code diagnosis | bounded background pacing, cooldown and no provider calls on covered reads |
| Railway Stage revision | required for exact smoke and sync-row diagnosis | `stale/unknown for corrective revision` | `2026-09-29` | existing dependency register predates this correction | DevOps must attest exact `branch@sha` before evidence |
| Stage PostgreSQL read model | determines legacy repair path | `unknown` | `2026-09-29` | local `.env` DB had zero sync/cache rows | collect only redacted aggregates after target attestation; no blind mutation |

## Rules Acknowledgement / Ingestion

- **Current status:** `planned declaration only`; all rows must be reloaded and bound after renewed `APROVADO` before execution.

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
| `delphi-ai/skills/bug-fix-evidence-loop/SKILL.md` | stage regression and missing immutable-total test coverage | evidence-first diagnosis and fail-first closure | solution-first patching | ingest before implementation |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | tests must define moving-total/coverage behavior | effective assertions across unit/integration/browser layers | implementation-shaped or weak tests | required during test-first execution |
| `delphi-ai/skills/test-orchestration-suite/SKILL.md` | full stack-aware verification is delivery-critical | targeted diagnostics plus full CI-equivalent suites | treating focused pass as delivery proof | required before delivery |
| `delphi-ai/skills/frontend-race-condition-validation/SKILL.md` | background refresh/export UI lifecycle remains async | stale-result/abort/download ownership | late warning/download effects | required if React async path changes |
| `delphi-ai/skills/rule-docker-shared-foundation-docs-sync-model-decision/SKILL.md` | canonical module conflicts with the local-export implementation | module/TODO/API vocabulary in lockstep | closing with TODO-only truth | required for module consolidation |

## Historical Implementation Evidence — Delivered Baseline

- `backend/prisma/schema.prisma` and migration `20260929120000_fiscal_note_read_model` were reused without a new schema change; their compound identity and workload indexes already support the approved evolution.
- `backend/src/fiscal-notes/fiscal-note-cache.service.ts`: one resumable 365-day bootstrap per context, durable page checkpoint, shared fiscal-rate lease/pacing, 60-second persisted provider cooldown, 15-minute rolling reconciliation of today/yesterday, idempotent upserts and bounded local list/export reads.
- `backend/src/fiscal-notes/fiscal-notes.service.ts`: list/export use PostgreSQL when no document filter is present; detail, PDF, XML and document-filtered operations remain provider-backed.
- `backend/src/fiscal-notes/fiscal-notes.controller.ts`: CSV responses disclose local source, stale state and cache age through headers.
- `frontend/src/api/notas.ts`, `frontend/src/notas/normalizacaoFiscal.ts` and `frontend/src/paginas/ListaNotas.tsx`: metadata contract validation plus explicit partial/stale notices.
- `backend/src/fiscal-notes/fiscal-note-cache.service.spec.ts`: seven scenarios cover concurrent deduplication, one-time history, context isolation, 20,000-row local export, checkpoint resume after `429`, rolling reconciliation, cooldown fallback and empty-cache failure.
- No `logs`, credentials, provider adapter, deployment or CI files changed.

## Historical Validation Evidence — Delivered Baseline

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

## Historical Closeout Status — Superseded by Corrective Evolution

- Local implementation and CI-equivalent validation are complete.
- The first stage request may still traverse the 365-day bootstrap and can receive `429`; successful pages remain durable and the next attempt resumes after the cooldown instead of restarting at page 1.
- After `bootstrap_complete`, list/export are PostgreSQL-backed and only today/yesterday are reconciled every 15 minutes.
- Deployment remains outside this TODO; stage smoke and live provider quota evidence remain post-deploy checks.

## Historical Completion Evidence Matrix — Delivered Baseline

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

## Historical Local CI-Equivalent Suite Matrix — Delivered Baseline

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes | Gate Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| backend behavior | cache reuse and existing fiscal contracts | `cd backend && npx jest --runInBand` | implementation | `passed` | executed: 16 passed suites, 364 passed tests, 2 contract-defined skips | `passed` | full local fiscal regression |
| backend static/build | Prisma schema, Nest wiring and TypeScript output | `cd backend && npx prisma validate && npx eslint "src/**/*.ts" && npm run build` | implementation | `passed` | executed with exit 0 | `passed` | non-mutating static validation |
| frontend consumer | metadata parser, stale notices and production bundle | `cd frontend && npm run test:notas && npm run lint && npm run build` | implementation | `passed` | executed: parser checks, lint and Vite production build | `passed` | deterministic consumer contract evidence |
| database | migration state and local query plan | local PostgreSQL / Prisma | Local-Implemented | `passed` | executed: schema up to date and indexed export plan | `passed` | local PostgreSQL at `localhost:55432` |
| runtime | repeated export after completed sync | deterministic synthetic harness | Local-Implemented | `passed` | executed: 20,000 rows, zero provider calls, 55 ms | `passed` | bounded service-level workload |

## Historical Pipeline/Copilot P1/P2 Preflight — Delivered Baseline

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes | Gate Status |
| --- | --- | --- | --- | --- | --- | --- |
| local implementation checkpoint | correctness, concurrency, privacy, performance and likely CI failures | `passed` | full diff review plus CI-equivalent commands | none | single-replica coordination constraint is accepted by design | `passed` |

## Historical Rule-Spirit Anti-Pattern Hunt — Delivered Baseline

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes | Gate Status |
| --- | --- | --- | --- | --- | --- | --- |
| source authority | `logs` used as fiscal cache/source | `passed` | cache service imports Smart Notas port and Prisma-owned tables only | none | `logs` remains external/read-only | `passed` |
| freshness | silent stale fallback | `passed` | cache service and frontend metadata tests | none | stale coverage is disclosed and revalidated | `passed` |
| context isolation | cross-context identity collision | `passed` | Prisma compound unique key plus foreign-context unit fixture | none | no aggregation | `passed` |
| provider traversal | unbounded traversal | `passed` | sync limits 20,000 rows/200 pages and is sequential | none | bounded implementation | `passed` |
| database/runtime evidence | indexed query and bounded export | `passed` | local PostgreSQL `EXPLAIN`; deterministic 20,000-row export | no local HTTP p95/p99 | stage HTTP metrics are post-deploy evidence, not local implementation scope | `passed` |
| heuristic scan | hard-coded target and source bypass heuristics | `passed` | `rule_spirit_anti_pattern_scan.sh` over backend fiscal and frontend source | 20 review-only matches | `.test` emails and `127.0.0.1` are synthetic test fixtures; `dia.test` is a regular expression; zero warning/blocker | `passed` |

## Historical Promotion Finding Routing Ledger — Delivered Baseline

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `RM-REVIEW-01` | low | `by-design/no-action` | Keep in-process synchronization deduplication for current single-replica topology. | Approved scope did not change Railway topology; database upserts/checkpoints remain retry-idempotent. | closed | Add a distributed lease before horizontal scaling. |
| `RM-HEURISTIC-01` | info | `by-design/no-action` | Retain synthetic `.test` emails, ephemeral loopback servers and date regex. | Scanner matches test fixtures and regex syntax, not runtime domain configuration or personal data. | closed | Rule-Spirit scan manual classification, 2026-09-29. |

## Historical Next Exact Step — Superseded

Versionar a implementação na branch `release/uninotas`; depois do deploy de stage, observar o primeiro bootstrap e confirmar que listagem/exportação passam a operar localmente, sem nova travessia histórica.

## Historical Blockers — Superseded

- No blocker for local delivery.
- `PENDING_PROVIDER_SMOKE`: the first real stage bootstrap/export must prove provider quota behavior without exposing PII in logs.
- `PENDING_STAGE_LOAD`: record HTTP p95/p99 and error rate on stage after the projection is complete.
- Horizontal scaling is not part of the current Railway topology contract; synchronization deduplication is in-process and durable idempotency is database-backed. Introduce a distributed lease before running multiple API replicas.

## Historical Framing Notes

- `PENDING_APPROVAL`: o usuário ainda não aprovou o escopo, a autoridade do read model, a política de frescor e o caminho de sincronização.
- `PENDING_TOPOLOGY`: owner de migration, capacidade do PostgreSQL e estratégia de execução do sync ainda não estão confirmados.

## Questions To Close

- [x] Nenhuma decisão material permanece aberta antes do review; detalhes de implementação condicionais estão cobertos por assumptions e pelo scope-change rule.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-RM-C01` | `Definition of Done` | monthly closed history through D-2, local restart, stored rows preserved | test+database | fail-first cache spec + real PostgreSQL window assertions | local | `planned` | exact artifacts pending implementation |
| `DOD-RM-C02` | `Definition of Done` | rolling D-1..D independent every 15 minutes | unit+scheduler | cache spec and scheduler wiring assertion | local | `planned` | must run while history incomplete |
| `DOD-RM-C03` | `Definition of Done` | list never waits provider and handles complete/partial/empty | integration+browser | Nest application spec + source-owned browser flow | local/browser | `planned` | provider mock must remain uncalled for local path |
| `DOD-RM-C04` | `Definition of Done` | covered DB export; incomplete exact 409 and no CSV | integration+browser | export application spec + browser download assertion | local/browser | `planned` | exact public code required |
| `DOD-RM-C05` | `Definition of Done` | non-destructive legacy repair | migration+database | baseline-schema repair fixture and redacted stage evidence | local/stage | `planned` | no count-only completion |
| `DOD-RM-C06` | `Definition of Done` | truthful API/UI synchronization errors | contract+browser | exception filter/service/frontend specs | local/browser | `planned` | provider code only after real provider call |
| `DOD-RM-C07` | `Definition of Done` | provider detail/docs/document filter and context isolation preserved | regression | full fiscal suites | local | `planned` | no PII projection expansion |
| `DOD-RM-C08` | `Definition of Done` | module/tests/build/DB/PCV/stage evidence coherent | review+runtime | gates and artifacts below | local/stage | `planned` | row cannot pass from aggregate suite alone |
| `VAL-RM-C01` | `Validation Steps` | fail-first regression set | test | targeted Jest RED/GREEN evidence | local | `planned` | capture initial failures before code |
| `VAL-RM-C02` | `Validation Steps` | full suites/static/build/Prisma | CI-equivalent | commands in current Local CI matrix | local | `planned` | all in-scope rows pass |
| `VAL-RM-C03` | `Validation Steps` | real PostgreSQL coverage/repair/plans | database | disposable empty+baseline runs and EXPLAIN artifacts | local PostgreSQL | `planned` | no production payloads |
| `VAL-RM-C04` | `Validation Steps` | bootstrap/rolling/list/export concurrency | concurrency | BCI artifact | local | `planned` | overlapping windows and restarts |
| `VAL-RM-C05` | `Validation Steps` | bounded local performance and zero upstream covered export | performance | EPS/RLS JSON artifacts with SHA-256 | local | `planned` | representative 20,000-row fixture |
| `VAL-RM-C06` | `Validation Steps` | React warning/progress/download behavior | browser | exact checkout publication + browser spec | browser | `planned` | freshness attestation mandatory |
| `VAL-RM-C07` | `Validation Steps` | revision-attested stage repair and smoke | runtime | redacted aggregate query + authenticated API smoke | Railway Stage | `planned` | DevOps handoff; bounded provider traffic |
| `VAL-RM-C08` | `Validation Steps` | deterministic/review/consolidation gates | review | guard outputs, no-context audits and module diff | local/Foundation | `planned` | all blockers resolved before delivery |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| corrective implementation diff + frozen decisions + CI evidence | P1/P2 state-machine, API, schema, UI and evidence failures | `planned` | fresh internal no-context review after implementation | pending | unresolved P1/P2 blocks delivery |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| derived read model / P-6 | PostgreSQL treated as fiscal authority or manual completion | `planned` | code/diff scan + tests | pending | no authority inversion |
| non-blocking local reads | hidden `await`/provider traversal in list/export | `planned` | call-count tests + heuristic scan | pending | zero upstream on covered path |
| interval coverage | global boolean or count-only proof | `planned` | query/state tests | pending | exact interval required |
| truthful errors | local coverage mapped to provider outage | `planned` | exact error tests | pending | public semantics must match cause |
| test quality | immutable-total-only fixtures or weakened assertions | `planned` | independent test-quality audit | pending | moving-total/restart cases required |

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** persistence/query and API error/metadata paths change around fiscal data, while auth, permissions and stored PII are intentionally unchanged.
- **Attack surface in scope:** authenticated list/export endpoints, query bounds, CSV generation, sync metadata/log redaction, context isolation and database repair.
- **Attack simulation decision:** `required`
- **Review evidence:** pending `security-adversarial-review` or equivalent bounded review before delivery.
- **Residual security risk:** stage diagnostics could leak PII if unredacted; evidence is restricted to counts, dates, states, page progress and sanitized codes.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** list/export query paths, scheduler concurrency, batch upserts and provider quota behavior all change.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `high` | `EPS-QUERY-SHAPE-CHANGED` | `before_local_implemented` | `EPS-E2` | `pending` | indexed interval coverage/export plan not yet proven | `U-QUERY-PATH-UNKNOWN` |
| `FRC` | `frontend-race-condition-validation` | `required` | `medium` | `FRC-STALE-RESPONSE` | `before_local_implemented` | `FRC-E2` | `pending` | background metadata may overwrite newer query state | `U-ASYNC-SURFACE-UNKNOWN` |
| `BCI` | `backend-concurrency-idempotency-validation` | `required` | `high` | `BCI-JOB-WEBHOOK-API-OVERLAP` | `before_local_implemented` | `BCI-E3` | `pending` | bootstrap/rolling/restart overlap not yet proven | `U-WRITE-OVERLAP-UNKNOWN` |
| `RLS` | `runtime-load-stress-validation` | `required` | `high` | `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED` | `before_production_ready` | `RLS-E2` | `pending` | real stage quota/latency remains unknown | `U-RUNTIME-PRESSURE-UNKNOWN` |

### EPS
- **Trigger rationale:** list/export query and coverage shape changes materially.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** pending implementation and exact workload artifact.

### FRC
- **Trigger rationale:** asynchronous list refresh/export error/download state is user-visible.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** pending implementation and browser/unit artifact.

### BCI
- **Trigger rationale:** scheduled bootstrap and rolling writes may overlap and must remain idempotent.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** pending implementation and concurrency artifact.

### RLS
- **Trigger rationale:** bulk sync/cache/index path plus stage provider pacing is runtime sensitive.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** pending representative local load and bounded stage smoke artifacts.

## Verification Debt Assessment

- **Audit outcome:** `pending`
- **Why this outcome:** TODO is `big`, existing tests missed the deployed failure and canonical module drift exists.
- **Inline code TODO debt:** `unknown until implementation diff audit`
- **Evidence / audit artifact:** pending `verification-debt-audit` before closeout.
- **Accepted residual debt:** none accepted before review.

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** bugfix/architecture/public-contract change with new test logic and a known prior coverage gap.
- **Trigger signals in scope:** `changed test logic|bugfix/regression|behavior-defining change|architectural change|shared API/schema|critical user journey`
- **Required evidence matrix:** `unit|integration PostgreSQL|browser web|stage smoke`
- **Package mode:** `bounded-file-set`
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after implementation; reviewer cannot be implementing agent`
- **Audit focus:** `product/test delta alignment|fail-first alignment|bypass detection|assertion efficacy/efficiency|moving-total/restart/coverage sufficiency`
- **Audit status:** `not_run`
- **Findings summary:** pending implementation.
- **Evidence / reference:** pending.
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** big cross-stack correction intentionally supersedes module decisions and changes a critical list/export contract.
- **Impact signals in scope:** `cross-stack|public API|runtime scheduler|intentional module supersede|high-severity issues`
- **Package mode:** `bounded-summary`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after test-quality audit; reviewer cannot be implementing agent`
- **Review focus:** `adherence|regressions|validation/test evidence|security/performance|elegance|structural soundness|verification debt`
- **Final review status:** `not_run`
- **Findings summary:** pending implementation.
- **Evidence / reference:** pending.
- **Waiver authority / reference:** `n/a`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `required`
- **Why this decision:** provider-per-request export and legacy global bootstrap are being retired while a temporary partial-list bridge remains.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement|temporary fallback bridge`
- **Package mode:** `bounded-summary`
- **Audit focus:** `true DB-covered canonical path|partial-list exception|legacy sync retirement|no hidden provider traversal`
- **Cutover audit status:** `not_run`
- **Findings summary:** pending implementation.
- **Evidence / reference:** pending.
- **Waiver authority / reference:** `n/a`

## Module Consolidation Gate

- [ ] Canonical fiscal module records interval coverage, windowed sync, local list/export and truthful errors.
- [ ] `FISC-EX-02/FISC-EX-04` are intentionally superseded with traceability to `D-RM-C*`.
- [ ] Provider-backed detail/documents and legacy module transition remain preserved.
- [ ] TODO/module cross-links and final decision/adherence evidence are recorded.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** corrective contract is prepared but not frozen/reviewed/approved or implemented.
- **Post-commit/push status:** `complete`
- **Next path/status action:** run audit escalation, fresh no-context critique, assumption-code coherence, scope-drift and pre-approval authority guards from baseline `fe1157216fa43f016685014d117068663e47deb5`.
