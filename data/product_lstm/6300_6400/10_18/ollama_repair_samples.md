# Ollama Repair Samples

## Report

- total_review_rows: 182
- rows_sent_to_ollama: 173
- rows_repaired: 0
- rows_rejected: 182
- rows_unrepairable: 182
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the access-list secure-update command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "access-list secure-update no access list secure-update.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the apply access-list (to interface or LAG) command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply access-list {ip | ipv6 | mac} <ACL-NAME> {in | out}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the apply access-list (to L3 VNI) command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "apply access-list (to VLAN) clear access-list hitcounts clear access-list hitcounts control-plane object-group address resequence object-group address reset object-group all reset object-group ip address object-group ipv6 address object-group port object-group port resequence object-group port reset show access-list show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection interface show arp inspection statistics show arp inspection vlan show arp state show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the ip local-proxy-arp exclude {<ip-address>} command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip local-proxy-arp exclude {<ip-address>}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the IPv6 local-proxy-nd exclude {<IPv6-address>} command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 local-proxy-nd exclude {<ipv6-address>}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the show arp inspection interface command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection statistics show arp inspection vlan show arp state show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.18, what does the show arp inspection statistics command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection vlan show arp state show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state show tech arp-security.", "reason": "ollama_invalid_json"}
