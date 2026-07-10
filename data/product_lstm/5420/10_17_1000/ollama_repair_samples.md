# Ollama Repair Samples

## Report

- total_review_rows: 172
- rows_sent_to_ollama: 162
- rows_repaired: 0
- rows_rejected: 172
- rows_unrepairable: 171
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the access-list secure-update command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "access-list secure-update no access list secure-update.", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the apply access-list control-plane command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "| | Public | | | ACL application | 75 | | --- | ------ | --- | --- | --------------- | --- |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the apply access-list (to interface or LAG) command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply access-list {ip | ipv6 | mac} <ACL-NAME> {in | out}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME> - access-list mac 116", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection interface show arp inspection statistics show arp inspection vlan show arp state show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the show bgp l2vpn evpn command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bgp l2vpn evpn <ROUTE-TYPE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what is the syntax of the show bgp l2vpn evpn command?", "intent": "show_command_syntax", "review_reason": "syntax_long_explanation", "target_value": "show bgp l2vpn evpn vni route-type - show bgp l2vpn evpn vtep - show bgp l2vpn evpn vtep route-type - show bgp l2vpn evpn vtep vni", "reason": "ollama_invalid_json"}
- {"input_text": "For 5420 AOS-CX 10.17.1000, what does the show bgp l2vpn evpn vtep command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bgp l2vpn evpn vtep <IP-address>.", "reason": "ollama_invalid_json"}
