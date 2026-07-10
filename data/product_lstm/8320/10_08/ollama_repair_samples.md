# Ollama Repair Samples

## Report

- total_review_rows: 51
- rows_sent_to_ollama: 37
- rows_repaired: 0
- rows_rejected: 51
- rows_unrepairable: 51
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8320 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] command is: - no snmp-server host <IPv4-ADDR> trap version <VERSION> [community <STRING>] - snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] - no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what is the syntax of the snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>] command is: no snmp-server host <IPv4-ADDR> inform version v2c [community <STRING>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what does the show mvrp statistics command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show mvrp statistics [<PORT-LIST>] [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what does the show nae-agent command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show nae-agent [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8320 AOS-CX 10.08, what is the syntax of the ip prefix-list command?", "intent": "cli_syntax", "review_reason": "syntax_long_explanation", "target_value": "The syntax of the ip prefix-list command is: - ip prefix-list <PREFIX-LIST-NAME> [seq <SEQ>] <IP-PREFIX/MASK> [ge <0-32>] [le <0-32>] - no ip prefix-list <PREFIX-LIST-NAME> [seq <SEQ>] <IP-PREFIX/MASK> [ge <0-32>] [le <0-32>]", "reason": "ollama_invalid_json"}
