# TODO — Monitor de Notas: adequar `uninotas-foundation` ao projeto

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Lifecycle state:** `Approved — execution pending PACED authority gates`
- **Created:** `2026-09-24`
- **Owner:** `Delphi / Strategic CTO-Tech-Lead`, sob autoridade humana do usuário

## Approval

- **Approved by:** `usuário — 2026-09-24 — “APROVADO”`
- **Approval scope:** executar `S-01..S-09` conforme `D-01..D-03`, limitando mudanças persistentes à Foundation do Monitor de Notas e à integração local PACED necessária para operar o método.
- **Execution not authorized:** código/runtime do Monitor de Notas, banco, deploy, segredos e núcleo compartilhado do `delphi-ai`; worktrees e checkouts auxiliares também não foram autorizados.
- **Renewed approval required when:** houver mudança de escopo, identidade canônica, tratamento do legado, arquitetura-alvo, validações obrigatórias ou repositórios envolvidos.

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
- **Qualifiers:** `none`
- **Next exact step:** congelar e publicar o baseline do TODO, executar as revisões/guards PACED pendentes e liberar a implementação somente após o authority guard retornar `go`.

## Active Work State

- **Work state:** `review`
- **Why this state now:** o usuário aprovou o contrato, mas os gates PACED de baseline, crítica, coerência e autoridade ainda precisam convergir antes da implementação.
- **Exit condition:** gates pré-execução verdes e authority guard pós-aprovação em `go`, quando o estado muda para `implementation`.

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

## Validation Steps

- [ ] `VAL-01` Verificar links internos e anchors em todos os documentos canônicos alterados.
- [ ] `VAL-02` Executar busca fail-closed por `LeadsHug|leadshug|WhatsApp|Typebot|Evolution|Baileys|Belluga|Bóora` e classificar cada ocorrência restante como histórica permitida ou falha.
- [ ] `VAL-03` Comparar stack, rotas, módulos, entidades e invariantes documentados com `backend/`, `frontend/`, `Dockerfile`, `docker-compose.yml`, `railway.json` e READMEs do produto.
- [ ] `VAL-04` Executar os guards aplicáveis do `delphi-ai` para escopo, autoridade, expectativa de diff, conclusão e closeout.
- [ ] `VAL-05` Executar `git diff --check` e confirmar ausência de segredos, artefatos gerados ou mudanças fora do contrato.
- [ ] `VAL-06` Revisar a matriz de evidências critério a critério; resumo agregado não substitui evidência 1:1.
- [ ] `VAL-07` Confirmar que o repositório do produto e o `delphi-ai` não receberam mudanças durante a execução.

## Completion Evidence Matrix

