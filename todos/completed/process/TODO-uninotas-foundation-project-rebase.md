# TODO — Monitor de Notas: adequar `uninotas-foundation` ao projeto

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Lifecycle state:** `In-Progress — implementation authority granted`
- **Created:** `2026-09-24`
- **Owner:** `Delphi / Strategic CTO-Tech-Lead`, sob autoridade humana do usuário

## Approval

- **Approved by:** `usuário — 2026-09-24 — “APROVADO”` (aprovação renovada após convergência R4 e `preflight-go`).
- **Approval scope:** execução integral de `S-01..S-09` conforme `D-01..D-05`, o mapa congelado de seis módulos, o disposition manifest, o validator e as validações 1:1, com mudanças persistentes limitadas à Foundation; aliases PACED locais já materializados são dependência read-only e não superfície de escrita deste TODO.
- **Current authority of that approval:** `implementation scope approved`; a execução permanece condicionada à ingestão vinculante registrada abaixo e ao authority guard normal retornar `go`.
- **Execution not authorized:** código/runtime do Monitor de Notas, banco, deploy, segredos e núcleo compartilhado do `delphi-ai`; worktrees e checkouts auxiliares também não foram autorizados.
- **Renewed approval required when:** houver mudança de escopo, identidade canônica, tratamento do legado, arquitetura-alvo, validações obrigatórias, repositórios envolvidos ou conversa material de risco além de `D-01..D-05`/`S-01..S-09`.

## Context

O diretório `uninotas-foundation` foi criado a partir de uma Foundation do LeadsHug e ainda descreve outro produto, outro domínio e outros módulos. A inspeção inicial encontrou 47 documentos Markdown com referências a LeadsHug ou ao domínio WhatsApp/Typebot/Evolution/Baileys.

O produto real neste workspace é o Monitor de Notas: uma aplicação NestJS 11 + React/Vite que lê os eventos do SmartNotas registrados pelo Routerfy na tabela `logs`, classifica falhas de emissão e permite que a equipe financeira registre tratamentos sem alterar a tabela de origem. A Foundation precisa passar a ser a autoridade documental desse produto antes de governar novos trabalhos.

## Framing Source & Story Slice

- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `ST-FOUNDATION-01`
- **Why this is the right current slice:** alinhar a autoridade documental ao produto existente é um único objetivo de governança e é pré-requisito para TODOs futuros confiáveis.
- **Direct-to-TODO rationale:** não há comportamento novo de usuário a descobrir; o trabalho é uma migração documental baseada no código, nos READMEs e na infraestrutura já existentes.

## Objective

Transformar `uninotas-foundation` em uma Foundation específica, coerente e verificável para o Monitor de Notas, removendo do tree atual o conteúdo herdado do LeadsHug e documentando o estado real do produto sem inventar capacidades. O histórico Git permanece como registro histórico, sem autoridade ativa.

## Contract Boundary

- Este TODO governa a descoberta, as decisões e a migração da Foundation do projeto.
- O código do produto é fonte de evidência e permanece somente leitura durante esta migração.
- Conteúdo estável deve ter um único owner canônico; índices e outras superfícies devem apontar para ele em vez de duplicar estado.
- Descobertas locais podem permanecer neste TODO quando servirem ao mesmo cutover documental.
- Uma nova funcionalidade, correção de produto, mudança de banco, alteração de API ou adaptação genérica do Delphi exige TODO próprio e aprovação separada.

## Implementation Intent

- **Current delivery:** cutover documental completo da Foundation herdada para a autoridade específica do Monitor de Notas, incluindo validações locais e integração PACED.
- **Planned next steps:** `none outside S-01..S-09`.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** uma substituição canônica única evita manter documentos LeadsHug como fallback, espelho ou autoridade concorrente.

## Delivery Status Canon

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `none`
- **Next exact step:** executar revisão final R19 sobre o HEAD imutável atual e, se limpa, publicar `main` em `origin/main`.

## Active Work State

- **Work state:** `review`
- **Why this state now:** o TODO está em `completed/process/`; R18 confirmou `CLOSEOUT-TQ-01` resolvido e encontrou somente `FINAL-R18-01` em duas instruções de freeze já executado, agora substituídas por R19/publicação como ações únicas.
- **Exit condition:** R19 e guards finais verdes, seguidos pela publicação em `origin/main`.

## Routine-Executor Implementation Evidence — 2026-09-24

- **State at this historical implementation checkpoint:** candidate tree prepared; a conclusão e o movimento posteriores estão registrados nas seções de closeout abaixo.
- **Implemented surfaces:** the frozen disposition manifest was applied; canonical roots, six frozen modules, policies, indexes, decisions, product-truth/cutover artifacts, validator, exception ledger, and safe validator tests now exist only in `uninotas-foundation`.
- **Local evidence:** historical draft evidence is superseded by the reproducible R3 `python3 -B` suite and validator; original chronology remains unverified.
- **Privacy evidence:** prohibited token material is assembled only inside `TemporaryDirectory` by the negative test; no persistently stored sample matches the validator pattern.
- **Boundary evidence:** product and `delphi-ai` status were inspected read-only; their pre-existing changes were not edited by this executor.
- **Remaining owner at this checkpoint:** independent test-quality, final-review, cutover-integrity, completion, and closeout gates were delivery-side responsibilities; R13 and completion later closed all except final review/closeout.
- **Hardening evidence:** validator checks the frozen file/module/index/manifest/ledger/link-anchor/privacy boundaries and mutation suite coverage; Git Bash `./delphi-ai/verify_context.sh` returned `Environment Verified: PACED-Ready.` on 2026-09-24. This is historical implementation evidence; current gate truth is recorded below.
- **Delivery-review RED→GREEN record:** independent delivery probes reported gaps TQ-01..TQ-04, CUTOVER, and ARCH in the initial validator draft. The immutable run evidence for the first 9-test draft was not preserved and is not used as delivery proof (TQ-05). This hardening round first reproduced privacy detection on previously excluded test source, then removed privacy exemptions and retained only runtime-built prohibited samples. R13 and the current completion guard supersede this historical checkpoint.

## Validator Remediation — 2026-09-24

- **Reviewer RED probes addressed:** lifecycle-path ambiguity, section-blind legacy permission, substring deletion checks, identity/scope under-specification, and excluded privacy surfaces.
- **Post-fix GREEN target:** the validator derives the single active/completed lifecycle, requires exact ledger rows by section, rejects every frozen `Delete` path independently, validates D-01/D-05 contracts, and scans every persisted file. This historical checkpoint was later confirmed by R13 and the current completion guard; final review/closeout remain the only active gates.

## Round-2 Remediation — 2026-09-24

- **Reviewer RED findings:** `ARCH-ADH-R2-01..04` and `TQ-R2-01` identified missing canonical contract ownership, unanchored D-01/D-04 assertions, incomplete serialized-credential detection, stale delivery state, and destination-stripping in the legacy scan.
- **Outcome:** the first remediation closed the destination, lifecycle and exact-delete gaps; R3 re-review reopened incomplete API contracts, serialized credential forms and phase-state synchronization. Those R3 blockers are remediated below; no review is marked clean by this implementation record.

## Round-3 Remediation — 2026-09-24

- **R3 finding ledger:** endpoint and SSE contract completeness, decision-table/ownership contradictions, nested serialization credential detection, clean-copy bytecode hygiene, and review-state synchronization were classified as release blockers within D-01..D-05 and remediated locally.
- **GREEN evidence:** the tracked-file-only clean-copy regression and the canonical local suite pass 8 tests with `python3 -B`; the validator, diff hygiene, diff-expectation guard and Git Bash PACED verification pass.
- **Chronology:** original test-first chronology is unverified; reproducible mutation RED→GREEN evidence is the relied-on implementation proof. Delivery R4 later returned no-go and is classified below; no independent delivery gate is clean yet.

## Delivery R4 Finding Classification — 2026-09-24

All material findings match D-01..D-05/DOD-01..DOD-10 and are `release-blocker` items in this TODO; no scope expansion or new product behavior was accepted.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `ARCH-ADH-R4-01` | release-blocker | complete request/response/bounds/media contracts plus public health owner and PT-10 hashes | integrated; superseded by R5 findings and R6 confirmation |
| `ARCH-ADH-R4-02` | release-blocker | distinguish normal JWT from SSE query verification, backend polling from EventSource reconnect, monitoring body 503, and treatment query failure | integrated; superseded by R5 findings and R6 confirmation |
| `ARCH-ADH-R4-03` | release-blocker | mandate owns full D-01 identity; cutover map owns D-02; constitution owns cross-module D-04; treatment routes have one owner | integrated; superseded by R5 findings and R6 confirmation |
| `ARCH-ADH-R4-04` / `TQ-R4-04` | release-blocker | canonical `Pending` stage and explicit planning-R4 versus delivery-R4/R5 state | integrated; superseded by R5 findings and R6 confirmation |
| `TQ-R4-01` | release-blocker | active-authority semantics are rejected before exact historical-ledger reconciliation | integrated; superseded by R5 findings and R6 confirmation |
| `TQ-R4-02` | release-blocker | whitespace-tolerant exact decision parsing, unique README H1, and normalized D-04 contradiction checks | integrated; superseded by R5 findings and R6 confirmation |
| `TQ-R4-03` | release-blocker | independently pinned 34-path set, token-move contract mutations, and cross-surface privacy matrix | integrated; superseded by R5 findings and R6 confirmation |
| `COPILOT-R4-CREDENTIALS` | release-blocker | URI-userinfo and access-key-family credential detection with runtime-built mutations | integrated; superseded by R5 findings and R6 confirmation |

## Delivery R5 Finding Classification — 2026-09-24

All R5 findings remain inside D-01..D-05 and are classified as `release-blocker`; overlapping observations are consolidated below. Remediation is integrated locally and requires an immutable R6 re-review before any completion claim.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `TQ-R5-01` / `CUTOVER-R5-01` | release-blocker | freeze the exact historical legacy-content digest independently of ledger metadata; detect English and Portuguese active-authority claims | integrated; delivery R6 pending |
| `TQ-R5-02` | release-blocker | whitespace/modal ownership and alternate-product identity mutations | integrated; delivery R6 pending |
| `ARCH-R5-01` / `CUTOVER-R5-03` | release-blocker | correct `cliente.logradouro`, explicit status/media per route, and exact SSE wire representation | integrated; delivery R6 pending |
| `ARCH-R5-02` | release-blocker | document polling as continuously active and LISTEN/NOTIFY as optional parallel source | integrated; delivery R6 pending |
| `ARCH-R5-03` | release-blocker | record D-01..D-05 adherence and compare the five frozen module decisions 1:1 | integrated; delivery R6 pending |
| `ARCH-R5-04` | release-blocker | route formal review through `gpt-5.6-sol` at `xhigh` with deterministic guard evidence | integrated; delivery R6 pending |
| `CUTOVER-R5-02` | release-blocker | add GitHub, OpenAI and Google provider-token patterns and runtime-built mutations | integrated; delivery R6 pending |
| `CUTOVER-R5-04` | release-blocker | document query-token maximum 200 separately from the unbounded observed header | integrated; delivery R6 pending |
| `CUTOVER-R5-05` | release-blocker | label PT-10 with exact relative paths and Git-object-byte hash command | integrated; delivery R6 pending |
| `CUTOVER-R5-06` | release-blocker | use boundary-aware legacy matching so current underscored lifecycle filenames are not false historical references | integrated; delivery R6 pending |
| `CUTOVER-R5-07` | release-blocker | restore TODO lane/classification and project-routing taxonomy | integrated; delivery R6 pending |

## Delivery R6 Finding Classification — 2026-09-24

All R6 findings are deduplicated below as `release-blocker` items inside D-01..D-05. No product/runtime change or scope expansion was accepted.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `TQ-R6-01` | release-blocker | replace broad word-boundary exemptions with a term-specific current lifecycle exemption; add compound/underscore English and Portuguese mutations | integrated; delivery R7 pending |
| `TQ-R6-02` | release-blocker | validate every documented table route as a route-bound request/auth/status/media/response tuple; mutate row removal and cross-route status swaps | integrated; delivery R7 pending |
| `TQ-R6-03` | release-blocker | add CPF, Brazilian phone and raw person-payload detection with cross-surface runtime-built mutations | integrated; delivery R7 pending |
| `TQ-R6-04` | release-blocker | pin an additional raw legacy-bearing-line digest so case/whitespace mutations fail | integrated; delivery R7 pending |
| `TQ-R6-05` | release-blocker | remove the ambient clean-copy skip and execute an explicit non-recursive child test list | integrated; delivery R7 pending |
| `ARCH-R6-01` / `CUTOVER-R6-02` | release-blocker | remove unsupported query-token trimming claim while retaining the observed 200-character bound | integrated; delivery R7 pending |
| `CUTOVER-R6-01` | release-blocker | replace six CRLF working-tree hashes with Git-object hashes and verify all 37 product-evidence paths | integrated; delivery R7 pending |
| `CUTOVER-R6-03` | release-blocker | document the observed JWT identity/profile cache and up-to-30-second deactivation/profile-change lag | integrated; delivery R7 pending |
| `CUTOVER-R6-04` | release-blocker | restore durable four-way review-finding taxonomy and promotion rules in TODO governance and constitution | integrated; delivery R7 pending |
| `CUTOVER-R6-05` | release-blocker | synchronize immutable R6 commit/packet state and next R7 action | integrated; delivery R7 pending |

## Delivery R7 Finding Classification — 2026-09-24

Architecture adherence returned `GO`. The seven test-quality/cutover findings below are `release-blocker` items inside D-01..D-05; no scope expansion was accepted.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `TQ-R7-01` | release-blocker | detect compact CPF, Brazilian landline and multiline raw person payload with non-overlapping mutations | confirmed at `de90987` |
| `TQ-R7-02` | release-blocker | parse Markdown table cells and bind request/auth, status/media and response tokens to exact columns | confirmed at `de90987` |
| `TQ-R7-03` | release-blocker | restrict the current lifecycle exemption against hyphen, dot, slash and backup suffixes | confirmed at `de90987` |
| `TQ-R7-ROUTING` | release-blocker | route test-quality and cutover reviews through `gpt-5.6-terra/xhigh`; retain architecture/final on `gpt-5.6-sol/xhigh` | confirmed at `de90987` |
| `CUTOVER-R7-01` | release-blocker | consolidate every delivery finding R4..R7 into the canonical promotion-routing ledger | confirmed at `de90987` |
| `CUTOVER-R7-02` | release-blocker | pin the exact lifecycle-aware 38-path tree plus unique ordered publication manifest; add removal/duplicate mutations | confirmed at `de90987` |
| `CUTOVER-R7-03` | release-blocker | add six primary API/auth/public/enum authorities to PT-10 and reverify all Git-object hashes | confirmed at `de90987` |

## Delivery R8 Finding Classification — 2026-09-24

Cutover integrity returned `GO`. Architecture adherence and test quality each returned one reproducible `release-blocker` inside D-01..D-05; both are integrated locally without product/runtime change and require immutable R9 confirmation.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `ARCH-ADH-R8-01` | release-blocker | distinguish authoritative external production `logs` from the derived, disposable, non-authoritative local replica; bind the mirror tool and local DDL through `PT-11` hashes | confirmed at `222a8a9` |
| `TQ-R8-01` | release-blocker | reject every publication-tree symlink and preserve symlinks during manifest-only copy; mutate an identical external README symlink before and after copy | confirmed at `222a8a9` |

## Delivery R9 Finding Classification — 2026-09-24

Test quality and cutover integrity returned `GO`; architecture confirmed `ARCH-ADH-R8-01` resolved and found one documentary state-coherence `release-blocker`. It remains inside the approved TODO governance scope and requires immutable R10 confirmation.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `ARCH-ADH-R9-01` | release-blocker | synchronize `Next exact step`, active-state rationale, exit condition, gate summaries, execution plan and closeout disposition on R10 | confirmed at `d269bc2` |

## Delivery R10 Finding Classification — 2026-09-24

