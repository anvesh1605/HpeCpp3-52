"""Validation, deduplication, and capping for product documentation QA rows."""

from __future__ import annotations

import re
from collections import Counter
from typing import Any


PRODUCT_DOC_DATA_FAMILY_CAPS = {
    "concept_explanation": 12000,
    "configuration_procedure": 10000,
    "cli_command_reference": 12000,
    "show_command_reference": 5000,
    "command_parameter_reference": 5000,
    "command_example": 5000,
    "feature_limitation": 5000,
    "troubleshooting": 4000,
    "web_ui_task": 3000,
    "rest_api_reference": 3000,
    "snmp_mib_reference": 3000,
    "event_log_reference": 3000,
    "security_policy": 5000,
    "qos_policy": 4000,
    "routing_feature": 5000,
    "monitoring_feature": 4000,
}

WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:/<>-]*")
GROUNDING_RE = re.compile(r"^For\s+.+?\s+AOS-CX\s+10[_\.]\d{2}(?:[_\.]\d{4})?,\s+", re.IGNORECASE)
UNDERSCORE_VERSION_RE = re.compile(r"\bAOS-CX\s+10_\d{2}(?:_\d{4})?\b", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(
    r"\b(?:TBD|To be determined)\b|<description from the table>|<real description>",
    re.IGNORECASE,
)
INVISIBLE_IMAGE_RE = re.compile(
    r"\b(?:shown below|figure below|as shown in the image|see the following figure)\b",
    re.IGNORECASE,
)
FOOTER_NAV_RE = re.compile(
    r"\b(?:Legal Disclaimer|Copyright|Notices|Warranty|Recently viewed|Follow HPE|"
    r"Company|Careers|How to buy|Product return and recycling|Table of contents|"
    r"Related documents)\b",
    re.IGNORECASE,
)
SUPPORT_FOOTER_SECTION_RE = re.compile(
    r"^(?:Accessing Aruba Support|Accessing HPE Aruba Networking Support|Accessing Updates|"
    r"Feature Packs|Other useful sites|Documentation feedback|Support and Other Resources|"
    r"HPE Aruba Networking Support Services|Aruba Support Portal|HPE My Networking|"
    r"End-of-Life information|Warranty information|Regulatory information)$",
    re.IGNORECASE,
)
SUPPORT_FOOTER_TEXT_RE = re.compile(
    r"\b(?:Accessing Aruba Support|Accessing HPE Aruba Networking Support|Accessing Updates|"
    r"Feature Packs|Other useful sites|Documentation feedback|Support and Other Resources|"
    r"HPE Aruba Networking Support Services|Aruba Support Portal|HPE My Networking|"
    r"End-of-Life information|Warranty information|Regulatory information|support\.hpe\.com|"
    r"asp\.arubanetworks\.com|arubanetworks\.com/support-services|HPE Support Center|"
    r"Support Portal|warranty|end-of-life|phone number|support services|"
    r"Applicable products|Latest version available online|Product publications|"
    r"Command syntax notation conventions|About this document)\b|https?://\S+",
    re.IGNORECASE,
)
BAD_VISUAL_SECTION_RE = re.compile(
    r"^(?:Figure\s+\d+|Table\s+\d+|Image\s*\d*|Panel\s*\d*|.*\bpanel\b.*)",
    re.IGNORECASE,
)
VISUAL_CAPTION_ANSWER_RE = re.compile(r"\b(?:Figure|Table)\s+\d+\s*[\.:]", re.IGNORECASE)
DOCUMENT_TITLE_RE = re.compile(
    r"^(?:AOS-CX\s+\d+\.\d+.*Guide|AOS-CX\s+\d+\.\d+.*\|.*Switch Series.*|"
    r".*Switch Series\).*|.*Guide\s*\|.*)$",
    re.IGNORECASE,
)
DOCUMENT_TITLE_QUESTION_RE = re.compile(r"\bwhat does the guide say about AOS-CX\s+\d+\.\d+.*Guide\b", re.IGNORECASE)
CHAPTER_SECTION_RE = re.compile(r"^Chapter\s+\d+(?:\s+.*)?$|^Chapter\s+\d+.*\.+\s*\d+$", re.IGNORECASE)
COMMAND_METADATA_SECTION_RE = re.compile(
    r"^(?:Command History|Command Information|Commands context|Command context|Example command|"
    r"Examples?|Modification|Platforms?|Authority|Parameters?|Usage)$",
    re.IGNORECASE,
)
GENERIC_METADATA_SECTION_RE = re.compile(
    r"^(?:Command\s+or\b|procedure\s+Example\b|Configuration concepts\b|"
    r"Configuration prerequisites\b|Commands?\b|Command context\b|Authority\b|"
    r"Platforms\b|Parameters?\b|Usage\b|Modification\b|Release\b|Examples?\b)",
    re.IGNORECASE,
)
EXAMPLE_SECTION_RE = re.compile(r"^Examples?(?:\s*:|\s+of\b|\s+using\b|\b)", re.IGNORECASE)
EXAMPLE_LIKE_SECTION_RE = re.compile(
    r"(?:\bconfiguration example\b|,\s*for example\b|\bcommand,\s*for example\b|"
    r"^Examples?\s*:|^Examples?\s+of\b|^Examples?\s+using\b|^Example command\b|"
    r"^Example success message\b|^Example HTML source\b)",
    re.IGNORECASE,
)
PARAMETER_DESCRIPTION_TOPIC_RE = re.compile(
    r"^(?:Specifies\s+the|Selects\s+the|Shows\s+the|Indicates\s+the|"
    r"Syntax\s*:|Range\s*:|Default\s*:|Parameter\b|Description\b)",
    re.IGNORECASE,
)
WEB_UI_FAKE_CLI_COMMAND_RE = re.compile(
    r"^(?:VSX|Analytics|Overview|Interfaces|VLANs|System|Diagnostics)$",
    re.IGNORECASE,
)
SYNTAX_QUESTION_RE = re.compile(r"\bwhat\s+is\s+the\s+syntax\s+of\b", re.IGNORECASE)
EVENT_ID_QUESTION_RE = re.compile(
    r"\bevent\s+log\s+information\s+is\s+documented\s+for\s+([A-Za-z0-9_.:-]+)",
    re.IGNORECASE,
)
BAD_ERPS_EXPANSION_RE = re.compile(
    r"\b(?:Egress Rate Profile|Error Rate Profile|Error Reporting Per Second|Extended Route Processing)\b",
    re.IGNORECASE,
)
FAKE_COMMAND_HEADING_RE = re.compile(r"^[A-Za-z0-9 /+_.()-]+ Commands?$", re.IGNORECASE)
PAGE_HEADER_RE = re.compile(
    r"AOS-CX\s+\d+\.\d+.*?Guide\s*\|.*?Switch Series\)?\s*\d*|"
    r"AOS-CX\s+\d+\.\d+.*?Guide\s*\|.*|"
    r"\|\s*\([^)]+Switch Series\)\s*\d+",
    re.IGNORECASE,
)
HARDENING_CLEAN_TOPICS = {
    "user management and password control",
    "authentication, authorization, and accounting",
    "authentication, authorization and accounting",
    "remote authentication",
    "source interface for aaa servers",
    "per-user management interface enablement",
    "authorization",
    "accounting",
    "two-factor authentication and authorization",
    "session management",
    "securing snmp access",
    "hardening the control plane",
    "rest interface restrictions",
}
HARDENING_NOISY_HEADING_RE = re.compile(
    r"^(?:"
    r"(?:[\u2022\u25e6?*o]|â—¦)\s+.*|"
    r"\*+\s*[^*]+\s*\*+|"
    r"Objective|Module|Script|Configuration|Show Commands|Source Interface|"
    r"Supported Management I|"
    r"Aruba-User-Mgmt-Interface\s*=.*|"
    r"Software,\s*Documentation,\s*Security Advisories and Bug Bounty Program"
    r")$",
    re.IGNORECASE,
)
HARDENING_PAGE_HEADING_RE = re.compile(r"^(?P<title>[A-Z][A-Za-z0-9,() /+&-]{8,90})\s+\d{1,3}$")
PDF_PAGE_HEADER_FRAGMENT_RE = re.compile(
    r"\b(?:Public\s+)?[A-Z][A-Za-z,() /+&-]{8,90}\s+\d{1,3}\b|"
    r"\bAOS-CX\s+\d+\.\d+.*?Guide\s*\|",
    re.IGNORECASE,
)
PDF_TABLE_HEADING_RE = re.compile(
    r"\b(?:Objective|Module|Script|Configuration|Show Commands|GROUP NAME|GROUP PRIORITY|"
    r"Default\s+-\s+Includes|RADIUS Server:|TACACS\+ Server:|RadSec Server:)\b",
    re.IGNORECASE,
)
CONFIG_DUMP_SECTION_RE = re.compile(r"^(?:CE|PE)\d+\s+Configuration$", re.IGNORECASE)
CONFIG_DUMP_ANSWER_RE = re.compile(
    r"(?:Current configuration:|show\s+(?:run|running-config)|export-password:|"
    r"hostname\s+(?:CE|PE)\d+|Version\s+Arub\s*a?\s*OS-CX|"
    r"^\s*!\s*$|^\s*vlan\s+\d+|^\s*interface\s+1/1/|^\s*router\s+(?:ospf|bgp)|"
    r"^\s*vrf\s+\S+|^\s*exit\s*$)",
    re.IGNORECASE | re.MULTILINE,
)
SHOW_OUTPUT_TABLE_SECTION_RE = re.compile(
    r"^(?:VRF\s+Address\s+Label\s+Interface(?:\s+VRF)?|Label\s+Interface\s+VRF|"
    r"Prefix\s+Nexthop\s+Interface\s+VRF\(egress\)\s+Origin/|"
    r"Allowed\s+VLAN\s+List:\s+all|Interface\s+Queue|Exit\s+Bindings|"
    r"Origin\s+Prefix\s+Incoming)$",
    re.IGNORECASE,
)
SHOW_OUTPUT_TABLE_ANSWER_RE = re.compile(
    r"(?:-{8,}|VRF\s+Address\s+Label\s+Interface|Prefix\s+Nexthop\s+Interface|"
    r"Allowed\s+VLAN\s+List|Interface\s+Queue|Exit\s+Bindings|Origin\s+Prefix\s+Incoming|"
    r"MAC\s+Address|Port\s+VLAN\s+ID|Status\s+Reason|Admin\s+State|Operational\s+State)",
    re.IGNORECASE,
)
FINAL_SMALL_NOISY_TOPIC_RE = re.compile(
    r"^(?:Management Address|For other routers on the same VLAN interface \(except|"
    r"MLD Snooping VLAN Counters|Troubleshooting steps|Interface)$",
    re.IGNORECASE,
)
GENERIC_WEAK_TOPIC_RE = re.compile(
    r"^(?:Interface|Configuration|Status|Statistics|Counters|Management Address|"
    r"Troubleshooting steps|Show Commands|Module)$",
    re.IGNORECASE,
)
REMAINING_TABLE_OUTPUT_RE = re.compile(
    r"(?:Port\s+Description|Port\s+VLAN-ID|System\s+Capabilities|Enabled\s+Capabilities|"
    r"Remote\s+Management\s+Address|Allowed\s+VLAN\s+List|Interface\s+Queue|"
    r"MLD\s+Snooping\s+VLAN\s+Counters|Counter\s+Name|Counter\s+Value|"
    r"\bPackets\b|\bBytes\b|-{8,})",
    re.IGNORECASE,
)
INCOMPLETE_CONNECTOR_RE = re.compile(r"\b(?:except|and|or|for|with|from|to)$", re.IGNORECASE)
FINAL_OUTPUT_LIKE_RE = re.compile(
    r"(?:Current configuration:|show\s+run|export-password:|Version\s+Arub\s*a?\s*OS-CX|"
    r"-{8,}|Exit\s+Bindings|Origin\s+Prefix\s+Incoming|Prefix\s+Nexthop\s+Interface|"
    r"Allowed\s+VLAN\s+List|Interface\s+Queue|VRF\s+Address\s+Label\s+Interface|"
    r"Label\s+Interface\s+VRF|hostname\s+CE|hostname\s+PE)",
    re.IGNORECASE,
)
BULLET_FRAGMENT_SECTION_RE = re.compile(
    r"^(?:[\u2022\u25e6?*]|â€¢|â—¦|-)\s+",
    re.IGNORECASE,
)
BAD_PAGE_HEADER_USECASE_RE = re.compile(
    r"^(?:Troubleshooting steps\s+\d+|Public Use cases?\s+\d+|Public Use case\s+\d+|"
    r"[A-Z][A-Za-z0-9 ,()/:-]{8,}\s+\d{1,4})$",
    re.IGNORECASE,
)
ANSWER_BOILERPLATE_RE = re.compile(
    r"AOS-CX\s+10\.|Guide\s*\||Switch Series\)|Command History|Command Information|"
    r"Release\s*\|\s*Modification|Platforms?\s*\|\s*Command context|\.{8,}",
    re.IGNORECASE,
)
COMMAND_OUTPUT_SECTION_RE = re.compile(
    r"(?:^Failure Reason\s*:|^LLDP Port Configuration$|^Interface Name\s*:|"
    r".*Routing Table.*|^OSPF Process ID.*|^OSPFv3 Process ID.*|"
    r"^Interface\s+.*\s+is\s+(?:up|down).*|.*Line Protocol is.*|"
    r"(?:^|,\s*)Interface\s+\d+/\d+(?:/\d+)?\s*$|"
    r".*Group\s+\d+\s+-\s+Address-Family.*|^State is\s+.*|^\*?\s*Global RADIUS Configuration\s*\*?$|"
    r"^Interface status\s*:.*|^VSX configuration$|^Unknown Interface Drops$|^Bad Header Length Drops$|"
    r"^Wrong OSPFv3 Version Drops$|^Total Drops$|^Virtual IP address is.*|^Virtual MAC address is.*|"
    r"^Advertisement interval is.*|^Active Router is.*|"
    r"^switch#.*|^SVOS>.*|^traceroute to\b|TTL Security Hops\s*:|Session Interface VRFsource IP|"
    r"^MST\d+\b)",
    re.IGNORECASE,
)
COMMAND_OUTPUT_ANSWER_RE = re.compile(
    r"(?:\bswitch#|\bswitch\(config|\bSVOS>|"
    r"\bInterface\s+\S+\s+is\s+(?:up|down)\b|"
    r"\bLine Protocol is\s+(?:up|down)\b|"
    r"\bState is\s+(?:ACTIVE|MASTER|BACKUP|INIT|DOWN|UP)\b|"
    r"\bOSPF Process ID\b|\bOSPFv3 Process ID\b|\bRouting Table\b|"
    r"\bVRF\s+\S+,\s*Routing Table\b|\bUnknown Interface Drops\b|"
    r"\bBad Header Length Drops\b|\bWrong OSPFv3 Version Drops\b|\bTotal Drops\b|"
    r"\bVirtual IP address is\b|\bVirtual MAC address is\b|\bAdvertisement interval is\b|"
    r"\bActive Router is\b|\bGlobal RADIUS Configuration\b|\bInterface status\s*:|"
    r"\bFailure Reason\s*:|\bLLDP Port Configuration\b|\bInterface Name\s*:|"
    r"\bMessage statistics:\s*Sent\s+Rcvd\b|\bPORT\s+ROLE\s+STATE\s+COST\s+PRIORITY\b|"
    r"\bShared-Secret\s*:|\bTracking User-name\s*:|\bNumber of Servers\s*:|"
    r"\bState abbreviations\s*:|\btraceroute to\b|^\s*\|\s*.+\|\s*$|^-{5,}$)",
    re.IGNORECASE | re.MULTILINE,
)
OUTPUT_SENSITIVE_FAMILIES = {
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
TOC_ONLY_RE = re.compile(r"^(?:contents|table of contents|[A-Za-z0-9 /_-]{1,80})$", re.IGNORECASE)
LABEL_ONLY_SECTIONS = {
    "syntax",
    "description",
    "command context",
    "command_context",
    "authority",
    "parameter",
    "parameters",
    "example",
    "examples",
    "usage",
    "command information",
    "command history",
    "platforms",
    "modification",
    "release",
}
CHAPTER_RE = CHAPTER_SECTION_RE
SYNTAX_PROMPT_POLLUTION_RE = re.compile(
    r"\bswitch(?:\([^)]*\))?[>#]|\bswitch\(config|\(config-if\)|\(config-hsc\)",
    re.IGNORECASE,
)
INVALID_SYNTAX_FRAGMENT_RE = re.compile(
    r"\b(?:Context:|Command context|Platforms?|Authority|Description|Examples?|Parameters?|"
    r"Modification|Release|AOS-CX|Guide\s*\||page\b|traceroute to|Interface is up|"
    r"State is ACTIVE|SVOS>|switch#|switch\(config)",
    re.IGNORECASE,
)
SYNTAX_CONTEXT_ONLY_RE = re.compile(r"^(?:Context:\s*)?config(?:-[A-Za-z0-9-]+)?\s*:?$", re.IGNORECASE)
CLI_PROMPT_RE = re.compile(r"\b(?:switch(?:\([^)]*\))?[>#]|SVOS>)\s*(?:\|\s*)?", re.IGNORECASE)
PAGE_HEADER_FOOTER_RE = re.compile(
    r"\bAOS-CX\s*[\d.]+\s*.*?Guide\s*\|\s*User\s*Guide\b|"
    r"\bAOS-CX10\.\d+\b|"
    r"\b[A-Za-z][A-Za-z ]{1,80}\s*\|\s*\d+\b|"
    r"\b[A-Za-z]{2,}\|\d+\b|"
    r"\bBFD\s*\|\s*\d+\b",
    re.IGNORECASE,
)
OCR_DAMAGE_PHRASES = (
    "todisable",
    "issuethe",
    "withoutthe",
    "setsthesource",
    "thisaddress",
    "thisaddressisused",
    "mustnotbe",
    "onthesame",
    "anyswitch",
    "otherwisealarge",
    "packetsmay",
    "wherexisadecimalnumber",
    "wherexis",
    "specifiesa",
    "specifiesasessionid",
    "specifiestheaddress",
    "numberoficmpredirect",
    "theinterface",
    "thenoformofthiscommand",
    "commandscontext",
    "aos-cx10.07high",
    "userguide",
    "bfd|33",
    "high availability |",
    "about this document |",
    "commandtochange",
)
MIXED_FILE_OCR_DAMAGE_PHRASES = (
    "clearsall",
    "snoopingisdisabledbydefault",
    "snoopingforthespecified",
    "formofthecommand",
    "bindingslearned",
    "Setsthedestination",
    "addressforthetunnel",
    "Foran IPv6",
    "enterthecommand",
    "groupnamed",
    "assignTACACS",
    "showthe",
    "Definethe",
    "sequencelist",
    "Rad Secwhileaddingdevices",
    "source IP oftheswitch",
    "Highestadministrativeweight",
    "Administrativeweightcanbeassigned",
    "LOCAL_PREFPA",
    "NLRIlocallyona",
    "addressfamily",
    "Selectsthe",
    "Theautogeneratedsequencenumber",
    "derivedbyadding",
    "Operatorsor",
    "Administratorsorlocalusergroupmembers",
    "Remotesyslogenables",
    "maximumoffour",
)
MERGED_WORD_PATTERNS = (
    r"\bQualityof\b",
    r"\bClassof\b",
    r"\bThedefaultgatewaysforhosts\b",
    r"\bTheautogeneratedsequencenumber\b",
    r"\bAdministratorsorlocalusergroupmembers\b",
    r"\bCommandcontext\b",
    r"\bRemotesyslogenables\b",
    r"\bSelectsthe\b",
    r"\bSpecifiesthe\b",
    r"\bshowthe\b",
    r"\benterthecommand\b",
    r"\bsourceIPoftheswitch\b",
)
MERGED_WORD_RE = re.compile("|".join(MERGED_WORD_PATTERNS), re.IGNORECASE)
SPACING_OCR_PATTERNS = (
    r"\bdes ired\b",
    r"\bmanage ment\b",
    r"\bconso le\b",
    r"\blogin-attem pts\b",
    r"\bAssoci ation\b",
    r"\bser ver\b",
    r"\bco nfigured\b",
    r"\bswi tch\b",
    r"\bp resent\b",
    r"\bUsernam e\b",
    r"\bprivileg e\b",
    r"\bNotif ications\b",
    r"\bPolic ing\b",
    r"\bQualityof\b",
    r"\bClassof\b",
    r"\bCommandcontext\b",
    r"\bSpecifiesthe\b",
    r"\bSelectsthe\b",
    r"\benterthecommand\b",
)
SPACING_OCR_RE = re.compile("|".join(SPACING_OCR_PATTERNS), re.IGNORECASE)
MERGED_WORD_HINTS = (
    "command",
    "interface",
    "address",
    "specifies",
    "session",
    "context",
    "default",
    "milliseconds",
)
PROCEDURE_ACTION_RE = re.compile(
    r"^(?:Configuring|Configure|Enabling|Enable|Disabling|Disable|Creating|Create|Adding|Add|"
    r"Removing|Remove|Deleting|Delete|Verifying|Verify|Viewing|View|Troubleshooting|"
    r"Replacing|Installing|Uploading|Downloading|Accessing|Logging\s+in)\b",
    re.IGNORECASE,
)
BAD_PROCEDURE_TRIGGER_RE = re.compile(
    r"\b(?:Overview|Command|Command Information|Command History|Configuration concepts|"
    r"Example|Examples|Figure|Table|Image|Panel|Restrictions|Limitations)\b",
    re.IGNORECASE,
)
FAKE_COMMAND_START_RE = re.compile(
    r"^(?:If you attempt|Interface\b.*\bis up\b|traceroute to|State is|Unknown Interface Drops|"
    r"Figure\b|Table\b|Chapter\b|AOS-CX\b|Command Information\b|Command History\b)",
    re.IGNORECASE,
)
ORPHAN_SEQUENCE_COMMAND_RE = re.compile(
    r"^(?:no\s+)?(?:<SEQUENCE-NUMBER>|\[<SEQUENCE-NUMBER>\]|SEQUENCE-NUMBER)$",
    re.IGNORECASE,
)
ORPHAN_SYNTAX_FRAGMENT_RE = re.compile(
    r"^(?:(?:no\s+)?(?:<SEQUENCE-NUMBER>|\[<SEQUENCE-NUMBER>\]|SEQUENCE-NUMBER)|"
    r"Context:\s*config(?:-[A-Za-z0-9-]+)?\s*:|"
    r"Parameters?|Authority|Platforms|Usage|Examples?)$",
    re.IGNORECASE,
)
PLACEHOLDER_TOKEN_RE = re.compile(r"<[^>]+>|\[[^\]]+\]|\{[^}]+\}")
OPERAND_WORD_RE = re.compile(
    r"^(?:vlan|voice-vlan-query|tos|fragment|count|rx|tx|both|vsx-peer|ip|ipv6|mac|interface|port|vrf)$",
    re.IGNORECASE,
)


def normalize(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "").replace("\xa0", " ")).strip()


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text or ""))


