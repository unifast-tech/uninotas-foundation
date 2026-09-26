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
- **Next exact step:** publicar as correções R8S como baseline R8T imutável, executar arquitetura/crítica R8T sem contexto e concluir os guards pré-aprovação.

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
- `Lane-Promoted`: n/a para esta autoridade documental single-branch; pushes de baseline de revisão não são delivery promotion.
- `Production-Ready`: C0 contém a implementação validada com o TODO ainda ativo; o candidate C1 move o TODO atomicamente para completed, atualiza somente o closeout allowlisted e persiste a stage com qualifier condicional. A stage só se torna efetiva quando C1 está publicado em `main`, uma observação fresh de `refs/heads/main` retorna exatamente C1, seu SHA/ancestry é verificado e o active scan semântico vinculado ao mesmo C1 retorna `todo_count=1` com exatamente o TODO discovery ativo e nenhum stale path desta transição; falha em qualquer condição invalida o closeout.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `uninotas-foundation:main` (autoridade single-branch/single-checkout)
- **Promotion lane path:** `main -> origin/main`
- **Lane-promoted threshold for this TODO:** `n/a — single-branch authority`
- **Production-ready threshold for this TODO:** C0 publicado/verificado + fresh `ls-remote refs/heads/main==C1` após move atômico, verificação externa de C1 e post-C1 semantic scan vinculado ao mesmo C1 `{todo_count:1, active_paths:[discovery TODO], stale_transition_path:false}`; `origin/main` local é apenas check adicional e, antes desse tuple, C1 é somente candidate condicional

