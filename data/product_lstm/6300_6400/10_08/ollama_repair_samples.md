# Ollama Repair Samples

## Report

- total_review_rows: 90
- rows_sent_to_ollama: 69
- rows_repaired: 0
- rows_rejected: 90
- rows_unrepairable: 90
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] - snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] - no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the no shutdown command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no shutdown", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what does the policy command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "policy <POLICY-NAME> [<SEQUENCE-NUMBER>] | class | {ip|ipv6|mac} | | | <CLASS-NAME> | | | | | | | ----- | ------------------ | ----------------- | --- | ------------ | ---------------- | ---------------- | --- | ------------------- | ------------------ | | | action | {<REMARK-ACTIONS> | | | | | <POLICE-ACTIONS> | | | | <OTHER-ACTIONS>} | | | [{<REMARK-ACTIONS> | | | | | <POLICE-ACTIONS> | | | | <OTHER-ACTIONS>}] | | [<SEQUENCE-NUMBER>] | comment | |... | | | | | | | | | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | AOS-CX10.08Command-LineInterfaceGuide| | | | | (6300,6400SwitchSeries) | | | | | | | -------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what does the show client device-fingerprint command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show client device-fingerprint <MAC-ADDRESS>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.08, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