def exact_qa_dedupe_key(row: dict[str, Any]) -> str:
    messages = row.get("messages", [])
    question = messages[0].get("content", "") if isinstance(messages, list) and len(messages) > 0 else ""
    answer = messages[1].get("content", "") if isinstance(messages, list) and len(messages) > 1 else ""
    return f"{normalize(question).lower()}||{normalize(answer).lower()}"


def _messages(row: dict[str, Any]) -> tuple[str, str] | None:
    messages = row.get("messages")
    if not isinstance(messages, list) or len(messages) != 2:
        return None
    if messages[0].get("role") != "user" or messages[1].get("role") != "assistant":
        return None
    return normalize(messages[0].get("content", "")), normalize(messages[1].get("content", ""))


def _is_syntax_only(row: dict[str, Any], answer: str) -> bool:
    if row.get("data_family") == "cli_command_reference" and "syntax:" in answer.lower():
        return True
    return row.get("syntax") and answer.lower().startswith("the syntax")


def _syntax_looks_corrupted(row: dict[str, Any], answer: str) -> bool:
    syntax = normalize(row.get("syntax", ""))
    if not syntax:
        return False
    if PLACEHOLDER_RE.search(syntax):
        return True
    if len(syntax) > 500:
        return True
    if syntax.count("<") != syntax.count(">"):
        return True
    if "  " in syntax:
        return True
    return "syntax: syntax" in answer.lower()