## Promotion Evidence (Required Before Lane-Promoted / Production-Ready)

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Foundation UniNotas cutover | `main@ac1ce08` | `n/a — main-only authority` | `n/a` | `origin/main@ac1ce08` | R8S material review-baseline evidence only; not delivery promotion |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree bootstrap; candidate_tree authoritative after capture`
- **Canonical path-set enumerator:** uma implementação, dois baselines explícitos. `--mode delivery --baseline 0fe906c1e496a1d38f1603cf188c224711011c32 --candidate-tree <OID>` produz o net path set global; como o TODO ativo nasceu depois desse baseline e não existe em C1, somente o destino completed aparece no resultado final. `--mode lifecycle --baseline <C0_PRE_MOVE> --candidate-tree <OID>` compara o candidate C1 com o commit pre-move publicado onde o path ativo existe e deve emitir source ativo D + destination completed A. O helper usa `git diff --no-renames --name-only <baseline> <candidate-tree>`, normaliza paths relativos e aplica C-sort; `lifecycle` exige baseline ancestor com source ativo presente. Antes do helper/capture existir, apenas o preflight delivery usa o bootstrap equivalente `bash -lc '{ git -C uninotas-foundation diff --no-renames --name-only 0fe906c1e496a1d38f1603cf188c224711011c32 --; git -C uninotas-foundation ls-files --others --exclude-standard; } | LC_ALL=C sort -u'`; depois da criação/capture, fallback inline é proibido.
- **Status/rename evidence view:** a view delivery usa `git diff --name-status --find-renames 0fe906c...`; a view lifecycle repete contra `C0_PRE_MOVE`. Nenhuma define path authority; servem somente para tipos de mudança/rename, e apenas a lifecycle pode provar o move active→completed.
- **Gate interface:** o Delphi `todo_diff_expectation_guard.py` não aceita input do helper; ele permanece um gate independente e classifica o working-tree delivery diff contra `0fe906c` com sua implementação existente (`--find-renames` + untracked). O helper project-owned alimenta profile scope, lifecycle move evidence e revisão humana; não há alegação de integração inexistente. Ambos usam a mesma Expected Changed Paths como allowlist, mas somente `mode=lifecycle` prova o source ativo criado após baseline. No-go em qualquer gate bloqueia entrega.
- **Rename evidence:** a decisão-file rename usa a view delivery porque o source existe em `0fe906c`; o TODO move usa exclusivamente a view lifecycle porque seu source nasceu depois de `0fe906c`. Após staging, cada view deve reconhecer seu par como `R` ou a revisão registra explicitamente D/A com conteúdo/proveniência equivalentes.

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `uninotas-foundation` | `.` | `main@0fe906c` | `working_tree` |

### Expected Changed Paths

Esta tabela autoriza a união rotulada de `delivery` e `lifecycle`; ausência do path ativo no net delivery set final é esperada, desde que `mode=lifecycle C0..C1` prove D/R para ele e A/R para o destino completed.

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
| `uninotas-foundation` | `deterministic/capability_identity_ledger.json` | `A` | oracle append-only de identidade, independente da projeção mutável do registry |
| `uninotas-foundation` | `deterministic/enumerate_change_paths.py` | `A` | única implementação executável do canonical path set pós-approval |
| `uninotas-foundation` | `deterministic/validate_closeout_diff.py` | `A` | guard C0-relative que restringe o candidate C1 ao move atômico e células/links finais allowlisted |
| `uninotas-foundation` | `deterministic/closeout_handoff.py` | `A` | entry point fechado para CAS promotion, evidence por fase e activation/recovery handoff real |
| `uninotas-foundation` | `deterministic/validate_foundation.py` | `M` | validador evolutivo fail-closed |
| `uninotas-foundation` | `deterministic/tests/test_registry_semantics.py` | `A` | semântica de registry/ledger/history |
| `uninotas-foundation` | `deterministic/tests/test_privacy_predicate.py` | `A` | predicado de privacidade isolado |
| `uninotas-foundation` | `deterministic/tests/test_validate_foundation.py` | `M` | contratos full-tree preservados |
| `uninotas-foundation` | `deterministic/tests/test_enumerate_change_paths.py` | `A` | delivery/lifecycle path sets |
| `uninotas-foundation` | `deterministic/tests/test_validate_closeout_diff.py` | `A` | move atômico e allowlist final C0→C1 |
| `uninotas-foundation` | `deterministic/tests/test_closeout_handoff.py` | `A` | bare-remote CAS e validação strict do handoff production/recovery |

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
- [ ] `DOD-04` Registry e módulos distinguem `current_runtime` de `target_planned`, preservam identidades no `baseline_capability_catalog` confrontado com o identity ledger independente e registram precedência, predecessor/sucessor e condição de promoção/retirada, sem declarar código futuro como implementado.
- [ ] `DOD-05` Notas/documentos, falhas de integração e casos operacionais têm owners canônicos distintos.
- [ ] `DOD-06` Validator e suíte rejeitam regressões de identidade, decisão/link canônico obsoleto, ownership, tenancy, privacidade, symlink, legado e publicação, além de quebra da bijeção módulo/catálogo ou ledger-origin-new/transition, ID/path/transition/membership/ledger duplicado, conflito baseline/new, alteração do conjunto baseline após genesis, binding LEDGER_GENESIS ausente/duplicada/malformada/conflitante ou substituída por descendente, descendant com genesis pending/ausente, remoção/rename/alias coordenada do seed inicial contra digest canônico ou de identidade posterior dentro da linhagem first-parent observável, histórico shallow/truncado/non-descendant/replaced ou sem genesis, capability current direta sem origem, módulo retired ainda ativo/capable ou com documento/manifest entry publicado, módulo ativo vazio ou incompatível com sua cardinalidade runtime, sequence gap, fork, ciclo, predecessor desconhecido/nulo em transferência, chain edge ou origin inválida, aresta não terminal planned, interseção `owned_capabilities ∩ planned_capabilities`, target com `owned_capabilities`, aresta terminal planned sem exatamente um owner atual/predecessor ou successor membership, planned membership órfã sem aresta terminal correspondente, capability transferida/planned ou terminal completed sem o owner exigido, dupla autoridade runtime, successor planejado duplicado e planned membership obsoleto após promoção; reescrita alternativa descendente de C0 pertence explicitamente a `RISK-HIST-01`. Fixtures positivas cobrem estado inicial, bootstrap pre-C0, checkout limpo de C0, C1 com C0 exato, ownership current estável, append de capability nova, ancestralidade completa, histórico longo com subprocess/blob-read counts limitados e tempo advisory, promoção parcial/final, tombstone retired, predecessor retirado e segundo hop.
- [ ] `DOD-07` Os artefatos atuais pertencem ao manifesto e a validação Foundation passa sem `frozen lifecycle tree mismatch`.
- [ ] `DOD-08` Nenhum segredo, valor real de CNPJ/identificador do provedor, payload/resposta privada ou URL capturada de documento foi persistido; CNPJ válido é coberto deterministicamente e identificador/URL contextual por regra precisa mais revisão de diff.
- [ ] `DOD-09` O roadmap aponta para o TODO NestJS de leitura como próximo slice, sem lhe conceder autoridade antecipada.
- [ ] `DOD-10` O arquivo/índice canônico de decisões migra para UniNotas sem links obsoletos nem reutilização semântica de IDs: D-01..D-05 preservam sua proveniência/handling e D-06..D-11 recebem somente autoridades novas.
- [ ] `DOD-11` Antes de qualquer claim `Local-Implemented`/closeout, o `todo_closeout_guard.py` corrigido reconhece este path como `active` e o scan `--all-active --repo uninotas-foundation` encontra os TODOs ativos reais; falso `go` com `path_state=other` ou `todo_count=0` bloqueia entrega.
- [ ] `DOD-12` O harness implementa e testa o modelo C0 ativo → candidate C1 atômico → handoff externo, sem completed intermediário, evidência prospectiva ou guard que exija seu próprio output como input; `CLOSEOUT-POS-01/02` executam a state machine e os guards Delphi reais em repositório temporário antes de C0.
- [ ] `DOD-13` `deterministic/enumerate_change_paths.py` é o helper project-owned único para profile/lifecycle/human review: mode delivery representa o net diff de `0fe906c` até working tree bootstrap ou `--candidate-tree`; mode lifecycle representa C0..candidate C1 e emite os dois endpoints do move com `--candidate-tree`. O Delphi diff guard continua independente e obrigatório, como worktree-proxy quando não aceita tree OID.
- [ ] `DOD-14` Closeout/recovery e candidate-tree binding separam delivery scope de phase delta, exigem tree estável, binding faseado de consumers, proof bridge C0→C1/C1R, focused closeout/recovery reviews e handoff `uninotas-closeout-handoff-v1` tipado; commit-tree equals candidate-tree após C0/C1/C1R.
- [ ] `DOD-15` O harness implementa/testa History Trust sem autorreferência: C0/C1/C1R publicam por expected-value lease exato mais fast-forward proof; mismatch entra em local-unpublished-diverged sem push/unconditional force e exige rebaseline/reconciliação + novo `APROVADO`; ativação observa `refs/heads/main==C1` após push e vincula o scan ao mesmo C1; ausência de proteção exige aceite de `RISK-HIST-01`.

## Validation Steps

- [ ] `VAL-01` Executar fail-first e as duas lanes: `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_registry_semantics.py uninotas-foundation/deterministic/tests/test_privacy_predicate.py` e `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py`, registrando RED/GREEN, duração separada/agregada e scan counters de `D-T05`.
- [ ] `VAL-02` Executar `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation`.
- [ ] `VAL-03` Executar `'/mnt/c/Program Files/Git/bin/bash.exe' -lc 'cd /c/Unifast/MonitorDeNotas && bash delphi-ai/verify_context.sh'`, runner canônico que evita a limitação CRLF do wrapper sob WSL.
- [ ] `VAL-04` Executar da raiz do workspace `python3 delphi-ai/tools/todo_diff_expectation_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --repo-root uninotas-foundation`, além dos guards Delphi de autoridade, conclusão e cutover definidos neste TODO.
- [ ] `VAL-05` Executar independentemente o Delphi diff-expectation guard, o helper `mode=delivery`, profile scope alimentado pelo helper, diff check e status/rename view; revisão humana confirma que cada path observado na modalidade aplicável possui row autorizada, sem alegar que o Delphi guard consome output externo.
- [ ] `VAL-06` Consumir a correção Delphi standalone já publicada: executar os dois comandos de closeout deste contrato e verificar semanticamente `path_state=active` no path individual e `todo_count>=1` no scan ativo; exit code/`go` isolado não basta.
- [ ] `VAL-07` Executar a fixture Git `CLOSEOUT-POS-02`, que prepara C0/candidate C1 com evidence já concluída e invoca closeout-diff/structure/authority/completion/closeout reais sem alterar o candidate após validação; outputs da entrega real pertencem ao handoff externo.
- [ ] `VAL-08` Executar `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_enumerate_change_paths.py` cobrindo untracked, staged D/A, rename reconhecido como R, source criado após delivery baseline/movido antes de C1 e `--candidate-tree` independente do working tree, com expectativas distintas para delivery e lifecycle.
- [ ] `VAL-09` Executar `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_closeout_diff.py uninotas-foundation/deterministic/tests/test_closeout_handoff.py`, cobrindo dual-set/bridge e o entry point real de CAS promotion + activation/recovery strict; fixtures alteram cada observação, consumer binding, C0/C1/C1R phase evidence e remote/scan boundary.
- [ ] `VAL-10` Executar fixtures History Trust para C0/C1 precommit, avanço de bare remote entre commit/push, C1 post-push com avanço antes da ativação, parent/ancestry, proteção indisponível e proibição de persistir OID próprio; observações reais ficam no candidate/handoff conforme sua disponibilidade temporal.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SCOPE-01` | Scope | identidade canônica | doc+test | roots/anchors | local | planned | Canonicalizar `UniNotas` como nome do produto e `uninotas` como `core_scope`, preservando `MonitorDeNotas` como nome técnico do repositório nesta entrega. |
| `SCOPE-02` | Scope | namespaces observados | doc+test | constitution/validator | local | planned | Declarar na constituição `Namespaces: nestjs,react,vite,postgresql,prisma,docker,railway`, refletindo somente a topologia já verificada e mantendo cada capability independente. |
| `SCOPE-03` | Scope | source ownership | doc+test | constitution/decisions | local | planned | Registrar a topologia externa confirmada e a propriedade de dados: Smart Notas para notas/documentos, PostgreSQL `logs` somente para falhas de integração. |
| `SCOPE-04` | Scope | contextos fiscais | doc+test | scope/identity | local | planned | Registrar Unifast e Prosperar como `FiscalIssuerContext`, sem tenancy e sem agregação inicial de notas. |
| `SCOPE-05` | Scope | Current/Target | doc+test | roots/decisions/modules | local | planned | Separar explicitamente comportamento atual e arquitetura-alvo nas raízes, decisões, roadmap e módulos afetados. |
| `SCOPE-06` | Scope | novos owners | doc+test | module files/index | local | planned | Criar os owners canônicos planejados exatos `modules/fiscal-notes-and-documents.md`, `modules/integration-error-occurrences.md` e `modules/operational-cases.md`. |
| `SCOPE-07` | Scope | policy/indexes | doc+test | scope policy/indexes | local | planned | Atualizar a política de scope/subscope e os índices sem inventar módulos de runtime já implementados. |
| `SCOPE-08` | Scope | validator evolutivo | code+test | deterministic harness | local | planned | Evoluir o validador e seus testes para a nova identidade, módulos e publicação governada, mantendo proteções existentes. |
| `SCOPE-09` | Scope | publicação privada-safe | doc+test+review | manifest/privacy guards | local | planned | Publicar no manifesto os artefatos de descoberta e este TODO sem persistir segredos, valores reais de CNPJ/identificador do provedor, payloads/respostas privadas ou URLs capturadas de documentos. |
| `DOD-01` | Definition of Done | identidade/core scope/Namespaces | doc+test | roots/anchors + `test_identity_core_scope_and_namespaces` | local | planned | `DOD-01` Identidade/mandato usam UniNotas, todos os anchors usam `core_scope=uninotas` e a constituição declara os `Namespaces` verificados, sem renomear o repositório técnico. |
| `DOD-02` | Definition of Done | topologia e source ownership | doc+test | constitution/decisions + `test_source_ownership_split` | local | planned | `DOD-02` Constituição e decisões registram a topologia externa e a separação de fontes aprovada. |
| `DOD-03` | Definition of Done | fiscal context sem tenancy | doc+test | scope/identity + `test_fiscal_context_is_not_tenancy` | local | planned | `DOD-03` Unifast/Prosperar são contextos fiscais explícitos e não tenants. |
| `DOD-04` | Definition of Done | `DOD-04` Registry e módulos distinguem `current_runtime` de `target_planned`, preservam identidades no `baseline_capability_catalog` confrontado com o identity ledger independente e registram precedência, predecessor/sucessor e condição de promoção/retirada, sem declarar código futuro como implementado. | doc+test | registry/modules + casos `CAP-*` + full-tree integration test | local | planned | multi-hop e catálogo; sem runtime externo |
| `DOD-05` | Definition of Done | três owners target distintos | doc+test | module index + `test_target_owner_boundaries` | local | planned | `DOD-05` Notas/documentos, falhas de integração e casos operacionais têm owners canônicos distintos. |
| `DOD-06` | Definition of Done | `DOD-06` Validator e suíte rejeitam regressões de identidade, decisão/link canônico obsoleto, ownership, tenancy, privacidade, symlink, legado e publicação, além de quebra da bijeção módulo/catálogo ou ledger-origin-new/transition, ID/path/transition/membership/ledger duplicado, conflito baseline/new, alteração do conjunto baseline após genesis, binding LEDGER_GENESIS ausente/duplicada/malformada/conflitante ou substituída por descendente, descendant com genesis pending/ausente, remoção/rename/alias coordenada do seed inicial contra digest canônico ou de identidade posterior dentro da linhagem first-parent observável, histórico shallow/truncado/non-descendant/replaced ou sem genesis, capability current direta sem origem, módulo retired ainda ativo/capable ou com documento/manifest entry publicado, módulo ativo vazio ou incompatível com sua cardinalidade runtime, sequence gap, fork, ciclo, predecessor desconhecido/nulo em transferência, chain edge ou origin inválida, aresta não terminal planned, interseção `owned_capabilities ∩ planned_capabilities`, target com `owned_capabilities`, aresta terminal planned sem exatamente um owner atual/predecessor ou successor membership, planned membership órfã sem aresta terminal correspondente, capability transferida/planned ou terminal completed sem o owner exigido, dupla autoridade runtime, successor planejado duplicado e planned membership obsoleto após promoção; reescrita alternativa descendente de C0 pertence explicitamente a `RISK-HIST-01`. Fixtures positivas cobrem estado inicial, bootstrap pre-C0, checkout limpo de C0, C1 com C0 exato, ownership current estável, append de capability nova, ancestralidade completa, histórico longo com subprocess/blob-read counts limitados e tempo advisory, promoção parcial/final, tombstone retired, predecessor retirado e segundo hop. | test | casos `CAP-*`/`GUARD-*` mutation + full-tree integration test | local | planned | diagnósticos específicos; nenhum placeholder em evidence/notes |
| `DOD-07` | Definition of Done | publicação sem frozen-tree mismatch | test | manifest + Foundation full-tree integration test | local | planned | `DOD-07` Os artefatos atuais pertencem ao manifesto e a validação Foundation passa sem `frozen lifecycle tree mismatch`. |
| `DOD-08` | Definition of Done | privacidade e nenhum segredo/PII | test+review | `GUARD-PRIV-*` mutation integration test + `REVIEW-PRIV-01` | local | planned | `DOD-08` Nenhum segredo, valor real de CNPJ/identificador do provedor, payload/resposta privada ou URL capturada de documento foi persistido; CNPJ válido é coberto deterministicamente e identificador/URL contextual por regra precisa mais revisão de diff. |
| `DOD-09` | Definition of Done | sequência do roadmap | doc+review | `system_roadmap.md` + aderência | n/a | planned | `DOD-09` O roadmap aponta para o TODO NestJS de leitura como próximo slice, sem lhe conceder autoridade antecipada. |
| `DOD-10` | Definition of Done | migração estável de decisões | doc+test | decision map/index + test | local | planned | `DOD-10` O arquivo/índice canônico de decisões migra para UniNotas sem links obsoletos nem reutilização semântica de IDs: D-01..D-05 preservam sua proveniência/handling e D-06..D-11 recebem somente autoridades novas. |
| `DOD-11` | Definition of Done | closeout guard standalone | external guard+regression | Delphi fix + semantic probes | local | planned | `DOD-11` Antes de qualquer claim `Local-Implemented`/closeout, o `todo_closeout_guard.py` corrigido reconhece este path como `active` e o scan `--all-active --repo uninotas-foundation` encontra os TODOs ativos reais; falso `go` com `path_state=other` ou `todo_count=0` bloqueia entrega. |
| `DOD-12` | Definition of Done | state machine sem self-reference | guard+test+git | `CLOSEOUT-POS-01/02` | local | planned | `DOD-12` O harness implementa e testa o modelo C0 ativo → candidate C1 atômico → handoff externo, sem completed intermediário, evidência prospectiva ou guard que exija seu próprio output como input; `CLOSEOUT-POS-01/02` executam a state machine e os guards Delphi reais em repositório temporário antes de C0. |
| `DOD-13` | Definition of Done | helper delivery/lifecycle | tool+test | helper + `CHANGESET-*` | local | planned | `DOD-13` `deterministic/enumerate_change_paths.py` é o helper project-owned único para profile/lifecycle/human review: mode delivery representa o net diff de `0fe906c` até working tree bootstrap ou `--candidate-tree`; mode lifecycle representa C0..candidate C1 e emite os dois endpoints do move com `--candidate-tree`. O Delphi diff guard continua independente e obrigatório, como worktree-proxy quando não aceita tree OID. |
| `DOD-14` | Definition of Done | candidate-tree/closeout enforcement | guard+test | closeout + tree-binding suite | local | planned | `DOD-14` Closeout/recovery e candidate-tree binding separam delivery scope de phase delta, exigem tree estável, binding faseado de consumers, proof bridge C0→C1/C1R, focused closeout/recovery reviews e handoff `uninotas-closeout-handoff-v1` tipado; commit-tree equals candidate-tree após C0/C1/C1R. |
| `DOD-15` | Definition of Done | History Trust sem autorreferência | git+test | History Trust fixtures | local | planned | `DOD-15` O harness implementa/testa History Trust sem autorreferência: C0/C1/C1R publicam por expected-value lease exato mais fast-forward proof; mismatch entra em local-unpublished-diverged sem push/unconditional force e exige rebaseline/reconciliação + novo `APROVADO`; ativação observa `refs/heads/main==C1` após push e vincula o scan ao mesmo C1; ausência de proteção exige aceite de `RISK-HIST-01`. |
| `VAL-01` | Validation Steps | suíte determinística | test | comandos unittest exatos | local | planned | `VAL-01` Executar fail-first e as duas lanes: `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_registry_semantics.py uninotas-foundation/deterministic/tests/test_privacy_predicate.py` e `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py`, registrando RED/GREEN, duração separada/agregada e scan counters de `D-T05`. |
| `VAL-02` | Validation Steps | Foundation validator | test | validator command | local | planned | `VAL-02` Executar `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation`. |
| `VAL-03` | Validation Steps | PACED readiness | environment | Git Bash command | local | planned | `VAL-03` Executar `'/mnt/c/Program Files/Git/bin/bash.exe' -lc 'cd /c/Unifast/MonitorDeNotas && bash delphi-ai/verify_context.sh'`, runner canônico que evita a limitação CRLF do wrapper sob WSL. |
| `VAL-04` | Validation Steps | guards authority/delivery/cutover | guard | Commands section | local | planned | `VAL-04` Executar da raiz do workspace `python3 delphi-ai/tools/todo_diff_expectation_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --repo-root uninotas-foundation`, além dos guards Delphi de autoridade, conclusão e cutover definidos neste TODO. |
| `VAL-05` | Validation Steps | diff baseline-aware | review | helper/profile/diff/status commands | local | planned | `VAL-05` Executar independentemente o Delphi diff-expectation guard, o helper `mode=delivery`, profile scope alimentado pelo helper, diff check e status/rename view; revisão humana confirma que cada path observado na modalidade aplicável possui row autorizada, sem alegar que o Delphi guard consome output externo. |
| `VAL-06` | Validation Steps | closeout sem false-go | guard | individual + `--all-active` | local | planned | `VAL-06` Consumir a correção Delphi standalone já publicada: executar os dois comandos de closeout deste contrato e verificar semanticamente `path_state=active` no path individual e `todo_count>=1` no scan ativo; exit code/`go` isolado não basta. |
| `VAL-07` | Validation Steps | real-guard fixture | test+guard | `CLOSEOUT-POS-02` integration test | local | planned | `VAL-07` Executar a fixture Git `CLOSEOUT-POS-02`, que prepara C0/candidate C1 com evidence já concluída e invoca closeout-diff/structure/authority/completion/closeout reais sem alterar o candidate após validação; outputs da entrega real pertencem ao handoff externo. |
| `VAL-08` | Validation Steps | path-set endpoints/untracked | test | `test_enumerate_change_paths.py` | local | planned | `VAL-08` Executar `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_enumerate_change_paths.py` cobrindo untracked, staged D/A, rename reconhecido como R, source criado após delivery baseline/movido antes de C1 e `--candidate-tree` independente do working tree, com expectativas distintas para delivery e lifecycle. |
| `VAL-09` | Validation Steps | closeout/recovery/tree binding | test | closeout diff + handoff integration tests | local | planned | `VAL-09` Executar `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_closeout_diff.py uninotas-foundation/deterministic/tests/test_closeout_handoff.py`, cobrindo dual-set/bridge e o entry point real de CAS promotion + activation/recovery strict; fixtures alteram cada observação, consumer binding, C0/C1/C1R phase evidence e remote/scan boundary. |
| `VAL-10` | Validation Steps | temporal History Trust fixtures | git+test | temp Git fixtures | local | planned | `VAL-10` Executar fixtures History Trust para C0/C1 precommit, avanço de bare remote entre commit/push, C1 post-push com avanço antes da ativação, parent/ancestry, proteção indisponível e proibição de persistir OID próprio; observações reais ficam no candidate/handoff conforme sua disponibilidade temporal. |

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
| `CAP-POS-07` | positive | `stable_current_ownership_without_transition` | capability baseline sem transferência permanece em exatamente um owner current e não ganha proveniência sintética |
| `CAP-POS-08` | positive+full-tree | `retired_catalog_tombstone_without_document` | predecessor retired permanece no catálogo/histórico por ID/path, enquanto seu documento e manifest entry não existem |
| `CAP-POS-09` | positive | `append_new_origin_identity` | capability `origin=new` é anexada ao ledger e ligada à transition sequence 1 correspondente |
| `CAP-POS-10` | positive+git-history | `complete_first_parent_history_from_genesis` | non-shallow HEAD descendente de genesis preserva todas as versões/identidades do ledger |
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
| `CAP-NEG-23` | negative | `completed_terminal_without_successor_owner` | `terminal completed capability has no sole successor owner` |
| `CAP-NEG-24` | negative | `orphan_planned_membership` | `planned membership has no matching terminal planned transition` |
| `CAP-NEG-25` | negative | `transferred_with_null_predecessor` | `transferred capability requires a predecessor` |
| `CAP-NEG-26` | negative | `duplicate_owned_membership` | `owned_capabilities contains duplicate capability id` |
| `CAP-NEG-27` | negative | `duplicate_planned_membership` | `planned_capabilities contains duplicate capability id` |
| `CAP-NEG-28` | negative | `current_runtime_without_owned_capability` | `current_runtime module must own at least one capability` |
| `CAP-NEG-29` | negative | `target_planned_without_planned_capability` | `target_planned module must plan at least one capability` |
| `CAP-NEG-30` | negative | `active_module_without_capabilities` | `active module has neither owned nor planned capabilities` |
| `CAP-NEG-31` | negative+full-tree | `retired_catalog_path_still_published` | `retired module path must be an unpublished historical tombstone` |
| `CAP-NEG-32` | negative | `baseline_capability_deleted` | `baseline capability is missing from governed ownership or transition state` |
| `CAP-NEG-33` | negative | `baseline_capability_renamed_or_aliased` | `baseline capability id is immutable and aliases are forbidden` |
| `CAP-NEG-34` | negative | `uncataloged_capability_inserted_directly_as_owned` | `non-baseline capability requires origin new transition history` |
| `CAP-NEG-35` | negative | `coordinated_initial_identity_erasure` | `frozen initial capability identity digest mismatch` mesmo após remover registry/ownership/transitions relacionados |
| `CAP-NEG-36` | negative+git-history | `coordinated_new_origin_identity_erasure` | `capability identity ledger removed or changed historical record` mesmo após remover transition/memberships relacionados |
| `CAP-NEG-52` | negative+git-history | `identity_removed_then_readded_unchanged` | cada versão posterior deve ser superconjunto semântico da anterior; reintrodução não apaga a violação intermediária |
| `CAP-NEG-53` | negative+git-history | `identity_mutated_then_reverted` | mutação intermediária viola imutabilidade mesmo quando a versão final restaura bytes/semântica anteriores |
| `CAP-NEG-37` | negative+git-history | `shallow_truncated_missing_or_non_descendant_genesis` | `capability identity history is incomplete or untrusted` para shallow, missing genesis, non-descendant ou replace/graft |
| `CAP-LIMIT-01` | documented limitation+git-history | `alternate_descendant_rewrite_preserving_genesis` | validator não detecta rewrite coerente que preserva C0; teste documenta `RISK-HIST-01` e impede claim fail-closed mais amplo |
| `CAP-NEG-38` | negative | `new_transition_missing_identity_ledger_record` | `origin new transition requires exactly one identity ledger record` |
| `CAP-NEG-39` | negative | `new_identity_record_missing_transition` | `origin new identity record references no sequence one transition` |
| `CAP-NEG-40` | negative | `new_identity_transition_capability_mismatch` | `origin new identity record capability does not match transition` |
| `CAP-NEG-41` | negative | `duplicate_identity_ledger_capability` | `capability identity ledger id is not unique` |
| `CAP-NEG-42` | negative | `baseline_and_new_origin_conflict` | `capability identity cannot have both baseline and new origins` |
| `CAP-NEG-43` | negative+git-history | `recorded_genesis_replaced_by_later_descendant` | `recorded ledger genesis is not the earliest first-parent ledger introduction commit` |
| `CAP-NEG-44` | negative+git-history | `post_genesis_identity_reclassified_as_baseline` | `post-genesis capability identities must use origin new`; cobre append coordenado de ledger baseline + baseline catalog + owner current |
| `CAP-POS-11` | positive+git-history+performance | `long_unrelated_history_with_sparse_ledger_changes` | 200 commits não relacionados e 5 mudanças do ledger visitam somente as 6 versões relevantes; Git calls `<= versions + 2` |
| `CAP-POS-12` | positive+git-history | `pre_c0_uncommitted_bootstrap_candidate` | genesis pending é aceito somente com active TODO, ledger seed canônico exato, HEAD sem ledger e candidate prestes a introduzi-lo |
| `CAP-POS-13` | positive+git-history | `clean_published_c0_bootstrap` | checkout limpo em HEAD=C0, primeiro commit que introduziu o ledger, aceita pending somente com seed canônico exato |
| `CAP-POS-14` | positive+git-history | `c1_records_exact_c0` | primeiro descendant exige e aceita LEDGER_GENESIS igual ao primeiro commit first-parent que introduziu o ledger |
| `CAP-POS-15` | positive+canonicalization | `ledger_formatting_and_key_order_change` | whitespace/key-order JSON diferentes produzem a mesma representação/digest canônicos |
| `CAP-NEG-45` | negative+git-history | `descendant_with_pending_or_missing_genesis` | `ledger genesis must be recorded after the clean C0 bootstrap commit` |
| `CAP-NEG-46` | negative+canonicalization | `seed_semantic_field_mutation` | `frozen initial capability identity digest mismatch` para qualquer campo semântico alterado |
| `CAP-NEG-47` | negative+genesis-binding | `ledger_genesis_field_missing` | `canonical LEDGER_GENESIS field is missing` |
| `CAP-NEG-48` | negative+genesis-binding | `ledger_genesis_field_duplicate` | `canonical LEDGER_GENESIS field must occur exactly once` |
| `CAP-NEG-49` | negative+genesis-binding | `ledger_genesis_oid_malformed` | `canonical LEDGER_GENESIS must be pending bootstrap or lowercase 40-hex OID` |
| `CAP-NEG-50` | negative+genesis-binding | `active_and_completed_todo_both_publish_genesis` | `exactly one canonical lifecycle TODO path may publish LEDGER_GENESIS` |
| `CAP-NEG-51` | negative+genesis-binding | `ledger_genesis_descendant_substitution` | `recorded LEDGER_GENESIS differs from earliest first-parent ledger introduction commit` |
| `GUARD-ID-01` | negative | `legacy_identity_or_decision_link` | identidade/índice canônico legado é rejeitado |
| `GUARD-TENANCY-01` | negative | `fiscal_context_as_tenant` | contexto fiscal tratado como tenancy é rejeitado |
| `GUARD-PUB-01` | negative | `unmanifested_or_missing_path` | árvore diverge do manifesto |
| `GUARD-SYMLINK-01` | negative | `unexpected_symlink` | symlink fora do contrato é rejeitado |
| `GUARD-LEGACY-01` | negative | `legacy_exception_mutation` | ledger histórico congelado é rejeitado |
| `GUARD-PRIV-01` | negative | `valid_cnpj_value` | CNPJ válido persistido é rejeitado |
| `GUARD-PRIV-02` | negative | `concrete_provider_identifier_context` | valor concreto em chave provider-ID reconhecida é rejeitado com diagnóstico específico |
| `GUARD-PRIV-03` | negative | `captured_document_url_context` | URL concreta em chave PDF/XML/DANFE/document reconhecida é rejeitada com diagnóstico específico |
| `GUARD-PRIV-POS-01` | positive | `official_url_generic_id_and_placeholders` | URL oficial da especificação, ID genérico e placeholders permitidos não geram falso positivo |
| `GUARD-PRIV-04` | negative | `concrete_credential_key_matrix` | token, authorization/bearer ou valor concreto sob chave CNPJ reconhecida é rejeitado em cada sintaxe, mesmo quando o CNPJ não passa checksum |
| `GUARD-PRIV-POS-02` | positive | `credential_placeholder_matrix` | cada placeholder permitido é aceito para cada família de chave e sintaxe suportada, inclusive fenced examples |
| `REVIEW-PRIV-01` | manual review | checklist de diff limitado aos paths esperados | nenhum valor contextual privado escapa das regras automáticas; attestation externa registra reviewer, `candidate_tree_oid`, exact path set e resultado sem copiar o valor sensível; mudança do OID invalida o parecer |

