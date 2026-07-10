AOS-CX 10.09 IP Services
Guide

6200 Switch Series

Published: February 2022
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

Acknowledgments

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in the
United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

| 2

Contents
Contents
| Contents                            |                                     | 3   |
| ----------------------------------- | ----------------------------------- | --- |
| About this                          | document                            | 8   |
| Applicableproducts                  |                                     | 8   |
| Latestversionavailableonline        |                                     | 8   |
| Commandsyntaxnotationconventions    |                                     | 8   |
| Abouttheexamples                    |                                     | 9   |
| Identifyingswitchportsandinterfaces |                                     | 9   |
| IRDP                                |                                     | 11  |
| ConfiguringIRDP                     |                                     | 12  |
| IRDPcommands                        |                                     | 13  |
|                                     | diag-dumpirdpbasic                  | 13  |
|                                     | ipirdp                              | 14  |
|                                     | ipirdpholdtime                      | 14  |
|                                     | ipirdpmaxadvertinterval             | 15  |
|                                     | ipirdpminadvertinterval             | 16  |
|                                     | ipirdppreference                    | 17  |
|                                     | showipirdp                          | 18  |
| IPv6 Router                         | Advertisement                       | 19  |
| ConfiguringIPv6RA                   |                                     | 19  |
| IPv6RAscenario                      |                                     | 21  |
| IPv6RAcommands                      |                                     | 21  |
|                                     | ipv6address<global-unicast-address> | 22  |
|                                     | ipv6addressautoconfig               | 22  |
|                                     | ipv6addresslink-local               | 23  |
|                                     | ipv6ndcache-limit                   | 24  |
|                                     | ipv6nddadattempts                   | 25  |
|                                     | ipv6ndhop-limit                     | 26  |
|                                     | ipv6ndmtu                           | 26  |
|                                     | ipv6ndns-interval                   | 27  |
|                                     | ipv6ndprefix                        | 27  |
|                                     | ipv6ndradnssearch-list              | 29  |
|                                     | ipv6ndradnsserver                   | 30  |
|                                     | ipv6ndralifetime                    | 31  |
|                                     | ipv6ndramanaged-config-flag         | 32  |
|                                     | ipv6ndramax-interval                | 33  |
|                                     | ipv6ndramin-interval                | 33  |
|                                     | ipv6ndraother-config-flag           | 34  |
|                                     | ipv6ndrareachable-time              | 35  |
|                                     | ipv6ndraretrans-timer               | 36  |
|                                     | ipv6ndrouter-preference             | 36  |
|                                     | ipv6ndsuppress-ra                   | 37  |
|                                     | showipv6ndglobaltraffic             | 38  |
|                                     | showipv6ndinterface                 | 39  |
|                                     | showipv6ndinterfaceprefix           | 41  |
|                                     | showipv6ndradnssearch-list          | 42  |
3
AOS-CX10.09IPServicesGuide| (6200 SwitchSeries)

show ipv6 nd ra dns server

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
DHCPv4 relay commands

DHCPv6 relay agent

Configuring the DHCPv6 relay agent
DHCPv6 relay scenario 1
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

43

44
44
45
46
47
50
50
50
52
53
54
54
55
56
56
57
58

60
60
60
60
61
61
62
62
63
65
66
72
72
73
74
78
79
80
81
81
82
83
84
85
86
86
87
88
89
89
90
91
92
93
94
95

Contents | 4

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

DHCP server interoperation
DHCPv4 snooping conditions for dropping DHCPv4 packets
Protocol details
DHCPv4 snooping commands

clear dhcpv4-snooping binding
clear dhcpv4-snooping statistics
dhcpv4-snooping
dhcpv4-snooping (in config-vlan context)
dhcpv4-snooping allow-overwrite-binding
dhcpv4-snooping authorized-server
dhcpv4-snooping external-storage
dhcpv4-snooping flash-storage
dhcpv4-snooping max-bindings
dhcpv4-snooping option 82
dhcpv4-snooping trust
dhcpv4-snooping verify mac
show dhcpv4-snooping
show dhcpv4-snooping binding
show dhcpv4-snooping statistics

DHCPv6 snooping commands

clear dhcpv6-snooping binding
clear dhcpv6-snooping statistics
dhcpv6-snooping
dhcpv6-snooping (in config-vlan context)
dhcpv6-snooping authorized-server
dhcpv6-snooping external-storage
dhcpv6-snooping flash-storage
dhcpv6-snooping max-bindings
dhcpv6-snooping trust
show dhcpv6-snooping
show dhcpv6-snooping binding
show dhcpv6-snooping statistics

ND snooping
Overview
ND snooping commands

clear nd-snooping binding
clear nd-snooping statistics

96
98
99
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
107
108
110

112
112
112
113
113
113
114
115
116
116
117
118
119
121
122
123
124
124
126
126
127
127
128
129
130
131
132
133
134
135
136
137
138

140
140
140
140
142

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

5

|                                                       | nd-snooping                       |         |          |        | 142 |
| ----------------------------------------------------- | --------------------------------- | ------- | -------- | ------ | --- |
|                                                       | nd-snooping(inconfig-vlancontext) |         |          |        | 143 |
|                                                       | nd-snoopingmac-check              |         |          |        | 143 |
|                                                       | nd-snoopingprefix-list            |         |          |        | 144 |
|                                                       | nd-snoopingmax-bindings           |         |          |        | 145 |
|                                                       | nd-snoopingnd-guard               |         |          |        | 146 |
|                                                       | nd-snoopingra-guard               |         |          |        | 147 |
|                                                       | nd-snoopingra-drop                |         |          |        | 148 |
|                                                       | nd-snoopingtrust                  |         |          |        | 149 |
|                                                       | shownd-snooping                   |         |          |        | 149 |
|                                                       | shownd-snoopingbinding            |         |          |        | 151 |
|                                                       | shownd-snoopingprefix-list        |         |          |        | 151 |
|                                                       | shownd-snoopingstatistics         |         |          |        | 152 |
| IP Tunnels                                            |                                   |         |          |        | 154 |
| ConfiguringanIPtunnel                                 |                                   |         |          |        | 154 |
| CreatinganIPv6inIPv4tunnelfortraversingapublicnetwork |                                   |         |          |        | 155 |
| CreatinganIPv6inIPv6tunnelfortraversingapublicnetwork |                                   |         |          |        | 156 |
| IPtunnelscommands                                     |                                   |         |          |        | 157 |
|                                                       | description                       |         |          |        | 157 |
|                                                       | destinationip                     |         |          |        | 158 |
|                                                       | destinationipv6                   |         |          |        | 159 |
|                                                       | interfacetunnel                   |         |          |        | 160 |
|                                                       | ipaddress                         |         |          |        | 161 |
|                                                       | ipv6address                       |         |          |        | 162 |
|                                                       | ipmtu                             |         |          |        | 163 |
|                                                       | showinterfacetunnel               |         |          |        | 164 |
|                                                       | showrunning-configinterfacetunnel |         |          |        | 165 |
|                                                       | shutdown                          |         |          |        | 166 |
|                                                       | sourceip                          |         |          |        | 167 |
|                                                       | sourceipv6                        |         |          |        | 168 |
|                                                       | ttl                               |         |          |        | 168 |
| Internet                                              | Control                           | Message | Protocol | (ICMP) | 170 |
| ICMPmessagetypes                                      |                                   |         |          |        | 170 |
| WhenICMPmessagesaresent                               |                                   |         |          |        | 170 |
| ICMPredirectmessages                                  |                                   |         |          |        | 171 |
| WhenICMPredirectmessagesaresent                       |                                   |         |          |        | 171 |
| ICMPcommands                                          |                                   |         |          |        | 171 |
|                                                       | ipicmpredirect                    |         |          |        | 171 |
|                                                       | ipicmpthrottle                    |         |          |        | 172 |
|                                                       | ipicmpunreachable                 |         |          |        | 173 |
| DNS                                                   |                                   |         |          |        | 174 |
| DNSclient                                             |                                   |         |          |        | 174 |
| ConfiguringtheDNSclient                               |                                   |         |          |        | 174 |
| DNSclientcommands                                     |                                   |         |          |        | 175 |
|                                                       | ipdnsdomain-list                  |         |          |        | 175 |
|                                                       | ipdnsdomain-name                  |         |          |        | 176 |
|                                                       | ipdnshost                         |         |          |        | 177 |
|                                                       | ipdnsserveraddress                |         |          |        | 178 |
|                                                       | showipdns                         |         |          |        | 179 |
| ARP                                                   |                                   |         |          |        | 180 |
| ConfiguringproxyARP                                   |                                   |         |          |        | 181 |
| ConfiguringlocalproxyARP                              |                                   |         |          |        | 181 |
Contents|6

| ARPcommands           |                             |           | 182 |
| --------------------- | --------------------------- | --------- | --- |
|                       | arpinspection               |           | 182 |
|                       | arpinspectiontrust          |           | 182 |
|                       | arpipv4mac                  |           | 183 |
|                       | cleararp                    |           | 184 |
|                       | iplocal-proxy-arp           |           | 184 |
|                       | ipv6neighbormac             |           | 185 |
|                       | ipproxy-arp                 |           | 186 |
|                       | showarp                     |           | 187 |
|                       | showarpinspectioninterface  |           | 188 |
|                       | showarpinspectionstatistics |           | 189 |
|                       | showarpstate                |           | 189 |
|                       | showarpsummary              |           | 190 |
|                       | showarptimeout              |           | 192 |
|                       | showarpvrf                  |           | 193 |
|                       | showipv6neighbors           |           | 194 |
|                       | showipv6neighborsstate      |           | 195 |
| Support               | and Other                   | Resources | 197 |
| AccessingArubaSupport |                             |           | 197 |
| AccessingUpdates      |                             |           | 198 |
|                       | ArubaSupportPortal          |           | 198 |
|                       | MyNetworking                |           | 198 |
| WarrantyInformation   |                             |           | 198 |
| RegulatoryInformation |                             |           | 198 |
| DocumentationFeedback |                             |           | 199 |
7
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedforadministrators
responsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
Aruba6200SwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A)
n
| Latest | version | available | online |
| ------ | ------- | --------- | ------ |
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
| Command    | syntax | notation | conventions |
| ---------- | ------ | -------- | ----------- |
| Convention |        | Usage    |             |
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Itemsthat
appearliketheexampletextinthepreviouscolumnaretobeenteredexactly
asshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
n <example-text> substitutewithanactualvalueinacommandorincode:
<example-text>
n
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variablesare |     |
| --- | --- | --------------------------------------------------------------- | --- |
n example-text
enclosedinanglebrackets(< >).Substitutethetext—includingthe
n example-text
enclosinganglebrackets—withanactualvalue.
Foroutputformatswhereitalictextcanbedisplayed,variablesmight
n
ormightnotbeenclosedinanglebrackets.Substitutethetext
includingtheenclosinganglebrackets,ifany,withanactualvalue.
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
8
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |
| --------------------------- | ----- | ------------- | --- |

Convention

… or

...

Usage

Ellipsis:

n In code and screen examples, a vertical or horizontal ellipsis indicates an

omission of information.

n In syntax using brackets and braces, an ellipsis indicates items that can be

repeated. When an item followed by ellipses is enclosed in brackets, zero

or more items can be specified.

About the examples
Examples in this document are representative and might not match your particular switch or environment.

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

In certain configuration contexts, the prompt may include variable information. For example, when in the
VLAN configuration context, a VLAN number appears in the prompt:
switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

About this document | 9

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

10

Chapter 2

IRDP

IRDP

ICMP Router Discovery Protocol (IRDP), an extension of the ICMP, is independent of any routing protocol. It
allows hosts to discover the IP addresses of neighboring routers that can act as default gateways to reach
devices on other IP networks.

On the switches covered by this guide, IRDP is configured on a VLAN interface.

IRDP operation

IRDP uses the following types of ICMP messages:

n Router advertisement (RA): Sent by a router to advertise IP addresses (including the primary and

secondary IP addresses) and preference.

n Router solicitation (RS): Sent by a host to request the IP addresses of routers on the subnet.

An interface with IRDP enabled periodically broadcasts or multicasts an RA message to advertise its IP
addresses. A receiving host adds the IP addresses to its routing table, and selects the IP address with the
highest preference as the default gateway.

When a host attached to the subnet starts up, the host multicasts an RS message to request immediate
advertisements. If the host does not receive any advertisements, it retransmits the RS several times. If the
host does not discover the IP addresses of neighboring routers because of network problems, the host can
still discover them from periodic RAs.

IRDP allows hosts to discover neighboring routers, but it does not suggest the best route to a destination. If
a host sends a packet to a router that is not the best next hop, the host will receive an ICMP redirect
message from the router.

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
advertising intervals. This mechanism prevents the local link from being overloaded by a large number of
RAs sent simultaneously from routers.

As a best practice, shorten the advertising interval on a link that suffers high packet loss rates

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

11

Destination address of RA

An RA uses either of the following destination IP addresses:

n Broadcast address 255.255.255.255.

n Multicast address 224.0.0.1, which identifies all hosts on the local link.

By default, the destination IP address of an RA is the multicast address. If all listening hosts in a local area
network support IP multicast, specify 224.0.0.1 as the destination IP address.

Proxy-advertised IP addresses

By default, an interface advertises its primary and secondary IP addresses. You can specify IP addresses of
other gateways for an interface to proxy-advertise.

VRF support

In IP-based computer networks, virtual routing and forwarding (VRF) is a technology that allows multiple
instances of a routing table to co-exist within the same router at the same time. Because the routing
instances are independent, the same or overlapping IP addresses can be used without conflicting with each
other.

IRDP is VRF aware. As the router advertisements and solicit processing occurs on the interface, packet is
through the interface and corresponding VRF.

VSX synchronization

IRDP supports VSX synchronization. For more information on using VSX, see the Virtual Switching Extension
(VSX) Guide for your switch and software version

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

n Enables IRDP on the layer 3 VLAN interface 2 with packet type set to broadcast.

n Sets the hold time to 5000 seconds.

n Sets the advertisement interval to 30 seconds.

n Sets the minimum advertisement interval to 25 seconds.

n Sets the IRDP preference level to 25.

IRDP | 12

| switch(config)# |     | interface |     | vlan | 2   |     |     |
| --------------- | --- | --------- | --- | ---- | --- | --- | --- |
switch(config-if-vlan)#
|                         |     |     | ip  | irdp | broadcast         |      |     |
| ----------------------- | --- | --- | --- | ---- | ----------------- | ---- | --- |
| switch(config-if-vlan)# |     |     | ip  | irdp | holdtime          | 5000 |     |
| switch(config-if-vlan)# |     |     | ip  | irdp | maxadvertinterval |      | 30  |
| switch(config-if-vlan)# |     |     | ip  | irdp | minadvertinterval |      | 25  |
| switch(config-if-vlan)# |     |     | ip  | irdp | preference        | 25   |     |
IRDP commands
| diag-dump      | irdp  | basic |     |     |     |     |     |
| -------------- | ----- | ----- | --- | --- | --- | --- | --- |
| diag-dump irdp | basic |       |     |     |     |     |     |
Description
DisplaysdiagnosticinformationforIRDP.
Example
| switch# | diag-dump | irdp | basic |     |     |     |     |
| ------- | --------- | ---- | ----- | --- | --- | --- | --- |
=========================================================================
| [Start] | Feature | irdp | Time | : Thu | Jan 7 | 04:46:25 | 2021 |
| ------- | ------- | ---- | ---- | ----- | ----- | -------- | ---- |
=========================================================================
-------------------------------------------------------------------------
| [Start] | Daemon | hpe-rdiscd |     |     |     |     |     |
| ------- | ------ | ---------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| Interface: | vlan2 | (state | :   | Down) |     |     |     |
| ---------- | ----- | ------ | --- | ----- | --- | --- | --- |
rdisc ipv4 (enabled: 1, max:600, min:450, hold:1800, pref:0, isBcast:0)
| No advertisable |       | IPv4   | addresses |       | on the | interface |     |
| --------------- | ----- | ------ | --------- | ----- | ------ | --------- | --- |
| Interface:      | vlan1 | (state | :         | Down) |        |           |     |
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
| No advertisable |     | IPv4 | addresses |     | on the | interface |     |
| --------------- | --- | ---- | --------- | --- | ------ | --------- | --- |
-------------------------------------------------------------------------
| [End] Daemon |     | hpe-rdiscd |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
=========================================================================
| [End] Feature |     | irdp |     |     |     |     |     |
| ------------- | --- | ---- | --- | --- | --- | --- | --- |
=========================================================================
| Diagnostic-dump |     | captured | for | feature | irdp |     |     |
| --------------- | --- | -------- | --- | ------- | ---- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
13
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- | --- |

ip irdp
| ip irdp [broadcast | | multicast] |     |
| ------------------ | ------------ | --- |
no ip irdp
Description
EnablesIRDPonaninterfaceandspecifiesthepackettypethatisusedtosendadvertisements.Bydefault,
thepackettypeissettomulticast.IRDPisonlysupportedonlayer3interfaces.
ThenoformofthiscommanddisablesIRDPonaninterface.
Parameter Description
broadcast
AdvertisementsaresentasbroadcastpacketstoIPaddress
255.255.255.255.
multicast Advertisementsaresentasmulticastpacketstothemulticast
groupwithIPaddress24.0.0.1.Default.
Examples
EnablingIRDPoninterfacevlan2withpackettypesettothedefaultvalue(multicast).
| switch(config)#         | interface | vlan 2  |
| ----------------------- | --------- | ------- |
| switch(config-if-vlan)# |           | ip irdp |
EnablingIRDPoninterface1/1/1withpackettypesettobroadcast.
| switch(config)#         | interface | vlan 2            |
| ----------------------- | --------- | ----------------- |
| switch(config-if-vlan)# |           | ip irdp broadcast |
DisablingIRDP.
| switch(config)#         | interface | vlan 2     |
| ----------------------- | --------- | ---------- |
| switch(config-if-vlan)# |           | no ip irdp |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp holdtime    |        |     |
| ------------------- | ------ | --- |
| ip irdp holdtime    | <TIME> |     |
| no ip irdp holdtime | <TIME> |     |
IRDP|14

Description
Specifiesthemaximumamountoftimethehostwillconsideranadvertisementtobevaliduntilanewer
advertisementarrives.Whenanewadvertisementarrives,holdtimeisreset.Holdtimemustbegreater
thanorequaltothemaximumadvertisementinterval.Therefore,iftheholdtimeforanadvertisement
expires,thehostcanreasonablyconcludethattherouterinterfacethatsenttheadvertisementisnolonger
available.Thedefaultholdtimeisthreetimesthemaximumadvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumamountoftimethehostwillconsideran
advertisementtobevaliduntilaneweradvertisementarrivesandupdateittothedefaultvalue.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<TIME> Specifiesthelifetimeofrouteradvertisementssentfromthis
interface.Range:4to9000seconds.Default:1800seconds.
Example
SettingtheholdtimeforVLANinterface2to5000seconds:
| switch(config)#         |     | interface | vlan    | 2             |
| ----------------------- | --- | --------- | ------- | ------------- |
| switch(config-if-vlan)# |     |           | ip irdp | holdtime 5000 |
RemovingthetheholdtimeforVLANinterface2to5000seconds:
| switch(config)#         |     | interface | vlan       | 2             |
| ----------------------- | --- | --------- | ---------- | ------------- |
| switch(config-if-vlan)# |     |           | no ip irdp | holdtime 5000 |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp    | maxadvertinterval |     |        |     |
| ---------- | ----------------- | --- | ------ | --- |
| ip irdp    | maxadvertinterval |     | <TIME> |     |
| no ip irdp | maxadvertinterval |     | <TIME> |     |
Description
Specifiesthemaximumrouteradvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumrouteradvertisementintervalandrevertsto
thedefaultvalue.
15
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |
| --------------------------- | --- | ------------------- | --- | --- |

| Parameter |     |     |     | Description                                       |     |
| --------- | --- | --- | --- | ------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiesthemaximumtimeallowedbetweenthesendingof |     |
unsolicitedrouteradvertisements.Range:4to1800seconds.
Default:600seconds.
Example
SettingtheadvertisementintervalforVLANinterface2to30seconds:
| switch(config)#         |     | interface | vlan    | 2                 |     |
| ----------------------- | --- | --------- | ------- | ----------------- | --- |
| switch(config-if-vlan)# |     |           | ip irdp | maxadvertinterval | 30  |
RemovingtheadvertisementintervalforVLANinterface2to30seconds:
| switch(config)#         |     | interface | vlan       | 2                 |     |
| ----------------------- | --- | --------- | ---------- | ----------------- | --- |
| switch(config-if-vlan)# |     |           | no ip irdp | maxadvertinterval | 30  |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp    | minadvertinterval |     |        |     |     |
| ---------- | ----------------- | --- | ------ | --- | --- |
| ip irdp    | minadvertinterval |     | <TIME> |     |     |
| no ip irdp | minadvertinterval |     | <TIME> |     |     |
Description
Specifiestheminimumamountoftimetheswitchwaitsbetweensendingrouteradvertisements.By
default,thisvalueisautomaticallysetbytheswitchtobe75%ofthevalueconfiguredformaximumrouter
advertisementinterval.Usethiscommandtooverridetheautomaticallyconfiguredvalue.
Thenoformofthiscommandremovesthespecifiedminimumamountoftimetheswitchwaitsbetween
sendingrouteradvertisementsandrevertstothedefaultvalue.
| Parameter |     |     |     | Description                                       |     |
| --------- | --- | --- | --- | ------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiestheminimumtimeallowedbetweenthesendingof |     |
unsolicitedrouteradvertisements.Range:3to1800seconds.
Default:450seconds(75%ofthedefaultvalueformaximum
routeradvertisementinterval).
Example
IRDP|16

SettingtheminimumadvertisementintervalforVLANinterface2to25seconds:
| switch(config)#         |     | interface | vlan    | 2                 |     |     |
| ----------------------- | --- | --------- | ------- | ----------------- | --- | --- |
| switch(config-if-vlan)# |     |           | ip irdp | minadvertinterval |     | 25  |
RemovingtheminimumadvertisementintervalforVLANinterface2to25seconds:
| switch(config)#         |     | interface | vlan       | 2                 |     |     |
| ----------------------- | --- | --------- | ---------- | ----------------- | --- | --- |
| switch(config-if-vlan)# |     |           | no ip irdp | minadvertinterval |     | 25  |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp    | preference |         |     |     |     |     |
| ---------- | ---------- | ------- | --- | --- | --- | --- |
| ip irdp    | preference | <LEVEL> |     |     |     |     |
| no ip irdp | preference | <LEVEL> |     |     |     |     |
Description
SpecifiestheIRDPpreferencelevel.Ifahostreceivesmultiplerouteradvertisementmessagesfrom
differentrouters,thehostselectstherouterthatsentthemessagewiththehighestpreferenceasthe
defaultgateway.
ThenoformofthiscommandremovesthespecifiedIRDPpreferencelevelandrevertstothedefaultvalue.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<LEVEL>
SpecifiestheIRDPpreferencelevel.Range:-2147483648to
2147483647.Default:0.
Example
SettingtheIRDPpreferencelevelforVLANinterface2to25.
| switch(config)#         |     | interface | vlan    | 2          |     |     |
| ----------------------- | --- | --------- | ------- | ---------- | --- | --- |
| switch(config-if-vlan)# |     |           | ip irdp | preference | 25  |     |
RemovingtheIRDPpreferencelevelforVLANinterface2to25.
17
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- |

| switch(config)# | interface | vlan | 2   |     |     |
| --------------- | --------- | ---- | --- | --- | --- |
switch(config-if-vlan)#
|     |     | no ip irdp | preference | 25  |     |
| --- | --- | ---------- | ---------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip irdp |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |
show ip irdp
Description
DisplaysIRDPconfigurationsettings.
Example
| switch#     | sh ip irdp |          |     |     |     |
| ----------- | ---------- | -------- | --- | --- | --- |
| ICMP Router | Discovery  | Protocol |     |     |     |
Interface Status Advertising Minimum Maximum Holdtime Preference
|     |     | Address | Interval | Interval |     |
| --- | --- | ------- | -------- | -------- | --- |
--------------- -------- ----------- -------- -------- -------- -----------
| vlan1         | Disabled | multicast | 450 | 600 | 1800 0 |
| ------------- | -------- | --------- | --- | --- | ------ |
| bridge_normal | Disabled | multicast | 450 | 600 | 1800 0 |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
IRDP|18

Chapter 3
IPv6 Router Advertisement
| IPv6 Router Advertisement |     |     |     |     |
| ------------------------- | --- | --- | --- | --- |
IPV6RAprovidesamethodforlocalIPV6hoststoautomaticallyconfiguretheirownIPaddress(andother
settingssuchasapreferredDNSserver)basedoninformationadvertisedbyswitches/routersoperatingon
thenetwork.
IPv6flags
BehaviorofIPv6hoststoIPv6RAmessagesiscontrolledbythemanagedaddressconfigurationflag(M
flag),andotherstatefulconfigurationflag(Oflag).
| M flag | O flag | Description                                              |     |     |
| ------ | ------ | -------------------------------------------------------- | --- | --- |
| 0      | 0      | IndicatesthatnoinformationisavailableviaDHCPv6.          |     |     |
| 0      | 1      | Indicatesthatotherconfigurationinformationisavailablevia |     |     |
DHCPv6.ExamplesofsuchinformationareDNS-related
informationorinformationonotherserverswithinthenetwork.
| 1   | 0   | IndicatesthataddressesareavailableviaDynamicHost |     |     |
| --- | --- | ------------------------------------------------ | --- | --- |
ConfigurationProtocol(DHCPv6).
| 1   | 1   | IftheMflagisset,theOflagisredundantandcanbeignored |     |     |
| --- | --- | -------------------------------------------------- | --- | --- |
becauseDHCPv6willreturnallavailableconfiguration
information.
| Configuring | IPv6 RA |     |     |     |
| ----------- | ------- | --- | --- | --- |
Procedure
1. EnabletransmissionofIPv6routeradvertisementswiththecommandno ipv6 nd suppress-ra.
2. Optionally,configureIPv6unicastaddressprefixeswiththecommandipv6 prefix.
nd
3. Optionally,configuresupportforDNSnameresolutionwiththecommandsipv6 nd ra dns server
| andipv6 nd | ra dns search-list. |     |     |     |
| ---------- | ------------------- | --- | --- | --- |
4. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| IPv6 RAsetting                    |     | Default value | Commandtochange   | it  |
| --------------------------------- | --- | ------------- | ----------------- | --- |
| Numberofneighborsolicitationstobe |     | 1             | ipv6nddadattempts |     |
sentwhenperformingDAD.
| NumberofneighborentriesintheND |     | 131072 | ipv6 nd cache-limit |     |
| ------------------------------ | --- | ------ | ------------------- | --- |
cache.
| HoplimittobesentintheRAmessages. |     | 64  | ipv6 nd hop-limit |     |
| -------------------------------- | --- | --- | ----------------- | --- |
19
AOS-CX10.09IPServicesGuide| (6200 SwitchSeries)

| IPv6 RAsetting          |     |     | Default value | Commandtochange |     | it  |
| ----------------------- | --- | --- | ------------- | --------------- | --- | --- |
| MTUvaluetobesentintheRA |     |     | 1500bytes     | ipv6 nd         | mtu |     |
messages.
Neighborsolicitationinterval 1000milliseconds ipv6 nd ns-interval
| Lifetimeofadefaultrouter. |     |     | 1800seconds | ipv6 nd | ra lifetime |     |
| ------------------------- | --- | --- | ----------- | ------- | ----------- | --- |
RetrievalofanIPv6addressbydevices. Disabled ipv6 nd ra managed-config-flag
| Maximumintervalbetween |     |     | 600seconds | ipv6 nd | ra max-interval |     |
| ---------------------- | --- | --- | ---------- | ------- | --------------- | --- |
transmissionsofIPv6RAs.
| Minimumintervalbetween |     |     | 200seconds | ipv6 nd | ra min-interval |     |
| ---------------------- | --- | --- | ---------- | ------- | --------------- | --- |
transmissionsofIPv6RAs.
Timethataninterfaceconsidersa 0milliseconds(no ipv6 nd ra reachable-time
| devicetobereachable. |     |     | limit) |     |     |     |
| -------------------- | --- | --- | ------ | --- | --- | --- |
RetryperiodbetweenNDsolicitations. 0(Uselocally ipv6 nd ra retrans-timer
configuredNS-
interval)
Defaultroutingpreferenceforan Medium ipv6 nd router-preference
interface.
5. ReviewIPv6RAconfigurationsettingswiththecommandsshow ipv6 nd interface,show ipv6 nd
interface prefix,show ipv6 nd ra dns server,andshow ipv6 nd ra dns search-list.
Example
Thisexamplecreatesthefollowingconfiguration:
EnablesIPV6RAoninterface1/1/3.
n
n SetstherecursiveDNSserveraddressto4001::1withalifetimeof400seconds.
n Setstheminimumintervalbetweentransmissionsto3seconds.
n Setsthemaximumintervalbetweentransmissionsto13seconds.
n Setsthelifetimeofadefaultrouterto1900seconds.
| switch(config)#    | interface         | 1/1/3              |                  |     |     |     |
| ------------------ | ----------------- | ------------------ | ---------------- | --- | --- | --- |
| switch(config-if)# | no ipv6           | nd suppress-ra     |                  |     |     |     |
| switch(config-if)# | ipv6              | nd ra dns server   | 4001::1 lifetime | 400 |     |     |
| switch(config-if)# | ipv6              | nd ra min-interval | 3                |     |     |     |
| switch(config-if)# | ipv6              | nd ra max-interval | 13               |     |     |     |
| switch(config-if)# | ipv6              | nd ra lifetime     | 1900             |     |     |     |
| switch(config-if)# | end               |                    |                  |     |     |     |
| switch# show       | ipv6 nd interface | 1/1/3              |                  |     |     |     |
| Interface          | 1/1/3 is up       |                    |                  |     |     |     |
| Admin state        | is up             |                    |                  |     |     |     |
IPv6 address:
| 2006::1/64      | [VALID]              |                             |             |         |     |     |
| --------------- | -------------------- | --------------------------- | ----------- | ------- | --- | --- |
| IPv6 link-local | address:             | fe80::98f2:b321:368:6dc6/64 |             | [VALID] |     |     |
| ICMPv6 active   | timers:              |                             |             |         |     |     |
| Last            | Router-Advertisement | sent:                       | 0 Secs      |         |     |     |
| Next            | Router-Advertisement | sent                        | in: 13 Secs |         |     |     |
IPv6RouterAdvertisement|20

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
In this scenario, two host computers are auto-configured with IP addresses using IPv6 RA. In addition, the
switch provides the hosts with an address of a recursive DNS server. The physical topology of the network
looks like this:

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

IPv6 RA commands

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

21

| ipv6 address    | <global-unicast-address> |     |     |
| --------------- | ------------------------ | --- | --- |
| ipv6 address    | <global-unicast-address> |     |     |
| no ipv6 address | <global-unicast-address> |     |     |
Description
Setsaglobalunicastaddressontheinterface.
Thenoformofthiscommandremovestheglobalunicastaddressontheinterface.
ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-local
addressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6 address
link-localcommand.
Example
Enablingaglobalunicastaddress:
| switch(config)#    | interface | 1/1/1        |                    |
| ------------------ | --------- | ------------ | ------------------ |
| switch(config-if)# |           | ipv6 address | 3731:54:65fe:2::a7 |
Disablingaglobalunicastaddress:
| switch(config)#    | interface | 1/1/1           |                    |
| ------------------ | --------- | --------------- | ------------------ |
| switch(config-if)# |           | no ipv6 address | 3731:54:65fe:2::a7 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| ipv6 address    | autoconfig |     |     |
| --------------- | ---------- | --- | --- |
| ipv6 address    | autoconfig |     |     |
| no ipv6 address | autoconfig |     |     |
Description
EnablestheinterfacetoautomaticallyobtainanIPv6addressusingrouteradvertisementinformationand
theEUI-64identifier.
Thenoformofthiscommanddisablesaddressauto-configuration.
IPv6RouterAdvertisement|22

Amaximumof15autoconfiguredaddressesaresupported.
n
n ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotadd
theipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,the
link-localaddressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6
| address | link-localcommand. |     |     |     |
| ------- | ------------------ | --- | --- | --- |
Usage
TheIPv6SLAACfeatureletstherouterobtaintheIPv6addressfortheinterfaceitisconfiguredthroughthe
SLAACmethod.ThisfeatureisnotavailableonthemgmtVRF.
Example
Enablingunicastautoconfiguring:
| switch(config)#    |     | interface | 1/1/1   |            |
| ------------------ | --- | --------- | ------- | ---------- |
| switch(config-if)# |     | ipv6      | address | autoconfig |
Disablingunicastautoconfiguring:
| switch(config)#    |     | interface | 1/1/1   |            |
| ------------------ | --- | --------- | ------- | ---------- |
| switch(config-if)# |     | no ipv6   | address | autoconfig |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| ipv6 address |            | link-local           |     |     |
| ------------ | ---------- | -------------------- | --- | --- |
| ipv6 address | link-local | [<IPV6-ADDR>/<MASK>] |     |     |
Description
EnablesIPv6onthecurrentinterface.Ifnoaddressisspecified,anIPv6link-localaddressisauto-generated
fortheinterface.Ifanaddressisspecified,auto-configurationisdisabledandthespecifiedaddress/maskis
assignedtotheinterface.
TodisableIPv6link-localontheinterface,removeipv6 address link-local,ipv6 address <global-
| ipv6-address>,andipv6 |     | address | autoconfigfromtheinterface. |     |
| --------------------- | --- | ------- | --------------------------- | --- |
ThisfeatureisnotavailableonthemanagementVRF.
23
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |
| --------------------------- | --- | ------------------- | --- | --- |

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
<MASK>
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom0to128.
Example
EnablingIPv6link-localontheinterface:
| switch(config)#    |     | interface | 1/1/1   |            |
| ------------------ | --- | --------- | ------- | ---------- |
| switch(config-if)# |     | ipv6      | address | link-local |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| ipv6 nd | cache-limit    |                |     |     |
| ------- | -------------- | -------------- | --- | --- |
| ipv6 nd | cache-limit    | <CACHELIMIT>   |     |     |
| no ipv6 | nd cache-limit | [<CACHELIMIT>] |     |     |
Description
ConfiguresthelimitonthenumberofneighborentriesintheNDcache.
Thenoformofthiscommandsetsthecachelimittothedefaultvalue.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<CACHELIMIT> Specifiestheneighborcacheentrieslimit.Range:1-131072.
Default:131072.
Examples
Settingthecachelimitto20.
IPv6RouterAdvertisement|24

| switch(config)# |     | ipv6 nd | cache-limit |     | 20  |
| --------------- | --- | ------- | ----------- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | dad             | attempts         |     |     |     |
| ------- | --------------- | ---------------- | --- | --- | --- |
| ipv6 nd | dad attempts    | <NUM-ATTEMPTS>   |     |     |     |
| no ipv6 | nd dad attempts | [<NUM-ATTEMPTS>] |     |     |     |
Description
Configuresthenumberofneighborsolicitationstobesentwhenperformingduplicateaddressdetection
(DAD)foraunicastaddressconfiguredonaninterface.IftheactivegatewayisconfiguredwiththesameIP
asanSVIIP,thenIPv6DADcannotbeconfigured.
Thenoformofthiscommandsetsthenumberofattemptstothedefaultvalue.
| Parameter    |                |     |     |     | Description |
| ------------ | -------------- | --- | --- | --- | ----------- |
| dad attempts | <NUM-ATTEMPTS> |     |     |     |             |
Specifiesthenumberofneighborsolicitationstosend.Range:0-
15.Default:1.
Examples
| switch(config)#    |     | interface | 1/1/1  |          |     |
| ------------------ | --- | --------- | ------ | -------- | --- |
| switch(config-if)# |     | ipv6      | nd dad | attempts | 5   |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
25
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

| ipv6 nd | hop-limit    |              |     |     |     |
| ------- | ------------ | ------------ | --- | --- | --- |
| ipv6 nd | hop-limit    | <HOPLIMIT>   |     |     |     |
| no ipv6 | nd hop-limit | [<HOPLIMIT>] |     |     |     |
Description
ConfiguresthehoplimittobesentinRAs.
Thenoformofthiscommandresetsthehoplimitto0.ThisreseteliminatesthehoplimitfromtheRAsthat
originateontheinterface,sothehostdeterminesthehoplimit.
| Parameter |            |     |     |     | Description |
| --------- | ---------- | --- | --- | --- | ----------- |
| hop-limit | <HOPLIMIT> |     |     |     |             |
Specifiesthehoplimit.Range:0-255.Default:64.
Examples
| switch(config)#    |     | interface | 1/1/1        |     |     |
| ------------------ | --- | --------- | ------------ | --- | --- |
| switch(config-if)# |     | ipv6      | nd hop-limit |     | 64  |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | mtu                  |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- |
| ipv6 nd | mtu <MTU-VALUE>      |     |     |     |     |
| no ipv6 | nd mtu [<MTU-VALUE>] |     |     |     |     |
Description
ConfigurestheMTUsizetobesentintheRAmessages.
Thenoformofthiscommandsetshoplimittothedefaultvalue.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<MTU-VALUE> SpecifiestheMTUsize.Range:1280-65535bytes.Default:1500
bytes.
Examples
| switch(config)#    |     | interface | 1/1/1  |      |     |
| ------------------ | --- | --------- | ------ | ---- | --- |
| switch(config-if)# |     | ipv6      | nd mtu | 1300 |     |
IPv6RouterAdvertisement|26