def _syntax_has_prompt_pollution(row: dict[str, Any]) -> bool:
    syntax = normalize(row.get("syntax", ""))
    if not syntax:
        return False
    return bool(SYNTAX_PROMPT_POLLUTION_RE.search(syntax))


def _field_text(row: dict[str, Any], *fields: str) -> str:
    return " ".join(normalize(row.get(field, "")) for field in fields if normalize(row.get(field, "")))


def _is_support_footer_row(row: dict[str, Any], question: str, answer: str) -> bool:
    section_text = _field_text(row, "section", "topic", "task")
    if any(SUPPORT_FOOTER_SECTION_RE.fullmatch(part) for part in (normalize(row.get("section", "")), normalize(row.get("topic", "")), normalize(row.get("task", ""))) if part):
        return True
    if SUPPORT_FOOTER_SECTION_RE.search(question):
        return True
    support_hits = len(SUPPORT_FOOTER_TEXT_RE.findall(answer))
    if support_hits >= 2:
        return True
    if SUPPORT_FOOTER_TEXT_RE.search(section_text) and word_count(answer) <= 120:
        return True
    if re.search(r"https?://\S+", answer) and re.search(r"\b(?:support|warranty|portal|end-of-life|updates?)\b", answer, re.IGNORECASE):
        return True
    return False


def _is_visual_caption_row(row: dict[str, Any], question: str, answer: str) -> bool:
    section_text = _field_text(row, "section", "topic", "task", "command")
    if BAD_VISUAL_SECTION_RE.match(section_text):
        return True
    if BAD_VISUAL_SECTION_RE.search(question):
        return True
    if VISUAL_CAPTION_ANSWER_RE.search(answer):
        return True
    if row.get("data_family") in {"concept_explanation", "configuration_procedure", "web_ui_task"}:
        if BAD_VISUAL_SECTION_RE.match(answer):
            return True
    return False


def _candidate_fields(row: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        normalize(row.get(field, ""))
        for field in ("section", "topic", "task", "command")
        if normalize(row.get(field, ""))
    )


def _balanced_field_values(row: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        normalize(row.get(field, ""))
        for field in ("section", "topic", "task", "command", "syntax")
        if normalize(row.get(field, ""))
    )


def is_document_title_like(text: str) -> bool:
    cleaned = normalize(text).strip(":- ")
    return bool(cleaned and DOCUMENT_TITLE_RE.match(cleaned))


def is_chapter_title_like(text: str) -> bool:
    cleaned = normalize(text).strip(":- ")
    return bool(cleaned and CHAPTER_SECTION_RE.match(cleaned))


