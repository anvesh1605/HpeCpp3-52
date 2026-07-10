# Ollama Repair Samples

## Report

- total_review_rows: 104
- rows_sent_to_ollama: 78
- rows_repaired: 0
- rows_rejected: 104
- rows_unrepairable: 104
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 9300 AOS-CX 10.12, what does the show user-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show user-list management-interface.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what does the bfd min-transmit-interval <INTERVAL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd min-transmit-interval <INTERVAL>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what does the vsx-sync command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "-! | - 10 | permit any | any any | | | ---- | ---------- | ------- | --- | Formoreinformationonfeaturesthatusethiscommand,refertotheVirtualSwitchingExtension(VSX)Guidefor yourswitchmodel. | Command History | | | | | ------------------- | ------- | ------- | ------------ | | Release | | | Modification | | 10.07orearlier | | | -- | | Command Information | | | | | Platforms | Command | context | Authority | 9300 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith executionrightsforthiscommand.Operatorscanexecutethis (#) commandfromtheoperatorcontext(>)only. | show vsx | active-forwarding | | | | -------- | ----------------- | --- | --- | show vsx active-forwarding [interface <INTERFACE-VLAN>] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what does the no routing command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan access 1 exit.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.12, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
