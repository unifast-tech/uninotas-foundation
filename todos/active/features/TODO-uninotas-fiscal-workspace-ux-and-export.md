# TODO — Evoluir a experiência fiscal e exportação do UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Created:** `2026-09-28`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário

## Context

A validação visual da primeira versão do UniNotas revelou problemas de contraste nos selects, desalinhamento dos filtros, ação de atualização redundante, marca provisória, navegação administrativa dispersa e paginação sem respiro. O usuário também precisa exportar o conjunto completo de notas que corresponde ao contexto e aos filtros aplicados na tela `Geral`.

Este corte estabelece uma experiência única e coerente para o workspace fiscal: `Geral` continua lendo Smart Notas para um único `FiscalIssuerContext`; `Processamento das notas` leva à projeção PostgreSQL existente; configurações de conta ficam em um menu acessível; e uma exportação CSV backend-owned percorre as páginas do provedor sem misturar Unifast e Prosperar nem entregar resultado silenciosamente parcial.

## Framing Source & Story Slice

- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `n/a`
- **Why this is the right current slice:** os sete pontos pertencem à mesma jornada autenticada `Geral -> filtrar -> exportar/navegar/configurar` e serão entregues no mesmo frontend e na mesma aprovação.
- **Direct-to-TODO rationale:** o comportamento já foi observado na interface, os destinos e dados existentes são conhecidos, e a única ambiguidade material — exportar página ou filtro inteiro — foi resolvida pelo usuário como filtro inteiro.

## Contract Boundary

- Este TODO define a evolução visual/navegacional do frontend e o endpoint fiscal de exportação necessário para baixar o filtro completo.
- A exportação sempre usa exatamente um contexto selecionado (`unifast` ou `prosperar`) e nunca cria uma lista agregada.
- O CSV representa todos os registros do filtro quando o total estiver dentro do limite operacional aprovado; acima dele, a API falha antes do download e orienta reduzir o filtro. Truncamento silencioso é proibido.
- O TODO é bounded but elastic somente para componentes, estilos, DTOs, serviço, testes e documentação diretamente necessários a essa jornada.
- Alteração da fonte de verdade, do conteúdo da tela operacional, do modelo de autenticação ou de deploy exige renovação de aprovação.

## Implementation Intent

- **Current delivery:** UI fiscal corrigida; marca oficial; menu de configurações; link `Processamento das notas`; paginação centralizada; exportação CSV completa do filtro selecionado com backend paginando Smart Notas de forma limitada e cancelável.
- **Planned next steps:** o cutover Smart Notas permanece governado por seu TODO próprio.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** entregar a jornada observada pelo usuário sem misturar autoridades fiscais/operacionais nem transferir paginação pesada para o navegador.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** congelar/revisar este plano, obter `preflight-go` e solicitar `APROVADO` antes de editar código.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** o contrato está sendo preparado para os gates de arquitetura, crítica e autoridade.
- **Exit condition:** `APROVADO` explícito e authority guard pós-aprovação em `go`, ou bloqueio formal.

## Provisional Notes

- **Missing for delivery:** implementação, testes, CI-equivalent, auditorias e consolidação canônica.
- **Revisit criteria:** qualquer mudança no limite/semântica do CSV, agregação de contextos, conteúdo da tela operacional ou modelo de sessão.
- **Dependencies unblocked:** os endpoints list/detail e o downloader autenticado já existem; Smart Notas retorna `total` e `totalPages` por contexto.

## Blocker Notes

- **Blocked:** `no`.
- **Current blocker:** `none`.
- **Unblock condition:** `n/a`.

## Scope

- [ ] `SCOPE-01` Corrigir selects nativos para que campo e opções tenham contraste legível nos temas claro e escuro.
- [ ] `SCOPE-02` Alinhar os controles da barra de filtros pela base; manter atualização automática de contexto/status/datas; remover o botão manual `Atualizar`; manter `Aplicar filtros` apenas para Documento e ID da compra.
- [ ] `SCOPE-03` Substituir a marca provisória pela imagem oficial fornecida pelo usuário, armazenada como ativo local versionado e com fallback acessível.
- [ ] `SCOPE-04` Substituir o bloco textual de sessão por um botão de configurações acessível que exiba nome, e-mail e perfil da conta; ofereça tema claro/escuro, senha e sair; e mostre Equipe somente para ADMIN.
- [ ] `SCOPE-05` Adicionar `Processamento das notas` ao lado de `Smart Notas`, apontando para a tela PostgreSQL existente sem alterar sua fonte, filtros ou semântica neste TODO.
- [ ] `SCOPE-06` Centralizar a paginação fiscal e garantir espaçamento inferior suficiente em desktop e celular.
- [ ] `SCOPE-07` Expor `GET /api/v1/notas/exportar` para todos os perfis leitores, usando os mesmos filtros fiscais da listagem exceto `pagina`, um único contexto e CSV UTF-8/BOM separado por ponto e vírgula.
- [ ] `SCOPE-08` Exportar todas as páginas do filtro até o limite rígido de 20.000 registros; rejeitar antes de gerar o arquivo quando `total > 20.000`; nunca truncar ou combinar contextos.
- [ ] `SCOPE-09` Paginar o provedor sequencialmente, preservar ordem por página, validar coerência entre páginas, respeitar abort do cliente e falhar sem arquivo quando qualquer página falhar.
- [ ] `SCOPE-10` Neutralizar fórmula de planilha em todo valor textual iniciado por `=`, `+`, `-`, `@`, TAB, CR ou LF; escapar aspas; usar nome de arquivo sanitizado com contexto e período.
- [ ] `SCOPE-11` Adicionar o botão `Exportar CSV` na Geral, desabilitado sem resultados ou durante exportação, com erro independente da listagem e proteção contra cliques duplicados.
- [ ] `SCOPE-12` Atualizar testes backend/frontend/browser e consolidar o contrato estável no módulo fiscal.

