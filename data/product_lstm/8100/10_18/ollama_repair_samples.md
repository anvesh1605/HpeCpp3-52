# Ollama Repair Samples

## Report

- total_review_rows: 142
- rows_sent_to_ollama: 136
- rows_repaired: 0
- rows_rejected: 142
- rows_unrepairable: 142
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8100 AOS-CX 10.18, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane show access-list secure-update show capacities show capacities-status show object-group.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the show resources command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show resources.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection interface show arp inspection statistics show arp inspection vlan show arp state.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the ip local-proxy-arp exclude {<ip-address>} command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip local-proxy-arp exclude {<ip-address>}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the IPv6 local-proxy-nd exclude {<IPv6-address>} command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 local-proxy-nd exclude {<ipv6-address>}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the show bfd command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bfd interface show hsc.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the bfd echo-src-ip-address <IPv4-ADDR> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd echo-src-ip-address <IPV4-ADDR>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the bfd min-echo-receive-interval <INTERVAL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd min-echo-receive-interval <INTERVAL>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.18, what does the show bgp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show bgp [{vrf <VRF-NAME>|all-vrf}] [{ip.", "reason": "ollama_invalid_json"}
