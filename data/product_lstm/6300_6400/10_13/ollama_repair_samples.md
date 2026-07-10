# Ollama Repair Samples

## Report

- total_review_rows: 164
- rows_sent_to_ollama: 113
- rows_repaired: 0
- rows_rejected: 164
- rows_unrepairable: 164
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.13, what does the show track command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show track brief show vrrp shutdown timers advertise track (VRRP group) track (VRRP virtual router) track by version vrrp vrrp dual-active-forwarding.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what does the show ip pim dfe command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ip pim dfe.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what does the show ip pim interface command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ip pim interface.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what is the syntax of the no ip pim-bidir command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip pim-bidir", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what does the apply policy <POLICY-NAME> routed-in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> routed-in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what is the syntax of the apply policy <POLICY-NAME> routed-in command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply policy <POLICY-NAME> routed-in", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what is the syntax of the IPv6 helper-address unicast <UNICAST-IPv6-ADDR> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 helper-address unicast <UNICAST-IPv6-ADDR>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.13, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