### Canonical Change-Set Case Matrix

| Case ID | Fixture | Expected assertion |
| --- | --- | --- |
| `CHANGESET-POS-01` | `untracked_nonignored_file` | path untracked aparece exatamente uma vez |
| `CHANGESET-POS-02` | `staged_delete_and_add_pair` | source D e destination A aparecem como dois paths individuais |
| `CHANGESET-POS-03` | `git_recognized_rename` | mesmo quando status view retorna R, canonical path set contém source e destination individualmente |
| `CHANGESET-POS-04` | `ignored_file` | path ignorado não aparece |
| `CHANGESET-POS-05` | `source_created_after_delivery_baseline_then_moved` | delivery set contém somente destino final; lifecycle set C0..C1 contém source D + destination A, sem exigir source no net delivery set |
| `CHANGESET-POS-06` | `candidate_tree_ignores_different_worktree` | mode delivery com `--candidate-tree` enumera somente o diff baseline→tree OID mesmo quando o working tree possui bytes adicionais |

### Candidate Tree Binding Contract

C0, C1 e C1R validam e publicam exatamente a árvore do índice, nunca um working tree implícito. Dois conjuntos diferentes são obrigatórios e nunca podem ser comparados como se tivessem a mesma base:

- `DELIVERY_SCOPE_SET`: diff cumulativo entre `0fe906c1e496a1d38f1603cf188c224711011c32` e `CANDIDATE_TREE_OID`; alimenta scope, diff/review e Expected Changed Paths. O helper aceita `--candidate-tree <OID>` para observar a árvore capturada, sem depender do working tree.
- `PHASE_COMMIT_DELTA_SET`: diff entre a árvore do `BASE_HEAD` congelado e `CANDIDATE_TREE_OID`; deve ser exatamente igual ao índice staged. Em C0, cada path do delta deve ser autorizado pelo Expected Changed Paths, mas o delta pode ser subconjunto do delivery scope porque mudanças de planejamento já publicadas antes de `BASE_HEAD` continuam apenas no conjunto cumulativo. Em C1/C1R, o delta é exatamente os cinco paths do closeout em sentido direto/reverso.

O protocolo obrigatório é:

1. observar remote tip, congelar `BASE_HEAD`, exigir índice inicialmente vazio e calcular o working-tree delta esperado contra `BASE_HEAD`; stagear integralmente somente esse delta;
2. exigir `git diff --quiet --` (nenhum tracked byte worktree≠index), zero untracked não ignorado e staged path set exatamente igual a `PHASE_COMMIT_DELTA_SET`;
3. capturar `CANDIDATE_TREE_OID=$(git write-tree)`; provar separadamente que `DELIVERY_SCOPE_SET` respeita o contrato cumulativo e que `PHASE_COMMIT_DELTA_SET` respeita a allowlist da fase;
4. vincular todo consumer ao candidate conforme a classificação faseada abaixo; mudança do OID invalida outputs da mesma fase, enquanto C0→C1/C1R só pode carregar reviews de implementação através do proof bridge tree-native e de uma revisão humana focada no novo candidate;
5. imediatamente antes do commit, repetir remote/base precondition, staged allowlist, worktree↔index equality e `git write-tree == CANDIDATE_TREE_OID`; nenhuma mutação após os guards é permitida;
6. imediatamente após o commit, exigir `git rev-parse HEAD^{tree} == CANDIDATE_TREE_OID` e parent/base equality antes de qualquer push. Mismatch invalida o commit para promoção e exige correção sem push/unconditional force; somente o expected-value lease contratual é permitido quando todas as precondições passam.

| Consumer class | Consumers | Binding rule |
| --- | --- | --- |
| `tree-native` | `validate_closeout_diff.py`, `enumerate_change_paths.py` e qualquer helper que aceite tree OID | recebe `--candidate-tree <CANDIDATE_TREE_OID>` e lê/diffa essa árvore explicitamente |
| `worktree-proxy` | Foundation validator, Delphi TODO guards, profile scope, diff/status views e suites que não aceitam tree OID | single-code-writer exclusivo; exigir index/worktree equality, zero untracked e `git write-tree==CANDIDATE_TREE_OID` imediatamente antes e depois de cada comando; mismatch descarta o output e reinicia o batch |
| `implementation-human-review@C0` | `REVIEW-PRIV-01`, delivery triple-review, security, architecture adherence, performance/concurrency, test-quality e final review | executar após capture de C0; attestation externa `{phase:C0, candidate_tree_oid, exact_path_set, reviewer_or_session, outcome}` permanece válida somente para conteúdo de implementação comprovadamente byte-frozen pelo proof bridge |
| `closeout-human-review@C1/C1R` | `REVIEW-C1-01` cutover integrity e `REVIEW-C1R-01` recovery integrity | executar após capture do candidate correspondente; conferir exact five-path delta, cells/links/failure tuple allowlisted, proof-bridge output e ausência de conteúdo de implementação novo; OID change exige rerun |

O proof bridge obrigatório é `validate_closeout_diff.py --base <C0|FAILED_C1> --candidate-tree <OID>`: ele prova deterministicamente que C1/C1R contém somente a transformação fechada já testada, registra base commit/tree, candidate tree, exact delta e resultado, e autoriza carregar apenas attestations C0 marcadas `scope=implementation_content`. Ele não carrega cutover/recovery review. `REVIEW-C1-01` é obrigatório antes do commit C1 e `REVIEW-C1R-01` antes do C1R. Qualquer byte fora do bridge, attestation C0 sem binding ou focused review ligado a outro OID é no-go. Nenhuma attestation dependente do OID é persistida no próprio candidate.

| Case ID | Fixture | Expected assertion |
| --- | --- | --- |
| `TREE-POS-01` | `staged_candidate_tree_matches_commit_tree` | staged paths/tree ficam estáveis pelos guards e commit tree equals captured candidate tree |
| `TREE-POS-02` | `delivery_baseline_precedes_base_head` | delivery scope mantém path já committed antes de BASE_HEAD, enquanto phase delta o omite legitimamente e continua exatamente igual ao índice |
| `TREE-NEG-01` | `authorized_change_left_unstaged` | `working tree differs from validated candidate index` |
| `TREE-NEG-02` | `unrelated_path_pre_staged` | `staged candidate contains path outside phase allowlist` |
| `TREE-NEG-03` | `mutation_after_validation_before_commit` | `candidate tree changed after final validation` |
| `TREE-NEG-04` | `commit_tree_differs_from_captured_candidate` | `committed tree does not match validated candidate tree` |
| `TREE-NEG-05` | `worktree_proxy_output_from_different_tree` | `guard output is not bound to current candidate tree` |
| `TREE-NEG-06` | `human_attestation_from_stale_candidate` | `review attestation candidate tree/path set does not match current candidate` |
| `TREE-POS-03` | `c0_implementation_reviews_carried_by_c1_proof_bridge` | byte-frozen implementation content retains C0 review bindings while focused C1 review binds the five-path candidate |
| `TREE-NEG-07` | `c1_missing_or_invalid_proof_bridge` | C0 implementation attestations cannot be reused without exact C0→C1 bridge |
| `TREE-NEG-08` | `focused_closeout_review_bound_to_other_tree` | C1/C1R focused review must bind the current candidate tree and exact phase delta |

### Remote Promotion Race Contract

C0, C1 e C1R usam compare-and-swap do ref remoto, não `origin/main`, como autoridade de publicação. Antes do commit e imediatamente antes do push, `git ls-remote --exit-code origin refs/heads/main` deve retornar a base esperada. O push exato é `git push --force-with-lease=refs/heads/main:<EXPECTED_REMOTE_OID> origin <NEW_COMMIT_OID>:refs/heads/main`, autorizado somente como expected-value lease; unconditional `--force`, lease sem OID exato e push ordinário são proibidos. Antes dele, exigir `merge-base --is-ancestor <EXPECTED_REMOTE_OID> <NEW_COMMIT_OID>` e parent exato; portanto a atualização continua fast-forward. Em C0, `BASE_HEAD==BASE_REMOTE_OID==EXPECTED_REMOTE_OID`; em C1, ambos são C0; em C1R, ambos são FAILED_C1. Se o ref mudar no intervalo após `ls-remote`, o lease rejeita atomicamente, inclusive mudança fast-forward-compatible/rewind. Após o push de C1, `post_push_remote_main_oid` deve ser C1 antes do scan; o scan local declara `scanned_head_oid=C1`; imediatamente antes do tuple de sucesso, uma segunda observação `actual_remote_main_oid` deve continuar igual a C1. As três identidades são obrigatórias.

Se o remoto avançar depois do commit local de C0 ou C1 e antes/durante o CAS push, o estado é `local-unpublished-diverged`: nenhum novo push, unconditional force, candidate ou claim de delivery é permitido. O failure tuple externo preserva `{phase, local_commit_oid, candidate_tree_oid, expected_remote_oid, actual_remote_main_oid, push_attempted:false|lease_rejected, production_ready_effective:false}` sem ser persistido no commit que referencia. O operador classifica os commits intervenientes, reconcilia/rebaselineia sob autoridade explícita e obtém novo `APROVADO` antes de formar outro candidate; C1R não se aplica porque o C1 local não foi publicado.

| Case ID | Fixture | Expected assertion |
| --- | --- | --- |
| `REMOTE-NEG-01` | `bare_remote_sibling_advances_after_local_c0_commit_before_push` | exact expected-value lease rejects C0 push and enters local-unpublished-diverged |
| `REMOTE-NEG-02` | `bare_remote_sibling_advances_after_local_c1_commit_before_push` | exact expected-value lease rejects C1 push; C1R is forbidden because C1 was not published |
| `REMOTE-NEG-03` | `bare_remote_advances_after_c1_push_before_activation` | actual remote main differs from C1, so success tuple/Production-Ready are forbidden and reconciliation is required |
| `REMOTE-POS-01` | `fresh_remote_equals_c1_and_scan_head_equals_c1` | activation tuple contains post-push remote C1, scanned HEAD C1 and fresh activation remote C1 before Production-Ready becomes effective |
| `REMOTE-NEG-04` | `remote_moves_to_commit_already_in_local_history_between_check_and_push` | expected-value lease rejects even a fast-forward-compatible/ancestor ref change that an ordinary push could accept |

### External Handoff Schema

`deterministic/closeout_handoff.py` é o único entry point operacional para publicar C0/C1/C1R e fechar activation/recovery. Outputs ficam obrigatoriamente sob `uninotas-foundation/artifacts/tmp/`, devem passar `git check-ignore`, usam JSON UTF-8 strict sem chaves desconhecidas e nunca são persistidos no candidate que referenciam. O helper usa gravação atômica temp→rename e falha sem output de sucesso quando qualquer precondição muda.

Interfaces fechadas:

- `promote --phase c0|c1|c1r --repo <repo> --expected-remote <OID> --new-commit <OID> --candidate-tree <OID> --consumer-bindings <ignored-json> [--base-evidence <ignored-json>] [--proof-bridge <ignored-json>] --output <ignored-json>`: revalida tree/parent/fast-forward/IDs, remote fresh, conjunto exato de consumers e executa o expected-value lease push. Emite phase evidence somente após fresh post-push remote/local checks.
- `activate --phase c1 --repo <repo> --c0-evidence <json> --c1-evidence <json> --delphi-root <path> --output <ignored-json>`: valida schemas/bindings, observa remote C1, executa o Delphi active scan com `scanned_head_oid=C1`, reobserva remote e emite `uninotas-closeout-handoff-v1` production somente se tudo permanecer coerente.
- `activate --phase c1r --repo <repo> --c0-evidence <json> --failed-c1-evidence <json> --c1r-evidence <json> --failure-tuple <json> --delphi-root <path> --output <ignored-json>`: valida reverse bridge/lease/bindings, executa exact two-TODO scan ligado a C1R, reobserva remote e emite handoff recovery com `recovery_effective:true` e `production_ready_effective:false`.

Antes de cada `promote`, o operador executa o Git write authority guard. A suíte usa bare remotes reais e o mesmo entry point; monkeypatch de push/remote/scan não satisfaz a lane de integração.

Schema production `uninotas-closeout-handoff-v1`:

- `c0` e `c1`: `{commit_oid, candidate_tree_oid, commit_tree_oid, tree_equal:true, parent_oid, delivery_scope_set:[...], phase_commit_delta_set:[...]}`;
- `proof_bridge`: `{validator:"validate_closeout_diff.py", base_commit_oid:C0, base_tree_oid, candidate_tree_oid:C1_TREE, exact_delta_set:[...], outcome:"go"}`;
- `consumer_bindings`: conjunto exato/único da matriz normativa abaixo;
- `remote_promotions`: `{c0:{fresh_pre_push_oid, expected_lease_oid, lease_result:"success", parent_and_fast_forward:true, post_push_remote_main_oid:C0, local_head_oid:C0, local_tracking_oid:C0}, c1:{fresh_pre_push_oid:C0, expected_lease_oid:C0, lease_result:"success", parent_and_fast_forward:true, post_push_remote_main_oid:C1, local_head_oid:C1, local_tracking_oid:C1}}`;
- `post_c1_active_scan`: `{scanned_head_oid:C1, outcome:"go", todo_count:1, active_paths:[exact discovery path], stale_transition_path:false}`;
- `actual_remote_main_oid:C1` observado após o scan; `production_ready_effective:true` somente quando todos os campos anteriores são coerentes.

Schema recovery usa `handoff_kind:"recovery"` e inclui `failed_c1`, `c1r` tree equality, reverse proof bridge, failure tuple, bindings C1R, `remote_promotions.c1r` com lease/fresh post-push C1R, `post_c1r_active_scan:{scanned_head_oid:C1R,todo_count:2,active_paths:[exact canonical transition, exact discovery],stale_completed_path:false}`, segunda observação `actual_remote_main_oid:C1R`, `recovery_effective:true` e `production_ready_effective:false`.

#### Required Consumer Binding Matrix

Cada ID aparece exatamente uma vez; ausente, duplicado, inesperado, phase/class/scope diferente ou outcome fora da coluna é no-go. `exact_path_set_source` resolve para a lista materializada no handoff, não somente para um label.