Test quality and cutover integrity returned `GO`; architecture confirmed `ARCH-ADH-R9-01` resolved and found one enum/schema `release-blocker`. The remediation uses only canonical PACED states and requires immutable R11 confirmation.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `ARCH-ADH-R10-01` | release-blocker | normalize active work state to `review`, architecture status to `findings_integrated`, and clean test/cutover gate statuses to `no_material_findings` | confirmed at `a72780d` |

## Delivery R11 Finding Classification — 2026-09-24

Test quality and cutover integrity returned `GO`; architecture confirmed `ARCH-ADH-R10-01` resolved and found one temporal next-step `release-blocker`. The test-quality observation is corrected in the same authoritative update, while the known WSL caveat remains explicitly outside this Foundation TODO.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `ARCH-ADH-R11-01` | release-blocker | make the immediate action execute/await R12 and then consolidate, without describing already-completed preparation | confirmed at `a973e52` |
| `TQ-R11-OBS-01` | release-blocker | update the current CI-equivalent matrix from stale 8-test candidate wording to the observed 10-test passed result | confirmed at `a973e52`; no residual follow-up |
| `ENV-R11-OBS-01` | by-design/no-action | retain the documented Git Bash acceptance runner; WSL CRLF remediation is outside Foundation authority and is not required because the accepted runner passes | classified with existing alias/runner evidence; no follow-up warranted by this TODO |

## Delivery R12 Finding Classification — 2026-09-24

Test quality and cutover integrity returned `GO`; architecture confirmed `ARCH-ADH-R11-01` resolved and found one taxonomy `release-blocker`. The R11 observations are now mapped to the exact project taxonomy without creating artificial debt or expanding Foundation authority.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `ARCH-ADH-R12-01` | release-blocker | replace the rejected generic labels with `release-blocker` for corrected evidence and `by-design/no-action` for the proven runner boundary | confirmed at `dc1d869` |

## Final Review R14 Finding Classification — 2026-09-24

The independent final review found no content, runtime, performance or elegance defect. Its single P2 `release-blocker` identified stale live lifecycle fields in the governing TODO; the remediation below is inside D-03/DOD-09 and requires confirmation on a new immutable commit.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `FINAL-R14-01` | release-blocker | synchronize current candidate reference, next action, final-review state, execution plan and closeout disposition after completion | confirmed at `65ae750` |

## Final Review R15 Finding Classification — 2026-09-24

The independent R15 review found no content/runtime defect and narrowed the remaining coherence issue to the undated live `Blocker Notes`. The P2 `release-blocker` is integrated below and requires one fresh R16 confirmation.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `FINAL-R15-01` | release-blocker | synchronize `Blocker Notes` with green completion, valid approval, integrated R14/R15 remediation and R16/closeout as the only remaining gates | confirmed at `65ae750` |

## Closeout Post-Move Finding Classification — 2026-09-24

The first full suite after the lifecycle move exposed a test-harness assumption, not a validator/content failure: three mutations addressed `ACTIVE_TODO` directly and one invalid-lifecycle probe used the now-valid historical value. The harness now derives the single current TODO, tests the opposite lifecycle symmetrically and keeps privacy/ledger mutations bound to the actual lifecycle.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `CLOSEOUT-TQ-01` | release-blocker | make lifecycle, ledger, privacy and clean-copy tests symmetric across active/completed trees; rerun all 10 tests after the move | confirmed technically at `5a1ff88` by R17 |

## Final Review R17 Finding Classification — 2026-09-24

R17 confirmed the symmetric harness, 10/10 post-move suite, exact 39-row ledger and manifest move. Its only P2 `release-blocker` concerned live temporal wording after commit `5a1ff88`, not the closeout implementation.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `FINAL-R17-01` | release-blocker | synchronize next action, work-state rationale, blocker notes, review gate, execution plan and closeout status with the committed post-move candidate | integrated; R18 found residual FINAL-R18-01 |

## Final Review R18 Finding Classification — 2026-09-24

R18 reconfirmed `CLOSEOUT-TQ-01` resolved and the technical tree unchanged from `5a1ff88`. Its only P2 `release-blocker` was two live instructions that still requested freezing an already committed remediation.

| Finding | Classification | Integrated remediation | Status |
| --- | --- | --- | --- |
| `FINAL-R18-01` | release-blocker | make R19 on the current immutable HEAD and publication the only remaining actions; remove every instruction to redo an existing freeze | integrated locally; R19 required |

## Post-Implementation Decision Adherence Validation

| Decision | Canonical evidence | Status |
| --- | --- | --- |
| D-01 | `decisions/monitor-de-notas-foundation-decisions.md` — D-01 row | Adherent |
| D-02 | `artifacts/analysis/monitor-de-notas-foundation-cutover-map-20260924.md` — durable removal/recovery map | Adherent |
| D-03 | `project_constitution.md` — Authority | Adherent |
| D-04 | `project_constitution.md` — Invariants, linked to the three application-data module owners | Adherent |
| D-05 | `policies/scope_subscope_governance.md` — machine-readable scope contract | Adherent |

## Final Module Decision Consistency Validation

| Frozen module decision | Exact replacement evidence | Status |
| --- | --- | --- |
| `modules/identity-and-tenancy.md` | `modules/identity-and-team.md`; cutover-map deletion row | Superseded (Approved) |
| `modules/inbox-and-conversations.md` | `modules/events-and-classification.md` + `modules/treatments-and-history.md`; cutover-map deletion row | Superseded (Approved) |
| `modules/integrations-and-channels.md` | `modules/events-and-classification.md` + `modules/realtime-invalidation.md`; cutover-map deletion row | Superseded (Approved) |
| `modules/audit-and-history.md` | `modules/treatments-and-history.md`; cutover-map deletion row | Superseded (Approved) |
| `modules/README.md` | exact six-module canonical index | Superseded (Approved) |

## Blocker Notes

- **Blocker:** `n/a`; R17 encontrou um release blocker temporal corrigível, não um impasse.
- **Why blocked now:** `n/a`; `CLOSEOUT-TQ-01` está confirmado, `FINAL-R18-01` está integrado e somente R19 mais publicação permanecem.
- **What unblocks it:** `n/a`; revisão R19 limpa, guards finais e publicação já autorizada.
- **Owner / source:** owner do TODO; D-01..D-05 continuam autorizados pelo `APROVADO` vigente e nenhuma nova aprovação está pendente.
- **Last confirmed truth:** R18 revisou `d057ee3acbe3a8125d3973bfffa3672e1d4046b0`, reconfirmou `CLOSEOUT-TQ-01` resolvido e encontrou somente `FINAL-R18-01` em duas instruções temporais; a correção está em `main@HEAD` para R19.

## Scope

- [x] `S-01` Inventariar a verdade atual do Monitor de Notas no código, banco documentado, infraestrutura, testes e READMEs, distinguindo comportamento comprovado de intenção futura.
- [x] `S-02` Definir e aplicar a identidade canônica do produto e da Foundation em títulos, links, namespaces e linguagem de domínio.
- [x] `S-03` Reescrever mandato, constituição, entidades, baseline tecnológico, lifecycle e roadmap para refletirem exclusivamente o projeto atual.
- [x] `S-04` Substituir os módulos herdados pelos seis módulos congelados do Monitor de Notas: fronteira externa e leitura de eventos/classificação, tratamentos/histórico, identidade/equipe, invalidação em tempo real, monitoramento operacional e runtime/deploy; escrita da tabela externa de produção `logs` permanece exclusivamente Routerfy, e a réplica local derivada somente pode ser populada pela ferramenta explícita de espelhamento.
- [x] `S-05` Reconciliar backlog, decisões, contratos e políticas com os owners canônicos novos, sem transportar decisões do LeadsHug como se fossem decisões do Monitor de Notas.
- [x] `S-06` Remover do tree atual TODOs, artefatos e documentos herdados do LeadsHug que não pertençam ao Monitor de Notas; o histórico Git será a única retenção do legado removido.
- [x] `S-07` Atualizar a governança para declarar o `delphi-ai` como distribuição local obrigatória do método PACED: todo trabalho do projeto passa por seus workflows e guards, com `APROVADO` e authority guard `go` antes de implementação.
- [x] `S-08` Criar ou adaptar validações determinísticas proporcionais para referências, identidade, links, schemas documentais e ausência de autoridade ativa do LeadsHug.
- [x] `S-09` Validar o pacote final contra o repositório real, registrar evidência 1:1 e concluir o cutover documental sem alterar código, banco ou runtime.

## Out of Scope

- [ ] `OOS-01` Alterar `backend/`, `frontend/`, Docker, Railway, banco de dados ou qualquer comportamento executável do Monitor de Notas.
- [ ] `OOS-02` Rodar seed, migração, espelhamento ou E2E mutável contra o banco remoto.
- [ ] `OOS-03` Implementar features, bugs ou melhorias descobertas durante o levantamento; elas devem virar backlog/TODOs separados.
- [ ] `OOS-04` Alterar o repositório compartilhado `delphi-ai`; lacunas genéricas encontradas devem ser propostas em contrato separado.
- [ ] `OOS-05` Reescrever retroativamente evidência histórica preservada apenas para fazê-la parecer pertencente ao novo produto.
- [ ] `OOS-06` Declarar capacidades, contratos, performance ou maturidade que não estejam comprovados pelo código, pelos testes ou por evidência operacional aceita.

## Decisions Pending — Resolve Before Freeze

- [x] Nenhuma decisão material pendente neste momento.

## Decisions — Resolved Before Freeze

- [x] `D-01` Usar **Monitor de Notas** como nome canônico do produto, `MonitorDeNotas` como nome técnico do repositório e `uninotas-foundation` como nome do repositório documental. Decisão confirmada pelo usuário em 2026-09-24; nomes de pastas não precisam ser alterados.
- [x] `D-02` Excluir do tree atual o conteúdo herdado do LeadsHug que não pertença ao Monitor de Notas, sem criar arquivo legado interno. O histórico Git preserva a proveniência sem manter autoridade documental concorrente. Decisão confirmada pelo usuário em 2026-09-24.
- [x] `D-03` O `delphi-ai` distribui o método **PACED** (*Progressively Accelerated Controlled Engineering through Determinism*) e é passagem obrigatória para todo trabalho do projeto. `uninotas-foundation` governa a verdade específica do produto; PACED governa método, workflows e guards. Alterar o núcleo compartilhado do `delphi-ai` continua exigindo TODO próprio. Decisão confirmada pelo usuário em 2026-09-24.
- [x] `D-04` A tabela externa de produção `logs` pertence ao Routerfy e é somente leitura para o Monitor de Notas; a aplicação escreve apenas em suas próprias tabelas de usuários e tratamentos. A réplica local de desenvolvimento é derivada, descartável, não autoritativa e somente a ferramenta explícita de espelhamento pode populá-la. Decisão consolidada da evidência já incluída no contrato aprovado (`README.md`, `backend/README.md`, Prisma, ferramenta de espelhamento e DDL local isolado).
- [x] `D-05` O produto atual não possui tenancy comprovada. Para satisfazer o contrato PACED de scope/subscope sem inventar domínio, a política local usa um único scope `monitor-de-notas`, subscopes iguais aos seis módulos congelados e `EnvironmentType=landlord` somente como adapter técnico do vocabulário PACED para superfícies únicas do projeto; isso não cria landlord/tenant de negócio. Decisão confirmada pelo novo `APROVADO` em 2026-09-24.

## Decision Baseline — Frozen Before Implementation

- [x] `D-01` Identidade canônica aprovada: produto `Monitor de Notas`, repositório `MonitorDeNotas` e Foundation `uninotas-foundation`.
- [x] `D-02` Política de legado aprovada: remoção do tree atual e retenção somente pelo histórico Git.
- [x] `D-03` Fronteira aprovada: Foundation como autoridade do produto e `delphi-ai`/PACED como autoridade obrigatória do processo de engenharia.
- [x] `D-04` Ownership de dados congelado: a tabela externa de produção `logs` pertence ao Routerfy e é read-only para a aplicação; a réplica local é derivada, descartável e não autoritativa; `monitor_usuarios` e `monitor_tratamentos` pertencem à aplicação.
- [x] `D-05` Scope congelado para o próximo review: produto single-scope sem tenancy; seis subscopes canônicos; `landlord` apenas como classificação técnica PACED, não entidade de domínio.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** correções de links, índices, nomes, anchors, schemas documentais e pequenos ajustes de estrutura necessários ao mesmo cutover.
- **Must update or split the TODO:** mudança de código/runtime, nova capacidade de produto, modificação genérica do Delphi, migração de banco, alteração de API ou nova conversa material de risco/aprovação.

## Definition of Done

- [x] `DOD-01` Nenhum documento canônico ativo apresenta o LeadsHug ou seu domínio como autoridade, produto ou arquitetura atual.
- [x] `DOD-02` README, mandato, constituição, entidades, lifecycle, baseline tecnológico e roadmap descrevem de forma coerente o Monitor de Notas comprovado.
- [x] `DOD-03` Os seis módulos usam os anchors obrigatórios de `delphi-ai/templates/module_template.md`, declaram o scope/subscope de `D-05` e possuem ownership, invariantes, capacidades e contratos correspondentes aos limites reais do sistema.
- [x] `DOD-04` Backlog, decisões, contratos, políticas e TODOs ativos estão reconciliados com a nova identidade e não mantêm estado vivo conflitante.
- [x] `DOD-05` Todo conteúdo herdado do LeadsHug sem função no Monitor de Notas foi removido do tree atual e permanece acessível apenas pelo histórico Git.
- [x] `DOD-06` A divisão de autoridade entre `uninotas-foundation`, `delphi-ai` e o repositório do produto está documentada sem links quebrados.
- [x] `DOD-07` Validações determinísticas e inspeções de referências passam no tree final e possuem evidência específica.
- [x] `DOD-08` O diff fica restrito aos paths aprovados da Foundation; código, configuração, segredos e runtime permanecem inalterados.
- [x] `DOD-09` Decisões estáveis e evidências finais foram consolidadas nos owners canônicos antes do TODO ser movido para `completed/`.
- [x] `DOD-10` Nenhum documento, artifact, código-fonte de teste ou fixture persistida contém PII real/sintética em formato detectável, payload bruto de produção, JWT montado, credencial ou exemplo operacional não redigido; amostras proibidas são montadas somente em diretório temporário durante o teste a partir de fragmentos inofensivos.
- [x] `DOD-11` O contrato de setup documenta e valida como uma checkout limpa materializa `foundation_documentation -> uninotas-foundation` sem versionar o symlink no produto.

## Validation Steps

- [x] `VAL-01` Verificar links internos e anchors em todos os documentos canônicos alterados.
- [x] `VAL-02` Executar busca fail-closed por `LeadsHug|leadshug|WhatsApp|Typebot|Evolution|Baileys|Belluga|Bóora` e classificar cada ocorrência restante como histórica permitida ou falha.
- [x] `VAL-03` Comparar stack, rotas, módulos, entidades e invariantes documentados com `backend/`, `frontend/`, `Dockerfile`, `docker-compose.yml`, `railway.json` e READMEs do produto.
- [x] `VAL-04` Executar os guards aplicáveis do `delphi-ai` para escopo, autoridade, expectativa de diff e conclusão; reservar o closeout guard para o movimento pós-final-review.
- [x] `VAL-05` Executar `git diff --check` e confirmar ausência de segredos, artefatos gerados ou mudanças fora do contrato.
- [x] `VAL-06` Revisar a matriz de evidências critério a critério; resumo agregado não substitui evidência 1:1.
- [x] `VAL-07` Confirmar que o repositório do produto e o `delphi-ai` não receberam mudanças durante a execução.
- [x] `VAL-08` Executar o mesmo scan automatizado de segredo/JWT/PII de alto risco sobre todo o tree persistido, inclusive código/fixtures de teste, e revisão manual de privacidade; mutation tests montam amostras proibidas somente em diretório temporário e provam a falha do scanner.
- [x] `VAL-09` Em workspace limpo no runner Git Bash comprovado, criar/verificar os aliases e executar o entrypoint existente `./delphi-ai/verify_context.sh` até obter `Environment Verified: PACED-Ready.`.

## Completion Evidence Matrix

