# Ollama Repair Samples

## Report

- total_review_rows: 93
- rows_sent_to_ollama: 63
- rows_repaired: 0
- rows_rejected: 93
- rows_unrepairable: 93
- rows_fixed_deterministically: 0

## Repaired Samples


## Rejected Samples

- {"input_text": "For 8325 AOS-CX 10.16, what does the bfd min-transmit-interval <INTERVAL> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no bfd min-transmit-interval <INTERVAL>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the neighbor command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no neighbor.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the VRF : default command do?", "intent": "cli_meaning", "review_reason": "long_target_rows_moved_to_review", "target_value": "| BGP Neighbor | | 1920:1680:1:1::8 | | (Internal) | | | | | | | | ------------------- | ---------- | ---------------- | ------------- | ----------- | ----- | ------------- | ---------- | ---------- | ------------- | --- | | Description | | |: RR | peer-group^ | | | | | | | | Peer-group | | |: RRv6 | | | | | | | | | Remote | Router | Id |: 192.168.1.8 | | | Local | Router | Id |: 192.168.1.1 | | | Remote | AS | |: 65001 | | | Local | AS | |: 65001 | | | Remote | Port | |: 42423 | | | Local | Port | |: 179 | | | State | | |: Established | | | Admin | Status | |: Up | | | Conn. Established | | |: 5 | | | Conn. | Dropped | |: 4 | | | Passive | | |: No | | | Update-Source | | |: loopback0^ | | | Cfg. Hold | Time | |: 180 | | | Cfg. | Keep | Alive |: 60 | | | Neg. Hold | Time | |: 180 | | | Neg. | Keep | Alive |: 60 | | | Up/Down | Time | |: 06h:46m:13s | | | Connect-Retry | | Time |: 120 | | | Local-AS | Prepend | |: No | | | Alt. | Local-AS | |: 0 | | | BFD | | |: Disabled | | | Slow | Peer | |: Yes | | | Password | | |: | | | | | | | | | Last Err | Sent | |: No | Error | | | | | | | | Last SubErr | Sent | |: No | Error | | | | | | | | Last Err | Rcvd | |: No | Error | | | | | | | | Last SubErr | Rcvd | |: No | Error | | | | | | | | Graceful-Restart | | |: Enabled | | | Gr. | Restart | Time |: 120 | | | Gr. Stalepath | | Time |: 300 | | | Remove | | Private-AS |: No | | | TTL | | |: 255 | | | Local | Cluster-ID | |: | | | Weight | | |: 0 | | | Fall-over | | |: No | | | Confederation-Peers | | |: No | | | | | | | | | Message | statistics | | | Sent | Rcvd | | | | | | | ------------------- | | | | ----- | ----- | | | | | | | Open | | | | 8 | | 7 | | | | | | Notification | | | | 3 | | 1 | | | | | | Updates | | | | 20730 | 91332 | | | | | | | Keepalives | | | | 1153 | 952 | | | | | | | Route Refresh | | | | 0 | | 0 | | | | | | Total | | | | 21894 | 92292 | | | | | | BGPcommands|330.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the vlan command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID> no vlan <ID>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the vlan <ID-RANGE> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "vlan <ID-RANGE> no vlan <ID-RANGE>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the ip unnumbered <ifname> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no ip unnumbered <ifname>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the show IPv6 nd ra dns server command do?", "intent": "show_command_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "show ipv6 nd ra dns server [vsx-peer].", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME> command do?", "intent": "cli_meaning", "review_reason": "meaning_is_only_syntax", "target_value": "no aaa authentication limit-login-attempts <ATTEMPTS> lockout-time <LOCKOUT-TIME>.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what is the syntax of the ssh password-authentication command?", "intent": "cli_syntax", "review_reason": "markdown_repair_failed", "target_value": "The syntax of the ssh password-authentication command is: - ssh password-authentication - no ssh password-authentication.", "reason": "ollama_invalid_json"}
- {"input_text": "For 8325 AOS-CX 10.16, what does the ssh public-key-authentication command do?", "intent": "cli_meaning", "review_reason": "generic_targets_moved_to_review", "target_value": "ssh public-key-authentication no ssh public-key-authentication.", "reason": "ollama_invalid_json"}
