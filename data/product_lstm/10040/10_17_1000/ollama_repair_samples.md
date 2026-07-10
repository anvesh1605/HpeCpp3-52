# Ollama Repair Samples

## Report

- total_review_rows: 246
- rows_sent_to_ollama: 225
- rows_repaired: 0
- rows_rejected: 246
- rows_unrepairable: 245
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the access-list secure-update command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "access-list secure-update.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the apply access-list (to interface or LAG) command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply access-list {ip | ipv6 | mac} <ACL-NAME> {in | out}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp state show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the show arp timeout command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp vrf show ipv6 neighbors show ipv6 neighbors state.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the show bfd command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bfd interface show hsc.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the bfd min-echo-receive-interval <INTERVAL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd min-echo-receive-interval <INTERVAL>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10040 AOS-CX 10.17.1000, what does the bfd min-receive-interval <INTERVAL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd min-receive-interval <INTERVAL>.", "reason": "ollama_invalid_json"}