CommandHistory
|     | Release        |     |     |     | Modification |     |
| --- | -------------- | --- | --- | --- | ------------ | --- |
|     | 10.07orearlier |     |     |     | --           |     |
CommandInformation
|     | Platforms |     | Commandcontext |     | Authority |     |
| --- | --------- | --- | -------------- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 | nd   | ns-interval    |          |     |     |     |
| ---- | ---- | -------------- | -------- | --- | --- | --- |
| ipv6 | nd   | ns-interval    | <TIME>   |     |     |     |
| no   | ipv6 | nd ns-interval | [<TIME>] |     |     |     |
Description
ConfigurestheNDtimeinmillisecondsbetweenDADneighborsolicitationssentforanunresolved
destination.Increasethens-intervaltimeifthenetworkissloworiftherearepersistentretryfailures.Ifthe
activegatewayisconfiguredwiththesameIPasanSVIIP,thenIPv6DADcannotbeconfigured
Thenoformofthiscommandsetsthens-intervaltothedefaultvalue.
|     | Parameter |     |     |     | Description |     |
| --- | --------- | --- | --- | --- | ----------- | --- |
<TIME> Specifiestheneighborsolicitationinterval.Range:1000-3600000
milliseconds.Default:1000milliseconds.
Examples
|     | switch(config)#    |     | interface | 1/1/1          |     |      |
| --- | ------------------ | --- | --------- | -------------- | --- | ---- |
|     | switch(config-if)# |     | ipv6      | nd ns-interval |     | 1200 |
CommandHistory
|     | Release        |     |     |     | Modification |     |
| --- | -------------- | --- | --- | --- | ------------ | --- |
|     | 10.07orearlier |     |     |     | --           |     |
CommandInformation
|     | Platforms |     | Commandcontext |     | Authority |     |
| --- | --------- | --- | -------------- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 | nd                | prefix                          |                 |                  |              |           |
| ---- | ----------------- | ------------------------------- | --------------- | ---------------- | ------------ | --------- |
| ipv6 | nd                | prefix <IPV6-ADDR>/<PREFIX-LEN> |                 |                  |              |           |
|      | [no-advertise     |                                 | | [valid        | <LIFETIME-VALUE> |              | preferred |
|      | <LIFETIME-VALUE>] |                                 | | no-autoconfig |                  | | no-onlink] |           |
27
| AOS-CX10.09IPServicesGuide| |     |     | (6200 SwitchSeries) |     |     |     |
| --------------------------- | --- | --- | ------------------- | --- | --- | --- |

| no ipv6   | nd prefix <IPV6-ADDR>/<PREFIX-LEN> |           | [no-advertise    |                  |     |     |
| --------- | ---------------------------------- | --------- | ---------------- | ---------------- | --- | --- |
| | [valid  | <LIFETIME-VALUE>                   | preferred | <LIFETIME-VALUE> |                  |     |     |
| ] |       | no-autoconfig | no-onlink]         |           |                  |                  |     |     |
| ipv6 nd   | prefix default [no-advertise       |           | | [valid         | <LIFETIME-VALUE> |     |     |
| preferred | <LIFETIME-VALUE>]                  | |         | no-autoconfig    | | no-onlink]}    |     |     |
no ipv6 nd prefix default [no-advertise | [valid <LIFETIME-VALUE>
| preferred | <LIFETIME-VALUE>] | |   | no-autoconfig | | no-onlink]} |     |     |
| --------- | ----------------- | --- | ------------- | ------------- | --- | --- |
Description
SpecifiesprefixesfortheroutingswitchtoincludeinRAstransmittedontheinterface.IPv6hostsusethe
prefixesinRAstoautoconfigurethemselveswithglobalunicastaddresses.Theautoconfiguredaddressofa
hostiscomposedoftheadvertisedprefixandtheinterfaceidentifierinthecurrentlink-localaddressofthe
host.
Bydefault,advertise,autoconfig,andonlinkareset.
Thenoformofthiscommandremovestheconfigurationontheinterface.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<IPV6-ADDR>/<PREFIX-LEN> SpecifiestheIPv6prefixtoadvertiseinRA.Format:X:X::X:X/M
default Specifiesapplyconfigurationtoallon-linkprefixesthatarenot
|     |     |     | individuallysetbytheipv6 |     | ra prefix | <IPV6-ADDR>/<PREFIX- |
| --- | --- | --- | ------------------------ | --- | --------- | -------------------- |
LEN>command.Itappliesthesamevalidandpreferredlifetimes,
linkstate,autoconfigurationstate,andadvertiseoptionstothe
advertisementssentforallon-linkprefixesthatarenot
individuallyconfiguredwithauniquelifetime.Thisalsoappliesto
theprefixesforanyglobalunicastaddressesconfiguredlateron
thesameinterface.
Usingdefaultonce,andthenusingitagainwithanynew
parametervaluesresultsinthenewvaluesreplacingtheformer
valuesinadvertisements.Ifdefaultisusedwithouttheno–
advertise,no–autoconfig,orno-onlinkparameter,the
advertisementsettingfortheabsentparameterisreturnedtoits
defaultsetting.
no-advertise
SpecifiesdonotadvertiseprefixinRA.
valid <LIFETIME-VALUE> Specifiesthetotaltime,inseconds,theprefixremainsavailable
beforebecomingunusable.Afterpreferred-lifetimeexpiration,
anyautoconfiguredaddressisdeprecatedandusedonlyfor
transactionsonlybeforepreferred-lifetimeexpires.Ifthevalid
lifetimeexpires,theaddressbecomesinvalid.
|     |     |     | Youcanenteravalueinsecondsorentervalid |     |     | infinitewhich |
| --- | --- | --- | -------------------------------------- | --- | --- | ------------- |
setsinfinitelifetime.Default:2,592,000secondswhichis30days.
Range:0–4294967294seconds.
preferred <LIFETIME-VALUE> Specifiesthespanoftimeduringwhichtheaddresscanbefreely
usedasasourceanddestinationfortraffic.Thissettingmustbe
lessthanorequaltothecorrespondingvalid–lifetimesetting.
Youcanenteravalueinsecondsorenterpreferred infinite
whichsetsinfinitelifetime.Default:604,800secondswhichis
sevendays.Range:0–4294967294seconds.
| no-autoconfig |     |     | Specifiesdonotuseprefixforautoconfiguration.   |     |     |     |
| ------------- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| no-onlink     |     |     | Specifiesdonotuseprefixforonlinkdetermination. |     |     |     |
IPv6RouterAdvertisement|28

Examples
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# ipv6 nd prefix 4001::1/64 valid 30 preferred 10 no-autoconfig no-
onlink
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra dns             | search-list |               |           |         |
| ------- | ------------------ | ----------- | ------------- | --------- | ------- |
| ipv6 nd | ra dns search-list |             | <DOMAIN-NAME> | [lifetime | <TIME>] |
| no ipv6 | nd ra dns          | search-list | <DOMAIN-NAME> |           |         |
Description
ConfigurestheDNSSearchList(DNSSL)toincludeinRouterAdvertisements(RAs)transmittedonthe
interface.
ThenoformofthiscommandremovestheDNSSearchListfromtheRAstransmittedontheinterface.
| Parameter     |     |     |     | Description                           |     |
| ------------- | --- | --- | --- | ------------------------------------- | --- |
| <DOMAIN-NAME> |     |     |     | SpecifiesthedomainnamesforDNSqueries. |     |
lifetime <TIME> Specifieslifetimeinseconds.Range:4-4294967295seconds.
Default:1800seconds.
Usage
n DNSSLcontainsthedomainnamesofDNSsuffixesorIPv6hoststoappendtoshort,unqualifieddomain
namesforDNSqueries.
n MultipleDNSdomainnamescanbeaddedtotheDNSSLbyusingthecommandrepeatedly.
n Amaximumofeightserveraddressesareallowed.
Examples
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# ipv6 nd ra dns search-list test.com lifetime 500
CommandHistory
29
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra dns           | server      |           |         |     |
| ------- | ---------------- | ----------- | --------- | ------- | --- |
| ipv6 nd | ra dns server    | <IPV6-ADDR> | [lifetime | <TIME>] |     |
| no ipv6 | nd ra dns server | <IPV6-ADDR> |           |         |     |
Description
ConfigurestheIPv6addressofapreferredRecursiveDNSServer(RDNSS)tobeincludedinRouter
Advertisements(RAs)transmittedontheinterface.
ThenoformofthiscommandremovestheconfiguredDNSserverfromtheRAstransmittedonthe
interface.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IPV6-ADDR>
SpecifiestheRDNSSaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| lifetime | <TIME> |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
SpecifiesIPv6DNSserverlifetimeinseconds.Range:4-
4294967295seconds.Default:1800seconds.
Usage
IncludingRDNSSinformationinRAsprovidesDNSserverconfigurationforconnectedIPv6hostswithout
n
requiringDHCPv6.
Multipleserverscanbeconfiguredontheinterfacebyusingthecommandrepeatedly.
n
Amaximumofeightserveraddressesareallowed.
n
Examples
switch(config)#
|                    |     | interface 1/1/1 |               |                  |     |
| ------------------ | --- | --------------- | ------------- | ---------------- | --- |
| switch(config-if)# |     | ipv6 nd         | ra dns server | 2001::1 lifetime | 400 |
CommandHistory
IPv6RouterAdvertisement|30

| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra lifetime    |          |     |     |
| ------- | -------------- | -------- | --- | --- |
| ipv6 nd | ra lifetime    | <TIME>   |     |     |
| no ipv6 | nd ra lifetime | [<TIME>] |     |     |
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
n Agivenhostonaninterfacerefreshesthedefaultrouterlifetimeforaspecificroutereachtimethehost
receivesanRAfromthatrouter.
n Aspecificrouterceasestobeadefaultroutercandidateforagivenhostifthedefaultrouterlifetime
expiresbeforethehostisupdatedwithanewRAfromtherouter.
Examples
| switch(config)#    |     | interface | 1/1/1          |      |
| ------------------ | --- | --------- | -------------- | ---- |
| switch(config-if)# |     | ipv6      | nd ra lifetime | 1200 |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
31
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |
| --------------------------- | --- | ------------------- | --- | --- |

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd ra                     | managed-config-flag |     |     |     |
| ------------------------------ | ------------------- | --- | --- | --- |
| ipv6 nd ra managed-config-flag |                     |     |     |     |
| no ipv6 nd ra                  | managed-config-flag |     |     |     |
Description
ControlstheMflagsettinginRAstheroutertransmitsonthecurrentinterface.EnabletheMflagtoindicate
thathostscanobtainIPaddressthroughDHCPv6.TheMflagisdisabledbydefault.
Thenoformofthiscommandturnsoff(disables)theMflag.
Usage
n EnablingtheMflagdirectshoststoacquiretheirIPv6addressingforthecurrentinterfacefroma
DHCPv6server.
n WhentheM-bitisenabled,receivinghostsignoretheOflagsetting,whichisconfiguredusingthe
| commandipv6 | nd  | ra other-config-flag. |     |     |
| ----------- | --- | --------------------- | --- | --- |
n WhentheM-bitisdisabled(thedefault),receivinghostsexpecttoreceivetheirIPv6addressesfromRA.
| M flag |     |     | O flag | Description                              |
| ------ | --- | --- | ------ | ---------------------------------------- |
| 0      |     |     | 0      | Indicatesthatnoinformationisavailablevia |
DHCPv6.
| 0   |     |     | 1   | Indicatesthatotherconfiguration |
| --- | --- | --- | --- | ------------------------------- |
informationisavailableviaDHCPv6.
ExamplesofsuchinformationareDNS-
relatedinformationorinformationonother
serverswithinthenetwork.
| 1   |     |     | 0   | Indicatesthataddressesareavailablevia |
| --- | --- | --- | --- | ------------------------------------- |
DynamicHostConfigurationProtocol
(DHCPv6).
| 1   |     |     | 1   | IftheMflagisset,theOflagisredundant |
| --- | --- | --- | --- | ----------------------------------- |
andcanbeignoredbecauseDHCPv6will
returnallavailableconfiguration
information.
Examples
| switch(config)#    |     | interface 1/1/1 |                        |     |
| ------------------ | --- | --------------- | ---------------------- | --- |
| switch(config-if)# |     | ipv6 nd         | ra managed-config-flag |     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
IPv6RouterAdvertisement|32

CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra max-interval    |     |          |     |     |
| ------- | ------------------ | --- | -------- | --- | --- |
| ipv6 nd | ra max-interval    |     | <TIME>   |     |     |
| no ipv6 | nd ra max-interval |     | [<TIME>] |     |     |
Description
ConfiguresthemaximumintervalbetweentransmissionsofIPv6RAsontheinterface.Theintervalbetween
RAtransmissionsonaninterfaceisarandomvaluethatchangeseverytimeanRAissent.Theintervalis
calculatedtobeavaluebetweenthecurrentmax-intervalandmin-intervalsettings.
Thenoformofthiscommandreturnsthesettingtoitsdefault,providedthedefaultvalueislessthanthe
defaultlifetimevalue.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<TIME> Specifiesthemaximumadvertisementtimeinseconds.Range:4-
1800.Default:600seconds.
Usage
Thisvaluehasonesettingperinterface.ThesettingdoesnotapplytoRAssentinresponsetoarouter
n
solicitationreceivedfromanotherdevice.
n Attemptingtosetmax-intervaltoavaluethatisnotsufficientlylargerthanthecurrentmin-intervalalso
resultsinanerrormessage.
Examples
| switch(config)#    |     | interface | 1/1/1 |                 |     |
| ------------------ | --- | --------- | ----- | --------------- | --- |
| switch(config-if)# |     | ipv6      | nd    | ra max-interval | 30  |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra min-interval |     |        |     |     |
| ------- | --------------- | --- | ------ | --- | --- |
| ipv6 nd | ra min-interval |     | <TIME> |     |     |
33
| AOS-CX10.09IPServicesGuide| |     | (6200 | SwitchSeries) |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- |

| no ipv6 | nd ra min-interval |     | [<TIME>] |     |     |
| ------- | ------------------ | --- | -------- | --- | --- |
Description
ConfigurestheminimumintervalbetweentransmissionsofIPv6RAsontheinterface.Theintervalbetween
RAtransmissionsonaninterfaceisarandomvaluethatchangeseverytimeanRAissent.Theintervalis
calculatedtobeavaluebetweenthecurrentmax-intervalandmin-intervalsettings.
Thenoformofthiscommandreturnsthesettingtoitsdefault,providedthedefaultvalueislessthanthe
currentmax-intervalsetting.
| Parameter |     |     |     | Description                                          |     |
| --------- | --- | --- | --- | ---------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiesaminimumadvertisementtimeinseconds.Range:3- |     |
1350.Default:200seconds.
Usage
ThisvaluehasonesettingperinterfaceanddoesnotapplytoRAssentinresponsetoarouter
n
solicitationreceivedfromanotherdevice.
Themin-intervalmustbelessthanthemax-interval.Attemptingtosetmin-intervaltoahighervalue
n
resultsinanerrormessage.
Examples
| switch(config)#    |     | interface | 1/1/1 |              |     |
| ------------------ | --- | --------- | ----- | ------------ | --- |
| switch(config-if)# |     | ipv6      | nd ra | min-interval | 25  |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra other-config-flag    |     |     |     |     |
| ------- | ----------------------- | --- | --- | --- | --- |
| ipv6 nd | ra other-config-flag    |     |     |     |     |
| no ipv6 | nd ra other-config-flag |     |     |     |     |
Description
ControlstheO-bitinRAstheroutertransmitsonthecurrentinterface;butisignoredunlesstheM-bitis
disabledinRAs.ConfiguretosettheO-bitinRAmessagesforhosttoobtainnetworkparametersthrough
DHCPv6.Theother-config-flagisdisabledbydefault.
FormoreinformationonconfiguringtheM-bit,see ipv6 nd ra managed-config-flag.
Thenoformofthiscommandturnsoff(disables)thesettingforthiscommandinRAs.
IPv6RouterAdvertisement|34

Usage
EnablingtheO-bitwhiletheM-bitisdisableddirectshostsontheinterfacetoacquiretheirother
configurationinformationfromDHCPv6.ExamplesofsuchinformationareDNS-relatedinformationor
informationonotherserverswithinthenetwork.
Examples
| switch(config)#    |     | interface | 1/1/1   |                      |     |
| ------------------ | --- | --------- | ------- | -------------------- | --- |
| switch(config-if)# |     |           | ipv6 nd | ra other-config-flag |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra reachable-time    |     |          |     |     |
| ------- | -------------------- | --- | -------- | --- | --- |
| ipv6 nd | ra reachable-time    |     | <TIME>   |     |     |
| no ipv6 | nd ra reachable-time |     | [<TIME>] |     |     |
Description
Setstheamountoftimethattheinterfaceconsidersadevicetobereachableafterreceivingareachability
confirmationfromthedevice.
Thenoformofthiscommandsetsthereachabletimetothedefaultvalueof0.(nolimit).
| Parameter |     |     |     | Description                                         |     |
| --------- | --- | --- | --- | --------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiesthereachabletimeinmilliseconds.Range:1000- |     |
3600000.Default:0(nolimit).
Examples
| switch(config)#    |     | interface | 1/1/1   |                   |      |
| ------------------ | --- | --------- | ------- | ----------------- | ---- |
| switch(config-if)# |     |           | ipv6 nd | ra reachable-time | 2000 |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
35
| AOS-CX10.09IPServicesGuide| |     | (6200 | SwitchSeries) |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- |

| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra retrans-timer    |     |          |     |     |     |
| ------- | ------------------- | --- | -------- | --- | --- | --- |
| ipv6 nd | ra retrans-timer    |     | <TIME>   |     |     |     |
| no ipv6 | nd ra retrans-timer |     | [<TIME>] |     |     |     |
Description
Configurestheperiod(retransmittimer)betweenNDsolicitationssentbyahostforanunresolved
destination,orbetweenDADneighborsolicitationrequests.Bydefault,hostsontheinterfaceusetheirown
locallyconfiguredNS-intervalsettingsinsteadofusingthevaluereceivedintheRAs.
Increasethistimerwhenneighborsolicitationretriesorfailuresareoccur,orina"slow"(WAN)network.
Thenoformofthiscommandsetsthevaluetothedefaultof0.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<TIME> Specifiestheretransmittimervalueinmilliseconds.Range:0-
4294967295milliseconds.Default:0(UselocallyconfiguredNS-
interval).
Examples
| switch(config)#    |     | interface | 1/1/1   |                  |     |     |
| ------------------ | --- | --------- | ------- | ---------------- | --- | --- |
| switch(config-if)# |     |           | ipv6 nd | ra retrans-timer |     | 400 |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | router-preference    |     |       |          |        |        |
| ------- | -------------------- | --- | ----- | -------- | ------ | ------ |
| ipv6 nd | router-preference    |     | {high | | medium | | low} |        |
| no ipv6 | nd router-preference |     | [high | | medium |        | | low] |
Description
SpecifiesthevaluethatissetintheDefaultRouterPreference(DRP)fieldofRouterAdvertisements(RAs)
thattheswitchsendsfromaninterface.AninterfacewithaDRPvalueofhighwillbepreferredbyother
devicesonthenetworkoverinterfaceswithanRAvalueofmediumorlow.
Thenoformofthiscommandsetthevaluetothedefaultofmedium.
IPv6RouterAdvertisement|36

| Parameter |     |     |     | Description              |     |
| --------- | --- | --- | --- | ------------------------ | --- |
| high      |     |     |     | SetsDRPtohigh.           |     |
| medium    |     |     |     | SetsDRPtomedium.Default. |     |
| low       |     |     |     | SetsDRPtolow.            |     |
Examples
| switch(config)#    |     | interface | 1/1/1                |     |      |
| ------------------ | --- | --------- | -------------------- | --- | ---- |
| switch(config-if)# |     | ipv6      | nd router-preference |     | high |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | suppress-ra      |                     |     |     |     |
| ------- | ---------------- | ------------------- | --- | --- | --- |
| ipv6 nd | suppress-ra      | [<SUPPRESS-OPTION>] |     |     |     |
| no ipv6 | nd ra supress-ra | [<SUPPRESS-OPTION>] |     |     |     |
Description
ConfiguressuppressionofIPv6RouterAdvertisementtransmissionsonaninterface.
ThenoformofthiscommandrestorestransmissionofIPv6RouterAdvertisementandoptions.
| Parameter   |                     |     |     | Description |     |
| ----------- | ------------------- | --- | --- | ----------- | --- |
| suppress-ra | [<SUPPRESS-OPTION>] |     |     |             |     |
SpecifiessuppressingRAtransmissions.Enteringsuppress-ra
withoutanyoptions,suppressesallRAmessages(default).Oryou
canenteroneofthefollowingoptions.
dnssl
SpecifiessuppressingDNSSLoptionsinRAmessages.
| mtu |     |     |     | SpecifiessuppressingMTUoptionsinRAmessages. |     |
| --- | --- | --- | --- | ------------------------------------------- | --- |
rdnss
SpecifiessuppressingRDNSSoptionsinRAmessages.
Examples
37
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

|     | switch(config)# |     | interface | 1/1/1 |     |     |     |
| --- | --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|     |                    |     | ipv6 | nd   | suppress-ra    | mtu dnssl | rdnss       |
| --- | ------------------ | --- | ---- | ---- | -------------- | --------- | ----------- |
|     | switch(config-if)# |     | no   | ipv6 | nd suppress-ra | mtu       | dnssl rdnss |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ipv6    | nd     | global  | traffic |     |     |     |
| ---- | ------- | ------ | ------- | ------- | --- | --- | --- |
| show | ipv6 nd | global | traffic |         |     |     |     |
Description
DisplaysIPV6NeighborDiscoverytrafficdetailsonadevice.
Examples
|     | switch#     | show           | ipv6 nd        | global          | traffic         |      |     |
| --- | ----------- | -------------- | -------------- | --------------- | --------------- | ---- | --- |
|     | ICMPv6      | packet         | Statistics     |                 | (sent/received) |      |     |
|     | Total       | Messages       |                |                 | :               | 18/0 |     |
|     | Error       | Messages       |                |                 | :               | 0/0  |     |
|     | Destination |                | Unreachables   |                 | :               | 0/0  |     |
|     | Time        | Exceeded       |                |                 | :               | 0/0  |     |
|     | Parameter   |                | Problems       |                 | :               | 0/0  |     |
|     | Echo        | Request        |                |                 | :               | 0/0  |     |
|     | Echo        | Replies        |                |                 | :               | 0/0  |     |
|     | Redirects   |                |                |                 | :               | 0/0  |     |
|     | Packet      | Too            | Big            |                 | :               | 0/0  |     |
|     | Router      | Advertisements |                |                 | :               | 4/0  |     |
|     | Router      | Solicitations  |                |                 | :               | 0/0  |     |
|     | Neighbor    |                | Advertisements |                 | :               | 0/0  |     |
|     | Neighbor    |                | Solicitations  |                 | :               | 3/0  |     |
|     | Duplicate   |                | router         | RA received     | :               | 0/0  |     |
|     | ICMPv6      | MLD            | Statistics     | (sent/received) |                 |      |     |
|     | V1          | Queries        | :              | 0/0             |                 |      |     |
|     | V2          | Queries        | :              | 0/0             |                 |      |     |
|     | V1          | Reports        | :              | 0/0             |                 |      |     |
|     | V2          | Reports        | :              | 11/0            |                 |      |     |
|     | V1          | Leaves         | :              | 0/0             |                 |      |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
IPv6RouterAdvertisement|38

CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | ipv6    | nd        | interface |            |     |            |                   |     |
| ---- | ------- | --------- | --------- | ---------- | --- | ---------- | ----------------- | --- |
| show | ipv6 nd | interface |           | [<IF-NAME> |     | | all-vrfs | | vrf <VRF-NAME>] |     |
Description
Displaysneighbordiscoveryinformationforaninterface.Ifnooptionsarespecified,displaysinformation
forthedefaultVRF.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<IF-NAME>
DisplaysinformationaboutthespecifiedIPv6enabledinterface.
| all-vrfs |     |     |     |     |     | DisplaysinformationaboutinterfacesinallVRFs. |     |     |
| -------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- |
vrf <VRF-NAME>
DisplaysinformationaboutinterfacesinaparticularVRF.Or,if
<VRF-NAME>isnotspecified,informationforthedefaultVRFis
displayed.
Examples
ShowinginformationforallVRFs:
|     | switch#              | show ipv6            | nd           | interface   |                              | all-vrfs |             |         |
| --- | -------------------- | -------------------- | ------------ | ----------- | ---------------------------- | -------- | ----------- | ------- |
|     | List of              | IPv6 Interfaces      |              | for         | VRF                          | default  |             |         |
|     | Interface            | 1/1/1                | is           | up          |                              |          |             |         |
|     | Admin                | state                | is up        |             |                              |          |             |         |
|     | IPv6 address:        |                      |              |             |                              |          |             |         |
|     | IPv6 link-local      |                      | address:     |             | fe80::7272:cfff:fee7:a8b9/64 |          |             | [VALID] |
|     | ICMPv6               | active               | timers:      |             |                              |          |             |         |
|     | Last                 | Router-Advertisement |              |             |                              | sent:    |             |         |
|     | Next                 | Router-Advertisement |              |             |                              | sent in: |             |         |
|     | Router-Advertisement |                      |              | parameters: |                              |          |             |         |
|     | Periodic             |                      | interval:    | 200         | to                           | 600 secs |             |         |
|     | Router               | Preference:          |              | medium      |                              |          |             |         |
|     | Send                 | "Managed             |              | Address     | Configuration"               |          | flag: false |         |
|     | Send                 | "Other               | Stateful     |             | Configuration"               |          | flag: false |         |
|     | Send                 | "Current             |              | Hop Limit"  |                              | field:   | 64          |         |
|     | Send                 | "MTU"                | option       | value:      |                              | 1500     |             |         |
|     | Send                 | "Router              |              | Lifetime"   | field:                       | 1800     |             |         |
|     | Send                 | "Reachable           |              | Time"       | field:                       | 0        |             |         |
|     | Send                 | "Retrans             |              | Timer"      | field:                       | 0        |             |         |
|     | Suppress             |                      | RA:          | true        |                              |          |             |         |
|     | Suppress             |                      | MTU          | in RA:      | true                         |          |             |         |
|     | ICMPv6               | error                | message      | parameters: |                              |          |             |         |
|     | Send                 | redirects:           |              | false       |                              |          |             |         |
|     | ICMPv6               | DAD parameters:      |              |             |                              |          |             |         |
|     | Current              |                      | DAD attempt: |             | 1                            |          |             |         |
39
| AOS-CX10.09IPServicesGuide| |     |     | (6200 | SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ----- | ------------- | --- | --- | --- | --- |

| List      | of IPv6 | Interfaces |       | for | VRF | red |     |     |
| --------- | ------- | ---------- | ----- | --- | --- | --- | --- | --- |
| Interface |         | 1/1/2      | is up |     |     |     |     |     |
| Admin     | state   | is         | up    |     |     |     |     |     |
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
| switch#   | show    | ipv6       | nd    | interface |     |         |     |     |
| --------- | ------- | ---------- | ----- | --------- | --- | ------- | --- | --- |
| List      | of IPv6 | Interfaces |       | for       | VRF | default |     |     |
| Interface |         | 1/1/1      | is up |           |     |         |     |     |
IPv6RouterAdvertisement|40

|     | Admin                | state                | is up        |             |                              |           |             |         |
| --- | -------------------- | -------------------- | ------------ | ----------- | ---------------------------- | --------- | ----------- | ------- |
|     | IPv6                 | address:             |              |             |                              |           |             |         |
|     | 2001::1/64           |                      | [VALID]      |             |                              |           |             |         |
|     | IPv6                 | link-local           | address:     |             | fe80::7272:cfff:fee7:a8b9/64 |           |             | [VALID] |
|     | ICMPv6               | active               | timers:      |             |                              |           |             |         |
|     | Last                 | Router-Advertisement |              |             |                              | sent: 6   | Secs        |         |
|     | Next                 | Router-Advertisement |              |             |                              | sent in:  | 7 Secs      |         |
|     | Router-Advertisement |                      |              | parameters: |                              |           |             |         |
|     | Periodic             |                      | interval:    |             | 3 to 13                      | secs      |             |         |
|     | Router               | Preference:          |              |             | medium                       |           |             |         |
|     | Send                 | "Managed             |              | Address     | Configuration"               |           | flag: false |         |
|     | Send                 | "Other               | Stateful     |             | Configuration"               |           | flag: false |         |
|     | Send                 | "Current             |              | Hop Limit"  |                              | field: 64 |             |         |
|     | Send                 | "MTU"                | option       | value:      |                              | 1500      |             |         |
|     | Send                 | "Router              |              | Lifetime"   | field:                       | 1900      |             |         |
|     | Send                 | "Reachable           |              | Time"       | field:                       | 0         |             |         |
|     | Send                 | "Retrans             |              | Timer"      | field:                       | 0         |             |         |
|     | Suppress             |                      | RA:          | true        |                              |           |             |         |
|     | Suppress             |                      | MTU          | in RA:      | true                         |           |             |         |
|     | ICMPv6               | error                | message      | parameters: |                              |           |             |         |
|     | Send                 | redirects:           |              | false       |                              |           |             |         |
|     | ICMPv6               | DAD parameters:      |              |             |                              |           |             |         |
|     | Current              |                      | DAD attempt: |             | 1                            |           |             |         |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | ipv6    | nd        | interface |        | prefix    |     |                 |     |
| ---- | ------- | --------- | --------- | ------ | --------- | --- | --------------- | --- |
| show | ipv6 nd | interface |           | prefix | [all-vrfs | |   | vrf <VRF-NAME>] |     |
Description
ShowsIPv6prefixinformationforallVRFsoraspecificVRF.Ifnooptionsarespecified,showsinformation
forthedefaultVRF.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
all-vrfs
ShowsprefixinformationforallVRFs.
| vrf | <VRF-NAME> |     |     |     |     | NameofaVRF. |     |     |
| --- | ---------- | --- | --- | --- | --- | ----------- | --- | --- |
Examples
ShowingprefixinformationforthedefaultVRF:
41
| AOS-CX10.09IPServicesGuide| |     |     | (6200 | SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ----- | ------------- | --- | --- | --- | --- |

switch# show ipv6 nd interface prefix

List of IPv6 Interfaces for VRF default
List of IPv6 Prefix advertised on 1/1/1

Prefix : 4545::/65
Enabled : Yes
Validlife time : 2592000
Preferred lifetime : 604800
On-link : Yes
Autonomous : Yes

Showing information for VRF red:

switch# show ipv6 nd interface prefix vrf red

List of IPv6 Interfaces for VRF red
List of IPv6 Prefix advertised on 1/1/2

Prefix : 2001::/64
Enabled : Yes
Validlife time : 2592000
Preferred lifetime : 604800
On-link : Yes
Autonomous : Yes

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

show ipv6 nd ra dns search-list
show ipv6 nd ra dns search-list

Description

Displays domain name information on all interfaces.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns search-list test.com
switch# show ipv6 nd ra dns search-list
Recursive DNS Search List on: 1

Suppress DNS Search List: Yes
DNS Search 1: test.com

lifetime 1800

Command History

IPv6 Router Advertisement | 42

Release

10.07 or earlier

Modification

--

Command Information

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
show ipv6 nd ra dns server

Description

Displays DNS server information on all interfaces.

Examples

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns server 2001::1
switch# show ipv6 nd ra dns server
Recursive DNS Server List on: 1

Suppress DNS Server List: Yes
DNS Server 1: 2001::1

lifetime 1800

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

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

43

Chapter 4

sFlow

sFlow

sFlow is a technology for monitoring traffic in switched or routed networks. The sFlow monitoring system is
comprised of:

n An sFlow Agent that runs on a network device, such as a switch. The agent uses sampling techniques to
capture information about the data traffic flowing through the device and forwards this information to
an sFlow collector.

n An sFlow Collector that receives monitoring information from sFlow agents. The collector stores this

information so that a network administrator can analyze it to understand network data flow patterns.
One sFlow collector can recieve the data from many sFlow agents.

The sFlow UDP datagrams sent to a collector are not encrypted, therefore any sensitive information contained in

an sFlow sample is exposed.

sFlow agent
The sFlow agent on the switch provides ingress sampling of all forwarded layer 2 and layer 3 traffic on LAG
and Ethernet ports. High-availability is supported (packet sampling continues to work after switch-over).

The sFlow agent can communicate with up to three sFlow collectors at the same time. The agent
communicates with collectors only on the default VRF.

Although you can configure very high sampling rates, the switch may drop samples if it cannot handle the
rate of sampled packets. High sampling rates may also cause high CPU usage resulting in control plane
performance issues.

A single sFlow datagram sent to a collector contains multiple flow and counter samples. The total number of
samples an sFlow datagram can contain varies depending on the settings for header size and maximum
datagram size.

Default settings

n sFlow is disabled on all interfaces.

n Collector port: UDP port 6343.

n Sampling rate: 4096.

n Polling interval: 30 seconds.

n Header size: 128 bytes.

n Max datagram size: 1400 bytes.

Supported features

n Global sampling rate

n Interface counters polling

n Agent IP configuration for IPv4 and IPv6

n Header size configuration

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

44

n Max datagram size configuration

n Ingress sampling for all forwarded traffic (L2, L3)

n Enable/Disable sFlow per interface

n Support for three remote collectors

n An out-of-band collector can be defined on the management VRF

n A collector can be defined on the non-default VRF

n Sampling on Ethernet and LAG interfaces

n High availability support (sampling continues to work after switch-over)

n Source IP support (setting source IP for sFlow datagrams sent to a remote collector)

Limitations

n No sampling of egress traffic

n Sampling rate cannot be set per interface (global only)

n sFlow is not configurable via SNMP

Configuring the sFlow agent

Procedure

1. Configure one or more sFlow collectors with the command sflow collector. This determines where

the sFlow agent sends sFlow information.

2. Enable the sFlow agent on all interfaces, or on a specific interface, with the command sflow.

3. Define the address of the sFlow agent with the command sflow agent-ip.

4. By default, the source IP address for sFlow datagrams is set to the IP address of the outgoing switch
interface on which the sFlow client is communicating with a collector. Since the switch can have
multiple routing interfaces, datagrams can potentially be sent on different paths at different times,
resulting in different source IP addresses for the same client. To resolve this issue, define a single
source IP address. For details, see Single source IP address in the Fundamentals Guide.

5. For most deployments, the default values for the following settings do not need to be changed. If

your deployment requires different settings, change the default values with the indicated
commands:

sFlow setting

Default value

Command to change it

Rate at which packets are sampled.

1 in every 4096 packets

sflow sampling

Rate at which the switch sends data to
an sFlow collector.

30 seconds

sflow polling

Size of the sFlow header.

128 bytes

sflow header-size

Maximum size of an sFlow datagram.

1400 bytes

sflow max-datagram-size

6. Review sFlow configuration settings with the command show sflow.

Example

This example creates the following configuration:

sFlow | 45

ConfiguresansFlowcollectorwiththeIPaddress10.10.20.209.
n
EnablesthesFlowagentonallinterfaces.
n
DefinesthesFlowagentIPaddresstobe10.10.1.5.
n
| switch(config)# | sflow | collector |     | 10.10.20.209 |
| --------------- | ----- | --------- | --- | ------------ |
| switch(config)# | sflow |           |     |              |
| switch(config)# | sflow | agent-ip  |     | 10.0.0.1     |
sFlow scenario
Inthisscenario,twohostssendsFlowtrafficthroughaswitchtoansFlowcollector.Thephysicaltopologyof
thenetworklookslikethis:
Procedure
1. EnablesFlowglobally.
| switch# config  |     |       |     |     |
| --------------- | --- | ----- | --- | --- |
| switch(config)# |     | sflow |     |     |
2. SetthesFlowagentIPaddressto10.10.12.1.
| switch(config)# |     | sflow agent-ip |     | 10.10.12.1 |
| --------------- | --- | -------------- | --- | ---------- |
3. SetthesFlowcollectorIPaddressto10.10.12.2.
| switch(config)# |     | sflow collector |     | 18.2.2.2 |
| --------------- | --- | --------------- | --- | -------- |
4. ConfiguresFLowsamplingrateandpollinginterval.
| switch(config)# |     | sflow sampling |     | 5000 |
| --------------- | --- | -------------- | --- | ---- |
| switch(config)# |     | sflow polling  |     | 20   |
5. Configureinterface1/1/1withIPaddress10.10.10.1/24.
| switch(config)#    |     | interface   | 1/1/1 |               |
| ------------------ | --- | ----------- | ----- | ------------- |
| switch(config-if)# |     | no shutdown |       |               |
| switch(config-if)# |     | ip address  |       | 10.10.10.1/24 |
| switch(config)#    |     | quit        |       |               |
6. Configureinterface1/1/2withIPaddress10.10.11.1/24.
| switch(config)#    |     | interface   | 1/1/2 |               |
| ------------------ | --- | ----------- | ----- | ------------- |
| switch(config-if)# |     | no shutdown |       |               |
| switch(config-if)# |     | ip address  |       | 10.10.11.1/24 |
| switch(config)#    |     | quit        |       |               |
7. Configureinterface1/1/3withIPaddress10.10.12.1/24.
| switch(config)#    |     | interface   | 1/1/3 |     |
| ------------------ | --- | ----------- | ----- | --- |
| switch(config-if)# |     | no shutdown |       |     |
46
AOS-CX10.09IPServicesGuide| (6200 SwitchSeries)

|     | switch(config-if)# |     | ip address | 10.10.12.1/24 |
| --- | ------------------ | --- | ---------- | ------------- |
|     | switch(config)#    |     | quit       |               |
8. VerifysFlowconfiguration
|     | switch#      | show sflow    |     |     |
| --- | ------------ | ------------- | --- | --- |
|     | sFlow Global | Configuration |     |     |
-----------------------------------------
|     | sFlow         |             |     | enabled                 |
| --- | ------------- | ----------- | --- | ----------------------- |
|     | Collector     | IP/Port/Vrf |     | 10.10.10.2/6343/default |
|     | Agent Address |             |     | 10.0.0.1                |
|     | Sampling      | Rate        |     | 1024                    |
|     | Polling       | Interval    |     | 30                      |
|     | Header        | Size        |     | 128                     |
|     | Max Datagram  | Size        |     | 1400                    |
|     | Sampling      | Mode        |     | both                    |
|     | sFlow Status  |             |     |                         |
-----------------------------------------
|     | Running       | - Yes |             |     |
| --- | ------------- | ----- | ----------- | --- |
|     | sFlow enabled | on    | Interfaces: |     |
-----------------------------------------
lag100
|     | sFlow Statistics |     |     |     |
| --- | ---------------- | --- | --- | --- |
-----------------------------------------
|       | Number   | of Ingress | Samples | 200 |
| ----- | -------- | ---------- | ------- | --- |
|       | Number   | of Egress  | Samples | 0   |
| sFlow | scenario |            | 2       |     |
Inthisscenario,twohostsconnectedtodifferentswitchessendsFlowtraffictoacollector.ALAGisusedto
connectthetwoswitches.Thephysicaltopologyofthenetworklookslikethis:
sFlow|47

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
| switch(config-lag-if)#           |           | vlan        | access | 8      |
| switch(config-lag-if)#           |           | lacp        | mode   | active |
48
AOS-CX10.09IPServicesGuide| (6200 SwitchSeries)

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
| switch(config)#                  |     | vlan | 8           |     |        |
| -------------------------------- | --- | ---- | ----------- | --- | ------ |
| switch(config-vlan-8)#           |     |      | no shutdown |     |        |
| switch(config)#                  |     | exit |             |     |        |
| b. DefineLAG100andassignVLANvlan |     |      |             |     | 8toit. |
switch(config)#
|                        |     | interface | lag         | 100    |        |
| ---------------------- | --- | --------- | ----------- | ------ | ------ |
| switch(config-lag-if)# |     |           | no shutdown |        |        |
| switch(config-lag-if)# |     |           | vlan        | access | 8      |
| switch(config-lag-if)# |     |           | lacp        | mode   | active |
c. Configureinterface1/1/1.
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
sFlow|49

|       | switch(config-if)#                                   |                    |          | no shutdown |                   |     |
| ----- | ---------------------------------------------------- | ------------------ | -------- | ----------- | ----------------- | --- |
|       | switch(config-if)#                                   |                    |          | vlan access | 8                 |     |
|       | d. Configureinterface1/1/2and1/1/3asmembersofLAG100. |                    |          |             |                   |     |
|       | switch#                                              | (config)#interface |          |             | 1/1/2             |     |
|       | switch(config-if)#                                   |                    |          | no shutdown |                   |     |
|       | switch(config-if)#                                   |                    |          | lag 100     |                   |     |
|       | switch(config-if)#                                   |                    |          | exit        |                   |     |
|       | switch(config)-if#                                   |                    |          | interface   | 1/1/3             |     |
|       | switch(config-if)#                                   |                    |          | no shutdown |                   |     |
|       | switch(config-if)#                                   |                    |          | lag 100     |                   |     |
|       | switch(config-if)#                                   |                    |          | exit        |                   |     |
| sFlow | agent                                                |                    | commands |             |                   |     |
| clear | sflow                                                | statistics         |          |             |                   |     |
| clear | sflow                                                | statistics         | {global  | | interface | <INTERFACE-NAME>} |     |
Description
ThiscommandclearsthesFlowsamplestatisticscounterto0eithergloballyorforaspecificinterface.
| Parameter |     |     |     |     | Description                        |     |
| --------- | --- | --- | --- | --- | ---------------------------------- | --- |
| global    |     |     |     |     | Specifiesallinterfacesontheswitch. |     |
interface <INTERFACE-NAME> Specifiesthenameofaninterfaceontheswitch.
Examples
ClearingtheglobalsFlowsamplestatisticscounterto0globally:
| switch(config)# |     |     | clear | sflow statistics | global |     |
| --------------- | --- | --- | ----- | ---------------- | ------ | --- |
ClearingtheglobalsFlowsamplestatisticscounterto0forinterface1/1/1:
| switch(config)# |     |     | clear | sflow statistics | interface | 1/1/1 |
| --------------- | --- | --- | ----- | ---------------- | --------- | ----- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow
50
| AOS-CX10.09IPServicesGuide| |     | (6200 | SwitchSeries) |     |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- | --- |

sflow
no sflow
Description
EnablesthesFlowagent.
n Intheconfigcontext,thiscommandenablesthesFlowagentgloballyonallinterfaces.
n Inanconfig-ifcontext,thiscommandenablesthesFlowagentonaspecificinterface.sFlowcannotbe
enabledonamemberofaLAG,onlyontheLAG.
ThesFlowagentisdisabledbydefault.
ThenoformofthiscommanddisablesthesFlowagentanddeletesallsFlowconfigurationsettings,either
globally,orforaspecificinterface.
Examples
EnablingsFlowgloballyonallinterfaces:
switch(config)#
sflow
DisablingsFlowgloballyonallinterfaces:
| switch(config)# | no sflow |     |
| --------------- | -------- | --- |
EnablingsFlowoninterface1/1/1:
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | sflow     |       |
DisablingsFlowoninterface1/1/1:
switch(config)#
|                    | interface | 1/1/1 |
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
CommandHistory
Release Modification
10.07orearlier --
sFlow|51

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if | forthiscommand. |
| --- | --------- | --------------- |
sflow agent-ip
| sflow agent-ip    | <IP-ADDR>   |     |
| ----------------- | ----------- | --- |
| no sflow agent-ip | [<IP-ADDR>] |     |
Description
DefinestheIPaddressofthesFlowagenttouseinsFlowdatagrams.ThisaddressmustbedefinedforsFlow
tofunction.HPErecommendsthattheaddress:
n canuniquelyidentifytheswitch
n isreachablebythesFlowcollector
doesnotchangewithtime
n
ThenoformofthiscommanddeletestheIPaddressofthesFlowagent.ThiscausessFlowtostopworking
andnodatagramswillbesenttothesFlowcollector.
| Parameter |     | Description |
| --------- | --- | ----------- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Theagentaddressisusedto
identifytheswitchinallsFlowdatagramssenttosFlowcollectors.
ItisusuallysettoanIPaddressontheswitchthatisreachable
fromansFlowcollector.
Examples
Settingtheagentaddressto10.10.10.100:
| switch(config)# | sflow agent-ip | 10.0.0.100 |
| --------------- | -------------- | ---------- |
Settingtheagentaddressto2001:0db8:85a3:0000:0000:8a2e:0370:7334:
switch(config)# sflow agent-ip 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Removingtheaddressconfigurationfromtheswitch,whichresultsinsFlowbeingdisabled:
| switch(config)# | no sflow agent-ip |     |
| --------------- | ----------------- | --- |
CommandHistory
52
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| sflow collector    |           |       |         |             |        |
| ------------------ | --------- | ----- | ------- | ----------- | ------ |
| sflow collector    | <IP-ADDR> | [port | <PORT>] | [vrf <VRF>] |        |
| no sflow collector | <IP-ADDR> | [port | <PORT>] | [vrf        | <VRF>] |
Description
DefinesacollectortowhichthesFlowagentsendsdata.Uptothreecollectorscanbedefined.Atleastone
collectorshouldbedefined,anditmustbereachablefromtheswitchforsFlowtowork.
| Parameter |           |     | Description |     |     |
| --------- | --------- | --- | ----------- | --- | --- |
| collector | <IP-ADDR> |     |             |     |     |
SpecifiestheIPaddressofacollectorinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
port <PORT> SpecifiestheUDPportonwhichtosendinformationtothesFlow
collector.Range:0to65536.Default:6343.
| vrf <VRF> |     |     | SpecifiestheVRFonwhichtosendinformationtothesFlow |     |     |
| --------- | --- | --- | ------------------------------------------------- | --- | --- |
collector.TheVRFmustbedefinedontheswitch.IfnoVRFis
specified,thedefaultVRF(default)isused.
Example
DefiningacollectorwithIPaddress10.10.10.100onUDPport6400:
| switch(config)# | sflow | collector | 10.0.0.1 | port | 6400 |
| --------------- | ----- | --------- | -------- | ---- | ---- |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sFlow|53

sflow disable
sflow disable
Description
DisablesthesFlowagent,butretainsanyexistingsFlowconfigurationsettings.Thesettingsbecomeactiveif
thesFlowagentisre-enabled.
Example
DisablingsFlowsupport:
| switch(config)# | sflow disable |     |
| --------------- | ------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow header-size
| sflow header-size    | <SIZE>   |     |
| -------------------- | -------- | --- |
| no sflow header-size | [<SIZE>] |     |
Description
SetsthesFlowheadersizeinbytes.
Thenoformofthiscommandsetstheheadersizetothedefaultvalueof128.
| Parameter |     | Description |
| --------- | --- | ----------- |
header-size <SIZE> SpecifiesthesFlowheadersizeinbytes.Range:64to256.Default:
128.
Examples
Settingtheheadersizeto64bytes:
| switch(config)# | sflow header-size | 64  |
| --------------- | ----------------- | --- |
Settingtheheadersizetothedefaultvalueof128bytes:
| switch(config)# | no sflow header-size |     |
| --------------- | -------------------- | --- |
54
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow max-datagram-size
sflow max-datagram-size <SIZE>
no sflow max-datagram-size [<SIZE>]
Description
SetsthemaximumnumberofbytesthataresentinonesFlowdatagram.
Thenoformofthiscommandsetsmaximumnumberofbytestothedefaultvalueof1400.
| Parameter |     | Description |
| --------- | --- | ----------- |
max-datagram-size <SIZE> Specifiesthemaximumdatagramsizeinbytes.Range:1to9000.
Default:1400.
Examples
Settingthedatagramsizeto1000bytes:
| switch(config)# | sflow max-datagram-size | 1000 |
| --------------- | ----------------------- | ---- |
Settingtheheadersizetothedefaultvalueof1400bytes:
| switch(config)# | no sflow max-datagram-size |     |
| --------------- | -------------------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sFlow|55

| sflow      | mode          |     |          |         |     |
| ---------- | ------------- | --- | -------- | ------- | --- |
| sflow mode | {ingress      | |   | egress   | | both} |     |
| no sflow   | mode {ingress |     | | egress | | both} |     |
Description
SetsthesFlowsamplingmode.Thedefaultmodeisingress.
Thenoformofthecommandsetsthesamplingmodetoingress.Executingthenoformofthecommand
withtheingressoptionwillhavenoimpactasingressisthedefaultmode.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
ingress
Samplesonlyingresstraffic.
| egress |     |     |     |     | Samplesonlyegresstraffic. |
| ------ | --- | --- | --- | --- | ------------------------- |
both
Samplesbothingressandegresstraffic.
Examples
SettingthesFlowmodetoonlysampleegresstraffic:
| switch#         | configure |       | terminal |        |     |
| --------------- | --------- | ----- | -------- | ------ | --- |
| switch(config)# |           | sflow | mode     | egress |     |
ResettingthesFlowsamplingmodetothedefaultofingressfrompreviouslyconfiguredmodeofegress:
| switch#         | configure |     | terminal |             |     |
| --------------- | --------- | --- | -------- | ----------- | --- |
| switch(config)# |           | no  | sflow    | mode egress |     |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| sflow         | polling    |              |     |     |     |
| ------------- | ---------- | ------------ | --- | --- | --- |
| sflow polling | <INTERVAL> |              |     |     |     |
| no sflow      | polling    | [<INTERVAL>] |     |     |     |
Description
DefinestheglobalpollingintervalforsFlowinseconds.
Thenoformofthiscommandsetsthepollingintervaltothedefaultvalueof30seconds.
56
| AOS-CX10.09IPServicesGuide| |     | (6200 | SwitchSeries) |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- |

| Parameter |     | Description |
| --------- | --- | ----------- |
<INTERVAL> Specifiesthepollingintervalinseconds.Range:10to3600.
Default:30.
Examples
Settingthepollingintervalto10:
| switch(config)# | sflow polling | 10  |
| --------------- | ------------- | --- |
Settingthepollingintervaltothedefaultvalue.
| switch(config)# | no sflow polling |     |
| --------------- | ---------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow sampling
| sflow sampling    | <RATE>   |     |
| ----------------- | -------- | --- |
| no sflow sampling | [<RATE>] |     |
Description
DefinestheglobalsamplingrateforsFlowinnumberofpackets.Thedefaultsamplingrateis4096,which
meansthatoneinevery4096packetsissampled.Awarningmessageisdisplayedwhenthesamplingrateis
settolessthan4096andproceedsonlyafteruserconfirmation.
Thenoformofthiscommandsetsthesamplingratetothedefaultvalueof4096.
| Parameter |     | Description |
| --------- | --- | ----------- |
sampling <RATE> Specifiesthesamplingrate.Range:1to1000000000.Default:
4096.
Examples
Settingthesamplingrateto5000:
| switch(config)# | sflow sampling | 5000 |
| --------------- | -------------- | ---- |
Settingthesamplingratetothedefault:
sFlow|57

switch(config)# no sflow sampling

Setting the sampling rate to 1000:

switch(config)# sflow sampling 1000
Setting the sFlow sampling rate lower than 4096 is not recommended and might
affect system performance.
Do you want to continue [y/n]? y
switch(config)#

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

config

Administrators or local user group members with execution rights
for this command.

show sflow
show sflow [interface <INTERFACE-NAME>]

Description

Shows sFlow configuration settings and statistics for all interfaces, or for a specific interface

Parameter

Description

interface <INTERFACE-NAME>

Specifies the name of an interface on the switch.

Examples

switch# show sflow
sFlow Global Configuration
-----------------------------------------
sFlow
Collector IP/Port/Vrf
Agent Address
Sampling Rate
Polling Interval
Header Size
Max Datagram Size
Sampling Mode

enabled
10.10.10.2/6343/default
10.0.0.1
1024
30
128
1400
both

sFlow Status
-----------------------------------------
Running - Yes

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

58

| sFlow enabled | on  | Interfaces: |     |     |
| ------------- | --- | ----------- | --- | --- |
-----------------------------------------
lag100
| sFlow Statistics |     |     |     |     |
| ---------------- | --- | --- | --- | --- |
-----------------------------------------
| Number | of Ingress | Samples | 200 |     |
| ------ | ---------- | ------- | --- | --- |
| Number | of Egress  | Samples | 0   |     |
ShowingsFlowinformationforinterface1/1/1:
| switch#             | show sflow | interface   | 1/1/1 |       |
| ------------------- | ---------- | ----------- | ----- | ----- |
| sFlow configuration |            | - Interface |       | 1/1/1 |
-----------------------------------------
| sFlow          |            |         | enabled |     |
| -------------- | ---------- | ------- | ------- | --- |
| Sampling       | Rate       |         | 1024    |     |
| Sampling       | Mode       |         | both    |     |
| Number         | of Ingress | Samples | 81      |     |
| Number         | of Egress  | Samples | 20      |     |
| sFlow Sampling | Status     |         | success |     |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sFlow|59

Chapter 5
DHCP
DHCP
TheDynamicHostConfigurationProtocol(DHCP)enablestheautomaticassignmentofIPaddressesand
otherconfigurationsettingstonetworkdevices.
TheDHCPrelayagentactsanintermediary,forwardingDHCPrequests/responsebetweenDHCP
clients/serversondifferentnetworks.ThisenablesDHCPclientstousetheservicesofDHCPserversthatare
notonthesamesubnetonwhichtheyarelocated.
DHCP client
| DHCP client | commands |     |
| ----------- | -------- | --- |
ipdhcp
ip dhcp
no ip dhcp
Description
EnablestheDHCPclientonthemanagementinterfaceoranyinterfaceVLAN toautomaticallyobtainanIP
addressfromaDHCPserveronthenetwork.Bydefault,theDHCPclientisenabledonthemanagement
interfaceandVLAN1.
ThenoformofthecommanddisablesDHCPmodeandissupportedonlyoninterfaceVLANs;itisnot
supportedonthemanagementinterface.
Examples
EnablingtheDHCPclientonthemanagementinterface:
switch(config)#
|                         | interface | mgmt        |
| ----------------------- | --------- | ----------- |
| switch(config-if-mgmt)# |           | ip dhcp     |
| switch(config-if-mgmt)# |           | no shutdown |
EnablingtheDHCPclientontheinterfacevlan1:
| switch(config)#         | interface | vlan 1      |
| ----------------------- | --------- | ----------- |
| switch(config-if-vlan)# |           | ip dhcp     |
| switch(config-if-vlan)# |           | no shutdown |
DisablingtheDHCPclientontheinterfacevlan1:
switch(config)#
|                         | interface | vlan 1     |
| ----------------------- | --------- | ---------- |
| switch(config-if-vlan)# |           | no ip dhcp |
Iftheinterfaceisnotenabled,youcanenableitbyenteringtheno shutdowncommand.
60
AOS-CX10.09IPServicesGuide| (6200 SwitchSeries)

ip dhcpissupportedonlyononevlanatatime.
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan | forthiscommand. |
| --- | -------------- | --------------- |
show ipdhcp
show ip dhcp
Description
DisplaysDHCPIPv4informationontheports.
Examples
DisplayingtheDHCPIPv4informationontheports:
| switch# show | ip dhcp |     |
| ------------ | ------- | --- |
INTERFACE-NAME ADDRESS DEFAULT_GATEWAY DOMAIN_NAME VRF DNS-SERVERS
--------------------------------------------------------------------------------------------------
-------
vlan1 10.254.239.10/27 domain.com default 50.0.0.2, 50.0.0.3,
50.0.0.4
CommandHistory
| Release        |     | Modification       |
| -------------- | --- | ------------------ |
| 10.09orearlier |     | Commandintroduced. |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| DHCP relay | agent |     |
| ---------- | ----- | --- |
DHCP|61

The function of the DHCP relay agent is to forward the DHCP messages to other subnets so that the DHCP
server does not have to be on the same subnet as the DHCP clients. The DHCP relay agent transfers DHCP
messages from the DHCP clients located on a subnet without a DHCP server, to other subnets. It also relays
answers from DHCP servers to DHCP clients.

Supported interfaces

The DHCP relay agent is supported on layer 3 interfaces, layer 3 VLAN interfaces, and LAG interfaces. DHCP
relay is not supported on the management interface.

DHCP server interoperation

Both DHCP relay and DHCP server can be configured on the same VRF.

DHCPv4 relay agent

Hop count in DHCP requests

When a DHCP client broadcasts request, the DHCP relay agent in the switch receives the packets and
forwards them to the DHCP server as unicast requests. During this process, the DHCP relay agent
increments the hop count before forwarding DHCP packets to the server. The DHCP server, in turn, includes
the hop count in the DHCP header in the response sent back to a DHCP client.

DHCP relay option 82

Option 82 is called the relay agent information option. When a DHCP relay agent forwards client-originated
DHCP packets to a DHCP server, the option 82 field is inserted/replaced, or the packet with this option is
dropped. Servers recognizing the relay agent information option may use the information to implement
policies for the assignment of IP addresses and other parameters. The relay agent relays the server-to-client
replies to the client.

If a second relay agent is configured to add its own option 82 information, it can encapsulate option 82
information in messages from a first relay agent. The DHCP server uses the option 82 information from
both relay agents to decide the IP address for the client.

Configuring a BOOTP/DHCP relay gateway

The DHCP relay agent selects the lowest-numbered IP address on the interface to use for DHCP messages.
The DHCP server then uses this IP address when it assigns client addresses. However, this IP address may
not be the same subnet as the one on which the client needs the DHCP service. This feature provides a way
to configure a gateway address for the DHCP relay agent to use for relayed DHCP requests, rather than the
DHCP relay agent automatically assigning the lowest-numbered IP address.

Configuring the DHCPv4 relay agent

Prerequisites

n An enabled layer 3 interface.

Procedure

1. The DHCPv4 relay agent is enabled by default. If it was previously disabled, enable it with the

command dhcp-relay.

2. Configure one or more IP helper addresses with the command ip helper-address. This determines
where the DHCPv4 agent forwards DHCP requests. IP helper addresses can be configured on layer 3
interfaces, layer 3 VLAN interfaces, and LAG interfaces.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

62

3. IfyouwanttomodifythecontentofforwardedDHCPpacketsordropDHCPpackets,configure
| option82supportwiththecommanddhcp-relay |     |     |     |     | option | 82. |
| --------------------------------------- | --- | --- | --- | --- | ------ | --- |
4. DefinethegatewayaddressthattheDHCPv4agentwillusewiththecommandipbootp-gateway.
5. Ifrequired,enablethehopcountincrementfeaturewiththecommanddhcp-relay hop-count-
increment.
6. ReviewDHCPv4relayagentconfigurationsettingswiththecommandsshow dhcp-relay,show ip
| helper-address,andshow |     |     |     | dhcp-relay | bootp-gateway. |     |
| ---------------------- | --- | --- | --- | ---------- | -------------- | --- |
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablestheDHCPv4relayagent.
Enablesinterface1/1/1andassignsanIPv4addresstoit.(Bydefault,allinterfacesarelayer3and
n
disabled.)
n DefinesanIPhelperaddressof10.10.20.209ontheinterface.
EnablesDHCPoption82supportandreplacesalloption82informationwiththevaluesfromtheswitch
n
withtheswitchMACaddressastheremoteID.
| switch(config)#    |             | dhcp-relay |                   |                 |                |     |
| ------------------ | ----------- | ---------- | ----------------- | --------------- | -------------- | --- |
| switch(config)#    |             | interface  |                   | 1/1/1           |                |     |
| switch(config-if)# |             |            | no shutdown       |                 |                |     |
| switch(config-if)# |             |            | ip address        | 198.51.100.1/24 |                |     |
| switch(config-if)# |             |            | ip helper-address |                 | 10.10.20.209   |     |
| switch(config-if)# |             |            | exit              |                 |                |     |
| switch(config)#    |             | dhcp-relay |                   | option          | 82 replace mac |     |
| switch#            | show        | dhcp-relay |                   |                 |                |     |
| DHCP Relay         | Agent       |            |                   |                 | : Enabled      |     |
| DHCP Request       |             | Hop Count  |                   | Increment       | : Enabled      |     |
| Option             | 82          |            |                   |                 | : Disabled     |     |
| Response           | Validation  |            |                   |                 | : Disabled     |     |
| Option             | 82 Handle   | Policy     |                   |                 | : replace      |     |
| Remote             | ID          |            |                   |                 | : mac          |     |
| DHCP Relay         | Statistics: |            |                   |                 |                |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |                |     | 60  | 10  |
| ---------- | ------ | --- | -------------- | --- | --- | --- |
| DHCP Relay | Option |     | 82 Statistics: |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50  |     | 8   |     |     | 50  | 8   |
| --- | --- | --- | --- | --- | --- | --- |
DHCPv4relayscenario1
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
DHCP|63

Procedure
1. DHCPrelayisenabledbydefault.Ifitwaspreviouslydisabled,enableit.
| switch#         | config |            |     |     |     |     |
| --------------- | ------ | ---------- | --- | --- | --- | --- |
| switch(config)# |        | dhcp-relay |     |     |     |     |
2. DefineanIPv4helperaddressoninterfaces1/1/1and1/1/2.
| switch(config)#    |     | interface |           | 1/1/1                   |             |     |
| ------------------ | --- | --------- | --------- | ----------------------- | ----------- | --- |
| switch(config-if)# |     |           | ip        | address 192.168.2.11/24 |             |     |
| switch(config-if)# |     |           | ip        | helper-address          | 192.168.1.1 |     |
| switch(config-if)# |     |           | interface | 1/1/2                   |             |     |
| switch(config-if)# |     |           | ip        | address 192.168.2.12/24 |             |     |
switch(config-if)#
|                    |     |     | ip   | helper-address | 192.168.1.1 |     |
| ------------------ | --- | --- | ---- | -------------- | ----------- | --- |
| switch(config-if)# |     |     | quit |                |             |     |
3. VerifyDHCPrelayconfiguration.
|     | switch#          | show dhcp-relay |           |           |            |     |
| --- | ---------------- | --------------- | --------- | --------- | ---------- | --- |
|     | DHCP Relay       | Agent           |           |           | : Enabled  |     |
|     | DHCP Request     |                 | Hop Count | Increment | : Enabled  |     |
|     | L2VPN Clients    |                 |           |           | : Disabled |     |
|     | Option           | 82              |           |           | : Disabled |     |
|     | Source-Interface |                 |           |           | : Disabled |     |
|     | Response         | Validation      |           |           | : Disabled |     |
|     | Option           | 82 Handle       | Policy    |           | : replace  |     |
|     | Remote           | ID              |           |           | : mac      |     |
|     | DHCP Relay       | Statistics:     |           |           |            |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|     | 60         |        | 10  |                | 60  | 10  |
| --- | ---------- | ------ | --- | -------------- | --- | --- |
|     | DHCP Relay | Option |     | 82 Statistics: |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|     | 50  |     | 8   |     | 50  | 8   |
| --- | --- | --- | --- | --- | --- | --- |
switch#
|     |            | show ip   | helper-address |     |     |     |
| --- | ---------- | --------- | -------------- | --- | --- | --- |
|     | IP Helper  | Addresses |                |     |     |     |
|     | Interface: | 1/1/1     |                |     |     |     |
|     | IP Helper  | Address   |                | VRF |     |     |
64
AOS-CX10.09IPServicesGuide| (6200 SwitchSeries)

| ----------------- |         |     | ----------------- |     |     |
| ----------------- | ------- | --- | ----------------- | --- | --- |
| 192.168.1.1       |         |     | default           |     |     |
| Interface:        | 1/1/2   |     |                   |     |     |
| IP Helper         | Address |     | VRF               |     |     |
| ----------------- |         |     | ----------------- |     |     |
| 192.168.1.1       |         |     | default           |     |     |
DHCPv4relayscenario2
Inthisscenario,hostonswitch1reachestheDHCPserveronswitchtwoviaaLAG.Thephysicaltopologyof
thenetworklookslikethis:
Procedure
1. Onswitch1:
a. CreateLAG100andassignanIPaddresstoit.
| switch# config         |     |           |            |      |              |
| ---------------------- | --- | --------- | ---------- | ---- | ------------ |
| switch(config)#        |     | interface | lag        | 100  |              |
| switch(config-lag-if)# |     |           | ip address |      | 10.0.10.1/24 |
| switch(config-lag-if)# |     |           | lacp       | mode | active       |
| switch(config-lag-if)# |     |           | exit       |      |              |
switch(config)#
b. AssignanIPaddresstointerface1/1/1andaanIPhelperaddresstoreachtheDHCPserver.
| switch(config)#    |     | interface | 1/1/1   |            |     |
| ------------------ | --- | --------- | ------- | ---------- | --- |
| switch(config-if)# |     | ip        | address | 20.0.0.1/8 |     |
switch(config-if)#
|     |     | ip  | helper-address |     | 9.0.0.2 |
| --- | --- | --- | -------------- | --- | ------- |
c. Assigninterfaces1/1/2and1/1/3toLAG100
| switch(config-if)# |     | interface |     | 1/1/2 |     |
| ------------------ | --- | --------- | --- | ----- | --- |
| switch(config-if)# |     | lag       | 100 |       |     |
| switch(config-if)# |     | interface |     | 1/1/3 |     |
| switch(config-if)# |     | lag       | 100 |       |     |
| switch(config-if)# |     | exit      |     |       |     |
switch(config)#
d. Createaroutebetween10.0.10.2and9.0.0.0.
| switch(config)# |     | ip route | 9.0.0.0/24 |     | 10.0.10.2 |
| --------------- | --- | -------- | ---------- | --- | --------- |
2. Onswitch2:
a. CreateLAG100andassignanIPaddresstoit.
| switch# config         |     |           |            |      |              |
| ---------------------- | --- | --------- | ---------- | ---- | ------------ |
| switch(config)#        |     | interface | lag        | 100  |              |
| switch(config-lag-if)# |     |           | ip address |      | 10.0.10.2/24 |
| switch(config-lag-if)# |     |           | lacp       | mode | active       |
DHCP|65

| switch(config-lag-if)# |     |     | exit |     |
| ---------------------- | --- | --- | ---- | --- |
switch(config)#
| b. Assigninterfaces1/1/1and1/1/2toLAG100 |     |           |       |     |
| ---------------------------------------- | --- | --------- | ----- | --- |
| switch(config-if)#                       |     | interface | 1/1/2 |     |
| switch(config-if)#                       |     | lag       | 100   |     |
| switch(config-if)#                       |     | interface | 1/1/3 |     |
| switch(config-if)#                       |     | lag       | 100   |     |
| switch(config-if)#                       |     | exit      |       |     |
switch(config)#
| c. AssignanIPaddresstointerface1/1/3.       |     |            |            |           |
| ------------------------------------------- | --- | ---------- | ---------- | --------- |
| switch(config)#                             |     | interface  | 1/1/3      |           |
| switch(config-if)#                          |     | ip address | 9.0.0.1/24 |           |
| d. Createaroutebetween20.0.0.0and10.0.10.1. |     |            |            |           |
| switch(config)#                             |     | ip route   | 20.0.0.0/8 | 10.0.10.1 |
DHCPv4relaycommands
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
| switch(config)# | no  | dhcp-relay |     |     |
| --------------- | --- | ---------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcp-relay hop-count-increment |                     |     |     |     |
| ------------------------------ | ------------------- | --- | --- | --- |
| dhcp-relay hop-count-increment |                     |     |     |     |
| no dhcp-relay                  | hop-count-increment |     |     |     |
66
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |     |
| --------------------------- | ----- | ------------- | --- | --- |

Description
EnablestheDHCPrelayhopcountincrementfeature,whichcausestheDHCPrelayagenttoincrementthe
hopcountinallrelayedDHCPpackets.Hopcountisenabledbydefault.
Thenoformofthiscommanddisablesthehopcountincrementfeature.
Examples
Enablingthehopcountincrementfeature.
| switch(config)# |     | dhcp-relay | hop-count-increment |     |     |     |     |     |
| --------------- | --- | ---------- | ------------------- | --- | --- | --- | --- | --- |
Disablingthehopcountincrementfeature.
| switch(config)# |     | no dhcp-relay | hop-count-increment |     |     |     |     |     |
| --------------- | --- | ------------- | ------------------- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcp-relay    | option | 82                 |            |     |          |            |              |        |
| ------------- | ------ | ------------------ | ---------- | --- | -------- | ---------- | ------------ | ------ |
| dhcp-relay    | option | 82 {replace        | [validate] |     | | drop   | [validate] | |            |        |
|               | keep   | | source-interface |            | |   | validate | [replace   | | drop]} [ip | | mac] |
| no dhcp-relay | option | 82 {replace        | [validate] |     | | drop   | [validate] | |            |        |
|               | keep   | | source-interface |            | |   | validate | [replace   | | drop]} [ip | | mac] |
Description
ConfiguresthebehaviorofDHCPrelayoption82.ADHCPrelayagentcanreceiveamessagefromanother
DHCPrelayagenthavingoption82.Therelayinformationfromthepreviousrelayagentisreplacedby
default.
ThenoformofthiscommanddisablestheDHCPrelayoption82configurations.
| Parameter |     |     |     | Description                                          |     |     |     |     |
| --------- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- |
| replace   |     |     |     | Replacetheexistingoption82fieldinaninboundclientDHCP |     |     |     |     |
packetwiththeinformationfromtheswitch.TheremoteIDand
circuitIDinformationfromthefirstrelayagentislost.Default.
| validate |     |     |     | Validateoption82informationinDHCPserverresponsesand |     |     |     |     |
| -------- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- |
dropinvalidresponses.
| drop |     |     |     | DropanyinboundclientDHCPpacketthatcontainsoption82 |     |     |     |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- |
DHCP|67

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
information.
keep Keeptheexistingoption82fieldinaninboundclientDHCPpacket.
TheremoteIDandcircuitIDinformationfromthefirstrelayagent
ispreserved.
source-interface
ConfigurestheDHCPrelaytouseaconfiguredsourceIPaddress
forinter-VRFserverreachability.SetthesourceIPaddresswith
thecommandip source-interface.
ip
UsetheIPaddressoftheinterfaceonwhichtheclientDHCP
packetenteredtheswitchastheoption82remoteID.
| mac |     |     | UsetheMACaddressoftheswitchastheoption82remoteID. |
| --- | --- | --- | ------------------------------------------------- |
Default.
Example
ThisexampleenablesDHCPoption82supportandreplacesalloption82informationwiththevaluesfrom
theswitch,withtheswitchMACaddressastheremoteID.
| switch(config)# | dhcp-relay | option | 82 replace mac |
| --------------- | ---------- | ------ | -------------- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipbootp-gateway
| ip bootp-gateway    | <IPV4-ADDR> |     |     |
| ------------------- | ----------- | --- | --- |
| no ip bootp-gateway | <IPV4-ADDR> |     |     |
Description
ConfiguresagatewayaddressfortheDHCPrelayagenttouseforDHCPrequests.BydefaultDHCPrelay
agentpicksthelowest-numberedIPaddressontheinterface.
Thenoformofthiscommandremovesthegatewayaddress.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiestheIPaddressofthegatewayinIPv4format(x.x.x.x),
wherexisaisadecimalnumberfrom0to255.
Examples
68
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

SetstheIPaddressofthegatewayforinterface1/1/1to10.10.10.10.
| switch(config)#    |     | interface        | 1/1/1 |             |     |
| ------------------ | --- | ---------------- | ----- | ----------- | --- |
| switch(config-if)# |     | ip bootp-gateway |       | 10.10.10.10 |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
iphelper-address
| ip helper-address    |     | <IPV4-ADDR> | [vrf | <VRF-NAME>] |     |
| -------------------- | --- | ----------- | ---- | ----------- | --- |
| no ip helper-address |     | <IPV4-ADDR> | [vrf | <VRF-NAME>] |     |
Description
DefinestheaddressofaremoteDHCPserverorDHCPrelayagent.Uptoeightaddressescanbedefined.
TheDHCPagentforwardsDHCPclientrequeststoalldefinedservers.
ThiscommandrequiresthatyoudefineasourceIPaddressforDHCPrelaywiththecommand ip source-
interface.TheconfiguredsourceIPontheVRFisusedtoforwardDHCPpacketstotheserver.
AhelperaddresscannotbedefinedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
helper-address <IPV4-ADDR> SpecifiesthehelperIPaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
Examples
DefiningtheIPhelperaddress10.10.10.209oninterface1/1/1.
| switch(config)#    |     | interface         | 1/1/1 |     |              |
| ------------------ | --- | ----------------- | ----- | --- | ------------ |
| switch(config-if)# |     | ip helper-address |       |     | 10.10.10.209 |
RemovingtheIPhelperaddress10.10.10.209oninterface1/1/1.
| switch(config-if)# |     | no ip | helper-address |     | 10.10.10.209 |
| ------------------ | --- | ----- | -------------- | --- | ------------ |
CommandHistory
DHCP|69

| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
showdhcp-relay
show dhcp-relay
Description
ShowsDHCPrelayconfigurationsettings.
Example
| switch#          | show dhcp-relay |           |           |            |     |
| ---------------- | --------------- | --------- | --------- | ---------- | --- |
| DHCP Relay       | Agent           |           |           | : Enabled  |     |
| DHCP Request     |                 | Hop Count | Increment | : Enabled  |     |
| L2VPN Clients    |                 |           |           | : Disabled |     |
| Option           | 82              |           |           | : Disabled |     |
| Source-Interface |                 |           |           | : Disabled |     |
| Response         | Validation      |           |           | : Disabled |     |
| Option           | 82 Handle       | Policy    |           | : replace  |     |
| Remote           | ID              |           |           | : mac      |     |
| DHCP Relay       | Statistics:     |           |           |            |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |             | 60  | 10  |
| ---------- | ------ | --- | ----------- | --- | --- |
| DHCP Relay | Option | 82  | Statistics: |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50  |     | 8   |     | 50  | 8   |
| --- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
70
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

| showdhcp-relay  | bootp-gateway |     |            |     |                   |
| --------------- | ------------- | --- | ---------- | --- | ----------------- |
| show dhcp-relay | bootp-gateway |     | [interface |     | <INTERFACE-NAME>] |
Description
Showsthebootpgatewaydefinedforallinterfacesoraspecificinterface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<INTERFACE-NAME> Specifiesaninterface.Format:member/slot/port.
Examples
| switch#              | show dhcp-relay |                 | bootp-gateway |           |       |
| -------------------- | --------------- | --------------- | ------------- | --------- | ----- |
| BOOTP Gateway        | Entries         |                 |               |           |       |
| Interface            |                 | Source          | IP            |           |       |
| -------------------- |                 | --------------- |               |           |       |
| 1/1/1                |                 | 1.1.1.1         |               |           |       |
| 1/1/2                |                 | 1.1.1.2         |               |           |       |
| switch#              | show ip         | helper-address  |               | interface | 1/1/1 |
| BOOTP Gateway        | Entries         |                 |               |           |       |
| Interface            |                 | Source          | IP            |           |       |
| -------------------- |                 | --------------- |               |           |       |
| 1/1/1                |                 | 1.1.1.1         |               |           |       |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
showiphelper-address
| show ip helper-address |     | [interface | <INTERFACE-ID>] |     |     |
| ---------------------- | --- | ---------- | --------------- | --- | --- |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
DHCP|71

| Parameter |                |     | Description |
| --------- | -------------- | --- | ----------- |
| interface | <INTERFACE-ID> |     |             |
Specifiesaninterface.Format:member/slot/port.
Example
switch#
| IP Helper         | Addresses              |                   |                 |
| ----------------- | ---------------------- | ----------------- | --------------- |
| Interface:        | 1/1/1                  |                   |                 |
| IP Helper         | Address                | VRF               |                 |
| ----------------- |                        | ----------------- |                 |
| 192.168.20.1      |                        | default           |                 |
| 192.168.10.1      |                        | default           |                 |
| Interface:        | 1/1/2                  |                   |                 |
| IP Helper         | Address                | VRF               |                 |
| ----------------- |                        | ----------------- |                 |
| 192.168.30.1      |                        | RED               |                 |
| switch#           | show ip helper-address |                   | interface 1/1/1 |
| IP Helper         | Addresses              |                   |                 |
| Interface:        | 1/1/1                  |                   |                 |
| IP Helper         | Address                | VRF               |                 |
| ----------------- |                        | ----------------- |                 |
| 192.168.20.1      |                        | default           |                 |
| 192.168.10.1      |                        | default           |                 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| DHCPv6 relay   | agent            |     |     |
| -------------- | ---------------- | --- | --- |
| Configuringthe | DHCPv6relayagent |     |     |
Prerequisites
n Anenabledlayer3interface.
Procedure
72
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

1. EnabletheDHCPv6agentwiththecommanddhcpv6-relay.
2. ConfigureoneormoreIPhelperaddresseswiththecommandipv6 helper-address.This
determineswheretheDHCPv6agentforwardDHCPrequests.
3. IfyouwanttoenableDHCPoption79supporttoforwardclientlink-layeraddresses,usethe
| commanddhcpv6-relay |     | option 79. |     |
| ------------------- | --- | ---------- | --- |
4. ReviewDHCPv6relayagentconfigurationsettingswiththecommandsshow dhcpv6-relayandshow
ipv6 helper-address.
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablestheDHCPv6relayagent.
Enablesinterface1/1/2andassignsanIPv6addresstoit.(Bydefault,allinterfacesarelayer3and
n
disabled.)
n DefinesanIPhelperaddressofFF01::1:1000oninterface1/1/2.
EnablesDHCPoption79.
n
| switch(config)#    | dhcpv6-relay |       |     |
| ------------------ | ------------ | ----- | --- |
| switch(config)#    | interface    | 1/1/2 |     |
| switch(config-if)# | no shutdown  |       |     |
switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
| switch(config-if)# | ip helper-address |        | FF01::1:1000 |
| ------------------ | ----------------- | ------ | ------------ |
| switch(config-if)# | exit              |        |              |
| switch(config)#    | dhcpv6-relay      | option | 79           |
DHCPv6relayscenario1
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
Procedure
DHCP|73

1. EnableDHCPrelay.
| switch# config  |              |     |     |     |
| --------------- | ------------ | --- | --- | --- |
| switch(config)# | dhcpv6-relay |     |     |     |
2. DefineanIPv6helperaddressoninterfaces1/1/1and1/1/2.
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|                    | ipv6      | address 2002::22/64 |         |     |
| ------------------ | --------- | ------------------- | ------- | --- |
| switch(config-if)# | ipv6      | helper-address      | 2001::1 |     |
| switch(config-if)# | interface | 1/1/2               |         |     |
| switch(config-if)# | ipv6      | address 2002::21/64 |         |     |
| switch(config-if)# | ipv6      | helper-address      | 2001::1 |     |
| switch(config-if)# | quit      |                     |         |     |
3. VerifyDHCPrelayconfiguration.
| switch# show                                   | dhcpv6-relay        |          |     |             |
| ---------------------------------------------- | ------------------- | -------- | --- | ----------- |
| DHCPv6 Relay                                   | Agent :             | Enabled  |     |             |
| Option 79                                      | :                   | Disabled |     |             |
| switch# show                                   | ipv6 helper-address |          |     |             |
| Interface:                                     | 1/1/1               |          |     |             |
| IPv6 Helper                                    | Address             |          |     | Egress Port |
| ---------------------------------------------- |                     |          |     | ----------- |
| 2001::1                                        |                     |          |     | 1/1/3       |
| Interface:                                     | 1/1/2               |          |     |             |
| IPv6 Helper                                    | Address             |          |     | Egress Port |
| --------------------------------------------   |                     |          |     | ----------- |
| 2001::1                                        |                     |          |     | 1/1/3       |
| DHCPrelay(IPv6)                                | commands            |          |     |             |
dhcpv6-relay
dhcpv6-relay
no dhcpv6-relay
Description
EnablesDHCPv6relaysupport.DHCPv6relayisdisabledbydefault.
DHCPrelayisnotsupportedonthemanagementinterface
ThenoformofthiscommanddisablesDHCPrelaysupport.
Examples
EnablesDHCPv6relaysupport.
| switch(config)# | dhcpv6-relay |     |     |     |
| --------------- | ------------ | --- | --- | --- |
RemovesDHCPv6relaysupport.
| switch(config)# | no dhcpv6-relay |     |     |     |
| --------------- | --------------- | --- | --- | --- |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
74
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-relay    | option 79 |     |
| --------------- | --------- | --- |
| dhcpv6-relay    | option 79 |     |
| no dhcpv6-relay | option 79 |     |
Description
EnablessupportforDHCPrelayoption79.Whenenabled,theDHCPv6relayagentforwardsthelink-layer
addressoftheclient.Thisoptionisdisabledbydefault.
ThenoformofthiscommanddisablessupportforDHCPrelayoption79.
Examples
EnablesDHCPoption79support.
| switch(config)# | dhcpv6-relay | option 79 |
| --------------- | ------------ | --------- |
DisablesDHCPoption79support.
switch(config)#
|     | no dhcpv6-relay | option 79 |
| --- | --------------- | --------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 helper-address
| ipv6 helper-address    | unicast <UNICAST-IPV6-ADDR> |                     |
| ---------------------- | --------------------------- | ------------------- |
| no ipv6 helper-address | unicast                     | <UNICAST-IPV6-ADDR> |
ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-NUM>
no ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>
Description
DefinestheaddressofaremoteDHCPv6serverorDHCPv6relayagent.Uptoeightaddressescanbe
defined.TheDHCPv6agentforwardsDHCPv6clientrequeststoalldefinedservers.
NotsupportedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
DHCP|75

Parameter

Description

<UNICAST-IPV6-ADDR>

<MULTICAST-IPV6-ADDR>

all-dhcp-servers

egress <PORT-NUM>

vrf <VRF-NAME>

Examples

Specifies the unicast helper IP address in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

Specifies the multicast helper IP address in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F.

Specifies all the DHCP server IPv6 addresses for the interface.

Specifies the port number on which DHCPv6 service requests are
relayed to a multicast destination. The egress port must be
different than the one on which the multicast helper address is
configured. Format: member/slot/port.

Specifies the name of the VRF from which the specified protocol
sets its source IP address.

Defining a multicast IPv6 helper address of 2001:DB8::1 on port 1/1/2:

switch(config-if)# ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress 1/1/2

Removing the IP helper address of 2001:DB8::1 on port 1/1/2:

switch(config-if)# no ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress
1/1/2

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

6200

config-if

Administrators or local user group members with execution rights
for this command.

show dhcpv6-relay

show dhcpv6-relay

Description

Shows DHCP relay configuration settings.

Example

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

76

| switch# | show  | dhcpv6-relay |           |     |     |
| ------- | ----- | ------------ | --------- | --- | --- |
| DHCPv6  | Relay | Agent        | : Enabled |     |     |
| Option  | 79    |              | : Enabled |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |
| --------- | --- | -------------- | --- | --------- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| showipv6  | helper-address |     |            |                 |     |
| --------- | -------------- | --- | ---------- | --------------- | --- |
| show ipv6 | helper-address |     | [interface | <INTERFACE-ID>] |     |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
interface <INTERFACE-ID> Specifiesaninterface.Format:member/slot/port.
Examples
| switch#                                        | show   | ipv6    | helper-address |           |             |
| ---------------------------------------------- | ------ | ------- | -------------- | --------- | ----------- |
| Interface:                                     |        | 1/1/1   |                |           |             |
| IPv6                                           | Helper | Address |                |           | Egress Port |
| ---------------------------------------------- |        |         |                |           | ----------- |
| 2001:db8:0:1::                                 |        |         |                |           | -           |
| FF01::1:1000                                   |        |         |                |           | 1/1/2       |
| Interface:                                     |        | 1/1/2   |                |           |             |
| IPv6                                           | Helper | Address |                |           | Egress Port |
| --------------------------------------------   |        |         |                |           | ----------- |
| 2001:db8:0:1::                                 |        |         |                |           | -           |
| switch#                                        | show   | ipv6    | helper-address | interface | 1/1/1       |
| Interface:                                     |        | 1/1/1   |                |           |             |
| IPv6                                           | Helper | Address |                |           | Egress Port |
| ---------------------------------------------- |        |         |                |           | ----------- |
| 2001:db8:0:1::                                 |        |         |                |           | -           |
| FF01::1:1000                                   |        |         |                |           | 1/1/2       |
DHCP|77

| switch#                                        | show ipv6 helper-address | interface | 1/1/1       |
| ---------------------------------------------- | ------------------------ | --------- | ----------- |
| Interface:                                     | 1/1/1                    |           |             |
| IPv6 Helper                                    | Address                  |           | Egress Port |
| ---------------------------------------------- |                          |           | ----------- |
| 2001:db8:0:1::                                 |                          |           | -           |
| FF01::1:1000                                   |                          |           | 1/1/2       |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| DHCP server |     |     |     |
| ----------- | --- | --- | --- |
Overview
Thedynamichostconfigurationprotocol(DHCP)enablesaservertoautomatetheassignmentofIP
addresses,andothernetworkingsettings,tohostcomputers.TheDHCPserverontheswitchprovidesboth
IPv4andIPv6supportandisindependentlyconfigurableoneachVRF.
Keyfeatures
Supportsmultipleaddresspoolsandstaticaddressbindings.
n
SupportsDHCPoptions,enablingtheservertoprovideadditionalinformationaboutthenetworkwhen
n
DHCPclientsrequestanaddress.
SupportsBOOTPtodistributebootimagefilesusinganexternalTFTPserver.
n
VRFaware,meaningthatDHCPclientrequestsreceivedonaninterfaceareprocessedbytheDHCP
n
serverinstanceconfiguredforaVRF.DHCPserverresponsesareforwardedtoclientsontheVRF.
Supportsexternalstorageofleaseinformationonaremotehost.ThisenablestheDHCPserverto
n
restoreleaseinformationafterarebootorafailure.Leaseinformationisstoredinaflatfileonthe
configuredexternaldevice.Itisimportantthattheexternaldeviceprovidepersistentexternalstorageto
allowrestorationofleaseinformation.Ifexternalstorageisnotconfigured,thenafterafailureorreboot,
allexistingleaseinformationislost.
DHCPrelayinteroperation
BothDHCPrelayandDHCPservercanbeconfiguredonthesameVRF.
DHCPsnoopinginteroperation
DHCPsnoopingmaynotbeconfiguredwithDHCPserver.
78
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Configuring a DHCPv4 server on a VRF

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

3. Define an address pool for the VRF with the command pool. This switches to the DHCPv4 server pool

context. Customize pool settings as follows:
a. Define the range of addresses in the pool with the command range.
b. Set the lease time for addresses in the pool with the command lease.
c. Set the domain name for the pool with the command domain-name.
d. Define up to four default routers with the command default-router.
e. Define up to four DNS servers with the command dns-server.
f. Create static bindings for specific addresses in the pool with the command static-bind.
g. Configure custom DHCPv4 options for the pool with the command option.
h. Configure NetBIOS support with the commands netbios-name-server and netbios-node-type.
i. Configure BOOTP options with the command bootp.
j. Exit the DHCPv4 server pool context with the command exit.

4. Enable the DHCP server on the VRF with the command enable.

5. Configure support for persistent external storage of DHCP settings with the command dhcp-server

external-storage.

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

DHCP | 79

| switch(config)# | dhcp-server | vrf primary |     |     |
| --------------- | ----------- | ----------- | --- | --- |
switch(config-dhcp-server)#
pool primary-pool
| switch(config-dhcp-server-pool)# |     | range 10.0.0.1 | 10.0.0.100     |     |
| -------------------------------- | --- | -------------- | -------------- | --- |
| switch(config-dhcp-server-pool)# |     | lease 12:00:00 |                |     |
| switch(config-dhcp-server-pool)# |     | domain-name    | example.org.in |     |
switch(config-dhcp-server-pool)# default-router ip 10.30.30.1 10.30.30.2
| switch(config-dhcp-server-pool)# |     | dns-server | 125.0.0.1 | 125.0.0.2 |
| -------------------------------- | --- | ---------- | --------- | --------- |
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.11 mac 24:be:05:24:75:73
| switch(config-dhcp-server-pool)# |            | option    | 3 ip 10.30.30.3 |     |
| -------------------------------- | ---------- | --------- | --------------- | --- |
| switch(config-dhcp-server-pool)# |            | exit      |                 |     |
| switch(config-dhcp-server)#      |            | enable    |                 |     |
| Configuring                      | the DHCPv6 | server on | a VRF           |     |
Prerequisites
Anenabledlayer3interface.
n
AVRF.
n
n Anexternalstoragedeviceinstalledandconfigured(optional).
Procedure
1. AssigntheDHCPv6servertoaVRFwiththecommanddhcpv6-server vrf.Thisswitchestothe
DHCPv6serverconfigurationcontext.
2. IfyouwanttheDHCPservertobethesoleauthorityforIPaddressesontheVRF,enable
authoritativemodewiththecommandauthoritative.
3. DefineanaddresspoolfortheVRFwiththecommandpool.ThisswitchestotheDHCPv6serverpool
context.Customizepoolsettingsasfollows:
| a. Definetherangeofaddressesinthepoolwiththecommandrange. |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- |
b. SettheDHCPleasetimeforaddressesinthepoolwiththecommandlease.
| c. DefineuptofourDNSserverswiththecommanddns-server. |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- |
d. Createstaticbindingsforspecificaddressesinthepoolwiththecommandstatic-bind.
| e. ConfigurecustomDHCPoptionsforthepoolwiththecommandoption. |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- |
| f. ExittheDHCPserverpoolcontextwiththecommandexit.           |     |     |     |     |
4. EnabletheDHCPv6serverontheVRFwiththecommandenable.
5. ConfiguresupportforpersistentexternalstorageofDHCPsettingswiththecommanddhcv6p-
| server | external-storage. |     |     |     |
| ------ | ----------------- | --- | --- | --- |
6. ViewDHCPv6serverconfigurationsettingswiththecommandshow dhcpv6-server all-vrfs.
Example
Thisexamplecreatesthefollowingconfiguration:
n ConfiguresaDHCPv6serveronVRFprimary-vrf.
n Enablesauthoritativemode.
n Definesthepoolprimary-poolwiththefollowingsettings:
o Addressrange:2001::1to2001::100.
Leasetime:12hours.
o
o DNSservers:2101::14and2101::14.
80
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

o Staticbindingof2001::101forclientID1:0:a0:24:ab:fb:9c.
DHCPcustomoption:22withIPaddress2101::15.
o
n EnablestheDHCPv6server.
| switch(config)#               | dhcpv6-server | vrf primary       |     |
| ----------------------------- | ------------- | ----------------- | --- |
| switch(config-dhcpv6-server)# |               | pool primary-pool |     |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::100 prefix-len 64
| switch(config-dhcpv6-server-pool)# |     | lease 12:00:00 |                   |
| ---------------------------------- | --- | -------------- | ----------------- |
| switch(config-dhcpv6-server-pool)# |     | dns-server     | 2101::13 2101::14 |
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
authorityforthenetworkontheVRF.Therefore,ifaclientrequestsanIPaddressleaseforwhichtheserver
hasnorecord,theserverrespondswithDHCPNAK,indicatingthattheclientmustnolongerusethatIP
address.Iftheserverisnotauthoritative,thenitwillignoreDHCPv4requestsreceivedforunknownleases
fromunknownhosts.
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
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
DHCP|81

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
bootp
bootp <REMOTE-URL>
no bootp <REMOTE-URL>
Description
SetstheBOOTPoptionsthatarereturnedbytheDHCPv4serverforthecurrentpool.BOOTPprovidesa
waytodistributeanIPaddressandbootimagefiletoclientstations.TheDHCPv4serverreturnstheIP
addressandthelocationofthebootimagefile,whichmustbestoredonanexternalTFTPserver.
ThenoformofthiscommanddisablessupportforBOOTP.
| Parameter |     | Description |
| --------- | --- | ----------- |
<REMOTE-URL> SpecifiesthenameandlocationofaBOOTPfileonaTFTPserver
intheformat:
tftp://{<IP> | <HOST>}/<FILE>
n <IP>:SpecifiestheIPaddressoftheTFTPserverhostingthe
fileinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255.Youcanremoveleadingzeros.Forexample,the
address192.169.005.100becomes192.168.5.100.
n <HOST>:Specifiesthefully-qualifieddomainnameoftheTFTP
serverhostingthefile.Range:1to64printableASCII
characters.
n <FILE>:SpecifiesthenameoftheBOOTPfile.Range:1to64
printableASCIIcharacters.
Example
DefinesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)# | dhcp-server | vrf primary |
| --------------- | ----------- | ----------- |
switch(config-dhcp-server)#
pool primary-pool
switch(config-dhcp-server-pool)# bootp tftp://10.0.0.1/mybootfile
DeletesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |
| --------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)# |             | pool primary-pool |
switch(config-dhcp-server-pool)# no bootp tftp://10.0.0.1/mybootfile
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
82
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| clear dhcp-server | leases |     |     |
| ----------------- | ------ | --- | --- |
clear dhcp-server leases [all-vrfs | <IPV4-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv4serverleaseinformation.TheDHCPv4servermustbedisabledbeforeclearinglease
information.
| Parameter |     |     | Description             |
| --------- | --- | --- | ----------------------- |
| all-vrfs  |     |     | ClearsleasesforallVRFs. |
<IPV4-ADDR> vrf <VRF-NAME> ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| vrf <VRF-NAME> |     |     | ClearsleasesforaspecificVRF. |
| -------------- | --- | --- | ---------------------------- |
Examples
ClearingallDHCPv4serverleases.
| switch(config)#             | dhcp-server       | vrf primary |     |
| --------------------------- | ----------------- | ----------- | --- |
| switch(config-dhcp-server)# |                   | disable     |     |
| switch(config-dhcp-server)# |                   | exit        |     |
| switch(config)#             | exit              |             |     |
| switch#                     | clear dhcp-server | leases      |     |
ClearingallDHCPv4serverleasesforVRFprimary-vrf.
| switch(config)#             | dhcp-server       | vrf primary |                 |
| --------------------------- | ----------------- | ----------- | --------------- |
| switch(config-dhcp-server)# |                   | disable     |                 |
| switch(config-dhcp-server)# |                   | exit        |                 |
| switch(config)#             | exit              |             |                 |
| switch#                     | clear dhcp-server | leases      | vrf primary-vrf |
CleartheDHCPv4serverleaseforIPaddress10.10.10.1onVRFprimary-vrf.
| switch(config)#             | dhcp-server       | vrf primary |                            |
| --------------------------- | ----------------- | ----------- | -------------------------- |
| switch(config-dhcp-server)# |                   | disable     |                            |
| switch(config-dhcp-server)# |                   | exit        |                            |
| switch(config)#             | exit              |             |                            |
| switch#                     | clear dhcp-server | leases      | 10.10.10.1 vrf primary-vrf |
CommandHistory
DHCP|83

| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
default-router
| default-router    | <IPV4-ADDR-LIST> |     |     |
| ----------------- | ---------------- | --- | --- |
| no default-router | <IPV4-ADDR-LIST> |     |     |
Description
DefinesuptofourdefaultroutersforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddefaultroutersfromthepool.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesofthedefaultroutersinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.Youcan
removeleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.Separate
addresseswithaspace.AmaximumoffourIPaddressescanbe
defined.
Example
Definestwodefaultrouters,10.0.0.1and10.0.0.10,fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# default-router ip 10.0.0.1 10.0.0.10
Deletesthedefaultrouter10.0.0.1fromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |             |
| -------------------------------- | ----------- | ----------------- | ----------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |             |
| switch(config-dhcp-server-pool)# |             | no default-router | ip 10.0.0.1 |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
84
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Platforms

Command context

Authority

6200

config-dhcp-server-pool

Administrators or local user group members with execution
rights for this command.

dhcp-server external-storage

dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]

