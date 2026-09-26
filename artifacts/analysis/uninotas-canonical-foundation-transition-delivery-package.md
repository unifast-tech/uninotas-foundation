# UniNotas Canonical Foundation Transition — Delivery Package

## Review boundary

- Governing TODO: `todos/active/process/TODO-uninotas-canonical-foundation-transition.md`.
- Delivery baseline: `0fe906c1e496a1d38f1603cf188c224711011c32`.
- C0 base HEAD/remote observed before staging: `7602404e9f6da91ae5c90303b54e13b9f5130e88`.
- Scope: TD-01..TD-07 only—canonical identity, source ownership, fiscal contexts, runtime-authority registry, target owner boundaries, validator protections, and exact publication inventory.
- Topology: principal checkout, one writer; no worktree, auxiliary checkout, runtime deployment, provider call, credential change, database mutation, or product behavior change.

The candidate tree OID and exact path set are supplied by the external dispatch/attestation. They are deliberately not persisted into the candidate they identify.

Human-review attestations are integrity/freshness metadata inside the approved release-operator trust boundary, not cryptographic credentials. The handoff validates their closed schema, consumer set, phase, candidate tree, exact path set, session identity, outcome, and scope; authentication of the human operator remains an external control.

## Frozen decisions and assumptions

| Decision | Frozen outcome |
| --- | --- |
| TD-01 | Product identity is UniNotas and `core_scope=uninotas`; `MonitorDeNotas` remains the technical repository name. |
| TD-02 | Current runtime keeps the mixed read-only `logs` projection; after capability promotion Smart Notas owns fiscal notes/documents and `logs` narrows to integration-failure evidence only. |
| TD-03 | Unifast and Prosperar are `FiscalIssuerContext` values, not tenants. |
| TD-04 | `current_runtime` and `target_planned` are explicit and distinct from the PACED lifecycle. |
| TD-05 | Fiscal notes/documents, integration-error occurrences, and operational cases have separate target owners. |
| TD-06 | The publication manifest is the sole exact inventory; the validator derives module projection from the governed registry. |
| TD-07 | The current writer/filter for PostgreSQL failure logs remains explicitly unknown. |

Smart Notas target modules remain planned. Current route contracts and current log-derived monitoring/invalidation remain observed runtime facts until later product TODOs promote capability ownership.

## Changed surfaces

- Canonical roots and policies: identity, constitution, mandate, entities, roadmap, technology baseline, lifecycle, query/evidence/scope governance.
- Decisions and modules: canonical UniNotas decision index, six current modules, and three planned target-owner modules.
- Deterministic authority: capability identity ledger, Foundation validator, delivery/lifecycle path enumerator, atomic closeout validator, CAS handoff entry point, and their tests.
- Publication and traceability: manifest, artifact indexes, feature brief, discovery TODO backlinks, and this delivery package.
- Historical frozen inputs remain unchanged: the completed project-rebase TODO and `deterministic/legacy_reference_exceptions.json`.

## Protection and validation evidence

| Area | Command / protection | Observed result |
| --- | --- | --- |
| Registry, identity, privacy | `python3 -B -m unittest deterministic/tests/test_registry_semantics.py deterministic/tests/test_privacy_predicate.py` from the Foundation root equivalent | 86 tests; 4.491s; passed |
| Publication/module projection | `python3 -B -m unittest deterministic/tests/test_validate_foundation.py` | 4 tests; 55.589s; three full-tree scans plus one Git lifecycle/genesis mutation contract; `scan_count=3`; passed |
| Delivery/lifecycle set | `python3 -B -m unittest deterministic/tests/test_enumerate_change_paths.py` | 7 tests; 0.959s; passed |
| Closeout/CAS/handoff | `python3 -B -m unittest deterministic/tests/test_validate_closeout_diff.py deterministic/tests/test_closeout_handoff.py` | 81 tests; 363.587s; passed |
| Canonical tree | `python3 -B deterministic/validate_foundation.py --root .` from Foundation root equivalent | passed |
| PACED readiness | `bash delphi-ai/verify_context.sh` through Git Bash | `PACED-Ready` |
| Diff contract | Delphi diff expectation guard after staging | 41 observed/41 authorized, zero forbidden/unclassified |

