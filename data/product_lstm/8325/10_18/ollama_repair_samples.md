# Ollama Repair Samples

## Report

- total_review_rows: 127
- rows_sent_to_ollama: 123
- rows_repaired: 0
- rows_rejected: 127
- rows_unrepairable: 127
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8325 AOS-CX 10.18, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the show resources command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show resources.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection interface show arp inspection statistics show arp inspection vlan show arp state show arp summary show arp timeout show arp vlan show arp vrf show ipv6 neighbors show ipv6 neighbors state show ipv6 neighbors vlan show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the show bfd command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bfd interface show hsc.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the bfd min-echo-receive-interval <INTERVAL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd min-echo-receive-interval <INTERVAL>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the bfd min-receive-interval <INTERVAL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd min-receive-interval <INTERVAL>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the show bgp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bgp [{vrf <VRF-NAME>|all-vrf}] [{ip 1v4 unicast|ipv6 unicast |all}] [vsx-peer][update-group [<INDEX>]] show bgp l2vpn evpn.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what does the show bgp l2vpn evpn command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bgp l2vpn evpn vni route-type show bgp l2vpn evpn vtep show bgp l2vpn evpn vtep route-type show bgp l2vpn evpn vtep vni show bgp l2vpn evpn vtep vni route-type show ip ospf routes show running-config bgp timers bgp transport vrf vrf.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.18, what is the syntax of the show bgp l2vpn evpn command?", "intent": "show_command_syntax", "review_reason": "syntax_long_explanation", "target_value": "The syntax of the show bgp l2vpn evpn command is: - show bgp l2vpn evpn vni route-type - show bgp l2vpn evpn vtep - show bgp l2vpn evpn vtep route-type - show bgp l2vpn evpn vtep vni.", "reason": "ollama_invalid_json"}
