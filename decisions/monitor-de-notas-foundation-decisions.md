# Monitor de Notas Foundation Decisions

| ID | Current decision | Evidence / canonical target |
| --- | --- | --- |
| D-01 | Product name is Monitor de Notas; technical repository is MonitorDeNotas; documentation repository is uninotas-foundation. | [mandate](../project_mandate.md) |
| D-02 | Retired documentation is removed from the active tree; Git history is recovery only. | [cutover map](../artifacts/analysis/monitor-de-notas-foundation-cutover-map-20260924.md) |
| D-03 | Foundation owns product truth; `delphi-ai` owns PACED method and guards. | [constitution](../project_constitution.md) |
| D-04 | Routerfy owns and writes the authoritative production `logs`; Monitor de Notas reads that external table only and writes only its application tables. The local development replica is derived, disposable, non-authoritative, and populated only by explicit mirror tooling. | [constitution](../project_constitution.md) |
| D-05 | There is one product scope and no business tenancy; `landlord` is PACED adapter vocabulary. | [scope policy](../policies/scope_subscope_governance.md) |
