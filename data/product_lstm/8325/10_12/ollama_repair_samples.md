# Ollama Repair Samples

## Report

- total_review_rows: 111
- rows_sent_to_ollama: 79
- rows_repaired: 0
- rows_rejected: 111
- rows_unrepairable: 111
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8325 AOS-CX 10.12, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what does the no routing command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan access 1 exit.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what does the show mirror command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show mirror [<SESSION-ID>] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what does the apply qos [queue-profile <QUEUE-NAME>] schedule-profile <SCHEDULE-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply qos [queue-profile <QUEUE-NAME>] schedule-profile <SCHEDULE-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.12, what is the syntax of the ip prefix-list command?", "intent": "cli_syntax", "review_reason": "syntax_long_explanation", "target_value": "The syntax of the ip prefix-list command is: - ip prefix-list <PREFIX-LIST-NAME> [seq <SEQ>] <IP-PREFIX/MASK> [ge <0-32>] [le <0-32>] - no ip prefix-list <PREFIX-LIST-NAME> [seq <SEQ>] <IP-PREFIX/MASK> [ge <0-32>] [le <0-32>]", "reason": "ollama_invalid_json"}
