# Ollama Repair Samples

## Report

- total_review_rows: 92
- rows_sent_to_ollama: 67
- rows_repaired: 0
- rows_rejected: 92
- rows_unrepairable: 92
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the vlan trunk native command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan trunk native tag voice.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the show track command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show track brief show vrrp shutdown timers advertise track (VRRP group) track (VRRP virtual router) track by version vrrp vrrp dual-active-forwarding.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the neighbor command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no neighbor.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the apply policy <POLICY-NAME> routed-in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> routed-in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the show client device-fingerprint command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show client device-fingerprint <MAC-ADDRESS>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the class gbp-mac command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| class gbp-mac | <CLASS-NAME> | | | | | | ------------- | ------------ | --- | --- | --- | --- | [<SEQUENCE-NUMBER>] | {match | | ignore} | | | | | | ------ | ---------------- | ---------- | --- | --- | --- | | {any | | <SRC-ROLE-NAME> | | default} | | | | | {any | | <DST-ROLE-NAME>} | | | | | {any | <SRC-ROLE-NAME> | default | infra | isl| internet | intranet} {any | aarp | appletalk | arp | fcoe | fcoe-init | ip | ipv6 | ipx-arpa | ipx-non- arpa |is-is | lldp | mpls-multicast | mpls-unicast | q-in-q | rbridge | trill |wake- | on-lan | | <NUMERIC-ETHERTYPE>} | | | | | | ------ | ---------------------- | --- | --- | --- | --- | [count] | [<SEQUENCE-NUMBER>] | comment | <TEXT-STRING> | | | | | ------------------- | ------- | ------------- | --- | --- | --- | class gbp-mac <CLASS-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT> Groupbasedpolicycommands|967.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the ip unnumbered <ifname> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip unnumbered <ifname>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the show IPv6 nd ra dns search-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ipv6 nd ra dns search-list [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.16, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
