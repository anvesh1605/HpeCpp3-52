# Ollama Repair Samples

## Report

- total_review_rows: 135
- rows_sent_to_ollama: 81
- rows_repaired: 0
- rows_rejected: 135
- rows_unrepairable: 135
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 10000 AOS-CX 10.13, what does the show user-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show user-list management-interface.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what is the syntax of the vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what is the syntax of the apply copp-policy command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply copp-policy <NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what is the syntax of the IPv6 helper-address unicast <UNICAST-IPv6-ADDR> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 helper-address unicast <UNICAST-IPv6-ADDR>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what is the syntax of the vsx-sync command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vsx-sync", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.13, what is the syntax of the https-server vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no https-server vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