Description

Configures the external storage file location for DHCPv4 server lease information. This file provides
persistent storage, enabling DHCPv4 server settings to be restored when the switch is restarted. Lease
information is stored in a flat file on the configured external device.

If external storage is not configured, then after a failure or reboot, all existing lease information is lost.

Lease information is saved to external storage each time the delay timer expires, which by default is every
300 seconds.

Lease information is not restored when issuing the command dhcp-server enable.

The no form of this command removes external storage support for the DHCPv4 server.

Parameter

<VOLUME-NAME>

Description

Specifies the external storage volume name. Range: 1 to 64
printable ASCII characters.

file <LEASE-FILENAME>

Specifies the external storage filename. Range: 1 to 255 printable
ASCII characters.

delay <DELAY>

Example

Specifies the interval in seconds between updates to the external
storage file. Range: 15 to 86400. Default: 300.

Stores the lease file on external storage volume Storage1 in file LeaseFile at an interval of 600 seconds.

switch(config)# dhcp-server external-storage Storage1 file LeaseFile delay 600

Disables storage of the lease file on external storage volume Storage1 in file LeaseFile.

switch(config)# no dhcp-server external-storage Storage1 file LeaseFile delay 600

Command History

Release

10.07 or earlier

Command Information

Modification

--

DHCP | 85

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcp-server    | vrf          |     |
| -------------- | ------------ | --- |
| dhcp-server    | vrf VRF-NAME |     |
| no dhcp-server | vrf VRF-NAME |     |
Description
ConfigurestheDHCPv4servertosupportaVRFandchangestotheconfig-dhcp-servercontextforthat
VRF.
ThenoformofthiscommandremovesDHCPv4serversupportonaVRF.
| Parameter |     | Description |
| --------- | --- | ----------- |
| VRF-NAME  |     | NameofaVRF. |
Example
ConfiguresDHCPv4serversupportonVRFprimary.
| switch(config)# | dhcp-server | vrf primary |
| --------------- | ----------- | ----------- |
RemovesDHCPv4serversupportonVRFprimary.
switch(config)#
|     | no dhcp-server | vrf primary |
| --- | -------------- | ----------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
disable
disable
Description
DisablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
86
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

DisablestheDHCPv4serveronVRFprimary.
| switch(config)#             | dhcp-server | vrf primary |     |
| --------------------------- | ----------- | ----------- | --- |
| switch(config-dhcp-server)# |             | disable     |     |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
dns-server
| dns-server <IPV4-ADDR-LIST> |                  |     |     |
| --------------------------- | ---------------- | --- | --- |
| no dns-server               | <IPV4-ADDR-LIST> |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesoftheDNSserversinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.Separate
addresseswithaspace.
Example
DefinestwoDNSserversfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)#
|     |     | dns-server | 10.0.20.1 |
| --- | --- | ---------- | --------- |
DeletesaDNSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |           |
| -------------------------------- | ----------- | ----------------- | --------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |           |
| switch(config-dhcp-server-pool)# |             | no dns-server     | 10.0.20.1 |
CommandHistory
DHCP|87

| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
domain-name
| domain-name    | <DOMAIN-NAME> |     |     |     |
| -------------- | ------------- | --- | --- | --- |
| no domain-name | <DOMAIN-NAME> |     |     |     |
Description
DefinesadomainnameforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddomainnamefromthepool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<DOMAIN-NAME> Specifiesadomainname.Range:1to255printableASCII
characters.
Example
Definesadomainnamefortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary |              |                |
| -------------------------------- | ----------- | ----------- | ------------ | -------------- |
| switch(config-dhcp-server)#      |             | pool        | primary-pool |                |
| switch(config-dhcp-server-pool)# |             |             | domain-name  | example.org.in |
Deletesadomainnamefromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary |                |                |
| -------------------------------- | ----------- | ----------- | -------------- | -------------- |
| switch(config-dhcp-server)#      |             | pool        | primary-pool   |                |
| switch(config-dhcp-server-pool)# |             |             | no domain-name | example.org.in |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
88
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

enable
enable
Description
EnablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
EnablestheDHCPv4serveronVRFprimary.
| switch(config)#             |     | dhcp-server | vrf    | primary |
| --------------------------- | --- | ----------- | ------ | ------- |
| switch(config-dhcp-server)# |     |             | enable |         |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
http-proxy
| http-proxy    | {<FQDN | | IPV4-ADDR>} | [vrf | <VRF-NAME>]      |
| ------------- | ------ | ------------- | ---- | ---------------- |
| no http-proxy | [<FQDN | | IPV4-ADDR>] |      | [vrf <VRF-NAME>] |
Description
SpecifiesHTTPproxylocationandVRF.
ThenoformofthiscommandremovesaspecifiedHTTPproxylocation.
| Parameter   |     |     |     | Description                               |
| ----------- | --- | --- | --- | ----------------------------------------- |
| <FQDN>      |     |     |     | SpecifiesFQDNforHTTP proxylocation.       |
| <IPV4-ADDR> |     |     |     | SpecifiesIPV4addressforHTTPproxylocation. |
| <VRF-NAME>  |     |     |     | SpecifiesVRF forHTTP proxy.               |
AFQDN orIPV4addressareoptionalinthenoformofthecommand.
Usage
HTTPproxylocationcanbeconfiguredusingtheCLI/RESTinterfaceorauto-configuredthroughthe
n
DHCP serverconnectedtotheswitch.
DHCP|89

TherearethreesourcesforHTTPproxylocation:
n
UserconfiguredHTTPproxyviaCLI orRESTinterface.
o
o DHCP optionsreceivedviamanagement/OOBMport.
o DHCPoptionsreceivedviaVLAN1onsupportedswitchplatforms.
nn OperationalconfigurationforHTTPproxylocationisdeterminedbythesourcewiththehighestpriority.
Sourcepriority:
1. Userconfigured.
2. DHCPoptionsreceivedviamanagement/OOBM port.
3. DHCP optionsreceivedviaVLAN1.
n HTTPproxylocationcanonlybeaFQDNoranIPV4address.
n WhenHTTPproxylocationandVRFareconfigured,theyoverrideanyexistingHTTPproxylocationandVRF.
n IfthiscommandisexecutedwithouttheVRFparameter,thedefaultVRFwillbeused.
PortnumbermayneedtobespecifiedattheendoftheIPaddressforFQDNtoconnectviaHTTPproxy.
n
o Forexample,8088istheTCPportnumber:http-proxy192.168.248.248:8088
Examples
SpecifyingaFQDNforHTTPproxylocationandMGMTVRF:
| switch(config)# | http-proxy | http-proxy.aruba.com | vrf mgmt |
| --------------- | ---------- | -------------------- | -------- |
RemovingHTTPproxylocation
| switch(config)# | no http-proxy |     |     |
| --------------- | ------------- | --- | --- |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lease
| lease {<TIME> | | infinite} |     |     |
| ------------- | ----------- | --- | --- |
no lease
Description
90
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

SetsthelengthoftheDHCPv4leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv4clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv4leasetimetoitsdefaultvalue1hour.
| Parameter |     | Description                                     |
| --------- | --- | ----------------------------------------------- |
| <TIME>    |     | SetstheDHCPv4leasetime.Format:DD:HH:MM.Default: |
01:00:00.
infinite SetstheDHCPv4leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
Example
SetstheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimaryto12hours.
| switch(config)#                  | dhcp-server | vrf primary       |
| -------------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |
| switch(config-dhcp-server-pool)# |             | lease 00:12:00    |
DeletestheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimary.
switch(config)#
|                                  | dhcp-server | vrf primary       |
| -------------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |
| switch(config-dhcp-server-pool)# |             | no lease 00:12:00 |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
netbios-name-server
| netbios-name-server | <IPV4-ADDR-LIST> |     |
| ------------------- | ---------------- | --- |
no netbios-name-server <IPV4-ADDR-LIST>
Description
DefinesuptofourNetBIOSWINSserversforthecurrentDHCPv4serverpool.WINSisusedbyMicrosoft
DHCPclientstomatchhostnameswithIPaddresses.
ThenoformofthiscommandremovesthespecifiedWINSserversfromthepool.
DHCP|91

| Parameter |     | Description |
| --------- | --- | ----------- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesofNetBIOS(WINS)serversinIPv4
format(x.x.x.x),wherexisadecimalnumberfrom0to255.
Separateaddresseswithaspace.AmaximumoffourIP
addressescanbedefined.
Example
DefinestwoWINSserversfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |
| --------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)# |             | pool primary-pool |
switch(config-dhcp-server-pool)# netbios-name-server ip 10.0.20.1 10.0.30.10
DeletesaWINSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |
| --------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)# |             | pool primary-pool |
switch(config-dhcp-server-pool)# no netbios-name-server ip 10.0.20.1
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
netbios-node-type
| netbios-node-type    | <TYPE> |     |
| -------------------- | ------ | --- |
| no netbios-node-type | <TYPE> |     |
Description
DefinestheNetBIOSnodetypeforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovestheNetBIOSnodetypeforthecurrentpool.
| Parameter |     | Description |
| --------- | --- | ----------- |
<TYPE>
SpecifiestheNetBIOSnodetype:broadcast,hybrid,mixed,or
peer-to-peer.
Examples
DefinestheNetBIOSnodetypebroadcastfortheDHCPv4serverpoolprimary-poolonVRFprimary.
92
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| switch(config)# | dhcp-server | vrf primary |     |
| --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
pool primary-pool
| switch(config-dhcp-server-pool)# |     | netbios-node-type | broadcast |
| -------------------------------- | --- | ----------------- | --------- |
DeletestheNetBIOSnodetypebroadcastfromtheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary          |           |
| -------------------------------- | ----------- | -------------------- | --------- |
| switch(config-dhcp-server)#      |             | pool primary-pool    |           |
| switch(config-dhcp-server-pool)# |             | no netbios-node-type | broadcast |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
Description
DefinescustomDHCPv4optionsforthecurrentDHCPv4serverpool.DHCPv4optionsenabletheDHCPv4
servertoprovideadditionalinformationaboutthenetworkwhenDHCPv4clientsrequestanaddress.
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
ip <IPV4-ADDR-LIST>
SpecifiesalistofIPaddressesinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
DHCP|93

| switch(config)# | dhcp-server | vrf primary |     |     |
| --------------- | ----------- | ----------- | --- | --- |
switch(config-dhcp-server)#
pool primary-pool
| switch(config-dhcp-server-pool)# |     |     | option 3 | ip 192.168.1.1 |
| -------------------------------- | --- | --- | -------- | -------------- |
DeletesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary |              |                  |
| -------------------------------- | ----------- | ----------- | ------------ | ---------------- |
| switch(config-dhcp-server)#      |             | pool        | primary-pool |                  |
| switch(config-dhcp-server-pool)# |             |             | no option    | 3 ip 192.168.1.1 |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
pool
pool <POOL-NAME>
no pool <POOL-NAME>
Description
CreatesaDHCPv4serverpoolforthecurrentVRFandswitchestotheconfig-dhcp-server-poolcontext
forit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64pools(IPv4and
IPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv4serverpool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<POOL-NAME> SpecifiestheDHCPv4poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary |              |     |
| --------------------------- | ----------- | ----------- | ------------ | --- |
| switch(config-dhcp-server)# |             | pool        | primary-pool |     |
switch(config-dhcp-server-pool)#
DeletestheDHCPv4serverpoolprimary-poolonVRFprimary.
94
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| switch(config)# |     | dhcp-server | vrf | primary |     |     |     |
| --------------- | --- | ----------- | --- | ------- | --- | --- | --- |
switch(config-dhcp-server)#
|     |     |     | no  | pool primary-pool |     |     |     |
| --- | --- | --- | --- | ----------------- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
range
| range <LOW-IPV4-ADDR>    |     | <HIGH-IPV4-ADDR> |     | [prefix-len | <MASK>] |     |     |
| ------------------------ | --- | ---------------- | --- | ----------- | ------- | --- | --- |
| no range <LOW-IPV4-ADDR> |     | <HIGH-IPV4-ADDR> |     | [prefix-len | <MASK>] |     |     |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv4serverpool.Amaximumof64ranges
aresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<LOW-IPV4-ADDR> SpecifiesthelowestIPaddressinthepoolinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
<HIGH-IPV4-ADDR> SpecifiesthehighestIPaddressinthepoolinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
prefix-len <MASK> SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom0to32.
NOTE:Whenactivegatewayisconfiguredontheinterface
servicedbythepool,youmustspecifyaprefixlengththatmatches
themaskontheIPaddressassignedtotheinterface.Otherwise,
clientstationswillgetaprefixlengthfromactivegatewaythat
maynotbeconsistentwiththeconfiguredrange,andaDHCP
errorwilloccur.Inthefollowingexample,theDHCPrangeprefixis
setto16tomatchthemaskontheIPaddressassignedto
interfaceVLAN2.
|     |     |     |     | switch(config)#         | interface | vlan 2         |              |
| --- | --- | --- | --- | ----------------------- | --------- | -------------- | ------------ |
|     |     |     |     | switch(config-if-vlan)# |           | ip address     | 200.1.1.1/16 |
|     |     |     |     | switch(config-if-vlan)# |           | active-gateway | ip 200.1.1.3 |
mac 00:aa:aa:aa:aa:aa
|     |     |     |     | switch(config-if-vlan)#          |             | exit |                   |
| --- | --- | --- | --- | -------------------------------- | ----------- | ---- | ----------------- |
|     |     |     |     | switch(config)#                  | dhcp-server | vrf  | primary           |
|     |     |     |     | switch(config-dhcp-server)#      |             | pool | primary-pool      |
|     |     |     |     | switch(config-dhcp-server-pool)# |             |      | range 192.168.1.1 |
|     |     |     |     | 192.168.1.100                    | prefix-len  | 16   |                   |
DHCP|95

Examples
Definestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfortheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary |              |
| --------------------------- | ----------- | ----------- | ------------ |
| switch(config-dhcp-server)# |             | pool        | primary-pool |
switch(config-dhcp-server-pool)# 192.168.1.1 192.168.1.100 prefix-len 24
Deletestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfromtheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)# | dhcp-server | vrf primary |     |
| --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
pool primary-pool
switch(config-dhcp-server-pool)# no 192.168.1.1 192.168.1.100 prefix-len 24
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show dhcp-server
| show dhcp-server | [all-vrfs]       |       |             |
| ---------------- | ---------------- | ----- | ----------- |
| show dhcp-server | leases {all-vrfs | | vrf | <VRF-NAME>} |
| show dhcp-server | pool <POOL-NAME> | [vrf  | <VRF-NAME>] |
Description
ShowsconfigurationsettingsfortheDHCPv4server.
| Parameter |     |     | Description                                       |
| --------- | --- | --- | ------------------------------------------------- |
| all-vrfs  |     |     | ShowsDHCPv4serverconfigurationsettingsforallVRFs. |
leases {all-vrfs | vrf <VRF-NAME>} ShowsDHCPv4serverleaseconfigurationsettingsforallVRFsora
specificVRF.
| pool <POOL-NAME> | [vrf <VRF-NAME>] |     |     |
| ---------------- | ---------------- | --- | --- |
ShowsDHCPv4serverpoolconfigurationsettingsforallVRFsora
specificVRF.
Examples
ShowingallDHCPv4serverconfigurationsettings.
96
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

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
| switch# show   | dhcp-server |               | vrf | primary-vrf |     |     |
| -------------- | ----------- | ------------- | --- | ----------- | --- | --- |
| VRF Name       |             | : primary-vrf |     |             |     |     |
| DHCP Server    |             | : disabled    |     |             |     |     |
| Operational    | State       | : disabled    |     |             |     |     |
| Authoritative  | Mode        | : false       |     |             |     |     |
| Pool Name      |             | : test        |     |             |     |     |
| Lease Duration |             | : 00:01:00    |     |             |     |     |
| DHCP dynamic   | IP          | allocation    |     |             |     |     |
--------------------------
| Start-IP-Address |         | End-IP-Address |     |     | Prefix-Length  |     |
| ---------------- | ------- | -------------- | --- | --- | -------------- | --- |
| ---------------- |         | -------------- |     |     | -------------- |     |
| 10.0.0.1         |         | 10.0.0.30      |     |     | *              |     |
| 192.168.1.1      |         | 192.168.1.20   |     |     | 24             |     |
| 192.168.10.30    |         | 192.168.10.60  |     |     | 16             |     |
| DHCP Server      | options |                |     |     |                |     |
-------------------
DHCP|97

