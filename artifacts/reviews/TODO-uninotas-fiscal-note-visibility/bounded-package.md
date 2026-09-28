# Bounded delivery audit package — fiscal note visibility

Derived, non-authoritative review packet for `TODO-uninotas-fiscal-note-visibility`.

## Frozen scope

- Product baseline: `MonitorNotes@8a0dba94a39da67fdd9979563beabb364371968a`.
- Add `recipientName` to the fiscal list summary and show it as `Tomador`.
- Show full purchase/access identifiers in authenticated fiscal UI.
- Detail returns and presents all 21 provider fields requested by the user plus the four existing detail-only fields.
- Public DTOs are exact positive allowlists: 17 summary fields and 27 detail fields.
- Internal records are split: `FiscalNoteListRecord` is the only page/export record; `FiscalNoteDetailRecord` owns detail-only PII.
- Signed/context-bound `noteId` remains the only route identity; it is not a confidentiality mechanism. Raw provider ID is display-only in detail.
- CSV schema is unchanged and excludes recipient PII and provider internal ID.
- All four authenticated roles remain readers; unauthenticated access remains rejected.
- No note-number filter, persistence, provider write, Prisma, Railway, deploy or infrastructure change.

## Bounded changed product paths

- `backend/src/fiscal-notes/fiscal-csv.serializer.ts`
- `backend/src/fiscal-notes/fiscal-notes.application.spec.ts`
- `backend/src/fiscal-notes/fiscal-notes.contract.spec.ts`
- `backend/src/fiscal-notes/fiscal-notes.export.spec.ts`
- `backend/src/fiscal-notes/fiscal-notes.rls.spec.ts`
- `backend/src/fiscal-notes/fiscal-notes.service.ts`
- `backend/src/fiscal-notes/fiscal-notes.types.ts`
- `backend/src/fiscal-notes/smart-notas.adapter.spec.ts`
- `backend/src/fiscal-notes/smart-notas.adapter.ts`
- `backend/src/fiscal-notes/smart-notas.port.ts`
- `backend/src/fiscal-notes/__tests__/smart-notas-live.probe.spec.ts`
- `frontend/package.json`
- `frontend/e2e/notas-race-required.mjs`
- `frontend/e2e/notas-unit.ts`
- `frontend/e2e/notas.mjs`
- `frontend/src/api/notas.ts`
- `frontend/src/estilos/layout.css`
- `frontend/src/notas/normalizacaoFiscal.ts`
- `frontend/src/paginas/DetalheNota.tsx`
- `frontend/src/paginas/ListaNotas.tsx`

## Canonical documentation paths

- `modules/fiscal-notes-and-documents.md`
- `artifacts/feature-briefs/uninotas-fiscal-workspace-improvements.md`
- `todos/active/features/TODO-uninotas-fiscal-note-visibility.md`

## Implementation summary

- Smart Notas list mapping normalizes only the common fiscal fields plus `recipientName`; detail mapping adds document, e-mail, city, state and country with explicit bounds and document shape validation.
- Service response types enumerate every public field rather than deriving from internal records.
- React requires every field in the 17/27 DTO shapes and rejects missing, wrongly typed, empty or overbound strings.
- Geral uses a semantic list of full-row links with six labeled cells; labels are visually hidden on desktop and visible on mobile.
- Detail renders 25 visible fiscal/provider entries: the 21 user-enumerated fields and the four existing detail-only values.
- Mask helpers and re-exports were removed because there are no remaining consumers.
- List cache remains memory-only and detail remains uncached.

## Frontend / Consumer Matrix

| Producer surface | Consumer | Status and evidence |
| --- | --- | --- |
| 17-field `GET /api/v1/notas` item | React `normalizarPaginaFiscal` and `ListaNotas` | implemented; exact-key unit assertions and browser Geral journey |
| 27-field `GET /api/v1/notas/:noteId` | React `normalizarDetalheFiscal` and `DetalheNota` | implemented; exact-key unit assertions and browser detail field matrix |
| `recipientName` in list cache | `CacheFiscal` in authenticated session | implemented; distinct old/new session and late-response unit evidence |
| unchanged 15-column CSV | browser export downloader | implemented; backend byte-exact schema and browser download journey |
| detail-only PII | no list/export consumer | intentionally absent by approved contract; structural record split and negative assertions |

## Validation evidence

- Fail-first evidence: adapter tests initially failed on absent recipient mappings/invalid document acceptance; frontend unit failed on absent `recipientName`.
- Backend full suite: 14 suites passed, 1 opt-in live-probe suite skipped; 306 tests passed, 2 skipped.
- Backend build and lint: passed.
- Frontend fiscal unit suite: passed, including exact 17/27 property omission/type rejection and distinct-session cache cleanup.
- Frontend race command: bare `npm run test:notas:race` runs `clear-late` and `same-key-refresh`, burst 20, and passed; explicit scenario environment remains supported.
- Frontend build and lint: passed.
- Mocked Chromium journey against a fresh Vite preview: passed on desktop and 390 px, including exact full identifiers, anti-truncation/copyability computed styles, 255-code-point name, 128-character purchase/reference values, semantic labels, Enter navigation, null fallback, no horizontal overflow, authenticated flow, logout, privacy sinks and legacy navigation regression.
- Synthetic export ceiling: 20,000 records with distinct 255-code-point recipient names passed within the existing logical deadline; CSV contains no recipient name.
- Signed route identity: service rejects a provider detail whose internal ID differs from the ID bound into the signed route token.
- Real user sample scan across bounded product/Foundation files: no matches.

## Security and residual risk

- Local adversarial review examined authentication/role guards, signed route input, positive property allowlists, provider field validation, no-store headers, aggregate-only logs, browser storage/referrer/request sinks and logout cleanup.
- The provider ID remains decodable from the pre-existing signed `noteId`; this is an approved integrity/context-binding design, not a confidentiality claim.
- No database or runtime activation is in scope. Real-context smoke remains owned by the existing cutover TODO.
- Current review state: no known material security finding; independent gates remain pending when this packet was created.
