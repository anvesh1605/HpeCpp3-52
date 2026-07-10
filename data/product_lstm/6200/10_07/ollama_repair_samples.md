# Ollama Repair Samples

## Report

- total_review_rows: 314
- rows_sent_to_ollama: 14
- rows_repaired: 0
- rows_rejected: 314
- rows_unrepairable: 311
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6200 AOS-CX 10.07, what does the access-list mac command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "access-list mac <ACL-NAME> no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the show access-list control-plane command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list [ip|ipv6] [<ACL-NAME>] control-plane [vrf <VRF-NAME>].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the show needed-updates command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show needed-updates [next-boot [primary|secondary]].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the show ntp associations command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ntp associations.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the ubt-mode vlan-extend command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ubt-mode.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what is the syntax of the ubt-mode vlan-extend command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "ubt-mode vlan-extend", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the show port-access captive-portal-profile command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show port-access captive-portal-profile [name <PROFILE-NAME>].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the show aaa authentication port-access mac-auth interface port-statistics command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show aaa authentication port-access mac-auth interface {all|<IF-NAME>} port-statistics.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the show snmp community command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show snmp community.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.07, what does the show snmp system command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show snmp system.", "reason": "ollama_invalid_json"}