Cada critério possui evidência concluída 1:1; nenhum resumo agregado substitui estas linhas antes do movimento para `completed/`.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `S-01` | `Scope` | `S-01` Inventariar a verdade atual do Monitor de Notas no código, banco documentado, infraestrutura, testes e READMEs, distinguindo comportamento comprovado de intenção futura. | `traceability` | `PT-01..PT-11`; 53 hashes verificados sobre 45 paths em `78bf271341dfccb2595389f0dbac0e01e8532a7b` | `produto congelado read-only` | `passed` | R13 confirmou zero divergências |
| `S-02` | `Scope` | `S-02` Definir e aplicar a identidade canônica do produto e da Foundation em títulos, links, namespaces e linguagem de domínio. | `doc+test` | `README.md`; `project_mandate.md`; Foundation validator; R13 architecture `GO` | `Foundation local` | `passed` | identidade Monitor de Notas/MonitorDeNotas/uninotas-foundation confirmada |
| `S-03` | `Scope` | `S-03` Reescrever mandato, constituição, entidades, baseline tecnológico, lifecycle e roadmap para refletirem exclusivamente o projeto atual. | `doc+review` | owners raiz no manifesto de 38 paths; R13 architecture `GO` | `Foundation local` | `passed` | owners canônicos revisados contra product truth |
| `S-04` | `Scope` | `S-04` Substituir os módulos herdados pelos seis módulos congelados do Monitor de Notas: fronteira externa e leitura de eventos/classificação, tratamentos/histórico, identidade/equipe, invalidação em tempo real, monitoramento operacional e runtime/deploy; escrita da tabela externa de produção `logs` permanece exclusivamente Routerfy, e a réplica local derivada somente pode ser populada pela ferramenta explícita de espelhamento. | `doc+review` | `modules/README.md`; seis módulos; `PT-11`; R13 architecture `GO` | `Foundation local + produto read-only` | `passed` | seis subscopes exatos e D-04 aderente |
| `S-05` | `Scope` | `S-05` Reconciliar backlog, decisões, contratos e políticas com os owners canônicos novos, sem transportar decisões do LeadsHug como se fossem decisões do Monitor de Notas. | `manifest+review` | disposition manifest 1:1; Foundation validator; R13 architecture `GO` | `Foundation local` | `passed` | nenhum estado vivo conflitante |
| `S-06` | `Scope` | `S-06` Remover do tree atual TODOs, artefatos e documentos herdados do LeadsHug que não pertençam ao Monitor de Notas; o histórico Git será a única retenção do legado removido. | `git+test` | diff `b73b0eb..dc1d869`; `DELETE_PATHS`; R13 cutover: 34/34 ausentes | `Git tree Foundation` | `passed` | histórico Git preserva recuperação |
| `S-07` | `Scope` | `S-07` Atualizar a governança para declarar o `delphi-ai` como distribuição local obrigatória do método PACED: todo trabalho do projeto passa por seus workflows e guards, com `APROVADO` e authority guard `go` antes de implementação. | `guard+doc` | `project_constitution.md`; approval record; authority guard `go` | `Foundation + Delphi read-only` | `passed` | D-03 e roteamento PACED aplicados em todas as rodadas |
| `S-08` | `Scope` | `S-08` Criar ou adaptar validações determinísticas proporcionais para referências, identidade, links, schemas documentais e ausência de autoridade ativa do LeadsHug. | `test` | `python3 -B -m unittest discover -s deterministic/tests -p 'test_*.py' -v`: 10 testes `OK`; validator de schema documental `PASS` | `Foundation local e clean-copy` | `passed` | inclui mutações negativas e proteção de symlink |
| `S-09` | `Scope` | `S-09` Validar o pacote final contra o repositório real, registrar evidência 1:1 e concluir o cutover documental sem alterar código, banco ou runtime. | `fingerprint+review` | R13 triple `GO`; produto/Delphi HEAD, status e diff iguais ao snapshot | `workspace read-only` | `passed` | somente a Foundation mudou |
| `DOD-01` | `Definition of Done` | `DOD-01` Nenhum documento canônico ativo apresenta o LeadsHug ou seu domínio como autoridade, produto ou arquitetura atual. | `test+review` | Foundation validator `PASS`; exact historical exception ledger; R13 architecture `GO` | `Foundation local` | `passed` | superfície ativa e história possuem regras distintas |
| `DOD-02` | `Definition of Done` | `DOD-02` README, mandato, constituição, entidades, lifecycle, baseline tecnológico e roadmap descrevem de forma coerente o Monitor de Notas comprovado. | `doc+traceability` | `artifacts/analysis/monitor-de-notas-product-truth-20260924.md`; 53/45 hashes sem divergência | `produto congelado read-only` | `passed` | cada afirmação material aponta a código/configuração |
| `DOD-03` | `Definition of Done` | `DOD-03` Os seis módulos usam os anchors obrigatórios de `delphi-ai/templates/module_template.md`, declaram o scope/subscope de `D-05` e possuem ownership, invariantes, capacidades e contratos correspondentes aos limites reais do sistema. | `doc+review` | module map, scope policy, validator e R13 architecture `GO` | `Foundation local` | `passed` | seis owners coesos e exatos |
| `DOD-04` | `Definition of Done` | `DOD-04` Backlog, decisões, contratos, políticas e TODOs ativos estão reconciliados com a nova identidade e não mantêm estado vivo conflitante. | `manifest+review` | disposition manifest; publication manifest; R13 taxonomy/architecture `GO` | `Foundation local` | `passed` | owners auxiliares reconciliados |
| `DOD-05` | `Definition of Done` | `DOD-05` Todo conteúdo herdado do LeadsHug sem função no Monitor de Notas foi removido do tree atual e permanece acessível apenas pelo histórico Git. | `git+test` | `git diff --name-status b73b0eb..dc1d869`; 34 exact deletes; validator `PASS` | `Git tree Foundation` | `passed` | histórico Git é a única retenção não ledgerada |
| `DOD-06` | `Definition of Done` | `DOD-06` A divisão de autoridade entre `uninotas-foundation`, `delphi-ai` e o repositório do produto está documentada sem links quebrados. | `test` | Foundation validator link/anchor scan `PASS`; alias contract; constitution | `Foundation local` | `passed` | não duplica regras PACED |
| `DOD-07` | `Definition of Done` | `DOD-07` Validações determinísticas e inspeções de referências passam no tree final e possuem evidência específica. | `test` | 10 unittest `OK`; Foundation/TODO validators `PASS`; R13 fresh reviews | `Foundation local e clean-copy` | `passed` | fixtures positivas e negativas executadas |
| `DOD-08` | `Definition of Done` | `DOD-08` O diff fica restrito aos paths aprovados da Foundation; código, configuração, segredos e runtime permanecem inalterados. | `git+guard` | diff guard `go`: 67/67, zero forbidden/unclassified; fingerprints exatos | `workspace e produto read-only` | `passed` | integration test `n/a` por desvio structure-only aprovado: nenhum fluxo observável muda; mudanças externas preexistentes não são atribuídas ao TODO |
| `DOD-09` | `Definition of Done` | `DOD-09` Decisões estáveis e evidências finais foram consolidadas nos owners canônicos antes do TODO ser movido para `completed/`. | `review` | D-01..D-05 `Adherent`; five frozen module decisions `Superseded (Approved)`; R13 architecture `GO` | `Foundation local` | `passed` | TODO retém somente histórico/evidência de execução |
| `DOD-10` | `Definition of Done` | `DOD-10` Nenhum documento, artifact, código-fonte de teste ou fixture persistida contém PII real/sintética em formato detectável, payload bruto de produção, JWT montado, credencial ou exemplo operacional não redigido; amostras proibidas são montadas somente em diretório temporário durante o teste a partir de fragmentos inofensivos. | `scan+review` | validator high-risk patterns `PASS`; privacy mutation matrix 10 tests `OK`; R13 test-quality `GO` | `Foundation tree + TemporaryDirectory` | `passed` | integration test `n/a` por desvio structure-only aprovado: nenhum fluxo observável muda; PII/payload/JWT/credencial somente em temp runtime |
| `DOD-11` | `Definition of Done` | `DOD-11` O contrato de setup documenta e valida como uma checkout limpa materializa `foundation_documentation -> uninotas-foundation` sem versionar o symlink no produto. | `setup test` | Git Bash `./delphi-ai/verify_context.sh`: `Environment Verified: PACED-Ready.`; alias contract | `Git Bash workspace Windows` | `passed` | `foundation_documentation -> uninotas-foundation`; link não versionado no produto |
| `VAL-01` | `Validation Steps` | `VAL-01` Verificar links internos e anchors em todos os documentos canônicos alterados. | `test` | `python3 -B deterministic/validate_foundation.py --root .`: `Foundation validation passed.` | `Foundation local` | `passed` | scan fail-closed de links/anchors |
| `VAL-02` | `Validation Steps` | legado classificado por superfície | `test` | Foundation validator `PASS`; `deterministic/legacy_reference_exceptions.json`; raw/normalized digests | `Foundation local` | `passed` | `VAL-02` Executar busca fail-closed por `LeadsHug|leadshug|WhatsApp|Typebot|Evolution|Baileys|Belluga|Bóora` e classificar cada ocorrência restante como histórica permitida ou falha. |
| `VAL-03` | `Validation Steps` | `VAL-03` Comparar stack, rotas, módulos, entidades e invariantes documentados com `backend/`, `frontend/`, `Dockerfile`, `docker-compose.yml`, `railway.json` e READMEs do produto. | `traceability review` | `PT-01..PT-11`; 53 pares/45 paths via Git-object bytes; R13 triple `GO` | `produto congelado read-only` | `passed` | sem consulta mutante ao banco |
| `VAL-04` | `Validation Steps` | `VAL-04` Executar os guards aplicáveis do `delphi-ai` para escopo, autoridade, expectativa de diff e conclusão; reservar o closeout guard para o movimento pós-final-review. | `guard` | TODO deterministic `PASS`; authority `go`; diff expectation `go`; completion guard command no candidato | `Foundation local` | `passed` | closeout guard fica no gate pós-final-review conforme o próprio critério |
| `VAL-05` | `Validation Steps` | `VAL-05` Executar `git diff --check` e confirmar ausência de segredos, artefatos gerados ou mudanças fora do contrato. | `git+scan` | `git diff --check`; validator privacy scan; diff guard 67/67 | `Foundation local` | `passed` | nenhum `.env`, bytecode ou valor sensível |
| `VAL-06` | `Validation Steps` | `VAL-06` Revisar a matriz de evidências critério a critério; resumo agregado não substitui evidência 1:1. | `review` | 29 linhas `S-01..S-09`, `DOD-01..DOD-11`, `VAL-01..VAL-09`, todas `passed` | `Foundation local` | `passed` | cobertura 1:1 revisada antes do completion guard |
| `VAL-07` | `Validation Steps` | `VAL-07` Confirmar que o repositório do produto e o `delphi-ai` não receberam mudanças durante a execução. | `fingerprint` | produto `78bf271` + status/diff congelados; Delphi `9ba43e8` + status/diff vazios | `workspace read-only` | `passed` | igualdade exata dos digests em R13 |
| `VAL-08` | `Validation Steps` | `VAL-08` Executar o mesmo scan automatizado de segredo/JWT/PII de alto risco sobre todo o tree persistido, inclusive código/fixtures de teste, e revisão manual de privacidade; mutation tests montam amostras proibidas somente em diretório temporário e provam a falha do scanner. | `scan+review` | validator inteiro + privacy mutation test + R13 test-quality audit | `Foundation tree + TemporaryDirectory` | `passed` | integration test `n/a` por desvio structure-only aprovado: nenhum fluxo observável muda; nenhuma allowlist |
| `VAL-09` | `Validation Steps` | `VAL-09` Em workspace limpo no runner Git Bash comprovado, criar/verificar os aliases e executar o entrypoint existente `./delphi-ai/verify_context.sh` até obter `Environment Verified: PACED-Ready.`. | `setup test` | `"C:\Program Files\Git\bin\bash.exe" -lc "cd /c/Unifast/MonitorDeNotas && ./delphi-ai/verify_context.sh"` | `Git Bash workspace Windows` | `passed` | saída exata `Environment Verified: PACED-Ready.`; sem commit de link no produto |

## Execution Lane Tracking

- **Local implementation branches:** `uninotas-foundation:main`
- **Promotion lane path:** `main -> origin/main`
- **Lane-promoted threshold for this TODO:** `origin/main` com validações e guards verdes
- **Production-ready threshold for this TODO:** `n/a — pacote documental autônomo; Completed exige publicação imutável em origin/main`

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| baseline do contrato | `main@65ae750` | `n/a — autoridade Foundation single-branch` | `n/a` | `direct push guarded` | `local-implemented; final review clean` |
| cutover da Foundation | `main@65ae750` | `n/a — autoridade Foundation single-branch` | `n/a` | `direct push after closeout gates` | `local-implemented; final review clean` |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `uninotas-foundation` | `uninotas-foundation` | `b73b0ebc79daeb74acd6c377b4b307438095c848` | `working_tree` |

`MonitorDeNotas` e `delphi-ai` não são implementation repositories deste TODO e, por isso, não entram como baselines do diff guard. A imutabilidade read-only dessas superfícies é validada separadamente pelos fingerprints congelados abaixo em `VAL-07`.

### Read-Only Evidence Snapshot

Capturado em 2026-09-24 antes de qualquer execução. A comparação final repete os comandos exatos; qualquer diferença fora de `uninotas-foundation` bloqueia `VAL-07` até classificação humana.

| Surface | Fingerprint / Ref | Exact Reproduction Command |
| --- | --- | --- |
| produto Git HEAD | `78bf271341dfccb2595389f0dbac0e01e8532a7b` | `git rev-parse HEAD` |
| produto status sem a Foundation | `51a2f9d37d5b710b23ef6358b40f5afa764a96f8e26adf1448b877043c454958` | `git status --porcelain=v1 -z -- . ':(exclude)uninotas-foundation' \| sha256sum` |
| produto diff rastreado sem a Foundation | `156b0be28fa3ae69459773d6c46f67dc27eaa64a27a2b0515e0e4cb8586d51fb` | `git diff --binary -- . ':(exclude)uninotas-foundation' \| sha256sum` |
| manifesto de arquivos de evidência do produto | `0c418fff5f3f3b488bebd1ccf67ac8a737d312c25fe2c601a0b8c35349191f22` | `find README.md backend frontend Dockerfile docker-compose.yml railway.json -type f ! -path '*/node_modules/*' ! -path '*/dist/*' ! -name '.env*' -print0 \| sort -z \| xargs -0 sha256sum \| sha256sum` |
| Delphi Git HEAD | `9ba43e8bba3618d029320bf6d7b40415881a0287` | `git -C delphi-ai rev-parse HEAD` |
| Delphi status | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `git -C delphi-ai status --porcelain=v1 -z \| sha256sum` |
| Delphi diff rastreado | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `git -C delphi-ai diff --binary \| sha256sum` |

Hashes individuais que sustentam as decisões de ownership ficam no `Pre-Execution Product Truth Baseline`; eles impedem que uma mudança preexistente ou concorrente seja confundida com a verdade revisada.

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `uninotas-foundation` | `*.md` | `M` | documentos canônicos raiz |
| `uninotas-foundation` | `modules/**` | `A,M,D,R,??` | substituir módulos herdados pelos módulos do produto atual |
| `uninotas-foundation` | `backlog/**` | `A,M,D,R,??` | reconciliar candidatos e próximos gates |
| `uninotas-foundation` | `decisions/**` | `A,M,D,R,??` | registrar decisões e retirar autoridade ativa herdada |
| `uninotas-foundation` | `contracts/**` | `A,M,D,R,??` | reconstruir índice de contratos verificáveis |
| `uninotas-foundation` | `policies/**` | `A,M,D,R,??` | preservar apenas políticas aplicáveis ao produto |
| `uninotas-foundation` | `artifacts/**` | `A,M,D,R,??` | evidência de descoberta/cutover conforme `D-02` |
| `uninotas-foundation` | `todos/**` | `A,M,D,R,??` | governança, classificação do legado e evidência deste TODO |
| `uninotas-foundation` | `deterministic/**` | `A,M,D,R,??` | validações específicas da Foundation, se aprovadas no refinamento |
| `uninotas-foundation` | `local_packages.yaml` | `M` | alinhar referências locais ao workspace atual |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `uninotas-foundation` | `.git/**` | `any` | metadados Git nunca são conteúdo da migração |

