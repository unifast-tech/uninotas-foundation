# TODO — Evoluir a experiência do workspace fiscal do UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Draft`
- **Created:** `2026-09-28`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário

## Context

A validação visual da primeira versão do UniNotas mostrou selects ilegíveis no tema escuro, controles desalinhados, atualização manual redundante, marca provisória, ações de sessão dispersas e paginação sem respiro. Este TODO entrega somente a correção React/Vite do workspace e sua navegação. A exportação do filtro completo é governada separadamente por `TODO-uninotas-filtered-csv-export.md`.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-workspace-improvements.md`
- **Story:** `ST-UX`
- **Why this is bounded:** ativo, header, filtros, disclosure de configurações e paginação pertencem à mesma composição visual autenticada e não criam contrato backend.

## Contract Boundary

- `Geral` continua sendo a tela Smart Notas de um único contexto fiscal.
- `Processamento das notas` abre a rota PostgreSQL existente `/erros`, disponível a todos os perfis autenticados, sem mudar dados, filtros ou permissões de tratamento.
- O controle de configurações é um disclosure acessível com links/botões normais; não implementa semântica ARIA de menu de aplicação.
- Este TODO não adiciona exportação nem muda API, auth, banco ou deploy.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** congelar/revisar o plano, obter `preflight-go` e solicitar `APROVADO`.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** achados independentes foram incorporados e o baseline revisável ainda será congelado.
- **Exit condition:** aprovação explícita e authority guard pós-aprovação em `go`, ou bloqueio formal.

## Provisional Notes

- **Missing for production-ready:** implementação, testes, evidência browser, auditorias e cutover/deploy separado.
- **Revisit criteria:** mudança de rotas, autorização, fonte PostgreSQL, modelo de sessão ou inclusão da exportação neste pacote.
- **Dependencies unblocked:** a implementação local usa somente React/Vite e a imagem oficial disponível; Chromium será revalidado antes do browser run.

## Blocker Notes

- **Blocked:** `no`.
- **Current blocker:** `none`.
- **Unblock condition:** `n/a`.

## Scope

- [ ] `SCOPE-UX-01` Corrigir select/campo/opções e indicadores de foco para contraste WCAG nos temas claro e escuro.
- [ ] `SCOPE-UX-02` Alinhar controles da barra pela base; manter atualização automática de contexto/status/datas; remover `Atualizar`; manter `Aplicar filtros` somente para Documento e ID da compra.
- [ ] `SCOPE-UX-03` Versionar e usar como ativo local a imagem oficial anexada, preservando fallback textual acessível.
- [ ] `SCOPE-UX-04` Reorganizar o header com marca, `Smart Notas` e `Processamento das notas`; ambos os destinos permanecem disponíveis a todos os usuários autenticados.
- [ ] `SCOPE-UX-05` Substituir o bloco textual de sessão por botão de configurações que mostre conta/perfil e contenha tema, senha, sair e Equipe somente para ADMIN.
- [ ] `SCOPE-UX-06` Centralizar paginação e garantir respiro inferior em desktop e viewport móvel.
- [ ] `SCOPE-UX-07` Atualizar testes frontend/browser e documentação visível diretamente afetada.

## Out of Scope

- Exportação CSV/XLSX ou qualquer mudança backend.
- Alterar a tela `/erros`, suas queries, banco, eventos, tratamento ou atualização em tempo real.
- Alterar autenticação, perfis ou permissão de gestão da equipe.
- Prisma, Docker, Railway, variáveis, deploy, merge ou promoção.
- Nova biblioteca de UI, ícones, tema ou estado.
- Worktrees, checkouts auxiliares e escritores paralelos de produto.

## Execution Lane Tracking (Required)

- **Local implementation branch:** `MonitorNotes:release/uninotas-smart-notas`
- **Foundation authority:** `uninotas-foundation:main`
- **Promotion lane:** `n/a — termina Local-Implemented; deploy fica no cutover`
- **Execution topology:** `principal checkout; single product-code writer`

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Baseline ref | Notes |
| --- | --- | --- |
| `MonitorNotes` | `release/uninotas-smart-notas@a4b5a0eb6ae96291ffe5c6e16f297b64dcd62f29` | preservar `artifacts/**` e gitlink preexistentes |
| `uninotas-foundation` | `main@9cffb901c063ad581d3519f5009814f38f7ec5db` | autoridade canônica antes do split |

### Expected Changed Paths

| Repository | Path glob | Change | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `frontend/public/marca-unifast.jpeg` | `A` | imagem oficial fornecida |
| `MonitorNotes` | `frontend/src/componentes/Cabecalho.tsx` | `M` | marca, navegação e disclosure |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | filtros e paginação |
| `MonitorNotes` | `frontend/src/hooks/useTema.ts` | `M` | somente se necessário para seleção explícita de tema |
| `MonitorNotes` | `frontend/src/estilos/*.css` | `M` | contraste, alinhamento, disclosure e respiro |
| `MonitorNotes` | `frontend/e2e/notas.mjs`, `frontend/e2e/notas-unit.ts` | `M` | comportamento e acessibilidade |
| `MonitorNotes` | `frontend/README.md` | `M` | navegação/validação, se desatualizado |
| `uninotas-foundation` | este TODO e destino completed | `M|D|A` | evidência/closeout |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | navegação/UX estável no closeout |

### Not Expected Changed Paths

| Repository | Path glob | Reason |
| --- | --- | --- |
| `MonitorNotes` | `backend/**`, `backend/prisma/**` | pacote frontend-only |
| `MonitorNotes` | `frontend/src/api/**` | nenhum contrato HTTP novo |
| `MonitorNotes` | `Dockerfile`, `docker-compose.yml`, `.github/**`, `*.env*` | runtime/pipeline/config fora do escopo |
| `MonitorNotes` | `artifacts/**` | estado preexistente do usuário |
| `uninotas-foundation` | `project_constitution.md`, `system_roadmap.md`, `policies/**`, `deterministic/**` | sem mudança estratégica/validator |

## Definition of Done

- [ ] `DOD-UX-01` Selects, opções, bordas e foco são legíveis em claro/escuro: texto normal >= 4.5:1; fronteira e foco >= 3:1.
- [ ] `DOD-UX-02` Filtros e CTA alinham; contexto/status/datas continuam automáticos; Documento/ID dependem de Aplicar; `Atualizar` inexiste.
- [ ] `DOD-UX-03` A imagem anexada aparece como marca oficial local com fallback acessível.
- [ ] `DOD-UX-04` `Smart Notas` abre a última Geral e `Processamento das notas` abre `/erros` para todos os perfis autenticados.
- [ ] `DOD-UX-05` Configurações mostra nome, e-mail e perfil; expõe tema, senha e sair; Equipe somente para ADMIN.
- [ ] `DOD-UX-06` Disclosure possui `aria-expanded`/`aria-controls`, fecha por Escape e clique externo, devolve foco ao gatilho, mantém tab order e não estoura com conta longa/mobile.
- [ ] `DOD-UX-07` Paginação está centralizada, responsiva e com espaço inferior perceptível.
- [ ] `DOD-UX-08` Testes, browser, auditorias e guards passam sem tocar backend/runtime.

## Decisions

- [x] `UX-D-01` Usar disclosure simples contendo conteúdo, links e botões normais; não usar `role=menu`.
- [x] `UX-D-02` O ícone de configurações terá nome acessível; estado aberto/fechado é local ao header.
- [x] `UX-D-03` Escape fecha e devolve foco; clique externo fecha; navegação fecha naturalmente por unmount.
- [x] `UX-D-04` `Processamento das notas` substitui o rótulo genérico `Erros` na navegação principal, preservando `/erros`.
- [x] `UX-D-05` A marca é copiada byte a byte do JPEG fornecido para `frontend/public/marca-unifast.jpeg`; nenhuma geração/alteração visual.
- [x] `UX-D-06` Nenhuma ação manual de refresh permanece na Geral; o cache/revalidation existente não muda.

## Assumptions Preview

| ID | Assumption | Concrete Evidence | If False | Handling |
| --- | --- | --- | --- | --- |
| `UX-A-01` | `/erros` é o destino PostgreSQL existente para todos os autenticados | `frontend/src/App.tsx:21-33`; `frontend/src/App.tsx:36-45` | exige mudança de rota/permissão | renovar aprovação |
| `UX-A-02` | tema atual já possui owner único reutilizável | `frontend/src/hooks/useTema.ts`; `frontend/src/componentes/Cabecalho.tsx:36-73` | exige refatorar contrato de tema | manter dentro do frontend se local |
| `UX-A-03` | atualização automática atual pertence ao contexto/lista | `frontend/src/paginas/ListaNotas.tsx:9-19`; `frontend/src/contextos/NotasFiscaisContexto.tsx` | remoção do botão poderia impedir revalidação | bloquear e revisar |
| `UX-A-04` | imagem anexada é a marca autorizada | JPEG anexado em `/mnt/c/Users/X23/Documents/`; solicitação explícita | ativo incorreto | substituir somente por nova orientação |

## Execution Plan

1. Criar/ajustar testes fail-first para filtros, disclosure, permissões, links e layout.
2. Copiar a imagem oficial como ativo local versionado.
3. Refatorar header/disclosure com foco e ações existentes, sem efeitos de render.
4. Corrigir filtros, contraste e paginação em CSS/ListaNotas.
5. Rodar unit/lint/build e preview browser fresco desktop/mobile.
6. Executar revisão de acessibilidade, aderência, qualidade de teste, final e guards; consolidar módulo somente depois de comportamento estável.

## Validation Steps

- [ ] `VAL-UX-01` `cd frontend && npm run test:notas`
- [ ] `VAL-UX-02` `cd frontend && npm run lint && npm run build`
- [ ] `VAL-UX-03` build fresco; iniciar `npm run preview -- --host 127.0.0.1`; provar bundle servido corresponde ao checkout; executar `ALVO=<preview> CHROME=<local> npm run e2e:notas`; encerrar preview.
- [ ] `VAL-UX-04` Browser em desktop e mobile cobre claro/escuro, foco/teclado/Escape/clique externo, ADMIN e não-ADMIN, conta longa, filtros e paginação.
- [ ] `VAL-UX-05` Capability audits React/Vite, `git diff --check`, validator/guards Foundation.

## Local Verification Matrix

| Surface | Command / Evidence | Status |
| --- | --- | --- |
| React unit contract | `cd frontend && npm run test:notas` | `planned` |
| Static/build | `cd frontend && npm run lint && npm run build` | `planned` |
| Browser | preview fresco + `npm run e2e:notas`, APIs interceptadas, desktop/mobile | `planned` |
| Accessibility | contrast measurements + keyboard/focus assertions | `planned` |
| Foundation | validator, diff/authority/completion guards | `planned` |

Não há pipeline versionada no repositório; estas evidências são `Local Verification`, não alegação de CI-Equivalent.

## Plan Review Gate

### Failure Modes & Edge Cases

- [ ] opção nativa continua branca sobre branco em um dos temas;
- [ ] disclosure prende foco, não fecha ou perde retorno de foco;
- [ ] não-ADMIN vê Equipe ou ADMIN deixa de vê-la;
- [ ] conta longa estoura o header;
- [ ] remover Atualizar interrompe a atualização automática;
- [ ] paginação encosta no viewport ou deixa de ser utilizável em mobile.

### Incorporated Independent Findings

| Finding | Severity | Resolution |
| --- | --- | --- |
| pacote combinava UX global e exportação pública | `high` | split em `ST-UX` e `ST-EXPORT` |
| acessibilidade do menu era vaga | `medium` | disclosure, foco, Escape, clique externo, contraste e overflow congelados |
| comandos eram chamados indevidamente de CI-Equivalent | `high` | matriz renomeada Local Verification e preview lifecycle explicitado |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review status:** `not_run after split`
- **Architecture adherence review:** `required after implementation`
- **Adherence status:** `not_run`
- **No-go handling:** `retornar ao plano; não aprovar/concluir com finding material aberto`.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Baseline branch:** `uninotas-foundation/main`
- **Baseline commit:** `1ced35fc4ece74ee472ec6696d6f0f1e8e5e60e0`
- **Baseline push reference:** `origin/main@1ced35fc4ece74ee472ec6696d6f0f1e8e5e60e0`
- **Gate status:** `no_material_findings`
- **Findings summary:** o split material e este contrato UX foram publicados no main canônico.
- **Evidence / reference:** commit `1ced35fc4ece74ee472ec6696d6f0f1e8e5e60e0`, push confirmado em 2026-09-28.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-workspace-ux.md`
- **Gate status:** `not_run`

## Audit Trigger Matrix

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | header global + accessibility + browser |
| `blast_radius` | `cross-module` | rotas autenticadas compartilham header |
| `behavioral_change_or_bugfix` | `yes` | UX visível |
| `changes_public_contract` | `no` | sem API |
| `touches_auth_or_tenant` | `no` | apenas visibilidade existente por perfil |
| `touches_runtime_or_infra` | `no` | n/a |
| `touches_tests` | `yes` | unit/browser |
| `critical_user_journey` | `yes` | navegação fiscal |
| `release_or_promotion_critical` | `yes` | entrega solicitada |
| `high_severity_plan_review_issue` | `no` | findings integrados |
| `explicit_three_lane_request` | `no` | n/a |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Critique status:** `not_run`
- **Isolation:** `fresh internal no-context reviewer; cannot implement`
- **Lenses:** `correctness|accessibility|elegance|structure|regression`.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Guard scope:** `UX-A-01,UX-A-02,UX-A-03,UX-A-04`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-workspace-ux.md`
- **Gate status:** `not_run`

## Approval

- **Approved by:** `pending explicit APROVADO`
- **Approval scope:** `SCOPE-UX-01..07`
- **Not authorized:** `export/backend/deploy/merge/worktrees`
- **Renewed approval required:** rota, auth, fonte ou diff boundary material muda.

## Agent Routing Preflight

- **Client surface:** `codex`
- **Governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Subagent authorization:** `pending APROVADO; workflow-required serialized executor`
- **Execution topology:** `primary-checkout-single-writer`
- **Guard outcome:** `pending`

## Performance & Concurrency Risk Assessment

- **Global sensitivity:** `low`
- **EPS:** `not_needed — no endpoint/data path change`
- **FRC:** `not_needed — disclosure has synchronous local state; browser lifecycle assertions still required`
- **BCI:** `not_needed — no backend/write`
- **RLS:** `not_needed — no bulk/runtime path`

## Required Delivery Gates

- `test-quality-audit`: `required`
- `architecture-adherence`: `required`
- `independent-final-review`: `required`
- `audit-protocol-triple-review`: `required before Completed per escalation outcome`
- `verification-debt-audit`: `required`
- `security-adversarial-review`: `not_needed; no new data/auth boundary`
- `cutover-integrity-audit`: `not_needed`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** aguardando baseline, reviews e aprovação.
- **Target after implementation:** `Local-Implemented`, sem deploy.
