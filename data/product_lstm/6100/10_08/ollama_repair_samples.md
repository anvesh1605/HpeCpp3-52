# Ollama Repair Samples

## Report

- total_review_rows: 67
- rows_sent_to_ollama: 58
- rows_repaired: 0
- rows_rejected: 67
- rows_unrepairable: 67
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] - snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] - no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the no shutdown command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no shutdown", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the vsx-sync command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vsx-sync", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the https-server vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no https-server vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.08, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
