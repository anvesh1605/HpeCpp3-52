# Ollama Repair Samples

## Report

- total_review_rows: 151
- rows_sent_to_ollama: 125
- rows_repaired: 0
- rows_rejected: 151
- rows_unrepairable: 151
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.12, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what does the apply policy <POLICY-NAME> routed-in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> routed-in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what is the syntax of the apply policy <POLICY-NAME> routed-in command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply policy <POLICY-NAME> routed-in", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.12, what is the syntax of the ip-sla <IP-SLA-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip-sla <IP-SLA-NAME>", "reason": "ollama_invalid_json"}
