# Ollama Repair Samples

## Report

- total_review_rows: 125
- rows_sent_to_ollama: 121
- rows_repaired: 0
- rows_rejected: 125
- rows_unrepairable: 124
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6200 AOS-CX 10.18, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the show capacities command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the show resources command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show resources.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection interface show arp inspection statistics show arp inspection vlan show arp state show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the show arp state command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the ip pim-bidir hello-interval <interval-value> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip pim-bidir hello-interval <interval-value>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the ip pim-bidir hello-holdtime <holdtime-value> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip pim-bidir hello-holdtime <holdtime-value>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.18, what does the IPv6 pim6-bidir hello-interval <interval-value> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 pim6-bidir hello-interval <interval-value>.", "reason": "ollama_invalid_json"}
