# Identity and Team

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `identity-and-team`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Business tenancy, deletion that loses treatment authorship, or credentials in documentation.
- **Dependency boundaries:** JWT authentication and `monitor_usuarios` profiles support protected product operations.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns session authentication, profiles, and financial-team administration. Users are deactivated rather than deleted to preserve authorship; product behavior protects the final administrator.

## Observed Authentication Contract

`POST /auth/login` accepts validated credentials and returns the authenticated session representation; `GET /auth/eu` returns the current authenticated user. `GET /usuarios`, `POST /usuarios`, `PATCH /usuarios/minha-senha`, `PATCH /usuarios/:id`, and `DELETE /usuarios/:id` are protected team operations. JWT authentication rejects missing, expired, inactive, or unknown users; role enforcement rejects an insufficient profile. Invalid credentials, self-deactivation, self-demotion, last-administrator removal, and missing users are rejected rather than silently changing ownership.

```json
{"base_path":"/api/v1","routes":["POST /auth/login","GET /auth/eu","GET /usuarios","POST /usuarios","PATCH /usuarios/minha-senha","PATCH /usuarios/:id","DELETE /usuarios/:id"],"authorization":"login public; JWT otherwise; list ADMIN|GESTOR; create/update/delete ADMIN","responses":"auth-session|current-user|user|user-list","errors":"401|403|404|validation use standard error body"}
```

## Purpose, Owned Entities, and Workflows
**Purpose:** govern who may operate the monitor. **Owned/orchestrated entities:** `Usuario`, profile, and authenticated session. **Workflows/capabilities:** authenticate, manage team profiles, deactivate users, and preserve the last administrator. **Invariants/validation/auth:** JWT guards protected operations; active status is required; deletion does not erase authorship. **Observed contracts:** auth and user services are evidenced; credential values, endpoint examples, and SLO are intentionally undocumented.

## Cross-Module Considerations and Failure Modes
Treatments consume user authorship. Authentication or user-store failure denies protected operation; it never grants a fallback identity.