Preencher com uma linha individual para cada item de `DOD-01..DOD-09` e `VAL-01..VAL-07` antes de qualquer alegação `Local-Implemented` ou movimento para `completed/`.

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01..DOD-09` | `Definition of Done` | critérios de migração documental | `doc/review/test` | `pending refinement` | `local` | `planned` | expandir 1:1 antes da execução |
| `VAL-01..VAL-07` | `Validation Steps` | validações do cutover | `test/review` | `pending refinement` | `local` | `planned` | expandir 1:1 antes da execução |

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
| `uninotas-foundation` | `uninotas-foundation/` | `main@f0e9e1ee590a` | `working_tree` |
| `MonitorDeNotas` | `./` excluindo `uninotas-foundation/` | `read-only evidence source; dirty pre-existing tree` | `working_tree` |
| `delphi-ai` | `delphi-ai/` | `read-only shared engineering authority` | `working_tree` |

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

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `modules/identity-and-tenancy.md` | identidade multi-tenant e BU WhatsApp do LeadsHug | `Supersede (Intentional)` | domínio incompatível com Monitor de Notas |
| `modules/inbox-and-conversations.md` | caixa e conversas WhatsApp | `Supersede (Intentional)` | módulo inexistente no produto atual |
| `modules/integrations-and-channels.md` | Meta/Evolution/Typebot e canais | `Supersede (Intentional)` | integrações incompatíveis com Routerfy/SmartNotas |
| `modules/audit-and-history.md` | auditoria do atendimento LeadsHug | `Supersede (Intentional)` | substituir por histórico de tratamentos e ownership real |
| `modules/README.md` | índice de módulos LeadsHug | `Supersede (Intentional)` | novo índice será derivado do produto atual |

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

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before execution authority`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `pending review baseline freeze`
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
| `A-01` | O código e os READMEs atuais são a melhor fonte disponível para reconstruir a verdade do produto. | aplicação inicializada; 34 testes verdes; READMEs e configuração inspecionados em 2026-09-24 | exigir fontes adicionais e revisar escopo | `High` | `Keep as Assumption` |
| `A-02` | A tabela `logs` permanece read-only e pertence ao Routerfy. | `README.md`, `backend/README.md`, `schema.prisma` e SQL isolado | muda invariantes, contratos e módulos | `High` | `Promote to Decision during refinement` |
| `A-03` | `uninotas-foundation` é a autoridade específica do produto e `delphi-ai` distribui o PACED obrigatório para todo trabalho. | decisão `D-03` e contrato PACED em `delphi-ai/README.md` | muda links, responsabilidades e gates | `High` | `Promoted to D-03` |

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** a migração documental precisa provar que as afirmações sobre arquitetura, ownership de dados e comportamento correspondem ao código atual antes de congelar o contrato.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-foundation-project-rebase.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending contract refinement`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** o pacote é `big`, altera toda a autoridade documental e precisa de baseline imutável antes das revisões independentes.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `main`
- **Baseline commit:** `pending`
- **Baseline push reference:** `origin/main@pending`
- **Gate status:** `not_run`
- **Findings summary:** contrato preparado; commit/push ainda pendentes.
- **Evidence / reference:** executar `git_write_authority_guard.py` para commit e push, então registrar SHA.
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
- **Findings summary:** `pending freeze-backed review`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Plan Review Gate

- **Status:** `prepared-pre-freeze`

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
- **Critique status:** `not_run`
- **Findings summary:** `pending baseline freeze`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

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

1. Decisões `D-01..D-03` fechadas pela autoridade humana em 2026-09-24.
2. Refinar o contrato, congelar baseline do TODO e executar revisão de plano/escopo PACED antes do `APROVADO`.
3. Produzir inventário de verdade do produto e mapa de substituição dos owners canônicos.
4. Reescrever a camada canônica raiz e a divisão de autoridades.
5. Reconstruir módulos, contratos, decisões, backlog, políticas e TODO governance.
6. Remover do tree atual o legado LeadsHug aprovado para exclusão, preservando sua proveniência somente no histórico Git.
7. Implementar ou adaptar os checks estruturais aprovados.
8. Executar validações, revisão independente proporcional, consolidação e closeout.

### Touched Surfaces

- `uninotas-foundation/*.md`
- `uninotas-foundation/{modules,backlog,decisions,contracts,policies,artifacts,todos,deterministic}/**`
- `uninotas-foundation/local_packages.yaml`
- integração operacional local PACED no root, sem alteração de código/runtime e sem commit no repositório de produto.

### Test Strategy

- **Strategy:** `test-first` para o validator local; `review-after` para documentos canônicos.
- **Why:** fixtures negativas precisam provar que o guard falha para identidade legada, links inválidos e autoridade concorrente antes da implementação final.
- **Fail-first targets:** testes temporários/fixtures do validator para ocorrência proibida em superfície ativa, link quebrado e owner canônico ausente.

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
| `uninotas-foundation / structural validation` | documentos e checks serão alterados | identidade, links, schemas e ausência de autoridade concorrente | contrato aprovado e tree candidato | definir no refinamento após inventariar os checks aplicáveis | `Local-Implemented` | `planned` | `pending` | nenhuma suíte genérica pode substituir checks específicos |

## Security Risk Assessment

- **Risk level:** `low`
- **Why this risk level:** o escopo é documental, mas pode expor segredos se exemplos ou `.env` forem copiados indevidamente.
- **Attack surface in scope:** referências a credenciais, URLs e topologia operacional.
- **Attack simulation decision:** `not_needed`
- **Review evidence:** usar apenas nomes de variáveis e valores redigidos; executar scan de segredos antes do closeout.
- **Residual security risk:** `none` se o scan permanecer limpo.

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
| `origin/main` de `uninotas-foundation` | baseline freeze e publicação final | `unknown` | `2026-09-24` | remote configurado; push ainda não testado | authority guard antes de qualquer push |
| `delphi-ai` local | workflows e guards PACED | `healthy with runner caveat` | `2026-09-24` | `verify_context.sh` via Git Bash passou | scripts CRLF rodam pelo Git Bash; Python guards rodam no WSL |
| PostgreSQL/Railway | somente evidência read-only de arquitetura | `healthy` | `2026-09-24` | `/api/v1/saude` retornou banco `ok` | nenhuma mutação/seed/E2E neste TODO |

## Review and Delivery Gates — Pending Refinement

- **Review Baseline Freeze:** required before the first planning-side guard/review.
- **Review Scope Drift:** required after review convergence and before `APROVADO`.
- **Independent planning critique:** required because complexity is `big` and the blast radius is cross-module within the Foundation.
- **Authority guard:** must return `go` only after explicit `APROVADO`, rule ingestion and resolved decisions.
- **Completion and closeout guards:** required before `Local-Implemented` or movement to `completed/`.
- **Cutover integrity audit:** required because the work retires one active documentary authority and establishes another.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** contrato aprovado, porém ainda em review PACED até baseline/revisões/authority guard liberarem execução.
- **Post-commit/push status:** `pending`
- **Next path/status action:** permanecer em `todos/active/process/` até implementação, evidência, reviews e closeout completos.
