import importlib.util
import pathlib
import json
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validate_foundation", ROOT / "deterministic" / "validate_foundation.py")


class RegistrySemanticsTests(unittest.TestCase):
    def setUp(self):
        self.module = importlib.util.module_from_spec(SPEC)
        SPEC.loader.exec_module(self.module)

    def test_new_capability_requires_sequence_one_and_no_predecessor(self):
        errors = self.module.validate_capability_registry(
            [{"module_id": "planned", "status": "target_planned", "owned_capabilities": [], "planned_capabilities": ["note.read"]}],
            [{"transition_id": "T-01", "capability_id": "note.read", "sequence": 2, "origin": "new", "predecessor": None, "successor": "planned", "state": "planned"}],
            [],
            [],
        )
        self.assertIn("origin new is valid only at sequence one", errors)

    def test_current_and_planned_membership_cannot_overlap(self):
        errors = self.module.validate_capability_registry(
            [{"module_id": "current", "status": "current_runtime", "owned_capabilities": ["note.read"], "planned_capabilities": ["note.read"]}], [], [], []
        )
        self.assertIn("owned_capabilities intersects planned_capabilities", errors)

    def test_cap_pos_01_initial_planned_chain(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["cap"]}]
        transitions=[{"transition_id":"T-01","capability_id":"cap","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"}]
        self.assertEqual([],self.module.validate_capability_registry(modules,transitions,["cap"],[]))

    def test_cap_pos_02_new_capability_planned(self):
        modules=[{"module_id":"planned","status":"target_planned","owned_capabilities":[],"planned_capabilities":["new"]}]
        transitions=[{"transition_id":"T-01","capability_id":"new","sequence":1,"origin":"new","predecessor":None,"successor":"planned","state":"planned"}]
        self.assertEqual([],self.module.validate_capability_registry(modules,transitions,[],[{"capability_id":"new","origin":"new"}]))

    def test_cap_pos_new_origin_completed_with_sole_successor_owner(self):
        policy={
            "modules":[{"module_id":"new-owner","path":"modules/new-owner.md","runtime_authority_state":"current_runtime","owned_capabilities":["new"],"planned_capabilities":[]}],
            "module_catalog":[{"module_id":"new-owner","path":"modules/new-owner.md","catalog_state":"active"}],
            "baseline_capability_catalog":[],
            "capability_transitions":[{"transition_id":"new-001","capability_id":"new","sequence":1,"origin":"new","transition_state":"completed","predecessor":None,"successor":"new-owner"}],
        }
        ledger={"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"new","origin":"new","origin_transition_id":"new-001"}]}
        self.assertEqual([],self.module.policy_registry_errors(policy,ledger,{"modules/new-owner.md"}))

    def test_cap_pos_catalog_backed_retired_predecessor_and_complete_second_hop(self):
        policy={
            "modules":[{"module_id":"c","path":"modules/c.md","runtime_authority_state":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}],
            "module_catalog":[{"module_id":"a","path":"modules/a.md","catalog_state":"retired"},{"module_id":"b","path":"modules/b.md","catalog_state":"retired"},{"module_id":"c","path":"modules/c.md","catalog_state":"active"}],
            "baseline_capability_catalog":[{"capability_id":"cap","baseline_owner":"a"}],
            "capability_transitions":[{"transition_id":"T1","capability_id":"cap","sequence":1,"origin":"transferred","transition_state":"completed","predecessor":"a","successor":"b"},{"transition_id":"T2","capability_id":"cap","sequence":2,"origin":"transferred","transition_state":"completed","predecessor":"b","successor":"c"}],
        }
        ledger={"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"cap","origin":"baseline","baseline_owner":"a"}]}
        self.assertEqual([],self.module.policy_registry_errors(policy,ledger,{"modules/c.md"}))

    def test_cap_neg_54_baseline_owner_projection_is_immutable(self):
        policy={
            "modules":[{"module_id":"a","path":"modules/a.md","runtime_authority_state":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}],
            "module_catalog":[{"module_id":"a","path":"modules/a.md","catalog_state":"active"}],
            "baseline_capability_catalog":[{"capability_id":"cap","baseline_owner":"rewritten-owner"}],
            "capability_transitions":[],
        }
        ledger={"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"cap","origin":"baseline","baseline_owner":"a"}]}
        self.assertIn("baseline capability owner projection mismatch",self.module.policy_registry_errors(policy,ledger,{"modules/a.md"}))

    def test_cap_neg_56_baseline_capability_cannot_change_owner_without_transition(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        ledger=[{"capability_id":"cap","origin":"baseline","baseline_owner":"a"}]
        self.assertIn("baseline capability without transition must remain with baseline owner",self.module.validate_capability_registry(modules,[],["cap"],ledger))

    def test_cap_neg_57_baseline_transition_must_start_from_baseline_owner(self):
        modules=[{"module_id":"a","status":"retired","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        transitions=[{"transition_id":"T","capability_id":"cap","sequence":1,"origin":"transferred","predecessor":"b","successor":"b","state":"completed"}]
        ledger=[{"capability_id":"cap","origin":"baseline","baseline_owner":"a"}]
        self.assertIn("baseline capability transition must start from baseline owner",self.module.validate_capability_registry(modules,transitions,["cap"],ledger))

    def test_cap_neg_55_active_catalog_id_path_binding_cannot_be_swapped(self):
        policy={
            "modules":[
                {"module_id":"a","path":"modules/a.md","runtime_authority_state":"current_runtime","owned_capabilities":["cap-a"],"planned_capabilities":[]},
                {"module_id":"b","path":"modules/b.md","runtime_authority_state":"current_runtime","owned_capabilities":["cap-b"],"planned_capabilities":[]},
            ],
            "module_catalog":[
                {"module_id":"a","path":"modules/b.md","catalog_state":"active"},
                {"module_id":"b","path":"modules/a.md","catalog_state":"active"},
            ],
            "baseline_capability_catalog":[{"capability_id":"cap-a","baseline_owner":"a"},{"capability_id":"cap-b","baseline_owner":"b"}],
            "capability_transitions":[],
        }
        ledger={"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"cap-a","origin":"baseline","baseline_owner":"a"},{"capability_id":"cap-b","origin":"baseline","baseline_owner":"b"}]}
        self.assertIn("active module catalog id/path binding mismatch",self.module.policy_registry_errors(policy,ledger,{"modules/a.md","modules/b.md"}))

    def test_cap_neg_transition_predecessor_must_exist_in_catalog(self):
        modules=[{"module_id":"c","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        catalog=[{"module_id":"c","path":"modules/c.md","status":"active"}]
        transition=[{"transition_id":"T","capability_id":"cap","sequence":1,"origin":"transferred","predecessor":"never-cataloged","successor":"c","state":"completed"}]
        self.assertIn("transition references unknown module",self.module.validate_capability_registry(modules,transition,["cap"],[],catalog))

    def test_cap_pos_03_partial_promotion(self):
        modules=[{"module_id":"current","status":"current_runtime","owned_capabilities":["done"],"planned_capabilities":["next"]}]
        transitions=[{"transition_id":"T-01","capability_id":"next","sequence":1,"origin":"new","predecessor":None,"successor":"current","state":"planned"}]
        self.assertEqual([],self.module.validate_capability_registry(modules,transitions,["done"],[]))

    def test_cap_pos_04_complete_promotion_retired_predecessor(self):
        modules=[{"module_id":"old","status":"retired","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"new","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        transitions=[{"transition_id":"T","capability_id":"cap","sequence":1,"origin":"transferred","predecessor":"old","successor":"new","state":"completed"}]
        self.assertEqual([],self.module.validate_capability_registry(modules,transitions,["cap"],[]))

    def test_cap_pos_05_second_hop_planned(self):
        modules=[{"module_id":"b","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]},{"module_id":"c","status":"target_planned","owned_capabilities":[],"planned_capabilities":["cap"]}]
        transitions=[{"transition_id":"T1","capability_id":"cap","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"completed"},{"transition_id":"T2","capability_id":"cap","sequence":2,"origin":"transferred","predecessor":"b","successor":"c","state":"planned"}]
        catalog=[{"module_id":"a","status":"retired"},{"module_id":"b","status":"active"},{"module_id":"c","status":"active"}]
        self.assertEqual([],self.module.validate_capability_registry(modules,transitions,["cap"],[],catalog))

    def test_cap_pos_06_second_hop_completed(self):
        modules=[{"module_id":"c","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        transitions=[{"transition_id":"T1","capability_id":"cap","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"completed"},{"transition_id":"T2","capability_id":"cap","sequence":2,"origin":"transferred","predecessor":"b","successor":"c","state":"completed"}]
        catalog=[{"module_id":"a","status":"retired"},{"module_id":"b","status":"retired"},{"module_id":"c","status":"active"}]
        self.assertEqual([],self.module.validate_capability_registry(modules,transitions,["cap"],[],catalog))

    def test_cap_pos_07_stable_current_ownership_without_transition(self):
        self.assertEqual([],self.module.validate_capability_registry([{"module_id":"a","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}],[],["cap"],[]))

    def test_cap_pos_09_append_new_origin_identity(self):
        self.assertEqual([],self.module.validate_ledger_binding({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"new","origin":"new"}]},[{"capability_id":"new","origin":"new","sequence":1,"predecessor":None}]))

    def test_cap_pos_08_retired_catalog_tombstone_without_document(self):
        modules=[{"module_id":"retired","status":"retired","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"current","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        self.assertEqual([],self.module.validate_capability_registry(modules,[],["cap"],[]))

    def test_cap_neg_01_to_05_distinct_diagnostics(self):
        cases={
            "CAP-NEG-01":([{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":["c"]}],[],"owned_capabilities intersects planned_capabilities"),
            "CAP-NEG-02":([{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]}],[],"capability has multiple current owners"),
        }
        for case,(modules,transitions,diagnostic) in cases.items():
            with self.subTest(case=case): self.assertIn(diagnostic,self.module.validate_capability_registry(modules,transitions,["c"],[]))

    def test_cap_neg_03_planned_predecessor_not_current_owner(self):
        modules=[{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transition=[{"transition_id":"T","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"}]
        self.assertIn("planned transfer predecessor is not the current owner",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_04_duplicate_planned_successor(self):
        modules=[{"module_id":"a","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        self.assertIn("capability has multiple planned successors",self.module.validate_capability_registry(modules,[],[],[]))

    def test_cap_neg_05_sequence_gap(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transition=[{"transition_id":"T","capability_id":"c","sequence":2,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"}]
        self.assertIn("capability transition sequence is not contiguous",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_12_to_15_catalog_bijection_and_retirement(self):
        cases={
          "CAP-NEG-12":([{ "module_id":"a","path":"a.md","status":"current_runtime"},{"module_id":"a","path":"b.md","status":"current_runtime"}],["a.md","b.md"],"module catalog identity/path is not unique"),
          "CAP-NEG-13":([{ "module_id":"a","path":"a.md","status":"current_runtime"}],["a.md","b.md"],"module has no matching active catalog entry"),
          "CAP-NEG-14":([{ "module_id":"a","path":"a.md","status":"current_runtime"}],["b.md"],"active module catalog is not bijective with modules"),
          "CAP-NEG-15":([{ "module_id":"a","path":"a.md","status":"retired","owned_capabilities":["c"]}],[],"retired module remains active, owned, or planned"),
        }
        for case,(catalog,paths,diagnostic) in cases.items():
            with self.subTest(case=case): self.assertIn(diagnostic,self.module.validate_module_catalog(catalog,paths))

    def test_cap_neg_06_transition_fork(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transitions=[{"transition_id":"T-01","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"},{"transition_id":"T-02","capability_id":"c","sequence":2,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"}]
        self.assertIn("capability transition chain fork",self.module.validate_capability_registry(modules,transitions,["c"],[]))

    def test_cap_neg_07_transition_cycle(self):
        modules=[{"module_id":"a","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]},{"module_id":"b","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]}]
        transitions=[{"transition_id":"T-01","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"completed"},{"transition_id":"T-02","capability_id":"c","sequence":2,"origin":"transferred","predecessor":"b","successor":"a","state":"planned"}]
        self.assertIn("capability transition chain cycle",self.module.validate_capability_registry(modules,transitions,["c"],[]))

    def test_cap_neg_08_unknown_module_reference(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transition=[{"transition_id":"T-01","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"missing","state":"planned"}]
        self.assertIn("transition references unknown module",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_09_broken_chain_edge(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["other"],"planned_capabilities":[]},{"module_id":"c","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transitions=[{"transition_id":"T-01","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"completed"},{"transition_id":"T-02","capability_id":"c","sequence":2,"origin":"transferred","predecessor":"a","successor":"c","state":"planned"}]
        self.assertIn("transition predecessor does not match prior successor",self.module.validate_capability_registry(modules,transitions,["c"],[]))

    def test_cap_neg_10_completed_with_planned_residue(self):
        modules=[{"module_id":"a","status":"retired","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"c","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transition=[{"transition_id":"T-01","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"completed"}]
        self.assertIn("completed capability retains planned membership",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_11_terminal_owner_mismatch(self):
        modules=[{"module_id":"a","status":"retired","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["other"],"planned_capabilities":[]},{"module_id":"c","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]}]
        transition=[{"transition_id":"T-01","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"completed"}]
        self.assertIn("terminal completed successor is not sole current owner",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_16_nonterminal_transition_must_be_completed(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"c","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transitions=[{"transition_id":"T-01","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"},{"transition_id":"T-02","capability_id":"c","sequence":2,"origin":"transferred","predecessor":"b","successor":"c","state":"planned"}]
        self.assertIn("nonterminal transition must be completed",self.module.validate_capability_registry(modules,transitions,["c"],[]))

    def test_cap_neg_17_duplicate_transition_id(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transitions=[{"transition_id":"T","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"},{"transition_id":"T","capability_id":"other","sequence":1,"origin":"new","predecessor":None,"successor":"b","state":"planned"}]
        self.assertIn("transition_id is not unique",self.module.validate_capability_registry(modules,transitions,["c"],[]))

    def test_cap_neg_18_new_origin_after_sequence_one(self):
        modules=[{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["new"]}]
        transition=[{"transition_id":"T","capability_id":"new","sequence":2,"origin":"new","predecessor":None,"successor":"b","state":"planned"}]
        self.assertIn("origin new is valid only at sequence one",self.module.validate_capability_registry(modules,transition,[],[]))

    def test_cap_neg_19_new_origin_with_predecessor(self):
        modules=[{"module_id":"a","status":"retired","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["new"]}]
        transition=[{"transition_id":"T","capability_id":"new","sequence":1,"origin":"new","predecessor":"a","successor":"b","state":"planned"}]
        self.assertIn("new capability predecessor must be null",self.module.validate_capability_registry(modules,transition,[],[]))

    def test_cap_neg_20_new_planned_with_preexisting_owner(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["new"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["new"]}]
        transition=[{"transition_id":"T","capability_id":"new","sequence":1,"origin":"new","predecessor":None,"successor":"b","state":"planned"}]
        self.assertIn("new planned capability already has an owner",self.module.validate_capability_registry(modules,transition,[],[]))

    def test_cap_neg_21_terminal_planned_missing_successor_membership(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["other"],"planned_capabilities":[]}]
        transition=[{"transition_id":"T","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"}]
        self.assertIn("terminal planned successor lacks planned membership",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_22_target_planned_with_owned_capability(self):
        modules=[{"module_id":"a","status":"target_planned","owned_capabilities":["c"],"planned_capabilities":["other"]}]
        self.assertIn("target_planned module cannot own capability",self.module.validate_capability_registry(modules,[],[],[]))

    def test_cap_neg_23_completed_terminal_without_successor_owner(self):
        modules=[{"module_id":"a","status":"retired","owned_capabilities":[],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["other"],"planned_capabilities":[]}]
        transition=[{"transition_id":"T","capability_id":"c","sequence":1,"origin":"transferred","predecessor":"a","successor":"b","state":"completed"}]
        self.assertIn("terminal completed capability has no sole successor owner",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_24_orphan_planned_membership(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        self.assertIn("planned membership has no matching terminal planned transition",self.module.validate_capability_registry(modules,[],["c"],[]))

    def test_cap_neg_25_transferred_with_null_predecessor(self):
        modules=[{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c"]}]
        transition=[{"transition_id":"T","capability_id":"c","sequence":1,"origin":"transferred","predecessor":None,"successor":"b","state":"planned"}]
        self.assertIn("transferred capability requires a predecessor",self.module.validate_capability_registry(modules,transition,["c"],[]))

    def test_cap_neg_26_duplicate_owned_membership(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c","c"],"planned_capabilities":[]}]
        self.assertIn("owned_capabilities contains duplicate capability id",self.module.validate_capability_registry(modules,[],["c"],[]))

    def test_cap_neg_27_duplicate_planned_membership(self):
        modules=[{"module_id":"a","status":"target_planned","owned_capabilities":[],"planned_capabilities":["c","c"]}]
        self.assertIn("planned_capabilities contains duplicate capability id",self.module.validate_capability_registry(modules,[],[],[]))

    def test_cap_neg_28_current_runtime_without_owned_capability(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":[],"planned_capabilities":["c"]}]
        self.assertIn("current_runtime module must own at least one capability",self.module.validate_capability_registry(modules,[],[],[]))

    def test_cap_neg_29_target_planned_without_planned_capability(self):
        modules=[{"module_id":"a","status":"target_planned","owned_capabilities":[],"planned_capabilities":[]}]
        self.assertIn("target_planned module must plan at least one capability",self.module.validate_capability_registry(modules,[],[],[]))

    def test_cap_neg_30_active_module_without_capabilities(self):
        modules=[{"module_id":"a","status":"active","owned_capabilities":[],"planned_capabilities":[]}]
        self.assertIn("active module has neither owned nor planned capabilities",self.module.validate_capability_registry(modules,[],[],[]))

    def test_cap_neg_31_retired_catalog_path_still_published(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp); path=root/"modules/retired.md"; path.parent.mkdir(); path.write_text("published")
            catalog=[{"module_id":"retired","path":"modules/retired.md","status":"retired"}]
            self.assertIn("retired module path must be an unpublished historical tombstone",self.module.validate_retired_catalog_tree(catalog,root))

    def test_cap_neg_32_baseline_capability_deleted(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["other"],"planned_capabilities":[]}]
        self.assertIn("baseline capability is missing from governed ownership or transition state",self.module.validate_capability_registry(modules,[],["c"],[]))

    def test_cap_neg_33_baseline_capability_renamed_or_aliased(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["c"],"planned_capabilities":[]}]
        ledger=[{"capability_id":"renamed-c","origin":"baseline"}]
        self.assertIn("baseline capability id is immutable and aliases are forbidden",self.module.validate_capability_registry(modules,[],["c"],ledger))

    def test_cap_neg_34_uncataloged_capability_inserted_directly_as_owned(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["uncataloged"],"planned_capabilities":[]}]
        self.assertIn("non-baseline capability requires origin new transition history",self.module.validate_capability_registry(modules,[],[],[]))

    def test_cap_neg_35_coordinated_initial_identity_erasure(self):
        initial=[{"capability_id":"c","origin":"baseline","baseline_owner":"a"}]
        self.assertIn("frozen initial capability identity digest mismatch",self.module.validate_initial_identity_digest([],self.module.canonical_identity_digest(initial)))

    def test_cap_neg_duplicate_owner_and_sequence_gap(self):
        duplicate=[{"module_id":"a","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]},{"module_id":"b","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        self.assertIn("capability has multiple current owners",self.module.validate_capability_registry(duplicate,[],["cap"],[]))
        gap=[{"module_id":"a","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["cap"]}]
        transition=[{"transition_id":"T-02","capability_id":"cap","sequence":2,"origin":"transferred","predecessor":"a","successor":"b","state":"planned"}]
        self.assertIn("capability transition sequence is not contiguous",self.module.validate_capability_registry(gap,transition,["cap"],[]))

    def test_cap_neg_duplicate_identity_ledger(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        ledger=[{"capability_id":"cap"},{"capability_id":"cap"}]
        self.assertIn("capability identity ledger id is not unique",self.module.validate_capability_registry(modules,[],["cap"],ledger))

    def test_cap_pos_10_and_neg_36_first_parent_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
            for key,value in (("user.email","test@example.invalid"),("user.name","Test")): subprocess.run(["git","-C",str(repo),"config",key,value],check=True)
            ledger=repo/"deterministic/capability_identity_ledger.json"; ledger.parent.mkdir()
            ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}]})); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","genesis"],check=True)
            genesis=subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],text=True,capture_output=True,check=True).stdout.strip()
            ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"},{"capability_id":"new","origin":"new","origin_transition_id":"new-001"}]})); subprocess.run(["git","-C",str(repo),"commit","-am","append","-q"],check=True)
            self.assertEqual([],self.module.validate_identity_history(repo))
            ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"cap","origin":"baseline","baseline_owner":"mutated"},{"capability_id":"new","origin":"new","origin_transition_id":"new-001"}]})); subprocess.run(["git","-C",str(repo),"commit","-am","mutate","-q"],check=True)
            self.assertIn("capability identity ledger removed or changed historical record",self.module.validate_identity_history(repo))

    def test_cap_neg_duplicate_identity_in_intermediate_history_cannot_collapse(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
            for key,value in (("user.email","test@example.invalid"),("user.name","Test")): subprocess.run(["git","-C",str(repo),"config",key,value],check=True)
            ledger=repo/"deterministic/capability_identity_ledger.json"; ledger.parent.mkdir()
            def commit(identities,message):
                ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":identities})); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm",message],check=True)
            valid=[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}]; commit(valid,"valid genesis"); commit(valid+valid,"duplicate intermediate"); commit(valid,"valid tip")
            self.assertEqual(["capability identity ledger id is not unique"],self.module.validate_identity_history(repo))

    def test_cap_neg_malformed_identity_schema_in_intermediate_history_is_untrusted(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
            for key,value in (("user.email","test@example.invalid"),("user.name","Test")): subprocess.run(["git","-C",str(repo),"config",key,value],check=True)
            ledger=repo/"deterministic/capability_identity_ledger.json"; ledger.parent.mkdir(); valid={"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}
            for identities,message in (([valid],"valid genesis"),([valid|{"unexpected":"forbidden"}],"malformed intermediate"),([valid],"valid tip")):
                ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":identities})); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm",message],check=True)
            self.assertEqual(["capability identity history is incomplete or untrusted"],self.module.validate_identity_history(repo))

    def test_cap_neg_36_coordinated_new_origin_erasure(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
            for k,v in (("user.email","test@example.invalid"),("user.name","Test")): subprocess.run(["git","-C",str(repo),"config",k,v],check=True)
            ledger=repo/"deterministic/capability_identity_ledger.json"; ledger.parent.mkdir(); ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"new","origin":"new","origin_transition_id":"new-001"}]})); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","new origin"],check=True)
            ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":[]})); subprocess.run(["git","-C",str(repo),"commit","-am","coordinated erase","-q"],check=True)
            self.assertIn("capability identity ledger removed or changed historical record",self.module.validate_identity_history(repo))

    def test_cap_neg_37_untrusted_history_variants(self):
        for case in ("shallow","malformed_ledger","non_descendant","replace","graft"):
            with self.subTest(case=case), tempfile.TemporaryDirectory() as tmp:
                repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
                for k,v in (("user.email","test@example.invalid"),("user.name","Test")): subprocess.run(["git","-C",str(repo),"config",k,v],check=True)
                ledger=repo/"deterministic/capability_identity_ledger.json"; ledger.parent.mkdir(); ledger.write_text(json.dumps({} if case=="malformed_ledger" else {"schema":"capability-identity-ledger-v1","identities":[]})); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","ledger"],check=True)
                if case=="shallow":
                    clone=pathlib.Path(tmp)/"shallow"; subprocess.run(["git","clone","-q","--depth=1","file://"+str(repo),str(clone)],check=True); repo=clone
                if case=="non_descendant": subprocess.run(["git","-C",str(repo),"checkout","--orphan","other"],check=True,capture_output=True); subprocess.run(["git","-C",str(repo),"rm","-rf","."],check=True,capture_output=True); (repo/"other").write_text("x"); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","other"],check=True)
                if case=="replace": subprocess.run(["git","-C",str(repo),"commit","--allow-empty","-qm","replace target"],check=True); subprocess.run(["git","-C",str(repo),"replace","HEAD","HEAD^"],check=True)
                if case=="graft": (repo/".git/info/grafts").write_text("0"*40+"\n")
                self.assertEqual(["capability identity history is incomplete or untrusted"],self.module.validate_identity_history(repo))

    def test_cap_pos_13_clean_c0_and_pos_14_exact_c0_descendant(self):
        self.assertEqual([],self.module.validate_ledger_binding({"schema":"capability-identity-ledger-v1","identities":[]},[],descendant=False))
        with tempfile.TemporaryDirectory() as tmp:
            repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True); subprocess.run(["git","-C",str(repo),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(repo),"config","user.name","Test"],check=True)
            (repo/"seed").write_text("x"); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","c0"],check=True); c0=subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],text=True,capture_output=True,check=True).stdout.strip()
            (repo/"descendant").write_text("x"); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","descendant"],check=True); head=subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],text=True,capture_output=True,check=True).stdout.strip(); self.assertEqual(0,subprocess.run(["git","-C",str(repo),"merge-base","--is-ancestor",c0,head]).returncode)
            self.assertEqual([],self.module.validate_ledger_binding({"schema":"capability-identity-ledger-v1","identities":[]},[],descendant=True))

    def test_cap_neg_38_to_42_new_origin_ledger_bindings(self):
        transition={"transition_id":"T-01","capability_id":"new","sequence":1,"origin":"new","predecessor":None,"successor":"planned"}
        cases={
            "CAP-NEG-38":({"schema":"capability-identity-ledger-v1","identities":[]},[transition],"origin new transition requires exactly one identity ledger record"),
            "CAP-NEG-39":({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"new","origin":"new"}]},[],"origin new identity record references no sequence one transition"),
            "CAP-NEG-41":({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"new","origin":"new"},{"capability_id":"new","origin":"new"}]},[transition],"capability identity ledger id is not unique"),
            "CAP-NEG-40":({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"other","origin":"new"}]},[transition],"origin new identity record capability does not match transition"),
        }
        for case,(ledger,transitions,diagnostic) in cases.items():
            with self.subTest(case=case): self.assertIn(diagnostic,self.module.validate_ledger_binding(ledger,transitions))

    def test_cap_neg_58_origin_new_identity_must_reference_exact_transition_id(self):
        ledger={"schema":"capability-identity-ledger-v1","identities":[{"capability_id":"new","origin":"new","origin_transition_id":"wrong-id"}]}
        transitions=[{"transition_id":"right-id","capability_id":"new","sequence":1,"origin":"new","predecessor":None,"successor":"planned"}]
        self.assertIn("origin new identity record transition id does not match transition",self.module.validate_ledger_binding(ledger,transitions))

    def test_cap_neg_42_baseline_new_origin_conflict(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]}]
        errors=self.module.validate_capability_registry(modules,[{"transition_id":"T","capability_id":"cap","sequence":1,"origin":"new","predecessor":None,"successor":"a"}],["cap"],[{"capability_id":"cap","origin":"new"}])
        self.assertIn("capability identity cannot have both baseline and new origins",errors)

    def test_registry_rejects_unknown_enum_values(self):
        modules=[{"module_id":"a","status":"current_runtime","owned_capabilities":["cap"],"planned_capabilities":[]},{"module_id":"b","status":"target_planned","owned_capabilities":[],"planned_capabilities":["cap"]}]
        transition={"transition_id":"T","capability_id":"cap","sequence":1,"origin":"unknown","predecessor":"a","successor":"b","state":"unknown"}
        errors=self.module.validate_capability_registry(modules,[transition],["cap"],[{"capability_id":"cap","origin":"baseline","baseline_owner":"a"}])
        self.assertIn("capability transition origin is invalid",errors)
        self.assertIn("capability transition state is invalid",errors)

    def test_cap_neg_45_47_49_ledger_schema_has_no_genesis_mirror(self):
        cases={
            "CAP-NEG-45":({"schema":"capability-identity-ledger-v1","genesis":"pending","identities":[]},True,"capability identity ledger schema is invalid"),
            "CAP-NEG-47":({"identities":[]},False,"capability identity ledger schema is invalid"),
            "CAP-NEG-49":({"schema":"unknown","identities":[]},False,"capability identity ledger schema is invalid"),
        }
        for case,(ledger,descendant,diagnostic) in cases.items():
            with self.subTest(case=case): self.assertIn(diagnostic,self.module.validate_ledger_binding(ledger,[],descendant=descendant))
        self.assertEqual([],self.module.validate_ledger_binding({"schema":"capability-identity-ledger-v1","identities":[]},[],descendant=True))

    def test_cap_pos_15_digest_is_canonical(self):
        left=[{"capability_id":"z","origin":"baseline","baseline_owner":"owner-z"},{"capability_id":"a","origin":"new","origin_transition_id":"T-a"}]
        right=[{"origin":"new","origin_transition_id":"T-a","capability_id":"a"},{"baseline_owner":"owner-z","origin":"baseline","capability_id":"z"}]
        self.assertEqual(self.module.canonical_identity_digest(left),self.module.canonical_identity_digest(right))

    def test_cap_limit_01_explicit_limit(self):
        self.assertIn("RISK-HIST-01", (ROOT / "todos/active/process/TODO-uninotas-canonical-foundation-transition.md").read_text())

    def test_cap_neg_43_48_50_51_ledger_rejects_any_genesis_mirror(self):
        oid="a"*40
        cases={
            "CAP-NEG-43":('{"genesis":"'+("b"*40)+'","identities":[]}',oid,"capability identity ledger must not publish genesis"),
            "CAP-NEG-48":('{"genesis":"'+oid+'","genesis":"'+oid+'","identities":[]}',None,"capability identity ledger must not publish genesis"),
            "CAP-NEG-50":('{"schema":"capability-identity-ledger-v1","identities":[]}',None,None),
            "CAP-NEG-51":('{"genesis":"'+("c"*40)+'","identities":[]}',oid,"capability identity ledger must not publish genesis"),
        }
        for case,(text,expected,diagnostic) in cases.items():
            with self.subTest(case=case):
                errors=self.module.validate_ledger_text_binding(text,expected)
                self.assertEqual([],errors) if diagnostic is None else self.assertIn(diagnostic,errors)

    def test_cap_neg_50_active_and_completed_cannot_publish_genesis(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp)
            paths=[]
            for relative in ("todos/active/process/TODO-uninotas-canonical-foundation-transition.md","todos/completed/process/TODO-uninotas-canonical-foundation-transition.md"):
                path=root/relative; path.parent.mkdir(parents=True,exist_ok=True); path.write_text("LEDGER_GENESIS="+("a"*40)); paths.append(relative)
            errors=self.module.validate_lifecycle_genesis_paths([relative for relative in paths if "LEDGER_GENESIS" in (root/relative).read_text()])
        self.assertIn("exactly one canonical lifecycle TODO path may publish LEDGER_GENESIS",errors)

    def test_cap_pos_12_pre_c0_uncommitted_candidate_conditions(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
            (repo/"README").write_text("base"); subprocess.run(["git","-C",str(repo),"add","."],check=True)
            subprocess.run(["git","-C",str(repo),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(repo),"config","user.name","Test"],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","base"],check=True)
            seed=self.module.canonical_identity_digest([])
            self.assertEqual([],self.module.validate_pre_c0_bootstrap(active_todo=True,head_has_ledger=False,seed_digest=seed,expected_seed_digest=seed))
            self.assertTrue(self.module.validate_pre_c0_bootstrap(active_todo=False,head_has_ledger=False,seed_digest=seed,expected_seed_digest=seed))

    def test_cap_neg_44_46_52_53_identity_history_rejects_each_distinct_mutation(self):
        cases={
            "CAP-NEG-44":([[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}],[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"},{"capability_id":"late","origin":"baseline","baseline_owner":"late-owner"}]],"post-genesis capability identities must use origin new"),
            "CAP-NEG-46":([[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}],[{"capability_id":"cap","origin":"new","origin_transition_id":"cap-001"}]],"frozen initial capability identity digest mismatch"),
            "CAP-NEG-52":([[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}],[],[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}]],"capability identity removed then readded"),
            "CAP-NEG-53":([[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}],[{"capability_id":"cap","origin":"new","origin_transition_id":"cap-001"}],[{"capability_id":"cap","origin":"baseline","baseline_owner":"owner"}]],"capability identity mutated then reverted"),
        }
        for case,(versions,diagnostic) in cases.items():
            with self.subTest(case=case), tempfile.TemporaryDirectory() as tmp:
                repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
                for k,v in (("user.email","test@example.invalid"),("user.name","Test")): subprocess.run(["git","-C",str(repo),"config",k,v],check=True)
                path=repo/"deterministic/capability_identity_ledger.json"; path.parent.mkdir()
                for index,identities in enumerate(versions): path.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":identities})); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm",f"v{index}"],check=True)
                self.assertIn(diagnostic,self.module.validate_identity_history(repo))

    def test_cap_pos_11_12_history_budget_and_pending_bootstrap(self):
        self.assertEqual([],self.module.validate_ledger_binding({"schema":"capability-identity-ledger-v1","identities":[]},[],descendant=False))
        with tempfile.TemporaryDirectory() as tmp:
            repo=pathlib.Path(tmp); subprocess.run(["git","init","-q",str(repo)],check=True)
            for k,v in (("user.email","test@example.invalid"),("user.name","Test")): subprocess.run(["git","-C",str(repo),"config",k,v],check=True)
            ledger=repo/"deterministic/capability_identity_ledger.json"; ledger.parent.mkdir()
            for index in range(6):
                ledger.write_text(json.dumps({"schema":"capability-identity-ledger-v1","identities":[{"capability_id":f"cap-{n}","origin":"new","origin_transition_id":f"cap-{n}-001"} for n in range(index+1)]}))
                subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm",f"ledger-{index}"],check=True)
                for unrelated in range(40 if index < 5 else 0):
                    (repo/"unrelated").write_text(f"{index}-{unrelated}"); subprocess.run(["git","-C",str(repo),"add","unrelated"],check=True); subprocess.run(["git","-C",str(repo),"commit","-qm","unrelated"],check=True)
            stats={}; self.assertEqual([],self.module.validate_identity_history(repo,stats=stats))
            self.assertEqual(6,stats["versions"]); self.assertEqual(6,stats["blob_reads"]); self.assertLessEqual(stats["ledger_git_calls"],stats["versions"]+2)
