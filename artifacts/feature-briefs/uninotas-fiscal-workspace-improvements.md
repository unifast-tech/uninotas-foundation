# Melhorias do workspace fiscal do UniNotas — Feature Brief

## Artifact Role

- **Why this brief exists now:** a revisão visual do UniNotas identificou ajustes de navegação, marca, contraste e layout, enquanto a exportação do filtro inteiro e a visibilidade fiscal ampliada introduzem contratos públicos e riscos próprios. O objetivo de release é único, mas os riscos e evidências precisam de três TODOs independentes.
- **What this brief is not:** autoridade de implementação, aprovação, módulo canônico ou contrato de deploy.

## Source Request

O usuário solicitou:

1. corrigir contraste dos selects em tema escuro;
2. alinhar filtros e remover a atualização manual redundante;
3. usar a marca oficial anexada;
4. exportar todas as notas correspondentes aos filtros aplicados;
5. reunir conta, tema, equipe, senha e sair em configurações;
6. expor `Processamento das notas` como acesso à tela PostgreSQL existente;
7. centralizar a paginação e criar respiro inferior.

Em 2026-09-28, o usuário esclareceu que a exportação deve abranger **todos os registros do contexto e dos filtros aplicados**, independentemente da página visível.

Ainda em 2026-09-28, o usuário solicitou uma terceira evolução: incluir `Tomador` na Geral, exibir compra e chaves completas para a equipe financeira e apresentar no card todos os campos enumerados do `GET /notas`. O filtro por número foi considerado e explicitamente cancelado por não existir suporte equivalente no provedor.

## Confirmed Product Direction

- `Geral` continua sendo a lista fiscal de um único contexto: Unifast ou Prosperar.
- Não existe lista nem exportação agregada entre contextos.
- Contexto, status e datas continuam atualizando automaticamente; Documento e ID da compra continuam dependendo de `Aplicar filtros`.
- O botão manual `Atualizar` deixa de existir na Geral.
- `Processamento das notas` abre a projeção PostgreSQL já existente; este objetivo não altera seus dados ou filtros.
- Todos os perfis leitores podem exportar o filtro fiscal do contexto ativo.
- A exportação pertence ao backend; o navegador faz uma única solicitação autenticada e nunca percorre páginas do provedor.
- Todos os perfis autenticados atuais podem visualizar os dados fiscais allowlisted; lista e detalhe continuam protegidos pelas rotas existentes.
- A Geral acrescenta somente o nome do tomador como nova PII. Documento, e-mail e localização ficam exclusivamente no detalhe; o CSV permanece sem PII do tomador.
- `noteId` assinado continua sendo a única identidade aceita na rota de detalhe. O ID interno pode ser exibido como referência, mas nunca enviado cru como autoridade de consulta.

## Story Decomposition

| Story ID | Story / User Value | Tactical TODO | Acceptance Boundary | Sequence |
| --- | --- | --- | --- | --- |
| `ST-UX` | Usar um workspace fiscal legível, alinhado, com marca e navegação coerentes | `todos/completed/features/TODO-uninotas-fiscal-workspace-ux.md` | `Local-Implemented` em `MonitorNotes@f1a950a9`; React/Vite, ativo local, CSS, acessibilidade e browser; sem novo endpoint | `1 — completed` |
| `ST-EXPORT` | Baixar todas as notas que pertencem ao contexto e aos filtros aplicados | `todos/completed/features/TODO-uninotas-filtered-csv-export.md` | `Local-Implemented` em `MonitorNotes@8a0dba94`; NestJS + cliente React, CSV seguro, paginação bounded, corrida/cancelamento e carga; sem deploy | `2 — completed` |
| `ST-VISIBILITY` | Identificar o tomador e consultar todos os dados fiscais aprovados sem máscaras | `todos/completed/features/TODO-uninotas-fiscal-note-visibility.md` | `Local-Implemented`; NestJS + React, allowlists 17/27, lista/detalhe responsivos, PII efêmera e CSV inalterado; sem deploy | `3 — completed` |

Os três TODOs podem receber aprovação na mesma conversa, mas mantêm implementação, risco e evidência independentes. O executor permanece serializado no checkout principal. Depois do closeout local de `ST-UX` e antes de iniciar `ST-EXPORT`, o segundo TODO deve rebaselinar produto e Foundation sobre o estado consolidado, reclassificar o diff e repetir coherence/drift/authority; qualquer mudança material exige review e aprovação renovados.

`ST-UX`, `ST-EXPORT` e `ST-VISIBILITY` concluíram localmente em 2026-09-28. O deploy, smoke real e calibração de quota continuam fora desse corte e pertencem ao cutover.

## Provider Constraint

Smart Notas oferece paginação numérica, sem cursor ou token de snapshot evidenciado. Assim, a entrega consegue validar página, metadados, contagem e duplicidade e falhar sem arquivo quando detectar mudança; ela não pode afirmar uma fotografia transacional enquanto a origem é alterada. O contrato de exportação deve comunicar essa limitação e nunca chamar uma travessia paginada de snapshot.

## Non-Goals

- exportação agregada, XLSX, fila/worker, persistência de arquivo ou cache de notas;
- mudança na tela/banco de processamento;
- mutation fiscal, DANFE/XML, Prisma, Docker, Railway, deploy ou merge;
- alteração do modelo de autenticação ou dos perfis leitores existentes.

## Completion Boundary

O objetivo fica pronto localmente quando os três TODOs alcançarem `Local-Implemented` com seus próprios testes, auditorias e documentação. Promoção/deploy continua pertencendo ao TODO de cutover.
