from __future__ import annotations

import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _env_text(name: str, default: str) -> str:
    value = os.getenv(name)
    return default if value is None or not value.strip() else value.strip()


def _env_path(name: str, default: Path | str) -> Path:
    return Path(_env_text(name, str(default))).expanduser()


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    try:
        return int(value.strip())
    except ValueError:
        return default


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "y", "on"}:
        return True
    if normalized in {"0", "false", "no", "n", "off"}:
        return False
    return default


def _default_allowed_origins() -> list[str]:
    return [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]


def _default_allowed_origin_regex() -> str:
    return (
        r"^(https?://(localhost|127\.0\.0\.1)(:\d+)?"
        r"|https://.*\.ngrok-free\.app"
        r"|https://.*\.ngrok\.app"
        r"|https://.*\.ngrok\.io"
        r"|https://.*\.trycloudflare\.com"
        r")$"
    )


def _resolve_model_file(model_dir: Path, filename: str = "best_model.pt") -> Path:
    if model_dir.suffix:
        return model_dir
    return model_dir / filename


MODEL_ROOT = _env_path("MODEL_ROOT", ROOT / "_bundle_models_used_fullbackend" / "models")
DATA_ROOT = _env_path("DATA_ROOT", ROOT / "Data")

RELEASE_NOTES_DATA_DIR = _env_path("RELEASE_NOTES_DATA_DIR", DATA_ROOT / "Release_Notes")
PRODUCT_DOCS_DATA_DIR = _env_path("PRODUCT_DOCS_DATA_DIR", DATA_ROOT / "product_docs_final_repaired")
RELEASE_LSTM_DATA_DIR = _env_path("RELEASE_LSTM_DATA_DIR", ROOT / "outputs_release_lstm" / "all_switches")
PRODUCT_LSTM_DATA_DIR = _env_path("PRODUCT_LSTM_DATA_DIR", ROOT / "outputs_product_lstm" / "all_switches")

QWEN_MODEL_DIR = _env_path(
    "QWEN_MODEL_DIR",
    MODEL_ROOT / "qwen25_3b_metadatactx_fullclean_1epoch_stratified",
)
RELEASE_LSTM_MODEL_DIR = _env_path("RELEASE_LSTM_MODEL_DIR", RELEASE_LSTM_DATA_DIR)
PRODUCT_LSTM_MODEL_DIR = _env_path("PRODUCT_LSTM_MODEL_DIR", PRODUCT_LSTM_DATA_DIR)
OLLAMA_BASE_URL = _env_text("OLLAMA_BASE_URL", "")

QWEN_MODEL_PATH = QWEN_MODEL_DIR
RELEASE_LOOKUP_DATA_PATH = RELEASE_NOTES_DATA_DIR

RELEASE_LSTM_MODEL_PATH = _resolve_model_file(RELEASE_LSTM_MODEL_DIR)
PRODUCT_LSTM_MODEL_PATH = _resolve_model_file(PRODUCT_LSTM_MODEL_DIR)

RELEASE_LOOKUP_INDEX_PATH = _env_path("RELEASE_LSTM_DATA_DIR", RELEASE_LSTM_DATA_DIR) / "lookup_index.json"
RELEASE_BUG_METADATA_PATH = _env_path("RELEASE_LSTM_DATA_DIR", RELEASE_LSTM_DATA_DIR) / "bug_metadata_index.json"
RELEASE_AVAILABILITY_PATH = _env_path("RELEASE_LSTM_DATA_DIR", RELEASE_LSTM_DATA_DIR) / "availability_index.json"


def _collect_product_lookup_paths(data_root: Path) -> list[Path]:
    search_roots = [data_root]
    parent = data_root.parent
    if parent.exists():
        for sibling_name in ("product_docs_final", "product_docs_final_repaired"):
            sibling_root = parent / sibling_name
            if sibling_root.exists():
                search_roots.append(sibling_root)

    unique_roots: list[Path] = []
    seen_roots: set[Path] = set()
    for root in search_roots:
        resolved_root = root.resolve()
        if resolved_root in seen_roots:
            continue
        seen_roots.add(resolved_root)
        unique_roots.append(root)

    paths: list[Path] = []
    for root in unique_roots:
        paths.extend(path for path in root.rglob("product_dataset_repaired.jsonl") if path.is_file())
        paths.extend(path for path in root.rglob("product_review_remaining.jsonl") if path.is_file())
        paths.extend(path for path in root.rglob("all_switches_product_dataset_final.jsonl") if path.is_file())
        paths.extend(path for path in root.rglob("product_dataset_final.jsonl") if path.is_file())
    synthetic_root = ROOT / "imporved_data_addition"
    if synthetic_root.exists():
        paths.extend(
            path
            for path in synthetic_root.rglob("aruba_aoscx_bilstm_balanced_*_merged.jsonl")
            if path.is_file()
        )
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in sorted(paths):
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(path)
    return unique


PRODUCT_LOOKUP_DATA_PATHS = _collect_product_lookup_paths(PRODUCT_DOCS_DATA_DIR)

FRONTEND_DIR = ROOT / "frontend_v2"
BACKEND_CACHE_DIR = ROOT / "backend_v2_cache"
CHAT_CONVERSATIONS_PATH = BACKEND_CACHE_DIR / "chat_conversations.json"
ALLOWED_ORIGINS = [
    origin.strip()
    for origin in _env_text("ALLOWED_ORIGINS", ",".join(_default_allowed_origins())).split(",")
    if origin.strip()
]
ALLOWED_ORIGIN_REGEX = _env_text("ALLOWED_ORIGIN_REGEX", _default_allowed_origin_regex())
PORT = _env_int("PORT", 8001)
QWEN_FINALIZE_ALL_RESPONSES = _env_bool("QWEN_FINALIZE_ALL_RESPONSES", True)
