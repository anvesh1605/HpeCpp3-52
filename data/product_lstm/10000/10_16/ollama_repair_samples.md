# Ollama Repair Samples

## Report

- total_review_rows: 122
- rows_sent_to_ollama: 92
- rows_repaired: 0
- rows_rejected: 122
- rows_unrepairable: 122
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 10000 AOS-CX 10.16, what does the neighbor command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no neighbor.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what is the syntax of the neighbor command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no neighbor", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what does the VRF : default command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| BGP Neighbor | 10.1.1.2 | | (Internal) | | | | | | | | ------------------- | ---------- | ---- | ------------- | ----- | ----------- | ---------------- | ---------- | ---------- | ---------- | | Description | | |: | | | | | | | | Peer-group | | |: | | | | | | | | Remote | Router | Id |: 10.1.1.2 | | | Local Router | | Id |: 10.1.1.1 | | Remote | AS | |: 1 | | | Local AS | | |: 1 | | Remote | Port | |: 179 | | | Local Port | | |: 56008 | | State | | |: Established | | | Admin Status | | |: Up | | Conn. Established | | |: 1 | | | Conn. Dropped | | |: 0 | | Passive | | |: No | | | Update-Source | | |: | | Cfg. Hold | Time | |: 180 | | | Cfg. Keep | Alive | |: 60 | | Neg. Hold | Time | |: 180 | | | Neg. Keep | Alive | |: 60 | | Up/Down | Time | |: 00m:01w:03d | | | Alt. Local-AS | | |: 0 | | Local-AS | Prepend | |: No | | | | | | | | BFD | | |: Disabled | | | | | | | | Password | | |: | | | | | | | | Last Err | Sent | |: No | Error | | | | | | | Last SubErr | | Sent |: No | Error | | | | | | | Last Err | Rcvd | |: No | Error | | | | | | | Last SubErr | | Rcvd |: No | Error | | | | | | | Graceful-Restart | | |: Enabled | | | Gr. Restart | | Time |: 120 | | Gr. Stalepath | | Time |: 150 | | | Remove | Private-AS | |: No | | TTL | | |: 255 | | | Local Cluster-ID | | |: | | Weight | | |: 0 | | | Fall-over | | |: No | | Message | statistics | | | Sent | Rcvd | | | | | | ------------------- | | | | ----- | ----- | | | | | | Open | | | | 1 | 1 | | | | | | Notification | | | | 0 | 0 | | | | | | Updates | | | | 3 | 2 | | | | | | Keepalives | | | | 17995 | 18009 | | | | | | Route Refresh | | | | 0 | 0 | | | | | | Total | | | | 17999 | 18012 | | | | | | Capability | | | | | Advertised | | | Received | | | ----------- | | | | | ----------- | | | ---------- | | | Route Refresh | | | | | Yes | | | Yes | | | Graceful | Restart | | | | Yes | | | Yes | | | Four Octet | ASN | | | | Yes | | | Yes | | | Address | family | IPv4 | Unicast | | Yes | | | Yes | | BGPcommands|346.", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what is the syntax of the vrf <VRF-NAME> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no vrf <VRF-NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what is the syntax of the no ip pim-bidir command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no ip pim-bidir", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what is the syntax of the no routing command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no routing", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what is the syntax of the apply copp-policy command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no apply copp-policy <NAME>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what is the syntax of the IPv6 helper-address unicast <UNICAST-IPv6-ADDR> command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "no IPv6 helper-address unicast <UNICAST-IPv6-ADDR>", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what is the syntax of the No IPv6 VRF redirect configured to this Distributed Services module command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "No IPv6 VRF redirect configured to this Distributed Services module", "reason": "ollama_invalid_json"}
- {"input_text": "For 10000 AOS-CX 10.16, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
