AOS-CX 10.10 IP Services
Guide

83xx, 9300, 10000 Switch Series

Published: August 2022

Version: 2

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

Acknowledgments

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in
the United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

3

Contents
| About this                          | document                            | 10  |
| ----------------------------------- | ----------------------------------- | --- |
| Applicableproducts                  |                                     | 10  |
| Latestversionavailableonline        |                                     | 10  |
| Commandsyntaxnotationconventions    |                                     | 10  |
| Abouttheexamples                    |                                     | 11  |
| Identifyingswitchportsandinterfaces |                                     | 11  |
| IRDP                                |                                     | 13  |
| ConfiguringIRDP                     |                                     | 14  |
| IRDPcommands                        |                                     | 15  |
|                                     | diag-dumpirdpbasic                  | 15  |
|                                     | ipirdp                              | 15  |
|                                     | ipirdpholdtime                      | 16  |
|                                     | ipirdpmaxadvertinterval             | 17  |
|                                     | ipirdpminadvertinterval             | 18  |
|                                     | ipirdppreference                    | 19  |
|                                     | showipirdp                          | 20  |
| IPv6 Router                         | Advertisement                       | 22  |
| ConfiguringIPv6RA                   |                                     | 22  |
| IPv6RAscenario                      |                                     | 24  |
| IPv6RAcommands                      |                                     | 25  |
|                                     | ipv6address<global-unicast-address> | 25  |
|                                     | ipv6addressautoconfig               | 25  |
|                                     | ipv6addresslink-local               | 26  |
|                                     | ipv6ndcache-limit                   | 27  |
|                                     | ipv6nddadattempts                   | 28  |
|                                     | ipv6ndhop-limit                     | 28  |
|                                     | ipv6ndmtu                           | 29  |
|                                     | ipv6ndns-interval                   | 30  |
|                                     | ipv6ndprefix                        | 30  |
|                                     | ipv6ndradnssearch-list              | 32  |
|                                     | ipv6ndradnsserver                   | 33  |
|                                     | ipv6ndralifetime                    | 34  |
|                                     | ipv6ndramanaged-config-flag         | 34  |
|                                     | ipv6ndramax-interval                | 35  |
|                                     | ipv6ndramin-interval                | 36  |
|                                     | ipv6ndraother-config-flag           | 37  |
|                                     | ipv6ndrareachable-time              | 38  |
|                                     | ipv6ndraretrans-timer               | 38  |
|                                     | ipv6ndroute                         | 39  |
|                                     | ipv6ndrouter-preference             | 40  |
|                                     | ipv6ndsuppress-ra                   | 41  |
|                                     | showipv6ndglobaltraffic             | 42  |
|                                     | showipv6ndinterface                 | 43  |
|                                     | showipv6ndinterfaceprefix           | 45  |
|                                     | showipv6ndinterfaceroute            | 46  |
|                                     | showipv6ndradnssearch-list          | 47  |
|                                     | showipv6ndradnsserver               | 48  |
4
AOS-CX10.10IPServicesGuide| (83xx,10000SwitchSeries)

sFlow

sFlow agent
Configuring the sFlow agent
sFlow scenario
sFlow scenario 2
sFlow agent commands

clear sflow statistics
sflow
sflow agent-ip
sflow collector
sflow disable
sflow header-size
sflow max-datagram-size
sflow mode
sflow polling
sflow sampling
show sflow

DHCP

DHCP client

DHCP client commands

ip dhcp
show ip dhcp

DHCP relay agent

DHCPv4 relay agent

Configuring the DHCPv4 relay agent
DHCPv4 relay scenario 1
DHCPv4 relay scenario 2
DHCPv4 relay scenario 3
DHCPv4 relay commands

DHCPv6 relay agent

Configuring the DHCPv6 relay agent
DHCPv6 relay scenario 1
DHCPv6 relay scenario 2
DHCP relay (IPv6) commands

DHCP server

Configuring a DHCPv4 server on a VRF
Configuring the DHCPv6 server on a VRF
DHCP server IPv4 commands

authoritative
bootp
clear dhcp-server leases
default-router
dhcp-server external-storage
dhcp-server vrf
disable
dns-server
domain-name
enable
http-proxy
lease
netbios-name-server
netbios-node-type
option
pool
range

50
50
51
52
53
56
56
57
58
59
60
60
61
62
63
64
65

67
67
67
67
68
69
69
71
72
73
74
76
86
86
87
88
89
94
94
96
97
97
98
99
100
101
102
103
103
104
105
106
107
108
109
110
111
112

| 5

show dhcp-server
static-bind

DHCP server IPv6 commands

authoritative
clear dhcpv6-server leases
dhcv6p-server external-storage
dhcpv6-server vrf
disable
dns-server
enable
lease
option
pool
range
show dhcpv6-server
static-bind

DHCP snooping

DHCPv6 guard
DHCP server interoperation
DHCPv4 snooping conditions for dropping DHCPv4 packets
Protocol details
Configuring DHCPv4 and v6 snooping over VXLAN overlay
DHCPv4 snooping commands

clear dhcpv4-snooping binding
clear dhcpv4-snooping statistics
dhcpv4-snooping
dhcpv4-snooping (in config-vlan context)
dhcpv4-snooping allow-overwrite-binding
dhcpv4-snooping authorized-server
dhcpv4-snooping event-log client
dhcpv4-snooping external-storage
dhcpv4-snooping flash-storage
dhcpv4-snooping max-bindings
dhcpv4-snooping option 82
dhcpv4-snooping static-attributes
dhcpv4-snooping trust
dhcpv4-snooping tunnel vxlan trust
dhcpv4-snooping verify mac
show dhcpv4-snooping
show dhcpv4-snooping binding
show dhcpv4-snooping statistics

DHCPv6 snooping commands

clear dhcpv6-snooping binding
clear dhcpv6-snooping guard-policy statistics
clear dhcpv6-snooping statistics
dhcpv6-snooping
dhcpv6-snooping (in config-vlan context)
dhcpv6-snooping authorized-server
dhcpv6-snooping event-log client
dhcpv6-snooping external-storage
dhcpv6-snooping flash-storage
dhcpv6-snooping max-bindings
dhcpv6-snooping trust
dhcpv6-snooping tunnel vxlan trust
match server access-list

113
115
116
116
117
118
119
120
121
122
122
123
124
125
126
128

130
130
130
131
131
132
132
132
133
134
134
135
136
137
138
139
140
141
143
143
144
145
146
147
149
150
150
151
152
152
153
154
155
156
157
158
159
160
160

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

6

matchclientprefix-list 161
preference 162
showdhcpv6-snooping 163
showdhcpv6-snoopingbinding 164
dhcpv6-snoopingguard-policy 165
showdhcpv6-snoopingguard-policy 166
showdhcpv6-snoopingguard-policyinterface 168
showdhcpv6-snoopingguard-policyvlan 169
showdhcpv6-snoopingstatistics 169
| ND snooping                                       |     | 171 |
| ------------------------------------------------- | --- | --- |
| Overview(appliestothe8325,9300,10000SwitchSeries) |     | 171 |
| Overview(appliestothe8360SwitchSeries)            |     | 171 |
| NDsnoopingcommands                                |     | 172 |
clearnd-snoopingbinding 172
clearnd-snoopingra-guard-policystatistics 173
clearnd-snoopingstatistics 174
nd-snooping 174
nd-snooping(inconfig-vlancontext) 175
nd-snoopingmac-check 176
nd-snoopingprefix-list 177
nd-snoopingmax-bindings 178
nd-snoopingnd-guard 179
nd-snoopingra-guard 179
nd-snoopingra-drop 181
nd-snoopingtrust 181
shownd-snooping 182
shownd-snoopingbindings 184
shownd-snoopingprefix-list 185
shownd-snoopingstatistics 186
| RAguardpolicycommands |     | 187 |
| --------------------- | --- | --- |
hoplimit 187
ipv6nd-snoopingra-guardpolicy 189
managed-config-flag 189
matchaccess-list 190
matchprefix-list 191
nd-snoopingra-guardattach-policy 192
other-config-flag 194
router-preference 195
shownd-snoopingra-guardinterface 196
shownd-snoopingra-guardpolicy 197
shownd-snoopingra-guardvlan 198
| IPv6 destination             | guard | 199 |
| ---------------------------- | ----- | --- |
| IPv6destinationguardcommands |       | 199 |
clearipv6destination-guardstatisticsvlan 199
ipv6destinationguard 200
showipv6destination-guardstatisticsvlan 200
showipv6destination-guard 201
| IP Tunnels                                            |     | 203 |
| ----------------------------------------------------- | --- | --- |
| ConfiguringanIPtunnel                                 |     | 204 |
| CreatingaGREtunnelfortraversingapublicnetwork         |     | 204 |
| CreatingtwoGREtunnelstodifferentdestinationaddresses  |     | 206 |
| CreatinganIPv6inIPv4tunnelfortraversingapublicnetwork |     | 208 |
| CreatinganIPv6inIPv6tunnelfortraversingapublicnetwork |     | 209 |
|7

| IPtunnelscommands               |                                   |         |          |        | 211 |
| ------------------------------- | --------------------------------- | ------- | -------- | ------ | --- |
|                                 | description                       |         |          |        | 211 |
|                                 | destinationip                     |         |          |        | 212 |
|                                 | destinationipv6                   |         |          |        | 213 |
|                                 | interfacetunnel                   |         |          |        | 214 |
|                                 | ipaddress                         |         |          |        | 216 |
|                                 | ipv6address                       |         |          |        | 217 |
|                                 | ipmtu                             |         |          |        | 218 |
|                                 | showinterfacetunnel               |         |          |        | 219 |
|                                 | showrunning-configinterfacetunnel |         |          |        | 221 |
|                                 | shutdown                          |         |          |        | 222 |
|                                 | sourceip                          |         |          |        | 223 |
|                                 | sourceipv6                        |         |          |        | 224 |
|                                 | ttl                               |         |          |        | 225 |
|                                 | vrfattach                         |         |          |        | 226 |
| IP Source                       | Lockdown                          |         |          |        | 228 |
| IPv4sourcelockdowncommands      |                                   |         |          |        | 228 |
|                                 | ipv4source-binding                |         |          |        | 228 |
|                                 | ipv4source-lockdown               |         |          |        | 229 |
|                                 | ipv4source-lockdownhardwareretry  |         |          |        | 230 |
|                                 | showipv4source-binding            |         |          |        | 231 |
|                                 | showipv4source-lockdown           |         |          |        | 232 |
| IPv6sourcelockdowncommands      |                                   |         |          |        | 234 |
|                                 | ipv6source-binding                |         |          |        | 234 |
|                                 | ipv6source-lockdown               |         |          |        | 235 |
|                                 | ipv6source-lockdownhardwareretry  |         |          |        | 236 |
|                                 | showipv6source-binding            |         |          |        | 237 |
|                                 | showipv6source-lockdown           |         |          |        | 238 |
| Internet                        | Control                           | Message | Protocol | (ICMP) | 241 |
| ICMPmessagetypes                |                                   |         |          |        | 241 |
| WhenICMPmessagesaresent         |                                   |         |          |        | 241 |
| ICMPredirectmessages            |                                   |         |          |        | 242 |
| WhenICMPredirectmessagesaresent |                                   |         |          |        | 242 |
| ICMPcommands                    |                                   |         |          |        | 242 |
|                                 | ipicmpredirect                    |         |          |        | 242 |
|                                 | ipicmpthrottle                    |         |          |        | 243 |
|                                 | ipicmpunreachable                 |         |          |        | 244 |
| DNS                             |                                   |         |          |        | 245 |
| DNSclient                       |                                   |         |          |        | 245 |
| ConfiguringtheDNSclient         |                                   |         |          |        | 245 |
| DNSclientcommands               |                                   |         |          |        | 246 |
|                                 | ipdnsdomain-list                  |         |          |        | 246 |
|                                 | ipdnsdomain-name                  |         |          |        | 247 |
|                                 | ipdnshost                         |         |          |        | 248 |
|                                 | ipdnsserveraddress                |         |          |        | 249 |
|                                 | showipdns                         |         |          |        | 250 |
| ARP                             |                                   |         |          |        | 253 |
| ConfiguringproxyARP             |                                   |         |          |        | 254 |
| ConfiguringlocalproxyARP        |                                   |         |          |        | 254 |
| ARPcommands                     |                                   |         |          |        | 255 |
|                                 | arpinspectiontrust                |         |          |        | 255 |
|                                 | arpprocess-grat-arp               |         |          |        | 255 |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 8

|                       | arpipv4mac                  |           | 257 |
| --------------------- | --------------------------- | --------- | --- |
|                       | cleararp                    |           | 257 |
|                       | iplocal-proxy-arp           |           | 258 |
|                       | ipv6neighbormac             |           | 259 |
|                       | ipproxy-arp                 |           | 260 |
|                       | showarp                     |           | 261 |
|                       | showarpinspectioninterface  |           | 262 |
|                       | showarpinspectionstatistics |           | 263 |
|                       | showarpstate                |           | 263 |
|                       | showarpsummary              |           | 264 |
|                       | showarptimeout              |           | 266 |
|                       | showarpvrf                  |           | 267 |
|                       | showipv6neighbors           |           | 268 |
|                       | showipv6neighborsstate      |           | 269 |
| Network               | Load Balancing              | (NLB)     | 271 |
| NLBcommands           |                             |           | 271 |
|                       | arpipv4mac                  |           | 271 |
|                       | showarp                     |           | 272 |
|                       | showipigmpsnoopingvlangroup |           | 273 |
| Support               | and Other                   | Resources | 274 |
| AccessingArubaSupport |                             |           | 274 |
| AccessingUpdates      |                             |           | 275 |
|                       | ArubaSupportPortal          |           | 275 |
|                       | MyNetworking                |           | 275 |
| WarrantyInformation   |                             |           | 275 |
| RegulatoryInformation |                             |           | 275 |
| DocumentationFeedback |                             |           | 276 |
|9

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C, JL704C, JL705C,
JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n Aruba 9300 Switch Series (R9A29A, R9A30A, R8Z96A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example-text

Usage

Identifies commands and their options and operands, code examples,
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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

10

Convention

Usage

|

{ }

[ ]

… or

...

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

About this document | 11

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 83xx, 9300, and 10000 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

12

Chapter 2

IRDP

IRDP

ICMP Router Discovery Protocol (IRDP), an extension of the ICMP, is independent of any routing
protocol. It allows hosts to discover the IP addresses of neighboring routers that can act as default
gateways to reach devices on other IP networks.

IRDP operation

IRDP uses the following types of ICMP messages:

n Router advertisement (RA): Sent by a router to advertise IP addresses (including the primary and

secondary IP addresses) and preference.

n Router solicitation (RS): Sent by a host to request the IP addresses of routers on the subnet.

An interface with IRDP enabled periodically broadcasts or multicasts an RA message to advertise its IP
addresses. A receiving host adds the IP addresses to its routing table, and selects the IP address with the
highest preference as the default gateway.

When a host attached to the subnet starts up, the host multicasts an RS message to request immediate
advertisements. If the host does not receive any advertisements, it retransmits the RS several times. If
the host does not discover the IP addresses of neighboring routers because of network problems, the
host can still discover them from periodic RAs.

IRDP allows hosts to discover neighboring routers, but it does not suggest the best route to a
destination. If a host sends a packet to a router that is not the best next hop, the host will receive an
ICMP redirect message from the router.

IP address preference

Every IP address advertised in RAs has a preference value. A larger preference value represents a higher
preference. The IP address with the highest preference is selected as the default gateway address.

You can specify the preference for IP addresses to be advertised on a router interface.

An address with the minimum preference value (-2147483648) will not be used as a default gateway
address.

Lifetime of an IP address

An RA contains a lifetime field that specifies the lifetime of advertised IP addresses. If the host does not
receive a new RA for an IP address within the address lifetime, the host removes the route entry.

All the IP addresses advertised by an interface have the same lifetime.

Advertising interval

A router interface with IRDP enabled sends out RAs randomly between the minimum and maximum
advertising intervals. This mechanism prevents the local link from being overloaded by a large number
of RAs sent simultaneously from routers.

As a best practice, shorten the advertising interval on a link that suffers high packet loss rates

Destination address of RA

An RA uses either of the following destination IP addresses:

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

13

n Broadcast address 255.255.255.255.

n Multicast address 224.0.0.1, which identifies all hosts on the local link.

By default, the destination IP address of an RA is the multicast address. If all listening hosts in a local
area network support IP multicast, specify 224.0.0.1 as the destination IP address.

Proxy-advertised IP addresses

By default, an interface advertises its primary and secondary IP addresses. You can specify IP addresses
of other gateways for an interface to proxy-advertise.

VRF support

In IP-based computer networks, virtual routing and forwarding (VRF) is a technology that allows multiple
instances of a routing table to co-exist within the same router at the same time. Because the routing
instances are independent, the same or overlapping IP addresses can be used without conflicting with
each other.

IRDP is VRF aware. As the router advertisements and solicit processing occurs on the interface, packet is
through the interface and corresponding VRF.

VSX synchronization

IRDP supports VSX synchronization. For more information on using VSX, see the Virtual Switching
Extension (VSX) Guide for your switch and software version

Configuring IRDP

Prerequisites

A layer 3 interface.

Procedure

1. Enable IRDP on an interface with the command ip irdp.

2. Set the maximum hold time with the command ip irdp holdtime.

3. Set the maximum router advertisement interval with the command ip irdp maxadvertinterval.

4. Set the minimum router advertisement interval with the command ip irdp minadvertinterval.

5. Set the IRDP preference level with the command ip irdp preference.

6. Review IRDP configuration settings with the command show ip irdp.

Example

This example creates the following configuration:

n Enables IRDP on the layer 3 interface 1/1/1 with packet type set to broadcast.

n Sets the hold time to 5000 seconds.

n Sets the advertisement interval to 30 seconds.

n Sets the minimum advertisement interval to 25 seconds.

n Sets the IRDP preference level to 25.

switch(config)# interface 1/1/1
switch(config-if)# ip irdp broadcast

IRDP | 14

| switch(config-if)# |     |     | ip irdp holdtime | 5000 |     |
| ------------------ | --- | --- | ---------------- | ---- | --- |
switch(config-if)#
|                    |     |     | ip irdp maxadvertinterval |     | 30  |
| ------------------ | --- | --- | ------------------------- | --- | --- |
| switch(config-if)# |     |     | ip irdp minadvertinterval |     | 25  |
| switch(config-if)# |     |     | ip irdp preference        | 25  |     |
IRDP commands
| diag-dump      | irdp  | basic |     |     |     |
| -------------- | ----- | ----- | --- | --- | --- |
| diag-dump irdp | basic |       |     |     |     |
Description
DisplaysdiagnosticinformationforIRDP.
Example
| switch# | diag-dump | irdp | basic |     |     |
| ------- | --------- | ---- | ----- | --- | --- |
=========================================================================
| [Start] | Feature | irdp | Time : Thu | Jun 8 09:50:28 | 2017 |
| ------- | ------- | ---- | ---------- | -------------- | ---- |
=========================================================================
-------------------------------------------------------------------------
| [Start] | Daemon | hpe-rdiscd |     |     |     |
| ------- | ------ | ---------- | --- | --- | --- |
-------------------------------------------------------------------------
| Interface: | 1/1/1 | (state | : Up) |     |     |
| ---------- | ----- | ------ | ----- | --- | --- |
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
| Router IPs | -     | 192.168.1.2, |       |     |     |
| ---------- | ----- | ------------ | ----- | --- | --- |
| Interface: | 1/1/2 | (state       | : Up) |     |     |
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
| Router IPs | -   | 192.168.2.2, |     |     |     |
| ---------- | --- | ------------ | --- | --- | --- |
-------------------------------------------------------------------------
| [End] Daemon |     | hpe-rdiscd |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- |
-------------------------------------------------------------------------
=========================================================================
| [End] Feature |     | irdp |     |     |     |
| ------------- | --- | ---- | --- | --- | --- |
=========================================================================
| Diagnostic     | dump        | captured | for feature | irdp         |     |
| -------------- | ----------- | -------- | ----------- | ------------ | --- |
| Command        | History     |          |             |              |     |
| Release        |             |          |             | Modification |     |
| 10.07orearlier |             |          |             | --           |     |
| Command        | Information |          |             |              |     |
| Platforms      | Command     |          | context     | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
ip irdp
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 15

| ip irdp [broadcast | | multicast] |     |     |
| ------------------ | ------------ | --- | --- |
no ip irdp
Description
EnablesIRDPonaninterfaceandspecifiesthepackettypethatisusedtosendadvertisements.By
default,thepackettypeissettomulticast.IRDPisonlysupportedonlayer3interfaces.
ThenoformofthiscommanddisablesIRDPonaninterface.
| Parameter |     |     | Description                                        |
| --------- | --- | --- | -------------------------------------------------- |
| broadcast |     |     | AdvertisementsaresentasbroadcastpacketstoIPaddress |
255.255.255.255.
multicast
Advertisementsaresentasmulticastpacketstothemulticast
groupwithIPaddress24.0.0.1.Default.
Examples
EnablingIRDPoninterface1/1/1withpackettypesettothedefaultvalue(multicast).
| switch(config)#    | interface | 1/1/1   |     |
| ------------------ | --------- | ------- | --- |
| switch(config-if)# |           | ip irdp |     |
EnablingIRDPoninterface1/1/1withpackettypesettobroadcast.
| switch(config)#    | interface | 1/1/1             |     |
| ------------------ | --------- | ----------------- | --- |
| switch(config-if)# |           | ip irdp broadcast |     |
DisablingIRDP.
| switch(config)#     | interface | 1/1/1      |              |
| ------------------- | --------- | ---------- | ------------ |
| switch(config-if)#  |           | no ip irdp |              |
| Command History     |           |            |              |
| Release             |           |            | Modification |
| 10.07orearlier      |           |            | --           |
| Command Information |           |            |              |
| Platforms           | Command   | context    | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip irdp holdtime    |        |     |     |
| ------------------- | ------ | --- | --- |
| ip irdp holdtime    | <TIME> |     |     |
| no ip irdp holdtime | <TIME> |     |     |
Description
IRDP|16

Specifiesthemaximumamountoftimethehostwillconsideranadvertisementtobevaliduntilanewer
advertisementarrives.Whenanewadvertisementarrives,holdtimeisreset.Holdtimemustbegreater
thanorequaltothemaximumadvertisementinterval.Therefore,iftheholdtimeforanadvertisement
expires,thehostcanreasonablyconcludethattherouterinterfacethatsenttheadvertisementisno
longeravailable.Thedefaultholdtimeisthreetimesthemaximumadvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumamountoftimethehostwillconsideran
advertisementtobevaliduntilaneweradvertisementarrivesandupdateittothedefaultvalue.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<TIME>
Specifiesthelifetimeofrouteradvertisementssentfromthis
interface.Range:4to9000seconds.Default:1800seconds.
Example
Settingtheholdtimeforinterface1/1/1to5000seconds:
| switch(config)#    |     | interface | 1/1/1   |          |      |
| ------------------ | --- | --------- | ------- | -------- | ---- |
| switch(config-if)# |     |           | ip irdp | holdtime | 5000 |
Removingthetheholdtimeforinterface1/1/1to5000seconds:
| switch(config)#    |             | interface | 1/1/1      |          |              |
| ------------------ | ----------- | --------- | ---------- | -------- | ------------ |
| switch(config-if)# |             |           | no ip irdp | holdtime | 5000         |
| Command            | History     |           |            |          |              |
| Release            |             |           |            |          | Modification |
| 10.07orearlier     |             |           |            |          | --           |
| Command            | Information |           |            |          |              |
| Platforms          | Command     |           | context    |          | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip irdp    | maxadvertinterval |     |        |     |     |
| ---------- | ----------------- | --- | ------ | --- | --- |
| ip irdp    | maxadvertinterval |     | <TIME> |     |     |
| no ip irdp | maxadvertinterval |     | <TIME> |     |     |
Description
Specifiesthemaximumrouteradvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumrouteradvertisementintervaland
revertstothedefaultvalue.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 17

| Parameter |     |     |     | Description                                       |     |
| --------- | --- | --- | --- | ------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiesthemaximumtimeallowedbetweenthesendingof |     |
unsolicitedrouteradvertisements.Range:4to1800seconds.
Default:600seconds.
Example
Settingtheadvertisementintervalforinterface1/1/1to30seconds:
| switch(config)#    |     | interface | 1/1/1   |                   |     |
| ------------------ | --- | --------- | ------- | ----------------- | --- |
| switch(config-if)# |     |           | ip irdp | maxadvertinterval | 30  |
Removingtheadvertisementintervalforinterface1/1/1to30seconds:
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|                |             |     | no ip irdp | maxadvertinterval | 30  |
| -------------- | ----------- | --- | ---------- | ----------------- | --- |
| Command        | History     |     |            |                   |     |
| Release        |             |     |            | Modification      |     |
| 10.07orearlier |             |     |            | --                |     |
| Command        | Information |     |            |                   |     |
| Platforms      | Command     |     | context    | Authority         |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip irdp    | minadvertinterval |     |        |     |     |
| ---------- | ----------------- | --- | ------ | --- | --- |
| ip irdp    | minadvertinterval |     | <TIME> |     |     |
| no ip irdp | minadvertinterval |     | <TIME> |     |     |
Description
Specifiestheminimumamountoftimetheswitchwaitsbetweensendingrouteradvertisements.By
default,thisvalueisautomaticallysetbytheswitchtobe75%ofthevalueconfiguredformaximum
routeradvertisementinterval.Usethiscommandtooverridetheautomaticallyconfiguredvalue.
Thenoformofthiscommandremovesthespecifiedminimumamountoftimetheswitchwaits
betweensendingrouteradvertisementsandrevertstothedefaultvalue.
| Parameter |     |     |     | Description                                       |     |
| --------- | --- | --- | --- | ------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiestheminimumtimeallowedbetweenthesendingof |     |
unsolicitedrouteradvertisements.Range:3to1800seconds.
Default:450seconds(75%ofthedefaultvalueformaximum
routeradvertisementinterval).
Example
IRDP|18

Settingtheminimumadvertisementintervalforinterface1/1/1to25seconds:
| switch(config)#    |     | interface | 1/1/1   |                   |     |     |
| ------------------ | --- | --------- | ------- | ----------------- | --- | --- |
| switch(config-if)# |     |           | ip irdp | minadvertinterval |     | 25  |
Removingtheminimumadvertisementintervalforinterface1/1/1to25seconds:
| switch(config)#    |             | interface | 1/1/1      |                   |     |     |
| ------------------ | ----------- | --------- | ---------- | ----------------- | --- | --- |
| switch(config-if)# |             |           | no ip irdp | minadvertinterval |     | 25  |
| Command            | History     |           |            |                   |     |     |
| Release            |             |           |            | Modification      |     |     |
| 10.07orearlier     |             |           |            | --                |     |     |
| Command            | Information |           |            |                   |     |     |
| Platforms          | Command     |           | context    | Authority         |     |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip irdp    | preference |         |         |     |     |     |
| ---------- | ---------- | ------- | ------- | --- | --- | --- |
| ip irdp    | preference | <LEVEL> |         |     |     |     |
| no ip irdp | preference |         | <LEVEL> |     |     |     |
Description
SpecifiestheIRDPpreferencelevel.Ifahostreceivesmultiplerouteradvertisementmessagesfrom
differentrouters,thehostselectstherouterthatsentthemessagewiththehighestpreferenceasthe
defaultgateway.
ThenoformofthiscommandremovesthespecifiedIRDPpreferencelevelandrevertstothedefault
value.
| Parameter |     |     |     | Description                                         |     |     |
| --------- | --- | --- | --- | --------------------------------------------------- | --- | --- |
| <LEVEL>   |     |     |     | SpecifiestheIRDPpreferencelevel.Range:-2147483648to |     |     |
2147483647.Default:0.
Example
SettingtheIRDPpreferencelevelforinterface1/1/1to25.
| switch(config)#    |     | interface | 1/1/1   |            |     |     |
| ------------------ | --- | --------- | ------- | ---------- | --- | --- |
| switch(config-if)# |     |           | ip irdp | preference | 25  |     |
RemovingtheIRDPpreferencelevelforinterface1/1/1to25.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 19

| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|                |             |     | no ip irdp | preference   | 25  |     |
| -------------- | ----------- | --- | ---------- | ------------ | --- | --- |
| Command        | History     |     |            |              |     |     |
| Release        |             |     |            | Modification |     |     |
| 10.07orearlier |             |     |            | --           |     |     |
| Command        | Information |     |            |              |     |     |
| Platforms      | Command     |     | context    | Authority    |     |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip irdp |            |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- |
| show ip irdp | [vsx-peer] |     |     |     |     |     |
Description
DisplaysIRDPconfigurationsettings.
| Parameter  |     |     |     | Description                |     |     |
| ---------- | --- | --- | --- | -------------------------- | --- | --- |
| <location> |     |     |     | Specifiesoneofthesevalues: |     |     |
n <FQDN>:afullyqualifieddomainname.
<IPV4>:anIPv4address.
n
n <IPV6>:anIPv6address.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISLisdown,
theoutputfromtheVSXpeerswitchisnotdisplayed.ThisparameterisavailableonswitchesthatsupportVSX.
Example
| switch#     | show      | ip irdp |          |     |     |     |
| ----------- | --------- | ------- | -------- | --- | --- | --- |
| ICMP Router | Discovery |         | Protocol |     |     |     |
Interface Status Advertising Minimum Maximum Holdtime Preference
|     |     |     | Address | Interval | Interval |     |
| --- | --- | --- | ------- | -------- | -------- | --- |
--------- -------- ----------- -------- -------- -------- -----------
| 1/1/1          | Enabled  |     | multicast | 6            | 8   | 10 10    |
| -------------- | -------- | --- | --------- | ------------ | --- | -------- |
| 1/1/2          | Disabled |     | multicast | 450          | 600 | 1800 0   |
| 1/1/3          | Enabled  |     | broadcast | 450          | 600 | 1800 115 |
| Command        | History  |     |           |              |     |          |
| Release        |          |     |           | Modification |     |          |
| 10.07orearlier |          |     |           | --           |     |          |
IRDP|20

Command Information

Platforms

Command context

Authority

All platforms

Manager (#)

Administrators or local user group members with execution
rights for this command.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

21

Chapter 3
|                           |     |     | IPv6 | Router | Advertisement |     |
| ------------------------- | --- | --- | ---- | ------ | ------------- | --- |
| IPv6 Router Advertisement |     |     |      |        |               |     |
IPV6RAprovidesamethodforlocalIPV6hoststoautomaticallyconfiguretheirownIPaddress(and
othersettingssuchasapreferredDNSserver)basedoninformationadvertisedbyswitches/routers
operatingonthenetwork.
IPv6 flags
BehaviorofIPv6hoststoIPv6RAmessagesiscontrolledbythemanagedaddressconfigurationflag(M
flag),andotherstatefulconfigurationflag(Oflag).
| M flag | O flag |     | Description                                              |     |     |     |
| ------ | ------ | --- | -------------------------------------------------------- | --- | --- | --- |
| 0      | 0      |     | IndicatesthatnoinformationisavailableviaDHCPv6.          |     |     |     |
| 0      | 1      |     | Indicatesthatotherconfigurationinformationisavailablevia |     |     |     |
DHCPv6.ExamplesofsuchinformationareDNS-related
informationorinformationonotherserverswithinthenetwork.
| 1   | 0   |     | IndicatesthataddressesareavailableviaDynamicHost |     |     |     |
| --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
ConfigurationProtocol(DHCPv6).
| 1   | 1   |     | IftheMflagisset,theOflagisredundantandcanbeignored |     |     |     |
| --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
becauseDHCPv6willreturnallavailableconfiguration
information.
| Configuring | IPv6 RA |     |     |     |     |     |
| ----------- | ------- | --- | --- | --- | --- | --- |
Procedure
1. EnabletransmissionofIPv6routeradvertisementswiththecommandno ipv6 nd suppress-ra.
2. Optionally,configureIPv6unicastaddressprefixeswiththecommandipv6 prefix.
nd
3. Optionally,configuresupportforDNSnameresolutionwiththecommandsipv6 nd ra dns
| serverandipv6 | nd ra dns | search-list. |     |     |     |     |
| ------------- | --------- | ------------ | --- | --- | --- | --- |
4. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
| IPv6 RA setting                   |     |     | Default value | Command           | to change | it  |
| --------------------------------- | --- | --- | ------------- | ----------------- | --------- | --- |
| Numberofneighborsolicitationstobe |     |     | 1             | ipv6nddadattempts |           |     |
sentwhenperformingDAD.
| NumberofneighborentriesintheND |     |     | 131072 | ipv6 nd | cache-limit |     |
| ------------------------------ | --- | --- | ------ | ------- | ----------- | --- |
cache.
22
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries)

| IPv6 RA                          | setting |     |     | Default   | value | Command | to change | it  |
| -------------------------------- | ------- | --- | --- | --------- | ----- | ------- | --------- | --- |
| HoplimittobesentintheRAmessages. |         |     |     | 64        |       | ipv6 nd | hop-limit |     |
| MTUvaluetobesentintheRA          |         |     |     | 1500bytes |       | ipv6 nd | mtu       |     |
messages.
Neighborsolicitationinterval 1000milliseconds ipv6 nd ns-interval
| Lifetimeofadefaultrouter. |     |     |     | 1800seconds |     | ipv6 nd | ra lifetime |     |
| ------------------------- | --- | --- | --- | ----------- | --- | ------- | ----------- | --- |
RetrievalofanIPv6addressbydevices. Disabled ipv6 nd ra managed-config-flag
| Maximumintervalbetween |     |     |     | 600seconds |     | ipv6 nd | ra max-interval |     |
| ---------------------- | --- | --- | --- | ---------- | --- | ------- | --------------- | --- |
transmissionsofIPv6RAs.
| Minimumintervalbetween |     |     |     | 200seconds |     | ipv6 nd | ra min-interval |     |
| ---------------------- | --- | --- | --- | ---------- | --- | ------- | --------------- | --- |
transmissionsofIPv6RAs.
Timethataninterfaceconsidersa 0milliseconds(no ipv6 nd ra reachable-time
| devicetobereachable. |     |     |     | limit) |     |     |     |     |
| -------------------- | --- | --- | --- | ------ | --- | --- | --- | --- |
RetryperiodbetweenNDsolicitations. 0(Uselocally ipv6 nd ra retrans-timer
configuredNS-
interval)
Defaultroutingpreferenceforan Medium ipv6 nd router-preference
interface.
5. ReviewIPv6RAconfigurationsettingswiththecommandsshow ipv6 nd interface,show ipv6
nd interface prefix,show ipv6 nd ra dns server,andshow ipv6 nd ra dns search-list.
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablesIPV6RAoninterface1/1/3.
n SetstherecursiveDNSserveraddressto4001::1withalifetimeof400seconds.
n Setstheminimumintervalbetweentransmissionsto3seconds.
n Setsthemaximumintervalbetweentransmissionsto13seconds.
n Setsthelifetimeofadefaultrouterto1900seconds.
| switch(config)#    |       | interface    | 1/1/3              |        |                  |     |     |     |
| ------------------ | ----- | ------------ | ------------------ | ------ | ---------------- | --- | --- | --- |
| switch(config-if)# |       | no ipv6      | nd suppress-ra     |        |                  |     |     |     |
| switch(config-if)# |       | ipv6         | nd ra dns          | server | 4001::1 lifetime | 400 |     |     |
| switch(config-if)# |       | ipv6         | nd ra min-interval |        | 3                |     |     |     |
| switch(config-if)# |       | ipv6         | nd ra max-interval |        | 13               |     |     |     |
| switch(config-if)# |       | ipv6         | nd ra lifetime     | 1900   |                  |     |     |     |
| switch(config-if)# |       | end          |                    |        |                  |     |     |     |
| switch# show       | ipv6  | nd interface | 1/1/3              |        |                  |     |     |     |
| Interface          | 1/1/3 | is up        |                    |        |                  |     |     |     |
| Admin state        | is    | up           |                    |        |                  |     |     |     |
IPv6 address:
| 2006::1/64      | [VALID] |          |                             |     |     |         |     |     |
| --------------- | ------- | -------- | --------------------------- | --- | --- | ------- | --- | --- |
| IPv6 link-local |         | address: | fe80::98f2:b321:368:6dc6/64 |     |     | [VALID] |     |     |
| ICMPv6 active   |         | timers:  |                             |     |     |         |     |     |
IPv6RouterAdvertisement|23

Last Router-Advertisement sent: 0 Secs
Next Router-Advertisement sent in: 13 Secs

Router-Advertisement parameters:

Periodic interval: 3 to 13 secs
Router Preference: medium
Send "Managed Address Configuration" flag: false
Send "Other Stateful Configuration" flag: false
Send "Current Hop Limit" field: 64
Send "MTU" option value: 1500
Send "Router Lifetime" field: 1900
Send "Reachable Time" field: 0
Send "Retrans Timer" field: 0
Suppress RA: false
Suppress MTU in RA: true
ICMPv6 error message parameters:

Send redirects: false

ICMPv6 DAD parameters:

Current DAD attempt: 1
switch# show ipv6 nd ra dns server
Recursive DNS Server List on: 1/1/3

Suppress DNS Server List: No
DNS Server 1: 2001::1

lifetime 400

IPv6 RA scenario

In this scenario, two host computers are auto-configured with IP addresses using IPv6 RA. In addition,
the switch provides the hosts with an address of a recursive DNS server. The physical topology of the
network looks like this:

Procedure

1. Configure the interfaces with IPv6 addresses.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# ipv6 address 2001::1/64
switch(config)# interface 1/1/2
switch(config-if)# ipv6 address 3001::1/64
switch(config)# interface 1/1/3
switch(config-if)# ipv6 address 4001::1/64

2. Enable transmission of all IPv6 RA messages.

switch(config-if)# no ipv6 nd suppress-ra

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

24

| IPv6 RA         | commands                 |     |     |     |
| --------------- | ------------------------ | --- | --- | --- |
| ipv6 address    | <global-unicast-address> |     |     |     |
| ipv6 address    | <global-unicast-address> |     |     |     |
| no ipv6 address | <global-unicast-address> |     |     |     |
Description
Setsaglobalunicastaddressontheinterface.
Thenoformofthiscommandremovestheglobalunicastaddressontheinterface.
ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-
localaddressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6 address
link-localcommand.
Example
Enablingaglobalunicastaddress:
switch(config)#
|                    | interface |      | 1/1/1   |                    |
| ------------------ | --------- | ---- | ------- | ------------------ |
| switch(config-if)# |           | ipv6 | address | 3731:54:65fe:2::a7 |
Disablingaglobalunicastaddress:
| switch(config)#     | interface |         | 1/1/1        |                    |
| ------------------- | --------- | ------- | ------------ | ------------------ |
| switch(config-if)#  |           | no      | ipv6 address | 3731:54:65fe:2::a7 |
| Command History     |           |         |              |                    |
| Release             |           |         |              | Modification       |
| 10.07orearlier      |           |         |              | --                 |
| Command Information |           |         |              |                    |
| Platforms           | Command   | context |              | Authority          |
config-if
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| ipv6 address    | autoconfig |     |     |     |
| --------------- | ---------- | --- | --- | --- |
| ipv6 address    | autoconfig |     |     |     |
| no ipv6 address | autoconfig |     |     |     |
Description
EnablestheinterfacetoautomaticallyobtainanIPv6addressusingrouteradvertisementinformation
andtheEUI-64identifier.
Thenoformofthiscommanddisablesaddressauto-configuration.
IPv6RouterAdvertisement|25

n Amaximumof15autoconfiguredaddressesaresupported.
n ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotadd
theipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,
thelink-localaddressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutethe
| ipv6 | address | link-localcommand. |     |     |
| ---- | ------- | ------------------ | --- | --- |
Usage
TheIPv6SLAACfeatureletstherouterobtaintheIPv6addressfortheinterfaceitisconfiguredthrough
theSLAACmethod.ThisfeatureisnotavailableonthemgmtVRF.
Example
Enablingunicastautoconfiguring:
| switch(config)#    |     | interface | 1/1/1        |            |
| ------------------ | --- | --------- | ------------ | ---------- |
| switch(config-if)# |     |           | ipv6 address | autoconfig |
Disablingunicastautoconfiguring:
| switch(config)#    |             | interface | 1/1/1           |              |
| ------------------ | ----------- | --------- | --------------- | ------------ |
| switch(config-if)# |             |           | no ipv6 address | autoconfig   |
| Command            | History     |           |                 |              |
| Release            |             |           |                 | Modification |
| 10.07orearlier     |             |           |                 | --           |
| Command            | Information |           |                 |              |
| Platforms          | Command     |           | context         | Authority    |
config-if
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| ipv6 address |            | link-local |                      |     |
| ------------ | ---------- | ---------- | -------------------- | --- |
| ipv6 address | link-local |            | [<IPV6-ADDR>/<MASK>] |     |
Description
EnablesIPv6onthecurrentinterface.Ifnoaddressisspecified,anIPv6link-localaddressisauto-
generatedfortheinterface.Ifanaddressisspecified,auto-configurationisdisabledandthespecified
address/maskisassignedtotheinterface.
TodisableIPv6link-localontheinterface,removeipv6 address link-local,ipv6 address <global-
| ipv6-address>,andipv6 |     |     | address autoconfigfromtheinterface. |     |
| --------------------- | --- | --- | ----------------------------------- | --- |
ThisfeatureisnotavailableonthemanagementVRF.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 26

| Parameter   |     |     |     | Description                       |
| ----------- | --- | --- | --- | --------------------------------- |
| <IPV6-ADDR> |     |     |     | SpecifiestheIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| <MASK> |     |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
Example
EnablingIPv6link-localontheinterface:
| switch(config)#    |             | interface | 1/1/1        |              |
| ------------------ | ----------- | --------- | ------------ | ------------ |
| switch(config-if)# |             |           | ipv6 address | link-local   |
| Command            | History     |           |              |              |
| Release            |             |           |              | Modification |
| 10.07orearlier     |             |           |              | --           |
| Command            | Information |           |              |              |
| Platforms          | Command     |           | context      | Authority    |
Allplatforms config-if OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| ipv6 nd | cache-limit    |              |                |     |
| ------- | -------------- | ------------ | -------------- | --- |
| ipv6 nd | cache-limit    | <CACHELIMIT> |                |     |
| no ipv6 | nd cache-limit |              | [<CACHELIMIT>] |     |
Description
ConfiguresthelimitonthenumberofneighborentriesintheNDcache.
Thenoformofthiscommandsetsthecachelimittothedefaultvalue.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<CACHELIMIT> Specifiestheneighborcacheentrieslimit.Range:1-131072.
Default:131072.
Examples
Settingthecachelimitto20.
IPv6RouterAdvertisement|27

| switch(config)# |             | ipv6 | nd cache-limit | 20           |
| --------------- | ----------- | ---- | -------------- | ------------ |
| Command         | History     |      |                |              |
| Release         |             |      |                | Modification |
| 10.07orearlier  |             |      |                | --           |
| Command         | Information |      |                |              |
| Platforms       | Command     |      | context        | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | dad             | attempts       |                  |     |
| ------- | --------------- | -------------- | ---------------- | --- |
| ipv6 nd | dad attempts    | <NUM-ATTEMPTS> |                  |     |
| no ipv6 | nd dad attempts |                | [<NUM-ATTEMPTS>] |     |
Description
Configuresthenumberofneighborsolicitationstobesentwhenperformingduplicateaddress
detection(DAD)foraunicastaddressconfiguredonaninterface.Iftheactivegatewayisconfiguredwith
thesameIPasanSVIIP,thenIPv6DADcannotbeconfigured.
Thenoformofthiscommandsetsthenumberofattemptstothedefaultvalue.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
dad attempts <NUM-ATTEMPTS> Specifiesthenumberofneighborsolicitationstosend.Range:0-
15.Default:1.
Examples
| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
|                |             |     | ipv6 nd dad | attempts 5   |
| -------------- | ----------- | --- | ----------- | ------------ |
| Command        | History     |     |             |              |
| Release        |             |     |             | Modification |
| 10.07orearlier |             |     |             | --           |
| Command        | Information |     |             |              |
| Platforms      | Command     |     | context     | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | hop-limit |     |     |     |
| ------- | --------- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 28

| ipv6 nd | hop-limit    | <HOPLIMIT>   |     |     |     |
| ------- | ------------ | ------------ | --- | --- | --- |
| no ipv6 | nd hop-limit | [<HOPLIMIT>] |     |     |     |
Description
ConfiguresthehoplimittobesentinRAs.
Thenoformofthiscommandresetsthehoplimitto0.ThisreseteliminatesthehoplimitfromtheRAs
thatoriginateontheinterface,sothehostdeterminesthehoplimit.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
hop-limit <HOPLIMIT> Specifiesthehoplimit.Range:0-255.Default:64.
Examples
| switch(config)#    |             | interface | 1/1/1             |     |              |
| ------------------ | ----------- | --------- | ----------------- | --- | ------------ |
| switch(config-if)# |             |           | ipv6 nd hop-limit |     | 64           |
| Command            | History     |           |                   |     |              |
| Release            |             |           |                   |     | Modification |
| 10.07orearlier     |             |           |                   |     | --           |
| Command            | Information |           |                   |     |              |
| Platforms          | Command     |           | context           |     | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | mtu                  |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- |
| ipv6 nd | mtu <MTU-VALUE>      |     |     |     |     |
| no ipv6 | nd mtu [<MTU-VALUE>] |     |     |     |     |
Description
ConfigurestheMTUsizetobesentintheRAmessages.
Thenoformofthiscommandsetshoplimittothedefaultvalue.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<MTU-VALUE>
SpecifiestheMTUsize.Range:1280-65535bytes.Default:1500
bytes.
Examples
| switch(config)#    |         | interface | 1/1/1       |      |     |
| ------------------ | ------- | --------- | ----------- | ---- | --- |
| switch(config-if)# |         |           | ipv6 nd mtu | 1300 |     |
| Command            | History |           |             |      |     |
IPv6RouterAdvertisement|29

|         | Release        |             |         |         | Modification |     |
| ------- | -------------- | ----------- | ------- | ------- | ------------ | --- |
|         | 10.07orearlier |             |         |         | --           |     |
| Command |                | Information |         |         |              |     |
|         | Platforms      |             | Command | context | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 | nd   | ns-interval    |        |          |     |     |
| ---- | ---- | -------------- | ------ | -------- | --- | --- |
| ipv6 | nd   | ns-interval    | <TIME> |          |     |     |
| no   | ipv6 | nd ns-interval |        | [<TIME>] |     |     |
Description
ConfigurestheNDtimeinmillisecondsbetweenDADneighborsolicitationssentforanunresolved
destination.Increasethens-intervaltimeifthenetworkissloworiftherearepersistentretryfailures.If
theactivegatewayisconfiguredwiththesameIPasanSVIIP,thenIPv6DADcannotbeconfigured
Thenoformofthiscommandsetsthens-intervaltothedefaultvalue.
|     | Parameter |     |     |     | Description |     |
| --- | --------- | --- | --- | --- | ----------- | --- |
<TIME> Specifiestheneighborsolicitationinterval.Range:1000-3600000
milliseconds.Default:1000milliseconds.
Examples
|         | switch(config)#    |             | interface | 1/1/1               |              |      |
| ------- | ------------------ | ----------- | --------- | ------------------- | ------------ | ---- |
|         | switch(config-if)# |             |           | ipv6 nd ns-interval |              | 1200 |
| Command |                    | History     |           |                     |              |      |
|         | Release            |             |           |                     | Modification |      |
|         | 10.07orearlier     |             |           |                     | --           |      |
| Command |                    | Information |           |                     |              |      |
|         | Platforms          |             | Command   | context             | Authority    |      |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 | nd                | prefix                          |                          |                  |     |               |
| ---- | ----------------- | ------------------------------- | ------------------------ | ---------------- | --- | ------------- |
| ipv6 | nd                | prefix <IPV6-ADDR>/<PREFIX-LEN> |                          |                  |     |               |
|      | [no-advertise     |                                 | | [valid                 | <LIFETIME-VALUE> |     | preferred     |
|      | <LIFETIME-VALUE>] |                                 |                          | | no-autoconfig  |     | | no-onlink]  |
| no   | ipv6              | nd prefix                       | <IPV6-ADDR>/<PREFIX-LEN> |                  |     | [no-advertise |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 30

| | [valid          | <LIFETIME-VALUE>      | preferred       | <LIFETIME-VALUE>        |     |     |
| ----------------- | --------------------- | --------------- | ----------------------- | --- | --- |
| ] | no-autoconfig | | no-onlink]          |                 |                         |     |     |
| ipv6 nd prefix    | default [no-advertise | |               | [valid <LIFETIME-VALUE> |     |     |
| preferred         | <LIFETIME-VALUE>]     | | no-autoconfig | | no-onlink]}           |     |     |
no ipv6 nd prefix default [no-advertise | [valid <LIFETIME-VALUE>
| preferred | <LIFETIME-VALUE>] | | no-autoconfig | | no-onlink]} |     |     |
| --------- | ----------------- | --------------- | ------------- | --- | --- |
Description
SpecifiesprefixesfortheroutingswitchtoincludeinRAstransmittedontheinterface.IPv6hostsuse
theprefixesinRAstoautoconfigurethemselveswithglobalunicastaddresses.Theautoconfigured
addressofahostiscomposedoftheadvertisedprefixandtheinterfaceidentifierinthecurrentlink-
localaddressofthehost.
Bydefault,advertise,autoconfig,andonlinkareset.
Thenoformofthiscommandremovestheconfigurationontheinterface.
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
<IPV6-ADDR>/<PREFIX-LEN> SpecifiestheIPv6prefixtoadvertiseinRA.Format:X:X::X:X/M
default Specifiesapplyconfigurationtoallon-linkprefixesthatarenot
|     |     | individuallysetbytheipv6 |     | ra prefix | <IPV6- |
| --- | --- | ------------------------ | --- | --------- | ------ |
ADDR>/<PREFIX-LEN>command.Itappliesthesamevalidand
preferredlifetimes,linkstate,autoconfigurationstate,and
advertiseoptionstotheadvertisementssentforallon-link
prefixesthatarenotindividuallyconfiguredwithaunique
lifetime.Thisalsoappliestotheprefixesforanyglobalunicast
addressesconfiguredlateronthesameinterface.
Usingdefaultonce,andthenusingitagainwithanynew
parametervaluesresultsinthenewvaluesreplacingtheformer
valuesinadvertisements.Ifdefaultisusedwithouttheno–
advertise,no–autoconfig,orno-onlinkparameter,the
advertisementsettingfortheabsentparameterisreturnedtoits
defaultsetting.
| no-advertise |     | SpecifiesdonotadvertiseprefixinRA. |     |     |     |
| ------------ | --- | ---------------------------------- | --- | --- | --- |
valid <LIFETIME-VALUE> Specifiesthetotaltime,inseconds,theprefixremainsavailable
beforebecomingunusable.Afterpreferred-lifetimeexpiration,
anyautoconfiguredaddressisdeprecatedandusedonlyfor
transactionsonlybeforepreferred-lifetimeexpires.Ifthevalid
lifetimeexpires,theaddressbecomesinvalid.
|     |     | Youcanenteravalueinsecondsorentervalid |     |     | infinite |
| --- | --- | -------------------------------------- | --- | --- | -------- |
whichsetsinfinitelifetime.Default:2,592,000secondswhichis30
days.Range:0–4294967294seconds.
preferred <LIFETIME-VALUE> Specifiesthespanoftimeduringwhichtheaddresscanbefreely
usedasasourceanddestinationfortraffic.Thissettingmustbe
lessthanorequaltothecorrespondingvalid–lifetimesetting.
Youcanenteravalueinsecondsorenterpreferred infinite
whichsetsinfinitelifetime.Default:604,800secondswhichis
sevendays.Range:0–4294967294seconds.
| no-autoconfig |     | Specifiesdonotuseprefixforautoconfiguration.   |     |     |     |
| ------------- | --- | ---------------------------------------------- | --- | --- | --- |
| no-onlink     |     | Specifiesdonotuseprefixforonlinkdetermination. |     |     |     |
Examples
IPv6RouterAdvertisement|31

| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|     |     |     | ipv6 nd prefix | 4001::1/64 | valid 30 preferred | 10 no-autoconfig |
| --- | --- | --- | -------------- | ---------- | ------------------ | ---------------- |
no-onlink
| Command        | History     |     |         |              |     |     |
| -------------- | ----------- | --- | ------- | ------------ | --- | --- |
| Release        |             |     |         | Modification |     |     |
| 10.07orearlier |             |     |         | --           |     |     |
| Command        | Information |     |         |              |     |     |
| Platforms      | Command     |     | context | Authority    |     |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra dns             | search-list |               |           |         |     |
| ------- | ------------------ | ----------- | ------------- | --------- | ------- | --- |
| ipv6 nd | ra dns search-list |             | <DOMAIN-NAME> | [lifetime | <TIME>] |     |
| no ipv6 | nd ra dns          | search-list | <DOMAIN-NAME> |           |         |     |
Description
ConfigurestheDNSSearchList(DNSSL)toincludeinRouterAdvertisements(RAs)transmittedonthe
interface.
ThenoformofthiscommandremovestheDNSSearchListfromtheRAstransmittedontheinterface.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<DOMAIN-NAME>
SpecifiesthedomainnamesforDNSqueries.
lifetime <TIME> Specifieslifetimeinseconds.Range:4-4294967295seconds.
Default:1800seconds.
Usage
n DNSSLcontainsthedomainnamesofDNSsuffixesorIPv6hoststoappendtoshort,unqualified
domainnamesforDNSqueries.
n MultipleDNSdomainnamescanbeaddedtotheDNSSLbyusingthecommandrepeatedly.
n Amaximumofeightserveraddressesareallowed.
Examples
| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)# ipv6 nd ra dns search-list test.com lifetime 500
| Command        | History |     |     |              |     |     |
| -------------- | ------- | --- | --- | ------------ | --- | --- |
| Release        |         |     |     | Modification |     |     |
| 10.07orearlier |         |     |     | --           |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 32

| Command   | Information |     |         |           |     |     |
| --------- | ----------- | --- | ------- | --------- | --- | --- |
| Platforms | Command     |     | context | Authority |     |     |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra dns        | server |             |           |         |     |
| ------- | ------------- | ------ | ----------- | --------- | ------- | --- |
| ipv6 nd | ra dns server |        | <IPV6-ADDR> | [lifetime | <TIME>] |     |
| no ipv6 | nd ra dns     | server | <IPV6-ADDR> |           |         |     |
Description
ConfigurestheIPv6addressofapreferredRecursiveDNSServer(RDNSS)tobeincludedinRouter
Advertisements(RAs)transmittedontheinterface.
ThenoformofthiscommandremovestheconfiguredDNSserverfromtheRAstransmittedonthe
interface.
| Parameter   |     |     |     | Description                          |     |     |
| ----------- | --- | --- | --- | ------------------------------------ | --- | --- |
| <IPV6-ADDR> |     |     |     | SpecifiestheRDNSSaddressinIPv6format |     |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
lifetime <TIME> SpecifiesIPv6DNSserverlifetimeinseconds.Range:4-
4294967295seconds.Default:1800seconds.
Usage
n IncludingRDNSSinformationinRAsprovidesDNSserverconfigurationforconnectedIPv6hosts
withoutrequiringDHCPv6.
n Multipleserverscanbeconfiguredontheinterfacebyusingthecommandrepeatedly.
n Amaximumofeightserveraddressesareallowed.
Examples
| switch(config)#    |             | interface | 1/1/1   |               |                  |     |
| ------------------ | ----------- | --------- | ------- | ------------- | ---------------- | --- |
| switch(config-if)# |             |           | ipv6 nd | ra dns server | 2001::1 lifetime | 400 |
| Command            | History     |           |         |               |                  |     |
| Release            |             |           |         | Modification  |                  |     |
| 10.07orearlier     |             |           |         | --            |                  |     |
| Command            | Information |           |         |               |                  |     |
IPv6RouterAdvertisement|33

| Platforms | Command |     | context | Authority |
| --------- | ------- | --- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra lifetime    |        |          |     |
| ------- | -------------- | ------ | -------- | --- |
| ipv6 nd | ra lifetime    | <TIME> |          |     |
| no ipv6 | nd ra lifetime |        | [<TIME>] |     |
Description
Configuresthelifetime,inseconds,fortheroutingswitchtobeusedasadefaultrouterbyhostsonthe
currentinterface.
Thenoformofthiscommandsetslifetimetothedefaultof1800seconds.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<TIME> Specifieslifetimeinsecondsofadefaultrouter.Asettingof0for
defaultrouterlifetimeinanRAindicatesthattheroutingswitchis
notadefaultrouterontheinterface.Range:0-9000seconds.
Default:1800seconds.
Usage
n Agivenhostonaninterfacerefreshesthedefaultrouterlifetimeforaspecificroutereachtimethe
hostreceivesanRAfromthatrouter.
n Aspecificrouterceasestobeadefaultroutercandidateforagivenhostifthedefaultrouterlifetime
expiresbeforethehostisupdatedwithanewRAfromtherouter.
Examples
| switch(config)#    |             | interface | 1/1/1   |                  |
| ------------------ | ----------- | --------- | ------- | ---------------- |
| switch(config-if)# |             |           | ipv6 nd | ra lifetime 1200 |
| Command            | History     |           |         |                  |
| Release            |             |           |         | Modification     |
| 10.07orearlier     |             |           |         | --               |
| Command            | Information |           |         |                  |
| Platforms          | Command     |           | context | Authority        |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra managed-config-flag    |     |     |     |
| ------- | ------------------------- | --- | --- | --- |
| ipv6 nd | ra managed-config-flag    |     |     |     |
| no ipv6 | nd ra managed-config-flag |     |     |     |
Description
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 34

ControlstheMflagsettinginRAstheroutertransmitsonthecurrentinterface.EnabletheMflagto
indicatethathostscanobtainIPaddressthroughDHCPv6.TheMflagisdisabledbydefault.
Thenoformofthiscommandturnsoff(disables)theMflag.
Usage
n EnablingtheMflagdirectshoststoacquiretheirIPv6addressingforthecurrentinterfacefroma
DHCPv6server.
n WhentheM-bitisenabled,receivinghostsignoretheOflagsetting,whichisconfiguredusingthe
| commandipv6 |     | nd ra | other-config-flag. |     |     |
| ----------- | --- | ----- | ------------------ | --- | --- |
n WhentheM-bitisdisabled(thedefault),receivinghostsexpecttoreceivetheirIPv6addressesfrom
RA.
| M flag |     |     |     | O flag | Description                              |
| ------ | --- | --- | --- | ------ | ---------------------------------------- |
| 0      |     |     |     | 0      | Indicatesthatnoinformationisavailablevia |
DHCPv6.
| 0   |     |     |     | 1   | Indicatesthatotherconfiguration |
| --- | --- | --- | --- | --- | ------------------------------- |
informationisavailableviaDHCPv6.
ExamplesofsuchinformationareDNS-
relatedinformationorinformationonother
serverswithinthenetwork.
| 1   |     |     |     | 0   | Indicatesthataddressesareavailablevia |
| --- | --- | --- | --- | --- | ------------------------------------- |
DynamicHostConfigurationProtocol
(DHCPv6).
| 1   |     |     |     | 1   | IftheMflagisset,theOflagisredundant |
| --- | --- | --- | --- | --- | ----------------------------------- |
andcanbeignoredbecauseDHCPv6will
returnallavailableconfiguration
information.
Examples
| switch(config)#    |             | interface | 1/1/1   |                        |     |
| ------------------ | ----------- | --------- | ------- | ---------------------- | --- |
| switch(config-if)# |             |           | ipv6 nd | ra managed-config-flag |     |
| Command            | History     |           |         |                        |     |
| Release            |             |           |         | Modification           |     |
| 10.07orearlier     |             |           |         | --                     |     |
| Command            | Information |           |         |                        |     |
| Platforms          | Command     |           | context | Authority              |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra max-interval    |     |          |     |     |
| ------- | ------------------ | --- | -------- | --- | --- |
| ipv6 nd | ra max-interval    |     | <TIME>   |     |     |
| no ipv6 | nd ra max-interval |     | [<TIME>] |     |     |
IPv6RouterAdvertisement|35

Description
ConfiguresthemaximumintervalbetweentransmissionsofIPv6RAsontheinterface.Theinterval
betweenRAtransmissionsonaninterfaceisarandomvaluethatchangeseverytimeanRAissent.The
intervaliscalculatedtobeavaluebetweenthecurrentmax-intervalandmin-intervalsettings.
Thenoformofthiscommandreturnsthesettingtoitsdefault,providedthedefaultvalueislessthan
thedefaultlifetimevalue.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<TIME> Specifiesthemaximumadvertisementtimeinseconds.Range:4-
1800.Default:600seconds.
Usage
n Thisvaluehasonesettingperinterface.ThesettingdoesnotapplytoRAssentinresponsetoa
routersolicitationreceivedfromanotherdevice.
Attemptingtosetmax-intervaltoavaluethatisnotsufficientlylargerthanthecurrentmin-interval
n
alsoresultsinanerrormessage.
Examples
| switch(config)#    |             | interface | 1/1/1   |                 |     |
| ------------------ | ----------- | --------- | ------- | --------------- | --- |
| switch(config-if)# |             |           | ipv6 nd | ra max-interval | 30  |
| Command            | History     |           |         |                 |     |
| Release            |             |           |         | Modification    |     |
| 10.07orearlier     |             |           |         | --              |     |
| Command            | Information |           |         |                 |     |
| Platforms          | Command     |           | context | Authority       |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra min-interval    |     |          |     |     |
| ------- | ------------------ | --- | -------- | --- | --- |
| ipv6 nd | ra min-interval    |     | <TIME>   |     |     |
| no ipv6 | nd ra min-interval |     | [<TIME>] |     |     |
Description
ConfigurestheminimumintervalbetweentransmissionsofIPv6RAsontheinterface.Theinterval
betweenRAtransmissionsonaninterfaceisarandomvaluethatchangeseverytimeanRAissent.The
intervaliscalculatedtobeavaluebetweenthecurrentmax-intervalandmin-intervalsettings.
Thenoformofthiscommandreturnsthesettingtoitsdefault,providedthedefaultvalueislessthan
thecurrentmax-intervalsetting.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 36

| Parameter |     |     |     | Description                                          |     |
| --------- | --- | --- | --- | ---------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiesaminimumadvertisementtimeinseconds.Range:3- |     |
1350.Default:200seconds.
Usage
n ThisvaluehasonesettingperinterfaceanddoesnotapplytoRAssentinresponsetoarouter
solicitationreceivedfromanotherdevice.
Themin-intervalmustbelessthanthemax-interval.Attemptingtosetmin-intervaltoahighervalue
n
resultsinanerrormessage.
Examples
| switch(config)#     |         | interface | 1/1/1 |              |     |
| ------------------- | ------- | --------- | ----- | ------------ | --- |
| switch(config-if)#  |         | ipv6      | nd ra | min-interval | 25  |
| Command History     |         |           |       |              |     |
| Release             |         |           |       | Modification |     |
| 10.07orearlier      |         |           |       | --           |     |
| Command Information |         |           |       |              |     |
| Platforms           | Command | context   |       | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd ra                   | other-config-flag |     |     |     |     |
| ---------------------------- | ----------------- | --- | --- | --- | --- |
| ipv6 nd ra other-config-flag |                   |     |     |     |     |
| no ipv6 nd ra                | other-config-flag |     |     |     |     |
Description
ControlstheO-bitinRAstheroutertransmitsonthecurrentinterface;butisignoredunlesstheM-bitis
disabledinRAs.ConfiguretosettheO-bitinRAmessagesforhosttoobtainnetworkparameters
throughDHCPv6.Theother-config-flagisdisabledbydefault.
FormoreinformationonconfiguringtheM-bit,see ipv6 nd ra managed-config-flag.
Thenoformofthiscommandturnsoff(disables)thesettingforthiscommandinRAs.
Usage
EnablingtheO-bitwhiletheM-bitisdisableddirectshostsontheinterfacetoacquiretheirother
configurationinformationfromDHCPv6.ExamplesofsuchinformationareDNS-relatedinformationor
informationonotherserverswithinthenetwork.
Examples
IPv6RouterAdvertisement|37

| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|                |             |     | ipv6 nd | ra other-config-flag |     |
| -------------- | ----------- | --- | ------- | -------------------- | --- |
| Command        | History     |     |         |                      |     |
| Release        |             |     |         | Modification         |     |
| 10.07orearlier |             |     |         | --                   |     |
| Command        | Information |     |         |                      |     |
| Platforms      | Command     |     | context | Authority            |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra reachable-time    |     |          |     |     |
| ------- | -------------------- | --- | -------- | --- | --- |
| ipv6 nd | ra reachable-time    |     | <TIME>   |     |     |
| no ipv6 | nd ra reachable-time |     | [<TIME>] |     |     |
Description
Setstheamountoftimethattheinterfaceconsidersadevicetobereachableafterreceivinga
reachabilityconfirmationfromthedevice.
Thenoformofthiscommandsetsthereachabletimetothedefaultvalueof0.(nolimit).
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<TIME>
Specifiesthereachabletimeinmilliseconds.Range:1000-
3600000.Default:0(nolimit).
Examples
| switch(config)#    |             | interface | 1/1/1   |                   |      |
| ------------------ | ----------- | --------- | ------- | ----------------- | ---- |
| switch(config-if)# |             |           | ipv6 nd | ra reachable-time | 2000 |
| Command            | History     |           |         |                   |      |
| Release            |             |           |         | Modification      |      |
| 10.07orearlier     |             |           |         | --                |      |
| Command            | Information |           |         |                   |      |
| Platforms          | Command     |           | context | Authority         |      |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | ra retrans-timer |     |     |     |     |
| ------- | ---------------- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 38

| ipv6 nd | ra retrans-timer    |     | <TIME>   |     |     |
| ------- | ------------------- | --- | -------- | --- | --- |
| no ipv6 | nd ra retrans-timer |     | [<TIME>] |     |     |
Description
Configurestheperiod(retransmittimer)betweenNDsolicitationssentbyahostforanunresolved
destination,orbetweenDADneighborsolicitationrequests.Bydefault,hostsontheinterfaceusetheir
ownlocallyconfiguredNS-intervalsettingsinsteadofusingthevaluereceivedintheRAs.
Increasethistimerwhenneighborsolicitationretriesorfailuresareoccur,orina"slow"(WAN)network.
Thenoformofthiscommandsetsthevaluetothedefaultof0.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<TIME> Specifiestheretransmittimervalueinmilliseconds.Range:0-
4294967295milliseconds.Default:0(UselocallyconfiguredNS-
interval).
Examples
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|                |             |     | ipv6 nd | ra retrans-timer | 400 |
| -------------- | ----------- | --- | ------- | ---------------- | --- |
| Command        | History     |     |         |                  |     |
| Release        |             |     |         | Modification     |     |
| 10.07orearlier |             |     |         | --               |     |
| Command        | Information |     |         |                  |     |
| Platforms      | Command     |     | context | Authority        |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | route |     |     |     |     |
| ------- | ----- | --- | --- | --- | --- |
ipv6 nd route <IPV6-ADDR>/<PREFIX-LEN> [no-advertise | lifetime {<SECONDS> | infinite} |
| preference | {low | | medium | | high}] |     |     |
| ---------- | ---- | -------- | -------- | --- | --- |
no ipv6 nd route <IPV6-ADDR>/<PREFIX-LEN> [no-advertise | lifetime {<SECONDS> | infinite}
| | preference | {low | | medium | | high}] |     |     |
| ------------ | ---- | -------- | -------- | --- | --- |
Description
ConfigurestheroutingswitchtoincludetheroutinginformationintheRAstransmittedontheinterface.
TheroutingswitchincludestherouteinformationintheRApacketsonlyiftheconfiguredroutesare
presentintheroutingtable.AfterreceivingtheRApacketscarryingtherouteinformation,theIPv6host
updatesitsroutingtable.Thehostslookuptheirroutingtableandselectsthebestpossiblerouteto
forwardpackets.
Thenoformofthiscommandremovesthesettingsforincludingtheroutinginformationinthe
RA packets.
IPv6RouterAdvertisement|39

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV6-ADDR>/<PREFIX-LEN> SpecifiestheIPv6routeprefixtoadvertiseinRA.Format:
X:X::X:X/M
no-advertise
Specifiestonotadvertisetherouteinformation.
lifetime {<SECONDS> | infinite} Specifiesthedurationinsecondsthattherouteisvalidforthe
routedetermination.Ifthisparameterisconfiguredwith0,the
routebecomesinvalid.
Default:1800.Range:0-4294967295.
preference {low | medium | high} Specifiesthepreferenceforthehoststochoosetherouter
associatedwiththerouteoverotherrouterswhenmultiple
identicalrouteprefixesfromdifferentroutersarereceived.
Default: medium
Examples
Configuringroutinginformationoninterface1/1/1.
| switch(config)# | int | 1/1/1 |     |
| --------------- | --- | ----- | --- |
switch(config-if)# ipv6 nd route 1::1/64 lifetime 200 preference high
| Command   | History     |         |                   |
| --------- | ----------- | ------- | ----------------- |
| Release   |             |         | Modification      |
| 10.10     |             |         | Commandintroduced |
| Command   | Information |         |                   |
| Platforms | Command     | context | Authority         |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | router-preference    |         |                 |
| ------- | -------------------- | ------- | --------------- |
| ipv6 nd | router-preference    | {high | | medium | low}   |
| no ipv6 | nd router-preference | [high   | | medium | low] |
Description
SpecifiesthevaluethatissetintheDefaultRouterPreference(DRP)fieldofRouterAdvertisements
(RAs)thattheswitchsendsfromaninterface.AninterfacewithaDRPvalueofhighwillbepreferredby
otherdevicesonthenetworkoverinterfaceswithanRAvalueofmediumorlow.
Thenoformofthiscommandsetthevaluetothedefaultofmedium.
| Parameter |     |     | Description    |
| --------- | --- | --- | -------------- |
| high      |     |     | SetsDRPtohigh. |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 40

| Parameter |     |     |     | Description              |     |     |     |
| --------- | --- | --- | --- | ------------------------ | --- | --- | --- |
| medium    |     |     |     | SetsDRPtomedium.Default. |     |     |     |
| low       |     |     |     | SetsDRPtolow.            |     |     |     |
Examples
| switch(config)#    |             | interface | 1/1/1   |                   |     |      |     |
| ------------------ | ----------- | --------- | ------- | ----------------- | --- | ---- | --- |
| switch(config-if)# |             |           | ipv6 nd | router-preference |     | high |     |
| Command            | History     |           |         |                   |     |      |     |
| Release            |             |           |         | Modification      |     |      |     |
| 10.07orearlier     |             |           |         | --                |     |      |     |
| Command            | Information |           |         |                   |     |      |     |
| Platforms          | Command     |           | context | Authority         |     |      |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd | suppress-ra      |                     |                     |     |     |     |     |
| ------- | ---------------- | ------------------- | ------------------- | --- | --- | --- | --- |
| ipv6 nd | suppress-ra      | [<SUPPRESS-OPTION>] |                     |     |     |     |     |
| no ipv6 | nd ra supress-ra |                     | [<SUPPRESS-OPTION>] |     |     |     |     |
Description
ConfiguressuppressionofIPv6RouterAdvertisementtransmissionsonaninterface.
ThenoformofthiscommandrestorestransmissionofIPv6RouterAdvertisementandoptions.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
suppress-ra [<SUPPRESS-OPTION>] SpecifiessuppressingRAtransmissions.Enteringsuppress-ra
withoutanyoptions,suppressesallRAmessages(default).Oryou
canenteroneofthefollowingoptions.
| dnssl |     |     |     | SpecifiessuppressingDNSSLoptionsinRAmessages. |     |     |     |
| ----- | --- | --- | --- | --------------------------------------------- | --- | --- | --- |
mtu
SpecifiessuppressingMTUoptionsinRAmessages.
| rdnss |     |     |     | SpecifiessuppressingRDNSSoptionsinRAmessages. |     |     |     |
| ----- | --- | --- | --- | --------------------------------------------- | --- | --- | --- |
Examples
| switch(config)#    |         | interface | 1/1/1   |                |     |           |       |
| ------------------ | ------- | --------- | ------- | -------------- | --- | --------- | ----- |
| switch(config-if)# |         |           | ipv6 nd | suppress-ra    | mtu | dnssl     | rdnss |
| switch(config-if)# |         |           | no ipv6 | nd suppress-ra |     | mtu dnssl | rdnss |
| Command            | History |           |         |                |     |           |       |
IPv6RouterAdvertisement|41

| Release        |     |             |         |         |     | Modification |     |
| -------------- | --- | ----------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier |     |             |         |         |     | --           |     |
| Command        |     | Information |         |         |     |              |     |
| Platforms      |     |             | Command | context |     | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | ipv6    | nd     | global  | traffic |            |     |     |
| ---- | ------- | ------ | ------- | ------- | ---------- | --- | --- |
| show | ipv6 nd | global | traffic |         | [vsx-peer] |     |     |
Description
DisplaysIPV6NeighborDiscoverytrafficdetailsonadevice.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
|                | switch#     | show           | ipv6 nd        | global | traffic         |              |      |
| -------------- | ----------- | -------------- | -------------- | ------ | --------------- | ------------ | ---- |
|                | ICMPv6      | packet         | Statistics     |        | (sent/received) |              |      |
|                | Total       | Messages       |                |        |                 | :            | 18/0 |
|                | Error       | Messages       |                |        |                 | :            | 0/0  |
|                | Destination |                | Unreachables   |        |                 | :            | 0/0  |
|                | Time        | Exceeded       |                |        |                 | :            | 0/0  |
|                | Parameter   |                | Problems       |        |                 | :            | 0/0  |
|                | Echo        | Request        |                |        |                 | :            | 0/0  |
|                | Echo        | Replies        |                |        |                 | :            | 0/0  |
|                | Redirects   |                |                |        |                 | :            | 0/0  |
|                | Packet      | Too            | Big            |        |                 | :            | 0/0  |
|                | Router      | Advertisements |                |        |                 | :            | 4/0  |
|                | Router      | Solicitations  |                |        |                 | :            | 0/0  |
|                | Neighbor    |                | Advertisements |        |                 | :            | 0/0  |
|                | Neighbor    |                | Solicitations  |        |                 | :            | 3/0  |
|                | Duplicate   |                | router         | RA     | received        | :            | 0/0  |
|                | ICMPv6      | MLD            | Statistics     |        | (sent/received) |              |      |
|                | V1          | Queries        | :              |        | 0/0             |              |      |
|                | V2          | Queries        | :              |        | 0/0             |              |      |
|                | V1          | Reports        | :              |        | 0/0             |              |      |
|                | V2          | Reports        | :              |        | 11/0            |              |      |
|                | V1          | Leaves         | :              |        | 0/0             |              |      |
| Command        |             | History        |                |        |                 |              |      |
| Release        |             |                |                |        |                 | Modification |      |
| 10.07orearlier |             |                |                |        |                 | --           |      |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 42

| Command   | Information |         |     |         |     |           |     |     |
| --------- | ----------- | ------- | --- | ------- | --- | --------- | --- | --- |
| Platforms |             | Command |     | context |     | Authority |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | ipv6 | nd  | interface |     |     |     |     |     |
| ---- | ---- | --- | --------- | --- | --- | --- | --- | --- |
show ipv6 nd interface [<IF-NAME> | all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
Displaysneighbordiscoveryinformationforaninterface.Ifnooptionsarespecified,displays
informationforthedefaultVRF.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<IF-NAME> DisplaysinformationaboutthespecifiedIPv6enabledinterface.
| all-vrfs |     |     |     |     |     | DisplaysinformationaboutinterfacesinallVRFs. |     |     |
| -------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- |
vrf <VRF-NAME> DisplaysinformationaboutinterfacesinaparticularVRF.Or,if
<VRF-NAME>isnotspecified,informationforthedefaultVRFis
displayed.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowinginformationforallVRFs:
| switch#              | show       | ipv6                 | nd        | interface   |                              | all-vrfs  |             |         |
| -------------------- | ---------- | -------------------- | --------- | ----------- | ---------------------------- | --------- | ----------- | ------- |
| List                 | of IPv6    | Interfaces           |           | for         | VRF                          | default   |             |         |
| Interface            |            | 1/1/1                | is        | up          |                              |           |             |         |
| Admin                | state      |                      | is up     |             |                              |           |             |         |
| IPv6                 | address:   |                      |           |             |                              |           |             |         |
| IPv6                 | link-local |                      | address:  |             | fe80::7272:cfff:fee7:a8b9/64 |           |             | [VALID] |
| ICMPv6               |            | active               | timers:   |             |                              |           |             |         |
|                      | Last       | Router-Advertisement |           |             |                              | sent:     |             |         |
|                      | Next       | Router-Advertisement |           |             |                              | sent in:  |             |         |
| Router-Advertisement |            |                      |           | parameters: |                              |           |             |         |
|                      | Periodic   |                      | interval: | 200         | to                           | 600 secs  |             |         |
|                      | Router     | Preference:          |           | medium      |                              |           |             |         |
|                      | Send       | "Managed             |           | Address     | Configuration"               |           | flag: false |         |
|                      | Send       | "Other               | Stateful  |             | Configuration"               |           | flag: false |         |
|                      | Send       | "Current             |           | Hop Limit"  |                              | field: 64 |             |         |
|                      | Send       | "MTU"                | option    | value:      |                              | 1500      |             |         |
|                      | Send       | "Router              |           | Lifetime"   | field:                       | 1800      |             |         |
|                      | Send       | "Reachable           |           | Time"       | field:                       | 0         |             |         |
|                      | Send       | "Retrans             |           | Timer"      | field:                       | 0         |             |         |
|                      | Suppress   |                      | RA:       | true        |                              |           |             |         |
|                      | Suppress   |                      | MTU       | in RA:      | true                         |           |             |         |
IPv6RouterAdvertisement|43

| ICMPv6    | error   |             | message  | parameters: |     |     |     |     |
| --------- | ------- | ----------- | -------- | ----------- | --- | --- | --- | --- |
|           | Send    | redirects:  |          | false       |     |     |     |     |
| ICMPv6    | DAD     | parameters: |          |             |     |     |     |     |
|           | Current | DAD         | attempt: |             | 1   |     |     |     |
| List      | of IPv6 | Interfaces  |          | for         | VRF | red |     |     |
| Interface |         | 1/1/2       | is up    |             |     |     |     |     |
| Admin     | state   | is          | up       |             |     |     |     |     |
IPv6 address:
|                      | 2001::1/64 |                      | [VALID]   |             |                              |           |             |         |
| -------------------- | ---------- | -------------------- | --------- | ----------- | ---------------------------- | --------- | ----------- | ------- |
| IPv6                 | link-local |                      | address:  |             | fe80::7272:cfff:fee7:a8b9/64 |           |             | [VALID] |
| ICMPv6               | active     |                      | timers:   |             |                              |           |             |         |
|                      | Last       | Router-Advertisement |           |             |                              | sent:     |             |         |
|                      | Next       | Router-Advertisement |           |             |                              | sent in:  |             |         |
| Router-Advertisement |            |                      |           | parameters: |                              |           |             |         |
|                      | Periodic   |                      | interval: | 200         | to                           | 600 secs  |             |         |
|                      | Router     | Preference:          |           | medium      |                              |           |             |         |
|                      | Send       | "Managed             | Address   |             | Configuration"               |           | flag: false |         |
|                      | Send       | "Other               | Stateful  |             | Configuration"               |           | flag: false |         |
|                      | Send       | "Current             | Hop       | Limit"      |                              | field: 64 |             |         |
|                      | Send       | "MTU"                | option    | value:      |                              | 1500      |             |         |
|                      | Send       | "Router              | Lifetime" |             | field:                       | 1800      |             |         |
|                      | Send       | "Reachable           |           | Time"       | field:                       | 0         |             |         |
|                      | Send       | "Retrans             | Timer"    |             | field:                       | 0         |             |         |
|                      | Suppress   |                      | RA: true  |             |                              |           |             |         |
|                      | Suppress   |                      | MTU in    | RA:         | true                         |           |             |         |
| ICMPv6               | error      |                      | message   | parameters: |                              |           |             |         |
|                      | Send       | redirects:           |           | false       |                              |           |             |         |
| ICMPv6               | DAD        | parameters:          |           |             |                              |           |             |         |
|                      | Current    | DAD                  | attempt:  |             | 1                            |           |             |         |
Showinginformationforinterface1/1/1:
| switch#   | show  | ipv6  | nd    | interface |     | 1/1/1 |     |     |
| --------- | ----- | ----- | ----- | --------- | --- | ----- | --- | --- |
| Interface |       | 1/1/1 | is up |           |     |       |     |     |
| Admin     | state | is    | up    |           |     |       |     |     |
IPv6 address:
| IPv6                 | link-local |                      | address:  |             | fe80::7272:cfff:fee7:a8b9/64 |           |             | [VALID] |
| -------------------- | ---------- | -------------------- | --------- | ----------- | ---------------------------- | --------- | ----------- | ------- |
| ICMPv6               | active     |                      | timers:   |             |                              |           |             |         |
|                      | Last       | Router-Advertisement |           |             |                              | sent:     |             |         |
|                      | Next       | Router-Advertisement |           |             |                              | sent in:  |             |         |
| Router-Advertisement |            |                      |           | parameters: |                              |           |             |         |
|                      | Periodic   |                      | interval: | 200         | to                           | 600 secs  |             |         |
|                      | Router     | Preference:          |           | high        |                              |           |             |         |
|                      | Send       | "Managed             | Address   |             | Configuration"               |           | flag: false |         |
|                      | Send       | "Other               | Stateful  |             | Configuration"               |           | flag: false |         |
|                      | Send       | "Current             | Hop       | Limit"      |                              | field: 64 |             |         |
|                      | Send       | "MTU"                | option    | value:      |                              | 1500      |             |         |
|                      | Send       | "Router              | Lifetime" |             | field:                       | 1800      |             |         |
|                      | Send       | "Reachable           |           | Time"       | field:                       | 0         |             |         |
|                      | Send       | "Retrans             | Timer"    |             | field:                       | 0         |             |         |
|                      | Suppress   |                      | RA: true  |             |                              |           |             |         |
|                      | Suppress   |                      | MTU in    | RA:         | true                         |           |             |         |
| ICMPv6               | error      |                      | message   | parameters: |                              |           |             |         |
|                      | Send       | redirects:           |           | false       |                              |           |             |         |
| ICMPv6               | DAD        | parameters:          |           |             |                              |           |             |         |
|                      | Current    | DAD                  | attempt:  |             | 1                            |           |             |         |
ShowinginformationforthedefaultVRF:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 44

|                | switch#              | show ipv6            | nd           | interface   |                              |              |             |         |
| -------------- | -------------------- | -------------------- | ------------ | ----------- | ---------------------------- | ------------ | ----------- | ------- |
|                | List of              | IPv6 Interfaces      |              |             | for VRF                      | default      |             |         |
|                | Interface            | 1/1/1                | is           | up          |                              |              |             |         |
|                | Admin                | state                | is up        |             |                              |              |             |         |
|                | IPv6                 | address:             |              |             |                              |              |             |         |
|                | 2001::1/64           |                      | [VALID]      |             |                              |              |             |         |
|                | IPv6                 | link-local           | address:     |             | fe80::7272:cfff:fee7:a8b9/64 |              |             | [VALID] |
|                | ICMPv6               | active               | timers:      |             |                              |              |             |         |
|                | Last                 | Router-Advertisement |              |             |                              | sent: 6      | Secs        |         |
|                | Next                 | Router-Advertisement |              |             |                              | sent in:     | 7 Secs      |         |
|                | Router-Advertisement |                      |              | parameters: |                              |              |             |         |
|                | Periodic             |                      | interval:    |             | 3 to                         | 13 secs      |             |         |
|                | Router               | Preference:          |              |             | medium                       |              |             |         |
|                | Send                 | "Managed             |              | Address     | Configuration"               |              | flag: false |         |
|                | Send                 | "Other               | Stateful     |             | Configuration"               |              | flag: false |         |
|                | Send                 | "Current             |              | Hop         | Limit"                       | field: 64    |             |         |
|                | Send                 | "MTU"                | option       |             | value:                       | 1500         |             |         |
|                | Send                 | "Router              |              | Lifetime"   |                              | field: 1900  |             |         |
|                | Send                 | "Reachable           |              | Time"       | field:                       | 0            |             |         |
|                | Send                 | "Retrans             |              | Timer"      | field:                       | 0            |             |         |
|                | Suppress             |                      | RA:          | true        |                              |              |             |         |
|                | Suppress             |                      | MTU          | in RA:      | true                         |              |             |         |
|                | ICMPv6               | error                | message      | parameters: |                              |              |             |         |
|                | Send                 | redirects:           |              | false       |                              |              |             |         |
|                | ICMPv6               | DAD parameters:      |              |             |                              |              |             |         |
|                | Current              |                      | DAD attempt: |             | 1                            |              |             |         |
| Command        |                      | History              |              |             |                              |              |             |         |
| Release        |                      |                      |              |             |                              | Modification |             |         |
| 10.07orearlier |                      |                      |              |             |                              | --           |             |         |
| Command        |                      | Information          |              |             |                              |              |             |         |
| Platforms      |                      | Command              |              | context     |                              | Authority    |             |         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | ipv6 | nd  | interface |     | prefix |     |     |     |
| ---- | ---- | --- | --------- | --- | ------ | --- | --- | --- |
show ipv6 nd interface prefix [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowsIPv6prefixinformationforallVRFsoraspecificVRF.Ifnooptionsarespecified,shows
informationforthedefaultVRF.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
all-vrfs
ShowsprefixinformationforallVRFs.
| vrf | <VRF-NAME> |     |     |     |     | NameofaVRF. |     |     |
| --- | ---------- | --- | --- | --- | --- | ----------- | --- | --- |
IPv6RouterAdvertisement|45

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingprefixinformationforthedefaultVRF:
|     | switch#    | show ipv6       | nd interface |         | prefix   |     |
| --- | ---------- | --------------- | ------------ | ------- | -------- | --- |
|     | List of    | IPv6 Interfaces |              | for VRF | default  |     |
|     | List of    | IPv6 Prefix     | advertised   |         | on 1/1/1 |     |
|     | Prefix     | : 4545::/65     |              |         |          |     |
|     | Enabled    | : Yes           |              |         |          |     |
|     | Validlife  | time            | : 2592000    |         |          |     |
|     | Preferred  | lifetime        | :            | 604800  |          |     |
|     | On-link    | : Yes           |              |         |          |     |
|     | Autonomous | :               | Yes          |         |          |     |
ShowinginformationforVRFred:
|                | switch#    | show ipv6       | nd interface |         | prefix vrf   | red |
| -------------- | ---------- | --------------- | ------------ | ------- | ------------ | --- |
|                | List of    | IPv6 Interfaces |              | for VRF | red          |     |
|                | List of    | IPv6 Prefix     | advertised   |         | on 1/1/2     |     |
|                | Prefix     | : 2001::/64     |              |         |              |     |
|                | Enabled    | : Yes           |              |         |              |     |
|                | Validlife  | time            | : 2592000    |         |              |     |
|                | Preferred  | lifetime        | :            | 604800  |              |     |
|                | On-link    | : Yes           |              |         |              |     |
|                | Autonomous | :               | Yes          |         |              |     |
| Command        |            | History         |              |         |              |     |
| Release        |            |                 |              |         | Modification |     |
| 10.07orearlier |            |                 |              |         | --           |     |
| Command        |            | Information     |              |         |              |     |
| Platforms      |            | Command         | context      |         | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | ipv6    | nd interface |       | route     |       |             |
| ---- | ------- | ------------ | ----- | --------- | ----- | ----------- |
| show | ipv6 nd | interface    | route | [all-vrfs | | vrf | <VRF-NAME>] |
Description
DisplaysrouteinformationofallinterfacesinthedefaultVRF.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 46

| Parameter |     |     | Description                                  |     |     |     |     |
| --------- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
| all-vrfs  |     |     | DisplaysinformationaboutinterfacesinallVRFs. |     |     |     |     |
vrf <VRF-NAME>
DisplaysinformationaboutinterfacesinaparticularVRF.Or,if<VRF-NAME>isnot
specified,displaysinformationforthedefaultVRF.
Examples
Showingroutinginformationforinterface1/1/1inthedefaultVRF:
| switch# | show    |            | ipv6 nd    | interface  |     | route    |     |
| ------- | ------- | ---------- | ---------- | ---------- | --- | -------- | --- |
| List    | of IPv6 |            | Interfaces | for        | VRF | default  |     |
| List    | of IPv6 |            | Routes     | advertised |     | on 1/1/1 |     |
|         | Route   | : 1::/64   |            |            |     |          |     |
|         | Enabled | :          | Yes        |            |     |          |     |
|         | Route   | lifetime   | :          | 200        |     |          |     |
|         | Route   | preference |            | : high     |     |          |     |
Showingroutinginformationforinterface1/1/1inVRFred:
| switch#   | show        |            | ipv6 nd    | interface  |     | route vrf         | red |
| --------- | ----------- | ---------- | ---------- | ---------- | --- | ----------------- | --- |
| List      | of IPv6     |            | Interfaces | for        | VRF | red               |     |
| List      | of IPv6     |            | Routes     | advertised |     | on 1/1/2          |     |
|           | Route       | : 2::/64   |            |            |     |                   |     |
|           | Enabled     | :          | No         |            |     |                   |     |
|           | Route       | lifetime   | :          | 1800       |     |                   |     |
|           | Route       | preference |            | : low      |     |                   |     |
| Command   | History     |            |            |            |     |                   |     |
| Release   |             |            |            |            |     | Modification      |     |
| 10.10     |             |            |            |            |     | Commandintroduced |     |
| Command   | Information |            |            |            |     |                   |     |
| Platforms |             | Command    |            | context    |     | Authority         |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show      | ipv6 | nd     | ra dns      | search-list |            |     |     |
| --------- | ---- | ------ | ----------- | ----------- | ---------- | --- | --- |
| show ipv6 | nd   | ra dns | search-list |             | [vsx-peer] |     |     |
Description
Displaysdomainnameinformationonallinterfaces.
IPv6RouterAdvertisement|47

Parameter

vsx-peer

Examples

Description

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns search-list test.com
switch# show ipv6 nd ra dns search-list
Recursive DNS Search List on: 1

Suppress DNS Search List: Yes
DNS Search 1: test.com

lifetime

1800

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

show ipv6 nd ra dns server
show ipv6 nd ra dns server [vsx-peer]

Description

Displays DNS server information on all interfaces.

Parameter

vsx-peer

Examples

Description

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns server 2001::1
switch# show ipv6 nd ra dns server
Recursive DNS Server List on: 1

Suppress DNS Server List: Yes
DNS Server 1: 2001::1

lifetime 1800

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

48

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
IPv6RouterAdvertisement|49

Chapter 4

sFlow

sFlow

sFlow is a technology for monitoring traffic in switched or routed networks. The sFlow monitoring
system is comprised of:

n An sFlow Agent that runs on a network device, such as a switch. The agent uses sampling techniques

to capture information about the data traffic flowing through the device and forwards this
information to an sFlow collector.

n An sFlow Collector that receives monitoring information from sFlow agents. The collector stores this

information so that a network administrator can analyze it to understand network data flow patterns.

The sFlow UDP datagrams sent to a collector are not encrypted, therefore any sensitive information contained in

an sFlow sample is exposed.

sFlow agent

The sFlow agent on the switch provides ingress sampling of all forwarded layer 2 and layer 3 traffic on
LAG and Ethernet ports. High-availability is supported (packet sampling continues to work after switch-
over).

The sFlow agent can communicate with up to three sFlow collectors at the same time. The agent
communicates with collectors on the default VRF and non-default VRF.

Although you can configure very high sampling rates, the switch may drop samples if it cannot handle
the rate of sampled packets. High sampling rates may also cause high CPU usage resulting in control
plane performance issues.

A single sFlow datagram sent to a collector contains multiple flow and counter samples. The total
number of samples an sFlow datagram can contain varies depending on the settings for header size and
maximum datagram size.

Default settings

n sFlow is disabled on all interfaces.

n Collector port: UDP port 6343.

n sflow sampling mode: Ingress

n Sampling rate: 4096.

n Polling interval: 30 seconds.

n Header size: 128 bytes.

n Max datagram size: 1400 bytes.

Supported features

n Global sampling rate

n Global sampling mode (Ingress, Egress, and Both)

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

50

n Interface counters polling

n Agent IP configuration for IPv4 and IPv6

n Header size configuration

n Max datagram size configuration

n Ingress sampling for all forwarded traffic (L2, L3)

n Egress sampling for all forwarded traffic (L2, L3)

n Enable/Disable sFlow per interface

n Support for three remote collectors

n A collector can be defined on the default and non-default VRF

n Sampling on Ethernet and LAG interfaces

n High availability support (sampling continues to work after switch-over)

n Source IP support (setting source IP for sFlow datagrams sent to a remote collector)

For the 4100i, 6000, and 6100 switch series, collector can be defined only on the default VRF. Also, there is no

sampling of egress traffic.

Limitations

n Sampling rate cannot be set per interface (global only)

n sFlow is not configurable via SNMP

n sFlow egress global counters will increase for broadcast, unknown-unicast, & multicast (BUM) traffic.
However, the interface counters will not increase because it is flooded traffic. The output port in the
sFlow sampled packet for BUM traffic will be 0x80000000.

n When the sampling mode is configured as both, the ingress and egress packets may not be sampled

in equal proportions.

n The sampled packet count will not match the configured value when sFlow is configured but it will

converge after sampling around 500 packets.

n sFlow egress sampling is supported only on certain types of CPU generated traffic.

n The sFlow egress sampling on VxLAN tunnel is not supported and there will not be any indication to

the user when configuring sFlow.

Configuring the sFlow agent

Procedure

1. Configure one or more sFlow collectors with the command sflow collector. This determines

where the sFlow agent sends sFlow information.

2. Enable the sFlow agent on all interfaces, or on a specific interface, with the command sflow.

3. Define the address of the sFlow agent with the command sflow agent-ip.

4. By default, the source IP address for sFlow datagrams is set to the IP address of the outgoing

switch interface on which the sFlow client is communicating with a collector. Since the switch can
have multiple routing interfaces, datagrams can potentially be sent on different paths at different
times, resulting in different source IP addresses for the same client. To resolve this issue, define a
single source IP address. For details, see Single source IP address in the Fundamentals Guide.

5. For most deployments, the default values for the following settings do not need to be changed. If

your deployment requires different settings, change the default values with the indicated

sFlow | 51

commands:
| sFlow setting |     | Default value | Command | to change | it  |
| ------------- | --- | ------------- | ------- | --------- | --- |
Rateatwhichpacketsaresampled. 1inevery4096packets sflow sampling
| Rateatwhichtheswitchsendsdatato |     | 30seconds | sflow polling |     |     |
| ------------------------------- | --- | --------- | ------------- | --- | --- |
ansFlowcollector.
| SizeofthesFlowheader.         |     | 128bytes  | sflow header-size   |     |     |
| ----------------------------- | --- | --------- | ------------------- | --- | --- |
| MaximumsizeofansFlowdatagram. |     | 1400bytes | sflow max-datagram- |     |     |
size
| 6. ReviewsFlowconfigurationsettingswiththecommandshow |     | sflow. |     |     |     |
| ----------------------------------------------------- | --- | ------ | --- | --- | --- |
Example
Thisexamplecreatesthefollowingconfiguration:
n ConfiguresansFlowcollectorwiththeIPaddress10.10.20.209.
n EnablesthesFlowagentonallinterfaces.
n DefinesthesFlowagentIPaddresstobe10.10.1.5.
| switch(config)# | sflow collector | 10.10.20.209 |     |     |     |
| --------------- | --------------- | ------------ | --- | --- | --- |
| switch(config)# | sflow           |              |     |     |     |
| switch(config)# | sflow agent-ip  | 10.0.0.1     |     |     |     |
sFlow scenario
Inthisscenario,twohostssendsFlowtrafficthroughaswitchtoansFlowcollector.Thephysical
topologyofthenetworklookslikethis:
Procedure
1. EnablesFlowglobally.
| switch# config  |       |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
| switch(config)# | sflow |     |     |     |     |
2. SetthesFlowagentIPaddressto10.10.12.1.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 52

|     | switch(config)# |     | sflow agent-ip |     | 10.10.12.1 |
| --- | --------------- | --- | -------------- | --- | ---------- |
3. SetthesFlowcollectorIPaddressto10.10.12.2.
|     | switch(config)# |     | sflow collector |     | 18.2.2.2 |
| --- | --------------- | --- | --------------- | --- | -------- |
4. ConfiguresFLowsamplingrateandpollinginterval.
|     | switch(config)# |     | sflow sampling |     | 5000 |
| --- | --------------- | --- | -------------- | --- | ---- |
|     | switch(config)# |     | sflow polling  |     | 20   |
5. Configureinterface1/1/1withIPaddress10.10.10.1/24.
|     | switch(config)#    |     | interface   | 1/1/1 |               |
| --- | ------------------ | --- | ----------- | ----- | ------------- |
|     | switch(config-if)# |     | no shutdown |       |               |
|     | switch(config-if)# |     | ip address  |       | 10.10.10.1/24 |
|     | switch(config)#    |     | quit        |       |               |
6. Configureinterface1/1/2withIPaddress10.10.11.1/24.
|     | switch(config)#    |     | interface   | 1/1/2 |               |
| --- | ------------------ | --- | ----------- | ----- | ------------- |
|     | switch(config-if)# |     | no shutdown |       |               |
|     | switch(config-if)# |     | ip address  |       | 10.10.11.1/24 |
|     | switch(config)#    |     | quit        |       |               |
7. Configureinterface1/1/3withIPaddress10.10.12.1/24.
|     | switch(config)#    |     | interface   | 1/1/3 |               |
| --- | ------------------ | --- | ----------- | ----- | ------------- |
|     | switch(config-if)# |     | no shutdown |       |               |
|     | switch(config-if)# |     | ip address  |       | 10.10.12.1/24 |
|     | switch(config)#    |     | quit        |       |               |
8. VerifysFlowconfiguration
Thefollowingexampleisonlyapplicableforthe8360seriesswitch
|     | switch#      | show sflow    |     |     |     |
| --- | ------------ | ------------- | --- | --- | --- |
|     | sFlow Global | Configuration |     |     |     |
-----------------------------------------
|     | sFlow         |             |     |     | enabled                 |
| --- | ------------- | ----------- | --- | --- | ----------------------- |
|     | Collector     | IP/Port/Vrf |     |     | 10.10.10.2/6343/default |
|     | Agent Address |             |     |     | 10.0.0.1                |
|     | Sampling      | Rate        |     |     | 1024                    |
|     | Polling       | Interval    |     |     | 30                      |
|     | Header        | Size        |     |     | 128                     |
|     | Max Datagram  | Size        |     |     | 1400                    |
|     | Sampling      | Mode        |     |     | both                    |
|     | sFlow Status  |             |     |     |                         |
-----------------------------------------
|     | Running       | - Yes |             |     |     |
| --- | ------------- | ----- | ----------- | --- | --- |
|     | sFlow enabled | on    | Interfaces: |     |     |
-----------------------------------------
lag100
|     | sFlow Statistics |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- |
-----------------------------------------
|       | Number   | of Ingress | Samples |     | 200 |
| ----- | -------- | ---------- | ------- | --- | --- |
|       | Number   | of Egress  | Samples |     | 0   |
| sFlow | scenario |            | 2       |     |     |
Inthisscenario,twohostsconnectedtodifferentswitchessendsFlowtraffictoacollector.ALAGis
usedtoconnectthetwoswitches.Thephysicaltopologyofthenetworklookslikethis:
sFlow|53

Procedure
1. Configureswitch1.
a. EnablesFlowglobally.
switch# config
| switch(config)# | sflow |     |     |     |
| --------------- | ----- | --- | --- | --- |
b. SetthesFlowagentIPaddressto10.10.12.1.
| switch(config)# | sflow | agent-ip | 10.10.12.1 |     |
| --------------- | ----- | -------- | ---------- | --- |
c. SetthesFlowcollectorIPaddressto10.10.12.2.
| switch(config)# | sflow | collector |     | 10.10.12.2 |
| --------------- | ----- | --------- | --- | ---------- |
d. ConfiguresFLowsamplingrateandpollinginterval.
| switch(config)# | sflow | sampling | 5000 |     |
| --------------- | ----- | -------- | ---- | --- |
| switch(config)# | sflow | polling  | 10   |     |
e. CreateVLAN8.
| switch(config)#                  | vlan      | 8           |        |        |
| -------------------------------- | --------- | ----------- | ------ | ------ |
| switch(config-vlan-8)#           |           | no shutdown |        |        |
| switch(config)#                  | exit      |             |        |        |
| f. DefineLAG100andassignVLANvlan |           |             |        | 8toit. |
| switch(config)#                  | interface | lag         | 100    |        |
| switch(config-lag-if)#           |           | no shutdown |        |        |
| switch(config-lag-if)#           |           | no routing  |        |        |
| switch(config-lag-if)#           |           | vlan        | access | 8      |
| switch(config-lag-if)#           |           | lacp        | mode   | active |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 54

g. Configureinterface1/1/1.
| switch(config)#        |     | interface | 1/1/1      |     |     |
| ---------------------- | --- | --------- | ---------- | --- | --- |
| switch(config-if)#     |     | no        | shutdown   |     |     |
| switch(config-lag-if)# |     |           | no routing |     |     |
| switch(config-if)#     |     | vlan      | access     | 8   |     |
h. Configureinterface1/1/2and1/1/3asmembersofLAG100.
| switch#            | (config)#interface |           |          | 1/1/2 |     |
| ------------------ | ------------------ | --------- | -------- | ----- | --- |
| switch(config-if)# |                    | no        | shutdown |       |     |
| switch(config-if)# |                    | lag       | 100      |       |     |
| switch(config-if)# |                    | exit      |          |       |     |
| switch(config)#    |                    | interface | 1/1/3    |       |     |
| switch(config-if)# |                    | no        | shutdown |       |     |
| switch(config-if)# |                    | lag       | 100      |       |     |
| switch(config-if)# |                    | exit      |          |       |     |
i. Configureinterface1/1/4withIPaddress10.10.12.1/24.
| switch#            | (config)#interface |      |          | 1/1/4         |     |
| ------------------ | ------------------ | ---- | -------- | ------------- | --- |
| switch(config-if)# |                    | no   | shutdown |               |     |
| switch(config-if)# |                    | ip   | address  | 10.10.12.1/24 |     |
| switch(config-if)# |                    | quit |          |               |     |
j. VerifysFlowconfiguration.
Thefollowingexampleisonlyapplicableforthe8360seriesswitch
| switch#      | show | sflow         |     |     |     |
| ------------ | ---- | ------------- | --- | --- | --- |
| sFlow Global |      | Configuration |     |     |     |
-----------------------------------------
| sFlow         |             |      |     | enabled                 |     |
| ------------- | ----------- | ---- | --- | ----------------------- | --- |
| Collector     | IP/Port/Vrf |      |     | 10.10.10.2/6343/default |     |
| Agent Address |             |      |     | 10.0.0.1                |     |
| Sampling      | Rate        |      |     | 1024                    |     |
| Polling       | Interval    |      |     | 30                      |     |
| Header        | Size        |      |     | 128                     |     |
| Max Datagram  |             | Size |     | 1400                    |     |
| Sampling      | Mode        |      |     | both                    |     |
sFlow Status
-----------------------------------------
| Running       | - Yes |                |     |     |     |
| ------------- | ----- | -------------- | --- | --- | --- |
| sFlow enabled |       | on Interfaces: |     |     |     |
-----------------------------------------
lag100
sFlow Statistics
-----------------------------------------
| Number | of Ingress | Samples |     | 200 |     |
| ------ | ---------- | ------- | --- | --- | --- |
| Number | of Egress  | Samples |     | 0   |     |
2. Configureswitch2.
a. CreateVLAN8.
switch(config)#
|                                  |     | vlan      | 8           |        |        |
| -------------------------------- | --- | --------- | ----------- | ------ | ------ |
| switch(config-vlan-8)#           |     |           | no shutdown |        |        |
| switch(config)#                  |     | exit      |             |        |        |
| b. DefineLAG100andassignVLANvlan |     |           |             |        | 8toit. |
| switch(config)#                  |     | interface | lag         | 100    |        |
| switch(config-lag-if)#           |     |           | no shutdown |        |        |
| switch(config-lag-if)#           |     |           | no routing  |        |        |
| switch(config-lag-if)#           |     |           | vlan        | access | 8      |
| switch(config-lag-if)#           |     |           | lacp        | mode   | active |
sFlow|55

|       | c. Configureinterface1/1/1.                          |                    |         |           |             |         |                   |     |
| ----- | ---------------------------------------------------- | ------------------ | ------- | --------- | ----------- | ------- | ----------------- | --- |
|       | switch(config)#                                      |                    |         | interface |             | 1/1/1   |                   |     |
|       | switch(config-if)#                                   |                    |         | no        | shutdown    |         |                   |     |
|       | switch(config-lag-if)#                               |                    |         |           | no          | routing |                   |     |
|       | switch(config-if)#                                   |                    |         | vlan      | access      |         | 8                 |     |
|       | d. Configureinterface1/1/2and1/1/3asmembersofLAG100. |                    |         |           |             |         |                   |     |
|       | switch#                                              | (config)#interface |         |           |             | 1/1/2   |                   |     |
|       | switch(config-if)#                                   |                    |         | no        | shutdown    |         |                   |     |
|       | switch(config-if)#                                   |                    |         | lag       | 100         |         |                   |     |
|       | switch(config-if)#                                   |                    |         | exit      |             |         |                   |     |
|       | switch(config)-if#                                   |                    |         | interface |             | 1/1/3   |                   |     |
|       | switch(config-if)#                                   |                    |         | no        | shutdown    |         |                   |     |
|       | switch(config-if)#                                   |                    |         | lag       | 100         |         |                   |     |
|       | switch(config-if)#                                   |                    |         | exit      |             |         |                   |     |
| sFlow | agent                                                | commands           |         |           |             |         |                   |     |
| clear | sflow                                                | statistics         |         |           |             |         |                   |     |
| clear | sflow                                                | statistics         | {global |           | | interface |         | <INTERFACE-NAME>} |     |
Description
ThiscommandclearsthesFlowsamplestatisticscounterto0eithergloballyorforaspecificinterface.
| Parameter |     |     |     |     |     | Description                        |     |     |
| --------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
| global    |     |     |     |     |     | Specifiesallinterfacesontheswitch. |     |     |
interface <INTERFACE-NAME> Specifiesthenameofaninterfaceontheswitch.
Examples
ClearingtheglobalsFlowsamplestatisticscounterto0globally:
| switch(config)# |     |     | clear | sflow | statistics |     | global |     |
| --------------- | --- | --- | ----- | ----- | ---------- | --- | ------ | --- |
ClearingtheglobalsFlowsamplestatisticscounterto0forinterface1/1/1:
| switch(config)# |             |         | clear | sflow   | statistics |              | interface | 1/1/1 |
| --------------- | ----------- | ------- | ----- | ------- | ---------- | ------------ | --------- | ----- |
| Command         | History     |         |       |         |            |              |           |       |
| Release         |             |         |       |         |            | Modification |           |       |
| 10.07orearlier  |             |         |       |         |            | --           |           |       |
| Command         | Information |         |       |         |            |              |           |       |
| Platforms       |             | Command |       | context |            | Authority    |           |       |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 56

sflow
sflow
no sflow
Description
EnablesthesFlowagent.
n Intheconfigcontext,thiscommandenablesthesFlowagentgloballyonallinterfaces.
n Inanconfig-ifcontext,thiscommandenablesthesFlowagentonaspecificinterface.sFlowcannot
beenabledonamemberofaLAG,onlyontheLAG.
ThesFlowagentisdisabledbydefault.
ThenoformofthiscommanddisablesthesFlowagentanddeletesallsFlowconfigurationsettings,
eitherglobally,orforaspecificinterface.
Examples
EnablingsFlowgloballyonallinterfaces:
| switch(config)# | sflow |     |
| --------------- | ----- | --- |
DisablingsFlowgloballyonallinterfaces:
| switch(config)# | no sflow |     |
| --------------- | -------- | --- |
EnablingsFlowoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | sflow     |       |
DisablingsFlowoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | no sflow  |       |
EnablingsFlowoninterfacelag100:
| switch(config)#    | interface | lag100 |
| ------------------ | --------- | ------ |
| switch(config-if)# | sflow     |        |
DisablingsFlowoninterfacelag100:
| switch(config)#    | interface | lag100 |
| ------------------ | --------- | ------ |
| switch(config-if)# | no sflow  |        |
Command History
sFlow|57

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|     | config-if |     | rightsforthiscommand. |
| --- | --------- | --- | --------------------- |
sflow agent-ip
| sflow agent-ip    | <IP-ADDR>   |     |     |
| ----------------- | ----------- | --- | --- |
| no sflow agent-ip | [<IP-ADDR>] |     |     |
Description
DefinestheIPaddressofthesFlowagenttouseinsFlowdatagrams.Thisaddressmustbedefinedfor
sFlowtofunction.HPErecommendsthattheaddress:
n canuniquelyidentifytheswitch
n isreachablebythesFlowcollector
n doesnotchangewithtime
ThenoformofthiscommanddeletestheIPaddressofthesFlowagent.ThiscausessFlowtostop
workingandnodatagramswillbesenttothesFlowcollector.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Theagentaddressisusedto
identifytheswitchinallsFlowdatagramssenttosFlowcollectors.
ItisusuallysettoanIPaddressontheswitchthatisreachable
fromansFlowcollector.
Examples
Settingtheagentaddressto10.10.10.100:
| switch(config)# | sflow | agent-ip | 10.0.0.100 |
| --------------- | ----- | -------- | ---------- |
Settingtheagentaddressto2001:0db8:85a3:0000:0000:8a2e:0370:7334:
switch(config)# sflow agent-ip 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Removingtheaddressconfigurationfromtheswitch,whichresultsinsFlowbeingdisabled:
| switch(config)# | no  | sflow agent-ip |     |
| --------------- | --- | -------------- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 58

| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow collector
| sflow collector    | <IP-ADDR> | [port | <PORT>] | [vrf <VRF>] |        |
| ------------------ | --------- | ----- | ------- | ----------- | ------ |
| no sflow collector | <IP-ADDR> | [port | <PORT>] | [vrf        | <VRF>] |
Description
DefinesacollectortowhichthesFlowagentsendsdata.Uptothreecollectorscanbedefined.Atleast
onecollectorshouldbedefined,anditmustbereachablefromtheswitchforsFlowtowork.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
collector <IP-ADDR> SpecifiestheIPaddressofacollectorinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
port <PORT>
SpecifiestheUDPportonwhichtosendinformationtothesFlow
collector.Range:0to65536.Default:6343.
| vrf <VRF> |     |     | SpecifiestheVRFonwhichtosendinformationtothesFlow |     |     |
| --------- | --- | --- | ------------------------------------------------- | --- | --- |
collector.TheVRFmustbedefinedontheswitch.IfnoVRFis
specified,thedefaultVRF(default)isused.
Example
DefiningacollectorwithIPaddress10.10.10.100onUDPport6400:
| switch(config)#     | sflow | collector | 10.0.0.1     | port | 6400 |
| ------------------- | ----- | --------- | ------------ | ---- | ---- |
| Command History     |       |           |              |      |      |
| Release             |       |           | Modification |      |      |
| 10.07orearlier      |       |           | --           |      |      |
| Command Information |       |           |              |      |      |
sFlow|59

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow disable
sflow disable
Description
DisablesthesFlowagent,butretainsanyexistingsFlowconfigurationsettings.Thesettingsbecome
activeifthesFlowagentisre-enabled.
Example
DisablingsFlowsupport:
| switch(config)#     | sflow   | disable |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow header-size
| sflow header-size    | <SIZE>   |     |     |
| -------------------- | -------- | --- | --- |
| no sflow header-size | [<SIZE>] |     |     |
Description
SetsthesFlowheadersizeinbytes.
Thenoformofthiscommandsetstheheadersizetothedefaultvalueof128.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
header-size <SIZE> SpecifiesthesFlowheadersizeinbytes.Range:64to256.Default:
128.
Examples
Settingtheheadersizeto64bytes:
| switch(config)# | sflow | header-size | 64  |
| --------------- | ----- | ----------- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 60

Settingtheheadersizetothedefaultvalueof128bytes:
| switch(config)#     | no      | sflow header-size |              |
| ------------------- | ------- | ----------------- | ------------ |
| Command History     |         |                   |              |
| Release             |         |                   | Modification |
| 10.07orearlier      |         |                   | --           |
| Command Information |         |                   |              |
| Platforms           | Command | context           | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow max-datagram-size
| sflow max-datagram-size    |     | <SIZE>   |     |
| -------------------------- | --- | -------- | --- |
| no sflow max-datagram-size |     | [<SIZE>] |     |
Description
SetsthemaximumnumberofbytesthataresentinonesFlowdatagram.
Thenoformofthiscommandsetsmaximumnumberofbytestothedefaultvalueof1400.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
max-datagram-size <SIZE> Specifiesthemaximumdatagramsizeinbytes.Range:1to9000.
Default:1400.
Examples
Settingthedatagramsizeto1000bytes:
| switch(config)# | sflow | max-datagram-size | 1000 |
| --------------- | ----- | ----------------- | ---- |
Settingtheheadersizetothedefaultvalueof1400bytes:
| switch(config)#     | no  | sflow max-datagram-size |              |
| ------------------- | --- | ----------------------- | ------------ |
| Command History     |     |                         |              |
| Release             |     |                         | Modification |
| 10.07orearlier      |     |                         | --           |
| Command Information |     |                         |              |
sFlow|61

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| sflow      | mode          |     |          |         |       |
| ---------- | ------------- | --- | -------- | ------- | ----- |
| sflow mode | {ingress      | |   | egress   | | both} |       |
| no sflow   | mode {ingress |     | | egress | |       | both} |
Description
SetsthesFlowsamplingmode.Thedefaultmodeisingress.
Thenoformofthecommandsetsthesamplingmodetoingress.Executingthenoformofthe
commandwiththeingressoptionwillhavenoimpactasingressisthedefaultmode.
| Parameter |     |     |     |     | Description                         |
| --------- | --- | --- | --- | --- | ----------------------------------- |
| ingress   |     |     |     |     | Samplesonlyingresstraffic.          |
| egress    |     |     |     |     | Samplesonlyegresstraffic.           |
| both      |     |     |     |     | Samplesbothingressandegresstraffic. |
Examples
SettingthesFlowmodetoonlysampleegresstraffic:
| switch#         | configure |       | terminal |        |     |
| --------------- | --------- | ----- | -------- | ------ | --- |
| switch(config)# |           | sflow | mode     | egress |     |
SettingthesFlowmodetoonlysampleingresstraffic:
| switch#         | configure |       | terminal |         |     |
| --------------- | --------- | ----- | -------- | ------- | --- |
| switch(config)# |           | sflow | mode     | ingress |     |
SettingthesFlowmodetosamplebothsampleingressandegresstraffic:
| switch#         | configure |       | terminal |      |     |
| --------------- | --------- | ----- | -------- | ---- | --- |
| switch(config)# |           | sflow | mode     | both |     |
ResettingthesFlowsamplingmodetothedefaultofingressfrompreviouslyconfiguredmodeofegress:
| switch#         | configure |     | terminal |             |     |
| --------------- | --------- | --- | -------- | ----------- | --- |
| switch(config)# |           | no  | sflow    | mode egress |     |
| Command         | History   |     |          |             |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 62

| Release |     |     | Modification                                     |
| ------- | --- | --- | ------------------------------------------------ |
| 10.10   |     |     | Commandenabledonthe8320,8325,9300,and10000Switch |
Series.
| 10.07orearlier      |         |         | --        |
| ------------------- | ------- | ------- | --------- |
| Command Information |         |         |           |
| Platforms           | Command | context | Authority |
8360 config Administratorsorlocalusergroupmemberswithexecution
| 8320 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8325
9300
10000
sflow polling
| sflow polling    | <INTERVAL>   |     |     |
| ---------------- | ------------ | --- | --- |
| no sflow polling | [<INTERVAL>] |     |     |
Description
DefinestheglobalpollingintervalforsFlowinseconds.
Thenoformofthiscommandsetsthepollingintervaltothedefaultvalueof30seconds.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<INTERVAL> Specifiesthepollingintervalinseconds.Range:10to3600.
Default:30.
Examples
Settingthepollingintervalto10:
| switch(config)# | sflow | polling 10 |     |
| --------------- | ----- | ---------- | --- |
Settingthepollingintervaltothedefaultvalue.
| switch(config)#     | no  | sflow polling |              |
| ------------------- | --- | ------------- | ------------ |
| Command History     |     |               |              |
| Release             |     |               | Modification |
| 10.07orearlier      |     |               | --           |
| Command Information |     |               |              |
sFlow|63

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow sampling
| sflow sampling    | <RATE>   |     |     |
| ----------------- | -------- | --- | --- |
| no sflow sampling | [<RATE>] |     |     |
Description
DefinestheglobalsamplingrateforsFlowinnumberofpackets.Thedefaultsamplingrateis4096,
whichmeansthatoneinevery4096packetsissampled.Awarningmessageisdisplayedwhenthe
samplingrateissettolessthan4096andproceedsonlyafteruserconfirmation.
Thenoformofthiscommandsetsthesamplingratetothedefaultvalueof4096.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
sampling <RATE> Specifiesthesamplingrate.Range:1to1000000000.Default:
4096.
Examples
Settingthesamplingrateto5000:
| switch(config)# | sflow | sampling | 5000 |
| --------------- | ----- | -------- | ---- |
Settingthesamplingratetothedefault:
| switch(config)# | no  | sflow sampling |     |
| --------------- | --- | -------------- | --- |
Settingthesamplingrateto1000:
| switch(config)# | sflow | sampling | 1000 |
| --------------- | ----- | -------- | ---- |
Setting the sFlow sampling rate lower than 4096 is not recommended and might
| affect system | performance. |        |     |
| ------------- | ------------ | ------ | --- |
| Do you want   | to continue  | [y/n]? | y   |
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 64

| show       | sflow      |                   |     |            |
| ---------- | ---------- | ----------------- | --- | ---------- |
| show sflow | [interface | <INTERFACE-NAME>] |     | [vsx-peer] |
Description
ShowssFlowconfigurationsettingsandstatisticsforallinterfaces,orforaspecificinterface.Italso
displaysthecurrentstatusofsFlowonthedeviceandreportsanyerrorsthatrequireattention.
IfsFlowisenabledontheinterfacesassociatedwithalaginterface,thentheinterfaceswillnotbeshownas
separateentriesundersFlow enabled on Interfaceintheoutput.Onlytheassociatedlaginterfacewill
haveanentryinthecolumn.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
interface <INTERFACE-NAME> Specifiesthenameofaninterfaceontheswitch.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingsFlowinformationforallinterfaces:
| switch# | show sflow           |     |     |     |
| ------- | -------------------- | --- | --- | --- |
| sFlow   | Global Configuration |     |     |     |
-----------------------------------------
| sFlow     |             |     | enabled               |     |
| --------- | ----------- | --- | --------------------- | --- |
| Collector | IP/Port/Vrf |     | 10.0.0.2/6343/default |     |
10.0.0.3/6400/default
| Agent    | Address       |     | 10.0.0.1 |     |
| -------- | ------------- | --- | -------- | --- |
| Sampling | Rate          |     | 1024     |     |
| Polling  | Interval      |     | 30       |     |
| Header   | Size          |     | 128      |     |
| Max      | Datagram Size |     | 1400     |     |
| Sampling | Mode          |     | ingress  |     |
| sFlow    | Status        |     |          |     |
-----------------------------------------
| Running | - Yes      |             |     |     |
| ------- | ---------- | ----------- | --- | --- |
| sFlow   | enabled on | Interfaces: |     |     |
-----------------------------------------
1/1/2
1/1/3
lag100
| sFlow | Statistics |     |     |     |
| ----- | ---------- | --- | --- | --- |
-----------------------------------------
| Number | of Ingress | Samples | 200 |     |
| ------ | ---------- | ------- | --- | --- |
| Number | of Egress  | Samples | 120 |     |
ShowingsFlowinformationforinterface1/1/1:
| switch# | show sflow | interface | 1/1/1 |     |
| ------- | ---------- | --------- | ----- | --- |
sFlow|65

| sFlow configuration |     | - Interface | 1/1/1 |     |     |     |
| ------------------- | --- | ----------- | ----- | --- | --- | --- |
-----------------------------------------
| sFlow                                  |            |             | enabled |     |     |     |
| -------------------------------------- | ---------- | ----------- | ------- | --- | --- | --- |
| Sampling                               | Rate       |             | 1024    |     |     |     |
| Sampling                               | Mode       |             | both    |     |     |     |
| Number                                 | of Ingress | Samples     | 81      |     |     |     |
| Number                                 | of Egress  | Samples     | 20      |     |     |     |
| sFlow Sampling                         | Status     |             | success |     |     |     |
| ShowingsFlowinformationforinterfacelag |            |             | 10:     |     |     |     |
| switch#                                | show sflow | interface   | lag 10  |     |     |     |
| sFlow Configuration                    |            | - Interface | lag10   |     |     |     |
-----------------------------------------
| sFlow          |            |             | enabled |     |     |     |
| -------------- | ---------- | ----------- | ------- | --- | --- | --- |
| Sampling       | Rate       |             | 4096    |     |     |     |
| Sampling       | Mode       |             | both    |     |     |     |
| Number         | of Ingress | Samples     | 0       |     |     |     |
| Number         | of Egress  | Samples     | 0       |     |     |     |
| sFlow Sampling | Status     |             | error   |     |     |     |
| Sampling       | Status on  | LAG members |         |     |     |     |
------------------------------------
| Intf 1/1/2 |         |     | no agent     |     |     |     |
| ---------- | ------- | --- | ------------ | --- | --- | --- |
| Intf 1/1/3 |         |     | no agent     |     |     |     |
| Command    | History |     |              |     |     |     |
| Release    |         |     | Modification |     |     |     |
10.10
|     |     |     | CommandoutputupdatedtodisplaySampling |                   |           | Mode,Number |
| --- | --- | --- | ------------------------------------- | ----------------- | --------- | ----------- |
|     |     |     | of Ingress                            | Samples,andNumber | of Egress | Samplesfor  |
8320,8325,9300,and10000seriesswitches.
| 10.07orearlier |             |         | --        |     |     |     |
| -------------- | ----------- | ------- | --------- | --- | --- | --- |
| Command        | Information |         |           |     |     |     |
| Platforms      | Command     | context | Authority |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 66

Chapter 5

DHCP

DHCP

The Dynamic Host Configuration Protocol (DHCP) enables the automatic assignment of IP addresses and
other configuration settings to network devices.

DHCP is composed of three components: DHCP server, DHCP client, and DHCP relay agent.

The DHCP server contains the IP addresses and configuration settings for a network as defined by a
network administrator. It responds to DHCP requests issued by DHCP clients, returning the requested
network configuration settings.

The DHCP client runs on a network device. It issues a request to a DHCP server to obtain an IP address
for the network device, and other network settings.

The DHCP relay agent acts an intermediary, forwarding DHCP requests/response between DHCP
clients/servers on different networks. This enables DHCP clients to use the services of DHCP servers that
are not on the same subnet on which they are located.

DHCP client

By default, the switch operates as a DHCP client on the management interface allowing it to
automatically obtain an IP address from a DHCP server on the network to which it is connected.

DHCP client commands

ip dhcp

ip dhcp
no ip dhcp

Description

Enables the DHCP client on the management interface or any interface VLAN to automatically obtain an
IP address from a DHCP server on the network. By default, the DHCP client is enabled on the
management interface and VLAN 1.

The no form of the command disables DHCP mode and is supported only on interface VLANs; it is not
supported on the management interface.

Examples

Enabling the DHCP client on the management interface:

switch(config)# interface mgmt
switch(config-if-mgmt)# ip dhcp
switch(config-if-mgmt)# no shutdown

Enabling the DHCP client on the interface vlan 1:

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

67

| switch(config)#         | interface | vlan        | 1   |     |     |
| ----------------------- | --------- | ----------- | --- | --- | --- |
| switch(config-if-vlan)# |           | ip dhcp     |     |     |     |
| switch(config-if-vlan)# |           | no shutdown |     |     |     |
DisablingtheDHCPclientontheinterfacevlan1:
| switch(config)#         | interface | vlan       | 1   |     |     |
| ----------------------- | --------- | ---------- | --- | --- | --- |
| switch(config-if-vlan)# |           | no ip dhcp |     |     |     |
EnablingtheDHCPclientontheinterfacevlan4undernon-defaultVRF:
| switch(config)#         | interface | vlan       | 4   |     |     |
| ----------------------- | --------- | ---------- | --- | --- | --- |
| switch(config-if-vlan)# |           | vrf attach | red |     |     |
switch(config-if-vlan)#
ip dhcp
Iftheinterfaceisnotenabled,youcanenableitbyenteringtheno shutdowncommand.
ip dhcpissupportedonlyononevlanatatime.
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config-if-mgmt Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     | rightsforthiscommand. |     |     |
| --- | -------------- | --- | --------------------- | --- | --- |
show ip dhcp
show ip dhcp
Description
DisplaysDHCPIPv4informationontheports.
Examples
DisplayingtheDHCPIPv4informationontheports:
| switch# show | ip dhcp |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- |
INTERFACE-NAME ADDRESS DEFAULT_GATEWAY DOMAIN_NAME VRF DNS-SERVERS
--------------------------------------------------------------------------------------------
-------------
| vlan1           | 10.254.239.10/27 |     |     | domain.com | default 50.0.0.2, |
| --------------- | ---------------- | --- | --- | ---------- | ----------------- |
| 50.0.0.3,       | 50.0.0.4         |     |     |            |                   |
| Command History |                  |     |     |            |                   |
DHCP|68

| Release             |         |         | Modification       |
| ------------------- | ------- | ------- | ------------------ |
| 10.09orearlier      |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| DHCP relay | agent |     |     |
| ---------- | ----- | --- | --- |
ThefunctionoftheDHCPrelayagentistoforwardtheDHCPmessagestoothersubnetssothatthe
DHCPserverdoesnothavetobeonthesamesubnetastheDHCPclients.TheDHCPrelayagent
transfersDHCPmessagesfromtheDHCPclientslocatedonasubnetwithoutaDHCPserver,toother
subnets.ItalsorelaysanswersfromDHCPserverstoDHCPclients.
| Supported interfaces |     |     |     |
| -------------------- | --- | --- | --- |
TheDHCPrelayagentissupportedonlayer3interfaces,layer3VLANinterfaces,andLAGinterfaces.
DHCPrelayisnotsupportedonthemanagementinterface.
VRF support
TheDHCPrelayagentisVRFawareandbehavesasfollowswhenVRFsaredefinedontheswitch:
n DHCPclientrequestsreceivedonaninterfaceareforwardedtotheconfiguredserversviatheVRF
thattheinterfaceispartof.
n DHCPserverresponsesreceivedonaninterfaceareforwardedtotheclientthatisreachableviathe
VRFthattheinterfaceispartof.
| DHCP server | interoperation |     |     |
| ----------- | -------------- | --- | --- |
BothDHCPrelayandDHCPservercanbeconfiguredonthesameVRF.
| DHCPv4 relay | agent         |     |     |
| ------------ | ------------- | --- | --- |
| Hop count in | DHCP requests |     |     |
WhenaDHCPclientbroadcastsrequest,theDHCPrelayagentintheswitchreceivesthepacketsand
forwardsthemtotheDHCPserverasunicastrequests.Duringthisprocess,theDHCPrelayagent
incrementsthehopcountbeforeforwardingDHCPpacketstotheserver.TheDHCPserver,inturn,
includesthehopcountintheDHCPheaderintheresponsesentbacktoaDHCPclient.
| DHCP relay | option 82 |     |     |
| ---------- | --------- | --- | --- |
Option82iscalledtherelayagentinformationoption.WhenaDHCPrelayagentforwardsclient-
originatedDHCPpacketstoaDHCPserver,theoption82fieldisinserted/replaced,orthepacketwith
thisoptionisdropped.Serversrecognizingtherelayagentinformationoptionmayusetheinformation
toimplementpoliciesfortheassignmentofIPaddressesandotherparameters.Therelayagentrelays
theserver-to-clientrepliestotheclient.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 69

If a second relay agent is configured to add its own option 82 information, it can encapsulate option 82
information in messages from a first relay agent. The DHCP server uses the option 82 information from
both relay agents to decide the IP address for the client.

Inter-VRF DHCP relay

The DHCP relay agent supports anycast gateway using option 82 sub-option 5 (RFC 3527). The DHCP
relay discovery packet is filled with the client's gateway IP address in sub-option 5 (discovery packet).
The DHCP server uses this information to offer an IP address from the right pool. Pool selection occurs
by matching the default gateway configuration settings on the DHCP server with the requested gateway
IP address in sub-option 5 in the discovery packet.

The switch uses DHCP relay sub-option 151 to enable DHCP relay to forward discovery and reply
packets between VXLAN DHCP clients and DHCP servers even when they are on different overlay or
underlay VRFs and the DHCP-server is reachable on the default VRF or one of the overlay VRFs.

In general deployments, a renewal of a DHCP client's IP occurs when the client sends a request to the
DHCP server directly. In the case of EVPN VXLAN clients, the DHCP server is not directly reachable.
Instead, the renewal request is sent to the DHCP relay. DHCP relay agent fills the option 82 sub-option
11 field in the DHCP discovery packet with the client's gateway IP on the VTEP (which is the relay
interface IP address of the VTEP) and the DHCP server returns a DHCP offer reply packet with option 54
set to the DHCP server Identifier. When the reply packet is received by the client, the client uses the IP in
option 54 to sent subsequent renewal requests to this IP (VTEP's Relay Interface IP) using sub-option 11
(also known as the Server ID Override Sub-option). Refer to RFC 5107 for more details.

Sub-options 5,11,151,152 are filled in the discover packet, only if a source IP address is defined (using
the command ip source-address) for the given DHCP server's source VRF. If the server does not
understand sub-option 151, then the server will add sub-option 152 in offer packet.

In an inter-VRF situation, when both DHCP relay and DHCP snooping are enabled on the switch with
option 82, DHCPv4 clients will not receive an IP address.

Configuring a BOOTP/DHCP relay gateway

The DHCP relay agent selects the lowest-numbered IP address on the interface to use for DHCP
messages. The DHCP server then uses this IP address when it assigns client addresses. However, this IP
address may not be the same subnet as the one on which the client needs the DHCP service. This
feature provides a way to configure a gateway address for the DHCP relay agent to use for relayed
DHCP requests, rather than the DHCP relay agent automatically assigning the lowest-numbered IP
address.

When configuring a bootp-gateway, dhcp-smart-relay will be ineffective. This can occur with dhcp-relay as well.

DHCP smart relay

The DHCP Smart Relay feature first attempts to use the primary IP address from the client-connected
interfaces as a gateway IP address (giaddr) and as an IP address for pool selection. If the DHCP server
does not reply to the DHCP discover messages with the primary IP address, the feature attempts to use
secondary IP addresses in sequential order from the lowest to the highest. The DHCP Smart Relay
forwards three client discover messages with every IP address configured on the client interface until it
receives a response from the server. If the list of IP addresses from the client-connected interface is
exhausted or the client times out, the DHCP Smart Relay uses the primary IP address. If the DHCP Smart
Relay is not configured, the giaddr is the lowest IP address on the interface.

The DHCP Smart Relay maintains the client cache which includes the information about the client,
giaddr, retry count for giaddr, port, the total number of processed discovery messages the timestamp of

DHCP | 70

the discover packets. This client cache is rebuilt upon high availability and VSF switchover, VSX-MM
(redundancy) switchover, and when the switch reboots.

DHCP Smart Relay is only supported for IPv4.

Configuring the DHCPv4 relay agent

Prerequisites

n An enabled layer 3 interface.

Procedure

1. The DHCPv4 relay agent is enabled by default. If it was previously disabled, enable it with the

command dhcp-relay.

2. Configure one or more IP helper addresses with the command ip helper-address. This

determines where the DHCPv4 agent forwards DHCP requests. IP helper addresses can be
configured on layer 3 interfaces, layer 3 VLAN interfaces, and LAG interfaces.

3.

If you want to modify the content of forwarded DHCP packets or drop DHCP packets, configure
option 82 support with the command dhcp-relay option 82.

4. Define the gateway address that the DHCPv4 agent will use with the command ip bootp-gateway.

5.

If required, enable the hop count increment feature with the command dhcp-relay hop-count-
increment.

6. Review DHCPv4 relay agent configuration settings with the commands show dhcp-relay, show ip

helper-address, and show dhcp-relay bootp-gateway.

Example

This example creates the following configuration:

n Enables the DHCPv4 relay agent.

n Enables interface 1/1/1 and assigns an IPv4 address to it. (By default, all interfaces are layer 3 and

disabled.)

n Defines an IP helper address of 10.10.20.209 on the interface.

n Enables DHCP option 82 support and replaces all option 82 information with the values from the

switch with the switch MAC address as the remote ID.

On 4100i, 6000 and 6100 series switches, only SVIs are supported.

switch(config)# dhcp-relay
switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# ip address 198.51.100.1/24
switch(config-if)# ip helper-address 10.10.20.209
switch(config-if)# exit
switch(config)# dhcp-relay option 82 replace mac
switch# show dhcp-relay

: enabled
DHCP Relay Agent
DHCP Request Hop Count Increment : enabled
Option 82

: disabled

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

71

|     | Response   | Validation  |        |     | : disabled |     |     |
| --- | ---------- | ----------- | ------ | --- | ---------- | --- | --- |
|     | Option     | 82 Handle   | Policy |     | : replace  |     |     |
|     | Remote     | ID          |        |     | : mac      |     |     |
|     | DHCP Relay | Statistics: |        |     |            |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|     | 60         |        | 10  |             | 60  |     | 10  |
| --- | ---------- | ------ | --- | ----------- | --- | --- | --- |
|     | DHCP Relay | Option | 82  | Statistics: |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|        | 50    |          | 8   |     | 50  |     | 8   |
| ------ | ----- | -------- | --- | --- | --- | --- | --- |
| DHCPv4 | relay | scenario | 1   |     |     |     |     |
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
Procedure
1. DHCPrelayisenabledbydefault.Ifitwaspreviouslydisabled,enableit.
|     | switch#         |     | config |            |     |     |     |
| --- | --------------- | --- | ------ | ---------- | --- | --- | --- |
|     | switch(config)# |     |        | dhcp-relay |     |     |     |
2. DefineanIPv4helperaddressoninterfaces1/1/1and1/1/2.
|     | switch(config)#    |     |     | interface         | 1/1/1           |             |     |
| --- | ------------------ | --- | --- | ----------------- | --------------- | ----------- | --- |
|     | switch(config-if)# |     |     | ip address        | 192.168.2.11/24 |             |     |
|     | switch(config-if)# |     |     | ip helper-address |                 | 192.168.1.1 |     |
switch(config-if)#
|     |                    |     |     | interface         | 1/1/2           |             |     |
| --- | ------------------ | --- | --- | ----------------- | --------------- | ----------- | --- |
|     | switch(config-if)# |     |     | ip address        | 192.168.2.12/24 |             |     |
|     | switch(config-if)# |     |     | ip helper-address |                 | 192.168.1.1 |     |
3. VerifyDHCPrelayconfiguration.
DHCP|72

|     | switch#          | show dhcp-relay |           |           |            |     |
| --- | ---------------- | --------------- | --------- | --------- | ---------- | --- |
|     | DHCP Relay       | Agent           |           |           | : enabled  |     |
|     | DHCP Request     |                 | Hop Count | Increment | : enabled  |     |
|     | Option           | 82              |           |           | : disabled |     |
|     | Source-Interface |                 |           |           | : disabled |     |
|     | Response         | Validation      |           |           | : disabled |     |
|     | Option           | 82 Handle       | Policy    |           | : replace  |     |
|     | Remote           | ID              |           |           | : mac      |     |
|     | DHCP Relay       | Statistics:     |           |           |            |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|     | 60         |        | 10  |             | 60  | 10  |
| --- | ---------- | ------ | --- | ----------- | --- | --- |
|     | DHCP Relay | Option | 82  | Statistics: |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|        | 50                |           | 8              |                   | 50  | 8   |
| ------ | ----------------- | --------- | -------------- | ----------------- | --- | --- |
|        | switch#           | show ip   | helper-address |                   |     |     |
|        | IP Helper         | Addresses |                |                   |     |     |
|        | Interface:        | 1/1/1     |                |                   |     |     |
|        | IP Helper         | Address   |                | VRF               |     |     |
|        | ----------------- |           |                | ----------------- |     |     |
|        | 192.168.1.1       |           |                | default           |     |     |
|        | Interface:        | 1/1/2     |                |                   |     |     |
|        | IP Helper         | Address   |                | VRF               |     |     |
|        | ----------------- |           |                | ----------------- |     |     |
|        | 192.168.1.1       |           |                | default           |     |     |
| DHCPv4 | relay scenario    |           | 2              |                   |     |     |
Inthisscenario,thetwohostcomputerscommunicatewithtwodifferentDHCPservers.Eachserveris
reachedonadifferentVRF.Thephysicaltopologyofthenetworklookslikethis:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 73

Procedure
1. CreatethetwoVRFs.
| switch#         | config |           |     |
| --------------- | ------ | --------- | --- |
| switch(config)# |        | vrf vrf 1 |     |
| switch(config)# |        | vrf vrf 2 |     |
2. Configureinterface1/1/1.SetitsIPaddress,associateitwithVRF1,anddefinethehelperIP
addresstoreachDHCPserver1.
| switch(configif)# |     | interface         | 1/1/1      |
| ----------------- | --- | ----------------- | ---------- |
| switch(configif)# |     | vrf attach        | vrf1       |
| switch(configif)# |     | ip address        | 20.0.0.1/8 |
| switch(configif)# |     | ip helper-address | 10.0.10.2  |
3. Configureinterface1/1/2.SetitsIPaddressandassociateitwithVRF1.
switch(configif)#
|                   |     | interface  | 1/1/2        |
| ----------------- | --- | ---------- | ------------ |
| switch(configif)# |     | vrf attach | vrf1         |
| switch(configif)# |     | ip address | 10.0.10.1/24 |
4. Configureinterface1/1/3.SetitsIPaddressandassociateitwithVRF1.
| switch(configif)# |     | interface  | 1/1/3      |
| ----------------- | --- | ---------- | ---------- |
| switch(configif)# |     | vrf attach | vrf2       |
| switch(configif)# |     | ip address | 9.0.0.1/24 |
5. Configureinterface1/1/4.SetitsIPaddress,associateitwithVRF2,anddefinethehelperIP
addresstoreachDHCPserver2.
| switch(configif)# |          | interface         | 1/1/4      |
| ----------------- | -------- | ----------------- | ---------- |
| switch(configif)# |          | vrf attach        | vrf2       |
| switch(configif)# |          | ip address        | 30.0.0.1/8 |
| switch(configif)# |          | ip helper-address | 9.0.0.2    |
| DHCPv4 relay      | scenario | 3                 |            |
Inthisscenario,hostonswitch1reachestheDHCPserveronswitchtwoviaaLAG.Thephysical
topologyofthenetworklookslikethis:
DHCP|74

Procedure
1. Onswitch1:
a. CreateLAG100andassignanIPaddresstoit.
switch# config
| switch(config)#        | interface |      | lag 100  |              |
| ---------------------- | --------- | ---- | -------- | ------------ |
| switch(config-lag-if)# |           | no   | shutdown |              |
| switch(config-lag-if)# |           | ip   | address  | 10.0.10.1/24 |
| switch(config-lag-if)# |           | lacp | mode     | active       |
| switch(config-lag-if)# |           | exit |          |              |
b. AssignanIPaddresstointerface1/1/1andanIPhelperaddresstoreachtheDHCPserver.
| switch(config)#    | interface |                | 1/1/1      |         |
| ------------------ | --------- | -------------- | ---------- | ------- |
| switch(config-if)# | ip        | address        | 20.0.0.1/8 |         |
| switch(config-if)# | ip        | helper-address |            | 9.0.0.2 |
c. Assigninterfaces1/1/2and1/1/3toLAG100.
| switch(config-if)# | interface |     | 1/1/2 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | interface |     | 1/1/3 |     |
| switch(config-if)# | lag       | 100 |       |     |
d. Createaroutebetween10.0.10.2and9.0.0.0.
| switch(config)# | ip route | 9.0.0.0/24 |     | 10.0.10.2 |
| --------------- | -------- | ---------- | --- | --------- |
2. Onswitch2:
a. CreateLAG100andassignanIPaddresstoit.
switch# config
| switch(config)#        | interface |     | lag 100  |     |
| ---------------------- | --------- | --- | -------- | --- |
| switch(config-lag-if)# |           | no  | shutdown |     |
switch(config-lag-if)#
|                        |     | ip   | address | 10.0.10.2/24 |
| ---------------------- | --- | ---- | ------- | ------------ |
| switch(config-lag-if)# |     | lacp | mode    | active       |
| switch(config-lag-if)# |     | exit |         |              |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 75

|        | b. AssignanIPaddresstointerface1/1/3.       |            |            |           |
| ------ | ------------------------------------------- | ---------- | ---------- | --------- |
|        | switch(config)#                             | interface  | 1/1/3      |           |
|        | switch(config-if)#                          | ip address | 9.0.0.1/24 |           |
|        | c. Assigninterfaces1/1/2and1/1/3toLAG100.   |            |            |           |
|        | switch(config-if)#                          | interface  | 1/1/2      |           |
|        | switch(config-if)#                          | lag        | 100        |           |
|        | switch(config-if)#                          | interface  | 1/1/3      |           |
|        | switch(config-if)#                          | lag        | 100        |           |
|        | d. Createaroutebetween20.0.0.0and10.0.10.1. |            |            |           |
|        | switch(config)#                             | ip route   | 20.0.0.0/8 | 10.0.10.1 |
| DHCPv4 | relay commands                              |            |            |           |
dhcp-relay
dhcp-relay
no dhcp-relay
Description
EnablesDHCPrelaysupport.DHCPrelayisenabledbydefault.DHCPrelayisnotsupportedonthe
managementinterface.
ThenoformofthiscommanddisablesDHCPrelaysupport.
Examples
ThisexampleenablesDHCPrelaysupport.
| switch(config)# | dhcp-relay |     |     |     |
| --------------- | ---------- | --- | --- | --- |
ThisexampleremovesDHCPrelaysupport.
| switch(config)# | no          | dhcp-relay |              |     |
| --------------- | ----------- | ---------- | ------------ | --- |
| Command         | History     |            |              |     |
| Release         |             |            | Modification |     |
| 10.07orearlier  |             |            | --           |     |
| Command         | Information |            |              |     |
| Platforms       | Command     | context    | Authority    |     |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
DHCP|76

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8360
9300
10000
| dhcp-relay hop-count-increment |                     |     |     |
| ------------------------------ | ------------------- | --- | --- |
| dhcp-relay hop-count-increment |                     |     |     |
| no dhcp-relay                  | hop-count-increment |     |     |
Description
EnablestheDHCPrelayhopcountincrementfeature,whichcausestheDHCPrelayagenttoincrement
thehopcountinallrelayedDHCPpackets.Hopcountisenabledbydefault.
Thenoformofthiscommanddisablesthehopcountincrementfeature.
Examples
Enablingthehopcountincrementfeature.
| switch(config)# | dhcp-relay |     | hop-count-increment |
| --------------- | ---------- | --- | ------------------- |
Disablingthehopcountincrementfeature.
| switch(config)#     | no      | dhcp-relay | hop-count-increment |
| ------------------- | ------- | ---------- | ------------------- |
| Command History     |         |            |                     |
| Release             |         |            | Modification        |
| 10.07orearlier      |         |            | --                  |
| Command Information |         |            |                     |
| Platforms           | Command | context    | Authority           |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
9300
10000
| dhcp-relay l2vpn-clients |               |     |     |
| ------------------------ | ------------- | --- | --- |
| dhcp-relay l2vpn-clients |               |     |     |
| no dhcp-relay            | l2vpn-clients |     |     |
Description
EnablesforwardingofpacketsfromL2VPNclients.Forwardingisenabledbydefault.
ThenoformofthiscommanddisablesforwardingofpacketsfromL2VPNclients.
Example
EnablingforwardingofpacketsfromL2VPNclients.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 77

| switch(config)# |     | dhcp-relay | l2vpn-clients |     |     |
| --------------- | --- | ---------- | ------------- | --- | --- |
switch(config)#
|                |             | no  | dhcp-relay l2vpn-clients |              |     |
| -------------- | ----------- | --- | ------------------------ | ------------ | --- |
| Command        | History     |     |                          |              |     |
| Release        |             |     |                          | Modification |     |
| 10.07orearlier |             |     |                          | --           |     |
| Command        | Information |     |                          |              |     |
| Platforms      | Command     |     | context                  | Authority    |     |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --------------------- | --- |
8360
9300
10000
| dhcp-relay | option | 82          |            |                   |     |
| ---------- | ------ | ----------- | ---------- | ----------------- | --- |
| dhcp-relay | option | 82 {replace | [validate] | | drop [validate] | |   |
keep | source-interface | validate [replace | drop]} [ip | mac]
no dhcp-relay option 82 {replace [validate] | drop [validate] |
keep | source-interface | validate [replace | drop]} [ip | mac]
Description
ConfiguresthebehaviorofDHCPrelayoption82.ADHCPrelayagentcanreceiveamessagefrom
anotherDHCPrelayagenthavingoption82.Therelayinformationfromthepreviousrelayagentis
replacedbydefault.
ThenoformofthiscommanddisablestheDHCPrelayoption82configurations.
| Parameter |     |     |     | Description                                          |     |
| --------- | --- | --- | --- | ---------------------------------------------------- | --- |
| replace   |     |     |     | Replacetheexistingoption82fieldinaninboundclientDHCP |     |
packetwiththeinformationfromtheswitch.TheremoteIDand
circuitIDinformationfromthefirstrelayagentislost.Default.
| validate |     |     |     | Validateoption82informationinDHCPserverresponsesand |     |
| -------- | --- | --- | --- | --------------------------------------------------- | --- |
dropinvalidresponses.
| drop |     |     |     | DropanyinboundclientDHCPpacketthatcontainsoption82 |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
information.
| keep |     |     |     | Keeptheexistingoption82fieldinaninboundclientDHCP |     |
| ---- | --- | --- | --- | ------------------------------------------------- | --- |
packet.TheremoteIDandcircuitIDinformationfromthefirst
relayagentispreserved.
source-interface
ConfigurestheDHCPrelaytouseaconfiguredsourceIPaddress
forinter-VRFserverreachability.SetthesourceIPaddresswith
thecommandip source-interface.
ip
UsetheIPaddressoftheinterfaceonwhichtheclientDHCP
packetenteredtheswitchastheoption82remoteID.
DHCP|78

| Parameter |     |     | Description                                       |
| --------- | --- | --- | ------------------------------------------------- |
| mac       |     |     | UsetheMACaddressoftheswitchastheoption82remoteID. |
Default.
Example
ThisexampleenablesDHCPoption82supportandreplacesalloption82informationwiththevalues
fromtheswitch,withtheswitchMACaddressastheremoteID.
| switch(config)#     | dhcp-relay | option  | 82 replace mac |
| ------------------- | ---------- | ------- | -------------- |
| Command History     |            |         |                |
| Release             |            |         | Modification   |
| 10.07orearlier      |            |         | --             |
| Command Information |            |         |                |
| Platforms           | Command    | context | Authority      |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
9300
10000
dhcp-smart-relay
dhcp-smart-relay
no dhcp-smart-relay
Description
EnablesDHCPSmartRelayonthedeviceandonalltheinterfaceswhereIPhelperaddressesare
configured.Disabledbydefaultatthedevicelevel.Notsupportedonthemanagementinterface.
ThenoformofthiscommanddisablesDHCPSmartRelay.
PriortoenablingDHCPSmartRelay,enableIPhelperaddressconfigurationandconfiguresecondaryIP
addressesontheinterface.
Examples
EnablingDHCPSmartRelay:
| switch(config)# | dhcp-smart-relay |     |     |
| --------------- | ---------------- | --- | --- |
DisablingDHCPSmartRelaysupport:
| switch(config)# | no  | dhcp-smart-relay |     |
| --------------- | --- | ---------------- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 79

| Command   |     | History     |         |     |         |     |                    |     |     |     |
| --------- | --- | ----------- | ------- | --- | ------- | --- | ------------------ | --- | --- | --- |
| Release   |     |             |         |     |         |     | Modification       |     |     |     |
| 10.10     |     |             |         |     |         |     | Commandintroduced. |     |     |     |
| Command   |     | Information |         |     |         |     |                    |     |     |     |
| Platforms |     |             | Command |     | context |     | Authority          |     |     |     |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     |     |     |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
8360
9300
10000
| diag-dump |     | dhcp-relay |     | basic |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- |
| diag-dump |     | dhcp-relay |     | basic |     |     |     |     |     |     |
Description
DumpsDHCPrelayconfigurationsforallinterfaces.
Examples
ThisexampleenablesDHCPrelaysupport.
|     | switch# | diag-dump |     | dhcp-relay |     | basic |     |     |     |     |
| --- | ------- | --------- | --- | ---------- | --- | ----- | --- | --- | --- | --- |
=========================================================================
|     | [Start] | Feature |     | dhcp-relay |     | Time | : Sun | Apr 26 06:38:10 | 2020 |     |
| --- | ------- | ------- | --- | ---------- | --- | ---- | ----- | --------------- | ---- | --- |
=========================================================================
-------------------------------------------------------------------------
|     | [Start] | Daemon |     | hpe-relay |     |     |     |     |     |     |
| --- | ------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
|     | DHCP      | Relay  | : 1                 |               |           |           |           |             |                  |     |
| --- | --------- | ------ | ------------------- | ------------- | --------- | --------- | --------- | ----------- | ---------------- | --- |
|     | DHCP      | Relay  | hop-count-increment |               |           |           | : 1       |             |                  |     |
|     | DHCP      | Relay  | Option82            |               | : 1       |           |           |             |                  |     |
|     | DHCP      | Relay  | Option82            |               | validate  | :         | 0         |             |                  |     |
|     | DHCP      | Relay  | Option82            |               | policy    | : keep    |           |             |                  |     |
|     | DHCP      | Relay  | Option82            |               | remote-id | :         | mac       |             |                  |     |
|     | DHCP      | Relay  | Option82            |               | Source    | Intf      | : Disable |             |                  |     |
|     | DHCP      | Smart  | Relay               | :             | Enable    |           |           |             |                  |     |
|     | System    | Mac    | [f4:03:43:80:27:00] |               |           |           |           |             |                  |     |
|     | VRF       | :BLUE, | Source              | Ip:200.0.0.10 |           |           |           |             |                  |     |
|     | vsx:      | Not    | Present             |               |           |           |           |             |                  |     |
|     | Interface |        | vlan2:              | 1             |           |           |           |             |                  |     |
|     | Client    |        | Packet              | Statistics:   |           |           |           |             |                  |     |
|     | Valid     |        |                     | Dropped       |           | O82_Valid |           | O82_Dropped | vsx_drops        |     |
|     | -----     |        |                     | -------       |           | --------- |           | ----------- | ---------        |     |
|     | 0         |        |                     | 0             |           | 0         |           | 0           | 0                |     |
|     | Server    |        | Packet              | Statistics:   |           |           |           |             |                  |     |
|     | Valid     |        |                     | Dropped       |           | O82_Valid |           | O82_Dropped | Invalid_IP_Drops | To_ |
Dsnoop
----- ------- --------- ----------- ---------------- --------
DHCP|80

-
| 0                |                 | 0           |         | 0         |      | 0           |        | 0                |     | 0   |
| ---------------- | --------------- | ----------- | ------- | --------- | ---- | ----------- | ------ | ---------------- | --- | --- |
| client request   |                 | dropped     | packets |           | with | extn option | 82 =   | 0                |     |     |
| client request   |                 | valid       | packets | with      | extn | option      | 82 = 0 |                  |     |     |
| server request   |                 | dropped     | packets |           | with | extn option | 82 =   | 0                |     |     |
| server request   |                 | valid       | packets | with      | extn | option      | 82 = 0 |                  |     |     |
| Port 67          | - 200.0.0.100,2 |             |         |           |      |             |        |                  |     |     |
| source vrf-BLUE. |                 |             |         |           |      |             |        |                  |     |     |
| Interface        | vlan3:          | 1           |         |           |      |             |        |                  |     |     |
| Client           | Packet          | Statistics: |         |           |      |             |        |                  |     |     |
| Valid            |                 | Dropped     |         | O82_Valid |      | O82_Dropped |        | vsx_drops        |     |     |
| -----            |                 | -------     |         | --------- |      | ----------- |        | ---------        |     |     |
| 0                |                 | 0           |         | 0         |      | 0           |        | 0                |     |     |
| Server           | Packet          | Statistics: |         |           |      |             |        |                  |     |     |
| Valid            |                 | Dropped     |         | O82_Valid |      | O82_Dropped |        | Invalid_IP_Drops |     | To_ |
Dsnoop
----- ------- --------- ----------- ---------------- --------
-
| 0                |                 | 0           |         | 0    |      | 0           |        | 0   |     | 0   |
| ---------------- | --------------- | ----------- | ------- | ---- | ---- | ----------- | ------ | --- | --- | --- |
| client request   |                 | dropped     | packets |      | with | extn option | 82 =   | 0   |     |     |
| client request   |                 | valid       | packets | with | extn | option      | 82 = 0 |     |     |     |
| server request   |                 | dropped     | packets |      | with | extn option | 82 =   | 0   |     |     |
| server request   |                 | valid       | packets | with | extn | option      | 82 = 0 |     |     |     |
| Port 67          | - 200.0.0.100,2 |             |         |      |      |             |        |     |     |     |
| source vrf-BLUE. |                 |             |         |      |      |             |        |     |     |     |
| DHCP Smart       | Relay           | Client      | Cache:  |      |      |             |        |     |     |     |
| Total Number     |                 | of entries: |         | 2    |      |             |        |     |     |     |
--------------------------------------------------------------------------
| Client-MAC |     |     | PortIndex |     | Timestamp | RetryCount |     | DiscCount | GWIP |     |
| ---------- | --- | --- | --------- | --- | --------- | ---------- | --- | --------- | ---- | --- |
--------------------------------------------------------------------------
| 00:50:56:bd:6a:7a |     |     | 20  |     | 1636105218 | 1   |     | 4   | 30.0.0.1 |     |
| ----------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | -------- | --- |
| 00:50:56:bd:71:17 |     |     | 20  |     | 1636105214 | 1   |     | 4   | 30.0.0.1 |     |
-------------------------------------------------------------------------
| [End] Daemon |     | hpe-relay |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
=========================================================================
| [End] Feature |     | dhcp-relay |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
=========================================================================
| Diagnostic-dump |             | captured |         | for feature |              | dhcp-relay |     |     |     |     |
| --------------- | ----------- | -------- | ------- | ----------- | ------------ | ---------- | --- | --- | --- | --- |
| Command         | History     |          |         |             |              |            |     |     |     |     |
| Release         |             |          |         |             | Modification |            |     |     |     |     |
| 10.07orearlier  |             |          |         |             | --           |            |     |     |     |     |
| Command         | Information |          |         |             |              |            |     |     |     |     |
| Platforms       | Command     |          | context |             | Authority    |            |     |     |     |     |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     |     |     | rightsforthiscommand. |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 81

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
8360
9300
10000
ip bootp-gateway
| ip bootp-gateway    | <IPV4-ADDR> |             |     |     |
| ------------------- | ----------- | ----------- | --- | --- |
| no ip bootp-gateway |             | <IPV4-ADDR> |     |     |
Description
ConfiguresagatewayaddressfortheDHCPrelayagenttouseforDHCPrequests.BydefaultDHCP
relayagentpicksthelowest-numberedIPaddressontheinterface.
Thenoformofthiscommandremovesthegatewayaddress.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiestheIPaddressofthegatewayinIPv4format(x.x.x.x),
wherexisaisadecimalnumberfrom0to255.
Examples
SettingtheIPaddressofthegatewayforinterface1/1/1to10.10.10.10:
| switch(config)#     |         | interface        | 1/1/1 |              |
| ------------------- | ------- | ---------------- | ----- | ------------ |
| switch(config-if)#  |         | ip bootp-gateway |       | 10.10.10.10  |
| Command History     |         |                  |       |              |
| Release             |         |                  |       | Modification |
| 10.07orearlier      |         |                  |       | --           |
| Command Information |         |                  |       |              |
| Platforms           | Command | context          |       | Authority    |
config-if
| 8320 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | --- | -------------------------------------------------- |
| 8325 |     |     |     | rightsforthiscommand.                              |
8360
9300
10000
ip helper-address
| ip helper-address    |     | <IPV4-ADDR> | [vrf | <VRF-NAME>] |
| -------------------- | --- | ----------- | ---- | ----------- |
| no ip helper-address |     | <IPV4-ADDR> | [vrf | <VRF-NAME>] |
Description
DefinestheaddressofaremoteDHCPserverorDHCPrelayagent.Uptoeightaddressescanbe
defined.TheDHCPagentforwardsDHCPclientrequeststoalldefinedservers.
DHCP|82

ThiscommandrequiresthatyoudefineasourceIPaddressforDHCPrelaywiththecommand ip
source-interface.TheconfiguredsourceIPontheVRFisusedtoforwardDHCPpacketstotheserver.
AhelperaddresscannotbedefinedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
helper-address <IPV4-ADDR> SpecifiesthehelperIPaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
| vrf <VRF-NAME> |     |     |     | SpecifiesthenameofaVRF.Default:default. |     |     |
| -------------- | --- | --- | --- | --------------------------------------- | --- | --- |
Examples
DefiningtheIPhelperaddress10.10.10.209oninterface1/1/1:
| switch(config)#    |     | interface         | 1/1/1 |     |              |     |
| ------------------ | --- | ----------------- | ----- | --- | ------------ | --- |
| switch(config-if)# |     | ip helper-address |       |     | 10.10.10.209 |     |
RemovingtheIPhelperaddress10.10.10.209oninterface1/1/1:
| switch(config-if)# |     | no ip | helper-address |     | 10.10.10.209 |     |
| ------------------ | --- | ----- | -------------- | --- | ------------ | --- |
DefiningtheIPhelperaddress10.10.10.209oninterface1/1/2onVRFmyvrf:
| switch(config)#    |     | interface         | 1/1/2 |     |              |           |
| ------------------ | --- | ----------------- | ----- | --- | ------------ | --------- |
| switch(config-if)# |     | ip helper-address |       |     | 10.10.10.209 | vrf myvrf |
RemovingtheIPhelperaddress10.10.10.209oninterface1/1/2onVRFmyvrf:
| switch(config-if)#  |         | no ip   | helper-address |              | 10.10.10.209 | vrf myvrf |
| ------------------- | ------- | ------- | -------------- | ------------ | ------------ | --------- |
| Command History     |         |         |                |              |              |           |
| Release             |         |         |                | Modification |              |           |
| 10.07orearlier      |         |         |                | --           |              |           |
| Command Information |         |         |                |              |              |           |
| Platforms           | Command | context |                | Authority    |              |           |
8320 config-if Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --- | --------------------- | --- | --- |
8360
9300
10000
show dhcp-relay
| show dhcp-relay | [vsx-peer] |     |     |     |     |     |
| --------------- | ---------- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 83

Description
ShowsDHCPrelayconfigurationsettings.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingDHCPrelaysettings:
| switch#          | show dhcp-relay  |           |            |     |
| ---------------- | ---------------- | --------- | ---------- | --- |
| DHCP Relay       | Agent            |           | : enabled  |     |
| DHCP Smart       | Relay            |           | : enabled  |     |
| DHCP Request     | Hop Count        | Increment | : enabled  |     |
| L2VPN Clients    |                  |           | : disabled |     |
| Option           | 82               |           | : disabled |     |
| Source-Interface |                  |           | : disabled |     |
| Response         | Validation       |           | : disabled |     |
| Option           | 82 Handle Policy |           | : replace  |     |
| Remote           | ID               |           | : mac      |     |
| DHCP Relay       | Statistics:      |           |            |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         | 10     |                | 60  | 10  |
| ---------- | ------ | -------------- | --- | --- |
| DHCP Relay | Option | 82 Statistics: |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50             | 8           |         | 50                                                   | 8   |
| -------------- | ----------- | ------- | ---------------------------------------------------- | --- |
| Command        | History     |         |                                                      |     |
| Release        |             |         | Modification                                         |     |
| 10.07orearlier |             |         | --                                                   |     |
| Command        | Information |         |                                                      |     |
| Platforms      | Command     | context | Authority                                            |     |
| 8320           |             |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Manager(#)
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     | commandfromtheoperatorcontext(>)only.                 |     |
9300
10000
| show dhcp-relay | bootp-gateway |     |     |     |
| --------------- | ------------- | --- | --- | --- |
show dhcp-relay bootp-gateway [interface <INTERFACE-NAME>] [vsx-peer]
DHCP|84

Description
Showsthebootpgatewaydefinedforallinterfacesoraspecificinterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-NAME>
Specifiesaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingthedesignatedbootpgatewayforallinterfaces:
| switch# show         | dhcp-relay | bootp-gateway   |              |     |
| -------------------- | ---------- | --------------- | ------------ | --- |
| BOOTP Gateway        | Entries    |                 |              |     |
| Interface            |            | Source          | IP           |     |
| -------------------- |            | --------------- |              |     |
| 1/1/1                |            | 1.1.1.1         |              |     |
| 1/1/2                |            | 1.1.1.2         |              |     |
| Command History      |            |                 |              |     |
| Release              |            |                 | Modification |     |
| 10.07orearlier       |            |                 | --           |     |
| Command Information  |            |                 |              |     |
| Platforms            | Command    | context         | Authority    |     |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     | commandfromtheoperatorcontext(>)only.                 |     |
9300
10000
show ip helper-address
| show ip helper-address |     | [interface | <INTERFACE-ID>] | [vsx-peer] |
| ---------------------- | --- | ---------- | --------------- | ---------- |
Description
ShowstheIPhelperaddressesdefinedforallinterfacesoraspecificinterface.
| Parameter                |     |     | Description |     |
| ------------------------ | --- | --- | ----------- | --- |
| interface <INTERFACE-ID> |     |     |             |     |
Specifiesaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 85

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheIPhelperaddressesforallinterfaces:
| switch#           | show ip helper-address |                   |     |     |
| ----------------- | ---------------------- | ----------------- | --- | --- |
| IP Helper         | Addresses              |                   |     |     |
| Interface:        | 1/1/1                  |                   |     |     |
| IP                | Helper Address         | VRF               |     |     |
| ----------------- |                        | ----------------- |     |     |
| 192.168.20.1      |                        | default           |     |     |
| 192.168.10.1      |                        | default           |     |     |
| Interface:        | 1/1/2                  |                   |     |     |
| IP                | Helper Address         | VRF               |     |     |
| ----------------- |                        | ----------------- |     |     |
| 192.168.30.1      |                        | RED               |     |     |
ShowingtheIPhelperaddressesforinterface1/1/1:
switch#
|                   | show ip helper-address |                   | interface    | 1/1/1 |
| ----------------- | ---------------------- | ----------------- | ------------ | ----- |
| IP Helper         | Addresses              |                   |              |       |
| Interface:        | 1/1/1                  |                   |              |       |
| IP                | Helper Address         | VRF               |              |       |
| ----------------- |                        | ----------------- |              |       |
| 192.168.20.1      |                        | default           |              |       |
| 192.168.10.1      |                        | default           |              |       |
| Command           | History                |                   |              |       |
| Release           |                        |                   | Modification |       |
| 10.07orearlier    |                        |                   | --           |       |
| Command           | Information            |                   |              |       |
| Platforms         | Command                | context           | Authority    |       |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     | commandfromtheoperatorcontext(>)only.                 |     |
9300
10000
| DHCPv6      | relay agent |             |     |     |
| ----------- | ----------- | ----------- | --- | --- |
| Configuring | the DHCPv6  | relay agent |     |     |
DHCP|86

Prerequisites
n Anenabledlayer3interface.
Procedure
1. EnabletheDHCPv6agentwiththecommanddhcpv6-relay.
2. ConfigureoneormoreIPhelperaddresseswiththecommandipv6 helper-address.This
determineswheretheDHCPv6agentforwardDHCPrequests.
3. IfyouwanttoenableDHCPoption79supporttoforwardclientlink-layeraddresses,usethe
| commanddhcpv6-relay |     |     | option 79. |     |
| ------------------- | --- | --- | ---------- | --- |
4. ReviewDHCPv6relayagentconfigurationsettingswiththecommandsshow dhcpv6-relayand
| show ipv6 | helper-address. |     |     |     |
| --------- | --------------- | --- | --- | --- |
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablestheDHCPv6relayagent.
n Enablesinterface1/1/2andassignsanIPv6addresstoit.(Bydefault,allinterfacesarelayer3and
disabled.)
n DefinesanIPhelperaddressofFF01::1:1000oninterface1/1/2.
n EnablesDHCPoption79.
| switch(config)#    |     | dhcpv6-relay |       |     |
| ------------------ | --- | ------------ | ----- | --- |
| switch(config)#    |     | interface    | 1/1/2 |     |
| switch(config-if)# |     | no shutdown  |       |     |
switch(config-if)#
|                    |          | ipv6              | address 2001:0db8:85a3::8a2e:0370:7334/24 |              |
| ------------------ | -------- | ----------------- | ----------------------------------------- | ------------ |
| switch(config-if)# |          | ip helper-address |                                           | FF01::1:1000 |
| switch(config-if)# |          | exit              |                                           |              |
| switch(config)#    |          | dhcpv6-relay      | option                                    | 79           |
| DHCPv6 relay       | scenario | 1                 |                                           |              |
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 87

Procedure
1. EnableDHCPrelay.
| switch# | config |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- |
switch(config)#
dhcpv6-relay
2. DefineanIPv6helperaddressoninterfaces1/1/1and1/1/2.
| switch(config)#    |     | interface | 1/1/1               |         |     |
| ------------------ | --- | --------- | ------------------- | ------- | --- |
| switch(config-if)# |     | ipv6      | address 2002::22/64 |         |     |
| switch(config-if)# |     | ipv6      | helper-address      | 2001::1 |     |
switch(config-if)#
|                    |     | interface | 1/1/2               |         |     |
| ------------------ | --- | --------- | ------------------- | ------- | --- |
| switch(config-if)# |     | ipv6      | address 2002::21/64 |         |     |
| switch(config-if)# |     | ipv6      | helper-address      | 2001::1 |     |
| switch(config-if)# |     | quit      |                     |         |     |
3. VerifyDHCPrelayconfiguration.
switch#
show dhcpv6-relay
| DHCPv6                                         | Relay Agent | :              | enabled  |     |             |
| ---------------------------------------------- | ----------- | -------------- | -------- | --- | ----------- |
| Option                                         | 79          | :              | disabled |     |             |
| switch#                                        | show ipv6   | helper-address |          |     |             |
| Interface:                                     | 1/1/1       |                |          |     |             |
| IPv6 Helper                                    | Address     |                |          |     | Egress Port |
| ---------------------------------------------- |             |                |          |     | ----------- |
| 2001::1                                        |             |                |          |     | 1/1/3       |
| Interface:                                     | 1/1/2       |                |          |     |             |
| IPv6 Helper                                    | Address     |                |          |     | Egress Port |
| --------------------------------------------   |             |                |          |     | ----------- |
| 2001::1                                        |             |                |          |     | 1/1/3       |
| DHCPv6 relay                                   | scenario    | 2              |          |     |             |
Inthisscenario,thetwohostcomputerscommunicatewithtwodifferentDHCPservers.Eachserveris
reachedonadifferentVRF.Thephysicaltopologyofthenetworklookslikethis:
DHCP|88

Procedure
1. CreatethetwoVRFs.
switch# config
| switch(config)# | vrf vrf 1 |     |     |
| --------------- | --------- | --- | --- |
| switch(config)# | vrf vrf 2 |     |     |
2. Configureinterface1/1/1.SetitsIPaddress,associateitwithVRF1,anddefinethehelperIP
addresstoreachDHCPserver1.
| switch(configif)# | interface           | 1/1/1      |                 |
| ----------------- | ------------------- | ---------- | --------------- |
| switch(configif)# | vrf attach          | vrf1       |                 |
| switch(configif)# | ipv6 address        | 20.0.0.1/8 |                 |
| switch(configif)# | ipv6 helper-address |            | unicast 1040::2 |
3. Configureinterface1/1/2.SetitsIPaddressandassociateitwithVRF1.
switch(configif)#
|                   | interface    | 1/1/2       |     |
| ----------------- | ------------ | ----------- | --- |
| switch(configif)# | vrf attach   | vrf1        |     |
| switch(configif)# | ipv6 address | 1040::1/120 |     |
4. Configureinterface1/1/3.SetitsIPaddressandassociateitwithVRF1.
| switch(configif)# | interface    | 1/1/3       |     |
| ----------------- | ------------ | ----------- | --- |
| switch(configif)# | vrf attach   | vrf2        |     |
| switch(configif)# | ipv6 address | 3030::1/120 |     |
5. Configureinterface1/1/4.SetitsIPaddress,associateitwithVRF2,anddefinethehelperIP
addresstoreachDHCPserver2.
| switch(configif)#          | interface           | 1/1/4       |                 |
| -------------------------- | ------------------- | ----------- | --------------- |
| switch(configif)#          | vrf attach          | vrf2        |                 |
| switch(configif)#          | ipv6 address        | 4040::1/120 |                 |
| switch(configif)#          | ipv6 helper-address |             | unicast 3030::2 |
| DHCP relay (IPv6) commands |                     |             |                 |
dhcpv6-relay
dhcpv6-relay
no dhcpv6-relay
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 89

Description
EnablesDHCPv6relaysupport.DHCPv6relayisdisabledbydefault.
DHCPrelayisnotsupportedonthemanagementinterface
ThenoformofthiscommanddisablesDHCPrelaysupport.
Examples
EnablesDHCPv6relaysupport.
| switch(config)# | dhcpv6-relay |     |     |
| --------------- | ------------ | --- | --- |
RemovesDHCPv6relaysupport.
| switch(config)#     | no      | dhcpv6-relay |              |
| ------------------- | ------- | ------------ | ------------ |
| Command History     |         |              |              |
| Release             |         |              | Modification |
| 10.07orearlier      |         |              | --           |
| Command Information |         |              |              |
| Platforms           | Command | context      | Authority    |
config
| 8320 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 8325 |     |     | rightsforthiscommand.                              |
8360
9300
10000
| dhcpv6-relay    | option 79 |     |     |
| --------------- | --------- | --- | --- |
| dhcpv6-relay    | option 79 |     |     |
| no dhcpv6-relay | option    | 79  |     |
Description
EnablessupportforDHCPrelayoption79.Whenenabled,theDHCPv6relayagentforwardsthelink-
layeraddressoftheclient.Thisoptionisdisabledbydefault.
ThenoformofthiscommanddisablessupportforDHCPrelayoption79.
Examples
EnablesDHCPoption79support.
| switch(config)# | dhcpv6-relay |     | option 79 |
| --------------- | ------------ | --- | --------- |
DisablesDHCPoption79support.
| switch(config)# | no  | dhcpv6-relay | option 79 |
| --------------- | --- | ------------ | --------- |
DHCP|90

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
9300
10000
ipv6 helper-address
| ipv6 helper-address    | unicast | <UNICAST-IPV6-ADDR>         |     |
| ---------------------- | ------- | --------------------------- | --- |
| no ipv6 helper-address |         | unicast <UNICAST-IPV6-ADDR> |     |
ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>
no ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>
Description
DefinestheaddressofaremoteDHCPv6serverorDHCPv6relayagent.Uptoeightaddressescanbe
defined.TheDHCPv6agentforwardsDHCPv6clientrequeststoalldefinedservers.
NotsupportedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<UNICAST-IPV6-ADDR> SpecifiestheunicasthelperIPaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
<MULTICAST-IPV6-ADDR> SpecifiesthemulticasthelperIPaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
all-dhcp-servers SpecifiesalltheDHCPserverIPv6addressesfortheinterface.
egress <PORT-NUM> SpecifiestheportnumberonwhichDHCPv6servicerequestsare
relayedtoamulticastdestination.Theegressportmustbe
differentthantheoneonwhichthemulticasthelperaddressis
configured.Format:member/slot/port.
vrf <VRF-NAME> SpecifiesthenameoftheVRFfromwhichthespecifiedprotocol
setsitssourceIPaddress.
Examples
DefiningamulticastIPv6helperaddressof2001:DB8::1onport1/1/2:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 91

switch(config-if)# ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress 1/1/2
RemovingtheIPhelperaddressof2001:DB8::1onport1/1/2:
switch(config-if)# no ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress
1/1/2
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
9300
10000
show dhcpv6-relay
| show dhcpv6-relay | [vsx-peer] |     |     |
| ----------------- | ---------- | --- | --- |
Description
ShowsDHCPrelayconfigurationsettings.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# show        | dhcpv6-relay |            |              |
| ------------------- | ------------ | ---------- | ------------ |
| DHCPv6              | Relay Agent  | : enabled  |              |
| Option              | 79           | : disabled |              |
| Command History     |              |            |              |
| Release             |              |            | Modification |
| 10.07orearlier      |              |            | --           |
| Command Information |              |            |              |
DHCP|92

| Platforms |     | Command | context | Authority |     |     |
| --------- | --- | ------- | ------- | --------- | --- | --- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
| 8360 |     |     |     | commandfromtheoperatorcontext(>)only.                 |     |     |
9300
10000
| show ipv6 | helper-address |     |            |                 |     |            |
| --------- | -------------- | --- | ---------- | --------------- | --- | ---------- |
| show ipv6 | helper-address |     | [interface | <INTERFACE-ID>] |     | [vsx-peer] |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
| Parameter |                |     |     | Description |     |     |
| --------- | -------------- | --- | --- | ----------- | --- | --- |
| interface | <INTERFACE-ID> |     |     |             |     |     |
Specifiesaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#                                        | show    | ipv6    | helper-address |           |       |             |
| ---------------------------------------------- | ------- | ------- | -------------- | --------- | ----- | ----------- |
| Interface:                                     |         | 1/1/1   |                |           |       |             |
| IPv6                                           | Helper  | Address |                |           |       | Egress Port |
| ---------------------------------------------- |         |         |                |           |       | ----------- |
| 2001:db8:0:1::                                 |         |         |                |           |       | -           |
| FF01::1:1000                                   |         |         |                |           |       | 1/1/2       |
| Interface:                                     |         | 1/1/2   |                |           |       |             |
| IPv6                                           | Helper  | Address |                |           |       | Egress Port |
| --------------------------------------------   |         |         |                |           |       | ----------- |
| 2001:db8:0:1::                                 |         |         |                |           |       | -           |
| switch#                                        | show    | ipv6    | helper-address | interface | 1/1/1 |             |
| Interface:                                     |         | 1/1/1   |                |           |       |             |
| IPv6                                           | Helper  | Address |                |           |       | Egress Port |
| ---------------------------------------------- |         |         |                |           |       | ----------- |
| 2001:db8:0:1::                                 |         |         |                |           |       | -           |
| FF01::1:1000                                   |         |         |                |           |       | 1/1/2       |
| switch#                                        | show    | ipv6    | helper-address | interface | 1/1/1 |             |
| Interface:                                     |         | 1/1/1   |                |           |       |             |
| IPv6                                           | Helper  | Address |                |           |       | Egress Port |
| ---------------------------------------------- |         |         |                |           |       | ----------- |
| 2001:db8:0:1::                                 |         |         |                |           |       | -           |
| FF01::1:1000                                   |         |         |                |           |       | 1/1/2       |
| Command                                        | History |         |                |           |       |             |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 93

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
| 8360 |     |     | commandfromtheoperatorcontext(>)only.                 |
9300
10000
| DHCP server |     |     |     |
| ----------- | --- | --- | --- |
Overview
Thedynamichostconfigurationprotocol(DHCP)enablesaservertoautomatetheassignmentofIP
addresses,andothernetworkingsettings,tohostcomputers.TheDHCPserverontheswitchprovides
bothIPv4andIPv6supportandisindependentlyconfigurableoneachVRF.
Key features
n Supportsmultipleaddresspoolsandstaticaddressbindings.
n SupportsDHCPoptions,enablingtheservertoprovideadditionalinformationaboutthenetwork
whenDHCPclientsrequestanaddress.
n SupportsBOOTPtodistributebootimagefilesusinganexternalTFTPserver.
n VRFaware,meaningthatDHCPclientrequestsreceivedonaninterfaceareprocessedbytheDHCP
serverinstanceconfiguredforaVRF.DHCPserverresponsesareforwardedtoclientsontheVRF.
n Supportsexternalstorageofleaseinformationonaremotehost.ThisenablestheDHCPserverto
restoreleaseinformationafterarebootorafailure.Leaseinformationisstoredinaflatfileonthe
configuredexternaldevice.Itisimportantthattheexternaldeviceprovidepersistentexternal
storagetoallowrestorationofleaseinformation.Ifexternalstorageisnotconfigured,thenaftera
failureorreboot,allexistingleaseinformationislost.
n SupportsVSX.InaVSXsetup,oneswitchactsasprimaryandtheotherswitchactsassecondary.The
DHCPserverisactiveonlyontheprimaryswitch.Afterafailover,theDHCPserverisenabledbased
onthestateandroleoftheswitch.ThestateoftheDHCPserverindicatestheoperationalstateof
theserver.VSXsynchronizationsupportsDHCPv4andDHCPv6server,includingexternalstorage
configurations.FormoreinformationonVSXsupport,seetheVirtualSwitchingExtension(VSX)Guide.
| DHCP relay | interoperation |     |     |
| ---------- | -------------- | --- | --- |
BothDHCPrelayandDHCPservercanbeconfiguredonthesameVRF.
| DHCP snooping | interoperation |     |     |
| ------------- | -------------- | --- | --- |
DHCPsnoopingmaynotbeconfiguredwithDHCPserver.
| Configuring | a DHCPv4 | server | on a VRF |
| ----------- | -------- | ------ | -------- |
DHCP|94

Prerequisites

n An enabled layer 3 interface.

n A VRF.

n An external TFTP server to host BOOTP image files (optional).

n An external storage device installed and configured (optional).

Procedure

1. Assign the DHCPv4 server to a VRF with the command dhcp-server vrf. This switches to the

DHCPv4 server configuration context.

2.

If you want the DHCPv4 server to be the sole authority for IP addresses on the VRF, enable
authoritative mode with the command authoritative.

3. Define an address pool for the VRF with the command pool. This switches to the DHCPv4 server

pool context. Customize pool settings as follows:
a. Define the range of addresses in the pool with the command range.
b. Set the lease time for addresses in the pool with the command lease.
c. Set the domain name for the pool with the command domain-name.
d. Define up to four default routers with the command default-router.
e. Define up to four DNS servers with the command dns-server.
f. Create static bindings for specific addresses in the pool with the command static-bind.
g. Configure custom DHCPv4 options for the pool with the command option.
h. Configure NetBIOS support with the commands netbios-name-server and netbios-node-

type.

i. Configure BOOTP options with the command bootp.
j. Exit the DHCPv4 server pool context with the command exit.

4. Enable the DHCP server on the VRF with the command enable.

5. Configure support for persistent external storage of DHCP settings with the command dhcp-

server external-storage.

6. View DHCPv4 server configuration settings with the command show dhcp-server all-vrfs.

Example

This example creates the following configuration:

n Configures the DHCPv4 server on VRF primary-vrf.

n Enables authoritative mode.

n Defines the pool primary-pool with the following settings:

o Address range: 10.0.0.1 to 10.0.0.100.

o Lease time: 12 hours.

o Domain name: example.org.in.

o Default routers: 10.30.30.1 and 10.30.30.2.

o DNS servers: 125.0.0.1 and 125.0.0.2.

o Static binding of 10.0.0.11 for MAC address 24:be:05:24:75:73.

o DHCP custom option 3 with IP address 10.30.30.3.

n Enables the DHCPv4 server.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

95

| switch(config)# | dhcp-server | vrf primary |     |
| --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
pool primary-pool
| switch(config-dhcp-server-pool)# |     | range       | 10.0.0.1 10.0.0.100 |
| -------------------------------- | --- | ----------- | ------------------- |
| switch(config-dhcp-server-pool)# |     | lease       | 12:00:00            |
| switch(config-dhcp-server-pool)# |     | domain-name | example.org.in      |
switch(config-dhcp-server-pool)# default-router ip 10.30.30.1 10.30.30.2
switch(config-dhcp-server-pool)# dns-server 125.0.0.1 125.0.0.2
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.11 mac 24:be:05:24:75:73
| switch(config-dhcp-server-pool)# |            | option    | 3 ip 10.30.30.3 |
| -------------------------------- | ---------- | --------- | --------------- |
| switch(config-dhcp-server-pool)# |            | exit      |                 |
| switch(config-dhcp-server)#      |            | enable    |                 |
| Configuring                      | the DHCPv6 | server on | a VRF           |
Prerequisites
n Anenabledlayer3interface.
n AVRF.
n Anexternalstoragedeviceinstalledandconfigured(optional).
Procedure
1. AssigntheDHCPv6servertoaVRFwiththecommanddhcpv6-server vrf.Thisswitchestothe
DHCPv6serverconfigurationcontext.
2. IfyouwanttheDHCPservertobethesoleauthorityforIPaddressesontheVRF,enable
authoritativemodewiththecommandauthoritative.
3. DefineanaddresspoolfortheVRFwiththecommandpool.ThisswitchestotheDHCPv6server
poolcontext.Customizepoolsettingsasfollows:
| a. Definetherangeofaddressesinthepoolwiththecommandrange. |     |     |     |
| --------------------------------------------------------- | --- | --- | --- |
b. SettheDHCPleasetimeforaddressesinthepoolwiththecommandlease.
| c. DefineuptofourDNSserverswiththecommanddns-server. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- |
d. Createstaticbindingsforspecificaddressesinthepoolwiththecommandstatic-bind.
| e. ConfigurecustomDHCPoptionsforthepoolwiththecommandoption. |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- |
| f. ExittheDHCPserverpoolcontextwiththecommandexit.           |     |     |     |
4. EnabletheDHCPv6serverontheVRFwiththecommandenable.
5. ConfiguresupportforpersistentexternalstorageofDHCPsettingswiththecommanddhcv6p-
| server | external-storage. |     |     |
| ------ | ----------------- | --- | --- |
6. ViewDHCPv6serverconfigurationsettingswiththecommandshow all-vrfs.
dhcpv6-server
Example
Thisexamplecreatesthefollowingconfiguration:
n ConfiguresaDHCPv6serveronVRFprimary-vrf.
n Enablesauthoritativemode.
n Definesthepoolprimary-poolwiththefollowingsettings:
o Addressrange:2001::1to2001::100.
o Leasetime:12hours.
o DNSservers:2101::14and2101::14.
DHCP|96

o Staticbindingof2001::101forclientID1:0:a0:24:ab:fb:9c.
o DHCPcustomoption:22withIPaddress2101::15.
n EnablestheDHCPv6server.
| switch(config)#               | dhcpv6-server | vrf primary       |     |
| ----------------------------- | ------------- | ----------------- | --- |
| switch(config-dhcpv6-server)# |               | pool primary-pool |     |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::100 prefix-len 64
| switch(config-dhcpv6-server-pool)# |     | lease 12:00:00 |     |
| ---------------------------------- | --- | -------------- | --- |
switch(config-dhcpv6-server-pool)# dns-server 2101::13 2101::14
switch(config-dhcpv6-server-pool)# static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c
| switch(config-dhcpv6-server-pool)# |               | option | 22 ipv6 2101::15 |
| ---------------------------------- | ------------- | ------ | ---------------- |
| switch(config-dhcpv6-server-pool)# |               | exit   |                  |
| switch(config-dhcpv6-server)#      |               | enable |                  |
| DHCP server                        | IPv4 commands |        |                  |
authoritative
authoritative
no authoritative
Description
ConfigurestheDHCPv4serverasauthoritativeonthecurrentVRF.Thismeansthattheserveristhesole
authorityforthenetworkontheVRF.Therefore,ifaclientrequestsanIPaddressleaseforwhichthe
serverhasnorecord,theserverrespondswithDHCPNAK,indicatingthattheclientmustnolongeruse
thatIPaddress.Iftheserverisnotauthoritative,thenitwillignoreDHCPv4requestsreceivedfor
unknownleasesfromunknownhosts.
ThenoformofthiscommanddisablesauthoritativemodeonthecurrentVRF.
Example
ConfiguresDHCPv4serverauthoritativemodeonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary   |     |
| --------------------------- | ----------- | ------------- | --- |
| switch(config-dhcp-server)# |             | authoritative |     |
RemovestheDHCPv4serverauthoritativemodeonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary      |     |
| --------------------------- | ----------- | ---------------- | --- |
| switch(config-dhcp-server)# |             | no authoritative |     |
Command History
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
Command Information
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 97

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8320 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
9300
10000
bootp
bootp <REMOTE-URL>
no bootp <REMOTE-URL>
Description
SetstheBOOTPoptionsthatarereturnedbytheDHCPv4serverforthecurrentpool.BOOTPprovidesa
waytodistributeanIPaddressandbootimagefiletoclientstations.TheDHCPv4serverreturnstheIP
addressandthelocationofthebootimagefile,whichmustbestoredonanexternalTFTPserver.
ThenoformofthiscommanddisablessupportforBOOTP.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<REMOTE-URL> SpecifiesthenameandlocationofaBOOTPfileonaTFTPserver
intheformat:
tftp://{<IP> | <HOST>}/<FILE>
n <IP>:SpecifiestheIPaddressoftheTFTPserverhostingthe
fileinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255.Youcanremoveleadingzeros.Forexample,the
address192.169.005.100becomes192.168.5.100.
<HOST>:Specifiesthefully-qualifieddomainnameoftheTFTP
n
serverhostingthefile.Range:1to64printableASCII
characters.
n <FILE>:SpecifiesthenameoftheBOOTPfile.Range:1to64
printableASCIIcharacters.
Example
DefinesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf  | primary      |
| --------------------------- | ----------- | ---- | ------------ |
| switch(config-dhcp-server)# |             | pool | primary-pool |
switch(config-dhcp-server-pool)# bootp tftp://10.0.0.1/mybootfile
DeletesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf  | primary      |
| --------------------------- | ----------- | ---- | ------------ |
| switch(config-dhcp-server)# |             | pool | primary-pool |
switch(config-dhcp-server-pool)# no bootp tftp://10.0.0.1/mybootfile
| Command History |     |     |     |
| --------------- | --- | --- | --- |
DHCP|98

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
8360
9300
10000
| clear dhcp-server | leases |     |     |     |
| ----------------- | ------ | --- | --- | --- |
clear dhcp-server leases [all-vrfs | <IPV4-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv4serverleaseinformation.TheDHCPv4servermustbedisabledbeforeclearinglease
information.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
all-vrfs
ClearsleasesforallVRFs.
<IPV4-ADDR> vrf <VRF-NAME> ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| vrf <VRF-NAME> |     |     |     | ClearsleasesforaspecificVRF. |
| -------------- | --- | --- | --- | ---------------------------- |
Examples
ClearingallDHCPv4serverleases.
| switch(config)#             | dhcp-server |     | vrf primary |     |
| --------------------------- | ----------- | --- | ----------- | --- |
| switch(config-dhcp-server)# |             |     | disable     |     |
| switch(config-dhcp-server)# |             |     | exit        |     |
| switch(config)#             | exit        |     |             |     |
| switch# clear               | dhcp-server |     | leases      |     |
ClearingallDHCPv4serverleasesforVRFprimary-vrf.
| switch(config)#             | dhcp-server |     | vrf primary |             |
| --------------------------- | ----------- | --- | ----------- | ----------- |
| switch(config-dhcp-server)# |             |     | disable     |             |
| switch(config-dhcp-server)# |             |     | exit        |             |
| switch(config)#             | exit        |     |             |             |
| switch# clear               | dhcp-server |     | leases vrf  | primary-vrf |
CleartheDHCPv4serverleaseforIPaddress10.10.10.1onVRFprimary-vrf.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 99

| switch(config)# | dhcp-server |     | vrf primary |     |
| --------------- | ----------- | --- | ----------- | --- |
switch(config-dhcp-server)#
disable
| switch(config-dhcp-server)# |             |         | exit              |                 |
| --------------------------- | ----------- | ------- | ----------------- | --------------- |
| switch(config)#             | exit        |         |                   |                 |
| switch# clear               | dhcp-server |         | leases 10.10.10.1 | vrf primary-vrf |
| Command History             |             |         |                   |                 |
| Release                     |             |         | Modification      |                 |
| 10.07orearlier              |             |         | --                |                 |
| Command Information         |             |         |                   |                 |
| Platforms                   | Command     | context | Authority         |                 |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
8325
| 8360 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
9300
10000
default-router
| default-router    | <IPV4-ADDR-LIST> |     |     |     |
| ----------------- | ---------------- | --- | --- | --- |
| no default-router | <IPV4-ADDR-LIST> |     |     |     |
Description
DefinesuptofourdefaultroutersforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddefaultroutersfromthepool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesofthedefaultroutersinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.Youcan
removeleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.Separate
addresseswithaspace.AmaximumoffourIPaddressescanbe
defined.
Example
Definestwodefaultrouters,10.0.0.1and10.0.0.10,fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |
| --------------------------- | ----------- | --- | ----------------- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |
switch(config-dhcp-server-pool)# default-router ip 10.0.0.1 10.0.0.10
Deletesthedefaultrouter10.0.0.1fromtheserverpoolprimary-poolonVRFprimary.
DHCP|100

| switch(config)# | dhcp-server | vrf | primary |     |
| --------------- | ----------- | --- | ------- | --- |
switch(config-dhcp-server)#
|                                  |         | pool    | primary-pool      |             |
| -------------------------------- | ------- | ------- | ----------------- | ----------- |
| switch(config-dhcp-server-pool)# |         |         | no default-router | ip 10.0.0.1 |
| Command History                  |         |         |                   |             |
| Release                          |         |         | Modification      |             |
| 10.07orearlier                   |         |         | --                |             |
| Command Information              |         |         |                   |             |
| Platforms                        | Command | context | Authority         |             |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | ------------------------------ | --- |
8360
9300
10000
| dhcp-server | external-storage |     |     |     |
| ----------- | ---------------- | --- | --- | --- |
dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
Description
ConfigurestheexternalstoragefilelocationforDHCPv4serverleaseinformation.Thisfileprovides
persistentstorage,enablingDHCPv4serversettingstoberestoredwhentheswitchisrestarted.Lease
informationisstoredinaflatfileontheconfiguredexternaldevice.
Ifexternalstorageisnotconfigured,thenafterafailureorreboot,allexistingleaseinformationislost.
Leaseinformationissavedtoexternalstorageeachtimethedelaytimerexpires,whichbydefaultis
every300seconds.
Leaseinformationisnotrestoredwhenissuingthecommanddhcp-server enable.
ThenoformofthiscommandremovesexternalstoragesupportfortheDHCPv4server.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<VOLUME-NAME>
Specifiestheexternalstoragevolumename.Range:1to64
printableASCIIcharacters.
file <LEASE-FILENAME> Specifiestheexternalstoragefilename.Range:1to255printable
ASCIIcharacters.
delay <DELAY> Specifiestheintervalinsecondsbetweenupdatestotheexternal
storagefile.Range:15to86400.Default:300.
Example
StorestheleasefileonexternalstoragevolumeStorage1infileLeaseFileatanintervalof600seconds.
switch(config)# dhcp-server external-storage Storage1 file LeaseFile delay 600
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 101

DisablesstorageoftheleasefileonexternalstoragevolumeStorage1infileLeaseFile.
switch(config)# no dhcp-server external-storage Storage1 file LeaseFile delay 600
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
8360
9300
10000
| dhcp-server    | vrf            |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| dhcp-server    | vrf <VRF-NAME> |     |     |     |
| no dhcp-server | vrf <VRF-NAME> |     |     |     |
Description
ConfigurestheDHCPv4servertosupportaVRFandchangestotheconfig-dhcp-servercontextfor
thatVRF.
ThenoformofthiscommandremovesDHCPv4serversupportonaVRF.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<VRF-NAME>
NameofaVRF.
Example
ConfiguresDHCPv4serversupportonVRFprimary.
| switch(config)# | dhcp-server |     | vrf | primary |
| --------------- | ----------- | --- | --- | ------- |
RemovesDHCPv4serversupportonVRFprimary.
| switch(config)# | no  | dhcp-server |     | vrf primary  |
| --------------- | --- | ----------- | --- | ------------ |
| Command History |     |             |     |              |
| Release         |     |             |     | Modification |
| 10.07orearlier  |     |             |     | --           |
DHCP|102

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
| 8320 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 8325 |     |     | rightsforthiscommand.                              |
8360
9300
10000
disable
disable
Description
DisablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhen
configuredonaVRF.
Example
DisablestheDHCPv4serveronVRFprimary.
| switch(config)#             | dhcp-server | vrf     | primary      |
| --------------------------- | ----------- | ------- | ------------ |
| switch(config-dhcp-server)# |             | disable |              |
| Command History             |             |         |              |
| Release                     |             |         | Modification |
| 10.07orearlier              |             |         | --           |
| Command Information         |             |         |              |
| Platforms                   | Command     | context | Authority    |
config-dhcp-server
| 8320 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 8325 |     |     | rightsforthiscommand.                              |
8360
9300
10000
dns-server
| dns-server <IPV4-ADDR-LIST> |                  |     |     |
| --------------------------- | ---------------- | --- | --- |
| no dns-server               | <IPV4-ADDR-LIST> |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesoftheDNSserversinIPv4format
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 103

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
(x.x.x.x),wherexisadecimalnumberfrom0to255.Separate
addresseswithaspace.
Example
DefinestwoDNSserversfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf  | primary      |     |           |
| -------------------------------- | ----------- | ---- | ------------ | --- | --------- |
| switch(config-dhcp-server)#      |             | pool | primary-pool |     |           |
| switch(config-dhcp-server-pool)# |             |      | dns-server   |     | 10.0.20.1 |
DeletesaDNSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf     | primary      |            |           |
| -------------------------------- | ----------- | ------- | ------------ | ---------- | --------- |
| switch(config-dhcp-server)#      |             | pool    | primary-pool |            |           |
| switch(config-dhcp-server-pool)# |             |         | no           | dns-server | 10.0.20.1 |
| Command History                  |             |         |              |            |           |
| Release                          |             |         | Modification |            |           |
| 10.07orearlier                   |             |         | --           |            |           |
| Command Information              |             |         |              |            |           |
| Platforms                        | Command     | context |              | Authority  |           |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | --- | ------------------------------ | --- |
8360
9300
10000
domain-name
| domain-name    | <DOMAIN-NAME> |     |     |     |     |
| -------------- | ------------- | --- | --- | --- | --- |
| no domain-name | <DOMAIN-NAME> |     |     |     |     |
Description
DefinesadomainnameforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddomainnamefromthepool.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<DOMAIN-NAME> Specifiesadomainname.Range:1to255printableASCII
characters.
Example
Definesadomainnamefortheserverpoolprimary-poolonVRFprimary.
DHCP|104

| switch(config)# | dhcp-server | vrf | primary |     |     |
| --------------- | ----------- | --- | ------- | --- | --- |
switch(config-dhcp-server)#
|                                  |     | pool | primary-pool |     |                |
| -------------------------------- | --- | ---- | ------------ | --- | -------------- |
| switch(config-dhcp-server-pool)# |     |      | domain-name  |     | example.org.in |
Deletesadomainnamefromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf     | primary      |             |                |
| -------------------------------- | ----------- | ------- | ------------ | ----------- | -------------- |
| switch(config-dhcp-server)#      |             | pool    | primary-pool |             |                |
| switch(config-dhcp-server-pool)# |             |         | no           | domain-name | example.org.in |
| Command History                  |             |         |              |             |                |
| Release                          |             |         | Modification |             |                |
| 10.07orearlier                   |             |         | --           |             |                |
| Command Information              |             |         |              |             |                |
| Platforms                        | Command     | context |              | Authority   |                |
config-dhcp-server-pool
| 8320 |     |     |     | Administratorsorlocalusergroupmemberswith |     |
| ---- | --- | --- | --- | ----------------------------------------- | --- |
| 8325 |     |     |     | executionrightsforthiscommand.            |     |
8360
9300
10000
enable
enable
Description
EnablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhen
configuredonaVRF.
Example
EnablestheDHCPv4serveronVRFprimary.
| switch(config)#             | dhcp-server | vrf    | primary      |     |     |
| --------------------------- | ----------- | ------ | ------------ | --- | --- |
| switch(config-dhcp-server)# |             | enable |              |     |     |
| Command History             |             |        |              |     |     |
| Release                     |             |        | Modification |     |     |
| 10.07orearlier              |             |        | --           |     |     |
| Command Information         |             |        |              |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 105

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8320 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
9300
10000
http-proxy
| http-proxy    | {<FQDN | IPV4-ADDR>} |             | [vrf <VRF-NAME>] |
| ------------- | -------------------- | ----------- | ---------------- |
| no http-proxy | [<FQDN |             | IPV4-ADDR>] | [vrf <VRF-NAME>] |
Description
SpecifiesHTTPproxylocationandVRF.
ThenoformofthiscommandremovesaspecifiedHTTPproxylocation.
| Parameter   |     |     | Description                               |
| ----------- | --- | --- | ----------------------------------------- |
| <FQDN>      |     |     | SpecifiesFQDNforHTTP proxylocation.       |
| <IPV4-ADDR> |     |     | SpecifiesIPV4addressforHTTPproxylocation. |
| <VRF-NAME>  |     |     | SpecifiesVRF forHTTP proxy.               |
AFQDN orIPV4addressareoptionalinthenoformofthecommand.
Usage
n HTTPproxylocationcanbeconfiguredusingtheCLI/RESTinterfaceorauto-configuredthroughthe
DHCP serverconnectedtotheswitch.
n TherearethreesourcesforHTTPproxylocation:
o UserconfiguredHTTPproxyviaCLI orRESTinterface.
o DHCP optionsreceivedviamanagement/OOBMport.
o DHCPoptionsreceivedviaVLAN1onsupportedswitchplatforms.
nn OperationalconfigurationforHTTPproxylocationisdeterminedbythesourcewiththehighest
priority.Sourcepriority:
| 1.  | Userconfigured.                             |     |     |
| --- | ------------------------------------------- | --- | --- |
| 2.  | DHCPoptionsreceivedviamanagement/OOBM port. |     |     |
| 3.  | DHCP optionsreceivedviaVLAN1.               |     |     |
DHCP|106

n HTTPproxylocationcanonlybeaFQDNoranIPV4address.
n WhenHTTPproxylocationandVRFareconfigured,theyoverrideanyexistingHTTPproxylocationandVRF.
n IfthiscommandisexecutedwithouttheVRFparameter,thedefaultVRFwillbeused.
n PortnumbermayneedtobespecifiedattheendoftheIPaddressforFQDNtoconnectviaHTTPproxy.
o Forexample,8088istheTCPportnumber:http-proxy192.168.248.248:8088
Examples
SpecifyingaFQDNforHTTPproxylocationandMGMTVRF:
| switch(config)# | http-proxy | http-proxy.aruba.com |     | vrf mgmt |
| --------------- | ---------- | -------------------- | --- | -------- |
RemovingHTTPproxylocation
| switch(config)#     | no      | http-proxy |              |     |
| ------------------- | ------- | ---------- | ------------ | --- |
| Command History     |         |            |              |     |
| Release             |         |            | Modification |     |
| 10.07orearlier      |         |            | --           |     |
| Command Information |         |            |              |     |
| Platforms           | Command | context    | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lease
| lease {<TIME> | | infinite} |     |     |     |
| ------------- | ----------- | --- | --- | --- |
no lease
Description
SetsthelengthoftheDHCPv4leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv4clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv4leasetimetoitsdefaultvalue1hour.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<TIME>
SetstheDHCPv4leasetime.Format:DD:HH:MM.Default:
01:00:00.
infinite SetstheDHCPv4leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 107

Example
SetstheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimaryto12hours.
switch(config)#
|                                  | dhcp-server | vrf primary       |          |
| -------------------------------- | ----------- | ----------------- | -------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |          |
| switch(config-dhcp-server-pool)# |             | lease             | 00:12:00 |
DeletestheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |                |
| -------------------------------- | ----------- | ----------------- | -------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |                |
| switch(config-dhcp-server-pool)# |             | no                | lease 00:12:00 |
| Command History                  |             |                   |                |
| Release                          |             | Modification      |                |
| 10.07orearlier                   |             | --                |                |
| Command Information              |             |                   |                |
| Platforms                        | Command     | context           | Authority      |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
8360
9300
10000
netbios-name-server
| netbios-name-server    | <IPV4-ADDR-LIST> |                  |     |
| ---------------------- | ---------------- | ---------------- | --- |
| no netbios-name-server |                  | <IPV4-ADDR-LIST> |     |
Description
DefinesuptofourNetBIOSWINSserversforthecurrentDHCPv4serverpool.WINSisusedbyMicrosoft
DHCPclientstomatchhostnameswithIPaddresses.
ThenoformofthiscommandremovesthespecifiedWINSserversfromthepool.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesofNetBIOS(WINS)serversinIPv4
format(x.x.x.x),wherexisadecimalnumberfrom0to255.
Separateaddresseswithaspace.AmaximumoffourIP
addressescanbedefined.
Example
DefinestwoWINSserversfortheserverpoolprimary-poolonVRFprimary.
DHCP|108

| switch(config)# | dhcp-server | vrf | primary |     |
| --------------- | ----------- | --- | ------- | --- |
switch(config-dhcp-server)#
|     |     | pool | primary-pool |     |
| --- | --- | ---- | ------------ | --- |
switch(config-dhcp-server-pool)# netbios-name-server ip 10.0.20.1 10.0.30.10
DeletesaWINSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf  | primary      |     |
| --------------------------- | ----------- | ---- | ------------ | --- |
| switch(config-dhcp-server)# |             | pool | primary-pool |     |
switch(config-dhcp-server-pool)# no netbios-name-server ip 10.0.20.1
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
config-dhcp-server-pool
| 8320 |     |     | Administratorsorlocalusergroupmemberswith |     |
| ---- | --- | --- | ----------------------------------------- | --- |
| 8325 |     |     | executionrightsforthiscommand.            |     |
8360
9300
10000
netbios-node-type
| netbios-node-type    | <TYPE> |     |     |     |
| -------------------- | ------ | --- | --- | --- |
| no netbios-node-type | <TYPE> |     |     |     |
Description
DefinestheNetBIOSnodetypeforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovestheNetBIOSnodetypeforthecurrentpool.
| Parameter |     |     | Description                                           |     |
| --------- | --- | --- | ----------------------------------------------------- | --- |
| <TYPE>    |     |     | SpecifiestheNetBIOSnodetype:broadcast,hybrid,mixed,or |     |
peer-to-peer.
Examples
DefinestheNetBIOSnodetypebroadcastfortheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf  | primary           |           |
| -------------------------------- | ----------- | ---- | ----------------- | --------- |
| switch(config-dhcp-server)#      |             | pool | primary-pool      |           |
| switch(config-dhcp-server-pool)# |             |      | netbios-node-type | broadcast |
DeletestheNetBIOSnodetypebroadcastfromtheDHCPv4serverpoolprimary-poolonVRFprimary.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 109

| switch(config)# | dhcp-server | vrf primary |     |
| --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
|     |     | pool primary-pool |     |
| --- | --- | ----------------- | --- |
switch(config-dhcp-server-pool)# no netbios-node-type broadcast
| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
8360
9300
10000
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
Description
DefinescustomDHCPv4optionsforthecurrentDHCPv4serverpool.DHCPv4optionsenablethe
DHCPv4servertoprovideadditionalinformationaboutthenetworkwhenDHCPv4clientsrequestan
address.
ThenoformofthiscommandremovescustomDHCPv4optionsfromthepool.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<OPTION-NUM> SpecifiesaDHCPv4optionnumber.ForalistofDHCPv4option
numbers,seehttps://www.iana.org/assignments/bootp-dhcp-
parameters/bootp-dhcp-parameters.xhtml.Range:2to254.
ascii <ASCII-STR> SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:
1to255ASCIIcharacters.
hex <HEX-STR> Specifiesavaluefortheselectedoptionasahexadecimalstring.
Range:1to255hexadecimalcharacters.
ip <IPV4-ADDR-LIST> SpecifiesalistofIPaddressesinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
DHCP|110

| switch(config)# | dhcp-server | vrf | primary |     |
| --------------- | ----------- | --- | ------- | --- |
switch(config-dhcp-server)#
|                                  |     | pool | primary-pool |                  |
| -------------------------------- | --- | ---- | ------------ | ---------------- |
| switch(config-dhcp-server-pool)# |     |      | option       | 3 ip 192.168.1.1 |
DeletesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf     | primary      |                         |
| -------------------------------- | ----------- | ------- | ------------ | ----------------------- |
| switch(config-dhcp-server)#      |             | pool    | primary-pool |                         |
| switch(config-dhcp-server-pool)# |             |         | no           | option 3 ip 192.168.1.1 |
| Command History                  |             |         |              |                         |
| Release                          |             |         | Modification |                         |
| 10.07orearlier                   |             |         | --           |                         |
| Command Information              |             |         |              |                         |
| Platforms                        | Command     | context |              | Authority               |
config-dhcp-server-pool
| 8320 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
| 8325 |     |     |     | executionrightsforthiscommand.            |
8360
9300
10000
pool
pool <POOL-NAME>
no pool <POOL-NAME>
Description
CreatesaDHCPv4serverpoolforthecurrentVRFandswitchestotheconfig-dhcp-server-pool
contextforit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64
pools(IPv4andIPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv4serverpool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<POOL-NAME>
SpecifiestheDHCPv4poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf  | primary      |     |
| --------------------------- | ----------- | ---- | ------------ | --- |
| switch(config-dhcp-server)# |             | pool | primary-pool |     |
switch(config-dhcp-server-pool)#
DeletestheDHCPv4serverpoolprimary-poolonVRFprimary.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 111

| switch(config)# |     | dhcp-server | vrf | primary |     |     |     |
| --------------- | --- | ----------- | --- | ------- | --- | --- | --- |
switch(config-dhcp-server)#
|                     |         |         | no  | pool primary-pool |     |     |     |
| ------------------- | ------- | ------- | --- | ----------------- | --- | --- | --- |
| Command History     |         |         |     |                   |     |     |     |
| Release             |         |         |     | Modification      |     |     |     |
| 10.07orearlier      |         |         |     | --                |     |     |     |
| Command Information |         |         |     |                   |     |     |     |
| Platforms           | Command | context |     | Authority         |     |     |     |
8320 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     |     | rightsforthiscommand. |     |     |     |
| ---- | --- | --- | --- | --------------------- | --- | --- | --- |
8360
9300
10000
range
| range <LOW-IPV4-ADDR>    |     | <HIGH-IPV4-ADDR> |     | [prefix-len | <MASK>] |     |     |
| ------------------------ | --- | ---------------- | --- | ----------- | ------- | --- | --- |
| no range <LOW-IPV4-ADDR> |     | <HIGH-IPV4-ADDR> |     | [prefix-len | <MASK>] |     |     |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv4serverpool.Amaximumof64
rangesaresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<LOW-IPV4-ADDR> SpecifiesthelowestIPaddressinthepoolinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
<HIGH-IPV4-ADDR>
SpecifiesthehighestIPaddressinthepoolinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
| prefix-len | <MASK> |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- |
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat(x),
wherexisadecimalnumberfrom0to32.
NOTE:Whenactivegatewayisconfiguredontheinterfaceserviced
bythepool,youmustspecifyaprefixlengththatmatchesthemask
ontheIPaddressassignedtotheinterface.Otherwise,client
stationswillgetaprefixlengthfromactivegatewaythatmaynotbe
consistentwiththeconfiguredrange,andaDHCPerrorwilloccur.In
thefollowingexample,theDHCPrangeprefixissetto16tomatch
themaskontheIPaddressassignedtointerfaceVLAN2.
|     |     |     |     | switch(config)#         | interface   | vlan 2         |              |
| --- | --- | --- | --- | ----------------------- | ----------- | -------------- | ------------ |
|     |     |     |     | switch(config-if-vlan)# |             | ip address     | 200.1.1.1/16 |
|     |     |     |     | switch(config-if-vlan)# |             | active-gateway | ip 200.1.1.3 |
|     |     |     |     | mac 00:aa:aa:aa:aa:aa   |             |                |              |
|     |     |     |     | switch(config-if-vlan)# |             | exit           |              |
|     |     |     |     | switch(config)#         | dhcp-server | vrf            | primary      |
DHCP|112

| Parameter |     |     | Description                      |     |            |                   |
| --------- | --- | --- | -------------------------------- | --- | ---------- | ----------------- |
|           |     |     | switch(config-dhcp-server)#      |     |            | pool primary-pool |
|           |     |     | switch(config-dhcp-server-pool)# |     |            | range 192.168.1.1 |
|           |     |     | 192.168.1.100                    |     | prefix-len | 16                |
Examples
Definestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfortheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |     |     |
| --------------------------- | ----------- | --- | ----------------- | --- | --- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |     |     |
switch(config-dhcp-server-pool)# 192.168.1.1 192.168.1.100 prefix-len 24
Deletestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfromtheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |     |     |
| --------------------------- | ----------- | --- | ----------------- | --- | --- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |     |     |
switch(config-dhcp-server-pool)# no 192.168.1.1 192.168.1.100 prefix-len 24
| Command History     |         |         |              |           |     |     |
| ------------------- | ------- | ------- | ------------ | --------- | --- | --- |
| Release             |         |         | Modification |           |     |     |
| 10.07orearlier      |         |         | --           |           |     |     |
| Command Information |         |         |              |           |     |     |
| Platforms           | Command | context |              | Authority |     |     |
config-dhcp-server-pool
| 8320 |     |     |     | Administratorsorlocalusergroupmemberswith |     |     |
| ---- | --- | --- | --- | ----------------------------------------- | --- | --- |
| 8325 |     |     |     | executionrightsforthiscommand.            |     |     |
8360
9300
10000
show dhcp-server
| show dhcp-server | [all-vrfs] |             |                  |             |     |     |
| ---------------- | ---------- | ----------- | ---------------- | ----------- | --- | --- |
| show dhcp-server | leases     | {all-vrfs   | | vrf            | <VRF-NAME>} |     |     |
| show dhcp-server | pool       | <POOL-NAME> | [vrf <VRF-NAME>] |             |     |     |
Description
ShowsconfigurationsettingsfortheDHCPv4server.
| Parameter        |       |             |     | Description                                       |     |     |
| ---------------- | ----- | ----------- | --- | ------------------------------------------------- | --- | --- |
| all-vrfs         |       |             |     | ShowsDHCPv4serverconfigurationsettingsforallVRFs. |     |     |
| leases {all-vrfs | | vrf | <VRF-NAME>} |     |                                                   |     |     |
ShowsDHCPv4serverleaseconfigurationsettingsforallVRFs
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 113

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
oraspecificVRF.
pool <POOL-NAME> [vrf <VRF-NAME>] ShowsDHCPv4serverpoolconfigurationsettingsforallVRFs
oraspecificVRF.
Examples
ShowingallDHCPv4serverconfigurationsettings.
| switch# show   | dhcp-server |               |     |     |     |     |
| -------------- | ----------- | ------------- | --- | --- | --- | --- |
| VRF Name       |             | : default     |     |     |     |     |
| DHCP Server    |             | : enabled     |     |     |     |     |
| Operational    | State       | : operational |     |     |     |     |
| Authoritative  | Mode        | : false       |     |     |     |     |
| Pool Name      |             | : test        |     |     |     |     |
| Lease Duration |             | : 00:01:00    |     |     |     |     |
| DHCP dynamic   | IP          | allocation    |     |     |     |     |
--------------------------
| Start-IP-Address |         | End-IP-Address |     |     | Prefix-Length  |     |
| ---------------- | ------- | -------------- | --- | --- | -------------- | --- |
| ---------------- |         | -------------- |     |     | -------------- |     |
| 192.168.1.1      |         | 192.168.1.20   |     |     | 24             |     |
| DHCP Server      | options |                |     |     |                |     |
-------------------
| Option-Number |        | Option-Type |            | Option-Value |          |                   |
| ------------- | ------ | ----------- | ---------- | ------------ | -------- | ----------------- |
| ------------- |        | ----------- |            | ------------ |          |                   |
| 6             |        | ip          |            | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 10.0.0.6 |
| DHCP Server   | static | IP          | allocation |              |          |                   |
--------------------------------
| IP-Address  |     | Client-Hostname  |     |     | State       | MAC-Address       |
| ----------- | --- | ---------------- | --- | --- | ----------- | ----------------- |
| ----------- |     | ---------------- |     |     | ------      | ------------      |
| 10.0.0.3    |     | *                |     |     | OPERATIONAL | aa:aa:aa:aa:aa:aa |
BOOTP Options
---------------
| Boot-File-Name |     | TFTP-Server-Name |     |     | TFTP-Server-Address   |     |
| -------------- | --- | ---------------- | --- | --- | --------------------- | --- |
| -------------- |     | ---------------- |     |     | --------------------- |     |
| boot.txt       |     | *                |     |     | 10.0.0.10             |     |
ShowingDHCPserverconfigurationsettingsforVRFprimary-vrf.
| switch# show  | dhcp-server |               | vrf | primary-vrf |     |     |
| ------------- | ----------- | ------------- | --- | ----------- | --- | --- |
| VRF Name      |             | : primary-vrf |     |             |     |     |
| DHCP Server   |             | : disabled    |     |             |     |     |
| Operational   | State       | : disabled    |     |             |     |     |
| Authoritative | Mode        | : false       |     |             |     |     |
| Pool Name     |             | : test        |     |             |     |     |
DHCP|114

| Lease Duration |     | : 00:01:00 |     |     |     |     |
| -------------- | --- | ---------- | --- | --- | --- | --- |
| DHCP dynamic   | IP  | allocation |     |     |     |     |
--------------------------
| Start-IP-Address |         | End-IP-Address |     | Prefix-Length  |     |     |
| ---------------- | ------- | -------------- | --- | -------------- | --- | --- |
| ---------------- |         | -------------- |     | -------------- |     |     |
| 10.0.0.1         |         | 10.0.0.30      |     | *              |     |     |
| 192.168.1.1      |         | 192.168.1.20   |     | 24             |     |     |
| 192.168.10.30    |         | 192.168.10.60  |     | 16             |     |     |
| DHCP Server      | options |                |     |                |     |     |
-------------------
| Option-Number |        | Option-Type   | Option-Value |          |          |          |
| ------------- | ------ | ------------- | ------------ | -------- | -------- | -------- |
| ------------- |        | -----------   | ------------ |          |          |          |
| 6             |        | ip            | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 | 10.0.0.6 |
| 18            |        | ascii         | aswed        |          |          |          |
| DHCP Server   | static | IP allocation |              |          |          |          |
--------------------------------
| IP-Address    | Client-Hostname |     | MAC-Address       |     |     |     |
| ------------- | --------------- | --- | ----------------- | --- | --- | --- |
| ----------    | --------------- |     | ----------------- |     |     |     |
| 10.0.0.1      |                 | *   | aa:bb:cc:11:12:a4 |     |     |     |
| 20.0.0.1      |                 | *   | 11:22:11:22:aa:dd |     |     |     |
| BOOTP Options |                 |     |                   |     |     |     |
---------------
| Boot-File-Name      |         | TFTP-Server-Name |     | State        |     | TFTP-Server-Address   |
| ------------------- | ------- | ---------------- | --- | ------------ | --- | --------------------- |
| --------------      |         | ---------------- |     | ------       |     | --------------------- |
| boot.txt            |         | *                |     | OPERATIONAL  |     | 10.0.0.10             |
| Command History     |         |                  |     |              |     |                       |
| Release             |         |                  |     | Modification |     |                       |
| 10.07orearlier      |         |                  |     | --           |     |                       |
| Command Information |         |                  |     |              |     |                       |
| Platforms           | Command | context          |     | Authority    |     |                       |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
8360
9300
10000
static-bind
static-bind {ip <IPV4-ADDR>}|{ mac <MAC-ADDR>} [hostname <HOST>]
| no static-bind | <IPV4-ADDR-LIST> |     |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- | --- |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaspecificMACaddress.
ThiscausestheDHCPv4servertoonlyassignthespecifiedIPaddresstoaclientstationwiththe
specifiedMACaddress.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 115

Thenoformofthiscommandremovesthespecifiedbinding.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.TheIPaddressmustbewithinthe
addressrangedefinedforthecurrentpool.
mac <MAC-ADDR> SpecifiesaclientstationMACaddress(xx:xx:xx:xx:xx:xx),
wherexisahexadecimalnumberfrom0toF.
hostname <HOST> Specifiesthehostnameoftheclientstation.Range:1to255
printableASCIIcharacters
Examples
Definesastaticaddressfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
Deletesastaticaddressfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# no static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
8325
8360
9300
10000
| DHCP server | IPv6 | commands |     |
| ----------- | ---- | -------- | --- |
authoritative
authoritative
no authoritative
Description
DHCP|116

ConfigurestheDHCPv6serverasauthoritativeonthecurrentVRF.Thismeansthattheserveristhesole
authorityforthenetworkontheVRF.Itrespondstoclientsolicitmessageswithadvertisemessages
havingapriority/preferencevaluesetto255(themaximum),insteadof0(theminimum).Clientsalways
choosetheDHCPv6serverwiththehighestpriority/preferencevalue.IftwoDHCPv6serverssendan
advertisemessagewiththesamepriority/preferencevalue,thentheclientpicksoneanddiscardsthe
other.
ThenoformofthiscommanddisablesauthoritativemodeonthecurrentVRF.
Example
ConfiguresDHCPv6serverauthoritativemodeonVRFprimary.
| switch(config)#               | dhcpv6-server | vrf           | primary |
| ----------------------------- | ------------- | ------------- | ------- |
| switch(config-dhcpv6-server)# |               | authoritative |         |
RemovesDHCPv6serverauthoritativemodeonVRFprimary.
| switch(config)#               | dhcpv6-server | vrf     | primary       |
| ----------------------------- | ------------- | ------- | ------------- |
| switch(config-dhcpv6-server)# |               | no      | authoritative |
| Command History               |               |         |               |
| Release                       |               |         | Modification  |
| 10.07orearlier                |               |         | --            |
| Command Information           |               |         |               |
| Platforms                     | Command       | context | Authority     |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
9300
10000
| clear dhcpv6-server | leases |     |     |
| ------------------- | ------ | --- | --- |
clear dhcpv6-server leases [all-vrfs | <IPV6-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv6serverleaseinformation.TheDHCPv6servermustbedisabledbeforeclearinglease
information.
| Parameter |     |     | Description             |
| --------- | --- | --- | ----------------------- |
| all-vrfs  |     |     | ClearsleasesforallVRFs. |
<IPV6-ADDR> vrf <VRF-NAME> ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 117

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
vrf <VRF-NAME>
ClearsleasesforaspecificVRF.
Examples
ClearingallDHCPv6serverleases.
| switch(config)# |     | dhcpv6-server |     | vrf | primary |     |
| --------------- | --- | ------------- | --- | --- | ------- | --- |
switch(config-dhcpv6-server)#
disable
| switch(config-dhcpv6-server)# |       |               |     | exit   |     |     |
| ----------------------------- | ----- | ------------- | --- | ------ | --- | --- |
| switch(config)#               |       | exit          |     |        |     |     |
| switch#                       | clear | dhcpv6-server |     | leases |     |     |
ClearingallDHCPv6serverleasesforVRFprimary-vrf.
| switch(config)#               |     | dhcpv6-server |     | vrf     | primary |     |
| ----------------------------- | --- | ------------- | --- | ------- | ------- | --- |
| switch(config-dhcpv6-server)# |     |               |     | disable |         |     |
| switch(config-dhcpv6-server)# |     |               |     | exit    |         |     |
| switch(config)#               |     | exit          |     |         |         |     |
switch#
|     | clear | dhcpv6-server |     | leases | vrf primary-vrf |     |
| --- | ----- | ------------- | --- | ------ | --------------- | --- |
CleartheDHCPv6serverleaseforIPaddress2001::1onVRFprimary-vrf.
| switch(config)#               |             | dhcpv6-server |         | vrf     | primary      |                 |
| ----------------------------- | ----------- | ------------- | ------- | ------- | ------------ | --------------- |
| switch(config-dhcpv6-server)# |             |               |         | disable |              |                 |
| switch(config-dhcpv6-server)# |             |               |         | exit    |              |                 |
| switch(config)#               |             | exit          |         |         |              |                 |
| switch#                       | clear       | dhcpv6-server |         | leases  | 2001::1      | vrf primary-vrf |
| Command                       | History     |               |         |         |              |                 |
| Release                       |             |               |         |         | Modification |                 |
| 10.07orearlier                |             |               |         |         | --           |                 |
| Command                       | Information |               |         |         |              |                 |
| Platforms                     |             | Command       | context |         | Authority    |                 |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     |     |     | commandfromtheoperatorcontext(>)only.                 |     |
9300
10000
| dhcv6p-server |     | external-storage |     |     |     |     |
| ------------- | --- | ---------------- | --- | --- | --- | --- |
DHCP|118

dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
Description
ConfigurestheexternalstoragefilelocationforDHCPv6serverleaseinformation.Thisfileprovides
persistentstorage,enablingDHCPv6serversettingstoberestoredwhentheswitchisrestarted.Lease
informationisstoredinaflatfileontheconfiguredexternaldevice.
Ifexternalstorageisnotconfigured,thenafterafailureorreboot,allexistingleaseinformationislost.
Leaseinformationissavedtoexternalstorageeachtimethedelaytimerexpires,whichbydefaultis
every300seconds.
Leaseinformationisnotrestoredwhenissuingthecommanddhcp-server enable.
ThenoformofthiscommandremovesexternalstoragesupportfortheDHCPv6server.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VOLUME-NAME> Specifiestheexternalstoragevolumename.Range:1to64
printableASCIIcharacters.
file <LEASE-FILENAME> Specifiestheexternalstoragefilename.Range:1to255printable
ASCIIcharacters.
delay <DELAY> Specifiestheintervalinsecondsbetweenupdatestotheexternal
storagefile.Range:15to86400.Default:300.
Example
StorestheleasefileonexternalstoragevolumeStorage1infileLeaseFileatanintervalof600seconds.
switch(config)# dhcpv6-server external-storage Storage1 file LeaseFile delay 600
DisablesstorageoftheleasefileonexternalstoragevolumeStorage1infileLeaseFile.
switch(config)# no dhcpv6-server external-storage Storage1 file LeaseFile delay
600
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config
| 8320 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
| 8325 |     |     | rightsforthiscommand.                              |
8360
9300
10000
| dhcpv6-server | vrf |     |     |
| ------------- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 119

| dhcpv6-server    | vrf VRF-NAME |     |     |
| ---------------- | ------------ | --- | --- |
| no dhcpv6-server | vrf VRF-NAME |     |     |
Description
ConfigurestheDHCPv6servertosupportaVRFandchangestotheconfig-dhcpv6-servercontextfor
thatVRF.
ThenoformofthiscommandremovesDHCPv6serversupportonaVRF.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
| VRF-NAME  |     |     | NameofaVRF. |
Example
ConfiguresDHCPv6serversupportonVRFprimary.
| switch(config)# | dhcpv6-server |     | vrf primary |
| --------------- | ------------- | --- | ----------- |
RemovestheDHCPv6serversupportonVRFprimary.
| switch(config)#     | no      | dhcpv6-server | vrf primary  |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
9300
10000
disable
disable
Description
DisablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhen
configuredonaVRF.
Example
DisablestheDHCPv6serveronVRFprimary.
DHCP|120

| switch(config)# | dhcpv6-server | vrf | primary |     |
| --------------- | ------------- | --- | ------- | --- |
switch(config-dhcpv6-server)#
disable
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
8360
9300
10000
dns-server
| dns-server <IPVv6-ADDR-LIST> |                   |     |     |     |
| ---------------------------- | ----------------- | --- | --- | --- |
| no dns-server                | <IPVv6-ADDR-LIST> |     |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPVv6-ADDR-LIST>
SpecifiestheIPaddressesoftheDNSserversinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDNSserver2001::13fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf  | primary      |          |
| ---------------------------------- | ------------- | ---- | ------------ | -------- |
| switch(config-dhcpv6-server)#      |               | pool | primary-pool |          |
| switch(config-dhcpv6-server-pool)# |               |      | dns-server   | 2001::13 |
DeletesDNSserver2001::13fromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf  | primary       |          |
| ---------------------------------- | ------------- | ---- | ------------- | -------- |
| switch(config-dhcpv6-server)#      |               | pool | primary-pool  |          |
| switch(config-dhcpv6-server-pool)# |               |      | no dns-server | 2001::13 |
| Command History                    |               |      |               |          |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 121

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8320 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
8360
9300
10000
enable
enable
Description
EnablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhen
configuredonaVRF.
Example
EnablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcpv6-server |         | vrf primary  |     |
| ----------------------------- | ------------- | ------- | ------------ | --- |
| switch(config-dhcpv6-server)# |               |         | enable       |     |
| Command History               |               |         |              |     |
| Release                       |               |         | Modification |     |
| 10.07orearlier                |               |         | --           |     |
| Command Information           |               |         |              |     |
| Platforms                     | Command       | context | Authority    |     |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
8360
9300
10000
lease
| lease {<TIME> | | infinite} |     |     |     |
| ------------- | ----------- | --- | --- | --- |
no lease
Description
SetsthelengthoftheDHCPv6leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv6clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv6leasetimetothedefaultvalue1hour.
DHCP|122

Parameter Description
<TIME> SetstheDHCPv6leasetime.Format:DD:HH:MM.Default:
01:00:00.
infinite
SetstheDHCPv6leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
Example
SetstheleasetimeforDHCPv6serverpoolprimary-poolonVRFprimaryto12hours.
switch(config)#
dhcpv6-server vrf primary
| switch(config-dhcpv6-server)#      |     | pool primary-pool |          |
| ---------------------------------- | --- | ----------------- | -------- |
| switch(config-dhcpv6-server-pool)# |     | lease             | 00:12:00 |
SetstheleasetimeforDHCPserverpoolprimary-poolonVRFprimarytothedefaultvalue.
| switch(config)#                    | dhcpv6-server | vrf primary       |                |
| ---------------------------------- | ------------- | ----------------- | -------------- |
| switch(config-dhcpv6-server)#      |               | pool primary-pool |                |
| switch(config-dhcpv6-server-pool)# |               | no                | lease 00:12:00 |
| Command History                    |               |                   |                |
Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8320 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | ------------------------------ |
8360
9300
10000
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
Description
DefinescustomDHCPv6optionsforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovescustomDHCPv6optionsfromthepool.
Parameter Description
<OPTION-NUM> SpecifiesaDHCPv6optionnumber.Range:2to254.
ascii <ASCII-STR> SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 123

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
1to255ASCIIcharacters.
hex <HEX-STR> Specifiesavaluefortheselectedoptionasahexadecimalstring.
Range:1to255hexadecimalcharacters.
ip <IPV6-ADDR-LIST> SpecifiesalistofIPaddressesfortheoptioninIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Example
DefinesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
| switch(config)# | dhcpv6-server |     | vrf primary |     |
| --------------- | ------------- | --- | ----------- | --- |
switch(config-dhcpv6-server)#
pool primary-pool
| switch(config-dhcpv6-server-pool)# |     |     | option | 22 ipv6 2001::12 |
| ---------------------------------- | --- | --- | ------ | ---------------- |
DeletesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server |         | vrf primary       |                         |
| ---------------------------------- | ------------- | ------- | ----------------- | ----------------------- |
| switch(config-dhcpv6-server)#      |               |         | pool primary-pool |                         |
| switch(config-dhcpv6-server-pool)# |               |         | no                | option 22 ipv6 2001::12 |
| Command History                    |               |         |                   |                         |
| Release                            |               |         | Modification      |                         |
| 10.07orearlier                     |               |         | --                |                         |
| Command Information                |               |         |                   |                         |
| Platforms                          | Command       | context |                   | Authority               |
config-dhcpv6-server-pool
| 8320 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
| 8325 |     |     |     | executionrightsforthiscommand.            |
8360
9300
10000
pool
pool <POOL-NAME>
no pool <POOL-NAME>
Description
CreatesaDHCPv6serverpoolforthecurrentVRFandswitchestotheconfig-dhcpv6-server-pool
contextforit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64
pools(IPv4andIPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv6serverpool.
DHCP|124

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<POOL-NAME> SpecifiestheDHCPv6poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)#
DeletestheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |         | dhcpv6-server | vrf | primary           |     |
| ----------------------------- | ------- | ------------- | --- | ----------------- | --- |
| switch(config-dhcpv6-server)# |         |               | no  | pool primary-pool |     |
| Command History               |         |               |     |                   |     |
| Release                       |         |               |     | Modification      |     |
| 10.07orearlier                |         |               |     | --                |     |
| Command Information           |         |               |     |                   |     |
| Platforms                     | Command | context       |     | Authority         |     |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
9300
10000
range
| range <LOW-IPV6-ADDR>    |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
| ------------------------ | --- | ---------------- | --- | ----------- | ------- |
| no range <LOW-IPV6-ADDR> |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv6serverpool.Amaximumof64
rangesaresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<LOW-IPV6-ADDR> SpecifiesthelowestIPaddressinthepoolinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 125

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<HIGH-IPV6-ADDR> SpecifiesthehighestIPaddressinthepoolinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
prefix-len <MASK> SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom64to128.
Example
DefinesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary       |     |
| ----------------------------- | ------------- | --- | ----------------- | --- |
| switch(config-dhcpv6-server)# |               |     | pool primary-pool |     |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::10 prefix-len 64
DeletesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary       |     |
| ----------------------------- | ------------- | --- | ----------------- | --- |
| switch(config-dhcpv6-server)# |               |     | pool primary-pool |     |
switch(config-dhcpv6-server-pool)# no range 2001::1 2001::10 prefix-len 64
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
8320 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
8360
9300
10000
show dhcpv6-server
| show dhcpv6-server | [all-vrfs] |             |                  |             |
| ------------------ | ---------- | ----------- | ---------------- | ----------- |
| show dhcpv6-server | leases     | {all-vrfs   | | vrf            | <VRF-NAME>} |
| show dhcpv6-server | pool       | <POOL-NAME> | [vrf <VRF-NAME>] |             |
Description
ShowsconfigurationsettingsfortheDHCPv6server.
| Parameter |     |     | Description                                       |     |
| --------- | --- | --- | ------------------------------------------------- | --- |
| all-vrfs  |     |     | ShowsDHCPv6serverconfigurationsettingsforallVRFs. |     |
DHCP|126

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
leases {all-vrfs | vrf <VRF-NAME>} ShowsDHCPv6serverleaseconfigurationsettingsforallVRFs
oraspecificVRF.
| pool <POOL-NAME> | [vrf | <VRF-NAME>] |     |     |
| ---------------- | ---- | ----------- | --- | --- |
ShowsDHCPv6serverpoolconfigurationsettingsforallVRFs
oraspecificVRF.
Examples
ShowingallDHCPv6serverconfigurationsettings.
switch#
show dhcpv6-server
| VRF Name       |       | : default     |     |     |
| -------------- | ----- | ------------- | --- | --- |
| DHCPv6 Server  |       | : enabled     |     |     |
| Operational    | State | : operational |     |     |
| Authoritative  | Mode  | : true        |     |     |
| Pool Name      |       | : test        |     |     |
| Lease Duration |       | : 00:01:00    |     |     |
| DHCPV6 dynamic | IP    | allocation    |     |     |
-----------------------------
| Start-IPv6-Address |         | End-IPv6-Address |     | Prefix-Length |
| ------------------ | ------- | ---------------- | --- | ------------- |
| ------------------ |         | ---------------- |     | ------------- |
| 2001::2            |         | 2001::10         |     | 64            |
| DHCPv6 Server      | options |                  |     |               |
---------------------
| Option-Number |        | Option-Type | Option-Value |     |
| ------------- | ------ | ----------- | ------------ | --- |
| ------------- |        | ----------- | ------------ |     |
| 7             |        | ipv6        | 2001::15     |     |
| DHCvP6 Server | static | IP          | allocation   |     |
-----------------------------------
| DHCPv6 Server | static | host | is not configured. |     |
| ------------- | ------ | ---- | ------------------ | --- |
ShowingDHCPv6serverconfigurationsettingsforVRFprimary-vrf.
| switch# show   | dhcpv6-server |               | vrf primary-vrf |     |
| -------------- | ------------- | ------------- | --------------- | --- |
| VRF Name       |               | : primary-vrf |                 |     |
| DHCPv6 Server  |               | : disabled    |                 |     |
| Operational    | State         | : standby     |                 |     |
| Authoritative  | Mode          | : false       |                 |     |
| Pool Name      |               | : test        |                 |     |
| Lease Duration |               | : 00:01:00    |                 |     |
| DHCPV6 dynamic | IP            | allocation    |                 |     |
-----------------------------
| Start-IPv6-Address |     | End-IPv6-Address |     | Prefix-Length |
| ------------------ | --- | ---------------- | --- | ------------- |
| ------------------ |     | ---------------- |     | ------------- |
| 2000::1            |     | 2000::20         |     | *             |
| 2001::20           |     | 2001::50         |     | *             |
| 2001::2            |     | 2001::10         |     | 64            |
| 2010::20           |     | 2010::40         |     | *             |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 127

| DHCPv6 Server |     | options |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- |
---------------------
| Option-Number |     | Option-Type |               | Option-Value |     |     |
| ------------- | --- | ----------- | ------------- | ------------ | --- | --- |
| ------------- |     | ----------- |               | ------------ |     |     |
| 7             |     | ipv6        |               | 2001::15     |     |     |
| 23            |     | ipv6        |               | 2001::30     |     |     |
| 30            |     | ipv6        |               | 2001::10     |     |     |
| DHCvP6 Server |     | static      | IP allocation |              |     |     |
-----------------------------------
| DHCPv6 Server  |     | static        | host is | not configured. |     |     |
| -------------- | --- | ------------- | ------- | --------------- | --- | --- |
| Pool Name      |     | : v6test      |         |                 |     |     |
| Lease Duration |     | : 00:01:00    |         |                 |     |     |
| DHCPv6 dynamic |     | IP allocation |         |                 |     |     |
-----------------------------
| Start-IPv6-Address |     |         | End-IPv6-Address |     | Prefix-Length |     |
| ------------------ | --- | ------- | ---------------- | --- | ------------- | --- |
| ------------------ |     |         | ---------------- |     | ------------- |     |
| 2001::1            |     |         | 2001::20         |     | 64            |     |
| 2010::10           |     |         | 2010::30         |     | *             |     |
| 2020::20           |     |         | 2020::60         |     | *             |     |
| DHCPv6 Server      |     | options |                  |     |               |     |
---------------------
| Option-Number |     | Option-Type |     | Option-Value                            |     |     |
| ------------- | --- | ----------- | --- | --------------------------------------- | --- | --- |
| ------------- |     | ----------- |     | -----------------                       |     |     |
| 7             |     | ipv6        |     | 2001::20                                |     |     |
| 23            |     | ipv6        |     | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |     |
2001:0db8:85a3:0000:0000:8a2e:0370:7335
2001:0db8:85a3:0000:0000:8a2e:0370:7336
2001:0db8:85a3:0000:0000:8a2e:0370:7337
| DHCPv6 Server |     | static | IP allocation |     |     |     |
| ------------- | --- | ------ | ------------- | --- | --- | --- |
------------------------------------
| IPv6-Address        |         | Client-Hostname |         | State        |     | Client-Id          |
| ------------------- | ------- | --------------- | ------- | ------------ | --- | ------------------ |
| ------------        |         | --------------- |         | -----------  |     | ---------          |
| 2100::4             |         | *               |         | OPERATIONAL  |     | 1:0:a0:24:ab:fb:9c |
| Command History     |         |                 |         |              |     |                    |
| Release             |         |                 |         | Modification |     |                    |
| 10.07orearlier      |         |                 |         | --           |     |                    |
| Command Information |         |                 |         |              |     |                    |
| Platforms           | Command |                 | context | Authority    |     |                    |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
8360
9300
10000
static-bind
DHCP|128

| static-bind    | ipv6 | <IPVv6-ADDR>      | client-id | <ID> [hostname | <HOST>] |
| -------------- | ---- | ----------------- | --------- | -------------- | ------- |
| no static-bind | ipv6 | <IPVv6-ADDR-LIST> |           |                |         |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaclientidentifierorDUID.
ThiscausestheDHCPv6servertoonlyassignthespecifiedIPaddresstoaclientstationwiththe
specifiedclientidentifierorDUID.
Thenoformofthiscommandremovesthespecifiedstaticbindingfromthepool.
| Parameter   |     |     |     | Description                               |     |
| ----------- | --- | --- | --- | ----------------------------------------- | --- |
| <IPV6-ADDR> |     |     |     | SpecifiestheIPaddresstoassigninIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Forexample,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| client-id | <ID> |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- |
SpecifiestheclientidentifierorDUID.
hostname <HOST> Specifiesthehostnameoftheclientstation.Range:1to255
printableASCIIcharacters
Example
DefinesastaticaddressfortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)# static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c
DeletesastaticaddressfromtheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)# no static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c
| Command        | History     |         |     |              |     |
| -------------- | ----------- | ------- | --- | ------------ | --- |
| Release        |             |         |     | Modification |     |
| 10.07orearlier |             |         |     | --           |     |
| Command        | Information |         |     |              |     |
| Platforms      | Command     | context |     | Authority    |     |
config-dhcpv6-server-pool
| 8320 |     |     |     | Administratorsorlocalusergroupmemberswith |     |
| ---- | --- | --- | --- | ----------------------------------------- | --- |
| 8325 |     |     |     | executionrightsforthiscommand.            |     |
8360
9300
10000
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 129

Chapter 6

DHCP snooping

DHCP snooping

Applies only to the 8360 Switch Series.

DHCP is a protocol used by DHCP servers in IP networks to dynamically allocate network configuration
data to client devices (DHCP clients). Possible network configuration data includes user IP address,
subnet mask, default gateway IP address, DNS server IP address, and lease duration. The DHCP protocol
enables DHCP clients to be dynamically configured with such network configuration data without any
manual setup process.

DHCP snooping is a security feature that helps avoid problems caused by an unauthorized DHCP server
on the network that provides invalid configuration data to DHCP clients. A user without malicious intent
may cause this problem by unknowingly adding to the network a switch or other device that includes a
DHCP server enabled by default. In some cases, a user with malicious intent adds a DHCP server to the
network as part of their Denial of Service or Man in the Middle attack.

DHCP snooping helps prevent such problems by distinguishing between trusted ports connected to
legitimate DHCP servers and untrusted ports connected to general users. DHCP packets are forwarded
between trusted ports without inspection. DHCP packets received on other switch ports are inspected
before being forwarded. DHCP Packets from untrusted sources are dropped.

DHCP Snooping and DHCP relay can be configured on the same switch.

When DHCP snooping and DHCP relay are both enabled on a VLAN, the following actions occur:

n Received packet: DHCP snooping processes the DHCP packet before (possibly) handing it to DHCP relay.

n Transmitted packet: DHCP packets sent by DHCP relay are intercepted by DHCP snooping to learn IP

bindings.

For even more rigorous security that is applied in hardware on a packet-by-packet basis, you can use IP source
lockdown feature as described in IP source lockdown.

DHCPv6 guard

The DHCPv6 guard feature is an extension of DHCPv6 snooping. When the DHCPv6 snooping feature is
configured globally and on the VLAN, the ports are configured as trusted and untrusted ports on the
VLAN. DHCPv6 guard enhances this feature by creating a policy and applying it on a port and VLAN. This
policy contains multiple attributes which are compared against the packet that is received on trusted
ports. If the packet complies with the attributes of the policy, it is forwarded to the destination port;
otherwise the packet is dropped.

DHCP server interoperation

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

130

DHCP server may not be configured with DHCP snooping.

DHCPv4 snooping conditions for dropping DHCPv4 packets

Applies only to DHCPv4 snooping.

Packet types that are
dropped

DHCPOFFER, DHCPACK,
DHCPNACK

Conditions for dropping the packets

n A packet from a DHCP server is received on an untrusted port.
n The switch is configured with a list of authorized DHCP server addresses

and a DHCP response received on a trusted port, but the source IP

address is not an authorized DHCP server.

DHCPRELEASE, DHCPDECLINE

n A broadcast packet that has a MAC address in the DHCP binding database,

but the port in the DHCP binding database does not match the port on

which the packet is received.

All DHCP packet types

n A DHCP packet received on an untrusted port in which the DHCP client

hardware MAC address does not match the source MAC address in the

packet.

n A DHCP packet containing DHCP relay information (option 82) is received

on an untrusted port.

Protocol details

1.

2.

3.

In a VSX setup, the configured VSX Primary switch writes IP binding entries to an external storage
file. If the VSX Primary switch reboots, the IP Binding entries will not be synced to the external
storage file until the VSX Primary switch comes back up. Once the VSX Primary switch comes up, it
will sync entries from the VSX secondary switch and write the consolidated bindings to external
storage.

In a VSX setup, external storage should be configured only after the VSX role is configured.

In a VSX setup, once external storage is configured, the VSX switch role should not be changed. If
there is a need to change the role, do so using these steps:
a. Remove DHCPv4-Snooping external storage.
b. Change the VSX role.
c. Configure DHCPv4-Snooping external storage

4. When a port is configured as a trusted port, all the dynamic IP binding entries learned on that

port will be deleted.

5. When a client is connected on a trusted port, the dynamic IP binding entries will not be learned

on the switch, even though the client gets an IP address.

6.

If DHCPv4 snooping is enabled on two back-to-back access switches, DHCP packets will be
dropped, Since by default option 82 is enabled on DHCPv4 snooping and the default policy is
drop. The second switch with DHCPv4 snooping enabled drops the packets. In this scenario the
user should enable DHCPv4 snooping option 82 on one switch, or else you can disable on both.

7. 8360 Switch Series: VXLAN is trusted by default for DHCPv4 and DHCPv6 snooping over VXLAN.

8. 8360 Switch Series: VXLAN operational status must be in the forward state to forward the packets

over VXLAN tunnel.

DHCP snooping | 131

Configuring DHCPv4 and v6 snooping over VXLAN overlay

Procedure

1. Configure VXLAN overlay setup to establish the VxLAN tunnel. For more information, see AOS-CX

VXLAN EVPN Guide.

2. Validate whether the tunnel is established between the VTEPS (either static or EVPN) with the

command show interface vxlan vteps.

The status of the tunnel should be operational in order to forward the packets.

3. Configure DHCPv4 and v6 snooping in the global and VLAN contexts with the commands dhcpv4-

snooping and dhcpv6-snooping.

4. Configure the server connected port as trusted with the commands dhcpv4-snooping trust and

dhcpv6-snooping trust.

If the server is connected through the VXLAN tunnel, then this step can be ignored. This is because
VXLAN is trusted by default for DHCPv4 and DHCPv6 snooping over VXLAN.

5. Validate the DHCPv4 and v6 snooping configuration with the commands show dhcpv4-snooping

and show dhcpv6-snooping.

DHCPv4 snooping commands

clear dhcpv4-snooping binding
clear dhcpv4-snooping binding {all | ip <IPV4-ADDR> vlan <VLAN-ID> | port <PORT-NUM> |
vlan <VLAN-ID>}

Description

Clears DHCPv4 snooping binding entries.

Parameter

all

Description

Specifies that all DHCPv4 binding information is to be cleared.

ip <IPV4-ADDR> vlan <VLAN-ID>

Specifies the IPv4 address and VLAN for which all DHCPv4 binding
information is to be cleared.

port <PORT-NUM>

vlan <VLAN-ID>

Examples

Specifies the port number for which all DHCPv4 binding
information is to be cleared.

Specifies the VLAN for which all DHCPv4 binding information is to
be cleared.

Clearing all DHCPv4 binding information for IP address 192.168.2.4 and VLAN 5:

switch(config)# clear dhcpv4-snooping binding ip 192.168.2.4 vlan 5

Clearing all DHCPv4 binding information for port 1/1/1:

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

132

| switch(config)# | clear | dhcpv4-snooping | binding port | 1/1/1 |
| --------------- | ----- | --------------- | ------------ | ----- |
ClearingallDHCPv4bindinginformationforVLAN10:
| switch(config)# | clear | dhcpv4-snooping | binding vlan | 10  |
| --------------- | ----- | --------------- | ------------ | --- |
ClearingallDHCPv4bindinginformation:
| switch(config)# | clear | dhcpv4-snooping | binding all                                     |     |
| --------------- | ----- | --------------- | ----------------------------------------------- | --- |
| Command History |       |                 |                                                 |     |
| Release         |       |                 | Modification                                    |     |
| 10.09.1000      |       |                 | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |       |                 | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| clear dhcpv4-snooping |     | statistics |     |     |
| --------------------- | --- | ---------- | --- | --- |
| clear dhcpv4-snooping |     | statistics |     |     |
Description
ClearsallDHCPv4snoopingstatistics.
Examples
ClearallDHCPv4snoopingstatistics:
switch#
| clear           | dhcpv4-snooping | statistics |                                                 |     |
| --------------- | --------------- | ---------- | ----------------------------------------------- | --- |
| Command History |                 |            |                                                 |     |
| Release         |                 |            | Modification                                    |     |
| 10.09.1000      |                 |            | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |                 |            | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
DHCPsnooping|133

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
dhcpv4-snooping
dhcpv4-snooping
no dhcpv4-snooping
Description
EnablesDHCPv4snooping.DHCPv4snoopingisdisabledbydefault.DHCPsnoopingisnotsupportedonthe
managementinterface.
ThenoformofthecommanddisablesDHCPv4snooping,flushingalltheIPbindingslearnedsinceDHCPv4
snoopingwasenabled.
Examples
EnablingDHCPv4snooping:
| switch(config)# | dhcpv4-snooping |     |     |
| --------------- | --------------- | --- | --- |
DisablingDHCPv4snooping:
| switch(config)# | no  | dhcpv4-snooping |                                                 |
| --------------- | --- | --------------- | ----------------------------------------------- |
| Command History |     |                 |                                                 |
| Release         |     |                 | Modification                                    |
| 10.09.1000      |     |                 | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |                 | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config
| 8360 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| dhcpv4-snooping |     | (in config-vlan | context) |
| --------------- | --- | --------------- | -------- |
dhcpv4-snooping
no dhcpv4-snooping
Description
EnablesDHCPv4snoopingforthespecifiedVLANintheconfig-vlancontext.DHCPv4snoopingis
disabledbydefaultforallVLANs.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 134

ThenoformofthecommanddisablesDHCPv4snoopingonthespecifiedVLAN,flushingalltheIP
bindingslearnedforthisVLANsinceDHCPv4snoopingwasenabledforthisVLAN.
Examples
EnablingDHCPv4snoopingonVLAN100:
| switch(config)#          | vlan | 100             |     |
| ------------------------ | ---- | --------------- | --- |
| switch(config-vlan-100)# |      | dhcpv4-snooping |     |
| switch(config-vlan-100)# |      | exit            |     |
switch(config)#
DisablingDHCPv4snoopingonVLAN100:
| switch(config)#          | vlan | 100                |     |
| ------------------------ | ---- | ------------------ | --- |
| switch(config-vlan-100)# |      | no dhcpv4-snooping |     |
| switch(config-vlan-100)# |      | exit               |     |
switch(config)#
| Command History |     |     |                                                 |
| --------------- | --- | --- | ----------------------------------------------- |
| Release         |     |     | Modification                                    |
| 10.09.1000      |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
config-vlan
| 8360 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| dhcpv4-snooping    |                         | allow-overwrite-binding |     |
| ------------------ | ----------------------- | ----------------------- | --- |
| dhcpv4-snooping    | allow-overwrite-binding |                         |     |
| no dhcpv4-snooping | allow-overwrite-binding |                         |     |
Description
AllowsbindingtobeoverwrittenforthesameIPaddress.Whenenabled,andaDHCPserveroffersa
hostanIPaddressthatisalreadyboundtoanexistinghostinthebindingtable,theexistingbindingis
overwrittenforthenewhostifthenewhostissuccessfullyabletoacquirethesameIPaddress.This
overwritingisdisabledbydefault,causingtheDHCPserverofferstobedropped.
ThenoformofthecommanddisablesDHCPv4snoopingoverwritebinding.
Examples
EnablingDHCPv4snoopingoverwritebinding:
| switch(config)# | dhcpv4-snooping |     | allow-overwrite-binding |
| --------------- | --------------- | --- | ----------------------- |
DHCPsnooping|135

DisablingDHCPv4snoopingoverwritebinding:
| switch(config)# | no  | dhcpv4-snooping | allow-overwrite-binding                         |     |
| --------------- | --- | --------------- | ----------------------------------------------- | --- |
| Command History |     |                 |                                                 |     |
| Release         |     |                 | Modification                                    |     |
| 10.09.1000      |     |                 | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |     |                 | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping |                   | authorized-server |             |                  |
| --------------- | ----------------- | ----------------- | ----------- | ---------------- |
| dhcpv4-snooping | authorized-server |                   | <IPV4-ADDR> | [vrf <VRF-NAME>] |
no dhcpv4-snooping authorized-server <IPV4-ADDR> [vrf <VRF-NAME>]
Description
Addsanauthorized(trusted)DHCPservertoalistofauthorizedserversforusebyDHCPv4snooping.
Thiscommandcanbeissuedmultipletimes,addingamaximumof20authorizedserversperVRF.By
default,withanemptylistofauthorizedservers,allDHCPserversareconsideredtobetrustedfor
DHCPv4snoopingpurposes.
ThemgmtVRFcannotbeusedwiththiscommand.
ThenoformofthiscommanddeletesthespecifiedDHCPserverfromtheauthorizedlist.
| Parameter      |     |     | Description                                      |     |
| -------------- | --- | --- | ------------------------------------------------ | --- |
| <IPV4-ADDR>    |     |     | SpecifiestheIPv4addressofthetrustedDHCPv4server. |     |
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.                             |     |
Usage
Forauthorizedserverlookup,theVRFisderivedfromtheSwitchVirtualInterface(SVI)configuredfor
theincomingVLAN.IftheSVIisnotconfigured,thedefaultVRFisassumed.
Examples
AddingDHCPservers192.168.2.2,192.168.2.3,and192.168.2.10totheauthorizedserverlist:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 136

| switch(config)# |     | dhcpv4-snooping |     | authorized-server |     | 192.168.2.2 |     |
| --------------- | --- | --------------- | --- | ----------------- | --- | ----------- | --- |
switch(config)#
|     |     | dhcpv4-snooping |     | authorized-server |     | 192.168.2.3 | vrf default |
| --- | --- | --------------- | --- | ----------------- | --- | ----------- | ----------- |
switch(config)# dhcpv4-snooping authorized-server 192.168.2.10 vrf default
RemovingDHCPserver192.168.2.3fromtheauthorizedserverlist:
switch(config)# no dhcpv4-snooping authorized-server 192.168.2.3 vrf default
| Command History |     |     |     |                                                 |     |     |     |
| --------------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
| Release         |     |     |     | Modification                                    |     |     |     |
| 10.09.1000      |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |     |
| 10.09           |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |
10.07orearlier
| Command Information |         |     |         |           |     |     |     |
| ------------------- | ------- | --- | ------- | --------- | --- | --- | --- |
| Platforms           | Command |     | context | Authority |     |     |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |           | event-log |        | client |     |     |     |
| ------------------ | --------- | --------- | ------ | ------ | --- | --- | --- |
| dhcpv4-snooping    | event-log |           | client |        |     |     |     |
| no dhcpv4-snooping |           | event-log | client |        |     |     |     |
Description
Thiscommandenables/disablesDHCPv4clientleveleventlogsthathelpwithclienttelemetryona
remotemanagementstationsuchasArubaCentral.Bydefault,clientleveleventlogsaredisabled.The
noformofthiscommanddisablesclient-leveleventlogsforDHCPv4snoopingaftertheyareenabled.
ViewtheseloggedDHCPv4snoopingeventsbyissuingthecommandshow events -c dhcpv4-
snooping.
Examples
EnablingDHCPv4clientleveleventlogs:
| switch(config)# |     | # dhcpv4-snooping |     | event-log | client |     |     |
| --------------- | --- | ----------------- | --- | --------- | ------ | --- | --- |
Disablingexternalstorage:
| witch(config)#  | #   | no dhcpv4-snooping |     | event-log | client |     |     |
| --------------- | --- | ------------------ | --- | --------- | ------ | --- | --- |
| Command History |     |                    |     |           |        |     |     |
DHCPsnooping|137

Release

10.10

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

8360

config

Administrators or local user group members with execution
rights for this command.

dhcpv4-snooping external-storage
dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
no dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>

Description

Configures external storage to be used for backing up IP bindings (used by DHCPv4 snooping) to a file.
When configured, the switch stores all the IP bindings in an external storage file so that they are
retained after the switch restarts. When the switch restarts, it reads the IP bindings from the configured
external storage file to populate its local cache.

When both external storage and flash storage are configured to store DHCP snooping IP bindings, the external

storage takes priority, and is used exclusively until it becomes unconfigured, at which time flash storage (if

configured) is used. Later, if external storage is configured again, flash storage stops and external storage

resumes.

The no form of this command disables the saving of IP bindings in an external storage file.

Parameter

Description

volume <VOL-NAME>

Specifies the name of the existing external storage volume where
the IP bindings file will be saved. Before running the dhcpv4-
snooping external-storage volume command, first create
the external storage volume using command external-storage

<VOLUME-NAME>. See External storage commands in the

Command-Line Interface Guide.

file <FILE-NAME>

Specifies the file name to use for storing IP bindings. Maximum
255 characters.

Configuring IP bindings storage in file dsnoop_ipbindings on existing volume dhcp_snoop:

switch(config)# dhcpv4-snooping external-storage volume dhcp_snoop file dsnoop_
ipbindings

Disabling external storage:

switch(config)# no dhcpv4-snooping external-storage volume dhcp_snoop

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

138

Disablingexternalstoragewhenflashstorageisalsoconfigured(notethemessageindicatingthatflash
storagewillbeused):
switch(config)# no dhcpv4-snooping external-storage volume dhcp_snoop
DHCPv4-Snooping will use flash storage to store IP Binding database
switch(config)#
| Command History |     |     |                                                 |
| --------------- | --- | --- | ----------------------------------------------- |
| Release         |     |     | Modification                                    |
| 10.09.1000      |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
| 10.08           |     |     | Updatedexamplewithflashstorageinformation.      |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |               | flash-storage |                 |
| ------------------ | ------------- | ------------- | --------------- |
| dhcpv4-snooping    | flash-storage |               | [delay <DELAY>] |
| no dhcpv4-snooping | flash-storage |               | [delay <DELAY>] |
Description
ConfiguresswitchflashstoragetobeusedforbackingupclientIPbindings(usedbyDHCPv4snooping).
Whenflashstorageisconfigured(andexternalstorageisnotalreadyconfiguredforthispurpose),the
switchstorestheIPbindingsinswitchflashstorage.Whentheswitchrestarts,itreadstheIPbindings
fromtheswitchflashstoragetopopulateitslocalcache.
WritingtheIPbindingstoflashstorageonlyoccursaftertheconfigureddelayandiftherehasbeena
changeinclientIPbindings.WritingisskippedwhenclientIPbindingshavenotchangedsincethe
previouswrite.
| Omittingdelay | <DELAY> setsthedefaultdelayof900seconds. |     |     |
| ------------- | ---------------------------------------- | --- | --- |
Toreduceswitchflashagingitisrecommendedthatyouuseexternalstorage(commanddhcpv4-snooping
external-storage)tobackupDHCPsnoopingIPbindings.Alternatively,considerconfiguringflashstoragewith
asubstantialdelaybetweenwrites.
WhenbothexternalstorageandflashstorageareconfiguredtostoreDHCPsnoopingIPbindings,theexternal
storagetakespriority,andisusedexclusivelyuntilitbecomesunconfigured,atwhichtimeflashstorage(if
configured)isused.Later,ifexternalstorageisconfiguredagain,flashstoragestopsandexternalstorage
resumes.
DHCPsnooping|139

ThenoformofthiscommanddisablesthesavingofIPbindingsinflashstorage.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
delay <DELAY> Specifiesthedelayinsecondsbetweenwrites(whennecessary)to
theflashstorage,Default:900.Range:300to86400.
Examples
ConfiguringswitchflashstorageforDHCPsnoopingIPbindingstoragewithawritedelayof1200
seconds:
| switch(config)# | dhcpv4-snooping |     |     | flash-storage | delay 1200 |
| --------------- | --------------- | --- | --- | ------------- | ---------- |
Warning: Using flash storage reduces switch lifetime. It is recommended to use an
external-storage.
| Do you want | to continue |     | (y/n)? | y   |     |
| ----------- | ----------- | --- | ------ | --- | --- |
switch(config)#
UnconfiguringusageofswitchflashstorageforIPbindings:
| switch(config)# | no  | dhcpv4-snooping |     | flash-storage                                   |     |
| --------------- | --- | --------------- | --- | ----------------------------------------------- | --- |
| Command History |     |                 |     |                                                 |     |
| Release         |     |                 |     | Modification                                    |     |
| 10.09.1000      |     |                 |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |     |                 |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.08
| Command Information |         |         |     |           |     |
| ------------------- | ------- | ------- | --- | --------- | --- |
| Platforms           | Command | context |     | Authority |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |              | max-bindings |                |     |     |
| ------------------ | ------------ | ------------ | -------------- | --- | --- |
| dhcpv4-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |
| no dhcpv4-snooping | max-bindings |              | <MAX-BINDINGS> |     |     |
Description
SetsthemaximumnumberofDHCPbindingsallowedontheselectedinterface.Forallinterfaceson
whichthiscommandisnotrun,thedefaultmaxbindingisthemaximumvalueoftherange.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 140

| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofDHCPbindings. Range:0to
2000.
Examples
SettheDHCPmaxbindingsto256oninterface1/1/1:
| switch(config)#    |     | interface       | 1/1/1 |     |              |     |     |
| ------------------ | --- | --------------- | ----- | --- | ------------ | --- | --- |
| switch(config-if)# |     | dhcpv4-snooping |       |     | max-bindings | 256 |     |
| switch(config-if)# |     | exit            |       |     |              |     |     |
switch(config)#
RevertDHCPmaxbindingstoitsdefaultoninterface1/1/1:
switch(config)#
|                    |     | interface          | 1/1/1 |     |              |     |     |
| ------------------ | --- | ------------------ | ----- | --- | ------------ | --- | --- |
| switch(config-if)# |     | no dhcpv4-snooping |       |     | max-bindings |     | 256 |
| switch(config-if)# |     | exit               |       |     |              |     |     |
switch(config)#
| Command History |     |     |     |                                                 |     |     |     |
| --------------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
| Release         |     |     |     | Modification                                    |     |     |     |
| 10.09.1000      |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |     |
| 10.09           |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |
10.07orearlier
| Command Information |         |         |     |           |     |     |     |
| ------------------- | ------- | ------- | --- | --------- | --- | --- | --- |
| Platforms           | Command | context |     | Authority |     |     |     |
8360 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping |     | option | 82  |     |     |     |     |
| --------------- | --- | ------ | --- | --- | --- | --- | --- |
dhcpv4-snooping option 82 [remote-id {mac | subnet-ip | mgmt-ip}]
|     |     |     | [untrusted-policy |     | {drop | | keep | | replace}] |
| --- | --- | --- | ----------------- | --- | ----- | ------ | ----------- |
no dhcpv4-snooping option 82 [remote-id {mac | subnet-ip | mgmt-ip}]
|     |     |     | [untrusted-policy |     | {drop | | keep | | replace}] |
| --- | --- | --- | ----------------- | --- | ----- | ------ | ----------- |
Description
Configurestheadditionofoption82DHCPrelayinformationtoDHCPclientpacketsthatarebeing
forwardedontrustedports.DHCPrelayisenabledbydefault.
Intheswitchdefaultstateandwhenthiscommandisenteredwithoutparameters(dhcpv4-snooping
option 82),thisdefaultconfigurationisused:
| dhcpv4-snooping | option | 82  | remote-id | mac | untrusted-policy |     | drop |
| --------------- | ------ | --- | --------- | --- | ---------------- | --- | ---- |
Whenremote-idisomitted,itsdefault(mac)isused.Whenuntrusted-policyisomitted,itsdefault
(drop)isused.
DHCPsnooping|141

The no form of this command disables DHCPv4 snooping option 82.

Parameter

remote-id

mac

subnet-ip

Description

Specifies what address to use as the remote ID for the replace
option of untrusted-policy. Specify one of these address
types:

The default. Uses the switch MAC address as the remote ID.

Uses the IP address of the client VLAN as the remote ID.

untrusted-policy

Specifies what action to take for DHCP packets (with option 82)
that are received on untrusted ports. Specify one of these actions:

drop

keep

replace

Examples

The default. Drop DHCP packets (with option 82) without
forwarding them.

Forward DHCP packets (with option 82).

Replace the option 82 information in the DHCP packets with
whatever is set for remote-id (one of: mac, subnet-ip, or mgmt-
ip) and forward the packets.

Configuring DHCPv4 snooping option 82 with the keep action:

switch(config)# dhcpv4-snooping option 82 untrusted-policy keep

Configuring DHCPv4 snooping option 82 with mgmt-ip as the remote-id and the replace action:

switch(config)# dhcpv4-snooping option 82 remote-id mgmt-ip untrusted-policy
replace

Disabling DHCPv4 snooping option 82:

switch(config)# no dhcpv4-snooping option 82 untrusted-policy keep

Command History

Release

10.09.1000

10.09

10.07 or earlier

Command Information

Modification

Command introduced for the 8360 Switch Series.

Command introduced for the 6000 and 6100 Switch Series.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

142

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |                   | static-attributes |     |
| ------------------ | ----------------- | ----------------- | --- |
| dhcpv4-snooping    | static-attributes |                   |     |
| no dhcpv4-snooping | static-attributes |                   |     |
Description
EnablesstorageofstaticattributesprovidedtotheDHCPclientbyDHCPserverduringDHCPpacket
exchange.Disabledbydefault.Whenenabled,thefollowingattributesarestoredinOVSDBalongwith
theclientIPbindingentry:
1. NameserverIPaddresses:DNSserverIPsprovidedbytheDHCPservertotheclient.Maximum:3
perclient.
2. DefaultgatewayIPaddress:RouterIPaddressesprovidedbyDHCPservertotheclient.
Maximum:3perclient.
3. ServerIPaddress:IPaddressoftheDHCPserverthatleasedtheIPtotheclient.
Thenoformofthecommanddisablesstoringofclientstaticattributes.Afterdisabling,existingclient
staticattributeswillbeflushed.
Examples
EnablingthestorageofDHCPv4snoopingstaticattributes:
| switch(config)# | dhcpv4-snooping |     | static-attributes |
| --------------- | --------------- | --- | ----------------- |
DisablingthestorageofDHCPv4snoopingstaticattributes:
| switch(config)#     | no      | dhcpv4-snooping | static-attributes  |
| ------------------- | ------- | --------------- | ------------------ |
| Command History     |         |                 |                    |
| Release             |         |                 | Modification       |
| 10.10               |         |                 | Commandintroduced. |
| Command Information |         |                 |                    |
| Platforms           | Command | context         | Authority          |
config
| 8360 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| dhcpv4-snooping    |       | trust |     |
| ------------------ | ----- | ----- | --- |
| dhcpv4-snooping    | trust |       |     |
| no dhcpv4-snooping | trust |       |     |
Description
DHCPsnooping|143

EnablesDHCPv4snoopingtrustontheselectedport.Onlyserverpacketsreceivedontrustedportsare
forwarded.Alltheportsareuntrustedbydefault.
ThenoformofthecommanddisablesDHCPv4snoopingtrustontheselectedport.
Examples
EnablingDHCPv4snoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface       | 2/2/1 |       |
| ------------------ | --- | --------------- | ----- | ----- |
| switch(config-if)# |     | dhcpv4-snooping |       | trust |
| switch(config-if)# |     | exit            |       |       |
switch(config)#
DisablingDHCPv4snoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface | 2/2/1           |       |
| ------------------ | --- | --------- | --------------- | ----- |
| switch(config-if)# |     | no        | dhcpv4-snooping | trust |
| switch(config-if)# |     | exit      |                 |       |
switch(config)#
| Command History |     |     |     |                                                 |
| --------------- | --- | --- | --- | ----------------------------------------------- |
| Release         |     |     |     | Modification                                    |
| 10.09.1000      |     |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |     |         |           |
| ------------------- | ------- | --- | ------- | --------- |
| Platforms           | Command |     | context | Authority |
8360 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |        | tunnel | vxlan       | trust |
| ------------------ | ------ | ------ | ----------- | ----- |
| dhcpv4-snooping    | tunnel | vxlan  | trust       |       |
| no dhcpv4-snooping |        | tunnel | vxlan trust |       |
Description
EnablesDHCPv4-snoopingtrustonallVxLANtunnels.
ThenoformofthecommandtomarksallVxLANtunnelsasuntrusted.
Bydefault,allVxLANtunnelinterfacesaretrusted.WhentrustisdisabledonVxLANtunnelinterfaces:
n DHCPbroadcastpacketsarenotforwardedonVxLANtunnels.
n DHCPserverpacketsreceivedonVxLANtunnelinterfacesarediscarded.
Examples
EnablingtrustonallVxLANtunnelinterfaces:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 144

| switch(config)# | dhcpv4-snooping |     | tunnel vxlan | trust |
| --------------- | --------------- | --- | ------------ | ----- |
DisablingtrustonallVxLANtunnelinterfaces:
| switch(config)#     | no      | dhcpv4-snooping | tunnel             | vxlan trust |
| ------------------- | ------- | --------------- | ------------------ | ----------- |
| Command History     |         |                 |                    |             |
| Release             |         |                 | Modification       |             |
| 10.10.1030          |         |                 | Commandintroduced. |             |
| Command Information |         |                 |                    |             |
| Platforms           | Command | context         | Authority          |             |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |        | verify mac |     |     |
| ------------------ | ------ | ---------- | --- | --- |
| dhcpv4-snooping    | verify | mac        |     |     |
| no dhcpv4-snooping | verify | mac        |     |     |
Description
ThiscommandenablesverificationofthehardwareaddressfieldinDHCPclientpackets.Whenenabled,
theDHCPclienthardwareaddressfieldandthesourceMACaddressmustbethesameforpackets
receivedonuntrustedportsorelsethepacketisdropped.ThisDHCPsnoopingMACverificationis
enabledbydefault.
ThenoformofthecommanddisablesDHCPv4snoopingMACverification.
Examples
EnablingDHCPv4snoopingMACverification:
| switch(config)# | dhcpv4-snooping |     | verify mac |     |
| --------------- | --------------- | --- | ---------- | --- |
DisablingDHCPv4snoopingMACverification:
| switch(config)# | no  | dhcpv4-snooping | verify                                          | mac |
| --------------- | --- | --------------- | ----------------------------------------------- | --- |
| Command History |     |                 |                                                 |     |
| Release         |     |                 | Modification                                    |     |
| 10.09.1000      |     |                 | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |     |                 | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
DHCPsnooping|145

| Command Information |         |     |         |     |           |     |     |     |
| ------------------- | ------- | --- | ------- | --- | --------- | --- | --- | --- |
| Platforms           | Command |     | context |     | Authority |     |     |     |
config
| 8360 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
rightsforthiscommand.
show dhcpv4-snooping
| show dhcpv4-snooping |     | [vsx-peer] |     |     |     |     |     |     |
| -------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Description
ShowstheDHCPv4snoopingconfiguration.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv4snoopingconfiguration:
| switch(config)# |                | show         | dhcpv4-snooping |                    |     |            |         |         |
| --------------- | -------------- | ------------ | --------------- | ------------------ | --- | ---------- | ------- | ------- |
| DHCPv4-Snooping |                | Information  |                 |                    |     |            |         |         |
| DHCPv4-Snooping |                |              |                 | : Yes              |     | Verify MAC | Address | : Yes   |
| Allow Overwrite |                | Binding      |                 | : No               |     | Enabled    | VLANs   | : 1-100 |
| IP Binding      | Disabled       |              | VLANs           | :                  |     |            |         |         |
| Static          | Attributes     |              | : Yes           |                    |     |            |         |         |
| Client          | Event          | Logs         | : No            |                    |     |            |         |         |
| Option 82       | Configurations |              |                 |                    |     |            |         |         |
| Untrusted       | Policy         |              | :               | replace            |     | Insertion  |         | : Yes   |
| Option          | 82 Remote-id   |              | :               | mac                |     |            |         |         |
| External        | Storage        | Information  |                 |                    |     |            |         |         |
| Volume          | Name           | : ipbinding  |                 |                    |     |            |         |         |
| File Name       | :              | ipv4Bindings |                 |                    |     |            |         |         |
| Inactive        | Since          | :            | 01:23:20        | 09/10/2021         |     |            |         |         |
| Error :         | File           | Write        | Failure         |                    |     |            |         |         |
| Flash Storage   |                | Information  |                 |                    |     |            |         |         |
| File Write      | Delay          | :            | 300 seconds     |                    |     |            |         |         |
| Active Storage  |                | : External   |                 |                    |     |            |         |         |
| Authorized      | Server         |              | Configurations  |                    |     |            |         |         |
| VRF             |                |              |                 | Authorized         |     | Servers    |         |         |
| ------------    |                |              |                 | ------------------ |     |            |         |         |
| default         |                |              |                 | 1.1.10.3           |     |            |         |         |
| default         |                |              |                 | 10.10.10.1         |     |            |         |         |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 146

| default          |       |          | 10.10.10.56                                     |          |
| ---------------- | ----- | -------- | ----------------------------------------------- | -------- |
| default          |       |          | 200.10.10.3                                     |          |
| green            |       |          | 1.1.10.3                                        |          |
| green            |       |          | 1.10.10.3                                       |          |
| green            |       |          | 10.10.100.3                                     |          |
| red              |       |          | 192.168.122.53                                  |          |
| red              |       |          | 192.168.122.121                                 |          |
| Port Information |       |          |                                                 |          |
|                  |       | Max      | Static                                          | Dynamic  |
| Port             | Trust | Bindings | Bindings                                        | Bindings |
| --------         | ----- | -------- | --------                                        | -------- |
| 1/1/2            | Yes   | 5000     | 50                                              | 0        |
| 1/1/3            | Yes   | 8192     | 0                                               | 0        |
| 1/1/5            | Yes   | 8192     | 0                                               | 22       |
| 1/1/16           | No    | 100      | 0                                               | 0        |
| 10/10/10         | No    | 8100     | 320                                             | 200      |
| lag120           | No    | 512      | 0                                               | 0        |
| Command History  |       |          |                                                 |          |
| Release          |       |          | Modification                                    |          |
| 10.09.1000       |       |          | Commandintroducedforthe8360SwitchSeries.        |          |
| 10.09            |       |          | Commandintroducedforthe6000and6100SwitchSeries. |          |
| 10.08            |       |          | Updatedexamplewithflashstorageinformation.      |          |
10.07orearlier
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show dhcpv4-snooping |     |         | binding            |     |
| -------------------- | --- | ------- | ------------------ | --- |
| show dhcpv4-snooping |     | binding | [vsx-peer][detail] |     |
Description
ShowstheDHCPv4snoopingbindingconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
detail ShowsdetailedinformationforactiveIPbindingsonthesystem.
DHCPsnooping|147

Examples
ShowingtheDHCPv4snoopingbindingconfiguration:
switch(config)#
|                   | show | dhcpv4-snooping |     | binding |           |           |
| ----------------- | ---- | --------------- | --- | ------- | --------- | --------- |
| MacAddress        |      | IP              |     | VLAN    | Interface | Time-Left |
| ----------------- |      | --------------- |     | ----    | --------- | --------- |
| aa:b1:c1:dd:ee:ff |      | 10.2.3.4        |     | 1       | 1/1/2     | 582       |
| aa:b2:c2:dd:ee:ff |      | 10.2.3.5        |     | 1       | 1/1/2     | 584       |
ShowingdetailedinformationforactiveIPbindings:
| switch(config)#    | show  | dhcpv4-snooping   |                     | binding | detail      |     |
| ------------------ | ----- | ----------------- | ------------------- | ------- | ----------- | --- |
| VLAN Id : 2,       | MAC : | 00:50:56:96:74:46 |                     |         |             |     |
| IP                 |       | Interface         | Time-Left           |         |             |     |
| ---------------    |       | ---------         | ------------------- |         |             |     |
| 100.1.2.100        |       | 1/1/23            | 194                 |         |             |     |
| Static Attributes: |       |                   |                     |         |             |     |
| Default Router     |       | : 100.1.2.1,      | 192.1.1.1,          |         | 1.1.1.2     |     |
| Server IP          |       | : 10.1.84.2       |                     |         |             |     |
| Name Servers       |       | : 192.1.1.2,      | 2.2.2.2,            |         | 1.1.1.1     |     |
| VLAN Id : 3,       | MAC : | 00:50:56:96:e5:8e |                     |         |             |     |
| IP                 |       | Interface         | Time-Left           |         |             |     |
| ---------------    |       | ---------         | ------------------- |         |             |     |
| 100.1.3.100        |       | 2/1/22            | 145                 |         |             |     |
| Static Attributes: |       |                   |                     |         |             |     |
| Default Router     |       | : 100.1.3.1,      | 192.1.1.1,          |         | 1.1.1.2     |     |
| Server IP          |       | : 10.1.84.2       |                     |         |             |     |
| Name Servers       |       | : 192.1.1.2,      | 2.2.2.2,            |         | 1.1.1.1     |     |
| VLAN Id : 3,       | MAC : | 00:11:01:00:00:03 |                     |         |             |     |
| IP                 |       | Interface         | Time-Left           |         |             |     |
| ---------------    |       | ---------         | ------------------- |         |             |     |
| 100.1.3.99         |       | 2/1/24            | 137                 |         |             |     |
| Static Attributes: |       |                   |                     |         |             |     |
| Default Router     |       | : 100.1.3.1,      | 192.1.1.1,          |         | 1.1.1.2     |     |
| Server IP          |       | : 10.1.84.2       |                     |         |             |     |
| Name Servers       |       | :192.168.0.1,     | 192.168.1.1,        |         | 192.168.2.1 |     |
Command History
| Release    |     |     |     | Modification                             |     |     |
| ---------- | --- | --- | --- | ---------------------------------------- | --- | --- |
| 10.10      |     |     |     | Detailparameteradded.                    |     |     |
| 10.09.1000 |     |     |     | Commandintroducedforthe8360SwitchSeries. |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 148

| Release |     |     |     |     | Modification                                    |     |     |     |
| ------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
| 10.09   |     |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |
10.07orearlier
| Command Information |         |         |     |     |                                                      |     |     |     |
| ------------------- | ------- | ------- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
| Platforms           | Command | context |     |     | Authority                                            |     |     |     |
| 8360                |         |         |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |     |
Operator(>)orManager
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv4-snooping |     |            | statistics |            |     |     |     |     |
| -------------------- | --- | ---------- | ---------- | ---------- | --- | --- | --- | --- |
| show dhcpv4-snooping |     | statistics |            | [vsx-peer] |     |     |     |     |
Description
ShowstheDHCPv4snoopingstatistics.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv4snoopingstatistics:
| switch(config)# |     | show dhcpv4-snooping |                               |                | statistics                                      |          |       |           |
| --------------- | --- | -------------------- | ----------------------------- | -------------- | ----------------------------------------------- | -------- | ----- | --------- |
| Packet-Type     |     | Action               | Reason                        |                |                                                 |          |       | Count     |
| -----------     |     | -------              | ----------------------------- |                |                                                 |          |       | --------- |
| server          |     | forward              | from trusted                  |                | port                                            |          |       | 5425      |
| client          |     | forward              | to trusted                    |                | port                                            |          |       | 3895      |
| server          |     | drop                 | received                      | on             | untrusted                                       |          | port  | 117       |
| server          |     | drop                 | unauthorized                  |                | server                                          |          |       | 214       |
| client          |     | drop                 | destination                   |                | on untrusted                                    |          | port  | 78        |
| client          |     | drop                 | untrusted                     | option         |                                                 | 82 field |       | 85        |
| client          |     | drop                 | bad DHCP                      | release        |                                                 | request  |       | 0         |
| client          |     | drop                 | failed                        | verify         | MAC                                             | check    |       | 5         |
| client          |     | drop                 | failed                        | on max-binding |                                                 |          | limit | 15        |
| Command History |     |                      |                               |                |                                                 |          |       |           |
| Release         |     |                      |                               |                | Modification                                    |          |       |           |
| 10.09.1000      |     |                      |                               |                | Commandintroducedforthe8360SwitchSeries.        |          |       |           |
| 10.09           |     |                      |                               |                | Commandintroducedforthe6000and6100SwitchSeries. |          |       |           |
10.07orearlier
DHCPsnooping|149

| Command   | Information |     |         |           |     |
| --------- | ----------- | --- | ------- | --------- | --- |
| Platforms | Command     |     | context | Authority |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| DHCPv6                | snooping |     | commands |     |     |
| --------------------- | -------- | --- | -------- | --- | --- |
| clear dhcpv6-snooping |          |     | binding  |     |     |
clear dhcpv6-snooping binding {all | ip <IPV6-ADDR> vlan <VLAN-ID> | interface <IFNAME> |
vlan <VLAN-ID>}
Description
ClearsDHCPv6snoopingbindingentries.
| Parameter |     |     |     | Description                                            |     |
| --------- | --- | --- | --- | ------------------------------------------------------ | --- |
| all       |     |     |     | SpecifiesthatallDHCPv6bindinginformationistobecleared. |     |
ip <IPV6-ADDR> vlan <VLAN-ID> SpecifiestheIPv6addressandVLANforwhichallDHCPv6binding
informationistobecleared.
interface <IFNAME> SpecifiestheinterfaceforwhichallDHCPv6bindinginformationis
tobecleared.
vlan <VLAN-ID> SpecifiestheVLANforwhichallDHCPv6bindinginformationisto
becleared.Range:1to4094.
Examples
ClearingallDHCPv6bindinginformationfor5000::1vlan1:
switch(config)# clear dhcpv6-snooping binding ip 5000::1 vlan 1
ClearingallDHCPv6bindinginformationforinterface1/1/10:
| switch(config)# |     | clear | dhcpv6-snooping | binding interface | 1/1/10 |
| --------------- | --- | ----- | --------------- | ----------------- | ------ |
ClearingallDHCPv6bindinginformationforVLAN10:
switch(config)#
|     |     | clear | dhcpv6-snooping | binding vlan | 10  |
| --- | --- | ----- | --------------- | ------------ | --- |
ClearingallDHCPv6bindinginformation:
| switch(config)# |         | clear | dhcpv6-snooping | binding all |     |
| --------------- | ------- | ----- | --------------- | ----------- | --- |
| Command         | History |       |                 |             |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 150

| Release    |     |     | Modification                                    |     |     |
| ---------- | --- | --- | ----------------------------------------------- | --- | --- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |
10.07orearlier
| Command Information |         |         |           |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Platforms           | Command | context | Authority |     |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| clear dhcpv6-snooping |     | guard-policy |     | statistics |     |
| --------------------- | --- | ------------ | --- | ---------- | --- |
clear dhcpv6-snooping guard-policy statistics [vlan <VLAN-ID> | interface <INTERFACE-
NAME>]
Description
ClearsallDHCPv6snoopingguardpolicystatisticsfromthespecifiedVLANorinterface.
| Parameter        |     |     | Description                      |     |     |
| ---------------- | --- | --- | -------------------------------- | --- | --- |
| <VLAN-ID>        |     |     | SpecifiestheVLANID.Range:1-4094. |     |     |
| <INTERFACE-NAME> |     |     | Specifiestheinterfacename.       |     |     |
Examples
ClearingallDHCPv6snoopingguardpolicystatisticsfromVLAN100:
| switch# clear | dhcpv6-snooping | guard-policy |     | statistics | vlan 100 |
| ------------- | --------------- | ------------ | --- | ---------- | -------- |
ClearingallDHCPv6snoopingguardpolicystatisticsfrominterface1/1/10:
switch# clear dhcpv6-snooping guard-policy statistics interface 1/1/10
| Command History     |     |     |                    |     |     |
| ------------------- | --- | --- | ------------------ | --- | --- |
| Release             |     |     | Modification       |     |     |
| 10.10               |     |     | Commandintroduced. |     |     |
| Command Information |     |     |                    |     |     |
DHCPsnooping|151

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| clear dhcpv6-snooping |     | statistics |     |
| --------------------- | --- | ---------- | --- |
| clear dhcpv6-snooping |     | statistics |     |
Description
ClearsallDHCPv6snoopingstatistics.
Examples
ClearallDHCPv6snoopingstatistics:
| switch# clear   | dhcpv6-snooping | statistics |                                                 |
| --------------- | --------------- | ---------- | ----------------------------------------------- |
| Command History |                 |            |                                                 |
| Release         |                 |            | Modification                                    |
| 10.09.1000      |                 |            | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |                 |            | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
dhcpv6-snooping
dhcpv6-snooping
no dhcpv6-snooping
Description
EnablesDHCPv6snooping.DHCPv6snoopingisdisabledbydefault.DHCPv6snoopingisnotsupported
onthemanagementinterface.
ThenoformofthecommanddisablesDHCPv6snooping,flushingalltheIPbindingslearnedsince
DHCPv6snoopingwasenabled.
Examples
EnablingDHCPv6snooping:
| switch(config)# | dhcpv6-snooping |     |     |
| --------------- | --------------- | --- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 152

DisablingDHCPv6snooping:
| switch(config)# | no  | dhcpv6-snooping |                                                 |
| --------------- | --- | --------------- | ----------------------------------------------- |
| Command History |     |                 |                                                 |
| Release         |     |                 | Modification                                    |
| 10.09.1000      |     |                 | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |                 | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping |     | (in config-vlan | context) |
| --------------- | --- | --------------- | -------- |
dhcpv6-snooping
no dhcpv6-snooping
Description
EnablesDHCPv6snoopingintheconfig-vlancontext.DHCPv6snoopingisdisabledbydefaultforall
VLANs.
ThenoformofthecommanddisablesDHCPv6snoopingonthespecifiedVLAN,flushingalltheIPv6
bindingslearnedforthisVLANsinceDHCPv6snoopingwasenabledforthisVLAN.
Examples
EnablingDHCPv6snoopingonVLAN100:
| switch(config)#          | vlan | 100             |     |
| ------------------------ | ---- | --------------- | --- |
| switch(config-vlan-100)# |      | dhcpv6-snooping |     |
| switch(config-vlan-100)# |      | exit            |     |
switch(config)#
DisablingDHCPv6snoopingonVLAN100:
| switch(config)#          | vlan | 100                |     |
| ------------------------ | ---- | ------------------ | --- |
| switch(config-vlan-100)# |      | no dhcpv6-snooping |     |
| switch(config-vlan-100)# |      | exit               |     |
switch(config)#
| Command History |     |     |     |
| --------------- | --- | --- | --- |
DHCPsnooping|153

| Release    |     |     | Modification                                    |
| ---------- | --- | --- | ----------------------------------------------- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
8360 config-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping |                   | authorized-server |                              |
| --------------- | ----------------- | ----------------- | ---------------------------- |
| dhcpv6-snooping | authorized-server |                   | <IPV6-ADDR> [vrf <VRF-NAME>] |
no dhcpv6-snooping authorized-server <IPV6-ADDR> [vrf <VRF-NAME>]
Description
Addsanauthorized(trusted)DHCPv6servertoalistofauthorizedserversforusebyDHCPv6snooping.
Thiscommandcanbeissuedmultipletimes,addingamaximumof20authorizedserversperVRF.By
default,withanemptylistofauthorizedservers,allDHCPv6serversareconsideredtobetrustedfor
DHCPv6snoopingpurposes.
ThemgmtVRFcannotbeusedwiththiscommand.
ConfigurethelinklocalIPv6addressinsteadofglobalIPv6addressoftheDHCPv6serverastheauthorized-
server.Forexample:
switch(config)# dhcpv6-snooping authorized-server fe80::2ca4:fa40:d4cd:bc2f
ThenoformofthiscommanddeletesthespecifiedDHCPv6serverfromtheauthorizedlist.
| Parameter      |     |     | Description                                      |
| -------------- | --- | --- | ------------------------------------------------ |
| <IPV6-ADDR>    |     |     | SpecifiestheIPv6addressofthetrustedDHCPv6server. |
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.                             |
Usage
Forauthorizedserverlookup,theVRFisderivedfromtheSwitchVirtualInterface(SVI)configuredfor
theincomingVLAN.IftheSVIisnotconfigured,thedefaultVRFisassumed.
Examples
AddingDHCPserversABCD:5ACD::2000,andABCD:5ACD::2010totheauthorizedserverlist:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 154

switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
switch(config)#
|     |     | dhcpv6-snooping |     | authorized-server |     | ABCD:5ACD::2010 | vrf default |
| --- | --- | --------------- | --- | ----------------- | --- | --------------- | ----------- |
RemovingDHCPserverABCD:5ACD::2000fromtheauthorizedserverlist:
switch(config)# no dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
| Command History     |         |     |         |                                          |     |     |     |
| ------------------- | ------- | --- | ------- | ---------------------------------------- | --- | --- | --- |
| Release             |         |     |         | Modification                             |     |     |     |
| 10.09.1000          |         |     |         | Commandintroducedforthe8360SwitchSeries. |     |     |     |
| Command Information |         |     |         |                                          |     |     |     |
| Platforms           | Command |     | context | Authority                                |     |     |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping    |           | event-log |        | client |     |     |     |
| ------------------ | --------- | --------- | ------ | ------ | --- | --- | --- |
| dhcpv6-snooping    | event-log |           | client |        |     |     |     |
| no dhcpv6-snooping |           | event-log | client |        |     |     |     |
Description
Thiscommandenables/disablesDHCPv6clientleveleventlogsthathelpwithclienttelemetryona
remotemanagementstationsuchasArubaCentral.Bydefault,clientleveleventlogsaredisabled.The
noformofthiscommanddisablesclient-leveleventlogsforDHCPv6snoopingaftertheyareenabled.
ViewtheseloggedDHCPv6snoopingeventsbyissuingthecommandshow events -c dhcpv6-
snooping.
Examples
EnablingDHCPv6clientleveleventlogs:
| switch(config)# |     | # dhcpv6-snooping |     | event-log | client |     |     |
| --------------- | --- | ----------------- | --- | --------- | ------ | --- | --- |
Disablingexternalstorage:
| witch(config)#      | #   | no dhcpv6-snooping |     | event-log          | client |     |     |
| ------------------- | --- | ------------------ | --- | ------------------ | ------ | --- | --- |
| Command History     |     |                    |     |                    |        |     |     |
| Release             |     |                    |     | Modification       |        |     |     |
| 10.10               |     |                    |     | Commandintroduced. |        |     |     |
| Command Information |     |                    |     |                    |        |     |     |
DHCPsnooping|155

Platforms

Command context

Authority

8360

config

Administrators or local user group members with execution
rights for this command.

dhcpv6-snooping external-storage
dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
no dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>

Description

Configures external storage to be used for backing up IPv6 bindings (used by DHCPv6 snooping) to a
file. When configured, the switch stores all the IP bindings in an external storage file so that they are
retained after the switch restarts. When the switch restarts, it reads the IPv6 bindings from the
configured external storage file to populate its local cache.

When both external storage and flash storage are configured to store DHCP snooping IP bindings, the external

storage takes priority, and is used exclusively until it becomes unconfigured, at which time flash storage (if

configured) is used. Later, if external storage is configured again, flash storage stops and external storage
resumes.

The no form of this command disables the saving of IPv6 bindings in an external storage file.

Parameter

Description

volume <VOL-NAME>

Specifies the name of the existing external storage volume where
the IPv6 bindings file will be saved. Before running the dhcpv6-
snooping external-storage volume command, first create
the external storage volume using command external-storage
<VOLUME-NAME>. See External storage commands in the Command-
Line Interface Guide.

file <FILE-NAME>

Specifies the file name to use for storing IPv6 bindings. Maximum
255 characters.

Examples

Configuring IPv6 bindings storage in file ipv6Bindings on existing volume dhcp_snoop:

switch(config)# dhcpv6-snooping external-storage volume dhcp_snoop file
ipv6Bindings

Disabling external storage:

switch(config)# no dhcpv6-snooping external-storage volume dhcp_snoop

Disabling external storage when flash storage is also configured (note the message indicating that flash
storage will be used):

switch(config)#
DHCPv6-Snooping will use flash storage to store IP Binding database

no dhcpv6-snooping external-storage volume dhcp_snoop

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

156

switch(config)#
| Command History     |         |         |                                            |
| ------------------- | ------- | ------- | ------------------------------------------ |
| Release             |         |         | Modification                               |
| 10.08               |         |         | Updatedexamplewithflashstorageinformation. |
| 10.07orearlier      |         |         | Commandintroduced                          |
| Command Information |         |         |                                            |
| Platforms           | Command | context | Authority                                  |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping    |               | flash-storage |                 |
| ------------------ | ------------- | ------------- | --------------- |
| dhcpv6-snooping    | flash-storage |               | [delay <DELAY>] |
| no dhcpv6-snooping | flash-storage |               | [delay <DELAY>] |
Description
ConfiguresswitchflashstoragetobeusedforbackingupclientIPbindings(usedbyDHCPv6snooping).
Whenflashstorageisconfigured(andexternalstorageisnotalreadyconfiguredforthispurpose),the
switchstorestheIPbindingsinswitchflashstorage.Whentheswitchrestarts,itreadstheIPbindings
fromtheswitchflashstoragetopopulateitslocalcache.
WritingtheIPbindingstoflashstorageonlyoccursaftertheconfigureddelayandiftherehasbeena
changeinclientIPbindings.WritingisskippedwhenclientIPbindingshavenotchangedsincethe
previouswrite.
| Omittingdelay | <DELAY> setsthedefaultdelayof900seconds. |     |     |
| ------------- | ---------------------------------------- | --- | --- |
Toreduceswitchflashagingitisrecommendedthatyouuseexternalstorage(commanddhcpv6-snooping
external-storage)tobackupDHCPsnoopingIPbindings.Alternatively,considerconfiguringflashstoragewith
asubstantialdelaybetweenwrites.
WhenbothexternalstorageandflashstorageareconfiguredtostoreDHCPsnoopingIPbindings,theexternal
storagetakespriority,andisusedexclusivelyuntilitbecomesunconfigured,atwhichtimeflashstorage(if
configured)isused.Later,ifexternalstorageisconfiguredagain,flashstoragestopsandexternalstorage
resumes.
ThenoformofthiscommanddisablesthesavingofIPbindingsinflashstorage.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
delay <DELAY> Specifiesthedelayinsecondsbetweenwrites(whennecessary)to
theflashstorage,Default:900.Range:300to86400.
DHCPsnooping|157

Examples
ConfiguringswitchflashstorageforDHCPsnoopingIPbindingstoragewithawritedelayof1200
seconds:
| switch(config)# |     | dhcpv6-snooping |     | flash-storage | delay 1200 |
| --------------- | --- | --------------- | --- | ------------- | ---------- |
Warning: Using flash storage reduces switch lifetime. It is recommended to use an
external-storage.
| Do you want | to continue |     | (y/n)? |     |     |
| ----------- | ----------- | --- | ------ | --- | --- |
y
switch(config)#
UnconfiguringusageofswitchflashstorageforIPbindings:
| switch(config)# |     | no dhcpv6-snooping |     | flash-storage |                                   |
| --------------- | --- | ------------------ | --- | ------------- | --------------------------------- |
| Command History |     |                    |     |               |                                   |
| Release         |     |                    |     |               | Modification                      |
| 10.09.1000      |     |                    |     |               | Commandintroducedforthe8360Switch |
Series.
| Command Information |         |     |         |           |     |
| ------------------- | ------- | --- | ------- | --------- | --- |
| Platforms           | Command |     | context | Authority |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping    |              | max-bindings |                |                |     |
| ------------------ | ------------ | ------------ | -------------- | -------------- | --- |
| dhcpv6-snooping    | max-bindings |              | <MAX-BINDINGS> |                |     |
| no dhcpv6-snooping |              | max-bindings |                | <MAX-BINDINGS> |     |
Description
SetsthemaximumnumberofDHCPv6bindingsallowedontheselectedinterface.Forallinterfaceson
whichthiscommandisnotrun,thedefaultmaxbindingisthemaximumvalueoftherange.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofDHCPbindings. Range:0to
2000.
Examples
SettheDHCPv6maxbindingsto256oninterface1/1/1:
| switch(config)#    |     | interface       | 1/1/1 |              |     |
| ------------------ | --- | --------------- | ----- | ------------ | --- |
| switch(config-if)# |     | dhcpv6-snooping |       | max-bindings | 256 |
| switch(config-if)# |     | exit            |       |              |     |
switch(config)#
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 158

RevertDHCPv6maxbindingstoitsdefaultoninterface1/1/1:
| switch(config)#    | interface | 1/1/1              |              |     |
| ------------------ | --------- | ------------------ | ------------ | --- |
| switch(config-if)# |           | no dhcpv6-snooping | max-bindings | 256 |
| switch(config-if)# |           | exit               |              |     |
switch(config)#
| Command History     |         |         |                                          |     |
| ------------------- | ------- | ------- | ---------------------------------------- | --- |
| Release             |         |         | Modification                             |     |
| 10.09.1000          |         |         | Commandintroducedforthe8360SwitchSeries. |     |
| Command Information |         |         |                                          |     |
| Platforms           | Command | context | Authority                                |     |
8360 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping    |       | trust |     |     |
| ------------------ | ----- | ----- | --- | --- |
| dhcpv6-snooping    | trust |       |     |     |
| no dhcpv6-snooping | trust |       |     |     |
Description
EnablesDHCPv6snoopingtrustontheselectedinterface.Onlyserverpacketsreceivedontrusted
interfacesareforwarded.Alltheinterfacesareuntrustedbydefault.
ThenoformofthecommanddisablesDHCPv6snoopingtrustontheselectedinterface.
config-if
Examples
EnablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    | interface | 2/2/1           |       |     |
| ------------------ | --------- | --------------- | ----- | --- |
| switch(config-if)# |           | dhcpv6-snooping | trust |     |
| switch(config-if)# |           | exit            |       |     |
switch(config)#
DisablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    | interface | 2/2/1              |       |     |
| ------------------ | --------- | ------------------ | ----- | --- |
| switch(config-if)# |           | no dhcpv6-snooping | trust |     |
| switch(config-if)# |           | exit               |       |     |
switch(config)#
| Command History |     |     |                                          |     |
| --------------- | --- | --- | ---------------------------------------- | --- |
| Release         |     |     | Modification                             |     |
| 10.09.1000      |     |     | Commandintroducedforthe8360SwitchSeries. |     |
DHCPsnooping|159

| Command   | Information |         |         |     |           |     |
| --------- | ----------- | ------- | ------- | --- | --------- | --- |
| Platforms |             | Command | context |     | Authority |     |
config
| 8360 |     |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| dhcpv6-snooping    |     |        | tunnel | vxlan | trust |     |
| ------------------ | --- | ------ | ------ | ----- | ----- | --- |
| dhcpv6-snooping    |     | tunnel | vxlan  | trust |       |     |
| no dhcpv4-snooping |     | tunnel | vxlan  | trust |       |     |
Description
EnablesDHCPv6-snoopingtrustonallVxLANtunnels.
ThenoformofthecommandtomarksallVxLANtunnelsasuntrusted.
Bydefault,allVxLANtunnelinterfacesaretrusted.WhentrustisdisabledonVxLANtunnelinterfaces:
n DHCPbroadcastpacketsarenotforwardedonVxLANtunnels.
DHCPserverpacketsreceivedonVxLANtunnelinterfacesarediscarded.
n
Examples
EnablingtrustonallVxLANtunnelinterfaces:
| switch(config)# |     | dhcpv6-snooping |     |     | tunnel vxlan | trust |
| --------------- | --- | --------------- | --- | --- | ------------ | ----- |
DisablingtrustonallVxLANtunnelinterfaces:
| switch(config)# |             | no      | dhcpv6-snooping |     | tunnel             | vxlan trust |
| --------------- | ----------- | ------- | --------------- | --- | ------------------ | ----------- |
| Command         | History     |         |                 |     |                    |             |
| Release         |             |         |                 |     | Modification       |             |
| 10.10.1030      |             |         |                 |     | Commandintroduced. |             |
| Command         | Information |         |                 |     |                    |             |
| Platforms       |             | Command | context         |     | Authority          |             |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| match server    |             | access-list |            |     |     |     |
| --------------- | ----------- | ----------- | ---------- | --- | --- | --- |
| match server    | access-list |             | <ACL-NAME> |     |     |     |
| no match server |             | access-list | <ACL-NAME> |     |     |     |
Description
ConfiguresanaccesslisttoaDHCPv6snoopingguardpolicy,enablingtheDHCPv6snoopingguard
policytoallowordenythespecificDHCPservertoassignanIPv6address.Ifnofiltersareapplied,DHCP
servertrafficfromanysourceIPaddressisallowedinthetrustedport.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 160

ThenoformofthecommandremovesthespecifiedaccesslistfromtheDHCPv6snoopingguardpolicy.
| Parameter  |     |     | Description                                     |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
| <ACL-NAME> |     |     | SpecifiesthenameoftheIPv6accesslisttobematched. |     |
Examples
Creatinganaccess-listacl1onDHCPv6snoopingguardpolicypol1:
| switch(config)# | dhcpv6-snooping |     | guard-policy | pol1 |
| --------------- | --------------- | --- | ------------ | ---- |
switch(config-dhcpv6-guard-policy)# match server access-list acl1
Deletingtheaccesslistacl1fromtheDHCPv6snoopingguardpolicypol1:
| switch(config)# | dhcpv6-snooping |     | guard-policy | pol1 |
| --------------- | --------------- | --- | ------------ | ---- |
switch(config-dhcpv6-guard-policy)# no match server access-list acl1
| Command   | History     |         |                    |           |
| --------- | ----------- | ------- | ------------------ | --------- |
| Release   |             |         | Modification       |           |
| 10.10     |             |         | Commandintroduced. |           |
| Command   | Information |         |                    |           |
| Platforms | Command     | context |                    | Authority |
8360 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| match client    | prefix-list |                    |     |     |
| --------------- | ----------- | ------------------ | --- | --- |
| match client    | prefix-list | <PREFIX-LIST-NAME> |     |     |
| no match client | prefix-list | <PREFIX-LIST-NAME> |     |     |
Description
Configuresaprefix-listfortheDHCPv6snoopingguardpolicyenablingthepolicytoallowtheassigned
IPv6addresseswithinaspecificprefixrange.
ThenoformofthecommandremovesaprefixlistfromtheDHCPv6snoopingguardpolicy.
| Parameter          |     |     | Description                          |     |
| ------------------ | --- | --- | ------------------------------------ | --- |
| <PREFIX-LIST-NAME> |     |     | SpecifiesthenameoftheIPv6prefixlist. |     |
Examples
Addingaprefixlistnamedpref1tothepol1DHCPv6snoopingguardpolicy:
DHCPsnooping|161

switch(config)# ipv6 prefix-list pref1 permit 2001:db8::/64 le 128
switch(config)#
|                                     |     | dhcpv6-snooping |     |     | guard-policy | pol1        |             |
| ----------------------------------- | --- | --------------- | --- | --- | ------------ | ----------- | ----------- |
| switch(config-dhcpv6-guard-policy)# |     |                 |     |     | match        | client      | prefix-list |
| <ipv6-prefix-list-name>             |     |                 |     |     | IPv6         | prefix-list | name        |
switch(config-dhcpv6-guard-policy)# match client prefix-list pref1
Deletingtheprefixlistnamedprf1fromthepol1DHCPv6snoopingguardpolicy:
| switch(config)# |     | dhcpv6-snooping |     |     | guard-policy | pol1 |     |
| --------------- | --- | --------------- | --- | --- | ------------ | ---- | --- |
switch(config-dhcpv6-guard-policy)# no match client prefix-list <ipv6-prefix-list-
name>
| Command   | History     |     |         |     |                    |           |     |
| --------- | ----------- | --- | ------- | --- | ------------------ | --------- | --- |
| Release   |             |     |         |     | Modification       |           |     |
| 10.10     |             |     |         |     | Commandintroduced. |           |     |
| Command   | Information |     |         |     |                    |           |     |
| Platforms | Command     |     | context |     |                    | Authority |     |
8360 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
preference
| preference | [minimum | |   | maximum | ] <VALUE> |     |     |     |
| ---------- | -------- | --- | ------- | --------- | --- | --- | --- |
no preference
Description
EnablesaDHCPv6snoopingguardpolicytoallowordenytheDHCPv6serversinthespecifiedserver
preferencerange.Ifnotconfiguredtheminimumpreferenceissetto0andmaximumpreferenceisset
to255.
ThenoformofthecommandremovestheserverpreferencelimitsonthespecifiedDHCPv6snooping
guardpolicy.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
minimum <VALUE> Specifiestheminimumvaluefortheserverpreferencerange.
Range:1-255.
maximum <VALUE> Specifiesthemaximumvaluefortheserverpreferencerange.
Range:1-255.
Examples
Settingtheminimumandmaximumserverpreferencerangeto6-250onDHCPv6snoopingguardpolicy
pol1:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 162

| switch(config)# | dhcpv6-snooping |     | guard-policy |     | pol1 |     |
| --------------- | --------------- | --- | ------------ | --- | ---- | --- |
switch(config-dhcpv6-guard-policy)#
|                                     |     |     |     | preference |     | min 6   |
| ----------------------------------- | --- | --- | --- | ---------- | --- | ------- |
| switch(config-dhcpv6-guard-policy)# |     |     |     | preference |     | max 250 |
DisablingtheserverpreferencerangeonDHCPv6snoopingguardpolicypol1:
| switch(config)#                     | dhcpv6-snooping |         | guard-policy       |               | pol1      |     |
| ----------------------------------- | --------------- | ------- | ------------------ | ------------- | --------- | --- |
| switch(config-dhcpv6-guard-policy)# |                 |         |                    | no preference |           |     |
| Command History                     |                 |         |                    |               |           |     |
| Release                             |                 |         | Modification       |               |           |     |
| 10.10                               |                 |         | Commandintroduced. |               |           |     |
| Command Information                 |                 |         |                    |               |           |     |
| Platforms                           | Command         | context |                    |               | Authority |     |
config-dhcpv6-guard-policy
| 8360 |     |     |     |     | Administratorsorlocalusergroupmemberswith |     |
| ---- | --- | --- | --- | --- | ----------------------------------------- | --- |
executionrightsforthiscommand.
show dhcpv6-snooping
| show dhcpv6-snooping | [vsx-peer] |     |     |     |     |     |
| -------------------- | ---------- | --- | --- | --- | --- | --- |
Description
ShowstheDHCPv6snoopingconfiguration.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv6snoopingconfiguration:
| switch(config)# | show                | dhcpv6-snooping |            |          |     |                 |
| --------------- | ------------------- | --------------- | ---------- | -------- | --- | --------------- |
| DHCPv6-Snooping | Information         |                 |            |          |     |                 |
| DHCPv6-Snooping |                     | : Yes           | Enabled    | VLANs    |     | : 1,5,7,100-110 |
| External        | Storage Information |                 |            |          |     |                 |
| Volume          | Name                | : dhcp_snoop    |            |          |     |                 |
| File Name       |                     | : ip_binding    |            |          |     |                 |
| Inactive        | Since               | : 01:23:20      | 09/10/2021 |          |     |                 |
| Error           |                     | : Failed        | to write   | external |     | storage         |
DHCPsnooping|163

| Flash Storage       | Information |                |          |                                            |                                         |         |
| ------------------- | ----------- | -------------- | -------- | ------------------------------------------ | --------------------------------------- | ------- |
| File Write          | Delay       | : 300          | seconds  |                                            |                                         |         |
| Active Storage      |             | : External     |          |                                            |                                         |         |
| Authorized          | Server      | Configurations |          |                                            |                                         |         |
| VRF                 |             |                |          |                                            | Authorized                              | Servers |
| ------------        |             |                |          |                                            | ------------------                      |         |
| default             |             |                |          |                                            | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |         |
| default             |             |                |          |                                            | 2002::2                                 |         |
| default             |             |                |          |                                            | 2004::1                                 |         |
| red                 |             |                |          |                                            | 2002::1                                 |         |
| red                 |             |                |          |                                            | 2002::2                                 |         |
| red                 |             |                |          |                                            | 2002::9                                 |         |
| green               |             |                |          |                                            | 5000::1                                 |         |
| green               |             |                |          |                                            | 5000::2                                 |         |
| green               |             |                |          |                                            | 5000::3                                 |         |
| green               |             |                |          |                                            | 5000::7                                 |         |
| green               |             |                |          |                                            | 5000::8                                 |         |
| Port Information    |             |                |          |                                            |                                         |         |
|                     |             | Max            | Static   |                                            | Dynamic                                 |         |
| Port                | Trust       | Bindings       | Bindings |                                            | Bindings                                |         |
| --------            | -----       | --------       | -------- |                                            | --------                                |         |
| 1/1/2               | Yes         | 0              | 0        |                                            | 0                                       |         |
| 1/1/3               | Yes         | 0              | 3        |                                            | 0                                       |         |
| 1/1/5               | Yes         | 0              | 22       |                                            | 0                                       |         |
| 1/1/16              | No          | 256            | 0        |                                            | 20                                      |         |
| 10/10/10            | No          | 256            | 12       |                                            | 7                                       |         |
| lag120              | No          | 256            | 3        |                                            | 0                                       |         |
| Command History     |             |                |          |                                            |                                         |         |
| Release             |             |                |          | Modification                               |                                         |         |
| 10.08               |             |                |          | Updatedexamplewithflashstorageinformation. |                                         |         |
| 10.07orearlier      |             |                |          | Commandintroduced                          |                                         |         |
| Command Information |             |                |          |                                            |                                         |         |
| Platforms           | Command     |                | context  | Authority                                  |                                         |         |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |         | binding    |     |     |     |
| -------------------- | --- | ------- | ---------- | --- | --- | --- |
| show dhcpv6-snooping |     | binding | [vsx-peer] |     |     |     |
Description
ShowstheDHCPv6snoopingbindingconfiguration.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 164

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv6snoopingbindingconfiguration:
| switch# show | dhcpv6-snooping |     | binding |     |     |
| ------------ | --------------- | --- | ------- | --- | --- |
| IP Binding   | Information     |     |         |     |     |
======================
| MAC-ADDRESS |     | IPV6-ADDRESS |     |     | VLAN INTERFACE |
| ----------- | --- | ------------ | --- | --- | -------------- |
TIME-LEFT
---------------- ---------------------------------------- ---- --------- ----
------
00:50:56:96:e4:cf aaaa:bbbb:cccc:dddd:eeee:1234:5678:abcd 1 1/1/1
584
| 00:50:56:96:04:4d |     | 1000::3 |     |     | 134 1/1/2 |
| ----------------- | --- | ------- | --- | --- | --------- |
435
| 00:50:56:96:d8:3d |     | 2000:1000::4 |     |     | 2002 lag123 |
| ----------------- | --- | ------------ | --- | --- | ----------- |
21234
| Command History |     |     |     |                                                 |     |
| --------------- | --- | --- | --- | ----------------------------------------------- | --- |
| Release         |     |     |     | Modification                                    |     |
| 10.09.1000      |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
| Command Information |         |     |         |           |     |
| ------------------- | ------- | --- | ------- | --------- | --- |
| Platforms           | Command |     | context | Authority |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| dhcpv6-snooping    |              | guard-policy |               |     |     |
| ------------------ | ------------ | ------------ | ------------- | --- | --- |
| dhcpv6-snooping    | guard-policy |              | <POLICY-NAME> |     |     |
| no dhcpv6-snooping |              | guard-policy | <POLICY-NAME> |     |     |
Description
ConfiguresaDHCPv6snoopingguardpolicywiththegivennameandenterstheguardpolicy
configurationcontext.
Thenoformofthecommanddisablesthespecifiedguardpolicy.
DHCPsnooping|165

| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<POLICY-NAME> SpecifiesthenameoftheDHCPv6snoopingguardpolicy.
Maximumlength:64.
Examples
CreatingtheDHCPv6snoopingguardpolicynamepol1:
| switch(config)# |     | dhcpv6-snooping |     | guard-policy |     | pol1 |     |
| --------------- | --- | --------------- | --- | ------------ | --- | ---- | --- |
switch(config-guard-policy-pol1)#
DeletingtheDHCPv6snoopingguardpolicynamedpol1:
| switch(config)# |     | no dhcpv6-snooping |     | guard-policy |     | pol1 |     |
| --------------- | --- | ------------------ | --- | ------------ | --- | ---- | --- |
CreatingtheDHCPv6snoopingguardpolicynamepol1oninterface1/1/1:
TheDHCPv6snoopingguardpolicyappliedontheporttakespriorityoverthepolicyappliedoverVLAN.
| switch(config)#    |     | interface       | 1/1/1 |              |     |      |     |
| ------------------ | --- | --------------- | ----- | ------------ | --- | ---- | --- |
| switch(config-if)# |     | dhcpv6-snooping |       | guard-policy |     | pol1 |     |
CreatingtheDHCPv6snoopingguardpolicynamepol1onaVLAN:
switch(config)#
|                          |           | vlan 100 |                 |                    |                                           |     |      |
| ------------------------ | --------- | -------- | --------------- | ------------------ | ----------------------------------------- | --- | ---- |
| switch(config-vlan-100)# |           |          | dhcpv6-snooping |                    | guard-policy                              |     | pol1 |
| Command History          |           |          |                 |                    |                                           |     |      |
| Release                  |           |          |                 | Modification       |                                           |     |      |
| 10.10                    |           |          |                 | Commandintroduced. |                                           |     |      |
| Command Information      |           |          |                 |                    |                                           |     |      |
| Platforms                | Command   |          | context         |                    | Authority                                 |     |      |
| 8360                     | config    |          |                 |                    | Administratorsorlocalusergroupmemberswith |     |      |
|                          | config-if |          |                 |                    | executionrightsforthiscommand.            |     |      |
config-dhcpv6-guard-policy
config-vlan-<VLAN-ID>
| show dhcpv6-snooping |     |                             | guard-policy |     |     |            |     |
| -------------------- | --- | --------------------------- | ------------ | --- | --- | ---------- | --- |
| show dhcpv6-snooping |     | guard-policy[<POLICY_NAME>] |              |     |     | [vsx-peer] |     |
Description
ShowstheDHCPv6snoopingguardpolicyconfiguration.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 166

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<POLICY-NAME> SpecifiestheDHCPv6snoopingguardpolicyforwhichthe
informationisdisplayed.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfiguration:
| switch# show    | dhcpv6-snooping |              | guard-policy |       |
| --------------- | --------------- | ------------ | ------------ | ----- |
| DHCPv6-Snooping |                 | guard-policy | Information  |       |
| DHCPV6          | Guard           | Policy name  | : POL1       |       |
| Attached        | Access          | List         | : ACL1       |       |
| Attached        | Prefix          | List         | : PRF1       |       |
| Preference      |                 | Range        | : 0-255      |       |
| Applied         | on              | VLAN         | : 5,7        |       |
| Applied         | on              | Port         |              |       |
| DHCPV6          | Guard           | Policy name  | : POL2       |       |
| Attached        | Access          | List         | : ACL2       |       |
| Attached        | Prefix          | List         | : PRF2       |       |
| Preference      |                 | Range        | : 2-20       |       |
| Applied         | on              | VLAN         |              |       |
| Applied         | on              | Port         | : 1/1/1,     | 1/1/2 |
| DHCPV6          | Guard           | Policy name  | : POL3       |       |
| Attached        | Access          | List         | : ACL3       |       |
| Attached        | Prefix          | List         | : PRF3       |       |
| Preference      |                 | Range        | : 3-60       |       |
| Applied         | on              | VLAN         | : 4,6        |       |
| Applied         | on              | Port         |              |       |
ShowingtheDHCPv6snoopingguardpolicyconfigurationforthepolicynamedPOLICY_NAME1:
| switch# show    | dhcpv6-snooping |              | guard-policy | POLICY_NAME1 |
| --------------- | --------------- | ------------ | ------------ | ------------ |
| DHCPv6-Snooping |                 | guard-policy | Information  |              |
========================
| DHCPV6     | Guard  | Policy name | : POLICY_NAME1 |     |
| ---------- | ------ | ----------- | -------------- | --- |
| Attached   | Access | List        | : ACL1         |     |
| Attached   | Prefix | List        | : PRF1         |     |
| Preference |        | Range       | : 0-255        |     |
vsx-sync
| Applied         | on  | VLAN | : 5,7              |       |
| --------------- | --- | ---- | ------------------ | ----- |
| Applied         | on  | Port | : 1/1/1,           | 1/1/2 |
| Command History |     |      |                    |       |
| Release         |     |      | Modification       |       |
| 10.10           |     |      | Commandintroduced. |       |
DHCPsnooping|167

| Command Information |         |         |     |           |     |     |
| ------------------- | ------- | ------- | --- | --------- | --- | --- |
| Platforms           | Command | context |     | Authority |     |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |     | guard-policy |     | interface |     |
| -------------------- | --- | --- | ------------ | --- | --------- | --- |
show dhcpv6-snooping guard-policy [interface <INTERFACE-NAME>] [vsx-peer]
Description
ShowstheDHCPv6snoopingguardpolicyconfigurationandstatisticsforthespecifiedinterface.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-NAME> SpecifiestheinterfacenameforwhichtheDHCPv6guardcounter
informationisdisplayed.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfigurationandstatisticsforinterface1/1/1:
| switch# show | dhcpv6-snooping |          | guard-policy |        | int 1/1/1 |     |
| ------------ | --------------- | -------- | ------------ | ------ | --------- | --- |
| DHCPv6 Guard | Policy          | Applied  |              | : pol1 |           |     |
| DHCPv6       | Guard Policy    | Counters |              |        |           |     |
==========================
| DHCPv6 Packets      | Received  |         |     | : 20               |                  |     |
| ------------------- | --------- | ------- | --- | ------------------ | ---------------- | --- |
| DHCPv6 Packets      | Forwarded |         |     | : 5                |                  |     |
| DHCPv6 Packets      | Dropped   |         |     | : 15 [Total]       |                  |     |
|                     |           |         |     | Access             | list error       | [7] |
|                     |           |         |     | Prefix             | list error       | [8] |
|                     |           |         |     | Server             | preference error | [0] |
| Command History     |           |         |     |                    |                  |     |
| Release             |           |         |     | Modification       |                  |     |
| 10.10               |           |         |     | Commandintroduced. |                  |     |
| Command Information |           |         |     |                    |                  |     |
| Platforms           | Command   | context |     | Authority          |                  |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 168

| show dhcpv6-snooping |     |              | guard-policy |                  | vlan |            |     |
| -------------------- | --- | ------------ | ------------ | ---------------- | ---- | ---------- | --- |
| show dhcpv6-snooping |     | guard-policy |              | [vlan <VLAN-ID>] |      | [vsx-peer] |     |
Description
ShowstheDHCPv6snoopingguardpolicyconfigurationandstatisticsforthespecifiedVLAN.
| Parameter |     |     |     | Description                                      |     |     |     |
| --------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
| <VLAN-ID> |     |     |     | SpecifiestheVLANID forwhichtheDHCPv6guardcounter |     |     |     |
informationisdisplayed.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfigurationandstatisticsforVLAN100:
| switch# show | dhcpv6-snooping |                 |     | guard-policy | vlan | 2   |     |
| ------------ | --------------- | --------------- | --- | ------------ | ---- | --- | --- |
| DHCPv6 Guard |                 | Policy Applied  |     | : pol1       |      |     |     |
| DHCPv6       | Guard           | Policy Counters |     |              |      |     |     |
==========================
| DHCPv6 Packets      |         | Received  |     | : 20               |            |       |     |
| ------------------- | ------- | --------- | --- | ------------------ | ---------- | ----- | --- |
| DHCPv6 Packets      |         | Forwarded |     | : 5                |            |       |     |
| DHCPv6 Packets      |         | Dropped   |     | : 15 [Total]       |            |       |     |
|                     |         |           |     | Access             | list       | error | [0] |
|                     |         |           |     | Prefix             | list       | error | [8] |
|                     |         |           |     | Server             | preference | error | [7] |
| Command History     |         |           |     |                    |            |       |     |
| Release             |         |           |     | Modification       |            |       |     |
| 10.10               |         |           |     | Commandintroduced. |            |       |     |
| Command Information |         |           |     |                    |            |       |     |
| Platforms           | Command | context   |     | Authority          |            |       |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |            | statistics |            |     |     |     |
| -------------------- | --- | ---------- | ---------- | ---------- | --- | --- | --- |
| show dhcpv6-snooping |     | statistics |            | [vsx-peer] |     |     |     |
Description
ShowstheDHCPv6snoopingstatistics.
DHCPsnooping|169

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheDHCPv6snoopingstatistics:
| switch(config)# | show    | dhcpv6-snooping               |         |                | statistics                                      |       |           |
| --------------- | ------- | ----------------------------- | ------- | -------------- | ----------------------------------------------- | ----- | --------- |
| Packet-Type     | Action  | Reason                        |         |                |                                                 |       | Count     |
| -----------     | ------- | ----------------------------- |         |                |                                                 |       | --------- |
| server          | forward | from                          | trusted |                | port                                            |       | 12        |
| client          | forward | to                            | trusted |                | port                                            |       | 20        |
| server          | drop    | received                      |         | on             | untrusted                                       | port  | 5         |
| server          | drop    | unauthorized                  |         |                | server                                          |       | 4         |
| client          | drop    | destination                   |         |                | on untrusted                                    | port  | 2         |
| client          | drop    | bad                           | DHCP    | release        | request                                         |       | 5         |
| server          | drop    | relay                         |         | reply          | on untrusted                                    | port  | 2         |
| client          | drop    | failed                        |         | on max-binding |                                                 | limit | 5         |
| Command History |         |                               |         |                |                                                 |       |           |
| Release         |         |                               |         |                | Modification                                    |       |           |
| 10.09.1000      |         |                               |         |                | Commandintroducedforthe8360SwitchSeries.        |       |           |
| 10.09           |         |                               |         |                | Commandintroducedforthe6000and6100SwitchSeries. |       |           |
10.07orearlier
| Command Information |         |         |     |     |           |     |     |
| ------------------- | ------- | ------- | --- | --- | --------- | --- | --- |
| Platforms           | Command | context |     |     | Authority |     |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 170

Chapter 7

ND snooping

ND snooping

ND snooping is not supported on the 8320 Switch Series.

Overview (applies to the 8325, 9300, 10000 Switch Series)

ND (Neighbor Discovery) snooping is used in Layer 2 switching networks and prevents ND attacks. RA
(Router Advertisement) guard is a sub-feature of ND snooping and manages RA and RR (Router Redirect)
packets on configured VLANs. RA and RR packets received on trusted ports are allowed. RA and
RR packets are dropped in the following cases:

n If the Ethernet source MAC address is mismatched with the address contained in the ICMPv6 Target

link layer address field of the ND packet.

n If a packet is received on an untrusted port of a RA guard enabled VLAN.

On the 8325, 9300, and 10000 Switch Series, only the RA guard portion of ND snooping is supported. The

following are not supported: RA guard policy, ND guard, RA drop.

Overview (applies to the 8360 Switch Series)

ND snooping is used in Layer 2 switching networks and prevents ND attacks. ND snooping drops invalid
ND packets, and together with DIPLDv6 (Dynamic IP Lockdown for IPv6), blocks data traffic from invalid
hosts. ND snooping learns the source MAC addresses, source IPv6 addresses, input interfaces, and
VLANs of incoming ND messages and data packets to build IP binding entries.

When DHCPv6 snooping and ND snooping are both enabled, and DHCPv6 clients request and IPv6 address,

entries are added to the DHCPv6 snooping table and DHCPv6 snooping takes priority over ND snooping.

ND snooping drops ND packets as follows:

n If the Ethernet source MAC address is mismatched with the address contained in the ICMPv6 Target

link layer address field of the ND packet.

n If the global IPv6 address in the source address field is mismatched with the ND snooping prefix filter

table.

n If the global IPv6 address or the link-local IPv6 address in the source IP address field is mismatched

with the ND snooping binding table.

ND snooping drops RA and RR packets on untrusted ports. To block only RA packets on VLANs with ND
snooping enabled, use nd-snooping ra-drop. RA (Router Advertisement) drop is disabled by default on
VLANs. When enabled (with nd-snooping ra-drop), ND snooping blocks RA packets on both trusted and
untrusted ports. When RA drop is disabled, ND snooping allows RA packets on trusted ports and blocks
them on untrusted ports.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

171

WhenRAguardpolicyisenabled(withipv6 nd-snooping ra-guard policy),RApacketsreceivedon
trustedportsarevalidatedagainstasetofparametersconfiguredonthepolicyandassignedtoaport
orVLAN.
FormoreinformationonRA guardincludingRAguardpolicies,seethisrelatedvideoontheArubaAirHeads
BroadcastingChannel.
DynamicIPv6lockdownisperformedforNDsnoopingentries.BasedontheDADNSreceivedfromthe
hostsbytheswitch,NDsnoopingentriesareprogrammedintotheIPbindingtableandthehardware
(asallowed).AndNDBindingtableentriesareaddedwhenNApacketsarereceivedfromhosts.
Therefore,datapacketsfrominvalidhostsandtransittrafficareblocked.
Statically-configuredIPbindinginformationsupersedesanyinformationcollecteddynamicallybyNDsnooping
forthesameclient.
| ND snooping       | commands |     |     |     |
| ----------------- | -------- | --- | --- | --- |
| clear nd-snooping | binding  |     |     |     |
clear nd-snooping bindings {all | ipv6 <IPV6-ADDR> vlan <VLAN-ID> |
| port <PORT-NUM> | | vlan <VLAN-ID>} |     |     |     |
| --------------- | ----------------- | --- | --- | --- |
Description
ClearsNDsnoopingbindingentries.
Command context
| Parameter |     | Description                                        |     |     |
| --------- | --- | -------------------------------------------------- | --- | --- |
| all       |     | SpecifiesthatallNDbindinginformationistobecleared. |     |     |
ip <IPV6-ADDR> vlan <VLAN-ID> SpecifiestheIPv6addressandVLANforwhichallNDbinding
informationistobecleared.
port <PORT-NUM> Specifiestheport(interface)forwhichallNDbindinginformation
istobecleared.
vlan <VLAN-ID>
SpecifiestheVLANforwhichallNDbindinginformationistobe
cleared.Range:1to4094.
Examples
ClearingallNDbindinginformationfor5000::1vlan1:
| switch(config)# | clear nd-snooping | bindings ipv6 | 5000::1 vlan | 1   |
| --------------- | ----------------- | ------------- | ------------ | --- |
ClearingallNDbindinginformationforport1/1/10:
| switch(config)# | clear nd-snooping | bindings port | 1/1/10 |     |
| --------------- | ----------------- | ------------- | ------ | --- |
ClearingallNDbindinginformationforVLAN10:
NDsnooping|172

| switch(config)# | clear | nd-snooping | bindings | vlan | 10  |
| --------------- | ----- | ----------- | -------- | ---- | --- |
ClearingallNDbindinginformation:
| switch(config)#     | clear   | nd-snooping | bindings                | all |     |
| ------------------- | ------- | ----------- | ----------------------- | --- | --- |
| Command History     |         |             |                         |     |     |
| Release             |         |             | Modification            |     |     |
| 10.10               |         |             | Addedsupportforthe8360. |     |     |
| 10.07orearlier      |         |             | --                      |     |     |
| Command Information |         |             |                         |     |     |
| Platforms           | Command | context     | Authority               |     |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| clear nd-snooping |     | ra-guard-policy |     | statistics |     |
| ----------------- | --- | --------------- | --- | ---------- | --- |
clear nd-snooping ra-guard-policy statistics [vlan <VLAN-ID>]|[interface <IFNAME>]
Description
ClearallRAGuardpolicystatisticsfromthespecifiedinterfaceorVLAN.
| Command context |     |     |             |     |     |
| --------------- | --- | --- | ----------- | --- | --- |
| Parameter       |     |     | Description |     |     |
vlan <VLAN-ID> ClearallRAGuardpolicyinformationonthespecifiedVLAN
interface <IFNAME> ClearallRAGuardpolicyinformationonthespecifiedinterface
Examples
ClearallRAGuardpolicystatisticsforVLAN10:
| switch# clear | nd-snooping | ra-guard-policy |     | statistics | vlan 10 |
| ------------- | ----------- | --------------- | --- | ---------- | ------- |
ClearallRAGuardpolicystatisticsforinterface1/1/10
switch# clear nd-snooping ra-guard-policy statistics interface 1/1/10
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 173

| Release             |         |         | Modification       |
| ------------------- | ------- | ------- | ------------------ |
| 10.10               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| clear nd-snooping |            | statistics |     |
| ----------------- | ---------- | ---------- | --- |
| clear nd-snooping | statistics |            |     |
Description
ClearsallNDsnoopingstatistics.
Examples
ClearallNDsnoopingstatistics:
| switch# clear       | nd-snooping | statistics |                                                      |
| ------------------- | ----------- | ---------- | ---------------------------------------------------- |
| Command History     |             |            |                                                      |
| Release             |             |            | Modification                                         |
| 10.10               |             |            | Addedsupportforthe8360.                              |
| 10.09               |             |            | Addedsupportforthe8325.Addedsupportforthe10000.      |
| 10.07orearlier      |             |            | --                                                   |
| Command Information |             |            |                                                      |
| Platforms           | Command     | context    | Authority                                            |
| 8325                |             |            | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
8360 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 9300 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
10000
nd-snooping
| nd-snooping    | {enable|disable} |     |     |
| -------------- | ---------------- | --- | --- |
| no nd-snooping | {enable|disable} |     |     |
Description
EnablesordisablesNDsnooping.NDsnoopingisdisabledbydefault.NDsnoopingisnotsupportedon
themanagementinterface.
Examples
NDsnooping|174

EnablingNDsnooping:
| switch(config)# | nd-snooping |     | enable |     |
| --------------- | ----------- | --- | ------ | --- |
DisablingNDsnooping:
| switch(config)#     | nd-snooping |         | disable |                                                 |
| ------------------- | ----------- | ------- | ------- | ----------------------------------------------- |
| Command History     |             |         |         |                                                 |
| Release             |             |         |         | Modification                                    |
| 10.10               |             |         |         | Addedsupportforthe8360.                         |
| 10.09               |             |         |         | Addedsupportforthe8325.Addedsupportforthe10000. |
| 10.07orearlier      |             |         |         | --                                              |
| Command Information |             |         |         |                                                 |
| Platforms           | Command     | context |         | Authority                                       |
8325 config Administratorsorlocalusergroupmemberswithexecution
| 8360 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
9300
10000
| nd-snooping | (in config-vlan |     |     | context) |
| ----------- | --------------- | --- | --- | -------- |
nd-snooping
no nd-snooping
Description
EnablesNDsnoopingintheconfig-vlancontext.NDsnoopingisdisabledbydefaultforallVLANs.
ThenoformofthecommanddisablesNDsnoopingonthespecifiedVLAN.
Examples
EnablingNDsnoopingonVLAN100:
| switch(config)#          | vlan | 100 |             |     |
| ------------------------ | ---- | --- | ----------- | --- |
| switch(config-vlan-100)# |      |     | nd-snooping |     |
| switch(config-vlan-100)# |      |     | exit        |     |
switch(config)#
DisablingNDsnoopingonVLAN100:
| switch(config)# | vlan | 100 |     |     |
| --------------- | ---- | --- | --- | --- |
switch(config-vlan-100)#
no nd-snooping
| switch(config-vlan-100)# |     |     | exit |     |
| ------------------------ | --- | --- | ---- | --- |
switch(config)#
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 175

| Command History     |         |         |     |                                                 |
| ------------------- | ------- | ------- | --- | ----------------------------------------------- |
| Release             |         |         |     | Modification                                    |
| 10.10               |         |         |     | Addedsupportforthe8360.                         |
| 10.09               |         |         |     | Addedsupportforthe8325.Addedsupportforthe10000. |
| 10.07orearlier      |         |         |     | --                                              |
| Command Information |         |         |     |                                                 |
| Platforms           | Command | context |     | Authority                                       |
8325 config-vlan Administratorsorlocalusergroupmemberswithexecution
| 8360 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
9300
10000
| nd-snooping    | mac-check |     |     |     |
| -------------- | --------- | --- | --- | --- |
| nd-snooping    | mac-check |     |     |     |
| no nd-snooping | mac-check |     |     |     |
Description
ThiscommandenablesverificationofthehardwareaddressfieldinNDsnoopingpackets.When
enabled,theICMPv6targetlinklayeraddressfieldandthesourceMACaddressmustbethesamefor
packetsreceivedonuntrustedportsorelsethepacketsaredropped.ThisNDsnoopingMAC
verificationisenabledbydefault.
ThenoformofthecommanddisablesNDsnoopingMACverification.
Examples
EnablingNDsnoopingMACverification:
| switch(config)# | nd-snooping |     | mac-check |     |
| --------------- | ----------- | --- | --------- | --- |
DisablingNDsnoopingMACverification:
| switch(config)#     | no  | nd-snooping |     | mac-check                                       |
| ------------------- | --- | ----------- | --- | ----------------------------------------------- |
| Command History     |     |             |     |                                                 |
| Release             |     |             |     | Modification                                    |
| 10.10               |     |             |     | Addedsupportforthe8360.                         |
| 10.09               |     |             |     | Addedsupportforthe8325.Addedsupportforthe10000. |
| 10.07orearlier      |     |             |     | --                                              |
| Command Information |     |             |     |                                                 |
NDsnooping|176

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
8325 config Administratorsorlocalusergroupmemberswithexecution
| 8360 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
9300
10000
| nd-snooping    | prefix-list |             |     |     |
| -------------- | ----------- | ----------- | --- | --- |
| nd-snooping    | prefix-list | <IPV6-ADDR> |     |     |
| no nd-snooping | prefix-list | <IPV6-ADDR> |     |     |
Description
ConfigurestheNDsnoopingprefixlistfortheselectedVLANandthespecifiedIPv6addressprefix.ND
snoopingmustbeenabledbothgloballyandonthisVLANbeforethisprefixlistconfigurationtakes
effect.
ThenoformofthiscommandremovestheprefixlistconfigurationfortheselectedVLANandIPv6
address.
| Parameter   |     |     | Description              |     |
| ----------- | --- | --- | ------------------------ | --- |
| <IPV6-ADDR> |     |     | SpecifiestheIPv6address. |     |
Examples
ConfiguringNDsnoopingprefix-listonVLAN1:
| switch(config)#        | vlan | 1           |             |            |
| ---------------------- | ---- | ----------- | ----------- | ---------- |
| switch(config-vlan-1)# |      | nd-snooping | prefix-list | 2001::1/64 |
switch(config-vlan-1)#
exit
switch(config)#
RemoveconfigurationofNDsnoopingprefix-listonVLAN100:
| switch(config)#        | vlan | 1              |             |            |
| ---------------------- | ---- | -------------- | ----------- | ---------- |
| switch(config-vlan-1)# |      | no nd-snooping | prefix-list | 2001::1/64 |
| switch(config-vlan-1)# |      | exit           |             |            |
switch(config)#
| Command        | History     |     |                         |     |
| -------------- | ----------- | --- | ----------------------- | --- |
| Release        |             |     | Modification            |     |
| 10.10          |             |     | Addedsupportforthe8360. |     |
| 10.07orearlier |             |     | --                      |     |
| Command        | Information |     |                         |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 177

| Platforms | Command |     | context |     | Authority |     |
| --------- | ------- | --- | ------- | --- | --------- | --- |
8360 config-vlan-<VLAN-ID> OperatorsorAdministratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.Operatorscan
executethiscommandfromtheoperatorcontext(>)only.
| nd-snooping    |              | max-bindings |                |     |     |     |
| -------------- | ------------ | ------------ | -------------- | --- | --- | --- |
| nd-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |     |
| no nd-snooping | max-bindings |              |                |     |     |     |
Description
SetsthemaximumnumberofNDbindingsallowedontheselectedinterface.Forallinterfacesonwhich
thiscommandisnotrun,thedefaultmaxbindingsapplies.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofNDbindings.Youcanusethe
|     |     |     |     | show | capacitiescommandtoseethemaximumavailablefor |     |
| --- | --- | --- | --- | ---- | -------------------------------------------- | --- |
yourswitchmodel.
Examples
SettheNDmaxbindingsto768oninterface2/2/1:
| switch(config)#    |     | interface | 2/2/1       |              |     |     |
| ------------------ | --- | --------- | ----------- | ------------ | --- | --- |
| switch(config-if)# |     |           | nd-snooping | max-bindings |     | 768 |
| switch(config-if)# |     |           | exit        |              |     |     |
switch(config)#
RevertNDmaxbindingstoitsdefaultoninterface2/2/1:
| switch(config)#    |     | interface | 2/2/1          |     |              |     |
| ------------------ | --- | --------- | -------------- | --- | ------------ | --- |
| switch(config-if)# |     |           | no nd-snooping |     | max-bindings |     |
| switch(config-if)# |     |           | exit           |     |              |     |
switch(config)#
| Command        | History     |     |         |                         |           |     |
| -------------- | ----------- | --- | ------- | ----------------------- | --------- | --- |
| Release        |             |     |         | Modification            |           |     |
| 10.10          |             |     |         | Addedsupportforthe8360. |           |     |
| 10.07orearlier |             |     |         | --                      |           |     |
| Command        | Information |     |         |                         |           |     |
| Platforms      | Command     |     | context |                         | Authority |     |
8360 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
NDsnooping|178

| nd-snooping    | nd-guard |     |     |
| -------------- | -------- | --- | --- |
| nd-snooping    | nd-guard |     |     |
| no nd-snooping | nd-guard |     |     |
Description
ThiscommandenablesNDguardontheselectedVLAN.
ThenoformofthecommanddisablesNDguardanddeletesalltheIPv6bindingslearnedontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
Examples
EnablingNDsnoopingNDguardonVLAN100:
switch(config)#
|                          | nd-snooping | enable      |          |
| ------------------------ | ----------- | ----------- | -------- |
| switch(config)#          | vlan        | 100         |          |
| switch(config-vlan-100)# |             | nd-snooping | nd-guard |
| switch(config-vlan-100)# |             | exit        |          |
switch(config)#
DisablingNDsnoopingNDguardonVLAN100:
| switch(config)#          | vlan | 100            |          |
| ------------------------ | ---- | -------------- | -------- |
| switch(config-vlan-100)# |      | no nd-snooping | nd-guard |
| switch(config-vlan-100)# |      | exit           |          |
switch(config)#
| Command History     |         |         |                         |
| ------------------- | ------- | ------- | ----------------------- |
| Release             |         |         | Modification            |
| 10.10               |         |         | Addedsupportforthe8360. |
| 10.07orearlier      |         |         | --                      |
| Command Information |         |         |                         |
| Platforms           | Command | context | Authority               |
config-vlan
| 8360 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| nd-snooping    | ra-guard       |     |     |
| -------------- | -------------- | --- | --- |
| nd-snooping    | ra-guard [log] |     |     |
| no nd-snooping | ra-guard       |     |     |
Description
ThiscommandenablesRoutingAdvertisement(RA)guardontheselectedVLAN.Whenenabled,ingress
RoutingAdvertisement(RA)andRoutingRedirect(RR)packetsontheselectedVLANareblockedon
untrustedports.Thepacketsareforwardedwhenreceivedontrustedports.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 179

ThenoformofthecommanddisablesRAguardontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     |     | Description                             |
| --------- | --- | --- | --- | --------------------------------------- |
| [log]     |     |     |     | Logsmessagesalongwithdropfunctionality. |
Examples
EnablingNDsnoopingRAguardonVLAN100:
| switch(config)#          | nd-snooping |     | enable      |          |
| ------------------------ | ----------- | --- | ----------- | -------- |
| switch(config)#          | vlan        | 100 |             |          |
| switch(config-vlan-100)# |             |     | nd-snooping | ra-guard |
| switch(config-vlan-100)# |             |     | exit        |          |
switch(config)#
EnablingNDsnoopingRAguardonVLAN100witheventloggingondroppedpackets:
| switch(config)#          | nd-snooping |     | enable      |              |
| ------------------------ | ----------- | --- | ----------- | ------------ |
| switch(config)#          | vlan        | 100 |             |              |
| switch(config-vlan-100)# |             |     | nd-snooping | ra-guard log |
| switch(config-vlan-100)# |             |     | exit        |              |
switch(config)#
DisablingNDsnoopingRAguardonVLAN100:
| switch(config)#          | vlan | 100 |                |          |
| ------------------------ | ---- | --- | -------------- | -------- |
| switch(config-vlan-100)# |      |     | no nd-snooping | ra-guard |
| switch(config-vlan-100)# |      |     | exit           |          |
switch(config)#
| Command History     |         |         |     |                                                 |
| ------------------- | ------- | ------- | --- | ----------------------------------------------- |
| Release             |         |         |     | Modification                                    |
| 10.10               |         |         |     | Addedsupportforthe8360.                         |
| 10.09               |         |         |     | Addedsupportforthe8325.Addedsupportforthe10000. |
| 10.07orearlier      |         |         |     | --                                              |
| Command Information |         |         |     |                                                 |
| Platforms           | Command | context |     | Authority                                       |
8325 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
| 8360 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
9300
10000
NDsnooping|180

| nd-snooping    | ra-drop |     |     |     |
| -------------- | ------- | --- | --- | --- |
| nd-snooping    | ra-drop |     |     |     |
| no nd-snooping | ra-drop |     |     |     |
Description
ThiscommandenablesRoutingAdvertisement(RA)dropontheselectedVLAN.Whenenabled,ingress
RApacketsontheselectedVLANareblockedonbothtrustedanduntrustedports.Whendisabled,RA
packetsareforwardedontheselectedVLANwithNDsnoopingtrustedportvalidation.RAdropis
disabledbydefault.
NDsnoopingmustbeenabledinboththeconfigcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
ThenoformofthecommanddisablesNDsnoopingRAdropontheselectedVLAN.
Examples
EnablingNDsnoopingRAdroponVLAN100:
| switch(config)#          | nd-snooping |     | enable      | vlan 100 |
| ------------------------ | ----------- | --- | ----------- | -------- |
| switch(config-vlan-100)# |             |     | nd-snooping | ra-drop  |
| switch(config-vlan-100)# |             |     | exit        |          |
switch(config)#
DisablingNDsnoopingRAdroponVLAN100:
| switch(config)#          | vlan | 100 |                |         |
| ------------------------ | ---- | --- | -------------- | ------- |
| switch(config-vlan-100)# |      |     | no nd-snooping | ra-drop |
| switch(config-vlan-100)# |      |     | exit           |         |
switch(config)#
| Command History     |         |         |     |                         |
| ------------------- | ------- | ------- | --- | ----------------------- |
| Release             |         |         |     | Modification            |
| 10.10               |         |         |     | Addedsupportforthe8360. |
| 10.07orearlier      |         |         |     | --                      |
| Command Information |         |         |     |                         |
| Platforms           | Command | context |     | Authority               |
config-vlan-<VLAN-ID>
| 8360 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| nd-snooping    | trust |     |     |     |
| -------------- | ----- | --- | --- | --- |
| nd-snooping    | trust |     |     |     |
| no nd-snooping | trust |     |     |     |
Description
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 181

EnablesNDsnoopingtrustontheselectedinterface(port)allowingRA andRRpacketstobereceived.
RA andRR packetsreceivedonuntrustedportsarediscarded,allportsareuntrustedbydefault.
ThenoformofthecommanddisablesNDsnoopingtrustontheselectedport.
Examples
EnablingNDsnoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface   | 2/2/1 |       |
| ------------------ | --- | ----------- | ----- | ----- |
| switch(config-if)# |     | nd-snooping |       | trust |
| switch(config-if)# |     | exit        |       |       |
switch(config)#
DisablingNDsnoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface      | 2/2/1 |       |
| ------------------ | --- | -------------- | ----- | ----- |
| switch(config-if)# |     | no nd-snooping |       | trust |
| switch(config-if)# |     | exit           |       |       |
switch(config)#
| Command History     |         |         |     |                                                 |
| ------------------- | ------- | ------- | --- | ----------------------------------------------- |
| Release             |         |         |     | Modification                                    |
| 10.10               |         |         |     | Addedsupportforthe8360.                         |
| 10.09               |         |         |     | Addedsupportforthe8325.Addedsupportforthe10000. |
| 10.07orearlier      |         |         |     | --                                              |
| Command Information |         |         |     |                                                 |
| Platforms           | Command | context |     | Authority                                       |
8325 config-if Administratorsorlocalusergroupmemberswithexecution
| 8360 |     |     |     | rightsforthiscommand. |
| ---- | --- | --- | --- | --------------------- |
9300
10000
show nd-snooping
| show nd-snooping | [vlan | <VLAN-ID>] |     | [vsx-peer] |
| ---------------- | ----- | ---------- | --- | ---------- |
Description
ShowseitherallNDsnoopingconfigurationortheconfigurationforthespecifiedVLAN.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
vlan <VLAN-ID> SpecifiestheVLANforwhichtheNDconfigurationistobeshown.
Range:1to4094.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
NDsnooping|182

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
(Appliestothe6200,6300,6400and8360.)ShowingallNDsnoopingconfiguration:
| switch(config)# | show        | nd-snooping |     |     |
| --------------- | ----------- | ----------- | --- | --- |
| ND Snooping     | Information |             |     |     |
========================
| ND Snooping     |               |         |                   | : Enabled  |
| --------------- | ------------- | ------- | ----------------- | ---------- |
| ND Snooping     | Enabled       | VLANs   |                   | : 10       |
| Trusted Port    | Bindings      | Enabled | VLANs             | : 10       |
| ND Guard        | Enabled VLANs |         |                   | : 10       |
| RA Guard        | Enabled VLANs |         |                   | : 10       |
| RA Drop Enabled | VLANs         |         |                   | :          |
| MAC Address     | Check         |         |                   | : Disabled |
| PORT TRUST      | MAX-BINDINGS  |         | CURRENT-BINDINGS  |            |
| ------- ------  | ------------- |         | ----------------- |            |
| 1/1/1 Yes       |               |         |                   |            |
| 1/1/2 Yes       |               |         |                   |            |
| 1/1/3 No        | 100           |         | 10                |            |
| 1/1/4 No        | 200           |         | 10                |            |
| 1/1/5 No        | 300           |         | 10                |            |
(Appliestothe6200,6300,6400,8360.)ShowingNDsnoopingconfigurationforVLAN2:
| switch(config)# | show        | nd-snooping | vlan | 2   |
| --------------- | ----------- | ----------- | ---- | --- |
| ND Snooping     | Information |             |      |     |
=======================
| ND Snooping    |               | : Enabled  |                   |     |
| -------------- | ------------- | ---------- | ----------------- | --- |
| MAC Address    | Check         | : Disabled |                   |     |
| Trusted Port   | Bindings      | : Enabled  |                   |     |
| ND Guard       |               | : Enabled  |                   |     |
| RA Guard       |               | : Disabled |                   |     |
| RA Drop        |               | : Disabled |                   |     |
| PORT TRUST     | MAX-BINDINGS  |            | CURRENT-BINDINGS  |     |
| ------- ------ | ------------- |            | ----------------- |     |
| 1/1/1 Yes      |               |            |                   |     |
| 1/1/2 Yes      |               |            |                   |     |
| 1/1/3 No       | 100           |            | 10                |     |
(Appliestothe8325,9300,10000.)ShowingallNDsnoopingconfiguration:
| switch(config)# | show        | nd-snooping |     |     |
| --------------- | ----------- | ----------- | --- | --- |
| ND Snooping     | Information |             |     |     |
========================
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 183

| ND Snooping |         |       | : Enabled  |
| ----------- | ------- | ----- | ---------- |
| ND Snooping | Enabled | VLANs | : 10       |
| RA Guard    | Enabled | VLANs | : 10       |
| MAC Address | Check   |       | : Disabled |
| PORT        | TRUST   |       |            |
| -------     | ------  |       |            |
| 1/1/1       | Yes     |       |            |
| 1/1/2       | Yes     |       |            |
| 1/1/3       | No      |       |            |
| 1/1/4       | No      |       |            |
| 1/1/5       | No      |       |            |
(Appliestothe8325,9300,10000.)ShowingNDsnoopingconfigurationforVLAN2:
| switch(config)# |             | show nd-snooping | vlan 2 |
| --------------- | ----------- | ---------------- | ------ |
| ND Snooping     | Information |                  |        |
=======================
| ND Snooping         |         | : Enabled  |                                                 |
| ------------------- | ------- | ---------- | ----------------------------------------------- |
| MAC Address         | Check   | : Disabled |                                                 |
| RA Guard            |         | : Disabled |                                                 |
| PORT                | TRUST   |            |                                                 |
| -------             | ------  |            |                                                 |
| 1/1/1               | Yes     |            |                                                 |
| 1/1/2               | Yes     |            |                                                 |
| 1/1/3               | No      |            |                                                 |
| Command History     |         |            |                                                 |
| Release             |         |            | Modification                                    |
| 10.10               |         |            | Addedsupportforthe8360.                         |
| 10.09               |         |            | Addedsupportforthe8325.Addedsupportforthe10000. |
| 10.07orearlier      |         |            | --                                              |
| Command Information |         |            |                                                 |
| Platforms           | Command | context    | Authority                                       |
8325 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8360 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 9300 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
10000
| show nd-snooping |          | bindings   |     |
| ---------------- | -------- | ---------- | --- |
| show nd-snooping | bindings | [vsx-peer] |     |
Description
ShowstheNDsnoopingbindingconfiguration.
NDsnooping|184

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheNDsnoopingbindingconfiguration:
| switch# show | nd-snooping  | bindings |     |             |            |
| ------------ | ------------ | -------- | --- | ----------- | ---------- |
| PORT         | IPV6-ADDRESS |          |     | MAC-ADDRESS | VLAN TIME- |
| LEFT STATE   |              |          |     |             |            |
------- ---------------------------------------- ------------------ ----- ------
--- ---------
| 1/1/1 | 2001::1 |     |     | 00:00:0A:01:02:03 | 1 600 |
| ----- | ------- | --- | --- | ----------------- | ----- |
Valid
| 1/1/2 | fe80::250:56ff:fe9a:143c |     |     | 00:00:0B:01:02:03 | 2 - |
| ----- | ------------------------ | --- | --- | ----------------- | --- |
Tentative
1/1/3 2001:1111:2222:3333:4444:5555:6666:7777 00:00:0C:01:02:03 4094 -
Testing
| Command History     |         |         |                         |     |     |
| ------------------- | ------- | ------- | ----------------------- | --- | --- |
| Release             |         |         | Modification            |     |     |
| 10.10               |         |         | Addedsupportforthe8360. |     |     |
| 10.07orearlier      |         |         | --                      |     |     |
| Command Information |         |         |                         |     |     |
| Platforms           | Command | context | Authority               |     |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show nd-snooping |             | prefix-list |     |     |     |
| ---------------- | ----------- | ----------- | --- | --- | --- |
| show nd-snooping | prefix-list | [vsx-peer]  |     |     |     |
Description
ShowstheNDsnoopingprefixlistinformation.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 185

ShowingtheNDsnoopingprefixlistinformation:
| switch# show                                      | nd-snooping | prefix-list |     |                                           |          |     |
| ------------------------------------------------- | ----------- | ----------- | --- | ----------------------------------------- | -------- | --- |
| VLAN IPV6-ADDRESS-PREFIX                          |             |             |     |                                           | SOURCE   |     |
| ----- ------------------------------------------- |             |             |     |                                           | -------- |     |
| 1 2001::/64                                       |             |             |     |                                           | Static   |     |
| 4094 3001::/64                                    |             |             |     |                                           | Dynamic  |     |
| Command History                                   |             |             |     |                                           |          |     |
| Release                                           |             |             |     | Modification                              |          |     |
| 10.10                                             |             |             |     | Addedsupportforthe8360.                   |          |     |
| 10.09                                             |             |             |     | Addedsupportforthe8325.Addedsupportforthe |          |     |
10000.
| 10.07orearlier      |         |         |           | --  |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- | --- |
| Command Information |         |         |           |     |     |     |
| Platforms           | Command | context | Authority |     |     |     |
8325 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 8360 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| ---- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
(#)
commandfromtheoperatorcontext(>)only.
9300
10000
| show nd-snooping |            | statistics |     |     |     |     |
| ---------------- | ---------- | ---------- | --- | --- | --- | --- |
| show nd-snooping | statistics | [vsx-peer] |     |     |     |     |
Description
ShowstheglobalNDsnoopingstatistics.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
(Appliestothe6200,6300,6400,8360.)ShowingglobalNDsnoopingstatistics:
| switch(config)# | show   | nd-snooping | statistics |     |     |       |
| --------------- | ------ | ----------- | ---------- | --- | --- | ----- |
| PACKET-TYPE     | ACTION | REASON      |            |     |     | COUNT |
------------ -------- ----------------------------------------------- --------
| RA  | forward | RA packets | received | on trusted   | port | 20  |
| --- | ------- | ---------- | -------- | ------------ | ---- | --- |
| RA  | drop    | RA packets | received | on untrusted | port | 45  |
| NS  | forward | NS packets | received | on trusted   | port | 52  |
NDsnooping|186

|     | NS  |     | forward |     | NS packets | received | on untrusted   | port       |        | 95  |
| --- | --- | --- | ------- | --- | ---------- | -------- | -------------- | ---------- | ------ | --- |
|     | NS  |     | drop    |     | NS packets | failed   | MAC check      |            |        | 14  |
|     | NS  |     | drop    |     | NS packets | failed   | Prefix check   |            |        | 12  |
|     | NS  |     | drop    |     | NS packets | failed   | on max-binding | limit      |        | 0   |
|     | NS  |     | drop    |     | NS packets | failed   | ND snooping    | validation | checks | 20  |
|     | NA  |     | forward |     | NA packets | received | on trusted     | port       |        | 17  |
|     | NA  |     | forward |     | NA packets | received | on untrusted   | port       |        | 30  |
|     | NA  |     | drop    |     | NA packets | failed   | Prefix check   |            |        | 15  |
|     | NA  |     | drop    |     | NA packets | failed   | on max-binding | limit      |        | 2   |
|     | NA  |     | drop    |     | NA packets | failed   | ND snooping    | validation | checks | 5   |
(Appliestothe8325,9300,10000.)ShowingglobalNDsnoopingstatistics:
|     | switch(config)# |     | show   | nd-snooping |        | statistics |     |     |     |       |
| --- | --------------- | --- | ------ | ----------- | ------ | ---------- | --- | --- | --- | ----- |
|     | PACKET-TYPE     |     | ACTION |             | REASON |            |     |     |     | COUNT |
------------ -------- ----------------------------------------------- --------
|                | RA  |             | forward |         | RA packets | received                                        | on trusted   | port |     | 20  |
| -------------- | --- | ----------- | ------- | ------- | ---------- | ----------------------------------------------- | ------------ | ---- | --- | --- |
|                | RA  |             | drop    |         | RA packets | received                                        | on untrusted | port |     | 45  |
|                | RR  |             | forward |         | RR packets | received                                        | on trusted   | port |     | 20  |
|                | RR  |             | drop    |         | RR packets | received                                        | on untrusted | port |     | 45  |
| Command        |     | History     |         |         |            |                                                 |              |      |     |     |
| Release        |     |             |         |         |            | Modification                                    |              |      |     |     |
| 10.10          |     |             |         |         |            | Addedsupportforthe8360.                         |              |      |     |     |
| 10.09          |     |             |         |         |            | Addedsupportforthe8325.Addedsupportforthe10000. |              |      |     |     |
| 10.07orearlier |     |             |         |         |            | --                                              |              |      |     |     |
| Command        |     | Information |         |         |            |                                                 |              |      |     |     |
| Platforms      |     |             | Command | context |            | Authority                                       |              |      |     |     |
8325 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
8360 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 9300 |     |     |     |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
10000
| RA  | guard | policy |     | commands |     |     |     |     |     |     |
| --- | ----- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- |
hop limit
| hop | limit     | [minimum | |   | maximum]   | <HOP-LIMIT> |             |     |     |     |     |
| --- | --------- | -------- | --- | ---------- | ----------- | ----------- | --- | --- | --- | --- |
| no  | hop limit | [minimum |     | | maximum] |             | <HOP-LIMIT> |     |     |     |     |
Description
EnablesverificationoftheadvertisedhopcountlimitiftheRAguardpolicyisappliedonaVLANor
interface.RApacketswiththehoplimitwithinthespecifiedminimumandmaximumvaluesare
processed.Ifnoneofthevaluesarespecifiedforhoplimit,thedefaultrangeis1-255.Ifhoplimitisnot
enabled,packetsarenotvalidatedforhoplimit.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 187

ThenoformofthecommanddisablesthehoplimitonthespecifiedRAguardpolicy.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter   |     |     |     | Description                             |     |
| ----------- | --- | --- | --- | --------------------------------------- | --- |
| <HOP-LIMIT> |     |     |     | Specifiesthehop-limitvalue.Range:1-255. |     |
minimum
Specifiestheminimumvalueforthehop-limitrange.Default:1,
Range1-255.
Therangeisminimum–255ifonlyaminimumvalueisspecified.
maximum Specifiesthemaximumvalueforthehop-limitrange.Default:
255,Range1-255.
Therangeis1–maximumifonlyamaximumvalueisspecified.
Examples
EnablingthehoplimitontheRAguardpolicyandaddingminimumandmaximumvaluesforhoplimit
onthepolicy:
| switch(config)#                | ipv6 | nd-snooping | ra-guard  |     | policy <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | --------- | --- | -------------------- |
| switch(config-raguard-policy)# |      |             | hop-limit |     | enable               |
| switch(config-raguard-policy)# |      |             | hop-limit |     | maximum 150          |
| switch(config-raguard-policy)# |      |             | hop-limit |     | minimum 50           |
DisablingthehoplimitontheRAguardpolicy:
| switch(config)#                | ipv6 | nd-snooping | ra-guard |           | policy <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | -------- | --------- | -------------------- |
| switch(config-raguard-policy)# |      |             | no       | hop-limit | enable               |
RemovingminimumandmaximumvaluesforthehoplimitontheRAguardpolicy:
| switch(config)#                | ipv6    | nd-snooping | ra-guard           |           | policy <POLICY-NAME> |
| ------------------------------ | ------- | ----------- | ------------------ | --------- | -------------------- |
| switch(config-raguard-policy)# |         |             | no                 | hop-limit | maximum 150          |
| switch(config-raguard-policy)# |         |             | no                 | hop-limit | minimum 50           |
| switch(config-raguard-policy)# |         |             | no                 | hop-limit | maximum              |
| switch(config-raguard-policy)# |         |             | no                 | hop-limit | minimum              |
| Command History                |         |             |                    |           |                      |
| Release                        |         |             | Modification       |           |                      |
| 10.10                          |         |             | Commandintroduced. |           |                      |
| Command Information            |         |             |                    |           |                      |
| Platforms                      | Command | context     |                    | Authority |                      |
8360 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
NDsnooping|188

| ipv6 nd-snooping    |     |          | ra-guard | policy        |     |
| ------------------- | --- | -------- | -------- | ------------- | --- |
| ipv6 nd-snooping    |     | ra-guard | policy   | <POLICY-NAME> |     |
| no ipv6 nd-snooping |     | ra-guard | policy   | <POLICY-NAME> |     |
Description
CreatestheRouterAdvertisement(RA)guardpolicywiththegivennameandenterstheRAguardpolicy
configurationcontext.
ThenoformofthecommandremovesthespecifiedRAguardpolicyfromtheswitch.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<POLICY-NAME>
SpecifiesthenameoftheRAguardpolicy.Maximumlength:64.
Examples
CreatingtheRAguardpolicygloballywithaspecifiedname:
switch(config)#
|     |     | ipv6 | nd-snooping | ra-guard policy | <POLICY-NAME> |
| --- | --- | ---- | ----------- | --------------- | ------------- |
switch(config-raguard-policy)#
DeletingthespecifiedRAguardpolicy:
switch(config)# no ipv6 nd-snooping ra-guard policy <POLICY-NAME>
| Command History     |         |     |         |                    |     |
| ------------------- | ------- | --- | ------- | ------------------ | --- |
| Release             |         |     |         | Modification       |     |
| 10.10               |         |     |         | Commandintroduced. |     |
| Command Information |         |     |         |                    |     |
| Platforms           | Command |     | context | Authority          |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
managed-config-flag
| managed-config-flag    |     | [on | | off]     |     |     |
| ---------------------- | --- | --- | ---------- | --- | --- |
| no managed-config-flag |     |     | [on | off] |     |     |
Description
Enablestheverificationoftheadvertisedmanageconfigurationflag.Verifiesthattheadvertised
managedaddressconfigurationflagisOnorOffbasedontheconfiguredvalue.
Thenoformofthecommanddisablesthemanageconfigurationflagverification.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 189

NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
on Verifiesthattheadvertisedmanagedaddressconfigurationflagis
On.
off Verifiesthattheadvertisedmanagedaddressconfigurationflagis
Off.
Examples
Enablingmanagedconfigurationflagverification:
| switch(config)#                | ipv6 | nd-snooping | ra-guard policy     | <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | ------------------- | ------------- |
| switch(config-raguard-policy)# |      |             | managed-config-flag | off           |
| switch(config-raguard-policy)# |      |             | managed-config-flag | on            |
Disablingmanagedconfigurationflagverification:
| switch(config)#                | ipv6    | nd-snooping | ra-guard policy        | <POLICY-NAME> |
| ------------------------------ | ------- | ----------- | ---------------------- | ------------- |
| switch(config-raguard-policy)# |         |             | no managed-config-flag |               |
| switch(config-raguard-policy)# |         |             | no managed-config-flag | off           |
| switch(config-raguard-policy)# |         |             | no managed-config-flag | on            |
| Command History                |         |             |                        |               |
| Release                        |         |             | Modification           |               |
| 10.10                          |         |             | Commandintroduced.     |               |
| Command Information            |         |             |                        |               |
| Platforms                      | Command | context     | Authority              |               |
8360 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
match access-list
| match access-list    | <ACL-NAME> |     |     |     |
| -------------------- | ---------- | --- | --- | --- |
| no match access-list | <ACL-NAME> |     |     |     |
Description
ConfigurestheaccesslisttoanRAguardpolicy.Theaccesslisthastobecreatedwiththedesiredmatch
criteriabeforeaddingitintoRAguardpolicy.Advertisedpacketsareverifiedforthematchcriteriawhen
anRAguardpolicywithmatchedaccesslistisenabledonatrustedportorVLANs.
ThenoformofthecommandremovestheaccesslistfromtheRAguardpolicy.
NDsnooping|190

NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter  |     |     | Description                                 |     |
| ---------- | --- | --- | ------------------------------------------- | --- |
| <ACL-NAME> |     |     | Specifiesthenameoftheaccesslisttobematched. |     |
Examples
AddinganaccesslistnamedExample_ACLtotheRAguardpolicyPOL1:
| switch(config)#                | ipv6 | nd-snooping | ra-guard policy   | POL1        |
| ------------------------------ | ---- | ----------- | ----------------- | ----------- |
| switch(config-raguard-policy)# |      |             | match access-list | Example_ACL |
DeletingtheaccesslistnamedExample_ACLfromtheRAguardpolicyPOL1:
| switch(config)# | ipv6 | nd-snooping | ra-guard policy | POL1 |
| --------------- | ---- | ----------- | --------------- | ---- |
switch(config-raguard-policy)# no match access-list Example_ACL
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.10               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
8360 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
match prefix-list
| match prefix-list    | <PREFIX-LIST-NAME> |     |     |     |
| -------------------- | ------------------ | --- | --- | --- |
| no match prefix-list | <PREFIX-LIST-NAME> |     |     |     |
Description
Configuresaprefix-listfortheRAguardpolicy.AdvertisedprefixesinRApacketsarecomparedagainst
theconfiguredprefix-listandifthereisnomatch,theRApacketsaredropped.IftheRAprefixlistisnot
configured,thischeckisnotperformed.
ThenoformofthecommandremovestheprefixlistfromtheRAguardpolicy.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 191

| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<PREFIX-LIST-NAME> Specifiesthenameoftheprefixlisttobematched.
Examples
AddingaprefixlistnamedPREFIX_LIST_EXAMPLEtothePOLICY1RAguardpolicy:
| switch(config)# |     | ipv6 nd-snooping |     | ra-guard | policy | POLICY1 |
| --------------- | --- | ---------------- | --- | -------- | ------ | ------- |
switch(config-raguard-policy)# match prefix-list PREFIX_LIST_EXAMPLE
DeletingtheprefixlistnamedPREFIX_LIST_EXAMPLEfromthePOLICY1RAguardpolicy:
| switch(config)# |     | ipv6 nd-snooping |     | ra-guard | policy | POLICY1 |
| --------------- | --- | ---------------- | --- | -------- | ------ | ------- |
switch(config-raguard-policy)# no match pefix-list PREFIX_LIST_EXAMPLE
| Command   | History     |     |         |                    |           |     |
| --------- | ----------- | --- | ------- | ------------------ | --------- | --- |
| Release   |             |     |         | Modification       |           |     |
| 10.10     |             |     |         | Commandintroduced. |           |     |
| Command   | Information |     |         |                    |           |     |
| Platforms | Command     |     | context |                    | Authority |     |
8360 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| nd-snooping    |          | ra-guard      | attach-policy |               |               |     |
| -------------- | -------- | ------------- | ------------- | ------------- | ------------- | --- |
| nd-snooping    | ra-guard | attach-policy |               | <POLICY-NAME> |               |     |
| no nd-snooping | ra-guard | attach-policy |               |               | <POLICY-NAME> |     |
Description
AppliesthecreatedRAguardpolicytoaspecificL2portorVLAN.
ThenoformofthecommanddetachesthespecifiedRAguardpolicyfromtheL2portorVLAN.
| Parameter     |     |     |     | Description                         |     |     |
| ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
| <POLICY-NAME> |     |     |     | SpecifiesthenameoftheRAguardpolicy. |     |     |
Usage
Intheinterfaceconfiguration(config-if)context:
n RAguardmustbeenabledonmemberVLANsoftheportforwhichRApacketsneedtobeinspected
usingthepolicy.
Intheinterfaceconfiguration(config-if)andVLANconfiguration(config-vlan)contexts:
NDsnooping|192

n RA packetsreceivedonuntrustedportsaredroppedwithoutanyinspection.
n RA packetsreceivedontrustedportsarevalidatedagainstthepolicy.
TheappliedpolicytakeseffectonlyifNDsnoopingisenabledgloballyandbothND snoopingandRA
n
guardareenabledundertheVLANcontext.
PolicyprecedencebetweenVLANandport:
n IfthepolicyisattachedtobothVLANandport,theportpolicytakesprecedenceovertheVLANpolicy.
n OnlyonepolicycanbeattachedperVLANorport.
n IftheportbelongstoadifferentVLAN(forexample,inthecaseofatrunkport)thetaggedVLAN
takespriority.Ifthepacketsareuntagged,thenativeVLANpolicytakesprecedence.
Examples
AttachingtheRAguardpolicytoanL2port:
| switch(config)# |     | interface | 1/1/10 |     |
| --------------- | --- | --------- | ------ | --- |
switch(config-if)# nd-snooping ra-guard attach-policy POLICY_NAME
AttemptingtoattachtheRAguardpolicytoaportwhereroutingisenabled,thepolicyisnotconfigured,
oritisanuntrustedport:
(Whenprompted,enter"Y"tocreatethepolicyandattachittotheinterface.)
| switch(config)# |     | interface | 1/1/10 |     |
| --------------- | --- | --------- | ------ | --- |
switch(config-if)# nd-snooping ra-guard attach-policy POLICY_NAME
RA Guard policy can't be attached to an interface with routing enabled.
| switch(config-if)# |     | no routing  |       |     |
| ------------------ | --- | ----------- | ----- | --- |
| switch(config-if)# |     | nd-snooping | trust |     |
switch(config-if)# nd-snooping ra-guard attach-policy POLICY_NAME
switch(config-if)#6300(config-if)# nd-snooping ra-guard attach-policy POLICY_NOT_
CREATED
| RA guard           | policy    | does not    | exist.                 |     |
| ------------------ | --------- | ----------- | ---------------------- | --- |
| Do you want        | to create | (y/n)?      |                        |     |
| switch(config)#    |           | interface   | 1/1/10                 |     |
| switch(config-if)# |           | nd-snooping | ra-guard attach-policy | AA  |
RA Guard policy is ineffective, as 1/1/10 is configured as untrusted port.
AttachingtheRAguardpolicytoaVLAN:
switch(config)#
|     |     | vlan 10 |     |     |
| --- | --- | ------- | --- | --- |
switch(config-vlan-10)# nd-snooping ra-guard attach-policy POLICY_NAME
DetachingtheRAguardpolicy:
| switch(config)# |     | interface | 1/1/10 |     |
| --------------- | --- | --------- | ------ | --- |
switch(config-if)# no nd-snooping ra-guard attach-policy POLICY_NAME
AttemptingtodetachaRAguardpolicywhichisnotappliedontheportorVLAN:
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 193

| switch(config)# |     | interface |     | 1/1/10 |     |     |     |     |
| --------------- | --- | --------- | --- | ------ | --- | --- | --- | --- |
switch(config-if)#
|          |        |             | no nd-snooping |     | ra-guard    | attach-policy |            | POLICY_NAME |
| -------- | ------ | ----------- | -------------- | --- | ----------- | ------------- | ---------- | ----------- |
| RA Guard | Policy | POLICY_NAME |                | is  | not applied | on            | this port. |             |
Attemptingtodetachanon-existentRAguardpolicy:
switch(config-if)# no nd-snooping ra-guard attach-policy POLICY_NOT_CREATED
| Could not | find        | the | policy  | POLICY_NOT_CREATED. |                    |     |     |     |
| --------- | ----------- | --- | ------- | ------------------- | ------------------ | --- | --- | --- |
| Command   | History     |     |         |                     |                    |     |     |     |
| Release   |             |     |         |                     | Modification       |     |     |     |
| 10.10     |             |     |         |                     | Commandintroduced. |     |     |     |
| Command   | Information |     |         |                     |                    |     |     |     |
| Platforms | Command     |     | context |                     | Authority          |     |     |     |
config-if
| 8360 |                       |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |     |
| ---- | --------------------- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
|      | config-vlan-<VLAN-ID> |     |     |     | rightsforthiscommand.                              |     |     |     |
other-config-flag
| other-config-flag    |     | [on | | off] |     |     |     |     |     |
| -------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
| no other-config-flag |     | [on | | off] |     |     |     |     |     |
Description
Enablestheverificationoftheadvertisedotherconfigurationflag.VerifiesthattheadvertisedOther
StatefulConfigurationflagisOnorOffbasedontheconfiguredvalue.
Thenoformofthecommanddisablesotherconfigurationflagverification.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
on VerifiesthattheadvertisedOtherStatefulConfigurationflagisOn.
off VerifiesthattheadvertisedOtherStatefulConfigurationflagis
Off.
Examples
Enablingotherconfigurationflagverification:
| switch(config)#                |     | ipv6 | nd-snooping |     | ra-guard          | policy | <POLICY-NAME> |     |
| ------------------------------ | --- | ---- | ----------- | --- | ----------------- | ------ | ------------- | --- |
| switch(config-raguard-policy)# |     |      |             |     | other-config-flag |        | off           |     |
| switch(config-raguard-policy)# |     |      |             |     | other-config-flag |        | on            |     |
NDsnooping|194

Disablingotherconfigurationflagverification:
| switch(config)#                |         | ipv6 nd-snooping | ra-guard           | policy            | <POLICY-NAME> |
| ------------------------------ | ------- | ---------------- | ------------------ | ----------------- | ------------- |
| switch(config-raguard-policy)# |         |                  | no                 | other-config-flag |               |
| switch(config-raguard-policy)# |         |                  | no                 | other-config-flag | off           |
| switch(config-raguard-policy)# |         |                  | no                 | other-config-flag | on            |
| Command History                |         |                  |                    |                   |               |
| Release                        |         |                  | Modification       |                   |               |
| 10.10                          |         |                  | Commandintroduced. |                   |               |
| Command Information            |         |                  |                    |                   |               |
| Platforms                      | Command | context          |                    | Authority         |               |
8360 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
router-preference
| router-preference    |     | {high | medium | | low} |      |     |
| -------------------- | --- | -------------- | ------ | ---- | --- |
| no router-preference |     | [high | medium | |      | low] |     |
Description
EnablestherouterpreferenceverificationontheRAguardpolicyforadvertisedpacketsandprocesses
thepacketsonlyiftherouterpreferenceislowerthantheconfiguredvalue.Iftherouterpreferenceis
notconfigured,thisvalidationisbypassed.
ThenoformofthiscommanddisablesrouterpreferenceverificationontheRAguardpolicy.
| Parameter |     |     | Description                             |     |     |
| --------- | --- | --- | --------------------------------------- | --- | --- |
| high      |     |     | Setsthemaximumrouterpreferencetohigh.   |     |     |
| medium    |     |     | Setsthemaximumrouterpreferencetomedium. |     |     |
| low       |     |     | Setsthemaximumrouterpreferencetolow.    |     |     |
Examples
Enablingrouterpreferenceverificationwiththemaximumrouterpreferencesettohigh:
| switch(config)#                |     | ipv6 nd-snooping | ra-guard          | policy | <POLICY-NAME> |
| ------------------------------ | --- | ---------------- | ----------------- | ------ | ------------- |
| switch(config-raguard-policy)# |     |                  | router-preference |        | high          |
Disablingrouterpreferenceverification:
| switch(config)#                |     | ipv6 nd-snooping | ra-guard | policy            | <POLICY-NAME> |
| ------------------------------ | --- | ---------------- | -------- | ----------------- | ------------- |
| switch(config-raguard-policy)# |     |                  | no       | router-preference |               |
| Command History                |     |                  |          |                   |               |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 195

| Release        |             |         |     |         | Modification       |           |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------------ | --------- | --- | --- |
| 10.10orearlier |             |         |     |         | Commandintroduced. |           |     |     |
| Command        | Information |         |     |         |                    |           |     |     |
| Platforms      |             | Command |     | context |                    | Authority |     |     |
8360 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | nd-snooping |          | ra-guard |           | interface      |     |     |     |
| ---- | ----------- | -------- | -------- | --------- | -------------- | --- | --- | --- |
| show | nd-snooping | ra-guard |          | interface | <INTERFACE-ID> |     |     |     |
Description
ShowsRAguardcountersforthespecifiedinterface.CountersareclearedoncetheRAguardpolicyis
detachedfromtheinterface.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-ID> SpecifiestheinterfaceforwhichtheRAguardcountersare
displayed.
Examples
ShowingRAguardcountersforinterface1/1/1:
|     | switch# show | nd-snooping |          | ra-guard |     | interface | 1/1/1 |     |
| --- | ------------ | ----------- | -------- | -------- | --- | --------- | ----- | --- |
|     | RA Guard     | Policy      | Counters |          |     |           |       |     |
========================
|         | RA Guard    | Policy    | Applied |        | :                  | POLICY_2   |                     |     |
| ------- | ----------- | --------- | ------- | ------ | ------------------ | ---------- | ------------------- | --- |
|         | RA Packets  | Received  |         |        | :                  | 10         |                     |     |
|         | RA Packets  | Forwarded |         |        | :                  | 5          |                     |     |
|         | RA Packets  | Dropped   |         |        | :                  | 5 [Total]  |                     |     |
|         |             |           |         | reason | :                  | Managed    | flag error          | [0] |
|         |             |           |         |        |                    | Other flag | error               | [0] |
|         |             |           |         |        |                    | Access     | list error          | [0] |
|         |             |           |         |        |                    | Prefix     | list error          | [0] |
|         |             |           |         |        |                    | Router     | preference error[0] |     |
|         |             |           |         |        |                    | Hop limit  | error               | [5] |
| Command | History     |           |         |        |                    |            |                     |     |
| Release |             |           |         |        | Modification       |            |                     |     |
| 10.10   |             |           |         |        | Commandintroduced. |            |                     |     |
| Command | Information |           |         |        |                    |            |                     |     |
NDsnooping|196

| Platforms | Command |     | context | Authority |     |     |
| --------- | ------- | --- | ------- | --------- | --- | --- |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show nd-snooping |          |     | ra-guard | policy          |     |     |
| ---------------- | -------- | --- | -------- | --------------- | --- | --- |
| show nd-snooping | ra-guard |     | policy   | [<POLICY-NAME>] |     |     |
Description
ShowstheRAguardpolicyconfiguration.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<POLICY-NAME> SpecifiesthenameoftheRAguardpolicytobedisplayed.
Examples
ShowingRAguardconfiguration:
| switch# show | nd-snooping |     | ra-guard | policy  |       |               |
| ------------ | ----------- | --- | -------- | ------- | ----- | ------------- |
| RA Guard     | Policy      |     |          | Applied | Ports | Applied VLANs |
----------------------------------------------------------------------------------
--------
| POLICY_NAME1 |             | 1/1/25,1/1/27,1/1/29-1/1/44,1/1/46 |          |        |              | 10,20,50-100 |
| ------------ | ----------- | ---------------------------------- | -------- | ------ | ------------ | ------------ |
| POLICY_NAME2 |             | 1/1/1-1/1/24                       |          |        |              |              |
| switch# show | nd-snooping |                                    | ra-guard | policy | POLICY_NAME1 |              |
| RA Guard     | policy      | Information                        |          |        |              |              |
========================
| Policy name    |       |     | :   | POLICY_NAME1                       |     |     |
| -------------- | ----- | --- | --- | ---------------------------------- | --- | --- |
| Policy Applied | Ports |     | :   | 1/1/25,1/1/27,1/1/29-1/1/44,1/1/46 |     |     |
| Policy Applied | VLANs |     | :   | 10,20,50-100                       |     |     |
| Hop Limit      |       |     | :   | enabled                            |     |     |
minimum : 50
maximum : 150
| Managed config      | flag |     | :   | On                 |     |     |
| ------------------- | ---- | --- | --- | ------------------ | --- | --- |
| Other config        | flag |     | :   | On                 |     |     |
| Access List         |      |     | :   | ACL1               |     |     |
| Prefix List         |      |     | :   | PREFIX_LIST_NAME   |     |     |
| Router Preference   |      |     | :   | high               |     |     |
| Command History     |      |     |     |                    |     |     |
| Release             |      |     |     | Modification       |     |     |
| 10.10               |      |     |     | Commandintroduced. |     |     |
| Command Information |      |     |     |                    |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 197

| Platforms |     | Command |     | context | Authority |     |     |     |
| --------- | --- | ------- | --- | ------- | --------- | --- | --- | --- |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | nd-snooping |          | ra-guard |                 | vlan |     |     |     |
| ---- | ----------- | -------- | -------- | --------------- | ---- | --- | --- | --- |
| show | nd-snooping | ra-guard |          | vlan <VLAN-ID>] |      |     |     |     |
Description
ShowsRAguardcountersforthespecifiedVLAN.CountersareclearedoncetheRAguardpolicyis
detachedfromtheVLAN.
| Parameter |     |     |     |     | Description                                   |     |     |     |
| --------- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- |
| <VLAN-ID> |     |     |     |     | SpecifiesaVLANIDforwhichtheRAguardcountersare |     |     |     |
displayed.Range:1to4094.
Examples
ShowingRAguardcountersforVLAN2:
|     | switch# show | nd-snooping |          | ra-guard | vlan | 2   |     |     |
| --- | ------------ | ----------- | -------- | -------- | ---- | --- | --- | --- |
|     | RA Guard     | Policy      | Counters |          |      |     |     |     |
========================
|           | RA Guard    | Policy    | Applied |         | : POLICY_1         |         |                     |     |
| --------- | ----------- | --------- | ------- | ------- | ------------------ | ------- | ------------------- | --- |
|           | RA Packets  | Received  |         |         | : 20               |         |                     |     |
|           | RA Packets  | Forwarded |         |         | : 5                |         |                     |     |
|           | RA Packets  | Dropped   |         |         | : 15               | [Total] |                     |     |
|           |             |           |         | reason  | : Managed          |         | flag error          | [1] |
|           |             |           |         |         | Other              | flag    | error               | [4] |
|           |             |           |         |         | Access             |         | list error          | [1] |
|           |             |           |         |         | Prefix             |         | list error          | [4] |
|           |             |           |         |         | Router             |         | preference error[0] |     |
|           |             |           |         |         | Hop                | limit   | error               | [5] |
| Command   | History     |           |         |         |                    |         |                     |     |
| Release   |             |           |         |         | Modification       |         |                     |     |
| 10.10     |             |           |         |         | Commandintroduced. |         |                     |     |
| Command   | Information |           |         |         |                    |         |                     |     |
| Platforms |             | Command   |         | context | Authority          |         |                     |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
NDsnooping|198

Chapter 8
IPv6 destination guard
| IPv6 destination |     | guard |     |     |     |     |
| ---------------- | --- | ----- | --- | --- | --- | --- |
EnablingIPv6destinationguardonaswitchpreventsNDcachedepletionissuesandhelpsinminimizing
Denial-of-Service(DoS)attacks.WhenIPv6destinationguardisenabledaddressresolutionisperformed
onlyforthedestinationaddressesthatareactiveonthelink.
ThisfeaturerequiresthebindingtabletobepopulatedwiththehelpofDHCPv6snooping,NDsnooping,
orstatic-ip-bindings.DestinationguardenablesthedestinationaddressbasedfilteringofIPv6trafficand
blockstheNeighborDiscovery(ND)protocolresolutionfordestinationaddressesthatarenotfoundin
thebindingtable.
| IPv6 destination |                   |     | guard      | commands |                |      |
| ---------------- | ----------------- | --- | ---------- | -------- | -------------- | ---- |
| clear ipv6       | destination-guard |     |            |          | statistics     | vlan |
| clear ipv6       | destination-guard |     | statistics |          | vlan <VLAN-ID> |      |
Description
ClearsIPv6destinationguardstatisticsfromthespecifiedVLAN.
| Command   | context |     |     |     |             |     |
| --------- | ------- | --- | --- | --- | ----------- | --- |
| Parameter |         |     |     |     | Description |     |
vlan <VLAN-ID> SpecifiestheVLANforwhichalldestinationguardstatisticsareto
becleared.Range:1to4094.
Examples
Clearingallipv6destination-guardstatisticsforVLAN10:
| switch#   | clear       | ipv6    | destination-guard |     | statistics         | vlan 10 |
| --------- | ----------- | ------- | ----------------- | --- | ------------------ | ------- |
| Command   | History     |         |                   |     |                    |         |
| Release   |             |         |                   |     | Modification       |         |
| 10.10     |             |         |                   |     | Commandintroduced. |         |
| Command   | Information |         |                   |     |                    |         |
| Platforms |             | Command | context           |     | Authority          |         |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
199
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries)

| ipv6 destination |     | guard |     |     |
| ---------------- | --- | ----- | --- | --- |
ipv6 destination-guard
| no ipv6 | destination-guard |     |     |     |
| ------- | ----------------- | --- | --- | --- |
Description
EnablesIPv6destinationguardonaVLAN.
ThenoformofthecommandremovestheIPv6destinationguardfromaVLAN.
Toavoiddroppingvalidpacketswhendestinationguardisenabled,itisrecommendedtoconfigureDHCPv6
snoopingandNDsnoopingtopopulatethebindingdatabase.
Examples
EnablingIPv6destinationguardpolicyonaVLAN:
switch(config)#
vlan 10
| switch(config-vlan-10)# |     | ipv6 destination-guard |     |     |
| ----------------------- | --- | ---------------------- | --- | --- |
DisablingIPv6destinationguardpolicyonaVLAN:
| switch(config-vlan-10)# |             | no ipv6 | destination-guard  |     |
| ----------------------- | ----------- | ------- | ------------------ | --- |
| Command                 | History     |         |                    |     |
| Release                 |             |         | Modification       |     |
| 10.10                   |             |         | Commandintroduced. |     |
| Command                 | Information |         |                    |     |
| Platforms               | Command     | context | Authority          |     |
8360 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | ipv6 destination-guard |            | statistics       | vlan |
| --------- | ---------------------- | ---------- | ---------------- | ---- |
| show ipv6 | destination-guard      | statistics | {vlan <VLAN-ID>} |      |
Description
ShowsIPv6destinationguardstatisticsforthespecifiedVLAN.
| Command   | context |     |             |     |
| --------- | ------- | --- | ----------- | --- |
| Parameter |         |     | Description |     |
vlan <VLAN-ID>
SpecifiestheVLANforwhichalldestinationguardstatisicsareto
bedisplayed.Range:1to4094.
Examples
IPv6destinationguard|200

ShowingIPv6destination-guardstatisticsforVLAN10:
| switch# show    | ipv6 destination-guard |                 | statistics | vlan 10 |
| --------------- | ---------------------- | --------------- | ---------- | ------- |
| Packets dropped | for                    | VLAN 10 : 25467 |            |         |
ShowingIPv6destination-guardstatisticsforallVLANs:
| switch# show        | ipv6 destination-guard |                 | statistics         |     |
| ------------------- | ---------------------- | --------------- | ------------------ | --- |
| Packets dropped     | for                    | VLAN 10 : 25467 |                    |     |
| Packets dropped     | for                    | VLAN 30 : 434   |                    |     |
| Packets dropped     | for                    | VLAN 50 : 8767  |                    |     |
| Command History     |                        |                 |                    |     |
| Release             |                        |                 | Modification       |     |
| 10.10               |                        |                 | Commandintroduced. |     |
| Command Information |                        |                 |                    |     |
| Platforms           | Command                | context         | Authority          |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show ipv6                   | destination-guard |     |     |     |
| --------------------------- | ----------------- | --- | --- | --- |
| show ipv6 destination-guard |                   |     |     |     |
Description
Showstheipv6destination-guardconfiguration.
Examples
ShowingtheIPv6destination-guardconfiguration:
| switch# show           | ipv6 destination-guard |               |                    |     |
| ---------------------- | ---------------------- | ------------- | ------------------ | --- |
| IPv6 Destination-Guard |                        | information   |                    |     |
| Enabled VLANs          |                        | : 10,20,31-35 |                    |     |
| Command History        |                        |               |                    |     |
| Release                |                        |               | Modification       |     |
| 10.10                  |                        |               | Commandintroduced. |     |
| Command Information    |                        |               |                    |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 201

Platforms

Command context

Authority

8360

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

IPv6 destination guard | 202

Chapter 9

IP Tunnels

IP Tunnels

True point-to-point networks are not always possible in corporate networking environment. Many
networks deploy nontraditional methods of connection (for example, DSL or broadband) at remote sites
or branch offices. The branch office, telecommuter, or business traveler then becomes separated from
the corporate network. Some method of tunneling becomes imperative to connect all the network sites
together.

Virtual Private Networking (VPN) is often deployed to create private tunnels through the public network
system for passing data to remote sites. While VPN is sufficient for the average business traveler, it is not
a good solution for branch site connectivity. VPN configurations must include statically maintained
access lists to identify traffic through the tunnel. These access lists are often tedious to configure for
larger networks and are prone to errors.

VPNs do not permit multicast traffic to pass; therefore routing protocols such as Routing Information
Protocol (RIP) and Open Shortest Path First (OSPF) are no longer options for dynamic routing updates.
All new additions to the network topology must be manually added to the various configured access
lists. Without dynamic routing from one site to another, network management is severely hampered.
Network managers need their non-heterogeneous networks to function like traditional point-to-point
networks so that traditional management methods (once available only on point-to-point circuits) can
apply to the entire network.

The solution to these challenges is to use IP tunnels. An IP tunnel provides a virtual link between
endpoints on two different networks enabling data to be exchanged as if the endpoints were directly
connected on the same network. Traffic between the devices is isolated from the intervening networks
that the tunnel spans.

For example, the following diagram shows an IP tunnel (using GRE) that connects two IPv4 networks
over an IPv4 network.

If network 1 and network 3 are using IPv6 addressing, the tunnel connects them by encapsulating the
IPv6 traffic in IPv4 packets to traverse network 2. The intermediate network devices do not know about
Network 1 and Network 2 because the packets are encapsulated.

An IP tunnel can also be used to create a point-to-point link for IPv6 traffic over an IPv6 network.

IP tunnels supported features

n Up to 127 tunnels can be defined on a switch shared between different tunnel types: GRE, IPv6 in

IPv4, and IPv6 in IPv6.

n A maximum of 16 source IP addresses are supported. Tunnels can have the same source IP address
and different destination IP addresses. The source IP, destination IP, and VRF combine to uniquely
identify a tunnel.

Unsupported features

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

203

n GREIPv4overIPv6.
n QoScannotbeappliedtoaGREtunnelinterface.
Keysupportcanbeaddedforsecurityandidentificationpurposeswhentherearemultiple
n
applications.
n VPNacrosspublicIPnetwork.
MPLSoverGRE.
n
n MultipointGREforscalablenetworktoreachmultipleremotesites.
| Configuring |     | an IP | tunnel |     |     |     |     |     |
| ----------- | --- | ----- | ------ | --- | --- | --- | --- | --- |
Prerequisites
Anenabledlayer3interfacewithanIPaddressassignedtoit,createdwiththecommandinterface.
Procedure
| 1. CreateanIPtunnelwiththecommandinterface |     |     |     |     |     | tunnel. |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------- | --- | --- |
2. SettheIPaddressforthetunnel.ForaGREtunnel,enterthecommandip address.ForanIPv6
| inIPv4oranIPv6inIPv6tunnel,enterthecommandipv6 |     |     |     |     |     |     | address. |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- |
3. SetthesourceIPaddressforthetunnel.ForaGREoranIPv6inIPv4tunnel,enterthecommand
| source | ip.ForanIPv6inIPv6tunnel,enterthecommandsource |     |     |     |     |     | ipv6. |     |
| ------ | ---------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- |
4. SetthedestinationIPaddressforthetunnel.ForaGREoranIPv6inIPv4tunnel,enterthe
commanddestination ip.ForanIPv6inIPv6tunnel,enterthecommanddestination ipv6.
5. Optionally,settheTTL(hopcount)forthetunnelwiththecommandttl.
| 6. Optionally,settheMTUforthetunnelwiththecommandip |     |     |     |     |     |     | mtu. |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- |
7. Optionally,addadescriptiontothetunnelwiththecommanddescription.
8. Bydefault,thetunnelisattachedtothedefaultVRF.AttachittoadifferentVRFwiththe
| commandvrf                                 |     | attach. |     |     |           |           |         |     |
| ------------------------------------------ | --- | ------- | --- | --- | --------- | --------- | ------- | --- |
| 9. Enablethetunnelwiththecommandno         |     |         |     |     | shutdown. |           |         |     |
| 10. Reviewtunnelsettingswiththecommandshow |     |         |     |     |           | interface | tunnel. |     |
Example
Thisexamplecreatesthefollowingconfiguration:
n CreatesGREtunnel33.
n SetthetunnelIPaddressto10.10.20.209/24.
n SetsthetunnelsourceIPaddressto10.10.10.1.
n SetsthetunneldestinationIPaddressto10.10.10.2.
n Enablesthetunnel.
| switch(config)#        |     | interface | tunnel     |     | 33 mode         | gre ipv4 |     |     |
| ---------------------- | --- | --------- | ---------- | --- | --------------- | -------- | --- | --- |
| switch(config-gre-if)# |     |           | ip address |     | 10.10.20.209/24 |          |     |     |
switch(config-gre-if)#
|                        |     |            | source      | ip  | address    | 10.10.10.1 |          |         |
| ---------------------- | --- | ---------- | ----------- | --- | ---------- | ---------- | -------- | ------- |
| switch(config-gre-if)# |     |            | destination |     | ip address | 10.10.10.2 |          |         |
| switch(config-gre-if)# |     |            | no shutdown |     |            |            |          |         |
| Creating               | a   | GRE tunnel |             | for | traversing |            | a public | network |
IPTunnels |204

ThisexamplecreatesaGREtunnelbetweentwoswitches,enablingtrafficfromtwonetworkstotraverse
apublicnetwork.
Procedure
1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress10.1.1.1/24toit.
switch# config
| switch(config)#    | interface | 1/1/1    |             |     |
| ------------------ | --------- | -------- | ----------- | --- |
| switch(config-if)# | ip        | address  | 10.1.1.1/24 |     |
| switch(config-if)# | no        | shutdown |             |     |
b. Enableinterface1/1/2andassigntheIPaddress180.1.10.2/24toit.
switch# config
| switch(config)#    | interface | 1/1/2    |               |     |
| ------------------ | --------- | -------- | ------------- | --- |
| switch(config-if)# | ip        | address  | 180.1.10.2/24 |     |
| switch(config-if)# | no        | shutdown |               |     |
| switch(config-if)# | exit      |          |               |     |
c. CreateGREtunnel10andassigntheIPaddress192.168.10.1/24,sourceaddress10.1.1.1,
anddestinationaddress20.1.1.1toit.
| switch(config)#        | interface | tunnel      |     | 10 mode gre ipv4 |
| ---------------------- | --------- | ----------- | --- | ---------------- |
| switch(config-gre-if)# |           | ip address  |     | 192.168.10.1/24  |
| switch(config-gre-if)# |           | source      | ip  | 10.1.1.1         |
| switch(config-gre-if)# |           | destination |     | ip 20.1.1.1      |
| switch(config-gre-if)# |           | no shutdown |     |                  |
| switch(config-gre-if)# |           | exit        |     |                  |
d. Definesroutessothattrafficfromnetwork1canreachnetwork2throughthetunnel.
| switch(config)# | ip route | 20.1.1.0/24   |     | 10.1.1.2 |
| --------------- | -------- | ------------- | --- | -------- |
| switch(config)# | ip route | 190.1.10.0/24 |     | tunnel10 |
2. Onswitch2:
a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit.
switch# config
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|                    | ip  | address  | 20.1.1.1/24 |     |
| ------------------ | --- | -------- | ----------- | --- |
| switch(config-if)# | no  | shutdown |             |     |
b. Enableinterface1/1/2andassigntheIPaddress190.1.10.2/24toit.
| switch(config)#    | interface | 1/1/2    |               |     |
| ------------------ | --------- | -------- | ------------- | --- |
| switch(config-if)# | ip        | address  | 190.1.10.2/24 |     |
| switch(config-if)# | no        | shutdown |               |     |
| switch(config-if)# | exit      |          |               |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 205

c. CreateGREtunnel10andassigntheIPaddress192.168.10.2/24,sourceaddress20.1.1.1,
anddestinationaddress10.1.1.1toit.
|     | switch(config)#        | interface | tunnel      |     | 10 mode gre     | ipv4 |
| --- | ---------------------- | --------- | ----------- | --- | --------------- | ---- |
|     | switch(config-gre-if)# |           | ip address  |     | 192.168.10.2/24 |      |
|     | switch(config-gre-if)# |           | source      | ip  | 20.1.1.1        |      |
|     | switch(config-gre-if)# |           | destination |     | ip 10.1.1.1     |      |
|     | switch(config-gre-if)# |           | no shutdown |     |                 |      |
|     | switch(config-gre-if)# |           | exit        |     |                 |      |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
|          | switch(config)# | ip route | 10.1.1.0/24   |     | 20.1.1.2  |             |
| -------- | --------------- | -------- | ------------- | --- | --------- | ----------- |
|          | switch(config)# | ip route | 180.1.10.0/24 |     | tunnel10  |             |
| Creating | two GRE         | tunnels  |               | to  | different | destination |
addresses
ThisexamplecreatestwoGREtunnelstodifferentdestinationaddresses.Trafficfromnetwork1can
reacheithernetwork2ornetwork3usingtheappropriatetunnel.
Procedure
IPTunnels |206

1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress10.1.1.1/24toit.
switch# config
| switch(config)#    | interface | 1/1/1    |             |     |
| ------------------ | --------- | -------- | ----------- | --- |
| switch(config-if)# | ip        | address  | 10.1.1.1/24 |     |
| switch(config-if)# | no        | shutdown |             |     |
b. Enableinterface1/1/2andassigntheIPaddress180.1.10.2/24toit.
switch# config
| switch(config)#    | interface | 1/1/2    |               |     |
| ------------------ | --------- | -------- | ------------- | --- |
| switch(config-if)# | ip        | address  | 180.1.10.2/24 |     |
| switch(config-if)# | no        | shutdown |               |     |
| switch(config-if)# | exit      |          |               |     |
c. Enableinterface1/1/3andassigntheIPaddress30.1.1.1/24toit.
switch# config
| switch(config)#    | interface   | 1/1/3    |     |     |
| ------------------ | ----------- | -------- | --- | --- |
| switch(config-if)# | 30.1.1.1/24 |          |     |     |
| switch(config-if)# | no          | shutdown |     |     |
| switch(config-if)# | exit        |          |     |     |
d. CreateGREtunnel10andassigntheIPaddress192.168.10.1/24,sourceaddress10.1.1.1,
anddestinationaddress20.1.1.1toit.
| switch(config)#        | interface | tunnel      |     | 10 mode gre ipv4 |
| ---------------------- | --------- | ----------- | --- | ---------------- |
| switch(config-gre-if)# |           | ip address  |     | 192.168.10.1/24  |
| switch(config-gre-if)# |           | source      | ip  | 10.1.1.1         |
| switch(config-gre-if)# |           | destination |     | ip 20.1.1.1      |
| switch(config-gre-if)# |           | no shutdown |     |                  |
| switch(config-gre-if)# |           | exit        |     |                  |
e. CreateGREtunnel20andassigntheIPaddress192.168.20.1/24,sourceaddress30.1.1.1,
anddestinationaddress40.1.1.1toit.
| switch(config)# | interface | tunnel |     | 20 mode gre ipv4 |
| --------------- | --------- | ------ | --- | ---------------- |
switch(config-gre-if)#
|                        |     | ip address  |     | 192.168.20.1/24 |
| ---------------------- | --- | ----------- | --- | --------------- |
| switch(config-gre-if)# |     | source      | ip  | 30.1.1.1        |
| switch(config-gre-if)# |     | destination |     | ip 40.1.1.1     |
| switch(config-gre-if)# |     | no shutdown |     |                 |
switch(config-gre-if)#
exit
f. Definesroutessothattrafficfromnetwork1canreachnetwork2throughtunnel10.
| switch(config)# | ip route | 20.1.1.0/24   |     | 10.1.1.2 |
| --------------- | -------- | ------------- | --- | -------- |
| switch(config)# | ip route | 190.1.10.0/24 |     | tunnel10 |
g. Definesroutessothattrafficfromnetwork1canreachnetwork3throughthetunnel20.
| switch(config)# | ip route | 40.1.1.0/24   |     | 30.1.1.2 |
| --------------- | -------- | ------------- | --- | -------- |
| switch(config)# | ip route | 200.1.10.0/24 |     | tunnel20 |
2. Onswitch2:
a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit.
switch# config
| switch(config)#    | interface | 1/1/1   |             |     |
| ------------------ | --------- | ------- | ----------- | --- |
| switch(config-if)# | ip        | address | 20.1.1.1/24 |     |
switch(config-if)#
no shutdown
b. Enableinterface1/1/2andassigntheIPaddress190.1.10.2/24toit.
| switch(config)#    | interface | 1/1/2    |               |     |
| ------------------ | --------- | -------- | ------------- | --- |
| switch(config-if)# | ip        | address  | 190.1.10.2/24 |     |
| switch(config-if)# | no        | shutdown |               |     |
| switch(config-if)# | exit      |          |               |     |
c. CreateGREtunnel10andassigntheIPaddress192.168.10.2/24,sourceaddress20.1.1.1,
anddestinationaddress10.1.1.1toit.
| switch(config)#        | interface | tunnel     |     | 10 mode gre ipv4 |
| ---------------------- | --------- | ---------- | --- | ---------------- |
| switch(config-gre-if)# |           | ip address |     | 192.168.10.2/24  |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 207

|     | switch(config-gre-if)# |     | source      | ip  | 20.1.1.1    |     |
| --- | ---------------------- | --- | ----------- | --- | ----------- | --- |
|     | switch(config-gre-if)# |     | destination |     | ip 10.1.1.1 |     |
|     | switch(config-gre-if)# |     | no shutdown |     |             |     |
switch(config-gre-if)#
exit
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughtunnel10.
|     | switch(config)# | ip route | 10.1.1.0/24   |     | 20.1.1.2 |     |
| --- | --------------- | -------- | ------------- | --- | -------- | --- |
|     | switch(config)# | ip route | 180.1.10.0/24 |     | tunnel10 |     |
3. Onswitch3:
|     | a. Enableinterface1/1/1andassigntheIPaddress40.1.1.1/24toit. |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
switch# config
|     | switch(config)#                                                | interface | 1/1/1    |             |     |     |
| --- | -------------------------------------------------------------- | --------- | -------- | ----------- | --- | --- |
|     | switch(config-if)#                                             | ip        | address  | 40.1.1.1/24 |     |     |
|     | switch(config-if)#                                             | no        | shutdown |             |     |     |
|     | b. Enableinterface1/1/2andassigntheIPaddress200.1.10.2/24toit. |           |          |             |     |     |
|     | switch(config)#                                                | interface | 1/1/2    |             |     |     |
switch(config-if)#
|     |                    | ip   | address  | 200.1.10.2/24 |     |     |
| --- | ------------------ | ---- | -------- | ------------- | --- | --- |
|     | switch(config-if)# | no   | shutdown |               |     |     |
|     | switch(config-if)# | exit |          |               |     |     |
c. CreateGREtunnel20andassigntheIPaddress192.168.20.2/24,sourceaddress40.1.1.1,
anddestinationaddress30.1.1.1toit.
|     | switch(config)#        | interface | tunnel      |     | 10 mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | --- | ---------------- | --- |
|     | switch(config-gre-if)# |           | ip address  |     | 192.168.20.2/24  |     |
|     | switch(config-gre-if)# |           | source      | ip  | 40.1.1.1         |     |
|     | switch(config-gre-if)# |           | destination |     | ip 30.1.1.1      |     |
|     | switch(config-gre-if)# |           | no shutdown |     |                  |     |
|     | switch(config-gre-if)# |           | exit        |     |                  |     |
d. Definesroutessothattrafficfromnetwork3canreachnetwork1throughtunnel20.
|          | switch(config)# | ip route | 30.1.1.0/24   |        | 40.1.1.2       |          |
| -------- | --------------- | -------- | ------------- | ------ | -------------- | -------- |
|          | switch(config)# | ip route | 180.1.10.0/24 |        | tunnel20       |          |
| Creating | an IPv6         | in       | IPv4          | tunnel | for traversing | a public |
network
ThisexamplecreatesanIPv6inIPv4tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
Procedure
IPTunnels |208

1. Onswitch1:
|     | a. Enableinterface1/1/1andassigntheIPaddress10.1.1.1/24toit. |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
switch# config
|     | switch(config)#                                             | interface |             | 1/1/1 |             |     |     |
| --- | ----------------------------------------------------------- | --------- | ----------- | ----- | ----------- | --- | --- |
|     | switch(config-if)#                                          |           | ip address  |       | 10.1.1.1/24 |     |     |
|     | switch(config-if)#                                          |           | no shutdown |       |             |     |     |
|     | b. Enableinterface1/1/2andassigntheIPaddress2080::2/64toit. |           |             |       |             |     |     |
switch# config
|     | switch(config)#    | interface |             | 1/1/2   |            |     |     |
| --- | ------------------ | --------- | ----------- | ------- | ---------- | --- | --- |
|     | switch(config-if)# |           | ipv6        | address | 2080::2/64 |     |     |
|     | switch(config-if)# |           | no shutdown |         |            |     |     |
|     | switch(config-if)# |           | exit        |         |            |     |     |
c. CreateIPv6inIPv4tunnel10andassigntheIPaddress2001:DB8::1/32,sourceaddress
10.1.1.1,anddestinationaddress20.1.1.1toit.
|     | switch(config)#       | interface |             | tunnel   | 10          | mode ip 6in4   |     |
| --- | --------------------- | --------- | ----------- | -------- | ----------- | -------------- | --- |
|     | switch(config-ip-if)# |           | ipv6        | address  |             | 2001:DB8::1/62 |     |
|     | switch(config-ip-if)# |           | source      |          | ip 10.1.1.1 |                |     |
|     | switch(config-ip-if)# |           | destination |          |             | ip 20.1.1.1    |     |
|     | switch(config-ip-if)# |           | no          | shutdown |             |                |     |
|     | switch(config-ip-if)# |           | exit        |          |             |                |     |
d. Definesroutessothattrafficfromnetwork1canreachnetwork2throughthetunnel.
|     | switch(config)# | ip   | route | 20.1.1.0/24 |     | 10.1.1.2 |     |
| --- | --------------- | ---- | ----- | ----------- | --- | -------- | --- |
|     | switch(config)# | ipv6 | route | 290::0/64   |     | tunnel10 |     |
2. Onswitch2:
|     | a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit. |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
switch# config
|     | switch(config)#                                             | interface |             | 1/1/1   |             |     |     |
| --- | ----------------------------------------------------------- | --------- | ----------- | ------- | ----------- | --- | --- |
|     | switch(config-if)#                                          |           | ip address  |         | 20.1.1.1/24 |     |     |
|     | switch(config-if)#                                          |           | no shutdown |         |             |     |     |
|     | b. Enableinterface1/1/2andassigntheIPaddress2090::2/64toit. |           |             |         |             |     |     |
|     | switch(config)#                                             | interface |             | 1/1/2   |             |     |     |
|     | switch(config-if)#                                          |           | ipv6        | address | 2090::2/64  |     |     |
|     | switch(config-if)#                                          |           | no shutdown |         |             |     |     |
|     | switch(config-if)#                                          |           | exit        |         |             |     |     |
c. CreateIPv6inIPv4tunnel10andassigntheIPaddress2001:DB8::2/32,sourceaddress
10.1.1.1,anddestinationaddress20.1.1.1toit.
switch(config)#
|     |                       | interface |             | tunnel  | 10          | mode ip 6in4   |     |
| --- | --------------------- | --------- | ----------- | ------- | ----------- | -------------- | --- |
|     | switch(config-ip-if)# |           | ipv6        | address |             | 2001:DB8::2/62 |     |
|     | switch(config-ip-if)# |           | source      |         | ip 20.1.1.1 |                |     |
|     | switch(config-ip-if)# |           | destination |         |             | ip 10.1.1.1    |     |
switch(config-ip-if)#
|     |                       |     | no   | shutdown |     |     |     |
| --- | --------------------- | --- | ---- | -------- | --- | --- | --- |
|     | switch(config-ip-if)# |     | exit |          |     |     |     |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
|          | switch(config)# | ip  | route | 10.1.1.0/24 |     | 20.1.1.2       |          |
| -------- | --------------- | --- | ----- | ----------- | --- | -------------- | -------- |
|          | switch(config)# | ip  | route | 2080::0/64  |     | tunnel10       |          |
| Creating | an IPv6         | in  | IPv6  | tunnel      |     | for traversing | a public |
network
ThisexamplecreatesanIPv6inIPv6tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 209

Procedure
1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress2001:DB8:5::1/64toit.
switch# config
| switch(config)#    | interface |             | 1/1/1   |                  |     |     |
| ------------------ | --------- | ----------- | ------- | ---------------- | --- | --- |
| switch(config-if)# |           | ipv6        | address | 2001:DB8:5::1/64 |     |     |
| switch(config-if)# |           | no shutdown |         |                  |     |     |
b. Enableinterface1/1/2andassigntheIPaddress2080::2/64toit.
switch# config
| switch(config)#    | interface |             | 1/1/2   |            |     |     |
| ------------------ | --------- | ----------- | ------- | ---------- | --- | --- |
| switch(config-if)# |           | ipv6        | address | 2080::2/64 |     |     |
| switch(config-if)# |           | no shutdown |         |            |     |     |
| switch(config-if)# |           | exit        |         |            |     |     |
c. CreateIPv6inIPv6tunnel10andassigntheIPaddress2001:DB8::1/32,sourceaddress
2001:DB8:5::1,anddestinationaddress2001:DB8:9::1toit.(Optional)SettheMTUandTTL
parametersforthistunnelinterface.
| switch(config)#       | interface |             | tunnel   | 10                 | mode           | ip 6in6 |
| --------------------- | --------- | ----------- | -------- | ------------------ | -------------- | ------- |
| switch(config-ip-if)# |           | ipv6        | address  |                    | 2001:DB8::1/62 |         |
| switch(config-ip-if)# |           | source      |          | ipv6 2001:DB8:5::1 |                |         |
| switch(config-ip-if)# |           | destination |          | ipv6               | 2001:DB8:9::1  |         |
| switch(config-ip-if)# |           | no          | shutdown |                    |                |         |
| switch(config-ip-if)# |           | exit        |          |                    |                |         |
d. Definesroutessothattrafficfromnetwork1canreachnetwork2throughthetunnel.
| switch(config)# | ipv6 | route | 2001:DB8:9::0/64 |     |          | 2001:DB8:5::2 |
| --------------- | ---- | ----- | ---------------- | --- | -------- | ------------- |
| switch(config)# | ipv6 | route | 2090::0/64       |     | tunnel10 |               |
2. Onswitch2:
a. Enableinterface1/1/1andassigntheIPaddress2001:DB8:9::1/64toit.
switch# config
| switch(config)#    | interface |             | 1/1/1   |                  |     |     |
| ------------------ | --------- | ----------- | ------- | ---------------- | --- | --- |
| switch(config-if)# |           | ipv6        | address | 2001:DB8:9::1/64 |     |     |
| switch(config-if)# |           | no shutdown |         |                  |     |     |
b. Enableinterface1/1/2andassigntheIPaddress2090::2/64toit.
| switch(config)#    | interface |             | 1/1/2   |            |     |     |
| ------------------ | --------- | ----------- | ------- | ---------- | --- | --- |
| switch(config-if)# |           | ipv6        | address | 2090::2/64 |     |     |
| switch(config-if)# |           | no shutdown |         |            |     |     |
| switch(config-if)# |           | exit        |         |            |     |     |
c. CreateIPv6inIPv6tunnel10andassigntheIPaddress2001:DB8::2/32,sourceaddress
2001:DB8:5::1,anddestinationaddress2001:DB8:9::1toit.(Optional)SettheMTUandTTL
IPTunnels |210

parametersforthistunnelinterface.
|     | switch(config)#       |     | interface |             | tunnel   | 10             | mode ip 6in6  |
| --- | --------------------- | --- | --------- | ----------- | -------- | -------------- | ------------- |
|     | switch(config-ip-if)# |     |           | ipv6        | address  | 2001:DB8::2/62 |               |
|     | switch(config-ip-if)# |     |           | source      | ipv6     | 2001:DB8:9::1  |               |
|     | switch(config-ip-if)# |     |           | destination |          | ipv6           | 2001:DB8:5::1 |
|     | switch(config-ip-if)# |     |           | no          | shutdown |                |               |
|     | switch(config-ip-if)# |     |           | exit        |          |                |               |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
|            | switch(config)# |     | ipv6 | route | 2001:DB8:5::0/64 |     | 2001:DB8:9::2 |
| ---------- | --------------- | --- | ---- | ----- | ---------------- | --- | ------------- |
|            | switch(config)# |     | ipv6 | route | 2080::0/64       |     | tunnel10      |
| IP tunnels | commands        |     |      |       |                  |     |               |
description
| description | <DESC> |     |     |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- | --- | --- |
no description
Description
AssociatesatextdescriptionwithanIPtunnelforidentificationpurposes.
ThenoformofthiscommandremovesthedescriptionfromanIPtunnel.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<DESC> SpecifiesthedescriptivetexttoassociatewiththeIPtunnel.
Range:1to64printableASCIIcharacters.
Examples
DefinesadescriptionforGREtunnel33.
| switch(config)#        |     | interface |             | tunnel | 33      | mode gre | ipv4       |
| ---------------------- | --- | --------- | ----------- | ------ | ------- | -------- | ---------- |
| switch(config-gre-if)# |     |           | description |        | Network |          | A Tunnel C |
RemovesthedescriptionforGREtunnel33.
| switch(config)#        |     | interface |     | tunnel      | 33  |     |     |
| ---------------------- | --- | --------- | --- | ----------- | --- | --- | --- |
| switch(config-gre-if)# |     |           | no  | description |     |     |     |
DefinesadescriptionforIPv6inIPv4tunnel27.
| switch(config)#       |     | interface |             | tunnel | 27      | mode ip | 6in4        |
| --------------------- | --- | --------- | ----------- | ------ | ------- | ------- | ----------- |
| switch(config-ip-if)# |     |           | description |        | Network |         | 3 Tunnel 27 |
RemovesthedescriptionforIPv6inIPv4tunnel27.
| switch(config)#       |     | interface |     | tunnel      | 27  |     |     |
| --------------------- | --- | --------- | --- | ----------- | --- | --- | --- |
| switch(config-ip-if)# |     |           | no  | description |     |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 211

DefinesadescriptionforIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel      | 8 mode  | ip 6in6    |
| --------------------- | --------- | ----------- | ------- | ---------- |
| switch(config-ip-if)# |           | description | Network | 4 Tunnel 8 |
RemovesthedescriptionforIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel         | 8            |     |
| --------------------- | --------- | -------------- | ------------ | --- |
| switch(config-ip-if)# |           | no description |              |     |
| Command History       |           |                |              |     |
| Release               |           |                | Modification |     |
| 10.07orearlier        |           |                | --           |     |
| Command Information   |           |                |              |     |
| Platforms             | Command   | context        | Authority    |     |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
| 8325 | config-ip-if |     | rightsforthiscommand. |     |
| ---- | ------------ | --- | --------------------- | --- |
8360
9300
10000
| destination    | ip             |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| destination    | ip <IPV4-ADDR> |     |     |     |
| no destination | ip <IPV4-ADDR> |     |     |     |
Description
SetsthedestinationIPaddressforanIPtunnel.Specifytheaddressoftheinterfaceontheremote
devicetowhichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPaddressfromanIPtunnel.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesthedestinationIPaddressinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
Examples
DefinesthedestinationIPaddresstobe10.10.10.1forGREtunnel33.
| switch(config)#        | interface | tunnel      | 33 mode | gre ipv4   |
| ---------------------- | --------- | ----------- | ------- | ---------- |
| switch(config-gre-if)# |           | destination | ip      | 10.10.10.1 |
IPTunnels |212

DeletesthedestinationIPaddress10.10.10.1fromGREtunnel33.
| switch(config)#        | interface | tunnel         | 33  |               |
| ---------------------- | --------- | -------------- | --- | ------------- |
| switch(config-gre-if)# |           | no destination |     | ip 10.10.10.1 |
DefinesthedestinationIPaddresstobe10.10.20.1forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel      | 27  | mode ip 6in4 |
| --------------------- | --------- | ----------- | --- | ------------ |
| switch(config-ip-if)# |           | destination | ip  | 10.10.20.1   |
DeletesthedestinationIPaddress10.10.20.1fromIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel         | 27           |               |
| --------------------- | --------- | -------------- | ------------ | ------------- |
| switch(config-ip-if)# |           | no destination |              | ip 10.10.20.1 |
| Command History       |           |                |              |               |
| Release               |           |                | Modification |               |
| 10.07orearlier        |           |                | --           |               |
| Command Information   |           |                |              |               |
| Platforms             | Command   | context        | Authority    |               |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
|     | config-ip-if |     | rightsforthiscommand. |     |
| --- | ------------ | --- | --------------------- | --- |
8325
8360
9300
10000
| destination    | ipv6              |     |     |     |
| -------------- | ----------------- | --- | --- | --- |
| destination    | ipv6 <IPVv6-ADDR> |     |     |     |
| no destination | ipv6 [IPV6-ADDR]  |     |     |     |
Description
SetsthedestinationIPv6addressforanIPtunnel.Specifytheaddressoftheinterfaceontheremote
devicetowhichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPv6addressfromanIPtunnel.
| Parameter   |     |     | Description                             |     |
| ----------- | --- | --- | --------------------------------------- | --- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Thisisoptionalinthenoformofthecommand.
Examples
DefinesthedestinationIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 213

| switch(config)# | interface | tunnel | 8 mode | ip 6in6 |
| --------------- | --------- | ------ | ------ | ------- |
switch(config-ip-if)#
|     |     | destination | ipv6 | 2001:DB8::1 |
| --- | --- | ----------- | ---- | ----------- |
DeletesthedestinationIPv6address2001:DB8::1fromIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel         | 8            |                  |
| --------------------- | --------- | -------------- | ------------ | ---------------- |
| switch(config-ip-if)# |           | no destination |              | ipv6 2001:DB8::1 |
| Command History       |           |                |              |                  |
| Release               |           |                | Modification |                  |
| 10.07orearlier        |           |                | --           |                  |
| Command Information   |           |                |              |                  |
| Platforms             | Command   | context        | Authority    |                  |
8320 config-ip-if Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
8360
9300
10000
| interface | tunnel |     |     |     |
| --------- | ------ | --- | --- | --- |
interface tunnel <TUNNEL-NUMBER> mode {gre ipv4 | ip 6in4 | ip 6in6}
| interface tunnel | <EXISTING-TUNNEL-NUMBER> |     |     |     |
| ---------------- | ------------------------ | --- | --- | --- |
no interface tunnel <EXISTING-TUNNEL-NUMBER> [mode {gre ipv4 | ip 6in4 | ip 6in6}]
Description
CreatesorupdatesanIPtunnel.Afteryouenterthecommand,thefirmwareswitchestothe
configurationcontextforthetunnel.
Ifthespecifiedtunnelexists,thiscommandswitchestothecontextforthetunnel.
Bydefault,alltunnelsareautomaticallyassignedtothedefaultVRFwhentheyarecreated.
ThenoformofthiscommanddeletesanexistingIPtunnel.Itisoptionaltoincludeamodeintheno
form,butifamodehasbeenentered,selectingamodeisrequired.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
mode {gre ipv4 | ip 6in4 | ip 6in6} CreatesanIPtunnel.Chooseoneofthefollowingoptions:
|     |     |     |     | n gre ipv4:CreatesaGREtunnel.                |
| --- | --- | --- | --- | -------------------------------------------- |
|     |     |     |     | n ip 6in4:CreatesanIPv4tunnelforIPv6traffic. |
|     |     |     |     | n ip 6in6:CreatesanIPv6tunnelforIPv6traffic. |
Thisisoptionalinthenoform,unlessamodehas
alreadybeenentered.
<TUNNEL-NUMBER> Specifiesthenumberforanewtunnel.Range:1to127.
Numberingissharedbetweenalltunnels,sothesametunnel
numbercannotbeusedforanIPv6inIPv4tunnelandaGRE
IPTunnels |214

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
tunnel.
<EXISTING-TUNNEL-NUMBER> SpecifiesthenumberforanexistingIPtunnel.Range:1to
127.
Examples
DefinesanewGREtunnelwithnumber27.
| switch(config)# | interface | tunnel | 33 mode gre ipv4 |
| --------------- | --------- | ------ | ---------------- |
switch(config-gre-if)#
Switchestotheconfig-gre-ifcontextforexistingtunnel33.
| switch(config)# | interface | tunnel | 33  |
| --------------- | --------- | ------ | --- |
switch(config-gre-if)#
DeletesGREtunnel33.
| switch(config)# | no interface | tunnel | 33  |
| --------------- | ------------ | ------ | --- |
DefinesanewIPv6inIPv4tunnelwithnumber27.
switch(config)#
|     | interface | tunnel | 27 mode ip 6in4 |
| --- | --------- | ------ | --------------- |
switch(config-ip-if)#
Switchestotheconfig-ip-ifcontextforexistingtunnel27.
| switch(config)# | interface | tunnel | 27  |
| --------------- | --------- | ------ | --- |
switch(config-ip-if)#
DeletesIPv6inIPv4tunnel27.
| switch(config)# | no interface | tunnel | 27  |
| --------------- | ------------ | ------ | --- |
DefinesanewIPv6inIPv6tunnelwithnumber8.
| switch(config)# | interface | tunnel | 8 mode ip 6in6 |
| --------------- | --------- | ------ | -------------- |
switch(config-ip-if)#
DeletesIPv6inIPv6tunnelwithnumber3.
| switch(config)# | no interface | tunnel | 33 mode gre ipv4 |
| --------------- | ------------ | ------ | ---------------- |
Command History
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 215

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
| 8325 | config-ip-if |     | rightsforthiscommand. |
| ---- | ------------ | --- | --------------------- |
| 8360 | config       |     |                       |
9300
10000
ip address
| ip address <IPV4-ADDR>/<MASK> |                    |     |     |
| ----------------------------- | ------------------ | --- | --- |
| no ip address                 | <IPV4-ADDR>/<MASK> |     |     |
Description
SetsthelocalIPaddressofaGREtunnel.Thisaddressidentifiesthetunnelinterfaceforrouting.Itmust
beonthesamesubnetasthetunneladdressassignedontheremotedevice.
ThenoformofthiscommanddeletesthelocalIPaddressassignedtoaGREtunnel.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR> SpecifiesthetunnelIPaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.Youcanremoveleadingzeros.
Forexample,theaddress192.169.005.100becomes
192.168.5.100.
| <MASK> |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to32.
Examples
DefinesthelocalIPaddress10.10.10.1forGREtunnel33.
| switch(config)#        | interface | tunnel     | 33 mode gre ipv4 |
| ---------------------- | --------- | ---------- | ---------------- |
| switch(config-gre-if)# |           | ip address | 10.10.10.1/24    |
DeletesthelocalIPaddress10.10.10.1forGREtunnel33.
| switch(config)#        | interface | tunnel        | 33            |
| ---------------------- | --------- | ------------- | ------------- |
| switch(config-gre-if)# |           | no ip address | 10.10.10.1/24 |
| Command History        |           |               |               |
| Release                |           |               | Modification  |
| 10.07orearlier         |           |               | --            |
IPTunnels |216

| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
config-gre-if
| 8320 |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | -------------------------------------------------- | --- |
| 8325 |     |     | rightsforthiscommand.                              |     |
8360
9300
10000
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK> |     |     |     |
| --------------- | ------------------ | --- | --- | --- |
| no ipv6 address | <IPV6-ADDR>/<MASK> |     |     |     |
Description
SetsthelocalIPaddressofanIPv6toIPv4tunnelorofanIPv6toIPv6tunnel.Thisaddressidentifiesthe
tunnelinterfaceforrouting.Itmustbeonthesamesubnetasthetunneladdressassignedonthe
remotedevice.
ThenoformofthiscommanddeletesthelocalIPaddressassignedtoanIPv6toIPv4tunnel.
| Parameter   |     |     | Description                             |     |
| ----------- | --- | --- | --------------------------------------- | --- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| <MASK> |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |     |
| ------ | --- | --- | ---------------------------------------------------- | --- |
(x),wherexisadecimalnumberfrom0to32.
Examples
DefinesthelocalIPaddress2001:DB8:5::1/64fortunnel8foranIPv6toIPv6tunnel.
| switch(config)#       | interface | tunnel       | 8 mode           | ip 6in6 |
| --------------------- | --------- | ------------ | ---------------- | ------- |
| switch(config-ip-if)# |           | ipv6 address | 2001:DB8:5::1/64 |         |
DeletesthelocalIPaddress2001:DB8::1/32fortunnel8.
| switch(config)#       | interface | tunnel          | 8            |                  |
| --------------------- | --------- | --------------- | ------------ | ---------------- |
| switch(config-ip-if)# |           | no ipv6 address |              | 2001:DB8:5::1/64 |
| Command History       |           |                 |              |                  |
| Release               |           |                 | Modification |                  |
| 10.07orearlier        |           |                 | --           |                  |
| Command Information   |           |                 |              |                  |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 217

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
8320 config-ip-if Administratorsorlocalusergroupmemberswithexecution
| 8325 | config-if |     | rightsforthiscommand. |
| ---- | --------- | --- | --------------------- |
8360
9300
10000
ip mtu
ip mtu <VALUE>
Description
SetstheMTU(maximumtransmissionunit)foranIPinterface.Thedefaultvalueis1500bytes.
ThenoformofthiscommandsetstheMTUtothedefaultvalueof1500bytes.
| Parameter |     |     | Description                                          |
| --------- | --- | --- | ---------------------------------------------------- |
| <VALUE>   |     |     | SpecifiestheMTUinbytes.Range:1,280bytesto9,192bytes. |
Usage
TheIPMTUisthelargestIPpacketthatcanbesentorreceivedbytheinterface.Foratunnel,theIP
MTUisthemaximumsizeoftheIPpayload.Toenablejumbopacketforwardingthroughthetunnel,set
theIPMTUofthetunneltoavaluegreaterthan1500.AlsosettheMTUandtheIPMTUvaluesforthe
underlyingphysicalinterfacethatthetunnelisusingtoavaluegreaterthan1,500bytes.TheIPMTUof
thetunnelmustalsobegreaterthanorequaltotheMTUoftheingressinterfaceontheswitch.TheIP
MTUvalueofthetunnelmustalsobelessthanorequaltotheIPMToftheunderlyinginterfacethatthe
tunnelisusing.
WhendefiningaGREtunnel,theMTUhastoaccountfor28bytesofIPlayeroverhead,plusaGRE
header.ItmustbelargerthantheMTUoftheinterfacethatthetunnelisusing.Packetslargerthanthe
MTUaredropped.
Examples
SetstheMTUonGREinterface33to1300bytes.
| switch(config)#        | interface | tunnel   | 33 mode gre ipv4 |
| ---------------------- | --------- | -------- | ---------------- |
| switch(config-gre-if)# |           | mtu 1300 |                  |
SetstheMTUonGREinterface33tothedefaultvalue.
| switch(config)#        | interface | tunnel | 33 mode gre ipv4 |
| ---------------------- | --------- | ------ | ---------------- |
| switch(config-gre-if)# |           | ip mtu |                  |
SetstheMTUonIPv6inIPv4tunnel27to1000bytes.
| switch(config)#       | interface | tunnel   | 27 mode ip 6in4 |
| --------------------- | --------- | -------- | --------------- |
| switch(config-ip-if)# |           | mtu 1000 |                 |
SetstheMTUonIPv6inIPv4tunnel27tothedefaultvalue.
IPTunnels |218

| switch(config)# | interface | tunnel | 27 mode | ip 6in4 |
| --------------- | --------- | ------ | ------- | ------- |
switch(config-ip-if)#
ip mtu
SetstheMTUonIPv6inIPv6tunnel8to900bytes.
| switch(config)#       | interface | tunnel      | 8 mode | ip 6in6 |
| --------------------- | --------- | ----------- | ------ | ------- |
| switch(config-ip-if)# |           | ip mtu 9000 |        |         |
SetstheMTUonIPv6inIPv6tunnel8tothedefaultvalue.
| switch(config)#       | interface | tunnel  | 8 mode       | ip 6in6 |
| --------------------- | --------- | ------- | ------------ | ------- |
| switch(config-ip-if)# |           | ip mtu  |              |         |
| Command History       |           |         |              |         |
| Release               |           |         | Modification |         |
| 10.07orearlier        |           |         | --           |         |
| Command Information   |           |         |              |         |
| Platforms             | Command   | context | Authority    |         |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
| 8325 | config-ip-if |     | rightsforthiscommand. |     |
| ---- | ------------ | --- | --------------------- | --- |
8360
9300
10000
| show interface | tunnel                  |     |            |     |
| -------------- | ----------------------- | --- | ---------- | --- |
| show interface | tunnel[<TUNNEL-NUMBER>] |     | [vsx-peer] |     |
Description
ShowsconfigurationsettingsforallIPtunnels,oraspecifictunnel.
| Parameter       |     |     | Description                                  |     |
| --------------- | --- | --- | -------------------------------------------- | --- |
| <TUNNEL-NUMBER> |     |     | SpecifiesthenumberofanIPtunnel.Range:1to127. |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 219

Showsconfigurationsettingsfortunnel10,whichisaGREtunnelinthefollowingexample.
| switch#    | show        | interface | tunnel10     |         |              |     |       |     |
| ---------- | ----------- | --------- | ------------ | ------- | ------------ | --- | ----- | --- |
| Interface  | tunnel10    |           | is up        |         |              |     |       |     |
| Admin      | state       | is up     |              |         |              |     |       |     |
| tunnel     | type        | GRE       | IPv4         |         |              |     |       |     |
| tunnel     | interface   |           | IPv4 address |         | 192.0.2.0/24 |     |       |     |
| tunnel     | source      | IPv4      | address      | 1.1.1.1 |              |     |       |     |
| tunnel     | destination |           | IPv4         | address | 2.2.2.2      |     |       |     |
| tunnel     | ttl         | 60        |              |         |              |     |       |     |
| Statistics |             |           |              |         | RX           | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets |     |     |     |     | 0   | 0   |     | 0   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3 Bytes   |     |     |     |     | 0   | 0   |     | 0   |
Showsconfigurationsettingsfortunnel12,whichisanIPv6inIPv6tunnelinthefollowingexample.
switch#
|              | show        | interface | tunnel12     |         |         |     |       |     |
| ------------ | ----------- | --------- | ------------ | ------- | ------- | --- | ----- | --- |
| Interface    | tunnel12    |           | is up        |         |         |     |       |     |
| Admin        | state       | is up     |              |         |         |     |       |     |
| tunnel       | type        | IPv6      | in IPv6      |         |         |     |       |     |
| tunnel       | interface   |           | IPv6 address |         | 4::1/64 |     |       |     |
| tunnel       | source      | IPv6      | address      | 2::1    |         |     |       |     |
| tunnel       | destination |           | IPv6         | address | 2::2    |     |       |     |
| tunnel       | ttl         | 60        |              |         |         |     |       |     |
| Description: |             | Network2  | Tunnel       |         |         |     |       |     |
| Statistics   |             |           |              |         | RX      | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets |     |     |     |     | 0   | 0   |     | 0   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3 Bytes   |     |     |     |     | 0   | 0   |     | 0   |
Showsconfigurationsettingsforalltunnels.
| switch#    | show        | interface | tunnel       |         |              |     |       |     |
| ---------- | ----------- | --------- | ------------ | ------- | ------------ | --- | ----- | --- |
| Interface  | tunnel10    |           | is up        |         |              |     |       |     |
| Admin      | state       | is up     |              |         |              |     |       |     |
| tunnel     | type        | GRE       | IPv4         |         |              |     |       |     |
| tunnel     | interface   |           | IPv4 address |         | 192.0.2.0/24 |     |       |     |
| tunnel     | source      | IPv4      | address      | 1.1.1.1 |              |     |       |     |
| tunnel     | destination |           | IPv4         | address | 2.2.2.2      |     |       |     |
| tunnel     | ttl         | 60        |              |         |              |     |       |     |
| Statistics |             |           |              |         | RX           | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets   |             |           |         |              | 0            | 0   |     | 0   |
| ------------ | ----------- | --------- | ------- | ------------ | ------------ | --- | --- | --- |
| L3 Bytes     |             |           |         |              | 0            | 0   |     | 0   |
| Interface    | tunnel11    |           | is up   |              |              |     |     |     |
| Admin        | state       | is up     |         |              |              |     |     |     |
| tunnel       | type        | IPv6      | in IPv4 |              |              |     |     |     |
| tunnel       | source      | IPv4      | address | 198.51.100.0 |              |     |     |     |
| tunnel       | destination |           | IPv4    | address      | 198.51.200.5 |     |     |     |
| tunnel       | ttl         | 80        |         |              |              |     |     |     |
| Description: |             | Network11 |         |              |              |     |     |     |
IPTunnels |220

| Statistics |     |     |     |     | RX  |     | TX  | Total |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
------------- -------------------- -------------------- --------------------
| L3 Packets   |             |          |         |         | 0       |     | 0   |       | 0   |
| ------------ | ----------- | -------- | ------- | ------- | ------- | --- | --- | ----- | --- |
| L3 Bytes     |             |          |         |         | 0       |     | 0   |       | 0   |
| Interface    | tunnel12    |          | is up   |         |         |     |     |       |     |
| Admin        | state       | is up    |         |         |         |     |     |       |     |
| tunnel       | type        | IPv6     | in IPv6 |         |         |     |     |       |     |
| tunnel       | interface   |          | IPv6    | address | 4::1/64 |     |     |       |     |
| tunnel       | source      | IPv6     | address | 2::1    |         |     |     |       |     |
| tunnel       | destination |          | IPv6    | address | 2::2    |     |     |       |     |
| tunnel       | ttl         | 60       |         |         |         |     |     |       |     |
| Description: |             | Network2 |         | Tunnel  |         |     |     |       |     |
| Statistics   |             |          |         |         | RX      |     | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets     |             |         |         |     | 0            |     | 0   |     | 0   |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- | --- | --- |
| L3 Bytes       |             |         |         |     | 0            |     | 0   |     | 0   |
| Command        | History     |         |         |     |              |     |     |     |     |
| Release        |             |         |         |     | Modification |     |     |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |     |     |
| Command        | Information |         |         |     |              |     |     |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |     |     |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
| 8360 |     |     |     |     | commandfromtheoperatorcontext(>)only.                 |     |     |     |     |
9300
10000
| show running-config |     |     |           | interface             | tunnel |            |     |     |     |
| ------------------- | --- | --- | --------- | --------------------- | ------ | ---------- | --- | --- | --- |
| show running-config |     |     | interface | tunnel<TUNNEL-NUMBER> |        | [vsx-peer] |     |     |     |
Description
ShowsthecommandsusedtoconfigureanIPtunnel.
| Parameter       |     |     |     |     | Description                                  |     |     |     |     |
| --------------- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
| <TUNNEL-NUMBER> |     |     |     |     | SpecifiesthenumberofanIPtunnel.Range:1to127. |     |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowstheconfigurationforaGREtunnel.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 221

| switch# show | running-config |        | interface | tunnel2 |
| ------------ | -------------- | ------ | --------- | ------- |
| interface    | tunnel         | 2 mode | gre ipv4  |         |
| source       | ip 10.10.20.11 |        |           |         |
| destination  | ip 10.20.1.2   |        |           |         |
| ip address   | 10.10.10.1/24  |        |           |         |
| ttl 60       |                |        |           |         |
ShowstheconfigurationforIPv6inIPv4tunnel.
| switch# show | running-config   |      | interface | tunnel5 |
| ------------ | ---------------- | ---- | --------- | ------- |
| interface    | tunnel5          | mode | ip 6in4   |         |
| source       | ip 10.10.10.12   |      |           |         |
| destination  | ip 22.20.20.20   |      |           |         |
| ip6 address  | 2001:DB8:5::1/64 |      |           |         |
| ttl 60       |                  |      |           |         |
no shutdown
| description | Network10 |     |     |     |
| ----------- | --------- | --- | --- | --- |
ShowstheconfigurationforIPv6inIPv6tunnel.
| switch# show        | running-config |         | interface    | tunnel1 |
| ------------------- | -------------- | ------- | ------------ | ------- |
| interface           | tunnel         | 1 mode  | ip 6in6      |         |
| description         | Network2       | Tunnel  |              |         |
| source              | ipv6 2::1      |         |              |         |
| destination         | ipv6           | 2::2    |              |         |
| ipv6 address        | 4::1/64        |         |              |         |
| ttl 60              |                |         |              |         |
| Command History     |                |         |              |         |
| Release             |                |         | Modification |         |
| 10.07orearlier      |                |         | --           |         |
| Command Information |                |         |              |         |
| Platforms           | Command        | context | Authority    |         |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
8325
| 8360 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
9300
10000
shutdown
shutdown
no shutdown
Description
ThiscommanddisablesanIPinterface.IPinterfacesaredisabledbydefaultwhencreated.
ThenoformofthiscommandenablesanIPinterface.
Examples
IPTunnels |222

EnablesGREinterface33.
| switch(config)#        | interface | tunnel      | 33 mode gre ipv4 |
| ---------------------- | --------- | ----------- | ---------------- |
| switch(config-gre-if)# |           | no shutdown |                  |
DisablesGREinterface33.
| switch(config)#        | interface | tunnel   | 33 mode gre ipv4 |
| ---------------------- | --------- | -------- | ---------------- |
| switch(config-gre-if)# |           | shutdown |                  |
EnablesIPv6inIPv4interface27.
| switch(config)#       | interface | tunnel      | 27 mode ip 6in4 |
| --------------------- | --------- | ----------- | --------------- |
| switch(config-ip-if)# |           | no shutdown |                 |
DisablesIPv6inIPv4interface27.
| switch(config)#       | interface | tunnel   | 27 mode ip 6in4 |
| --------------------- | --------- | -------- | --------------- |
| switch(config-ip-if)# |           | shutdown |                 |
| Command History       |           |          |                 |
| Release               |           |          | Modification    |
| 10.07orearlier        |           |          | --              |
| Command Information   |           |          |                 |
| Platforms             | Command   | context  | Authority       |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
| 8325 | config-ip-if |     | rightsforthiscommand. |
| ---- | ------------ | --- | --------------------- |
8360
9300
10000
| source ip             |             |     |     |
| --------------------- | ----------- | --- | --- |
| source ip <IPV4-ADDR> |             |     |     |
| no source ip          | <IPV4-ADDR> |     |     |
Description
SetsthesourceIPaddressforanIPtunnel.SpecifytheIPaddressofalayer3interfaceontheswitch.
TunnelscanhavethesamesourceIPaddressanddifferentdestinationIPaddresses.
ThenoformofthiscommanddeletesthesourceIPaddressforanIPtunnel.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR> SpecifiesthesourceIPaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 223

Examples
DefinesthesourceIPaddresstobe10.10.20.1forGREtunnel33.
switch(config)#
|                        | interface | tunnel | 33 mode gre ipv4 |
| ---------------------- | --------- | ------ | ---------------- |
| switch(config-gre-if)# |           | source | ip 10.10.20.1    |
DeletesthesourceIPaddress10.1.20.1fromGREtunnel33.
| switch(config)#        | interface | tunnel    | 33            |
| ---------------------- | --------- | --------- | ------------- |
| switch(config-gre-if)# |           | no source | ip 10.10.20.1 |
DefinesthesourceIPaddresstobe10.10.10.1forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# |           | source | ip 10.10.10.1   |
DeletesthesourceIPaddress10.1.10.1fromIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel    | 27            |
| --------------------- | --------- | --------- | ------------- |
| switch(config-ip-if)# |           | no source | ip 10.10.10.1 |
| Command History       |           |           |               |
| Release               |           |           | Modification  |
| 10.07orearlier        |           |           | --            |
| Command Information   |           |           |               |
| Platforms             | Command   | context   | Authority     |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
|     | config-ip-if |     | rightsforthiscommand. |
| --- | ------------ | --- | --------------------- |
8325
8360
9300
10000
| source ipv6    |             |     |     |
| -------------- | ----------- | --- | --- |
| source ipv6    | <IPV6-ADDR> |     |     |
| no source ipv6 | [IPV6-ADDR] |     |     |
Description
SetsthesourceIPv6addresstobeusedfortheencapsulation.
ThenoformofthiscommanddeletesthesourceIPv6addressforanIPtunnel.
| Parameter   |     |     | Description                             |
| ----------- | --- | --- | --------------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |
IPTunnels |224

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Thisisoptionalinthenoformofthecommand.
Examples
DefinesthesourceIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel | 8 mode           | ip 6in6 |
| --------------------- | --------- | ------ | ---------------- | ------- |
| switch(config-ip-if)# |           | source | ipv6 2001:DB8::1 |         |
DeletesthesourceIPaddress2001:DB8::1fromIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel    | 8            |             |
| --------------------- | --------- | --------- | ------------ | ----------- |
| switch(config-ip-if)# |           | no source | ipv6         | 2001:DB8::1 |
| Command History       |           |           |              |             |
| Release               |           |           | Modification |             |
| 10.07orearlier        |           |           | --           |             |
| Command Information   |           |           |              |             |
| Platforms             | Command   | context   | Authority    |             |
8320 config-ip-if Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
8360
9300
10000
ttl
ttl <COUNT>
no ttl
Description
SetstheTTL(time-to-live),alsoknownasthehopcount,fortunneledpackets.Ifnotconfigured,the
defaultvalueof64isusedforthetunnel.(Thehopcountoftheoriginalpacketsisnotchanged.)A
maximumoffourdifferentTTLvaluescanbeusedatthesametimebyalltunnelsontheswitch.For
example,iftunnel-1hasTTL10,tunnel-2hasTTL20,tunnel-3hasTTL30,andtunnel-4hasTTL40,then
tunnel-5cannothaveauniqueTTLvalue,itmustreuseoneofthevaluesassignedtotheothertunnels
(10,20,30,40).
ThenoformofthiscommandsetsTTLtothedefaultvalueof64.
| Parameter |     |     | Description                                   |     |
| --------- | --- | --- | --------------------------------------------- | --- |
| <COUNT>   |     |     | Specifiesthehopcount.Range:1to255.Default:64. |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 225

Examples
DefinesaTTLof99forGREtunnel33.
switch(config)#
|                        | interface | tunnel | 33 mode gre ipv4 |
| ---------------------- | --------- | ------ | ---------------- |
| switch(config-gre-if)# |           | ttl 99 |                  |
SetstheTTLforGREtunnel33tothedefaultvalueof64.
| switch(config)#        | interface | tunnel | 33  |
| ---------------------- | --------- | ------ | --- |
| switch(config-gre-if)# |           | no ttl |     |
DefinesaTTLof55forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# |           | ttl 55 |                 |
SetstheTTLforIPv6inIPv4tunnel27tothedefaultvalueof64.
| switch(config)#       | interface | tunnel  | 27           |
| --------------------- | --------- | ------- | ------------ |
| switch(config-ip-if)# |           | no ttl  |              |
| Command History       |           |         |              |
| Release               |           |         | Modification |
| 10.07orearlier        |           |         | --           |
| Command Information   |           |         |              |
| Platforms             | Command   | context | Authority    |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
|     | config-ip-if |     | rightsforthiscommand. |
| --- | ------------ | --- | --------------------- |
8325
8360
9300
10000
vrf attach
| vrf attach <VRF-NAME> |            |     |     |
| --------------------- | ---------- | --- | --- |
| no vrf attach         | <VRF-NAME> |     |     |
Description
AssignsanIPtunneltoaVRF.Bydefault,alltunnelsareautomaticallyassignedtothedefaultVRFwhen
theyarecreated.
ThenoformofthiscommandassignsatunneltothedefaultVRF(default).
| Parameter  |     |     | Description                                  |
| ---------- | --- | --- | -------------------------------------------- |
| <VRF-NAME> |     |     | SpecifiestheVRFnametowhichtoassignthetunnel. |
IPTunnels |226

Examples
AssignsGREtunnel33tovrf1.
switch(config)#
|                        | interface | tunnel     | 33 mode | gre ipv4 |
| ---------------------- | --------- | ---------- | ------- | -------- |
| switch(config-gre-if)# |           | vrf attach | vrf1    |          |
ReassignsGREtunnel33tothedefaultVRF.
| switch(config)#        | interface | tunnel | 33     |      |
| ---------------------- | --------- | ------ | ------ | ---- |
| switch(config-gre-if)# |           | no vrf | attach | vrf1 |
AssignsIPv6inIPv4tunnel27tovrf2.
| switch(config)#       | interface | tunnel     | 27 mode | gre ipv4 |
| --------------------- | --------- | ---------- | ------- | -------- |
| switch(config-ip-if)# |           | vrf attach | vrf2    |          |
ReassignsIPv6inIPv4tunnel27tothedefaultVRF.
| switch(config)#       | interface | tunnel        | 27   |     |
| --------------------- | --------- | ------------- | ---- | --- |
| switch(config-ip-if)# |           | no vrf attach | vrf2 |     |
AssignsIPv6inIPv6tunnel8tovrf3.
| switch(config)#       | interface | tunnel     | 8 mode | ip 6in6 |
| --------------------- | --------- | ---------- | ------ | ------- |
| switch(config-ip-if)# |           | vrf attach | vrf3   |         |
ReassignsIPv6inIPv6tunnel8tothedefaultVRF.
switch(config)#
|                       | interface | tunnel        | 8            |     |
| --------------------- | --------- | ------------- | ------------ | --- |
| switch(config-ip-if)# |           | no vrf attach | vrf3         |     |
| Command History       |           |               |              |     |
| Release               |           |               | Modification |     |
| 10.07orearlier        |           |               | --           |     |
| Command Information   |           |               |              |     |
| Platforms             | Command   | context       | Authority    |     |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecution
| 8325 | config-ip-if |     | rightsforthiscommand. |     |
| ---- | ------------ | --- | --------------------- | --- |
8360
9300
10000
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 227

Chapter 10

IP Source Lockdown

IP Source Lockdown

IP source lockdown provides added security by preventing IP source address spoofing on a per-port
basis. Every packet is inspected for this purpose in hardware. When IP source lockdown is enabled, IP
traffic received on an interface (port) is forwarded only if the VLAN, IP address, MAC address, interface
(port) matches the IP binding database entry.

It is best to configure IP source lockdown during a switch maintenance period as enabling it may cause client

traffic to be dropped for 10 to 15 seconds.

To use IPv4 source lockdown, the IPv4 binding database must be populated. The binding database is
typically dynamically populated by DHCPv4 snooping that learns and saves the binding information.
Alternatively, the IPv4 binding database can be statically populated with the ipv4 source-binding
command described in this chapter. Often DHCPv4 snooping is used to dynamically populate most of
the IP binding database along with the ipv4 source-binding command that is used to add the binding
information for several known and trusted clients, typically administrators. For dynamic IP binding
database population with DHCPv4 snooping, see DHCP snooping.

To use IPv6 source lockdown, the IPv6 binding database must be populated. The binding database is
typically dynamically populated by DHCPv6 snooping that learns and saves the binding information.
Alternatively, the IPv6 binding database can be statically populated with the ipv6 source-binding
command described in this chapter. Often DHCPv6 snooping is used to dynamically populate most of
the IPv6 binding database along with the ipv6 source-binding command that is used to add the
binding information for several known and trusted clients, typically administrators. For dynamic IPv6
binding database population with DHCPv6 snooping, see DHCP snooping.

IP source lockdown should not be configured on ISL (inter-switch link) ports.

IPv4 source lockdown commands

ipv4 source-binding
ipv4 source-binding <VLAN-ID> <IPV4-ADDR> <MAC-ADDR> <IFNAME>
no ipv4 source-binding <VLAN-ID> <IPV4-ADDR> <MAC-ADDR> <IFNAME>

Description

Adds static IPv4 client source binding information to the switch IP binding database. Although DHCPv4
snooping is often used to dynamically populate the binding database, this command is available for
manually adding entries to the switch IP binding database.

Statically configured IP binding information supersedes any dynamically collected binding information for the

same client.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

228

Thenoformofthiscommandremovesthespecifiedbindingthatwasstaticallyconfiguredwiththeipv4
source-bindingcommand.Thenoformhasnoeffectonbindingsthatweredynamicallyconfigured
withDHCPv4snooping.
| Parameter |     |     | Description                                      |
| --------- | --- | --- | ------------------------------------------------ |
| <VLAN-ID> |     |     | SpecifiestheIDofanexistingVLANonwhichtheclientis |
connected.Range:1to4094.
| <IPV4-ADDR> |     |     | SpecifiestheclientIPv4unicastaddress.             |
| ----------- | --- | --- | ------------------------------------------------- |
| <MAC-ADDR>  |     |     | SpecifiestheclientMACaddress.                     |
| <IFNAME>    |     |     | Specifiestheinterfaceonwhichtheclientisconnected. |
Examples
AddingastaticIPv4binding:
switch(config)# ipv4 source-binding 1 10.2.1.4 00:50:56:96:e4:cf 1/1/1
RemovingaIPv4binding:
switch(config)# no ipv4 source-binding 1 10.2.1.4 00:50:56:96:e4:cf 1/1/1
| Command History     |         |         |                                     |
| ------------------- | ------- | ------- | ----------------------------------- |
| Release             |         |         | Modification                        |
| 10.10               |         |         | Commandenabledon8360seriesswitches. |
| 10.07orearlier      |         |         | --                                  |
| Command Information |         |         |                                     |
| Platforms           | Command | context | Authority                           |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv4 source-lockdown
ipv4 source-lockdown
no ipv4 source-lockdown
Description
EnablesIPv4sourcelockdownforallVLANsontheselectedinterface(port).
ThenoformofthiscommanddisablesIPv4sourcelockdownfortheselectedinterface(port).
Examples
EnablingIPv4sourcelockdownoninterface1/1/1:
IPSourceLockdown|229

| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|     |     | ipv4 | source-lockdown |     |     |     |
| --- | --- | ---- | --------------- | --- | --- | --- |
EnablingIPv4sourcelockdownoninterfacelag112:
| switch(config)#    |     | interface | lag112          |     |     |     |
| ------------------ | --- | --------- | --------------- | --- | --- | --- |
| switch(config-if)# |     | ipv4      | source-lockdown |     |     |     |
DisablingIPv4sourcelockdownoninterface1/1/1:
| switch(config)#     |         | interface | 1/1/1                |                                     |     |     |
| ------------------- | ------- | --------- | -------------------- | ----------------------------------- | --- | --- |
| switch(config-if)#  |         | no        | ipv4 source-lockdown |                                     |     |     |
| Command History     |         |           |                      |                                     |     |     |
| Release             |         |           |                      | Modification                        |     |     |
| 10.10               |         |           |                      | Commandenabledon8360seriesswitches. |     |     |
| 10.07orearlier      |         |           |                      | --                                  |     |     |
| Command Information |         |           |                      |                                     |     |     |
| Platforms           | Command |           | context              | Authority                           |     |     |
8360 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv4 source-lockdown |     |          | hardware |           | retry       |     |
| -------------------- | --- | -------- | -------- | --------- | ----------- | --- |
| ipv4 source-lockdown |     | hardware | retry    | <VLAN-ID> | <IPV4-ADDR> |     |
Description
RetriestheIPv4sourcelockdownhardwareprogrammingforaclientidentifiedbyVLANandIPv4
address.
| Parameter |     |     |     | Description                                      |     |     |
| --------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| <VLAN-ID> |     |     |     | SpecifiestheIDofanexistingVLANonwhichtheclientis |     |     |
connected.Range:1to4094.
| <IPV4-ADDR> |     |     |     | SpecifiestheclientIPv4unicastaddress. |     |     |
| ----------- | --- | --- | --- | ------------------------------------- | --- | --- |
Example
ConfigureIPv4sourcelockdownhardwareretryfortheclientonVLAN10.
| switch(config)# |     | ipv4 source-lockdown |     |     | hardware retry | 10 1.1.2.1 |
| --------------- | --- | -------------------- | --- | --- | -------------- | ---------- |
| Command History |     |                      |     |     |                |            |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 230

| Release        |             |         | Modification                        |     |     |     |
| -------------- | ----------- | ------- | ----------------------------------- | --- | --- | --- |
| 10.10          |             |         | Commandenabledon8360seriesswitches. |     |     |     |
| 10.07orearlier |             |         | --                                  |     |     |     |
| Command        | Information |         |                                     |     |     |     |
| Platforms      | Command     | context | Authority                           |     |     |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | ipv4 source-binding |            |     |     |     |     |
| --------- | ------------------- | ---------- | --- | --- | --- | --- |
| show ipv4 | source-binding      | [vsx-peer] |     |     |     |     |
Description
ShowsallIPv4staticsourcebindinginformationirrespectiveofsourcelockdownconfiguration..
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingallIPv4sourcebindinginformation:
| switch# | show ipv4 | source-binding |             |           |      |              |
| ------- | --------- | -------------- | ----------- | --------- | ---- | ------------ |
| PORT    |           | VLAN           | MAC-ADDRESS | HW-STATUS | FROM | IPv4-ADDRESS |
-------------- --------- ----------------- --------- -------- -------------
| 1/1/1          |             | 2       | aa:bb:cc:dd:ee:ff                                    | Yes | static | 1.2.3.4     |
| -------------- | ----------- | ------- | ---------------------------------------------------- | --- | ------ | ----------- |
| 1/1/2          |             | 12      | aa:ab:cc:dd:ee:ff                                    | Yes | static | 10.20.30.40 |
| Command        | History     |         |                                                      |     |        |             |
| Release        |             |         | Modification                                         |     |        |             |
| 10.10          |             |         | Commandenabledon8360seriesswitches.                  |     |        |             |
| 10.07orearlier |             |         | --                                                   |     |        |             |
| Command        | Information |         |                                                      |     |        |             |
| Platforms      | Command     | context | Authority                                            |     |        |             |
| 8360           |             |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |        |             |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
IPSourceLockdown|231

| show ipv4 | source-lockdown |     |     |     |
| --------- | --------------- | --- | --- | --- |
show ipv4 source-lockdown [binding [interface <IFNAME> | ip <IPV4-ADDR> | mac <MAC-ADDR>
| | vlan <VLAN-ID>] | | interface | <IFNAME>] | [vsx-peer] |     |
| ----------------- | ----------- | --------- | ---------- | --- |
Description
ShowssummaryordetailedIPv4sourcelockdowninformation.Whenenteredwithoutparameters,
summarystatusinformationforallinterfaces(ports)inthebindingdatabaseisshown.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
binding Specifiesthatdetailedlockdownbindingrecordinformationisto
bedisplayed.Thebindingdatabaserecordcanbeidentifiedby
anyoneofinterface(port),ip,mac,orvlan.
interface <IFNAME> Specifiestheclientinterface(port).Whenenteredwithoutthe
bindingparameter,thesummarystatusinformationisdisplayed
forthespecifiedinterface.
| ip <IPV4-ADDR> |     |     | SpecifiestheclientIPv4unicastaddress. |     |
| -------------- | --- | --- | ------------------------------------- | --- |
| mac <MAC-ADDR> |     |     | SpecifiestheclientMACaddress.         |     |
vlan <VLAN-ID> SpecifiestheIDofanexistingVLANonwhichtheclientis
connected.Range:1to4094.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingthesummarystatusinformationforallinterfacesinthebindingdatabase:
| switch# show | ipv4 source-lockdown |           |     |     |
| ------------ | -------------------- | --------- | --- | --- |
| INTERFACE    | LOCKDOWN             | HW-STATUS |     |     |
| ---------    | --------             | --------- |     |     |
| 1/1/1        | Yes                  | Yes       |     |     |
| 1/1/2        | Yes                  | No        |     |     |
| lag112       | Yes                  | Yes       |     |     |
Showingthesummarystatusinformationforthespecifiedinterfaceinthebindingdatabase:
| switch# show | ipv4 source-lockdown |           | interface | 1/1/2 |
| ------------ | -------------------- | --------- | --------- | ----- |
| INTERFACE    | LOCKDOWN             | HW-STATUS |           |       |
| ---------    | --------             | --------- |           |       |
| 1/1/2        | Yes                  | No        |           |       |
Showingthedetailedbindingrecordandrelatedinformationforallinterfacesinthebindingdatabase:
| switch# show | ipv4 source-lockdown |     | binding |     |
| ------------ | -------------------- | --- | ------- | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 232

| Interface      | Name         | : 1/1/1             |             |     |
| -------------- | ------------ | ------------------- | ----------- | --- |
| VLAN Id        |              | : 2000              |             |     |
| MAC Address    |              | : 00:50:56:96:e4:cf |             |     |
| IP Address     |              | : 192.168.142.113   |             |     |
| Time Remaining |              | : static            |             |     |
| Lockdown       | Status       | : Yes               |             |     |
| Hardware       | Status       | : Yes               |             |     |
| Hardware       | Error Reason | : --                |             |     |
| Interface      | Name         | : 1/1/2             |             |     |
| VLAN Id        |              | : 100               |             |     |
| MAC Address    |              | : 00:50:56:96:04:4d |             |     |
| IP Address     |              | : 120.168.43.52     |             |     |
| Time Remaining |              | : 115 seconds       |             |     |
| Lockdown       | Status       | : Yes               |             |     |
| Hardware       | Status       | : No                |             |     |
| Hardware       | Error Reason | : Resource          | unavailable |     |
| Interface      | Name         | : lag112            |             |     |
| VLAN Id        |              | : 12                |             |     |
| MAC Address    |              | : 00:50:56:96:d8:3d |             |     |
| IP Address     |              | : 120.168.76.182    |             |     |
| Time Remaining |              | : static            |             |     |
| Lockdown       | Status       | : Yes               |             |     |
| Hardware       | Status       | : Yes               |             |     |
| Hardware       | Error Reason | : --                |             |     |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/2:
| switch#        | show ipv4 source-lockdown |                     | binding     | interface 1/1/2 |
| -------------- | ------------------------- | ------------------- | ----------- | --------------- |
| Interface      | Name                      | : 1/1/2             |             |                 |
| VLAN Id        |                           | : 100               |             |                 |
| MAC Address    |                           | : 00:50:56:96:04:4d |             |                 |
| IP Address     |                           | : 120.168.43.52     |             |                 |
| Time Remaining |                           | : 115 seconds       |             |                 |
| Lockdown       | Status                    | : Yes               |             |                 |
| Hardware       | Status                    | : No                |             |                 |
| Hardware       | Error Reason              | : Resource          | unavailable |                 |
Showingthedetailedbindingrecordandrelatedinformationforinterfacelag112(identifiedinthis
examplecommandbytheIPaddress):
| switch#        | show ipv4 source-lockdown |                     | binding | ip 120.168.76.182 |
| -------------- | ------------------------- | ------------------- | ------- | ----------------- |
| Interface      | Name                      | : lag112            |         |                   |
| VLAN Id        |                           | : 12                |         |                   |
| MAC Address    |                           | : 00:50:56:96:d8:3d |         |                   |
| IP Address     |                           | : 120.168.76.182    |         |                   |
| Time Remaining |                           | : static            |         |                   |
| Lockdown       | Status                    | : Yes               |         |                   |
| Hardware       | Status                    | : Yes               |         |                   |
| Hardware       | Error Reason              | : --                |         |                   |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/1(identifiedinthis
examplecommandbytheMACaddress):
IPSourceLockdown|233

switch# show ipv4 source-lockdown binding mac 00:50:56:96:e4:cf
| Interface      | Name   |        | : 1/1/1             |     |     |     |
| -------------- | ------ | ------ | ------------------- | --- | --- | --- |
| VLAN Id        |        |        | : 2000              |     |     |     |
| MAC Address    |        |        | : 00:50:56:96:e4:cf |     |     |     |
| IP Address     |        |        | : 192.168.142.113   |     |     |     |
| Time Remaining |        |        | : static            |     |     |     |
| Lockdown       | Status |        | : Yes               |     |     |     |
| Hardware       | Status |        | : Yes               |     |     |     |
| Hardware       | Error  | Reason | : --                |     |     |     |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/2(identifiedinthis
examplecommandbytheVLAN):
| switch#        | show        | ipv4 source-lockdown |                     | binding                             | vlan | 100 |
| -------------- | ----------- | -------------------- | ------------------- | ----------------------------------- | ---- | --- |
| Interface      | Name        |                      | : 1/1/2             |                                     |      |     |
| VLAN Id        |             |                      | : 100               |                                     |      |     |
| MAC Address    |             |                      | : 00:50:56:96:04:4d |                                     |      |     |
| IP Address     |             |                      | : 120.168.43.52     |                                     |      |     |
| Time Remaining |             |                      | : 115               | seconds                             |      |     |
| Lockdown       | Status      |                      | : Yes               |                                     |      |     |
| Hardware       | Status      |                      | : No                |                                     |      |     |
| Hardware       | Error       | Reason               | : Resource          | unavailable                         |      |     |
| Command        | History     |                      |                     |                                     |      |     |
| Release        |             |                      |                     | Modification                        |      |     |
| 10.10          |             |                      |                     | Commandenabledon8360seriesswitches. |      |     |
| 10.07orearlier |             |                      |                     | --                                  |      |     |
| Command        | Information |                      |                     |                                     |      |     |
| Platforms      | Command     |                      | context             | Authority                           |      |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| IPv6 source |     | lockdown |     | commands |     |     |
| ----------- | --- | -------- | --- | -------- | --- | --- |
ipv6 source-binding
| ipv6 source-binding |     | <VLAN-ID> |     | <IPV6-ADDR> | <MAC-ADDR> | <IFNAME> |
| ------------------- | --- | --------- | --- | ----------- | ---------- | -------- |
no ipv6 source-binding <VLAN-ID> <IPV6-ADDR> <MAC-ADDR> <IFNAME>
Description
AddsstaticIPv6clientsourcebindinginformationtotheswitchIPv6bindingdatabase.Although
DHCPv6snoopingisoftenusedtodynamicallypopulatethebindingdatabase,thiscommandis
availableformanuallyaddingentriestotheswitchIPv6bindingdatabase.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 234

StaticallyconfiguredIPv6bindinginformationsupersedesanydynamicallycollectedbindinginformationforthe
sameclient.
Thenoformofthiscommandremovesthespecifiedbindingthatwasstaticallyconfiguredwiththeipv6
source-bindingcommand.Thenoformhasnoeffectonbindingsthatweredynamicallyconfigured
withDHCPv6snooping.
| Parameter |     |     | Description                                      |
| --------- | --- | --- | ------------------------------------------------ |
| <VLAN-ID> |     |     | SpecifiestheIDofanexistingVLANonwhichtheclientis |
connected.Range:1to4094.
| <IPV6-ADDR> |     |     | SpecifiestheclientIPv6address. |
| ----------- | --- | --- | ------------------------------ |
<MAC-ADDR>
SpecifiestheclientMACaddress.
| <IFNAME> |     |     | Specifiestheinterfaceonwhichtheclientisconnected. |
| -------- | --- | --- | ------------------------------------------------- |
Examples
AddingastaticIPv6binding:
switch(config)# ipv6 source-binding 2 2000::2 00:12:11:44:55:12 1/1/28
RemovingaIPv6binding:
switch(config)# no ipv6 source-binding 2 2000::2 00:12:11:44:55:12 1/1/28
| Command History     |         |         |                                     |
| ------------------- | ------- | ------- | ----------------------------------- |
| Release             |         |         | Modification                        |
| 10.10               |         |         | Commandenabledon8360seriesswitches. |
| 10.07orearlier      |         |         | --                                  |
| Command Information |         |         |                                     |
| Platforms           | Command | context | Authority                           |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ipv6 source-lockdown
ipv6 source-lockdown
no ipv6 source-lockdown
Description
EnablesIPv6sourcelockdownforallVLANsontheselectedinterface(port).
ThenoformofthiscommanddisablesIPv6sourcelockdownfortheselectedinterface(port).
IPSourceLockdown|235

Examples
EnablingIPv6sourcelockdownoninterface1/1/1:
switch(config)#
|                    |     | interface | 1/1/1           |     |     |
| ------------------ | --- | --------- | --------------- | --- | --- |
| switch(config-if)# |     | ipv6      | source-lockdown |     |     |
EnablingIPv6sourcelockdownoninterfacelag112:
| switch(config)#    |     | interface | lag112          |     |     |
| ------------------ | --- | --------- | --------------- | --- | --- |
| switch(config-if)# |     | ipv6      | source-lockdown |     |     |
DisablingIPv6sourcelockdownoninterface1/1/1:
| switch(config)#     |         | interface | 1/1/1                |                                     |     |
| ------------------- | ------- | --------- | -------------------- | ----------------------------------- | --- |
| switch(config-if)#  |         | no        | ipv6 source-lockdown |                                     |     |
| Command History     |         |           |                      |                                     |     |
| Release             |         |           |                      | Modification                        |     |
| 10.10               |         |           |                      | Commandenabledon8360seriesswitches. |     |
| 10.07orearlier      |         |           |                      | --                                  |     |
| Command Information |         |           |                      |                                     |     |
| Platforms           | Command |           | context              | Authority                           |     |
8360 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 source-lockdown |     |          | hardware |           | retry       |
| -------------------- | --- | -------- | -------- | --------- | ----------- |
| ipv6 source-lockdown |     | hardware | retry    | <VLAN-ID> | <IPV6-ADDR> |
Description
RetriestheIPV6sourcelockdownhardwareprogrammingforaclientidentifiedbyVLANandIPv6
address.
| Parameter |     |     |     | Description                                      |     |
| --------- | --- | --- | --- | ------------------------------------------------ | --- |
| <VLAN-ID> |     |     |     | SpecifiestheIDofanexistingVLANonwhichtheclientis |     |
connected.Range:1to4094.
| <IPV6-ADDR> |     |     |     | SpecifiestheclientIPv6address. |     |
| ----------- | --- | --- | --- | ------------------------------ | --- |
Example
ConfigureIPv6sourcelockdownhardwareretryfortheclientonVLAN1.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 236

| switch(config)# |             | ipv6 | source-lockdown |     | hardware                            | retry 1 2000::2 |     |     |
| --------------- | ----------- | ---- | --------------- | --- | ----------------------------------- | --------------- | --- | --- |
| Command         | History     |      |                 |     |                                     |                 |     |     |
| Release         |             |      |                 |     | Modification                        |                 |     |     |
| 10.10           |             |      |                 |     | Commandenabledon8360seriesswitches. |                 |     |     |
| 10.07orearlier  |             |      |                 |     | --                                  |                 |     |     |
| Command         | Information |      |                 |     |                                     |                 |     |     |
| Platforms       | Command     |      | context         |     | Authority                           |                 |     |     |
8360 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show      | ipv6 source-binding |     |            |     |     |     |     |     |
| --------- | ------------------- | --- | ---------- | --- | --- | --- | --- | --- |
| show ipv6 | source-binding      |     | [vsx-peer] |     |     |     |     |     |
Description
ShowsallIPv6staticsourcebindinginformationirrespectiveofsourcelockdownconfiguration.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingallIPv6sourcebindinginformation:
|      | switch# |      | show | ipv6 source-binding |     |           |      |              |
| ---- | ------- | ---- | ---- | ------------------- | --- | --------- | ---- | ------------ |
| PORT |         | VLAN |      | MAC-ADDRESS         |     | HW-STATUS | FROM | IPv6-ADDRESS |
-------------- --------- ----------------- --------- -------- -------------
| 1/1/1          |         | 1234 |     | 00:50:56:96:e4:cf |                                     | Yes/No | static | 3000::1 |
| -------------- | ------- | ---- | --- | ----------------- | ----------------------------------- | ------ | ------ | ------- |
| 1/1/1          |         | 1    |     | 00:50:56:96:04:4d |                                     | Yes/No | static | 3000::2 |
| 1/1/24         |         | 1    |     | 00:01:01:00:00:01 |                                     | Yes    | static | 1001::1 |
| Command        | History |      |     |                   |                                     |        |        |         |
| Release        |         |      |     |                   | Modification                        |        |        |         |
| 10.10          |         |      |     |                   | Commandenabledon8360seriesswitches. |        |        |         |
| 10.07orearlier |         |      |     |                   | --                                  |        |        |         |
IPSourceLockdown|237

| Command   |     | Information |         |     |         |           |     |
| --------- | --- | ----------- | ------- | --- | ------- | --------- | --- |
| Platforms |     |             | Command |     | context | Authority |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | ipv6 |     | source-lockdown |     |     |     |     |
| ---- | ---- | --- | --------------- | --- | --- | --- | --- |
show ipv6 source-lockdown [binding [interface <IFNAME> | ip <IPV6-ADDR> | mac <MAC-ADDR>
| |   | vlan <VLAN-ID>] |     |     | | interface | <IFNAME>] | [vsx-peer] |     |
| --- | --------------- | --- | --- | ----------- | --------- | ---------- | --- |
Description
ShowssummaryordetailedIPv6sourcelockdowninformation.Whenenteredwithoutparameters,
summarystatusinformationforallinterfaces(ports)inthebindingdatabaseisshown.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
binding Specifiesthatdetailedlockdownbindingrecordinformationisto
bedisplayed.Thebindingdatabaserecordcanbeidentifiedby
anyoneofinterface(port),ip,mac,orvlan.
interface <IFNAME> Specifiestheclientinterface(port).Whenenteredwithoutthe
bindingparameter,thesummarystatusinformationisdisplayed
forthespecifiedinterface.
| ip  | <IPV6-ADDR> |     |     |     |     | SpecifiestheclientIPv6address. |     |
| --- | ----------- | --- | --- | --- | --- | ------------------------------ | --- |
| mac | <MAC-ADDR>  |     |     |     |     | SpecifiestheclientMACaddress.  |     |
vlan <VLAN-ID> SpecifiestheIDofanexistingVLANonwhichtheclientis
connected.Range:1to4094.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingthesummarystatusinformationforallinterfacesinthebindingdatabase:
|     | switch#   | show | ipv6     | source-lockdown |           |     |     |
| --- | --------- | ---- | -------- | --------------- | --------- | --- | --- |
|     | INTERFACE |      | LOCKDOWN |                 | HW-STATUS |     |     |
|     | --------- |      | -------- |                 | --------- |     |     |
|     | 1/1/1     |      | Yes      |                 | Yes       |     |     |
|     | 1/1/2     |      | Yes      |                 | Yes       |     |     |
|     | lag112    |      | Yes      |                 | Yes       |     |     |
Showingthesummarystatusinformationforthespecifiedinterfaceinthebindingdatabase:
switch#
|     |     | show | ipv6 | source-lockdown |     | interface | 1/1/2 |
| --- | --- | ---- | ---- | --------------- | --- | --------- | ----- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 238

| INTERFACE | LOCKDOWN | HW-STATUS |     |     |
| --------- | -------- | --------- | --- | --- |
| --------- | -------- | --------- |     |     |
| 1/1/2     | Yes      | No        |     |     |
Showingthedetailedbindingrecordandrelatedinformationforallinterfacesinthebindingdatabase:
| switch#        | show ipv6 source-lockdown |                                 | binding     |     |
| -------------- | ------------------------- | ------------------------------- | ----------- | --- |
| Interface      | Name                      | : 1/1/1                         |             |     |
| VLAN Id        |                           | : 1234                          |             |     |
| MAC Address    |                           | : 00:50:56:96:e4:cf             |             |     |
| IP Address     |                           | : aaaa:bbbb:cccc:dddd:eeee:1234 |             |     |
| Time Remaining |                           | : static                        |             |     |
| Lockdown       | Status                    | : Yes                           |             |     |
| Hardware       | Status                    | : Yes                           |             |     |
| Hardware       | Error Reason              | : --                            |             |     |
| Interface      | Name                      | : 1/1/2                         |             |     |
| VLAN Id        |                           | : 1234                          |             |     |
| MAC Address    |                           | : 00:50:56:96:04:4d             |             |     |
| IP Address     |                           | : 4000::1                       |             |     |
| Time Remaining |                           | : 3290 seconds                  |             |     |
| Lockdown       | Status                    | : Yes                           |             |     |
| Hardware       | Status                    | : No                            |             |     |
| Hardware       | Error Reason              | : Resource                      | unavailable |     |
| Interface      | Name                      | : lag112                        |             |     |
| VLAN Id        |                           | : 151                           |             |     |
| MAC Address    |                           | : 00:50:56:96:d8:3d             |             |     |
| IP Address     |                           | : 1001::5                       |             |     |
| Time Remaining |                           | : 1200 seconds                  |             |     |
| Lockdown       | Status                    | : No                            |             |     |
| Hardware       | Status                    | : Yes                           |             |     |
| Hardware       | Error Reason              | : --                            |             |     |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/2:
| switch#        | show ipv6 source-lockdown |                     | binding     | interface 1/1/2 |
| -------------- | ------------------------- | ------------------- | ----------- | --------------- |
| Interface      | Name                      | : 1/1/2             |             |                 |
| VLAN Id        |                           | : 1234              |             |                 |
| MAC Address    |                           | : 00:50:56:96:04:4d |             |                 |
| IP Address     |                           | : 4000::1           |             |                 |
| Time Remaining |                           | : 3290 seconds      |             |                 |
| Lockdown       | Status                    | : Yes               |             |                 |
| Hardware       | Status                    | : No                |             |                 |
| Hardware       | Error Reason              | : Resource          | unavailable |                 |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/2(identifiedinthis
examplecommandbytheIPaddress):
| switch#     | show ipv6 source-lockdown |                     | binding | ip 4000::1 |
| ----------- | ------------------------- | ------------------- | ------- | ---------- |
| Interface   | Name                      | : 1/1/2             |         |            |
| VLAN Id     |                           | : 1234              |         |            |
| MAC Address |                           | : 00:50:56:96:04:4d |         |            |
| IP Address  |                           | : 4000::1           |         |            |
IPSourceLockdown|239

| Time Remaining |              | : 515 seconds |     |     |
| -------------- | ------------ | ------------- | --- | --- |
| Lockdown       | Status       | : No          |     |     |
| Hardware       | Status       | : Yes         |     |     |
| Hardware       | Error Reason | : --          |     |     |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/1(identifiedinthis
examplecommandbytheMACaddress):
switch# show ipv6 source-lockdown binding mac 00:50:56:96:e4:cf
| Interface      | Name         | : 1/1/1                         |     |     |
| -------------- | ------------ | ------------------------------- | --- | --- |
| VLAN Id        |              | : 1234                          |     |     |
| MAC Address    |              | : 00:50:56:96:e4:cf             |     |     |
| IP Address     |              | : aaaa:bbbb:cccc:dddd:eeee:1234 |     |     |
| Time Remaining |              | : static                        |     |     |
| Lockdown       | Status       | : Yes                           |     |     |
| Hardware       | Status       | : Yes                           |     |     |
| Hardware       | Error Reason | : --                            |     |     |
Showingthedetailedbindingrecordandrelatedinformationforinterfacelag112(identifiedinthis
examplecommandbytheVLAN):
| switch#        | show ipv6 source-lockdown |                     | binding vlan                        | 151 |
| -------------- | ------------------------- | ------------------- | ----------------------------------- | --- |
| Interface      | Name                      | : lag112            |                                     |     |
| VLAN Id        |                           | : 151               |                                     |     |
| MAC Address    |                           | : 00:50:56:96:d8:3d |                                     |     |
| IP Address     |                           | : 1001::5           |                                     |     |
| Time Remaining |                           | : 1200 seconds      |                                     |     |
| Lockdown       | Status                    | : No                |                                     |     |
| Hardware       | Status                    | : Yes               |                                     |     |
| Hardware       | Error Reason              | : --                |                                     |     |
| Command        | History                   |                     |                                     |     |
| Release        |                           |                     | Modification                        |     |
| 10.10          |                           |                     | Commandenabledon8360seriesswitches. |     |
| 10.07orearlier |                           |                     | --                                  |     |
| Command        | Information               |                     |                                     |     |
| Platforms      | Command                   | context             | Authority                           |     |
8360 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 240

|          |                 |          |         |         | Chapter  | 11     |
| -------- | --------------- | -------- | ------- | ------- | -------- | ------ |
|          |                 | Internet | Control | Message | Protocol | (ICMP) |
| Internet | Control Message | Protocol | (ICMP)  |         |          |        |
TheInternetControlMessageProtocol(ICMP)isasupportingprotocolintheInternetprotocolsuite.The
protocolisusedbynetworkdevices,includingrouters,tosenderrormessagesandoperational
information.Forexample,anICMPmessagemightindicatethatarequestedserviceisnotavailable.
AnotherexampleofanICMPmessagemightbethatahostorroutercouldnotbereached.
| ICMP | message types |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- |
Thetypefieldidentifiesthetypeofmessagesentbythehostorgateway.
| Type | ICMP messages |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- |
0 EchoReply(PingReply,usedwithType8,PingRequest)
3 DestinationUnreachable
4 SourceQuench
5 Redirect
8 EchoRequest(PingRequest,usedwithType0,PingReply)
9 RouterAdvertisement(UsedwithType9)
10 RouterSolicitation(UsedwithType10)
11 TimeExceeded
12 ParameterProblem
13 TimestampRequest(UsedwithType14)
14 TimestampReply(UsedwithType13)
15 InformationRequest(obsolete)(UsedwithType16)
16 InformationReply(obsolete)(UsedwithType15)
17 AddressMaskRequest(UsedwithType17)
18 AddressMaskReply(UsedwithType18)
| When | ICMP messages | are | sent |     |     |     |
| ---- | ------------- | --- | ---- | --- | --- | --- |
241
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries)

ICMPmessagesaresentwhenoneormoreofthefollowingscenariosoccur:
n Adatagramcannotreachitsdestination.
n Thegatewaydoesnothavethebufferingcapacitytoforwardadatagram.
n Thegatewaycandirectthehosttosendtrafficonashorterroute.
| ICMP | redirect | messages |     |     |
| ---- | -------- | -------- | --- | --- |
ICMPredirectmessagesareusedbyrouterstonotifythehostsonthedatalinkthatabetterrouteis
availableforaparticulardestination.
| When | ICMP | redirect | messages | are sent |
| ---- | ---- | -------- | -------- | -------- |
Theswitchisconfiguredtosendredirectsbydefault.ICMPredirectmessagesaresentwhenoneor
moreofthefollowingscenariosoccur:
n Theinterfaceonwhichthepacketcomesintotherouteristhesameinterfaceonwhichthepacket
getsroutedout.
ThesubnetornetworkofthesourceIPaddressisonthesamesubnetornetworkofthenext-hopIP
n
addressoftheroutedpacket.
n Thedatagramisnotsource-routed.
Thedestinationunicastaddressisunreachable.Inthiscase,theroutergeneratestheICMP
n
destinationunreachablemessagetoinformthesourcehostaboutthesituation.
| ICMP    | commands      |     |     |     |
| ------- | ------------- | --- | --- | --- |
| ip icmp | redirect      |     |     |     |
| ip icmp | redirect      |     |     |     |
| no ip   | icmp redirect |     |     |     |
Description
EnablesthesendingofICMPv4andICMPv6redirectmessagestothesourcehost.Enabledbydefault.
ThenoformofthiscommanddisablesICMPv4andICMPv6redirectmessagestothesourcehost.
Examples
EnablingICMPredirectmessages:
switch(config)#
|     |     | ip icmp | redirect |     |
| --- | --- | ------- | -------- | --- |
DisablingICMPredirectmessages:
| switch(config)# |         | no ip icmp | redirect |     |
| --------------- | ------- | ---------- | -------- | --- |
| Command         | History |            |          |     |
InternetControlMessageProtocol(ICMP)|242

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip icmp throttle    |                     |     |     |
| ------------------- | ------------------- | --- | --- |
| ip icmp throttle    | <PACKET-INTERVAL>   |     |     |
| no ip icmp throttle | [<PACKET-INTERVAL>] |     |     |
Description
UsedtoconfigurethethrottleparameterforbothICMPv4andICMPv6errormessagesandredirect
messages.
ThenoformofthiscommanddisablesthethrottleparameterforbothICMPv4andICMPv6error
messagesandredirectmessages.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PACKET-INTERVAL> SpecifiestheICMPv4/v6packetintervalinseconds.Default:1
second.Range:1-86400.
Examples
EnablingthethrottleparameterforbothICMPv4andICMPv6errormessagesandredirectmessages:
| switch(config)# | ip  | icmp throttle | 3000 |
| --------------- | --- | ------------- | ---- |
DisablingthethrottleparameterforbothICMPv4andICMPv6errormessagesandredirectmessages:
| switch(config)# | no  | ip icmp throttle |                                                   |
| --------------- | --- | ---------------- | ------------------------------------------------- |
| Command History |     |                  |                                                   |
| Release         |     |                  | Modification                                      |
| 10.8            |     |                  | Addedtheoptional<PACKET-INTERVAL>parametertotheno |
formofthecommand.
| 10.07orearlier      |     |     | --  |
| ------------------- | --- | --- | --- |
| Command Information |     |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 243

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip icmp unreachable |     |     |     |
| ------------------- | --- | --- | --- |
ip icmp unreachable
| no ip icmp unreachable |     |     |     |
| ---------------------- | --- | --- | --- |
Description
EnablesthesendingofICMPv4andICMPv6destinationunreachablemessagesontheswitchtoa
sourcehostwhenaspecifichostisunreachable.Theunreachablehostaddressoriginatesfromthe
failedpacked.Defaultsetting.
ThenoformofthiscommanddisablesthesendingofICMPv4andICMPv6destinationunreachable
messagesfromtheswitchtoasourcehostwhenaspecifichostisunreachable.Thiscommanddoesnot
preventotherhostsfromsendinganICMPunreachablemessage.
Examples
EnablingICMPv4andICMPv6destinationunreachablemessagestoasourcehost:
| switch(config)# | ip  | icmp unreachable |     |
| --------------- | --- | ---------------- | --- |
DisablingICMPv4andICMPv6destinationunreachablemessagestoasourcehost:
| switch(config)#     | no      | ip icmp unreachable |              |
| ------------------- | ------- | ------------------- | ------------ |
| Command History     |         |                     |              |
| Release             |         |                     | Modification |
| 10.07orearlier      |         |                     | --           |
| Command Information |         |                     |              |
| Platforms           | Command | context             | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
InternetControlMessageProtocol(ICMP)|244

Chapter 12

DNS

DNS

The Domain Name System (DNS) is the Internet protocol for mapping a hostname to its IP address. DNS
allows users to enter more readily memorable and intuitive hostnames, rather than IP addresses, to
identify devices connected to a network. It also allows a host to keep the same hostname even if it
changes its IP address.

Hostname resolution can be either static or dynamic.

n In static resolution, a local table is defined on the switch that associates hostnames with their IP
addresses. Static tables can be used to speed up the resolution of frequently queried hosts.

n Dynamic resolution requires that the switch query a DNS server located elsewhere on the network.

Dynamic name resolution takes more time than static name resolution, but requires far less
configuration and management.

DNS client

The DNS client resolves hostnames to IP addresses for protocols that are running on the switch. When
the DNS client receives a request to resolve a hostname, it can do so in one of two ways:

n Forward the request to a DNS name server for resolution.

n Reply to the request without using a DNS name server, by resolving the name using a statically

defined table of hostnames and their associated IP addresses.

Configuring the DNS client

Procedure

1. Configure one or more DNS name servers with the command ip dns server.

2. To resolve DNS requests by appending a domain name to the requests, either configure a single
domain name with the command ip dns domain-name, or configure a list of up to six domain
names with the command ip dns domain-list.

3. To use static name resolution for certain hosts, associate an IP address to a host with the

command ip dns host.

4. Review your DNS configuration settings with the command show ip dns.

Examples

This example creates the following configuration:

n Defines the domain switch.com to append to all requests.

n Defines a DNS server with IPv4 address of 1.1.1.1.

n Defines a static DNS host named myhost1 with an IPv4 address of 3.3.3.3.

n DNS client traffic is sent on the default VRF (named default).

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

245

| switch(config)# |     | ip dns domain-name |     | switch.com |     |
| --------------- | --- | ------------------ | --- | ---------- | --- |
switch(config)#
|                 |                 | ip dns server-address |         | 1.1.1.1 |         |
| --------------- | --------------- | --------------------- | ------- | ------- | ------- |
| switch(config)# |                 | ip dns host           | myhost1 | 3.3.3.3 |         |
| switch(config)# |                 | exit                  |         |         |         |
| switch#         | show            | ip dns                |         |         |         |
| VRF             | Name : vrf_mgmt |                       |         |         |         |
| Host            | Name            |                       |         |         | Address |
--------------------------------------------------------------------------------
| VRF    | Name : vrf_default |              |     |     |         |
| ------ | ------------------ | ------------ | --- | --- | ------- |
| Domain | Name               | : switch.com |     |     |         |
| DNS    | Domain list        | :            |     |     |         |
| Name   | Server(s)          | : 1.1.1.1    |     |     |         |
| Host   | Name               |              |     |     | Address |
--------------------------------------------------------------------------------
myhost1
Thisexamplecreatesthefollowingconfiguration:
n DefinesthreedomainstoappendtoDNSrequestsdomain1.com,domain2.com,domain3.com
withtrafficforwardingonVRFmainvrf.
n DefinesaDNSserverwithanIPv6addressofc::13.
n DefinesaDNShostnamedmyhostwithanIPv4addressof3.3.3.3.
| switch(config)# |     | ip dns domain-list |     | domain1.com | vrf mainvrf |
| --------------- | --- | ------------------ | --- | ----------- | ----------- |
switch(config)#
|                 |                | ip dns domain-list    |              | domain2.com | vrf mainvrf |
| --------------- | -------------- | --------------------- | ------------ | ----------- | ----------- |
| switch(config)# |                | ip dns domain-list    |              | domain3.com | vrf mainvrf |
| switch(config)# |                | ip dns server-address |              | c::13       |             |
| switch(config)# |                | ip dns host           | myhost       | 3.3.3.3     | vrf mainvrf |
| switch(config)# |                | quit                  |              |             |             |
| switch#         | show           | ip dns mainvrf        |              |             |             |
| VRF             | Name : mainvrf |                       |              |             |             |
| Domain          | Name           | :                     |              |             |             |
| DNS             | Domain list    | : domain1.com,        | domain2.com, |             | domain3.com |
| Name            | Server(s)      | : c::13               |              |             |             |
| Host            | Name           |                       |              |             | Address     |
--------------------------------------------------------------------------------
myhost 3.3.3.3
| DNS       | client      | commands      |      |                  |     |
| --------- | ----------- | ------------- | ---- | ---------------- | --- |
| ip dns    | domain-list |               |      |                  |     |
| ip dns    | domain-list | <DOMAIN-NAME> | [vrf | <VRF-NAME>]      |     |
| no ip dns | domain-list | <DOMAIN-NAME> |      | [vrf <VRF-NAME>] |     |
Description
ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
DNS|246

Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
| switch(config)# |     |     | ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | --- | ------ | ----------- | --- | ----------- | --- |
| switch(config)# |     |     | ip dns | domain-list |     | domain2.com |     |
Thisexampledefinesalistwithtwoentries,domain2.comanddomain5.com,withrequestsbeingsent
onmainvrf.
| switch(config)# |     |     | ip dns | domain-list |     | domain2.com | vrf mainvrf |
| --------------- | --- | --- | ------ | ----------- | --- | ----------- | ----------- |
| switch(config)# |     |     | ip dns | domain-list |     | domain5.com | vrf mainvrf |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |             |         | no ip dns | domain-list |              | domain1.com |     |
| --------------- | ----------- | ------- | --------- | ----------- | ------------ | ----------- | --- |
| Command         | History     |         |           |             |              |             |     |
| Release         |             |         |           |             | Modification |             |     |
| 10.07orearlier  |             |         |           |             | --           |             |     |
| Command         | Information |         |           |             |              |             |     |
| Platforms       |             | Command | context   |             | Authority    |             |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | domain-name |     |               |     |       |            |     |
| --------- | ----------- | --- | ------------- | --- | ----- | ---------- | --- |
| ip dns    | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.
Bydefault,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip
dns domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 247

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DOMAIN-NAME> SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
vrf <VRF-NAME>
SpecifiesaVRFname.Default:default.
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     | ip  | dns | domain-name | domain.com |     |
| --------------- | --- | --- | --- | ----------- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |             | no      | ip dns  | domain-name | domain.com   |     |
| --------------- | ----------- | ------- | ------- | ----------- | ------------ | --- |
| Command         | History     |         |         |             |              |     |
| Release         |             |         |         |             | Modification |     |
| 10.07orearlier  |             |         |         |             | --           |     |
| Command         | Information |         |         |             |              |     |
| Platforms       |             | Command | context |             | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | host |             |           |           |                  |     |
| --------- | ---- | ----------- | --------- | --------- | ---------------- | --- |
| ip dns    | host | <HOST-NAME> | <IP-ADDR> |           | [ vrf <VRF-NAME> | ]   |
| no ip dns | host | <HOST-NAME> |           | <IP-ADDR> | [ vrf <VRF-NAME> | ]   |
Description
AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadof
queryingaDNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFis
defined,thedefaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
host <HOST-NAME> Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
DNS|248

Examples
| ThisexampledefinesanIPv4addressof |     |     |     |     | 3.3.3.3forhost1. |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
switch(config)#
|                                       |             |         | ip dns    | host | host1 | 3.3.3.3           |     |       |
| ------------------------------------- | ----------- | ------- | --------- | ---- | ----- | ----------------- | --- | ----- |
| ThisexampledefinesanIPv6addressofb::5 |             |         |           |      |       | forhost           | 1.  |       |
| switch(config)#                       |             |         | ip dns    | host | host1 | b::5              |     |       |
| Thisexampledefinesremovestheentryfor  |             |         |           |      |       | host 1withaddress |     | b::5. |
| switch(config)#                       |             |         | no ip dns | host | host1 | b::5              |     |       |
| Command                               | History     |         |           |      |       |                   |     |       |
| Release                               |             |         |           |      |       | Modification      |     |       |
| 10.07orearlier                        |             |         |           |      |       | --                |     |       |
| Command                               | Information |         |           |      |       |                   |     |       |
| Platforms                             |             | Command | context   |      |       | Authority         |     |       |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns    | server         | address |           |     |       |            |     |     |
| --------- | -------------- | ------- | --------- | --- | ----- | ---------- | --- | --- |
| ip dns    | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |     |
| no ip dns | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |     |
Description
ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 249

| switch(config)# | ip  | dns server-address |     | 1.1.1.1 |
| --------------- | --- | ------------------ | --- | ------- |
Thisexampledefinesanameserverata::1.
| switch(config)# | ip  | dns server-address |     | a::1 |
| --------------- | --- | ------------------ | --- | ---- |
Thisexampleremovesanameserverata::1.
| switch(config)#     | no      | ip dns server-address |              | a::1 |
| ------------------- | ------- | --------------------- | ------------ | ---- |
| Command History     |         |                       |              |      |
| Release             |         |                       | Modification |      |
| 10.07orearlier      |         |                       | --           |      |
| Command Information |         |                       |              |      |
| Platforms           | Command | context               | Authority    |      |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip dns |                            |     |     |     |
| ----------- | -------------------------- | --- | --- | --- |
| show ip dns | [vrf <VRF-NAME>][vsx-peer] |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
TheseexamplesdefineDNSsettingsandthenshowhowtheyaredisplayedwiththeshow ip dns
command.
| switch(config)# | ip  | dns domain-name | domain.com  |     |
| --------------- | --- | --------------- | ----------- | --- |
| switch(config)# | ip  | dns domain-list | domain5.com |     |
switch(config)#
|                 | ip  | dns domain-list    | domain8.com |         |
| --------------- | --- | ------------------ | ----------- | ------- |
| switch(config)# | ip  | dns server-address |             | 4.4.4.4 |
| switch(config)# | ip  | dns server-address |             | 6.6.6.6 |
DNS|250

| switch(config)# |     | ip dns | host | host3 | 5.5.5.5 |     |     |
| --------------- | --- | ------ | ---- | ----- | ------- | --- | --- |
switch(config)#
|                 |     | ip dns | host           | host2 | 2.2.2.2        |     |         |
| --------------- | --- | ------ | -------------- | ----- | -------------- | --- | ------- |
| switch(config)# |     | ip dns | host           | host3 | c::12          |     |         |
| switch(config)# |     | ip dns | domain-name    |       | reddomain.com  |     | vrf red |
| switch(config)# |     | ip dns | domain-list    |       | reddomain5.com |     | vrf red |
| switch(config)# |     | ip dns | domain-list    |       | reddomain8.com |     | vrf red |
| switch(config)# |     | ip dns | server-address |       | 4.4.4.5        |     | vrf red |
| switch(config)# |     | ip dns | server-address |       | 6.6.6.7        |     | vrf red |
| switch(config)# |     | ip dns | host           | host3 | 5.5.5.6        | vrf | red     |
| switch(config)# |     | ip dns | host           | host2 | 2.2.2.3        | vrf | red     |
| switch(config)# |     | ip dns | host           | host3 | c::13          | vrf | red     |
switch#
show ip dns
| VRF Name       | : default |                |         |             |     |     |     |
| -------------- | --------- | -------------- | ------- | ----------- | --- | --- | --- |
| Domain Name    | :         | domain.com     |         |             |     |     |     |
| DNS Domain     | list      | : domain5.com, |         | domain8.com |     |     |     |
| Name Server(s) |           | : 4.4.4.4,     | 6.6.6.6 |             |     |     |     |
| Host Name      |           | Address        |         |             |     |     |     |
-------------------------------
| host2          |       | 2.2.2.2           |         |     |                |     |     |
| -------------- | ----- | ----------------- | ------- | --- | -------------- | --- | --- |
| host3          |       | 5.5.5.5           |         |     |                |     |     |
| host3          |       | c::12             |         |     |                |     |     |
| VRF Name       | : red |                   |         |     |                |     |     |
| Domain Name    | :     | reddomain.com     |         |     |                |     |     |
| DNS Domain     | list  | : reddomain5.com, |         |     | reddomain8.com |     |     |
| Name Server(s) |       | : 4.4.4.5,        | 6.6.6.7 |     |                |     |     |
| Host Name      |       | Address           |         |     |                |     |     |
-------------------------------
| host2           |     | 2.2.2.3   |                |       |             |     |         |
| --------------- | --- | --------- | -------------- | ----- | ----------- | --- | ------- |
| host3           |     | 5.5.5.6   |                |       |             |     |         |
| host3           |     | c::13     |                |       |             |     |         |
| switch(config)# |     | ip dns    | domain-name    |       | domain.com  |     | vrf red |
| switch(config)# |     | ip dns    | domain-list    |       | domain5.com |     | vrf red |
| switch(config)# |     | ip dns    | domain-list    |       | domain8.com |     | vrf red |
| switch(config)# |     | ip dns    | server-address |       | 4.4.4.4     |     | vrf red |
| switch(config)# |     | ip dns    | server-address |       | 6.6.6.6     |     | vrf red |
| switch(config)# |     | ip dns    | host           | host3 | 5.5.5.5     | vrf | red     |
| switch(config)# |     | no ip dns | host           | host2 | 2.2.2.2     |     | vrf red |
| switch(config)# |     | ip dns    | host           | host3 | c::12       | vrf | red     |
switch#
|                | show  | ip dns vrf     | red     |             |     |     |     |
| -------------- | ----- | -------------- | ------- | ----------- | --- | --- | --- |
| VRF Name       | : red |                |         |             |     |     |     |
| Domain Name    | :     | domain.com     |         |             |     |     |     |
| DNS Domain     | list  | : domain5.com, |         | domain8.com |     |     |     |
| Name Server(s) |       | : 4.4.4.4,     | 6.6.6.6 |             |     |     |     |
| Host Name      |       | Address        |         |             |     |     |     |
-------------------------------
| host3   |         | 5.5.5.5 |     |     |     |     |     |
| ------- | ------- | ------- | --- | --- | --- | --- | --- |
| host3   |         | c::12   |     |     |     |     |     |
| Command | History |         |     |     |     |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 251

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|252

Chapter 13

ARP

ARP

ARP (Address Resolution Protocol) is used to map the network address assigned to a device to its
physical address. For example, on an Ethernet network, ARP maps layer 3 IPv4 network addresses to
layer 2 MAC addresses. (ARP does not work with IPv6 addresses. Instead, the Neighbor discovery
protocol is used.)

ARP operates at layer 2. ARP requests are broadcast to all devices on the local network segment and are
not forwarded by routers. ARP is enabled by default and cannot be disabled.

Proxy ARP

Proxy ARP allows a routing switch to answer ARP requests from devices on one network on behalf of
devices on another network. The ARP proxy is aware of the location of the traffic destination, and offers
its own MAC address as the final destination.

For example, if Proxy ARP is enabled on a routing switch connected to two subnets (10.10.10.0/24 and
20.20.20.0/24), the routing switch can respond to an ARP request from 10.10.10.69 for the MAC address
of the device with IP address 20.20.20.69.

Typically, the host that sent the ARP request then sends its packets to the switch that has the ARP proxy.
This switch then forwards the packets to the intended host through a mechanism such as a tunnel.

Proxy ARP is supported on L3 physical and VLAN interfaces. It is disabled by default. To enable proxy
ARP, routing must be enabled on the interface.

Local proxy ARP

Local proxy ARP is a technique by which a device on a given network answers the ARP queries for a host
address that is on the same network. It is primarily used to enable layer 3 communication between
hosts within a common subnet that are separated by layer 2 boundaries (Example: PVLAN). Local proxy
ARP is supported on L3 physical and VLAN interfaces.

Local proxy ARP is disabled by default. Routing must be enabled on the interface to enable local proxy
ARP.

Dynamic ARP inspection

ARP is used for resolving IP against MAC addresses on a broadcast network segment like the Ethernet
and was originally defined by Internet Standard RFC 826. ARP does not support any inherent security
mechanism and as such depends on simple datagram exchanges for the resolution, with many of these
being broadcast.

Because it is an unreliable and non-secure protocol, ARP is vulnerable to attacks. Some attacks may be
targeted toward the networks whereas other attacks may be targeted toward the switch itself. The
attacks primarily intend to create denial of service (DoS) for the other entities present in the network.

Most of the attacks are carried out in one of the following three forms:

n Overwhelming the switch control plane with too many ARP packets.

n Overwhelming the switch control plane with too many unresolved data packets.

n Masquerading as a trusted gateway/server by wrongly advertising ARPs.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

253

Severaldefensemechanismscanbeputinplaceonaswitchtoprotectagainstattacks:
n LimittheamountofARPactivityallowedfromahostoronaport.
n EnsurethatallARPpacketsareconsistentwithoneormorebindingdatabases,whichcanbecreated
throughvariousmeans.
n EnforceintegritychecksontheARPpacketstocheckagainstdifferentMACorIPaddressesinthe
EthernetorIPheaderandARPheader.
 Onlythefollowingissupported:
n EnablinganddisablingofDynamicARPInspectiononaVLANlevel(itdoesnothavetobeSVI).
n DefiningthememberportsofaVLANaseithertrustedoruntrusted.
n OnlyARPtrafficonuntrustedportssubjectedtochecks.
n Routedports(RoPs)alwaystreatedastrusted.
n ListeningtotheDHCPBindingstableandcheckeveryARPpackettomatchagainstthebinding.
ARPACLsarenotsupportedinthisreleaseandtheDHCPsnoopingtablewillbetheonlysourceof
binding.
| Configuring | proxy | ARP |     |
| ----------- | ----- | --- | --- |
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtoaninterfacewiththecommandinterface,ortoaninterfaceVLANwiththecommand
| interface | vlan,ortoaLAGwiththecommandinterface |     | lag. |
| --------- | ------------------------------------ | --- | ---- |
3. EnablelocalproxyARPwiththecommandip proxy-arp.
Examples
ThisexampleconfiguresproxyARPoninterface1/1/2
| switch# config     |           |           |     |
| ------------------ | --------- | --------- | --- |
| switch(config)#    | interface | 1/1/2     |     |
| switch(config-if)# | ip        | proxy-arp |     |
.
ThisexampleconfiguresproxyARPoninterfaceVLAN30.
| switch# config          |           |              |     |
| ----------------------- | --------- | ------------ | --- |
| switch(config)#         | interface | vlan 30      |     |
| switch(config-vlan-30)# |           | ip proxy-arp |     |
| Configuring             | local     | proxy ARP    |     |
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtoaninterfacewiththecommandinterface,ortoaninterfaceVLANwiththecommand
ARP|254

| interface | vlan,ortoaLAGwiththecommandinterface |     |     | lag. |
| --------- | ------------------------------------ | --- | --- | ---- |
3. EnablelocalproxyARPwiththecommandip local-proxy-arp.
Examples
ThisexampleconfigureslocalproxyARPoninterface1/1/2
| switch# config     |           |                    |     |     |
| ------------------ | --------- | ------------------ | --- | --- |
| switch(config)#    | interface | 1/1/2              |     |     |
| switch(config-if)# |           | ip local-proxy-arp |     |     |
ThisexampleconfigureslocalproxyARPoninterfaceVLAN30.
| switch# config          |           |                    |     |     |
| ----------------------- | --------- | ------------------ | --- | --- |
| switch(config)#         | interface | vlan               | 30  |     |
| switch(config-vlan-30)# |           | ip local-proxy-arp |     |     |
ARP commands
| arp inspection    | trust |     |     |     |
| ----------------- | ----- | --- | --- | --- |
| arp inspection    | trust |     |     |     |
| no arp inspection | trust |     |     |     |
Description
Configurestheinterfaceasatrusted.Allinterfacesareuntrustedbydefault.
Thenoformofthiscommandreturnstheinterfacetothedefaultstate(untrusted).
Example
Settinganinterfaceastrusted:
| switch(config-if)#  |         | arp inspection | trust        |     |
| ------------------- | ------- | -------------- | ------------ | --- |
| Command History     |         |                |              |     |
| Release             |         |                | Modification |     |
| 10.07orearlier      |         |                | --           |     |
| Command Information |         |                |              |     |
| Platforms           | Command | context        | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
arp process-grat-arp
arp process-grat-arp
no arp process-grat-arp
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 255

Description
EnablestheprocessingofgratuitousARPpacketsontheindividualportorgroupofL3portstogether.
Bydefault,thegratuitousARPprocessingisenabled.WhengratuitousARP(GARP)processingis
enabled,aswitchthatisadvertisinganychangesinitsMACthroughtheGARPwillreflectinthe
neighbortableoftheswitch.However,theswitchwillnotbeabletolearntheneighborthroughthe
GARP.ThisconfigurationisapplicableonlyonL3interfacessuchasROPs,subinterfaces,andSVIs.
ThenoformofthiscommanddisablestheprocessingofgratuitousARPpackets.
Example
EnablingtheprocessingofgratuitousARPpacketsontheinterface1/1/1:
| switch(config)#    | interface | 1/1/1                |     |
| ------------------ | --------- | -------------------- | --- |
| switch(config-if)# |           | no shutdown          |     |
| switch(config-if)# |           | arp process-grat-arp |     |
EnablingtheprocessingofgratuitousARPpacketsoninterfaces1/1/1to1/1/5:
| switch(config)#                 | interface | 1/1/1-1/1/5 |                      |
| ------------------------------- | --------- | ----------- | -------------------- |
| switch(config-if<1/1/1-1/1/5>)# |           |             | no shutdown          |
| switch(config-if<1/1/1-1/1/5>)# |           |             | arp process-grat-arp |
EnablingtheprocessingofgratuitousARPpacketsonsub-interface1/1/1.10:
AppliesonlytotheAruba6300,6400,and8360SwitchSeries.
| switch(config)#       | interface | 1/1/1.10             |     |
| --------------------- | --------- | -------------------- | --- |
| switch(config-subif)# |           | no shutdown          |     |
| switch(config-subif)# |           | arp process-grat-arp |     |
DisablingtheprocessingofgratuitousARPpacketsonVLANs2to100:
| switch(config)#                | interface | vlan    | 2-100                   |
| ------------------------------ | --------- | ------- | ----------------------- |
| switch(config-if-vlan<2-100>)# |           |         | no shutdown             |
| switch(config-if-vlan<2-100>)# |           |         | no arp process-grat-arp |
| Command History                |           |         |                         |
| Release                        |           |         | Modification            |
| 10.07orearlier                 |           |         | --                      |
| Command Information            |           |         |                         |
| Platforms                      | Command   | context | Authority               |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     | rightsforthiscommand. |
| --- | -------------- | --- | --------------------- |
config-subif
ARP|256

| arp ipv4 | mac         |             |                |            |     |     |
| -------- | ----------- | ----------- | -------------- | ---------- | --- | --- |
| arp ipv4 | <IPV4_ADDR> |             | mac <MAC_ADDR> |            |     |     |
| no arp   | ipv4        | <IPV4_ADDR> | mac            | <MAC_ADDR> |     |     |
Description
SpecifiesapermanentstaticneighborentryintheARPtable(forIPv4neighbors).
ThenoformofthiscommanddeletesapermanentstaticneighborentryfromtheARPtable.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
ipv4 <IPV4-ADDR> SpecifiestheIPaddressoftheneighbororthevirtualIPaddress
oftheclusterinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255..Range:4096to131072.Default:131072.
mac <MAC-ADDR> SpecifiestheMACaddressoftheneighbororthemulticastMAC
addressinIANAformat(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
Example
ConfiguringastaticARPentryonainterfaceVLAN10:
| switch(config)#         |     | interface |     | vlan     | 10      |                       |
| ----------------------- | --- | --------- | --- | -------- | ------- | --------------------- |
| switch(config-if-vlan)# |     |           |     | arp ipv4 | 2.2.2.2 | mac 01:00:5e:00:00:01 |
RemovingastaticARPentryoninterfaceVLAN10:
| switch(config)# |     | interface |     | vlan | 10  |     |
| --------------- | --- | --------- | --- | ---- | --- | --- |
switch(config-if-vlan)# no arp ipv4 2.2.2.2 mac 01:00:5e:00:00:01
| Command        | History     |         |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     |     | config-if-vlan |     |     | rightsforthiscommand. |     |
| --- | --- | -------------- | --- | --- | --------------------- | --- |
clear arp
| clear arp | [port | <PORT-ID> |     | | vrf {all-vrfs |     | | <VRF-NAME>}] |
| --------- | ----- | --------- | --- | --------------- | --- | -------------- |
Description
ClearsIPv4andIPv6neighborentriesfromtheARPtable.Ifyoudonotspecifyanyparameters,ARP
tableentriesareclearedforthedefaultVRF.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 257

| Parameter      |     |     | Description                               |
| -------------- | --- | --- | ----------------------------------------- |
| port <PORT-ID> |     |     | Specifiesaphysicalportontheswitch.Format: |
member/slot/port.Forexample:1/1/1..
| all-vrfs   |     |     | SelectsallVRFs.                         |
| ---------- | --- | --- | --------------------------------------- |
| <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |
Examples
ClearingallIPv4andIPv6neighborARPentriesforthedefaultVRF:
| switch# clear | arp |     |     |
| ------------- | --- | --- | --- |
ClearingallARPneighborentriesforaport:
switch#
clear arp 1/1/35
ClearingallIPv4andIPv6neighborARPentriesforallVRFs:
| switch# clear | arp vrf | all-vrfs |     |
| ------------- | ------- | -------- | --- |
ClearingallIPv4andIPv6neighborARPentriesforaspecificVRFinstance:
| switch# clear       | arp vrf | RED     |              |
| ------------------- | ------- | ------- | ------------ |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip local-proxy-arp
ip local-proxy-arp
no ip local-proxy-arp
Description
EnableslocalproxyARPonthespecifiedinterface.LocalproxyARPissupportedonLayer3physical
interfacesandonVLANinterfaces.ToenablelocalproxyARPonaninterface,routingmustbeenabled
onthatinterface.
ThenoformofthiscommanddisableslocalproxyARPonthespecifiedinterface.
ARP|258

Examples
EnablinglocalproxyARPoninterface1/1/1:
switch#
|                    | interface 1/1/1 |                    |     |
| ------------------ | --------------- | ------------------ | --- |
| switch(config-if)# |                 | ip local proxy-arp |     |
EnablinglocalproxyARPoninterfaceVLAN3:
| switch#                 | interface vlan | 3                  |     |
| ----------------------- | -------------- | ------------------ | --- |
| switch(config-if-vlan)# |                | ip local-proxy-arp |     |
DisablinglocalproxyARPononinterface1/1/1.
| switch#            | interface 1/1/1 |                       |              |
| ------------------ | --------------- | --------------------- | ------------ |
| switch(config-if)# |                 | no ip local-proxy-arp |              |
| Command            | History         |                       |              |
| Release            |                 |                       | Modification |
| 10.07orearlier     |                 |                       | --           |
| Command            | Information     |                       |              |
| Platforms          | Command         | context               | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|                  | config-if-vlan |                | rightsforthiscommand. |
| ---------------- | -------------- | -------------- | --------------------- |
| ipv6 neighbor    | mac            |                |                       |
| ipv6 neighbor    | <IPV6-ADDR>    | mac <MAC-ADDR> |                       |
| no ipv6 neighbor | <IPV6-ADDR>    | mac <MAC-ADDR> |                       |
Description
SpecifiesapermanentstaticneighborentryintheARPtable(forIPv6neighbors).
ThenoformofthiscommanddeletesapermanentstaticneighborentryfromtheARPtable.
| Parameter    |     |     | Description                      |
| ------------ | --- | --- | -------------------------------- |
| <IPV6-ADDR>> |     |     | SpecifiesanIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
| mac <MAC-ADDR>> |     |     | SpecifiestheMACaddressoftheneighbor |
| --------------- | --- | --- | ----------------------------------- |
(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0
toF.Range:4096to131072.Default:131072.
Example
| CreatesastaticARPentryoninterface |     | 1/1/1. |     |
| --------------------------------- | --- | ------ | --- |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 259

| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|     |     | arp ipv6 neighbor | 2001:0db8:85a3::8a2e:0370:7334 | mac |
| --- | --- | ----------------- | ------------------------------ | --- |
00:50:56:96:df:c8
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip proxy-arp
ip proxy-arp
no ip proxy-arp
Description
EnablesproxyARPforthespecifiedLayer3interface.ProxyARPissupportedonLayer3physical
interfaces,LAGinterfaces,andVLANinterfaces.Itisdisabledbydefault.ToenableproxyARPonan
interface,routingmustbeenabledonthatinterface.
ThenoformofthiscommanddisablesproxyARPforthespecifiedinterface.
Examples
EnablingproxyARPoninterface1/1/1:
| switch# interface       | 1/1/1 |              |     |     |
| ----------------------- | ----- | ------------ | --- | --- |
| switch(config-if)#      |       | ip proxy-arp |     |     |
| EnablingproxyARPonVLAN  |       | 3:           |     |     |
| switch# interface       | vlan  | 3            |     |     |
| switch(config-if-vlan)# |       | ip proxy-arp |     |     |
EnablingproxyARPonaLAG11:
| switch(config)#        | int | lag 11       |     |     |
| ---------------------- | --- | ------------ | --- | --- |
| switch(config-lag-if)# |     | ip proxy-arp |     |     |
DisablingproxyARPoninterface1/1/1:
| switch# interface  | 1/1/1 |                 |     |     |
| ------------------ | ----- | --------------- | --- | --- |
| switch(config-if)# |       | no ip proxy-arp |     |     |
ARP|260

| Command History     |         |         |              |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| Release             |         |         | Modification |     |     |     |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     | rightsforthiscommand. |     |     |     |
| --- | -------------- | --- | --------------------- | --- | --- | --- |
config-lag-vlan
show arp
show arp [vsx-peer]
Description
ShowstheentriesintheARP(AddressResolutionProtocol)table.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
ThiscommanddisplaysinformationaboutARPentries,includingtheIPaddress,MACaddress,port,and
state.
Whennoparametersarespecified,theshow arpcommandshowsallARPentriesforthedefaultVRF
(VirtualRouterForwarding)instance.
Examples
| switch# show | arp |     |      |               |     |       |
| ------------ | --- | --- | ---- | ------------- | --- | ----- |
| IPv4 Address | MAC |     | Port | Physical Port |     | State |
-------------------------------------------------------------------------------
| 192.168.1.2  |        | 00:50:56:96:7b:e0 | vlan10 | 1/1/29 | stale     |     |
| ------------ | ------ | ----------------- | ------ | ------ | --------- | --- |
| 192.168.1.3  |        | 00:50:56:96:7b:ac | vlan10 | 1/1/1  | reachable |     |
| Total Number | Of ARP | Entries Listed-   | 2.     |        |           |     |
-------------------------------------------------------------------------------
| Command History     |     |     |              |     |     |     |
| ------------------- | --- | --- | ------------ | --- | --- | --- |
| Release             |     |     | Modification |     |     |     |
| 10.07orearlier      |     |     | --           |     |     |     |
| Command Information |     |     |              |     |     |     |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 261

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show arp            | inspection | interface |     |     |
| ------------------- | ---------- | --------- | --- | --- |
| show arp inspection | interface  |           |     |     |
Description
DisplaysthecurrentconfigurationofdynamicARPinspectiononaVLANorinterface.
Examples
| switch# | show arp inspection |     | interface |     |
| ------- | ------------------- | --- | --------- | --- |
---------------------------------------------------------------------------
| Interface |     | Trust-State |     |     |
| --------- | --- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 |     | Untrusted |     |     |
| ----- | --- | --------- | --- | --- |
---------------------------------------------------------------------------
| switch# | show arp inspection |     | interface | vsx-peer |
| ------- | ------------------- | --- | --------- | -------- |
---------------------------------------------------------------------------
| Interface |     | Trust-State |     |     |
| --------- | --- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1  |     | Untrusted |     |     |
| ------ | --- | --------- | --- | --- |
| lag100 |     | Trusted   |     |     |
---------------------------------------------------------------------------
| switch# | show arp inspection |     | interface | 1/1/1 |
| ------- | ------------------- | --- | --------- | ----- |
---------------------------------------------------------------------------
| Interface |     | Trust-State |     |     |
| --------- | --- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 |     | Untrusted |     |     |
| ----- | --- | --------- | --- | --- |
---------------------------------------------------------------------------
| Command        | History     |         |     |              |
| -------------- | ----------- | ------- | --- | ------------ |
| Release        |             |         |     | Modification |
| 10.07orearlier |             |         |     | --           |
| Command        | Information |         |     |              |
| Platforms      | Command     | context |     | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
ARP|262

| show arp            | inspection | statistics |     |     |     |
| ------------------- | ---------- | ---------- | --- | --- | --- |
| show arp inspection | statistics |            |     |     |     |
Description
DisplaysstatisticsaboutforwardedanddroppedARPpackets.
Examples
| switch# | show arp inspection |     | statistics | vlan | 1-200 |
| ------- | ------------------- | --- | ---------- | ---- | ----- |
-----------------------------------------------------------------
| VLAN | Name |     | Forwarded |     | Dropped |
| ---- | ---- | --- | --------- | --- | ------- |
-----------------------------------------------------------------
| 1   | DEFAULT_VLAN_1 |     | 0   |     | 0   |
| --- | -------------- | --- | --- | --- | --- |
-----------------------------------------------------------------
| switch# | show arp inspection |     | statistics | vlan |     |
| ------- | ------------------- | --- | ---------- | ---- | --- |
-----------------------------------------------------------------
| VLAN | Name |     | Forwarded |     | Dropped |
| ---- | ---- | --- | --------- | --- | ------- |
-----------------------------------------------------------------
| 1   | DEFAULT_VLAN_1 |     | 0   |     | 0   |
| --- | -------------- | --- | --- | --- | --- |
| 200 | VLAN200        |     | 0   |     | 0   |
-----------------------------------------------------------------
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show arp | state |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- |
show arp state {all | failed | incomplete | permanent | reachable | stale} [vsx-peer]
Description
ShowsARP(AddressResolutionProtocol)cacheentriesthatareinthespecifiedstate.
| Parameter |     |     | Description                                    |     |     |
| --------- | --- | --- | ---------------------------------------------- | --- | --- |
| all       |     |     | ShowstheARPcacheentriesforallVRF(VirtualRouter |     |     |
Forwarding)instances.
failed
ShowstheARPcacheentriesthatareinfailedstate.The
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 263

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
neighbormighthavebeendeleted.
incomplete
ShowstheARPcacheentriesthatareinincompletestate.
Anincompletestatemeansthataddressresolutionisinprogress
andthelink-layeraddressoftheneighborhasnotyetbeen
determined.Asolicitationrequestwassent,andtheswitchis
waitingforasolicitationreplyoratimeout.
| permanent |     |     | ShowstheARPcacheentriesthatareinpermanentstate.ARP |     |     |
| --------- | --- | --- | -------------------------------------------------- | --- | --- |
entriesthatareinapermanentstatecanberemovedby
administrativeactiononly.
| reachable |     |     | ShowstheARPcacheentriesthatareinreachablestate, |     |     |
| --------- | --- | --- | ----------------------------------------------- | --- | --- |
meaningthattheneighborisknowntohavebeenreachable
recently.
| stale |     |     | ShowsARPcacheentriesthatareinstalestate. |     |     |
| ----- | --- | --- | ---------------------------------------- | --- | --- |
ARPcacheentriesareinthestalestateiftheelapsedtimeisin
excessoftheARPtimeoutinsecondssincethelastpositive
confirmationthattheforwardingpathwasfunctioningproperly.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# show | arp state | failed |      |               |       |
| ------------ | --------- | ------ | ---- | ------------- | ----- |
| IPv4 Address | MAC       |        | Port | Physical Port | State |
---------------------------------------------------------------------------
| 192.168.1.4         |         |         | vlan10       |     | failed |
| ------------------- | ------- | ------- | ------------ | --- | ------ |
| Command History     |         |         |              |     |        |
| Release             |         |         | Modification |     |        |
| 10.07orearlier      |         |         | --           |     |        |
| Command Information |         |         |              |     |        |
| Platforms           | Command | context | Authority    |     |        |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show arp         | summary   |                   |            |     |     |
| ---------------- | --------- | ----------------- | ---------- | --- | --- |
| show arp summary | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |     |     |
ARP|264

Description
ShowsasummaryoftheIPv4andIPv6neighborentriesontheswitchforallVRFsoraspecificVRF.
| Parameter      |     |     | Description             |     |
| -------------- | --- | --- | ----------------------- | --- |
| all-vrfs       |     |     | SelectsallVRFs.         |     |
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingsummaryARPinformationforallVRFs:
| switch#     | show arp | summary all-vrfs |        |      |
| ----------- | -------- | ---------------- | ------ | ---- |
| ARP Entry's | State    |                  | : IPv4 | IPv6 |
-------------------------------------------------------
| Number | of Reachable  | ARP entries | : 2 | 0   |
| ------ | ------------- | ----------- | --- | --- |
| Number | of Stale ARP  | entries     | : 0 | 0   |
| Number | of Failed     | ARP entries | : 2 | 2   |
| Number | of Incomplete | ARP entries | : 0 | 0   |
| Number | of Permanent  | ARP entries | : 0 | 0   |
-------------------------------------------------------
| Total ARP | Entries: | 6   | : 4 | 2   |
| --------- | -------- | --- | --- | --- |
-------------------------------------------------------
ShowingasummaryofallIPv4andIPv6neighborentriesontheprimaryandsecondary(peer)switches:
| vsx-primary# | show  | arp summary |      |      |
| ------------ | ----- | ----------- | ---- | ---- |
| ARP Entry's  | State |             | IPv4 | IPv6 |
---------------------------------------------------------
| Number | of Reachable  | ARP entries | 25858 | 32231 |
| ------ | ------------- | ----------- | ----- | ----- |
| Number | of Stale ARP  | entries     | 0     | 1     |
| Number | of Failed     | ARP entries | 0     | 257   |
| Number | of Incomplete | ARP entries | 0     | 0     |
| Number | of Permanent  | ARP entries | 0     | 0     |
---------------------------------------------------------
| Total ARP    | Entries- | 58347       | 25858    | 32489 |
| ------------ | -------- | ----------- | -------- | ----- |
| vsx-primary# | show     | arp summary | vsx-peer |       |
| ARP Entry's  | State    |             | IPv4     | IPv6  |
---------------------------------------------------------
| Number | of Reachable | ARP entries | 25858 | 32168 |
| ------ | ------------ | ----------- | ----- | ----- |
| Number | of Stale ARP | entries     | 0     | 3     |
| Number | of Failed    | ARP entries | 0     | 317   |
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 265

| Number | of Incomplete | ARP | entries | 0   | 0   |
| ------ | ------------- | --- | ------- | --- | --- |
| Number | of Permanent  | ARP | entries | 0   | 0   |
---------------------------------------------------------
| Total ARP | Entries- | 58346 |     | 25858 | 32488 |
| --------- | -------- | ----- | --- | ----- | ----- |
---------------------------------------------------------
| Command        | History     |         |     |              |     |
| -------------- | ----------- | ------- | --- | ------------ | --- |
| Release        |             |         |     | Modification |     |
| 10.07orearlier |             |         |     | --           |     |
| Command        | Information |         |     |              |     |
| Platforms      | Command     | context |     | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp         | timeout |               |            |     |     |
| ---------------- | ------- | ------------- | ---------- | --- | --- |
| show arp timeout |         | [<INTERFACE>] | [vsx-peer] |     |     |
Description
Showstheage-outperiodforeachARP(AddressResolutionProtocol)entryforaport,LAG,orVLAN
interface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<INTERFACE> Specifiesaphysicalport,VLAN,orLAGontheswitch.Forphysical
ports,usetheformatmember/slot/port(forexample,1/3/1).
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingARPtimeoutinformationforaport:
switch#
|              | show arp | timeout | 1/1/1 |     |     |
| ------------ | -------- | ------- | ----- | --- | --- |
| ARP Timeout: |          |         |       |     |     |
------------------
| Port    |         | VRF     |     |     | Timeout |
| ------- | ------- | ------- | --- | --- | ------- |
| 1/1/1   |         | default |     |     | 600     |
| Command | History |         |     |     |         |
ARP|266

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show arp           | vrf   |             |            |     |     |
| ------------------ | ----- | ----------- | ---------- | --- | --- |
| show arp {all-vrfs | | vrf | <VRF-NAME>} | [vsx-peer] |     |     |
Description
ShowstheARPtableforallVRFinstances,orforthenamedVRF.
| Parameter |     |     | Description       |     |     |
| --------- | --- | --- | ----------------- | --- | --- |
| all-vrfs  |     |     | SpecifiesallVRFs. |     |     |
vrf <VRF-NAME> SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingARPentriesforVRFtest.
| switch# show | arp vrf  | test |     |     |     |
| ------------ | -------- | ---- | --- | --- | --- |
| ARP IPv4     | Entries: |      |     |     |     |
-------------------------------------------------------
| IPv4 Address | MAC               |     | Port Physical | Port State | VRF  |
| ------------ | ----------------- | --- | ------------- | ---------- | ---- |
| 10.20.30.40  | 00:50:56:bd:6a:c5 |     | 1/1/29 1/1/29 | reachable  | test |
-------------------------------------------------------
| Total Number | Of ARP | Entries Listed: | 1.  |     |     |
| ------------ | ------ | --------------- | --- | --- | --- |
-------------------------------------------------------
| switch# show | arp all-vrfs |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- |
| ARP IPv4     | Entries:     |     |     |     |     |
-------------------------------------------------------
| IPv4 Address   | MAC               |     | Port Physical | Port State | VRF  |
| -------------- | ----------------- | --- | ------------- | ---------- | ---- |
| 192.168.120.10 | 00:50:56:bd:10:be |     | 1/1/32 1/1/32 | reachable  | red  |
| 10.20.30.40    | 00:50:56:bd:6a:c5 |     | 1/1/29 1/1/29 | reachable  | test |
-------------------------------------------------------
| Total Number | Of ARP | Entries Listed: | 2.  |     |     |
| ------------ | ------ | --------------- | --- | --- | --- |
-------------------------------------------------------
ShowingARPentriesforallVRFs.
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 267

| switch# | show          | arp all-vrfs |     |     |     |     |     |     |     |
| ------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| ARP     | IPv4 Entries: |              |     |     |     |     |     |     |     |
-------------------------------------------------------
| IPv4           | Address | MAC               |     |     | Port   | Physical | Port | State     | VRF  |
| -------------- | ------- | ----------------- | --- | --- | ------ | -------- | ---- | --------- | ---- |
| 192.168.120.10 |         | 00:50:56:bd:10:be |     |     | 1/1/32 | 1/1/32   |      | reachable | red  |
| 10.20.30.40    |         | 00:50:56:bd:6a:c5 |     |     | 1/1/29 | 1/1/29   |      | reachable | test |
-------------------------------------------------------
| Total | Number | Of ARP | Entries | Listed: | 2.  |     |     |     |     |
| ----- | ------ | ------ | ------- | ------- | --- | --- | --- | --- | --- |
-------------------------------------------------------
| Command        | History     |         |         |     |              |     |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- | --- | --- |
| Release        |             |         |         |     | Modification |     |     |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |     |     |
| Command        | Information |         |         |     |              |     |     |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show      | ipv6      | neighbors |     |       |             |            |     |     |     |
| --------- | --------- | --------- | --- | ----- | ----------- | ---------- | --- | --- | --- |
| show ipv6 | neighbors | {all-vrfs |     | | vrf | <VRF-NAME>} | [vsx-peer] |     |     |     |
Description
ShowsentriesintheARPtableforallIPv6neighborsforallVRFsorforaspecificVRF.
Whennoparametersarespecified,thiscommandshowsallARPentriesforthedefaultVRF,andstate
informationforreachableandstaleentriesonly.
| Parameter |     |     |     |     | Description       |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
| all-vrfs  |     |     |     |     | SpecifiesallVRFs. |     |     |     |     |
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# | show     | ipv6 neighbors |     |     |     |     |     |     |     |
| ------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| IPv6    | Entries: |                |     |     |     |     |     |     |     |
-------------------------------------------------------
| IPv6 | Address |     |     | MAC |     | Port |     | Physical | Port State |
| ---- | ------- | --- | --- | --- | --- | ---- | --- | -------- | ---------- |
ARP|268

fe80::a21d:48ff:fe8f:2700 a0:1d:48:8f:27:00 vlan2300 1/1/31 reachable
fe80::f603:43ff:fe80:a600 f4:03:43:80:a6:00 vlan2300 1/1/30 reachable
-------------------------------------------------------
| Total Number | Of IPv6 | Neighbors | Entries Listed: | 2.  |
| ------------ | ------- | --------- | --------------- | --- |
-------------------------------------------------------
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|           | (#)       |       | rightsforthiscommand. |     |
| --------- | --------- | ----- | --------------------- | --- |
| show ipv6 | neighbors | state |                       |     |
show ipv6 neighbors state {all | failed | incomplete | permanent | reachable | stale}
[vsx-peer]
Description
ShowsallIPv6neighborARP(AddressResolutionProtocol)cacheentries,orthosecacheentriesthatare
inthespecifiedstate.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
all
ShowsallARPcacheentries.
| failed |     |     | ShowsARPcacheentriesthatareinfailedstate.Theneighbor |     |
| ------ | --- | --- | ---------------------------------------------------- | --- |
mighthavebeendeleted.Settheneighbortobeunreachable.
| incomplete |     |     | ShowsARPcacheentriesthatareinincompletestate. |     |
| ---------- | --- | --- | --------------------------------------------- | --- |
Anincompletestatemeansthataddressresolutionisinprogress
andthelink-layeraddressoftheneighborhasnotyetbeen
determined.Thismeansthatasolicitationrequestwassent,and
youarewaitingforasolicitationreplyoratimeout.
| permanent |     |     | ShowsARPcacheentriesthatareinpermanentstate. |     |
| --------- | --- | --- | -------------------------------------------- | --- |
reachable ShowsARPcacheentriesthatareinreachablestate,meaning
thattheneighborisknowntohavebeenreachablerecently.
| stale |     |     | ShowsARPcacheentriesthatareinstalestate. |     |
| ----- | --- | --- | ---------------------------------------- | --- |
ARPcacheentriesareinthestalestateiftheelapsedtimeisin
excessoftheARPtimeoutinsecondssincethelastpositive
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 269

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
confirmationthattheforwardingpathwasfunctioningproperly.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# show | ipv6 neighbors |     | state all |               |            |
| ------------ | -------------- | --- | --------- | ------------- | ---------- |
| IPv6 Address |                |     | MAC       | Port Physical | Port State |
--------------------------------------------------------------------------------
| 100::2 |     |     | 48:0f:cf:af:f1:cc | lag1 lag1 |     |
| ------ | --- | --- | ----------------- | --------- | --- |
reachable
| 300::3 |     |     | 48:0f:cf:af:33:be | vlan3 1/4/20 |     |
| ------ | --- | --- | ----------------- | ------------ | --- |
reachable
| fe80::4a0f:cfff:feaf:f1cc |     |     | 48:0f:cf:af:f1:cc | lag1 lag1 |     |
| ------------------------- | --- | --- | ----------------- | --------- | --- |
reachable
| 200::3 |     |     | 48:0f:cf:af:33:be | 1/4/11 1/4/11 |     |
| ------ | --- | --- | ----------------- | ------------- | --- |
reachable
| fe80::4a0f:cfff:feaf:33be |     |     | 48:0f:cf:af:33:be | vlan3 1/4/20 |     |
| ------------------------- | --- | --- | ----------------- | ------------ | --- |
reachable
| Total Number | Of IPv6 | Neighbors | Entries Listed- | 5.  |     |
| ------------ | ------- | --------- | --------------- | --- | --- |
---------------------------------------------------------------------------------
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
ARP|270

Chapter 14
|         |                |       | Network | Load Balancing | (NLB) |
| ------- | -------------- | ----- | ------- | -------------- | ----- |
| Network | Load Balancing | (NLB) |         |                |       |
NetworkLoadBalancing(NLB)isaloadbalancingtechnologyforserverclustering.NLBsupportsload
sharingandredundancyamongserverswithinacluster.Toimplementfastfailover,NLBrequiresthat
theswitchforwardsnetworktraffictooneorallserversinthecluster.Eachserverfiltersoutthe
unexpectedtraffic.Formoreinformation,seeConfiguringnetworkinfrastructuretosupporttheNLB
operationmode
NLBisusedtospreadincomingrequestsacrossasmanyas32servers.Currently,NLBinAOS-CX
supportsonlyIGMPmulticastmode.TheIGMPmulticastmodesendsthepacketsoutoftheportswhich
connecttotheclustermembers.AssignastaticmulticastMACaddresswithintheInternetAssigned
NumbersAuthority(IANA)rangetothecluster'svirtualunicastIPaddress.Theclusteredserverssend
IGMPjoinstotheconfiguredmulticastclustergroup.IfIGMPsnoopingisenabled,theswitch
dynamicallypopulatestheIGMPsnoopingtablewiththeclusteredservers,whichpreventsunicast
flooding.
NLB commands
| arp ipv4 | mac              |                |     |     |     |
| -------- | ---------------- | -------------- | --- | --- | --- |
| arp ipv4 | <IPv4-ADDR>      | mac <MAC-ADDR> |     |     |     |
| no arp   | ipv4 <IPv4-ADDR> | mac <MAC-ADDR> |     |     |     |
Description
ConfiguresstaticARPmulticastontheinterface.
ThenoformofthiscommandremovesthestaticARPmulticastconfiguration.
| Parameter |     | Description |     |     |     |
| --------- | --- | ----------- | --- | --- | --- |
<IPv4-ADDR>
Specifiescluster'svirtualIPv4address.
<MAC-ADDR> SpecifiesmulticastMACaddressinIANAformat(xx:xx:xx:xx:xx:xx)
andnonIANAformat(xxxx.xxxx.xxxx).
Examples
ConfiguringstaticARPmulticastonaninterface:
| switch(config)#         | vlan      | 10               |        |     |     |
| ----------------------- | --------- | ---------------- | ------ | --- | --- |
| switch(config-vlan-10)# |           | no shutdown      |        |     |     |
| switch(config-vlan-10)# |           | ip igmp snooping | enable |     |     |
| switch(config-vlan-10)# |           | exit             |        |     |     |
| switch(config)#         | interface | vlan10           |        |     |     |
| switch(config-if-vlan)# |           | ip igmp enable   |        |     |     |
switch(config-if-vlan)# arp ipv4 10.1.30.254 mac 01:00:5e:7F:1E:FE
271
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries)

IfyourNLBVirtualIPaddressis10.1.30.254,thentheserverwilljointhe239.255.30.254IGMPgroup.ThisIGMP
groupismappedtothedestinationMACaddressof01:00:5e:7F:1E:FE.
On8320,8325,9300,and10000:TheclusterssendstheIGMPjointoanyvalidmulticastgroupIPaddressthatis
withintherangefrom224.0.0.0to239.255.255.255exceptreservedgroupIPaddresses.
| Command History     |         |         |                                                    |     |     |
| ------------------- | ------- | ------- | -------------------------------------------------- | --- | --- |
| Release             |         |         | Modification                                       |     |     |
| 10.08               |         |         | AddedNLBsupportfor8360Switchseries.                |     |     |
| 10.07orearlier      |         |         | --                                                 |     |     |
| Command Information |         |         |                                                    |     |     |
| Platforms           | Command | context | Authority                                          |     |     |
| 8320                |         |         | Administratorsorlocalusergroupmemberswithexecution |     |     |
config-ifand
| 8325 | config-if-vlan |     | rightsforthiscommand. |     |     |
| ---- | -------------- | --- | --------------------- | --- | --- |
8360
9300
10000
show arp
show arp
Description
DisplaysthestaticARPmulticastinformation.
Examples
DisplayingthestaticARPmulticastinformation:
| switch# show | arp |     |      |               |       |
| ------------ | --- | --- | ---- | ------------- | ----- |
| IPv4 Address | MAC |     | Port | Physical Port | State |
---------------------------------------------------------------------------
| 3.3.3.3      | 01:00:5e:00:00:02 |                 |        | 1/1/1 | permanent |
| ------------ | ----------------- | --------------- | ------ | ----- | --------- |
| 2.2.2.2      | 01:00:5e:00:00:01 |                 | vlan10 |       | permanent |
| Total Number | Of ARP            | Entries Listed- | 2.     |       |           |
---------------------------------------------------------------------------
| Command History |     |     |                                     |     |     |
| --------------- | --- | --- | ----------------------------------- | --- | --- |
| Release         |     |     | Modification                        |     |     |
| 10.08           |     |     | AddedNLBsupportfor8360Switchseries. |     |     |
| 10.07orearlier  |     |     | --                                  |     |     |
NetworkLoadBalancing(NLB)|272

| Command   | Information |         |     |           |     |     |     |     |
| --------- | ----------- | ------- | --- | --------- | --- | --- | --- | --- |
| Platforms | Command     | context |     | Authority |     |     |     |     |
8320 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 8325 | (#) |     |     | rightsforthiscommand. |     |     |     |     |
| ---- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
8360
9300
10000
| show    | ip igmp snooping |      | vlan      | group |            |     |     |     |
| ------- | ---------------- | ---- | --------- | ----- | ---------- | --- | --- | --- |
| show ip | igmp snooping    | vlan | <VLAN-ID> | group | IGMP-Group |     |     |     |
Description
Displaysmulticastjoins(membersofthecluster)participatingintheIGMPgroup.
Examples
DisplayingmulticastjoinsparticipatingintheIGMPgroup:
| switch# | show ip igmp             | snooping |     | vlan 10 | group 239.255.30.254 |       |           |         |
| ------- | ------------------------ | -------- | --- | ------- | -------------------- | ----- | --------- | ------- |
| VLAN    | ID : 10                  |          |     |         |                      |       |           |         |
| VLAN    | Name : VLAN10            |          |     |         |                      |       |           |         |
| Group   | Address : 239.255.30.254 |          |     |         |                      |       |           |         |
| Last    | Reporter : 10.1.30.254   |          |     |         |                      |       |           |         |
| Group   | Type : Filter            |          |     |         |                      |       |           |         |
|         |                          |          |     |         | V1                   | V2    | Sources   | Sources |
| Port    | Vers Mode                | Uptime   |     | Expires | Timer                | Timer | Forwarded | Blocked |
--------- ---- ---- --------- --------- --------- --------- --------- --------
| 1/1/6          | 2 EXC       | 0m 21s  |     | 1m 12s                              |     | 2m 48s | 0   | 0   |
| -------------- | ----------- | ------- | --- | ----------------------------------- | --- | ------ | --- | --- |
| Command        | History     |         |     |                                     |     |        |     |     |
| Release        |             |         |     | Modification                        |     |        |     |     |
| 10.08          |             |         |     | AddedNLBsupportfor8360Switchseries. |     |        |     |     |
| 10.07orearlier |             |         |     | --                                  |     |        |     |     |
| Command        | Information |         |     |                                     |     |        |     |     |
| Platforms      | Command     | context |     | Authority                           |     |        |     |     |
8320 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
| 8325 | (#) |     |     | rightsforthiscommand. |     |     |     |     |
| ---- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
8360
9300
10000
AOS-CX10.10IPServicesGuide|(83xx,10000SwitchSeries) 273

Chapter 15

Support and Other Resources

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.arubanetworks.com/support-services/

AOS-CX Switch Software Documentation
Portal

https://www.arubanetworks.com/techdocs/AOS-CX/help_
portal/Content/home.htm

Aruba Support Portal

https://asp.arubanetworks.com/

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

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

Airheads social
forums and
Knowledge Base

AOS-CX Switch
Software
Documentation
Portal

Aruba Hardware
Documentation

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

274

andTranslations
Portal
| Arubasoftware | https://asp.arubanetworks.com/downloads |     |
| ------------- | --------------------------------------- | --- |
| Software      | https://lms.arubanetworks.com/          |     |
licensing
End-of-Life https://www.arubanetworks.com/support-services/end-of-life/
information
| ArubaDeveloper | https://developer.arubanetworks.com/ |     |
| -------------- | ------------------------------------ | --- |
Hub
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheArubaSupportPortalortheHPEMyNetworkingWebsite.
| Aruba | Support | Portal |
| ----- | ------- | ------ |
https://asp.arubanetworks.com/downloads
IfyouareunabletofindyourproductintheArubaSupportPortal,youmayneedtosearchMy
Networking,whereoldernetworkingproductscanbefound:
My Networking
https://www.hpe.com/networking/support
Toviewandupdateyourentitlements,andtolinkyourcontractsandwarrantieswithyourprofile,goto
theHewlettPackardEnterpriseSupportCenterMore Information on Access to Support Materials
page:
https://support.hpe.com/portal/site/hpsc/aae/home/
AccesstosomeupdatesmightrequireproductentitlementwhenaccessedthroughtheHewlettPackard
EnterpriseSupportCenter.YoumusthaveanHPPassportsetupwithrelevantentitlements.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://asp.arubanetworks.com/notifications/subscriptions(requiresanactiveArubaSupportPortal
(ASP)accounttomanagesubscriptions).SecuritynoticesareviewablewithoutanASPaccount.
| Warranty | Information |     |
| -------- | ----------- | --- |
Toviewwarrantyinformationforyourproduct,gotohttps://www.arubanetworks.com/support-
services/product-warranties/.
| Regulatory | Information |     |
| ---------- | ----------- | --- |
Toviewtheregulatoryinformationforyourproduct,viewtheSafetyandComplianceInformationfor
Server,Storage,Power,Networking,andRackProducts,availableathttps://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts
| Additional | regulatory | information |
| ---------- | ---------- | ----------- |
SupportandOtherResources|275

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs,
product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback

Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.10 IP Services Guide | (83xx, 10000 Switch Series)

276