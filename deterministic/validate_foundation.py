#!/usr/bin/env python3
"""Fail-closed validator for the UniNotas Foundation cutover."""
import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
from urllib.parse import unquote, urlsplit
from pathlib import Path

FULL_TREE_SCAN_COUNT = 0

def reset_full_tree_scan_count():
    global FULL_TREE_SCAN_COUNT
    FULL_TREE_SCAN_COUNT = 0

ACTIVE_TODO = "todos/active/process/TODO-uninotas-canonical-foundation-transition.md"
COMPLETED_TODO = "todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"
LIFECYCLES = {ACTIVE_TODO: "active", COMPLETED_TODO: "completed"}
ROOT_FILES = {"README.md", "project_mandate.md", "project_constitution.md", "domain_entities.md", "technology_baseline.md", "evolution_lifecycle.md", "system_roadmap.md", "local_packages.yaml"}
SUPPORT_FILES = {"artifacts/README.md", "artifacts/publication-manifest.txt", "backlog/README.md", "contracts/README.md", "decisions/README.md", "decisions/uninotas-foundation-decisions.md", "policies/engineering_guardrails.md", "policies/query_path_guardrails.md", "policies/scope_subscope_governance.md", "policies/validation_evidence_policy.md", "todos/README.md"}
FROZEN_PUBLICATION_PATHS = {".gitattributes", "deterministic/tests/fixtures/valid-tree/README.md"}
REQUIRED_ANCHORS = ("Module Intent & Boundaries", "Core scope:", "Subscope:", "EnvironmentType:", "Out-of-scope guardrails:", "Dependency boundaries:", "Canonical Coverage Status:", "Purpose", "Owned", "Workflows", "Invariants", "Cross-Module")
REQUIRED_CONTRACT_SECTIONS = {"events-and-classification.md": ("Observed API Contract", "Ownership Invariant"), "treatments-and-history.md": ("Observed Treatment Contract",), "identity-and-team.md": ("Observed Authentication Contract",), "realtime-invalidation.md": ("Observed Realtime Message Contract",), "operational-monitoring.md": ("Observed Monitoring Contract",), "runtime-and-deployment.md": ("Observed Runtime Contract", "Observed Health Contract")}
OBSERVED_RUNTIME_MODULES = frozenset(REQUIRED_CONTRACT_SECTIONS)
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
TERMS = ("lead" + "shug", "what" + "sapp", "type" + "bot", "evol" + "ution", "bai" + "leys", "bell" + "uga", "bó" + "ora")
FROZEN_LEGACY_CONTENT_DIGEST = "29ff45d9a2ad3a231bb8d8653bb555aff9404622f416f87d5f6bd9f009216a67"
FROZEN_RAW_LEGACY_CONTENT_DIGEST = "5f5df51409a3e4933271b59e6715fff0e48c40ac0011c6dd46d7bfcc0b53c89b"
FROZEN_INITIAL_CAPABILITY_IDENTITY_DIGEST = "180845cdb4546be1639c12bf61f0765ed05bad021a3c14011422c1f02bf83030"
FROZEN_INITIAL_CAPABILITY_IDS = {"note_read_model","integration_error_read_model","operational_workflow","authentication","team_profiles","legacy_log_invalidation","legacy_log_monitoring","runtime_topology","health_read","fiscal_document_read"}
IDENTITY = {"README.md": ("UniNotas", "uninotas", "MonitorDeNotas"), "project_mandate.md": ("UniNotas", "MonitorDeNotas", "uninotas-foundation"), "project_constitution.md": ("UniNotas", "Namespaces: nestjs, react, vite, postgresql, prisma, docker, railway"), "decisions/uninotas-foundation-decisions.md": ("UniNotas", "D-06", "D-11"), ACTIVE_TODO: ("UniNotas", "MonitorDeNotas", "uninotas-foundation")}
IDENTITY_ANCHORS = {"README.md": "# UniNotas Foundation", "decisions/uninotas-foundation-decisions.md": "| D-06 | UniNotas is canonical"}
CANONICAL_ASSERTIONS = {"project_constitution.md": "Smart Notas is the target-planned source of truth for fiscal notes and documents."}
FISCAL_CONTEXT_ASSERTIONS = {
    "project_constitution.md": "Unifast and Prosperar are distinct `FiscalIssuerContext` values, not tenants.",
    "policies/scope_subscope_governance.md": "Unifast and Prosperar are `FiscalIssuerContext` values, not tenants.",
}
TARGET_OWNER_CAPABILITIES = {
    "fiscal-notes-and-documents": {"note_read_model", "fiscal_document_read"},
    "integration-error-occurrences": {"integration_error_read_model"},
    "operational-cases": {"operational_workflow"},
}
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
RETIRED_ROUTERFY_LOG_OWNERSHIP = re.compile(r"(?i)(?:externally\s+owned\s+Routerfy\s+record|ownership\s+from\s+Routerfy|Routerfy\s+remains?\s+owner\s+of\s+persisted\s+source\s+rows)")
CURRENT_TRUTH_SURFACES = {"project_constitution.md", "domain_entities.md", "modules/events-and-classification.md"}
CONFLICTING_IDENTITY = re.compile(r"(?i)(?:canonical\s+product|product\s+name)\s+(?:is|=)\s+(?!uninotas\b)[^\n]+")
ACTIVE_AUTHORITY_PHRASES = re.compile(r"(?i)(?:is\s+(?:the\s+)?(?:current|active|canonical)\s+(?:authority|architecture|foundation|product)|(?:is|remains?)\s+(?:the\s+)?source\s+of\s+truth|remains?\s+(?:the\s+)?active\s+authority|(?:owns|governs)\s+(?:this|the)\s+(?:foundation|product|architecture)|é\s+(?:a\s+)?(?:autoridade\s+(?:atual|ativa|canônica)|fonte\s+da\s+verdade|produto\s+(?:atual|canônico))|permanece\s+(?:a\s+)?autoridade\s+ativa|(?:possui|governa)\s+(?:esta|o|a)\s+(?:foundation|produto|arquitetura))")

