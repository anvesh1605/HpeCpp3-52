# Ollama Repair Samples

## Report

- total_review_rows: 129
- rows_sent_to_ollama: 93
- rows_repaired: 0
- rows_rejected: 129
- rows_unrepairable: 129
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8360 AOS-CX 10.10, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what does the interface lag command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "interface lag <ID> no interface lag <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what does the show user command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show user <USERNAME> authorized-key.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what is the syntax of the show user command?", "intent": "show_command_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the show user command is: show user <USERNAME> authorized-key.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.10, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
