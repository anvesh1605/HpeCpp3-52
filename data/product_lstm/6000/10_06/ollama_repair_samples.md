# Ollama Repair Samples

## Report

- total_review_rows: 111
- rows_sent_to_ollama: 87
- rows_repaired: 0
- rows_rejected: 111
- rows_unrepairable: 108
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 6000 AOS-CX 10.06, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the apply policy <POLICY-NAME> {in} command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> {in}.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the IPv6 source-binding <VLAN-ID> <IPv6-ADDR> <MAC-ADDR> <IFNAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 source-binding <VLAN-ID> <IPV6-ADDR> <MAC-ADDR> <IFNAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the ip ospf <PROCESS-ID> area <AREA-ID> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip ospf <PROCESS-ID> area <AREA-ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the IPv6 ospfv3 <PROCESS-ID> area <AREA-ID> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ipv6 ospfv3 <PROCESS-ID> area <area-id>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the crypto pki certificate <CERT-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no crypto pki certificate <CERT-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the aaa authentication port-access dot1x authenticator cached-reauth command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication port-access dot1x authenticator cached-reauth.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the aaa authentication port-access dot1x authenticator reauth command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication port-access dot1x authenticator reauth.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.06, what does the aaa authentication port-access mac-auth cached-reauth command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication port-access mac-auth cached-reauth.", "reason": "ollama_invalid_json"}
