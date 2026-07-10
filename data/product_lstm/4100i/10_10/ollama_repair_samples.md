# Ollama Repair Samples

## Report

- total_review_rows: 115
- rows_sent_to_ollama: 90
- rows_repaired: 0
- rows_rejected: 115
- rows_unrepairable: 115
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the no shutdown command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no shutdown", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what does the ip dhcp command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| mac-group | grp03 | | | | | | | | --------- | ----- | --- | --- | --- | --- | --- | --- | ``` Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideforyourswitch model. | Command | History | | | | | | | | -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | | Release | | | | | Modification | | | | 10.07orearlier | | | | | -- | | | | Command | Information | | | | | | | | Platforms | Command | | context | | Authority | | | config-mac-group | 4100i | | | | | Administratorsorlocalusergroupmemberswithexecution | | | | ----- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | rightsforthiscommand. | port-access | | cdp-group | | | | | | | -------------- | --------- | --------- | ---------------- | --- | --- | --- | --- | | port-access | cdp-group | | <CDP-GROUP-NAME> | | | | | | no port-access | cdp-group | | <CDP-GROUP-NAME> | | | | |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the IPv6 source-binding command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 source-binding <VLAN-ID> <IPv6-ADDR> <MAC-ADDR> <IFNAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what is the syntax of the ip irdp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip irdp", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.10, what does the interface lag command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "interface lag <ID> no interface lag <ID>.", "reason": "ollama_invalid_json"}
