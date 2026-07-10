# Ollama Repair Samples

## Report

- total_review_rows: 154
- rows_sent_to_ollama: 117
- rows_repaired: 0
- rows_rejected: 154
- rows_unrepairable: 154
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.10, what does the vlan trunk native command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan trunk native tag voice.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what does the show track command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show track brief show vrrp shutdown timers advertise track (VRRP group) track (VRRP virtual router) track by version vrrp.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what is the syntax of the vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.10, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
