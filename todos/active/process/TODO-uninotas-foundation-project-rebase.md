# TODO — Monitor de Notas: adequar `uninotas-foundation` ao projeto

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Lifecycle state:** `Review — material PACED findings being integrated`
- **Created:** `2026-09-24`
- **Owner:** `Delphi / Strategic CTO-Tech-Lead`, sob autoridade humana do usuário

## Approval

- **Approved by:** `usuário — 2026-09-24 — “APROVADO”`
- **Approval scope:** intenção para `S-01..S-09` conforme `D-01..D-03`, com mudanças persistentes limitadas à Foundation; aliases PACED locais já materializados são dependência read-only e não superfície de escrita deste TODO.
- **Current authority of that approval:** `planning intent only`; a aprovação antecedeu os reviews obrigatórios e não autoriza execução até o pacote convergir, obter `preflight-go` e receber novo `APROVADO`.
- **Execution not authorized:** código/runtime do Monitor de Notas, banco, deploy, segredos e núcleo compartilhado do `delphi-ai`; worktrees e checkouts auxiliares também não foram autorizados.
- **Renewed approval required when:** após a convergência destes reviews e sempre que houver mudança de escopo, identidade canônica, tratamento do legado, arquitetura-alvo, validações obrigatórias ou repositórios envolvidos.

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

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Blocked`
- **Next exact step:** integrar os achados `RF-01..RF-08`, publicar um baseline imutável novo e repetir arquitetura/crítica contra o snapshot exato antes dos guards de coerência, drift e preflight.

## Active Work State

- **Work state:** `blocked`
- **Why this state now:** arquitetura e crítica independentes convergiram em `no-go` de execução com achados materiais de planejamento.
- **Exit condition:** `RF-01..RF-08` estão integrados, o review do baseline renovado não possui achado material aberto e os guards de coerência, drift e preflight retornam `go|preflight-go` conforme seu contrato.

## Blocker Notes

- **Blocker:** o pacote ainda não satisfaz o piso de planejamento PACED; não existe autoridade de execução.
- **Why blocked now:** inventário definidor de arquitetura, baseline de evidência, manifesto destrutivo e critérios determinísticos estavam incompletos; além disso, o review não estava ligado aos bytes imutáveis do baseline registrado.
- **What unblocks it:** integrar o ledger de achados, publicar/refazer o freeze com commit + blob/hash, repetir os reviews e obter novo `APROVADO` após todos os guards pré-aprovação.
- **Owner / source:** owner do TODO, com decisão humana no novo gate de aprovação.
- **Last confirmed truth:** reviewers internos `architecture_opinion` e `critique` retornaram `no-go` em 2026-09-24; direção de hard cutover foi mantida, mas execução foi recusada.

## Scope

- [ ] `S-01` Inventariar a verdade atual do Monitor de Notas no código, banco documentado, infraestrutura, testes e READMEs, distinguindo comportamento comprovado de intenção futura.
- [ ] `S-02` Definir e aplicar a identidade canônica do produto e da Foundation em títulos, links, namespaces e linguagem de domínio.
- [ ] `S-03` Reescrever mandato, constituição, entidades, baseline tecnológico, lifecycle e roadmap para refletirem exclusivamente o projeto atual.
- [ ] `S-04` Substituir os módulos herdados por módulos do Monitor de Notas, incluindo pelo menos ingestão/leitura de eventos, classificação, tratamentos, identidade/equipe, tempo real/monitoramento e operação/deploy.
- [ ] `S-05` Reconciliar backlog, decisões, contratos e políticas com os owners canônicos novos, sem transportar decisões do LeadsHug como se fossem decisões do Monitor de Notas.
- [ ] `S-06` Remover do tree atual TODOs, artefatos e documentos herdados do LeadsHug que não pertençam ao Monitor de Notas; o histórico Git será a única retenção do legado removido.
- [ ] `S-07` Atualizar a governança para declarar o `delphi-ai` como distribuição local obrigatória do método PACED: todo trabalho do projeto passa por seus workflows e guards, com `APROVADO` e authority guard `go` antes de implementação.
- [ ] `S-08` Criar ou adaptar validações determinísticas proporcionais para referências, identidade, links, schemas documentais e ausência de autoridade ativa do LeadsHug.
- [ ] `S-09` Validar o pacote final contra o repositório real, registrar evidência 1:1 e concluir o cutover documental sem alterar código, banco ou runtime.

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
- [x] `D-04` A tabela externa `logs` pertence ao Routerfy e é somente leitura para o Monitor de Notas; a aplicação escreve apenas em suas próprias tabelas de usuários e tratamentos. Decisão consolidada da evidência já incluída no contrato aprovado (`README.md`, `backend/README.md`, Prisma e SQL isolado).

## Decision Baseline — Frozen Before Implementation

- [x] `D-01` Identidade canônica aprovada: produto `Monitor de Notas`, repositório `MonitorDeNotas` e Foundation `uninotas-foundation`.
- [x] `D-02` Política de legado aprovada: remoção do tree atual e retenção somente pelo histórico Git.
- [x] `D-03` Fronteira aprovada: Foundation como autoridade do produto e `delphi-ai`/PACED como autoridade obrigatória do processo de engenharia.
- [x] `D-04` Ownership de dados congelado: `logs` read-only; `monitor_usuarios` e `monitor_tratamentos` pertencem à aplicação.

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** correções de links, índices, nomes, anchors, schemas documentais e pequenos ajustes de estrutura necessários ao mesmo cutover.
- **Must update or split the TODO:** mudança de código/runtime, nova capacidade de produto, modificação genérica do Delphi, migração de banco, alteração de API ou nova conversa material de risco/aprovação.

## Definition of Done

- [ ] `DOD-01` Nenhum documento canônico ativo apresenta o LeadsHug ou seu domínio como autoridade, produto ou arquitetura atual.
- [ ] `DOD-02` README, mandato, constituição, entidades, lifecycle, baseline tecnológico e roadmap descrevem de forma coerente o Monitor de Notas comprovado.
- [ ] `DOD-03` Os módulos possuem ownership, invariantes, capacidades e contratos correspondentes aos limites reais do sistema.
- [ ] `DOD-04` Backlog, decisões, contratos, políticas e TODOs ativos estão reconciliados com a nova identidade e não mantêm estado vivo conflitante.
- [ ] `DOD-05` Todo conteúdo herdado do LeadsHug sem função no Monitor de Notas foi removido do tree atual e permanece acessível apenas pelo histórico Git.
- [ ] `DOD-06` A divisão de autoridade entre `uninotas-foundation`, `delphi-ai` e o repositório do produto está documentada sem links quebrados.
- [ ] `DOD-07` Validações determinísticas e inspeções de referências passam no tree final e possuem evidência específica.
- [ ] `DOD-08` O diff fica restrito aos paths aprovados da Foundation; código, configuração, segredos e runtime permanecem inalterados.
- [ ] `DOD-09` Decisões estáveis e evidências finais foram consolidadas nos owners canônicos antes do TODO ser movido para `completed/`.
- [ ] `DOD-10` Nenhum documento, artifact ou fixture persiste PII real, payload bruto de produção, JWT, credencial ou exemplo operacional não redigido.
- [ ] `DOD-11` O contrato de setup documenta e valida como uma checkout limpa materializa `foundation_documentation -> uninotas-foundation` sem versionar o symlink no produto.

## Validation Steps

- [ ] `VAL-01` Verificar links internos e anchors em todos os documentos canônicos alterados.
- [ ] `VAL-02` Executar busca fail-closed por `LeadsHug|leadshug|WhatsApp|Typebot|Evolution|Baileys|Belluga|Bóora` e classificar cada ocorrência restante como histórica permitida ou falha.
- [ ] `VAL-03` Comparar stack, rotas, módulos, entidades e invariantes documentados com `backend/`, `frontend/`, `Dockerfile`, `docker-compose.yml`, `railway.json` e READMEs do produto.
- [ ] `VAL-04` Executar os guards aplicáveis do `delphi-ai` para escopo, autoridade, expectativa de diff, conclusão e closeout.
- [ ] `VAL-05` Executar `git diff --check` e confirmar ausência de segredos, artefatos gerados ou mudanças fora do contrato.
- [ ] `VAL-06` Revisar a matriz de evidências critério a critério; resumo agregado não substitui evidência 1:1.
- [ ] `VAL-07` Confirmar que o repositório do produto e o `delphi-ai` não receberam mudanças durante a execução.
- [ ] `VAL-08` Executar scan automatizado de segredo/JWT/PII de alto risco e revisão manual de privacidade nos documentos, artifacts e fixtures novos.
- [ ] `VAL-09` Em checkout/workspace limpo, criar ou verificar o alias pelo comando canônico e executar `bash delphi-ai/bootloaders/verify_context.sh` com sucesso.

## Completion Evidence Matrix

Cada critério possui evidência planejada 1:1; nenhum resumo agregado substitui estas linhas antes de qualquer alegação `Local-Implemented` ou movimento para `completed/`.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01` | `Definition of Done` | nenhuma autoridade LeadsHug ativa | `test+review` | `python3 deterministic/validate_foundation.py --root .` + manifesto de exceções históricas | `local` | `planned` | superfície ativa e história possuem regras distintas |
| `DOD-02` | `Definition of Done` | owners raiz descrevem o produto atual | `doc+traceability` | `artifacts/analysis/monitor-de-notas-product-truth-20260924.md` | `local` | `planned` | cada afirmação material aponta a código/configuração |
| `DOD-03` | `Definition of Done` | módulos correspondem aos limites reais | `doc+review` | `Canonical Target Module Map` + architecture adherence review | `local` | `planned` | seis owners coesos e fechados antes da execução |
| `DOD-04` | `Definition of Done` | owners auxiliares reconciliados | `manifest+review` | `Tracked Foundation File Disposition Manifest` | `local` | `planned` | uma disposição por arquivo de entrada |
| `DOD-05` | `Definition of Done` | legado removido do tree | `git+test` | `git ls-files` + validator de paths/autoridade | `local` | `planned` | histórico Git é a única retenção não explicitamente permitida |
| `DOD-06` | `Definition of Done` | fronteiras Foundation/PACED/produto sem links quebrados | `test` | validator de links + setup contract | `local` | `planned` | não duplica regras PACED |
| `DOD-07` | `Definition of Done` | checks determinísticos passam | `test` | `python3 -m unittest discover -s deterministic/tests -p 'test_*.py'` | `local` | `planned` | inclui fixtures positivas e negativas |
| `DOD-08` | `Definition of Done` | diff restrito à Foundation | `git+guard` | `todo_diff_expectation_guard.py` + fingerprints dos repositórios read-only | `local` | `planned` | mudanças preexistentes não são atribuídas ao TODO |
| `DOD-09` | `Definition of Done` | decisões promovidas aos owners | `review` | matriz de owners + closeout guard | `local` | `planned` | TODO deixa de ser owner de verdade estável |
| `DOD-10` | `Definition of Done` | ausência de PII/payload/segredo persistido | `scan+review` | validator high-risk patterns + checklist manual de privacidade | `local` | `planned` | exemplos somente sintéticos/redigidos |
| `DOD-11` | `Definition of Done` | alias PACED reproduzível | `setup test` | comando de setup documentado + `verify_context.sh` | `clean workspace` | `planned` | symlink continua local e não versionado no produto |
| `VAL-01` | `Validation Steps` | links e anchors válidos | `test` | `python3 deterministic/validate_foundation.py --root .` | `local` | `planned` | fail-closed |
| `VAL-02` | `Validation Steps` | legado classificado por superfície | `test` | validator + `deterministic/legacy_reference_exceptions.json` | `local` | `planned` | exceção exige path, razão e owner |
| `VAL-03` | `Validation Steps` | documentação coerente com produto | `traceability review` | product-truth artifact + hashes da evidence snapshot | `read-only product tree` | `planned` | sem consulta mutante ao banco |
| `VAL-04` | `Validation Steps` | guards PACED aplicáveis passam | `guard` | comandos listados em Rules/Gates | `local` | `planned` | registrar saída específica por gate |
| `VAL-05` | `Validation Steps` | higiene do diff | `git+scan` | `git diff --check` + scan de segredo/artefato | `local` | `planned` | nenhum `.env` ou valor sensível |
| `VAL-06` | `Validation Steps` | evidência 1:1 completa | `review` | esta matriz sem `planned|pending` | `local` | `planned` | bloqueia completion |
| `VAL-07` | `Validation Steps` | produto e Delphi inalterados | `fingerprint` | repetir comandos de `Read-Only Evidence Snapshot` | `workspace` | `planned` | igualdade exata dos digests |
| `VAL-08` | `Validation Steps` | privacidade e segredo | `scan+review` | high-risk pattern scan + inspeção manual registrada | `local` | `planned` | inclui fixtures/artifacts |
| `VAL-09` | `Validation Steps` | setup reproduzível | `setup test` | alias canônico + `bash delphi-ai/bootloaders/verify_context.sh` | `clean workspace` | `planned` | sem commit de link no produto |

