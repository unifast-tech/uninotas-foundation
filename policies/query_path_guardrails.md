# Query Path Guardrails

`logs` is Routerfy-owned and read-only. Queries must retain the SmartNotas boundary, must not assume `ref_id` uniqueness, and must preserve SQL/TypeScript classification equivalence. Treatments are application-owned append-only records.
