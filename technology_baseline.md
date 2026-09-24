# Monitor de Notas — Technology Baseline

Verified on 2026-09-24 from the read-only product tree.

| Layer | Observed implementation | Evidence |
| --- | --- | --- |
| API | NestJS 11 / TypeScript | `../backend/` |
| Web | React / Vite / TypeScript | `../frontend/` |
| Data | PostgreSQL via Prisma; raw SQL for external `logs` | `../backend/prisma/`, `../backend/src/logs/` |
| Runtime | Docker and Railway configuration | `../Dockerfile`, `../docker-compose.yml`, `../railway.json` |

This is navigation evidence, not authorization to change infrastructure, providers, secrets, or runtime health.
