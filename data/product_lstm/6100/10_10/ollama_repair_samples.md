# Ollama Repair Samples

## Report

- total_review_rows: 102
- rows_sent_to_ollama: 79
- rows_repaired: 0
- rows_rejected: 102
- rows_unrepairable: 102
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what does the ip dhcp command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| mac-group | grp03 | | | | | | | | --------- | ----- | --- | --- | --- | --- | --- | --- | ``` Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideforyourswitch model. | Command | History | | | | | | | | -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | | Release | | | | | Modification | | | | 10.07orearlier | | | | | -- | | | | Command | Information | | | | | | | | Platforms | Command | | context | | Authority | | | 6000 config-mac-group Administratorsorlocalusergroupmemberswithexecutionrights | 6100 | | | | | forthiscommand. | | | | -------------- | --------- | --------- | ---------------- | --- | --------------- | --- | --- | | port-access | | cdp-group | | | | | | | port-access | cdp-group | | <CDP-GROUP-NAME> | | | | | | no port-access | cdp-group | | <CDP-GROUP-NAME> | | | | |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the IPv6 source-binding command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 source-binding <VLAN-ID> <IPv6-ADDR> <MAC-ADDR> <IFNAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the ip irdp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip irdp", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what is the syntax of the aaa accounting all-mgmt command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa accounting all-mgmt <CONNECTION-TYPE>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.10, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
