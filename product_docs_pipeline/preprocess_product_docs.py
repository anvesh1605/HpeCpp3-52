"""Deterministic preprocessing for Aruba AOS-CX product documentation Markdown.

This pipeline is intentionally separate from release-note preprocessing. It does
not use LangChain, Ollama, OpenAI, or any other LLM for extraction.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from project.src.product_doc_parser import (
    PRODUCT_DOC_FILE_MAP,
    VERSION_RE,
    discover_markdown_files,
    parse_product_doc_file,
    path_metadata,
)
from project.src.product_doc_qa_generator import format_version_for_question, generate_qa_rows
from project.src.product_doc_validator import (
    PRODUCT_DOC_DATA_FAMILY_CAPS,
    command_output_counter_like_count,
    command_output_indicator_count,
    exact_qa_dedupe_key,
    has_balanced_symbols,
    has_balanced_syntax_symbols,
    has_configuration_dump,
    has_final_output_like_damage,
    has_merged_word_damage,
    has_pdf_table_damage,
    has_page_header_fragment,
    has_remaining_table_output,
    has_show_output_table,
    has_spacing_ocr_damage,
    is_bad_final_section,
    is_bullet_fragment_field,
    is_chapter_title_like,
    is_command_metadata_section,
    is_document_title_like,
    is_example_like_text,
    is_example_section_like,
    is_broken_truncated_topic_field,
    is_event_log_source_misclassified_row,
    is_fake_command_heading_row,
    is_final_small_noisy_field,
    is_generic_weak_topic_field,
    is_generic_metadata_section,
    is_hardening_guide_row,
    is_hardening_noisy_field,
    is_page_header_usecase_field,
    is_parameter_description_topic,
    is_long_bad_final_section,
    is_web_ui_fake_cli_row,
    event_id_requested_by_question,
    has_suspicious_erps_expansion,
    merged_word_indicator_count,
    looks_like_parameter_or_syntax_fragment,
    looks_like_command_output_text,
    normalize_multi_syntax,
    question_asks_command_syntax,
    rows_with_grounding,
    spacing_ocr_indicator_count,
    syntax_matches_command,
    validate_qa_row,
    word_count,
)


DEFAULT_FINAL_JSONL = Path("final_json") / "product_docs" / "train_chat_product_docs.jsonl"
MAX_CONCEPT_ANSWER_WORDS = 180
MAX_EVENT_LOG_RATIO = 0.15

TEXT_FIXES = {
    "switchers with multiple management modules": "switches with multiple management modules",
}

TERM_FIXES = {
    "des ired": "desired",
    "manage ment": "management",
    "conso le": "console",
    "login-attem pts": "login-attempts",
    "Associ ation": "Association",
    "add ed": "added",
    "ser ver": "server",
    "co nfigured": "configured",
    "swi tch": "switch",
    "p resent": "present",
    "A lternative": "Alternative",
    "Usernam e": "Username",
    "Authori ze": "Authorize",
    "u ser": "user",
    "privileg e": "privilege",
    "Notif ications": "Notifications",
    "t hreshold": "threshold",
    "Polic ing": "Policing",
    "CLI s": "CLIs",
    "Web-UI": "Web UI",
    "HTTP s": "HTTPS",
    "user-grou p": "user-group",
    "s Flow": "sFlow",
    "s Flow Agent": "sFlow Agent",
    "s Flow Collector": "sFlow Collector",
    "VLAN s": "VLANs",
    "LAG s": "LAGs",
    "VRF s": "VRFs",
    "Qo S": "QoS",
    "Qualityof Service": "Quality of Service",
    "Classof Service": "Class of Service",
    "Diff Serv": "DiffServ",
    "Rad Sec": "RadSec",
    "Air Wave": "AirWave",
    "OSPF v2": "OSPFv2",
    "OSPF v3": "OSPFv3",
    "RIP ng": "RIPng",
    "IP sec": "IPsec",
    "DHCP v4": "DHCPv4",
    "DHCP v6": "DHCPv6",
    "MAC address": "MAC address",
    "IPv4 address": "IPv4 address",
    "IPv6 address": "IPv6 address",
}

OCR_PHRASE_FIXES = {
    "SetsthesourceIPv4addressforBFDechopackets": "Sets the source IPv4 address for BFD echo packets",
    "Thisaddressisusedinallechosessions": "This address is used in all echo sessions",
    "sourceIPv4addressforBFDechopackets": "source IPv4 address for BFD echo packets",
    "sourceIPv4address": "source IPv4 address",
    "forBFDechopackets": "for BFD echo packets",
    "TodisableBFD,issuethecommandwithoutthebfd": "To disable BFD, issue the command without the bfd",
    "TodisableBFD": "To disable BFD",
    "TodilableBFD": "To disable BFD",
    "issuethecommandwithoutthebfd": "issue the command without the bfd",
    "issuethecommand": "issue the command",
    "withoutthebfd": "without the bfd",
    "setsthesource": "sets the source",
    "Setsthesource": "Sets the source",
    "Thisaddressisused": "This address is used",
    "inallechosessions": "in all echo sessions",
    "sourceIPaddress": "source IP address",
    "mustnotbe": "must not be",
    "onthesamenetworksegment": "on the same network segment",
    "anyswitchinterface": "any switch interface",
    "otherwisealarge": "otherwise a large",
    "numberofICMPredirect": "number of ICMP redirect",
    "packetsmaybesent": "packets may be sent",
    "causingnetworkcongestion": "causing network congestion",
    "Thenoformofthiscommand": "The no form of this command",
    "removesthesource": "removes the source",
    "switchtostopsending": "switch to stop sending",
    "Whenavalidvalueisset": "When a valid value is set",
    "receivingechopackets": "receiving echo packets",
    "willstarttransmitting": "will start transmitting",
    "BFDcontrolsessions": "BFD control sessions",
    "continuetorun": "continue to run",
    "concurrentlywithechopackets": "concurrently with echo packets",
    "SpecifiesasessionID": "Specifies a session ID",
    "Specifiestheaddress": "Specifies the address",
    "wherexisadecimalnumber": "where x is a decimal number",
    "Specifiesaroutedestination": "Specifies a route destination",
    "Thedefaultgatewaysforhosts": "The default gateways for hosts",
    "Theautogeneratedsequencenumber": "The autogenerated sequence number",
    "Administratorsorlocalusergroupmembers": "Administrators or local user group members",
    "Commandcontext": "Command context",
    "Remotesyslogenables": "Remote syslog enables",
    "Selectsthe": "Selects the",
    "Specifiesthe": "Specifies the",
    "showthe": "show the",
    "enterthecommand": "enter the command",
    "sourceIPoftheswitch": "source IP of the switch",
    "source IP oftheswitch": "source IP of the switch",
}

QUESTION_UNDERSCORE_VERSION_RE = re.compile(r"\bAOS-CX\s+10_\d{2}(?:_\d{4})?\b", re.IGNORECASE)
MAJOR_CONCEPT_LABEL_RE = re.compile(
    r"(?<!^)(?<!\n)(?P<prefix>\.|\:)\s+"
    r"(?P<label>Terminology:|Supported:|Not supported:|Failover requirements:|"
    r"Standby recovery requirements:|Key parts of the HA feature include:)",
    re.IGNORECASE,
)
WORD_TOKEN_RE = re.compile(r"\S+")
PAGE_HEADER_PATTERNS = (
    re.compile(r"AOS-CX\s+\d+\.\d+.*?Guide\s*\|.*?Switch Series\)?\s*\d*", re.IGNORECASE),
    re.compile(r"AOS-CX\s+\d+\.\d+.*?Guide\s*\|.*", re.IGNORECASE),
    re.compile(r"\|\s*\([^)]+Switch Series\)\s*\d+", re.IGNORECASE),
)


def _path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def _write_json(payload: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def _counter_json(counter: Counter[str]) -> dict[str, int]:
    return dict(sorted(counter.items()))


def _parse_family_cap(values: list[str] | None) -> dict[str, int]:
    caps = dict(PRODUCT_DOC_DATA_FAMILY_CAPS)
    for raw in values or []:
        if "=" not in raw:
            raise ValueError(f"Invalid --family-cap value {raw!r}. Use data_family=limit.")
        family, raw_limit = raw.split("=", 1)
        family = family.strip()
        if not family:
            raise ValueError(f"Invalid --family-cap value {raw!r}. Missing data family.")
        try:
            limit = int(raw_limit)
        except ValueError as exc:
            raise ValueError(f"Invalid cap limit in {raw!r}.") from exc
        if limit < 0:
            raise ValueError(f"Invalid cap limit in {raw!r}. Limit must be >= 0.")
        caps[family] = limit
    return caps


def _path_parts(input_root: Path, file_path: Path) -> tuple[str, ...]:
    try:
        return file_path.relative_to(input_root).parts
    except ValueError:
        return file_path.parts


def _should_process_file(input_root: Path, file_path: Path, switch_name: str, version: str) -> bool:
    parts = _path_parts(input_root, file_path)
    if len(parts) >= 3:
        file_switch = parts[0]
        file_version = parts[1].replace(".", "_")
        if switch_name and file_switch.lower() != switch_name.lower():
            return False
        if version and file_version.lower() != version.replace(".", "_").lower():
            return False
    return True


def _empty_quality_report() -> dict[str, Any]:
    return {
        "input_files": 0,
        "files_processed": 0,
        "files_skipped": 0,
        "total_structured_records": 0,
        "total_qa_rows_before_dedup": 0,
        "total_qa_rows_after_dedup": 0,
        "duplicates_removed": 0,
        "rows_removed_by_validation": 0,
        "rows_removed_by_cap": 0,
        "jsonl_parse_errors": 0,
        "exact_duplicate_qa_pairs": 0,
        "duplicate_questions_found": 0,
        "duplicate_question_rows_dropped": 0,
        "duplicate_questions_final": 0,
        "rows_with_switch_version_grounding": 0,
        "source_type_counts": {},
        "data_family_counts": {},
        "document_title_counts": {},
        "switch_counts": {},
        "version_counts": {},
        "commands_extracted": 0,
        "procedures_extracted": 0,
        "concepts_extracted": 0,
        "examples_extracted": 0,
        "rest_endpoints_extracted": 0,
        "snmp_objects_extracted": 0,
        "event_logs_extracted": 0,
        "chapter_heading_rows_dropped": 0,
        "command_boundary_merges_detected": 0,
        "parameter_rows_dropped_as_noisy": 0,
        "ocr_spacing_damage_rows_dropped": 0,
        "ocr_damage_rows_dropped": 0,
        "page_header_footer_fragments_removed": 0,
        "incomplete_procedure_rows_dropped": 0,
        "command_records_with_clean_description": 0,
        "command_records_missing_description": 0,
        "version_display_fixed_rows": 0,
        "bullet_marker_cleaned_rows": 0,
        "ocr_phrase_fixed_rows": 0,
        "page_number_fragments_removed": 0,
        "spacing_term_fixes_applied": 0,
        "spacing_ocr_rows_fixed": 0,
        "merged_word_rows_fixed": 0,
        "multi_syntax_rows_normalized": 0,
        "multi_syntax_variants_dropped": 0,
        "multi_syntax_rows_dropped": 0,
        "rows_with_underscore_version_in_question": 0,
        "syntax_prompt_fragments_removed": 0,
        "syntax_rows_dropped_due_to_prompt_pollution": 0,
        "long_concept_answers_truncated": 0,
        "configuration_dump_rows_dropped": 0,
        "show_output_table_rows_dropped": 0,
        "bullet_fragment_rows_renamed": 0,
        "bullet_fragment_rows_dropped": 0,
        "page_header_usecase_rows_renamed": 0,
        "page_header_usecase_rows_dropped": 0,
        "final_output_like_rows_dropped": 0,
        "final_small_noisy_rows_dropped": 0,
        "generic_weak_topic_rows_dropped": 0,
        "generic_weak_topic_rows_renamed": 0,
        "remaining_table_output_rows_dropped": 0,
        "broken_truncated_topic_rows_dropped": 0,
        "support_footer_rows_dropped": 0,
        "visual_caption_rows_dropped": 0,
        "syntax_command_root_mismatch_rows_dropped": 0,
        "sibling_command_syntax_mismatch_rows_dropped": 0,
        "orphan_syntax_fragment_rows_dropped": 0,
        "unbalanced_syntax_rows_repaired": 0,
        "unbalanced_syntax_rows_dropped": 0,
        "unbalanced_field_rows_repaired": 0,
        "unbalanced_field_rows_dropped": 0,
        "syntax_context_only_rows_dropped": 0,
        "invalid_syntax_rows_dropped": 0,
        "fake_command_heading_rows_dropped": 0,
        "fake_command_name_rows_dropped": 0,
        "orphan_sequence_number_command_rows_dropped": 0,
        "parameter_rows_generated": 0,
        "command_example_rows_generated": 0,
        "event_log_rows_before_cap": 0,
        "event_log_rows_after_cap": 0,
        "event_log_rows_dropped_by_cap": 0,
        "mixed_file_ocr_damage_rows_dropped": 0,
        "pdf_table_damaged_rows_dropped": 0,
        "spacing_ocr_rows_dropped": 0,
        "bad_procedure_trigger_rows_dropped": 0,
        "hardening_rows_before_validation": 0,
        "hardening_rows_after_validation": 0,
        "hardening_noisy_rows_dropped": 0,
        "generic_overview_rows_renamed": 0,
        "generic_overview_rows_dropped": 0,
        "document_title_rows_dropped": 0,
        "chapter_title_rows_dropped": 0,
        "command_metadata_section_rows_dropped": 0,
        "page_header_fragments_removed_from_answers": 0,
        "rows_dropped_due_to_remaining_page_headers": 0,
        "bad_final_section_rows_dropped": 0,
        "long_bad_section_rows_dropped": 0,
        "parameter_fragment_topic_rows_dropped": 0,
        "parameter_description_topic_rows_dropped": 0,
        "syntax_fragment_topic_rows_dropped": 0,
        "generic_metadata_section_rows_dropped": 0,
        "example_section_rows_dropped": 0,
        "example_like_concept_rows_dropped": 0,
        "web_ui_fake_cli_rows_dropped": 0,
        "syntax_answer_not_short_exact_rows_dropped": 0,
        "event_id_answer_mismatch_rows_dropped": 0,
        "suspicious_erps_expansion_rows_dropped": 0,
        "command_section_repaired_from_command_name": 0,
        "bad_concept_section_rows_dropped": 0,
        "command_output_rows_dropped": 0,
        "bad_output_section_rows_dropped": 0,
        "answer_output_fragment_rows_dropped": 0,
        "answer_boilerplate_rows_dropped": 0,
        "show_command_reference_rows_kept": 0,
        "output_interpretation_rows_generated": 0,
        "output_like_rows_final": 0,
        "event_log_ratio_after_cap": 0.0,
        "document_title_rows_final": 0,
        "chapter_title_rows_final": 0,
        "command_metadata_section_rows_final": 0,
        "generic_metadata_section_rows_final": 0,
        "support_footer_rows_final": 0,
        "visual_caption_rows_final": 0,
        "page_header_rows_final": 0,
        "configuration_dump_rows_final": 0,
        "show_output_table_rows_final": 0,
        "bullet_fragment_rows_final": 0,
        "page_header_usecase_rows_final": 0,
        "final_small_noisy_rows_final": 0,
        "generic_weak_topic_rows_final": 0,
        "remaining_table_output_rows_final": 0,
        "broken_truncated_topic_rows_final": 0,
        "syntax_command_root_mismatch_rows_final": 0,
        "unbalanced_syntax_rows_final": 0,
        "unbalanced_field_rows_final": 0,
        "parameter_fragment_rows_final": 0,
        "parameter_description_topic_rows_final": 0,
        "syntax_prompt_pollution_rows_final": 0,
        "fake_command_heading_rows_final": 0,
        "fake_command_name_rows_final": 0,
        "major_ocr_damage_rows_final": 0,
        "merged_word_rows_dropped": 0,
        "merged_word_rows_final": 0,
        "spacing_ocr_rows_final": 0,
        "pdf_table_damaged_rows_final": 0,
        "example_section_rows_final": 0,
        "example_like_rows_final": 0,
        "web_ui_fake_cli_rows_final": 0,
        "event_log_source_misclassified_rows_final": 0,
        "syntax_answer_not_short_exact_rows_final": 0,
        "event_id_answer_mismatch_rows_final": 0,
        "suspicious_erps_expansion_rows_final": 0,
        "warnings": [],
    }


def _row_messages(row: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]] | None:
    messages = row.get("messages")
    if not isinstance(messages, list) or len(messages) != 2:
        return None
    if not isinstance(messages[0], dict) or not isinstance(messages[1], dict):
        return None
    return messages[0], messages[1]


def normalize_spacing_and_terms(text: str, is_syntax: bool = False) -> str:
    """
    Fix safe spacing/OCR issues while preserving command syntax structures.

    Syntax fields only get conservative whitespace and prompt cleanup. Natural
    language fields also get punctuation, parentheses, and known term fixes.
    """
    raw = str(text or "").replace("\xa0", " ")
    if not raw:
        return ""
    if is_syntax:
        cleaned = re.sub(r"\b(?:switch(?:\([^)]*\))?[>#]|SVOS>)\s*(?:\|\s*)?", "", raw, flags=re.IGNORECASE)
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in cleaned.splitlines()]
        return "\n".join(line for line in lines if line).strip()

    cleaned = _apply_term_fixes(raw)
    cleaned, _ = _apply_ocr_phrase_fixes(cleaned)
    normalized_lines: list[str] = []
    for line in cleaned.splitlines():
        line = re.sub(r"[ \t]+", " ", line).strip()
        line = re.sub(r"\s+([,.;:!?])", r"\1", line)
        line = re.sub(r"([,;!?])(?=\S)", r"\1 ", line)
        line = re.sub(r":(?!//)(?=\S)", ": ", line)
        line = re.sub(r"(?<!\d)\.(?=[A-Z])", ". ", line)
        line = re.sub(r"\(\s+", "(", line)
        line = re.sub(r"\s+\)", ")", line)
        line = re.sub(r"\s{2,}", " ", line).strip()
        if line:
            normalized_lines.append(line)
    return "\n".join(normalized_lines).strip()


def _normalize_text_with_counters(text: str, counters: Counter[str], is_syntax: bool = False) -> str:
    original = str(text or "")
    before_merged_hits = merged_word_indicator_count(original)
    before_spacing_hits = spacing_ocr_indicator_count(original)
    cleaned = normalize_spacing_and_terms(original, is_syntax=is_syntax)
    if cleaned != original:
        counters["spacing_term_fixes_applied"] += 1
    after_merged_hits = merged_word_indicator_count(cleaned)
    if before_merged_hits and after_merged_hits < before_merged_hits:
        counters["merged_word_rows_fixed"] += 1
    after_spacing_hits = spacing_ocr_indicator_count(cleaned)
    if before_spacing_hits and after_spacing_hits < before_spacing_hits:
        counters["spacing_ocr_rows_fixed"] += 1
    return cleaned


def _recover_hardening_topic(text: str) -> str:
    cleaned = str(text or "").strip()
    match = re.fullmatch(r"(?P<title>[A-Z][A-Za-z0-9,() /+&-]{8,90})\s+\d{1,3}", cleaned)
    if not match:
        return cleaned
    title = re.sub(r"\s+", " ", match.group("title")).strip()
    if title and not is_hardening_noisy_field(title):
        return title
    return cleaned


def _repair_hardening_topic_fields(
    row: dict[str, Any],
    user_message: dict[str, Any],
    assistant_message: dict[str, Any],
    counters: Counter[str],
) -> None:
    if not is_hardening_guide_row(row):
        return
    for field in ("section", "topic", "task"):
        value = row.get(field)
        if not isinstance(value, str) or not value:
            continue
        recovered = _recover_hardening_topic(value)
        if recovered == value:
            continue
        row[field] = recovered
        counters["hardening_topic_rows_repaired"] += 1
        for message in (user_message, assistant_message):
            content = str(message.get("content", ""))
            if content:
                message["content"] = content.replace(value, recovered)


def _clean_generated_rows(rows: list[dict[str, Any]]) -> dict[tuple[str, str], Counter[str]]:
    counters_by_group: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    for row in rows:
        message_pair = _row_messages(row)
        if message_pair is None:
            continue
        user_message, assistant_message = message_pair
        group = _group_key(row)
        counters = counters_by_group[group]

        for field in ("document_title", "section", "topic", "task"):
            value = row.get(field)
            if isinstance(value, str) and value:
                row[field] = _normalize_text_with_counters(value, counters)

        _repair_hardening_topic_fields(row, user_message, assistant_message, counters)

        for field in ("command", "syntax"):
            value = row.get(field)
            if isinstance(value, str) and value:
                row[field] = _normalize_text_with_counters(value, counters, is_syntax=True)

        if _repair_command_section(row):
            counters["command_section_repaired_from_command_name"] += 1

        question = str(user_message.get("content", ""))
        fixed_question = _normalize_text_with_counters(question, counters)
        if fixed_question != question:
            user_message["content"] = fixed_question
            question = fixed_question
        version = str(row.get("version", ""))
        version_display = format_version_for_question(version)
        if version and version_display and version != version_display:
            fixed_question = question.replace(f"AOS-CX {version}", f"AOS-CX {version_display}")
            if fixed_question != question:
                user_message["content"] = fixed_question
                question = fixed_question
                counters["version_display_fixed_rows"] += 1

        answer = str(assistant_message.get("content", ""))
        cleaned_answer, answer_counters = _clean_answer_text(answer, row)
        cleaned_answer, multi_syntax_counters = _normalize_multi_syntax_row(row, cleaned_answer)
        assistant_message["content"] = cleaned_answer
        counters.update(answer_counters)
        counters.update(multi_syntax_counters)
    return counters_by_group


def _clean_answer_text(answer: str, row: dict[str, Any]) -> tuple[str, Counter[str]]:
    counters: Counter[str] = Counter()
    text = str(answer or "")
    original_merged_hits = merged_word_indicator_count(text)

    text = _apply_text_fixes(text)
    text = _apply_term_fixes(text)

    text, phrase_fixed = _apply_ocr_phrase_fixes(text)
    if phrase_fixed:
        counters["ocr_phrase_fixed_rows"] += 1

    text, bullet_fixed = _clean_bullet_markers(text)
    if bullet_fixed:
        counters["bullet_marker_cleaned_rows"] += 1

    text, page_header_fragments = _remove_page_header_fragments(text)
    counters["page_header_fragments_removed_from_answers"] += page_header_fragments

    text, page_fragments = _remove_page_number_fragments(text)
    counters["page_number_fragments_removed"] += page_fragments

    text = _clean_repeated_concept_heading(text, row)
    text, concept_counters = _format_concept_answer(text, row)
    counters.update(concept_counters)
    text = _normalize_answer_spacing(text)
    merged_fixed_before_final_spacing = counters["merged_word_rows_fixed"]
    text = _normalize_text_with_counters(text, counters)
    if (
        original_merged_hits
        and merged_word_indicator_count(text) < original_merged_hits
        and counters["merged_word_rows_fixed"] == merged_fixed_before_final_spacing
    ):
        counters["merged_word_rows_fixed"] += 1
    return text, counters


def _syntax_variants_for_count(syntax: str) -> list[str]:
    return [part.strip(" .") for part in str(syntax or "").split(";") if part.strip(" .")]


def _normalize_multi_syntax_row(row: dict[str, Any], answer: str) -> tuple[str, Counter[str]]:
    counters: Counter[str] = Counter()
    if row.get("data_family") not in {"cli_command_reference", "show_command_reference"}:
        return answer, counters
    command = str(row.get("command", "") or "")
    syntax = str(row.get("syntax", "") or "")
    if not command or ";" not in syntax:
        return answer, counters

    original_variants = list(dict.fromkeys(_syntax_variants_for_count(syntax)))
    is_valid, normalized_syntax = normalize_multi_syntax(command, syntax)
    if not is_valid:
        counters["multi_syntax_rows_dropped"] += 1
        return answer, counters

    normalized_variants = [
        line.strip()[2:].strip()
        for line in normalized_syntax.splitlines()
        if line.strip().startswith("- ")
    ] or [normalized_syntax.strip()]
    dropped_variants = max(0, len(original_variants) - len(set(normalized_variants)))
    if dropped_variants:
        counters["multi_syntax_variants_dropped"] += dropped_variants
    if normalized_syntax != syntax:
        row["syntax"] = normalized_syntax
        counters["multi_syntax_rows_normalized"] += 1
        answer = answer.replace(syntax, normalized_syntax)
        answer = re.sub(r"(is:)\s+-\s+", r"\1\n- ", answer, flags=re.IGNORECASE)
        answer = re.sub(r"(Syntax:)\s+-\s+", r"\1\n- ", answer, flags=re.IGNORECASE)
    return answer, counters


def _apply_text_fixes(text: str) -> str:
    cleaned = text
    for source, replacement in TEXT_FIXES.items():
        cleaned = re.sub(re.escape(source), replacement, cleaned, flags=re.IGNORECASE)
    return cleaned


def _apply_term_fixes(text: str) -> str:
    cleaned = str(text or "")
    for source, replacement in TERM_FIXES.items():
        cleaned = re.sub(re.escape(source), replacement, cleaned, flags=re.IGNORECASE)
    return cleaned


def _repair_command_section(row: dict[str, Any]) -> bool:
    if row.get("data_family") not in {"cli_command_reference", "show_command_reference"}:
        return False
    command = str(row.get("command", "") or "").strip()
    section = str(row.get("section", "") or "").strip()
    if not command or not section:
        return False
    if section.lower() == command.lower():
        return False
    row["section"] = command
    return True


def _apply_ocr_phrase_fixes(text: str) -> tuple[str, bool]:
    cleaned = text
    for source, replacement in sorted(OCR_PHRASE_FIXES.items(), key=lambda item: len(item[0]), reverse=True):
        cleaned = cleaned.replace(source, replacement)
    cleaned = re.sub(r",(?=[A-Za-z])", ", ", cleaned)
    cleaned = re.sub(r"\.(?=[A-Z])", ". ", cleaned)
    cleaned = re.sub(r"\b(command)(without)\b", r"\1 \2", cleaned, flags=re.IGNORECASE)
    return cleaned, cleaned != text


def _remove_page_header_fragments(text: str) -> tuple[str, int]:
    cleaned = str(text or "")
    total = 0
    for pattern in PAGE_HEADER_PATTERNS:
        cleaned, count = pattern.subn(" ", cleaned)
        total += count
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned, total


def _clean_bullet_markers(text: str) -> tuple[str, bool]:
    cleaned = text
    cleaned = re.sub(r"(^|[\n.:;])\s+n\s+(?=[A-Z0-9(<])", r"\1\n- ", cleaned)
    cleaned = re.sub(r"(^|[\n.:;])\s+o\s+(?=[A-Z0-9(<])", r"\1\n  - ", cleaned)
    cleaned = re.sub(r"(^|[\n.:;])\s+l\s+(?=[A-Z0-9(<])", r"\1\n    - ", cleaned)
    cleaned = re.sub(r"(?<![A-Za-z0-9])n\s+(?=[A-Z0-9(<])", "\n- ", cleaned)
    cleaned = re.sub(r"(?<![A-Za-z0-9])o\s+(?=[A-Z0-9(<])", "\n  - ", cleaned)
    cleaned = re.sub(r"(?<![A-Za-z0-9])l\s+(?=[A-Z0-9(<])", "\n    - ", cleaned)
    return cleaned, cleaned != text


def _remove_page_number_fragments(text: str) -> tuple[str, int]:
    cleaned, ipv4_count = re.subn(r"\bIPv4\s+\d+\s+-\s+", "IPv4 - ", text)
    cleaned, bullet_count = re.subn(r"\s+\d+\s+(?=(?:\n|\s)*-\s+[A-Z])", " ", cleaned)
    return cleaned, ipv4_count + bullet_count


def _clean_repeated_concept_heading(text: str, row: dict[str, Any]) -> str:
    if row.get("data_family") != "concept_explanation":
        return text
    topic = str(row.get("topic") or row.get("section") or "").strip()
    if not topic:
        return text
    direct_topic = re.sub(r"\s+Overview$", "", topic, flags=re.IGNORECASE).strip()
    cleaned = re.sub(
        rf"^({re.escape(topic)}):\s+\1\b",
        rf"\1:",
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    if direct_topic and direct_topic != topic:
        cleaned = re.sub(rf"^{re.escape(topic)}:", f"{direct_topic}:", cleaned, count=1, flags=re.IGNORECASE)
    return cleaned


def _format_concept_answer(text: str, row: dict[str, Any]) -> tuple[str, Counter[str]]:
    counters: Counter[str] = Counter()
    if row.get("data_family") != "concept_explanation":
        return text, counters
    cleaned = MAJOR_CONCEPT_LABEL_RE.sub(lambda match: f"{match.group('prefix')}\n\n{match.group('label')}", text)
    cleaned = re.sub(
        r"(?<!\n)\s+(Key parts of the HA feature include:|Terminology:|Supported:|Not supported:|"
        r"Failover requirements:|Standby recovery requirements:)",
        r"\n\1",
        cleaned,
        flags=re.IGNORECASE,
    )
    truncated = _truncate_concept_answer(cleaned, MAX_CONCEPT_ANSWER_WORDS)
    if truncated != cleaned:
        counters["long_concept_answers_truncated"] += 1
    return truncated, counters


def _truncate_concept_answer(text: str, max_words: int) -> str:
    tokens = list(WORD_TOKEN_RE.finditer(text))
    if len(tokens) <= max_words:
        return text
    cutoff = tokens[max_words - 1].end()
    boundary_candidates = [
        text.rfind(". ", 0, cutoff),
        text.rfind(".\n", 0, cutoff),
        text.rfind("\n- ", 0, cutoff),
        text.rfind("\n\n", 0, cutoff),
    ]
    boundary = max(boundary_candidates)
    if boundary < max(80, cutoff // 2):
        return text
    if text[boundary : boundary + 2] in {". ", ".\n"}:
        boundary += 1
    return text[:boundary].rstrip()


def _normalize_answer_spacing(text: str) -> str:
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in str(text or "").splitlines()]
    cleaned = "\n".join(line for line in lines if line)
    return cleaned.strip()


def _rows_with_underscore_version(rows: list[dict[str, Any]]) -> int:
    count = 0
    for row in rows:
        message_pair = _row_messages(row)
        if message_pair is None:
            continue
        question = str(message_pair[0].get("content", ""))
        if QUESTION_UNDERSCORE_VERSION_RE.search(question):
            count += 1
    return count


def _duplicate_questions_final(rows: list[dict[str, Any]]) -> int:
    counts = Counter(_question_dedupe_key(row) for row in rows if _question_dedupe_key(row))
    return sum(1 for count in counts.values() if count > 1)


def _assistant_answer(row: dict[str, Any]) -> str:
    pair = _row_messages(row)
    return str(pair[1].get("content", "")) if pair else ""


def _user_question(row: dict[str, Any]) -> str:
    pair = _row_messages(row)
    return str(pair[0].get("content", "")) if pair else ""


def _answer_has_syntax(answer: str) -> bool:
    return bool(re.match(r"^\s*Syntax\s*:\s+\S+", str(answer or ""), re.IGNORECASE))


def _exact_duplicate_row_count(rows: list[dict[str, Any]]) -> int:
    counts = Counter(json.dumps(row, sort_keys=True, ensure_ascii=False) for row in rows)
    return sum(count - 1 for count in counts.values() if count > 1)


def _exact_duplicate_qa_count(rows: list[dict[str, Any]]) -> int:
    counts = Counter(exact_qa_dedupe_key(row) for row in rows)
    return sum(count - 1 for count in counts.values() if count > 1)


def _build_product_doc_repair_validation_report(rows: list[dict[str, Any]]) -> dict[str, Any]:
    family_counts = Counter(str(row.get("data_family", "")) for row in rows)
    missing_messages = 0
    missing_assistant = 0
    missing_cli_command = 0
    missing_syntax_answer = 0
    syntax_answer_not_short = 0
    event_id_mismatch = 0
    suspicious_erps = 0
    syntax_question_rows = 0
    command_description_rows = 0
    show_command_rows = 0
    event_question_rows = 0

    for row in rows:
        messages = row.get("messages")
        if not isinstance(messages, list) or len(messages) != 2:
            missing_messages += 1
            missing_assistant += 1
            continue
        question = _user_question(row)
        answer = _assistant_answer(row)
        family = str(row.get("data_family", ""))
        if not answer:
            missing_assistant += 1
        if family in {"cli_command_reference", "show_command_reference"} and not str(row.get("command", "")).strip():
            missing_cli_command += 1
        if family in {"cli_command_reference", "show_command_reference"} and question_asks_command_syntax(question):
            syntax_question_rows += 1
            if not _answer_has_syntax(answer):
                missing_syntax_answer += 1
                syntax_answer_not_short += 1
        if family == "cli_command_reference" and re.search(r"\bwhat\s+does\b", question, re.IGNORECASE):
            command_description_rows += 1
        if family == "show_command_reference":
            show_command_rows += 1
        if family == "event_log_reference":
            event_question_rows += 1
            requested_event_id = event_id_requested_by_question(question)
            if requested_event_id and requested_event_id not in answer:
                event_id_mismatch += 1
        if has_suspicious_erps_expansion(answer):
            suspicious_erps += 1

    duplicate_question_count = _duplicate_questions_final(rows)
    exact_duplicate_qa_pairs = _exact_duplicate_qa_count(rows)
    exact_duplicate_rows = _exact_duplicate_row_count(rows)
    warnings = []
    warning_checks = {
        "rows_missing_messages": missing_messages,
        "rows_missing_assistant_answer": missing_assistant,
        "rows_missing_command_where_cli_row": missing_cli_command,
        "rows_missing_syntax_in_syntax_answer_rows": missing_syntax_answer,
        "syntax_question_answer_not_short_exact": syntax_answer_not_short,
        "event_id_answer_mismatch_rows": event_id_mismatch,
        "suspicious_erps_expansion_rows": suspicious_erps,
        "duplicate_questions": duplicate_question_count,
        "duplicate_exact_qa_pairs": exact_duplicate_qa_pairs,
        "duplicate_exact_rows": exact_duplicate_rows,
    }
    for key, value in warning_checks.items():
        if value:
            warnings.append(f"{key}: {value}")

    return {
        "total_product_documentation_rows": len(rows),
        "cli_command_reference_count": family_counts.get("cli_command_reference", 0),
        "show_command_reference_count": family_counts.get("show_command_reference", 0),
        "event_log_reference_count": family_counts.get("event_log_reference", 0),
        "syntax_question_rows": syntax_question_rows,
        "command_description_rows": command_description_rows,
        "show_command_rows": show_command_rows,
        "event_question_rows": event_question_rows,
        **warning_checks,
        "counts_by_data_family": _counter_json(family_counts),
        "warnings": warnings,
    }


def _sample_rows_by_kind(rows: list[dict[str, Any]], per_kind: int = 5) -> list[dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = {
        "cli_syntax": [],
        "command_description": [],
        "show_command": [],
        "event_log": [],
    }
    for row in rows:
        family = str(row.get("data_family", ""))
        question = _user_question(row)
        if family == "cli_command_reference" and question_asks_command_syntax(question):
            bucket = "cli_syntax"
        elif family == "cli_command_reference" and re.search(r"\bwhat\s+does\b", question, re.IGNORECASE):
            bucket = "command_description"
        elif family == "show_command_reference":
            bucket = "show_command"
        elif family == "event_log_reference":
            bucket = "event_log"
        else:
            continue
        if len(buckets[bucket]) < per_kind:
            buckets[bucket].append(row)
    samples: list[dict[str, Any]] = []
    for bucket in ("cli_syntax", "command_description", "show_command", "event_log"):
        for row in buckets[bucket]:
            sample = dict(row)
            sample["sample_kind"] = bucket
            samples.append(sample)
    return samples


SUPPORT_FINAL_RE = re.compile(
    r"\b(?:Accessing Aruba Support|Accessing HPE Aruba Networking Support|Accessing Updates|"
    r"Feature Packs|Other useful sites|Documentation feedback|Support and Other Resources|"
    r"HPE Aruba Networking Support Services|Aruba Support Portal|HPE My Networking|"
    r"End-of-Life information|Warranty information|Regulatory information)\b",
    re.IGNORECASE,
)
VISUAL_FINAL_RE = re.compile(r"^(?:Figure\s+\d+|Table\s+\d+|Image\s*\d*|Panel\s*\d*|.*\bpanel\b.*)", re.IGNORECASE)
VISUAL_ANSWER_FINAL_RE = re.compile(r"\b(?:Figure|Table)\s+\d+\s*[\.:]", re.IGNORECASE)
FAKE_COMMAND_FINAL_RE = re.compile(
    r"^(?:If you attempt|Interface\b.*\bis up\b|traceroute to|State is|Unknown Interface Drops|"
    r"Figure\b|Table\b|Chapter\b|AOS-CX\b|Command Information\b|Command History\b)",
    re.IGNORECASE,
)
SYNTAX_PROMPT_FINAL_RE = re.compile(r"\b(?:switch(?:\([^)]*\))?[>#]|SVOS>)", re.IGNORECASE)
MAJOR_OCR_DAMAGE_FINAL_RE = re.compile(
    r"\b(?:todisable|issuethe|withoutthe|thenoformofthiscommand|commandscontext|"
    r"aos-cx10\.\d+|high availability \|)\b",
    re.IGNORECASE,
)
OUTPUT_SENSITIVE_FINAL_FAMILIES = {
    "concept_explanation",
    "routing_feature",
    "security_policy",
    "qos_policy",
    "monitoring_feature",
    "feature_limitation",
    "configuration_procedure",
    "web_ui_task",
    "troubleshooting",
}


def _message_text(row: dict[str, Any], index: int) -> str:
    pair = _row_messages(row)
    if pair is None:
        return ""
    return str(pair[index].get("content", ""))


def _final_field_values(row: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get(field, "") or "").strip()
        for field in ("section", "topic", "task", "command")
        if str(row.get(field, "") or "").strip()
    )


def _balanced_final_field_values(row: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get(field, "") or "").strip()
        for field in ("section", "topic", "task", "command", "syntax")
        if str(row.get(field, "") or "").strip()
    )


def _fake_command_name_final(row: dict[str, Any]) -> bool:
    command = str(row.get("command", "") or "").strip()
    if not command:
        return False
    if FAKE_COMMAND_FINAL_RE.search(command):
        return True
    if word_count(command) > 10:
        return True
    return command.count(",") > 2 or command.count(".") > 2 or "guide |" in command.lower()


def _final_issue_counts(rows: list[dict[str, Any]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        fields = _final_field_values(row)
        question = _message_text(row, 0)
        answer = _message_text(row, 1)
        section_blob = " ".join(fields)
        if any(is_document_title_like(value) for value in fields) or re.search(
            r"\bwhat does the guide say about AOS-CX\s+\d+\.\d+", question, re.IGNORECASE
        ):
            counts["document_title_rows_final"] += 1
        if any(is_chapter_title_like(value) for value in fields) or re.search(
            r"\bwhat does the guide say about Chapter\s+\d+\b", question, re.IGNORECASE
        ):
            counts["chapter_title_rows_final"] += 1
        if any(is_command_metadata_section(value) for value in fields):
            counts["command_metadata_section_rows_final"] += 1
        if any(is_generic_metadata_section(value) for value in fields):
            counts["generic_metadata_section_rows_final"] += 1
        if any(is_example_section_like(value) for value in fields) or re.search(
            r"\bwhat does the guide say about Examples?(?:\s*:|\s+of\b|\s+using\b|\b)",
            question,
            re.IGNORECASE,
        ):
            counts["example_section_rows_final"] += 1
        if any(is_example_like_text(value) for value in fields) or re.search(
            r"(?:Classifier policies configuration example|<VLAN-LIST>\s+command,\s*for example|"
            r"\bconfiguration example\b|,\s*for example\b|Example success message|Example HTML source)",
            question,
            re.IGNORECASE,
        ):
            counts["example_like_rows_final"] += 1
        if is_web_ui_fake_cli_row(row):
            counts["web_ui_fake_cli_rows_final"] += 1
        if is_event_log_source_misclassified_row(row):
            counts["event_log_source_misclassified_rows_final"] += 1
        if (
            str(row.get("data_family", "")) in {"cli_command_reference", "show_command_reference"}
            and question_asks_command_syntax(question)
            and not answer.strip().startswith("Syntax:")
        ):
            counts["syntax_answer_not_short_exact_rows_final"] += 1
        requested_event_id = event_id_requested_by_question(question)
        if (
            str(row.get("data_family", "")) == "event_log_reference"
            and requested_event_id
            and requested_event_id not in answer
        ):
            counts["event_id_answer_mismatch_rows_final"] += 1
        if has_suspicious_erps_expansion(answer):
            counts["suspicious_erps_expansion_rows_final"] += 1
        if SUPPORT_FINAL_RE.search(section_blob) or SUPPORT_FINAL_RE.search(question):
            counts["support_footer_rows_final"] += 1
        if (
            VISUAL_FINAL_RE.match(section_blob)
            or re.search(r"\b(?:Figure\s+\d+|Table\s+\d+|Panel)\b", question, re.IGNORECASE)
            or VISUAL_ANSWER_FINAL_RE.search(answer)
        ):
            counts["visual_caption_rows_final"] += 1
        if has_page_header_fragment(answer):
            counts["page_header_rows_final"] += 1
        if has_configuration_dump(row, answer):
            counts["configuration_dump_rows_final"] += 1
        if has_show_output_table(row, answer):
            counts["show_output_table_rows_final"] += 1
        if any(is_bullet_fragment_field(value) for value in fields):
            counts["bullet_fragment_rows_final"] += 1
        if any(is_page_header_usecase_field(value) for value in fields):
            counts["page_header_usecase_rows_final"] += 1
        if str(row.get("data_family", "")) in OUTPUT_SENSITIVE_FINAL_FAMILIES:
            if any(is_final_small_noisy_field(value) for value in fields):
                counts["final_small_noisy_rows_final"] += 1
            if any(is_generic_weak_topic_field(value) for value in fields):
                counts["generic_weak_topic_rows_final"] += 1
            if any(is_broken_truncated_topic_field(value) for value in fields):
                counts["broken_truncated_topic_rows_final"] += 1
        if has_remaining_table_output(row, answer):
            counts["remaining_table_output_rows_final"] += 1
        command = str(row.get("command", "") or "").strip()
        syntax = str(row.get("syntax", "") or "").strip()
        if command and syntax and not syntax_matches_command(command, syntax):
            counts["syntax_command_root_mismatch_rows_final"] += 1
        if command and syntax and not has_balanced_syntax_symbols(syntax):
            counts["unbalanced_syntax_rows_final"] += 1
        if any(not has_balanced_symbols(value) for value in _balanced_final_field_values(row)):
            counts["unbalanced_field_rows_final"] += 1
        if _fake_command_name_final(row):
            counts["fake_command_name_rows_final"] += 1
        if is_fake_command_heading_row(row):
            counts["fake_command_heading_rows_final"] += 1
        if command and is_long_bad_final_section(command, command):
            counts["long_bad_section_rows_final"] += 1
        elif any(is_long_bad_final_section(value, command) for value in fields):
            counts["long_bad_section_rows_final"] += 1
        if syntax and SYNTAX_PROMPT_FINAL_RE.search(syntax):
            counts["syntax_prompt_pollution_rows_final"] += 1
        if MAJOR_OCR_DAMAGE_FINAL_RE.search(answer):
            counts["major_ocr_damage_rows_final"] += 1
        if str(row.get("data_family", "")) in OUTPUT_SENSITIVE_FINAL_FAMILIES:
            output_text = " ".join(
                str(row.get(field, "") or "") for field in ("section", "topic", "task", "command")
            )
            if any(looks_like_parameter_or_syntax_fragment(value) for value in fields) or looks_like_parameter_or_syntax_fragment(question):
                counts["parameter_fragment_rows_final"] += 1
            if str(row.get("data_family", "")) not in {"cli_command_reference", "show_command_reference"} and any(
                is_parameter_description_topic(str(row.get(field, "") or ""))
                for field in ("section", "topic", "task")
            ):
                counts["parameter_description_topic_rows_final"] += 1
            if (
                looks_like_command_output_text(output_text + " " + question)
                or command_output_indicator_count(answer) >= 2
                or command_output_counter_like_count(answer) >= 4
                or has_final_output_like_damage(row, answer)
            ):
                counts["output_like_rows_final"] += 1
        answer_merged_hits = merged_word_indicator_count(answer)
        if (
            any(has_merged_word_damage(value) for value in fields)
            or has_merged_word_damage(question)
            or answer_merged_hits >= 2
            or (
                str(row.get("data_family", "")) in {"configuration_procedure", "web_ui_task", "troubleshooting"}
                and answer_merged_hits > 0
            )
        ):
            counts["merged_word_rows_final"] += 1
        if has_spacing_ocr_damage(" ".join((*fields, question, answer))):
            counts["spacing_ocr_rows_final"] += 1
        if has_pdf_table_damage(row, answer):
            counts["pdf_table_damaged_rows_final"] += 1
    return counts


def _build_quality_report(
    group_key: tuple[str, str],
    group_files: list[Path],
    processed_files: set[Path],
    skipped_files: set[Path],
    records: list[dict[str, Any]],
    generated_rows_count: int,
    valid_rows_before_dedup_count: int,
    final_rows: list[dict[str, Any]],
    duplicates_removed: int,
    duplicate_questions_found: int,
    duplicate_question_rows_dropped: int,
    validation_drops: Counter[str],
    rows_removed_by_cap: int,
    extraction_counters: Counter[str],
    cleanup_counters: Counter[str],
    event_cap_counters: Counter[str],
    warnings: list[str],
) -> dict[str, Any]:
    switch, version = group_key
    report = _empty_quality_report()
    report.update(
        {
            "input_files": len(group_files),
            "files_processed": sum(1 for path in group_files if path in processed_files),
            "files_skipped": sum(1 for path in group_files if path in skipped_files),
            "total_structured_records": len(records),
            "total_rows": len(final_rows),
            "total_qa_rows_generated": generated_rows_count,
            "total_qa_rows_before_dedup": valid_rows_before_dedup_count,
            "total_qa_rows_after_dedup": len(final_rows),
            "duplicates_removed": duplicates_removed,
            "exact_duplicate_qa_pairs": sum(
                count - 1
                for count in Counter(exact_qa_dedupe_key(row) for row in final_rows).values()
                if count > 1
            ),
            "jsonl_parse_errors": 0,
            "duplicate_questions_found": duplicate_questions_found,
            "duplicate_question_rows_dropped": duplicate_question_rows_dropped,
            "duplicate_questions_final": _duplicate_questions_final(final_rows),
            "rows_removed_by_validation": sum(validation_drops.values()),
            "validation_drop_reasons": _counter_json(validation_drops),
            "rows_removed_by_cap": rows_removed_by_cap,
            "rows_with_switch_version_grounding": rows_with_grounding(final_rows),
            "source_type_counts": _counter_json(Counter(str(row.get("source_type", "")) for row in final_rows)),
            "data_family_counts": _counter_json(Counter(str(row.get("data_family", "")) for row in final_rows)),
            "document_title_counts": _counter_json(Counter(str(row.get("document_title", "")) for row in final_rows)),
            "switch_counts": _counter_json(Counter(str(row.get("switch", "")) for row in final_rows)) or {switch: 0},
            "version_counts": _counter_json(Counter(str(row.get("version", "")) for row in final_rows)) or {version: 0},
            "commands_extracted": extraction_counters["commands_extracted"],
            "procedures_extracted": extraction_counters["procedures_extracted"],
            "concepts_extracted": extraction_counters["concepts_extracted"],
            "examples_extracted": extraction_counters["examples_extracted"],
            "rest_endpoints_extracted": extraction_counters["rest_endpoints_extracted"],
            "snmp_objects_extracted": extraction_counters["snmp_objects_extracted"],
            "event_logs_extracted": extraction_counters["event_logs_extracted"],
            "chapter_heading_rows_dropped": extraction_counters["chapter_heading_rows_dropped"]
            + validation_drops["chapter_heading_row"],
            "command_boundary_merges_detected": extraction_counters["command_boundary_merges_detected"],
            "parameter_rows_dropped_as_noisy": extraction_counters["parameter_rows_dropped_as_noisy"]
            + validation_drops["noisy_parameter_row"],
            "ocr_spacing_damage_rows_dropped": validation_drops["ocr_spacing_damage"],
            "ocr_damage_rows_dropped": validation_drops["ocr_spacing_damage"],
            "page_header_footer_fragments_removed": extraction_counters["page_header_footer_fragments_removed"],
            "incomplete_procedure_rows_dropped": extraction_counters["incomplete_procedure_rows_dropped"]
            + validation_drops["incomplete_procedure"],
            "command_records_with_clean_description": extraction_counters["command_records_with_clean_description"],
            "command_records_missing_description": extraction_counters["command_records_missing_description"],
            "version_display_fixed_rows": cleanup_counters["version_display_fixed_rows"],
            "bullet_marker_cleaned_rows": cleanup_counters["bullet_marker_cleaned_rows"],
            "ocr_phrase_fixed_rows": cleanup_counters["ocr_phrase_fixed_rows"],
            "page_number_fragments_removed": cleanup_counters["page_number_fragments_removed"],
            "spacing_term_fixes_applied": cleanup_counters["spacing_term_fixes_applied"],
            "spacing_ocr_rows_fixed": cleanup_counters["spacing_ocr_rows_fixed"],
            "merged_word_rows_fixed": cleanup_counters["merged_word_rows_fixed"],
            "multi_syntax_rows_normalized": cleanup_counters["multi_syntax_rows_normalized"],
            "multi_syntax_variants_dropped": cleanup_counters["multi_syntax_variants_dropped"],
            "multi_syntax_rows_dropped": validation_drops["multi_syntax"],
            "rows_with_underscore_version_in_question": _rows_with_underscore_version(final_rows),
            "syntax_prompt_fragments_removed": extraction_counters["syntax_prompt_fragments_removed"],
            "syntax_rows_dropped_due_to_prompt_pollution": validation_drops["syntax_prompt_pollution"],
            "long_concept_answers_truncated": cleanup_counters["long_concept_answers_truncated"],
            "configuration_dump_rows_dropped": validation_drops["configuration_dump"],
            "show_output_table_rows_dropped": validation_drops["show_output_table"],
            "bullet_fragment_rows_renamed": cleanup_counters["bullet_fragment_rows_renamed"],
            "bullet_fragment_rows_dropped": validation_drops["bullet_fragment"],
            "page_header_usecase_rows_renamed": cleanup_counters["page_header_usecase_rows_renamed"],
            "page_header_usecase_rows_dropped": validation_drops["page_header_usecase"],
            "final_output_like_rows_dropped": validation_drops["final_output_like"],
            "final_small_noisy_rows_dropped": validation_drops["final_small_noisy"],
            "generic_weak_topic_rows_dropped": validation_drops["generic_weak_topic"],
            "generic_weak_topic_rows_renamed": cleanup_counters["generic_weak_topic_rows_renamed"],
            "remaining_table_output_rows_dropped": validation_drops["remaining_table_output"],
            "broken_truncated_topic_rows_dropped": validation_drops["broken_truncated_topic"],
            "support_footer_rows_dropped": extraction_counters["support_footer_rows_dropped"]
            + validation_drops["support_footer"],
            "visual_caption_rows_dropped": extraction_counters["visual_caption_rows_dropped"]
            + validation_drops["visual_caption"],
            "syntax_command_root_mismatch_rows_dropped": validation_drops["syntax_command_root_mismatch"],
            "sibling_command_syntax_mismatch_rows_dropped": validation_drops[
                "sibling_command_syntax_mismatch"
            ],
            "orphan_syntax_fragment_rows_dropped": validation_drops["orphan_syntax_fragment"],
            "unbalanced_syntax_rows_repaired": 0,
            "unbalanced_syntax_rows_dropped": validation_drops["unbalanced_syntax"],
            "unbalanced_field_rows_repaired": 0,
            "unbalanced_field_rows_dropped": validation_drops["unbalanced_field"],
            "syntax_context_only_rows_dropped": validation_drops["syntax_context_only"],
            "invalid_syntax_rows_dropped": validation_drops["invalid_syntax"],
            "fake_command_heading_rows_dropped": validation_drops["fake_command_heading"],
            "fake_command_name_rows_dropped": validation_drops["fake_command_name"],
            "orphan_sequence_number_command_rows_dropped": validation_drops["orphan_sequence_number_command"],
            "orphan_command_fragment_rows_dropped": validation_drops["orphan_sequence_number_command"]
            + validation_drops["syntax_context_only"]
            + validation_drops["syntax_prompt_pollution"]
            + validation_drops["orphan_syntax_fragment"],
            "parameter_rows_generated": sum(
                1 for row in final_rows if row.get("data_family") == "command_parameter_reference"
            ),
            "command_example_rows_generated": sum(
                1 for row in final_rows if row.get("data_family") == "command_example"
            ),
            "event_log_rows_before_cap": event_cap_counters["event_log_rows_before_cap"],
            "event_log_rows_after_cap": event_cap_counters["event_log_rows_after_cap"],
            "event_log_rows_dropped_by_cap": event_cap_counters["event_log_rows_dropped_by_cap"],
            "event_log_ratio_after_cap": round(
                event_cap_counters["event_log_rows_after_cap"] / len(final_rows), 4
            )
            if final_rows
            else 0.0,
            "mixed_file_ocr_damage_rows_dropped": validation_drops["mixed_file_ocr_damage"],
            "pdf_table_damaged_rows_dropped": validation_drops["pdf_table_damaged"],
            "spacing_ocr_rows_dropped": validation_drops["spacing_ocr_damage"],
            "bad_procedure_trigger_rows_dropped": validation_drops["bad_procedure_trigger"],
            "hardening_rows_after_validation": sum(1 for row in final_rows if is_hardening_guide_row(row)),
            "hardening_noisy_rows_dropped": validation_drops["hardening_noisy"],
            "hardening_rows_before_validation": sum(1 for row in final_rows if is_hardening_guide_row(row))
            + validation_drops["hardening_noisy"],
            "generic_overview_rows_renamed": extraction_counters["generic_overview_rows_renamed"],
            "generic_overview_rows_dropped": extraction_counters["generic_overview_rows_dropped"]
            + validation_drops["generic_overview"],
            "document_title_rows_dropped": validation_drops["document_title"],
            "chapter_title_rows_dropped": extraction_counters["chapter_heading_rows_dropped"]
            + validation_drops["chapter_title"]
            + validation_drops["chapter_heading_row"],
            "command_metadata_section_rows_dropped": validation_drops["command_metadata_section"],
            "page_header_fragments_removed_from_answers": cleanup_counters["page_header_fragments_removed_from_answers"],
            "rows_dropped_due_to_remaining_page_headers": validation_drops["remaining_page_header"],
            "bad_final_section_rows_dropped": validation_drops["bad_final_section"],
            "long_bad_section_rows_dropped": validation_drops["long_bad_section"],
            "parameter_fragment_topic_rows_dropped": validation_drops["parameter_fragment_topic"],
            "parameter_description_topic_rows_dropped": validation_drops["parameter_description_topic"],
            "syntax_fragment_topic_rows_dropped": validation_drops["syntax_fragment_topic"],
            "generic_metadata_section_rows_dropped": validation_drops["generic_metadata_section"],
            "example_section_rows_dropped": validation_drops["example_section"],
            "example_like_concept_rows_dropped": validation_drops["example_like_concept"],
            "web_ui_fake_cli_rows_dropped": validation_drops["web_ui_fake_cli"],
            "syntax_answer_not_short_exact_rows_dropped": validation_drops["syntax_answer_not_short_exact"],
            "event_id_answer_mismatch_rows_dropped": validation_drops["event_id_answer_mismatch"],
            "suspicious_erps_expansion_rows_dropped": validation_drops["suspicious_erps_expansion"],
            "command_section_repaired_from_command_name": cleanup_counters[
                "command_section_repaired_from_command_name"
            ],
            "bad_concept_section_rows_dropped": validation_drops["bad_concept_section"],
            "command_output_rows_dropped": validation_drops["command_output"]
            + validation_drops["bad_output_section"]
            + validation_drops["answer_output_fragment"],
            "bad_output_section_rows_dropped": validation_drops["bad_output_section"],
            "answer_output_fragment_rows_dropped": validation_drops["answer_output_fragment"],
            "answer_boilerplate_rows_dropped": validation_drops["answer_boilerplate"],
            "merged_word_rows_dropped": validation_drops["merged_word_damage"],
            "show_command_reference_rows_kept": sum(
                1 for row in final_rows if row.get("data_family") == "show_command_reference"
            ),
            "output_interpretation_rows_generated": 0,
            "warnings": warnings,
        }
    )
    report.update(_final_issue_counts(final_rows))
    return report


def _group_key(record: dict[str, Any]) -> tuple[str, str]:
    return str(record.get("switch", "unknown_from_product_doc")), str(record.get("version", "unknown_version"))


def _group_key_for_file(input_root: Path, file_path: Path, switch_override: str, version_override: str) -> tuple[str, str]:
    metadata = path_metadata(input_root, file_path, switch_override=switch_override, version_override=version_override)
    return metadata["switch"], metadata["version"]


def _parse_product_doc_worker(payload: tuple[int, Path, Path, str, str]) -> tuple[int, tuple[str, str], Path, list[dict[str, Any]], dict[str, Any]]:
    index, input_root, md_file, switch_name, version = payload
    group = _group_key_for_file(input_root, md_file, switch_name, version)
    parsed_records, file_info = parse_product_doc_file(
        input_root=input_root,
        file_path=md_file,
        switch_override=switch_name,
        version_override=version,
    )
    return index, group, md_file, parsed_records, file_info


def _trim_max_rows(rows: list[dict[str, Any]], max_rows: int | None) -> tuple[list[dict[str, Any]], int]:
    if not max_rows or max_rows < 0 or len(rows) <= max_rows:
        return rows, 0
    return rows[:max_rows], len(rows) - max_rows


def _validate_rows_by_group(
    rows: list[dict[str, Any]],
    require_grounding: bool,
) -> tuple[list[dict[str, Any]], Counter[str], dict[tuple[str, str], Counter[str]], Counter[tuple[str, str]]]:
    valid_rows: list[dict[str, Any]] = []
    global_drops: Counter[str] = Counter()
    group_drops: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    generated_count_by_group: Counter[tuple[str, str]] = Counter()
    for row in rows:
        group = _group_key(row)
        generated_count_by_group[group] += 1
        valid, reason = validate_qa_row(row, require_grounding=require_grounding)
        if valid:
            valid_rows.append(row)
        else:
            global_drops[reason] += 1
            group_drops[group][reason] += 1
    return valid_rows, global_drops, group_drops, generated_count_by_group


def _dedupe_rows_by_group(
    rows: list[dict[str, Any]],
    enabled: bool,
) -> tuple[list[dict[str, Any]], int, Counter[tuple[str, str]]]:
    if not enabled:
        return rows, 0, Counter()
    seen: set[str] = set()
    kept: list[dict[str, Any]] = []
    duplicates_removed = 0
    duplicate_by_group: Counter[tuple[str, str]] = Counter()
    for row in rows:
        key = exact_qa_dedupe_key(row)
        if key in seen:
            duplicates_removed += 1
            duplicate_by_group[_group_key(row)] += 1
            continue
        seen.add(key)
        kept.append(row)
    return kept, duplicates_removed, duplicate_by_group


def _question_dedupe_key(row: dict[str, Any]) -> str:
    pair = _row_messages(row)
    question = str(pair[0].get("content", "")) if pair else ""
    return re.sub(r"\s+", " ", question).strip().lower()


def _answer_quality_score(row: dict[str, Any]) -> float:
    pair = _row_messages(row)
    answer = str(pair[1].get("content", "")) if pair else ""
    command = str(row.get("command", "") or "")
    syntax = str(row.get("syntax", "") or "")
    score = 0.0
    if command and syntax:
        if syntax_matches_command(command, syntax) and has_balanced_syntax_symbols(syntax):
            score += 50
        else:
            score -= 100
    if has_page_header_fragment(answer):
        score -= 30
    if command_output_indicator_count(answer) >= 2 or command_output_counter_like_count(answer) >= 4:
        score -= 25
    if re.search(r"\b(?:Guide\s*\||Command Information|Command History|Switch Series\))\b", answer, re.IGNORECASE):
        score -= 20
    if re.search(r"\b(?:todisable|issuethe|withoutthe|thenoformofthiscommand)\b", answer, re.IGNORECASE):
        score -= 20
    words = word_count(answer)
    if 12 <= words <= 180:
        score += 10
    if words > 220:
        score -= min(30, (words - 220) / 10)
    if words < 8:
        score -= 30
    family = str(row.get("data_family", ""))
    if family in {"cli_command_reference", "show_command_reference"} and command:
        score += 8
    if family == "event_log_reference":
        score -= 2
    return score


def _dedupe_rows_by_question(
    rows: list[dict[str, Any]],
    enabled: bool,
) -> tuple[list[dict[str, Any]], int, int, Counter[tuple[str, str]], Counter[tuple[str, str]]]:
    if not enabled:
        return rows, 0, 0, Counter(), Counter()
    buckets: dict[str, list[tuple[int, dict[str, Any]]]] = defaultdict(list)
    for index, row in enumerate(rows):
        key = _question_dedupe_key(row)
        if key:
            buckets[key].append((index, row))
    duplicate_questions_found = sum(1 for bucket in buckets.values() if len(bucket) > 1)
    if not duplicate_questions_found:
        return rows, 0, 0, Counter(), Counter()

    keep_ids: set[int] = set()
    found_by_group: Counter[tuple[str, str]] = Counter()
    dropped_by_group: Counter[tuple[str, str]] = Counter()
    duplicate_rows_dropped = 0

    for bucket in buckets.values():
        if len(bucket) == 1:
            keep_ids.add(id(bucket[0][1]))
            continue
        best_index, best_row = max(bucket, key=lambda item: (_answer_quality_score(item[1]), -item[0]))
        keep_ids.add(id(best_row))
        found_by_group[_group_key(best_row)] += 1
        for _, row in bucket:
            if row is best_row:
                continue
            duplicate_rows_dropped += 1
            dropped_by_group[_group_key(row)] += 1

    # Preserve original order for deterministic output.
    kept = [row for row in rows if id(row) in keep_ids]
    return kept, duplicate_questions_found, duplicate_rows_dropped, found_by_group, dropped_by_group


def _cap_rows_by_group(
    rows: list[dict[str, Any]],
    enabled: bool,
    caps: dict[str, int],
) -> tuple[list[dict[str, Any]], int, Counter[str], Counter[tuple[str, str]]]:
    if not enabled:
        return rows, 0, Counter(), Counter()
    counts: Counter[str] = Counter()
    cap_drops: Counter[str] = Counter()
    cap_removed_by_group: Counter[tuple[str, str]] = Counter()
    kept: list[dict[str, Any]] = []
    for row in rows:
        family = str(row.get("data_family", "concept_explanation"))
        limit = caps.get(family)
        if limit is not None and counts[family] >= limit:
            cap_drops[family] += 1
            cap_removed_by_group[_group_key(row)] += 1
            continue
        counts[family] += 1
        kept.append(row)
    return kept, sum(cap_drops.values()), cap_drops, cap_removed_by_group


def _is_event_log_row_for_cap(row: dict[str, Any]) -> bool:
    if row.get("data_family") == "event_log_reference":
        return True
    source_type = normalize_report_key(row.get("source_type", ""))
    topic_blob = normalize_report_key(
        " ".join(str(row.get(field, "") or "") for field in ("section", "topic", "task", "document_title"))
    )
    return "event_log" in source_type or "event log" in topic_blob or "event logs" in topic_blob


def _event_bucket_key(row: dict[str, Any]) -> tuple[str, str]:
    return normalize_report_key(row.get("source_file", "")), normalize_report_key(row.get("section", ""))


def normalize_report_key(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().lower()


def _select_diverse_event_rows(event_rows: list[dict[str, Any]], limit: int) -> set[int]:
    if limit <= 0:
        return set()
    buckets: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in event_rows:
        buckets[_event_bucket_key(row)].append(row)
    selected: set[int] = set()
    bucket_keys = sorted(buckets, key=lambda key: (len(buckets[key]), key))
    while len(selected) < limit:
        progressed = False
        for key in bucket_keys:
            bucket = buckets[key]
            if not bucket:
                continue
            selected.add(id(bucket.pop(0)))
            progressed = True
            if len(selected) >= limit:
                break
        if not progressed:
            break
    return selected


def _cap_event_log_rows_by_ratio(
    rows: list[dict[str, Any]],
    enabled: bool,
    max_ratio: float = MAX_EVENT_LOG_RATIO,
) -> tuple[list[dict[str, Any]], Counter[str], dict[tuple[str, str], Counter[str]]]:
    stats: Counter[str] = Counter()
    stats_by_group: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    event_rows = [row for row in rows if _is_event_log_row_for_cap(row)]
    non_event_count = len(rows) - len(event_rows)

    stats["event_log_rows_before_cap"] = len(event_rows)
    for row in event_rows:
        stats_by_group[_group_key(row)]["event_log_rows_before_cap"] += 1

    if not enabled or not event_rows or non_event_count <= 0:
        kept_rows = rows
        selected_event_ids = {id(row) for row in event_rows}
    else:
        max_event_rows = int((max_ratio * non_event_count) / max(0.0001, 1.0 - max_ratio))
        max_event_rows = max(0, min(len(event_rows), max_event_rows))
        selected_event_ids = _select_diverse_event_rows(event_rows, max_event_rows)
        kept_rows = [
            row
            for row in rows
            if not _is_event_log_row_for_cap(row) or id(row) in selected_event_ids
        ]

    kept_event_count = sum(1 for row in kept_rows if _is_event_log_row_for_cap(row))
    stats["event_log_rows_after_cap"] = kept_event_count
    stats["event_log_rows_dropped_by_cap"] = len(event_rows) - kept_event_count

    for row in event_rows:
        group = _group_key(row)
        if id(row) in selected_event_ids:
            stats_by_group[group]["event_log_rows_after_cap"] += 1
        else:
            stats_by_group[group]["event_log_rows_dropped_by_cap"] += 1
    return kept_rows, stats, stats_by_group


def run(args: argparse.Namespace) -> dict[str, Any]:
    input_root = args.input_root
    output_root = args.output_root
    final_jsonl = args.final_jsonl
    family_caps = _parse_family_cap(args.family_cap)

    all_files = discover_markdown_files(input_root)
    selected_files = [
        path
        for path in all_files
        if _should_process_file(input_root, path, args.switch_name, args.version)
    ]
    if args.max_files:
        selected_files = selected_files[: args.max_files]

    records_by_group: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    files_by_group: dict[tuple[str, str], list[Path]] = defaultdict(list)
    processed_files: set[Path] = set()
    skipped_files: set[Path] = set()
    warnings_by_group: dict[tuple[str, str], list[str]] = defaultdict(list)
    extraction_by_group: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)

    workers = max(1, int(args.workers or 1))
    parse_results: list[tuple[tuple[str, str], Path, list[dict[str, Any]], dict[str, Any]] | None] = [
        None
        for _ in selected_files
    ]
    if workers > 1 and len(selected_files) > 1:
        print(f"Parsing {len(selected_files)} product-doc Markdown files with {workers} workers...", flush=True)
        payloads = [
            (index, input_root, md_file, args.switch_name, args.version)
            for index, md_file in enumerate(selected_files)
        ]
        started_at = time.monotonic()
        completed = 0
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(_parse_product_doc_worker, payload) for payload in payloads]
            for future in as_completed(futures):
                index, group, md_file, parsed_records, file_info = future.result()
                parse_results[index] = (group, md_file, parsed_records, file_info)
                completed += 1
                if completed == len(selected_files) or completed % 10 == 0:
                    elapsed = max(time.monotonic() - started_at, 0.001)
                    files_per_minute = completed / elapsed * 60
                    remaining = len(selected_files) - completed
                    eta_minutes = remaining / files_per_minute if files_per_minute else 0
                    print(
                        f"Parsed files: {completed}/{len(selected_files)} "
                        f"({files_per_minute:.1f} files/min, ETA {eta_minutes:.1f} min)",
                        flush=True,
                    )
    else:
        print(f"Parsing {len(selected_files)} product-doc Markdown files with 1 worker...", flush=True)
        started_at = time.monotonic()
        for index, md_file in enumerate(selected_files):
            _, group, parsed_file, parsed_records, file_info = _parse_product_doc_worker(
                (index, input_root, md_file, args.switch_name, args.version)
            )
            parse_results[index] = (group, parsed_file, parsed_records, file_info)
            completed = index + 1
            if completed == len(selected_files) or completed % 10 == 0:
                elapsed = max(time.monotonic() - started_at, 0.001)
                files_per_minute = completed / elapsed * 60
                remaining = len(selected_files) - completed
                eta_minutes = remaining / files_per_minute if files_per_minute else 0
                print(
                    f"Parsed files: {completed}/{len(selected_files)} "
                    f"({files_per_minute:.1f} files/min, ETA {eta_minutes:.1f} min)",
                    flush=True,
                )

    for result in parse_results:
        if result is None:
            continue
        group, md_file, parsed_records, file_info = result
        files_by_group[group].append(md_file)
        processed_files.add(md_file)
        if not parsed_records:
            skipped_files.add(md_file)
        records_by_group[group].extend(parsed_records)
        extraction_by_group[group].update(file_info.get("counters", {}))
        warnings_by_group[group].extend(file_info.get("warnings", []))

    all_records: list[dict[str, Any]] = []
    for group in sorted(records_by_group):
        all_records.extend(records_by_group[group])

    generated_rows = generate_qa_rows(all_records, ground=args.ground_questions_with_version)
    cleanup_by_group = _clean_generated_rows(generated_rows)
    (
        valid_rows,
        validation_drops,
        validation_drops_by_group,
        generated_count_by_group,
    ) = _validate_rows_by_group(
        generated_rows,
        require_grounding=args.ground_questions_with_version,
    )

    deduped_rows, duplicates_removed, duplicate_by_group = _dedupe_rows_by_group(
        valid_rows,
        enabled=args.dedupe_global,
    )

    (
        question_deduped_rows,
        duplicate_questions_found,
        duplicate_question_rows_dropped,
        duplicate_questions_found_by_group,
        duplicate_question_dropped_by_group,
    ) = _dedupe_rows_by_question(
        deduped_rows,
        enabled=args.dedupe_global,
    )

    capped_rows, rows_removed_by_cap, cap_drops, cap_removed_by_group = _cap_rows_by_group(
        question_deduped_rows,
        enabled=args.cap_generic_sections,
        caps=family_caps,
    )
    event_capped_rows, event_cap_stats, event_cap_by_group = _cap_event_log_rows_by_ratio(
        capped_rows,
        enabled=args.cap_generic_sections,
    )
    if event_cap_stats["event_log_rows_dropped_by_cap"]:
        rows_removed_by_cap += event_cap_stats["event_log_rows_dropped_by_cap"]
        cap_drops["event_log_ratio"] += event_cap_stats["event_log_rows_dropped_by_cap"]
        for group, counters in event_cap_by_group.items():
            cap_removed_by_group[group] += counters["event_log_rows_dropped_by_cap"]
    capped_rows = event_capped_rows

    pre_trim_rows = list(capped_rows)
    capped_rows, max_rows_removed = _trim_max_rows(capped_rows, args.max_rows)
    if max_rows_removed:
        rows_removed_by_cap += max_rows_removed
        cap_drops["max_rows"] += max_rows_removed
        for row in pre_trim_rows[args.max_rows :]:
            cap_removed_by_group[_group_key(row)] += 1

    rows_by_group: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    valid_before_dedup_by_group: Counter[tuple[str, str]] = Counter()

    for row in valid_rows:
        valid_before_dedup_by_group[_group_key(row)] += 1
    for row in capped_rows:
        rows_by_group[_group_key(row)].append(row)

    _write_jsonl(capped_rows, final_jsonl)
    repair_validation_report = _build_product_doc_repair_validation_report(capped_rows)
    repair_validation_report_path = final_jsonl.parent / "product_doc_preprocessing_validation_report.json"
    debug_sample_path = final_jsonl.parent / "debug_product_doc_repaired_samples.jsonl"
    _write_json(repair_validation_report, repair_validation_report_path)
    _write_jsonl(_sample_rows_by_kind(capped_rows), debug_sample_path)

    quality_reports: dict[str, Any] = {}
    for group in sorted(files_by_group):
        switch, version = group
        group_dir = output_root / switch / version
        group_records = records_by_group.get(group, [])
        group_rows = rows_by_group.get(group, [])
        structured_path = group_dir / "structured_records.json"
        train_path = group_dir / "train_chat.jsonl"
        quality_path = group_dir / "quality_report.json"
        _write_json(group_records, structured_path)
        _write_jsonl(group_rows, train_path)

        report = _build_quality_report(
            group_key=group,
            group_files=files_by_group[group],
            processed_files=processed_files,
            skipped_files=skipped_files,
            records=group_records,
            generated_rows_count=generated_count_by_group[group],
            valid_rows_before_dedup_count=valid_before_dedup_by_group[group],
            final_rows=group_rows,
            duplicates_removed=duplicate_by_group[group],
            duplicate_questions_found=duplicate_questions_found_by_group[group],
            duplicate_question_rows_dropped=duplicate_question_dropped_by_group[group],
            validation_drops=validation_drops_by_group[group],
            rows_removed_by_cap=cap_removed_by_group[group],
            extraction_counters=extraction_by_group[group],
            cleanup_counters=cleanup_by_group[group],
            event_cap_counters=event_cap_by_group[group],
            warnings=warnings_by_group[group],
        )
        report["output_paths"] = {
            "structured_records": str(structured_path),
            "train_chat": str(train_path),
            "quality_report": str(quality_path),
            "final_jsonl": str(final_jsonl),
        }
        _write_json(report, quality_path)
        quality_reports[f"{switch}/{version}"] = report

    summary = {
        "input_files_discovered": len(all_files),
        "input_files_selected": len(selected_files),
        "workers": workers,
        "groups_processed": len(files_by_group),
        "structured_records": len(all_records),
        "qa_rows_generated": len(generated_rows),
        "qa_rows_valid_before_dedup": len(valid_rows),
        "qa_rows_final": len(capped_rows),
        "duplicates_removed": duplicates_removed,
        "duplicate_questions_found": duplicate_questions_found,
        "duplicate_question_rows_dropped": duplicate_question_rows_dropped,
        "duplicate_questions_final": _duplicate_questions_final(capped_rows),
        "rows_removed_by_validation": sum(validation_drops.values()),
        "validation_drop_reasons": _counter_json(validation_drops),
        "rows_removed_by_cap": rows_removed_by_cap,
        "cap_drop_reasons": _counter_json(cap_drops),
        "event_log_rows_before_cap": event_cap_stats["event_log_rows_before_cap"],
        "event_log_rows_after_cap": event_cap_stats["event_log_rows_after_cap"],
        "event_log_rows_dropped_by_cap": event_cap_stats["event_log_rows_dropped_by_cap"],
        "rows_with_switch_version_grounding": rows_with_grounding(capped_rows),
        "rows_with_underscore_version_in_question": _rows_with_underscore_version(capped_rows),
        "output_root": str(output_root),
        "final_jsonl": str(final_jsonl),
        "product_doc_preprocessing_entry_point": str(Path(__file__).resolve()),
        "product_doc_repaired_rows": repair_validation_report["syntax_question_rows"]
        + repair_validation_report["command_description_rows"]
        + repair_validation_report["show_command_rows"]
        + repair_validation_report["event_question_rows"],
        "counts_by_data_family": repair_validation_report["counts_by_data_family"],
        "validation_report": str(repair_validation_report_path),
        "debug_sample_file": str(debug_sample_path),
        "validation_warnings": repair_validation_report["warnings"],
        "quality_reports": {
            key: value.get("output_paths", {}).get("quality_report", "")
            for key, value in quality_reports.items()
        },
        "source_type_map_entries": len(PRODUCT_DOC_FILE_MAP),
    }
    return summary


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Deterministically preprocess Aruba AOS-CX product documentation Markdown."
    )
    parser.add_argument("--input-root", type=_path, required=True)
    parser.add_argument("--output-root", type=_path, required=True)
    parser.add_argument("--final-jsonl", type=_path, default=DEFAULT_FINAL_JSONL)
    parser.add_argument("--write-intermediate", action="store_true", help="Accepted for parity; intermediates are always written.")
    parser.add_argument("--switch-name", default="", help="Filter/override switch family, for example 8360.")
    parser.add_argument("--version", default="", help="Filter/override AOS-CX version, for example 10_10.")
    parser.add_argument("--max-files", type=int, default=None)
    parser.add_argument("--max-rows", type=int, default=None)
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel parser workers for Markdown files.")
    parser.add_argument("--ground_questions_with_version", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--dedupe_global", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--cap_generic_sections", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument(
        "--enable-output-interpretation",
        action="store_true",
        default=False,
        help="Reserved for a future show_command_output_interpretation dataset; disabled by default.",
    )
    parser.add_argument(
        "--family-cap",
        action="append",
        default=None,
        help="Override a data-family cap as data_family=limit. May be repeated.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    summary = run(args)
    print("Product documentation preprocessing complete.")
    print("Files changed for this product-doc repair:")
    print("- project/src/product_doc_qa_generator.py")
    print("- project/src/product_doc_validator.py")
    print("- preprocess_product_docs.py")
    print("- repair_product_doc_answer_formats.py")
    print(f"Product documentation preprocessing entry point: {summary['product_doc_preprocessing_entry_point']}")
    print(f"Input files selected: {summary['input_files_selected']}")
    print(f"Workers: {summary['workers']}")
    print(f"Groups processed: {summary['groups_processed']}")
    print(f"Structured records: {summary['structured_records']}")
    print(f"Q&A rows generated: {summary['qa_rows_generated']}")
    print(f"Product documentation rows repaired/standardized: {summary['product_doc_repaired_rows']}")
    print(f"Counts by data_family: {json.dumps(summary['counts_by_data_family'], sort_keys=True)}")
    print(f"Validation warnings: {summary['validation_warnings']}")
    print(f"Final Q&A rows: {summary['qa_rows_final']}")
    print(f"Final JSONL: {summary['final_jsonl']}")
    print(f"Validation report: {summary['validation_report']}")
    print(f"Debug sample file: {summary['debug_sample_file']}")
    print(f"Output root: {summary['output_root']}")
    if summary["rows_removed_by_validation"]:
        print(f"Rows removed by validation: {summary['rows_removed_by_validation']}")
    if summary["rows_removed_by_cap"]:
        print(f"Rows removed by cap: {summary['rows_removed_by_cap']}")


if __name__ == "__main__":
    main(sys.argv[1:])
