from __future__ import annotations

from pathlib import Path


TERMINAL_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = TERMINAL_ROOT.parent

QWEN_MODEL_PATH = Path(
    r"E:\52\Train_w\Train\outputs_final\qwen25_15b_qlora_1epoch_20260706_225219\merged_full_model"
)
RELEASE_BILSTM_PATH = Path(r"C:\Hpe\Train\outputs_release_lstm\all_switches\best_model.pt")
PRODUCT_BILSTM_PATH = Path(r"C:\Hpe\Train\outputs_product_lstm\all_switches\best_model.pt")
PRODUCT_VALIDATED_DATA_PATH = Path(
    r"C:\Hpe\Train\Data\aruba_aoscx_product_documentation_dataset_hpe_validated.jsonl"
)
MANUAL_GROUNDED_OVERRIDE_PATH = (
    PROJECT_ROOT / "Data" / "product_docs_final_repaired" / "manual_grounding_overrides.jsonl"
)

RELEASE_DATA_ROOT = PROJECT_ROOT / "Data" / "Release_Notes"
PRODUCT_AGGREGATE_PATHS = [
    PROJECT_ROOT / "Data" / "product_docs_final" / "all_switches_product_dataset_final.jsonl",
    PROJECT_ROOT / "Data" / "product_docs_final_repaired" / "all_switches_product_dataset_final.jsonl",
]
PRODUCT_FALLBACK_ROOTS = [
    PROJECT_ROOT / "Data" / "product_docs_final",
    PROJECT_ROOT / "Data" / "product_docs_final_repaired",
]
SYNTHETIC_DATA_PATHS = [
    PROJECT_ROOT / "imporved_data_addition" / "aruba_aoscx_bilstm_balanced_2040_merged.jsonl",
    PROJECT_ROOT / "imporved_data_addition" / "aruba_aoscx_bilstm_balanced_2040_merged_technical (1).jsonl",
]

ALLOWED_SWITCH_FAMILIES = [
    "10000",
    "10040",
    "4100",
    "4100i",
    "4100i_6100_6200_6300",
    "5420",
    "6000",
    "6100",
    "6200",
    "6200F",
    "6200_6300",
    "6200_6300_6400",
    "6300",
    "6300_6300L_6400",
    "6300_6400",
    "6300_6400_8100_8360",
    "6300_6400_8100_83xx_10000",
    "6400",
    "8100",
    "8100_83xx_9300_10000",
    "8320",
    "8325",
    "8360",
    "8400",
    "9300",
    "9300S_10040",
    "9300s",
    "All AOS-CX",
    "VSF supported switches",
    "VSX supported switches",
]

RELEASE_LIKE_INTENTS = {
    "bug_category",
    "bug_scenario",
    "bug_symptom",
    "bug_workaround",
    "release_caveat",
    "release_date",
}

SYNTAX_LIKE_INTENTS = {
    "cli_syntax",
    "show_command_syntax",
}

INTENT_ALIAS_MAP = {
    "cli_syntax": {"show_command_syntax"},
    "show_command_syntax": {"cli_syntax"},
    "cli_output": {"show_command_meaning", "cli_meaning"},
    "show_command_meaning": {"cli_output", "cli_meaning"},
    "cli_meaning": {"cli_output", "show_command_meaning"},
    "event_id_meaning": {"event_log_meaning"},
    "event_log_meaning": {"event_id_meaning"},
    "limitation": {"release_caveat"},
    "release_caveat": {"limitation"},
}

PRODUCT_INTENT_CANONICAL_MAP = {
    "procedure": "configuration_procedure",
    "configuration": "configuration_procedure",
    "supported_feature": "support_matrix",
    "comparison": "support_matrix",
    "syntax": "cli_syntax",
    "meaning": "cli_meaning",
    "explanation": "concept_explanation",
    "concept": "concept_explanation",
}

CAPACITY_OR_SCALE_KEYWORDS = (
    "route scale",
    "supported route scale",
    "maximum routes",
    "maximum supported routes",
    "route capacity",
    "capacity",
    "member number range",
    "supported capacity",
    "stack members",
)

CAPACITY_OR_SCALE_PENALTY_KEYWORDS = (
    "minimum version",
    "minimum supported version",
    "supports version",
    "supports versions",
    "version support",
    "supported version",
    "supported versions",
    "since which version",
    "from which version",
)

QWEN_MAX_NEW_TOKENS = 220
MIN_LOOKUP_SCORE = 24.0
MIN_MODEL_CONFIDENCE = 0.22
TOP_K_CANDIDATES = 8

SAFE_NO_MATCH = "No reliable matching answer found in the current dataset."
