# Dependency Readiness — UniNotas Cutover

## Snapshot

- **Updated:** `2026-09-27`
- **Owner:** `Operational / DevOps`
- **Governing TODO:** `todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Environment topology:** `artifacts/environment-topology.md`
- **Status:** `partially_ready`

## Dependencies

| Dependency | Target | Status | Evidence | Remaining Gate |
| --- | --- | --- | --- | --- |
| Railway project | `Unifast Products` | `confirmed` | project-owner response | none |
| Railway environment label | `Stage` | `confirmed customer-facing` | project-owner response | use mandatory cutover window and release rollback |
| Railway service identity | `MonitorNotes` | `confirmed` | project-owner response | none |
| Railway public domain | `https://monitornotes-stage.up.railway.app` | `healthy` | `/api/v1/saude` returned HTTP 200 with app/database `ok` on 2026-09-27 | attest deployed revision before runtime evidence |
| Railway source | `main` | `confirmed` | project-owner response | checkpoint must reach this source before deploy |
| Railway plan / region / replicas | `Pro / US East / 1` | `confirmed` | project-owner response | re-resolve immediately before remote mutation |
| Railway operator | `project Owner (identity confirmed privately)` | `confirmed` | project-owner response; identifier omitted for privacy | re-resolve role immediately before remote mutation |
| Railway application logs | `30-day Pro retention` | `confirmed` | official Railway retention + project-owner acceptance | verify access/redaction during cutover |
| Cutover window | `20:00–22:00 America/Sao_Paulo` | `confirmed` | project-owner acceptance + customer-facing Stage | execute only after final operational approval |
| Smart Notas API | Unifast + Prosperar | `unknown` | local credential keys exist; values remain private | redacted `/empresa`, list and detail probe |

## Policy

- Never copy secret values or full fiscal identifiers into this artifact.
- Public health proves only the currently served application/database response, not the candidate revision or Smart Notas binding.
- Target topology is confirmed. Runtime/browser evidence still requires a fresh deployed-revision/config attestation; target identity and operator role must be re-resolved immediately before remote mutation.
