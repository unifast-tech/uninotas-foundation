# TODO — Canonicalizar a Foundation para a arquitetura UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Lifecycle state:** `Active — planning`
- **Created:** `2026-09-25`
- **Owner:** `Delphi / Strategic CTO-Tech-Lead`, sob autoridade humana do usuário

## Context

O produto em execução ainda é documentado como Monitor de Notas, com PostgreSQL `logs` como fonte de toda a experiência. A direção confirmada para UniNotas muda essa autoridade: Smart Notas passa a fornecer todas as notas e documentos; PostgreSQL permanece apenas como evidência de falhas de integração; Unifast e Prosperar são dois contextos fiscais, não tenants. Implementar o adapter NestJS antes de consolidar essa arquitetura criaria conflito entre código e Foundation.

O validador atual também congela exatamente a árvore criada no rebase inicial. Por isso, os artefatos de descoberta já aprovados aparecem como `frozen lifecycle tree mismatch`. A correção do contrato de publicação faz parte deste mesmo cutover canônico, preservando as proteções de privacidade, symlink, legado, identidade e contratos.

## Framing Source & Story Slice

- **Feature brief:** `artifacts/feature-briefs/uninotas-smart-notas-central.md`
- **Primary story ID:** `ST-02`
- **Why this is the right current slice:** a correção canônica é o pré-requisito explícito de `ST-03`; ela resolve uma única conversa de autoridade documental sem alterar o runtime.
- **Direct-to-TODO rationale:** `n/a — feature brief existente`.

## Objective

Estabelecer na Foundation a identidade UniNotas, a topologia `FastPay (Routerfy) -> n8n -> Smart Notas`, a separação entre notas da API e falhas do PostgreSQL, os dois contextos fiscais e os futuros owners de notas, falhas e casos operacionais, distinguindo rigorosamente comportamento atual de arquitetura-alvo e tornando o validador de publicação apto a governar a árvore evolutiva.

## Contract Boundary

- Este TODO define **WHAT** será entregue e o que conta como concluído.
- `Assumptions Preview` e `Execution Plan` definem **HOW** a entrega é atualmente planejada.
- O contrato é **bounded but elastic** somente para refinamentos locais da mesma transição canônica.
- Nova rota, código de produto, schema, migração, configuração runtime ou comportamento de UI exige TODO próprio e aprovação separada.

## Implementation Intent

- **Current delivery:** cutover documental da arquitetura UniNotas e evolução do validador/manifesto da própria Foundation.
- **Planned next steps:** TODO NestJS de leitura Smart Notas por contexto fiscal; TODO de DANFE; TODO React de contexto/cache; TODO de falhas/casos operacionais.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** a Foundation deve declarar a arquitetura aprovada e separar `Current` de `Target` antes que o primeiro adapter de produto seja implementado.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** publicar uma nova baseline pós-remediação de `DEP-CLOSEOUT-01`, executar arquitetura/crítica R8 sem contexto e concluir os guards pré-aprovação.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** o contrato está em refinamento/revisão pré-aprovação; nenhuma implementação canônica ou determinística foi iniciada.
- **Exit condition:** baseline aprovado, implementação validada e gates de entrega concluídos.

## Scope

- [ ] Canonicalizar `UniNotas` como nome do produto e `uninotas` como `core_scope`, preservando `MonitorDeNotas` como nome técnico do repositório nesta entrega.
- [ ] Declarar na constituição `Namespaces: nestjs,react,vite,postgresql,prisma,docker,railway`, refletindo somente a topologia já verificada e mantendo cada capability independente.
- [ ] Registrar a topologia externa confirmada e a propriedade de dados: Smart Notas para notas/documentos, PostgreSQL `logs` somente para falhas de integração.
- [ ] Registrar Unifast e Prosperar como `FiscalIssuerContext`, sem tenancy e sem agregação inicial de notas.
- [ ] Separar explicitamente comportamento atual e arquitetura-alvo nas raízes, decisões, roadmap e módulos afetados.
- [ ] Criar os owners canônicos planejados exatos `modules/fiscal-notes-and-documents.md`, `modules/integration-error-occurrences.md` e `modules/operational-cases.md`.
- [ ] Atualizar a política de scope/subscope e os índices sem inventar módulos de runtime já implementados.
- [ ] Evoluir o validador e seus testes para a nova identidade, módulos e publicação governada, mantendo proteções existentes.
- [ ] Publicar no manifesto os artefatos de descoberta e este TODO sem persistir segredos, valores reais de CNPJ/identificador do provedor, payloads/respostas privadas ou URLs capturadas de documentos.

## Out of Scope

- [ ] Alterar backend, frontend, Prisma, PostgreSQL, Docker, Railway, `.env` ou qualquer configuração runtime.
- [ ] Criar rotas Smart Notas, cache, download de DANFE/XML ou UI de seleção fiscal.
- [ ] Implementar `OperationalCase`, migrar tratamentos ou decidir agrupamento/correlação de falhas.
- [ ] Investigar ou alterar a automação n8n/FastPay.
- [ ] Realizar chamadas adicionais à API Smart Notas ou registrar qualquer valor de credencial/identificador.
- [ ] Renomear repositórios, diretórios de produto/runtime, pacotes, imagens ou serviços técnicos; o rename do arquivo canônico de decisões para UniNotas está explicitamente dentro do escopo.
- [ ] Alterar `delphi-ai`; o suporte standalone já foi entregue separadamente pelos commits Delphi `6dc5bd4` e `0e54e2a` e será apenas consumido/validado nesta entrega.
- [ ] Usar worktrees, checkouts auxiliares, `worker/*` ou `reconcile/*`.

## Delivery Status Semantics

- `Pending`: nenhuma entrega material foi concluída.
- `Local-Implemented`: o cutover documental e o harness foram implementados e validados localmente.
- `Lane-Promoted`: n/a para esta autoridade documental single-branch.
- `Production-Ready`: a entrega foi validada e publicada em `main` após todos os gates.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `uninotas-foundation:main` (autoridade single-branch/single-checkout)
- **Promotion lane path:** `main -> origin/main`
- **Lane-promoted threshold for this TODO:** `origin/main`
- **Production-ready threshold for this TODO:** `origin/main` após gates de conclusão

