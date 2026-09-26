import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validate_foundation", ROOT / "deterministic" / "validate_foundation.py")

def valid_cnpj():
    digits = [int(value) for value in "123456780001"]
    for weights in ((5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2), (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)):
        remainder = sum(value * weight for value, weight in zip(digits, weights)) % 11
        digits.append(0 if remainder < 2 else 11 - remainder)
    return "".join(map(str, digits))

class PrivacyPredicateTests(unittest.TestCase):
    syntaxes = (lambda key, value: f"export {key}={value}", lambda key, value: f"- {key}: {value}", lambda key, value: f'"{key}": {value}', lambda key, value: f"| {key} | {value} |")

    def setUp(self):
        self.module = importlib.util.module_from_spec(SPEC)
        SPEC.loader.exec_module(self.module)

    def test_guard_priv_01_rejects_runtime_generated_valid_cnpj(self):
        compact = valid_cnpj()
        formatted = f"{compact[:2]}.{compact[2:5]}.{compact[5:8]}/{compact[8:12]}-{compact[12:]}"
        for value in (compact, formatted): self.assertEqual("valid CNPJ value", self.module.private_context_diagnostic(f"cnpj={value}"))

    def test_guard_priv_02_provider_id_families_all_syntaxes_and_fences(self):
        for key in self.module.PROVIDER_ID_KEYS:
            for syntax in self.syntaxes:
                for fenced in (False, True):
                    text = syntax(key, "opaque-value")
                    if fenced: text = f"```example\n{text}\n```"
                    self.assertEqual("concrete provider identifier context", self.module.private_context_diagnostic(text), (key, text))

    def test_guard_priv_03_document_url_families_all_syntaxes_and_fences(self):
        for key in self.module.DOCUMENT_URL_KEYS:
            for syntax in self.syntaxes:
                for fenced in (False, True):
                    text = syntax(key, "https://captured.invalid/document")
                    if fenced: text = f"```example\n{text}\n```"
                    self.assertEqual("captured document URL context", self.module.private_context_diagnostic(text), (key, text))

    def test_guard_priv_04_credential_families_all_syntaxes_and_fences(self):
        for key, diagnostic in self.module.CREDENTIAL_KEYS.items():
            for syntax in self.syntaxes:
                for fenced in (False, True):
                    text = syntax(key, "invalid-checksum-value")
                    if fenced: text = f"```example\n{text}\n```"
                    self.assertEqual(diagnostic, self.module.private_context_diagnostic(text), (key, text))

    def test_guard_priv_pos_01_official_root_generic_ids_and_normalization(self):
        cases = ("documentation_url=https://app.smart-notas.com/api/docs", "generic_id=opaque-value", "smartNotasNoteId = <placeholder>", "ＰｒｏｖｉｄｅｒＩｄ = <redacted>", 'provider_id="https%3A%2F%2Fexample.invalid%2Fsafe"')
        for text in cases: self.assertIsNone(self.module.private_context_diagnostic(text), text)
        self.assertEqual("captured document URL context", self.module.private_context_diagnostic("document_url=https://app.smart-notas.com/api/docs"))

    def test_guard_priv_pos_02_every_placeholder_for_every_family_syntax_and_fence(self):
        placeholders = ("", "<redacted>", "<placeholder>", "REDACTED", "${SAFE_VARIABLE}", "https://example.invalid/safe")
        for key in (*self.module.CREDENTIAL_KEYS, *self.module.PROVIDER_ID_KEYS, *self.module.DOCUMENT_URL_KEYS):
            for syntax in self.syntaxes:
                for placeholder in placeholders:
                    text = f"```example\n{syntax(key, placeholder)}\n```"
                    self.assertIsNone(self.module.private_context_diagnostic(text), (key, placeholder, text))

    def test_one_layer_quote_stripping_and_one_time_percent_decoding(self):
        self.assertEqual("concrete provider identifier context", self.module.private_context_diagnostic("provider_id='opaque-value'"))
        self.assertEqual("captured document URL context", self.module.private_context_diagnostic("document_url=https%3A%2F%2Fcaptured.invalid%2Fdocument"))
        self.assertEqual("concrete provider identifier context", self.module.private_context_diagnostic("provider_id=%256fpaque-value"))

    def test_guard_priv_06_invisible_unicode_cannot_split_sensitive_keys(self):
        cases={
            "smart_notas_unifast_"+"token":"token"+" credential",
            "smart_notas_unifast_"+"cnpj":"CNPJ credential",
            "provider_"+"id":"concrete provider identifier context",
            "document_"+"url":"captured document URL context",
        }
        for key,diagnostic in cases.items():
            midpoint=len(key)//2
            for codepoint in ("\u200b","\u034f","\ufe0f","\u00a0","\u2060"):
                disguised=key[:midpoint]+codepoint+key[midpoint:]
                for syntax,value in (("json",f'"{disguised}": "concrete-sensitive-value"'),("env",f"{disguised}=concrete-sensitive-value"),("yaml",f"{disguised}: concrete-sensitive-value"),("table",f"| {disguised} | concrete-sensitive-value |")):
                    with self.subTest(key=key,codepoint=ord(codepoint),syntax=syntax): self.assertEqual(diagnostic,self.module.private_context_diagnostic(value))

    def test_guard_priv_07_nfkc_compatible_sensitive_keys_cannot_bypass_detection(self):
        cases={
            "smart_notas_unifast_"+"token":"token"+" credential",
            "smart_notas_prosperar_"+"cnpj":"CNPJ credential",
            "provider_"+"id":"concrete provider identifier context",
            "document_"+"url":"captured document URL context",
        }
        for key,diagnostic in cases.items():
            fullwidth="".join(chr(ord(character)+0xFEE0) if 0x21 <= ord(character) <= 0x7E else character for character in key)
            mixed="".join(chr(ord(character)+0xFEE0) if index % 2 == 0 and 0x21 <= ord(character) <= 0x7E else character for index,character in enumerate(key))
            for disguised in (fullwidth,mixed):
                for syntax,value in (("json",f'"{disguised}": "concrete-sensitive-value"'),("env",f"{disguised}=concrete-sensitive-value"),("yaml",f"{disguised}: concrete-sensitive-value"),("table",f"| {disguised} | concrete-sensitive-value |")):
                    with self.subTest(key=key,disguise=disguised,syntax=syntax): self.assertEqual(diagnostic,self.module.private_context_diagnostic(value))

    def test_guard_priv_08_quoted_markdown_and_structured_json_keys_cannot_bypass_detection(self):
        cases={
            "smart_notas_unifast_"+"token":"token"+" credential",
            "smart_notas_prosperar_"+"cnpj":"CNPJ credential",
            "provider_"+"id":"concrete provider identifier context",
            "document_"+"url":"captured document URL context",
        }
        for key,diagnostic in cases.items():
            escaped=key.replace("_",r"\u005f")
            variants=(
                f"'{key}': concrete-sensitive-value",
                f"| `{key}` | concrete-sensitive-value |",
                f'{{"{key}":"concrete-sensitive-value"}}',
                f'{{"nested":{{"{escaped}":"concrete-sensitive-value"}}}}',
            )
            for text in variants:
                with self.subTest(key=key,text=text): self.assertEqual(diagnostic,self.module.private_context_diagnostic(text))

    def test_guard_priv_09_compatibility_wrappers_escapes_and_duplicate_json_keys_cannot_bypass_detection(self):
        cases={
            "smart_notas_unifast_"+"token":"token"+" credential",
            "smart_notas_prosperar_"+"cnpj":"CNPJ credential",
            "provider_"+"id":"concrete provider identifier context",
            "document_"+"url":"captured document URL context",
        }
        for key,diagnostic in cases.items():
            escaped_x=key.replace("_",r"\x5f"); escaped_u=key.replace("_",r"\U0000005f")
            variants=(
                f"\uff02{key}\uff02: concrete-sensitive-value",
                f"| \uff40{key}\uff40 | concrete-sensitive-value |",
                f"| ``{key}`` | concrete-sensitive-value |",
                f'"{escaped_x}": concrete-sensitive-value',
                f'"{escaped_u}": concrete-sensitive-value',
                f'{{"{key}":"concrete-sensitive-value","{key}":"<placeholder>"}}',
            )
            for text in variants:
                with self.subTest(key=key,text=text): self.assertEqual(diagnostic,self.module.private_context_diagnostic(text))

    def test_guard_priv_10_escaped_invisible_and_fullwidth_keys_cannot_bypass_detection(self):
        for key in (r"pro\u200bvider_id",r"\uff50rovider_id"):
            for text in (f'"{key}": "concrete-sensitive-value"',f"{key}=concrete-sensitive-value",f"{key}: concrete-sensitive-value",f"| {key} | concrete-sensitive-value |"):
                with self.subTest(key=key,text=text): self.assertEqual("concrete provider identifier context",self.module.private_context_diagnostic(text))

    def test_guard_priv_11_invisible_or_escaped_characters_cannot_split_valid_cnpj(self):
        compact = valid_cnpj()
        formatted = f"{compact[:2]}.{compact[2:5]}.{compact[5:8]}/{compact[8:12]}-{compact[12:]}"
        variants = []
        for value in (compact, formatted):
            midpoint = len(value) // 2
            variants.extend((
                value[:midpoint] + "\u200b" + value[midpoint:],
                value[:midpoint] + "\u034f" + value[midpoint:],
                f'{{"reference":"{value[:midpoint]}\\u200b{value[midpoint:]}"}}',
                f'reference: "{value[:midpoint]}\\u034f{value[midpoint:]}"',
            ))
        for text in variants:
            with self.subTest(text=text):
                self.assertEqual("valid CNPJ value", self.module.private_context_diagnostic(text))

    def test_guard_priv_12_yaml_flow_mappings_cannot_bypass_sensitive_contexts(self):
        cases = (
            ("{provider_id: opaque-sensitive-value}", "concrete provider identifier context"),
            ("- {document_url: https://private.invalid/doc/123}", "captured document URL context"),
            ("{nested: {smart_notas_unifast_token: concrete-sensitive-value}}", "token credential"),
            ('[{"smart_notas_prosperar_cnpj": "concrete-sensitive-value"}]', "CNPJ credential"),
            (r"{pro\u0076ider_id: opaque-sensitive-value}", "concrete provider identifier context"),
            ("{provider_id: <placeholder>, provider_id: opaque-sensitive-value}", "concrete provider identifier context"),
        )
        for text, diagnostic in cases:
            with self.subTest(text=text):
                self.assertEqual(diagnostic, self.module.private_context_diagnostic(text))

        for key in (*self.module.CREDENTIAL_KEYS, *self.module.PROVIDER_ID_KEYS, *self.module.DOCUMENT_URL_KEYS):
            with self.subTest(key=key):
                self.assertIsNone(self.module.private_context_diagnostic(f"{{{key}: <placeholder>}}"))

    def test_guard_priv_13_flow_mapping_scan_has_linear_work_budget(self):
        depth = 4000
        text = "{nested:" * depth + "{provider_id: opaque-sensitive-value}" + "}" * depth
        stats = {}
        pairs = list(self.module.flow_mapping_pairs(text, stats=stats))
        self.assertEqual([("provider_id", "opaque-sensitive-value")], pairs)
        self.assertLessEqual(stats["characters_scanned"], len(text))
        self.assertLessEqual(stats["key_chars_materialized"], len(text))
        self.assertLessEqual(stats["value_chars_materialized"], 512 * len(pairs))

    def test_guard_priv_14_long_escape_padded_flow_key_cannot_bypass_detection(self):
        padded_key = "pro" + (r"\u200b" * 300) + "vider_id"
        text = f"{{{padded_key}: opaque-sensitive-value}}"
        self.assertEqual("concrete provider identifier context", self.module.private_context_diagnostic(text))

    def test_guard_priv_15_nested_mapping_keys_keep_global_linear_materialization_budget(self):
        text = "{provider_id: opaque-sensitive-value}"
        for _ in range(1000):
            text = "{" + text + ": benign-value}"
        stats = {}
        pairs = list(self.module.flow_mapping_pairs(text, stats=stats))
        self.assertEqual([("provider_id", "opaque-sensitive-value")], pairs)
        self.assertLessEqual(stats["characters_scanned"], len(text))
        self.assertLessEqual(stats["key_chars_materialized"], len(text))
        self.assertLessEqual(stats["value_chars_materialized"], 512 * len(pairs))
