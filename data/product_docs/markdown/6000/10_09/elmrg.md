AOS-CX Event Log Message
Reference Guide 10.09

4100i, 6xxx, 8xxx Switch Series

Published: September 2022
Edition: 2

Copyright Information

© Copyright 2022 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General Public
License, and/or certain other open source licenses. A complete machine-readable copy of the source code
corresponding to such code is available upon request. This offer is valid to anyone in receipt of this
information and shall expire three years following the date of the final distribution of this product version
by Hewlett Packard Enterprise Company. To obtain such source code, send a check or money order in the
amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

Notices

The information contained herein is subject to change without notice. The only warranties for Hewlett
Packard Enterprise products and services are set forth in the express warranty statements accompanying
such products and services. Nothing herein should be construed as constituting an additional warranty.
Hewlett Packard Enterprise shall not be liable for technical or editorial errors or omissions contained herein.

Confidential computer software. Valid license from Hewlett Packard Enterprise required for possession, use,
or copying. Consistent with FAR 12.211 and 12.212, Commercial Computer Software, Computer Software
Documentation, and Technical Data for Commercial Items are licensed to the U.S. Government under
vendor's standard commercial license.

Links to third-party websites take you outside the Hewlett Packard Enterprise website. Hewlett Packard
Enterprise has no control over and is not responsible for information outside the Hewlett Packard
Enterprise website.

| 2

Contents
Contents
| Contents                           |                |            |            |             |              | 3   |
| ---------------------------------- | -------------- | ---------- | ---------- | ----------- | ------------ | --- |
| Identifyingmodularswitchcomponents |                |            |            |             |              | 8   |
| AAA                                | events         |            |            |             |              | 9   |
| Accounting                         |                | events     |            |             |              | 11  |
| ACLs                               | events         |            |            |             |              | 12  |
| Alarm                              | events         |            |            |             |              | 13  |
| ARP                                | security       | events     |            |             |              | 16  |
| ASIC                               | table          | full error | for        | L3PD events |              | 17  |
| BFD                                | events         |            |            |             |              | 20  |
| BGP                                | events         |            |            |             |              | 25  |
| Bluetooth                          |                | Management |            | events      |              | 30  |
| CDP                                | events         |            |            |             |              | 32  |
| Certificate                        |                | management |            | events      |              | 34  |
| Config                             | Management     |            | events     |             |              | 39  |
| Connectivity                       |                | Fault      | Management |             | (CFM) events | 41  |
| Console                            | events         |            |            |             |              | 42  |
| Container                          |                | manager    | events     |             |              | 43  |
| CoPP                               | events         |            |            |             |              | 44  |
| CPU_RX                             | events         |            |            |             |              | 47  |
| Credential                         |                | Manager    | events     |             |              | 48  |
| Device                             | fingerprinting |            | events     |             |              | 50  |
| DHCP                               | Relay          | events     |            |             |              | 51  |
| DHCP                               | server         | events     |            |             |              | 52  |
3
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| DHCPv4        | snooping      | events     |          |        |        | 55  |
| ------------- | ------------- | ---------- | -------- | ------ | ------ | --- |
| DHCPv6        | Relay         | events     |          |        |        | 60  |
| DHCPv6        | snooping      | events     |          |        |        | 61  |
| Dicovery      | and           | Capability | Exchange | (DCBx) | events | 65  |
| DNS client    | events        |            |          |        |        | 67  |
| Dot1x         | supplicant    | events     |          |        |        | 68  |
| DPSE events   |               |            |          |        |        | 69  |
| ECMP          | events        |            |          |        |        | 71  |
| ERPS events   |               |            |          |        |        | 73  |
| EVPN          | events        |            |          |        |        | 77  |
| External      | Storage       | events     |          |        |        | 81  |
| Fan events    |               |            |          |        |        | 83  |
| Fault monitor |               | events     |          |        |        | 88  |
| Firmware      | Update        | events     |          |        |        | 90  |
| Hardware      | Health        | Monitor    | events   |        |        | 92  |
| Hardware      | switch        | controller | sync     | events |        | 95  |
| HTTPS         | Server events |            |          |        |        | 98  |
| In-System     | Programming   |            | events   |        |        | 100 |
| Interface     | events        |            |          |        |        | 103 |
| Internal      | storage       | events     |          |        |        | 105 |
| IP source     | lockdown      | events     |          |        |        | 106 |
| IP tunnels    | events        |            |          |        |        | 108 |
| IP-SLA        | events        |            |          |        |        | 112 |
| IPv6 Router   | Advertisement |            | events   |        |        | 114 |
| IRDP events   |               |            |          |        |        | 119 |
| Job scheduler |               | events     |          |        |        | 120 |
| L3 Encap      | capacity      | events     |          |        |        | 121 |
Contents|4

| L3 Resource |             | Manager    |         | events        |        |        | 122 |
| ----------- | ----------- | ---------- | ------- | ------------- | ------ | ------ | --- |
| LACP        | events      |            |         |               |        |        | 123 |
| LAG         | events      |            |         |               |        |        | 129 |
| Layer       | 3 Interface |            | events  |               |        |        | 132 |
| LED events  |             |            |         |               |        |        | 139 |
| LLDP        | events      |            |         |               |        |        | 140 |
| Loop        | Protect     | events     |         |               |        |        | 143 |
| Loopback    |             | events     |         |               |        |        | 145 |
| MAC         | address     | management |         |               | events |        | 146 |
| MAC         | Address     | mode       |         | configuration |        | events | 148 |
| MACsec      | events      |            |         |               |        |        | 149 |
| Management  |             | events     |         |               |        |        | 151 |
| MDNS        | events      |            |         |               |        |        | 152 |
| MGMD        | events      |            |         |               |        |        | 153 |
| Mirroring   |             | events     |         |               |        |        | 158 |
| Module      | events      |            |         |               |        |        | 160 |
| MPLS        | events      |            |         |               |        |        | 168 |
| MSDP        | events      |            |         |               |        |        | 169 |
| Multicast   |             | Traffic    | Manager |               | events |        | 171 |
| Multiple    | spanning    |            | tree    | protocol      |        | events | 172 |
| MVRP        | events      |            |         |               |        |        | 176 |
| NAE         | Agents      | events     |         |               |        |        | 178 |
| NAE         | events      |            |         |               |        |        | 179 |
| NAE         | script      | generation |         | events        |        |        | 182 |
| NAE         | Scripts     | events     |         |               |        |        | 183 |
| ND snooping |             | events     |         |               |        |        | 186 |
| NDM         | events      |            |         |               |        |        | 188 |
5
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| NTP events      |        |            |          |               |        | 195 |
| --------------- | ------ | ---------- | -------- | ------------- | ------ | --- |
| OSPFv2          | events |            |          |               |        | 197 |
| OSPFv3          | events |            |          |               |        | 200 |
| Password        |        | Reset      | events   |               |        | 202 |
| PIM events      |        |            |          |               |        | 203 |
| Policies        | events |            |          |               |        | 210 |
| Port access     |        | events     |          |               |        | 211 |
| Port access     |        | group      | based    | policy events |        | 214 |
| Port access     |        | roles      | events   |               |        | 216 |
| Port events     |        |            |          |               |        | 217 |
| Port security   |        | events     |          |               |        | 219 |
| Port Statistics |        | events     |          |               |        | 220 |
| Power           | events |            |          |               |        | 221 |
| Power           | over   | Ethernet   | events   |               |        | 226 |
| PTP events      |        |            |          |               |        | 235 |
| QoS ASIC        |        | Provider   | events   |               |        | 239 |
| Quality         | of     | Service    | events   |               |        | 241 |
| Rapid           | per    | VLAN       | Spanning | Tree Protocol | events | 242 |
| RBAC            | events |            |          |               |        | 245 |
| Redundant       |        | Management |          | events        |        | 246 |
| Replication     |        | Manager    | events   |               |        | 248 |
| REST            | events |            |          |               |        | 249 |
| Self Test       | events |            |          |               |        | 261 |
| sFlow           | events |            |          |               |        | 262 |
| SFTP            | Client | events     |          |               |        | 269 |
| Smartlink       |        | events     |          |               |        | 270 |
| SNMP            | events |            |          |               |        | 271 |
Contents|6

| SSH client     |            | events       |           |           |        |              | 274 |
| -------------- | ---------- | ------------ | --------- | --------- | ------ | ------------ | --- |
| SSH server     |            | events       |           |           |        |              | 275 |
| Supportability |            |              | events    |           |        |              | 278 |
| SYS events     |            |              |           |           |        |              | 285 |
| SYSMON         |            | events       |           |           |        |              | 287 |
| TCAM           | events     |              |           |           |        |              | 289 |
| Telnet         | server     |              | events    |           |        |              | 293 |
| Temperature    |            |              | events    |           |        |              | 295 |
| Time           | management |              |           | events    |        |              | 298 |
| Transceiver    |            |              | events    |           |        |              | 299 |
| UDLD           | events     |              |           |           |        |              | 302 |
| UDP            | Broadcast  |              | Forwarder |           | events |              | 304 |
| UFD            | events     |              |           |           |        |              | 305 |
| User           | management |              |           | events    |        |              | 306 |
| User-based     |            | tunnels      |           | events    |        |              | 308 |
| Virtual        | Switching  |              |           | Extension |        | (VSX) events | 316 |
| Virtual        | Switching  |              |           | Framework |        | (VSF) events | 324 |
| VLAN           | events     |              |           |           |        |              | 334 |
| VLAN           | Interface  |              | events    |           |        |              | 338 |
| VRF events     |            |              |           |           |        |              | 339 |
| VRF Manager    |            |              | events    |           |        |              | 340 |
| VRRP           | events     |              |           |           |        |              | 341 |
| VSX Sync       |            | events       |           |           |        |              | 347 |
| VXLAN          | agent      |              | events    |           |        |              | 348 |
| VXLAN          | events     |              |           |           |        |              | 349 |
| Zero           | touch      | provisioning |           |           | events |              | 353 |
| Support        |            | and          | other     | resources |        |              | 359 |
7
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Warranty information
Documentation feedback

359
359

Identifying modular switch components

n Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

Contents | 8

Chapter 3
AAA events
AAA events
ThefollowingaretheeventsrelatedtoAAA.
EventID:2301
| Message  | AAA <aaa_config_type> |     | update: | <aaa_config_event> |
| -------- | --------------------- | --- | ------- | ------------------ |
| Category | AAA                   |     |         |                    |
| Severity | Information           |     |         |                    |
Description LogsAAAAuthentication/Authorization/Accounting/fail-through
EventID:2302
| Message  | TACACS <tacacs_type> |     | <tacacs_action>: | <tacacs_event> |
| -------- | -------------------- | --- | ---------------- | -------------- |
| Category | AAA                  |     |                  |                |
| Severity | Information          |     |                  |                |
Description LogsTACACS+serverupdate,servergroupupdateandglobaldefaultupdate
EventID:2303
| Message  | RADIUS <radius_type> |     | <radius_action>: | <radius_event> |
| -------- | -------------------- | --- | ---------------- | -------------- |
| Category | AAA                  |     |                  |                |
| Severity | Information          |     |                  |                |
Description LogsRADIUSserverupdate,servergroupupdateandglobaldefaultupdate
EventID:2304
Message RADIUS Server with Address:<server_address>, Authport:<server_
|             | authport>,                                  | VRF_ID:<server_vrfid> |     | is "<status>" |
| ----------- | ------------------------------------------- | --------------------- | --- | ------------- |
| Category    | AAA                                         |                       |     |               |
| Severity    | Information                                 |                       |     |               |
| Description | LogschangesinRADIUSserverreachabilitystatus |                       |     |               |
EventID:2305
9
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

TACACS server host <server_address> port <server_port> vrf <server_vrf>
<status>

Category

AAA

Severity

Information

Description

Logs changes in TACACS server reachability status

Event ID: 2306

Message

RADIUS Server route with Address:<server_address>, VRF_ID:<server_
vrfid> is "<status>"

Category

AAA

Severity

Information

Description

Logs changes in RADIUS server route reachability status

AAA events | 10

Chapter 4

Accounting events

Accounting events

The following are the events related to accounting.

Event ID: 13101

Message

SSH session from <ip_address> with User <user_name> timed out due to
idle timeout.

Category

Accounting

Severity

Information

Description

Logs a message when a SSH session timed out due to the session being idle

Event ID: 13102

Message

TELNET session from <ip_address> with User <user_name> timed out due to
idle timeout.

Category

Accounting

Severity

Information

Description

Logs a message when a TELNET session timed out due to the session being idle

Event ID: 13103

Message

CONSOLE session from <ip_address> with User <user_name> timed out due
to idle timeout.

Category

Accounting

Severity

Information

Description

Logs a message when a CONSOLE session timed out due to the session being idle

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

11

Chapter 5

ACLs events

ACLs events

The following are the events related to ACLs.

Event ID: 10001

Message

Category

Severity

<log>

ACLs

Information

Description

ACL log

Event ID: 10002

Message

<acl_name> on <interface_name> (<direction>): <hit_delta> <ace_string>

Category

ACLs

Severity

Information

Description

ACL log statistics

Event ID: 10003

Message

ACL <acl_type> <acl_name> failed to apply on <application>

Category

Severity

ACLs

Error

Description

ACL application failure

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

12

Chapter 6

Alarm events

Alarm events

The following are the events related to alarm.

Event ID: 11701

Message

Input alarm <id> config change: name: <name>, relay: <relay>, log_and_
trap: <log_and_trap>, trigger: <trigger>

Category

Alarm

Severity

Information

Description

Event reported when there is a change in input alarm configuration.

Event ID: 11702

Message

System alarm (<type>) config change: relay: <relay>, log_and_trap:
<log_and_trap>

Category

Alarm

Severity

Information

Description

Event reported when there is a change in system alarm configuration.

Event ID: 11703

Message

System alarm <name> has activated through log-and-trap': yes

Category

Alarm

Severity

Information

Description

Event reported when system alarm has activated

Event ID: 11704

Message

Input alarm <name> has activated through log-and-trap, triggered at
<trigger>': yes

Category

Alarm

Severity

Information

Description

Event reported when input alarm has activated

Event ID: 11705

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

13

Message Snooze alarm activated, disabling relay function for <length> min': yes
| Category    | Alarm                                         |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | Eventreportedwhenalarmsnoozetimerhasactivated |     |     |     |
EventID:11706
| Message     | Snooze alarm                                | has expired': | yes |     |
| ----------- | ------------------------------------------- | ------------- | --- | --- |
| Category    | Alarm                                       |               |     |     |
| Severity    | Information                                 |               |     |     |
| Description | Eventreportedwhenalarmsnoozetimerhasexpired |               |     |     |
EventID:11707
| Message     | Alarm relay                                     | function | is re-enabled': | yes |
| ----------- | ----------------------------------------------- | -------- | --------------- | --- |
| Category    | Alarm                                           |          |                 |     |
| Severity    | Information                                     |          |                 |     |
| Description | Eventreportedwhenalarmrelayfunctionisre-enabled |          |                 |     |
EventID:11708
Message Snooze alarm repeats, disabling relay function for <length> min': yes
| Category    | Alarm                                    |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- |
| Severity    | Information                              |     |     |     |
| Description | Eventreportedwhenalarmsnoozetimerrepeats |     |     |     |
EventID:11709
| Message  | System alarm | <name> has | activated | through relay |
| -------- | ------------ | ---------- | --------- | ------------- |
| Category | Alarm        |            |           |               |
| Severity | Information  |            |           |               |
Description Eventreportedwhensystemalarmhasactivatedthroughrelay
EventID:11710
Message Input alarm <name> has activated through relay, triggered at <trigger>
Alarmevents|14

Category

Alarm

Severity

Information

Description

Event reported when input alarm has activated through relay

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

15

Chapter 7
ARP security events
| ARP security events |     |     |     |
| ------------------- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoARPsecurity.
EventID:10401
| Message     | ARP inspection                   | <status> | on vlan <vlan_id>. |
| ----------- | -------------------------------- | -------- | ------------------ |
| Category    | ARPsecurity                      |          |                    |
| Severity    | Information                      |          |                    |
| Description | ARPinspectionconfigurationonVLAN |          |                    |
EventID:10402
| Message     | ARP inspection                     | <status> | on port <port_name>. |
| ----------- | ---------------------------------- | -------- | -------------------- |
| Category    | ARPsecurity                        |          |                      |
| Severity    | Information                        |          |                      |
| Description | ARPinspectionportmodeconfiguration |          |                      |
16
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 8
|            |            |          | ASIC   | table | full error | for L3PD | events |
| ---------- | ---------- | -------- | ------ | ----- | ---------- | -------- | ------ |
| ASIC table | full error | for L3PD | events |       |            |          |        |
ThefollowingaretheeventsrelatedtoASICtablefullerrorforL3PD.
EventID:10801
Message Neighbor add failure due to neighbor hardware full.' throttle_count: 1
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- | --- |
| Severity |     | Error                     |     |     |     |     |     |
Description HardwaretableforNEIGHBORentriesarefull,nonewneighborswillbeadded.
EventID:10802
Message Route add failure due to route hardware full' throttle_count: 1
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- | --- |
| Severity |     | Error                     |     |     |     |     |     |
Description HardwaretableforROUTEentriesarefull,nonewroutewillbeadded.
EventID:10803
| Message  |     | Self IP add               | failure due | to self | ip hardware full |     |     |
| -------- | --- | ------------------------- | ----------- | ------- | ---------------- | --- | --- |
| Category |     | ASICtablefullerrorforL3PD |             |         |                  |     |     |
| Severity |     | Error                     |             |         |                  |     |     |
Description HardwaretableforSELFIPentriesarefull,nonewselfipwillbeadded.
EventID:10804
Message Custom route prefix tables configured from customer_override.yaml
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- | --- |
| Severity |     | Information               |     |     |     |     |     |
Description Customrouteprefixtablesconfiguredfromcustomer_override.yaml
EventID:10805(Severity:Warning)
17
| AOS-CXEventLogMessageReferenceGuide10.09| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

Message

Error parsing LIST_ROUTE_IPV4_PREFIX in customer_override.yaml file

Category

ASIC table full error for L3PD

Severity

Warning

Description

Error parsing LIST_ROUTE_IPV4_PREFIX in customer_override.yaml file

Event ID: 10806 (Severity: Warning)

Message

Error parsing LIST_ROUTE_IPV6_PREFIX in customer_override.yaml file

Category

ASIC table full error for L3PD

Severity

Warning

Description

Error parsing LIST_ROUTE_IPV6_PREFIX in customer_override.yaml file

Event ID: 10807

Message

Using configured IPv4 prefix-priority list <prefix_list>.

Category

ASIC table full error for L3PD

Severity

Information

Description

Log configured ip prefix-priority list.

Event ID: 10808

Message

Using configured IPv6 prefix-priority list <prefix_list>.

Category

ASIC table full error for L3PD

Severity

Information

Description

Log configured ipv6 prefix-priority list.

Event ID: 10809

Message

HW programming failed for IPv4 prefix-priority <route_prefix>

Category

ASIC table full error for L3PD

Severity

Error

Description

Logs failure while configuring hardware for ipv4 prefix-priority.

Event ID: 10810

Message

HW programming failed for IPv6 prefix-priority <route_prefix>

ASIC table full error for L3PD events | 18

Category

ASIC table full error for L3PD

Severity

Error

Description

Logs failure while configuring hardware for ipv6 prefix-priority.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

19

Chapter 9
BFD events
BFD events
ThefollowingaretheeventsrelatedtoBFD.
EventID:7301
| Message     | BFD was enabled                     |     |
| ----------- | ----------------------------------- | --- |
| Category    | BFD                                 |     |
| Severity    | Information                         |     |
| Description | EventraisedwhenBFDisenabledglobally |     |
EventID:7302
| Message     | BFD was disabled                     |     |
| ----------- | ------------------------------------ | --- |
| Category    | BFD                                  |     |
| Severity    | Information                          |     |
| Description | EventraisedwhenBFDisdisabledglobally |     |
EventID:7303
| Message     | BFD echo was                            | enabled |
| ----------- | --------------------------------------- | ------- |
| Category    | BFD                                     |         |
| Severity    | Information                             |         |
| Description | EventraisedwhenBFDechoisenabledglobally |         |
EventID:7304
| Message     | BFD echo was                         | disabled |
| ----------- | ------------------------------------ | -------- |
| Category    | BFD                                  |          |
| Severity    | Information                          |          |
| Description | EventraisedwhenBFDisdisabledglobally |          |
EventID:7305
20
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | BFD echo was                                 | enabled | on interface | <intf> |     |
| ----------- | -------------------------------------------- | ------- | ------------ | ------ | --- |
| Category    | BFD                                          |         |              |        |     |
| Severity    | Information                                  |         |              |        |     |
| Description | EventraisedwhenBFDechoisenabledonaninterface |         |              |        |     |
EventID:7306
| Message     | BFD echo was                              | disabled | on interface | <intf> |     |
| ----------- | ----------------------------------------- | -------- | ------------ | ------ | --- |
| Category    | BFD                                       |          |              |        |     |
| Severity    | Information                               |          |              |        |     |
| Description | EventraisedwhenBFDisdisabledonaninterface |          |              |        |     |
EventID:7307
Message BFD session is up. session_id=<session_id>, vrf=<vrf>, op_mode=<op_
mode>, src_port=<src_port>, dest_ip=<dest_ip>, local_state=<local_
state>, local_diag=<local_diag>, remote_state=<remote_state>, remote_
diag=<remote_diag>
| Category    | BFD                                      |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                              |     |     |     |     |
| Description | EventraisedwhenaBFDsessionstatebecomesup |     |     |     |     |
EventID:7308
Message BFD session is down. session_id=<session_id>, vrf=<vrf>, op_mode=<op_
mode>, src_port=<src_port>, dest_ip=<dest_ip>, local_state=<local_
state>, local_diag=<local_diag>, remote_state=<remote_state>, remote_
diag=<remote_diag>
| Category    | BFD                                        |     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- |
| Severity    | Information                                |     |     |     |     |
| Description | EventraisedwhenaBFDsessionstatebecomesdown |     |     |     |     |
EventID:7309
Message BFD session is administratively down. session_id=<session_id>,
vrf=<vrf>, op_mode=<op_mode>, src_port=<src_port>, dest_ip=<dest_ip>,
|          | local_state=<local_state>, |     | local_diag=<local_diag>,  |     | remote_ |
| -------- | -------------------------- | --- | ------------------------- | --- | ------- |
|          | state=<remote_state>,      |     | remote_diag=<remote_diag> |     |         |
| Category | BFD                        |     |                           |     |         |
BFDevents|21

| Severity    | Information                                      |     |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- | --- |
| Description | EventraisedwhenaBFDsessionisadministrativelydown |     |     |     |     |
EventID:7310
| Message  | BFD session | was created | without | a source port |     |
| -------- | ----------- | ----------- | ------- | ------------- | --- |
| Category | BFD         |             |         |               |     |
| Severity | Information |             |         |               |     |
Description EventraisedwhenaBFDsessioniscreatedwithoutasourceport
EventID:7311
| Message  | Port <name> | can forward | BFD traffic |     |     |
| -------- | ----------- | ----------- | ----------- | --- | --- |
| Category | BFD         |             |             |     |     |
| Severity | Information |             |             |     |     |
Description EventraisedwhenaportusedbyBFDsessioncanforwardtraffic
EventID:7312
| Message  | Port <name> | can not forward | BFD | traffic |     |
| -------- | ----------- | --------------- | --- | ------- | --- |
| Category | BFD         |                 |     |         |     |
| Severity | Information |                 |     |         |     |
Description EventraisedwhenaportusedbyBFDsessioncannotforwardtraffic
EventID:7313
| Message  | BFD sessions | maximum | active capacity | reached |     |
| -------- | ------------ | ------- | --------------- | ------- | --- |
| Category | BFD          |         |                 |         |     |
| Severity | Information  |         |                 |         |     |
Description EventraisedwhenthemaximumnumberofactiveBFDsessionsisreached
EventID:7314(Severity:Warning)
Message The echo function for the BFD session <session_id> will not become
|          | active until | a global | echo source | IP address | is configured |
| -------- | ------------ | -------- | ----------- | ---------- | ------------- |
| Category | BFD          |          |             |            |               |
22
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

| Severity | Warning |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
Description EventraisedwhenanEchosessioniscreatedwithoutavalidecho_sourceIPaddress
configured
EventID:7315
Message BFD session is unidirectional. session_id=<session_id>, vrf=<vrf>, op_
|     | mode=<op_mode>, | src_port=<src_port>, |     | dest_ip=<dest_ip>, | local_ |
| --- | --------------- | -------------------- | --- | ------------------ | ------ |
state=<local_state>, local_diag=<local_diag>, remote_state=<remote_
|          | state>, | remote_diag=<remote_diag> |     |     |     |
| -------- | ------- | ------------------------- | --- | --- | --- |
| Category | BFD     |                           |     |     |     |
| Severity | Error   |                           |     |     |     |
Description EventraisedwhenaBFDsessionstatebecomesunidirectional
EventID:7316(Severity:Warning)
Message BFD echo cannot be enabled on tunnels. interface=<intf>
| Category | BFD     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
| Severity | Warning |     |     |     |     |
Description EventraisedwhenBFDechoisenabledonaTunnelinterface
EventID:7317(Severity:Warning)
| Message  | BFD echo | is not supported | on IPv6 | sessions |     |
| -------- | -------- | ---------------- | ------- | -------- | --- |
| Category | BFD      |                  |         |          |     |
| Severity | Warning  |                  |         |          |     |
Description EventraisedwhenBFDechoisenabledforasessionusingIPv6
EventID:7318
Message IP Version mismatch for BFD. session_id=<session_id>, vrf=<vrf>, op_
|     | mode=<op_mode>, | src_port=<src_port>, |     | dest_ip=<dest_ip>, | local_ |
| --- | --------------- | -------------------- | --- | ------------------ | ------ |
state=<local_state>, local_diag=<local_diag>, remote_state=<remote_
|          | state>,   | remote_diag=<remote_diag>, |                    | from=<from>, | ip_version=<ip_ |
| -------- | --------- | -------------------------- | ------------------ | ------------ | --------------- |
|          | version>, | Invalid                    | IP address: <addr> |              |                 |
| Category | BFD       |                            |                    |              |                 |
| Severity | Error     |                            |                    |              |                 |
Description "EventraisedwhenSRCorDSTIPVersiondoesn'tmatchthesession'sIPVersion"
EventID:7319(Severity:Warning)
BFDevents|23

| Message  | BFD single-hop | is not supported | on interface | <intf> |
| -------- | -------------- | ---------------- | ------------ | ------ |
| Category | BFD            |                  |              |        |
| Severity | Warning        |                  |              |        |
Description "EventraisedwhenaBFDsingle-hopsessionsourceportisaloopback"
EventID:7320(Severity:Warning)
Message BFD session interval override not supported for protocol <from>
| Category | BFD     |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description "EventraisedwhenaBFDsessionspecifiesanintervalforaprotocolthatdoesnot
supportoverride"
EventID:7321(Severity:Warning)
Message BFD session <direction> interval override of <requested_interval> ms is
out of bounds for protocol <from>, using <applied_interval> ms instead
| Category | BFD     |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description "EventraisedwhenaBFDsessionspecifiesanintervaloutsidethespecifiedbounds"
24
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 10
BGP events
BGP events
ThefollowingaretheeventsrelatedtoBGP.
EventID:2901
| Message     | <remote-addr>:                      | Peer | up. vrf-name: | <vrf-name> |
| ----------- | ----------------------------------- | ---- | ------------- | ---------- |
| Category    | BGP                                 |      |               |            |
| Severity    | Information                         |      |               |            |
| Description | LogsthechangesinBGPconnectionstate. |      |               |            |
EventID:2902
Message <remote-addr>: Peer down. error-code: <error-code>, error-sub-code:
|             | <error-subcode>.                           | vrf-name: | <vrf-name> |     |
| ----------- | ------------------------------------------ | --------- | ---------- | --- |
| Category    | BGP                                        |           |            |     |
| Severity    | Information                                |           |            |     |
| Description | LogsthefailureinBGPconnectionstatechanges. |           |            |     |
EventID:2903
Message <remote-addr>: Peer has received prefix equal to Maximum Prefix value
|          | configured. | vrf-name: | <vrf-name> |     |
| -------- | ----------- | --------- | ---------- | --- |
| Category | BGP         |           |            |     |
| Severity | Information |           |            |     |
Description Trapwhenthenumberofreceivedprefixreachesthemaximumprefixvalue.
EventID:2904
Message <remote-addr>: Peer has received prefix equal to Threshold value
|          | configured. | vrf-name: | <vrf-name> |     |
| -------- | ----------- | --------- | ---------- | --- |
| Category | BGP         |           |            |     |
| Severity | Information |           |            |     |
Description Trapwhenthenumberofreceivedprefixreachedthethresholdvalue.
EventID:2905
25
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | BGP AS <as_number>  | configured. | vrf-name: | <vrf-name> |
| ----------- | ------------------- | ----------- | --------- | ---------- |
| Category    | BGP                 |             |           |            |
| Severity    | Information         |             |           |            |
| Description | LogsBGPenableevent. |             |           |            |
EventID:2906
Message BGP AS <as_number> unconfigured. vrf-name: <vrf-name>
| Category    | BGP                  |     |     |     |
| ----------- | -------------------- | --- | --- | --- |
| Severity    | Information          |     |     |     |
| Description | LogsBGPdisableevent. |     |     |     |
EventID:2907
| Message     | BGP router-id           | changed. vrf-name: | <vrf-name> |     |
| ----------- | ----------------------- | ------------------ | ---------- | --- |
| Category    | BGP                     |                    |            |     |
| Severity    | Information             |                    |            |     |
| Description | LogsBGProuter-idchange. |                    |            |     |
EventID:2908
Message <remote_addr>: Peer configured, AS <remote_as>. vrf-name: <vrf-name>
| Category    | BGP                    |     |     |     |
| ----------- | ---------------------- | --- | --- | --- |
| Severity    | Information            |     |     |     |
| Description | LogscreationofBGPpeer. |     |     |     |
EventID:2909
Message <remote_addr>: User reset request. vrf-name: <vrf-name>
| Category    | BGP                           |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Severity    | Information                   |     |     |     |
| Description | LogsBGPpeersessionresetevent. |     |     |     |
EventID:2910
Message <remote_addr>: Peer password changed. vrf-name: <vrf-name>
BGPevents|26

| Category    | BGP                             |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- |
| Severity    | Information                     |     |     |     |
| Description | LogsBGPpeerpasswordchangeevent. |     |     |     |
EventID:2911
| Message     | <remote_addr>:         | Peer deleted. | vrf-name: | <vrf-name> |
| ----------- | ---------------------- | ------------- | --------- | ---------- |
| Category    | BGP                    |               |           |            |
| Severity    | Information            |               |           |            |
| Description | LogsdeletionofBGPpeer. |               |           |            |
EventID:2912
Message <remote_addr>: Peer admin disabled. vrf-name: <vrf-name>
| Category    | BGP                          |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Information                  |     |     |     |
| Description | LogsBGPpeeradmindisableevent |     |     |     |
EventID:2913
Message <remote_addr>: Peer admin enabled. vrf-name: <vrf-name>
| Category    | BGP                          |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Information                  |     |     |     |
| Description | LogsBGPpeeradminenableevent. |     |     |     |
EventID:2914
Message <remote_addr>: Peer remote-as changed to <remote_as>. vrf-name: <vrf-
name>
| Category    | BGP                              |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- |
| Severity    | Information                      |     |     |     |
| Description | LogsBGPpeerremote-aschangeevent. |     |     |     |
EventID:2915
Message <remote_addr>: Peer local-as changed to <local_as>. vrf-name: <vrf-
name>
27
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Category

BGP

Severity

Information

Description

BGP peer local-as change event.

Event ID: 2916

Message

<remote_addr>: Peer source-address changed to <src_ipaddr>. vrf-name:
<vrf-name>

Category

BGP

Severity

Information

Description

Logs peer source address change event.

Event ID: 2917

Message

<remote_addr>: Peer remove-private-as configuration changed. vrf-name:
<vrf-name>

Category

BGP

Severity

Information

Description

Logs configuration of peer remove-private-as.

Event ID: 2918

Message

<bgp_id>: BGP identifier sent by Peer <remote_addr> matches ours. BGP
session may not established. vrf-name: <vrf-name>

Category

BGP

Severity

Information

Description

Logs peer identifier has been matched with local identifier.

Event ID: 2919 (Severity: Critical)

Message

Category

Severity

The BGP RIB has reached the threshold limit of <threshold_limit> for
VRF <vrf-name>': yes

BGP

Critical

Description

Trap when the rib size reaches the threshold value.

Event ID: 2920

BGP events | 28

Message

<pg_name>: Peer-group configured with remote-as <remote_as>. vrf-name:
<vrf-name>

Category

BGP

Severity

Information

Description

Logs BGP peer-group remote-as configuration event.

Event ID: 2921

Message

<remote_addr>: Peer ignore-leading-as configuration changed. vrf-name:
<vrf-name>

Category

BGP

Severity

Information

Description

Logs configuration of peer ignore-leading-as.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

29

Chapter 11
|           |            |        | Bluetooth | Management | events |
| --------- | ---------- | ------ | --------- | ---------- | ------ |
| Bluetooth | Management | events |           |            |        |
ThefollowingaretheeventsrelatedtoBluetoothmanagement.
EventID:8001
| Message | Bluetooth | has been | <enabled_disabled> |     |     |
| ------- | --------- | -------- | ------------------ | --- | --- |
Category BluetoothManagement
Severity Information
Description EventraisedwhenBluetoothisenabledordisabled
EventID:8002(Severity:Warning)
| Message | Bluetooth | unable | to trust pairing | device |     |
| ------- | --------- | ------ | ---------------- | ------ | --- |
Category BluetoothManagement
Severity Warning
Description EventraisedwhenBluetoothisunabletotrustpairingdevice
EventID:8003
| Message | Bluetooth | adapter | <inserted_removed> |     |     |
| ------- | --------- | ------- | ------------------ | --- | --- |
Category BluetoothManagement
Severity Information
Description EventraisedwhenbtdreceivessignalforBluetoothadapterevent
EventID:8004
Message Bluetooth device <connected_disconnected>: <mac_address>
Category BluetoothManagement
Severity Information
Description EventraisedwhenbtdreceivessignalforBluetoothdeviceevent
EventID:8005(Severity:Warning)
30
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Message

Bluetooth device rejected because another device is already connected

Category

Bluetooth Management

Severity

Warning

Description

Event raised when btd disconnects a newly paried device because another device is
already connected

Bluetooth Management events | 31

Chapter 12
CDP events
CDP events
ThefollowingaretheeventsrelatedtoCDP.
EventID:8901
| Message     | CDP Enabled    |     |     |
| ----------- | -------------- | --- | --- |
| Category    | CDP            |     |     |
| Severity    | Information    |     |     |
| Description | LogsCDPenabled |     |     |
EventID:8902
| Message     | CDP Disabled   |     |     |
| ----------- | -------------- | --- | --- |
| Category    | CDP            |     |     |
| Severity    | Information    |     |     |
| Description | LogsCDPdisbled |     |     |
EventID:8903
| Message     | CDP neighbor                     | <mac> is added | on <interface> |
| ----------- | -------------------------------- | -------------- | -------------- |
| Category    | CDP                              |                |                |
| Severity    | Information                      |                |                |
| Description | LogtoindicateCDPneighboraddition |                |                |
EventID:8904
Message CDP neighbor <mac> is updated on <interface>' throttle_count: 100
| Category    | CDP                                   |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Information                           |     |     |
| Description | LogtoindicateCDPneighbourmodification |     |     |
EventID:8905
32
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | CDP neighbor                     | <mac> is deleted | on <interface> |
| ----------- | -------------------------------- | ---------------- | -------------- |
| Category    | CDP                              |                  |                |
| Severity    | Information                      |                  |                |
| Description | LogtoindicateCDPneighbordeletion |                  |                |
EventID:8906
| Message     | All CDP neighbor                         | info cleared |     |
| ----------- | ---------------------------------------- | ------------ | --- |
| Category    | CDP                                      |              |     |
| Severity    | Information                              |              |     |
| Description | LogtoindicateallCDPneighborinfoiscleared |              |     |
CDPevents|33

Chapter 13
|             |            |        | Certificate | management | events |
| ----------- | ---------- | ------ | ----------- | ---------- | ------ |
| Certificate | management | events |             |            |        |
Thefollowingaretheeventsrelatedtocertificatemanagement.
EventID:7701
| Message     | TA Profile                         | <name> created |     |     |     |
| ----------- | ---------------------------------- | -------------- | --- | --- | --- |
| Category    | Certificatemanagement              |                |     |     |     |
| Severity    | Information                        |                |     |     |     |
| Description | Eventraisedwhenataprofileiscreated |                |     |     |     |
EventID:7702
| Message     | TA Profile                         | <name> deleted |     |     |     |
| ----------- | ---------------------------------- | -------------- | --- | --- | --- |
| Category    | Certificatemanagement              |                |     |     |     |
| Severity    | Information                        |                |     |     |     |
| Description | Eventraisedwhenataprofileisremoved |                |     |     |     |
EventID:7703
| Message     | Leaf                                      | certificate <name> | imported |     |     |
| ----------- | ----------------------------------------- | ------------------ | -------- | --- | --- |
| Category    | Certificatemanagement                     |                    |          |     |     |
| Severity    | Information                               |                    |          |     |     |
| Description | Eventraisedwhenaleafcertificateisimported |                    |          |     |     |
EventID:7704
| Message     | Leaf                                     | certificate <name> | deleted |     |     |
| ----------- | ---------------------------------------- | ------------------ | ------- | --- | --- |
| Category    | Certificatemanagement                    |                    |         |     |     |
| Severity    | Information                              |                    |         |     |     |
| Description | Eventraisedwhenaleafcertificateisdeleted |                    |         |     |     |
EventID:7705(Severity:Warning)
34
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

| Message  | Certificate           | <name> will | expire within | <days> days |
| -------- | --------------------- | ----------- | ------------- | ----------- |
| Category | Certificatemanagement |             |               |             |
| Severity | Warning               |             |               |             |
Description Eventraisedwhenaninstalledcertifiatewillexpirewithin60days
EventID:7706(Severity:Warning)
Message Certificate <name> has not yet reached its start date
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Warning               |     |     |     |
Description Eventraisedwhenaninstalledcertifiateisnotyetpastitsstartdate
EventID:7707(Severity:Warning)
Message Certificate <name> has expired and can no longer be used
| Category    | Certificatemanagement                          |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                        |     |     |     |
| Description | Eventraisedwhenaninstalledcertifiatehasexpired |     |     |     |
EventID:7708
Message Certificate <name> verified and accepted' throttle_count: 100
| Category    | Certificatemanagement                      |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Information                                |     |     |     |
| Description | Eventraisedwhenacertificatechainisverified |     |     |     |
EventID:7709(Severity:Warning)
Message Certificate <name> rejected due to verification failure (<error>)'
|             | throttle_count:                            | 100 |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Category    | Certificatemanagement                      |     |     |     |
| Severity    | Warning                                    |     |     |     |
| Description | Eventraisedwhenacertificatechainisrejected |     |     |     |
EventID:7710
Certificatemanagementevents|35

| Message  | Certificate           | signing request | <name> created |
| -------- | --------------------- | --------------- | -------------- |
| Category | Certificatemanagement |                 |                |
| Severity | Information           |                 |                |
Description Eventraisedwhenacertificatesigningrequestiscreatedontheswitch
EventID:7711
| Message  | Self-signed           | certificate | <name> created |
| -------- | --------------------- | ----------- | -------------- |
| Category | Certificatemanagement |             |                |
| Severity | Information           |             |                |
Description Eventraisedwhenaself-signedcertificateiscreatedontheswitch
EventID:7712
Message Application association with the <name> certificate is not permitted
| Category | Certificatemanagement |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Error                 |     |     |
Description Eventraisedwhenaninvalidcertificateassociationismade
EventID:7713(Severity:Warning)
Message Certificate <name> failed OCSP verification (<status>), but was
accepted because OCSP enforcement is set to optional.' throttle_count:
100
| Category | Certificatemanagement |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Warning               |     |     |
Description EventraisedwhenacertificateisverifiedduetooptionalOCSPenforcement
EventID:7714
Message CA certificates successfully downloaded from EST server <name>
| Category | Certificatemanagement |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Information           |     |     |
Description EventraisedwhenCAcertificatesweresuccessfullydownloadedfromanESTserver
EventID:7715
36
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Message Failed to download CA certificates from EST server <name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Error                 |     |     |     |
Description EventraisedwhenCAcertificatescouldnotbedownloadedfromanESTserver
EventID:7716
Message Certificate <name> successfully enrolled by EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description EventraisedwhenacertificateissuccessfullyenrolledwithEST
EventID:7717
Message Failed to enroll certificate <name> with EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Error                 |     |     |     |
Description EventraisedwhencertificateenrollmentwithanESTserverfails
EventID:7718
Message Certificate <name> successfully reenrolled by EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description EventraisedwhenacertificateissuccessfullyreenrolledwithEST
EventID:7719
Message Failed to reenroll certificate <name> with EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Error                 |     |     |     |
Description EventraisedwhencertificatereenrollmentwithanESTserverfails
EventID:7720(Severity:Warning)
| Message | Certificate | <name> | is not set for | signing purpose |
| ------- | ----------- | ------ | -------------- | --------------- |
Certificatemanagementevents|37

| Category    | Certificatemanagement                              |     |     |     |
| ----------- | -------------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                            |     |     |     |
| Description | Eventraisedwhenasignercertifiateisnotsetforsigning |     |     |     |
EventID:7721(Severity:Warning)
| Message  | Certificate           | <name> | is invalid | or malformed |
| -------- | --------------------- | ------ | ---------- | ------------ |
| Category | Certificatemanagement |        |            |              |
| Severity | Warning               |        |            |              |
Description Eventraisedwhenaninstalledcertifiateisinvalidormalformed
38
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 14
|                   |        |     | Config | Management | events |
| ----------------- | ------ | --- | ------ | ---------- | ------ |
| Config Management | events |     |        |            |        |
Thefollowingaretheeventsrelatedtoconfigmanagement.
EventID:6801
| Message  | Copying configs  | from: <from> | to: <to> |     |     |
| -------- | ---------------- | ------------ | -------- | --- | --- |
| Category | ConfigManagement |              |          |     |     |
| Severity | Information      |              |          |     |     |
Description Logsamessagewhenconfigscopyingfromoneformattoanother
EventID:6802
| Message     | Error while                               | copying configs. | Error: <error> |     |     |
| ----------- | ----------------------------------------- | ---------------- | -------------- | --- | --- |
| Category    | ConfigManagement                          |                  |                |     |     |
| Severity    | Error                                     |                  |                |     |     |
| Description | Logsamessagewhencopyingconfighassomeerror |                  |                |     |     |
EventID:6803
| Message  | <type>:<value>   |     |     |     |     |
| -------- | ---------------- | --- | --- | --- | --- |
| Category | ConfigManagement |     |     |     |     |
| Severity | Information      |     |     |     |     |
Description Logsamessagewhenconfigvalidationprunestables/columnsinstartup-configorwhen
errorsareencountered
EventID:6804
| Message  | Error while      | copying configs. | Error: <error> |     |     |
| -------- | ---------------- | ---------------- | -------------- | --- | --- |
| Category | ConfigManagement |                  |                |     |     |
| Severity | Error            |                  |                |     |     |
Description Logsamessagewhencopyingconfigtoshadowdbhassomeerror
EventID:6805
39
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

Information while copying configs. Info: <info>

Category

Config Management

Severity

Information

Description

Logs a message when copying config has some information

Config Management events | 40

Chapter 15
|     |     | Connectivity | Fault Management | (CFM) |
| --- | --- | ------------ | ---------------- | ----- |
events
| Connectivity | Fault Management | (CFM) events |     |     |
| ------------ | ---------------- | ------------ | --- | --- |
ThefollowingaretheeventsrelatedtoConnectivityFaultManagement(CFM).
EventID:11601
Message Connection lost for Maintenance Endpoint <id> on <interface>.
| Category | ConnectivityFaultManagement(CFM) |     |     |     |
| -------- | -------------------------------- | --- | --- | --- |
| Severity | Error                            |     |     |     |
Description EventreportedwhenconnectionislostontheMaintanenceEndpoint.
EventID:11602
Message Connection restored for Maintenance Endpoint <id> on <interface>.
| Category | ConnectivityFaultManagement(CFM) |     |     |     |
| -------- | -------------------------------- | --- | --- | --- |
| Severity | Information                      |     |     |     |
Description EventreportedwhenconnectionisrestoredontheMaintanenceEndpoint.
41
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 16

Console events

Console events

The following are the events related to console.

Event ID: 13001

Message

User <user_name> logged in from <ip_address> through CONSOLE session.

Category

Console

Severity

Information

Description

Logs a message when a user login is successful

Event ID: 13002

Message

User <user_name> login from <ip_address> for CONSOLE session has
failed.

Category

Console

Severity

Error

Description

Logs a message when a user login fails

Event ID: 13003

Message

User <user_name> logged out of CONSOLE session from <ip_address>.

Category

Console

Severity

Information

Description

Logs a message when a user logs out of a session

Event ID: 13004 (Severity: Warning)

Message

Category

Severity

Description

CONSOLE session from User <user_name> is closed because maximum number
of sessions per user is reached.

Console

Warning

Logs a message when a user tries to login while maximum number of sessions per user
are reached.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

42

Chapter 17
|           |         |        |     | Container | manager | events |
| --------- | ------- | ------ | --- | --------- | ------- | ------ |
| Container | manager | events |     |           |         |        |
Thefollowingaretheeventsrelatedtocontainermanager.
EventID:11801
| Message     |     | Container <name>                    | is created |     |     |     |
| ----------- | --- | ----------------------------------- | ---------- | --- | --- | --- |
| Category    |     | Containermanager                    |            |     |     |     |
| Severity    |     | Information                         |            |     |     |     |
| Description |     | Eventreportedwhencontaineriscreated |            |     |     |     |
EventID:11802
| Message     |     | Container <name>                    | is removed |     |     |     |
| ----------- | --- | ----------------------------------- | ---------- | --- | --- | --- |
| Category    |     | Containermanager                    |            |     |     |     |
| Severity    |     | Information                         |            |     |     |     |
| Description |     | Eventreportedwhencontainerisremoved |            |     |     |     |
EventID:11803
| Message     |     | Container <name>                        | is operational |     |     |     |
| ----------- | --- | --------------------------------------- | -------------- | --- | --- | --- |
| Category    |     | Containermanager                        |                |     |     |     |
| Severity    |     | Information                             |                |     |     |     |
| Description |     | Eventreportedwhencontainerisoperational |                |     |     |     |
43
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 18
CoPP events
CoPP events
Thefollowingaretheeventsrelatedtocontrolplanepolicing.
EventID:1501
| Message     | COPP initialization            |     | failed |
| ----------- | ------------------------------ | --- | ------ |
| Category    | CoPP                           |     |        |
| Severity    | Error                          |     |        |
| Description | LogsCOPPinitializationfailure. |     |        |
EventID:1502
| Message     | COPP initialization            |     | successful |
| ----------- | ------------------------------ | --- | ---------- |
| Category    | CoPP                           |     |            |
| Severity    | Information                    |     |            |
| Description | LogsCOPPinitializationsuccess. |     |            |
EventID:1503
| Message     | Ingress                                        | FP Group | create failed |
| ----------- | ---------------------------------------------- | -------- | ------------- |
| Category    | CoPP                                           |          |               |
| Severity    | Error                                          |          |               |
| Description | Logsingressfieldprocessorgroupcreationfailure. |          |               |
EventID:1504
| Message     | Egress                                        | FP Group create | failed |
| ----------- | --------------------------------------------- | --------------- | ------ |
| Category    | CoPP                                          |                 |        |
| Severity    | Error                                         |                 |        |
| Description | Logsegressfieldprocessorgroupcreationfailure. |                 |        |
EventID:1505
44
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Programming                                  | defaults failed |     |     |
| ----------- | -------------------------------------------- | --------------- | --- | --- |
| Category    | CoPP                                         |                 |     |     |
| Severity    | Error                                        |                 |     |     |
| Description | Logsfailureforinitializationofdefaultvalues. |                 |     |     |
EventID:1506
| Message  | Packet | class programming | failed for | <class> |
| -------- | ------ | ----------------- | ---------- | ------- |
| Category | CoPP   |                   |            |         |
| Severity | Error  |                   |            |         |
Description LogsfailureofprogrammingqueueforaCoPPpacketclass.
EventID:1507
Message Failed to program ingress field processor rule for <class>
| Category | CoPP  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description LogsfailureofprogrammingingressfieldprocessorforaCOPPclass.
EventID:1508
| Message  | Failed | to program egress | rule for | <class> |
| -------- | ------ | ----------------- | -------- | ------- |
| Category | CoPP   |                   |          |         |
| Severity | Error  |                   |          |         |
Description LogsfailureofprogrammingegressfieldprocessorforaCOPPclass.
EventID:1509
| Message     | CoPP initial                                 | initialization | failed | on slot <slot> |
| ----------- | -------------------------------------------- | -------------- | ------ | -------------- |
| Category    | CoPP                                         |                |        |                |
| Severity    | Error                                        |                |        |                |
| Description | LogsCoPPinitialinitializationfailureonaslot. |                |        |                |
EventID:1510
| Message | CoPP final | initialization | failed | on slot <slot> |
| ------- | ---------- | -------------- | ------ | -------------- |
CoPPevents|45

| Category    | CoPP                                       |     |     |
| ----------- | ------------------------------------------ | --- | --- |
| Severity    | Error                                      |     |     |
| Description | LogsCoPPfinalinitializationfailureonaslot. |     |     |
EventID:1511
| Message     | CoPP deinitialization                   | failed | on slot <slot> |
| ----------- | --------------------------------------- | ------ | -------------- |
| Category    | CoPP                                    |        |                |
| Severity    | Error                                   |        |                |
| Description | LogsCoPPdeinitializationfailureonaslot. |        |                |
EventID:1512
Message Failed to configure hardware for CoPP on slot <slot> class <class>
| Category | CoPP  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description LogsfailurewhileconfiguringhardwareonaslotforaCoPPclass.
EventID:1513
Message Failed to retrieve CoPP statistics from slot <slot> class <class>
| Category | CoPP  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description LogsfailurewhileretrievingstatisticsonaslotforaCoPPclass.
46
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 19

CPU_RX events

CPU_RX events

The following are the events related to CPU_RX.

Event ID: 7501

Message

Kernel filter "<action>" failed on unit <unit> for <filter_description>

Category

CPU_RX

Severity

Information

Description

Event raised when a kernel filter cannot be created or deleted

Event ID: 7502

Message

Cannot create kernel filter on unit <unit> for <filter_description>.
All filters are in use. Configuring fewer per-port features can help
with this issue.

Category

CPU_RX

Severity

Error

Description

Event raised when a kernel filter cannot be created because all filters are in use

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

47

Chapter 20
|            |         |        |     | Credential | Manager | events |
| ---------- | ------- | ------ | --- | ---------- | ------- | ------ |
| Credential | Manager | events |     |            |         |        |
Thefollowingaretheeventsrelatedtocredentialmanager.
EventID:6501(Severity:Warning)
Message An internal error occurred while reading the export password and
|          |     | default export    | password was | used instead. |     |     |
| -------- | --- | ----------------- | ------------ | ------------- | --- | --- |
| Category |     | CredentialManager |              |               |     |     |
| Severity |     | Warning           |              |               |     |     |
Description Warnstheuserthatexportpasswordfilewascorruptedanddefaultpasswdwasused
instead.
EventID:6502(Severity:Warning)
Message A critical system file has been corrupted. Please configure your export
password to the one used by your most recent configuration export and
|          |     | import your       | most recent configuration. |     |     |     |
| -------- | --- | ----------------- | -------------------------- | --- | --- | --- |
| Category |     | CredentialManager |                            |     |     |     |
| Severity |     | Warning           |                            |     |     |     |
Description Warnstheuserthatthechassissecrethasbeencorrupted.
EventID:6504
Message Self-signed certificate successfully created for the https-server.
| Category |     | CredentialManager |     |     |     |     |
| -------- | --- | ----------------- | --- | --- | --- | --- |
| Severity |     | Information       |     |     |     |     |
Description Logsamessagewhentheself-signedcertiscreatedbycredmgr.
EventID:6505
| Message  |     | User admin password | changed | from ServiceOS |     |     |
| -------- | --- | ------------------- | ------- | -------------- | --- | --- |
| Category |     | CredentialManager   |         |                |     |     |
| Severity |     | Information         |         |                |     |     |
Description LogsamessagewhenauserchangesadminpasswordfromServiceOS
EventID:6506
48
| AOS-CXEventLogMessageReferenceGuide10.09| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

| Message  | SSH authorized    | keys | were added | for user <user> |     |
| -------- | ----------------- | ---- | ---------- | --------------- | --- |
| Category | CredentialManager |      |            |                 |     |
| Severity | Information       |      |            |                 |     |
Description LogsamessagewhenSSHauthorizedkeysareaddedforauser
EventID:6507
| Message  | Failed            | to write SSH | authorized | keys for user | <user> |
| -------- | ----------------- | ------------ | ---------- | ------------- | ------ |
| Category | CredentialManager |              |            |               |        |
| Severity | Error             |              |            |               |        |
Description LogsamessageafterafailuretowriteSSHauthorizedkeysforauser
EventID:6508
| Message  | SSH authorized    | keys | deleted | for user <user> |     |
| -------- | ----------------- | ---- | ------- | --------------- | --- |
| Category | CredentialManager |      |         |                 |     |
| Severity | Information       |      |         |                 |     |
Description LogsamessageaftedeletingSSHauthorizedkeysforauser
EventID:6509
Message User <user> has configured an invalid SSH authorized key with key
|          | identifier        | <key-id> |     |     |     |
| -------- | ----------------- | -------- | --- | --- | --- |
| Category | CredentialManager |          |     |     |     |
| Severity | Error             |          |     |     |     |
Description LogsamessagewhenSSHauthorizedkeyfailsvalidationchack
CredentialManagerevents|49

Chapter 21

Device fingerprinting events

Device fingerprinting events

The following are the events related to device fingerprinting.

Event ID: 12401 (Severity: Warning)

Message

Reached the maximum number of clients limit on the switch for device
fingerprinting.

Category

Device fingerprinting

Severity

Warning

Description

Log the event when the maximum client limit for device fingerprinting is reached on the
switch.

Event ID: 12402 (Severity: Warning)

Message

Reached the maximum clients limit of <client_limit> on the interface
<interface> for device fingerprinting.

Category

Device fingerprinting

Severity

Warning

Description

Log the event when the per port clients limit for device fingerprinting is reached.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

50

Chapter 22
DHCP Relay events
| DHCP Relay events |     |     |
| ----------------- | --- | --- |
ThefollowingaretheeventsrelatedtoDHCPrelay.
EventID:3401
| Message  | DHCP Relay  | Enabled |
| -------- | ----------- | ------- |
| Category | DHCPRelay   |         |
| Severity | Information |         |
Description ThiscommandenablestheDHCPRelayfeatureinthedevice.
EventID:3402
| Message  | DHCP Relay  | Disabled |
| -------- | ----------- | -------- |
| Category | DHCPRelay   |          |
| Severity | Information |          |
Description ThiscommanddisablestheDHCPRelayfeatureinthedevice.
51
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 23

DHCP server events

DHCP server events

The following are the events related to DHCP server.

Event ID: 1901

Message

DHCP Lease added <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Information

Description

Logs DHCP lease addition

Event ID: 1902

Message

DHCP Lease deleted <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Information

Description

Logs DHCP lease deletion

Event ID: 1903

Message

DHCP Lease updated <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Information

Description

Logs DHCP lease updation

Event ID: 1904

Message

DHCP Lease addition failed <expiry_time> <mac> <ip> <host> <client_id>

Category

DHCP server

Severity

Error

Description

Logs failure in DHCP lease addition

Event ID: 1905

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

52

Message DHCP Lease deletion failed <expiry_time> <mac> <ip> <host> <client_id>
| Category    | DHCPserver                     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | LogsfailureinDHCPleasedeletion |     |     |     |
EventID:1906
Message DHCP Lease update failed <expiry_time> <mac> <ip> <host> <client_id>
| Category    | DHCPserver                     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | LogsfailureinDHCPleaseupdation |     |     |     |
EventID:1907
| Message     | DHCP server                                  | enabled | on VRF <vrf_name> |     |
| ----------- | -------------------------------------------- | ------- | ----------------- | --- |
| Category    | DHCPserver                                   |         |                   |     |
| Severity    | Information                                  |         |                   |     |
| Description | EventraisedwhenDHCPservergetsenabledontheVRF |         |                   |     |
EventID:1908
| Message     | DHCP server                                   | disabled | on VRF <vrf_name> |     |
| ----------- | --------------------------------------------- | -------- | ----------------- | --- |
| Category    | DHCPserver                                    |          |                   |     |
| Severity    | Information                                   |          |                   |     |
| Description | EventraisedwhenDHCPservergetsdisabledontheVRF |          |                   |     |
EventID:1909
Message Invalid DHCP configuration: <config> provided on DHCP Server instance
|          | running    | on VRF <vrf_name>. | Ignoring this | config. |
| -------- | ---------- | ------------------ | ------------- | ------- |
| Category | DHCPserver |                    |               |         |
| Severity | Error      |                    |               |         |
Description EventraisedwhenuserconfiguresaninvalidDHCPconfiguration
EventID:1910
DHCPserverevents|53

| Message     | DHCP Server                                     | Lease cleared | on vrf <vrf>. |
| ----------- | ----------------------------------------------- | ------------- | ------------- |
| Category    | DHCPserver                                      |               |               |
| Severity    | Information                                     |               |               |
| Description | EventraisedwhenDHCPServerLeaseontheVRFiscleared |               |               |
EventID:1911
| Message  | DHCPv6 Server | Lease cleared | on vrf <vrf>. |
| -------- | ------------- | ------------- | ------------- |
| Category | DHCPserver    |               |               |
| Severity | Information   |               |               |
Description EventraisedwhenDHCPv6ServerLeaseontheVRFiscleared
54
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Chapter 24
|        |          |        | DHCPv4 | snooping | events |
| ------ | -------- | ------ | ------ | -------- | ------ |
| DHCPv4 | snooping | events |        |          |        |
ThefollowingaretheeventsrelatedtoDHCPv4snooping.
EventID:8201(Severity:Warning)
Message Server <ip_address> packet received on untrusted port <port> dropped.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhileserverpacketreceivedonuntrustedport.
EventID:8202(Severity:Warning)
Message Client packet destined to untrusted port <port> dropped.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketdroppedwhilepacketdestinedtountrustedport.
EventID:8203(Severity:Warning)
Message Packet received from unauthorized server <ip_address> on port <port>.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhilepacketreceivedfromunauthorizedserver.
EventID:8204(Severity:Warning)
Message Received untrusted relay info from client <mac> on port <port>.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketreceivedwithuntrustedrelayinfo.
EventID:8205(Severity:Warning)
55
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

Client address <client_mac> not equal to source MAC <source_mac>
detected on port <port>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when client address not equal to source MAC.

Event ID: 8206 (Severity: Warning)

Message

Binding for <ip_address>:<mac> exists on port <existing_port>. Dropping
release request received for the binding on <new_port>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when release packet received on incorrect port.

Event ID: 8207 (Severity: Warning)

Message

The dynamic binding for <mac> on port <port> was replaced with a manual
binding.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when dynamic binding for a port was replaced with a manual binding.

Event ID: 8208 (Severity: Warning)

Message

Drop request from <mac> for already assigned address <ip_address>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when drop client request for already assigned ip.

Event ID: 8209 (Severity: Warning)

Message

Drop offer from <server_ip_address> of already assigned address <lease_
ip_address> to <mac>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when drop server offer for already assigned ip.

Event ID: 8210 (Severity: Warning)

DHCPv4 snooping events | 56

Message Drop offer from <server_ip_address> of <lease_ip_address> address is
illegal.
| Category    | DHCPv4snooping                           |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Warning                                  |     |     |
| Description | Logeventwhendropserverofferforillegalip. |     |     |
EventID:8211(Severity:Warning)
Message Maximum bindings limit reached on port <port>, dropping request from
<mac>.
| Category    | DHCPv4snooping                         |     |     |
| ----------- | -------------------------------------- | --- | --- |
| Severity    | Warning                                |     |     |
| Description | Logeventwhenbindinglimitreachedonport. |     |     |
EventID:8212
| Message     | All the dynamic                                 | binding entries | were cleared. |
| ----------- | ----------------------------------------------- | --------------- | ------------- |
| Category    | DHCPv4snooping                                  |                 |               |
| Severity    | Information                                     |                 |               |
| Description | Logeventwhenalldynamicbindingentriesarecleared. |                 |               |
EventID:8213
Message Dynamic binding entries on the port <port> were cleared.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhenalldynamicbindingentriesonaportarecleared.
EventID:8214
Message Dynamic binding entries on the VLAN <vid> were cleared.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhenalldynamicbindingentriesonavlanarecleared.
EventID:8215
57
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Message Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhenaspecificdynamicbindingentryonavlaniscleared.
EventID:8216
Message Failed to import dynamic ip binding entries from external storage.
|          | volume: <volume_name>, |     | filename: <file_name>. |
| -------- | ---------------------- | --- | ---------------------- |
| Category | DHCPv4snooping         |     |                        |
| Severity | Error                  |     |                        |
Description Logeventwhenfailedtoimportdynamicipbindingentriesfromexternalstorage.
EventID:8217
Message Failed to import dynamic ip binding entries from local storage.
|          | filepath: <file_path>. |     |     |
| -------- | ---------------------- | --- | --- |
| Category | DHCPv4snooping         |     |     |
| Severity | Error                  |     |     |
Description Logeventwhenfailedtoimportdynamicipbindingentriesfromlocalstorage.
EventID:8218(Severity:Warning)
| Message  | Flash-storage  | is active | for DHCPv4-Snooping. |
| -------- | -------------- | --------- | -------------------- |
| Category | DHCPv4snooping |           |                      |
| Severity | Warning        |           |                      |
Description Logeventwhenflash-storagebecomesactiveafterexternal-storageunconfiguration.
EventID:8219
Message Successfully imported <bindings_imported> dynamic ip binding entries
from external storage. volume: <volume_name>, filename: <file_name>.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhendynamicipbindingentriesfromexternalstoragearesuccessfully
imported.
EventID:8220
DHCPv4snoopingevents|58

Message

Successfully imported <bindings_imported> dynamic ip binding entries
from local storage.

Category

DHCPv4 snooping

Severity

Information

Description

Log event when dynamic ip binding entries from local storage are successfully imported.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

59

Chapter 25
DHCPv6 Relay events
| DHCPv6 Relay | events |     |
| ------------ | ------ | --- |
ThefollowingaretheeventsrelatedtoDHCPv6relay.
EventID:3301
| Message  | DHCPv6 Relay | Enabled |
| -------- | ------------ | ------- |
| Category | DHCPv6Relay  |         |
| Severity | Information  |         |
Description ThiscommandenablestheDHCPv6Relayfeatureinthedevice.
EventID:3302
| Message  | DHCPv6 Relay | Disabled |
| -------- | ------------ | -------- |
| Category | DHCPv6Relay  |          |
| Severity | Information  |          |
Description ThiscommanddisablestheDHCPv6Relayfeatureinthedevice.
60
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 26
|        |          |        | DHCPv6 | snooping | events |
| ------ | -------- | ------ | ------ | -------- | ------ |
| DHCPv6 | snooping | events |        |          |        |
ThefollowingaretheeventsrelatedtoDHCPv6snooping.
EventID:8301(Severity:Warning)
Message Server <ipv6_address> packet received on untrusted port <port> dropped.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhileserverpacketreceivedonuntrustedport.
EventID:8302(Severity:Warning)
Message Client packet destined to untrusted port <port> dropped.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketdroppedwhilepacketdestinedtountrustedport.
EventID:8303(Severity:Warning)
Message Packet received from unauthorized server <ipv6_address> on port <port>.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhilepacketreceivedfromunauthorizedserver.
EventID:8304(Severity:Warning)
Message Received untrusted relay info from client <mac> on port <port>.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketreceivedwithuntrustedrelayinfo.
EventID:8305(Severity:Warning)
61
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message Binding for <ipv6_address>:<mac> exists on port <existing_port>.
|          | Dropping release | request received | for the binding | on <new_port>. |
| -------- | ---------------- | ---------------- | --------------- | -------------- |
| Category | DHCPv6snooping   |                  |                 |                |
| Severity | Warning          |                  |                 |                |
Description Logeventwhenreleasepacketreceivedonincorrectport.
EventID:8306(Severity:Warning)
Message The dynamic binding for <mac> on port <port> was replaced with a manual
binding.
| Category | DHCPv6snooping |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Warning        |     |     |     |
Description Logeventwhendynamicbindingforaportwasreplacedwithamanualbinding.
EventID:8307(Severity:Warning)
Message Drop request from <mac> for already assigned address <ipv6_address>.
| Category | DHCPv6snooping |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Warning        |     |     |     |
Description Logeventwhendropclientrequestforalreadyassignedip.
EventID:8308(Severity:Warning)
Message Maximum bindings limit reached on port <port>, dropping request from
<mac>.
| Category    | DHCPv6snooping                         |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- |
| Severity    | Warning                                |     |     |     |
| Description | Logeventwhenbindinglimitreachedonport. |     |     |     |
EventID:8309
| Message     | All the dynamic                                 | binding entries | were cleared. |     |
| ----------- | ----------------------------------------------- | --------------- | ------------- | --- |
| Category    | DHCPv6snooping                                  |                 |               |     |
| Severity    | Information                                     |                 |               |     |
| Description | Logeventwhenalldynamicbindingentriesarecleared. |                 |               |     |
EventID:8310
DHCPv6snoopingevents|62

Message

Dynamic binding entries on the port <port> were cleared.

Category

DHCPv6 snooping

Severity

Information

Description

Log event when all dynamic binding entries on a port are cleared.

Event ID: 8311

Message

Dynamic binding entries on the VLAN <vid> were cleared.

Category

DHCPv6 snooping

Severity

Information

Description

Log event when all dynamic binding entries on a vlan are cleared.

Event ID: 8312

Message

Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.

Category

DHCPv6 snooping

Severity

Information

Description

Log event when a specific dynamic binding entry on a vlan is cleared.

Event ID: 8313

Message

Failed to import dynamic ip binding entries from external storage.
volume":" <volume_name>, filename":" <file_name>.

Category

DHCPv6 snooping

Severity

Error

Description

Log event when import of dynamic binding entries from external storage is failed.

Event ID: 8314

Message

Failed to import dynamic ip binding entries from local storage.
filepath":" <file_path>.

Category

DHCPv6 snooping

Severity

Error

Description

Log event when import of dynamic binding entries from local storage is failed.

Event ID: 8315 (Severity: Warning)

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

63

| Message  | Flash-storage  | is active | for DHCPv6-Snooping. |
| -------- | -------------- | --------- | -------------------- |
| Category | DHCPv6snooping |           |                      |
| Severity | Warning        |           |                      |
Description Logeventwhenflash-storagebecomesactiveafterexternal-storageunconfiguration.
EventID:8316
Message Successfully imported <bindings_imported> dynamic ip binding entries
from external storage. volume: <volume_name>, filename: <file_name>.
| Category | DHCPv6snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhendynamicipbindingentriesfromexternalstoragearesuccessfully
imported.
EventID:8317
Message Successfully imported <bindings_imported> dynamic ip binding entries
|          | from local     | storage. |     |
| -------- | -------------- | -------- | --- |
| Category | DHCPv6snooping |          |     |
| Severity | Information    |          |     |
Description Logeventwhendynamicipbindingentriesfromlocalstoragearesuccessfullyimported.
DHCPv6snoopingevents|64

Chapter 27
|     |     |     | Dicovery | and Capability | Exchange |
| --- | --- | --- | -------- | -------------- | -------- |
(DCBx) events
| Dicovery | and Capability | Exchange | (DCBx) | events |     |
| -------- | -------------- | -------- | ------ | ------ | --- |
ThefollowingaretheeventsrelatedtoDCBx.
EventID:9201
| Message     |     | DCBX Enabled                        |     |     |     |
| ----------- | --- | ----------------------------------- | --- | --- | --- |
| Category    |     | DicoveryandCapabilityExchange(DCBx) |     |     |     |
| Severity    |     | Information                         |     |     |     |
| Description |     | LogseventwhenDCBXisgloballyenabled  |     |     |     |
EventID:9202
| Message     |     | DCBX Disabled                       |     |     |     |
| ----------- | --- | ----------------------------------- | --- | --- | --- |
| Category    |     | DicoveryandCapabilityExchange(DCBx) |     |     |     |
| Severity    |     | Information                         |     |     |     |
| Description |     | LogeventwhenDCBXisgloballydisabled  |     |     |     |
EventID:9203
| Message     |     | DCBX is enabled                         | on interface | <intf_name> |     |
| ----------- | --- | --------------------------------------- | ------------ | ----------- | --- |
| Category    |     | DicoveryandCapabilityExchange(DCBx)     |              |             |     |
| Severity    |     | Information                             |              |             |     |
| Description |     | LogeventwhenDCBXisenabledontheinterface |              |             |     |
EventID:9204
| Message     |     | DCBX is disabled                         | on interface | <intf_name> |     |
| ----------- | --- | ---------------------------------------- | ------------ | ----------- | --- |
| Category    |     | DicoveryandCapabilityExchange(DCBx)      |              |             |     |
| Severity    |     | Information                              |              |             |     |
| Description |     | LogeventwhenDCBXisdisabledontheinterface |              |             |     |
EventID:9205
65
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

| Message     | DCBX status                                     | active | on interface | <intf_name> |
| ----------- | ----------------------------------------------- | ------ | ------------ | ----------- |
| Category    | DicoveryandCapabilityExchange(DCBx)             |        |              |             |
| Severity    | Information                                     |        |              |             |
| Description | LogeventwhenDCBXoperstatusisactiveonaninterface |        |              |             |
EventID:9206
| Message  | DCBX status                         | inactive | on interface | <intf_name> |
| -------- | ----------------------------------- | -------- | ------------ | ----------- |
| Category | DicoveryandCapabilityExchange(DCBx) |          |              |             |
| Severity | Information                         |          |              |             |
Description LogeventwhenDCBXoperstatusisinactiveonaninterface
EventID:9207
| Message     | PFC TLV status                            | active | on interface | <intf_name> |
| ----------- | ----------------------------------------- | ------ | ------------ | ----------- |
| Category    | DicoveryandCapabilityExchange(DCBx)       |        |              |             |
| Severity    | Information                               |        |              |             |
| Description | LogeventwhenPFCTLVsareactiveonaninterface |        |              |             |
EventID:9208
| Message     | PFC TLV status                              | inactive | on interface | <intf_name> |
| ----------- | ------------------------------------------- | -------- | ------------ | ----------- |
| Category    | DicoveryandCapabilityExchange(DCBx)         |          |              |             |
| Severity    | Information                                 |          |              |             |
| Description | LogeventwhenPFCTLVsareinactiveonaninterface |          |              |             |
EventID:9209(Severity:Warning)
Message PFC TLV status priority mismatch on interface <intf_name>
| Category | DicoveryandCapabilityExchange(DCBx) |     |     |     |
| -------- | ----------------------------------- | --- | --- | --- |
| Severity | Warning                             |     |     |     |
Description LogeventwhenthereisPFCTLVprioritymismatchonaninterface
DicoveryandCapabilityExchange(DCBx)events|66

Chapter 28
DNS client events
| DNS client events |     |     |
| ----------------- | --- | --- |
ThefollowingaretheeventsrelatedtoDNSclient.
EventID:11901
| Message     | <type> event                       | for VRF <vrf_name> |
| ----------- | ---------------------------------- | ------------------ |
| Category    | DNSclient                          |                    |
| Severity    | Information                        |                    |
| Description | EventreportedwhenDNSeventtriggered |                    |
67
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 29

Dot1x supplicant events

Dot1x supplicant events

The following are the events related to dot1x supplicant.

Event ID: 12301

Message

802.1X supplicant has blocked the interface <ifname>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant is blocking the interface on the data-plane.

Event ID: 12302

Message

802.1X supplicant has unblocked the interface <ifname>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant is opening the interface on the data-plane.

Event ID: 12303

Message

802.1X supplicant PAE restarted on interface <ifname> due to change in
policy <policy>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant PAE is restarted due to a change in the policy used on the interface.

Event ID: 12304

Message

802.1X supplicant is not supported on the port <port>.

Category

Dot1x supplicant

Severity

Information

Description

The 802.1X supplicant is enabled on a port that is not supported (Ex: LAG, ROP).

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

68

Chapter 30
DPSE events
DPSE events
ThefollowingaretheeventsrelatedtoDPSE.
EventID:10901(Severity:Critical)
Message Line card module <linecard_name> triggered backplane sequence recovery
| Category | DPSE     |     |     |
| -------- | -------- | --- | --- |
| Severity | Critical |     |     |
Description Alinecardhitabackplanesequenceerrorthattriggeredarecoveryoperation
EventID:10902
| Message  | HA event triggered | backplane | sequence recovery |
| -------- | ------------------ | --------- | ----------------- |
| Category | DPSE               |           |                   |
| Severity | Information        |           |                   |
Description AbackplanesequenceresetwastriggeredduetoanHAevent
EventID:10903
| Message  | HA event completed | backplane | sequence recovery |
| -------- | ------------------ | --------- | ----------------- |
| Category | DPSE               |           |                   |
| Severity | Information        |           |                   |
Description ThesystemcompletedabackplanesequenceresettriggeredbyanHAevent
EventID:10904(Severity:Critical)
Message Line card module <linecard_name> completed backplane sequence recovery
| Category | DPSE     |     |     |
| -------- | -------- | --- | --- |
| Severity | Critical |     |     |
Description Thesystemcompletedbackplanesequencerecoverytriggeredbylinecarderror
EventID:10905
69
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | No active                                   | modules have | been detected | in the system. |
| ----------- | ------------------------------------------- | ------------ | ------------- | -------------- |
| Category    | DPSE                                        |              |               |                |
| Severity    | Information                                 |              |               |                |
| Description | Noactivemoduleshavebeendetectedinthesystem. |              |               |                |
EventID:10906(Severity:Critical)
Message Control Plane (<operation_name>) failure during (<plugin_name>)
configuration
| Category    | DPSE                                          |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Critical                                      |     |     |     |
| Description | Anops-switchdpluginfailedexecutinganoperation |     |     |     |
DPSEevents|70

Chapter 31
ECMP events
ECMP events
ThefollowingaretheeventsrelatedtoECMP.
EventID:1801
Message Failed to update ecmp object for route <route>, error: <err>
| Category    | ECMP                              |     |     |
| ----------- | --------------------------------- | --- | --- |
| Severity    | Error                             |     |     |
| Description | logserrorswhilecreatingecmpgroup. |     |     |
EventID:1802
| Message     | Update ecmp                 | object for | route <route> |
| ----------- | --------------------------- | ---------- | ------------- |
| Category    | ECMP                        |            |               |
| Severity    | Information                 |            |               |
| Description | logswhilecreatingecmpgroup. |            |               |
EventID:1803
Message Failed to delete ecmp egress object <egressid>, error: <err>
| Category    | ECMP                              |     |     |
| ----------- | --------------------------------- | --- | --- |
| Severity    | Error                             |     |     |
| Description | logserrorswhiledeletingecmpgroup. |     |     |
EventID:1804
| Message     | Delete ecmp                 | egress object | <egressid> |
| ----------- | --------------------------- | ------------- | ---------- |
| Category    | ECMP                        |               |            |
| Severity    | Information                 |               |            |
| Description | logswhiledeletingecmpgroup. |               |            |
EventID:1805
71
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

ECMP error: <err>

Category

Severity

ECMP

Error

Description

logs for ECMP setup errors.

ECMP events | 72

Chapter 32
ERPS events
ERPS events
ThefollowingaretheeventsrelatedtoERPS.
EventID:8501(Severity:Warning)
Message Expected R-APS packets not received on <ifID> in ring <ringID> with
|          | control VLAN | <ccvlan> |     |
| -------- | ------------ | -------- | --- |
| Category | ERPS         |          |     |
| Severity | Warning      |          |     |
Description LogeventwhenRAPSmessagesarenotreceivedforacertaintimeinterval
EventID:8502(Severity:Warning)
Message Misconfiguration detected on ring <ringID> with control VLAN <ccvlan>.
Another node in the ring with mac <node> is also operating as an RPL
owner
| Category    | ERPS                                     |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Warning                                  |     |     |
| Description | Logeventwhenaringmisconfigurationhappens |     |     |
EventID:8503
Message Operational state of the ring <ringID>, instance <instanceID> changed
to <state>
| Category    | ERPS                             |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | Logstatetransitionofringinstance |     |     |
EventID:8504
| Message     | <interfaceName>                             | is not | an L2 port |
| ----------- | ------------------------------------------- | ------ | ---------- |
| Category    | ERPS                                        |        |            |
| Severity    | Information                                 |        |            |
| Description | Logeventwhenringisconfiguredwithanon-L2port |        |            |
73
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Event ID: 8505

Message

<interfaceName> is already associated with <portName> of ERPS ring
<ringID>

Category

ERPS

Severity

Information

Description

Log event when an interface which is already associated to a ring port is getting mapped
to other ring port as well

Event ID: 8506

Message

Configured control-channel VLAN <ccVlan> is already protected by ERPS
ring <ringID>, instance <instanceID>

Category

ERPS

Severity

Information

Description

Log event when control-channel VLAN is part of the protected-vlans

Event ID: 8507

Message

VLAN <ccVlan> is already configured as control-channel for instance
<instanceID> of ring <ringID>

Category

ERPS

Severity

Information

Description

Log event when control-channel VLAN overlaps with another control-channel of same ring

Event ID: 8508

Message

Vlan <dataVlan> is already part of the protected VLAN set of ring
<ringID> instance <instanceID>

Category

ERPS

Severity

Information

Description

Log event when protected-vlan(s) overlap

Event ID: 8509

Message

Control VLAN must not be same on parent and sub rings

Category

ERPS

Severity

Information

Description

Log event when same control-channel VLAN is configured on both major and sub-rings

ERPS events | 74

EventID:8510
| Message  | Parent-ring | <ringID> | is same as sub-ring |
| -------- | ----------- | -------- | ------------------- |
| Category | ERPS        |          |                     |
| Severity | Information |          |                     |
Description Logeventwhenparent-ringidisconfiguredtobethesameassub-ring
EventID:8511
Message VLAN <vlanID> in the protected VLANs list is also configured as the
control-channel
| Category | ERPS        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogeventwhenVLANfromtheprotected-vlanslistisalreadyconfiguredascontrol-
channelVLAN
EventID:8512
Message <portName> is already configured as RPL port for instance <instanceID>
| Category | ERPS        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogeventifthesameringportisconfiguredasRPLportformorethanoneinstance
EventID:8513
Message RPL configuration is not allowed on ISL port <interfaceName>
| Category | ERPS        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogeventifringportwhichisalsoanISLisbeingconfiguredasRPL
EventID:8514
Message Protected VLAN set of instance in sub-ring should map to same instance
|          | in the parent | ring |     |
| -------- | ------------- | ---- | --- |
| Category | ERPS          |      |     |
| Severity | Information   |      |     |
Description Logeventifprotected-vlansetofsub-ringisnotasubsetofthemajor-ring
EventID:8515
75
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Message

Operational state of the ring <ringID>, instance <instanceID> changed
to Initializing with reason <reason>

Category

ERPS

Severity

Information

Description

Log transition of state of ring instance to initializing and the reason for it

ERPS events | 76

Chapter 33
EVPN events
EVPN events
ThefollowingaretheeventsrelatedtoEVPN.
EventID:9501
| Message     | EVPN EVI:               | <evi> created |     |
| ----------- | ----------------------- | ------------- | --- |
| Category    | EVPN                    |               |     |
| Severity    | Information             |               |     |
| Description | LogsEVPNEVIcreateevent. |               |     |
EventID:9502
| Message     | EVPN EVI:               | <evi> deleted |     |
| ----------- | ----------------------- | ------------- | --- |
| Category    | EVPN                    |               |     |
| Severity    | Information             |               |     |
| Description | LogsEVPNEVIdeleteevent. |               |     |
EventID:9503
| Message     | EVPN RD:                       | <rd> updated for | EVI: <evi> |
| ----------- | ------------------------------ | ---------------- | ---------- |
| Category    | EVPN                           |                  |            |
| Severity    | Information                    |                  |            |
| Description | LogsEVPNRDupdateeventforanEVI. |                  |            |
EventID:9504
| Message     | EVPN RD                        | deleted for EVI: | <evi> |
| ----------- | ------------------------------ | ---------------- | ----- |
| Category    | EVPN                           |                  |       |
| Severity    | Information                    |                  |       |
| Description | LogsEVPNRDdeleteeventforanEVI. |                  |       |
EventID:9505
77
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | EVPN RT:                       | <rt> created | for EVI: | <evi> |
| ----------- | ------------------------------ | ------------ | -------- | ----- |
| Category    | EVPN                           |              |          |       |
| Severity    | Information                    |              |          |       |
| Description | LogsEVPNRTcreateeventforanEVI. |              |          |       |
EventID:9506
| Message     | EVPN RT:                       | <rt> deleted | for EVI: | <evi> |
| ----------- | ------------------------------ | ------------ | -------- | ----- |
| Category    | EVPN                           |              |          |       |
| Severity    | Information                    |              |          |       |
| Description | LogsEVPNRTdeleteeventforanEVI. |              |          |       |
EventID:9507
| Message     | EVPN RT:                       | <rt> updated | for EVI: | <evi> |
| ----------- | ------------------------------ | ------------ | -------- | ----- |
| Category    | EVPN                           |              |          |       |
| Severity    | Information                    |              |          |       |
| Description | LogsEVPNRTupdateeventforanEVI. |              |          |       |
EventID:9508
| Message     | VNI: <vni>               | is added | for EVPN Peer | VTEP: <vtep_ip> |
| ----------- | ------------------------ | -------- | ------------- | --------------- |
| Category    | EVPN                     |          |               |                 |
| Severity    | Information              |          |               |                 |
| Description | LogsEVPNVTEPVNIaddevent. |          |               |                 |
EventID:9509
| Message     | VNI: <vni>                  | is deleted | for EVPN | Peer VTEP: <vtep_ip> |
| ----------- | --------------------------- | ---------- | -------- | -------------------- |
| Category    | EVPN                        |            |          |                      |
| Severity    | Information                 |            |          |                      |
| Description | LogsEVPNVTEPVNIdeleteevent. |            |          |                      |
EventID:9510
Message EVPN static MAC conflict <action>, MAC: <mac_addr>, IP address: <ip_
|     | addr>, VTEP: | <vtep_ip> |     |     |
| --- | ------------ | --------- | --- | --- |
EVPNevents|78

| Category    | EVPN                            |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- |
| Severity    | Error                           |     |     |     |
| Description | LogsEVPNstaticMACconflictevent. |     |     |     |
EventID:9511
| Message     | EVPN static                     | MAC conflict | <action>, | MAC: <mac_addr> |
| ----------- | ------------------------------- | ------------ | --------- | --------------- |
| Category    | EVPN                            |              |           |                 |
| Severity    | Error                           |              |           |                 |
| Description | LogsEVPNstaticMACconflictevent. |              |           |                 |
EventID:9512
Message EVPN duplicate MAC dampening <action>, MAC: <mac_addr>
| Category    | EVPN                                |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Error                               |     |     |     |
| Description | LogsEVPNduplicateMACdampeningevent. |     |     |     |
EventID:9513
| Message     | EVPN VRF:               | <vrf> created |     |     |
| ----------- | ----------------------- | ------------- | --- | --- |
| Category    | EVPN                    |               |     |     |
| Severity    | Information             |               |     |     |
| Description | LogsEVPNVRFcreateevent. |               |     |     |
EventID:9514
| Message     | EVPN VRF:               | <vrf> deleted |     |     |
| ----------- | ----------------------- | ------------- | --- | --- |
| Category    | EVPN                    |               |     |     |
| Severity    | Information             |               |     |     |
| Description | LogsEVPNVRFdeleteevent. |               |     |     |
EventID:9515
| Message  | EVPN RD: | <rd> updated | for VRF: <vrf> |     |
| -------- | -------- | ------------ | -------------- | --- |
| Category | EVPN     |              |                |     |
79
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Information               |     |     |
| ----------- | ------------------------- | --- | --- |
| Description | LogsEVPNVRFRDupdateevent. |     |     |
EventID:9516
| Message     | EVPN RT: <rt>             | created for | VRF: <vrf> |
| ----------- | ------------------------- | ----------- | ---------- |
| Category    | EVPN                      |             |            |
| Severity    | Information               |             |            |
| Description | LogsEVPNVRFRTcreateevent. |             |            |
EventID:9517
| Message     | EVPN RT: <rt>             | deleted for | VRF: <vrf> |
| ----------- | ------------------------- | ----------- | ---------- |
| Category    | EVPN                      |             |            |
| Severity    | Information               |             |            |
| Description | LogsEVPNVRFRTdeleteevent. |             |            |
EventID:9518
| Message     | EVPN RT: <rt>             | updated for | VRF: <vrf> |
| ----------- | ------------------------- | ----------- | ---------- |
| Category    | EVPN                      |             |            |
| Severity    | Information               |             |            |
| Description | LogsEVPNVRFRTupdateevent. |             |            |
EventID:9519
Message EVPN dynamic vxlan tunnel briding mode ibgp-ebgp enabled
| Category | EVPN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhendynamicvxlantunnelbridingmodeibgp-ebgpisenabled
EventID:9520
Message EVPN dynamic vxlan tunnel briding mode ibgp-ebgp disabled
| Category | EVPN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhendynamicvxlantunnelbridingmodeibgp-ebgpisdisabled
EVPNevents|80

Chapter 34
|                  |        |     | External | Storage | events |
| ---------------- | ------ | --- | -------- | ------- | ------ |
| External Storage | events |     |          |         |        |
Thefollowingaretheeventsrelatedtoexternalstorage.
EventID:7801
| Message     | Share <name>                      | mount failure' | throttle_count: | 10  |     |
| ----------- | --------------------------------- | -------------- | --------------- | --- | --- |
| Category    | ExternalStorage                   |                |                 |     |     |
| Severity    | Error                             |                |                 |     |     |
| Description | Eventraisedwhenasharefailstomount |                |                 |     |     |
EventID:7802
| Message     | Share <name>                         | dismount failure |     |     |     |
| ----------- | ------------------------------------ | ---------------- | --- | --- | --- |
| Category    | ExternalStorage                      |                  |     |     |     |
| Severity    | Error                                |                  |     |     |     |
| Description | Eventraisedwhenasharefailstodismount |                  |     |     |     |
EventID:7803
| Message     | Share <name>                | is mounted |     |     |     |
| ----------- | --------------------------- | ---------- | --- | --- | --- |
| Category    | ExternalStorage             |            |     |     |     |
| Severity    | Information                 |            |     |     |     |
| Description | Eventraisedwhenasharemounts |            |     |     |     |
EventID:7804
| Message     | Share <name>                   | is dismounted |     |     |     |
| ----------- | ------------------------------ | ------------- | --- | --- | --- |
| Category    | ExternalStorage                |               |     |     |     |
| Severity    | Information                    |               |     |     |     |
| Description | Eventraisedwhenasharedismounts |               |     |     |     |
EventID:7805
81
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message  | Share <name>    | mount is aborted |
| -------- | --------------- | ---------------- |
| Category | ExternalStorage |                  |
| Severity | Error           |                  |
Description Eventraisedwhenamounttimesoutorabortsduetoaconfigchange
EventID:7806
| Message     | USB device                   | <status>. |
| ----------- | ---------------------------- | --------- |
| Category    | ExternalStorage              |           |
| Severity    | Information                  |           |
| Description | USBdevicemountedorunmounted. |           |
ExternalStorageevents|82

Chapter 35
Fan events
Fan events
Thefollowingaretheeventsrelatedtofan.
EventID:201
Message There are <count> total fans in subsystem <subsystem>.
| Category    | Fan                                   |     |
| ----------- | ------------------------------------- | --- |
| Severity    | Information                           |     |
| Description | Logthetotalnumberoffansinthesubsystem |     |
EventID:202
Message Subsystem <subsystem> setting fan speed control register to <speedval>:
<value>.
| Category    | Fan               |     |
| ----------- | ----------------- | --- |
| Severity    | Information       |     |
| Description | Logthefanspeedset |     |
EventID:203
| Message     | Air flow direction:    | <value>. |
| ----------- | ---------------------- | -------- |
| Category    | Fan                    |          |
| Severity    | Information            |          |
| Description | Logtheairflowdirection |          |
EventID:204(Severity:Warning)
| Message     | Fan tray <FT_Name>                          | was removed. |
| ----------- | ------------------------------------------- | ------------ |
| Category    | Fan                                         |              |
| Severity    | Warning                                     |              |
| Description | Logeventwhenafantrayisremovedfromthechassis |              |
EventID:205
83
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Fan tray                                     | <FT_Name> was | inserted. |     |
| ----------- | -------------------------------------------- | ------------- | --------- | --- |
| Category    | Fan                                          |               |           |     |
| Severity    | Information                                  |               |           |     |
| Description | Logeventwhenafantrayisinsertedintothechassis |               |           |     |
EventID:206
| Message     | Fan module                                  | <FMod_Name> | was removed. |     |
| ----------- | ------------------------------------------- | ----------- | ------------ | --- |
| Category    | Fan                                         |             |              |     |
| Severity    | Information                                 |             |              |     |
| Description | Logeventwhenafanmoduleisremovedfromafantray |             |              |     |
EventID:207
| Message     | Fan module                                   | <FMod_Name> | was inserted. |     |
| ----------- | -------------------------------------------- | ----------- | ------------- | --- |
| Category    | Fan                                          |             |               |     |
| Severity    | Information                                  |             |               |     |
| Description | Logeventwhenafanmoduleisinsertedintoafantray |             |               |     |
EventID:208
Message Unsupported fan tray <FT_Name> detected. Please insert a standard fan
tray.
| Category    | Fan                                        |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Error                                      |     |     |     |
| Description | Logeventwhenanunsupportedfantrayisinserted |     |     |     |
EventID:209
Message Shutting down system now because <num_of_failure> <failure_type>
|          | <compare_mode> | limit | of <num_of_failure_limit>': | yes |
| -------- | -------------- | ----- | --------------------------- | --- |
| Category | Fan            |       |                             |     |
| Severity | Error          |       |                             |     |
Description Logerrorwhensystemshutdownisinitiatedduetocriticalfanfaults
EventID:211(Severity:Warning)
Fanevents|84

Message Shutting down system in <seconds> seconds because <num_of_failure>
|          | <failure_type> | <compare_mode> | limit of <num_of_failure_limit> |     |
| -------- | -------------- | -------------- | ------------------------------- | --- |
| Category | Fan            |                |                                 |     |
| Severity | Warning        |                |                                 |     |
Description Logerrorwhenthenumberoffailuresexceedtheallowablelimit
EventID:212(Severity:Warning)
| Message     | System                                  | shutdown timer is cancelled.': | yes |     |
| ----------- | --------------------------------------- | ------------------------------ | --- | --- |
| Category    | Fan                                     |                                |     |     |
| Severity    | Warning                                 |                                |     |     |
| Description | Logeventwhentheshutdowntimeriscancelled |                                |     |     |
EventID:213
| Message     | <num_of_failure>              | <failure_type> | in the system.': | yes |
| ----------- | ----------------------------- | -------------- | ---------------- | --- |
| Category    | Fan                           |                |                  |     |
| Severity    | Error                         |                |                  |     |
| Description | Logerrorwhentherearefanfaults |                |                  |     |
EventID:214
Message <function>: Fan <fan_name> faulted, reason: <reason>.': yes
| Category    | Fan                               |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Error                             |     |     |     |
| Description | Listoutthefaultyormissingfannames |     |     |     |
EventID:215
| Message     | <FanName>       | fan is <FanStatus>. |     |     |
| ----------- | --------------- | ------------------- | --- | --- |
| Category    | Fan             |                     |     |     |
| Severity    | Information     |                     |     |     |
| Description | Logthefanstatus |                     |     |     |
EventID:216
85
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message Status of fan <FanName> has changed from <OldStatus> to <NewStatus>.
| Category    | Fan                     |     |     |
| ----------- | ----------------------- | --- | --- |
| Severity    | Information             |     |     |
| Description | Logthechangeinfanstatus |     |     |
EventID:217(Severity:Warning)
Message Operational fan count below minimum. <FanCount> fans operating, but
|             | <FanMinimum> are                         | required. |     |
| ----------- | ---------------------------------------- | --------- | --- |
| Category    | Fan                                      |           |     |
| Severity    | Warning                                  |           |     |
| Description | Logwhenminimumnumberoffansarenotpresent. |           |     |
EventID:218
Message Fan speed index for thermal zone <ZoneIdx> is <FanSpdIdxStatus>.
| Category | Fan         |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logwhenthefanspeedindexchangestoandfromthemaximumforeachthermalzone
EventID:219
| Message     | Fan tray <FT_Name>                   | powered | <Status>. |
| ----------- | ------------------------------------ | ------- | --------- |
| Category    | Fan                                  |         |           |
| Severity    | Information                          |         |           |
| Description | Logeventwhenafantrayispoweredonoroff |         |           |
EventID:220
| Message  | Fan tray <FT_Name> | airflow | is <FT_Dir>. |
| -------- | ------------------ | ------- | ------------ |
| Category | Fan                |         |              |
| Severity | Information        |         |              |
Description Logeventwhenafantrayisinsertedspecifyingitsairflowdirection
EventID:221(Severity:Warning)
Message <FT_air_curr> airflow fan tray <FT_Name> unsupported; this system
Fanevents|86

requires <FT_air_req> airflow.

Category

Fan

Severity

Warning

Description

Log event when a fan tray airflow is not matching with system airflow

Event ID: 222

Message

Category

Severity

<num_of_failure> <failure_type> <compare_mode> limit of <num_of_
failure_limit>': yes

Fan

Error

Description

Log error when number of faulty/supported fans does not meet the allowable limit

Event ID: 223 (Severity: Warning)

Message

Fan tray <FT_Name> FRU EPPROM is incorrectly programmed.

Category

Fan

Severity

Warning

Description

Log when fan tray SKU ID in FRU is mismatched

Event ID: 224 (Severity: Warning)

Message

<FT_air_curr> airflow fan tray <FT_Name> disabled; this system requires
<FT_air_req> airflow.

Category

Fan

Severity

Warning

Description

Log event when a fan tray airflow is not matching with system airflow and is disabled

Event ID: 225 (Severity: Warning)

Message

fan tray <FT_Name> misconfigured; this fan tray has been <En_Dis>.

Category

Fan

Severity

Warning

Description

Log event when a misconfigured fan tray is enabled or disabled

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

87

Chapter 36
|               |        |     |     | Fault | monitor events |
| ------------- | ------ | --- | --- | ----- | -------------- |
| Fault monitor | events |     |     |       |                |
Thefollowingaretheeventsrelatedtofaultmonitor.
EventID:11101(Severity:Warning)
| Message     | Interface                                   | <interface>: | <fault> fault | detected': | yes |
| ----------- | ------------------------------------------- | ------------ | ------------- | ---------- | --- |
| Category    | Faultmonitor                                |              |               |            |     |
| Severity    | Warning                                     |              |               |            |     |
| Description | Logseventwhenafaultisdetectedonaninterface. |              |               |            |     |
EventID:11102(Severity:Warning)
Message Interface <interface>: <fault> fault detected and port disabled': yes
| Category | Faultmonitor |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- |
| Severity | Warning      |     |     |     |     |
Description Logseventandshutdowntheinterfacewhenafaultisdetectedonaninterface.
EventID:11103
Message Interface <interface>: <fault> fault re-enable time expired, port
|             | enabled':                             | yes |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- |
| Category    | Faultmonitor                          |     |     |     |     |
| Severity    | Information                           |     |     |     |     |
| Description | Interfaceisauto-enabledontimerexpiry. |     |     |     |     |
EventID:11104
Message Interface <interface>: <fault> fault disable cancelled due to
|             | configuration                                        | change': | yes |     |     |
| ----------- | ---------------------------------------------------- | -------- | --- | --- | --- |
| Category    | Faultmonitor                                         |          |     |     |     |
| Severity    | Information                                          |          |     |     |     |
| Description | Interfaceisauto-enabledonprofileconfigurationchange. |          |     |     |     |
EventID:11105
88
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

Admin state changed and interface: <interface> is auto-enabled': yes

Category

Fault monitor

Severity

Information

Description

Interface is auto-enabled on admin state change.

Event ID: 11106 (Severity: Warning)

Message

Interface <interface>: <fault> fault detected, port is already disabled
by another fault.': yes

Category

Fault monitor

Severity

Warning

Description

Logs event when disabling of a faulty interface failed.

Event ID: 11107

Message

MAC Lockout packet drop detected for <mac> as source address: <sa_diff_
count>.

Category

Fault monitor

Severity

Information

Description

Logs event when a packet drop is detected for MAC Lockout MAC as source address.

Event ID: 11108

Message

MAC Lockout packet drop detected for <mac> as destination address: <da_
diff_count>.

Category

Fault monitor

Severity

Information

Description

Logs event when a packet drop is detected for MAC Lockout MAC as destination address.

Event ID: 11109

Message

MAC Lockout packet drop detected for <mac> as source: <sa_diff_count>
and destination: <da_diff_count> address.

Category

Fault monitor

Severity

Information

Description

Logs event when a packet drop is detected for MAC Lockout.

Fault monitor events | 89

Chapter 37

Firmware Update events

Firmware Update events

The following are the events related to firmware update.

Event ID: 4401

Message

User <user>: <image_profile> image updated via <dnld_type> from <host>.
Firmware version, Before Update: <before> After Update: <after>

Category

Firmware Update

Severity

Information

Description

Indicates that the switch firmware was succesfully updated from a remote source

Event ID: 4402

Message

User <user>: <image_profile> image updated via <dnld_type>. Firmware
version, Before Update: <before> After Update: <after>

Category

Firmware Update

Severity

Information

Description

Indicates that the switch firmware was succesfully updated from a local source

Event ID: 4403

Message

User <user>: <image_profile> image update failed via <dnld_type> from
<host>

Category

Firmware Update

Severity

Error

Description

Indicates that a switch firmware update failed from a remote source

Event ID: 4404

Message

User <user>: <image_profile> image update failed via <dnld_type>

Category

Firmware Update

Severity

Error

Description

Indicates that a switch firmware update failed from a local source

Event ID: 4405

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

90

| Message  | Firmware image | signature | not valid |
| -------- | -------------- | --------- | --------- |
| Category | FirmwareUpdate |           |           |
| Severity | Error          |           |           |
Description Indicatesthatathesignatureverificationcheckduringswitchfirmwareupdatefailed
EventID:4406
| Message  | Firmware image | is not | compatible with hardware |
| -------- | -------------- | ------ | ------------------------ |
| Category | FirmwareUpdate |        |                          |
| Severity | Error          |        |                          |
Description Indicatesthatfirmwareimagedownloadedforupdateisnotcompatiblewithhardware
EventID:4407
| Message  | Firmware image | is invalid |     |
| -------- | -------------- | ---------- | --- |
| Category | FirmwareUpdate |            |     |
| Severity | Error          |            |     |
Description Indicatesthatimagedownloadedforupdateisnotaswitchimage
FirmwareUpdateevents|91

Hardware Health Monitor events

Chapter 38

Hardware Health Monitor events

The following are the events related to hardware health monitor.

Event ID: 3001

Message

Diagnostic <test_name> failed with error code <error_code> on
management module <slot>': yes

Category

Hardware Health Monitor

Severity

Error

Description

Event raised when hardware diagnostics detects error in management module

Event ID: 3002

Message

Diagnostic <test_name> failed with error code <error_code> on line card
<slot>': yes

Category

Hardware Health Monitor

Severity

Error

Description

Event raised when hardware diagnostics detects error in line card

Event ID: 3003

Message

Diagnostic <test_name> failed with error code <error_code> on fabric
card <slot>': yes

Category

Hardware Health Monitor

Severity

Error

Description

Event raised when hardware diagnostics detects error in fabric card

Event ID: 3004

Message

Diagnostic <test_name> failed with error code <error_code> on fan tray
<slot>': yes

Category

Hardware Health Monitor

Severity

Error

Description

Event raised when hardware diagnostics detects error in fan tray

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

92

EventID:3005
Message Diagnostic <test_name> failed with error code <error_code> on rear
|          | display               | card <slot>': | yes |     |     |
| -------- | --------------------- | ------------- | --- | --- | --- |
| Category | HardwareHealthMonitor |               |     |     |     |
| Severity | Error                 |               |     |     |     |
Description Eventraisedwhenhardwarediagnosticsdetectserrorinreardisplaycard
EventID:3006
Message Diagnostic <test_name> failed with error code <error_code> for the
|          | system':              | yes |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Category | HardwareHealthMonitor |     |     |     |     |
| Severity | Error                 |     |     |     |     |
Description Eventraisedwhenhardwarediagnosticsdetectserrorinthesystem
EventID:3007(Severity:Warning)
| Message     | There are             | <origin> | happening on | <location>': | yes |
| ----------- | --------------------- | -------- | ------------ | ------------ | --- |
| Category    | HardwareHealthMonitor |          |              |              |     |
| Severity    | Warning               |          |              |              |     |
| Description | LogsMCEBUSerror       |          |              |              |     |
EventID:3008(Severity:Warning)
| Message     | There are                         | IO errors | on <location> | from |     |
| ----------- | --------------------------------- | --------- | ------------- | ---- | --- |
|             | <seg>:<bus>:<device>:<function>': |           |               | yes  |     |
| Category    | HardwareHealthMonitor             |           |               |      |     |
| Severity    | Warning                           |           |               |      |     |
| Description | LogsMCEIOerror                    |           |               |      |     |
EventID:3009
| Message     | There are                                  | unknown | errors on <location> | from |     |
| ----------- | ------------------------------------------ | ------- | -------------------- | ---- | --- |
|             | <status>:<addr>:<misc>:<mcgstatus>:<cap>': |         |                      |      | yes |
| Category    | HardwareHealthMonitor                      |         |                      |      |     |
| Severity    | Information                                |         |                      |      |     |
| Description | LogsMCEunknownerror                        |         |                      |      |     |
HardwareHealthMonitorevents|93

Event ID: 3010 (Severity: Warning)

Message

CPUs <cpus> L<level> <type> cache error detected. CPUs <offlined>
offlined': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Logs CPU cache error

Event ID: 3011 (Severity: Warning)

Message

Socket <socket> correctable memory error count <cecount> exceeded
threshold <threshold>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when socket correctable memory error count is exceeded threshold

Event ID: 3012 (Severity: Warning)

Message

Module <channel> correctable memory error count <cecount> exceeded
threshold <threshold>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when module correctable memory error count is exceeded threshold

Event ID: 3013 (Severity: Warning)

Message

Page <page> correctable memory error count <cecount> exceeded threshold
<threshold> and <offlined>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when page correctable memory error count is exceeded threshold

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

94

Hardware switch controller sync events

Chapter 39

Hardware switch controller sync events

The following are the events related to hardware switch controller.

Event ID: 8801

Message

Hardware VTEP DB setup is completed

Category

Hardware switch controller sync

Severity

Information

Description

Log when hardware VTEP DB setup is completed

Event ID: 8802

Message

Physical Port <port> is created in Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Information

Description

Log when physical port is created in hardware VTEP DB

Event ID: 8803

Message

Physical Port <port> is deleted from Hardware VTEP DB

Category

Hardware switch controller sync

Severity

Information

Description

Log when physical port is deleted from hardware VTEP DB

Event ID: 8804

Message

HSC configuration is completed on the switch and pushed to Hardware
VTEP DB

Category

Hardware switch controller sync

Severity

Information

Description

Logs when HSC configuration is completed on the switch and pushed to Hardware VTEP
DB

Event ID: 8805

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

95

Message HSC configuration is deleted from the switch and Hardware VTEP DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenHSCconfigurationisdeletedfromtheswitchandHardwareVTEPDB
EventID:8806
Message Local MAC <mac> learnt on VLAN <vlan> is updated in the Hardware VTEP
DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenlocalMAClearnonVLANisupdatedintheHardwarVTEPDB
EventID:8807
Message Local MAC <mac> learnt on VLAN <vlan> is removed from the Hardware VTEP
DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenlocalMAClearntonVLANisremovedfromtheHardwareVTEPDB
EventID:8808
| Message     | VXLAN IP <ip>                               | is updated | in the Hardware | VTEP DB |
| ----------- | ------------------------------------------- | ---------- | --------------- | ------- |
| Category    | Hardwareswitchcontrollersync                |            |                 |         |
| Severity    | Information                                 |            |                 |         |
| Description | LogswhenVXLANIPisupdatedintheHardwareVTEPDB |            |                 |         |
EventID:8809
Message VXLAN IP <ip> is removed from Switch and Hardware VTEP DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
EventID:8810
Message Unicast Remote MAC <mac> learnt on VNI <vni> is added to the switch
Hardwareswitchcontrollersyncevents|96

| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenunicastremoteMAClearntonVNIisaddedtotheswitch
EventID:8811
Message Unicast Remote MAC <mac> learnt on VNI <vni> is removed from the switch
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenunicastremoteMAClearntonVNIisremovedfromtheswitch
EventID:8812
| Message     | Tunnel <ip>                               | is removed | from Hardware | VTEP DB |
| ----------- | ----------------------------------------- | ---------- | ------------- | ------- |
| Category    | Hardwareswitchcontrollersync              |            |               |         |
| Severity    | Information                               |            |               |         |
| Description | LogswhentunnelisremovedfromHardwareVTEPDB |            |               |         |
97
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

|                     |     |     |     |       | Chapter | 40     |
| ------------------- | --- | --- | --- | ----- | ------- | ------ |
|                     |     |     |     | HTTPS | Server  | events |
| HTTPS Server events |     |     |     |       |         |        |
ThefollowingaretheeventsrelatedtoHTTPSserver.
EventID:5601
| Message  | User <user> | has enabled | <mode> for | REST mode |     |     |
| -------- | ----------- | ----------- | ---------- | --------- | --- | --- |
| Category | HTTPSServer |             |            |           |     |     |
| Severity | Information |             |            |           |     |     |
Description LogsamessagewhenauserchangesthestatusoftheRESTmode
EventID:5602
| Message  | User <user> | has <status> | HTTPS Server | on VRF <vrf> |     |     |
| -------- | ----------- | ------------ | ------------ | ------------ | --- | --- |
| Category | HTTPSServer |              |              |              |     |     |
| Severity | Information |              |              |              |     |     |
Description Logsamessagewhenauserenables/disablesthehttps-serverVRFconfiguration
EventID:5603
| Message     | User <user>                                 | closed all | HTTPS sessions |     |     |     |
| ----------- | ------------------------------------------- | ---------- | -------------- | --- | --- | --- |
| Category    | HTTPSServer                                 |            |                |     |     |     |
| Severity    | Information                                 |            |                |     |     |     |
| Description | LogsamessagewhenauserclosesallHTTPSsessions |            |                |     |     |     |
EventID:5604
Message User <user> changed the HTTPS Server max user sessions amount to
<sessions>
| Category | HTTPSServer |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
| Severity | Information |     |     |     |     |     |
Description Logsamessagewhenauserchangesthemaximumamountofsessionsperuser
EventID:5605
98
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

User <user> changed the HTTPS Server idle timeout to <timeout>

Category

HTTPS Server

Severity

Information

Description

Logs a message when a user changes the value of the session idle timeout

HTTPS Server events | 99

In-System Programming events

Chapter 41

In-System Programming events

The following are the events related to in-system programming.

Event ID: 7200

Message

Internal fatal error at <file>:<line>

Category

In-System Programming

Severity

Error

Description

ISP internal fatal error

Event ID: 7210

Message

Non-failsafe update needed for <devspec>. Please run the allow-unsafe-
updates command

Category

In-System Programming

Severity

Error

Description

A non-failsafe device update is needed, but the allow-unsafe-updates command has not
yet been run

Event ID: 7211

Message

Do not interrupt non-failsafe update for <devspec>

Category

In-System Programming

Severity

Error

Description

A non-failsafe device update is about to start, so do not interrupt it

Event ID: 7212

Message

Starting update for <devspec> from version <fromver> to version <tover>

Category

In-System Programming

Severity

Information

Description

A device update is about to start

Event ID: 7213

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

100

Message Update successful for <devspec> from version <fromver> to version
<tover>
| Category | In-SystemProgramming |     |
| -------- | -------------------- | --- |
| Severity | Information          |     |
Description Adeviceupdatewassuccessfulorinsomecaseswassuccessfullyarrangedtobe
performedlater
EventID:7214(Severity:Critical)
| Message     | Update failed        | for <devspec> |
| ----------- | -------------------- | ------------- |
| Category    | In-SystemProgramming |               |
| Severity    | Critical             |               |
| Description | Adeviceupdatefailed  |               |
EventID:7215
Message Deferred update for <devspec> will be performed after an automatic
module reset
| Category | In-SystemProgramming |     |
| -------- | -------------------- | --- |
| Severity | Information          |     |
Description Adeviceupdatewaspostponeduntilafteranautomaticresetofitsmodule
EventID:7216
Message Approximately <time> minute(s) remaining to update <numdevs> device(s)
on <modspec>
| Category | In-SystemProgramming |     |
| -------- | -------------------- | --- |
| Severity | Information          |     |
Description Indicatestheapproximateremainingupdatetimeforamodule
EventID:7217
Message Insufficient redundant power is available to update <devspec>
| Category    | In-SystemProgramming                   |     |
| ----------- | -------------------------------------- | --- |
| Severity    | Information                            |     |
| Description | Unabletoupdatenon-redundantpowersupply |     |
EventID:7218
In-SystemProgrammingevents|101

Message Programmable device updates are pending that require a power cycle.
Wait for all fabric and line modules to be ready, then power the system
|          | off and              | back on again |     |     |
| -------- | -------------------- | ------------- | --- | --- |
| Category | In-SystemProgramming |               |     |     |
| Severity | Information          |               |     |     |
Description ISPneedsthechassispower-cycledmanuallywhenitcannotbedoneautomatically
EventID:7219(Severity:Critical)
| Message     | Failed                               | to write-protect | <devspec> | (pass <pass>) |
| ----------- | ------------------------------------ | ---------------- | --------- | ------------- |
| Category    | In-SystemProgramming                 |                  |           |               |
| Severity    | Critical                             |                  |           |               |
| Description | Failedtowrite-protectamoduleordevice |                  |           |               |
102
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 42
Interface events
Interface events
Thefollowingaretheeventsrelatedtointerface.
EventID:401
Message Interface port_admin set to up for <interface> interface
| Category    | Interface                         |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Information                       |     |     |     |
| Description | Logwheninterfaceport_adminsettoup |     |     |     |
EventID:402
Message Interface port_admin set to down for <interface> interface
| Category    | Interface                           |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Information                         |     |     |     |
| Description | Logwheninterfaceport_adminsettodown |     |     |     |
EventID:403
| Message     | Link status                    | for interface | <interface> | is up': yes |
| ----------- | ------------------------------ | ------------- | ----------- | ----------- |
| Category    | Interface                      |               |             |             |
| Severity    | Information                    |               |             |             |
| Description | Logwheninterfacelinkstatusisup |               |             |             |
EventID:404
Message Link status for interface <interface> is <state>': yes
| Category    | Interface                        |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- |
| Severity    | Information                      |     |     |     |
| Description | Logwheninterfacelinkstatusisdown |     |     |     |
EventID:405
103
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message  | Reserved for | future | use |
| -------- | ------------ | ------ | --- |
| Category | Interface    |        |     |
| Severity | Error        |        |     |
EventID:406
Message Interface <interface> encountered a hardware error that caused a link
reset
| Category | Interface   |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logwheninterfaceencounteredanerrorthatrequiresuserintervention
EventID:407
Message Interface <interface> downshifted to speed <port_speed> Mbps because
|             | link attempt                          | failed | at higher speed. |
| ----------- | ------------------------------------- | ------ | ---------------- |
| Category    | Interface                             |        |                  |
| Severity    | Information                           |        |                  |
| Description | Logwheninterfaceencounteredadownshift |        |                  |
EventID:408(Severity:Warning)
Message Interface <interface> is down because MACsec and PFC features are
|          | mutually exclusive. |     |     |
| -------- | ------------------- | --- | --- |
| Category | Interface           |     |     |
| Severity | Warning             |     |     |
Description LogwheninterfaceisdownduetoincompatibleMACsecandPFCconfigutration
Interfaceevents|104

Chapter 43

Internal storage events

Internal storage events

The following are the events related to internal storage.

Event ID: 9101

Message

Failed to report storage <name> details for module <module_num>. Error:
<error>': yes

Category

Internal storage

Severity

Error

Description

Event raised when there is a storage reporting failure

Event ID: 9102

Message

Storage <name> health alert. Endurance utilization at <usage>% in
module <module_num>': yes

Category

Internal storage

Severity

Information

Description

Event raised when the storage health deteriorates

Event ID: 9103

Message

Storage <name> endurance utilization at <usage>% in module <module_
num>': yes

Category

Internal storage

Severity

Information

Description

Event raised when there is a change in storage endurance

Event ID: 9104

Message

Storage <name> health alert. Endurance utilization at <usage>% in
module <module_num>. Failure is imminent. Please backup data': yes

Category

Internal storage

Severity

Error

Description

Event raised when storage failure is imminent

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

105

Chapter 44
|           |          |        |     | IP source | lockdown | events |
| --------- | -------- | ------ | --- | --------- | -------- | ------ |
| IP source | lockdown | events |     |           |          |        |
ThefollowingaretheeventsrelatedtoIPsourcelockdown.
EventID:9801(Severity:Warning)
Message IP source-lockdown resource utilization has reached 80 percent of the
|          |     | supported limit  | of <max_supported_limit> |     | on the system |     |
| -------- | --- | ---------------- | ------------------------ | --- | ------------- | --- |
| Category |     | IPsourcelockdown |                          |     |               |     |
| Severity |     | Warning          |                          |     |               |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
reached80percentofthesupportedlimits
EventID:9802(Severity:Critical)
Message IP source-lockdown resource utilization has exceeded maximum supported
|          |     | limit of <max_supported_limit> |               | on the          | system. IP source-lockdown |     |
| -------- | --- | ------------------------------ | ------------- | --------------- | -------------------------- | --- |
|          |     | functionality                  | will not work | for new entries |                            |     |
| Category |     | IPsourcelockdown               |               |                 |                            |     |
| Severity |     | Critical                       |               |                 |                            |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
exceededthesupportedlimits
EventID:9803
Message IP source-lockdown resource utilization has reduced below 80 percent of
|          |     | the supported    | limit of <max_supported_limit> |     | on the system |     |
| -------- | --- | ---------------- | ------------------------------ | --- | ------------- | --- |
| Category |     | IPsourcelockdown |                                |     |               |     |
| Severity |     | Information      |                                |     |               |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
reducedbelow80percentofthesupportedlimits
EventID:9804
Message IPv4 source-lockdown is enabled on interface <interface>
| Category |     | IPsourcelockdown |     |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- | --- |
106
| AOS-CXEventLogMessageReferenceGuide10.09| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

Severity

Information

Description

Log event when IPV4_SOURCE_LOCKDOWN is enabled on an interface

Event ID: 9805

Message

IPv4 source-lockdown is disabled on interface <interface>

Category

IP source lockdown

Severity

Information

Description

Log event when IPV4_SOURCE_LOCKDOWN is disabled on an interface

Event ID: 9806

Message

IPv6 source-lockdown is enabled on interface <interface>

Category

IP source lockdown

Severity

Information

Description

Log event when IPV6_SOURCE_LOCKDOWN is enabled on an interface

Event ID: 9807

Message

IPv6 source-lockdown is disabled on interface <interface>

Category

IP source lockdown

Severity

Information

Description

Log event when IPV6_SOURCE_LOCKDOWN is disabled on an interface

IP source lockdown events | 107

Chapter 45

IP tunnels events

IP tunnels events

The following are the events related to IP tunnels.

Event ID: 9601

Message

Tunnel Creation Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>)
Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel creation fails

Event ID: 9602

Message

Tunnel Created - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local
IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel created

Event ID: 9603

Message

Tunnel Deletion Failed - Name (<tunnel_name>) Type (<type>) VRF (<vrf>)
Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel deletion failed

Event ID: 9604

Message

Tunnel Deleted - Name (<tunnel_name>) Type (<type>) VRF (<vrf>) Local
IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel deleted

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

108

Event ID: 9605

Message

Tunnel Modification Failed - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>) TTL (<ttl>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel modification failed

Event ID: 9606

Message

Tunnel Source IP Modified - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel source ip modified

Event ID: 9607

Message

Tunnel Destination IP Modified - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel destination ip modified

Event ID: 9608

Message

Tunnel TTL Modified - Name (<tunnel_name>) Type (<type>) VRF (<vrf>)
Local IP (<src_ip>) Remote IP (<dst_ip>) TTL (<ttl>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel TTL modified

Event ID: 9609

Message

Tunnel MTU Modification Failed - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>) MTU (<ip_mtu>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel mtu modification failed

IP tunnels events | 109

Event ID: 9610

Message

Tunnel MTU Modified - Name (<tunnel_name>) Type (<type>) VRF (<vrf>)
Local IP (<src_ip>) Remote IP (<dst_ip>) MTU (<ip_mtu>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel mtu modified

Event ID: 9611

Message

Tunnel Nexthop Add Failed - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel nexthop add failed

Event ID: 9612

Message

Tunnel Nexthop Added - Name (<tunnel_name>) Type (<type>) VRF (<vrf>)
Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel nexthop gets added

Event ID: 9613

Message

Tunnel Nexthop Modify Failed - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel nexthop modify failed

Event ID: 9614

Message

Tunnel Nexthop Modified - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel nexthop gets modified

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

110

Event ID: 9615

Message

Tunnel Nexthop Delete Failed - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel nexthop delete failed

Event ID: 9616

Message

Tunnel Nexthop Deleted - Name (<tunnel_name>) Type (<type>) VRF (<vrf>)
Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel nexthop gets deleted

IP tunnels events | 111

Chapter 46
IP-SLA events
IP-SLA events
ThefollowingaretheeventsrelatedtoIP-SLA.
EventID:7401
Message IP-SLA session:<name> state changed to failed <state> due to reason
<reason>
| Category | IP-SLA |     |     |
| -------- | ------ | --- | --- |
| Severity | Error  |     |     |
Description EventraisedwhenanIP-SLAsessionstateischangedtoanyfailedstate
EventID:7402
Message IP-SLA session:<name> state changed to <state> due to reason <reason>
| Category | IP-SLA      |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description EventraisedwhenanIP-SLAsessionstateischangedtoanyinfostate
EventID:7403
| Message     | IP-SLA <name>:                                 | <operation> |     |
| ----------- | ---------------------------------------------- | ----------- | --- |
| Category    | IP-SLA                                         |             |     |
| Severity    | Information                                    |             |     |
| Description | EventraisedwhenanIP-SLAsessionisaddedordeleted |             |     |
EventID:7404
| Message     | IP-SLA session:<name>                        | is incomplete | to schedule |
| ----------- | -------------------------------------------- | ------------- | ----------- |
| Category    | IP-SLA                                       |               |             |
| Severity    | Error                                        |               |             |
| Description | EventraisedwhenanIP-SLAincompleconfigisadded |               |             |
EventID:7405
112
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

Category

Severity

IP-SLA session:<name> interface <interface> is not ready and SLA is
disabled

IP-SLA

Error

Description

Event raised when an IP-SLA session stopped due to source IP or interface changes

Event ID: 7406

Message

IP-SLA session:<name> interface <interface> is ready and SLA is enabled

Category

Severity

IP-SLA

Error

Description

Event raised when an IP-SLA session started due to source IP or interface changes

Event ID: 7407

Message

IP-SLA session:<name> failed to bind source, reason:<reason>

Category

Severity

IP-SLA

Error

Description

Event raised when an IP-SLA session failed to bind source

Event ID: 7408

Message

IP-SLA session:<name> failed to initialize socket, reason:<reason>

Category

Severity

IP-SLA

Error

Description

Event raised when an IP-SLA session failed to initialize socket

IP-SLA events | 113

Chapter 47
|             |               |        | IPv6 | Router Advertisement | events |
| ----------- | ------------- | ------ | ---- | -------------------- | ------ |
| IPv6 Router | Advertisement | events |      |                      |        |
ThefollowingaretheeventsrelatedtoIPv6routeradvertisement.
EventID:3901
| Message     | ipv6 ra                      | enabled on | interface: | <intf> |     |
| ----------- | ---------------------------- | ---------- | ---------- | ------ | --- |
| Category    | IPv6RouterAdvertisement      |            |            |        |     |
| Severity    | Information                  |            |            |        |     |
| Description | Eventraisedwhenipv6raenabled |            |            |        |     |
EventID:3902
| Message     | ipv6 ra                       | disabled on | interface: | <intf> |     |
| ----------- | ----------------------------- | ----------- | ---------- | ------ | --- |
| Category    | IPv6RouterAdvertisement       |             |            |        |     |
| Severity    | Information                   |             |            |        |     |
| Description | Eventraisedwhenipv6radisabled |             |            |        |     |
EventID:3903
Message Disabled sending MTU in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                      |     |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                                  |     |     |     |     |
| Description | Eventraisedwhenipv6rasuppressmtuisconfigured |     |     |     |     |
EventID:3904
Message Enabled sending MTU in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                    |     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- |
| Severity    | Information                                |     |     |     |     |
| Description | Eventraisedwhenipv6rasuppressmtuconfigured |     |     |     |     |
EventID:3905
114
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Message Disabled sending RDNSS in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                        |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Information                                    |     |     |     |
| Description | Eventraisedwhenipv6rasuppressrdnssisconfigured |     |     |     |
EventID:3906
Message Enabled sending RDNSS in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |
| Description | Eventraisedwhenipv6rasuppressrdnssisremoved |     |     |     |
EventID:3907
Message Disabled sending DNSSL in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                        |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Information                                    |     |     |     |
| Description | Eventraisedwhenipv6rasuppressdnsslisconfigured |     |     |     |
EventID:3908
Message Enabled sending DNSSL in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |
| Description | Eventraisedwhenipv6rasuppressdnsslisremoved |     |     |     |
EventID:3909
| Message     | Interface:                            | <intf> | is added to router | discovery |
| ----------- | ------------------------------------- | ------ | ------------------ | --------- |
| Category    | IPv6RouterAdvertisement               |        |                    |           |
| Severity    | Information                           |        |                    |           |
| Description | Eventraisedwhenipv6rainterfaceisadded |        |                    |           |
EventID:3910
| Message | Interface: | <intf> | is deleted from | router discovery |
| ------- | ---------- | ------ | --------------- | ---------------- |
IPv6RouterAdvertisementevents|115

| Category    | IPv6RouterAdvertisement                 |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Eventraisedwhenipv6rainterfaceisdeleted |     |     |     |
EventID:3911
Message Added ipv6 prefix: <ipv6_addr>/<prefixlen> on interface: <intf>
| Category    | IPv6RouterAdvertisement                      |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- |
| Severity    | Information                                  |     |     |     |
| Description | Eventraisedwhenipv6addressisaddedoninterface |     |     |     |
EventID:3912
Message Deleted ipv6 prefix: <ipv6_addr>/<prefixlen> from interface: <intf>
| Category    | IPv6RouterAdvertisement                          |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | Information                                      |     |     |     |
| Description | Eventraisedwhenipv6addressisdeletedfrominterface |     |     |     |
EventID:3913
Message Added RA Prefix: <prefix> on interface: <intf> to prefix list
| Category    | IPv6RouterAdvertisement                   |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Information                               |     |     |     |
| Description | EventraisedwhenRAPrefixisaddedoninterface |     |     |     |
EventID:3914
Message Deleted RA Prefix: <prefix> on interface: <intf> from prefix list
| Category    | IPv6RouterAdvertisement                       |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | EventraisedwhenRAPrefixisdeletedfrominterface |     |     |     |
EventID:3915
| Message  | default prefix          | is configured | on interface | <intf> |
| -------- | ----------------------- | ------------- | ------------ | ------ |
| Category | IPv6RouterAdvertisement |               |              |        |
116
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Information                              |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Description | Eventraisedwhendefaultprefixisconfigured |     |     |
EventID:3916
| Message     | RDNSS is added              | on interface: | <intf> |
| ----------- | --------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement     |               |        |
| Severity    | Information                 |               |        |
| Description | EventraisedwhenRDNSSisadded |               |        |
EventID:3917
| Message     | RDNSS is deleted              | on interface: | <intf> |
| ----------- | ----------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement       |               |        |
| Severity    | Information                   |               |        |
| Description | EventraisedwhenRDNSSisdeleted |               |        |
EventID:3918
| Message     | DNSSL is added              | on interface: | <intf> |
| ----------- | --------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement     |               |        |
| Severity    | Information                 |               |        |
| Description | EventraisedwhenDNSSLisadded |               |        |
EventID:3919
| Message     | DNSSL is deleted              | on interface: | <intf> |
| ----------- | ----------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement       |               |        |
| Severity    | Information                   |               |        |
| Description | EventraisedwhenDNSSLisdeleted |               |        |
EventID:3920
Message Added RA Route: <route> on interface: <intf> to route list
| Category    | IPv6RouterAdvertisement                  |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | EventraisedwhenRARouteisaddedoninterface |     |     |
IPv6RouterAdvertisementevents|117

Event ID: 3921

Message

Deleted RA Route: <route> on interface: <intf> from route list

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when RA Route is deleted from interface

Event ID: 3922

Message

Interface: <intf> has been configured with the invalid IPv6 nd ra
maxInterval or minInterval

Category

IPv6 Router Advertisement

Severity

Information

Description

Event raised when ipv6 nd ra maxInterval or minInterval is improper

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

118

Chapter 48
IRDP events
IRDP events
ThefollowingaretheeventsrelatedtoIRDP.
EventID:3501
| Message  | IRDP enabled | on interface | <interface> |
| -------- | ------------ | ------------ | ----------- |
| Category | IRDP         |              |             |
| Severity | Information  |              |             |
Description ThiscommandenablestheIRDP(ICMPRouterDiscoveryProtocol)featureoninterface.
EventID:3502
| Message  | IRDP disabled | on interface | <interface> |
| -------- | ------------- | ------------ | ----------- |
| Category | IRDP          |              |             |
| Severity | Information   |              |             |
Description ThiscommanddisablestheIRDP(ICMPRouterDiscoveryProtocol)featureoninterface.
EventID:3503
Message Interface: <interface> has been configured with the invalid irdp
|          | holdtime    | or minInterval | or maxInterval |
| -------- | ----------- | -------------- | -------------- |
| Category | IRDP        |                |                |
| Severity | Information |                |                |
Description EventraisedwhenirdpholdtimeormaxIntervalorminIntervalisimproper
119
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 49

Job scheduler events

Job scheduler events

The following are the events related to job scheduler.

Event ID: 12201

Message

Creating schedule <name>, trigger time(s): <start_datetime><details>

Category

Job scheduler

Severity

Information

Description

Event reported when a schedule is created

Event ID: 12202

Message

Schedule <name> triggered, trigger_count: <trigger_count>

Category

Job scheduler

Severity

Information

Description

Event reported when a schedule triggers

Event ID: 12203

Message

Timezone changed. Re-creating schedule <name>, trigger time(s): <start_
datetime><details>

Category

Job scheduler

Severity

Information

Description

Event reported when the schedules are recreated due to timezone change.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

120

Chapter 50
|          |          |        |     | L3 Encap | capacity | events |
| -------- | -------- | ------ | --- | -------- | -------- | ------ |
| L3 Encap | capacity | events |     |          |          |        |
ThefollowingaretheeventsrelatedtoL3Encapcapacity.
EventID:10601(Severity:Warning)
Message L3 resources critical for neighbor and route forwarding are low. Used:
|          |     | <encaps_allocated>, | Available: | <encaps_free> |     |     |
| -------- | --- | ------------------- | ---------- | ------------- | --- | --- |
| Category |     | L3Encapcapacity     |            |               |     |     |
| Severity |     | Warning             |            |               |     |     |
Description L3resourcesneededforneighborandrouteforwardingarerunninglow.Large-scale
neighbormovescouldcausetrafficloss.
EventID:10602
Message L3 resources critical for neighbor and route forwarding are at safe
|          |     | levels. Used:   | <encaps_allocated>, | Available: | <encaps_free> |     |
| -------- | --- | --------------- | ------------------- | ---------- | ------------- | --- |
| Category |     | L3Encapcapacity |                     |            |               |     |
| Severity |     | Information     |                     |            |               |     |
Description L3resourcesneededforneighborandrouteforwardingarebacktoasafelevel.
EventID:10603
Message Out of L3 resources critical for neighbor and route forwarding. Used:
|          |     | <encaps_allocated>, | Available: | <encaps_free> |     |     |
| -------- | --- | ------------------- | ---------- | ------------- | --- | --- |
| Category |     | L3Encapcapacity     |            |               |     |     |
| Severity |     | Error               |            |               |     |     |
Description L3resourcesneededforneighborandrouteforwardinghaverunout.Trafficlossis
imminent.
121
| AOS-CXEventLogMessageReferenceGuide10.09| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

Chapter 51
|             |         |        |     | L3 Resource | Manager | events |
| ----------- | ------- | ------ | --- | ----------- | ------- | ------ |
| L3 Resource | Manager | events |     |             |         |        |
ThefollowingaretheeventsrelatedtoL3ResourceManager.
EventID:11501(Severity:Warning)
Message IPv6 route prefix <prefix> is not supported on this platform.
| Category    | L3ResourceManager                   |     |     |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Warning                             |     |     |     |     |     |
| Description | logswarningforrouteadditionattempt. |     |     |     |     |     |
EventID:11502
Message "Exceeded resource '<resource>' capacity adding <object>. Use 'show
|             | capacities-status'                 |     | for more | information." | throttle_count: | 40  |
| ----------- | ---------------------------------- | --- | -------- | ------------- | --------------- | --- |
| Category    | L3ResourceManager                  |     |          |               |                 |     |
| Severity    | Error                              |     |          |               |                 |     |
| Description | logserrorforrunningoutofresources. |     |          |               |                 |     |
EventID:11503(Severity:Warning)
Message "Resource '<resource>' usage is at <percent>% of capacity. Use 'show
|             | capacities-status'                          |     | for more | information." | throttle_count: | 40  |
| ----------- | ------------------------------------------- | --- | -------- | ------------- | --------------- | --- |
| Category    | L3ResourceManager                           |     |          |               |                 |     |
| Severity    | Warning                                     |     |          |               |                 |     |
| Description | logswarningforhittingcertaincapacitylimits. |     |          |               |                 |     |
122
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

Chapter 52
LACP events
LACP events
ThefollowingaretheeventsrelatedtoLACP.
EventID:1301
| Message     | Dynamic                  | LAG <lag_id> | created |     |
| ----------- | ------------------------ | ------------ | ------- | --- |
| Category    | LACP                     |              |         |     |
| Severity    | Information              |              |         |     |
| Description | DynamicLAGhasbeencreated |              |         |     |
EventID:1302
| Message     | Dynamic                  | LAG <lag_id> | deleted |     |
| ----------- | ------------------------ | ------------ | ------- | --- |
| Category    | LACP                     |              |         |     |
| Severity    | Information              |              |         |     |
| Description | DynamicLAGhasbeendeleted |              |         |     |
EventID:1303
Message Interface <intf_id> added to LAG <lag_id>. Existing configuration on
|             | interface                         | <intf_id> | will be removed. |     |
| ----------- | --------------------------------- | --------- | ---------------- | --- |
| Category    | LACP                              |           |                  |     |
| Severity    | Information                       |           |                  |     |
| Description | LogwheninterfacehasbeenaddedtoLAG |           |                  |     |
EventID:1304
Message Interface <intf_id> removed from LAG <lag_id>. It will be set with
|             | default                               | configuration | with admin | down state. |
| ----------- | ------------------------------------- | ------------- | ---------- | ----------- |
| Category    | LACP                                  |               |            |             |
| Severity    | Information                           |               |            |             |
| Description | LogwheninterfacehasbeenremovedfromLAG |               |            |             |
EventID:1305
123
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | LACP system                    | priority | set to <system_priority> |     |     |
| ----------- | ------------------------------ | -------- | ------------------------ | --- | --- |
| Category    | LACP                           |          |                          |     |     |
| Severity    | Information                    |          |                          |     |     |
| Description | LogwhenLACPsystempriorityisset |          |                          |     |     |
EventID:1306
| Message     | LACP mode            | set to <lacp_mode> | for | LAG <lag_id> |     |
| ----------- | -------------------- | ------------------ | --- | ------------ | --- |
| Category    | LACP                 |                    |     |              |     |
| Severity    | Information          |                    |     |              |     |
| Description | LogwhenLACPmodeisset |                    |     |              |     |
EventID:1307
| Message     | LACP system              | ID set | to <system_id> |     |     |
| ----------- | ------------------------ | ------ | -------------- | --- | --- |
| Category    | LACP                     |        |                |     |     |
| Severity    | Information              |        |                |     |     |
| Description | LogwhenLACPsystemIDisset |        |                |     |     |
EventID:1308
| Message     | LACP rate            | set to <lacp_rate> | for | LAG <lag_id> |     |
| ----------- | -------------------- | ------------------ | --- | ------------ | --- |
| Category    | LACP                 |                    |     |              |     |
| Severity    | Information          |                    |     |              |     |
| Description | LogwhenLACPrateisset |                    |     |              |     |
EventID:1309
Message Partner is detected for interface <intf_id> LAG <lag_id>: <partner_sys_
|             | id>. Actor                   | state: <actor_state>, |     | partner state | <partner_state> |
| ----------- | ---------------------------- | --------------------- | --- | ------------- | --------------- |
| Category    | LACP                         |                       |     |               |                 |
| Severity    | Information                  |                       |     |               |                 |
| Description | LogwhenLACPpartnerisdetected |                       |     |               |                 |
EventID:1310(Severity:Warning)
Message Partner is out of sync for interface <intf_id> LAG <lag_id>. Actor
LACPevents|124

|             | state:                       | <actor_state>, | partner state | <partner_state> |
| ----------- | ---------------------------- | -------------- | ------------- | --------------- |
| Category    | LACP                         |                |               |                 |
| Severity    | Warning                      |                |               |                 |
| Description | LogwhenLACPparterisoutofsync |                |               |                 |
EventID:1311(Severity:Warning)
Message Partner is lost (timed out) for interface <intf_id> LAG <lag_id>.
State: <fsm_state>
| Category    | LACP                               |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Warning                            |     |     |     |
| Description | LogtoindicatethatLACPpartnerislost |     |     |     |
EventID:1312
| Message     | Failed                     | to create LAG | <lag_id> |     |
| ----------- | -------------------------- | ------------- | -------- | --- |
| Category    | LACP                       |               |          |     |
| Severity    | Error                      |               |          |     |
| Description | LogwhenLAGcreationisfailed |               |          |     |
EventID:1313
| Message     | LAG <lag_id>        | set as | VSX |     |
| ----------- | ------------------- | ------ | --- | --- |
| Category    | LACP                |        |     |     |
| Severity    | Information         |        |     |     |
| Description | LogwhenVSXiscreated |        |     |     |
EventID:1314
Message LAG <lag_id> not sending LACPDUs through interface <intf_id> because
|          | VSX information | is  | not complete |     |
| -------- | --------------- | --- | ------------ | --- |
| Category | LACP            |     |              |     |
| Severity | Information     |     |              |     |
Description LogwhenLAGisnotsendingLACPDUsthroughinterfacebecauseVSXinformationis
incomplete
EventID:1315
125
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message LACP fallback mode set to <lacp_fallback_mode> for lag <lag_id>
| Category    | LACP                         |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Error                        |     |     |     |
| Description | LogwhenLACPfallbackmodeisset |     |     |     |
EventID:1316
Message LACP fallback timeout set to <lacp_fallback_timeout> for lag <lag_id>
| Category    | LACP                            |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- |
| Severity    | Error                           |     |     |     |
| Description | LogwhenLACPfallbacktimeoutisset |     |     |     |
EventID:1317
Message LACP fallback timeout <lacp_fallback_timeout> expired for lag <lag_id>
| Category    | LACP                                |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Error                               |     |     |     |
| Description | LogwhenLACPfallbacktimeoutisexpired |     |     |     |
EventID:1318
Message Interface <intf_id> enabled by fallback for lag <lag_id>
| Category    | LACP                                |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Error                               |     |     |     |
| Description | Logwheninterfaceisenabledbyfallback |     |     |     |
EventID:1319
| Message  | LAG global  | load balancing | mode is set | to <mode> |
| -------- | ----------- | -------------- | ----------- | --------- |
| Category | LACP        |                |             |           |
| Severity | Information |                |             |           |
Description LogstosetgloballoadbalancingmodeforLAGinterfaces.
EventID:1320
Message LAG load balancing mode is set to <mode> for lag <lag_id>
LACPevents|126

| Category | LACP        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogstosetperportloadbalancingmodeforLAGinterface.
EventID:1321
Message LAG <lag_id> State change for interface <intf_id>: Actor state: <actor_
|          | state>, Partner | state | <partner_state> |
| -------- | --------------- | ----- | --------------- |
| Category | LACP            |       |                 |
| Severity | Information     |       |                 |
Description LogsthatcapturechangestoLACPstateforLAGinterface.
EventID:1322
Message Interface <intf_name> cannot be part of Lag <lag_number>. Speed
mismatched (Interface speed <port_speed>Mbps Lag base speed <lag_
|          | speed>Mbps).' | throttle_count: | 100 |
| -------- | ------------- | --------------- | --- |
| Category | LACP          |                 |     |
| Severity | Information   |                 |     |
Description LogstocaptureifLACPprotocoldoesnotallowinterfacetobepartoflagduetospeed
mismatch.
EventID:1323
| Message     | Fallback                                        | is <fallback> | for LAG <lag_id> |
| ----------- | ----------------------------------------------- | ------------- | ---------------- |
| Category    | LACP                                            |               |                  |
| Severity    | Information                                     |               |                  |
| Description | LogstocaptureiffallbackischangedforLAGinterface |               |                  |
EventID:1324
| Message     | LACP Graceful                                  | Shut is | initiated |
| ----------- | ---------------------------------------------- | ------- | --------- |
| Category    | LACP                                           |         |           |
| Severity    | Information                                    |         |           |
| Description | LogsthatcaputreLACPGracefulShutforLAGinterface |         |           |
EventID:1325
127
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Message

LACP Graceful Shut is completed

Category

LACP

Severity

Information

Description

Logs that caputre LACP Graceful Shut for LAG interface

LACP events | 128

Chapter 53
LAG events
LAG events
ThefollowingaretheeventsrelatedtoLAG.
EventID:1401
| Message     | Trunk set               | succeeds unit | <unit> lag_id | <lag_id> |
| ----------- | ----------------------- | ------------- | ------------- | -------- |
| Category    | LAG                     |               |               |          |
| Severity    | Debug                   |               |               |          |
| Description | Logsthecreationoftrunk. |               |               |          |
EventID:1402
Message Lag creation failed unit <unit> lag_id <lag_id> rc <rc> error <error>
| Category    | LAG                            |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | Logsthefailureoftrunkcreation. |     |     |     |
EventID:1403
Message Destroy lag failed on unit <unit> lag_id <lag_id> rc <rc> error <error>
| Category    | LAG                           |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Severity    | Error                         |     |     |     |
| Description | Logsthefailureoftrunkdestroy. |     |     |     |
EventID:1404
Message Trunk member add port succeeds on unit <unit> hw_port <hw_port> tid
<tid>
| Category    | LAG                           |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Severity    | Debug                         |     |     |     |
| Description | Logstheadditionofporttotrunk. |     |     |     |
EventID:1405
129
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message Trunk port attach error on hw_port <hw_port> tid <tid> rc <rc> <error>
| Category    | LAG                                    |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- |
| Severity    | Error                                  |     |     |     |
| Description | Logsthefailureofadditionofporttotrunk. |     |     |     |
EventID:1406
Message Failed to set egress enable on hw_port <hw_port> tid <tid> rc <rc>
error <error>
| Category    | LAG                              |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- |
| Severity    | Error                            |     |     |     |
| Description | Logsthefailuretosetegressenable. |     |     |     |
EventID:1407
Message Failed to delete hw_port <hw_port> from tid <tid> rc <rc> error <error>
| Category    | LAG                          |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Error                        |     |     |     |
| Description | Logsthefailuretodeleteaport. |     |     |     |
EventID:1408
Message Trunk psc set failed on unit <unit> lag_id <lag_id> psc <psc> rc <rc>
error <error>
| Category    | LAG                                       |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Error                                     |     |     |     |
| Description | Logsthefailuretosetportselectioncriteria. |     |     |     |
EventID:1409
| Message     | LAG <interface>,                                 | set to load | balance mode | to <mode> |
| ----------- | ------------------------------------------------ | ----------- | ------------ | --------- |
| Category    | LAG                                              |             |              |           |
| Severity    | Information                                      |             |              |           |
| Description | logstosetloadbalancingmodeforLAGL2/L3interfaces. |             |              |           |
EventID:1410
LAGevents|130

| Message     | Add port            | <port> to LAG | <interface> |
| ----------- | ------------------- | ------------- | ----------- |
| Category    | LAG                 |               |             |
| Severity    | Information         |               |             |
| Description | logstoaddporttoLAG. |               |             |
EventID:1411
| Message     | Remove port              | <port> from | LAG <interface> |
| ----------- | ------------------------ | ----------- | --------------- |
| Category    | LAG                      |             |                 |
| Severity    | Information              |             |                 |
| Description | logstoremoveportfromLAG. |             |                 |
EventID:1412
Message Add port <port> to vlan <vlan> for L3 LAG <interface>
| Category    | LAG                   |     |     |
| ----------- | --------------------- | --- | --- |
| Severity    | Information           |     |     |
| Description | logstoaddporttoL3LAG. |     |     |
EventID:1413
Message Remove port <port> to vlan <vlan> for L3 LAG <interface>
| Category    | LAG                      |     |     |
| ----------- | ------------------------ | --- | --- |
| Severity    | Information              |     |     |
| Description | logstoremoveportfromLAG. |     |     |
EventID:1414
| Message     | Destroy             | L3 LAG interface | <interface> |
| ----------- | ------------------- | ---------------- | ----------- |
| Category    | LAG                 |                  |             |
| Severity    | Information         |                  |             |
| Description | logstodestroyL3LAG. |                  |             |
131
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Chapter 54
|                   |        |     |     | Layer | 3 Interface | events |
| ----------------- | ------ | --- | --- | ----- | ----------- | ------ |
| Layer 3 Interface | events |     |     |       |             |        |
Thefollowingaretheeventsrelatedtolayer3interface.
EventID:1701
| Message     | L3-Interface             | <interface>, | created |     |     |     |
| ----------- | ------------------------ | ------------ | ------- | --- | --- | --- |
| Category    | Layer3Interface          |              |         |     |     |     |
| Severity    | Information              |              |         |     |     |     |
| Description | logstocreateL3interface. |              |         |     |     |     |
EventID:1702
| Message     | L3-Interface             | <interface>, | deleted |     |     |     |
| ----------- | ------------------------ | ------------ | ------- | --- | --- | --- |
| Category    | Layer3Interface          |              |         |     |     |     |
| Severity    | Information              |              |         |     |     |     |
| Description | logstodeleteL3interface. |              |         |     |     |     |
EventID:1703
Message Interface <interface>, configured administratively <state>
| Category    | Layer3Interface                 |     |     |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                     |     |     |     |     |     |
| Description | logsforadminstateofL3interface. |     |     |     |     |     |
EventID:1704
Message Failed to create <vlanid> for layer 3 interface <interface>
| Category    | Layer3Interface                                 |     |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Error                                           |     |     |     |     |     |
| Description | logserrorswhilecreatingvlanforlayer3interfaces. |     |     |     |     |     |
EventID:1705
132
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message Failed to destroy layer 3 interface <interface> vlan <vlanid>, error:
<err>
| Category    | Layer3Interface                                   |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Error                                             |     |     |
| Description | logserrorswhiledestroyingvlanforlayer3interfaces. |     |     |
EventID:1706
Message Failed to delete an l3 interface <interface>, error: <err>
| Category    | Layer3Interface                           |     |     |
| ----------- | ----------------------------------------- | --- | --- |
| Severity    | Error                                     |     |     |
| Description | logserrorswhiledestroyinglayer3interface. |     |     |
EventID:1707
Message Failed to add L3 host entry for ip <ipaddr>, error: <err>' throttle_
count: 1
| Category    | Layer3Interface               |     |     |
| ----------- | ----------------------------- | --- | --- |
| Severity    | Error                         |     |     |
| Description | logserrorswhileaddingl3hosts. |     |     |
EventID:1708
| Message     | Added L3 host           | entry for | ip <ipaddr> |
| ----------- | ----------------------- | --------- | ----------- |
| Category    | Layer3Interface         |           |             |
| Severity    | Information             |           |             |
| Description | logswhileaddingl3hosts. |           |             |
EventID:1709
Message Failed to delete L3 host entry for ip <ipaddr>, error: <err>
| Category    | Layer3Interface                 |     |     |
| ----------- | ------------------------------- | --- | --- |
| Severity    | Error                           |     |     |
| Description | logserrorswhiledeletingl3hosts. |     |     |
EventID:1710
Layer3Interfaceevents|133

| Message     | Deleted                   | L3 host entry | for ip <ipaddr> |     |
| ----------- | ------------------------- | ------------- | --------------- | --- |
| Category    | Layer3Interface           |               |                 |     |
| Severity    | Information               |               |                 |     |
| Description | logswhiledeletingl3hosts. |               |                 |     |
EventID:1711
| Message     | Failed                                  | to get L3 host | hit for | ip <ipaddr> |
| ----------- | --------------------------------------- | -------------- | ------- | ----------- |
| Category    | Layer3Interface                         |                |         |             |
| Severity    | Error                                   |                |         |             |
| Description | logserrorstogetL3hosthitforaspecificip. |                |         |             |
EventID:1712
| Message     | L3 interface          | error: | <err> |     |
| ----------- | --------------------- | ------ | ----- | --- |
| Category    | Layer3Interface       |        |       |     |
| Severity    | Error                 |        |       |     |
| Description | logsforL3setuperrors. |        |       |     |
EventID:1713
Message Added Nexthop <nexthop>, egress_id <egress_id>, for route <prefix>
| Category    | Layer3Interface         |     |     |     |
| ----------- | ----------------------- | --- | --- | --- |
| Severity    | Information             |     |     |     |
| Description | logsfornexthopaddition. |     |     |     |
EventID:1714
| Message     | Delete                  | Nexthop <nexthop> | for route | <prefix> |
| ----------- | ----------------------- | ----------------- | --------- | -------- |
| Category    | Layer3Interface         |                   |           |          |
| Severity    | Information             |                   |           |          |
| Description | logsfornexthopdeletion. |                   |           |          |
EventID:1715
| Message | Added route | <prefix> |     |     |
| ------- | ----------- | -------- | --- | --- |
134
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Category    | Layer3Interface       |     |     |     |     |
| ----------- | --------------------- | --- | --- | --- | --- |
| Severity    | Information           |     |     |     |     |
| Description | logsforrouteaddition. |     |     |     |     |
EventID:1716
| Message     | Update:             | route state: | <state> |     |     |
| ----------- | ------------------- | ------------ | ------- | --- | --- |
| Category    | Layer3Interface     |              |         |     |     |
| Severity    | Information         |              |         |     |     |
| Description | logsforrouteupdate. |              |         |     |     |
EventID:1717
| Message     | Delete                | route <prefix> |     |     |     |
| ----------- | --------------------- | -------------- | --- | --- | --- |
| Category    | Layer3Interface       |                |     |     |     |
| Severity    | Information           |                |     |     |     |
| Description | logsforroutedeletion. |                |     |     |     |
EventID:1718
| Message     | Delete                     | route <prefix>, | error: <err> |     |     |
| ----------- | -------------------------- | --------------- | ------------ | --- | --- |
| Category    | Layer3Interface            |                 |              |     |     |
| Severity    | Error                      |                 |              |     |     |
| Description | logserrorforroutedeletion. |                 |              |     |     |
EventID:1719
| Message     | Add route                     | <prefix>, | error: <err>' | throttle_count: | 1   |
| ----------- | ----------------------------- | --------- | ------------- | --------------- | --- |
| Category    | Layer3Interface               |           |               |                 |     |
| Severity    | Error                         |           |               |                 |     |
| Description | logserrorforrouteaditiontion. |           |               |                 |     |
EventID:1720
Message Error creating egress object for port <port>, error: <err>
| Category | Layer3Interface |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
Layer3Interfaceevents|135

| Severity    | Error                              |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Description | logserrorsforegressobjectcreation. |     |     |     |
EventID:1721
Message Created L3 egress ID <egress_id> for port <port> intf <intf>
| Category    | Layer3Interface              |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Information                  |     |     |     |
| Description | logsforegressobjectcreation. |     |     |     |
EventID:1722
Message Error deleting egress object for port <port>, error: <err>
| Category    | Layer3Interface                    |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Error                              |     |     |     |
| Description | logserrorsforegressobjectdeletion. |     |     |     |
EventID:1723
| Message     | Deleted                      | L3 egress | ID <egress_id> | for port <port> |
| ----------- | ---------------------------- | --------- | -------------- | --------------- |
| Category    | Layer3Interface              |           |                |                 |
| Severity    | Information                  |           |                |                 |
| Description | logsforegressobjectdeletion. |           |                |                 |
EventID:1724
Message Interface <interface>, configured with ipv4 address <value>
| Category    | Layer3Interface                      |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | logsforipv4addressupdateoninterface. |     |     |     |
EventID:1725
Message Interface <interface>, configured with ipv6 address <value>
| Category    | Layer3Interface                      |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | logsforipv6addressupdateoninterface. |     |     |     |
136
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

EventID:1726
| Message     | Interface                              | <interface>, | ipv4 address | deleted <value> |
| ----------- | -------------------------------------- | ------------ | ------------ | --------------- |
| Category    | Layer3Interface                        |              |              |                 |
| Severity    | Information                            |              |              |                 |
| Description | logsforipv4addressdeletefrominterface. |              |              |                 |
EventID:1727
| Message     | Interface                              | <interface>, | ipv6 address | deleted <value> |
| ----------- | -------------------------------------- | ------------ | ------------ | --------------- |
| Category    | Layer3Interface                        |              |              |                 |
| Severity    | Information                            |              |              |                 |
| Description | logsforipv6addressdeletefrominterface. |              |              |                 |
EventID:1728
Message IPv6 Address Status: Interface <intf>, address <addr>, status <addr_
status>
| Category    | Layer3Interface                         |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Eventraisedwhenipv6addressstatuschanges |     |     |     |
EventID:1729
Message Interface <interface>, configured with secondary ipv4 address <value>
| Category    | Layer3Interface                               |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | logsforsecondaryipv4addressupdateoninterface. |     |     |     |
EventID:1730
Message Interface <interface>, secondary ipv4 address deleted <value>
| Category    | Layer3Interface                                 |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |
| Description | logsforsecondaryipv4addressdeletefrominterface. |     |     |     |
EventID:1731
Layer3Interfaceevents|137

Message

IP MTU <mtu> not applied due to hardware resource limitation

Category

Layer 3 Interface

Severity

Error

Description

Logs failure while configuring hardware for IPMTU.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

138

Chapter 55
LED events
LED events
ThefollowingaretheeventsrelatedtoLED.
EventID:501
| Message     | There are                           | <count> LED | types in subsystem | <subsystem> |
| ----------- | ----------------------------------- | ----------- | ------------------ | ----------- |
| Category    | LED                                 |             |                    |             |
| Severity    | Information                         |             |                    |             |
| Description | LogaboutnumberofLEDtypesinsubsystem |             |                    |             |
EventID:502
Message There are <count> LED configs in subsystem <subsystem>
| Category    | LED                                  |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | LogaboutnumberofLEDconfiginsubsystem |     |     |     |
139
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 56
LLDP events
LLDP events
ThefollowingaretheeventsrelatedtoLLDP.
EventID:101
| Message  | LLDP Enabled |     |     |
| -------- | ------------ | --- | --- |
| Category | LLDP         |     |     |
| Severity | Information  |     |     |
Description LogseventwhenLLDP(LinkLayerDiscoveryProtocol)featureisenabledintheswitch.
EventID:102
| Message  | LLDP Disabled |     |     |
| -------- | ------------- | --- | --- |
| Category | LLDP          |     |     |
| Severity | Information   |     |     |
Description LogseventwhenLLDP(LinkLayerDiscoveryProtocol)featureisdisabledintheswitch.
EventID:103
| Message  | Configured  | LLDP tx-timer | to <value> |
| -------- | ----------- | ------------- | ---------- |
| Category | LLDP        |               |            |
| Severity | Information |               |            |
Description LogseventwhentheLLDPstatusupdateintervalisconfiguredbytheuser.
EventID:104
| Message  | LLDP neighbor | <chassisid> | added on <interface> |
| -------- | ------------- | ----------- | -------------------- |
| Category | LLDP          |             |                      |
| Severity | Information   |             |                      |
Description Logseventwhenanewneighborentryisaddedtotheswitch.
EventID:105
140
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message LLDP neighbor <chassisid> updated on <interface>' throttle_count: 100
| Category | LLDP        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Logseventwhenanexistingneighborentryisupdatedintheswitch.
EventID:106
| Message  | LLDP neighbor | <chassisid> | deleted | on <interface> |
| -------- | ------------- | ----------- | ------- | -------------- |
| Category | LLDP          |             |         |                |
| Severity | Information   |             |         |                |
Description Logseventwhenanexistingneighborentryisdeletedfromswitch.
EventID:107
| Message  | Configured  | LLDP Management | IP <value> |     |
| -------- | ----------- | --------------- | ---------- | --- |
| Category | LLDP        |                 |            |     |
| Severity | Information |                 |            |     |
Description LogseventwhenanewmanagementIPaddressisconfiguredbytheuser.
EventID:108
| Message  | Configured  | LLDP tx-hold | to <hold> |     |
| -------- | ----------- | ------------ | --------- | --- |
| Category | LLDP        |              |           |     |
| Severity | Information |              |           |     |
Description LogseventwhenLLDPtransmitmultipliervalueisconfiguredbytheuser.
EventID:109
| Message  | Configured  | LLDP tx-delay | to <value> |     |
| -------- | ----------- | ------------- | ---------- | --- |
| Category | LLDP        |               |            |     |
| Severity | Information |               |            |     |
Description LogseventwhenLLDPtransmitdelayvalueisconfiguredbytheuser.
EventID:110
| Message | Configured | LLDP reinit-delay | to <value> |     |
| ------- | ---------- | ----------------- | ---------- | --- |
LLDPevents|141

| Category | LLDP        |     |
| -------- | ----------- | --- |
| Severity | Information |     |
Description LogseventwhenLLDPinterfacereinitializationvalueisconfiguredbytheuser.
EventID:111
| Message  | LLDP statistics | cleared |
| -------- | --------------- | ------- |
| Category | LLDP            |         |
| Severity | Information     |         |
Description LogseventwhenLLDPstatisticsareclearedfromtheswitch.
EventID:112
| Message  | LLDP neighbor | info cleared |
| -------- | ------------- | ------------ |
| Category | LLDP          |              |
| Severity | Information   |              |
Description LogseventwhenLLDPneighborinformationisclearedfromtheswitch.
EventID:113
Message PVID mismatch on <interface> pvid = <pvid>, Neighbor <chassisid> port_
|          | id = <ninterface> | pvid = <npvid> |
| -------- | ----------------- | -------------- |
| Category | LLDP              |                |
| Severity | Information       |                |
Description LogeventwhenthePVIDmismatchesbetweentheswitchandneighboroveraninterface.
142
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |
| ----------------------------------------- | --- | ----------------------------- |

Chapter 57
Loop Protect events
| Loop Protect events |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
Thefollowingaretheeventsrelatedtoloopprotect.
EventID:2801(Severity:Warning)
Message Port <portName> is disabled by Loop-protection after loop detection on
VLAN <vlan>
| Category    | LoopProtect                   |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | --- |
| Severity    | Warning                       |     |     |     |     |
| Description | LogsportdisabledbyLoopprotect |     |     |     |     |
EventID:2802(Severity:Warning)
Message Ports TX <txportName> and RX <rxportName> are disabled by Loop-protect
|             | after loop                    | detection | on VLAN <vlan> |     |     |
| ----------- | ----------------------------- | --------- | -------------- | --- | --- |
| Category    | LoopProtect                   |           |                |     |     |
| Severity    | Warning                       |           |                |     |     |
| Description | LogsportdisabledbyLoopprotect |           |                |     |     |
EventID:2803(Severity:Warning)
| Message     | Loop detected                    | on port | <portName> | on VLAN | <vlan> |
| ----------- | -------------------------------- | ------- | ---------- | ------- | ------ |
| Category    | LoopProtect                      |         |            |         |        |
| Severity    | Warning                          |         |            |         |        |
| Description | LogsportwhichreceivesPDUofitsown |         |            |         |        |
EventID:2804
| Message     | Port <portName>                         | enabled | after | disable time | expired |
| ----------- | --------------------------------------- | ------- | ----- | ------------ | ------- |
| Category    | LoopProtect                             |         |       |              |         |
| Severity    | Information                             |         |       |              |         |
| Description | Logsportenabledafterdisabledtimeexpired |         |       |              |         |
EventID:2805
143
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Port <portName> | added for | loop-protection |
| ----------- | --------------- | --------- | --------------- |
| Category    | LoopProtect     |           |                 |
| Severity    | Information     |           |                 |
| Description | Logsportadded   |           |                 |
EventID:2806
| Message     | Port <portName> | deleted | from loop-protection |
| ----------- | --------------- | ------- | -------------------- |
| Category    | LoopProtect     |         |                      |
| Severity    | Information     |         |                      |
| Description | Logsportdeleted |         |                      |
EventID:2807
| Message     | Loop-Protection                    | stats cleared | for port <portName> |
| ----------- | ---------------------------------- | ------------- | ------------------- |
| Category    | LoopProtect                        |               |                     |
| Severity    | Information                        |               |                     |
| Description | Loop-Protectionstatsclearedforport |               |                     |
EventID:2808
Message Ports TX <txportName> and RX <rxportName> are involved during TX port
disabling
| Category    | LoopProtect                                  |     |     |
| ----------- | -------------------------------------------- | --- | --- |
| Severity    | Information                                  |     |     |
| Description | LogsTXandRXportsafterTXdisabledbyLoopprotect |     |     |
LoopProtectevents|144

Chapter 58
Loopback events
Loopback events
Thefollowingaretheeventsrelatedtoloopback.
EventID:901
| Message     | Loopback Interface                | <interface>, | created |
| ----------- | --------------------------------- | ------------ | ------- |
| Category    | Loopback                          |              |         |
| Severity    | Information                       |              |         |
| Description | Logwhenloopbackinterfaceiscreated |              |         |
EventID:902
| Message     | Loopback Interface                | <interface>, | deleted |
| ----------- | --------------------------------- | ------------ | ------- |
| Category    | Loopback                          |              |         |
| Severity    | Information                       |              |         |
| Description | Logwhenloopbackinterfaceisdeleted |              |         |
EventID:903
Message Loopback Interface <interface>, configured administratively <state>
| Category    | Loopback                            |     |     |
| ----------- | ----------------------------------- | --- | --- |
| Severity    | Information                         |     |     |
| Description | Logaboutloopbackinterfaceadminstate |     |     |
145
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 59
|             |            |        | MAC address | management | events |
| ----------- | ---------- | ------ | ----------- | ---------- | ------ |
| MAC address | management | events |             |            |        |
ThefollowingaretheeventsrelatedtoMACaddressmanagement.
EventID:4801
Message MAC <mac> moved from port <from-intf> to port <to-intf> on VLAN <vlan>
| Category    | MACaddressmanagement     |     |     |     |     |
| ----------- | ------------------------ | --- | --- | --- | --- |
| Severity    | Information              |     |     |     |     |
| Description | EventraisedwhenL2macmove |     |     |     |     |
EventID:4802
Message All dynamic MAC addresses on VLAN <vlan> were flushed
| Category | MACaddressmanagement |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- |
| Severity | Information          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithvlandeleteeventorclearmac-address
commandfromvtysh
EventID:4803
Message All dynamic MAC addresses on port <intf> were flushed
| Category | MACaddressmanagement |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- |
| Severity | Information          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithportmovetoL3eventorclearmac-
addresscommandfromvtysh
EventID:4804
Message All dynamic MAC addresses on port <intf> were flushed
| Category | MACaddressmanagement |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- |
| Severity | Information          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithportdowneventorclearmac-address
commandfromvtysh
EventID:4805
146
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Message All dynamic MAC addresses on VLAN <vlan> were flushed
| Category | MACaddressmanagement |     |     |     |
| -------- | -------------------- | --- | --- | --- |
| Severity | Information          |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithvlandowneventorclearmac-address
commandfromvtysh
EventID:4806(Severity:Warning)
| Message  | L2X thread           | not running. | Attempting | to recover |
| -------- | -------------------- | ------------ | ---------- | ---------- |
| Category | MACaddressmanagement |              |            |            |
| Severity | Warning              |              |            |            |
Description EventraisedwhenBCML2Xthreadisidentifiedasnotrunning
EventID:4807(Severity:Warning)
| Message  | L2X thread           | recovered |     |     |
| -------- | -------------------- | --------- | --- | --- |
| Category | MACaddressmanagement |           |     |     |
| Severity | Warning              |           |     |     |
Description EventraisedwhenBCML2Xthreadissuccessfullyrecovered
EventID:4808
| Message     | L2X thread                                       | recovery failed |     |     |
| ----------- | ------------------------------------------------ | --------------- | --- | --- |
| Category    | MACaddressmanagement                             |                 |     |     |
| Severity    | Error                                            |                 |     |     |
| Description | EventraisedwhenBCML2Xthreadisfailedtoberecovered |                 |     |     |
MACaddressmanagementevents|147

Chapter 60
|     |     | MAC | Address | mode | configuration |
| --- | --- | --- | ------- | ---- | ------------- |
events
| MAC Address | mode configuration | events |     |     |     |
| ----------- | ------------------ | ------ | --- | --- | --- |
ThefollowingaretheeventsrelatedtoMACAddressmodeconfiguration.
EventID:11001
Message The MAC Address configured mode changed from <old_mode> to <new_mode>
| Category    | MACAddressmodeconfiguration                      |     |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- | --- |
| Severity    | Information                                      |     |     |     |     |
| Description | LogeventwhentheMACAddressconfiguredmodeischanged |     |     |     |     |
EventID:11002
Message The MAC Address operational mode changed from <old_mode> to <new_mode>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Information                 |     |     |     |     |
Description LogeventwhentheMACAddressoperationalmodeischanged
EventID:11003
Message Station MAC add failure due to hardware full, mac=<mac> vlan=<vlan>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Error                       |     |     |     |     |
Description LogeventwhenalocalstationMACaddresscannotbeaddedbecausethetableisfull
EventID:11004
Message The MAC Address operational mode changed from <old_mode> to <new_mode>
|          | due to reaching             | SVI threshold. | Current=<current> | Max=<max> |     |
| -------- | --------------------------- | -------------- | ----------------- | --------- | --- |
| Category | MACAddressmodeconfiguration |                |                   |           |     |
| Severity | Error                       |                |                   |           |     |
Description LogeventwhentheMACAddressoperationalmodeischangedduetooutofresources
148
| AOS-CXEventLogMessageReferenceGuide10.09| | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------- | ----------------------------- | --- | --- | --- | --- |

Chapter 61

MACsec events

MACsec events

The following are the events related to MACsec.

Event ID: 11201

Message

MACsec session established on Rx Secure Channel <sci> on interface
<ifname>.

Category

MACsec

Severity

Information

Description

A MACsec session established on an interface.

Event ID: 11202

Message

MKA session secured for Connectivity Association <ckn> on interface
<ifname>.

Category

MACsec

Severity

Information

Description

A Connectivity Association was successfully established on an interface.

Event ID: 11203

Message

Secure Association key updated for Connectivity Association <ckn> on
interface <ifname> - Latest AN/KN <latest_an>/<latest_kn>, Old AN/KN
<old_an>/<old_kn>.

Category

MACsec

Severity

Information

Description

A new Secure Association key created for a Connectivity Association.

Event ID: 11204

Message

Possible replay attempt detected on the Secure Channel <sci>.

Category

MACsec

Severity

Information

Description

A possible replay attempt detected on a Secure Channel.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

149

Event ID: 11205

Message

The data traffic on interface <ifname> is now secured by MACsec.

Category

MACsec

Severity

Information

Description

The data plane traffic on an interface is secured by MACsec.

Event ID: 11206

Message

The data traffic on interface <ifname> is no longer secured by MACsec.

Category

MACsec

Severity

Information

Description

The data plane traffic on an interface is not secured by MACsec anymore.

Event ID: 11204

Message

Possible replay attempt detected on the Secure Channel <sci>.

Category

MACsec

Severity

Information

Description

A possible replay attempt detected on a Secure Channel.

MACsec events | 150

Chapter 62
Management events
| Management events |     |     |
| ----------------- | --- | --- |
Thefollowingaretheeventsrelatedtomanagement.
EventID:4301
| Message     | MGMT_INTF:                                     | <mgmt_intf_config_param> |
| ----------- | ---------------------------------------------- | ------------------------ |
| Category    | Management                                     |                          |
| Severity    | Information                                    |                          |
| Description | Logsrelatedtomanagementinterfaceconfigurations |                          |
EventID:4302
| Message  | MGMT_INTF: | <mgmt_intf_config_err> |
| -------- | ---------- | ---------------------- |
| Category | Management |                        |
| Severity | Error      |                        |
Description Logsrelatedtomanagementinterfaceconfigurationserror
EventID:4303(Severity:Critical)
| Message  | MGMT_INTF: | <mgmt_intf_config_crit> |
| -------- | ---------- | ----------------------- |
| Category | Management |                         |
| Severity | Critical   |                         |
Description Logsrelatedtomanagementinterfacecriticalconfigurations
151
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 63

MDNS events

MDNS events

The following are the events related to MDNS.

Event ID: 11401

Message

mDNS-SD enabled

Category

MDNS

Severity

Information

Description

Logs event when mDNS-SD feature is enabled in the switch.

Event ID: 11402

Message

mDNS-SD disabled

Category

MDNS

Severity

Information

Description

Logs event when mDNS-SD feature is disabled in the switch.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

152

Chapter 64
MGMD events
MGMD events
ThefollowingaretheeventsrelatedtoMGMD.
EventID:2601(Severity:Fatal)
| Message  | Failed | to alloc a <pkt_type> | pkt(interface | <vlan>) |
| -------- | ------ | --------------------- | ------------- | ------- |
| Category | MGMD   |                       |               |         |
| Severity | Fatal  |                       |               |         |
Description ThislogeventinformspacketallocationfailedinMGMDsubsystem.
EventID:2602
Message Received IGMPv1 query from <ip_address> when the device is configured
for IGMPv2.
| Category | MGMD        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventusedtologIGMPwarningwhenIGMPv1queryisreceived.
EventID:2603(Severity:Fatal)
Message Unable to alloc a buf of size <size_value> for <sub_system>
| Category | MGMD  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Fatal |     |     |     |
Description ThislogeventinformstheuserthatMGMDcouldnotallocatememory.
EventID:2604
Message Interface <if_name>: Other Querier detected for <mgmd_type>
| Category | MGMD        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatIGMP/MLDdetectedotherquerier.
EventID:2605
153
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message <mgmd_type> Querier Election in progress for interface <if_name> with
|          | IP address  | <ip_address> |     |     |
| -------- | ----------- | ------------ | --- | --- |
| Category | MGMD        |              |     |     |
| Severity | Information |              |     |     |
Description ThislogeventinformstheuserthatIGMP/MLDhasstartedquerierelectiononinterface.
EventID:2606
| Message  | Interface   | <if_name>: | End <mgmd_type> | Querier role |
| -------- | ----------- | ---------- | --------------- | ------------ |
| Category | MGMD        |            |                 |              |
| Severity | Information |            |                 |              |
Description ThislogeventinformstheuserthatIGMP/MLDendedquerierroleoninterface.
EventID:2607
Message Interface <if_name>: Start <mgmd_type> Querier role addr: <ip_address>
| Category | MGMD        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatMGMDstartedquerierroleoninterface.
EventID:2608(Severity:Warning)
Message Received packet from <ip_address>, type <type>, on invalid port <port>
| Category | MGMD    |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description ThislogeventinformstheuserthatMGMDreceivedpacketoninvalidport.
EventID:2609
Message Received IGMPv1 query from <ip_address> when the device is configured
|          | for IGMPv3.' | throttle_count: | 1   |     |
| -------- | ------------ | --------------- | --- | --- |
| Category | MGMD         |                 |     |     |
| Severity | Information  |                 |     |     |
Description ThislogeventusedtologIGMPwarningwhenconfiguredmodeisIGMPv3andIGMPv1
queryisreceived.
EventID:2610
MGMDevents|154

Message Received IGMPv2 query from <ip_address> when the device is configured
|          | for IGMPv3.' | throttle_count: | 1   |     |
| -------- | ------------ | --------------- | --- | --- |
| Category | MGMD         |                 |     |     |
| Severity | Information  |                 |     |     |
Description ThislogeventusedtologIGMPwarningwhenconfiguredmodeisIGMPv3andIGMPv2
queryisreceived.
EventID:2611
| Message  | <mgmd_type> | snooping | is <status> | on VLAN <vlan> |
| -------- | ----------- | -------- | ----------- | -------------- |
| Category | MGMD        |          |             |                |
| Severity | Information |          |             |                |
Description ThislogeventinformstheuserthatIGMP/MLDstatusonVLAN.
EventID:2612
| Message  | <mgmd_type> | is <status> | on Interface | <if_name> |
| -------- | ----------- | ----------- | ------------ | --------- |
| Category | MGMD        |             |              |           |
| Severity | Information |             |              |           |
Description ThislogeventinformstheusertheIGMP/MLDstatusontheInterface.
EventID:2613
Message Port <port> on vlan <vlan> is set to <status> mode for <mgmd_type>.
| Category | MGMD        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Thislogeventinformstheuserthattheportmodehaschanged.
EventID:2614
Message <mgmd_type> is not operational on VLAN <vlan> due to resource
unavailability
| Category | MGMD  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description ThislogeventinformstheuserthattheIGMP/MLDisdisabledonaVLANduetointernal
errors.
EventID:2615
155
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message <mgmd_type> is not operational on interface <l3Port> due to resource
unavailability
| Category | MGMD  |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
| Severity | Error |     |     |     |     |
Description ThislogeventinformstheuserthattheIGMP/MLDisdisabledonaL3interfacedueto
internalerrors.
EventID:2616
Message IGMP/MLD Resource utilization has exceeded the supported limits on the
|          | system. Membership | reports | for the | new groups | will be dropped. |
| -------- | ------------------ | ------- | ------- | ---------- | ---------------- |
| Category | MGMD               |         |         |            |                  |
| Severity | Information        |         |         |            |                  |
Description ThislogeventinformstheuserthatMGMDresourceutilizationhasexceededthe
supportedlimits
EventID:2617
Message IGMP/MLD Resource utilization has reached 90 percent of the supported
|          | limits on   | the system. |     |     |     |
| -------- | ----------- | ----------- | --- | --- | --- |
| Category | MGMD        |             |     |     |     |
| Severity | Information |             |     |     |     |
Description ThislogeventinformstheuserthatMGMDresourceutilizationhasreached90percent
ofthesupportedlimits
EventID:2618
| Message  | <mgmd_type> | snooping | is <status> | on VLAN <vlan>. |     |
| -------- | ----------- | -------- | ----------- | --------------- | --- |
| Category | MGMD        |          |             |                 |     |
| Severity | Information |          |             |                 |     |
Description ThislogeventinformstheuserthatwhetherIGMP/MLDsnoopingisoperational.
EventID:2619
Message Received IGMPv3 query from <ip_address> when the device is configured
|          | for IGMPv2.' | throttle_count: | 1   |     |     |
| -------- | ------------ | --------------- | --- | --- | --- |
| Category | MGMD         |                 |     |     |     |
| Severity | Information  |                 |     |     |     |
Description ThislogeventusedtologIGMPwarningwhenIGMPv2queryisreceived.
MGMDevents|156

Event ID: 2620

Message

Received MLDV1 query from <ip_address> when the device is configured
for MLDV2.' throttle_count: 1

Category

MGMD

Severity

Information

Description

This log event used to log MLD warning when configured mode is MLDV2 and MLDV1
query is received.

Event ID: 2621

Message

Received MLDV2 query from <ip_address> when the device is configured
for MLDV1.' throttle_count: 1

Category

MGMD

Severity

Information

Description

This log event used to log MLD warning when configured mode is MLDv2 and MLDv1
query is received.

Event ID: 2622

Message

Flood mode is temporarily activated on ERPS ports <port0> and <port1>
as ring state for ring id <ring_id> changed to <state>.

Category

MGMD

Severity

Information

Description

This log event used to log if ERPS Ring state changed to idle or protection.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

157

Chapter 65
Mirroring events
Mirroring events
Thefollowingaretheeventsrelatedtomirroring.
EventID:6701
| Message     | Failed                                           | to create mirror | session <number> |
| ----------- | ------------------------------------------------ | ---------------- | ---------------- |
| Category    | Mirroring                                        |                  |                  |
| Severity    | Error                                            |                  |                  |
| Description | Logsamessagewhenthecreationofamirrorsessionfails |                  |                  |
EventID:6702
| Message  | Mirror      | session <number> | created |
| -------- | ----------- | ---------------- | ------- |
| Category | Mirroring   |                  |         |
| Severity | Information |                  |         |
Description Logsamessagewhenthecreationofamirrorsessionsucceeds
EventID:6703
| Message     | Failed                                           | to delete mirror | session <number> |
| ----------- | ------------------------------------------------ | ---------------- | ---------------- |
| Category    | Mirroring                                        |                  |                  |
| Severity    | Error                                            |                  |                  |
| Description | Logsamessagewhenthedeletionofamirrorsessionfails |                  |                  |
EventID:6704
| Message  | Mirror      | session <number> | deleted |
| -------- | ----------- | ---------------- | ------- |
| Category | Mirroring   |                  |         |
| Severity | Information |                  |         |
Description Logsamessagewhenmirrorsessionissuccessfullydeleted
EventID:6705
158
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Failed                                        | to update mirror | session <number> |
| ----------- | --------------------------------------------- | ---------------- | ---------------- |
| Category    | Mirroring                                     |                  |                  |
| Severity    | Error                                         |                  |                  |
| Description | Logsamessagewhenanupdateofamirrorsessionfails |                  |                  |
EventID:6706
| Message  | Mirror      | session <number> | updated |
| -------- | ----------- | ---------------- | ------- |
| Category | Mirroring   |                  |         |
| Severity | Information |                  |         |
Description Logsamessagewhentheupdateofamirrorsessionsucceeds
Mirroringevents|159

Chapter 66
Module events
Module events
Thefollowingaretheeventsrelatedtomodule.
EventID:3201
| Message     | <type> module                                   | <name> | inserted': yes |     |
| ----------- | ----------------------------------------------- | ------ | -------------- | --- |
| Category    | Module                                          |        |                |     |
| Severity    | Information                                     |        |                |     |
| Description | Indicatesthatthemodulehasbeenphysicallyinserted |        |                |     |
EventID:3202(Severity:Warning)
| Message     | <type> module                                  | <name> | removed': yes |     |
| ----------- | ---------------------------------------------- | ------ | ------------- | --- |
| Category    | Module                                         |        |               |     |
| Severity    | Warning                                        |        |               |     |
| Description | Indicatesthatthemodulehasbeenphysicallyremoved |        |               |     |
EventID:3203
| Message     | Initiating                            | <type> module | <name> reboot': | yes |
| ----------- | ------------------------------------- | ------------- | --------------- | --- |
| Category    | Module                                |               |                 |     |
| Severity    | Information                           |               |                 |     |
| Description | Indicatesthatthemoduleisabouttoreboot |               |                 |     |
EventID:3204
| Message     | <type> module                               | <name> | is ready |     |
| ----------- | ------------------------------------------- | ------ | -------- | --- |
| Category    | Module                                      |        |          |     |
| Severity    | Information                                 |        |          |     |
| Description | Indicatesthatthemoduleisinitializedandready |        |          |     |
EventID:3205
160
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | <type> module                | <name> | is down: <reason> |     |
| ----------- | ---------------------------- | ------ | ----------------- | --- |
| Category    | Module                       |        |                   |     |
| Severity    | Information                  |        |                   |     |
| Description | Indicatesthatthemoduleisdown |        |                   |     |
EventID:3206
| Message     | <type> module                           | <name> | is in diagnostics | mode |
| ----------- | --------------------------------------- | ------ | ----------------- | ---- |
| Category    | Module                                  |        |                   |      |
| Severity    | Information                             |        |                   |      |
| Description | Indicatesthatamoduleisindiagnosticsmode |        |                   |      |
EventID:3207
| Message     | <type> module                 | <name> | has failed: <reason>': | yes |
| ----------- | ----------------------------- | ------ | ---------------------- | --- |
| Category    | Module                        |        |                        |     |
| Severity    | Error                         |        |                        |     |
| Description | Indicatesthatamodulehasfailed |        |                        |     |
EventID:3208
| Message     | <type> module                                      | <name> | admin state set | to up |
| ----------- | -------------------------------------------------- | ------ | --------------- | ----- |
| Category    | Module                                             |        |                 |       |
| Severity    | Information                                        |        |                 |       |
| Description | Indicatesthatthemoduleadministrativestateissettoup |        |                 |       |
EventID:3209
| Message  | <type> module | <name> | admin state set | to down |
| -------- | ------------- | ------ | --------------- | ------- |
| Category | Module        |        |                 |         |
| Severity | Information   |        |                 |         |
Description Indicatesthatthemoduleadministrativestateissettodown
EventID:3210
| Message | <type> module | <name> | admin state set | to diagnostics |
| ------- | ------------- | ------ | --------------- | -------------- |
Moduleevents|161

| Category | Module      |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Indicatesthatthemoduleadministrativestateissettodiagnostics
EventID:3211
| Message     | <type> module                         | <name> ISP | passed |     |
| ----------- | ------------------------------------- | ---------- | ------ | --- |
| Category    | Module                                |            |        |     |
| Severity    | Information                           |            |        |     |
| Description | IndicatesthatISPhaspassedforthemodule |            |        |     |
EventID:3212
| Message     | <type> module                         | <name> ISP | failed': yes |     |
| ----------- | ------------------------------------- | ---------- | ------------ | --- |
| Category    | Module                                |            |              |     |
| Severity    | Error                                 |            |              |     |
| Description | IndicatesthatISPhasfailedforthemodule |            |              |     |
EventID:3213(Severity:Warning)
| Message     | <type> module                              | <name> ISP | skipped |     |
| ----------- | ------------------------------------------ | ---------- | ------- | --- |
| Category    | Module                                     |            |         |     |
| Severity    | Warning                                    |            |         |     |
| Description | IndicatesthatISPhasbeenskippedforthemodule |            |         |     |
EventID:3214
| Message     | <type> module                                    | <name> has | enabled standby | power |
| ----------- | ------------------------------------------------ | ---------- | --------------- | ----- |
| Category    | Module                                           |            |                 |       |
| Severity    | Debug                                            |            |                 |       |
| Description | Indicatesthatthemoduleisinstandby(low-power)mode |            |                 |       |
EventID:3215
Message <type> module <name> is requesting to power on with priority <priority>
| Category | Module |     |     |     |
| -------- | ------ | --- | --- | --- |
162
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Debug                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Description | Indicatesthatthemoduleisrequestingtopoweron |     |     |     |
EventID:3216
| Message  | <type> module | <name> power | request has | been granted |
| -------- | ------------- | ------------ | ----------- | ------------ |
| Category | Module        |              |             |              |
| Severity | Debug         |              |             |              |
Description Indicatesthatthepowerrequestforthemodulehasbeengranted
EventID:3217
| Message  | <type> module | <name> power | request has | been denied |
| -------- | ------------- | ------------ | ----------- | ----------- |
| Category | Module        |              |             |             |
| Severity | Error         |              |             |             |
Description Indicatesthatthepowerrequestforthemodulehasbeendenied
EventID:3218
| Message     | <type> module                                    | <name> enabling | main power |     |
| ----------- | ------------------------------------------------ | --------------- | ---------- | --- |
| Category    | Module                                           |                 |            |     |
| Severity    | Debug                                            |                 |            |     |
| Description | Indicatesthatmainpowerforthemoduleisbeingenabled |                 |            |     |
EventID:3219
| Message     | <type> module                                    | <name> main | power enabled |     |
| ----------- | ------------------------------------------------ | ----------- | ------------- | --- |
| Category    | Module                                           |             |               |     |
| Severity    | Debug                                            |             |               |     |
| Description | Indicatesthatmainpowerforthemodulehasbeenenabled |             |               |     |
EventID:3220
| Message     | <type> module                               | <name> main | power failed': | yes |
| ----------- | ------------------------------------------- | ----------- | -------------- | --- |
| Category    | Module                                      |             |                |     |
| Severity    | Error                                       |             |                |     |
| Description | Indicatesthatmainpowerforthemodulehasfailed |             |                |     |
Moduleevents|163

EventID:3221
| Message  | <type> module | <name> device | initialization | started |
| -------- | ------------- | ------------- | -------------- | ------- |
| Category | Module        |               |                |         |
| Severity | Debug         |               |                |         |
Description Indicatesthatdeviceinitializationforthemodulehasstarted
EventID:3222
| Message  | <type> module | <name> device | initialization | passed |
| -------- | ------------- | ------------- | -------------- | ------ |
| Category | Module        |               |                |        |
| Severity | Debug         |               |                |        |
Description Indicatesthatdeviceinitializationforthemodulehaspassed
EventID:3223
Message <type> module <name> device initialization failed: <reason>': yes
| Category | Module |     |     |     |
| -------- | ------ | --- | --- | --- |
| Severity | Error  |     |     |     |
Description Indicatesthatdeviceinitializationforthemodulehasfailed
EventID:3224
| Message     | <type> module                                     | <name> ASIC | initialization | started |
| ----------- | ------------------------------------------------- | ----------- | -------------- | ------- |
| Category    | Module                                            |             |                |         |
| Severity    | Information                                       |             |                |         |
| Description | IndicatesthatanASICforthemoduleisbeinginitialized |             |                |         |
EventID:3225
| Message  | <type> module | <name> ASIC | initialization | completed |
| -------- | ------------- | ----------- | -------------- | --------- |
| Category | Module        |             |                |           |
| Severity | Debug         |             |                |           |
Description IndicatesthatASICinitializationforthemodulehascompleted
EventID:3226
164
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message <type> module <name> ASIC initialization failed: <reason>': yes
| Category    | Module                                               |     |     |     |
| ----------- | ---------------------------------------------------- | --- | --- | --- |
| Severity    | Error                                                |     |     |     |
| Description | IndicatesthatASICinitializationforthemodulehasfailed |     |     |     |
EventID:3227
| Message  | <type> | module <name> ASIC | deinitialization | started |
| -------- | ------ | ------------------ | ---------------- | ------- |
| Category | Module |                    |                  |         |
| Severity | Debug  |                    |                  |         |
Description IndicatesthatanASICforthemoduleisbeingdeinitialized
EventID:3228
| Message  | <type> | module <name> ASIC | deinitialization | completed |
| -------- | ------ | ------------------ | ---------------- | --------- |
| Category | Module |                    |                  |           |
| Severity | Debug  |                    |                  |           |
Description IndicatesthatASICdeinitializationforthemodulehascompleted
EventID:3229
Message <type> module <name> ASIC denitialization failed: <reason>': yes
| Category | Module |     |     |     |
| -------- | ------ | --- | --- | --- |
| Severity | Error  |     |     |     |
Description IndicatesthatASICdeinitializationforthemodulehasfailed
EventID:3230
| Message     | <name>                                          | is starting zeroization': | yes |     |
| ----------- | ----------------------------------------------- | ------------------------- | --- | --- |
| Category    | Module                                          |                           |     |     |
| Severity    | Information                                     |                           |     |     |
| Description | Indicatesthatthemoduleisabouttostartzeroization |                           |     |     |
EventID:3231
| Message | <name> | zeroization completed. |     |     |
| ------- | ------ | ---------------------- | --- | --- |
Moduleevents|165

| Category    | Module                                        |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | Indicatesthatthemodulezeroizationhascompleted |     |     |     |
EventID:3232
| Message     | <name> zeroization                                | failed.': |     | yes |
| ----------- | ------------------------------------------------- | --------- | --- | --- |
| Category    | Module                                            |           |     |     |
| Severity    | Information                                       |           |     |     |
| Description | Indicatesthatthemodulezeroizationfailedtocomplete |           |     |     |
EventID:3233
Message <type> module <name> configured with product number <part_number>
| Category    | Module                                  |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Indicatesthatthemodulehasbeenconfigured |     |     |     |
EventID:3234
| Message     | <type> module                             | <name> has | been | unconfigured |
| ----------- | ----------------------------------------- | ---------- | ---- | ------------ |
| Category    | Module                                    |            |      |              |
| Severity    | Information                               |            |      |              |
| Description | Indicatesthatthemodulehasbeenunconfigured |            |      |              |
EventID:3235
| Message     | <type> module                            | <name> initiating |     | failover |
| ----------- | ---------------------------------------- | ----------------- | --- | -------- |
| Category    | Module                                   |                   |     |          |
| Severity    | Information                              |                   |     |          |
| Description | Indicatesthatthemodulehasstartedfailover |                   |     |          |
EventID:3236
| Message  | <type> module | <name> failover |     | completed |
| -------- | ------------- | --------------- | --- | --------- |
| Category | Module        |                 |     |           |
166
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Information                                |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Description | Indicatesthatthemodulehascompletedfailover |     |     |     |
EventID:3237
| Message     | <type> module                          | <name> initiating | ISP |     |
| ----------- | -------------------------------------- | ----------------- | --- | --- |
| Category    | Module                                 |                   |     |     |
| Severity    | Information                            |                   |     |     |
| Description | IndicatesthatISPhasstartedforthemodule |                   |     |     |
EventID:3238
| Message     | <type> module                             | <name> enabling | front-end | power |
| ----------- | ----------------------------------------- | --------------- | --------- | ----- |
| Category    | Module                                    |                 |           |       |
| Severity    | Information                               |                 |           |       |
| Description | Indicatesthatfront-endpowerisbeingenabled |                 |           |       |
EventID:3239(Severity:Warning)
Message <type> module <name> disabling front-end power: <reason>
| Category    | Module                                     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Warning                                    |     |     |     |
| Description | Indicatesthatfront-endpowerisbeingdisabled |     |     |     |
EventID:3240
| Message     | <type> module                                   | <name> has | persistent | hardware error |
| ----------- | ----------------------------------------------- | ---------- | ---------- | -------------- |
| Category    | Module                                          |            |            |                |
| Severity    | Error                                           |            |            |                |
| Description | Indicatesthatpersistenthardwareerrorhasoccurred |            |            |                |
Moduleevents|167

Chapter 67

MPLS events

MPLS events

The following are the events related to MPLS.

Event ID: 13301

Message

MPLS LDP session with local identifier <local_ldp_id> and peer
identifier <peer_ldp_id> has come up.

Category

MPLS

Severity

Information

Description

Logs a message when an LDP neighbor comes up

Event ID: 13302

Message

MPLS LDP session with local identifier <local_ldp_id> and peer
identifier <peer_ldp_id> has gone down.

Category

MPLS

Severity

Information

Description

Logs a message when an LDP neighbor goes down

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

168

Chapter 68
MSDP events
MSDP events
ThefollowingaretheeventsrelatedtoMSDP.
EventID:8601
| Message     | Router MSDP                   | is <status> | on VRF <vrf_name> |     |
| ----------- | ----------------------------- | ----------- | ----------------- | --- |
| Category    | MSDP                          |             |                   |     |
| Severity    | Information                   |             |                   |     |
| Description | Routermsdpconfigurationstatus |             |                   |     |
EventID:8602
Message Forwarding state of interface <if_name> has been changed to <state>
| Category    | MSDP                                 |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | MSDPSourceInterfaceoperationalstatus |     |     |     |
EventID:8603
Message MSDP Peer <peer_ip>(<tcp_entity>) with connection source <if_name> has
|             | entered <state>                          | state |     |     |
| ----------- | ---------------------------------------- | ----- | --- | --- |
| Category    | MSDP                                     |       |     |     |
| Severity    | Information                              |       |     |     |
| Description | LogsthechangesinMSDPPeerconnectionstate. |       |     |     |
EventID:8604
| Message     | Port <port>                               | is <status> | to MSDP Peer | <peer_ip> |
| ----------- | ----------------------------------------- | ----------- | ------------ | --------- |
| Category    | MSDP                                      |             |              |           |
| Severity    | Information                               |             |              |           |
| Description | Logeventwhenportisaddedordeletedforapeer. |             |              |           |
EventID:8606
169
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message MSDP Peer <peer_ip> is <status> on VRF <vrf_name>. Interface <if_name>
|             | is added to                         | the Peer |     |     |
| ----------- | ----------------------------------- | -------- | --- | --- |
| Category    | MSDP                                |          |     |     |
| Severity    | Information                         |          |     |     |
| Description | Logeventwhenpeerisenabledordisabled |          |     |     |
EventID:8607
| Message     | Start <tcp_entity>                  | role | for MSDP peer | <peer_ip> |
| ----------- | ----------------------------------- | ---- | ------------- | --------- |
| Category    | MSDP                                |      |               |           |
| Severity    | Information                         |      |               |           |
| Description | Logeventwhenclientorserveriselected |      |               |           |
EventID:8608
| Message     | Finish packet                         | was received | on MSDP | Peer <peer_ip> |
| ----------- | ------------------------------------- | ------------ | ------- | -------------- |
| Category    | MSDP                                  |              |         |                |
| Severity    | Information                           |              |         |                |
| Description | LogeventwhenTCPfinalpacketisreceived. |              |         |                |
EventID:8609(Severity:Warning)
Message Failed to add SA Cache entry: S=<src_ip>, G=<grp_ip>, R=<rp_ip> for
|             | Peer <peer_ip>                         | as MSDP | SA Cache Limit | is reached |
| ----------- | -------------------------------------- | ------- | -------------- | ---------- |
| Category    | MSDP                                   |         |                |            |
| Severity    | Warning                                |         |                |            |
| Description | LogeventwhenMSDPSAcachelimitisreached. |         |                |            |
MSDPevents|170

Chapter 69
|           |                 |        | Multicast | Traffic | Manager | events |
| --------- | --------------- | ------ | --------- | ------- | ------- | ------ |
| Multicast | Traffic Manager | events |           |         |         |        |
ThefollowingaretheeventsrelatedtoMulticastTrafficManager.
EventID:4001(Severity:Warning)
Message The Multicast L3 Bridge Control Forwarding entries limit was reached:
|     | <limit>' | throttle_count: | 100 |     |     |     |
| --- | -------- | --------------- | --- | --- | --- | --- |
Category MulticastTrafficManager
Severity Warning
Description EventraisedwhenthemaximumnumberofmulticastL3BridgeControlForwarding
entriesisreached
171
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

Chapter 70
|          |          |               | Multiple | spanning | tree protocol | events |
| -------- | -------- | ------------- | -------- | -------- | ------------- | ------ |
| Multiple | spanning | tree protocol | events   |          |               |        |
Thefollowingaretheeventsrelatedtomultiplespanningtreeprotocol.
EventID:2001
| Message  |     | MSTP Enabled                 |     |     |     |     |
| -------- | --- | ---------------------------- | --- | --- | --- | --- |
| Category |     | Multiplespanningtreeprotocol |     |     |     |     |
| Severity |     | Information                  |     |     |     |     |
Description ThiscommandenablestheMSTP(MultipleSpanning-treeProtocol)featureinthedevice.
EventID:2002
| Message  |     | MSTP Disabled                |     |     |     |     |
| -------- | --- | ---------------------------- | --- | --- | --- | --- |
| Category |     | Multiplespanningtreeprotocol |     |     |     |     |
| Severity |     | Information                  |     |     |     |     |
Description ThiscommanddisablestheMSTP(MultipleSpanning-treeProtocol)featureinthedevice.
EventID:2003(Severity:Warning)
| Message  |     | <config_parameter>           | should | be <value> |     |     |
| -------- | --- | ---------------------------- | ------ | ---------- | --- | --- |
| Category |     | Multiplespanningtreeprotocol |        |            |     |     |
| Severity |     | Warning                      |        |            |     |     |
Description ThislogeventinformstheuserthattheMSTPconfigparameterisbad
EventID:2004(Severity:Warning)
| Message  |     | BPDU has <config_parameter>  |     | from port | <value> |     |
| -------- | --- | ---------------------------- | --- | --------- | ------- | --- |
| Category |     | Multiplespanningtreeprotocol |     |           |         |     |
| Severity |     | Warning                      |     |           |         |     |
Description ThislogeventinformstheuserthattheSwitchreceivedaBPDUwithabadconfig
EventID:2005(Severity:Warning)
172
| AOS-CXEventLogMessageReferenceGuide10.09| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

| Message  | Bad reconfiguration          | request: <reconfig_parameter> |
| -------- | ---------------------------- | ----------------------------- |
| Category | Multiplespanningtreeprotocol |                               |
| Severity | Warning                      |                               |
Description ThislogeventinformstheuserthattheMSTPreconfigparameterisbad
EventID:2006
Message <proto> - Root changed from <old_priority>: <old_mac> to <new_
priority>: <new_mac>
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Information                  |     |
Description ThislogeventinformstheuserthattheMSTProothaschanged
EventID:2007(Severity:Warning)
Message Port <port> disabled - BPDU received on protected port
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Warning                      |     |
Description ThislogeventinformstheuserthatBPDUwasreceivedonprotectedport
EventID:2008
Message <proto> starved for <pkt_type> on port <port> from <priority_mac>
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Information                  |     |
Description ThislogeventinformstheuserthattheRxqueueisstarvedinthepaticularport
EventID:2009
Message BPDU loss- port <port> moved to inconsistent state for <proto>
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Information                  |     |
Description Thislogeventinformstheuserthattheportisininconsistentstate
EventID:2010
Multiplespanningtreeprotocolevents|173

Message Port <port> moved out of inconsistent state for <proto>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description ThislogeventinformstheuserthattheMSTPisoutofinconsistentstate
EventID:2011
Message Topology Change received on port <port> for <proto> from source: <mac>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description ThislogeventinformstheuserthattheMSTPtopologychangeisreceived
EventID:2012
Message <proto> - Topology Change generated on port <port> going in to <state>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description ThislogeventinformstheuserthattheMSTPtopologychangeisgenerated
EventID:2013
| Message  | BPDU received                | on admin | edge port <port> |
| -------- | ---------------------------- | -------- | ---------------- |
| Category | Multiplespanningtreeprotocol |          |                  |
| Severity | Information                  |          |                  |
Description ThislogeventinformstheuserthataBPDUwasreceivedonadminedgeport
EventID:2014
| Message  | Port <port>                  | blocked | on CIST |
| -------- | ---------------------------- | ------- | ------- |
| Category | Multiplespanningtreeprotocol |         |         |
| Severity | Information                  |         |         |
Description ThislogeventinformstheuserthattheCISTportisblocked
EventID:2015
| Message | Port <port> | unblocked | on CIST |
| ------- | ----------- | --------- | ------- |
174
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description ThislogeventinformstheuserthattheCISTportisunblocked
EventID:2016
| Message  | Port <port>                  | blocked | on MST<instance> |
| -------- | ---------------------------- | ------- | ---------------- |
| Category | Multiplespanningtreeprotocol |         |                  |
| Severity | Information                  |         |                  |
Description ThislogeventinformstheuserthattheMSTIportisblocked
EventID:2017
| Message  | Port <port>                  | unblocked | on MST<instance> |
| -------- | ---------------------------- | --------- | ---------------- |
| Category | Multiplespanningtreeprotocol |           |                  |
| Severity | Information                  |           |                  |
Description ThislogeventinformstheuserthattheMSTIportisunblocked
EventID:2018
Message <proto> Root Port changed from <old_port> to <new_port>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description Thislogeventinformstheuserthattherootportischanged
EventID:2019
Message spanning tree mode changed from <old_mode> to <new_mode>, it will
|          | trigger the                  | reconvergence |     |
| -------- | ---------------------------- | ------------- | --- |
| Category | Multiplespanningtreeprotocol |               |     |
| Severity | Information                  |               |     |
Description Thislogeventinformstheuserthatthespanningtreemodeischanged.
Multiplespanningtreeprotocolevents|175

Chapter 71
MVRP events
MVRP events
ThefollowingaretheeventsrelatedtoMVRP.
EventID:3101
| Message  | MVRP enabled | on port <port> |     |     |
| -------- | ------------ | -------------- | --- | --- |
| Category | MVRP         |                |     |     |
| Severity | Information  |                |     |     |
Description ThiscommandenablestheMVRP(MultipleVLANRegistrationProtocol)featureon
interface.
EventID:3102
| Message  | MVRP disabled | on port <port> |     |     |
| -------- | ------------- | -------------- | --- | --- |
| Category | MVRP          |                |     |     |
| Severity | Information   |                |     |     |
Description ThiscommanddisablestheMVRP(MultipleVLANRegistrationProtocol)featureon
interface.
EventID:3103
Message MVRP failed to create VLAN <vlan>. Maximum VLANs <max_vlan> already
|             | created' throttle_count:                          |     | 100 |     |
| ----------- | ------------------------------------------------- | --- | --- | --- |
| Category    | MVRP                                              |     |     |     |
| Severity    | Information                                       |     |     |     |
| Description | Thislogeventinformsuserthatthevlancreateisfailed. |     |     |     |
EventID:3104
| Message  | MVRP statistics | have been | cleared for | port <port> |
| -------- | --------------- | --------- | ----------- | ----------- |
| Category | MVRP            |           |             |             |
| Severity | Information     |           |             |             |
Description Thislogeventinformsuserthatthemvrpstatisticshavebeencleared.
EventID:3105
176
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

MVRP statistics have been cleared for <port> ports

Category

MVRP

Severity

Information

Description

This log event informs user that the mvrp statistics have been cleared.

MVRP events | 177

Chapter 72

NAE Agents events

NAE Agents events

The following are the events related to NAE agents.

Event ID: 6901

Message

An action has been triggered by the NAE agent <name>': yes

Category

NAE Agents

Severity

Information

Description

Action has been triggered by an NAE agent

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

178

Chapter 73

NAE events

NAE events

The following are the events related to Network Analytics Engine.

Event ID: 6001

Message

NAE agent <name> started to collect samples from <uri>.

Category

NAE

Severity

Information

Description

NAE agent started to collect samples.

Event ID: 6002

Message

NAE agent <name> stopped to collect samples from <uri>.

Category

NAE

Severity

Information

Description

NAE agent stooped to collect samples.

Event ID: 6003

Message

NAE agent <name> with URI <uri> has error and cannot collect samples.

Category

Severity

NAE

Error

Description

NAE agent with URI has error and cannot collect samples.

Event ID: 6004

Message

NAE agent <name> is watching for condition <condition>.

Category

NAE

Severity

Information

Description

NAE agent is watching for condition.

Event ID: 6005

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

179

Message

NAE agent <name> stopped to watch for condition <condition>.

Category

NAE

Severity

Information

Description

NAE agent stopped to watch for condition.

Event ID: 6006

Message

Category

Severity

NAE agent <name> with condition <condition> has error and is not
watched.

NAE

Error

Description

NAE agent with condition has error and is not watched.

Event ID: 6007

Message

NAE agent <name> generated an alert based on condition <condition>.

Category

NAE

Severity

Information

Description

NAE agent generated an alert based on condition.

Event ID: 6008 (Severity: Warning)

Message

NAE experiencing a spike in data points to process for NAE monitor
<monitorName>. NAE will temporarily stop monitoring new data points for
<monitorName>.

Category

NAE

Severity

Warning

Description

NAE experiencing a spike in data points to process. Temporarily disabling processing
updates from specific NAE monitor.

Event ID: 6009

Message

NAE resuming to monitor data points from NAE monitor <monitorName>

Category

NAE

Severity

Information

Description

NAE resuming to monitor data points from specific NAE monitor.

Event ID: 6010

NAE events | 180

| Message  | User <user> | has cleard | NAE time series | database |
| -------- | ----------- | ---------- | --------------- | -------- |
| Category | NAE         |            |                 |          |
| Severity | Information |            |                 |          |
Description LogsamessagewhenauserclearstheNAEtimeseriesdatabase
181
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 74
|            |            |        | NAE script | generation | events |
| ---------- | ---------- | ------ | ---------- | ---------- | ------ |
| NAE script | generation | events |            |            |        |
ThefollowingaretheeventsrelatedtoNAEscriptgeneration.
EventID:12701
| Message     | NAE                    | agent <agent> creation | failed. Reason | <reason> |     |
| ----------- | ---------------------- | ---------------------- | -------------- | -------- | --- |
| Category    | NAEscriptgeneration    |                        |                |          |     |
| Severity    | Error                  |                        |                |          |     |
| Description | NAEagentcreationfailed |                        |                |          |     |
182
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Chapter 75
NAE Scripts events
| NAE Scripts events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoNetworkAnalyticsEnginescripts.
EventID:5501
| Message     | NAE script                 | <name> has | been validated. |     |
| ----------- | -------------------------- | ---------- | --------------- | --- |
| Category    | NAEScripts                 |            |                 |     |
| Severity    | Information                |            |                 |     |
| Description | NAEscripthasbeenvalidated. |            |                 |     |
EventID:5502
| Message     | Error found            | in NAE | Script <name>. |     |
| ----------- | ---------------------- | ------ | -------------- | --- |
| Category    | NAEScripts             |        |                |     |
| Severity    | Error                  |        |                |     |
| Description | ErrorfoundinNAEScript. |        |                |     |
EventID:5503
| Message     | Error found           | in NAE | Agent <name>. |     |
| ----------- | --------------------- | ------ | ------------- | --- |
| Category    | NAEScripts            |        |               |     |
| Severity    | Error                 |        |               |     |
| Description | ErrorfoundinNAEAgent. |        |               |     |
EventID:5504
Message Error executing NAE action <action_type> belonging to condition
|             | <condition>     | and agent | <agent> due | to <description>. |
| ----------- | --------------- | --------- | ----------- | ----------------- |
| Category    | NAEScripts      |           |             |                   |
| Severity    | Error           |           |             |                   |
| Description | NAEActionerror. |           |             |                   |
EventID:5505
183
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | NAE Script                          | <name> | has been created | by the system. |
| ----------- | ----------------------------------- | ------ | ---------------- | -------------- |
| Category    | NAEScripts                          |        |                  |                |
| Severity    | Information                         |        |                  |                |
| Description | NAEScripthasbeencreatedbythesystem. |        |                  |                |
EventID:5506
| Message     | NAE Agent                          | <name> has | been created | by the system. |
| ----------- | ---------------------------------- | ---------- | ------------ | -------------- |
| Category    | NAEScripts                         |            |              |                |
| Severity    | Information                        |            |              |                |
| Description | NAEAgenthasbeencreatedbythesystem. |            |              |                |
EventID:5507
| Message     | <msg>                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | NAEScripts                                  |     |     |     |
| Severity    | Information                                 |     |     |     |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |     |     |     |
EventID:5508
| Message     | <msg>                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | NAEScripts                                  |     |     |     |
| Severity    | Information                                 |     |     |     |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |     |     |     |
EventID:5509(Severity:Critical)
| Message     | <msg>                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | NAEScripts                                  |     |     |     |
| Severity    | Critical                                    |     |     |     |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |     |     |     |
EventID:5510
| Message | <msg> |     |     |     |
| ------- | ----- | --- | --- | --- |
NAEScriptsevents|184

Category

NAE Scripts

Severity

Error

Description

Log event when instantiated from active NAE agent.

Event ID: 5511 (Severity: Warning)

Message

<msg>

Category

NAE Scripts

Severity

Warning

Description

Log event when instantiated from active NAE agent.

Event ID: 5512 (Severity: Emergency)

Message

<msg>

Category

NAE Scripts

Severity

Emergency

Description

Log event when instantiated from active NAE agent.

Event ID: 5513 (Severity: Emergency)

Message

<msg>

Category

NAE Scripts

Severity

Emergency

Description

Log event when instantiated from active NAE agent.

Event ID: 5514

Message

<msg>

Category

NAE Scripts

Severity

Debug

Description

Log event when instantiated from active NAE agent.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

185

Chapter 76
ND snooping events
| ND snooping events |     |     |     |
| ------------------ | --- | --- | --- |
ThefollowingaretheeventsrelatedtoNDsnooping.
EventID:8401
| Message     | All the dynamic                                 | binding entries | were cleared. |
| ----------- | ----------------------------------------------- | --------------- | ------------- |
| Category    | NDsnooping                                      |                 |               |
| Severity    | Information                                     |                 |               |
| Description | Logeventwhenalldynamicbindingentriesarecleared. |                 |               |
EventID:8402
Message Dynamic binding entries on the port <port> were cleared.
| Category | NDsnooping  |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhenalldynamicbindingentriesonaportarecleared.
EventID:8403
Message Dynamic binding entries on the VLAN <vid> were cleared.
| Category | NDsnooping  |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhenalldynamicbindingentriesonavlanarecleared.
EventID:8404
Message Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.
| Category | NDsnooping  |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhenaspecificdynamicbindingentryonavlaniscleared.
EventID:8405
186
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

ND packet of type=<type> received on port:<port> vlan:<vlan> with src_
mac:<src_mac> is <status>. count=<count>

Category

ND snooping

Severity

Information

Description

Log event when ND packet received on port.

ND snooping events | 187

Chapter 77
NDM events
NDM events
ThefollowingaretheeventsrelatedtoNDM.
EventID:6101
Message Static Neighbor <ip> created on Port <port>, VRF <vrf> mac <mac>
| Category    | NDM                   |     |     |     |
| ----------- | --------------------- | --- | --- | --- |
| Severity    | Information           |     |     |     |
| Description | Staticneighborcreated |     |     |     |
EventID:6102
Message Static Neighbor <ip> deleted on Port <port>, VRF <vrf> and mac <mac>
| Category    | NDM                   |     |     |     |
| ----------- | --------------------- | --- | --- | --- |
| Severity    | Information           |     |     |     |
| Description | Staticneighbordeleted |     |     |     |
EventID:6103
Message Static Neighbor <ip> modified on Port <port> and VRF <vrf> from mac
|             | <old_mac>              | to new mac | <new_mac> |     |
| ----------- | ---------------------- | ---------- | --------- | --- |
| Category    | NDM                    |            |           |     |
| Severity    | Information            |            |           |     |
| Description | Staticneighbormodified |            |           |     |
EventID:6104
| Message     | IPDB neighbor                       | <ip> | added in port <port>, | VRF <vrf> |
| ----------- | ----------------------------------- | ---- | --------------------- | --------- |
| Category    | NDM                                 |      |                       |           |
| Severity    | Information                         |      |                       |           |
| Description | IPDBneighboraddedtotheneighborTable |      |                       |           |
EventID:6105
188
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | IPDB Neighbor                           | <ip> | Deleted |     |
| ----------- | --------------------------------------- | ---- | ------- | --- |
| Category    | NDM                                     |      |         |     |
| Severity    | Information                             |      |         |     |
| Description | IPDBneighbordeletedfromtheneighborTable |      |         |     |
EventID:6106
Message Clear all Arp entries requested on Port <port> and VRF <vrf>
| Category    | NDM                                       |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Information                               |     |     |     |
| Description | ClearallarpentriesrequestedonSpecificPort |     |     |     |
EventID:6107
Message Clear all VSX Peer ARP entries requested on Port <port> and vrf <vrf>
| Category    | NDM                                              |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | Information                                      |     |     |     |
| Description | ClearallVSXPeerARPentriesrequestedonSpecificPort |     |     |     |
EventID:6108
| Message     | Clear all                                | Arp entries | requested | on VRF <vrf> |
| ----------- | ---------------------------------------- | ----------- | --------- | ------------ |
| Category    | NDM                                      |             |           |              |
| Severity    | Information                              |             |           |              |
| Description | ClearallarpentriesrequestedonSpecificVRF |             |           |              |
EventID:6109
Message Clear all VSX Peer Arp entries requested on VRF <vrf>
| Category    | NDM                                             |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |
| Description | ClearallVSXPeerarpentriesrequestedonSpecificVRF |     |     |     |
EventID:6110
| Message | Clear all | Arp entries | requested |     |
| ------- | --------- | ----------- | --------- | --- |
NDMevents|189

| Category    | NDM                         |     |     |
| ----------- | --------------------------- | --- | --- |
| Severity    | Information                 |     |     |
| Description | Clearallarpentriesrequested |     |     |
EventID:6111
| Message     | Clear all                          | VSX Peer Arp | entries requested |
| ----------- | ---------------------------------- | ------------ | ----------------- |
| Category    | NDM                                |              |                   |
| Severity    | Information                        |              |                   |
| Description | ClearallVSXPeerarpentriesrequested |              |                   |
EventID:6112
Message EVPN Virtual Tunnel EndPoint Neighbor <ip> added to Port<port> on VRF
<vrf>
| Category | NDM         |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description EVPNVirtualTunnelEndPointNeighboraddedtotheneighbortable
EventID:6113
Message EVPN Virtual Tunnel EndPoint Neighbor <ip> updated on Port<port> and
|          | VRF <vrf>   | with mac <mac> |     |
| -------- | ----------- | -------------- | --- |
| Category | NDM         |                |     |
| Severity | Information |                |     |
Description EVPNVirtualTunnelEndPointNeighborUpdatedintheneighbortable
EventID:6114
Message EVPN VTEP Neighbor <ip> deleted from Port<port> and VRF <vrf>
| Category    | NDM                                         |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Severity    | Information                                 |     |     |
| Description | EVPNVTEPNeighbordeletedfromtheneighbortable |     |     |
EventID:6115
| Message | Management | Role set | to <role> |
| ------- | ---------- | -------- | --------- |
190
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Category

NDM

Severity

Information

Description

Processing Redundancy management

Event ID: 6116

Message

Management role changed from old <role1> to new role <role2>

Category

NDM

Severity

Information

Description

Management role changed to new role

Event ID: 6117

Message

IPv4 neighbor ageout time changed to <time> seconds on port <port>

Category

NDM

Severity

Information

Description

IPv4 neighbor ageout time changed to new value

Event ID: 6118

Message

IPv6 neighbor ageout time changed to <time> seconds on port <port>

Category

NDM

Severity

Information

Description

IPv6 neighbor ageout time changed to new value

Event ID: 6119

Message

VSX neighbor datapath init sync status is neighbor sync completed

Category

NDM

Severity

Information

Description

VSX neighbor datapath init sync status is neighbor sync completed

Event ID: 6120

Message

VSX neighbor datapath init sync status is neighbor sync in progress

Category

NDM

NDM events | 191

| Severity | Information |     |     |     |
| -------- | ----------- | --- | --- | --- |
Description VSXneighbordatapathinitsyncstatusisneighborsyncinprogress
EventID:6121
| Message     | static neighbor                          | <ip> add | failed, Subnet | match failed |
| ----------- | ---------------------------------------- | -------- | -------------- | ------------ |
| Category    | NDM                                      |          |                |              |
| Severity    | Error                                    |          |                |              |
| Description | StaticNeighboraddfailed,subnetnotmatched |          |                |              |
EventID:6122
| Message     | static neighbor                   | <ip> add | failed, it | is own ip |
| ----------- | --------------------------------- | -------- | ---------- | --------- |
| Category    | NDM                               |          |            |           |
| Severity    | Error                             |          |            |           |
| Description | StaticNeighboraddfailed,itisownip |          |            |           |
EventID:6123
Message static neighbor <ip> Subnet match add failed, port is down
| Category    | NDM                                |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Error                              |     |     |     |
| Description | StaticNeighboraddfailed,portisdown |     |     |     |
EventID:6124
| Message     | Neighbor table                             | VSX peer | DB connection | terminated |
| ----------- | ------------------------------------------ | -------- | ------------- | ---------- |
| Category    | NDM                                        |          |               |            |
| Severity    | Information                                |          |               |            |
| Description | NeighbortableVSXpeerDBconnectionterminated |          |               |            |
EventID:6125
| Message     | Neighbor table                              | VSX peer | DB connection | established |
| ----------- | ------------------------------------------- | -------- | ------------- | ----------- |
| Category    | NDM                                         |          |               |             |
| Severity    | Information                                 |          |               |             |
| Description | NeighbortableVSXpeerDBconnectionestablished |          |               |             |
192
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

EventID:6126
| Message     | VSX Peer                           | IP <ip> added | the port <port> | and VRF <vrf> |
| ----------- | ---------------------------------- | ------------- | --------------- | ------------- |
| Category    | NDM                                |               |                 |               |
| Severity    | Information                        |               |                 |               |
| Description | VSXPeerIPaddedinportvsxPeerIpCache |               |                 |               |
EventID:6127
Message VSX Peer IP <ip> deleted from the port <port> and VRF <vrf>
| Category    | NDM                                  |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | VSXPeerIPdeletedinportvsxPeerIpCache |     |     |     |
EventID:6128
| Message     | Proxy arp                           | enabled for | the port <port> |     |
| ----------- | ----------------------------------- | ----------- | --------------- | --- |
| Category    | NDM                                 |             |                 |     |
| Severity    | Information                         |             |                 |     |
| Description | Proxyarpenabledforthegiveninterface |             |                 |     |
EventID:6129
| Message     | Proxy arp                           | disabled | for the port <port> |     |
| ----------- | ----------------------------------- | -------- | ------------------- | --- |
| Category    | NDM                                 |          |                     |     |
| Severity    | Information                         |          |                     |     |
| Description | Proxyarpdiabledforthegiveninterface |          |                     |     |
EventID:6130
Message Neighbor <ip> modified on Port <port> and VRF <vrf> from mac <old_mac>
|             | to new           | mac <new_mac> |     |     |
| ----------- | ---------------- | ------------- | --- | --- |
| Category    | NDM              |               |     |     |
| Severity    | Information      |               |     |     |
| Description | Neighbormodified |               |     |     |
EventID:6131
NDMevents|193

| Message     | Neighbor                       | Discovery daemon started |     |
| ----------- | ------------------------------ | ------------------------ | --- |
| Category    | NDM                            |                          |     |
| Severity    | Information                    |                          |     |
| Description | NeighborDiscoverydaemonstarted |                          |     |
EventID:6132
Message Duplicate IPv4 address <ip> is detected on port <port> with a MAC
|             | address                         | of <mac>' throttle_count: | 40  |
| ----------- | ------------------------------- | ------------------------- | --- |
| Category    | NDM                             |                           |     |
| Severity    | Error                           |                           |     |
| Description | DuplicateIPdetectedfromARPreply |                           |     |
EventID:6133
Message Duplicate IPv6 address <ip> is detected on port <port> with a MAC
|          | address | of <mac> |     |
| -------- | ------- | -------- | --- |
| Category | NDM     |          |     |
| Severity | Error   |          |     |
Description DuplicateIPv6addressdetectedfromNeighbouradvertisement
EventID:6134
Message Duplicate IPv4 address <ip> is detected on port <port> with a MAC
|             | address                           | of <mac>' throttle_count: | 40  |
| ----------- | --------------------------------- | ------------------------- | --- |
| Category    | NDM                               |                           |     |
| Severity    | Error                             |                           |     |
| Description | DuplicateIPdetectedfromARPrequest |                           |     |
194
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Chapter 78
NTP events
NTP events
ThefollowingaretheeventsrelatedtoNTP.
EventID:1101
| Message     | NTP Association                        | <event>: | <server> <server_info> |
| ----------- | -------------------------------------- | -------- | ---------------------- |
| Category    | NTP                                    |          |                        |
| Severity    | Information                            |          |                        |
| Description | LogsNTPAssociationconfigurationchanges |          |                        |
EventID:1102
Message NTP Trusted keys <trusted_keys> and Untrusted keys <untrusted_keys>
| Category    | NTP                                           |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Information                                   |     |     |
| Description | LogsNTPTrustedandUntrustedauthentication-keys |     |     |
EventID:1103
| Message     | NTP Authentication                | state | change: <old> -> <new> |
| ----------- | --------------------------------- | ----- | ---------------------- |
| Category    | NTP                               |       |                        |
| Severity    | Information                       |       |                        |
| Description | LogsNTPAuthenticationstatechanges |       |                        |
EventID:1104
| Message     | NTP VRF state                       | change: <old> | -> <new> |
| ----------- | ----------------------------------- | ------------- | -------- |
| Category    | NTP                                 |               |          |
| Severity    | Information                         |               |          |
| Description | LogsNTPVRFconfigurationstatechanges |               |          |
EventID:1105
195
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message NTP primary server connection established to <server>
| Category | NTP         |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogsNTPprimaryserverconnectionestablishedstatechange
EventID:1106
| Message     | NTP primary                                   | server connection | lost to <server> |
| ----------- | --------------------------------------------- | ----------------- | ---------------- |
| Category    | NTP                                           |                   |                  |
| Severity    | Information                                   |                   |                  |
| Description | LogsNTPprimaryserverconnectionloststatechange |                   |                  |
EventID:1107
| Message     | NTP enable                                     | state change: | <old> -> <new> |
| ----------- | ---------------------------------------------- | ------------- | -------------- |
| Category    | NTP                                            |               |                |
| Severity    | Information                                    |               |                |
| Description | EventraisedwhenNTPischangedtoenabledordisabled |               |                |
NTPevents|196

Chapter 79
OSPFv2 events
OSPFv2 events
ThefollowingaretheeventsrelatedtoOSPFv2.
EventID:2401
Message AdjChg: Nbr <router-id> on <ospf-interface>(<area>): <old_state> ->
<new_state>
| Category    | OSPFv2                                       |     |     |
| ----------- | -------------------------------------------- | --- | --- |
| Severity    | Information                                  |     |     |
| Description | LogsthechangesinOSPFv2neighbourstatemachine. |     |     |
EventID:2402
Message Interface <interface>(<area>) changed from <old_state> to <new_state>,
input: <input>
| Category    | OSPFv2                                |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Information                           |     |     |
| Description | LogsthechangesintheinterfaceFSMstate. |     |     |
EventID:2403
| Message     | <event> with                 | <destination> | <nexthops> |
| ----------- | ---------------------------- | ------------- | ---------- |
| Category    | OSPFv2                       |               |            |
| Severity    | Information                  |               |            |
| Description | LogsOSPFv2routeaddanddelete. |               |            |
EventID:2404
Message AdjChg: Nbr <router-id> on <ospf-interface>: <state> -> <next_state>
(<event>)
| Category    | OSPFv2                                       |     |     |
| ----------- | -------------------------------------------- | --- | --- |
| Severity    | Information                                  |     |     |
| Description | LogsthechangesinOSPFv2neighbourstatemachine. |     |     |
EventID:2405
197
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Router-id                     | updated from | <old> to <new> |
| ----------- | ----------------------------- | ------------ | -------------- |
| Category    | OSPFv2                        |              |                |
| Severity    | Information                   |              |                |
| Description | Logsthechangesintherouter-id. |              |                |
EventID:2406
| Message     | Failed                                      | to <action> <rule> | error: <err> |
| ----------- | ------------------------------------------- | ------------------ | ------------ |
| Category    | OSPFv2                                      |                    |              |
| Severity    | Error                                       |                    |              |
| Description | LogserrorsforOSPFv2FPcreation/installation. |                    |              |
EventID:2407
Message OSPF all routers field entry added: group_id=<group_id> fp_id=<fp_id>
stat_id=<stats_id>
| Category    | OSPFv2                                |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Information                           |     |     |
| Description | LogsforOSPFv2FPcreation/installation. |     |     |
EventID:2408
Message OSPF designated routers field entry added: group_id=<group_id> fp_
|             | id=<fp_id>                              | stat_id=<stats_id> |     |
| ----------- | --------------------------------------- | ------------------ | --- |
| Category    | OSPFv2                                  |                    |     |
| Severity    | Information                             |                    |     |
| Description | LogsforOSPFv2DRFPcreation/installation. |                    |     |
EventID:2409
Message Graceful Restart state changed, <old_state> -> <new_state>, reason:
<reason>
| Category    | OSPFv2                                      |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Severity    | Information                                 |     |     |
| Description | LogsthechangesofOSPFv2GracefulRestartstate. |     |     |
EventID:2410
OSPFv2events|198

Message

Duplicate router-id for <ospf-interface> from source <source-ip>

Category

Severity

OSPFv2

Error

Description

Logs when router-id is duplicate.

Event ID: 2411

Message

Distance External <external>, Inter-area <inter>, and Intra-area
<intra> applied to all the OSPF processes in <vrf> VRF

Category

OSPFv2

Severity

Information

Description

Logs the changes of OSPFv2 distance.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

199

Chapter 80
OSPFv3 events
OSPFv3 events
ThefollowingaretheeventsrelatedtoOSPFv3.
EventID:4901
| Message     | Failed                                      | to <action> | <rule> error: <err> |
| ----------- | ------------------------------------------- | ----------- | ------------------- |
| Category    | OSPFv3                                      |             |                     |
| Severity    | Error                                       |             |                     |
| Description | LogserrorsforOSPFv3FPcreation/installation. |             |                     |
EventID:4902
Message OSPF3 all routers field entry added: group_id=<group_id> fp_id=<fp_id>
stat_id=<stats_id>
| Category    | OSPFv3                                |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Information                           |     |     |
| Description | LogsforOSPFv3FPcreation/installation. |     |     |
EventID:4903
Message OSPF3 designated routers field entry added: group_id=<group_id> fp_
|             | id=<fp_id>                              | stat_id=<stats_id> |     |
| ----------- | --------------------------------------- | ------------------ | --- |
| Category    | OSPFv3                                  |                    |     |
| Severity    | Information                             |                    |     |
| Description | LogsforOSPFv3DRFPcreation/installation. |                    |     |
EventID:4904
Message AdjChg: Nbr<router-id> on interface <link-local> on <interface>
|             | (<area>):                                    | <old_state> | -> <new_state> |
| ----------- | -------------------------------------------- | ----------- | -------------- |
| Category    | OSPFv3                                       |             |                |
| Severity    | Information                                  |             |                |
| Description | LogsthechangesinOSPFv3neighbourstatemachine. |             |                |
EventID:4905
200
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

Interface <link-local> on <interface>(<area>) changed from <old_state>
to <new_state>, input: <input>

Category

OSPFv3

Severity

Information

Description

Logs the changes in the interface FSM state.

Event ID: 4906

Message

Graceful Restart state changed, <old_state> -> <new_state>, reason:
<reason>

Category

OSPFv3

Severity

Information

Description

Logs the changes of OSPFv3 Graceful Restart state.

Event ID: 4907

Message

Duplicate router-id for <link-local> from source <source-ip>

Category

Severity

OSPFv3

Error

Description

Logs when router-id is duplicate.

Event ID: 4908

Message

Distance External <external>, Inter-area <inter>, and Intra-area
<intra> applied to all the OSPFv3 processes in <vrf> VRF

Category

OSPFv3

Severity

Information

Description

Logs the changes of OSPFv3 distance.

OSPFv3 events | 201

|                |        |     |     |          | Chapter | 81     |
| -------------- | ------ | --- | --- | -------- | ------- | ------ |
|                |        |     |     | Password | Reset   | events |
| Password Reset | events |     |     |          |         |        |
Thefollowingaretheeventsrelatedtopasswordreset.
EventID:5901
| Message     | Password reset                                   | succeeded | for admin | user. |     |     |
| ----------- | ------------------------------------------------ | --------- | --------- | ----- | --- | --- |
| Category    | PasswordReset                                    |           |           |       |     |     |
| Severity    | Information                                      |           |           |       |     |     |
| Description | Logmessagewhenadminuserpasswordresetissuccessful |           |           |       |     |     |
EventID:5902
| Message     | Password reset                            | failed | for admin | user. |     |     |
| ----------- | ----------------------------------------- | ------ | --------- | ----- | --- | --- |
| Category    | PasswordReset                             |        |           |       |     |     |
| Severity    | Information                               |        |           |       |     |     |
| Description | Logmessagewhenadminuserpasswordresetfails |        |           |       |     |     |
202
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 82

PIM events

PIM events

The following are the events related to PIM.

Event ID: 5101

Message

Category

Severity

Failed to send <pkt_type> packet on Interface <InterfaceName>'
throttle_count: 100

PIM

Error

Description

Send error packet

Event ID: 5102

Message

PIM interface <InterfaceName> is configured with IP <ip_address>

Category

PIM

Severity

Information

Description

Pim IP config

Event ID: 5103

Message

Category

Severity

Packet dropped from <ip_address> on interface <InterfaceName> <error>
<value>' throttle_count: 100

PIM

Error

Description

Packet dropped

Event ID: 5104

Message

Category

Severity

Received packet from router <ip_address>, unkwn pkt type <pkt_type>'
throttle_count: 100

PIM

Error

Description

Received packet from router

Event ID: 5105

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

203

| Message | Failed | to add flow | <dip0>.<dip1>.<dip2>.<dip3>, |     |     |
| ------- | ------ | ----------- | ---------------------------- | --- | --- |
<sip0>.<sip1>.<sip2>.<sip3> (<status> <srcport> <srcvid> <totalvid>
|             | <flowtype>      | <callerid>) |     |     |     |
| ----------- | --------------- | ----------- | --- | --- | --- |
| Category    | PIM             |             |     |     |     |
| Severity    | Error           |             |     |     |     |
| Description | Failedtoaddflow |             |     |     |     |
EventID:5106
Message Failed to remove flow g <dip0>.<dip1>.<dip2>.<dip3>, s <sip0>,
|     | <sip1>.<sip2>.<sip3> |     | (<status> | <srcport> | <srcvid> <flowtype> |
| --- | -------------------- | --- | --------- | --------- | ------------------- |
<callerid>)
| Category    | PIM                           |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | --- |
| Severity    | Error                         |     |     |     |     |
| Description | FailedtoremoveflowforHardware |     |     |     |     |
EventID:5107(Severity:Warning)
Message Failed to add a mroute for s=<source>, g=<group> on interface
<interfaceName> as the configured mroute limits are reached' throttle_
count: 100
| Category    | PIM                                        |     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- |
| Severity    | Warning                                    |     |     |     |     |
| Description | Failedtoprogrammrouteasthelimitsarereached |     |     |     |     |
EventID:5108(Severity:Warning)
Message Failed to add a mroute for s=<source>, g=<group> on interface
<interfaceName> as the configured sources per group limit is reached'
|          | throttle_count: | 100 |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Category | PIM             |     |     |     |     |
| Severity | Warning         |     |     |     |     |
Description Failedtoprogrammrouteasthesourcespergrouplimitisreached
EventID:5109
Message This router is elected as the <ip_version> <state> for interface
<ifname>
| Category | PIM |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
PIMevents|204

| Severity    | Information      |     |     |
| ----------- | ---------------- | --- | --- |
| Description | PIMDRelectionlog |     |     |
EventID:5110
Message <type> <reason> failed with Fd: <fd> on Port: <port>. Error
|             | description:                 | <err> |     |
| ----------- | ---------------------------- | ----- | --- |
| Category    | PIM                          |       |     |
| Severity    | Error                        |       |     |
| Description | Multicastsocketcreationerror |       |     |
EventID:5111
Message OVSDB operation failed with <err>' throttle_count: 100
| Category    | PIM               |     |     |
| ----------- | ----------------- | --- | --- |
| Severity    | Error             |     |     |
| Description | DBOperationfailed |     |     |
EventID:5112
Message New Elected BSR for VRF <vrf_name> is <ebsr_ip> with priority
<priority>
| Category    | PIM         |     |     |
| ----------- | ----------- | --- | --- |
| Severity    | Information |     |     |
| Description | ElectedBSR  |     |     |
EventID:5113
| Message     | Elected BSR       | removed | on VRF <vrf_name> |
| ----------- | ----------------- | ------- | ----------------- |
| Category    | PIM               |         |                   |
| Severity    | Information       |         |                   |
| Description | ElectedBSRremoved |         |                   |
EventID:5114
Message Candidate BSR <ip_address> with priority <priority> is <status> on
|     | interface | <ifname> |     |
| --- | --------- | -------- | --- |
205
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Category    | PIM                    |     |     |
| ----------- | ---------------------- | --- | --- |
| Severity    | Information            |     |     |
| Description | ConfiguredcandidateBSR |     |     |
EventID:5115
Message PIM Neighbor <neighbor_ip> is <event> on interface <ifname>
| Category    | PIM            |     |     |
| ----------- | -------------- | --- | --- |
| Severity    | Information    |     |     |
| Description | Neighborstatus |     |     |
EventID:5116(Severity:Warning)
Message <pkt> packet is discarded on interface <ifname>. Reason: <reason>'
|             | throttle_count: 100 |     |     |
| ----------- | ------------------- | --- | --- |
| Category    | PIM                 |     |     |
| Severity    | Warning             |     |     |
| Description | Packetdrop          |     |     |
EventID:5117
Message Forwarding state has changed to <state> on <ip_version> enabled
interface <ifname>
| Category    | PIM                        |     |     |
| ----------- | -------------------------- | --- | --- |
| Severity    | Information                |     |     |
| Description | Interfaceoperationalstatus |     |     |
EventID:5118
Message <pim_version> <mode> mode is <status> on interface <ifname>
| Category    | PIM              |     |     |
| ----------- | ---------------- | --- | --- |
| Severity    | Information      |     |     |
| Description | InterfacePIMmode |     |     |
EventID:5119
| Message | Router <pim_version> | is <mode> | on VRF <vrfname> |
| ------- | -------------------- | --------- | ---------------- |
PIMevents|206

| Category    | PIM                          |     |     |
| ----------- | ---------------------------- | --- | --- |
| Severity    | Information                  |     |     |
| Description | Routerpimconfigurationstatus |     |     |
EventID:5120
Message Candidate RP <ip_address> is <event> on VRF <vrf_name>
| Category    | PIM                        |     |     |
| ----------- | -------------------------- | --- | --- |
| Severity    | Information                |     |     |
| Description | LearntorremovedcandidateRP |     |     |
EventID:5121
Message Software Packet Queue <limit> threshold value <val> reached. Queue
size: <qsize>
| Category    | PIM                                 |     |     |
| ----------- | ----------------------------------- | --- | --- |
| Severity    | Information                         |     |     |
| Description | SoftwarePacketQueuereachesthreshold |     |     |
EventID:5122
Message This router is elected as the <ip_version> VSX <state> for interface
<ifname>
| Category    | PIM                 |     |     |
| ----------- | ------------------- | --- | --- |
| Severity    | Information         |     |     |
| Description | PIMVSXDRElectionlog |     |     |
EventID:5123
| Message     | VSX ISL Status        | changed | to <isl_status> |
| ----------- | --------------------- | ------- | --------------- |
| Category    | PIM                   |         |                 |
| Severity    | Information           |         |                 |
| Description | VSXISLStatusupdatelog |         |                 |
EventID:5124
Message Candidate RP <ip_address> is configured on interface <ifname>
207
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Category

PIM

Severity

Information

Description

Configured candidate RP

Event ID: 5125

Message

BFD Session created for neighbor <ip_address> on interface <ifname>

Category

PIM

Severity

Information

Description

BFD Session created

Event ID: 5126

Message

BFD Session deleted for neighbor <ip_address> on interface <ifname>

Category

PIM

Severity

Information

Description

BFD Session deleted

Event ID: 5127

Message

PIM Resource utilization of <capacity_type> has reached/exceeded the
supported limits on the system.

Category

PIM

Severity

Information

Description

This log event informs the user that PIM resource utilization has exceeded the supported
limits

Event ID: 5128

Message

PIM Resource utilization of <capacity_type> has reached 90 percent of
the supported limits on the system.

Category

PIM

Severity

Information

Description

This log event informs the user that PIM resource utilization has reached 90 percent of
the supported limits

Event ID: 5129

PIM events | 208

Message

PIM Resource utilization of <capacity_type> has dropped below 90
percent of the supported limits on the system.

Category

PIM

Severity

Information

Description

This log event informs the user that PIM resource utilization drops below 90 percent of
the supported limits

Event ID: 5130

Message

Router <pim_version> PIM-SSM is <mode> on VRF <vrfname>

Category

PIM

Severity

Information

Description

Router PIM-SSM configuration status

Event ID: 5131

Message

Router <pim_version> PIM-SSM range ACL is <mode> on VRF <vrfname>

Category

PIM

Severity

Information

Description

Router PIM-SSM range ACL configuration status

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

209

Chapter 83

Policies events

Policies events

The following are the events related to policies.

Event ID: 10101

Message

Policy <policy_name> failed to apply on <application>

Category

Severity

Policies

Error

Description

Policy application failure

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

210

Chapter 84
Port access events
| Port access events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
Thefollowingaretheeventsrelatedtoportaccess.
EventID:10501
Message Client <mac_address> was logged-off administratively through command-
line interface
| Category | Portaccess  |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Clientwaslogged-offadministrativelythroughcommand-lineinterface
EventID:10502
| Message     | Port <port>                         | is blocked | by port-access |     |
| ----------- | ----------------------------------- | ---------- | -------------- | --- |
| Category    | Portaccess                          |            |                |     |
| Severity    | Information                         |            |                |     |
| Description | Theportisblockedbyport-accessdaemon |            |                |     |
EventID:10503
| Message     | Port <port>                           | is unblocked | by port-access |     |
| ----------- | ------------------------------------- | ------------ | -------------- | --- |
| Category    | Portaccess                            |              |                |     |
| Severity    | Information                           |              |                |     |
| Description | Theportisunblockedbyport-accessdaemon |              |                |     |
EventID:10504
Message Clients were logged-off on the port <port> due to a change in
|          | authentication | mode | from <old_mode> | to <new_mode> |
| -------- | -------------- | ---- | --------------- | ------------- |
| Category | Portaccess     |      |                 |               |
| Severity | Information    |      |                 |               |
Description Theauthenticationmodeassociatedwiththeportischanged
EventID:10505
211
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message Clients were logged-off on the port <port> due to a change in client
|             | limit from                                   | <old_limit> | to <new_limit> |     |
| ----------- | -------------------------------------------- | ----------- | -------------- | --- |
| Category    | Portaccess                                   |             |                |     |
| Severity    | Information                                  |             |                |     |
| Description | Theclientlimitassociatedwiththeportischanged |             |                |     |
EventID:10506
Message The name associated with VLAN <vlan_id> changed from <old_name> to
<new_name>
| Category | Portaccess  |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThenameassociatedwithaVLANinusebyport-accessdaemonchanged
EventID:10507
Message Clients using policy <policy_name> were logged-off due to a
|             | configuration                            | change | in the policy |     |
| ----------- | ---------------------------------------- | ------ | ------------- | --- |
| Category    | Portaccess                               |        |               |     |
| Severity    | Information                              |        |               |     |
| Description | Thepolicyconfigurationisupdatedbytheuser |        |               |     |
EventID:10508
| Message  | VLAN conflict | detected | on port <port> |     |
| -------- | ------------- | -------- | -------------- | --- |
| Category | Portaccess    |          |                |     |
| Severity | Error         |          |                |     |
Description VLANisconfiguredasTrunkforsomeclientsandaccessforothers.Thiscouldpotentially
resultintrafficloss
EventID:10509
Message Client limit exceeded on port <port>, caused by an unauthenticated
|             | client <mac_addr>'                        | throttle_count: |     | 30: yes |
| ----------- | ----------------------------------------- | --------------- | --- | ------- |
| Category    | Portaccess                                |                 |     |         |
| Severity    | Information                               |                 |     |         |
| Description | Logeventwhenanintruderisdetectedontheport |                 |     |         |
EventID:10510
Portaccessevents|212

Message

All clients except client with MAC address <mac_addr> logged-off on the
port <port> due to a change in authentication mode from <old_mode> to
<new_mode>

Category

Port access

Severity

Information

Description

The authentication mode associated with the port is changed

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

213

|             |             |               |       |       | Chapter | 85     |
| ----------- | ----------- | ------------- | ----- | ----- | ------- | ------ |
|             |             | Port access   | group | based | policy  | events |
| Port access | group based | policy events |       |       |         |        |
Thefollowingaretheeventsrelatedtoportaccessgroupbasedpolicy.
EventID:12601
Message Configuration change in the policy <pac_gbp_name> <operation>
| Category | Portaccessgroupbasedpolicy |     |     |     |     |     |
| -------- | -------------------------- | --- | --- | --- | --- | --- |
| Severity | Information                |     |     |     |     |     |
Description Thegroupbasedpolicyconfigurationisupdatedbytheuser
EventID:12602
Message Configuration update in the policy due to class change <pac_gbp_name>
<operation>
| Category | Portaccessgroupbasedpolicy |     |     |     |     |     |
| -------- | -------------------------- | --- | --- | --- | --- | --- |
| Severity | Information                |     |     |     |     |     |
Description Thegroupbasedpolicyclassconfigurationisupdatedbytheuser
EventID:12603
Message Trigger received to <operation> policy: <pac_gbp_name> for client:
<client>
| Category    | Portaccessgroupbasedpolicy                      |     |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |     |     |
| Description | Thegroupbasedpolicyapplying/unapplyingforclient |     |     |     |     |     |
EventID:12604
Message Trigger received to <operation> policy: <pac_gbp_name> for client:
|             | <client>                                        | is <result> |     |     |     |     |
| ----------- | ----------------------------------------------- | ----------- | --- | --- | --- | --- |
| Category    | Portaccessgroupbasedpolicy                      |             |     |     |     |     |
| Severity    | Information                                     |             |     |     |     |     |
| Description | Thegroupbasedpolicyapply/unapplyforclientresult |             |     |     |     |     |
EventID:12605
214
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

Message

Trigger received on <operation> of line_card: <line_card> to <action>
policy: <pac_gbp_name>

Category

Port access group based policy

Severity

Information

Description

The group based policy apply/unapply on new linecard

Event ID: 12606

Message

Trigger received on <operation> of line_card: <line_card> to <action>
policy: <pac_gbp_name> is <result>

Category

Port access group based policy

Severity

Information

Description

The group based policy apply/unapply on new linecard result

Port access group based policy events | 215

Chapter 86

Port access roles events

Port access roles events

The following are the events related to port access roles.

Event ID: 9301

Message

Failed to apply ClearPass role - <cprole_error_string>

Category

Port access roles

Severity

Error

Description

Logs an event if there are errors when applying a ClearPass role

Event ID: 9302

Message

Failed to create the role - <role_name>, maximum limit reached'
throttle_count: 100

Category

Port access roles

Severity

Error

Description

Logs an event if the maximum limit is reached while creating a Port Access Role

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

216

Chapter 87
Port events
Port events
Thefollowingaretheeventsrelatedtoport.
EventID:601
| Message     | Netlink socket                     | creation | failed <error> |
| ----------- | ---------------------------------- | -------- | -------------- |
| Category    | Port                               |          |                |
| Severity    | Information                        |          |                |
| Description | Logwhennetlinksocketcreationfailed |          |                |
EventID:602
| Message     | Netlink socket                 | bind failed | <error> |
| ----------- | ------------------------------ | ----------- | ------- |
| Category    | Port                           |             |         |
| Severity    | Information                    |             |         |
| Description | Logwhennetlinksocketbindfailed |             |         |
EventID:603
Message Netlink failed to set mtu <mtu> for interface <interface>
| Category    | Port                                     |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | Logwhennetlinkfailedtosetmtuforinterface |     |     |
EventID:604
Message Netlink failed to bring <status> the interface <interface>
| Category    | Port                                           |     |     |
| ----------- | ---------------------------------------------- | --- | --- |
| Severity    | Information                                    |     |     |
| Description | Logwhennetlinkfailedtochangetheinterfacestatus |     |     |
EventID:605
217
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Unknown internal          | vlan policy | <policy> |
| ----------- | ------------------------- | ----------- | -------- |
| Category    | Port                      |             |          |
| Severity    | Information               |             |          |
| Description | Unknowninternalvlanpolicy |             |          |
EventID:606
| Message     | Error allocating                              | internal | vlan for port <vlan> |
| ----------- | --------------------------------------------- | -------- | -------------------- |
| Category    | Port                                          |          |                      |
| Severity    | Information                                   |          |                      |
| Description | Logwhenallocationfailedforinternalvlanforport |          |                      |
EventID:607
| Message     | Overlapping                               | networks observed | for <ip_address> |
| ----------- | ----------------------------------------- | ----------------- | ---------------- |
| Category    | Port                                      |                   |                  |
| Severity    | Error                                     |                   |                  |
| Description | Logwhenaduplicateaddressisreceivedonaport |                   |                  |
Portevents|218

Chapter 88

Port security events

Port security events

The following are the events related to port security.

Event ID: 9401

Message

Client limit exceeded on port <if_name>, caused by an unauthorized
client <mac_addr>' throttle_count: 30: yes

Category

Port security

Severity

Information

Description

Log event when an intruder is detected on the port

Event ID: 9402

Message

Port security sticky client move violation triggered on port <port> for
client with MAC address <mac_addr>.' throttle_count: 30: yes

Category

Port security

Severity

Information

Description

Log event when sticky mac is moved to other port

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

219

Chapter 89

Port Statistics events

Port Statistics events

The following are the events related to port statistics.

Event ID: 6601

Message

Failed to create layer 3 IPv4 RX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv4 RX counter fails

Event ID: 6602

Message

Failed to create layer 3 IPv6 RX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv6 RX counter fails

Event ID: 6603

Message

Failed to create layer 3 IPv4 TX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv4 TX counter fails

Event ID: 6604

Message

Failed to create layer 3 IPv6 TX statistic for port:<name>

Category

Port Statistics

Severity

Error

Description

Logs a message when the creation of a Layer 3 IPv6 TX counter fails

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

220

Chapter 90
Power events
Power events
Thefollowingaretheeventsrelatedtopower.
EventID:301
| Message     | PSU <name>               | changed state | to <state> |     |
| ----------- | ------------------------ | ------------- | ---------- | --- |
| Category    | Power                    |               |            |     |
| Severity    | Information              |               |            |     |
| Description | LogthechangeinPSUstatus. |               |            |     |
EventID:302(Severity:Warning)
Message PSUs inserted in the system are of <Type> types. This is <Support>
configuration.
| Category    | Power                               |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Warning                             |     |     |     |
| Description | LogtheidentificationofmixedPSUtypes |     |     |     |
EventID:303
Message PSU <name> encountered a warning. Total warning count: <warnings>
| Category    | Power                             |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Error                             |     |     |     |
| Description | LogthewarningsencounteredbythePSU |     |     |     |
EventID:304
| Message     | PSU <name>                        | faulted. Total | fault count: | <failures> |
| ----------- | --------------------------------- | -------------- | ------------ | ---------- |
| Category    | Power                             |                |              |            |
| Severity    | Error                             |                |              |            |
| Description | LogthefailuresencounteredbythePSU |                |              |            |
EventID:305(Severity:Warning)
221
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | PSU <name>:                        | Internal | communication | <status> |     |
| ----------- | ---------------------------------- | -------- | ------------- | -------- | --- |
| Category    | Power                              |          |               |          |     |
| Severity    | Warning                            |          |               |          |     |
| Description | LogPSUinternalcommunicationfailure |          |               |          |     |
EventID:306(Severity:Warning)
| Message     | PSU <name>:    | Fan-<fanidx> | <status> |     |     |
| ----------- | -------------- | ------------ | -------- | --- | --- |
| Category    | Power          |              |          |     |     |
| Severity    | Warning        |              |          |     |     |
| Description | LogPSUfanfault |              |          |     |     |
EventID:307(Severity:Warning)
Message PSU <name>: <sensorid> sensor <status> threshold limit
| Category    | Power                                        |     |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- | --- |
| Severity    | Warning                                      |     |     |     |     |
| Description | LogwhenPSUtemperaturesensorexceededthreshold |     |     |     |     |
EventID:308
Message PSU <name> has shutdown due to over temperature in <sensorid> sensor
| Category    | Power                                           |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- |
| Severity    | Error                                           |     |     |     |     |
| Description | LogwhenPSUtemperaturesensortriggeredPSUshutdown |     |     |     |     |
EventID:309(Severity:Warning)
| Message     | PSU <name>:                             | Output current | <status> | threshold | limit |
| ----------- | --------------------------------------- | -------------- | -------- | --------- | ----- |
| Category    | Power                                   |                |          |           |       |
| Severity    | Warning                                 |                |          |           |       |
| Description | LogwhenPSUoutputcurrentexceedsthreshold |                |          |           |       |
EventID:310
| Message | PSU <name> | has shutdown | due to output | overcurrent |     |
| ------- | ---------- | ------------ | ------------- | ----------- | --- |
Powerevents|222

| Category    | Power                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Error                                       |     |     |     |
| Description | LogwhenPSUoutputcurrenttriggeredPSUshutdown |     |     |     |
EventID:311
| Message     | PSU <name>                                  | has shutdown | due to output | overvoltage |
| ----------- | ------------------------------------------- | ------------ | ------------- | ----------- |
| Category    | Power                                       |              |               |             |
| Severity    | Error                                       |              |               |             |
| Description | LogwhenPSUoutputvoltagetriggeredPSUshutdown |              |               |             |
EventID:312
| Message     | PSU Redundancy                                | set | to <redund> |     |
| ----------- | --------------------------------------------- | --- | ----------- | --- |
| Category    | Power                                         |     |             |     |
| Severity    | Information                                   |     |             |     |
| Description | LogachangeinthePSUredundancyuserconfiguration |     |             |     |
EventID:313
| Message     | PSU Redundancy                               | operating | at <redund> |     |
| ----------- | -------------------------------------------- | --------- | ----------- | --- |
| Category    | Power                                        |           |             |     |
| Severity    | Information                                  |           |             |     |
| Description | LogachangeinthePSUredundancyoperationalstate |           |             |     |
EventID:314(Severity:Warning)
Message PSU <name> disabled: PSU airflow does not match system-airflow
| Category | Power   |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description LogwhenPSUisdisabledduetoairflowdirectionmismatch
EventID:315
| Message  | PSU <name> | disabled: | PSU communication | error |
| -------- | ---------- | --------- | ----------------- | ----- |
| Category | Power      |           |                   |       |
223
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Error                                       |     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- | --- |
| Description | LogwhenPSUisdisabledduetocommunicationerror |     |     |     |     |
EventID:316(Severity:Warning)
Message <type> module <name> denied power due to insufficient power. Configured
|          | PoE power | can be deconfigured | to allow card | to be granted | power. |
| -------- | --------- | ------------------- | ------------- | ------------- | ------ |
| Category | Power     |                     |               |               |        |
| Severity | Warning   |                     |               |               |        |
Description Thereisinsufficientpowertopoweracard.PowercanberemovedfromconfiguredPoE
PDstobeabletopowerthecard.
EventID:317(Severity:Warning)
Message PSU <name> disabled: PSU inserted is not supported by the system
| Category    | Power                                     |     |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- | --- |
| Severity    | Warning                                   |     |     |     |     |
| Description | LogwhenPSUisdisabledduetoanunsupportedPSU |     |     |     |     |
EventID:318
| Message     | Power over                         | Ethernet status | has faulted |     |     |
| ----------- | ---------------------------------- | --------------- | ----------- | --- | --- |
| Category    | Power                              |                 |             |     |     |
| Severity    | Error                              |                 |             |     |     |
| Description | Log54VPoweroverEthernetstatusfault |                 |             |     |     |
EventID:319
| Message     | Power over                          | Ethernet status | is good |     |     |
| ----------- | ----------------------------------- | --------------- | ------- | --- | --- |
| Category    | Power                               |                 |         |     |     |
| Severity    | Information                         |                 |         |     |     |
| Description | Log54VPoweroverEthernetstatusisgood |                 |         |     |     |
EventID:320
| Message  | PSU <name> | <alert> occurred |     |     |     |
| -------- | ---------- | ---------------- | --- | --- | --- |
| Category | Power      |                  |     |     |     |
Powerevents|224

| Severity    | Error                        |     |
| ----------- | ---------------------------- | --- |
| Description | LogwhenPSUvoltagealertoccurs |     |
EventID:321
| Message     | PSU <name>                     | <alert> recovered |
| ----------- | ------------------------------ | ----------------- |
| Category    | Power                          |                   |
| Severity    | Information                    |                   |
| Description | LogwhenPSUvoltagealertrecovers |                   |
EventID:322(Severity:Warning)
Message Invalid PoE power configuration, using default maximum PoE power
| Category    | Power                              |     |
| ----------- | ---------------------------------- | --- |
| Severity    | Warning                            |     |
| Description | LogwhenconfiguredPoEpowerisinvalid |     |
225
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |
| ----------------------------------------- | --- | ----------------------------- |

Chapter 91
|            |          |        | Power | over Ethernet | events |
| ---------- | -------- | ------ | ----- | ------------- | ------ |
| Power over | Ethernet | events |       |               |        |
ThefollowingaretheeventsrelatedtopoweroverEthernet.
EventID:7901
Message Detected powered device on interface <interface_name>. Type:<pd_type>,
Class:<pd_class>
| Category    | PoweroverEthernet                            |     |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                                  |     |     |     |     |
| Description | Detectedpowereddeviceoninterface.Type,Class. |     |     |     |     |
EventID:7902
Message Powered device power delivery on interface <interface_name>
| Category    | PoweroverEthernet                      |     |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                            |     |     |     |     |
| Description | Powereddevicepowerdeliveryoninterface. |     |     |     |     |
EventID:7903(Severity:Warning)
Message Powered device power denied on interface <interface_name>
| Category    | PoweroverEthernet                    |     |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- |
| Severity    | Warning                              |     |     |     |     |
| Description | Powereddevicepowerdeniedoninterface. |     |     |     |     |
EventID:7904(Severity:Warning)
Message Powered device fault on interface <interface_name>. Fault type <fault_
type>
| Category    | PoweroverEthernet                        |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Warning                                  |     |     |     |     |
| Description | Powereddevicefaultoninterface.Faulttype. |     |     |     |     |
EventID:7905
226
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message Powered device disconnected on interface <interface_name>
| Category    | PoweroverEthernet                     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- |
| Severity    | Information                           |     |     |     |
| Description | Powereddevicedisconnectedoninterface. |     |     |     |
EventID:7906
| Message     | PoE disabled           | on interface | <interface_name> |     |
| ----------- | ---------------------- | ------------ | ---------------- | --- |
| Category    | PoweroverEthernet      |              |                  |     |
| Severity    | Information            |              |                  |     |
| Description | PoEdisabledoninterface |              |                  |     |
EventID:7907
Message Powered device mps absent on interface <interface_name>
| Category    | PoweroverEthernet                 |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Information                       |     |     |     |
| Description | Powereddevicempsabsentoninterface |     |     |     |
EventID:7908
Message Detected dual signature powered device on interface <interface_name>.
|          | Type:<pd_type>,   | ClassA:<paira_class>, |     | ClassB:<pairb_class> |
| -------- | ----------------- | --------------------- | --- | -------------------- |
| Category | PoweroverEthernet |                       |     |                      |
| Severity | Information       |                       |     |                      |
Description Detecteddualsignaturepowereddeviceoninterface.Type,ClassA,ClassB
EventID:7909
Message Dual signature powered device power delivery on interface <interface_
name>
| Category | PoweroverEthernet |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| Severity | Information       |     |     |     |
Description Dualsignaturepowereddevicepowerdeliveryoninterface.
EventID:7910(Severity:Warning)
PoweroverEthernetevents|227

Message

Dual signature powered device fault on interface <interface_name> pair
<pair>. Fault type <fault_type>

Category

Power over Ethernet

Severity

Warning

Description

Dual signature powered device fault on interface. Fault type.

Event ID: 7911

Message

Dual signature powered device mps absent on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Dual signature powered device mps absent on interface

Event ID: 7912

Message

Powered device FET bad fault recovered on interface <interface_name>

Category

Power over Ethernet

Severity

Information

Description

Powered device FET bad fault recovered on interface

Event ID: 7913

Message

Powered device FET bad fault recovery failed on interface <interface_
name>

Category

Power over Ethernet

Severity

Information

Description

Powered device FET bad fault recovery failed on interface

Event ID: 7914

Message

Powered device got class demoted on interface <interface_name>.
Requested_class <req_class> Assigned_class <assigned_class>

Category

Power over Ethernet

Severity

Information

Description

Powered device got class demoted on interface

Event ID: 7915

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

228

Message Dual signature powered device got class demoted on interface
<interface_name>. Requested_classA <req_class_A> Requested_classB <req_
class_B> Assigned_classA <assigned_class_A> Assigned_classB <assigned_
class_B>
| Category | PoweroverEthernet |     |     |
| -------- | ----------------- | --- | --- |
| Severity | Information       |     |     |
Description Dualsignaturepowereddevicegotclassdemotedoninterface
EventID:7916
Message Powered device pre std detect enabled on interface <interface_name>
| Category    | PoweroverEthernet                           |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Severity    | Information                                 |     |     |
| Description | Powereddeviceprestddetectenabledoninterface |     |     |
EventID:7917
Message PoE usage exceeded threshold limit of <threshold_limit>
| Category    | PoweroverEthernet              |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | PoEusageexceededthresholdlimit |     |     |
EventID:7918
| Message     | PoE controller            | <cntrl_name> | got into fault |
| ----------- | ------------------------- | ------------ | -------------- |
| Category    | PoweroverEthernet         |              |                |
| Severity    | Information               |              |                |
| Description | PoEcontrollergotintofault |              |                |
EventID:7919
| Message     | PoE controller        | <cntrl_name> | got reset |
| ----------- | --------------------- | ------------ | --------- |
| Category    | PoweroverEthernet     |              |           |
| Severity    | Information           |              |           |
| Description | PoEcontrollergotreset |              |           |
EventID:7920
PoweroverEthernetevents|229

Message

Powered device got class promoted on interface <interface_
name>.Requested_class <req_class> Assigned_class <assigned_class>

Category

Power over Ethernet

Severity

Information

Description

Powered device got class promoted

Event ID: 7921

Message

Dual signature powered device got class promoted on interface
<interface_name>.Requested_classA <req_class_A> Requested_classB <req_
class_B> Assigned_classA <assigned_class_A> Assigned_classB <assigned_
class_B>

Category

Power over Ethernet

Severity

Information

Description

Dual signature powered device got class promoted

Event ID: 7922

Message

Powered device is drawing power more than its class on interface
<interface_name>, type:<pd_type> class:<pd_class> power:<power> is
exceeding the max average power of the PD class. Check the PD max power
draw, cabling type and length to improve interoperability

Category

Power over Ethernet

Severity

Information

Description

Powered device is drawing power more than its class

Event ID: 7923

Message

Powered device UVLO fault on interface <interface_name>, will attempt
to recover itself by toggling power

Category

Power over Ethernet

Severity

Information

Description

Powered device UVLO fault on interface

Event ID: 7924

Message

Powered device FET BAD fault on interface <interface_name>

Category

Power over Ethernet

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

230

| Severity    | Information              |     |     |     |
| ----------- | ------------------------ | --- | --- | --- |
| Description | PowereddeviceFETBADfault |     |     |     |
EventID:7925
Message Dual signature powered device is drawing power more than its class on
|          | interface            | <interface_name>, | type:<pd_type> | classA:<paira_class> |
| -------- | -------------------- | ----------------- | -------------- | -------------------- |
|          | classB:<pairb_class> | power:<power>     |                |                      |
| Category | PoweroverEthernet    |                   |                |                      |
| Severity | Information          |                   |                |                      |
Description Dualsignaturepowereddeviceisdrawingpowermorethanitsclass
EventID:7926
| Message     | PoE usage                | is below threshold | of <threshold_limit> |     |
| ----------- | ------------------------ | ------------------ | -------------------- | --- |
| Category    | PoweroverEthernet        |                    |                      |     |
| Severity    | Information              |                    |                      |     |
| Description | PoEusageisbelowthreshold |                    |                      |     |
EventID:7927(Severity:Warning)
Message Total power drawn: <power_drawn>W by powered device is exceeding the
total available PoE power:<power_available>W. Check the PD max power
|             | draw, cabling                            | type and length | to avoid system | crowbar. |
| ----------- | ---------------------------------------- | --------------- | --------------- | -------- |
| Category    | PoweroverEthernet                        |                 |                 |          |
| Severity    | Warning                                  |                 |                 |          |
| Description | PoEdrawnpowerismorethanavailablePoEpower |                 |                 |          |
EventID:7928(Severity:Warning)
Message Powered device invalid signature indication on interface <interface_
name>.
| Category    | PoweroverEthernet                       |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Warning                                 |     |     |     |
| Description | Powereddeviceinvalidsignatureindication |     |     |     |
EventID:7929
PoweroverEthernetevents|231

| Message     | PoE hardware                   | access daemon | exiting |     |
| ----------- | ------------------------------ | ------------- | ------- | --- |
| Category    | PoweroverEthernet              |               |         |     |
| Severity    | Information                    |               |         |     |
| Description | PoEhardwareaccessdaemonexiting |               |         |     |
EventID:7930
| Message     | POE proto             | daemon exiting |     |     |
| ----------- | --------------------- | -------------- | --- | --- |
| Category    | PoweroverEthernet     |                |     |     |
| Severity    | Information           |                |     |     |
| Description | POEprotodaemonexiting |                |     |     |
EventID:7931
Message Always-on PoE detected a powered device on interface <interface_name>
|             | and delivered                                 | power |     |     |
| ----------- | --------------------------------------------- | ----- | --- | --- |
| Category    | PoweroverEthernet                             |       |     |     |
| Severity    | Information                                   |       |     |     |
| Description | Always-onPoEdetectedapowereddeviceoninterface |       |     |     |
EventID:7932
Message Powered device disconnected on interface <interface_name> due to LLDP
dot3 disable
| Category | PoweroverEthernet |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| Severity | Information       |     |     |     |
Description PowereddevicedisconnectedoninterfaceduetoLLDPdot3disable
EventID:7933
| Message     | Subsystem                   | <subsys_name> | came up with | quick PoE |
| ----------- | --------------------------- | ------------- | ------------ | --------- |
| Category    | PoweroverEthernet           |               |              |           |
| Severity    | Information                 |               |              |           |
| Description | SubsystemcameupwithquickPoE |               |              |           |
EventID:7934
232
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message

Quick PoE detected a powered device on interface <interface_name> and
delivered power

Category

Power over Ethernet

Severity

Information

Description

Quick PoE detected a powered device on interface

Event ID: 7935 (Severity: Warning)

Message

Powered device denied on interface <interface_name> of line module with
Quick PoE enabled. Remove device to avoid crowbar on reboot.

Category

Power over Ethernet

Severity

Warning

Description

Powered device denied on interface of line module with Quick PoE enabled.

Event ID: 7936 (Severity: Warning)

Message

Powered device demoted on interface <interface_name> of line module
with Quick PoE enabled. Remove device to avoid crowbar on reboot.

Category

Power over Ethernet

Severity

Warning

Description

Powered device demoted on interface of line module with Quick PoE enabled

Event ID: 7937 (Severity: Warning)

Message

PoE disable ignored on interface <interface_name> because Quick PoE is
enabled

Category

Power over Ethernet

Severity

Warning

Description

PoE disable ignored on interface because Quick PoE is enabled

Event ID: 7938 (Severity: Warning)

Message

PoE assigned class configuration is ignored on interface <interface_
name> because Quick PoE is enabled

Category

Power over Ethernet

Severity

Warning

Description

PoE assigned class configuration is ignored on interface because Quick PoE is enabled

Event ID: 7939

Power over Ethernet events | 233

Message

Powered device requested power down on interface <interface_name>
<duration>

Category

Power over Ethernet

Severity

Information

Description

Powered device requested power down on interface.

Event ID: 7940

Message

Powered device disconnected on interface <interface_name> due to pd-
class-override config change

Category

Power over Ethernet

Severity

Information

Description

Powered device disconnected on interface due to pd-class-override config change

Event ID: 7941

Message

Powered device disconnected on interface <interface_name> due to power-
pairs config change

Category

Power over Ethernet

Severity

Information

Description

Powered device disconnected on interface due to power-pairs config change

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

234

Chapter 92
PTP events
PTP events
ThefollowingaretheeventsrelatedtoPTP.
EventID:12101
Message PTP <type> <delay_mechanism> <clock_step> clock started with profile
|             | <profile>                           | and transport | <transport>. |
| ----------- | ----------------------------------- | ------------- | ------------ |
| Category    | PTP                                 |               |              |
| Severity    | Information                         |               |              |
| Description | EventreportedwhenPTPclockisstarted. |               |              |
EventID:12102
| Message     | PTP clock                           | stopped. Reason: | <reason> |
| ----------- | ----------------------------------- | ---------------- | -------- |
| Category    | PTP                                 |                  |          |
| Severity    | Information                         |                  |          |
| Description | EventreportedwhenPTPclockisstopped. |                  |          |
EventID:12103
| Message     | Interface                                    | <name> enabled | for PTP exchange. |
| ----------- | -------------------------------------------- | -------------- | ----------------- |
| Category    | PTP                                          |                |                   |
| Severity    | Information                                  |                |                   |
| Description | EventreportedwhenPTPportisenabledfortxandrx. |                |                   |
EventID:12104
Message Interface <name> disabled for PTP exchange. Reason: <reason>
| Category    | PTP                                        |     |     |
| ----------- | ------------------------------------------ | --- | --- |
| Severity    | Information                                |     |     |
| Description | EventreportedwhenPTPenabledportisdisabled. |     |     |
EventID:12105
235
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | PTP clock                               | is in <state> | state |     |
| ----------- | --------------------------------------- | ------------- | ----- | --- |
| Category    | PTP                                     |               |       |     |
| Severity    | Information                             |               |       |     |
| Description | EventreportedfordifferentPTPclockstate. |               |       |     |
EventID:12106
| Message     | Interface                              | <name> | is in <state> | state |
| ----------- | -------------------------------------- | ------ | ------------- | ----- |
| Category    | PTP                                    |        |               |       |
| Severity    | Information                            |        |               |       |
| Description | EventreportedfordifferentPTPportstate. |        |               |       |
EventID:12107
Message New GrandSource/Parent is selected: Parent: <parent>, GrandSource:
<grandsource>, Quality: <quality>, Priority1: <priority1>, Priority2:
<priority2>
| Category    | PTP                                           |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | EventreportedwhenPTPparentisupdated/modified. |     |     |     |
EventID:12108
Message PTP operational log_announce_interval is changed to <value> on
|          | interface   | <name> | for profile | <profile> |
| -------- | ----------- | ------ | ----------- | --------- |
| Category | PTP         |        |             |           |
| Severity | Information |        |             |           |
Description EventreportedwhenPTPlogannounceintervalismodified.
EventID:12109
Message PTP operational log_min_pdelay_request_interval is changed to <value>
|          | on interface | <name> | for profile | <profile> |
| -------- | ------------ | ------ | ----------- | --------- |
| Category | PTP          |        |             |           |
| Severity | Information  |        |             |           |
Description EventreportedwhenPTPlogminpdelayrequestintervalismodified.
EventID:12110
PTPevents|236

Message PTP operational log_min_delay_request_interval is changed to <value> on
|          | interface   | <name> for | profile <profile> |
| -------- | ----------- | ---------- | ----------------- |
| Category | PTP         |            |                   |
| Severity | Information |            |                   |
Description EventreportedwhenPTPlogmindelayrequestintervalismodified.
EventID:12111
Message PTP operational sync_request_timeout is changed to <value> on interface
|          | <name>      | for profile | <profile> |
| -------- | ----------- | ----------- | --------- |
| Category | PTP         |             |           |
| Severity | Information |             |           |
Description EventreportedwhenPTPsyncrequesttimeoutismodified.
EventID:12112
Message PTP operational sync_interval is changed to <value> on interface <name>
|             | for profile                                 | <profile> |     |
| ----------- | ------------------------------------------- | --------- | --- |
| Category    | PTP                                         |           |     |
| Severity    | Information                                 |           |     |
| Description | EventreportedwhenPTPsyncintervalismodified. |           |     |
EventID:12113
Message PTP operational announce_request_timeout is changed to <value> on
|          | interface   | <name> for | profile <profile> |
| -------- | ----------- | ---------- | ----------------- |
| Category | PTP         |            |                   |
| Severity | Information |            |                   |
Description EventreportedwhenPTPannouncerequesttimeoutismodified.
EventID:12114
| Message     | PTP config                                | invalid. | Reason: <reason> |
| ----------- | ----------------------------------------- | -------- | ---------------- |
| Category    | PTP                                       |          |                  |
| Severity    | Information                               |          |                  |
| Description | EventreportedifPTPconfigurationisinvalid. |          |                  |
EventID:12115
237
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Message     | PTP domain                                       | modified | from | <old> | to <new> | value |
| ----------- | ------------------------------------------------ | -------- | ---- | ----- | -------- | ----- |
| Category    | PTP                                              |          |      |       |          |       |
| Severity    | Information                                      |          |      |       |          |       |
| Description | EventreportedifPTPdomainconfigurationismodified. |          |      |       |          |       |
EventID:12116
| Message     | PTP vlan                                       | modified | from | <old> to | <new> | on port <port> |
| ----------- | ---------------------------------------------- | -------- | ---- | -------- | ----- | -------------- |
| Category    | PTP                                            |          |      |          |       |                |
| Severity    | Information                                    |          |      |          |       |                |
| Description | EventreportedifPTPvlanconfigurationismodified. |          |      |          |       |                |
EventID:12117
| Message  | PTP source_ip_interface |     |     | <action>. | Port: | <value> |
| -------- | ----------------------- | --- | --- | --------- | ----- | ------- |
| Category | PTP                     |     |     |           |       |         |
| Severity | Information             |     |     |           |       |         |
Description EventreportedifPTPsource_ip_interfaceconfigurationismodified.
EventID:12118
| Message     | PTP source_ip                                       | <action>. |     | IP: <value> |     |     |
| ----------- | --------------------------------------------------- | --------- | --- | ----------- | --- | --- |
| Category    | PTP                                                 |           |     |             |     |     |
| Severity    | Information                                         |           |     |             |     |     |
| Description | EventreportedifPTPsource_ipconfigurationismodified. |           |     |             |     |     |
PTPevents|238

|          |          |        |     |          | Chapter  | 93     |
| -------- | -------- | ------ | --- | -------- | -------- | ------ |
|          |          |        |     | QoS ASIC | Provider | events |
| QoS ASIC | Provider | events |     |          |          |        |
ThefollowingaretheeventsrelatedtoqualityofserviceASICprovider.
EventID:5801(Severity:Warning)
Message QoS failed initial initialization for slot <local_slot>. Error: <error>
| Category    |     | QoSASICProvider                |     |     |     |     |
| ----------- | --- | ------------------------------ | --- | --- | --- | --- |
| Severity    |     | Warning                        |     |     |     |     |
| Description |     | QoSinitialinitializationfailed |     |     |     |     |
EventID:5802(Severity:Critical)
Message QoS failed final initialization on new slot <new_slot> for peer slot
<existing_slot>
| Category    |     | QoSASICProvider                        |     |     |     |     |
| ----------- | --- | -------------------------------------- | --- | --- | --- | --- |
| Severity    |     | Critical                               |     |     |     |     |
| Description |     | QoSfinalinitializationfailedfornewslot |     |     |     |     |
EventID:5803
| Message     |     | QoS error after card     | removal from | slot <slot> |     |     |
| ----------- | --- | ------------------------ | ------------ | ----------- | --- | --- |
| Category    |     | QoSASICProvider          |              |             |     |     |
| Severity    |     | Error                    |              |             |     |     |
| Description |     | QoSerroraftercardremoval |              |             |     |     |
EventID:5804
Message Error during QoS feature configuration: <error_string>
| Category    |     | QoSASICProvider                             |     |     |     |     |
| ----------- | --- | ------------------------------------------- | --- | --- | --- | --- |
| Severity    |     | Error                                       |     |     |     |     |
| Description |     | ErrorwhileattemptingQoSfeatureconfiguration |     |     |     |     |
EventID:5805
239
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

Error during QoS HW configuration: <error_string> error <val>

Category

QoS ASIC Provider

Severity

Error

Description

Error while attempting QoS HW configuration

Event ID: 5806 (Severity: Warning)

Message

Port: <port_name> PFC priority <pri> using queue <queue> should not be
sharing the queue with other local-priorities

Category

QoS ASIC Provider

Severity

Warning

Description

Warning PFC priority sharing a queue

QoS ASIC Provider events | 240

Chapter 94
|                    |        |     | Quality | of Service | events |
| ------------------ | ------ | --- | ------- | ---------- | ------ |
| Quality of Service | events |     |         |            |        |
Thefollowingaretheeventsrelatedtoqualityofservice.
EventID:5701
Message QoS failed to retrieve default information. Error: <error>
| Category    | QualityofService                        |     |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                             |     |     |     |     |
| Description | QoSfailedtoretrievedefaultconfiguration |     |     |     |     |
EventID:5702
| Message     | QoS error:       | <error_string> |     |     |     |
| ----------- | ---------------- | -------------- | --- | --- | --- |
| Category    | QualityofService |                |     |     |     |
| Severity    | Error            |                |     |     |     |
| Description | QoSerroroccurred |                |     |     |     |
EventID:5703(Severity:Warning)
Message The PFC configuration for interface <ifname> exceeds the system limit
|          | of <limit>       | unique combinations | and was not | applied |     |
| -------- | ---------------- | ------------------- | ----------- | ------- | --- |
| Category | QualityofService |                     |             |         |     |
| Severity | Warning          |                     |             |         |     |
Description Loggedwhentherearemoreuniquecombinationsofflowcontrolledprioritiesthanthe
systemallows.
241
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 95
|     |     | Rapid | per VLAN | Spanning | Tree Protocol |
| --- | --- | ----- | -------- | -------- | ------------- |
events
| Rapid per | VLAN Spanning | Tree Protocol | events |     |     |
| --------- | ------------- | ------------- | ------ | --- | --- |
ThefollowingaretheeventsrelatedtorapidperVLANspanningtreeprotocol.
EventID:5001
| Message | RPVST Enabled |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- |
Category RapidperVLANSpanningTreeProtocol
Severity Information
Description ThislogeventindicatesthatRPVSThasbeenenabledontheswitch.
EventID:5002
| Message | RPVST Disabled |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
Category RapidperVLANSpanningTreeProtocol
Severity Information
Description ThislogeventindicatesthatRPVSThasbeendisabledontheswitch.
EventID:5003
Message RPVST - Root changed from <old_priority>: <old_mac> to <new_priority>:
|     | <new_mac> | on VLAN <vlan>. |     |     |     |
| --- | --------- | --------------- | --- | --- | --- |
Category RapidperVLANSpanningTreeProtocol
Severity Information
Description ThislogeventindicatesthatRPVSTrootonaVLANhaschanged
EventID:5004(Severity:Warning)
Message Port <port> disabled - BPDU received on protected port on VLAN <vlan>.
Category RapidperVLANSpanningTreeProtocol
Severity Warning
Description ThislogeventinformstheuserBPDUreceivedonprotectedport
EventID:5005
242
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Message <proto> starved for <pkt_type> on port <port> from <priority_mac> on
VLAN <vlan>.
| Category | RapidperVLANSpanningTreeProtocol |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description ThislogeventinformstheuserthattheRxisstarvedinpaticularport
EventID:5006
Message Topology change received on port <port> from source: <mac> on VLAN
<vlan>.
| Category | RapidperVLANSpanningTreeProtocol |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description ThislogeventinformstheuserthattheRPVSTtopologychangeisreceived
EventID:5007
Message Topology change generated on port <port> on VLAN <vlan>.
| Category | RapidperVLANSpanningTreeProtocol |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description ThislogeventinformstheuserthattheRPVSTtopologychangeisgenerated
EventID:5008(Severity:Warning)
| Message  | Port <port>                      | blocked | on RPVST <instance> |
| -------- | -------------------------------- | ------- | ------------------- |
| Category | RapidperVLANSpanningTreeProtocol |         |                     |
| Severity | Warning                          |         |                     |
Description Thislogeventinformstheuserthattheportisblockedontheinstance
EventID:5009(Severity:Warning)
| Message  | Port <port>                      | unblocked | on RPVST <instance> |
| -------- | -------------------------------- | --------- | ------------------- |
| Category | RapidperVLANSpanningTreeProtocol |           |                     |
| Severity | Warning                          |           |                     |
Description Thislogeventinformstheuserthattheportisunblockedontheinstance
EventID:5010
RapidperVLANSpanningTreeProtocolevents|243

Message

Root port changed from <old_port> to <new_port> on VLAN <vlan>.

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Information

Description

This log event informs the user that the root port is changed

Event ID: 5011

Message

PVID mismatch detected on <interface> with pvid = <pvid>, Neighbor pvid
= <npvid>' throttle_count: 100

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Information

Description

Log event when the PVID mismatches between the switch and neighbor over an interface

Event ID: 5012

Message

spanning tree mode changed from <old_mode> to <new_mode>, it will
trigger the reconvergence

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Information

Description

This log event informs the user that the spanning tree mode is changed.

Event ID: 5013

Message

Current Virtual Ports <Current_Virtual_Ports> exceeds the max supported
limit <Maximum_Virtual_Ports>

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Information

Description

Log event when the current virtual port count crosses the maximum allowed value

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

244

Chapter 96
RBAC events
RBAC events
ThefollowingaretheeventsrelatedtoRBAC.
EventID:10301
| Message     | Local authorization                           |     | has been <tac_status>d |
| ----------- | --------------------------------------------- | --- | ---------------------- |
| Category    | RBAC                                          |     |                        |
| Severity    | Information                                   |     |                        |
| Description | Logeventwhenlocaltac_plusserverhasbeenstarted |     |                        |
EventID:10302
| Message     | Failed                                       | to <tac_status> | local authorization |
| ----------- | -------------------------------------------- | --------------- | ------------------- |
| Category    | RBAC                                         |                 |                     |
| Severity    | Error                                        |                 |                     |
| Description | Logeventwhenlocaltac_plusserverfailedtostart |                 |                     |
245
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 97
|           |            |        | Redundant | Management | events |
| --------- | ---------- | ------ | --------- | ---------- | ------ |
| Redundant | Management | events |           |            |        |
Thefollowingaretheeventsrelatedtoredundantmanagement.
EventID:2201
| Message     | Failover                                       | detected: Reason | <reason> |     |     |
| ----------- | ---------------------------------------------- | ---------------- | -------- | --- | --- |
| Category    | RedundantManagement                            |                  |          |     |     |
| Severity    | Information                                    |                  |          |     |     |
| Description | Thislogeventinformsthatfailovereventisdetected |                  |          |     |     |
EventID:2202
Message Lost <mgmt_module> as Standby Management Module, redundancy disabled
| Category | RedundantManagement |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
| Severity | Information         |     |     |     |     |
Description Thislogeventinformsthatstandbymgmtmodulehasbeenremoved
EventID:2203
Message Detected the removal of the Standby Management Module
| Category | RedundantManagement |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
| Severity | Information         |     |     |     |     |
Description Thislogeventinformsthatstandbymgmtmodulehasbeenremoved
EventID:2204
| Message  | <mgmt_module>       | is Active |     |     |     |
| -------- | ------------------- | --------- | --- | --- | --- |
| Category | RedundantManagement |           |     |     |     |
| Severity | Information         |           |     |     |     |
Description ThislogeventinformsaboutthestatusofActivemgmtmodule
EventID:2205
246
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

| Message  | <mgmt_module>       | is Standby |     |
| -------- | ------------------- | ---------- | --- |
| Category | RedundantManagement |            |     |
| Severity | Information         |            |     |
Description ThislogeventinformsaboutthestatusofStandbymgmtmodule
EventID:2206
Message Detected <mgmt_module> as Standby Management Module, redundancy enabled
| Category | RedundantManagement |     |     |
| -------- | ------------------- | --- | --- |
| Severity | Information         |     |     |
Description Thislogeventinformsthatstandbymgmtmoduleisaddedtothesystem
EventID:2207
Message Remote Standby Management module recover detected. Reason: Heartbeat
loss
| Category | RedundantManagement |     |     |
| -------- | ------------------- | --- | --- |
| Severity | Information         |     |     |
Description ThislogeventinformstheuserthatActivemgmtmodulehasdetectedheartbeatloss
EventID:2208
| Message     | <mgmt_module>                                      | is waiting | for filesync |
| ----------- | -------------------------------------------------- | ---------- | ------------ |
| Category    | RedundantManagement                                |            |              |
| Severity    | Information                                        |            |              |
| Description | Thislogeventinformstheuserthatfilesyncisinprogress |            |              |
EventID:2209
| Message  | <mgmt_module>       | is starting | ISSU operation |
| -------- | ------------------- | ----------- | -------------- |
| Category | RedundantManagement |             |                |
| Severity | Information         |             |                |
Description ThislogeventinformstheuserthatanISSUoperationhasbegun
RedundantManagementevents|247

Chapter 98
|             |         |        |     | Replication |     | Manager | events |
| ----------- | ------- | ------ | --- | ----------- | --- | ------- | ------ |
| Replication | Manager | events |     |             |     |         |        |
Thefollowingaretheeventsrelatedtoreplicationmanager.
EventID:2701(Severity:Warning)
| Message     | All                                      | bitmaps have | been allocated |     |     |     |     |
| ----------- | ---------------------------------------- | ------------ | -------------- | --- | --- | --- | --- |
| Category    | ReplicationManager                       |              |                |     |     |     |     |
| Severity    | Warning                                  |              |                |     |     |     |     |
| Description | Logtoindicateallbitmapshavebeenallocated |              |                |     |     |     |     |
EventID:2702(Severity:Warning)
| Message  | Over               | 80 percent | of bitmaps | have been | allocated |     |     |
| -------- | ------------------ | ---------- | ---------- | --------- | --------- | --- | --- |
| Category | ReplicationManager |            |            |           |           |     |     |
| Severity | Warning            |            |            |           |           |     |     |
Description Logtoindicateover80percentofbitmapshavebeenallocated
EventID:2705(Severity:Warning)
Message Multicast L3 Bridge Control Forwarding entry with uuid <uuid_str> has
|          | no                 | reference | to a VLAN |     |     |     |     |
| -------- | ------------------ | --------- | --------- | --- | --- | --- | --- |
| Category | ReplicationManager |           |           |     |     |     |     |
| Severity | Warning            |           |           |     |     |     |     |
Description LogindicatesMutlicastL3BridgeControlForwardingentrywithuuidhasnoreferencetoa
VLAN
248
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |

Chapter 99

REST events

REST events

The following are the events related to REST.

Event ID: 4601

Message

Authentication failed for user <user> in session <sessionid>

Category

Severity

REST

Error

Description

logs a failed authentication attempt of a user via REST

Event ID: 4602

Message

Authentication succeeded for user <user> in session <sessionid>

Category

REST

Severity

Information

Description

logs a successful authentication attempt of a user via REST

Event ID: 4603 (Severity: Critical)

Message

Category

Severity

Conflict in authorization configuration. Existing config::URL(<match>),
type(<value>) New config::(<url>), type(<autztype>)

REST

Critical

Description

logs an authorization configuration conflict

Event ID: 4606

Message

Category

Severity

Authorization failed for user <user>, for resource <resource>, with
action <action>

REST

Error

Description

logs a failed authorization attempt of a user via REST

Event ID: 4607

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

249

Message Authorization succeeded for user <user>, for resource <resource>, with
action <action>
| Category    | REST                                              |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Information                                       |     |     |
| Description | logsasuccessfulauthorizationattemptofauserviaREST |     |     |
EventID:4608
Message Authorization allowed for user <user>, for resource <resource>, with
action <action>
| Category    | REST                                            |     |     |
| ----------- | ----------------------------------------------- | --- | --- |
| Severity    | Information                                     |     |     |
| Description | logsanallowedauthorizationattemptofauserviaREST |     |     |
EventID:4609
Message User <user> added <added_user> with role <added_user_role>
| Category    | REST                             |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | logsasuccessfuladdofauserviaREST |     |     |
EventID:4610
| Message     | User <user>                           | deleted <deleted_user> |     |
| ----------- | ------------------------------------- | ---------------------- | --- |
| Category    | REST                                  |                        |     |
| Severity    | Information                           |                        |     |
| Description | logsasuccessfuldeletionofauserviaREST |                        |     |
EventID:4611
| Message     | User <user>                                  | successfully | changed password |
| ----------- | -------------------------------------------- | ------------ | ---------------- |
| Category    | REST                                         |              |                  |
| Severity    | Information                                  |              |                  |
| Description | logsasuccessfulpasswordchangeforauserviaREST |              |                  |
EventID:4612(Severity:Warning)
RESTevents|250

| Message     | User <user>                                     | password | change failed |
| ----------- | ----------------------------------------------- | -------- | ------------- |
| Category    | REST                                            |          |               |
| Severity    | Warning                                         |          |               |
| Description | logsanunsuccessfulpasswordchangeforauserviaREST |          |               |
EventID:4613
Message <user> has written a new switch configuration to <config_name>
| Category    | REST                             |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | logsasuccessconfigwriteoperation |     |     |
EventID:4614
Message <user> has copied switch configuration <from_name> to <to_name>
| Category    | REST                    |     |     |
| ----------- | ----------------------- | --- | --- |
| Severity    | Information             |     |     |
| Description | logsasuccesscopyofsaved |     |     |
EventID:4615
Message <user> has configured <dns_nameserver> DNS nameserver to <dns>
| Category    | REST                                          |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Information                                   |     |     |
| Description | logsasuccesswhenthenameserveriswrittentoovsdb |     |     |
EventID:4616
| Message     | <user> has                                      | deleted all | DNS nameservers |
| ----------- | ----------------------------------------------- | ----------- | --------------- |
| Category    | REST                                            |             |                 |
| Severity    | Information                                     |             |                 |
| Description | logsasuccesswhenthenameserverisdeletedfromovsdb |             |                 |
EventID:4617
| Message | <user> created | <uri> |     |
| ------- | -------------- | ----- | --- |
251
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Category    | REST                                            |     |     |
| ----------- | ----------------------------------------------- | --- | --- |
| Severity    | Information                                     |     |     |
| Description | AuserhassuccessfullycreatedanewresourceinOVSDB. |     |     |
EventID:4618
| Message     | <user> deleted                               | <uri> |     |
| ----------- | -------------------------------------------- | ----- | --- |
| Category    | REST                                         |       |     |
| Severity    | Information                                  |       |     |
| Description | AuserhassuccessfullydeletedaresourceinOVSDB. |       |     |
EventID:4619
| Message     | <user> modified                               | <uri> |     |
| ----------- | --------------------------------------------- | ----- | --- |
| Category    | REST                                          |       |     |
| Severity    | Information                                   |       |     |
| Description | AuserhassuccessfullymodifiedaresourceinOVSDB. |       |     |
EventID:4620
| Message     | User: <user>                            | added subscriber: | <subscriber>. |
| ----------- | --------------------------------------- | ----------------- | ------------- |
| Category    | REST                                    |                   |               |
| Severity    | Information                             |                   |               |
| Description | Auserhasaddednewnotificationsubscriber. |                   |               |
EventID:4621
| Message     | User: <user>                           | removed subscriber: | <subscriber>. |
| ----------- | -------------------------------------- | ------------------- | ------------- |
| Category    | REST                                   |                     |               |
| Severity    | Information                            |                     |               |
| Description | Auserhasremovednotificationsubscriber. |                     |               |
EventID:4622
Message Subscriber: <subscriber> added subscription: <subscription>.
| Category | REST |     |     |
| -------- | ---- | --- | --- |
RESTevents|252

| Severity    | Information                         |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Description | Asubscriberhasaddednewsubscription. |     |     |     |
EventID:4623
Message Subscriber: <subscriber> removed subscription: <subscription>.
| Category    | REST                               |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Information                        |     |     |     |
| Description | Asubscriberhasremovedsubscription. |     |     |     |
EventID:4624(Severity:Warning)
Message Unable to add new subscriber. Max number of subscribers has been
reached.
| Category    | REST                                        |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                     |     |     |     |
| Description | Unabletoaddnewsubscriberasmaxnumberreached. |     |     |     |
EventID:4625(Severity:Warning)
Message Unable to add new subscription. Max number of subscriptions for
|          | <subscriber> | has been | reached. |     |
| -------- | ------------ | -------- | -------- | --- |
| Category | REST         |          |          |     |
| Severity | Warning      |          |          |     |
Description Unabletoaddnewsubscriptionasmaxnumberreachedforthespecifiedsubscriber.
EventID:4626
| Message     | NAE Script                           | <name> has | been created | by user <user>. |
| ----------- | ------------------------------------ | ---------- | ------------ | --------------- |
| Category    | REST                                 |            |              |                 |
| Severity    | Information                          |            |              |                 |
| Description | NAEScripthasbeencreatedsuccessfully. |            |              |                 |
EventID:4627
| Message  | NAE Script | <name> has | been deleted | by user <user>. |
| -------- | ---------- | ---------- | ------------ | --------------- |
| Category | REST       |            |              |                 |
253
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Information                          |     |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- |
| Description | NAEScripthasbeendeletedsuccessfully. |     |     |     |     |
EventID:4628
| Message     | NAE Agent                           | <name> has | been created | by user <user>. |     |
| ----------- | ----------------------------------- | ---------- | ------------ | --------------- | --- |
| Category    | REST                                |            |              |                 |     |
| Severity    | Information                         |            |              |                 |     |
| Description | NAEAgenthasbeencreatedsuccessfully. |            |              |                 |     |
EventID:4629
| Message     | NAE Agent                           | <name> has | been updated | by user <user>. |     |
| ----------- | ----------------------------------- | ---------- | ------------ | --------------- | --- |
| Category    | REST                                |            |              |                 |     |
| Severity    | Information                         |            |              |                 |     |
| Description | NAEAgenthasbeenupdatedsuccessfully. |            |              |                 |     |
EventID:4630
| Message     | NAE Agent                           | <name> has | been deleted | by user <user>. |     |
| ----------- | ----------------------------------- | ---------- | ------------ | --------------- | --- |
| Category    | REST                                |            |              |                 |     |
| Severity    | Information                         |            |              |                 |     |
| Description | NAEAgenthasbeendeletedsuccessfully. |            |              |                 |     |
EventID:4631
Message Error rebooting switch, reboot command: <command>, error received:
<error>
| Category    | REST                       |     |     |     |     |
| ----------- | -------------------------- | --- | --- | --- | --- |
| Severity    | Error                      |     |     |     |     |
| Description | Logsanerrorifarebootfails. |     |     |     |     |
EventID:4632
Message Connection to Aruba Central on location <central_location> on VRF <vrf>
|          | with Source | IP <source_ip> | has | been successfully | established. |
| -------- | ----------- | -------------- | --- | ----------------- | ------------ |
| Category | REST        |                |     |                   |              |
RESTevents|254

Severity

Information

Description

Connection is established with Aruba Central.

Event ID: 4633

Message

Connection to Aruba Central on location <central_location> on VRF <vrf>
and Source IP <source_ip> has been closed by Aruba Central. Requesting
new Aruba Central location from CLI/DHCP/Activate.

Category

REST

Severity

Information

Description

Connection to Aruba Central has been closed by Aruba Central. Request to get new
location from CLI/DHCP/Activate.

Event ID: 4634

Message

Connection to Aruba Central on location <central_location> on VRF <vrf>
and Source IP <source_ip> has been closed by Aruba Central. Trying to
reconnect.

Category

REST

Severity

Information

Description

Connection to Aruba Central has been closed by Aruba Central. Trying to reconnect.

Event ID: 4635

Message

Received Aruba Central location <central_location> on VRF <vrf> with
Source IP <source_ip>

Category

REST

Severity

Information

Description

Received new Aruba Central location.

Event ID: 4636

Message

Received new Aruba Central location. Closing existing connection with
Aruba Central on location <central_location> on VRF <vrf> with Source
IP <source_ip>.

Category

REST

Severity

Information

Description

Received new Aruba Central location. Closing existing connection with Aruba Central.

Event ID: 4637

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

255

Message Internal error. Closing connection to Aruba Central on location
|             | <central_location>                             |     | on VRF <vrf> | with Source | IP <source_ip>. |
| ----------- | ---------------------------------------------- | --- | ------------ | ----------- | --------------- |
| Category    | REST                                           |     |              |             |                 |
| Severity    | Error                                          |     |              |             |                 |
| Description | Internalerror.ClosingconnectiontoArubaCentral. |     |              |             |                 |
EventID:4638
Message Waiting for Aruba Central location from CLI/DHCP/Aruba Activate Server.
| Category | REST        |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
| Severity | Information |     |     |     |     |
Description WaitingforArubaCentrallocationfromCentralSource(CLI/DHCP/ArubaActivate
Server).
EventID:4639
Message Connecting to Aruba Central on location <central_location> on VRF <vrf>
|             | with Source               | IP <source_ip>. |     |     |     |
| ----------- | ------------------------- | --------------- | --- | --- | --- |
| Category    | REST                      |                 |     |     |     |
| Severity    | Information               |                 |     |     |     |
| Description | ConnectingtoArubaCentral. |                 |     |     |     |
EventID:4640
Message Failed to connect to Aruba Central on location <central_location> on
|             | VRF <vrf>                      | with Source | IP <source_ip> |     |     |
| ----------- | ------------------------------ | ----------- | -------------- | --- | --- |
| Category    | REST                           |             |                |     |     |
| Severity    | Error                          |             |                |     |     |
| Description | FailedtoconnecttoArubaCentral. |             |                |     |     |
EventID:4641
| Message     | Aruba Central                     | is disabled. |     |     |     |
| ----------- | --------------------------------- | ------------ | --- | --- | --- |
| Category    | REST                              |              |     |     |     |
| Severity    | Information                       |              |     |     |     |
| Description | TheArubaCentralfeatureisdisabled. |              |     |     |     |
EventID:4642
RESTevents|256

Message Aruba Central is disabled. Closing connection to Aruba Central on
location <central_location> on VRF <vrf> with Source IP <source_ip>
| Category    | REST                              |     |     |
| ----------- | --------------------------------- | --- | --- |
| Severity    | Information                       |     |     |
| Description | TheArubaCentralfeatureisdisabled. |     |     |
EventID:4643
| Message     | Aruba Central                    | is enabled. |     |
| ----------- | -------------------------------- | ----------- | --- |
| Category    | REST                             |             |     |
| Severity    | Information                      |             |     |
| Description | TheArubaCentralfeatureisenabled. |             |     |
EventID:4645
Message Aruba Activate server <activate_address> is reachable via VRF <vrf>.
| Category    | REST                                          |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Information                                   |     |     |
| Description | ArubaActivateserverisreachableviaanactiveVRF. |     |     |
EventID:4646
Message Aruba Activate server <activate_address> is not reachable through any
|          | supported   | VRF. |     |
| -------- | ----------- | ---- | --- |
| Category | REST        |      |     |
| Severity | Information |      |     |
Description ArubaActivateserverisnotreachablethroughanysupportedVRF.
EventID:4647
| Message     | Switch time                       | is synced | with NTP Servers. |
| ----------- | --------------------------------- | --------- | ----------------- |
| Category    | REST                              |           |                   |
| Severity    | Information                       |           |                   |
| Description | SwitchtimeissyncedwithNTPServers. |           |                   |
EventID:4648
257
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Message

Switch time is synced with Aruba Activate Server <activate_address>.

Category

REST

Severity

Information

Description

Switch time is synced with Aruba Activate Server.

Event ID: 4649

Message

Category

Severity

Unable to sync switch time with Aruba Activate Server <activate_
address> via VRF <vrf>.

REST

Error

Description

Unable to sync switch time with Aruba Activate Server.

Event ID: 4650

Message

Unable to fetch Aruba Central location <central_location> from
<central_source> via VRF <vrf>.

Category

REST

Severity

Information

Description

Unable to fetch Aruba Central location from Central Source (CLI/DHCP/Aruba Activate
Server).

Event ID: 4651

Message

Aruba Central location <central_location> successfully fetched from
<central_source> via VRF <vrf>

Category

REST

Severity

Information

Description

Aruba Central location successfully fetched from Central Source (CLI/DHCP/Aruba
Activate Server) via VRF.

Event ID: 4652 (Severity: Warning)

Message

Aruba Central connected, any config change through rest <rest_
operation> operation may not be persistent. If central reapplies the
config, change can be overwritten

Category

REST

Severity

Warning

REST events | 258

Description

Aruba Central connected, any config change through rest may not be persistent, aruba
central can overwrite the change

Event ID: 4653

Message

User <user> has configured <mode> for configuration lockout

Category

REST

Severity

Information

Description

Logs a message when a user changes the REST configuration lockout mode

Event ID: 4654

Message

Aruba Central support mode is <mode> for a vtysh session

Category

REST

Severity

Information

Description

Logs a message when a Aruba Central support mode is enabled or disabled

Event ID: 4655

Message

User <user_name> logged in from <identity> through REST session

Category

REST

Severity

Information

Description

Logs a message when a user login is successful

Event ID: 4656

Message

User <user_name> login from <identity> for REST session has failed

Category

Severity

REST

Error

Description

Logs a message when a user login fails

Event ID: 4657

Message

User <user_name> logged out of REST session from <identity>

Category

REST

Severity

Information

Description

Logs a message when a user logs out of a session

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

259

EventID:4658(Severity:Warning)
Message REST session from <identity> with User <user_name> is rejected because
|          | maximum session | limit | is reached |
| -------- | --------------- | ----- | ---------- |
| Category | REST            |       |            |
| Severity | Warning         |       |            |
Description Logsamessagewhenausertriestologinwhilemaximumnumberofsessionsare
reached
EventID:4659
Message REST session from <identity> with User <user_name> timed out due to
idle timeout
| Category | REST        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogsamessagewhenaRESTsessiontimedoutduetothesessionbeingidle
EventID:4660
| Message     | REST server                                  | is enabled | on VRF <vrf_name> |
| ----------- | -------------------------------------------- | ---------- | ----------------- |
| Category    | REST                                         |            |                   |
| Severity    | Information                                  |            |                   |
| Description | LogsamessagewhentheRESTserverisenabledonaVRF |            |                   |
EventID:4661
| Message     | REST server                                   | is disabled | on VRF <vrf_name> |
| ----------- | --------------------------------------------- | ----------- | ----------------- |
| Category    | REST                                          |             |                   |
| Severity    | Information                                   |             |                   |
| Description | LogsamessagewhentheRESTserverisdisabledonaVRF |             |                   |
RESTevents|260

Chapter 100
Self Test events
Self Test events
Thefollowingaretheeventsrelatedtoselftest.
EventID:4501
| Message     | Selftest has                                 | started | on subsystem | <subsystem> |
| ----------- | -------------------------------------------- | ------- | ------------ | ----------- |
| Category    | SelfTest                                     |         |              |             |
| Severity    | Information                                  |         |              |             |
| Description | logsthestartofselftestonaparticularsubsystem |         |              |             |
EventID:4502
| Message     | Selftest has                                      | completed | on subsystem | <subsystem> |
| ----------- | ------------------------------------------------- | --------- | ------------ | ----------- |
| Category    | SelfTest                                          |           |              |             |
| Severity    | Information                                       |           |              |             |
| Description | logsthecompletionofselftestonaparticularsubsystem |           |              |             |
EventID:4503
Message Selftest has failed on subsystem <subsystem> with error code <value>':
yes
| Category    | SelfTest                                     |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- |
| Severity    | Error                                        |     |     |     |
| Description | logstheselftestfailureofaparticularsubsystem |     |     |     |
EventID:4504
Message Selftest has failed on <stack>/<slot>/<interface> with error code
|             | <value>':                                   | yes |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | SelfTest                                    |     |     |     |
| Severity    | Error                                       |     |     |     |
| Description | logstheportselftestfailureonagivensubsystem |     |     |     |
261
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 101
sFlow events
sFlow events
ThefollowingaretheeventsrelatedtosFlow.
EventID:1001
| Message  | Failed | to <operation> | host sFlow | agent: <error> |
| -------- | ------ | -------------- | ---------- | -------------- |
| Category | sFlow  |                |            |                |
| Severity | Error  |                |            |                |
Description Logafailurewhentryingtostart/stop/restarthostsFlowdaemon.
EventID:1002
Message Failed to <operation> host sFlow configuration file <file>: <error>
| Category | sFlow |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description Logafailurewhentryingtoread/writetohostsFlowconfigurationfile.
EventID:1003
Message Failed to <operation> sFlow configuration from bridge <bridge>: <error>
| Category    | sFlow                                          |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Error                                          |     |     |     |
| Description | LogafailurewhentryingtoconfiguresFlowonSIMOVS. |     |     |     |
EventID:1004
| Message  | Failed | to delete all | iptable rules: | <error> |
| -------- | ------ | ------------- | -------------- | ------- |
| Category | sFlow  |               |                |         |
| Severity | Error  |               |                |         |
Description LogafailurewhentryingtodeletealliptablerulesaddedforsFlow.
EventID:1005
262
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message Failed to <operation> <chain> iptable rules for <port>: <error>
| Category | sFlow |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
| Severity | Error |     |     |     |     |
Description Logafailurewhentryingtoadd/deleteaniptableruleforsFlow.
EventID:1006
| Message     | sFlow initialization                   |     | failed. |     |     |
| ----------- | -------------------------------------- | --- | ------- | --- | --- |
| Category    | sFlow                                  |     |         |     |     |
| Severity    | Error                                  |     |         |     |     |
| Description | LogsanerrorifsFlowinitializationfails. |     |         |     |     |
EventID:1007
| Message     | Invalid                                       | packet sent | by ASIC in | sFlow callback. |     |
| ----------- | --------------------------------------------- | ----------- | ---------- | --------------- | --- |
| Category    | sFlow                                         |             |            |                 |     |
| Severity    | Error                                         |             |            |                 |     |
| Description | LogsanerrorforaninvalidpacketinsFlowcallback. |             |            |                 |     |
EventID:1008
| Message     | Unable                                           | to get netdev | for interface | <interface> |     |
| ----------- | ------------------------------------------------ | ------------- | ------------- | ----------- | --- |
| Category    | sFlow                                            |               |               |             |     |
| Severity    | Error                                            |               |               |             |     |
| Description | Logsanerrorifaninterfacedoesnothaveanetdevclass. |               |               |             |     |
EventID:1009
| Message     | Failed                                            | to create KNET | filter | as description | is blank |
| ----------- | ------------------------------------------------- | -------------- | ------ | -------------- | -------- |
| Category    | sFlow                                             |                |        |                |          |
| Severity    | Error                                             |                |        |                |          |
| Description | Logsanerrorifthedescrptiontocreateafilterisblank. |                |        |                |          |
EventID:1010
| Message | Failed | to create KNET | filter | for: <desc> |     |
| ------- | ------ | -------------- | ------ | ----------- | --- |
sFlowevents|263

| Category    | sFlow                                      |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Error                                      |     |     |     |
| Description | LogsanerrorifsFlowKNETfiltercreationfails. |     |     |     |
EventID:1011
| Message     | The received                      | sampled | packet | is null |
| ----------- | --------------------------------- | ------- | ------ | ------- |
| Category    | sFlow                             |         |        |         |
| Severity    | Error                             |         |        |         |
| Description | Logsanerrorifsampledpacketisnull. |         |        |         |
EventID:1012
| Message     | The sFlow                                | agent is | not initialized |     |
| ----------- | ---------------------------------------- | -------- | --------------- | --- |
| Category    | sFlow                                    |          |                 |     |
| Severity    | Error                                    |          |                 |     |
| Description | LogsanerrorifsFlowagentisnotinitialized. |          |                 |     |
EventID:1013
| Message     | The sFlow                                  | sampler | is not initialized |     |
| ----------- | ------------------------------------------ | ------- | ------------------ | --- |
| Category    | sFlow                                      |         |                    |     |
| Severity    | Error                                      |         |                    |     |
| Description | LogsanerrorifsFlowsamplerisnotinitialized. |         |                    |     |
EventID:1014
Message Cannot enable/disable sFlow on an invalid port: <port>
| Category | sFlow |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description LogsanerrorifsFlowisenabled/disabledonaninvalidport.
EventID:1015
| Message  | sFlow sampler | is not | available | on port: <port> |
| -------- | ------------- | ------ | --------- | --------------- |
| Category | sFlow         |        |           |                 |
264
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Error                                      |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Description | LogsanerrorifsFlowsamplerismissingonaport. |     |     |     |
EventID:1016
| Message     | sFlow receiver                            | is not | available |     |
| ----------- | ----------------------------------------- | ------ | --------- | --- |
| Category    | sFlow                                     |        |           |     |
| Severity    | Error                                     |        |           |     |
| Description | LogsanerrorifsFlowreceiverisnotavailable. |        |           |     |
EventID:1017
| Message     | Failed                                        | to retrieve port | configuration: | <error> |
| ----------- | --------------------------------------------- | ---------------- | -------------- | ------- |
| Category    | sFlow                                         |                  |                |         |
| Severity    | Error                                         |                  |                |         |
| Description | Logsanerrorifportconfigurationisnotavailable. |                  |                |         |
EventID:1018
| Message     | Failed                                         | to set sampling | rate on port | <port>: <error> |
| ----------- | ---------------------------------------------- | --------------- | ------------ | --------------- |
| Category    | sFlow                                          |                 |              |                 |
| Severity    | Error                                          |                 |              |                 |
| Description | Logsanerrorifsettingasamplingrateonaportfails. |                 |              |                 |
EventID:1019
| Message  | Failed | to get sampling | rate on port | <port>: <error> |
| -------- | ------ | --------------- | ------------ | --------------- |
| Category | sFlow  |                 |              |                 |
| Severity | Error  |                 |              |                 |
Description Logsanerrorifunabletoretrievesamplingrateonaport.
EventID:1020
| Message  | Invalid | agent interface | IP address: | <ip_address> |
| -------- | ------- | --------------- | ----------- | ------------ |
| Category | sFlow   |                 |             |              |
| Severity | Error   |                 |             |              |
Description LogsanerrorincaseofinvalidagentinterfaceIPaddressconfiguration.
sFlowevents|265

EventID:1021
| Message  | Invalid collector | IP address: | <ip_address> |
| -------- | ----------------- | ----------- | ------------ |
| Category | sFlow             |             |              |
| Severity | Error             |             |              |
Description LogsanerrorincaseofinvalidcollectorIPaddressconfiguration.
EventID:1022
Message Failed to get interface statistics for unit <unit> port <port>: <error>
| Category    | sFlow                                             |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Error                                             |     |     |
| Description | Logsanerrorifunabletoretrieveinterfacestatistics. |     |     |
EventID:1023
| Message     | sFlow agent               | created. |     |
| ----------- | ------------------------- | -------- | --- |
| Category    | sFlow                     |          |     |
| Severity    | Information               |          |     |
| Description | LogscreationofsFlowagent. |          |     |
EventID:1024
| Message     | sFlow agent               | deleted. |     |
| ----------- | ------------------------- | -------- | --- |
| Category    | sFlow                     |          |     |
| Severity    | Information               |          |     |
| Description | LogsdeletionofsFlowagent. |          |     |
EventID:1025
Message Changed sFlow sampling rate from <old_rate> to <new_rate>.
| Category    | sFlow                           |     |     |
| ----------- | ------------------------------- | --- | --- |
| Severity    | Information                     |     |     |
| Description | LogsachangeinsFlowsamplingrate. |     |     |
EventID:1026
266
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Message     | Set sFlow                         | agents | header len | to <hdrlen>. |
| ----------- | --------------------------------- | ------ | ---------- | ------------ |
| Category    | sFlow                             |        |            |              |
| Severity    | Information                       |        |            |              |
| Description | LogssFlowagentsheaderlengthevent. |        |            |              |
EventID:1027
| Message     | Set sFlow                         | agents | IP to <ip_addr>. |     |
| ----------- | --------------------------------- | ------ | ---------------- | --- |
| Category    | sFlow                             |        |                  |     |
| Severity    | Information                       |        |                  |     |
| Description | LogssettingIPaddresstosFlowagent. |        |                  |     |
EventID:1028
| Message     | Set max                                | datagram | size on sFlow | agent to <dgramsize>. |
| ----------- | -------------------------------------- | -------- | ------------- | --------------------- |
| Category    | sFlow                                  |          |               |                       |
| Severity    | Information                            |          |               |                       |
| Description | LogsettingmaxdatagramsizeonsFlowagent. |          |               |                       |
EventID:1029
Message Add sFlow poller on <port_name> with ifIndex <ifIndex> at interval
<intvl>.
| Category    | sFlow                  |     |     |     |
| ----------- | ---------------------- | --- | --- | --- |
| Severity    | Information            |     |     |     |
| Description | AddsFlowpolleronaport. |     |     |     |
EventID:1030
| Message     | Remove                    | sFlow poller | on <ifIndex>. |     |
| ----------- | ------------------------- | ------------ | ------------- | --- |
| Category    | sFlow                     |              |               |     |
| Severity    | Information               |              |               |     |
| Description | DeletesFlowpolleronaport. |              |               |     |
EventID:1031
sFlowevents|267

| Message     | Set polling                      | interval | of <intvl> | on sFlow agent. |
| ----------- | -------------------------------- | -------- | ---------- | --------------- |
| Category    | sFlow                            |          |            |                 |
| Severity    | Information                      |          |            |                 |
| Description | SetpollingintervalforsFlowagent. |          |            |                 |
EventID:1032
| Message     | sFlow sampling         | mode set | to <mode>. |     |
| ----------- | ---------------------- | -------- | ---------- | --- |
| Category    | sFlow                  |          |            |     |
| Severity    | Information            |          |            |     |
| Description | LogschangeinsFlowmode. |          |            |     |
268
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 102
SFTP Client events
| SFTP Client events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoSFTPclient.
EventID:5301
| Message     | SFTP file                 | transfer from | <from> | to <to> completed. |
| ----------- | ------------------------- | ------------- | ------ | ------------------ |
| Category    | SFTPClient                |               |        |                    |
| Severity    | Information               |               |        |                    |
| Description | SFTPfiletransfercompleted |               |        |                    |
EventID:5302
Message SFTP file transfer from <from> to <to> failed - <status>.
| Category    | SFTPClient             |     |     |     |
| ----------- | ---------------------- | --- | --- | --- |
| Severity    | Information            |     |     |     |
| Description | SFTPfiletransferfailed |     |     |     |
269
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 103

Smartlink events

Smartlink events

The following are the events related to smartlink.

Event ID: 11301

Message

Flush message received on <ifName> with control VLAN <id>

Category

Smartlink

Severity

Information

Description

Event raised when flush message received on interface with control vlan

Event ID: 11302

Message

Active link of the smartlink group <id> changed to <ifName>

Category

Smartlink

Severity

Information

Description

Event raised when active link changed in the smartlink group

Event ID: 11303

Message

Backup link of the smartlink group <id> changed to <ifName>

Category

Smartlink

Severity

Information

Description

Event raised when backup link changed in the smartlink group

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

270

Chapter 104
SNMP events
SNMP events
ThefollowingaretheeventsrelatedtoSNMP.
EventID:7101
| Message     | Snmp agent          | is up and | running | in namespace |     | <vrf> |
| ----------- | ------------------- | --------- | ------- | ------------ | --- | ----- |
| Category    | SNMP                |           |         |              |     |       |
| Severity    | Information         |           |         |              |     |       |
| Description | SNMPagentisenabled. |           |         |              |     |       |
EventID:7102
| Message     | Snmp sub               | agent is | up and | running | in namespace | <vrf> |
| ----------- | ---------------------- | -------- | ------ | ------- | ------------ | ----- |
| Category    | SNMP                   |          |        |         |              |       |
| Severity    | Information            |          |        |         |              |       |
| Description | SNMPsubagentisenabled. |          |        |         |              |       |
EventID:7103
| Message     | Snmp agent           | is disabled | for | namespace | <vrf> |     |
| ----------- | -------------------- | ----------- | --- | --------- | ----- | --- |
| Category    | SNMP                 |             |     |           |       |     |
| Severity    | Information          |             |     |           |       |     |
| Description | SNMPagentisdisabled. |             |     |           |       |     |
EventID:7104
| Message     | Snmp sub                | agent is | disabled | for namespace |     | <vrf> |
| ----------- | ----------------------- | -------- | -------- | ------------- | --- | ----- |
| Category    | SNMP                    |          |          |               |     |       |
| Severity    | Information             |          |          |               |     |       |
| Description | SNMPsubagentisdisabled. |          |          |               |     |       |
EventID:7105
271
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Failed                        | to poll snmp |     |     |     |
| ----------- | ----------------------------- | ------------ | --- | --- | --- |
| Category    | SNMP                          |              |     |     |     |
| Severity    | Information                   |              |     |     |     |
| Description | SNMPpollthreadcreationfailed. |              |     |     |     |
EventID:7106
| Message     | Snmp and                                     | credential | manager | integration | failed |
| ----------- | -------------------------------------------- | ---------- | ------- | ----------- | ------ |
| Category    | SNMP                                         |            |         |             |        |
| Severity    | Information                                  |            |         |             |        |
| Description | SNMPfailedtosynchronizewithcredentialmanager |            |         |             |        |
EventID:7107
| Message     | Snmp system             | now configured |     |     |     |
| ----------- | ----------------------- | -------------- | --- | --- | --- |
| Category    | SNMP                    |                |     |     |     |
| Severity    | Information             |                |     |     |     |
| Description | SNMPsystemisconfigured. |                |     |     |     |
EventID:7108
| Message     | Snmp and                                 | database | Integration | has been | initialized |
| ----------- | ---------------------------------------- | -------- | ----------- | -------- | ----------- |
| Category    | SNMP                                     |          |             |          |             |
| Severity    | Information                              |          |             |          |             |
| Description | Snmpsuccessfullysynchronizedwithdatabase |          |             |          |             |
EventID:7109
| Message     | Successfully                        | initialized | all | SNMP plugins |     |
| ----------- | ----------------------------------- | ----------- | --- | ------------ | --- |
| Category    | SNMP                                |             |     |              |     |
| Severity    | Information                         |             |     |              |     |
| Description | SNMPpluginssuccessfullyinitialized. |             |     |              |     |
EventID:7110
| Message | Destroyed | all SNMP | plugins |     |     |
| ------- | --------- | -------- | ------- | --- | --- |
SNMPevents|272

| Category    | SNMP                                 |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | SNMPpluginsuccessfullydeinitialized. |     |     |     |
EventID:7111
| Message     | SNMP cache           | sync on-demand | is set to: | <truth_value> |
| ----------- | -------------------- | -------------- | ---------- | ------------- |
| Category    | SNMP                 |                |            |               |
| Severity    | Information          |                |            |               |
| Description | SNMPondemandidlsync. |                |            |               |
273
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 105

SSH client events

SSH client events

The following are the events related to SSH client.

Event ID: 9001

Message

Connection to SSH server <ipaddr> on VRF <vrf_name> is established for
user <username> over port <port_num>

Category

SSH client

Severity

Information

Description

SSH client session is successful.

Event ID: 9002

Message

Connection to SSH server <ipaddr> on VRF <vrf_name> over port <port_
num> is denied

Category

SSH client

Severity

Error

Description

SSH client session is denied

Event ID: 9003

Message

Connection to SSH server <ipaddr> on VRF <vrf_name> is succesfully
closed for user <username> over port <port_num>

Category

SSH client

Severity

Information

Description

SSH client session is successful.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

274

Chapter 106
SSH server events
| SSH server events |     |     |     |
| ----------------- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoSSHserver.
EventID:5201
| Message     | SSH host-key                            | <key_name> | is installed. |
| ----------- | --------------------------------------- | ---------- | ------------- |
| Category    | SSHserver                               |            |               |
| Severity    | Information                             |            |               |
| Description | LogsamessagewhentheSSHhost-keygenerated |            |               |
EventID:5202
| Message     | SSH server                                  | is enabled | on VRF <vrf_name>. |
| ----------- | ------------------------------------------- | ---------- | ------------------ |
| Category    | SSHserver                                   |            |                    |
| Severity    | Information                                 |            |                    |
| Description | LogsamessagewhentheSSHserverisenabledonaVRF |            |                    |
EventID:5203
| Message     | SSH server                                   | is disabled | on VRF <vrf_name>. |
| ----------- | -------------------------------------------- | ----------- | ------------------ |
| Category    | SSHserver                                    |             |                    |
| Severity    | Information                                  |             |                    |
| Description | LogsamessagewhentheSSHserverisdisabledonaVRF |             |                    |
EventID:5204
Message SSH client-public-key <key_name> was installed for the user <username>.
| Category | SSHserver   |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logsamessagewhenaddsshclient-public-keyintoauthorized_keysfile
EventID:5205
275
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

SSH client-public-key <key_name> was removed for the user <username>.

Category

SSH server

Severity

Information

Description

Logs a message when delete ssh client-public-key into authorized_keys file

Event ID: 5207

Message

An internal error occurred while reading the SSH host-key <key_name>.

Category

SSH server

Severity

Information

Description

Logs a message when the SSH host-key is corrupted

Event ID: 5208

Message

Failed to enable SSH server on VRF <vrf_name>. Admin password is not
set.

Category

SSH server

Severity

Error

Description

Logs a message when a user tries to enable SSH server without setting admin password

Event ID: 5209

Message

User <user_name> logged in from <ip_address> through SSH session.

Category

SSH server

Severity

Information

Description

Logs a message when a user login is successful

Event ID: 5210

Message

User <user_name> login from <ip_address> for SSH session has failed.

Category

SSH server

Severity

Error

Description

Logs a message when a user login fails

Event ID: 5211

SSH server events | 276

Message

User <user_name> logged out of SSH session from <ip_address>.

Category

SSH server

Severity

Information

Description

Logs a message when a user logs out of a session

Event ID: 5212 (Severity: Warning)

Message

SSH session from <ip_address> is rejected because maximum number of SSH
sessions is reached.

Category

SSH server

Severity

Warning

Description

Logs a message when a user tries to login while maximum number of sessions are
reached.

Event ID: 5213 (Severity: Warning)

Message

SSH session from User <user_name> is closed because maximum number of
sessions per user is reached.

Category

SSH server

Severity

Warning

Description

Logs a message when a user session is closed while maximum number of sessions per
user are reached.

Event ID: 5214 (Severity: Warning)

Message

SSH session from <ip_address> is closed because of host key failure.

Category

SSH server

Severity

Warning

Description

Logs a message when a user session is closed due to host key failure.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

277

Chapter 107
Supportability events
| Supportability | events |     |     |
| -------------- | ------ | --- | --- |
Thefollowingaretheeventsrelatedtosupportability.
EventID:1201(Severity:Critical)
| Message     | <process>                             | crashed due | to <signal>,<timestamp> |
| ----------- | ------------------------------------- | ----------- | ----------------------- |
| Category    | Supportability                        |             |                         |
| Severity    | Critical                              |             |                         |
| Description | Adaemonhascrashedandgeneratedcoredump |             |                         |
EventID:1202
| Message     | Kernel          | panic occurred |     |
| ----------- | --------------- | -------------- | --- |
| Category    | Supportability  |                |     |
| Severity    | Error           |                |     |
| Description | Logskernelcrash |                |     |
EventID:1203
Message Kernel failed to compress vmcore. Error log:<err_desc>
| Category    | Supportability                   |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Error                            |     |     |
| Description | Logskernelfailedtocompressvmcore |     |     |
EventID:1204
Message Kernel panic occurred and secondary kernel failed to save uncompressed
|          | core. Error    | log:<err_desc> |     |
| -------- | -------------- | -------------- | --- |
| Category | Supportability |                |     |
| Severity | Error          |                |     |
Description Logskernelpanicoccurredandsecondarykernelcorefailedtosaveuncompressedcore
EventID:1205
278
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message Kernel panic occurred and system is restored back to normal state
| Category    | Supportability          |     |     |     |
| ----------- | ----------------------- | --- | --- | --- |
| Severity    | Error                   |     |     |     |
| Description | Logskernelpanicoccurred |     |     |     |
EventID:1206(Severity:Critical)
Message Module rebooted. Reason: <reason>, Boot-ID: <boot_id>
| Category    | Supportability        |     |     |     |
| ----------- | --------------------- | --- | --- | --- |
| Severity    | Critical              |     |     |     |
| Description | Logsrebootinformation |     |     |     |
EventID:1207(Severity:Warning)
| Message  | Available      | system memory | is back | to normal state |
| -------- | -------------- | ------------- | ------- | --------------- |
| Category | Supportability |               |         |                 |
| Severity | Warning        |               |         |                 |
Description Eventraisedwhenavailablesystemmemoryisrestoredtonormallevel.
EventID:1208
Message High system memory usage detected. High memory usage daemons are
<daemons>
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Error          |     |     |     |
Description Eventraisedwhensystemmemoryusagegoesbeyondhighthreshold.
EventID:1209(Severity:Emergency)
| Message  | Available      | system memory | is critically | low': yes |
| -------- | -------------- | ------------- | ------------- | --------- |
| Category | Supportability |               |               |           |
| Severity | Emergency      |               |               |           |
Description Eventraisedwhensystemmemoryusagecrossescriticalthreshold.
EventID:1210(Severity:Warning)
Supportabilityevents|279

| Message  | Memory         | reservation | for reboot library | failed |
| -------- | -------------- | ----------- | ------------------ | ------ |
| Category | Supportability |             |                    |        |
| Severity | Warning        |             |                    |        |
Description Eventraisedwhenmemoryreservationforrebootlibraryfails.
EventID:1211(Severity:Emergency)
| Message     | Unable                                    | to get current | system memory | usage |
| ----------- | ----------------------------------------- | -------------- | ------------- | ----- |
| Category    | Supportability                            |                |               |       |
| Severity    | Emergency                                 |                |               |       |
| Description | Eventraisedwhensystemmemoryreadisfailing. |                |               |       |
EventID:1212(Severity:Emergency)
Message Available system memory is critically low. Reboot will be triggered
soon.
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Emergency      |     |     |     |
Description Availablememoryiscriticallylow,systemwillberebooted.
EventID:1213
Message RMON alarm <index> - Rising threshold value of <threshold> reached for
<oid>.
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Information    |     |     |     |
Description Eventraisedwhenthesampledvaluehasreachedtherisingthreshold.
EventID:1214
Message RMON alarm <index> - Falling threshold value of <threshold> reached for
<oid>.
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Information    |     |     |     |
Description Eventraisedwhenthesampledvaluehasreachedthefallingthreshold.
EventID:1215
280
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Message     | <process>                                  | exiting. Reason: | <reason> |
| ----------- | ------------------------------------------ | ---------------- | -------- |
| Category    | Supportability                             |                  |          |
| Severity    | Error                                      |                  |          |
| Description | Aprocessisexitingduetoanunrecoverableerror |                  |          |
EventID:1216(Severity:Emergency)
| Message     | <process>                                          | exiting. Reason: | <reason> |
| ----------- | -------------------------------------------------- | ---------------- | -------- |
| Category    | Supportability                                     |                  |          |
| Severity    | Emergency                                          |                  |          |
| Description | Acriticalprocessisexitingduetoanunrecoverableerror |                  |          |
EventID:1217
| Message     | Coredump(s)                 | are deleted | by user |
| ----------- | --------------------------- | ----------- | ------- |
| Category    | Supportability              |             |         |
| Severity    | Information                 |             |         |
| Description | Coredump(s)aredeletedbyuser |             |         |
EventID:1218
Message Remote logging to <remote_host> over <vrf> vrf added.
| Category | Supportability |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Eventraisedwhenanewsyslogserverisaddedforremotelogging.
EventID:1219
Message Remote logging to <remote_host> over <vrf> vrf removed.
| Category | Supportability |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Eventraisedwhenasyslogserverisremovedfromremotelogging.
EventID:1220
Message Configuration of remote logging to <remote_host> over <vrf> vrf
modified.
Supportabilityevents|281

| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Information    |     |     |     |
Description Eventraisedwhenanexistingsyslogserverconfigurationismodified.
EventID:1221
Message Watchdog timeout is increased due to high memory usage
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Information    |     |     |     |
Description EventraisedwhenavailableRAMmemorygoesbelowthethresholdandwatchdog
timeoutisincreased.
EventID:1222
| Message  | Watchdog timeout | is restored | to default | value |
| -------- | ---------------- | ----------- | ---------- | ----- |
| Category | Supportability   |             |            |       |
| Severity | Information      |             |            |       |
Description EventraisedwhentheavailableRAMmemoryisrestoredtonormalrangeandthe
watchdogtimeoutisrestoredtodefaultvalue.
EventID:1223(Severity:Warning)
| Message  | The <log_type> | buffer | is almost full.': | yes |
| -------- | -------------- | ------ | ----------------- | --- |
| Category | Supportability |        |                   |     |
| Severity | Warning        |        |                   |     |
Description Eventraisedthelogbufferisalmostfull.Usercancopytheselogsbeforethelogsbeing
overwritten.
EventID:1224(Severity:Warning)
Message The <log_type> buffer has wrapped, older logs will be overwritten.':
yes
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Warning        |     |     |     |
Description Eventraisedthelogbufferhaswrapped;olderlogswillbeoverwritten.
EventID:1225
282
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message Collection of support-files named <name> of type <type> is requested
|             | for the module                                      | <module>. |     |
| ----------- | --------------------------------------------------- | --------- | --- |
| Category    | Supportability                                      |           |     |
| Severity    | Information                                         |           |     |
| Description | Eventraisedwhensuppuort-filescollectionisrequested. |           |     |
EventID:1226
Message Support-files named <name> is requested for deletion.
| Category | Supportability |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Eventraisedwhenarequstrecivedtodeletegivensupport-files.
EventID:1227
| Message     | Support-files                           | named <name> | is deleted. |
| ----------- | --------------------------------------- | ------------ | ----------- |
| Category    | Supportability                          |              |             |
| Severity    | Information                             |              |             |
| Description | Eventraisedwhensuppuort-filesisdeleted. |              |             |
EventID:1228
Message Collection of support-files named <name> failed due to <reason>.
| Category    | Supportability                                |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Error                                         |     |     |
| Description | Eventraisedwhencollectionsupport-filesfailed. |     |     |
EventID:1229
Message Deletion of support-files named <name> failed due to <reason>.
| Category    | Supportability                                    |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Error                                             |     |     |
| Description | Eventraisedwhenfailedtodeleteagivensupport-files. |     |     |
EventID:1230
Supportabilityevents|283

| Message  | Collection     | of support-files | named <name> | is <state>. |
| -------- | -------------- | ---------------- | ------------ | ----------- |
| Category | Supportability |                  |              |             |
| Severity | Information    |                  |              |             |
Description Eventraisedwhencollectionofsupport-filesstatechanges.
EventID:1231
| Message  | Syslog client  | restarted | due to configuration | change. |
| -------- | -------------- | --------- | -------------------- | ------- |
| Category | Supportability |           |                      |         |
| Severity | Information    |           |                      |         |
Description Eventraisedwhenremotesyslogisrestartedduetoconfigurationchange.
EventID:1232
| Message     | The security                               | log buffer | is cleared |     |
| ----------- | ------------------------------------------ | ---------- | ---------- | --- |
| Category    | Supportability                             |            |            |     |
| Severity    | Information                                |            |            |     |
| Description | Eventraisedasthesecuritylogbufferiscleared |            |            |     |
284
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Chapter 108
SYS events
SYS events
ThefollowingaretheeventsrelatedtoSYS.
EventID:701
| Message     | Failed                                   | to read FRU | data from base | system |
| ----------- | ---------------------------------------- | ----------- | -------------- | ------ |
| Category    | SYS                                      |             |                |        |
| Severity    | Information                              |             |                |        |
| Description | LogwhenfailedtoreadFRUdatafrombasesystem |             |                |        |
EventID:702
| Message     | Failed                       | to read FRU | header |     |
| ----------- | ---------------------------- | ----------- | ------ | --- |
| Category    | SYS                          |             |        |     |
| Severity    | Information                  |             |        |     |
| Description | LogwhenfailedtoreadFRUheader |             |        |     |
EventID:703
| Message     | Error reading                | FRU | EEPROM Header |     |
| ----------- | ---------------------------- | --- | ------------- | --- |
| Category    | SYS                          |     |               |     |
| Severity    | Information                  |     |               |     |
| Description | logwhenFRUEEPROMHeaderfailed |     |               |     |
EventID:704
| Message     | Failed                          | to intialize | devices |     |
| ----------- | ------------------------------- | ------------ | ------- | --- |
| Category    | SYS                             |              |         |     |
| Severity    | Information                     |              |         |     |
| Description | Logwhenfailedtointializedevices |              |         |     |
EventID:705
285
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Failed                        | to allocate memory | for <value> |
| ----------- | ----------------------------- | ------------------ | ----------- |
| Category    | SYS                           |                    |             |
| Severity    | Information                   |                    |             |
| Description | Logwhenfailedtoallocatememory |                    |             |
EventID:706
| Message     | Initiating                              | system reboot |     |
| ----------- | --------------------------------------- | ------------- | --- |
| Category    | SYS                                     |               |     |
| Severity    | Information                             |               |     |
| Description | Indicatesthatthechassisisabouttoreboot. |               |     |
EventID:707
| Message  | Initiating | chassis thermal | reboot |
| -------- | ---------- | --------------- | ------ |
| Category | SYS        |                 |        |
| Severity | Error      |                 |        |
Description Indicatesthatthechassisexperiencedathermaleventandwillreboot
EventID:708
Message Invalid Device Version Programmed. Please check MFG data programmed on
the device.
| Category | SYS   |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description Indicatesinvaliddeviceversionisprogrammedonthedevice
EventID:709
| Message  | Failed | to read assembly | revision |
| -------- | ------ | ---------------- | -------- |
| Category | SYS    |                  |          |
| Severity | Error  |                  |          |
Description Indicatesdevicehasfailedtoreadassemblyrevisionthatisprogrammed
SYSevents|286

Chapter 109

SYSMON events

SYSMON events

The following are the events related to SYSMON.

Event ID: 6301

Message

System resource utilization poll interval is changed to <poll>'
throttle_count: 40

Category

SYSMON

Severity

Information

Description

System resource utilization poll change event

Event ID: 6302 (Severity: Warning)

Message

Failed to read system memory usage for module <module_num>

Category

SYSMON

Severity

Warning

Description

Warns a user when system memory usage read failed

Event ID: 6303

Message

Current system memory usage for module <module_num> is <mem_usage>%

Category

SYSMON

Severity

Information

Description

Reports current system memory usage in percentage

Event ID: 6304 (Severity: Warning)

Message

Storage utilization for <partition_name> partition is at <utilization>%
in module <module_name>': yes

Category

SYSMON

Severity

Warning

Description

Warns a user when the storage utilization has exceeded the warning limit.

Event ID: 6305

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

287

Message

Storage <partition_name> partition high utilization alert. Utilization
is at <utilization>% in module <module_name>': yes

Category

SYSMON

Severity

Error

Description

Raises high storage utilization alert when the utilization crosses higher utilization limit.

Event ID: 6306 (Severity: Warning)

Message

Excessive write to <partition_name> partition in module <module_name>
observed. <mem_usage>GB written over past <unit_count> <unit>': yes

Category

SYSMON

Severity

Warning

Description

Warns a user when higher write to the storage observed

Event ID: 6307 (Severity: Warning)

Message

Excessive write to swap in module <module_name> observed. <mem_usage>GB
written over past <unit_count> <unit>': yes

Category

SYSMON

Severity

Warning

Description

Warns a user when higher write to the swap observed.

Event ID: 6308

Message

Excessive write to <partition_name> partition in module <module_name>
observed. <mem_usage>GB written over past <unit_count> <unit>': yes

Category

SYSMON

Severity

Error

Description

Warns a user when excessive write to the storage observed

Event ID: 6309

Message

Excessive write to swap in module <module_name> observed. <mem_usage>GB
written over past <unit_count> <unit>': yes

Category

SYSMON

Severity

Error

Description

Warns a user when excessive write to the swap observed.

SYSMON events | 288

Chapter 110
TCAM events
TCAM events
ThefollowingaretheeventsrelatedtoTCAM.
EventID:10201
| Message     | "Policer installation      | has | failed" |     |
| ----------- | -------------------------- | --- | ------- | --- |
| Category    | TCAM                       |     |         |     |
| Severity    | Error                      |     |         |     |
| Description | Policerinstallationfailure |     |         |     |
EventID:10202
Message "TCAM entry installation has failed in table <table_name>"
| Category    | TCAM                         |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Error                        |     |     |     |
| Description | TCAMentryinstallationfailure |     |     |     |
EventID:10203
| Message     | "Installation                | of TCAM table | <table_name> | has failed" |
| ----------- | ---------------------------- | ------------- | ------------ | ----------- |
| Category    | TCAM                         |               |              |             |
| Severity    | Error                        |               |              |             |
| Description | TCAMtableinstallationfailure |               |              |             |
EventID:10204
Message "High-capacity TCAM/LPM entry installation failed in table <table_
name>"
| Category    | TCAM                                          |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Error                                         |     |     |     |
| Description | High-capacityTCAM/LPMentryinstallationfailure |     |     |     |
EventID:10205
289
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message "High-capacity TCAM/LPM table <table_name> installation failed"
| Category    | TCAM                                          |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Error                                         |     |     |
| Description | High-capacityTCAM/LPMtableinstallationfailure |     |     |
EventID:10206
| Message     | "Counter installation          | has | failed" |
| ----------- | ------------------------------ | --- | ------- |
| Category    | TCAM                           |     |         |
| Severity    | Error                          |     |         |
| Description | TCAMCounterinstallationfailure |     |         |
EventID:10207
| Message     | "Range Checker                      | installation | has failed" |
| ----------- | ----------------------------------- | ------------ | ----------- |
| Category    | TCAM                                |              |             |
| Severity    | Error                               |              |             |
| Description | TCAMRangeCheckerinstallationfailure |              |             |
EventID:10208
| Message     | "Policer uninstallation      | has | failed" |
| ----------- | ---------------------------- | --- | ------- |
| Category    | TCAM                         |     |         |
| Severity    | Error                        |     |         |
| Description | Policeruninstallationfailure |     |         |
EventID:10209
Message "TCAM entry uninstallation has failed in table <table_name>"
| Category    | TCAM                           |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Error                          |     |     |
| Description | TCAMentryuninstallationfailure |     |     |
EventID:10210
Message "High-capacity TCAM/LPM entry uninstallation failed in table <table_
name>"
TCAMevents|290

| Category    | TCAM                                            |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- |
| Severity    | Error                                           |     |     |     |     |
| Description | High-capacityTCAM/LPMentryuninstallationfailure |     |     |     |     |
EventID:10211
| Message     | "High-capacity                                  | TCAM/LPM | table uninstallation |     | failed" |
| ----------- | ----------------------------------------------- | -------- | -------------------- | --- | ------- |
| Category    | TCAM                                            |          |                      |     |         |
| Severity    | Error                                           |          |                      |     |         |
| Description | High-capacityTCAM/LPMtableuninstallationfailure |          |                      |     |         |
EventID:10212
| Message     | "Counter uninstallation          |     | has failed" |     |     |
| ----------- | -------------------------------- | --- | ----------- | --- | --- |
| Category    | TCAM                             |     |             |     |     |
| Severity    | Error                            |     |             |     |     |
| Description | TCAMCounteruninstallationfailure |     |             |     |     |
EventID:10213
| Message     | "Range Checker                        | uninstallation | has | failed" |     |
| ----------- | ------------------------------------- | -------------- | --- | ------- | --- |
| Category    | TCAM                                  |                |     |         |     |
| Severity    | Error                                 |                |     |         |     |
| Description | TCAMRangeCheckeruninstallationfailure |                |     |         |     |
EventID:10214
| Message     | "TCAM Context                              | Group selectors | have | been exhausted" |     |
| ----------- | ------------------------------------------ | --------------- | ---- | --------------- | --- |
| Category    | TCAM                                       |                 |      |                 |     |
| Severity    | Error                                      |                 |      |                 |     |
| Description | TCAMContextGroupselectorshavebeenexhausted |                 |      |                 |     |
EventID:10215
| Message  | "TCAM Context | Group IDs | have been | exhausted" |     |
| -------- | ------------- | --------- | --------- | ---------- | --- |
| Category | TCAM          |           |           |            |     |
291
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Severity

Error

Description

TCAM Context Group IDs have been exhausted

TCAM events | 292

|                      |     |     |     |        | Chapter | 111    |
| -------------------- | --- | --- | --- | ------ | ------- | ------ |
|                      |     |     |     | Telnet | server  | events |
| Telnet server events |     |     |     |        |         |        |
Thefollowingaretheeventsrelatedtotelnetserver.
EventID:12901
| Message     | TELNET server                                  | is enabled | on VRF <vrf_name>. |     |     |     |
| ----------- | ---------------------------------------------- | ---------- | ------------------ | --- | --- | --- |
| Category    | Telnetserver                                   |            |                    |     |     |     |
| Severity    | Information                                    |            |                    |     |     |     |
| Description | LogsamessagewhentheTelnetserverisenabledonaVRF |            |                    |     |     |     |
EventID:12902
| Message     | TELNET server                                   | is disabled | on VRF <vrf_name>. |     |     |     |
| ----------- | ----------------------------------------------- | ----------- | ------------------ | --- | --- | --- |
| Category    | Telnetserver                                    |             |                    |     |     |     |
| Severity    | Information                                     |             |                    |     |     |     |
| Description | LogsamessagewhentheTelnetserverisdisabledonaVRF |             |                    |     |     |     |
EventID:12903
Message Failed to enable Telnet server on VRF <vrf_name>. Admin password is not
set.
| Category | Telnetserver |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- |
| Severity | Error        |     |     |     |     |     |
Description LogsamessagewhenausertriestoenableTelnetserverwithoutsettingadmin
password
EventID:12904
Message User <user_name> logged in from <ip_address> through TELNET session.
| Category    | Telnetserver                           |     |     |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                            |     |     |     |     |     |
| Description | Logsamessagewhenauserloginissuccessful |     |     |     |     |     |
EventID:12905
293
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

User <user_name> login from <ip_address> for TELNET session has failed.

Category

Telnet server

Severity

Error

Description

Logs a message when a user login fails

Event ID: 12906

Message

User <user_name> logged out of TELNET session from <ip_address>.

Category

Telnet server

Severity

Information

Description

Logs a message when a user logs out of a session

Event ID: 12907 (Severity: Warning)

Message

TELNET session from <ip_address> is rejected because maximum number of
TELNET sessions is reached.

Category

Telnet server

Severity

Warning

Description

Logs a message when a user tries to login while maximum number of sessions are
reached.

Event ID: 12908 (Severity: Warning)

Message

TELNET session from User <user_name> is closed because maximum number
of sessions per user is reached.

Category

Telnet server

Severity

Warning

Description

Logs a message when a user session is closed when maximum number of sessions per
user are reached.

Telnet server events | 294

Chapter 112
Temperature events
| Temperature events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
Thefollowingaretheeventsrelatedtotemperature.
EventID:801(Severity:Warning)
| Message     | Unrecognized                         | sensor type | <type> |     |
| ----------- | ------------------------------------ | ----------- | ------ | --- |
| Category    | Temperature                          |             |        |     |
| Severity    | Warning                              |             |        |     |
| Description | Logeventwhensensortypeisunrecognized |             |        |     |
EventID:802(Severity:Warning)
Message Module <module> shutdown initiated for sensor <name> with critical
|          | temperature, | <temp> degC.': | yes |     |
| -------- | ------------ | -------------- | --- | --- |
| Category | Temperature  |                |     |     |
| Severity | Warning      |                |     |     |
Description Logeventwhensensortemperatureisabovethecriticalthreshold
EventID:803(Severity:Warning)
Message Over-temperature for sensor <name>, <temp> degC.': yes
| Category | Temperature |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Warning     |     |     |     |
Description Logeventwhensensortemperatureisabovetheover-temperaturethreshold
EventID:804
| Message  | Sensor <name> | back to | safe temperature, | <temp> degC. |
| -------- | ------------- | ------- | ----------------- | ------------ |
| Category | Temperature   |         |                   |              |
| Severity | Information   |         |                   |              |
Description Logeventwhenasensorreturnstosafeoperatingconditions
EventID:805
295
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | System derate                  | changed from | <old> to <new> |
| ----------- | ------------------------------ | ------------ | -------------- |
| Category    | Temperature                    |              |                |
| Severity    | Information                    |              |                |
| Description | Logwhenthesystemderatechanges. |              |                |
EventID:806(Severity:Warning)
Message Ambient temperature for sensor <name> above <temp> degC
| Category | Temperature |     |     |
| -------- | ----------- | --- | --- |
| Severity | Warning     |     |     |
Description Logwhenambienttemperatureisabovetheambienttemperaturelimits.
EventID:807
Message Ambient temperature for sensor <name> back to safe temperature, between
|          | <t_low> and | <t_high> degC |     |
| -------- | ----------- | ------------- | --- |
| Category | Temperature |               |     |
| Severity | Information |               |     |
Description Logwhenambienttemperaturereturnstosafeoperatingconditions.
EventID:808
Message Sensor <name> <limit_type> limit configuration <status>
| Category | Temperature |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logfailuresinconfiguringsensortemperaturewarning/criticallimits.
EventID:809(Severity:Warning)
Message Ambient temperature <temp> degC is above the commercial grade
|          | transceiver | limit of <limit_high> | degC |
| -------- | ----------- | --------------------- | ---- |
| Category | Temperature |                       |      |
| Severity | Warning     |                       |      |
Description Logwhenambienttemperatureisabovecommercialgradetransceiverupperlimitwhen
non-industrialtransceiversareinstalled.
EventID:810(Severity:Warning)
Temperatureevents|296

Message

Ambient temperature <temp> degC is below the commercial grade
transceiver range of <limit_low> degC

Category

Temperature

Severity

Warning

Description

Log when ambient temperature is below commercial grade transceiver lower limit when
non-industrial transceivers are installed.

Event ID: 811

Message

Ambient temperature <temp> degC returned to within the commercial grade
transceiver range of <limit_low>-<limit_high> degC

Category

Temperature

Severity

Information

Description

Log when ambient temperature returns to commercial grade transceiver range when
non-industrial transceivers are installed.

Event ID: 812 (Severity: Warning)

Message

Ambient temperature for sensor <name> below <temp> degC

Category

Temperature

Severity

Warning

Description

Log when ambient temperature is below the ambient temperature limits.

Event ID: 813 (Severity: Warning)

Message

Under-temperature for sensor <name>, <temp> degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is below the under-temperature threshold

Event ID: 814 (Severity: Warning)

Message

Module <module> shutdown initiated for sensor <name> with low critical
temperature, <temp> degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is below the low critical threshold

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

297

Chapter 113
|                 |        |     | Time | management events |
| --------------- | ------ | --- | ---- | ----------------- |
| Time management | events |     |      |                   |
Thefollowingaretheeventsrelatedtotimemanagement.
EventID:6201
| Message     | System timezone         | changed from | <oldtz> | to <newtz> |
| ----------- | ----------------------- | ------------ | ------- | ---------- |
| Category    | Timemanagement          |              |         |            |
| Severity    | Information             |              |         |            |
| Description | Changethesystemtimezone |              |         |            |
EventID:6202
Message System date/time changed from <old_time> to <new_time>
| Category    | Timemanagement           |     |     |     |
| ----------- | ------------------------ | --- | --- | --- |
| Severity    | Information              |     |     |     |
| Description | Changethesystemdate/time |     |     |     |
298
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 114
Transceiver events
| Transceiver events |     |     |
| ------------------ | --- | --- |
Thefollowingaretheeventsrelatedtotransceiver.
EventID:3801
| Message  | allow-unsupported-transceiver | feature enabled |
| -------- | ----------------------------- | --------------- |
| Category | Transceiver                   |                 |
| Severity | Information                   |                 |
Description Eventraisedwhenunsupportedtransceivermodeisenabled
EventID:3802
| Message  | allow-unsupported-transceiver | feature disabled |
| -------- | ----------------------------- | ---------------- |
| Category | Transceiver                   |                  |
| Severity | Information                   |                  |
Description Eventraisedwhenunsupportedtransceivermodeisdisabled
EventID:3803
Message allow-unsupported-transceiver feature enabled: Unsupported transceivers
found in: <list>
| Category | Transceiver |     |
| -------- | ----------- | --- |
| Severity | Information |     |
Description Eventraisedtolistunsupportedtransceiversinunsupportedtransceivermode
EventID:3804
Message Transceiver hot-swap insert for interface <interface>
| Category    | Transceiver                                      |     |
| ----------- | ------------------------------------------------ | --- |
| Severity    | Information                                      |     |
| Description | Eventraisedtoindicatetransceiverhotswapinsertion |     |
EventID:3805
299
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

Transceiver hot-swap remove for interface <interface>

Category

Transceiver

Severity

Information

Description

Event raised to indicate transceiver hotswap removal

Event ID: 3806 (Severity: Warning)

Message

Interface <interface> transceiver attempted link recovery <count>
times' throttle_count: 100

Category

Transceiver

Severity

Warning

Description

Event raised to indicate transceiver link recovery attempts

Event ID: 3807

Message

<path>

Category

Transceiver

Severity

Information

Description

Event raised to indicate detection path of unsupported transceivers

Event ID: 3808

Message

Transceiver <xcvr_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Information

Description

Event raised to indicate status of transceivers that are allowed to be operational and its
reason

Event ID: 3809 (Severity: Warning)

Message

Transceiver <xcvr_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate status of transceivers that are not allowed to be operational and
its reason

Event ID: 3810 (Severity: Warning)

Transceiver events | 300

Message

Unknown transceiver inserted in interface <interface>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate an unknown transceiver was inserted

Event ID: 3811 (Severity: Warning)

Message

Transceiver in <interface> is incompatible with the interface group
speed

Category

Transceiver

Severity

Warning

Description

Event raised to indicate a transceiver was inserted in a port that is a member of a group
configured to operate at a different speed

Event ID: 3812

Message

Adapter <adapter_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Information

Description

Event raised to indicate status of adapters that are allowed to be operational and its
reason

Event ID: 3813 (Severity: Warning)

Message

Adapter <adapter_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate status of adapters that are not allowed to be operational and its
reason

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

301

Chapter 115
UDLD events
UDLD events
ThefollowingaretheeventsrelatedtoUDLD.
EventID:4101
| Message     | UDLD is enabled              | on interface: | <intf> |
| ----------- | ---------------------------- | ------------- | ------ |
| Category    | UDLD                         |               |        |
| Severity    | Information                  |               |        |
| Description | EventraisedwhenUDLDisenabled |               |        |
EventID:4102
| Message     | UDLD is disabled              | on interface: | <intf> |
| ----------- | ----------------------------- | ------------- | ------ |
| Category    | UDLD                          |               |        |
| Severity    | Information                   |               |        |
| Description | EventraisedwhenUDLDisdisabled |               |        |
EventID:4103
| Message     | UDLD interface                                 | <intf> | is unblocked |
| ----------- | ---------------------------------------------- | ------ | ------------ |
| Category    | UDLD                                           |        |              |
| Severity    | Information                                    |        |              |
| Description | EventraisedwhenUDLDsetstheinterfaceasunblocked |        |              |
EventID:4104
| Message     | UDLD interface                               | <intf> | is blocked |
| ----------- | -------------------------------------------- | ------ | ---------- |
| Category    | UDLD                                         |        |            |
| Severity    | Error                                        |        |            |
| Description | EventraisedwhenUDLDsetstheinterfaceasblocked |        |            |
EventID:4105
302
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message  | UDLD interface | <intf> | is undetermined |     |
| -------- | -------------- | ------ | --------------- | --- |
| Category | UDLD           |        |                 |     |
| Severity | Error          |        |                 |     |
Description EventraisedwhenUDLDmovesfrombidirectionalstatetoundetermined(RFC5171mode
only)
EventID:4106(Severity:Warning)
Message UDLD interface <intf> interval <intvl_a> clamped to <intvl_b>
| Category | UDLD    |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description LogsawarningwhenUDLDclampstheintervalwhenoperatinginRFC5171mode
EventID:4107
| Message     | UDLD link                        | is enabled | on interface: | <intf> |
| ----------- | -------------------------------- | ---------- | ------------- | ------ |
| Category    | UDLD                             |            |               |        |
| Severity    | Information                      |            |               |        |
| Description | EventraisedwhenUDLDlinkisenabled |            |               |        |
EventID:4108
| Message     | UDLD link                         | is disabled | on interface: | <intf> |
| ----------- | --------------------------------- | ----------- | ------------- | ------ |
| Category    | UDLD                              |             |               |        |
| Severity    | Information                       |             |               |        |
| Description | EventraisedwhenUDLDlinkisdisabled |             |               |        |
UDLDevents|303

Chapter 116
|               |           |        | UDP Broadcast | Forwarder | events |
| ------------- | --------- | ------ | ------------- | --------- | ------ |
| UDP Broadcast | Forwarder | events |               |           |        |
ThefollowingaretheeventsrelatedtoUDPBroadcastForwarder.
EventID:3601
| Message  | UDP Broadcast         | Forwarder | Enabled |     |     |
| -------- | --------------------- | --------- | ------- | --- | --- |
| Category | UDPBroadcastForwarder |           |         |     |     |
| Severity | Information           |           |         |     |     |
Description ThiscommandenablestheUDPBroadcastForwarderfeatureinthedevice.
EventID:3602
| Message  | UDP Broadcast         | Forwarder | Disabled |     |     |
| -------- | --------------------- | --------- | -------- | --- | --- |
| Category | UDPBroadcastForwarder |           |          |     |     |
| Severity | Information           |           |          |     |     |
Description ThiscommanddisablestheUDPBroadcastForwarderfeatureinthedevice.
304
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Chapter 117

UFD events

UFD events

The following are the events related to UFD.

Event ID: 12001 (Severity: Critical)

Message

Category

Severity

Uplink Failure Detection session-id <id>, state changed from <from_
state> to <to_state>.

UFD

Critical

Description

Event reported when Links-to-Disable go down.

Event ID: 12002

Message

Uplink Failure Detection session-id <id>, state changed from <from_
state> to <to_state>.

Category

UFD

Severity

Information

Description

Event reported when Links-to-Disable ports are restored.

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

305

Chapter 118
|                 |        |     | User | management events |
| --------------- | ------ | --- | ---- | ----------------- |
| User management | events |     |      |                   |
Thefollowingaretheeventsrelatedtousermanagement.
EventID:4701
| Message     | User <user>                                | added <added_user> | with role | <user_role> |
| ----------- | ------------------------------------------ | ------------------ | --------- | ----------- |
| Category    | Usermanagement                             |                    |           |             |
| Severity    | Information                                |                    |           |             |
| Description | Logsamessagewhenanewuserisaddedtotheswitch |                    |           |             |
EventID:4702
Message User <user> deleted <deleted_user> with role <user_role>
| Category    | Usermanagement                              |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |
| Description | Logsamessagewhenauserisdeletedfromtheswitch |     |     |     |
EventID:4703
| Message     | User <username>                             | successfully | changed password |     |
| ----------- | ------------------------------------------- | ------------ | ---------------- | --- |
| Category    | Usermanagement                              |              |                  |     |
| Severity    | Information                                 |              |                  |     |
| Description | Logsamessagewhenauserchangeshis/herpassword |              |                  |     |
EventID:4704
| Message  | User <username> | password change | failed |     |
| -------- | --------------- | --------------- | ------ | --- |
| Category | Usermanagement  |                 |        |     |
| Severity | Error           |                 |        |     |
Description Logsamessagewhenauserfailstochangehis/herpassword
EventID:4705
306
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | User <username>                         | set export | password |
| ----------- | --------------------------------------- | ---------- | -------- |
| Category    | Usermanagement                          |            |          |
| Severity    | Information                             |            |          |
| Description | Logsamessagewhenausersetsexportpassword |            |          |
EventID:4706
| Message  | User <username> | restored | default export password |
| -------- | --------------- | -------- | ----------------------- |
| Category | Usermanagement  |          |                         |
| Severity | Information     |          |                         |
Description Logsamessagewhenauserrestoresdefaultexportpassword
Usermanagementevents|307

|            |         |        |            | Chapter | 119    |
| ---------- | ------- | ------ | ---------- | ------- | ------ |
|            |         |        | User-based | tunnels | events |
| User-based | tunnels | events |            |         |        |
Thefollowingaretheeventsrelatedtouser-basedtunnels.
EventID:9701
Message Tunnel Node Server SAC (<sac_ip>) is selected as (<state>)
| Category |     | User-basedtunnels |     |     |     |
| -------- | --- | ----------------- | --- | --- | --- |
| Severity |     | Information       |     |     |     |
Description EventraisedwhencontrollerisselectedasActive/Standby
EventID:9702
Message Tunnel Node Server Heartbeat has failed for SAC (<sac_ip>)
| Category    |     | User-basedtunnels                           |     |     |     |
| ----------- | --- | ------------------------------------------- | --- | --- | --- |
| Severity    |     | Error                                       |     |     |     |
| Description |     | EventraisedwhenheartbeatnotreceivedfromaSAC |     |     |     |
EventID:9703
Message Tunnel Node Server keepalive has failed for UAC (<uac_ip>)
| Category    |     | User-basedtunnels                           |     |     |     |
| ----------- | --- | ------------------------------------------- | --- | --- | --- |
| Severity    |     | Error                                       |     |     |     |
| Description |     | EventraisedwhenkeepalivenotreceivedfromaUAC |     |     |     |
EventID:9704
Message Tunnel Node Server SAC bootstrapping has reinitialized to (<sac_ip>)
| Category |     | User-basedtunnels |     |     |     |
| -------- | --- | ----------------- | --- | --- | --- |
| Severity |     | Information       |     |     |     |
Description EventraisedwhenSACbootstappingtoaSACisre-initialized
EventID:9705
308
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message  | Tunnel            | Node Server | PAPI key | has mismatched |
| -------- | ----------------- | ----------- | -------- | -------------- |
| Category | User-basedtunnels |             |          |                |
| Severity | Error             |             |          |                |
Description Eventraisedwhenpapimsgkeysentandreceivedisdifferent({key_id})
EventID:9706(Severity:Critical)
| Message     | Tunnel                       | Node Server | UAC node | is down (<uac_ip>) |
| ----------- | ---------------------------- | ----------- | -------- | ------------------ |
| Category    | User-basedtunnels            |             |          |                    |
| Severity    | Critical                     |             |          |                    |
| Description | EventraisedwhenUACnodeisdown |             |          |                    |
EventID:9707
Message Tunnel is Created - Gre Key (<gre_key>) VRF (<vrf>) Source IP (<src_
|             | ip>) Destination                        |     | IP (<dst_ip>) |     |
| ----------- | --------------------------------------- | --- | ------------- | --- |
| Category    | User-basedtunnels                       |     |               |     |
| Severity    | Information                             |     |               |     |
| Description | Eventraisedwhenuserbasedtunneliscreated |     |               |     |
EventID:9708
Message Tunnel Creation has Failed - Gre Key (<gre_key>) VRF (<vrf>) Source IP
|             | (<src_ip>)                                  | Destination | IP (<dst_ip>) |     |
| ----------- | ------------------------------------------- | ----------- | ------------- | --- |
| Category    | User-basedtunnels                           |             |               |     |
| Severity    | Error                                       |             |               |     |
| Description | Eventraisedwhenuserbasedtunnelcreationfails |             |               |     |
EventID:9709
| Message     | Tunnel                                  | is Deleted | - Tunnel | Id (<tunnel_id>) |
| ----------- | --------------------------------------- | ---------- | -------- | ---------------- |
| Category    | User-basedtunnels                       |            |          |                  |
| Severity    | Information                             |            |          |                  |
| Description | Eventraisedwhenuserbasedtunnelisdeleted |            |          |                  |
EventID:9710
User-basedtunnelsevents|309

| Message     | Tunnel Deletion                             | has | Failed - Tunnel | Id (<tunnel_id>) |
| ----------- | ------------------------------------------- | --- | --------------- | ---------------- |
| Category    | User-basedtunnels                           |     |                 |                  |
| Severity    | Error                                       |     |                 |                  |
| Description | Eventraisedwhenuserbasedtunneldeletionfails |     |                 |                  |
EventID:9711
Message Tunnel is UP - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source IP
|             | (<src_ip>)                              | Destination | IP (<dst_ip>) |     |
| ----------- | --------------------------------------- | ----------- | ------------- | --- |
| Category    | User-basedtunnels                       |             |               |     |
| Severity    | Information                             |             |               |     |
| Description | Eventraisedwhenuserbasedtunnelstateisup |             |               |     |
EventID:9712
Message Tunnel is DOWN - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source IP
|             | (<src_ip>)                                | Destination | IP (<dst_ip>) |     |
| ----------- | ----------------------------------------- | ----------- | ------------- | --- |
| Category    | User-basedtunnels                         |             |               |     |
| Severity    | Error                                     |             |               |     |
| Description | Eventraisedwhenuserbasedtunnelstateisdown |             |               |     |
EventID:9713
Message Client (<client_mac>) is bound to tunnel id (<tunnel_id>)
| Category    | User-basedtunnels                       |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Eventraisedwhenuserisgetsbindedtotunnel |     |     |     |
EventID:9714
Message Client (<client_mac>) binding to tunnel id (<tunnel_id>) has failed
| Category    | User-basedtunnels                       |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Error                                   |     |     |     |
| Description | Eventraisedwhenuserbindtotunnelidfailed |     |     |     |
EventID:9715
310
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Message     | Client (<client_mac>)                   |     | is removed | from tunnel. |
| ----------- | --------------------------------------- | --- | ---------- | ------------ |
| Category    | User-basedtunnels                       |     |            |              |
| Severity    | Information                             |     |            |              |
| Description | Eventraisedwhenuserisgetsbindedtotunnel |     |            |              |
EventID:9716
Message Client (<client_mac>) unbinding to tunnel id (<tunnel_id>) has failed
| Category    | User-basedtunnels                         |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Error                                     |     |     |     |
| Description | Eventraisedwhenuserunbindtotunnelidfailed |     |     |     |
EventID:9717
Message Client (<client_mac>) is getting modified to bind to tunnel id
|          | (<tunnel_id>)'    | throttle_count: |     | 100 |
| -------- | ----------------- | --------------- | --- | --- |
| Category | User-basedtunnels |                 |     |     |
| Severity | Information       |                 |     |     |
Description Eventraisedwhenalreadybindedusertoatunnelgetsmodified
EventID:9718
Message Modification of Client (<client_mac>) binded to (<tunnel_id>) has
|          | failed' throttle_count: |     | 100 |     |
| -------- | ----------------------- | --- | --- | --- |
| Category | User-basedtunnels       |     |     |     |
| Severity | Error                   |     |     |     |
Description Eventraisedwhenmodificationofalreadybindedusertoatunnelfails
EventID:9719
Message NFD port (<nfd_id>) is created for client (<client_mac>) vlan id
|             | (<vlan_id>)                  | port (<port>) | ecmp | id (<ecmp_id>) |
| ----------- | ---------------------------- | ------------- | ---- | -------------- |
| Category    | User-basedtunnels            |               |      |                |
| Severity    | Information                  |               |      |                |
| Description | EventraisedonNFDportcreation |               |      |                |
EventID:9720
User-basedtunnelsevents|311

Message NFD port (<nfd_id>) creation for client (<client_mac>) vlan id (<vlan_
|             | id>) port                           | (<port>) | ecmp id (<ecmp_id>) | has failed |
| ----------- | ----------------------------------- | -------- | ------------------- | ---------- |
| Category    | User-basedtunnels                   |          |                     |            |
| Severity    | Error                               |          |                     |            |
| Description | EventraisedonNFDportcreationfailure |          |                     |            |
EventID:9721
Message NFD port (<nfd_id>) is deleted for ecmp id(<ecmp_id>)
| Category    | User-basedtunnels            |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Information                  |     |     |     |
| Description | EventraisedonNFDportdeletion |     |     |     |
EventID:9722
Message NFD port (<nfd_id>) deletion for ecmp id (<ecmp_id>) has failed
| Category    | User-basedtunnels                   |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Error                               |     |     |     |
| Description | EventraisedwhenNFDportdeletionfails |     |     |     |
EventID:9723
| Message     | ECMP group                     | is created | for ecmp | id (<ecmp_id>) |
| ----------- | ------------------------------ | ---------- | -------- | -------------- |
| Category    | User-basedtunnels              |            |          |                |
| Severity    | Information                    |            |          |                |
| Description | EventraisedonECMPgroupcreation |            |          |                |
EventID:9724
Message ECMP group creation for ecmp id (<ecmp_id>) has failed
| Category    | User-basedtunnels                     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- |
| Severity    | Error                                 |     |     |     |
| Description | EventraisedonECMPgroupcreationfailure |     |     |     |
EventID:9725
312
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Message     | ECMP group                     | is deleted | for | ecmp id (<ecmp_id>) |     |     |
| ----------- | ------------------------------ | ---------- | --- | ------------------- | --- | --- |
| Category    | User-basedtunnels              |            |     |                     |     |     |
| Severity    | Information                    |            |     |                     |     |     |
| Description | EventraisedonECMPgroupdeletion |            |     |                     |     |     |
EventID:9726
Message ECMP group deletion for ecmp id(<ecmp_id>) has failed
| Category    | User-basedtunnels                     |     |     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Error                                 |     |     |     |     |     |
| Description | EventraisedwhenECMPgroupdeletionfails |     |     |     |     |     |
EventID:9727
Message MDestRx Tunnel is Created - Gre Key (<gre_key>) VLAN (<vlan>) VRF
|             | (<vrf>)                                        | Source IP (<src_ip>) |     | Destination | IP  | (<dst_ip>) |
| ----------- | ---------------------------------------------- | -------------------- | --- | ----------- | --- | ---------- |
| Category    | User-basedtunnels                              |                      |     |             |     |            |
| Severity    | Information                                    |                      |     |             |     |            |
| Description | Eventraisedwhenmdestrxuserbasedtunneliscreated |                      |     |             |     |            |
EventID:9728
Message MDestRx Tunnel Creation has Failed - Gre Key (<gre_key>) VLAN (<vlan>)
|          | VRF (<vrf>)       | Source | IP (<src_ip>) | Destination |     | IP (<dst_ip>) |
| -------- | ----------------- | ------ | ------------- | ----------- | --- | ------------- |
| Category | User-basedtunnels |        |               |             |     |               |
| Severity | Error             |        |               |             |     |               |
Description Eventraisedwhenmdestrxuserbasedtunnelcreationfails
EventID:9729
| Message     | MDest Rx                                       | Tunnel is | Deleted | - Tunnel | Id (<tunnel_id>) |     |
| ----------- | ---------------------------------------------- | --------- | ------- | -------- | ---------------- | --- |
| Category    | User-basedtunnels                              |           |         |          |                  |     |
| Severity    | Information                                    |           |         |          |                  |     |
| Description | Eventraisedwhenmdestrxuserbasedtunnelisdeleted |           |         |          |                  |     |
EventID:9730
User-basedtunnelsevents|313

Message MDest Rx Tunnel Deletion has Failed - Tunnel Id (<tunnel_id>)
| Category | User-basedtunnels |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| Severity | Error             |     |     |     |
Description Eventraisedwhenmdestrxuserbasedtunneldeletionfails
EventID:9731
Message MDestRx Tunnel is UP - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>)
|             | Source                                         | IP (<src_ip>) | Destination | IP (<dst_ip>) |
| ----------- | ---------------------------------------------- | ------------- | ----------- | ------------- |
| Category    | User-basedtunnels                              |               |             |               |
| Severity    | Information                                    |               |             |               |
| Description | Eventraisedwhenmdestrxuserbasedtunnelstateisup |               |             |               |
EventID:9732
Message MDestRx Tunnel is DOWN - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>)
|             | Source                                           | IP (<src_ip>) | Destination | IP (<dst_ip>) |
| ----------- | ------------------------------------------------ | ------------- | ----------- | ------------- |
| Category    | User-basedtunnels                                |               |             |               |
| Severity    | Error                                            |               |             |               |
| Description | Eventraisedwhenmdestrxuserbasedtunnelstateisdown |               |             |               |
EventID:9733
Message User bootstrap is failed for client (<mac_addr>) on port (<port>) due
to <reason>.
| Category    | User-basedtunnels                    |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Error                                |     |     |     |
| Description | Eventraisedwhenuserbootstrapisfailed |     |     |     |
EventID:9734
| Message     | Operational                             | state | of <zone> zone | is UP. |
| ----------- | --------------------------------------- | ----- | -------------- | ------ |
| Category    | User-basedtunnels                       |       |                |        |
| Severity    | Information                             |       |                |        |
| Description | Eventraisedwhenzoneoperationalstateisup |       |                |        |
EventID:9735(Severity:Warning)
314
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message

Operational state of <zone> zone is DOWN due to <reason>.

Category

User-based tunnels

Severity

Warning

Description

Event raised when zone operational state is down

User-based tunnels events | 315

Chapter 120
|                   |           | Virtual      | Switching | Extension | (VSX) events |
| ----------------- | --------- | ------------ | --------- | --------- | ------------ |
| Virtual Switching | Extension | (VSX) events |           |           |              |
ThefollowingaretheeventsrelatedtoVSX.
EventID:7001
| Message     | VSX ISL port                   | <port> | is down |     |     |
| ----------- | ------------------------------ | ------ | ------- | --- | --- |
| Category    | VirtualSwitchingExtension(VSX) |        |         |     |     |
| Severity    | Information                    |        |         |     |     |
| Description | VSXISLlinkisdown.              |        |         |     |     |
EventID:7002
| Message     | VSX ISL port                   | <port> | is up |     |     |
| ----------- | ------------------------------ | ------ | ----- | --- | --- |
| Category    | VirtualSwitchingExtension(VSX) |        |       |     |     |
| Severity    | Information                    |        |       |     |     |
| Description | VSXISLlinkisup.                |        |       |     |     |
EventID:7003
| Message     | VSX ISL port                   | <port> | is In-Sync with | the peer. |     |
| ----------- | ------------------------------ | ------ | --------------- | --------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |        |                 |           |     |
| Severity    | Information                    |        |                 |           |     |
| Description | VSXISLisInSyncwiththepeer.     |        |                 |           |     |
EventID:7004
Message VSX ISL port <port> is Out-Of-Sync with the peer: <reason>
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Severity    | Error                          |     |     |     |     |
| Description | VSXISLisOut-Of-Syncwiththepeer |     |     |     |     |
EventID:7005(Severity:Warning)
316
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

| Message     | VSX Keepalive                             | failed |
| ----------- | ----------------------------------------- | ------ |
| Category    | VirtualSwitchingExtension(VSX)            |        |
| Severity    | Warning                                   |        |
| Description | VSXKeepaliveisnotabletoreachthepeerdevice |        |
EventID:7006
| Message     | VSX Keepalive                          | succeeded |
| ----------- | -------------------------------------- | --------- |
| Category    | VirtualSwitchingExtension(VSX)         |           |
| Severity    | Information                            |           |
| Description | VSXKeepaliveisabletoreachthepeerdevice |           |
EventID:7007
| Message  | VSX role                       | is primary |
| -------- | ------------------------------ | ---------- |
| Category | VirtualSwitchingExtension(VSX) |            |
| Severity | Information                    |            |
Description Operationalroleofthisdevicederivedbasedondevicepriorityofthe2devices.
EventID:7008
| Message  | VSX role                       | is secondary |
| -------- | ------------------------------ | ------------ |
| Category | VirtualSwitchingExtension(VSX) |              |
| Severity | Information                    |              |
Description Operationalroleofthisdevicederivedbasedondevicepriorityofthe2devices.
EventID:7009
Message VSX Software version mismatch: peer version <peer_sw_ver>, local
|          | version <local_sw_ver>         |     |
| -------- | ------------------------------ | --- |
| Category | VirtualSwitchingExtension(VSX) |     |
| Severity | Information                    |     |
Description VSXSoftwareversionmismatch:peerswversionisnotsameaslocalswversion.
EventID:7010
Message VSX Device mismatch: peer device <peer_device_type>, local device
VirtualSwitchingExtension(VSX)events|317

<local_device_type>
| Category | VirtualSwitchingExtension(VSX) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Information                    |     |     |     |
Description VSXDevicetypemismatch:peerdevicetypeisnotsameaslocaldevicetype.
EventID:7011
| Message     | VSX <vsx_id>                   | state local | up, remote | down |
| ----------- | ------------------------------ | ----------- | ---------- | ---- |
| Category    | VirtualSwitchingExtension(VSX) |             |            |      |
| Severity    | Information                    |             |            |      |
| Description | VSXlocalupremotedown.          |             |            |      |
EventID:7012
| Message     | VSX <vsx_id>                   | state local | down, remote | up  |
| ----------- | ------------------------------ | ----------- | ------------ | --- |
| Category    | VirtualSwitchingExtension(VSX) |             |              |     |
| Severity    | Information                    |             |              |     |
| Description | VSXlocaldownremoteup.          |             |              |     |
EventID:7013
| Message     | VSX <vsx_id>                   | state local | up, remote | up  |
| ----------- | ------------------------------ | ----------- | ---------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |             |            |     |
| Severity    | Information                    |             |            |     |
| Description | VSXlocalupremoteup.            |             |            |     |
EventID:7014
| Message     | VSX <vsx_id>                   | state local | down, remote | down |
| ----------- | ------------------------------ | ----------- | ------------ | ---- |
| Category    | VirtualSwitchingExtension(VSX) |             |              |      |
| Severity    | Information                    |             |              |      |
| Description | VSXlocaldownremotedown.        |             |              |      |
EventID:7015
| Message | VSX ISL sliding | window | parameters | are reset. |
| ------- | --------------- | ------ | ---------- | ---------- |
318
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Category    | VirtualSwitchingExtension(VSX)           |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- |
| Severity    | Information                              |     |     |     |
| Description | VSXresettingtheISLprotocolslidingwindow. |     |     |     |
EventID:7016
Message VSX own ISL hello packet received, ignoring the packet.
| Category    | VirtualSwitchingExtension(VSX)                 |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Information                                    |     |     |     |
| Description | VSXswitchreceivesownISLhellopacketfromnetwork. |     |     |     |
EventID:7017
Message Rebooting the VSX <vsx_role> device with newly updated <bank_name>
image.
| Category    | VirtualSwitchingExtension(VSX)      |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Information                         |     |     |     |
| Description | SwitchrebootduetoVSXsoftwareupdate. |     |     |     |
EventID:7018
Message VSX primary ISL version <primary_version> dose not match with VSX
secondary ISL version <secondary_version>. Performing a non-hitless
image update.
| Category | VirtualSwitchingExtension(VSX) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Information                    |     |     |     |
Description VSXinter-switch-linkprotocolversionmismatchaftersecondaryreboot.
EventID:7019
| Message     | VSX <vsx_role>                 | image update | failed due | to <reason>. |
| ----------- | ------------------------------ | ------------ | ---------- | ------------ |
| Category    | VirtualSwitchingExtension(VSX) |              |            |              |
| Severity    | Error                          |              |            |              |
| Description | VSXimageupdatefailed.          |              |            |              |
EventID:7020
VirtualSwitchingExtension(VSX)events|319

| Message  | ISL out-of-sync                | and keepalive | is in established |
| -------- | ------------------------------ | ------------- | ----------------- |
| Category | VirtualSwitchingExtension(VSX) |               |                   |
| Severity | Information                    |               |                   |
Description ISLout-of-syncandkeepaliveisinestablished,handledsplitbrain
EventID:7021
| Message     | ISL out-of-sync                      | and keepalive | also failed |
| ----------- | ------------------------------------ | ------------- | ----------- |
| Category    | VirtualSwitchingExtension(VSX)       |               |             |
| Severity    | Information                          |               |             |
| Description | ISLout-of-syncandkeepalivealsofailed |               |             |
EventID:7022
| Message     | Linkup delay                   | timer started |     |
| ----------- | ------------------------------ | ------------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |               |     |
| Severity    | Information                    |               |     |
| Description | Linkupdelaytimerstarted        |               |     |
EventID:7023
| Message     | Linkup delay                   | timer expired |     |
| ----------- | ------------------------------ | ------------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |               |     |
| Severity    | Information                    |               |     |
| Description | Linkupdelaytimerexpired        |               |     |
EventID:7024
Message VSX <vsx_role> state changed from <prev_state> to <state>.
| Category    | VirtualSwitchingExtension(VSX) |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | VSXsoftwareupdatestatechange.  |     |     |
EventID:7025
| Message | Bailout timer | started |     |
| ------- | ------------- | ------- | --- |
320
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Category    | VirtualSwitchingExtension(VSX) |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | Bailouttimerstarted            |     |     |
EventID:7026
| Message     | Bailout timer                  | expired |     |
| ----------- | ------------------------------ | ------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |         |     |
| Severity    | Information                    |         |     |
| Description | Bailouttimerexpired            |         |     |
EventID:7027
| Message     | Bailout timer                  | stopped |     |
| ----------- | ------------------------------ | ------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |         |     |
| Severity    | Information                    |         |     |
| Description | Bailouttimerstopped            |         |     |
EventID:7028
| Message     | Linkup-delay                   | timer stopped |     |
| ----------- | ------------------------------ | ------------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |               |     |
| Severity    | Information                    |               |     |
| Description | Linkup-delaytimerstopped       |               |     |
EventID:7029
Message VSX device roles are inconsistent: local VSX device role <local_vsx_
|          | role>, peer                    | VSX device | role <peer_vsx_role> |
| -------- | ------------------------------ | ---------- | -------------------- |
| Category | VirtualSwitchingExtension(VSX) |            |                      |
| Severity | Error                          |            |                      |
Description VSXdevicerolesaresaidtobeconsistentonlyifoneVSXdeviceisconfiguredasprimary
andotherVSXdeviceisconfiguredassecondary
EventID:7029
| Message | VSX <vsx_role> | state | changed to <state>-<sub_state>. |
| ------- | -------------- | ----- | ------------------------------- |
VirtualSwitchingExtension(VSX)events|321

| Category    | VirtualSwitchingExtension(VSX)    |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Information                       |     |     |     |
| Description | VSXsoftwareupdatesub-statechange. |     |     |     |
EventID:7030
| Message     | VSX Keepalive                                    | is configured | without | creating VRF |
| ----------- | ------------------------------------------------ | ------------- | ------- | ------------ |
| Category    | VirtualSwitchingExtension(VSX)                   |               |         |              |
| Severity    | Information                                      |               |         |              |
| Description | VRFneedstobecreatedbeforeconfiguringVSXKeepalive |               |         |              |
EventID:7031
Message VSX Keepalive is configured without configuring IP address
| Category | VirtualSwitchingExtension(VSX) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Information                    |     |     |     |
Description IPaddressneedstobeconfiguredbeforeconfiguringVSXKeepalive
EventID:7032
Message Active-gateway is enabled on <port>. Cannot program Active-forwarding
| Category    | VirtualSwitchingExtension(VSX)    |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Error                             |     |     |     |
| Description | Failedtoprogramactive-forwarding. |     |     |     |
EventID:7033
Message Active-forwarding is enabled on <port>. Cannot program Active-gateway
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | Failedtoprogramactive-gateway. |     |     |     |
EventID:7034
| Message  | Netdev <ifname>                | configured | with ipv4 | address <value> |
| -------- | ------------------------------ | ---------- | --------- | --------------- |
| Category | VirtualSwitchingExtension(VSX) |            |           |                 |
322
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Severity    | Information                                     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Description | programmedactive-gatewayIP4addresssuccessfully. |     |     |     |
EventID:7035
| Message     | Netdev <ifname>                                 | configured | with ipv6 | address <value> |
| ----------- | ----------------------------------------------- | ---------- | --------- | --------------- |
| Category    | VirtualSwitchingExtension(VSX)                  |            |           |                 |
| Severity    | Information                                     |            |           |                 |
| Description | programmedactive-gatewayIP6addresssuccessfully. |            |           |                 |
VirtualSwitchingExtension(VSX)events|323

|     |     |     |         |           | Chapter   | 121   |
| --- | --- | --- | ------- | --------- | --------- | ----- |
|     |     |     | Virtual | Switching | Framework | (VSF) |
events
| Virtual Switching | Framework | (VSF) | events |     |     |     |
| ----------------- | --------- | ----- | ------ | --- | --- | --- |
ThefollowingaretheeventsrelatedtoVSF.
EventID:9901
| Message     | Member                         | <member_id> | boot complete |     |     |     |
| ----------- | ------------------------------ | ----------- | ------------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF) |             |               |     |     |     |
| Severity    | Information                    |             |               |     |     |     |
| Description | logeventformemberbootcomplete  |             |               |     |     |     |
EventID:9902
| Message     | Standby                        | <member_id> | boot complete |     |     |     |
| ----------- | ------------------------------ | ----------- | ------------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF) |             |               |     |     |     |
| Severity    | Information                    |             |               |     |     |     |
| Description | logeventforstandbybootcomplete |             |               |     |     |     |
EventID:9903
| Message     | Conductor                        | <member_id> | boot complete |     |     |     |
| ----------- | -------------------------------- | ----------- | ------------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)   |             |               |     |     |     |
| Severity    | Information                      |             |               |     |     |     |
| Description | logeventforConductorbootcomplete |             |               |     |     |     |
EventID:9905
| Message     | Resetting                             | member | <member_id> |     |     |     |
| ----------- | ------------------------------------- | ------ | ----------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)        |        |             |     |     |     |
| Severity    | Information                           |        |             |     |     |     |
| Description | Eventlogindicatesthatmemberisreseting |        |             |     |     |     |
EventID:9906(Severity:Warning)
324
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

| Message  | Member <member_id>             | conflict | detected | on link <link> |
| -------- | ------------------------------ | -------- | -------- | -------------- |
| Category | VirtualSwitchingFramework(VSF) |          |          |                |
| Severity | Warning                        |          |          |                |
Description EventlogforFailedprocessingHellopacketbecauseofmembernumberconflict
EventID:9907(Severity:Warning)
| Message  | Incompatible                   | version detected |     |     |
| -------- | ------------------------------ | ---------------- | --- | --- |
| Category | VirtualSwitchingFramework(VSF) |                  |     |     |
| Severity | Warning                        |                  |     |     |
Description Eventlogforindicatesthatwegotapacketwithadiffprotover
EventID:9908
| Message     | Topology                            | is <topo_type> |     |     |
| ----------- | ----------------------------------- | -------------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)      |                |     |     |
| Severity    | Information                         |                |     |     |
| Description | Eventlogindicatesthecurrenttopology |                |     |     |
EventID:9910
| Message  | Member <member_id>             | removed |     |     |
| -------- | ------------------------------ | ------- | --- | --- |
| Category | VirtualSwitchingFramework(VSF) |         |     |     |
| Severity | Information                    |         |     |     |
Description Eventlogindicatesthememberhasbeenremovedduetouserrequest
EventID:9911(Severity:Warning)
Message Maximum number of switches in the stack has reached. Cannot add MAC
|          | <mac_address>                  | product type | <type> |     |
| -------- | ------------------------------ | ------------ | ------ | --- |
| Category | VirtualSwitchingFramework(VSF) |              |        |     |
| Severity | Warning                        |              |        |     |
Description EventlogindicatesthatwewouldexceedtheMAXswitchesifweaddthisnewswitch
EventID:9912
Message Stack state is no-split with conductor id <member_id>' throttle_count:
VirtualSwitchingFramework(VSF)events|325

100
| Category    | VirtualSwitchingFramework(VSF) |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | logeventforstackstateactive    |     |     |
EventID:9913(Severity:Warning)
| Message     | Lost member                    | <member_id> | with <reason> |
| ----------- | ------------------------------ | ----------- | ------------- |
| Category    | VirtualSwitchingFramework(VSF) |             |               |
| Severity    | Warning                        |             |               |
| Description | Eventlogforlostmember          |             |               |
EventID:9914
| Message     | Reboot                            | of MAC <mac_address> | status-<status> |
| ----------- | --------------------------------- | -------------------- | --------------- |
| Category    | VirtualSwitchingFramework(VSF)    |                      |                 |
| Severity    | Information                       |                      |                 |
| Description | Eventlogforstatusofarebootrequest |                      |                 |
EventID:9915
Message Member <member_id> elected as conductor reason-<reason>
| Category    | VirtualSwitchingFramework(VSF)     |     |     |
| ----------- | ---------------------------------- | --- | --- |
| Severity    | Information                        |     |     |
| Description | logeventfortheswitchwonasconductor |     |     |
EventID:9916
Message Member <member_id> elected as standby reason-<reason>
| Category    | VirtualSwitchingFramework(VSF)   |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | logeventfortheswitchwonasstandby |     |     |
EventID:9917(Severity:Warning)
Message Switch with MAC <mac_address> cannot join stack due to incorrect
|     | product | id <product_id> |     |
| --- | ------- | --------------- | --- |
326
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventforthememberwasnotallowedtojoinduetoamismatchedproduct-id
EventID:9919(Severity:Warning)
Message Found Unsupported switch with MAC <mac_address> and Product type
<product_type>, connected to switch with MAC <mac_addr> on stack port
<port_id>
| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventforswitchrunningonadifferentplatformandtryingtojointhestack
EventID:9920(Severity:Warning)
| Message     | Heart beat                     | lost for member | <member_id> |     |
| ----------- | ------------------------------ | --------------- | ----------- | --- |
| Category    | VirtualSwitchingFramework(VSF) |                 |             |     |
| Severity    | Warning                        |                 |             |     |
| Description | logeventforheartbeatlost       |                 |             |     |
EventID:9921(Severity:Warning)
| Message  | OS version                     | mismatch detected | for member | <member_id> |
| -------- | ------------------------------ | ----------------- | ---------- | ----------- |
| Category | VirtualSwitchingFramework(VSF) |                   |            |             |
| Severity | Warning                        |                   |            |             |
Description logeventwhenos_version_mismatchhappenedonstandbyandmember
EventID:9922(Severity:Warning)
Message Attempt to connect member <member_id> from a different stack
| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventwhenmemberattempttoconnecttoadifferentstack
EventID:9923
| Message | VSF link | <link> is up |     |     |
| ------- | -------- | ------------ | --- | --- |
VirtualSwitchingFramework(VSF)events|327

| Category    | VirtualSwitchingFramework(VSF) |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Information                    |     |     |     |
| Description | logeventwhenvsflinkisup        |     |     |     |
EventID:9924
| Message     | VSF link <link>                | is down |     |     |
| ----------- | ------------------------------ | ------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF) |         |     |     |
| Severity    | Information                    |         |     |     |
| Description | logeventwhenvsflinkisdown      |         |     |     |
EventID:9925(Severity:Warning)
Message Invalid MAC <mac_address> detected on link <link> with peer MAC <mac_
add>
| Category    | VirtualSwitchingFramework(VSF)               |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                      |     |     |     |
| Description | logeventwhendifferentMACaddressonthesamelink |     |     |     |
EventID:9926(Severity:Warning)
| Message     | 2 member loop                             | detected | on ring topology |     |
| ----------- | ----------------------------------------- | -------- | ---------------- | --- |
| Category    | VirtualSwitchingFramework(VSF)            |          |                  |     |
| Severity    | Warning                                   |          |                  |     |
| Description | logeventwhenthereisa2memberloopintopology |          |                  |     |
EventID:9927
Message Fragment with conductor <member_id> is Active' throttle_count: 100
| Category    | VirtualSwitchingFramework(VSF) |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Information                    |     |     |     |
| Description | logeventforactivefragment      |     |     |     |
EventID:9928
| Message | Fragment with | conductor | <member_id> | is Inactive |
| ------- | ------------- | --------- | ----------- | ----------- |
328
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

| Category    | VirtualSwitchingFramework(VSF) |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Severity    | Information                    |     |     |     |     |
| Description | logeventforInactivefragment    |     |     |     |     |
EventID:9929
| Message     | Active                                 | fragment | detection | timeout |     |
| ----------- | -------------------------------------- | -------- | --------- | ------- | --- |
| Category    | VirtualSwitchingFramework(VSF)         |          |           |         |     |
| Severity    | Information                            |          |           |         |     |
| Description | logeventforactivestackdetectiontimeout |          |           |         |     |
EventID:9930
| Message     | Member                          | <member_id> | is  | configured | as Secondary |
| ----------- | ------------------------------- | ----------- | --- | ---------- | ------------ |
| Category    | VirtualSwitchingFramework(VSF)  |             |     |            |              |
| Severity    | Information                     |             |     |            |              |
| Description | logeventforstandbyconfiguration |             |     |            |              |
EventID:9931
| Message     | Secondary                         | configuration |     | removed |     |
| ----------- | --------------------------------- | ------------- | --- | ------- | --- |
| Category    | VirtualSwitchingFramework(VSF)    |               |     |         |     |
| Severity    | Information                       |               |     |         |     |
| Description | logeventforstandbyunconfiguration |               |     |         |     |
EventID:9932
Message Attempt to connect a member with MAC <mac_address> and product type
|             | <product_id>                            |     | having different |     | airflows |
| ----------- | --------------------------------------- | --- | ---------------- | --- | -------- |
| Category    | VirtualSwitchingFramework(VSF)          |     |                  |     |          |
| Severity    | Information                             |     |                  |     |          |
| Description | logeventwhenMaterSKUdevicejoinsthestack |     |                  |     |          |
EventID:9933(Severity:Warning)
| Message | Peer timeout |     | on interface | <port_id> |     |
| ------- | ------------ | --- | ------------ | --------- | --- |
VirtualSwitchingFramework(VSF)events|329

| Category    | VirtualSwitchingFramework(VSF)                   |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | Warning                                          |     |     |     |
| Description | logeventforpeertimeoutasitdidnotreceiveanypacket |     |     |     |
EventID:9934(Severity:Warning)
| Message     | Loop detected                  | on  | interface <port_id> |     |
| ----------- | ------------------------------ | --- | ------------------- | --- |
| Category    | VirtualSwitchingFramework(VSF) |     |                     |     |
| Severity    | Warning                        |     |                     |     |
| Description | logeventforloopdetectioninlink |     |                     |     |
EventID:9935(Severity:Warning)
Message Interface <port_id> detected a peer with a different VSF handshake
version
| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventwhenpeerswitchisindifferentVSFhandshakeversion
EventID:9936
| Message     | Interface                                   | <port_id> | added to VSF | link <link> |
| ----------- | ------------------------------------------- | --------- | ------------ | ----------- |
| Category    | VirtualSwitchingFramework(VSF)              |           |              |             |
| Severity    | Information                                 |           |              |             |
| Description | logeventwheninterfaceaddedtoaparticularlink |           |              |             |
EventID:9937
| Message     | Interface                                       | <port_id> | removed from | VSF link <link> |
| ----------- | ----------------------------------------------- | --------- | ------------ | --------------- |
| Category    | VirtualSwitchingFramework(VSF)                  |           |              |                 |
| Severity    | Information                                     |           |              |                 |
| Description | logeventwheninterfaceremovedfromaparticularlink |           |              |                 |
EventID:9938(Severity:Warning)
Message Switch with mac <mac_address> not able to autojoin as it is connected
on interface <port> which is a non default autojoin VSF interface
330
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when the switch is not able to autojoin as it is connected with a non default VSF
interface

Event ID: 9939 (Severity: Warning)

Message

Switch with MAC <mac_address> not able to autojoin as it is connected
to interface <port> which is not provisioned on the conductor for
member <member_id>

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when there is an inconsistency detected between conductors provisioned VSF
link configuration and the interface on which switch is attempting to autojoin

Event ID: 9940 (Severity: Warning)

Message

Switch with MAC <mac_address> is not autojoin eligible

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when peer switch is not autojoin eligible

Event ID: 9941 (Severity: Warning)

Message

Switch with MAC <mac_address> attempting to autojoin via multiple
interfaces

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when there is more than one interface physically connected to same switch VSF
link for autojoin

Event ID: 9942 (Severity: Warning)

Message

Switch with MAC <mac_address> failed to autojoin as there is no free
member number available

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log even when switch is not allowed to autojoin because of insufficient resources

Event ID: 9943 (Severity: Warning)

Virtual Switching Framework (VSF) events | 331

Message Switch with mac <mac_address> failed to autojoin on link <link>, port
<port>
| Category | VirtualSwitchingFramework(VSF) |     |     |     |     |     |
| -------- | ------------------------------ | --- | --- | --- | --- | --- |
| Severity | Warning                        |     |     |     |     |     |
Description logeventwhentwodifferentswitchesareattemptingtoautojoinbyconnectingtothe
sameVSFlinkonthepeer
EventID:9944(Severity:Warning)
Message Switch has VSF configurations present. Force autojoin will not take
into effect. Remove all VSF configurations followed by unconfiguring
|          | and reconfiguring              | force | autojoin | for it | to take into | effect |
| -------- | ------------------------------ | ----- | -------- | ------ | ------------ | ------ |
| Category | VirtualSwitchingFramework(VSF) |       |          |        |              |        |
| Severity | Warning                        |       |          |        |              |        |
Description logeventwhenVSFforceautojoinfailsasVSFconfigurationsexists
EventID:9945
| Message     | VSF force                             | autojoin | enabled |     |     |     |
| ----------- | ------------------------------------- | -------- | ------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)        |          |         |     |     |     |
| Severity    | Information                           |          |         |     |     |     |
| Description | logeventwhenVSFforceautojoinisenabled |          |         |     |     |     |
EventID:9946
| Message     | VSF force                              | autojoin | disabled |     |     |     |
| ----------- | -------------------------------------- | -------- | -------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)         |          |          |     |     |     |
| Severity    | Information                            |          |          |     |     |     |
| Description | logeventwhenVSFforceautojoinisdisabled |          |          |     |     |     |
EventID:9947(Severity:Warning)
Message Switch with MAC <mac_addr1> failed to autojoin. Connect the device
|          | <mac_addr2>                    | to member | <mbr_id> | link <link_id> | to proceed |     |
| -------- | ------------------------------ | --------- | -------- | -------------- | ---------- | --- |
| Category | VirtualSwitchingFramework(VSF) |           |          |                |            |     |
| Severity | Warning                        |           |          |                |            |     |
Description logeventwhenmemberconnectedtoanunsupportedinterface
EventID:9948(Severity:Warning)
332
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

Message

Interface <port_id> in VSF link <link> detected a peer with
inconsistent VSF link configuration

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when interface is in inconsistent link configuration error

Event ID: 9949

Message

Secondary member changed from <old_standby_id> to <new_standby_id>

Category

Virtual Switching Framework (VSF)

Severity

Information

Description

log event when existing secondary changes to new specified secondary member

Virtual Switching Framework (VSF) events | 333

Chapter 122
VLAN events
VLAN events
ThefollowingaretheeventsrelatedtoVLAN.
EventID:2101
| Message  | VLAN <vid>  | created | in hardware |     |
| -------- | ----------- | ------- | ----------- | --- |
| Category | VLAN        |         |             |     |
| Severity | Information |         |             |     |
Description ThislogeventinformstheuserthatVLANiscreatedinHardware
EventID:2102
| Message  | Failed | to create VLAN | <vid> in | Hardware |
| -------- | ------ | -------------- | -------- | -------- |
| Category | VLAN   |                |          |          |
| Severity | Error  |                |          |          |
Description ThislogeventinformstheuserthatVLANisnotcreatedinHardware
EventID:2103
| Message  | VLAN <vid>  | removed | from hardware |     |
| -------- | ----------- | ------- | ------------- | --- |
| Category | VLAN        |         |               |     |
| Severity | Information |         |               |     |
Description ThislogeventinformstheuserthatVLANisremovedfromHardware
EventID:2104
| Message  | Failed | to remove VLAN | <vid> from | hardware |
| -------- | ------ | -------------- | ---------- | -------- |
| Category | VLAN   |                |            |          |
| Severity | Error  |                |            |          |
Description ThislogeventinformstheuserthatVLANisnotremovedfromHardware
EventID:2105
334
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message  | Internal    | VLAN <vid> is allocated | to port | <port> |
| -------- | ----------- | ----------------------- | ------- | ------ |
| Category | VLAN        |                         |         |        |
| Severity | Information |                         |         |        |
Description ThislogeventinformsthatinternalVLANisallocatedtoport
EventID:2106
| Message     | Failed                                            | to allocate internal | VLAN to port | <port> |
| ----------- | ------------------------------------------------- | -------------------- | ------------ | ------ |
| Category    | VLAN                                              |                      |              |        |
| Severity    | Error                                             |                      |              |        |
| Description | ThislogeventinformsthatinternalVLANisnotallocated |                      |              |        |
EventID:2107
Message The mode for port <port> changed from <from> to <to> on VLAN <vid>
| Category | VLAN        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Thislogeventinformsthattheportmodehaschangedfromoneofthetrunktypesto
accessorviceversa
EventID:2108
Message Created Mac based VLAN entry. VLAN <vid> is mapped to client <mac> on
port <port>
| Category | VLAN        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatMacbasedVLANiscreatedinHardware
EventID:2109
Message Failed to create Mac based VLAN entry for <mac> with VLAN <vid> on port
<port>
| Category | VLAN  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description ThislogeventinformstheuserthatMacbasedVLANisnotcreatedinHardware
EventID:2110
VLANevents|335

Message Deleted Mac based VLAN entry for <mac> with VLAN <vid> on port <port>
| Category | VLAN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisremovedfromHardware
EventID:2111
Message Failed to remove Mac based VLAN entry for <mac> with VLAN <vid> on port
<port>
| Category | VLAN  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisnotremovedfromHardware
EventID:2112
Message Updated MAC based VLAN entry. VLAN <vid> is mapped to client <mac> on
port <port>
| Category | VLAN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisupdatedinHardware
EventID:2113
Message Failed to update Mac based VLAN entry for <mac> with VLAN <vid> on port
<port>
| Category | VLAN  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisnotupdatedinHardware
EventID:2114
| Message  | Internal VLAN | changed | to <vlan> |
| -------- | ------------- | ------- | --------- |
| Category | VLAN          |         |           |
| Severity | Information   |         |           |
Description ThislogeventinformsthatinternalVLANrangeischanged
EventID:2115
336
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

Message VLAN <vid> is down due to pvlan misconfig reason <reason>
| Category | VLAN        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatVLANisdownduetopvlanmisconfig
EventID:2116
| Message  | VLAN <vid>  | is recovered | from pvlan | misconfig |
| -------- | ----------- | ------------ | ---------- | --------- |
| Category | VLAN        |              |            |           |
| Severity | Information |              |            |           |
Description ThislogeventinformstheuserthatVLANisrecoveredfrompvlanmisconfig
EventID:2117
Message Remote node <remote_node> add for VLAN <vid> on node <local_node>
failed
| Category | VLAN  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description Thislogeventinformstheuserthatremotenodeaddforavlanfailed
EventID:2118
Message Remote node <remote_node> remove for VLAN <vid> on node <local_node>
failed
| Category | VLAN  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description Thislogeventinformstheuserthatremotenoderemoveforavlanfailed
EventID:2119
Message VLAN translation rule addition failed for port:<port_name>, in_
|          | vlan:<orig_vlan>, | out_vlan:<trans_vlan>, |     | reason=<rst> |
| -------- | ----------------- | ---------------------- | --- | ------------ |
| Category | VLAN              |                        |     |              |
| Severity | Error             |                        |     |              |
Description Logsamessagewhenvlantranslationruleadditionfailedinhardware
VLANevents|337

Chapter 123
VLAN Interface events
| VLAN Interface | events |     |     |
| -------------- | ------ | --- | --- |
ThefollowingaretheeventsrelatedtoVLANinterface.
EventID:1601
Message Vlaninterface vlan<vlan>, failed to create an l3 interface, error:
<err>
| Category    | VLANInterface                         |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Error                                 |     |     |
| Description | logserrorswhilecreatingvlaninterface. |     |     |
EventID:1602
| Message     | Vlan Interface             | <interface>, | created |
| ----------- | -------------------------- | ------------ | ------- |
| Category    | VLANInterface              |              |         |
| Severity    | Information                |              |         |
| Description | logstocreatevlaninterface. |              |         |
338
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 124

VRF events

VRF events

The following are the events related to VRF.

Event ID: 6401

Message

VRF with vrf name <vrf_name> is configured in the switch

Category

VRF

Severity

Information

Description

Logs a message when VRF is configured in the switch

Event ID: 6402

Message

Failed to configure VRF with vrf name <vrf_name> in the switch

Category

Severity

VRF

Error

Description

Logs a message when VRF configuration failed in the switch

Event ID: 6403

Message

VRF with vrf name <vrf_name> is deleted from the switch

Category

VRF

Severity

Information

Description

Logs a message when VRF is deleted from the switch

Event ID: 6404

Message

Failed to delete VRF with vrf name <vrf_name> from the switch

Category

Severity

VRF

Error

Description

Logs a message when VRF deletion failed in the switch

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

339

Chapter 125
VRF Manager events
| VRF Manager events |     |     |     |
| ------------------ | --- | --- | --- |
ThefollowingaretheeventsrelatedtoVRFManager.
EventID:5401
| Message  | Created     | a vrf entity | <vrf_entity> |
| -------- | ----------- | ------------ | ------------ |
| Category | VRFManager  |              |              |
| Severity | Information |              |              |
EventID:5402
| Message  | Deleted     | a vrf entity | <vrf_entity> |
| -------- | ----------- | ------------ | ------------ |
| Category | VRFManager  |              |              |
| Severity | Information |              |              |
EventID:5403
| Message  | vrf entity | creation | failed <vrf_entity> |
| -------- | ---------- | -------- | ------------------- |
| Category | VRFManager |          |                     |
| Severity | Error      |          |                     |
340
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 126
VRRP events
VRRP events
ThefollowingaretheeventsrelatedtoVRRP.
EventID:3701
| Message     | VRRP has been             | enabled | on this router |
| ----------- | ------------------------- | ------- | -------------- |
| Category    | VRRP                      |         |                |
| Severity    | Information               |         |                |
| Description | LogsVRRPglobalenableevent |         |                |
EventID:3702
| Message     | VRRP has been              | disabled | on this router |
| ----------- | -------------------------- | -------- | -------------- |
| Category    | VRRP                       |          |                |
| Severity    | Information                |          |                |
| Description | LogsVRRPglobaldisableevent |          |                |
EventID:3703
Message <inet_type> virtual router <vrid> on interface <interface> has taken
owner IP
| Category    | VRRP                                      |     |     |
| ----------- | ----------------------------------------- | --- | --- |
| Severity    | Information                               |     |     |
| Description | LogsvirtualrouterhastakencontrolofownerIP |     |     |
EventID:3704
Message <inet_type> virtual router <vrid> on interface <interface> has taken
|             | standby IP                                  |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Category    | VRRP                                        |     |     |
| Severity    | Information                                 |     |     |
| Description | LogsvirtualrouterhastakencontrolofstandbyIP |     |     |
EventID:3705
341
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Message

<inet_type> virtual router <vrid> on interface <interface> lost standby
IP

Category

VRRP

Severity

Information

Description

Logs virtual router has lost control of standby IP

Event ID: 3706

Message

<inet_type> virtual router <vrid> created on interface <interface>

Category

VRRP

Severity

Information

Description

Logs creation of virtual router on interface

Event ID: 3707

Message

<inet_type> virtual router <vrid> deleted from interface <interface>

Category

VRRP

Severity

Information

Description

Logs deletion of virtual router from interface

Event ID: 3708

Message

<type> address <address> is added to virtual router <vrid> on interface
<interface>

Category

VRRP

Severity

Information

Description

Logs addition of IP address to virtual router

Event ID: 3709

Message

<type> address <address> is deleted from virtual router <vrid> on
interface <interface>

Category

VRRP

Severity

Information

Description

Logs deletion of IP address from virtual router

Event ID: 3710

VRRP events | 342

Message

<inet_type> virtual router <vrid> version changed to <value> on
interface <interface>

Category

VRRP

Severity

Information

Description

Logs version change for virtual router

Event ID: 3711

Message

<inet_type> virtual router <vrid> advertisement interval has changed to
<value> milliseconds on interface <interface>

Category

VRRP

Severity

Information

Description

Logs advertisement timer has changed for virtual router

Event ID: 3712

Message

<inet_type> virtual router <vrid> preempt delay time has changed to
<value> seconds on interface <interface>

Category

VRRP

Severity

Information

Description

Logs preempt delay timer has changed for virtual router

Event ID: 3713

Message

<inet_type> virtual router <vrid> state change from <old_state> to
<new_state> on interface <interface>

Category

VRRP

Severity

Information

Description

Logs state has changed for virtual router on interface

Event ID: 3714

Message

Enabled preempt option for <inet_type> virtual router <vrid> on
interface <interface>

Category

VRRP

Severity

Information

Description

Logs preempt option has been enabled for virtual router

Event ID: 3715

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

343

Message

Enabled virtual IP ping for <inet_type> virtual router <vrid> on
interface <interface>

Category

VRRP

Severity

Information

Description

Logs virtual IP ping has been enabled for virtual router

Event ID: 3716

Message

Enabled <inet_type> virtual router <vrid> on interface <interface>

Category

VRRP

Severity

Information

Description

Logs virtual router has been enabled on interface

Event ID: 3717

Message

Disabled preempt option for <inet_type> virtual router <vrid> on
interface <interface>

Category

VRRP

Severity

Information

Description

Logs preempt option has been disabled for virtual router

Event ID: 3718

Message

Disabled virtual IP ping for <inet_type> virtual router <vrid> on
interface <interface>

Category

VRRP

Severity

Information

Description

Logs virtual IP ping has been disabled for virtual router

Event ID: 3719

Message

Disabled <inet_type> virtual router <vrid> on interface <interface>

Category

VRRP

Severity

Information

Description

Logs virtual router has been disabled on interface

Event ID: 3720

VRRP events | 344

Message <inet_type> virtual router <vrid> priority changed to <value> on
|             | interface                                  | <interface> |     |
| ----------- | ------------------------------------------ | ----------- | --- |
| Category    | VRRP                                       |             |     |
| Severity    | Information                                |             |     |
| Description | Logspriorityhasbeenchangedforvirtualrouter |             |     |
EventID:3721
Message <inet_type> virtual router <vrid> mode changed to <value> on interface
<interface>
| Category    | VRRP                                |     |     |
| ----------- | ----------------------------------- | --- | --- |
| Severity    | Information                         |     |     |
| Description | Logsvirtualroutermodehasbeenchanged |     |     |
EventID:3722
Message Track object <track> is associated with <inet_type> virtual router
<vrid>
| Category    | VRRP                                              |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Information                                       |     |     |
| Description | Logstrackobjecthasbeenassociatedwithvirtualrouter |     |     |
EventID:3723
Message Track object <track> is de-associated from <inet_type> virtual router
<vrid>
| Category | VRRP        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logstrackobjecthasbeende-associatedfromvirtualrouter
EventID:3724
| Message     | Track object                  | <track> | is created |
| ----------- | ----------------------------- | ------- | ---------- |
| Category    | VRRP                          |         |            |
| Severity    | Information                   |         |            |
| Description | Logstrackobjecthasbeencreated |         |            |
EventID:3725
345
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Message     | Track object                  | <track> | is deleted |
| ----------- | ----------------------------- | ------- | ---------- |
| Category    | VRRP                          |         |            |
| Severity    | Information                   |         |            |
| Description | Logstrackobjecthasbeendeleted |         |            |
EventID:3726
Message Track object <track> state changed <old_state> to <new_state>
| Category    | VRRP                       |     |     |
| ----------- | -------------------------- | --- | --- |
| Severity    | Information                |     |     |
| Description | Logstrackobjectstatechange |     |     |
EventID:3727
Message Track object <track> associated with interface <interface>
| Category    | VRRP                                    |     |     |
| ----------- | --------------------------------------- | --- | --- |
| Severity    | Information                             |     |     |
| Description | Logstrackobjectassociationwithinterface |     |     |
EventID:3728
Message <inet_type> virtual router <vrid> recieved packet with authentication
|             | type mismatch                             | on interface | <interface> |
| ----------- | ----------------------------------------- | ------------ | ----------- |
| Category    | VRRP                                      |              |             |
| Severity    | Information                               |              |             |
| Description | Logsauthenticationfailuresonvirtualrouter |              |             |
EventID:3729
Message <inet_type> virtual router <vrid> recieved packet with authentication
|             | key mismatch                              | on interface | <interface> |
| ----------- | ----------------------------------------- | ------------ | ----------- |
| Category    | VRRP                                      |              |             |
| Severity    | Information                               |              |             |
| Description | Logsauthenticationfailuresonvirtualrouter |              |             |
VRRPevents|346

Chapter 127
VSX Sync events
VSX Sync events
ThefollowingaretheeventsrelatedtoVSXsync.
EventID:7601
| Message  | Configuration | sync error: | <id> |
| -------- | ------------- | ----------- | ---- |
| Category | VSXSync       |             |      |
| Severity | Error         |             |      |
Description LogseventwhenerrorinsynchronizingconfigbetweentwoVSXpeers
EventID:7602
| Message     | Configuration                             | sync update: | <id> |
| ----------- | ----------------------------------------- | ------------ | ---- |
| Category    | VSXSync                                   |              |      |
| Severity    | Information                               |              |      |
| Description | Logseventwhenthereisanupdateforconfigsync |              |      |
EventID:7603
| Message  | Configuration-persistence: |     | <id> |
| -------- | -------------------------- | --- | ---- |
| Category | VSXSync                    |     |      |
| Severity | Information                |     |      |
Description Logseventwhenconfigiscopiedtostartup-configonanyoftheVSXpeer
347
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

Chapter 128

VXLAN agent events

VXLAN agent events

The following are the events related to VXLAN agent.

Event ID: 12501

Message

Netvp add failed for vni_id: <vni_id>, tunnel_id: <tunnel_id>, vlan:
<vlan>.

Category

VXLAN agent

Severity

Error

Description

Event raised when netvp add fails in agent

Event ID: 12502

Message

Tunnel add failed for tunnel_id: <tunnel_id>, ecmp_id: <ecmp_id>.

Category

VXLAN agent

Severity

Error

Description

Event raised when tunnel add fails in agent

AOS-CX Event Log Message Reference Guide 10.09 | (4100i, 6xxx, 8xxx Switch Series)

348

Chapter 129
VXLAN events
VXLAN events
ThefollowingaretheeventsrelatedtoVXLAN.
EventID:8101
| Message     | VNI id <vni_id>                 | creation failed |
| ----------- | ------------------------------- | --------------- |
| Category    | VXLAN                           |                 |
| Severity    | Error                           |                 |
| Description | EventraisedwhenVNIcreationfails |                 |
EventID:8102
| Message     | VNI id <vni_id>           | created |
| ----------- | ------------------------- | ------- |
| Category    | VXLAN                     |         |
| Severity    | Information               |         |
| Description | EventraisedwhenVNIcreated |         |
EventID:8103
| Message     | VNI id <vni_id>                 | deletion fails |
| ----------- | ------------------------------- | -------------- |
| Category    | VXLAN                           |                |
| Severity    | Error                           |                |
| Description | EventraisedwhenVNIdeletionfails |                |
EventID:8104
| Message     | VNI id <vni_id>             | has been deleted |
| ----------- | --------------------------- | ---------------- |
| Category    | VXLAN                       |                  |
| Severity    | Information                 |                  |
| Description | EventraisedwhenVNIisdeleted |                  |
EventID:8105
349
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)

| Message     | Vtep-Peer                         | <vtep_peer> | is created |
| ----------- | --------------------------------- | ----------- | ---------- |
| Category    | VXLAN                             |             |            |
| Severity    | Information                       |             |            |
| Description | EventraisedwhenVtep-Peeriscreated |             |            |
EventID:8106
| Message     | Vtep-Peer                              | <vtep_peer> | has been deleted |
| ----------- | -------------------------------------- | ----------- | ---------------- |
| Category    | VXLAN                                  |             |                  |
| Severity    | Information                            |             |                  |
| Description | EventraisedwhenVtep-Peerhasbeendeleted |             |                  |
EventID:8107
| Message     | Vtep-Peer                             | <vtep_peer> | deletion failed |
| ----------- | ------------------------------------- | ----------- | --------------- |
| Category    | VXLAN                                 |             |                 |
| Severity    | Error                                 |             |                 |
| Description | EventraisedwhenVtep-Peerdeletionfails |             |                 |
EventID:8108
Message Access-Port with vlan <vlan_id> and port <port_name> has been created
| Category    | VXLAN                                    |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | EventraisedwhenAccess-Porthasbeencreated |     |     |
EventID:8109
Message Access-Port with port <port_name> and vlan <vlan_id> has been deleted
| Category    | VXLAN                                    |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | EventraisedwhenAccess-Porthasbeendeleted |     |     |
EventID:8110
| Message | Vtep-Peer | <vtep> state | is operational |
| ------- | --------- | ------------ | -------------- |
VXLANevents|350

| Category | VXLAN       |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description EventraisedwhenVtep-Peerstatusischangedtooperational
EventID:8111
| Message  | Vtep-Peer   | <vtep> state | is configuration_error |
| -------- | ----------- | ------------ | ---------------------- |
| Category | VXLAN       |              |                        |
| Severity | Information |              |                        |
Description EventraisedwhenVtep-Peerstatusischangedtoconfigurationerror
EventID:8112
| Message  | Vtep-Peer   | <vtep> state | is no_hw_resources |
| -------- | ----------- | ------------ | ------------------ |
| Category | VXLAN       |              |                    |
| Severity | Information |              |                    |
Description EventraisedwhenVtep-Peerstatusischangedtonohardwareresources
EventID:8113
| Message  | Vtep-Peer   | <vtep> state | is activating |
| -------- | ----------- | ------------ | ------------- |
| Category | VXLAN       |              |               |
| Severity | Information |              |               |
Description EventraisedwhenVtep-Peerstatusischangedtoactivating
EventID:8114
| Message     | Tunnel                                       | <remote_ip> added | to hardware |
| ----------- | -------------------------------------------- | ----------------- | ----------- |
| Category    | VXLAN                                        |                   |             |
| Severity    | Information                                  |                   |             |
| Description | EventraisedwhenaVxLANtunnelisaddedtohardware |                   |             |
EventID:8115
| Message  | Tunnel | <remote_ip> deleted | from hardware |
| -------- | ------ | ------------------- | ------------- |
| Category | VXLAN  |                     |               |
351
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Severity    | Information                                      |     |     |
| ----------- | ------------------------------------------------ | --- | --- |
| Description | EventraisedwhenaVxLANtunnelisdeletedfromhardware |     |     |
EventID:8116
| Message  | Tunnel <remote_ip> | delete deferred |     |
| -------- | ------------------ | --------------- | --- |
| Category | VXLAN              |                 |     |
| Severity | Information        |                 |     |
Description EventraisedwhenaVxLANtunnelhasitsdeletiondeferredbyL3PD
EventID:8117
| Message  | Tunnel <remote_ip> | deferred delete | canceled |
| -------- | ------------------ | --------------- | -------- |
| Category | VXLAN              |                 |          |
| Severity | Information        |                 |          |
Description EventraisedwhenaVxLANtunnelhasitsdeferreddeletioncanceled
VXLANevents|352

Chapter 130
|            |              |        | Zero touch | provisioning | events |
| ---------- | ------------ | ------ | ---------- | ------------ | ------ |
| Zero touch | provisioning | events |            |              |        |
Thefollowingaretheeventsrelatedtozerotouchprovisioning.
EventID:8701
| Message     | ZTP service                  | has started |     |     |     |
| ----------- | ---------------------------- | ----------- | --- | --- | --- |
| Category    | Zerotouchprovisioning        |             |     |     |     |
| Severity    | Information                  |             |     |     |     |
| Description | LogeventwhenZTPservicestarts |             |     |     |     |
EventID:8702
| Message     | ZTP service                 | has stopped |     |     |     |
| ----------- | --------------------------- | ----------- | --- | --- | --- |
| Category    | Zerotouchprovisioning       |             |     |     |     |
| Severity    | Information                 |             |     |     |     |
| Description | LogeventwhenZTPservicestops |             |     |     |     |
EventID:8703
| Message     | ZTP service                              | status changed | to in-progress |     |     |
| ----------- | ---------------------------------------- | -------------- | -------------- | --- | --- |
| Category    | Zerotouchprovisioning                    |                |                |     |     |
| Severity    | Information                              |                |                |     |     |
| Description | LogeventwhenZTPchangestatustoin-progress |                |                |     |     |
EventID:8704
| Message     | ZTP service                          | status changed | to success |     |     |
| ----------- | ------------------------------------ | -------------- | ---------- | --- | --- |
| Category    | Zerotouchprovisioning                |                |            |     |     |
| Severity    | Information                          |                |            |     |     |
| Description | LogeventwhenZTPchangestatustosuccess |                |            |     |     |
EventID:8705(Severity:Critical)
353
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- | --- |

Message

ZTP service status changed to failed because of invalid configuration
file

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of invalid config file

Event ID: 8706 (Severity: Critical)

Message

ZTP service status changed to failed because of invalid image file

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of invalid image file

Event ID: 8707 (Severity: Warning)

Message

ZTP service status changed to failed because TFTP info is not available

Category

Zero touch provisioning

Severity

Warning

Description

Log event when ZTP fails because no TFTP info is available

Event ID: 8708 (Severity: Warning)

Message

ZTP service status changed to failed because TFTP server is not
reachable

Category

Zero touch provisioning

Severity

Warning

Description

Log event when ZTP fails because TFTP server is not reachable

Event ID: 8709 (Severity: Critical)

Message

ZTP service status changed to failed because of non-default startup
configuration

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP failed because of non-default startup config

Event ID: 8710 (Severity: Critical)

Zero touch provisioning events | 354

Message ZTP service status changed to failed because running configuration is
modified
| Category | Zerotouchprovisioning |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Critical              |     |     |
Description LogeventwhenZTPfailedbecauseofmodifiedrunningconfig
EventID:8711(Severity:Warning)
Message ZTP service status changed to failed because of timeout
| Category    | Zerotouchprovisioning                 |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Warning                               |     |     |
| Description | LogeventwhenZTPfailedbecauseoftimeout |     |     |
EventID:8712
| Message  | ZTP: Image            | file not provided |     |
| -------- | --------------------- | ----------------- | --- |
| Category | Zerotouchprovisioning |                   |     |
| Severity | Information           |                   |     |
Description LogsrelatedtoZTPconfigurations-imagefilenotprovided
EventID:8713
| Message  | ZTP: Config           | file not | provided |
| -------- | --------------------- | -------- | -------- |
| Category | Zerotouchprovisioning |          |          |
| Severity | Information           |          |          |
Description Logsrelatedtoztpconfigurations-configfilenotprovided
EventID:8714
| Message  | ZTP: TFTP             | server option | not provided |
| -------- | --------------------- | ------------- | ------------ |
| Category | Zerotouchprovisioning |               |              |
| Severity | Information           |               |              |
Description Logsrelatedtoztpconfigurations-TFTPservernamenotprovided
EventID:8715
355
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| ----------------------------------------- | --- | ----------------------------- | --- |

| Message  | ZTP: Exceeded         | max path | length of | TFTP server |     |
| -------- | --------------------- | -------- | --------- | ----------- | --- |
| Category | Zerotouchprovisioning |          |           |             |     |
| Severity | Error                 |          |           |             |     |
Description Logsrelatedtoztpconfigurations-pathlengthexceededofTFTPservername
EventID:8718
| Message     | ZTP: Received                                 | TFTP server | <tftp_ip> | from dhcp | server |
| ----------- | --------------------------------------------- | ----------- | --------- | --------- | ------ |
| Category    | Zerotouchprovisioning                         |             |           |           |        |
| Severity    | Information                                   |             |           |           |        |
| Description | Logsrelatedtoztpconfigurations-TFTPIPreceived |             |           |           |        |
EventID:8719
Message ZTP: Received image file <image_file> from dhcp server
| Category | Zerotouchprovisioning |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Severity | Information           |     |     |     |     |
Description Logsrelatedtoztpconfigurations-Imagefilenamereceived
EventID:8720
Message ZTP: Received config file <config_file> from dhcp server
| Category | Zerotouchprovisioning |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Severity | Information           |     |     |     |     |
Description Logsrelatedtoztpconfigurations-Configfilenamereceived
EventID:8721
Message ZTP: Received Aruba Central location <central_location> from DHCP
server
| Category | Zerotouchprovisioning |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Severity | Information           |     |     |     |     |
Description Logsrelatedtoztpconfigurations-ArubaCentralFQDNorIPv4received
EventID:8723
Zerotouchprovisioningevents|356

| Message  | ZTP: Aruba            | Central location | option not | provided |
| -------- | --------------------- | ---------------- | ---------- | -------- |
| Category | Zerotouchprovisioning |                  |            |          |
| Severity | Information           |                  |            |          |
Description Logsrelatedtoztpconfigurations-ArubaCentralFQDNorIPv4notprovided
EventID:8724
Message ZTP: Received HTTP proxy location <http_proxy_location> from DHCP
server.
| Category | Zerotouchprovisioning |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description Logsrelatedtoztpconfigurations-ArubaHTTPproxyFQDNorIPv4received
EventID:8726
Message ZTP: HTTP proxy location was not received in the DHCP offer.
| Category | Zerotouchprovisioning |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description Logsrelatedtoztpconfigurations-HTTPProxyFQDNorIPv4notprovided
EventID:8727(Severity:Critical)
Message ZTP service status changed to failed because <filename> file download
|          | encountered           | unexpected | error. |     |
| -------- | --------------------- | ---------- | ------ | --- |
| Category | Zerotouchprovisioning |            |        |     |
| Severity | Critical              |            |        |     |
Description LogeventwhenZTPfailsbecauseofunexpectederrorinconfig/imagefiledownload
EventID:8728(Severity:Critical)
Message ZTP service status changed to failed because <filename> file did not
get downloaded.
| Category | Zerotouchprovisioning |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Critical              |     |     |     |
Description LogeventwhenZTPfailsbecauseofconfig/imagefiledownloaderror
EventID:8729(Severity:Critical)
357
| AOS-CXEventLogMessageReferenceGuide10.09| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| ----------------------------------------- | --- | ----------------------------- | --- | --- |

Message

ZTP service status changed to failed because the downloaded
configuration could not be copied to start-up configuration.

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because downloaded config did not get copied to start-up config

Event ID: 8730 (Severity: Critical)

Message

ZTP service status changed to failed because <filename> file download
encountered unexpected error. Reason: <reason>

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of unexpected error in config file download

Zero touch provisioning events | 358

Chapter 131
|          |             |           | Support | and other | resources |
| -------- | ----------- | --------- | ------- | --------- | --------- |
| Support  | and other   | resources |         |           |           |
| Warranty | information |           |         |           |           |
Toviewwarrantyinformationforyourproduct,gotohttps://www.arubanetworks.com/support-
services/product-warranties/.
| Documentation |     | feedback |     |     |     |
| ------------- | --- | -------- | --- | --- | --- |
Arubaiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpusimprovethe
documentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback(docsfeedback-
switching@hpe.com).Whensubmittingyourfeedback,includethedocumenttitle,partnumber,edition,and
publicationdatelocatedonthefrontcoverofthedocument.Foronlinehelpcontent,includetheproduct
name,productversion,helpedition,andpublicationdatelocatedonthelegalnoticespage.
359
AOS-CXEventLogMessageReferenceGuide10.09| (4100i,6xxx,8xxxSwitchSeries)