def repository_entries(root):
    root = Path(root)
    def published(path):
        parts=path.relative_to(root).parts
        return ".git" not in parts and parts[:2] != ("artifacts","tmp")
    return [path for path in root.rglob("*") if published(path)]
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

# UniNotas extension: isolated fiscal privacy and capability-registry semantics.
CNPJ_CANDIDATE = re.compile(r"(?<!\d)(?:\d{14}|\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})(?!\d)")
PLACEHOLDER = re.compile(r"^(?:<redacted>|<placeholder>|REDACTED|\$\{[A-Z][A-Z0-9_]*\})$")
CREDENTIAL_KEYS = dict((key, diagnostic) for key, diagnostic in (
    ("smart_notas_unifast_" + "token", "token credential"),
    ("smart_notas_prosperar_" + "token", "token credential"),
    ("smart_notas_unifast_" + "cnpj", "CNPJ credential"),
    ("smart_notas_prosperar_" + "cnpj", "CNPJ credential"),
    ("author" + "ization", "authorization credential"),
    ("bearer_" + "token", "authorization credential"),
))
PROVIDER_ID_KEYS = {"id_interno", "provider_id", "smart_notas_note_id"}
DOCUMENT_URL_KEYS = {"pdf_url", "xml_url", "danfe_url", "document_url", "smart_notas_document_url"}
PRIVACY_ESCAPE = re.compile(r"\\(?:u([0-9a-fA-F]{4})|U([0-9a-fA-F]{8})|x([0-9a-fA-F]{2}))")

def decode_privacy_escapes(value):
    def decode_escape(match):
        digits = next(group for group in (match.group(1), match.group(2), match.group(3)) if group is not None)
        try: return chr(int(digits, 16))
        except (ValueError, OverflowError): return match.group(0)
    return PRIVACY_ESCAPE.sub(decode_escape, value)

def normalize_privacy_candidate_text(value):
    value = unicodedata.normalize("NFKC", decode_privacy_escapes(value))
    return "".join(character for character in value if unicodedata.category(character) not in {"Cf", "Mn", "Me"})

def has_valid_cnpj(text):
    for match in CNPJ_CANDIDATE.finditer(normalize_privacy_candidate_text(text)):
        digits = [int(value) for value in re.sub(r"\D", "", match.group(0))]
        if len(digits) != 14 or len(set(digits)) == 1: continue
        def check(weights):
            remainder = sum(value * weight for value, weight in zip(digits, weights)) % 11
            return 0 if remainder < 2 else 11 - remainder
        if check((5,4,3,2,9,8,7,6,5,4,3,2)) == digits[12] and check((6,5,4,3,2,9,8,7,6,5,4,3,2)) == digits[13]: return True
    return False

def normalize_privacy_key(key):
    key = key.strip()
    key = decode_privacy_escapes(key)
    key = "".join(
        character for character in key
        if ord(character) < 128 or unicodedata.category(character) not in {"Cc", "Cf", "Mn", "Me", "Zl", "Zp", "Zs"}
    )
    key = "".join(character for character in unicodedata.normalize("NFKC", key) if ord(character) < 128).strip()
    while len(key) >= 2 and key[0] == key[-1] and key[0] in "'\"`": key = key[1:-1].strip()
    key = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", key)
    return re.sub(r"[\s_-]+", "_", key).strip("_").casefold()