| Option-Number |        | Option-Type |               | Option-Value |          |          |          |
| ------------- | ------ | ----------- | ------------- | ------------ | -------- | -------- | -------- |
| ------------- |        | ----------- |               | ------------ |          |          |          |
| 6             |        | ip          |               | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 | 10.0.0.6 |
| 18            |        | ascii       |               | aswed        |          |          |          |
| DHCP          | Server | static      | IP allocation |              |          |          |          |
--------------------------------
| IP-Address |         | Client-Hostname |     | MAC-Address       |     |     |     |
| ---------- | ------- | --------------- | --- | ----------------- | --- | --- | --- |
| ---------- |         | --------------- |     | ----------------- |     |     |     |
| 10.0.0.1   |         | *               |     | aa:bb:cc:11:12:a4 |     |     |     |
| 20.0.0.1   |         | *               |     | 11:22:11:22:aa:dd |     |     |     |
| BOOTP      | Options |                 |     |                   |     |     |     |
---------------
| Boot-File-Name |     | TFTP-Server-Name |     |     | State       |     | TFTP-Server-Address   |
| -------------- | --- | ---------------- | --- | --- | ----------- | --- | --------------------- |
| -------------- |     | ---------------- |     |     | ------      |     | --------------------- |
| boot.txt       |     | *                |     |     | OPERATIONAL |     | 10.0.0.10             |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
static-bind
| static-bind    | {ip | <IPV4-ADDR>}|{ mac |     | <MAC-ADDR>} | [hostname |     | <HOST>] |
| -------------- | --- | ------------------ | --- | ----------- | --------- | --- | ------- |
| no static-bind |     | <IPV4-ADDR-LIST>   |     |             |           |     |         |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaspecificMACaddress.This
causestheDHCPv4servertoonlyassignthespecifiedIPaddresstoaclientstationwiththespecifiedMAC
address.
Thenoformofthiscommandremovesthespecifiedbinding.
| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.TheIPaddressmustbewithinthe
addressrangedefinedforthecurrentpool.
mac <MAC-ADDR>
SpecifiesaclientstationMACaddress(xx:xx:xx:xx:xx:xx),
wherexisahexadecimalnumberfrom0toF.
hostname <HOST> Specifiesthehostnameoftheclientstation.Range:1to255
printableASCIIcharacters
98
| AOS-CX10.09IPServicesGuide| |     | (6200 | SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- | --- | --- |

Examples
Definesastaticaddressfortheserverpoolprimary-poolonVRFprimary.
switch(config)#
|                             | dhcp-server | vrf primary       |
| --------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)# |             | pool primary-pool |
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
Deletesastaticaddressfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |
| --------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)# |             | pool primary-pool |
switch(config-dhcp-server-pool)# no static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| DHCP server | IPv6 commands |     |
| ----------- | ------------- | --- |
authoritative
authoritative
no authoritative
Description
ConfigurestheDHCPv6serverasauthoritativeonthecurrentVRF.Thismeansthattheserveristhesole
authorityforthenetworkontheVRF.Itrespondstoclientsolicitmessageswithadvertisemessageshaving
apriority/preferencevaluesetto255(themaximum),insteadof0(theminimum).Clientsalwayschoose
theDHCPv6serverwiththehighestpriority/preferencevalue.IftwoDHCPv6serverssendanadvertise
messagewiththesamepriority/preferencevalue,thentheclientpicksoneanddiscardstheother.
ThenoformofthiscommanddisablesauthoritativemodeonthecurrentVRF.
Example
ConfiguresDHCPv6serverauthoritativemodeonVRFprimary.
| switch(config)#               | dhcpv6-server | vrf primary   |
| ----------------------------- | ------------- | ------------- |
| switch(config-dhcpv6-server)# |               | authoritative |
RemovesDHCPv6serverauthoritativemodeonVRFprimary.
DHCP|99