def is_command_metadata_section(text: str) -> bool:
    cleaned = normalize(text).strip(":- ")
    return bool(cleaned and COMMAND_METADATA_SECTION_RE.fullmatch(cleaned))


def is_generic_metadata_section(text: str) -> bool:
    cleaned = normalize(text).strip(":- ")
    return bool(cleaned and GENERIC_METADATA_SECTION_RE.match(cleaned))


def is_example_section_like(text: str) -> bool:
    cleaned = normalize(text).strip()
    return bool(cleaned and EXAMPLE_SECTION_RE.match(cleaned))


def is_example_like_text(text: str) -> bool:
    cleaned = normalize(text).strip()
    return bool(cleaned and (EXAMPLE_SECTION_RE.match(cleaned) or EXAMPLE_LIKE_SECTION_RE.search(cleaned)))


def is_web_ui_fake_cli_row(row: dict[str, Any]) -> bool:
    if str(row.get("source_type", "")) != "product_web_ui":
        return False
    if str(row.get("data_family", "")) not in {"cli_command_reference", "show_command_reference"}:
        return False
    command = normalize(row.get("command", "") or row.get("section", ""))
    return bool(command and WEB_UI_FAKE_CLI_COMMAND_RE.fullmatch(command))


def is_event_log_source_misclassified_row(row: dict[str, Any]) -> bool:
    return (
        str(row.get("source_type", "")) == "product_event_log_reference"
        and str(row.get("data_family", "")) != "event_log_reference"
    )


def question_asks_command_syntax(question: str) -> bool:
    return bool(SYNTAX_QUESTION_RE.search(normalize(question)))


def event_id_requested_by_question(question: str) -> str:
    match = EVENT_ID_QUESTION_RE.search(normalize(question))
    return match.group(1).strip(" ?.") if match else ""


def has_suspicious_erps_expansion(text: str) -> bool:
    return bool(BAD_ERPS_EXPANSION_RE.search(normalize(text)))


def is_fake_command_heading_text(text: str) -> bool:
    cleaned = normalize(text).strip(" .:-")
    return bool(cleaned and FAKE_COMMAND_HEADING_RE.fullmatch(cleaned))


def is_fake_command_heading_row(row: dict[str, Any]) -> bool:
    if str(row.get("data_family", "")) not in {"cli_command_reference", "show_command_reference"}:
        return False
    return is_fake_command_heading_text(str(row.get("command", "") or "")) or is_fake_command_heading_text(
        str(row.get("syntax", "") or "")
    )


def is_hardening_guide_row(row: dict[str, Any]) -> bool:
    return str(row.get("source_type", "")) == "product_hardening" and "hardening guide" in normalize(
        row.get("document_title", "")
    ).lower()


def has_page_header_fragment(text: str) -> bool:
    return bool(PAGE_HEADER_RE.search(normalize(text)))


def has_balanced_syntax_symbols(syntax: str) -> bool:
    cleaned = normalize(syntax)
    if not cleaned:
        return True
    pairs = {"]": "[", "}": "{", ">": "<"}
    openings = set(pairs.values())
    stack: list[str] = []
    for char in cleaned:
        if char in openings:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


def has_balanced_symbols(text: str) -> bool:
    """
    Validate balanced [], {}, and <>.

    Product-doc command fragments with malformed symbols are usually truncated
    extraction noise, so callers should prefer dropping over guessing.
    """
    return has_balanced_syntax_symbols(text)


def looks_like_parameter_or_syntax_fragment(text: str) -> bool:
    cleaned = normalize(text).strip(" .:")
    if not cleaned:
        return False
    if cleaned[0] in "<[{":
        return True
    if not has_balanced_syntax_symbols(cleaned):
        return True
    placeholder_count = len(PLACEHOLDER_TOKEN_RE.findall(cleaned))
    if placeholder_count <= 0:
        return False
    words = [word.lower() for word in re.findall(r"\b[A-Za-z][A-Za-z0-9_-]*\b", cleaned)]
    placeholder_words = {
        part.lower()
        for placeholder in PLACEHOLDER_TOKEN_RE.findall(cleaned)
        for part in re.findall(r"[A-Za-z][A-Za-z0-9_-]*", placeholder)
    }
    normal_words = [word for word in words if word not in placeholder_words and word not in {"or", "and"}]
    if placeholder_count >= max(1, len(normal_words)):
        return True
    if placeholder_count and len(normal_words) <= 3 and any(OPERAND_WORD_RE.fullmatch(word) for word in normal_words):
        return True
    return False


def command_output_indicator_count(text: str) -> int:
    cleaned = normalize(text)
    if not cleaned:
        return 0
    return len(COMMAND_OUTPUT_ANSWER_RE.findall(cleaned))


def command_output_counter_like_count(text: str) -> int:
    cleaned = normalize(text)
    if not cleaned:
        return 0
    return len(
        re.findall(
            r"\b[A-Za-z][A-Za-z /()_-]{2,48}\s*:\s*"
            r"(?:\d+|up|down|ACTIVE|MASTER|BACKUP|INIT|None|[0-9A-Fa-f:.]{3,})\b",
            cleaned,
        )
    )


def looks_like_command_output_text(text: str) -> bool:
    cleaned = normalize(text).strip(":- ")
    if not cleaned:
        return False
    if COMMAND_OUTPUT_SECTION_RE.search(cleaned):
        return True
    if command_output_indicator_count(cleaned) >= 2:
        return True
    pipe_count = cleaned.count("|")
    if pipe_count >= 6 and not re.search(r"\b(?:displays|shows|configures|enables|describes|documents)\b", cleaned, re.IGNORECASE):
        return True
    return command_output_counter_like_count(cleaned) >= 4


def is_bad_final_section(section: str, command: str = "") -> bool:
    cleaned = normalize(section).strip(":- ")
    if not cleaned:
        return True
    if is_document_title_like(cleaned) or is_chapter_title_like(cleaned) or is_command_metadata_section(cleaned):
        return True
    if BAD_VISUAL_SECTION_RE.match(cleaned) or SUPPORT_FOOTER_SECTION_RE.fullmatch(cleaned):
        return True
    if COMMAND_OUTPUT_SECTION_RE.search(cleaned):
        return True
    if cleaned.lower().startswith(("aos-cx", "chapter")):
        return True
    if "guide |" in cleaned.lower() or "switch series)" in cleaned.lower() or "................................................................" in cleaned:
        return True
    if re.search(r"\bpage\s+\d+$", cleaned, re.IGNORECASE):
        return True
    if is_long_bad_final_section(cleaned, command):
        return True
    if "|" in cleaned and not _looks_like_valid_command_section(cleaned, command):
        return True
    return False


def is_good_final_section(section: str, data_family: str = "", command: str = "") -> bool:
    return not is_bad_final_section(section, command)


def is_long_bad_final_section(section: str, command: str = "") -> bool:
    cleaned = normalize(section).strip(":- ")
    return bool(cleaned and len(cleaned) > 90 and not _looks_like_valid_command_section(cleaned, command))


def _looks_like_valid_command_section(section: str, command: str = "") -> bool:
    cleaned = normalize(section)
    normalized_command = normalize(command)
    if normalized_command and cleaned.lower() == normalized_command.lower():
        return True
    if cleaned.lower().startswith(("show ", "clear ", "copy ", "ip ", "ipv6 ", "aaa ", "access-list ", "snmp-server ")):
        return True
    if re.search(r"<[^>]+>|\[[^\]]+\]|\{[^}]+}", cleaned) and word_count(cleaned) <= 14:
        return True
    return False


def _has_document_title_row(row: dict[str, Any], question: str) -> bool:
    if any(is_document_title_like(value) for value in _candidate_fields(row)):
        return True
    return bool(DOCUMENT_TITLE_QUESTION_RE.search(question))


def _has_chapter_title_row(row: dict[str, Any], question: str) -> bool:
    if any(is_chapter_title_like(value) for value in _candidate_fields(row)):
        return True
    return bool(re.search(r"\bwhat does the guide say about Chapter\s+\d+\b", question, re.IGNORECASE))


def _has_command_metadata_section(row: dict[str, Any], question: str) -> bool:
    if any(is_command_metadata_section(value) for value in _candidate_fields(row)):
        return True
    return bool(re.search(r"\b(?:Command History|Command Information|Commands context|Command context)\b", question, re.IGNORECASE))


def _has_generic_metadata_section(row: dict[str, Any], question: str) -> bool:
    if any(is_generic_metadata_section(value) for value in _candidate_fields(row)):
        return True
    return bool(
        re.search(
            r"\b(?:Command or|procedure Example|Configuration concepts|Configuration prerequisites)\b",
            question,
            re.IGNORECASE,
        )
    )


def _has_example_section(row: dict[str, Any], question: str) -> bool:
    # Example datasets are intentionally disabled for now, so example-like sections
    # are kept out of the main product-doc training set.
    if any(is_example_section_like(value) for value in _candidate_fields(row)):
        return True
    return bool(re.search(r"\bwhat does the guide say about Examples?(?:\s*:|\s+of\b|\s+using\b|\b)", question, re.IGNORECASE))


