# Ollama Repair Samples

## Report

- total_review_rows: 102
- rows_sent_to_ollama: 73
- rows_repaired: 0
- rows_rejected: 102
- rows_unrepairable: 102
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8400 AOS-CX 10.12, what does the ip dhcp command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| SVOS> ip | show | | | | ------------ | ------------- | --- | --- | | Interface |: Link | Up | | | IP Address |: 10.0.26.17 | | | | Subnet Mask: | 255.255.252.0 | | | | Gateway |: 10.0.24.1 | | | | SVOS> ip | disable | | | | SVOS> ip | show | | | | Interface |: Disabled | | | SVOS> Formoreinformationonfeaturesthatusethiscommand,refertotheDiagnosticsandSupportabilityGuidefor yourswitchmodel. | Command History | | | | | ------------------- | ------- | ------- | ------------ | | Release | | | Modification | | 10.07orearlier | | | -- | | Command Information | | | | | Platforms | Command | context | Authority | 8400 ServiceOS(SVOS>) Administratorsorlocalusergroupmemberswithexecutionrights forthiscommand. ls | ls [<OPTIONS>] | [<FILE-NME>] | | | | -------------- | ------------ | --- | --- |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what does the no routing command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan access 1 exit.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what does the apply qos [queue-profile <QUEUE-NAME>] schedule-profile <SCHEDULE-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply qos [queue-profile <QUEUE-NAME>] schedule-profile <SCHEDULE-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what is the syntax of the ip prefix-list command?", "intent": "cli_syntax", "review_reason": "syntax_long_explanation", "target_value": "The syntax of the ip prefix-list command is: - ip prefix-list <PREFIX-LIST-NAME> [seq <SEQ>] <IP-PREFIX/MASK> [ge <0-32>] [le <0-32>] - no ip prefix-list <PREFIX-LIST-NAME> [seq <SEQ>] <IP-PREFIX/MASK> [ge <0-32>] [le <0-32>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 8400 AOS-CX 10.12, what is the syntax of the snmp-server view <VIEWNAME> <OID_TREE> [<MASK>] <included/excluded> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the snmp-server view <VIEWNAME> <OID_TREE> [<MASK>] <included/excluded> command is: no snmp-server view <VIEWNAME> <OID_TREE> [<MASK>] <included/excluded>", "reason": "ollama_invalid_json"}
