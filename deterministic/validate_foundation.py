#!/usr/bin/env python3
"""Fail-closed validator for the frozen Monitor de Notas Foundation cutover."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ACTIVE_TODO = "todos/active/process/TODO-uninotas-foundation-project-rebase.md"
COMPLETED_TODO = "todos/completed/process/TODO-uninotas-foundation-project-rebase.md"
LIFECYCLES = {ACTIVE_TODO: "active_until_closeout_move", COMPLETED_TODO: "historical"}
ROOT_FILES = {"README.md", "project_mandate.md", "project_constitution.md", "domain_entities.md", "technology_baseline.md", "evolution_lifecycle.md", "system_roadmap.md", "local_packages.yaml"}
SUPPORT_FILES = {"artifacts/README.md", "artifacts/publication-manifest.txt", "backlog/README.md", "contracts/README.md", "decisions/README.md", "decisions/monitor-de-notas-foundation-decisions.md", "policies/engineering_guardrails.md", "policies/query_path_guardrails.md", "policies/scope_subscope_governance.md", "policies/validation_evidence_policy.md", "todos/README.md"}
MODULES = {"events-and-classification.md", "treatments-and-history.md", "identity-and-team.md", "realtime-invalidation.md", "operational-monitoring.md", "runtime-and-deployment.md"}
REQUIRED_ANCHORS = ("Module Intent & Boundaries", "Core scope:", "Subscope:", "EnvironmentType:", "Out-of-scope guardrails:", "Dependency boundaries:", "Canonical Coverage Status:", "Purpose", "Owned", "Workflows", "Invariants", "Cross-Module")
REQUIRED_CONTRACT_SECTIONS = {"events-and-classification.md": ("Observed API Contract", "Ownership Invariant"), "treatments-and-history.md": ("Observed Treatment Contract",), "identity-and-team.md": ("Observed Authentication Contract",), "realtime-invalidation.md": ("Observed Realtime Message Contract",), "operational-monitoring.md": ("Observed Monitoring Contract",), "runtime-and-deployment.md": ("Observed Runtime Contract", "Observed Health Contract")}
REQUIRED_CONTRACT_TOKENS = {
    "events-and-classification.md": ("GET /eventos/exportar", "pagina", "1..200", "TODOS|ERRO|PENDENTE|SUCESSO|TRATADOS", "20,000", "{dados,meta}", "logradouro", "HTTP 200 `application/json`", "HTTP 200 `text/csv; charset=utf-8`", "{statusCode,erro,mensagem,caminho,timestamp}"),
    "treatments-and-history.md": ("PATCH /eventos/:refId/tratamento", "POST /eventos/tratar-lote", "RESOLVIDO|IGNORADO|PENDENTE", "1,000", "500", "HTTP 200 `application/json`", "{solicitados,aplicados,ignorados}"),
    "identity-and-team.md": ("POST /auth/login", "PATCH /usuarios/minha-senha", "PATCH /usuarios/:id", "DELETE /usuarios/:id", "ADMIN|GESTOR", "8..72", "HTTP 201 `application/json`", "HTTP 200 `application/json`", "{accessToken,expiraEm,usuario}"),
    "realtime-invalidation.md": ("signature/expiry only", "Content-Type: text/event-stream", "event:` field", "data:` field", "evento.novo|evento.tratado|heartbeat", "api|banco|polling|sistema", "continuously active", "optional parallel", "EventSource reconnection", "standard error body"),
    "operational-monitoring.md": ("MONITORAMENTO_TOKEN", "x-monitor-token", "maximum 200 characters", "1..1440", "atencao|critico", "application/json", "{status,cor,erros,pendentes,sucessos,total,ultima_verificacao,janela,limites,detalhe}", "HTTP 503"),
    "runtime-and-deployment.md": ("GET /api/v1/saude", "application/json", "{status,banco,em}", "degradado", "indisponivel", "HTTP 200", "external production `logs`", "derived, disposable, and non-authoritative", "backend/prisma/espelhar.ts", "backend/prisma/sql/002_logs_dev.sql"),
}
REQUIRED_ROUTE_CONTRACTS = {
    "events-and-classification.md": {
        "GET /eventos": (("common filters",), ("HTTP 200", "`application/json`"), ("`{dados,meta}`",)),
        "GET /eventos/resumo": (("common filters",), ("HTTP 200", "`application/json`"), ("`{total,erro,pendente,sucesso,tratados}`",)),
        "GET /eventos/produtos": (("none",), ("HTTP 200", "`application/json`"), ("array of `{nome,eventos,erros}`",)),
        "GET /eventos/exportar": (("common filters",), ("HTTP 200", "`text/csv; charset=utf-8`"), ("20,000 rows",)),
        "GET /eventos/:refId": (("correlation `refId`",), ("HTTP 200", "`application/json`"), ("`orientacao,origem,cliente,venda,produtor,historico,camposPendentes,payload,resposta`",)),
        "GET /eventos/:refId/payload": (("correlation `refId`",), ("HTTP 200", "`application/json`"), ("`{enviado,resposta}`",)),
    },
    "treatments-and-history.md": {
        "PATCH /eventos/:refId/tratamento": (("`situacao=RESOLVIDO|IGNORADO|PENDENTE`",), ("HTTP 200", "`application/json`"), ("complete event-detail projection",)),
        "POST /eventos/tratar-lote": (("`refIds`", "at most 500 entries"), ("HTTP 200", "`application/json`"), ("`{solicitados,aplicados,ignorados}`",)),
    },
    "identity-and-team.md": {
        "POST /auth/login": (("public",), ("HTTP 200", "`application/json`"), ("`{accessToken,expiraEm,usuario}`",)),
        "GET /auth/eu": (("normal JWT",), ("HTTP 200", "`application/json`"), ("current user summary",)),
        "GET /usuarios": (("`ADMIN|GESTOR`",), ("HTTP 200", "`application/json`"), ("array of users",)),
        "POST /usuarios": (("`ADMIN`",), ("HTTP 201", "`application/json`"), ("created user fields",)),
        "PATCH /usuarios/minha-senha": (("normal JWT",), ("HTTP 200", "`application/json`"), ("updated user fields",)),
        "PATCH /usuarios/:id": (("`ADMIN`",), ("HTTP 200", "`application/json`"), ("updated user fields",)),
        "DELETE /usuarios/:id": (("`ADMIN`",), ("HTTP 200", "`application/json`"), ("deactivated user fields",)),
    },
}
DELETE_PATHS = frozenset({
    "artifacts/analysis/leadshug-architecture-truth-and-legacy-boundaries-20260915.md", "artifacts/analysis/leadshug-executive-system-dossier-20260915.md", "artifacts/analysis/leadshug-system-analysis-20260915.md", "artifacts/feature-briefs/leadshug-pre-code-evolution-program-20260918.md", "artifacts/migration/claude-legacy-reconciliation-review.json", "artifacts/migration/claude-legacy-reconciliation-review.prompt.txt", "artifacts/migration/legacy-reconciliation-20260915.md", "artifacts/workspace-link-stabilization-20260915.md", "decisions/ST-01-foundation-lifecycle-decisions.md", "deterministic/.gitkeep", "modules/audit-and-history.md", "modules/identity-and-tenancy.md", "modules/inbox-and-conversations.md", "modules/integrations-and-channels.md", "policies/central_whatsapp_independent_legacy_policy.md", "policies/web_to_app_promotion_policy.md", "todos/active/features/TODO-leadshug-mode-specific-primary-and-secondary-color.md", "todos/active/features/TODO-leadshug-typebot-automation-integration.md", "todos/active/process/TODO-foundation-lifecycle-structural-validator.md", "todos/completed/features/TODO-delphi-shell-line-endings-and-cross-platform-validation.md", "todos/completed/features/TODO-leadshug-foundation-and-delphi-migration.md", "todos/completed/features/TODO-leadshug-identity-visual-screen-tests.md", "todos/completed/features/TODO-leadshug-initial-branding-and-unofficial-connection.md", "todos/completed/features/TODO-leadshug-post-onboarding-brand-settings.md", "todos/completed/features/TODO-leadshug-secondary-color-background-contract.md", "todos/completed/process/TODO-central-whatsapp-independent-legacy-policy.md", "todos/completed/process/TODO-ci-contract-and-migration-test-gates.md", "todos/completed/process/TODO-leadshug-architecture-truth-and-legacy-boundaries.md", "todos/completed/process/TODO-leadshug-authority-and-technology-documentation-rebase.md", "todos/completed/process/TODO-leadshug-executive-system-dossier.md", "todos/completed/process/TODO-leadshug-foundation-evolution-lifecycle.md", "todos/completed/process/TODO-leadshug-legacy-authority-migration-and-retirement.md", "todos/completed/process/TODO-leadshug-system-analysis-and-modernization-plan.md", "todos/completed/process/TODO-leadshug-workspace-link-stabilization.md",
})
EXPECTED_COMMON_FILES = frozenset({
    ".gitattributes", ".gitignore", "README.md", "artifacts/README.md", "artifacts/analysis/monitor-de-notas-foundation-cutover-map-20260924.md", "artifacts/analysis/monitor-de-notas-product-truth-20260924.md", "artifacts/publication-manifest.txt", "backlog/README.md", "contracts/README.md", "decisions/README.md", "decisions/monitor-de-notas-foundation-decisions.md", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/fixtures/valid-tree/README.md", "deterministic/tests/test_validate_foundation.py", "deterministic/validate_foundation.py", "domain_entities.md", "evolution_lifecycle.md", "local_packages.yaml", "modules/README.md", "modules/events-and-classification.md", "modules/identity-and-team.md", "modules/operational-monitoring.md", "modules/realtime-invalidation.md", "modules/runtime-and-deployment.md", "modules/treatments-and-history.md", "policies/engineering_guardrails.md", "policies/query_path_guardrails.md", "policies/scope_subscope_governance.md", "policies/validation_evidence_policy.md", "project_constitution.md", "project_mandate.md", "system_roadmap.md", "technology_baseline.md", "todos/README.md", "todos/ephemeral/.gitignore", "todos/ephemeral/.gitkeep", "todos/promotion_lane/.gitkeep",
})
TERMS = ("lead" + "shug", "what" + "sapp", "type" + "bot", "evol" + "ution", "bai" + "leys", "bell" + "uga", "bó" + "ora")
FROZEN_LEGACY_CONTENT_DIGEST = "1e6c89d8c5d8366180447acca336103b5a3429793295bf83f3b04641f2d7f3b4"
FROZEN_RAW_LEGACY_CONTENT_DIGEST = "36caf0bd79388f3b8f59db33402681cee3e8f575e0f0773af5c88e2db9fa68ca"
IDENTITY = {"README.md": ("Monitor de Notas", "uninotas-foundation", "foundation_documentation"), "project_mandate.md": ("Monitor de Notas", "MonitorDeNotas", "uninotas-foundation"), "project_constitution.md": ("Monitor de Notas",), "decisions/monitor-de-notas-foundation-decisions.md": ("Monitor de Notas", "MonitorDeNotas", "uninotas-foundation"), ACTIVE_TODO: ("Monitor de Notas", "MonitorDeNotas", "uninotas-foundation", "foundation_documentation"), COMPLETED_TODO: ("Monitor de Notas", "MonitorDeNotas", "uninotas-foundation", "foundation_documentation")}
IDENTITY_ANCHORS = {"README.md": "# Monitor de Notas Foundation", "decisions/monitor-de-notas-foundation-decisions.md": "| D-01 | Product name is Monitor de Notas; technical repository is MonitorDeNotas; documentation repository is uninotas-foundation. |"}
CANONICAL_ASSERTIONS = {"project_constitution.md": "Routerfy owns and writes the authoritative production `logs`; Monitor de Notas reads that external table only and writes only `monitor_usuarios` and `monitor_tratamentos`."}
JWT = re.compile("eyJ" + r"[A-Za-z0-9_-]{8,}" + r"\.[A-Za-z0-9_-]{8,}" + r"\.[A-Za-z0-9_-]{4,}")
PRIVATE = re.compile("-----" + "BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE " + "KEY-----")
CREDENTIAL_ASSIGNMENT = re.compile(r"(?im)^\s*(?:-\s*)?(?:\{\s*)?[\"']?[A-Za-z0-9_-]*(?:api[_-]?key|secret|password|token)[\"']?\s*[:=]\s*(?:[\"'][^\"'\r\n]{8,}[\"']|[A-Za-z0-9._~-]{8,})")
SERIALIZED_CREDENTIAL = re.compile(r"(?i)[\"'](?:[A-Za-z0-9_-]*(?:api[_-]?key|secret|password|token))[\"']\s*:\s*[\"'][^\"'\r\n]{8,}[\"']")
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
URL_CREDENTIAL = re.compile(r"(?i)[?&](?:[A-Za-z0-9_-]*(?:api[_-]?key|secret|password|token))=[A-Za-z0-9._~-]{8,}")
BEARER = re.compile(r"(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._~-]{8,}")
URI_CREDENTIAL = re.compile(r"(?i)(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqps?|https?)://[^/\s:@]+:[^@\s/]{4,}@")
ACCESS_KEY = re.compile("AK" + r"IA[0-9A-Z]{16}")
GITHUB_PROVIDER_PATTERN = re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{36,}|github_" + r"pat_[A-Za-z0-9_]{20,})")
OPENAI_PROVIDER_PATTERN = re.compile("s" + r"k-(?:proj-)?[A-Za-z0-9_-]{20,}")
GOOGLE_PROVIDER_PATTERN = re.compile("AI" + r"za[0-9A-Za-z_-]{35}")
CPF_PATTERN = re.compile(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)")
CPF_COMPACT_CANDIDATE = re.compile(r"(?<![A-Za-z0-9])\d{11}(?![A-Za-z0-9])")
PHONE_PATTERN = re.compile(r"(?<![A-Za-z0-9])(?:\+?55\s*)?\(?\d{2}\)?[\s.-]*(?:9\d{4}|[2-5]\d{3})[\s.-]?\d{4}(?![A-Za-z0-9])")
RAW_PERSON_PAYLOAD_PATTERN = re.compile(r"(?is)\{(?=[^{}]{0,1000}\"no" + r"me\"\s*:)(?=[^{}]{0,1000}\"(?:documento|cpf)\"\s*:)(?=[^{}]{0,1000}\"telefone\"\s*:)[^{}]{1,1000}\}")
CONFLICTING_LOG_OWNERSHIP = re.compile(r"(?i)(?:monitor\s+de\s+notas\s+(?:(?:can|may)\s+)?(?:own|owns|write|writes|mutate|mutates|manage|manages)\s+`?logs`?|`?logs`?\s+(?:(?:can|may)\s+be\s+)?(?:is\s+|are\s+)?(?:owned|written|writable|mutable)[^\n]{0,60}monitor\s+de\s+notas)")
CONFLICTING_IDENTITY = re.compile(r"(?i)(?:canonical\s+product|product\s+name)\s+(?:is|=)\s+(?!monitor\s+de\s+notas\b)[^\n]+")
ACTIVE_AUTHORITY_PHRASES = re.compile(r"(?i)(?:is\s+(?:the\s+)?(?:current|active|canonical)\s+(?:authority|architecture|foundation|product)|(?:is|remains?)\s+(?:the\s+)?source\s+of\s+truth|remains?\s+(?:the\s+)?active\s+authority|(?:owns|governs)\s+(?:this|the)\s+(?:foundation|product|architecture)|é\s+(?:a\s+)?(?:autoridade\s+(?:atual|ativa|canônica)|fonte\s+da\s+verdade|produto\s+(?:atual|canônico))|permanece\s+(?:a\s+)?autoridade\s+ativa|(?:possui|governa)\s+(?:esta|o|a)\s+(?:foundation|produto|arquitetura))")

def repository_entries(root): return [p for p in Path(root).rglob("*") if ".git" not in p.parts]
def files(root): return {p.relative_to(root).as_posix(): p for p in repository_entries(root) if p.is_file() and not p.is_symlink()}
def headings(text): return {line.lstrip("#").strip().lower() for line in text.splitlines() if line.startswith("#")}
def normalized_line_hash(line): return hashlib.sha256(" ".join(line.split()).casefold().encode("utf-8")).hexdigest()
def term_occurs(term, text):
    folded = text.casefold()
    if term.casefold() == "evolution":
        folded = re.sub(r"(?<![\w])evolution_lifecycle(?:\.md)?(?![\w./-])", "", folded)
    return term.casefold() in folded
def section_occurrences(text):
    section, found = "Preamble", {}
    for line in text.splitlines():
        if line.startswith("## "): section = line[3:].strip()
        for term in TERMS:
            if term_occurs(term, line): found.setdefault((term.casefold(), section), []).append(normalized_line_hash(line))
    return {key: sorted(values) for key, values in found.items()}

def raw_legacy_content_digest(text):
    section, payload = "Preamble", []
    for line in text.splitlines():
        if line.startswith("## "): section = line[3:].strip()
        for term in TERMS:
            if term_occurs(term, line): payload.append((term.casefold(), section, line))
    return hashlib.sha256(json.dumps(sorted(payload), ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()

def markdown_table_cells(line):
    cells, buffer, in_code = [], [], False
    for character in line:
        if character == "`": in_code = not in_code; buffer.append(character)
        elif character == "|" and not in_code: cells.append("".join(buffer).strip()); buffer = []
        else: buffer.append(character)
    cells.append("".join(buffer).strip())
    if cells and not cells[0]: cells = cells[1:]
    if cells and not cells[-1]: cells = cells[:-1]
    return cells

def has_valid_compact_cpf(text):
    for match in CPF_COMPACT_CANDIDATE.finditer(text):
        digits = [int(value) for value in match.group(0)]
        if len(set(digits)) == 1: continue
        first = (sum(digits[index] * (10 - index) for index in range(9)) * 10) % 11
        second = (sum(digits[index] * (11 - index) for index in range(10)) * 10) % 11
        if (0 if first == 10 else first) == digits[9] and (0 if second == 10 else second) == digits[10]: return True
    return False

def lifecycle(tree, errors):
    present = [path for path in LIFECYCLES if path in tree]
    if len(present) != 1: errors.append("governing TODO lifecycle must contain exactly one active or completed path"); return None, None
    return present[0], LIFECYCLES[present[0]]

def ledger_entries(tree, todo_path, expected_lifecycle, errors):
    keys = {"path", "term", "context_kind", "section", "reason", "owner", "lifecycle", "line_hashes"}
    try:
        data = json.loads(tree["deterministic/legacy_reference_exceptions.json"].read_text(encoding="utf-8"))
        todo_text = tree[todo_path].read_text(encoding="utf-8")
        actual, rows = section_occurrences(todo_text), {}
        for line in todo_text.splitlines():
            if any(term_occurs(term, line) for term in TERMS) and ACTIVE_AUTHORITY_PHRASES.search(line):
                errors.append("active legacy authority claim cannot be ledgered")
        if not isinstance(data, list) or not data: raise ValueError
        for row in data:
            if set(row) != keys or any(not isinstance(row[k], str) or not row[k].strip() for k in keys - {"line_hashes"}): raise ValueError
            key = (row["term"].casefold(), row["section"])
            hashes = row["line_hashes"]
            if "*" in row["path"] + row["term"] or row["path"] != todo_path or row["context_kind"] != "historical_migration_record" or row["lifecycle"] != expected_lifecycle or key in rows or not isinstance(hashes, list) or not hashes or hashes != sorted(hashes) or any(not re.fullmatch(r"[0-9a-f]{64}", value) for value in hashes): raise ValueError
            rows[key] = hashes
        if rows != actual: raise ValueError
        frozen_payload = sorted((row["term"].casefold(), row["section"], tuple(row["line_hashes"])) for row in data)
        frozen_digest = hashlib.sha256(json.dumps(frozen_payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
        if frozen_digest != FROZEN_LEGACY_CONTENT_DIGEST: raise ValueError
        if raw_legacy_content_digest(todo_text) != FROZEN_RAW_LEGACY_CONTENT_DIGEST: raise ValueError
    except (KeyError, ValueError, json.JSONDecodeError): errors.append("invalid legacy exception ledger")

def scope_policy(tree, errors):
    try:
        text = tree["policies/scope_subscope_governance.md"].read_text(encoding="utf-8")
        contract = json.loads(re.search(r"```json\s*(\{.*?\})\s*```", text, re.S).group(1))
        expected = {"core_scope": "monitor-de-notas", "subscopes": sorted(n[:-3] for n in MODULES), "environment_type": "landlord", "landlord_role": "paced_technical_adapter", "business_tenancy": False}
        if contract != expected: raise ValueError
        return contract
    except (KeyError, AttributeError, ValueError, json.JSONDecodeError): errors.append("scope policy mismatch"); return None

def validate(root):
    root, errors = Path(root), []
    entries = repository_entries(root)
    errors += [f"symlink forbidden in publication tree: {p.relative_to(root).as_posix()}" for p in entries if p.is_symlink()]
    tree = files(root)
    todo_path, expected_lifecycle = lifecycle(tree, errors)
    required = ROOT_FILES | SUPPORT_FILES | {"modules/README.md", "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"}
    if todo_path: required.add(todo_path)
    errors += [f"missing required file: {p}" for p in required - set(tree)]
    actual_modules = {Path(p).name for p in tree if p.startswith("modules/") and p != "modules/README.md"}
    if actual_modules != MODULES: errors.append("exact six-module set mismatch")
    for path in DELETE_PATHS & set(tree): errors.append(f"forbidden deleted path present: {path}")
    if "modules/README.md" in tree:
        text = tree["modules/README.md"].read_text(encoding="utf-8")
        if {n for n in MODULES if f"({n})" in text} != MODULES or any(text.count(f"({n})") != 1 for n in MODULES): errors.append("module index/canonical owner mismatch")
    policy = scope_policy(tree, errors)
    for name in MODULES:
        path = tree.get("modules/" + name)
        if not path: continue
        text = path.read_text(encoding="utf-8")
        contract_bodies = []
        for anchor in REQUIRED_ANCHORS:
            if anchor not in text: errors.append(f"missing module anchor {anchor}: {name}")
        for section in REQUIRED_CONTRACT_SECTIONS[name]:
            body = re.search(rf"^## {re.escape(section)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
            if not body or not body.group(1).strip(): errors.append(f"missing module contract section {section}: {name}")
            else: contract_bodies.append(body.group(1))
        contract_text = "\n".join(contract_bodies)
        for token in REQUIRED_CONTRACT_TOKENS.get(name, ()):
            if token not in contract_text: errors.append(f"missing module contract semantic {token}: {name}")
        for route, column_tokens in REQUIRED_ROUTE_CONTRACTS.get(name, {}).items():
            route_rows = [markdown_table_cells(line) for line in contract_text.splitlines() if line.startswith("|") and markdown_table_cells(line)[:1] == [f"`{route}`"]]
            if len(route_rows) != 1 or len(route_rows[0]) != 4 or any(token not in route_rows[0][column] for column, tokens in enumerate(column_tokens, start=1) for token in tokens): errors.append(f"route contract mismatch {route}: {name}")
        if not policy or re.search(r"\*\*Core scope:\*\* `monitor-de-notas`", text) is None or re.search(rf"\*\*Subscope:\*\* `{re.escape(name[:-3])}`", text) is None or "`landlord`" not in text: errors.append(f"scope/subscope mismatch: {name}")
    if todo_path: ledger_entries(tree, todo_path, expected_lifecycle, errors)
    for owner, tokens in IDENTITY.items():
        if owner in tree and any(token not in tree[owner].read_text(encoding="utf-8") for token in tokens): errors.append(f"canonical identity mismatch: {owner}")
    for owner, anchor in IDENTITY_ANCHORS.items():
        if owner in tree and anchor not in tree[owner].read_text(encoding="utf-8"): errors.append(f"canonical identity anchor mismatch: {owner}")
    if "README.md" in tree:
        h1 = [line.strip() for line in tree["README.md"].read_text(encoding="utf-8").splitlines() if line.startswith("# ")]
        if h1 != ["# Monitor de Notas Foundation"]: errors.append("canonical identity heading mismatch: README.md")
    for owner, assertion in CANONICAL_ASSERTIONS.items():
        if owner in tree and assertion not in tree[owner].read_text(encoding="utf-8"): errors.append(f"canonical ownership mismatch: {owner}")
    decisions = tree.get("decisions/monitor-de-notas-foundation-decisions.md")
    if decisions:
        rows = re.findall(r"^\|\s*(D-0[1-5])\s*\|\s*(.*?)\s*\|", decisions.read_text(encoding="utf-8"), re.M)
        if [key for key, _ in rows] != ["D-01", "D-02", "D-03", "D-04", "D-05"] or "Routerfy owns and writes the authoritative production `logs`; Monitor de Notas reads that external table only and writes only its application tables." not in dict(rows).get("D-04", ""): errors.append("canonical decision table mismatch")
    for relative, path in tree.items():
        text = path.read_text(encoding="utf-8", errors="replace")
        if JWT.search(text) or PRIVATE.search(text) or CREDENTIAL_ASSIGNMENT.search(text) or SERIALIZED_CREDENTIAL.search(text) or URL_CREDENTIAL.search(text) or BEARER.search(text) or URI_CREDENTIAL.search(text) or ACCESS_KEY.search(text) or GITHUB_PROVIDER_PATTERN.search(text) or OPENAI_PROVIDER_PATTERN.search(text) or GOOGLE_PROVIDER_PATTERN.search(text) or CPF_PATTERN.search(text) or has_valid_compact_cpf(text) or PHONE_PATTERN.search(text) or RAW_PERSON_PAYLOAD_PATTERN.search(text) or EMAIL.search(text): errors.append(f"privacy pattern in {relative}")
        if relative not in {todo_path, "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"} and CONFLICTING_LOG_OWNERSHIP.search(text): errors.append(f"contradictory external ownership claim in {relative}")
        if relative not in {todo_path, "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"} and CONFLICTING_IDENTITY.search(text): errors.append(f"contradictory canonical identity claim in {relative}")
        for _, target in ([] if path.suffix == ".py" else re.findall(r"\[([^]]+)\]\(([^)]+)\)", text)):
            target, _, anchor = target.partition("#")
            if "://" in target or target.startswith("mailto:"): continue
            dest = (path.parent / target).resolve() if target else path
            if not dest.is_file(): errors.append(f"broken relative link in {relative}: {target}")
            elif anchor and anchor.lower().replace("-", " ") not in headings(dest.read_text(encoding="utf-8", errors="replace")): errors.append(f"broken anchor in {relative}: {anchor}")
        if relative not in {todo_path, "artifacts/publication-manifest.txt", "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"} and any(term_occurs(term, text) for term in TERMS): errors.append(f"legacy authority/reference in {relative}")
    manifest = tree.get("artifacts/publication-manifest.txt")
    if manifest:
        expected_tree = EXPECTED_COMMON_FILES | ({todo_path} if todo_path else set())
        if set(tree) != expected_tree: errors.append("frozen lifecycle tree mismatch")
        listed = [x.strip() for x in manifest.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]
        if listed != sorted(expected_tree): errors.append("publication manifest must uniquely and exactly match frozen lifecycle tree")
    return errors

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--root", required=True); args = parser.parse_args(); errors = validate(args.root)
    if errors: print("Foundation validation failed:\n" + "\n".join("- " + e for e in errors)); raise SystemExit(1)
    print("Foundation validation passed.")
if __name__ == "__main__": main()
