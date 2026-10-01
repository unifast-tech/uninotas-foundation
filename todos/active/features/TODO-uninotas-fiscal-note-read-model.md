# TODO — Estabelecer e estabilizar o read model local de notas fiscais

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Active / Local-Implemented / Independent-Gates-Pending`
- **Created:** `2026-09-29`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário
- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-read-model.md`
- **Story:** `ST-FISCAL-READ-MODEL`

## Lane and authority

- **Lane:** `Tactical TODO`
- **Complexity:** `big`
- **Primary profile:** `Operational / Coder`
- **Technical scope:** `nestjs, react, vite, postgresql, prisma`
- **Current work state:** `implementation-authorized`
- **Implementation authority:** `granted by renewed user direction on 2026-09-30 for D-RM-C01..C27`.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** obter validação do usuário para a Opção A de `D-RM-I03/R3` (booleano público aditivo `autoRetry`), incorporar a decisão e os testes no TODO, congelar/revisar a nova baseline e só então pedir `APROVADO` renovado para código; o parser continua inalterado até a causa ser observada.

## Active Work State

- **Work state:** `review`
- **Why this state now:** a baseline `D-RM-C01..C27` foi implementada localmente, mas a consulta operacional fornecida pelo usuário em `2026-10-01` revelou falhas de admissão local e de contrato do provedor não cobertas pela evidência anterior. O delta corretivo abaixo é somente planejamento; a aprovação anterior não autoriza alterar a estratégia de recuperação.
- **Exit condition:** congelar e revisar a baseline `D-RM-I01..I03`, obter `APROVADO` renovado para a correção de admissão/diagnóstico e então executar os testes e código dentro desse limite. A causa exata da rejeição de contrato é resultado esperado da instrumentação implantada, não pré-condição impossível para aprová-la.

## Provisional Notes

- **Missing for production-ready:** concluir os gates independentes requeridos pelo audit floor e, após promoção autorizada, atestar a revisão implantada, reparar sem destruição e validar o stage com perfil RLS.
- **Revisit criteria:** todos os critérios `DOD-RM-C*` e `VAL-RM-C*` aprovados e evidenciados, incluindo smoke de stage com revisão exata em execução.
- **Dependencies unblocked:** o TODO de cancelamento pode continuar em planejamento, mas sua implementação não deve preceder a estabilização deste read model.
- **New incident qualifier:** o usuário confirmou que `main@fb8d88137212bbe549707aa064cc03185a14e6db` era o deploy ativo no horário das cinco falhas fornecidas. Logs sanitizados de ambos os contextos confirmam respostas HTTP 200 com erro de contrato, mas não a validação exata; o ambiente/banco consultado ainda não foi nomeado explicitamente e resultados anteriores de testes/revisões não fecham este delta.

## Implementation Intent

- **Current delivery:** estabilizar o read model implantado para que listagem/paginação sejam sempre locais e não bloqueantes, exportações locais dependam somente da cobertura do intervalo solicitado e a sincronização histórica converja em janelas fechadas.
- **Planned next steps:** após esta correção, retomar o TODO independente de cancelamento fiscal; isso não está autorizado aqui.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** mantém Smart Notas como autoridade e reutiliza PostgreSQL/Nest scheduler existentes; `D-RM-C21` adiciona somente hints de prioridade limitados e reconstruíveis, enquanto `D-RM-C23..C27` completam a mesma projeção normalizada que já alimenta lista/exportação, sem payload bruto, chamadas de detalhe por linha, fila externa ou nova réplica.

## Execution Lane Tracking

- **Local implementation branches:** `MonitorNotes:release/uninotas`, `uninotas-foundation:main`
- **Promotion lane path:** `release/uninotas -> PR definido pelo usuário`; Foundation permanece na autoridade canônica `main` e sua publicação segue governança própria.
- **Lane-promoted threshold for this TODO:** PR da branch `release/uninotas` aprovado/mesclado no alvo informado pelo usuário.
- **Production-ready threshold for this TODO:** revisão exata implantada em Railway Stage, reparação concluída e smoke autenticado/list-export aprovado.

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| corrective read model | `release/uninotas@6f48e60c5c0690a02f9ca0dbed8a6d31e2761475` | `user-owned PR/merge to main pending` | `n/a; project uses main as the current production source` | `pending user-owned PR/merge` | `committed and pushed after explicit authorization; no merge or deploy performed by Delphi` |
| canonical Foundation contract | `main@working-tree` | `n/a` | `n/a` | `n/a` | `synchronized locally; validation pending` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** schema/state concretization needed for approved interval coverage; exact normalized fields already returned by `GET /notas`; tests/fixtures; non-destructive legacy-row repair; and bounded observability that serve the same list/export projection.
- **Must update or split the TODO:** detail-only data, raw payload, partial export, deep historical reconciliation policy, durable/external queue, new worker/replica, provider quota/credential changes, cancellation or any Smart Notas mutation.

## Approval

- **Approved by:** `usuário — APROVADO em 2026-09-29`
- **Approval scope:** `corrective implementation defined in D-RM-C01..D-RM-C27: existing Prisma/PostgreSQL read model, demand-aware NestJS synchronization, yesterday/today React default, automatic partial-period revalidation, complete-only export, complete normalized GET /notas CSV projection, source-owned tests and canonical module synchronization on release/uninotas`
- **Execution not authorized by approval:** deploy/merge/promoção, credenciais/quota, mudança Railway/topologia, escrita em logs, cancelamento fiscal ou operações destrutivas no banco de stage.
- **Renewed approval required when:** mudar janela histórica, semântica de cobertura/exportação, contrato público, estratégia de recuperação, schema, topologia, limites, riscos ou evidências obrigatórias.

## Historical Approval Evidence — Delivered Baseline Only

- **Original approval:** `APROVADO o escopo e as premissas recomendadas do TODO.` (`2026-09-29`).
- **Original scope:** persistência derivada, sincronização resumível, leitura local condicionada, testes e documentação; sem deploy, credenciais ou escrita em `logs`.
- **Prior renewed approval:** `APROVADO o fluxo de carga histórica única e reconciliação diária do TODO.` (`2026-09-29`).
- **Prior renewed scope:** bootstrap de 365 dias, reconciliação de hoje/ontem, fallback local, metadados de frescor e detalhe/PDF/XML no provedor.
- **Authority boundary:** estas evidências explicam a baseline instalada em stage, mas foram explicitamente encerradas para a nova evolução porque o comportamento observado invalida premissas materiais de convergência e exportação.
- **Superseded approval attempt:** o usuário respondeu `APROVADO` em `2026-09-29`, porém as critiques obrigatórias posteriores encontraram mudanças materiais ainda não apresentadas (`FRM-CRIT-01..05`, `FRM-R2-01..05`, `FRM-R3-01..03`). Nenhuma implementação foi iniciada sob essa aprovação; ela foi substituída pela aprovação convergida registrada abaixo.
- **Renewed converged approval:** `APROVADO` recebido em `2026-09-29` após apresentação explícita de atomic publication, daily coverage, retained horizon, snapshot reads, bounded scheduler, truthful freshness and test expansion. Esta é a autoridade vigente para `D-RM-C01..C20`.
- **Renewed demand-aware approval:** `Vamos fazer assim então toda vez o user abrir o UniNotas ele vê o dia de ontem e hoje por padrão no filtro e dps ele escolhe a janela que precisa e faz o carregamento conforme você falou deixando liberado para exportação, parte essencial do projeto` recebido em `2026-09-30`, após confirmação explícita de que usuários concorrentes mantêm filtros independentes. Esta é a autoridade vigente para `D-RM-C21..C22`; não autoriza migration, nova réplica, worker externo, merge ou deploy.
- **Renewed complete-export approval:** após confirmar que o `GET /notas` devolve `nome` e `documento`, o usuário aprovou `Vamos fazer isso então` em `2026-09-30` para persistir e exportar todos os campos conhecidos dessa listagem. Esta é a autoridade vigente para `D-RM-C23..C27`; autoriza migration aditiva local, não autoriza deploy, merge, credenciais ou dados de detalhe/raw payload.

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

## Approved change - provider failure fallback

The current provider-first contract is insufficient when Smart Notas returns a temporary `429`. The approved change keeps Smart Notas as the fiscal authority and allows list/export to serve the last valid local projection while a controlled revalidation is pending.

This material change to freshness and failure semantics was approved by the user on `2026-09-29`.

| ID | Proposed decision | Boundary |
| --- | --- | --- |
| `D-RM-E01` | Stale fallback | List and export may return the last complete local coverage when the provider fails with a temporary limit/unavailability error; an empty cache must still return the provider error. |
| `D-RM-E02` | Background revalidation | Provider synchronization must not block the interactive list/export request after a valid local coverage exists; only one sync may run per context/date window. |
| `D-RM-E03` | Freshness disclosure | Responses using stale local data must expose source and cache age through an explicit contract/header; the UI must not present stale data as current. |
| `D-RM-E04` | Retry/cooldown | A provider `429` must trigger bounded backoff and a persisted cooldown, preventing immediate repeated full traversals after a failed sync. |
| `D-RM-E05` | Detail ownership | Detail, PDF and XML remain provider-backed and do not silently fall back to the summary projection. |

## Approved change - bootstrap plus rolling reconciliation

The proposed synchronization policy is narrowed to avoid traversing the entire historical period on every request:

- **Bootstrap:** perform one complete historical load per fiscal context, with resumable pages and an explicit `bootstrap_complete` state. Historical list/export reads are allowed only after this state is complete.
- **Rolling reconciliation:** after bootstrap, query Smart Notas only for the current date and the previous date, using the application timezone (`America/Sao_Paulo`), and upsert returned records to capture new notes and status changes.
- **Local consumers:** list and export read the complete locally stored projection, applying the requested filters in PostgreSQL. They do not re-traverse historical provider pages after bootstrap.
- **Provider-backed consumers:** detail, PDF and XML continue to call Smart Notas directly and do not use the summary projection as a silent fallback.

This proposal replaces the current per-request/per-period full coverage strategy and was approved for implementation on `2026-09-29`.

## Corrective Change — Approved and Locally Implemented

### Observed Symptoms and Evidence

- Stage keeps returning `readModel.coverage=partial`, which makes the React list continuously show `Carga histórica em andamento. Exibindo as notas já armazenadas.`
- CSV export returns the public `SmartNotasIndisponivel` message even when PostgreSQL already contains notes for the requested period.
- `FiscalNoteCacheService.list()` awaits `ensureBootstrap()` before the local query; `exportAll()` rejects every state other than `bootstrap_complete` before reading cached rows.
- The 365-day bootstrap includes the current day, freezes `total`, `totalPages` and `perPage`, and rejects any later page whose totals changed. New notes arriving during a long traversal can therefore make the checkpoint permanently incompatible with the provider's next response.
- The persisted-error mapper preserves only `SmartNotasLimiteExterno`; pagination inconsistency, timeout and unexpected failures are collapsed into `SmartNotasIndisponivel`, hiding the actual reason.
- The existing seven cache-service tests pass but keep provider totals immutable. They do not cover a changed total after checkpoint resume, a stale `bootstrap_running` record after process restart, interval-complete export during global partial coverage, or truthful error mapping.
- The local `DATABASE_URL` inspected on `2026-09-29` contained zero read-model sync/cache rows, so the exact stage `erroCodigo` remains runtime evidence to collect. This does not invalidate the code-level failure path above.

### Operational Incident Evidence — 2026-10-01 (Provisional; Approval Pending)