| consumer_id | phase | consumer_class | scope | exact_path_set_source | allowed outcome |
| --- | --- | --- | --- | --- | --- |
| `foundation-validator-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `semantic-suite-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `foundation-suite-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `change-set-suite-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `closeout-handoff-suite-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `paced-readiness-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `diff-expectation-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `profile-scope-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `todo-authority-c0` | C0 | worktree-proxy | implementation_content | `DELIVERY_SCOPE_SET` | `go` |
| `privacy-review-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `architecture-adherence-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `security-review-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `test-quality-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `final-review-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `verification-debt-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `triple-correctness-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `triple-security-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `triple-test-quality-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `performance-concurrency-c0` | C0 | implementation-human-review | implementation_content | `DELIVERY_SCOPE_SET` | `no_material_findings` |
| `closeout-proof-bridge-c1` | C1 | tree-native | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-structure-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `foundation-validator-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `diff-expectation-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `delivery-path-set-c1` | C1 | tree-native | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `lifecycle-path-set-c1` | C1 | tree-native | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `status-evidence-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `profile-scope-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `diff-check-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-authority-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-completion-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-closeout-c1` | C1 | worktree-proxy | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `closeout-integrity-review-c1` | C1 | closeout-human-review | closeout_transform | `PHASE_COMMIT_DELTA_SET` | `no_material_findings` |
| `recovery-proof-bridge-c1r` | C1R | tree-native | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-structure-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `foundation-validator-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `diff-expectation-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `profile-scope-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `diff-check-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-authority-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-completion-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `todo-closeout-c1r` | C1R | worktree-proxy | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `go` |
| `recovery-integrity-review-c1r` | C1R | closeout-human-review | recovery_transform | `PHASE_COMMIT_DELTA_SET` | `no_material_findings` |

| Case ID | Fixture | Expected assertion |
| --- | --- | --- |
| `HANDOFF-POS-01` | `complete_candidate_tree_proof_chain` | schema valida C0/C1 tree equality, exact sets, proof bridge, every required consumer binding, CAS promotion and scan |
| `HANDOFF-NEG-01` | `stale_consumer_binding_in_handoff` | consumer bound to tree different from its phase/proof bridge is rejected |
| `HANDOFF-NEG-02` | `handoff_commit_tree_mismatch` | commit tree unequal to recorded candidate tree blocks Production-Ready |
| `HANDOFF-NEG-03` | `missing_required_consumer_or_exact_path_set` | untyped output list or incomplete binding cannot satisfy the schema |
| `HANDOFF-NEG-04` | `unknown_duplicate_or_wrong_phase_consumer` | strict consumer catalog rejects extra/duplicate/misclassified bindings |
| `HANDOFF-NEG-05` | `missing_or_contradictory_c0_cas_evidence` | production handoff requires complete C0 fresh-pre/lease/post-push/local evidence |
| `HANDOFF-POS-02` | `complete_c1r_recovery_handoff` | C1R reverse bridge, lease, two remote observations and exact two-TODO scan produce recovery-effective only |
| `HANDOFF-NEG-06` | `remote_advances_after_c1r_push_before_or_after_scan` | either C1R remote observation mismatch blocks recovery-effective |
| `HANDOFF-NEG-07` | `c1r_scan_bound_to_different_head_or_worktree` | recovery scan must bind to committed C1R tree and exact active set |

### Atomic Final Closeout Diff Contract

C0 é publicado com implementação pronta, stage `Local-Implemented`, delivery guards/audits vinculados ao candidate tree verdes e este TODO ainda em `active/`. Não existe commit intermediário com TODO incompleto em `completed/`. O staged-tree candidate de C1 parte do HEAD=C0 limpo e pode alterar somente cinco paths finais: source active D, destination completed A, `artifacts/publication-manifest.txt` M, o link deste TODO em `artifacts/feature-briefs/uninotas-smart-notas-central.md` M e o link no TODO de discovery M. Manifesto/backlinks podem somente trocar o path active pelo completed; qualquer outra mudança textual é no-go.

O completed TODO de C1 deve ser semanticamente idêntico ao active TODO de C0, exceto por allowlist de célula/campo:

- `Artifact Identity -> Lifecycle state` muda para `Completed — conditional Production-Ready candidate`;
- `Delivery Status Canon` muda para `Current delivery stage: Production-Ready`, qualifier fixa `conditional — effective only after fresh actual_remote_main_oid==HEAD==origin/main==C1 verification and semantic post-C1 scan bound to scanned_head_oid=C1 with todo_count=1/exact discovery path/no stale transition; failed publication, remote mismatch or scan mismatch invalidates closeout`, e next step fixa `external C1 remote verification + semantic active scan handoff`;
- na row desta entrega em `Promotion Evidence`, somente `Local Branch/Commit`, `PR to main` e `Current Status`; scope/thresholds ficam congelados e nenhum campo tenta registrar o próprio C1 SHA;
- checkboxes, toda `Completion Evidence Matrix` e seus outputs já estão completos em C0 e ficam byte-frozen em C1; nenhum resultado dos guards finais é escrito de volta no TODO;
- History Trust recebe evidência observada de C0 e a verificação precommit de que fresh remote tip, `origin/main` e base HEAD são C0; fatos sobre o OID/push/remote activation de C1 ficam exclusivamente no handoff externo;
- `TODO Closeout Disposition` muda para `move-completed`, razão fixa `candidate C1 guards green; Production-Ready remains conditional on external handoff`, post status `C0 verified; C1 external verification pending` e next action `external C1 verification + active scan handoff`;
- `Post-Push Attestation` registra somente C0 OID/verificação e a descrição fixa do handoff externo de C1.

Os critérios de closeout descrevem o harness/state machine implementado e testado, não tentam armazenar a execução final que os próprios guards produzem. Seus estados exatos são:

| Criterion | C0 active | Candidate C1 completed | External handoff (not persisted in C1) |
| --- | --- | --- | --- |
| `DOD-12` | checked/passed com `CLOSEOUT-POS-01/02` | byte-frozen; nenhum output final embutido | executa a state machine real e conserva outputs externos |
| `DOD-15` | checked/passed com fixtures temporais History Trust/remote race | byte-frozen; C0 observed fields pertencem ao gate, não à evidence row | prova parent/ancestry, fresh remote pre-push, actual remote C1 pós-push e scan bound; mismatch segue estado fail-closed aplicável |
| `VAL-07` | checked/passed com fixture que invoca os guards Delphi reais | byte-frozen | executa a mesma sequência sobre a entrega real |
| `VAL-10` | checked/passed com fixtures C0/C1 pre/post-commit, bare remote advance e activation | byte-frozen | executa C1 post-commit/pre-push/post-push remote checks e vincula scan ao OID observado |

`DOD-14` e `VAL-09` também estão checked/passed em C0 por testes positivos/negativos do guard. Todos os DOD/VAL e evidence rows ficam concluídos antes de formar C0. `CLOSEOUT-POS-02` invoca `todo_authority_guard.py`, `todo_completion_guard.py --require-delivery` e `todo_closeout_guard.py` reais contra um candidate fixture já completo: nenhum wrapper/mock substitui Delphi. A suíte deve provar que nenhuma criterion/evidence row cita como input obrigatório o output do mesmo guard que a fiscaliza (`CLOSEOUT-NEG-08`).

`validate_closeout_diff.py --base C0` valida paths, move e células antes de qualquer completion guard. Deterministic validation, Foundation validator, diff/profile gates, authority, completion e closeout rodam sobre esse mesmo candidate vinculado e seus outputs são anexados ao handoff externo, não ao candidate. Após o commit local, o handoff prova parent/tree, reobserva remote tip=C0 antes do push, publica C1, confirma `post_push_remote_main_oid==HEAD==origin/main==C1`, executa scan com `scanned_head_oid=C1` e reobserva `actual_remote_main_oid=C1` imediatamente antes do tuple. Esses fatos dependentes do OID novo nunca são pré-preenchidos dentro do próprio commit.

O caminho de sucesso não possui C2. Falha externa após C1 publicado divide-se de modo fail-closed:

1. tip remoto real observado por `git ls-remote origin refs/heads/main`, `origin/main` local e `HEAD` são todos `FAILED_C1`, com working tree limpo: recovery C1R é permitido. O tip remoto real é reobservado antes de preparar o candidate, imediatamente antes do commit e imediatamente antes do push. `validate_closeout_diff.py --mode recovery --base <FAILED_C1>` exige exatamente os mesmos cinco paths em sentido reverso.
2. Remote avançou/divergiu, HEAD é incerto ou a igualdade acima falha: nenhum recovery commit/push é autorizado. Preservar o failure tuple externamente, parar e exigir reconciliação de autoridade + `APROVADO` renovado/rebaseline que classifique intervening commits; é proibido forçar push, descartar trabalho ou prometer active set exato antes disso.

No caso 1, a transformação C1→C1R é fechada por campo:

| Surface | Failed C1 value | C1R recovery value |
| --- | --- | --- |
| lifecycle path/state | completed; `Completed — conditional Production-Ready candidate` | reverse move para active; `Active — blocked recovery` |
| Delivery stage | `Production-Ready` condicional | `Local-Implemented`; qualifier `Blocked — external closeout verification failed`; next step `reconcile observed C1 failure and rerun atomic closeout` |
| Active Work State | `review` | `blocked`; reason `published C1 failed external activation`; exit `failure reconciled and exact closeout protocol green` |
| Promotion Evidence | row C1 condicional | somente `Current Status` muda para `C1 external activation failed; C1R recovery in progress`; demais células congeladas |
| Scope/DoD/VAL/Completion Evidence | checked/passed | byte-frozen checked/passed |
| History Trust + LEDGER_GENESIS | C0 evidence/binding | byte-frozen |
| Post-Push `Failed-C1 recovery` | instrução condicional | `failure_id=<stable-id>; failed_c1_oid=<40-lowercase-hex>; predicate=<parent_mismatch|ancestry_failure|head_origin_mismatch|actual_remote_mismatch|semantic_scan_mismatch>; observed=<bounded-redacted-result>; recorded_at_utc=<RFC3339>` |
| TODO Closeout Disposition | `move-completed` | `blocked`; reason `published C1 failed external activation`; post status `FAILED_C1 observed; C1R recovery pending`; next action `publish/verify C1R then reconcile blocker` |
| manifest + two backlinks | completed path | somente troca completed→active |

Todo o restante é byte-frozen. Sobre o candidate C1R rodam recovery boundary, structure/Foundation/diff/profile/authority/completion/closeout e `REVIEW-C1R-01`, cada qual com o consumer ID C1R exato e o mesmo tree. `closeout_handoff.py promote --phase c1r` revalida FAILED_C1/parent/tree/bindings e executa CAS; `activate --phase c1r` exige post-push remote C1R, scan com `scanned_head_oid=C1R` e exact two-TODO active set, seguida de nova observação remote C1R. Só então emite recovery handoff strict com `recovery_effective:true` e `production_ready_effective:false`. Qualquer divergência antes/depois do push ou scan exige reconciliação; recovery nunca mascara o failure tuple.

| Case ID | Fixture | Expected assertion |
| --- | --- | --- |
| `CLOSEOUT-POS-01` | `atomic_move_and_allowed_cells` | C0 active → candidate C1 completed com cinco paths/células exatos é aceito |
| `CLOSEOUT-POS-02` | `completed_path_guard_sequence` | fixture Git temporária executa closeout-diff, structure, authority, completion e closeout sobre o mesmo candidate C1 |
| `CLOSEOUT-POS-03` | `post_c1_semantic_active_scan` | handoff fixture exige fresh actual remote C1, `scanned_head_oid=C1`, `todo_count=1`, active path igual ao TODO discovery e zero stale canonical-transition path |
| `CLOSEOUT-POS-04` | `failed_c1_recovery_to_active` | C1R reverte exatamente cinco paths, persiste failure já observado e restaura active set exato de dois TODOs |
| `CLOSEOUT-NEG-01` | `incomplete_todo_moved_to_completed` | `completed path requires all repository-verifiable criteria complete` |
| `CLOSEOUT-NEG-02` | `unexpected_sixth_path_or_backlink_edit` | `final closeout changed a non-allowlisted path or backlink content` |
| `CLOSEOUT-NEG-03` | `todo_semantic_text_changed` | `final closeout changed frozen contract content` |
| `CLOSEOUT-NEG-04` | `promotion_static_cell_changed` | `final closeout changed frozen promotion scope or threshold cell` |
| `CLOSEOUT-NEG-05` | `self_commit_or_prospective_oid_persisted` | `final closeout cannot persist facts that depend on the uncreated C1 OID` |
| `CLOSEOUT-NEG-06` | `delivery_or_closeout_value_outside_state_machine` | `final closeout used a non-contract stage or disposition transition` |
| `CLOSEOUT-NEG-07` | `post_c1_false_go_zero_or_wrong_active_set` | `post-C1 active scan semantic result does not match the exact remaining active TODO set` |
| `CLOSEOUT-NEG-08` | `criterion_requires_its_enforcing_guard_output` | `completion criterion cannot require its own enforcing guard result as input evidence` |
| `CLOSEOUT-NEG-09` | `failed_published_c1_without_recovery` | `failed external closeout verification requires corrective active-state recovery` |
| `CLOSEOUT-NEG-10` | `recovery_hides_failure_or_changes_scope` | `closeout recovery may only restore lifecycle truth and observed failure evidence` |
| `CLOSEOUT-NEG-11` | `recovery_remote_tip_advanced_or_diverged` | `recovery requires observed remote tip, origin/main and HEAD to equal FAILED_C1; stop for authority reconciliation` |
| `CLOSEOUT-NEG-13` | `bare_remote_advanced_local_tracking_stale` | `fresh ls-remote observation blocks recovery even when local origin/main still equals FAILED_C1` |
| `CLOSEOUT-NEG-14` | `local_commit_remote_advanced_before_push` | `unpublished C0/C1 cannot push or enter published-C1 recovery; reconciliation/rebaseline and renewed approval required` |
| `CLOSEOUT-NEG-15` | `remote_advanced_after_c1_push_before_activation` | `Production-Ready requires fresh actual remote main exactly equal to C1 and scan bound to C1` |
| `CLOSEOUT-NEG-12` | `recovery_field_outside_exact_state_table` | `recovery changed a byte-frozen field or used an invalid failure tuple` |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas OpenAPI | fundamenta a arquitetura-alvo | healthy | 2026-09-25 | fingerprint e probes redigidos no ledger | nenhuma chamada nesta entrega |
| Git remote Foundation | necessário para baseline de revisão | healthy | 2026-09-25 | `main`/`origin/main@ac1ce08`; baseline material R8S publicada; guard main-only instalado e Git for Windows é o writer válido | nenhum ajuste |
| `DEP-CLOSEOUT-01` Delphi standalone closeout support | impede falso `go` e stale active TODO no closeout | healthy/resolved | 2026-09-25 | TODO Delphi concluído em `6dc5bd4`/`0e54e2a`; comando individual retornou `path_state=active`; `--all-active --repo uninotas-foundation` retornou `todo_count=2`, ambos paths ativos reais e zero violações | consumir a correção já publicada e repetir os dois comandos antes do closeout |
| `DEP-CLOSEOUT-STATES-02` Delphi completed/recovery compatibility | final candidate e C1R dependem dos guards atuais sem alteração Delphi | healthy/resolved by pre-approval synthetic probe | 2026-09-25 | exact-shape temp TODOs: completed conditional e active/Blocked recovery retornaram `go` nos três guards reais (`todo_completion_guard --require-delivery`, `todo_authority_guard --require-delivery-gates`, `todo_closeout_guard --repo`); artifacts `artifacts/tmp/r8n-*-probe*.txt` | CI matrix reduzida ao schema canônico e Completion Evidence agora possui 34 bindings literais; repetir nas fixtures source-owned e entrega real |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `operational-coder; assurance-tester-quality`
- **Scope-check command:** pre-implementation bootstrap: `bash -lc 'mapfile -t paths < <({ git -C uninotas-foundation diff --no-renames --name-only 0fe906c1e496a1d38f1603cf188c224711011c32 --; git -C uninotas-foundation ls-files --others --exclude-standard; } | LC_ALL=C sort -u | sed "s#^#foundation_documentation/#"); ((${#paths[@]} > 0)) && python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto "${paths[@]}"'`; pós-capture do candidate: `bash -lc 'mapfile -t paths < <(python3 uninotas-foundation/deterministic/enumerate_change_paths.py --mode delivery --repo uninotas-foundation --baseline 0fe906c1e496a1d38f1603cf188c224711011c32 --candidate-tree <CANDIDATE_TREE_OID> | sed "s#^#foundation_documentation/#"); ((${#paths[@]} > 0)) && python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto "${paths[@]}"'`.
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

O JSON machine-readable de `policies/scope_subscope_governance.md` terá `core_scope=uninotas`, uma coleção ativa `modules`, um catálogo persistente `module_catalog` e uma coleção ordenada `capability_transitions`. Cada módulo ativo declara `subscope`, `path`, `runtime_authority_state`, `owned_capabilities` e `planned_capabilities`; cada array não contém IDs duplicados. Cada entrada do catálogo declara `module_id`, `path` e `catalog_state=active|retired`; `module_id` e `path` são globalmente únicos. Existe uma bijeção exata entre `modules` e entradas `active` do catálogo, com mesmo ID/path. Uma entrada `retired` não pode coexistir em `modules`, possuir ou planejar capability, nem compartilhar ID/path com outra entrada. Cada transição declara `transition_id`, `capability_id`, `sequence`, `origin=transferred|new`, `transition_state=planned|completed`, `predecessor` e `successor`; `transition_id` é globalmente único. `origin=new` exige `sequence=1` e `predecessor=null`; `origin=transferred` sempre exige predecessor não nulo presente no `module_catalog`, inclusive em arestas históricas completed; toda aresta posterior à primeira usa `origin=transferred`. `runtime_authority_state=current_runtime|target_planned` é um eixo distinto do lifecycle PACED de `evolution_lifecycle.md`; ele responde somente qual módulo possui autoridade sobre comportamento executável observado. Um `target_planned` sempre tem `owned_capabilities=[]` e pelo menos um ID em `planned_capabilities`. Um módulo `current_runtime` possui pelo menos um ID em `owned_capabilities`, pode manter outros em `planned_capabilities` e preserva conjuntos disjuntos. Nenhum módulo ativo pode ter ambos os arrays vazios.

O mesmo JSON terá um `baseline_capability_catalog` histórico e imutável, autoridade única para IDs que já existiam antes deste cutover. Cada entrada contém somente `capability_id` e `baseline_owner`; ambos são únicos e não podem ser apagados, renomeados ou receber alias. Seu conjunto deve permanecer exatamente igual à projeção `capability_id`/`baseline_owner` das rows `origin=baseline` presentes na versão do ledger em C0; não basta ser um subconjunto estável do seed. Capabilities posteriores não entram retroativamente nesse catálogo: toda row adicionada depois de C0 deve usar `origin=new`, e sua identidade nasce em uma aresta sequence 1 `origin=new`. Todo ID em owned/planned/transitions deve ser coberto por exatamente uma origem: entrada baseline ou cadeia cuja primeira aresta é `origin=new`. Um ID baseline sem transição permanece exatamente no `baseline_owner`; quando possui transição, sua cadeia terminal governa ownership/planned pelas regras abaixo. Um ID não catalogado não pode aparecer diretamente em `owned_capabilities`; ele só pode se tornar owned por uma cadeia `origin=new` terminal completed. Desaparecimento/rename de baseline, alias, append baseline pós-C0 e inserção current direta sem origem são inválidos.

| Baseline capability ID | Baseline owner |
| --- | --- |
| `note_read_model` | `events-and-classification` |
| `integration_error_read_model` | `events-and-classification` |
| `operational_workflow` | `treatments-and-history` |
| `authentication` | `identity-and-team` |
| `team_profiles` | `identity-and-team` |
| `legacy_log_invalidation` | `realtime-invalidation` |
| `legacy_log_monitoring` | `operational-monitoring` |
| `runtime_topology` | `runtime-and-deployment` |
| `health_read` | `runtime-and-deployment` |

`deterministic/capability_identity_ledger.json` é o oracle de enforcement independente da projeção mutável acima. Ele contém registros normalizados append-only: baseline usa `capability_id`, `origin=baseline`, `baseline_owner`; capability nova usa `capability_id`, `origin=new`, `origin_transition_id`. O seed inicial completo — as nove rows baseline mais `fiscal_document_read` como primeiro registro `origin=new` ligado a `fiscal-document-read-001` — é ancorado por `FROZEN_INITIAL_CAPABILITY_IDENTITY_DIGEST` em `validate_foundation.py`, seguindo o padrão fail-closed já usado pelo frozen legacy ledger.

A representação canônica versionada `capability-identity-ledger-v1` governa digest e comparação semântica. O parser rejeita chaves extras/ausentes e normaliza cada row para exatamente os campos permitidos por sua origem; rows são ordenadas por `capability_id` em ordem Unicode code-point (os IDs contratados permanecem ASCII). O array é serializado em UTF-8 como JSON minificado com chaves lexicograficamente ordenadas, `ensure_ascii=false`, separators `(',', ':')`, sem BOM ou newline final; o digest é SHA-256 lowercase hexadecimal desses bytes. Whitespace, indentação e ordem original de chaves/rows não mudam a identidade; qualquer mudança em `capability_id`, `origin`, `baseline_owner` ou `origin_transition_id` muda a forma canônica e deve falhar. O seed digest aplica-se exatamente às dez rows iniciais, identificadas pelo conjunto congelado de IDs, enquanto a comparação histórica aplica a mesma canonicalização a cada record.

`capability_id` é único no ledger e os conjuntos `origin=baseline`/`origin=new` são disjuntos. Cada row `origin=new` corresponde bijetivamente a exatamente uma transition sequence 1 `origin=new` com o mesmo `capability_id` e `transition_id=origin_transition_id`; toda cadeia cuja primeira aresta é `origin=new` possui exatamente essa row. Transition ausente, transition de outra capability, ID duplicado ou conflito baseline/new é inválido antes de qualquer persistência histórica.

O validator full-tree usa `LEDGER_GENESIS=C0_PRE_MOVE`, o primeiro commit publicado que contém o ledger, preenchido e congelado no completed TODO em C1. Em todo HEAD posterior, ele deriva independentemente o primeiro commit da ancestry first-parent que introduziu `deterministic/capability_identity_ledger.json` e exige igualdade exata com o C0 registrado; apontar o campo para um descendente resolvível é no-go. Uma exceção bootstrap fechada aceita genesis pending somente em dois estados: (a) candidate pre-C0 com TODO ativo, HEAD sem ledger histórico e working tree contendo exatamente o seed canônico; ou (b) checkout limpo cujo `HEAD` é ele próprio o primeiro commit que introduziu o ledger e ainda contém exatamente o seed. Qualquer descendant de C0 com genesis pending/ausente falha; C1 deve registrar o OID exato de C0. Antes e durante esse bootstrap, o frozen initial digest ancora as dez identidades. Depois de C0, o validator exige repositório não shallow, nenhum replace/graft, genesis resolvível e ancestor de `HEAD`. Uma única consulta `git log --first-parent --reverse --format=%H -- <ledger-path>` enumera apenas commits que mudaram o ledger; o validator carrega exatamente essas versões, incluindo C0. Para cada par consecutivo, a versão posterior deve ser superconjunto semântico imutável da anterior sob `capability-identity-ledger-v1`; remoção→reintrodução ou mutação→reversão falha na versão intermediária, mesmo quando a versão final coincide. A união acumulada deve existir no ledger corrente. O conjunto de rows `origin=baseline` e sua projeção no `baseline_capability_catalog` permanecem exatamente os de C0; toda identidade aparecida pela primeira vez depois de C0 deve ser `origin=new`. Histórico ausente, truncado, shallow, non-descendant, com replacement, C0 substituído por descendente ou baseline retroativo é no-go, nunca fallback para o registry atual.

A única binding machine-readable de `LEDGER_GENESIS` é o campo Markdown exato `**C0 active implementation/genesis commit:**` sob o heading único `## Post-Push Attestation (Atomic Final Closeout)`, no único path lifecycle existente deste TODO: active antes do move ou completed depois dele. O valor bootstrap literal é `pending delivery — persisted in C1 after observation`; fora dos dois estados bootstrap fechados, o valor deve começar por exatamente um OID lowercase `^[0-9a-f]{40}$` seguido apenas de descrição fixa allowlisted. Campo/heading ausente, duplicado, malformado, divergente, ou presença simultânea dos paths active/completed é no-go. O atomic-closeout guard permite a troca do literal pelo OID C0 observado uma única vez em C1; recovery preserva esse OID. Nenhum outro C0 mencionado em tabelas/prosa é fonte para o validator.

