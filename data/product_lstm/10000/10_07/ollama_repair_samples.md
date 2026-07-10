# Ollama Repair Samples

## Report

- total_review_rows: 64
- rows_sent_to_ollama: 40
- rows_repaired: 0
- rows_rejected: 64
- rows_unrepairable: 64
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the bfd enable command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "bfd enable", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the clear bfd statistics command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "clear bfd | statistics | [session | <ID>]", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the ip ospf bfd command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "ip ospf | bfd", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the neighbor fall-over bfd command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "neighbor | {<IP-ADDRESS>|<PEER-GROUP-NAME>} | | | | fall-over | | bfd", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the show bfd command?", "intent": "show_command_syntax", "review_reason": "markdown_repair_failed", "target_value": "show bfd | [session | <ID>] | [all-vrfs | | vrf | <NAME>] | [vsx-peer]", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the show bfd interface command?", "intent": "show_command_syntax", "review_reason": "markdown_repair_failed", "target_value": "show bfd interface | | <NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the erps ring <ringid> <port0 port1> interface command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "erps ring <ringid>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the erps ring <ringid> description command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "erps ring | <ringid>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the erps ring <ringid> guard-interval command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "erps ring | <ringid>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.07, what is the syntax of the erps ring <ringid> instance <id> control-vlan command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "erps | ring <ringid>", "reason": "ollama_invalid_json"}
