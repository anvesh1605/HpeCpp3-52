# Ollama Repair Samples

## Report

- total_review_rows: 101
- rows_sent_to_ollama: 84
- rows_repaired: 0
- rows_rejected: 101
- rows_unrepairable: 101
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what does the ip dhcp command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| mac-group | grp03 | | | | | | | | --------- | ----- | --- | --- | --- | --- | --- | --- | ``` Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideforyourswitch model. | Command | History | | | | | | | | -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | | Release | | | | | Modification | | | | 10.07orearlier | | | | | -- | | | | Command | Information | | | | | | | | Platforms | Command | | context | | Authority | | | 6000 config-mac-group Administratorsorlocalusergroupmemberswithexecutionrights | 6100 | | | | | forthiscommand. | | | | -------------- | --------- | --------- | ---------------- | --- | --------------- | --- | --- | | port-access | | cdp-group | | | | | | | port-access | cdp-group | | <CDP-GROUP-NAME> | | | | | | no port-access | cdp-group | | <CDP-GROUP-NAME> | | | | |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the IPv6 source-binding command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 source-binding <VLAN-ID> <IPv6-ADDR> <MAC-ADDR> <IFNAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the ip irdp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip irdp", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what does the no routing command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| vlan trunk | native 1 | | | | ---------- | ------------- | --- | --- | | vlan trunk | allowed 10-12 | | | | lacp mode | active | | | exit | interface | lag 11 multi-chassis | | | | --------- | -------------------- | --- | --- | no shutdown no routing | vlan trunk | native 1 | | | | ---------- | ------------------ | --- | --- | | vlan trunk | allowed 10-12,2001 | | | | lacp mode | active | | | exit | interface | lag 256 | | | | ----------- | ------- | --- | --- | | description | VSX_ISL | | | no shutdown no routing | vlan trunk | native 1 | tag | | | ---------- | ----------- | --- | --- | | vlan trunk | allowed all | | | | lacp mode | active | | | exit Displayingtherunningconfigurationforinterfacelagwithlacp fallback-staticconfigured. | switch# show | running-config | interface | lag | | ------------ | -------------- | --------- | --- | | interface | lag 1 | | | no shutdown no routing | vlan trunk | native 1 | | | | -------------------- | ----------- | --- | --- | | vlan trunk | allowed all | | | | lacp mode | active | | | | lacp fallback-static | | | | shutdown shutdown no shutdown.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6100 AOS-CX 10.12, what is the syntax of the no routing command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no routing", "reason": "ollama_invalid_json"}
