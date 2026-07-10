AOS-CX 10.13 Event Log
Message Reference Guide

All Switch Series

Published: November 2023

Version: 1

Copyright Information

© Copyright 2024 Hewlett Packard Enterprise Development LP.

This product includes code licensed under certain open source licenses which require source
compliance. The corresponding source for these components is available upon request. This offer is
valid to anyone in receipt of this information and shall expire three years following the date of the final
distribution of this product version by Hewlett Packard Enterprise Company. To obtain such source
code, please check if the code is available in the HPE Software Center at
https://myenterpriselicense.hpe.com/cwp-ui/software but, if not, send a written request for specific
software version and product for which you want the open source code. Along with the request, please
send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
Attn: General Counsel
WW Corporate Headquarters
1701 E Mossy Oaks Rd Spring, TX 77389
United States of America.

| 2

Notices

The information contained herein is subject to change without notice. The only warranties for Hewlett
Packard Enterprise products and services are set forth in the express warranty statements
accompanying such products and services. Nothing herein should be construed as constituting an
additional warranty. Hewlett Packard Enterprise shall not be liable for technical or editorial errors or
omissions contained herein.

Confidential computer software. Valid license from Hewlett Packard Enterprise required for possession,
use, or copying. Consistent with FAR 12.211 and 12.212, Commercial Computer Software, Computer
Software Documentation, and Technical Data for Commercial Items are licensed to the U.S. Government
under vendor's standard commercial license.

Links to third-party websites take you outside the Hewlett Packard Enterprise website. Hewlett Packard
Enterprise has no control over and is not responsible for information outside the Hewlett Packard
Enterprise website.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

3

Contents
| About                               | this       | document   |        |            |        |        |              | 12  |
| ----------------------------------- | ---------- | ---------- | ------ | ---------- | ------ | ------ | ------------ | --- |
| Applicableproducts                  |            |            |        |            |        |        |              | 12  |
| Latestversionavailableonline        |            |            |        |            |        |        |              | 12  |
| Commandsyntaxnotationconventions    |            |            |        |            |        |        |              | 12  |
| Abouttheexamples                    |            |            |        |            |        |        |              | 13  |
| Identifyingswitchportsandinterfaces |            |            |        |            |        |        |              | 14  |
| Identifyingmodularswitchcomponents  |            |            |        |            |        |        |              | 15  |
| EventLogMessageFormat               |            |            |        |            |        |        |              | 16  |
| AAA events                          |            |            |        |            |        |        |              | 18  |
| Accounting                          |            | events     |        |            |        |        |              | 20  |
| ACLs                                | events     |            |        |            |        |        |              | 21  |
| Alarm                               | events     |            |        |            |        |        |              | 22  |
| ARC events                          |            |            |        |            |        |        |              | 24  |
| ARP security                        |            | events     |        |            |        |        |              | 27  |
| ASIC table                          |            | full       | error  | for        | L3PD   | events |              | 28  |
| BFD events                          |            |            |        |            |        |        |              | 31  |
| BGP events                          |            |            |        |            |        |        |              | 36  |
| Bidirectional                       |            | PIM        |        | (PIM-BIDI) |        | events |              | 40  |
| Bluetooth                           |            | Management |        |            | events |        |              | 42  |
| CDP events                          |            |            |        |            |        |        |              | 44  |
| Central                             | Source     |            | events |            |        |        |              | 45  |
| Client                              | insight    |            | events |            |        |        |              | 46  |
| Certificate                         |            | management |        |            | events |        |              | 49  |
| Config                              | Management |            |        | events     |        |        |              | 54  |
| Config                              | validator  |            | events |            |        |        |              | 55  |
| Connectivity                        |            | Fault      |        | Management |        |        | (CFM) events | 56  |
| Console                             | events     |            |        |            |        |        |              | 57  |
5
AOS-CX10.13EventLogMessageReferenceGuide| (AllSwitchSeries)

| Container   | manager        |             | events             |        |         |         | 59  |
| ----------- | -------------- | ----------- | ------------------ | ------ | ------- | ------- | --- |
| CoPP        | events         |             |                    |        |         |         | 61  |
| CPU_RX      | events         |             |                    |        |         |         | 64  |
| Credential  | Manager        |             | events             |        |         |         | 65  |
| CX LMS      | events         |             |                    |        |         |         | 66  |
| Device      | fingerprinting |             | events             |        |         |         | 68  |
| DHCP        | Relay          | events      |                    |        |         |         | 69  |
| DHCP        | server         | events      |                    |        |         |         | 70  |
| DHCPv4      | snooping       | events      |                    |        |         |         | 73  |
| DHCPv6      | Relay          | events      |                    |        |         |         | 78  |
| DHCPv6      | snooping       | events      |                    |        |         |         | 79  |
| Discovery   | and            | Capability  | Exchange           | (DCBx) | events  |         | 84  |
| Distributed |                | services    | events             |        |         |         | 85  |
| DNS         | client events  |             |                    |        |         |         | 87  |
| Dot1x       | supplicant     | events      |                    |        |         |         | 88  |
| Download    | events         |             |                    |        |         |         | 88  |
| DPSE        | daemon         | events      |                    |        |         |         | 91  |
| ECMP        | events         |             |                    |        |         |         | 93  |
| ERPS        | events         |             |                    |        |         |         | 95  |
| EVPN        | events         |             |                    |        |         |         | 99  |
| External    | Storage        | events      |                    |        |         |         | 105 |
| Fan events  |                |             |                    |        |         |         | 107 |
| Fault       | monitor        | events      |                    |        |         |         | 112 |
| Feature     | Pack           | events      |                    |        |         |         | 114 |
| Firmware    | Update         | events      |                    |        |         |         | 118 |
| Forwarding  |                | and Queuing | for Time-Sensitive |        | Streams | (FQTSS) |     |
| events      |                |             |                    |        |         |         | 120 |
|6

| Hardware      |             | Health        |                 | Monitor       | events     |        | 121 |
| ------------- | ----------- | ------------- | --------------- | ------------- | ---------- | ------ | --- |
| Hardware      |             | switch        |                 | controller    | sync       | events | 127 |
| Hot Patch     |             | events        |                 |               |            |        | 129 |
| HTTPS         | Server      | events        |                 |               |            |        | 136 |
| In-System     |             | Programming   |                 |               | events     |        | 138 |
| Interface     |             | and           | Interface       |               | Diagnostic | events | 141 |
| Internal      | storage     |               | events          |               |            |        | 144 |
| IP Flow       | Information |               |                 | Export        | events     |        | 145 |
| IP Flow       | Monitoring  |               |                 | Advertisement |            | events | 145 |
| IP source     |             | lockdown      |                 | events        |            |        | 147 |
| IP tunnels    |             | events        |                 |               |            |        | 149 |
| IP-SLA        | events      |               |                 |               |            |        | 153 |
| IPSec         | tunnel      | offload       |                 | events        |            |        | 154 |
| IPv6 Router   |             | Advertisement |                 |               | events     |        | 156 |
| IRDP          | events      |               |                 |               |            |        | 161 |
| ISSU          | events      |               |                 |               |            |        | 161 |
| Job scheduler |             |               | events          |               |            |        | 165 |
| L3 Encap      |             | capacity      |                 | events        |            |        | 166 |
| L3 Resource   |             | Manager       |                 |               | events     |        | 167 |
| LACP          | events      |               |                 |               |            |        | 169 |
| LAG events    |             |               |                 |               |            |        | 175 |
| Launch        | Daemon      |               | (LaunchD)events |               |            |        | 177 |
| Layer         | 3 Interface |               |                 | events        |            |        | 179 |
| LED events    |             |               |                 |               |            |        | 186 |
| LLDP          | events      |               |                 |               |            |        | 187 |
| Loop          | Protect     | events        |                 |               |            |        | 190 |
| Loopback      |             | events        |                 |               |            |        | 193 |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 7

| MAC         | address  | management |         |               | events |        |        | 194 |
| ----------- | -------- | ---------- | ------- | ------------- | ------ | ------ | ------ | --- |
| MAC         | Address  | mode       |         | configuration |        | events |        | 196 |
| MAC         | Learning |            | events  |               |        |        |        | 196 |
| MACsec      | events   |            |         |               |        |        |        | 199 |
| Management  |          | events     |         |               |        |        |        | 202 |
| MDNS        | events   |            |         |               |        |        |        | 203 |
| MGMD        | events   |            |         |               |        |        |        | 204 |
| Mirroring   |          | events     |         |               |        |        |        | 210 |
| Module      | events   |            |         |               |        |        |        | 212 |
| MPLS        | events   |            |         |               |        |        |        | 221 |
| MSDP        | events   |            |         |               |        |        |        | 222 |
| Message     | Session  |            | Relay   | Protocol      |        | events |        | 223 |
| Multicast   |          | Traffic    | Manager |               | events |        |        | 227 |
| Message     | Session  |            | Relay   | Protocol      |        | (MSRP) | events | 228 |
| MVRP        | events   |            |         |               |        |        |        | 232 |
| NAE         | Agents   | events     |         |               |        |        |        | 234 |
| NAE         | events   |            |         |               |        |        |        | 235 |
| NAE         | script   | generation |         | events        |        |        |        | 238 |
| NAE         | Scripts  | events     |         |               |        |        |        | 239 |
| ND snooping |          | events     |         |               |        |        |        | 242 |
| NDM         | events   |            |         |               |        |        |        | 244 |
| NTP         | events   |            |         |               |        |        |        | 251 |
| OSPFv2      | events   |            |         |               |        |        |        | 253 |
| OSPFv3      | events   |            |         |               |        |        |        | 256 |
| Packet      | capture  |            | events  |               |        |        |        | 257 |
| Password    |          | Reset      | events  |               |        |        |        | 261 |
| PIM events  |          |            |         |               |        |        |        | 262 |
|8

| Policies        | events            |          |               |        | 269 |
| --------------- | ----------------- | -------- | ------------- | ------ | --- |
| Port access     | events            |          |               |        | 270 |
| Port access     | application-based |          | policy events |        | 277 |
| Port access     | group             | based    | policy events |        | 279 |
| Port access     | roles             | events   |               |        | 281 |
| Port events     |                   |          |               |        | 282 |
| Port security   | events            |          |               |        | 284 |
| Port Statistics | events            |          |               |        | 285 |
| Power           | events            |          |               |        | 286 |
| Power           | over Ethernet     | events   |               |        | 291 |
| PTP events      |                   |          |               |        | 300 |
| Proxy           | ARP events        |          |               |        | 304 |
| QoS ASIC        | Provider          | events   |               |        | 306 |
| Quality         | of Service        | events   |               |        | 308 |
| Rapid           | per VLAN          | Spanning | Tree Protocol | events | 309 |
| RBAC            | events            |          |               |        | 313 |
| Redundant       | Management        |          | events        |        | 314 |
| Replication     | Manager           | events   |               |        | 316 |
| REST            | events            |          |               |        | 317 |
| Self Test       | events            |          |               |        | 329 |
| sFlow           | events            |          |               |        | 330 |
| SFTP            | Client events     |          |               |        | 337 |
| Smartlink       | events            |          |               |        | 338 |
| SNMP            | events            |          |               |        | 339 |
| SSH client      | events            |          |               |        | 342 |
| SSH server      | events            |          |               |        | 343 |
| Supportability  | events            |          |               |        | 348 |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 9

| SYS events                         |            |              |           |           |        |              | 355 |
| ---------------------------------- | ---------- | ------------ | --------- | --------- | ------ | ------------ | --- |
| SYSMON                             |            | events       |           |           |        |              | 358 |
| TCAM                               | events     |              |           |           |        |              | 360 |
| Telnet                             | server     |              | events    |           |        |              | 364 |
| Temperature                        |            |              | events    |           |        |              | 367 |
| Time                               | management |              |           | events    |        |              | 370 |
| TPM                                | events     |              |           |           |        |              | 370 |
| Traffic                            | Insight    |              | events    |           |        |              | 371 |
| Transceiver                        |            | events       |           |           |        |              | 374 |
| UDLD                               | events     |              |           |           |        |              | 378 |
| UDP                                | Broadcast  |              | Forwarder |           |        | events       | 380 |
| UFD                                | events     |              |           |           |        |              | 381 |
| User                               | management |              |           | events    |        |              | 382 |
| User-based                         |            | tunnels      |           | events    |        |              | 384 |
| Virtual                            | Switching  |              |           | Extension |        | (VSX) events | 392 |
| Virtual                            | Switching  |              |           | Framework |        | (VSF) events | 400 |
| VLAN                               | events     |              |           |           |        |              | 412 |
| VLAN                               | Interface  |              | events    |           |        |              | 418 |
| VRF events                         |            |              |           |           |        |              | 419 |
| VRF Manager                        |            |              | events    |           |        |              | 420 |
| VRRP                               | events     |              |           |           |        |              | 421 |
| VSX Sync                           |            | events       |           |           |        |              | 428 |
| VXLAN                              | agent      |              | events    |           |        |              | 429 |
| VXLAN                              | events     |              |           |           |        |              | 430 |
| Zero                               | touch      | provisioning |           |           | events |              | 434 |
| Support                            | and        |              | Other     | Resources |        |              | 440 |
| AccessingHPEArubaNetworkingSupport |            |              |           |           |        |              | 440 |
| AccessingUpdates                   |            |              |           |           |        |              | 441 |
|10

Aruba Support Portal
My Networking
Warranty information
Regulatory Information
Documentation feedback

441
441
441
442
442

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

11

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A, R8Q69A, R8Q70A,
R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A, JL724B, JL725B, JL726B, JL727B, JL728B,
S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,  S0M87A,  S0M88A,  S0M89A,  S0M90A,
S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A, S0X44A)

n Aruba 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B, R0X40C, R0X41A,
R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C, R0X26A, R0X27A,
JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

n Aruba 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C, JL704C, JL705C,
JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n Aruba 8400 Switch Series (JL366A, JL363A, JL687A)

n Aruba 9300 Switch Series (R9A29A, R9A30A, R8Z96A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

12

Convention

Usage

filenames, pathnames, and output displayed in a command window. Items
that appear like the example text in the previous column are to be entered
exactly as shown and are required unless enclosed in brackets ([ ]).

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:
n <example-text>
n <example-text>
n example-text

n example-text

|

{ }

[ ]

… or

...

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

Braces. Indicates that at least one of the enclosed items is required.

Brackets. Indicates that the enclosed item or items are optional.

Ellipsis:

n In code and screen examples, a vertical or horizontal ellipsis indicates an

omission of information.

n In syntax using brackets and braces, an ellipsis indicates items that can be

repeated. When an item followed by ellipses is enclosed in brackets, zero

or more items can be specified.

About the examples

Examples in this document are representative and might not match your particular switch or
environment.

The slot and port numbers in this document are for illustration only and might be unavailable on your
switch.

Understanding the CLI prompts

When illustrating the prompts in the command line interface (CLI), this document uses the generic term
switch, instead of the host name of the switch. For example:
switch>

The CLI prompt indicates the current command context. For example:
switch>

Indicates the operator command context.

switch#

Indicates the manager command context.

switch(CONTEXT-NAME)#

About this document | 13

Indicates the configuration context for a feature. For example:

switch(config-if)#

Identifies the interface context.

Variable information in CLI prompts

In certain configuration contexts, the prompt may include variable information. For example, when in
the VLAN configuration context, a VLAN number appears in the prompt:
switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 4100i Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

14

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the 83xx, 9300, and 10000 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

On the 8400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/5 and 1/6.

o Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

n port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

Identifying modular switch components

n Power supplies are on the front of the switch behind the bezel above the management modules.

Power supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format:

member/module:

About this document | 15

o member:1.
o member:1or2.
n Thedisplaymoduleontherearoftheswitchisnotlabeledwithamemberorslotnumber.
| Event Log | Message | Format |
| --------- | ------- | ------ |
Theeventlogmessagesgeneratedbyaswitchincludeitsorigin,severity,ID,modulerole,andmodule
ID.Thefollowingtableliststheeventlogmessagefieldsanditsdescriptions.
Table1:EventLogMessageFields
| Field         |     | Description                                      |
| ------------- | --- | ------------------------------------------------ |
| Messageorigin |     | Theoriginmessageoftheevent.                      |
| EventID       |     | TheuniqueeventIDofthelogmessage.                 |
| Severity      |     | Theseverityofthelogmessage.                      |
| ModuleRole    |     | Themodulerolefromwhichthelogmessagewasgenerated. |
| ModuleID      |     | ThemoduleID fromwhichthelogmessagewasgenerated.  |
| Message       |     | Theeventlogmessage.                              |
Theseverityofanyeventlogmessageindicatesthenatureoftheeventandtheactiontheuseris
requiredtoperform.Thefollowingtableliststhesupportedseveritiesanditsindications.
Table2:EventLogSeverities
| Severity | Description                      |     |
| -------- | -------------------------------- | --- |
| DEBUG    | Debugmessages                    |     |
| INFO     | Informationalmessages            |     |
| NOTICE   | Anissuewithasignificantcondition |     |
| WARN     | Warningcondition                 |     |
| ERR      | Anerrorinthesystem               |     |
| CRI      | Criticalcondition                |     |
| ALERT    | Immediateactionneeded            |     |
| EMERG    | Systemisunusable                 |     |
Listedbelowarethemodulerolesanditsdescriptionsgeneratedbytheeventlogmessages:
n AMM—ActiveManagementModule
n SMM—StandbyManagementModule
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 16

n UMM — Unassigned Management Module

n LC —Line card

For event logs generated during an early boot or when the module role is not determined by the chassis
switch, the module role will be set to UMM. After the module role is determined, the event logs are
updated with AMM or SMM.

Listed below are the module roles and its descriptions generated by the event log messages for a VSF
stack:

n CDTR—Conductor

n STBY—Standby

n MMBR—Member

n UKWN—Unknown

For event logs generated during VSF discovery or when the VSF role is not determined by the VSF stack ,
the module role will be set to UKWN. After the VSF role is determined, the event logs are updated either
with CDTR, STBY, or MMBR.

About this document | 17

Chapter 2
AAA events
AAA events
ThefollowingaretheeventsrelatedtoAAA.
Event ID: 2301
| Message  | AAA <aaa_config_type> |     | update: | <aaa_config_event> |
| -------- | --------------------- | --- | ------- | ------------------ |
| Category | AAA                   |     |         |                    |
| Severity | Information           |     |         |                    |
Description LogsAAAAuthentication/Authorization/Accounting/fail-through
Event ID: 2302
| Message  | TACACS <tacacs_type> |     | <tacacs_action>: | <tacacs_event> |
| -------- | -------------------- | --- | ---------------- | -------------- |
| Category | AAA                  |     |                  |                |
| Severity | Information          |     |                  |                |
Description LogsTACACS+serverupdate,servergroupupdateandglobaldefaultupdate
Event ID: 2303
| Message  | RADIUS <radius_type> |     | <radius_action>: | <radius_event> |
| -------- | -------------------- | --- | ---------------- | -------------- |
| Category | AAA                  |     |                  |                |
| Severity | Information          |     |                  |                |
Description LogsRADIUSserverupdate,servergroupupdateandglobaldefaultupdate
Event ID: 2304
Message RADIUS Server with Address:<server_address>, Authport:<server_
|             | authport>,                                  | VRF_ID:<server_vrfid> |     | is "<status>" |
| ----------- | ------------------------------------------- | --------------------- | --- | ------------- |
| Category    | AAA                                         |                       |     |               |
| Severity    | Information                                 |                       |     |               |
| Description | LogschangesinRADIUSserverreachabilitystatus |                       |     |               |
Event ID: 2305
18
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

TACACS server host <server_address> port <server_port> vrf <server_
vrf> <status>

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

Event ID: 2307

Message

Category

Severity

Decrypted TACACS passkey length {key_length} exceeded the maximum
allowed plaintext key length {max_key_length}

AAA

Error

Description

Decrypted TACACS server key length exceeded the maximum length allowed

AAA events | 19

Chapter 3

Accounting events

Accounting events

The following are the events related to accounting.

Event ID: 13101

Message

SSH session from {ip_address} for user {user_name} closed due to
inactivity.'

Category

Accounting

Severity

Information

Description

Logs a message when a SSH session timed out due to the session being idle

Event ID: 13102

Message

TELNET session from <ip_address> with User <user_name> timed out due
to idle timeout.

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

20

Chapter 4

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

<acl_name> on <interface_name> (<direction>): <hit_delta> <ace_
string>

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

21

Chapter 5

Alarm events

Alarm events

The following are the events related to alarm.

Event ID: 11701

Message

Input alarm <id> config change: name: <name>, relay: <relay>, log_
and_trap: <log_and_trap>, trigger: <trigger>

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

22

Message Snooze alarm activated, disabling relay function for <length> min':
yes
| Category    | Alarm                                         |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | Eventreportedwhenalarmsnoozetimerhasactivated |     |     |     |
Event ID: 11706
| Message     | Snooze alarm                                | has expired': | yes |     |
| ----------- | ------------------------------------------- | ------------- | --- | --- |
| Category    | Alarm                                       |               |     |     |
| Severity    | Information                                 |               |     |     |
| Description | Eventreportedwhenalarmsnoozetimerhasexpired |               |     |     |
Event ID: 11707
| Message     | Alarm relay                                     | function | is re-enabled': | yes |
| ----------- | ----------------------------------------------- | -------- | --------------- | --- |
| Category    | Alarm                                           |          |                 |     |
| Severity    | Information                                     |          |                 |     |
| Description | Eventreportedwhenalarmrelayfunctionisre-enabled |          |                 |     |
Event ID: 11708
Message Snooze alarm repeats, disabling relay function for <length> min': yes
| Category    | Alarm                                    |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- |
| Severity    | Information                              |     |     |     |
| Description | Eventreportedwhenalarmsnoozetimerrepeats |     |     |     |
Event ID: 11709
| Message  | System alarm | <name> has | activated | through relay |
| -------- | ------------ | ---------- | --------- | ------------- |
| Category | Alarm        |            |           |               |
| Severity | Information  |            |           |               |
Description Eventreportedwhensystemalarmhasactivatedthroughrelay
Event ID: 11710
Message Input alarm <name> has activated through relay, triggered at
Alarmevents|23

<trigger>

Category

Alarm

Severity

Information

Description

Event reported when input alarm has activated through relay

ARC events
The following are the events related to Application Recognition and Control (ARC).

Event ID: 14101

Message

Category

Severity

<log>App Recognition feature has been {status} - event_name: ARCD_LC_
STATUS_CHANGE

ARC

Info

Description

Log event that indicates global configuration for App Recognition feature

Event ID: 14102

Message

Category

Severity

Linecard {node_id} is {status} - event_name: ARCD_BULK_SYN_RECEIVE

ARC

Info

Description

linecard up event

Event ID: 14103

Message

Category

Severity

BULK SYNC event received from linecard {node_id} - event_name: ARCD_BULK_SYN_ALL_

SENT

ARC

Info

Description

Bulk sync event received

Event ID: 14104

Message

Category

Severity

BULK SYNC ALL request sent to all LC - event_name: ARCD_PUBLISHER_STATUS_CHANGE

ARC

Info

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

24

Description

bulk sync all event sent!

Event ID: 14105

Message

Category

Severity

ARCD Publisher is {status} - event_name: ARCD_FLUSH_TIMER

ARC

Info

Description

ARCD Publisher status

Event ID: 14106

Message

Category

Severity

FLUSH timer on LC {node_id} is {status}. - event_name: ARCD_OVERFLOW_HIGH_

THRESHOLD

ARC

Info

Description

flush timer start/expire status!

Event ID: 14107

Message

Category

Severity

Description

Event ID: 14108

Message

Category

Severity

Description

Event ID: 14109

IP Flow table utilization has exceeded high threshold on linecard {node_id} - event_name:

ARCD_OVERFLOW_LOW_THRESHOLD

ARC

Info

IP Flow table utilization reached high threshold on a LC

IP Flow table utilization back to lower threshold on linecard {node_id} - event_name:

ARCD_GLOBAL_STATUS_CHANGE

ARC

Info

IP Flow table utilization back to lower threshold on a LC

Message

App Recognition feature has been {status} - event_name: ARCD_FEATURE_PACK_HONOR_

MODE

ARC events | 25

Category

Severity

Description

Event ID: 14110

ARC

Info

Log event that indicates global configuration for App Recognition feature

Message

App Recognition is operating without a valid feature pack is_security_log : yes

Category

ARC

Severity

Warning

Description

Log event that indicates App Recognition feature is operating without a valid feature pack

Event ID: 14111

Message

App Recognition is blocked due to invalid or missing feature pack is_security_log : yes

Category

ARC

Severity

Warning

Description

Log event that indicates App Recognition feature is not blocked due to invalid or missing

feature pack

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

26

Chapter 6
ARP security events
| ARP security events |     |     |     |
| ------------------- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoARPsecurity.
Event ID: 10401
| Message     | ARP inspection                   | <status> | on vlan <vlan_id>. |
| ----------- | -------------------------------- | -------- | ------------------ |
| Category    | ARPsecurity                      |          |                    |
| Severity    | Information                      |          |                    |
| Description | ARPinspectionconfigurationonVLAN |          |                    |
Event ID: 10402
| Message     | ARP inspection                     | <status> | on port <port_name>. |
| ----------- | ---------------------------------- | -------- | -------------------- |
| Category    | ARPsecurity                        |          |                      |
| Severity    | Information                        |          |                      |
| Description | ARPinspectionportmodeconfiguration |          |                      |
27
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 7
|            |            |          | ASIC   | table | full error | for L3PD | events |
| ---------- | ---------- | -------- | ------ | ----- | ---------- | -------- | ------ |
| ASIC table | full error | for L3PD | events |       |            |          |        |
ThefollowingaretheeventsrelatedtoASICtablefullerrorforL3PD.
| Event ID: | 10801 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
Message Neighbor add failure due to neighbor hardware full.' throttle_count:
1
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- | --- |
| Severity |     | Error                     |     |     |     |     |     |
Description HardwaretableforNEIGHBORentriesarefull,nonewneighborswillbeadded.
| Event ID: | 10802 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
Message Route add failure due to route hardware full' throttle_count: 1
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- | --- |
| Severity |     | Error                     |     |     |     |     |     |
Description HardwaretableforROUTEentriesarefull,nonewroutewillbeadded.
| Event ID: | 10803 |                           |             |         |                  |     |     |
| --------- | ----- | ------------------------- | ----------- | ------- | ---------------- | --- | --- |
| Message   |       | Self IP add               | failure due | to self | ip hardware full |     |     |
| Category  |       | ASICtablefullerrorforL3PD |             |         |                  |     |     |
| Severity  |       | Error                     |             |         |                  |     |     |
Description HardwaretableforSELFIPentriesarefull,nonewselfipwillbeadded.
| Event ID: | 10804 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
Message Custom route prefix tables configured from customer_override.yaml
| Category |     | ASICtablefullerrorforL3PD |     |     |     |     |     |
| -------- | --- | ------------------------- | --- | --- | --- | --- | --- |
| Severity |     | Information               |     |     |     |     |     |
Description Customrouteprefixtablesconfiguredfromcustomer_override.yaml
| Event ID: | 10805 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
28
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Error parsing LIST_ROUTE_IPV4_PREFIX in customer_override.yaml file

Category

ASIC table full error for L3PD

Severity

Warning

Description

Error parsing LIST_ROUTE_IPV4_PREFIX in customer_override.yaml file

Event ID: 10806

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

ASIC table full error for L3PD events | 29

Category

ASIC table full error for L3PD

Severity

Error

Description

Logs failure while configuring hardware for ipv6 prefix-priority.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

30

Chapter 8
BFD events
BFD events
ThefollowingaretheeventsrelatedtoBFD.
Event ID: 7301
| Message     | BFD was enabled                     |     |
| ----------- | ----------------------------------- | --- |
| Category    | BFD                                 |     |
| Severity    | Information                         |     |
| Description | EventraisedwhenBFDisenabledglobally |     |
Event ID: 7302
| Message     | BFD was disabled                     |     |
| ----------- | ------------------------------------ | --- |
| Category    | BFD                                  |     |
| Severity    | Information                          |     |
| Description | EventraisedwhenBFDisdisabledglobally |     |
Event ID: 7303
| Message     | BFD echo was                            | enabled |
| ----------- | --------------------------------------- | ------- |
| Category    | BFD                                     |         |
| Severity    | Information                             |         |
| Description | EventraisedwhenBFDechoisenabledglobally |         |
Event ID: 7304
| Message     | BFD echo was                         | disabled |
| ----------- | ------------------------------------ | -------- |
| Category    | BFD                                  |          |
| Severity    | Information                          |          |
| Description | EventraisedwhenBFDisdisabledglobally |          |
Event ID: 7305
31
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | BFD echo was                                 | enabled | on interface | <intf> |     |
| ----------- | -------------------------------------------- | ------- | ------------ | ------ | --- |
| Category    | BFD                                          |         |              |        |     |
| Severity    | Information                                  |         |              |        |     |
| Description | EventraisedwhenBFDechoisenabledonaninterface |         |              |        |     |
Event ID: 7306
| Message     | BFD echo was                              | disabled | on interface | <intf> |     |
| ----------- | ----------------------------------------- | -------- | ------------ | ------ | --- |
| Category    | BFD                                       |          |              |        |     |
| Severity    | Information                               |          |              |        |     |
| Description | EventraisedwhenBFDisdisabledonaninterface |          |              |        |     |
Event ID: 7307
Message BFD session is up. session_id=<session_id>, vrf=<vrf>, op_mode=<op_
mode>, src_port=<src_port>, dest_ip=<dest_ip>, local_state=<local_
state>, local_diag=<local_diag>, remote_state=<remote_state>, remote_
diag=<remote_diag>
| Category    | BFD                                      |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                              |     |     |     |     |
| Description | EventraisedwhenaBFDsessionstatebecomesup |     |     |     |     |
Event ID: 7308
Message BFD session is down. session_id=<session_id>, vrf=<vrf>, op_mode=<op_
mode>, src_port=<src_port>, dest_ip=<dest_ip>, local_state=<local_
state>, local_diag=<local_diag>, remote_state=<remote_state>, remote_
diag=<remote_diag>
| Category    | BFD                                        |     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- |
| Severity    | Information                                |     |     |     |     |
| Description | EventraisedwhenaBFDsessionstatebecomesdown |     |     |     |     |
Event ID: 7309
Message BFD session is administratively down. session_id=<session_id>,
vrf=<vrf>, op_mode=<op_mode>, src_port=<src_port>, dest_ip=<dest_ip>,
|          | local_state=<local_state>, |     | local_diag=<local_diag>,  |     | remote_ |
| -------- | -------------------------- | --- | ------------------------- | --- | ------- |
|          | state=<remote_state>,      |     | remote_diag=<remote_diag> |     |         |
| Category | BFD                        |     |                           |     |         |
BFDevents|32

| Severity    | Information                                      |     |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- | --- |
| Description | EventraisedwhenaBFDsessionisadministrativelydown |     |     |     |     |
Event ID: 7310
| Message  | BFD session | was created | without | a source port |     |
| -------- | ----------- | ----------- | ------- | ------------- | --- |
| Category | BFD         |             |         |               |     |
| Severity | Information |             |         |               |     |
Description EventraisedwhenaBFDsessioniscreatedwithoutasourceport
Event ID: 7311
| Message  | Port <name> | can forward | BFD traffic |     |     |
| -------- | ----------- | ----------- | ----------- | --- | --- |
| Category | BFD         |             |             |     |     |
| Severity | Information |             |             |     |     |
Description EventraisedwhenaportusedbyBFDsessioncanforwardtraffic
Event ID: 7312
| Message  | Port <name> | can not forward | BFD | traffic |     |
| -------- | ----------- | --------------- | --- | ------- | --- |
| Category | BFD         |                 |     |         |     |
| Severity | Information |                 |     |         |     |
Description EventraisedwhenaportusedbyBFDsessioncannotforwardtraffic
Event ID: 7313
| Message  | BFD sessions | maximum | active capacity | reached |     |
| -------- | ------------ | ------- | --------------- | ------- | --- |
| Category | BFD          |         |                 |         |     |
| Severity | Information  |         |                 |         |     |
Description EventraisedwhenthemaximumnumberofactiveBFDsessionsisreached
Event ID: 7314
Message The echo function for the BFD session <session_id> will not become
|          | active until | a global | echo source | IP address | is configured |
| -------- | ------------ | -------- | ----------- | ---------- | ------------- |
| Category | BFD          |          |             |            |               |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 33

| Severity | Warning |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
Description EventraisedwhenanEchosessioniscreatedwithoutavalidecho_sourceIPaddress
configured
Event ID: 7315
Message BFD session is unidirectional. session_id=<session_id>, vrf=<vrf>,
op_mode=<op_mode>, src_port=<src_port>, dest_ip=<dest_ip>, local_
state=<local_state>, local_diag=<local_diag>, remote_state=<remote_
|          | state>, | remote_diag=<remote_diag> |     |     |     |
| -------- | ------- | ------------------------- | --- | --- | --- |
| Category | BFD     |                           |     |     |     |
| Severity | Error   |                           |     |     |     |
Description EventraisedwhenaBFDsessionstatebecomesunidirectional
Event ID: 7316
Message BFD echo cannot be enabled on tunnels. interface=<intf>
| Category | BFD     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
| Severity | Warning |     |     |     |     |
Description EventraisedwhenBFDechoisenabledonaTunnelinterface
Event ID: 7317
| Message  | BFD echo | is not supported | on IPv6 | sessions |     |
| -------- | -------- | ---------------- | ------- | -------- | --- |
| Category | BFD      |                  |         |          |     |
| Severity | Warning  |                  |         |          |     |
Description EventraisedwhenBFDechoisenabledforasessionusingIPv6
Event ID: 7318
Message IP Version mismatch for BFD. session_id=<session_id>, vrf=<vrf>, op_
|     | mode=<op_mode>, | src_port=<src_port>, |     | dest_ip=<dest_ip>, | local_ |
| --- | --------------- | -------------------- | --- | ------------------ | ------ |
state=<local_state>, local_diag=<local_diag>, remote_state=<remote_
state>, remote_diag=<remote_diag>, from=<from>, ip_version=<ip_
|          | version>, | Invalid | IP address: <addr> |     |     |
| -------- | --------- | ------- | ------------------ | --- | --- |
| Category | BFD       |         |                    |     |     |
| Severity | Error     |         |                    |     |     |
Description "EventraisedwhenSRCorDSTIPVersiondoesn'tmatchthesession'sIPVersion"
Event ID: 7319
BFDevents|34

| Message  | BFD single-hop | is not supported | on interface | <intf> |
| -------- | -------------- | ---------------- | ------------ | ------ |
| Category | BFD            |                  |              |        |
| Severity | Warning        |                  |              |        |
Description "EventraisedwhenaBFDsingle-hopsessionsourceportisaloopback"
Event ID: 7320
Message BFD session interval override not supported for protocol <from>
| Category | BFD     |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description "EventraisedwhenaBFDsessionspecifiesanintervalforaprotocolthatdoesnot
supportoverride"
Event ID: 7321
Message BFD session <direction> interval override of <requested_interval> ms
is out of bounds for protocol <from>, using <applied_interval> ms
instead
| Category | BFD     |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description "EventraisedwhenaBFDsessionspecifiesanintervaloutsidethespecifiedbounds"
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 35

Chapter 9
BGP events
BGP events
ThefollowingaretheeventsrelatedtoBGP.
Event ID: 2901
| Message     | <remote-addr>:                      | Peer | up. vrf-name: | <vrf-name> |
| ----------- | ----------------------------------- | ---- | ------------- | ---------- |
| Category    | BGP                                 |      |               |            |
| Severity    | Information                         |      |               |            |
| Description | LogsthechangesinBGPconnectionstate. |      |               |            |
Event ID: 2902
Message <remote-addr>: Peer down. error-code: <error-code>, error-sub-code:
|             | <error-subcode>.                           | vrf-name: | <vrf-name> |     |
| ----------- | ------------------------------------------ | --------- | ---------- | --- |
| Category    | BGP                                        |           |            |     |
| Severity    | Information                                |           |            |     |
| Description | LogsthefailureinBGPconnectionstatechanges. |           |            |     |
Event ID: 2903
Message <remote-addr>: Peer has received prefix equal to Maximum Prefix value
|          | configured. | vrf-name: | <vrf-name> |     |
| -------- | ----------- | --------- | ---------- | --- |
| Category | BGP         |           |            |     |
| Severity | Information |           |            |     |
Description Trapwhenthenumberofreceivedprefixreachesthemaximumprefixvalue.
Event ID: 2904
Message <remote-addr>: Peer has received prefix equal to Threshold value
|          | configured. | vrf-name: | <vrf-name> |     |
| -------- | ----------- | --------- | ---------- | --- |
| Category | BGP         |           |            |     |
| Severity | Information |           |            |     |
Description Trapwhenthenumberofreceivedprefixreachedthethresholdvalue.
Event ID: 2905
36
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | BGP AS <as_number>  | configured. | vrf-name: | <vrf-name> |
| ----------- | ------------------- | ----------- | --------- | ---------- |
| Category    | BGP                 |             |           |            |
| Severity    | Information         |             |           |            |
| Description | LogsBGPenableevent. |             |           |            |
Event ID: 2906
Message BGP AS <as_number> unconfigured. vrf-name: <vrf-name>
| Category    | BGP                  |     |     |     |
| ----------- | -------------------- | --- | --- | --- |
| Severity    | Information          |     |     |     |
| Description | LogsBGPdisableevent. |     |     |     |
Event ID: 2907
| Message     | BGProuter-idchanged:{ip}vrf-name:{vrf-name} |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | BGP                                         |     |     |     |
| Severity    | Information                                 |     |     |     |
| Description | LogsBGProuter-idchanged.                    |     |     |     |
Event ID: 2908
Message <remote_addr>: Peer configured, AS <remote_as>. vrf-name: <vrf-name>
| Category    | BGP                    |     |     |     |
| ----------- | ---------------------- | --- | --- | --- |
| Severity    | Information            |     |     |     |
| Description | LogscreationofBGPpeer. |     |     |     |
Event ID: 2909
Message <remote_addr>: User reset request. vrf-name: <vrf-name>
| Category    | BGP                           |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Severity    | Information                   |     |     |     |
| Description | LogsBGPpeersessionresetevent. |     |     |     |
Event ID: 2910
Message <remote_addr>: Peer password changed. vrf-name: <vrf-name>
BGPevents|37

| Category    | BGP                             |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- |
| Severity    | Information                     |     |     |     |
| Description | LogsBGPpeerpasswordchangeevent. |     |     |     |
Event ID: 2911
| Message     | <remote_addr>:         | Peer deleted. | vrf-name: | <vrf-name> |
| ----------- | ---------------------- | ------------- | --------- | ---------- |
| Category    | BGP                    |               |           |            |
| Severity    | Information            |               |           |            |
| Description | LogsdeletionofBGPpeer. |               |           |            |
Event ID: 2912
Message <remote_addr>: Peer admin disabled. vrf-name: <vrf-name>
| Category    | BGP                          |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Information                  |     |     |     |
| Description | LogsBGPpeeradmindisableevent |     |     |     |
Event ID: 2913
Message <remote_addr>: Peer admin enabled. vrf-name: <vrf-name>
| Category    | BGP                          |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Information                  |     |     |     |
| Description | LogsBGPpeeradminenableevent. |     |     |     |
Event ID: 2914
Message <remote_addr>: Peer remote-as changed to <remote_as>. vrf-name: <vrf-
name>
| Category    | BGP                              |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- |
| Severity    | Information                      |     |     |     |
| Description | LogsBGPpeerremote-aschangeevent. |     |     |     |
Event ID: 2915
Message <remote_addr>: Peer local-as changed to <local_as>. vrf-name: <vrf-
name>
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 38

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

<remote_addr>: Peer remove-private-as configuration changed. vrf-
name: <vrf-name>

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

Event ID: 2919

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

BGP events | 39

Message <pg_name>: Peer-group configured with remote-as <remote_as>. vrf-
name: <vrf-name>
| Category    | BGP                                           |     |
| ----------- | --------------------------------------------- | --- |
| Severity    | Information                                   |     |
| Description | LogsBGPpeer-groupremote-asconfigurationevent. |     |
Event ID: 2921
Message <remote_addr>: Peer ignore-leading-as configuration changed. vrf-
name: <vrf-name>
| Category    | BGP                                       |     |
| ----------- | ----------------------------------------- | --- |
| Severity    | Information                               |     |
| Description | Logsconfigurationofpeerignore-leading-as. |     |
Event ID: 2922
Message {remote_addr}:NeighboraddedtoPeergroup{peer-grp}vrf-name:{vrf-name}
| Category    | BGP                              |     |
| ----------- | -------------------------------- | --- |
| Severity    | Information                      |     |
| Description | Logsneighboradditiontopeergroup. |     |
Event ID: 2923
Message
{remote_addr}:NeighbordeletedfromPeergroup{peer-grp}vrf-name:{vrf-name}
| Category | BGP         |     |
| -------- | ----------- | --- |
| Severity | Information |     |
Description
Logsneighbordeletionfrompeergrou
Event ID: 2924
Message Logsifdynamictunnelbridgingmodeibgp-ebgpwasenabledandbroadcastgroupis
beingconfiguredinaroute-map.
| Category | BGP   |     |
| -------- | ----- | --- |
| Severity | Error |     |
Description Dynamictunnelbridgingibgp-ebgpmodeisenabled,Pleasedisableit.
| Bidirectional | PIM (PIM-BIDI) | events |
| ------------- | -------------- | ------ |
bi-directional
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 40

The following are the events related to bidirectional PIM.

Event ID: 15301

Message

Router pim {status} on vrf {vrf_name}

Category

Bidirectional PIM

Severity

Information

Description

This log event informs about router PIM status of a VRF.

Event ID: 15302

Message

Interface {if_name} state {state}

Category

Bidirectional PIM

Severity

Information

Description

This log event informs about interface status

Event ID: 15303

Message

Dropping Packet on interface {if_index}, Due to {reason}

Category

Bidirectional PIM

Severity

Error

Description

This log event informs about dropping packet

Event ID: 15304

Message

PIM Bidi {state} on Interface {if_name}

Category

Bidirectional PIM

Severity

Information

Description

This log event informs about PIM Bidi state on interface

Event ID: 15305

Message

PIM Bidi Neighbor {ip_address} is {state} on Interface {if_name}

Category

Bidirectional PIM

Severity

Information

Description

This log event informs about the creation and deletion of a PIM Bidi Neighbor

Bidirectional PIM (PIM-BIDI) events | 41

Chapter 10
|           |            |        | Bluetooth | Management | events |
| --------- | ---------- | ------ | --------- | ---------- | ------ |
| Bluetooth | Management | events |           |            |        |
ThefollowingaretheeventsrelatedtoBluetoothmanagement.
| Event ID: | 8001      |          |                    |     |     |
| --------- | --------- | -------- | ------------------ | --- | --- |
| Message   | Bluetooth | has been | <enabled_disabled> |     |     |
Category BluetoothManagement
Severity Information
Description EventraisedwhenBluetoothisenabledordisabled
| Event ID: | 8002      |        |                  |        |     |
| --------- | --------- | ------ | ---------------- | ------ | --- |
| Message   | Bluetooth | unable | to trust pairing | device |     |
Category BluetoothManagement
Severity Warning
Description EventraisedwhenBluetoothisunabletotrustpairingdevice
| Event ID: | 8003      |         |                    |     |     |
| --------- | --------- | ------- | ------------------ | --- | --- |
| Message   | Bluetooth | adapter | <inserted_removed> |     |     |
Category BluetoothManagement
Severity Information
Description EventraisedwhenbtdreceivessignalforBluetoothadapterevent
| Event ID: | 8004 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Bluetooth device <connected_disconnected>: <mac_address>
Category BluetoothManagement
Severity Information
Description EventraisedwhenbtdreceivessignalforBluetoothdeviceevent
| Event ID: | 8005 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
42
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Bluetooth device rejected because another device is already connected

Category

Bluetooth Management

Severity

Warning

Description

Event raised when btd disconnects a newly paried device because another device is
already connected

Bluetooth Management events | 43

Chapter 11
CDP events
CDP events
ThefollowingaretheeventsrelatedtoCDP.
Event ID: 8901
| Message     | CDP Enabled    |     |     |
| ----------- | -------------- | --- | --- |
| Category    | CDP            |     |     |
| Severity    | Information    |     |     |
| Description | LogsCDPenabled |     |     |
Event ID: 8902
| Message     | CDP Disabled   |     |     |
| ----------- | -------------- | --- | --- |
| Category    | CDP            |     |     |
| Severity    | Information    |     |     |
| Description | LogsCDPdisbled |     |     |
Event ID: 8903
| Message     | CDP neighbor                     | <mac> is added | on <interface> |
| ----------- | -------------------------------- | -------------- | -------------- |
| Category    | CDP                              |                |                |
| Severity    | Information                      |                |                |
| Description | LogtoindicateCDPneighboraddition |                |                |
Event ID: 8904
Message CDP neighbor <mac> is updated on <interface>' throttle_count: 100
| Category    | CDP                                   |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Information                           |     |     |
| Description | LogtoindicateCDPneighbourmodification |     |     |
Event ID: 8905
44
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | CDP                                      | neighbor <mac> | is deleted   | on <interface> |
| ----------- | ---------------------------------------- | -------------- | ------------ | -------------- |
| Category    | CDP                                      |                |              |                |
| Severity    | Information                              |                |              |                |
| Description | LogtoindicateCDPneighbordeletion         |                |              |                |
| Event ID:   | 8906                                     |                |              |                |
| Message     | All                                      | CDP neighbor   | info cleared |                |
| Category    | CDP                                      |                |              |                |
| Severity    | Information                              |                |              |                |
| Description | LogtoindicateallCDPneighborinfoiscleared |                |              |                |
| Central     | Source                                   | events         |              |                |
ThefollowingaretheeventsrelatedtoanArubaCentralsource.
| Event ID: | 14601 |     |     |     |
| --------- | ----- | --- | --- | --- |
Message ArubaActivateserver{activate_address}isreachableviaVRF{vrf}.
| Category    | CENTRALSOURCE                                 |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Info                                          |     |     |     |
| Description | ArubaActivateserverisreachableviaanactiveVRF. |     |     |     |
| Event ID:   | 14602                                         |     |     |     |
Message
eceivedcertificatefromArubaActivateserver,processingwithcertificatemanager.
Certificatelength:{cert_length}.
| Category | CENTRALSOURCE |     |     |     |
| -------- | ------------- | --- | --- | --- |
| Severity | Info          |     |     |     |
Description
ArubaActivateserversentaCAcertificatetobeinstalled.
| Event ID: | 14603 |     |     |     |
| --------- | ----- | --- | --- | --- |
Message ArubaCentrallocation{central_location}successfullyfetchedfrom{central_source}via
VRF{vrf}
| Category | CENTRALSOURCE |     |     |     |
| -------- | ------------- | --- | --- | --- |
| Severity | Info          |     |     |     |
CentralSourceevents|45

Description ArubaCentrallocationsuccessfullyfetchedfromCentralSource(CLI/DHCP/Aruba
ActivateServer)viaVRF.
| Event ID: | 14604 |     |
| --------- | ----- | --- |
Message UnabletofetchArubaCentrallocationfromCentralSource(CLI/DHCP/ArubaActivate
Server).
| Category | CENTRALSOURCE |     |
| -------- | ------------- | --- |
| Severity | Info          |     |
Description UnabletofetchArubaCentrallocation{central_location}from{central_source}viaVRF
{vrf}.
| Event ID: | 14605                                      |     |
| --------- | ------------------------------------------ | --- |
| Message   | SwitchtimeissyncedwithArubaActivateServer. |     |
| Category  | CENTRALSOURCE                              |     |
| Severity  | Info                                       |     |
Description SwitchtimeissyncedwithArubaActivateServer{activate_address}.
| Event ID: | 14606 |     |
| --------- | ----- | --- |
Message
SwitchtimeissyncedwithNTPServers.
| Category | CENTRALSOURCE |     |
| -------- | ------------- | --- |
| Severity | Info          |     |
Description
SwitchtimeissyncedwithNTPServers.
| Client | insight | events |
| ------ | ------- | ------ |
Thefollowingaretheeventsrelatedtoclientinsight.
| Event ID: | 14301 |     |
| --------- | ----- | --- |
Message Client{mac}successfullyon-boardedonVLAN{vlans}.Clienton-boardingstartedat{ob_
start_ts};L2completeat{l2_end_ts};L3completeat{l3_end_ts}is_security_log:no
| Category    | ClientInsight               |     |
| ----------- | --------------------------- | --- |
| Severity    | Information                 |     |
| Description | Clienton-boardingsuccessful |     |
| Event ID:   | 14302                       |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 46

Message

Client {mac} partial success while on-boarding on VLAN {vlans}. L2 status:{l2_ob_state} L3

status:{l3_ob_state}. Client on-boarding started at {ob_start_ts};L2 complete at {l2_end_

ts}; L3 complete at {l3_end_ts}. is_security_log : no

Category

Client Insight

Severity

Information

Description

Client on-boarding partially success

Event ID: 14303

Message

Client {mac} failed to on-board with status: {onboarding_status} reason_code: {failure_

phase_id} is_security_log : no

Category

Client Insight

Severity

Information

Description

Client on-boarding failed

Event ID: 14304

Message

Maximum system wide client limit {client-number} reached. throttle_time : 15 throttle_

count : 1 is_security_log: no

Category

Client Insight

Severity

Information

Description

Maximum system wide client limit reached

Event ID: 14305

Message

Client {mac} successfully on-boarded on VLAN {vlans}; Client on-boarding started at {ob_

start_ts}; L2 complete at {l2_end_ts}; L3 complete at {l3_end_ts}; ARP to GW response

received at {arp_end_ts}; DNS on-boarding to {dns_server_ip} completed at {dns_end_ts}
is_security_log : no

Category

Client Insight

Severity

Information

Description

Client on-boarding successful

Event ID: 14306

Message

Client {mac} on-boarded on VLANs {vlans} and failed on VLANs {failed_vlans}; Client on-

boarding started at {ob_start_ts}; L2 complete at {l2_end_ts}; L3 complete at {l3_end_ts};

ARP to GW response received at {arp_end_ts}; DNS on-boarding to {dns_server_ip}

Client insight events | 47

completed at {dns_end_ts}; L2 status {l2_ob_state} failure_reason_code - {l2_failure_

reason}; L3 status {l3_ob_state} failure_reason_code - {l3_failure_reason}; DNS on-

boarding status {dns_status} failure_reason_code - {dns_failure_reason}

Category

Client Insight

Severity

Information

Description

Client on-boarding partially success

Event ID: 14307

Message

Client {mac} failed to on-board with status: {onboarding_status} in failure phase: {failure_

phase_id} with reason: {failure_reason} is_security_log : no

Category

Client Insight

Severity

Information

Description

Client on-boarding failed

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

48

Chapter 12
|             |            |        | Certificate | management | events |
| ----------- | ---------- | ------ | ----------- | ---------- | ------ |
| Certificate | management | events |             |            |        |
Thefollowingaretheeventsrelatedtocertificatemanagement.
| Event ID:   | 7701                                      |                    |          |     |     |
| ----------- | ----------------------------------------- | ------------------ | -------- | --- | --- |
| Message     | TA Profile                                | <name> created     |          |     |     |
| Category    | Certificatemanagement                     |                    |          |     |     |
| Severity    | Information                               |                    |          |     |     |
| Description | Eventraisedwhenataprofileiscreated        |                    |          |     |     |
| Event ID:   | 7702                                      |                    |          |     |     |
| Message     | TA Profile                                | <name> deleted     |          |     |     |
| Category    | Certificatemanagement                     |                    |          |     |     |
| Severity    | Information                               |                    |          |     |     |
| Description | Eventraisedwhenataprofileisremoved        |                    |          |     |     |
| Event ID:   | 7703                                      |                    |          |     |     |
| Message     | Leaf                                      | certificate <name> | imported |     |     |
| Category    | Certificatemanagement                     |                    |          |     |     |
| Severity    | Information                               |                    |          |     |     |
| Description | Eventraisedwhenaleafcertificateisimported |                    |          |     |     |
| Event ID:   | 7704                                      |                    |          |     |     |
| Message     | Leaf                                      | certificate <name> | deleted  |     |     |
| Category    | Certificatemanagement                     |                    |          |     |     |
| Severity    | Information                               |                    |          |     |     |
| Description | Eventraisedwhenaleafcertificateisdeleted  |                    |          |     |     |
| Event ID:   | 7705                                      |                    |          |     |     |
49
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | Certificate           | <name> will | expire within | <days> days |
| -------- | --------------------- | ----------- | ------------- | ----------- |
| Category | Certificatemanagement |             |               |             |
| Severity | Warning               |             |               |             |
Description Eventraisedwhenaninstalledcertifiatewillexpirewithin60days
Event ID: 7706
Message Certificate <name> has not yet reached its start date
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Warning               |     |     |     |
Description Eventraisedwhenaninstalledcertifiateisnotyetpastitsstartdate
Event ID: 7707
Message Certificate <name> has expired and can no longer be used
| Category    | Certificatemanagement                          |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                        |     |     |     |
| Description | Eventraisedwhenaninstalledcertifiatehasexpired |     |     |     |
Event ID: 7708
Message Certificate <name> verified and accepted' throttle_count: 100
| Category    | Certificatemanagement                      |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Information                                |     |     |     |
| Description | Eventraisedwhenacertificatechainisverified |     |     |     |
Event ID: 7709
Message Certificate <name> rejected due to verification failure (<error>)'
|             | throttle_count:                            | 100 |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Category    | Certificatemanagement                      |     |     |     |
| Severity    | Warning                                    |     |     |     |
| Description | Eventraisedwhenacertificatechainisrejected |     |     |     |
Event ID: 7710
Certificatemanagementevents|50

| Message  | Certificate           | signing request | <name> created |
| -------- | --------------------- | --------------- | -------------- |
| Category | Certificatemanagement |                 |                |
| Severity | Information           |                 |                |
Description Eventraisedwhenacertificatesigningrequestiscreatedontheswitch
Event ID: 7711
| Message  | Self-signed           | certificate | <name> created |
| -------- | --------------------- | ----------- | -------------- |
| Category | Certificatemanagement |             |                |
| Severity | Information           |             |                |
Description Eventraisedwhenaself-signedcertificateiscreatedontheswitch
Event ID: 7712
Message Application association with the <name> certificate is not permitted
| Category | Certificatemanagement |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Error                 |     |     |
Description Eventraisedwhenaninvalidcertificateassociationismade
Event ID: 7713
Message Certificate <name> failed OCSP verification (<status>), but was
accepted because OCSP enforcement is set to optional.' throttle_
count: 100
| Category | Certificatemanagement |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Warning               |     |     |
Description EventraisedwhenacertificateisverifiedduetooptionalOCSPenforcement
Event ID: 7714
Message CA certificates successfully downloaded from EST server <name>
| Category | Certificatemanagement |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Information           |     |     |
Description EventraisedwhenCAcertificatesweresuccessfullydownloadedfromanESTserver
Event ID: 7715
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 51

Message Failed to download CA certificates from EST server <name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Error                 |     |     |     |
Description EventraisedwhenCAcertificatescouldnotbedownloadedfromanESTserver
Event ID: 7716
Message Certificate <name> successfully enrolled by EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description EventraisedwhenacertificateissuccessfullyenrolledwithEST
Event ID: 7717
Message Failed to enroll certificate <name> with EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Error                 |     |     |     |
Description EventraisedwhencertificateenrollmentwithanESTserverfails
Event ID: 7718
Message Certificate <name> successfully reenrolled by EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description EventraisedwhenacertificateissuccessfullyreenrolledwithEST
Event ID: 7719
Message Failed to reenroll certificate <name> with EST server <est_name>
| Category | Certificatemanagement |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Error                 |     |     |     |
Description EventraisedwhencertificatereenrollmentwithanESTserverfails
Event ID: 7720
| Message | Certificate | <name> | is not set for | signing purpose |
| ------- | ----------- | ------ | -------------- | --------------- |
Certificatemanagementevents|52

| Category    | Certificatemanagement                              |     |     |     |
| ----------- | -------------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                            |     |     |     |
| Description | Eventraisedwhenasignercertifiateisnotsetforsigning |     |     |     |
Event ID: 7721
| Message  | Certificate           | <name> | is invalid | or malformed |
| -------- | --------------------- | ------ | ---------- | ------------ |
| Category | Certificatemanagement |        |            |              |
| Severity | Warning               |        |            |              |
Description Eventraisedwhenaninstalledcertifiateisinvalidormalformed
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 53

Chapter 13
|                   |        |     | Config | Management | events |
| ----------------- | ------ | --- | ------ | ---------- | ------ |
| Config Management | events |     |        |            |        |
Thefollowingaretheeventsrelatedtoconfigmanagement.
Event ID: 6801
| Message  | Copying configs  | from: <from> | to: <to> |     |     |
| -------- | ---------------- | ------------ | -------- | --- | --- |
| Category | ConfigManagement |              |          |     |     |
| Severity | Information      |              |          |     |     |
Description Logsamessagewhenconfigscopyingfromoneformattoanother
Event ID: 6802
| Message     | Error while                               | copying configs. | Error: <error> |     |     |
| ----------- | ----------------------------------------- | ---------------- | -------------- | --- | --- |
| Category    | ConfigManagement                          |                  |                |     |     |
| Severity    | Error                                     |                  |                |     |     |
| Description | Logsamessagewhencopyingconfighassomeerror |                  |                |     |     |
Event ID: 6803
| Message  | <type>:<value>   |     |     |     |     |
| -------- | ---------------- | --- | --- | --- | --- |
| Category | ConfigManagement |     |     |     |     |
| Severity | Information      |     |     |     |     |
Description Logsamessagewhenconfigvalidationprunestables/columnsinstartup-configorwhen
errorsareencountered
Event ID: 6804
| Message  | Error while      | copying configs. | Error: <error> |     |     |
| -------- | ---------------- | ---------------- | -------------- | --- | --- |
| Category | ConfigManagement |                  |                |     |     |
| Severity | Error            |                  |                |     |     |
Description Logsamessagewhencopyingconfigtoshadowdbhassomeerror
Event ID: 6805
54
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message | Information | while copying | configs. Info: | <info> |
| ------- | ----------- | ------------- | -------------- | ------ |
Category ConfigManagement
Severity Information
Description Logsamessagewhencopyingconfighassomeinformation
| Config | validator | events |     |     |
| ------ | --------- | ------ | --- | --- |
Thefollowingaretheeventsrelatedtoconfigurationvalidation.
| Event ID: | 13401 |     |     |     |
| --------- | ----- | --- | --- | --- |
Message Config{name}failedtovalidate.Reason{reason}
Category ConfigValidator
Severity Error
Description Failedtovalidateconfiguration
Configvalidatorevents|55

Chapter 14
|              | Connectivity     | Fault Management | (CFM) events |
| ------------ | ---------------- | ---------------- | ------------ |
| Connectivity | Fault Management | (CFM) events     |              |
ThefollowingaretheeventsrelatedtoConnectivityFaultManagement(CFM).
| Event ID: 11601 |     |     |     |
| --------------- | --- | --- | --- |
Message Connection lost for Maintenance Endpoint <id> on <interface>.
| Category | ConnectivityFaultManagement(CFM) |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Error                            |     |     |
Description EventreportedwhenconnectionislostontheMaintanenceEndpoint.
| Event ID: 11602 |     |     |     |
| --------------- | --- | --- | --- |
Message Connection restored for Maintenance Endpoint <id> on <interface>.
| Category | ConnectivityFaultManagement(CFM) |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description EventreportedwhenconnectionisrestoredontheMaintanenceEndpoint.
56
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 15

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

Event ID: 13004

Message

Category

Severity

Description

Event ID: 13005

CONSOLE session from User <user_name> is closed because maximum
number of sessions per user is reached.

Console

Warning

Logs a message when a user tries to login while maximum number of sessions per user
are reached.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

57

Message

Category

Severity

Description

User {user_name} login from {ip_address} for CONSOLE session has
failed since the user is trying to login through an interface which
is not allowed. Allowed interfaces are: {mgmt_intf}

Console

Warning

Logs a message when a user login fails since the access through this management
interface is not allowed

Console events | 58

Chapter 16
|           |         |        |     | Container | manager | events |
| --------- | ------- | ------ | --- | --------- | ------- | ------ |
| Container | manager | events |     |           |         |        |
Thefollowingaretheeventsrelatedtocontainermanager.
| Event ID:   | 11801 |                                         |                |     |     |     |
| ----------- | ----- | --------------------------------------- | -------------- | --- | --- | --- |
| Message     |       | Container <name>                        | is created     |     |     |     |
| Category    |       | Containermanager                        |                |     |     |     |
| Severity    |       | Information                             |                |     |     |     |
| Description |       | Eventreportedwhencontaineriscreated     |                |     |     |     |
| Event ID:   | 11802 |                                         |                |     |     |     |
| Message     |       | Container <name>                        | is removed     |     |     |     |
| Category    |       | Containermanager                        |                |     |     |     |
| Severity    |       | Information                             |                |     |     |     |
| Description |       | Eventreportedwhencontainerisremoved     |                |     |     |     |
| Event ID:   | 11803 |                                         |                |     |     |     |
| Message     |       | Container <name>                        | is operational |     |     |     |
| Category    |       | Containermanager                        |                |     |     |     |
| Severity    |       | Information                             |                |     |     |     |
| Description |       | Eventreportedwhencontainerisoperational |                |     |     |     |
| Event ID:   | 11804 |                                         |                |     |     |     |
Message Endpoint has been executed for container {name} with parameters:
{params}
| Category |     | Containermanager |     |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- | --- |
| Severity |     | Information      |     |     |     |     |
Description Eventreportedwhencontainerexeccommandhasbeenrunwithadditionalparameters.
| Event ID: | 11805 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
59
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Endpoint has been executed for container {name} with no parameters.

Category

Container manager

Severity

Information

Description

Event reported when container exec command has been run with no parameters.

Container manager events | 60

Chapter 17
CoPP events
CoPP events
Thefollowingaretheeventsrelatedtocontrolplanepolicing.
Event ID: 1501
| Message     | COPP initialization            |     | failed |
| ----------- | ------------------------------ | --- | ------ |
| Category    | CoPP                           |     |        |
| Severity    | Error                          |     |        |
| Description | LogsCOPPinitializationfailure. |     |        |
Event ID: 1502
| Message     | COPP initialization            |     | successful |
| ----------- | ------------------------------ | --- | ---------- |
| Category    | CoPP                           |     |            |
| Severity    | Information                    |     |            |
| Description | LogsCOPPinitializationsuccess. |     |            |
Event ID: 1503
| Message     | Ingress                                        | FP Group | create failed |
| ----------- | ---------------------------------------------- | -------- | ------------- |
| Category    | CoPP                                           |          |               |
| Severity    | Error                                          |          |               |
| Description | Logsingressfieldprocessorgroupcreationfailure. |          |               |
Event ID: 1504
| Message     | Egress                                        | FP Group create | failed |
| ----------- | --------------------------------------------- | --------------- | ------ |
| Category    | CoPP                                          |                 |        |
| Severity    | Error                                         |                 |        |
| Description | Logsegressfieldprocessorgroupcreationfailure. |                 |        |
Event ID: 1505
61
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Programming                                  | defaults failed |     |     |
| ----------- | -------------------------------------------- | --------------- | --- | --- |
| Category    | CoPP                                         |                 |     |     |
| Severity    | Error                                        |                 |     |     |
| Description | Logsfailureforinitializationofdefaultvalues. |                 |     |     |
Event ID: 1506
| Message  | Packet | class programming | failed for | <class> |
| -------- | ------ | ----------------- | ---------- | ------- |
| Category | CoPP   |                   |            |         |
| Severity | Error  |                   |            |         |
Description LogsfailureofprogrammingqueueforaCoPPpacketclass.
Event ID: 1507
Message Failed to program ingress field processor rule for <class>
| Category | CoPP  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description LogsfailureofprogrammingingressfieldprocessorforaCOPPclass.
Event ID: 1508
| Message  | Failed | to program egress | rule for | <class> |
| -------- | ------ | ----------------- | -------- | ------- |
| Category | CoPP   |                   |          |         |
| Severity | Error  |                   |          |         |
Description LogsfailureofprogrammingegressfieldprocessorforaCOPPclass.
Event ID: 1509
| Message     | CoPP initial                                 | initialization | failed | on slot <slot> |
| ----------- | -------------------------------------------- | -------------- | ------ | -------------- |
| Category    | CoPP                                         |                |        |                |
| Severity    | Error                                        |                |        |                |
| Description | LogsCoPPinitialinitializationfailureonaslot. |                |        |                |
Event ID: 1510
| Message | CoPP final | initialization | failed | on slot <slot> |
| ------- | ---------- | -------------- | ------ | -------------- |
CoPPevents|62

| Category    | CoPP                                       |     |     |
| ----------- | ------------------------------------------ | --- | --- |
| Severity    | Error                                      |     |     |
| Description | LogsCoPPfinalinitializationfailureonaslot. |     |     |
Event ID: 1511
| Message     | CoPP deinitialization                   | failed | on slot <slot> |
| ----------- | --------------------------------------- | ------ | -------------- |
| Category    | CoPP                                    |        |                |
| Severity    | Error                                   |        |                |
| Description | LogsCoPPdeinitializationfailureonaslot. |        |                |
Event ID: 1512
Message Failed to configure hardware for CoPP on slot <slot> class <class>
| Category | CoPP  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description LogsfailurewhileconfiguringhardwareonaslotforaCoPPclass.
Event ID: 1513
Message Failed to retrieve CoPP statistics from slot <slot> class <class>
| Category | CoPP  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description LogsfailurewhileretrievingstatisticsonaslotforaCoPPclass.
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 63

Chapter 18

CPU_RX events

CPU_RX events

The following are the events related to CPU_RX.

Event ID: 7501

Message

Kernel filter "<action>" failed on unit <unit> for <filter_
description>

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

64

Chapter 19
|            |         |        |     | Credential | Manager | events |
| ---------- | ------- | ------ | --- | ---------- | ------- | ------ |
| Credential | Manager | events |     |            |         |        |
Thefollowingaretheeventsrelatedtocredentialmanager.
| Event ID: | 6501 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message An internal error occurred while reading the export password and
|          |     | default export    | password was | used instead. |     |     |
| -------- | --- | ----------------- | ------------ | ------------- | --- | --- |
| Category |     | CredentialManager |              |               |     |     |
| Severity |     | Warning           |              |               |     |     |
Description Warnstheuserthatexportpasswordfilewascorruptedanddefaultpasswdwasused
instead.
| Event ID: | 6502 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message A critical system file has been corrupted. Please configure your
export password to the one used by your most recent configuration
|          |     | export and import | your most | recent configuration. |     |     |
| -------- | --- | ----------------- | --------- | --------------------- | --- | --- |
| Category |     | CredentialManager |           |                       |     |     |
| Severity |     | Warning           |           |                       |     |     |
Description Warnstheuserthatthechassissecrethasbeencorrupted.
| Event ID: | 6504 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Self-signed certificate successfully created for the https-server.
| Category |     | CredentialManager |     |     |     |     |
| -------- | --- | ----------------- | --- | --- | --- | --- |
| Severity |     | Information       |     |     |     |     |
Description Logsamessagewhentheself-signedcertiscreatedbycredmgr.
| Event ID: | 6505 |                     |         |                |     |     |
| --------- | ---- | ------------------- | ------- | -------------- | --- | --- |
| Message   |      | User admin password | changed | from ServiceOS |     |     |
| Category  |      | CredentialManager   |         |                |     |     |
| Severity  |      | Information         |         |                |     |     |
Description LogsamessagewhenauserchangesadminpasswordfromServiceOS
| Event ID: | 6506 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
65
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | SSH authorized    | keys | were added | for user <user> |     |
| -------- | ----------------- | ---- | ---------- | --------------- | --- |
| Category | CredentialManager |      |            |                 |     |
| Severity | Information       |      |            |                 |     |
Description LogsamessagewhenSSHauthorizedkeysareaddedforauser
Event ID: 6507
| Message  | Failed            | to write SSH | authorized | keys for user | <user> |
| -------- | ----------------- | ------------ | ---------- | ------------- | ------ |
| Category | CredentialManager |              |            |               |        |
| Severity | Error             |              |            |               |        |
Description LogsamessageafterafailuretowriteSSHauthorizedkeysforauser
Event ID: 6508
| Message  | SSH authorized    | keys | deleted | for user <user> |     |
| -------- | ----------------- | ---- | ------- | --------------- | --- |
| Category | CredentialManager |      |         |                 |     |
| Severity | Information       |      |         |                 |     |
Description LogsamessageaftedeletingSSHauthorizedkeysforauser
Event ID: 6509
Message User <user> has configured an invalid SSH authorized key with key
|          | identifier        | <key-id> |     |     |     |
| -------- | ----------------- | -------- | --- | --- | --- |
| Category | CredentialManager |          |     |     |     |
| Severity | Error             |          |     |     |     |
Description LogsamessagewhenSSHauthorizedkeyfailsvalidationchack
| CX LMS events |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoAOS-CXFeaturePackmanagement.
Event ID: 15001
Message Featurepackcloud-managedmodeisenabled,LMSserverwillbeusedforfeaturepack
management
| Category | CX_LMS      |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
| Severity | Information |     |     |     |     |
Description
Eventraisedwhenthefeaturepackmanagamentmodeissettocloud-managed
CXLMSevents|66

Event ID: 15002

Message

Feature pack cloud-managed mode is disabled, LMS server will no longer be used for

feature pack management

Category

CX_LMS

Severity

Information

Description

Event raised when the feature pack managament mode is set to anything different from

cloud-managed

Event ID: 15003

Message

Feature pack validation with the LMS server triggered

Category

CX_LMS

Severity

Information

Description

Event raised when a new feature pack validation process using LMS server is triggered

Event ID: 15004

Message

CX-LMS has successfully installed a new feature pack file in the system

Category

CX_LMS

Severity

Information

Description

Event raised when CX-LMS succesfully installs a new feature pack file in the switch.

Event ID: 15005

Message

CX-LMS has successfully validated the system license

Category

CX_LMS

Severity

Information

Description

Event raised when CX-LMS succesfully validates the feature pack in the switch.

Event ID: 15006

Message

CX-LMS failed to validate the system license

Category

CX_LMS

Severity

Error

Description

Event raised when CX-LMS fails to validate a feature pack for the switch.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

67

Chapter 20

Device fingerprinting events

Device fingerprinting events

The following are the events related to device fingerprinting.

Event ID: 12401

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

Event ID: 12402

Message

Reached the maximum clients limit of <client_limit> on the interface
<interface> for device fingerprinting.

Category

Device fingerprinting

Severity

Warning

Description

Log the event when the per port clients limit for device fingerprinting is reached.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

68

Chapter 21
DHCP Relay events
| DHCP Relay events |     |     |
| ----------------- | --- | --- |
ThefollowingaretheeventsrelatedtoDHCPrelay.
Event ID: 3401
| Message  | DHCP Relay  | Enabled |
| -------- | ----------- | ------- |
| Category | DHCPRelay   |         |
| Severity | Information |         |
Description ThiscommandenablestheDHCPRelayfeatureinthedevice.
Event ID: 3402
| Message  | DHCP Relay  | Disabled |
| -------- | ----------- | -------- |
| Category | DHCPRelay   |          |
| Severity | Information |          |
Description ThiscommanddisablestheDHCPRelayfeatureinthedevice.
69
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 22

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

DHCP Lease addition failed <expiry_time> <mac> <ip> <host> <client_
id>

Category

DHCP server

Severity

Error

Description

Logs failure in DHCP lease addition

Event ID: 1905

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

70

Message DHCP Lease deletion failed <expiry_time> <mac> <ip> <host> <client_
id>
| Category    | DHCPserver                     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | LogsfailureinDHCPleasedeletion |     |     |     |
Event ID: 1906
Message DHCP Lease update failed <expiry_time> <mac> <ip> <host> <client_id>
| Category    | DHCPserver                     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | LogsfailureinDHCPleaseupdation |     |     |     |
Event ID: 1907
| Message     | DHCP server                                  | enabled | on VRF <vrf_name> |     |
| ----------- | -------------------------------------------- | ------- | ----------------- | --- |
| Category    | DHCPserver                                   |         |                   |     |
| Severity    | Information                                  |         |                   |     |
| Description | EventraisedwhenDHCPservergetsenabledontheVRF |         |                   |     |
Event ID: 1908
| Message     | DHCP server                                   | disabled | on VRF <vrf_name> |     |
| ----------- | --------------------------------------------- | -------- | ----------------- | --- |
| Category    | DHCPserver                                    |          |                   |     |
| Severity    | Information                                   |          |                   |     |
| Description | EventraisedwhenDHCPservergetsdisabledontheVRF |          |                   |     |
Event ID: 1909
Message Invalid DHCP configuration: <config> provided on DHCP Server instance
|          | running    | on VRF <vrf_name>. | Ignoring this | config. |
| -------- | ---------- | ------------------ | ------------- | ------- |
| Category | DHCPserver |                    |               |         |
| Severity | Error      |                    |               |         |
Description EventraisedwhenuserconfiguresaninvalidDHCPconfiguration
Event ID: 1910
DHCPserverevents|71

| Message     | DHCP Server                                     | Lease cleared | on vrf <vrf>. |
| ----------- | ----------------------------------------------- | ------------- | ------------- |
| Category    | DHCPserver                                      |               |               |
| Severity    | Information                                     |               |               |
| Description | EventraisedwhenDHCPServerLeaseontheVRFiscleared |               |               |
Event ID: 1911
| Message  | DHCPv6 Server | Lease cleared | on vrf <vrf>. |
| -------- | ------------- | ------------- | ------------- |
| Category | DHCPserver    |               |               |
| Severity | Information   |               |               |
Description EventraisedwhenDHCPv6ServerLeaseontheVRFiscleared
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 72

Chapter 23
|        |          |        | DHCPv4 | snooping | events |
| ------ | -------- | ------ | ------ | -------- | ------ |
| DHCPv4 | snooping | events |        |          |        |
ThefollowingaretheeventsrelatedtoDHCPv4snooping.
| Event | ID: 8201 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Server <ip_address> packet received on untrusted port <port> dropped.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhileserverpacketreceivedonuntrustedport.
| Event | ID: 8202 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Client packet destined to untrusted port <port> dropped.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketdroppedwhilepacketdestinedtountrustedport.
| Event | ID: 8203 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Packet received from unauthorized server <ip_address> on port <port>.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhilepacketreceivedfromunauthorizedserver.
| Event | ID: 8204 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Received untrusted relay info from client <mac> on port <port>.
| Category |     | DHCPv4snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketreceivedwithuntrustedrelayinfo.
| Event | ID: 8205 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
73
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Client address <client_mac> not equal to source MAC <source_mac>
detected on port <port>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when client address not equal to source MAC.

Event ID: 8206

Message

Binding for <ip_address>:<mac> exists on port <existing_port>.
Dropping release request received for the binding on <new_port>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when release packet received on incorrect port.

Event ID: 8207

Message

The dynamic binding for <mac> on port <port> was replaced with a
manual binding.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when dynamic binding for a port was replaced with a manual binding.

Event ID: 8208

Message

Drop request from <mac> for already assigned address <ip_address>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when drop client request for already assigned ip.

Event ID: 8209

Message

Drop offer from <server_ip_address> of already assigned address
<lease_ip_address> to <mac>.

Category

DHCPv4 snooping

Severity

Warning

Description

Log event when drop server offer for already assigned ip.

Event ID: 8210

DHCPv4 snooping events | 74

Message Drop offer from <server_ip_address> of <lease_ip_address> address is
illegal.
| Category    | DHCPv4snooping                           |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Warning                                  |     |     |
| Description | Logeventwhendropserverofferforillegalip. |     |     |
Event ID: 8211
Message Maximum bindings limit reached on port <port>, dropping request from
<mac>.
| Category    | DHCPv4snooping                         |     |     |
| ----------- | -------------------------------------- | --- | --- |
| Severity    | Warning                                |     |     |
| Description | Logeventwhenbindinglimitreachedonport. |     |     |
Event ID: 8212
| Message     | All the dynamic                                 | binding entries | were cleared. |
| ----------- | ----------------------------------------------- | --------------- | ------------- |
| Category    | DHCPv4snooping                                  |                 |               |
| Severity    | Information                                     |                 |               |
| Description | Logeventwhenalldynamicbindingentriesarecleared. |                 |               |
Event ID: 8213
Message Dynamic binding entries on the port <port> were cleared.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhenalldynamicbindingentriesonaportarecleared.
Event ID: 8214
Message Dynamic binding entries on the VLAN <vid> were cleared.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhenalldynamicbindingentriesonavlanarecleared.
Event ID: 8215
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 75

Message Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhenaspecificdynamicbindingentryonavlaniscleared.
Event ID: 8216
Message Failed to import dynamic ip binding entries from external storage.
|          | volume: <volume_name>, |     | filename: <file_name>. |
| -------- | ---------------------- | --- | ---------------------- |
| Category | DHCPv4snooping         |     |                        |
| Severity | Error                  |     |                        |
Description Logeventwhenfailedtoimportdynamicipbindingentriesfromexternalstorage.
Event ID: 8217
Message Failed to import dynamic ip binding entries from local storage.
|          | filepath: <file_path>. |     |     |
| -------- | ---------------------- | --- | --- |
| Category | DHCPv4snooping         |     |     |
| Severity | Error                  |     |     |
Description Logeventwhenfailedtoimportdynamicipbindingentriesfromlocalstorage.
Event ID: 8218
| Message  | Flash-storage  | is active | for DHCPv4-Snooping. |
| -------- | -------------- | --------- | -------------------- |
| Category | DHCPv4snooping |           |                      |
| Severity | Warning        |           |                      |
Description Logeventwhenflash-storagebecomesactiveafterexternal-storageunconfiguration.
Event ID: 8219
Message Successfully imported <bindings_imported> dynamic ip binding entries
from external storage. volume: <volume_name>, filename: <file_name>.
| Category | DHCPv4snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhendynamicipbindingentriesfromexternalstoragearesuccessfully
imported.
Event ID: 8220
DHCPv4snoopingevents|76

Message

Successfully imported <bindings_imported> dynamic ip binding entries
from local storage.

Category

DHCPv4 snooping

Severity

Information

Description

Log event when dynamic ip binding entries from local storage are successfully imported.

Event ID: 8221

Message

Client {mac} on vlan {vid}, port {port} received {client_ip} from server {server_ip} with

lease {lease}. Nameserver:{nameserver_ip}, Gateway:{gateway_ip}.

Category

DHCPv4 snooping

Severity

Information

Description

Log event when a client receives IP from DHCP server along with static attributes.

Event ID: 8222

Message

Client {mac} on vlan {vid}, port {port} released {client_ip}.

Category

DHCPv4 snooping

Severity

Information

Description

Log event when a client releases

Event ID: 8223

Message

Client {mac} on vlan {vid}, port {port} lease period expired for {client_ip}.

Category

DHCPv4 snooping

Severity

Information

Description

Log event when a client's lease period expires.

Event ID: 8224

Message

Client {mac} on vlan {vid}, port {port} with {client_ip}. Client attributes updated: Gateway

{gateway_ip}, Nameserver {nameserver_ip}, Lease period {lease}.

Category

DHCPv4 snooping

Severity

Information

Description

Log event when a client's static attributes are updated.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

77

Chapter 24
DHCPv6 Relay events
| DHCPv6 Relay | events |     |
| ------------ | ------ | --- |
ThefollowingaretheeventsrelatedtoDHCPv6relay.
Event ID: 3301
| Message  | DHCPv6 Relay | Enabled |
| -------- | ------------ | ------- |
| Category | DHCPv6Relay  |         |
| Severity | Information  |         |
Description ThiscommandenablestheDHCPv6Relayfeatureinthedevice.
Event ID: 3302
| Message  | DHCPv6 Relay | Disabled |
| -------- | ------------ | -------- |
| Category | DHCPv6Relay  |          |
| Severity | Information  |          |
Description ThiscommanddisablestheDHCPv6Relayfeatureinthedevice.
78
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 25
|        |          |        | DHCPv6 | snooping | events |
| ------ | -------- | ------ | ------ | -------- | ------ |
| DHCPv6 | snooping | events |        |          |        |
ThefollowingaretheeventsrelatedtoDHCPv6snooping.
| Event | ID: 8301 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Server <ipv6_address> packet received on untrusted port <port>
dropped.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhileserverpacketreceivedonuntrustedport.
| Event | ID: 8302 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Client packet destined to untrusted port <port> dropped.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketdroppedwhilepacketdestinedtountrustedport.
| Event | ID: 8303 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Packet received from unauthorized server <ipv6_address> on port
<port>.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenpacketdroppedwhilepacketreceivedfromunauthorizedserver.
| Event | ID: 8304 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Received untrusted relay info from client <mac> on port <port>.
| Category |     | DHCPv6snooping |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Warning        |     |     |     |
Description Logeventwhenclientpacketreceivedwithuntrustedrelayinfo.
| Event | ID: 8305 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
79
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Binding for <ipv6_address>:<mac> exists on port <existing_port>.
Dropping release request received for the binding on <new_port>.
| Category | DHCPv6snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Warning        |     |     |
Description Logeventwhenreleasepacketreceivedonincorrectport.
Event ID: 8306
Message The dynamic binding for <mac> on port <port> was replaced with a
manual binding.
| Category | DHCPv6snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Warning        |     |     |
Description Logeventwhendynamicbindingforaportwasreplacedwithamanualbinding.
Event ID: 8307
Message Drop request from <mac> for already assigned address <ipv6_address>.
| Category | DHCPv6snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Warning        |     |     |
Description Logeventwhendropclientrequestforalreadyassignedip.
Event ID: 8308
Message Maximum bindings limit reached on port <port>, dropping request from
<mac>.
| Category    | DHCPv6snooping                         |     |     |
| ----------- | -------------------------------------- | --- | --- |
| Severity    | Warning                                |     |     |
| Description | Logeventwhenbindinglimitreachedonport. |     |     |
Event ID: 8309
| Message     | All the dynamic                                 | binding entries | were cleared. |
| ----------- | ----------------------------------------------- | --------------- | ------------- |
| Category    | DHCPv6snooping                                  |                 |               |
| Severity    | Information                                     |                 |               |
| Description | Logeventwhenalldynamicbindingentriesarecleared. |                 |               |
Event ID: 8310
DHCPv6snoopingevents|80

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

Event ID: 8315

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

81

| Message  | Flash-storage  | is active | for DHCPv6-Snooping. |
| -------- | -------------- | --------- | -------------------- |
| Category | DHCPv6snooping |           |                      |
| Severity | Warning        |           |                      |
Description Logeventwhenflash-storagebecomesactiveafterexternal-storageunconfiguration.
Event ID: 8316
Message Successfully imported <bindings_imported> dynamic ip binding entries
from external storage. volume: <volume_name>, filename: <file_name>.
| Category | DHCPv6snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Logeventwhendynamicipbindingentriesfromexternalstoragearesuccessfully
imported.
Event ID: 8317
Message Successfully imported <bindings_imported> dynamic ip binding entries
|          | from local     | storage. |     |
| -------- | -------------- | -------- | --- |
| Category | DHCPv6snooping |          |     |
| Severity | Information    |          |     |
Description Logeventwhendynamicipbindingentriesfromlocalstoragearesuccessfullyimported.
Event ID: 8318
Message Client{mac}onvlan{vid},port{port}received{client_ip}fromserver{server_ip}with
lease{lease}.Nameserver:{nameserver_ip}.
| Category | DHCPv6snooping |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description
LogeventwhenaclientreceivesIPv6addressfromDHCPserveralongwithstatic
attributes
Event ID: 8319
Message
Client{mac}onvlan{vid},port{port}released{client_ip}.
| Category    | DHCPv6snooping                          |     |     |
| ----------- | --------------------------------------- | --- | --- |
| Severity    | Information                             |     |     |
| Description | LogeventwhenaclientreleasesIPv6address. |     |     |
DHCPv6snoopingevents|82

Event ID: 8320

Message

Client {mac} on vlan {vid}, port {port} lease period expired for {client_ip}.

Category

DHCPv6 snooping

Severity

Information

Description

Log event when a client's lease period expires.

Event ID: 8321

Message

Client {mac} on vlan {vid}, port {port} with {client_ip}. Client attributes updated:

Nameserver {nameserver_ip}, Lease period {lease}.

Category

DHCPv6 snooping

Severity

Information

Description

Log event when a client's static attributes are updated.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

83

|           |                |          |            |          | Chapter | 26     |
| --------- | -------------- | -------- | ---------- | -------- | ------- | ------ |
|           | Discovery      | and      | Capability | Exchange | (DCBx)  | events |
| Discovery | and Capability | Exchange | (DCBx)     | events   |         |        |
ThefollowingaretheeventsrelatedtoDCBx.
| Event ID: | 9201         |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- |
| Message   | DCBX Enabled |     |     |     |     |     |
Category DicoveryandCapabilityExchange(DCBx)
Severity Information
Description LogseventwhenDCBXisgloballyenabled
| Event ID: | 9202          |     |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- | --- |
| Message   | DCBX Disabled |     |     |     |     |     |
Category DicoveryandCapabilityExchange(DCBx)
Severity Information
Description LogeventwhenDCBXisgloballydisabled
| Event ID: | 9203    |            |           |             |     |     |
| --------- | ------- | ---------- | --------- | ----------- | --- | --- |
| Message   | DCBX is | enabled on | interface | <intf_name> |     |     |
Category DicoveryandCapabilityExchange(DCBx)
Severity Information
Description LogeventwhenDCBXisenabledontheinterface
| Event ID: | 9204    |          |              |             |     |     |
| --------- | ------- | -------- | ------------ | ----------- | --- | --- |
| Message   | DCBX is | disabled | on interface | <intf_name> |     |     |
Category DicoveryandCapabilityExchange(DCBx)
Severity Information
Description LogeventwhenDCBXisdisabledontheinterface
| Event ID: | 9205 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
84
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | DCBX status                                     | active | on interface | <intf_name> |
| ----------- | ----------------------------------------------- | ------ | ------------ | ----------- |
| Category    | DicoveryandCapabilityExchange(DCBx)             |        |              |             |
| Severity    | Information                                     |        |              |             |
| Description | LogeventwhenDCBXoperstatusisactiveonaninterface |        |              |             |
Event ID: 9206
| Message  | DCBX status                         | inactive | on interface | <intf_name> |
| -------- | ----------------------------------- | -------- | ------------ | ----------- |
| Category | DicoveryandCapabilityExchange(DCBx) |          |              |             |
| Severity | Information                         |          |              |             |
Description LogeventwhenDCBXoperstatusisinactiveonaninterface
Event ID: 9207
| Message     | PFC TLV status                            | active | on interface | <intf_name> |
| ----------- | ----------------------------------------- | ------ | ------------ | ----------- |
| Category    | DicoveryandCapabilityExchange(DCBx)       |        |              |             |
| Severity    | Information                               |        |              |             |
| Description | LogeventwhenPFCTLVsareactiveonaninterface |        |              |             |
Event ID: 9208
| Message     | PFC TLV status                              | inactive | on interface | <intf_name> |
| ----------- | ------------------------------------------- | -------- | ------------ | ----------- |
| Category    | DicoveryandCapabilityExchange(DCBx)         |          |              |             |
| Severity    | Information                                 |          |              |             |
| Description | LogeventwhenPFCTLVsareinactiveonaninterface |          |              |             |
Event ID: 9209
Message PFC TLV status priority mismatch on interface <intf_name>
| Category | DicoveryandCapabilityExchange(DCBx) |     |     |     |
| -------- | ----------------------------------- | --- | --- | --- |
| Severity | Warning                             |     |     |     |
Description LogeventwhenthereisPFCTLVprioritymismatchonaninterface
| Distributed | services | events |     |     |
| ----------- | -------- | ------ | --- | --- |
Thefollowingaretheeventsrelatedtodistributedservicesonthe10000Switchseries.
Event ID: 13901
Distributedservicesevents|85

Message

Chassis Reboot Requested: {reason}

Category

Distributed Services

Severity

Warning

Description

Log event that indicates the chassis requires a reboot.

Event ID: 13902

Message

Distributed Services Admission Rejected. Reason: {reason}

Category

Distributed Services

Severity

Warning

Description

Log event that indicates admission to PSM was rejected.' event_description_template

Event ID: 13903

Message

PSM coordinates mismatch. Active coordinates: {active_coordinates},
Configured coordinates: {configured_coordinates}.

Category

Distributed Services

Severity

Warning

Description

Log event that indicates mismatch of PSM coordinates.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

86

Chapter 27
DNS client events
| DNS client events |     |     |
| ----------------- | --- | --- |
ThefollowingaretheeventsrelatedtoDNSclient.
Event ID: 11901
| Message     | <type> event                       | for VRF <vrf_name> |
| ----------- | ---------------------------------- | ------------------ |
| Category    | DNSclient                          |                    |
| Severity    | Information                        |                    |
| Description | EventreportedwhenDNSeventtriggered |                    |
87
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 28

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

802.1X supplicant PAE restarted on interface <ifname> due to change
in policy <policy>.

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

Download events
The following are the events related to file download actions.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

88

Event ID: 14501

Message

Category

Severity

File download started from {url}

DNLD

Info

Description

Indicates that a file download has been started

Event ID: 14502

Message

Category

Severity

File download complete from {url}

DNLD

Info

Description

Indicates that a file has been successfully downloaded

Event ID: 14503

Message

Category

Severity

File download aborted from {url}

DNLD

Info

Description

Indicates that a file download has been aborted

Event ID: 14504

Message

Category

Severity

File download failed from {url} with error code: {error}, {desc}

DNLD

Info

Description

Indicates that a file download has failed

Event ID: 14505

Message

Category

Severity

File upload started to {url}

DNLD

Info

Description

Indicates that a file upload has been started

Event ID: 14506

Download events | 89

Message

Category

Severity

File upload complete to {url}

DNLD

Info

Description

Indicates that a file has been successfully uploaded

Event ID: 14507

Message

Category

Severity

File upload aborted to {url}

DNLD

Info

Description

Indicates that a file upload has been aborted

Event ID: 14508

Message

Category

Severity

File upload failed to {url} with error code: {error}, {desc}

DNLD

Info

Description

Indicates that a file upload has failed

Event ID: 14509

Message

Category

Severity

File download retrying from {url}

DNLD

Info

Description

Indicates that a file download has been retried

Event ID: 14510

Message

Category

Severity

File upload retrying from {url}

DNLD

Info

Description

Indicates that a file upload has been retried

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

90

Chapter 29
DPSE daemon events
| DPSE daemon | events |     |     |
| ----------- | ------ | --- | --- |
ThefollowingaretheeventsrelatedtotheDPSEdaemon.
Event ID: 10901
Message Line card module {linecard_name} triggered backplane enhanced
sequence recovery
| Category | BackPlaneSequenceEvents(DPSE) |     |     |
| -------- | ----------------------------- | --- | --- |
| Severity | Critical                      |     |     |
Description Alinecardhitabackplanesequenceerrorthattriggeredarecoveryoperation
Event ID: 10902
| Message  | HA event triggered            | backplane | sequence recovery |
| -------- | ----------------------------- | --------- | ----------------- |
| Category | BackPlaneSequenceEvents(DPSE) |           |                   |
| Severity | Information                   |           |                   |
Description AbackplanesequenceresetwastriggeredduetoanHAevent
Event ID: 10903
| Message  | HA event completed            | backplane | sequence recovery |
| -------- | ----------------------------- | --------- | ----------------- |
| Category | BackPlaneSequenceEvents(DPSE) |           |                   |
| Severity | Information                   |           |                   |
Description ThesystemcompletedabackplanesequenceresettriggeredbyanHAevent
Event ID: 10904
Message Line card module {linecard_name} triggered backplane enhanced
sequence recovery
| Category | BackPlaneSequenceEvents(DPSE) |     |     |
| -------- | ----------------------------- | --- | --- |
| Severity | Critical                      |     |     |
Description Thesystemcompletedbackplanesequencerecoverytriggeredbylinecarderror
Event ID: 10905
91
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | No active                                   | modules have | been detected | in the system. |
| ----------- | ------------------------------------------- | ------------ | ------------- | -------------- |
| Category    | BackPlaneSequenceEvents(DPSE)               |              |               |                |
| Severity    | Information                                 |              |               |                |
| Description | Noactivemoduleshavebeendetectedinthesystem. |              |               |                |
Event ID: 10906
Message Control Plane (<operation_name>) failure during (<plugin_name>)
configuration
| Category    | BackPlaneSequenceEvents(DPSE)                 |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Critical                                      |     |     |     |
| Description | Anops-switchdpluginfailedexecutinganoperation |     |     |     |
DPSEdaemonevents|92

Chapter 30
ECMP events
ECMP events
ThefollowingaretheeventsrelatedtoECMP.
Event ID: 1801
Message Failed to update ecmp object for route <route>, error: <err>
| Category    | ECMP                              |     |     |
| ----------- | --------------------------------- | --- | --- |
| Severity    | Error                             |     |     |
| Description | logserrorswhilecreatingecmpgroup. |     |     |
Event ID: 1802
| Message     | Update ecmp                 | object for | route <route> |
| ----------- | --------------------------- | ---------- | ------------- |
| Category    | ECMP                        |            |               |
| Severity    | Information                 |            |               |
| Description | logswhilecreatingecmpgroup. |            |               |
Event ID: 1803
Message Failed to delete ecmp egress object <egressid>, error: <err>
| Category    | ECMP                              |     |     |
| ----------- | --------------------------------- | --- | --- |
| Severity    | Error                             |     |     |
| Description | logserrorswhiledeletingecmpgroup. |     |     |
Event ID: 1804
| Message     | Delete ecmp                 | egress object | <egressid> |
| ----------- | --------------------------- | ------------- | ---------- |
| Category    | ECMP                        |               |            |
| Severity    | Information                 |               |            |
| Description | logswhiledeletingecmpgroup. |               |            |
Event ID: 1805
93
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

ECMP error: <err>

Category

Severity

ECMP

Error

Description

logs for ECMP setup errors.

ECMP events | 94

Chapter 31
ERPS events
ERPS events
ThefollowingaretheeventsrelatedtoERPS.
Event ID: 8501
Message Expected R-APS packets not received on <ifID> in ring <ringID> with
|          | control VLAN | <ccvlan> |     |
| -------- | ------------ | -------- | --- |
| Category | ERPS         |          |     |
| Severity | Warning      |          |     |
Description LogeventwhenRAPSmessagesarenotreceivedforacertaintimeinterval
Event ID: 8502
Message Misconfiguration detected on ring <ringID> with control VLAN
<ccvlan>. Another node in the ring with mac <node> is also operating
|             | as an RPL owner                          |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Category    | ERPS                                     |     |     |
| Severity    | Warning                                  |     |     |
| Description | Logeventwhenaringmisconfigurationhappens |     |     |
Event ID: 8503
Message Operational state of the ring <ringID>, instance <instanceID> changed
to <state>
| Category    | ERPS                             |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | Logstatetransitionofringinstance |     |     |
Event ID: 8504
| Message     | <interfaceName>                             | is not | an L2 port |
| ----------- | ------------------------------------------- | ------ | ---------- |
| Category    | ERPS                                        |        |            |
| Severity    | Information                                 |        |            |
| Description | Logeventwhenringisconfiguredwithanon-L2port |        |            |
95
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

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

Log event when control-channel VLAN overlaps with another control-channel of same
ring

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

ERPS events | 96

| Severity | Information |     |     |
| -------- | ----------- | --- | --- |
Description Logeventwhensamecontrol-channelVLANisconfiguredonbothmajorandsub-rings
Event ID: 8510
| Message  | Parent-ring | <ringID> | is same as sub-ring |
| -------- | ----------- | -------- | ------------------- |
| Category | ERPS        |          |                     |
| Severity | Information |          |                     |
Description Logeventwhenparent-ringidisconfiguredtobethesameassub-ring
Event ID: 8511
Message VLAN <vlanID> in the protected VLANs list is also configured as the
control-channel
| Category | ERPS        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogeventwhenVLANfromtheprotected-vlanslistisalreadyconfiguredascontrol-
channelVLAN
Event ID: 8512
Message <portName> is already configured as RPL port for instance
<instanceID>
| Category | ERPS        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogeventifthesameringportisconfiguredasRPLportformorethanoneinstance
Event ID: 8513
Message RPL configuration is not allowed on ISL port <interfaceName>
| Category | ERPS        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogeventifringportwhichisalsoanISLisbeingconfiguredasRPL
Event ID: 8514
Message Protected VLAN set of instance in sub-ring should map to same
|     | instance | in the parent | ring |
| --- | -------- | ------------- | ---- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 97

Category

ERPS

Severity

Information

Description

Log event if protected-vlan set of sub-ring is not a subset of the major-ring

Event ID: 8515

Message

Operational state of the ring <ringID>, instance <instanceID> changed
to Initializing with reason <reason>

Category

ERPS

Severity

Information

Description

Log transition of state of ring instance to initializing and the reason for it

ERPS events | 98

Chapter 32
EVPN events
EVPN events
ThefollowingaretheeventsrelatedtoEVPN.
Event ID: 9501
| Message     | EVPN EVI:               | <evi> created |     |
| ----------- | ----------------------- | ------------- | --- |
| Category    | EVPN                    |               |     |
| Severity    | Information             |               |     |
| Description | LogsEVPNEVIcreateevent. |               |     |
Event ID: 9502
| Message     | EVPN EVI:               | <evi> deleted |     |
| ----------- | ----------------------- | ------------- | --- |
| Category    | EVPN                    |               |     |
| Severity    | Information             |               |     |
| Description | LogsEVPNEVIdeleteevent. |               |     |
Event ID: 9503
| Message     | EVPN RD:                       | <rd> updated for | EVI: <evi> |
| ----------- | ------------------------------ | ---------------- | ---------- |
| Category    | EVPN                           |                  |            |
| Severity    | Information                    |                  |            |
| Description | LogsEVPNRDupdateeventforanEVI. |                  |            |
Event ID: 9504
| Message     | EVPN RD                        | deleted for EVI: | <evi> |
| ----------- | ------------------------------ | ---------------- | ----- |
| Category    | EVPN                           |                  |       |
| Severity    | Information                    |                  |       |
| Description | LogsEVPNRDdeleteeventforanEVI. |                  |       |
Event ID: 9505
99
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | EVPN RT:                       | <rt> created | for EVI: | <evi> |
| ----------- | ------------------------------ | ------------ | -------- | ----- |
| Category    | EVPN                           |              |          |       |
| Severity    | Information                    |              |          |       |
| Description | LogsEVPNRTcreateeventforanEVI. |              |          |       |
Event ID: 9506
| Message     | EVPN RT:                       | <rt> deleted | for EVI: | <evi> |
| ----------- | ------------------------------ | ------------ | -------- | ----- |
| Category    | EVPN                           |              |          |       |
| Severity    | Information                    |              |          |       |
| Description | LogsEVPNRTdeleteeventforanEVI. |              |          |       |
Event ID: 9507
| Message     | EVPN RT:                       | <rt> updated | for EVI: | <evi> |
| ----------- | ------------------------------ | ------------ | -------- | ----- |
| Category    | EVPN                           |              |          |       |
| Severity    | Information                    |              |          |       |
| Description | LogsEVPNRTupdateeventforanEVI. |              |          |       |
Event ID: 9508
| Message     | VNI: <vni>               | is added | for EVPN Peer | VTEP: <vtep_ip> |
| ----------- | ------------------------ | -------- | ------------- | --------------- |
| Category    | EVPN                     |          |               |                 |
| Severity    | Information              |          |               |                 |
| Description | LogsEVPNVTEPVNIaddevent. |          |               |                 |
Event ID: 9509
| Message     | VNI: <vni>                  | is deleted | for EVPN | Peer VTEP: <vtep_ip> |
| ----------- | --------------------------- | ---------- | -------- | -------------------- |
| Category    | EVPN                        |            |          |                      |
| Severity    | Information                 |            |          |                      |
| Description | LogsEVPNVTEPVNIdeleteevent. |            |          |                      |
Event ID: 9510
Message EVPN static MAC conflict <action>, MAC: <mac_addr>, IP address: <ip_
|     | addr>, VTEP: | <vtep_ip> |     |     |
| --- | ------------ | --------- | --- | --- |
EVPNevents|100

| Category    | EVPN                            |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- |
| Severity    | Error                           |     |     |     |
| Description | LogsEVPNstaticMACconflictevent. |     |     |     |
Event ID: 9511
| Message     | EVPN static                     | MAC conflict | <action>, | MAC: <mac_addr> |
| ----------- | ------------------------------- | ------------ | --------- | --------------- |
| Category    | EVPN                            |              |           |                 |
| Severity    | Error                           |              |           |                 |
| Description | LogsEVPNstaticMACconflictevent. |              |           |                 |
Event ID: 9512
Message EVPN duplicate MAC dampening <action>, MAC: <mac_addr>
| Category    | EVPN                                |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Error                               |     |     |     |
| Description | LogsEVPNduplicateMACdampeningevent. |     |     |     |
Event ID: 9513
| Message     | EVPN VRF:               | <vrf> created |     |     |
| ----------- | ----------------------- | ------------- | --- | --- |
| Category    | EVPN                    |               |     |     |
| Severity    | Information             |               |     |     |
| Description | LogsEVPNVRFcreateevent. |               |     |     |
Event ID: 9514
| Message     | EVPN VRF:               | <vrf> deleted |     |     |
| ----------- | ----------------------- | ------------- | --- | --- |
| Category    | EVPN                    |               |     |     |
| Severity    | Information             |               |     |     |
| Description | LogsEVPNVRFdeleteevent. |               |     |     |
Event ID: 9515
| Message  | EVPN RD: | <rd> updated | for VRF: <vrf> |     |
| -------- | -------- | ------------ | -------------- | --- |
| Category | EVPN     |              |                |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 101

| Severity    | Information               |     |     |
| ----------- | ------------------------- | --- | --- |
| Description | LogsEVPNVRFRDupdateevent. |     |     |
Event ID: 9516
| Message     | EVPN RT: <rt>             | created for | VRF: <vrf> |
| ----------- | ------------------------- | ----------- | ---------- |
| Category    | EVPN                      |             |            |
| Severity    | Information               |             |            |
| Description | LogsEVPNVRFRTcreateevent. |             |            |
Event ID: 9517
| Message     | EVPN RT {rt_type}:        | {rt} | deleted for VRF: {vrf} |
| ----------- | ------------------------- | ---- | ---------------------- |
| Category    | EVPN                      |      |                        |
| Severity    | Information               |      |                        |
| Description | LogsEVPNVRFRTdeleteevent. |      |                        |
Event ID: 9518
| Message     | EVPN RT {rt_type}:        | {rt} | deleted for VRF: {vrf} |
| ----------- | ------------------------- | ---- | ---------------------- |
| Category    | EVPN                      |      |                        |
| Severity    | Information               |      |                        |
| Description | LogsEVPNVRFRTupdateevent. |      |                        |
Event ID: 9519
Message EVPN dynamic vxlan tunnel briding mode ibgp-ebgp enabled
| Category | EVPN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhendynamicvxlantunnelbridingmodeibgp-ebgpisenabled
Event ID: 9520
Message EVPN dynamic vxlan tunnel briding mode ibgp-ebgp disabled
| Category | EVPN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhendynamicvxlantunnelbridingmodeibgp-ebgpisdisabled
EVPNevents|102

Event ID: 9521
Message
|             | EVPN VLAN                              | Aware Bundle | : {bundle_name} | created. |
| ----------- | -------------------------------------- | ------------ | --------------- | -------- |
| Category    | EVPN                                   |              |                 |          |
| Severity    | Information                            |              |                 |          |
| Description | LogeventwhenEVPNVLANAwarebundlecreated |              |                 |          |
Event ID: 9522
| Message     | EVPN VLAN                              | Aware Bundle | : {bundle_name} | deleted. |
| ----------- | -------------------------------------- | ------------ | --------------- | -------- |
| Category    | EVPN                                   |              |                 |          |
| Severity    | Information                            |              |                 |          |
| Description | LogeventwhenEVPNVLANAwarebundledeleted |              |                 |          |
Event ID: 9523
Message
|          | EVPN VLAN   | Aware Bundle | : {bundle_name} | disabled. |
| -------- | ----------- | ------------ | --------------- | --------- |
| Category | EVPN        |              |                 |           |
| Severity | Information |              |                 |           |
Description
LogeventwhenEVPNVLANAwarebundledisabled
Event ID: 9524
| Message     | EVPNVLANAwareBundle:{bundle_name}enabled. |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Category    | EVPN                                      |     |     |     |
| Severity    | Information                               |     |     |     |
| Description | LogeventwhenEVPNVLANAwarebundleenabled    |     |     |     |
Event ID: 9525
Message
EVPNEVI:{evi}updatedwithethernet-tag:{eth_tag}.
| Category | EVPN        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description
LogeventwhenVLANethernet-tagisupdated
Event ID: 9526
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 103

Message

EVPN duplicate IP dampening {action}, MAC: {mac_addr}, IP address: {ip_addr}, VTEP:

{vtep_ip}

Category

EVPN

Severity

Information

Description

Logs EVPN duplicate IP dampening event.

Event ID: 9527

Message

EVPN EVI: RT {rtt} {rt} updated for EVI: {evi}

Category

EVPN

Severity

Information

Description

Logs EVPN RT update event for an EVI.

Event ID: 9528

Message

A route-map exists with broadcast group config, please unconfigure it

Category

EVPN

Severity

Information

Description

Logs event when a route-map exists with broadcast group and dynamic bridging ibgp-
ebgp mode is being configured.

EVPN events | 104

Chapter 33
|                  |        |     | External | Storage | events |
| ---------------- | ------ | --- | -------- | ------- | ------ |
| External Storage | events |     |          |         |        |
Thefollowingaretheeventsrelatedtoexternalstorage.
Event ID: 7801
| Message     | Share <name>                      | mount failure' | throttle_count: | 10  |     |
| ----------- | --------------------------------- | -------------- | --------------- | --- | --- |
| Category    | ExternalStorage                   |                |                 |     |     |
| Severity    | Error                             |                |                 |     |     |
| Description | Eventraisedwhenasharefailstomount |                |                 |     |     |
Event ID: 7802
| Message     | Share <name>                         | dismount failure |     |     |     |
| ----------- | ------------------------------------ | ---------------- | --- | --- | --- |
| Category    | ExternalStorage                      |                  |     |     |     |
| Severity    | Error                                |                  |     |     |     |
| Description | Eventraisedwhenasharefailstodismount |                  |     |     |     |
Event ID: 7803
| Message     | Share <name>                | is mounted |     |     |     |
| ----------- | --------------------------- | ---------- | --- | --- | --- |
| Category    | ExternalStorage             |            |     |     |     |
| Severity    | Information                 |            |     |     |     |
| Description | Eventraisedwhenasharemounts |            |     |     |     |
Event ID: 7804
| Message     | Share <name>                   | is dismounted |     |     |     |
| ----------- | ------------------------------ | ------------- | --- | --- | --- |
| Category    | ExternalStorage                |               |     |     |     |
| Severity    | Information                    |               |     |     |     |
| Description | Eventraisedwhenasharedismounts |               |     |     |     |
Event ID: 7805
105
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | Share <name>    | mount is aborted |
| -------- | --------------- | ---------------- |
| Category | ExternalStorage |                  |
| Severity | Error           |                  |
Description Eventraisedwhenamounttimesoutorabortsduetoaconfigchange
Event ID: 7806
| Message     | USB device                   | <status>. |
| ----------- | ---------------------------- | --------- |
| Category    | ExternalStorage              |           |
| Severity    | Information                  |           |
| Description | USBdevicemountedorunmounted. |           |
ExternalStorageevents|106

Chapter 34
Fan events
Fan events
Thefollowingaretheeventsrelatedtofan.
Event ID: 201
Message There are <count> total fans in subsystem <subsystem>.
| Category    | Fan                                   |     |
| ----------- | ------------------------------------- | --- |
| Severity    | Information                           |     |
| Description | Logthetotalnumberoffansinthesubsystem |     |
Event ID: 202
Message Subsystem <subsystem> setting fan speed control register to
|             | <speedval>: <value>. |     |
| ----------- | -------------------- | --- |
| Category    | Fan                  |     |
| Severity    | Information          |     |
| Description | Logthefanspeedset    |     |
Event ID: 203
| Message     | Air flow direction:    | <value>. |
| ----------- | ---------------------- | -------- |
| Category    | Fan                    |          |
| Severity    | Information            |          |
| Description | Logtheairflowdirection |          |
Event ID: 204
| Message     | Fan tray <FT_Name>                          | was removed. |
| ----------- | ------------------------------------------- | ------------ |
| Category    | Fan                                         |              |
| Severity    | Info                                        |              |
| Description | Logeventwhenafantrayisremovedfromthechassis |              |
Event ID: 205
107
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Fan tray                                     | <FT_Name> was | inserted. |     |
| ----------- | -------------------------------------------- | ------------- | --------- | --- |
| Category    | Fan                                          |               |           |     |
| Severity    | Information                                  |               |           |     |
| Description | Logeventwhenafantrayisinsertedintothechassis |               |           |     |
Event ID: 206
| Message     | Fan module                                  | <FMod_Name> | was removed. |     |
| ----------- | ------------------------------------------- | ----------- | ------------ | --- |
| Category    | Fan                                         |             |              |     |
| Severity    | Information                                 |             |              |     |
| Description | Logeventwhenafanmoduleisremovedfromafantray |             |              |     |
Event ID: 207
| Message     | Fan module                                   | <FMod_Name> | was inserted. |     |
| ----------- | -------------------------------------------- | ----------- | ------------- | --- |
| Category    | Fan                                          |             |               |     |
| Severity    | Information                                  |             |               |     |
| Description | Logeventwhenafanmoduleisinsertedintoafantray |             |               |     |
Event ID: 208
Message Fan tray {FT_Name} is not supported by the system. Please insert a
supported fan tray. Refer to the Installation Guide for supported
configurations.
| Category    | Fan                                        |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Error                                      |     |     |     |
| Description | Logeventwhenanunsupportedfantrayisinserted |     |     |     |
Event ID: 209
Message Shutting down system now because <num_of_failure> <failure_type>
|          | <compare_mode> | limit | of <num_of_failure_limit>': | yes |
| -------- | -------------- | ----- | --------------------------- | --- |
| Category | Fan            |       |                             |     |
| Severity | Emergency      |       |                             |     |
Description Logerrorwhensystemshutdownisinitiatedduetocriticalfanfaults
Event ID: 211
Fanevents|108

Message Shutting down system in <seconds> seconds because <num_of_failure>
|          | <failure_type> | <compare_mode> | limit of <num_of_failure_limit> |     |
| -------- | -------------- | -------------- | ------------------------------- | --- |
| Category | Fan            |                |                                 |     |
| Severity | Alert          |                |                                 |     |
Description Logerrorwhenthenumberoffailuresexceedtheallowablelimit
Event ID: 212
| Message     | System                                  | shutdown timer is cancelled.': | yes |     |
| ----------- | --------------------------------------- | ------------------------------ | --- | --- |
| Category    | Fan                                     |                                |     |     |
| Severity    | Info                                    |                                |     |     |
| Description | Logeventwhentheshutdowntimeriscancelled |                                |     |     |
Event ID: 213
| Message     | <num_of_failure>              | <failure_type> | in the system.': | yes |
| ----------- | ----------------------------- | -------------- | ---------------- | --- |
| Category    | Fan                           |                |                  |     |
| Severity    | Error                         |                |                  |     |
| Description | Logerrorwhentherearefanfaults |                |                  |     |
Event ID: 214
Message <function>: Fan <fan_name> faulted, reason: <reason>.': yes
| Category    | Fan                               |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Error                             |     |     |     |
| Description | Listoutthefaultyormissingfannames |     |     |     |
Event ID: 215
| Message     | <FanName>       | fan is <FanStatus>. |     |     |
| ----------- | --------------- | ------------------- | --- | --- |
| Category    | Fan             |                     |     |     |
| Severity    | Information     |                     |     |     |
| Description | Logthefanstatus |                     |     |     |
Event ID: 216
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 109

Message Status of fan <FanName> has changed from <OldStatus> to <NewStatus>.
| Category    | Fan                     |     |     |
| ----------- | ----------------------- | --- | --- |
| Severity    | Information             |     |     |
| Description | Logthechangeinfanstatus |     |     |
Event ID: 217
Message Operational fan count below minimum. <FanCount> fans operating, but
|             | <FanMinimum> are                         | required. |     |
| ----------- | ---------------------------------------- | --------- | --- |
| Category    | Fan                                      |           |     |
| Severity    | Warning                                  |           |     |
| Description | Logwhenminimumnumberoffansarenotpresent. |           |     |
Event ID: 218
Message Fan speed index for thermal zone <ZoneIdx> is <FanSpdIdxStatus>.
| Category | Fan         |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logwhenthefanspeedindexchangestoandfromthemaximumforeachthermalzone
Event ID: 219
| Message     | Fan tray <FT_Name>                   | powered | <Status>. |
| ----------- | ------------------------------------ | ------- | --------- |
| Category    | Fan                                  |         |           |
| Severity    | Information                          |         |           |
| Description | Logeventwhenafantrayispoweredonoroff |         |           |
Event ID: 220
| Message  | Fan tray <FT_Name> | airflow | is <FT_Dir>. |
| -------- | ------------------ | ------- | ------------ |
| Category | Fan                |         |              |
| Severity | Information        |         |              |
Description Logeventwhenafantrayisinsertedspecifyingitsairflowdirection
Event ID: 221
Message <FT_air_curr> airflow fan tray <FT_Name> unsupported; this system
Fanevents|110

requires <FT_air_req> airflow.

Category

Severity

Fan

Error

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

Event ID: 223

Message

Fan tray <FT_Name> FRU EPPROM is incorrectly programmed.

Category

Severity

Fan

Error

Description

Log when fan tray SKU ID in FRU is mismatched

Event ID: 224

Message

Category

Severity

<FT_air_curr> airflow fan tray <FT_Name> disabled; this system
requires <FT_air_req> airflow.

Fan

Error

Description

Log event when a fan tray airflow is not matching with system airflow and is disabled

Event ID: 225

Message

fan tray <FT_Name> misconfigured; this fan tray has been <En_Dis>.

Category

Fan

Severity

Information

Description

Log event when a misconfigured fan tray is enabled or disabled

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

111

Chapter 35
|               |        |     |     | Fault | monitor events |
| ------------- | ------ | --- | --- | ----- | -------------- |
| Fault monitor | events |     |     |       |                |
Thefollowingaretheeventsrelatedtofaultmonitor.
Event ID: 11101
| Message     | Interface                                   | <interface>: | <fault> fault | detected': | yes |
| ----------- | ------------------------------------------- | ------------ | ------------- | ---------- | --- |
| Category    | Faultmonitor                                |              |               |            |     |
| Severity    | Warning                                     |              |               |            |     |
| Description | Logseventwhenafaultisdetectedonaninterface. |              |               |            |     |
Event ID: 11102
Message Interface <interface>: <fault> fault detected and port disabled': yes
| Category | Faultmonitor |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- |
| Severity | Warning      |     |     |     |     |
Description Logseventandshutdowntheinterfacewhenafaultisdetectedonaninterface.
Event ID: 11103
Message Interface <interface>: <fault> fault re-enable time expired, port
|             | enabled':                             | yes |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- |
| Category    | Faultmonitor                          |     |     |     |     |
| Severity    | Information                           |     |     |     |     |
| Description | Interfaceisauto-enabledontimerexpiry. |     |     |     |     |
Event ID: 11104
Message Interface <interface>: <fault> fault disable cancelled due to
|          | configuration | change': | yes |     |     |
| -------- | ------------- | -------- | --- | --- | --- |
| Category | Faultmonitor  |          |     |     |     |
| Severity | Information   |          |     |     |     |
Description Interfaceisauto-enabledonprofileconfigurationchange.
Event ID: 11105
112
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Admin state changed and interface: <interface> is auto-enabled': yes

Category

Fault monitor

Severity

Information

Description

Interface is auto-enabled on admin state change.

Event ID: 11106

Message

Interface <interface>: <fault> fault detected, port is already
disabled by another fault.': yes

Category

Fault monitor

Severity

Warning

Description

Logs event when disabling of a faulty interface failed.

Event ID: 11107

Message

MAC Lockout packet drop detected for {mac} as destination address with packet count:
{da_diff_count}.

Category

Fault monitor

Severity

Information

Description

Logs event when a packet drop is detected for MAC Lockout MAC as source address.

Event ID: 11108

Message

MAC Lockout packet drop detected for {mac} as destination address
with packet count: {da_diff_count}.

Category

Fault monitor

Severity

Information

Description

Logs event when a packet drop is detected for MAC Lockout MAC as destination address.

Event ID: 11109

Message

MAC Lockout packet drop detected for {mac} as source & destination
address with source packet count: {sa_diff_count} and destination
packet count: {da_diff_count}.

Category

Fault monitor

Severity

Information

Description

Logs event when a packet drop is detected for MAC Lockout.

Fault monitor events | 113

Feature Pack events
The following are the events related to CX Advanced and CX Premium feature packs.

Event ID: 14401

Message

{feature_pack_name} installed

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack is installed

Event ID: 14402

Message

{feature_pack_name} erased.

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack is erased.

Event ID: 14403

Message

{feature_pack_name} expired on {expiry_date}.

Category

Feature Pack

Severity

Warning

Description

Event raised when a feature pack expires

Event ID: 14404

Message

Feature pack {parameter_type} {subscription_parameter} does not match device

{parameter_type} {device_parameter}

Category

Feature Pack

Severity

Warning

Description

Event raised when a feature pack serial number or MAC address does not match that of

the device

Event ID: 14405

Message

Event raised when a feature pack file downloads successfully

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

114

Category

Feature Pack

Severity

Info

Description

Feature pack file download success

Event ID: 14406

Message

Feature pack file download failure

Category

Feature Pack

Severity

Warning

Description

Event raised when a feature pack file download fails

Event ID: 14407

Message

Feature pack subscription through Aruba Central is {connection_state}

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack subscription through Aruba Central becomes

connected or disconnected

Event ID: 14408

Message

VSF member serial number {device_serial} not subscribed as part of installed feature

pack

Category

Feature Pack

Severity

Warning

Description

Event raised when a VSF member is not subscribed as part of the installed feature pack

Event ID: 14409

Message

Feature {feature_name} is operating in honor mode without a valid feature pack.

Category

Feature Pack

Severity

Warning

Description

Periodic event raised to indicate that a feature is operating in honor mode

Event ID: 14410

Feature Pack events | 115

Message

Connection to feature pack server lost and subscription for {feature_pack_name} cannot

be validated. Subscribed features will continue to operate in honor mode.

Category

Feature Pack

Severity

Warning

Description

Event raised when a connection to the feature pack server has been lost and the feature

pack subscription cannot be validated

Event ID: 14411

Message

No feature pack is installed. This device requires an Advanced or Premium feature pack

to use advanced or premium features.

Category

Feature Pack

Severity

Warning

Description

Event raised to indicate that the device requires a feature pack

Event ID: 14412

Message

Advanced feature pack installed. This system requires a Premium feature pack to use all

features.

Category

Feature Pack

Severity

Warning

Description

Event raised to indicate that a higher feature pack tier is available and necessary to

enable higher tier features

Event ID: 14413

Message

Software feature pack {feature_pack_name} revoked by the server.

Category

Feature Pack

Severity

Info

Description

Event raised when a feature pack is revoked by the feature pack server.

Event ID: 14414

Message

Feature pack mode {feature_pack_mode} does not match installed feature pack type

{feature_pack_type}.

Category

Feature Pack

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

116

Severity

Warning

Description

Event raised when the feature pack mode configured does not match the feature pack

type installed on the device.

Event ID: 14415

Message

Cloud-managed mode is enabled. A feature pack server will be used for feature pack

management.

Category

Feature Pack

Severity

Info

Description

Event raised when the feature pack management mode is set to cloud-managed

Event ID: 14416

Message

Cloud-managed mode is disabled. A feature pack server will no longer be used for

feature pack management.

Category

Feature Pack

Severity

Info

Description

Event raised when the management mode is different than cloud-managed

Event ID: 14417

Message

The feature pack has been successfully validated by the server

Category

Feature Pack

Severity

Info

Description

Event raised when the feature pack was successfully validated by the server

Event ID: 14418

Message

Feature pack server failed to validate the installed feature pack

Category

Feature Pack

Severity

Error

Description

Event raised when there is an error validating a feature pack by the server

Feature Pack events | 117

Chapter 36

Firmware Update events

Firmware Update events

The following are the events related to firmware update.

Event ID: 4401

Message

User <user>: <image_profile> image updated via <dnld_type> from
<host>. Firmware version, Before Update: <before> After Update:
<after>

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

118

Event ID: 4405
| Message  | Firmware image | signature | not valid |
| -------- | -------------- | --------- | --------- |
| Category | FirmwareUpdate |           |           |
| Severity | Error          |           |           |
Description Indicatesthatthesignatureverificationcheckduringaswitchfirmwareorhot-patch
downloadfailed
Event ID: 4406
| Message  | Firmware image | is not | compatible with hardware |
| -------- | -------------- | ------ | ------------------------ |
| Category | FirmwareUpdate |        |                          |
| Severity | Error          |        |                          |
Description Indicatesthatthesignatureverificationcheckduringaswitchfirmwareorhot-patch
downloadfailed
Event ID: 4407
| Message  | Firmware image | is invalid |     |
| -------- | -------------- | ---------- | --- |
| Category | FirmwareUpdate |            |     |
| Severity | Error          |            |     |
Description Indicatesthatthesignatureverificationcheckduringaswitchfirmwareorhot-patch
downloadfailed
Event ID: 4408
Message User{user}:hot-patch"{hotpatch_name}"downloadedvia{dnld_type}from{host
| Category | FirmwareUpdate |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Indicatesthatahot-patchimagewasdownloadedsuccesfullyfromaremotesour
Event ID: 4409
Message
User{user}:hot-patch"{hotpatch_name}"downloadedvia{dnld_type}.
| Category | FirmwareUpdate |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description
Indicatesthatahot-patchimagewasdownloadedsuccesfullyfromalocalsource
Event ID: 4410
FirmwareUpdateevents|119

Message User{user}:hot-patch"{hotpatch_name}"downloadfailedvia{dnld_type}from{host}
| Category | FirmwareUpdate |     |     |     |     |
| -------- | -------------- | --- | --- | --- | --- |
| Severity | Information    |     |     |     |     |
Description Indicatesthatahot-patchimagedownloadfailedfromaremotesource
Event ID: 4411
Message
User{user}:hot-patch"{hotpatch_name}"downloadfailedvia{dnld_type}
| Category | FirmwareUpdate |     |     |     |     |
| -------- | -------------- | --- | --- | --- | --- |
| Severity | Information    |     |     |     |     |
Description
Indicatesthatahot-patchimagedownloadfailedfromalocalsource
| Forwarding     | and Queuing |     | for Time-Sensitive |     | Streams |
| -------------- | ----------- | --- | ------------------ | --- | ------- |
| (FQTSS) events |             |     |                    |     |         |
Thefollowingaretheeventsrelatedtodistributedservicesonthe10000Switchseries.
Event ID: 13902
| Message     | FQTSSallocrequested                        |     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- | --- |
| Category    | FQTSS                                      |     |     |     |     |
| Severity    | Warning                                    |     |     |     |     |
| Description | EventreportedwhenFQTSSreceivedallocrequest |     |     |     |     |
Event ID: 13903
| Message     | Event reported                               | when FQTSS | received dealloc | request |     |
| ----------- | -------------------------------------------- | ---------- | ---------------- | ------- | --- |
| Category    | FQTSS                                        |            |                  |         |     |
| Severity    | Warning                                      |            |                  |         |     |
| Description | EventreportedwhenFQTSSreceiveddeallocrequest |            |                  |         |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 120

|          |                |        |          |        | Chapter | 37     |
| -------- | -------------- | ------ | -------- | ------ | ------- | ------ |
|          |                |        | Hardware | Health | Monitor | events |
| Hardware | Health Monitor | events |          |        |         |        |
Thefollowingaretheeventsrelatedtohardwarehealthmonitor.
| Event ID: | 3001 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Diagnostic <test_name> failed with error code <error_code> on
|     | management | module <slot>': | yes |     |     |     |
| --- | ---------- | --------------- | --- | --- | --- | --- |
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinmanagementmodule
| Event ID: | 3002 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Diagnostic <test_name> failed with error code <error_code> on line
card <slot>': yes
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinlinecard
| Event ID: | 3003 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Diagnostic <test_name> failed with error code <error_code> on fabric
card <slot>': yes
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinfabriccard
| Event ID: | 3004 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Diagnostic <test_name> failed with error code <error_code> on fan
tray <slot>': yes
Category HardwareHealthMonitor
Severity Error
Description Eventraisedwhenhardwarediagnosticsdetectserrorinfantray
121
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Event ID: 3005
Message Diagnostic <test_name> failed with error code <error_code> on rear
|          | display               | card <slot>': | yes |     |     |
| -------- | --------------------- | ------------- | --- | --- | --- |
| Category | HardwareHealthMonitor |               |     |     |     |
| Severity | Error                 |               |     |     |     |
Description Eventraisedwhenhardwarediagnosticsdetectserrorinreardisplaycard
Event ID: 3006
Message Diagnostic <test_name> failed with error code <error_code> for the
|          | system':              | yes |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Category | HardwareHealthMonitor |     |     |     |     |
| Severity | Error                 |     |     |     |     |
Description Eventraisedwhenhardwarediagnosticsdetectserrorinthesystem
Event ID: 3007
| Message     | There are             | <origin> | happening on | <location>': | yes |
| ----------- | --------------------- | -------- | ------------ | ------------ | --- |
| Category    | HardwareHealthMonitor |          |              |              |     |
| Severity    | Warning               |          |              |              |     |
| Description | LogsMCEBUSerror       |          |              |              |     |
Event ID: 3008
| Message     | There are                         | IO errors | on <location> | from |     |
| ----------- | --------------------------------- | --------- | ------------- | ---- | --- |
|             | <seg>:<bus>:<device>:<function>': |           |               | yes  |     |
| Category    | HardwareHealthMonitor             |           |               |      |     |
| Severity    | Warning                           |           |               |      |     |
| Description | LogsMCEIOerror                    |           |               |      |     |
Event ID: 3009
| Message     | There are                                  | unknown | errors on <location> | from |     |
| ----------- | ------------------------------------------ | ------- | -------------------- | ---- | --- |
|             | <status>:<addr>:<misc>:<mcgstatus>:<cap>': |         |                      |      | yes |
| Category    | HardwareHealthMonitor                      |         |                      |      |     |
| Severity    | Information                                |         |                      |      |     |
| Description | LogsMCEunknownerror                        |         |                      |      |     |
HardwareHealthMonitorevents|122

Event ID: 3010

Message

CPUs <cpus> L<level> <type> cache error detected. CPUs <offlined>
offlined': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Logs CPU cache error

Event ID: 3011

Message

Socket <socket> correctable memory error count <cecount> exceeded
threshold <threshold>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when socket correctable memory error count is exceeded threshold

Event ID: 3012

Message

Module <channel> correctable memory error count <cecount> exceeded
threshold <threshold>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when module correctable memory error count is exceeded threshold

Event ID: 3013

Message

Page <page> correctable memory error count <cecount> exceeded
threshold <threshold> and <offlined>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when page correctable memory error count is exceeded threshold

Event ID: 3013

Message

Page <page> correctable memory error count <cecount> exceeded
threshold <threshold> and <offlined>': yes

Category

Hardware Health Monitor

Severity

Warning

Description

Log when page correctable memory error count is exceeded threshold

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

123

Event ID: 3014

Message

Diagnostic {test_name} failed with error code {error_code} on management module {slot}

and report as info

Category

Hardware Health Monitor

Severity

Information

Description

Event raised when hardware diagnostics detects error in management module and

report as inf

Event ID: 3015

Message

Diagnostic {test_name} failed with error code {error_code} on management module {slot}

and report as warning

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in management module and

report as warning

Event ID: 3016

Message

Diagnostic {test_name} failed with error code {error_code} on fabric card {slot} and
report as inf

Category

Hardware Health Monitor

Severity

Information

Description

Event raised when hardware diagnostics detects error in fabric card and report as inf

Event ID: 3017

Message

Diagnostic {test_name} failed with error code {error_code} on fabric card {slot} and

report as warnin

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in fabric card and report as

warning

Event ID: 3018

Message

Diagnostic {test_name} failed with error code {error_code} on line card {slot} and report

Hardware Health Monitor events | 124

as info

Category

Hardware Health Monitor

Severity

Information

Description

Event raised when hardware diagnostics detects error in line card and report as info'

Event ID: 3019

Message

Diagnostic {test_name} failed with error code {error_code} on line card {slot} and report

as warning

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in line card and report as warning

Event ID: 3020

Message

Diagnostic {test_name} failed with error code {error_code} on fan tray {slot} and report

as info

Category

Hardware Health Monitor

Severity

Information

Description

Event raised when hardware diagnostics detects error in fan tray and report as info

Event ID: 3021

Message

Diagnostic {test_name} failed with error code {error_code} on fan tray {slot} and report

as warning

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics detects error in fan tray and report as warning

Event ID: 13801

Message

HW Fault (Error {error_code}) detected on the switch. {impact_
statement}. Contact support for assistance.

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics error detected in the system

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

125

Event ID: 13802

Message

HW Fault (Error {error_code}) detected on the switch. {impact_
statement}. Contact support for assistance.

Category

Hardware Health Monitor

Severity

Warning

Description

Event raised when hardware diagnostics error detected in the system

Hardware Health Monitor events | 126

Chapter 38
|          |                   | Hardware    | switch | controller | sync events |
| -------- | ----------------- | ----------- | ------ | ---------- | ----------- |
| Hardware | switch controller | sync events |        |            |             |
Thefollowingaretheeventsrelatedtohardwareswitchcontroller.
| Event ID: | 8801     |               |              |     |     |
| --------- | -------- | ------------- | ------------ | --- | --- |
| Message   | Hardware | VTEP DB setup | is completed |     |     |
Category Hardwareswitchcontrollersync
Severity Information
Description LogwhenhardwareVTEPDBsetupiscompleted
| Event ID: | 8802     |             |            |                  |     |
| --------- | -------- | ----------- | ---------- | ---------------- | --- |
| Message   | Physical | Port <port> | is created | in Hardware VTEP | DB  |
Category Hardwareswitchcontrollersync
Severity Information
Description LogwhenphysicalportiscreatedinhardwareVTEPDB
| Event ID: | 8803 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Physical Port <port> is deleted from Hardware VTEP DB
Category Hardwareswitchcontrollersync
Severity Information
Description LogwhenphysicalportisdeletedfromhardwareVTEPDB
| Event ID: | 8804 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message HSC configuration is completed on the switch and pushed to Hardware
VTEP DB
Category Hardwareswitchcontrollersync
Severity Information
Description LogswhenHSCconfigurationiscompletedontheswitchandpushedtoHardwareVTEP
DB
| Event ID: | 8805 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
127
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message HSC configuration is deleted from the switch and Hardware VTEP DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenHSCconfigurationisdeletedfromtheswitchandHardwareVTEPDB
Event ID: 8806
Message Local MAC <mac> learnt on VLAN <vlan> is updated in the Hardware VTEP
DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenlocalMAClearnonVLANisupdatedintheHardwarVTEPDB
Event ID: 8807
Message Local MAC <mac> learnt on VLAN <vlan> is removed from the Hardware
VTEP DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenlocalMAClearntonVLANisremovedfromtheHardwareVTEPDB
Event ID: 8808
| Message     | VXLAN IP <ip>                               | is updated | in the Hardware | VTEP DB |
| ----------- | ------------------------------------------- | ---------- | --------------- | ------- |
| Category    | Hardwareswitchcontrollersync                |            |                 |         |
| Severity    | Information                                 |            |                 |         |
| Description | LogswhenVXLANIPisupdatedintheHardwareVTEPDB |            |                 |         |
Event ID: 8809
Message VXLAN IP <ip> is removed from Switch and Hardware VTEP DB
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Event ID: 8810
Message Unicast Remote MAC <mac> learnt on VNI <vni> is added to the switch
Hardwareswitchcontrollersyncevents|128

| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenunicastremoteMAClearntonVNIisaddedtotheswitch
Event ID: 8811
Message Unicast Remote MAC <mac> learnt on VNI <vni> is removed from the
switch
| Category | Hardwareswitchcontrollersync |     |     |     |
| -------- | ---------------------------- | --- | --- | --- |
| Severity | Information                  |     |     |     |
Description LogswhenunicastremoteMAClearntonVNIisremovedfromtheswitch
Event ID: 8812
| Message     | Tunnel                                    | <ip> is removed | from Hardware | VTEP DB |
| ----------- | ----------------------------------------- | --------------- | ------------- | ------- |
| Category    | Hardwareswitchcontrollersync              |                 |               |         |
| Severity    | Information                               |                 |               |         |
| Description | LogswhentunnelisremovedfromHardwareVTEPDB |                 |               |         |
| Hot Patch   | events                                    |                 |               |         |
ThefollowingaretheeventsrelatedtoHotPatchupdates.
Event ID: 13201
| Message  | Hot-patch | {patch_name} | will be disabled | upon reboot. |
| -------- | --------- | ------------ | ---------------- | ------------ |
| Category | HotPatch  |              |                  |              |
| Severity | LOG_INFO  |              |                  |              |
Description Logsamessagefortheusertorebootthesysteminordertodeactivatepatch
Event ID: 13202
| Message     | Hot-patch                    | {patch_name} | added. |     |
| ----------- | ---------------------------- | ------------ | ------ | --- |
| Category    | HotPatch                     |              |        |     |
| Severity    | LOG_INFO                     |              |        |     |
| Description | Newhot-patchfilewasdetected. |              |        |     |
-Event ID: 13203
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 129

| Message     | Hot-patch                                   | {patch_name} | successfully | applied. |
| ----------- | ------------------------------------------- | ------------ | ------------ | -------- |
| Category    | HotPatch                                    |              |              |          |
| Severity    | LOG_INFO                                    |              |              |          |
| Description | Hot-patchwasappliedtorunningsystemsoftware. |              |              |          |
Event ID: 13204
| Message     | Hot-patch{patch_name}removed. |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Category    | HotPatch                      |     |     |     |
| Severity    | LOG_INFO                      |     |     |     |
| Description | Hot-patchfiledeleted.         |     |     |     |
Event ID: 13205
Message Hot-patch {patch_name} config mismatch, patch applied.
| Category    | HotPatch                                |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | LOG_WARN                                |     |     |     |
| Description | Hot-patchconfigandfilesystemdonotagree. |     |     |     |
Event ID: 13206
| Message     | Hot-patch                           | {patch_name} | is missing. |     |
| ----------- | ----------------------------------- | ------------ | ----------- | --- |
| Category    | HotPatch                            |              |             |     |
| Severity    | LOG_WARN                            |              |             |     |
| Description | Hot-patchisnotfoundonthefilesystem. |              |             |     |
Event ID: 13207
| Message     | Hot-patch                        | {patch_name} | verification | failed. |
| ----------- | -------------------------------- | ------------ | ------------ | ------- |
| Category    | HotPatch                         |              |              |         |
| Severity    | LOG_ERR                          |              |              |         |
| Description | Hot-patchfailedfileverification. |              |              |         |
Event ID: 13208
| Message | Hot-patch | {patch_name} | failed | to apply' |
| ------- | --------- | ------------ | ------ | --------- |
HotPatchevents|130

| Category    | HotPatch                                       |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | LOG_ERR                                        |     |     |     |
| Description | Hot-patchfailedtoapplytoallrequiredcomponents. |     |     |     |
Event ID: 13209
| Message  | Hot-patch | {patch_name} | image signature | not valid. |
| -------- | --------- | ------------ | --------------- | ---------- |
| Category | HotPatch  |              |                 |            |
| Severity | LOG_ERR   |              |                 |            |
Description Indicatesthatathesignatureverificationcheckduringahot-patchdownloadfailed
Event ID: 13210
Message Hot-patch {patch_name} image is not compatible with hardware.
| Category | HotPatch |     |     |     |
| -------- | -------- | --- | --- | --- |
| Severity | LOG_ERR  |     |     |     |
Description Indicatesthatthehot-patchimagedownloadedisnotcompatiblewithhardware
Event ID: 13211
Message Hot-patch {patch_name} image is not compatible with software.
| Category | HotPatch |     |     |     |
| -------- | -------- | --- | --- | --- |
| Severity | LOG_ERR  |     |     |     |
Description Indicatesthatthehot-patchimagedownloadedisnotcompatiblewiththecurrent
softwareversion
Event ID: 13212
| Message  | Hot-patch | {patch_name} | is invalid' |     |
| -------- | --------- | ------------ | ----------- | --- |
| Category | HotPatch  |              |             |     |
| Severity | LOG_ERR   |              |             |     |
Description Indicatesthatthehot-patchfiledownloadedforisnotavalidimage'event_description_
template:
Event ID: 13213
Message Hot-patch {patch_name} was modified after it was parsed'
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 131

| Category | HotPatch |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- |
| Severity | LOG_WARN |     |     |     |     |
Description Indicatesthatthehot-patchfilewasmodifiedafterparsing
Event ID: 13214
Message Not enough disk space available to install hot-patch {patch_name}.
| Category | HotPatch |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- |
| Severity | LOG_ERR  |     |     |     |     |
Description Indicatesthatthehot-patchfilecouldnotbeinstalledduetolowdiskspace
Event ID: 13215
Message Not enough memory available to install hot-patch {patch_name}'
| Category | HotPatch |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- |
| Severity | LOG_ERR  |     |     |     |     |
Description Indicatesthatthehot-patchfilecouldnotbeinstalledduetolowmemory
Event ID: 13216
| Message     | Indicates                             | that hot-patch | install | timed out. |     |
| ----------- | ------------------------------------- | -------------- | ------- | ---------- | --- |
| Category    | HotPatch                              |                |         |            |     |
| Severity    | LOG_ERR                               |                |         |            |     |
| Description | Hot-patch{patch_name}installtimedout. |                |         |            |     |
Event ID: 13217
Message Hot-patch {patch_name} could not be installed because a newer hot-
|          | patch has | been, or will | be, installed' |     |     |
| -------- | --------- | ------------- | -------------- | --- | --- |
| Category | HotPatch  |               |                |     |     |
| Severity | LOG_WARN  |               |                |     |     |
Description Indicatesthatthehot-patchfilecouldnotbeinstalledbecauseanewerhot-patchhas
been,orwillbe,installed
Event ID: 13218
Message Hot-patch {patch_name} could not be installed because another patch
|     | that is | configured to | be installed | has the same | timestamp. |
| --- | ------- | ------------- | ------------ | ------------ | ---------- |
HotPatchevents|132

| Category | HotPatch |     |     |
| -------- | -------- | --- | --- |
| Severity | LOG_WARN |     |     |
Description Indicatesthatthehot-patchfilecouldnotbeinstalledbecauseanotherpatchthatis
configuredtobeinstalledhasthesametimestamp
Event ID: 13219
Message Hot-patch {patch_name} verification timed out after {time_out}
seconds.
| Category    | HotPatch                                    |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Severity    | LOG_ERR                                     |     |     |
| Description | Indicatesthathot-patchverificationtimedout. |     |     |
Event ID: 13220
| Message     | Hot-patch                                       | {patch_name} | is applying. |
| ----------- | ----------------------------------------------- | ------------ | ------------ |
| Category    | HotPatch                                        |              |              |
| Severity    | LOG_INFO                                        |              |              |
| Description | Indicatesthatahot-patchiscurrentlybeingapplied. |              |              |
Event ID: 13221
| Message     | Hot-patch                                         | {patch_name} | is unapplying. |
| ----------- | ------------------------------------------------- | ------------ | -------------- |
| Category    | HotPatch                                          |              |                |
| Severity    | LOG_INFO                                          |              |                |
| Description | Indicatesthatahot-patchiscurrentlybeingunapplied. |              |                |
Event ID: 13222
| Message     | Hot-patch                                  | {patch_name} | is not applied. |
| ----------- | ------------------------------------------ | ------------ | --------------- |
| Category    | HotPatch                                   |              |                 |
| Severity    | LOG_INFO                                   |              |                 |
| Description | Hot-patchunappliedonrunningsystemsoftware. |              |                 |
Event ID: 13223
Message Hot-patch {patch_name} failed to unapply. Reboot recommended.
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 133

| Category    | HotPatch                                         |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | LOG_ERR                                          |     |     |     |
| Description | Hot-patchfailedtounapplyonallrequiredcomponents. |     |     |     |
Event ID: 13224
| Message     | Hot-patch                  | {patch_name} | failed | to download' |
| ----------- | -------------------------- | ------------ | ------ | ------------ |
| Category    | HotPatch                   |              |        |              |
| Severity    | LOG_ERR                    |              |        |              |
| Description | Hot-patchfailedtodownload. |              |        |              |
Event ID: 13224
| Message     | Hot-patch                  | {patch_name} | failed | to download' |
| ----------- | -------------------------- | ------------ | ------ | ------------ |
| Category    | HotPatch                   |              |        |              |
| Severity    | LOG_ERR                    |              |        |              |
| Description | Hot-patchfailedtodownload. |              |        |              |
Event ID: 13224
| Message     | Hot-patch                  | {patch_name} | failed | to download' |
| ----------- | -------------------------- | ------------ | ------ | ------------ |
| Category    | HotPatch                   |              |        |              |
| Severity    | LOG_ERR                    |              |        |              |
| Description | Hot-patchfailedtodownload. |              |        |              |
Event ID: 13225
| Message     | Hot-patch                        | {patch_name} | downloaded | successfully' |
| ----------- | -------------------------------- | ------------ | ---------- | ------------- |
| Category    | HotPatch                         |              |            |               |
| Severity    | LOG_INFO                         |              |            |               |
| Description | Hot-patchdownloadedsuccessfully. |              |            |               |
Event ID: 13226
Message Attempt to Hot-Patch {patch_name} on {ss_type}_{ss_name} at boot : "
{status}"'
HotPatchevents|134

Category

Hot Patch

Severity

LOG_INFO

Description

Status of the Hot-patch attempted to be applied at boot

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

135

|                     |     |     |     |       | Chapter | 39     |
| ------------------- | --- | --- | --- | ----- | ------- | ------ |
|                     |     |     |     | HTTPS | Server  | events |
| HTTPS Server events |     |     |     |       |         |        |
ThefollowingaretheeventsrelatedtoHTTPSserver.
Event ID: 5601
| Message  | User <user> | has enabled | <mode> for | REST mode |     |     |
| -------- | ----------- | ----------- | ---------- | --------- | --- | --- |
| Category | HTTPSServer |             |            |           |     |     |
| Severity | Information |             |            |           |     |     |
Description LogsamessagewhenauserchangesthestatusoftheRESTmode
Event ID: 5602
| Message  | User <user> | has <status> | HTTPS Server | on VRF <vrf> |     |     |
| -------- | ----------- | ------------ | ------------ | ------------ | --- | --- |
| Category | HTTPSServer |              |              |              |     |     |
| Severity | Information |              |              |              |     |     |
Description Logsamessagewhenauserenables/disablesthehttps-serverVRFconfiguration
Event ID: 5603
| Message     | User <user>                                 | closed all | HTTPS sessions |     |     |     |
| ----------- | ------------------------------------------- | ---------- | -------------- | --- | --- | --- |
| Category    | HTTPSServer                                 |            |                |     |     |     |
| Severity    | Information                                 |            |                |     |     |     |
| Description | LogsamessagewhenauserclosesallHTTPSsessions |            |                |     |     |     |
Event ID: 5604
Message User <user> changed the HTTPS Server max user sessions amount to
<sessions>
| Category | HTTPSServer |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
| Severity | Information |     |     |     |     |     |
Description Logsamessagewhenauserchangesthemaximumamountofsessionsperuser
Event ID: 5605
136
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

User <user> changed the HTTPS Server idle timeout to <timeout>

Category

HTTPS Server

Severity

Information

Description

Logs a message when a user changes the value of the session idle timeout

HTTPS Server events | 137

Chapter 40
|           |             |        | In-System | Programming | events |
| --------- | ----------- | ------ | --------- | ----------- | ------ |
| In-System | Programming | events |           |             |        |
Thefollowingaretheeventsrelatedtoin-systemprogramming.
| Event ID: | 7200     |                |               |     |     |
| --------- | -------- | -------------- | ------------- | --- | --- |
| Message   | Internal | fatal error at | <file>:<line> |     |     |
Category In-SystemProgramming
Severity Error
Description ISPinternalfatalerror
| Event ID: | 7210 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Non-failsafe update needed for <devspec>. Please run the allow-
unsafe-updates command
Category In-SystemProgramming
Severity Error
Description Anon-failsafedeviceupdateisneeded,buttheallow-unsafe-updatescommandhasnot
yetbeenrun
| Event ID: | 7211   |                        |        |               |     |
| --------- | ------ | ---------------------- | ------ | ------------- | --- |
| Message   | Do not | interrupt non-failsafe | update | for <devspec> |     |
Category In-SystemProgramming
Severity Error
Description Anon-failsafedeviceupdateisabouttostart,sodonotinterruptit
| Event ID: | 7212 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Starting update for <devspec> from version <fromver> to version
<tover>
Category In-SystemProgramming
Severity Information
Description Adeviceupdateisabouttostart
| Event ID: | 7213 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
138
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Update successful for <devspec> from version <fromver> to version
<tover>
| Category | In-SystemProgramming |     |
| -------- | -------------------- | --- |
| Severity | Information          |     |
Description Adeviceupdatewassuccessfulorinsomecaseswassuccessfullyarrangedtobe
performedlater
Event ID: 7214
| Message     | Update failed        | for <devspec> |
| ----------- | -------------------- | ------------- |
| Category    | In-SystemProgramming |               |
| Severity    | Critical             |               |
| Description | Adeviceupdatefailed  |               |
Event ID: 7215
Message Deferred update for <devspec> will be performed after an automatic
module reset
| Category | In-SystemProgramming |     |
| -------- | -------------------- | --- |
| Severity | Information          |     |
Description Adeviceupdatewaspostponeduntilafteranautomaticresetofitsmodule
Event ID: 7216
Message Approximately <time> minute(s) remaining to update <numdevs> device
(s) on <modspec>
| Category | In-SystemProgramming |     |
| -------- | -------------------- | --- |
| Severity | Information          |     |
Description Indicatestheapproximateremainingupdatetimeforamodule
Event ID: 7217
Message Insufficient redundant power is available to update <devspec>
| Category    | In-SystemProgramming                   |     |
| ----------- | -------------------------------------- | --- |
| Severity    | Information                            |     |
| Description | Unabletoupdatenon-redundantpowersupply |     |
Event ID: 7218
In-SystemProgrammingevents|139

Message Programmable device updates are pending that require a power cycle.
Wait for all fabric and line modules to be ready, then power the
|          | system               | off and back | on again |     |
| -------- | -------------------- | ------------ | -------- | --- |
| Category | In-SystemProgramming |              |          |     |
| Severity | Information          |              |          |     |
Description ISPneedsthechassispower-cycledmanuallywhenitcannotbedoneautomatically
Event ID: 7219
| Message     | Failed                               | to write-protect | <devspec> | (pass <pass>) |
| ----------- | ------------------------------------ | ---------------- | --------- | ------------- |
| Category    | In-SystemProgramming                 |                  |           |               |
| Severity    | Critical                             |                  |           |               |
| Description | Failedtowrite-protectamoduleordevice |                  |           |               |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 140

Chapter 41
|           |               | Interface  | and Interface | Diagnostic | events |
| --------- | ------------- | ---------- | ------------- | ---------- | ------ |
| Interface | and Interface | Diagnostic | events        |            |        |
Thefollowingaretheeventsrelatedtointerface.
| Event ID: | 401 |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
Message Interface port_admin set to up for <interface> interface
| Category    | Interface                         |     |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- | --- |
| Severity    | Information                       |     |     |     |     |
| Description | Logwheninterfaceport_adminsettoup |     |     |     |     |
| Event ID:   | 402                               |     |     |     |     |
Message Interface port_admin set to down for <interface> interface
| Category    | Interface                           |            |                       |            |     |
| ----------- | ----------------------------------- | ---------- | --------------------- | ---------- | --- |
| Severity    | Information                         |            |                       |            |     |
| Description | Logwheninterfaceport_adminsettodown |            |                       |            |     |
| Event ID:   | 403                                 |            |                       |            |     |
| Message     | Link                                | status for | interface {interface} | is {state} |     |
| Category    | Interface                           |            |                       |            |     |
| Severity    | Information                         |            |                       |            |     |
| Description | Logwheninterfacelinkstatusisup      |            |                       |            |     |
| Event ID:   | 404                                 |            |                       |            |     |
| Message     | Link                                | status for | interface {interface} | is {state} |     |
| Category    | Interface                           |            |                       |            |     |
| Severity    | Information                         |            |                       |            |     |
| Description | Logwheninterfacelinkstatusisdown    |            |                       |            |     |
| Event ID:   | 405                                 |            |                       |            |     |
141
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | Reserved for | future | use |
| -------- | ------------ | ------ | --- |
| Category | Interface    |        |     |
| Severity | Error        |        |     |
Event ID: 406
Message Interface <interface> encountered a hardware error that caused a link
reset
| Category | Interface   |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logwheninterfaceencounteredanerrorthatrequiresuserintervention
Event ID: 407
Message Interface <interface> downshifted to speed <port_speed> Mbps because
|             | link attempt                          | failed | at higher speed. |
| ----------- | ------------------------------------- | ------ | ---------------- |
| Category    | Interface                             |        |                  |
| Severity    | Information                           |        |                  |
| Description | Logwheninterfaceencounteredadownshift |        |                  |
Event ID: 408
Message Interface <interface> is down because MACsec and PFC features are
|          | mutually exclusive. |     |     |
| -------- | ------------------- | --- | --- |
| Category | Interface           |     |     |
| Severity | Warning             |     |     |
Description LogwheninterfaceisdownduetoincompatibleMACsecandPFCconfiguration
Event ID: 409
Message Interface {interface} link reset ignored. {count} total link resets
|             | ignored for                        | this interface |     |
| ----------- | ---------------------------------- | -------------- | --- |
| Category    | Interface                          |                |     |
| Severity    | Information                        |                |     |
| Description | Logwheninterfaceignoresalinkreset' |                |     |
Event ID: 410
InterfaceandInterfaceDiagnosticevents|142

Message

Category

Severity

Description

Event ID: 14201

Interface {interface} cannot be enabled due to invalid configuration

Interface

Warning

Logged when the interface cannot be enabled due to a configuration setting that is
incompatible with hardware

Message

Interface {interface}: unable to run cable diagnostic on VSF port

Category

Interface

Severity

Error

Description

Cable diagnostic test is unable to run on VSF port.

Event ID: 14202

Message

Interface {interface}: unable to run cable diagnostic on unsupported
port.

Category

Interface

Severity

Error

Description

Cable diagnostic test is unable to run on unsupported port.

Event ID: 14203

Message

Interface {interface}: unable to run cable diagnostic when another
diagnostic test is in progress.

Category

Interface

Severity

Error

Description

Cable diagnostic test is unable to run due to another ongoing diagnostic test

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

143

Chapter 42

Internal storage events

Internal storage events

The following are the events related to internal storage.

Event ID: 9101

Message

Failed to report storage <name> details for module <module_num>.
Error: <error>': yes

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

144

| IP Flow | Information | Export | events |     |
| ------- | ----------- | ------ | ------ | --- |
ThefollowingaretheeventsrelatedtoIPFlowInformationExport(IPFIX).
| Event ID: | 15401 |     |     |     |
| --------- | ----- | --- | --- | --- |
Message FailedtoenablethedeliveryofIPFIXflowtelemetrypacketstotheCPU.
| Category | IPFIX |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description EventraisedwhenthereisafailuretoenablethedeliveryofIPFIXflowtelemetrypackets
totheCPU.
| IP Flow | Monitoring | Advertisement |     | events |
| ------- | ---------- | ------------- | --- | ------ |
ThefollowingaretheeventsrelatedtoIPFlowMonitoring(IPFM).
| Event ID: | 15101                              |     |     |     |
| --------- | ---------------------------------- | --- | --- | --- |
| Message   | FlowTrackingfeaturehasbeen{status} |     |     |     |
| Category  | IPFlowMonitoring                   |     |     |     |
| Severity  | Information                        |     |     |     |
Description LogeventthatindicatesglobalconfigurationforFlowTrackingfeature
| Event ID: | 15102 |     |     |     |
| --------- | ----- | --- | --- | --- |
Message
Linecard{node_id}is{status}
| Category    | IPFlowMonitoring                           |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Information                                |     |     |     |
| Description | linecardupevent                            |     |     |     |
| Event ID:   | 15103                                      |     |     |     |
| Message     | BULKSYNCeventreceivedfromlinecard{node_id} |     |     |     |
| Category    | IPFlowMonitoring                           |     |     |     |
| Severity    | Information                                |     |     |     |
Description
Bulksynceventreceived
| Event ID: | 15104 |     |     |     |
| --------- | ----- | --- | --- | --- |
IPFlowInformationExportevents|145

Message

BULK SYNC ALL request sent to all LC

Category

IP Flow Monitoring

Severity

Information

Description

bulk sync all event sent!

Event ID: 15105

Message

IPFMD Publisher is {status}

Category

IP Flow Monitoring

Severity

Information

Description

IPFMD Publisher status

Event ID: 15106

Message

FLUSH timer on LC {node_id} is {status}.

Category

IP Flow Monitoring

Severity

Information

Description

flush timer start/expire status!

Event ID: 15107

Message

IP Flow table utilization has exceeded high threshold on linecard {node_id}

Category

IP Flow Monitoring

Severity

Information

Description

IP Flow table utilization reached high threshold on a LC

Event ID: 15108

Message

IP Flow table utilization back to lower threshold on linecard {node_id}

Category

IP Flow Monitoring

Severity

Information

Description

IP Flow table utilization back to lower threshold on a LC

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

146

Chapter 43
|           |          |        |     | IP source | lockdown | events |
| --------- | -------- | ------ | --- | --------- | -------- | ------ |
| IP source | lockdown | events |     |           |          |        |
ThefollowingaretheeventsrelatedtoIPsourcelockdown.
| Event ID: | 9801 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message IP source-lockdown resource utilization has reached 80 percent of the
|          |     | supported limit  | of <max_supported_limit> |     | on the system |     |
| -------- | --- | ---------------- | ------------------------ | --- | ------------- | --- |
| Category |     | IPsourcelockdown |                          |     |               |     |
| Severity |     | Warning          |                          |     |               |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
reached80percentofthesupportedlimits
| Event ID: | 9802 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message IP source-lockdown resource utilization has exceeded maximum
supported limit of <max_supported_limit> on the system. IP source-
|          |     | lockdown functionality | will not | work for | new entries |     |
| -------- | --- | ---------------------- | -------- | -------- | ----------- | --- |
| Category |     | IPsourcelockdown       |          |          |             |     |
| Severity |     | Critical               |          |          |             |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
exceededthesupportedlimits
| Event ID: | 9803 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message IP source-lockdown resource utilization has reduced below 80 percent
|          |     | of the supported | limit of <max_supported_limit> |     | on the system |     |
| -------- | --- | ---------------- | ------------------------------ | --- | ------------- | --- |
| Category |     | IPsourcelockdown |                                |     |               |     |
| Severity |     | Information      |                                |     |               |     |
Description ThislogeventinformstheuserthatIP_SOURCE_LOCKDOWNresourceutilizationhas
reducedbelow80percentofthesupportedlimits
| Event ID: | 9804 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message IPv4 source-lockdown is enabled on interface <interface>
| Category |     | IPsourcelockdown |     |     |     |     |
| -------- | --- | ---------------- | --- | --- | --- | --- |
147
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

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

IP source lockdown events | 148

Chapter 44

IP tunnels events

IP tunnels events

The following are the events related to IP tunnels.

Event ID: 9601

Message

Tunnel Creation Failed - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

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

Tunnel Deletion Failed - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

149

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

Tunnel Destination IP Modified - Name (<tunnel_name>) Type (<type>)
VRF (<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

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

Tunnel MTU Modification Failed - Name (<tunnel_name>) Type (<type>)
VRF (<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>) MTU (<ip_mtu>)

Category

IP tunnels

Severity

Error

Description

Event raised when tunnel mtu modification failed

IP tunnels events | 150

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

151

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

Tunnel Nexthop Deleted - Name (<tunnel_name>) Type (<type>) VRF
(<vrf>) Local IP (<src_ip>) Remote IP (<dst_ip>)

Category

IP tunnels

Severity

Information

Description

Event raised when tunnel nexthop gets deleted

IP tunnels events | 152

Chapter 45
IP-SLA events
IP-SLA events
ThefollowingaretheeventsrelatedtoIP-SLA.
Event ID: 7401
Message IP-SLA session:<name> state changed to failed <state> due to reason
<reason>
| Category | IP-SLA |     |     |
| -------- | ------ | --- | --- |
| Severity | Error  |     |     |
Description EventraisedwhenanIP-SLAsessionstateischangedtoanyfailedstate
Event ID: 7402
Message IP-SLA session:<name> state changed to <state> due to reason <reason>
| Category | IP-SLA      |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description EventraisedwhenanIP-SLAsessionstateischangedtoanyinfostate
Event ID: 7403
| Message     | IP-SLA <name>:                                 | <operation> |     |
| ----------- | ---------------------------------------------- | ----------- | --- |
| Category    | IP-SLA                                         |             |     |
| Severity    | Information                                    |             |     |
| Description | EventraisedwhenanIP-SLAsessionisaddedordeleted |             |     |
Event ID: 7404
| Message     | IP-SLA session:<name>                        | is incomplete | to schedule |
| ----------- | -------------------------------------------- | ------------- | ----------- |
| Category    | IP-SLA                                       |               |             |
| Severity    | Error                                        |               |             |
| Description | EventraisedwhenanIP-SLAincompleconfigisadded |               |             |
Event ID: 7405
153
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message IP-SLA session:<name> interface <interface> is not ready and SLA is
disabled
| Category |     | IP-SLA |     |
| -------- | --- | ------ | --- |
| Severity |     | Error  |     |
Description EventraisedwhenanIP-SLAsessionstoppedduetosourceIPorinterfacechanges
| Event | ID: 7406 |     |     |
| ----- | -------- | --- | --- |
Message IP-SLA session:<name> interface <interface> is ready and SLA is
enabled
| Category |     | IP-SLA |     |
| -------- | --- | ------ | --- |
| Severity |     | Error  |     |
Description EventraisedwhenanIP-SLAsessionstartedduetosourceIPorinterfacechanges
| Event | ID: 7407 |     |     |
| ----- | -------- | --- | --- |
Message IP-SLA session:<name> failed to bind source, reason:<reason>
| Category    |          | IP-SLA                                           |     |
| ----------- | -------- | ------------------------------------------------ | --- |
| Severity    |          | Error                                            |     |
| Description |          | EventraisedwhenanIP-SLAsessionfailedtobindsource |     |
| Event       | ID: 7408 |                                                  |     |
Message IP-SLA session:<name> failed to initialize socket, reason:<reason>
| Category |     | IP-SLA |     |
| -------- | --- | ------ | --- |
| Severity |     | Error  |     |
Description EventraisedwhenanIP-SLAsessionfailedtoinitializesocket
| IPSec | tunnel | offload | events |
| ----- | ------ | ------- | ------ |
ThefollowingaretheeventsrelatedtoIPSectunneloffloadstates.
| Event    | ID: 14801 |                                      |     |
| -------- | --------- | ------------------------------------ | --- |
| Message  |           | PSectunnelisUP-TunnelId({tunnel_id}) |     |
| Category |           | IPSEC_TUNNEL_OFFLOAD                 |     |
| Severity |           | Information                          |     |
Description
EventraisedwhenIPSectunnelstateisup
IPSectunneloffloadevents|154

Event ID: 14802

Message

IPSec tunnel is DOWN - Tunnel Id ({tunnel_id})

Category

IPSEC_TUNNEL_OFFLOAD

Severity

Information

Description

Event raised when IPSec tunnel state is down

Event ID: 14803

Message

IPSec Tunnel is down due to VSX passive mode - Tunnel ({tunnel_id})

Category

IPSEC_TUNNEL_OFFLOAD

Severity

Information

Description

Event raised when IPSec tunnel state is down due to VSX passive mode

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

155

Chapter 46
|             |               | IPv6   | Router Advertisement | events |
| ----------- | ------------- | ------ | -------------------- | ------ |
| IPv6 Router | Advertisement | events |                      |        |
ThefollowingaretheeventsrelatedtoIPv6routeradvertisement.
| Event ID: 3901 |                               |                        |        |     |
| -------------- | ----------------------------- | ---------------------- | ------ | --- |
| Message        | ipv6 ra                       | enabled on interface:  | <intf> |     |
| Category       | IPv6RouterAdvertisement       |                        |        |     |
| Severity       | Information                   |                        |        |     |
| Description    | Eventraisedwhenipv6raenabled  |                        |        |     |
| Event ID: 3902 |                               |                        |        |     |
| Message        | ipv6 ra                       | disabled on interface: | <intf> |     |
| Category       | IPv6RouterAdvertisement       |                        |        |     |
| Severity       | Information                   |                        |        |     |
| Description    | Eventraisedwhenipv6radisabled |                        |        |     |
| Event ID: 3903 |                               |                        |        |     |
Message Disabled sending MTU in Router-Advertisement messages on <intf>
| Category       | IPv6RouterAdvertisement                      |     |     |     |
| -------------- | -------------------------------------------- | --- | --- | --- |
| Severity       | Information                                  |     |     |     |
| Description    | Eventraisedwhenipv6rasuppressmtuisconfigured |     |     |     |
| Event ID: 3904 |                                              |     |     |     |
Message Enabled sending MTU in Router-Advertisement messages on <intf>
| Category       | IPv6RouterAdvertisement                    |     |     |     |
| -------------- | ------------------------------------------ | --- | --- | --- |
| Severity       | Information                                |     |     |     |
| Description    | Eventraisedwhenipv6rasuppressmtuconfigured |     |     |     |
| Event ID: 3905 |                                            |     |     |     |
156
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Disabled sending RDNSS in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                        |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Information                                    |     |     |     |
| Description | Eventraisedwhenipv6rasuppressrdnssisconfigured |     |     |     |
Event ID: 3906
Message Enabled sending RDNSS in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |
| Description | Eventraisedwhenipv6rasuppressrdnssisremoved |     |     |     |
Event ID: 3907
Message Disabled sending DNSSL in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                        |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Information                                    |     |     |     |
| Description | Eventraisedwhenipv6rasuppressdnsslisconfigured |     |     |     |
Event ID: 3908
Message Enabled sending DNSSL in Router-Advertisement messages on <intf>
| Category    | IPv6RouterAdvertisement                     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |
| Description | Eventraisedwhenipv6rasuppressdnsslisremoved |     |     |     |
Event ID: 3909
| Message     | Interface:                            | <intf> | is added to router | discovery |
| ----------- | ------------------------------------- | ------ | ------------------ | --------- |
| Category    | IPv6RouterAdvertisement               |        |                    |           |
| Severity    | Information                           |        |                    |           |
| Description | Eventraisedwhenipv6rainterfaceisadded |        |                    |           |
Event ID: 3910
| Message | Interface: | <intf> | is deleted from | router discovery |
| ------- | ---------- | ------ | --------------- | ---------------- |
IPv6RouterAdvertisementevents|157

| Category    | IPv6RouterAdvertisement                 |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Eventraisedwhenipv6rainterfaceisdeleted |     |     |     |
Event ID: 3911
Message Added ipv6 prefix: <ipv6_addr>/<prefixlen> on interface: <intf>
| Category    | IPv6RouterAdvertisement                      |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- |
| Severity    | Information                                  |     |     |     |
| Description | Eventraisedwhenipv6addressisaddedoninterface |     |     |     |
Event ID: 3912
Message Deleted ipv6 prefix: <ipv6_addr>/<prefixlen> from interface: <intf>
| Category    | IPv6RouterAdvertisement                          |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | Information                                      |     |     |     |
| Description | Eventraisedwhenipv6addressisdeletedfrominterface |     |     |     |
Event ID: 3913
Message Added RA Prefix: <prefix> on interface: <intf> to prefix list
| Category    | IPv6RouterAdvertisement                   |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Information                               |     |     |     |
| Description | EventraisedwhenRAPrefixisaddedoninterface |     |     |     |
Event ID: 3914
Message Deleted RA Prefix: <prefix> on interface: <intf> from prefix list
| Category    | IPv6RouterAdvertisement                       |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | EventraisedwhenRAPrefixisdeletedfrominterface |     |     |     |
Event ID: 3915
| Message  | default prefix          | is configured | on interface | <intf> |
| -------- | ----------------------- | ------------- | ------------ | ------ |
| Category | IPv6RouterAdvertisement |               |              |        |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 158

| Severity    | Information                              |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Description | Eventraisedwhendefaultprefixisconfigured |     |     |
Event ID: 3916
| Message     | RDNSS is added              | on interface: | <intf> |
| ----------- | --------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement     |               |        |
| Severity    | Information                 |               |        |
| Description | EventraisedwhenRDNSSisadded |               |        |
Event ID: 3917
| Message     | RDNSS is deleted              | on interface: | <intf> |
| ----------- | ----------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement       |               |        |
| Severity    | Information                   |               |        |
| Description | EventraisedwhenRDNSSisdeleted |               |        |
Event ID: 3918
| Message     | DNSSL is added              | on interface: | <intf> |
| ----------- | --------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement     |               |        |
| Severity    | Information                 |               |        |
| Description | EventraisedwhenDNSSLisadded |               |        |
Event ID: 3919
| Message     | DNSSL is deleted              | on interface: | <intf> |
| ----------- | ----------------------------- | ------------- | ------ |
| Category    | IPv6RouterAdvertisement       |               |        |
| Severity    | Information                   |               |        |
| Description | EventraisedwhenDNSSLisdeleted |               |        |
Event ID: 3920
Message Added RA Route: <route> on interface: <intf> to route list
| Category    | IPv6RouterAdvertisement                  |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | EventraisedwhenRARouteisaddedoninterface |     |     |
IPv6RouterAdvertisementevents|159

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

160

Chapter 47
IRDP events
IRDP events
ThefollowingaretheeventsrelatedtoIRDP.
Event ID: 3501
| Message  | IRDP enabled | on interface | <interface> |
| -------- | ------------ | ------------ | ----------- |
| Category | IRDP         |              |             |
| Severity | Information  |              |             |
Description ThiscommandenablestheIRDP(ICMPRouterDiscoveryProtocol)featureoninterface.
Event ID: 3502
| Message  | IRDP disabled | on interface | <interface> |
| -------- | ------------- | ------------ | ----------- |
| Category | IRDP          |              |             |
| Severity | Information   |              |             |
Description ThiscommanddisablestheIRDP(ICMPRouterDiscoveryProtocol)featureoninterface.
Event ID: 3503
Message Interface: <interface> has been configured with the invalid irdp
|          | holdtime    | or minInterval | or maxInterval |
| -------- | ----------- | -------------- | -------------- |
| Category | IRDP        |                |                |
| Severity | Information |                |                |
Description EventraisedwhenirdpholdtimeormaxIntervalorminIntervalisimproper
ISSU events
ThefollowingaretheeventsrelatedtoIn-ServiceSoftwareUpgrade(ISSU)actions.
Event ID: 13501
Message {action}in-servicesoftwareupgradeto{location}operatingsystemimage{version}'
| Severity    | INFO                                      |     |     |
| ----------- | ----------------------------------------- | --- | --- |
| Category    | ISSU                                      |     |     |
| Description | EventtoindicateISSUhasstartedorcompleted' |     |     |
161
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Event ID: 13502

Message

Severity

Category

In-service software upgrade started operation {operation}' ISSU_ERROR

INFO

ISSU

Description

Event to indicate progress of ISSU'

Event ID: 13503

Message

Severity

Category

{error_type} during ISSU operation {operation}'

CRIT

ISSU

Description

A critical error occurred during ISSU'

Event ID: 13504

Message

Severity

Category

ISSU {condition}: {reason_message}'

CRIT

ISSU

Description

Indicates the reason ISSU aborted or failed'

Event ID: 13505

Message

Severity

ISSU {condition}: Feature "{feature}" not ready: {not_ready_reason}'

CRIT , not_ready_reason

Category

ISSU

Description

Indicates ISSU was aborted due to a feature not being ready'

Event ID: 13506

Message

Severity

Category

ISSU {condition}: Feature "{feature}" failed to prepare for ISSU'

CRIT

ISSU

Description

Indicates ISSU was aborted due to a feature failing to prepare for ISSU'

Event ID: 13507

ISSU events | 162

Message

Severity

Category

ISSU rollback timer has been started, {wait_time} minutes remaining before reboot'

INFO

ISSU

Description

Indicates ISSU rollback timer has been started'

Event ID: 13508

Message

Severity

Category

ISSU rollback timer is running, {wait_time} minutes remaining before reboot'

INFO

ISSU

Description

Indicates ISSU rollback timer is running'

Event ID: 13509

Message

Severity

ISSU has been accepted, the rollback timer has been stopped'

INFO

Description

Indicates last ISSU was accepted, and rollback timer will stop'

Category

ISSU

Event ID: 13510

Message

Severity

Category

Description

Event ID: 13511

Message

Severity

Category

'ISSU rollback timer expired, booting system to previous software version

INFO

ISSU

Indicates ISSU rollback timer expired and the system will boot to previous software
version'

'ISSU rollback timer expired. WARNING: previous software version {previous_software_
version} was not found, booting system to active bank {active_bank} with {new_software_
version} software version. This may cause issues with the current configuration'

INFO

ISSU

Description

'Indicates ISSU rollback timer expired and the system boot to new software version'

Event ID: 13512

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

163

Message

Severity

Category

ISSU rollback timer has been recreated, {wait_time} minutes remaining before reboot.'

INFO

ISSU

Description

Indicates ISSU rollback timer is running after an ISSUd restart'

ISSU events | 164

Chapter 48

Job scheduler events

Job scheduler events

The following are the events related to job scheduler.

Event ID: 12201

Message

Creating schedule <name>, trigger time(s): <start_datetime><details>

Category

Job scheduler (SCHEDULE)

Severity

Information

Description

Event reported when a schedule is created

Event ID: 12202

Message

Schedule <name> triggered, trigger_count: <trigger_count>

Category

Job scheduler (SCHEDULE)

Severity

Information

Description

Event reported when a schedule triggers

Event ID: 12203

Message

Timezone changed. Re-creating schedule <name>, trigger time(s):
<start_datetime><details>

Category

Job scheduler (SCHEDULE)

Severity

Information

Description

Event reported when the schedules are recreated due to timezone change.

Event ID: 13701

Message

Starting Job {job_name} due to Schedule {schedule_name}'s trigger

Category

Job scheduler (JOB)

Severity

Information

Description

Event reported when a job is executed

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

165

|          |          |        |     |     |          | Chapter  | 49     |
| -------- | -------- | ------ | --- | --- | -------- | -------- | ------ |
|          |          |        |     |     | L3 Encap | capacity | events |
| L3 Encap | capacity | events |     |     |          |          |        |
ThefollowingaretheeventsrelatedtoL3Encapcapacity.
| Event ID: | 10601 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
Message L3 resources critical for neighbor and route forwarding are low.
|          |     | Used: <encaps_allocated>, |     | Available: | <encaps_free> |     |     |
| -------- | --- | ------------------------- | --- | ---------- | ------------- | --- | --- |
| Category |     | L3Encapcapacity           |     |            |               |     |     |
| Severity |     | Warning                   |     |            |               |     |     |
Description L3resourcesneededforneighborandrouteforwardingarerunninglow.Large-scale
neighbormovescouldcausetrafficloss.
| Event ID: | 10602 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
Message L3 resources critical for neighbor and route forwarding are at safe
|          |     | levels. Used:   | <encaps_allocated>, |     | Available: | <encaps_free> |     |
| -------- | --- | --------------- | ------------------- | --- | ---------- | ------------- | --- |
| Category |     | L3Encapcapacity |                     |     |            |               |     |
| Severity |     | Information     |                     |     |            |               |     |
Description L3resourcesneededforneighborandrouteforwardingarebacktoasafelevel.
| Event ID: | 10603 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
Message Out of L3 resources critical for neighbor and route forwarding. Used:
|          |     | <encaps_allocated>, | Available: | <encaps_free> |     |     |     |
| -------- | --- | ------------------- | ---------- | ------------- | --- | --- | --- |
| Category |     | L3Encapcapacity     |            |               |     |     |     |
| Severity |     | Error               |            |               |     |     |     |
Description L3resourcesneededforneighborandrouteforwardinghaverunout.Trafficlossis
imminent.
166
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 50
|             |         |        |     | L3 Resource | Manager | events |
| ----------- | ------- | ------ | --- | ----------- | ------- | ------ |
| L3 Resource | Manager | events |     |             |         |        |
ThefollowingaretheeventsrelatedtoL3ResourceManager.
| Event ID: 11501 |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
Message IPv6 route prefix {prefix} is recommended for transit network use
only. The traffic would be software routed. Routing performance to
|                 | local                               | destination | addresses | on this network | may be impacted. |     |
| --------------- | ----------------------------------- | ----------- | --------- | --------------- | ---------------- | --- |
| Category        | L3ResourceManager                   |             |           |                 |                  |     |
| Severity        | Warning                             |             |           |                 |                  |     |
| Description     | logswarningforrouteadditionattempt. |             |           |                 |                  |     |
| Event ID: 11502 |                                     |             |           |                 |                  |     |
Message "Exceeded resource '<resource>' capacity adding <object>. Use 'show
|                 | capacities-status'                 |     | for more | information." | throttle_count: | 40  |
| --------------- | ---------------------------------- | --- | -------- | ------------- | --------------- | --- |
| Category        | L3ResourceManager                  |     |          |               |                 |     |
| Severity        | Error                              |     |          |               |                 |     |
| Description     | logserrorforrunningoutofresources. |     |          |               |                 |     |
| Event ID: 11503 |                                    |     |          |               |                 |     |
Message "Resource '<resource>' usage is at <percent>% of capacity. Use 'show
|                 | capacities-status'                          |     | for more | information." | throttle_count: | 40  |
| --------------- | ------------------------------------------- | --- | -------- | ------------- | --------------- | --- |
| Category        | L3ResourceManager                           |     |          |               |                 |     |
| Severity        | Warning                                     |     |          |               |                 |     |
| Description     | logswarningforhittingcertaincapacitylimits. |     |          |               |                 |     |
| Event ID: 11504 |                                             |     |          |               |                 |     |
Message OverlayECMProute{prefix}hasbeenprogrammedasasingleroute.
| Category | L3ResourceManager |     |     |     |     |     |
| -------- | ----------------- | --- | --- | --- | --- | --- |
| Severity | Information       |     |     |     |     |     |
Description logswarningwhenoverlayECMPgroupisprogrammedassingleroute.
167
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Event ID: 11505

Message

Traffic for IPv6 route prefix {prefix} will be software routed and performance impacted if

no other matching route prefixes from 0-64 for the same destination exist.

Category

L3 Resource Manager

Severity

Warning

Description

Logs warning that traffic might be routed in software for new route.

Event ID: 11506

Message

Tunnel {vtep} resolved nexthop {nexthop} removed.

Category

L3 Resource Manager

Severity

Information

Description

L3RM received event removing resolved nexthop from tunnel.

Event ID: 11507

Message

Tunnel {vtep} resolved nexthop {nexthop} added.

Category

L3 Resource Manager

Severity

Information

Description

L3RM received event adding resolved nexthop to tunnel.

L3 Resource Manager events | 168

Chapter 51
LACP events
LACP events
ThefollowingaretheeventsrelatedtoLACP.
Event ID: 1301
| Message     | Dynamic                  | LAG <lag_id> | created |     |
| ----------- | ------------------------ | ------------ | ------- | --- |
| Category    | LACP                     |              |         |     |
| Severity    | Information              |              |         |     |
| Description | DynamicLAGhasbeencreated |              |         |     |
Event ID: 1302
| Message     | Dynamic                  | LAG <lag_id> | deleted |     |
| ----------- | ------------------------ | ------------ | ------- | --- |
| Category    | LACP                     |              |         |     |
| Severity    | Information              |              |         |     |
| Description | DynamicLAGhasbeendeleted |              |         |     |
Event ID: 1303
Message Interface <intf_id> added to LAG <lag_id>. Existing configuration on
|             | interface                         | <intf_id> | will be removed. |     |
| ----------- | --------------------------------- | --------- | ---------------- | --- |
| Category    | LACP                              |           |                  |     |
| Severity    | Information                       |           |                  |     |
| Description | LogwheninterfacehasbeenaddedtoLAG |           |                  |     |
Event ID: 1304
Message Interface <intf_id> removed from LAG <lag_id>. It will be set with
|             | default                               | configuration | with admin | down state. |
| ----------- | ------------------------------------- | ------------- | ---------- | ----------- |
| Category    | LACP                                  |               |            |             |
| Severity    | Information                           |               |            |             |
| Description | LogwheninterfacehasbeenremovedfromLAG |               |            |             |
Event ID: 1305
169
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | LACP system                    | priority | set to <system_priority> |
| ----------- | ------------------------------ | -------- | ------------------------ |
| Category    | LACP                           |          |                          |
| Severity    | Information                    |          |                          |
| Description | LogwhenLACPsystempriorityisset |          |                          |
Event ID: 1306
| Message     | LACP mode            | set to <lacp_mode> | for LAG <lag_id> |
| ----------- | -------------------- | ------------------ | ---------------- |
| Category    | LACP                 |                    |                  |
| Severity    | Information          |                    |                  |
| Description | LogwhenLACPmodeisset |                    |                  |
Event ID: 1307
| Message     | LACP system              | ID set | to <system_id> |
| ----------- | ------------------------ | ------ | -------------- |
| Category    | LACP                     |        |                |
| Severity    | Information              |        |                |
| Description | LogwhenLACPsystemIDisset |        |                |
Event ID: 1308
| Message     | LACP rate            | set to <lacp_rate> | for LAG <lag_id> |
| ----------- | -------------------- | ------------------ | ---------------- |
| Category    | LACP                 |                    |                  |
| Severity    | Information          |                    |                  |
| Description | LogwhenLACPrateisset |                    |                  |
Event ID: 1309
Message Partner is detected for interface <intf_id> LAG <lag_id>: <partner_
sys_id>. Actor state: <actor_state>, partner state <partner_state>
| Category    | LACP                         |     |     |
| ----------- | ---------------------------- | --- | --- |
| Severity    | Information                  |     |     |
| Description | LogwhenLACPpartnerisdetected |     |     |
Event ID: 1310
Message Partner is out of sync for interface <intf_id> LAG <lag_id>. Actor
LACPevents|170

|             | state:                       | <actor_state>, | partner state | <partner_state> |
| ----------- | ---------------------------- | -------------- | ------------- | --------------- |
| Category    | LACP                         |                |               |                 |
| Severity    | Warning                      |                |               |                 |
| Description | LogwhenLACPparterisoutofsync |                |               |                 |
Event ID: 1311
Message Partner is lost (timed out) for interface <intf_id> LAG <lag_id>.
State: <fsm_state>
| Category    | LACP                               |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Warning                            |     |     |     |
| Description | LogtoindicatethatLACPpartnerislost |     |     |     |
Event ID: 1312
| Message     | Failed                     | to create LAG | <lag_id> |     |
| ----------- | -------------------------- | ------------- | -------- | --- |
| Category    | LACP                       |               |          |     |
| Severity    | Error                      |               |          |     |
| Description | LogwhenLAGcreationisfailed |               |          |     |
Event ID: 1313
| Message     | LAG <lag_id>        | set as | VSX |     |
| ----------- | ------------------- | ------ | --- | --- |
| Category    | LACP                |        |     |     |
| Severity    | Information         |        |     |     |
| Description | LogwhenVSXiscreated |        |     |     |
Event ID: 1314
Message LAG <lag_id> not sending LACPDUs through interface <intf_id> because
|          | VSX information | is  | not complete |     |
| -------- | --------------- | --- | ------------ | --- |
| Category | LACP            |     |              |     |
| Severity | Information     |     |              |     |
Description LogwhenLAGisnotsendingLACPDUsthroughinterfacebecauseVSXinformationis
incomplete
Event ID: 1315
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 171

Message LACP fallback mode set to <lacp_fallback_mode> for lag <lag_id>
| Category    | LACP                         |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Error                        |     |     |     |
| Description | LogwhenLACPfallbackmodeisset |     |     |     |
Event ID: 1316
Message LACP fallback timeout set to <lacp_fallback_timeout> for lag <lag_id>
| Category    | LACP                            |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- |
| Severity    | Error                           |     |     |     |
| Description | LogwhenLACPfallbacktimeoutisset |     |     |     |
Event ID: 1317
Message LACP fallback timeout <lacp_fallback_timeout> expired for lag <lag_
id>
| Category    | LACP                                |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Error                               |     |     |     |
| Description | LogwhenLACPfallbacktimeoutisexpired |     |     |     |
Event ID: 1318
Message Interface <intf_id> enabled by fallback for lag <lag_id>
| Category    | LACP                                |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Error                               |     |     |     |
| Description | Logwheninterfaceisenabledbyfallback |     |     |     |
Event ID: 1319
| Message  | LAG global  | load balancing | mode is set | to <mode> |
| -------- | ----------- | -------------- | ----------- | --------- |
| Category | LACP        |                |             |           |
| Severity | Information |                |             |           |
Description LogstosetgloballoadbalancingmodeforLAGinterfaces.
Event ID: 1320
LACPevents|172

Message LAG load balancing mode is set to <mode> for lag <lag_id>
| Category | LACP        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogstosetperportloadbalancingmodeforLAGinterface.
Event ID: 1321
Message LAG <lag_id> State change for interface <intf_id>: Actor state:
|          | <actor_state>, | Partner | state <partner_state> |
| -------- | -------------- | ------- | --------------------- |
| Category | LACP           |         |                       |
| Severity | Information    |         |                       |
Description LogsthatcapturechangestoLACPstateforLAGinterface.
Event ID: 1322
Message Interface <intf_name> cannot be part of Lag <lag_number>. Speed
mismatched (Interface speed <port_speed>Mbps Lag base speed <lag_
|          | speed>Mbps).' | throttle_count: | 100 |
| -------- | ------------- | --------------- | --- |
| Category | LACP          |                 |     |
| Severity | Information   |                 |     |
Description LogstocaptureifLACPprotocoldoesnotallowinterfacetobepartoflagduetospeed
mismatch.
Event ID: 1323
| Message     | Fallback                                        | is <fallback> | for LAG <lag_id> |
| ----------- | ----------------------------------------------- | ------------- | ---------------- |
| Category    | LACP                                            |               |                  |
| Severity    | Information                                     |               |                  |
| Description | LogstocaptureiffallbackischangedforLAGinterface |               |                  |
Event ID: 1324
| Message     | LACP Graceful                                  | Shut is | initiated |
| ----------- | ---------------------------------------------- | ------- | --------- |
| Category    | LACP                                           |         |           |
| Severity    | Information                                    |         |           |
| Description | LogsthatcaputreLACPGracefulShutforLAGinterface |         |           |
Event ID: 1325
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 173

| Message     | LACP Graceful                                  | Shut is completed |
| ----------- | ---------------------------------------------- | ----------------- |
| Category    | LACP                                           |                   |
| Severity    | Information                                    |                   |
| Description | LogsthatcaputreLACPGracefulShutforLAGinterface |                   |
Event ID: 1326
Message
Interface{intf_id}enabledbyfallback-staticforlag{lag_id}
| Category | LACP        |     |
| -------- | ----------- | --- |
| Severity | Information |     |
Description
Logwheninterfaceisenabledbyfallback-static
Event ID: 1327
Message Interface{intf_id}disabledbyfallback-staticforlag{lag_id}
| Category    | LACP                                        |     |
| ----------- | ------------------------------------------- | --- |
| Severity    | Information                                 |     |
| Description | Logwheninterfaceisdisabledbyfallback-static |     |
Event ID: 1328
Message
Interface{intf_id}lag{lag_id}blockedaslinkpartnersonvsxprimaryandsecondary
mismatch
| Category | LACP        |     |
| -------- | ----------- | --- |
| Severity | Information |     |
Description
Logwheninterfaceisblockedduetomismatchingpartneronthevsxinterface
LACPevents|174

Chapter 52
LAG events
LAG events
ThefollowingaretheeventsrelatedtoLAG.
Event ID: 1401
| Message     | Trunk set               | succeeds unit | <unit> lag_id | <lag_id> |
| ----------- | ----------------------- | ------------- | ------------- | -------- |
| Category    | LAG                     |               |               |          |
| Severity    | Information             |               |               |          |
| Description | Logsthecreationoftrunk. |               |               |          |
Event ID: 1402
Message Lag creation failed unit <unit> lag_id <lag_id> rc <rc> error <error>
| Category    | LAG                            |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | Logsthefailureoftrunkcreation. |     |     |     |
Event ID: 1403
Message Destroy lag failed on unit <unit> lag_id <lag_id> rc <rc> error
<error>
| Category    | LAG                           |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Severity    | Error                         |     |     |     |
| Description | Logsthefailureoftrunkdestroy. |     |     |     |
Event ID: 1404
Message Trunk member add port succeeds on unit <unit> hw_port <hw_port> tid
<tid>
| Category    | LAG                           |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Severity    | Debug                         |     |     |     |
| Description | Logstheadditionofporttotrunk. |     |     |     |
Event ID: 1405
175
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Trunk port attach error on hw_port <hw_port> tid <tid> rc <rc>
<error>
| Category    | LAG                                    |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- |
| Severity    | Error                                  |     |     |     |
| Description | Logsthefailureofadditionofporttotrunk. |     |     |     |
Event ID: 1406
Message Failed to set egress enable on hw_port <hw_port> tid <tid> rc <rc>
error <error>
| Category    | LAG                              |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- |
| Severity    | Error                            |     |     |     |
| Description | Logsthefailuretosetegressenable. |     |     |     |
Event ID: 1407
Message Failed to delete hw_port <hw_port> from tid <tid> rc <rc> error
<error>
| Category    | LAG                          |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Error                        |     |     |     |
| Description | Logsthefailuretodeleteaport. |     |     |     |
Event ID: 1408
Message Trunk psc set failed on unit <unit> lag_id <lag_id> psc <psc> rc <rc>
error <error>
| Category    | LAG                                       |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Error                                     |     |     |     |
| Description | Logsthefailuretosetportselectioncriteria. |     |     |     |
Event ID: 1409
| Message     | LAG <interface>,                                 | set to load | balance mode | to <mode> |
| ----------- | ------------------------------------------------ | ----------- | ------------ | --------- |
| Category    | LAG                                              |             |              |           |
| Severity    | Information                                      |             |              |           |
| Description | logstosetloadbalancingmodeforLAGL2/L3interfaces. |             |              |           |
Event ID: 1410
LAGevents|176

| Message     | Add port                 | <port> to LAG    | <interface>     |
| ----------- | ------------------------ | ---------------- | --------------- |
| Category    | LAG                      |                  |                 |
| Severity    | Information              |                  |                 |
| Description | logstoaddporttoLAG.      |                  |                 |
| Event ID:   | 1411                     |                  |                 |
| Message     | Remove                   | port <port> from | LAG <interface> |
| Category    | LAG                      |                  |                 |
| Severity    | Information              |                  |                 |
| Description | logstoremoveportfromLAG. |                  |                 |
| Event ID:   | 1412                     |                  |                 |
Message Add port <port> to vlan <vlan> for L3 LAG <interface>
| Category    | LAG                   |     |     |
| ----------- | --------------------- | --- | --- |
| Severity    | Information           |     |     |
| Description | logstoaddporttoL3LAG. |     |     |
| Event ID:   | 1413                  |     |     |
Message Remove port <port> to vlan <vlan> for L3 LAG <interface>
| Category    | LAG                      |                  |             |
| ----------- | ------------------------ | ---------------- | ----------- |
| Severity    | Information              |                  |             |
| Description | logstoremoveportfromLAG. |                  |             |
| Event ID:   | 1414                     |                  |             |
| Message     | Destroy                  | L3 LAG interface | <interface> |
| Category    | LAG                      |                  |             |
| Severity    | Information              |                  |             |
| Description | logstodestroyL3LAG.      |                  |             |
| Launch      | Daemon                   | (LaunchD)events  |             |
Thefollowingaretheeventsrelatedadaemonbeinglaunched.
| Event ID: | 14902 |     |     |
| --------- | ----- | --- | --- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 177

Message

Category

Severity

Failed to start {daemon} daemon

LAUNCHD

Error

Description

Event raised when a daemon failed to start on config availability

Launch Daemon (LaunchD)events | 178

Chapter 53
|                   |        |     |     | Layer | 3 Interface | events |
| ----------------- | ------ | --- | --- | ----- | ----------- | ------ |
| Layer 3 Interface | events |     |     |       |             |        |
Thefollowingaretheeventsrelatedtolayer3interface.
Event ID: 1701
| Message     | L3-Interface             | <interface>, | created |     |     |     |
| ----------- | ------------------------ | ------------ | ------- | --- | --- | --- |
| Category    | Layer3Interface          |              |         |     |     |     |
| Severity    | Information              |              |         |     |     |     |
| Description | logstocreateL3interface. |              |         |     |     |     |
Event ID: 1702
| Message     | L3-Interface             | <interface>, | deleted |     |     |     |
| ----------- | ------------------------ | ------------ | ------- | --- | --- | --- |
| Category    | Layer3Interface          |              |         |     |     |     |
| Severity    | Information              |              |         |     |     |     |
| Description | logstodeleteL3interface. |              |         |     |     |     |
Event ID: 1703
Message Interface <interface>, configured administratively <state>
| Category    | Layer3Interface                 |     |     |     |     |     |
| ----------- | ------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                     |     |     |     |     |     |
| Description | logsforadminstateofL3interface. |     |     |     |     |     |
Event ID: 1704
Message Failed to create <vlanid> for layer 3 interface <interface>
| Category    | Layer3Interface                                 |     |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Error                                           |     |     |     |     |     |
| Description | logserrorswhilecreatingvlanforlayer3interfaces. |     |     |     |     |     |
Event ID: 1705
179
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Failed to destroy layer 3 interface <interface> vlan <vlanid>, error:
<err>
| Category    | Layer3Interface                                   |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Error                                             |     |     |
| Description | logserrorswhiledestroyingvlanforlayer3interfaces. |     |     |
Event ID: 1706
Message Failed to delete an l3 interface <interface>, error: <err>
| Category    | Layer3Interface                           |     |     |
| ----------- | ----------------------------------------- | --- | --- |
| Severity    | Error                                     |     |     |
| Description | logserrorswhiledestroyinglayer3interface. |     |     |
Event ID: 1707
Message Failed to add L3 host entry for ip <ipaddr>, error: <err>' throttle_
count: 1
| Category    | Layer3Interface               |     |     |
| ----------- | ----------------------------- | --- | --- |
| Severity    | Error                         |     |     |
| Description | logserrorswhileaddingl3hosts. |     |     |
Event ID: 1708
| Message     | Added L3 host           | entry for | ip <ipaddr> |
| ----------- | ----------------------- | --------- | ----------- |
| Category    | Layer3Interface         |           |             |
| Severity    | Information             |           |             |
| Description | logswhileaddingl3hosts. |           |             |
Event ID: 1709
Message Failed to delete L3 host entry for ip <ipaddr>, error: <err>
| Category    | Layer3Interface                 |     |     |
| ----------- | ------------------------------- | --- | --- |
| Severity    | Error                           |     |     |
| Description | logserrorswhiledeletingl3hosts. |     |     |
Event ID: 1710
Layer3Interfaceevents|180

| Message     | Deleted                   | L3 host entry | for ip <ipaddr> |     |
| ----------- | ------------------------- | ------------- | --------------- | --- |
| Category    | Layer3Interface           |               |                 |     |
| Severity    | Information               |               |                 |     |
| Description | logswhiledeletingl3hosts. |               |                 |     |
Event ID: 1711
| Message     | Failed                                  | to get L3 host | hit for | ip <ipaddr> |
| ----------- | --------------------------------------- | -------------- | ------- | ----------- |
| Category    | Layer3Interface                         |                |         |             |
| Severity    | Error                                   |                |         |             |
| Description | logserrorstogetL3hosthitforaspecificip. |                |         |             |
Event ID: 1712
| Message     | L3 interface          | error: | <err> |     |
| ----------- | --------------------- | ------ | ----- | --- |
| Category    | Layer3Interface       |        |       |     |
| Severity    | Error                 |        |       |     |
| Description | logsforL3setuperrors. |        |       |     |
Event ID: 1713
Message Added Nexthop <nexthop>, egress_id <egress_id>, for route <prefix>
| Category    | Layer3Interface         |     |     |     |
| ----------- | ----------------------- | --- | --- | --- |
| Severity    | Information             |     |     |     |
| Description | logsfornexthopaddition. |     |     |     |
Event ID: 1714
| Message     | Delete                  | Nexthop <nexthop> | for route | <prefix> |
| ----------- | ----------------------- | ----------------- | --------- | -------- |
| Category    | Layer3Interface         |                   |           |          |
| Severity    | Information             |                   |           |          |
| Description | logsfornexthopdeletion. |                   |           |          |
Event ID: 1715
| Message | Added route | <prefix> |     |     |
| ------- | ----------- | -------- | --- | --- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 181

| Category    | Layer3Interface       |     |     |     |     |
| ----------- | --------------------- | --- | --- | --- | --- |
| Severity    | Information           |     |     |     |     |
| Description | logsforrouteaddition. |     |     |     |     |
Event ID: 1716
| Message     | Update:             | route state: | <state> |     |     |
| ----------- | ------------------- | ------------ | ------- | --- | --- |
| Category    | Layer3Interface     |              |         |     |     |
| Severity    | Information         |              |         |     |     |
| Description | logsforrouteupdate. |              |         |     |     |
Event ID: 1717
| Message     | Delete                | route <prefix> |     |     |     |
| ----------- | --------------------- | -------------- | --- | --- | --- |
| Category    | Layer3Interface       |                |     |     |     |
| Severity    | Information           |                |     |     |     |
| Description | logsforroutedeletion. |                |     |     |     |
Event ID: 1718
| Message     | Delete                     | route <prefix>, | error: <err> |     |     |
| ----------- | -------------------------- | --------------- | ------------ | --- | --- |
| Category    | Layer3Interface            |                 |              |     |     |
| Severity    | Error                      |                 |              |     |     |
| Description | logserrorforroutedeletion. |                 |              |     |     |
Event ID: 1719
| Message     | Add route                     | <prefix>, | error: <err>' | throttle_count: | 1   |
| ----------- | ----------------------------- | --------- | ------------- | --------------- | --- |
| Category    | Layer3Interface               |           |               |                 |     |
| Severity    | Error                         |           |               |                 |     |
| Description | logserrorforrouteaditiontion. |           |               |                 |     |
Event ID: 1720
Message Error creating egress object for port <port>, error: <err>
| Category | Layer3Interface |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
Layer3Interfaceevents|182

| Severity    | Error                              |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Description | logserrorsforegressobjectcreation. |     |     |     |
Event ID: 1721
Message Created L3 egress ID <egress_id> for port <port> intf <intf>
| Category    | Layer3Interface              |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Information                  |     |     |     |
| Description | logsforegressobjectcreation. |     |     |     |
Event ID: 1722
Message Error deleting egress object for port <port>, error: <err>
| Category    | Layer3Interface                    |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Error                              |     |     |     |
| Description | logserrorsforegressobjectdeletion. |     |     |     |
Event ID: 1723
| Message     | Deleted                      | L3 egress | ID <egress_id> | for port <port> |
| ----------- | ---------------------------- | --------- | -------------- | --------------- |
| Category    | Layer3Interface              |           |                |                 |
| Severity    | Information                  |           |                |                 |
| Description | logsforegressobjectdeletion. |           |                |                 |
Event ID: 1724
Message Interface <interface>, configured with ipv4 address <value>
| Category    | Layer3Interface                      |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | logsforipv4addressupdateoninterface. |     |     |     |
Event ID: 1725
Message Interface <interface>, configured with ipv6 address <value>
| Category    | Layer3Interface                      |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | logsforipv6addressupdateoninterface. |     |     |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 183

Event ID: 1726
| Message     | Interface                              | <interface>, | ipv4 address | deleted <value> |
| ----------- | -------------------------------------- | ------------ | ------------ | --------------- |
| Category    | Layer3Interface                        |              |              |                 |
| Severity    | Information                            |              |              |                 |
| Description | logsforipv4addressdeletefrominterface. |              |              |                 |
Event ID: 1727
| Message     | Interface                              | <interface>, | ipv6 address | deleted <value> |
| ----------- | -------------------------------------- | ------------ | ------------ | --------------- |
| Category    | Layer3Interface                        |              |              |                 |
| Severity    | Information                            |              |              |                 |
| Description | logsforipv6addressdeletefrominterface. |              |              |                 |
Event ID: 1728
Message IPv6 Address Status: Interface <intf>, address <addr>, status <addr_
status>
| Category    | Layer3Interface                         |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Eventraisedwhenipv6addressstatuschanges |     |     |     |
Event ID: 1729
Message Interface <interface>, configured with secondary ipv4 address <value>
| Category    | Layer3Interface                               |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | logsforsecondaryipv4addressupdateoninterface. |     |     |     |
Event ID: 1730
Message Interface <interface>, secondary ipv4 address deleted <value>
| Category    | Layer3Interface                                 |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |
| Description | logsforsecondaryipv4addressdeletefrominterface. |     |     |     |
Event ID: 1731
Layer3Interfaceevents|184

Message

IP MTU <mtu> not applied due to hardware resource limitation

Category

Layer 3 Interface

Severity

Error

Description

Logs failure while configuring hardware for IPMTU.

Event ID: 1732

Message

IPv6 address {value} is not applied on interface {interface}, as only
one global ipv6 address will be in effect.

Category

Layer 3 Interface

Severity

Error

Description

Logs failure while configuring more than one global ipv6 address on an interface.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

185

Chapter 54
LED events
LED events
ThefollowingaretheeventsrelatedtoLED.
Event ID: 501
| Message     | There are                           | <count> LED | types in subsystem | <subsystem> |
| ----------- | ----------------------------------- | ----------- | ------------------ | ----------- |
| Category    | LED                                 |             |                    |             |
| Severity    | Information                         |             |                    |             |
| Description | LogaboutnumberofLEDtypesinsubsystem |             |                    |             |
Event ID: 502
Message There are <count> LED configs in subsystem <subsystem>
| Category    | LED                                  |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | LogaboutnumberofLEDconfiginsubsystem |     |     |     |
186
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 55
LLDP events
LLDP events
ThefollowingaretheeventsrelatedtoLLDP.
Event ID: 101
| Message  | LLDP Enabled |     |     |
| -------- | ------------ | --- | --- |
| Category | LLDP         |     |     |
| Severity | Information  |     |     |
Description LogseventwhenLLDP(LinkLayerDiscoveryProtocol)featureisenabledintheswitch.
Event ID: 102
| Message  | LLDP Disabled |     |     |
| -------- | ------------- | --- | --- |
| Category | LLDP          |     |     |
| Severity | Information   |     |     |
Description LogseventwhenLLDP(LinkLayerDiscoveryProtocol)featureisdisabledintheswitch.
Event ID: 103
| Message  | Configured  | LLDP tx-timer | to <value> |
| -------- | ----------- | ------------- | ---------- |
| Category | LLDP        |               |            |
| Severity | Information |               |            |
Description LogseventwhentheLLDPstatusupdateintervalisconfiguredbytheuser.
Event ID: 104
| Message  | LLDP neighbor | <chassisid> | added on <interface> |
| -------- | ------------- | ----------- | -------------------- |
| Category | LLDP          |             |                      |
| Severity | Information   |             |                      |
Description Logseventwhenanewneighborentryisaddedtotheswitch.
Event ID: 105
187
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message LLDP neighbor <chassisid> updated on <interface>' throttle_count: 100
| Category | LLDP        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Logseventwhenanexistingneighborentryisupdatedintheswitch.
Event ID: 106
| Message  | LLDP neighbor | <chassisid> | deleted | on <interface> |
| -------- | ------------- | ----------- | ------- | -------------- |
| Category | LLDP          |             |         |                |
| Severity | Information   |             |         |                |
Description Logseventwhenanexistingneighborentryisdeletedfromswitch.
Event ID: 107
| Message  | Configured  | LLDP Management | IP <value> |     |
| -------- | ----------- | --------------- | ---------- | --- |
| Category | LLDP        |                 |            |     |
| Severity | Information |                 |            |     |
Description LogseventwhenanewmanagementIPaddressisconfiguredbytheuser.
Event ID: 108
| Message  | Configured  | LLDP tx-hold | to <hold> |     |
| -------- | ----------- | ------------ | --------- | --- |
| Category | LLDP        |              |           |     |
| Severity | Information |              |           |     |
Description LogseventwhenLLDPtransmitmultipliervalueisconfiguredbytheuser.
Event ID: 109
| Message  | Configured  | LLDP tx-delay | to <value> |     |
| -------- | ----------- | ------------- | ---------- | --- |
| Category | LLDP        |               |            |     |
| Severity | Information |               |            |     |
Description LogseventwhenLLDPtransmitdelayvalueisconfiguredbytheuser.
Event ID: 110
| Message | Configured | LLDP reinit-delay | to <value> |     |
| ------- | ---------- | ----------------- | ---------- | --- |
LLDPevents|188

| Category | LLDP        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogseventwhenLLDPinterfacereinitializationvalueisconfiguredbytheuser.
Event ID: 111
| Message  | LLDP statistics | cleared |     |
| -------- | --------------- | ------- | --- |
| Category | LLDP            |         |     |
| Severity | Information     |         |     |
Description LogseventwhenLLDPstatisticsareclearedfromtheswitch.
Event ID: 112
| Message  | LLDP neighbor | info cleared |     |
| -------- | ------------- | ------------ | --- |
| Category | LLDP          |              |     |
| Severity | Information   |              |     |
Description LogseventwhenLLDPneighborinformationisclearedfromtheswitch.
Event ID: 113
Message PVID mismatch on <interface> pvid = <pvid>, Neighbor <chassisid>
|          | port_id     | = <ninterface> | pvid = <npvid> |
| -------- | ----------- | -------------- | -------------- |
| Category | LLDP        |                |                |
| Severity | Information |                |                |
Description LogeventwhenthePVIDmismatchesbetweentheswitchandneighboroveran
interface.
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 189

Chapter 56
Loop Protect events
| Loop Protect events |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
Thefollowingaretheeventsrelatedtoloopprotect.
Event ID: 2801
Message Port <portName> is disabled by Loop-protection after loop detection
|             | on VLAN <vlan>                |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- |
| Category    | LoopProtect                   |     |     |     |
| Severity    | Warning                       |     |     |     |
| Description | LogsportdisabledbyLoopprotect |     |     |     |
Event ID: 2802
Message Ports TX <txportName> and RX <rxportName> are disabled by Loop-
|             | protect after                 | loop detection | on VLAN <vlan> |     |
| ----------- | ----------------------------- | -------------- | -------------- | --- |
| Category    | LoopProtect                   |                |                |     |
| Severity    | Warning                       |                |                |     |
| Description | LogsportdisabledbyLoopprotect |                |                |     |
Event ID: 2803
| Message     | Loop detected                    | on port <portName> | on VLAN | <vlan> |
| ----------- | -------------------------------- | ------------------ | ------- | ------ |
| Category    | LoopProtect                      |                    |         |        |
| Severity    | Warning                          |                    |         |        |
| Description | LogsportwhichreceivesPDUofitsown |                    |         |        |
Event ID: 2804
| Message     | Port <portName>                         | enabled after | disable time | expired |
| ----------- | --------------------------------------- | ------------- | ------------ | ------- |
| Category    | LoopProtect                             |               |              |         |
| Severity    | Information                             |               |              |         |
| Description | Logsportenabledafterdisabledtimeexpired |               |              |         |
Event ID: 2805
190
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Port <portName> | added for | loop-protection |
| ----------- | --------------- | --------- | --------------- |
| Category    | LoopProtect     |           |                 |
| Severity    | Information     |           |                 |
| Description | Logsportadded   |           |                 |
Event ID: 2806
| Message     | Port <portName> | deleted | from loop-protection |
| ----------- | --------------- | ------- | -------------------- |
| Category    | LoopProtect     |         |                      |
| Severity    | Information     |         |                      |
| Description | Logsportdeleted |         |                      |
Event ID: 2807
| Message     | Loop-Protection                    | stats cleared | for port <portName> |
| ----------- | ---------------------------------- | ------------- | ------------------- |
| Category    | LoopProtect                        |               |                     |
| Severity    | Information                        |               |                     |
| Description | Loop-Protectionstatsclearedforport |               |                     |
Event ID: 2808
Message Ports TX <txportName> and RX <rxportName> are involved during TX port
disabling
| Category    | LoopProtect                                  |     |     |
| ----------- | -------------------------------------------- | --- | --- |
| Severity    | Information                                  |     |     |
| Description | LogsTXandRXportsafterTXdisabledbyLoopprotect |     |     |
Event ID: 2809
Message Port{portName}isdisabledbyLoop-protectionafterloopdetectiononVLAN{vlan}
| Category    | LoopProtect                   |     |     |
| ----------- | ----------------------------- | --- | --- |
| Severity    | Warning                       |     |     |
| Description | LogsportdisabledbyLoopprotect |     |     |
Event ID: 2810
LoopProtectevents|191

Message

Ports TX {txportName} and RX {rxportName} are involved during RX port disabling

Category

Loop Protect

Severity

Information

Description

Logs TX and RX ports after RX disabled by Loop protect

Event ID: 2811

Message

Max vport limit {vportLimit} reached. Current vport {currvportCount}

Category

Loop Protect

Severity

Information

Description

Logs max vport limit reached and Current vport count.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

192

Chapter 57
Loopback events
Loopback events
Thefollowingaretheeventsrelatedtoloopback.
Event ID: 901
| Message     | Loopback Interface                | <interface>, | created |
| ----------- | --------------------------------- | ------------ | ------- |
| Category    | Loopback                          |              |         |
| Severity    | Information                       |              |         |
| Description | Logwhenloopbackinterfaceiscreated |              |         |
Event ID: 902
| Message     | Loopback Interface                | <interface>, | deleted |
| ----------- | --------------------------------- | ------------ | ------- |
| Category    | Loopback                          |              |         |
| Severity    | Information                       |              |         |
| Description | Logwhenloopbackinterfaceisdeleted |              |         |
Event ID: 903
Message Loopback Interface <interface>, configured administratively <state>
| Category    | Loopback                            |     |     |
| ----------- | ----------------------------------- | --- | --- |
| Severity    | Information                         |     |     |
| Description | Logaboutloopbackinterfaceadminstate |     |     |
193
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 58
|             |            |        | MAC address | management | events |
| ----------- | ---------- | ------ | ----------- | ---------- | ------ |
| MAC address | management | events |             |            |        |
ThefollowingaretheeventsrelatedtoMACaddressmanagement.
| Event ID: 4801 |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
Message MAC <mac> moved from port <from-intf> to port <to-intf> on VLAN
<vlan>
| Category       | MACaddressmanagement     |     |     |     |     |
| -------------- | ------------------------ | --- | --- | --- | --- |
| Severity       | Information              |     |     |     |     |
| Description    | EventraisedwhenL2macmove |     |     |     |     |
| Event ID: 4802 |                          |     |     |     |     |
Message All dynamic MAC addresses on VLAN <vlan> were flushed
| Category | MACaddressmanagement |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- |
| Severity | Information          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithvlandeleteeventorclearmac-address
commandfromvtysh
| Event ID: 4803 |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
Message All dynamic MAC addresses on port <intf> were flushed
| Category | MACaddressmanagement |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- |
| Severity | Information          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithportmovetoL3eventorclearmac-
addresscommandfromvtysh
| Event ID: 4804 |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
Message All dynamic MAC addresses on port <intf> were flushed
| Category | MACaddressmanagement |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- |
| Severity | Information          |     |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithportdowneventorclearmac-address
commandfromvtysh
| Event ID: 4805 |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
194
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message All dynamic MAC addresses on VLAN <vlan> were flushed
| Category | MACaddressmanagement |     |     |     |
| -------- | -------------------- | --- | --- | --- |
| Severity | Information          |     |     |     |
Description EventraisedwhenL2MACtableisflushedwithvlandowneventorclearmac-address
commandfromvtysh
Event ID: 4806
| Message  | L2X thread           | not running. | Attempting | to recover |
| -------- | -------------------- | ------------ | ---------- | ---------- |
| Category | MACaddressmanagement |              |            |            |
| Severity | Warning              |              |            |            |
Description EventraisedwhenBCML2Xthreadisidentifiedasnotrunning
Event ID: 4807
| Message  | L2X thread           | recovered |     |     |
| -------- | -------------------- | --------- | --- | --- |
| Category | MACaddressmanagement |           |     |     |
| Severity | Warning              |           |     |     |
Description EventraisedwhenBCML2Xthreadissuccessfullyrecovered
Event ID: 4808
| Message     | L2X thread                                       | recovery failed |     |     |
| ----------- | ------------------------------------------------ | --------------- | --- | --- |
| Category    | MACaddressmanagement                             |                 |     |     |
| Severity    | Error                                            |                 |     |     |
| Description | EventraisedwhenBCML2Xthreadisfailedtoberecovered |                 |     |     |
Event ID: 4809
Message MAC hash collision occurred for MAC {mac} on VLAN {vlan}
| Category    | MACaddressmanagement                      |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Error                                     |     |     |     |
| Description | LogswarningthatMAChitahashcollisioninSDK. |     |     |     |
MACaddressmanagementevents|195

Chapter 59
|             |                    | MAC Address | mode | configuration | events |
| ----------- | ------------------ | ----------- | ---- | ------------- | ------ |
| MAC Address | mode configuration | events      |      |               |        |
ThefollowingaretheeventsrelatedtoMACAddressmodeconfiguration.
| Event ID: 11001 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Message The MAC Address configured mode changed from <old_mode> to <new_mode>
| Category        | MACAddressmodeconfiguration                      |     |     |     |     |
| --------------- | ------------------------------------------------ | --- | --- | --- | --- |
| Severity        | Information                                      |     |     |     |     |
| Description     | LogeventwhentheMACAddressconfiguredmodeischanged |     |     |     |     |
| Event ID: 11002 |                                                  |     |     |     |     |
Message The MAC Address operational mode changed from <old_mode> to <new_
mode>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Information                 |     |     |     |     |
Description LogeventwhentheMACAddressoperationalmodeischanged
| Event ID: 11003 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Message Station MAC add failure due to hardware full, mac=<mac> vlan=<vlan>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Error                       |     |     |     |     |
Description LogeventwhenalocalstationMACaddresscannotbeaddedbecausethetableisfull
| Event ID: 11004 |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
Message The MAC Address operational mode changed from <old_mode> to <new_
mode> due to reaching SVI threshold. Current=<current> Max=<max>
| Category | MACAddressmodeconfiguration |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
| Severity | Error                       |     |     |     |     |
Description LogeventwhentheMACAddressoperationalmodeischangedduetooutofresources
| MAC Learning | events |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- |
196
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

The following are the events related to MAC learning.

Event ID: 4801

Message

MAC <mac> moved from port <from-intf> to port <to-intf> on VLAN
<vlan>

Category

MAC Learning

Severity

Information

Description

Event raised when L2 mac move

Event ID: 4802

Message

All dynamic MAC addresses on VLAN <vlan> were flushed

Category

MAC Learning

Severity

Information

Description

Event raised when L2 MAC table is flushed with vlan delete event or clear mac-address
command from vtysh

Event ID: 4803

Message

All dynamic MAC addresses on port <intf> were flushed

Category

MAC Learning

Severity

Information

Description

Event raised when L2 MAC table is flushed with port move to L3 event or clear mac-
address command from vtysh

Event ID: 4804

Message

All dynamic MAC addresses on port <intf> were flushed

Category

MAC Learning

Severity

Information

Description

Event raised when L2 MAC table is flushed with port down event or clear mac-address
command from vtysh

Event ID: 4805

Message

All dynamic MAC addresses on VLAN <vlan> were flushed

Category

MAC Learning

Severity

Information

MAC Learning events | 197

Description

Event raised when L2 MAC table is flushed with vlan down event or clear mac-address
command from vtysh

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

198

Chapter 60

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

199

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

The data traffic on interface <ifname> is no longer secured by
MACsec.

Category

MACsec

Severity

Information

Description

The data plane traffic on an interface is not secured by MACsec anymore.

Event ID: 11207

Message

Interface {ifname} MACsec selftest failed - {reason}.

Category

MACsec

Severity

Error

Description

MACsec selftest failed for the specified interface.

Event ID: 11208

Message

MACsec frame with an unknown SCI detected on MACsec entity running on
interface {ifname} with port ID {id}

Category

MACsec

Severity

Information

Description

Detected a MACsec frame with unknown SCI on an interface with the specified port ID.

Event ID: 11209

Message

Suspending data delay protection for Connectivity Association {ckn}
on interface {ifname} during ISSU.

Category

MACsec

Severity

Information

Description

Data delay protection is suspended for the specified CKN on interface during ISSU.

Event ID: 11210

MACsec events | 200

Message Resuming data delay protection for Connectivity Association {ckn} on
|          | interface   | {ifname} | post ISSU. |     |
| -------- | ----------- | -------- | ---------- | --- |
| Category | MACsec      |          |            |     |
| Severity | Information |          |            |     |
Description DatadelayprotectionisresumedforthegivenCKNpostISSU.
Event ID: 11211
| Message     | ISSU aborted         | by MACsec. | Reason - | {reason}. |
| ----------- | -------------------- | ---------- | -------- | --------- |
| Category    | MACsec               |            |          |           |
| Severity    | Information          |            |          |           |
| Description | ISSUabortedbyMACsec. |            |          |           |
Event ID: 11212
Message Interface {ifname} blocked by MACsec due to a misconfiguration.
|          | Reason | - {reason}. |     |     |
| -------- | ------ | ----------- | --- | --- |
| Category | MACsec |             |     |     |
| Severity | Error  |             |     |     |
Description MACsecdaemonblockedaninterfaceduetoaconfigurationerror.
Event ID: 11213
Message MACsec is disabled on port {name}. Additional licenses are needed to
|          | enable | the {feature} | functionality | on the port. |
| -------- | ------ | ------------- | ------------- | ------------ |
| Category | MACsec |               |               |              |
| Severity | Error  |               |               |              |
Description Theportwillremainblockedforbothingressandegresstraffictillavalidlicenseisnot
installed.
Event ID: 11214
Message MACsec is operational on port {name} without a valid license for
{feature}.
| Category    | MACsec                                   |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- |
| Severity    | Information                              |     |     |     |
| Description | MACsecisoperationalontheportinhonormode. |     |     |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 201

Chapter 61
Management events
| Management events |     |     |
| ----------------- | --- | --- |
Thefollowingaretheeventsrelatedtomanagement.
Event ID: 4301
| Message     | MGMT_INTF:                                     | <mgmt_intf_config_param> |
| ----------- | ---------------------------------------------- | ------------------------ |
| Category    | Management                                     |                          |
| Severity    | Information                                    |                          |
| Description | Logsrelatedtomanagementinterfaceconfigurations |                          |
Event ID: 4302
| Message  | MGMT_INTF: | <mgmt_intf_config_err> |
| -------- | ---------- | ---------------------- |
| Category | Management |                        |
| Severity | Error      |                        |
Description Logsrelatedtomanagementinterfaceconfigurationserror
Event ID: 4303
| Message  | MGMT_INTF: | <mgmt_intf_config_crit> |
| -------- | ---------- | ----------------------- |
| Category | Management |                         |
| Severity | Critical   |                         |
Description Logsrelatedtomanagementinterfacecriticalconfigurations
202
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 62

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

203

Chapter 63
MGMD events
| MGMD | events |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoMGMD.
| Event    | ID: 2601 (Severity: | Fatal) |                       |               |         |
| -------- | ------------------- | ------ | --------------------- | ------------- | ------- |
| Message  |                     | Failed | to alloc a <pkt_type> | pkt(interface | <vlan>) |
| Category |                     | MGMD   |                       |               |         |
| Severity |                     | Fatal  |                       |               |         |
Description ThislogeventinformspacketallocationfailedinMGMDsubsystem.
| Event | ID: 2602 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Received IGMPv1 query from <ip_address> when the device is configured
for IGMPv2.
| Category |     | MGMD        |     |     |     |
| -------- | --- | ----------- | --- | --- | --- |
| Severity |     | Information |     |     |     |
Description ThislogeventusedtologIGMPwarningwhenIGMPv1queryisreceived.
| Event | ID: 2603 (Severity: | Fatal) |     |     |     |
| ----- | ------------------- | ------ | --- | --- | --- |
Message Unable to alloc a buf of size <size_value> for <sub_system>
| Category |     | MGMD  |     |     |     |
| -------- | --- | ----- | --- | --- | --- |
| Severity |     | Fatal |     |     |     |
Description ThislogeventinformstheuserthatMGMDcouldnotallocatememory.
| Event | ID: 2604 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message Interface <if_name>: Other Querier detected for <mgmd_type>
| Category |     | MGMD        |     |     |     |
| -------- | --- | ----------- | --- | --- | --- |
| Severity |     | Information |     |     |     |
Description ThislogeventinformstheuserthatIGMP/MLDdetectedotherquerier.
| Event | ID: 2605 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
204
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message <mgmd_type> Querier Election in progress for interface <if_name> with
|          | IP address  | <ip_address> |     |     |
| -------- | ----------- | ------------ | --- | --- |
| Category | MGMD        |              |     |     |
| Severity | Information |              |     |     |
Description ThislogeventinformstheuserthatIGMP/MLDhasstartedquerierelectiononinterface.
Event ID: 2606
| Message  | Interface   | <if_name>: | End <mgmd_type> | Querier role |
| -------- | ----------- | ---------- | --------------- | ------------ |
| Category | MGMD        |            |                 |              |
| Severity | Information |            |                 |              |
Description ThislogeventinformstheuserthatIGMP/MLDendedquerierroleoninterface.
Event ID: 2607
Message Interface <if_name>: Start <mgmd_type> Querier role addr: <ip_
address>
| Category | MGMD        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatMGMDstartedquerierroleoninterface.
Event ID: 2608
Message Received packet from <ip_address>, type <type>, on invalid port
<port>
| Category | MGMD    |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description ThislogeventinformstheuserthatMGMDreceivedpacketoninvalidport.
Event ID: 2609
Message Received IGMPv1 query from <ip_address> when the device is configured
|          | for IGMPv3.' | throttle_count: | 1   |     |
| -------- | ------------ | --------------- | --- | --- |
| Category | MGMD         |                 |     |     |
| Severity | Information  |                 |     |     |
Description ThislogeventusedtologIGMPwarningwhenconfiguredmodeisIGMPv3andIGMPv1
queryisreceived.
Event ID: 2610
MGMDevents|205

Message Received IGMPv2 query from <ip_address> when the device is configured
|          | for IGMPv3.' | throttle_count: | 1   |     |
| -------- | ------------ | --------------- | --- | --- |
| Category | MGMD         |                 |     |     |
| Severity | Information  |                 |     |     |
Description ThislogeventusedtologIGMPwarningwhenconfiguredmodeisIGMPv3andIGMPv2
queryisreceived.
Event ID: 2611
| Message  | <mgmd_type> | snooping | is <status> | on VLAN <vlan> |
| -------- | ----------- | -------- | ----------- | -------------- |
| Category | MGMD        |          |             |                |
| Severity | Information |          |             |                |
Description ThislogeventinformstheuserthatIGMP/MLDstatusonVLAN.
Event ID: 2612
| Message  | <mgmd_type> | is <status> | on Interface | <if_name> |
| -------- | ----------- | ----------- | ------------ | --------- |
| Category | MGMD        |             |              |           |
| Severity | Information |             |              |           |
Description ThislogeventinformstheusertheIGMP/MLDstatusontheInterface.
Event ID: 2613
Message Port <port> on vlan <vlan> is set to <status> mode for <mgmd_type>.
| Category | MGMD        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Thislogeventinformstheuserthattheportmodehaschanged.
Event ID: 2614
Message <mgmd_type> is not operational on VLAN <vlan> due to resource
unavailability
| Category | MGMD  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description ThislogeventinformstheuserthattheIGMP/MLDisdisabledonaVLANduetointernal
errors.
Event ID: 2615
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 206

Message <mgmd_type> is not operational on interface <l3Port> due to resource
unavailability
| Category | MGMD  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description ThislogeventinformstheuserthattheIGMP/MLDisdisabledonaL3interfacedueto
internalerrors.
Event ID: 2616
Message IGMP/MLD Resource utilization has exceeded the supported limits on
the system. Membership reports for the new groups will be dropped.
| Category | MGMD        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatMGMDresourceutilizationhasexceededthe
supportedlimits
Event ID: 2617
Message IGMP/MLD Resource utilization has reached 90 percent of the supported
|          | limits on   | the system. |     |     |
| -------- | ----------- | ----------- | --- | --- |
| Category | MGMD        |             |     |     |
| Severity | Information |             |     |     |
Description ThislogeventinformstheuserthatMGMDresourceutilizationhasreached90percent
ofthesupportedlimits
Event ID: 2618
| Message  | <mgmd_type> | snooping | is <status> | on VLAN <vlan>. |
| -------- | ----------- | -------- | ----------- | --------------- |
| Category | MGMD        |          |             |                 |
| Severity | Information |          |             |                 |
Description ThislogeventinformstheuserthatwhetherIGMP/MLDsnoopingisoperational.
Event ID: 2619
Message Received IGMPv3 query from <ip_address> when the device is configured
|          | for IGMPv2.' | throttle_count: | 1   |     |
| -------- | ------------ | --------------- | --- | --- |
| Category | MGMD         |                 |     |     |
| Severity | Information  |                 |     |     |
Description ThislogeventusedtologIGMPwarningwhenIGMPv2queryisreceived.
MGMDevents|207

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

Event ID: 2623

Message

Remote IDL connection established.

Category

MGMD

Severity

Information

Description

This log event is used to indicate remote IDL connection is established

Event ID: 2624

Message

Querier functionality offloaded to VSX peer.

Category

MGMD

Severity

Information

Description

This log event is used to indicate that querier is offloaded.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

208

Event ID: 2625

Message

IGMPv2 packet received for group address {ip_address} in SSM range which is not part of

SSM map.

Category

MGMD

Severity

Information

Description

This log event is used to identify IGMPv2 packet in ssm-range but not in ssm-map.

Event ID: 2626

Message

MLDv1 packet received for group address {ip_address} in SSM range which is not part of

SSM map.

Category

MGMD

Severity

Information

Description

This log event is used to identify MLDv1 packet in ssm-range but not in ssm-map.

Event ID: 2627

Message

SSM-map {acl_name} applied to {protocol} interface {port_name}

Category

MGMD

Severity

Information

Description

This log event is used to identify that ssm-map ACL is applied to particular interface.

Event ID: 2628

Message

Category

Severity

Description

IGMP/MLD internal queue limit exceeded. Needs admin intervention.

MGMD

Alert

This log event is used to intimate the user that IGMP/MLD control packet queue is full.

MGMD events | 209

Chapter 64
Mirroring events
Mirroring events
Thefollowingaretheeventsrelatedtomirroring.
Event ID: 6701
| Message     | Failed                                           | to create mirror | session <number> |
| ----------- | ------------------------------------------------ | ---------------- | ---------------- |
| Category    | Mirroring                                        |                  |                  |
| Severity    | Error                                            |                  |                  |
| Description | Logsamessagewhenthecreationofamirrorsessionfails |                  |                  |
Event ID: 6702
| Message  | Mirror      | session <number> | created |
| -------- | ----------- | ---------------- | ------- |
| Category | Mirroring   |                  |         |
| Severity | Information |                  |         |
Description Logsamessagewhenthecreationofamirrorsessionsucceeds
Event ID: 6703
| Message     | Failed                                           | to delete mirror | session <number> |
| ----------- | ------------------------------------------------ | ---------------- | ---------------- |
| Category    | Mirroring                                        |                  |                  |
| Severity    | Error                                            |                  |                  |
| Description | Logsamessagewhenthedeletionofamirrorsessionfails |                  |                  |
Event ID: 6704
| Message  | Mirror      | session <number> | deleted |
| -------- | ----------- | ---------------- | ------- |
| Category | Mirroring   |                  |         |
| Severity | Information |                  |         |
Description Logsamessagewhenmirrorsessionissuccessfullydeleted
Event ID: 6705
210
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Failed                                        | to update mirror | session <number> |
| ----------- | --------------------------------------------- | ---------------- | ---------------- |
| Category    | Mirroring                                     |                  |                  |
| Severity    | Error                                         |                  |                  |
| Description | Logsamessagewhenanupdateofamirrorsessionfails |                  |                  |
Event ID: 6706
| Message  | Mirror      | session <number> | updated |
| -------- | ----------- | ---------------- | ------- |
| Category | Mirroring   |                  |         |
| Severity | Information |                  |         |
Description Logsamessagewhentheupdateofamirrorsessionsucceeds
Mirroringevents|211

Chapter 65
Module events
Module events
Thefollowingaretheeventsrelatedtomodule.
Event ID: 3201
| Message     | <type> module                                   | <name> | inserted': yes |     |
| ----------- | ----------------------------------------------- | ------ | -------------- | --- |
| Category    | Module                                          |        |                |     |
| Severity    | Information                                     |        |                |     |
| Description | Indicatesthatthemodulehasbeenphysicallyinserted |        |                |     |
Event ID: 3202
| Message     | <type> module                                  | <name> | removed': yes |     |
| ----------- | ---------------------------------------------- | ------ | ------------- | --- |
| Category    | Module                                         |        |               |     |
| Severity    | Warning                                        |        |               |     |
| Description | Indicatesthatthemodulehasbeenphysicallyremoved |        |               |     |
Event ID: 3203
| Message     | Initiating                            | <type> module | <name> reboot': | yes |
| ----------- | ------------------------------------- | ------------- | --------------- | --- |
| Category    | Module                                |               |                 |     |
| Severity    | Information                           |               |                 |     |
| Description | Indicatesthatthemoduleisabouttoreboot |               |                 |     |
Event ID: 3204
| Message     | <type> module                               | <name> | is ready |     |
| ----------- | ------------------------------------------- | ------ | -------- | --- |
| Category    | Module                                      |        |          |     |
| Severity    | Information                                 |        |          |     |
| Description | Indicatesthatthemoduleisinitializedandready |        |          |     |
Event ID: 3205
212
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | <type> module                | <name> | is down: <reason> |     |
| ----------- | ---------------------------- | ------ | ----------------- | --- |
| Category    | Module                       |        |                   |     |
| Severity    | Information                  |        |                   |     |
| Description | Indicatesthatthemoduleisdown |        |                   |     |
Event ID: 3206
| Message     | <type> module                           | <name> | is in diagnostics | mode |
| ----------- | --------------------------------------- | ------ | ----------------- | ---- |
| Category    | Module                                  |        |                   |      |
| Severity    | Information                             |        |                   |      |
| Description | Indicatesthatamoduleisindiagnosticsmode |        |                   |      |
Event ID: 3207
| Message     | <type> module                 | <name> | has failed: <reason>': | yes |
| ----------- | ----------------------------- | ------ | ---------------------- | --- |
| Category    | Module                        |        |                        |     |
| Severity    | Error                         |        |                        |     |
| Description | Indicatesthatamodulehasfailed |        |                        |     |
Event ID: 3208
| Message     | <type> module                                      | <name> | admin state set | to up |
| ----------- | -------------------------------------------------- | ------ | --------------- | ----- |
| Category    | Module                                             |        |                 |       |
| Severity    | Information                                        |        |                 |       |
| Description | Indicatesthatthemoduleadministrativestateissettoup |        |                 |       |
Event ID: 3209
| Message  | <type> module | <name> | admin state set | to down |
| -------- | ------------- | ------ | --------------- | ------- |
| Category | Module        |        |                 |         |
| Severity | Information   |        |                 |         |
Description Indicatesthatthemoduleadministrativestateissettodown
Event ID: 3210
| Message | <type> module | <name> | admin state set | to diagnostics |
| ------- | ------------- | ------ | --------------- | -------------- |
Moduleevents|213

| Category | Module      |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Indicatesthatthemoduleadministrativestateissettodiagnostics
Event ID: 3211
| Message     | <type> module                         | <name> ISP | passed |     |
| ----------- | ------------------------------------- | ---------- | ------ | --- |
| Category    | Module                                |            |        |     |
| Severity    | Information                           |            |        |     |
| Description | IndicatesthatISPhaspassedforthemodule |            |        |     |
Event ID: 3212
| Message     | <type> module                         | <name> ISP | failed': yes |     |
| ----------- | ------------------------------------- | ---------- | ------------ | --- |
| Category    | Module                                |            |              |     |
| Severity    | Error                                 |            |              |     |
| Description | IndicatesthatISPhasfailedforthemodule |            |              |     |
Event ID: 3213
| Message     | <type> module                              | <name> ISP | skipped |     |
| ----------- | ------------------------------------------ | ---------- | ------- | --- |
| Category    | Module                                     |            |         |     |
| Severity    | Warning                                    |            |         |     |
| Description | IndicatesthatISPhasbeenskippedforthemodule |            |         |     |
Event ID: 3214
| Message     | <type> module                                    | <name> has | enabled standby | power |
| ----------- | ------------------------------------------------ | ---------- | --------------- | ----- |
| Category    | Module                                           |            |                 |       |
| Severity    | Information                                      |            |                 |       |
| Description | Indicatesthatthemoduleisinstandby(low-power)mode |            |                 |       |
Event ID: 3215
Message <type> module <name> is requesting to power on with priority
<priority>
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 214

| Category    | Module                                      |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |
| Description | Indicatesthatthemoduleisrequestingtopoweron |     |     |     |
Event ID: 3216
| Message  | <type> module | <name> power | request has | been granted |
| -------- | ------------- | ------------ | ----------- | ------------ |
| Category | Module        |              |             |              |
| Severity | Information   |              |             |              |
Description Indicatesthatthepowerrequestforthemodulehasbeengranted
Event ID: 3217
| Message  | <type> module | <name> power | request has | been denied |
| -------- | ------------- | ------------ | ----------- | ----------- |
| Category | Module        |              |             |             |
| Severity | Warning       |              |             |             |
Description Indicatesthatthepowerrequestforthemodulehasbeendenied
Event ID: 3218
| Message     | <type> module                                    | <name> enabling | main power |     |
| ----------- | ------------------------------------------------ | --------------- | ---------- | --- |
| Category    | Module                                           |                 |            |     |
| Severity    | Information                                      |                 |            |     |
| Description | Indicatesthatmainpowerforthemoduleisbeingenabled |                 |            |     |
Event ID: 3219
| Message     | <type> module                                    | <name> main | power enabled |     |
| ----------- | ------------------------------------------------ | ----------- | ------------- | --- |
| Category    | Module                                           |             |               |     |
| Severity    | Information                                      |             |               |     |
| Description | Indicatesthatmainpowerforthemodulehasbeenenabled |             |               |     |
Event ID: 3220
| Message  | <type> module | <name> main | power failed': | yes |
| -------- | ------------- | ----------- | -------------- | --- |
| Category | Module        |             |                |     |
Moduleevents|215

| Severity    | Error                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Description | Indicatesthatmainpowerforthemodulehasfailed |     |     |     |
Event ID: 3221
| Message  | <type> module | <name> device | initialization | started |
| -------- | ------------- | ------------- | -------------- | ------- |
| Category | Module        |               |                |         |
| Severity | Information   |               |                |         |
Description Indicatesthatdeviceinitializationforthemodulehasstarted
Event ID: 3222
| Message  | <type> module | <name> device | initialization | passed |
| -------- | ------------- | ------------- | -------------- | ------ |
| Category | Module        |               |                |        |
| Severity | Information   |               |                |        |
Description Indicatesthatdeviceinitializationforthemodulehaspassed
Event ID: 3223
Message <type> module <name> device initialization failed: <reason>': yes
| Category | Module |     |     |     |
| -------- | ------ | --- | --- | --- |
| Severity | Error  |     |     |     |
Description Indicatesthatdeviceinitializationforthemodulehasfailed
Event ID: 3224
| Message     | <type> module                                     | <name> ASIC | initialization | started |
| ----------- | ------------------------------------------------- | ----------- | -------------- | ------- |
| Category    | Module                                            |             |                |         |
| Severity    | Information                                       |             |                |         |
| Description | IndicatesthatanASICforthemoduleisbeinginitialized |             |                |         |
Event ID: 3225
| Message  | <type> module | <name> ASIC | initialization | completed |
| -------- | ------------- | ----------- | -------------- | --------- |
| Category | Module        |             |                |           |
| Severity | Information   |             |                |           |
Description IndicatesthatASICinitializationforthemodulehascompleted
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 216

Event ID: 3226
Message <type> module <name> ASIC initialization failed: <reason>': yes
| Category    | Module                                               |     |     |     |
| ----------- | ---------------------------------------------------- | --- | --- | --- |
| Severity    | Error                                                |     |     |     |
| Description | IndicatesthatASICinitializationforthemodulehasfailed |     |     |     |
Event ID: 3227
| Message  | <type>      | module <name> ASIC | deinitialization | started |
| -------- | ----------- | ------------------ | ---------------- | ------- |
| Category | Module      |                    |                  |         |
| Severity | Information |                    |                  |         |
Description IndicatesthatanASICforthemoduleisbeingdeinitialized
Event ID: 3228
| Message  | <type>      | module <name> ASIC | deinitialization | completed |
| -------- | ----------- | ------------------ | ---------------- | --------- |
| Category | Module      |                    |                  |           |
| Severity | Information |                    |                  |           |
Description IndicatesthatASICdeinitializationforthemodulehascompleted
Event ID: 3229
Message <type> module <name> ASIC denitialization failed: <reason>': yes
| Category | Module |     |     |     |
| -------- | ------ | --- | --- | --- |
| Severity | Error  |     |     |     |
Description IndicatesthatASICdeinitializationforthemodulehasfailed
Event ID: 3230
| Message     | <name>                                          | is starting zeroization': | yes |     |
| ----------- | ----------------------------------------------- | ------------------------- | --- | --- |
| Category    | Module                                          |                           |     |     |
| Severity    | Information                                     |                           |     |     |
| Description | Indicatesthatthemoduleisabouttostartzeroization |                           |     |     |
Event ID: 3231
Moduleevents|217

| Message     | <name> zeroization                            | completed. |     |     |
| ----------- | --------------------------------------------- | ---------- | --- | --- |
| Category    | Module                                        |            |     |     |
| Severity    | Information                                   |            |     |     |
| Description | Indicatesthatthemodulezeroizationhascompleted |            |     |     |
Event ID: 3232
| Message     | <name> zeroization                                | failed.': |     | yes |
| ----------- | ------------------------------------------------- | --------- | --- | --- |
| Category    | Module                                            |           |     |     |
| Severity    | Error                                             |           |     |     |
| Description | Indicatesthatthemodulezeroizationfailedtocomplete |           |     |     |
Event ID: 3233
Message <type> module <name> configured with product number <part_number>
| Category    | Module                                  |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Indicatesthatthemodulehasbeenconfigured |     |     |     |
Event ID: 3234
| Message     | <type> module                             | <name> has | been | unconfigured |
| ----------- | ----------------------------------------- | ---------- | ---- | ------------ |
| Category    | Module                                    |            |      |              |
| Severity    | Information                               |            |      |              |
| Description | Indicatesthatthemodulehasbeenunconfigured |            |      |              |
Event ID: 3235
| Message     | <type> module                            | <name> initiating |     | failover |
| ----------- | ---------------------------------------- | ----------------- | --- | -------- |
| Category    | Module                                   |                   |     |          |
| Severity    | Information                              |                   |     |          |
| Description | Indicatesthatthemodulehasstartedfailover |                   |     |          |
Event ID: 3236
| Message | <type> module | <name> failover |     | completed |
| ------- | ------------- | --------------- | --- | --------- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 218

| Category    | Module                                     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Information                                |     |     |     |
| Description | Indicatesthatthemodulehascompletedfailover |     |     |     |
Event ID: 3237
| Message     | <type> module                          | <name> initiating | ISP |     |
| ----------- | -------------------------------------- | ----------------- | --- | --- |
| Category    | Module                                 |                   |     |     |
| Severity    | Information                            |                   |     |     |
| Description | IndicatesthatISPhasstartedforthemodule |                   |     |     |
Event ID: 3238
| Message     | <type> module                             | <name> enabling | front-end | power |
| ----------- | ----------------------------------------- | --------------- | --------- | ----- |
| Category    | Module                                    |                 |           |       |
| Severity    | Information                               |                 |           |       |
| Description | Indicatesthatfront-endpowerisbeingenabled |                 |           |       |
Event ID: 3239
Message <type> module <name> disabling front-end power: <reason>
| Category    | Module                                     |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Warning                                    |     |     |     |
| Description | Indicatesthatfront-endpowerisbeingdisabled |     |     |     |
Event ID: 3240
| Message     | <type> module                                   | <name> has | persistent | hardware error |
| ----------- | ----------------------------------------------- | ---------- | ---------- | -------------- |
| Category    | Module                                          |            |            |                |
| Severity    | Error                                           |            |            |                |
| Description | Indicatesthatpersistenthardwareerrorhasoccurred |            |            |                |
Event ID: 3241
Message
{name}isstartingzeroizationandsettingenhancedsecuremode
| Category | Module |     |     |     |
| -------- | ------ | --- | --- | --- |
Moduleevents|219

Severity

Information

Description

Indicates that the module is about to start zeroization and setting enhanced secure mode

Event ID: 3242

Message

{name} zeroization completed and enhanced secure mode set.

Category

Module

Severity

Information

Description

Indicates that the module zeroization has completed and enhanced secure mode s

Event ID: 3240

Message

Category

Severity

{name} zeroization failed.

Module

Error

Description

Indicates that the module zeroization failed to complete

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

220

Chapter 66

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

Event ID: 13303

Message

MPLS Graceful Restart process started

Category

MPLS

Severity

Information

Description

Logs the start of MPLS Graceful Restart.

Event ID: 13304

Message

Category

Severity

MPLS Graceful Restart process is complete

MPLS

Error

Description

Logs the end of MPLS Graceful Restart.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

221

Chapter 67
MSDP events
MSDP events
ThefollowingaretheeventsrelatedtoMSDP.
Event ID: 8601
| Message     | Router MSDP                   | is <status> | on VRF <vrf_name> |     |
| ----------- | ----------------------------- | ----------- | ----------------- | --- |
| Category    | MSDP                          |             |                   |     |
| Severity    | Information                   |             |                   |     |
| Description | Routermsdpconfigurationstatus |             |                   |     |
Event ID: 8602
Message Forwarding state of interface <if_name> has been changed to <state>
| Category    | MSDP                                 |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | MSDPSourceInterfaceoperationalstatus |     |     |     |
Event ID: 8603
Message MSDP Peer <peer_ip>(<tcp_entity>) with connection source <if_name>
|             | has entered                              | <state> state |     |     |
| ----------- | ---------------------------------------- | ------------- | --- | --- |
| Category    | MSDP                                     |               |     |     |
| Severity    | Information                              |               |     |     |
| Description | LogsthechangesinMSDPPeerconnectionstate. |               |     |     |
Event ID: 8604
| Message     | Port <port>                               | is <status> | to MSDP Peer | <peer_ip> |
| ----------- | ----------------------------------------- | ----------- | ------------ | --------- |
| Category    | MSDP                                      |             |              |           |
| Severity    | Information                               |             |              |           |
| Description | Logeventwhenportisaddedordeletedforapeer. |             |              |           |
Event ID: 8606
222
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message MSDP Peer <peer_ip> is <status> on VRF <vrf_name>. Interface <if_
|                | name>                                 | is added to  | the Peer |          |           |           |
| -------------- | ------------------------------------- | ------------ | -------- | -------- | --------- | --------- |
| Category       | MSDP                                  |              |          |          |           |           |
| Severity       | Information                           |              |          |          |           |           |
| Description    | Logeventwhenpeerisenabledordisabled   |              |          |          |           |           |
| Event ID: 8607 |                                       |              |          |          |           |           |
| Message        | Start                                 | <tcp_entity> | role     | for MSDP | peer      | <peer_ip> |
| Category       | MSDP                                  |              |          |          |           |           |
| Severity       | Information                           |              |          |          |           |           |
| Description    | Logeventwhenclientorserveriselected   |              |          |          |           |           |
| Event ID: 8608 |                                       |              |          |          |           |           |
| Message        | Finish                                | packet was   | received | on       | MSDP Peer | <peer_ip> |
| Category       | MSDP                                  |              |          |          |           |           |
| Severity       | Information                           |              |          |          |           |           |
| Description    | LogeventwhenTCPfinalpacketisreceived. |              |          |          |           |           |
| Event ID: 8609 |                                       |              |          |          |           |           |
Message Failed to add SA Cache entry: S=<src_ip>, G=<grp_ip>, R=<rp_ip> for
|             | Peer <peer_ip>                         | as    | MSDP     | SA Cache | Limit  | is reached |
| ----------- | -------------------------------------- | ----- | -------- | -------- | ------ | ---------- |
| Category    | MSDP                                   |       |          |          |        |            |
| Severity    | Warning                                |       |          |          |        |            |
| Description | LogeventwhenMSDPSAcachelimitisreached. |       |          |          |        |            |
| Message     | Session                                | Relay | Protocol |          | events |            |
ThefollowingaretheeventsrelatedtoMessageSessionRelayProtocol(MSRP).
| Event ID: 15501 |                                         |     |     |     |     |     |
| --------------- | --------------------------------------- | --- | --- | --- | --- | --- |
| Message         | MSRPstream{streamid}createdonport{name} |     |     |     |     |     |
| Category        | MessageSessionRelayProtocol             |     |     |     |     |     |
| Severity        | Information                             |     |     |     |     |     |
Description
EventreportedwhenMSRPstreamiscreated
MessageSessionRelayProtocol events|223

Event ID: 15502

Message

MSRP stream {streamid} deleted

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when MSRP stream is deleted

Event ID: 15503

Message

MSRP is active on port {port}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when MSRP becomes active on port

Event ID: 15504

Message

MSRP is inactive on port {port}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when MSRP becomes inactive on port

Event ID: 15505

Message

MSRP Stream {streamid} Talker has left

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when MSRP Talker leave

Event ID: 15506

Message

MSRP Stream {streamid} Listener connected on port {name} has left

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when MSRP Listener leave

Event ID: 15507

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

224

Message

Resource allocation status for stream {streamid} on port {name} is {status}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when resource allocation status is updated for an MSRP stream

Event ID: 15508

Message

Resource de-allocated for stream {streamid} on port {name}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when resource de allocated for an MSRP stream

Event ID: 15509

Message

Resource allocation requested for stream {streamid} on port {name}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when resource allocation requested for an MSRP stream

Event ID: 15510

Message

Resource de-allocation requested for stream {streamid} on port {name} due to {reason}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when resource de alloc requested for an MSRP stream

Event ID: 15511

Message

MSRP Listener added with declaration-type {decl_type} for stream {streamid} on port

{name}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when listener gets added for an MSRP stream

Event ID: 15512

Message Session Relay Protocol events | 225

Message

MSRP Listener declaration-type changed to {decl_type} for stream {streamid} on port

{name}

Category

Message Session Relay Protocol

Severity

Information

Description

Event reported when listener declaration-type changes for an MSRP stream

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

226

Chapter 68
|           |                 |        | Multicast | Traffic | Manager | events |
| --------- | --------------- | ------ | --------- | ------- | ------- | ------ |
| Multicast | Traffic Manager | events |           |         |         |        |
ThefollowingaretheeventsrelatedtoMulticastTrafficManager.
| Event ID: | 4001 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message The Multicast L3 Bridge Control Forwarding entries limit was reached:
|     | <limit>' | throttle_count: | 100 |     |     |     |
| --- | -------- | --------------- | --- | --- | --- | --- |
Category MulticastTrafficManager
Severity Warning
Description EventraisedwhenthemaximumnumberofmulticastL3BridgeControlForwarding
entriesisreached
| Event ID: | 4002 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message {mgmd_type} snooping filter unknown mcast feature will be {status}.
Category MulticastTrafficManager
Severity Info
Description Loggedwhenmgmdsnoopingfilterunknownmcastfeatureenablementorremoval
statusinMTM
| Event ID: | 4003 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Failed to {status} {mgmd_type} snooping filter unknown mcast feature.
Category MulticastTrafficManager
Severity Error
Description Loggedwhenerroroccurswhileupdatingmgmdsnoopingfilterunknownmcastentry
intocpurxtable.
227
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

|         |         |                |         |        |          | Chapter | 69     |
| ------- | ------- | -------------- | ------- | ------ | -------- | ------- | ------ |
|         |         | Message        | Session | Relay  | Protocol | (MSRP)  | events |
| Message | Session | Relay Protocol | (MSRP)  | events |          |         |        |
ThefollowingaretheeventsrelatedtoMessageSessionRelayProtocol(MSRP).
| Event ID: | 2001 |                              |     |     |     |     |     |
| --------- | ---- | ---------------------------- | --- | --- | --- | --- | --- |
| Message   |      | MSTP Enabled                 |     |     |     |     |     |
| Category  |      | Multiplespanningtreeprotocol |     |     |     |     |     |
| Severity  |      | Information                  |     |     |     |     |     |
Description ThiscommandenablestheMSTP(MultipleSpanning-treeProtocol)featureinthedevice.
| Event ID: | 2002 |                              |     |     |     |     |     |
| --------- | ---- | ---------------------------- | --- | --- | --- | --- | --- |
| Message   |      | MSTP Disabled                |     |     |     |     |     |
| Category  |      | Multiplespanningtreeprotocol |     |     |     |     |     |
| Severity  |      | Information                  |     |     |     |     |     |
Description ThiscommanddisablestheMSTP(MultipleSpanning-treeProtocol)featureinthedevice.
| Event ID: | 2003 |                              |        |            |     |     |     |
| --------- | ---- | ---------------------------- | ------ | ---------- | --- | --- | --- |
| Message   |      | <config_parameter>           | should | be <value> |     |     |     |
| Category  |      | Multiplespanningtreeprotocol |        |            |     |     |     |
| Severity  |      | Warning                      |        |            |     |     |     |
Description ThislogeventinformstheuserthattheMSTPconfigparameterisbad
| Event ID: | 2004 |                              |     |           |         |     |     |
| --------- | ---- | ---------------------------- | --- | --------- | ------- | --- | --- |
| Message   |      | BPDU has <config_parameter>  |     | from port | <value> |     |     |
| Category  |      | Multiplespanningtreeprotocol |     |           |         |     |     |
| Severity  |      | Warning                      |     |           |         |     |     |
Description ThislogeventinformstheuserthattheSwitchreceivedaBPDUwithabadconfig
| Event ID: | 2005 |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- |
228
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | Bad reconfiguration          | request: <reconfig_parameter> |
| -------- | ---------------------------- | ----------------------------- |
| Category | Multiplespanningtreeprotocol |                               |
| Severity | Warning                      |                               |
Description ThislogeventinformstheuserthattheMSTPreconfigparameterisbad
Event ID: 2006
Message <proto> - Root changed from <old_priority>: <old_mac> to <new_
priority>: <new_mac>
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Information                  |     |
Description ThislogeventinformstheuserthattheMSTProothaschanged
Event ID: 2007
Message Port <port> disabled - BPDU received on protected port
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Warning                      |     |
Description ThislogeventinformstheuserthatBPDUwasreceivedonprotectedport
Event ID: 2008
Message <proto> starved for <pkt_type> on port <port> from <priority_mac>
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Information                  |     |
Description ThislogeventinformstheuserthattheRxqueueisstarvedinthepaticularport
Event ID: 2009
Message BPDU loss- port <port> moved to inconsistent state for <proto>
| Category | Multiplespanningtreeprotocol |     |
| -------- | ---------------------------- | --- |
| Severity | Information                  |     |
Description Thislogeventinformstheuserthattheportisininconsistentstate
Event ID: 2010
MessageSessionRelayProtocol(MSRP) events|229

Message Port <port> moved out of inconsistent state for <proto>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description ThislogeventinformstheuserthattheMSTPisoutofinconsistentstate
Event ID: 2011
Message Topology Change received on port <port> for <proto> from source:
<mac>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description ThislogeventinformstheuserthattheMSTPtopologychangeisreceived
Event ID: 2012
Message <proto> - Topology Change generated on port <port> going in to
<state>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description ThislogeventinformstheuserthattheMSTPtopologychangeisgenerated
Event ID: 2013
| Message  | BPDU received                | on admin | edge port <port> |
| -------- | ---------------------------- | -------- | ---------------- |
| Category | Multiplespanningtreeprotocol |          |                  |
| Severity | Information                  |          |                  |
Description ThislogeventinformstheuserthataBPDUwasreceivedonadminedgeport
Event ID: 2014
| Message  | Port <port>                  | blocked | on CIST |
| -------- | ---------------------------- | ------- | ------- |
| Category | Multiplespanningtreeprotocol |         |         |
| Severity | Information                  |         |         |
Description ThislogeventinformstheuserthattheCISTportisblocked
Event ID: 2015
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 230

| Message  | Port <port>                  | unblocked | on CIST |
| -------- | ---------------------------- | --------- | ------- |
| Category | Multiplespanningtreeprotocol |           |         |
| Severity | Information                  |           |         |
Description ThislogeventinformstheuserthattheCISTportisunblocked
Event ID: 2016
| Message  | Port <port>                  | blocked | on MST<instance> |
| -------- | ---------------------------- | ------- | ---------------- |
| Category | Multiplespanningtreeprotocol |         |                  |
| Severity | Information                  |         |                  |
Description ThislogeventinformstheuserthattheMSTIportisblocked
Event ID: 2017
| Message  | Port <port>                  | unblocked | on MST<instance> |
| -------- | ---------------------------- | --------- | ---------------- |
| Category | Multiplespanningtreeprotocol |           |                  |
| Severity | Information                  |           |                  |
Description ThislogeventinformstheuserthattheMSTIportisunblocked
Event ID: 2018
Message <proto> Root Port changed from <old_port> to <new_port>
| Category | Multiplespanningtreeprotocol |     |     |
| -------- | ---------------------------- | --- | --- |
| Severity | Information                  |     |     |
Description Thislogeventinformstheuserthattherootportischanged
Event ID: 2019
Message spanning tree mode changed from <old_mode> to <new_mode>, it will
|          | trigger the                  | reconvergence |     |
| -------- | ---------------------------- | ------------- | --- |
| Category | Multiplespanningtreeprotocol |               |     |
| Severity | Information                  |               |     |
Description Thislogeventinformstheuserthatthespanningtreemodeischanged.
MessageSessionRelayProtocol(MSRP) events|231

Chapter 70
MVRP events
MVRP events
ThefollowingaretheeventsrelatedtoMVRP.
Event ID: 3101
| Message  | MVRP enabled | on port <port> |     |     |
| -------- | ------------ | -------------- | --- | --- |
| Category | MVRP         |                |     |     |
| Severity | Information  |                |     |     |
Description ThiscommandenablestheMVRP(MultipleVLANRegistrationProtocol)featureon
interface.
Event ID: 3102
| Message  | MVRP disabled | on port <port> |     |     |
| -------- | ------------- | -------------- | --- | --- |
| Category | MVRP          |                |     |     |
| Severity | Information   |                |     |     |
Description ThiscommanddisablestheMVRP(MultipleVLANRegistrationProtocol)featureon
interface.
Event ID: 3103
Message MVRP failed to create VLAN <vlan>. Maximum VLANs <max_vlan> already
|             | created' throttle_count:                          |     | 100 |     |
| ----------- | ------------------------------------------------- | --- | --- | --- |
| Category    | MVRP                                              |     |     |     |
| Severity    | Information                                       |     |     |     |
| Description | Thislogeventinformsuserthatthevlancreateisfailed. |     |     |     |
Event ID: 3104
| Message  | MVRP statistics | have been | cleared for | port <port> |
| -------- | --------------- | --------- | ----------- | ----------- |
| Category | MVRP            |           |             |             |
| Severity | Information     |           |             |             |
Description Thislogeventinformsuserthatthemvrpstatisticshavebeencleared.
Event ID: 3105
232
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

MVRP statistics have been cleared for <port> ports

Category

MVRP

Severity

Information

Description

This log event informs user that the mvrp statistics have been cleared.

MVRP events | 233

Chapter 71

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

234

Chapter 72

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

235

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

Event ID: 6008

Message

NAE experiencing a spike in data points to process for NAE monitor
<monitorName>. NAE will temporarily stop monitoring new data points
for <monitorName>.

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

NAE events | 236

Message

User <user> has cleard NAE time series database

Category

NAE

Severity

Information

Description

Logs a message when a user clears the NAE time series database

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

237

Chapter 73
|            |            |        | NAE script | generation | events |
| ---------- | ---------- | ------ | ---------- | ---------- | ------ |
| NAE script | generation | events |            |            |        |
ThefollowingaretheeventsrelatedtoNAEscriptgeneration.
| Event ID:   | 12701                  |                        |                |          |     |
| ----------- | ---------------------- | ---------------------- | -------------- | -------- | --- |
| Message     | NAE                    | agent <agent> creation | failed. Reason | <reason> |     |
| Category    | NAEscriptgeneration    |                        |                |          |     |
| Severity    | Error                  |                        |                |          |     |
| Description | NAEagentcreationfailed |                        |                |          |     |
238
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 74
NAE Scripts events
| NAE Scripts events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoNetworkAnalyticsEnginescripts.
Event ID: 5501
| Message     | NAE script                 | <name> has | been validated. |     |
| ----------- | -------------------------- | ---------- | --------------- | --- |
| Category    | NAEScripts                 |            |                 |     |
| Severity    | Information                |            |                 |     |
| Description | NAEscripthasbeenvalidated. |            |                 |     |
Event ID: 5502
| Message     | Error found            | in NAE | Script <name>. |     |
| ----------- | ---------------------- | ------ | -------------- | --- |
| Category    | NAEScripts             |        |                |     |
| Severity    | Error                  |        |                |     |
| Description | ErrorfoundinNAEScript. |        |                |     |
Event ID: 5503
| Message     | Error found           | in NAE | Agent <name>. |     |
| ----------- | --------------------- | ------ | ------------- | --- |
| Category    | NAEScripts            |        |               |     |
| Severity    | Error                 |        |               |     |
| Description | ErrorfoundinNAEAgent. |        |               |     |
Event ID: 5504
Message Error executing NAE action <action_type> belonging to condition
|             | <condition>     | and agent | <agent> due | to <description>. |
| ----------- | --------------- | --------- | ----------- | ----------------- |
| Category    | NAEScripts      |           |             |                   |
| Severity    | Error           |           |             |                   |
| Description | NAEActionerror. |           |             |                   |
Event ID: 5505
239
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | NAE Script                          | <name> | has been created | by the system. |
| ----------- | ----------------------------------- | ------ | ---------------- | -------------- |
| Category    | NAEScripts                          |        |                  |                |
| Severity    | Information                         |        |                  |                |
| Description | NAEScripthasbeencreatedbythesystem. |        |                  |                |
Event ID: 5506
| Message     | NAE Agent                          | <name> has | been created | by the system. |
| ----------- | ---------------------------------- | ---------- | ------------ | -------------- |
| Category    | NAEScripts                         |            |              |                |
| Severity    | Information                        |            |              |                |
| Description | NAEAgenthasbeencreatedbythesystem. |            |              |                |
Event ID: 5507
| Message     | <msg>                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | NAEScripts                                  |     |     |     |
| Severity    | Information                                 |     |     |     |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |     |     |     |
Event ID: 5508
| Message     | <msg>                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | NAEScripts                                  |     |     |     |
| Severity    | Information                                 |     |     |     |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |     |     |     |
Event ID: 5509
| Message     | <msg>                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | NAEScripts                                  |     |     |     |
| Severity    | Critical                                    |     |     |     |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |     |     |     |
Event ID: 5510
| Message | <msg> |     |     |     |
| ------- | ----- | --- | --- | --- |
NAEScriptsevents|240

| Category    | NAEScripts                                  |            |
| ----------- | ------------------------------------------- | ---------- |
| Severity    | Error                                       |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5511                                    |            |
| Message     | <msg>                                       |            |
| Category    | NAEScripts                                  |            |
| Severity    | Warning                                     |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5512 (Severity:                         | Emergency) |
| Message     | <msg>                                       |            |
| Category    | NAEScripts                                  |            |
| Severity    | Emergency                                   |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5513 (Severity:                         | Emergency) |
| Message     | <msg>                                       |            |
| Category    | NAEScripts                                  |            |
| Severity    | Emergency                                   |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
| Event       | ID: 5514                                    |            |
| Message     | <msg>                                       |            |
| Category    | NAEScripts                                  |            |
| Severity    | Debug                                       |            |
| Description | LogeventwheninstantiatedfromactiveNAEagent. |            |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 241

Chapter 75
ND snooping events
| ND snooping events |     |     |     |
| ------------------ | --- | --- | --- |
ThefollowingaretheeventsrelatedtoNDsnooping.
Event ID: 8401
| Message     | All the dynamic                                 | binding entries | were cleared. |
| ----------- | ----------------------------------------------- | --------------- | ------------- |
| Category    | NDsnooping                                      |                 |               |
| Severity    | Information                                     |                 |               |
| Description | Logeventwhenalldynamicbindingentriesarecleared. |                 |               |
Event ID: 8402
Message Dynamic binding entries on the port <port> were cleared.
| Category | NDsnooping  |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhenalldynamicbindingentriesonaportarecleared.
Event ID: 8403
Message Dynamic binding entries on the VLAN <vid> were cleared.
| Category | NDsnooping  |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhenalldynamicbindingentriesonavlanarecleared.
Event ID: 8404
Message Dynamic binding entry with ip <ip> on the VLAN <vid> was cleared.
| Category | NDsnooping  |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logeventwhenaspecificdynamicbindingentryonavlaniscleared.
Event ID: 8405
242
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

ND packet of type=<type> received on port:<port> vlan:<vlan> with
src_mac:<src_mac> is <status>. count=<count>

Category

ND snooping

Severity

Information

Description

Log event when ND packet received on port.

ND snooping events | 243

Chapter 76
NDM events
NDM events
ThefollowingaretheeventsrelatedtoNDM.
Event ID: 6101
Message Static Neighbor <ip> created on Port <port>, VRF <vrf> mac <mac>
| Category    | NDM                   |     |     |     |
| ----------- | --------------------- | --- | --- | --- |
| Severity    | Information           |     |     |     |
| Description | Staticneighborcreated |     |     |     |
Event ID: 6102
Message Static Neighbor <ip> deleted on Port <port>, VRF <vrf> and mac <mac>
| Category    | NDM                   |     |     |     |
| ----------- | --------------------- | --- | --- | --- |
| Severity    | Information           |     |     |     |
| Description | Staticneighbordeleted |     |     |     |
Event ID: 6103
Message Static Neighbor <ip> modified on Port <port> and VRF <vrf> from mac
|             | <old_mac>              | to new mac | <new_mac> |     |
| ----------- | ---------------------- | ---------- | --------- | --- |
| Category    | NDM                    |            |           |     |
| Severity    | Information            |            |           |     |
| Description | Staticneighbormodified |            |           |     |
Event ID: 6104
| Message     | IPDB neighbor                       | <ip> | added in port <port>, | VRF <vrf> |
| ----------- | ----------------------------------- | ---- | --------------------- | --------- |
| Category    | NDM                                 |      |                       |           |
| Severity    | Information                         |      |                       |           |
| Description | IPDBneighboraddedtotheneighborTable |      |                       |           |
Event ID: 6105
244
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | IPDB Neighbor                           | <ip> | Deleted |     |
| ----------- | --------------------------------------- | ---- | ------- | --- |
| Category    | NDM                                     |      |         |     |
| Severity    | Information                             |      |         |     |
| Description | IPDBneighbordeletedfromtheneighborTable |      |         |     |
Event ID: 6106
Message Clear all Arp entries requested on Port <port> and VRF <vrf>
| Category    | NDM                                       |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Information                               |     |     |     |
| Description | ClearallarpentriesrequestedonSpecificPort |     |     |     |
Event ID: 6107
Message Clear all VSX Peer ARP entries requested on Port <port> and vrf <vrf>
| Category    | NDM                                              |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | Information                                      |     |     |     |
| Description | ClearallVSXPeerARPentriesrequestedonSpecificPort |     |     |     |
Event ID: 6108
| Message     | Clear all                                | Arp entries | requested | on VRF <vrf> |
| ----------- | ---------------------------------------- | ----------- | --------- | ------------ |
| Category    | NDM                                      |             |           |              |
| Severity    | Information                              |             |           |              |
| Description | ClearallarpentriesrequestedonSpecificVRF |             |           |              |
Event ID: 6109
Message Clear all VSX Peer Arp entries requested on VRF <vrf>
| Category    | NDM                                             |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |
| Description | ClearallVSXPeerarpentriesrequestedonSpecificVRF |     |     |     |
Event ID: 6110
| Message | Clear all | Arp entries | requested |     |
| ------- | --------- | ----------- | --------- | --- |
NDMevents|245

| Category    | NDM                         |     |     |
| ----------- | --------------------------- | --- | --- |
| Severity    | Information                 |     |     |
| Description | Clearallarpentriesrequested |     |     |
Event ID: 6111
| Message     | Clear all                          | VSX Peer Arp | entries requested |
| ----------- | ---------------------------------- | ------------ | ----------------- |
| Category    | NDM                                |              |                   |
| Severity    | Information                        |              |                   |
| Description | ClearallVSXPeerarpentriesrequested |              |                   |
Event ID: 6112
Message EVPN Virtual Tunnel EndPoint Neighbor <ip> added to Port<port> on VRF
<vrf>
| Category | NDM         |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description EVPNVirtualTunnelEndPointNeighboraddedtotheneighbortable
Event ID: 6113
Message EVPN Virtual Tunnel EndPoint Neighbor <ip> updated on Port<port> and
|          | VRF <vrf>   | with mac <mac> |     |
| -------- | ----------- | -------------- | --- |
| Category | NDM         |                |     |
| Severity | Information |                |     |
Description EVPNVirtualTunnelEndPointNeighborUpdatedintheneighbortable
Event ID: 6114
Message EVPN VTEP Neighbor <ip> deleted from Port<port> and VRF <vrf>
| Category    | NDM                                         |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Severity    | Information                                 |     |     |
| Description | EVPNVTEPNeighbordeletedfromtheneighbortable |     |     |
Event ID: 6115
| Message | Management | Role set | to <role> |
| ------- | ---------- | -------- | --------- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 246

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

NDM events | 247

| Severity | Information |     |     |     |
| -------- | ----------- | --- | --- | --- |
Description VSXneighbordatapathinitsyncstatusisneighborsyncinprogress
Event ID: 6121
| Message     | static neighbor                          | <ip> add | failed, Subnet | match failed |
| ----------- | ---------------------------------------- | -------- | -------------- | ------------ |
| Category    | NDM                                      |          |                |              |
| Severity    | Error                                    |          |                |              |
| Description | StaticNeighboraddfailed,subnetnotmatched |          |                |              |
Event ID: 6122
| Message     | static neighbor                   | <ip> add | failed, it | is own ip |
| ----------- | --------------------------------- | -------- | ---------- | --------- |
| Category    | NDM                               |          |            |           |
| Severity    | Error                             |          |            |           |
| Description | StaticNeighboraddfailed,itisownip |          |            |           |
Event ID: 6123
Message static neighbor <ip> Subnet match add failed, port is down
| Category    | NDM                                |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Error                              |     |     |     |
| Description | StaticNeighboraddfailed,portisdown |     |     |     |
Event ID: 6124
| Message     | Neighbor table                             | VSX peer | DB connection | terminated |
| ----------- | ------------------------------------------ | -------- | ------------- | ---------- |
| Category    | NDM                                        |          |               |            |
| Severity    | Information                                |          |               |            |
| Description | NeighbortableVSXpeerDBconnectionterminated |          |               |            |
Event ID: 6125
| Message     | Neighbor table                              | VSX peer | DB connection | established |
| ----------- | ------------------------------------------- | -------- | ------------- | ----------- |
| Category    | NDM                                         |          |               |             |
| Severity    | Information                                 |          |               |             |
| Description | NeighbortableVSXpeerDBconnectionestablished |          |               |             |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 248

Event ID: 6126
| Message     | VSX Peer                           | IP <ip> added | the port <port> | and VRF <vrf> |
| ----------- | ---------------------------------- | ------------- | --------------- | ------------- |
| Category    | NDM                                |               |                 |               |
| Severity    | Information                        |               |                 |               |
| Description | VSXPeerIPaddedinportvsxPeerIpCache |               |                 |               |
Event ID: 6127
Message VSX Peer IP <ip> deleted from the port <port> and VRF <vrf>
| Category    | NDM                                  |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | VSXPeerIPdeletedinportvsxPeerIpCache |     |     |     |
Event ID: 6128
| Message     | Proxy arp                           | enabled for | the port <port> |     |
| ----------- | ----------------------------------- | ----------- | --------------- | --- |
| Category    | NDM                                 |             |                 |     |
| Severity    | Information                         |             |                 |     |
| Description | Proxyarpenabledforthegiveninterface |             |                 |     |
Event ID: 6129
| Message     | Proxy arp                           | disabled | for the port <port> |     |
| ----------- | ----------------------------------- | -------- | ------------------- | --- |
| Category    | NDM                                 |          |                     |     |
| Severity    | Information                         |          |                     |     |
| Description | Proxyarpdiabledforthegiveninterface |          |                     |     |
Event ID: 6130
Message Neighbor <ip> modified on Port <port> and VRF <vrf> from mac <old_
|             | mac> to          | new mac <new_mac> |     |     |
| ----------- | ---------------- | ----------------- | --- | --- |
| Category    | NDM              |                   |     |     |
| Severity    | Information      |                   |     |     |
| Description | Neighbormodified |                   |     |     |
Event ID: 6131
NDMevents|249

| Message     | Neighbor                       | Discovery daemon started |     |
| ----------- | ------------------------------ | ------------------------ | --- |
| Category    | NDM                            |                          |     |
| Severity    | Information                    |                          |     |
| Description | NeighborDiscoverydaemonstarted |                          |     |
Event ID: 6132
Message Duplicate IPv4 address <ip> is detected on port <port> with a MAC
|             | address                         | of <mac>' throttle_count: | 40  |
| ----------- | ------------------------------- | ------------------------- | --- |
| Category    | NDM                             |                           |     |
| Severity    | Error                           |                           |     |
| Description | DuplicateIPdetectedfromARPreply |                           |     |
Event ID: 6133
Message Duplicate IPv6 address <ip> is detected on port <port> with a MAC
|          | address | of <mac> |     |
| -------- | ------- | -------- | --- |
| Category | NDM     |          |     |
| Severity | Error   |          |     |
Description DuplicateIPv6addressdetectedfromNeighbouradvertisement
Event ID: 6134
Message Duplicate IPv4 address <ip> is detected on port <port> with a MAC
|             | address                           | of <mac>' throttle_count: | 40  |
| ----------- | --------------------------------- | ------------------------- | --- |
| Category    | NDM                               |                           |     |
| Severity    | Error                             |                           |     |
| Description | DuplicateIPdetectedfromARPrequest |                           |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 250

Chapter 77
NTP events
NTP events
ThefollowingaretheeventsrelatedtoNTP.
Event ID: 1101
| Message     | NTP Association                        | <event>: | <server> <server_info> |
| ----------- | -------------------------------------- | -------- | ---------------------- |
| Category    | NTP                                    |          |                        |
| Severity    | Information                            |          |                        |
| Description | LogsNTPAssociationconfigurationchanges |          |                        |
Event ID: 1102
Message NTP Trusted keys <trusted_keys> and Untrusted keys <untrusted_keys>
| Category    | NTP                                           |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Information                                   |     |     |
| Description | LogsNTPTrustedandUntrustedauthentication-keys |     |     |
Event ID: 1103
| Message     | NTP Authentication                | state | change: <old> -> <new> |
| ----------- | --------------------------------- | ----- | ---------------------- |
| Category    | NTP                               |       |                        |
| Severity    | Information                       |       |                        |
| Description | LogsNTPAuthenticationstatechanges |       |                        |
Event ID: 1104
| Message     | NTP VRF state                       | change: <old> | -> <new> |
| ----------- | ----------------------------------- | ------------- | -------- |
| Category    | NTP                                 |               |          |
| Severity    | Information                         |               |          |
| Description | LogsNTPVRFconfigurationstatechanges |               |          |
Event ID: 1105
251
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message NTP primary server connection established to <server>
| Category | NTP         |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description LogsNTPprimaryserverconnectionestablishedstatechange
Event ID: 1106
| Message     | NTP primary                                   | server connection | lost to <server> |
| ----------- | --------------------------------------------- | ----------------- | ---------------- |
| Category    | NTP                                           |                   |                  |
| Severity    | Information                                   |                   |                  |
| Description | LogsNTPprimaryserverconnectionloststatechange |                   |                  |
Event ID: 1107
| Message     | NTP enable                                     | state change: | <old> -> <new> |
| ----------- | ---------------------------------------------- | ------------- | -------------- |
| Category    | NTP                                            |               |                |
| Severity    | Information                                    |               |                |
| Description | EventraisedwhenNTPischangedtoenabledordisabled |               |                |
NTPevents|252

Chapter 78
OSPFv2 events
OSPFv2 events
ThefollowingaretheeventsrelatedtoOSPFv2.
Event ID: 2401
Message AdjChg: Nbr <router-id> on <ospf-interface>(<area>): <old_state> ->
<new_state>
| Category    | OSPFv2                                       |     |     |
| ----------- | -------------------------------------------- | --- | --- |
| Severity    | Information                                  |     |     |
| Description | LogsthechangesinOSPFv2neighbourstatemachine. |     |     |
Event ID: 2402
Message Interface <interface>(<area>) changed from <old_state> to <new_
|             | state>, input:                        | <input> |     |
| ----------- | ------------------------------------- | ------- | --- |
| Category    | OSPFv2                                |         |     |
| Severity    | Information                           |         |     |
| Description | LogsthechangesintheinterfaceFSMstate. |         |     |
Event ID: 2403
| Message     | <event> with                 | <destination> | <nexthops> |
| ----------- | ---------------------------- | ------------- | ---------- |
| Category    | OSPFv2                       |               |            |
| Severity    | Information                  |               |            |
| Description | LogsOSPFv2routeaddanddelete. |               |            |
Event ID: 2404
Message AdjChg: Nbr <router-id> on <ospf-interface>: <state> -> <next_state>
(<event>)
| Category    | OSPFv2                                       |     |     |
| ----------- | -------------------------------------------- | --- | --- |
| Severity    | Information                                  |     |     |
| Description | LogsthechangesinOSPFv2neighbourstatemachine. |     |     |
Event ID: 2405
253
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Router-id                     | updated from | <old> to <new> |
| ----------- | ----------------------------- | ------------ | -------------- |
| Category    | OSPFv2                        |              |                |
| Severity    | Information                   |              |                |
| Description | Logsthechangesintherouter-id. |              |                |
Event ID: 2406
| Message     | Failed                                      | to <action> <rule> | error: <err> |
| ----------- | ------------------------------------------- | ------------------ | ------------ |
| Category    | OSPFv2                                      |                    |              |
| Severity    | Error                                       |                    |              |
| Description | LogserrorsforOSPFv2FPcreation/installation. |                    |              |
Event ID: 2407
Message OSPF all routers field entry added: group_id=<group_id> fp_id=<fp_id>
stat_id=<stats_id>
| Category    | OSPFv2                                |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Information                           |     |     |
| Description | LogsforOSPFv2FPcreation/installation. |     |     |
Event ID: 2408
Message OSPF designated routers field entry added: group_id=<group_id> fp_
|             | id=<fp_id>                              | stat_id=<stats_id> |     |
| ----------- | --------------------------------------- | ------------------ | --- |
| Category    | OSPFv2                                  |                    |     |
| Severity    | Information                             |                    |     |
| Description | LogsforOSPFv2DRFPcreation/installation. |                    |     |
Event ID: 2409
Message Graceful Restart state changed, <old_state> -> <new_state>, reason:
<reason>
| Category    | OSPFv2                                      |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Severity    | Information                                 |     |     |
| Description | LogsthechangesofOSPFv2GracefulRestartstate. |     |     |
Event ID: 2410
OSPFv2events|254

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

255

Chapter 79
OSPFv3 events
OSPFv3 events
ThefollowingaretheeventsrelatedtoOSPFv3.
Event ID: 4901
| Message     | Failed                                      | to <action> | <rule> error: <err> |
| ----------- | ------------------------------------------- | ----------- | ------------------- |
| Category    | OSPFv3                                      |             |                     |
| Severity    | Error                                       |             |                     |
| Description | LogserrorsforOSPFv3FPcreation/installation. |             |                     |
Event ID: 4902
Message OSPF3 all routers field entry added: group_id=<group_id> fp_id=<fp_
id> stat_id=<stats_id>
| Category    | OSPFv3                                |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Information                           |     |     |
| Description | LogsforOSPFv3FPcreation/installation. |     |     |
Event ID: 4903
Message OSPF3 designated routers field entry added: group_id=<group_id> fp_
|             | id=<fp_id>                              | stat_id=<stats_id> |     |
| ----------- | --------------------------------------- | ------------------ | --- |
| Category    | OSPFv3                                  |                    |     |
| Severity    | Information                             |                    |     |
| Description | LogsforOSPFv3DRFPcreation/installation. |                    |     |
Event ID: 4904
Message AdjChg: Nbr<router-id> on interface <link-local> on <interface>
|             | (<area>):                                    | <old_state> | -> <new_state> |
| ----------- | -------------------------------------------- | ----------- | -------------- |
| Category    | OSPFv3                                       |             |                |
| Severity    | Information                                  |             |                |
| Description | LogsthechangesinOSPFv3neighbourstatemachine. |             |                |
Event ID: 4905
256
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Interface <link-local> on <interface>(<area>) changed from <old_
|             | state>                                | to <new_state>, | input: | <input> |     |
| ----------- | ------------------------------------- | --------------- | ------ | ------- | --- |
| Category    | OSPFv3                                |                 |        |         |     |
| Severity    | Information                           |                 |        |         |     |
| Description | LogsthechangesintheinterfaceFSMstate. |                 |        |         |     |
| Event ID:   | 4906                                  |                 |        |         |     |
Message Graceful Restart state changed, <old_state> -> <new_state>, reason:
<reason>
| Category    | OSPFv3                                      |     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |     |
| Description | LogsthechangesofOSPFv3GracefulRestartstate. |     |     |     |     |
| Event ID:   | 4907                                        |     |     |     |     |
Message Duplicate router-id for <link-local> from source <source-ip>
| Category    | OSPFv3                        |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | --- |
| Severity    | Error                         |     |     |     |     |
| Description | Logswhenrouter-idisduplicate. |     |     |     |     |
| Event ID:   | 4908                          |     |     |     |     |
Message Distance External <external>, Inter-area <inter>, and Intra-area
|             | <intra>                         | applied | to all the | OSPFv3 processes | in <vrf> VRF |
| ----------- | ------------------------------- | ------- | ---------- | ---------------- | ------------ |
| Category    | OSPFv3                          |         |            |                  |              |
| Severity    | Information                     |         |            |                  |              |
| Description | LogsthechangesofOSPFv3distance. |         |            |                  |              |
| Packet      | capture                         | events  |            |                  |              |
Thefollowingaretheeventsrelatedtopacketcapturesessions.
| Event ID: | 15201 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
Message
capturefailedtostartthesession{session_name}
| Category | Packetcapture |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- |
| Severity | Error         |     |     |     |     |
Packetcaptureevents|257

Description

Event raised when packet capture is failed to start

Event ID: 15202

Message

Packet capture failed to stop the session {session_name}

Category

Packet capture

Severity

Error

Description

Event raised when packet capture is failed to stop

Event ID: 15203

Message

Packet capture started for the session {session_name}

Category

Packet capture

Severity

Information

Description

Event raised when packet capture is started

Event ID: 15204

Message

Packet capture stopped for the session {session_name}

Category

Packet capture

Severity

Information

Description

Event raised when packet capture is stopped

Event ID: 15205

Message

Packet capture session {session_name} client state set to initializing

Category

Packet capture

Severity

Information

Description

Packet capture session row client state set to initializing

Event ID: 15206

Message

Packet capture session {session_name} client state set to in-progress

Category

Packet capture

Severity

Information

Description

acket capture session row client state set to in-progress

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

258

Event ID: 15207

Message

acket capture session {session_name} client state set to completed

Category

Packet capture

Severity

Information

Description

Packet capture session row client state set to completed

Event ID: 15208

Message

Packet capture session {session_name} client state set to hw failed

Category

Packet capture

Severity

Error

Description

Packet capture session row client state set to hw failed

Event ID: 15209

Message

Packet capture session {session_name} client state set to connection failed

Category

Packet capture

Severity

Error

Description

Packet capture session row client state set to conection failed

Event ID: 15210

Message

Packet capture session {session_name} hw programmed is {value}

Category

Packet capture

Severity

Information

Description

Packet capture session row hw programmed value

Event ID: 15211

Message

Packet capture session {session_name} max timeout reached

Category

Packet capture

Severity

Information

Description

Packet capture session row client state set to completed due to max time out

Event ID: 15212

Packet capture events | 259

Message

Packet capture session {session_name} max packet transmitted

Category

Packet capture

Severity

Information

Description

Packet capture session row client state set to completed due to max packet transmitted

Event ID: 15213

Message

Packet capture configuration error for session {session_name}, reason : {reason}

Category

Packet capture

Severity

Error

Description

Event raised when packet capture configuration is invalid

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

260

Chapter 80
Password Reset events
| Password Reset | events |     |     |     |
| -------------- | ------ | --- | --- | --- |
Thefollowingaretheeventsrelatedtopasswordreset.
Event ID: 5901
| Message     | Password reset                                   | succeeded | for admin | user. |
| ----------- | ------------------------------------------------ | --------- | --------- | ----- |
| Category    | PasswordReset                                    |           |           |       |
| Severity    | Information                                      |           |           |       |
| Description | Logmessagewhenadminuserpasswordresetissuccessful |           |           |       |
Event ID: 5902
| Message     | Password reset                            | failed | for admin | user. |
| ----------- | ----------------------------------------- | ------ | --------- | ----- |
| Category    | PasswordReset                             |        |           |       |
| Severity    | Information                               |        |           |       |
| Description | Logmessagewhenadminuserpasswordresetfails |        |           |       |
261
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 81

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

262

| Message | Failed | to add flow | <dip0>.<dip1>.<dip2>.<dip3>, |     |     |
| ------- | ------ | ----------- | ---------------------------- | --- | --- |
<sip0>.<sip1>.<sip2>.<sip3> (<status> <srcport> <srcvid> <totalvid>
|             | <flowtype>      | <callerid>) |     |     |     |
| ----------- | --------------- | ----------- | --- | --- | --- |
| Category    | PIM             |             |     |     |     |
| Severity    | Error           |             |     |     |     |
| Description | Failedtoaddflow |             |     |     |     |
Event ID: 5106
Message Failed to remove flow g <dip0>.<dip1>.<dip2>.<dip3>, s <sip0>,
|     | <sip1>.<sip2>.<sip3> |     | (<status> | <srcport> | <srcvid> <flowtype> |
| --- | -------------------- | --- | --------- | --------- | ------------------- |
<callerid>)
| Category    | PIM                           |     |     |     |     |
| ----------- | ----------------------------- | --- | --- | --- | --- |
| Severity    | Error                         |     |     |     |     |
| Description | FailedtoremoveflowforHardware |     |     |     |     |
Event ID: 5107
Message Failed to add a mroute for s=<source>, g=<group> on interface
|             | <interfaceName>                            | as  | the configured | mroute | limits are reached' |
| ----------- | ------------------------------------------ | --- | -------------- | ------ | ------------------- |
|             | throttle_count:                            | 100 |                |        |                     |
| Category    | PIM                                        |     |                |        |                     |
| Severity    | Warning                                    |     |                |        |                     |
| Description | Failedtoprogrammrouteasthelimitsarereached |     |                |        |                     |
Event ID: 5108
Message Failed to add a mroute for s=<source>, g=<group> on interface
<interfaceName> as the configured sources per group limit is reached'
|          | throttle_count: | 100 |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Category | PIM             |     |     |     |     |
| Severity | Warning         |     |     |     |     |
Description Failedtoprogrammrouteasthesourcespergrouplimitisreached
Event ID: 5109
Message This router is elected as the <ip_version> <state> for interface
<ifname>
| Category | PIM |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
PIMevents|263

| Severity    | Information      |     |     |
| ----------- | ---------------- | --- | --- |
| Description | PIMDRelectionlog |     |     |
Event ID: 5110
Message <type> <reason> failed with Fd: <fd> on Port: <port>. Error
|             | description:                 | <err> |     |
| ----------- | ---------------------------- | ----- | --- |
| Category    | PIM                          |       |     |
| Severity    | Error                        |       |     |
| Description | Multicastsocketcreationerror |       |     |
Event ID: 5111
Message OVSDB operation failed with <err>' throttle_count: 100
| Category    | PIM               |     |     |
| ----------- | ----------------- | --- | --- |
| Severity    | Error             |     |     |
| Description | DBOperationfailed |     |     |
Event ID: 5112
Message New Elected BSR for VRF <vrf_name> is <ebsr_ip> with priority
<priority>
| Category    | PIM         |     |     |
| ----------- | ----------- | --- | --- |
| Severity    | Information |     |     |
| Description | ElectedBSR  |     |     |
Event ID: 5113
| Message     | Elected BSR       | removed | on VRF <vrf_name> |
| ----------- | ----------------- | ------- | ----------------- |
| Category    | PIM               |         |                   |
| Severity    | Information       |         |                   |
| Description | ElectedBSRremoved |         |                   |
Event ID: 5114
Message Candidate BSR <ip_address> with priority <priority> is <status> on
|     | interface | <ifname> |     |
| --- | --------- | -------- | --- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 264

| Category    | PIM                    |     |     |
| ----------- | ---------------------- | --- | --- |
| Severity    | Information            |     |     |
| Description | ConfiguredcandidateBSR |     |     |
Event ID: 5115
Message PIM Neighbor <neighbor_ip> is <event> on interface <ifname>
| Category    | PIM            |     |     |
| ----------- | -------------- | --- | --- |
| Severity    | Information    |     |     |
| Description | Neighborstatus |     |     |
Event ID: 5116
Message <pkt> packet is discarded on interface <ifname>. Reason: <reason>'
|             | throttle_count: 100 |     |     |
| ----------- | ------------------- | --- | --- |
| Category    | PIM                 |     |     |
| Severity    | Warning             |     |     |
| Description | Packetdrop          |     |     |
Event ID: 5117
Message Forwarding state has changed to <state> on <ip_version> enabled
interface <ifname>
| Category    | PIM                        |     |     |
| ----------- | -------------------------- | --- | --- |
| Severity    | Information                |     |     |
| Description | Interfaceoperationalstatus |     |     |
Event ID: 5118
Message <pim_version> <mode> mode is <status> on interface <ifname>
| Category    | PIM              |     |     |
| ----------- | ---------------- | --- | --- |
| Severity    | Information      |     |     |
| Description | InterfacePIMmode |     |     |
Event ID: 5119
| Message | Router <pim_version> | is <mode> | on VRF <vrfname> |
| ------- | -------------------- | --------- | ---------------- |
PIMevents|265

| Category    | PIM                          |     |     |
| ----------- | ---------------------------- | --- | --- |
| Severity    | Information                  |     |     |
| Description | Routerpimconfigurationstatus |     |     |
Event ID: 5120
Message Candidate RP <ip_address> is <event> on VRF <vrf_name>
| Category    | PIM                        |     |     |
| ----------- | -------------------------- | --- | --- |
| Severity    | Information                |     |     |
| Description | LearntorremovedcandidateRP |     |     |
Event ID: 5121
Message Software Packet Queue <limit> threshold value <val> reached. Queue
size: <qsize>
| Category    | PIM                                 |     |     |
| ----------- | ----------------------------------- | --- | --- |
| Severity    | Information                         |     |     |
| Description | SoftwarePacketQueuereachesthreshold |     |     |
Event ID: 5122
Message This router is elected as the <ip_version> VSX <state> for interface
<ifname>
| Category    | PIM                 |     |     |
| ----------- | ------------------- | --- | --- |
| Severity    | Information         |     |     |
| Description | PIMVSXDRElectionlog |     |     |
Event ID: 5123
| Message     | VSX ISL Status        | changed | to <isl_status> |
| ----------- | --------------------- | ------- | --------------- |
| Category    | PIM                   |         |                 |
| Severity    | Information           |         |                 |
| Description | VSXISLStatusupdatelog |         |                 |
Event ID: 5124
Message Candidate RP <ip_address> is configured on interface <ifname>
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 266

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

PIM events | 267

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

Event ID: 5132

Message

Category

Severity

Description

Event ID: 5133

Vxlan-tunnel configured with {mode} mode. Border router functionality is {status} on this

router.

PIM

Information

The dynamic VXLAN tunnel bridging mode configured and the Border Gateway status

with respect to PIM.

Message

PIM NSF timer {status} {action_str}

Category

PIM

Severity

Information

Description

PIM NSF timer status

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

268

Chapter 82

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

269

Chapter 83
Port access events
| Port access events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
Thefollowingaretheeventsrelatedtoportaccess.
Event ID: 10501
Message Client <mac_address> was logged-off administratively through command-
line interface
| Category | Portaccess  |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Clientwaslogged-offadministrativelythroughcommand-lineinterface
Event ID: 10502
| Message     | Port <port>                         | is blocked | by port-access |     |
| ----------- | ----------------------------------- | ---------- | -------------- | --- |
| Category    | Portaccess                          |            |                |     |
| Severity    | Information                         |            |                |     |
| Description | Theportisblockedbyport-accessdaemon |            |                |     |
Event ID: 10503
| Message     | Port <port>                           | is unblocked | by port-access |     |
| ----------- | ------------------------------------- | ------------ | -------------- | --- |
| Category    | Portaccess                            |              |                |     |
| Severity    | Information                           |              |                |     |
| Description | Theportisunblockedbyport-accessdaemon |              |                |     |
Event ID: 10504
Message Clients were logged-off on the port <port> due to a change in
|          | authentication | mode | from <device/client> | to client/device> |
| -------- | -------------- | ---- | -------------------- | ----------------- |
| Category | Portaccess     |      |                      |                   |
| Severity | Information    |      |                      |                   |
Description Theauthenticationmodeassociatedwiththeportischanged
Event ID: 10505
270
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Clients were logged-off on the port <port> due to a change in client
|             | limit from                                   | <old_limit> | to <new_limit> |
| ----------- | -------------------------------------------- | ----------- | -------------- |
| Category    | Portaccess                                   |             |                |
| Severity    | Information                                  |             |                |
| Description | Theclientlimitassociatedwiththeportischanged |             |                |
Event ID: 10506
Message The name associated with VLAN <vlan_id> changed from <old_name> to
<new_name>
| Category | Portaccess  |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description ThenameassociatedwithaVLANinusebyport-accessdaemonchanged
Event ID: 10507
Message Clients using policy <policy_name> were logged-off due to a
|             | configuration                            | change | in the policy |
| ----------- | ---------------------------------------- | ------ | ------------- |
| Category    | Portaccess                               |        |               |
| Severity    | Information                              |        |               |
| Description | Thepolicyconfigurationisupdatedbytheuser |        |               |
Event ID: 10508
| Message  | VLAN conflict | detected | on port <port-name> |
| -------- | ------------- | -------- | ------------------- |
| Category | Portaccess    |          |                     |
| Severity | Error         |          |                     |
Description VLANisconfiguredasTrunkforsomeclientsandaccessforothers.Thiscouldpotentially
resultintrafficloss
Event ID: 10509
Message Client limit exceeded on port <port>, caused by an unauthenticated
client <mac_addr>
| Category    | Portaccess                                |     |     |
| ----------- | ----------------------------------------- | --- | --- |
| Severity    | Error                                     |     |     |
| Description | Logeventwhenanintruderisdetectedontheport |     |     |
Event ID: 10510
Portaccessevents|271

Message

All clients except client with MAC address <mac_addr> logged-off on
the port <port> due to a change in authentication mode from <old_
mode> to <new_mode>

Category

Port access

Severity

Information

Description

The authentication mode associated with the port is changed

Event ID: 10511

Message

All clients except client with MAC address <mac_addr> logged-off on
the port <port> due to a proxy-logoff request

Category

Port access

Severity

Information

Description

Clients were logged off due to proxy logoff

Event ID: 10512

Message

Client with MAC address <mac_addr> learnt on port <port-name>

Category

Port access

Severity

Information

Description

Received a client for authentication/authorization on secure port

Event ID: 10513

Message

Client with MAC address <mac_addr> deleted on port <port-name>

Category

Port access

Severity

Information

Description

Deleted a port-access client

Event ID: 10514

Message

Client with MAC address <mac_addr> authorized on port <port-name>
with role <role-name>

Category

Port access

Severity

Information

Description

Client authorized with role

Event ID: 10515

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

272

Message

Client with MAC address <mac_addr> on port <port-name> failed <auth-
method> authentication with reason <failure-reason>

Category

Port access

Severity

Information

Description

Client has failed authentication

Event ID: 10516

Message

Client with MAC address <mac_addr> on port <if_name> triggered for
MAC authentication request with ID <request_id>

Category

Port access

Severity

Information

Description

MAC authentication request sent for client

Event ID: 10517

Message

Client with MAC address <mac_addr> on port <if-name> received
response for MAC-Authentication request ID <request-id> as <response>

Category

Port access

Severity

Information

Description

MAC authentication response received for client

Event ID: 10518

Message

Client with MAC address <mac_addr> on port <if-name> triggered for
802.1x authentication request with ID <request-id>

Category

Port access

Severity

Information

Description

802.1x Authentication response received for client

Event ID: 10519

Message

Client with MAC address <mac_addr> on port <if-name> received
response for 802.1x authentication request ID <request-id> as
<response>

Category

Port access

Severity

Information

Description

802.1x Authentication response received for client

Port access events | 273

Event ID: 10520

Message

Reached the maximum cached-clients limit of <limit> on the switch
for Limited Auth-Survivability

Category

Port access

Severity

Information

Description

Port Access cached-client maximum limit reached

Event ID: 10521

Message

Restored <num-cached-clients> cached-clients from persistent-storage
after reboot

Category

Port access

Severity

Information

Description

Cached-Clients were recovered from persistent-storage

Event ID: 10522

Message

Interface <if-name> is flapped by port-access as port of a CoA
request

Category

Port access

Severity

Information

Description

The port is flapped by port-access daemon

Event ID: 10523

Message

Interface <if-name> is disabled by port-access as port of a CoA
request

Category

Port access

Severity

Information

Description

The port is disabled by port-access daemon

Event ID: 10524

Message

<request_pkt> request received for client with MAC address <mac_
addr> on port <if-name> from dyn-authorization client <address> on
vrf <vrf-name>

Category

Port access

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

274

Severity

Information

Description

Disconnect/CoA request received from dyn-authorization client

Event ID: 10525

Message

<request_pkt> request received from <address> on VRF <vrf_name> for
client with MAC address <mac_addr> on port <if-name> is successfully
processed

Category

Port access

Severity

Information

Description

Disconnect/CoA request request is handled successfully

Event ID: 10526

Message

<request_pkt> request received from <address> on VRF <vrf_name> for
client with MAC address <mac_addr> on port <if-name> failed to
process with error <error_cause>

Category

Port access

Severity

Information

Description

Disconnect/CoA request request is failed

Event ID: 10527

Message

MAC Authentication triggered for client <mac_addr> on port <if_name>
with ID <request_id> to server <ip:port, proto, vrf {vrf_name}>

Category

Port access

Severity

Information

Description

MAC Authentication reuqest sent for client

Event ID: 10528

Message

MAC Authentication succeeded for client <mac_addr> on port <if_name>
with ID <request_id> to server <ip:port, proto, vrf {vrf_name}>

Category

Port access

Severity

Information

Description

MAC Authentication response received for client

Event ID: 10529

Port access events | 275

Message MAC Authentication failed with reason <response> for client <mac_
addr> on port <if_name> with ID <request_id> from servers <server_
list>
| Category    | Portaccess                                 |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Information                                |     |     |     |
| Description | MACAuthenticationresponsereceivedforclient |     |     |     |
Event ID: 10530
Message 802.1x Authentication triggered for client <mac_addr> on port <if_
name> with ID <request_id> to server <ip:port, proto, vrf {vrf_name}>
| Category    | Portaccess                               |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- |
| Severity    | Information                              |     |     |     |
| Description | 802.1xAuthenticationrequestsentforclient |     |     |     |
Event ID: 10531
Message 802.1x Authentication succeeded for client <mac_addr> on port <if_
name> with ID <request_id> from server <ip:port, proto, vrf {vrf_
name}>
| Category    | Portaccess                                |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Information                               |     |     |     |
| Description | 802.1xAuthenticationresponsesentforclient |     |     |     |
Event ID: 10532
Message 802.1x Authentication failed with reason <response> for client <mac_
addr> on port <if_name> with ID <request_id> from servers <server_
list>
| Category    | Portaccess                                    |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | 802.1xAuthenticationresponsereceivedforclient |     |     |     |
Event ID: 10533
| Message     | Interface                                | <if_name> | is blocked | by port-access |
| ----------- | ---------------------------------------- | --------- | ---------- | -------------- |
| Category    | Portaccess                               |           |            |                |
| Severity    | Information                              |           |            |                |
| Description | Theinterfaceisblockedbyport-accessdaemon |           |            |                |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 276

Event ID: 10534
Message
|             | Interface                                  | <if_name> | is unblocked | by port-access |        |
| ----------- | ------------------------------------------ | --------- | ------------ | -------------- | ------ |
| Category    | Portaccess                                 |           |              |                |        |
| Severity    | Information                                |           |              |                |        |
| Description | Theinterfaceisunblockedbyport-accessdaemon |           |              |                |        |
| Port access | application-based                          |           |              | policy         | events |
Thefollowingaretheeventsrelatedtoportaccessapplication-basedpolicies(ABPs).
Event ID: 14701
Message
Configurationchangeinthepolicy{pac_abp_name}{operation}
| Category | PORT_ACCESS_ABP |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Severity | Information     |     |     |     |     |
Description
Userupdatedtheapplicationbasedpolicyconfiguratio.
Event ID: 14702
Message onfigurationupdateinthepolicyduetoclasschange{pac_abp_name}{operation}
| Category | PORT_ACCESS_ABP |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Severity | Error           |     |     |     |     |
Description Userupdatedtheapplicationbasedpolicyclassconfiguration
Event ID: 14703
Message
Triggerreceivedto{operation}policy:{pac_abp_name}forclient:{client}
| Category | PORT_ACCESS_ABP |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
| Severity | Information     |     |     |     |     |
Description
Theapplicationbasedpolicyapplying/unapplyingforclient
Event ID: 14704
Message Triggerreceivedto{operation}policy:{pac_abp_name}forclient:{client}is{result}
| Category | PORT_ACCESS_ABP |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- |
Portaccessapplication-basedpolicyevents|277

Severity

Error

Description

Trigger received to {operation} policy: {pac_abp_name} for client: {client}

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

278

|             |             |               |       |       | Chapter | 84     |
| ----------- | ----------- | ------------- | ----- | ----- | ------- | ------ |
|             |             | Port access   | group | based | policy  | events |
| Port access | group based | policy events |       |       |         |        |
Thefollowingaretheeventsrelatedtoportaccessgroupbasedpolicy.
| Event ID: | 12601 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message Configuration change in the policy <pac_gbp_name> <operation>
| Category | Portaccessgroupbasedpolicy |     |     |     |     |     |
| -------- | -------------------------- | --- | --- | --- | --- | --- |
| Severity | Information                |     |     |     |     |     |
Description Thegroupbasedpolicyconfigurationisupdatedbytheuser
| Event ID: | 12602 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message Configuration update in the policy due to class change <pac_gbp_name>
<operation>
| Category | Portaccessgroupbasedpolicy |     |     |     |     |     |
| -------- | -------------------------- | --- | --- | --- | --- | --- |
| Severity | Information                |     |     |     |     |     |
Description Thegroupbasedpolicyclassconfigurationisupdatedbytheuser
| Event ID: | 12603 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
Message Trigger received to <operation> policy: <pac_gbp_name> for client:
<client>
| Category    | Portaccessgroupbasedpolicy                      |     |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                                     |     |     |     |     |     |
| Description | Thegroupbasedpolicyapplying/unapplyingforclient |     |     |     |     |     |
| Event ID:   | 12604                                           |     |     |     |     |     |
Message Trigger received to <operation> policy: <pac_gbp_name> for client:
|             | <client>                                        | is <result> |     |     |     |     |
| ----------- | ----------------------------------------------- | ----------- | --- | --- | --- | --- |
| Category    | Portaccessgroupbasedpolicy                      |             |     |     |     |     |
| Severity    | Information                                     |             |     |     |     |     |
| Description | Thegroupbasedpolicyapply/unapplyforclientresult |             |     |     |     |     |
| Event ID:   | 12605                                           |             |     |     |     |     |
279
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

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

Port access group based policy events | 280

Chapter 85

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

Event ID: 9303

Message

A local user role with name {role_name} already exists and conflicts with the newly

inserted ClearPass role

Category

Port access roles

Severity

Warning

Description

Warns a user when local user role is already existing.

Event ID: 9304

Message

A ClearPass role with name {role_name} already exists and conflicts with the newly

inserted {role_type} role.

Category

Port access roles

Severity

Warning

Description

Warns a user when a ClearPass role is already existing.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

281

Chapter 86
Port events
Port events
Thefollowingaretheeventsrelatedtoport.
Event ID: 601
| Message     | Netlink socket                     | creation | failed <error> |
| ----------- | ---------------------------------- | -------- | -------------- |
| Category    | Port                               |          |                |
| Severity    | Information                        |          |                |
| Description | Logwhennetlinksocketcreationfailed |          |                |
Event ID: 602
| Message     | Netlink socket                 | bind failed | <error> |
| ----------- | ------------------------------ | ----------- | ------- |
| Category    | Port                           |             |         |
| Severity    | Information                    |             |         |
| Description | Logwhennetlinksocketbindfailed |             |         |
Event ID: 603
Message Netlink failed to set mtu <mtu> for interface <interface>
| Category    | Port                                     |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | Logwhennetlinkfailedtosetmtuforinterface |     |     |
Event ID: 604
Message Netlink failed to bring <status> the interface <interface>
| Category    | Port                                           |     |     |
| ----------- | ---------------------------------------------- | --- | --- |
| Severity    | Information                                    |     |     |
| Description | Logwhennetlinkfailedtochangetheinterfacestatus |     |     |
Event ID: 605
282
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Unknown internal          | vlan policy | <policy> |
| ----------- | ------------------------- | ----------- | -------- |
| Category    | Port                      |             |          |
| Severity    | Information               |             |          |
| Description | Unknowninternalvlanpolicy |             |          |
Event ID: 606
| Message     | Error allocating                              | internal | vlan for port <vlan> |
| ----------- | --------------------------------------------- | -------- | -------------------- |
| Category    | Port                                          |          |                      |
| Severity    | Information                                   |          |                      |
| Description | Logwhenallocationfailedforinternalvlanforport |          |                      |
Event ID: 607
| Message     | Overlapping                               | networks observed | for <ip_address> |
| ----------- | ----------------------------------------- | ----------------- | ---------------- |
| Category    | Port                                      |                   |                  |
| Severity    | Error                                     |                   |                  |
| Description | Logwhenaduplicateaddressisreceivedonaport |                   |                  |
Portevents|283

Chapter 87

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

Client is trying to get access on a port security enabled port

Event ID: 9402

Message

Port security sticky client move violation triggered on port <port>
for client with MAC address <mac_addr>.' throttle_count: 30: yes

Category

Port security

Severity

Information

Description

Client, which has been programmed as sticky client on a port, tried to connect on
different port

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

284

Chapter 88

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

285

Chapter 89
Power events
Power events
Thefollowingaretheeventsrelatedtopower.
Event ID: 301
| Message     | PSU <name>               | changed state | to <state> |     |
| ----------- | ------------------------ | ------------- | ---------- | --- |
| Category    | Power                    |               |            |     |
| Severity    | Information              |               |            |     |
| Description | LogthechangeinPSUstatus. |               |            |     |
Event ID: 302
Message PSUs inserted in the system are of <Type> types. This is <Support>
configuration.
| Category    | Power                               |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Warning                             |     |     |     |
| Description | LogtheidentificationofmixedPSUtypes |     |     |     |
Event ID: 303
Message PSU <name> encountered a warning. Total warning count: <warnings>
| Category    | Power                             |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Error                             |     |     |     |
| Description | LogthewarningsencounteredbythePSU |     |     |     |
Event ID: 304
| Message     | PSU <name>                        | faulted. Total | fault count: | <failures> |
| ----------- | --------------------------------- | -------------- | ------------ | ---------- |
| Category    | Power                             |                |              |            |
| Severity    | Error                             |                |              |            |
| Description | LogthefailuresencounteredbythePSU |                |              |            |
Event ID: 305
286
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | PSU <name>:                        | Internal | communication | <status> |     |
| ----------- | ---------------------------------- | -------- | ------------- | -------- | --- |
| Category    | Power                              |          |               |          |     |
| Severity    | Warning                            |          |               |          |     |
| Description | LogPSUinternalcommunicationfailure |          |               |          |     |
Event ID: 306
| Message     | PSU <name>:    | Fan-<fanidx> | <status> |     |     |
| ----------- | -------------- | ------------ | -------- | --- | --- |
| Category    | Power          |              |          |     |     |
| Severity    | Warning        |              |          |     |     |
| Description | LogPSUfanfault |              |          |     |     |
Event ID: 307
Message PSU <name>: <sensorid> sensor <status> threshold limit
| Category    | Power                                        |     |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- | --- |
| Severity    | Warning                                      |     |     |     |     |
| Description | LogwhenPSUtemperaturesensorexceededthreshold |     |     |     |     |
Event ID: 308
Message PSU <name> has shutdown due to over temperature in <sensorid> sensor
| Category    | Power                                           |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- |
| Severity    | Error                                           |     |     |     |     |
| Description | LogwhenPSUtemperaturesensortriggeredPSUshutdown |     |     |     |     |
Event ID: 309
| Message     | PSU <name>:                             | Output current | <status> | threshold | limit |
| ----------- | --------------------------------------- | -------------- | -------- | --------- | ----- |
| Category    | Power                                   |                |          |           |       |
| Severity    | Warning                                 |                |          |           |       |
| Description | LogwhenPSUoutputcurrentexceedsthreshold |                |          |           |       |
Event ID: 310
| Message | PSU <name> | has shutdown | due to output | overcurrent |     |
| ------- | ---------- | ------------ | ------------- | ----------- | --- |
Powerevents|287

| Category    | Power                                       |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Error                                       |     |     |     |
| Description | LogwhenPSUoutputcurrenttriggeredPSUshutdown |     |     |     |
Event ID: 311
| Message     | PSU <name>                                  | has shutdown | due to output | overvoltage |
| ----------- | ------------------------------------------- | ------------ | ------------- | ----------- |
| Category    | Power                                       |              |               |             |
| Severity    | Error                                       |              |               |             |
| Description | LogwhenPSUoutputvoltagetriggeredPSUshutdown |              |               |             |
Event ID: 312
| Message     | PSU Redundancy                                | set | to <redund> |     |
| ----------- | --------------------------------------------- | --- | ----------- | --- |
| Category    | Power                                         |     |             |     |
| Severity    | Information                                   |     |             |     |
| Description | LogachangeinthePSUredundancyuserconfiguration |     |             |     |
Event ID: 313
| Message     | PSU Redundancy                               | operating | at <redund> |     |
| ----------- | -------------------------------------------- | --------- | ----------- | --- |
| Category    | Power                                        |           |             |     |
| Severity    | Information                                  |           |             |     |
| Description | LogachangeinthePSUredundancyoperationalstate |           |             |     |
Event ID: 314
Message PSU <name> disabled: PSU airflow does not match system-airflow
| Category | Power |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description LogwhenPSUisdisabledduetoairflowdirectionmismatch
Event ID: 315
| Message  | PSU <name> | disabled: | PSU communication | error |
| -------- | ---------- | --------- | ----------------- | ----- |
| Category | Power      |           |                   |       |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 288

| Severity    | Error                                       |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Description | LogwhenPSUisdisabledduetocommunicationerror |     |     |
Event ID: 316
Message <type> module <name> denied power due to insufficient power.
Configured PoE power can be deconfigured to allow card to be granted
power.
| Category | Power   |     |     |
| -------- | ------- | --- | --- |
| Severity | Warning |     |     |
Description Thereisinsufficientpowertopoweracard.PowercanberemovedfromconfiguredPoE
PDstobeabletopowerthecard.
Event ID: 317
Message PSU <name> disabled: PSU inserted is not supported by the system
| Category    | Power                                     |     |     |
| ----------- | ----------------------------------------- | --- | --- |
| Severity    | Warning                                   |     |     |
| Description | LogwhenPSUisdisabledduetoanunsupportedPSU |     |     |
Event ID: 318
| Message     | Power over                         | Ethernet status | has faulted |
| ----------- | ---------------------------------- | --------------- | ----------- |
| Category    | Power                              |                 |             |
| Severity    | Error                              |                 |             |
| Description | Log54VPoweroverEthernetstatusfault |                 |             |
Event ID: 319
| Message     | Power over                          | Ethernet status | is good |
| ----------- | ----------------------------------- | --------------- | ------- |
| Category    | Power                               |                 |         |
| Severity    | Information                         |                 |         |
| Description | Log54VPoweroverEthernetstatusisgood |                 |         |
Event ID: 320
| Message | PSU <name> | <alert> occurred |     |
| ------- | ---------- | ---------------- | --- |
Powerevents|289

| Category    | Power                        |     |
| ----------- | ---------------------------- | --- |
| Severity    | Error                        |     |
| Description | LogwhenPSUvoltagealertoccurs |     |
Event ID: 321
| Message     | PSU <name>                     | <alert> recovered |
| ----------- | ------------------------------ | ----------------- |
| Category    | Power                          |                   |
| Severity    | Information                    |                   |
| Description | LogwhenPSUvoltagealertrecovers |                   |
Event ID: 322
Message Invalid PoE power configuration, using default maximum PoE power
| Category    | Power                              |     |
| ----------- | ---------------------------------- | --- |
| Severity    | Warning                            |     |
| Description | LogwhenconfiguredPoEpowerisinvalid |     |
Event ID: 322
Message PSU {name} is not supported by the system. Please insert a supported
PSU. Refer to the Installation Guide for supported configurations.
| Category | Power |     |
| -------- | ----- | --- |
| Severity | Error |     |
Description LogeventforanunsupportedPSU,recordedperiodicallyforeachPSU
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 290

Chapter 90
|            |          |        | Power | over Ethernet | events |
| ---------- | -------- | ------ | ----- | ------------- | ------ |
| Power over | Ethernet | events |       |               |        |
ThefollowingaretheeventsrelatedtopoweroverEthernet.
| Event ID: | 7901 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Detected powered device on interface <interface_name>. Type:<pd_
|             | type>,                                       | Class:<pd_class> |     |     |     |
| ----------- | -------------------------------------------- | ---------------- | --- | --- | --- |
| Category    | PoweroverEthernet                            |                  |     |     |     |
| Severity    | Information                                  |                  |     |     |     |
| Description | Detectedpowereddeviceoninterface.Type,Class. |                  |     |     |     |
| Event ID:   | 7902                                         |                  |     |     |     |
Message Powered device power delivery on interface <interface_name>
| Category    | PoweroverEthernet                      |     |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                            |     |     |     |     |
| Description | Powereddevicepowerdeliveryoninterface. |     |     |     |     |
| Event ID:   | 7903                                   |     |     |     |     |
Message Powered device power denied on interface <interface_name>
| Category    | PoweroverEthernet                    |     |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- | --- |
| Severity    | Warning                              |     |     |     |     |
| Description | Powereddevicepowerdeniedoninterface. |     |     |     |     |
| Event ID:   | 7904                                 |     |     |     |     |
Message Powered device fault on interface <interface_name>. Fault type
<fault_type>
| Category    | PoweroverEthernet                        |     |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Severity    | Warning                                  |     |     |     |     |
| Description | Powereddevicefaultoninterface.Faulttype. |     |     |     |     |
| Event ID:   | 7905                                     |     |     |     |     |
291
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Powered device disconnected on interface <interface_name>
| Category    | PoweroverEthernet                     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- |
| Severity    | Information                           |     |     |     |
| Description | Powereddevicedisconnectedoninterface. |     |     |     |
Event ID: 7906
| Message     | PoE disabled           | on interface | <interface_name> |     |
| ----------- | ---------------------- | ------------ | ---------------- | --- |
| Category    | PoweroverEthernet      |              |                  |     |
| Severity    | Information            |              |                  |     |
| Description | PoEdisabledoninterface |              |                  |     |
Event ID: 7907
Message Powered device mps absent on interface <interface_name>
| Category    | PoweroverEthernet                 |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Information                       |     |     |     |
| Description | Powereddevicempsabsentoninterface |     |     |     |
Event ID: 7908
Message Detected dual signature powered device on interface <interface_name>.
|          | Type:<pd_type>,   | ClassA:<paira_class>, |     | ClassB:<pairb_class> |
| -------- | ----------------- | --------------------- | --- | -------------------- |
| Category | PoweroverEthernet |                       |     |                      |
| Severity | Information       |                       |     |                      |
Description Detecteddualsignaturepowereddeviceoninterface.Type,ClassA,ClassB
Event ID: 7909
Message Dual signature powered device power delivery on interface <interface_
name>
| Category | PoweroverEthernet |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| Severity | Information       |     |     |     |
Description Dualsignaturepowereddevicepowerdeliveryoninterface.
Event ID: 7910
PoweroverEthernetevents|292

Message

Dual signature powered device fault on interface <interface_name>
pair <pair>. Fault type <fault_type>

Category

Power over Ethernet

Severity

Warning

Description

Dual signature powered device fault on interface. Fault type.

Event ID: 7911

Message

Dual signature powered device mps absent on interface <interface_
name>

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

293

Message Dual signature powered device got class demoted on interface
<interface_name>. Requested_classA <req_class_A> Requested_classB
<req_class_B> Assigned_classA <assigned_class_A> Assigned_classB
<assigned_class_B>
| Category | PoweroverEthernet |     |     |
| -------- | ----------------- | --- | --- |
| Severity | Information       |     |     |
Description Dualsignaturepowereddevicegotclassdemotedoninterface
Event ID: 7916
Message Powered device pre std detect enabled on interface <interface_name>
| Category    | PoweroverEthernet                           |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Severity    | Information                                 |     |     |
| Description | Powereddeviceprestddetectenabledoninterface |     |     |
Event ID: 7917
Message PoE usage exceeded threshold limit of <threshold_limit>
| Category    | PoweroverEthernet              |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | PoEusageexceededthresholdlimit |     |     |
Event ID: 7918
| Message     | PoE controller            | <cntrl_name> | got into fault |
| ----------- | ------------------------- | ------------ | -------------- |
| Category    | PoweroverEthernet         |              |                |
| Severity    | Information               |              |                |
| Description | PoEcontrollergotintofault |              |                |
Event ID: 7919
| Message     | PoE controller        | <cntrl_name> | got reset |
| ----------- | --------------------- | ------------ | --------- |
| Category    | PoweroverEthernet     |              |           |
| Severity    | Information           |              |           |
| Description | PoEcontrollergotreset |              |           |
Event ID: 7920
PoweroverEthernetevents|294

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
<interface_name>.Requested_classA <req_class_A> Requested_classB
<req_class_B> Assigned_classA <assigned_class_A> Assigned_classB
<assigned_class_B>

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
exceeding the max average power of the PD class. Check the PD max
power draw, cabling type and length to improve interoperability

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

295

| Severity    | Information              |     |     |     |
| ----------- | ------------------------ | --- | --- | --- |
| Description | PowereddeviceFETBADfault |     |     |     |
Event ID: 7925
Message Dual signature powered device is drawing power more than its class on
interface <interface_name>, type:<pd_type> classA:<paira_class>
classB:<pairb_class> power:<power>
| Category | PoweroverEthernet |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| Severity | Information       |     |     |     |
Description Dualsignaturepowereddeviceisdrawingpowermorethanitsclass
Event ID: 7926
| Message     | PoE usage                | is below threshold | of <threshold_limit> |     |
| ----------- | ------------------------ | ------------------ | -------------------- | --- |
| Category    | PoweroverEthernet        |                    |                      |     |
| Severity    | Information              |                    |                      |     |
| Description | PoEusageisbelowthreshold |                    |                      |     |
Event ID: 7927
Message Total power drawn: <power_drawn>W by powered device is exceeding the
total available PoE power:<power_available>W. Check the PD max power
|             | draw, cabling                            | type and length | to avoid system | crowbar. |
| ----------- | ---------------------------------------- | --------------- | --------------- | -------- |
| Category    | PoweroverEthernet                        |                 |                 |          |
| Severity    | Warning                                  |                 |                 |          |
| Description | PoEdrawnpowerismorethanavailablePoEpower |                 |                 |          |
Event ID: 7928
Message Powered device invalid signature indication on interface <interface_
name>.
| Category    | PoweroverEthernet                       |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Warning                                 |     |     |     |
| Description | Powereddeviceinvalidsignatureindication |     |     |     |
Event ID: 7929
PoweroverEthernetevents|296

| Message     | PoE hardware                   | access daemon | exiting |     |
| ----------- | ------------------------------ | ------------- | ------- | --- |
| Category    | PoweroverEthernet              |               |         |     |
| Severity    | Information                    |               |         |     |
| Description | PoEhardwareaccessdaemonexiting |               |         |     |
Event ID: 7930
| Message     | POE proto             | daemon exiting |     |     |
| ----------- | --------------------- | -------------- | --- | --- |
| Category    | PoweroverEthernet     |                |     |     |
| Severity    | Information           |                |     |     |
| Description | POEprotodaemonexiting |                |     |     |
Event ID: 7931
Message Always-on PoE detected a powered device on interface <interface_name>
|             | and delivered                                 | power |     |     |
| ----------- | --------------------------------------------- | ----- | --- | --- |
| Category    | PoweroverEthernet                             |       |     |     |
| Severity    | Information                                   |       |     |     |
| Description | Always-onPoEdetectedapowereddeviceoninterface |       |     |     |
Event ID: 7932
Message Powered device disconnected on interface <interface_name> due to LLDP
dot3 disable
| Category | PoweroverEthernet |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| Severity | Information       |     |     |     |
Description PowereddevicedisconnectedoninterfaceduetoLLDPdot3disable
Event ID: 7933
| Message     | Subsystem                   | <subsys_name> | came up with | quick PoE |
| ----------- | --------------------------- | ------------- | ------------ | --------- |
| Category    | PoweroverEthernet           |               |              |           |
| Severity    | Information                 |               |              |           |
| Description | SubsystemcameupwithquickPoE |               |              |           |
Event ID: 7934
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 297

Message

Quick PoE detected a powered device on interface <interface_name> and
delivered power

Category

Power over Ethernet

Severity

Information

Description

Quick PoE detected a powered device on interface

Event ID: 7935

Message

Powered device denied on interface <interface_name> of line module
with Quick PoE enabled. Remove device to avoid crowbar on reboot.

Category

Power over Ethernet

Severity

Warning

Description

Powered device denied on interface of line module with Quick PoE enabled.

Event ID: 7936

Message

Powered device demoted on interface <interface_name> of line module
with Quick PoE enabled. Remove device to avoid crowbar on reboot.

Category

Power over Ethernet

Severity

Warning

Description

Powered device demoted on interface of line module with Quick PoE enabled

Event ID: 7937

Message

PoE disable ignored on interface <interface_name> because Quick PoE
is enabled

Category

Power over Ethernet

Severity

Warning

Description

PoE disable ignored on interface because Quick PoE is enabled

Event ID: 7938

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

Power over Ethernet events | 298

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

Powered device disconnected on interface <interface_name> due to
power-pairs config change

Category

Power over Ethernet

Severity

Information

Description

Powered device disconnected on interface due to power-pairs config change

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

299

Chapter 91
PTP events
PTP events
ThefollowingaretheeventsrelatedtoPTP.
Event ID: 12101
Message PTP <type> <delay_mechanism> <clock_step> clock started with profile
|             | <profile>                           | and transport | <transport>. |
| ----------- | ----------------------------------- | ------------- | ------------ |
| Category    | PTP                                 |               |              |
| Severity    | Information                         |               |              |
| Description | EventreportedwhenPTPclockisstarted. |               |              |
Event ID: 12102
| Message     | PTP clock                           | stopped. Reason: | <reason> |
| ----------- | ----------------------------------- | ---------------- | -------- |
| Category    | PTP                                 |                  |          |
| Severity    | Information                         |                  |          |
| Description | EventreportedwhenPTPclockisstopped. |                  |          |
Event ID: 12103
| Message     | Interface                                    | <name> enabled | for PTP exchange. |
| ----------- | -------------------------------------------- | -------------- | ----------------- |
| Category    | PTP                                          |                |                   |
| Severity    | Information                                  |                |                   |
| Description | EventreportedwhenPTPportisenabledfortxandrx. |                |                   |
Event ID: 12104
Message Interface <name> disabled for PTP exchange. Reason: <reason>
| Category    | PTP                                        |     |     |
| ----------- | ------------------------------------------ | --- | --- |
| Severity    | Information                                |     |     |
| Description | EventreportedwhenPTPenabledportisdisabled. |     |     |
Event ID: 12105
300
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | PTP clock                               | is in <state> | state |     |
| ----------- | --------------------------------------- | ------------- | ----- | --- |
| Category    | PTP                                     |               |       |     |
| Severity    | Information                             |               |       |     |
| Description | EventreportedfordifferentPTPclockstate. |               |       |     |
Event ID: 12106
| Message     | Interface                              | {name} | is in {state} | state{reason} |
| ----------- | -------------------------------------- | ------ | ------------- | ------------- |
| Category    | PTP                                    |        |               |               |
| Severity    | Information                            |        |               |               |
| Description | EventreportedfordifferentPTPportstate. |        |               |               |
Event ID: 12107
Message New GrandSource/Parent is selected: Parent: <parent>, GrandSource:
<grandsource>, Quality: <quality>, Priority1: <priority1>, Priority2:
<priority2>
| Category    | PTP                                           |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Information                                   |     |     |     |
| Description | EventreportedwhenPTPparentisupdated/modified. |     |     |     |
Event ID: 12108
Message PTP operational log_announce_interval is changed to <value> on
|          | interface   | <name> | for profile | <profile> |
| -------- | ----------- | ------ | ----------- | --------- |
| Category | PTP         |        |             |           |
| Severity | Information |        |             |           |
Description EventreportedwhenPTPlogannounceintervalismodified.
Event ID: 12109
Message PTP operational log_min_pdelay_request_interval is changed to <value>
|          | on interface | <name> | for profile | <profile> |
| -------- | ------------ | ------ | ----------- | --------- |
| Category | PTP          |        |             |           |
| Severity | Information  |        |             |           |
Description EventreportedwhenPTPlogminpdelayrequestintervalismodified.
Event ID: 12110
PTPevents|301

Message PTP operational log_min_delay_request_interval is changed to <value>
|          | on interface | <name> | for profile <profile> |
| -------- | ------------ | ------ | --------------------- |
| Category | PTP          |        |                       |
| Severity | Information  |        |                       |
Description EventreportedwhenPTPlogmindelayrequestintervalismodified.
Event ID: 12111
Message PTP operational sync_request_timeout is changed to <value> on
|          | interface   | <name> for | profile <profile> |
| -------- | ----------- | ---------- | ----------------- |
| Category | PTP         |            |                   |
| Severity | Information |            |                   |
Description EventreportedwhenPTPsyncrequesttimeoutismodified.
Event ID: 12112
Message PTP operational sync_interval is changed to <value> on interface
|             | <name>                                      | for profile | <profile> |
| ----------- | ------------------------------------------- | ----------- | --------- |
| Category    | PTP                                         |             |           |
| Severity    | Information                                 |             |           |
| Description | EventreportedwhenPTPsyncintervalismodified. |             |           |
Event ID: 12113
Message PTP operational announce_request_timeout is changed to <value> on
|          | interface   | <name> for | profile <profile> |
| -------- | ----------- | ---------- | ----------------- |
| Category | PTP         |            |                   |
| Severity | Information |            |                   |
Description EventreportedwhenPTPannouncerequesttimeoutismodified.
Event ID: 12114
| Message     | PTP config                                | invalid. | Reason: <reason> |
| ----------- | ----------------------------------------- | -------- | ---------------- |
| Category    | PTP                                       |          |                  |
| Severity    | Information                               |          |                  |
| Description | EventreportedifPTPconfigurationisinvalid. |          |                  |
Event ID: 12115
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 302

| Message     | PTP domain                                       | modified | from | <old> | to <new> | value |
| ----------- | ------------------------------------------------ | -------- | ---- | ----- | -------- | ----- |
| Category    | PTP                                              |          |      |       |          |       |
| Severity    | Information                                      |          |      |       |          |       |
| Description | EventreportedifPTPdomainconfigurationismodified. |          |      |       |          |       |
Event ID: 12116
| Message     | PTP vlan                                       | modified | from | <old> to | <new> | on port <port> |
| ----------- | ---------------------------------------------- | -------- | ---- | -------- | ----- | -------------- |
| Category    | PTP                                            |          |      |          |       |                |
| Severity    | Information                                    |          |      |          |       |                |
| Description | EventreportedifPTPvlanconfigurationismodified. |          |      |          |       |                |
Event ID: 12117
| Message  | PTP source_ip_interface |     |     | <action>. | Port: | <value> |
| -------- | ----------------------- | --- | --- | --------- | ----- | ------- |
| Category | PTP                     |     |     |           |       |         |
| Severity | Information             |     |     |           |       |         |
Description EventreportedifPTPsource_ip_interfaceconfigurationismodified.
Event ID: 12118
| Message     | PTP source_ip                                       | <action>. |     | IP: <value> |     |     |
| ----------- | --------------------------------------------------- | --------- | --- | ----------- | --- | --- |
| Category    | PTP                                                 |           |     |             |     |     |
| Severity    | Information                                         |           |     |             |     |     |
| Description | EventreportedifPTPsource_ipconfigurationismodified. |           |     |             |     |     |
Event ID: 12119
Message
PTPoffsethasreachedbeyondthethreshold{low_limit}<{curr_offset}<{high_limit}
| Category | PTP     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- |
| Severity | Warning |     |     |     |     |     |
Description
EventreportedifPTPoffsetgoesbeyondthethresholdvalue.
Event ID: 12120
Message PTPoffsethasreachedbelowthethreshold{low_limit}<{curr_offset}<{high_limit}
PTPevents|303

| Category    | PTP                                                |     |     |     |
| ----------- | -------------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                            |     |     |     |
| Description | EventreportedifPTPoffsetiswithinthethresholdvalue. |     |     |     |
Event ID: 12121
Message
PTPmaynotworkasexpectedwhenPTPclockisBCandenabledonMCLAG{int_name}-
{lag_name}.
| Category    | PTP                                              |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | Warning                                          |     |     |     |
| Description | EventreportedifPTPclockisBCandPTPenabledonMCLAG. |     |     |     |
| Proxy ARP   | events                                           |     |     |     |
ThefollowingaretheeventsrelatedtoproxyARP.
Event ID: 4205
| Message  | Local proxy | ARP enabled | for port <port> | on vrf <vrf> |
| -------- | ----------- | ----------- | --------------- | ------------ |
| Category | ProxyARP    |             |                 |              |
| Severity | Information |             |                 |              |
Description LogsamessagewhenthefeatureisenabledforaportinsideaVRF
Event ID: 4206
Message Local proxy ARP disabled for port <port> on vrf <vrf>
| Category | ProxyARP    |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description LogsamessagewhenthefeatureisdisabledforaportinsideaVRF
Event ID: 4207
Message Failed to enable local proxy ARP for port <port> on vrf <vrf>
| Category | ProxyARP |     |     |     |
| -------- | -------- | --- | --- | --- |
| Severity | Error    |     |     |     |
Description LogsamessagewhenthefeatureenablefailsforaportinsideaVRF
Event ID: 4208
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 304

Message

Failed to disable local proxy ARP for port <port> on vrf <vrf>

Category

Proxy ARP

Severity

Error

Description

Logs a message when the feature disable fails for a port inside a VRF

Proxy ARP events | 305

|          |          |        |     |          | Chapter  | 92     |
| -------- | -------- | ------ | --- | -------- | -------- | ------ |
|          |          |        |     | QoS ASIC | Provider | events |
| QoS ASIC | Provider | events |     |          |          |        |
ThefollowingaretheeventsrelatedtoqualityofserviceASICprovider.
| Event ID: | 5801 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message QoS failed initial initialization for slot <local_slot>. Error:
<error>
| Category    |      | QoSASICProvider                |     |     |     |     |
| ----------- | ---- | ------------------------------ | --- | --- | --- | --- |
| Severity    |      | Warning                        |     |     |     |     |
| Description |      | QoSinitialinitializationfailed |     |     |     |     |
| Event ID:   | 5802 |                                |     |     |     |     |
Message QoS failed final initialization on new slot <new_slot> for peer slot
<existing_slot>
| Category    |      | QoSASICProvider                        |              |             |     |     |
| ----------- | ---- | -------------------------------------- | ------------ | ----------- | --- | --- |
| Severity    |      | Critical                               |              |             |     |     |
| Description |      | QoSfinalinitializationfailedfornewslot |              |             |     |     |
| Event ID:   | 5803 |                                        |              |             |     |     |
| Message     |      | QoS error after card                   | removal from | slot <slot> |     |     |
| Category    |      | QoSASICProvider                        |              |             |     |     |
| Severity    |      | Error                                  |              |             |     |     |
| Description |      | QoSerroraftercardremoval               |              |             |     |     |
| Event ID:   | 5804 |                                        |              |             |     |     |
Message Error during QoS feature configuration: <error_string>
| Category    |      | QoSASICProvider                             |     |     |     |     |
| ----------- | ---- | ------------------------------------------- | --- | --- | --- | --- |
| Severity    |      | Error                                       |     |     |     |     |
| Description |      | ErrorwhileattemptingQoSfeatureconfiguration |     |     |     |     |
| Event ID:   | 5805 |                                             |     |     |     |     |
306
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Error during QoS HW configuration: <error_string> error <val>

Category

QoS ASIC Provider

Severity

Error

Description

Error while attempting QoS HW configuration

Event ID: 5806

Message

Port: <port_name> PFC priority <pri> using queue <queue> should not
be sharing the queue with other local-priorities

Category

QoS ASIC Provider

Severity

Warning

Description

Warning PFC priority sharing a queue

Event ID: 5807

Message

QoS de-initialization not executed after card removal from slot
{slot}

Category

QoS ASIC Provider

Severity

Error

Description

QoS de-initialization not executed after card removal

QoS ASIC Provider events | 307

Chapter 93
|                    |        |     | Quality | of Service | events |
| ------------------ | ------ | --- | ------- | ---------- | ------ |
| Quality of Service | events |     |         |            |        |
Thefollowingaretheeventsrelatedtoqualityofservice.
Event ID: 5701
Message QoS failed to retrieve default information. Error: <error>
| Category    | QualityofService                        |     |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- | --- |
| Severity    | Information                             |     |     |     |     |
| Description | QoSfailedtoretrievedefaultconfiguration |     |     |     |     |
Event ID: 5702
| Message     | QoS error:       | <error_string> |     |     |     |
| ----------- | ---------------- | -------------- | --- | --- | --- |
| Category    | QualityofService |                |     |     |     |
| Severity    | Error            |                |     |     |     |
| Description | QoSerroroccurred |                |     |     |     |
Event ID: 5703
Message The PFC configuration for interface <ifname> exceeds the system limit
|          | of <limit>       | unique combinations | and was not | applied |     |
| -------- | ---------------- | ------------------- | ----------- | ------- | --- |
| Category | QualityofService |                     |             |         |     |
| Severity | Warning          |                     |             |         |     |
Description Loggedwhentherearemoreuniquecombinationsofflowcontrolledprioritiesthanthe
systemallows.
308
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 94
|           |      | Rapid    | per VLAN      | Spanning | Tree Protocol | events |
| --------- | ---- | -------- | ------------- | -------- | ------------- | ------ |
| Rapid per | VLAN | Spanning | Tree Protocol | events   |               |        |
ThefollowingaretheeventsrelatedtorapidperVLANspanningtreeprotocol.
| Event ID: | 5001 |                                  |     |     |     |     |
| --------- | ---- | -------------------------------- | --- | --- | --- | --- |
| Message   |      | RPVST Enabled                    |     |     |     |     |
| Category  |      | RapidperVLANSpanningTreeProtocol |     |     |     |     |
| Severity  |      | Information                      |     |     |     |     |
Description ThislogeventindicatesthatRPVSThasbeenenabledontheswitch.
| Event ID: | 5002 |                                  |     |     |     |     |
| --------- | ---- | -------------------------------- | --- | --- | --- | --- |
| Message   |      | RPVST Disabled                   |     |     |     |     |
| Category  |      | RapidperVLANSpanningTreeProtocol |     |     |     |     |
| Severity  |      | Information                      |     |     |     |     |
Description ThislogeventindicatesthatRPVSThasbeendisabledontheswitch.
| Event ID: | 5003 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message RPVST - Root changed from <old_priority>: <old_mac> to <new_
|          |     | priority>:                       | <new_mac> | on VLAN <vlan>. |     |     |
| -------- | --- | -------------------------------- | --------- | --------------- | --- | --- |
| Category |     | RapidperVLANSpanningTreeProtocol |           |                 |     |     |
| Severity |     | Information                      |           |                 |     |     |
Description ThislogeventindicatesthatRPVSTrootonaVLANhaschanged
| Event ID: | 5004 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
Message Port <port> disabled - BPDU received on protected port on VLAN
<vlan>.
| Category |     | RapidperVLANSpanningTreeProtocol |     |     |     |     |
| -------- | --- | -------------------------------- | --- | --- | --- | --- |
| Severity |     | Warning                          |     |     |     |     |
Description ThislogeventinformstheuserBPDUreceivedonprotectedport
| Event ID: | 5005 |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- |
309
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message <proto> starved for <pkt_type> on port <port> from <priority_mac> on
VLAN <vlan>.
| Category | RapidperVLANSpanningTreeProtocol |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description ThislogeventinformstheuserthattheRxisstarvedinpaticularport
Event ID: 5006
Message Topology change received on port <port> from source: <mac> on VLAN
<vlan>.
| Category | RapidperVLANSpanningTreeProtocol |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description ThislogeventinformstheuserthattheRPVSTtopologychangeisreceived
Event ID: 5007
Message Topology change generated on port <port> on VLAN <vlan>.
| Category | RapidperVLANSpanningTreeProtocol |     |     |
| -------- | -------------------------------- | --- | --- |
| Severity | Information                      |     |     |
Description ThislogeventinformstheuserthattheRPVSTtopologychangeisgenerated
Event ID: 5008
| Message  | Port <port>                      | blocked | on RPVST <instance> |
| -------- | -------------------------------- | ------- | ------------------- |
| Category | RapidperVLANSpanningTreeProtocol |         |                     |
| Severity | Warning                          |         |                     |
Description Thislogeventinformstheuserthattheportisblockedontheinstance
Event ID: 5009
| Message  | Port <port>                      | unblocked | on RPVST <instance> |
| -------- | -------------------------------- | --------- | ------------------- |
| Category | RapidperVLANSpanningTreeProtocol |           |                     |
| Severity | Warning                          |           |                     |
Description Thislogeventinformstheuserthattheportisunblockedontheinstance
Event ID: 5010
RapidperVLANSpanningTreeProtocolevents|310

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

PVID mismatch detected on <interface> with pvid = <pvid>, Neighbor
pvid = <npvid>' throttle_count: 100

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

Current Virtual Ports <Current_Virtual_Ports> exceeds the max
supported limit <Maximum_Virtual_Ports>

Category

Rapid per VLAN Spanning Tree Protocol

Severity

Information

Description

Log event when the current virtual port count crosses the maximum allowed value

Event ID: 5014

Message

Category

Severity

AUTO RPVST Enabled

Rapid per VLAN Spanning Tree Protocol

Information

Description

RPVST AUTO VLAN is enabled.

Event ID: 5015

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

311

Message

Category

Severity

AUTO RPVST Disabled

Rapid per VLAN Spanning Tree Protocol

Information

Description

RPVST AUTO VLAN is disabled.

Rapid per VLAN Spanning Tree Protocol events | 312

Chapter 95
RBAC events
RBAC events
ThefollowingaretheeventsrelatedtoRBAC.
Event ID: 10301
| Message     | Local authorization                           |     | has been <tac_status>d |
| ----------- | --------------------------------------------- | --- | ---------------------- |
| Category    | RBAC                                          |     |                        |
| Severity    | Information                                   |     |                        |
| Description | Logeventwhenlocaltac_plusserverhasbeenstarted |     |                        |
Event ID: 10302
| Message     | Failed                                       | to <tac_status> | local authorization |
| ----------- | -------------------------------------------- | --------------- | ------------------- |
| Category    | RBAC                                         |                 |                     |
| Severity    | Error                                        |                 |                     |
| Description | Logeventwhenlocaltac_plusserverfailedtostart |                 |                     |
313
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 96
|           |            |        | Redundant | Management | events |
| --------- | ---------- | ------ | --------- | ---------- | ------ |
| Redundant | Management | events |           |            |        |
Thefollowingaretheeventsrelatedtoredundantmanagement.
| Event ID:   | 2201                                           |           |                 |     |     |
| ----------- | ---------------------------------------------- | --------- | --------------- | --- | --- |
| Message     | Failover                                       | detected: | Reason <reason> |     |     |
| Category    | RedundantManagement                            |           |                 |     |     |
| Severity    | Information                                    |           |                 |     |     |
| Description | Thislogeventinformsthatfailovereventisdetected |           |                 |     |     |
| Event ID:   | 2202                                           |           |                 |     |     |
Message Lost <mgmt_module> as Standby Management Module, redundancy disabled
| Category | RedundantManagement |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
| Severity | Information         |     |     |     |     |
Description Thislogeventinformsthatstandbymgmtmodulehasbeenremoved
| Event ID: | 2203 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
Message Detected the removal of the Standby Management Module
| Category | RedundantManagement |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
| Severity | Information         |     |     |     |     |
Description Thislogeventinformsthatstandbymgmtmodulehasbeenremoved
| Event ID: | 2204                |     |        |     |     |
| --------- | ------------------- | --- | ------ | --- | --- |
| Message   | <mgmt_module>       | is  | Active |     |     |
| Category  | RedundantManagement |     |        |     |     |
| Severity  | Information         |     |        |     |     |
Description ThislogeventinformsaboutthestatusofActivemgmtmodule
| Event ID: | 2205 |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
314
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | <mgmt_module>       | is Standby |     |
| -------- | ------------------- | ---------- | --- |
| Category | RedundantManagement |            |     |
| Severity | Information         |            |     |
Description ThislogeventinformsaboutthestatusofStandbymgmtmodule
Event ID: 2206
Message Detected <mgmt_module> as Standby Management Module, redundancy
enabled
| Category | RedundantManagement |     |     |
| -------- | ------------------- | --- | --- |
| Severity | Information         |     |     |
Description Thislogeventinformsthatstandbymgmtmoduleisaddedtothesystem
Event ID: 2207
Message Remote Standby Management module recover detected. Reason: Heartbeat
loss
| Category | RedundantManagement |     |     |
| -------- | ------------------- | --- | --- |
| Severity | Information         |     |     |
Description ThislogeventinformstheuserthatActivemgmtmodulehasdetectedheartbeatloss
Event ID: 2208
| Message     | <mgmt_module>                                      | is waiting | for filesync |
| ----------- | -------------------------------------------------- | ---------- | ------------ |
| Category    | RedundantManagement                                |            |              |
| Severity    | Information                                        |            |              |
| Description | Thislogeventinformstheuserthatfilesyncisinprogress |            |              |
Event ID: 2209
| Message  | <mgmt_module>       | is starting | ISSU operation |
| -------- | ------------------- | ----------- | -------------- |
| Category | RedundantManagement |             |                |
| Severity | Information         |             |                |
Description ThislogeventinformstheuserthatanISSUoperationhasbegun
RedundantManagementevents|315

Chapter 97
|             |         |        |     | Replication |     | Manager | events |
| ----------- | ------- | ------ | --- | ----------- | --- | ------- | ------ |
| Replication | Manager | events |     |             |     |         |        |
Thefollowingaretheeventsrelatedtoreplicationmanager.
| Event ID:   | 2701                                     |              |                |           |           |     |     |
| ----------- | ---------------------------------------- | ------------ | -------------- | --------- | --------- | --- | --- |
| Message     | All                                      | bitmaps have | been allocated |           |           |     |     |
| Category    | ReplicationManager                       |              |                |           |           |     |     |
| Severity    | Warning                                  |              |                |           |           |     |     |
| Description | Logtoindicateallbitmapshavebeenallocated |              |                |           |           |     |     |
| Event ID:   | 2702                                     |              |                |           |           |     |     |
| Message     | Over                                     | 80 percent   | of bitmaps     | have been | allocated |     |     |
| Category    | ReplicationManager                       |              |                |           |           |     |     |
| Severity    | Warning                                  |              |                |           |           |     |     |
Description Logtoindicateover80percentofbitmapshavebeenallocated
| Event ID: | 2705 |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- |
Message Multicast L3 Bridge Control Forwarding entry with uuid <uuid_str> has
|          | no                 | reference | to a VLAN |     |     |     |     |
| -------- | ------------------ | --------- | --------- | --- | --- | --- | --- |
| Category | ReplicationManager |           |           |     |     |     |     |
| Severity | Warning            |           |           |     |     |     |     |
Description LogindicatesMutlicastL3BridgeControlForwardingentrywithuuidhasnoreferenceto
aVLAN
316
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 98

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

Event ID: 4603

Message

Category

Severity

Conflict in authorization configuration. Existing config::URL
(<match>), type(<value>) New config::(<url>), type(<autztype>)

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

317

Message Authorization succeeded for user <user>, for resource <resource>,
|             | with action                                       | <action> |     |
| ----------- | ------------------------------------------------- | -------- | --- |
| Category    | REST                                              |          |     |
| Severity    | Information                                       |          |     |
| Description | logsasuccessfulauthorizationattemptofauserviaREST |          |     |
Event ID: 4608
Message Authorization allowed for user <user>, for resource <resource>, with
action <action>
| Category    | REST                                            |     |     |
| ----------- | ----------------------------------------------- | --- | --- |
| Severity    | Information                                     |     |     |
| Description | logsanallowedauthorizationattemptofauserviaREST |     |     |
Event ID: 4609
Message User <user> added <added_user> with role <added_user_role>
| Category    | REST                             |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | logsasuccessfuladdofauserviaREST |     |     |
Event ID: 4610
| Message     | User <user>                           | deleted <deleted_user> |     |
| ----------- | ------------------------------------- | ---------------------- | --- |
| Category    | REST                                  |                        |     |
| Severity    | Information                           |                        |     |
| Description | logsasuccessfuldeletionofauserviaREST |                        |     |
Event ID: 4611
| Message     | User <user>                                  | successfully | changed password |
| ----------- | -------------------------------------------- | ------------ | ---------------- |
| Category    | REST                                         |              |                  |
| Severity    | Information                                  |              |                  |
| Description | logsasuccessfulpasswordchangeforauserviaREST |              |                  |
Event ID: 4612
RESTevents|318

| Message     | User <user>                                     | password | change failed |
| ----------- | ----------------------------------------------- | -------- | ------------- |
| Category    | REST                                            |          |               |
| Severity    | Warning                                         |          |               |
| Description | logsanunsuccessfulpasswordchangeforauserviaREST |          |               |
Event ID: 4613
Message <user> has written a new switch configuration to <config_name>
| Category    | REST                             |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | logsasuccessconfigwriteoperation |     |     |
Event ID: 4614
Message <user> has copied switch configuration <from_name> to <to_name>
| Category    | REST                    |     |     |
| ----------- | ----------------------- | --- | --- |
| Severity    | Information             |     |     |
| Description | logsasuccesscopyofsaved |     |     |
Event ID: 4615
Message <user> has configured <dns_nameserver> DNS nameserver to <dns>
| Category    | REST                                          |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Information                                   |     |     |
| Description | logsasuccesswhenthenameserveriswrittentoovsdb |     |     |
Event ID: 4616
| Message     | <user> has                                      | deleted all | DNS nameservers |
| ----------- | ----------------------------------------------- | ----------- | --------------- |
| Category    | REST                                            |             |                 |
| Severity    | Information                                     |             |                 |
| Description | logsasuccesswhenthenameserverisdeletedfromovsdb |             |                 |
Event ID: 4617
| Message | <user> created | <uri> |     |
| ------- | -------------- | ----- | --- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 319

| Category    | REST                                            |     |     |
| ----------- | ----------------------------------------------- | --- | --- |
| Severity    | Information                                     |     |     |
| Description | AuserhassuccessfullycreatedanewresourceinOVSDB. |     |     |
Event ID: 4618
| Message     | <user> deleted                               | <uri> |     |
| ----------- | -------------------------------------------- | ----- | --- |
| Category    | REST                                         |       |     |
| Severity    | Information                                  |       |     |
| Description | AuserhassuccessfullydeletedaresourceinOVSDB. |       |     |
Event ID: 4619
| Message     | <user> modified                               | <uri> |     |
| ----------- | --------------------------------------------- | ----- | --- |
| Category    | REST                                          |       |     |
| Severity    | Information                                   |       |     |
| Description | AuserhassuccessfullymodifiedaresourceinOVSDB. |       |     |
Event ID: 4620
| Message     | User: <user>                            | added subscriber: | <subscriber>. |
| ----------- | --------------------------------------- | ----------------- | ------------- |
| Category    | REST                                    |                   |               |
| Severity    | Information                             |                   |               |
| Description | Auserhasaddednewnotificationsubscriber. |                   |               |
Event ID: 4621
| Message     | User: <user>                           | removed subscriber: | <subscriber>. |
| ----------- | -------------------------------------- | ------------------- | ------------- |
| Category    | REST                                   |                     |               |
| Severity    | Information                            |                     |               |
| Description | Auserhasremovednotificationsubscriber. |                     |               |
Event ID: 4622
Message Subscriber: <subscriber> added subscription: <subscription>.
| Category | REST |     |     |
| -------- | ---- | --- | --- |
RESTevents|320

| Severity    | Information                         |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Description | Asubscriberhasaddednewsubscription. |     |     |     |
Event ID: 4623
Message Subscriber: <subscriber> removed subscription: <subscription>.
| Category    | REST                               |     |     |     |
| ----------- | ---------------------------------- | --- | --- | --- |
| Severity    | Information                        |     |     |     |
| Description | Asubscriberhasremovedsubscription. |     |     |     |
Event ID: 4624
Message Unable to add new subscriber. Max number of subscribers has been
reached.
| Category    | REST                                        |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                     |     |     |     |
| Description | Unabletoaddnewsubscriberasmaxnumberreached. |     |     |     |
Event ID: 4625
Message Unable to add new subscription. Max number of subscriptions for
|          | <subscriber> | has been | reached. |     |
| -------- | ------------ | -------- | -------- | --- |
| Category | REST         |          |          |     |
| Severity | Warning      |          |          |     |
Description Unabletoaddnewsubscriptionasmaxnumberreachedforthespecifiedsubscriber.
Event ID: 4626
| Message     | NAE Script                           | <name> has | been created | by user <user>. |
| ----------- | ------------------------------------ | ---------- | ------------ | --------------- |
| Category    | REST                                 |            |              |                 |
| Severity    | Information                          |            |              |                 |
| Description | NAEScripthasbeencreatedsuccessfully. |            |              |                 |
Event ID: 4627
| Message  | NAE Script | <name> has | been deleted | by user <user>. |
| -------- | ---------- | ---------- | ------------ | --------------- |
| Category | REST       |            |              |                 |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 321

| Severity    | Information                          |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Description | NAEScripthasbeendeletedsuccessfully. |     |     |     |
Event ID: 4628
| Message     | NAE Agent                           | <name> has | been created | by user <user>. |
| ----------- | ----------------------------------- | ---------- | ------------ | --------------- |
| Category    | REST                                |            |              |                 |
| Severity    | Information                         |            |              |                 |
| Description | NAEAgenthasbeencreatedsuccessfully. |            |              |                 |
Event ID: 4629
| Message     | NAE Agent                           | <name> has | been updated | by user <user>. |
| ----------- | ----------------------------------- | ---------- | ------------ | --------------- |
| Category    | REST                                |            |              |                 |
| Severity    | Information                         |            |              |                 |
| Description | NAEAgenthasbeenupdatedsuccessfully. |            |              |                 |
Event ID: 4630
| Message     | NAE Agent                           | <name> has | been deleted | by user <user>. |
| ----------- | ----------------------------------- | ---------- | ------------ | --------------- |
| Category    | REST                                |            |              |                 |
| Severity    | Information                         |            |              |                 |
| Description | NAEAgenthasbeendeletedsuccessfully. |            |              |                 |
Event ID: 4631
Message Error rebooting switch, reboot command: <command>, error received:
<error>
| Category    | REST                       |     |     |     |
| ----------- | -------------------------- | --- | --- | --- |
| Severity    | Error                      |     |     |     |
| Description | Logsanerrorifarebootfails. |     |     |     |
Event ID: 4632
Message Connection to Aruba Central on location <central_location> on VRF
<vrf> with Source IP <source_ip> has been successfully established.
| Category | REST |     |     |     |
| -------- | ---- | --- | --- | --- |
RESTevents|322

Severity

Information

Description

Connection is established with Aruba Central.

Event ID: 4633

Message

Connection to Aruba Central on location <central_location> on VRF
<vrf> and Source IP <source_ip> has been closed by Aruba Central.
Requesting new Aruba Central location from CLI/DHCP/Activate.

Category

REST

Severity

Information

Description

Connection to Aruba Central has been closed by Aruba Central. Request to get new
location from CLI/DHCP/Activate.

Event ID: 4634

Message

Connection to Aruba Central on location <central_location> on VRF
<vrf> and Source IP <source_ip> has been closed by Aruba Central.
Trying to reconnect.

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

323

Message Internal error. Closing connection to Aruba Central on location
|             | <central_location>                             |     | on VRF <vrf> | with Source | IP <source_ip>. |
| ----------- | ---------------------------------------------- | --- | ------------ | ----------- | --------------- |
| Category    | REST                                           |     |              |             |                 |
| Severity    | Error                                          |     |              |             |                 |
| Description | Internalerror.ClosingconnectiontoArubaCentral. |     |              |             |                 |
Event ID: 4638
Message Waiting for Aruba Central location from CLI/DHCP/Aruba Activate
Server.
| Category | REST        |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
| Severity | Information |     |     |     |     |
Description WaitingforArubaCentrallocationfromCentralSource(CLI/DHCP/ArubaActivateServer).
Event ID: 4639
Message Connecting to Aruba Central on location <central_location> on VRF
|             | <vrf> with                | Source | IP <source_ip>. |     |     |
| ----------- | ------------------------- | ------ | --------------- | --- | --- |
| Category    | REST                      |        |                 |     |     |
| Severity    | Information               |        |                 |     |     |
| Description | ConnectingtoArubaCentral. |        |                 |     |     |
Event ID: 4640
Message Failed to connect to Aruba Central on location <central_location> on
|             | VRF <vrf>                      | with Source | IP <source_ip> |     |     |
| ----------- | ------------------------------ | ----------- | -------------- | --- | --- |
| Category    | REST                           |             |                |     |     |
| Severity    | Error                          |             |                |     |     |
| Description | FailedtoconnecttoArubaCentral. |             |                |     |     |
Event ID: 4641
| Message     | Aruba Central                     | is disabled. |     |     |     |
| ----------- | --------------------------------- | ------------ | --- | --- | --- |
| Category    | REST                              |              |     |     |     |
| Severity    | Information                       |              |     |     |     |
| Description | TheArubaCentralfeatureisdisabled. |              |     |     |     |
Event ID: 4642
RESTevents|324

Message Aruba Central is disabled. Closing connection to Aruba Central on
location <central_location> on VRF <vrf> with Source IP <source_ip>
| Category    | REST                              |     |     |
| ----------- | --------------------------------- | --- | --- |
| Severity    | Information                       |     |     |
| Description | TheArubaCentralfeatureisdisabled. |     |     |
Event ID: 4643
| Message     | Aruba Central                    | is enabled. |     |
| ----------- | -------------------------------- | ----------- | --- |
| Category    | REST                             |             |     |
| Severity    | Information                      |             |     |
| Description | TheArubaCentralfeatureisenabled. |             |     |
Event ID: 4645
Message Aruba Activate server <activate_address> is reachable via VRF <vrf>.
| Category    | REST                                          |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Information                                   |     |     |
| Description | ArubaActivateserverisreachableviaanactiveVRF. |     |     |
Event ID: 4646
Message Aruba Activate server <activate_address> is not reachable through any
|          | supported   | VRF. |     |
| -------- | ----------- | ---- | --- |
| Category | REST        |      |     |
| Severity | Information |      |     |
Description ArubaActivateserverisnotreachablethroughanysupportedVRF.
Event ID: 4647
| Message     | Switch time                       | is synced | with NTP Servers. |
| ----------- | --------------------------------- | --------- | ----------------- |
| Category    | REST                              |           |                   |
| Severity    | Information                       |           |                   |
| Description | SwitchtimeissyncedwithNTPServers. |           |                   |
Event ID: 4648
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 325

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

Event ID: 4652

Message

Aruba Central connected, any config change through rest <rest_
operation> operation may not be persistent. If central reapplies the
config, change can be overwritten

Category

REST

Severity

Warning

REST events | 326

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

327

Event ID: 4658
Message REST session from <identity> with User <user_name> is rejected
|          | because maximum | session | limit is reached |
| -------- | --------------- | ------- | ---------------- |
| Category | REST            |         |                  |
| Severity | Warning         |         |                  |
Description Logsamessagewhenausertriestologinwhilemaximumnumberofsessionsare
reached
Event ID: 4659
Message {user_agent} session from {identity} with User {user_name} timed out
|          | due to idle | timeout |     |
| -------- | ----------- | ------- | --- |
| Category | REST        |         |     |
| Severity | Information |         |     |
Description LogsamessagewhenaRESTsessiontimedoutduetothesessionbeingidle
Event ID: 4660
| Message     | REST server                                  | is enabled | on VRF <vrf_name> |
| ----------- | -------------------------------------------- | ---------- | ----------------- |
| Category    | REST                                         |            |                   |
| Severity    | Information                                  |            |                   |
| Description | LogsamessagewhentheRESTserverisenabledonaVRF |            |                   |
Event ID: 4661
| Message     | REST server                                   | is disabled | on VRF <vrf_name> |
| ----------- | --------------------------------------------- | ----------- | ----------------- |
| Category    | REST                                          |             |                   |
| Severity    | Information                                   |             |                   |
| Description | LogsamessagewhentheRESTserverisdisabledonaVRF |             |                   |
Event ID: 4662
Message User{user_name}loginfrom{ip_address}forRESTsessionhasfailedsincetheuseris
tryingtologinthroughaninterfacewhichisnotallowed.Allowedinterfacesare:{mgmt_
intf}
| Category | REST  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description Logsamessagewhenauserloginfailssincetheaccessthroughthismanagement
interfaceisnotallowed.
RESTevents|328

Chapter 99
Self Test events
Self Test events
Thefollowingaretheeventsrelatedtoselftest.
Event ID: 4501
| Message     | Selftest has                                 | started | on subsystem | <subsystem> |
| ----------- | -------------------------------------------- | ------- | ------------ | ----------- |
| Category    | SelfTest                                     |         |              |             |
| Severity    | Information                                  |         |              |             |
| Description | logsthestartofselftestonaparticularsubsystem |         |              |             |
Event ID: 4502
| Message     | Selftest has                                      | completed | on subsystem | <subsystem> |
| ----------- | ------------------------------------------------- | --------- | ------------ | ----------- |
| Category    | SelfTest                                          |           |              |             |
| Severity    | Information                                       |           |              |             |
| Description | logsthecompletionofselftestonaparticularsubsystem |           |              |             |
Event ID: 4503
Message Selftest has failed on subsystem <subsystem> with error code
|             | <value>':                                    | yes |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- |
| Category    | SelfTest                                     |     |     |     |
| Severity    | Error                                        |     |     |     |
| Description | logstheselftestfailureofaparticularsubsystem |     |     |     |
Event ID: 4504
Message Selftest has failed on <stack>/<slot>/<interface> with error code
|             | <value>':                                   | yes |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Category    | SelfTest                                    |     |     |     |
| Severity    | Error                                       |     |     |     |
| Description | logstheportselftestfailureonagivensubsystem |     |     |     |
329
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 100
sFlow events
sFlow events
ThefollowingaretheeventsrelatedtosFlow.
Event ID: 1001
| Message  | Failed | to <operation> | host sFlow | agent: <error> |
| -------- | ------ | -------------- | ---------- | -------------- |
| Category | sFlow  |                |            |                |
| Severity | Error  |                |            |                |
Description Logafailurewhentryingtostart/stop/restarthostsFlowdaemon.
Event ID: 1002
Message Failed to <operation> host sFlow configuration file <file>: <error>
| Category | sFlow |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description Logafailurewhentryingtoread/writetohostsFlowconfigurationfile.
Event ID: 1003
Message Failed to <operation> sFlow configuration from bridge <bridge>:
<error>
| Category    | sFlow                                          |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Error                                          |     |     |     |
| Description | LogafailurewhentryingtoconfiguresFlowonSIMOVS. |     |     |     |
Event ID: 1004
| Message  | Failed | to delete all | iptable rules: | <error> |
| -------- | ------ | ------------- | -------------- | ------- |
| Category | sFlow  |               |                |         |
| Severity | Error  |               |                |         |
Description LogafailurewhentryingtodeletealliptablerulesaddedforsFlow.
Event ID: 1005
330
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Failed to <operation> <chain> iptable rules for <port>: <error>
| Category | sFlow |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
| Severity | Error |     |     |     |     |
Description Logafailurewhentryingtoadd/deleteaniptableruleforsFlow.
Event ID: 1006
| Message     | sFlow initialization                   |     | failed. |     |     |
| ----------- | -------------------------------------- | --- | ------- | --- | --- |
| Category    | sFlow                                  |     |         |     |     |
| Severity    | Error                                  |     |         |     |     |
| Description | LogsanerrorifsFlowinitializationfails. |     |         |     |     |
Event ID: 1007
| Message     | Invalid                                       | packet sent | by ASIC in | sFlow callback. |     |
| ----------- | --------------------------------------------- | ----------- | ---------- | --------------- | --- |
| Category    | sFlow                                         |             |            |                 |     |
| Severity    | Error                                         |             |            |                 |     |
| Description | LogsanerrorforaninvalidpacketinsFlowcallback. |             |            |                 |     |
Event ID: 1008
| Message     | Unable                                           | to get netdev | for interface | <interface> |     |
| ----------- | ------------------------------------------------ | ------------- | ------------- | ----------- | --- |
| Category    | sFlow                                            |               |               |             |     |
| Severity    | Error                                            |               |               |             |     |
| Description | Logsanerrorifaninterfacedoesnothaveanetdevclass. |               |               |             |     |
Event ID: 1009
| Message     | Failed                                            | to create KNET | filter | as description | is blank |
| ----------- | ------------------------------------------------- | -------------- | ------ | -------------- | -------- |
| Category    | sFlow                                             |                |        |                |          |
| Severity    | Error                                             |                |        |                |          |
| Description | Logsanerrorifthedescrptiontocreateafilterisblank. |                |        |                |          |
Event ID: 1010
| Message | Failed | to create KNET | filter | for: <desc> |     |
| ------- | ------ | -------------- | ------ | ----------- | --- |
sFlowevents|331

| Category    | sFlow                                      |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Severity    | Error                                      |     |     |     |
| Description | LogsanerrorifsFlowKNETfiltercreationfails. |     |     |     |
Event ID: 1011
| Message     | The received                      | sampled | packet | is null |
| ----------- | --------------------------------- | ------- | ------ | ------- |
| Category    | sFlow                             |         |        |         |
| Severity    | Error                             |         |        |         |
| Description | Logsanerrorifsampledpacketisnull. |         |        |         |
Event ID: 1012
| Message     | The sFlow                                | agent is | not initialized |     |
| ----------- | ---------------------------------------- | -------- | --------------- | --- |
| Category    | sFlow                                    |          |                 |     |
| Severity    | Error                                    |          |                 |     |
| Description | LogsanerrorifsFlowagentisnotinitialized. |          |                 |     |
Event ID: 1013
| Message     | The sFlow                                  | sampler | is not | initialized |
| ----------- | ------------------------------------------ | ------- | ------ | ----------- |
| Category    | sFlow                                      |         |        |             |
| Severity    | Error                                      |         |        |             |
| Description | LogsanerrorifsFlowsamplerisnotinitialized. |         |        |             |
Event ID: 1014
Message Cannot enable/disable sFlow on an invalid port: <port>
| Category | sFlow |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description LogsanerrorifsFlowisenabled/disabledonaninvalidport.
Event ID: 1015
| Message  | sFlow sampler | is not | available | on port: <port> |
| -------- | ------------- | ------ | --------- | --------------- |
| Category | sFlow         |        |           |                 |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 332

| Severity    | Error                                      |     |     |     |
| ----------- | ------------------------------------------ | --- | --- | --- |
| Description | LogsanerrorifsFlowsamplerismissingonaport. |     |     |     |
Event ID: 1016
| Message     | sFlow receiver                            | is not | available |     |
| ----------- | ----------------------------------------- | ------ | --------- | --- |
| Category    | sFlow                                     |        |           |     |
| Severity    | Error                                     |        |           |     |
| Description | LogsanerrorifsFlowreceiverisnotavailable. |        |           |     |
Event ID: 1017
| Message     | Failed                                        | to retrieve port | configuration: | <error> |
| ----------- | --------------------------------------------- | ---------------- | -------------- | ------- |
| Category    | sFlow                                         |                  |                |         |
| Severity    | Error                                         |                  |                |         |
| Description | Logsanerrorifportconfigurationisnotavailable. |                  |                |         |
Event ID: 1018
| Message     | Failed                                         | to set sampling | rate on port | <port>: <error> |
| ----------- | ---------------------------------------------- | --------------- | ------------ | --------------- |
| Category    | sFlow                                          |                 |              |                 |
| Severity    | Error                                          |                 |              |                 |
| Description | Logsanerrorifsettingasamplingrateonaportfails. |                 |              |                 |
Event ID: 1019
| Message  | Failed | to get sampling | rate on port | <port>: <error> |
| -------- | ------ | --------------- | ------------ | --------------- |
| Category | sFlow  |                 |              |                 |
| Severity | Error  |                 |              |                 |
Description Logsanerrorifunabletoretrievesamplingrateonaport.
Event ID: 1020
| Message  | Invalid | agent interface | IP address: | <ip_address> |
| -------- | ------- | --------------- | ----------- | ------------ |
| Category | sFlow   |                 |             |              |
| Severity | Error   |                 |             |              |
Description LogsanerrorincaseofinvalidagentinterfaceIPaddressconfiguration.
sFlowevents|333

Event ID: 1021
| Message  | Invalid collector | IP address: | <ip_address> |
| -------- | ----------------- | ----------- | ------------ |
| Category | sFlow             |             |              |
| Severity | Error             |             |              |
Description LogsanerrorincaseofinvalidcollectorIPaddressconfiguration.
Event ID: 1022
Message Failed to get interface statistics for unit <unit> port <port>:
<error>
| Category    | sFlow                                             |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Error                                             |     |     |
| Description | Logsanerrorifunabletoretrieveinterfacestatistics. |     |     |
Event ID: 1023
| Message     | sFlow agent               | created. |     |
| ----------- | ------------------------- | -------- | --- |
| Category    | sFlow                     |          |     |
| Severity    | Information               |          |     |
| Description | LogscreationofsFlowagent. |          |     |
Event ID: 1024
| Message     | sFlow agent               | deleted. |     |
| ----------- | ------------------------- | -------- | --- |
| Category    | sFlow                     |          |     |
| Severity    | Information               |          |     |
| Description | LogsdeletionofsFlowagent. |          |     |
Event ID: 1025
Message Changed sFlow sampling rate from <old_rate> to <new_rate>.
| Category    | sFlow                           |     |     |
| ----------- | ------------------------------- | --- | --- |
| Severity    | Information                     |     |     |
| Description | LogsachangeinsFlowsamplingrate. |     |     |
Event ID: 1026
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 334

| Message     | Set sFlow                         | agents | header len | to <hdrlen>. |
| ----------- | --------------------------------- | ------ | ---------- | ------------ |
| Category    | sFlow                             |        |            |              |
| Severity    | Information                       |        |            |              |
| Description | LogssFlowagentsheaderlengthevent. |        |            |              |
Event ID: 1027
| Message     | Set sFlow                         | agents | IP to <ip_addr>. |     |
| ----------- | --------------------------------- | ------ | ---------------- | --- |
| Category    | sFlow                             |        |                  |     |
| Severity    | Information                       |        |                  |     |
| Description | LogssettingIPaddresstosFlowagent. |        |                  |     |
Event ID: 1028
| Message     | Set max                                | datagram | size on sFlow | agent to <dgramsize>. |
| ----------- | -------------------------------------- | -------- | ------------- | --------------------- |
| Category    | sFlow                                  |          |               |                       |
| Severity    | Information                            |          |               |                       |
| Description | LogsettingmaxdatagramsizeonsFlowagent. |          |               |                       |
Event ID: 1029
Message Add sFlow poller on <port_name> with ifIndex <ifIndex> at interval
<intvl>.
| Category    | sFlow                  |     |     |     |
| ----------- | ---------------------- | --- | --- | --- |
| Severity    | Information            |     |     |     |
| Description | AddsFlowpolleronaport. |     |     |     |
Event ID: 1030
| Message     | Remove                    | sFlow poller | on <ifIndex>. |     |
| ----------- | ------------------------- | ------------ | ------------- | --- |
| Category    | sFlow                     |              |               |     |
| Severity    | Information               |              |               |     |
| Description | DeletesFlowpolleronaport. |              |               |     |
Event ID: 1031
sFlowevents|335

| Message     | Set polling                      | interval | of <intvl> | on sFlow agent. |
| ----------- | -------------------------------- | -------- | ---------- | --------------- |
| Category    | sFlow                            |          |            |                 |
| Severity    | Information                      |          |            |                 |
| Description | SetpollingintervalforsFlowagent. |          |            |                 |
Event ID: 1032
| Message     | sFlow sampling         | mode set | to <mode>. |     |
| ----------- | ---------------------- | -------- | ---------- | --- |
| Category    | sFlow                  |          |            |     |
| Severity    | Information            |          |            |     |
| Description | LogschangeinsFlowmode. |          |            |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 336

Chapter 101
SFTP Client events
| SFTP Client events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoSFTPclient.
Event ID: 5301
| Message     | SFTP file                 | transfer from | <from> | to <to> completed. |
| ----------- | ------------------------- | ------------- | ------ | ------------------ |
| Category    | SFTPClient                |               |        |                    |
| Severity    | Information               |               |        |                    |
| Description | SFTPfiletransfercompleted |               |        |                    |
Event ID: 5302
Message SFTP file transfer from <from> to <to> failed - <status>.
| Category    | SFTPClient             |     |     |     |
| ----------- | ---------------------- | --- | --- | --- |
| Severity    | Information            |     |     |     |
| Description | SFTPfiletransferfailed |     |     |     |
337
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 102

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

338

Chapter 103
SNMP events
SNMP events
ThefollowingaretheeventsrelatedtoSNMP.
Event ID: 7101
| Message     | Snmp agent          | is up and | running | in namespace |     | <vrf> |
| ----------- | ------------------- | --------- | ------- | ------------ | --- | ----- |
| Category    | SNMP                |           |         |              |     |       |
| Severity    | Information         |           |         |              |     |       |
| Description | SNMPagentisenabled. |           |         |              |     |       |
Event ID: 7102
| Message     | Snmp sub               | agent is | up and | running | in namespace | <vrf> |
| ----------- | ---------------------- | -------- | ------ | ------- | ------------ | ----- |
| Category    | SNMP                   |          |        |         |              |       |
| Severity    | Information            |          |        |         |              |       |
| Description | SNMPsubagentisenabled. |          |        |         |              |       |
Event ID: 7103
| Message     | Snmp agent           | is disabled | for | namespace | <vrf> |     |
| ----------- | -------------------- | ----------- | --- | --------- | ----- | --- |
| Category    | SNMP                 |             |     |           |       |     |
| Severity    | Information          |             |     |           |       |     |
| Description | SNMPagentisdisabled. |             |     |           |       |     |
Event ID: 7104
| Message     | Snmp sub                | agent is | disabled | for namespace |     | <vrf> |
| ----------- | ----------------------- | -------- | -------- | ------------- | --- | ----- |
| Category    | SNMP                    |          |          |               |     |       |
| Severity    | Information             |          |          |               |     |       |
| Description | SNMPsubagentisdisabled. |          |          |               |     |       |
Event ID: 7105
339
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Failed                        | to poll snmp |     |     |     |
| ----------- | ----------------------------- | ------------ | --- | --- | --- |
| Category    | SNMP                          |              |     |     |     |
| Severity    | Information                   |              |     |     |     |
| Description | SNMPpollthreadcreationfailed. |              |     |     |     |
Event ID: 7106
| Message     | Snmp and                                     | credential | manager | integration | failed |
| ----------- | -------------------------------------------- | ---------- | ------- | ----------- | ------ |
| Category    | SNMP                                         |            |         |             |        |
| Severity    | Information                                  |            |         |             |        |
| Description | SNMPfailedtosynchronizewithcredentialmanager |            |         |             |        |
Event ID: 7107
| Message     | Snmp system             | now configured |     |     |     |
| ----------- | ----------------------- | -------------- | --- | --- | --- |
| Category    | SNMP                    |                |     |     |     |
| Severity    | Information             |                |     |     |     |
| Description | SNMPsystemisconfigured. |                |     |     |     |
Event ID: 7108
| Message     | Snmp and                                 | database | Integration | has been | initialized |
| ----------- | ---------------------------------------- | -------- | ----------- | -------- | ----------- |
| Category    | SNMP                                     |          |             |          |             |
| Severity    | Information                              |          |             |          |             |
| Description | Snmpsuccessfullysynchronizedwithdatabase |          |             |          |             |
Event ID: 7109
| Message     | Successfully                        | initialized | all | SNMP plugins |     |
| ----------- | ----------------------------------- | ----------- | --- | ------------ | --- |
| Category    | SNMP                                |             |     |              |     |
| Severity    | Information                         |             |     |              |     |
| Description | SNMPpluginssuccessfullyinitialized. |             |     |              |     |
Event ID: 7110
| Message | Destroyed | all SNMP | plugins |     |     |
| ------- | --------- | -------- | ------- | --- | --- |
SNMPevents|340

| Category    | SNMP                                 |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Information                          |     |     |     |
| Description | SNMPpluginsuccessfullydeinitialized. |     |     |     |
Event ID: 7111
| Message     | SNMP cache           | sync on-demand | is set to: | <truth_value> |
| ----------- | -------------------- | -------------- | ---------- | ------------- |
| Category    | SNMP                 |                |            |               |
| Severity    | Information          |                |            |               |
| Description | SNMPondemandidlsync. |                |            |               |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 341

Chapter 104

SSH client events

SSH client events

The following are the events related to SSH client.

Event ID: 9001

Message

Connection to SSH server <ipaddr> on VRF <vrf_name> is established
for user <username> over port <port_num>

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

342

Chapter 105
SSH server events
| SSH server events |     |     |     |
| ----------------- | --- | --- | --- |
ThefollowingaretheeventsrelatedtoSSHserver.
Event ID: 5201
| Message     | SSH host-key                            | <key_name> | is installed. |
| ----------- | --------------------------------------- | ---------- | ------------- |
| Category    | SSHserver                               |            |               |
| Severity    | Information                             |            |               |
| Description | LogsamessagewhentheSSHhost-keygenerated |            |               |
Event ID: 5202
| Message     | SSH server                                  | is enabled | on VRF <vrf_name>. |
| ----------- | ------------------------------------------- | ---------- | ------------------ |
| Category    | SSHserver                                   |            |                    |
| Severity    | Information                                 |            |                    |
| Description | LogsamessagewhentheSSHserverisenabledonaVRF |            |                    |
Event ID: 5203
| Message     | SSH server                                   | is disabled | on VRF <vrf_name>. |
| ----------- | -------------------------------------------- | ----------- | ------------------ |
| Category    | SSHserver                                    |             |                    |
| Severity    | Information                                  |             |                    |
| Description | LogsamessagewhentheSSHserverisdisabledonaVRF |             |                    |
Event ID: 5204
Message SSH client-public-key <key_name> was installed for the user
<username>.
| Category | SSHserver   |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logsamessagewhenaddsshclient-public-keyintoauthorized_keysfile
Event ID: 5205
343
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

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

User {user_name} login from {ip_address} for SSH session failed
during password based authentication.

Category

SSH server

Severity

Error

Description

Logs a message when a user login fails

Event ID: 5211

SSH server events | 344

Message

User <user_name> logged out of SSH session from <ip_address>.

Category

SSH server

Severity

Information

Description

Logs a message when a user logs out of a session

Event ID: 5212

Message

SSH session from <ip_address> is rejected because maximum number of
SSH sessions is reached.

Category

SSH server

Severity

Warning

Description

Logs a message when a user tries to login while maximum number of sessions are
reached.

Event ID: 5213

Message

SSH session from user {user_name} closed because maximum number of
sessions per user is reached.

Category

SSH server

Severity

Warning

Description

Logs a message when a user session is closed while maximum number of sessions per
user are reached.

Event ID: 5214

Message

SSH session from {ip_address} denied due to host key verification
failure.

Category

SSH server

Severity

Warning

Description

Logs a message when a user session is closed due to host key failure.

Event ID: 5215

Message

SSH session from {ip_address} for user {user_name} denied. The allowed user

management interfaces are: {mgmt_intf

Category

SSH server

Severity

Error

Description

Logs a message when a user login fails since the access through this management

interface is not allowed

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

345

Event ID: 5216

Message

SSH session from {ip_address} for user {user_name} rejected due to failed public key

validation

Category

SSH server

Severity

Error

Description

Logs a message when a user login fails due to public key failure

Event ID: 5217

Message

SSH server on VRF {vrf_name} is in an error state.

Category

SSH server

Severity

Error

Description

Logs a message when SSH server goes into an error state.

Event ID: 5218

Message

Converting configured SSH server allow-list entry {original_ip} to CIDR format ({new_ip})

Category

SSH server

Severity

Information

Description

Logs a message when SSH server converts an IP address to CIDR format.

Event ID: 5219

Message

Failed to convert configured SSH server allow-list entry {original_ip} to CIDR format, using

original address as-is

Category

SSH server

Severity

Error

Description

Logs a message when SSH server fails to convert an IP address to CIDR format.

Event ID: 5220

Message

RADIUS authorize-only request failed for SSH session from {ip_address} for user {user_

name}.

Category

SSH server

Severity

Error

Description

Logs a message when SSH connection fails due to authorize-only attempt.

SSH server events | 346

Event ID: 5221

Message

SSH session from {ip_address} denied because username {user_name} not found in

authenticating certificate Common Name or User Principal Name fields.

Category

SSH server

Severity

Error

Description

Logs a message when the authenticating username was searched for and not found in

the authenticating certificate.

Event ID: 5222

Message

SSH session from {ip_address} for user {user_name} denied by SSH server allow-list

Category

SSH server

Severity

Error

Description

Logs a message when the authenticating IP is denied due to the SSH server allow list.

Event ID: 5223

Message

Logs a message when an empty SSH allow-list has been enabled.

Category

SSH server

Severity

Warning

Description

An empty SSH allow-list has been enabled and all new SSH connections will be denie

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

347

Chapter 106
Supportability events
| Supportability | events |     |     |
| -------------- | ------ | --- | --- |
Thefollowingaretheeventsrelatedtosupportability.
Event ID: 1201
| Message     | <process>                             | crashed due | to <signal>,<timestamp> |
| ----------- | ------------------------------------- | ----------- | ----------------------- |
| Category    | Supportability                        |             |                         |
| Severity    | Critical                              |             |                         |
| Description | Adaemonhascrashedandgeneratedcoredump |             |                         |
Event ID: 1202
| Message     | Kernel          | panic occurred |     |
| ----------- | --------------- | -------------- | --- |
| Category    | Supportability  |                |     |
| Severity    | Error           |                |     |
| Description | Logskernelcrash |                |     |
Event ID: 1203
Message Kernel failed to compress vmcore. Error log:<err_desc>
| Category    | Supportability                   |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Error                            |     |     |
| Description | Logskernelfailedtocompressvmcore |     |     |
Event ID: 1204
Message Kernel panic occurred and secondary kernel failed to save
|          | uncompressed   | core. | Error log:<err_desc> |
| -------- | -------------- | ----- | -------------------- |
| Category | Supportability |       |                      |
| Severity | Error          |       |                      |
Description Logskernelpanicoccurredandsecondarykernelcorefailedtosaveuncompressedcore
Event ID: 1205
348
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message Kernel panic occurred and system is restored back to normal state
| Category    |          | Supportability          |     |     |     |
| ----------- | -------- | ----------------------- | --- | --- | --- |
| Severity    |          | Error                   |     |     |     |
| Description |          | Logskernelpanicoccurred |     |     |     |
| Event       | ID: 1206 |                         |     |     |     |
Message Module rebooted. Reason: <reason>, Boot-ID: <boot_id>
| Category    |          | Supportability        |               |         |                 |
| ----------- | -------- | --------------------- | ------------- | ------- | --------------- |
| Severity    |          | Information           |               |         |                 |
| Description |          | Logsrebootinformation |               |         |                 |
| Event       | ID: 1207 |                       |               |         |                 |
| Message     |          | Available             | system memory | is back | to normal state |
| Category    |          | Supportability        |               |         |                 |
| Severity    |          | Warning               |               |         |                 |
Description Eventraisedwhenavailablesystemmemoryisrestoredtonormallevel.
| Event | ID: 1208 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message High system memory usage detected. High memory usage daemons are
<daemons>
| Category |     | Supportability |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Error          |     |     |     |
Description Eventraisedwhensystemmemoryusagegoesbeyondhighthreshold.
| Event    | ID: 1209 (Severity: | Emergency)     |               |               |           |
| -------- | ------------------- | -------------- | ------------- | ------------- | --------- |
| Message  |                     | Available      | system memory | is critically | low': yes |
| Category |                     | Supportability |               |               |           |
| Severity |                     | Emergency      |               |               |           |
Description Eventraisedwhensystemmemoryusagecrossescriticalthreshold.
| Event | ID: 1210 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Supportabilityevents|349

| Message  |     | Memory         | reservation | for reboot | library failed |
| -------- | --- | -------------- | ----------- | ---------- | -------------- |
| Category |     | Supportability |             |            |                |
| Severity |     | Warning        |             |            |                |
Description Eventraisedwhenmemoryreservationforrebootlibraryfails.
| Event       | ID: 1211 (Severity: | Emergency)                                |                |        |              |
| ----------- | ------------------- | ----------------------------------------- | -------------- | ------ | ------------ |
| Message     |                     | Unable                                    | to get current | system | memory usage |
| Category    |                     | Supportability                            |                |        |              |
| Severity    |                     | Emergency                                 |                |        |              |
| Description |                     | Eventraisedwhensystemmemoryreadisfailing. |                |        |              |
| Event       | ID: 1212 (Severity: | Emergency)                                |                |        |              |
Message Available system memory is critically low. Reboot will be triggered
soon.
| Category |     | Supportability |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Emergency      |     |     |     |
Description Availablememoryiscriticallylow,systemwillberebooted.
| Event | ID: 1213 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message RMON alarm <index> - Rising threshold value of <threshold> reached
for <oid>.
| Category |     | Supportability |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Information    |     |     |     |
Description Eventraisedwhenthesampledvaluehasreachedtherisingthreshold.
| Event | ID: 1214 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
Message RMON alarm <index> - Falling threshold value of <threshold> reached
for <oid>.
| Category |     | Supportability |     |     |     |
| -------- | --- | -------------- | --- | --- | --- |
| Severity |     | Information    |     |     |     |
Description Eventraisedwhenthesampledvaluehasreachedthefallingthreshold.
| Event | ID: 1215 |     |     |     |     |
| ----- | -------- | --- | --- | --- | --- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 350

| Message     |                     | <process>                                          | exiting. Reason: | <reason> |
| ----------- | ------------------- | -------------------------------------------------- | ---------------- | -------- |
| Category    |                     | Supportability                                     |                  |          |
| Severity    |                     | Error                                              |                  |          |
| Description |                     | Aprocessisexitingduetoanunrecoverableerror         |                  |          |
| Event       | ID: 1216 (Severity: | Emergency)                                         |                  |          |
| Message     |                     | <process>                                          | exiting. Reason: | <reason> |
| Category    |                     | Supportability                                     |                  |          |
| Severity    |                     | Emergency                                          |                  |          |
| Description |                     | Acriticalprocessisexitingduetoanunrecoverableerror |                  |          |
| Event       | ID: 1217            |                                                    |                  |          |
| Message     |                     | Coredump(s)                                        | are deleted      | by user  |
| Category    |                     | Supportability                                     |                  |          |
| Severity    |                     | Information                                        |                  |          |
| Description |                     | Coredump(s)aredeletedbyuser                        |                  |          |
| Event       | ID: 1218            |                                                    |                  |          |
Message Remote logging to <remote_host> over <vrf> vrf added.
| Category |     | Supportability |     |     |
| -------- | --- | -------------- | --- | --- |
| Severity |     | Information    |     |     |
Description Eventraisedwhenanewsyslogserverisaddedforremotelogging.
| Event | ID: 1219 |     |     |     |
| ----- | -------- | --- | --- | --- |
Message Remote logging to <remote_host> over <vrf> vrf removed.
| Category |     | Supportability |     |     |
| -------- | --- | -------------- | --- | --- |
| Severity |     | Information    |     |     |
Description Eventraisedwhenasyslogserverisremovedfromremotelogging.
| Event | ID: 1220 |     |     |     |
| ----- | -------- | --- | --- | --- |
Message Configuration of remote logging to <remote_host> over <vrf> vrf
modified.
Supportabilityevents|351

| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Information    |     |     |     |
Description Eventraisedwhenanexistingsyslogserverconfigurationismodified.
Event ID: 1221
Message Watchdog timeout is increased due to high memory usage
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Information    |     |     |     |
Description EventraisedwhenavailableRAMmemorygoesbelowthethresholdandwatchdog
timeoutisincreased.
Event ID: 1222
| Message  | Watchdog timeout | is restored | to default | value |
| -------- | ---------------- | ----------- | ---------- | ----- |
| Category | Supportability   |             |            |       |
| Severity | Information      |             |            |       |
Description EventraisedwhentheavailableRAMmemoryisrestoredtonormalrangeandthe
watchdogtimeoutisrestoredtodefaultvalue.
Event ID: 1223
| Message  | The <log_type> | buffer | is almost full.': | yes |
| -------- | -------------- | ------ | ----------------- | --- |
| Category | Supportability |        |                   |     |
| Severity | Warning        |        |                   |     |
Description Eventraisedthelogbufferisalmostfull.Usercancopytheselogsbeforethelogsbeing
overwritten.
Event ID: 1224
Message The <log_type> buffer has wrapped, older logs will be overwritten.':
yes
| Category | Supportability |     |     |     |
| -------- | -------------- | --- | --- | --- |
| Severity | Warning        |     |     |     |
Description Eventraisedthelogbufferhaswrapped;olderlogswillbeoverwritten.
Event ID: 1225
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 352

Message Collection of support-files named <name> of type <type> is requested
|             | for the module                                      | <module>. |     |
| ----------- | --------------------------------------------------- | --------- | --- |
| Category    | Supportability                                      |           |     |
| Severity    | Information                                         |           |     |
| Description | Eventraisedwhensuppuort-filescollectionisrequested. |           |     |
Event ID: 1226
Message Support-files named <name> is requested for deletion.
| Category | Supportability |     |     |
| -------- | -------------- | --- | --- |
| Severity | Information    |     |     |
Description Eventraisedwhenarequstrecivedtodeletegivensupport-files.
Event ID: 1227
| Message     | Support-files                           | named <name> | is deleted. |
| ----------- | --------------------------------------- | ------------ | ----------- |
| Category    | Supportability                          |              |             |
| Severity    | Information                             |              |             |
| Description | Eventraisedwhensuppuort-filesisdeleted. |              |             |
Event ID: 1228
Message Collection of support-files named <name> failed due to <reason>.
| Category    | Supportability                                |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Error                                         |     |     |
| Description | Eventraisedwhencollectionsupport-filesfailed. |     |     |
Event ID: 1229
Message Deletion of support-files named <name> failed due to <reason>.
| Category    | Supportability                                    |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Error                                             |     |     |
| Description | Eventraisedwhenfailedtodeleteagivensupport-files. |     |     |
Event ID: 1230
Supportabilityevents|353

| Message  | Collection     | of support-files | named <name> | is <state>. |
| -------- | -------------- | ---------------- | ------------ | ----------- |
| Category | Supportability |                  |              |             |
| Severity | Information    |                  |              |             |
Description Eventraisedwhencollectionofsupport-filesstatechanges.
Event ID: 1231
| Message  | Syslog client  | restarted | due to configuration | change. |
| -------- | -------------- | --------- | -------------------- | ------- |
| Category | Supportability |           |                      |         |
| Severity | Information    |           |                      |         |
Description Eventraisedwhenremotesyslogisrestartedduetoconfigurationchange.
Event ID: 1232
| Message     | The security                               | log buffer | is cleared |     |
| ----------- | ------------------------------------------ | ---------- | ---------- | --- |
| Category    | Supportability                             |            |            |     |
| Severity    | Information                                |            |            |     |
| Description | Eventraisedasthesecuritylogbufferiscleared |            |            |     |
Event ID: 1233
| Message     | Starting                              | System Logging | Service. |     |
| ----------- | ------------------------------------- | -------------- | -------- | --- |
| Category    | Supportability                        |                |          |     |
| Severity    | Information                           |                |          |     |
| Description | Eventraisedwhenremotesyslogisstarting |                |          |     |
Event ID: 1234
| Message     | Started                              | System Logging | Service. |     |
| ----------- | ------------------------------------ | -------------- | -------- | --- |
| Category    | Supportability                       |                |          |     |
| Severity    | Information                          |                |          |     |
| Description | Eventraisedwhenremotesyslogisstarted |                |          |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 354

Chapter 107
SYS events
SYS events
ThefollowingaretheeventsrelatedtoSYS.
Event ID: 701
| Message     | Failed                                   | to read FRU | data from base | system |
| ----------- | ---------------------------------------- | ----------- | -------------- | ------ |
| Category    | SYS                                      |             |                |        |
| Severity    | Information                              |             |                |        |
| Description | LogwhenfailedtoreadFRUdatafrombasesystem |             |                |        |
Event ID: 702
| Message     | Failed                       | to read FRU | header |     |
| ----------- | ---------------------------- | ----------- | ------ | --- |
| Category    | SYS                          |             |        |     |
| Severity    | Information                  |             |        |     |
| Description | LogwhenfailedtoreadFRUheader |             |        |     |
Event ID: 703
| Message     | Error reading                | FRU | EEPROM Header |     |
| ----------- | ---------------------------- | --- | ------------- | --- |
| Category    | SYS                          |     |               |     |
| Severity    | Information                  |     |               |     |
| Description | logwhenFRUEEPROMHeaderfailed |     |               |     |
Event ID: 704
| Message     | Failed                          | to intialize | devices |     |
| ----------- | ------------------------------- | ------------ | ------- | --- |
| Category    | SYS                             |              |         |     |
| Severity    | Information                     |              |         |     |
| Description | Logwhenfailedtointializedevices |              |         |     |
Event ID: 705
355
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Failed                        | to allocate memory | for <value> |
| ----------- | ----------------------------- | ------------------ | ----------- |
| Category    | SYS                           |                    |             |
| Severity    | Information                   |                    |             |
| Description | Logwhenfailedtoallocatememory |                    |             |
Event ID: 706
| Message     | Initiating                              | system reboot |     |
| ----------- | --------------------------------------- | ------------- | --- |
| Category    | SYS                                     |               |     |
| Severity    | Information                             |               |     |
| Description | Indicatesthatthechassisisabouttoreboot. |               |     |
Event ID: 707
| Message  | Initiating | chassis thermal | reboot |
| -------- | ---------- | --------------- | ------ |
| Category | SYS        |                 |        |
| Severity | Error      |                 |        |
Description Indicatesthatthechassisexperiencedathermaleventandwillreboot
Event ID: 708
Message Invalid Device Version Programmed. Please check MFG data programmed
on the device.
| Category | SYS   |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description Indicatesinvaliddeviceversionisprogrammedonthedevice
Event ID: 709
| Message  | Failed | to read assembly | revision |
| -------- | ------ | ---------------- | -------- |
| Category | SYS    |                  |          |
| Severity | Error  |                  |          |
Description Indicatesdevicehasfailedtoreadassemblyrevisionthatisprogrammed
Event ID: 710
SYSevents|356

| Message  | The system | has entered | the recovery | console |
| -------- | ---------- | ----------- | ------------ | ------- |
| Category | SYS        |             |              |         |
| Severity | Info       |             |              |         |
Description Indicatesthatthesystemhasenteredtherecoveryconsole
Event ID: 711
Message Detected DDR errors during uboot BIST, module {module} reported
{error_sbe}
| Category | SYS  |     |     |     |
| -------- | ---- | --- | --- | --- |
| Severity | Info |     |     |     |
Description ndicatesthatthesystemhasdetectedDDRerrorsduringubootBIST
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 357

Chapter 108

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

Event ID: 6302

Message

Failed to read system memory usage for module <module_num>

Category

Severity

SYSMON

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

Event ID: 6304

Message

Category

Severity

Storage utilization for <partition_name> partition is at
<utilization>% in module <module_name>': yes

SYSMON

Warning

Description

Warns a user when the storage utilization has exceeded the warning limit.

Event ID: 6305

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

358

Message

Storage <partition_name> partition high utilization alert.
Utilization is at <utilization>% in module <module_name>': yes

Category

SYSMON

Severity

Error

Description

Raises high storage utilization alert when the utilization crosses higher utilization limit.

Event ID: 6306

Message

Category

Severity

Excessive write to <partition_name> partition in module <module_name>
observed. <mem_usage>GB written over past <unit_count> <unit>': yes

SYSMON

Warning

Description

Warns a user when higher write to the storage observed

Event ID: 6307

Message

Category

Severity

Excessive write to swap in module <module_name> observed. <mem_
usage>GB written over past <unit_count> <unit>': yes

SYSMON

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

Excessive write to swap in module <module_name> observed. <mem_
usage>GB written over past <unit_count> <unit>': yes

Category

SYSMON

Severity

Error

Description

Warns a user when excessive write to the swap observed.

SYSMON events | 359

Chapter 109
TCAM events
TCAM events
ThefollowingaretheeventsrelatedtoTCAM.
Event ID: 10201
| Message     | "Policer installation      | has | failed" |     |
| ----------- | -------------------------- | --- | ------- | --- |
| Category    | TCAM                       |     |         |     |
| Severity    | Error                      |     |         |     |
| Description | Policerinstallationfailure |     |         |     |
Event ID: 10202
Message "TCAM entry installation has failed in table <table_name>"
| Category    | TCAM                         |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- |
| Severity    | Error                        |     |     |     |
| Description | TCAMentryinstallationfailure |     |     |     |
Event ID: 10203
| Message     | "Installation                | of TCAM table | <table_name> | has failed" |
| ----------- | ---------------------------- | ------------- | ------------ | ----------- |
| Category    | TCAM                         |               |              |             |
| Severity    | Error                        |               |              |             |
| Description | TCAMtableinstallationfailure |               |              |             |
Event ID: 10204
Message "High-capacity TCAM/LPM entry installation failed in table <table_
name>"
| Category    | TCAM                                          |     |     |     |
| ----------- | --------------------------------------------- | --- | --- | --- |
| Severity    | Error                                         |     |     |     |
| Description | High-capacityTCAM/LPMentryinstallationfailure |     |     |     |
Event ID: 10205
360
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message "High-capacity TCAM/LPM table <table_name> installation failed"
| Category    | TCAM                                          |     |     |
| ----------- | --------------------------------------------- | --- | --- |
| Severity    | Error                                         |     |     |
| Description | High-capacityTCAM/LPMtableinstallationfailure |     |     |
Event ID: 10206
| Message     | "Counter installation          | has | failed" |
| ----------- | ------------------------------ | --- | ------- |
| Category    | TCAM                           |     |         |
| Severity    | Error                          |     |         |
| Description | TCAMCounterinstallationfailure |     |         |
Event ID: 10207
| Message     | "Range Checker                      | installation | has failed" |
| ----------- | ----------------------------------- | ------------ | ----------- |
| Category    | TCAM                                |              |             |
| Severity    | Error                               |              |             |
| Description | TCAMRangeCheckerinstallationfailure |              |             |
Event ID: 10208
| Message     | "Policer uninstallation      | has | failed" |
| ----------- | ---------------------------- | --- | ------- |
| Category    | TCAM                         |     |         |
| Severity    | Error                        |     |         |
| Description | Policeruninstallationfailure |     |         |
Event ID: 10209
Message "TCAM entry uninstallation has failed in table <table_name>"
| Category    | TCAM                           |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Error                          |     |     |
| Description | TCAMentryuninstallationfailure |     |     |
Event ID: 10210
Message "High-capacity TCAM/LPM entry uninstallation failed in table <table_
name>"
TCAMevents|361

| Category    | TCAM                                            |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- |
| Severity    | Error                                           |     |     |     |     |
| Description | High-capacityTCAM/LPMentryuninstallationfailure |     |     |     |     |
Event ID: 10211
| Message     | "High-capacity                                  | TCAM/LPM | table uninstallation |     | failed" |
| ----------- | ----------------------------------------------- | -------- | -------------------- | --- | ------- |
| Category    | TCAM                                            |          |                      |     |         |
| Severity    | Error                                           |          |                      |     |         |
| Description | High-capacityTCAM/LPMtableuninstallationfailure |          |                      |     |         |
Event ID: 10212
| Message     | "Counter uninstallation          |     | has failed" |     |     |
| ----------- | -------------------------------- | --- | ----------- | --- | --- |
| Category    | TCAM                             |     |             |     |     |
| Severity    | Error                            |     |             |     |     |
| Description | TCAMCounteruninstallationfailure |     |             |     |     |
Event ID: 10213
| Message     | "Range Checker                        | uninstallation | has | failed" |     |
| ----------- | ------------------------------------- | -------------- | --- | ------- | --- |
| Category    | TCAM                                  |                |     |         |     |
| Severity    | Error                                 |                |     |         |     |
| Description | TCAMRangeCheckeruninstallationfailure |                |     |         |     |
Event ID: 10214
| Message     | "TCAM Context                              | Group selectors | have | been exhausted" |     |
| ----------- | ------------------------------------------ | --------------- | ---- | --------------- | --- |
| Category    | TCAM                                       |                 |      |                 |     |
| Severity    | Error                                      |                 |      |                 |     |
| Description | TCAMContextGroupselectorshavebeenexhausted |                 |      |                 |     |
Event ID: 10215
| Message  | "TCAM Context | Group IDs | have been | exhausted" |     |
| -------- | ------------- | --------- | --------- | ---------- | --- |
| Category | TCAM          |           |           |            |     |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 362

Severity

Error

Description

TCAM Context Group IDs have been exhausted

TCAM events | 363

|                      |     |     |     |        | Chapter | 110    |
| -------------------- | --- | --- | --- | ------ | ------- | ------ |
|                      |     |     |     | Telnet | server  | events |
| Telnet server events |     |     |     |        |         |        |
Thefollowingaretheeventsrelatedtotelnetserver.
Event ID: 12901
| Message     | TELNET server                                  | is enabled | on VRF <vrf_name>. |     |     |     |
| ----------- | ---------------------------------------------- | ---------- | ------------------ | --- | --- | --- |
| Category    | Telnetserver                                   |            |                    |     |     |     |
| Severity    | Information                                    |            |                    |     |     |     |
| Description | LogsamessagewhentheTelnetserverisenabledonaVRF |            |                    |     |     |     |
Event ID: 12902
| Message     | TELNET server                                   | is disabled | on VRF <vrf_name>. |     |     |     |
| ----------- | ----------------------------------------------- | ----------- | ------------------ | --- | --- | --- |
| Category    | Telnetserver                                    |             |                    |     |     |     |
| Severity    | Information                                     |             |                    |     |     |     |
| Description | LogsamessagewhentheTelnetserverisdisabledonaVRF |             |                    |     |     |     |
Event ID: 12903
Message Failed to enable Telnet server on VRF <vrf_name>. Admin password is
not set.
| Category | Telnetserver |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- |
| Severity | Error        |     |     |     |     |     |
Description LogsamessagewhenausertriestoenableTelnetserverwithoutsettingadmin
password
Event ID: 12904
Message User <user_name> logged in from <ip_address> through TELNET session.
| Category    | Telnetserver                           |     |     |     |     |     |
| ----------- | -------------------------------------- | --- | --- | --- | --- | --- |
| Severity    | Information                            |     |     |     |     |     |
| Description | Logsamessagewhenauserloginissuccessful |     |     |     |     |     |
Event ID: 12905
364
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

User <user_name> login from <ip_address> for TELNET session has
failed.

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

Event ID: 12907

Message

TELNET session from <ip_address> is rejected because maximum number
of TELNET sessions is reached.

Category

Telnet server

Severity

Warning

Description

Logs a message when a user tries to login while maximum number of sessions are
reached.

Event ID: 12908

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

Event ID: 12908

Message

User {user_name} login from {ip_address} for TELNET session has
failed since the user is trying to login through an interface which
is not allowed. Allowed interfaces are: {mgmt_intf}

Category

Telnet server

Severity

Error

Telnet server events | 365

Description

Logs a message when a user login fails since the access through this management

interface is not allowed

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

366

Chapter 111
Temperature events
| Temperature events |     |     |     |     |
| ------------------ | --- | --- | --- | --- |
Thefollowingaretheeventsrelatedtotemperature.
Event ID: 801
| Message     | Unrecognized                         | sensor type | <type> |     |
| ----------- | ------------------------------------ | ----------- | ------ | --- |
| Category    | Temperature                          |             |        |     |
| Severity    | Warning                              |             |        |     |
| Description | Logeventwhensensortypeisunrecognized |             |        |     |
Event ID: 802
Message Module <module> shutdown initiated for sensor <name> with critical
|          | temperature, | <temp> degC.': | yes |     |
| -------- | ------------ | -------------- | --- | --- |
| Category | Temperature  |                |     |     |
| Severity | Warning      |                |     |     |
Description Logeventwhensensortemperatureisabovethecriticalthreshold
Event ID: 803
Message Over-temperature for sensor <name>, <temp> degC.': yes
| Category | Temperature |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Warning     |     |     |     |
Description Logeventwhensensortemperatureisabovetheover-temperaturethreshold
Event ID: 804
| Message  | Sensor <name> | back to | safe temperature, | <temp> degC. |
| -------- | ------------- | ------- | ----------------- | ------------ |
| Category | Temperature   |         |                   |              |
| Severity | Information   |         |                   |              |
Description Logeventwhenasensorreturnstosafeoperatingconditions
Event ID: 805
367
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | System derate                  | changed from | <old> to <new> |
| ----------- | ------------------------------ | ------------ | -------------- |
| Category    | Temperature                    |              |                |
| Severity    | Information                    |              |                |
| Description | Logwhenthesystemderatechanges. |              |                |
Event ID: 806
Message Ambient temperature for sensor <name> above <temp> degC
| Category | Temperature |     |     |
| -------- | ----------- | --- | --- |
| Severity | Warning     |     |     |
Description Logwhenambienttemperatureisabovetheambienttemperaturelimits.
Event ID: 807
Message Ambient temperature for sensor <name> back to safe temperature,
|          | between <t_low> | and <t_high> | degC |
| -------- | --------------- | ------------ | ---- |
| Category | Temperature     |              |      |
| Severity | Information     |              |      |
Description Logwhenambienttemperaturereturnstosafeoperatingconditions.
Event ID: 808
Message Sensor <name> <limit_type> limit configuration <status>
| Category | Temperature |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logfailuresinconfiguringsensortemperaturewarning/criticallimits.
Event ID: 809
Message Ambient temperature <temp> degC is above the commercial grade
|          | transceiver | limit of <limit_high> | degC |
| -------- | ----------- | --------------------- | ---- |
| Category | Temperature |                       |      |
| Severity | Warning     |                       |      |
Description Logwhenambienttemperatureisabovecommercialgradetransceiverupperlimitwhen
non-industrialtransceiversareinstalled.
Event ID: 810
Temperatureevents|368

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

Ambient temperature <temp> degC returned to within the commercial
grade transceiver range of <limit_low>-<limit_high> degC

Category

Temperature

Severity

Information

Description

Log when ambient temperature returns to commercial grade transceiver range when
non-industrial transceivers are installed.

Event ID: 812

Message

Ambient temperature for sensor <name> below <temp> degC

Category

Temperature

Severity

Warning

Description

Log when ambient temperature is below the ambient temperature limits.

Event ID: 813

Message

Under-temperature for sensor <name>, <temp> degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is below the under-temperature threshold

Event ID: 814

Message

Module <module> shutdown initiated for sensor <name> with low
critical temperature, <temp> degC.': yes

Category

Temperature

Severity

Warning

Description

Log event when sensor temperature is below the low critical threshold

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

369

Chapter 112
|                 |        |     | Time | management events |
| --------------- | ------ | --- | ---- | ----------------- |
| Time management | events |     |      |                   |
Thefollowingaretheeventsrelatedtotimemanagement.
Event ID: 6201
| Message     | System timezone         | changed from | <oldtz> | to <newtz> |
| ----------- | ----------------------- | ------------ | ------- | ---------- |
| Category    | Timemanagement          |              |         |            |
| Severity    | Information             |              |         |            |
| Description | Changethesystemtimezone |              |         |            |
Event ID: 6202
Message System date/time changed from <old_time> to <new_time>
| Category    | Timemanagement           |     |     |     |
| ----------- | ------------------------ | --- | --- | --- |
| Severity    | Information              |     |     |     |
| Description | Changethesystemdate/time |     |     |     |
TPM events
ThefollowingaretheeventsrelatedtotheTPMDaemon.
Event ID: 13601
| Message  | TPM_Signrequestedby{process_name}wassuccessful |     |     |     |
| -------- | ---------------------------------------------- | --- | --- | --- |
| Category | TPMDaemon                                      |     |     |     |
| Severity | Information                                    |     |     |     |
Description IndicatesaTPM_Signoperationwassuccessfullyexecuted
Event ID: 13602
Message TPM_Signrequestedby{process_name}failedwithcode{reason}
| Category    | TPMDaemon                         |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Error                             |     |     |     |
| Description | IndicatesaTPM_Signoperationfailed |     |     |     |
370
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Event ID: | 13603 |     |
| --------- | ----- | --- |
Message
TPMselftesterrorsoccurredonthecurrentboot
| Category | TPMDaemon |     |
| -------- | --------- | --- |
| Severity | Error     |     |
Description IndicatesaTPMselftesterroroccurredonthecurrentboot
| Event ID: | 13604                                        |     |
| --------- | -------------------------------------------- | --- |
| Message   | Rebooted{reboot_num}timestoretryTPMselftests |     |
| Category  | TPMDaemon                                    |     |
| Severity  | Error                                        |     |
Description
IndicatesthesystemwasrebootedsomenumberoftimetorecoveryfromaTPMselftest
error
| Traffic | Insight | events |
| ------- | ------- | ------ |
ThefollowingaretheeventsrelatedtoTrafficInsight.
| Event ID: | 14001 |     |
| --------- | ----- | --- |
Message
Instance{instance_name}created
| Category | TrafficInsight |     |
| -------- | -------------- | --- |
| Severity | Info           |     |
Description
Eventindicatesnewtrafficinsightinstanceiscreated.
| Event ID:   | 14002                                          |     |
| ----------- | ---------------------------------------------- | --- |
| Message     | Instance{instance_name}deleted                 |     |
| Category    | TrafficInsight                                 |     |
| Severity    | Info                                           |     |
| Description | Eventindicatestrafficinsightinstanceisdeleted. |     |
| Event ID:   | 14003                                          |     |
Message
Top-Nflowsrunning-statisticsclearedforthemonitor{monitor_name}andinstance
{instance_name}
TrafficInsightevents|371

Category

Traffic Insight

Severity

Info

Description

Flow running-statistics timeout expired.

Event ID: 14004

Message

Top-N flows aggregate-statistics cleared for the monitor {monitor_name} and instance

{instance_name}

Category

Traffic Insight

Severity

Info

Description

Flow aggregate-statistics timeout expired.

Event ID: 14005

Message

Traffic Insight instance {instance_name} enabled

Category

Traffic Insight

Severity

Info

Description

Event indicates traffic insight instance is enabled.

Event ID: 14006

Message

Traffic Insight instance {instance_name} disabled

Category

Traffic Insight

Severity

Info

Description

Event indicates traffic insight instance is disabled.

Event ID: 14007

Message

Ignoring the flow for monitor {monitor_name} instance {instance_name}, maximum

application flow cache limit reached

Category

Traffic Insight

Severity

Info

Description

Event indicates maximum application flow cache limit reached for a traffic insight

instance.

Event ID: 14008

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

372

Message

DNS Average Latency statistics cache cleared for the monitor {monitor_name} and

instance {instance_name}

Category

Traffic Insight

Severity

Info

Description

Event indicates DNS average latency statistics cache gets cleared after the timeout.

Event ID: 14009

Message

14009

Category

Traffic Insight

Severity

Info

Description

Event indicates maximum flow count reached for raw-flows flow monitor for a traffic

insight instance.

Traffic Insight events | 373

Chapter 113
Transceiver events
| Transceiver events |     |     |     |
| ------------------ | --- | --- | --- |
Thefollowingaretheeventsrelatedtotransceiver.
Event ID: 3801
| Message  | allow-unsupported-transceiver |     | feature enabled |
| -------- | ----------------------------- | --- | --------------- |
| Category | Transceiver                   |     |                 |
| Severity | Information                   |     |                 |
Description Eventraisedwhenunsupportedtransceivermodeisenabled
Event ID: 3802
| Message  | allow-unsupported-transceiver |     | feature disabled |
| -------- | ----------------------------- | --- | ---------------- |
| Category | Transceiver                   |     |                  |
| Severity | Information                   |     |                  |
Description Eventraisedwhenunsupportedtransceivermodeisdisabled
Event ID: 3803
Message allow-unsupported-transceiver feature enabled: Unsupported
|          | transceivers | found in: | <list> |
| -------- | ------------ | --------- | ------ |
| Category | Transceiver  |           |        |
| Severity | Information  |           |        |
Description Eventraisedtolistunsupportedtransceiversinunsupportedtransceivermode
Event ID: 3804
Message Transceiver hot-swap insert for interface <interface>
| Category    | Transceiver                                      |     |     |
| ----------- | ------------------------------------------------ | --- | --- |
| Severity    | Information                                      |     |     |
| Description | Eventraisedtoindicatetransceiverhotswapinsertion |     |     |
Event ID: 3805
374
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

Transceiver hot-swap remove for interface <interface>

Category

Transceiver

Severity

Information

Description

Event raised to indicate transceiver hotswap removal

Event ID: 3806

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

Event ID: 3809

Message

Transceiver <xcvr_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate status of transceivers that are not allowed to be operational and
its reason

Event ID: 3810

Transceiver events | 375

Message

Unknown transceiver inserted in interface <interface>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate an unknown transceiver was inserted

Event ID: 3811

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

Event ID: 3813

Message

Adapter <adapter_desc> inserted in <interface> is <status>. <reason>

Category

Transceiver

Severity

Warning

Description

Event raised to indicate status of adapters that are not allowed to be operational and its
reason

Event ID: 3814

Message

Interface {interface} transceiver disabled - {disabled_reason}

Category

Transceiver

Severity

Warning

Description

Logged when the transceiver inserted in the interface is disabled

Event ID: 3815

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

376

Message

Interface {interface} transceiver enabled

Category

Transceiver

Severity

Info

Description

Logged when a previously disabled transceiver is enabled

Transceiver events | 377

Chapter 114
UDLD events
UDLD events
ThefollowingaretheeventsrelatedtoUDLD.
Event ID: 4101
| Message     | UDLD is enabled              | on interface: | <intf> |
| ----------- | ---------------------------- | ------------- | ------ |
| Category    | UDLD                         |               |        |
| Severity    | Information                  |               |        |
| Description | EventraisedwhenUDLDisenabled |               |        |
Event ID: 4102
| Message     | UDLD is disabled              | on interface: | <intf> |
| ----------- | ----------------------------- | ------------- | ------ |
| Category    | UDLD                          |               |        |
| Severity    | Information                   |               |        |
| Description | EventraisedwhenUDLDisdisabled |               |        |
Event ID: 4103
| Message     | UDLD interface                                 | <intf> | is unblocked |
| ----------- | ---------------------------------------------- | ------ | ------------ |
| Category    | UDLD                                           |        |              |
| Severity    | Information                                    |        |              |
| Description | EventraisedwhenUDLDsetstheinterfaceasunblocked |        |              |
Event ID: 4104
| Message     | UDLD interface                               | <intf> | is blocked |
| ----------- | -------------------------------------------- | ------ | ---------- |
| Category    | UDLD                                         |        |            |
| Severity    | Error                                        |        |            |
| Description | EventraisedwhenUDLDsetstheinterfaceasblocked |        |            |
Event ID: 4105
378
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | UDLD interface | <intf> | is undetermined |     |
| -------- | -------------- | ------ | --------------- | --- |
| Category | UDLD           |        |                 |     |
| Severity | Error          |        |                 |     |
Description EventraisedwhenUDLDmovesfrombidirectionalstatetoundetermined(RFC5171
modeonly)
Event ID: 4106
Message UDLD interface <intf> interval <intvl_a> clamped to <intvl_b>
| Category | UDLD    |     |     |     |
| -------- | ------- | --- | --- | --- |
| Severity | Warning |     |     |     |
Description LogsawarningwhenUDLDclampstheintervalwhenoperatinginRFC5171mode
Event ID: 4107
| Message     | UDLD link                        | is enabled | on interface: | <intf> |
| ----------- | -------------------------------- | ---------- | ------------- | ------ |
| Category    | UDLD                             |            |               |        |
| Severity    | Information                      |            |               |        |
| Description | EventraisedwhenUDLDlinkisenabled |            |               |        |
Event ID: 4108
| Message     | UDLD link                         | is disabled | on interface: | <intf> |
| ----------- | --------------------------------- | ----------- | ------------- | ------ |
| Category    | UDLD                              |             |               |        |
| Severity    | Information                       |             |               |        |
| Description | EventraisedwhenUDLDlinkisdisabled |             |               |        |
UDLDevents|379

Chapter 115
|               |           |        | UDP Broadcast | Forwarder | events |
| ------------- | --------- | ------ | ------------- | --------- | ------ |
| UDP Broadcast | Forwarder | events |               |           |        |
ThefollowingaretheeventsrelatedtoUDPBroadcastForwarder.
Event ID: 3601
| Message  | UDP Broadcast         | Forwarder | Enabled |     |     |
| -------- | --------------------- | --------- | ------- | --- | --- |
| Category | UDPBroadcastForwarder |           |         |     |     |
| Severity | Information           |           |         |     |     |
Description ThiscommandenablestheUDPBroadcastForwarderfeatureinthedevice.
Event ID: 3602
| Message  | UDP Broadcast         | Forwarder | Disabled |     |     |
| -------- | --------------------- | --------- | -------- | --- | --- |
| Category | UDPBroadcastForwarder |           |          |     |     |
| Severity | Information           |           |          |     |     |
Description ThiscommanddisablestheUDPBroadcastForwarderfeatureinthedevice.
380
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 116

UFD events

UFD events

The following are the events related to UFD.

Event ID: 12001

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

381

Chapter 117
|                 |        |     | User | management events |
| --------------- | ------ | --- | ---- | ----------------- |
| User management | events |     |      |                   |
Thefollowingaretheeventsrelatedtousermanagement.
Event ID: 4701
| Message     | User <user>                                | added <added_user> | with role | <user_role> |
| ----------- | ------------------------------------------ | ------------------ | --------- | ----------- |
| Category    | Usermanagement                             |                    |           |             |
| Severity    | Information                                |                    |           |             |
| Description | Logsamessagewhenanewuserisaddedtotheswitch |                    |           |             |
Event ID: 4702
Message User <user> deleted <deleted_user> with role <user_role>
| Category    | Usermanagement                              |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- |
| Severity    | Information                                 |     |     |     |
| Description | Logsamessagewhenauserisdeletedfromtheswitch |     |     |     |
Event ID: 4703
| Message     | User <username>                             | successfully | changed password |     |
| ----------- | ------------------------------------------- | ------------ | ---------------- | --- |
| Category    | Usermanagement                              |              |                  |     |
| Severity    | Information                                 |              |                  |     |
| Description | Logsamessagewhenauserchangeshis/herpassword |              |                  |     |
Event ID: 4704
| Message  | User <username> | password change | failed |     |
| -------- | --------------- | --------------- | ------ | --- |
| Category | Usermanagement  |                 |        |     |
| Severity | Error           |                 |        |     |
Description Logsamessagewhenauserfailstochangehis/herpassword
Event ID: 4705
382
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | User <username>                         | set export | password |
| ----------- | --------------------------------------- | ---------- | -------- |
| Category    | Usermanagement                          |            |          |
| Severity    | Information                             |            |          |
| Description | Logsamessagewhenausersetsexportpassword |            |          |
Event ID: 4706
| Message  | User <username> | restored | default export password |
| -------- | --------------- | -------- | ----------------------- |
| Category | Usermanagement  |          |                         |
| Severity | Information     |          |                         |
Description Logsamessagewhenauserrestoresdefaultexportpassword
Event ID: 4707
| Message     | Logsamessagewhenauserislockedout            |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Category    | Usermanagement                              |     |     |
| Severity    | Information                                 |     |     |
| Description | User{username}lockedoutfromsession{session} |     |     |
Usermanagementevents|383

Chapter 118

User-based tunnels events

User-based tunnels events

The following are the events related to user-based tunnels.

Event ID: 9701

Message

Tunnel Node Server SAC (<sac_ip>) is selected as (<state>)

Category

User-based tunnels

Severity

Information

Description

Event raised when controller is selected as Active/Standby

Event ID: 9702

Message

Tunnel Node Server Heartbeat has failed for SAC (<sac_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when heartbeat not received from a SAC

Event ID: 9703

Message

Tunnel Node Server keepalive has failed for UAC (<uac_ip>)

Category

User-based tunnels

Severity

Error

Description

Event raised when keepalive not received from a UAC

Event ID: 9704

Message

Tunnel Node Server SAC bootstrapping has reinitialized to (<sac_ip>)

Category

User-based tunnels

Severity

Information

Description

Event raised when SAC bootstapping to a SAC is re-initialized

Event ID: 9705

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

384

| Message  | Tunnel            | Node Server | PAPI | key has mismatched |     |
| -------- | ----------------- | ----------- | ---- | ------------------ | --- |
| Category | User-basedtunnels |             |      |                    |     |
| Severity | Error             |             |      |                    |     |
Description Eventraisedwhenpapimsgkeysentandreceivedisdifferent({key_id})
Event ID: 9706
| Message     | Tunnel                       | Node Server | UAC | node is down | (<uac_ip>) |
| ----------- | ---------------------------- | ----------- | --- | ------------ | ---------- |
| Category    | User-basedtunnels            |             |     |              |            |
| Severity    | Critical                     |             |     |              |            |
| Description | EventraisedwhenUACnodeisdown |             |     |              |            |
Event ID: 9707
Message Tunnel is Created - Gre Key (<gre_key>) VRF (<vrf>) Source IP (<src_
|             | ip>) Destination                        |     | IP (<dst_ip>) |     |     |
| ----------- | --------------------------------------- | --- | ------------- | --- | --- |
| Category    | User-basedtunnels                       |     |               |     |     |
| Severity    | Information                             |     |               |     |     |
| Description | Eventraisedwhenuserbasedtunneliscreated |     |               |     |     |
Event ID: 9708
Message Tunnel Creation has Failed - Gre Key (<gre_key>) VRF (<vrf>) Source
|             | IP (<src_ip>)                               | Destination |     | IP (<dst_ip>) |     |
| ----------- | ------------------------------------------- | ----------- | --- | ------------- | --- |
| Category    | User-basedtunnels                           |             |     |               |     |
| Severity    | Error                                       |             |     |               |     |
| Description | Eventraisedwhenuserbasedtunnelcreationfails |             |     |               |     |
Event ID: 9709
| Message     | Tunnel                                  | is Deleted | - Tunnel | Id (<tunnel_id>) |     |
| ----------- | --------------------------------------- | ---------- | -------- | ---------------- | --- |
| Category    | User-basedtunnels                       |            |          |                  |     |
| Severity    | Information                             |            |          |                  |     |
| Description | Eventraisedwhenuserbasedtunnelisdeleted |            |          |                  |     |
Event ID: 9710
User-basedtunnelsevents|385

| Message     | Tunnel Deletion                             | has | Failed - Tunnel | Id (<tunnel_id>) |
| ----------- | ------------------------------------------- | --- | --------------- | ---------------- |
| Category    | User-basedtunnels                           |     |                 |                  |
| Severity    | Error                                       |     |                 |                  |
| Description | Eventraisedwhenuserbasedtunneldeletionfails |     |                 |                  |
Event ID: 9711
Message Tunnel is UP - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source IP
|             | (<src_ip>)                              | Destination | IP (<dst_ip>) |     |
| ----------- | --------------------------------------- | ----------- | ------------- | --- |
| Category    | User-basedtunnels                       |             |               |     |
| Severity    | Information                             |             |               |     |
| Description | Eventraisedwhenuserbasedtunnelstateisup |             |               |     |
Event ID: 9712
Message Tunnel is DOWN - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>) Source
|             | IP (<src_ip>)                             | Destination | IP (<dst_ip>) |     |
| ----------- | ----------------------------------------- | ----------- | ------------- | --- |
| Category    | User-basedtunnels                         |             |               |     |
| Severity    | Error                                     |             |               |     |
| Description | Eventraisedwhenuserbasedtunnelstateisdown |             |               |     |
Event ID: 9713
Message Client (<client_mac>) is bound to tunnel id (<tunnel_id>)
| Category    | User-basedtunnels                       |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Information                             |     |     |     |
| Description | Eventraisedwhenuserisgetsbindedtotunnel |     |     |     |
Event ID: 9714
Message Client (<client_mac>) binding to tunnel id (<tunnel_id>) has failed
| Category    | User-basedtunnels                       |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- |
| Severity    | Error                                   |     |     |     |
| Description | Eventraisedwhenuserbindtotunnelidfailed |     |     |     |
Event ID: 9715
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 386

| Message     | Client (<client_mac>)                   |     | is removed | from tunnel. |
| ----------- | --------------------------------------- | --- | ---------- | ------------ |
| Category    | User-basedtunnels                       |     |            |              |
| Severity    | Information                             |     |            |              |
| Description | Eventraisedwhenuserisgetsbindedtotunnel |     |            |              |
Event ID: 9716
Message Client (<client_mac>) unbinding to tunnel id (<tunnel_id>) has failed
| Category    | User-basedtunnels                         |     |     |     |
| ----------- | ----------------------------------------- | --- | --- | --- |
| Severity    | Error                                     |     |     |     |
| Description | Eventraisedwhenuserunbindtotunnelidfailed |     |     |     |
Event ID: 9717
Message Client (<client_mac>) is getting modified to bind to tunnel id
|          | (<tunnel_id>)'    | throttle_count: |     | 100 |
| -------- | ----------------- | --------------- | --- | --- |
| Category | User-basedtunnels |                 |     |     |
| Severity | Information       |                 |     |     |
Description Eventraisedwhenalreadybindedusertoatunnelgetsmodified
Event ID: 9718
Message Modification of Client (<client_mac>) binded to (<tunnel_id>) has
|          | failed' throttle_count: |     | 100 |     |
| -------- | ----------------------- | --- | --- | --- |
| Category | User-basedtunnels       |     |     |     |
| Severity | Error                   |     |     |     |
Description Eventraisedwhenmodificationofalreadybindedusertoatunnelfails
Event ID: 9719
Message NFD port (<nfd_id>) is created for client (<client_mac>) vlan id
|             | (<vlan_id>)                  | port (<port>) | ecmp | id (<ecmp_id>) |
| ----------- | ---------------------------- | ------------- | ---- | -------------- |
| Category    | User-basedtunnels            |               |      |                |
| Severity    | Information                  |               |      |                |
| Description | EventraisedonNFDportcreation |               |      |                |
Event ID: 9720
User-basedtunnelsevents|387

Message NFD port (<nfd_id>) creation for client (<client_mac>) vlan id
|             | (<vlan_id>)                         | port (<port>) | ecmp | id (<ecmp_id>) | has failed |
| ----------- | ----------------------------------- | ------------- | ---- | -------------- | ---------- |
| Category    | User-basedtunnels                   |               |      |                |            |
| Severity    | Error                               |               |      |                |            |
| Description | EventraisedonNFDportcreationfailure |               |      |                |            |
Event ID: 9721
Message NFD port (<nfd_id>) is deleted for ecmp id(<ecmp_id>)
| Category    | User-basedtunnels            |     |     |     |     |
| ----------- | ---------------------------- | --- | --- | --- | --- |
| Severity    | Information                  |     |     |     |     |
| Description | EventraisedonNFDportdeletion |     |     |     |     |
Event ID: 9722
Message NFD port (<nfd_id>) deletion for ecmp id (<ecmp_id>) has failed
| Category    | User-basedtunnels                   |     |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- | --- |
| Severity    | Error                               |     |     |     |     |
| Description | EventraisedwhenNFDportdeletionfails |     |     |     |     |
Event ID: 9723
| Message     | ECMP group                     | is created | for ecmp | id (<ecmp_id>) |     |
| ----------- | ------------------------------ | ---------- | -------- | -------------- | --- |
| Category    | User-basedtunnels              |            |          |                |     |
| Severity    | Information                    |            |          |                |     |
| Description | EventraisedonECMPgroupcreation |            |          |                |     |
Event ID: 9724
Message ECMP group creation for ecmp id (<ecmp_id>) has failed
| Category    | User-basedtunnels                     |     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- |
| Severity    | Error                                 |     |     |     |     |
| Description | EventraisedonECMPgroupcreationfailure |     |     |     |     |
Event ID: 9725
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 388

| Message     | ECMP group                     | is deleted | for | ecmp id (<ecmp_id>) |     |
| ----------- | ------------------------------ | ---------- | --- | ------------------- | --- |
| Category    | User-basedtunnels              |            |     |                     |     |
| Severity    | Information                    |            |     |                     |     |
| Description | EventraisedonECMPgroupdeletion |            |     |                     |     |
Event ID: 9726
Message ECMP group deletion for ecmp id(<ecmp_id>) has failed
| Category    | User-basedtunnels                     |     |     |     |     |
| ----------- | ------------------------------------- | --- | --- | --- | --- |
| Severity    | Error                                 |     |     |     |     |
| Description | EventraisedwhenECMPgroupdeletionfails |     |     |     |     |
Event ID: 9727
Message MDestRx Tunnel is Created - Gre Key (<gre_key>) VLAN (<vlan>) VRF
|             | (<vrf>)                                        | Source IP (<src_ip>) |     | Destination | IP (<dst_ip>) |
| ----------- | ---------------------------------------------- | -------------------- | --- | ----------- | ------------- |
| Category    | User-basedtunnels                              |                      |     |             |               |
| Severity    | Information                                    |                      |     |             |               |
| Description | Eventraisedwhenmdestrxuserbasedtunneliscreated |                      |     |             |               |
Event ID: 9728
Message MDestRx Tunnel Creation has Failed - Gre Key (<gre_key>) VLAN
(<vlan>) VRF (<vrf>) Source IP (<src_ip>) Destination IP (<dst_ip>)
| Category | User-basedtunnels |     |     |     |     |
| -------- | ----------------- | --- | --- | --- | --- |
| Severity | Error             |     |     |     |     |
Description Eventraisedwhenmdestrxuserbasedtunnelcreationfails
Event ID: 9729
| Message     | MDest Rx                                       | Tunnel is | Deleted | - Tunnel | Id (<tunnel_id>) |
| ----------- | ---------------------------------------------- | --------- | ------- | -------- | ---------------- |
| Category    | User-basedtunnels                              |           |         |          |                  |
| Severity    | Information                                    |           |         |          |                  |
| Description | Eventraisedwhenmdestrxuserbasedtunnelisdeleted |           |         |          |                  |
Event ID: 9730
User-basedtunnelsevents|389

Message MDest Rx Tunnel Deletion has Failed - Tunnel Id (<tunnel_id>)
| Category | User-basedtunnels |     |     |     |
| -------- | ----------------- | --- | --- | --- |
| Severity | Error             |     |     |     |
Description Eventraisedwhenmdestrxuserbasedtunneldeletionfails
Event ID: 9731
Message MDestRx Tunnel is UP - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>)
|             | Source                                         | IP (<src_ip>) | Destination | IP (<dst_ip>) |
| ----------- | ---------------------------------------------- | ------------- | ----------- | ------------- |
| Category    | User-basedtunnels                              |               |             |               |
| Severity    | Information                                    |               |             |               |
| Description | Eventraisedwhenmdestrxuserbasedtunnelstateisup |               |             |               |
Event ID: 9732
Message MDestRx Tunnel is DOWN - Tunnel Id (<tunnel_id>) Gre Key (<gre_key>)
|             | Source                                           | IP (<src_ip>) | Destination | IP (<dst_ip>) |
| ----------- | ------------------------------------------------ | ------------- | ----------- | ------------- |
| Category    | User-basedtunnels                                |               |             |               |
| Severity    | Error                                            |               |             |               |
| Description | Eventraisedwhenmdestrxuserbasedtunnelstateisdown |               |             |               |
Event ID: 9733
Message User bootstrap is failed for client (<mac_addr>) on port (<port>) due
to <reason>.
| Category    | User-basedtunnels                    |     |     |     |
| ----------- | ------------------------------------ | --- | --- | --- |
| Severity    | Error                                |     |     |     |
| Description | Eventraisedwhenuserbootstrapisfailed |     |     |     |
Event ID: 9734
| Message     | Operational                             | state | of <zone> zone | is UP. |
| ----------- | --------------------------------------- | ----- | -------------- | ------ |
| Category    | User-basedtunnels                       |       |                |        |
| Severity    | Information                             |       |                |        |
| Description | Eventraisedwhenzoneoperationalstateisup |       |                |        |
Event ID: 9735
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 390

Message

Operational state of <zone> zone is DOWN due to <reason>.

Category

User-based tunnels

Severity

Warning

Description

Event raised when zone operational state is down

Event ID: 9736

Message

Tunnel Node Server WoL VLAN bootstrap {state} with controller {sac_
ip}

Category

User-based tunnels

Severity

Information

Description

Event raised when WoL VLAN bootstrap response received from controller
(Active/Standby)

Event ID: 9737

Message

Tunnel Node Server WoL VLAN bootstrap failed due to incompatible
controller ({sac_ip}) version {version}

Category

User-based tunnels

Severity

Information

Description

Event raised when controller version does not support WoL VLAN bootstrap

User-based tunnels events | 391

Chapter 119
|                   |           | Virtual      | Switching | Extension | (VSX) events |
| ----------------- | --------- | ------------ | --------- | --------- | ------------ |
| Virtual Switching | Extension | (VSX) events |           |           |              |
ThefollowingaretheeventsrelatedtoVSX.
Event ID: 7001
| Message     | VSX ISL                        | port <port> | is down |     |     |
| ----------- | ------------------------------ | ----------- | ------- | --- | --- |
| Category    | VirtualSwitchingExtension(VSX) |             |         |     |     |
| Severity    | Information                    |             |         |     |     |
| Description | VSXISLlinkisdown.              |             |         |     |     |
Event ID: 7002
| Message     | VSX ISL                        | port <port> | is up |     |     |
| ----------- | ------------------------------ | ----------- | ----- | --- | --- |
| Category    | VirtualSwitchingExtension(VSX) |             |       |     |     |
| Severity    | Information                    |             |       |     |     |
| Description | VSXISLlinkisup.                |             |       |     |     |
Event ID: 7003
| Message     | VSX ISL                        | port <port> | is In-Sync with | the peer. |     |
| ----------- | ------------------------------ | ----------- | --------------- | --------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |             |                 |           |     |
| Severity    | Information                    |             |                 |           |     |
| Description | VSXISLisInSyncwiththepeer.     |             |                 |           |     |
Event ID: 7004
Message VSX ISL port <port> is Out-Of-Sync with the peer: <reason>
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Severity    | Error                          |     |     |     |     |
| Description | VSXISLisOut-Of-Syncwiththepeer |     |     |     |     |
Event ID: 7005
392
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | VSX Keepalive                             | failed |
| ----------- | ----------------------------------------- | ------ |
| Category    | VirtualSwitchingExtension(VSX)            |        |
| Severity    | Warning                                   |        |
| Description | VSXKeepaliveisnotabletoreachthepeerdevice |        |
Event ID: 7006
| Message     | VSX Keepalive                          | succeeded |
| ----------- | -------------------------------------- | --------- |
| Category    | VirtualSwitchingExtension(VSX)         |           |
| Severity    | Information                            |           |
| Description | VSXKeepaliveisabletoreachthepeerdevice |           |
Event ID: 7007
| Message  | VSX role                       | is primary |
| -------- | ------------------------------ | ---------- |
| Category | VirtualSwitchingExtension(VSX) |            |
| Severity | Information                    |            |
Description Operationalroleofthisdevicederivedbasedondevicepriorityofthe2devices.
Event ID: 7008
| Message  | VSX role                       | is secondary |
| -------- | ------------------------------ | ------------ |
| Category | VirtualSwitchingExtension(VSX) |              |
| Severity | Information                    |              |
Description Operationalroleofthisdevicederivedbasedondevicepriorityofthe2devices.
Event ID: 7009
Message VSX Software version mismatch: peer version <peer_sw_ver>, local
|          | version <local_sw_ver>         |     |
| -------- | ------------------------------ | --- |
| Category | VirtualSwitchingExtension(VSX) |     |
| Severity | Information                    |     |
Description VSXSoftwareversionmismatch:peerswversionisnotsameaslocalswversion.
Event ID: 7010
Message VSX Device mismatch: peer device <peer_device_type>, local device
VirtualSwitchingExtension(VSX)events|393

<local_device_type>
| Category | VirtualSwitchingExtension(VSX) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Information                    |     |     |     |
Description VSXDevicetypemismatch:peerdevicetypeisnotsameaslocaldevicetype.
Event ID: 7011
| Message     | VSX <vsx_id>                   | state local | up, remote | down |
| ----------- | ------------------------------ | ----------- | ---------- | ---- |
| Category    | VirtualSwitchingExtension(VSX) |             |            |      |
| Severity    | Information                    |             |            |      |
| Description | VSXlocalupremotedown.          |             |            |      |
Event ID: 7012
| Message     | VSX <vsx_id>                   | state local | down, remote | up  |
| ----------- | ------------------------------ | ----------- | ------------ | --- |
| Category    | VirtualSwitchingExtension(VSX) |             |              |     |
| Severity    | Information                    |             |              |     |
| Description | VSXlocaldownremoteup.          |             |              |     |
Event ID: 7013
| Message     | VSX <vsx_id>                   | state local | up, remote | up  |
| ----------- | ------------------------------ | ----------- | ---------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |             |            |     |
| Severity    | Information                    |             |            |     |
| Description | VSXlocalupremoteup.            |             |            |     |
Event ID: 7014
| Message     | VSX <vsx_id>                   | state local | down, remote | down |
| ----------- | ------------------------------ | ----------- | ------------ | ---- |
| Category    | VirtualSwitchingExtension(VSX) |             |              |      |
| Severity    | Information                    |             |              |      |
| Description | VSXlocaldownremotedown.        |             |              |      |
Event ID: 7015
| Message | VSX ISL sliding | window | parameters | are reset. |
| ------- | --------------- | ------ | ---------- | ---------- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 394

| Category    | VirtualSwitchingExtension(VSX)           |     |     |     |
| ----------- | ---------------------------------------- | --- | --- | --- |
| Severity    | Information                              |     |     |     |
| Description | VSXresettingtheISLprotocolslidingwindow. |     |     |     |
Event ID: 7016
Message VSX own ISL hello packet received, ignoring the packet.
| Category    | VirtualSwitchingExtension(VSX)                 |     |     |     |
| ----------- | ---------------------------------------------- | --- | --- | --- |
| Severity    | Information                                    |     |     |     |
| Description | VSXswitchreceivesownISLhellopacketfromnetwork. |     |     |     |
Event ID: 7017
Message Rebooting the VSX <vsx_role> device with newly updated <bank_name>
image.
| Category    | VirtualSwitchingExtension(VSX)      |     |     |     |
| ----------- | ----------------------------------- | --- | --- | --- |
| Severity    | Information                         |     |     |     |
| Description | SwitchrebootduetoVSXsoftwareupdate. |     |     |     |
Event ID: 7018
Message VSX primary ISL version <primary_version> dose not match with VSX
secondary ISL version <secondary_version>. Performing a non-hitless
image update.
| Category | VirtualSwitchingExtension(VSX) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Information                    |     |     |     |
Description VSXinter-switch-linkprotocolversionmismatchaftersecondaryreboot.
Event ID: 7019
| Message     | VSX <vsx_role>                 | image update | failed due | to <reason>. |
| ----------- | ------------------------------ | ------------ | ---------- | ------------ |
| Category    | VirtualSwitchingExtension(VSX) |              |            |              |
| Severity    | Error                          |              |            |              |
| Description | VSXimageupdatefailed.          |              |            |              |
Event ID: 7020
VirtualSwitchingExtension(VSX)events|395

| Message  | ISL out-of-sync                | and keepalive | is in established |
| -------- | ------------------------------ | ------------- | ----------------- |
| Category | VirtualSwitchingExtension(VSX) |               |                   |
| Severity | Information                    |               |                   |
Description ISLout-of-syncandkeepaliveisinestablished,handledsplitbrain
Event ID: 7021
| Message     | ISL out-of-sync                      | and keepalive | also failed |
| ----------- | ------------------------------------ | ------------- | ----------- |
| Category    | VirtualSwitchingExtension(VSX)       |               |             |
| Severity    | Information                          |               |             |
| Description | ISLout-of-syncandkeepalivealsofailed |               |             |
Event ID: 7022
| Message     | Linkup delay                   | timer started |     |
| ----------- | ------------------------------ | ------------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |               |     |
| Severity    | Information                    |               |     |
| Description | Linkupdelaytimerstarted        |               |     |
Event ID: 7023
| Message     | Linkup delay                   | timer expired |     |
| ----------- | ------------------------------ | ------------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |               |     |
| Severity    | Information                    |               |     |
| Description | Linkupdelaytimerexpired        |               |     |
Event ID: 7024
Message VSX <vsx_role> state changed from <prev_state> to <state>.
| Category    | VirtualSwitchingExtension(VSX) |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | VSXsoftwareupdatestatechange.  |     |     |
Event ID: 7025
| Message | Bailout timer | started |     |
| ------- | ------------- | ------- | --- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 396

| Category    | VirtualSwitchingExtension(VSX) |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | Bailouttimerstarted            |     |     |
Event ID: 7026
| Message     | Bailout timer                  | expired |     |
| ----------- | ------------------------------ | ------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |         |     |
| Severity    | Information                    |         |     |
| Description | Bailouttimerexpired            |         |     |
Event ID: 7027
| Message     | Bailout timer                  | stopped |     |
| ----------- | ------------------------------ | ------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |         |     |
| Severity    | Information                    |         |     |
| Description | Bailouttimerstopped            |         |     |
Event ID: 7028
| Message     | Linkup-delay                   | timer stopped |     |
| ----------- | ------------------------------ | ------------- | --- |
| Category    | VirtualSwitchingExtension(VSX) |               |     |
| Severity    | Information                    |               |     |
| Description | Linkup-delaytimerstopped       |               |     |
Event ID: 7029
Message VSX device roles are inconsistent: local VSX device role <local_vsx_
|          | role>, peer                    | VSX device | role <peer_vsx_role> |
| -------- | ------------------------------ | ---------- | -------------------- |
| Category | VirtualSwitchingExtension(VSX) |            |                      |
| Severity | Error                          |            |                      |
Description VSXdevicerolesaresaidtobeconsistentonlyifoneVSXdeviceisconfiguredasprimary
andotherVSXdeviceisconfiguredassecondary
Event ID: 7029
| Message | VSX <vsx_role> | state | changed to <state>-<sub_state>. |
| ------- | -------------- | ----- | ------------------------------- |
VirtualSwitchingExtension(VSX)events|397

| Category    | VirtualSwitchingExtension(VSX)    |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Information                       |     |     |     |
| Description | VSXsoftwareupdatesub-statechange. |     |     |     |
Event ID: 7030
| Message     | VSX Keepalive                                    | is configured | without | creating VRF |
| ----------- | ------------------------------------------------ | ------------- | ------- | ------------ |
| Category    | VirtualSwitchingExtension(VSX)                   |               |         |              |
| Severity    | Information                                      |               |         |              |
| Description | VRFneedstobecreatedbeforeconfiguringVSXKeepalive |               |         |              |
Event ID: 7031
Message VSX Keepalive is configured without configuring IP address
| Category | VirtualSwitchingExtension(VSX) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Information                    |     |     |     |
Description IPaddressneedstobeconfiguredbeforeconfiguringVSXKeepalive
Event ID: 7032
Message Active-gateway is enabled on <port>. Cannot program Active-forwarding
| Category    | VirtualSwitchingExtension(VSX)    |     |     |     |
| ----------- | --------------------------------- | --- | --- | --- |
| Severity    | Error                             |     |     |     |
| Description | Failedtoprogramactive-forwarding. |     |     |     |
Event ID: 7033
Message Active-forwarding is enabled on <port>. Cannot program Active-gateway
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Error                          |     |     |     |
| Description | Failedtoprogramactive-gateway. |     |     |     |
Event ID: 7034
| Message  | Netdev <ifname>                | configured | with ipv4 | address <value> |
| -------- | ------------------------------ | ---------- | --------- | --------------- |
| Category | VirtualSwitchingExtension(VSX) |            |           |                 |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 398

| Severity    | Information                                     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Description | programmedactive-gatewayIP4addresssuccessfully. |     |     |     |
Event ID: 7035
| Message     | Netdev <ifname>                                 | configured | with ipv6 | address <value> |
| ----------- | ----------------------------------------------- | ---------- | --------- | --------------- |
| Category    | VirtualSwitchingExtension(VSX)                  |            |           |                 |
| Severity    | Information                                     |            |           |                 |
| Description | programmedactive-gatewayIP6addresssuccessfully. |            |           |                 |
Event ID: 7036
| Message     | VSX{vsx_role}statechangedto{state}-{sub_state}. |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- |
| Category    | VirtualSwitchingExtension(VSX)                  |     |     |     |
| Severity    | Information                                     |     |     |     |
| Description | VSXsoftwareupdatesub-statechange.               |     |     |     |
Event ID: 7037
Message VSXsecondaryhasbetterMCLAGstatecomparedtoVSXprimary.MCLAGsandSVIsare
broughtdownonVSXprimary.
| Category    | VirtualSwitchingExtension(VSX) |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Information                    |     |     |     |
| Description | VSXsplitstateisinversed.       |     |     |     |
VirtualSwitchingExtension(VSX)events|399

Chapter 120
|                   |           | Virtual | Switching | Framework | (VSF) events |
| ----------------- | --------- | ------- | --------- | --------- | ------------ |
| Virtual Switching | Framework | (VSF)   | events    |           |              |
ThefollowingaretheeventsrelatedtoVSF.
Event ID: 9901
| Message     | Member                         | <member_id> | boot complete |     |     |
| ----------- | ------------------------------ | ----------- | ------------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF) |             |               |     |     |
| Severity    | Information                    |             |               |     |     |
| Description | logeventformemberbootcomplete  |             |               |     |     |
Event ID: 9902
| Message     | Standby                        | <member_id> | boot complete |     |     |
| ----------- | ------------------------------ | ----------- | ------------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF) |             |               |     |     |
| Severity    | Information                    |             |               |     |     |
| Description | logeventforstandbybootcomplete |             |               |     |     |
Event ID: 9903
| Message     | Conductor                        | <member_id> | boot complete |     |     |
| ----------- | -------------------------------- | ----------- | ------------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)   |             |               |     |     |
| Severity    | Information                      |             |               |     |     |
| Description | logeventforConductorbootcomplete |             |               |     |     |
Event ID: 9905
| Message     | Resetting                             | member | <member_id> |     |     |
| ----------- | ------------------------------------- | ------ | ----------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)        |        |             |     |     |
| Severity    | Information                           |        |             |     |     |
| Description | Eventlogindicatesthatmemberisreseting |        |             |     |     |
Event ID: 9906
400
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | Member <member_id>             | conflict | detected | on link <link> |
| -------- | ------------------------------ | -------- | -------- | -------------- |
| Category | VirtualSwitchingFramework(VSF) |          |          |                |
| Severity | Warning                        |          |          |                |
Description EventlogforFailedprocessingHellopacketbecauseofmembernumberconflict
Event ID: 9907
| Message  | Incompatible                   | version detected |     |     |
| -------- | ------------------------------ | ---------------- | --- | --- |
| Category | VirtualSwitchingFramework(VSF) |                  |     |     |
| Severity | Warning                        |                  |     |     |
Description Eventlogforindicatesthatwegotapacketwithadiffprotover
Event ID: 9908
| Message     | Topology                            | is <topo_type> |     |     |
| ----------- | ----------------------------------- | -------------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)      |                |     |     |
| Severity    | Information                         |                |     |     |
| Description | Eventlogindicatesthecurrenttopology |                |     |     |
Event ID: 9910
| Message  | Member <member_id>             | removed |     |     |
| -------- | ------------------------------ | ------- | --- | --- |
| Category | VirtualSwitchingFramework(VSF) |         |     |     |
| Severity | Information                    |         |     |     |
Description Eventlogindicatesthememberhasbeenremovedduetouserrequest
Event ID: 9911
Message Maximum number of switches in the stack has reached. Cannot add MAC
|          | <mac_address>                  | product type | <type> |     |
| -------- | ------------------------------ | ------------ | ------ | --- |
| Category | VirtualSwitchingFramework(VSF) |              |        |     |
| Severity | Warning                        |              |        |     |
Description EventlogindicatesthatwewouldexceedtheMAXswitchesifweaddthisnewswitch
Event ID: 9912
Message Stack state is no-split with conductor id <member_id>' throttle_
VirtualSwitchingFramework(VSF)events|401

count: 100
| Category    | VirtualSwitchingFramework(VSF) |     |     |
| ----------- | ------------------------------ | --- | --- |
| Severity    | Information                    |     |     |
| Description | logeventforstackstateactive    |     |     |
Event ID: 9913
| Message     | Lost member                    | <member_id> | with <reason> |
| ----------- | ------------------------------ | ----------- | ------------- |
| Category    | VirtualSwitchingFramework(VSF) |             |               |
| Severity    | Warning                        |             |               |
| Description | Eventlogforlostmember          |             |               |
Event ID: 9914
| Message     | Reboot                            | of MAC <mac_address> | status-<status> |
| ----------- | --------------------------------- | -------------------- | --------------- |
| Category    | VirtualSwitchingFramework(VSF)    |                      |                 |
| Severity    | Information                       |                      |                 |
| Description | Eventlogforstatusofarebootrequest |                      |                 |
Event ID: 9915
Message Member <member_id> elected as conductor reason-<reason>
| Category    | VirtualSwitchingFramework(VSF)     |     |     |
| ----------- | ---------------------------------- | --- | --- |
| Severity    | Information                        |     |     |
| Description | logeventfortheswitchwonasconductor |     |     |
Event ID: 9916
Message Member <member_id> elected as standby reason-<reason>
| Category    | VirtualSwitchingFramework(VSF)   |     |     |
| ----------- | -------------------------------- | --- | --- |
| Severity    | Information                      |     |     |
| Description | logeventfortheswitchwonasstandby |     |     |
Event ID: 9917
Message Switch with MAC <mac_address> cannot join stack due to incorrect
|     | product | id <product_id> |     |
| --- | ------- | --------------- | --- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 402

| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventforthememberwasnotallowedtojoinduetoamismatchedproduct-id
Event ID: 9919
Message Found Unsupported switch with MAC <mac_address> and Product type
<product_type>, connected to switch with MAC <mac_addr> on stack port
<port_id>
| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventforswitchrunningonadifferentplatformandtryingtojointhestack
Event ID: 9920
| Message     | Heart beat                     | lost for member | <member_id> |     |
| ----------- | ------------------------------ | --------------- | ----------- | --- |
| Category    | VirtualSwitchingFramework(VSF) |                 |             |     |
| Severity    | Warning                        |                 |             |     |
| Description | logeventforheartbeatlost       |                 |             |     |
Event ID: 9921
| Message  | OS version                     | mismatch detected | for member | <member_id> |
| -------- | ------------------------------ | ----------------- | ---------- | ----------- |
| Category | VirtualSwitchingFramework(VSF) |                   |            |             |
| Severity | Warning                        |                   |            |             |
Description logeventwhenos_version_mismatchhappenedonstandbyandmember
Event ID: 9922
Message Attempt to connect member <member_id> from a different stack
| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventwhenmemberattempttoconnecttoadifferentstack
Event ID: 9923
| Message | VSF link | <link> is up |     |     |
| ------- | -------- | ------------ | --- | --- |
VirtualSwitchingFramework(VSF)events|403

| Category    | VirtualSwitchingFramework(VSF) |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Information                    |     |     |     |
| Description | logeventwhenvsflinkisup        |     |     |     |
Event ID: 9924
| Message     | VSF link <link>                | is down |     |     |
| ----------- | ------------------------------ | ------- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF) |         |     |     |
| Severity    | Information                    |         |     |     |
| Description | logeventwhenvsflinkisdown      |         |     |     |
Event ID: 9925
Message Invalid MAC <mac_address> detected on link <link> with peer MAC <mac_
add>
| Category    | VirtualSwitchingFramework(VSF)               |     |     |     |
| ----------- | -------------------------------------------- | --- | --- | --- |
| Severity    | Warning                                      |     |     |     |
| Description | logeventwhendifferentMACaddressonthesamelink |     |     |     |
Event ID: 9926
| Message     | 2 member loop                             | detected | on ring topology |     |
| ----------- | ----------------------------------------- | -------- | ---------------- | --- |
| Category    | VirtualSwitchingFramework(VSF)            |          |                  |     |
| Severity    | Warning                                   |          |                  |     |
| Description | logeventwhenthereisa2memberloopintopology |          |                  |     |
Event ID: 9927
Message Fragment with conductor <member_id> is Active' throttle_count: 100
| Category    | VirtualSwitchingFramework(VSF) |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- |
| Severity    | Information                    |     |     |     |
| Description | logeventforactivefragment      |     |     |     |
Event ID: 9928
| Message | Fragment with | conductor | <member_id> | is Inactive |
| ------- | ------------- | --------- | ----------- | ----------- |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 404

| Category    | VirtualSwitchingFramework(VSF) |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
| Severity    | Information                    |     |     |     |     |
| Description | logeventforInactivefragment    |     |     |     |     |
Event ID: 9929
| Message     | Active                                 | fragment | detection | timeout |     |
| ----------- | -------------------------------------- | -------- | --------- | ------- | --- |
| Category    | VirtualSwitchingFramework(VSF)         |          |           |         |     |
| Severity    | Information                            |          |           |         |     |
| Description | logeventforactivestackdetectiontimeout |          |           |         |     |
Event ID: 9930
| Message     | Member                          | <member_id> | is  | configured | as Secondary |
| ----------- | ------------------------------- | ----------- | --- | ---------- | ------------ |
| Category    | VirtualSwitchingFramework(VSF)  |             |     |            |              |
| Severity    | Information                     |             |     |            |              |
| Description | logeventforstandbyconfiguration |             |     |            |              |
Event ID: 9931
| Message     | Secondary                         | configuration |     | removed |     |
| ----------- | --------------------------------- | ------------- | --- | ------- | --- |
| Category    | VirtualSwitchingFramework(VSF)    |               |     |         |     |
| Severity    | Information                       |               |     |         |     |
| Description | logeventforstandbyunconfiguration |               |     |         |     |
Event ID: 9932
Message Attempt to connect a member with MAC <mac_address> and product type
|             | <product_id>                            |     | having different |     | airflows |
| ----------- | --------------------------------------- | --- | ---------------- | --- | -------- |
| Category    | VirtualSwitchingFramework(VSF)          |     |                  |     |          |
| Severity    | Information                             |     |                  |     |          |
| Description | logeventwhenMaterSKUdevicejoinsthestack |     |                  |     |          |
Event ID: 9933
| Message | Peer timeout |     | on interface | <port_id> |     |
| ------- | ------------ | --- | ------------ | --------- | --- |
VirtualSwitchingFramework(VSF)events|405

| Category    | VirtualSwitchingFramework(VSF)                   |     |     |     |
| ----------- | ------------------------------------------------ | --- | --- | --- |
| Severity    | Warning                                          |     |     |     |
| Description | logeventforpeertimeoutasitdidnotreceiveanypacket |     |     |     |
Event ID: 9934
| Message     | Loop detected                  | on  | interface <port_id> |     |
| ----------- | ------------------------------ | --- | ------------------- | --- |
| Category    | VirtualSwitchingFramework(VSF) |     |                     |     |
| Severity    | Warning                        |     |                     |     |
| Description | logeventforloopdetectioninlink |     |                     |     |
Event ID: 9935
Message Interface <port_id> detected a peer with a different VSF handshake
version
| Category | VirtualSwitchingFramework(VSF) |     |     |     |
| -------- | ------------------------------ | --- | --- | --- |
| Severity | Warning                        |     |     |     |
Description logeventwhenpeerswitchisindifferentVSFhandshakeversion
Event ID: 9936
| Message     | Interface                                   | <port_id> | added to VSF | link <link> |
| ----------- | ------------------------------------------- | --------- | ------------ | ----------- |
| Category    | VirtualSwitchingFramework(VSF)              |           |              |             |
| Severity    | Information                                 |           |              |             |
| Description | logeventwheninterfaceaddedtoaparticularlink |           |              |             |
Event ID: 9937
| Message     | Interface                                       | <port_id> | removed from | VSF link <link> |
| ----------- | ----------------------------------------------- | --------- | ------------ | --------------- |
| Category    | VirtualSwitchingFramework(VSF)                  |           |              |                 |
| Severity    | Information                                     |           |              |                 |
| Description | logeventwheninterfaceremovedfromaparticularlink |           |              |                 |
Event ID: 9938
Message Switch with mac <mac_address> not able to autojoin as it is connected
on interface <port> which is a non default autojoin VSF interface
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 406

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when the switch is not able to autojoin as it is connected with a non default VSF
interface

Event ID: 9939

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

Event ID: 9940

Message

Switch with MAC <mac_address> is not autojoin eligible

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when peer switch is not autojoin eligible

Event ID: 9941

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

Event ID: 9942

Message

Switch with MAC <mac_address> failed to autojoin as there is no free
member number available

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log even when switch is not allowed to autojoin because of insufficient resources

Event ID: 9943

Virtual Switching Framework (VSF) events | 407

Message Switch with mac <mac_address> failed to autojoin on link <link>, port
<port>
| Category | VirtualSwitchingFramework(VSF) |     |     |     |     |     |
| -------- | ------------------------------ | --- | --- | --- | --- | --- |
| Severity | Warning                        |     |     |     |     |     |
Description logeventwhentwodifferentswitchesareattemptingtoautojoinbyconnectingtothe
sameVSFlinkonthepeer
Event ID: 9944
Message Switch has VSF configurations present. Force autojoin will not take
into effect. Remove all VSF configurations followed by unconfiguring
|          | and reconfiguring              | force | autojoin | for it | to take into | effect |
| -------- | ------------------------------ | ----- | -------- | ------ | ------------ | ------ |
| Category | VirtualSwitchingFramework(VSF) |       |          |        |              |        |
| Severity | Warning                        |       |          |        |              |        |
Description logeventwhenVSFforceautojoinfailsasVSFconfigurationsexists
Event ID: 9945
| Message     | VSF force                             | autojoin | enabled |     |     |     |
| ----------- | ------------------------------------- | -------- | ------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)        |          |         |     |     |     |
| Severity    | Information                           |          |         |     |     |     |
| Description | logeventwhenVSFforceautojoinisenabled |          |         |     |     |     |
Event ID: 9946
| Message     | VSF force                              | autojoin | disabled |     |     |     |
| ----------- | -------------------------------------- | -------- | -------- | --- | --- | --- |
| Category    | VirtualSwitchingFramework(VSF)         |          |          |     |     |     |
| Severity    | Information                            |          |          |     |     |     |
| Description | logeventwhenVSFforceautojoinisdisabled |          |          |     |     |     |
Event ID: 9947
Message Switch with MAC <mac_addr1> failed to autojoin. Connect the device
|          | <mac_addr2>                    | to member | <mbr_id> | link <link_id> | to proceed |     |
| -------- | ------------------------------ | --------- | -------- | -------------- | ---------- | --- |
| Category | VirtualSwitchingFramework(VSF) |           |          |                |            |     |
| Severity | Warning                        |           |          |                |            |     |
Description logeventwhenmemberconnectedtoanunsupportedinterface
Event ID: 9948
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 408

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

Event ID: 9950

Message

Switch with MAC {mac_addr} failed to autojoin as it is connected on interface {port_id}

which has MACsec configuration

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

log event when a VSF interface is connected to another interface with MACsec
configuration

Event ID: 9951

Message

Bringing down MACsec configured interface {port_id} as it is added to a VSF link. VSF link

and MACsec configurations needs to be removed from the interface {port_id} and VSF

link needs to be reconfigured for it to take into effect

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when an interface with MACsec configuration is added to VSF link

Event ID: 9952

Message

Switchover detected during ISSU operation: "{operation}"

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when ISSU switchover is detected

Virtual Switching Framework (VSF) events | 409

Event ID: 9953

Message

ISSU state failed for member {id} during ISSU operation: "{operation}"

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log to indicate VSF_Member issu_state failed in conductor

Event ID: 9954

Message

VSF member {id} going out of stack during ISSU operation: "{operation}", rebooting the

stack

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log to indicate when standby/member goes out of the stack

Event ID: 9955

Message

Unintentional failover detected during ISSU operation: "{operation}", rebooting the stack

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when unintentional failover occurs during issu in_progress

Event ID: 9956

Message

ISSU complete timer expired. Rebooting switch {id} during ISSU operation: "{operation}"

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when ISSU timer expires before ISSU is complete

Event ID: 9957

Message

Member {member_id} interface {port_id} in VSF link {link} detected a peer {mac_address}

with incompatible product type {prod_type}

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when member attempt to connect to incompatible peer jtypes

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

410

Event ID: 9958

Message

Egress port shape rate {lowest_speed} will be applied for all VSF interfaces

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when port shape is updated with uniform speed

Event ID: 9959

Message

Egress port shape rate {lowest_speed} applied for all VSF interfaces

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event when port shape is updated with uniform speed

Event ID: 9960

Message

Egress port shape rate {lowest_speed} update is failed to apply for interface {if_name}

Category

Virtual Switching Framework (VSF)

Severity

Warning

Description

Log event to capture the QOS applied failures.

Virtual Switching Framework (VSF) events | 411

Chapter 121
VLAN events
VLAN events
ThefollowingaretheeventsrelatedtoVLAN.
Event ID: 2101
| Message  | VLAN <vid>  | created | in hardware |     |
| -------- | ----------- | ------- | ----------- | --- |
| Category | VLAN        |         |             |     |
| Severity | Information |         |             |     |
Description ThislogeventinformstheuserthatVLANiscreatedinHardware
Event ID: 2102
| Message  | Failed | to create VLAN | <vid> in | Hardware |
| -------- | ------ | -------------- | -------- | -------- |
| Category | VLAN   |                |          |          |
| Severity | Error  |                |          |          |
Description ThislogeventinformstheuserthatVLANisnotcreatedinHardware
Event ID: 2103
| Message  | VLAN <vid>  | removed | from hardware |     |
| -------- | ----------- | ------- | ------------- | --- |
| Category | VLAN        |         |               |     |
| Severity | Information |         |               |     |
Description ThislogeventinformstheuserthatVLANisremovedfromHardware
Event ID: 2104
| Message  | Failed | to remove VLAN | <vid> from | hardware |
| -------- | ------ | -------------- | ---------- | -------- |
| Category | VLAN   |                |            |          |
| Severity | Error  |                |            |          |
Description ThislogeventinformstheuserthatVLANisnotremovedfromHardware
Event ID: 2105
412
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message  | Internal    | VLAN <vid> is allocated | to port | <port> |
| -------- | ----------- | ----------------------- | ------- | ------ |
| Category | VLAN        |                         |         |        |
| Severity | Information |                         |         |        |
Description ThislogeventinformsthatinternalVLANisallocatedtoport
Event ID: 2106
| Message     | Failed                                            | to allocate internal | VLAN to port | <port> |
| ----------- | ------------------------------------------------- | -------------------- | ------------ | ------ |
| Category    | VLAN                                              |                      |              |        |
| Severity    | Error                                             |                      |              |        |
| Description | ThislogeventinformsthatinternalVLANisnotallocated |                      |              |        |
Event ID: 2107
Message The mode for port <port> changed from <from> to <to> on VLAN <vid>
| Category | VLAN        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description Thislogeventinformsthattheportmodehaschangedfromoneofthetrunktypesto
accessorviceversa
Event ID: 2108
Message Created Mac based VLAN entry. VLAN <vid> is mapped to client <mac> on
port <port>
| Category | VLAN        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatMacbasedVLANiscreatedinHardware
Event ID: 2109
Message Failed to create Mac based VLAN entry for <mac> with VLAN <vid> on
port <port>
| Category | VLAN  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description ThislogeventinformstheuserthatMacbasedVLANisnotcreatedinHardware
Event ID: 2110
VLANevents|413

Message Deleted Mac based VLAN entry for <mac> with VLAN <vid> on port <port>
| Category | VLAN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisremovedfromHardware
Event ID: 2111
Message Failed to remove Mac based VLAN entry for <mac> with VLAN <vid> on
port <port>
| Category | VLAN  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisnotremovedfromHardware
Event ID: 2112
Message Updated MAC based VLAN entry. VLAN <vid> is mapped to client <mac> on
port <port>
| Category | VLAN        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisupdatedinHardware
Event ID: 2113
Message Failed to update Mac based VLAN entry for <mac> with VLAN <vid> on
port <port>
| Category | VLAN  |     |     |
| -------- | ----- | --- | --- |
| Severity | Error |     |     |
Description ThislogeventinformstheuserthatMACbasedVLANisnotupdatedinHardware
Event ID: 2114
| Message  | Internal VLAN | changed | to <vlan> |
| -------- | ------------- | ------- | --------- |
| Category | VLAN          |         |           |
| Severity | Information   |         |           |
Description ThislogeventinformsthatinternalVLANrangeischanged
Event ID: 2115
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 414

Message VLAN <vid> is down due to pvlan misconfig reason <reason>
| Category | VLAN        |     |     |     |
| -------- | ----------- | --- | --- | --- |
| Severity | Information |     |     |     |
Description ThislogeventinformstheuserthatVLANisdownduetopvlanmisconfig
Event ID: 2116
| Message  | VLAN <vid>  | is recovered | from pvlan | misconfig |
| -------- | ----------- | ------------ | ---------- | --------- |
| Category | VLAN        |              |            |           |
| Severity | Information |              |            |           |
Description ThislogeventinformstheuserthatVLANisrecoveredfrompvlanmisconfig
Event ID: 2117
Message Remote node <remote_node> add for VLAN <vid> on node <local_node>
failed
| Category | VLAN  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description Thislogeventinformstheuserthatremotenodeaddforavlanfailed
Event ID: 2118
Message Remote node <remote_node> remove for VLAN <vid> on node <local_node>
failed
| Category | VLAN  |     |     |     |
| -------- | ----- | --- | --- | --- |
| Severity | Error |     |     |     |
Description Thislogeventinformstheuserthatremotenoderemoveforavlanfailed
Event ID: 2119
Message VLAN translation rule addition failed for port:<port_name>, in_
|          | vlan:<orig_vlan>, | out_vlan:<trans_vlan>, |     | reason=<rst> |
| -------- | ----------------- | ---------------------- | --- | ------------ |
| Category | VLAN              |                        |     |              |
| Severity | LOG_INFO          |                        |     |              |
Description Logsamessagewhenvlantranslationruleadditionfailedinhardware
Event ID: 2120
VLANevents|415

Message

Category

Severity

{intf_name} is now an SVLAN customer-network interface.

VLAN

LOG_INFO

Description

{intf_name} is now an SVLAN customer-network interface.

Event ID: 2121

Message

Category

Severity

'{intf_name} is now an SVLAN provider-network interface.'

VLAN

LOG_INFO

Description

Logs a message when port is part for QinQ provider-network

Event ID: 2122

Message

Category

Severity

'{intf_name} is no longer an SVLAN interface.'

VLAN

LOG_INFO

Description

'Logs a message when port is no longer part for QinQ' event_description_template:

Event ID: 2123

Message

Category

Severity

'Secondary VLAN {sec_vid} of type {sec_type} is associated to primary VLAN {prim_vid}'

VLAN

LOG_INFO

Description

'This log event informs the user that secondary VLAN is associated to a primary VLAN'

Event ID: 2124

Message

'Secondary VLAN {sec_vid} admin state {sec_admin} is ignored. Primary VLAN {prim_vid}

admin state ({prim_admin}) will be applied'

Category

VLAN

Severity

LOG_INFO

Description

'This log event informs the user that secondary VLAN admin state is ignored'

Event ID: 2125

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

416

Message

Category

Severity

'UUFB {port} enabled in hardware'

VLAN

LOG_INFO

Description

'This log event informs the user that UUFB has been enabled on a physical port'

Event ID: 2126

Message

Category

Severity

'UUFB {port} disabled in hardware'

VLAN

LOG_INFO

Description

'This log event informs the user that UUFB has been disabled on a physical port'

VLAN events | 417

Chapter 122
VLAN Interface events
| VLAN Interface | events |     |     |
| -------------- | ------ | --- | --- |
ThefollowingaretheeventsrelatedtoVLANinterface.
Event ID: 1601
Message Vlaninterface vlan<vlan>, failed to create an l3 interface, error:
<err>
| Category    | VLANInterface                         |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Error                                 |     |     |
| Description | logserrorswhilecreatingvlaninterface. |     |     |
Event ID: 1602
| Message     | Vlan Interface             | <interface>, | created |
| ----------- | -------------------------- | ------------ | ------- |
| Category    | VLANInterface              |              |         |
| Severity    | Information                |              |         |
| Description | logstocreatevlaninterface. |              |         |
418
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 123

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

419

Chapter 124
VRF Manager events
| VRF Manager events |     |     |     |
| ------------------ | --- | --- | --- |
ThefollowingaretheeventsrelatedtoVRFManager.
Event ID: 5401
| Message  | Created     | a vrf entity | <vrf_entity> |
| -------- | ----------- | ------------ | ------------ |
| Category | VRFManager  |              |              |
| Severity | Information |              |              |
Event ID: 5402
| Message  | Deleted     | a vrf entity | <vrf_entity> |
| -------- | ----------- | ------------ | ------------ |
| Category | VRFManager  |              |              |
| Severity | Information |              |              |
Event ID: 5403
| Message  | vrf entity | creation | failed <vrf_entity> |
| -------- | ---------- | -------- | ------------------- |
| Category | VRFManager |          |                     |
| Severity | Error      |          |                     |
420
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 125
VRRP events
VRRP events
ThefollowingaretheeventsrelatedtoVRRP.
Event ID: 3701
| Message     | VRRP has been             | enabled | on this router |
| ----------- | ------------------------- | ------- | -------------- |
| Category    | VRRP                      |         |                |
| Severity    | Information               |         |                |
| Description | LogsVRRPglobalenableevent |         |                |
Event ID: 3702
| Message     | VRRP has been              | disabled | on this router |
| ----------- | -------------------------- | -------- | -------------- |
| Category    | VRRP                       |          |                |
| Severity    | Information                |          |                |
| Description | LogsVRRPglobaldisableevent |          |                |
Event ID: 3703
Message <inet_type> virtual router <vrid> on interface <interface> has taken
owner IP
| Category    | VRRP                                      |     |     |
| ----------- | ----------------------------------------- | --- | --- |
| Severity    | Information                               |     |     |
| Description | LogsvirtualrouterhastakencontrolofownerIP |     |     |
Event ID: 3704
Message <inet_type> virtual router <vrid> on interface <interface> has taken
|             | standby IP                                  |     |     |
| ----------- | ------------------------------------------- | --- | --- |
| Category    | VRRP                                        |     |     |
| Severity    | Information                                 |     |     |
| Description | LogsvirtualrouterhastakencontrolofstandbyIP |     |     |
Event ID: 3705
421
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

<inet_type> virtual router <vrid> on interface <interface> lost
standby IP

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

<type> address <address> is added to virtual router <vrid> on
interface <interface>

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

VRRP events | 422

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

<inet_type> virtual router <vrid> advertisement interval has changed
to <value> milliseconds on interface <interface>

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

423

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

VRRP events | 424

Message <inet_type> virtual router <vrid> priority changed to <value> on
|             | interface                                  | <interface> |     |
| ----------- | ------------------------------------------ | ----------- | --- |
| Category    | VRRP                                       |             |     |
| Severity    | Information                                |             |     |
| Description | Logspriorityhasbeenchangedforvirtualrouter |             |     |
Event ID: 3721
Message <inet_type> virtual router <vrid> mode changed to <value> on
|             | interface                           | <interface> |     |
| ----------- | ----------------------------------- | ----------- | --- |
| Category    | VRRP                                |             |     |
| Severity    | Information                         |             |     |
| Description | Logsvirtualroutermodehasbeenchanged |             |     |
Event ID: 3722
Message Track object <track> is associated with <inet_type> virtual router
<vrid>
| Category    | VRRP                                              |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Severity    | Information                                       |     |     |
| Description | Logstrackobjecthasbeenassociatedwithvirtualrouter |     |     |
Event ID: 3723
Message Track object <track> is de-associated from <inet_type> virtual router
<vrid>
| Category | VRRP        |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description Logstrackobjecthasbeende-associatedfromvirtualrouter
Event ID: 3724
| Message     | Track object                  | <track> | is created |
| ----------- | ----------------------------- | ------- | ---------- |
| Category    | VRRP                          |         |            |
| Severity    | Information                   |         |            |
| Description | Logstrackobjecthasbeencreated |         |            |
Event ID: 3725
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 425

| Message     | Track object                  | <track> | is deleted |
| ----------- | ----------------------------- | ------- | ---------- |
| Category    | VRRP                          |         |            |
| Severity    | Information                   |         |            |
| Description | Logstrackobjecthasbeendeleted |         |            |
Event ID: 3726
Message Track object <track> state changed <old_state> to <new_state>
| Category    | VRRP                       |     |     |
| ----------- | -------------------------- | --- | --- |
| Severity    | Information                |     |     |
| Description | Logstrackobjectstatechange |     |     |
Event ID: 3727
Message Track object <track> associated with interface <interface>
| Category    | VRRP                                    |     |     |
| ----------- | --------------------------------------- | --- | --- |
| Severity    | Information                             |     |     |
| Description | Logstrackobjectassociationwithinterface |     |     |
Event ID: 3728
Message <inet_type> virtual router <vrid> recieved packet with authentication
|             | type mismatch                             | on interface | <interface> |
| ----------- | ----------------------------------------- | ------------ | ----------- |
| Category    | VRRP                                      |              |             |
| Severity    | Information                               |              |             |
| Description | Logsauthenticationfailuresonvirtualrouter |              |             |
Event ID: 3729
Message <inet_type> virtual router <vrid> recieved packet with authentication
|             | key mismatch                              | on interface | <interface> |
| ----------- | ----------------------------------------- | ------------ | ----------- |
| Category    | VRRP                                      |              |             |
| Severity    | Information                               |              |             |
| Description | Logsauthenticationfailuresonvirtualrouter |              |             |
Event ID: 3730
VRRPevents|426

Message

Category

Severity

Enabled vrrpv3 checksum for {inet_type} virtual router {vrid} on interface {interface}

VRRP

Information

Description

Logs vrrpv3 checksum has been enabled for virtual router

Event ID: 3731

Message

Category

Severity

Disabled vrrpv3 checksum for {inet_type} virtual router {vrid} on interface {interface}

VRRP

Information

Description

Logs vrrpv3 checksum has been disabled for virtual router

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

427

Chapter 126
VSX Sync events
VSX Sync events
ThefollowingaretheeventsrelatedtoVSXsync.
Event ID: 7601
| Message  | Configuration | sync error: | <id> |
| -------- | ------------- | ----------- | ---- |
| Category | VSXSync       |             |      |
| Severity | Error         |             |      |
Description LogseventwhenerrorinsynchronizingconfigbetweentwoVSXpeers
Event ID: 7602
| Message     | Configuration                             | sync update: | <id> |
| ----------- | ----------------------------------------- | ------------ | ---- |
| Category    | VSXSync                                   |              |      |
| Severity    | Information                               |              |      |
| Description | Logseventwhenthereisanupdateforconfigsync |              |      |
Event ID: 7603
| Message  | Configuration-persistence: |     | <id> |
| -------- | -------------------------- | --- | ---- |
| Category | VSXSync                    |     |      |
| Severity | Information                |     |      |
Description Logseventwhenconfigiscopiedtostartup-configonanyoftheVSXpeer
428
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Chapter 127

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

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

429

Chapter 128
VXLAN events
VXLAN events
ThefollowingaretheeventsrelatedtoVXLAN.
Event ID: 8101
| Message     | VNI id <vni_id>                 | creation failed |
| ----------- | ------------------------------- | --------------- |
| Category    | VXLAN                           |                 |
| Severity    | Error                           |                 |
| Description | EventraisedwhenVNIcreationfails |                 |
Event ID: 8102
| Message     | VNI id <vni_id>           | created |
| ----------- | ------------------------- | ------- |
| Category    | VXLAN                     |         |
| Severity    | Information               |         |
| Description | EventraisedwhenVNIcreated |         |
Event ID: 8103
| Message     | VNI id <vni_id>                 | deletion fails |
| ----------- | ------------------------------- | -------------- |
| Category    | VXLAN                           |                |
| Severity    | Error                           |                |
| Description | EventraisedwhenVNIdeletionfails |                |
Event ID: 8104
| Message     | VNI id <vni_id>             | has been deleted |
| ----------- | --------------------------- | ---------------- |
| Category    | VXLAN                       |                  |
| Severity    | Information                 |                  |
| Description | EventraisedwhenVNIisdeleted |                  |
Event ID: 8105
430
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

| Message     | Vtep-Peer                         | <vtep_peer> | is created |
| ----------- | --------------------------------- | ----------- | ---------- |
| Category    | VXLAN                             |             |            |
| Severity    | Information                       |             |            |
| Description | EventraisedwhenVtep-Peeriscreated |             |            |
Event ID: 8106
| Message     | Vtep-Peer                              | <vtep_peer> | has been deleted |
| ----------- | -------------------------------------- | ----------- | ---------------- |
| Category    | VXLAN                                  |             |                  |
| Severity    | Information                            |             |                  |
| Description | EventraisedwhenVtep-Peerhasbeendeleted |             |                  |
Event ID: 8107
| Message     | Vtep-Peer                             | <vtep_peer> | deletion failed |
| ----------- | ------------------------------------- | ----------- | --------------- |
| Category    | VXLAN                                 |             |                 |
| Severity    | Error                                 |             |                 |
| Description | EventraisedwhenVtep-Peerdeletionfails |             |                 |
Event ID: 8108
Message Access-Port with vlan <vlan_id> and port <port_name> has been created
| Category    | VXLAN                                    |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | EventraisedwhenAccess-Porthasbeencreated |     |     |
Event ID: 8109
Message Access-Port with port <port_name> and vlan <vlan_id> has been deleted
| Category    | VXLAN                                    |     |     |
| ----------- | ---------------------------------------- | --- | --- |
| Severity    | Information                              |     |     |
| Description | EventraisedwhenAccess-Porthasbeendeleted |     |     |
Event ID: 8110
| Message | Vtep-Peer | <vtep> state | is operational |
| ------- | --------- | ------------ | -------------- |
VXLANevents|431

| Category | VXLAN       |     |     |
| -------- | ----------- | --- | --- |
| Severity | Information |     |     |
Description EventraisedwhenVtep-Peerstatusischangedtooperational
Event ID: 8111
| Message  | Vtep-Peer   | <vtep> state | is configuration_error |
| -------- | ----------- | ------------ | ---------------------- |
| Category | VXLAN       |              |                        |
| Severity | Information |              |                        |
Description EventraisedwhenVtep-Peerstatusischangedtoconfigurationerror
Event ID: 8112
| Message  | Vtep-Peer   | <vtep> state | is no_hw_resources |
| -------- | ----------- | ------------ | ------------------ |
| Category | VXLAN       |              |                    |
| Severity | Information |              |                    |
Description EventraisedwhenVtep-Peerstatusischangedtonohardwareresources
Event ID: 8113
| Message  | Vtep-Peer   | <vtep> state | is activating |
| -------- | ----------- | ------------ | ------------- |
| Category | VXLAN       |              |               |
| Severity | Information |              |               |
Description EventraisedwhenVtep-Peerstatusischangedtoactivating
Event ID: 8114
| Message     | Tunnel                                       | <remote_ip> added | to hardware |
| ----------- | -------------------------------------------- | ----------------- | ----------- |
| Category    | VXLAN                                        |                   |             |
| Severity    | Information                                  |                   |             |
| Description | EventraisedwhenaVxLANtunnelisaddedtohardware |                   |             |
Event ID: 8115
| Message  | Tunnel | <remote_ip> deleted | from hardware |
| -------- | ------ | ------------------- | ------------- |
| Category | VXLAN  |                     |               |
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 432

| Severity    | Information                                      |     |     |
| ----------- | ------------------------------------------------ | --- | --- |
| Description | EventraisedwhenaVxLANtunnelisdeletedfromhardware |     |     |
Event ID: 8116
| Message  | Tunnel <remote_ip> | delete deferred |     |
| -------- | ------------------ | --------------- | --- |
| Category | VXLAN              |                 |     |
| Severity | Information        |                 |     |
Description EventraisedwhenaVxLANtunnelhasitsdeletiondeferredbyL3PD
Event ID: 8117
| Message  | Tunnel <remote_ip> | deferred | delete canceled |
| -------- | ------------------ | -------- | --------------- |
| Category | VXLAN              |          |                 |
| Severity | Information        |          |                 |
Description EventraisedwhenaVxLANtunnelhasitsdeferreddeletioncanceled
Event ID: 8118
| Message  | Eventraisedwhenvxlaninterfaceadminstateischanged. |     |     |
| -------- | ------------------------------------------------- | --- | --- |
| Category | VXLAN                                             |     |     |
| Severity | Information                                       |     |     |
Description Eventraisedwhenvxlaninterfaceadminstateischanged.
Event ID: 8119
| Message  | Nexthop {action} | received for | tunnel {vtep_peer} |
| -------- | ---------------- | ------------ | ------------------ |
| Category | VXLAN            |              |                    |
| Severity | Information      |              |                    |
Description Eventraisedwhennexthopoperationadd/delete/modifyistriggeredonavtep-peer
Event ID: 8120
| Message     | Tunnel{vtep_peer}forwarding_stateis{state}        |     |     |
| ----------- | ------------------------------------------------- | --- | --- |
| Category    | VXLAN                                             |     |     |
| Severity    | Information                                       |     |     |
| Description | EventraisedwhenVtep-Peerforwarding_stateischanged |     |     |
VXLANevents|433

Chapter 129
|            |              |        | Zero touch | provisioning | events |
| ---------- | ------------ | ------ | ---------- | ------------ | ------ |
| Zero touch | provisioning | events |            |              |        |
Thefollowingaretheeventsrelatedtozerotouchprovisioning.
| Event ID:   | 8701                                     |                |                |     |     |
| ----------- | ---------------------------------------- | -------------- | -------------- | --- | --- |
| Message     | ZTP service                              | has started    |                |     |     |
| Category    | Zerotouchprovisioning                    |                |                |     |     |
| Severity    | Information                              |                |                |     |     |
| Description | LogeventwhenZTPservicestarts             |                |                |     |     |
| Event ID:   | 8702                                     |                |                |     |     |
| Message     | ZTP service                              | has stopped    |                |     |     |
| Category    | Zerotouchprovisioning                    |                |                |     |     |
| Severity    | Information                              |                |                |     |     |
| Description | LogeventwhenZTPservicestops              |                |                |     |     |
| Event ID:   | 8703                                     |                |                |     |     |
| Message     | ZTP service                              | status changed | to in-progress |     |     |
| Category    | Zerotouchprovisioning                    |                |                |     |     |
| Severity    | Information                              |                |                |     |     |
| Description | LogeventwhenZTPchangestatustoin-progress |                |                |     |     |
| Event ID:   | 8704                                     |                |                |     |     |
| Message     | ZTP service                              | status changed | to success     |     |     |
| Category    | Zerotouchprovisioning                    |                |                |     |     |
| Severity    | Information                              |                |                |     |     |
| Description | LogeventwhenZTPchangestatustosuccess     |                |                |     |     |
| Event ID:   | 8705                                     |                |                |     |     |
434
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries)

Message

ZTP service status changed to failed because of invalid configuration
file

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of invalid config file

Event ID: 8706

Message

ZTP service status changed to failed because of invalid image file

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because of invalid image file

Event ID: 8707

Message

ZTP service status changed to failed because TFTP info is not
available

Category

Zero touch provisioning

Severity

Warning

Description

Log event when ZTP fails because no TFTP info is available

Event ID: 8708

Message

ZTP service status changed to failed because TFTP server is not
reachable

Category

Zero touch provisioning

Severity

Warning

Description

Log event when ZTP fails because TFTP server is not reachable

Event ID: 8709

Message

ZTP service status changed to failed because of non-default startup
configuration

Category

Zero touch provisioning

Severity

Information

Description

Log event when ZTP failed because of non-default startup config

Event ID: 8710

Zero touch provisioning events | 435

Message ZTP service status changed to failed because running configuration is
modified
| Category | Zerotouchprovisioning |     |     |
| -------- | --------------------- | --- | --- |
| Severity | Information           |     |     |
Description LogeventwhenZTPfailedbecauseofmodifiedrunningconfig
Event ID: 8711
Message ZTP service status changed to failed because of timeout
| Category    | Zerotouchprovisioning                 |     |     |
| ----------- | ------------------------------------- | --- | --- |
| Severity    | Warning                               |     |     |
| Description | LogeventwhenZTPfailedbecauseoftimeout |     |     |
Event ID: 8712
| Message  | ZTP: Image            | file not provided |     |
| -------- | --------------------- | ----------------- | --- |
| Category | Zerotouchprovisioning |                   |     |
| Severity | Information           |                   |     |
Description LogsrelatedtoZTPconfigurations-imagefilenotprovided
Event ID: 8713
| Message  | ZTP: Config           | file not | provided |
| -------- | --------------------- | -------- | -------- |
| Category | Zerotouchprovisioning |          |          |
| Severity | Information           |          |          |
Description Logsrelatedtoztpconfigurations-configfilenotprovided
Event ID: 8714
| Message  | ZTP: TFTP             | server option | not provided |
| -------- | --------------------- | ------------- | ------------ |
| Category | Zerotouchprovisioning |               |              |
| Severity | Information           |               |              |
Description Logsrelatedtoztpconfigurations-TFTPservernamenotprovided
Event ID: 8715
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 436

| Message  | ZTP: Exceeded         | max path | length of | TFTP server |     |
| -------- | --------------------- | -------- | --------- | ----------- | --- |
| Category | Zerotouchprovisioning |          |           |             |     |
| Severity | Error                 |          |           |             |     |
Description Logsrelatedtoztpconfigurations-pathlengthexceededofTFTPservername
Event ID: 8718
| Message     | ZTP: Received                                 | TFTP server | <tftp_ip> | from dhcp | server |
| ----------- | --------------------------------------------- | ----------- | --------- | --------- | ------ |
| Category    | Zerotouchprovisioning                         |             |           |           |        |
| Severity    | Information                                   |             |           |           |        |
| Description | Logsrelatedtoztpconfigurations-TFTPIPreceived |             |           |           |        |
Event ID: 8719
Message ZTP: Received image file <image_file> from dhcp server
| Category | Zerotouchprovisioning |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Severity | Information           |     |     |     |     |
Description Logsrelatedtoztpconfigurations-Imagefilenamereceived
Event ID: 8720
Message ZTP: Received config file <config_file> from dhcp server
| Category | Zerotouchprovisioning |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Severity | Information           |     |     |     |     |
Description Logsrelatedtoztpconfigurations-Configfilenamereceived
Event ID: 8721
Message ZTP: Received Aruba Central location <central_location> from DHCP
server
| Category | Zerotouchprovisioning |     |     |     |     |
| -------- | --------------------- | --- | --- | --- | --- |
| Severity | Information           |     |     |     |     |
Description Logsrelatedtoztpconfigurations-ArubaCentralFQDNorIPv4received
Event ID: 8723
Zerotouchprovisioningevents|437

| Message  | ZTP: Aruba            | Central location | option not | provided |
| -------- | --------------------- | ---------------- | ---------- | -------- |
| Category | Zerotouchprovisioning |                  |            |          |
| Severity | Information           |                  |            |          |
Description Logsrelatedtoztpconfigurations-ArubaCentralFQDNorIPv4notprovided
Event ID: 8724
Message ZTP: Received HTTP proxy location <http_proxy_location> from DHCP
server.
| Category | Zerotouchprovisioning |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description Logsrelatedtoztpconfigurations-ArubaHTTPproxyFQDNorIPv4received
Event ID: 8726
Message ZTP: HTTP proxy location was not received in the DHCP offer.
| Category | Zerotouchprovisioning |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Information           |     |     |     |
Description Logsrelatedtoztpconfigurations-HTTPProxyFQDNorIPv4notprovided
Event ID: 8727
Message ZTP service status changed to failed because <filename> file download
|          | encountered           | unexpected | error. |     |
| -------- | --------------------- | ---------- | ------ | --- |
| Category | Zerotouchprovisioning |            |        |     |
| Severity | Critical              |            |        |     |
Description LogeventwhenZTPfailsbecauseofunexpectederrorinconfig/imagefiledownload
Event ID: 8728
Message ZTP service status changed to failed because <filename> file did not
get downloaded.
| Category | Zerotouchprovisioning |     |     |     |
| -------- | --------------------- | --- | --- | --- |
| Severity | Critical              |     |     |     |
Description LogeventwhenZTPfailsbecauseofconfig/imagefiledownloaderror
Event ID: 8729
AOS-CX10.13EventLogMessageReferenceGuide|(AllSwitchSeries) 438

Message

ZTP service status changed to failed because the downloaded
configuration could not be copied to start-up configuration.

Category

Zero touch provisioning

Severity

Critical

Description

Log event when ZTP fails because downloaded config did not get copied to start-up
config

Event ID: 8730

Message

ZTP service status changed to failed because <filename> file download
encountered unexpected error. Reason: <reason>

Category

Zero touch provisioning

Severity

Error

Description

Log event when ZTP fails because of unexpected error in config file download

Event ID: 8731

Message

Category

Severity

Received Alternative Aruba central location {alt_aruba_central_loc} from dhcp server.

Zero touch provisioning

Information

Description

Log event when ZTP receives the Alternative Aruba central location.

Zero touch provisioning events | 439

Chapter 130

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1-800-943-4526 (US & Canada Toll-Free Number)

+1-408-754-1200 (Primary - Toll Number)

+1-650-385-6582 (Backup - Toll Number - Use only when all other

numbers are not working)

International telephone

https://www.arubanetworks.com/support-services/contact-
support/

Be sure to collect the following information before contacting Support:

n Technical support registration number (if applicable)

n Product name, model or version, and serial number

n Operating system name and version

n Firmware version

n Error messages

n Product-specific reports and logs

n Add-on products or components

n Third-party products or components

Other useful sites

Other websites that can be used to find information:

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

AOS-CX Software
Technical Update
channel on

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

Videos on new features introduced in this release:

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

440

YouTube.

HPE Aruba
Networking
Hardware
Documentation
and Translations
Portal

HPE Aruba
Networking
software

Software
licensing and
Feature Packs

End-of-Life
information

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

https://networkingsupport.hpe.com/downloads

https://licensemanagement.hpe.com/

https://www.arubanetworks.com/support-services/end-of-life/

Accessing Updates

You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

https://networkingsupport.hpe.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My
Networking, where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to
the Hewlett Packard Enterprise Support Center More Information on Access to Support Materials
page:

https://support.hpe.com/portal/site/hpsc/aae/home/

Access to some updates might require product entitlement when accessed through the Hewlett Packard
Enterprise Support Center. You must have an HP Passport set up with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://networkingsupport.hpe.com/notifications/subscriptions (requires an active HPE Aruba
Networking support account to manage subscriptions). Security notices are viewable without a
networking support account.

Warranty information

To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Support and Other Resources | 441

Regulatory Information

To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs,
product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation feedback

Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.13 Event Log Message Reference Guide | (All Switch Series)

442