# Identity and Team

## Module Intent & Boundaries
- **Core scope:** `uninotas`
- **Subscope:** `identity-and-team`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Runtime authority state:** `current_runtime`
- **Owned capabilities:** `authentication`, `team_profiles`
- **Planned capabilities:** none
- **Out-of-scope guardrails:** Business tenancy, deletion that loses treatment authorship, or credentials in documentation.
- **Dependency boundaries:** JWT authentication and `monitor_usuarios` profiles support protected product operations.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns session authentication, profiles, and financial-team administration. Users are deactivated rather than deleted to preserve authorship; product behavior protects the final administrator.

## Observed Authentication Contract

All routes use base path `/api/v1`. Normal protected routes validate bearer signature/expiry. On a cache miss they resolve an active, known user before role checks; a cached identity/profile may be reused for up to 30 seconds, so deactivation or profile-change enforcement may lag by that observed cache window. The realtime query-token exception is owned separately and does not perform that user lookup.

| Route | Authorization and request | Status / media | Successful response |
| --- | --- | --- | --- |
| `POST /auth/login` | public; body has valid `email` and string `senha` of at least 6 characters | HTTP 200 `application/json` | `{accessToken,expiraEm,usuario}`; `usuario={id,nome,email,perfil,senhaProvisoria}` |
| `GET /auth/eu` | normal JWT | HTTP 200 `application/json` | current user summary fields above |
| `GET /usuarios` | `ADMIN|GESTOR` | HTTP 200 `application/json` | array of users `{id,nome,email,perfil,ativo,senhaProvisoria,criadoEm}` |
| `POST /usuarios` | `ADMIN`; `nome` 3..200, valid `email`, `senha` 8..72, optional `perfil=ADMIN|GESTOR|ANALISTA|LEITOR` | HTTP 201 `application/json` | created user fields |
| `PATCH /usuarios/minha-senha` | normal JWT; body `senhaAtual` string and `novaSenha` 8..72 | HTTP 200 `application/json` | updated user fields |
| `PATCH /usuarios/:id` | `ADMIN`; UUID path; partial create fields plus optional boolean `ativo` | HTTP 200 `application/json` | updated user fields |
| `DELETE /usuarios/:id` | `ADMIN`; UUID path | HTTP 200 `application/json` | deactivated user fields; row/authorship remains |

Invalid credentials, missing/expired bearer tokens, inactive/unknown users after cache revalidation on normal JWT routes, insufficient roles, self-deactivation, self-demotion, last-administrator removal, duplicate identity, missing users, and validation failures reject through `{statusCode,erro,mensagem,caminho,timestamp}`. The cache-window qualification above applies to deactivation and profile changes.

## Purpose, Owned Entities, and Workflows
**Purpose:** govern who may operate the monitor. **Owned/orchestrated entities:** `Usuario`, profile, and authenticated session. **Workflows/capabilities:** authenticate, manage team profiles, deactivate users, and preserve the last administrator. **Invariants/validation/auth:** JWT guards protected operations; active status is required; deletion does not erase authorship. **Observed contracts:** auth and user services are evidenced; credential values, endpoint examples, and SLO are intentionally undocumented.

## Cross-Module Considerations and Failure Modes
Treatments consume user authorship. Authentication or user-store failure denies protected operation; it never grants a fallback identity.
