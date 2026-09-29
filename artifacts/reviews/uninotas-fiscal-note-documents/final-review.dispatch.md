# PACED Subagent Dispatch: final_review

## Dispatch Identity
- **Artifact kind:** `subagent_review_dispatch`
- **Authoritative:** `false`
- **Edit policy:** `derived_dispatch_packet`
- **Review kind:** `final_review`
- **Bounded package:** `uninotas-foundation/artifacts/reviews/uninotas-fiscal-note-documents/delivery-package.md`
- **Reviewer count:** `1`
- **No-context required:** `true`

## Required Axes
- `adherence`
- `residual_risk`
- `performance`
- `elegance`
- `structural_soundness`

## Focus Points
- Review the delivered bounded package for regressions, adherence gaps, residual risk, and waiver quality.
- Explicitly call out any performance regressions, elegance regressions, or brittle structural shortcuts.
- Stay inside the bounded package and treat the review as closure-focused.
- For each material finding, add category and formalizable-hint when you can judge them honestly.
- When assessing design, seek the simplest faithful Clean Code/SOLID design for the approved intent. Do not invent future-facing work or erase explicit TODO intent. Planning review may challenge proposed intent; delivery review must preserve approved intent or return for renewed approval.

## Required Result Fields
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings[].finding_id (optional)`
- `findings[].category (optional)`
- `findings[].formalizable_hint (optional)`
- `findings[].candidate_rule_level (optional)`
- `findings[]`

## Required Result Binding
The reviewer result's `dispatch_path` must equal this exact dispatch JSON path:
`/mnt/c/unifast/monitordenotas/uninotas-foundation/artifacts/reviews/uninotas-fiscal-note-documents/final-review.dispatch.json`
Do not substitute the bounded package path, governing TODO path, or reviewer output path.

## Goal
Expanded final review: findings first; verify adherence, P1/P2 correctness/security/test risks, rule-spirit triage, performance/elegance/structural soundness, unresolved debt and local-delivery claim.

## Related TODO
`uninotas-foundation/todos/active/features/TODO-uninotas-fiscal-note-documents.md`

Reviewers must cross-check findings against the governing TODO's explicit decisions, approved exceptions, compatibility mandates, and non-goals before classifying something as blocking drift.

## Historical Finding Carry-Forward
Previously adjudicated findings are historical context, not automatic reopening triggers.
- Resolved findings are historical context only. Do not reopen them unless the current bounded package materially changes the same locus/behavior or fresh evidence shows regression.
- Challenged findings stay closed unless the current bounded package materially changes the same locus/behavior or the prior rationale is objectively insufficient.
- Deferred findings must cite the recorded follow-up/waiver path first. Re-raise them only when the current bounded package changes the same locus or closure now depends on that deferred risk.
- Unresolved findings remain valid to re-raise until they are fixed, challenged, or formally deferred with authority.

### Recorded Dispositions
- `promotion_routing / PERF-DOC-001` -> `resolved`
  - Disposition: classification=release-blocker; routing=validar ownership também em rejection tardia; status=resolved
  - Summary: mesma lifecycle aprovada
  - Reference: triple round-01 resolution
- `promotion_routing / TQA-DOC-001` -> `resolved`
  - Disposition: classification=release-blocker; routing=provar efeitos externos e lifecycle resolve/reject/navigation; status=resolved
  - Summary: mesma matriz de testes aprovada
  - Reference: triple round-01 resolution + FRC artifact
- `promotion_routing / TQA-DOC-002` -> `resolved`
  - Disposition: classification=release-blocker; routing=corrigir/provar disclosure móvel list/detail; status=resolved
  - Summary: mesmo escopo responsivo aprovado
  - Reference: triple round-01 resolution
- `promotion_routing / SEC-DOC-01` -> `resolved`
  - Disposition: classification=release-blocker; routing=exigir sintaxe absoluta e retornar somente `parsed.href`; status=resolved
  - Summary: mesma boundary URL aprovada
  - Reference: security confirmation
- `promotion_routing / SEC-DOC-02` -> `resolved`
  - Disposition: classification=release-blocker; routing=manter flags e usar texto neutro para retorno `null` ambíguo; status=resolved
  - Summary: mesma UX/fallback aprovada
  - Reference: security confirmation
- `promotion_routing / SEC-DOC-03` -> `resolved`
  - Disposition: classification=release-blocker; routing=bound também após canonicalização; status=resolved
  - Summary: mesmo limite de 8 KiB aprovado
  - Reference: Unicode expansion regression
- `promotion_routing / TQA-DOC-R2-001` -> `resolved`
  - Disposition: classification=release-blocker; routing=fixture JSON válida exata/over, stream sem length e cancel; status=resolved
  - Summary: mesma evidência de 16 KiB aprovada
  - Reference: triple round-02 resolution
- `promotion_routing / TQA-DOC-R3-001` -> `resolved`
  - Disposition: classification=release-blocker; routing=asserção direta zero-prefetch ao abrir/trocar disclosure; status=resolved
  - Summary: ajuste inline no teste aprovado
  - Reference: triple round-03 resolution + fresh browser

## Result Contract
Return exactly one JSON object and no Markdown fence or prose.
Do not emit `null`; omit optional fields that do not apply.
No top-level fields other than the following are allowed:
- `schema_version`: `subagent-review-result-v1`
- `artifact_kind`: `subagent_review_result`
- `dispatch_path`: the exact binding shown above
- `review_kind`: `final_review`
- `reviewer_label`
- `overall_assessment`
- `recommended_path`
- `performance_position`
- `elegance_position`
- `structural_soundness_position`
- `operational_fit_position`
- `findings`

Every `*_position` value must be one of: `strong_positive`, `acceptable`, `mixed`, `regresses`, `unknown`, `not_evaluated`.
Each finding may contain only these fields:
- required: `severity`, `title`, `rationale`, `suggested_action`
- optional: `finding_id`, `category`, `formalizable_hint`, `candidate_rule_level`, `candidate_rule_id`, `affected_paths`
- `severity` values: `low`, `medium`, `high`
- `category` values: `architecture`, `adherence`, `tests`, `performance`, `security`, `elegance`, `structural_soundness`, `operational_fit`, `residual_risk`, `other`
- `formalizable_hint` values: `yes`, `partial`, `no`, `unknown`
- `candidate_rule_level` values: `paced`, `project`, `none`, `unknown`
