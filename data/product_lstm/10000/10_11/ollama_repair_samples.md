# Ollama Repair Samples

## Report

- total_review_rows: 363
- rows_sent_to_ollama: 328
- rows_repaired: 0
- rows_rejected: 363
- rows_unrepairable: 363
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the apply copp-policy command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply copp-policy <NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the vlan <ID-RANGE> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID-RANGE>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the vsx-sync command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vsx-sync", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.11, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