- **Source and limits:** user-provided, read-only result from `monitor_fiscal_note_syncs`, ordered by `atualizado_em DESC`; no note payload, token or PII was provided. The user supplied the Railway/GitHub-linked revision [`main@fb8d88137212bbe549707aa064cc03185a14e6db`](https://github.com/unifast-tech/MonitorNotes/commit/fb8d88137212bbe549707aa064cc03185a14e6db), titled `Merge pull request #15 from unifast-tech/release/uninotas feat: export complete fiscal note projection`, and explicitly confirmed that this deploy was active at `10:17:48–10:18:03` on `2026-10-01`. This is user attestation of the incident revision, not independent inspection of the private commit; the environment/database queried has not been named explicitly. The earlier `2026-09-29` local-empty observation above is historical and no longer means that the runtime error codes are unknown.

| contexto_fiscal | data_inicio | data_fim | estado | erro_codigo | itens_por_pagina | pagina_concluida | atualizado_em (as supplied; timezone unconfirmed) |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| prosperar | 2025-10-01 | 2025-10-31 | bootstrap_failed | ExportacaoFiscalOcupada | null | 0 | 2026-10-01 10:18:03 |
| prosperar | 2026-08-01 | 2026-08-31 | bootstrap_failed | ExportacaoFiscalOcupada | null | 0 | 2026-10-01 10:18:00 |
| unifast | 2025-11-01 | 2025-11-30 | bootstrap_failed | ExportacaoFiscalOcupada | 200 | 4 | 2026-10-01 10:17:57 |
| unifast | 2026-05-01 | 2026-05-31 | bootstrap_failed | ExportacaoFiscalOcupada | 200 | 3 | 2026-10-01 10:17:54 |
| unifast | 2026-03-01 | 2026-03-31 | bootstrap_failed | SmartNotasContratoInvalido | 200 | 1 | 2026-10-01 10:17:48 |

- **Confirmed by code:** `ExportacaoFiscalOcupada` originates in local `FiscalRateCoordinator.startExport()`/page admission; `walkPages()` currently persists it as `bootstrap_failed`. The historical walk reuses `read-model:bootstrap:<context>` as the actor, whose admitted cooldown lasts 60 seconds. Four nearby occupied rows are consistent with that cooldown, but the precise rejection branch (cooldown, lease, configured capacity) is not proven without redacted runtime configuration/telemetry. `itens_por_pagina=200` and checkpoints 3/4 prove that those Unifast generations staged pages before the later local refusal; null/zero Prosperar rows do not prove a provider request occurred.
- **Separate provider-boundary failure:** `SmartNotasContratoInvalido` is emitted by `SmartNotasAdapter` for an invalid status, bounded-body/JSON condition or rejected normalized field. The March checkpoint shows one page staged; the next attempted page would be page 2 for that generation, but the failing request and exact validation branch still need sanitized correlation evidence. No raw response or recipient values may be logged into this TODO.
- **Railway application-log evidence, user pasted on 2026-10-01:** 21 `SmartNotasAdapter` `operation=list` failures between `13:10:47` and `13:24:31` as displayed in the log excerpt: 11 Unifast, 10 Prosperar. All have `outcome=SmartNotasContratoInvalido`, `upstreamStatus=200` and durations of 67–239 ms. The Unifast event at `13:17:48` (`correlationId=c0837651-bc69-4c17-89b9-b58785c0803f`) matches the March sync-row second `10:17:48` after a three-hour UTC→São Paulo conversion; this is strong temporal/contextual correlation, not proof of the log display/database session timezones or of the page number, because neither is recorded with the event. These events rule out a non-200 provider status and adapter timeout for those attempts; they do not distinguish oversized/missing body, malformed JSON, envelope/page metadata or one rejected field. The adapter logs no response size, validation category, page or sync-window identifier, and `walkPages()` does not pass a sync trace to `list()`. Both contexts are affected, but whether they fail for one shared response shape or different records is unknown. No provider payload, token or PII was copied.
- **Invalidated hypothesis:** these five `erro_codigo` values do not support the prior Prisma-interactive-transaction timeout hypothesis; a generic Prisma exception would be persisted as `unexpected_error`. A 200-item page count reduces provider requests but does not remove local admission or contract failures.
- **User-visible gap:** `publicSyncError()` maps both codes to `unexpected`, and React renders the same generic failure plus a 60-second local persisted cooldown. This can present expected local backpressure as a failed provider synchronization.

**Bug-fix evidence gate (before any new implementation):**

| Required question | Current answer |
| --- | --- |
| End-to-end tests from provider/admission to UI? | No incident-specific chain: coordinator and adapter have mocked cases, but no test proves consecutive historical windows under the same 60-second actor cooldown through persisted sync state and UI. |
| Real DB/backend payload inspected? | Persisted sync metadata and 21 sanitized adapter logs: yes. User attests `main@fb8d88137212bbe549707aa064cc03185a14e6db` was active at the failure time. Exact environment/database name, provider response body and rejected validation branch: not supplied; the current logs do not encode the latter. |
| Which existing test failed? | None was rerun for this intake; prior green suites used deterministic mocks and did not exercise this runtime sequence or the real rejected page. They cannot be claimed as incident closure. |
| New fail-first tests needed? | Same-context consecutive windows/resume with admission refusal and eventual retry; page-2 contract rejection with sanitized diagnostic category; persisted-state → API → UI distinction between waiting and genuine failure. |
| Analyzer-enforced rule? | `no-rule-needed` for now: the observed timing and provider-data shape are runtime conditions, not a reliably recognizable static code pattern. Reassess only if the causal tests expose a recurring forbidden architecture shape. |

**Proposed correction boundary, not yet approved:** keep local admission pressure as scheduled/deferred work without falsely recording a provider failure or losing generation/checkpoint; preserve one in-process pump, fiscal-context separation, provider quota, bounded retries and complete-only export. Add bounded, PII-free internal diagnostics for the specific rejected status/body/field category, then decide whether the provider adapter needs a contract change from sanitized evidence. Do not increase response-size, timeout, quota or concurrency limits merely to clear the generic message; do not add a new worker, queue, replica, migration or raw-payload persistence. Any public read-model/UI change must be explicitly frozen and approved before implementation.

### Incident Execution Contract — Prepared for Renewed Approval

This is one bounded incident slice: stop classifying **local admission refusal** as a provider failure and make the independent HTTP-200 contract rejection diagnosable. It does not promise that every historical window will complete before the rejected provider shape is identified. The follow-up parser decision stays inside this TODO's incident conversation but requires fresh evidence and renewed approval if it changes accepted fiscal data.

| Decision | Proposed baseline for this slice | Module relationship and boundary |
| --- | --- | --- |
| `D-RM-I01` Local admission | Only **transient** `ExportacaoFiscalOcupada` (lease, cooldown or temporary capacity pressure) is deferred work, not a provider failure. Preserve candidates, generation, raw count, checkpoint and prior genuine error; **bootstrap and rolling admission both precede any state/error clearing or generation/candidate mutation**. Use explicit internal deferred state for new/local pending work and a conservative 60-second persisted eligibility window from the deferral transition only; the single pump skips it before eligibility and retries at the next scheduled/nudged opportunity thereafter. A configuration with no possible export slot (`maxConcurrency < 2` or export share zero) is a distinct fail-closed **operational stop**, surfaced in sanitized diagnostics/public metadata where applicable, with no futile retry loop until configuration/restart. | Preserves `FISC-RM-02/03/06`, one-replica coordination and complete-only export. No new worker, queue, replica or database migration is authorized. |
| `D-RM-I02` Contract diagnostics only | For `operation=list` and `SmartNotasContratoInvalido`, **enrich the existing per-request final event** (do not emit a second line) with a truthful allowlisted category (`body_missing`, `body_declared_invalid`, `body_declared_oversize`, `body_stream_oversize`, `json_invalid`, `envelope_invalid`, `page_metadata_invalid`, `record_invalid`), optional allowlisted field **name** and failure kind (`missing`, `type`, `empty`, `length`, `format`), observed byte count when known, context, date window, page, correlation ID, upstream status and duration. Every in-scope validation branch must map to exactly one category; other adapter operations keep their current logging contract. Never emit URL/query strings, provider body, record value, token, recipient data or raw exception. Keep the public error code and fail-closed parser unchanged. | Preserves the Smart Notas authority, positive DTO allowlist and `FISC-RM-07`; internal observability only. A future parser/limit change is explicitly excluded until real sanitized causal evidence is reviewed and newly approved. |
| `D-RM-I03` Consumer behavior | Reuse `coverage=partial`, `syncState=idle|syncing|failed`, `lastSyncError` and `retryAfterSeconds`. A transiently deferred unit (including legacy occupied rows projected compatibly) is `partial/idle/null` with a bounded retry countdown. For **partial** coverage, a genuine contract/configuration failure remains `failed` with its truthful existing public error. Make the smallest React timer change: `partial/failed` with `retryAfterSeconds=null` stops automatic revalidation; manual refresh remains available and backend static-capacity guard prevents futile provider attempts. Other pending/active intervals retain bounded automatic refresh. For **complete** but stale rolling coverage, preserve established `complete/idle` projection and existing stale-freshness/manual-refresh UI; expose operational fault only through existing `lastSyncError` metadata and sanitized logs, not a new failure banner. CSV stays disabled only when exact daily coverage is incomplete. | Preserves `FISC-RM-04/06`, React's closed enums, messages and API shape. One scoped frontend timer change is included; no new public enum/message is authorized. Backend/API/browser regression evidence is required. |

**Admission/state transition contract (no schema migration):** `bootstrap_deferred` and `rolling_deferred` are internal text states, not new public enums. A local refusal never counts as a provider attempt. Set `atualizadoEm` **once at the explicit deferred transition**; no seeding, retention, read or repeat nudge may update it while waiting. Derive the conservative 60-second `retryAfterSeconds` from that persisted timestamp; do not return null during the active wait. The backend gates scheduled and request-nudged pumps until eligibility even with several viewers. After restart, persisted state remains sufficient to honor the wait. A genuine prior failed row keeps its original `erroCodigo` and `atualizadoEm` when later admission is refused, so its error ordering is not changed by local pressure; any in-process cooldown remains bounded, and restart may attempt admission once before reapplying the gate. Only successful admission may clear that error. Public error selection is based on real failed state, never on a newer deferred row.

| Starting state | Transient local refusal | Next eligible pump / public projection |
| --- | --- | --- |
| `bootstrap_pending|bootstrap_running` with or without staged pages | Keep generation, candidates and counters; mark internal deferred, no provider error. | Resume the same checkpoint; `partial/idle/null` with countdown until admitted. |
| Legacy `bootstrap_failed` with `ExportacaoFiscalOcupada` | Read-time compatibility projects pending without mutating provider data; next normal pump safely changes only state/error marker, not generation, candidates or checkpoint. | Resume staged page after eligibility; no manual Stage SQL or destructive repair. If static capacity is impossible, show operational failure instead of pending. |
| `bootstrap_failed|rolling_failed` with a genuine prior provider/contract error | Keep failed state, original error, original update timestamp, generation and checkpoint; a later local refusal may update only a bounded in-process admission gate, never the persisted failure ordering. | For partial coverage, `failed` and original public error remain visible; retry only when eligible or after manual/scheduled recheck. |
| New rolling or existing `rolling_running|rolling_deferred` with staged pages | Admission precedes generation creation/rotation/deletion; after refusal keep or create a deferred row without discarding staged data. | Resume an in-progress generation/checkpoint; a fresh rolling refresh may rotate generation only **after** successful admission. |
| Existing `rolling_complete` awaiting refresh | Preserve published projection and existing candidate/generation metadata until admission. | Complete coverage remains readable; only an admitted refresh may start a new generation. |
| Impossible static export capacity | Do not convert to deferred; record a distinct sanitized operational configuration fault **once for unchanged process configuration** and stop repeated admission attempts. Do not clear any prior genuine provider error or published projection. | Partial coverage: existing `failed/unexpected` with `retryAfterSeconds=null`, no automatic React polling, manual refresh allowed. Complete/stale rolling: established `complete/idle`, stale-freshness/manual-refresh UI, existing error metadata and sanitized operational log. Re-evaluate after configuration correction/restart. |

**Deferred-state inventory that implementation must close:** update every state enumerator/guard, not just `walkPages`: `runPump` context selection; historical `ensureHistoricalWindow`, demanded-window selection and post-run completion; `processHistoricalWindow` eligibility/resume; both `seedHistoricalWindows` in-progress/covering checks; `ensureRollingInBackground`; `coverageForWith` active/error/deferred projection; moved-note publication conflict guard; and retention's candidate-preservation SQL. `bootstrap_deferred|rolling_deferred` must remain selected for the next eligible pump, must prevent reseeding/rotation and must retain staged candidates through restart and retained-horizon advancement. A read/nudge before eligibility must not write the row or call the provider. No periodic retry is promised for static incapacity; client and backend stop independently until configuration/restart or a manual recheck.

**R3 approval-material decision pending (2026-10-01):** the independent re-review of `ad9b4e4` confirmed the R2 fixes but exposed a contradiction in `D-RM-I03`: `partial/failed` with `retryAfterSeconds=null` also describes a **recoverable** provider failure older than 60 seconds. Stopping all such React timers would miss a background publication that completes just after the list response, so CSV might stay disabled until manual refresh. In addition, static incapacity has no authoritative persisted sync row for a new rolling window, and `coverageForWith()` currently ignores rows without `generationId`; the proposed failed/metadata projection is therefore not yet proven. Do **not** implement the current timer rule as frozen intent.

| Choice | Proposed treatment | Tradeoff |
| --- | --- | --- |
| `A` **recommended; needs user validation** | Add one backward-compatible public boolean such as `readModel.autoRetry` (default `true` for older responses), sourced from a typed read-only coordinator capability for impossible static export configuration. `coverageForWith()` projects this signal even with no sync row; true provider errors keep precedence in `lastSyncError`, and no generation/candidate is changed merely for presentation. React stops automatic polling only when `autoRetry=false`; recoverable errors keep bounded revalidation. For complete/stale rolling coverage, preserve `complete/idle`, stale-freshness UI and manual refresh while exposing the operational fault through existing metadata/logs. No database migration or new public enum/message. | Small additive API/normalizer/timer change, testable and preserves automatic recovery. |
| `B` | Keep the current no-new-field timer stop for every `partial/failed` with null retry deadline. | Less code, but breaks automatic observation of recoverable background completion; not recommended. |
| `C` | Keep existing automatic polling for all partial failures. | Preserves recovery, but static incapacity keeps many viewers reading/nudging every two seconds indefinitely; not recommended. |

Separately, `D-RM-I01` must treat each **new** eligible-but-refused admission as a fresh deferred transition with a new persisted 60-second clock; reads/nudges before that eligibility never reset it. This bounds a lease/capacity contention lasting beyond one minute. Test several viewers over multiple windows and after restart. This refinement and the chosen I03 option require a refreshed pushed baseline and review before `APROVADO`.

**Execution phases and stop line:** first add fail-first tests for local refusal/checkpoint survival and PII-free diagnostic categories; then implement `D-RM-I01/I02`, validate the unchanged public consumer contract, and only after a separately authorized Stage deployment observe one normal retry. If the resulting category identifies a provider-shape mismatch, return to the decision/review/approval loop before changing parser acceptance, body limit, timeout or page size. No manual bulk retry, direct Stage data repair or production write is authorized by this plan.

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
| `D-RM-C09` | Provider-owned detail/documents | Detail, PDF, XML and `documento`-filtered reads remain provider-backed; the public JSON summary remains unchanged. Its prior internal recipient-field exclusion is intentionally superseded by `D-RM-C23..C27` only for the local allowlisted Finance CSV projection. | Preserves `D-RM-03`, `D-RM-E05`, `FISC-DOC-*` and the provider-owned detail boundary. |
| `D-RM-C10` | Runtime boundary | Use the existing NestJS process and scheduler in the current single-replica topology. No durable/external queue, worker service, Railway topology, provider quota or credential change is authorized; only the bounded reconstructible in-process priority hints frozen in `D-RM-C21` are allowed. | Preserves the prior topology limitation and requires a separate TODO before horizontal scaling. |
| `D-RM-C11` | Atomic window publication | Provider pages are written to an isolated candidate generation. Canonical cache rows and interval coverage change together in one database transaction only after the complete traversal validates; failed or superseded generations are never visible to list/export. | Closes the partial-publication gap in `D-RM-C02/C05` and preserves the last valid projection. |
| `D-RM-C12` | Exact membership and absence | Every candidate must have a valid scheduled issue date inside the exact context/window. Null, malformed or out-of-window rows fail that generation. Successful publication deletes canonical rows proven absent from the same exact interval before upserting the candidate set. | Makes complete/empty/removed/moved semantics provable rather than count-derived. |
| `D-RM-C13` | Gap-free calendar frontier | Initial history is the inclusive 365-day interval `[D-366,D-2]`, split into month-clipped provider traversals in `America/Sao_Paulo`; rolling owns `[D-1,D]`. Each successful traversal publishes canonical daily proof, so a newly eligible `D-2` reuses its prior rolling proof or enters history as one missing day. | Makes month/year/leap-day rollover, retention and gap/overlap behavior deterministic. |
| `D-RM-C14` | Bounded scheduler and public state | One in-process pump runs at startup and every 15 minutes, never overlaps itself, prioritizes rolling for both contexts, then advances at most one historical window globally in round-robin order. The API exposes the frozen coverage/sync/progress/error fields below, including complete-zero versus partial-zero semantics. | Closes priority, fairness, concurrency and consumer ambiguity without changing the single-replica topology. |
| `D-RM-C15` | Daily canonical coverage proof | Add a context/date coverage ledger as the only authority for local completeness. Monthly historical and two-day rolling traversals publish one proof row for every calendar day in their exact interval, including days with zero notes; operational sync intervals may overlap, but canonical coverage never does. | Resolves rolling/frontier supersession and boundary clipping without deriving completeness from mutable sync rows or row counts. |
| `D-RM-C16` | Request snapshot and admissible horizon | Every pump/request captures `D` once in `America/Sao_Paulo`. Local list/export accept only intervals fully inside `[D-366,D]`; outside intervals fail with HTTP `422 PeriodoFiscalForaDoHorizonte`. Coverage, count and rows/CSV are read in one PostgreSQL `REPEATABLE READ` transaction. | Prevents mixed-generation responses, permanently partial requests and retention races while preserving provider-backed `documento` queries. |
| `D-RM-C17` | Bounded set-based publication | Final candidate promotion uses parameterized set-based SQL inside one bounded Prisma transaction, supported by generation/date indexes. Provider I/O never runs inside this transaction; timeout/lock failure preserves the previous published generation and enters normal persisted retry/backoff. | Keeps 20,000-row publication predictable and avoids thousands of row-by-row statements or long unbounded locks. |
| `D-RM-C18` | Durable distinct completeness | Publication requires the active generation's candidate `COUNT(*)` to equal both its durable raw-observed item count and the provider's frozen expected total, with page/per-page invariants satisfied. A duplicate provider ID across any pages or restart collapses in candidates but increments raw observations, causing rollback and `pagination_inconsistent`. | Prevents a resumed generation from publishing false complete coverage after duplicate IDs. |
| `D-RM-C19` | Interval-scoped freshness | Each daily proof stores `published_at`. The API adds `freshnessState=current|historical_snapshot|stale_rolling|unknown`; existing freshness fields are conservative aggregates over the exact interval, and historical snapshots never advertise an unsupported retry/deep refresh. | Intentionally refines `D-RM-07`: the 15-minute rule applies to requested rolling days, while older proof is disclosed as a historical snapshot rather than falsely revalidated. |
| `D-RM-C20` | Snapshot-visible retained horizon | Add one context-state row containing `horizon_date`, `retained_from` and `retained_through`. Retention updates this row and prunes rows/proofs in the same transaction; local list/export admit dates from the context-state row visible in their `REPEATABLE READ` snapshot, never from transaction/application wall-clock alone. | Aligns horizon bounds and retained rows in one MVCC state so midnight retention cannot invalidate an already admitted lower bound. |
| `D-RM-C21` | Demand-aware historical priority | An ordinary partial list registers only `{contextoFiscal,dataInicio,dataFim}` in a bounded in-memory, per-context queue. Exact equal demands coalesce; filters such as status and purchase do not create independent provider traversals. After rolling both contexts, each pump advances at most one demanded historical window, alternating contexts, while every fourth historical opportunity remains reserved for the oldest background unit. Requests never await provider I/O; restart safely loses only priority hints and later reads reconstruct them. | Makes the user-selected interval converge promptly without mixing users, duplicating identical work, changing the durable coverage authority or starving the retained 365-day bootstrap. |
| `D-RM-C22` | Default and automatic convergence UX | A new UniNotas list URL defaults to yesterday through today in `America/Sao_Paulo`. When the applied local interval is partial and has no `documento`, React revalidates the same query at a bounded cadence, cancels on filter/session/navigation lifecycle changes and automatically enables CSV when exact interval coverage becomes complete. | Removes the misleading manual-refresh loop while preserving independent per-user filters, local-only reads and the complete-only export invariant. |
| `D-RM-C23` | Complete list projection | Normalize and persist every documented/observed field returned by `GET /notas`: provider internal ID, model, purpose, status, environment, fiscal number, access key, purchase ID, product, unit/total value, scheduled/payment date, competence, recipient name/document/e-mail/city/state/country and platform. | The projection remains rebuildable and allowlisted; raw payload and detail-only fields remain forbidden. |
| `D-RM-C24` | Complete CSV schema | Export the complete normalized list projection in a fixed deterministic order, with Portuguese business-oriented headers and `contextoFiscal`; null remains empty and every value retains existing CSV formula protection. | Makes the filtered export useful to Finance without N detail requests or provider dependency after covered synchronization. |
| `D-RM-C25` | PII authorization boundary | Existing authenticated reader roles may export recipient name, document, e-mail and location because the product is restricted to the Finance team; responses remain private/no-store and observability must never log these values. | Intentionally supersedes the prior CSV PII exclusion while preserving authentication, context isolation and no-log rules. |
| `D-RM-C26` | Additive data rollout | Add nullable projection columns to cache and candidate tables plus a projection-version marker on daily coverage through one forward-only Prisma migration. Existing rows remain valid with nulls and old proofs remain version 1; subsequent synchronization backfills fields and publishes version 2 proof naturally, without a destructive or provider-per-row backfill. | Supports overlapping application versions and prevents old name-only coverage from authorizing a complete new CSV. |
| `D-RM-C27` | Detail boundary unchanged | `GET /notas/:noteId`, PDF and XML stay provider-backed; the export never calls detail per note. | Prevents monthly export amplification and keeps detail-only data out of the local projection. |

### Refined Publication, Calendar, Scheduler and Consumer Contract

#### Atomic candidate publication

- Add expand-only Prisma/PostgreSQL tables for candidates keyed by `{sync_id, generation_id, provider_id_interno}`, coverage days uniquely keyed by `{contexto_fiscal, coverage_date}` with durable `published_at` and projection version, and retained-horizon context state uniquely keyed by `contexto_fiscal`; the sync row records its active generation and durable raw-observed count. Candidates contain only the complete allowlisted `GET /notas` projection plus `observed_at`; no raw payload, detail-only field, PDF/XML or ephemeral URL is added.
- A window traversal writes and idempotently replaces rows only in its candidate generation. List/export continue reading the canonical cache and therefore cannot observe page-by-page or retry-partial data.
- After the final page, one database transaction locks and rechecks the current sync/generation, validates exact context/date membership and page invariants, deletes canonical rows for that exact context/date interval that are absent from the candidate set, upserts the candidate rows, upserts one completed coverage-day proof for every day in the interval, marks the operational sync complete, and removes its candidates.
- The generation durably increments `raw_items_observed` for every provider item before candidate-key deduplication. Publication requires `candidate COUNT(*) = raw_items_observed = total_esperado`, plus the frozen `paginas_esperadas`, `itens_por_pagina` and final-page cardinality invariants. Any mismatch, including a duplicate provider ID separated by checkpoint/restart, rolls back publication and records sanitized `pagination_inconsistent`.
- Absence deletion and candidate promotion use parameterized set-based `DELETE ... NOT EXISTS` and `INSERT ... SELECT ... ON CONFLICT DO UPDATE`, not a per-row Prisma upsert loop. The migration adds candidate indexes for active generation/date membership and retains the canonical context/date index. Provider calls and page staging occur before the publication transaction.
- Publication sets local PostgreSQL `lock_timeout <= 2s` and `statement_timeout <= 30s`, with the Prisma interactive transaction bounded to `<= 35s`. A timeout rolls back the entire publication, records a sanitized failure after rollback and follows persisted cooldown/backoff; it never expands the timeout dynamically.
- A failure, restart, provider-total change or stale generation leaves the prior canonical projection and coverage unchanged. Cleanup may delete only candidates owned by that failed/superseded generation.
- Legacy `bootstrap_*` metadata is retired without deleting canonical cache rows. Every new window is provider-verified before it can become complete; existing rows remain visible only under truthful partial coverage until publication proves the interval.

#### Calendar frontier and lifecycle

- `D` is captured once per pump in `America/Sao_Paulo`; interactive requests derive it inside their database snapshot as defined below. It is never recomputed mid-operation. Initial historical membership is exactly 365 inclusive calendar days, from `D-366` through `D-2`, split into immutable month-clipped provider traversals. Rolling is the exact two-day interval `[D-1,D]`.
- Operational sync rows describe provider traversals and may overlap across rolling/day/month boundaries. They never authorize reads. Successful publication writes/upserts the canonical daily coverage ledger for each exact day, so the proof set is non-overlapping by database uniqueness and requires no interval-precedence heuristic.
- When `D` advances, yesterday's successful rolling publication already provides the daily proof for the newly historical `D-2`. If that proof is missing, `D-2` enters the historical queue as an immutable one-day traversal; no completed day is refetched merely to change its rolling/historical label.
- Month compaction affects completed operational sync/checkpoint records only. A transaction may replace contiguous completed operational records with a summary after verifying the daily coverage ledger; it never changes coverage-day proofs or canonical note rows.
- After rolling/frontier maintenance, a short transaction derives its next `D` from PostgreSQL `statement_timestamp() AT TIME ZONE 'America/Sao_Paulo'`, deletes canonical rows and daily proofs strictly before `D-366`, removes inactive/superseded candidates, retires irrelevant operational metadata, and upserts `{horizon_date: D, retained_from: D-366, retained_through: D}` in the same commit. Legacy-repair startup preserves all existing cache rows; routine pruning/first context-state publication begins only after the new model has at least one successfully published generation for the context.
- Coverage is the exact count/continuity of daily proof rows for the requested context/dates. Month/year/leap-day transitions, midnight interleavings, inverted bounds and cross-context reuse therefore have one set-based answer and are explicit test fixtures.

#### Request snapshot and horizon admission

- The first statement inside each local list/export `REPEATABLE READ` transaction selects the fiscal context-state row and establishes the MVCC snapshot. When the row exists, its `horizon_date`, `retained_from` and `retained_through` are the only admission/freshness clock for that request.
- Before the first retained-horizon row exists, the same first statement also returns PostgreSQL `statement_timestamp()` and derives provisional `[D-366,D]` bounds. This is safe because retention is forbidden until it atomically creates that row; if another transaction creates/prunes afterward, the older request snapshot still sees pre-prune rows/proofs. Once an anchor is snapshot-visible, provisional bounds are never used.
- Local list/export without `documento` require `dataInicio >= retained_from`, `dataFim <= retained_through` and the existing maximum-span rule. A violation performs no provider/cache/export work and returns HTTP `422` with `{statusCode: 422, erro: 'PeriodoFiscalForaDoHorizonte', mensagem: 'O período deve estar entre as datas suportadas.', detalhes: {dataMinima: 'YYYY-MM-DD', dataMaxima: 'YYYY-MM-DD'}}`, using the snapshot-visible bounds.
- React constrains the local date controls to the same `[D-366,D]` bounds and renders the exact backend error if a stale URL violates them. The provider-backed `documento` path preserves its existing valid-date/max-span contract and is not reclassified as local coverage.
- After admitting the snapshot-visible retained bounds, list reads coverage metadata, total and page rows inside that same logical Prisma transaction; export reads coverage/admission and all bounded rows inside its equivalent snapshot before building the CSV buffer.
- Publication or retention that commits during a request is wholly before or wholly after that request's database snapshot. Responses cannot combine old totals/coverage with new rows, and an export admitted as complete cannot lose rows to concurrent pruning.

#### Scheduler ownership and bounded work

- One `pumpPromise` owns synchronization in the NestJS process. Startup and 15-minute ticks coalesce onto it; a tick never creates a second pump, and shutdown stops admitting new work before awaiting/cancelling the current bounded provider operation.
- Each pump captures `D` once and services rolling `D-1..D` for every configured fiscal context first. It then advances at most one missing historical coverage window globally, rotating the starting context after each attempt so Unifast and Prosperar cannot starve each other.
- Provider page walks are sequential globally in the approved one-replica topology. Persisted cooldown/backoff is honored before admission, and stale `running` ownership is recovered deterministically without concurrent generations.
- Interactive list/export never awaits the pump. A request may issue a coalesced nudge only; it reads the canonical projection and persisted state immediately.

#### Frozen public read-model contract

For list responses without `documento`, `readModel` preserves the existing fields and adds these exact fields:

| Field | Type / values | Consumer meaning |
| --- | --- | --- |
| `syncState` | `idle \| syncing \| failed` | current operational state for the requested context/interval |
| `freshnessState` | `current \| historical_snapshot \| stale_rolling \| unknown` | interval-scoped meaning of the persisted proof timestamps |
| `completedWindows` | non-negative integer | number of canonical daily coverage proof units complete for the requested interval |
| `totalWindows` | positive integer | inclusive number of calendar days required for the requested interval |
| `lastSyncError` | `provider_rate_limited \| provider_unavailable \| provider_timeout \| pagination_inconsistent \| unexpected \| null` | sanitized reason for the latest relevant failed generation |
| `retryAfterSeconds` | non-negative integer or `null` | remaining persisted cooldown when known |

- Existing `syncing` is retained as an additive-compatibility alias and equals `syncState === 'syncing'`. `syncState` is `syncing` when any relevant interval generation is active; otherwise `failed` when an incomplete relevant window has a latest failure; otherwise `idle`. A successful relevant publication clears its prior `lastSyncError` and `retryAfterSeconds`.
- `completedWindows` and `totalWindows` are computed from the canonical daily coverage ledger for the exact requested interval; a valid local list interval has `totalWindows >= 1` and `0 <= completedWindows <= totalWindows`.
- For `coverage=complete`, `lastSuccessfulSyncAt` is the minimum `published_at` across all requested daily proofs and `cacheAgeSeconds` is its non-negative age at the transaction timestamp. For `coverage=partial`, both fields are `null` because no interval-wide successful snapshot exists.
- `freshnessState=unknown` for partial coverage. Using snapshot-visible `horizon_date` as `D`, complete coverage is `stale_rolling` when any requested `D-1`/`D` proof is older than 15 minutes; otherwise `historical_snapshot` when the interval includes any date `<=D-2`; otherwise `current`. Existing `stale` is the compatibility alias `freshnessState !== 'current'`.
- Historical proofs are immutable snapshots, not continuously fresh assertions. `historical_snapshot` discloses the conservative timestamp and offers no retry/deep-refresh action because periodic deep reconciliation remains outside this TODO; a separate approved change is required to alter that ownership.
- `coverage=complete` with zero rows means a proven empty result and uses the ordinary empty-state copy.
- `coverage=partial` with zero rows remains HTTP `200`, suppresses the ordinary empty-state copy and shows an actionable synchronization message with progress/error/retry data; it must not imply that no fiscal notes exist.
- `coverage=partial` with stored rows renders those canonical rows with the same actionable partial-state disclosure.
- Export checks coverage before opening the CSV response. Incomplete coverage returns the JSON error envelope with HTTP `409` and exact code `ExportacaoFiscalCoberturaIncompleta`; it writes no CSV bytes.
- Detail, PDF, XML and `documento`-filtered operations retain the existing provider-backed contract and do not claim these local coverage guarantees.

| List state | Rows | React presentation | Export action |
| --- | --- | --- | --- |
| `coverage=complete`, `freshnessState=current` | any | ordinary table or ordinary proven-empty state; no synchronization warning | enabled |
| `coverage=complete`, `freshnessState=historical_snapshot` | any | table/empty state plus historical-snapshot timestamp/disclaimer; no unsupported retry action | enabled against the same complete local snapshot |
| `coverage=complete`, `freshnessState=stale_rolling` | any | table/empty state plus stale rolling notice, retry delay and update action | enabled against the same complete local snapshot |
| `coverage=partial`, `syncState=syncing` | any | stored rows when present; otherwise no ordinary empty copy; show progress `completedWindows/totalWindows` | disabled with incomplete-coverage explanation |
| `coverage=partial`, `syncState=failed` | any | stored rows when present; otherwise no ordinary empty copy; show sanitized reason and retry delay/action | disabled with incomplete-coverage explanation |
| `coverage=partial`, `syncState=idle` | any | stored rows when present; otherwise no ordinary empty copy; show pending-synchronization action | disabled with incomplete-coverage explanation |
| HTTP `422 PeriodoFiscalForaDoHorizonte` | none | preserve filters, show supported `[D-366,D]` dates and offer reset to the default yesterday/today interval | disabled; no download |

The backend remains authoritative: a stale client that submits export during partial coverage still receives exact `409`, and a stale URL outside the horizon receives exact `422`; neither response creates a download.

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
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-6-luna`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `not-requested`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Profile:** `Operational / Coder`
- **Scope:** `nestjs, react, vite, postgresql, prisma`
- **Package-first result:** Delphi package query for `fiscal cache synchronization read model` completed with zero matches; the existing host-owned fiscal module remains the selected boundary and no dependency is added. Node capability audits for NestJS and Prisma returned `ready`.
- **Guard outcome:** `go`
- **Waiver / exception reference:** `n/a`
- **Guard evidence:** `agent_role_routing_guard.py --client codex --surface implementation --role routine-executor --model gpt-6-luna --effort medium --proof-mode declared --execution-topology primary-checkout-single-writer --worktree-authorization not-authorized` returned `Overall outcome: go` on 2026-10-01. Pre-approval authority guard must be rerun after the refined review; earlier `preflight-go` is historical only.

**Routing refresh for the 2026-10-01 incident:** the current Delphi contract selects `gpt-6-luna` for a future routine implementation executor; this preflight declares that future lane only, not that execution has begun. The user chose `gpt-6-sol` for this WSL window, so the incident's independent review lanes were dispatched with `gpt-6-sol`; the primary chat's actual model is not inferred from this TODO. The future implementation model must be confirmed against the user's preference at execution start rather than silently changed. No worktree or parallel code-writer authority follows from model selection.

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

- [ ] Substituir o bootstrap móvel por travessias históricas month-clipped em `[D-366,D-2]`, com checkpoint operacional e prova diária canônica por contexto.
- [ ] Persistir páginas em gerações candidatas invisíveis e publicar cache/cobertura atomicamente apenas após a validação integral da janela.
- [ ] Aplicar pertença exata por data/contexto e remover, na publicação, registros comprovadamente ausentes da janela sem apagar dados fora dela.
- [ ] Registrar completude em um ledger diário canônico e executar promoção/ausência em SQL set-based com índices e timeouts limitados.
- [ ] Impedir falsa completude validando contagem distinta candidata, itens brutos observados e total esperado inclusive após checkpoint/restart.
- [ ] Executar reconciliação `D-1..D` independentemente do bootstrap histórico e sem bloquear listagem/exportação.
- [ ] Orquestrar startup/ticks em um único pump não sobreposto, com rolling prioritário, trabalho histórico globalmente limitado e alternância justa entre contextos.
- [ ] Calcular cobertura do intervalo solicitado a partir das janelas concluídas e da janela rolling aplicável.
- [ ] Fazer listagem/paginação sem `documento` lerem PostgreSQL imediatamente, divulgando cobertura, sincronização, frescor e progresso de modo explícito.
- [ ] Ler cobertura/contagem/linhas em um único snapshot `REPEATABLE READ` e rejeitar intervalos locais fora de `[D-366,D]` com `422 PeriodoFiscalForaDoHorizonte`.
- [ ] Derivar `D` dentro do snapshot PostgreSQL e calcular frescor conservador a partir de `published_at` diário para o intervalo exato.
- [ ] Fazer exportação sem `documento` ler PostgreSQL quando o intervalo estiver coberto e rejeitar cobertura incompleta com erro próprio antes de gerar CSV.
- [ ] Preservar e reaproveitar as notas já armazenadas; migrar/aposentar com segurança o registro legado de bootstrap sem declarar cobertura não comprovada.
- [ ] Corrigir o mapeamento de erros para separar indisponibilidade real do provedor de projeção incompleta/inconsistente.
- [ ] Atualizar o contrato React e os avisos de lista/exportação para os estados corretos, sem download parcial.
- [ ] Atualizar o módulo canônico `fiscal-notes-and-documents.md` para substituir a travessia histórica por requisição descrita em `FISC-EX-02/FISC-EX-04` pela leitura local coberta.
- [ ] Adicionar regressões causais; como o RED pré-correção não foi preservado, classificar a execução real como `test-after`, além de integração PostgreSQL, planos/limites e smoke autenticado de stage com revisão exata atestada.
- [ ] Ampliar o record de listagem, candidate/cache Prisma e CSV para todos os campos conhecidos do `GET /notas`, incluindo nome, documento, e-mail e localização do tomador, sem chamadas ao detalhe.
- [ ] Adicionar migration expand-only com colunas nullable, preservar linhas existentes e permitir backfill somente por sincronização normal do provedor.
- [ ] Atualizar regressões de adapter, serializer, cache, migration e contrato HTTP para a projeção/ordem completa e para a não exposição de PII em logs.
- [ ] **Incidente proposto; aprovação pendente:** separar espera de admissão local (`ExportacaoFiscalOcupada`) de falha efetiva da sincronização, preservando geração/checkpoint e limites de concorrência enquanto a unidade aguarda sua próxima oportunidade.
- [ ] **Incidente proposto; aprovação pendente:** identificar com metadados sanitizados a categoria exata de `SmartNotasContratoInvalido` e correlacionar janela/página; o checkpoint de março sugere a página seguinte, mas o log atual não contém página. Nenhuma validação pública/privada muda nesta autorização.

## Out of Scope

- Emissão, cancelamento, alteração ou qualquer endpoint mutável do Smart Notas.
- Escrita, normalização ou mudança de semântica da tabela externa `logs`.
- Cache de URLs de PDF/XML ou armazenamento indiscriminado de payloads com dados pessoais.
- Agregação entre contextos fiscais.
- Deploy Railway, mudança de credenciais/quota ou alteração do cutover Smart Notas já aberto.
- Exportação parcial, botão para “baixar o que já existe” ou qualquer CSV apresentado como completo sem cobertura integral do intervalo.
- Fila/worker externo, nova réplica, lease distribuído, alteração do scheduler de infraestrutura ou operação destrutiva direta no banco de stage.
- Persistência de payload bruto, campos exclusivos do detalhe, telefone/endereço completo, PDF, XML ou URL efêmera.
- Para este incidente: aumentar arbitrariamente `timeout`, 2 MiB de corpo, `perPage`, quota ou concorrência; relaxar o parser para aceitar dados fiscais desconhecidos; executar consulta/correção destrutiva em produção.

## Historical Canonical Anchors — Delivered Baseline

- `foundation_documentation/project_constitution.md`
- `foundation_documentation/modules/fiscal-notes-and-documents.md`
- `foundation_documentation/modules/events-and-classification.md`
- `foundation_documentation/modules/operational-monitoring.md`
- `foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-note-read-model.md`

## Architecture Change Governance

- **Applicability:** `required`
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
| unit test | cache/sync state machine | `fiscal-note-cache.service.spec.ts` | total muda após checkpoint, restart de janela e rolling independente | `implement-in-this-todo` | regressão test-after + suite completa; nenhum artefato RED histórico é alegado |
| integration test | Prisma/PostgreSQL coverage | real local PostgreSQL fixture | gaps/overlaps, contexto cruzado, aposentadoria legada e export coberto | `implement-in-this-todo` | migration/schema check + query assertions |
| contract test | list/export errors and metadata | Nest application specs | cobertura incompleta disfarçada de provider error ou CSV parcial | `implement-in-this-todo` | exact status/code/body/header assertions |
| browser test | React list/export | existing frontend E2E/unit runner | aviso permanente, erro incorreto ou download parcial | `implement-in-this-todo` | source-owned test + stage smoke |
| performance/load | DB pagination/export + sync pacing | EPS/RLS artifacts | provider call on covered export, query regression or sync storm | `implement-in-this-todo` | machine-checkable `pcv-1` evidence |
| incident state-machine tests | coordinator/cache + PostgreSQL | `fiscal-rate-coordinator*.spec.ts`, `fiscal-note-cache*.spec.ts`, read-model integration spec | local `ExportacaoFiscalOcupada` falsely persisted as provider failure or destroys rolling/historical checkpoint | `implement-in-this-todo` | `DOD/VAL-RM-I01`, RED/GREEN and zero-extra-provider-call assertions; execution begins only after renewed approval |
| incident observability/privacy tests | Smart Notas adapter | `smart-notas.adapter.spec.ts` and bounded log spy | invalid HTTP-200 response has no safe subtype or logs a provider value/URL/PII | `implement-in-this-todo` | `DOD/VAL-RM-I02`, one-event/category/negative-content assertions; execution begins only after renewed approval |
| incident consumer contract tests | Nest API + React existing normalizer/browser | source-owned contract/browser tests | local wait shown as provider failure or CSV enabled under partial coverage | `implement-in-this-todo` | `DOD/VAL-RM-I03`, no public enum change; execution begins only after renewed approval |

## Definition of Done

- [ ] `DOD-RM-C01` Histórico usa travessias month-clipped até `D-2`, publica prova diária canônica, retoma/reinicia localmente e não perde notas já armazenadas.
- [ ] `DOD-RM-C02` Rolling `D-1..D` executa a cada 15 minutos independentemente da conclusão histórica.
- [ ] `DOD-RM-C03` Listagem/paginação sem `documento` nunca aguarda provider e representa corretamente intervalos completos, parciais e vazios.
- [ ] `DOD-RM-C04` Exportação sem `documento` usa somente PostgreSQL para intervalo coberto e retorna `409 ExportacaoFiscalCoberturaIncompleta` sem bytes CSV quando incompleto.
- [ ] `DOD-RM-C05` Estado legado de stage possui caminho idempotente e não destrutivo de reparação; nenhuma cobertura é marcada completa por inferência de contagem.
- [ ] `DOD-RM-C06` Erros públicos distinguem provider real de sincronização/cobertura local, e a UI apresenta mensagens acionáveis.
- [ ] `DOD-RM-C07` Detalhe, PDF, XML e filtro `documento` continuam provider-backed e os contextos fiscais permanecem isolados.
- [ ] `DOD-RM-C08` Módulo canônico, testes, builds, lint, Prisma/PostgreSQL, EPS/BCI/RLS e evidência de stage estão coerentes com a decisão aprovada.
- [ ] `DOD-RM-C09` Uma janela incompleta/falha nunca altera cache ou cobertura visível; publicação concluída troca conjunto canônico, ausências e estado em uma única transação.
- [ ] `DOD-RM-C10` Horizonte e frontier não possuem gap/overlap em viradas de mês/ano/29 de fevereiro, e o scheduler não sobrepõe pumps nem causa starvation entre contextos.
- [ ] `DOD-RM-C11` Contrato público distingue `complete+zero`, `partial+zero`, sincronizando e falha pelos campos congelados em `D-RM-C14`.
- [ ] `DOD-RM-C12` Listagem e exportação nunca misturam cobertura/total/linhas de gerações diferentes, mesmo quando publicação ou retenção confirma entre statements.
- [ ] `DOD-RM-C13` Consultas locais fora de `[D-366,D]` falham deterministicamente com `422 PeriodoFiscalForaDoHorizonte`; o ledger diário não mantém prova de datas podadas.
- [ ] `DOD-RM-C14` Publicação de 0, poucas e 20.000 linhas é set-based, indexada, limitada por timeout e deixa a geração anterior intacta em qualquer rollback.
- [ ] `DOD-RM-C15` Duplicata de `providerIdInterno` entre páginas ou após restart impede publicação e preserva cache/coverage anterior com `pagination_inconsistent`.
- [ ] `DOD-RM-C16` Frescor de intervalo completo/zero é derivado de prova diária durável e distingue histórico, rolling atual e rolling vencido sem oferecer deep refresh inexistente.
- [ ] `DOD-RM-C17` Admissão usa o horizonte persistido visível no mesmo snapshot das linhas; poda e avanço do horizonte confirmam juntos na virada do dia.
- [ ] `DOD-RM-C18` Intervalos parciais consultados recebem prioridade deduplicada e justa após rolling, sem mais de uma unidade histórica por pump e sem starvation do bootstrap de fundo.
- [ ] `DOD-RM-C19` A abertura padrão usa ontem/hoje; a tela revalida somente a consulta local parcial aplicada, cancela timers obsoletos e habilita exportação automaticamente após cobertura completa.
- [ ] `DOD-RM-C20` A projeção local e o CSV incluem exatamente todos os campos allowlisted de `GET /notas`, preservam CPF/CNPJ como texto, não consultam detalhe por linha e não registram PII em observabilidade.
- [ ] `DOD-RM-C21` A migration adiciona campos nullable em cache/candidates, preserva linhas antigas e o sync subsequente preenche os novos valores sem operação destrutiva.
- [ ] `DOD-RM-I01` **Proposto; aprovação pendente:** recusa **temporária** de admissão local não é persistida nem apresentada como falha do provedor, não apaga checkpoint/candidates/geração e não limpa erro real ou reinicia bootstrap/rolling antes da admissão. Estados internos deferred conservam relógio e progresso por reinício, seeding, pump, publicação por nota movida e retenção; configuração sem vaga de exportação é falha operacional sanitizada e não entra em retry infinito. Linhas antigas `*_failed/ExportacaoFiscalOcupada` são projetadas/reclassificadas sem destruir progresso; um erro real anterior e sua ordenação temporal nunca são apagados por recusa local.
- [ ] `DOD-RM-I02` **Proposto; aprovação pendente:** rejeição real do contrato Smart Notas em `list` continua fail-closed; o evento estruturado **já existente** recebe exatamente uma categoria allowlisted por tentativa, inclusive `body_declared_invalid`, contexto/janela/página/correlação, tamanho quando conhecido e nome/tipo da validação quando seguro, sem segunda linha, corpo bruto, URL, valores de campos, credenciais ou PII; nenhuma aceitação nova é introduzida antes da evidência sanitizada e da aprovação posterior.
- [ ] `DOD-RM-I03` **Proposto; aprovação pendente:** API/React reutilizam os estados públicos existentes e `retryAfterSeconds` para distinguir espera local de falha real sem polling de 2s durante um cooldown de 60s; `partial/failed` sem prazo de retry não agenda novas consultas automáticas, preservando atualização manual. Cobertura completa com rolling vencido mantém aviso de frescor atual, não novo banner de falha; CSV continua proibido apenas quando a cobertura diária exata é incompleta.

## Validation Steps

- [ ] `VAL-RM-C01` Executar regressões causais para total alterado após checkpoint, processo reiniciado, rolling concorrente, intervalo coberto/incompleto e mapeamento fiel de erro; registrar como `test-after` quando não houver artefato RED preservado.
- [ ] `VAL-RM-C02` Executar suites completas backend/frontend, lint, builds e validação/generação Prisma.
- [ ] `VAL-RM-C03` Em PostgreSQL local real, validar janelas sem gap/overlap, isolamento, migração/reparação legada e planos de paginação/exportação.
- [ ] `VAL-RM-C04` Validar concorrência entre bootstrap, rolling, listas e exports sem duplicidade, perda de checkpoint ou tempestade upstream.
- [ ] `VAL-RM-C05` Medir exportações pequena/média/20.000 linhas e paginação DB, comprovando zero chamadas Smart Notas no intervalo coberto.
- [ ] `VAL-RM-C06` Validar no React aviso parcial/progresso, remoção do aviso após cobertura e ausência de download em `409`.
- [ ] `VAL-RM-C07` Após deploy autorizado, atestar `branch@sha`, consultar estado agregado redatado, reparar sem destruição e executar smoke autenticado de lista/exportação no stage.
- [ ] `VAL-RM-C08` Executar guards TODO/diff/completion, auditoria de qualidade de testes, revisão final no-contexto e consolidação do módulo.
- [ ] `VAL-RM-C09` Injetar falha tardia após páginas persistidas e provar que nenhum candidato, ausência ou cobertura parcial se torna visível.
- [ ] `VAL-RM-C10` Cobrir nota removida, nota movida de data, data nula/malformada/fora da janela, publicação vazia, compactação mensal, restart e geração supersedida.
- [ ] `VAL-RM-C11` Cobrir ticks simultâneos, startup concorrente, shutdown, cooldown, prioridade rolling, alternância justa e ausência de starvation.
- [ ] `VAL-RM-C12` Forçar publicação/retenção entre leitura de cobertura, contagem e linhas por barreiras reais no PostgreSQL, provando snapshot coerente para página e CSV.
- [ ] `VAL-RM-C13` Cobrir limites `D-366`/`D`, um dia antes/depois, URL antiga, caminho `documento`, avanço de retenção e transição rolling→frontier à meia-noite.
- [ ] `VAL-RM-C14` Medir `EXPLAIN`, statements, locks, rollback e latência concorrente para publicação vazia/pequena/20.000 linhas.
- [ ] `VAL-RM-C15` Reiniciar após checkpoint e repetir o mesmo provider ID em páginas diferentes; provar `candidate count != raw observed`, rollback e cobertura inalterada em PostgreSQL real.
- [ ] `VAL-RM-C16` Cobrir complete-zero, histórico puro, histórico+rolling atual, rolling vencido/falhado e respectivas mensagens/ações no backend e browser.
- [ ] `VAL-RM-C17` Em PostgreSQL real: (a) com anchor existente, abrir transação antes da meia-noite e confirmar retenção+novo horizonte antes e depois da primeira leitura, provando visões nova/antiga coerentes; (b) sem context-state, estabelecer o snapshot/provisional bounds, confirmar em paralelo a primeira criação do anchor+poda e provar que a requisição original ainda vê coverage/count/rows pré-poda, enquanto nova requisição vê o anchor e nunca usa bounds provisórios.
- [ ] `VAL-RM-C18` Provar em Jest que demandas idênticas coalescem, a janela consultada precede o histórico antigo, contextos alternam e uma unidade de fundo é atendida após no máximo três demandas.
- [ ] `VAL-RM-C19` Provar em testes unitários/browser que a URL vazia usa ontem/hoje, partial dispara revalidação automática sem clique, troca de filtro cancela o ciclo antigo e CSV é habilitado ao receber cobertura completa.
- [ ] `VAL-RM-C20` Executar regressões do adapter, serializer, cache e contrato HTTP provando a ordem completa do CSV, nulls, zeros à esquerda, fórmula, caracteres especiais e ausência de chamadas ao detalhe.
- [ ] `VAL-RM-C21` Executar `prisma validate`, `prisma generate` e aplicar a migration em bancos PostgreSQL descartáveis vazio e baseline, provando linhas legadas preservadas e novos campos nullable.
- [ ] `VAL-RM-I01` **Proposto; aprovação pendente:** reproduzir RED e depois GREEN para duas janelas do mesmo contexto dentro de 60s, checkpoint 3/4, rolling novo/existente e linhas antigas `bootstrap_failed/ExportacaoFiscalOcupada`; cobrir cooldown, lease e capacidade temporária com zero chamada adicional ao provedor, geração/candidates/progresso intactos, reinício do processo, retomada após relógio persistido e ambos os contextos. Forçar seeding, demanda, pump, publicação por nota movida e avanço da retenção durante um checkpoint deferred; provar que nenhum deles apaga ou torna invisível a geração. Testar `maxConcurrency=1` e export share zero: falha operacional sanitizada uma vez, nenhum loop de tentativas, nenhuma perda de erro real/projeção publicada.
- [ ] `VAL-RM-I02` **Proposto; aprovação pendente:** reproduzir RED e depois GREEN para `list` HTTP 200 com corpo ausente, `Content-Length` malformado/negativo/acima de 2 MiB, stream acima de 2 MiB, JSON inválido, envelope/metadados de página e campo inválido em página 2; verificar categoria allowlisted, janela/página/correlação, **uma linha final existente por tentativa**, status público inalterado e ausência de URL, payload, token, nome/CPF/e-mail e valores de campos nos logs.
- [ ] `VAL-RM-I03` **Proposto; aprovação pendente:** validar em PostgreSQL, contrato HTTP e browser linha incidente legada e novo deferred como `coverage=partial`, `syncState=idle`, `lastSyncError=null`, `retryAfterSeconds` não nulo durante a espera, mensagem pendente e sem CSV; repetir com vários viewers para provar cadência bounded de leituras/nudges e zero chamadas extras ao provedor. Para configuração impossível e cobertura parcial, observar mais de um cooldown com vários viewers: `failed/unexpected`, prazo nulo, zero releituras/nudges/admissões **automáticas**, mas atualização manual disponível. Para rolling completo/vencido, preservar `complete/idle`, metadado de erro/log sanitizado, aviso de frescor e CSV permitido, sem novo banner. Forçar um erro real anterior seguido de recusa local e janelas sobrepostas para provar precedência/ordenação do erro; exportação parcial só libera após prova completa. Depois de deploy separadamente autorizado, atestar `branch@sha` e repetir consulta agregada sem dados de notas.

## Test Decisions — Frozen

| ID | Decision | Evidence lane |
| --- | --- | --- |
| `D-T01` | Test-first intended; test-after observed | The approved intent was fail-first, but no immutable pre-fix RED artifact was preserved. Current evidence is limited to causal test-after regressions for late-page failure, cross-page/restart duplicate IDs, superseded generation, removed/moved/null/out-of-window records, complete-zero/partial-zero, freshness states, rolling→daily proof, horizon admission and stale fallback. |
| `D-T02` | Integration | On real PostgreSQL, prove distinct/raw/expected completeness, set-based atomic publication, daily proof/retention and DB-date-aligned one-snapshot list/export under forced commit interleavings; preserve provider-backed detail/PDF/XML contracts. |
| `D-T03` | Concurrency | Simultaneous startup/ticks/requests share one pump and captured `D`; rolling has priority, historical work is globally bounded, contexts alternate fairly and shutdown admits no new work. |
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
| `uninotas-foundation` | `uninotas-foundation` | `main@d10c04f` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/schema.prisma` | `M` | required candidate ownership, daily coverage proof, retained-horizon context state and atomic publication contract |
| `MonitorNotes` | `backend/prisma/migrations/**` | `A, ??` | required expand-only candidate/coverage/horizon migration and supporting constraints/indexes |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `A, M, ??` | windowed bootstrap, rolling independence, local reads, truthful errors and regression tests |
| `MonitorNotes` | `backend/src/common/filters/**` | `M` | public error mapping for incomplete read-model coverage if centrally owned there |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | interval coverage/progress contract and export error handling |
| `MonitorNotes` | `frontend/src/api/cliente.ts` | `M` | preserve the structured public error code and retained-horizon bounds for truthful UI handling |
| `MonitorNotes` | `frontend/src/notas/**` | `A, M, ??` | metadata normalization/cache/export controller regression coverage |
| `MonitorNotes` | `frontend/src/notas/urlFiscal.ts` | `M` | request-snapshotted local horizon normalization and stale-URL handling |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | actionable partial/complete synchronization state |
| `MonitorNotes` | `frontend/e2e/**` | `A, M, ??` | browser-visible list/export regressions when this is the source-owned runner |
| `MonitorNotes` | `frontend/src/**/*.spec.ts*` | `A, M, ??` | frontend contract/render regressions |
| `MonitorNotes` | `delphi-ai` | `M` | pre-existing workspace link reflects the separately approved Delphi helper commit; excluded from product staging |
| `MonitorNotes` | `foundation_documentation` | `M` | pre-existing Foundation workspace link reflects TODO evidence; excluded from product staging |
| `MonitorNotes` | `uninotas-foundation` | `M, T` | pre-existing tracked-gitlink versus workspace-symlink topology; excluded from product staging |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-read-model.md` | `M` | approval, decisions and delivery evidence |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | canonical local-read/export/coverage contract and superseded provider traversal decisions |
| `uninotas-foundation` | `domain_entities.md` | `M` | document the rebuildable candidate, coverage, synchronization and horizon entities without changing fiscal authority |
| `uninotas-foundation` | `system_roadmap.md` | `M` | evidence-only status synchronization from planned to locally implemented and promotion-pending |
| `uninotas-foundation` | `artifacts/dependency-readiness.md` | `M` | redacted stage/provider readiness evidence via DevOps handoff if runtime status is refreshed |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A, M, D, R` | secrets/local environment are excluded |
| `MonitorNotes` | `backend/src/logs/**` | `A, M, D, R` | external logs remain outside the read model |
| `MonitorNotes` | `Dockerfile`, `railway.json`, `.github/**` | `A, M, D, R` | deployment/CI topology is outside this correction |
| `uninotas-foundation` | `project_constitution.md` | `M` | no constitutional invariant change is authorized |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| workspace links `delphi-ai`, `foundation_documentation`, `uninotas-foundation` | noise / governed support topology | links predate this product implementation; Delphi and Foundation changes were separately authorized and versioned in their owning repositories | retain links locally; exclude them from MonitorNotes staging | already authorized by user during this TODO session |
| `frontend/src/api/cliente.ts` | required public-error support | the list/export UI must receive the exact backend code and retained-horizon bounds; no unrelated client behavior changed | admit as implementation scope | covered by frontend deterministic/build checks |
| `domain_entities.md`, `system_roadmap.md` | required canonical evidence sync | entity ownership and roadmap stage must match the locally implemented, promotion-pending read model without granting deployment authority | admit as Foundation evidence scope | remains subject to the blocked scope-drift refresh/push gate |
| root `artifacts/**` corpus | generated verification noise, pruned | 384 untracked review/browser/prior-TODO artifacts were inventoried; durable conclusions were consolidated in the TODO and the current FRC artifact was made self-contained | removed from the workspace after explicit user authorization; recoverable quarantine recorded in session handoff | authorized by user on 2026-09-30; diff guard now passes with 24/24 classified changes |

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
| `operational-coder` | `assurance-tester-quality` | TODO `big`, bugfix arquitetural e contrato público | bounded TODO/code/test/evidence packages | `architecture review executed; PostgreSQL/test-quality evidence still pending` |
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

## Decision Resolution / Renewed Approval Pending

- [x] `D-RM-C01..C27`: as opções da baseline anterior foram comparadas e aprovadas nas datas registradas; sua aprovação não se estende automaticamente ao incidente de `2026-10-01`.
- [x] `D-RM-I01`: direção revisada: preservar geração/checkpoint/candidates; recusa **transitória** vira espera com relógio persistido, enquanto configuração sem capacidade é falha operacional visível sem loop. Linhas legadas ocupadas ganham projeção/retomada segura. Achados da primeira rodada integrados; requer nova baseline/revisão e `APROVADO`, não implementado.
- [x] `D-RM-I02`: os 21 logs confirmam HTTP 200 em ambos os contextos mas não informam subtipo. Direção revisada: enriquecer o único evento existente de `list` com categoria sanitizada, inclusive comprimento declarado inválido, **sem alterar o parser**; outra decisão/aprovação será necessária se o contrato aceito mudar. Requer nova baseline/revisão e `APROVADO`, não implementado.
- [x] `D-RM-I03`: direção revisada: reutilizar `idle`/`failed` e `retryAfterSeconds` públicos existentes para evitar polling de 2s durante a espera; preservar erro real anterior e bloquear CSV incompleto. Sem novo enum/mensagem. Requer nova baseline/revisão e `APROVADO`, não implementado.
- [ ] `D-RM-I03/R3`: decidir com o usuário se aceita o booleano aditivo `readModel.autoRetry` (Opção A recomendada) para diferenciar incapacidade estática de falha recuperável. A regra atual de parar todo `partial/failed` com prazo nulo **não** pode ser executada porque perdeu a atualização automática após publicação assíncrona. Após a decisão, atualizar contrato/testes, congelar baseline e revalidar; nada implementado.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `fiscal-notes-and-documents#FISC-EX-01` | export aplica um contexto e todos os filtros | `Preserve` | `Canonical Decision Register` |
| `fiscal-notes-and-documents#FISC-EX-02` | backend percorre páginas do provedor para cada export | `Supersede (Intentional)` | `D-RM-C04/C06`; local covered export becomes canonical |
| `fiscal-notes-and-documents#FISC-EX-03` | Buffer completo antes da resposta | `Preserve` | CSV atomic application boundary remains |
| `fiscal-notes-and-documents#FISC-EX-04` | consistência detectável da paginação provider, sem snapshot | `Supersede (Intentional)` | provider checks move to sync windows; export consistency becomes DB coverage/query based |
| `fiscal-notes-and-documents#FISC-EX-05..10` | HTTP/CSV/security/limits/coordinator contracts | `Preserve`, except `FISC-EX-08` is intentionally superseded by the approved complete list-projection CSV in `D-RM-C23..C27` | module sections cited above |
| `fiscal-notes-and-documents#FISC-VIS-01..03` | positive response allowlists and signed IDs | `Supersede (Intentional)` | extend only the internal normalized list/cache/export projection; keep the public paginated summary and signed route identity unchanged |
| `fiscal-notes-and-documents#FISC-DOC-01..03` | PDF/XML provider-backed | `Preserve` | `D-RM-C09` |
| `fiscal-notes-and-documents#FISC-CAN-01` | proposed cancellation | `Out of Scope` | cancellation TODO remains independently gated |
| `events-and-classification#note_read_model transition` | legacy module remains current owner until cutover | `Preserve` | scope policy `note-read-model-001` stays planned |

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-RM-C01` | Smart Notas has no transactional snapshot/cursor/stable-order contract for list pagination. | `uninotas-foundation/modules/fiscal-notes-and-documents.md` (`FISC-EX-04`); `backend/src/fiscal-notes/smart-notas.adapter.ts` | provider-native delta/snapshot could simplify sync and would require contract refresh | `High` | `Keep as Assumption` |
| `A-RM-C02` | The moving total can change because the delivered bootstrap includes the current day and freezes metadata across pages/retries. | `backend/src/fiscal-notes/fiscal-note-cache.service.ts:164`; `backend/src/fiscal-notes/fiscal-note-cache.service.ts:249`; `backend/src/fiscal-notes/fiscal-note-cache.service.ts:326` | if provider guarantees immutable totals, windowing remains bounded and safer but root cause may be another stored error | `High` | `Keep as Assumption` |
| `A-RM-C03` | Existing canonical cache/sync rows cannot prove atomic complete-window publication because page writes are immediately visible and have no isolated generation ownership. | `schema.prisma:91-109`; `fiscal-note-cache.service.ts` page upserts | an expand-only candidate-generation migration is required and must be validated on empty and delivered-baseline schemas | `High` | `Resolved into D-RM-C11/C12` |
| `A-RM-C04` | Stage runs one API replica. | dependency readiness records `replicas=1` | distributed lease becomes required before deployment | `Medium` | `Block deployment, not planning` |
| `A-RM-C05` | Historical 2026-09-29 observation: the exact runtime sync error was unknown from the empty local DB. | local read-only query returned empty sync/cache at that time | later operational evidence may select a different repair branch | `High` for that date | `Superseded by user-provided 2026-10-01 sync rows and attested deploy revision; provider subcause remains open in A-RM-I02` |
| `A-RM-C06` | Historical statuses older than `D-1` may change externally, but broad periodic deep reconciliation is outside this correction. | Smart Notas authority + no changed-since contract | stale older status remains residual risk; cancellation overlay covers only Monitor-owned cancellation | `Medium` | `Keep as Assumption; document residual risk` |
| `A-RM-C07` | `GET /notas` returns the complete listed recipient fields (`nome`, `documento`, `email`, `cidade`, `estado`, `pais`) on each summary record. | user-provided real response sample plus the previously observed `GET /notas` payload | if a field is omitted/null, the nullable projection and CSV emit an empty cell; invalid typed/non-null values remain a provider contract error | `High` | `Keep as Assumption; cover adapter acceptance/nullability` |
| `A-RM-I01` | The four occupied rows may involve the local 60-second actor cooldown, but the exact admission branch and runtime limits are not yet known; the incident contract must handle transient and impossible-capacity branches independently of this guess. | user-provided sync rows seconds apart; `backend/src/fiscal-notes/fiscal-rate-coordinator.ts:startExport`; `backend/src/fiscal-notes/fiscal-note-cache.service.ts:walkPages` | a lease or static configuration fault must take its distinct transition/stop path; do not claim cooldown as proven root cause | `Medium` | `Keep as Assumption; confirm with redacted runtime configuration before Stage observation, but do not block bounded code/tests` |
| `A-RM-I02` | HTTP status 200 is known for the temporally matched March event, but the body/envelope/field rejection subtype is unknown; 200 per page alone is not proof of a size overflow. | checkpoint 1; 21 user-pasted adapter events with `upstreamStatus=200`; adapter logs only outcome/status/duration/correlation, not validation category/page/window | widening validation blindly could admit invalid fiscal data or expose PII | `High` for status; `Low` for subtype | `Instrument sanitized validation category and sync correlation after approval; block parser/limit change until causal evidence` |
| `A-RM-I03` | The incident ran under `main@fb8d88137212bbe549707aa064cc03185a14e6db`, which is not automatically the local `release/uninotas` checkout. | user-supplied revision link plus explicit confirmation that it was active at the failure time; private commit not independently inspected | local-only code analysis could still diverge from the deployed merge, and the target database must be identified before any repair | `High` for user attestation; `Low` for local-code equivalence | `Use the attested SHA for incident attribution; verify deployed/local code differences and exact database target before a runtime-fix or stage-smoke claim` |

## Execution Plan

### Touched Surfaces

- `backend/src/fiscal-notes/**`, conditional `backend/src/common/filters/**`
- required `backend/prisma/schema.prisma` and additive candidate-generation/daily-coverage migration
- `frontend/src/api/notas.ts`, `frontend/src/notas/**`, `frontend/src/paginas/ListaNotas.tsx`, source-owned tests
- `foundation_documentation/modules/fiscal-notes-and-documents.md` and this TODO

### Ordered Steps

1. Add causal regression tests for atomic late-page failure, changed totals/generation restart, removed/moved/null/out-of-window notes, frontier rollover, non-blocking list, scheduler overlap/fairness, interval coverage, complete-only export and truthful zero/error states; record the realized lane as test-after because no pre-fix RED artifact was retained.
2. Add the expand-only candidate-generation plus daily-coverage relational contract and implement set-based one-transaction publication, including exact membership, proven-absence deletion and safe generation cleanup.
3. Model the exact `[D-366,D-2]` historical frontier, `[D-1,D]` rolling publication into daily proofs, horizon admission/retention, operational metadata compaction, legacy retirement and per-window restart/backoff.
4. Decouple synchronization from requests and implement the single bounded scheduler pump with rolling priority, global sequential provider walks, context rotation and shutdown behavior.
5. Implement `REPEATABLE READ` interval coverage/count/row snapshots and local list/export semantics, preserving context/filter/order/20,000-row CSV bounds.
6. Update the exact public read-model/horizon-error contract and React complete-zero/partial-zero/progress/error/date-bound/download lifecycle.
7. Implement non-destructive legacy-state repair and verify against empty/baseline PostgreSQL databases; do not mutate stage directly from this lane.
8. Update the canonical fiscal module, run CI-equivalent/performance/concurrency/security gates, then hand off deployment/smoke to DevOps.
9. Expand the normalized `GET /notas` record and candidate/cache schema with nullable recipient document/e-mail/city/state/country fields, then propagate them through normal synchronization without detail calls.
10. Replace the partial fiscal CSV allowlist with the approved complete list projection, preserving deterministic order, quoting, formula neutralization, size bounds and no-store transport.
11. Validate the additive migration on empty/baseline PostgreSQL plus focused adapter/serializer/cache/application regressions; no frontend change is required because the download contract remains the same.
12. **Incident delta, approval pending:** preserve the user-attested incident `main@fb8d88137212bbe549707aa064cc03185a14e6db` and 21 status-200 logs as baseline; confirm the read-only target environment/database before any Stage operation. No more copies of identical logs are required.
13. **Incident delta, approval pending:** before product edits, refresh/freeze/push the TODO-only review baseline, run renewed plan/audit/critique/coherence/scope-drift/pre-approval gates, and obtain `APROVADO` specifically for `D-RM-I01..I03`. Prior approval and green tests apply only to `D-RM-C01..C27`.
14. **Incident delta, approval pending:** test-first: reproduce transient lease/cooldown, impossible static capacity, checkpoint 3/4, legacy occupied row, prior genuine error, refused rolling and several-viewer polling against the current code. Require preserved generation/candidates, bounded retry and zero extra provider calls. Add synthetic `list` HTTP-200 cases for every safe rejection category, including malformed declared length, and assert the existing single log event contains no raw values/PII.
15. **Incident delta, approval pending:** after renewed approval, separate transient deferral from static operational stop, preserve/compatibly project legacy rows, update every state enumerator/retention path, gate both scheduled and nudged pumps by persisted eligibility, and move **bootstrap and rolling** admission before any state/error or generation/candidate mutation. Keep one pump, no public enum and the original provider error/timestamp on later local refusal. Make the one React timer adjustment that stops automatic polls on `partial/failed` with no retry deadline while retaining manual refresh. Enrich only the existing list failure event from safe query window/page and validation metadata, never URL, document/purchase filters or response values. Preserve fail-closed parsing and complete-only export.
16. **Incident delta, approval pending:** rerun scoped CI-equivalent and PostgreSQL/API/browser checks, independent test-quality/final-review gates and exact-revision Stage smoke after a **separately authorized deployment**. Observe one normal scheduled retry to learn the rejected category. Only then decide a parser/limit correction through refreshed TODO decisions and renewed approval; previous green evidence remains baseline-only.

### Test Strategy

- **Strategy:** `test-after (variance from the approved test-first intent)`
- **Why:** production-like stage symptoms passed all existing immutable-total unit tests, but this execution did not preserve an immutable pre-fix RED run. The final evidence therefore proves causal regressions only and must not be described as TDD/RED-GREEN.
- **Regression targets:** provider total changes after page 1/resume; duplicate provider ID across pages separated by durable restart; late-page failure with zero visible partial publication; stale/superseded generation; removed/moved/null/malformed/out-of-window notes; complete-zero freshness; historical-only/mixed/stale-rolling states; month/year/leap-day rolling→daily transition and retention; publication between coverage/count/items; BEGIN-before-midnight with retention commit before/after the first horizon snapshot read; exact horizon boundaries/URL/path `documento`; simultaneous ticks/startup/requests/shutdown; rolling priority/context fairness; covered/partial zero-row UI; incomplete export exact `409`; no provider call on covered reads; 20.000-row set-based timeout/rollback; exact provider-error preservation.
- **Incident test strategy (not yet executed):** `test-first` for `D-RM-I01..I03`, with deterministic RED on false failure/checkpoint loss after local admission refusal and on missing sanitized contract subtype; GREEN and cross-layer replay only after renewed approval. The adapter fixtures are synthetic and never include a real recipient payload. Existing `test-after` evidence above remains historical and cannot be relabeled RED.

### Package-First Assessment

- **Query executed:** `bash delphi-ai/tools/query_packages.sh --project-root . --search "fiscal csv export"` (rechecked for C23..C27; prior query: `fiscal cache synchronization read model`)
- **Relevant packages found:** none.
- **READMEs read:** `n/a`.
- **Decision:** extend the existing host-owned fiscal-notes module; do not create a package or add a dependency.
- **Tier:** local host implementation.
- **Rationale:** the correction changes UniNotas-specific persistence, synchronization and CSV projection contracts and has no reusable proprietary package match.

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
| incident local wait versus genuine contract failure | financial user's list/export readiness and notices | `web-only` | backend API + source-owned browser regression | `no` | `no` for synthetic regression; read-only Stage smoke after separate deploy approval | `partial/idle/null` says pending and blocks CSV; `partial/failed/unexpected` says real failure; no new public enum | n/a |

## Frontend / Consumer Matrix

| Producer Surface | Consumer | Required State | Failure / Partial State | Evidence | Disposition |
| --- | --- | --- | --- | --- | --- |
| `GET /api/v1/notas` coverage/source metadata | `NotasFiscaisContexto` + `ListaNotas` | covered interval renders local rows without historical-loading warning | partial/failed sync renders an actionable synchronization notice without hiding stored rows | frontend parser/unit + browser list flow | consumer implemented and must be updated/evidenced in this TODO |
| `GET /api/v1/notas/exportar` interval coverage contract | `ListaNotas` export controller | covered interval downloads exactly one CSV | incomplete interval handles `409 ExportacaoFiscalCoberturaIncompleta` and downloads zero bytes | backend contract + browser download flow | consumer implemented and must be updated/evidenced in this TODO |
| local list/export horizon admission | URL normalizer + date controls + `ListaNotas` | interval inside request-captured `[D-366,D]` proceeds | stale/outside URL handles `422 PeriodoFiscalForaDoHorizonte`, preserves filters, offers yesterday/today reset and downloads nothing | backend boundary contract + browser stale-URL flow | consumer must be added/evidenced in this TODO |
| provider-backed detail/PDF/XML/document-filter paths | `DetalheNota`, `AcoesDocumento`, document-filter list | existing provider behavior remains unchanged | provider errors retain existing user-visible behavior | existing unit/browser regression suites | preserve without new consumer behavior |
| background historical/rolling synchronization | no direct UI command surface | UI consumes only explicit read-model metadata | no polling loop or provider traversal is owned by React | backend scheduler tests + frontend negative assertion | consumer intentionally observes metadata only |
| incident: transient local admission | `GET /api/v1/notas` → `ListaNotas` | janela sem vaga permanece incompleta, `syncState=idle`/`lastSyncError=null`/retry countdown e aguarda com checkpoint preservado | recusa local usa mensagem pendente existente, sem novo enum; timer respeita prazo | fail-first coordinator/cache + API + browser cadence/restart | `approval pending`; old green evidence does not cover it |
| incident: impossible static capacity | `GET /api/v1/notas` → `ListaNotas` | cobertura parcial expõe `failed/unexpected` sem prazo automático; usuário pode atualizar manualmente | timer React não agenda revalidação de `partial/failed` com prazo nulo; backend não tenta provider enquanto configuração segue incapaz | PostgreSQL/API + multi-viewer browser across >60s; complete/stale rolling freshness regression | `approval pending`; one scoped frontend timer change |
| incident: invalid provider contract | internal Smart Notas list adapter → persisted sync → `ListaNotas` | rejeição fail-closed com categoria **interna** sanitizada e sem dados pessoais | erro real em intervalo parcial continua `failed`/`unexpected`; aceitação/parser e contrato público só mudam após evidência e aprovação posteriores | synthetic status/body/field negatives + bounded real correlation metadata | `approval pending; exact rejected branch unknown` |

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend cache focused | state machine correction | moving total, restart, daily proof, rolling, horizon, coverage/export/error semantics | deterministic provider pages + sync/coverage rows | `cd backend && npx jest fiscal-note-cache.service.spec.ts --runInBand` | `Local-Implemented` | `passed-local` | focused suite passed in current working tree | database-only assertions remain gated separately |
| backend full | API/error/provider regressions | all fiscal endpoints and common error envelope | `TEST_DATABASE_URL`, no live provider | `cd backend && DOTENV_CONFIG_PATH=.env node -r dotenv/config node_modules/jest/bin/jest.js --runInBand` | `Local-Implemented` | `passed-local` | 18 suites passed, 1 skipped; 403 passed, 2 skipped, 405 total | includes 23 PostgreSQL cases across publication and disposable-schema migration suites; the remaining skipped suite is the separate RLS surface |
| backend static/build | Nest/TypeScript/Prisma | compile and schema/client coherence | installed dependencies | `cd backend && npx prisma validate && npm run prisma:generate && npx eslint "src/**/*.ts" && npm run build` | `Local-Implemented` | `passed-local` | Prisma validation, lint and build exited 0 | use repo-owned versions |
| PostgreSQL real integration | relational publication/coverage/repair path | generation rollback, service-level snapshot barriers, daily proof/retention, `20x5` overlap, restart duplicate, mutable total, resumable final publication, exact legacy collision and disposable legacy upgrade | local baseline schema fixture | `TEST_DATABASE_URL=... npx jest fiscal-note-read-model.integration.spec.ts fiscal-note-read-model.migration.integration.spec.ts --runInBand` | `Local-Implemented` | `passed-local` | 23/23 passed; migrations 2/2 up to date; 20k publication remains within the 35s bound | only project PostgreSQL container was started; no stage or remote DB mutation |
| frontend unit/build | metadata/messages/download lifecycle | partial/complete notices and incomplete export | deterministic API fixtures | `cd frontend && npm run test:notas && npm run lint && npm run build` | `Local-Implemented` | `passed-local` | all three commands exited 0 | complete-zero and exact 409/422 covered |
| browser flow | actual list/export UX | partial notice disappears when covered; incomplete export downloads nothing | Vite production preview + deterministic backend fixture | Windows Chrome against source-owned `frontend/e2e/notas.mjs` | `Local-Implemented` | `passed-local` | `OK mocked fiscal/cache/privacy/session and legacy PATCH flows` | local preview processes were stopped after execution |
| incident RED + cross-layer replay | local admission, provider-contract and scoped React timer regression | no false `failed`/candidate loss on transient refusal; static incapacity has no auto-poll; 200-invalid page remains fail-closed with a safe subtype; existing public API/export shape | same-context windows within 60s, persisted checkpoint 3/4, deferred retention, prior true error, complete rolling, several viewers, synthetic invalid 200 page; no live PII | focused Jest coordinator/cache/adapter + real PostgreSQL integration + `npm run test:notas` + source-owned browser scenario, then full in-scope CI | renewed `Local-Implemented` | `planned-not-run` | no incident GREEN evidence | previous passed rows are baseline-only, not proof for `D-RM-I01..I03` |

## Runtime / Rollout Notes

- Default rollout is expand/repair/switch without deleting cache rows. If schema expansion is unnecessary, code must still handle legacy sync rows deterministically.
- Feature flags or deploy topology changes are not assumed. Stage repair runs only after the exact deployed revision and target database are attested through the DevOps handoff.
- A rollback must disable new scheduling/read switching without erasing coverage/cache metadata. No manual `UPDATE ... bootstrap_complete` is an acceptable rollback or repair.
- The earlier stage symptom was described as `rate-limited/degraded`; the five new rows contain no `SmartNotasLimiteExterno`, so current provider rate limiting is unproven. Validation still requires bounded calls and redacted aggregate logs.
- The user attested that `main@fb8d88137212bbe549707aa064cc03185a14e6db` was active throughout the `2026-10-01 10:17:48–10:18:03` incident interval. The queried environment/database has not been named, the private commit has not been independently inspected and the exact `SmartNotasContratoInvalido` validation category is unknown. No runtime repair, parser relaxation, stage smoke or promotion claim follows from revision attestation alone. Capture only status/size/validation category/correlation, never provider body, recipient fields or secrets.

## Plan Review Gate

- **Status:** `converged-findings-integrated`; R5 confirmou o desenho MVCC do horizonte e sua única lacuna de teste no caminho sem anchor foi incorporada em `VAL-RM-C17`.
- **Incident delta status:** `R3-decision-pending`; the earlier R5 result applies only to `D-RM-C01..C27`. R1/R2 findings were integrated; R3 of pushed `ad9b4e4` exposed a high-severity recovery regression in the timer rule and an undefined static-capacity projection source. Option A is proposed but not chosen; the TODO is not ready for `APROVADO` or implementation until the user validates this public-contract choice and the revised baseline is reviewed.

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

**Incident issue cards (packet preparation only; not yet freeze-backed review):**

- **Issue ID:** `OPS-RM-I01`; **severity:** high; **evidence:** `backend/src/fiscal-notes/fiscal-note-cache.service.ts:532-545,548-620` and `fiscal-rate-coordinator.ts:94-143`; four `ExportacaoFiscalOcupada` persisted rows on 2026-10-01.
  - **Why now:** `runRolling()` rotates generation/deletes candidates before `walkPages()` asks for admission; the latter persists a local refusal as `*_failed`.
  - **A (recommended):** admit before destructive state change, and defer a refused/resumable unit as pending while preserving generation/checkpoint and respecting coordinator retry eligibility. **Effort:** medium; **risk:** medium (state transitions); **blast radius:** fiscal backend; **maintenance:** low; **performance:** no extra provider calls, fewer futile retries; **elegance:** high; **structural soundness:** high.
  - **B:** leave the failed row and suppress the UI error only. **Effort:** low; **risk:** high (false persisted state); **blast radius:** API/UI; **maintenance:** high; **performance:** neutral; **elegance:** low; **structural soundness:** low.
  - **C (do nothing):** keep local refusal as `failed`. **Effort:** none; **risk:** high (non-convergent visible error); **blast radius:** all contexts/periods; **maintenance:** recurring operations; **performance:** repeated futile pumps; **elegance:** low; **structural soundness:** low.

- **Issue ID:** `OBS-RM-I02`; **severity:** high; **evidence:** `backend/src/fiscal-notes/smart-notas.adapter.ts:149-194,207-232,309-338,388-477`; 21 status-200 contract failures in the user-pasted log.
  - **Why now:** current logs do not identify body, JSON, envelope, page metadata or field rejection, and they lack safe window/page correlation; relaxing the parser now would be speculative.
  - **A (recommended):** allowlisted internal failure category plus safe query window/page/correlation and byte count when known, logged once per failed request; leave acceptance and public envelope unchanged. **Effort:** medium; **risk:** low with negative privacy tests; **blast radius:** fiscal adapter/tests; **maintenance:** low; **performance:** negligible error-only metadata; **elegance:** high; **structural soundness:** high.
  - **B:** capture raw response/provider note for manual inspection. **Effort:** low; **risk:** critical (PII/secrets retention); **blast radius:** logs/compliance; **maintenance:** high; **performance:** log-volume increase; **elegance:** low; **structural soundness:** low; **rejected:** violates the no-payload boundary.
  - **C (do nothing):** continue logging only `SmartNotasContratoInvalido`. **Effort:** none; **risk:** high (cause remains unknown); **blast radius:** both fiscal contexts; **maintenance:** repeated manual triage; **performance:** repeated failed syncs; **elegance:** low; **structural soundness:** low.

- **Issue ID:** `UX-RM-I03`; **severity:** medium; **evidence:** `fiscal-note-cache.service.ts:221-240`, `frontend/src/notas/apresentacaoFiscal.ts:6-29`, `frontend/src/notas/normalizacaoFiscal.ts:87-129`.
  - **Why now:** pending local work must not masquerade as provider failure, but a new public enum would widen the incident unnecessarily.
  - **A (recommended):** reuse `partial/idle/null` plus retry countdown for deferred work and `failed/unexpected` for genuine failure on partial coverage; add only the React timer stop for `partial/failed` with no retry deadline, preserving manual refresh and CSV gate. Complete/stale rolling keeps the established freshness UI. **Effort:** low; **risk:** low with browser cadence test; **blast radius:** backend state + one React timer + tests; **maintenance:** low; **performance:** avoids indefinite 2-second polling; **elegance:** high; **structural soundness:** high.
  - **B:** introduce a public `waiting_for_capacity` state and new React message. **Effort:** medium; **risk:** medium (contract/client drift); **blast radius:** API + React; **maintenance:** medium; **performance:** neutral; **elegance:** medium; **structural soundness:** valid only if existing states prove insufficient.
  - **C (do nothing):** retain false `failed/unexpected` after local refusal. **Effort:** none; **risk:** high; **blast radius:** finance UI/CSV readiness; **maintenance:** operational confusion; **performance:** neutral; **elegance:** low; **structural soundness:** low.

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
- [ ] Local refusal between historical windows, after page 3/4, or before rolling admission: keep candidate/coverage unchanged and retry only when eligible; never mark provider failure or leak a stale lease.
- [ ] Provider returns HTTP 200 with oversized declared/stream body, invalid JSON, unknown envelope/page or invalid recipient field: fail closed and emit one bounded category without any value, URL or payload.
- [ ] A real provider failure follows a local refusal: retain the real provider error; do not overwrite it with an invented local-failure category or claim completion without daily proof.

### Residual Unknowns / Risks

- [ ] The exact provider response subtype remains unknown despite 21 status-200 logs; it must not be inferred from `perPage=200`. The queried database environment is not explicitly named, though the incident deploy SHA is user-attested.
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
- **Latest TEACH evidence / artifact:** `audit_escalation_guard.py` returned `Overall outcome: go` on `2026-09-29`; fingerprint `ad81743d5b49`; derived critique/test-quality/final/triple-review/performance-concurrency floors remain `required`, security `recommended`, verification-debt `required`.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | state machine, API, UI, persistence and stage repair |
| `blast_radius` | `cross-stack` | NestJS + React + PostgreSQL/Prisma |
| `behavioral_change_or_bugfix` | `yes` | stage regression correction |
| `changes_public_contract` | `yes` | coverage metadata and `409 ExportacaoFiscalCoberturaIncompleta` |
| `touches_auth_or_tenant` | `no` | existing auth/roles/context isolation preserved |
| `touches_runtime_or_infra` | `yes` | in-process scheduler/startup behavior; no infrastructure files |
| `touches_tests` | `yes` | approved intent was fail-first; delivered evidence is explicitly test-after plus full regression coverage |
| `critical_user_journey` | `yes` | fiscal list/pagination/export |
| `release_or_promotion_critical` | `yes` | current stage behavior is degraded |
| `high_severity_plan_review_issue` | `yes` | `ARCH-RM-C01` and `API-RM-C02` |
| `explicit_three_lane_request` | `no` | no explicit user request |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `blocked`
- **Decision review evidence / resolution:** R1/R2 findings remain integrated. Fresh R3 architecture opinion of pushed `ad9b4e4` found `ARCH-R3-01` (medium): impossible static capacity has no authoritative source for public partial/complete projection when no sync row exists. Recommended typed coordinator capability + explicit read-time precedence is recorded as Option A above but awaits user validation, new freeze and review. Derived result: `artifacts/tmp/uninotas-incident-r3-architecture-merged.md`; no architecture approval is claimed; R5 is historical C01..C27 evidence only.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-summary`
- **Adherence review status:** `findings_integrated_pending_rerun`
- **Adherence review evidence / resolution:** the first final review found historical-seeding, resumable-candidate retention and durable-cardinality defects. These are corrected and exercised against PostgreSQL; a fresh reviewer must attest the new diff before Completed.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** big architecture correction needs a committed/pushed immutable TODO packet before independent review.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `uninotas-foundation:main`
- **Baseline commit:** `ad9b4e4961daefac48deab903668820aa744d8bf`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** prior C01..C27 baseline `9d3bf55` passed R5. Incident `af6c34a` and `96ca8de` received independent critique/architecture findings, all integrated; the second-round refinement (scoped React timer, exhaustive deferred state handling, exact retry/error precedence) is frozen and pushed at `ad9b4e4` as a TODO-only commit. Fresh review of this refined baseline remains pending.
- **Evidence / reference:** `https://github.com/unifast-tech/uninotas-foundation/commit/ad9b4e4961daefac48deab903668820aa744d8bf`; prior R5 evidence remains in its resolution ledger below.
- **Waiver authority / reference:** `n/a`
- **2026-10-01 incident delta:** `ad9b4e4` is the current pushed review baseline for I01..I03. Prior rounds are finding evidence, not approval of the refined plan; re-review, scope-drift and renewed human approval remain pending.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** any post-review change to windows, coverage, errors, repair or evidence can alter the approved risk conversation.
- **Trigger stage:** `after planning review/critique convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** guard against the new pushed baseline `ad9b4e4` returned `go`, 0 of 23 material sections changed, on 2026-10-01. The prior `96ca8de` four-section drift was resolved by the second-round finding integration and re-freeze, not waived. User validation of the new frontend timer scope remains separate.
- **Evidence / reference:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md`: `Overall outcome: go`, `Changed material sections: 0` against `ad9b4e4961daefac48deab903668820aa744d8bf` on 2026-10-01.
- **Waiver authority / reference:** `n/a`
- **2026-10-01 incident delta:** second-round findings are now in pushed `ad9b4e4`; a fresh review and renewed human approval are still required before implementation.

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** `big`, cross-stack, public contract/runtime-sensitive behavior, intentional module supersede and high-severity findings.
- **Impact signals in scope:** `cross-stack blast radius|public API|runtime scheduler|intentional module supersede|high-severity issue cards`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** this TODO, fiscal module, cache service/spec, fiscal service/types/errors and React list/API normalization files.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after baseline freeze; reviewer cannot be implementing agent`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `blocked`
- **Findings summary:** R1–R5 remain historical for C01..C27; incident R1/R2 findings are integrated. Fresh R3 critique of pushed `ad9b4e4` found `I-R3-CRIT-01` (high): stopping all failed/null timers suppresses automatic observation of a recoverable asynchronous publication, and `I-R3-CRIT-02` (medium): repeated transient refusal after the first 60-second window can return to two-second polling. The public-signal choice is pending user validation; no critique convergence or `APROVADO` is claimed.
- **Evidence / reference:** R3 derived result `artifacts/tmp/uninotas-incident-r3-critique-merged.md`; the authoritative resolution is consolidated in the incident ledger below, not in the disposable dispatch artifacts.
- **Waiver authority / reference:** `n/a`

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `I-CRIT-01` | `Integrated` | `useful` | `yes` | `project` | `n/a` | I01 separates static incapacity from transient refusal; VAL-I01 tests no-loop behavior. |
| `I-CRIT-02` | `Integrated` | `useful` | `partial` | `project` | `n/a` | I01 transition table and VAL-I01/I03 cover legacy occupied rows and persisted progress. |
| `I-CRIT-03` | `Integrated` | `useful` | `yes` | `project` | `n/a` | I03 reuses retryAfterSeconds; VAL-I03 asserts multi-viewer cadence. |
| `I-CRIT-04` | `Integrated` | `useful` | `yes` | `project` | `n/a` | I02 scopes list diagnostics, includes declared-invalid length and enriches existing event. |
| `I-R2-CRIT-01` | `Integrated` | `useful` | `yes` | `project` | `n/a` | I03 scopes one React timer condition: no automatic polling on partial/failed with null retry deadline; manual refresh remains. |
| `I-R3-CRIT-01` | `Deferred` | `useful` | `yes` | `project` | `n/a` | Option A proposes an explicit public auto-retry signal; human scope validation and re-review are required before changing I03. |
| `I-R3-CRIT-02` | `Deferred` | `useful` | `partial` | `project` | `n/a` | I01 proposal resets the persisted eligibility clock only after a new eligible admission refusal; must be frozen/re-reviewed with the selected I03 option. |

### Critique Finding Resolution Ledger

| Finding ID | Severity | Finding | Resolution in refined baseline | Status |
| --- | --- | --- | --- | --- |
| `FRM-CRIT-01` | high | Mutable canonical page writes cannot prove atomic complete-window visibility or absence. | `D-RM-C11/C12/C16/C18`; candidate generation, distinct completeness, set publication and snapshot readers; targeted PostgreSQL tests. | `Closed through R4` |
| `FRM-CRIT-02` | high | D-2 frontier, retention, rollover, gaps/overlaps and month lifecycle were underspecified. | `D-RM-C13/C15/C16/C20`; daily proof, deterministic rolling/retention/admission and snapshot-visible horizon. | `Closed except FRM-R3-03 focused refinement` |
| `FRM-CRIT-03` | high | Scheduler had no bounded priority, fairness, overlap or shutdown contract. | `D-RM-C14`; captured `D`, single pump, rolling-first, one historical window globally per pump, context rotation, sequential provider walks and shutdown admission. | `Closed through R4` |
| `FRM-CRIT-04` | high | Public `readModel` fields/states and zero-row UI behavior were not frozen. | `D-RM-C14/C16/C19` public/UI tables; truthful complete-zero, freshness, exact export `409` and horizon `422`. | `Closed through R4` |
| `FRM-CRIT-05` | medium | Tests omitted atomic failure, absence/movement/null dates, rollover, scheduler starvation and incomplete-zero UI. | Expanded `D-T01..03`, `VAL-RM-C09..17`, ordered plan and named regression interleavings; execution is classified as test-after. | `Closed except FRM-R3-03 focused refinement` |

### R2 Critique Finding Resolution Ledger

| Finding ID | Severity | Finding | Resolution in refined baseline | Status |
| --- | --- | --- | --- | --- |
| `FRM-R2-01` | high | Separate coverage/count/row statements can mix committed generations. | `D-RM-C16/C20`; snapshot-visible horizon and one PostgreSQL snapshot for list/export; barrier tests. | `Closed except FRM-R3-03 focused refinement` |
| `FRM-R2-02` | high | Retention horizon conflicts with unrestricted valid date intervals. | `D-RM-C16/C20`; exact local horizon, snapshot-visible admission, `422` bounds and React tests. | `Closed except FRM-R3-03 focused refinement` |
| `FRM-R2-03` | high | Rolling/frontier/compaction metadata can overlap without deterministic supersession. | `D-RM-C15`; canonical context/date coverage ledger; operational overlaps do not authorize reads. | `Closed through R4` |
| `FRM-R2-04` | medium | 20.000-row promotion could become thousands of statements/unbounded locks. | `D-RM-C17`; set-based parameterized publication, indexes and fixed timeouts with rollback/backoff. | `Closed through R4` |
| `FRM-R2-05` | medium | Tests did not force reader/publication races, horizon boundaries or metadata failures. | `VAL-RM-C12..17`, `D-T01..03` and named PostgreSQL/browser/concurrency interleavings. | `Closed except FRM-R3-03 focused refinement` |

### R3 Critique Finding Resolution Ledger

| Finding ID | Severity | Finding | Resolution in refined baseline | Status |
| --- | --- | --- | --- | --- |
| `FRM-R3-01` | high | Duplicate provider IDs separated by checkpoint/restart can collapse and falsely satisfy completion. | `D-RM-C18`; durable raw observation count; exact candidate/raw/expected equality and page invariants; PostgreSQL restart regression `VAL-RM-C15`. | `Closed by R4` |
| `FRM-R3-02` | high | Preserved freshness fields lack truthful interval derivation after sync compaction. | `D-RM-C19`; durable daily `published_at`; exact conservative aggregates and `freshnessState`; historical snapshots have no unsupported retry; tests `VAL-RM-C16`. | `Closed by R4` |
| `FRM-R3-03` | medium | Application-captured/time-derived `D` can disagree with the MVCC snapshot during midnight retention. | `D-RM-C20`; snapshot-visible retained-horizon row advances in the same commit as pruning; anchored/no-anchor before/after snapshot barriers in `VAL-RM-C17`. | `Closed by R5; test refinement integrated` |

### R4 Critique Finding Resolution Ledger

| Finding ID | Severity | Finding | Resolution in refined baseline | Status |
| --- | --- | --- | --- | --- |
| `FRM-R3-03` | medium | `transaction_timestamp()` is fixed at transaction start, not necessarily the first repeatable-read snapshot. | `D-RM-C20` persists `{horizon_date, retained_from, retained_through}` and advances it atomically with pruning; requests read anchor/rows in one MVCC snapshot; `VAL-RM-C17` forces anchored and first-no-anchor commit orders. | `Closed by R5` |

### R5 Critique Finding Resolution Ledger

| Finding ID | Severity | Finding | Resolution in refined baseline | Status |
| --- | --- | --- | --- | --- |
| `FRM-R5-01` | medium | The provisional no-anchor race lacked an explicit falsifying test. | `VAL-RM-C17(b)` now requires no context-state, provisional first snapshot, concurrent first-anchor creation+pruning, continued old-snapshot visibility and a subsequent anchor-visible request. | `Integrated` |

### 2026-10-01 Incident Planning Review Resolution Ledger

The critique and architecture opinion were fresh no-context reviews of the pushed `af6c34a` package. Their positions were mixed on performance, structural soundness and operational fit; all material findings are integrated below. These are planning findings, not implementation evidence or an approval waiver.

| Finding ID | Severity | Finding | Resolution in refined I01..I03 plan | Status |
| --- | --- | --- | --- | --- |
| `I-CRIT-01`, `ARCH-I01` | high | Static configuration may make export permanently impossible while returning occupied. | `D-RM-I01` separates impossible capacity from transient admission, records a visible operational stop and forbids futile retries; `VAL-RM-I01` covers both impossible configurations. | `Integrated` |
| `I-CRIT-02`, `ARCH-I02` | high/medium | Legacy occupied failures, checkpointed generations and true prior errors need explicit transitions. | I01 transition table preserves artifacts, projects legacy occupied rows compatibly, resumes checkpoints and never erases a genuine provider error; PostgreSQL/API fixtures in `VAL-RM-I01/I03`. | `Integrated` |
| `I-CRIT-03`, `PERF-I03` | medium | Partial/idle/null without retry delay causes two-second viewer polls and pump nudges. | I01/I03 use persisted conservative 60-second eligibility and existing public `retryAfterSeconds`; backend gates nudges and `VAL-RM-I03` asserts multi-viewer cadence. | `Integrated` |
| `I-CRIT-04`, `OBS-I04` | medium | Malformed declared length has no truthful category; a second log would duplicate the existing event; scope of shared adapter is unclear. | I02 scopes to `list`, adds `body_declared_invalid`, maps every in-scope branch and enriches only the existing final event; `VAL-RM-I02` adds negative privacy/cardinality cases. | `Integrated` |
| `I-R2-CRIT-01` | high | Permanent capacity fault would still cause React's 2-second automatic list/pump loop. | I03 includes the minimal timer stop for `partial/failed` with null retry deadline and keeps manual refresh; `VAL-RM-I03` tests several viewers beyond 60 seconds. | `Integrated` |
| `ARCH-R2-01` | high | Deferred states could be omitted from pump, seeding, demand, moved-note publication and retention. | I01 adds a named state-enumerator/retention inventory; `VAL-RM-I01` forces deferred checkpoint through restart and retained-horizon advance. | `Integrated` |
| `ARCH-R2-02` | medium | Complete/stale rolling has different public failure semantics from incomplete coverage. | I03 explicitly keeps `complete/idle` and existing stale-freshness/manual refresh; operational fault remains in existing metadata and sanitized logs, not a new banner. | `Integrated` |
| `ARCH-R2-03` | medium | Bootstrap currently clears a prior error before admission. | I01 now places admission before every bootstrap/rolling error/state/generation mutation and tests failed-checkpoint then local refusal. | `Integrated` |
| `ARCH-R2-04` | medium | Automatic update timestamp as eligibility marker could drift and reorder true errors. | I01 allows only explicit deferred transition to set its persisted clock; pending reads/seeding/retention never reset it, and true failed row/error/timestamp remain untouched by local refusal. | `Integrated` |
| `I-R3-CRIT-01` | high | Terminal timer stop also hides recoverable background publication after the response snapshot. | Option A proposes a typed static-capacity signal + public `autoRetry` boolean; awaiting human scope validation and fresh review. | `Deferred—approval pending` |
| `I-R3-CRIT-02` | medium | A long-held lease makes the first deferred timestamp expire and reopens 2-second polling. | Proposed repeat-deferral clock renewal only after an eligible refusal, with multi-window test; not frozen/approved. | `Deferred—approval pending` |
| `ARCH-R3-01` | medium | Static-capacity fault has no authoritative projection source when a new rolling window has no sync row. | Option A proposes read-only coordinator capability and explicit error precedence with no sync-row/generation mutation; awaiting human validation and review. | `Deferred—approval pending` |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** the correction depends on exact checkpoint, error-map and schema capabilities observed in code.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** live code assumptions including `A-RM-C01/C02` and incident `A-RM-I01`; runtime-only subtype/deploy unknowns are separately recorded.
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** deterministic guard returned `go`/`no_material_findings` on 2026-10-01. Direct inspection confirms `startExport()` has both impossible static capacity and transient lease/cooldown branches, `walkPages()` currently writes occupied as failed, and the React pending timer uses `retryAfterSeconds`; the refined plan no longer assumes cooldown was the sole incident cause. The guard's machine-reported live count is 2, so its result does not independently certify the unresolved runtime configuration or provider-body subtype.
- **Evidence / reference:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/features/TODO-uninotas-fiscal-note-read-model.md` returned `Overall outcome: go` and `Live assumptions checked: 2` on 2026-10-01; cited code paths inspected directly.
- **Waiver authority / reference:** `n/a`

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas API | feeds historical/rolling windows | `list contract rejection observed; exact subtype unknown` | `2026-10-01` | 21 user-pasted `list` logs have HTTP 200 with `SmartNotasContratoInvalido`; earlier `429/503` observation is historical | preserve bounded pacing; add sanitized category before any parser/limit change |
| Railway Stage revision | required for exact smoke and sync-row diagnosis | `stale/unknown for corrective revision` | `2026-09-29` | existing dependency register predates this correction | DevOps must attest exact `branch@sha` before evidence |
| Stage PostgreSQL read model | determines legacy repair path | `unknown` | `2026-09-29` | local `.env` DB had zero sync/cache rows | collect only redacted aggregates after target attestation; no blind mutation |

## Rules Acknowledgement / Ingestion

- **Current status:** `ingested for C23..C27 on 2026-09-30`; the NestJS, Prisma, PostgreSQL, package-first, test-creation and TODO-driven rules/workflows were reloaded before implementation.

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
| `delphi-ai/skills/bug-fix-evidence-loop/SKILL.md` | stage regression and missing immutable-total test coverage | evidence-first diagnosis; approved fail-first intent, with the realized variance recorded as test-after | solution-first patching | ingested; no RED artifact is claimed |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | tests must define moving-total/coverage behavior | effective assertions across unit/integration/browser layers | implementation-shaped or weak tests | required during regression execution; realized evidence is test-after |
| `delphi-ai/skills/test-orchestration-suite/SKILL.md` | full stack-aware verification is delivery-critical | targeted diagnostics plus full CI-equivalent suites | treating focused pass as delivery proof | required before delivery |
| `delphi-ai/skills/frontend-race-condition-validation/SKILL.md` | background refresh/export UI lifecycle remains async | stale-result/abort/download ownership | late warning/download effects | required if React async path changes |
| `delphi-ai/skills/rule-docker-shared-foundation-docs-sync-model-decision/SKILL.md` | canonical module conflicts with the local-export implementation | module/TODO/API vocabulary in lockstep | closing with TODO-only truth | required for module consolidation |

## Corrective Implementation Evidence — Current Working Tree

- `backend/prisma/schema.prisma` and `backend/prisma/migrations/20260929153000_fiscal_read_model_generations_coverage/` add candidate generations, raw-observation accounting, daily coverage and the context horizon anchor without deleting the canonical cache.
- `backend/src/fiscal-notes/fiscal-note-cache.service.ts` implements one non-overlapping pump, rolling-first reconciliation for both contexts, globally round-robin historical progress, isolated candidates, durable equality checks, atomic set-based publication, exact absence and movement repair.
- `backend/src/fiscal-notes/fiscal-notes.service.ts` keeps ordinary list/export on the local read model, uses one `REPEATABLE READ` snapshot for admission/coverage/count/data, returns exact `409` for incomplete export and `422` outside the retained horizon, and preserves provider ownership for detail, documents and `documento`-filtered reads.
- `frontend/src/notas/apresentacaoFiscal.ts`, `frontend/src/notas/normalizacaoFiscal.ts` and `frontend/src/paginas/ListaNotas.tsx` derive one presentation state for complete, partial, stale, failed and empty results; complete-zero export remains enabled while partial export is blocked.
- Source-owned backend and browser fixtures cover partial-zero, partial rows with usable pagination, stale/failure copy, exact `409`, exact `422` with date reset, detail/documents and complete-zero `204` export.
- `backend/prisma/migrations/20260930130000_fiscal_note_complete_export_projection/` adds nullable recipient document/e-mail/city/state/country columns and versions coverage proofs so pre-change coverage cannot release a falsely complete CSV; existing rows stay readable while ordinary synchronization replaces version-1 proof with version 2.
- `smart-notas.adapter`, the candidate/cache publisher and `fiscal-csv.serializer` now carry the complete allowlisted `GET /notas` projection. Public list JSON remains the existing 17-field allowlist and detail/PDF/XML remain provider-backed.
- Product commit `6f48e60c5c0690a02f9ca0dbed8a6d31e2761475` was pushed to `MonitorNotes/release/uninotas` after explicit authorization. No merge, deploy, provider mutation, Railway change or remote database write was performed by Delphi.

## Corrective Validation Evidence — Current Working Tree

| Check | Result | Evidence |
| --- | --- | --- |
| Backend full suite | passed locally with PostgreSQL enabled | `TEST_DATABASE_URL` + `jest --runInBand` — 18 suites passed, 1 skipped; 403 tests passed, 2 skipped, 405 total |
| Backend static/build/schema | passed locally | Prisma validate/generate, migration status, ESLint and Nest build exited 0; 2/2 migrations applied |
| Frontend contract/lint/build | passed locally | `npm run test:notas`; `npm run lint`; `npm run build` |
| Browser flow | passed locally | Windows Chrome against Vite production preview: `OK mocked fiscal/cache/privacy/session and legacy PATCH flows` |
| Diff hygiene | passed locally | `git diff --check` |
| TODO diff expectation guard | passed / `go` | after authorized artifact pruning and durable evidence consolidation, the guard observed exactly 24 changes across MonitorNotes and uninotas-foundation, all 24 classified, with zero forbidden or unclassified paths. |
| Independent architecture review | first review findings integrated; rerun pending | corrected incomplete historical seeding, retention of resumable failed candidates and durable raw-before-dedupe semantics; new review must attest the resulting diff |
| Local PostgreSQL migration | passed | existing baseline schema was preserved; first migration was safely baselined, second migration deployed, and `prisma migrate status` reports up to date |
| PostgreSQL integration specs | passed | 23/23 cases across publication and disposable-schema migration suites: atomic publication/rollback, daily proof, FK/unique, 20k rows, BCI `20x5`, anchored-list and no-anchor-export C20 barriers, movement repair, interrupted historical reconciliation, exact legacy-window recovery, failed-checkpoint/final-publication resume, mutable-total cleanup with projection preservation, restart duplicate cardinality, invalid membership, superseded generation and legacy upgrade preservation |
| PostgreSQL plan/load/lock | passed locally | 20k publication 1,153 ms; page 2.735 ms; export SQL 26.538 ms; coverage 0.157 ms; zero waiting locks after rollback; EPS/BCI `pcv-1` artifacts hash-valid |
| Test-quality heuristic | passed (`low`); independent findings integrated; rerun pending | obsolete seven-test `describe.skip` block removed; real regressions now cover `walkPages` total mutation, restart duplicate, resumable failure, invalid membership, superseded generation and disposable legacy upgrade; no bypass/support-route/auth-shortcut remains |
| Security adversarial review | passed with no material finding | JWT/role guard, context scoping, parameterized production SQL, summary PII allowlist, CSV formula neutralization and sanitized logs reviewed; unsafe SQL is confined to a controlled integration-test trigger fixture |
| Foundation deterministic validator | blocked by external structural drift | current validator reports missing identity-ledger binding for a pre-existing `origin:new` transition plus frozen lifecycle/publication-manifest mismatches; the registry, ledger and manifest were not changed by this TODO |
| Complete-export focused regressions | passed locally | 5 suites passed; 163 passed, 1 skipped, 164 total; exact 22-column CSV, recipient null/text/formula handling, adapter mapping, unchanged 17-field public list and projection-version behavior covered |
| Complete-export static/build/schema | passed locally | Prisma format/validate/generate, Nest build, ESLint and `git diff --check` exited 0 |
| Backend suite excluding PostgreSQL integration files | passed locally | 16 suites passed, 1 skipped; 385 passed, 2 skipped, 387 total |
| Complete-export PostgreSQL integration | blocked by local infrastructure | full run reached `localhost:55432` and failed only because the configured PostgreSQL was stopped; Docker was intentionally not restarted after the user's resource-usage request |

## Historical Implementation Evidence — Delivered Baseline

- `backend/prisma/schema.prisma` and migration `20260929120000_fiscal_note_read_model` were reused without a new schema change; their compound identity and workload indexes already support the previously approved change.
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

## Historical Closeout Status — Superseded by Corrective Change

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
| `DOD-RM-03` | `Definition of Done` | Migration state, builds, lint, tests and indexed access path pass. | CI-equivalent | commands and results in Validation Evidence and local matrix | local | `passed` | no new migration was required for that prior change |
| `VAL-RM-01` | `Validation` | Backend full regression suite. | command | `npx jest --runInBand`: 16 passed suites, 364 passed tests, 2 expected skips | Node local | `passed` | includes detail/documents regressions |
| `VAL-RM-02` | `Validation` | Backend static, build and Prisma checks. | command | ESLint, Nest build, Prisma validate/generate/status all exit 0 | Node/PostgreSQL local | `passed` | schema is up to date |
| `VAL-RM-03` | `Validation` | Frontend parser, lint and production build. | command | `npm run test:notas`; `npm run lint`; `npm run build` | React/Vite local | `passed` | metadata malformed-shape rejection covered |
| `VAL-RM-04` | `Validation` | Bounded local export and indexed query path. | performance | 20,000 rows, zero provider calls, 55 ms harness; local PostgreSQL `EXPLAIN` | Node/PostgreSQL local | `passed` | HTTP stage p95/p99 deferred until deployment |
| `VAL-RM-05` | `Validation` | Security/privacy boundary remains allowlisted and authenticated after the approved CSV expansion. | manual adversarial review | diff review: no raw payload/PDF/XML URL or secret persistence; only normalized `GET /notas` fields enter candidate/cache and the authenticated CSV; no `logs` writes | local | `pending` | independent review of the expanded PII projection remains required |

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

### Frozen Decision Adherence Matrix

| Decision ID | Implementation / Evidence | Status | Residual |
| --- | --- | --- | --- |
| `D-RM-C01` | historical range ends at captured `D-2`; month-clipped seeding and PostgreSQL reconciliation fixture | `adherent-local` | stage calendar observation pending |
| `D-RM-C02` | independent durable sync rows/checkpoints per canonical window | `adherent-local` | explicit monthly compaction fixture remains debt |
| `D-RM-C03` | pump reconciles both rolling contexts before one historical unit | `adherent-local` | single-replica runtime only |
| `D-RM-C04` | ordinary list reads one local snapshot and only nudges background work | `adherent-local` | stage latency/RLS pending |
| `D-RM-C05` | daily coverage ledger computes exact requested interval state | `adherent-local` | none locally known |
| `D-RM-C06` | incomplete export throws exact 409 before cache row query | `adherent-local` | stronger browser downloader oracle is P3 debt |
| `D-RM-C07` | local sync/coverage errors remain distinct from provider-operation errors | `adherent-local` | stage copy observation pending |
| `D-RM-C08` | additive migration preserves cache and retires legacy syncs in disposable schema | `adherent-local` | stage legacy aggregates pending |
| `D-RM-C09` | detail/PDF/XML/document-filter paths remain provider-backed; public JSON summary remains unchanged while C23..C27 govern the internal Finance CSV projection | `adherent-local` | live provider smoke pending |
| `D-RM-C10` | existing Nest process/scheduler and one-replica assumption retained | `adherent-local` | horizontal scaling remains forbidden without new design |
| `D-RM-C11` | isolated generation plus bounded atomic publication/rollback | `adherent-local` | stage lock pressure pending |
| `D-RM-C12` | exact absence, movement repair and invalid membership regressions | `adherent-local` | none locally known |
| `D-RM-C13` | canonical months are always reconciled; post-anchor frontier uses one-day units | `adherent-local` | explicit midnight frontier fixture remains debt |
| `D-RM-C14` | coalesced rolling-first, round-robin pump and frozen public state fields | `adherent-local` | failed/historical UI action matrix remains partial |
| `D-RM-C15` | one unique context/date proof per published day, including zero | `adherent-local` | none locally known |
| `D-RM-C16` | DB-clock admission and one `REPEATABLE READ` request snapshot | `adherent-local` | none locally known |
| `D-RM-C17` | parameterized set SQL with lock/statement/transaction limits and indexes | `adherent-local` | RLS/stage capacity pending |
| `D-RM-C18` | checkpoint/raw count is updated before candidate upserts; restart duplicate proves raw 2/candidate 1 | `adherent-local` | none locally known |
| `D-RM-C19` | daily `published_at` derives exact interval freshness states | `adherent-local-partial-ui` | browser action presence/absence oracle remains P3 debt |
| `D-RM-C20` | context horizon advances with pruning; anchored/no-anchor MVCC barriers pass | `adherent-local` | stage rollover observation pending |
| `D-RM-C21` | bounded exact-demand coalescing, cross-context alternation, rolling-first and one background unit after three demand units | `adherent-local` | single-replica runtime smoke pending |
| `D-RM-C22` | yesterday/today default, lifecycle-cancelled partial polling and automatic CSV enablement | `adherent-local` | stage browser smoke pending |
| `D-RM-C23` | adapter, candidates and canonical cache carry every allowlisted `GET /notas` field while public list JSON remains unchanged | `adherent-local-static-unit` | real PostgreSQL publication pending |
| `D-RM-C24` | serializer emits the frozen 22-column Finance CSV with null/text/formula handling | `adherent-local` | stage download smoke pending |
| `D-RM-C25` | PII remains behind existing authenticated reader roles, private/no-store transport and sanitized observability | `adherent-local` | independent security rerun pending |
| `D-RM-C26` | forward-only migration adds nullable recipient columns and versions old/new daily coverage as 1/2 | `adherent-local-static` | disposable PostgreSQL migration execution pending |
| `D-RM-C27` | export uses list projection only; detail/PDF/XML paths and tests remain provider-backed | `adherent-local` | live provider smoke pending |

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-RM-C01` | `Definition of Done` | month-clipped history through D-2, canonical daily proof, local restart, stored rows preserved | test+database | cache specs + PostgreSQL integration spec | local | `passed-local` | real PostgreSQL publication, empty proof, rollback and repair cases pass |
| `DOD-RM-C02` | `Definition of Done` | rolling D-1..D independent every 15 minutes | unit+scheduler | cache spec and scheduler wiring assertion | local | `passed-local` | runs while history is incomplete; PostgreSQL overlap proof remains under C08 |
| `DOD-RM-C03` | `Definition of Done` | list never waits provider and handles complete/partial/empty | integration+browser | service specs + source-owned browser flow | local/browser | `passed-local` | provider remains uncalled on ordinary local path |
| `DOD-RM-C04` | `Definition of Done` | covered DB export; incomplete exact 409 and no CSV | integration+browser | service/exception specs + browser download assertion | local/browser | `passed-local` | includes complete-zero `204`, partial `409` and outside-horizon `422` |
| `DOD-RM-C05` | `Definition of Done` | non-destructive legacy repair | migration+database | additive migration and baseline repair fixture | local/stage | `passed-local` | local baseline retained pre-existing tables and rows; stage execution remains under C07 |
| `DOD-RM-C06` | `Definition of Done` | truthful API/UI synchronization errors | contract+browser | exception filter/service/frontend specs | local/browser | `passed-local` | sanitized sync cause is distinct from provider-operation failure |
| `DOD-RM-C07` | `Definition of Done` | provider detail/docs/document filter and context isolation preserved | regression | full fiscal suites | local | `passed-local` | PII expands only the authenticated internal CSV projection under C23..C27; detail ownership is unchanged |
| `DOD-RM-C08` | `Definition of Done` | module/tests/build/DB/PCV/stage evidence coherent | review+runtime | gates and artifacts below | local/stage | `partial` | local PostgreSQL EPS/BCI pass; independent gates, RLS and stage evidence remain open |
| `DOD-RM-C09` | `Definition of Done` | failed/incomplete generation never mutates visible cache/coverage | PostgreSQL transaction | late-failure and mismatch regressions | local | `passed-local` | rollback preserves prior projection and proof |
| `DOD-RM-C10` | `Definition of Done` | gap-free frontier and fair non-overlapping scheduler | unit+PostgreSQL | seed reconciliation and pump specs | local | `passed-local` | partial legacy metadata cannot suppress missing canonical month units |
| `DOD-RM-C11` | `Definition of Done` | public complete/partial/zero/sync/failure contract | contract+browser | backend/frontend fixtures | local/browser | `passed-local` | UI action-matrix strengthening remains test-quality debt |
| `DOD-RM-C12` | `Definition of Done` | one-snapshot coverage/count/rows | PostgreSQL barriers | anchored and no-anchor interleavings | local | `passed-local` | list and export retain coherent MVCC views |
| `DOD-RM-C13` | `Definition of Done` | exact retained horizon and pruned proof | boundary+database | admission and retention specs | local | `passed-local` | stage rollover observation remains runtime evidence |
| `DOD-RM-C14` | `Definition of Done` | bounded set publication for zero/small/20k with rollback | load+database | EPS and publication specs | local | `passed-local` | 20k publication remained below 35s transaction bound |
| `DOD-RM-C15` | `Definition of Done` | duplicate across restart cannot publish | PostgreSQL restart regression | durable raw/candidate inequality | local | `passed-local` | candidate count 1 versus raw observed 2 rejects publication |
| `DOD-RM-C16` | `Definition of Done` | interval freshness is truthful | unit+browser | freshness/presentation fixtures | local/browser | `partial` | backend states pass; explicit failed/historical browser action matrix remains to strengthen |
| `DOD-RM-C17` | `Definition of Done` | retained horizon is snapshot-visible | PostgreSQL barriers | context-state race regressions | local | `passed-local` | anchored and first-anchor cases pass |
| `DOD-RM-C18` | `Definition of Done` | demanded intervals are deduplicated, fair and bounded without background starvation | unit | cache-service demand/pump regressions | local | `passed-local` | exact repeats coalesce; contexts alternate; fourth opportunity is background |
| `DOD-RM-C19` | `Definition of Done` | default yesterday/today and automatic complete-only export convergence | unit+browser+race | parser, mocked browser transition and required race probes | local/browser | `passed-local` | partial response revalidates without click and enables CSV after complete response |
| `DOD-RM-C20` | `Definition of Done` | complete allowlisted list projection and CSV without per-row detail or PII logs | adapter+serializer+contract | focused fiscal suites | local | `passed-local-unit` | exact 22 columns, leading-zero document, formula protection, nulls and unchanged 17-field public summary pass; real DB publication remains under C21 |
| `DOD-RM-C21` | `Definition of Done` | additive nullable migration preserves legacy rows and ordinary sync backfills fields | migration+database | disposable-schema migration spec plus publication integration spec | local PostgreSQL | `blocked-infrastructure` | test and SQL are implemented; configured `localhost:55432` PostgreSQL is stopped |
| `VAL-RM-C01` | `Validation Steps` | regression set for mutable total/restart/coverage/error | test | focused Jest and real PostgreSQL regressions | local | `passed-local-test-after` | causal failures were observed during implementation, but no immutable pre-fix RED artifact was preserved; do not claim formal RED/GREEN evidence |
| `VAL-RM-C02` | `Validation Steps` | full suites/static/build/Prisma | CI-equivalent | commands in current Local CI matrix | local | `passed-local` | backend 403 passed/2 skipped/405 total; frontend checks green; Prisma status/validate/generate green |
| `VAL-RM-C03` | `Validation Steps` | real PostgreSQL coverage/repair/plans | database | disposable legacy migration plus 22 publication cases and EPS artifact | local PostgreSQL | `passed-local` | migration semantics, daily coverage, legacy collision, final-checkpoint retry, mutable-total cleanup, restart and representative plans executed without remote DB access |
| `VAL-RM-C04` | `Validation Steps` | bootstrap/rolling/list/export concurrency | concurrency | unit evidence plus BCI/PostgreSQL artifact | local | `passed-local` | `20x5` overlapping publications and both service-level reader/retention barriers pass |
| `VAL-RM-C05` | `Validation Steps` | bounded local performance and zero upstream covered export | performance | 20,000-row test plus EXPLAIN/lock artifact | local | `passed-local` | 1,177 ms latest publication, indexed page/export plans and zero waiting locks; stage RLS remains separate |
| `VAL-RM-C06` | `Validation Steps` | React warning/progress/download behavior | browser | Windows Chrome + production preview | browser | `passed-local` | exact mocked source-owned flow passed |
| `VAL-RM-C07` | `Validation Steps` | revision-attested stage repair and smoke | runtime | redacted aggregate query + authenticated API smoke | Railway Stage | `planned` | DevOps handoff; bounded provider traffic |
| `VAL-RM-C08` | `Validation Steps` | deterministic/review/consolidation gates | review | guard outputs, no-context audits and module diff | local/Foundation | `planned` | all blockers resolved before delivery |
| `VAL-RM-C09` | `Validation Steps` | late failure cannot leak candidate publication | PostgreSQL fault injection | coverage-trigger rollback fixture | local | `passed-local` | canonical cache/coverage remain unchanged and resumable candidate survives |
| `VAL-RM-C10` | `Validation Steps` | absence/movement/invalid membership/empty/restart/supersession | PostgreSQL regressions | publication integration suite | local | `partial` | named cases pass; explicit monthly-compaction fixture remains absent |
| `VAL-RM-C11` | `Validation Steps` | pump concurrency/fairness/shutdown/cooldown | unit | cache-service pump specs | local | `passed-local` | non-overlap, rolling priority, alternation and shutdown pass |
| `VAL-RM-C12` | `Validation Steps` | publication/retention reader races | PostgreSQL barriers | list/export repeatable-read cases | local | `passed-local` | forced commits do not mix generations |
| `VAL-RM-C13` | `Validation Steps` | horizon/document/retention/frontier boundaries | unit+database+browser | admission and provider-preservation suites | local | `partial` | exact D-366/D and provider document path pass; explicit midnight frontier fixture remains open |
| `VAL-RM-C14` | `Validation Steps` | plans/statements/locks/latency | EPS+PostgreSQL | pcv EPS artifact and 20k benchmark | local | `passed-local` | bounded transaction and zero residual waiting locks |
| `VAL-RM-C15` | `Validation Steps` | restart duplicate creates durable inequality | PostgreSQL | restart staging/publication regression | local | `passed-local` | raw 2, candidate 1, no canonical rows/proofs published |
| `VAL-RM-C16` | `Validation Steps` | complete-zero/historical/current/stale/failed UI states | unit+browser | parser/presentation/browser fixtures | local/browser | `partial` | state derivation passes; failed and historical action presence/absence needs stronger browser oracle |
| `VAL-RM-C17` | `Validation Steps` | anchored/no-anchor retained-horizon MVCC races | PostgreSQL | two forced-interleaving cases | local | `passed-local` | old snapshot remains coherent and new request sees advanced anchor |
| `VAL-RM-C18` | `Validation Steps` | demand coalescing, interval priority, fairness and background reservation | Jest | focused cache spec plus backend suite excluding stopped PostgreSQL fixture | local | `passed-local` | focused cache 23/23; executable non-DB suite 385 passed/2 skipped |
| `VAL-RM-C19` | `Validation Steps` | yesterday/today default, automatic polling, obsolete-cycle cancellation and CSV enablement | unit+browser+race | `test:notas`, `e2e:notas`, `test:notas:race`, lint/build | local/browser | `passed-local` | browser observed partial→complete with at least two list requests and no click; race bursts 20 passed |
| `VAL-RM-C20` | `Validation Steps` | adapter/serializer/cache/HTTP complete-export regressions | Jest | five focused fiscal suites | local | `passed-local` | 163 passed, 1 skipped; no detail calls introduced and exact CSV contract passes |
| `VAL-RM-C21` | `Validation Steps` | Prisma validation/generation plus empty/baseline PostgreSQL migration | schema+database | Prisma validate/generate and migration integration spec | local PostgreSQL | `partial` | Prisma validate/generate pass; database execution is blocked only by stopped `localhost:55432` |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| corrective implementation diff + frozen decisions + CI evidence | P1/P2 state-machine, API, schema, UI and evidence failures | `no-material-findings` | fresh R5 test-quality and R3 final reviews plus current local CI evidence | exact legacy collision, final-checkpoint retry, mutable-total cleanup and local export audit findings integrated; no unresolved local P1/P2 | PostgreSQL, diff expectation and independent-review evidence are complete locally; scope-drift, cutover and stage gates still block delivery |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| derived read model / P-6 | PostgreSQL treated as fiscal authority or manual completion | `passed-local` | module/code diff and provider-preservation regressions | none found locally | Smart Notas remains authority; local rows are rebuildable summaries |
| non-blocking local reads | hidden `await`/provider traversal in list/export | `passed-local` | service call-count and incomplete-export negative oracles | none found locally | covered ordinary list/export perform zero provider calls |
| interval coverage | global boolean or count-only proof | `passed-local` | daily-proof, complete-zero and snapshot integration tests | none found locally | exact context/day coverage is required |
| truthful errors | local coverage mapped to provider outage | `passed-local` | exception filter, service and UI contract tests | none found locally | incomplete/out-of-horizon/provider errors remain distinct |
| test quality | immutable-total-only fixtures or weakened assertions | `findings-integrated-pending-rerun` | independent audit plus mutable-total/restart PostgreSQL regressions | prior P2 gaps integrated | fresh no-context test-quality verdict pending |

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** persistence/query and API error/metadata paths change around fiscal data, while auth, permissions and stored PII are intentionally unchanged.
- **Attack surface in scope:** authenticated list/export endpoints, query bounds, CSV generation, sync metadata/log redaction, context isolation and database repair.
- **Attack simulation decision:** `required`
- **Review evidence:** bounded `security-adversarial-review` executed on `2026-09-30` against the prior name-only projection; no material finding. JWT and role guards remain global/class-scoped; every local read/write is context-scoped; production raw SQL uses tagged parameter binding with explicit UUID casts; public summary still excludes recipient document/e-mail/location, while candidates/cache now retain these allowlisted fields solely for the authenticated Finance CSV under C23..C27; logs expose only actor, operation, context, outcome and correlation ID; CSV formula neutralization tests pass. `$executeRawUnsafe` is confined to a local integration-test trigger name derived from an internally generated alphanumeric context. An independent security rerun for the expanded projection remains pending.
- **Residual security risk:** stage diagnostics could leak PII if unredacted; stage evidence remains restricted to counts, dates, states, page progress and sanitized codes. All authenticated financial roles intentionally see both fiscal contexts per prior human decision, so context selection is data partitioning rather than per-user tenant authorization.
- **Incident diagnostic security delta (prepared-pre-freeze):** the proposed event is emitted only on contract rejection and contains a fixed category/failure-kind vocabulary, allowlisted field **name**, context/window/page/correlation, numeric byte count when known, status and duration. Logging request URL, `documento`, `idCompra`, response bytes/body, record values, raw exceptions or credentials is forbidden. A negative log-content test and bounded one-event assertion are mandatory before release; the prior name-only security review is not incident approval.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** list/export query paths, scheduler concurrency, batch upserts and provider quota behavior all change.
- **Current delivery stage at review time:** `Local-Implemented / Evidence-Blocked`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `high` | `EPS-QUERY-SHAPE-CHANGED` | `before_local_implemented` | `EPS-E2` | `passed` | representative local PostgreSQL plan/load evidence passed; stage capacity remains RLS-owned | `none` |
| `FRC` | `frontend-race-condition-validation` | `required` | `medium` | `FRC-STALE-RESPONSE` | `before_local_implemented` | `FRC-E2` | `passed` | browser and source-owned race fixtures passed | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `required` | `high` | `BCI-JOB-WEBHOOK-API-OVERLAP` | `before_local_implemented` | `BCI-E3` | `passed` | real PostgreSQL `20x5`, rollback and reader-retention barriers passed | `none` |
| `RLS` | `runtime-load-stress-validation` | `required` | `high` | `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED` | `before_production_ready` | `RLS-E2` | `pending` | real stage quota/latency remains unknown | `U-RUNTIME-PRESSURE-UNKNOWN` |

**Incident delta (approval pending):** `D-RM-I01` changes admission/checkpoint concurrency and requires a fresh BCI proof for two contexts, same-actor cooldown, refused bootstrap/rolling generation, deferred retention and eventual bounded retry. `D-RM-I02` enriches only one existing error-path event; profile its bounded cost and log cardinality without increasing provider call rate. `D-RM-I03` includes one React timer condition to stop indefinite 2-second polling on terminal partial failure; browser race/cadence evidence is required. Earlier `passed` lane rows certify the C01..C27 baseline only; they are not evidence for I01..I03. RLS remains pending until an authorized deployment.

### EPS
- **Trigger rationale:** list/export query and coverage shape changes materially.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** `evidence_type=explain-analyze-buffers-and-benchmark`; `environment_id=local-wsl-postgresql16-principal-checkout`; `run_id=fiscal-read-model-eps-20260930T020927Z`; `artifact_uri=artifacts/tmp/uninotas-fiscal-read-model/pcv/eps.json`; `artifact_schema_version=pcv-1`; `artifact_sha256=2e0a535125263ffe778fbee81ac87e7c3408b04da9922c6cedb9d0ae4b3b1391`; `sample_profile_id=EPS-SP-STRONG`; `acceptance_rule_id=EPS-A2`; `result_summary=passed: indexed bounded page/export at 20k, bounded full-set scans, no waiting locks or exact-lookup anti-pattern`; `reviewer_id=codex-assurance-tester-quality`.

### FRC
- **Trigger rationale:** asynchronous list refresh/export error/download state is user-visible.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** `evidence_type=deterministic-ui-race-and-browser-fixtures`; `environment_id=local-principal-checkout`; `run_id=fiscal-read-model-frc-20260930T110715Z`; `artifact_uri=uninotas-foundation/artifacts/tmp/uninotas-fiscal-read-model/pcv/frc.json`; `artifact_schema_version=pcv-1`; `artifact_sha256=437c8c676f5a3d18596af0bbcf0aa8dee535ab0125d8b7d44bf4084011c25fc9`; `sample_profile_id=FRC-SP-M`; `acceptance_rule_id=FRC-A2`; `result_summary=passed: 27/27 burst probes plus parser, cache TTL/dedupe/late-response/LRU, export abort/download and intercepted browser fiscal flows`; `reviewer_id=codex-assurance-tester-quality`.

### BCI
- **Trigger rationale:** scheduled bootstrap and rolling writes may overlap and must remain idempotent.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** `evidence_type=real-postgresql-overlapping-publication-probe`; `environment_id=local-wsl-postgresql16-principal-checkout`; `run_id=fiscal-read-model-bci-20260930T023300Z`; `artifact_uri=artifacts/tmp/uninotas-fiscal-read-model/pcv/bci.json`; `artifact_schema_version=pcv-1`; `artifact_sha256=c3157fd3ece4ff0e8c4485ff8b2f91f5f247d54dfe4bff1e8732ee96193c13ce`; `sample_profile_id=BCI-SP-H`; `acceptance_rule_id=BCI-A1`; `result_summary=passed: exactly one commit and nineteen safe rejects in each of five batches, with restart/resume and canonical invariants preserved`; `reviewer_id=codex-assurance-tester-quality`.

### RLS
- **Trigger rationale:** bulk sync/cache/index path plus stage provider pacing is runtime sensitive.
- **Recorded at (UTC):** `2026-09-29T19:53:54Z`
- **Executor ID:** `codex-primary`
- **Evidence object:** pending representative local load and bounded stage smoke artifacts.

## Verification Debt Assessment

- **Audit outcome:** `local-independent-gates-approved / external-and-stage-gates-open`
- **Why this outcome:** deterministic, browser, disposable migration fixture, 23 real-PostgreSQL cases, C20 barriers, resumable failure, restart duplicate, `20x5` BCI and EPS plan/load/lock evidence pass. Fresh R5 test-quality and R3 final reviewers found no material local issue after all product, audit-log and falsifiability gaps were integrated; external drift and runtime gates remain separate.
- **Inline code TODO debt:** no skipped corrective test block remains; UI action-matrix strengthening and stage RLS remain explicit evidence debt.
- **Evidence / audit artifact:** first final review returned `NOT_APPROVABLE` and first test-quality audit returned `FINDINGS_INTEGRATED_REQUIRED`; their P1/P2 implementation findings are addressed in the current working tree.
- **Accepted residual debt:** P3 browser hardening for explicit retry presence in `failed` and retry/refresh absence in `historical_snapshot`; this does not weaken the validated backend contract.

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
- **Audit status:** `no_material_findings`
- **Findings summary:** fresh R5 confirmed the prior durable restart/total/generation/membership, legacy-upgrade, incomplete-export, audit-log and evidence-classification findings are integrated with no new material issue. The failed/historical browser action matrix remains explicitly classified as P3 hardening.
- **Evidence / reference:** fresh no-context R5 on `2026-09-30`; PostgreSQL suites 23/23, focused post-correction set 50/50, backend full suite 403 passed/2 skipped/405 total, deterministic scanner `low` with no bypass or weak-assertion signal.
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** big cross-stack correction intentionally supersedes module decisions and changes a critical list/export contract.
- **Impact signals in scope:** `cross-stack|public API|runtime scheduler|intentional module supersede|high-severity issues`
- **Package mode:** `bounded-summary`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after test-quality audit; reviewer cannot be implementing agent`
- **Review focus:** `adherence|regressions|validation/test evidence|security/performance|elegance|structural soundness|verification debt`
- **Final review status:** `no_material_findings`
- **Findings summary:** fresh R3 found no remaining local P1/P2 after rechecking exact monthly/frontier legacy recovery, final-checkpoint publication retry, mutable-total cleanup, export-cache aggregate audit logging and all canonical PCV hashes. The failed/historical browser action matrix remains P3 hardening; scope/runtime blockers remain separate and explicit. The later artifact-pruning pass changed no product code and the diff expectation guard now passes.
- **Evidence / reference:** fresh no-context final R3 on `2026-09-30`; focused post-correction set 50/50, PostgreSQL 23/23 and full backend 403 passed/2 skipped/405 total.
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

- [x] Canonical fiscal module records interval coverage, windowed sync, local list/export and truthful errors.
- [x] `FISC-EX-02/FISC-EX-04` are intentionally superseded with traceability to `D-RM-C*`.
- [x] Provider-backed detail/documents and legacy module transition remain preserved.
- [ ] TODO/module cross-links and final decision/adherence evidence are recorded after PostgreSQL execution.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** corrective baseline implementation and local evidence remain historical; the new `2026-10-01` local-admission/provider-contract incident adds unresolved decisions and tests. Scope-drift resolution, cutover audit, RLS and exact-revision runtime evidence also remain open; closing or promoting now would overstate delivery.
- **Post-commit/push status:** `MonitorNotes release/uninotas@6f48e60c5c0690a02f9ca0dbed8a6d31e2761475 pushed; remote SHA attested equal; PR/merge/deploy remain user-owned and pending`
- **Next path/status action:** use the user-attested revision behind the five supplied sync rows, collect the sanitized cause for the March contract rejection, then reconverge `D-RM-I01..I03` and the updated review baseline for renewed `APROVADO`; promotion and production-ready claims remain separate and pending.
