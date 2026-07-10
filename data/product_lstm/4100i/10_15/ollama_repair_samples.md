# Ollama Repair Samples

## Report

- total_review_rows: 93
- rows_sent_to_ollama: 78
- rows_repaired: 0
- rows_rejected: 93
- rows_unrepairable: 93
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 4100i AOS-CX 10.15, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the aaa authentication port-access captive-portal-profile <PROFILE-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no aaa authentication port-access captive-portal-profile <PROFILE-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the apply copp-policy command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply copp-policy <NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what does the ip dhcp command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| mac-group grp01 | | | | | | --------------- | -------- | ----------------- | --- | --- | | seq 10 ignore | mac | b2:c3:44:12:78:11 | | | | seq 30 ignore | mac-mask | 71:14:89:f3/32 | | | ``` Removingtherulethatmatchesthesequencenumber25fromtheMACgroupnamedgrp01. | switch(config)# | mac-group | grp01 | | | | ------------------------- | --------- | --------- | ------ | --- | | switch(config-mac-group)# | | no ignore | seq 25 | | Formoreinformationonfeaturesthatusethiscommand,refertotheFundamentalsGuideforyourswitch model. Command History | Release | | | Modification | | | -------------- | --- | --- | ------------ | --- | | 10.07orearlier | | | -- | | Command Information Deviceprofilecommands|347.", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the IPv6 helper-address unicast <UNICAST-IPv6-ADDR> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 helper-address unicast <UNICAST-IPv6-ADDR>", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the ip icmp redirect command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp redirect", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the ip icmp unreachable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip icmp unreachable", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the ip igmp querier command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp querier", "reason": "ollama_invalid_json"}
- {"input_text": "For 4100i AOS-CX 10.15, what is the syntax of the no ip igmp command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip igmp", "reason": "ollama_invalid_json"}