## Out of Scope

- Lista agregada Unifast + Prosperar, exportação multi-contexto ou um terceiro contexto “Geral”.
- Alterar o conteúdo/queries da tela PostgreSQL de processamento; hard cut error-only permanece no TODO de cutover.
- DANFE, XML, emissão, cancelamento, mutations fiscais ou persistência/cache de notas.
- Prisma, schema PostgreSQL, Docker, Railway, variáveis de ambiente, deploy ou merge.
- Nova biblioteca de UI, ícones, CSV, tema ou estado; usar React, CSS e Web APIs já presentes.
- Retry automático de Smart Notas, export assíncrono persistido, fila/worker ou arquivo temporário no servidor.
- Worktrees, checkouts auxiliares, branches `worker/*`/`reconcile/*` ou escritores paralelos de código.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:release/uninotas-smart-notas`; `uninotas-foundation:main`
- **Promotion lane path:** `n/a — este TODO termina como Local-Implemented até decisão de promoção separada`
- **Lane-promoted threshold for this TODO:** `n/a`
- **Production-ready threshold for this TODO:** `n/a — deploy continua no TODO de cutover`

## Promotion Evidence

| Scope Item | Local Branch/Commit | Main / Authority | Current Status |
| --- | --- | --- | --- |
| Produto | `release/uninotas-smart-notas@a4b5a0eb6ae96291ffe5c6e16f297b64dcd62f29` | implementação ainda não iniciada | `Pending` |
| Foundation | `main@db96701aa7b0600a67074c7bd47c4a1e3613ec93` | TODO a congelar/publicar | `review` |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; qualquer path não classificado exige análise e, se ampliar escopo, nova aprovação`
- **User validation:** `required on material deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `release/uninotas-smart-notas@a4b5a0eb6ae96291ffe5c6e16f297b64dcd62f29` | `working_tree`, preservando `artifacts/**` e gitlink preexistentes |
| `uninotas-foundation` | `foundation_documentation` | `main@db96701aa7b0600a67074c7bd47c4a1e3613ec93` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `frontend/public/marca-unifast.jpeg` | `A` | imagem oficial fornecida pelo usuário |
| `MonitorNotes` | `frontend/src/componentes/Cabecalho.tsx` | `M` | marca, navegação e menu de configurações |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | filtros, exportação e paginação |
| `MonitorNotes` | `frontend/src/paginas/DetalheNota.tsx`, `frontend/src/App.tsx` | `M` | nomenclatura/navegação operacional se necessário |
| `MonitorNotes` | `frontend/src/api/notas.ts`, `frontend/src/api/cliente.ts` | `M` | download autenticado fiscal e filtros sem página |
| `MonitorNotes` | `frontend/src/hooks/useTema.ts` | `M` | controle explícito de tema no menu, se necessário |
| `MonitorNotes` | `frontend/src/estilos/*.css` | `M` | contraste, menu, alinhamento e paginação |
| `MonitorNotes` | `frontend/e2e/notas.mjs`, `frontend/e2e/notas-unit.ts` | `M` | jornada e transformação CSV/UI |
| `MonitorNotes` | `frontend/README.md` | `M` | comportamento visível e comando de validação |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M|A` | DTO, endpoint, orquestração paginada, CSV e testes |
| `MonitorNotes` | `backend/src/common/csv.ts`, `backend/src/common/csv.spec.ts` | `A` | helper host-local seguro e reutilizável, se a implementação confirmar necessidade |
| `MonitorNotes` | `backend/README.md` | `M` | contrato público da exportação |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-workspace-ux-and-export.md` | `A|M|D` | contrato/evidência/closeout |
| `uninotas-foundation` | `todos/completed/features/TODO-uninotas-fiscal-workspace-ux-and-export.md` | `A` | destino de closeout, se concluído |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | contrato fiscal estável |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | publicação governada dos paths finais, se exigida pelo validator |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/**` | `any` | nenhuma mudança de dados |
| `MonitorNotes` | `backend/src/logs/**` | `any` | processamento PostgreSQL não muda neste TODO |
| `MonitorNotes` | `Dockerfile`, `docker-compose.yml`, `.github/**` | `any` | runtime/pipeline fora do escopo |
| `MonitorNotes` | `backend/.env*`, `frontend/.env*` | `any` | nenhuma configuração nova |
| `MonitorNotes` | `artifacts/**` | `D|M` | evidências preexistentes pertencem ao usuário; somente novos tmp governados podem ser adicionados se exigidos |
| `uninotas-foundation` | `project_constitution.md`, `system_roadmap.md`, `policies/**`, `deterministic/**` | `any` | nenhuma mudança constitucional/estratégica/validator |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / defense | Decision | User validation |
| --- | --- | --- | --- | --- |
| `uninotas-foundation` gitlink e `artifacts/**` já divergentes no superprojeto | `pre-existing user-owned state` | observado antes do TODO | preservar, não stagear/alterar | já divulgado; qualquer toque novo bloqueia |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** pequenos componentes, helpers e fixtures necessários aos critérios acima, sem nova dependência.
- **Must update or split the TODO:** aggregate export, fila/worker, persistência, alteração de logs, novo segredo/config ou qualquer mudança de deploy.

## Definition of Done

- [ ] `DOD-01` Selects permanecem legíveis nos temas claro e escuro; filtros e ações alinham; não existe botão manual `Atualizar` na Geral.
- [ ] `DOD-02` A imagem oficial aparece no cabeçalho com fallback; `Processamento das notas` abre a tela PostgreSQL existente.
- [ ] `DOD-03` Menu de configurações é acessível por teclado/clique externo/Escape, mostra conta/perfil, controla tema, senha e sair; Equipe aparece somente para ADMIN.
- [ ] `DOD-04` Paginação da Geral fica centralizada, responsiva e com espaço inferior.
- [ ] `DOD-05` Exportar CSV baixa o filtro inteiro do contexto selecionado, independentemente da página visível, com colunas e nome determinísticos.
- [ ] `DOD-06` Exportações vazias ou acima de 20.000 linhas são tratadas explicitamente; nenhum arquivo parcial/truncado é apresentado como sucesso.
- [ ] `DOD-07` Paginação upstream é sequencial, limitada, cancelável e valida consistência; list/detail continuam com uma chamada upstream por request.
- [ ] `DOD-08` CSV é UTF-8/BOM, `;`, protege contra fórmula e não contém token, CNPJ configurado, payload cru, `idInterno` ou `noteId` opaco.
- [ ] `DOD-09` Clique duplicado não inicia duas exportações; navegação/logout durante exportação cancela ou invalida o fluxo sem efeito tardio.
- [ ] `DOD-10` Suites backend/frontend/browser, auditorias requeridas e guards finais passam; módulo fiscal documenta o contrato sem promover deploy.

## Validation Steps

- [ ] `VAL-01` Test-first: criar negativas backend para rota/filtros, múltiplas páginas, zero, >20.000, página inconsistente, abort/falha intermediária, CSV injection e headers/arquivo.
- [ ] `VAL-02` Executar no backend `npm test -- --runInBand && npm run build && npm run lint`.
- [ ] `VAL-03` Test-first: ampliar browser interceptado para tema/select, menu e permissões, link de processamento, export completo/erro/double-click e paginação responsiva.
- [ ] `VAL-04` Executar no frontend `npm run test:notas && npm run test:notas:race && npm run lint && npm run build`.
- [ ] `VAL-05` Executar `npm run e2e:notas` contra build/preview local fresco com todas as APIs interceptadas e download capturado.
- [ ] `VAL-06` Executar probes de race `5/10/20` para exportação duplicada/cancelamento, ou incorporar contagem determinística equivalente no runner browser com justificativa.
- [ ] `VAL-07` Rodar capability audits React/Vite/NestJS, auditoria de performance do endpoint, segurança CSV/PII e revisão de acessibilidade.
- [ ] `VAL-08` Rodar validator Foundation, guards de diff/autoridade/conclusão e `git diff --check`.

## Completion Evidence Matrix

| Criterion ID | Criterion | Evidence Type | Planned Evidence | Status |
| --- | --- | --- | --- | --- |
| `DOD-01..04` | UX, tema, menu, navegação e paginação | `browser+accessibility` | `frontend/e2e/notas.mjs` em desktop/mobile | `planned` |
| `DOD-05..08` | export completo, seguro e bounded | `backend contract+unit+browser` | specs fiscal + download interceptado | `planned` |
| `DOD-09` | duplicate/cancel safety | `race+browser` | bursts e contagem exata | `planned` |
| `DOD-10` | gates e docs | `command+review+validator` | matrizes abaixo | `planned` |
| `VAL-01..08` | comandos/guardas previstos | `command` | saídas e artefatos vinculados no closeout | `planned` |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas | fonte paginada real | `contract-known; quota unknown` | `2026-09-28` | discovery + adapter atual | testes usam port stub; smoke real permanece cutover |
| Chromium local | validação visível/download | `previously healthy` | `2026-09-27` | runner Playwright existente | preflight antes do e2e |
| Logo anexada | ativo oficial | `healthy` | `2026-09-28` | inspeção do JPEG 500x500 | copiar bytes sem transformação visual |

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `react,vite,nestjs`
- **Expected supporting profiles:** `assurance-tester-quality`; `assurance-security-adversarial` recomendado para CSV/endpoint.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-tester-quality` | contrato público e jornada crítica | backend/frontend/tests | `planned after implementation` |
| `operational-coder` | `assurance-security-adversarial` | CSV injection, PII e download autenticado | export endpoint/client | `planned/recommended` |
| `operational-coder` | `operational-devops` | promoção/deploy fora do escopo | cutover | `deferred to existing cutover TODO` |

## Complexity

- **Level (`small|medium|big`):** `medium`
- **Checkpoint policy:** `one frozen planning checkpoint; one implementation checkpoint before delivery reviews`
- **Why this level:** há mudança pública NestJS, paginação upstream bounded, fluxo assíncrono de download e vários limites React, mas sem banco, mutation ou deploy.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `foundation_documentation/modules/identity-and-team.md`; `foundation_documentation/modules/events-and-classification.md`
- **Planned decision promotion targets:** `fiscal-notes-and-documents#Purpose, Owned Entities, and Workflows`; `#Invariants`
- **Module decision consolidation targets:** contrato de exportação e UX/navegação estável em `fiscal-notes-and-documents.md`.

## Decision Pending

- [x] `none — formato, escopo do filtro e contexto foram resolvidos neste baseline`.

## Decisions

- [x] `D-01` “Geral” é o nome da tela; exportação usa somente o `FiscalIssuerContext` selecionado, Unifast ou Prosperar, sem agregado.
- [x] `D-02` Exportação cobre todo o filtro aplicado, não somente a página visível; `pagina` não é aceito no endpoint de exportação.
- [x] `D-03` Limite de 20.000 registros é fail-closed: `total > 20.000` retorna erro antes do CSV e pede filtro menor; truncamento é proibido.
- [x] `D-04` A exportação faz primeira página para conhecer total/shape e busca páginas restantes sequencialmente; cada página mantém timeout/abort/bounds do adapter; qualquer erro invalida o arquivo inteiro.
- [x] `D-05` O serviço monta o CSV somente após todas as páginas válidas estarem disponíveis, mantendo memória limitada pelo teto de 20.000; list/detail preservam o atual one-call invariant.
- [x] `D-06` Colunas: `contextoFiscal;numeroFiscal;status;produto;idCompra;chaveAcesso;ambiente;modelo;finalidade;plataforma;emissaoAgendada;dataPagamento;competencia;valorUnitario;valorTotal`.
- [x] `D-07` Todo valor textual externo recebe neutralização de fórmula antes de quote/escape; não exportar `noteId`, `idInterno`, PII do destinatário, token, CNPJ configurado ou payload cru.
- [x] `D-08` Contexto/status/datas continuam autoaplicados; Documento/ID da compra dependem de `Aplicar filtros`; refresh manual é removido.
- [x] `D-09` Menu de configurações existe para todos os usuários; mostra nome/e-mail/perfil; `Equipe` é condicional a ADMIN; tema, senha e sair permanecem disponíveis conforme sessão.
- [x] `D-10` `Processamento das notas` é somente um novo rótulo/destino visível para a rota PostgreSQL existente; nenhum contrato de logs muda.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `fiscal-notes-and-documents#Invariants` | um contexto por request; sem agregado ou payload bruto | `Preserve` | módulo fiscal |
| `fiscal-notes-and-documents#Purpose` | Smart Notas é fonte de lista/detalhe | `Preserve and extend with export` | módulo fiscal |
| `identity-and-team#Observed Authentication Contract` | conta/perfil vêm da sessão JWT | `Preserve` | módulo identity |
| `events-and-classification#Observed API Contract` | `/eventos` é projeção PostgreSQL separada | `Preserve` | módulo events |
| `completed backend TODO DOD-11` | list/detail fazem no máximo uma chamada provider | `Preserve for list/detail; intentionally extend only export` | TODO histórico + specs |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-10` constituem o baseline material preparado para review; implementação permanece bloqueada até crítica/arquitetura/coherence/drift, `preflight-go` e `APROVADO`.

## Architecture Change Governance

- **Applicability (`required|not_needed`):** `required`
- **Why this applies:** o TODO estabelece um endpoint fiscal público e uma exceção explícita, limitada à exportação, ao comportamento de uma chamada upstream por request.
- **Deviation / debt being retired:** exportar no cliente por page-walk sujeito a rate limit/arquivo parcial; refresh manual redundante e navegação de sessão dispersa.
- **Target steady-state after closeout:** backend é o único owner da paginação/export CSV; frontend inicia um download autenticado; list/detail permanecem single-page; contextos nunca agregam.
- **Temporary exceptions allowed:** `none`.
- **Cutover / removal condition:** `n/a — contrato novo entra de forma aditiva`.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| thin controller + application provider | NestJS architecture rule | `/notas/exportar` | transporte não deve possuir paginação/CSV |
| single state owner + accessible async CTA | React architecture rule | header/list | evita duplicidade e estado tardio |
| fail-closed complete export | `D-02..D-05` | backend/client | nunca confundir parcial com sucesso |
| one fiscal context | module invariant | API/CSV | impede mistura Unifast/Prosperar |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden | Exception Policy |
| --- | --- | --- | --- |
| frontend caminhar páginas | múltiplos `GET /notas` ao clicar exportar | rate limit/arquivo parcial | none |
| truncar em 20k | CSV 200 com total maior | viola “exportar tudo” | none; retornar erro |
| stream parcial | headers/bytes antes de completar provider | falha intermediária parece sucesso | none neste corte |
| agregar contextos | duas credenciais no mesmo CSV | quebra isolamento fiscal | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| contract test | NestJS | `npm test -- --runInBand` | filtro/paginação/cap/abort/headers | `implement-in-this-todo` | fiscal application/contract specs |
| browser test | React | `npm run e2e:notas` | menu/export/double click/route/theme | `implement-in-this-todo` | intercepted Chromium |
| lint/build | Node | package scripts | hook/render/type/bundle regressions | `already-enforced` | CI matrix |
| security review | CSV | adversarial formula fixtures | planilha executável/PII | `implement-in-this-todo` | specs + review |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `pending frozen baseline`
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`
- **No-go handling:** `return to decision/delivery loop; never claim approval/completion with unresolved divergence`.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** mudança medium/cross-stack/public contract exige review reproduzível.
- **Trigger stage:** `before first planning-side review or guard`
- **Baseline branch:** `uninotas-foundation/main`
- **Baseline commit:** `9c67c9d6521dd4570d186965774195b52a55d9fc`
- **Baseline push reference:** `origin/main@9c67c9d6521dd4570d186965774195b52a55d9fc`
- **Gate status:** `no_material_findings`
- **Findings summary:** `o commit material contém somente este TODO e foi publicado no main canônico da Foundation`.
- **Evidence / reference:** `git diff --cached --name-status` registrou apenas `A todos/active/features/TODO-uninotas-fiscal-workspace-ux-and-export.md`; Git for Windows publicou `db96701..9c67c9d`.
- **Waiver authority / reference:** `n/a`
- **Pre-freeze packet-prep rule:** `all review rows remain prepared-pre-freeze until this gate passes`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** confirmar que reviews não alteraram escopo sem nova validação.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `canonical set from workflow`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-workspace-ux-and-export.md`
- **No-go handling rule:** `reconverge, revalidate with user and refresh baseline`.
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] Exportar página ou filtro inteiro? `Filtro inteiro`, confirmado pelo usuário em 2026-09-28.
- [x] Contexto agregado? `Não`; contexto selecionado Unifast ou Prosperar.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | rota PostgreSQL existente pode ser reutilizada apenas mudando rótulo/link | `App.tsx`, `ListaEventos.tsx` | ampliaria logs scope | `High` | `Keep as Assumption` |
| `A-02` | primeiro page response permite rejeitar `total > 20k` antes de produzir CSV | adapter valida `total/totalPages` | exigiria fila/stream diferente | `High` | `Keep as Assumption` |
| `A-03` | até 20k resumos CSV cabem em memória de forma bounded | campos possuem bounds; teto explícito | precisaria storage/stream | `Medium` | `Promoted to D-05` |
| `A-04` | paginação sequencial respeita melhor quota e semaphore atual | adapter fail-fast em `maxConcurrency`; list page-based | export pode demorar | `High` | `Promoted to D-04` |
| `A-05` | imagem anexada é a marca autorizada | solicitação explícita + inspeção 500x500 | ativo incorreto | `High` | `Keep as Assumption` |

## Execution Plan

### Touched Surfaces

- `backend/src/fiscal-notes/**`, testes e documentação backend.
- `frontend/src/{componentes,paginas,api,hooks,estilos}/**`, ativo público e testes.
- `foundation_documentation/modules/fiscal-notes-and-documents.md` no closeout.

### Ordered Steps

1. Criar testes backend fail-first do contrato `/notas/exportar` e helper CSV seguro.
2. Implementar DTO sem `pagina`, serviço bounded multi-page, CSV e controller thin com headers/no-store/abort.
3. Criar testes frontend/browser fail-first para menu, selects, exportação completa, duplicate click, navegação e layout.
4. Integrar logo oficial, header/menu, link de processamento, filtros sem refresh, botão exportar e paginação central.
5. Executar suites estreitas e amplas; corrigir apenas dentro do contrato.
6. Executar PCV/security/test-quality/final/adherence gates e consolidar módulo/README.

### Test Strategy

- **Strategy:** `test-first` para endpoint/export e jornada visível; CSS visual acompanhado de browser assertions.
- **Why:** comportamento público, assíncrono e de segurança é verificável antes da implementação.
- **Fail-first targets:** 404 da nova rota; ausência do botão/menu/link; dupla exportação; CSV formula/over-limit/abort; contraste/posição computados.

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Why now:** não é bugfix isolado; screenshots e código atual já evidenciam os gaps, e testes novos pertencem à execução aprovada.
- **Target symptom:** `n/a`
- **Allowed surfaces:** `none pre-approval`
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status:** `not_run`
- **Findings summary:** `n/a`.

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane? | Backend Real-Data? | Planned Evidence | N/A Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| theme/select/header/menu | visible/accessibility | `web-only` | `Playwright readonly` | `no` | `no` | intercepted browser desktop/mobile | n/a |
| filters without refresh | query behavior | `web-only` | `Playwright readonly` | `no` | `no` | request count/assertions | n/a |
| full CSV export | API/download | `web-only` | `Playwright readonly + backend contract` | `no` | `no` | multi-page fixture/download content | n/a |
| processing navigation | navigation | `web-only` | `Playwright readonly` | `no` | `no` | existing event fixture | n/a |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Preconditions | Command | Required Before | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend NestJS | public export endpoint | validation, cap, multi-page, failure, abort, CSV | port/fetch deterministic stubs | `cd backend && npm test -- --runInBand && npm run build && npm run lint` | `Local-Implemented` | `planned` | stdout | full backend family |
| frontend React/Vite | UI and adapter | parser/cache unaffected + menu/download/layout | Node deps present | `cd frontend && npm run test:notas && npm run test:notas:race && npm run lint && npm run build` | `Local-Implemented` | `planned` | stdout | full frontend family |
| frontend browser | critical journey | login -> filter -> export -> settings -> processing | fresh local preview; intercepted APIs; local Chromium | `cd frontend && ALVO=<fresh-preview> CHROME=<local> npm run e2e:notas` | `Local-Implemented` | `planned` | runner output | capture download |
| capability audits | architecture | owning manifests/scripts | repo state | `node_capability_surface_audit.py` for nestjs/react/vite | `Local-Implemented` | `planned` | stdout | no manifest mixing |
| Foundation | docs/guards | TODO/module/publication integrity | canonical main checkout | `todo_deterministic_validator.py` + `validate_foundation.py` + TODO guards | `Local-Implemented` | `planned` | stdout | no validator edits |

### Runtime / Rollout Notes

- Nenhuma variável, migration ou serviço novo.
- Endpoint permanece atrás do JWT/perfis leitores e da feature fiscal existente.
- Smoke real/provedor e promoção continuam no cutover; este TODO prova localmente com ports/fixtures determinísticos.

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
  - **Severity:** `medium`
  - **Evidence:** provider não aceita page size; adapter limita `totalPages` a 10.000; rate/concurrency atuais são por request/call.
  - **Why it matters now:** export no cliente ou paginação ilimitada pode falhar parcialmente ou pressionar quota.
  - **Option A (Recommended):** endpoint backend, sequencial, cap 20k fail-closed, buffer bounded e abort.
    - **Effort/Risk/Blast:** `medium/medium/cross-stack`
    - **Maintenance/Performance/Elegance/Structure:** `medium / bounded slower / improves / improves`
  - **Option B:** browser percorre páginas.
    - **Effort/Risk/Blast:** `low/high/frontend`
    - **Maintenance/Performance/Elegance/Structure:** `high / rate-limited / regresses / regresses`
  - **Option C (Do Nothing):** sem exportação.
    - **Effort/Risk/Blast:** `low/high/local`
    - **Maintenance/Performance/Elegance/Structure:** `low / neutral / neutral / neutral`, mas não atende usuário.
  - **Recommendation:** `A`, pois garante arquivo completo ou erro explícito.

- **Issue ID:** `UX-01`
  - **Severity:** `low`
  - **Evidence:** refresh explícito duplicado ao auto-update; links de sessão dispersos no header.
  - **Why it matters now:** confusão e desalinhamento observados pelo usuário.
  - **Option A (Recommended):** remover refresh, menu acessível com estado local e ações existentes.
    - **Effort/Risk/Blast:** `low/low/frontend`
    - **Maintenance/Performance/Elegance/Structure:** `low / improves / improves / improves`
  - **Option B:** manter ações e apenas estilizar.
    - **Effort/Risk/Blast:** `low/medium/frontend`
    - **Maintenance/Performance/Elegance/Structure:** `medium / neutral / regresses / neutral`
  - **Option C:** não mudar.
    - **Effort/Risk/Blast:** `low/medium/local`
    - **Maintenance/Performance/Elegance/Structure:** `low / neutral / regresses / neutral`
  - **Recommendation:** `A`.

### Failure Modes & Edge Cases

- [ ] total muda entre páginas: validar page/total/totalPages e quantidade final; falhar, nunca exportar snapshot incoerente.
- [ ] logout/401/abort durante export: cancelar e não disparar download tardio.
- [ ] fórmula/aspas/quebra de linha: neutralizar e escapar deterministically.
- [ ] clique fora/Escape/foco no menu: fechar sem prender teclado.
- [ ] viewport estreito: menu, filtros e paginação sem overflow.
- [ ] rota `exportar` não pode ser capturada como `:noteId`.

### Residual Unknowns / Risks

- [ ] Quota/latência real do Smart Notas para filtros próximos do teto permanece desconhecida; smoke/capacity real pertence ao cutover.
- [ ] Snapshot do provedor pode mudar durante paginação; contrato falha fechado em metadata/contagem incoerente, mas não há cursor transacional.

## Additional Architectural Opinions

- **Needed:** `no beyond required architecture/critique gates`
- **Why ambiguity remains:** `recommended path is dominant after explicit fail-closed cap; required formal reviews still run`.
- **Opinion count:** `0`
- **Package mode:** `bounded-summary`
- **Internal reviewer mandate:** `not_needed here; architecture_opinion and critique recorded in their canonical sections`.
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-workspace-ux-and-export.md`
- **Latest TEACH evidence / artifact:** `pending audit guard after origin/main@9c67c9d`.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | cross-stack public export + UI |
| `blast_radius` | `cross-stack` | NestJS and React/Vite |
| `behavioral_change_or_bugfix` | `yes` | visible behavior and endpoint |
| `changes_public_contract` | `yes` | new GET export route |
| `touches_auth_or_tenant` | `no` | existing JWT/readers reused; no auth rules change |
| `touches_runtime_or_infra` | `no` | no runtime topology/config |
| `touches_tests` | `yes` | contract/browser/race fixtures |
| `critical_user_journey` | `yes` | fiscal listing/export |
| `release_or_promotion_critical` | `yes` | requested delivery polish before cutover |
| `high_severity_plan_review_issue` | `no` | no unresolved high card |
| `explicit_three_lane_request` | `no` | user did not request triple audit |

## Independent No-Context Critique Gate

- **Critique decision:** `pending audit guard`
- **Why this decision:** medium cross-stack/public contract.
- **Impact signals in scope:** `cross-stack blast radius|public API|critical journey`.
- **Package mode:** `bounded-summary`
- **Package minimum contents:** `frozen baseline|scope|assumptions|plan|issue cards|risks`.
- **Critique isolation mode:** `fresh internal no-context reviewer`.
- **Internal reviewer mandate:** `pending guard; reviewer cannot implement`.
- **Canonical multi-lane audit protocol:** `pending guard`
- **Audit session / round evidence:** `n/a unless required`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** A-01/A-02/A-04/A-05 bind plan to current code/assets.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-04,A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-workspace-ux-and-export.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending explicit APROVADO`
- **Approval scope:** `pending`
- **Execution not authorized by approval:** `deploy, merge, logs semantics, aggregate contexts, worktrees`
- **Renewed approval required when:** `export semantics/cap/columns, source authority, auth, context aggregation, runtime or diff boundary changes materially`.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | tactical work | approval/gates/diff | preapproval code | governs lifecycle |
| `delphi-ai/skills/package-first-verification/SKILL.md` | new export/helper | package query first | duplicate package | no relevant package found |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | UI/hooks/menu | purity/state/a11y/async | effect suppression/stale state | browser/race proof |
| `delphi-ai/skills/wf-react-change-ui-boundary-method/SKILL.md` | React boundaries | explicit states/actions | hidden coupling | component design |
| `delphi-ai/skills/rule-vite-vite-build-runtime-always-on/SKILL.md` | asset/build | local asset/build contract | env/asset guess | build proof |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | new endpoint | thin controller/runtime validation | controller business logic | service-owned export |
| `delphi-ai/skills/wf-nestjs-change-application-boundary-method/SKILL.md` | HTTP boundary | DTO/auth/error/limits | implicit unbounded work | contract tests |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | new tests | fail-first/observable behavior | mock fallback/bypass | coverage matrix |
| `delphi-ai/skills/frontend-race-condition-validation/SKILL.md` | async export/menu | duplicate/cancel policy | double download | bursts/browser |
| `delphi-ai/skills/endpoint-performance-scrutiny/SKILL.md` | multi-page endpoint | bounded-list evidence | unbounded page walk | cap/metrics review |
| `delphi-ai/skills/ci-equivalent-governance/SKILL.md` | delivery suites | full package families | targeted-only claim | backend/frontend matrices |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `pending APROVADO; workflow-required executor delegation after approval`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `pending`
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01..D-10` | `planned` | implementation/tests/docs | complete before delivery |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `fiscal-notes-and-documents#Invariants` | Preserve | `planned` | tests/module | one context |
| `identity-and-team#Observed Authentication Contract` | Preserve | `planned` | browser/auth fixture | no role changes |
| `events-and-classification#Observed API Contract` | Preserve | `planned` | route/browser | no logs changes |

### Exception Handling

- Qualquer `Exception`/`Regression` bloqueia entrega até correção ou renovação de `APROVADO`.

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| bounded implementation diff | API/UI/security/races | `planned` | post-implementation review | pending | pending |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Search Lens | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| React/NestJS/TODO/security | client page-walk, partial CSV, context mix, inaccessible menu, hidden PII | `planned` | post-implementation | pending | pending |

## Promotion Finding Routing Ledger

| Finding ID | Finding Source | Severity | Classification | Required Action | Status | Rationale / Follow-up |
| --- | --- | --- | --- | --- | --- | --- |
| `none-yet` | n/a | n/a | `by-design/no-action` | none | `accepted` | placeholder until reviews |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planejamento aguardando aprovação/execução.
- **Post-commit/push status:** `pending`
- **Next path/status action:** `obtain APROVADO, execute, then decide completed/promotion lane`.

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** endpoint autenticado gera planilha com texto externo e valores fiscais; risco de formula injection/PII/DoS bounded.
- **Attack surface in scope:** `JWT read endpoint, query validation, CSV download, external provider text`.
- **Attack simulation decision:** `pending audit guard; at least recommended`.
- **Review evidence:** `planned adversarial fixtures and security review`.
- **Residual security risk:** `provider text can be adversarial; neutralization and strict allowlist required`.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** export percorre páginas externas e a UI tem CTA assíncrono retriggerable.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Severity | Reason Code | Deadline | Minimum Evidence | State | Residual Risk | Uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `high` | `EPS-DATA-PATH-CHANGED` | `before_local_implemented` | `EPS-E2` | `pending` | provider latency/quota | `U-QUERY-PATH-UNKNOWN` |
| `FRC` | `frontend-race-condition-validation` | `required` | `high` | `FRC-DUPLICATE-MUTATION` | `before_local_implemented` | `FRC-E3` | `pending` | duplicate/cancel | `U-ASYNC-SURFACE-UNKNOWN` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-NON-IDEMPOTENT-WRITE` | `before_local_implemented` | `BCI-INV` | `not_applicable` | none; GET/no write | `none` |
| `RLS` | `runtime-load-stress-validation` | `recommended` | `medium` | `RLS-BATCH-OR-BULK-PATH-CHANGED` | `before_local_implemented` | `RLS-E1` | `pending` | bounded 20k path | `U-RUNTIME-PRESSURE-UNKNOWN` |

### EPS
- **Trigger rationale:** new bounded multi-page external read path.
- **Recorded at (UTC):** `2026-09-28T15:30:00Z`
- **Executor ID:** `pending-routine-executor`
- **Evidence object:** `pending implementation artifact`.

### FRC
- **Trigger rationale:** export CTA can be clicked repeatedly or outlive route/session.
- **Recorded at (UTC):** `2026-09-28T15:30:00Z`
- **Executor ID:** `pending-routine-executor`
- **Evidence object:** `pending browser/race artifact`.

### BCI
- **Trigger rationale:** GET export has no write or irreversible server side effect.
- **Recorded at (UTC):** `2026-09-28T15:30:00Z`
- **Executor ID:** `pending-routine-executor`
- **Evidence object:** `n/a; not_needed`.

### RLS
- **Trigger rationale:** bulk path needs bounded sample/profile evidence but no production SLO claim.
- **Recorded at (UTC):** `2026-09-28T15:30:00Z`
- **Executor ID:** `pending-routine-executor`
- **Evidence object:** `pending deterministic 20k-cap profile artifact`.

## Verification Debt Assessment

- **Audit outcome:** `pending`
- **Why this outcome:** medium cross-stack task.
- **Inline code TODO debt:** `pending`
- **Evidence / audit artifact:** `planned verification-debt-audit`.
- **Accepted residual debt:** `none planned`.

## Independent Test Quality Audit Gate

- **Audit decision:** `pending audit guard`
- **Why this decision:** public contract/tests/critical journey.
- **Trigger signals in scope:** `behavior change|public API|tests|critical journey`.
- **Required evidence matrix:** `unit|integration|browser`.
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** `baseline|diff|tests|evidence|DoD|risks`.
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `pending guard`
- **Gate-satisfying evidence expectation:** `fresh internal audit if required`
- **Audit focus:** `fail-first|assertion efficacy|coverage|bypass`.
- **Required applicable evidence:** `test diff + commands + browser fixture`.
- **Audit status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent No-Context Final Review Gate

- **Final review decision:** `pending audit guard`
- **Why this decision:** cross-stack public behavior.
- **Impact signals in scope:** `public API|critical journey|performance/security`.
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** `baseline|diff|adherence|validation|audit|risks|debt`.
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `pending guard`
- **Canonical multi-lane audit protocol:** `pending guard`
- **Audit session / round evidence:** `n/a unless required`
- **Review focus:** `adherence|regressions|security|performance|elegance|structure`.
- **Final review status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `not_needed`
- **Why this decision:** no cutover/deploy/legacy retirement occurs here.
- **Cutover signals in scope:** `none`.
- **Package mode:** `n/a`
- **Canonical multi-lane audit protocol:** `n/a`
- **Audit session / round evidence:** `n/a`
- **Audit focus:** `n/a`
- **Cutover audit status:** `n/a`
- **Findings summary:** `none`
- **Evidence / reference:** `scope boundary`
- **Waiver authority / reference:** `n/a`

## Delivery Confidence Gate

- [ ] Lane promotion evidence complete: `n/a until requested`.
- [ ] Runtime impact classified: `low; additive GET behind existing flag`.
- [ ] PCV lanes gate-satisfying.
- [ ] Local implementation confidence stated after evidence.
- [ ] Release readiness outcome: `not evaluated in this TODO`.

## Module Consolidation Gate

- [ ] `fiscal-notes-and-documents.md` atualizado com export e UX estáveis.
- [ ] Decisões preservadas/supersedidas rastreadas.
- [ ] Links active/completed atualizados no closeout.

## Commands

- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo . --expect nestjs --manifest backend/package.json`
- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo . --expect react --expect vite --manifest frontend/package.json`
- `cd backend && npm test -- --runInBand && npm run build && npm run lint`
- `cd frontend && npm run test:notas && npm run test:notas:race && npm run lint && npm run build`
- Browser intercepted runner on fresh preview.
- Foundation validator and TODO lifecycle guards.

## Files Expected

- Use `Diff Expectation Contract` as authority.

## COMENTÁRIO:

- “Exportar tudo selecionado dentro do filtro” foi interpretado como todas as páginas do único contexto fiscal ativo; o teto de 20.000 nunca trunca: exige filtro menor quando excedido.
