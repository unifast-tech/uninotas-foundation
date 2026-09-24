# TODO Governance

Active TODOs are bounded execution contracts, not stable product truth. Execution requires explicit approval and authority guard `go`; completed TODOs retain evidence only. PACED workflows and guards are provided by `delphi-ai`.

## Project Routing Taxonomy

- `active/features/` is reserved for approved product-capability delivery contracts.
- `active/bugs/` is reserved for approved defect-repair contracts.
- `active/process/` owns approved Foundation, governance, migration, and other process contracts while work is open.
- `completed/<lane>/` retains the closed contract and its evidence under the same lane classification; the Monitor de Notas Foundation rebase is retained in `completed/process/`.

The external PACED owner defines intake, review, execution, audit, and closeout mechanics under `delphi-ai/skills/`; this repository records only project-specific contracts and evidence. A lane directory is created only when an approved project TODO needs it and the exact publication manifest is updated. Stable product truth belongs in the canonical root, module, policy, decision, contract, or artifact owner—not in an active TODO.

## Review Finding Classification

Every deduplicated review or audit finding is recorded in the governing TODO's promotion-routing ledger as exactly one of:

- `release-blocker`: must be resolved before the current delivery or promotion claim.
- `follow-up-fast-follow`: does not block the current lane, but requires an explicit approved fast-follow TODO owner before the lane is called clean.
- `follow-up-hardening`: does not block the current lane, but requires an explicit approved hardening TODO owner before the lane is called clean.
- `by-design/no-action`: requires evidence showing why no change or follow-up owner is warranted.

Only `release-blocker` blocks the current lane. Non-blocking real findings are never discarded; they are linked to their explicit project TODO owner before closeout.
