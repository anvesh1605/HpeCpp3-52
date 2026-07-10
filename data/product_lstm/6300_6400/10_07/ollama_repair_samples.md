# Ollama Repair Samples

## Report

- total_review_rows: 356
- rows_sent_to_ollama: 59
- rows_repaired: 0
- rows_rejected: 356
- rows_unrepairable: 355
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the access-list mac command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "access-list mac <ACL-NAME> no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the ip ospf bfd command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip ospf bfd.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the neighbor <IP-ADDRESS> orf-prefix-list <PREFIX-LIST-NAME> in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no neighbor <IP-ADDRESS> orf-prefix-list <PREFIX-LIST-NAME> in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the ip-sla <IP-SLA-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip-sla <IP-SLA-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the IPv6 source-binding <VLAN-ID> <IPv6-ADDR> <MAC-ADDR> <IFNAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 source-binding <VLAN-ID> <IPV6-ADDR> <MAC-ADDR> <IFNAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the crypto pki certificate <CERT-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no crypto pki certificate <CERT-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the vlan <VLAN-LIST> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no vlan <VLAN-LIST>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.07, what does the no routing command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan access 1 exit.", "reason": "ollama_invalid_json"}
