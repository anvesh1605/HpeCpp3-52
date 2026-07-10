# Ollama Repair Samples

## Report

- total_review_rows: 70
- rows_sent_to_ollama: 53
- rows_repaired: 0
- rows_rejected: 70
- rows_unrepairable: 70
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8360 AOS-CX 10.09, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what does the show mvrp statistics command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show mvrp statistics [<PORT-LIST>] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what does the show nae-agent command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show nae-agent [<AGENT-NAME>] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what does the show IPv6 mroute <GROUP-ADDR> command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ipv6 mroute <GROUP-ADDR> [<SOURCE-ADDR>].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what does the crypto pki application <APP-NAME> certificate <CERT-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no crypto pki application <APP-NAME> certificate <CERT-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8360 AOS-CX 10.09, what does the show crypto pki ta-profile command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show crypto pki ta-profile [<TA-NAME>].", "reason": "ollama_invalid_json"}
