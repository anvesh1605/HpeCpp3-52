# Ollama Repair Samples

## Report

- total_review_rows: 155
- rows_sent_to_ollama: 111
- rows_repaired: 0
- rows_rejected: 155
- rows_unrepairable: 149
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the show access-list control-plane command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list [ip|ipv6] [<ACL-NAME>] control-plane [vrf <VRF-NAME>] [commands] [configuration] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what is Classifier policies?", "intent": "concept_explanation", "review_reason": "long_target_rows_moved_to_review", "target_value": "Classifier policies overview Classifier policies let a network administrator define sets of rules based on network traffic addressing or other header content, and use these rules to restrict or alter the passage of traffic through the switch. Choosing the rule criteria is called Classification, and one such rule, or list, is called a policy. Classification is achieved by creating a traffic class. The three types of classes (MAC, IPv4, and IPv6) are each focused on relevant frame/packet characteristics. Classes can be configured to match or ignore almost any frame or packet header field. Network traffic passing through a switch can be classified based on many different frame/packet characteristics including, but not limited to:.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the neighbor <IP-ADDR> activate command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no neighbor <IP-ADDR> activate.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the neighbor <IP-ADDRESS> orf-prefix-list <PREFIX-LIST-NAME> in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no neighbor <IP-ADDRESS> orf-prefix-list <PREFIX-LIST-NAME> in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the ip dns host <HOST-NAME> <IP-ADDR> [ vrf <VRF-NAME> ] command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip dns host <HOST-NAME> <IP-ADDR> [ vrf <VRF-NAME> ].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the IPv6 source-binding <VLAN-ID> <IPv6-ADDR> <MAC-ADDR> <IFNAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 source-binding <VLAN-ID> <IPV6-ADDR> <MAC-ADDR> <IFNAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the ip ospf <PROCESS-ID> area <AREA-ID> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip ospf <PROCESS-ID> area <AREA-ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.06, what does the IPv6 ospfv3 <PROCESS-ID> area <AREA-ID> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 ospfv3 <PROCESS-ID> area <area-id>.", "reason": "ollama_invalid_json"}