## PACED Setup / Recalibration Status

- **Lane:** `recalibration`.
- **Readiness:** `pass` após habilitar `core.symlinks=true` localmente e materializar os bootloaders/links PACED como symlinks reais pelo WSL.
- **Structural drift:** `none` após a correção operacional local.
- **Documentation drift:** `material` — a Foundation descreve LeadsHug.
- **Canonical coverage drift:** `material` — módulos e contratos pertencem a outro domínio.
- **Governance drift:** `material` — autoridades ainda nomeiam LeadsHug/leadshug-engineering em vez do limite `uninotas-foundation` + PACED.
- **Derived doctor caveat:** o setup doctor validou presença/estrutura e produziu `calibrated`, mas o processo Windows encerrou `49` por ausência de Python no Git Bash e o diagnóstico não inspeciona semântica de produto; por isso ele não substitui o drift material comprovado por conteúdo.
- **Outcome:** `normalization TODO required`; este é o TODO de normalização aprovado.

## Profile Scope & Handoffs

- **Gate 0 — Genesis Eligibility:** `rejected` — há repositório canônico, lifecycle e TODO tático; a correção é evolução estratégica governada, não bootstrap sem contrato.
- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack` documental, com evidência `nestjs`, `react`, `vite`, `postgresql`, `prisma`, `docker` e `railway` somente leitura.
- **Expected supporting profiles:** `routine-executor`, `assurance-tester-quality`, `formal-reviewer`.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto <changed-paths>`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `Strategic / CTO-Tech-Lead` | `routine-executor` | executar a substituição documental já decidida sem redefinir o contrato | `uninotas-foundation/**` | `completed; R3 remediation locally green` |
| `routine-executor` | `Assurance / Tester-Quality` | desafiar evidência, links, referências e ausência de autoridade concorrente | diff e validações da Foundation | `delivery R13 test-quality GO on dc1d869` |
| `Assurance / Tester-Quality` | `formal-reviewer` | revisar aderência arquitetural e integridade do cutover | pacote final consolidado | `delivery R13 architecture/cutover GO; final review is the next independent gate` |

## Complexity

- **Level:** `big`
- **Checkpoint policy:** `section-by-section`
- **Why this level:** o cutover altera identidade, autoridade, módulos, políticas, decisões, contratos, TODOs e validação estrutural de toda a Foundation.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary anchors:** `project_mandate.md`, `project_constitution.md`, `domain_entities.md`, `technology_baseline.md`, `evolution_lifecycle.md` e `system_roadmap.md`.
- **Module index:** `modules/README.md`.
- **Supporting owners:** `backlog/README.md`, `decisions/README.md`, `contracts/README.md`, `policies/`, `todos/README.md` e `artifacts/README.md`.
- **Product evidence sources:** `../README.md`, `../backend/README.md`, `../frontend/README.md` e código/configuração do produto.
- **Planned decision promotion targets:** `project_mandate.md`, `project_constitution.md`, `evolution_lifecycle.md` e módulos novos.
- **Module decision consolidation targets:** decisões de ownership e invariantes nos respectivos módulos; decisões transversais em `decisions/README.md`/registro próprio.

## Pre-Execution Product Truth Baseline

Este inventário read-only fecha a descoberta que antes estava indevidamente delegada ao executor. Ele governa somente a reescrita documental; nenhuma dessas leituras autoriza mudança no produto.

| Truth ID | Verified Product Truth / Boundary | Exact Evidence | SHA-256 / Stable Ref | Target Owner |
| --- | --- | --- | --- | --- |
| `PT-01` | Routerfy grava a tabela autoritativa de produção `logs`; Monitor de Notas somente a lê por SQL cru; a tabela não possui chave primária e não entra no Prisma. | `backend/docs/tabela-logs.md`; `backend/prisma/schema.prisma`; `backend/src/logs/logs.sql.ts` | `151fbc8540804ff73c8b3d8f8164c1d5d6f932dde8e9aecbcd9f731ff59dd3e6`; `cb53048b181e179e0d0a74188a17279e36213a50508a058fd69bd3a110056963`; `142c26ab4bdda0d53e59934460b029e6463c05e6d30083c7b2e2a2c4fd441643` | `modules/events-and-classification.md` |
| `PT-02` | Somente eventos `org_path = 'SmartNotas'` alimentam o monitor; `ref_id` não é identidade única de uma tentativa e correlaciona tratamentos/histórico. | `backend/src/logs/logs.sql.ts`; `backend/src/logs/logs.service.ts`; `backend/docs/tabela-logs.md` | `142c26ab4bdda0d53e59934460b029e6463c05e6d30083c7b2e2a2c4fd441643`; `579fbb4312b516e7de70b12e434f9d19d8dbb84f309c892ab16d152563bb02cc`; `151fbc8540804ff73c8b3d8f8164c1d5d6f932dde8e9aecbcd9f731ff59dd3e6` | `modules/events-and-classification.md` + `modules/treatments-and-history.md` |
| `PT-03` | Classificação possui projeção TypeScript e expressão SQL equivalentes; situação efetiva aplica o último tratamento, e `PENDENTE` reabre para a situação original. | `backend/src/logs/logs.classifier.ts`; `backend/src/logs/logs.sql.ts`; `backend/src/logs/logs.mapper.ts` | `ca0a4340189321e1924eec0fbda82c492aca4b19bc0476d54953eb8e0eafcfbe`; `142c26ab4bdda0d53e59934460b029e6463c05e6d30083c7b2e2a2c4fd441643`; `875ea83fa0982d64ac00e0b66ff6c8aa12a447d52d232f672daecb070367441f` | `modules/events-and-classification.md` |
| `PT-04` | A aplicação escreve `monitor_tratamentos` como histórico append-only correlacionado por `ref_id`; o último registro define o tratamento corrente. | `backend/prisma/schema.prisma`; `backend/src/logs/logs.service.ts` | `cb53048b181e179e0d0a74188a17279e36213a50508a058fd69bd3a110056963`; `579fbb4312b516e7de70b12e434f9d19d8dbb84f309c892ab16d152563bb02cc` | `modules/treatments-and-history.md` |
| `PT-05` | A aplicação possui `monitor_usuarios`, autenticação JWT e perfis; usuários são desativados, não apagados, para preservar autoria. | `backend/prisma/schema.prisma`; `backend/src/auth/auth.service.ts`; `backend/src/usuarios/usuarios.service.ts` | `cb53048b181e179e0d0a74188a17279e36213a50508a058fd69bd3a110056963`; `59d506febff80a402e5b01347c2fd3c212ab3408584428c794c8778f7d89814d`; `08033dd301b931ba5a97afffd177393e2899046bc3ed4c65a02c16f989391f5e` | `modules/identity-and-team.md` |
| `PT-06` | SSE envia somente sinal de invalidação; o cliente rebusca a API. Eventos podem vir da API, LISTEN/NOTIFY opcional ou polling, com heartbeat/dedupe. | `backend/src/realtime/realtime.service.ts`; `frontend/src/hooks/useTempoReal.ts` | `5b24b40d4bbe88fbc95e5fe920f3a71a6dae19a2cfc7d83845f8753565d27bed`; `1e5f6bf8b4ce9af68902f2c22a7f85843f4deef05c9a62eb8e6fbba14880a411` | `modules/realtime-invalidation.md` |
| `PT-07` | Monitoramento operacional externo reutiliza o resumo de eventos em janela móvel e deve distinguir banco indisponível de zero erros. | `backend/src/monitoramento/monitoramento.service.ts`; `backend/src/logs/logs.service.ts` | `bea861ead5853965a8b6918f179b04e8305a993940c4f16ae8e72af1ca29ddcf`; `579fbb4312b516e7de70b12e434f9d19d8dbb84f309c892ab16d152563bb02cc` | `modules/operational-monitoring.md` |
| `PT-08` | React/Vite consome listagem, filtros, resumo, detalhe, tratamentos, equipe e invalidação realtime por contratos explícitos da API. | `frontend/src/api/eventos.ts`; `frontend/src/paginas/ListaEventos.tsx`; `frontend/src/paginas/DetalheEvento.tsx`; `frontend/src/paginas/Equipe.tsx` | `212a47f7b1e3c85fed39e55e63a30d5d0b1dbe7926ac5e8b312bfb89e9d00fbc`; `63b3b9941b5825496e757e5d9de6f0fe1ccf18eb9f50366f8a40e0456cf1cad5`; `a4d2829c6b7b1269c8ecc3f0b58c3bc8fe956cae878c80eaad7126f4be90f643`; `2d9a1e8b8645189fefdd832a48209b3a28bf85e68d9216356051e52d19ce010b` | módulos funcionais correspondentes; sem módulo frontend paralelo |
| `PT-09` | Execução e deploy são NestJS + React/Vite + PostgreSQL/Prisma em Docker/Railway, sem mudança de runtime neste TODO. | `Dockerfile`; `docker-compose.yml`; `railway.json`; `backend/src/config/configuration.ts` | `9d0554370de58fd504282f0d8bf98c1bce841d9ef736da11be611dfa17cd9e32`; `5e5e9f39e191b477e9981ba9047ace1ee7082e73ca447d454d27dddcaec9a781`; `f711055e59a2442c04299987a2bc30fe24cd02df86cd9e4e4cf57efec76a5697`; `5948aeb71df0b82690e131f689b9005043e9d8d610a750b8a026f8aa79af702e` | `modules/runtime-and-deployment.md` |
| `PT-10` | Rotas `/api/v1`, limites de request/response, guards, wire SSE, health, monitoramento e erro padrão são contratos observados. | paths exatos e hashes em `artifacts/analysis/monitor-de-notas-product-truth-20260924.md` | commit congelado `78bf271341dfccb2595389f0dbac0e01e8532a7b`; comando `git show <commit>:<relative-path> \| sha256sum` sobre bytes do objeto Git | seis módulos canônicos |
| `PT-11` | A réplica local de desenvolvimento de `logs` é derivada, descartável e não autoritativa; somente a ferramenta explícita de espelhamento a popula, sem transferir ownership da produção. | `backend/prisma/espelhar.ts`; `backend/prisma/sql/002_logs_dev.sql` | `a1a847f686e143583e42cb9d4ab983e0cd426fb3c30404ba67fcde081ce40869`; `34ff7fae8d6a31e329bc222e89ef369a4bc2ebff23444e39c863d23872b6a98e` | `modules/runtime-and-deployment.md` |

Os hashes completos foram obtidos com `git show 78bf271341dfccb2595389f0dbac0e01e8532a7b:<relative-path> | sha256sum`, isto é, sobre os bytes normalizados do objeto Git congelado, e não sobre bytes CRLF/LF do working tree. O comando deve ser repetido antes do closeout; o artifact final de product truth preserva esta matriz Foundation → fonte.

## Canonical Target Module Map

| Final Module | Singular Ownership | Key Invariants / Contracts | Replaces |
| --- | --- | --- | --- |
| `modules/events-and-classification.md` | fronteira read-only Routerfy/SmartNotas, consulta, filtros, paginação, exportação e classificação original/efetiva | nunca escrever em `logs`; `ref_id` não é PK; SQL e classificador devem permanecer semanticamente alinhados | `integrations-and-channels.md`; parte de `inbox-and-conversations.md` |
| `modules/treatments-and-history.md` | comandos de tratamento e histórico auditável | escreve somente `monitor_tratamentos`; correlação por `ref_id`; último tratamento governa situação efetiva; autoria preservada | `audit-and-history.md`; parte de `inbox-and-conversations.md` |
| `modules/identity-and-team.md` | autenticação, perfis e administração da equipe financeira | JWT; usuário ativo; proteção do último admin; desativação preserva autoria | `identity-and-tenancy.md` |
| `modules/realtime-invalidation.md` | sinalização SSE de mudança | evento não é fonte de verdade; consumidor sempre rebusca API; polling permanece ativo e LISTEN/NOTIFY é fonte paralela opcional | capacidade inexistente na Foundation herdada |
| `modules/operational-monitoring.md` | contrato para robô/alerta operacional | reutiliza semântica do resumo; indisponibilidade não equivale a zero; janela/limites explícitos | capacidade inexistente na Foundation herdada |
| `modules/runtime-and-deployment.md` | topologia, configuração e deploy comprovados | documentar somente Docker/Railway/configuração observada; sem secret values e sem mudança de runtime | fragmentos transversais herdados, sem transportar domínio LeadsHug |

O índice `modules/README.md` apontará exatamente para estes seis módulos. Adição, remoção, merge ou split material exige atualizar esta tabela e renovar `APROVADO`.

Todos os seis módulos terão `Core scope=monitor-de-notas`, um subscope igual ao nome canônico sem `.md`, `EnvironmentType=landlord` somente como adapter PACED conforme `D-05`, e os anchors obrigatórios de `delphi-ai/templates/module_template.md`. Nenhum módulo poderá inferir tenancy, BU, canal ou organização a partir desse adapter técnico.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `modules/identity-and-tenancy.md` | identidade multi-tenant e BU WhatsApp do LeadsHug | `Supersede (Intentional)` | domínio incompatível com Monitor de Notas |
| `modules/inbox-and-conversations.md` | caixa e conversas WhatsApp | `Supersede (Intentional)` | módulo inexistente no produto atual |
| `modules/integrations-and-channels.md` | Meta/Evolution/Typebot e canais | `Supersede (Intentional)` | integrações incompatíveis com Routerfy/SmartNotas |
| `modules/audit-and-history.md` | auditoria do atendimento LeadsHug | `Supersede (Intentional)` | substituir por histórico de tratamentos e ownership real |
| `modules/README.md` | índice de módulos LeadsHug | `Supersede (Intentional)` | novo índice será derivado do produto atual |

## Tracked Foundation File Disposition Manifest

Manifesto 1:1 dos 59 arquivos rastreados no baseline. `Rewrite` preserva o path mas substitui sua autoridade; `Delete` remove o conteúdo do tree atual; `Keep` exige inspeção final; `Move at closeout` só ocorre após os gates de conclusão.

