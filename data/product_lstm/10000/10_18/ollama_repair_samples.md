# Ollama Repair Samples

## Report

- total_review_rows: 287
- rows_sent_to_ollama: 261
- rows_repaired: 0
- rows_rejected: 287
- rows_unrepairable: 286
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 10000 AOS-CX 10.18, what does the access-list secure-update command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "access-list secure-update.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what does the apply access-list (to interface or LAG) command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply access-list {ip | ipv6 | mac} <ACL-NAME> {in | out}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection interface show arp inspection statistics show arp inspection vlan show arp state show arp summary show arp timeout show arp vlan show arp vrf show ipv6 neighbors show ipv6 neighbors state show ipv6 neighbors vlan show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what does the ip local-proxy-arp [uplink-passthrough] command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip local-proxy-arp [uplink-passthrough].", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what does the ip local-proxy-arp exclude {<ip-address>} command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip local-proxy-arp exclude {<ip-address>}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what is the syntax of the ip local-proxy-arp exclude {<ip-address>} command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip local-proxy-arp exclude {<ip-address>}", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.18, what does the IPv6 local-proxy-nd exclude {<IPv6-address>} command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 local-proxy-nd exclude {<ipv6-address>}.", "reason": "ollama_invalid_json"}
