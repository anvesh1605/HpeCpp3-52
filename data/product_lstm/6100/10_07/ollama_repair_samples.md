# Ollama Repair Samples

## Report

- total_review_rows: 278
- rows_sent_to_ollama: 16
- rows_repaired: 0
- rows_rejected: 278
- rows_unrepairable: 275
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6100 AOS-CX 10.07, what does the show access-list control-plane command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list [ip|ipv6] [<ACL-NAME>] control-plane [vrf <VRF-NAME>].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what does the show running-config command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show running-config [<FEATURE>] [all].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what does the show needed-updates command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show needed-updates [next-boot [primary|secondary]].", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what does the show ntp associations command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ntp associations.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what does the show user-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show user-list.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what does the ssh public-key-algorithms command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-algorithms <PUBLIC-KEY-ALGORITHMS-LIST> no ssh public-key-algorithms.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what is the syntax of the ssh public-key-algorithms command?", "intent": "cli_syntax", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-algorithms <PUBLIC-KEY-ALGORITHMS-LIST>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what is the syntax of the ssh public-key-authentication command?", "intent": "cli_syntax", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.07, what does the ocsp url {primary | secondary} <URL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ocsp url {primary | secondary}.", "reason": "ollama_invalid_json"}