def _has_example_like_concept(row: dict[str, Any], question: str) -> bool:
    if str(row.get("data_family", "")) in {"command_example", "documentation_example"}:
        return False
    if str(row.get("data_family", "")) not in {
        "concept_explanation",
        "security_policy",
        "routing_feature",
        "qos_policy",
        "monitoring_feature",
        "feature_limitation",
        "web_ui_task",
        "troubleshooting",
    }:
        return False
    if any(is_example_like_text(value) for value in _candidate_fields(row)):
        return True
    return bool(
        re.search(
            r"(?:Classifier policies configuration example|<VLAN-LIST>\s+command,\s*for example|"
            r"\bconfiguration example\b|,\s*for example\b|Example success message|Example HTML source)",
            question,
            re.IGNORECASE,
        )
    )


def is_hardening_noisy_field(text: str) -> bool:
    cleaned = normalize(text).strip(":- ")
    if not cleaned:
        return False
    if HARDENING_NOISY_HEADING_RE.fullmatch(cleaned):
        return True
    page_match = HARDENING_PAGE_HEADING_RE.fullmatch(cleaned)
    if page_match:
        title = page_match.group("title").strip().lower()
        return title in HARDENING_CLEAN_TOPICS or len(title.split()) <= 8
    if re.search(r"\b(?:Public|Subtopics)\b", cleaned, re.IGNORECASE) and re.search(r"\b\d{1,3}$", cleaned):
        return True
    return False


def _has_hardening_noisy_row(row: dict[str, Any], question: str) -> bool:
    if not is_hardening_guide_row(row):
        return False
    if any(is_hardening_noisy_field(value) for value in _candidate_fields(row)):
        return True
    return bool(HARDENING_NOISY_HEADING_RE.search(question))


def is_bullet_fragment_field(text: str) -> bool:
    return bool(BULLET_FRAGMENT_SECTION_RE.match(normalize(text)))


def _has_bullet_fragment_row(row: dict[str, Any], question: str) -> bool:
    if any(is_bullet_fragment_field(value) for value in _candidate_fields(row)):
        return True
    return bool(BULLET_FRAGMENT_SECTION_RE.search(question))


def is_page_header_usecase_field(text: str) -> bool:
    return bool(BAD_PAGE_HEADER_USECASE_RE.fullmatch(normalize(text).strip(":- ")))


def _has_page_header_usecase_row(row: dict[str, Any], question: str) -> bool:
    if any(is_page_header_usecase_field(value) for value in _candidate_fields(row)):
        return True
    return bool(BAD_PAGE_HEADER_USECASE_RE.search(question))


def is_final_small_noisy_field(text: str) -> bool:
    return bool(FINAL_SMALL_NOISY_TOPIC_RE.fullmatch(normalize(text).strip(":- ")))


def _has_final_small_noisy_row(row: dict[str, Any], question: str) -> bool:
    if not _is_topic_quality_sensitive_row(row):
        return False
    if any(is_final_small_noisy_field(value) for value in _candidate_fields(row)):
        return True
    return bool(FINAL_SMALL_NOISY_TOPIC_RE.search(question))


def is_generic_weak_topic_field(text: str) -> bool:
    return bool(GENERIC_WEAK_TOPIC_RE.fullmatch(normalize(text).strip(":- ")))


def _has_generic_weak_topic_row(row: dict[str, Any], question: str) -> bool:
    if not _is_topic_quality_sensitive_row(row):
        return False
    if any(is_generic_weak_topic_field(value) for value in _candidate_fields(row)):
        return True
    return bool(re.search(r"\bwhat does the guide say about (?:Interface|Configuration|Status|Statistics|Counters|Module)\?", question, re.IGNORECASE))


def is_broken_truncated_topic_field(text: str) -> bool:
    cleaned = normalize(text).strip(":- ")
    if not cleaned:
        return False
    if cleaned.count("(") != cleaned.count(")"):
        return True
    if INCOMPLETE_CONNECTOR_RE.search(cleaned):
        return True
    if cleaned.startswith(("For other routers on the same VLAN interface",)):
        return True
    return False


def _has_broken_truncated_topic_row(row: dict[str, Any], question: str) -> bool:
    if not _is_topic_quality_sensitive_row(row):
        return False
    if any(is_broken_truncated_topic_field(value) for value in _candidate_fields(row)):
        return True
    return bool(is_broken_truncated_topic_field(question))


def _has_bad_final_section(row: dict[str, Any]) -> bool:
    return is_bad_final_section(normalize(row.get("section", "")), normalize(row.get("command", "")))


def _has_long_bad_section(row: dict[str, Any]) -> bool:
    return is_long_bad_final_section(normalize(row.get("section", "")), normalize(row.get("command", "")))


def _has_bad_concept_section(row: dict[str, Any]) -> bool:
    family = str(row.get("data_family", ""))
    if family not in {"concept_explanation", "routing_feature", "security_policy", "qos_policy", "monitoring_feature", "feature_limitation"}:
        return False
    section = normalize(row.get("section", ""))
    topic = normalize(row.get("topic", ""))
    if is_bad_final_section(section):
        return True
    if topic and is_bad_final_section(topic):
        return True
    if section.lower() == "overview" or topic.lower() == "overview":
        return True
    return bool(COMMAND_OUTPUT_SECTION_RE.search(section) or COMMAND_OUTPUT_SECTION_RE.search(topic))


def _has_parameter_fragment_topic(row: dict[str, Any]) -> bool:
    if not _is_output_sensitive_row(row):
        return False
    for value in _candidate_fields(row):
        if looks_like_parameter_or_syntax_fragment(value):
            return True
    return False


def is_parameter_description_topic(text: str) -> bool:
    cleaned = normalize(text).strip()
    return bool(cleaned and PARAMETER_DESCRIPTION_TOPIC_RE.match(cleaned))


def _has_parameter_description_topic(row: dict[str, Any]) -> bool:
    if str(row.get("data_family", "")) in {"cli_command_reference", "show_command_reference"}:
        return False
    if not _is_output_sensitive_row(row):
        return False
    for field in ("section", "topic", "task"):
        if is_parameter_description_topic(str(row.get(field, "") or "")):
            return True
    return False


def _has_syntax_fragment_topic(row: dict[str, Any]) -> bool:
    if not _is_output_sensitive_row(row):
        return False
    for value in _candidate_fields(row):
        cleaned = normalize(value)
        if cleaned and not has_balanced_syntax_symbols(cleaned):
            return True
        if cleaned.startswith(("[", "{")):
            return True
    return False


def _is_output_sensitive_row(row: dict[str, Any]) -> bool:
    return str(row.get("data_family", "")) in OUTPUT_SENSITIVE_FAMILIES


def _is_topic_quality_sensitive_row(row: dict[str, Any]) -> bool:
    return str(row.get("data_family", "")) in OUTPUT_SENSITIVE_FAMILIES


def _has_bad_output_section(row: dict[str, Any]) -> bool:
    if not _is_output_sensitive_row(row):
        return False
    messages = _messages(row)
    question = messages[0] if messages else ""
    return looks_like_command_output_text(_field_text(row, "section", "topic", "task", "command") + " " + question)


def _has_answer_output_fragment(row: dict[str, Any], answer: str) -> bool:
    if not _is_output_sensitive_row(row):
        return False
    if command_output_indicator_count(answer) >= 2:
        return True
    counter_like = command_output_counter_like_count(answer)
    if counter_like >= 4:
        return True
    if counter_like >= 2 and re.search(r"\b(?:Rx|Tx)\s+Statistics\b|={5,}|-{5,}", answer, re.IGNORECASE):
        return True
    pipe_count = answer.count("|")
    if pipe_count >= 8 and not re.search(r"\b(?:displays|shows|configures|enables|describes|documents)\b", answer, re.IGNORECASE):
        return True
    return False


def _has_command_output_content(row: dict[str, Any], answer: str) -> bool:
    if row.get("data_family") == "command_example":
        return False
    if not _is_output_sensitive_row(row):
        return False
    section_text = _field_text(row, "section", "topic", "task")
    if looks_like_command_output_text(section_text):
        return True
    return _has_answer_output_fragment(row, answer)


def _command_fragment_count(text: str) -> int:
    cleaned = normalize(text)
    return len(
        re.findall(
            r"(?:\bswitch(?:\([^)]*\))?[>#]|\bshow\s+[a-z0-9-]+|\baaa\s+[a-z0-9-]+|"
            r"\bradius-server\s+host\b|\btacacs-server\s+host\b|\bip\s+source-interface\b|"
            r"\bipv6\s+source-interface\b|<[^>]+>)",
            cleaned,
            re.IGNORECASE,
        )
    )