| switch(config)# | dhcpv6-server | vrf | primary |
| --------------- | ------------- | --- | ------- |
switch(config-dhcpv6-server)#
no authoritative
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| clear dhcpv6-server | leases |     |     |
| ------------------- | ------ | --- | --- |
clear dhcpv6-server leases [all-vrfs | <IPV6-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv6serverleaseinformation.TheDHCPv6servermustbedisabledbeforeclearinglease
information.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
all-vrfs
ClearsleasesforallVRFs.
<IPV6-ADDR> vrf <VRF-NAME> ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| vrf <VRF-NAME> |     |     | ClearsleasesforaspecificVRF. |
| -------------- | --- | --- | ---------------------------- |
Examples
ClearingallDHCPv6serverleases.
| switch(config)#               | dhcpv6-server       | vrf     | primary |
| ----------------------------- | ------------------- | ------- | ------- |
| switch(config-dhcpv6-server)# |                     | disable |         |
| switch(config-dhcpv6-server)# |                     | exit    |         |
| switch(config)#               | exit                |         |         |
| switch#                       | clear dhcpv6-server | leases  |         |
ClearingallDHCPv6serverleasesforVRFprimary-vrf.
100
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| switch(config)# |     | dhcpv6-server | vrf | primary |     |
| --------------- | --- | ------------- | --- | ------- | --- |
switch(config-dhcpv6-server)#
disable
| switch(config-dhcpv6-server)# |       |               | exit   |                 |     |
| ----------------------------- | ----- | ------------- | ------ | --------------- | --- |
| switch(config)#               |       | exit          |        |                 |     |
| switch#                       | clear | dhcpv6-server | leases | vrf primary-vrf |     |
CleartheDHCPv6serverleaseforIPaddress2001::1onVRFprimary-vrf.
| switch(config)#               |     | dhcpv6-server | vrf     | primary |     |
| ----------------------------- | --- | ------------- | ------- | ------- | --- |
| switch(config-dhcpv6-server)# |     |               | disable |         |     |
| switch(config-dhcpv6-server)# |     |               | exit    |         |     |
| switch(config)#               |     | exit          |         |         |     |
switch#
|     | clear | dhcpv6-server | leases | 2001::1 | vrf primary-vrf |
| --- | ----- | ------------- | ------ | ------- | --------------- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |
| --------- | --- | -------------- | --- | --------- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| dhcv6p-server |     | external-storage |     |     |     |
| ------------- | --- | ---------------- | --- | --- | --- |
dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
Description
ConfigurestheexternalstoragefilelocationforDHCPv6serverleaseinformation.Thisfileprovides
persistentstorage,enablingDHCPv6serversettingstoberestoredwhentheswitchisrestarted.Lease
informationisstoredinaflatfileontheconfiguredexternaldevice.
Ifexternalstorageisnotconfigured,thenafterafailureorreboot,allexistingleaseinformationislost.
Leaseinformationissavedtoexternalstorageeachtimethedelaytimerexpires,whichbydefaultisevery
300seconds.
Leaseinformationisnotrestoredwhenissuingthecommanddhcp-server enable.
ThenoformofthiscommandremovesexternalstoragesupportfortheDHCPv6server.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<VOLUME-NAME>
Specifiestheexternalstoragevolumename.Range:1to64
printableASCIIcharacters.
file <LEASE-FILENAME> Specifiestheexternalstoragefilename.Range:1to255printable
ASCIIcharacters.
DHCP|101

| Parameter |     | Description |
| --------- | --- | ----------- |
delay <DELAY> Specifiestheintervalinsecondsbetweenupdatestotheexternal
storagefile.Range:15to86400.Default:300.
Example
StorestheleasefileonexternalstoragevolumeStorage1infileLeaseFileatanintervalof600seconds.
switch(config)# dhcpv6-server external-storage Storage1 file LeaseFile delay 600
DisablesstorageoftheleasefileonexternalstoragevolumeStorage1infileLeaseFile.
switch(config)# no dhcpv6-server external-storage Storage1 file LeaseFile delay 600
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-server    | vrf          |     |
| ---------------- | ------------ | --- |
| dhcpv6-server    | vrf VRF-NAME |     |
| no dhcpv6-server | vrf VRF-NAME |     |
Description
ConfigurestheDHCPv6servertosupportaVRFandchangestotheconfig-dhcpv6-servercontextforthat
VRF.
ThenoformofthiscommandremovesDHCPv6serversupportonaVRF.
| Parameter |     | Description |
| --------- | --- | ----------- |
| VRF-NAME  |     | NameofaVRF. |
Example
ConfiguresDHCPv6serversupportonVRFprimary.
| switch(config)# | dhcpv6-server | vrf primary |
| --------------- | ------------- | ----------- |
RemovestheDHCPv6serversupportonVRFprimary.
102
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| switch(config)# | no dhcpv6-server | vrf primary |
| --------------- | ---------------- | ----------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
disable
disable
Description
DisablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
DisablestheDHCPv6serveronVRFprimary.
switch(config)#
|                               | dhcpv6-server | vrf primary |
| ----------------------------- | ------------- | ----------- |
| switch(config-dhcpv6-server)# |               | disable     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
dns-server
| dns-server <IPVv6-ADDR-LIST> |                   |     |
| ---------------------------- | ----------------- | --- |
| no dns-server                | <IPVv6-ADDR-LIST> |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
DHCP|103

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<IPVv6-ADDR-LIST> SpecifiestheIPaddressesoftheDNSserversinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDNSserver2001::13fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf primary |              |          |
| ---------------------------------- | ------------- | ----------- | ------------ | -------- |
| switch(config-dhcpv6-server)#      |               | pool        | primary-pool |          |
| switch(config-dhcpv6-server-pool)# |               |             | dns-server   | 2001::13 |
DeletesDNSserver2001::13fromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf primary |               |          |
| ---------------------------------- | ------------- | ----------- | ------------- | -------- |
| switch(config-dhcpv6-server)#      |               | pool        | primary-pool  |          |
| switch(config-dhcpv6-server-pool)# |               |             | no dns-server | 2001::13 |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
enable
enable
Description
EnablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
EnablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcpv6-server | vrf primary |     |     |
| ----------------------------- | ------------- | ----------- | --- | --- |
| switch(config-dhcpv6-server)# |               | enable      |     |     |
CommandHistory
104
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lease
| lease {<TIME> | | infinite} |     |
| ------------- | ----------- | --- |
no lease
Description
SetsthelengthoftheDHCPv6leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv6clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv6leasetimetothedefaultvalue1hour.
| Parameter |     | Description                                     |
| --------- | --- | ----------------------------------------------- |
| <TIME>    |     | SetstheDHCPv6leasetime.Format:DD:HH:MM.Default: |
01:00:00.
infinite
SetstheDHCPv6leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
Example
SetstheleasetimeforDHCPv6serverpoolprimary-poolonVRFprimaryto12hours.
| switch(config)#                    | dhcpv6-server | vrf primary       |
| ---------------------------------- | ------------- | ----------------- |
| switch(config-dhcpv6-server)#      |               | pool primary-pool |
| switch(config-dhcpv6-server-pool)# |               | lease 00:12:00    |
SetstheleasetimeforDHCPserverpoolprimary-poolonVRFprimarytothedefaultvalue.
| switch(config)#                    | dhcpv6-server | vrf primary       |
| ---------------------------------- | ------------- | ----------------- |
| switch(config-dhcpv6-server)#      |               | pool primary-pool |
| switch(config-dhcpv6-server-pool)# |               | no lease 00:12:00 |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
DHCP|105

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
Description
DefinescustomDHCPv6optionsforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovescustomDHCPv6optionsfromthepool.
| Parameter    |     | Description                                |     |
| ------------ | --- | ------------------------------------------ | --- |
| <OPTION-NUM> |     | SpecifiesaDHCPv6optionnumber.Range:2to254. |     |
ascii <ASCII-STR> SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:
1to255ASCIIcharacters.
hex <HEX-STR> Specifiesavaluefortheselectedoptionasahexadecimalstring.
Range:1to255hexadecimalcharacters.
ip <IPV6-ADDR-LIST>
SpecifiesalistofIPaddressesfortheoptioninIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Example
DefinesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf primary |                         |
| ---------------------------------- | ------------- | ----------- | ----------------------- |
| switch(config-dhcpv6-server)#      |               | pool        | primary-pool            |
| switch(config-dhcpv6-server-pool)# |               |             | option 22 ipv6 2001::12 |
DeletesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
switch(config)#
|                                    | dhcpv6-server | vrf primary |                            |
| ---------------------------------- | ------------- | ----------- | -------------------------- |
| switch(config-dhcpv6-server)#      |               | pool        | primary-pool               |
| switch(config-dhcpv6-server-pool)# |               |             | no option 22 ipv6 2001::12 |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
106
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
pool
pool <POOL-NAME>
| no pool <POOL-NAME> |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- |
Description
CreatesaDHCPv6serverpoolforthecurrentVRFandswitchestotheconfig-dhcpv6-server-poolcontext
forit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64pools(IPv4and
IPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv6serverpool.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<POOL-NAME> SpecifiestheDHCPv6poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server |     | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | --- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               |     | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)#
DeletestheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server |     | vrf | primary           |     |
| ----------------------------- | --- | ------------- | --- | --- | ----------------- | --- |
| switch(config-dhcpv6-server)# |     |               |     | no  | pool primary-pool |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
config-dhcpv6-server
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
range
| range <LOW-IPV6-ADDR>    |     |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
| ------------------------ | --- | --- | ---------------- | --- | ----------- | ------- |
| no range <LOW-IPV6-ADDR> |     |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
DHCP|107

Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv6serverpool.Amaximumof64ranges
aresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<LOW-IPV6-ADDR> SpecifiesthelowestIPaddressinthepoolinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
<HIGH-IPV6-ADDR> SpecifiesthehighestIPaddressinthepoolinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
prefix-len <MASK> SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom64to128.
Example
DefinesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server | vrf primary       |     |     |
| ----------------------------- | ------------- | ----------------- | --- | --- |
| switch(config-dhcpv6-server)# |               | pool primary-pool |     |     |
switch(config-dhcpv6-server-pool)#
|     |     | range 2001::1 | 2001::10 prefix-len | 64  |
| --- | --- | ------------- | ------------------- | --- |
DeletesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server | vrf primary       |     |     |
| ----------------------------- | ------------- | ----------------- | --- | --- |
| switch(config-dhcpv6-server)# |               | pool primary-pool |     |     |
switch(config-dhcpv6-server-pool)# no range 2001::1 2001::10 prefix-len 64
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show dhcpv6-server
| show dhcpv6-server | [all-vrfs]       |                   |     |     |
| ------------------ | ---------------- | ----------------- | --- | --- |
| show dhcpv6-server | leases {all-vrfs | | vrf <VRF-NAME>} |     |     |
| show dhcpv6-server | pool <POOL-NAME> | [vrf <VRF-NAME>]  |     |     |
Description
ShowsconfigurationsettingsfortheDHCPv6server.
108
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| Parameter |     |     | Description                                       |     |
| --------- | --- | --- | ------------------------------------------------- | --- |
| all-vrfs  |     |     | ShowsDHCPv6serverconfigurationsettingsforallVRFs. |     |
leases {all-vrfs | vrf <VRF-NAME>} ShowsDHCPv6serverleaseconfigurationsettingsforallVRFsor
aspecificVRF.
| pool <POOL-NAME> | [vrf | <VRF-NAME>] |     |     |
| ---------------- | ---- | ----------- | --- | --- |
ShowsDHCPv6serverpoolconfigurationsettingsforallVRFsora
specificVRF.
Examples
ShowingallDHCPv6serverconfigurationsettings.
| switch# show   | dhcpv6-server |               |     |     |
| -------------- | ------------- | ------------- | --- | --- |
| VRF Name       |               | : default     |     |     |
| DHCPv6 Server  |               | : enabled     |     |     |
| Operational    | State         | : operational |     |     |
| Authoritative  | Mode          | : true        |     |     |
| Pool Name      |               | : test        |     |     |
| Lease Duration |               | : 00:01:00    |     |     |
| DHCPV6 dynamic | IP            | allocation    |     |     |
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
DHCP|109

| 2010::20      |     |         | 2010::40 |     | *   |     |
| ------------- | --- | ------- | -------- | --- | --- | --- |
| DHCPv6 Server |     | options |          |     |     |     |
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
| IPv6-Address |     | Client-Hostname |     |     | State       | Client-Id          |
| ------------ | --- | --------------- | --- | --- | ----------- | ------------------ |
| ------------ |     | --------------- |     |     | ----------- | ---------          |
| 2100::4      |     | *               |     |     | OPERATIONAL | 1:0:a0:24:ab:fb:9c |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority                                            |     |     |
| --------- | -------------- | --- | --- | ---------------------------------------------------- | --- | --- |
| 6200      |                |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
static-bind
110
| AOS-CX10.09IPServicesGuide| |     | (6200 | SwitchSeries) |     |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- | --- |

| static-bind    | ipv6 | <IPVv6-ADDR>      | client-id | <ID> [hostname | <HOST>] |
| -------------- | ---- | ----------------- | --------- | -------------- | ------- |
| no static-bind | ipv6 | <IPVv6-ADDR-LIST> |           |                |         |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaclientidentifierorDUID.This
causestheDHCPv6servertoonlyassignthespecifiedIPaddresstoaclientstationwiththespecifiedclient
identifierorDUID.
Thenoformofthiscommandremovesthespecifiedstaticbindingfromthepool.
| Parameter   |     |     |     | Description                               |     |
| ----------- | --- | --- | --- | ----------------------------------------- | --- |
| <IPV6-ADDR> |     |     |     | SpecifiestheIPaddresstoassigninIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Forexample,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| client-id | <ID>   |     |     | SpecifiestheclientidentifierorDUID. |     |
| --------- | ------ | --- | --- | ----------------------------------- | --- |
| hostname  | <HOST> |     |     |                                     |     |
Specifiesthehostnameoftheclientstation.Range:1to255
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
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
DHCP|111

Chapter 6

DHCP snooping

DHCP snooping

DHCP is a protocol used by DHCP servers in IP networks to dynamically allocate network configuration data
to client devices (DHCP clients). Possible network configuration data includes user IP address, subnet mask,
default gateway IP address, DNS server IP address, and lease duration. The DHCP protocol enables DHCP
clients to be dynamically configured with such network configuration data without any manual setup
process.

DHCP snooping is a security feature that helps avoid problems caused by an unauthorized DHCP server on
the network that provides invalid configuration data to DHCP clients. A user without malicious intent may
cause this problem by unknowingly adding to the network a switch or other device that includes a DHCP
server enabled by default. In some cases, a user with malicious intent adds a DHCP server to the network as
part of their Denial of Service or Man in the Middle attack.

DHCP snooping helps prevent such problems by distinguishing between trusted ports connected to
legitimate DHCP servers and untrusted ports connected to general users. DHCP packets are forwarded
between trusted ports without inspection. DHCP packets received on other switch ports are inspected
before being forwarded. DHCP Packets from untrusted sources are dropped.

In support of the separate IP source lockdown feature, DHCP snooping dynamically collects client
information (VLAN, IPv4 address, MAC address, interface) and adds it to the switch IP binding database.
Alternatively, the IP binding database can be statically updated using the ipv4 source-binding or ipv6
source-binding commands. Statically configured IP binding information supersedes any dynamically
collected information for the same client.

DHCP Snooping and DHCP relay can be configured on the same switch.

When DHCP snooping and DHCP relay are both enabled on a VLAN, the following actions occur:

n Received packet: DHCP snooping processes the DHCP packet before (possibly) handing it to DHCP relay.

n Transmitted packet: DHCP packets sent by DHCP relay are intercepted by DHCP snooping to learn IP

bindings.

For even more rigorous security that is applied in hardware on a packet-by-packet basis, you can use IP source
lockdown feature as described in IP source lockdown.

DHCP server interoperation
DHCP server may not be configured with DHCP snooping.

DHCPv4 snooping conditions for dropping DHCPv4 packets
Applies only to DHCPv4 snooping.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

112

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

1. When a port is configured as a trusted port, all the dynamic IP binding entries learned on that port

will be deleted.

2. When a client is connected on a trusted port, the dynamic IP binding entries will not be learned on the

switch, even though the client gets an IP address.

3.

If DHCPv4 snooping is enabled on two back-to-back access switches, DHCP packets will be dropped,
Since by default option 82 is enabled on DHCPv4 snooping and the default policy is drop. The second
switch with DHCPv4 snooping enabled drops the packets. In this scenario the user should enable
DHCPv4 snooping option 82 on one switch, or else you can disable on both.

DHCPv4 snooping commands

clear dhcpv4-snooping binding
clear dhcpv4-snooping binding {all | ip <IPV4-ADDR> vlan <VLAN-ID> | port <PORT-NUM> | vlan
<VLAN-ID>}

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

Specifies the port number for which all DHCPv4 binding
information is to be cleared.

Specifies the VLAN for which all DHCPv4 binding information is to
be cleared.

DHCP snooping | 113

Examples
ClearingallDHCPv4bindinginformationforIPaddress192.168.2.4andVLAN5:
switch(config)#
|     | clear dhcpv4-snooping | binding | ip 192.168.2.4 | vlan 5 |
| --- | --------------------- | ------- | -------------- | ------ |
ClearingallDHCPv4bindinginformationforport1/1/1:
| switch(config)# | clear dhcpv4-snooping | binding | port 1/1/1 |     |
| --------------- | --------------------- | ------- | ---------- | --- |
ClearingallDHCPv4bindinginformationforVLAN10:
| switch(config)# | clear dhcpv4-snooping | binding | vlan 10 |     |
| --------------- | --------------------- | ------- | ------- | --- |
ClearingallDHCPv4bindinginformation:
| switch(config)# | clear dhcpv4-snooping | binding | all |     |
| --------------- | --------------------- | ------- | --- | --- |
CommandHistory
| Release    |     | Modification                                    |     |     |
| ---------- | --- | ----------------------------------------------- | --- | --- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |     |     |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| clear dhcpv4-snooping |            | statistics |     |     |
| --------------------- | ---------- | ---------- | --- | --- |
| clear dhcpv4-snooping | statistics |            |     |     |
Description
ClearsallDHCPv4snoopingstatistics.
Examples
ClearallDHCPv4snoopingstatistics:
| switch# | clear dhcpv4-snooping | statistics |     |     |
| ------- | --------------------- | ---------- | --- | --- |
CommandHistory
114
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| Release    |     | Modification                                    |
| ---------- | --- | ----------------------------------------------- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
| switch(config)# | dhcpv4-snooping |     |
| --------------- | --------------- | --- |
DisablingDHCPv4snooping:
| switch(config)# | no dhcpv4-snooping |     |
| --------------- | ------------------ | --- |
CommandHistory
| Release    |     | Modification                                    |
| ---------- | --- | ----------------------------------------------- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
DHCPsnooping|115

| dhcpv4-snooping | (in config-vlan | context) |
| --------------- | --------------- | -------- |
dhcpv4-snooping
no dhcpv4-snooping
Description
EnablesDHCPv4snoopingforthespecifiedVLANintheconfig-vlancontext.DHCPv4snoopingisdisabled
bydefaultforallVLANs.
ThenoformofthecommanddisablesDHCPv4snoopingonthespecifiedVLAN,flushingalltheIPbindings
learnedforthisVLANsinceDHCPv4snoopingwasenabledforthisVLAN.
Examples
EnablingDHCPv4snoopingonVLAN100:
| switch(config)# | vlan 100 |     |
| --------------- | -------- | --- |
switch(config-vlan-100)#
dhcpv4-snooping
switch(config-vlan-100)# exit
switch(config)#
DisablingDHCPv4snoopingonVLAN100:
| switch(config)#          | vlan 100           |     |
| ------------------------ | ------------------ | --- |
| switch(config-vlan-100)# | no dhcpv4-snooping |     |
switch(config-vlan-100)# exit
switch(config)#
CommandHistory
| Release    |     | Modification                                    |
| ---------- | --- | ----------------------------------------------- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
dhcpv4-snooping allow-overwrite-binding
| dhcpv4-snooping    | allow-overwrite-binding |     |
| ------------------ | ----------------------- | --- |
| no dhcpv4-snooping | allow-overwrite-binding |     |
Description
AllowsbindingtobeoverwrittenforthesameIPaddress.Whenenabled,andaDHCPserveroffersahostan
IPaddressthatisalreadyboundtoanexistinghostinthebindingtable,theexistingbindingisoverwritten
116
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

forthenewhostifthenewhostissuccessfullyabletoacquirethesameIPaddress.Thisoverwritingis
disabledbydefault,causingtheDHCPserverofferstobedropped.
ThenoformofthecommanddisablesDHCPv4snoopingoverwritebinding.
Examples
EnablingDHCPv4snoopingoverwritebinding:
| switch(config)# | dhcpv4-snooping | allow-overwrite-binding |     |
| --------------- | --------------- | ----------------------- | --- |
DisablingDHCPv4snoopingoverwritebinding:
| switch(config)# | no dhcpv4-snooping | allow-overwrite-binding |     |
| --------------- | ------------------ | ----------------------- | --- |
CommandHistory
| Release    |     | Modification                                    |     |
| ---------- | --- | ----------------------------------------------- | --- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
config
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
dhcpv4-snooping authorized-server
| dhcpv4-snooping | authorized-server | <IPV4-ADDR> | [vrf <VRF-NAME>] |
| --------------- | ----------------- | ----------- | ---------------- |
no dhcpv4-snooping authorized-server <IPV4-ADDR> [vrf <VRF-NAME>]
Description
Addsanauthorized(trusted)DHCPservertoalistofauthorizedserversforusebyDHCPv4snooping.This
commandcanbeissuedmultipletimes,addingamaximumof20authorizedserversperVRF.Bydefault,
withanemptylistofauthorizedservers,allDHCPserversareconsideredtobetrustedforDHCPv4
snoopingpurposes.
ThemgmtVRFcannotbeusedwiththiscommand.
ThenoformofthiscommanddeletesthespecifiedDHCPserverfromtheauthorizedlist.
| Parameter   |     | Description                                      |     |
| ----------- | --- | ------------------------------------------------ | --- |
| <IPV4-ADDR> |     | SpecifiestheIPv4addressofthetrustedDHCPv4server. |     |
vrf <VRF-NAME>
SpecifiestheVRFname.Thenamemustbedefault.
DHCPsnooping|117

Usage

For authorized server lookup, the VRF is derived from the Switch Virtual Interface (SVI) configured for the
incoming VLAN. If the SVI is not configured, the default VRF is assumed.

Examples

Adding DHCP servers 192.168.2.2, 192.168.2.3, and 192.168.2.10 to the authorized server list:

switch(config)# dhcpv4-snooping authorized-server 192.168.2.2
switch(config)# dhcpv4-snooping authorized-server 192.168.2.3 vrf default
switch(config)# dhcpv4-snooping authorized-server 192.168.2.10 vrf default

Removing DHCP server 192.168.2.3 from the authorized server list:

switch(config)# no dhcpv4-snooping authorized-server 192.168.2.3 vrf default

Command History

Release

10.09.1000

10.09

10.07 or earlier

Command Information

Modification

Command introduced for the 8360 Switch Series.

Command introduced for the 6000 and 6100 Switch Series.

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution rights
for this command.

dhcpv4-snooping external-storage
dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
no dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>

Description

Configures external storage to be used for backing up IP bindings (used by DHCPv4 snooping) to a file.
When configured, the switch stores all the IP bindings in an external storage file so that they are retained
after the switch restarts. When the switch restarts, it reads the IP bindings from the configured external
storage file to populate its local cache.

When both external storage and flash storage are configured to store DHCP snooping IP bindings, the external

storage takes priority, and is used exclusively until it becomes unconfigured, at which time flash storage (if

configured) is used. Later, if external storage is configured again, flash storage stops and external storage

resumes.

The no form of this command disables the saving of IP bindings in an external storage file.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

118

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

Disabling external storage when flash storage is also configured (note the message indicating that flash
storage will be used):

switch(config)# no dhcpv4-snooping external-storage volume dhcp_snoop
DHCPv4-Snooping will use flash storage to store IP Binding database
switch(config)#

Command History

Release

10.09.1000

10.09

10.08

10.07 or earlier

Modification

Command introduced for the 8360 Switch Series.

Command introduced for the 6000 and 6100 Switch Series.

Updated example with flash storage information.

Command Information

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution rights
for this command.

dhcpv4-snooping flash-storage
dhcpv4-snooping flash-storage [delay <DELAY>]
no dhcpv4-snooping flash-storage [delay <DELAY>]

Description

DHCP snooping | 119

ConfiguresswitchflashstoragetobeusedforbackingupclientIPbindings(usedbyDHCPv4snooping).
Whenflashstorageisconfigured(andexternalstorageisnotalreadyconfiguredforthispurpose),the
switchstorestheIPbindingsinswitchflashstorage.Whentheswitchrestarts,itreadstheIPbindingsfrom
theswitchflashstoragetopopulateitslocalcache.
WritingtheIPbindingstoflashstorageonlyoccursaftertheconfigureddelayandiftherehasbeenachange
inclientIPbindings.WritingisskippedwhenclientIPbindingshavenotchangedsincethepreviouswrite.
| Omittingdelay | <DELAY> setsthedefaultdelayof900seconds. |     |     |     |
| ------------- | ---------------------------------------- | --- | --- | --- |
Toreduceswitchflashagingitisrecommendedthatyouuseexternalstorage(commanddhcpv4-snooping
external-storage)tobackupDHCPsnoopingIPbindings.Alternatively,considerconfiguringflashstoragewitha
substantialdelaybetweenwrites.
WhenbothexternalstorageandflashstorageareconfiguredtostoreDHCPsnoopingIPbindings,theexternal
storagetakespriority,andisusedexclusivelyuntilitbecomesunconfigured,atwhichtimeflashstorage(if
configured)isused.Later,ifexternalstorageisconfiguredagain,flashstoragestopsandexternalstorage
resumes.
ThenoformofthiscommanddisablesthesavingofIPbindingsinflashstorage.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
delay <DELAY> Specifiesthedelayinsecondsbetweenwrites(whennecessary)to
theflashstorage,Default:900.Range:300to86400.
Examples
ConfiguringswitchflashstorageforDHCPsnoopingIPbindingstoragewithawritedelayof1200seconds:
| switch(config)# | dhcpv4-snooping |     | flash-storage | delay 1200 |
| --------------- | --------------- | --- | ------------- | ---------- |
Warning: Using flash storage reduces switch lifetime. It is recommended to use an
external-storage.
| Do you want | to continue | (y/n)? | y   |     |
| ----------- | ----------- | ------ | --- | --- |
switch(config)#
UnconfiguringusageofswitchflashstorageforIPbindings:
| switch(config)# | no dhcpv4-snooping |     | flash-storage |     |
| --------------- | ------------------ | --- | ------------- | --- |
CommandHistory
| Release    |     |     | Modification                                    |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.08
CommandInformation
120
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |              | max-bindings |                |     |     |
| ------------------ | ------------ | ------------ | -------------- | --- | --- |
| dhcpv4-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |
| no dhcpv4-snooping |              | max-bindings | <MAX-BINDINGS> |     |     |
Description
SetsthemaximumnumberofDHCPbindingsallowedontheselectedinterface.Forallinterfacesonwhich
thiscommandisnotrun,thedefaultmaxbindingisthemaximumvalueoftherange.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofDHCPbindings.Range0to
1024.
Examples
SettheDHCPmaxbindingsto256oninterface1/1/1:
| switch(config)#    |     | interface       | 1/1/1 |              |     |
| ------------------ | --- | --------------- | ----- | ------------ | --- |
| switch(config-if)# |     | dhcpv4-snooping |       | max-bindings | 256 |
| switch(config-if)# |     | exit            |       |              |     |
switch(config)#
RevertDHCPmaxbindingstoitsdefaultoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1           |              |     |
| ------------------ | --- | --------- | --------------- | ------------ | --- |
| switch(config-if)# |     | no        | dhcpv4-snooping | max-bindings | 256 |
| switch(config-if)# |     | exit      |                 |              |     |
switch(config)#
CommandHistory
| Release    |     |     |     | Modification                                    |     |
| ---------- | --- | --- | --- | ----------------------------------------------- | --- |
| 10.09.1000 |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09      |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
DHCPsnooping|121

| dhcpv4-snooping |     | option | 82  |     |     |
| --------------- | --- | ------ | --- | --- | --- |
dhcpv4-snooping option 82 [remote-id {mac | subnet-ip | mgmt-ip}]
|     |     | [untrusted-policy |     | {drop | keep | | replace}] |
| --- | --- | ----------------- | --- | ------------ | ----------- |
no dhcpv4-snooping option 82 [remote-id {mac | subnet-ip | mgmt-ip}]
|     |     | [untrusted-policy |     | {drop | keep | | replace}] |
| --- | --- | ----------------- | --- | ------------ | ----------- |
Description
Configurestheadditionofoption82DHCPrelayinformationtoDHCPclientpacketsthatarebeing
forwardedontrustedports.DHCPrelayisenabledbydefault.
Intheswitchdefaultstateandwhenthiscommandisenteredwithoutparameters(dhcpv4-snooping
option 82),thisdefaultconfigurationisused:
| dhcpv4-snooping | option | 82 remote-id | mac untrusted-policy |     | drop |
| --------------- | ------ | ------------ | -------------------- | --- | ---- |
Whenremote-idisomitted,itsdefault(mac)isused.Whenuntrusted-policyisomitted,itsdefault(drop)is
used.
ThenoformofthiscommanddisablesDHCPv4snoopingoption82.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
remote-id SpecifieswhataddresstouseastheremoteIDforthereplace
optionofuntrusted-policy.Specifyoneoftheseaddresstypes:
| mac       |     |     | Thedefault.UsestheswitchMACaddressastheremoteID. |     |     |
| --------- | --- | --- | ------------------------------------------------ | --- | --- |
| subnet-ip |     |     | UsestheIPaddressoftheclientVLANastheremoteID.    |     |     |
untrusted-policy SpecifieswhatactiontotakeforDHCPpackets(withoption82)
thatarereceivedonuntrustedports.Specifyoneoftheseactions:
| drop |     |     | Thedefault.DropDHCPpackets(withoption82)without |     |     |
| ---- | --- | --- | ----------------------------------------------- | --- | --- |
forwardingthem.
| keep    |     |     | ForwardDHCPpackets(withoption82).                 |     |     |
| ------- | --- | --- | ------------------------------------------------- | --- | --- |
| replace |     |     | Replacetheoption82informationintheDHCPpacketswith |     |     |
whateverissetforremote-id(oneof:mac,subnet-ip,ormgmt-
ip)andforwardthepackets.
Examples
ConfiguringDHCPv4snoopingoption82withthekeepaction:
| switch(config)# | dhcpv4-snooping |     | option | 82 untrusted-policy | keep |
| --------------- | --------------- | --- | ------ | ------------------- | ---- |
ConfiguringDHCPv4snoopingoption82withmgmt-ipastheremote-idandthereplaceaction:
switch(config)# dhcpv4-snooping option 82 remote-id mgmt-ip untrusted-policy replace
DisablingDHCPv4snoopingoption82:
switch(config)# no dhcpv4-snooping option 82 untrusted-policy keep
CommandHistory
122
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |     |     |
| --------------------------- | ----- | ------------- | --- | --- | --- |

| Release    |     |     | Modification                                    |
| ---------- | --- | --- | ----------------------------------------------- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |       | trust |     |
| ------------------ | ----- | ----- | --- |
| dhcpv4-snooping    | trust |       |     |
| no dhcpv4-snooping |       | trust |     |
Description
EnablesDHCPv4snoopingtrustontheselectedport.Onlyserverpacketsreceivedontrustedportsare
forwarded.Alltheportsareuntrustedbydefault.
ThenoformofthecommanddisablesDHCPv4snoopingtrustontheselectedport.
Examples
EnablingDHCPv4snoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface 2/2/1 |       |
| ------------------ | --- | --------------- | ----- |
| switch(config-if)# |     | dhcpv4-snooping | trust |
| switch(config-if)# |     | exit            |       |
switch(config)#
DisablingDHCPv4snoopingtrustoninterface2/2/1:
switch(config)#
|                    |     | interface 2/2/1    |       |
| ------------------ | --- | ------------------ | ----- |
| switch(config-if)# |     | no dhcpv4-snooping | trust |
| switch(config-if)# |     | exit               |       |
switch(config)#
CommandHistory
| Release    |     |     | Modification                                    |
| ---------- | --- | --- | ----------------------------------------------- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
DHCPsnooping|123

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    | verify     | mac |
| ------------------ | ---------- | --- |
| dhcpv4-snooping    | verify mac |     |
| no dhcpv4-snooping | verify mac |     |
Description
ThiscommandenablesverificationofthehardwareaddressfieldinDHCPclientpackets.Whenenabled,the
DHCPclienthardwareaddressfieldandthesourceMACaddressmustbethesameforpacketsreceivedon
untrustedportsorelsethepacketisdropped.ThisDHCPsnoopingMACverificationisenabledbydefault.
ThenoformofthecommanddisablesDHCPv4snoopingMACverification.
Examples
EnablingDHCPv4snoopingMACverification:
| switch(config)# | dhcpv4-snooping | verify mac |
| --------------- | --------------- | ---------- |
DisablingDHCPv4snoopingMACverification:
| switch(config)# | no dhcpv4-snooping | verify mac |
| --------------- | ------------------ | ---------- |
CommandHistory
| Release    |     | Modification                                    |
| ---------- | --- | ----------------------------------------------- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show dhcpv4-snooping
show dhcpv4-snooping
Description
ShowstheDHCPv4snoopingconfiguration.
Examples
124
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

ShowingtheDHCPv4snoopingconfiguration:
| switch(config)# |                | show           | dhcpv4-snooping |              |            |                    |            |         |                 |
| --------------- | -------------- | -------------- | --------------- | ------------ | ---------- | ------------------ | ---------- | ------- | --------------- |
| DHCPv4-Snooping |                | Information    |                 |              |            |                    |            |         |                 |
| DHCPv4-Snooping |                |                |                 | : Yes        |            |                    | Verify MAC | Address | : Yes           |
| Allow Overwrite |                | Binding        |                 | : Yes        |            |                    | Enabled    | VLANs   | : 1,5,7,100-110 |
| Option 82       | Configurations |                |                 |              |            |                    |            |         |                 |
| Untrusted       | Policy         |                | :               | replace      |            |                    | Insertion  |         | : Yes           |
| Option          | 82 Remote-id   |                | :               | mac          |            |                    |            |         |                 |
| External        | Storage        | Information    |                 |              |            |                    |            |         |                 |
| Volume          | Name           |                | :               | ipbinding    |            |                    |            |         |                 |
| File Name       |                |                | :               | ipv4Bindings |            |                    |            |         |                 |
| Inactive        | Since          |                | :               | 01:23:20     | 09/10/2021 |                    |            |         |                 |
| Error           |                |                | :               | File Write   |            | Failure            |            |         |                 |
| Flash Storage   |                | Information    |                 |              |            |                    |            |         |                 |
| File Write      | Delay          | :              | 300             | seconds      |            |                    |            |         |                 |
| Active Storage  |                | : External     |                 |              |            |                    |            |         |                 |
| Authorized      | Server         | Configurations |                 |              |            |                    |            |         |                 |
| VRF             |                |                |                 |              |            | Authorized         | Servers    |         |                 |
| ------------    |                |                |                 |              |            | ------------------ |            |         |                 |
| default         |                |                |                 |              |            | 1.1.10.3           |            |         |                 |
| default         |                |                |                 |              |            | 10.10.10.1         |            |         |                 |
| default         |                |                |                 |              |            | 10.10.10.56        |            |         |                 |
| default         |                |                |                 |              |            | 200.10.10.3        |            |         |                 |
| green           |                |                |                 |              |            | 1.1.10.3           |            |         |                 |
| green           |                |                |                 |              |            | 1.10.10.3          |            |         |                 |
| green           |                |                |                 |              |            | 10.10.100.3        |            |         |                 |
| red             |                |                |                 |              |            | 192.168.122.53     |            |         |                 |
| red             |                |                |                 |              |            | 192.168.122.121    |            |         |                 |
Port Information
|          |       | Max      |      | Static   |     | Dynamic  |     |     |     |
| -------- | ----- | -------- | ---- | -------- | --- | -------- | --- | --- | --- |
| Port     | Trust | Bindings |      | Bindings |     | Bindings |     |     |     |
| -------- | ----- | -------- |      | -------- |     | -------- |     |     |     |
| 1/1/2    | Yes   |          | 5000 | 50       |     | 0        |     |     |     |
| 1/1/3    | Yes   |          | 8192 | 0        |     | 0        |     |     |     |
| 1/1/5    | Yes   |          | 8192 | 0        |     | 22       |     |     |     |
| 1/1/16   | No    |          | 100  | 0        |     | 0        |     |     |     |
| 10/10/10 | No    |          | 8100 | 320      |     | 200      |     |     |     |
| lag120   | No    |          | 512  | 0        |     | 0        |     |     |     |
CommandHistory
| Release    |     |     |     |     | Modification                                    |     |     |     |     |
| ---------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
| 10.09.1000 |     |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |     |     |
| 10.09      |     |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |     |
DHCPsnooping|125

| Release |     | Modification                               |     |
| ------- | --- | ------------------------------------------ | --- |
| 10.08   |     | Updatedexamplewithflashstorageinformation. |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv4-snooping | binding |     |     |
| -------------------- | ------- | --- | --- |
| show dhcpv4-snooping | binding |     |     |
Description
ShowstheDHCPv4snoopingbindingconfiguration.
Examples
ShowingtheDHCPv4snoopingbindingconfiguration:
| switch(config)#   | show dhcpv4-snooping | binding        |           |
| ----------------- | -------------------- | -------------- | --------- |
| MacAddress        | IP                   | VLAN Interface | Time-Left |
| ----------------- | ---------------      | ---- --------- | --------- |
| aa:b1:c1:dd:ee:ff | 10.2.3.4             | 1 1/1/2        | 582       |
| aa:b2:c2:dd:ee:ff | 10.2.3.5             | 1 1/1/2        | 584       |
CommandHistory
| Release    |     | Modification                                    |     |
| ---------- | --- | ----------------------------------------------- | --- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv4-snooping | statistics |     |     |
| -------------------- | ---------- | --- | --- |
| show dhcpv4-snooping | statistics |     |     |
126
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Description
ShowstheDHCPv4snoopingstatistics.
Examples
ShowingtheDHCPv4snoopingstatistics:
| switch(config)# |     | show    | dhcpv4-snooping               |         |              | statistics |       |           |
| --------------- | --- | ------- | ----------------------------- | ------- | ------------ | ---------- | ----- | --------- |
| Packet-Type     |     | Action  | Reason                        |         |              |            |       | Count     |
| -----------     |     | ------- | ----------------------------- |         |              |            |       | --------- |
| server          |     | forward | from                          | trusted | port         |            |       | 5425      |
| client          |     | forward | to trusted                    |         | port         |            |       | 3895      |
| server          |     | drop    | received                      |         | on untrusted |            | port  | 117       |
| server          |     | drop    | unauthorized                  |         | server       |            |       | 214       |
| client          |     | drop    | destination                   |         | on           | untrusted  | port  | 78        |
| client          |     | drop    | untrusted                     |         | option       | 82         | field | 85        |
| client          |     | drop    | bad                           | DHCP    | release      | request    |       | 0         |
| client          |     | drop    | failed                        | verify  |              | MAC check  |       | 5         |
| client          |     | drop    | failed                        | on      | max-binding  |            | limit | 15        |
CommandHistory
| Release    |     |     |     |     | Modification                                    |     |     |     |
| ---------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
| 10.09.1000 |     |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |     |
| 10.09      |     |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |
10.07orearlier
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| DHCPv6                | snooping |     | commands |         |     |     |     |     |
| --------------------- | -------- | --- | -------- | ------- | --- | --- | --- | --- |
| clear dhcpv6-snooping |          |     |          | binding |     |     |     |     |
clear dhcpv6-snooping binding {all | ip <IPV6-ADDR> vlan <VLAN-ID> | interface <IFNAME> |
vlan <VLAN-ID>}
Description
ClearsDHCPv6snoopingbindingentries.
| Parameter |     |     |     |     | Description                                            |     |     |     |
| --------- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
| all       |     |     |     |     | SpecifiesthatallDHCPv6bindinginformationistobecleared. |     |     |     |
DHCPsnooping|127

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
ip <IPV6-ADDR> vlan <VLAN-ID> SpecifiestheIPv6addressandVLANforwhichallDHCPv6binding
informationistobecleared.
interface <IFNAME> SpecifiestheinterfaceforwhichallDHCPv6bindinginformationis
tobecleared.
vlan <VLAN-ID>
SpecifiestheVLANforwhichallDHCPv6bindinginformationisto
becleared.Range:1to4094.
Examples
ClearingallDHCPv6bindinginformationfor5000::1vlan1:
| switch(config)# | clear dhcpv6-snooping | binding | ip 5000::1 vlan | 1   |
| --------------- | --------------------- | ------- | --------------- | --- |
ClearingallDHCPv6bindinginformationforinterface1/1/10:
| switch(config)# | clear dhcpv6-snooping | binding | interface 1/1/10 |     |
| --------------- | --------------------- | ------- | ---------------- | --- |
ClearingallDHCPv6bindinginformationforVLAN10:
| switch(config)# | clear dhcpv6-snooping | binding | vlan 10 |     |
| --------------- | --------------------- | ------- | ------- | --- |
ClearingallDHCPv6bindinginformation:
| switch(config)# | clear dhcpv6-snooping | binding | all |     |
| --------------- | --------------------- | ------- | --- | --- |
CommandHistory
| Release    |     | Modification                                    |     |     |
| ---------- | --- | ----------------------------------------------- | --- | --- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |     |     |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| clear dhcpv6-snooping | statistics |     |     |     |
| --------------------- | ---------- | --- | --- | --- |
clear dhcpv6-snooping statistics
Description
128
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

ClearsallDHCPv6snoopingstatistics.
Examples
ClearallDHCPv6snoopingstatistics:
| switch# | clear dhcpv6-snooping | statistics |
| ------- | --------------------- | ---------- |
CommandHistory
| Release    |     | Modification                                    |
| ---------- | --- | ----------------------------------------------- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
dhcpv6-snooping
dhcpv6-snooping
no dhcpv6-snooping
Description
EnablesDHCPv6snooping.DHCPv6snoopingisdisabledbydefault.DHCPv6snoopingisnotsupportedon
themanagementinterface.
ThenoformofthecommanddisablesDHCPv6snooping,flushingalltheIPbindingslearnedsinceDHCPv6
snoopingwasenabled.
Examples
EnablingDHCPv6snooping:
| switch(config)# | dhcpv6-snooping |     |
| --------------- | --------------- | --- |
DisablingDHCPv6snooping:
| switch(config)# | no dhcpv6-snooping |     |
| --------------- | ------------------ | --- |
CommandHistory
DHCPsnooping|129

| Release    |     | Modification                                    |
| ---------- | --- | ----------------------------------------------- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-snooping | (in config-vlan | context) |
| --------------- | --------------- | -------- |
dhcpv6-snooping
no dhcpv6-snooping
Description
EnablesDHCPv6snoopingintheconfig-vlancontext.DHCPv6snoopingisdisabledbydefaultforall
VLANs.
ThenoformofthecommanddisablesDHCPv6snoopingonthespecifiedVLAN,flushingalltheIPv6
bindingslearnedforthisVLANsinceDHCPv6snoopingwasenabledforthisVLAN.
Examples
EnablingDHCPv6snoopingonVLAN100:
| switch(config)# | vlan 100 |     |
| --------------- | -------- | --- |
switch(config-vlan-100)# dhcpv6-snooping
switch(config-vlan-100)# exit
switch(config)#
DisablingDHCPv6snoopingonVLAN100:
| switch(config)#          | vlan 100           |     |
| ------------------------ | ------------------ | --- |
| switch(config-vlan-100)# | no dhcpv6-snooping |     |
switch(config-vlan-100)# exit
switch(config)#
CommandHistory
| Release    |     | Modification                                    |
| ---------- | --- | ----------------------------------------------- |
| 10.09.1000 |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
CommandInformation
130
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

Platforms

Command context

Authority

6200

config-vlan

Administrators or local user group members with execution rights
for this command.

dhcpv6-snooping authorized-server
dhcpv6-snooping authorized-server <IPV6-ADDR> [vrf <VRF-NAME>]
no dhcpv6-snooping authorized-server <IPV6-ADDR> [vrf <VRF-NAME>]

Description

Adds an authorized (trusted) DHCPv6 server to a list of authorized servers for use by DHCPv6 snooping.
This command can be issued multiple times, adding a maximum of 20 authorized servers per VRF. By
default, with an empty list of authorized servers, all DHCPv6 servers are considered to be trusted for
DHCPv6 snooping purposes.

The mgmt VRF cannot be used with this command.

Configure the link local IPv6 address instead of global IPv6 address of the DHCPv6 server as the authorized-

server. For example:

switch(config)# dhcpv6-snooping authorized-server fe80::2ca4:fa40:d4cd:bc2f

The no form of this command deletes the specified DHCPv6 server from the authorized list.

Parameter

<IPV6-ADDR>

vrf <VRF-NAME>

Usage

Description

Specifies the IPv6 address of the trusted DHCPv6 server.

Specifies the VRF name. The name must be default.

For authorized server lookup, the VRF is derived from the Switch Virtual Interface (SVI) configured for the
incoming VLAN. If the SVI is not configured, the default VRF is assumed.

Examples

Adding DHCP servers ABCD:5ACD::2000, and ABCD:5ACD::2010 to the authorized server list:

switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2010 vrf default

Removing DHCP server ABCD:5ACD::2000 from the authorized server list:

switch(config)# no dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default

Command History

DHCP snooping | 131

Release

10.09.1000

10.09

10.07 or earlier

Modification

Command introduced for the 8360 Switch Series.

Command introduced for the 6000 and 6100 Switch Series.

Command Information

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution rights
for this command.

dhcpv6-snooping external-storage
dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
no dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>

Description

Configures external storage to be used for backing up IPv6 bindings (used by DHCPv6 snooping) to a file.
When configured, the switch stores all the IP bindings in an external storage file so that they are retained
after the switch restarts. When the switch restarts, it reads the IPv6 bindings from the configured external
storage file to populate its local cache.

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

switch(config)# dhcpv6-snooping external-storage volume dhcp_snoop file ipv6Bindings

Disabling external storage:

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

132

switch(config)# no dhcpv6-snooping external-storage volume dhcp_snoop

Disabling external storage when flash storage is also configured (note the message indicating that flash
storage will be used):

switch(config)# no dhcpv6-snooping external-storage volume dhcp_snoop
DHCPv6-Snooping will use flash storage to store IP Binding database
switch(config)#

Command History

Release

10.09

10.08

10.07 or earlier

Command Information

Modification

Command introduced for the 6000 and 6100 Switch Series.

Updated example with flash storage information.

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution rights
for this command.

dhcpv6-snooping flash-storage
dhcpv6-snooping flash-storage [delay <DELAY>]
no dhcpv6-snooping flash-storage [delay <DELAY>]

Description

Configures switch flash storage to be used for backing up client IP bindings (used by DHCPv6 snooping).
When flash storage is configured (and external storage is not already configured for this purpose), the
switch stores the IP bindings in switch flash storage. When the switch restarts, it reads the IP bindings from
the switch flash storage to populate its local cache.

Writing the IP bindings to flash storage only occurs after the configured delay and if there has been a
change in client IP bindings. Writing is skipped when client IP bindings have not changed since the previous
write.

Omitting delay <DELAY> sets the default delay of 900 seconds.

To reduce switch flash aging it is recommended that you use external storage (command dhcpv6-snooping
external-storage) to backup DHCP snooping IP bindings. Alternatively, consider configuring flash storage with a
substantial delay between writes.

DHCP snooping | 133

WhenbothexternalstorageandflashstorageareconfiguredtostoreDHCPsnoopingIPbindings,theexternal
storagetakespriority,andisusedexclusivelyuntilitbecomesunconfigured,atwhichtimeflashstorage(if
configured)isused.Later,ifexternalstorageisconfiguredagain,flashstoragestopsandexternalstorage
resumes.
ThenoformofthiscommanddisablesthesavingofIPbindingsinflashstorage.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
delay <DELAY> Specifiesthedelayinsecondsbetweenwrites(whennecessary)to
theflashstorage,Default:900.Range:300to86400.
Examples
ConfiguringswitchflashstorageforDHCPsnoopingIPbindingstoragewithawritedelayof1200seconds:
| switch(config)# | dhcpv6-snooping |     | flash-storage | delay 1200 |
| --------------- | --------------- | --- | ------------- | ---------- |
Warning: Using flash storage reduces switch lifetime. It is recommended to use an
external-storage.
| Do you want | to continue | (y/n)? | y   |     |
| ----------- | ----------- | ------ | --- | --- |
switch(config)#
UnconfiguringusageofswitchflashstorageforIPbindings:
| switch(config)# | no dhcpv6-snooping |     | flash-storage |     |
| --------------- | ------------------ | --- | ------------- | --- |
CommandHistory
| Release    |     |     | Modification                                    |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.08
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
config
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-snooping    | max-bindings |                |     |     |
| ------------------ | ------------ | -------------- | --- | --- |
| dhcpv6-snooping    | max-bindings | <MAX-BINDINGS> |     |     |
| no dhcpv6-snooping | max-bindings | <MAX-BINDINGS> |     |     |
Description
SetsthemaximumnumberofDHCPv6bindingsallowedontheselectedinterface.Forallinterfaceson
whichthiscommandisnotrun,thedefaultmaxbindingisthemaximumvalueoftherange.
134
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofDHCPbindings.Range0to
1024.
Examples
SettheDHCPv6maxbindingsto256oninterface1/1/1:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|                    | dhcpv6-snooping |     | max-bindings | 256 |
| ------------------ | --------------- | --- | ------------ | --- |
| switch(config-if)# | exit            |     |              |     |
switch(config)#
RevertDHCPv6maxbindingstoitsdefaultoninterface1/1/1:
| switch(config)#    | interface          | 1/1/1 |              |     |
| ------------------ | ------------------ | ----- | ------------ | --- |
| switch(config-if)# | no dhcpv6-snooping |       | max-bindings | 256 |
| switch(config-if)# | exit               |       |              |     |
switch(config)#
CommandHistory
| Release    |     |     | Modification                                    |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-snooping    | trust |     |     |     |
| ------------------ | ----- | --- | --- | --- |
| dhcpv6-snooping    | trust |     |     |     |
| no dhcpv6-snooping | trust |     |     |     |
Description
EnablesDHCPv6snoopingtrustontheselectedinterface.Onlyserverpacketsreceivedontrusted
interfacesareforwarded.Alltheinterfacesareuntrustedbydefault.
ThenoformofthecommanddisablesDHCPv6snoopingtrustontheselectedinterface.
config-if
Examples
EnablingDHCPv6snoopingtrustoninterface2/2/1:
DHCPsnooping|135

| switch(config)# |     | interface | 2/2/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|                    |     | dhcpv6-snooping |     | trust |     |     |
| ------------------ | --- | --------------- | --- | ----- | --- | --- |
| switch(config-if)# |     | exit            |     |       |     |     |
switch(config)#
DisablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface          | 2/2/1 |     |       |     |
| ------------------ | --- | ------------------ | ----- | --- | ----- | --- |
| switch(config-if)# |     | no dhcpv6-snooping |       |     | trust |     |
| switch(config-if)# |     | exit               |       |     |       |     |
switch(config)#
CommandHistory
| Release    |     |     |     | Modification                                    |     |     |
| ---------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
| 10.09.1000 |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |
| 10.09      |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show dhcpv6-snooping
show dhcpv6-snooping
Description
ShowstheDHCPv6snoopingconfiguration.
Examples
ShowingtheDHCPv6snoopingconfiguration:
| switch(config)# |             | show dhcpv6-snooping |              |            |          |                 |
| --------------- | ----------- | -------------------- | ------------ | ---------- | -------- | --------------- |
| DHCPv6-Snooping |             | Information          |              |            |          |                 |
| DHCPv6-Snooping |             | :                    | Yes          | Enabled    | VLANs    | : 1,5,7,100-110 |
| External        | Storage     | Information          |              |            |          |                 |
| Volume          | Name        |                      | : dhcp_snoop |            |          |                 |
| File Name       |             |                      | : ip_binding |            |          |                 |
| Inactive        | Since       |                      | : 01:23:20   | 09/10/2021 |          |                 |
| Error           |             |                      | : Failed     | to write   | external | storage         |
| Flash Storage   | Information |                      |              |            |          |                 |
136
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- |

| File Write       | Delay   | : 300 seconds  |          |                                         |         |
| ---------------- | ------- | -------------- | -------- | --------------------------------------- | ------- |
| Active           | Storage | : External     |          |                                         |         |
| Authorized       | Server  | Configurations |          |                                         |         |
| VRF              |         |                |          | Authorized                              | Servers |
| ------------     |         |                |          | ------------------                      |         |
| default          |         |                |          | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |         |
| default          |         |                |          | 2002::2                                 |         |
| default          |         |                |          | 2004::1                                 |         |
| red              |         |                |          | 2002::1                                 |         |
| red              |         |                |          | 2002::2                                 |         |
| red              |         |                |          | 2002::9                                 |         |
| green            |         |                |          | 5000::1                                 |         |
| green            |         |                |          | 5000::2                                 |         |
| green            |         |                |          | 5000::3                                 |         |
| green            |         |                |          | 5000::7                                 |         |
| green            |         |                |          | 5000::8                                 |         |
| Port Information |         |                |          |                                         |         |
|                  |         | Max            | Static   | Dynamic                                 |         |
| Port             | Trust   | Bindings       | Bindings | Bindings                                |         |
| --------         | -----   | --------       | -------- | --------                                |         |
| 1/1/2            | Yes     | 0              | 0        | 0                                       |         |
| 1/1/3            | Yes     | 0              | 3        | 0                                       |         |
| 1/1/5            | Yes     | 0              | 22       | 0                                       |         |
| 1/1/16           | No      | 256            | 0        | 20                                      |         |
| 10/10/10         | No      | 256            | 12       | 7                                       |         |
| lag120           | No      | 256            | 3        | 0                                       |         |
CommandHistory
| Release |     |     |     | Modification                                    |     |
| ------- | --- | --- | --- | ----------------------------------------------- | --- |
| 10.09   |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
| 10.08   |     |     |     | Updatedexamplewithflashstorageinformation.      |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |         | binding |     |     |
| -------------------- | --- | ------- | ------- | --- | --- |
| show dhcpv6-snooping |     | binding |         |     |     |
Description
ShowstheDHCPv6snoopingbindingconfiguration.
DHCPsnooping|137

Examples
ShowingtheDHCPv6snoopingbindingconfiguration:
switch#
|            | show dhcpv6-snooping |     | binding |     |     |     |     |     |
| ---------- | -------------------- | --- | ------- | --- | --- | --- | --- | --- |
| IP Binding | Information          |     |         |     |     |     |     |     |
======================
| MAC-ADDRESS |     | IPV6-ADDRESS |     |     |     |     | VLAN INTERFACE | TIME- |
| ----------- | --- | ------------ | --- | --- | --- | --- | -------------- | ----- |
LEFT
---------------- ---------------------------------------- ---- --------- ------
----
00:50:56:96:e4:cf aaaa:bbbb:cccc:dddd:eeee:1234:5678:abcd 1 1/1/1
584
| 00:50:56:96:04:4d |     | 1000::3 |     |     |     |     | 134 1/1/2 |     |
| ----------------- | --- | ------- | --- | --- | --- | --- | --------- | --- |
435
| 00:50:56:96:d8:3d |     | 2000:1000::4 |     |     |     |     | 2002 lag123 |     |
| ----------------- | --- | ------------ | --- | --- | --- | --- | ----------- | --- |
21234
CommandHistory
| Release    |     |     |     | Modification                                    |     |     |     |     |
| ---------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
| 10.09.1000 |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |     |     |
| 10.09      |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |            | statistics |     |     |     |     |     |
| -------------------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- |
| show dhcpv6-snooping |     | statistics |            |     |     |     |     |     |
Description
ShowstheDHCPv6snoopingstatistics.
Examples
ShowingtheDHCPv6snoopingstatistics:
| switch(config)# |         | show dhcpv6-snooping          |         | statistics |      |           |     |     |
| --------------- | ------- | ----------------------------- | ------- | ---------- | ---- | --------- | --- | --- |
| Packet-Type     | Action  | Reason                        |         |            |      | Count     |     |     |
| -----------     | ------- | ----------------------------- |         |            |      | --------- |     |     |
| server          | forward | from                          | trusted | port       |      | 12        |     |     |
| client          | forward | to                            | trusted | port       |      | 20        |     |     |
| server          | drop    | received                      | on      | untrusted  | port | 5         |     |     |
| server          | drop    | unauthorized                  |         | server     |      | 4         |     |     |
138
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |

| client | drop destination |       | on          | untrusted | port  | 2   |
| ------ | ---------------- | ----- | ----------- | --------- | ----- | --- |
| client | drop bad         | DHCP  | release     | request   |       | 5   |
| server | drop relay       | reply | on          | untrusted | port  | 2   |
| client | drop failed      | on    | max-binding |           | limit | 5   |
CommandHistory
| Release    |     |     | Modification                                    |     |     |     |
| ---------- | --- | --- | ----------------------------------------------- | --- | --- | --- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |     |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |
10.07orearlier
CommandInformation
| Platforms | Commandcontext |     | Authority                                            |     |     |     |
| --------- | -------------- | --- | ---------------------------------------------------- | --- | --- | --- |
| 6200      |                |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |     |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
DHCPsnooping|139

Chapter 7

ND snooping

ND snooping

Overview
ND (Neighbor Discovery) snooping prevents ND attacks. ND snooping drops invalid ND packets, and
together with DIPLDv6 (Dynamic IP Lockdown for IPv6), blocks data traffic from invalid hosts. ND snooping
is used in Layer 2 switching networks. ND snooping learns the source MAC addresses, source IPv6 addresses,
input interfaces, and VLANs of incoming ND messages and data packets to build IP binding entries.

When DHCPv6 snooping and ND snooping are both enabled, and DHCPv6 clients request and IPv6 address,

entries are added to the DHCP snooping table and DHCP snooping takes priority over ND snooping.

ND snooping drops ND packets as follows:

n If the Ethernet source MAC address is mismatched with the address contained in the ICMPv6 Target link

layer address field of the ND packet.

n If the global IPv6 address in the source address field is mismatched with the ND snooping prefix filter

table.

n If the global IPv6 address or the link-local IPv6 address in the source IP address field is mismatched with

the ND snooping binding table.

ND snooping drops RA and RR packets on untrusted ports. To block only RA packets on VLANs with ND
snooping enabled, use nd-snooping ra-drop. RA (Router Advertisement) drop is disabled by default on
VLANs. When enabled (with nd-snooping ra-drop), ND snooping blocks RA packets on both trusted and
untrusted ports. When RA drop is disabled, ND snooping allows RA packets on trusted ports and blocks
them on untrusted ports.

Dynamic IPv6 lockdown is performed for ND snooping entries. Based on the DAD NS received from the
hosts by the switch, ND snooping entries are programmed into the IP binding table and the hardware (as
allowed). And ND Binding table entries are added when NA packets are received from hosts. Therefore, data
packets from invalid hosts and transit traffic are blocked.

Statically-configured IP binding information supersedes any information collected dynamically by ND snooping for

the same client.

ND snooping commands

clear nd-snooping binding
clear nd-snooping binding {all | ipv6 <IPV6-ADDR> vlan <VLAN-ID> | port <PORT-NUM> | vlan
<VLAN-ID>}

Description

Clears ND snooping binding entries.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

140

Commandcontext
| Parameter |     | Description                                        |     |     |
| --------- | --- | -------------------------------------------------- | --- | --- |
| all       |     | SpecifiesthatallNDbindinginformationistobecleared. |     |     |
ip <IPV6-ADDR> vlan <VLAN-ID> SpecifiestheIPv6addressandVLANforwhichallNDbinding
informationistobecleared.
port <PORT-NUM> SpecifiestheportforwhichallNDbindinginformationistobe
cleared.
vlan <VLAN-ID> SpecifiestheVLANforwhichallNDbindinginformationistobe
cleared.Range:1to4094.
Examples
ClearingallNDbindinginformationfor5000::1:
| switch(config)# | clear nd-snooping | binding ipv6 | 5000::1 |     |
| --------------- | ----------------- | ------------ | ------- | --- |
ClearingallNDbindinginformationfor5000::1vlan1:
| switch(config)# | clear nd-snooping | binding ipv6 | 5000::1 vlan | 1   |
| --------------- | ----------------- | ------------ | ------------ | --- |
ClearingallNDbindinginformationforport1/1/10:
| switch(config)# | clear nd-snooping | binding port | 1/1/10 |     |
| --------------- | ----------------- | ------------ | ------ | --- |
ClearingallNDbindinginformationforVLAN10:
| switch(config)# | clear nd-snooping | binding vlan | 10  |     |
| --------------- | ----------------- | ------------ | --- | --- |
ClearingallNDbindinginformation:
| switch(config)# | clear nd-snooping | binding all |     |     |
| --------------- | ----------------- | ----------- | --- | --- |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
NDsnooping|141

| clear nd-snooping | statistics |     |     |
| ----------------- | ---------- | --- | --- |
| clear nd-snooping | statistics |     |     |
Description
ClearsallNDsnoopingstatistics.
Examples
ClearallNDsnoopingstatistics:
| switch# | clear nd-snooping | statistics |     |
| ------- | ----------------- | ---------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
nd-snooping
| nd-snooping    | {enable|disable} |     |     |
| -------------- | ---------------- | --- | --- |
| no nd-snooping | {enable|disable} |     |     |
Description
EnablesordisablesNDsnooping.NDsnoopingisdisabledbydefault.NDsnoopingisnotsupportedonthe
managementinterface.
Examples
EnablingNDsnooping:
| switch(config)# | nd-snooping | enable |     |
| --------------- | ----------- | ------ | --- |
DisablingNDsnooping:
| switch(config)# | nd-snooping | disable |     |
| --------------- | ----------- | ------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
142
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping | (in config-vlan | context) |
| ----------- | --------------- | -------- |
nd-snooping
no nd-snooping
Description
EnablesNDsnoopingintheconfig-vlancontext.NDsnoopingisdisabledbydefaultforallVLANs.
ThenoformofthecommanddisablesNDsnoopingonthespecifiedVLAN,flushingalltheIPv6bindings
learnedforthisVLANsinceNDsnoopingwasenabledforthisVLAN.
Examples
EnablingNDsnoopingonVLAN100:
| switch(config)# | vlan 100 |     |
| --------------- | -------- | --- |
switch(config-vlan-100)# nd-snooping
switch(config-vlan-100)# exit
switch(config)#
DisablingNDsnoopingonVLAN100:
| switch(config)#          | vlan 100       |     |
| ------------------------ | -------------- | --- |
| switch(config-vlan-100)# | no nd-snooping |     |
switch(config-vlan-100)# exit
switch(config)#
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | mac-check |     |
| -------------- | --------- | --- |
| nd-snooping    | mac-check |     |
| no nd-snooping | mac-check |     |
Description
NDsnooping|143

ThiscommandenablesverificationofthehardwareaddressfieldinNDsnoopingpackets.Whenenabled,
theICMPv6targetlinklayeraddressfieldandthesourceMACaddressmustbethesameforpackets
receivedonuntrustedportsorelsethepacketsaredropped.ThisNDsnoopingMACverificationisenabled
bydefault.
ThenoformofthecommanddisablesNDsnoopingMACverification.
Examples
EnablingNDsnoopingMACverification:
| switch(config)# |     | nd-snooping |     | mac-check |     |     |
| --------------- | --- | ----------- | --- | --------- | --- | --- |
DisablingNDsnoopingMACverification:
| switch(config)# |     | no nd-snooping |     |     | mac-check |     |
| --------------- | --- | -------------- | --- | --- | --------- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |
| --------- | -------------- | --- | --- | --- | --------- | --- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    |             | prefix-list |             |     |     |     |
| -------------- | ----------- | ----------- | ----------- | --- | --- | --- |
| nd-snooping    | prefix-list |             | <IPV6-ADDR> |     |     |     |
| no nd-snooping | prefix-list |             | <IPV6-ADDR> |     |     |     |
Description
ConfigurestheNDsnoopingprefixlistfortheselectedVLANandthespecifiedIPv6addressprefix.ND
snoopingmustbeenabledbothgloballyandonthisVLANbeforethisprefixlistconfigurationtakeseffect.
ThenoformofthiscommandremovestheprefixlistconfigurationfortheselectedVLANandIPv6address.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<IPV6-ADDR>
SpecifiestheIPv6address.
Examples
ConfiguringNDsnoopingprefix-listonVLAN1:
| switch(config)#        |     | vlan | 1           |     |             |            |
| ---------------------- | --- | ---- | ----------- | --- | ----------- | ---------- |
| switch(config-vlan-1)# |     |      | nd-snooping |     | prefix-list | 2001::1/64 |
144
| AOS-CX10.09IPServicesGuide| |     | (6200 | SwitchSeries) |     |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- | --- |

| switch(config-vlan-1)# |     |     | exit |     |     |     |     |
| ---------------------- | --- | --- | ---- | --- | --- | --- | --- |
switch(config)#
RemoveconfigurationofNDsnoopingprefix-listonVLAN100:
| switch(config)#        |     | vlan | 1              |     |             |     |            |
| ---------------------- | --- | ---- | -------------- | --- | ----------- | --- | ---------- |
| switch(config-vlan-1)# |     |      | no nd-snooping |     | prefix-list |     | 2001::1/64 |
| switch(config-vlan-1)# |     |      | exit           |     |             |     |            |
switch(config)#
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
6200 config-vlan-<VLAN-ID> OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| nd-snooping    |              | max-bindings |                |     |     |     |     |
| -------------- | ------------ | ------------ | -------------- | --- | --- | --- | --- |
| nd-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |     |     |
| no nd-snooping | max-bindings |              |                |     |     |     |     |
Description
SetsthemaximumnumberofNDbindingsallowedontheselectedinterface.Forallinterfacesonwhichthis
commandisnotrun,thedefaultmaxbindingsapplies.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofNDbindings.Youcanusethe
|     |     |     |     |     | show capacitiescommandtoseethemaximumavailablefor |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- |
yourswitchmodel.
Examples
SettheNDmaxbindingsto768oninterface2/2/1:
| switch(config)#    |     | interface | 2/2/1       |              |     |     |     |
| ------------------ | --- | --------- | ----------- | ------------ | --- | --- | --- |
| switch(config-if)# |     |           | nd-snooping | max-bindings |     | 768 |     |
| switch(config-if)# |     |           | exit        |              |     |     |     |
switch(config)#
RevertNDmaxbindingstoitsdefaultoninterface2/2/1:
NDsnooping|145

| switch(config)# | interface | 2/2/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|                    | no   | nd-snooping | max-bindings |
| ------------------ | ---- | ----------- | ------------ |
| switch(config-if)# | exit |             |              |
switch(config)#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | nd-guard |     |     |
| -------------- | -------- | --- | --- |
| nd-snooping    | nd-guard |     |     |
| no nd-snooping | nd-guard |     |     |
Description
ThiscommandenablesNDguardontheselectedVLAN.
ThenoformofthecommanddisablesNDguardanddeletesalltheIPv6bindingslearnedontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcanbe
used.
Examples
EnablingNDsnoopingNDguardonVLAN100:
| switch(config)#          | nd-snooping | enable      |          |
| ------------------------ | ----------- | ----------- | -------- |
| switch(config)#          | vlan 100    |             |          |
| switch(config-vlan-100)# |             | nd-snooping | nd-guard |
| switch(config-vlan-100)# |             | exit        |          |
switch(config)#
DisablingNDsnoopingNDguardonVLAN100:
| switch(config)#          | vlan 100 |                |          |
| ------------------------ | -------- | -------------- | -------- |
| switch(config-vlan-100)# |          | no nd-snooping | nd-guard |
| switch(config-vlan-100)# |          | exit           |          |
switch(config)#
CommandHistory
146
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | ra-guard       |     |     |
| -------------- | -------------- | --- | --- |
| nd-snooping    | ra-guard [log] |     |     |
| no nd-snooping | ra-guard       |     |     |
Description
ThiscommandenablesRoutingAdvertisement(RA)guardontheselectedVLAN.Whenenabled,ingress
RoutingAdvertisement(RA)andRoutingRedirect(RR)packetsontheselectedVLANareblockedon
untrustedports.Thepacketsareforwardedwhenreceivedontrustedports.
ThenoformofthecommanddisablesRAguardontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcanbe
used.
| Parameter |     |     | Description                             |
| --------- | --- | --- | --------------------------------------- |
| [log]     |     |     | Logsmessagesalongwithdropfunctionality. |
Examples
EnablingNDsnoopingRAguardonVLAN100:
| switch(config)#          | nd-snooping | enable      |          |
| ------------------------ | ----------- | ----------- | -------- |
| switch(config)#          | vlan 100    |             |          |
| switch(config-vlan-100)# |             | nd-snooping | ra-guard |
| switch(config-vlan-100)# |             | exit        |          |
switch(config)#
EnablingNDsnoopingRAguardonVLAN100witheventloggingondroppedpackets:
| switch(config)#          | nd-snooping | enable      |              |
| ------------------------ | ----------- | ----------- | ------------ |
| switch(config)#          | vlan 100    |             |              |
| switch(config-vlan-100)# |             | nd-snooping | ra-guard log |
| switch(config-vlan-100)# |             | exit        |              |
switch(config)#
DisablingNDsnoopingRAguardonVLAN100:
NDsnooping|147

| switch(config)# | vlan 100 |     |     |
| --------------- | -------- | --- | --- |
switch(config-vlan-100)#
|                          |     | no nd-snooping | ra-guard |
| ------------------------ | --- | -------------- | -------- |
| switch(config-vlan-100)# |     | exit           |          |
switch(config)#
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | ra-drop |     |     |
| -------------- | ------- | --- | --- |
| nd-snooping    | ra-drop |     |     |
| no nd-snooping | ra-drop |     |     |
Description
ThiscommandenablesRoutingAdvertisement(RA)dropontheselectedVLAN.Whenenabled,ingressRA
packetsontheselectedVLANareblockedonbothtrustedanduntrustedports.Whendisabled,RApackets
areforwardedontheselectedVLANwithNDsnoopingtrustedportvalidation.RAdropisdisabledby
default.
NDsnoopingmustbeenabledinboththeconfigcontextandtheconfig-vlancontextbeforethiscommandcanbe
used.
ThenoformofthecommanddisablesNDsnoopingRAdropontheselectedVLAN.
Examples
EnablingNDsnoopingRAdroponVLAN100:
| switch(config)#          | nd-snooping | enable      | vlan 100 |
| ------------------------ | ----------- | ----------- | -------- |
| switch(config-vlan-100)# |             | nd-snooping | ra-drop  |
| switch(config-vlan-100)# |             | exit        |          |
switch(config)#
DisablingNDsnoopingRAdroponVLAN100:
| switch(config)#          | vlan 100 |                |         |
| ------------------------ | -------- | -------------- | ------- |
| switch(config-vlan-100)# |          | no nd-snooping | ra-drop |
| switch(config-vlan-100)# |          | exit           |         |
switch(config)#
CommandHistory
148
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
6200 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | trust |     |     |     |
| -------------- | ----- | --- | --- | --- |
| nd-snooping    | trust |     |     |     |
| no nd-snooping | trust |     |     |     |
Description
EnablesNDsnoopingtrustontheselectedinterface(port).Onlyserverpacketsreceivedontrustedports
areforwarded.Alltheportsareuntrustedbydefault.
ThenoformofthecommanddisablesNDsnoopingtrustontheselectedport.
Examples
EnablingNDsnoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface   | 2/2/1 |       |
| ------------------ | --- | ----------- | ----- | ----- |
| switch(config-if)# |     | nd-snooping |       | trust |
| switch(config-if)# |     | exit        |       |       |
switch(config)#
DisablingNDsnoopingtrustoninterface2/2/1:
switch(config)#
|                    |     | interface      | 2/2/1 |       |
| ------------------ | --- | -------------- | ----- | ----- |
| switch(config-if)# |     | no nd-snooping |       | trust |
| switch(config-if)# |     | exit           |       |       |
switch(config)#
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
config-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show nd-snooping
NDsnooping|149

| show nd-snooping | [vlan <VLAN-ID>] |     |
| ---------------- | ---------------- | --- |
Description
ShowseitherallNDsnoopingconfigurationortheconfigurationforthespecifiedVLAN.
| Parameter |     | Description |
| --------- | --- | ----------- |
vlan <VLAN-ID> SpecifiestheVLANforwhichtheNDconfigurationistobeshown.
Range:1to4094.
Examples
ShowingallNDsnoopingconfiguration:
| switch(config)# | show nd-snooping |     |
| --------------- | ---------------- | --- |
| ND Snooping     | Information      |     |
========================
| ND Snooping     |               | : Enabled         |
| --------------- | ------------- | ----------------- |
| ND Snooping     | Enabled VLANs | : 1               |
| RA Drop Enabled | VLANs         | : 2-3             |
| MAC Address     | Check         | : Disabled        |
| PORT TRUST      | MAX-BINDINGS  | CURRENT-BINDINGS  |
| ------- ------  | ------------- | ----------------- |
| 1/1/1 Yes       | -             | -                 |
| 1/1/2 Yes       | -             | -                 |
| 1/1/3 No        | 100           | 10                |
| 1/1/4 No        | 200           | 10                |
| 1/1/5 No        | 300           | 10                |
ShowingNDsnoopingconfigurationforVLAN2:
| switch(config)# | show nd-snooping | vlan 2 |
| --------------- | ---------------- | ------ |
| ND Snooping     | Information      |        |
=======================
| ND Snooping    | : Enabled        |                   |
| -------------- | ---------------- | ----------------- |
| MAC Address    | Check : Disabled |                   |
| RA Drop        | : Disabled       |                   |
| PORT TRUST     | MAX-BINDINGS     | CURRENT-BINDINGS  |
| ------- ------ | -------------    | ----------------- |
| 1/1/1 Yes      | -                | -                 |
| 1/1/2 Yes      | -                | -                 |
| 1/1/3 No       | 100              | 10                |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
150
AOS-CX10.09IPServicesGuide| (6200 SwitchSeries)

| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6200 OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
(#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show nd-snooping |         | binding |     |     |
| ---------------- | ------- | ------- | --- | --- |
| show nd-snooping | binding |         |     |     |
Description
ShowstheNDsnoopingbindingconfiguration.
Examples
ShowingtheNDsnoopingbindingconfiguration:
| switch# | show nd-snooping | binding |             |            |
| ------- | ---------------- | ------- | ----------- | ---------- |
| PORT    | IPV6-ADDRESS     |         | MAC-ADDRESS | VLAN TIME- |
LEFT STATE
------- ---------------------------------------- ------------------ ----- --------
- ---------
| 1/1/1 | 2001::1 |     | 00:00:0A:01:02:03 | 1 600 |
| ----- | ------- | --- | ----------------- | ----- |
Valid
| 1/1/2 | fe80::250:56ff:fe9a:143c |     | 00:00:0B:01:02:03 | 2 - |
| ----- | ------------------------ | --- | ----------------- | --- |
Tentative
1/1/3 2001:1111:2222:3333:4444:5555:6666:7777 00:00:0C:01:02:03 4094 -
Testing
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
(#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show nd-snooping |             | prefix-list |     |     |
| ---------------- | ----------- | ----------- | --- | --- |
| show nd-snooping | prefix-list |             |     |     |
Description
ShowstheNDsnoopingprefixlistinformation.
Examples
ShowingtheNDsnoopingprefixlistinformation:
NDsnooping|151

| switch# | show nd-snooping                            | prefix-list |     |     |          |     |     |
| ------- | ------------------------------------------- | ----------- | --- | --- | -------- | --- | --- |
| VLAN    | IPV6-ADDRESS-PREFIX                         |             |     |     | SOURCE   |     |     |
| -----   | ------------------------------------------- |             |     |     | -------- |     |     |
| 1       | 2001::/64                                   |             |     |     | Static   |     |     |
| 4094    | 3001::/64                                   |             |     |     | Dynamic  |     |     |
CommandHistory
| Release        |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show nd-snooping |            | statistics |     |     |     |     |     |
| ---------------- | ---------- | ---------- | --- | --- | --- | --- | --- |
| show nd-snooping | statistics |            |     |     |     |     |     |
Description
ShowstheglobalNDsnoopingstatistics.
Examples
ShowingglobalNDsnoopingstatistics:
| switch(config)# | show nd-snooping |        | statistics |     |     |     |       |
| --------------- | ---------------- | ------ | ---------- | --- | --- | --- | ----- |
| PACKET-TYPE     | ACTION           | REASON |            |     |     |     | COUNT |
------------ -------- ----------------------------------------------- --------
| RA  | forward | RA packets | received | on trusted     | port       |        | 20  |
| --- | ------- | ---------- | -------- | -------------- | ---------- | ------ | --- |
| RA  | drop    | RA packets | received | on untrusted   | port       |        | 45  |
| NS  | forward | NS packets | received | on trusted     | port       |        | 52  |
| NS  | forward | NS packets | received | on untrusted   | port       |        | 95  |
| NS  | drop    | NS packets | failed   | MAC check      |            |        | 14  |
| NS  | drop    | NS packets | failed   | Prefix check   |            |        | 12  |
| NS  | drop    | NS packets | failed   | on max-binding | limit      |        | 0   |
| NS  | drop    | NS packets | failed   | ND snooping    | validation | checks | 20  |
| NA  | forward | NA packets | received | on trusted     | port       |        | 17  |
| NA  | forward | NA packets | received | on untrusted   | port       |        | 30  |
| NA  | drop    | NA packets | failed   | Prefix check   |            |        | 15  |
| NA  | drop    | NA packets | failed   | on max-binding | limit      |        | 2   |
| NA  | drop    | NA packets | failed   | ND snooping    | validation | checks | 5   |
CommandHistory
| Release        |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |     |
152
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- | --- | --- | --- |

Command Information

Platforms

Command context

Authority

6200

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

ND snooping | 153

Chapter 8

IP Tunnels

IP Tunnels

True point-to-point networks are not always possible in corporate networking environment. Many networks
deploy nontraditional methods of connection (for example, DSL or broadband) at remote sites or branch
offices. The branch office, telecommuter, or business traveler then becomes separated from the corporate
network. Some method of tunneling becomes imperative to connect all the network sites together.

Virtual Private Networking (VPN) is often deployed to create private tunnels through the public network
system for passing data to remote sites. While VPN is sufficient for the average business traveler, it is not a
good solution for branch site connectivity. VPN configurations must include statically maintained access lists
to identify traffic through the tunnel. These access lists are often tedious to configure for larger networks
and are prone to errors.

VPNs do not permit multicast traffic to pass; therefore routing protocols such as Routing Information
Protocol (RIP) and Open Shortest Path First (OSPF) are no longer options for dynamic routing updates. All
new additions to the network topology must be manually added to the various configured access lists.
Without dynamic routing from one site to another, network management is severely hampered. Network
managers need their non-heterogeneous networks to function like traditional point-to-point networks so
that traditional management methods (once available only on point-to-point circuits) can apply to the entire
network.

The solution to these challenges is to use IP tunnels. An IP tunnel provides a virtual link between endpoints
on two different networks enabling data to be exchanged as if the endpoints were directly connected on the
same network. Traffic between the devices is isolated from the intervening networks that the tunnel spans.

IP tunnels supported features

n Up to 127 tunnels can be defined on a switch shared between different tunnel types.

Unsupported features

n Key support can be added for security and identification purposes when there are multiple applications.

n VPN across public IP network.

Configuring an IP tunnel

Prerequisites

An enabled layer 3 interface with an IP address assigned to it, created with the command interface.

Procedure

1. Create an IP tunnel with the command interface tunnel .

2. Set the IP address for the tunnel. For an IPv6 in IPv4 or an IPv6 in IPv6 tunnel, enter the command

ipv6 address.

3. Set the source IP address for the tunnel. For an IPv6 in IPv4 tunnel, enter the command source ip.

For an IPv6 in IPv6 tunnel, enter the command source ipv6.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

154

4. SetthedestinationIPaddressforthetunnel.ForanIPv6inIPv4tunnel,enterthecommand
destination ip.ForanIPv6inIPv6tunnel,enterthecommanddestination ipv6.
5. Optionally,settheTTL(hopcount)forthetunnelwiththecommandttl.
| 6.  | Optionally,settheMTUforthetunnelwiththecommandip |     |     |     |     |     | mtu. |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | ---- | --- |
7. Optionally,addadescriptiontothetunnelwiththecommanddescription.
| 8.       | Enablethetunnelwiththecommandno        |     |      |        | shutdown. |           |            |          |
| -------- | -------------------------------------- | --- | ---- | ------ | --------- | --------- | ---------- | -------- |
| 9.       | Reviewtunnelsettingswiththecommandshow |     |      |        |           | interface | tunnel.    |          |
| Creating | an IPv6                                | in  | IPv4 | tunnel |           | for       | traversing | a public |
network
ThisexamplecreatesanIPv6inIPv4tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
Procedure
1. Onswitch1:
|     | a. Enableinterface1/1/1andassigntheIPaddress10.1.1.1/24toit. |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
switch# config
|     | switch(config)#                                             | interface |             | 1/1/1       |     |     |     |     |
| --- | ----------------------------------------------------------- | --------- | ----------- | ----------- | --- | --- | --- | --- |
|     | switch(config-if)#                                          |           | ip address  | 10.1.1.1/24 |     |     |     |     |
|     | switch(config-if)#                                          |           | no shutdown |             |     |     |     |     |
|     | b. Enableinterface1/1/2andassigntheIPaddress2080::2/64toit. |           |             |             |     |     |     |     |
switch# config
|     | switch(config)#    | interface |              | 1/1/2 |            |     |     |     |
| --- | ------------------ | --------- | ------------ | ----- | ---------- | --- | --- | --- |
|     | switch(config-if)# |           | ipv6 address |       | 2080::2/64 |     |     |     |
|     | switch(config-if)# |           | no shutdown  |       |            |     |     |     |
|     | switch(config-if)# |           | exit         |       |            |     |     |     |
c. CreateIPv6inIPv4tunnel10andassigntheIPaddress2001:DB8::1/32,sourceaddress
10.1.1.1,anddestinationaddress20.1.1.1toit.
|     | switch(config)#       | interface |             | tunnel   | 10             | mode ip  | 6in4 |     |
| --- | --------------------- | --------- | ----------- | -------- | -------------- | -------- | ---- | --- |
|     | switch(config-ip-if)# |           | ipv6        | address  | 2001:DB8::1/62 |          |      |     |
|     | switch(config-ip-if)# |           | source      | ip       | 10.1.1.1       |          |      |     |
|     | switch(config-ip-if)# |           | destination |          | ip             | 20.1.1.1 |      |     |
|     | switch(config-ip-if)# |           | no          | shutdown |                |          |      |     |
|     | switch(config-ip-if)# |           | exit        |          |                |          |      |     |
IPTunnels |155

d. Definesroutessothattrafficfromnetwork1canreachnetwork2throughthetunnel.
|     | switch(config)# | ip   | route | 20.1.1.0/24 |     | 10.1.1.2 |     |
| --- | --------------- | ---- | ----- | ----------- | --- | -------- | --- |
|     | switch(config)# | ipv6 | route | 290::0/64   |     | tunnel10 |     |
2. Onswitch2:
|     | a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit. |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
switch# config
switch(config)#
|     |                                                             | interface |             | 1/1/1   |             |     |     |
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
|     | switch(config)#       | interface |             | tunnel   | 10          | mode ip 6in4   |     |
| --- | --------------------- | --------- | ----------- | -------- | ----------- | -------------- | --- |
|     | switch(config-ip-if)# |           | ipv6        | address  |             | 2001:DB8::2/62 |     |
|     | switch(config-ip-if)# |           | source      |          | ip 20.1.1.1 |                |     |
|     | switch(config-ip-if)# |           | destination |          |             | ip 10.1.1.1    |     |
|     | switch(config-ip-if)# |           | no          | shutdown |             |                |     |
|     | switch(config-ip-if)# |           | exit        |          |             |                |     |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
|          | switch(config)# | ip  | route | 10.1.1.0/24 |     | 20.1.1.2       |          |
| -------- | --------------- | --- | ----- | ----------- | --- | -------------- | -------- |
|          | switch(config)# | ip  | route | 2080::0/64  |     | tunnel10       |          |
| Creating | an IPv6         | in  | IPv6  | tunnel      |     | for traversing | a public |
network
ThisexamplecreatesanIPv6inIPv6tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
Procedure
1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress2001:DB8:5::1/64toit.
switch# config
|     | switch(config)# | interface |     | 1/1/1 |     |     |     |
| --- | --------------- | --------- | --- | ----- | --- | --- | --- |
156
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |     |     |     |     |
| --------------------------- | ----- | ------------- | --- | --- | --- | --- | --- |

| switch(config-if)# |     | ipv6        | address | 2001:DB8:5::1/64 |     |     |
| ------------------ | --- | ----------- | ------- | ---------------- | --- | --- |
| switch(config-if)# |     | no shutdown |         |                  |     |     |
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
| switch(config)#    | interface |      | 1/1/1   |                  |     |     |
| ------------------ | --------- | ---- | ------- | ---------------- | --- | --- |
| switch(config-if)# |           | ipv6 | address | 2001:DB8:9::1/64 |     |     |
switch(config-if)#
no shutdown
b. Enableinterface1/1/2andassigntheIPaddress2090::2/64toit.
| switch(config)#    | interface |             | 1/1/2   |            |     |     |
| ------------------ | --------- | ----------- | ------- | ---------- | --- | --- |
| switch(config-if)# |           | ipv6        | address | 2090::2/64 |     |     |
| switch(config-if)# |           | no shutdown |         |            |     |     |
| switch(config-if)# |           | exit        |         |            |     |     |
c. CreateIPv6inIPv6tunnel10andassigntheIPaddress2001:DB8::2/32,sourceaddress
2001:DB8:5::1,anddestinationaddress2001:DB8:9::1toit.(Optional)SettheMTUandTTL
parametersforthistunnelinterface.
| switch(config)#       | interface |             | tunnel   | 10                 | mode           | ip 6in6 |
| --------------------- | --------- | ----------- | -------- | ------------------ | -------------- | ------- |
| switch(config-ip-if)# |           | ipv6        | address  |                    | 2001:DB8::2/62 |         |
| switch(config-ip-if)# |           | source      |          | ipv6 2001:DB8:9::1 |                |         |
| switch(config-ip-if)# |           | destination |          | ipv6               | 2001:DB8:5::1  |         |
| switch(config-ip-if)# |           | no          | shutdown |                    |                |         |
| switch(config-ip-if)# |           | exit        |          |                    |                |         |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
| switch(config)# | ipv6 | route | 2001:DB8:5::0/64 |     |          | 2001:DB8:9::2 |
| --------------- | ---- | ----- | ---------------- | --- | -------- | ------------- |
| switch(config)# | ipv6 | route | 2080::0/64       |     | tunnel10 |               |
IP tunnels commands
description
description <DESC>
no description
Description
AssociatesatextdescriptionwithanIPtunnelforidentificationpurposes.
ThenoformofthiscommandremovesthedescriptionfromanIPtunnel.
IPTunnels |157

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<DESC> SpecifiesthedescriptivetexttoassociatewiththeIPtunnel.
Range:1to64printableASCIIcharacters.
Examples
DefinesadescriptionforIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel      | 27 mode | ip 6in4     |
| --------------------- | --------- | ----------- | ------- | ----------- |
| switch(config-ip-if)# |           | description | Network | 3 Tunnel 27 |
RemovesthedescriptionforIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel         | 27  |     |
| --------------------- | --------- | -------------- | --- | --- |
| switch(config-ip-if)# |           | no description |     |     |
DefinesadescriptionforIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel      | 8 mode ip | 6in6       |
| --------------------- | --------- | ----------- | --------- | ---------- |
| switch(config-ip-if)# |           | description | Network   | 4 Tunnel 8 |
RemovesthedescriptionforIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel         | 8   |     |
| --------------------- | --------- | -------------- | --- | --- |
| switch(config-ip-if)# |           | no description |     |     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
config-ip-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| destination    | ip             |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| destination    | ip <IPV4-ADDR> |     |     |     |
| no destination | ip <IPV4-ADDR> |     |     |     |
Description
SetsthedestinationIPaddressforanIPtunnel.Specifytheaddressoftheinterfaceontheremotedeviceto
whichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPaddressfromanIPtunnel.
158
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |     |
| --------------------------- | ----- | ------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiesthedestinationIPaddressinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
Examples
DefinesthedestinationIPaddresstobe10.10.20.1forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel      | 27 mode ip 6in4 |
| --------------------- | --------- | ----------- | --------------- |
| switch(config-ip-if)# |           | destination | ip 10.10.20.1   |
DeletesthedestinationIPaddress10.10.20.1fromIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel         | 27            |
| --------------------- | --------- | -------------- | ------------- |
| switch(config-ip-if)# |           | no destination | ip 10.10.20.1 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| destination    | ipv6              |     |     |
| -------------- | ----------------- | --- | --- |
| destination    | ipv6 <IPVv6-ADDR> |     |     |
| no destination | ipv6 [IPV6-ADDR]  |     |     |
Description
SetsthedestinationIPv6addressforanIPtunnel.Specifytheaddressoftheinterfaceontheremotedevice
towhichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPv6addressfromanIPtunnel.
| Parameter   |     |     | Description                             |
| ----------- | --- | --- | --------------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Thisisoptionalinthenoformofthecommand.
Examples
DefinesthedestinationIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel
IPTunnels |159

| switch(config)# | interface | tunnel | 8 mode ip 6in6 |
| --------------- | --------- | ------ | -------------- |
switch(config-ip-if)#
|     |     | destination | ipv6 2001:DB8::1 |
| --- | --- | ----------- | ---------------- |
DeletesthedestinationIPv6address2001:DB8::1fromIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel         | 8                |
| --------------------- | --------- | -------------- | ---------------- |
| switch(config-ip-if)# |           | no destination | ipv6 2001:DB8::1 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-ip-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| interface | tunnel |     |     |
| --------- | ------ | --- | --- |
interface tunnel <TUNNEL-NUMBER> mode {gre ipv4 | ip 6in4 | ip 6in6}
| interface tunnel | <EXISTING-TUNNEL-NUMBER> |     |     |
| ---------------- | ------------------------ | --- | --- |
no interface tunnel <EXISTING-TUNNEL-NUMBER> [mode {gre ipv4 | ip 6in4 | ip 6in6}]
Description
CreatesorupdatesanIPtunnel.Afteryouenterthecommand,thefirmwareswitchestotheconfiguration
contextforthetunnel.
Ifthespecifiedtunnelexists,thiscommandswitchestothecontextforthetunnel.
Bydefault,alltunnelsareautomaticallyassignedtothedefaultVRFwhentheyarecreated.
ThenoformofthiscommanddeletesanexistingIPtunnel.Itisoptionaltoincludeamodeinthenoform,
butifamodehasbeenentered,selectingamodeisrequired.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
mode {gre ipv4 | ip 6in4 | ip 6in6} CreatesanIPtunnel.Chooseoneofthefollowingoptions:
n ip 6in4:CreatesanIPv4tunnelforIPv6traffic.
ip 6in6:CreatesanIPv6tunnelforIPv6traffic.
n
Thisisoptionalinthenoform,unlessamodehasalready
beenentered.
<TUNNEL-NUMBER> Specifiesthenumberforanewtunnel.Range:1to127.
Numberingissharedbetweenalltunnels,sothesametunnel
numbercannotbeusedforanIPv6inIPv4tunnelandaGRE
tunnel.
<EXISTING-TUNNEL-NUMBER>
SpecifiesthenumberforanexistingIPtunnel.Range:1to127.
Examples
160
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |
| --------------------------- | ----- | ------------- | --- |

DefinesanewIPv6inIPv4tunnelwithnumber27.
| switch(config)# | interface | tunnel | 27 mode | ip 6in4 |
| --------------- | --------- | ------ | ------- | ------- |
switch(config-ip-if)#
Switchestotheconfig-ip-ifcontextforexistingtunnel27.
| switch(config)# | interface | tunnel | 27  |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-ip-if)#
DeletesIPv6inIPv4tunnel27.
| switch(config)# | no interface | tunnel | 27  |     |
| --------------- | ------------ | ------ | --- | --- |
DefinesanewIPv6inIPv6tunnelwithnumber8.
| switch(config)# | interface | tunnel | 8 mode | ip 6in6 |
| --------------- | --------- | ------ | ------ | ------- |
switch(config-ip-if)#
DeletesIPv6inIPv6tunnelwithnumber3.
| switch(config)# | no interface | tunnel | 33  | mode gre ipv4 |
| --------------- | ------------ | ------ | --- | ------------- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config |     | forthiscommand. |     |
| --- | ------ | --- | --------------- | --- |
ip address
| ip address <IPV4-ADDR>/<MASK> |                    |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |
| no ip address                 | <IPV4-ADDR>/<MASK> |     |     |     |
Description
SetsthelocalIPaddressofaGREtunnel.Thisaddressidentifiesthetunnelinterfaceforrouting.Itmustbe
onthesamesubnetasthetunneladdressassignedontheremotedevice.
ThenoformofthiscommanddeletesthelocalIPaddressassignedtoaGREtunnel.
IPTunnels |161

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiesthetunnelIPaddressinIPv4format(x.x.x.x),wherex
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK> |     |     |
| --------------- | ------------------ | --- | --- |
| no ipv6 address | <IPV6-ADDR>/<MASK> |     |     |
Description
SetsthelocalIPaddressofanIPv6toIPv4tunnelorofanIPv6toIPv6tunnel.Thisaddressidentifiesthe
tunnelinterfaceforrouting.Itmustbeonthesamesubnetasthetunneladdressassignedontheremote
device.
ThenoformofthiscommanddeletesthelocalIPaddressassignedtoanIPv6toIPv4tunnel.
| Parameter   |     |     | Description                             |
| ----------- | --- | --- | --------------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
162
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |
| --------------------------- | ----- | ------------- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
hexadecimalnumberfrom0toF.
| <MASK> |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to32.
Examples
DefinesthelocalIPaddress2001:DB8:5::1/64fortunnel8foranIPv6toIPv6tunnel.
| switch(config)#       | interface | tunnel       | 8 mode ip 6in6   |
| --------------------- | --------- | ------------ | ---------------- |
| switch(config-ip-if)# |           | ipv6 address | 2001:DB8:5::1/64 |
DeletesthelocalIPaddress2001:DB8::1/32fortunnel8.
| switch(config)#       | interface | tunnel          | 8                |
| --------------------- | --------- | --------------- | ---------------- |
| switch(config-ip-if)# |           | no ipv6 address | 2001:DB8:5::1/64 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-ip-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if |     | forthiscommand. |
| --- | --------- | --- | --------------- |
ip mtu
ip mtu <VALUE>
Description
SetstheMTU(maximumtransmissionunit)foranIPinterface.Thedefaultvalueis1500bytes.
ThenoformofthiscommandsetstheMTUtothedefaultvalueof1500bytes.
| Parameter |     |     | Description                                          |
| --------- | --- | --- | ---------------------------------------------------- |
| <VALUE>   |     |     | SpecifiestheMTUinbytes.Range:1,280bytesto9,192bytes. |
Usage
TheIPMTUisthelargestIPpacketthatcanbesentorreceivedbytheinterface.Foratunnel,theIPMTUis
themaximumsizeoftheIPpayload.Toenablejumbopacketforwardingthroughthetunnel,settheIPMTU
ofthetunneltoavaluegreaterthan1500.AlsosettheMTUandtheIPMTUvaluesfortheunderlying
physicalinterfacethatthetunnelisusingtoavaluegreaterthan1,500bytes.TheIPMTUofthetunnel
IPTunnels |163

mustalsobegreaterthanorequaltotheMTUoftheingressinterfaceontheswitch.TheIPMTUvalueof
thetunnelmustalsobelessthanorequaltotheIPMToftheunderlyinginterfacethatthetunnelisusing.
Examples
SetstheMTUonIPv6inIPv4tunnel27to1000bytes.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | mtu       | 1000   |                 |
SetstheMTUonIPv6inIPv4tunnel27tothedefaultvalue.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | ip        | mtu    |                 |
SetstheMTUonIPv6inIPv6tunnel8to900bytes.
| switch(config)#       | interface | tunnel   | 8 mode ip 6in6 |
| --------------------- | --------- | -------- | -------------- |
| switch(config-ip-if)# | ip        | mtu 9000 |                |
SetstheMTUonIPv6inIPv6tunnel8tothedefaultvalue.
| switch(config)#       | interface | tunnel | 8 mode ip 6in6 |
| --------------------- | --------- | ------ | -------------- |
| switch(config-ip-if)# | ip        | mtu    |                |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface | tunnel                  |     |     |
| -------------- | ----------------------- | --- | --- |
| show interface | tunnel[<TUNNEL-NUMBER>] |     |     |
Description
ShowsconfigurationsettingsforallIPtunnels,oraspecifictunnel.
| Parameter       |     |     | Description                                  |
| --------------- | --- | --- | -------------------------------------------- |
| <TUNNEL-NUMBER> |     |     | SpecifiesthenumberofanIPtunnel.Range:1to127. |
Examples
164
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Showsconfigurationsettingsfortunnel12,whichisanIPv6inIPv6tunnelinthefollowingexample.
|     | switch#      | show        | interface |         | tunnel12 |         |     |     |       |     |
| --- | ------------ | ----------- | --------- | ------- | -------- | ------- | --- | --- | ----- | --- |
|     | Interface    | tunnel12    |           | is      | up       |         |     |     |       |     |
|     | Admin        | state       | is up     |         |          |         |     |     |       |     |
|     | tunnel       | type        | IPv6      | in IPv6 |          |         |     |     |       |     |
|     | tunnel       | interface   |           | IPv6    | address  | 4::1/64 |     |     |       |     |
|     | tunnel       | source      | IPv6      | address |          | 2::1    |     |     |       |     |
|     | tunnel       | destination |           | IPv6    | address  | 2::2    |     |     |       |     |
|     | tunnel       | ttl         | 60        |         |          |         |     |     |       |     |
|     | Description: |             | Network2  |         | Tunnel   |         |     |     |       |     |
|     | Statistics   |             |           |         |          | RX      |     | TX  | Total |     |
------------- -------------------- -------------------- --------------------
|     | L3 Packets |     |     |     |     |     | 0   | 0   |     | 0   |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | L3 Bytes   |     |     |     |     |     | 0   | 0   |     | 0   |
CommandHistory
| Release        |     |     |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     |     | Commandcontext |     |     |     | Authority |     |     |     |
| --------- | --- | --- | -------------- | --- | --- | --- | --------- | --- | --- | --- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | running-config |     |     |           | interface             |     | tunnel |     |     |     |
| ---- | -------------- | --- | --- | --------- | --------------------- | --- | ------ | --- | --- | --- |
| show | running-config |     |     | interface | tunnel<TUNNEL-NUMBER> |     |        |     |     |     |
Description
ShowsthecommandsusedtoconfigureanIPtunnel.
| Parameter |     |     |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<TUNNEL-NUMBER>
SpecifiesthenumberofanIPtunnel.Range:1to127.
Examples
ShowstheconfigurationforIPv6inIPv4tunnel.
|     | switch#     | show | running-config   |             |     | interface | tunnel5 |     |     |     |
| --- | ----------- | ---- | ---------------- | ----------- | --- | --------- | ------- | --- | --- | --- |
|     | interface   |      | tunnel5          | mode        | ip  | 6in4      |         |     |     |     |
|     | source      | ip   | 10.10.10.12      |             |     |           |         |     |     |     |
|     | destination |      | ip               | 22.20.20.20 |     |           |         |     |     |     |
|     | ip6 address |      | 2001:DB8:5::1/64 |             |     |           |         |     |     |     |
|     | ttl 60      |      |                  |             |     |           |         |     |     |     |
IPTunnels |165

no shutdown
| description | Network10 |     |     |
| ----------- | --------- | --- | --- |
ShowstheconfigurationforIPv6inIPv6tunnel.
| switch#      | show running-config | interface | tunnel1 |
| ------------ | ------------------- | --------- | ------- |
| interface    | tunnel 1 mode       | ip 6in6   |         |
| description  | Network2            | Tunnel    |         |
| source       | ipv6 2::1           |           |         |
| destination  | ipv6 2::2           |           |         |
| ipv6 address | 4::1/64             |           |         |
| ttl 60       |                     |           |         |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
shutdown
shutdown
no shutdown
Description
ThiscommanddisablesanIPinterface.IPinterfacesaredisabledbydefaultwhencreated.
ThenoformofthiscommandenablesanIPinterface.
Examples
EnablesIPv6inIPv4interface27.
| switch(config)#       | interface | tunnel   | 27 mode ip 6in4 |
| --------------------- | --------- | -------- | --------------- |
| switch(config-ip-if)# | no        | shutdown |                 |
DisablesIPv6inIPv4interface27.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | shutdown  |        |                 |
CommandHistory
166
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Examples
DefinesthesourceIPaddresstobe10.10.10.1forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# |           | source | ip 10.10.10.1   |
DeletesthesourceIPaddress10.1.10.1fromIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel    | 27            |
| --------------------- | --------- | --------- | ------------- |
| switch(config-ip-if)# |           | no source | ip 10.10.10.1 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
IPTunnels |167

| source ipv6    |             |     |     |     |
| -------------- | ----------- | --- | --- | --- |
| source ipv6    | <IPV6-ADDR> |     |     |     |
| no source ipv6 | [IPV6-ADDR] |     |     |     |
Description
SetsthesourceIPv6addresstobeusedfortheencapsulation.
ThenoformofthiscommanddeletesthesourceIPv6addressforanIPtunnel.
| Parameter   |     |     | Description                             |     |
| ----------- | --- | --- | --------------------------------------- | --- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Thisisoptionalinthenoformofthecommand.
Examples
DefinesthesourceIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel | 8 mode           | ip 6in6 |
| --------------------- | --------- | ------ | ---------------- | ------- |
| switch(config-ip-if)# |           | source | ipv6 2001:DB8::1 |         |
DeletesthesourceIPaddress2001:DB8::1fromIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel    | 8    |             |
| --------------------- | --------- | --------- | ---- | ----------- |
| switch(config-ip-if)# |           | no source | ipv6 | 2001:DB8::1 |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ttl
ttl <COUNT>
no ttl
Description
SetstheTTL(time-to-live),alsoknownasthehopcount,fortunneledpackets.Ifnotconfigured,thedefault
valueof64isusedforthetunnel.(Thehopcountoftheoriginalpacketsisnotchanged.)Amaximumof
fourdifferentTTLvaluescanbeusedatthesametimebyalltunnelsontheswitch.Forexample,iftunnel-1
hasTTL10,tunnel-2hasTTL20,tunnel-3hasTTL30,andtunnel-4hasTTL40,thentunnel-5cannothavea
uniqueTTLvalue,itmustreuseoneofthevaluesassignedtotheothertunnels(10,20,30,40).
168
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |     |
| --------------------------- | ----- | ------------- | --- | --- |

ThenoformofthiscommandsetsTTLtothedefaultvalueof64.
| Parameter |     |     | Description                                   |
| --------- | --- | --- | --------------------------------------------- |
| <COUNT>   |     |     | Specifiesthehopcount.Range:1to255.Default:64. |
Examples
DefinesaTTLof55forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | ttl       | 55     |                 |
SetstheTTLforIPv6inIPv4tunnel27tothedefaultvalueof64.
| switch(config)#       | interface | tunnel | 27  |
| --------------------- | --------- | ------ | --- |
| switch(config-ip-if)# | no        | ttl    |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-ip-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
IPTunnels |169

Internet Control Message Protocol
(ICMP)

Chapter 9

Internet Control Message Protocol (ICMP)

The Internet Control Message Protocol (ICMP) is a supporting protocol in the Internet protocol suite. The
protocol is used by network devices, including routers, to send error messages and operational information.
For example, an ICMP message might indicate that a requested service is not available. Another example of
an ICMP message might be that a host or router could not be reached.

ICMP message types
The type field identifies the type of message sent by the host or gateway.

Type

ICMP messages

0

3

4

5

8

9

10

11

12

13

14

15

16

17

18

Echo Reply (Ping Reply, used with Type 8, Ping Request)

Destination Unreachable

Source Quench

Redirect

Echo Request (Ping Request, used with Type 0, Ping Reply)

Router Advertisement (Used with Type 9)

Router Solicitation (Used with Type 10)

Time Exceeded

Parameter Problem

Timestamp Request (Used with Type 14)

Timestamp Reply (Used with Type 13)

Information Request (obsolete) (Used with Type 16)

Information Reply (obsolete) (Used with Type 15)

Address Mask Request (Used with Type 17)

Address Mask Reply (Used with Type 18)

When ICMP messages are sent

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

170

ICMPmessagesaresentwhenoneormoreofthefollowingscenariosoccur:
Adatagramcannotreachitsdestination.
n
n Thegatewaydoesnothavethebufferingcapacitytoforwardadatagram.
n Thegatewaycandirectthehosttosendtrafficonashorterroute.
| ICMP | redirect | messages |     |     |
| ---- | -------- | -------- | --- | --- |
ICMPredirectmessagesareusedbyrouterstonotifythehostsonthedatalinkthatabetterrouteis
availableforaparticulardestination.
| When | ICMP | redirect | messages | are sent |
| ---- | ---- | -------- | -------- | -------- |
Theswitchisconfiguredtosendredirectsbydefault.ICMPredirectmessagesaresentwhenoneormoreof
thefollowingscenariosoccur:
n Theinterfaceonwhichthepacketcomesintotherouteristhesameinterfaceonwhichthepacketgets
routedout.
n ThesubnetornetworkofthesourceIPaddressisonthesamesubnetornetworkofthenext-hopIP
addressoftheroutedpacket.
Thedatagramisnotsource-routed.
n
n Thedestinationunicastaddressisunreachable.Inthiscase,theroutergeneratestheICMPdestination
unreachablemessagetoinformthesourcehostaboutthesituation.
| ICMP       | commands |     |     |     |
| ---------- | -------- | --- | --- | --- |
| ip icmp    | redirect |     |     |     |
| ip icmp    | redirect |     |     |     |
| no ip icmp | redirect |     |     |     |
Description
EnablesthesendingofICMPv4andICMPv6redirectmessagestothesourcehost.Enabledbydefault.ICMP
redirectandactiveforwardingaremutuallyexclusive.
ThenoformofthiscommanddisablesICMPv4andICMPv6redirectmessagestothesourcehost.
Examples
EnablingICMPredirectmessages:
| switch(config)# |     | ip icmp | redirect |     |
| --------------- | --- | ------- | -------- | --- |
DisablingICMPredirectmessages:
| switch(config)# |     | no ip icmp | redirect |     |
| --------------- | --- | ---------- | -------- | --- |
CommandHistory
InternetControlMessageProtocol(ICMP)|171

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip icmp throttle    |                     |     |
| ------------------- | ------------------- | --- |
| ip icmp throttle    | <PACKET-INTERVAL>   |     |
| no ip icmp throttle | [<PACKET-INTERVAL>] |     |
Description
UsedtoconfigurethethrottleparameterforbothICMPv4andICMPv6errormessagesandredirect
messages.
ThenoformofthiscommanddisablesthethrottleparameterforbothICMPv4andICMPv6errormessages
andredirectmessages.
| Parameter |     | Description |
| --------- | --- | ----------- |
<PACKET-INTERVAL>
SpecifiestheICMPv4/v6packetintervalinseconds.Default:1
second.Range:1-86400.
Examples
EnablingthethrottleparameterforbothICMPv4andICMPv6errormessagesandredirectmessages:
| switch(config)# | ip icmp | throttle 3000 |
| --------------- | ------- | ------------- |
DisablingthethrottleparameterforbothICMPv4andICMPv6errormessagesandredirectmessages:
| switch(config)# | no ip icmp | throttle |
| --------------- | ---------- | -------- |
CommandHistory
| Release |     | Modification                                      |
| ------- | --- | ------------------------------------------------- |
| 10.8    |     | Addedtheoptional<PACKET-INTERVAL>parametertotheno |
formofthecommand.
| 10.07orearlier |     | --  |
| -------------- | --- | --- |
CommandInformation
172
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip icmp unreachable |     |     |
| ------------------- | --- | --- |
ip icmp unreachable
| no ip icmp unreachable |     |     |
| ---------------------- | --- | --- |
Description
EnablesthesendingofICMPv4andICMPv6destinationunreachablemessagesontheswitchtoasource
hostwhenaspecifichostisunreachable.Theunreachablehostaddressoriginatesfromthefailedpacked.
Defaultsetting.
ThenoformofthiscommanddisablesthesendingofICMPv4andICMPv6destinationunreachable
messagesfromtheswitchtoasourcehostwhenaspecifichostisunreachable.Thiscommanddoesnot
preventotherhostsfromsendinganICMPunreachablemessage.
Examples
EnablingICMPv4andICMPv6destinationunreachablemessagestoasourcehost:
| switch(config)# | ip icmp | unreachable |
| --------------- | ------- | ----------- |
DisablingICMPv4andICMPv6destinationunreachablemessagestoasourcehost:
| switch(config)# | no ip icmp | unreachable |
| --------------- | ---------- | ----------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
InternetControlMessageProtocol(ICMP)|173

Chapter 10

DNS

DNS

The Domain Name System (DNS) is the Internet protocol for mapping a hostname to its IP address. DNS
allows users to enter more readily memorable and intuitive hostnames, rather than IP addresses, to identify
devices connected to a network. It also allows a host to keep the same hostname even if it changes its IP
address.

Hostname resolution can be either static or dynamic.

n In static resolution, a local table is defined on the switch that associates hostnames with their IP
addresses. Static tables can be used to speed up the resolution of frequently queried hosts.

n Dynamic resolution requires that the switch query a DNS server located elsewhere on the network.

Dynamic name resolution takes more time than static name resolution, but requires far less configuration
and management.

DNS client
The DNS client resolves hostnames to IP addresses for protocols that are running on the switch. When the
DNS client receives a request to resolve a hostname, it can do so in one of two ways:

n Forward the request to a DNS name server for resolution.

n Reply to the request without using a DNS name server, by resolving the name using a statically defined

table of hostnames and their associated IP addresses.

Configuring the DNS client

Procedure

1. Configure one or more DNS name servers with the command ip dns server.

2. To resolve DNS requests by appending a domain name to the requests, either configure a single

domain name with the command ip dns domain-name, or configure a list of up to six domain names
with the command ip dns domain-list.

3. To use static name resolution for certain hosts, associate an IP address to a host with the command

ip dns host.

4. Review your DNS configuration settings with the command show ip dns.

Examples

This example creates the following configuration:

n Defines the domain switch.com to append to all requests.

n Defines a DNS server with IPv4 address of 1.1.1.1.

n Defines a static DNS host named myhost1 with an IPv4 address of 3.3.3.3.

n DNS client traffic is sent on the default VRF (named default).

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

174

| switch(config)# |     | ip dns | domain-name | switch.com |
| --------------- | --- | ------ | ----------- | ---------- |
switch(config)#
|                 |                 | ip dns | server-address | 1.1.1.1 |
| --------------- | --------------- | ------ | -------------- | ------- |
| switch(config)# |                 | ip dns | host myhost1   | 3.3.3.3 |
| switch(config)# |                 | exit   |                |         |
| switch#         | show            | ip dns |                |         |
| VRF             | Name : vrf_mgmt |        |                |         |
| Host            | Name            |        |                | Address |
--------------------------------------------------------------------------------
| VRF    | Name : vrf_default |              |     |         |
| ------ | ------------------ | ------------ | --- | ------- |
| Domain | Name               | : switch.com |     |         |
| DNS    | Domain list        | :            |     |         |
| Name   | Server(s)          | : 1.1.1.1    |     |         |
| Host   | Name               |              |     | Address |
--------------------------------------------------------------------------------
myhost1
| DNS       | client      | commands      |      |                  |
| --------- | ----------- | ------------- | ---- | ---------------- |
| ip dns    | domain-list |               |      |                  |
| ip dns    | domain-list | <DOMAIN-NAME> | [vrf | <VRF-NAME>]      |
| no ip dns | domain-list | <DOMAIN-NAME> |      | [vrf <VRF-NAME>] |
Description
ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
| vrf <VRF-NAME> |     |     |     | SpecifiesaVRFname.Default:default. |
| -------------- | --- | --- | --- | ---------------------------------- |
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
| switch(config)# |     | ip dns | domain-list | domain1.com |
| --------------- | --- | ------ | ----------- | ----------- |
| switch(config)# |     | ip dns | domain-list | domain2.com |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |     | no ip dns | domain-list | domain1.com |
| --------------- | --- | --------- | ----------- | ----------- |
CommandHistory
DNS|175

| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | domain-name |               |     |       |            |     |
| --------- | ----------- | ------------- | --- | ----- | ---------- | --- |
| ip dns    | domain-name | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | domain-name | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.By
default,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip dns
domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DOMAIN-NAME>
SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     | ip dns | domain-name |     | domain.com |     |
| --------------- | --- | ------ | ----------- | --- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |     | no ip dns | domain-name |     | domain.com |     |
| --------------- | --- | --------- | ----------- | --- | ---------- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
176
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- |

| Platforms |     | Commandcontext |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | host |             |           |           |                  |     |
| --------- | ---- | ----------- | --------- | --------- | ---------------- | --- |
| ip dns    | host | <HOST-NAME> | <IP-ADDR> |           | [ vrf <VRF-NAME> | ]   |
| no ip dns | host | <HOST-NAME> |           | <IP-ADDR> | [ vrf <VRF-NAME> | ]   |
Description
AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadofqueryinga
DNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFisdefined,the
defaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
host <HOST-NAME> Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
| ThisexampledefinesanIPv4addressof        |     |     |        |            | 3.3.3.3forhost1.  |     |
| ---------------------------------------- | --- | --- | ------ | ---------- | ----------------- | --- |
| switch(config)#                          |     | ip  | dns    | host host1 | 3.3.3.3           |     |
| ThisexampledefinesanIPv6addressofb::5    |     |     |        |            | forhost 1.        |     |
| switch(config)#                          |     | ip  | dns    | host host1 | b::5              |     |
| Thisexampledefinesremovestheentryforhost |     |     |        |            | 1withaddressb::5. |     |
| switch(config)#                          |     | no  | ip dns | host       | host1 b::5        |     |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
DNS|177

| Platforms |     | Commandcontext |     |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | server         | address |           |     |       |            |     |
| --------- | -------------- | ------- | --------- | --- | ----- | ---------- | --- |
| ip dns    | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
| switch(config)# |     |     | ip dns | server-address |     | 1.1.1.1 |     |
| --------------- | --- | --- | ------ | -------------- | --- | ------- | --- |
Thisexampledefinesanameserverata::1.
switch(config)#
|     |     |     | ip dns | server-address |     | a::1 |     |
| --- | --- | --- | ------ | -------------- | --- | ---- | --- |
Thisexampleremovesanameserverata::1.
| switch(config)# |     |     | no ip dns | server-address |     | a::1 |     |
| --------------- | --- | --- | --------- | -------------- | --- | ---- | --- |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |
CommandInformation
178
| AOS-CX10.09IPServicesGuide| |     |     | (6200 SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ------------------- | --- | --- | --- | --- |

| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip     | dns  |             |     |     |     |
| ----------- | ---- | ----------- | --- | --- | --- |
| show ip dns | [vrf | <VRF-NAME>] |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
| switch(config)# |     | ip dns | domain-name |     | domain.com  |
| --------------- | --- | ------ | ----------- | --- | ----------- |
| switch(config)# |     | ip dns | domain-list |     | domain5.com |
| switch(config)# |     | ip dns | domain-list |     | domain8.com |
switch(config)#
|                 |           | ip dns         | server-address |               | 4.4.4.4 |
| --------------- | --------- | -------------- | -------------- | ------------- | ------- |
| switch(config)# |           | ip dns         | server-address |               | 6.6.6.6 |
| switch(config)# |           | ip dns         | host           | host3 5.5.5.5 |         |
| switch(config)# |           | ip dns         | host           | host3 c::12   |         |
| switch#         | show      | ip dns         |                |               |         |
| VRF Name        | : default |                |                |               |         |
| Domain Name     | :         | domain.com     |                |               |         |
| DNS Domain      | list      | : domain5.com, |                | domain8.com   |         |
| Name Server(s)  |           | : 4.4.4.4,     | 6.6.6.6        |               |         |
| Host Name       |           | Address        |                |               |         |
-------------------------------
| host3 |     | 5.5.5.5 |     |     |     |
| ----- | --- | ------- | --- | --- | --- |
| host3 |     | c::12   |     |     |     |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|179

Chapter 11

ARP

ARP

ARP (Address Resolution Protocol) is used to map the network address assigned to a device to its physical
address. For example, on an Ethernet network, ARP maps layer 3 IPv4 network addresses to layer 2 MAC
addresses. (ARP does not work with IPv6 addresses. Instead, the Neighbor discovery protocol is used.)

ARP operates at layer 2. ARP requests are broadcast to all devices on the local network segment and are not
forwarded by routers. ARP is enabled by default and cannot be disabled.

Proxy ARP

Proxy ARP allows a routing switch to answer ARP requests from devices on one network on behalf of devices
on another network. The ARP proxy is aware of the location of the traffic destination, and offers its own
MAC address as the final destination.

For example, if Proxy ARP is enabled on a routing switch connected to two subnets (10.10.10.0/24 and
20.20.20.0/24), the routing switch can respond to an ARP request from 10.10.10.69 for the MAC address of
the device with IP address 20.20.20.69.

Typically, the host that sent the ARP request then sends its packets to the switch that has the ARP proxy.
This switch then forwards the packets to the intended host through a mechanism such as a tunnel.

Proxy ARP is supported on L3 physical and VLAN interfaces. It is disabled by default. To enable proxy ARP,
routing must be enabled on the interface.

Local proxy ARP

Local proxy ARP is a technique by which a device on a given network answers the ARP queries for a host
address that is on the same network. It is primarily used to enable layer 3 communication between hosts
within a common subnet that are separated by layer 2 boundaries (Example: PVLAN). Local proxy ARP is
supported on L3 physical and VLAN interfaces.

Local proxy ARP is disabled by default. Routing must be enabled on the interface to enable local proxy ARP.

Dynamic ARP inspection

ARP is used for resolving IP against MAC addresses on a broadcast network segment like the Ethernet and
was originally defined by Internet Standard RFC 826. ARP does not support any inherent security
mechanism and as such depends on simple datagram exchanges for the resolution, with many of these
being broadcast.

Because it is an unreliable and non-secure protocol, ARP is vulnerable to attacks. Some attacks may be
targeted toward the networks whereas other attacks may be targeted toward the switch itself. The attacks
primarily intend to create denial of service (DoS) for the other entities present in the network.

Most of the attacks are carried out in one of the following three forms:

n Overwhelming the switch control plane with too many ARP packets.

n Overwhelming the switch control plane with too many unresolved data packets.

n Masquerading as a trusted gateway/server by wrongly advertising ARPs.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

180

Several defense mechanisms can be put in place on a switch to protect against attacks:

n Limit the amount of ARP activity allowed from a host or on a port.

n Ensure that all ARP packets are consistent with one or more binding databases, which can be created

through various means.

n Enforce integrity checks on the ARP packets to check against different MAC or IP addresses in the

Ethernet or IP header and ARP header.

 Only the following is supported:

n Enabling and disabling of Dynamic ARP Inspection on a VLAN level (it does not have to be SVI).

n Defining the member ports of a VLAN as either trusted or untrusted.

n Only ARP traffic on untrusted ports subjected to checks.

n Routed ports (RoPs) always treated as trusted.

n Listening to the DHCP Bindings table and check every ARP packet to match against the binding.

ARP ACLs are not supported in this release and the DHCP snooping table will be the only source of binding.

Configuring proxy ARP

Procedure

1. Switch to configuration context with the command config.

2. Switch to an interface VLAN with the command interface vlan.

3. Enable local proxy ARP with the command ip proxy-arp.

Examples

This example configures proxy ARP on interface VLAN 30.

switch# config
switch(config)# interface vlan 30
switch(config-vlan-30)# ip proxy-arp

Configuring local proxy ARP

Procedure

1. Switch to configuration context with the command config.

2. Switch to an interface VLAN with the command interface vlan.

3. Enable local proxy ARP with the command ip local-proxy-arp.

Examples

This example configures local proxy ARP on interface VLAN 30.

switch# config
switch(config)# interface vlan 30
switch(config-vlan-30)# ip local-proxy-arp

ARP | 181

ARP commands
arp inspection
arp inspection
Description
EnablesDynamicARPInspectiononthecurrentVLAN,forcingallARPpacketsfromuntrustedportstobe
subjectedtoaMAC-IPassociationcheckagainstabindingtable.
ThenoformofthiscommanddisablesDynamicARPInspectionontheVLAN.
Examples
EnablingdynamicARPinspection:
| switch#         | configure terminal |     |
| --------------- | ------------------ | --- |
| switch(config)# | vlan 1             |     |
switch(config-vlan)# arp inspection
DisablingdynamicARPinspection:
| switch#              | configure terminal |     |
| -------------------- | ------------------ | --- |
| switch(config)#      | vlan 1             |     |
| switch(config-vlan)# | no arp inspection  |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| arp inspection    | trust |     |
| ----------------- | ----- | --- |
| arp inspection    | trust |     |
| no arp inspection | trust |     |
Description
Configurestheinterfaceasatrusted.Allinterfacesareuntrustedbydefault.
Thenoformofthiscommandreturnstheinterfacetothedefaultstate(untrusted).
Example
Settinganinterfaceastrusted:
| switch(config-if)# | arp inspection | trust |
| ------------------ | -------------- | ----- |
182
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| arp ipv4    | mac         |     |                |     |
| ----------- | ----------- | --- | -------------- | --- |
| arp ipv4    | <IPV4_ADDR> | mac | <MAC_ADDR>     |     |
| no arp ipv4 | <IPV4_ADDR> |     | mac <MAC_ADDR> |     |
Description
SpecifiesapermanentstaticneighborentryintheARPtable(forIPv4neighbors).
ThenoformofthiscommanddeletesapermanentstaticneighborentryfromtheARPtable.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
ipv4 <IPV4-ADDR> SpecifiestheIPaddressoftheneighbororthevirtualIPaddressof
theclusterinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255..Range:4096to131072.Default:131072.
mac <MAC-ADDR> SpecifiestheMACaddressoftheneighbororthemulticastMAC
addressinIANAformat(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
Example
ConfiguringastaticARPentryonainterfaceVLAN10:
| switch(config)#         |     | interface | vlan     | 10                            |
| ----------------------- | --- | --------- | -------- | ----------------------------- |
| switch(config-if-vlan)# |     |           | arp ipv4 | 2.2.2.2 mac 01:00:5e:00:00:01 |
RemovingastaticARPentryoninterfaceVLAN10:
| switch(config)# |     | interface | vlan | 10  |
| --------------- | --- | --------- | ---- | --- |
switch(config-if-vlan)# no arp ipv4 2.2.2.2 mac 01:00:5e:00:00:01
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
ARP|183

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |
| --- | -------------- | --- | --------------- |
clear arp
| clear arp | [port <PORT-ID> | | vrf {all-vrfs | | <VRF-NAME>}] |
| --------- | --------------- | --------------- | -------------- |
Description
ClearsIPv4andIPv6neighborentriesfromtheARPtable.Ifyoudonotspecifyanyparameters,ARPtable
entriesareclearedforthedefaultVRF.
| Parameter |           |     | Description                               |
| --------- | --------- | --- | ----------------------------------------- |
| port      | <PORT-ID> |     | Specifiesaphysicalportontheswitch.Format: |
member/slot/port.Forexample:1/1/1..
| all-vrfs   |     |     | SelectsallVRFs.                         |
| ---------- | --- | --- | --------------------------------------- |
| <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |
Examples
ClearingallIPv4andIPv6neighborARPentriesforthedefaultVRF:
| switch# | clear arp |     |     |
| ------- | --------- | --- | --- |
ClearingallARPneighborentriesforaport:
| switch# | clear arp 1/1/35 |     |     |
| ------- | ---------------- | --- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip local-proxy-arp
ip local-proxy-arp
no ip local-proxy-arp
Description
184
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |
| --------------------------- | ----- | ------------- | --- |

EnableslocalproxyARPonthespecifiedinterface.LocalproxyARPissupportedonLayer3physical
interfacesandonVLANinterfaces.ToenablelocalproxyARPonaninterface,routingmustbeenabledon
thatinterface.
ThenoformofthiscommanddisableslocalproxyARPonthespecifiedinterface.
Examples
EnablinglocalproxyARPoninterface1/1/1:
| switch#            | interface 1/1/1 |                    |     |
| ------------------ | --------------- | ------------------ | --- |
| switch(config-if)# |                 | ip local proxy-arp |     |
EnablinglocalproxyARPoninterfaceVLAN3:
| switch#                 | interface vlan | 3                  |     |
| ----------------------- | -------------- | ------------------ | --- |
| switch(config-if-vlan)# |                | ip local-proxy-arp |     |
DisablinglocalproxyARPononinterface1/1/1.
| switch#            | interface 1/1/1 |                       |     |
| ------------------ | --------------- | --------------------- | --- |
| switch(config-if)# |                 | no ip local-proxy-arp |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|                  | config-if-vlan |                | forthiscommand. |
| ---------------- | -------------- | -------------- | --------------- |
| ipv6 neighbor    | mac            |                |                 |
| ipv6 neighbor    | <IPV6-ADDR>    | mac <MAC-ADDR> |                 |
| no ipv6 neighbor | <IPV6-ADDR>    | mac <MAC-ADDR> |                 |
Description
SpecifiesapermanentstaticneighborentryintheARPtable(forIPv6neighbors).
ThenoformofthiscommanddeletesapermanentstaticneighborentryfromtheARPtable.
| Parameter    |     |     | Description                      |
| ------------ | --- | --- | -------------------------------- |
| <IPV6-ADDR>> |     |     | SpecifiesanIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
ARP|185

Parameter Description
mac <MAC-ADDR>> SpecifiestheMACaddressoftheneighbor
(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0
toF.Range:4096to131072.Default:131072.
Example
| CreatesastaticARPentryoninterface |           | 1/1/1. |
| --------------------------------- | --------- | ------ |
| switch(config)#                   | interface | 1/1/1  |
switch(config-if)# arp ipv6 neighbor 2001:0db8:85a3::8a2e:0370:7334 mac
00:50:56:96:df:c8
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip proxy-arp
ip proxy-arp
no ip proxy-arp
Description
EnablesproxyARPforthespecifiedLayer3interface.ProxyARPissupportedonLayer3physicalinterfaces,
LAGinterfaces,andVLANinterfaces.Itisdisabledbydefault.ToenableproxyARPonaninterface,routing
mustbeenabledonthatinterface.
ThenoformofthiscommanddisablesproxyARPforthespecifiedinterface.
Examples
EnablingproxyARPoninterface1/1/1:
| switch#            | interface 1/1/1 |     |
| ------------------ | --------------- | --- |
| switch(config-if)# | ip proxy-arp    |     |
EnablingproxyARPonVLAN3:
| switch#                 | interface vlan | 3            |
| ----------------------- | -------------- | ------------ |
| switch(config-if-vlan)# |                | ip proxy-arp |
EnablingproxyARPonaLAG11:
186
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| switch(config)#        | int | lag 11       |     |     |     |     |
| ---------------------- | --- | ------------ | --- | --- | --- | --- |
| switch(config-lag-if)# |     | ip proxy-arp |     |     |     |     |
DisablingproxyARPoninterface1/1/1:
| switch#            | interface | 1/1/1           |     |     |     |     |
| ------------------ | --------- | --------------- | --- | --- | --- | --- |
| switch(config-if)# |           | no ip proxy-arp |     |     |     |     |
CommandHistory
| Release        |     |     | Modification |     |     |     |
| -------------- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |     |
| --------- | -------------- | --- | --------- | --- | --- | --- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |     |     |     |
| --- | -------------- | --- | --------------- | --- | --- | --- |
config-lag-vlan
show arp
show arp
Description
ShowstheentriesintheARP(AddressResolutionProtocol)table.
Usage
ThiscommanddisplaysinformationaboutARPentries,includingtheIPaddress,MACaddress,port,and
state.
Whennoparametersarespecified,theshow arpcommandshowsallARPentriesforthedefaultVRF(Virtual
RouterForwarding)instance.
Examples
| switch#      | show arp |     |      |               |     |       |
| ------------ | -------- | --- | ---- | ------------- | --- | ----- |
| IPv4 Address | MAC      |     | Port | Physical Port |     | State |
-------------------------------------------------------------------------------
| 192.168.1.2  |        | 00:50:56:96:7b:e0 | vlan10 | 1/1/29 | stale     |     |
| ------------ | ------ | ----------------- | ------ | ------ | --------- | --- |
| 192.168.1.3  |        | 00:50:56:96:7b:ac | vlan10 | 1/1/1  | reachable |     |
| Total Number | Of ARP | Entries Listed-   | 2.     |        |           |     |
-------------------------------------------------------------------------------
CommandHistory
ARP|187

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show arp            | inspection | interface |     |
| ------------------- | ---------- | --------- | --- |
| show arp inspection | interface  |           |     |
Description
DisplaysthecurrentconfigurationofdynamicARPinspectiononaVLANorinterface.
Examples
| switch# | show arp inspection | interface |     |
| ------- | ------------------- | --------- | --- |
---------------------------------------------------------------------------
| Interface | Trust-State |     |     |
| --------- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 | Untrusted |     |     |
| ----- | --------- | --- | --- |
---------------------------------------------------------------------------
| switch# | show arp inspection | interface | vsx-peer |
| ------- | ------------------- | --------- | -------- |
---------------------------------------------------------------------------
| Interface | Trust-State |     |     |
| --------- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1  | Untrusted |     |     |
| ------ | --------- | --- | --- |
| lag100 | Trusted   |     |     |
---------------------------------------------------------------------------
| switch# | show arp inspection | interface | 1/1/1 |
| ------- | ------------------- | --------- | ----- |
---------------------------------------------------------------------------
| Interface | Trust-State |     |     |
| --------- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 | Untrusted |     |     |
| ----- | --------- | --- | --- |
---------------------------------------------------------------------------
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
188
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show arp            | inspection | statistics |     |     |
| ------------------- | ---------- | ---------- | --- | --- |
| show arp inspection | statistics |            |     |     |
Description
DisplaysstatisticsaboutforwardedanddroppedARPpackets.
Examples
| switch# | show arp inspection | statistics | vlan | 1-200 |
| ------- | ------------------- | ---------- | ---- | ----- |
-----------------------------------------------------------------
| VLAN | Name | Forwarded |     | Dropped |
| ---- | ---- | --------- | --- | ------- |
-----------------------------------------------------------------
| 1   | DEFAULT_VLAN_1 | 0   |     | 0   |
| --- | -------------- | --- | --- | --- |
-----------------------------------------------------------------
| switch# | show arp inspection | statistics | vlan |     |
| ------- | ------------------- | ---------- | ---- | --- |
-----------------------------------------------------------------
| VLAN | Name | Forwarded |     | Dropped |
| ---- | ---- | --------- | --- | ------- |
-----------------------------------------------------------------
| 1   | DEFAULT_VLAN_1 | 0   |     | 0   |
| --- | -------------- | --- | --- | --- |
| 200 | VLAN200        | 0   |     | 0   |
-----------------------------------------------------------------
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp | state |     |     |     |
| -------- | ----- | --- | --- | --- |
show arp state {all | failed | incomplete | permanent | reachable | stale}
Description
ShowsARP(AddressResolutionProtocol)cacheentriesthatareinthespecifiedstate.
ARP|189

| Parameter |     |     | Description                                    |     |     |
| --------- | --- | --- | ---------------------------------------------- | --- | --- |
| all       |     |     | ShowstheARPcacheentriesforallVRF(VirtualRouter |     |     |
Forwarding)instances.
| failed |     |     | ShowstheARPcacheentriesthatareinfailedstate.The |     |     |
| ------ | --- | --- | ----------------------------------------------- | --- | --- |
neighbormighthavebeendeleted.
| incomplete |     |     | ShowstheARPcacheentriesthatareinincompletestate. |     |     |
| ---------- | --- | --- | ------------------------------------------------ | --- | --- |
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
Examples
switch#
|              | show arp state | failed |      |               |       |
| ------------ | -------------- | ------ | ---- | ------------- | ----- |
| IPv4 Address | MAC            |        | Port | Physical Port | State |
---------------------------------------------------------------------------
| 192.168.1.4 |     |     | vlan10 |     | failed |
| ----------- | --- | --- | ------ | --- | ------ |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show arp         | summary   |                   |     |     |     |
| ---------------- | --------- | ----------------- | --- | --- | --- |
| show arp summary | [all-vrfs | | vrf <VRF-NAME>] |     |     |     |
Description
190
| AOS-CX10.09IPServicesGuide| | (6200 | SwitchSeries) |     |     |     |
| --------------------------- | ----- | ------------- | --- | --- | --- |

ShowsasummaryoftheIPv4andIPv6neighborentriesontheswitchforallVRFsoraspecificVRF.
| Parameter      |     |     | Description             |     |
| -------------- | --- | --- | ----------------------- | --- |
| all-vrfs       |     |     | SelectsallVRFs.         |     |
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |     |
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
| Number | of Reachable  | ARP entries | 25858 | 32168 |
| ------ | ------------- | ----------- | ----- | ----- |
| Number | of Stale ARP  | entries     | 0     | 3     |
| Number | of Failed     | ARP entries | 0     | 317   |
| Number | of Incomplete | ARP entries | 0     | 0     |
| Number | of Permanent  | ARP entries | 0     | 0     |
---------------------------------------------------------
| Total ARP | Entries- | 58346 | 25858 | 32488 |
| --------- | -------- | ----- | ----- | ----- |
---------------------------------------------------------
CommandHistory
ARP|191

| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp         | timeout       |     |     |     |
| ---------------- | ------------- | --- | --- | --- |
| show arp timeout | [<INTERFACE>] |     |     |     |
Description
Showstheage-outperiodforeachARP(AddressResolutionProtocol)entryforaport,LAG,orVLAN
interface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE> Specifiesaphysicalport,VLAN,orLAGontheswitch.Forphysical
ports,usetheformatmember/slot/port(forexample,1/3/1).
Examples
ShowingARPtimeoutinformationforaport:
| switch# | show arp timeout | 1/1/1 |     |     |
| ------- | ---------------- | ----- | --- | --- |
ARP Timeout:
------------------
| Port  | VRF     |     |     | Timeout |
| ----- | ------- | --- | --- | ------- |
| 1/1/1 | default |     |     | 600     |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
192
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| show arp           | vrf               |     |     |     |
| ------------------ | ----------------- | --- | --- | --- |
| show arp {all-vrfs | | vrf <VRF-NAME>} |     |     |     |
Description
ShowstheARPtableforallVRFinstances,orforthenamedVRF.
| Parameter |     | Description       |     |     |
| --------- | --- | ----------------- | --- | --- |
| all-vrfs  |     | SpecifiesallVRFs. |     |     |
vrf <VRF-NAME> SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
Examples
ShowingARPentriesforVRFtest.
| switch# show      | arp vrf test |     |     |     |
| ----------------- | ------------ | --- | --- | --- |
| ARP IPv4 Entries: |              |     |     |     |
-------------------------------------------------------
| IPv4 Address | MAC               | Port Physical | Port State | VRF  |
| ------------ | ----------------- | ------------- | ---------- | ---- |
| 10.20.30.40  | 00:50:56:bd:6a:c5 | 1/1/29 1/1/29 | reachable  | test |
-------------------------------------------------------
| Total Number | Of ARP Entries | Listed: 1. |     |     |
| ------------ | -------------- | ---------- | --- | --- |
-------------------------------------------------------
| switch# show      | arp all-vrfs |     |     |     |
| ----------------- | ------------ | --- | --- | --- |
| ARP IPv4 Entries: |              |     |     |     |
-------------------------------------------------------
| IPv4 Address   | MAC               | Port Physical | Port State | VRF  |
| -------------- | ----------------- | ------------- | ---------- | ---- |
| 192.168.120.10 | 00:50:56:bd:10:be | 1/1/32 1/1/32 | reachable  | red  |
| 10.20.30.40    | 00:50:56:bd:6a:c5 | 1/1/29 1/1/29 | reachable  | test |
-------------------------------------------------------
| Total Number | Of ARP Entries | Listed: 2. |     |     |
| ------------ | -------------- | ---------- | --- | --- |
-------------------------------------------------------
ShowingARPentriesforallVRFs.
| switch# show      | arp all-vrfs |     |     |     |
| ----------------- | ------------ | --- | --- | --- |
| ARP IPv4 Entries: |              |     |     |     |
-------------------------------------------------------
| IPv4 Address   | MAC               | Port Physical | Port State | VRF  |
| -------------- | ----------------- | ------------- | ---------- | ---- |
| 192.168.120.10 | 00:50:56:bd:10:be | 1/1/32 1/1/32 | reachable  | red  |
| 10.20.30.40    | 00:50:56:bd:6a:c5 | 1/1/29 1/1/29 | reachable  | test |
-------------------------------------------------------
| Total Number | Of ARP Entries | Listed: 2. |     |     |
| ------------ | -------------- | ---------- | --- | --- |
-------------------------------------------------------
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
ARP|193

| Platforms |     | Commandcontext |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show      | ipv6      | neighbors |       |             |     |     |     |
| --------- | --------- | --------- | ----- | ----------- | --- | --- | --- |
| show ipv6 | neighbors | {all-vrfs | | vrf | <VRF-NAME>} |     |     |     |
Description
ShowsentriesintheARPtableforallIPv6neighborsforallVRFsorforaspecificVRF.
Whennoparametersarespecified,thiscommandshowsallARPentriesforthedefaultVRF,andstate
informationforreachableandstaleentriesonly.
| Parameter |     |     |     | Description       |     |     |     |
| --------- | --- | --- | --- | ----------------- | --- | --- | --- |
| all-vrfs  |     |     |     | SpecifiesallVRFs. |     |     |     |
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
Examples
| switch# | show     | ipv6 neighbors |     |     |     |     |     |
| ------- | -------- | -------------- | --- | --- | --- | --- | --- |
| IPv6    | Entries: |                |     |     |     |     |     |
-------------------------------------------------------
| IPv6 | Address |     | MAC |     | Port | Physical Port | State |
| ---- | ------- | --- | --- | --- | ---- | ------------- | ----- |
fe80::a21d:48ff:fe8f:2700 a0:1d:48:8f:27:00 vlan2300 1/1/31 reachable
fe80::f603:43ff:fe80:a600 f4:03:43:80:a6:00 vlan2300 1/1/30 reachable
-------------------------------------------------------
| Total | Number | Of IPv6 Neighbors |     | Entries Listed: | 2.  |     |     |
| ----- | ------ | ----------------- | --- | --------------- | --- | --- | --- |
-------------------------------------------------------
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
(#)
194
| AOS-CX10.09IPServicesGuide| |     | (6200 SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- | --- |

show ipv6 neighbors state
show ipv6 neighbors state {all | failed | incomplete | permanent | reachable | stale}

Description

Shows all IPv6 neighbor ARP (Address Resolution Protocol) cache entries, or those cache entries that are in
the specified state.

Parameter

all

failed

incomplete

permanent

reachable

stale

Example

Description

Shows all ARP cache entries.

Shows ARP cache entries that are in failed state. The neighbor
might have been deleted. Set the neighbor to be unreachable.

Shows ARP cache entries that are in incomplete state.
An incomplete state means that address resolution is in progress
and the link-layer address of the neighbor has not yet been
determined. This means that a solicitation request was sent, and
you are waiting for a solicitation reply or a timeout.

Shows ARP cache entries that are in permanent state.

Shows ARP cache entries that are in reachable state, meaning
that the neighbor is known to have been reachable recently.

Shows ARP cache entries that are in stale state.
ARP cache entries are in the stale state if the elapsed time is in
excess of the ARP timeout in seconds since the last positive
confirmation that the forwarding path was functioning properly.

switch# show ipv6 neighbors state all

MAC

IPv6 Address
State
--------------------------------------------------------------------------------
100::2
300::3
fe80::4a0f:cfff:feaf:f1cc
200::3
fe80::4a0f:cfff:feaf:33be

48:0f:cf:af:f1:cc lag1
48:0f:cf:af:33:be vlan3
48:0f:cf:af:f1:cc lag1
48:0f:cf:af:33:be 1/4/11
48:0f:cf:af:33:be vlan3

lag1
1/4/20
lag1
1/4/11
1/4/20

reachable
reachable
reachable
reachable
reachable

Physical Port

Port

Total Number Of IPv6 Neighbors Entries Listed- 5.
---------------------------------------------------------------------------------

Command History

Release

10.07 or earlier

Command Information

Modification

--

ARP | 195

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
196
| AOS-CX10.09IPServicesGuide| | (6200 SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

Support and Other Resources

Chapter 12

Support and Other Resources

Accessing Aruba Support

Aruba Support Services

https://www.arubanetworks.com/support-services/

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

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.htm

Airheads social
forums and
Knowledge
Base

AOS-CX Switch
Software
Documentation
Portal

Aruba
Hardware
Documentation
and
Translations

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

197

Portal

Aruba software

https://asp.arubanetworks.com/downloads

Software
licensing

End-of-Life
information

Aruba
Developer Hub

https://lms.arubanetworks.com/

https://www.arubanetworks.com/support-services/end-of-life/

https://developer.arubanetworks.com/

Accessing Updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My Networking,
where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to the
Hewlett Packard Enterprise Support Center More Information on Access to Support Materials page:

https://support.hpe.com/portal/site/hpsc/aae/home/

Access to some updates might require product entitlement when accessed through the Hewlett Packard
Enterprise Support Center. You must have an HP Passport set up with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal (ASP)
account to manage subscriptions). Security notices are viewable without an ASP account.

Warranty Information
To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Regulatory Information
To view the regulatory information for your product, view the Safety and Compliance Information for Server,
Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Support and Other Resources | 198

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs, product
recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For more
information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.09 IP Services Guide | (6200 Switch Series)

199