Tests cover negative mutation cases for identity/namespaces, current-versus-target source ownership, retired Routerfy attribution, fiscal-context semantics, target-owner boundaries, lifecycle transitions, privacy (including invisible/escaped CNPJ values, duplicate-preserving YAML flow mappings, escape-padded long scalar keys, nested structural keys and deterministic global linear-work budgets), publication, symlink/legacy behavior, candidate-tree binding, exact phase deltas, strict/duplicate-safe JSON schemas, durable intent/resume, post-push remote CAS races, and exact-set activation/recovery scans. Positive registry fixtures include completed `origin=new` ownership and multi-hop history whose earlier modules survive only as catalog tombstones. No mock or fallback is accepted for the bare-remote handoff integration lane.

The current producer-to-consumer lane executes C0 publication, C0_POST verification, C1 proof production/promotion, C1R reverse-proof production/promotion, and activation through the real CLIs. Lifecycle genesis is read from the sole typed TODO field and checked against first-parent ledger history; the identity ledger has the exact root schema `{schema,identities}` and cannot mirror genesis. Duplicate fields, descendant `pending`, unavailable/untrusted Git history, unknown registry enums, non-ignored journals/outputs, and production failpoint use are explicit negative cases. Validator counters now measure the actual Git subprocesses and reuse the first repository enumeration rather than reporting a second hidden traversal.

The C0 promotion boundary no longer trusts outcome-only guard bindings. Before writing its durable intent or pushing, `closeout_handoff.py promote --phase c0` resolves the canonical sibling Delphi, fixes the approved delivery baseline, executes the real diff-expectation, delivery-authority, and delivery-completion guards against the clean C0 commit tree, rejects any nonzero/non-`go` result, rechecks tree cleanliness after every command, and embeds candidate-bound command/output hashes in `live_gate_evidence`; resume reexecutes and replaces that evidence. C1/C1R accept review inputs rather than a caller-authored bridge and internally execute the canonical closeout validator during promote, resume, verification, and activation. The C1 integration fixture also runs the full Foundation validator, while Git-backed lifecycle mutations cover exact C0 genesis plus descendant, pending, missing, malformed, duplicate, and simultaneous active/completed bindings.

Round-04 remediation makes the frozen ledger digest a canonical-order seed projection while allowing strict `origin=new` append-only growth; the full-tree suite proves an appended identity/transition does not trip the seed guard. The closeout lane now requires every real closeout guard to exit successfully, persists/revalidates full production and recovery handoff schemas, records per-phase cumulative delivery and phase-delta sets, and rejects tracked phase inputs/outputs through `git check-ignore` before parsing or side effects.

The validator parses the governed registry before comparing the publication tree: active module paths and the module index are derived from `module_catalog`, generic metadata is checked for every active registry module, and only stable observed-contract semantics plus the three approved target-owner minima remain coded invariants. Current runtime remains the legacy mixed read-only `logs` projection; Smart Notas/error-only `logs` is explicitly target-planned until capability promotion.

## Review lenses and residual risk

- Architecture: reject future-as-current claims, hidden tenancy, duplicate inventory authority, implicit capability aliases, and unbounded compatibility bridges.
- Security/privacy: reject credentials, real CNPJ values, captured provider identifiers, private document URLs, payloads, or responses; verify placeholder handling does not weaken concrete-secret rejection.
- Performance/concurrency: no endpoint, UI, backend-write, or runtime-pressure surface changes; assess validator scan/call bounds and atomic CAS behavior only.
- Test quality: check assertion efficacy, exact diagnostic coverage, real Git/bare-remote boundaries, no silent fallback, and full-tree scan budget.
- Cutover integrity: verify the old decision filename is actually retired, historical exceptions remain bounded, target owners remain planned, and the active-to-completed closeout is the only temporary lifecycle bridge.

`RISK-HIST-01` is the explicit accepted limit: the frozen seed is always protected, while identities added after C0 are protected only within the observable first-parent lineage. An alternative descendant history that preserves C0 cannot be detected without an external anchor. The approval accepts this limit; the delivery must not describe it as broader fail-closed protection.