def has_pdf_table_damage(row: dict[str, Any], answer: str) -> bool:
    family = str(row.get("data_family", ""))
    cleaned_answer = normalize(answer)
    field_blob = _field_text(row, "section", "topic", "task")
    if not cleaned_answer:
        return False
    if is_hardening_guide_row(row) and PDF_PAGE_HEADER_FRAGMENT_RE.search(cleaned_answer):
        return True
    if is_hardening_guide_row(row) and re.match(r"^[^:]{1,100}:\s+[a-z]", cleaned_answer):
        return True
    if PDF_TABLE_HEADING_RE.search(field_blob) and _command_fragment_count(cleaned_answer) >= 2:
        return True
    if family == "concept_explanation" and _command_fragment_count(cleaned_answer) >= 5:
        return True
    if PDF_TABLE_HEADING_RE.search(cleaned_answer) and "|" in cleaned_answer and _command_fragment_count(cleaned_answer) >= 2:
        return True
    if re.search(r"(?:[A-Z]\s){8,}[A-Z]", cleaned_answer):
        return True
    if re.search(r"-{8,}.*\|.*-{8,}", cleaned_answer):
        return True
    return False


def final_output_like_indicator_count(text: str) -> int:
    cleaned = normalize(text)
    if not cleaned:
        return 0
    return len(FINAL_OUTPUT_LIKE_RE.findall(cleaned))


def has_configuration_dump(row: dict[str, Any], answer: str) -> bool:
    if str(row.get("data_family", "")) not in OUTPUT_SENSITIVE_FAMILIES:
        return False
    field_values = _candidate_fields(row)
    if any(CONFIG_DUMP_SECTION_RE.fullmatch(value) for value in field_values):
        return True
    answer_hits = len(CONFIG_DUMP_ANSWER_RE.findall(str(answer or "")))
    if answer_hits >= 2:
        return True
    return bool(any(CONFIG_DUMP_SECTION_RE.search(value) for value in field_values) and answer_hits >= 1)


def has_show_output_table(row: dict[str, Any], answer: str) -> bool:
    family = str(row.get("data_family", ""))
    if family not in OUTPUT_SENSITIVE_FAMILIES and family not in {"cli_command_reference", "show_command_reference"}:
        return False
    field_values = _candidate_fields(row)
    if any(SHOW_OUTPUT_TABLE_SECTION_RE.fullmatch(value) for value in field_values):
        return True
    answer_hits = len(SHOW_OUTPUT_TABLE_ANSWER_RE.findall(str(answer or "")))
    if family in {"cli_command_reference", "show_command_reference"}:
        return answer_hits >= 2 and command_output_indicator_count(answer) >= 1
    return answer_hits >= 2


def remaining_table_output_indicator_count(text: str) -> int:
    cleaned = normalize(text)
    if not cleaned:
        return 0
    return len(REMAINING_TABLE_OUTPUT_RE.findall(cleaned))


def has_remaining_table_output(row: dict[str, Any], answer: str) -> bool:
    family = str(row.get("data_family", ""))
    if family not in OUTPUT_SENSITIVE_FAMILIES:
        return False
    field_hits = sum(1 for value in _candidate_fields(row) if REMAINING_TABLE_OUTPUT_RE.search(value))
    answer_hits = remaining_table_output_indicator_count(answer)
    return field_hits + answer_hits >= 2


def has_final_output_like_damage(row: dict[str, Any], answer: str) -> bool:
    family = str(row.get("data_family", ""))
    if family in {"cli_command_reference", "show_command_reference"}:
        return final_output_like_indicator_count(answer) >= 3
    return final_output_like_indicator_count(answer) >= 2


def _has_answer_boilerplate(row: dict[str, Any], answer: str) -> bool:
    if has_page_header_fragment(answer):
        return True
    if not ANSWER_BOILERPLATE_RE.search(answer):
        return False
    if _is_syntax_only(row, answer):
        syntax = normalize(row.get("syntax", ""))
        command = normalize(row.get("command", ""))
        return not (syntax and command and syntax_matches_command(command, syntax))
    return True


def _normalize_command_like(text: str, keep_leading_no: bool = True) -> str:
    cleaned = normalize(text).lower()
    cleaned = CLI_PROMPT_RE.sub("", cleaned)
    cleaned = re.sub(r"^\s*syntax\s*:\s*", "", cleaned)
    cleaned = re.sub(r"\s*\|\s*", " ", cleaned)
    cleaned = re.sub(r"[.;]+$", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" :")
    if not keep_leading_no:
        cleaned = re.sub(r"^no\s+", "", cleaned)
    return cleaned


def _is_placeholder_token(token: str) -> bool:
    cleaned = token.strip(",;.")
    if not cleaned:
        return True
    if re.fullmatch(r"(?:<[^>]+>|\[[^\]]+]|\{[^}]+})", cleaned):
        return True
    if any(char in cleaned for char in "<>[]{}"):
        return True
    if cleaned.startswith("("):
        return True
    return False


def _command_root_tokens(text: str) -> list[str]:
    cleaned = _normalize_command_like(text, keep_leading_no=False)
    tokens: list[str] = []
    for raw_token in cleaned.split():
        token = raw_token.strip(",;.")
        if _is_placeholder_token(token):
            break
        tokens.append(token)
        if len(tokens) >= 4:
            break
    return tokens


def command_root(command: str) -> str:
    """
    Normalize a command and return its stable root.

    The root removes leading "no", ignores CLI prompts, and stops before
    placeholders or optional syntax blocks so comparisons do not rely on
    variable names.
    """
    return " ".join(_command_root_tokens(command))


def _tokens_in_order(needles: list[str], haystack: list[str]) -> bool:
    normalized_haystack = [token.strip("[]{}<>.,;").lower() for token in haystack]
    position = 0
    for needle in needles:
        try:
            found = normalized_haystack.index(needle, position)
        except ValueError:
            return False
        position = found + 1
    return True


def _starts_with_command_root(text: str, root: str) -> bool:
    return bool(text == root or text.startswith(f"{root} "))


def _syntax_match_tokens(syntax: str) -> list[tuple[str, bool]]:
    cleaned = _normalize_command_like(syntax, keep_leading_no=False)
    tokens: list[tuple[str, bool]] = []
    optional_depth = 0
    for raw_token in cleaned.split():
        starts_optional = raw_token.startswith(("[", "{"))
        if starts_optional:
            optional_depth += 1
        token_optional = optional_depth > 0 or starts_optional
        pieces = re.split(r"[|/]", raw_token)
        for piece in pieces:
            token = piece.strip("[]{}<>.,;")
            if not token or token == "-":
                continue
            if re.fullmatch(r"[A-Z0-9_-]+", token) and any(char in piece for char in "<>"):
                continue
            if piece.startswith("<") or piece.endswith(">"):
                continue
            tokens.append((token.lower(), token_optional or any(char in piece for char in "[]{}<>")))
        if raw_token.endswith(("]", "}")) and optional_depth > 0:
            optional_depth -= 1
    return tokens


def _syntax_prefix_matches_tokens(command_tokens: list[str], syntax: str) -> bool:
    syntax_tokens = _syntax_match_tokens(syntax)
    if not command_tokens or not syntax_tokens:
        return False
    command_index = 0
    syntax_index = 0
    while command_index < len(command_tokens):
        if syntax_index >= len(syntax_tokens):
            return False
        syntax_token, optional = syntax_tokens[syntax_index]
        command_token = command_tokens[command_index]
        if syntax_token == command_token:
            command_index += 1
            syntax_index += 1
            continue
        if optional:
            syntax_index += 1
            continue
        return False
    return True


def _split_syntax_variants(syntax: str) -> list[str]:
    raw = str(syntax or "")
    bullet_variants = [
        line.strip()[2:].strip(" .")
        for line in raw.splitlines()
        if line.strip().startswith("- ") and line.strip()[2:].strip(" .")
    ]
    if bullet_variants:
        return bullet_variants
    return [part.strip(" .") for part in normalize(syntax).split(";") if part.strip(" .")]


def normalize_multi_syntax(command: str, syntax: str) -> tuple[bool, str]:
    """
    Validate and normalize semicolon-separated syntax variants.

    Returns (is_valid, normalized_syntax). Variants are kept only when they
    match the command root. Multiple valid variants are formatted as a newline
    bullet list for readability.
    """
    variants = _split_syntax_variants(syntax)
    if len(variants) <= 1:
        single = variants[0] if variants else normalize(syntax)
        return _single_syntax_matches_command(command, single), single
    valid_variants = [
        variant
        for variant in variants
        if has_balanced_syntax_symbols(variant) and syntax_matches_command(command, variant)
    ]
    if not valid_variants:
        return False, ""
    unique_variants = list(dict.fromkeys(valid_variants))
    if len(unique_variants) == 1:
        return True, unique_variants[0]
    return True, "\n".join(f"- {variant}" for variant in unique_variants)


def _single_syntax_matches_command(command: str, syntax: str) -> bool:
    command_norm = _normalize_command_like(command, keep_leading_no=False)
    syntax_norm_with_no = _normalize_command_like(syntax, keep_leading_no=True)
    syntax_norm = _normalize_command_like(syntax, keep_leading_no=False)
    if not command_norm or not syntax_norm:
        return False
    command_root_text = command_root(command_norm)
    if not command_root_text:
        return False
    if _starts_with_command_root(syntax_norm, command_root_text) or _starts_with_command_root(
        syntax_norm_with_no, f"no {command_root_text}"
    ):
        return True
    command_root_tokens = command_root_text.split()
    if _syntax_prefix_matches_tokens(command_root_tokens, syntax_norm) or _syntax_prefix_matches_tokens(
        command_root_tokens, syntax_norm_with_no
    ):
        return True
    syntax_root_tokens = _command_root_tokens(syntax_norm)
    if not syntax_root_tokens:
        return False
    syntax_root = " ".join(syntax_root_tokens)
    if command_root_text.startswith(syntax_root):
        syntax_tokens = syntax_norm.split()
        return _tokens_in_order(command_root_tokens, syntax_tokens)
    return False


