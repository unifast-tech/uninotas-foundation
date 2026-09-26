# UniNotas Foundation Lifecycle

## UniNotas current/target boundary

UniNotas uses `current_runtime` for observed behavior and `target_planned` for future architecture; lifecycle evidence does not itself alter runtime authority.

PACED states govern delivery method and evidence only. They never collapse, replace, or promote the independent current/target authority axis.

This document owns lifecycle semantics. Modules own stable local truth; TODOs own approval and delivery evidence; decisions own rationale; artifacts are evidence only.

| Record | States | Transition authority |
| --- | --- | --- |
| Candidate | Proposed, Under-Review, Selected-for-Planning, Deferred, Rejected | strategic steward with evidence |
| Capability | Not-Assessed, Discovery, Planned, In-Progress, Delivered, Retired | module owner and approved TODO evidence |
| TODO | Draft, Review, Approved, In-Progress, Completed, Cancelled | human approval and delivery gates |

`In-Progress` requires explicit `APROVADO` and authority guard `go`; completion is a separate closeout action.
