# TODO — Ativar e promover a leitura Smart Notas do UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Created:** `2026-09-27`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário
- **Origin:** follow-up obrigatório `R3-CUTOVER-01` do TODO `TODO-uninotas-smart-notas-read-backend.md`

## Context

O módulo local `fiscal-notes` entrega a fronteira read-only candidata, mas permanece desabilitado e sem ownership canônico. Este TODO será o owner exclusivo do cutover operacional: provar os dois emissores, calibrar capacidade, habilitar/deployar com rollback e somente então promover a autoridade de leitura de notas da Smart Notas.

## Contract Boundary

- Este arquivo abre o owner executável do cutover prometido; sua criação não autoriza implementação, deploy, segredo, ativação ou promoção.
- A execução exige refinamento, revisão e novo `APROVADO` específico.
- O cutover não pode reintroduzir PostgreSQL `logs` como fonte de sucesso, dual-read silencioso ou cache persistente de notas.

## Delivery Status Canon

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Work state:** `planning`
- **Next exact step:** refinar o plano de ativação contra a implementação backend validada, congelar rollback/observabilidade e submeter este TODO à aprovação humana.
- **Exit condition:** deploy habilitado validado nos dois contextos, rollback comprovado e ownership promovido atomicamente sem fallback de sucesso em `logs`.

## Entry Criteria

- [ ] Backend read-only concluído como `Local-Implemented`, com testes/build/lint e revisões finais aceitos.
- [ ] `SMART_NOTAS_READ_ENABLED` permanece `false` até o instante aprovado de ativação.
- [ ] Nenhum segredo ou identificador fiscal foi versionado em código, TODO ou evidência.
- [ ] Contratos de lista, detalhe, erro, privacidade e capacidade permanecem compatíveis com o TODO backend.

## Scope

- [ ] `CUT-01` Injetar por secret store os pares independentes token/CNPJ de Unifast e Prosperar e a chave HMAC, sem registrar valores.
- [ ] `CUT-02` Executar probe redatado `/empresa`, lista e detalhe para ambos os contextos e bloquear mismatch antes de tráfego de usuário.
- [ ] `CUT-03` Calibrar timeout, concorrência, budgets e memória considerando `réplicas × limite local`, quota observável do provedor e o envelope `concorrência × corpo`; fixar orçamento RSS/heap e validar respostas válidas próximas de 2 MiB antes da ativação.
- [ ] `CUT-04` Comprovar destino, retenção, acesso e redaction do sink de auditoria operacional antes da ativação.
- [ ] `CUT-05` Definir sequência enable/deploy/smoke, health/readiness e rollback para flag/configuração/versão anterior.
- [ ] `CUT-06` Validar rotação da chave HMAC e o comportamento de relistagem para identificadores antigos, sem aceitar chaves indefinidamente.
- [ ] `CUT-07` Coordenar consumidores para usar as rotas Smart Notas sem agregação entre emissores nem dependência do conteúdo do `noteId`.
- [ ] `CUT-08` Promover atomicamente `note_read_model` para Smart Notas nos módulos/ledger canônicos somente depois do smoke aprovado.
- [ ] `CUT-09` Manter `logs` apenas como fonte de erros de integração e registrar plano explícito de retirada da leitura legada `/eventos` quando os consumidores migrarem.
- [ ] `CUT-10` Capturar evidência de rollback testado e critérios objetivos de abortar o cutover.

## Out of Scope

- Frontend React ou alteração visual.
- Emissão/cancelamento de notas, DANFE/XML, relatórios ou exportação.
- Alteração de schema Prisma/PostgreSQL ou persistência de espelho/cache de notas.
- Agregação “Todos”, polling, webhook ou retry automático.
- Mudança do tratamento de falhas Routerfy/n8n além de preservar `logs` como fonte exclusiva desses erros.
- Worktrees, checkouts auxiliares ou branches de reconciliação sem autorização humana separada.

## Required Operational Decisions Before Approval

| Decision | Required evidence | State |
| --- | --- | --- |
| Secret destination and rotation owner | serviço/owner de secret store e procedimento redatado | `open` |
| Production timeout | probes e distribuição de latência sem payload | `open` |
| Replica count and provider quota | topologia real + budget agregado seguro | `open` |
| Audit sink and retention | destino, acesso, retenção e alerta | `open` |
| Enable/deploy order | sequência reproduzível e janela operacional | `open` |
| Rollback trigger | thresholds objetivos e responsável | `open` |
| Consumer migration | lista de consumidores e critério de retirada legada | `open` |
| HMAC rotation | validade, relistagem e recuperação | `open` |

## Definition of Done

- [ ] `DOD-CUT-01` Os dois pares fiscais são validados contra a empresa esperada sem exposição de segredo/CNPJ em evidência.
- [ ] `DOD-CUT-02` Timeout, rate, concorrência e orçamento de bytes/memória em voo são calibrados contra a topologia real, medidos sob carga near-limit e documentados com rollback.
- [ ] `DOD-CUT-03` Auditoria operacional tem sink/retention/acesso comprovados e não contém recurso sensível.
- [ ] `DOD-CUT-04` Ativação e smoke passam para lista/detalhe em Unifast e Prosperar; falha não retorna sucesso vazio nem usa `logs`.
- [ ] `DOD-CUT-05` Rollback foi ensaiado e restaura estado seguro sem invalidar dados persistidos, pois não existe espelho local.
- [ ] `DOD-CUT-06` Ownership canônico é promovido atomicamente após o smoke, com `events-and-classification` preservado somente para erros/legado explicitamente registrado.
- [ ] `DOD-CUT-07` Consumidores e retirada da leitura legada têm owner e critério verificável; nenhum dual-read indefinido permanece.

## Validation Plan

- [ ] Reexecutar suite CI-equivalent do backend no artefato exato a implantar.
- [ ] Executar probes redatados dos dois emissores antes e depois da ativação.
- [ ] Confirmar configuração efetiva sem imprimir valores e confirmar flag inicialmente desligada.
- [ ] Executar smoke autenticado dos dois GETs por contexto, incluindo erro controlado e `no-store`.
- [ ] Observar latência, 429/503/504, concorrência e logs durante a janela definida.
- [ ] Executar e registrar o rollback ensaiado.
- [ ] Validar Foundation e capability ledger somente após a promoção atômica.

## Risk and Rollback Frame

- **Primary risks:** pareamento incorreto token/CNPJ, quota agregada por réplica, timeout inadequado, sink de auditoria ausente, rotação HMAC e promoção prematura de ownership.
- **Safe default:** flag desligada.
- **Abort conditions:** mismatch de emissor, vazamento em log/resposta, taxa sustentada de falha acima do threshold a congelar, ausência de auditoria, saturação sem recuperação ou smoke de qualquer contexto falhar.
- **Rollback direction:** desabilitar a flag/reverter a release candidata; não transformar `logs` em fallback de sucesso.

## Approval

- **Status:** `not_requested`
- **Implementation authority:** `none`
- **Required approval:** resposta humana explícita `APROVADO` após refinamento/revisão deste contrato.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** owner de cutover aberto conforme contrato backend; planejamento e aprovação ainda pendentes.
