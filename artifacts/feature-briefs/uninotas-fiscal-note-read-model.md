# Feature Brief — Read model local de notas fiscais

## Objective

Estabelecer uma projeção local, derivada e reconstruível das notas fiscais do Smart Notas para que listagens e exportações volumosas possam consultar o PostgreSQL sem depender de uma travessia completa do provedor a cada operação.

## Problem

O Smart Notas limita temporariamente consultas durante exportações grandes. A exportação atual percorre páginas diretamente no provedor e, por isso, repete custo, latência e risco de `429` em cada execução.

## Proposed story

Criar um read model fiscal local, separado de `logs`, com sincronização resumível Smart Notas → PostgreSQL e leitura local para listagem/exportação quando houver cobertura válida. A API do Smart Notas continua sendo a autoridade fiscal; o PostgreSQL será apenas uma projeção derivada, nunca um fallback silencioso para dados ausentes ou uma fonte de emissão.

## Decisions required before implementation

- Identidade e unicidade por `contextoFiscal + idInterno`.
- Campos persistidos, classificação de dados pessoais e eventual payload bruto redigido.
- Política de frescor, invalidação e comportamento quando a projeção estiver atrasada ou incompleta.
- Dono e execução da sincronização: request, job, comando operacional ou worker.
- Estratégia de backfill inicial, retomada após falha e tratamento de mudanças de status.
- Uso de Prisma migrations versus SQL de migração aprovado pelo repositório.
- Índices, orçamento de conexões, retenção, backup/restauração e observabilidade.
- Se o detalhe completo será armazenado ou continuará sendo obtido sob demanda no Smart Notas.

## Boundaries

Inclui listagem/exportação fiscal e a projeção derivada necessária para reduzi-las. Não inclui emissão, cancelamento, alteração de notas, documentos PDF/XML, escrita em `logs`, agregação entre Unifast e Prosperar ou substituição da autoridade Smart Notas.

## Success criteria

- Exportações repetidas cobertas pelo read model não fazem uma travessia completa no Smart Notas.
- Contextos fiscais permanecem isolados.
- Falhas, atraso, lacunas e sincronização parcial são explícitos; nunca viram lista vazia de sucesso.
- A projeção pode ser apagada e reconstruída a partir da API sem perder a autoridade fiscal.
- Consultas e exportações locais têm plano/indexação e limites de memória demonstrados.