| Baseline Path | Disposition | Final Owner / Rationale |
| --- | --- | --- |
| `.gitattributes` | `Keep` | metadado neutro, sujeito a inspeção final |
| `.gitignore` | `Keep` | metadado neutro, sujeito a inspeção final |
| `README.md` | `Rewrite` | índice da Foundation Monitor de Notas + contrato de setup PACED |
| `artifacts/README.md` | `Rewrite` | índice de evidências do produto atual |
| `artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md` | `Delete` | legado preservado somente no Git |
| `artifacts/analysis/leadshug-executive-system-dossier-20260915.md` | `Delete` | legado preservado somente no Git |
| `artifacts/analysis/leadshug-system-analysis-20260915.md` | `Delete` | legado preservado somente no Git |
| `artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md` | `Delete` | legado preservado somente no Git |
| `artifacts/migration/claude-legacy-reconciliation-review.json` | `Delete` | migração de outro produto |
| `artifacts/migration/claude-legacy-reconciliation-review.prompt.txt` | `Delete` | migração de outro produto |
| `artifacts/migration/legacy-reconciliation-20260915.md` | `Delete` | migração de outro produto |
| `artifacts/publication-manifest.txt` | `Rewrite` | manifesto exato do novo tree publicado |
| `artifacts/workspace-link-stabilization-20260915.md` | `Delete` | evidência LeadsHug não autoritativa |
| `backlog/README.md` | `Rewrite` | candidatos do Monitor de Notas, vazio se não comprovados |
| `contracts/README.md` | `Rewrite` | índice de contratos observados, sem inventar contratos públicos |
| `decisions/README.md` | `Rewrite` | índice de decisões do Monitor de Notas |
| `decisions/ST-01-foundation-lifecycle-decisions.md` | `Delete` | decisão herdada substituída por `D-01..D-04` |
| `deterministic/.gitkeep` | `Delete` | substituído por validator, testes e exception ledger reais |
| `domain_entities.md` | `Rewrite` | `LogEvent`, `Tratamento`, `Usuario` e projeções comprovadas |
| `evolution_lifecycle.md` | `Rewrite` | lifecycle PACED específico da Foundation atual |
| `local_packages.yaml` | `Rewrite` | referências locais do workspace Monitor de Notas |
| `modules/README.md` | `Rewrite` | índice exato dos seis módulos congelados |
| `modules/audit-and-history.md` | `Delete` | substituído por `treatments-and-history.md` sem semântica LeadsHug |
| `modules/identity-and-tenancy.md` | `Delete` | substituído por `identity-and-team.md`; produto não é multi-tenant comprovado |
| `modules/inbox-and-conversations.md` | `Delete` | domínio inexistente no produto atual |
| `modules/integrations-and-channels.md` | `Delete` | substituído pela fronteira Routerfy read-only em events/classification |
| `policies/central_whatsapp_independent_legacy_policy.md` | `Delete` | política de domínio inexistente |
| `policies/engineering_guardrails.md` | `Rewrite` | guardrails locais que referenciam PACED sem duplicá-lo |
| `policies/query_path_guardrails.md` | `Rewrite` | invariantes read-only/query de `logs` comprovados |
| `policies/scope_subscope_governance.md` | `Rewrite` | policy obrigatória PACED: scope único `monitor-de-notas`, seis subscopes e ausência explícita de tenancy de negócio conforme `D-05` |
| `policies/validation_evidence_policy.md` | `Rewrite` | evidência 1:1, privacidade e fingerprints read-only |
| `policies/web_to_app_promotion_policy.md` | `Delete` | lane inexistente no projeto atual |
| `project_constitution.md` | `Rewrite` | constituição Monitor de Notas |
| `project_mandate.md` | `Rewrite` | mandato Monitor de Notas |
| `system_roadmap.md` | `Rewrite` | roadmap comprovado, sem transportar backlog legado |
| `technology_baseline.md` | `Rewrite` | NestJS/React/Vite/PostgreSQL/Prisma/Docker/Railway observados |
| `todos/README.md` | `Rewrite` | governança PACED e classificação de findings do projeto atual |
| `todos/active/features/TODO-leadshug-mode-specific-primary-and-secondary-color.md` | `Delete` | trabalho ativo de outro produto |
| `todos/active/features/TODO-leadshug-typebot-automation-integration.md` | `Delete` | trabalho ativo de outro produto |
| `todos/active/process/TODO-foundation-lifecycle-structural-validator.md` | `Delete` | contrato herdado substituído pelo validator deste TODO |
| `todos/active/process/TODO-uninotas-foundation-project-rebase.md` | `Move at closeout` | mover para `todos/completed/process/` somente após todos os gates |
| `todos/completed/features/TODO-delphi-shell-line-endings-and-cross-platform-validation.md` | `Delete` | histórico externo ao produto; Git preserva |
| `todos/completed/features/TODO-leadshug-foundation-and-delphi-migration.md` | `Delete` | histórico LeadsHug |
| `todos/completed/features/TODO-leadshug-identity-visual-screen-tests.md` | `Delete` | histórico LeadsHug |
| `todos/completed/features/TODO-leadshug-initial-branding-and-unofficial-connection.md` | `Delete` | histórico LeadsHug |
| `todos/completed/features/TODO-leadshug-post-onboarding-brand-settings.md` | `Delete` | histórico LeadsHug |
| `todos/completed/features/TODO-leadshug-secondary-color-background-contract.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-central-whatsapp-independent-legacy-policy.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-ci-contract-and-migration-test-gates.md` | `Delete` | contrato CI de outro produto |
| `todos/completed/process/TODO-leadshug-architecture-truth-and-legacy-boundaries.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-leadshug-authority-and-technology-documentation-rebase.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-leadshug-executive-system-dossier.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-leadshug-legacy-authority-migration-and-retirement.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-leadshug-system-analysis-and-modernization-plan.md` | `Delete` | histórico LeadsHug |
| `todos/completed/process/TODO-leadshug-workspace-link-stabilization.md` | `Delete` | histórico LeadsHug |
| `todos/ephemeral/.gitignore` | `Keep` | estrutura neutra de lifecycle |
| `todos/ephemeral/.gitkeep` | `Keep` | estrutura neutra de lifecycle |
| `todos/promotion_lane/.gitkeep` | `Keep` | estrutura neutra de lifecycle |

### Planned Additions

| New Path | Owner / Purpose |
| --- | --- |
| `artifacts/analysis/monitor-de-notas-product-truth-20260924.md` | matriz completa de verdade → código/hash |
| `artifacts/analysis/monitor-de-notas-foundation-cutover-map-20260924.md` | before/after, disposition e prova de cutover |
| `decisions/monitor-de-notas-foundation-decisions.md` | racional/proveniência de `D-01..D-04` promovidos |
| `modules/events-and-classification.md` | `PT-01..PT-03` + consumidores de lista/detalhe/export em `PT-08` |
| `modules/treatments-and-history.md` | `PT-02,PT-04` + consumidor de tratamento/detalhe em `PT-08` |
| `modules/identity-and-team.md` | `PT-05` + consumidor de equipe/sessão em `PT-08` |
| `modules/realtime-invalidation.md` | `PT-06` + consumer hook em `PT-08` |
| `modules/operational-monitoring.md` | `PT-07` |
| `modules/runtime-and-deployment.md` | `PT-09` |
| `deterministic/validate_foundation.py` | validator canônico local |
| `deterministic/legacy_reference_exceptions.json` | exceções históricas com path, razão e owner |
| `deterministic/tests/test_validate_foundation.py` | testes positivos e mutation-style negativos |
| `deterministic/tests/fixtures/**` | somente trees persistidos válidos e fragmentos não detectáveis; casos proibidos são montados em temp runtime |

## Module Decision Consistency Gate

- **Status:** `delivery-R13-clean`; D-01..D-05 estão `Adherent`, as cinco decisões permanecem `Superseded (Approved)` e R13 confirmou a consistência do pacote `Local-Implemented`.
- **Finding:** todas as decisões de módulos herdadas pertencem ao LeadsHug; nenhuma deve ser preservada como verdade do Monitor de Notas.
- **Resolution:** supersessão intencional integral, autorizada por `D-02`, com substituição pelos módulos listados em `S-04`.
- **Evidence:** conteúdo atual de `modules/*.md`, estrutura do backend/frontend e READMEs do produto.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** a Foundation ativa descreve outro sistema e precisa de um cutover de autoridade, não apenas troca textual de nomes.
- **Deviation / debt being retired:** documentos, módulos e TODOs LeadsHug atuando como se fossem verdade do Monitor de Notas.
- **Target steady-state after closeout:** uma Foundation cujo conteúdo ativo pertence somente ao produto atual e cujo histórico legado, se preservado, é inequivocamente não autoritativo.
- **Temporary exceptions allowed:** `none`.
- **Cutover / removal condition:** todos os owners canônicos e índices apontam à nova verdade, validações passam e não há duas autoridades ativas concorrentes.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| autoridade específica do produto separada do método de engenharia | `D-03` | toda a Foundation | evita duplicar regras PACED e mantém decisões de negócio locais |
| `logs` de produção é fonte externa read-only para a aplicação; a réplica local é derivada e não autoritativa; tratamentos pertencem à aplicação | `D-04` consolidada com `PT-01` e `PT-11` | dados, eventos, tratamentos e runtime | preserva ownership e impede mutação acidental da tabela Routerfy |
| um owner canônico por verdade viva | `evolution_lifecycle.md` | módulos, decisões, contratos, backlog e TODOs | elimina estado concorrente e documentação divergente |
| afirmações somente com evidência atual | `S-01`, `OOS-06` | todo documento novo | impede transportar capacidades do LeadsHug ou inferências não comprovadas |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| renomear LeadsHug por busca/substituição sem revalidar o domínio | termos/entidades incompatíveis ou módulos sem correspondente no código | produz documentação falsa com aparência atual | `none` |
| manter arquivos LeadsHug como fallback ativo ou arquivo interno | ocorrências não justificadas no tree atual | cria duas autoridades concorrentes | `none`; legado somente no Git |
| copiar regras genéricas PACED para a Foundation | duplicação de workflows/guards do `delphi-ai` | causa drift entre método e produto | somente referência/link ao owner PACED |
| editar produto/runtime para fazê-lo coincidir com a documentação | diff fora de `uninotas-foundation` | inverte a direção deste TODO de normalização documental | exige TODO próprio e novo `APROVADO` |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| `guard` | identidade e legado | validator local em `deterministic/` + scan fail-closed `VAL-02` | retorno de autoridade LeadsHug ou termos de domínio incompatíveis | `implement-in-this-todo` | teste positivo/negativo e execução no tree final |
| `review` | verdade vs. código | matriz de rastreabilidade Foundation → código/docs | afirmações sem fonte ou módulos inventados | `implement-in-this-todo` | artifact de análise e `VAL-03` |
| `guard` | escopo do diff | `todo_diff_expectation_guard.py` + `git diff --check` | mudança fora da Foundation ou em segredo/runtime | `already-enforced` | saída final `go` |
| `guard` | execução PACED | `todo_authority_guard.py`, `todo_completion_guard.py`, `todo_closeout_guard.py` | execução/fechamento sem aprovação e evidência | `already-enforced` | outputs finais registrados no TODO |

### Deterministic Validator Contract

- **Canonical commands:** `python3 -B -m unittest discover -s deterministic/tests -p 'test_*.py'` e `python3 -B deterministic/validate_foundation.py --root .`.
- **Active-authority surfaces:** documentos raiz, `modules/`, `backlog/`, `contracts/`, `decisions/`, `policies/`, `todos/README.md` e TODOs ativos diferentes do contrato de migração governante.
- **Governing migration TODO:** enquanto este arquivo estiver em `todos/active/process/`, cada termo legado permitido deve possuir linha exata no ledger com `path`, `term`, `context_kind=historical_migration_record`, `section`, `reason`, `owner` e `lifecycle=active_until_closeout_move`; isso registra proveniência, não autoriza o termo em owners canônicos.
- **Historical surfaces:** após o closeout move, a entrada muda para o path em `todos/completed/process/` e `lifecycle=historical`; outros completed TODOs/artifacts só são permitidos quando listados sem wildcard em `deterministic/legacy_reference_exceptions.json`.
- **Closeout sequence:** validar tree candidato com a exceção ativa estrita; executar reviews/guards; mover o TODO; atualizar somente o path/lifecycle da exceção; repetir a suíte inteira antes do commit/push final.
- **Fail-closed checks:** arquivos obrigatórios incluindo `policies/scope_subscope_governance.md`, anchors do `module_template.md` nos seis módulos, consistência scope/subscope, links/anchors relativos, ausência dos paths `Delete`, owner único, nenhuma autoridade ativa LeadsHug, exception ledger sem wildcard amplo, nenhum symlink no tree publicado e nenhum arquivo não classificado pelo publication manifest.
- **Privacy checks:** rejeitar JWT-like tokens, private-key markers, atribuições de segredo e identificadores pessoais plausíveis em todo o tree, inclusive fontes/fixtures de teste; nomes de variáveis e fragmentos que isoladamente não formam o padrão proibido são permitidos.
- **Mutation fixtures:** autoridade legada em owner ativo, menção histórica permitida no governing TODO, mesma menção como autoridade ativa proibida, exception sem owner/razão/lifecycle, link quebrado, módulo órfão, anchor obrigatório ausente, scope divergente, owner ausente e symlink externo antes/depois da cópia por manifesto podem usar trees temporários inofensivos; JWT/PII/segredo proibido deve ser montado somente em `tempfile.TemporaryDirectory` durante o teste, concatenando fragmentos fonte que não acionam o scan do repositório.
- **Manual complement:** revisar semanticamente que nenhuma ocorrência permitida apresenta o legado como verdade atual e que nenhum exemplo deriva de payload real.

### PACED Workspace Alias Contract

- **Owner:** setup local do workspace do Monitor de Notas; o repositório de produto não versiona esse symlink.
- **Required topology:** `foundation_documentation -> uninotas-foundation` e `delphi-ai -> C:\Unifast\delphi-ai` (ou paths equivalentes no host).
- **Canonical Windows command:** `cmd /c mklink /D foundation_documentation uninotas-foundation` quando o alias ainda não existir; para o Delphi, `cmd /c mklink /D delphi-ai C:\Unifast\delphi-ai`.
- **WSL equivalent:** `ln -s uninotas-foundation foundation_documentation` e `ln -s /mnt/c/Unifast/delphi-ai delphi-ai`, somente depois de confirmar que o destino não existe.
- **Acceptance runner comprovado:** no host Windows com Git for Windows, `"C:\Program Files\Git\bin\bash.exe" -lc "cd /c/Unifast/MonitorDeNotas && ./delphi-ai/verify_context.sh"`; execução em 2026-09-24 retornou `Environment Verified: PACED-Ready.`.
- **WSL limitation:** `bash delphi-ai/verify_context.sh` não é aceito como evidência enquanto o wrapper CRLF falhar no WSL; corrigir o Delphi exige TODO separado e não bloqueia o runner Git Bash comprovado.
- **Acceptance:** no runner declarado, verificar os dois symlinks e executar o entrypoint existente `delphi-ai/verify_context.sh`; `delphi-ai/bootloaders/verify_context.sh` não existe e não deve ser referenciado.
- **Scope boundary:** os aliases atuais são infraestrutura local preestabelecida e read-only neste TODO; recriação para validar setup não é mudança persistente do produto nem autoriza qualquer outro path raiz.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before execution authority`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `no_material_findings`
- **Decision review evidence / resolution:** R1-R3 geraram `RF-01..RF-16`; R4 reviewer `foundation-architecture-r4` retornou zero findings e posições `performance=acceptable`, `elegance/structural/operational=strong_positive` sobre o snapshot `7f28cd8`.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `no_material_findings`
- **Adherence review evidence / resolution:** fresh architecture delivery R13 returned `GO` on immutable `dc1d86985c66e04384e59b582132d2309bae2b76`, confirmed `ARCH-ADH-R12-01` resolved and found no new issue.
- **No-go handling:** retornar ao diagnóstico/decisão ou ao loop de evidência; não alegar execução ou conclusão com divergência aberta.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | O snapshot de código/configuração é a fonte técnica para reconstruir a verdade do produto; READMEs somente corroboram. | `backend/prisma/schema.prisma`; `backend/src/logs/logs.sql.ts`; `backend/src/logs/logs.service.ts`; `backend/src/realtime/realtime.service.ts`; `backend/src/monitoramento/monitoramento.service.ts`; `backend/src/auth/auth.service.ts`; `backend/src/usuarios/usuarios.service.ts`; `backend/prisma/espelhar.ts`; `backend/prisma/sql/002_logs_dev.sql`; controllers/guards/filter enumerados em `PT-10`; `frontend/src/api/eventos.ts`; `frontend/src/hooks/useTempoReal.ts`; `PT-01..PT-11` e SHA-256 exatos no snapshot `HEAD 78bf271341dfccb2595389f0dbac0e01e8532a7b` | qualquer hash divergente reabre inventário e scope review | `High` | `Keep as Assumption` |
| `A-02` | A tabela externa de produção `logs` permanece read-only para o Monitor de Notas e pertence ao Routerfy; a réplica local é derivada, descartável e não autoritativa. | `backend/prisma/schema.prisma@cb53048b…`, `backend/src/logs/logs.sql.ts@142c26ab…`, `backend/docs/tabela-logs.md@151fbc85…`, `backend/prisma/espelhar.ts@a1a847f6…`, `backend/prisma/sql/002_logs_dev.sql@34ff7fae…` | muda invariantes, contratos e módulos | `High` | `Promoted to D-04` |
| `A-03` | `uninotas-foundation` é a autoridade específica do produto e `delphi-ai` distribui o PACED obrigatório para todo trabalho. | `D-03`; `delphi-ai/README.md` no commit `9ba43e8bba3618d029320bf6d7b40415881a0287`; alias contract local | muda links, responsabilidades e gates | `High` | `Promoted to D-03` |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** a migração documental precisa provar que as afirmações sobre arquitetura, ownership de dados e comportamento correspondem ao código atual antes de congelar o contrato.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md`
- **Gate status:** `findings_integrated`
- **Findings summary:** R2 detectou que o guard não dereferencia `PT-01..PT-09`; `A-01` agora cita paths de código diretamente e o guard passou.
- **Evidence / reference:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md` — `Overall outcome: go`; `Live assumptions checked: 1` em 2026-09-24.
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** o pacote é `big`, altera toda a autoridade documental e precisa de baseline imutável antes das revisões independentes.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `main`
- **Baseline commit:** `7f28cd8a506f8c36b4cdd5cd40192748bc4efb7f`
- **Baseline push reference:** `origin/main`
- **Baseline TODO blob:** `13fced0c1ca6ec4470631aebb559de29dfaa1602`
- **Baseline snapshot SHA-256:** `3524658154b2f7372e1c24d3a13bec42432318fa3eac5186e758ecfb0f67caa0`
- **Gate status:** `no_material_findings`
- **Findings summary:** `RF-15..RF-16` integrados; package final sincronizado e ligado a commit, ref, blob e SHA-256.
- **Evidence / reference:** git-write guards `go`; push `dfe6603..7f28cd8`; `ls-remote` confirmou o SHA integral; snapshot `/tmp/monitor-foundation-review.tJs1Sm/review-package-7f28cd8.md`.
- **Waiver authority / reference:** `n/a`
- **Review packet rule:** cada rodada usa snapshot derivado de commit publicado, com blob e SHA-256; evidência pós-freeze não altera o pacote material salvo quando um finding exige novo baseline.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impedir que a revisão ou o plano ampliem silenciosamente o contrato aprovado.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before execution authority`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** zero seções materiais divergiram do baseline final `7f28cd8`; `origin/main` resolveu e contém o commit.
- **Evidence / reference:** guard canônico — `Overall outcome: go`; `Changed material sections: 0` em 2026-09-24.
- **Waiver authority / reference:** `n/a`

