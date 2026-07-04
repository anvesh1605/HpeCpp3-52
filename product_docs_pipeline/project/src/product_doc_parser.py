"""Deterministic parser for Aruba AOS-CX product documentation Markdown.

This module is intentionally separate from the release-note parser. Product
documentation teaches product behavior, commands, procedures, and references;
release notes teach bug/change information.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PRODUCT_DOC_FILE_MAP = {
    "cli": "product_cli_reference",
    "command-line": "product_cli_reference",
    "command_line": "product_cli_reference",
    "fundamentals": "product_fundamentals",
    "ip_services": "product_ip_services",
    "ip service": "product_ip_services",
    "ip_route": "product_ip_routing",
    "ip routing": "product_ip_routing",
    "l2_bridging": "product_l2_bridging",
    "layer-2": "product_l2_bridging",
    "link_aggregation": "product_link_aggregation",
    "link aggregation": "product_link_aggregation",
    "security": "product_security",
    "acls": "product_acls_classifier",
    "classifier": "product_acls_classifier",
    "qos": "product_qos",
    "quality of service": "product_qos",
    "copp": "product_copp",
    "diagnostics": "product_diagnostics_supportability",
    "supportability": "product_diagnostics_supportability",
    "monitoring": "product_monitoring",
    "elmrg": "product_event_log_reference",
    "event log": "product_event_log_reference",
    "snmp_mib": "product_snmp_mib_reference",
    "snmp mib": "product_snmp_mib_reference",
    "multicast": "product_multicast",
    "hardening": "product_hardening",
    "vsf": "product_vsf",
    "vxlan": "product_vxlan",
    "vsx": "product_vsx",
    "mpls": "product_mpls",
    "high_availability": "product_high_availability",
    "high availability": "product_high_availability",
    "rest_v1": "product_rest_api",
    "rest_v10": "product_rest_api",
    "rest": "product_rest_api",
    "web_ui": "product_web_ui",
    "web ui": "product_web_ui",
    "nae": "product_nae",
    "network analytics engine": "product_nae",
    "job_scheduler": "product_job_scheduler",
    "job scheduler": "product_job_scheduler",
}

DATA_FAMILIES = {
    "concept_explanation",
    "configuration_procedure",
    "cli_command_reference",
    "show_command_reference",
    "command_parameter_reference",
    "command_example",
    "feature_limitation",
    "troubleshooting",
    "web_ui_task",
    "rest_api_reference",
    "snmp_mib_reference",
    "event_log_reference",
    "security_policy",
    "qos_policy",
    "routing_feature",
    "monitoring_feature",
}

HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
VERSION_RE = re.compile(r"^10[_\.]\d{2}(?:[_\.]\d{4})?$", re.IGNORECASE)
SWITCH_TOKEN_RE = re.compile(r"\b(?:4100i|5420|6000|6100|6200|6300|6400|8100|83xx|8320|8325|8360|8400|9300|10000|10040)\b", re.IGNORECASE)
HTTP_ENDPOINT_RE = re.compile(r"\b(GET|POST|PUT|PATCH|DELETE)\s+((?:/rest|/system)/[^\s`|)]+)", re.IGNORECASE)
OID_RE = re.compile(r"\b(?:\d+\.){3,}\d+\b")
EVENT_ID_RE = re.compile(r"\b(?:event\s*)?(?:id|event-id|event id)\s*[:=]?\s*([A-Za-z0-9_.:-]{3,})\b", re.IGNORECASE)
COMMAND_HEADING_RE = re.compile(
    r"^(?:show|clear|configure|config|copy|boot|checkpoint|erase|diag|ping|traceroute|"
    r"ls|pwd|rm|rmdir|reboot|secure-mode|"
    r"interface|vlan|vrf|router|ip|ipv6|aaa|access-list|snmp-server|logging|ntp|"
    r"radius|tacacs|crypto|ssh|https-server|rest|vsx|vlan|qos|class|policy|apply|"
    r"feature|bfd|erps|neighbor|redundancy|hsc|no)\b",
    re.IGNORECASE,
)
PROCEDURE_HEADING_RE = re.compile(
    r"^(?:configuring|configure|enabling|enable|disabling|disable|creating|create|adding|add|"
    r"removing|remove|deleting|delete|verifying|verify|viewing|view|troubleshooting|"
    r"replacing|installing|uploading|downloading|accessing|logging\s+in)\b",
    re.IGNORECASE,
)
BAD_PROCEDURE_HEADING_RE = re.compile(
    r"\b(?:Overview|Command|Command Information|Command History|Configuration concepts|"
    r"Example|Examples|Figure|Table|Image|Panel|Restrictions|Limitations)\b",
    re.IGNORECASE,
)
LIMITATION_HEADING_RE = re.compile(
    r"\b(?:limitations?|restrictions?|guidelines?|considerations?|notes?|cautions?|warnings?|important)\b",
    re.IGNORECASE,
)
CONCEPT_HEADING_RE = re.compile(
    r"\b(?:overview|about|behavior|guidelines|restrictions|notes|limitations|concept|operation|"
    r"considerations|introduction|description|support|requirements)\b",
    re.IGNORECASE,
)
TROUBLESHOOTING_RE = re.compile(r"\b(?:troubleshoot|troubleshooting|error|fault|diagnostic|debug)\b", re.IGNORECASE)
CODE_FENCE_RE = re.compile(r"```[\s\S]*?```")
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:/<>-]*")
CLI_PROMPT_RE = re.compile(r"\bswitch(?:\([^)]*\))?[>#]\s*(?:\|\s*)?", re.IGNORECASE)
ORDERED_STEP_RE = re.compile(r"^\s*(?:\d+[\.)]|Step\s+\d+[:.)-]?)\s+(.+)$", re.IGNORECASE)
NOTE_RE = re.compile(r"^\s*(?:>\s*)?(Note|Warning|Caution|Important)\s*[:.-]\s*(.+)$", re.IGNORECASE)
LABEL_RE = re.compile(
    r"^\s*(Syntax|Description|Commands?\s*contexts?|Parameters?|Authority|Usage|Examples?|"
    r"Request|Response|Method|URI|Resource|Severity|Recommended action)\s*:?\s*$",
    re.IGNORECASE,
)
INLINE_LABEL_RE = re.compile(
    r"^\s*(Syntax|Description|Commands?\s*contexts?|Parameters?|Authority|Usage|Examples?|"
    r"Request|Response|Method|URI|Resource|Severity|Recommended action)\s*:\s+(.+)$",
    re.IGNORECASE,
)
PAGE_HEADER_FOOTER_RE = re.compile(
    r"^\s*(?:"
    r"AOS-CX\s*[\d.]+\s*.*?Guide\s*\|\s*User\s*Guide(?:\s+\d+)?|"
    r"[A-Za-z][A-Za-z ]{1,80}\s*\|\s*\d+|"
    r"[A-Za-z]{2,}\|\d+|"
    r"Contents\s*\|\s*\d+|"
    r"About this Document\s*\|\s*\d+"
    r")\s*$",
    re.IGNORECASE,
)

BOILERPLATE_PHRASES = (
    "Legal Disclaimer",
    "Copyright",
    "Notices",
    "Warranty",
    "HPE links",
    "Table of contents",
    "Contents",
    "Related documents",
    "Recently viewed",
    "Follow HPE",
    "Company",
    "Careers",
    "How to buy",
    "Product return and recycling",
    "Privacy",
    "Terms of use",
    "Cookie Preferences",
)

BOILERPLATE_LINE_RE = re.compile(
    r"^(?:"
    + "|".join(re.escape(phrase) for phrase in BOILERPLATE_PHRASES)
    + r")\b",
    re.IGNORECASE,
)

GENERIC_TABLE_SECTION_TITLES = {
    "command to change it",
    "syntax",
    "parameter",
    "parameters",
    "description",
    "command context",
    "command_context",
    "usage",
    "authority",
    "default",
    "value",
    "values",
    "example",
    "examples",
}

INTRO_FRONT_MATTER_TITLES = {
    "about this document",
    "about the examples",
    "applicable products",
    "command syntax notation conventions",
    "conventions",
    "document conventions",
    "identifying switch ports and interfaces",
    "latest version available online",
    "support and other resources",
    "switch prompts",
    "understanding the cli prompts",
    "variable information in cli prompts",
}

SUPPORT_FOOTER_SECTION_PATTERNS = [
    r"^Accessing Aruba Support$",
    r"^Accessing HPE Aruba Networking Support$",
    r"^Accessing Updates$",
    r"^Feature Packs$",
    r"^Other useful sites$",
    r"^Documentation feedback$",
    r"^Support and Other Resources$",
    r"^HPE Aruba Networking Support Services$",
    r"^Aruba Support Portal$",
    r"^HPE My Networking$",
    r"^End-of-Life information$",
    r"^Warranty information$",
    r"^Regulatory information$",
]
SUPPORT_FOOTER_SECTION_RES = tuple(re.compile(pattern, re.IGNORECASE) for pattern in SUPPORT_FOOTER_SECTION_PATTERNS)

BAD_VISUAL_SECTION_PATTERNS = [
    r"^Figure\s+\d+",
    r"^Table\s+\d+",
    r"^Image\s+\d*",
    r"^Panel\s+\d*",
    r".*\bpanel\b.*",
]
BAD_VISUAL_SECTION_RES = tuple(re.compile(pattern, re.IGNORECASE) for pattern in BAD_VISUAL_SECTION_PATTERNS)

OCR_ACRONYMS = (
    "AOS-CX",
    "BFD",
    "BGP",
    "CLI",
    "DHCP",
    "DNS",
    "HTTP",
    "HTTPS",
    "IP",
    "IPv4",
    "IPv6",
    "JSON",
    "LAG",
    "MAC",
    "MIB",
    "OSPF",
    "REST",
    "SNMP",
    "SSH",
    "STP",
    "UDP",
    "URL",
    "VLAN",
    "VRF",
    "VSF",
    "VSX",
    "VXLAN",
)

OCR_MERGED_REPLACEMENTS = (
    (r"\bAboutthis\b", "About this"),
    (r"\bAccessControl\b", "Access Control"),
    (r"\bAdda\b", "Add a"),
    (r"\bAddan\b", "Add an"),
    (r"\bAddthe\b", "Add the"),
    (r"\bApplythe\b", "Apply the"),
    (r"\bBegin\bdefining", "Begin defining"),
    (r"\bBegindefining\b", "Begin defining"),
    (r"\bCommandLine\b", "Command Line"),
    (r"\bCommandcontext\b", "Command context"),
    (r"\bCommandto\b", "Command to"),
    (r"\bConfigurethe\b", "Configure the"),
    (r"\bClearsstatisticsforallBFDsessionsorforaspecificBFDsession\b", "Clears statistics for all BFD sessions or for a specific BFD session"),
    (r"\bCreatea\b", "Create a"),
    (r"\bCreatean\b", "Create an"),
    (r"\bDefinea\b", "Define a"),
    (r"\bDefinean\b", "Define an"),
    (r"\bDisablesBFDforOSPFv2onthecurrentinterface\b", "Disables BFD for OSPFv2 on the current interface"),
    (r"\bDisablesBFDontheswitch\b", "Disables BFD on the switch"),
    (r"\bEnablesBFDonallOSPFv2orOSPFv3interfaces\b", "Enables BFD on all OSPFv2 or OSPFv3 interfaces"),
    (r"\bEnablesBFDforOSPFv2onthecurrentinterface\b", "Enables BFD for OSPFv2 on the current interface"),
    (r"\bEnablesordisablesBFDonthespecifiedstaticroute\b", "Enables or disables BFD on the specified static route"),
    (r"\bEnablesordisablesBFDforHSCfeature\b", "Enables or disables BFD for HSC feature"),
    (r"\bEnterthe\b", "Enter the"),
    (r"\bExitthe\b", "Exit the"),
    (r"\bFormost\b", "For most"),
    (r"\bfastpeeringsession\b", "fast peering session"),
    (r"\bformofthiscommandsetsthe\b", "form of this command sets the"),
    (r"\bformofthiscommanddisables\b", "form of this command disables"),
    (r"\bformofthiscommandsets\b", "form of this command sets"),
    (r"\bfromBFD\b", "from BFD"),
    (r"\bHighAvailability\b", "High Availability"),
    (r"\bIdentifyingSwitch\b", "Identifying Switch"),
    (r"\binterfacelevel\b", "interface level"),
    (r"\bManagementModule\b", "Management Module"),
    (r"\bonall\b", "on all"),
    (r"\bShowyour\b", "Show your"),
    (r"\bSetsthe\b", "Sets the"),
    (r"\bSpecifiesa\b", "Specifies a"),
    (r"\bSpecifiesan\b", "Specifies an"),
    (r"\bSpecifiesthe\b", "Specifies the"),
    (r"\bThisoverridestheglobalsettingsdefinedwiththe\b", "This overrides the global settings defined with the"),
    (r"\bThenoform", "The no form"),
    (r"\bThiscommand\b", "This command"),
    (r"\bToview\b", "To view"),
    (r"\baddressfor\b", "address for"),
    (r"\ballowsaccess\b", "allows access"),
    (r"\batboththe\b", "at both the"),
    (r"\batthe\b", "at the"),
    (r"\bbfdandipv6\b", "bfd and ipv6"),
    (r"\bcommandsip\b", "commands ip"),
    (r"\bandipv6\b", "and ipv6"),
    (r"\bechopackets\b", "echo packets"),
    (r"\bechosessions\b", "echo sessions"),
    (r"\benabledatthe\b", "enabled at the"),
    (r"\benablesordisables\b", "enables or disables"),
    (r"\binterfaces,excluding\b", "interfaces, excluding"),
    (r"\bIPV4\b", "IPv4"),
    (r"\bIPV6\b", "IPv6"),
    (r"\bIPv([46])or\b", r"IPv\1 or"),
    (r"\bmultiplieronaninterface\b", "multiplier on an interface"),
    (r"\bmultiplieronaninterface\b", "multiplier on an interface"),
    (r"\bmultipliertothedefaultvalueof\b", "multiplier to the default value of"),
    (r"\bPIMIP\s*v([46])\b", r"PIM IPv\1"),
    (r"\bofthiscommand\b", "of this command"),
    (r"\bontheswitch\b", "on the switch"),
    (r"\bPIMIP\b", "PIM IP"),
    (r"\bretainsallconfigurationsettings\b", "retains all configuration settings"),
    (r"\bswitch,butretainsallconfigurationsettings\b", "switch, but retains all configuration settings"),
    (r"\bthoseonwhich\b", "those on which"),
    (r"\bthoseonwhichBFDwasenabledattheinterfacelevelwiththecommandsip\b", "those on which BFD was enabled at the interface level with the commands ip"),
    (r"\bOSPFv2orOSPFv3\b", "OSPFv2 or OSPFv3"),
    (r"\bOSPFv2/OSPFv3orPIMIPv4/IPv6\b", "OSPFv2/OSPFv3 or PIM IPv4/IPv6"),
    (r"\bwiththe\b", "with the"),
    (r"\bfromthe\b", "from the"),
    (r"\btothe\b", "to the"),
    (r"\binthe\b", "in the"),
    (r"\bonthe\b", "on the"),
    (r"\bofthe\b", "of the"),
    (r"\bandthe\b", "and the"),
    (r"\bforthe\b", "for the"),
    (r"\bifthat\b", "if that"),
    (r"\bifthe\b", "if the"),
    (r"\bsothat\b", "so that"),
    (r"\bthatthe\b", "that the"),
    (r"\bwhenthe\b", "when the"),
    (r"\bwillbe\b", "will be"),
    (r"\bmustbe\b", "must be"),
    (r"\bcanbe\b", "can be"),
    (r"\bdoesnot\b", "does not"),
    (r"\bdonot\b", "do not"),
    (r"\bcommandbfd\b", "command bfd"),
    (r"\bcommandscontext\b", "Command context"),
    (r"\bcommandneighbor\b", "command neighbor"),
    (r"\bcommandsaddress-familyandneighbor\b", "commands address-family and neighbor"),
    (r"\bdefaultvalues\b", "default values"),
    (r"\bdetectionmultiplieronaninterface\b", "detection multiplier on an interface"),
    (r"\bdetectionmultipliertothedefaultvalueof", "detection multiplier to the default value of "),
    (r"\bdetectionmultiplier\b", "detection multiplier"),
    (r"\bfeaturesdonot\b", "features do not"),
    (r"\bforHSCfeature\b", "for HSC feature"),
    (r"\bneedtobechanged\b", "need to be changed"),
    (r"\bnetworkoperating\b", "network operating"),
    (r"\bpackets\.Thisaddress\b", "packets. This address"),
    (r"\btopeering\b", "to peering"),
    (r"\btoreceive\b", "to receive"),
    (r"\busedinallecho\b", "used in all echo"),
    (r"\bv([23])interfaces\b", r"v\1 interfaces"),
    (r"\bv([23])or\b", r"v\1 or"),
    (r"\bv([23])orPIM", r"v\1 or PIM"),
    (r"\bwasenabled\b", "was enabled"),
    (r"\bwasenabledattheinterfacelevelwiththecommandsip\b", "was enabled at the interface level with the commands ip"),
    (r"\bwiththecommandsip\b", "with the commands ip"),
    (r"\bStaticRoute\b", "Static Route"),
)


@dataclass(frozen=True)
class MarkdownSection:
    title: str
    level: int
    hierarchy: tuple[str, ...]
    content: str
    line_number: int


def normalize_text(text: str) -> str:
    text = (text or "").replace("\xa0", " ")
    text = text.replace("\u2010", "-").replace("\u2011", "-")
    text = text.replace("\u2012", "-").replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    text = cleanup_ocr_spacing(text)
    return re.sub(r"\s+", " ", text).strip()


def cleanup_ocr_spacing(text: str) -> str:
    """Conservatively separate common words merged by PDF/OCR extraction.

    This intentionally uses targeted networking/documentation terms rather than
    a probabilistic word segmenter, so CLI symbols, URLs, versions, and command
    syntax stay intact.
    """

    if not text:
        return ""
    for _ in range(2):
        for pattern, replacement in OCR_MERGED_REPLACEMENTS:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    for acronym in sorted(OCR_ACRONYMS, key=len, reverse=True):
        escaped = re.escape(acronym)
        text = re.sub(rf"(?<=[a-z0-9])({escaped})(?=[A-Za-z])", r" \1", text)
        text = re.sub(rf"({escaped})(?=[a-z])", r"\1 ", text)
    text = re.sub(r"(?<=[a-z])(?=[A-Z][a-z])", " ", text)
    text = re.sub(r"\b([A-Z][a-z]+)(a|an|the)(?=[A-Z])", r"\1 \2 ", text)
    text = re.sub(r"(?<=[a-z0-9])\.(?=[A-Z])", ". ", text)
    text = re.sub(r"\bIP v([46])\b", r"IPv\1", text)
    text = re.sub(r"\bOSPF v([23])\b", r"OSPFv\1", text)
    text = text.replace("Open v Switch", "Open vSwitch")
    return text


def clean_inline_markdown(text: str) -> str:
    text = text or ""
    text = re.sub(r"!\[[^\]]*]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)]\(([^)]+)\)", r"\1 (\2)", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = text.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ")
    return normalize_text(text.strip(" \t|#"))


def _slugish(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", normalize_text(text).lower()).strip("_")


def discover_markdown_files(input_root: Path, max_files: int | None = None) -> list[Path]:
    if not input_root.exists():
        raise FileNotFoundError(f"Input root does not exist: {input_root}")
    files = sorted(
        path
        for path in input_root.rglob("*.md")
        if path.is_file()
        and ".venv" not in path.parts
        and ".markitdown_venv" not in path.parts
        and ".markitdown_venv312" not in path.parts
        and "_logs" not in path.parts
    )
    return files[:max_files] if max_files else files


def path_metadata(input_root: Path, file_path: Path, switch_override: str = "", version_override: str = "") -> dict[str, str]:
    try:
        relative = file_path.relative_to(input_root)
    except ValueError:
        relative = file_path
    parts = relative.parts

    switch = switch_override.strip()
    version = version_override.strip()
    if not switch and len(parts) >= 3:
        switch = parts[0]
    if not version and len(parts) >= 3 and VERSION_RE.match(parts[1]):
        version = parts[1].replace(".", "_")
    if not switch:
        switch = "unknown_from_product_doc"
    if not version:
        version = "unknown_version"
    return {"switch": switch, "version": version, "relative_source_file": relative.as_posix()}


def extract_document_title(markdown_text: str, file_path: Path) -> str:
    fallback = normalize_text(file_path.stem.replace("_", " ").replace("-", " ")).title()
    for line_number, raw_line in enumerate(markdown_text.splitlines(), start=1):
        line = raw_line.strip()
        match = HEADING_RE.match(line)
        if match:
            title = clean_inline_markdown(match.group(2))
            if (
                title
                and not _is_boilerplate_title(title)
                and line_number <= 120
                and len(title) > 8
                and not COMMAND_HEADING_RE.match(title)
            ):
                return title
            return fallback
    return fallback


def classify_product_doc(file_path: Path, document_title: str) -> str:
    haystack = f"{file_path.stem} {document_title}".replace("-", " ").replace("_", " ").lower()
    stem_key = file_path.stem.lower()
    for key, source_type in sorted(PRODUCT_DOC_FILE_MAP.items(), key=lambda item: len(item[0]), reverse=True):
        key_normalized = key.replace("_", " ").lower()
        if key in stem_key or key_normalized in haystack:
            return source_type
    return "product_documentation"


def infer_supported_switch_series(file_path: Path, document_title: str, folder_switch: str) -> list[str]:
    text = f"{file_path.stem} {document_title}"
    series = []
    for match in SWITCH_TOKEN_RE.finditer(text):
        token = match.group(0)
        if token.lower() not in {item.lower() for item in series}:
            series.append(token)
    if folder_switch and folder_switch != "unknown_from_product_doc":
        if folder_switch.lower() not in {item.lower() for item in series}:
            series.insert(0, folder_switch)
    return series


def remove_boilerplate(markdown_text: str) -> str:
    cleaned: list[str] = []
    skip_section_level: int | None = None
    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        heading = HEADING_RE.match(line.strip())
        if heading:
            title = clean_inline_markdown(heading.group(2))
            level = len(heading.group(1))
            if _is_boilerplate_title(title):
                skip_section_level = level
                continue
            if skip_section_level is not None and level <= skip_section_level:
                skip_section_level = None
        if skip_section_level is not None:
            continue
        stripped = clean_inline_markdown(line).strip(" -*")
        if _is_boilerplate_line(stripped):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def _is_boilerplate_line(line: str) -> bool:
    if not line:
        return False
    if BOILERPLATE_LINE_RE.search(line):
        return True
    lowered = line.lower()
    if lowered in {"home", "support", "products", "solutions", "services", "contact us"}:
        return True
    if "www.hpe.com" in lowered and len(line.split()) <= 8:
        return True
    return False


def _is_boilerplate_title(title: str) -> bool:
    normalized = normalize_text(title).strip(":- ")
    if not normalized:
        return False
    if is_support_footer_title(normalized):
        return True
    lowered = normalized.lower()
    exact = {
        "contents",
        "table of contents",
        "legal disclaimer",
        "notices",
        "warranty",
        "support",
        "related documents",
        "recently viewed",
    }
    if lowered in exact:
        return True
    return any(lowered.startswith(phrase.lower()) for phrase in BOILERPLATE_PHRASES)


def is_support_footer_title(title: str) -> bool:
    normalized = normalize_text(title).strip(":- ")
    if not normalized:
        return False
    return any(pattern.match(normalized) for pattern in SUPPORT_FOOTER_SECTION_RES)


def is_visual_caption_title(title: str) -> bool:
    normalized = normalize_text(title).strip(":- ")
    if not normalized:
        return False
    return any(pattern.match(normalized) for pattern in BAD_VISUAL_SECTION_RES)


def is_page_header_footer_line(line: str) -> bool:
    cleaned = normalize_text((line or "").strip(" |"))
    if not cleaned:
        return False
    return bool(PAGE_HEADER_FOOTER_RE.match(cleaned))


def count_page_header_footer_fragments(text: str) -> int:
    return sum(1 for line in (text or "").splitlines() if is_page_header_footer_line(line))


def is_chapter_marker(title: str) -> bool:
    return bool(re.fullmatch(r"Chapter\s+\d+", normalize_text(title), flags=re.IGNORECASE))


def normalize_chapter_sections(sections: list[MarkdownSection]) -> list[MarkdownSection]:
    normalized_sections: list[MarkdownSection] = []
    for section in sections:
        if not is_chapter_marker(section.title):
            normalized_sections.append(section)
            continue
        replacement = _section_from_chapter_marker(section)
        if replacement:
            normalized_sections.append(replacement)
    return normalized_sections


def _section_from_chapter_marker(section: MarkdownSection) -> MarkdownSection | None:
    lines = section.content.splitlines()
    for index, raw_line in enumerate(lines):
        candidate = clean_inline_markdown(raw_line)
        if not _is_real_heading_after_chapter(candidate):
            continue
        remaining = lines[index + 1 :]
        while remaining and not clean_inline_markdown(remaining[0]):
            remaining = remaining[1:]
        if remaining and clean_inline_markdown(remaining[0]).lower() == candidate.lower():
            remaining = remaining[1:]
        return MarkdownSection(
            title=candidate,
            level=section.level,
            hierarchy=(candidate,),
            content="\n".join(remaining).strip(),
            line_number=section.line_number + index + 1,
        )
    return None


def _is_real_heading_after_chapter(text: str) -> bool:
    cleaned = normalize_text(text).strip()
    if not cleaned:
        return False
    lowered = cleaned.lower()
    if lowered in GENERIC_TABLE_SECTION_TITLES or lowered in INTRO_FRONT_MATTER_TITLES:
        return False
    if is_chapter_marker(cleaned) or _is_boilerplate_title(cleaned) or is_page_header_footer_line(cleaned):
        return False
    if cleaned.endswith((".", ",", ";", ":")) or word_count(cleaned) > 10:
        return False
    return True


def split_markdown_sections(markdown_text: str) -> list[MarkdownSection]:
    sections: list[MarkdownSection] = []
    hierarchy: dict[int, str] = {}
    current_title = "Document"
    current_level = 1
    current_line = 1
    current_content: list[str] = []

    def flush() -> None:
        content = "\n".join(current_content).strip()
        if not content and current_title == "Document":
            return
        titles = tuple(hierarchy[index] for index in sorted(hierarchy) if index <= current_level)
        section_hierarchy = titles or (current_title,)
        sections.append(
            MarkdownSection(
                title=current_title,
                level=current_level,
                hierarchy=section_hierarchy,
                content=content,
                line_number=current_line,
            )
        )

    for line_number, raw_line in enumerate(markdown_text.splitlines(), start=1):
        match = HEADING_RE.match(raw_line.strip())
        if match:
            flush()
            level = len(match.group(1))
            title = clean_inline_markdown(match.group(2))
            current_title = title or "Untitled"
            current_level = level
            current_line = line_number
            current_content = []
            hierarchy[level] = current_title
            for existing_level in list(hierarchy):
                if existing_level > level:
                    del hierarchy[existing_level]
            continue
        current_content.append(raw_line)
    flush()
    sections = [section for section in sections if section.content.strip() or section.title != "Document"]
    if len(sections) <= 1 and word_count(markdown_text) > 300:
        fallback_sections = split_plain_heading_sections(markdown_text)
        if len(fallback_sections) > len(sections):
            return fallback_sections
    return sections


def split_plain_heading_sections(markdown_text: str) -> list[MarkdownSection]:
    sections: list[MarkdownSection] = []
    current_title = "Document"
    current_line = 1
    current_content: list[str] = []

    def flush() -> None:
        content = "\n".join(current_content).strip()
        if not content and current_title == "Document":
            return
        sections.append(
            MarkdownSection(
                title=current_title,
                level=2,
                hierarchy=(current_title,),
                content=content,
                line_number=current_line,
            )
        )

    lines = markdown_text.splitlines()
    for index, raw_line in enumerate(lines):
        line = raw_line.rstrip()
        previous_blank = index == 0 or not lines[index - 1].strip()
        next_blank = index + 1 >= len(lines) or not lines[index + 1].strip()
        if _is_plain_heading_candidate(line, previous_blank=previous_blank, next_blank=next_blank):
            flush()
            current_title = clean_inline_markdown(line)
            current_line = index + 1
            current_content = []
            continue
        current_content.append(line)
    flush()
    return sections


def _is_plain_heading_candidate(line: str, previous_blank: bool, next_blank: bool) -> bool:
    cleaned = clean_inline_markdown(line)
    if not cleaned or _is_boilerplate_title(cleaned):
        return False
    lowered = cleaned.lower()
    if is_support_footer_title(cleaned) or is_visual_caption_title(cleaned):
        return False
    if lowered in GENERIC_TABLE_SECTION_TITLES or lowered in INTRO_FRONT_MATTER_TITLES:
        return False
    if is_page_header_footer_line(cleaned):
        return False
    if line.lstrip().startswith("|") or "|" in cleaned or "http://" in cleaned.lower() or "https://" in cleaned.lower():
        return False
    if len(cleaned) > 110 or cleaned.endswith((".", ",", ";", ":")):
        return False
    if re.match(r"^Chapter\s+\d+\b", cleaned, re.IGNORECASE):
        return True
    if re.match(r"^(?:Appendix|Part)\s+[A-Za-z0-9]+\b", cleaned, re.IGNORECASE):
        return True
    heading_keyword = re.search(
        r"\b(?:Overview|Features?|Configuration|Configuring|Commands?|Guidelines?|Restrictions?|"
        r"Examples?|Troubleshooting|Reference|Behavior|Failover|Management|Module|VSX|VLAN|"
        r"Interface|Routing|Security|Policy)\b",
        cleaned,
    )
    if not (previous_blank or next_blank):
        return False
    if word_count(cleaned) > 10:
        return False
    if COMMAND_HEADING_RE.match(cleaned) and not heading_keyword:
        return False
    if heading_keyword:
        return True
    return False


def parse_labeled_blocks(content: str) -> dict[str, str]:
    blocks: dict[str, list[str]] = {}
    active_label = ""
    for raw_line in content.splitlines():
        line = raw_line.rstrip()
        inline_match = INLINE_LABEL_RE.match(line)
        if inline_match:
            active_label = _canonical_label(inline_match.group(1))
            blocks.setdefault(active_label, []).append(inline_match.group(2).strip())
            continue
        label_match = LABEL_RE.match(line)
        if label_match:
            active_label = _canonical_label(label_match.group(1))
            blocks.setdefault(active_label, [])
            continue
        if active_label:
            blocks.setdefault(active_label, []).append(line)
    return {label: "\n".join(lines).strip() for label, lines in blocks.items() if "\n".join(lines).strip()}


def _canonical_label(label: str) -> str:
    cleaned = normalize_text(label).lower()
    if cleaned.startswith("parameter"):
        return "parameters"
    if cleaned.startswith("example"):
        return "examples"
    if cleaned.startswith("command") or cleaned.startswith("commands"):
        return "command_context"
    return cleaned.replace(" ", "_")


def is_command_section(section: MarkdownSection, source_type: str) -> bool:
    title = clean_inline_markdown(section.title)
    content = section.content
    blocks = parse_labeled_blocks(content)
    has_command_labels = bool({"syntax", "description", "command_context", "parameters", "authority", "usage", "examples"} & set(blocks))
    if "syntax" in blocks and "description" in blocks:
        return True
    if source_type == "product_cli_reference" and has_command_labels:
        return True
    if COMMAND_HEADING_RE.match(title) and ("syntax" in blocks or "description" in blocks or "parameters" in blocks):
        return True
    return False


def is_procedure_section(section: MarkdownSection) -> bool:
    title = clean_inline_markdown(section.title)
    lowered_title = title.lower()
    if lowered_title in GENERIC_TABLE_SECTION_TITLES:
        return False
    if is_support_footer_title(title) or is_visual_caption_title(title):
        return False
    if BAD_PROCEDURE_HEADING_RE.search(title):
        return False
    if section.title == "Document" and word_count(section.content) > 1000:
        return False
    return bool(PROCEDURE_HEADING_RE.match(title))


def is_limitation_section(section: MarkdownSection) -> bool:
    title = " ".join(section.hierarchy)
    return bool(LIMITATION_HEADING_RE.search(title))


def is_front_matter_section(section: MarkdownSection) -> bool:
    title = clean_inline_markdown(section.title).lower().strip()
    if is_support_footer_title(title):
        return True
    if title in INTRO_FRONT_MATTER_TITLES:
        return True
    lowered = section.content.lower()
    legal_hits = sum(
        phrase in lowered
        for phrase in (
            "open source code",
            "copyright",
            "legal disclaimer",
            "warranty",
            "hewlett packard enterprise shall not be liable",
            "confidential computer software",
        )
    )
    if legal_hits >= 2:
        return True
    intro_hits = sum(
        phrase in lowered
        for phrase in (
            "about this document",
            "applicable products",
            "latest version available online",
            "command syntax notation conventions",
            "about the examples",
            "identifying switch ports and interfaces",
            "understanding the cli prompts",
        )
    )
    if title.startswith("chapter 1") and intro_hits >= 2:
        return True
    if "identifying switch ports and interfaces" in lowered:
        return True
    if "understanding the cli prompts" in lowered and "about the examples" in lowered:
        return True
    return section.line_number <= 40 and (
        title.startswith("part number")
        or "open source code" in lowered
        or "hewlett packard enterprise company" in lowered
    )


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text or ""))


def strip_table_markup(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if is_page_header_footer_line(stripped):
            continue
        if re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?", stripped):
            continue
        if stripped.startswith("|") and "|" in stripped[1:]:
            cells = [
                clean_inline_markdown(cell)
                for cell in stripped.strip("|").split("|")
                if clean_inline_markdown(cell) and not re.fullmatch(r":?-{3,}:?", clean_inline_markdown(cell))
            ]
            if len(cells) == 1:
                lines.append(cells[0])
                continue
        lines.append(line)
    return "\n".join(lines).strip()


def compact_section_text(text: str, max_chars: int = 1600) -> str:
    text = strip_table_markup(text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = clean_inline_markdown(text)
    if len(text) <= max_chars:
        return text
    cutoff = text.rfind(". ", 0, max_chars)
    if cutoff < 240:
        cutoff = max_chars
    return text[: cutoff + 1].strip()


def extract_command_records_from_section(base: dict[str, Any], section: MarkdownSection) -> tuple[list[dict[str, Any]], Counter[str]]:
    counters: Counter[str] = Counter()
    candidates = _command_block_candidates(section)
    if not candidates:
        record = extract_command_record(base, section)
        return ([record] if record else []), counters

    lines = section.content.splitlines()
    records: list[dict[str, Any]] = []
    if len(candidates) > 1 or candidates[0][0] > 0:
        counters["command_boundary_merges_detected"] += max(1, len(candidates) - 1)
    for position, (start_index, command) in enumerate(candidates):
        end_index = candidates[position + 1][0] if position + 1 < len(candidates) else len(lines)
        block_text = "\n".join(lines[start_index + 1 : end_index]).strip()
        synthetic_section = MarkdownSection(
            title=command,
            level=section.level,
            hierarchy=tuple(list(section.hierarchy[:-1]) + [command]) if section.hierarchy else (command,),
            content=block_text,
            line_number=section.line_number + start_index + 1,
        )
        record = extract_command_record(base, synthetic_section)
        if record:
            records.append(record)
    return records, counters


def _command_block_candidates(section: MarkdownSection) -> list[tuple[int, str]]:
    lines = section.content.splitlines()
    candidates: list[tuple[int, str]] = []
    for index, raw_line in enumerate(lines):
        command = _command_candidate_from_line(raw_line)
        if not command:
            continue
        if not _has_syntax_label_after(lines, index, max_scan=10):
            continue
        if candidates and candidates[-1][1].lower() == command.lower():
            continue
        candidates.append((index, command))
    return candidates


def _has_syntax_label_after(lines: list[str], index: int, max_scan: int) -> bool:
    for raw_line in lines[index + 1 : min(len(lines), index + max_scan + 1)]:
        cleaned = clean_inline_markdown(raw_line).strip(":")
        if not cleaned:
            continue
        if cleaned.lower() == "syntax":
            return True
        if LABEL_RE.match(cleaned) and cleaned.lower() != "syntax":
            return False
    return False


def _command_candidate_from_line(raw_line: str) -> str:
    stripped = (raw_line or "").strip()
    if not stripped or is_page_header_footer_line(stripped):
        return ""
    if "|" in stripped:
        candidate = _table_command_candidate(stripped)
    else:
        candidate = clean_inline_markdown(stripped)
    candidate = _clean_command_candidate(candidate)
    if not _looks_like_command_candidate_text(candidate):
        return ""
    return candidate


def _table_command_candidate(line: str) -> str:
    cells = [clean_inline_markdown(cell) for cell in line.strip("|").split("|")]
    meaningful = [cell for cell in cells if cell and not re.fullmatch(r":?-{3,}:?", cell)]
    if not meaningful:
        return ""
    if meaningful[0].lower().startswith("switch("):
        return ""
    context_index = next((index for index, cell in enumerate(meaningful) if "context:" in cell.lower()), None)
    if context_index is not None:
        meaningful = meaningful[:context_index]
    return " ".join(meaningful)


def _clean_command_candidate(text: str) -> str:
    cleaned = normalize_text(text)
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r"\s+\|\s+", " ", cleaned)
    cleaned = re.sub(r"\s*\(Context:.*$", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip(" :;,.")
    return cleaned


def _looks_like_command_candidate_text(text: str) -> bool:
    if not text or len(text) > 180:
        return False
    lowered = text.lower()
    if lowered in GENERIC_TABLE_SECTION_TITLES or lowered in INTRO_FRONT_MATTER_TITLES:
        return False
    if LABEL_RE.match(text) or INLINE_LABEL_RE.match(text):
        return False
    if _is_boilerplate_title(text) or is_page_header_footer_line(text):
        return False
    if text.endswith((".", ":", ",")):
        return False
    if word_count(text) > 18:
        return False
    if re.search(r"\b(is|are|was|were|displays|defines|specifies|selects|provides|contains)\b", text, re.IGNORECASE):
        return False
    return bool(COMMAND_HEADING_RE.match(text))


def clean_command_syntax(syntax: str) -> str:
    cleaned = clean_inline_markdown(syntax)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = CLI_PROMPT_RE.sub("", cleaned)
    cleaned = re.sub(r"^\|\s*", "", cleaned)
    cleaned = re.sub(r"\s+\|\s*$", "", cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned


def _syntax_prompt_fragment_count(text: str) -> int:
    return len(CLI_PROMPT_RE.findall(str(text or "")))


def extract_command_record(base: dict[str, Any], section: MarkdownSection) -> dict[str, Any] | None:
    blocks = parse_labeled_blocks(section.content)
    raw_syntax = _first_nonempty_line(blocks.get("syntax", ""))
    syntax = clean_command_syntax(raw_syntax)
    command = _command_from_title_or_syntax(section.title, syntax)
    if not command:
        return None
    section_title = section.title
    if clean_inline_markdown(section.title).lower() in GENERIC_TABLE_SECTION_TITLES:
        section_title = command
    description = compact_section_text(blocks.get("description", ""), max_chars=800)
    parameters = _extract_parameters(blocks.get("parameters", ""))
    examples = _extract_examples(blocks.get("examples", "") or section.content)
    data_family = "show_command_reference" if command.lower().startswith("show ") else "cli_command_reference"
    return {
        **base,
        "data_family": data_family,
        "section": section_title,
        "section_hierarchy": [section_title] if section_title != section.title else list(section.hierarchy),
        "line_number": section.line_number,
        "command": command,
        "syntax": syntax,
        "_syntax_prompt_fragments_removed": _syntax_prompt_fragment_count(raw_syntax),
        "description": description,
        "parameters": parameters,
        "usage": compact_section_text(blocks.get("usage", ""), max_chars=800),
        "examples": examples,
        "authority": compact_section_text(blocks.get("authority", ""), max_chars=400),
        "command_context": compact_section_text(blocks.get("command_context", ""), max_chars=400),
    }


def extract_plain_command_records(base: dict[str, Any], markdown_text: str) -> list[dict[str, Any]]:
    """Extract CLI command blocks from PDFs whose headings were not converted.

    Many command-reference PDFs contain plain text command headings followed by
    "Description", "Parameter", "Usage", and "Examples" labels. This fallback
    avoids treating a whole CLI book as one giant section.
    """

    lines = markdown_text.splitlines()
    candidates: list[tuple[int, list[str]]] = []
    for index, raw_line in enumerate(lines):
        line = clean_inline_markdown(raw_line)
        if not _looks_like_plain_command_start(line):
            continue
        syntax_lines = _syntax_lines_after(lines, index, max_scan=28)
        if not _syntax_belongs_to_command(line, syntax_lines):
            continue
        if not _has_label_after(lines, index, "description", max_scan=40):
            continue
        candidates.append((index, syntax_lines))

    records: list[dict[str, Any]] = []
    seen_commands: set[str] = set()
    for start_position, (start, syntax_lines) in enumerate(candidates):
        end = candidates[start_position + 1][0] if start_position + 1 < len(candidates) else min(len(lines), start + 180)
        block_text = "\n".join(lines[start:end]).strip()
        title = clean_inline_markdown(lines[start])
        synthetic_section = MarkdownSection(
            title=title,
            level=2,
            hierarchy=(title,),
            content=block_text,
            line_number=start + 1,
        )
        record = extract_command_record(base, synthetic_section)
        if not record:
            continue
        if not record.get("syntax"):
            record["syntax"] = "; ".join(syntax_lines)
        command_key = normalize_text(str(record.get("command", ""))).lower()
        if not command_key or command_key in seen_commands:
            continue
        seen_commands.add(command_key)
        records.append(record)
    return records


def _looks_like_plain_command_start(line: str) -> bool:
    if not line or len(line) > 180:
        return False
    if "|" in line or line.endswith(".") or line.endswith(":"):
        return False
    if word_count(line) > 18:
        return False
    if re.search(r"\b(is|are|was|were|displays|defines|specifies|selects)\b", line, re.IGNORECASE):
        return False
    return bool(COMMAND_HEADING_RE.match(line))


def _syntax_lines_after(lines: list[str], index: int, max_scan: int) -> list[str]:
    syntax_lines: list[str] = []
    for raw_line in lines[index + 1 : min(len(lines), index + max_scan + 1)]:
        cleaned = clean_inline_markdown(raw_line)
        lowered = cleaned.lower().strip(":")
        if not cleaned:
            if syntax_lines:
                continue
            continue
        if lowered == "description" or lowered.startswith("description "):
            break
        if LABEL_RE.match(cleaned):
            break
        if cleaned.startswith("|") or "|" in cleaned:
            continue
        if re.match(r"^(?:AOS-CX|Chapter|Command History|Command Information|Platforms)\b", cleaned, re.IGNORECASE):
            continue
        if len(cleaned) > 220:
            continue
        syntax_lines.append(cleaned)
        if len(syntax_lines) >= 4:
            break
    return syntax_lines


def _syntax_belongs_to_command(command: str, syntax_lines: list[str]) -> bool:
    if not syntax_lines:
        return False
    command_norm = normalize_text(command).lower()
    command_tokens = command_norm.split()
    if not command_tokens:
        return False
    first_token = command_tokens[0]
    for syntax in syntax_lines:
        syntax_norm = normalize_text(syntax).lower()
        if syntax_norm == command_norm:
            return True
        if syntax_norm.startswith(f"{command_norm} "):
            return True
        if syntax_norm.startswith(f"no {command_norm}"):
            return True
        if len(command_tokens) == 1 and syntax_norm.startswith(f"{first_token} "):
            return True
    return False


def _has_label_after(lines: list[str], index: int, label: str, max_scan: int) -> bool:
    wanted = label.lower()
    for raw_line in lines[index + 1 : min(len(lines), index + max_scan + 1)]:
        line = clean_inline_markdown(raw_line).strip(":").lower()
        if line == wanted:
            return True
        if wanted == "description" and line.startswith("description "):
            return True
    return False


def _command_from_title_or_syntax(title: str, syntax: str) -> str:
    clean_title = clean_inline_markdown(title).strip()
    if COMMAND_HEADING_RE.match(clean_title):
        return clean_title
    if syntax:
        line = clean_inline_markdown(syntax)
        line = re.sub(r"\s+", " ", line)
        return line[:180].strip()
    return ""


def _first_nonempty_line(text: str) -> str:
    for line in (text or "").splitlines():
        cleaned = clean_inline_markdown(line)
        if cleaned:
            return cleaned
    return ""


def _first_paragraph(text: str, exclude_labels: bool = False) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        if is_page_header_footer_line(line):
            continue
        if exclude_labels and (LABEL_RE.match(line) or INLINE_LABEL_RE.match(line)):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if not line.strip():
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if line.strip().startswith("|"):
            continue
        current.append(line.strip())
    if current:
        paragraphs.append(" ".join(current))
    for paragraph in paragraphs:
        cleaned = clean_inline_markdown(paragraph)
        if word_count(cleaned) >= 6:
            return cleaned[:900].strip()
    return ""


def _extract_parameters(text: str) -> list[str]:
    parameters: list[str] = []
    for raw_line in text.splitlines():
        line = clean_inline_markdown(raw_line).strip(" -*|")
        if not line:
            continue
        if re.fullmatch(r":?-{3,}:?", line):
            continue
        if line.lower() in {"parameter", "description", "parameters"}:
            continue
        if len(line) > 320:
            line = line[:320].rstrip()
        if line not in parameters:
            parameters.append(line)
    return parameters[:30]


def _extract_examples(text: str) -> list[str]:
    examples: list[str] = []
    for match in CODE_FENCE_RE.finditer(text):
        value = match.group(0).strip()
        if value and value not in examples:
            examples.append(value)
    if examples:
        return examples[:5]

    capture = False
    current: list[str] = []
    for line in text.splitlines():
        if re.match(r"^\s*Examples?\s*:?\s*$", line, re.IGNORECASE):
            capture = True
            continue
        if capture and LABEL_RE.match(line):
            break
        if capture:
            current.append(line.rstrip())
    example_text = "\n".join(current).strip()
    if example_text:
        examples.append(example_text[:1600].strip())
    return examples[:5]


def extract_procedure_record(base: dict[str, Any], section: MarkdownSection) -> dict[str, Any] | None:
    steps: list[str] = []
    commands: list[str] = []
    notes: list[str] = []
    in_fence = False
    fence_lines: list[str] = []
    for raw_line in section.content.splitlines():
        if is_page_header_footer_line(raw_line):
            continue
        line = raw_line.rstrip()
        if line.strip().startswith("```"):
            in_fence = not in_fence
            if not in_fence and fence_lines:
                command_block = "\n".join(fence_lines).strip()
                if command_block:
                    commands.append(command_block)
                fence_lines = []
            continue
        if in_fence:
            fence_lines.append(line)
            continue
        step_match = ORDERED_STEP_RE.match(line)
        if step_match:
            step = clean_inline_markdown(step_match.group(1))
            if step and not _is_bad_procedure_step(step):
                steps.append(step)
            elif len(steps) >= 2:
                break
            continue
        note_match = NOTE_RE.match(line)
        if note_match:
            notes.append(f"{note_match.group(1)}: {clean_inline_markdown(note_match.group(2))}")
            continue
        cleaned = clean_inline_markdown(line)
        if COMMAND_HEADING_RE.match(cleaned) and len(cleaned.split()) <= 14:
            commands.append(cleaned)
    steps = [step for step in steps if not _is_bad_procedure_step(step)]
    if len(steps) < 2:
        return None
    family = "troubleshooting" if TROUBLESHOOTING_RE.search(section.title) else "configuration_procedure"
    if base.get("source_type") == "product_web_ui":
        family = "web_ui_task"
    return {
        **base,
        "data_family": family,
        "section": section.title,
        "section_hierarchy": list(section.hierarchy),
        "line_number": section.line_number,
        "task": clean_inline_markdown(section.title),
        "procedure": steps[:30],
        "commands": commands[:20],
        "notes": notes[:20],
    }


def _is_bad_procedure_step(step: str) -> bool:
    cleaned = normalize_text(step).strip(" .;:")
    if not cleaned:
        return True
    lowered = cleaned.lower()
    if lowered in {"if", "then", "or", "and", "command to change it", "description", "parameter", "parameters"}:
        return True
    if is_page_header_footer_line(cleaned):
        return True
    if "commandtochange" in lowered.replace(" ", "") or "default value" in lowered:
        return True
    if re.search(r"\b(?:if|then|or|and|to|with|from|for|when|where|that|the|a|an|of)$", lowered):
        return True
    if cleaned.endswith((" If", " If.", " if", " if.")):
        return True
    if word_count(cleaned) < 3 and not COMMAND_HEADING_RE.match(cleaned):
        return True
    words = cleaned.split()
    if len(words) == 1 and len(cleaned) > 28:
        return True
    return False


def extract_rest_records(base: dict[str, Any], section: MarkdownSection) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for method, endpoint in HTTP_ENDPOINT_RE.findall(section.content):
        description = _first_paragraph(section.content) or compact_section_text(section.content, max_chars=700)
        records.append(
            {
                **base,
                "data_family": "rest_api_reference",
                "section": section.title,
                "section_hierarchy": list(section.hierarchy),
                "line_number": section.line_number,
                "method": method.upper(),
                "endpoint": endpoint,
                "description": description,
            }
        )
    return _dedupe_records(records, ("method", "endpoint", "section"))


def extract_snmp_records(base: dict[str, Any], section: MarkdownSection) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    text = section.content
    if not (OID_RE.search(text) or re.search(r"\bMIB\b", text, re.IGNORECASE)):
        return records
    for line in text.splitlines():
        cleaned = clean_inline_markdown(line).strip(" |")
        if not cleaned:
            continue
        oid_match = OID_RE.search(cleaned)
        mib_like = re.search(r"\b[A-Za-z][A-Za-z0-9-]*(?:MIB|OBJECT|OID)[A-Za-z0-9-]*\b", cleaned)
        if not oid_match and not mib_like:
            continue
        records.append(
            {
                **base,
                "data_family": "snmp_mib_reference",
                "section": section.title,
                "section_hierarchy": list(section.hierarchy),
                "line_number": section.line_number,
                "object_name": mib_like.group(0) if mib_like else "",
                "oid": oid_match.group(0) if oid_match else "",
                "description": cleaned[:900],
            }
        )
    return _dedupe_records(records[:40], ("object_name", "oid", "description"))


def extract_event_records(base: dict[str, Any], section: MarkdownSection) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    text = section.content
    if not (EVENT_ID_RE.search(text) or re.search(r"\bseverity\b", text, re.IGNORECASE)):
        return records
    blocks = parse_labeled_blocks(text)
    for line in text.splitlines():
        cleaned = clean_inline_markdown(line)
        event_match = EVENT_ID_RE.search(cleaned)
        if not event_match:
            continue
        records.append(
            {
                **base,
                "data_family": "event_log_reference",
                "section": section.title,
                "section_hierarchy": list(section.hierarchy),
                "line_number": section.line_number,
                "event_id": event_match.group(1),
                "severity": compact_section_text(blocks.get("severity", ""), max_chars=200),
                "description": cleaned[:900],
                "recommended_action": compact_section_text(blocks.get("recommended_action", ""), max_chars=700),
            }
        )
    return _dedupe_records(records[:40], ("event_id", "description"))


def extract_concept_record(base: dict[str, Any], section: MarkdownSection) -> dict[str, Any] | None:
    title = clean_inline_markdown(section.title)
    lowered_title = title.lower()
    overview_renamed = False
    if lowered_title == "overview":
        parent_title = _overview_parent_title(section)
        if not parent_title:
            return None
        title = f"{parent_title} Overview"
        lowered_title = title.lower()
        overview_renamed = True
    if (
        lowered_title in GENERIC_TABLE_SECTION_TITLES
        or lowered_title in INTRO_FRONT_MATTER_TITLES
        or is_support_footer_title(title)
        or is_visual_caption_title(title)
        or is_chapter_marker(title)
        or _is_boilerplate_title(title)
    ):
        return None
    description = compact_section_text(section.content, max_chars=1400)
    if word_count(description) < 40:
        return None
    family = infer_concept_family(base.get("source_type", ""), section)
    if not family:
        return None
    return {
        **base,
        "data_family": family,
        "section": section.title,
        "section_hierarchy": list(section.hierarchy),
        "line_number": section.line_number,
        "topic": title,
        "description": description,
        "_generic_overview_renamed": int(overview_renamed),
    }


def _overview_parent_title(section: MarkdownSection) -> str:
    for candidate in reversed(section.hierarchy[:-1]):
        cleaned = clean_inline_markdown(candidate)
        lowered = cleaned.lower()
        if not cleaned or lowered == "overview":
            continue
        if lowered in GENERIC_TABLE_SECTION_TITLES or lowered in INTRO_FRONT_MATTER_TITLES:
            continue
        if is_support_footer_title(cleaned) or is_visual_caption_title(cleaned):
            continue
        if is_chapter_marker(cleaned) or _is_boilerplate_title(cleaned):
            continue
        return cleaned
    return ""


def infer_concept_family(source_type: str, section: MarkdownSection) -> str:
    title_context = " ".join(section.hierarchy)
    if is_limitation_section(section):
        return "feature_limitation"
    if TROUBLESHOOTING_RE.search(title_context):
        return "troubleshooting"
    if source_type == "product_security":
        return "security_policy"
    if source_type == "product_qos":
        return "qos_policy"
    if source_type == "product_ip_routing":
        return "routing_feature"
    if source_type == "product_monitoring":
        return "monitoring_feature"
    if source_type == "product_web_ui" and PROCEDURE_HEADING_RE.match(clean_inline_markdown(section.title)):
        return "web_ui_task"
    if CONCEPT_HEADING_RE.search(title_context) or source_type != "product_documentation":
        return "concept_explanation"
    return ""


def _dedupe_records(records: list[dict[str, Any]], fields: tuple[str, ...]) -> list[dict[str, Any]]:
    seen = set()
    kept = []
    for record in records:
        key = tuple(normalize_text(str(record.get(field, ""))).lower() for field in fields)
        if key in seen:
            continue
        seen.add(key)
        kept.append(record)
    return kept


def _consume_internal_record_counters(record: dict[str, Any], counters: Counter[str]) -> None:
    counters["syntax_prompt_fragments_removed"] += int(record.pop("_syntax_prompt_fragments_removed", 0) or 0)
    counters["generic_overview_rows_renamed"] += int(record.pop("_generic_overview_renamed", 0) or 0)


def parse_product_doc_file(
    input_root: Path,
    file_path: Path,
    switch_override: str = "",
    version_override: str = "",
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    raw_text = file_path.read_text(encoding="utf-8", errors="replace")
    document_title = extract_document_title(raw_text, file_path)
    source_type = classify_product_doc(file_path, document_title)
    meta = path_metadata(input_root, file_path, switch_override=switch_override, version_override=version_override)
    cleaned_text = remove_boilerplate(raw_text)
    sections = split_markdown_sections(cleaned_text)

    base = {
        "source_type": source_type,
        "switch": meta["switch"],
        "version": meta["version"],
        "document_title": document_title,
        "source_file": meta["relative_source_file"],
        "supported_switch_series": infer_supported_switch_series(file_path, document_title, meta["switch"]),
    }

    records: list[dict[str, Any]] = []
    counters: Counter[str] = Counter()
    warnings: list[str] = []
    commands_seen: set[str] = set()
    counters["page_header_footer_fragments_removed"] += count_page_header_footer_fragments(raw_text)
    counters["chapter_heading_rows_dropped"] += sum(1 for section in sections if is_chapter_marker(section.title))
    sections = normalize_chapter_sections(sections)

    if source_type == "product_cli_reference":
        plain_command_records = extract_plain_command_records(base, cleaned_text)
        for record in plain_command_records:
            _consume_internal_record_counters(record, counters)
            records.append(record)
            commands_seen.add(normalize_text(str(record.get("command", ""))).lower())
            if word_count(str(record.get("description", ""))) >= 3:
                counters["command_records_with_clean_description"] += 1
            else:
                counters["command_records_missing_description"] += 1
            if record.get("parameters"):
                counters["parameter_rows_dropped_as_noisy"] += 1
        counters["commands_extracted"] += len(plain_command_records)
        counters["examples_extracted"] += sum(len(record.get("examples", [])) for record in plain_command_records)

    for section in sections:
        section_title = clean_inline_markdown(section.title)
        if is_support_footer_title(section_title):
            counters["support_footer_rows_dropped"] += 1
            continue
        if is_visual_caption_title(section_title):
            counters["visual_caption_rows_dropped"] += 1
            continue
        if _is_boilerplate_title(section.title):
            continue
        if is_front_matter_section(section):
            continue
        if section.title == "Document" and source_type == "product_cli_reference" and commands_seen:
            continue
        if is_command_section(section, source_type):
            command_records, command_counters = extract_command_records_from_section(base, section)
            counters.update(command_counters)
            kept_command = False
            for record in command_records:
                command_key = normalize_text(str(record.get("command", ""))).lower()
                if command_key in commands_seen:
                    continue
                _consume_internal_record_counters(record, counters)
                commands_seen.add(command_key)
                records.append(record)
                counters["commands_extracted"] += 1
                if word_count(str(record.get("description", ""))) >= 3:
                    counters["command_records_with_clean_description"] += 1
                else:
                    counters["command_records_missing_description"] += 1
                if record.get("parameters"):
                    counters["parameter_rows_dropped_as_noisy"] += 1
                if record.get("examples"):
                    counters["examples_extracted"] += len(record.get("examples", []))
                kept_command = True
            if kept_command:
                continue
        if source_type == "product_rest_api":
            rest_records = extract_rest_records(base, section)
            records.extend(rest_records)
            counters["rest_endpoints_extracted"] += len(rest_records)
            if rest_records:
                continue
        if source_type == "product_snmp_mib_reference":
            snmp_records = extract_snmp_records(base, section)
            records.extend(snmp_records)
            counters["snmp_objects_extracted"] += len(snmp_records)
            if snmp_records:
                continue
        if source_type == "product_event_log_reference":
            event_records = extract_event_records(base, section)
            records.extend(event_records)
            counters["event_logs_extracted"] += len(event_records)
            if event_records:
                continue
        if is_procedure_section(section):
            record = extract_procedure_record(base, section)
            if record:
                _consume_internal_record_counters(record, counters)
                records.append(record)
                counters["procedures_extracted"] += 1
                continue
            counters["incomplete_procedure_rows_dropped"] += 1
            continue
        if section_title.lower() == "overview" and not _overview_parent_title(section):
            counters["generic_overview_rows_dropped"] += 1
            continue
        record = extract_concept_record(base, section)
        if record:
            _consume_internal_record_counters(record, counters)
            records.append(record)
            if record["data_family"] == "feature_limitation":
                counters["limitations_extracted"] += 1
            else:
                counters["concepts_extracted"] += 1

    if not records:
        warnings.append(f"No product documentation records extracted from {file_path}")

    file_info = {
        **base,
        "sections_seen": len(sections),
        "records_extracted": len(records),
        "warnings": warnings,
        "counters": dict(counters),
    }
    return records, file_info