def syntax_matches_command(command: str, syntax: str) -> bool:
    if ";" in normalize(syntax) or any(line.strip().startswith("- ") for line in str(syntax or "").splitlines()):
        return normalize_multi_syntax(command, syntax)[0]
    return _single_syntax_matches_command(command, syntax)


def _syntax_is_context_only(row: dict[str, Any]) -> bool:
    syntax = normalize(row.get("syntax", ""))
    return bool(syntax and SYNTAX_CONTEXT_ONLY_RE.fullmatch(syntax))


def _has_orphan_syntax_fragment(row: dict[str, Any]) -> bool:
    if str(row.get("data_family", "")) not in {"cli_command_reference", "show_command_reference"}:
        return False
    command = normalize(row.get("command", ""))
    syntax = normalize(row.get("syntax", ""))
    return bool(
        (command and ORPHAN_SYNTAX_FRAGMENT_RE.fullmatch(command))
        or (syntax and ORPHAN_SYNTAX_FRAGMENT_RE.fullmatch(syntax))
    )


def _has_unbalanced_syntax(row: dict[str, Any]) -> bool:
    if str(row.get("data_family", "")) not in {"cli_command_reference", "show_command_reference"}:
        return False
    syntax = normalize(row.get("syntax", ""))
    return bool(syntax and not has_balanced_syntax_symbols(syntax))


def _has_unbalanced_field(row: dict[str, Any]) -> bool:
    return any(not has_balanced_symbols(value) for value in _balanced_field_values(row))


def _has_multi_syntax_mismatch(row: dict[str, Any]) -> bool:
    if str(row.get("data_family", "")) not in {"cli_command_reference", "show_command_reference"}:
        return False
    command = normalize(row.get("command", ""))
    syntax = normalize(row.get("syntax", ""))
    return bool(command and ";" in syntax and not normalize_multi_syntax(command, syntax)[0])


def _syntax_is_invalid(row: dict[str, Any], answer: str) -> bool:
    syntax = normalize(row.get("syntax", ""))
    if not syntax:
        return False
    if syntax.isdigit():
        return True
    if INVALID_SYNTAX_FRAGMENT_RE.search(syntax):
        return True
    if SYNTAX_PROMPT_POLLUTION_RE.search(syntax):
        return True
    if re.search(r"\b(?:traceroute to|Interface is up|line protocol is up|State is ACTIVE)\b", syntax, re.IGNORECASE):
        return True
    parts = [part.strip() for part in syntax.split(";") if part.strip()]
    if len(parts) > 1:
        roots = {" ".join(_command_root_tokens(part)[:2]) for part in parts if _command_root_tokens(part)}
        if len(roots) > 1:
            return True
    return "syntax: syntax" in answer.lower()


def _syntax_root_mismatch(row: dict[str, Any]) -> bool:
    command = normalize(row.get("command", ""))
    syntax = normalize(row.get("syntax", ""))
    if not command or not syntax:
        return False
    return not syntax_matches_command(command, syntax)


def _has_sibling_command_syntax_mismatch(row: dict[str, Any]) -> bool:
    if str(row.get("data_family", "")) not in {"cli_command_reference", "show_command_reference"}:
        return False
    command = normalize(row.get("command", ""))
    syntax = normalize(row.get("syntax", ""))
    if not command or not syntax or syntax_matches_command(command, syntax):
        return False
    command_tokens = _command_root_tokens(command)
    syntax_tokens = _command_root_tokens(syntax)
    if not command_tokens or not syntax_tokens:
        return False
    if command_tokens[0] in {"show", "clear", "copy"} and syntax_tokens[0] == command_tokens[0]:
        return True
    return bool(
        re.match(r"^(?:show|clear|copy)\b", command, re.IGNORECASE)
        and re.match(r"^(?:show|clear|copy)\b", syntax, re.IGNORECASE)
    )


def _is_fake_command_name(row: dict[str, Any]) -> bool:
    command = normalize(row.get("command", ""))
    if not command:
        return False
    if word_count(command) > 10:
        return True
    if FAKE_COMMAND_START_RE.search(command):
        return True
    lowered = command.lower()
    if "if you attempt" in lowered or "guide |" in lowered or "................................................................" in command:
        return True
    if re.search(r"\bpage\s+\d+\b|\|\s*\d+\b", lowered):
        return True
    if command.count(",") > 2 or command.count(".") > 2:
        return True
    if "," in command and re.search(r",\s+(?:and|or|if|while|when|where|the|use|attempt)\b", lowered):
        return True
    if re.search(r"\b(?:is|are|was|were)\b", lowered) and not lowered.startswith(("show ", "clear ", "copy ")):
        return True
    return False


def _is_orphan_sequence_command(row: dict[str, Any]) -> bool:
    command = normalize(row.get("command", ""))
    if not command:
        return False
    if not ORPHAN_SEQUENCE_COMMAND_RE.fullmatch(command):
        return False
    context = _field_text(row, "section", "topic", "source_file")
    return not re.search(r"\baccess-list\s+(?:ip|ipv6|mac)\b", context, re.IGNORECASE)


def _mixed_ocr_indicator_count(text: str) -> int:
    lowered = normalize(text).lower()
    compact = re.sub(r"\s+", "", lowered)
    count = 0
    for phrase in MIXED_FILE_OCR_DAMAGE_PHRASES:
        phrase_lower = phrase.lower()
        if phrase_lower in lowered or re.sub(r"\s+", "", phrase_lower) in compact:
            count += 1
    return count


def _has_mixed_file_ocr_damage(row: dict[str, Any], answer: str) -> bool:
    count = _mixed_ocr_indicator_count(answer)
    if count <= 0:
        return False
    family = str(row.get("data_family", ""))
    if family in {"configuration_procedure", "web_ui_task"}:
        return True
    if family in {"cli_command_reference", "show_command_reference"}:
        return count >= 2
    return count > 2


def _has_bad_procedure_trigger(row: dict[str, Any], question: str) -> bool:
    family = str(row.get("data_family", ""))
    if family not in {"configuration_procedure", "web_ui_task", "troubleshooting"}:
        return False
    title = normalize(row.get("task") or row.get("section") or row.get("topic") or "")
    if not title:
        return True
    if SUPPORT_FOOTER_SECTION_RE.fullmatch(title) or BAD_VISUAL_SECTION_RE.match(title):
        return True
    if BAD_PROCEDURE_TRIGGER_RE.search(title):
        return True
    if re.search(r"\bhow do you\s+(?:overview|command|command information|figure|table|image|panel)\b", question, re.IGNORECASE):
        return True
    return not PROCEDURE_ACTION_RE.match(title)


def _is_generic_overview_row(row: dict[str, Any], question: str) -> bool:
    section = normalize(row.get("section", ""))
    topic = normalize(row.get("topic", ""))
    task = normalize(row.get("task", ""))
    if any(value.lower() == "overview" for value in (section, topic, task) if value):
        return True
    return bool(re.search(r"\b(?:about|for|documented for|how do you)\s+Overview\b", question, re.IGNORECASE))


def has_ocr_spacing_damage(text: str) -> bool:
    cleaned = normalize(text)
    lowered = cleaned.lower()
    if any(phrase in lowered for phrase in OCR_DAMAGE_PHRASES):
        return True
    if PAGE_HEADER_FOOTER_RE.search(cleaned):
        return True
    for word in re.findall(r"\b[A-Za-z][A-Za-z0-9-]{30,}\b", cleaned):
        lower_word = word.lower()
        if lower_word.startswith(("http", "https")):
            continue
        if any(hint in lower_word for hint in MERGED_WORD_HINTS):
            return True
    return False


def merged_word_indicator_count(text: str) -> int:
    cleaned = normalize(text)
    if not cleaned:
        return 0
    return len(MERGED_WORD_RE.findall(cleaned))


def has_merged_word_damage(text: str) -> bool:
    return merged_word_indicator_count(text) > 0


def spacing_ocr_indicator_count(text: str) -> int:
    cleaned = normalize(text)
    if not cleaned:
        return 0
    return len(SPACING_OCR_RE.findall(cleaned))


def has_spacing_ocr_damage(text: str) -> bool:
    return spacing_ocr_indicator_count(text) > 0


def _has_merged_word_damage_row(row: dict[str, Any], question: str, answer: str) -> bool:
    if any(has_merged_word_damage(value) for value in _candidate_fields(row)):
        return True
    if has_merged_word_damage(question):
        return True
    answer_hits = merged_word_indicator_count(answer)
    if answer_hits >= 2:
        return True
    if str(row.get("data_family", "")) in {"configuration_procedure", "web_ui_task", "troubleshooting"}:
        return answer_hits > 0
    return False