## Plan Review Gate

- **Status:** `no_material_findings`

### Review Sections

- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards

- **Issue ID:** `ARCH-01`
  - **Severity:** `high`
  - **Evidence:** 47 documentos Markdown contêm identidade/domínio LeadsHug; `modules/*.md` não corresponde ao produto atual.
  - **Why it matters now:** uma troca apenas nominal conservaria contratos falsos como autoridade.
  - **Option A (Recommended):** reconstruir os owners canônicos a partir de evidência do produto e excluir o conteúdo legado sem fallback.
    - **Effort:** `high`; **Risk:** `medium`; **Blast radius:** `cross-module`; **Maintenance burden:** `low`; **Performance impact:** `neutral`; **Elegance impact:** `improves`; **Structural soundness impact:** `improves`.
  - **Option B:** editar somente títulos e termos ostensivos.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `cross-module`; **Maintenance burden:** `high`; **Performance impact:** `neutral`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Option C (Do Nothing):** manter a Foundation LeadsHug.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `cross-module`; **Maintenance burden:** `high`; **Performance impact:** `neutral`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Recommendation:** `Option A`, coerente com `D-02` e o cutover de autoridade.

- **Issue ID:** `ARCH-02`
  - **Severity:** `medium`
  - **Evidence:** PACED exige `foundation_documentation/`, enquanto o repositório documental aprovado se chama `uninotas-foundation`.
  - **Why it matters now:** tools e bootloaders precisam de um path estável sem renomear o repositório.
  - **Option A (Recommended):** manter `uninotas-foundation` e expor `foundation_documentation -> uninotas-foundation` como integração operacional local.
    - **Effort:** `low`; **Risk:** `low`; **Blast radius:** `local`; **Maintenance burden:** `low`; **Performance impact:** `neutral`; **Elegance impact:** `improves`; **Structural soundness impact:** `improves`.
  - **Option B:** renomear o repositório.
    - **Effort:** `medium`; **Risk:** `medium`; **Blast radius:** `cross-module`; **Maintenance burden:** `medium`; **Performance impact:** `neutral`; **Elegance impact:** `neutral`; **Structural soundness impact:** `neutral`.
  - **Option C (Do Nothing):** executar ferramentas com paths divergentes.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `local`; **Maintenance burden:** `high`; **Performance impact:** `neutral`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Recommendation:** `Option A`, já comprovada pelo readiness PACED.

- **Issue ID:** `TEST-01`
  - **Severity:** `medium`
  - **Evidence:** os validadores herdados são incompletos/pendentes e não provam identidade, links e authority cutover do novo produto.
  - **Why it matters now:** revisão manual isolada não impede regressão futura.
  - **Option A (Recommended):** entregar validator local pequeno, determinístico e testado para os invariantes deste cutover.
    - **Effort:** `medium`; **Risk:** `low`; **Blast radius:** `module`; **Maintenance burden:** `low`; **Performance impact:** `neutral`; **Elegance impact:** `improves`; **Structural soundness impact:** `improves`.
  - **Option B:** manter apenas comandos `rg` manuais.
    - **Effort:** `low`; **Risk:** `medium`; **Blast radius:** `module`; **Maintenance burden:** `medium`; **Performance impact:** `neutral`; **Elegance impact:** `neutral`; **Structural soundness impact:** `regresses`.
  - **Option C (Do Nothing):** nenhuma proteção persistente.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `module`; **Maintenance burden:** `high`; **Performance impact:** `neutral`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Recommendation:** `Option A`, limitado a standard library e invariantes explícitos.

### Failure Modes & Edge Cases

- [x] Excluir um arquivo genérico ainda útil junto com conteúdo LeadsHug; mitigado pela reconstrução por owner/propósito e validação de links.
- [x] Canonizar contagens operacionais temporárias como verdade permanente; mitigado mantendo números voláteis fora dos invariantes.
- [x] Documentar `logs` como tabela Prisma ou gravável; mitigado pela validação de ownership read-only contra schema/SQL.
- [x] Duplicar regras PACED na Foundation; mitigado referenciando o owner compartilhado nos docs locais.
- [x] Deixar TODOs ativos LeadsHug autorizando trabalho; mitigado pelo scan fail-closed de autoridade ativa residual.
- [x] Copiar valores de `.env`; mitigado usando somente nomes/redações e scan de segredos.

### Residual Unknowns / Risks