def normalize_privacy_value(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"`": value = value[1:-1]
    return unquote(value.strip())

def flow_mapping_pairs(text, stats=None):
    stats = stats if stats is not None else {}
    stats.update(characters_scanned=0, key_chars_materialized=0, value_chars_materialized=0)
    sensitive_keys = set(CREDENTIAL_KEYS) | PROVIDER_ID_KEYS | DOCUMENT_URL_KEYS
    stack, quote, escaped, index = [], None, False, 0
    matching = {"}": "{", "]": "[", ")": "("}

    def finish_pair(frame, end):
        colon = frame.get("colon")
        if colon is None or frame.get("key_has_nested"): return None
        key_start, key_end = frame["entry_start"], colon
        while key_start < key_end and text[key_start].isspace(): key_start += 1
        while key_end > key_start and text[key_end - 1].isspace(): key_end -= 1
        raw_key = text[key_start:key_end]
        stats["key_chars_materialized"] += len(raw_key)
        if normalize_privacy_key(raw_key) not in sensitive_keys: return None

        value_start, value_end = colon + 1, end
        while value_start < value_end and text[value_start].isspace(): value_start += 1
        while value_end > value_start and text[value_end - 1].isspace(): value_end -= 1
        if value_end - value_start > 512:
            raw_value = "<concrete-structured-or-oversized-value>"
        else:
            raw_value = text[value_start:value_end]
        stats["value_chars_materialized"] += len(raw_value)
        return raw_key, raw_value

    while index < len(text):
        character = text[index]
        stats["characters_scanned"] += 1
        if quote:
            if escaped:
                escaped = False
            elif character == "\\" and quote == '"':
                escaped = True
            elif character == quote:
                if quote == "'" and index + 1 < len(text) and text[index + 1] == "'":
                    index += 1
                    stats["characters_scanned"] += 1
                else:
                    quote = None
            index += 1
            continue

        if character in "'\"":
            quote = character
        elif character == "{":
            if stack and stack[-1]["kind"] == "{" and stack[-1]["colon"] is None:
                stack[-1]["key_has_nested"] = True
            stack.append({"kind": "{", "entry_start": index + 1, "colon": None, "key_has_nested": False})
        elif character in "[(":
            if stack and stack[-1]["kind"] == "{" and stack[-1]["colon"] is None:
                stack[-1]["key_has_nested"] = True
            stack.append({"kind": character})
        elif character in matching and stack and stack[-1]["kind"] == matching[character]:
            frame = stack.pop()
            if character == "}":
                pair = finish_pair(frame, index)
                if pair: yield pair
        elif character == ":" and stack and stack[-1]["kind"] == "{" and stack[-1]["colon"] is None:
            stack[-1]["colon"] = index
        elif character == "," and stack and stack[-1]["kind"] == "{":
            pair = finish_pair(stack[-1], index)
            if pair: yield pair
            stack[-1]["entry_start"], stack[-1]["colon"], stack[-1]["key_has_nested"] = index + 1, None, False
        index += 1

def privacy_pairs(text):
    class JsonObjectPairs(list): pass
    try: structured = json.loads(text, object_pairs_hook=JsonObjectPairs)
    except (json.JSONDecodeError, TypeError): structured = None
    def structured_pairs(value):
        if isinstance(value, JsonObjectPairs):
            for key, item in value:
                yield key, item if isinstance(item, str) else json.dumps(item, sort_keys=True)
                yield from structured_pairs(item)
        elif isinstance(value, list):
            for item in value: yield from structured_pairs(item)
    if structured is not None: yield from structured_pairs(structured)
    yield from flow_mapping_pairs(text)
    for line in text.splitlines():
        line = "".join(character for character in line if unicodedata.category(character) not in {"Cc","Cf"} or character in "\t")
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = markdown_table_cells(stripped)
            for index in range(len(cells) - 1): yield cells[index], cells[index + 1]
            continue
        match = re.match(r'^\s*"(?P<key>[^"]+)"\s*:\s*(?P<value>.*?)(?:,)?\s*$', line)
        if not match: match = re.match(r"^\s*(?:export\s+)?(?P<key>[^=\r\n]+?)\s*=\s*(?P<value>.*)$", line)
        if not match: match = re.match(r"^\s*(?:-\s*)?(?P<key>[^:\r\n]+?)\s*:\s*(?P<value>.*)$", line)
        if match: yield match.group("key"), match.group("value")

def is_allowed_privacy_value(value):
    if not value or PLACEHOLDER.fullmatch(value): return True
    parsed = urlsplit(value)
    return parsed.scheme.casefold() == "https" and parsed.netloc.casefold() == "example.invalid"

def private_context_diagnostic(text):
    if has_valid_cnpj(text): return "valid CNPJ value"
    for raw_key, raw_value in privacy_pairs(text):
        key, value = normalize_privacy_key(raw_key), normalize_privacy_value(raw_value)
        if key in CREDENTIAL_KEYS and not is_allowed_privacy_value(value): return CREDENTIAL_KEYS[key]
        if key in PROVIDER_ID_KEYS and not is_allowed_privacy_value(value): return "concrete provider identifier context"
        if key in DOCUMENT_URL_KEYS and not is_allowed_privacy_value(value): return "captured document URL context"
    return None

def private_context_diagnostics(text):
    """Return every recognized contextual privacy violation, once per family."""
    diagnostics=[]
    if has_valid_cnpj(text): diagnostics.append("valid CNPJ value")
    for raw_key, raw_value in privacy_pairs(text):
        key, value = normalize_privacy_key(raw_key), normalize_privacy_value(raw_value)
        if key in CREDENTIAL_KEYS and not is_allowed_privacy_value(value): diagnostics.append(CREDENTIAL_KEYS[key])
        if key in PROVIDER_ID_KEYS and not is_allowed_privacy_value(value): diagnostics.append("concrete provider identifier context")
        if key in DOCUMENT_URL_KEYS and not is_allowed_privacy_value(value): diagnostics.append("captured document URL context")
    return sorted(set(diagnostics))

def has_basic_privacy(text):
    patterns=(JWT,PRIVATE,CREDENTIAL_ASSIGNMENT,SERIALIZED_CREDENTIAL,URL_CREDENTIAL,BEARER,URI_CREDENTIAL,ACCESS_KEY,GITHUB_PROVIDER_PATTERN,OPENAI_PROVIDER_PATTERN,GOOGLE_PROVIDER_PATTERN,CPF_PATTERN,PHONE_PATTERN,RAW_PERSON_PAYLOAD_PATTERN)
    concrete_email=any(not match.group(0).casefold().endswith("@example.invalid") for match in EMAIL.finditer(text))
    return any(pattern.search(text) for pattern in patterns) or has_valid_compact_cpf(text) or concrete_email

def validate_capability_registry(modules, transitions, baseline_capabilities, identity_ledger, catalog=None):
    errors, owners, planners, chains, known = [], {}, {}, {}, {row.get("module_id") for row in modules}
    catalog_ids = {row.get("module_id") for row in catalog} if isinstance(catalog,list) else known
    for module in modules:
        owned, planned = module.get("owned_capabilities", []), module.get("planned_capabilities", [])
        if module.get("status") not in {"current_runtime", "target_planned", "retired"}: errors.append("runtime authority state is invalid")
        if len(owned) != len(set(owned)): errors.append("owned_capabilities contains duplicate capability id")
        if len(planned) != len(set(planned)): errors.append("planned_capabilities contains duplicate capability id")
        if set(owned) & set(planned): errors.append("owned_capabilities intersects planned_capabilities")
        if module.get("status") == "current_runtime" and not owned: errors.append("current_runtime module must own at least one capability")
        if module.get("status") == "target_planned" and owned: errors.append("target_planned module cannot own capability")
        if module.get("status") == "target_planned" and not planned: errors.append("target_planned module must plan at least one capability")
        if module.get("status") not in {"current_runtime","target_planned","retired"} and not owned and not planned: errors.append("active module has neither owned nor planned capabilities")
        if module.get("status") == "retired" and (owned or planned): errors.append("retired module remains active, owned, or planned")
        for capability in owned: owners.setdefault(capability, []).append(module.get("module_id"))
        for capability in planned: planners.setdefault(capability, []).append(module.get("module_id"))
    if any(len(value) > 1 for value in owners.values()): errors.append("capability has multiple current owners")
    if any(len(value) > 1 for value in planners.values()): errors.append("capability has multiple planned successors")
    seen = set()
    for row in transitions:
        tid, capability = row.get("transition_id"), row.get("capability_id")
        if tid in seen: errors.append("transition_id is not unique")
        seen.add(tid); chains.setdefault(capability, []).append(row)
        if row.get("origin") not in {"new", "transferred"}: errors.append("capability transition origin is invalid")
        if row.get("state") not in {"planned", "completed"}: errors.append("capability transition state is invalid")
        if row.get("successor") not in catalog_ids or row.get("predecessor") is not None and row.get("predecessor") not in catalog_ids: errors.append("transition references unknown module")
        if row.get("origin") == "new":
            if row.get("sequence") != 1: errors.append("origin new is valid only at sequence one")
            if row.get("predecessor") is not None: errors.append("new capability predecessor must be null")
            if row.get("state") == "planned" and capability in owners: errors.append("new planned capability already has an owner")
        elif row.get("predecessor") is None: errors.append("transferred capability requires a predecessor")
    for capability, rows in chains.items():
        ordered = sorted(rows, key=lambda row: row.get("sequence", 0))
        if [row.get("sequence") for row in ordered] != list(range(1, len(ordered) + 1)): errors.append("capability transition sequence is not contiguous")
        predecessors = [row.get("predecessor") for row in ordered if row.get("predecessor") is not None]
        if len(predecessors) != len(set(predecessors)): errors.append("capability transition chain fork")
        chain_nodes = set()
        for row in ordered:
            predecessor, successor = row.get("predecessor"), row.get("successor")
            if predecessor is not None:
                chain_nodes.add(predecessor)
            if successor in chain_nodes: errors.append("capability transition chain cycle")
            chain_nodes.add(successor)
        for previous, current in zip(ordered, ordered[1:]):
            if current.get("predecessor") != previous.get("successor"): errors.append("transition predecessor does not match prior successor")
        terminal = ordered[-1] if ordered else None
        if any(row.get("state") != "completed" for row in ordered[:-1]): errors.append("nonterminal transition must be completed")
        for row in ordered:
            if row.get("state") == "planned" and row.get("origin") != "new" and row.get("predecessor") not in {module.get("module_id") for module in modules if module.get("status") == "current_runtime" and row.get("capability_id") in module.get("owned_capabilities", [])}: errors.append("planned transfer predecessor is not the current owner")
        if terminal and terminal.get("state") == "completed":
            if capability in planners: errors.append("completed capability retains planned membership")
            if not owners.get(capability): errors.append("terminal completed capability has no sole successor owner")
            elif owners[capability] != [terminal.get("successor")]: errors.append("terminal completed successor is not sole current owner")
        if terminal and terminal.get("state") == "planned" and terminal.get("successor") not in planners.get(capability, []): errors.append("terminal planned successor lacks planned membership")
    for capability, planned_modules in planners.items():
        rows = chains.get(capability, [])
        terminal = max(rows, key=lambda row: row.get("sequence", 0), default=None)
        if not terminal or terminal.get("state") != "planned" or terminal.get("successor") not in planned_modules: errors.append("planned membership has no matching terminal planned transition")
    if set(baseline_capabilities) - (set(owners) | set(planners) | set(chains)): errors.append("baseline capability is missing from governed ownership or transition state")
    baseline = set(baseline_capabilities)
    baseline_identity_ids = {row.get("capability_id") for row in identity_ledger if row.get("origin") == "baseline"}
    if baseline_identity_ids and baseline_identity_ids != baseline: errors.append("baseline capability id is immutable and aliases are forbidden")
    baseline_owners = {row.get("capability_id"):row.get("baseline_owner") for row in identity_ledger if row.get("origin") == "baseline"}
    for capability, baseline_owner in baseline_owners.items():
        ordered = sorted(chains.get(capability, []), key=lambda row: row.get("sequence", 0))
        if not ordered and owners.get(capability) != [baseline_owner]: errors.append("baseline capability without transition must remain with baseline owner")
        if ordered and ordered[0].get("predecessor") != baseline_owner: errors.append("baseline capability transition must start from baseline owner")
    new_capabilities = {capability for capability, rows in chains.items() if any(row.get("origin") == "new" and row.get("sequence") == 1 for row in rows)}
    if baseline & new_capabilities: errors.append("capability identity cannot have both baseline and new origins")
    if set(owners) - baseline - new_capabilities: errors.append("non-baseline capability requires origin new transition history")
    identifiers = [row.get("capability_id") for row in identity_ledger]
    if len(identifiers) != len(set(identifiers)): errors.append("capability identity ledger id is not unique")
    return errors

def canonical_identity_digest(identities):
    """Stable digest independent of JSON whitespace and key order."""
    normalized=[]
    for row in identities:
        if not isinstance(row,dict): raise ValueError("capability identity row schema is invalid")
        required={"capability_id","origin","baseline_owner"} if row.get("origin")=="baseline" else {"capability_id","origin","origin_transition_id"} if row.get("origin")=="new" else set()
        if not required or set(row)!=required or any(not isinstance(row.get(key),str) or not row.get(key) for key in required): raise ValueError("capability identity row schema is invalid")
        normalized.append({key:row[key] for key in sorted(required)})
    normalized.sort(key=lambda row:row["capability_id"])
    return hashlib.sha256(json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()

def validate_initial_identity_digest(identities, expected_digest):
    if canonical_identity_digest(identities) != expected_digest:
        return ["frozen initial capability identity digest mismatch"]
    return []

def validate_identity_history(repo, ledger_path="deterministic/capability_identity_ledger.json", stats=None, *, expected_genesis=None, allow_pending_genesis=False):
    """Read only first-parent ledger versions; reject shallow/replaced/mutated lineage."""
    errors=[]
    calls=0
    def run(*args):
        nonlocal calls
        calls += 1
        return subprocess.run(["git","-C",str(repo),*args],text=True,capture_output=True)
    git_dir=Path(repo)/".git"
    if git_dir.is_file():
        marker=git_dir.read_text(encoding="utf-8",errors="ignore").strip()
        if marker.startswith("gitdir:"): git_dir=(Path(repo)/marker[7:].strip()).resolve()
    packed=git_dir/"packed-refs"; grafts=git_dir/"info/grafts"; replacements=git_dir/"refs/replace"
    if ((git_dir/"shallow").is_file() and (git_dir/"shallow").stat().st_size) or (grafts.is_file() and grafts.read_text(encoding="utf-8",errors="ignore").strip()) or (replacements.is_dir() and any(replacements.rglob("*"))) or (packed.is_file() and " refs/replace/" in packed.read_text(encoding="utf-8",errors="ignore")): return ["capability identity history is incomplete or untrusted"]
    head=run("rev-parse","HEAD").stdout.strip()
    history=run("log","--first-parent","--format=%H","--",ledger_path)
    commits=[line for line in history.stdout.splitlines() if line]
    if not commits: return ["capability identity history is incomplete or untrusted"]
    previous={}; genesis=None; initial={}; missing=set(); changed=set()
    for commit in reversed(commits):
        blob=run("show",f"{commit}:{ledger_path}")
        if stats is not None: stats["blob_reads"]=stats.get("blob_reads",0)+1
        try:
            data=json.loads(blob.stdout)
            if set(data)!={"schema","identities"} or data.get("schema")!="capability-identity-ledger-v1" or not isinstance(data.get("identities"),list): raise TypeError
            identities=data["identities"]
        except (json.JSONDecodeError,KeyError,TypeError): return ["capability identity history is incomplete or untrusted"]
        identifiers=[row.get("capability_id") for row in identities if isinstance(row,dict)]
        if len(identifiers)!=len(identities) or any(not isinstance(identifier,str) or not identifier for identifier in identifiers): return ["capability identity history is incomplete or untrusted"]
        if len(identifiers)!=len(set(identifiers)): return ["capability identity ledger id is not unique"]
        try: canonical_identity_digest(identities)
        except ValueError: return ["capability identity history is incomplete or untrusted"]
        current={row.get("capability_id"):row for row in identities}
        if not previous: genesis=commit; initial=dict(current)
        if not set(previous).issubset(current): errors.append("capability identity ledger removed or changed historical record"); missing.update(set(previous)-set(current))
        for key in set(previous)&set(current):
            if previous[key]!=current[key]: errors.append("capability identity ledger removed or changed historical record"); changed.add(key)
        for key in set(current)&missing: errors.append("capability identity removed then readded")
        for key,row in current.items():
            if key not in initial and row.get("origin")=="baseline": errors.append("post-genesis capability identities must use origin new")
            if key in initial and row!=initial[key]: errors.append("frozen initial capability identity digest mismatch")
            if key in changed and key in initial and row==initial[key]: errors.append("capability identity mutated then reverted")
        previous=current
    if expected_genesis=="pending":
        if not allow_pending_genesis or head!=genesis: errors.append("ledger genesis must be recorded after the clean C0 bootstrap commit")
    elif expected_genesis is not None and expected_genesis!=genesis:
        errors.append("recorded LEDGER_GENESIS differs from earliest first-parent ledger introduction commit")
    if stats is not None:
        stats["versions"]=len(commits)
        stats["ledger_git_calls"]=calls
    return sorted(set(errors))

def validate_ledger_binding(ledger, transitions, *, descendant=False):
    """Validate CAP-NEG-38..51 binding rules independent of mutable registry projection."""
    errors=[]; identities=ledger.get("identities", []) if isinstance(ledger, dict) else []
    if not isinstance(ledger,dict) or set(ledger)!={"schema","identities"} or ledger.get("schema")!="capability-identity-ledger-v1" or not isinstance(identities,list): errors.append("capability identity ledger schema is invalid")
    ids=[row.get("capability_id") for row in identities]
    if len(ids)!=len(set(ids)): errors.append("capability identity ledger id is not unique")
    new_rows={row.get("capability_id"):row for row in identities if row.get("origin")=="new"}
    new_transitions={row.get("capability_id"):row for row in transitions if row.get("origin")=="new"}
    for cap,row in new_transitions.items():
        if cap not in new_rows: errors.append("origin new transition requires exactly one identity ledger record")
        elif row.get("sequence")!=1 or row.get("predecessor") is not None: errors.append("new capability predecessor must be null")
    for cap,row in new_rows.items():
        transition=new_transitions.get(cap)
        if not transition: errors.append("origin new identity record references no sequence one transition")
        elif transition.get("capability_id")!=row.get("capability_id"): errors.append("origin new identity record capability does not match transition")
        elif transition.get("transition_id")!=row.get("origin_transition_id"): errors.append("origin new identity record transition id does not match transition")
    if len(new_rows) == len(new_transitions) and set(new_rows) != set(new_transitions): errors.append("origin new identity record capability does not match transition")
    return sorted(set(errors))

def validate_ledger_text_binding(text, expected_genesis=None):
    """Keep genesis solely in the lifecycle TODO; the identity ledger cannot mirror it."""
    return ["capability identity ledger must not publish genesis"] if re.search(r'"genesis"\s*:',text) else []

def validate_lifecycle_genesis_paths(paths_with_genesis):
    if len(paths_with_genesis) != 1:
        return ["exactly one canonical lifecycle TODO path may publish LEDGER_GENESIS"]
    return []

def lifecycle_genesis_binding(tree, todo_path):
    errors=validate_lifecycle_genesis_paths([path for path in LIFECYCLES if path in tree])
    if errors or not todo_path: return None, errors
    text=tree[todo_path].read_text(encoding="utf-8")
    headings=list(re.finditer(r"^## Post-Push Attestation \(Atomic Final Closeout\)\s*$",text,re.M))
    fields=list(re.finditer(r"^- \*\*C0 active implementation/genesis commit:\*\* `([^`]+)`\s*$",text,re.M))
    if len(headings)!=1 or len(fields)!=1: return None,["canonical LEDGER_GENESIS field must occur exactly once"]
    section_end=re.search(r"^## ",text[headings[0].end():],re.M); end=headings[0].end()+(section_end.start() if section_end else len(text)-headings[0].end())
    if not headings[0].end() <= fields[0].start() < end: return None,["canonical LEDGER_GENESIS field is outside Post-Push Attestation"]
    raw=fields[0].group(1); pending="pending delivery — persisted in C1 after observation"
    if raw==pending:
        if todo_path==COMPLETED_TODO: return None,["ledger genesis must be recorded after the clean C0 bootstrap commit"]
        return "pending",[]
    if not re.fullmatch(r"[0-9a-f]{40}",raw): return None,["canonical LEDGER_GENESIS must be pending bootstrap or lowercase 40-hex OID"]
    return raw,[]

def validate_module_catalog(catalog, module_paths):
    errors=[]; ids=[row.get("module_id") for row in catalog]; paths=[row.get("path") for row in catalog]
    if len(ids)!=len(set(ids)) or len(paths)!=len(set(paths)): errors.append("module catalog identity/path is not unique")
    active={row.get("path") for row in catalog if row.get("status")!="retired"}
    if active-set(module_paths): errors.append("active module catalog is not bijective with modules")
    if set(module_paths)-active: errors.append("module has no matching active catalog entry")
    for row in catalog:
        if row.get("status") not in {"active", "retired"}: errors.append("module catalog state is invalid")
        if row.get("status")=="retired" and row.get("path") in module_paths: errors.append("retired module path must be an unpublished historical tombstone")
        if row.get("status")=="retired" and (row.get("owned_capabilities") or row.get("planned_capabilities")): errors.append("retired module remains active, owned, or planned")
    return sorted(set(errors))

def policy_registry_errors(policy, ledger, module_paths):
    """Normalize the published policy vocabulary before applying CAP semantics."""
    if not policy or not isinstance(ledger, dict): return ["capability registry projection mismatch"]
    modules=[{**row, "status": row.get("runtime_authority_state")} for row in policy.get("modules", [])]
    transitions=[{**row, "state": row.get("transition_state")} for row in policy.get("capability_transitions", [])]
    catalog=[{**row, "status": row.get("catalog_state")} for row in policy.get("module_catalog", [])]
    baseline_rows=policy.get("baseline_capability_catalog", [])
    baseline=[row.get("capability_id") for row in baseline_rows]
    errors=validate_capability_registry(modules, transitions, baseline, ledger.get("identities", []), catalog)
    policy_baseline={row.get("capability_id"):row.get("baseline_owner") for row in baseline_rows if isinstance(row,dict)}
    ledger_baseline={row.get("capability_id"):row.get("baseline_owner") for row in ledger.get("identities",[]) if isinstance(row,dict) and row.get("origin")=="baseline"}
    if len(policy_baseline)!=len(baseline_rows) or policy_baseline!=ledger_baseline: errors.append("baseline capability owner projection mismatch")
    module_bindings={(row.get("module_id"),row.get("path")) for row in policy.get("modules",[]) if isinstance(row,dict)}
    active_catalog_bindings={(row.get("module_id"),row.get("path")) for row in policy.get("module_catalog",[]) if isinstance(row,dict) and row.get("catalog_state")=="active"}
    if module_bindings!=active_catalog_bindings: errors.append("active module catalog id/path binding mismatch")
    errors += validate_ledger_binding(ledger, transitions)
    errors += validate_module_catalog(catalog, module_paths)
    return sorted(set(errors))

def repository_ledger_history_errors(root, tree, todo_path, identities):
    """Fail closed unless immutable-ledger history resolves in a trusted Git worktree."""
    binding,binding_errors=lifecycle_genesis_binding(tree,todo_path)
    if binding_errors: return binding_errors
    top=subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True, capture_output=True)
    if top.returncode: return ["capability identity history is incomplete or untrusted"]
    repo=Path(top.stdout.strip())
    try: relative=(Path(root).resolve().relative_to(repo.resolve()) / "deterministic/capability_identity_ledger.json").as_posix()
    except ValueError: return ["capability identity history is incomplete or untrusted"]
    head_has_ledger=subprocess.run(["git", "-C", str(repo), "cat-file", "-e", f"HEAD:{relative}"], capture_output=True).returncode==0
    if not head_has_ledger:
        if binding!="pending": return ["recorded LEDGER_GENESIS differs from earliest first-parent ledger introduction commit"]
        return validate_pre_c0_bootstrap(active_todo=todo_path==ACTIVE_TODO,head_has_ledger=False,seed_digest=canonical_identity_digest(identities),expected_seed_digest=FROZEN_INITIAL_CAPABILITY_IDENTITY_DIGEST)
    return validate_identity_history(repo,relative,expected_genesis=binding,allow_pending_genesis=todo_path==ACTIVE_TODO)

def validate_retired_catalog_tree(catalog, root):
    root = Path(root)
    if any(row.get("status") == "retired" and (root / row.get("path", "")).is_file() for row in catalog):
        return ["retired module path must be an unpublished historical tombstone"]
    return []

def validate_pre_c0_bootstrap(*, active_todo, head_has_ledger, seed_digest, expected_seed_digest):
    if active_todo and not head_has_ledger and seed_digest == expected_seed_digest:
        return []
    return ["pre-C0 pending bootstrap requires active TODO, HEAD without ledger, and exact canonical seed"]

def lifecycle(tree, errors):
    present = [path for path in LIFECYCLES if path in tree]
    if len(present) != 1: errors.append("governing TODO lifecycle must contain exactly one active or completed path"); return None, None
    return present[0], LIFECYCLES[present[0]]

def ledger_entries(tree, errors):
    keys = {"path", "term", "context_kind", "section", "reason", "owner", "lifecycle", "line_hashes"}
    try:
        data = json.loads(tree["deterministic/legacy_reference_exceptions.json"].read_text(encoding="utf-8"))
        historical_path = "todos/completed/process/TODO-uninotas-foundation-project-rebase.md"
        todo_text = tree[historical_path].read_text(encoding="utf-8")
        actual, rows = section_occurrences(todo_text), {}
        for line in todo_text.splitlines():
            if any(term_occurs(term, line) for term in TERMS) and ACTIVE_AUTHORITY_PHRASES.search(line):
                errors.append("active legacy authority claim cannot be ledgered")
        if not isinstance(data, list) or not data: raise ValueError
        for row in data:
            if set(row) != keys or any(not isinstance(row[k], str) or not row[k].strip() for k in keys - {"line_hashes"}): raise ValueError
            key = (row["term"].casefold(), row["section"])
            hashes = row["line_hashes"]
            if "*" in row["path"] + row["term"] or row["path"] != historical_path or row["context_kind"] != "historical_migration_record" or row["lifecycle"] != "historical" or key in rows or not isinstance(hashes, list) or not hashes or hashes != sorted(hashes) or any(not re.fullmatch(r"[0-9a-f]{64}", value) for value in hashes): raise ValueError
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
        required={"core_scope":"uninotas","environment_type":"landlord","landlord_role":"paced_technical_adapter","business_tenancy":False}
        if any(contract.get(key)!=value for key,value in required.items()): raise ValueError
        modules,catalog,baseline,transitions=(contract.get(key) for key in ("modules","module_catalog","baseline_capability_catalog","capability_transitions"))
        baseline_ids={"note_read_model","integration_error_read_model","operational_workflow","authentication","team_profiles","legacy_log_invalidation","legacy_log_monitoring","runtime_topology","health_read"}
        if not all(isinstance(value,list) for value in (modules,catalog,baseline,transitions)) or len(baseline)!=9 or len(transitions)<4: raise ValueError
        module_ids={row.get("module_id") for row in modules if isinstance(row,dict)}
        if contract.get("subscopes")!=sorted(module_ids) or not {name[:-3] for name in OBSERVED_RUNTIME_MODULES}.issubset(module_ids) or not set(TARGET_OWNER_CAPABILITIES).issubset(module_ids): raise ValueError
        if {row.get("capability_id") for row in baseline}!=baseline_ids or not {"note-read-model-001","integration-error-read-model-001","operational-workflow-001","fiscal-document-read-001"} <= {row.get("transition_id") for row in transitions}: raise ValueError
        return contract
    except (KeyError, AttributeError, ValueError, json.JSONDecodeError): errors.append("scope policy mismatch"); return None

def validate(root):
    global FULL_TREE_SCAN_COUNT
    FULL_TREE_SCAN_COUNT += 1
    root, errors = Path(root), []
    tracked_tmp=subprocess.run(["git","-C",str(root),"ls-files","--","artifacts/tmp"],text=True,capture_output=True)
    if tracked_tmp.returncode==0 and tracked_tmp.stdout.strip(): errors.append("tracked file forbidden under artifacts/tmp")
    entries = repository_entries(root)
    errors += [f"symlink forbidden in publication tree: {p.relative_to(root).as_posix()}" for p in entries if p.is_symlink()]
    tree = {p.relative_to(root).as_posix(): p for p in entries if p.is_file() and not p.is_symlink()}
    todo_path, expected_lifecycle = lifecycle(tree, errors)
    required = ROOT_FILES | SUPPORT_FILES | {"modules/README.md", "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"}
    if todo_path: required.add(todo_path)
    errors += [f"missing required file: {p}" for p in required - set(tree)]
    actual_modules = {Path(p).name for p in tree if p.startswith("modules/") and p != "modules/README.md"}
    for path in DELETE_PATHS & set(tree): errors.append(f"forbidden deleted path present: {path}")
    policy = scope_policy(tree, errors)
    active_module_names=set()
    if policy:
        active_module_names={Path(row.get("path","")).name for row in policy["module_catalog"] if isinstance(row,dict) and row.get("catalog_state")=="active"}
        if actual_modules!=active_module_names: errors.append("canonical module catalog mismatch")
    if "modules/README.md" in tree and policy:
        text = tree["modules/README.md"].read_text(encoding="utf-8")
        if {name for name in active_module_names if f"({name})" in text} != active_module_names or any(text.count(f"({name})") != 1 for name in active_module_names): errors.append("module index/canonical owner mismatch")
    ledger_path=tree.get("deterministic/capability_identity_ledger.json"); ledger=None
    if ledger_path:
        try:
            ledger_text=ledger_path.read_text(encoding="utf-8"); errors += validate_ledger_text_binding(ledger_text); ledger=json.loads(ledger_text); identities=ledger["identities"]
            seed=[row for row in identities if isinstance(row,dict) and row.get("capability_id") in FROZEN_INITIAL_CAPABILITY_IDS]
            if set(ledger)!={"schema","identities"} or ledger.get("schema")!="capability-identity-ledger-v1" or {row.get("capability_id") for row in seed}!=FROZEN_INITIAL_CAPABILITY_IDS or validate_initial_identity_digest(seed,FROZEN_INITIAL_CAPABILITY_IDENTITY_DIGEST): raise ValueError
            canonical_identity_digest(identities)
            if sum(row.get("origin")=="baseline" for row in seed)!=9 or {row.get("capability_id") for row in seed if row.get("origin")=="new"}!={"fiscal_document_read"}: raise ValueError
        except (ValueError,KeyError,json.JSONDecodeError): errors.append("capability identity seed projection mismatch")
    if policy and ledger:
        errors += policy_registry_errors(policy, ledger, {"modules/" + name for name in actual_modules})
        errors += repository_ledger_history_errors(root,tree,todo_path,identities)
    for name in active_module_names:
        path = tree.get("modules/" + name)
        if not path: continue
        text = path.read_text(encoding="utf-8")
        for anchor in REQUIRED_ANCHORS:
            if anchor not in text: errors.append(f"missing module anchor {anchor}: {name}")
        if not policy or re.search(r"\*\*Core scope:\*\* `uninotas`", text) is None or re.search(rf"\*\*Subscope:\*\* `{re.escape(name[:-3])}`", text) is None or "`landlord`" not in text: errors.append(f"scope/subscope mismatch: {name}")
        else:
            row=next((item for item in policy["modules"] if item["module_id"]==name[:-3]),None)
            owned=", ".join(f"`{value}`" for value in row["owned_capabilities"]) if row else ""; planned=", ".join(f"`{value}`" for value in row["planned_capabilities"]) if row else ""
            if not row or f"**Runtime authority state:** `{row['runtime_authority_state']}`" not in text or f"**Owned capabilities:** {owned or 'none'}" not in text or f"**Planned capabilities:** {planned or 'none'}" not in text: errors.append(f"module metadata does not match scope registry: {name}")
    for name in OBSERVED_RUNTIME_MODULES:
        path = tree.get("modules/" + name)
        if not path: continue
        text = path.read_text(encoding="utf-8"); contract_bodies = []
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
    target_modules={f"{row.get('module_id')}.md" for row in policy.get("modules",[]) if isinstance(row,dict) and row.get("runtime_authority_state")=="target_planned"} if policy else set()
    for name in target_modules:
        path=tree.get("modules/"+name); text=path.read_text(encoding="utf-8") if path else ""; row=next((item for item in policy["modules"] if item["module_id"]==name[:-3]),None) if policy else None
        owned=", ".join(f"`{value}`" for value in row["owned_capabilities"]) if row else ""; planned=", ".join(f"`{value}`" for value in row["planned_capabilities"]) if row else ""
        if not row or not all(token in text for token in ("## Module Intent & Boundaries","## Canonical Coverage Status","## Purpose, Owned Entities, and Workflows","## Invariants","## Cross-Module Considerations",f"**Runtime authority state:** `{row['runtime_authority_state']}`",f"**Owned capabilities:** {owned or 'none'}",f"**Planned capabilities:** {planned or 'none'}")): errors.append(f"module metadata does not match scope registry: {name}")
    ledger_entries(tree, errors)
    if todo_path and any(term_occurs(term, tree[todo_path].read_text(encoding="utf-8")) for term in TERMS): errors.append(f"legacy authority/reference in {todo_path}")
    for owner, tokens in IDENTITY.items():
        if owner in tree and any(token not in tree[owner].read_text(encoding="utf-8") for token in tokens): errors.append(f"canonical identity mismatch: {owner}")
    for owner, anchor in IDENTITY_ANCHORS.items():
        if owner in tree and anchor not in tree[owner].read_text(encoding="utf-8"): errors.append(f"canonical identity anchor mismatch: {owner}")
    if "README.md" in tree:
        h1 = [line.strip() for line in tree["README.md"].read_text(encoding="utf-8").splitlines() if line.startswith("# ")]
        if h1 != ["# UniNotas Foundation"]: errors.append("canonical identity heading mismatch: README.md")
    for owner, assertion in CANONICAL_ASSERTIONS.items():
        if owner in tree and assertion not in tree[owner].read_text(encoding="utf-8"): errors.append(f"canonical ownership mismatch: {owner}")
    for owner, assertion in FISCAL_CONTEXT_ASSERTIONS.items():
        if owner in tree and assertion not in tree[owner].read_text(encoding="utf-8"): errors.append(f"canonical fiscal context mismatch: {owner}")
    if policy:
        by_module={row.get("module_id"):set(row.get("planned_capabilities",[])) for row in policy.get("modules",[]) if isinstance(row,dict)}
        for module_id, required_capabilities in TARGET_OWNER_CAPABILITIES.items():
            if not required_capabilities.issubset(by_module.get(module_id,set())): errors.append(f"canonical target owner mismatch: {module_id}")
    decisions = tree.get("decisions/uninotas-foundation-decisions.md")
    if decisions:
        rows = re.findall(r"^\|\s*(D-(?:0[1-9]|1[01]))\s*\|\s*(.*?)\s*\|", decisions.read_text(encoding="utf-8"), re.M)
        if [key for key, _ in rows] != [f"D-{number:02d}" for number in range(1,12)] or "Target-planned Smart Notas owns every note/document" not in dict(rows).get("D-07", ""): errors.append("canonical decision table mismatch")
    for relative, path in tree.items():
        text = path.read_text(encoding="utf-8", errors="replace")
        basic_privacy = has_basic_privacy(text)
        contextual = private_context_diagnostics(text)
        if basic_privacy: errors.append(f"privacy pattern in {relative}")
        errors += [f"privacy pattern in {relative}: {diagnostic}" for diagnostic in contextual]
        if relative not in {todo_path, "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"} and CONFLICTING_LOG_OWNERSHIP.search(text): errors.append(f"contradictory external ownership claim in {relative}")
        if relative in CURRENT_TRUTH_SURFACES and RETIRED_ROUTERFY_LOG_OWNERSHIP.search(text): errors.append(f"retired Routerfy log ownership claim in {relative}")
        if relative not in {todo_path, "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"} and CONFLICTING_IDENTITY.search(text): errors.append(f"contradictory canonical identity claim in {relative}")
        for _, target in ([] if path.suffix == ".py" else re.findall(r"\[([^]]+)\]\(([^)]+)\)", text)):
            target, _, anchor = target.partition("#")
            if "://" in target or target.startswith("mailto:"): continue
            dest = (path.parent / target).resolve() if target else path
            if not dest.is_file(): errors.append(f"broken relative link in {relative}: {target}")
            elif anchor and anchor.lower().replace("-", " ") not in headings(dest.read_text(encoding="utf-8", errors="replace")): errors.append(f"broken anchor in {relative}: {anchor}")
        historical_ledger_path = "todos/completed/process/TODO-uninotas-foundation-project-rebase.md"
        if relative not in {todo_path, historical_ledger_path, "artifacts/publication-manifest.txt", "deterministic/validate_foundation.py", "deterministic/legacy_reference_exceptions.json", "deterministic/tests/test_validate_foundation.py"} and any(term_occurs(term, text) for term in TERMS): errors.append(f"legacy authority/reference in {relative}")
    manifest = tree.get("artifacts/publication-manifest.txt")
    if manifest:
        expected_tree = set(tree)
        listed = [x.strip() for x in manifest.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]
        if set(listed) != expected_tree or not FROZEN_PUBLICATION_PATHS <= expected_tree or not FROZEN_PUBLICATION_PATHS <= set(listed): errors.append("frozen lifecycle tree mismatch")
        if len(listed) != len(set(listed)) or set(listed) != expected_tree: errors.append("publication manifest must uniquely and exactly match publication tree")
    return errors

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--root", required=True); args = parser.parse_args(); errors = validate(args.root)
    if errors: print("Foundation validation failed:\n" + "\n".join("- " + e for e in errors)); raise SystemExit(1)
    print("Foundation validation passed.")
if __name__ == "__main__": main()
