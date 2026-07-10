# Ollama Repair Samples

## Report

- total_review_rows: 86
- rows_sent_to_ollama: 61
- rows_repaired: 0
- rows_rejected: 86
- rows_unrepairable: 86
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8100 AOS-CX 10.16, what does the show user-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show user-list management-interface.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the apply policy <POLICY-NAME> routed-in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> routed-in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the class gbp-mac command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| class gbp-mac | <CLASS-NAME> | | | | | ------------- | ------------ | --- | --- | --- | [<SEQUENCE-NUMBER>] | {match | | ignore} | | | | | ------ | ---------------- | ---------- | --- | --- | | {any | | <SRC-ROLE-NAME> | | default} | | | | {any | | <DST-ROLE-NAME>} | | | | {any | <SRC-ROLE-NAME> | default | infra | isl| internet | intranet} {any | aarp | appletalk | arp | fcoe | fcoe-init | ip | ipv6 | ipx-arpa | ipx-non- arpa |is-is | lldp | mpls-multicast | mpls-unicast | q-in-q | rbridge | trill |wake- | on-lan | | <NUMERIC-ETHERTYPE>} | | | | | ------ | ---------------------- | --- | --- | --- | [count] | [<SEQUENCE-NUMBER>] | comment | <TEXT-STRING> | | | | ------------------- | ------- | ------------- | --- | --- | class gbp-mac <CLASS-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT> AOS-CX10.16Command-LineInterfaceGuide|(8100,8360SwitchSeries) 847.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the show ip igmp snooping command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ip igmp snooping.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the show IPv6 nd ra dns server command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ipv6 nd ra dns server [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the interface lag command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "interface lag <ID> no interface lag <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8100 AOS-CX 10.16, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
