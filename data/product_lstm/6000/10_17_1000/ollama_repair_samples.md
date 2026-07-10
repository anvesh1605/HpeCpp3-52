# Ollama Repair Samples

## Report

- total_review_rows: 143
- rows_sent_to_ollama: 137
- rows_repaired: 1
- rows_rejected: 142
- rows_unrepairable: 141
- rows_fixed_deterministically: 0

## Repaired Samples

- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the show ssh server command do?", "intent": "show_command_meaning", "slots": {"switch": "6000", "version": "10.17.1000", "command": "show ssh server"}, "target_value": "show ssh server [vrf default]."}

## Rejected Samples

- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the show access-list command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show access-list control-plane show access-list hitcounts show access-list hitcounts control-plane.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the access-list mac <ACL-NAME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no access-list mac <ACL-NAME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what is the syntax of the access-list mac <ACL-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no access-list mac <ACL-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the show arp command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show arp inspection interface show arp inspection statistics show arp inspection vlan show arp state show arp summary show arp timeout show arp vrf show ipv6 neighbors show ipv6 neighbors state show tech arp-security.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the show checkpoint <CHECKPOINT-NAME> command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show checkpoint <CHECKPOINT-NAME> hash show checkpoint post-configuration show checkpoint show checkpoint date show running-config hash show startup-config hash write memory.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the apply policy <POLICY-NAME> {in} [per-interface] command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> {in} [per-interface] Context config-vlan:.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what is the syntax of the apply policy <POLICY-NAME> {in} [per-interface] command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply policy <POLICY-NAME> {in} [per-interface] - apply policy <POLICY-NAME> in - no apply policy <POLICY-NAME> in", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the apply policy <POLICY-NAME> in command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no apply policy <POLICY-NAME> in.", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what is the syntax of the apply policy <POLICY-NAME> in command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply policy <POLICY-NAME> in", "reason": "ollama_invalid_json"}
- {"input_text": "For 6000 AOS-CX 10.17.1000, what does the show ip dns command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "Show FQDN Resolver Show IP DNS FQDN Resolver Detail Show IP DNS FQDN Resolver Refresh Interval.", "reason": "ollama_invalid_json"}
