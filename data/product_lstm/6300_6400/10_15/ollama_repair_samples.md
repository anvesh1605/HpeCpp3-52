# Ollama Repair Samples

## Report

- total_review_rows: 108
- rows_sent_to_ollama: 79
- rows_repaired: 0
- rows_rejected: 108
- rows_unrepairable: 108
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the vlan trunk native command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan trunk native tag voice.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the show track command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show track brief show vrrp shutdown timers advertise track (VRRP group) track (VRRP virtual router) track by version vrrp vrrp dual-active-forwarding.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the apply policy <POLICY-NAME> routed-in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> routed-in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the show client device-fingerprint command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show client device-fingerprint <MAC-ADDRESS>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the show IPv6 nd ra dns server command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ipv6 nd ra dns server [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the no routing command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan access 1 exit.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.15, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