## Promotion Evidence (Required Before Lane-Promoted / Production-Ready)

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Foundation UniNotas cutover | `main@a5c7ec1` | `n/a — main-only authority` | `n/a` | `origin/main@a5c7ec1` | R6 review baseline published |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `uninotas-foundation` | `.` | `main@0fe906c` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| `uninotas-foundation` | `README.md` | `M` | identidade canônica |
| `uninotas-foundation` | `project_mandate.md` | `M` | mandato UniNotas |
| `uninotas-foundation` | `project_constitution.md` | `M` | topologia e invariantes |
| `uninotas-foundation` | `domain_entities.md` | `M` | vocabulário do domínio |
| `uninotas-foundation` | `system_roadmap.md` | `M` | sequência de entrega |
| `uninotas-foundation` | `technology_baseline.md` | `M` | identidade no baseline observado sem alterar fatos técnicos |
| `uninotas-foundation` | `evolution_lifecycle.md` | `M` | relacionar lifecycle PACED ao estado separado de autoridade runtime |
| `uninotas-foundation` | `contracts/README.md` | `M` | índice deixa de presumir exatamente seis owners |
| `uninotas-foundation` | `decisions/README.md` | `M` | atualizar o índice para a autoridade UniNotas e impedir link legado quebrado |
| `uninotas-foundation` | `decisions/monitor-de-notas-foundation-decisions.md` | `D, R` | aposentar o path canônico legado após migração integral das decisões |
| `uninotas-foundation` | `decisions/uninotas-foundation-decisions.md` | `A, R` | autoridade canônica de decisões UniNotas, preservando histórico pelo Git |
| `uninotas-foundation` | `modules/README.md` | `M` | índice/lifecycle dos owners |
| `uninotas-foundation` | `modules/events-and-classification.md` | `M` | owner current e sucessores target |
| `uninotas-foundation` | `modules/treatments-and-history.md` | `M` | owner current e sucessor target |
| `uninotas-foundation` | `modules/identity-and-team.md` | `M` | no-tenancy e contexto fiscal |
| `uninotas-foundation` | `modules/realtime-invalidation.md` | `M` | current logs invalidation versus target source split |
| `uninotas-foundation` | `modules/operational-monitoring.md` | `M` | current logs summary versus target monitoring split |
| `uninotas-foundation` | `modules/runtime-and-deployment.md` | `M` | current runtime e target external boundary |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `A` | target provider-backed fiscal owner |
| `uninotas-foundation` | `modules/integration-error-occurrences.md` | `A` | target external failure-evidence owner |
| `uninotas-foundation` | `modules/operational-cases.md` | `A` | target application workflow owner |
| `uninotas-foundation` | `policies/scope_subscope_governance.md` | `M` | novos subscopes explícitos |
| `uninotas-foundation` | `policies/query_path_guardrails.md` | `M` | separar current logs queries do target note source |
| `uninotas-foundation` | `policies/validation_evidence_policy.md` | `M` | promover boundary de CNPJ/identifier/document URL |
| `uninotas-foundation` | `artifacts/README.md` | `M` | indexação dos artefatos |
| `uninotas-foundation` | `artifacts/analysis/uninotas-canonical-foundation-transition-delivery-package.md` | `A, M` | pacote bounded para os audits de entrega; derivado e não autoritativo |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-smart-notas-central.md` | `A, M` | framing já produzido e reconciliação ST-02 |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | contrato de publicação |
| `uninotas-foundation` | `todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md` | `A, M` | ledger de descoberta e sequência corrigida |
| `uninotas-foundation` | `todos/active/process/TODO-uninotas-canonical-foundation-transition.md` | `A, M, D, R` | autoridade tática/evidência e origem do closeout final |
| `uninotas-foundation` | `todos/completed/process/TODO-uninotas-canonical-foundation-transition.md` | `A, R` | destino exato autorizado somente no closeout após todos os gates |
| `uninotas-foundation` | `deterministic/validate_foundation.py` | `M` | validador evolutivo fail-closed |
| `uninotas-foundation` | `deterministic/tests/**` | `A, M` | mutações e regressões do validator |

### Not Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| `uninotas-foundation` | `todos/completed/features/**` | `any` | histórias fechadas fora do target exato são imutáveis nesta entrega |
| `uninotas-foundation` | `todos/completed/process/TODO-uninotas-foundation-project-rebase.md` | `any` | processo fechado anterior é imutável nesta entrega |
| `uninotas-foundation` | `deterministic/legacy_reference_exceptions.json` | `any` | ledger histórico congelado não é reescrito |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)

| Diff item | Classification | Evidence / agent defense | Decision | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `guard ainda não executado` | `n/a` | `n/a` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** correções locais de links, índices, fixtures do validador e semântica documental necessárias ao mesmo cutover.
- **Must update or split the TODO:** qualquer código de produto, mudança runtime, regra de autorização, contrato HTTP ou novo objetivo independente.

## Definition of Done

- [ ] `DOD-01` Identidade/mandato usam UniNotas, todos os anchors usam `core_scope=uninotas` e a constituição declara os `Namespaces` verificados, sem renomear o repositório técnico.
- [ ] `DOD-02` Constituição e decisões registram a topologia externa e a separação de fontes aprovada.
- [ ] `DOD-03` Unifast/Prosperar são contextos fiscais explícitos e não tenants.
- [ ] `DOD-04` Registry e módulos distinguem `current_runtime` de `target_planned`, com precedência, predecessor/sucessor e condição de promoção/retirada, sem declarar código futuro como implementado.
- [ ] `DOD-05` Notas/documentos, falhas de integração e casos operacionais têm owners canônicos distintos.
- [ ] `DOD-06` Validator e suíte rejeitam regressões de identidade, decisão/link canônico obsoleto, ownership, tenancy, privacidade, symlink, legado e publicação, além de quebra da bijeção módulo/catálogo, ID/path/transition duplicado, módulo retired ainda ativo/capable, sequence gap, fork, ciclo, predecessor desconhecido, chain edge ou origin inválida, aresta não terminal planned, interseção `owned_capabilities ∩ planned_capabilities`, target com `owned_capabilities`, aresta terminal planned sem exatamente um owner atual/predecessor ou successor membership, capability ativa sem owner, dupla autoridade runtime, successor planejado duplicado e planned membership obsoleto após promoção; fixtures positivas cobrem estado inicial, capability nova, promoção parcial/final, predecessor retirado e segundo hop planned/completed.
- [ ] `DOD-07` Os artefatos atuais pertencem ao manifesto e a validação Foundation passa sem `frozen lifecycle tree mismatch`.
- [ ] `DOD-08` Nenhum segredo, valor real de CNPJ/identificador do provedor, payload/resposta privada ou URL capturada de documento foi persistido; CNPJ válido é coberto deterministicamente e identificador/URL contextual por regra precisa mais revisão de diff.
- [ ] `DOD-09` O roadmap aponta para o TODO NestJS de leitura como próximo slice, sem lhe conceder autoridade antecipada.
- [ ] `DOD-10` O arquivo/índice canônico de decisões migra para UniNotas sem links obsoletos nem reutilização semântica de IDs: D-01..D-05 preservam sua proveniência/handling e D-06..D-11 recebem somente autoridades novas.
- [ ] `DOD-11` Antes de qualquer claim `Local-Implemented`/closeout, o `todo_closeout_guard.py` corrigido reconhece este path como `active` e o scan `--all-active --repo uninotas-foundation` encontra os TODOs ativos reais; falso `go` com `path_state=other` ou `todo_count=0` bloqueia entrega.

## Validation Steps

- [ ] `VAL-01` Executar fail-first e suíte: `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py`.
- [ ] `VAL-02` Executar `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation`.
- [ ] `VAL-03` Executar `'/mnt/c/Program Files/Git/bin/bash.exe' -lc 'cd /c/Unifast/MonitorDeNotas && bash delphi-ai/verify_context.sh'`, runner canônico que evita a limitação CRLF do wrapper sob WSL.
- [ ] `VAL-04` Executar da raiz do workspace `python3 delphi-ai/tools/todo_diff_expectation_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --repo-root uninotas-foundation`, além dos guards Delphi de autoridade, conclusão e cutover definidos neste TODO.
- [ ] `VAL-05` Executar da raiz do workspace `git -C uninotas-foundation diff --check 0fe906c1e496a1d38f1603cf188c224711011c32 --` e `git -C uninotas-foundation diff --name-status --find-renames 0fe906c1e496a1d38f1603cf188c224711011c32 --`.
- [ ] `VAL-06` Após o TODO Delphi separado reparar o guard standalone, executar os dois comandos de closeout deste contrato e verificar semanticamente `path_state=active` no path individual e `todo_count>=1` no scan ativo; exit code/`go` isolado não basta.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01` | Definition of Done | identidade/core scope/Namespaces | doc+test | roots/anchors + `test_identity_core_scope_and_namespaces` | local | planned | sem runtime |
| `DOD-02` | Definition of Done | topologia e source ownership | doc+test | constitution/decisions + `test_source_ownership_split` | local | planned | logs nunca são fallback de nota |
| `DOD-03` | Definition of Done | fiscal context sem tenancy | doc+test | scope/identity + `test_fiscal_context_is_not_tenancy` | local | planned | Unifast/Prosperar não são tenants |
| `DOD-04` | Definition of Done | Current/Target + cadeia de capabilities | doc+test | registry/modules + casos `CAP-*` abaixo | local | planned | inclui multi-hop e catálogo |
| `DOD-05` | Definition of Done | três owners target distintos | doc+test | module index + `test_target_owner_boundaries` | local | planned | limites exclusivos |
| `DOD-06` | Definition of Done | validator fail-closed | test | todos os casos `CAP-*`/`GUARD-*` abaixo | local | planned | cada caso registra diagnóstico esperado |
| `DOD-07` | Definition of Done | publicação sem frozen-tree mismatch | test | manifest + Foundation validator | local | planned | árvore exata vem do manifesto |
| `DOD-08` | Definition of Done | privacidade e nenhum segredo/PII | test+review | `GUARD-PRIV-*` + revisão de diff | local | planned | nenhum valor real em fixture |
| `DOD-09` | Definition of Done | sequência do roadmap | doc+review | `system_roadmap.md` + decisão de aderência | n/a | planned | não autoriza backend |
| `DOD-10` | Definition of Done | migração estável de decisões | doc+test | decision map/index + `test_decision_id_migration_and_links` | local | planned | D-01..D-05 não mudam de significado |
| `DOD-11` | Definition of Done | closeout guard cobre Foundation standalone | external guard+regression | TODO Delphi concluído + path state/count reais | local | planned | precondição externa satisfeita; repetir antes do closeout |
| `VAL-01` | Validation Steps | suíte determinística | test | comando unittest exato | local | planned | registrar duração e RED/GREEN |
| `VAL-02` | Validation Steps | Foundation validator | test | comando validator exato | local | planned | deve passar integralmente |
| `VAL-03` | Validation Steps | PACED readiness | environment | comando Git Bash exato | local | planned | requer `PACED-Ready` |
| `VAL-04` | Validation Steps | guards de autoridade/delivery/cutover | guard | comandos exatos em Commands | local | planned | todos devem retornar go |
| `VAL-05` | Validation Steps | diff baseline-aware | review | dois comandos Git exatos | local | planned | inclui rename detection |
| `VAL-06` | Validation Steps | closeout sem falso go | guard | comando individual + `--all-active --repo uninotas-foundation` | local | planned | preflight provou path_state active e count 2; repetir antes do closeout |

### DOD-06 Validator Case Matrix

Os nomes abaixo são o contrato mínimo de fixtures/builders e testes. Cada teste deve provar o diagnóstico específico, não apenas um exit code agregado.

| Case ID | Polarity | Fixture / builder | Expected assertion / diagnostic |
| --- | --- | --- | --- |
| `CAP-POS-01` | positive | `initial_planned_chain` | cadeia sequence 1 transferida é aceita |
| `CAP-POS-02` | positive | `new_capability_planned` | capability `origin=new`, predecessor nulo e ownerless é aceita |
| `CAP-POS-03` | positive | `partial_promotion` | successor current pode possuir uma capability e planejar outra |
| `CAP-POS-04` | positive | `complete_promotion_retired_predecessor` | predecessor retired conhecido + terminal completed é aceito |
| `CAP-POS-05` | positive | `second_hop_planned` | histórico A→B completed + terminal B→C planned governa B/C |
| `CAP-POS-06` | positive | `second_hop_completed` | histórico A→B e terminal B→C completed governam C somente |
| `CAP-NEG-01` | negative | `owned_planned_overlap` | `owned_capabilities intersects planned_capabilities` |
| `CAP-NEG-02` | negative | `duplicate_current_owner` | `capability has multiple current owners` |
| `CAP-NEG-03` | negative | `planned_terminal_missing_owner` | `planned transfer predecessor is not the current owner` |
| `CAP-NEG-04` | negative | `duplicate_planned_successor` | `capability has multiple planned successors` |
| `CAP-NEG-05` | negative | `transition_sequence_gap` | `capability transition sequence is not contiguous` |
| `CAP-NEG-06` | negative | `transition_fork` | `capability transition chain fork` |
| `CAP-NEG-07` | negative | `transition_cycle` | `capability transition chain cycle` |
| `CAP-NEG-08` | negative | `unknown_module_reference` | `transition references unknown module` |
| `CAP-NEG-09` | negative | `broken_chain_edge` | `transition predecessor does not match prior successor` |
| `CAP-NEG-10` | negative | `completed_with_planned_residue` | `completed capability retains planned membership` |
| `CAP-NEG-11` | negative | `terminal_owner_mismatch` | `terminal completed successor is not sole current owner` |
| `CAP-NEG-12` | negative | `duplicate_catalog_id_or_path` | `module catalog identity/path is not unique` |
| `CAP-NEG-13` | negative | `active_catalog_without_module` | `active module catalog is not bijective with modules` |
| `CAP-NEG-14` | negative | `module_without_active_catalog` | `module has no matching active catalog entry` |
| `CAP-NEG-15` | negative | `retired_module_still_active_or_capable` | `retired module remains active, owned, or planned` |
| `CAP-NEG-16` | negative | `nonterminal_transition_still_planned` | `nonterminal transition must be completed` |
| `CAP-NEG-17` | negative | `duplicate_transition_id` | `transition_id is not unique` |
| `CAP-NEG-18` | negative | `new_origin_after_sequence_one` | `origin new is valid only at sequence one` |
| `CAP-NEG-19` | negative | `new_origin_with_predecessor` | `new capability predecessor must be null` |
| `CAP-NEG-20` | negative | `new_planned_with_preexisting_owner` | `new planned capability already has an owner` |
| `CAP-NEG-21` | negative | `terminal_planned_missing_successor_membership` | `terminal planned successor lacks planned membership` |
| `CAP-NEG-22` | negative | `target_planned_with_owned_capability` | `target_planned module cannot own capability` |
| `CAP-NEG-23` | negative | `active_capability_without_owner` | `active capability has no current owner` |
| `GUARD-ID-01` | negative | `legacy_identity_or_decision_link` | identidade/índice canônico legado é rejeitado |
| `GUARD-TENANCY-01` | negative | `fiscal_context_as_tenant` | contexto fiscal tratado como tenancy é rejeitado |
| `GUARD-PUB-01` | negative | `unmanifested_or_missing_path` | árvore diverge do manifesto |
| `GUARD-SYMLINK-01` | negative | `unexpected_symlink` | symlink fora do contrato é rejeitado |
| `GUARD-LEGACY-01` | negative | `legacy_exception_mutation` | ledger histórico congelado é rejeitado |
| `GUARD-PRIV-01` | negative | `valid_cnpj_value` | CNPJ válido persistido é rejeitado |
| `GUARD-PRIV-02` | negative+review | `captured_provider_identifier_or_document_url` | valor contextual é detectado ou bloqueado pela revisão precisa de diff |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas OpenAPI | fundamenta a arquitetura-alvo | healthy | 2026-09-25 | fingerprint e probes redigidos no ledger | nenhuma chamada nesta entrega |
| Git remote Foundation | necessário para baseline de revisão | healthy | 2026-09-25 | `main`/`origin/main@5a06037`; guard main-only instalado e Git for Windows é o writer válido | nenhum ajuste |
| `DEP-CLOSEOUT-01` Delphi standalone closeout support | impede falso `go` e stale active TODO no closeout | healthy/resolved | 2026-09-25 | TODO Delphi concluído em `6dc5bd4`/`0e54e2a`; comando individual retornou `path_state=active`; `--all-active --repo uninotas-foundation` retornou `todo_count=2`, ambos paths ativos reais e zero violações | consumir a correção já publicada e repetir os dois comandos antes do closeout |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `operational-coder; assurance-tester-quality`
- **Scope-check command:** `bash -lc 'mapfile -t paths < <(git -C uninotas-foundation diff --name-only 0fe906c1e496a1d38f1603cf188c224711011c32 -- | sed "s#^#foundation_documentation/#"); ((${#paths[@]} > 0)) && python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto "${paths[@]}"'`
- **Scope-check interpretation:** `no changed paths detected` é inválido para esta entrega; `allowed` segue o profile e `review required|unknown` deve ser reconciliado pela Handoff Log, não tratado como passe silencioso.

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | implementar alterações determinísticas após congelamento estratégico | `deterministic/**` | planned |
| operational-coder | strategic-cto | consolidar constituição/mandato/decisões | roots, modules, policies | planned |
| strategic-cto | assurance-tester-quality | auditar harness e cutover | TODO + diff + tests | planned |

## Complexity

- **Level (`small|medium|big`):** `big`
- **Checkpoint policy:** `section-by-section`
- **Why this level:** altera identidade, ownership, módulo/scope e o harness fail-closed da autoridade documental, com blast radius transversal na Foundation.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `modules/events-and-classification.md`
- **Secondary module docs:** `modules/treatments-and-history.md`, `modules/runtime-and-deployment.md`, `modules/identity-and-team.md`, `modules/realtime-invalidation.md`, `modules/operational-monitoring.md`
- **Planned decision promotion targets:** `project_mandate.md`, `project_constitution.md`, `domain_entities.md`, `system_roadmap.md`, `decisions/`, `modules/`, `policies/scope_subscope_governance.md`
- **Module decision consolidation targets:** `modules/fiscal-notes-and-documents.md`, `modules/integration-error-occurrences.md`, `modules/operational-cases.md` e os seis módulos atuais afetados.

## Decision Pending (Resolve Before Freeze)

- [x] `DEP-CLOSEOUT-01 — resolvida pelo TODO Delphi standalone concluído em 0e54e2a; a correção 6dc5bd4 tornou o guard compatível com a autoridade Foundation e os probes reais confirmaram path_state=active e todo_count=2`.

## Planned Module Registry Contract

O JSON machine-readable de `policies/scope_subscope_governance.md` terá `core_scope=uninotas`, uma coleção ativa `modules`, um catálogo persistente `module_catalog` e uma coleção ordenada `capability_transitions`. Cada módulo ativo declara `subscope`, `path`, `runtime_authority_state`, `owned_capabilities` e `planned_capabilities`. Cada entrada do catálogo declara `module_id`, `path` e `catalog_state=active|retired`; `module_id` e `path` são globalmente únicos. Existe uma bijeção exata entre `modules` e entradas `active` do catálogo, com mesmo ID/path. Uma entrada `retired` não pode coexistir em `modules`, possuir ou planejar capability, nem compartilhar ID/path com outra entrada. Cada transição declara `transition_id`, `capability_id`, `sequence`, `origin=transferred|new`, `transition_state=planned|completed`, `predecessor` e `successor`; `transition_id` é globalmente único. `predecessor=null` e `origin=new` são válidos somente em `sequence=1`; toda aresta posterior usa `origin=transferred`. `runtime_authority_state=current_runtime|target_planned` é um eixo distinto do lifecycle PACED de `evolution_lifecycle.md`; ele responde somente qual módulo possui autoridade sobre comportamento executável observado. Um `target_planned` sempre tem `owned_capabilities=[]`; sua intenção aparece somente em `planned_capabilities`. Um módulo `current_runtime` pode possuir capabilities já promovidas e manter outras em `planned_capabilities`, desde que os conjuntos sejam disjuntos.

Os IDs de capability são estáveis entre predecessor e successor: `note_read_model`, `integration_error_read_model` e `operational_workflow` têm `origin=transferred` e não mudam durante a transferência. `fiscal_document_read` tem `origin=new`, sem predecessor. Para cada módulo, `owned_capabilities ∩ planned_capabilities = ∅`. A cadeia de cada capability tem `sequence` inteira, única e contígua iniciando em `1`; a aresta `n+1` deve ter `predecessor=successor` da aresta `n`; nenhum fork, ciclo, alias, gap ou módulo ausente do `module_catalog` é válido. Toda aresta não terminal deve estar `completed`; somente a aresta terminal (maior `sequence`) governa ownership/planned atuais. Arestas concluídas anteriores preservam proveniência, mas não exigem que seus successors continuem owners. Toda capability ativa tem exatamente um owner; nenhuma capability pode existir apenas em transições concluídas sem owner terminal.

Quando a aresta terminal está `planned`, uma transferência exige exatamente um owner `current_runtime` no predecessor ativo e exatamente um planned membership no successor ativo; o successor deve existir em `modules`. Uma capability nova na primeira aresta exige zero owners atuais, exatamente um planned membership no successor, `origin=new` e `predecessor=null`. Uma nova aresta multi-hop só pode ser acrescentada depois que a anterior está `completed`; ela usa `origin=transferred` e parte do owner current anterior.

Promoção é atômica por capability: no mesmo diff, o TODO implementador remove o ID de `owned_capabilities` do predecessor quando `origin=transferred`, remove o ID de `planned_capabilities` do successor, adiciona o ID a `owned_capabilities` do successor, muda a aresta terminal para `completed` e atualiza `runtime_authority_state` e index aplicáveis. Em uma aresta terminal `completed`, o successor deve existir como `current_runtime`, ser o único owner e não pode conservar planned membership. Predecessor/successor de qualquer aresta histórica permanecem no `module_catalog`; um módulo pode virar `retired` apenas quando não possui nem planeja capabilities. Um predecessor com capabilities restantes continua `current_runtime`; sem nenhuma, sai de `modules`, mas permanece `retired` no catálogo. Promoção parcial é válida: o successor passa a `current_runtime`, possui as capabilities concluídas e mantém capabilities ainda `planned` em seu conjunto planejado. Na segunda transferência `A -> B -> C`, a aresta histórica concluída `A -> B` permanece válida mesmo após B deixar de ser owner; somente a aresta terminal `B -> C` determina owner/planned atuais.

| Transition ID | Capability ID | Sequence | Origin | State at this cutover | Predecessor | Successor |
| --- | --- | ---: | --- | --- | --- | --- |
| `note-read-model-001` | `note_read_model` | 1 | `transferred` | `planned` | `events-and-classification` | `fiscal-notes-and-documents` |
| `integration-error-read-model-001` | `integration_error_read_model` | 1 | `transferred` | `planned` | `events-and-classification` | `integration-error-occurrences` |
| `operational-workflow-001` | `operational_workflow` | 1 | `transferred` | `planned` | `treatments-and-history` | `operational-cases` |
| `fiscal-document-read-001` | `fiscal_document_read` | 1 | `new` | `planned` | `null` | `fiscal-notes-and-documents` |

| Subscope / path | Runtime authority state | Owned / planned capability IDs | Predecessor/successor handling |
| --- | --- | --- | --- |
| `events-and-classification` / `modules/events-and-classification.md` | `current_runtime` | owned: `note_read_model`, `integration_error_read_model`; planned: none | successors fiscais/erros; IDs saem separadamente |
| `treatments-and-history` / `modules/treatments-and-history.md` | `current_runtime` | owned: `operational_workflow`; planned: none | successor `operational-cases` após migração aprovada |
| `identity-and-team` / `modules/identity-and-team.md` | `current_runtime` | `authentication`, `team_profiles` | preservar; futuras permissões por contexto exigem TODO |
| `realtime-invalidation` / `modules/realtime-invalidation.md` | `current_runtime` | `legacy_log_invalidation` | preservar; adaptar fontes em TODO futuro |
| `operational-monitoring` / `modules/operational-monitoring.md` | `current_runtime` | `legacy_log_monitoring` | preservar; separar métricas em TODO futuro |
| `runtime-and-deployment` / `modules/runtime-and-deployment.md` | `current_runtime` | `runtime_topology`, `health_read` | preservar fatos observados; registrar alvo sem inventar writer |
| `fiscal-notes-and-documents` / `modules/fiscal-notes-and-documents.md` | `target_planned` | owned: none; planned: `note_read_model`, `fiscal_document_read` | predecessor `events-and-classification` para `note_read_model`; document read é novo |
| `integration-error-occurrences` / `modules/integration-error-occurrences.md` | `target_planned` | owned: none; planned: `integration_error_read_model` | predecessor `events-and-classification`; writer/filter desconhecido |
| `operational-cases` / `modules/operational-cases.md` | `target_planned` | owned: none; planned: `operational_workflow` | predecessor `treatments-and-history` |

## Decisions (Resolved Before Freeze)

Os IDs `TD-*` pertencem somente a este contrato tático e não reutilizam os IDs estáveis do arquivo canônico de decisões.

- [x] `TD-01` O nome canônico do produto e o `core_scope` serão `UniNotas`/`uninotas`; o repositório técnico permanece `MonitorDeNotas` nesta entrega.
- [x] `TD-02` Smart Notas é a fonte completa das notas e documentos; PostgreSQL `logs` é somente evidência de falhas de integração.
- [x] `TD-03` Unifast e Prosperar são `FiscalIssuerContext` independentes, nunca tenants, organizações ou agregação implícita.
- [x] `TD-04` O registry usará `runtime_authority_state=current_runtime|target_planned`, distinto do lifecycle PACED, e `capability_transitions` persistentes com `planned|completed`. IDs estáveis transferem atomicamente; planned nunca concede autoridade; as regras pré/pós-promoção e de capability nova são as congeladas no registry contract.
- [x] `TD-05` Os owners alvo exatos são: `fiscal-notes-and-documents` para fatos/documentos do provedor; `integration-error-occurrences` para evidência externa, normalização e correlação determinística; `operational-cases` para workflow, membership, tratamento e autoria da aplicação.
- [x] `TD-06` `artifacts/publication-manifest.txt` será o único inventário exato da árvore; o validator manterá singletons/famílias/status permitidos, derivará o registry de módulos do scope policy + metadata dos módulos e isolará o ledger histórico do inventário geral de TODOs, sem duplicar a árvore completa em Python.
- [x] `TD-07` O writer/filter externo de falhas permanece desconhecido nesta entrega; a Foundation pode afirmar somente o alvo PostgreSQL read-only/error-evidence e não pode nomear n8n ou outro writer sem evidência posterior.

## Frozen Decision Coherence Matrix (1:1)

| Decision | Prior decision / module reference | Handling | Evidence / intended consolidation |
| --- | --- | --- | --- |
| `TD-01` | foundation decision `D-01`; scope policy `monitor-de-notas` | Supersede (Intentional) | canonical `D-06`; identity roots + `core_scope=uninotas` + todos os module anchors |
| `TD-02` | foundation decision `D-04`; events ownership | Supersede (Intentional) | canonical `D-07`; constitution + current/target source matrix |
| `TD-03` | foundation decision `D-05`; identity no-tenancy | Preserve | canonical `D-05` + `D-08`; scope policy + identity module |
| `TD-04` | `evolution_lifecycle.md` capability lifecycle | Preserve | canonical `D-09`; declare separate runtime-authority axis and relationship |
| `TD-05` | events/treatments current ownership | Supersede (Intentional) | canonical `D-10`; three exact target module paths/boundaries |
| `TD-06` | foundation decision `D-02`; frozen validator tree | Preserve + Extend | canonical `D-02` + `D-11`; preserve Git-history recovery while making manifest sole active inventory |
| `TD-07` | discovery decision `SD-05` + confirmed baseline (writer/filter não identificado) | Preserve | canonical `D-07`; explicit unknown in feature brief, discovery ledger, runtime/target docs |

### Canonical Decision ID Migration

O novo arquivo `decisions/uninotas-foundation-decisions.md` preservará os IDs existentes e acrescentará novos IDs; nenhum ID antigo recebe significado diferente.

| Current canonical ID | Current meaning | Migration handling | Resulting canonical authority |
| --- | --- | --- | --- |
| `D-01` | Monitor de Notas é o produto canônico | Supersede (Intentional) | `D-01` permanece como registro superseded por `D-06` (UniNotas/`uninotas`; repo técnico preservado) |
| `D-02` | documentos aposentados saem da árvore; Git é recovery | Preserve | `D-02` mantém o mesmo significado; `D-11` acrescenta manifesto como inventário ativo único |
| `D-03` | Foundation possui verdade do produto; Delphi possui PACED | Preserve | `D-03` mantém ID e significado sem colisão com contexto fiscal |
| `D-04` | Routerfy é declarado writer e `logs` é fonte do monitor | Supersede (Intentional) | `D-04` permanece histórico/superseded por `D-07`, que separa Current/Target e mantém writer/filter desconhecido |
| `D-05` | um product scope e nenhuma business tenancy | Preserve | `D-05` mantém o mesmo significado; `D-08` acrescenta dois contextos fiscais sem tenancy |
| `n/a` | nova autoridade runtime por capability | Add | `D-09` |
| `n/a` | novos owners alvo | Add | `D-10` |

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `decisions#D-01` | produto Monitor de Notas | Supersede (Intentional) | `decisions/monitor-de-notas-foundation-decisions.md` |
| `decisions#D-04` | `logs` sustenta toda observação do monitor | Supersede (Intentional) | `project_constitution.md#invariants` |
| `decisions#D-05` | sem business tenancy | Preserve | `policies/scope_subscope_governance.md` |
| `events#ownership` | eventos de `logs` são o read model completo | Supersede (Intentional) | `modules/events-and-classification.md#ownership-invariant` |
| `treatments#ownership` | tratamento é ligado somente a `ref_id` | Supersede (Intentional) | `modules/treatments-and-history.md#specification` |
| `runtime#logs` | produção `logs` é externa e read-only | Preserve | `modules/runtime-and-deployment.md#observed-runtime-contract` |
| `identity#no-tenancy` | não há business tenancy | Preserve | `modules/identity-and-team.md#module-intent--boundaries` |
| `realtime#logs-invalidation` | polling/LISTEN atuais invalidam a experiência baseada em logs | Preserve | `modules/realtime-invalidation.md#specification` |
| `monitoring#logs-summary` | monitor atual resume classificações de logs | Preserve | `modules/operational-monitoring.md#specification` |

## Decision Baseline (Frozen Before Implementation)

- [x] `TD-01` UniNotas/`uninotas` são identidade e core scope canônicos; o nome técnico do repositório não muda.
- [x] `TD-02` Toda nota/documento vem da Smart Notas; `logs` nunca é fallback ou espelho de notas bem-sucedidas.
- [x] `TD-03` O contexto fiscal faz parte de identidade, resolução de credencial e isolamento, sem criar tenancy.
- [x] `TD-04` O eixo de autoridade runtime, IDs estáveis, proveniência persistente e condições pré/pós-promoção impedem overlap, gap ou planned membership residual sem competir com o lifecycle PACED.
- [x] `TD-05` Os três paths/owners alvo e seus limites exclusivos são os definidos acima; `OperationalCase` não altera fatos das fontes.
- [x] `TD-06` Manifesto é a única enumeração exata; código valida famílias/singletons/semântica/privacidade e não mantém uma segunda cópia da árvore.
- [x] `TD-07` O writer/filter de falhas não é pré-condição do cutover Current/Target enquanto permanecer explicitamente desconhecido e bloquear apenas o futuro error-adapter.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** a entrega supersede identidade, source ownership e arquitetura modular, além de corrigir um validator de cutover que bloqueia evolução normal.
- **Deviation / debt being retired:** Foundation afirma `logs` como fonte completa e valida apenas a árvore exata do rebase inicial.
- **Target steady-state after closeout:** UniNotas com registry `current_runtime|target_planned`, precedência e sucessão explícitas, owners alvo exclusivos e validação evolutiva fail-closed.
- **Temporary exceptions allowed:** documentos de comportamento atual podem conservar Monitor de Notas/rotas atuais apenas quando marcados como `Current` e sem autoridade sobre o alvo.
- **Cutover / removal condition:** todas as referências canônicas não-históricas aderem a TD-01..TD-07 e ao mapeamento canônico D-01..D-11, e a suíte de mutação passa.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| current-versus-target runtime-authority axis | TD-04 | Foundation | evita declarar capacidade não implementada ou dois owners runtime ativos sem redefinir lifecycle PACED |
| source ownership split | TD-02 | modules/domain | impede fallback silencioso em logs de sucesso |
| context is not tenancy | TD-03 | scope/domain | impede vazamento conceitual e técnico |
| manifest + semantic guards | TD-06 | deterministic | permite evolução sem perder fail-closed |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| `logs` como base de notas | ownership scanner/test | contradiz TD-02 | nenhuma |
| Unifast/Prosperar como tenants | scope policy/test | contradiz TD-03 | nenhuma |
| documento alvo rotulado Current sem código | status contract/test | cria falsa verdade | nenhuma |
| árvore exata duplicada no manifesto e no Python | mutation test | repete o bloqueio atual e cria duas autoridades | nenhuma |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | Foundation semantics | `test_validate_foundation.py` | identity/source/tenancy/current-target drift | implement-in-this-todo | mutation GREEN |
| guard | publication tree | `validate_foundation.py` + manifest | arquivo não governado, symlink, privacidade | implement-in-this-todo | validator GREEN |
| test | privacy boundary | valid formatted/compact CNPJ + contextual provider-ID/document-URL mutations | captured business/provider values without banning official docs or generic IDs | implement-in-this-todo | mutation GREEN + bounded diff review |
| review | architecture | independent architecture/adherence review | supersede incompleto | implement-in-this-todo | review artifacts |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `R7 teve seus achados locais integrados e DEP-CLOSEOUT-01 foi resolvida externamente; nova arquitetura R8 sem contexto é obrigatória sobre a baseline pós-remediação`
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`
- **No-go handling:** retornar ao ciclo afetado; não solicitar aprovação nem concluir com divergência aberta.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** a revisão altera decisões canônicas e precisa de pacote imutável.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `main`
- **Baseline commit:** `a5c7ec1ae52d5423027b51cc8e133201f204cd94`
- **Baseline push reference:** `origin/main`
- **Gate status:** `not_run`
- **Findings summary:** R7 foi integrado e a dependência Delphi foi resolvida; falta publicar a baseline R8 imutável que será submetida às revisões pré-aprovação.
- **Evidence / reference:** baseline anterior `origin/main@a5c7ec1`; resolução externa Delphi `6dc5bd4` + `0e54e2a`; novo commit Foundation pendente.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** decisões materiais devem permanecer idênticas ao baseline revisado.
- **Trigger stage:** `after planning reviews converge and before APROVADO`
- **Baseline source:** `Gate: Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `template canonical set`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Gate status:** `not_run`
- **Findings summary:** a medição anterior retornou zero seções materiais alteradas contra o baseline então vigente; a resolução de DEP-CLOSEOUT-01 exige nova baseline e nova medição R8.
- **Evidence / reference:** `uninotas_architecture_opinion_r7` + `uninotas_plan_critique_r7`; repetir após freeze R8.
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] Nome canônico: `UniNotas`.
- [x] Repositório técnico: permanece `MonitorDeNotas` nesta entrega.
- [x] Contextos fiscais: Unifast e Prosperar, sem tenancy.
- [x] Lista agregada: fora da primeira entrega.
- [x] Fonte das notas: Smart Notas somente.
- [x] Papel do PostgreSQL: falhas de integração somente.
- [x] Corrigir o falso `go` do closeout guard standalone (`DEP-CLOSEOUT-01`): TODO Delphi concluído em `0e54e2a`, correção em `6dc5bd4` e probes reais verdes.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `none` | Não há hipótese viva: ausência de mudança runtime é boundary verificável; o mismatch é fato observado; identidade técnica é TD-01 | Scope, diff contract, `validate_foundation.py` e TD-01 | n/a | High | Keep as Assumption |

## Execution Plan

### Touched Surfaces

- `uninotas-foundation` roots, decisions, modules, policies, artifact index/manifest, TODOs e `deterministic/**`.

### Ordered Steps

1. Escrever testes de mutação fail-first para TD-01..TD-07, migração D-01..D-11, eixo de autoridade runtime/IDs estáveis e o novo contrato de publicação.
2. Atualizar identidade, mandato, constituição, entidades, decisões e roadmap com separação Current/Target.
3. Criar os três owners alvo e atualizar módulos existentes, index e scope policy.
4. Tornar o manifesto a única enumeração exata; extrair validadores puros para registry/privacidade/ownership e manter poucos testes full-tree, sem enfraquecer symlink, legado ou ownership.
5. Consumir a resolução já publicada de `DEP-CLOSEOUT-01` e repetir os probes de path state/count reais antes de qualquer claim `Local-Implemented` ou closeout.
6. Executar a suíte Foundation, validator, PACED readiness e guards de entrega.
7. Submeter diff consolidado às revisões independentes exigidas e promover decisões estáveis.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** o validator é o harness arquitetural; cada semântica precisa de mutação negativa antes do cutover.
- **Fail-first target(s):** identidade/core scope UniNotas, source split, context-not-tenant, runtime-authority/lifecycle separation, módulo/catálogo ausente ou duplicado, sequence gap, fork/ciclo, predecessor desconhecido, chain edge inválida, interseção owned/planned, target com owned capability, aresta terminal planned sem exatamente um owner atual ou successor planejado, capability ativa sem owner, dupla autoridade pelo mesmo ID, successor planejado duplicado, planned membership residual, owner incompatível com aresta terminal, capability nova legítima, predecessor retirado legítimo, segundo hop planned/completed, manifesto único, CNPJ válido e URL/identificador privado contextual.
- **`D-T01` evidence layer:** validadores puros + fixtures mínimas são a camada primária para semântica de registry, decisões e privacidade.
- **`D-T02` compatibility layer:** poucos testes full-tree comprovam manifesto, links, symlinks, legado e composição real da Foundation.
- **`D-T03` topology/exclusion:** nenhum banco, API, browser, container ou dado fiscal real é necessário; substituir essa ausência por mock não acrescenta prova.
- **`D-T04` gate:** cada caso CAP/GUARD deve falhar antes da implementação correspondente e passar depois, com diagnóstico específico; suíte agregada sozinha não satisfaz o critério.

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Why now:** não é bugfix runtime; a falha `frozen lifecycle tree mismatch` já está objetivamente reproduzida.
- **Target symptom:** `n/a`
- **Allowed surfaces:** `none`
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical project docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status:** `not_run`
- **Findings summary:** `n/a`

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation cutover | validator e contrato canônico mudam; sem runtime/UI | n/a | n/a | yes | no | RED/GREEN das fixtures positivas/negativas + validator + reviews | mutation lane é determinística e não exige backend real |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation deterministic suite | validator e testes mudam | TD-01..TD-07, migração D-01..D-11 e mutações negativas/positivas | fixtures mínimas + poucos testes full-tree; sem dados reais | `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py` | Local-Implemented | planned | command output + duração | evitar crescimento multiplicativo sobre baseline observado ~179s |
| Foundation validator | publicação muda | árvore canônica completa | checkout consolidado | `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation` | Local-Implemented | planned | command output | deve eliminar mismatch |
| PACED readiness | integração do alias/artefatos | contexto continua inicializável | Git Bash aceito | `'/mnt/c/Program Files/Git/bin/bash.exe' -lc 'cd /c/Unifast/MonitorDeNotas && bash delphi-ai/verify_context.sh'` | Local-Implemented | planned | command output | runner canônico executável; wrapper WSL isolado por CRLF |

### Runtime / Rollout Notes

- Sem runtime, migração, feature flag ou segredo. Rollout é somente documental e segue lanes Git.

## Plan Review Gate

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
  - **Evidence:** `deterministic/validate_foundation.py:EXPECTED_COMMON_FILES` e erro observado `frozen lifecycle tree mismatch`.
  - **Why it matters now:** a árvore congelada impede que a Foundation governe novos TODOs e artefatos legítimos.
  - **Option A (Recommended):** manifesto como única enumeração exata; Python mantém singletons/famílias/status e deriva registry de módulos do scope policy + metadata, sem copiar a árvore completa.
    - **Effort/Risk/Blast/Maintenance:** medium/medium/cross-module/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** acrescentar manualmente cada novo caminho à constante e ao manifesto.
    - **Effort/Risk/Blast/Maintenance:** low/high/local/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Option C (Do Nothing):** conservar o bloqueio.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A congelada em TD-06; adição legítima exige mudança explícita do manifesto e aprovação nas famílias/semântica permitidas.

- **Issue ID:** `ARCH-02`
  - **Severity:** `high`
  - **Evidence:** `project_constitution.md#invariants` versus feature brief `Confirmed Direction`.
  - **Why it matters now:** substituir a verdade atual pela futura sem rotulagem faria a documentação mentir até o código migrar.
  - **Option A (Recommended):** registry `current_runtime|target_planned`, matriz de precedência/sucessão e condição de promoção/retirada, refletidos nas seções de módulo.
    - **Effort/Risk/Blast/Maintenance:** medium/low/cross-module/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** publicar somente o alvo como atual.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/medium.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Option C (Do Nothing):** manter a autoridade antiga e bloquear backend.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A, única que preserva verdade observada e direção aprovada.

- **Issue ID:** `SEC-01`
  - **Severity:** `medium`
  - **Evidence:** `DOD-08` versus os patterns atuais em `deterministic/validate_foundation.py`.
  - **Why it matters now:** CNPJ e URL privada capturada ainda não têm cobertura objetiva, enquanto “ID” genérico causaria falso positivo.
  - **Option A (Recommended):** detectar CNPJ formatado/compacto válido; rejeitar identifier/URL somente em contexto de valor capturado/provedor e complementar com diff review.
    - **Effort/Risk/Blast/Maintenance:** medium/low/local/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** banir qualquer número longo ou URL.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** regresses/regresses/regresses.
  - **Option C (Do Nothing):** depender apenas de revisão humana.
    - **Effort/Risk/Blast/Maintenance:** low/medium/local/medium.
    - **Performance/Elegance/Structural:** neutral/neutral/regresses.
  - **Recommendation:** Option A, refletida em DOD-08 e no harness.

- **Issue ID:** `TEST-01`
  - **Severity:** `medium`
  - **Evidence:** suíte atual observada em aproximadamente 179 segundos e cópias/full scans por mutação em `deterministic/tests/test_validate_foundation.py`.
  - **Why it matters now:** novas matrizes de mutação podem tornar o feedback local impraticável.
  - **Option A (Recommended):** extrair validadores puros, usar fixtures mínimas e manter poucos testes end-to-end full-tree com duração registrada.
    - **Effort/Risk/Blast/Maintenance:** medium/low/local/low.
    - **Performance/Elegance/Structural:** improves/improves/improves.
  - **Option B:** apenas adicionar mutações ao harness atual.
    - **Effort/Risk/Blast/Maintenance:** low/medium/local/high.
    - **Performance/Elegance/Structural:** regresses/regresses/neutral.
  - **Option C (Do Nothing):** não adicionar cobertura.
    - **Effort/Risk/Blast/Maintenance:** low/high/local/medium.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A como obrigação de entrega, sem SLO rígido inventado.

### Failure Modes & Edge Cases

- [ ] Validator aceita arquivo não manifestado ou symlink.
- [ ] Termo UniNotas é atualizado, mas decisões/índices continuam Monitor de Notas sem rótulo histórico/current.
- [ ] `logs` permanece fallback implícito para notas.
- [ ] Fiscal context é confundido com tenancy.
- [ ] Novo módulo é marcado Current antes de existir no produto.
- [ ] Testes persistem exemplos que parecem credenciais ou dados pessoais.
- [ ] A suíte de mutação repete cópias/full scans e cresce muito além do baseline de aproximadamente 179 segundos.

### Residual Unknowns / Risks

- [ ] O writer/filter exato das falhas no PostgreSQL permanece investigação posterior, explicitamente não bloqueia este cutover e não será inventado aqui.
- [ ] Permissões por contexto, identidade opaca da nota e DANFE continuam decisões dos próximos TODOs.

### Diagnostic Review Finding Resolution

Os pareceres executados sobre a branch indevida são diagnóstico útil, mas não satisfazem os gates formais. Ambos serão repetidos por revisores frescos sobre um baseline válido em `main`.

| Finding ID | Source | Resolution | Evidence / rationale |
| --- | --- | --- | --- |
| `CRIT-01` | plan critique | Integrated | autoridade restaurada em `main`; branch remota/local removida; guard main-only instalado |
| `CRIT-02` | plan critique | Integrated | SHA incorreta descartada; baseline válido publicado em `main` |
| `ARCH-01` | both | Integrated | TD-04 congela eixo de autoridade runtime, precedência, sucessão e promoção/retirada |
| `ARCH-02` | both | Integrated | TD-06 congela manifesto como inventário exato único e registry derivado |
| `DISC-01` | both | Integrated | AMB-11/G-23/ST-02 revisados; writer permanece desconhecido e bloqueia apenas error-adapter |
| `COHERENCE-01` | plan critique | Integrated | Frozen Decision Coherence Matrix cobre TD-01..TD-07; module baseline cobre os seis owners atuais |
| `SEC-01` | both | Integrated | DOD/harness distinguem CNPJ determinístico de ID/URL contextual |
| `DIFF-01` | plan critique | Integrated | globs de decisions/modules/feature-brief/TODOs foram substituídos por paths exatos |
| `ASSUME-01` | plan critique | Integrated | hipóteses redundantes removidas; decisões/fatos/constraints assumem seus owners corretos |
| `TEST-01` | both | Integrated | fixtures mínimas, validadores puros e duração viram obrigação de entrega |
| `ARCH-R2-01` | formal architecture review | Integrated | transferências atômicas por capability permitem promoção fiscal antes do error-adapter |
| `ARCH-R2-02` | formal architecture review | Integrated | matriz congelada agora é 1:1 por TD-01..TD-07 |
| `DIFF-R2-01` | both formal reviews | Integrated | heading canônico, único repo declarado e roots/policies/contracts omitidos classificados |
| `LIFECYCLE-R2-01` | formal critique | Integrated | `runtime_authority_state` é eixo separado e explicitamente relacionado ao lifecycle PACED |
| `DISC-R2-01` | formal critique | Integrated | n8n possui apenas orchestration; writer PostgreSQL permanece desconhecido |
| `STATE-R2-01` | formal critique | Integrated | work state e próximos passos sincronizados para review/fresh baseline |
| `TEMPLATE-R2-01` | formal critique | Integrated | module template adicionado à ingestão obrigatória |
| `ARCH-R3-01` | both formal reviews | Integrated | capability IDs estáveis + planned/owned tornam transferências e overlaps verificáveis |
| `ARCH-R3-02` | formal architecture review | Integrated | toda terminologia congelada reserva lifecycle ao PACED e usa eixo/estado para runtime authority |
| `SCOPE-R3-01` | formal architecture review | Integrated | TD-01 fixa `core_scope=uninotas` e atualiza todos os anchors/validator |
| `STATE-R3-01` | formal critique | Integrated | status, next step, gate evidence e baseline preparados para freeze R3 |
| `ARCH-R4-01` | formal architecture review + critique | Integrated | `capability_transitions` congela origem, predecessor e successor por ID; invariantes distinguem transferências de capability nova e tornam gap/overlap/planned residual rejeitáveis |
| `DIFF-R4-01` | formal architecture review | Integrated | VAL-04 e Commands registram o comando executável com TODO path e repo root corretos |
| `COHERENCE-R4-01` | formal architecture review | Integrated | TD-07 agora preserva explicitamente a descoberta `SD-05` e seu unknown de writer/filter |
| `STATE-R4-01` | both formal reviews | Integrated | next step, review evidence, drift e closeout avançam para freeze/convergência R4 |
| `IDENTITY-R4-01` | formal critique | Integrated | decisão canônica migra para `decisions/uninotas-foundation-decisions.md`; path legado é removido e fica recuperável no Git |
| `ARCH-R5-01` / `CAPABILITY-TRANSITION-01` | both formal reviews | Integrated | `transition_state=planned|completed`, proveniência persistente e invariantes de promoção parcial/final tornam estados pré/pós determinísticos |
| `DEC-R5-01` / `DECISION-MIGRATION-01` | both formal reviews | Integrated | IDs táticos viram `TD-*`; D-01..D-05 mantêm significado/proveniência e D-06..D-11 recebem as novas autoridades |
| `DIFF-R5-01` / `DECISION-RENAME-01` | both formal reviews | Integrated | decisions index, rename `R`, target exato de closeout e comandos baseline-aware entram no contrato |
| `TOPO-R5-01` | formal architecture review | Integrated | constituição declarará os sete Namespaces observados sem implicações entre capabilities |
| `PCV-R5-01` | formal architecture review | Integrated | as quatro rows pcv-1 incluem todos os campos obrigatórios e rationale de ausência de superfície |
| `CMD-R5-01` | formal architecture review | Integrated | readiness usa Git Bash, runner canônico que executa o wrapper sem a limitação CRLF WSL |
| `TEST-CONTRACT-01` | formal critique | Integrated | Flow Evidence exige mutation lane e evidência RED/GREEN para fixtures positivas/negativas |
| `STATE-ORACLE-01` | formal critique R6 | Integrated | cadeia ordenada por capability, terminal edge e module_catalog distinguem histórico multi-hop de ownership atual e dangling real |
| `VALIDATION-01` | formal critique R6 | Integrated | Completion Evidence tem uma row por DOD/VAL e DOD-06 possui casos positivos/negativos com fixture e diagnóstico esperado |
| `EXECUTION-01` | formal critique R6 | Integrated | regras de teste/delivery/closeout ingeridas; comandos exatos cobrem authority, audits, completion, repo-scoped closeout e active scan |
| `CATALOG-R7-01` / `F-01` | both formal reviews R7 | Integrated | bijeção catalog/modules, retired/active, terminal membership, origin/sequence e 12 mutações adicionais fecham o oracle 1:1 |
| `CLOSEOUT-R7-01` / `F-02` | both formal reviews R7 | Resolved external | TODO Delphi concluído em `0e54e2a`; correção `6dc5bd4`; probes reais retornam `path_state=active`, `todo_count=2` e zero violações |
| `PROFILE-R7-01` / `F-03` | formal critique R7 | Integrated | scope command agora classifica o diff Foundation real com prefixo de autoridade; empty diff não satisfaz |
| `TEST-R7-01` / `F-04` | formal critique R7 | Integrated | evidence matrix exige unit + full-tree integration/contract sem runtime externo |

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** o validator pode ser evoluído por manifesto único ou por inventário gerado; revisão independente deve desafiar a opção recomendada.
- **Opinion count:** `6`
- **Package mode:** `bounded-summary`
- **Internal reviewer mandate:** `required — fresh internal no-context reviewer after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `uninotas_architecture_opinion_main` | manifesto único + transferências por capability + matrix 1:1 | runtime neutral; harness precisa ser otimizado | melhora ao remover autoridades duplicadas | exigiu promoção parcial explícita | Integrated | formal R2 |
| `uninotas_architecture_opinion_r3` | IDs estáveis e core scope explícito | runtime neutral | remove aliases ambíguos | exige ownership verificável pelo mesmo ID | Integrated | formal R3 |
| `uninotas_architecture_opinion_r4` | proveniência/invariantes por capability + comando/coerência/estado exatos | runtime neutral | decisão canônica UniNotas elimina path ativo legado | exige ownership e sucessão deterministicamente verificáveis | Integrated | formal R4 |
| `uninotas_architecture_opinion_r5` | lifecycle terminal, migração estável de IDs e contrato operacional completo | runtime neutral | preserva proveniência sem ambiguidade | exige transições persistentes, paths/runner/namespaces/pcv fechados | Integrated | formal R5 |
| `uninotas_architecture_opinion_r6` | GO sem achados materiais no baseline d2c1223 | runtime neutral | manifesto/registry permanecem simples | confirmou source/current-target/IDs/diff/pcv | Accepted | formal R6; crítica paralela exigiu evolução multi-hop |
| `uninotas_architecture_opinion_r7` | catálogo/mutações adicionais + correção do closeout guard standalone | runtime neutral | mantém chain oracle explícito | falso go externo impedia fechamento confiável | Integrated / External resolved | formal R7; DEP-CLOSEOUT-01 resolvida em Delphi `6dc5bd4`/`0e54e2a` |

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Latest TEACH evidence / artifact:** `audit_escalation_guard.py: Overall outcome go; fingerprint bdde6668065b; critique, architecture decision/adherence, security, test-quality, final review, verification debt and delivery triple-review required; performance/concurrency recommended`.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | identidade + módulos + validator |
| `blast_radius` | `cross-module` | múltiplos owners canônicos |
| `behavioral_change_or_bugfix` | `yes` | comportamento do validator |
| `changes_public_contract` | `yes` | contrato documental do produto |
| `touches_auth_or_tenant` | `yes` | negação explícita de tenancy/contexto |
| `touches_runtime_or_infra` | `no` | nenhuma mudança runtime |
| `touches_tests` | `yes` | suíte determinística |
| `critical_user_journey` | `no` | sem fluxo runtime |
| `release_or_promotion_critical` | `yes` | desbloqueia slices seguintes |
| `high_severity_plan_review_issue` | `yes` | ARCH-01/02 |
| `explicit_three_lane_request` | `no` | não solicitado pelo usuário |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** big/cross-module/public-contract/high-severity.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede|high-severity issue card`
- **Package mode:** `bounded-summary`
- **Package minimum contents:** `frozen baseline|scope|assumptions|plan|issue cards|residual risks`
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after baseline freeze`
- **Canonical multi-lane audit protocol:** `n/a for planning critique; audit-protocol-triple-review required additively before Completed`
- **Audit session / round evidence:** `n/a until run`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** `R7 apontou quatro grupos; os achados locais foram integrados e DEP-CLOSEOUT-01 foi resolvida externamente; falta crítica R8 sobre baseline publicada`.
- **Evidence / reference:** `uninotas_plan_critique_r7`; resolução Delphi `6dc5bd4`/`0e54e2a`; nova crítica obrigatória após freeze R8.
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** embora não haja hipótese viva, o guard confirma que fatos e decisões citam código/docs reais antes da aprovação.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `none — fatos/decisões substituíram as hipóteses vivas; o guard ainda confirma coerência dos anchors`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending explicit APROVADO`
- **Approval scope:** `pending`
- **Execution not authorized by approval:** `backend, frontend, database, runtime, secrets, API calls, worktrees`
- **Renewed approval required when:** TD-01..TD-07, mapeamento D-01..D-11, scope, module topology, validation semantics ou risco material mudar.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | contrato tático | APROVADO + guards | implementação prematura | bloqueia execução |
| `delphi-ai/rules/core/foundation-docs-sync-model-decision.md` | contratos/domínio mudam | scope/modules/roadmap alinhados | subscopes implícitos | sincronização 1:1 |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | ciclo completo | gates e evidência | atalhos de lifecycle | roteia execução |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | revisão prévia | baseline publicado e reviews | aprovação sem preflight | exige freeze |
| `delphi-ai/workflows/docker/deterministic-todo-validation-method.md` | TODO tático | markdown canônico | editar bundle derivado | valida estrutura |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | validator/fixtures mudam | teste first, casos 1:1 e runner real | aggregate pass, mock/fallback silencioso | governa CAP/GUARD matrix |
| `delphi-ai/workflows/docker/todo-delivery-gates-method.md` | entrega exige prova | evidence por critério + guards/audits | evidência agregada | comandos de delivery obrigatórios |
| `delphi-ai/workflows/docker/todo-closeout-promotion-method.md` | TODO será movido após entrega | mesmo TODO + closeout guards | stale active TODO | governa move-completed |
| `delphi-ai/skills/audit-protocol-triple-review/SKILL.md` | cutover canônico | package/run-root e três lanes | audit sem estado/resultado | audit aditivo antes de Completed |
| `delphi-ai/templates/module_template.md` | três módulos serão criados | anchors canônicos e coverage status | inventar formato paralelo ou sobrecarregar lifecycle PACED | blueprint obrigatório dos novos módulos |
| `uninotas-foundation/policies/scope_subscope_governance.md` | novos owners | sem business tenancy | contexto como tenant | atualização explícita |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `governed routine-executor lane required by the applicable routing workflow; no parallel code writers`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `TD-01` | pending | pending implementation | identidade UniNotas + `core_scope=uninotas` |
| `TD-02` | pending | pending implementation | source ownership split |
| `TD-03` | pending | pending implementation | fiscal context sem tenancy |
| `TD-04` | pending | pending implementation | runtime-authority state e transferências por capability |
| `TD-05` | pending | pending implementation | três owners target exclusivos |
| `TD-06` | pending | pending implementation | manifesto único + semantic registry |
| `TD-07` | pending | pending implementation | writer/filter explicitamente desconhecido |
| `D-T01` | pending | pending implementation | validadores puros + fixtures mínimas |
| `D-T02` | pending | pending implementation | poucos testes full-tree de compatibilidade |
| `D-T03` | pending | pending implementation | exclusão explícita de runtime/dados reais |
| `D-T04` | pending | pending implementation | RED/GREEN e diagnóstico específico por caso |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `decisions#D-01` | Supersede (Intentional) | pending | pending | identity/core scope |
| `decisions#D-04` | Supersede (Intentional) | pending | pending | source ownership target split |
| `decisions#D-05` | Preserve | pending | pending | no business tenancy |
| `events#ownership` | Supersede (Intentional) | pending | pending | current capabilities e successors |
| `treatments#ownership` | Supersede (Intentional) | pending | pending | successor operational-cases |
| `runtime#logs` | Preserve | pending | pending | facts observed; writer unknown |
| `identity#no-tenancy` | Preserve | pending | pending | context is not tenancy |
| `realtime#logs-invalidation` | Preserve | pending | pending | current invalidation |
| `monitoring#logs-summary` | Preserve | pending | pending | current monitoring |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| bounded Foundation diff | P1/P2 contract/privacy/validator drift | planned | pending | pending | pre-delivery |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| TODO authority + Foundation sync | future-as-current, weakened validator, hidden tenancy/fallback | planned | pending | pending | pre-delivery |

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** o validator e os documentos processam conteúdo que pode conter segredo/PII, embora nenhuma chamada runtime seja feita.
- **Attack surface in scope:** `documentation privacy scanner; credential/PII persistence prevention`.
- **Attack simulation decision:** `required`
- **Review evidence:** `audit floor SEC-AUTH-OR-TENANT; security-adversarial-review required before Completed`.
- **Residual security risk:** `pending review`.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `low`
- **Why this level:** nenhuma superfície runtime muda, mas o piso recomenda classificação independente por ser release-sensitive.
- **Current delivery stage at review time:** `Pending`

| Policy | Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Trigger Rationale | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code | Recorded At UTC | Executor ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pcv-1` | `EPS` | endpoint-performance-scrutiny | not_needed | low | EPS-DATA-PATH-CHANGED | nenhum endpoint, query ou data-access path muda; o reason code foi avaliado como falso | before_local_implemented | EPS-E1 | not_applicable | none | none | `2026-09-25T16:12:12Z` | `codex-primary` |
| `pcv-1` | `FRC` | frontend-race-condition-validation | not_needed | low | FRC-STALE-RESPONSE | nenhuma UI ou leitura assíncrona retriggerable muda; o reason code foi avaliado como falso | before_local_implemented | FRC-POLICY | not_applicable | none | none | `2026-09-25T16:12:12Z` | `codex-primary` |
| `pcv-1` | `BCI` | backend-concurrency-idempotency-validation | not_needed | low | BCI-EXACT-ONCE-SEMANTICS | nenhuma escrita backend ou superfície de overlap muda; o reason code foi avaliado como falso | before_local_implemented | BCI-INV | not_applicable | none | none | `2026-09-25T16:12:12Z` | `codex-primary` |
| `pcv-1` | `RLS` | runtime-load-stress-validation | not_needed | low | RLS-SLO-CLAIM | nenhuma superfície de pressão runtime ou claim de SLO muda; o reason code foi avaliado como falso | before_production_ready | RLS-E1 | not_applicable | none | none | `2026-09-25T16:12:12Z` | `codex-primary` |

## Verification Debt Assessment

- **Audit outcome:** `required before Completed`
- **Why this outcome:** big architectural cutover requires audit before completion.
- **Inline code TODO debt:** `none expected`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none currently accepted`

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** validator/test logic and architectural semantics change.
- **Trigger signals in scope:** `changed test logic|architectural change|non-trivial validation risk`
- **Required evidence matrix:** `unit + full-tree integration/contract` (sem runtime externo; a árvore real da Foundation é a boundary de compatibilidade).
- **Package mode:** `bounded-file-set`
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required — fresh internal no-context reviewer before Completed`
- **Audit status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** identidade e arquitetura cross-module.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede`
- **Package mode:** `bounded-summary`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required — fresh internal no-context reviewer before Completed`
- **Final review status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `required`
- **Why this decision:** cutover canônico e aposentadoria da autoridade antiga.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement`
- **Package mode:** `bounded-file-set`
- **Canonical multi-lane audit protocol:** `audit-protocol-triple-review required additively before Completed`
- **Audit session / round evidence:** `n/a until run`
- **Audit focus:** `true canonical path|current-target labels|hidden fallback|validator preservation`
- **Cutover audit status:** `not_run`
- **Findings summary:** `pending`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planejamento e aprovação ainda não concluídos.
- **Post-commit/push status:** `pending`
- **Next path/status action:** publicar/revisar a baseline R8 pós-resolução de DEP-CLOSEOUT-01, executar guards pré-aprovação e solicitar `APROVADO` explícito.

## Module Consolidation Gate

- [ ] Canonical module docs updated with TD-01..TD-07 and canonical decision migration D-01..D-11.
- [ ] Decision promotion ledger links to this TODO.
- [ ] Prior decisions preserved or intentionally superseded.
- [ ] Conflicting tactical notes replaced by canonical references.
- [ ] TODO/module links updated after lifecycle movement.

## Commands (Run Locally)

- Pre-approval structure: `python3 delphi-ai/tools/todo_deterministic_validator.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- Pre-approval coherence: `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- Pre-approval drift: `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- Pre-approval authority: `python3 delphi-ai/tools/todo_authority_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --pre-approval`
- Profile scope on the real Foundation diff: `bash -lc 'mapfile -t paths < <(git -C uninotas-foundation diff --name-only 0fe906c1e496a1d38f1603cf188c224711011c32 -- | sed "s#^#foundation_documentation/#"); ((${#paths[@]} > 0)) && python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto "${paths[@]}"'`
- After `APROVADO`, before implementation: `python3 delphi-ai/tools/todo_authority_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py`
- `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation`
- `'/mnt/c/Program Files/Git/bin/bash.exe' -lc 'cd /c/Unifast/MonitorDeNotas && bash delphi-ai/verify_context.sh'`
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --repo-root uninotas-foundation`
- `git -C uninotas-foundation diff --check 0fe906c1e496a1d38f1603cf188c224711011c32 --`
- `git -C uninotas-foundation diff --name-status --find-renames 0fe906c1e496a1d38f1603cf188c224711011c32 --`
- Audit package start: `python3 delphi-ai/skills/audit-protocol-triple-review/scripts/triple_audit_session.py start --package uninotas-foundation/artifacts/analysis/uninotas-canonical-foundation-transition-delivery-package.md --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --extra-lane cutover-integrity --run-root uninotas-foundation/artifacts/tmp/uninotas-canonical-foundation-transition-audit`
- Delivery authority: `python3 delphi-ai/tools/todo_authority_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --require-delivery-gates`
- Delivery completion: `python3 delphi-ai/tools/todo_completion_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- Pre-move closeout after `DEP-CLOSEOUT-01`: `python3 delphi-ai/tools/todo_closeout_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --repo uninotas-foundation` (must report `path_state=active`, not only `go`).
- Git commit authority: `python3 delphi-ai/tools/git_write_authority_guard.py --repo uninotas-foundation --action git-commit --authority-surface foundation_documentation`
- Git push authority: `python3 delphi-ai/tools/git_write_authority_guard.py --repo uninotas-foundation --action git-push --authority-surface foundation_documentation`
- Post-commit/push active scan after `DEP-CLOSEOUT-01`: `python3 delphi-ai/tools/todo_closeout_guard.py --all-active --repo uninotas-foundation` (must report the real nonzero active TODO count, not only `go`).

## Files Expected (Compatibility Note)

- O `Diff Expectation Contract` é a autoridade exclusiva sobre paths esperados.
