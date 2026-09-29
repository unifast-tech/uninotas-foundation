# Documentos da nota e affordances do workspace — Feature Brief

## Artifact Role

- **Why this brief exists now:** a solicitação combina uma capacidade fiscal nova (acesso a PDF/XML), a confirmação do detalhe já entregue e um pequeno ajuste visual no cabeçalho. O brief separa o que é integração nova do que já existe e impede uma segunda implementação de detalhe.
- **What this brief is not:** autoridade de implementação, módulo canônico, contrato de deploy ou aprovação.

## Source Idea / Request

O usuário solicitou, em 2026-09-28:

1. mostrar os detalhes da SmartNotas quando a nota for aberta;
2. oferecer PDF e XML em um menu de três pontos verticais em cada nota;
3. aumentar o ícone de configurações.

Referências oficiais informadas:

- `GET /notas/{idInterno}` (`operationId=notasDetalhe`);
- `GET /notas/{idInterno}/pdf` (`operationId=notasPdf`);
- `GET /notas/{idInterno}/xml` (`operationId=notasXml`).

## Problem / Desired Outcome

- **Problem:** o detalhe fiscal completo já existe no UniNotas, mas os documentos oficiais ainda exigem sair do produto; o gatilho de configurações também tem um glifo pequeno para sua caixa de interação.
- **Desired outcome:** o usuário financeiro abre o detalhe completo atual e, a partir de cada nota, escolhe `Abrir PDF` ou `Abrir XML` sem conhecer `idInterno`, token ou CNPJ; o controle de configurações fica visualmente mais evidente.
- **Why now:** a central fiscal está sendo preparada para uso operacional e PDF/XML são artefatos essenciais da conferência da nota.

## Constraints / Non-Goals

- **Constraints:** manter um único contexto fiscal por consulta; usar exclusivamente o `noteId` assinado/context-bound como identidade pública; credenciais permanecem no backend; não pré-carregar documentos; não persistir/cachear/logar URLs ou conteúdo fiscal; todos os quatro perfis leitores mantêm acesso; respeitar `202` do provedor como documento ainda indisponível.
- **Non-goals:** emissão/cancelamento/carta de correção, armazenamento local de PDF/XML, anexos em banco, lista agregada Unifast+Prosperar, nova variável Railway, mudança de perfis, deploy ou cutover.

## Canonical Touchpoints

- **Constitution impact:** `none` — fonte, perfis e separação de contextos não mudam.
- **Roadmap impact:** `none` — extensão do módulo fiscal já previsto.
- **Primary module candidates:** `modules/fiscal-notes-and-documents.md`
- **Secondary module candidates:** `none` — os quatro perfis leitores já pertencem ao contrato do módulo fiscal; não existe módulo `authentication-and-access.md`.

## Evidence / References

- OpenAPI oficial publicado em `https://app.smart-notas.com/docs/api-docs.json`, SHA-256 `cc2a415962dcff00b7d91d3a1bfe99544ec3bd1543b2e5f9d93df1b8ce686502`, consultado em 2026-09-28.
- `backend/src/fiscal-notes/smart-notas.adapter.ts` já chama `GET /notas/{idInterno}` para detalhe.
- `frontend/src/paginas/DetalheNota.tsx` já apresenta a allowlist completa aprovada de detalhe.
- `frontend/src/paginas/ListaNotas.tsx` possui uma linha/card navegável por `noteId` e ainda não possui ações documentais.
- `frontend/src/componentes/Cabecalho.tsx` expõe o gatilho acessível `Abrir configurações` com o glifo `⚙` herdando `12px` de `.btn`.

## Ambiguities To Resolve Before TODO

| ID | Ambiguity | Why It Matters | Current Evidence | Handling |
| --- | --- | --- | --- | --- |
| `AMB-01` | A solicitação de detalhe exigiria uma nova rota? | Duplicaria contrato e chamadas ao provedor. | detalhe backend/frontend já implementado e testado | `resolve now: preservar e testar; nenhuma nova rota de detalhe` |
| `AMB-02` | PDF/XML devem ser pré-carregados? | Dobraria chamadas, consumiria quota e criaria URLs obsoletas. | endpoints oficiais são independentes e retornam `202` quando pendentes | `resolve now: resolver somente após clique` |
| `AMB-03` | O backend deve armazenar ou fazer proxy do arquivo? | Aumentaria retenção, memória e superfície SSRF. | o contrato oficial devolve uma URL HTTPS; probe redatado Prosperar observou `files.smart-notas.com` | `resolve now: handoff efêmero de URL restrita às origins conhecidas, sem proxy/persistência` |
| `AMB-04` | O menu aparece apenas no detalhe? | “em cada nota” inclui as linhas/cards da Geral. | lista já é a superfície de seleção de nota | `resolve now: menu em cada linha/card e também no cabeçalho do detalhe` |

## Story Decomposition

| Story ID | Story / User Value | Primary Module | Secondary Modules | Acceptance Boundary | Candidate Validation Signal | Candidate TODO Decision | Dependencies / Blockers | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ST-DOCUMENT-ACTIONS` | Abrir PDF ou XML de qualquer nota e continuar vendo todos os dados fiscais aprovados | `fiscal-notes-and-documents` | `authentication-and-access` | duas resoluções autenticadas por `noteId`, menu `⋮` na Geral e detalhe, estados disponível/pendente/erro, sem retenção | Jest adapter/application/contract + unit React + Playwright desktop/mobile | `create-now` | API SmartNotas habilitada para prova real somente no cutover; fixtures locais são determinísticas | detalhe existente é preservado, não refeito |
| `ST-SETTINGS-AFFORDANCE` | Identificar e acionar configurações com mais facilidade | `fiscal-notes-and-documents` | `none` | glifo maior dentro de alvo mínimo 44x44, sem regressão do disclosure | computed CSS + teclado/foco em Playwright | `merge-with-other` | nenhuma | ajuste pequeno no mesmo CSS/browser package; não muda comportamento de conta |

## Retire This Brief When

- Condição satisfeita: o TODO foi aprovado, implementado e convergiu em revisão final independente sem ambiguidade de framing pendente.
- Resultado promovido: detalhes existentes preservados; PDF/XML sob demanda, URL efêmera protegida e gatilho de configurações ampliado estão documentados em `modules/fiscal-notes-and-documents.md`.
- Estado: `retired by completed tactical TODO`; deploy e smoke real continuam sob autoridade do TODO de cutover.
