# Inference Demo Cases

| ID | Type | Question | Expected Answer | Status |
| --- | --- | --- | --- | --- |
| 1 | product_concept | For 10000 AOS-CX 10.07, what does the guide say about High Availability Overview? | High Availability is based on redundant management, OVSDB synchronization, and filesystem replication. The goals are five-nines availability, fault tolerance, and minimal-disruption hardware replacement. | good |
| 2 | product_concept | For 10000 AOS-CX 10.07, what does the guide say about Management Module Failover Overview? | There are two failover types: controlled failover, triggered by rebooting the Active MM or running redundancy switchover, and uncontrolled failover, triggered by events such as an Active MM crash or hot removal. The Standby MM can detect failover by mailbox interrupt, hot-removal detection, or heartbeat loss. | good |
| 3 | product_concept | For 10000 AOS-CX 10.07, explain how BFD operates. | BFD is a fast failure-detection mechanism that creates a session between two devices, sends control packets, and marks the session down if packets stop arriving. It supports asynchronous mode, demand mode, and echo-based detection. | good |
| 4 | product_command | For 10000 AOS-CX 10.07, what does the redundancy switchover command do? | It immediately switches the system over to the Standby Management Module. It must be run from the Active Management Module and fails if the Standby Management Module is unavailable or in a failed state. | good |
| 5 | cli_syntax | For 10040 AOS-CX 10.17.1000, what is the syntax of the redundancy switchover command? | `redundancy switchover` | good |
| 6 | product_procedure | For 8400 AOS-CX 10.17.1000, what is Step 3: Configuring local proxy ARP in switch A? | If local proxy ARP is enabled in the L3 gateway, the gateway responds to ARP requests for addresses in the same subnet. In other words, it acts as the proxy for ARP resolution. | good |
| 7 | release_caveat | For 4100i AOS-CX 10.13.1170, what caveat is documented for IP-SLA? | Use unique ports for each service. Reusing ports that belong to other applications or services can cause unexpected behavior. | good |
| 8 | release_caveat | For 4100i AOS-CX 10.16.1030, what caveat is documented for Central? | If the switch can connect to Aruba Central but is not registered or lacks a valid license, it can repeatedly disconnect and reconnect. Disable Aruba Central until registration or licensing is fixed. | good |
| 9 | release_caveat | For 4100i AOS-CX 10.13.1120, what caveat is documented for REST? | REST supports the admin and operator roles, but it does not work with TACACS+ command authorization. | good |
| 10 | release_caveat | For 4100i AOS-CX 10.13.1150, what caveat is documented for Certificates? | Legacy certificate names with unsupported characters will migrate during upgrade, but those certificates can no longer be edited. New certificate names must use only letters, numbers, dots, dashes, and underscores. | good |
| 11 | release_caveat | For 4100i AOS-CX 10.17.1010, what caveat is documented for Classifiers? | Policies containing both MAC and IPv6 classes are not allowed. | good |
| 12 | data_not_available | For 5420 AOS-CX 10.17.1010, what caveat is documented for Multicast? | This particular data is not available in the current Aruba product documentation dataset. | known_missing |

## Notes

- The set is intentionally weighted toward successful answers.
- The final row is kept as a negative coverage check for a missing 5420 product-doc case.
- Syntax answers are kept as exact syntax text with a code block.
