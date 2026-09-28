# Exibir tomador, identificadores e dados completos da nota

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`

## Context

A equipe financeira precisa identificar rapidamente quem é o tomador de cada nota, copiar os identificadores operacionais completos diretamente da Geral e consultar no card de detalhe todos os campos enumerados do `GET /notas`. Os payloads reais redigidos de listagem e detalhe do Smart Notas contêm esses campos; o produto já normaliza parte deles, mas hoje exclui o identificador interno e os dados pessoais/localização, mascara identificadores e apresenta apenas um subconjunto no detalhe. Os valores reais fornecidos na solicitação são evidência transitória e não podem ser copiados para código, documentação, fixtures, logs ou artifacts.

## Framing Source & Story Slice
- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `n/a`
- **Why this is the right current slice:** é uma única evolução da capacidade de identificação visual de notas na Geral e no detalhe, ainda que atravesse o contrato NestJS e a apresentação React.
- **Direct-to-TODO rationale:** o pedido possui uma tela principal, um objetivo de usuário e uma conversa de aprovação; não exige decomposição adicional.

## Contract Boundary
- Este TODO define **WHAT** deve ser entregue e o que conta como pronto.
- A implementação somente começa após congelamento/revisão do contrato e resposta explícita `APROVADO`.
- Descoberta que amplie fonte de dados, persistência local, infraestrutura, autorização ou campos pessoais exige atualização e nova aprovação.

## Implementation Intent
- **Current delivery:** ampliar o resumo fiscal com nome do tomador, exibir nome/compra/chave completos na Geral e apresentar no detalhe todos os campos allowlisted do `GET /notas`, inclusive referência interna Smart Notas, documento, e-mail e localização.
- **Planned next steps:** atualizar o feature brief e o módulo fiscal com as decisões estáveis após aprovação; implementar e validar backend/frontend no checkout principal.
- **Anticipatory implementation authorized now:** `none`
- **Rationale:** o DTO normalizado continua sendo o único limite entre Smart Notas e navegador; nenhum payload bruto ou credencial atravessa a API do UniNotas.

## Delivery Status Canon (Required)
- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** refinar e congelar o escopo expandido explicitamente pelo usuário, repetir reviews/guards e solicitar `APROVADO`.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** `implementation`
- **Why this state now:** a solicitação atual validou e ampliou o card de detalhe; o contrato está novamente em preparação pré-aprovação.
- **Exit condition:** baseline/reviews/guards do escopo expandido convergem e a implementação aprovada é concluída.

## Execution Lane Tracking (Required)
- **Local implementation branches:** `MonitorNotes:release/uninotas-smart-notas`; `uninotas-foundation:main`
- **Promotion lane path:** `release/uninotas-smart-notas -> main` por PR já planejado para a entrega local consolidada
- **Lane-promoted threshold for this TODO:** `main`
- **Production-ready threshold for this TODO:** `Railway stage` após o cutover governante

## Scope
- [ ] `SCOPE-01` Mapear `nome` para `recipientName: string|null`, sempre presente no resumo e detalhe, com limite de 255 caracteres.
- [ ] `SCOPE-02` Exibir na Geral uma coluna `Tomador` com o nome completo ou `Não disponível`, mantendo tabela acessível e responsiva.
- [ ] `SCOPE-03` Exibir `purchaseId`, `accessKey` e `referencedAccessKey` integralmente na área fiscal autenticada, com quebra/cópia visual segura, removendo apenas a máscara de apresentação.
- [ ] `SCOPE-04` Preservar os filtros, paginação, cache, atualização e exportação existentes sem alterar sua semântica.
- [ ] `SCOPE-05` Cobrir contrato NestJS, normalização React, estados ausentes e jornada browser da Geral/detalhe.
- [ ] `SCOPE-06` Atualizar módulo fiscal, feature brief e contratos operacionais estáveis sem registrar valores reais de PII ou identificadores fiscais.
- [ ] `SCOPE-07` Substituir o tipo público baseado em `Omit<FiscalNoteRecord,...>` por uma allowlist positiva explícita, impedindo que futuros campos internos sejam publicados automaticamente.
- [ ] `SCOPE-08` Preservar a linha inteira como link por meio de lista semântica de cartões rotulados: colunas visuais no desktop e rótulos por célula no mobile/leitor de tela, sem ARIA de tabela incompleta.
- [ ] `SCOPE-09` Remover helpers/re-exports de máscara que ficarem sem consumidores e manter canários de privacidade separados por sink.
- [ ] `SCOPE-10` Ampliar somente o DTO público de detalhe com `providerInternalId`, `recipientDocument`, `recipientEmail`, `recipientCity`, `recipientState` e `recipientCountry`, mantendo o resumo de lista limitado a `recipientName` como nova PII.
- [ ] `SCOPE-11` Mostrar no card de detalhe todos os campos do `GET /notas` enumerados pelo usuário: ID interno, modelo, finalidade, status, ambiente, número, chave, compra, produto, valor unitário, valor total, emissão agendada, pagamento, competência, nome, documento, e-mail, cidade, estado, país e plataforma; preservar também os campos de detalhe já existentes.
- [ ] `SCOPE-12` Manter `noteId` opaco como única identidade de rota. `providerInternalId` é somente referência visível autenticada e nunca parâmetro aceito do consumidor.

## Out of Scope
- [ ] Alterar perfis, autenticação ou conceder acesso a usuários não autenticados.
- [ ] Expor telefone, CEP, rua, número, bairro, complemento, inscrições, retorno bruto ou qualquer campo pessoal não enumerado.
- [ ] Persistir notas/PII em Prisma, PostgreSQL, arquivo, `localStorage`, `sessionStorage` ou IndexedDB.
- [ ] Alterar emissão, cancelamento, PDF/DANFE, XML, Routerfy/n8n, Railway ou deploy.
- [ ] Criar lista agregada Unifast + Prosperar.
- [ ] Criar filtro por número da nota, varrer páginas do provedor ou criar projeção/índice fiscal local.
- [ ] Adicionar o nome do tomador ao CSV existente.
- [ ] Adicionar documento, e-mail, localização ou ID interno ao CSV ou à resposta pública da lista.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** DTO/campo normalizado, adapter, Geral/detalhe, CSS e testes diretamente necessários ao mesmo objetivo.
- **Must update or split the TODO:** novo filtro, índice/projeção fiscal persistente, worker/sincronização, novo endpoint externo, mudança de perfis, nova fonte ou ampliação do CSV.

## Definition of Done
- [ ] `DOD-01` A Geral mostra o nome do tomador para registros que o Smart Notas devolve com `nome`, sem consultar PostgreSQL.
- [ ] `DOD-02` Compra e chaves são mostradas completas somente dentro das rotas autenticadas existentes e continuam ausentes de logs, URLs e armazenamento persistente.
- [ ] `DOD-03` O resumo público contém somente `recipientName` como nova PII; o detalhe contém somente os seis novos campos allowlisted e os campos fiscais já aprovados; todo campo pessoal não enumerado continua excluído.
- [ ] `DOD-04` Filtros, paginação, cache e exportação mantêm a semântica atual sem regressão.
- [ ] `DOD-05` A tabela permanece utilizável em desktop e mobile, incluindo valores longos de compra/chave e nome ausente.
- [ ] `DOD-06` Testes e documentação provam a ampliação deliberada de PII/identificadores sem persistir exemplos reais.
- [ ] `DOD-07` `recipientName` é sempre serializado como string normalizada ou `null`; campo presente vazio, somente espaços ou acima de 255 caracteres falha como `SmartNotasContratoInvalido`.
- [ ] `DOD-08` Testes provam acesso dos quatro perfis atuais, rejeição sem autenticação, exclusão de PII extra/CSV e limpeza do cache enriquecido no logout/disposal.
- [ ] `DOD-09` O normalizador frontend rejeita `recipientName` ausente, tipo inválido, string vazia ou acima de 255; aceita somente `null` ou string válida em lista e detalhe.
- [ ] `DOD-10` Desktop e viewport de 390 px provam nome de 255 caracteres, compra/chave/chave referenciada longas sem truncamento ou overflow, rótulos semânticos, link de linha acessível por teclado e texto copiável.
- [ ] `DOD-11` Canários `allowed-visible-but-forbidden-in-sinks` são visíveis somente na UI fiscal e permanecem ausentes de URL, storage, console, referrer e requests alheios; PII não aprovada permanece `forbidden-everywhere`.
- [ ] `DOD-12` Cache/logout usa canários distintos por sessão e resposta tardia para provar que objetos enriquecidos antigos não reaparecem antes nem depois da resposta da nova sessão.
- [ ] `DOD-13` O card apresenta todos os 21 campos enumerados pelo usuário e preserva os campos de detalhe existentes, com `Não disponível` para valores legitimamente nulos e rótulos fiscais claros.
- [ ] `DOD-14` `providerInternalId` é visível/copiável apenas no detalhe autenticado; a rota, cache key, list response e CSV continuam usando/expondo somente contratos já aprovados e nunca aceitam esse ID do navegador.
- [ ] `DOD-15` Documento aceita somente 11 ou 14 dígitos; e-mail é `string|null` de até 320 caracteres; cidade até 255, estado até 64 e país até 128; valores presentes vazios/overbound ou documento inválido falham como contrato Smart Notas inválido.
- [ ] `DOD-16` Nenhum valor real fornecido pelo usuário é persistido; fixtures usam canários sintéticos inequívocos e não reutilizam pessoa, documento, e-mail, chave, compra ou ID do exemplo real.

## Validation Steps
- [ ] `VAL-01` Executar testes unitários/contratuais do adapter, DTO, serviço e controller fiscal com fixtures sintéticas.
- [ ] `VAL-02` Executar `cd backend && npm test -- --runInBand && npm run build && npm run lint` no runner proprietário do projeto.
- [ ] `VAL-03` Executar `cd frontend && npm run test:notas && npm run test:notas:race && npm run build && npm run lint` no runner proprietário do projeto.
- [ ] `VAL-04` Executar `cd frontend && npm run e2e:notas` contra bundle fresco, cobrindo nome, valores completos, paginação e exportação sem regressão.
- [ ] `VAL-05` Executar revisão de segurança sobre PII, identificadores, logs, URL, cache, logout e respostas de erro.
- [ ] `VAL-06` Executar matriz explícita `ADMIN|GESTOR|ANALISTA|LEITOR|não autenticado`, resposta HTTP allowlisted, CSV sem nome e cache limpo após logout.
- [ ] `VAL-07` Executar browser desktop e 390 px em Geral e detalhe, verificando `scrollWidth`, conteúdo exato não truncado, labels/semântica, teclado e ausência dos canários nos sinks proibidos.
- [ ] `VAL-08` Executar teste unitário/race de cache com valores enriquecidos old-session, resposta tardia e valores distintos new-session.
- [ ] `VAL-09` Executar contract/browser matrix que conta e verifica os 21 campos solicitados no detalhe, ausência desses novos campos sensíveis na lista/CSV e preservação dos campos de detalhe anteriores.
- [ ] `VAL-10` Executar scan/revisão do diff e artifacts para garantir que nenhum valor real fornecido na solicitação foi copiado ou persistido.

## Diff Expectation Contract (Required Before Delivery)
- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `release/uninotas-smart-notas@8a0dba94a39da67fdd9979563beabb364371968a` | `working_tree` |
| `uninotas-foundation` | `foundation_documentation` | `main@c4056a9726eebd857f6288049b3ca7cfd08384f9` | `working_tree` |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M|A` | contrato, adapter, serviço e testes fiscais |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | DTO público do cliente |
| `MonitorNotes` | `frontend/src/notas/**` | `M` | normalização e testes |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | filtro e coluna do tomador/identificadores |
| `MonitorNotes` | `frontend/src/paginas/DetalheNota.tsx` | `M` | tomador e identificadores completos |
| `MonitorNotes` | `frontend/src/estilos/**` | `M` | tabela responsiva e valores longos |
| `MonitorNotes` | `frontend/e2e/**` | `M` | jornada browser |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | decisões estáveis |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-workspace-improvements.md` | `M` | terceira story e estado |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-visibility.md` | `A|M|D` | contrato e closeout |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/**` | `any` | nenhuma persistência ou migração |
| `MonitorNotes` | `backend/src/logs/**` | `any` | PostgreSQL não participa da lista fiscal |
| `MonitorNotes` | `.env*` | `any` | nenhum segredo/config novo |
| `MonitorNotes` | `Dockerfile` | `any` | runtime fora do escopo |
| `MonitorNotes` | `artifacts/**` | `any` | artefatos locais preexistentes não pertencem ao TODO |

## Package-First Assessment
- **Queries executed:** `bash delphi-ai/tools/query_packages.sh --project-root . --search "fiscal"`; `--search "export"`.
- **Relevant packages found:** nenhum.
- **READMEs read:** `n/a`.
- **Decision:** implementação host-local nos módulos fiscal NestJS/React existentes; nenhum pacote novo.
- **Tier:** `Local`.
- **Rationale:** alteração específica do contrato Smart Notas e da tela Geral, sem utilitário reutilizável novo.

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `react,vite,nestjs,cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality,assurance-security-adversarial`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-tester-quality` | contrato público e jornada visível | backend/frontend/tests | `planned` |
| `operational-coder` | `assurance-security-adversarial` | nova PII e identificadores completos | DTO/cache/log/UI | `planned` |

## Complexity
- **Level:** `medium`
- **Checkpoint policy:** `one checkpoint`
- **Why this level:** mudança coesa, porém cross-stack, pública, visível e sensível a PII e identificadores fiscais.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `none`
- **Planned decision promotion targets:** `Canonical Decision Register`, `Purpose, Owned Entities, and Workflows`, `API Endpoint Definitions`, `Invariants`.
- **Module decision consolidation targets:** decisões de visibilidade/autorização e DTO do tomador.

## Decision Pending (Resolve Before Freeze)
- [x] Nenhuma decisão material permanece pendente.

## Decisions (Resolved Before Freeze)
- [x] `D-01` `nome` do Smart Notas será exposto como `recipientName` e apresentado como `Tomador` no resumo e detalhe.
- [x] `D-02` Todos os perfis autenticados atuais (`ADMIN|GESTOR|ANALISTA|LEITOR`) pertencem à equipe financeira e podem ver no detalhe todos os campos enumerados, além de nome, compra e chaves completos na Geral.
- [x] `D-03` Documento e compra continuam efêmeros e aplicados explicitamente; contexto/status/datas continuam automáticos.
- [x] `D-04` O filtro por número foi cancelado pelo usuário em 2026-09-28 e está fora do escopo; nenhuma varredura de páginas, filtro local parcial ou projeção persistente será criada.
- [x] `D-05` A exportação existente já contém compra/chave completas e não ganha automaticamente o nome do tomador; ampliar o CSV com PII exige pedido/decisão separado.
- [x] `D-06` Nome/compra/chaves não entram em URL, logs, telemetria ou armazenamento persistente; o cache continua apenas em memória e é limpo com a sessão.
- [x] `D-07` O contrato público usa allowlist positiva e não deriva sua superfície de todos os campos de `FiscalNoteRecord` por `Omit`.
- [x] `D-08` `recipientName` é sempre presente como `string|null`; `nome` ausente/null vira `null`, enquanto presente vazio, somente espaços ou acima de 255 caracteres invalida o contrato do provedor.
- [x] `D-09` A autorização existente é preservada e provada para os quatro perfis leitores; o acesso sem JWT continua rejeitado.
- [x] `D-10` O cliente trata `recipientName` como campo público obrigatório e estrito: apenas `null` ou string não vazia de até 255 caracteres; qualquer ausência/tipo/valor inválido falha como resposta incompatível.
- [x] `D-11` A Geral preserva o link de linha usando lista semântica de cartões/células rotuladas, com cabeçalho visual desktop e rótulos acessíveis/mobile, evitando ARIA de tabela incompleta.
- [x] `D-12` Valores autorizados visíveis e PII proibida usam conjuntos de canários separados para que remover a máscara nunca enfraqueça provas de URL/storage/log/request/referrer.
- [x] `D-13` Limpeza de cache/sessão é provada com valores enriquecidos distintos e resposta antiga tardia, não apenas com página vazia ou segunda resposta idêntica.
- [x] `D-14` O detalhe público acrescenta somente `providerInternalId`, `recipientDocument`, `recipientEmail`, `recipientCity`, `recipientState` e `recipientCountry`; telefone/endereço completo/inscrições/retorno bruto permanecem privados.
- [x] `D-15` `providerInternalId` pode ser mostrado como referência financeira, mas `noteId` opaco continua sendo a única identidade de rota e nenhuma chamada aceita ID interno informado pelo cliente.
- [x] `D-16` Os campos adicionais de detalhe não entram na lista, CSV, URL, logs, telemetria ou armazenamento persistente; ficam somente na resposta/cache efêmero autenticado do detalhe.
- [x] `D-17` Documento usa validação 11/14 dígitos; e-mail/localização usam limites explícitos e valores presentes inválidos falham fechados no adapter/normalizador.
- [x] `D-18` Os valores reais da solicitação são dados sensíveis transitórios e são proibidos em qualquer arquivo ou artifact persistido.

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `FISC-EX-01` | exporta todos os filtros aplicados | `Preserve` | módulo `Canonical Decision Register` |
| `FISC-EX-08` | compra/chave brutas permitidas no CSV; PII excluída | `Preserve` | módulo `CSV schema` |
| fiscal read DTO | DTO atual exclui toda PII do tomador e o ID interno do provedor | `Supersede (Intentional)` | módulo `Purpose, Owned Entities, and Workflows` |
| provider-supported search | primeiro contrato expõe somente filtros do provedor | `Preserve`; número permanece fora do escopo | discovery `Complete Capability Matrix > Search` |

## Decision Baseline (Frozen Before Implementation)
- [x] `D-01` Expor `recipientName` no resumo/detalhe e os seis campos adicionais somente no detalhe autenticado.
- [x] `D-02` Mostrar todos os campos enumerados do `GET /notas` no card para os leitores autenticados atuais.
- [x] `D-03` Manter campos sensíveis efêmeros, fora da URL/persistência/logs.
- [x] `D-04` Não implementar filtro por número neste TODO.
- [x] `D-05` Não ampliar o CSV com nome do tomador neste TODO.
- [x] `D-06` Preservar filtros, cache, paginação e exportação existentes.
- [x] `D-07` Usar allowlist pública positiva e `recipientName: string|null` com limite 255.
- [x] `D-08` Provar os quatro perfis, rejeição sem autenticação, exclusão do CSV e limpeza de cache.
- [x] `D-09` Usar normalização frontend estrita, lista semântica rotulada e testes desktop/mobile/sinks/sessão com canários distintos.
- [x] `D-10` Remover helpers/re-exports de masking sem consumidores; não manter código morto da política anterior.
- [x] `D-11` Manter `noteId` opaco como rota e `providerInternalId` apenas como referência visível/copiável no detalhe.
- [x] `D-12` Proibir novos campos sensíveis na lista/CSV/sinks e proibir persistência dos valores reais da solicitação.

## Architecture Change Governance
- **Applicability:** `required`
- **Why this applies:** o TODO amplia intencionalmente o contrato de privacidade que antes excluía toda PII do tomador e o ID interno do provedor.
- **Deviation / debt being retired:** máscara visual deixou de atender à necessidade da equipe financeira; nenhuma dívida de origem de dados será resolvida por fallback.
- **Target steady-state after closeout:** resumo allowlisted expõe nome e identificadores fiscais já existentes; detalhe allowlisted expõe todos os campos enumerados pelo usuário, com PII/localização minimizada à lista explícita; rota continua opaca e pesquisa limitada aos filtros do provedor.
- **Temporary exceptions allowed:** `none`.
- **Cutover / removal condition:** `n/a`.

### Patterns To Enforce
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| DTO allowlist | NestJS fiscal adapter | provider -> API | impede vazamento de payload/PII não aprovado |
| ephemeral sensitive filters | módulo fiscal `Invariants` | React cache/query | evita URL/storage/log exposure |
| provider-supported filter boundary | `D-04` | list/export | impede filtro parcial ou varredura dispendiosa |
| opaque route identity | `D-15` | detail route | permite referência visível sem transformar ID do provedor em autoridade de entrada |

### Anti-Patterns To Prohibit
| Anti-Pattern | Prohibited Surface | Protection Harness |
| --- | --- | --- |
| espalhar payload bruto do Smart Notas | adapter/DTO/frontend | contract tests e normalização allowlisted |
| introduzir pesquisa por número disfarçada | React/adapter | diff review e contract tests dos filtros permitidos |
| persistir nome/chaves/compra | URL/browser/db/logs | testes de URL/cache/logout e security review |
| remover canário global para fazer E2E passar | browser tests | separar visibilidade permitida de sinks proibidos e manter ambas as asserções |
| aceitar campo público ausente como `null` | frontend normalizer | contract tests strict list/detail |
| espalhar PII de detalhe para resumo/CSV | service/serializer | exact-key list/detail tests plus golden CSV |
| usar exemplo real como fixture | tests/docs/artifacts | privacy scan and manual diff review |

### Architecture Protection Harness
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| `test` | Smart Notas adapter/DTO | `backend/src/fiscal-notes/smart-notas.adapter.spec.ts`; backend full suite | PII não aprovada atravessando a allowlist ou campos de detalhe vazando para lista/CSV | `implement-in-this-todo` | `DOD-03`, `DOD-13`..`DOD-15`, `VAL-01`, `VAL-02`, `VAL-09` |
| `test` | React normalization/UI | frontend fiscal tests + `npm run e2e:notas` | nome ausente quebrando UI ou identificadores ainda mascarados | `implement-in-this-todo` | `DOD-01`, `DOD-02`, `DOD-05`, `VAL-03`, `VAL-04` |
| `audit` | contrato de privacidade | `security-adversarial-review` | PII/IDs em URL, storage, logs ou erro | `implement-in-this-todo` | `DOD-06`, `VAL-05` |
| `test` | browser privacy/cache/accessibility | `frontend/e2e/notas.mjs`; `frontend/e2e/notas-unit.ts` | canário autorizado escapando para sinks, cache antigo reaparecendo ou labels/overflow inválidos | `implement-in-this-todo` | `DOD-09`..`DOD-12`, `VAL-07`, `VAL-08` |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)
- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** previous reviewer `/root/fiscal_visibility_architecture_opinion` remains historical; new review required because PII/ID scope expanded after that opinion.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending`
- **No-go handling:** `when either required review is absent, blocked, or exposes an unresolved approval-breaking divergence, return to the affected diagnosis/decision or delivery-evidence loop; do not claim APROVADO or Completed.`

## Assumptions Preview
| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | `nome` é o nome/razão social do tomador | `todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md`; observed field matrix | label/semantics must be corrected before implementation | `High` | `Promote to Decision` via `D-01` |
| `A-02` | leitores atuais são membros da equipe financeira e podem ver o conjunto completo enumerado no detalhe | user confirmation dated 2026-09-28 plus current request; `frontend/src/paginas/Equipe.tsx` roles | authorization contract must be redesigned | `High` | `Promote to Decision` via `D-02` |
| `A-03` | compra/chave already arrive complete and are masked only in React | `backend/src/fiscal-notes/smart-notas.adapter.ts`; `frontend/src/notas/normalizacaoFiscal.ts`; `frontend/src/paginas/ListaNotas.tsx` | backend/provider contract work would be required | `High` | `Keep as Assumption` |
| `A-04` | Smart Notas não oferece filtro por número | `foundation_documentation/todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md`; `backend/src/fiscal-notes/smart-notas.adapter.ts` forwards only documented provider filters | exclusion remains harmless, but a future TODO may reconsider | `High` | `Keep as Assumption` |
| `A-05` | lista e detalhe do provedor contêm ID interno, documento, e-mail, cidade, estado e país | `foundation_documentation/todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md` observed list/detail field matrices | provider mapping/nullable decisions must be corrected | `High` | `Promote to Decision` via `D-14` |

## Execution Plan
### Touched Surfaces
- `backend/src/fiscal-notes/**`
- `backend/src/fiscal-notes/fiscal-notes.application.spec.ts`
- `backend/src/fiscal-notes/fiscal-notes.export.spec.ts`
- `backend/src/fiscal-notes/fiscal-notes.rls.spec.ts`
- `backend/src/fiscal-notes/__tests__/smart-notas-live.probe.spec.ts`
- `frontend/src/api/notas.ts`
- `frontend/src/notas/normalizacaoFiscal.ts`
- `frontend/src/paginas/ListaNotas.tsx`
- `frontend/src/paginas/DetalheNota.tsx`
- `frontend/src/estilos/**`
- `frontend/e2e/notas.mjs`
- `frontend/e2e/notas-unit.ts`
- canonical fiscal module, feature brief and this TODO

### Ordered Steps
1. Adicionar testes fail-first para resumo/detalhe allowlisted, todos os campos enumerados, normalização frontend estrita, quatro perfis HTTP reais, sinks/canários, cache de sessão e exibição integral.
2. Estender o record interno do adapter com os seis campos novos, criar projeções públicas positivas distintas para resumo e detalhe e manter rota/query/filtros inalterados.
3. Estender tipos/normalização, Geral e card de detalhe React com todos os campos enumerados, mantendo valores legitimamente nulos explícitos.
4. Converter a grade visual em lista semântica de links/células rotuladas, aplicar `min-width: 0`/`overflow-wrap: anywhere` aos valores reais e preservar a jornada existente de filtros/exportação.
5. Executar testes focados, suites completas, browser fresco e segurança.
6. Consolidar módulo/feature brief e executar gates de entrega/closeout.

## Test Strategy
- **Intent:** `critical-user-journey` e `compatibility`.
- **Strategy:** `test-first` para DTO/normalização e regressões visuais; fixtures exclusivamente sintéticas.
- **Why:** a mudança é observável, aditiva no contrato e sensível à privacidade.
- **Fail-first target(s):** provider nome/documento/e-mail/localização ausentes/null/vazios/overbound; documento não 11/14; HTTP fields ausentes/tipo inválido; exact-key summary/detail projections; PII extra descartada; quatro perfis/rejeição sem JWT; card com os 21 campos; CSV exato sem novos campos; route remains opaque; cache old/new-session; desktop/mobile labels/teclado/overflow; preservação dos filtros/exportação existentes.
- **Deliberate exclusions:** nenhum payload real, segredo, CNPJ, nome real ou identificador real será persistido em teste/artifact.

### Pre-APROVADO RED Evidence Capture
- **Decision:** `not_needed`
- **Why now:** não é correção de bug/regressão e o comportamento solicitado está suficientemente definido.
- **Target symptom:** `n/a`
- **Allowed surfaces:** `n/a`
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical project docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status:** `not_run`
- **Findings summary:** `n/a`

## Frontend / Consumer Matrix
| Producer | Consumer | Contract Change | Compatibility / Evidence |
| --- | --- | --- | --- |
| `GET /api/v1/notas` | `ListaNotas` | adiciona somente `recipientName`; filtros permanecem inalterados | exact-key additive DTO + contract/browser tests |
| `GET /api/v1/notas/:noteId` | `DetalheNota` | adiciona `recipientName`, `providerInternalId`, documento, e-mail, cidade, estado e país; mostra todos os campos enumerados | exact-key additive detail DTO + application/browser tests |
| `GET /api/v1/notas/exportar` | export action | nenhum contrato/schema muda; todos os novos campos permanecem ausentes | golden CSV regression tests |

## Flow Evidence Planning Matrix
| Flow | Intended Evidence | Preconditions | Status |
| --- | --- | --- | --- |
| Geral com tomador/IDs completos | `frontend/e2e/notas.mjs` | bundle fresco e API interceptada com fixtures sintéticas | `planned` |
| detalhe com tomador/IDs completos | `frontend/e2e/notas.mjs` | bundle fresco e API interceptada com fixtures sintéticas | `planned` |
| detalhe com todos os 21 campos | `frontend/e2e/notas.mjs` | fixture sintética completa e valores nulos alternativos | `planned` |
| filtro + paginação + exportação sem regressão | unit/race/browser | contratos atuais preservados | `planned` |
| logout/cache enriquecido old/new-session | `frontend/e2e/notas-unit.ts` + browser | canários distintos e resposta tardia controlada | `planned` |
| desktop/390px semantics and long values | browser list/detail | nome 255, purchase/key/reference longos | `planned` |

## Local CI-Equivalent Suite Matrix
| Owner | Command | Scenario Proved | Preconditions | Status |
| --- | --- | --- | --- | --- |
| backend | `npm test -- --runInBand` | adapter/DTO/query/list/export/privacy | runner Node do projeto e fixtures sintéticas | `planned` |
| backend | `npm run build && npm run lint` | tipos/build/estilo | dependências instaladas | `planned` |
| frontend | `npm run test:notas && npm run test:notas:race` | normalização e regressão de cache/filtros/corridas | runner Node do projeto | `planned` |
| frontend | `npm run build && npm run lint` | bundle/tipos/estilo | dependências instaladas | `planned` |
| frontend | `npm run e2e:notas` | jornada visível e responsiva | bundle fresco + Chrome local | `planned` |

## Plan Review Gate

### Review Sections
- [x] Architecture — Smart Notas permanece autoridade; resumo e detalhe possuem allowlists positivas distintas e a rota continua opaca.
- [x] Code Quality — nomes canônicos para seis campos adicionais de detalhe; nenhuma lógica de filtro, busca ou persistência nova.
- [x] Tests — contrato e browser cobrem os 21 campos, valores longos/ausentes, perfis/sinks e preservam lista/CSV/filtros/exportação.
- [x] Performance — nenhuma chamada upstream, varredura, query ou cardinalidade nova.
- [x] Security — PII/ID interno ampliados somente no detalhe autenticado; demais PII e todos os sinks/persistências continuam proibidos.
- [x] Elegance — extensão aditiva do record interno com duas projeções públicas explícitas, sem novo serviço/abstração.
- [x] Structural Soundness — adapter continua sendo o limite de payload, a rota usa `noteId` e o frontend recebe somente DTO normalizado.

### Issue Cards
- **Issue ID:** `SEC-01`
  - **Severity:** `high`
  - **Evidence:** contrato atual exclui PII/ID interno em `modules/fiscal-notes-and-documents.md`; usuário autorizou explicitamente o conjunto enumerado no card financeiro.
  - **Why it matters now:** documento, e-mail, localização e ID do provedor ampliam materialmente o impacto de uma allowlist ou sink incorreto.
  - **Option A (Recommended):** resumo recebe somente `recipientName`; detalhe recebe exatamente os seis campos adicionais nomeados e mantém `noteId` como rota.
    - **Effort:** `low`
    - **Risk:** `medium`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option B (Alternative):** expor todo o payload/tomador e ocultar campos no React.
    - **Effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Option C (Do Nothing):** manter o detalhe atual incompleto.
    - **Effort:** `low`
    - **Risk:** `low`
    - **Blast radius:** `local`
    - **Maintenance burden:** `low`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `neutral`
    - **Structural soundness impact:** `neutral`
  - **Recommendation:** `Option A`, pois atende ao card completo solicitado com minimização por superfície e preserva adapter/rota como trust boundaries.

### Failure Modes & Edge Cases
- [x] `nome` ausente/null: renderizar `Não disponível` sem falhar a página.
- [x] `recipientName` público ausente/tipo inválido/vazio/overbound: falhar normalização em lista e detalhe, sem converter regressão em `null`.
- [x] compra/chave ausentes: manter `Não disponível` em vez de string vazia.
- [x] valores longos: permitir quebra/cópia sem alargar indefinidamente a tabela.
- [x] payload com PII adicional: descartar no adapter/normalizador e provar por teste negativo.
- [x] CSV existente: não adicionar nome e preservar contrato/ordem atual.
- [x] resumo/lista: não vazar documento, e-mail, localização ou ID interno ao ampliar o detalhe.
- [x] rota: nunca aceitar `providerInternalId` do navegador, embora o mostre como referência.
- [x] exemplo real da conversa: nunca copiar para fixtures/docs/artifacts.
- [x] canário visível: continuar proibido em URL/storage/console/request/referrer sem confundir com PII proibida em qualquer superfície.
- [x] logout/resposta tardia: old-session PII/IDs distintos não reaparecem antes ou depois do payload new-session.

### Residual Unknowns / Risks
- [x] Uma conta financeira comprometida verá os dados completos autorizados; risco residual aceito para esta superfície autenticada e revisto no gate de segurança.

## Additional Architectural Opinions
- **Needed:** `yes`
- **Why ambiguity remains:** deterministic architecture review required because this TODO intentionally supersedes the prior no-PII public DTO contract.
- **Opinion count:** `1 completed + 1 fresh rerun required`
- **Package mode:** `bounded-summary`
- **Internal reviewer mandate:** `required; previous reviewer cannot satisfy the expanded scope, so a fresh no-context architecture reviewer is pending`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `/root/fiscal_visibility_architecture_opinion` | `acceptable_with_changes` | low/bounded payload and DOM increase; no calls/query changes | direct adapter -> explicit public DTO -> React is simplest | positive allowlist required instead of public `Omit` | `Integrated` | architecture-opinion final, 2026-09-28 |

### Architecture Opinion Finding Resolution
| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `ARCH-OP-01` | `Challenged` | `useful` | `no` | `none` | `n/a` | discovery already records `nome` in both list and detail; Context/A-01 now cite that evidence explicitly, so no fallback/query expansion is needed |
| `ARCH-OP-02` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `D-07`, `SCOPE-07` and harness require a positive public DTO allowlist instead of `Omit` inheritance |
| `ARCH-OP-03` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `D-08`/`DOD-07` freeze always-present `string|null`, 255 chars and invalid-present behavior |
| `ARCH-OP-04` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `D-09`, `DOD-08`, `VAL-06` establish explicit auth/privacy/cache/CSV matrix |
| `ARCH-OP-05` | `Integrated` | `useful` | `no` | `none` | `n/a` | performance text recognizes small bounded payload/cache/DOM growth, validated through bound and browser tests |

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)
- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-visibility.md`
- **Latest TEACH evidence / artifact:** `Overall outcome: go`; fingerprint `2226291325c9`; architecture decision review and critique required before approval; delivery audits derived as recorded below.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | cross-stack API/UI/privacy change |
| `blast_radius` | `cross-stack` | NestJS producer and React consumers |
| `behavioral_change_or_bugfix` | `yes` | new visible detail fields, tomador in list and unmasked identifiers |
| `changes_public_contract` | `yes` | additive `recipientName` in summary/detail plus six detail-only fields |
| `touches_auth_or_tenant` | `no` | profiles and guards remain unchanged |
| `touches_runtime_or_infra` | `no` | no deploy/runtime/config change |
| `touches_tests` | `yes` | contract/unit/browser fixtures and assertions change |
| `critical_user_journey` | `yes` | finance note identification in Geral/detail |
| `release_or_promotion_critical` | `yes` | requested for the pending delivery package |
| `high_severity_plan_review_issue` | `yes` | SEC-01 is high because detail now exposes document, email, location and provider ID |
| `explicit_three_lane_request` | `no` | user did not request dedicated three-lane protocol |

## Independent No-Context Critique Gate
- **Critique decision:** `required`
- **Why this decision:** medium cross-stack public-contract and privacy change.
- **Impact signals in scope:** `cross-stack blast radius|public contract/api|intentional module supersede`
- **Package mode:** `bounded-summary`
- **Package minimum contents:** `frozen baseline|scope boundary|assumptions|execution plan|SEC-01|security residual`
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; fresh no-context reviewer distinct from the architecture-opinion reviewer and implementing agent`
- **Canonical multi-lane audit protocol:** `audit-protocol-triple-review` (required before Completed; additive, not a substitute for planning critique)
- **Audit session / round evidence:** `delivery-side; pending implementation`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** previous six findings remain integrated, but a fresh critique is required for expanded detail PII/ID scope.
- **Evidence / reference:** historical reviewer `/root/fiscal_visibility_plan_critique`; expanded-scope rerun pending.
- **Waiver authority / reference:** `n/a`

| Finding ID | Resolution | Usefulness | Formalizable | Candidate Rule Level | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `CRIT-01` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `D-11`, SCOPE-08, DOD-10 and VAL-07 freeze semantic linked cards, labels, keyboard and desktop/390px overflow proof |
| `CRIT-02` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `D-12`, DOD-11 and harness split allowed-visible canaries from forbidden-everywhere PII and retain sink assertions |
| `CRIT-03` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `D-13`, DOD-12 and VAL-08 require distinct old/new-session enriched canaries plus delayed response |
| `CRIT-04` | `Integrated` | `useful` | `partial` | `project` | `n/a` | touched surfaces and VAL-06 name `fiscal-notes.application.spec.ts` as the real JWT/profile HTTP boundary |
| `CRIT-05` | `Integrated` | `useful` | `partial` | `project` | `n/a` | `D-10` and DOD-09 make the frontend required field strict for list/detail |
| `CRIT-06` | `Integrated` | `useful` | `no` | `none` | `n/a` | consumer inventory includes export/RLS/live/application/notas-unit fixtures; SCOPE-09/D-10 remove obsolete mask helpers |

## Gate: Assumption Code Coherence
- **Gate decision:** `required`
- **Why this decision:** A-01 through A-03 directly determine the public DTO and presentation change.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03,A-04,A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-visibility.md`
- **Gate status:** `not_run`
- **Findings summary:** new A-05 and expanded A-02 require rerun after fresh reviews.
- **Evidence / reference:** previous coherence guard was green before expanded detail scope; new run pending.
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze
- **Gate decision:** `required`
- **Why this decision:** planning-side reviews must evaluate a committed and pushed scope-bearing contract.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `main`
- **Baseline commit:** `b85d7577270f497ab395f4157450f7cc2bffdc93`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** scope-bearing contract refreshed after architecture-opinion integration; number search remains excluded and the allowlist/null/auth matrix is frozen.
- **Evidence / reference:** authority guards returned `go`; initial freeze `9d389bd`, refreshed scope baseline pushed through `b85d757`.
- **Waiver authority / reference:** `n/a`
- **Pre-freeze packet-prep rule:** `satisfied; no review result predates the freeze`

## Gate: Review Scope Drift
- **Gate decision:** `required`
- **Why this decision:** scope-bearing sections must remain aligned with the frozen no-number-search contract.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-visibility.md`
- **No-go handling rule:** `return to review, revalidate material changes with the user and refresh the pushed baseline`
- **Gate status:** `not_run`
- **Findings summary:** user explicitly revalidated and expanded the scope in the current request; baseline refresh and full rerun are pending.
- **Evidence / reference:** prior `no-go` is superseded by the user's expanded field-list request; no approval authority is inferred.
- **Waiver authority / reference:** `n/a`

## Questions To Close
- [x] Nenhuma pergunta material permanece; o filtro por número foi explicitamente cancelado.

## Rules Acknowledgement / Ingestion
| Rule / Workflow / Skill | Why It Applies | Pre-Approval Status |
| --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | autoridade e gates | `prepared` |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | estado do TODO | `prepared` |
| `delphi-ai/workflows/react/change-ui-boundary-method.md` | Geral/detalhe/filtros | `prepared` |
| `delphi-ai/workflows/nestjs/change-application-boundary-method.md` | DTO/query/serviço | `prepared` |
| `delphi-ai/skills/package-first-verification/SKILL.md` | package-first | `ingested` |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | cobertura cross-stack | `prepared` |
| `delphi-ai/skills/security-adversarial-review/SKILL.md` | PII/identificadores | `prepared` |

## Agent Routing Preflight
- **Status:** `planned`
- **Execution surface:** `product-code`
- **Role:** `operational-coder`
- **Model / effort:** `inherited / implementation-focused`
- **Topology:** `primary-checkout-single-writer`
- **Subagent / delegation authorization:** `not_authorized_for_implementation`
- **Git isolation authorization:** `not_authorized`; worktrees/auxiliary checkouts remain forbidden.

## Approval
- **Status:** `not_requested`
- **Reason:** expanded detail scope requires refreshed baseline, architecture opinion, critique and deterministic guards.
- **Renewed approval trigger:** any additional PII/provider field, persistence, source, role, CSV/list expansion or search semantics.

## Security Risk Assessment
- **Risk level:** `high`
- **Why this risk level:** intentional exposure of document, email, city/state/country, provider ID and full fiscal/order identifiers through an authenticated detail contract.
- **Attack surface in scope:** JWT/profile authorization, distinct summary/detail DTO allowlists, opaque-route boundary, provider payload, browser memory/cache, URL/log/error/telemetry, CSV exclusion and long-value rendering.
- **Attack simulation decision:** `required`
- **Review evidence:** `planned via security-adversarial-review`.
- **Residual security risk:** disclosure remains possible to any compromised authorized finance account; no field-level role reduction was requested.

### Authorization and Privacy Validation Matrix
| Actor / Surface | Expected Outcome | Planned Evidence |
| --- | --- | --- |
| `ADMIN` | list includes only `recipientName`; detail includes exact expanded allowlist and fiscal fields | backend application/contract test |
| `GESTOR` | same authenticated read contracts | backend application/contract test |
| `ANALISTA` | same authenticated read contracts | backend application/contract test |
| `LEITOR` | same authenticated read contracts | backend application/contract test |
| unauthenticated | route rejected before fiscal service/provider call | controller/application test |
| provider payload with extra recipient PII | extra fields absent from serialized HTTP DTO | adapter + contract negative test |
| list response | document/email/location/provider ID absent; only name added | exact-key HTTP/service test |
| CSV export | raw purchase/key preserved; all new PII/provider ID absent | serializer/export regression test |
| detail route | opaque `noteId` required; raw provider ID never accepted as route/query input | application/codec negative test |
| logout/session disposal | enriched in-memory page removed and late render suppressed | frontend cache/race/browser test |
| real values from request | absent from repository/artifacts and command output | diff/privacy scan + manual review |

## Performance & Concurrency Risk Assessment
- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `low`
- **Why this level:** os mesmos registros e chamadas são mantidos; seis strings bounded ampliam apenas o record interno e a resposta/cache/DOM do detalhe (e records transitórios da exportação), sem mudar I/O, query, quota, paginação ou concorrência.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `n/a-query-unchanged` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `n/a-async-unchanged` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `n/a-read-only` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |
| `RLS` | `runtime-load-stress-validation` | `not_needed` | `low` | `n/a-load-shape-unchanged` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |

## TODO Closeout Disposition
- **Disposition:** `keep-active`
- **Disposition reason:** contrato reconvergido e aguardando aprovação/implementação.
- **Post-commit/push status:** `pending`
- **Next path/status action:** completar gates pré-aprovação e solicitar `APROVADO`.

## Commands (Run Locally)
- `bash delphi-ai/tools/query_packages.sh --project-root . --search "fiscal"`
- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo . --expect react --manifest frontend/package.json`
- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo . --expect nestjs --manifest backend/package.json`
- comandos de validação definidos em `Local CI-Equivalent Suite Matrix` após aprovação.
