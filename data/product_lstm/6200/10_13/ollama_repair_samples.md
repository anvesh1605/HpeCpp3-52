# Ollama Repair Samples

## Report

- total_review_rows: 141
- rows_sent_to_ollama: 91
- rows_repaired: 0
- rows_rejected: 141
- rows_unrepairable: 141
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the IPv6 helper-address unicast <UNICAST-IPv6-ADDR> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 helper-address unicast <UNICAST-IPv6-ADDR>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "Thefollowingmatchcriteriaisnotsupported.Ifthismatchcriteriaisattemptedtobeconfigured,anerror messagewillbedisplayedandtheactionwillnotbecompleted. | PCP on | MAC classes | | | | | | | ------ | ----------- | --- | --- | --- | --- | --- | apply policy (config-if, config-lag-if, config-if-vlan, config- vlan) | Context config-if, | config-lag-if: | | | | | | | ------------------ | -------------- | ------------------ | --- | --------------- | --- | --- | | apply policy | <POLICY-NAME> | {in|out|routed-in} | | [per-interface] | | | no apply policy <POLICY-NAME> {in|out|routed-in} [per-interface] | Context config-vlan: | | | | | | | | ----------------------- | ------------- | --------- | --- | --- | --- | --- | | apply policy | <POLICY-NAME> | {in|out} | | | | | | no apply policy | <POLICY-NAME> | {in|out} | | | | | | Context config-if-vlan: | | | | | | | | apply policy | <POLICY-NAME> | routed-in | | | | | | no apply policy | <POLICY-NAME> | routed-in | | | | |.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the vlan <ID> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vlan <ID>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what does the https-server vrf <VRF-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no https-server vrf <VRF-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the https-server vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no https-server vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 6200 AOS-CX 10.13, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
