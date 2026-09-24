# TODO Governance

Active TODOs are bounded execution contracts, not stable product truth. Execution requires explicit approval and authority guard `go`; completed TODOs retain evidence only. PACED workflows and guards are provided by `delphi-ai`.

## Project Routing Taxonomy

- `active/features/` is reserved for approved product-capability delivery contracts.
- `active/bugs/` is reserved for approved defect-repair contracts.
- `active/process/` owns Foundation, governance, migration, and other process contracts; the current Foundation rebase is routed here.
- `completed/<lane>/` retains the closed contract and its evidence under the same lane classification.

The external PACED owner defines intake, review, execution, audit, and closeout mechanics under `delphi-ai/skills/`; this repository records only project-specific contracts and evidence. A lane directory is created only when an approved project TODO needs it and the exact publication manifest is updated. Stable product truth belongs in the canonical root, module, policy, decision, contract, or artifact owner—not in an active TODO.