- [x] O conteúdo exato dos novos módulos foi refinado durante o inventário sem alterar o conjunto de domínios aprovado em `S-04`.
- [x] A lacuna semântica do setup doctor PACED foi coberta pelo validator local, pelos 53 pares de hash e pelas revisões independentes.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md`
- **Latest TEACH evidence / artifact:** `audit_escalation_guard.py — Overall outcome: go; fingerprint 777f23c42717; critique/test-quality/final/architecture reviews required; security/PCV/triple-review not needed`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | cutover integral da Foundation |
| `blast_radius` | `cross-module` | todos os owners documentais são afetados |
| `behavioral_change_or_bugfix` | `no` | documentação/guards apenas |
| `changes_public_contract` | `no` | contratos são documentados a partir do runtime existente, não alterados |
| `touches_auth_or_tenant` | `no` | autenticação é documentada, não modificada |
| `touches_runtime_or_infra` | `no` | runtime e infraestrutura são somente leitura |
| `touches_tests` | `yes` | validator local terá testes determinísticos |
| `critical_user_journey` | `no` | sem mudança de jornada |
| `release_or_promotion_critical` | `no` | Foundation autônoma, sem release de produto |
| `high_severity_plan_review_issue` | `yes` | `ARCH-01` exige cutover real, não renomeação superficial |
| `explicit_three_lane_request` | `no` | usuário não pediu protocolo triplo dedicado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** complexidade `big`, blast radius cross-module e issue arquitetural alta.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede|high-severity issue card`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** TODO congelado, READMEs do produto, schema Prisma, SQL de logs e índices/documentos Foundation atuais.
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required — fresh formal reviewer; no worktree and read-only package`
- **Canonical multi-lane audit protocol:** `n/a`
- **Audit session / round evidence:** `n/a`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `no_material_findings`
- **Findings summary:** R4 closure critique retornou zero findings; `RF-01..RF-16` permanecem resolvidos sem regressão.
- **Resolution ledger:** achados originais da crítica, antes da deduplicação `RF-01..RF-08`.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `CRIT-01` | `Integrated` | `useful` | `yes` | `paced` | `n/a` | aprovação anterior rebaixada a intenção; novo `APROVADO` tornou-se obrigatório em `RF-01` |
| `CRIT-02` | `Integrated` | `useful` | `yes` | `paced` | `n/a` | freeze renovado registra commit, push, blob e SHA-256 em `RF-02` |
| `CRIT-03` | `Integrated` | `useful` | `yes` | `paced` | `n/a` | snapshot read-only registra HEAD/status/diff/content digests e paths/hash em `RF-04` |
| `CRIT-04` | `Integrated` | `useful` | `yes` | `paced` | `n/a` | mapa final de módulos, disposition 1:1 e evidence matrix foram congelados em `RF-03` |
| `CRIT-05` | `Integrated` | `useful` | `yes` | `project` | `n/a` | validator por superfície, exception ledger e mutation fixtures definidos em `RF-05` |
| `CRIT-06` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `DOD-10`, `VAL-08` e security assessment cobrem PII/payload/JWT/segredo em `RF-06` |
| `CRIT-07` | `Integrated` | `useful` | `partial` | `project` | `n/a` | aliases declarados preestabelecidos/read-only e removidos do touched scope em `RF-08` |
| `CRIT-R2-01` | `Integrated` | `useful` | `no` | `none` | `n/a` | paths relativos concretos foram adicionados diretamente à evidência de `A-01` em `RF-13` |
| `CRIT-R2-02` | `Integrated` | `useful` | `no` | `none` | `n/a` | `Baseline push reference` agora contém o ref Git resolvível `origin/main` em `RF-14` |
| `CRIT-R2-03` | `Integrated` | `useful` | `yes` | `paced` | `n/a` | scope policy mudou de `Delete` para `Rewrite` e ganhou contrato `D-05` em `RF-09` |
| `CRIT-R2-04` | `Integrated` | `useful` | `partial` | `paced` | `n/a` | acceptance usa entrypoint existente e runner Git Bash comprovado; WSL fica explicitamente não aceito em `RF-10` |
| `CRIT-R3-01` | `Integrated` | `useful` | `partial` | `paced` | `n/a` | lifecycle, next step, blocker notes, execution plan e `D-01..D-05` foram sincronizados em `RF-15` |
| `CRIT-R3-02` | `Integrated` | `useful` | `partial` | `project` | `n/a` | amostras JWT/PII proibidas agora são montadas somente em temp runtime; tree persistido inteiro continua sob scan em `RF-16` |

- **Evidence / reference:** R4 dispatch `/tmp/monitor-foundation-review.tJs1Sm/critique-r4-dispatch.json`; reviewer `fresh-stateless-closure-critique-r4`; zero findings; posições `performance/operational=acceptable`, `elegance/structural=strong_positive`.
- **Waiver authority / reference:** `n/a`

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| immutable Foundation R13 package `dc1d86985c66e04384e59b582132d2309bae2b76` | CI/Copilot-style P1/P2 contract, test-quality, architecture and cutover failure modes | `passed` | three fresh R13 reviewers over `/tmp/monitor-foundation-copilot-r13/review-packet.md`; 10 tests; validators/extractors | `none` | all three lanes `GO`; no P1 or P2 finding; prior rows are resolved in the canonical ledger |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| all ingested PACED rules, workflows and project invariants | direct violation, disguised bypass, fallback, scope escape and test-only shortcut | `passed` | normalized `rule_spirit_anti_pattern_scan.sh --repo . --stack all --path . --json-output /tmp/foundation-rule-spirit-r13.json` | `none`; zero heuristic findings; severity `none` | R13 manual reviews also confirmed no bypass; no allowlist used |

## Verification Debt Adjudication

- **Audit outcome:** `none` after manual adjudication of `/tmp/foundation-verification-debt-r13.txt`.
- **Short rationale:** the helper's `high` heuristic consists of historical remediation rows, intentional unchecked `Out of Scope` non-goals, canonical paths/labels containing the word `TODO`, explicit `n/a` fields and the accepted Git Bash runner boundary; all current S/DoD/VAL requirements have concrete `passed` evidence and completion is `go`.
- **Inline code TODO debt classification:** `accepted`; no executable source marker was introduced—the matches are the governing TODO filename, ledger owner `TODO owner`, PACED commands and documentary governance prose.
- **Promotion debt:** `none`; stable identity, ownership, module and validation conclusions are in canonical owners, with the tactical record retaining only provenance and review history.
- **Accepted residual debt:** `none`; the unpreserved first-draft chronology is not used as proof, and the WSL CRLF observation is `by-design/no-action` because Git Bash is the accepted runner and Delphi is read-only.
- **Material issue cards:** `none`; no audit signal requires implementation or a follow-up TODO.

## Promotion Finding Routing Ledger

Os achados de arquitetura e crítica foram congelados, deduplicados e classificados contra o objetivo, decisões e non-goals do TODO. Todos permanecem no mesmo TODO porque são requisitos para autoridade de execução, não trabalho de hardening posterior.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `RF-01` (`ARCH-OP-02`,`CRIT-01`) | `high` | `release-blocker` | tratar aprovação anterior como intenção; exigir novo `APROVADO` pós-gates | ordem de autoridade é parte do contrato atual | `resolved in planning` | `Approval.Current authority`; aprovação renovada recebida em 2026-09-24 |
| `RF-02` (`ARCH-OP-03`,`CRIT-02`) | `high` | `release-blocker` | commit + TODO blob/hash no dispatch e freeze renovado | reproducibilidade do review atual | `resolved in planning` | `Gate: Review Baseline Freeze` |
| `RF-03` (`ARCH-OP-01`,`CRIT-04`) | `high` | `release-blocker` | inventário read-only, seis módulos fechados e disposition 1:1 antes da execução | elimina discricionariedade destrutiva do executor | `resolved in planning` | `PT-01..PT-09`; module map; disposition manifest |
| `RF-04` (`CRIT-03`) | `high` | `release-blocker` | HEAD/status/diff/content fingerprints para produto e Delphi | prova `VAL-07` e ancora assumptions em bytes | `resolved in planning` | `Read-Only Evidence Snapshot` |
| `RF-05` (`ARCH-OP-04`,`CRIT-05`) | `medium` | `release-blocker` | validator por superfície + exception ledger explícito + mutation fixtures | `DOD-01/VAL-02` dependem dessa semântica | `resolved in planning; delivery evidence in DoD` | `Deterministic Validator Contract` |
| `RF-06` (`CRIT-06`) | `medium` | `release-blocker` | proibir PII/payload/JWT/credencial e exigir scan + revisão manual | artefatos persistentes fazem parte da entrega atual | `resolved in planning; delivery evidence in DoD` | `DOD-10`; `VAL-08`; Security Risk Assessment |
| `RF-07` (`ARCH-OP-05`) | `medium` | `release-blocker` | documentar owner/comandos/aceitação do alias em workspace limpo | setup PACED é condição operacional atual | `resolved in planning; delivery evidence in DoD` | `DOD-11`; `VAL-09`; alias contract |
| `RF-08` (`CRIT-07`) | `medium` | `release-blocker` | declarar aliases preestabelecidos/read-only e remover escrita raiz do touched scope | mantém diff enforcement determinístico | `resolved in planning` | `Touched Surfaces`; `Diff Expectation Contract` |
| `RF-09` (`ARCH-R2-01`,`CRIT-R2-03`) | `high` | `release-blocker` | reescrever, não excluir, a policy de scope/subscope obrigatória | os seis módulos precisam dessa autoridade canônica | `resolved in planning` | `D-05`; disposition manifest; module map |
| `RF-10` (`ARCH-R2-02`,`CRIT-R2-04`) | `high` | `release-blocker` | usar `delphi-ai/verify_context.sh` no Git Bash comprovado e não alegar WSL | reabre e corrige o acceptance inexequível de `RF-07` | `resolved in planning; delivery evidence in DoD` | `DOD-11`; `VAL-09`; alias contract |
| `RF-11` (`ARCH-R2-03`) | `medium` | `release-blocker` | remover “ingestão”, distribuir `PT-08` pelos módulos funcionais e exigir `module_template.md` | fecha ownership e blueprint dos seis módulos | `resolved in planning` | `S-04`; Planned Additions; Rules Ingestion |
| `RF-12` (`ARCH-R2-04`) | `medium` | `release-blocker` | classificar termos históricos do governing TODO por seção/owner/lifecycle e repetir suite após move | evita ciclo impossível ou allowlist ampla | `resolved in planning; delivery evidence in DoD` | `Deterministic Validator Contract` |
| `RF-13` (`CRIT-R2-01`) | `high` | `release-blocker` | incluir paths de código diretamente em `A-01` | guard não dereferencia `PT-01..PT-09` | `resolved; coherence guard go` | `Assumptions Preview.A-01`; guard 2026-09-24 |
| `RF-14` (`CRIT-R2-02`) | `high` | `release-blocker` | usar ref real `origin/main` e manter SHA em campo separado | guard precisa resolver o ref com Git | `resolved; scope-drift guard go` | `Gate: Review Baseline Freeze`; guard 2026-09-24 |
| `RF-15` (`ARCH-R3-01`,`CRIT-R3-01`) | `high` | `release-blocker` | sincronizar lifecycle, next step, work state, blockers, execution plan, questions e closeout | elimina instruções concorrentes antes do novo approval | `resolved; planning R4 clean` | seções canônicas de estado + `Execution Plan` |
| `RF-16` (`CRIT-R3-02`) | `medium` | `release-blocker` | gerar padrões proibidos apenas em temp runtime a partir de fragmentos inofensivos | evita validator rejeitar o próprio corpus ou exigir allowlist ampla | `resolved; planning R4 clean` | `DOD-10`; `VAL-08`; validator/test contracts |
| `ARCH-ADH-R4-01` | `high` | `release-blocker` | complete route/request/response/media/health contracts and PT-10 | contract fidelity is required by the approved cutover | `fixed at cacc054; superseded by later rounds` | `Delivery R4 Finding Classification` |
| `ARCH-ADH-R4-02` | `high` | `release-blocker` | distinguish JWT/SSE, polling/reconnect, monitoring 503 and treatment failure | same approved architecture boundary | `fixed at cacc054; superseded by later rounds` | `Delivery R4 Finding Classification` |
| `ARCH-ADH-R4-03` | `high` | `release-blocker` | restore singular mandate/data/route ownership | same approved architecture boundary | `fixed at cacc054` | `Delivery R4 Finding Classification` |
| `ARCH-ADH-R4-04`,`TQ-R4-04` | `medium` | `release-blocker` | synchronize delivery state | governing TODO state is part of this delivery | `fixed at cacc054` | `Delivery R4 Finding Classification` |
| `TQ-R4-01` | `high` | `release-blocker` | reject active-authority semantics before historical reconciliation | validator is part of current cutover | `fixed at cacc054; superseded by later rounds` | `Delivery R4 Finding Classification` |
| `TQ-R4-02` | `high` | `release-blocker` | harden identity/decision/ownership parsing | validator is part of current cutover | `fixed at cacc054; superseded by later rounds` | `Delivery R4 Finding Classification` |
| `TQ-R4-03` | `high` | `release-blocker` | independently pin deletion set and mutation coverage | validator is part of current cutover | `fixed at cacc054; superseded by later rounds` | `Delivery R4 Finding Classification` |
| `COPILOT-R4-CREDENTIALS` | `high` | `release-blocker` | detect URI-userinfo and access-key credentials | privacy contract is in current DoD | `fixed at cacc054; superseded by later rounds` | `Delivery R4 Finding Classification` |
| `TQ-R5-01`,`CUTOVER-R5-01` | `high` | `release-blocker` | freeze historical content and multilingual authority claims | validator is part of current cutover | `fixed at 04b865e; superseded by later rounds` | `Delivery R5 Finding Classification` |
| `TQ-R5-02` | `high` | `release-blocker` | harden ownership/identity contradiction probes | validator is part of current cutover | `fixed at 04b865e` | `Delivery R5 Finding Classification` |
| `ARCH-R5-01`,`CUTOVER-R5-03` | `high` | `release-blocker` | correct field/status/media/SSE contracts | contract fidelity is required by current cutover | `fixed at 04b865e` | `Delivery R5 Finding Classification` |
| `ARCH-R5-02` | `high` | `release-blocker` | correct polling and optional notification semantics | contract fidelity is required by current cutover | `fixed at 04b865e` | `Delivery R5 Finding Classification` |
| `ARCH-R5-03` | `medium` | `release-blocker` | record decision adherence and frozen module supersession 1:1 | closeout evidence belongs here | `fixed at 04b865e` | `Delivery R5 Finding Classification` |
| `ARCH-R5-04` | `high` | `release-blocker` | use guarded formal-review routing | PACED routing is required by D-03 | `fixed at 04b865e; refined by R7` | `Delivery R5 Finding Classification` |
| `CUTOVER-R5-02` | `high` | `release-blocker` | add provider credential patterns | privacy contract is in current DoD | `fixed at 04b865e` | `Delivery R5 Finding Classification` |
| `CUTOVER-R5-04` | `medium` | `release-blocker` | document query-token bound precisely | contract fidelity is required by current cutover | `fixed at 04b865e` | `Delivery R5 Finding Classification` |
| `CUTOVER-R5-05` | `high` | `release-blocker` | make PT-10 paths/hash method exact | frozen product truth is current evidence | `fixed at 04b865e; superseded by later rounds` | `Delivery R5 Finding Classification` |
| `CUTOVER-R5-06` | `high` | `release-blocker` | remove lifecycle-name false collision without broad bypass | validator is part of current cutover | `fixed at 04b865e; superseded by later rounds` | `Delivery R5 Finding Classification` |
| `CUTOVER-R5-07` | `medium` | `release-blocker` | restore project TODO routing taxonomy | governance owner belongs in current cutover | `fixed at 04b865e; superseded by later rounds` | `Delivery R5 Finding Classification` |
| `TQ-R6-01` | `high` | `release-blocker` | block brand compounds and underscore variants | validator is part of current cutover | `fixed at f7dde5d` | `Delivery R6 Finding Classification` |
| `TQ-R6-02` | `high` | `release-blocker` | bind routes to status/media semantics | validator is part of current cutover | `fixed at f7dde5d; refined by R7` | `Delivery R6 Finding Classification` |
| `TQ-R6-03` | `medium` | `release-blocker` | expand PII/raw-payload coverage | privacy contract is in current DoD | `fixed at f7dde5d; refined by R7` | `Delivery R6 Finding Classification` |
| `TQ-R6-04` | `medium` | `release-blocker` | freeze raw historical lines in addition to normalized semantics | validator is part of current cutover | `fixed at f7dde5d` | `Delivery R6 Finding Classification` |
| `TQ-R6-05` | `medium` | `release-blocker` | remove ambient clean-copy skip | clean-copy proof is current evidence | `fixed at f7dde5d` | `Delivery R6 Finding Classification` |
| `ARCH-R6-01`,`CUTOVER-R6-02` | `medium` | `release-blocker` | remove unsupported token normalization claim | contract fidelity is required by current cutover | `fixed at f7dde5d` | `Delivery R6 Finding Classification` |
| `CUTOVER-R6-01` | `high` | `release-blocker` | replace working-tree hashes with Git-object evidence | frozen product truth is current evidence | `fixed at f7dde5d; refined by R7` | `Delivery R6 Finding Classification` |
| `CUTOVER-R6-03` | `medium` | `release-blocker` | document JWT cache enforcement lag | contract fidelity is required by current cutover | `fixed at f7dde5d` | `Delivery R6 Finding Classification` |
| `CUTOVER-R6-04` | `medium` | `release-blocker` | restore four-way finding taxonomy/promotion rule | governance owner belongs in current cutover | `fixed at f7dde5d` | `Delivery R6 Finding Classification` |
| `CUTOVER-R6-05` | `medium` | `release-blocker` | synchronize delivery state | governing TODO state is part of this delivery | `fixed at f7dde5d` | `Delivery R6 Finding Classification` |
| `TQ-R7-01` | `high` | `release-blocker` | detect compact/document/landline/multiline payload variants independently | privacy contract is in current DoD | `confirmed at de90987` | `Delivery R7 Finding Classification`; R8 test-quality |
| `TQ-R7-02` | `medium` | `release-blocker` | bind route tuple tokens to exact Markdown columns | validator is part of current cutover | `confirmed at de90987` | `Delivery R7 Finding Classification`; R8 test-quality |
| `TQ-R7-03` | `medium` | `release-blocker` | reject suffixed lifecycle-name lookalikes | validator is part of current cutover | `confirmed at de90987` | `Delivery R7 Finding Classification`; R8 test-quality |
| `TQ-R7-ROUTING` | `high` | `release-blocker` | route each review kind to its guarded model family | PACED routing is required by D-03 | `confirmed at de90987` | `Agent Routing Preflight`; R8 routing |
| `CUTOVER-R7-01` | `medium` | `release-blocker` | consolidate delivery findings into this canonical ledger | prevents carry-forward loss | `confirmed at de90987` | `Delivery R7 Finding Classification`; R8 cutover |
| `CUTOVER-R7-02` | `medium` | `release-blocker` | freeze lifecycle-aware tree and unique ordered manifest | exact publication set is current cutover scope | `confirmed at de90987` | `Delivery R7 Finding Classification`; R8 cutover |
| `CUTOVER-R7-03` | `medium` | `release-blocker` | add primary API/auth/public/enum evidence paths | PT-10 fidelity is current cutover evidence | `confirmed at de90987` | `Delivery R7 Finding Classification`; R8 cutover |
| `ARCH-ADH-R8-01` | `medium` | `release-blocker` | distinguish production ownership from explicit local-replica population and add exact evidence | D-04/runtime fidelity is required by the current cutover | `confirmed at 222a8a9` | `Delivery R8 Finding Classification`; R9 architecture |
| `TQ-R8-01` | `high` | `release-blocker` | reject symlinks and preserve them in the clean-copy harness so external content cannot be laundered | publication-tree integrity is required by the current cutover | `confirmed at 222a8a9` | `Delivery R8 Finding Classification`; R9 test-quality |
| `ARCH-ADH-R9-01` | `medium` | `release-blocker` | synchronize every normative state field on the R10 action | governing TODO coherence is required by D-03 | `confirmed at d269bc2` | `Delivery R9 Finding Classification`; R10 architecture |
| `ARCH-ADH-R10-01` | `medium` | `release-blocker` | normalize work-state and required review/audit statuses to PACED enums | deterministic schema and carry-forward are required by D-03 | `confirmed at a72780d` | `Delivery R10 Finding Classification`; R11 architecture |
| `ARCH-ADH-R11-01` | `medium` | `release-blocker` | make the immediate action current at immutable review time | governing TODO temporal coherence is required by D-03 | `confirmed at a973e52` | `Delivery R11 Finding Classification`; R12 architecture |
| `TQ-R11-OBS-01` | `low` | `release-blocker` | update current suite count/status to observed evidence | inaccurate current closeout evidence cannot be promoted | `confirmed at a973e52; no residual follow-up` | `Delivery R11 Finding Classification`; R12 test-quality |
| `ENV-R11-OBS-01` | `low` | `by-design/no-action` | retain Git Bash runner; do not modify Delphi in this TODO | the accepted Git Bash runner passes; WSL is not an acceptance runner and Delphi is read-only | `classified; no follow-up warranted` | `PACED Workspace Alias Contract`; Git Bash PACED-ready evidence |
| `ARCH-ADH-R12-01` | `medium` | `release-blocker` | remap generic observation labels to the exact project taxonomy | finding classification is canonical governance | `confirmed at dc1d869` | `Delivery R12 Finding Classification`; R13 architecture |
| `FINAL-R14-01` | `medium` | `release-blocker` | synchronize all live lifecycle fields after completion and first final review | governing TODO must expose one truthful current state before closeout | `confirmed at 65ae750` | `Final Review R14 Finding Classification`; R16 |
| `FINAL-R15-01` | `medium` | `release-blocker` | synchronize the undated live Blocker Notes with the actual completion/final-review state | no competing lifecycle truth may remain before closeout | `confirmed at 65ae750` | `Final Review R15 Finding Classification`; R16 |
| `CLOSEOUT-TQ-01` | `high` | `release-blocker` | remove active-path assumptions from the persisted closeout test harness | completed lifecycle must pass the same clean-copy/mutation suite before publication | `confirmed technically at 5a1ff88 by R17` | `Closeout Post-Move Finding Classification`; post-move suite |
| `FINAL-R17-01` | `medium` | `release-blocker` | synchronize all live post-move fields with committed candidate and R18/publication as the only remaining actions | completed governing record must not canonize false lifecycle/publication state | `integrated at d057ee3; R18 found residual FINAL-R18-01` | `Final Review R17 Finding Classification`; R17 reviewer |
| `FINAL-R18-01` | `medium` | `release-blocker` | remove instructions to redo the already committed freeze | current immutable HEAD review and publication must be the only live actions | `integrated locally; R19 pending` | `Final Review R18 Finding Classification`; R18 reviewer |

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** o TODO criará validator e testes que sustentam o cutover canônico.
- **Trigger signals in scope:** `changed test logic|architectural change|non-trivial validation risk`
- **Required evidence matrix:** `unit + mutation-style negative fixtures`
- **Package mode:** `bounded-file-set`
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after implementation`
- **Audit status:** `no_material_findings`
- **Findings summary:** delivery R13 returned `GO`; 10 tests passed, validators/extractors/symlink protection remained valid, and no new test-quality finding was raised.
- **Evidence / reference:** immutable delivery R13 baseline `dc1d86985c66e04384e59b582132d2309bae2b76`; fresh R13 test-quality review over `/tmp/monitor-foundation-copilot-r13/review-packet.md`.
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** conclusão remove uma autoridade documental e estabelece outra.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede`
- **Package mode:** `bounded-file-set`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after implementation and test audit`
- **Canonical multi-lane audit protocol:** `n/a`
- **Final review status:** `findings_integrated`
- **Findings summary:** R18 on immutable `d057ee3acbe3a8125d3973bfffa3672e1d4046b0` reconfirmed `CLOSEOUT-TQ-01` resolved and found only P2 `FINAL-R18-01` in two instructions to redo the committed freeze; those instructions now name only R19 and publication.
- **Evidence / reference:** reviewer `/root/foundation_final_review_r18`; packet `/tmp/monitor-foundation-final-r18/review-packet.md`; R19 required on the current immutable HEAD.
- **Waiver authority / reference:** `n/a`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `required`
- **Why this decision:** há aposentadoria completa da autoridade LeadsHug e proibição de fallback interno.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement`
- **Package mode:** `bounded-file-set`
- **Canonical multi-lane audit protocol:** `n/a`
- **Cutover audit status:** `no_material_findings`
- **Findings summary:** delivery R13 returned `GO`: temporal state, canonical taxonomy/carry-forward, 34 exact deletions, lifecycle-aware 38-path tree, ledger through R12, 53 pairs over 45 product paths, frozen fingerprints and Foundation-only scope all passed.
- **Evidence / reference:** immutable delivery R13 baseline `dc1d86985c66e04384e59b582132d2309bae2b76`; fresh R13 cutover review over `/tmp/monitor-foundation-copilot-r13/review-packet.md`.
- **Waiver authority / reference:** `n/a`

## Execution Plan — Approved; Guard-Gated

1. Publicar o freeze sincronizado após `RF-15..RF-16` e executar a última arquitetura/crítica sobre commit/blob/hash exatos.
2. Com review limpo, repetir coerência e scope drift, executar `todo_authority_guard.py --pre-approval` e exigir `preflight-go`.
3. `Concluído em 2026-09-24`: novo `APROVADO` recebido para `D-01..D-05`, `S-01..S-09`, mapa de seis módulos, disposition manifest e validações congeladas.
4. `Concluído`: regras ingeridas, authority guard normal `go` e execução limitada à Foundation.
5. `Concluído com ressalva cronológica`: mutation RED→GREEN reproduzível entregue; o RED inicial imutável não foi preservado e test-first original não é alegado.
6. `Concluído`: camada canônica raiz, scope policy e divisão de autoridades reescritas conforme o manifesto.
7. `Concluído`: seis módulos, contratos, decisões, backlog, políticas e governança reconstruídos nos targets aprovados.
8. `Concluído localmente`: paths `Delete` removidos, suíte/validator/guards locais verdes e remediações R2/R3 integradas.
9. `Concluído com no-go`: delivery R4 executada sobre `1aae0c837fdd16c4675d544e3eb1324f4db55b90`; findings classificados dentro de D-01..D-05.
10. `Concluído localmente`: findings delivery R4 integrados e congelados no commit `cacc054`.
11. `Concluído com no-go`: delivery R5 executada sobre `1e7e73043e697f2e9bf536772cf3717d79f85cbf`; findings classificados dentro de D-01..D-05.
12. `Concluído com no-go`: delivery R6 executada sobre `04b865ea35501d5f59f0e6a9e7d7b953d7d9598d`; findings classificados dentro de D-01..D-05.
13. `Concluído com no-go parcial`: arquitetura R7 retornou `GO`; test-quality/cutover R7 sobre `1374caedafa63935fd390c273a346365ea88109e` encontraram findings e uma rota de modelo inválida, todos classificados no ledger canônico.
14. `Concluído com no-go parcial`: delivery R8 sobre `de909878b014c708fa103dd2d3b9213f0abe1c33` retornou cutover `GO` e os blockers `ARCH-ADH-R8-01`/`TQ-R8-01`, classificados no ledger canônico.
15. `Concluído com no-go parcial`: delivery R9 sobre `222a8a9b0d63c47f002b3b752f2a83bd548260e0` confirmou test-quality/cutover `GO`, confirmou os blockers R8 resolvidos e encontrou somente `ARCH-ADH-R9-01` na sincronização de estado.
16. `Concluído com no-go parcial`: delivery R10 sobre `d269bc269f761de68587abc83813480a23cfd200` confirmou test-quality/cutover `GO`, confirmou `ARCH-ADH-R9-01` resolvido e encontrou somente `ARCH-ADH-R10-01` nos enums PACED.
17. `Concluído com no-go parcial`: delivery R11 sobre `a72780df68156eae85a88a6071989fa3730ded8a` confirmou test-quality/cutover `GO`, confirmou `ARCH-ADH-R10-01` resolvido e encontrou somente `ARCH-ADH-R11-01` no passo temporal; `TQ-R11-OBS-01` foi integrado e `ENV-R11-OBS-01` classificado fora do escopo.
18. `Concluído com no-go parcial`: delivery R12 sobre `a973e5207d52f55cdddb4dd5b8dc8fb72e32f1f3` confirmou test-quality/cutover `GO`, confirmou `ARCH-ADH-R11-01` resolvido e encontrou somente `ARCH-ADH-R12-01` na taxonomia do ledger.
19. `Concluído`: delivery R13 sobre `dc1d86985c66e04384e59b582132d2309bae2b76` retornou `GO` conjunto em arquitetura, test-quality e cutover, sem blocker ou finding novo.
20. `Concluído`: evidência 1:1 consolidada; suíte 10/10, Foundation/TODO validators, diff, authority e completion guards verdes; dívida de verificação adjudicada como `none`; candidato congelado em `92787e564258998aac8643c45a3b8346b03a9fcc`.
21. `Concluído com no-go`: revisão final R14 sobre `92787e564258998aac8643c45a3b8346b03a9fcc` encontrou somente `FINAL-R14-01`, um P2 de coerência temporal no TODO, sem defeito de conteúdo ou runtime.
22. `Concluído com no-go`: a remediação R14 foi congelada em `4124b1f9a821cbdcdd56b9188edd96cb98980ce2`; R15 encontrou somente `FINAL-R15-01` no `Blocker Notes`, sem defeito de conteúdo/runtime.
23. `Concluído`: remediação integral R14/R15 congelada em `65ae75054a06e5e9ebbe2104b78d924bd2fdbc72`; R16 retornou `GO`, confirmou ambos os blockers resolvidos e encontrou zero finding material/P1/P2/release blocker.
24. `Concluído com finding integrado`: guards finais e movimento para `completed/process/` concluídos; ledger/manifest atualizados; a primeira suíte pós-move encontrou `CLOSEOUT-TQ-01`, o harness foi tornado lifecycle-aware e a repetição passou 10/10 em 134.909s.
25. `Concluído com no-go`: candidato pós-move congelado em `5a1ff884ae883e5bd0e50b27d9a463aa5d53085e`; R17 confirmou a correção técnica e encontrou somente `FINAL-R17-01` nos campos temporais.
26. `Concluído com no-go`: `FINAL-R17-01` foi integrado em `d057ee3acbe3a8125d3973bfffa3672e1d4046b0`; R18 reconfirmou a correção técnica e encontrou somente `FINAL-R18-01` em duas instruções de freeze já executado.
27. `Em andamento`: executar R19 sobre o HEAD imutável atual que contém `FINAL-R18-01` e, se limpa, publicar `main`.

### Touched Surfaces

- `uninotas-foundation/*.md`
- `uninotas-foundation/{modules,backlog,decisions,contracts,policies,artifacts,todos,deterministic}/**`
- `uninotas-foundation/local_packages.yaml`
- os aliases PACED existentes no root são preestabelecidos e read-only; este TODO não cria, edita, remove nem versiona paths no repositório do produto.

### Test Strategy

- **Strategy:** `retrofit reproducible mutation RED→GREEN`; original test-first chronology is unverified.
- **Why:** fixtures negativas precisam provar que o guard falha para identidade legada, links inválidos e autoridade concorrente antes da implementação final.
- **Fail-first targets:** trees temporários do validator para ocorrência proibida em superfície ativa, link quebrado, owner canônico ausente e padrões JWT/PII montados em runtime; o corpus persistido permanece elegível ao scan normal.
- **Exact local suite:** `python3 -B -m unittest discover -s deterministic/tests -p 'test_*.py' && python3 -B deterministic/validate_foundation.py --root .`.

### Runtime / Rollout Notes

- Não há migração, feature flag ou rollout de runtime.
- A publicação é atômica no repositório Foundation `main`; o tree candidato deve passar antes do commit final.
- O banco remoto permanece somente leitura durante validações deste TODO.

## Questions To Close

- [x] Nenhuma questão material aberta de escopo; `D-01..D-05` foram confirmadas pelo `APROVADO` renovado e delivery findings são remediações internas ao contrato.

## Rules Acknowledgement / Ingestion

- **Binding ingestion timestamp:** `2026-09-24`, após o `APROVADO` renovado.
- **Touched-surface confirmation:** somente documentação, testes e tooling determinístico local de `uninotas-foundation`; produto/runtime e `delphi-ai` permanecem read-only.
- **Profile scope check:** `Strategic / CTO-Tech-Lead` para o cutover canônico, com handoff já declarado ao `Operational / Coder` somente para criar e validar o guard local; nenhum path `forbidden` ou `unknown` será escrito.

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/main_instructions.md` | autoridade PACED carregada pelo bootloader | separação core genérico vs. verdade local e TODO governado | transportar conteúdo de outro projeto ou executar fora dos gates | Foundation concentra produto; Delphi permanece genérico |
| `delphi-ai/system_architecture_principles.md` | princípios de owner único, contrato explícito e domínio primeiro | `logs` read-only, contratos explícitos, SSoT | inferir stack/capacidade ou duplicar owner | módulos partem do domínio e evidência real |
| `delphi-ai/workflows/docker/delphi-project-setup-method.md` | recalibração PACED de projeto brownfield | classificação de drift e limites inherited/project-owned | declarar calibrated só por presença de arquivos | status real é `needs-normalization` |
| `delphi-ai/workflows/docker/documentation-migration-method.md` | migração de documentação herdada | inventário, gap analysis e owners canônicos | editar legado superficialmente ou importar domínio automaticamente | executar cutover por evidência e template |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | orquestração do lifecycle tático | ordem de gates, aprovação, evidência e closeout | pular fases por conveniência | cada transição fica registrada no TODO |
| `delphi-ai/workflows/docker/todo-contract-refinement-method.md` | contrato `big` precisa matrizes/anchors/decisões | diff estrito, módulos e evidência 1:1 | scope implícito | refinamento antes do authority go |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | `APROVADO` recebido e precisa de evidência persistente | freeze, crítica, coerência e scope drift | tratar aprovação em chat como único gate | execução aguarda gates convergirem |
| `delphi-ai/workflows/docker/todo-execution-boundary-method.md` | controla implementação pós-aprovação | single-writer e authority guard | worktree/checkout auxiliar ou expansão oculta | executor limitado à Foundation |
| `delphi-ai/rules/core/delphi-project-setup-model-decision.md` | pedido explícito de adoção PACED | readiness + recalibração + TODO | feature work com drift material | este TODO é a normalização exigida |
| `delphi-ai/templates/module_template.md` | seis módulos canônicos serão criados | anchors de intent/boundaries, coverage, rules, contracts e cross-module concerns | módulos livres ou espelhos de pastas runtime | validator exige anchors aplicáveis em cada módulo |
| `uninotas-foundation/policies/scope_subscope_governance.md` | policy obrigatória para module ownership | `D-05`, scope único e seis subscopes comprovados | importar tenancy LeadsHug ou expandir scope implicitamente | reescrever antes de consolidar módulos e validar consistência |

## Package-First Assessment

- **Query executed:** `bash delphi-ai/tools/query_packages.sh --project-root /mnt/c/Unifast/MonitorDeNotas --search "validation"`
- **Result:** `0 package(s) found` em 2026-09-24.
- **Decision:** implementar o validator documental local previsto no TODO; não há pacote ecossistêmico ou local reutilizável que satisfaça o contrato congelado de identidade, links, owners, schema e privacy scan.
- **Boundary:** a avaliação não autoriza publicar pacote novo nem alterar registros compartilhados; o helper permanece específico de `uninotas-foundation/deterministic/`.

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `delivery-review`
- **Selected role:** `formal-reviewer`
- **Selected model:** `gpt-5.6-sol`
- **Selected effort:** `xhigh`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `explicit human reference — D-03 + “APROVADO” em 2026-09-24 exige que todo trabalho passe pelo PACED`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Routing guard evidence:** the canonical preflight fields above represent `architecture_adherence` and returned `go`; the supplemental sibling/final routing rows below also returned `go` with no violations on 2026-09-24. Delivery reviewers remain read-only.

| Review kind | Model | Effort | Guard result |
| --- | --- | --- | --- |
| `architecture_adherence` | `gpt-5.6-sol` | `xhigh` | `go` |
| `test_quality_audit` | `gpt-5.6-terra` | `xhigh` | `go` |
| `cutover_integrity_audit` | `gpt-5.6-terra` | `xhigh` | `go` |
| `final_review` | `gpt-5.6-sol` | `xhigh` | `go` |
- **Authority preflight outcome:** `preflight-go`
- **Authority preflight evidence:** `python3 delphi-ai/tools/todo_authority_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md --pre-approval` — zero violations em 2026-09-24.
- **Post-approval authority outcome:** `go`
- **Post-approval authority evidence:** `python3 delphi-ai/tools/todo_authority_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md` — zero violations em 2026-09-24 após aprovação renovada e ingestão vinculante.
- **Waiver / exception reference:** `n/a`

## Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Migração da Foundation | `structure-only documentation governance` | `n/a` | `n/a` | `no` | `no` | inspeção documental, guards e comparação read-only com código | não altera comportamento ou fluxo de usuário |

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `uninotas-foundation / structural validation` | documentos e checks alterados: identidade, links, owner único, privacy patterns e ausência de autoridade concorrente | `python3 -B -m unittest discover -s deterministic/tests -p 'test_*.py' && python3 -B deterministic/validate_foundation.py --root .` | `completion/closeout` | `passed` | post-move: 10 tests `OK` em 134.909s; Foundation/TODO validators `PASS` | harness lifecycle-aware; nenhuma suíte genérica substitui estes checks específicos |

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** o inventário consulta código/documentação com payloads e campos de cliente; uma cópia literal pode persistir PII, JWT ou dados de produção mesmo sem alterar runtime.
- **Attack surface in scope:** credenciais, JWT/query strings, PII de cliente/aluno, payloads brutos, URLs e topologia operacional.
- **Attack simulation decision:** `not_needed`
- **Review evidence:** `DOD-10/VAL-08`; validator de padrões de alto risco; revisão manual de todo artifact/fixture novo; somente exemplos sintéticos ou redigidos.
- **Residual security risk:** `low` após scan e revisão manual, pois detecção automática de PII contextual não é completa.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `none`
- **Why this level:** não há mudança de query, frontend assíncrono, escrita concorrente ou runtime.
- **Current delivery stage at planning review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `EPS-DATA-PATH-CHANGED` | `before_local_implemented` | `EPS-E1` | `not_applicable` | `none` | `none` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `FRC-LIFECYCLE-ASYNC-EFFECT` | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-NON-IDEMPOTENT-WRITE` | `before_local_implemented` | `BCI-INV` | `not_applicable` | `none` | `none` |
| `RLS` | `runtime-load-stress-validation` | `not_needed` | `low` | `RLS-SLO-CLAIM` | `before_production_ready` | `RLS-E1` | `not_applicable` | `none` | `none` |

Cada lane é `not_needed` porque o TODO não altera endpoints, efeitos assíncronos, escritas de backend, filas, SSE, queries, carga ou runtime. Os reason codes são apenas chaves canônicas de matriz; nenhum trigger técnico ocorreu.

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| `origin/main` de `uninotas-foundation` | baseline freeze e publicação final | `healthy; candidate unpublished` | `2026-09-24` | `origin/main` confirmado em `b73b0ebc79daeb74acd6c377b4b307438095c848`; implementação/remediação permanece somente local até os gates finais | publicar apenas após completion/closeout verdes |
| `delphi-ai` local | workflows e guards PACED | `healthy with runner caveat` | `2026-09-24` | `verify_context.sh` via Git Bash passou | scripts CRLF rodam pelo Git Bash; Python guards rodam no WSL |
| PostgreSQL/Railway | somente evidência read-only de arquitetura | `healthy` | `2026-09-24` | `/api/v1/saude` retornou banco `ok` | nenhuma mutação/seed/E2E neste TODO |

## Review and Delivery Gates

- **Review Baseline Freeze:** required before the first planning-side guard/review.
- **Review Scope Drift:** required after review convergence and before `APROVADO`.
- **Independent planning critique:** required because complexity is `big` and the blast radius is cross-module within the Foundation.
- **Authority guard:** must return `go` only after explicit `APROVADO`, rule ingestion and resolved decisions.
- **Completion and closeout guards:** required before `Local-Implemented` or movement to `completed/`.
- **Cutover integrity audit:** required because the work retires one active documentary authority and establishes another.
- **Delivery R13 architecture/test-quality/cutover review:** all three fresh lanes returned `GO` on immutable `dc1d869`; no P1/P2, blocker or new finding remained.
- **Independent final review R16:** `GO` on immutable `65ae750`; `FINAL-R14-01` and `FINAL-R15-01` confirmed resolved; no material finding/P1/P2/release blocker at that baseline.
- **Post-move test correction:** R17 confirmed `CLOSEOUT-TQ-01` resolved at `5a1ff88`; 10/10, validator, 39 ledger rows and manifest move are exact.
- **Final review R17/R18:** technical closeout `GO`; R18 reconfirmed `CLOSEOUT-TQ-01` and only `FINAL-R18-01` temporal wording remains for R19 confirmation.
- **Pre-move closeout guard:** `go` sobre cópia byte-idêntica (`cmp -s`) em path temporário real `foundation_documentation/todos/active/process/`, com `--repo` apontando ao Git real da Foundation; isso compensa o `Path.resolve()` do guard, que elimina o nome do alias e classificaria incorretamente o path direto como `other`.

## TODO Closeout Disposition

- **Disposition:** `move-completed`
- **Disposition reason:** implementação, delivery, completion e closeout técnico estão verdes; `FINAL-R18-01` está integrado e somente R19 precede a publicação.
- **Post-commit/push status:** `technical closeout is committed at 5a1ff884ae883e5bd0e50b27d9a463aa5d53085e; temporal remediation through FINAL-R18-01 is at main@HEAD; origin/main remains at b73b0eb approval checkpoint`
- **Next path/status action:** obter R19 limpa sobre o HEAD imutável atual e publicar `main` em `origin/main`.