## Execution Lane Tracking

- **Local implementation branches:** `uninotas-foundation:main`
- **Promotion lane path:** `main -> origin/main`
- **Lane-promoted threshold for this TODO:** `origin/main` com validações e guards verdes
- **Production-ready threshold for this TODO:** `n/a — pacote documental autônomo; Completed exige publicação imutável em origin/main`

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| baseline do contrato | `main@pending` | `n/a — autoridade Foundation single-branch` | `n/a` | `direct push guarded` | `planned` |
| cutover da Foundation | `main@pending` | `n/a — autoridade Foundation single-branch` | `n/a` | `direct push after closeout gates` | `planned` |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `uninotas-foundation` | `uninotas-foundation/` | `main@b62927be0b5c38ec3e6c529562e8707f1de28bfc` antes da integração dos findings | `commit + working_tree` |
| `MonitorDeNotas` | `./` excluindo `uninotas-foundation/` | `HEAD 78bf271341dfccb2595389f0dbac0e01e8532a7b + fingerprints abaixo` | `immutable read-only snapshot` |
| `delphi-ai` | `delphi-ai/` | `HEAD 9ba43e8bba3618d029320bf6d7b40415881a0287 + clean fingerprints` | `immutable read-only snapshot` |

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
| `uninotas-foundation` | `modules/**` | `A,M,D,R` | substituir módulos herdados pelos módulos do produto atual |
| `uninotas-foundation` | `backlog/**` | `A,M,D,R` | reconciliar candidatos e próximos gates |
| `uninotas-foundation` | `decisions/**` | `A,M,D,R` | registrar decisões e retirar autoridade ativa herdada |
| `uninotas-foundation` | `contracts/**` | `A,M,D,R` | reconstruir índice de contratos verificáveis |
| `uninotas-foundation` | `policies/**` | `A,M,D,R` | preservar apenas políticas aplicáveis ao produto |
| `uninotas-foundation` | `artifacts/**` | `A,M,D,R` | evidência de descoberta/cutover conforme `D-02` |
| `uninotas-foundation` | `todos/**` | `A,M,D,R` | governança, classificação do legado e evidência deste TODO |
| `uninotas-foundation` | `deterministic/**` | `A,M,D,R` | validações específicas da Foundation, se aprovadas no refinamento |
| `uninotas-foundation` | `local_packages.yaml` | `M` | alinhar referências locais ao workspace atual |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorDeNotas` | `backend/**` | `any` | fonte de evidência somente leitura |
| `MonitorDeNotas` | `frontend/**` | `any` | fonte de evidência somente leitura |
| `MonitorDeNotas` | `Dockerfile|docker-compose.yml|railway.json` | `any` | infraestrutura fora do escopo |
| `MonitorDeNotas` | `**/.env*` | `any` | segredos/configuração fora do escopo |
| `delphi-ai` | `**` | `any` | engenharia compartilhada fora do escopo atual |
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
| `Strategic / CTO-Tech-Lead` | `routine-executor` | executar a substituição documental já decidida sem redefinir o contrato | `uninotas-foundation/**` | `planned after authority go` |
| `routine-executor` | `Assurance / Tester-Quality` | desafiar evidência, links, referências e ausência de autoridade concorrente | diff e validações da Foundation | `planned` |
| `Assurance / Tester-Quality` | `formal-reviewer` | revisar aderência arquitetural e integridade do cutover | pacote final consolidado | `planned` |

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
| `PT-01` | Routerfy grava `logs`; Monitor de Notas somente lê por SQL cru; a tabela não possui chave primária e não entra no Prisma. | `backend/docs/tabela-logs.md`; `backend/prisma/schema.prisma`; `backend/src/logs/logs.sql.ts` | `151fbc8540804ff73c8b3d8f8164c1d5d6f932dde8e9aecbcd9f731ff59dd3e6`; `cb53048b181e179e0d0a74188a17279e36213a50508a058fd69bd3a110056963`; `142c26ab4bdda0d53e59934460b029e6463c05e6d30083c7b2e2a2c4fd441643` | `modules/events-and-classification.md` |
| `PT-02` | Somente eventos `org_path = 'SmartNotas'` alimentam o monitor; `ref_id` não é identidade única de uma tentativa e correlaciona tratamentos/histórico. | `backend/src/logs/logs.sql.ts`; `backend/src/logs/logs.service.ts`; `backend/docs/tabela-logs.md` | `142c26ab4bdda0d53e59934460b029e6463c05e6d30083c7b2e2a2c4fd441643`; `5015d24db62ccc93ee65bcac9ba6cb4cb24a6b06a5a21ac2f027326bddd95c6a`; `151fbc8540804ff73c8b3d8f8164c1d5d6f932dde8e9aecbcd9f731ff59dd3e6` | `modules/events-and-classification.md` + `modules/treatments-and-history.md` |
| `PT-03` | Classificação possui projeção TypeScript e expressão SQL equivalentes; situação efetiva aplica o último tratamento, e `PENDENTE` reabre para a situação original. | `backend/src/logs/logs.classifier.ts`; `backend/src/logs/logs.sql.ts`; `backend/src/logs/logs.mapper.ts` | `ca0a4340189321e1924eec0fbda82c492aca4b19bc0476d54953eb8e0eafcfbe`; `142c26ab4bdda0d53e59934460b029e6463c05e6d30083c7b2e2a2c4fd441643`; `4b2358bb136919adc00eaa3b8ff3d5265d3fad3db958e976106c258045d63ef4` | `modules/events-and-classification.md` |
| `PT-04` | A aplicação escreve `monitor_tratamentos` como histórico append-only correlacionado por `ref_id`; o último registro define o tratamento corrente. | `backend/prisma/schema.prisma`; `backend/src/logs/logs.service.ts` | `cb53048b181e179e0d0a74188a17279e36213a50508a058fd69bd3a110056963`; `5015d24db62ccc93ee65bcac9ba6cb4cb24a6b06a5a21ac2f027326bddd95c6a` | `modules/treatments-and-history.md` |
| `PT-05` | A aplicação possui `monitor_usuarios`, autenticação JWT e perfis; usuários são desativados, não apagados, para preservar autoria. | `backend/prisma/schema.prisma`; `backend/src/auth/auth.service.ts`; `backend/src/usuarios/usuarios.service.ts` | `cb53048b181e179e0d0a74188a17279e36213a50508a058fd69bd3a110056963`; `59d506febff80a402e5b01347c2fd3c212ab3408584428c794c8778f7d89814d`; `08033dd301b931ba5a97afffd177393e2899046bc3ed4c65a02c16f989391f5e` | `modules/identity-and-team.md` |
| `PT-06` | SSE envia somente sinal de invalidação; o cliente rebusca a API. Eventos podem vir da API, LISTEN/NOTIFY opcional ou polling, com heartbeat/dedupe. | `backend/src/realtime/realtime.service.ts`; `frontend/src/hooks/useTempoReal.ts` | `5b24b40d4bbe88fbc95e5fe920f3a71a6dae19a2cfc7d83845f8753565d27bed`; `1e5f6bf8b4ce9af68902f2c22a7f85843f4deef05c9a62eb8e6fbba14880a411` | `modules/realtime-invalidation.md` |
| `PT-07` | Monitoramento operacional externo reutiliza o resumo de eventos em janela móvel e deve distinguir banco indisponível de zero erros. | `backend/src/monitoramento/monitoramento.service.ts`; `backend/src/logs/logs.service.ts` | `454461a6678559c61fb409d1a54c5b794600fb185a1b46c63f48a6e5e1a2da32`; `5015d24db62ccc93ee65bcac9ba6cb4cb24a6b06a5a21ac2f027326bddd95c6a` | `modules/operational-monitoring.md` |
| `PT-08` | React/Vite consome listagem, filtros, resumo, detalhe, tratamentos, equipe e invalidação realtime por contratos explícitos da API. | `frontend/src/api/eventos.ts`; `frontend/src/paginas/ListaEventos.tsx`; `frontend/src/paginas/DetalheEvento.tsx`; `frontend/src/paginas/Equipe.tsx` | `1cf0e9f33b6ecfaa9040a5cb8b4d04f9d18c1a5d7b289d53c5c5ba693af9a317`; `0eeb6881f23ded8feeafb0ab36fe7f9f8e78e7463e8706d3e88c9b0ab4f36e9b`; `a4d2829c6b7b1269c8ecc3f0b58c3bc8fe956cae878c80eaad7126f4be90f643`; `2d9a1e8b8645189fefdd832a48209b3a28bf85e68d9216356051e52d19ce010b` | módulos funcionais correspondentes; sem módulo frontend paralelo |
| `PT-09` | Execução e deploy são NestJS + React/Vite + PostgreSQL/Prisma em Docker/Railway, sem mudança de runtime neste TODO. | `Dockerfile`; `docker-compose.yml`; `railway.json`; `backend/src/config/configuration.ts` | `9d0554370de58fd504282f0d8bf98c1bce841d9ef736da11be611dfa17cd9e32`; `5e5e9f39e191b477e9981ba9047ace1ee7082e73ca447d454d27dddcaec9a781`; `f711055e59a2442c04299987a2bc30fe24cd02df86cd9e4e4cf57efec76a5697`; `57f87a470fb953f53ace1511355b9092db6e9c9e12f4c98a1e6cc1fcf8699a4e` | `modules/runtime-and-deployment.md` |

Os hashes completos foram obtidos por `sha256sum` no snapshot de 2026-09-24 e devem ser repetidos antes do closeout; o artifact final de product truth preservará esta matriz Foundation → fonte.

## Canonical Target Module Map

| Final Module | Singular Ownership | Key Invariants / Contracts | Replaces |
| --- | --- | --- | --- |
| `modules/events-and-classification.md` | fronteira read-only Routerfy/SmartNotas, consulta, filtros, paginação, exportação e classificação original/efetiva | nunca escrever em `logs`; `ref_id` não é PK; SQL e classificador devem permanecer semanticamente alinhados | `integrations-and-channels.md`; parte de `inbox-and-conversations.md` |
| `modules/treatments-and-history.md` | comandos de tratamento e histórico auditável | escreve somente `monitor_tratamentos`; correlação por `ref_id`; último tratamento governa situação efetiva; autoria preservada | `audit-and-history.md`; parte de `inbox-and-conversations.md` |
| `modules/identity-and-team.md` | autenticação, perfis e administração da equipe financeira | JWT; usuário ativo; proteção do último admin; desativação preserva autoria | `identity-and-tenancy.md` |
| `modules/realtime-invalidation.md` | sinalização SSE de mudança | evento não é fonte de verdade; consumidor sempre rebusca API; polling é fallback explícito | capacidade inexistente na Foundation herdada |
| `modules/operational-monitoring.md` | contrato para robô/alerta operacional | reutiliza semântica do resumo; indisponibilidade não equivale a zero; janela/limites explícitos | capacidade inexistente na Foundation herdada |
| `modules/runtime-and-deployment.md` | topologia, configuração e deploy comprovados | documentar somente Docker/Railway/configuração observada; sem secret values e sem mudança de runtime | fragmentos transversais herdados, sem transportar domínio LeadsHug |

O índice `modules/README.md` apontará exatamente para estes seis módulos. Adição, remoção, merge ou split material exige atualizar esta tabela e renovar `APROVADO`.

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
| `policies/scope_subscope_governance.md` | `Delete` | política LeadsHug sem owner atual comprovado |
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
| `modules/events-and-classification.md` | `PT-01..PT-03` |
| `modules/treatments-and-history.md` | `PT-02,PT-04` |
| `modules/identity-and-team.md` | `PT-05` |
| `modules/realtime-invalidation.md` | `PT-06` |
| `modules/operational-monitoring.md` | `PT-07` |
| `modules/runtime-and-deployment.md` | `PT-08,PT-09` |
| `deterministic/validate_foundation.py` | validator canônico local |
| `deterministic/legacy_reference_exceptions.json` | exceções históricas com path, razão e owner |
| `deterministic/tests/test_validate_foundation.py` | testes positivos e mutation-style negativos |
| `deterministic/tests/fixtures/**` | trees sintéticos sem PII/segredo real |

## Module Decision Consistency Gate

- **Status:** `prepared-pre-freeze`.
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
| `logs` é fonte externa read-only; tratamentos pertencem à aplicação | `D-04` derivada de evidência e a consolidar | dados, eventos e tratamentos | preserva ownership e impede mutação acidental da tabela Routerfy |
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

- **Canonical commands:** `python3 -m unittest discover -s deterministic/tests -p 'test_*.py'` e `python3 deterministic/validate_foundation.py --root .`.
- **Active-authority surfaces:** documentos raiz, `modules/`, `backlog/`, `contracts/`, `decisions/`, `policies/`, `todos/README.md` e `todos/active/`.
- **Historical surfaces:** `todos/completed/` e artifacts de migração permitidos somente quando listados em `deterministic/legacy_reference_exceptions.json` com `path`, `term`, `reason` e `owner`.
- **Fail-closed checks:** arquivos obrigatórios, índice de seis módulos, links/anchors relativos, ausência dos paths marcados `Delete`, owner único, nenhuma autoridade ativa LeadsHug, exception ledger sem wildcard amplo e nenhum arquivo não classificado pelo publication manifest.
- **Privacy checks:** rejeitar JWT-like tokens, private-key markers, atribuições de segredo e identificadores pessoais plausíveis em artifacts/fixtures; nomes de variáveis e exemplos sintéticos explicitamente marcados são permitidos.
- **Mutation fixtures:** autoridade legada em owner ativo, menção histórica permitida, exception sem owner/razão, link quebrado, módulo órfão, owner ausente e fixture com JWT/PII sintético proibido.
- **Manual complement:** revisar semanticamente que nenhuma ocorrência permitida apresenta o legado como verdade atual e que nenhum exemplo deriva de payload real.

### PACED Workspace Alias Contract

- **Owner:** setup local do workspace do Monitor de Notas; o repositório de produto não versiona esse symlink.
- **Required topology:** `foundation_documentation -> uninotas-foundation` e `delphi-ai -> C:\Unifast\delphi-ai` (ou paths equivalentes no host).
- **Canonical Windows command:** `cmd /c mklink /D foundation_documentation uninotas-foundation` quando o alias ainda não existir; para o Delphi, `cmd /c mklink /D delphi-ai C:\Unifast\delphi-ai`.
- **WSL equivalent:** `ln -s uninotas-foundation foundation_documentation` e `ln -s /mnt/c/Unifast/delphi-ai delphi-ai`, somente depois de confirmar que o destino não existe.
- **Acceptance:** `test -L foundation_documentation && test -L delphi-ai` e `bash delphi-ai/bootloaders/verify_context.sh` devem passar em workspace limpo.
- **Scope boundary:** os aliases atuais são infraestrutura local preestabelecida e read-only neste TODO; recriação para validar setup não é mudança persistente do produto nem autoriza qualquer outro path raiz.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before execution authority`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** reviewer `fresh-stateless-paced-architecture-reviewer`; hard cutover confirmado, achados `ARCH-OP-01..05` deduplicados em `RF-01..RF-08`; novo review obrigatório sobre baseline renovado e imutável.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`
- **No-go handling:** retornar ao diagnóstico/decisão ou ao loop de evidência; não alegar execução ou conclusão com divergência aberta.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | O snapshot de código/configuração é a fonte técnica para reconstruir a verdade do produto; READMEs somente corroboram. | `PT-01..PT-09`, paths e SHA-256 exatos no snapshot `HEAD 78bf271341dfccb2595389f0dbac0e01e8532a7b` | qualquer hash divergente reabre inventário e scope review | `High` | `Keep as Assumption` |
| `A-02` | A tabela `logs` permanece read-only e pertence ao Routerfy. | `backend/prisma/schema.prisma@cb53048b…`, `backend/src/logs/logs.sql.ts@142c26ab…`, `backend/docs/tabela-logs.md@151fbc85…` | muda invariantes, contratos e módulos | `High` | `Promoted to D-04` |
| `A-03` | `uninotas-foundation` é a autoridade específica do produto e `delphi-ai` distribui o PACED obrigatório para todo trabalho. | `D-03`; `delphi-ai/README.md` no commit `9ba43e8bba3618d029320bf6d7b40415881a0287`; alias contract local | muda links, responsabilidades e gates | `High` | `Promoted to D-03` |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** a migração documental precisa provar que as afirmações sobre arquitetura, ownership de dados e comportamento correspondem ao código atual antes de congelar o contrato.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md`
- **Gate status:** `findings_integrated`
- **Findings summary:** primeira leitura detectou que `A-01` não possuía paths/hashes concretos; o snapshot `PT-01..PT-09` integrou a correção.
- **Evidence / reference:** `Read-Only Evidence Snapshot` + `Pre-Execution Product Truth Baseline`; execução determinística final permanece pendente do review renovado.
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** o pacote é `big`, altera toda a autoridade documental e precisa de baseline imutável antes das revisões independentes.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `main`
- **Baseline commit:** `092b099fd7d49d1f1859586026dd6c70ce90f2e7`
- **Baseline push reference:** `origin/main@092b099fd7d49d1f1859586026dd6c70ce90f2e7`
- **Baseline TODO blob:** `f393bb904b2aec6faa003ffff784f6e5f22103a6`
- **Baseline snapshot SHA-256:** `2f89a72e2bac26f7428129accd69d5ee951fbd12cef4ae09141ffa316e6ba91c`
- **Gate status:** `no_material_findings`
- **Findings summary:** `RF-01..RF-08` foram integrados em pacote material novo; commit, remoto, blob e snapshot exato estão ligados antes do rerun.
- **Evidence / reference:** git-write guards `go`; push `b62927b..092b099`; `ls-remote` confirmou o SHA integral; package imutável `/tmp/monitor-foundation-review.tJs1Sm/review-package-092b099.md` possui o SHA-256 registrado.
- **Waiver authority / reference:** `n/a`
- **Pre-freeze packet-prep rule:** toda revisão abaixo permanece `prepared-pre-freeze`; nenhuma está marcada como aprovada antes do baseline publicado.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impedir que a revisão ou o plano ampliem silenciosamente o contrato aprovado.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before execution authority`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md`
- **Gate status:** `not_run`
- **Findings summary:** baseline material renovado e ligado; executar após o segundo ciclo de reviews.
- **Evidence / reference:** finding histórico `RF-02` integrado; comando canônico permanece inalterado.
- **Waiver authority / reference:** `n/a`

## Plan Review Gate

- **Status:** `findings_integrated — rerun required on renewed immutable baseline`

### Review Sections

- [ ] Architecture
- [ ] Code Quality
- [ ] Tests
- [ ] Performance
- [ ] Security
- [ ] Elegance
- [ ] Structural Soundness

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

- [ ] Excluir um arquivo genérico ainda útil junto com conteúdo LeadsHug; mitigar reconstruindo por owner/propósito e validando links.
- [ ] Canonizar contagens operacionais temporárias como verdade permanente; manter números voláteis fora dos invariantes.
- [ ] Documentar `logs` como tabela Prisma ou gravável; validar ownership read-only contra schema/SQL.
- [ ] Duplicar regras PACED na Foundation; validar que docs locais referenciam o owner compartilhado.
- [ ] Deixar TODOs ativos LeadsHug autorizando trabalho; scan deve falhar para qualquer autoridade ativa residual.
- [ ] Copiar valores de `.env`; usar apenas nomes/redações e executar scan de segredos.

### Residual Unknowns / Risks

- [ ] O conteúdo exato dos novos módulos será refinado durante o inventário, sem alterar o conjunto de domínios aprovado em `S-04`.
- [ ] O setup doctor PACED não valida semântica de produto; o validator local e a revisão de rastreabilidade precisam cobrir essa lacuna.

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
- **Critique status:** `findings_integrated`
- **Findings summary:** reviewer confirmou a direção de hard cutover, mas recusou execução por aprovação fora de ordem, dispatch mutável, evidência read-only não congelada, decisões destrutivas incompletas, scan legado ambíguo, privacidade incompleta e escopo raiz contraditório.
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

- **Evidence / reference:** dispatch `/tmp/monitor-foundation-review.tJs1Sm/critique-dispatch.json`; merge validado pelo schema; achados `CRIT-01..07` deduplicados em `RF-01..RF-08`.
- **Waiver authority / reference:** `n/a`

## Promotion Finding Routing Ledger

Os achados de arquitetura e crítica foram congelados, deduplicados e classificados contra o objetivo, decisões e non-goals do TODO. Todos permanecem no mesmo TODO porque são requisitos para autoridade de execução, não trabalho de hardening posterior.

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `RF-01` (`ARCH-OP-02`,`CRIT-01`) | `high` | `release-blocker` | tratar aprovação anterior como intenção; exigir novo `APROVADO` pós-gates | ordem de autoridade é parte do contrato atual | `integrated; gate rerun pending` | `Approval.Current authority`; novo approval pendente |
| `RF-02` (`ARCH-OP-03`,`CRIT-02`) | `high` | `release-blocker` | commit + TODO blob/hash no dispatch e freeze renovado | reproducibilidade do review atual | `integrated; baseline refresh pending` | `Gate: Review Baseline Freeze` |
| `RF-03` (`ARCH-OP-01`,`CRIT-04`) | `high` | `release-blocker` | inventário read-only, seis módulos fechados e disposition 1:1 antes da execução | elimina discricionariedade destrutiva do executor | `integrated; rerun pending` | `PT-01..PT-09`; module map; disposition manifest |
| `RF-04` (`CRIT-03`) | `high` | `release-blocker` | HEAD/status/diff/content fingerprints para produto e Delphi | prova `VAL-07` e ancora assumptions em bytes | `integrated; guard rerun pending` | `Read-Only Evidence Snapshot` |
| `RF-05` (`ARCH-OP-04`,`CRIT-05`) | `medium` | `release-blocker` | validator por superfície + exception ledger explícito + mutation fixtures | `DOD-01/VAL-02` dependem dessa semântica | `integrated; delivery evidence pending` | `Deterministic Validator Contract` |
| `RF-06` (`CRIT-06`) | `medium` | `release-blocker` | proibir PII/payload/JWT/credencial e exigir scan + revisão manual | artefatos persistentes fazem parte da entrega atual | `integrated; delivery evidence pending` | `DOD-10`; `VAL-08`; Security Risk Assessment |
| `RF-07` (`ARCH-OP-05`) | `medium` | `release-blocker` | documentar owner/comandos/aceitação do alias em workspace limpo | setup PACED é condição operacional atual | `integrated; clean-workspace evidence pending` | `DOD-11`; `VAL-09`; alias contract |
| `RF-08` (`CRIT-07`) | `medium` | `release-blocker` | declarar aliases preestabelecidos/read-only e remover escrita raiz do touched scope | mantém diff enforcement determinístico | `integrated; diff guard pending` | `Touched Surfaces`; `Diff Expectation Contract` |

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** o TODO criará validator e testes que sustentam o cutover canônico.
- **Trigger signals in scope:** `changed test logic|architectural change|non-trivial validation risk`
- **Required evidence matrix:** `unit + mutation-style negative fixtures`
- **Package mode:** `bounded-file-set`
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after implementation`
- **Audit status:** `not_run`
- **Findings summary:** `pending implementation`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** conclusão remove uma autoridade documental e estabelece outra.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede`
- **Package mode:** `bounded-file-set`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after implementation and test audit`
- **Canonical multi-lane audit protocol:** `n/a`
- **Final review status:** `not_run`
- **Findings summary:** `pending implementation`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `required`
- **Why this decision:** há aposentadoria completa da autoridade LeadsHug e proibição de fallback interno.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement`
- **Package mode:** `bounded-file-set`
- **Canonical multi-lane audit protocol:** `n/a`
- **Cutover audit status:** `not_run`
- **Findings summary:** `pending implementation`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Execution Plan — Draft, Not Authorized

1. Tratar a aprovação anterior como intenção de planejamento e integrar `RF-01..RF-08`.
2. Congelar/publicar o TODO com inventário `PT-01..PT-09`, mapa final de seis módulos, disposition 1:1 e contratos exatos de validação.
3. Repetir arquitetura e crítica sobre snapshot ligado a commit/blob/hash; executar coerência, scope drift e authority preflight.
4. Solicitar novo `APROVADO`; somente depois executar o authority guard normal e exigir `go`.
5. Reescrever a camada canônica raiz e a divisão de autoridades conforme o manifesto congelado.
6. Reconstruir módulos, contratos, decisões, backlog, políticas e TODO governance exatamente nos targets aprovados.
7. Remover do tree atual os paths `Delete`, preservando proveniência somente no histórico Git.
8. Implementar test-first o validator/fixtures e executar validações, reviews delivery-side, consolidação e closeout.

### Touched Surfaces

- `uninotas-foundation/*.md`
- `uninotas-foundation/{modules,backlog,decisions,contracts,policies,artifacts,todos,deterministic}/**`
- `uninotas-foundation/local_packages.yaml`
- os aliases PACED existentes no root são preestabelecidos e read-only; este TODO não cria, edita, remove nem versiona paths no repositório do produto.

### Test Strategy

- **Strategy:** `test-first` para o validator local; `review-after` para documentos canônicos.
- **Why:** fixtures negativas precisam provar que o guard falha para identidade legada, links inválidos e autoridade concorrente antes da implementação final.
- **Fail-first targets:** testes temporários/fixtures do validator para ocorrência proibida em superfície ativa, link quebrado e owner canônico ausente.
- **Exact local suite:** `python3 -m unittest discover -s deterministic/tests -p 'test_*.py' && python3 deterministic/validate_foundation.py --root .`.

### Runtime / Rollout Notes

- Não há migração, feature flag ou rollout de runtime.
- A publicação é atômica no repositório Foundation `main`; o tree candidato deve passar antes do commit final.
- O banco remoto permanece somente leitura durante validações deste TODO.

## Questions To Close

- [x] Nenhuma questão material aberta; `D-01..D-04` formam a baseline congelada.

## Rules Acknowledgement / Ingestion

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

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `explicit human reference — D-03 + “APROVADO” em 2026-09-24 exige que todo trabalho passe pelo PACED`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Waiver / exception reference:** `n/a`

## Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Migração da Foundation | `structure-only documentation governance` | `n/a` | `n/a` | `no` | `no` | inspeção documental, guards e comparação read-only com código | não altera comportamento ou fluxo de usuário |

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `uninotas-foundation / structural validation` | documentos e checks serão alterados | identidade, links, owner único, privacy patterns e ausência de autoridade concorrente | novo `APROVADO`, authority `go` e tree candidato | `python3 -m unittest discover -s deterministic/tests -p 'test_*.py' && python3 deterministic/validate_foundation.py --root .` | `Local-Implemented` | `planned` | `Deterministic Validator Contract` | nenhuma suíte genérica substitui estes checks específicos |

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
- **Current delivery stage at review time:** `Pending`

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
| `origin/main` de `uninotas-foundation` | baseline freeze e publicação final | `healthy` | `2026-09-24` | `ls-remote` confirmou `092b099fd7d49d1f1859586026dd6c70ce90f2e7`; blob/hash do package registrados | publicar somente novas evidências não materiais até o review convergir |
| `delphi-ai` local | workflows e guards PACED | `healthy with runner caveat` | `2026-09-24` | `verify_context.sh` via Git Bash passou | scripts CRLF rodam pelo Git Bash; Python guards rodam no WSL |
| PostgreSQL/Railway | somente evidência read-only de arquitetura | `healthy` | `2026-09-24` | `/api/v1/saude` retornou banco `ok` | nenhuma mutação/seed/E2E neste TODO |

## Review and Delivery Gates

- **Review Baseline Freeze:** required before the first planning-side guard/review.
- **Review Scope Drift:** required after review convergence and before `APROVADO`.
- **Independent planning critique:** required because complexity is `big` and the blast radius is cross-module within the Foundation.
- **Authority guard:** must return `go` only after explicit `APROVADO`, rule ingestion and resolved decisions.
- **Completion and closeout guards:** required before `Local-Implemented` or movement to `completed/`.
- **Cutover integrity audit:** required because the work retires one active documentary authority and establishes another.

## TODO Closeout Disposition

- **Disposition:** `blocked`
- **Disposition reason:** findings de planejamento foram integrados, mas freeze/reviews/guards renovados e novo `APROVADO` ainda são obrigatórios antes de executar.
- **Post-commit/push status:** `renewed baseline pending`
- **Next path/status action:** permanecer em `todos/active/process/` até implementação, evidência, reviews e closeout completos.
