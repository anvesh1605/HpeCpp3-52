# Ollama Repair Samples

## Report

- total_review_rows: 109
- rows_sent_to_ollama: 87
- rows_repaired: 0
- rows_rejected: 109
- rows_unrepairable: 109
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the no shutdown command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no shutdown", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what does the policy command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "policy <POLICY-NAME> [<SEQUENCE-NUMBER>] | class | {ip|ipv6|mac} | | | <CLASS-NAME> | | | | | | | ----- | ------------------ | ----------------- | --- | ------------ | ---------------- | ---------------- | --- | ------------------- | ------------------ | | | action | {<REMARK-ACTIONS> | | | | | <POLICE-ACTIONS> | | | | <OTHER-ACTIONS>} | | | [{<REMARK-ACTIONS> | | | | | <POLICE-ACTIONS> | | | | <OTHER-ACTIONS>}] | | [<SEQUENCE-NUMBER>] | comment | |... | | | | | | | | | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | AOS-CX10.09Command-LineInterfaceGuide| | | | | (6300,6400SwitchSeries) | | | | | | | -------------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what does the show client device-fingerprint command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show client device-fingerprint <MAC-ADDRESS>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the ip igmp version <VERSION> strict command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp version <VERSION> strict", "reason": "ollama_invalid_json"}
- {"input_text": "For 6300_6400 AOS-CX 10.09, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