O contrato de custo limita o que é observável deterministicamente: uma consulta path-limited `git log` encontra os OIDs relevantes e há no máximo uma leitura `git show` por versão, com `git_calls <= k + 2`. A consulta Git ainda pode percorrer internamente o histórico total; portanto não há claim assintótico independente do número de commits. `CAP-POS-11` constrói repositório com 200 commits não relacionados e cinco mudanças após C0, exige seis versões/até oito subprocess calls e registra wall-clock apenas como tendência advisory.

A garantia automatizada é deliberadamente limitada à linhagem first-parent observável desde C0. Uma reescrita remota alternativa que preserve C0 mas remova descendentes confiáveis não pode ser detectada sem âncora fora da branch; ela é risco residual explícito `RISK-HIST-01`, não promessa fail-closed. Antes de cada delivery, os gates registram evidência disponível de proteção/non-fast-forward do remote; ausência dessa proteção não é convertida em falsa prova e exige aceitação humana no `APROVADO` ou rebaseline independente futuro. Validadores puros recebem snapshots históricos explícitos; testes usam repositório Git temporário real e incluem uma limitação documentada para dois descendentes alternativos do mesmo genesis. Assim, o digest protege sempre o seed inicial e o histórico protege identidades posteriores somente dentro da linhagem confiável observável.

Os IDs de capability são estáveis entre predecessor e successor: `note_read_model`, `integration_error_read_model` e `operational_workflow` têm `origin=transferred` e não mudam durante a transferência. `fiscal_document_read` tem `origin=new`, sem predecessor. Para cada módulo, `owned_capabilities ∩ planned_capabilities = ∅`. A cadeia de cada capability tem `sequence` inteira, única e contígua iniciando em `1`; a aresta `n+1` deve ter `predecessor=successor` da aresta `n`; nenhum fork, ciclo, alias, gap ou módulo ausente do `module_catalog` é válido. Toda aresta não terminal deve estar `completed`; somente a aresta terminal (maior `sequence`) governa ownership/planned atuais. Arestas concluídas anteriores preservam proveniência, mas não exigem que seus successors continuem owners. O conjunto governado de capabilities é exatamente a união do `baseline_capability_catalog` com IDs cuja cadeia começa em `origin=new`; owned/planned/transitions são estados/referências desse universo, não sua autoridade de identidade. `capability_transitions` registra somente capability nova planejada ou transferência real/histórica: uma capability baseline estável sem transição é válida exatamente quando aparece uma única vez em `owned_capabilities` do `baseline_owner` ativo `current_runtime` e zero vezes em `planned_capabilities`; não se inventa aresta histórica para ela.

Quando a aresta terminal está `planned`, uma transferência exige exatamente um owner `current_runtime` no predecessor ativo e exatamente um planned membership no successor ativo; o successor deve existir em `modules`. Uma capability nova na primeira aresta exige zero owners atuais, exatamente um planned membership no successor, `origin=new` e `predecessor=null`; essa capability ainda é intenção target, não capability runtime ativa. Quando a aresta terminal está `completed`, exige exatamente um owner no successor `current_runtime` e zero planned memberships. Cada ocorrência em `planned_capabilities` possui relação bijetiva com exatamente uma aresta terminal `planned` do mesmo `capability_id` cujo `successor` é o módulo que contém a ocorrência; planned membership sem essa aresta, ou uma aresta planned com membership ausente/duplicada, é inválida. Uma nova aresta multi-hop só pode ser acrescentada depois que a anterior está `completed`; ela usa `origin=transferred` e parte do owner current anterior.

Promoção é atômica por capability: no mesmo diff, o TODO implementador remove o ID de `owned_capabilities` do predecessor quando `origin=transferred`, remove o ID de `planned_capabilities` do successor, adiciona o ID a `owned_capabilities` do successor, muda a aresta terminal para `completed` e atualiza `runtime_authority_state` e index aplicáveis. Em uma aresta terminal `completed`, o successor deve existir como `current_runtime`, ser o único owner e não pode conservar planned membership. Predecessor/successor de qualquer aresta histórica permanecem no `module_catalog`; um módulo pode virar `retired` apenas quando não possui nem planeja capabilities. Um predecessor com capabilities restantes continua `current_runtime`; sem nenhuma, sai de `modules`, mas permanece `retired` no catálogo. Promoção parcial é válida: o successor passa a `current_runtime`, possui as capabilities concluídas e mantém capabilities ainda `planned` em seu conjunto planejado. Na segunda transferência `A -> B -> C`, a aresta histórica concluída `A -> B` permanece válida mesmo após B deixar de ser owner; somente a aresta terminal `B -> C` determina owner/planned atuais.

Uma entrada `module_catalog.catalog_state=retired` é um tombstone histórico, não um documento publicado: preserva o último `module_id` e path canônico somente para proveniência de transições, mas o path deve estar ausente de `modules`, do filesystem publicado e do manifesto exato. Descoberta full-tree considera somente entries `active`; links canônicos vivos para tombstones são inválidos e referências históricas usam o `module_id`/transition, não um link de arquivo quebrado. Reativação futura exige mudança atômica explícita para `active`, recriação do documento/manifest entry e nova autoridade aprovada; enquanto retired, existência do arquivo ou manifest entry é erro.

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
- [x] `TD-04` O registry usará `runtime_authority_state=current_runtime|target_planned`, distinto do lifecycle PACED, `baseline_capability_catalog` para identidades preexistentes confrontado com identity ledger independente digest+Git-history e `capability_transitions` persistentes com `planned|completed`. IDs estáveis transferem atomicamente; planned nunca concede autoridade; as regras pré/pós-promoção e de capability nova são as congeladas no registry contract.
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
| `n/a` | identidade canônica UniNotas | Add from `TD-01` | `D-06`: produto `UniNotas`, `core_scope=uninotas`, repositório técnico preservado |
| `n/a` | autoridade de dados Current/Target | Add from `TD-02` + `TD-07` | `D-07`: Smart Notas para notas/documentos, PostgreSQL somente falhas e writer/filter desconhecido |
| `n/a` | contextos fiscais sem tenancy | Add from `TD-03` | `D-08`: Unifast e Prosperar são `FiscalIssuerContext`, sem agregação implícita |
| `n/a` | nova autoridade runtime por capability | Add from `TD-04` | `D-09`: eixo runtime separado do lifecycle, com catálogo, ledger e transições persistentes |
| `n/a` | novos owners alvo | Add from `TD-05` | `D-10`: três owners alvo e limites exclusivos |
| `n/a` | inventário ativo único | Add from `TD-06` | `D-11`: manifesto é inventário ativo exato; Git permanece recovery histórico |

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
- [x] `TD-04` O eixo de autoridade runtime, baseline capability catalog confrontado com ledger digest+Git-history, IDs estáveis, proveniência persistente e condições pré/pós-promoção impedem coordinated delete/alias, overlap, gap ou planned membership residual sem competir com o lifecycle PACED.
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
| test | privacy boundary | valid formatted/compact CNPJ + high-confidence contextual provider-ID/document-URL mutations | captured business/provider values without banning official docs or generic IDs | implement-in-this-todo | mutation RED/GREEN com diagnóstico específico |
| review | residual privacy boundary | `REVIEW-PRIV-01` checklist sobre diff/path esperado | valor contextual privado fora dos padrões automatizáveis | implement-in-this-todo | attestation externa com reviewer, candidate tree OID, exact paths e resultado, sem reproduzir valor sensível |
| review | architecture | independent architecture/adherence review | supersede incompleto | implement-in-this-todo | review artifacts |

### Deterministic Privacy Predicate

O scanner opera sobre o texto governado publicado pelo manifesto e sobre fixtures puras sem persistir valores reais. A gramática reconhecida é line-oriented e fechada: (1) env/assignment `KEY=VALUE`, com `export` opcional; (2) YAML ou item de lista `KEY: VALUE`, com `-` opcional; (3) JSON de uma linha `"KEY": VALUE`; e (4) tabela Markdown, em que uma célula com chave reconhecida usa a célula imediatamente seguinte como valor. Linhas dentro de fenced code blocks são examinadas pela mesma gramática. Inline code sem par, links Markdown, prosa livre e estruturas multilinha não são inferidos e pertencem ao checklist `REVIEW-PRIV-01`.

Após extração, chaves são normalizadas por Unicode NFKC, separação de camelCase, `casefold` e substituição de espaço/hífen por `_`; valores removem somente whitespace e uma camada externa de aspas/backticks. Para URL, scheme/host são comparados em lowercase e percent-decoding ocorre exatamente uma vez. Não há heurística probabilística. `GUARD-PRIV-02`, `GUARD-PRIV-03`, `GUARD-PRIV-04`, `GUARD-PRIV-POS-01` e `GUARD-PRIV-POS-02` são parametrizados sobre as quatro sintaxes suportadas, incluindo fenced examples, cada família de chave e pares rejeitados/permitidos.

