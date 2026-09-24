# Monitor de Notas Foundation

`uninotas-foundation` is the canonical product documentation for Monitor de Notas. It records verified product boundaries; it does not authorize runtime changes.

Start with the [mandate](project_mandate.md), [constitution](project_constitution.md), [domain entities](domain_entities.md), [technology baseline](technology_baseline.md), lifecycle record, and [module index](modules/README.md).

## Authority and setup

This repository owns product-specific truth. The local `delphi-ai` distribution owns the PACED method, workflows, and deterministic guards. An approved active TODO plus authority guard `go` is required before implementation.

The workspace alias `foundation_documentation -> uninotas-foundation` is local setup, not product content. On Windows use `cmd /c mklink /D foundation_documentation uninotas-foundation` only when the alias is absent. Validate it in Git Bash with `./delphi-ai/verify_context.sh`; the WSL wrapper has a documented CRLF limitation and is not the acceptance runner.
