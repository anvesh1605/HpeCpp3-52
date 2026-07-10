# Ollama Repair Samples

## Report

- total_review_rows: 71
- rows_sent_to_ollama: 62
- rows_repaired: 0
- rows_rejected: 71
- rows_unrepairable: 71
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] - snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] - no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the bfd min-receive-interval <INTERVAL> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no bfd min-receive-interval <INTERVAL>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the bfd min-transmit-interval <INTERVAL> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no bfd min-transmit-interval <INTERVAL>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the no shutdown command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no shutdown", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what does the show running-config command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show running-config.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.08, what is the syntax of the https-server vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no https-server vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