- `GUARD-PRIV-01` reconhece somente candidatos compactos `(?<!\d)\d{14}(?!\d)` ou formatados `(?<!\d)\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}(?!\d)`, confirma os dígitos verificadores e rejeita os válidos; fixtures constroem o valor durante o teste para que nenhum CNPJ válido fique versionado. Outras representações ficam em `REVIEW-PRIV-01`.
- Credenciais concretas são rejeitadas quando uma atribuição ou par estruturado usa `smart_notas_unifast_token`, `smart_notas_prosperar_token`, `smart_notas_unifast_cnpj`, `smart_notas_prosperar_cnpj`, `authorization` ou `bearer_token` com valor não permitido.
- `GUARD-PRIV-02` cobre as chaves normalizadas `id_interno`, `provider_id` e `smart_notas_note_id`; qualquer valor concreto nessas chaves é privado.
- `GUARD-PRIV-03` cobre `pdf_url`, `xml_url`, `danfe_url`, `document_url` e `smart_notas_document_url`; qualquer URL concreta nessas chaves é privada.
- Valores permitidos são somente vazio, `<redacted>`, `<placeholder>`, `REDACTED`, referência `${NOME_DA_VARIAVEL}` bem formada ou URL sob `https://example.invalid/`. O único URL oficial real permitido pela regra é a raiz pública `https://app.smart-notas.com/api/docs`, quando não aparece como valor de uma chave de documento capturado.
- `GUARD-PRIV-04` exige diagnóstico por família (`token credential`, `CNPJ credential`, `authorization credential`) e rejeita qualquer valor concreto nas chaves reconhecidas; a chave CNPJ não depende do checksum de `GUARD-PRIV-01`. `GUARD-PRIV-POS-02` prova cada placeholder permitido em cada família/sintaxe para impedir tanto bypass quanto falso positivo.
- Nomes de chave sem valor, IDs genéricos fora das chaves reconhecidas e menções textuais à API não são rejeitados. Variantes não cobertas pelo predicado ficam exclusivamente em `REVIEW-PRIV-01`; o checklist registra externamente candidate tree OID/exact paths/reviewer/conclusão sem copiar o candidato sensível e é invalidado se o OID mudar.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `running`
- **Decision review evidence / resolution:** `R8S considerou a arquitetura pronta, mas a crítica exigiu entry point executável do handoff real, C0 CAS evidence, C1R recovery handoff e consumer IDs fechados; integrados, portanto baseline/revisão R8T é obrigatória`
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
- **Baseline commit:** `ac1ce08fc5d31c3b205e275220925f137e5c24f5`
- **Baseline push reference:** `origin/main`
- **Gate status:** `findings_integrated`
- **Findings summary:** os achados R8R foram integrados e a baseline material R8S imutável foi publicada somente como evidência de revisão.
- **Evidence / reference:** `origin/main@ac1ce08`; merges derivados `uninotas-r8r-architecture-merge.json` e `uninotas-r8r-critique-merge.json`; monotonic ledger, exact CAS, phased reviews e typed handoff integrados.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** decisões materiais devem permanecer idênticas ao baseline revisado.
- **Trigger stage:** `after planning reviews converge and before APROVADO`
- **Baseline source:** `Gate: Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `template canonical set`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Gate status:** `not_run`
- **Findings summary:** baseline material R8S publicada; arquitetura/crítica R8S e o guard de drift ainda não foram concluídos.
- **Evidence / reference:** freeze `origin/main@ac1ce08fc5d31c3b205e275220925f137e5c24f5`; este SHA deve ser exatamente o consumido pelo drift guard após convergência.
- **Waiver authority / reference:** `n/a`

## Gate: History Trust Evidence

- **Gate decision:** `required`
- **Why this decision:** identidade pós-seed depende da linhagem first-parent observável e não existe âncora externa independente nesta entrega.
- **Trigger stage:** `precommit base check + post-commit fresh remote pre-push check for C0/C1 + post-C1-push remote activation check`
- **Protection evidence rule:** registrar somente proteção non-fast-forward observável; `unavailable` é estado permitido apenas com `APROVADO` que aceita `RISK-HIST-01`, nunca prova positiva.
- **Gate status:** `not_run`
- **Findings summary:** `pending delivery; human acceptance is pending explicit APROVADO`.
- **Evidence / reference:** rows faseadas abaixo; nenhuma credencial/API adicional será usada para consultar configuração remota.
- **Waiver authority / reference:** `n/a — residual risk acceptance is part of Approval, not a technical waiver`

| Phase | Precommit observed remote/base | Post-commit actual OID evidence | Non-fast-forward protection evidence | Persistence / result |
| --- | --- | --- | --- | --- |
| `C0` | pending `BASE_HEAD==BASE_REMOTE_OID; fresh remote exact` | pending `parent(C0)=base; tree binding; fast-forward proof; exact expected-value lease result` | `unavailable unless directly observable` | lease rejection enters external local-unpublished-diverged; success facts persist in C1 |
| `C1` | pending `fresh remote OID=C0 and base HEAD=C0` | external `parent(C1)=C0; tree binding; fast-forward proof; exact lease; post_push_remote_main_oid=C1; scanned_head_oid=C1; actual_remote_main_oid=C1 before tuple` | `unavailable unless directly observable` | lease rejection enters local-unpublished-diverged; either post-push mismatch forbids activation and requires reconciliation |

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

## Frontend / Consumer Matrix

| Producer Surface In This TODO | Consumer | Delivery State | Evidence / Waiver |
| --- | --- | --- | --- |
| `none — documentação canônica e harness determinístico somente` | `n/a` | `not_triggered — nenhum endpoint, job, payload, schema runtime, projection, webhook ou read model executável será criado/alterado` | limites de Scope/Out of Scope; os producers e consumers planejados pertencem aos TODOs futuros NestJS/React e exigirão matrizes próprias, portanto não há ausência de consumer a dispensar nesta entrega |

### Test Strategy

- **Strategy:** `test-first`
- **Why:** o validator é o harness arquitetural; cada semântica precisa de mutação negativa antes do cutover.
- **Fail-first target(s):** identidade/core scope UniNotas, source split, context-not-tenant, runtime-authority/lifecycle separation, módulo/catálogo ausente ou duplicado, membership duplicado, remoção/rename/alias simples ou coordenada de capability baseline/new contra digest/histórico, capability current sem baseline ou `origin=new`, bijeção exata entre cada ledger record `origin=new` e uma única transição sequence 1 `origin=new` da mesma capability (`CAP-NEG-38..42`), substituição do genesis registrado por descendente (`CAP-NEG-43`), append pós-C0 reclassificado como baseline (`CAP-NEG-44`), bootstrap pre-C0/C0/C1 e descendant pending inválido (`CAP-POS-12..14`/`CAP-NEG-45`), canonicalização/digest semântico (`CAP-POS-15`/`CAP-NEG-46`), binding genesis única/exata (`CAP-NEG-47..51`), histórico monotônico inclusive remove→readd/mutate→revert (`CAP-NEG-52/53`) e longo com leituras limitadas (`CAP-POS-11`), módulo ativo vazio ou com cardinalidade incompatível, sequence gap, fork/ciclo, predecessor desconhecido ou nulo em transferência, chain edge inválida, interseção owned/planned, target com owned capability, aresta terminal planned sem exatamente um owner atual ou successor planejado, planned membership órfã, terminal completed sem owner successor, transferência planned sem owner predecessor, dupla autoridade pelo mesmo ID, successor planejado duplicado, planned membership residual, owner incompatível com aresta terminal, ownership baseline estável respaldado pelo catálogo/ledger sem transição sintética, capability nova legítima e ownerless enquanto planned, append de identidade nova, predecessor retirado legítimo, segundo hop planned/completed, limitação documentada de rewrite alternativo que preserva C0 (`CAP-LIMIT-01`/`RISK-HIST-01`), manifesto único, CNPJ válido, credenciais, provider ID/URL privada em contexto formalizado, limites permitidos sem falso positivo, candidate/review binding (`TREE-POS-01..03`/`TREE-NEG-01..08`), handoff tipado (`HANDOFF-POS-01`/`HANDOFF-NEG-01..03`), recovery remote (`CLOSEOUT-NEG-13`) e CAS promotion/activation (`REMOTE-POS-01`/`REMOTE-NEG-01..04`/`CLOSEOUT-NEG-14..15`).
- **`D-T01` evidence layer:** validadores puros + fixtures mínimas são a camada primária para semântica de registry, decisões e privacidade.
- **`D-T02` compatibility layer:** poucos testes full-tree comprovam manifesto, links, symlinks, legado e composição real da Foundation.
- **`D-T03` topology/exclusion:** nenhum banco, API, browser, container ou dado fiscal real é necessário; `CAP-NEG-36/52/53` usam repositório Git temporário real para provar append-only monotônico, inclusive remove→readd e mutate→revert, sem mock de Git.
- **`D-T04` gate:** cada caso `CAP-*`/`GUARD-*` deve falhar antes da implementação correspondente e passar depois, com diagnóstico específico; `REVIEW-PRIV-01` é evidência manual separada e não conta como fixture; suíte agregada sozinha não satisfaz o critério.
- **`D-T05` performance evidence:** casos semânticos ficam em `test_registry_semantics.py`/`test_privacy_predicate.py` e executam zero cópias/scans full-tree; somente `FoundationTreeContractTests.test_manifest_matches_published_tree`, `test_symlink_and_legacy_contracts` e `test_registry_composes_with_module_files` podem varrer a árvore, uma vez cada. Change-set/closeout tests usam repositórios Git mínimos e também zero scans da Foundation completa. O history helper usa uma consulta first-parent limitada ao path do ledger e no máximo uma leitura por versão retornada; `CAP-POS-11` exige seis versões visitadas e `git_calls <= 8` apesar de 200 commits não relacionados. Hard gates são scan count `<=3`, history calls `<=k+2` e nenhum helper com full-tree scan. Duração pure/full-tree e dos helpers é registrada como tendência advisory; a observação histórica de ~179s não bloqueia isoladamente sem protocolo de máquina/repetição comparável.

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

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundation pure semantic suite | registry/privacy; CAP/GUARD em memória, zero full-tree scan | `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_registry_semantics.py uninotas-foundation/deterministic/tests/test_privacy_predicate.py` | Local-Implemented | planned | command output + duração + scan counter=0 | falha se qualquer fixture copiar/varrer a árvore |
| Foundation full-tree compatibility | manifesto, symlink/legado e registry↔módulos; três scans allowlisted | `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py` | Local-Implemented | planned | command output + duração + scan counter<=3 | somente três testes nomeados varrem a árvore uma vez cada |
| Foundation change-set helper | delivery/lifecycle, D/A, R, untracked e source pós-baseline em Git temporário | `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_enumerate_change_paths.py` | Local-Implemented | planned | command output | helper único; mode-specific expectations |
| Foundation atomic closeout/handoff | C0→C1/C1R, dual-set, proof bridge, strict consumer/schema e real atomic CAS/activation em Git temporário | `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_closeout_diff.py uninotas-foundation/deterministic/tests/test_closeout_handoff.py` | Local-Implemented | planned | command output | usa bare remote/entry point real e rejeita stale bindings, invalid phase evidence, tree divergence e remote races antes/depois do push/scan |
| Foundation core-validator performance | subprocess/blob reads, scan count e wall-clock advisory | executar pure/full-tree sequencialmente e medir history/change-set/closeout | Local-Implemented | planned | hard counters + advisory timings | hard: scans<=3, history calls<=k+2, zero helper full-tree |
| Foundation validator | árvore canônica completa | `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation` | Local-Implemented | planned | command output | deve eliminar mismatch |
| PACED readiness | alias/artefatos continuam inicializáveis | `'/mnt/c/Program Files/Git/bin/bash.exe' -lc 'cd /c/Unifast/MonitorDeNotas && bash delphi-ai/verify_context.sh'` | Local-Implemented | planned | command output | runner Git Bash; limitação CRLF WSL isolada |

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
- [ ] `RISK-HIST-01` Uma reescrita alternativa de `main` que preserve C0 mas apague descendentes não é detectável somente pela branch reescrita. O seed inicial continua protegido por digest; identidades pós-seed dependem da linhagem first-parent observável e de governança externa non-fast-forward. O `APROVADO` deste TODO aceita esse limite até existir âncora externa independente; qualquer rewrite conhecido exige parar e rebaseline humano.

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
| `PACKAGE-R8A-01` | both formal reviews R8A | Resolved package defect | pacote por índice não era autossuficiente; R8B repetiu a rubrica completa com o TODO integral embutido |
| `ARCH-R8B-01` / `CAP-R8-01` | architecture opinion + critique R8B | Integrated | conjunto governado/cardinalidade terminal explícitos, bijeção planned membership↔terminal planned e `CAP-NEG-23/24` fecham ownerless legítimo versus órfão inválido |
| `TEST-R8-01` | formal critique R8B | Integrated | `GUARD-PRIV-02` virou fixture automática de contexto formalizado e `REVIEW-PRIV-01` tornou a revisão residual evidência separada |
| `STATE-R8-01` / `OPS-R8B-01` | both formal reviews R8B | Integrated | remote readiness, next step e baseline lifecycle foram reconciliados e exigem novo freeze R8C |
| `ROUTING-R8-01` | formal critique R8B | Integrated | ação atual é formal-review; implementação fica provisória e exige novo guard após APROVADO |
| `ARCH-R8C-01` | formal architecture review R8C | Integrated | capability baseline estável sem transição possui cardinalidade explícita e `CAP-POS-07`, sem proveniência sintética |
| `CRIT-R8C-01` | formal critique R8C | Integrated | toda aresta transferred exige predecessor não nulo no catálogo; `CAP-NEG-25` cobre inclusive historical completed |
| `CRIT-R8C-02` | formal critique R8C | Integrated | arrays são únicos, estados de módulo têm mínimos explícitos e `CAP-NEG-26..30` cobrem duplicata/vazio/incompatibilidade |
| `CRIT-R8C-03` | formal critique R8C | Integrated | predicado de privacidade congela normalização, context keys, placeholders, URL oficial e fixtures negativa/positiva; residual permanece manual |
| `OPS-R8C-01` / `CRIT-R8C-04` | both formal reviews R8C | Integrated | gate, next step e closeout apontam para novo freeze R8D, sem referência pendente à baseline já publicada |
| `ARCH-R8D-CLEAN` | formal architecture review R8D | Accepted | zero achados; ownership, transições, cardinalidades e privacy predicate foram considerados arquiteturalmente prontos |
| `CRIT-R8D-01` | formal critique R8D | Integrated | canonical change-set enumerator une baseline diff e untracked, alimenta profile/diff/human review e fecha rename D/A→R |
| `CRIT-R8D-02` | formal critique R8D | Integrated | `DOD-12`/`VAL-07` e Final-tree closeout revalidam manifesto, TODO e guards após move e vinculam Production-Ready ao SHA final |
| `CRIT-R8D-03` | formal critique R8D | Integrated | retired catalog entry é tombstone histórico não publicado; `CAP-POS-08`/`CAP-NEG-31` fecham filesystem/manifest/discovery |
| `CRIT-R8D-04` | formal critique R8D | Integrated | grammar line-oriented, candidate boundaries e fixtures por sintaxe tornam o privacy parser reproduzível; unsupported vai ao checklist |
| `CRIT-R8D-05` | formal critique R8D | Integrated | D-T05 separa pure/full-tree, allowlista três scans, mede lanes e exige adjudicação acima do baseline/contador |
| `CAPABILITY-IDENTITY-R8E-01` | formal architecture review R8E | Integrated | `baseline_capability_catalog` preserva IDs/owners históricos; qualquer ID vem do baseline ou de sequence 1 `origin=new`; `CAP-NEG-32..34` fecham delete/rename/direct-current |
| `CRIT-R8E-01` | formal critique R8E | Integrated | canonical path-set usa name-only+untracked e é a única entrada dos consumidores; status/rename é view separada |
| `CRIT-R8E-02` | formal critique R8E | Integrated | `Lane-Promoted` e threshold são n/a; baseline push é review evidence e somente SHA final pode ser Production-Ready |
| `GATE-STATE-R8E-01` / `CRIT-R8E-03` | both formal reviews R8E | Integrated | baseline/drift lifecycle será vinculado ao mesmo SHA R8F antes da próxima revisão |
| `ARCH-R8F-01` / `CRIT-R8F-02` | both formal reviews R8F | Integrated | identity ledger append-only usa frozen initial digest + união histórica Git fail-closed; coordinated erasure possui `CAP-NEG-35/36` |
| `OPS-R8F-01` / `CRIT-R8F-01` | both formal reviews R8F | Integrated | helper único usa `--no-renames`, untracked e C-sort; profile consome helper; `CHANGESET-*` cobre D/A, R e untracked |
| `CRIT-R8F-03` | formal critique R8F | Integrated | closeout C1 delivery tree + C2 attestation-only elimina commit contendo o próprio SHA; handoff externo reporta ambos |
| `CRIT-R8F-04` | formal critique R8F | Integrated | `GUARD-PRIV-04`/`POS-02` cobrem cada credential-key family, sintaxe, fenced example, concrete value e placeholder com diagnóstico específico |
| `ARCH-R8G-01` | formal architecture review R8G | Integrated | helper único separa net delivery `0fe..C1` de lifecycle `C0..C1`; `CHANGESET-POS-05` cobre source criado após baseline |
| `ARCH-R8G-02` / `CRIT-R8G-03` | architecture + critique R8G | Integrated | trust boundary exige non-shallow/no-replace, genesis C0 ancestor, first-parent completo e main não reescrita; `CAP-POS-10`/`NEG-37` cobrem completude |
| `CRIT-R8G-01` | formal critique R8G | Integrated | completion/authority/closeout rodam somente no working tree C2 depois de C1 publicado; push C2/active scan ficam no handoff externo |
| `CRIT-R8G-02` | formal critique R8G | Integrated | `validate_attestation_diff.py` compara C2 contra C1, limita um path/campos allowlisted e possui matriz `ATTEST-*` |
| `ARCH-R8H-01` / `CRIT-R8H-04` | architecture + critique R8H | Integrated with explicit residual risk | garantia automatizada cobre sempre o seed congelado e identidades posteriores somente na linhagem first-parent observável; rewrite alternativo preservando C0 é `RISK-HIST-01`, aceito somente pelo `APROVADO` humano |
| `CRIT-R8H-01` | formal critique R8H | Integrated | C0 OID e verificação remota são preenchidos em C1 e ficam fora da allowlist C2; `ATTEST-NEG-04` rejeita sua mutação |
| `CRIT-R8H-02` | formal critique R8H | Integrated | interface real do Delphi diff guard permanece independente; helper project-owned alimenta somente profile/lifecycle/revisão humana, sem integração inventada |
| `CRIT-R8H-03` | formal critique R8H | Integrated | ledger `origin=new` e transição sequence 1 `origin=new` formam bijeção por capability; `CAP-NEG-38..42` cobrem ausência, mismatch, duplicata e conflito de origem |
| `ARCH-R8I-01` | formal architecture review R8I | Integrated | C1 grava C0 OID/verificação; C2 os preserva byte-for-byte e acrescenta somente C1/evidence allowlisted; steps 3/6/7 e attestation wording foram alinhados |
| `ARCH-R8I-02` / `CRIT-R8I-04` | architecture + critique R8I | Integrated | `D-T05` ganhou row de aderência e D-06..D-11 possuem rows explícitas com origem TD e autoridade resultante |
| `CRIT-R8I-01` | formal critique R8I | Integrated | validator deriva o primeiro commit first-parent que introduziu o ledger e exige igualdade com C0 registrado; `CAP-NEG-43` rejeita descendente substituto |
| `CRIT-R8I-02` | formal critique R8I | Integrated | baseline catalog deve igualar exatamente a projeção baseline de C0; toda identidade pós-C0 usa `origin=new`; `CAP-NEG-44` cobre append baseline coordenado |
| `CRIT-R8I-03` | formal critique R8I | Integrated | comandos C1/C2 completos usam o completed path para structure/diff/authority/completion/closeout; `ATTEST-POS-02` valida a sequência em fixture Git |
| `CRIT-R8I-05` | formal critique R8I | Integrated | history helper visita apenas commits first-parent que mudam o ledger, com `git_calls<=k+2`; `CAP-POS-11` cobre 200 commits alheios e seis versões |
| `ARCH-R8J-01` / `CRIT-R8J-01` / `CRIT-R8J-02` | architecture + critique R8J | Integrated | state table C1/C2 define seis critérios tardios, allowlist por célula, valores/qualifier exatos e ativação externa condicional de Production-Ready; `ATTEST-NEG-05..08` fecham células estáticas |
| `OPS-R8J-01` | formal architecture review R8J | Integrated | bootstrap aceita somente candidate pre-C0/HEAD=C0 com seed exato; descendant pending falha, C1 exige C0; `CAP-POS-12..14`/`NEG-45` e revalidação limpa de C0 cobrem a sequência |
| `CRIT-R8J-03` | formal critique R8J | Integrated | current-action avança para integração R8J/freeze R8K; novo coherence pass obrigatório após publicação |
| `CRIT-R8J-04` | formal critique R8J | Integrated | `Gate: History Trust Evidence`, DOD-15/VAL-10 e rows C0/C1/C2 possuem remote OID, ancestry, availability e aceite humano explícito de RISK-HIST-01 |
| `CRIT-R8J-05` | formal critique R8J | Integrated | `capability-identity-ledger-v1` fixa fields, ordering, UTF-8/minified JSON e SHA-256; `CAP-POS-15`/`NEG-46` distinguem formatação de mutação semântica |
| `ARCH-R8K-01` / `CRIT-R8K-01` | architecture + critique R8K | Integrated | history trust separa precommit base check de post-commit/pre-push OID check; C0 facts entram em C1 e C1 facts ficam no handoff externo |
| `ARCH-R8K-02` | formal architecture review R8K | Integrated | removido completed intermediário/C2; C0 permanece ativo e C1 faz move final atômico com stage condicional, validado antes do commit e ativado externamente |
| `CRIT-R8K-02` | formal critique R8K | Integrated | current-action avança de baseline R8K já publicada para integração/freeze R8L, sem repetir ação concluída |
| `CRIT-R8K-03` | formal critique R8K | Integrated | wildcard `deterministic/tests/**` substituído pelos cinco arquivos de teste exatos autorizados |
| `CRIT-R8K-04` | formal critique R8K | Integrated | wall-clock ~179s vira tendência advisory; hard gates permanecem scan count `<=3`, history calls `<=k+2` e zero helper full-tree |
| `RISK-HIST-01-R8L` | formal architecture review R8L | Accepted residual | reviewer considerou arquitetura pronta; risco permanece explicitamente condicionado ao APROVADO e ao History Trust Gate |
| `CRIT-R8L-01` | formal critique R8L | Integrated | phase table fixa C0/candidate C1/handoff para DOD-12/15 e VAL-07/10; candidate exige todos checkboxes checked/rows passed e `CLOSEOUT-POS-02` invoca guards Delphi reais |
| `CRIT-R8L-02` | formal critique R8L | Integrated | pós-C1 exige `todo_count=1`, exact discovery TODO membership e ausência do stale transition path; `CLOSEOUT-POS-03`/`NEG-07` cobrem false-go |
| `CRIT-R8L-03` | formal critique R8L | Integrated | current-action avança de baseline R8L já publicada para integração/freeze R8M, sem repetir freeze concluído |
| `RISK-HIST-01-R8M` | formal architecture review R8M | Accepted residual | arquitetura novamente considerada pronta; aceite humano e History Trust permanecem obrigatórios |
| `CRIT-R8M-01` | formal critique R8M | Integrated | todos critérios/evidence concluem em C0 por fixtures; candidate C1 congela matriz, final guards geram somente handoff externo; `CLOSEOUT-NEG-08` proíbe self-referential evidence |
| `CRIT-R8M-02` | formal critique R8M | Integrated | failure após C1 publicado exige C1R reverso para active/Blocked com exact two-TODO scan antes de retry; success path continua sem C2 |
| `CRIT-R8M-03` | formal critique R8M | Integrated | current-action avança de baseline R8M já publicada para integração/freeze R8N |
| `CRIT-R8M-04` | formal critique R8M | Integrated | LEDGER_GENESIS possui heading/field/path/grammar/bootstrap/uniqueness únicos e `CAP-NEG-47..51` |
| `OPS-R8N-01` / `RECOVERY-R8N-01` | architecture + critique R8N | Integrated | C1R exige HEAD/origin iguais ao failed C1 e tree limpo em dois checks; remote divergence para sem commit/push e exige reconciliation + renewed APROVADO |
| `RECOVERY-R8N-02` | formal critique R8N | Integrated | C1→C1R possui tabela exata de fields, failure tuple schema, byte-freeze, reverse links e comandos/guards ordenados; `CLOSEOUT-NEG-11/12` fecham desvios |
| `PERF-R8N-01` | formal architecture review R8N | Integrated | claim limitado a uma consulta path-limited + até uma blob read por versão; Git pode percorrer histórico total; wall-clock segue advisory |
| `STATE-R8N-01` | formal critique R8N | Integrated | current-action avança de baseline R8N publicada para integração/freeze R8O |
| `DEP-R8N-01` / `PROBE-R8N-01` | formal critique + real pre-approval probe | Resolved | schemas CI/completion alinhados aos guards; completed conditional e active/Blocked recovery retornaram go em completion/authority/closeout reais com 34 evidence bindings |
| `ARCH-R8O-CLEAN` | formal architecture review R8O | Accepted / Ready with RISK-HIST-01 | Option A, separação Current/Target, identidade estável, transições e closeout atômico foram considerados prontos; nenhum achado arquitetural |
| `CRIT-R8O-01` | formal critique R8O | Integrated | C0/C1/C1R passam a stagear o candidate completo, rejeitar extra/unstaged, capturar tree OID, executar guards contra a árvore staged, revalidar antes do commit e provar commit-tree equality; `TREE-POS-01`/`TREE-NEG-01..04` fecham os desvios |
| `STATE-R8O-01` | formal critique R8O | Integrated | current-action avança da baseline R8O já publicada para integração/freeze R8P; `VAL-06` consome a correção Delphi resolvida em vez de aguardá-la |
| `ARCH-R8P-01` / `CRIT-R8P-01` | architecture + critique R8P | Integrated | `DELIVERY_SCOPE_SET` usa baseline `0fe906c`→candidate e `PHASE_COMMIT_DELTA_SET` usa BASE_HEAD→candidate; somente o segundo iguala índice, com `TREE-POS-02`/`CHANGESET-POS-06` |
| `CRIT-R8P-02` | formal critique R8P | Integrated | recovery reobserva tip remoto real por `ls-remote` antes do preparo, commit e push; local `origin/main` é check adicional; `CLOSEOUT-NEG-13` cobre remote avançado com tracking stale |
| `CRIT-R8P-03` | formal critique R8P | Integrated | consumers são tree-native/worktree-proxy/human-review; proxies têm pre/post OID checks e reviews usam attestation externa candidate-bound invalidada por mudança |
| `STATE-R8P-01` | formal review R8P | Integrated | current-action avança da baseline R8P já publicada para integração/freeze R8Q |
| `ARCH-R8Q-CLEAN` | formal architecture review R8Q | Accepted / Ready with RISK-HIST-01 | dual-set, consumer binding e remote-tip recovery foram considerados corretos, elegantes e estruturalmente prontos; nenhum achado arquitetural |
| `CRIT-R8Q-01` | formal critique R8Q | Integrated | ativação pós-push exige fresh `actual_remote_main_oid==C1`, `scanned_head_oid==C1` e tuple externo vinculado; `REMOTE-POS-01`/`REMOTE-NEG-03` fecham false activation |
| `CRIT-R8Q-02` | formal critique R8Q | Integrated | fresh remote pre-push obrigatório em C0/C1; avanço após commit entra em `local-unpublished-diverged`, proíbe push/force-push/C1R e exige reconciliação/rebaseline + novo `APROVADO`; `REMOTE-NEG-01/02` |
| `STATE-R8Q-01` | formal review R8Q | Integrated | current-action avança da baseline R8Q já publicada para integração/freeze R8R |
| `ARCH-R8R-01` | formal architecture review R8R | Integrated | cada versão do identity ledger deve ser superconjunto semântico imutável da anterior; `CAP-NEG-52/53` rejeitam remove→readd e mutate→revert mantendo uma leitura por versão |
| `CRIT-R8R-01` | formal critique R8R | Integrated | C0/C1/C1R usam exact expected-value lease com fast-forward/parent proof; `REMOTE-NEG-04` cobre ref change compatível que ordinary push aceitaria |
| `CRIT-R8R-02` | formal critique R8R | Integrated | reviews de implementation content ligam-se a C0 e passam a C1 somente via proof bridge; `REVIEW-C1-01`/`REVIEW-C1R-01` focados ligam-se aos candidates finais |
| `CRIT-R8R-03` | formal critique R8R | Integrated | `uninotas-closeout-handoff-v1` preserva trees, exact sets, bridge, typed consumer bindings, CAS/remote observations e scan; `HANDOFF-POS-01`/`NEG-01..03` |
| `STATE-R8R-01` | formal review R8R | Integrated | current-action avança da baseline R8R já publicada para integração/freeze R8S |
| `ARCH-R8S-CLEAN` | formal architecture review R8S | Accepted / Ready with RISK-HIST-01 | Option A, ledger monotônico, CAS, proof bridge e handoff foram considerados prontos para aprovação explícita; nenhum achado arquitetural |
| `CRIT-R8S-01` | formal critique R8S | Integrated | `deterministic/closeout_handoff.py` vira único entry point real para promote/activate, strict unknown-field rejection, fresh observations, Delphi scan e outputs ignorados |
| `CRIT-R8S-02` | formal critique R8S | Integrated | schema phase-aware preserva C0 fresh-pre/lease/post-push/local/parent/fast-forward evidence além de C1 |
| `CRIT-R8S-03` | formal critique R8S | Integrated | C1R possui recovery handoff strict com reverse bridge, CAS, duas observações remotas, scan bound C1R/exact two-TODO e recovery-effective only |
| `CRIT-R8S-04` | formal critique R8S | Integrated | Required Consumer Binding Matrix congela IDs únicos/exatos, phase/class/scope/path source/outcome; casos rejeitam ausência/duplicata/extra/misclassification |
| `STATE-R8S-01` | formal review R8S | Integrated | current-action avança da baseline R8S já publicada para integração/freeze R8T |

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** o validator pode ser evoluído por manifesto único ou por inventário gerado; revisão independente deve desafiar a opção recomendada.
- **Opinion count:** `24`
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
| `uninotas_architecture_opinion_r8b` | manifesto/registry/transições mantidos; fechar bijeção planned↔terminal | acceptable | strong positive | mixed até integrar a bijeção | Integrated / Rerun required | merge R8B válido; achados integrados e baseline R8C obrigatória |
| `uninotas_architecture_opinion_r8c` | manter arquitetura; explicitar ownership baseline sem transição sintética | strong positive | strong positive | mixed até fechar cardinalidades | Integrated / Rerun required | merge R8C válido; achados integrados e baseline R8D obrigatória |
| `uninotas_architecture_opinion_r8d` | adotar manifesto único + registry derivado + transições persistentes | strong positive | strong positive | strong positive | Accepted / Clean | merge R8D válido; zero achados arquiteturais, crítica paralela exigiu refinamentos operacionais |
| `uninotas_architecture_opinion_r8e` | manter arquitetura e adicionar baseline capability catalog | strong positive | strong positive | mixed até persistir identidade baseline | Integrated / Rerun required | merge R8E válido; IDs baseline e lane/path-set integrados, baseline R8F obrigatória |
| `uninotas_architecture_opinion_r8f` | manter arquitetura e adicionar oracle independente digest+Git history | strong positive | strong positive | mixed até fechar coordinated erasure | Integrated / Rerun required | merge R8F válido; oracle/path/attestation/privacy integrados, baseline R8G obrigatória |
| `uninotas_architecture_opinion_r8g` | manter arquitetura; separar delivery/lifecycle path evidence e explicitar history trust | strong positive | strong positive | mixed até fechar closeout/trust boundary | Integrated / Rerun required | merge R8G válido; baselines/guards/ancestry integrados, baseline R8H obrigatória |
| `uninotas_architecture_opinion_r8h` | manter a arquitetura, mas estreitar a garantia histórica ao seed congelado + linhagem first-parent observável | strong positive | strong positive | mixed até explicitar o limite de rewrite alternativo | Integrated / Rerun required | merge R8H válido; RISK-HIST-01, C0 frozen, interface real dos guards e bijeção ledger/transição integrados; baseline R8I obrigatória |
| `uninotas_architecture_opinion_r8i` | manter manifesto/registry/ledger/C0-C2, corrigindo a âncora genesis e o procedimento operacional | strong positive | strong positive | strong positive; operational fit mixed até correção | Integrated / Rerun required | merges R8I válidos; genesis/baseline/history budget/traceability/comandos closeout integrados, baseline R8J obrigatória |
| `uninotas_architecture_opinion_r8j` | manter Option A e definir state machine executável para bootstrap C0 e attestation C2 | strong positive | strong positive | mixed até fechar lifecycle boundaries | Integrated / Rerun required | merges R8J válidos; bootstrap/state table/cell allowlist/conditional stage/history gate/digest integrados, baseline R8K obrigatória |
| `uninotas_architecture_opinion_r8k` | manter Option A, mas substituir C0/C1/C2 por C0 ativo + C1 final atômico + handoff externo | strong positive | mixed | mixed até remover estados impossíveis | Integrated / Rerun required | merges R8K válidos; closeout atômico, history ordering, exact test paths e performance determinística integrados, baseline R8L obrigatória |
| `uninotas_architecture_opinion_r8l` | adotar Option A; arquitetura pronta com aceite explícito do risco residual | strong positive | strong positive | strong positive | Accepted / Ready with RISK-HIST-01 | merge R8L válido; crítica paralela exigiu apenas estados tardios/scan semântico, baseline R8M obrigatória |
| `uninotas_architecture_opinion_r8m` | adotar Option A e preservar closeout atômico/scan semântico | strong positive | strong positive | strong positive | Accepted / Ready with RISK-HIST-01 | merge R8M válido; crítica paralela exigiu evidence não autorreferente, recovery e binding genesis, baseline R8N obrigatória |
| `uninotas_architecture_opinion_r8n` | manter Option A; dividir recovery por remote-tip equality e estreitar claim de custo | acceptable | strong positive | strong positive | Integrated / Rerun required | merges R8N válidos; recovery/state tables/probes/matrix schemas/performance claim integrados, baseline R8O obrigatória |
| `uninotas_architecture_opinion_r8o` | adotar Option A; arquitetura pronta para aprovação explícita condicionada a RISK-HIST-01 e aos guards | strong positive | strong positive | strong positive | Accepted / Clean | merge R8O válido; zero achados arquiteturais, crítica paralela exigiu candidate-tree binding e baseline R8P |
| `uninotas_architecture_opinion_r8p` | manter Option A, separando cumulative delivery scope do commit delta de C0 | strong positive | mixed | mixed até corrigir binding | Integrated / Rerun required | merges R8P válidos; dual-set, remote-tip e consumer binding integrados, baseline R8Q obrigatória |
| `uninotas_architecture_opinion_r8q` | adotar Option A com dual-set, binding por consumer e recovery baseado no remote tip real | strong positive | strong positive | strong positive | Accepted / Clean | merge R8Q válido; zero achados arquiteturais, crítica paralela exigiu remote activation/pre-push race contract e baseline R8R |
| `uninotas_architecture_opinion_r8r` | adotar Option A após fechar monotonicidade do identity ledger | strong positive | strong positive | mixed até enforcement monotônico | Integrated / Rerun required | merges R8R válidos; monotonic ledger, atomic CAS, phased reviews e typed handoff integrados, baseline R8S obrigatória |
| `uninotas_architecture_opinion_r8s` | adotar Option A; arquitetura pronta com ledger monotônico, CAS, proof bridge e handoff tipado | strong positive | strong positive | strong positive | Accepted / Clean | merge R8S válido; crítica paralela exigiu operational handoff entry point/phase schemas/closed consumer IDs e baseline R8T |

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
- **Critique status:** `running`
- **Findings summary:** `R8S apontou ausência de gate executável do handoff real, C0 CAS incompleto no schema, C1R sem activation tuple equivalente e consumer set aberto; entry point, schemas por fase/recovery e catálogo fechado foram integrados e exigem crítica R8T`.
- **Evidence / reference:** merges derivados `uninotas-r8s-architecture-merge.json` e `uninotas-r8s-critique-merge.json`; `closeout_handoff.py`, Required Consumer Binding Matrix e `HANDOFF-POS-02`/`NEG-04..07`; nova crítica obrigatória após freeze R8T.
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
- **Approval scope:** `pending — must explicitly include TD-01..TD-07, D-T01..D-T05, DOD-01..DOD-15/VAL-01..VAL-10 and acceptance of RISK-HIST-01`
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
- **Current governed action:** `formal-review`
- **Selected role:** `formal-reviewer`
- **Selected model:** `gpt-5.6-sol`
- **Selected effort:** `xhigh`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `fresh no-context architecture_opinion and critique reviewers required by the applicable routing workflow; read-only and no parallel code writers`
- **Execution topology:** `n/a — read-only formal review`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `n/a — reviewers do not mutate source`
- **Guard outcome:** `go`
- **Waiver / exception reference:** `n/a`
- **Post-approval implementation routing:** `provisional routine-executor/gpt-5.6-terra/medium on primary-checkout-single-writer; must rerun agent_role_routing_guard.py after explicit APROVADO and before implementation`.

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
| `D-T05` | pending | pending implementation | hard: três scans full-tree no máximo e history `git_calls<=k+2`; wall-clock incluindo ~179s é advisory |

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

## Post-Push Attestation (Atomic Final Closeout)

- **C0 active implementation/genesis commit:** `pending delivery — persisted in C1 after observation`
- **C0 remote verification:** `pending delivery — persisted in C1 after observation`
- **C1 atomic completed-tree commit:** `external handoff after local commit/push; never persisted into itself`
- **C1 parent/ancestry verification:** `external handoff must prove parent(C1)=C0 and C0 ancestor of C1`
- **C1 remote verification:** `external handoff must prove HEAD==origin/main==C1, post_push_remote_main_oid=C1 before scan and fresh actual_remote_main_oid=C1 immediately before activation tuple`
- **Post-C1 active scan:** `external handoff bound to scanned_head_oid=C1; must report go, todo_count=1, exact active_paths=[todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md], and stale_transition_path=false`
- **Production-Ready evidence:** `pending external uninotas-closeout-handoff-v1 artifact containing C0/C1 candidate+commit tree equality, exact path sets, proof_bridge, typed consumer_bindings, expected-value lease result, post-push/activation remote OIDs, scanned_head_oid=C1, exact semantic scan and production_ready_effective:true`
- **Failed-C1 recovery:** `if C1 was pushed and any external predicate fails, closeout_handoff promote/activate c1r must emit strict recovery handoff with C1R tree/CAS/two remote observations/scanned_head_oid/exact two-TODO set, recovery_effective:true and production_ready_effective:false; retain failure tuple externally`
- **Unpublished C0/C1 divergence:** `if exact expected-value lease rejects or fresh remote tip differs after local commit, retain external local-unpublished-diverged tuple, do not retry/unconditionally force-push or use C1R, and require authority reconciliation/rebaseline plus renewed APROVADO`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planejamento e aprovação ainda não concluídos.
- **Post-commit/push status:** `pending`
- **Next path/status action:** publicar as correções R8S como baseline R8T, executar as revisões/guards pré-aprovação e solicitar `APROVADO` explícito com aceite de `RISK-HIST-01`.

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
- Pre-implementation bootstrap path set: `bash -lc '{ git -C uninotas-foundation diff --no-renames --name-only 0fe906c1e496a1d38f1603cf188c224711011c32 --; git -C uninotas-foundation ls-files --others --exclude-standard; } | LC_ALL=C sort -u'`
- Post-implementation delivery path set: `python3 uninotas-foundation/deterministic/enumerate_change_paths.py --mode delivery --repo uninotas-foundation --baseline 0fe906c1e496a1d38f1603cf188c224711011c32 --candidate-tree <CANDIDATE_TREE_OID>`
- Closeout lifecycle path set: `python3 uninotas-foundation/deterministic/enumerate_change_paths.py --mode lifecycle --repo uninotas-foundation --baseline <C0_PRE_MOVE> --candidate-tree <CANDIDATE_TREE_OID>`
- Status/rename evidence view: `bash -lc '{ git -C uninotas-foundation diff --name-status --find-renames 0fe906c1e496a1d38f1603cf188c224711011c32 --; git -C uninotas-foundation ls-files --others --exclude-standard | sed "s#^#A\\t#"; } | LC_ALL=C sort -u -k2,2 -k1,1'`
- Pre-implementation profile scope: `bash -lc 'mapfile -t paths < <({ git -C uninotas-foundation diff --no-renames --name-only 0fe906c1e496a1d38f1603cf188c224711011c32 --; git -C uninotas-foundation ls-files --others --exclude-standard; } | LC_ALL=C sort -u | sed "s#^#foundation_documentation/#"); ((${#paths[@]} > 0)) && python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto "${paths[@]}"'`
- Post-implementation profile scope: `bash -lc 'mapfile -t paths < <(python3 uninotas-foundation/deterministic/enumerate_change_paths.py --mode delivery --repo uninotas-foundation --baseline 0fe906c1e496a1d38f1603cf188c224711011c32 --candidate-tree <CANDIDATE_TREE_OID> | sed "s#^#foundation_documentation/#"); ((${#paths[@]} > 0)) && python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto "${paths[@]}"'`
- After `APROVADO`, before implementation: `python3 delphi-ai/tools/todo_authority_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- Pure semantic lane: `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_registry_semantics.py uninotas-foundation/deterministic/tests/test_privacy_predicate.py`
- Change-set helper lane: `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_enumerate_change_paths.py`
- Closeout/handoff lane: `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_closeout_diff.py uninotas-foundation/deterministic/tests/test_closeout_handoff.py`
- `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py`
- `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation`
- `'/mnt/c/Program Files/Git/bin/bash.exe' -lc 'cd /c/Unifast/MonitorDeNotas && bash delphi-ai/verify_context.sh'`
- `python3 delphi-ai/tools/todo_diff_expectation_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --repo-root uninotas-foundation`
- `git -C uninotas-foundation diff --check 0fe906c1e496a1d38f1603cf188c224711011c32 --`
- `git -C uninotas-foundation diff --name-status --find-renames 0fe906c1e496a1d38f1603cf188c224711011c32 --`
- Audit package start: `python3 delphi-ai/skills/audit-protocol-triple-review/scripts/triple_audit_session.py start --package uninotas-foundation/artifacts/analysis/uninotas-canonical-foundation-transition-delivery-package.md --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --extra-lane cutover-integrity --run-root uninotas-foundation/artifacts/tmp/uninotas-canonical-foundation-transition-audit`
- Final delivery authority/completion: run on the same uncommitted candidate C1 tree against the completed path, after atomic-closeout diff validation.
- C1 atomic closeout boundary: `python3 uninotas-foundation/deterministic/validate_closeout_diff.py --repo uninotas-foundation --base <C0> --candidate-tree <CANDIDATE_TREE_OID> --todo todos/completed/process/TODO-uninotas-canonical-foundation-transition.md`
- Failed-C1 recovery boundary: `python3 uninotas-foundation/deterministic/validate_closeout_diff.py --mode recovery --repo uninotas-foundation --base <FAILED_C1> --candidate-tree <CANDIDATE_TREE_OID> --todo todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- Failed-C1 recovery tip precondition: `REMOTE_MAIN_OID=$(git -C uninotas-foundation ls-remote --exit-code origin refs/heads/main | awk 'NR==1 {print $1}'); test "$REMOTE_MAIN_OID" = "<FAILED_C1>" && test "$(git -C uninotas-foundation rev-parse origin/main)" = "<FAILED_C1>" && test "$(git -C uninotas-foundation rev-parse HEAD)" = "<FAILED_C1>" && test -z "$(git -C uninotas-foundation status --porcelain)"` (repeat fresh `ls-remote==FAILED_C1` immediately before commit and push; local `origin/main` is additional only; mismatch stops for reconciliation).
- C1 completed-path structure: `python3 delphi-ai/tools/todo_deterministic_validator.py --todo uninotas-foundation/todos/completed/process/TODO-uninotas-canonical-foundation-transition.md`
- C1 completed-path diff gate: `python3 delphi-ai/tools/todo_diff_expectation_guard.py uninotas-foundation/todos/completed/process/TODO-uninotas-canonical-foundation-transition.md --repo-root uninotas-foundation`
- C1 delivery authority: `python3 delphi-ai/tools/todo_authority_guard.py uninotas-foundation/todos/completed/process/TODO-uninotas-canonical-foundation-transition.md --require-delivery-gates`
- C1 completion: `python3 delphi-ai/tools/todo_completion_guard.py uninotas-foundation/todos/completed/process/TODO-uninotas-canonical-foundation-transition.md --require-delivery`
- C1 closeout: `python3 delphi-ai/tools/todo_closeout_guard.py uninotas-foundation/todos/completed/process/TODO-uninotas-canonical-foundation-transition.md --repo uninotas-foundation`
- Pre-move closeout after `DEP-CLOSEOUT-01`: `python3 delphi-ai/tools/todo_closeout_guard.py uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md --repo uninotas-foundation` (must report `path_state=active`, not only `go`).
- Git commit authority: `python3 delphi-ai/tools/git_write_authority_guard.py --repo uninotas-foundation --action git-commit --authority-surface foundation_documentation`
- Git push authority: `python3 delphi-ai/tools/git_write_authority_guard.py --repo uninotas-foundation --action git-push --authority-surface foundation_documentation`
- C0 CAS promotion/evidence: `python3 uninotas-foundation/deterministic/closeout_handoff.py promote --phase c0 --repo uninotas-foundation --expected-remote <BASE_REMOTE_OID> --new-commit <C0> --candidate-tree <C0_TREE> --consumer-bindings <IGNORED_C0_BINDINGS_JSON> --output uninotas-foundation/artifacts/tmp/uninotas-c0-promotion.json`
- C1 CAS promotion/evidence: `python3 uninotas-foundation/deterministic/closeout_handoff.py promote --phase c1 --repo uninotas-foundation --expected-remote <C0> --new-commit <C1> --candidate-tree <C1_TREE> --consumer-bindings <IGNORED_C1_BINDINGS_JSON> --base-evidence uninotas-foundation/artifacts/tmp/uninotas-c0-promotion.json --proof-bridge <IGNORED_C1_BRIDGE_JSON> --output uninotas-foundation/artifacts/tmp/uninotas-c1-promotion.json`
- C1 production activation: `python3 uninotas-foundation/deterministic/closeout_handoff.py activate --phase c1 --repo uninotas-foundation --c0-evidence uninotas-foundation/artifacts/tmp/uninotas-c0-promotion.json --c1-evidence uninotas-foundation/artifacts/tmp/uninotas-c1-promotion.json --delphi-root delphi-ai --output uninotas-foundation/artifacts/tmp/uninotas-closeout-handoff-v1.json`
- C1R CAS promotion/evidence: `python3 uninotas-foundation/deterministic/closeout_handoff.py promote --phase c1r --repo uninotas-foundation --expected-remote <FAILED_C1> --new-commit <C1R> --candidate-tree <C1R_TREE> --consumer-bindings <IGNORED_C1R_BINDINGS_JSON> --base-evidence <IGNORED_FAILED_C1_EVIDENCE_JSON> --proof-bridge <IGNORED_C1R_BRIDGE_JSON> --output uninotas-foundation/artifacts/tmp/uninotas-c1r-promotion.json`
- C1R recovery activation: `python3 uninotas-foundation/deterministic/closeout_handoff.py activate --phase c1r --repo uninotas-foundation --c0-evidence uninotas-foundation/artifacts/tmp/uninotas-c0-promotion.json --failed-c1-evidence <IGNORED_FAILED_C1_EVIDENCE_JSON> --c1r-evidence uninotas-foundation/artifacts/tmp/uninotas-c1r-promotion.json --failure-tuple <IGNORED_FAILURE_TUPLE_JSON> --delphi-root delphi-ai --output uninotas-foundation/artifacts/tmp/uninotas-recovery-handoff-v1.json`
- Post-commit/push active scan: `python3 delphi-ai/tools/todo_closeout_guard.py --all-active --repo uninotas-foundation` (must report the real nonzero active TODO count, not only `go`).
- History trust remote observation: `git -C uninotas-foundation ls-remote --exit-code origin refs/heads/main`
- History trust precommit base: `git -C uninotas-foundation merge-base --is-ancestor <REMOTE_MAIN_OID> <BASE_HEAD_OID>` (exit 0 obrigatório; congelar `BASE_HEAD_OID`).
- History trust atomic CAS push: prove exact parent/tree and `merge-base --is-ancestor <EXPECTED_REMOTE_OID> <NEW_COMMIT_OID>`, reobserve remote, then execute only `git push --force-with-lease=refs/heads/main:<EXPECTED_REMOTE_OID> origin <NEW_COMMIT_OID>:refs/heads/main`; lease rejection enters `local-unpublished-diverged`, prohibits retry/unconditional force/C1R and requires reconciliation/rebaseline plus renewed `APROVADO`.
- C1 post-push activation observation: capture fresh `POST_PUSH_REMOTE_MAIN_OID` and require it plus `HEAD==origin/main==C1`; record `scanned_head_oid=C1`, run semantic active scan, then capture fresh `ACTUAL_REMOTE_MAIN_OID` immediately before activation and require both remote observations equal C1; include all three OIDs in the external success tuple.
- Candidate cumulative delivery scope: `python3 uninotas-foundation/deterministic/enumerate_change_paths.py --mode delivery --repo uninotas-foundation --baseline 0fe906c1e496a1d38f1603cf188c224711011c32 --candidate-tree <CANDIDATE_TREE_OID>` must satisfy Expected Changed Paths independently of the staged delta.
- Candidate phase delta: `git -C uninotas-foundation diff --name-only --no-renames <BASE_HEAD> <CANDIDATE_TREE_OID> | LC_ALL=C sort -u` must equal `git -C uninotas-foundation diff --cached --name-only --no-renames | LC_ALL=C sort -u`; every C0 delta path must be authorized, while C1/C1R must equal their exact five-path allowlist.
- Candidate index/worktree equality: `git -C uninotas-foundation diff --quiet -- && test -z "$(git -C uninotas-foundation ls-files --others --exclude-standard)"` after staging the complete phase allowlist.
- Candidate tree capture/recheck: `git -C uninotas-foundation write-tree` (record as `<CANDIDATE_TREE_OID>`), then rerun immediately before commit and require the same OID.
- Worktree-proxy binding wrapper: before and after each non-tree-native command, require candidate index/worktree equality and `test "$(git -C uninotas-foundation write-tree)" = "<CANDIDATE_TREE_OID>"`; any mismatch invalidates the command output and all later attestations.
- Human-review binding: record ignored/external attestation `{candidate_tree_oid, exact_path_set, reviewer_or_session, outcome}` after capture; candidate OID change requires rerun and no self-dependent OID is persisted in the candidate.
- Commit tree binding: `test "$(git -C uninotas-foundation rev-parse HEAD^{tree})" = "<CANDIDATE_TREE_OID>"` immediately after commit and before push.

### Final-tree closeout (Required Order)

1. Com implementação pronta e o TODO ainda ativo, observar remote OID, exigir `BASE_HEAD==BASE_REMOTE_OID`, congelar ambos, exigir índice vazio, stagear somente o delta C0 completo e capturar o candidate tree OID. Provar separadamente cumulative delivery scope versus `0fe906c` e phase delta versus BASE_HEAD; executar History Trust, guards, `REVIEW-PRIV-01` e todos os audits/reviews de implementação sobre esse C0 OID conforme o binding faseado.
2. Imediatamente antes do commit, repetir remote/base, cumulative/delta allowlists, index/worktree equality, tree OID e validade das attestations. Criar C0 local e exigir `tree(C0)=captured tree`, `parent(C0)=BASE_HEAD==BASE_REMOTE_OID`; após Git push authority guard, executar exclusivamente `closeout_handoff.py promote --phase c0`, que faz fast-forward/CAS, observa pós-push e emite o C0 phase evidence consumido por C1. Lease rejection entra em local-unpublished-diverged e proíbe retry/C1R.
3. Em checkout limpo de C0, repetir Foundation validator sob a exceção bootstrap fechada, executar closeout guard no path ativo e confirmar `path_state=active`. C0 vira `LEDGER_GENESIS` e baseline de `mode=lifecycle`.
4. Observar via `ls-remote` que remote tip, `origin/main` e HEAD são C0, congelar base HEAD=C0 e preparar o move active→completed, manifesto/backlinks finais, C0 OID/verificação e stage condicional; stagear exatamente os cinco paths, exigir index/worktree equality e capturar C1 candidate tree OID. Nenhum fato do futuro C1 é persistido.
5. Executar, contra o mesmo staged tree OID, `C1 atomic closeout boundary` como proof bridge C0→C1, `C1 completed-path structure`, Foundation validator, `C1 completed-path diff gate`, `mode=delivery`, `mode=lifecycle`, status views, profile scope, diff check, `C1 delivery authority`, `C1 completion` e `C1 closeout`; executar `REVIEW-C1-01` focado e vinculado ao candidate, carregar somente attestations C0 de implementation content via bridge e revalidar allowlist/equality/tree OID/fresh remote=C0 imediatamente antes do commit.
6. Criar C1 local e exigir `tree(C1)=captured tree` e `parent(C1)=C0`; após Git push authority guard, executar exclusivamente `closeout_handoff.py promote --phase c1` com C0 phase evidence, proof bridge e exact C1 bindings. Lease rejection entra em local-unpublished-diverged e proíbe retry/C1R.
7. Executar `closeout_handoff.py activate --phase c1`, que revalida strict schemas/bindings, observa post-push remote, liga/executa o Delphi scan a C1, reobserva remote e emite `uninotas-closeout-handoff-v1`. Lista não tipada ou mismatch proíbe `production_ready_effective:true`. Não existe C2 nem persistência do próprio SHA.
8. Se C1 falhar externamente, reportar o tuple. Somente com fresh remote/local/HEAD FAILED_C1 e tree limpo, preparar C1R, stagear cinco reverse paths, capturar tree, executar recovery bridge + exact C1R consumers e `REVIEW-C1R-01`. Após Git push authority guard, usar exclusivamente `closeout_handoff.py promote --phase c1r`; depois executar `activate --phase c1r`, que exige duas observações C1R e scan ligado a C1R com exact two-TODO set antes de `recovery_effective:true`. Qualquer lease/remote/tree/scan mismatch exige reconciliação + `APROVADO` renovado.

## Files Expected (Compatibility Note)

- O `Diff Expectation Contract` é a autoridade exclusiva sobre paths esperados.
