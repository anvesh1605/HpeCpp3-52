# Ollama Repair Samples

## Report

- total_review_rows: 115
- rows_sent_to_ollama: 63
- rows_repaired: 0
- rows_rejected: 115
- rows_unrepairable: 115
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 9300 AOS-CX 10.13, what does the show user-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show user-list management-interface.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what does the interface lag command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "interface lag <ID> no interface lag <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh public-key-authentication command is: - ssh public-key-authentication - no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 9300 AOS-CX 10.13, what does the show mirror command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show mirror [<SESSION-ID>] [vsx-peer].", "reason": "ollama_invalid_json"}
