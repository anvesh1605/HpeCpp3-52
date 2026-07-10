# Ollama Repair Samples

## Report

- total_review_rows: 69
- rows_sent_to_ollama: 53
- rows_repaired: 0
- rows_rejected: 69
- rows_unrepairable: 69
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8325 AOS-CX 10.09, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what does the show mvrp statistics command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show mvrp statistics [<PORT-LIST>] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what does the show nae-agent command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show nae-agent [<AGENT-NAME>] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what does the router pim command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| switch(config-pim)# | | register-rate-limit | | 10 | | | ------------------- | --- | ---------------------- | --- | --- | --- | | switch(config-pim)# | | no register-rate-limit | | | | Configuringandremovingcandidate-RProuterpriorityandholdtimes | switch(config)# | | router pim | | | | | ------------------- | ----------- | ------------ | ------------ | --- | --- | | switch(config-pim)# | | rp-candidate | priority | 250 | | | switch(config-pim)# | | rp-candidate | hold-time | 200 | | | Command | History | | | | | | Release | | | Modification | | | | 10.07orearlier | | | -- | | | | Command | Information | | | | | | Platforms | Command | context | Authority | | | 8320 config Administratorsorlocalusergroupmemberswithexecutionrights | 8325 | | | forthiscommand. | | | | ---- | --- | --- | --------------- | --- | --- | rp-address | rp-address | <IP-ADDR> | [<GRP-ADDR/GRP-MASK>] | | [override] | | | ------------- | --------- | --------------------- | --- | ---------- | --- | | no rp-address | <IP-ADDR> | [<GRP-ADDR/GRP-MASK>] | | [override] | |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.09, what does the show IPv6 mroute <GROUP-ADDR> command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ipv6 mroute <GROUP-ADDR> [<SOURCE-ADDR>].", "reason": "ollama_invalid_json"}
