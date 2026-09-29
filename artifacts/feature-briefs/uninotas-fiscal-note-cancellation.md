# Feature Brief — Cancelamento de nota fiscal

## Artifact Role

- **Why this brief exists now:** o pedido combina uma mutação fiscal externa, autorização por perfil, coerência do read model e uma mudança visível no detalhe da nota.
- **What this brief is not:** não substitui o módulo fiscal, a constituição, o roadmap ou o TODO tático e não concede autoridade de implementação.

## Source Idea / Request

- Permitir cancelar uma nota pelo MonitorNotes usando a operação oficial `notasCancelar` do SmartNotas.
- Exibir o botão `Cancelar nota` no cabeçalho do detalhe, à esquerda de uma divisória, mantendo o menu de três pontos no extremo direito.
- Decisão humana confirmada: `ADMIN`, `GESTOR` e `ANALISTA` podem cancelar; `LEITOR` permanece somente leitura.

## Problem / Desired Outcome

- **Problem:** hoje o monitor permite consultar detalhes e documentos, mas o cancelamento precisa ser executado fora da aplicação; o menu de três pontos também ocupa uma coluna intermediária do cabeçalho.
- **Desired outcome:** uma nota `Autorizada` pode ser cancelada de forma confirmada, autorizada, observável e sem repetição automática; a tela comunica sucesso, indisponibilidade ou procedimento manual e mantém lista/cache coerentes.
- **Why now:** o SmartNotas já publica o contrato `POST /notas/{idInterno}/cancelar`, e o read model local exige reconciliação explícita após uma mutação bem-sucedida.

## Constraints / Non-Goals

- **Constraints:** SmartNotas continua sendo a autoridade fiscal; usar somente o `noteId` opaco assinado como autoridade de rota; não aceitar CNPJ/token/id interno do cliente; não repetir automaticamente uma mutação de resultado incerto; exigir confirmação; manter `LEITOR` sem permissão; mensagem externa deve ser limitada e tratada como texto.
- **Non-goals:** cancelamento em lote, motivo livre, emissão, reprocessamento, cancelamento de status diferente de `Autorizada`, automação de procedimento municipal manual, alteração de credenciais/quota ou armazenamento de payload bruto.

## Canonical Touchpoints

- **Constitution impact:** none — preserva autenticação, isolamento de contexto e SmartNotas como autoridade.
- **Module-authority impact:** required — a decisão proposta `FISC-CAN-01` cria uma exceção limitada ao guardrail atual de `provider writes`; permanece inativa até aprovação explícita do TODO.
- **Roadmap impact:** none — evolução delimitada do módulo fiscal existente.
- **Primary module candidates:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module candidates:** `foundation_documentation/modules/identity-and-team.md`

## Evidence / References

- SmartNotas: `POST /notas/{idInterno}/cancelar`, operação `notasCancelar`: `https://app.smart-notas.com/api/docs#tag/Notas/operation/notasCancelar`.
- `backend/src/fiscal-notes/smart-notas.adapter.ts`: transporte, credenciais por contexto, limites e normalização atuais.
- `backend/src/fiscal-notes/fiscal-notes.controller.ts`: endpoints fiscais e perfis leitores atuais.
- `backend/src/auth/perfil.enum.ts`: `PERFIS_QUE_EDITAM` já contém `ADMIN|GESTOR|ANALISTA`.
- `frontend/src/paginas/DetalheNota.tsx`: cabeçalho e menu de documentos atuais.
- `backend/src/fiscal-notes/fiscal-note-cache.service.ts`: projeção local que precisa refletir cancelamento confirmado.

## Ambiguities To Resolve Before TODO

| ID | Ambiguity | Why It Matters | Current Evidence | Handling |
| --- | --- | --- | --- | --- |
| `AMB-CAN-01` | Quem pode cancelar? | É uma mutação fiscal de alto impacto. | Usuário confirmou `ADMIN|GESTOR|ANALISTA`; `LEITOR` somente leitura. | `resolved` |
| `AMB-CAN-02` | Há motivo de cancelamento? | Mudaria DTO, UX e contrato externo. | OpenAPI não define request body. | `resolved: no body` |
| `AMB-CAN-03` | Como tratar timeout? | Retry automático pode duplicar uma operação irreversível. | Provider não publica chave de idempotência. | `resolved: estado uncertain durável e fail-closed, sem expiração ou retry pelo Monitor` |
| `AMB-CAN-04` | Como refletir no banco? | Lista local não pode permanecer autorizada após sucesso conhecido nem ser rebaixada por página antiga. | Read model é derivado e indexado por contexto + ID interno. | `resolved: operação/tombstone durável + upsert atômico que cobre cache presente ou ausente` |
| `AMB-CAN-05` | Como tratar duas abas/clientes/réplicas? | Single-flight apenas no React ou processo não protege o provider. | PostgreSQL já é dependência compartilhada do read model. | `resolved: eleição atômica durável por contexto + ID, uma chamada líder e lease vencido convertido em uncertain` |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ST-FISCAL-CANCEL-01` | Cancelar uma nota autorizada no detalhe com confirmação e feedback seguro. | fiscal-notes-and-documents | identity-and-team, React UI | Uma única mutação líder por nota; perfis corretos; tombstone/cache monotônico; layout responsivo; erros e resultado manual explícitos. | adapter/service/PostgreSQL application tests, concorrência/race, parser/UI e browser responsivo | `create-now` | aprovação do TODO | história atual |
| `ST-FISCAL-CANCEL-02` | Cancelamento em lote ou por motivo customizado. | fiscal-notes-and-documents | operations | contrato próprio e suporte oficial do provider | contrato/provider + carga | `defer` | API não oferece esse contrato | fora do pedido |

## Retire This Brief When

- O TODO tático de `ST-FISCAL-CANCEL-01` estiver aprovado e o módulo fiscal consolidar as decisões estáveis.
