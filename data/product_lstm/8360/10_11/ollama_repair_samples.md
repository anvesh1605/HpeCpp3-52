# Ollama Repair Samples

## Report

- total_review_rows: 97
- rows_sent_to_ollama: 69
- rows_repaired: 0
- rows_rejected: 97
- rows_unrepairable: 97
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8360 AOS-CX 10.11, what is VLAN: 1?", "intent": "concept_explanation", "review_reason": "long_target_rows_moved_to_review", "target_value": "35 permit 0xffee any aabb.cc11.1234 40 deny any any any | | Hit-counts: | enabled | | | | --- | ----------- | ------- | --- | --- | ReplacinganACEinanexistingMACACL: | switch(config)# | access-list | mac | MY_MAC_ACL | | | ---------------------- | ----------- | ----------- | ------------------ | ------ | | switch(config-acl-ip)# | | 35 permit | any aabb.cc11.1234 | 0xeeee | | switch(config-acl-ip)# | | exit | | | | switch(config)# | do show | access-list | | | | Type | Name | | | | | Sequence | Comment | | | | Action EtherType | | Source MAC | Address | | | | --- | ----------- | ----------- | --- | --- | | | Destination | MAC Address | | | | | Additional | Parameters | | | ------------------------------------------------------------------------------- | MAC | MY_MAC_ACL | | | | | --- | ---------- | --- | --- | --- | 10 permit ipv6 1122.3344.5566/ffff.ffff.0000 any 20 permit any aaaa.bbbb.cccc 1111.2222.3333 | | QoS Priority | Code Point: | 4 | | | --- | ------------ | ----------- | --- | --- | 30 permit appletalk any any VLAN: 1 35 permit 0xeeee AOS-CX10.11ACLsandClassifierPoliciesGuide| (6300,6400,8360SwitchSeries).", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what does the show user-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show user-list management-interface.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what does the apply policy <POLICY-NAME> routed-in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> routed-in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.11, what does the show mirror command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show mirror [<SESSION-ID>] [vsx-peer].", "reason": "ollama_invalid_json"}