def _has_spacing_ocr_damage_row(row: dict[str, Any], question: str, answer: str) -> bool:
    return has_spacing_ocr_damage(" ".join((*_candidate_fields(row), question, answer)))


def _is_chapter_heading_row(row: dict[str, Any], question: str) -> bool:
    section = normalize(row.get("section", ""))
    topic = normalize(row.get("topic", ""))
    return (
        bool(CHAPTER_RE.fullmatch(section))
        or bool(CHAPTER_RE.fullmatch(topic))
        or "what does the guide say about chapter" in question.lower()
    )


def _is_noisy_parameter_row(row: dict[str, Any], answer: str) -> bool:
    if row.get("data_family") != "command_parameter_reference":
        return False
    lowered = answer.lower()
    if "|" in answer:
        return True
    if any(fragment in lowered for fragment in ("aos-cx10.07", "user guide", "command context")):
        return True
    return has_ocr_spacing_damage(answer)


def validate_qa_row(row: dict[str, Any], require_grounding: bool = True) -> tuple[bool, str]:
    pair = _messages(row)
    if pair is None:
        return False, "messages_missing_or_invalid"
    question, answer = pair
    if not question or not answer:
        return False, "empty_question_or_answer"
    if _has_document_title_row(row, question):
        return False, "document_title"
    if _has_chapter_title_row(row, question):
        return False, "chapter_title"
    if _has_example_section(row, question):
        return False, "example_section"
    if _has_example_like_concept(row, question):
        return False, "example_like_concept"
    if _has_generic_metadata_section(row, question):
        return False, "generic_metadata_section"
    if _has_command_metadata_section(row, question):
        return False, "command_metadata_section"
    if _is_support_footer_row(row, question, answer):
        return False, "support_footer"
    if _is_visual_caption_row(row, question, answer):
        return False, "visual_caption"
    if _is_chapter_heading_row(row, question):
        return False, "chapter_heading_row"
    if _is_generic_overview_row(row, question):
        return False, "generic_overview"
    if require_grounding and UNDERSCORE_VERSION_RE.search(question):
        return False, "underscore_version_in_question"
    if require_grounding and not GROUNDING_RE.search(question):
        return False, "missing_switch_version_grounding"
    if _is_noisy_parameter_row(row, answer):
        return False, "noisy_parameter_row"
    if _is_orphan_sequence_command(row):
        return False, "orphan_sequence_number_command"
    if is_web_ui_fake_cli_row(row):
        return False, "web_ui_fake_cli"
    if is_event_log_source_misclassified_row(row):
        return False, "event_log_source_misclassified"
    if (
        str(row.get("data_family", "")) in {"cli_command_reference", "show_command_reference"}
        and question_asks_command_syntax(question)
        and not answer.startswith("Syntax:")
    ):
        return False, "syntax_answer_not_short_exact"
    requested_event_id = event_id_requested_by_question(question)
    if (
        str(row.get("data_family", "")) == "event_log_reference"
        and requested_event_id
        and requested_event_id not in answer
    ):
        return False, "event_id_answer_mismatch"
    if has_suspicious_erps_expansion(answer):
        return False, "suspicious_erps_expansion"
    if is_fake_command_heading_row(row):
        return False, "fake_command_heading"
    if _is_fake_command_name(row):
        return False, "fake_command_name"
    if _has_bad_procedure_trigger(row, question):
        return False, "bad_procedure_trigger"
    if _has_hardening_noisy_row(row, question):
        return False, "hardening_noisy"
    if _has_bullet_fragment_row(row, question):
        return False, "bullet_fragment"
    if _has_page_header_usecase_row(row, question):
        return False, "page_header_usecase"
    if _has_final_small_noisy_row(row, question):
        return False, "final_small_noisy"
    if _has_generic_weak_topic_row(row, question):
        return False, "generic_weak_topic"
    if _has_broken_truncated_topic_row(row, question):
        return False, "broken_truncated_topic"
    if _has_unbalanced_field(row):
        return False, "unbalanced_field"
    if _has_syntax_fragment_topic(row):
        return False, "syntax_fragment_topic"
    if _has_parameter_fragment_topic(row):
        return False, "parameter_fragment_topic"
    if _has_parameter_description_topic(row):
        return False, "parameter_description_topic"
    if has_configuration_dump(row, answer):
        return False, "configuration_dump"
    if has_show_output_table(row, answer):
        return False, "show_output_table"
    if has_remaining_table_output(row, answer):
        return False, "remaining_table_output"
    if has_final_output_like_damage(row, answer):
        return False, "final_output_like"
    if _has_bad_output_section(row):
        return False, "bad_output_section"
    if _has_answer_output_fragment(row, answer):
        return False, "answer_output_fragment"
    if has_pdf_table_damage(row, answer):
        return False, "pdf_table_damaged"
    if _has_long_bad_section(row):
        return False, "long_bad_section"
    if _has_bad_final_section(row):
        return False, "bad_final_section"
    if _has_bad_concept_section(row):
        return False, "bad_concept_section"
    if _has_command_output_content(row, answer):
        return False, "command_output"
    if has_page_header_fragment(answer):
        return False, "remaining_page_header"
    if _has_answer_boilerplate(row, answer):
        return False, "answer_boilerplate"
    if PLACEHOLDER_RE.search(answer):
        return False, "placeholder_text"
    if (
        row.get("data_family") not in {"cli_command_reference", "show_command_reference"}
        and normalize(row.get("section", "")).lower() in LABEL_ONLY_SECTIONS
    ):
        return False, "label_only_concept_section"
    if FOOTER_NAV_RE.search(answer):
        return False, "footer_navigation_boilerplate"
    if INVISIBLE_IMAGE_RE.search(answer):
        return False, "references_invisible_image"
    if _syntax_is_context_only(row):
        return False, "syntax_context_only"
    if _has_orphan_syntax_fragment(row):
        return False, "orphan_syntax_fragment"
    if _has_unbalanced_syntax(row):
        return False, "unbalanced_syntax"
    if _has_multi_syntax_mismatch(row):
        return False, "multi_syntax"
    if _syntax_is_invalid(row, answer):
        return False, "invalid_syntax"
    if _has_sibling_command_syntax_mismatch(row):
        return False, "sibling_command_syntax_mismatch"
    if _syntax_root_mismatch(row):
        return False, "syntax_command_root_mismatch"
    if _syntax_looks_corrupted(row, answer):
        return False, "corrupted_command_syntax"
    if _syntax_has_prompt_pollution(row):
        return False, "syntax_prompt_pollution"
    if _has_mixed_file_ocr_damage(row, answer):
        return False, "mixed_file_ocr_damage"
    if _has_merged_word_damage_row(row, question, answer):
        return False, "merged_word_damage"
    if _has_spacing_ocr_damage_row(row, question, answer):
        return False, "spacing_ocr_damage"
    if has_ocr_spacing_damage(answer):
        return False, "ocr_spacing_damage"
    if answer.strip().lower() in {"n/a", "unknown", "none", "tbd"}:
        return False, "empty_semantic_answer"
    if re.search(r"\bIf\.$|\bif\.$", answer.strip()):
        return False, "incomplete_procedure"
    if not _is_syntax_only(row, answer) and word_count(answer) < 8:
        return False, "short_answer"
    if TOC_ONLY_RE.fullmatch(answer.strip(" .")) and word_count(answer) <= 8:
        return False, "answer_only_heading_or_toc"
    return True, "kept"


def validate_rows(
    rows: list[dict[str, Any]],
    require_grounding: bool = True,
) -> tuple[list[dict[str, Any]], Counter[str]]:
    kept: list[dict[str, Any]] = []
    drops: Counter[str] = Counter()
    for row in rows:
        valid, reason = validate_qa_row(row, require_grounding=require_grounding)
        if valid:
            kept.append(row)
        else:
            drops[reason] += 1
    return kept, drops


def dedupe_rows(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    seen: set[str] = set()
    kept: list[dict[str, Any]] = []
    duplicates = 0
    for row in rows:
        key = exact_qa_dedupe_key(row)
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        kept.append(row)
    return kept, duplicates


def apply_family_caps(
    rows: list[dict[str, Any]],
    caps: dict[str, int] | None = None,
) -> tuple[list[dict[str, Any]], int, Counter[str]]:
    limits = caps or PRODUCT_DOC_DATA_FAMILY_CAPS
    counts: Counter[str] = Counter()
    removed_by_family: Counter[str] = Counter()
    kept: list[dict[str, Any]] = []
    for row in rows:
        family = str(row.get("data_family", "concept_explanation"))
        limit = limits.get(family)
        if limit is not None and counts[family] >= limit:
            removed_by_family[family] += 1
            continue
        counts[family] += 1
        kept.append(row)
    return kept, sum(removed_by_family.values()), removed_by_family


def rows_with_grounding(rows: list[dict[str, Any]]) -> int:
    count = 0
    for row in rows:
        messages = row.get("messages", [])
        question = messages[0].get("content", "") if isinstance(messages, list) and messages else ""
        if GROUNDING_RE.search(normalize(question)):
            count += 1
    return count
