AOS-CX 10.11 IP Services
Guide

6200 Switch Series

Published: February 2023
Edition: 2

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General
Public License, and/or certain other open source licenses. A complete machine-readable copy of the
source code corresponding to such code is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, send a check or
money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

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

| 2

Contents
Contents
| Contents                            |                                     | 3   |
| ----------------------------------- | ----------------------------------- | --- |
| About this                          | document                            | 9   |
| Applicableproducts                  |                                     | 9   |
| Latestversionavailableonline        |                                     | 9   |
| Commandsyntaxnotationconventions    |                                     | 9   |
| Abouttheexamples                    |                                     | 10  |
| Identifyingswitchportsandinterfaces |                                     | 10  |
| IRDP                                |                                     | 12  |
| ConfiguringIRDP                     |                                     | 13  |
| IRDPcommands                        |                                     | 14  |
|                                     | diag-dumpirdpbasic                  | 14  |
|                                     | ipirdp                              | 15  |
|                                     | ipirdpholdtime                      | 15  |
|                                     | ipirdpmaxadvertinterval             | 16  |
|                                     | ipirdpminadvertinterval             | 17  |
|                                     | ipirdppreference                    | 18  |
|                                     | showipirdp                          | 19  |
| IPv6 Router                         | Advertisement                       | 20  |
| ConfiguringIPv6RA                   |                                     | 20  |
| IPv6RAscenario                      |                                     | 22  |
| IPv6RAcommands                      |                                     | 22  |
|                                     | ipv6address<global-unicast-address> | 23  |
|                                     | ipv6addressautoconfig               | 23  |
|                                     | ipv6addresslink-local               | 24  |
|                                     | ipv6ndcache-limit                   | 25  |
|                                     | ipv6nddadattempts                   | 26  |
|                                     | ipv6ndhop-limit                     | 27  |
|                                     | ipv6ndmtu                           | 27  |
|                                     | ipv6ndns-interval                   | 28  |
|                                     | ipv6ndprefix                        | 28  |
|                                     | ipv6ndradnssearch-list              | 30  |
|                                     | ipv6ndradnsserver                   | 31  |
|                                     | ipv6ndralifetime                    | 32  |
|                                     | ipv6ndramanaged-config-flag         | 33  |
|                                     | ipv6ndramax-interval                | 34  |
|                                     | ipv6ndramin-interval                | 35  |
|                                     | ipv6ndraother-config-flag           | 35  |
|                                     | ipv6ndrareachable-time              | 36  |
|                                     | ipv6ndraretrans-timer               | 37  |
|                                     | ipv6ndroute                         | 38  |
|                                     | ipv6ndrouter-preference             | 39  |
|                                     | ipv6ndsuppress-ra                   | 39  |
|                                     | showipv6ndglobaltraffic             | 40  |
|                                     | showipv6ndinterface                 | 41  |
|                                     | showipv6ndinterfaceprefix           | 43  |
3
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

show ipv6 nd interface route
show ipv6 nd ra dns search-list
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

Protocol and feature details
Supported platform and standards
Configuration task list
Considerations and best practices
Use case
DHCP client commands

ip dhcp
show ip dhcp

DHCP relay agent

Supported platform and standards
DHCPv4 relay agent

Configuring the DHCPv4 relay agent
Use Case
DHCPv4 relay commands

DHCPv6 relay agent

Configuring the DHCPv6 relay agent
Use Case
DHCP relay (IPv6) commands

Troubleshooting

DHCP server

Protocol and feature details
Supported platform and standards
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

44
45
46

47
47
48
49
50
53
53
53
55
56
57
57
58
59
60
60
61

64
64
64
64
64
64
65
66
66
67
68
68
68
69
70
75
84
84
85
87
91
93
93
93
94
95
96
96
97
98
99
100
101
102

Contents | 4

dns-server
domain-name
enable
lease
netbios-name-server
netbios-node-type
option
pool
range
show dhcp-server
static-bind

DHCP server IPv6 commands

authoritative
clear dhcpv6-server leases
dhcpv6-server external-storage
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

Troubleshooting

FAQ

DHCP snooping
Protocol details
Supported platform and standards
Use case
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

102
103
104
104
105
106
107
108
109
110
112
113
113
114
115
116
117
117
118
119
120
121
121
122
125
126
126

129
130
130
130
133
133
134
135
136
137
137
138
139
140
142
142
144
145
145
146
148
149
150
150
151
152
152
153

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

5

dhcpv6-snooping authorized-server
dhcpv6-snooping event-log client
dhcpv6-snooping external-storage
dhcpv6-snooping flash-storage
dhcpv6-snooping max-bindings
dhcpv6-snooping trust
match server access-list
match client prefix-list
preference
show dhcpv6-snooping
show dhcpv6-snooping binding
dhcpv6-snooping guard-policy
show dhcpv6-snooping guard-policy
show dhcpv6-snooping guard-policy interface
show dhcpv6-snooping guard-policy vlan
show dhcpv6-snooping statistics

Troubleshooting

DHCP Options

DHCP options commands

http-proxy

ND snooping
Overview
ND snooping commands

clear nd-snooping binding
clear nd-snooping ra-guard-policy statistics
clear nd-snooping statistics
nd-snooping
nd-snooping (in config-vlan context)
nd-snooping mac-check
nd-snooping prefix-list
nd-snooping max-bindings
nd-snooping nd-guard
nd-snooping ra-guard
nd-snooping ra-drop
nd-snooping trust
show nd-snooping
show nd-snooping binding
show nd-snooping prefix-list
show nd-snooping statistics

RA guard policy commands

hop limit
ipv6 nd-snooping ra-guard policy
managed-config-flag
match access-list
match prefix-list
nd-snooping ra-guard attach-policy
other-config-flag
router-preference
show nd-snooping ra-guard interface
show nd-snooping ra-guard policy
show nd-snooping ra-guard vlan

IPv6 destination guard

IPv6 destination guard commands

154
155
156
157
158
159
160
161
161
162
164
164
165
167
167
168
169

171
171
171

173
173
173
174
175
175
176
177
177
178
179
180
181
182
183
183
185
185
186
187
187
188
189
190
191
191
193
194
195
196
197

199
199

Contents | 6

|                                                       | clearipv6destination-guardstatisticsvlan |         |          |        | 199 |
| ----------------------------------------------------- | ---------------------------------------- | ------- | -------- | ------ | --- |
|                                                       | ipv6destinationguard                     |         |          |        | 200 |
|                                                       | showipv6destination-guardstatisticsvlan  |         |          |        | 200 |
|                                                       | showipv6destination-guard                |         |          |        | 201 |
| IP Tunnels                                            |                                          |         |          |        | 203 |
| ConfiguringanIPtunnel                                 |                                          |         |          |        | 203 |
| CreatinganIPv6inIPv4tunnelfortraversingapublicnetwork |                                          |         |          |        | 204 |
| CreatinganIPv6inIPv6tunnelfortraversingapublicnetwork |                                          |         |          |        | 205 |
| IPtunnelscommands                                     |                                          |         |          |        | 206 |
|                                                       | description                              |         |          |        | 206 |
|                                                       | destinationip                            |         |          |        | 207 |
|                                                       | destinationipv6                          |         |          |        | 208 |
|                                                       | interfacetunnel                          |         |          |        | 209 |
|                                                       | ipaddress                                |         |          |        | 210 |
|                                                       | ipv6address                              |         |          |        | 211 |
|                                                       | ipmtu                                    |         |          |        | 212 |
|                                                       | showinterfacetunnel                      |         |          |        | 213 |
|                                                       | showrunning-configinterfacetunnel        |         |          |        | 214 |
|                                                       | shutdown                                 |         |          |        | 215 |
|                                                       | sourceip                                 |         |          |        | 216 |
|                                                       | sourceipv6                               |         |          |        | 217 |
|                                                       | ttl                                      |         |          |        | 217 |
| Internet                                              | Control                                  | Message | Protocol | (ICMP) | 219 |
| ICMPmessagetypes                                      |                                          |         |          |        | 219 |
| WhenICMPmessagesaresent                               |                                          |         |          |        | 219 |
| ICMPredirectmessages                                  |                                          |         |          |        | 220 |
| WhenICMPredirectmessagesaresent                       |                                          |         |          |        | 220 |
| ICMPcommands                                          |                                          |         |          |        | 220 |
|                                                       | ipicmpredirect                           |         |          |        | 220 |
|                                                       | ipicmpthrottle                           |         |          |        | 221 |
|                                                       | ipicmpunreachable                        |         |          |        | 222 |
| DNS                                                   |                                          |         |          |        | 223 |
| DNSclient                                             |                                          |         |          |        | 223 |
| ConfiguringtheDNSclient                               |                                          |         |          |        | 223 |
| DNSclientcommands                                     |                                          |         |          |        | 224 |
|                                                       | ipdnsdomain-list                         |         |          |        | 224 |
|                                                       | ipdnsdomain-name                         |         |          |        | 225 |
|                                                       | ipdnshost                                |         |          |        | 226 |
|                                                       | ipdnsserveraddress                       |         |          |        | 227 |
|                                                       | showipdns                                |         |          |        | 228 |
| ARP                                                   |                                          |         |          |        | 229 |
| ConfiguringproxyARP                                   |                                          |         |          |        | 230 |
| ConfiguringlocalproxyARP                              |                                          |         |          |        | 230 |
| ARPcommands                                           |                                          |         |          |        | 231 |
|                                                       | arpinspection                            |         |          |        | 231 |
|                                                       | arpinspectiontrust                       |         |          |        | 231 |
|                                                       | arpipv4mac                               |         |          |        | 232 |
|                                                       | arpprocess-grat-arp                      |         |          |        | 233 |
|                                                       | cleararp                                 |         |          |        | 234 |
|                                                       | debugarp-security                        |         |          |        | 235 |
|                                                       | iplocal-proxy-arp                        |         |          |        | 236 |
|                                                       | ipproxy-arp                              |         |          |        | 237 |
7
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

|                       | ipv6neighbormac             |           | 238 |
| --------------------- | --------------------------- | --------- | --- |
|                       | showarp                     |           | 239 |
|                       | showarpinspectioninterface  |           | 239 |
|                       | showarpinspectionstatistics |           | 240 |
|                       | showarpinspectionvlan       |           | 241 |
|                       | showarpstate                |           | 242 |
|                       | showarpsummary              |           | 243 |
|                       | showarptimeout              |           | 245 |
|                       | showarpvrf                  |           | 245 |
|                       | showipv6neighbors           |           | 246 |
|                       | showipv6neighborsstate      |           | 247 |
|                       | showtecharp-security        |           | 249 |
| Support               | and Other                   | Resources | 251 |
| AccessingArubaSupport |                             |           | 251 |
| AccessingUpdates      |                             |           | 252 |
|                       | ArubaSupportPortal          |           | 252 |
|                       | MyNetworking                |           | 252 |
| WarrantyInformation   |                             |           | 252 |
| RegulatoryInformation |                             |           | 252 |
| DocumentationFeedback |                             |           | 253 |
Contents|8

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba6200SwitchSeries(JL724A,JL725A,JL726A,JL727A,JL728A,R8Q67A,R8Q68A,R8Q69A,R8Q70A,
R8Q71A,R8V08A,R8V09A,R8V10A,R8V11A,R8V12A,R8Q72A)
| Latest | version | available | online |
| ------ | ------- | --------- | ------ |
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
| Command    | syntax | notation | conventions |
| ---------- | ------ | -------- | ----------- |
| Convention |        | Usage    |             |
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Items
thatappearliketheexampletextinthepreviouscolumnaretobeentered
exactlyasshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
<example-text> substitutewithanactualvalueinacommandorincode:
n
n <example-text>
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variables |     |
| --- | --- | ------------------------------------------------------------ | --- |
n example-text
areenclosedinanglebrackets(< >).Substitutethetext—including
n example-text
theenclosinganglebrackets—withanactualvalue.
|     |     | n Foroutputformatswhereitalictextcanbedisplayed,variables |     |
| --- | --- | --------------------------------------------------------- | --- |
mightormightnotbeenclosedinanglebrackets.Substitutethe
textincludingtheenclosinganglebrackets,ifany,withanactual
value.
| Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
9
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Convention |     | Usage                                                    |     |
| ---------- | --- | -------------------------------------------------------- | --- |
| [ ]        |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| …or        |     | Ellipsis:                                                |     |
... n Incodeandscreenexamples,averticalorhorizontalellipsisindicatesan
omissionofinformation.
n Insyntaxusingbracketsandbraces,anellipsisindicatesitemsthatcanbe
repeated.Whenanitemfollowedbyellipsesisenclosedinbrackets,zero
ormoreitemscanbespecified.
| About the | examples |     |     |
| --------- | -------- | --- | --- |
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchor
environment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understanding | the CLI prompts |     |     |
| ------------- | --------------- | --- | --- |
Whenillustratingthepromptsinthecommandlineinterface(CLI),thisdocumentusesthegenericterm
switch,insteadofthehostnameoftheswitch.Forexample:
switch>
TheCLIpromptindicatesthecurrentcommandcontext.Forexample:
switch>
Indicatestheoperatorcommandcontext.
switch#
Indicatesthemanagercommandcontext.
switch(CONTEXT-NAME)#
Indicatestheconfigurationcontextforafeature.Forexample:
switch(config-if)#
Identifiestheinterfacecontext.
| Variable information | in  | CLI prompts |     |
| -------------------- | --- | ----------- | --- |
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,whenin
theVLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 6200 Switch | Series |     |     |
| ------------------ | ------ | --- | --- |
Aboutthisdocument|10

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

11

Chapter 2

IRDP

IRDP

ICMP Router Discovery Protocol (IRDP), an extension of the ICMP, is independent of any routing
protocol. It allows hosts to discover the IP addresses of neighboring routers that can act as default
gateways to reach devices on other IP networks.

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

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

12

Destination address of RA

An RA uses either of the following destination IP addresses:

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

n Enables IRDP on the layer 3 VLAN interface 2 with packet type set to broadcast.

n Sets the hold time to 5000 seconds.

n Sets the advertisement interval to 30 seconds.

n Sets the minimum advertisement interval to 25 seconds.

n Sets the IRDP preference level to 25.

IRDP | 13

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
| switch# | diag-dump |     | irdp basic |     |     |     |     |
| ------- | --------- | --- | ---------- | --- | --- | --- | --- |
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
| Diagnostic-dump |             | captured | for     | feature | irdp         |     |     |
| --------------- | ----------- | -------- | ------- | ------- | ------------ | --- | --- |
| Command         | History     |          |         |         |              |     |     |
| Release         |             |          |         |         | Modification |     |     |
| 10.07orearlier  |             |          |         |         | --           |     |     |
| Command         | Information |          |         |         |              |     |     |
| Platforms       | Command     |          | context |         | Authority    |     |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
14
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

ip irdp
| ip irdp [broadcast | | multicast] |     |     |
| ------------------ | ------------ | --- | --- |
no ip irdp
Description
EnablesIRDPonaninterfaceandspecifiesthepackettypethatisusedtosendadvertisements.By
default,thepackettypeissettomulticast.IRDPisonlysupportedonlayer3interfaces.
ThenoformofthiscommanddisablesIRDPonaninterface.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
broadcast
AdvertisementsaresentasbroadcastpacketstoIPaddress
255.255.255.255.
multicast Advertisementsaresentasmulticastpacketstothemulticast
groupwithIPaddress24.0.0.1.Default.
Examples
EnablingIRDPoninterfacevlan2withpackettypesettothedefaultvalue(multicast).
| switch(config)#         | interface | vlan    | 2   |
| ----------------------- | --------- | ------- | --- |
| switch(config-if-vlan)# |           | ip irdp |     |
EnablingIRDPoninterface1/1/1withpackettypesettobroadcast.
| switch(config)#         | interface | vlan    | 2         |
| ----------------------- | --------- | ------- | --------- |
| switch(config-if-vlan)# |           | ip irdp | broadcast |
DisablingIRDP.
| switch(config)#         | interface | vlan       | 2            |
| ----------------------- | --------- | ---------- | ------------ |
| switch(config-if-vlan)# |           | no ip irdp |              |
| Command History         |           |            |              |
| Release                 |           |            | Modification |
| 10.07orearlier          |           |            | --           |
| Command Information     |           |            |              |
| Platforms               | Command   | context    | Authority    |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp holdtime    |        |     |     |
| ------------------- | ------ | --- | --- |
| ip irdp holdtime    | <TIME> |     |     |
| no ip irdp holdtime | <TIME> |     |     |
IRDP|15

Description
Specifiesthemaximumamountoftimethehostwillconsideranadvertisementtobevaliduntilanewer
advertisementarrives.Whenanewadvertisementarrives,holdtimeisreset.Holdtimemustbegreater
thanorequaltothemaximumadvertisementinterval.Therefore,iftheholdtimeforanadvertisement
expires,thehostcanreasonablyconcludethattherouterinterfacethatsenttheadvertisementisno
longeravailable.Thedefaultholdtimeisthreetimesthemaximumadvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumamountoftimethehostwillconsideran
advertisementtobevaliduntilaneweradvertisementarrivesandupdateittothedefaultvalue.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<TIME> Specifiesthelifetimeofrouteradvertisementssentfromthis
interface.Range:4to9000seconds.Default:1800seconds.
Example
SettingtheholdtimeforVLANinterface2to5000seconds:
| switch(config)#         |     | interface | vlan    | 2        |      |
| ----------------------- | --- | --------- | ------- | -------- | ---- |
| switch(config-if-vlan)# |     |           | ip irdp | holdtime | 5000 |
RemovingthetheholdtimeforVLANinterface2to5000seconds:
| switch(config)#         |             | interface | vlan       | 2            |      |
| ----------------------- | ----------- | --------- | ---------- | ------------ | ---- |
| switch(config-if-vlan)# |             |           | no ip irdp | holdtime     | 5000 |
| Command                 | History     |           |            |              |      |
| Release                 |             |           |            | Modification |      |
| 10.07orearlier          |             |           |            | --           |      |
| Command                 | Information |           |            |              |      |
| Platforms               | Command     |           | context    | Authority    |      |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp    | maxadvertinterval |     |        |     |     |
| ---------- | ----------------- | --- | ------ | --- | --- |
| ip irdp    | maxadvertinterval |     | <TIME> |     |     |
| no ip irdp | maxadvertinterval |     | <TIME> |     |     |
Description
Specifiesthemaximumrouteradvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumrouteradvertisementintervaland
revertstothedefaultvalue.
16
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

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
| switch(config)#         |             | interface | vlan       | 2                 |     |
| ----------------------- | ----------- | --------- | ---------- | ----------------- | --- |
| switch(config-if-vlan)# |             |           | no ip irdp | maxadvertinterval | 30  |
| Command                 | History     |           |            |                   |     |
| Release                 |             |           |            | Modification      |     |
| 10.07orearlier          |             |           |            | --                |     |
| Command                 | Information |           |            |                   |     |
| Platforms               | Command     |           | context    | Authority         |     |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
IRDP|17

SettingtheminimumadvertisementintervalforVLANinterface2to25seconds:
| switch(config)#         |     | interface | vlan    | 2                 |     |     |
| ----------------------- | --- | --------- | ------- | ----------------- | --- | --- |
| switch(config-if-vlan)# |     |           | ip irdp | minadvertinterval |     | 25  |
RemovingtheminimumadvertisementintervalforVLANinterface2to25seconds:
| switch(config)#         |             | interface | vlan       | 2                 |     |     |
| ----------------------- | ----------- | --------- | ---------- | ----------------- | --- | --- |
| switch(config-if-vlan)# |             |           | no ip irdp | minadvertinterval |     | 25  |
| Command                 | History     |           |            |                   |     |     |
| Release                 |             |           |            | Modification      |     |     |
| 10.07orearlier          |             |           |            | --                |     |     |
| Command                 | Information |           |            |                   |     |     |
| Platforms               | Command     |           | context    | Authority         |     |     |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
SettingtheIRDPpreferencelevelforVLANinterface2to25.
| switch(config)#         |     | interface | vlan    | 2          |     |     |
| ----------------------- | --- | --------- | ------- | ---------- | --- | --- |
| switch(config-if-vlan)# |     |           | ip irdp | preference | 25  |     |
RemovingtheIRDPpreferencelevelforVLANinterface2to25.
18
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

| switch(config)# |     | interface | vlan | 2   |     |     |
| --------------- | --- | --------- | ---- | --- | --- | --- |
switch(config-if-vlan)#
|                     |         |     | no ip irdp | preference   | 25  |     |
| ------------------- | ------- | --- | ---------- | ------------ | --- | --- |
| Command History     |         |     |            |              |     |     |
| Release             |         |     |            | Modification |     |     |
| 10.07orearlier      |         |     |            | --           |     |     |
| Command Information |         |     |            |              |     |     |
| Platforms           | Command |     | context    | Authority    |     |     |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip irdp |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
show ip irdp
Description
DisplaysIRDPconfigurationsettings.
Example
| switch#     | sh ip     | irdp |          |     |     |     |
| ----------- | --------- | ---- | -------- | --- | --- | --- |
| ICMP Router | Discovery |      | Protocol |     |     |     |
Interface Status Advertising Minimum Maximum Holdtime Preference
|     |     |     | Address | Interval | Interval |     |
| --- | --- | --- | ------- | -------- | -------- | --- |
--------------- -------- ----------- -------- -------- -------- -----------
| vlan1               |         | Disabled | multicast | 450          | 600 | 1800 0 |
| ------------------- | ------- | -------- | --------- | ------------ | --- | ------ |
| bridge_normal       |         | Disabled | multicast | 450          | 600 | 1800 0 |
| Command History     |         |          |           |              |     |        |
| Release             |         |          |           | Modification |     |        |
| 10.07orearlier      |         |          |           | --           |     |        |
| Command Information |         |          |           |              |     |        |
| Platforms           | Command |          | context   | Authority    |     |        |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
IRDP|19

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
20
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

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
IPv6RouterAdvertisement|21

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

IPv6 RA commands

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

22

| ipv6 address    | <global-unicast-address> |     |     |     |
| --------------- | ------------------------ | --- | --- | --- |
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
| switch(config)#    | interface |      | 1/1/1   |                    |
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
Allplatforms config-if OperatorsorAdministratorsorlocalusergroupmemberswith
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
IPv6RouterAdvertisement|23

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
Allplatforms config-if OperatorsorAdministratorsorlocalusergroupmemberswith
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
24
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------- | --- | ------------------ | --- | --- |

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
IPv6RouterAdvertisement|25

| switch(config)# |             | ipv6 | nd cache-limit |     | 20           |
| --------------- | ----------- | ---- | -------------- | --- | ------------ |
| Command         | History     |      |                |     |              |
| Release         |             |      |                |     | Modification |
| 10.07orearlier  |             |      |                |     | --           |
| Command         | Information |      |                |     |              |
| Platforms       | Command     |      | context        |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | dad             | attempts       |                  |     |     |
| ------- | --------------- | -------------- | ---------------- | --- | --- |
| ipv6 nd | dad attempts    | <NUM-ATTEMPTS> |                  |     |     |
| no ipv6 | nd dad attempts |                | [<NUM-ATTEMPTS>] |     |     |
Description
Configuresthenumberofneighborsolicitationstobesentwhenperformingduplicateaddress
detection(DAD)foraunicastaddressconfiguredonaninterface.Iftheactivegatewayisconfiguredwith
thesameIPasanSVIIP,thenIPv6DADcannotbeconfigured.
Thenoformofthiscommandsetsthenumberofattemptstothedefaultvalue.
| Parameter    |                |     |     |     | Description |
| ------------ | -------------- | --- | --- | --- | ----------- |
| dad attempts | <NUM-ATTEMPTS> |     |     |     |             |
Specifiesthenumberofneighborsolicitationstosend.Range:0-
15.Default:1.
Examples
| switch(config)#    |             | interface | 1/1/1       |          |              |
| ------------------ | ----------- | --------- | ----------- | -------- | ------------ |
| switch(config-if)# |             |           | ipv6 nd dad | attempts | 5            |
| Command            | History     |           |             |          |              |
| Release            |             |           |             |          | Modification |
| 10.07orearlier     |             |           |             |          | --           |
| Command            | Information |           |             |          |              |
| Platforms          | Command     |           | context     |          | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
26
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

| ipv6 nd | hop-limit    |              |     |     |     |
| ------- | ------------ | ------------ | --- | --- | --- |
| ipv6 nd | hop-limit    | <HOPLIMIT>   |     |     |     |
| no ipv6 | nd hop-limit | [<HOPLIMIT>] |     |     |     |
Description
ConfiguresthehoplimittobesentinRAs.
Thenoformofthiscommandresetsthehoplimitto0.ThisreseteliminatesthehoplimitfromtheRAs
thatoriginateontheinterface,sothehostdeterminesthehoplimit.
| Parameter |            |     |     |     | Description |
| --------- | ---------- | --- | --- | --- | ----------- |
| hop-limit | <HOPLIMIT> |     |     |     |             |
Specifiesthehoplimit.Range:0-255.Default:64.
Examples
| switch(config)#    |             | interface | 1/1/1             |     |              |
| ------------------ | ----------- | --------- | ----------------- | --- | ------------ |
| switch(config-if)# |             |           | ipv6 nd hop-limit |     | 64           |
| Command            | History     |           |                   |     |              |
| Release            |             |           |                   |     | Modification |
| 10.07orearlier     |             |           |                   |     | --           |
| Command            | Information |           |                   |     |              |
| Platforms          | Command     |           | context           |     | Authority    |
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
| switch(config)#    |     | interface | 1/1/1       |      |     |
| ------------------ | --- | --------- | ----------- | ---- | --- |
| switch(config-if)# |     |           | ipv6 nd mtu | 1300 |     |
IPv6RouterAdvertisement|27

| Command |                | History     |     |         |              |     |
| ------- | -------------- | ----------- | --- | ------- | ------------ | --- |
|         | Release        |             |     |         | Modification |     |
|         | 10.07orearlier |             |     |         | --           |     |
| Command |                | Information |     |         |              |     |
|         | Platforms      | Command     |     | context | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
|         | Platforms          | Command     |           | context             | Authority    |      |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 | nd                | prefix                          |          |                  |     |              |
| ---- | ----------------- | ------------------------------- | -------- | ---------------- | --- | ------------ |
| ipv6 | nd                | prefix <IPV6-ADDR>/<PREFIX-LEN> |          |                  |     |              |
|      | [no-advertise     |                                 | | [valid | <LIFETIME-VALUE> |     | preferred    |
|      | <LIFETIME-VALUE>] |                                 |          | | no-autoconfig  |     | | no-onlink] |
28
| AOS-CX10.11IPServicesGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- |

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
SpecifiesprefixesfortheroutingswitchtoincludeinRAstransmittedontheinterface.IPv6hostsuse
theprefixesinRAstoautoconfigurethemselveswithglobalunicastaddresses.Theautoconfigured
addressofahostiscomposedoftheadvertisedprefixandtheinterfaceidentifierinthecurrentlink-
localaddressofthehost.
Bydefault,advertise,autoconfig,andonlinkareset.
Thenoformofthiscommandremovestheconfigurationontheinterface.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<IPV6-ADDR>/<PREFIX-LEN> SpecifiestheIPv6prefixtoadvertiseinRA.Format:X:X::X:X/M
default Specifiesapplyconfigurationtoallon-linkprefixesthatarenot
|     |     |     | individuallysetbytheipv6 |     | ra prefix | <IPV6- |
| --- | --- | --- | ------------------------ | --- | --------- | ------ |
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
no-advertise
SpecifiesdonotadvertiseprefixinRA.
valid <LIFETIME-VALUE> Specifiesthetotaltime,inseconds,theprefixremainsavailable
beforebecomingunusable.Afterpreferred-lifetimeexpiration,
anyautoconfiguredaddressisdeprecatedandusedonlyfor
transactionsonlybeforepreferred-lifetimeexpires.Ifthevalid
lifetimeexpires,theaddressbecomesinvalid.
|     |     |     | Youcanenteravalueinsecondsorentervalid |     |     | infinite |
| --- | --- | --- | -------------------------------------- | --- | --- | -------- |
whichsetsinfinitelifetime.Default:2,592,000secondswhichis30
days.Range:0–4294967294seconds.
preferred <LIFETIME-VALUE> Specifiesthespanoftimeduringwhichtheaddresscanbefreely
usedasasourceanddestinationfortraffic.Thissettingmustbe
lessthanorequaltothecorrespondingvalid–lifetimesetting.
Youcanenteravalueinsecondsorenterpreferred infinite
whichsetsinfinitelifetime.Default:604,800secondswhichis
sevendays.Range:0–4294967294seconds.
| no-autoconfig |     |     | Specifiesdonotuseprefixforautoconfiguration.   |     |     |     |
| ------------- | --- | --- | ---------------------------------------------- | --- | --- | --- |
| no-onlink     |     |     | Specifiesdonotuseprefixforonlinkdetermination. |     |     |     |
IPv6RouterAdvertisement|29

Examples
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# ipv6 nd prefix 4001::1/64 valid 30 preferred 10 no-autoconfig
no-onlink
| Command        | History     |     |         |              |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| Release        |             |     |         | Modification |     |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
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
n DNSSLcontainsthedomainnamesofDNSsuffixesorIPv6hoststoappendtoshort,unqualified
domainnamesforDNSqueries.
n MultipleDNSdomainnamescanbeaddedtotheDNSSLbyusingthecommandrepeatedly.
n Amaximumofeightserveraddressesareallowed.
Examples
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# ipv6 nd ra dns search-list test.com lifetime 500
| Command | History |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
30
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

| Release        |             |         | Modification |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
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
n IncludingRDNSSinformationinRAsprovidesDNSserverconfigurationforconnectedIPv6hosts
withoutrequiringDHCPv6.
n Multipleserverscanbeconfiguredontheinterfacebyusingthecommandrepeatedly.
n Amaximumofeightserveraddressesareallowed.
Examples
switch(config)#
|                    |         | interface 1/1/1 |               |                  |     |
| ------------------ | ------- | --------------- | ------------- | ---------------- | --- |
| switch(config-if)# |         | ipv6 nd         | ra dns server | 2001::1 lifetime | 400 |
| Command            | History |                 |               |                  |     |
IPv6RouterAdvertisement|31

| Release        |             |     |         | Modification |
| -------------- | ----------- | --- | ------- | ------------ |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
32
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------- | --- | ------------------ | --- | --- |

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd ra                     | managed-config-flag |     |     |     |     |
| ------------------------------ | ------------------- | --- | --- | --- | --- |
| ipv6 nd ra managed-config-flag |                     |     |     |     |     |
| no ipv6 nd ra                  | managed-config-flag |     |     |     |     |
Description
ControlstheMflagsettinginRAstheroutertransmitsonthecurrentinterface.EnabletheMflagto
indicatethathostscanobtainIPaddressthroughDHCPv6.TheMflagisdisabledbydefault.
Thenoformofthiscommandturnsoff(disables)theMflag.
Usage
n EnablingtheMflagdirectshoststoacquiretheirIPv6addressingforthecurrentinterfacefroma
DHCPv6server.
n WhentheM-bitisenabled,receivinghostsignoretheOflagsetting,whichisconfiguredusingthe
| commandipv6 | nd  | ra other-config-flag. |     |     |     |
| ----------- | --- | --------------------- | --- | --- | --- |
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
| switch(config)#    |     | interface | 1/1/1                     |     |     |
| ------------------ | --- | --------- | ------------------------- | --- | --- |
| switch(config-if)# |     | ipv6      | nd ra managed-config-flag |     |     |
| Command History    |     |           |                           |     |     |
IPv6RouterAdvertisement|33

| Release        |             |     |         | Modification |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra max-interval    |     |          |     |     |
| ------- | ------------------ | --- | -------- | --- | --- |
| ipv6 nd | ra max-interval    |     | <TIME>   |     |     |
| no ipv6 | nd ra max-interval |     | [<TIME>] |     |     |
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
n Attemptingtosetmax-intervaltoavaluethatisnotsufficientlylargerthanthecurrentmin-interval
alsoresultsinanerrormessage.
Examples
| switch(config)#    |             | interface | 1/1/1   |                 |     |
| ------------------ | ----------- | --------- | ------- | --------------- | --- |
| switch(config-if)# |             |           | ipv6 nd | ra max-interval | 30  |
| Command            | History     |           |         |                 |     |
| Release            |             |           |         | Modification    |     |
| 10.07orearlier     |             |           |         | --              |     |
| Command            | Information |           |         |                 |     |
34
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

| Platforms | Command |     | context | Authority |     |
| --------- | ------- | --- | ------- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<TIME>
Specifiesaminimumadvertisementtimeinseconds.Range:3-
1350.Default:200seconds.
Usage
n ThisvaluehasonesettingperinterfaceanddoesnotapplytoRAssentinresponsetoarouter
solicitationreceivedfromanotherdevice.
n Themin-intervalmustbelessthanthemax-interval.Attemptingtosetmin-intervaltoahighervalue
resultsinanerrormessage.
Examples
| switch(config)#    |             | interface | 1/1/1      |              |     |
| ------------------ | ----------- | --------- | ---------- | ------------ | --- |
| switch(config-if)# |             |           | ipv6 nd ra | min-interval | 25  |
| Command            | History     |           |            |              |     |
| Release            |             |           |            | Modification |     |
| 10.07orearlier     |             |           |            | --           |     |
| Command            | Information |           |            |              |     |
| Platforms          | Command     |           | context    | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra other-config-flag    |     |     |     |     |
| ------- | ----------------------- | --- | --- | --- | --- |
| ipv6 nd | ra other-config-flag    |     |     |     |     |
| no ipv6 | nd ra other-config-flag |     |     |     |     |
IPv6RouterAdvertisement|35

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
| switch(config)#    |             | interface | 1/1/1   |                      |
| ------------------ | ----------- | --------- | ------- | -------------------- |
| switch(config-if)# |             |           | ipv6 nd | ra other-config-flag |
| Command            | History     |           |         |                      |
| Release            |             |           |         | Modification         |
| 10.07orearlier     |             |           |         | --                   |
| Command            | Information |           |         |                      |
| Platforms          | Command     |           | context | Authority            |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra reachable-time    |     |          |     |
| ------- | -------------------- | --- | -------- | --- |
| ipv6 nd | ra reachable-time    |     | <TIME>   |     |
| no ipv6 | nd ra reachable-time |     | [<TIME>] |     |
Description
Setstheamountoftimethattheinterfaceconsidersadevicetobereachableafterreceivinga
reachabilityconfirmationfromthedevice.
Thenoformofthiscommandsetsthereachabletimetothedefaultvalueof0.(nolimit).
| Parameter |     |     |     | Description                                         |
| --------- | --- | --- | --- | --------------------------------------------------- |
| <TIME>    |     |     |     | Specifiesthereachabletimeinmilliseconds.Range:1000- |
3600000.Default:0(nolimit).
Examples
36
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------- | --- | ------------------ | --- | --- |

| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|                |             |     | ipv6 nd | ra reachable-time | 2000 |
| -------------- | ----------- | --- | ------- | ----------------- | ---- |
| Command        | History     |     |         |                   |      |
| Release        |             |     |         | Modification      |      |
| 10.07orearlier |             |     |         | --                |      |
| Command        | Information |     |         |                   |      |
| Platforms      | Command     |     | context | Authority         |      |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | ra retrans-timer    |     |          |     |     |
| ------- | ------------------- | --- | -------- | --- | --- |
| ipv6 nd | ra retrans-timer    |     | <TIME>   |     |     |
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
| switch(config)#    |             | interface | 1/1/1   |                  |     |
| ------------------ | ----------- | --------- | ------- | ---------------- | --- |
| switch(config-if)# |             |           | ipv6 nd | ra retrans-timer | 400 |
| Command            | History     |           |         |                  |     |
| Release            |             |           |         | Modification     |     |
| 10.07orearlier     |             |           |         | --               |     |
| Command            | Information |           |         |                  |     |
IPv6RouterAdvertisement|37

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | route |     |     |
| ------- | ----- | --- | --- |
ipv6 nd route <IPV6-ADDR>/<PREFIX-LEN> [no-advertise | lifetime {<SECONDS> | infinite} |
| preference | {low | medium | | high}] |     |
| ---------- | ------------- | -------- | --- |
no ipv6 nd route <IPV6-ADDR>/<PREFIX-LEN> [no-advertise | lifetime {<SECONDS> | infinite}
| | preference | {low | medium | | high}] |     |
| ------------ | ------------- | -------- | --- |
Description
ConfigurestheroutingswitchtoincludetheroutinginformationintheRAstransmittedontheinterface.
TheroutingswitchincludestherouteinformationintheRApacketsonlyiftheconfiguredroutesare
presentintheroutingtable.AfterreceivingtheRApacketscarryingtherouteinformation,theIPv6host
updatesitsroutingtable.Thehostslookuptheirroutingtableandselectsthebestpossiblerouteto
forwardpackets.
Thenoformofthiscommandremovesthesettingsforincludingtheroutinginformationinthe
RA packets.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV6-ADDR>/<PREFIX-LEN> SpecifiestheIPv6routeprefixtoadvertiseinRA.Format:
X:X::X:X/M
| no-advertise |     |     | Specifiestonotadvertisetherouteinformation. |
| ------------ | --- | --- | ------------------------------------------- |
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
| Command | History     |     |                   |
| ------- | ----------- | --- | ----------------- |
| Release |             |     | Modification      |
| 10.10   |             |     | Commandintroduced |
| Command | Information |     |                   |
38
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Platforms | Command |     | context | Authority |     |
| --------- | ------- | --- | ------- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | router-preference    |     |         |          |        |
| ------- | -------------------- | --- | ------- | -------- | ------ |
| ipv6 nd | router-preference    |     | {high | | medium   | | low} |
| no ipv6 | nd router-preference |     | [high   | | medium | | low] |
Description
SpecifiesthevaluethatissetintheDefaultRouterPreference(DRP)fieldofRouterAdvertisements
(RAs)thattheswitchsendsfromaninterface.AninterfacewithaDRPvalueofhighwillbepreferredby
otherdevicesonthenetworkoverinterfaceswithanRAvalueofmediumorlow.
Thenoformofthiscommandsetthevaluetothedefaultofmedium.
| Parameter |     |     |     | Description              |     |
| --------- | --- | --- | --- | ------------------------ | --- |
| high      |     |     |     | SetsDRPtohigh.           |     |
| medium    |     |     |     | SetsDRPtomedium.Default. |     |
| low       |     |     |     | SetsDRPtolow.            |     |
Examples
| switch(config)#    |             | interface | 1/1/1                     |              |      |
| ------------------ | ----------- | --------- | ------------------------- | ------------ | ---- |
| switch(config-if)# |             |           | ipv6 nd router-preference |              | high |
| Command            | History     |           |                           |              |      |
| Release            |             |           |                           | Modification |      |
| 10.07orearlier     |             |           |                           | --           |      |
| Command            | Information |           |                           |              |      |
| Platforms          | Command     |           | context                   | Authority    |      |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 nd | suppress-ra      |                     |                     |     |     |
| ------- | ---------------- | ------------------- | ------------------- | --- | --- |
| ipv6 nd | suppress-ra      | [<SUPPRESS-OPTION>] |                     |     |     |
| no ipv6 | nd ra supress-ra |                     | [<SUPPRESS-OPTION>] |     |     |
Description
ConfiguressuppressionofIPv6RouterAdvertisementtransmissionsonaninterface.
ThenoformofthiscommandrestorestransmissionofIPv6RouterAdvertisementandoptions.
IPv6RouterAdvertisement|39

| Parameter   |     |                     |     |     |     | Description |     |     |
| ----------- | --- | ------------------- | --- | --- | --- | ----------- | --- | --- |
| suppress-ra |     | [<SUPPRESS-OPTION>] |     |     |     |             |     |     |
SpecifiessuppressingRAtransmissions.Enteringsuppress-ra
withoutanyoptions,suppressesallRAmessages(default).Oryou
canenteroneofthefollowingoptions.
|     | dnssl |     |     |     |     | SpecifiessuppressingDNSSLoptionsinRAmessages. |     |     |
| --- | ----- | --- | --- | --- | --- | --------------------------------------------- | --- | --- |
|     | mtu   |     |     |     |     | SpecifiessuppressingMTUoptionsinRAmessages.   |     |     |
|     | rdnss |     |     |     |     | SpecifiessuppressingRDNSSoptionsinRAmessages. |     |     |
Examples
|                | switch(config)#    |             | interface |         | 1/1/1          |              |           |             |
| -------------- | ------------------ | ----------- | --------- | ------- | -------------- | ------------ | --------- | ----------- |
|                | switch(config-if)# |             |           | ipv6    | nd suppress-ra |              | mtu dnssl | rdnss       |
|                | switch(config-if)# |             |           | no ipv6 | nd             | suppress-ra  | mtu       | dnssl rdnss |
| Command        |                    | History     |           |         |                |              |           |             |
| Release        |                    |             |           |         |                | Modification |           |             |
| 10.07orearlier |                    |             |           |         |                | --           |           |             |
| Command        |                    | Information |           |         |                |              |           |             |
| Platforms      |                    |             | Command   | context |                | Authority    |           |             |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show | ipv6    | nd     | global  | traffic |     |     |     |     |
| ---- | ------- | ------ | ------- | ------- | --- | --- | --- | --- |
| show | ipv6 nd | global | traffic |         |     |     |     |     |
Description
DisplaysIPV6NeighborDiscoverytrafficdetailsonadevice.
Examples
|     | switch#     | show           | ipv6           | nd global | traffic         |     |      |     |
| --- | ----------- | -------------- | -------------- | --------- | --------------- | --- | ---- | --- |
|     | ICMPv6      | packet         | Statistics     |           | (sent/received) |     |      |     |
|     | Total       | Messages       |                |           |                 | :   | 18/0 |     |
|     | Error       | Messages       |                |           |                 | :   | 0/0  |     |
|     | Destination |                | Unreachables   |           |                 | :   | 0/0  |     |
|     | Time        | Exceeded       |                |           |                 | :   | 0/0  |     |
|     | Parameter   |                | Problems       |           |                 | :   | 0/0  |     |
|     | Echo        | Request        |                |           |                 | :   | 0/0  |     |
|     | Echo        | Replies        |                |           |                 | :   | 0/0  |     |
|     | Redirects   |                |                |           |                 | :   | 0/0  |     |
|     | Packet      | Too            | Big            |           |                 | :   | 0/0  |     |
|     | Router      | Advertisements |                |           |                 | :   | 4/0  |     |
|     | Router      | Solicitations  |                |           |                 | :   | 0/0  |     |
|     | Neighbor    |                | Advertisements |           |                 | :   | 0/0  |     |
40
| AOS-CX10.11IPServicesGuide| |     |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |

|                | Neighbor    | Solicitations  |     |                 | :            | 3/0 |     |
| -------------- | ----------- | -------------- | --- | --------------- | ------------ | --- | --- |
|                | Duplicate   | router         |     | RA received     | :            | 0/0 |     |
|                | ICMPv6      | MLD Statistics |     | (sent/received) |              |     |     |
|                | V1 Queries  |                | :   | 0/0             |              |     |     |
|                | V2 Queries  |                | :   | 0/0             |              |     |     |
|                | V1 Reports  |                | :   | 0/0             |              |     |     |
|                | V2 Reports  |                | :   | 11/0            |              |     |     |
|                | V1 Leaves   |                | :   | 0/0             |              |     |     |
| Command        | History     |                |     |                 |              |     |     |
| Release        |             |                |     |                 | Modification |     |     |
| 10.07orearlier |             |                |     |                 | --           |     |     |
| Command        | Information |                |     |                 |              |     |     |
| Platforms      |             | Command        |     | context         | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | ipv6    | nd        | interface  |     |            |                   |     |
| ---- | ------- | --------- | ---------- | --- | ---------- | ----------------- | --- |
| show | ipv6 nd | interface | [<IF-NAME> |     | | all-vrfs | | vrf <VRF-NAME>] |     |
Description
Displaysneighbordiscoveryinformationforaninterface.Ifnooptionsarespecified,displays
informationforthedefaultVRF.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<IF-NAME> DisplaysinformationaboutthespecifiedIPv6enabledinterface.
all-vrfs
DisplaysinformationaboutinterfacesinallVRFs.
vrf <VRF-NAME> DisplaysinformationaboutinterfacesinaparticularVRF.Or,if
<VRF-NAME>isnotspecified,informationforthedefaultVRFis
displayed.
Examples
ShowinginformationforallVRFs:
|     | switch#         | show ipv6            | nd       | interface | all-vrfs                     |     |         |
| --- | --------------- | -------------------- | -------- | --------- | ---------------------------- | --- | ------- |
|     | List of         | IPv6 Interfaces      |          | for       | VRF default                  |     |         |
|     | Interface       | 1/1/1                | is up    |           |                              |     |         |
|     | Admin           | state is             | up       |           |                              |     |         |
|     | IPv6 address:   |                      |          |           |                              |     |         |
|     | IPv6 link-local |                      | address: |           | fe80::7272:cfff:fee7:a8b9/64 |     | [VALID] |
|     | ICMPv6          | active               | timers:  |           |                              |     |         |
|     | Last            | Router-Advertisement |          |           | sent:                        |     |         |
IPv6RouterAdvertisement|41

|                      | Next     | Router-Advertisement |           |             |                | sent in:  |             |     |
| -------------------- | -------- | -------------------- | --------- | ----------- | -------------- | --------- | ----------- | --- |
| Router-Advertisement |          |                      |           | parameters: |                |           |             |     |
|                      | Periodic |                      | interval: | 200         | to             | 600 secs  |             |     |
|                      | Router   | Preference:          |           | medium      |                |           |             |     |
|                      | Send     | "Managed             | Address   |             | Configuration" |           | flag: false |     |
|                      | Send     | "Other               | Stateful  |             | Configuration" |           | flag: false |     |
|                      | Send     | "Current             | Hop       | Limit"      |                | field: 64 |             |     |
|                      | Send     | "MTU"                | option    | value:      |                | 1500      |             |     |
|                      | Send     | "Router              | Lifetime" |             | field:         | 1800      |             |     |
|                      | Send     | "Reachable           |           | Time"       | field:         | 0         |             |     |
|                      | Send     | "Retrans             | Timer"    |             | field:         | 0         |             |     |
|                      | Suppress |                      | RA: true  |             |                |           |             |     |
|                      | Suppress |                      | MTU in    | RA:         | true           |           |             |     |
| ICMPv6               | error    |                      | message   | parameters: |                |           |             |     |
|                      | Send     | redirects:           |           | false       |                |           |             |     |
| ICMPv6               | DAD      | parameters:          |           |             |                |           |             |     |
|                      | Current  | DAD                  | attempt:  |             | 1              |           |             |     |
| List                 | of IPv6  | Interfaces           |           | for         | VRF            | red       |             |     |
| Interface            |          | 1/1/2                | is up     |             |                |           |             |     |
| Admin                | state    | is                   | up        |             |                |           |             |     |
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
42
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

|     | Send     | "MTU"           | option       |             | value: | 1500        |     |     |
| --- | -------- | --------------- | ------------ | ----------- | ------ | ----------- | --- | --- |
|     | Send     | "Router         |              | Lifetime"   |        | field: 1800 |     |     |
|     | Send     | "Reachable      |              | Time"       | field: | 0           |     |     |
|     | Send     | "Retrans        |              | Timer"      | field: | 0           |     |     |
|     | Suppress |                 | RA:          | true        |        |             |     |     |
|     | Suppress |                 | MTU          | in RA:      | true   |             |     |     |
|     | ICMPv6   | error           | message      | parameters: |        |             |     |     |
|     | Send     | redirects:      |              | false       |        |             |     |     |
|     | ICMPv6   | DAD parameters: |              |             |        |             |     |     |
|     | Current  |                 | DAD attempt: |             | 1      |             |     |     |
ShowinginformationforthedefaultVRF:
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
| show | ipv6    | nd        | interface |        | prefix    |     |                 |     |
| ---- | ------- | --------- | --------- | ------ | --------- | --- | --------------- | --- |
| show | ipv6 nd | interface |           | prefix | [all-vrfs | |   | vrf <VRF-NAME>] |     |
IPv6RouterAdvertisement|43

Description
ShowsIPv6prefixinformationforallVRFsoraspecificVRF.Ifnooptionsarespecified,shows
informationforthedefaultVRF.
| Parameter |            |     |     |     | Description                       |     |
| --------- | ---------- | --- | --- | --- | --------------------------------- | --- |
| all-vrfs  |            |     |     |     | ShowsprefixinformationforallVRFs. |     |
| vrf       | <VRF-NAME> |     |     |     | NameofaVRF.                       |     |
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
44
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

Description
DisplaysrouteinformationofallinterfacesinthedefaultVRF.
| Parameter |     | Description                                  |     |     |     |
| --------- | --- | -------------------------------------------- | --- | --- | --- |
| all-vrfs  |     | DisplaysinformationaboutinterfacesinallVRFs. |     |     |     |
vrf <VRF-NAME>
DisplaysinformationaboutinterfacesinaparticularVRF.Or,if<VRF-NAME>isnot
specified,displaysinformationforthedefaultVRF.
Examples
Showingroutinginformationforinterface1/1/1inthedefaultVRF:
| switch# | show             | ipv6       | nd interface | route       |     |
| ------- | ---------------- | ---------- | ------------ | ----------- | --- |
| List    | of IPv6          | Interfaces | for          | VRF default |     |
| List    | of IPv6          | Routes     | advertised   | on 1/1/1    |     |
|         | Route :          | 1::/64     |              |             |     |
|         | Enabled          | : Yes      |              |             |     |
|         | Route lifetime   |            | : 200        |             |     |
|         | Route preference |            | : high       |             |     |
Showingroutinginformationforinterface1/1/1inVRFred:
| switch#   | show             | ipv6       | nd interface | route vrf         | red |
| --------- | ---------------- | ---------- | ------------ | ----------------- | --- |
| List      | of IPv6          | Interfaces | for          | VRF red           |     |
| List      | of IPv6          | Routes     | advertised   | on 1/1/2          |     |
|           | Route :          | 2::/64     |              |                   |     |
|           | Enabled          | : No       |              |                   |     |
|           | Route lifetime   |            | : 1800       |                   |     |
|           | Route preference |            | : low        |                   |     |
| Command   | History          |            |              |                   |     |
| Release   |                  |            |              | Modification      |     |
| 10.10     |                  |            |              | Commandintroduced |     |
| Command   | Information      |            |              |                   |     |
| Platforms |                  | Command    | context      | Authority         |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show      | ipv6 | nd ra dns          | search-list |     |     |
| --------- | ---- | ------------------ | ----------- | --- | --- |
| show ipv6 | nd   | ra dns search-list |             |     |     |
Description
Displaysdomainnameinformationonallinterfaces.
IPv6RouterAdvertisement|45

Examples

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

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

46

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

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

47

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

n sFlow is not configurable through SNMP.

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

sFlow | 48

| sFlow setting                 |     | Default value | Command             | to change | it  |
| ----------------------------- | --- | ------------- | ------------------- | --------- | --- |
| SizeofthesFlowheader.         |     | 128bytes      | sflow header-size   |           |     |
| MaximumsizeofansFlowdatagram. |     | 1400bytes     | sflow max-datagram- |           |     |
size
| 6. ReviewsFlowconfigurationsettingswiththecommandshow |     | sflow. |     |     |     |
| ----------------------------------------------------- | --- | ------ | --- | --- | --- |
Example
Thisexamplecreatesthefollowingconfiguration:
ConfiguresansFlowcollectorwiththeIPaddress10.10.20.209.
n
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
| switch(config)# | sflow agent-ip | 10.10.12.1 |     |     |     |
| --------------- | -------------- | ---------- | --- | --- | --- |
3. SetthesFlowcollectorIPaddressto10.10.12.2.
| switch(config)# | sflow collector | 18.2.2.2 |     |     |     |
| --------------- | --------------- | -------- | --- | --- | --- |
4. ConfiguresFLowsamplingrateandpollinginterval.
| switch(config)# | sflow sampling | 5000 |     |     |     |
| --------------- | -------------- | ---- | --- | --- | --- |
| switch(config)# | sflow polling  | 20   |     |     |     |
49
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

5. Configureinterface1/1/1withIPaddress10.10.10.1/24.
|     | switch(config)#    |     | interface   | 1/1/1         |
| --- | ------------------ | --- | ----------- | ------------- |
|     | switch(config-if)# |     | no shutdown |               |
|     | switch(config-if)# |     | ip address  | 10.10.10.1/24 |
|     | switch(config)#    |     | quit        |               |
6. Configureinterface1/1/2withIPaddress10.10.11.1/24.
|     | switch(config)#    |     | interface   | 1/1/2         |
| --- | ------------------ | --- | ----------- | ------------- |
|     | switch(config-if)# |     | no shutdown |               |
|     | switch(config-if)# |     | ip address  | 10.10.11.1/24 |
|     | switch(config)#    |     | quit        |               |
7. Configureinterface1/1/3withIPaddress10.10.12.1/24.
|     | switch(config)#    |     | interface   | 1/1/3         |
| --- | ------------------ | --- | ----------- | ------------- |
|     | switch(config-if)# |     | no shutdown |               |
|     | switch(config-if)# |     | ip address  | 10.10.12.1/24 |
|     | switch(config)#    |     | quit        |               |
8. VerifysFlowconfiguration
switch#
|     |              | show sflow    |     |     |
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
Inthisscenario,twohostsconnectedtodifferentswitchessendsFlowtraffictoacollector.ALAGis
usedtoconnectthetwoswitches.Thephysicaltopologyofthenetworklookslikethis:
sFlow|50

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
51
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

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
sFlow|52

|       | switch(config-if)#                                   |                    |         | no        | shutdown    |       |                   |     |
| ----- | ---------------------------------------------------- | ------------------ | ------- | --------- | ----------- | ----- | ----------------- | --- |
|       | switch(config-if)#                                   |                    |         | vlan      | access      |       | 8                 |     |
|       | d. Configureinterface1/1/2and1/1/3asmembersofLAG100. |                    |         |           |             |       |                   |     |
|       | switch#                                              | (config)#interface |         |           |             | 1/1/2 |                   |     |
|       | switch(config-if)#                                   |                    |         | no        | shutdown    |       |                   |     |
|       | switch(config-if)#                                   |                    |         | lag       | 100         |       |                   |     |
|       | switch(config-if)#                                   |                    |         | exit      |             |       |                   |     |
|       | switch(config)-if#                                   |                    |         | interface |             | 1/1/3 |                   |     |
|       | switch(config-if)#                                   |                    |         | no        | shutdown    |       |                   |     |
|       | switch(config-if)#                                   |                    |         | lag       | 100         |       |                   |     |
|       | switch(config-if)#                                   |                    |         | exit      |             |       |                   |     |
| sFlow | agent                                                | commands           |         |           |             |       |                   |     |
| clear | sflow                                                | statistics         |         |           |             |       |                   |     |
| clear | sflow                                                | statistics         | {global |           | | interface |       | <INTERFACE-NAME>} |     |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow
53
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

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
Command History
Release Modification
10.07orearlier --
sFlow|54

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if |     | forthiscommand. |
| --- | --------- | --- | --------------- |
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
| Command History |     |                |     |
55
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow collector
| sflow collector    | <IP-ADDR> | [port | <PORT>] | [vrf <VRF>] |        |
| ------------------ | --------- | ----- | ------- | ----------- | ------ |
| no sflow collector | <IP-ADDR> | [port | <PORT>] | [vrf        | <VRF>] |
Description
DefinesacollectortowhichthesFlowagentsendsdata.Uptothreecollectorscanbedefined.Atleast
onecollectorshouldbedefined,anditmustbereachablefromtheswitchforsFlowtowork.
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
| switch(config)#     | sflow   | collector | 10.0.0.1     | port | 6400 |
| ------------------- | ------- | --------- | ------------ | ---- | ---- |
| Command History     |         |           |              |      |      |
| Release             |         |           | Modification |      |      |
| 10.07orearlier      |         |           | --           |      |      |
| Command Information |         |           |              |      |      |
| Platforms           | Command | context   | Authority    |      |      |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sFlow|56

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Settingtheheadersizetothedefaultvalueof128bytes:
| switch(config)# | no  | sflow header-size |     |
| --------------- | --- | ----------------- | --- |
57
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config)#     | no      | sflow max-datagram-size |              |
| ------------------- | ------- | ----------------------- | ------------ |
| Command History     |         |                         |              |
| Release             |         |                         | Modification |
| 10.07orearlier      |         |                         | --           |
| Command Information |         |                         |              |
| Platforms           | Command | context                 | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sFlow|58

| sflow      | mode          |          |         |
| ---------- | ------------- | -------- | ------- |
| sflow mode | {ingress      | | egress | | both} |
| no sflow   | mode {ingress | | egress | | both} |
Description
SetsthesFlowsamplingmode.Thedefaultmodeisingress.
Thenoformofthecommandsetsthesamplingmodetoingress.Executingthenoformofthe
commandwiththeingressoptionwillhavenoimpactasingressisthedefaultmode.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
ingress
Samplesonlyingresstraffic.
| egress |     |     | Samplesonlyegresstraffic. |
| ------ | --- | --- | ------------------------- |
both
Samplesbothingressandegresstraffic.
Examples
SettingthesFlowmodetoonlysampleegresstraffic:
| switch#         | configure | terminal   |        |
| --------------- | --------- | ---------- | ------ |
| switch(config)# |           | sflow mode | egress |
SettingthesFlowmodetoonlysampleingresstraffic:
| switch#         | configure | terminal   |         |
| --------------- | --------- | ---------- | ------- |
| switch(config)# |           | sflow mode | ingress |
SettingthesFlowmodetosamplebothsampleingressandegresstraffic:
| switch#         | configure | terminal   |      |
| --------------- | --------- | ---------- | ---- |
| switch(config)# |           | sflow mode | both |
ResettingthesFlowsamplingmodetothedefaultofingressfrompreviouslyconfiguredmodeofegress:
| switch#         | configure   | terminal |              |
| --------------- | ----------- | -------- | ------------ |
| switch(config)# |             | no sflow | mode egress  |
| Command         | History     |          |              |
| Release         |             |          | Modification |
| 10.07orearlier  |             |          | --           |
| Command         | Information |          |              |
59
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |
| --------------------------- | --- | ------------------ | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow polling
| sflow polling    | <INTERVAL>   |     |     |
| ---------------- | ------------ | --- | --- |
| no sflow polling | [<INTERVAL>] |     |     |
Description
DefinestheglobalpollingintervalforsFlowinseconds.
Thenoformofthiscommandsetsthepollingintervaltothedefaultvalueof30seconds.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<INTERVAL>
Specifiesthepollingintervalinseconds.Range:10to3600.
Default:30.
Examples
Settingthepollingintervalto10:
switch(config)#
|     | sflow | polling 10 |     |
| --- | ----- | ---------- | --- |
Settingthepollingintervaltothedefaultvalue.
| switch(config)#     | no      | sflow polling |              |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
sflow sampling
| sflow sampling    | <RATE>   |     |     |
| ----------------- | -------- | --- | --- |
| no sflow sampling | [<RATE>] |     |     |
Description
DefinestheglobalsamplingrateforsFlowinnumberofpackets.Thedefaultsamplingrateis4096,
whichmeansthatoneinevery4096packetsissampled.Awarningmessageisdisplayedwhenthe
samplingrateissettolessthan4096andproceedsonlyafteruserconfirmation.
sFlow|60

Thenoformofthiscommandsetsthesamplingratetothedefaultvalueof4096.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
sampling <RATE> Specifiesthesamplingrate.Range:1to1000000000.Default:
4096.
Examples
Settingthesamplingrateto5000:
| switch(config)# |     | sflow | sampling | 5000 |
| --------------- | --- | ----- | -------- | ---- |
Settingthesamplingratetothedefault:
| switch(config)# |     | no  | sflow sampling |     |
| --------------- | --- | --- | -------------- | --- |
Settingthesamplingrateto1000:
| switch(config)# |     | sflow | sampling | 1000 |
| --------------- | --- | ----- | -------- | ---- |
Setting the sFlow sampling rate lower than 4096 is not recommended and might
| affect | system  | performance. |        |     |
| ------ | ------- | ------------ | ------ | --- |
| Do you | want to | continue     | [y/n]? | y   |
switch(config)#
| Command        | History     |     |         |              |
| -------------- | ----------- | --- | ------- | ------------ |
| Release        |             |     |         | Modification |
| 10.07orearlier |             |     |         | --           |
| Command        | Information |     |         |              |
| Platforms      | Command     |     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show       | sflow      |     |                   |     |
| ---------- | ---------- | --- | ----------------- | --- |
| show sflow | [interface |     | <INTERFACE-NAME>] |     |
Description
ShowssFlowconfigurationsettingsandstatisticsforallinterfaces,orforaspecificinterface.Italso
displaysthecurrentstatusofsFlowonthedeviceandreportsanyerrorsthatrequireattention.
IfsFlowisenabledontheinterfacesassociatedwithalaginterface,thentheinterfaceswillnotbeshownas
separateentriesundersFlow enabled on Interfaceintheoutput.Onlytheassociatedlaginterfacewillhave
anentryinthecolumn.
61
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |
| --------------------------- | --- | ------------------ | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
interface <INTERFACE-NAME> Specifiesthenameofaninterfaceontheswitch.
Examples
ShowingsFlowinformationforallinterfaces:
| switch#      | show | sflow         |     |
| ------------ | ---- | ------------- | --- |
| sFlow Global |      | Configuration |     |
-----------------------------------------
| sFlow     |             |     | enabled               |
| --------- | ----------- | --- | --------------------- |
| Collector | IP/Port/Vrf |     | 10.0.0.2/6343/default |
10.0.0.3/6400/default
| Agent Address |          |      | 10.0.0.1 |
| ------------- | -------- | ---- | -------- |
| Sampling      | Rate     |      | 1024     |
| Polling       | Interval |      | 30       |
| Header        | Size     |      | 128      |
| Max Datagram  |          | Size | 1400     |
| Sampling      | Mode     |      | ingress  |
sFlow Status
-----------------------------------------
| Running       | - Yes |                |     |
| ------------- | ----- | -------------- | --- |
| sFlow enabled |       | on Interfaces: |     |
-----------------------------------------
1/1/2
1/1/3
lag100
sFlow Statistics
-----------------------------------------
| Number | of Ingress | Samples | 200 |
| ------ | ---------- | ------- | --- |
| Number | of Egress  | Samples | 120 |
ShowingsFlowinformationforinterface1/1/1:
| switch#             | show | sflow interface | 1/1/1 |
| ------------------- | ---- | --------------- | ----- |
| sFlow configuration |      | - Interface     | 1/1/1 |
-----------------------------------------
| sFlow                                  |            |                 | enabled |
| -------------------------------------- | ---------- | --------------- | ------- |
| Sampling                               | Rate       |                 | 1024    |
| Sampling                               | Mode       |                 | both    |
| Number                                 | of Ingress | Samples         | 81      |
| Number                                 | of Egress  | Samples         | 20      |
| sFlow Sampling                         |            | Status          | success |
| ShowingsFlowinformationforinterfacelag |            |                 | 10:     |
| switch#                                | show       | sflow interface | lag 10  |
| sFlow Configuration                    |            | - Interface     | lag10   |
-----------------------------------------
| sFlow    |            |         | enabled |
| -------- | ---------- | ------- | ------- |
| Sampling | Rate       |         | 4096    |
| Sampling | Mode       |         | both    |
| Number   | of Ingress | Samples | 0       |
| Number   | of Egress  | Samples | 0       |
sFlow|62

| sFlow Sampling | Status    | error       |     |
| -------------- | --------- | ----------- | --- |
| Sampling       | Status on | LAG members |     |
------------------------------------
| Intf 1/1/2          |         |         | no agent     |
| ------------------- | ------- | ------- | ------------ |
| Intf 1/1/3          |         |         | no agent     |
| Command History     |         |         |              |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
63
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

Chapter 5
DHCP
DHCP
TheDynamicHostConfigurationProtocol(DHCP)enablestheautomaticassignmentofIPaddressesand
otherconfigurationsettingstonetworkdevices.
TheDHCPrelayagentactsanintermediary,forwardingDHCPrequests/responsebetweenDHCP
clients/serversondifferentnetworks.ThisenablesDHCPclientstousetheservicesofDHCPserversthat
arenotonthesamesubnetonwhichtheyarelocated.
| DHCP     | client |         |         |     |     |     |
| -------- | ------ | ------- | ------- | --- | --- | --- |
| Protocol | and    | feature | details |     |     |     |
DHCPClientissupportedonIPv4andIPv6(forIPV6itissupportedonlyonmanagementVRF).
TheIPDHCPassignmentwithArubaAOS-CXswitchistoallowthefollowing:
n IPswitchassignment.
n ManagingtheinitialIPaccesstotheswitch.
PrepareforZeroTouchProvisioning(ZTP)withHPEGreenLakeArubaCentral.
n
ZeroTouchProvisioning(ZTP)isonlysupportedforIPV4inArubaCentral
PrepareforZeroTouchProvisioning(ZTP)byusingDHCPoptionsalongwithaTFTPserver.
n
| Supported | platform |     | and standards |     |     |     |
| --------- | -------- | --- | ------------- | --- | --- | --- |
ThefollowingtablelistthesupportedVLANsandportsfortheAOS-CXSwitch.
Table1:SupportedVLANandPortsforDHCP
|               |     |      |      | Any Other |              | Management |
| ------------- | --- | ---- | ---- | --------- | ------------ | ---------- |
| Platform      |     | VLAN | 1    |           | In band Port |            |
|               |     |      |      | VLAN      |              | VRF port   |
| 6200          |     | Yes  |      |           |              |            |
|               |     |      |      | Yes       | Yes          | Yes        |
| Configuration |     | task | list |           |              |            |
ToruntheDHCPClientdothefollowing:
n EntertheinterfaceVLANorManagementVRFcontext
n EnableDHCP
| Considerations |     | and | best practices |     |     |     |
| -------------- | --- | --- | -------------- | --- | --- | --- |
TheIPDHCPcanonlybeconfiguredononeVLANperswitch.
64
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

IfanOOBManagementportisavailable,youcanconfiguretheDHCPservicesimultaneouslyforthe
VLANINBandandtheOOBManagementport.WhenboththeINBanddataportandtheOOB
ManagementportreceiveaDHCPaddress,thentheDHCPaddressreceivedontheOOBMportis
preferredovertheINBanddataportforZTP.
Use case
IPDHCPassignmentwithArubaAOS-CXswitchesistoallowIPswitchassignmentandZeroTouch
ProvisioningusingHPEGreenLakeArubaCentral,asshownbelow.
InthefollowingDHCPclientscenariotheOOBManagementportisinuse.TheINBanddataportscan
alsobeusedforZeroTouchProvisioning(ZTP).
Formoreinformationrelatedtothesupportedportsforthedifferentswitches,see Table1,Supported
VLANandPortsforDHCP.
1. SwitchconfigurationfromfactoryonOOBManagementport.
switch#
!
| interface | mgmt |     |     |
| --------- | ---- | --- | --- |
no shutdown
ip dhcp
!
2. OOBManagementportgetsassignedwithanIPv4address10.5.5.27fromDHCPserver.
| switch# show             | interface | mgmt |                     |
| ------------------------ | --------- | ---- | ------------------- |
| Address                  | Mode      |      | : dhcp              |
| Admin State              |           |      | : up                |
| Link State               |           |      | : up                |
| Mac Address              |           |      | : 88:3a:30:9a:39:01 |
| IPv4 address/subnet-mask |           |      | : 10.5.5.27/24      |
| Default                  | gateway   | IPv4 | : 10.5.5.254        |
IPv6 address/prefix : 2a00:23c5:ac8a:3e01:8a3a:30ff:fe9a:3901/64
| IPv6 link | local   | address/prefix: | fe80::8a3a:30ff:fe9a:3901/64 |
| --------- | ------- | --------------- | ---------------------------- |
| Default   | gateway | IPv6            | : fe80::f286:20ff:fe0b:fe5   |
DHCP|65

|     | Primary   | Nameserver |            |     | : 10.5.19.69 |
| --- | --------- | ---------- | ---------- | --- | ------------ |
|     | Secondary |            | Nameserver |     | : 10.5.19.79 |
|     | Tertiary  | Nameserver |            |     | : 8.8.4.4    |
ThefollowingoutputshowsaswitchconnectedtoArubacentralallocatedwithanIPaddressof
10.5.5.27onitsOOBMGMTportbyaDHCPserver.Basedonitsdesignatedconfigurationinthepublic
cloud,theswitchcangetitsconfigurationparametersdirectlyfromArubaCentral.
| switch# | show     | aruba-central |     |     |                 |
| ------- | -------- | ------------- | --- | --- | --------------- |
| Central | admin    | state         |     |     | : enabled       |
| Central | location |               |     |     | : device-prod2- |
d2.central.arubanetworks.com
| VRF     | for connection |            |        |        | : mgmt      |
| ------- | -------------- | ---------- | ------ | ------ | ----------- |
| Central | connection     |            | status |        | : connected |
| Central | source         |            |        |        | : activate  |
| Central | source         | connection |        | status | : connected |
Central source last connected on : Wed Sep 22 18:39:05 UTC 2021
| System   | time     | synchronized |      | from Activate | : True                         |
| -------- | -------- | ------------ | ---- | ------------- | ------------------------------ |
| Activate |          | Server       | URL  |               | : devices-v2.arubanetworks.com |
| CLI      | location |              |      |               | : N/A                          |
| CLI      | VRF      |              |      |               | : N/A                          |
| Source   | IP       |              |      |               | : 10.5.5.27                    |
| Source   | IP       | Overridden   |      |               | : False                        |
| Central  | support  |              | mode |               | : disabled                     |
| DHCP     | client   | commands     |      |               |                                |
ip dhcp
ip dhcp
no ip dhcp
Description
EnablestheDHCPclientonthemanagementinterfaceoranyinterfaceVLAN toautomaticallyobtainan
IPaddressfromaDHCPserveronthenetwork.Bydefault,theDHCPclientisenabledonthe
managementinterfaceandVLAN1.
ThenoformofthecommanddisablesDHCPmodeandissupportedonlyoninterfaceVLANs;itisnot
supportedonthemanagementinterface.
Examples
EnablingtheDHCPclientonthemanagementinterface:
| switch(config)#         |     | interface |     | mgmt        |     |
| ----------------------- | --- | --------- | --- | ----------- | --- |
| switch(config-if-mgmt)# |     |           |     | ip dhcp     |     |
| switch(config-if-mgmt)# |     |           |     | no shutdown |     |
EnablingtheDHCPclientontheinterfacevlan1:
| switch(config)#         |     | interface |     | vlan 1      |     |
| ----------------------- | --- | --------- | --- | ----------- | --- |
| switch(config-if-vlan)# |     |           |     | ip dhcp     |     |
| switch(config-if-vlan)# |     |           |     | no shutdown |     |
DisablingtheDHCPclientontheinterfacevlan1:
66
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

| switch(config)# | interface | vlan | 1   |     |     |
| --------------- | --------- | ---- | --- | --- | --- |
switch(config-if-vlan)#
|     |     | no ip dhcp |     |     |     |
| --- | --- | ---------- | --- | --- | --- |
Iftheinterfaceisnotenabled,youcanenableitbyenteringtheno shutdowncommand.
ip dhcpissupportedonlyononevlanatatime.
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
Allplatforms config-if-mgmt Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |     |     |
| --- | -------------- | --- | --------------- | --- | --- |
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
| vlan1               | 10.254.239.10/27 |         |                    | domain.com | default 50.0.0.2, |
| ------------------- | ---------------- | ------- | ------------------ | ---------- | ----------------- |
| 50.0.0.3,           | 50.0.0.4         |         |                    |            |                   |
| Command History     |                  |         |                    |            |                   |
| Release             |                  |         | Modification       |            |                   |
| 10.09orearlier      |                  |         | Commandintroduced. |            |                   |
| Command Information |                  |         |                    |            |                   |
| Platforms           | Command          | context | Authority          |            |                   |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
DHCP|67

| DHCP relay | agent |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- |
ThefunctionoftheDHCPrelayagentistoforwardtheDHCPmessagestoothersubnetssothatthe
DHCPserverdoesnothavetobeonthesamesubnetastheDHCPclients.TheDHCPrelayagent
transfersDHCPmessagesfromtheDHCPclientslocatedonasubnetwithoutaDHCPserver,toother
subnets.ItalsorelaysanswersfromDHCPserverstoDHCPclients.
| Supported | platform | and | standards |     |     |
| --------- | -------- | --- | --------- | --- | --- |
ThefollowingtablelistthesupportedplatformsforDHCPv4relayandDHCPv6relay.
Table1:Supportplatformsfor DHCPv4relayandDHCPv6relay
DHCPv4 Smart
| Platform | DHCPv4 | Relay |     | DHCPv6 | Relay |
| -------- | ------ | ----- | --- | ------ | ----- |
Relay
| 6200 | Yes |     | Yes | Yes |     |
| ---- | --- | --- | --- | --- | --- |
Table2:Scale
DHCP v4/v6 enabled
| Platform |     |     |     | DHCP v4/v6 | helper SVI |
| -------- | --- | --- | --- | ---------- | ---------- |
SVI
| 6200 |     |     | 128 | 8   |     |
| ---- | --- | --- | --- | --- | --- |
DHCPrelaybehaviorsareasfollows:
n DHCPv6relayisdisabledbydefault.
n DHCPv4Smartrelayisdisabledbydefault.
n DHCPrelayhopcountisenabledbydefault.
InDHCPv4relaytheoption82policyisreplacebydefault.
n
n TheMACaddressoftheswitchisusedastheoption82remoteIDbydefault.
n InDHCPv6relaytheoption79policyisdisabledbydefault.
n InDHCPv4relaythesource-interfaceisdisabledbydefault.
| DHCPv4    | relay agent      |     |     |     |     |
| --------- | ---------------- | --- | --- | --- | --- |
| Hop count | in DHCP requests |     |     |     |     |
WhenaDHCPclientbroadcastsrequest,theDHCPrelayagentintheswitchreceivesthepacketsand
forwardsthemtotheDHCPserverasunicastrequests.Duringthisprocess,theDHCPrelayagent
incrementsthehopcountbeforeforwardingDHCPpacketstotheserver.TheDHCPserver,inturn,
includesthehopcountintheDHCPheaderintheresponsesentbacktoaDHCPclient.
| DHCP relay | option 82 |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- |
Option82iscalledtherelayagentinformationoption.WhenaDHCPrelayagentforwardsclient-
originatedDHCPpacketstoaDHCPserver,theoption82fieldisinserted/replaced,orthepacketwith
thisoptionisdropped.Serversrecognizingtherelayagentinformationoptionmayusetheinformation
toimplementpoliciesfortheassignmentofIPaddressesandotherparameters.Therelayagentrelays
theserver-to-clientrepliestotheclient.
68
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

If a second relay agent is configured to add its own option 82 information, it can encapsulate option 82
information in messages from a first relay agent. The DHCP server uses the option 82 information from
both relay agents to decide the IP address for the client.

Configuring a BOOTP/DHCP relay gateway

The DHCP relay agent selects the lowest-numbered IP address on the interface to use for DHCP
messages. The DHCP server then uses this IP address when it assigns client addresses. However, this IP
address may not be the same subnet as the one on which the client needs the DHCP service. This
feature provides a way to configure a gateway address for the DHCP relay agent to use for relayed
DHCP requests, rather than the DHCP relay agent automatically assigning the lowest-numbered IP
address.

On configuring a bootp-gateway the dhcp-smart-relay is disabled. This can occur with dhcp-relay as well.

Configuring the DHCPv4 relay agent

Prerequisites

Procedure

1. The DHCPv4 relay agent is enabled by default. If it was previously disabled, enable it with the

command dhcp-relay.

2. Configure one or more IP helper addresses with the command ip helper-address. This

determines where the DHCPv4 relay agent forwards DHCP requests. IP helper addresses can be
configured on layer 3 interfaces, layer 3 VLAN interfaces, and LAG interfaces.

3.

If you want to modify the content of forwarded DHCP packets or drop DHCP packets, configure
option 82 support with the command dhcp-relay option 82.

4. Define the gateway address that the DHCPv4 relay agent will use with the command ip bootp-

gateway.

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

DHCP | 69

| switch(config)# |     | dhcp-relay |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- | --- | --- |
switch(config)#
|                         |             | interface  |      | 1/1/1             |                 |              |     |
| ----------------------- | ----------- | ---------- | ---- | ----------------- | --------------- | ------------ | --- |
| switch(config-if)#      |             |            | vlan | access            | 100             |              |     |
| switch(config-if)#      |             |            | exit |                   |                 |              |     |
| switch(config)#         |             | interface  |      | vlan              | 100             |              |     |
| switch(config-if-vlan)# |             |            |      | ip address        | 198.51.100.1/24 |              |     |
| switch(config-if-vlan)# |             |            |      | ip helper-address |                 | 10.10.20.209 |     |
| switch(config-if-vlan)# |             |            |      | exit              |                 |              |     |
| switch(config)#         |             | dhcp-relay |      | option            | 82 replace      | mac          |     |
| switch#                 | show        | dhcp-relay |      |                   |                 |              |     |
| DHCP Relay              | Agent       |            |      |                   | : enabled       |              |     |
| DHCP Request            |             | Hop Count  |      | Increment         | : enabled       |              |     |
| Option                  | 82          |            |      |                   | : disabled      |              |     |
| Source-Interface        |             |            |      |                   | : disabled      |              |     |
| Response                | Validation  |            |      |                   | : disabled      |              |     |
| Option                  | 82 Handle   | Policy     |      |                   | : replace       |              |     |
| Remote                  | ID          |            |      |                   | : mac           |              |     |
| DHCP Relay              | Statistics: |            |      |                   |                 |              |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |                |     | 60  |     | 10  |
| ---------- | ------ | --- | -------------- | --- | --- | --- | --- |
| DHCP Relay | Option |     | 82 Statistics: |     |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50  |     | 8   |     |     | 50  |     | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |
Use Case
ThissectionexplaintheusecasesforDHCPv4relayagent.
| DHCPv4 relay | scenario | 1   |     |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- | --- | --- |
Inthisscenario,DHCPrelayontheswitchenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
Procedure
70
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

1. DHCPrelayisenabledbydefault.Ifitwaspreviouslydisabled,enableit.
switch#
config
| switch(config)# |     | dhcp-relay |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- | --- |
2. DefineanIPv4helperaddressoninterfacevlan100
switch(config)#
|                         |     | interface | 1/1/1             |     |                 |     |
| ----------------------- | --- | --------- | ----------------- | --- | --------------- | --- |
| switch(config-if)#      |     |           | vlan access       | 100 |                 |     |
| switch(config-if)#      |     |           | exit              |     |                 |     |
| switch(config)#         |     | interface | 1/1/2             |     |                 |     |
| switch(config-if)#      |     |           | vlan access       | 100 |                 |     |
| switch(config-if)#      |     |           | exit              |     |                 |     |
| switch(config)#         |     | interface | vlan              | 100 |                 |     |
| switch(config-if-vlan)# |     |           | ip address        |     | 192.168.2.11/24 |     |
| switch(config-if-vlan)# |     |           | ip helper-address |     | 192.168.1.1     |     |
3. VerifyDHCPrelayconfiguration.
| switch#          | show        | dhcp-relay |           |     |          |     |
| ---------------- | ----------- | ---------- | --------- | --- | -------- | --- |
| DHCP Relay       | Agent       |            |           | :   | enabled  |     |
| DHCP Request     |             | Hop Count  | Increment | :   | enabled  |     |
| Option           | 82          |            |           | :   | disabled |     |
| Source-Interface |             |            |           | :   | disabled |     |
| Response         | Validation  |            |           | :   | disabled |     |
| Option           | 82 Handle   | Policy     |           | :   | replace  |     |
| Remote           | ID          |            |           | :   | mac      |     |
| DHCP Relay       | Statistics: |            |           |     |          |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |                | 60  |     | 10  |
| ---------- | ------ | --- | -------------- | --- | --- | --- |
| DHCP Relay | Option |     | 82 Statistics: |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50                    |           | 8    |                   | 50  |                   | 8   |
| --------------------- | --------- | ---- | ----------------- | --- | ----------------- | --- |
| switch(config)#       |           | show | ip helper-address |     |                   |     |
| IP Helper             | Addresses |      |                   |     |                   |     |
| Interface:            | vlan100   |      |                   |     |                   |     |
| IP Helper             | Address   |      |                   |     | VRF               |     |
| -----------------     |           |      |                   |     | ----------------- |     |
| 192.168.1.1           |           |      |                   |     | default           |     |
| DHCPv4 relay scenario | 2         |      |                   |     |                   |     |
Inthisscenario,hostonswitch1reachestheDHCPserveronswitchtwoviaaLAG.Thephysical
topologyofthenetworklookslikethis:
DHCP|71

Procedure
1. Onswitch1:
a. CreateLAG100andassignanIPaddresstoit.
switch# config
| switch(config)#         | interface |      | lag 100  |              |     |
| ----------------------- | --------- | ---- | -------- | ------------ | --- |
| switch(config-lag-if)#  |           | no   | shutdown |              |     |
| switch(config-lag-if)#  |           | vlan | access   | 200          |     |
| switch(config-lag-if)#  |           | lacp | mode     | active       |     |
| switch(config-lag-if)#  |           | exit |          |              |     |
| switch(config)#         | interface |      | vlan 200 |              |     |
| switch(config-if-vlan)# |           | ip   | address  | 10.0.10.1/24 |     |
b. AssignanIPaddresstointerfacevlan100andanIPhelperaddresstoreachtheDHCPserver.
| switch(config)#         | interface |          | 1/1/1          |            |         |
| ----------------------- | --------- | -------- | -------------- | ---------- | ------- |
| switch(config-if)#      | no        | shutdown |                |            |         |
| switch(config-if)#      | vlan      | access   | 100            |            |         |
| switch(config-if)#      | exit      |          |                |            |         |
| switch(config)#         | interface |          | vlan 100       |            |         |
| switch(config-if-vlan)# |           | ip       | address        | 20.0.0.1/8 |         |
| switch(config-if-vlan)# |           | ip       | helper-address |            | 9.0.0.2 |
c. Assigninterfaces1/1/2and1/1/3toLAG100.
| switch(config-if)# | interface |     | 1/1/2 |     |     |
| ------------------ | --------- | --- | ----- | --- | --- |
| switch(config-if)# | lag       | 100 |       |     |     |
| switch(config-if)# | interface |     | 1/1/3 |     |     |
| switch(config-if)# | lag       | 100 |       |     |     |
d. Createaroutebetween10.0.10.2and9.0.0.0.
| switch(config)# | ip route | 9.0.0.0/24 |     | 10.0.10.2 |     |
| --------------- | -------- | ---------- | --- | --------- | --- |
2. Onswitch2:
a. CreateLAG100andassignanIPaddresstoit.
72
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

switch# config
| switch(config)#         | interface |      | lag 100  |              |
| ----------------------- | --------- | ---- | -------- | ------------ |
| switch(config-lag-if)#  |           | no   | shutdown |              |
| switch(config-lag-if)#  |           | vlan | access   | 200          |
| switch(config-lag-if)#  |           | lacp | mode     | active       |
| switch(config-lag-if)#  |           | exit |          |              |
| switch(config)#         | interface |      | vlan 200 |              |
| switch(config-if-vlan)# |           | ip   | address  | 10.0.10.2/24 |
b. AssignanIPaddresstointerfacevlan300.
| switch(config)#         | interface |          | 1/1/3    |            |
| ----------------------- | --------- | -------- | -------- | ---------- |
| switch(config-if)#      | no        | shutdown |          |            |
| switch(config-if)#      | vlan      | access   | 300      |            |
| switch(config-if)#      | exit      |          |          |            |
| switch(config)#         | interface |          | vlan 300 |            |
| switch(config-if-vlan)# |           | ip       | address  | 9.0.0.1/24 |
c. Assigninterfaces1/1/1and1/1/2toLAG100.
switch(config-if)#
|                    | interface |     | 1/1/1 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | interface |     | 1/1/2 |     |
| switch(config-if)# | lag       | 100 |       |     |
d. Createaroutebetween20.0.0.0and10.0.10.1.
| switch(config)#         | ip route | 20.0.0.0/8 |     | 10.0.10.1 |
| ----------------------- | -------- | ---------- | --- | --------- |
| DHCPv4 relay scenario 3 |          |            |     |           |
InthefollowingscenariooftheDHCPsmartrelay,theprimaryaddressisusedastheGIADDR;ifthe
serverisunavailable,thenthesecondaryaddressisused.FromAOS-CX10.10.1000andlaterreleases,
theGIADRRusethesecondaryaddressinanascendingorderwhenthereismorethanonesecondary
address.
1. IfDHCPscopeexhaustionhappensatasite,anadditional scopecanbeaddedtoincreasetheIP
addresscapacity whilekeepingtheexistingIPscopeandsubnet.Thephysicaltopologyofthe
networklookslikethis:
DHCP|73

2.

If the DHCP server is resilient or scope is required, then whole scopes can be placed on separate
servers. If a server or scope becomes unavailable, then for address assignment, the next available
scope is attempted.

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

74

Inboththeabovetopology,theaccessswitchissetupthesameway.Theonlydifferenceisintheserver
whichisusedforhelperaddresses.
!
| dhcp-smart-relay |     |     | <-- Enable | DHCP smart | relay |
| ---------------- | --- | --- | ---------- | ---------- | ----- |
!
| interface vlan | 2   |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
ip address 172.16.1.254/24 <-- Add the local IPS which will act
as GIADDR
| ip address | 10.10.610.254/24 | secondary |     |     |     |
| ---------- | ---------------- | --------- | --- | --- | --- |
ip helper-address 10.19.69.15 <-- Add the IP helpers to reach the
| required DHCP         | servers     |     |     |     |     |
| --------------------- | ----------- | --- | --- | --- | --- |
| ip helper-address     | 10.19.71.15 |     |     |     |     |
| DHCPv4 relay commands |             |     |     |     |     |
dhcp-relay
dhcp-relay
no dhcp-relay
Description
EnablesDHCPrelaysupport.DHCPrelayisenabledbydefault.DHCPrelayisnotsupportedonthe
managementinterface.
DHCP|75

ThenoformofthiscommanddisablesDHCPrelaysupport.
Examples
ThisexampleenablesDHCPrelaysupport.
| switch(config)# | dhcp-relay |     |     |
| --------------- | ---------- | --- | --- |
ThisexampleremovesDHCPrelaysupport.
| switch(config)#     | no      | dhcp-relay |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
config
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config)# | no  | dhcp-relay | hop-count-increment |
| --------------- | --- | ---------- | ------------------- |
| Command History |     |            |                     |
| Release         |     |            | Modification        |
| 10.07orearlier  |     |            | --                  |
76
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Command   | Information |     |         |           |     |
| --------- | ----------- | --- | ------- | --------- | --- |
| Platforms | Command     |     | context | Authority |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
validate
Validateoption82informationinDHCPserverresponsesand
dropinvalidresponses.
| drop |     |     |     | DropanyinboundclientDHCPpacketthatcontainsoption82 |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
information.
| keep |     |     |     | Keeptheexistingoption82fieldinaninboundclientDHCP |     |
| ---- | --- | --- | --- | ------------------------------------------------- | --- |
packet.TheremoteIDandcircuitIDinformationfromthefirst
relayagentispreserved.
source-interface ConfigurestheDHCPrelaytouseaconfiguredsourceIPaddress
forinter-VRFserverreachability.SetthesourceIPaddresswith
thecommandip source-interface.
| ip  |     |     |     | UsetheIPaddressoftheinterfaceonwhichtheclientDHCP |     |
| --- | --- | --- | --- | ------------------------------------------------- | --- |
packetenteredtheswitchastheoption82remoteID.
| mac |     |     |     | UsetheMACaddressoftheswitchastheoption82remoteID. |     |
| --- | --- | --- | --- | ------------------------------------------------- | --- |
Default.
Example
ThisexampleenablesDHCPoption82supportandreplacesalloption82informationwiththevalues
fromtheswitch,withtheswitchMACaddressastheremoteID.
| switch(config)# |         | dhcp-relay | option | 82 replace mac |     |
| --------------- | ------- | ---------- | ------ | -------------- | --- |
| Command         | History |            |        |                |     |
DHCP|77

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config)# |     | dhcp-smart-relay |     |
| --------------- | --- | ---------------- | --- |
DisablingDHCPSmartRelaysupport:
| switch(config)# |             | no dhcp-smart-relay |                    |
| --------------- | ----------- | ------------------- | ------------------ |
| Command         | History     |                     |                    |
| Release         |             |                     | Modification       |
| 10.10           |             |                     | Commandintroduced. |
| Command         | Information |                     |                    |
| Platforms       | Command     | context             | Authority          |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| diag-dump | dhcp-relay | basic |     |
| --------- | ---------- | ----- | --- |
| diag-dump | dhcp-relay | basic |     |
78
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |
| --------------------------- | --- | ------------------ | --- |

Description
DumpsDHCPrelayconfigurationsforallinterfaces.
Examples
ThisexampleenablesDHCPrelaysupport.
| switch# | diag-dump | dhcp-relay |     | basic |     |     |     |     |
| ------- | --------- | ---------- | --- | ----- | --- | --- | --- | --- |
=========================================================================
| [Start] | Feature | dhcp-relay |     | Time : Sun | Apr 26 06:38:10 |     | 2020 |     |
| ------- | ------- | ---------- | --- | ---------- | --------------- | --- | ---- | --- |
=========================================================================
-------------------------------------------------------------------------
| [Start] | Daemon | hpe-relay |     |     |     |     |     |     |
| ------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| DHCP Relay | :                   | 1             |           |                |             |     |                  |     |
| ---------- | ------------------- | ------------- | --------- | -------------- | ----------- | --- | ---------------- | --- |
| DHCP Relay | hop-count-increment |               |           | : 1            |             |     |                  |     |
| DHCP Relay | Option82            |               | : 1       |                |             |     |                  |     |
| DHCP Relay | Option82            |               | validate  | : 0            |             |     |                  |     |
| DHCP Relay | Option82            |               | policy    | : keep         |             |     |                  |     |
| DHCP Relay | Option82            |               | remote-id | : mac          |             |     |                  |     |
| DHCP Relay | Option82            |               | Source    | Intf : Disable |             |     |                  |     |
| DHCP Smart | Relay               | :             | Enable    |                |             |     |                  |     |
| System Mac | [f4:03:43:80:27:00] |               |           |                |             |     |                  |     |
| VRF :BLUE, | Source              | Ip:200.0.0.10 |           |                |             |     |                  |     |
| vsx: Not   | Present             |               |           |                |             |     |                  |     |
| Interface  | vlan2:              | 1             |           |                |             |     |                  |     |
| Client     | Packet              | Statistics:   |           |                |             |     |                  |     |
| Valid      |                     | Dropped       |           | O82_Valid      | O82_Dropped |     | vsx_drops        |     |
| -----      |                     | -------       |           | ---------      | ----------- |     | ---------        |     |
| 0          |                     | 0             |           | 0              | 0           |     | 0                |     |
| Server     | Packet              | Statistics:   |           |                |             |     |                  |     |
| Valid      |                     | Dropped       |           | O82_Valid      | O82_Dropped |     | Invalid_IP_Drops | To_ |
Dsnoop
----- ------- --------- ----------- ---------------- --------
-
| 0              |                 | 0       |         | 0         | 0           |      | 0   | 0   |
| -------------- | --------------- | ------- | ------- | --------- | ----------- | ---- | --- | --- |
| client request |                 | dropped | packets | with      | extn option | 82   | = 0 |     |
| client request |                 | valid   | packets | with extn | option      | 82 = | 0   |     |
| server request |                 | dropped | packets | with      | extn option | 82   | = 0 |     |
| server request |                 | valid   | packets | with extn | option      | 82 = | 0   |     |
| Port 67        | - 200.0.0.100,2 |         |         |           |             |      |     |     |
source vrf-BLUE.
| Interface | vlan3: | 1           |     |           |             |     |                  |     |
| --------- | ------ | ----------- | --- | --------- | ----------- | --- | ---------------- | --- |
| Client    | Packet | Statistics: |     |           |             |     |                  |     |
| Valid     |        | Dropped     |     | O82_Valid | O82_Dropped |     | vsx_drops        |     |
| -----     |        | -------     |     | --------- | ----------- |     | ---------        |     |
| 0         |        | 0           |     | 0         | 0           |     | 0                |     |
| Server    | Packet | Statistics: |     |           |             |     |                  |     |
| Valid     |        | Dropped     |     | O82_Valid | O82_Dropped |     | Invalid_IP_Drops | To_ |
Dsnoop
----- ------- --------- ----------- ---------------- --------
-
DHCP|79

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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip bootp-gateway
| ip bootp-gateway    |     | <IPV4-ADDR> |     |     |     |     |     |     |     |     |
| ------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| no ip bootp-gateway |     | <IPV4-ADDR> |     |     |     |     |     |     |     |     |
Description
ConfiguresagatewayaddressfortheDHCPrelayagenttouseforDHCPrequests.BydefaultDHCPrelay
agentpicksthelowest-numberedIPaddressontheinterface.
Thenoformofthiscommandremovesthegatewayaddress.
| Parameter |     |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
<IPV4-ADDR> SpecifiestheIPaddressofthegatewayinIPv4format(x.x.x.x),
wherexisaisadecimalnumberfrom0to255.
Examples
SettingtheIPaddressofthegatewayforinterfacevlan100to10.10.10.10:
80
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |

| switch(config)# |     | interface |     | vlan100 |     |
| --------------- | --- | --------- | --- | ------- | --- |
switch(config-if)#
|                     |         | ip  | bootp-gateway | 10.10.10.10  |     |
| ------------------- | ------- | --- | ------------- | ------------ | --- |
| Command History     |         |     |               |              |     |
| Release             |         |     |               | Modification |     |
| 10.07orearlier      |         |     |               | --           |     |
| Command Information |         |     |               |              |     |
| Platforms           | Command |     | context       | Authority    |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip helper-address
| ip helper-address    |     | <IPV4-ADDR> |     | [vrf <VRF-NAME>] |     |
| -------------------- | --- | ----------- | --- | ---------------- | --- |
| no ip helper-address |     | <IPV4-ADDR> |     | [vrf <VRF-NAME>] |     |
Description
DefinestheaddressofaremoteDHCPserverorDHCPrelayagent.Uptoeightaddressescanbe
defined.TheDHCPrelayagentforwardsDHCPclientrequeststoalldefinedservers.
IfIPhelperadddressisdefinedwithVRFargumentthenthiscommandrequiresyoudefineasourceIP
addressforDHCPrelaywiththecommand ip source-interface.TheconfiguredsourceIPontheVRF
isusedtoforwardDHCPpacketstotheserver.
AhelperaddresscannotbedefinedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
helper-address <IPV4-ADDR> SpecifiesthehelperIPaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
| vrf <VRF-NAME> |     |     |     | SpecifiesthenameofaVRF.Default:default. |     |
| -------------- | --- | --- | --- | --------------------------------------- | --- |
Examples
DefiningtheIPhelperaddress10.10.10.209oninterfacevlan100:
| switch(config)#         |     | interface |     | vlan100        |              |
| ----------------------- | --- | --------- | --- | -------------- | ------------ |
| switch(config-if-vlan)# |     |           | ip  | helper-address | 10.10.10.209 |
RemovingtheIPhelperaddress10.10.10.209oninterfacevlan100:
| switch(config-if-vlan)# |     |     | no  | ip helper-address | 10.10.10.209 |
| ----------------------- | --- | --- | --- | ----------------- | ------------ |
| Command History         |     |     |     |                   |              |
DHCP|81

| Release        |             |     |         | Modification |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show dhcp-relay
show dhcp-relay
Description
ShowsDHCPrelayconfigurationsettings.
Example
ShowingDHCPrelaysettings:
| switch(config)#  |             | show   | dhcp-relay |            |     |
| ---------------- | ----------- | ------ | ---------- | ---------- | --- |
| DHCP Relay       | Agent       |        |            | : enabled  |     |
| DHCP Smart       | Relay       |        |            | : enabled  |     |
| DHCP Request     | Hop         | Count  | Increment  | : enabled  |     |
| Option           | 82          |        |            | : enabled  |     |
| Source-Interface |             |        |            | : disabled |     |
| Response         | Validation  |        |            | : disabled |     |
| Option           | 82 Handle   | Policy |            | : replace  |     |
| Remote           | ID          |        |            | : mac      |     |
| DHCP Relay       | Statistics: |        |            |            |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |             | 60  | 10  |
| ---------- | ------ | --- | ----------- | --- | --- |
| DHCP Relay | Option | 82  | Statistics: |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50             |             | 8   |     | 50           | 8   |
| -------------- | ----------- | --- | --- | ------------ | --- |
| Command        | History     |     |     |              |     |
| Release        |             |     |     | Modification |     |
| 10.07orearlier |             |     |     | --           |     |
| Command        | Information |     |     |              |     |
82
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

| Platforms | Command | context |     |     | Authority                                            |
| --------- | ------- | ------- | --- | --- | ---------------------------------------------------- |
| 6200      |         |         |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show dhcp-relay | bootp-gateway |     |            |     |                   |
| --------------- | ------------- | --- | ---------- | --- | ----------------- |
| show dhcp-relay | bootp-gateway |     | [interface |     | <INTERFACE-NAME>] |
Description
Showsthebootpgatewaydefinedforallinterfacesoraspecificinterface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<INTERFACE-NAME> Specifiesaninterface.Format:member/slot/port.
Examples
Showingthedesignatedbootpgatewayforallinterfaces:
| switch(config)#      |         | show dhcp-relay |     | bootp-gateway |           |
| -------------------- | ------- | --------------- | --- | ------------- | --------- |
| BOOTP Gateway        | Entries |                 |     |               |           |
| Interface            |         | Source          | IP  |               |           |
| -------------------- |         | --------------- |     |               |           |
| vlan10               |         | 1.1.1.1         |     |               |           |
| vlan20               |         | 2.2.2.2         |     |               |           |
| Command History      |         |                 |     |               |           |
| Release              |         |                 |     | Modification  |           |
| 10.07orearlier       |         |                 |     | --            |           |
| Command Information  |         |                 |     |               |           |
| Platforms            | Command | context         |     |               | Authority |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
show ip helper-address
| show ip helper-address |     | [interface |     | <INTERFACE-ID>] |     |
| ---------------------- | --- | ---------- | --- | --------------- | --- |
Description
ShowstheIPhelperaddressesdefinedforallinterfacesoraspecificinterface.
DHCP|83

| Parameter |     |                |     |     | Description |     |
| --------- | --- | -------------- | --- | --- | ----------- | --- |
| interface |     | <INTERFACE-ID> |     |     |             |     |
Specifiesaninterface.Format:member/slot/port.
Examples
ShowingtheIPhelperaddressesforallinterfaces:
|     | switch(config)#   |           | show | ip helper-address |                   |     |
| --- | ----------------- | --------- | ---- | ----------------- | ----------------- | --- |
|     | IP Helper         | Addresses |      |                   |                   |     |
|     | Interface:        | vlan11    |      |                   |                   |     |
|     | IP Helper         | Address   |      |                   | VRF               |     |
|     | ----------------- |           |      |                   | ----------------- |     |
|     | 10.10.10.209      |           |      |                   | default           |     |
|     | Interface:        | vlan20    |      |                   |                   |     |
|     | IP Helper         | Address   |      |                   | VRF               |     |
|     | ----------------- |           |      |                   | ----------------- |     |
|     | 3.3.3.3           |           |      |                   | default           |     |
|     | 20.20.20.20       |           |      |                   | default           |     |
ShowingtheIPhelperaddressesforinterfacevlan20:
|                | switch(config)#   |             | show | ip helper-address | interface         | vlan20 |
| -------------- | ----------------- | ----------- | ---- | ----------------- | ----------------- | ------ |
|                | IP Helper         | Addresses   |      |                   |                   |        |
|                | Interface:        | vlan20      |      |                   |                   |        |
|                | IP Helper         | Address     |      |                   | VRF               |        |
|                | ----------------- |             |      |                   | ----------------- |        |
|                | 3.3.3.3           |             |      |                   | default           |        |
|                | 20.20.20.20       |             |      |                   | default           |        |
| Command        |                   | History     |      |                   |                   |        |
| Release        |                   |             |      |                   | Modification      |        |
| 10.07orearlier |                   |             |      |                   | --                |        |
| Command        |                   | Information |      |                   |                   |        |
| Platforms      |                   | Command     |      | context           | Authority         |        |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| DHCPv6      |     | relay | agent  |             |     |     |
| ----------- | --- | ----- | ------ | ----------- | --- | --- |
| Configuring |     | the   | DHCPv6 | relay agent |     |     |
Prerequisites
84
| AOS-CX10.11IPServicesGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- |

Procedure
1. EnabletheDHCPv6relayagentwiththecommanddhcpv6-relay.
2. ConfigureoneormoreIPhelperaddresseswiththecommandipv6 helper-address.This
determineswheretheDHCPv6agentforwardDHCPrequests.
3. IfyouwanttoenableDHCPoption79supporttoforwardclientlink-layeraddresses,usethe
| commanddhcpv6-relay |     | option 79. |     |
| ------------------- | --- | ---------- | --- |
4. ReviewDHCPv6relayagentconfigurationsettingswiththecommandsshow dhcpv6-relayand
| show ipv6 helper-address. |     |     |     |
| ------------------------- | --- | --- | --- |
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablestheDHCPv6relayagent.
n Enablesinterface1/1/2andassignsanIPv6addresstoit.(Bydefault,allinterfacesarelayer3and
disabled.)
n DefinesanIPhelperaddressofFF01::1:1000oninterface1/1/2.
n EnablesDHCPoption79.
| switch(config)#    | dhcpv6-relay |                     |                 |
| ------------------ | ------------ | ------------------- | --------------- |
| switch(config)#    | interface    | 1/1/1               |                 |
| switch(config-if)# | no shutdown  |                     |                 |
| switch(config-if)# | ipv6         | address 2002::22/64 |                 |
| switch(config-if)# | ipv6         | helper-address      | unicast 2001::1 |
switch(config-if)# ipv6 helper-address multicast ff01::1:1000 egress 1/1/1
switch(config-if)# ipv6 helper-address multicast all-dhcp-servers egress 1/1/1
| switch(config-if)# | exit        |                     |                 |
| ------------------ | ----------- | ------------------- | --------------- |
| switch(config)#    | interface   | 1/1/2               |                 |
| switch(config-if)# | no shutdown |                     |                 |
| switch(config-if)# | ipv6        | address 2002::21/64 |                 |
| switch(config-if)# | ipv6        | helper-address      | unicast 2001::1 |
switch(config-if)# ipv6 helper-address multicast ff01::1:1000 egress 1/1/1
switch(config-if)# ipv6 helper-address multicast all-dhcp-servers egress 1/1/1
| switch(config-if)# | exit |     |     |
| ------------------ | ---- | --- | --- |
| switch(config)#    | end  |     |     |
Use Case
ThissectionexplaintheusecasesforDHCPv6relayagent.
| DHCPv6 relay scenario | 1   |     |     |
| --------------------- | --- | --- | --- |
Inthisscenario,DHCPrelayontheswitchenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
DHCP|85

Procedure
1. EnableDHCPrelay.
switch# config
switch(config)#
dhcpv6-relay
2. DefineanIPv6helperaddress.
| n Oninterfacevlan       | 10and | vlan         | 20.                 |             |                 |
| ----------------------- | ----- | ------------ | ------------------- | ----------- | --------------- |
| switch(config)#         |       | dhcpv6-relay |                     |             |                 |
| switch(config)#         |       | interface    | 1/1/1               |             |                 |
| switch(config)#         |       | no shutdown  |                     |             |                 |
| switch(config-if)#      |       | vlan         | access 10           |             |                 |
| switch(config-if)#      |       | exit         |                     |             |                 |
| switch(config)#         |       | interface    | 1/1/2               |             |                 |
| switch(config)#         |       | no shutdown  |                     |             |                 |
| switch(config-if)#      |       | vlan         | access 20           |             |                 |
| switch(config-if)#      |       | exit         |                     |             |                 |
| switch(config)#         |       | interface    | vlan 10             |             |                 |
| switch(config-if-vlan)# |       |              | no shutdown         |             |                 |
| switch(config-if-vlan)# |       |              | ipv6 address        | 2002::22/64 |                 |
| switch(config-if-vlan)# |       |              | ipv6 helper-address |             | unicast 2001::1 |
switch(config-if-vlan)# ipv6 helper-address multicast ff01::1:1000 egress
vlan30
switch(config-if-vlan)# ipv6 helper-address multicast all-dhcp-servers
| egress vlan50           |     |           |                     |             |                 |
| ----------------------- | --- | --------- | ------------------- | ----------- | --------------- |
| switch(config-if-vlan)# |     |           | exit                |             |                 |
| switch(config)#         |     | interface | vlan 20             |             |                 |
| switch(config-if-vlan)# |     |           | no shutdown         |             |                 |
| switch(config-if-vlan)# |     |           | ipv6 address        | 2002::21/64 |                 |
| switch(config-if-vlan)# |     |           | ipv6 helper-address |             | unicast 2001::1 |
switch(config-if-vlan)# ipv6 helper-address multicast ff01::1:1000 egress
vlan30
switch(config-if-vlan)# ipv6 helper-address multicast all-dhcp-servers
86
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

| egress                  | vlan50 |      |     |
| ----------------------- | ------ | ---- | --- |
| switch(config-if-vlan)# |        | exit |     |
| switch(config)#         | end    |      |     |
3. VerifyDHCPrelayconfiguration.
| n Wheninterfacevlan                            | 10andvlan                | 20isconfiguredasrelay. |              |
| ---------------------------------------------- | ------------------------ | ---------------------- | ------------ |
| switch#                                        | show dhcpv6-relay        |                        |              |
| DHCPv6                                         | Relay Agent :            | enabled                |              |
| Option                                         | 79 :                     | disabled               |              |
| switch#                                        | show ipv6 helper-address |                        |              |
| IP Helper                                      | Addresses                |                        |              |
| Interface:                                     | vlan10                   |                        |              |
| IP Helper                                      | Address                  |                        | Egress Port  |
| ---------------------------------------------- |                          |                        | ------------ |
all-dhcp-servers vlan50
ff01::1:1000 vlan30
2001::1 -
| Interface: | vlan20  |     |             |
| ---------- | ------- | --- | ----------- |
| IP Helper  | Address |     | Egress Port |
----------------------------------------------------------
all-dhcp-servers vlan50
ff01::1:1000 vlan30
2001::1 -
n Wheninterface1/1/1and1/1/2isconfiguredasrelay.
| switch#     | show dhcpv6-relay        |     |             |
| ----------- | ------------------------ | --- | ----------- |
| DHCPv6      | Relay Agent : enabled    |     |             |
| Option      | 79 : disabled            |     |             |
| switch#     | show ipv6 helper-address |     |             |
| Interface:  | 1/1/1                    |     |             |
| IPv6 Helper | Address                  |     | Egress Port |
---------------------------------------------------------
| all-dhcp-servers |         |     | 1/1/3       |
| ---------------- | ------- | --- | ----------- |
| ff01::1:1000     |         |     | 1/1/3       |
| 2001::1          |         |     | -           |
| Interface:       | 1/1/2   |     |             |
| IPv6 Helper      | Address |     | Egress Port |
--------------------------------------------------------
| all-dhcp-servers  |          |     | 1/1/3 |
| ----------------- | -------- | --- | ----- |
| ff01::1:1000      |          |     | 1/1/3 |
| 2001::1           |          |     | -     |
| DHCP relay (IPv6) | commands |     |       |
dhcpv6-relay
dhcpv6-relay
no dhcpv6-relay
Description
DHCP|87

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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Command History |     |              |           |
88
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

6200

config

Administrators or local user group members with execution rights
for this command.

ipv6 helper-address

ipv6 helper-address unicast <UNICAST-IPV6-ADDR>
no ipv6 helper-address unicast <UNICAST-IPV6-ADDR>
ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>
no ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-
NUM>

Description

Defines the address of a remote DHCPv6 server or DHCPv6 relay agent. Up to eight addresses can be
defined. The DHCPv6 agent forwards DHCPv6 client requests to all defined servers.

Not supported on the OOBM interface.

The no form of this command removes an IP helper address.

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

DHCP | 89

switch(config-if)# no ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress
1/1/2
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show dhcpv6-relay
show dhcpv6-relay
Description
ShowsDHCPrelayconfigurationsettings.
Example
| switch#        | show dhcpv6-relay |            |              |
| -------------- | ----------------- | ---------- | ------------ |
| DHCPv6         | Relay Agent       | : enabled  |              |
| Option         | 79                | : disabled |              |
| Command        | History           |            |              |
| Release        |                   |            | Modification |
| 10.07orearlier |                   |            | --           |
| Command        | Information       |            |              |
| Platforms      | Command           | context    | Authority    |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show ipv6 | helper-address |            |                 |
| --------- | -------------- | ---------- | --------------- |
| show ipv6 | helper-address | [interface | <INTERFACE-ID>] |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
90
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Parameter |                |     | Description |     |     |
| --------- | -------------- | --- | ----------- | --- | --- |
| interface | <INTERFACE-ID> |     |             |     |     |
Specifiesaninterface.Format:member/slot/port.
Examples
| switch#                                        | show ipv6   | helper-address |              |             |         |
| ---------------------------------------------- | ----------- | -------------- | ------------ | ----------- | ------- |
| Interface:                                     | 1/1/1       |                |              |             |         |
| IPv6 Helper                                    | Address     |                |              | Egress Port |         |
| ---------------------------------------------- |             |                |              | ----------- |         |
| 2001:db8:0:1::                                 |             |                |              | -           |         |
| FF01::1:1000                                   |             |                |              | 1/1/2       |         |
| Interface:                                     | 1/1/2       |                |              |             |         |
| IPv6 Helper                                    | Address     |                |              | Egress Port |         |
| --------------------------------------------   |             |                |              | ----------- |         |
| 2001:db8:0:1::                                 |             |                |              | -           |         |
| switch#                                        | show ipv6   | helper-address | interface    | 1/1/1       |         |
| Interface:                                     | 1/1/1       |                |              |             |         |
| IPv6 Helper                                    | Address     |                |              | Egress Port |         |
| ---------------------------------------------- |             |                |              | ----------- |         |
| 2001:db8:0:1::                                 |             |                |              | -           |         |
| FF01::1:1000                                   |             |                |              | 1/1/2       |         |
| switch#                                        | show ipv6   | helper-address | interface    | vlan20      |         |
| Interface:                                     | vlan20      |                |              |             |         |
| IP Helper                                      | Address     |                |              | Egress Port |         |
| ---------------------------------------------- |             |                |              | ----------- |         |
| 2001::1                                        |             |                |              | -           |         |
| ff01::1:1000                                   |             |                |              | vlan30      | default |
| Command                                        | History     |                |              |             |         |
| Release                                        |             |                | Modification |             |         |
| 10.07orearlier                                 |             |                | --           |             |         |
| Command                                        | Information |                |              |             |         |
| Platforms                                      | Command     | context        | Authority    |             |         |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
Troubleshooting
| One or more | DHCP clients | not getting | IP address |     |     |
| ----------- | ------------ | ----------- | ---------- | --- | --- |
DHCP|91

n Reachability between relay and server(s)—Server reachability is required for DHCP Relay function to

work.

1.Ping to check IP reachability between switch and the server(s).

2.Confirm the ping test is made in the appropriate VRF and with the correct gateway IP. By default,
DHCP Relay picks the lowest IP address on the client-connected interface as the gateway IP address.

When configured, the bootp-gateway IP address is used as the gateway IP.

n Source-ip configuration—With the source-ip configuration in the VRF, DHCP relay uses it as a gateway

IP address to communicate with the DHCP server.

1.

It requires dhcp_relay source-interface configuration for ip source-interface relay to
work.

2. Ping the server with source-ip as the configured source-interface IP. The same test is

applicable for the Inter-VRF route leak (IVRL) configuration.

3.

If the client and server are in different VRFs, test server reachability in server-VRF by using
configured source-interface IP.

n Option-82 conflict with DHCP snooping and Relay [DHCPv4 Specific]

AOS-CX supports configuring DHCP snooping and DHCP relay on the same VLAN. In cases where DHCP
relay is configured to use source-interface along with inter-vrf server, Option 82 is added to the
packet sent to the server.

If Option 82 is enabled for both DHCP snooping and DHCP relay, DHCP snooping gets the priority. In this
scenario for DHCP relay to work, disable Option-82 for DHCP snooping.

n Check if the helper-address is configured to the correct VRF where the DHCP server is rechable

n CoPP drop checks—In case of excessive DHCP traffic, CoPP does the rate limit by dropping some of

the packets.

Check if client packets are getting dropped by CoPP using show copp statistics class dhcp-ipv4 or

show copp statistics class dhcp-ipv6 commands.

n Server pool configuration and exhaustion

1. Check the server side configuration to see if IP lease criteria is being met for the client.

2. Check if the right VRF selection is happening for the lease allocation.

DHCP Smart-Relay

It allows the DHCP relay agent to use non-lower IP addresses from the client-connected interfaces as
giaddr and for pool selection when the DHCP server does not reply to the DHCP discover messages with
the lowest IP address. More than one IP address and helper address must be configured on the client-
connected interfaces. The server must be configured with the DHCPv4 pools for the client-connected IP
addresses

n Server Reachability

Ensure the ping test is made in the appropriate VRF and with the correct gateway IP (IPs from the client-
connected interfaces).

n Bootp gateway IP configuration

When a bootp gateway IP is configured, it gets the highest priority and is used as a gateway IP.

n Source-ip configuration

When a source IP is configured, Option 82 needs to be enabled. The Source IP is used as a gateway IP, and
Option 82 is used as sub-option 5 contains the IP used for the pool selection.

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

92

n Client Cache and timeout

For debugging, a client cache is built, which contains information on the gateway IP for every client.

The entry is added to the client cache for the client which does not have an existing entry. The client
entries are deleted if the client is idle for 360 seconds. In other cases, a particular client entry might get
deleted if it is the oldest entry in time and if the client cache is full. The client cache is deleted completely
if the functionality is disabled.

It uses the lowest IP address as giaddr or for pool selection when all client-connected IPs are exhausted
or the client retries after an idle timeout. The client cache is rebuilt upon HA and VSF switchover, VSX-MM
(redundancy) switchover, and reboot of the switch.

DHCP server
The dynamic host configuration protocol (DHCP) enables a server to automate the assignment of IP
addresses, and other networking settings, to host computers. The DHCP server on the switch provides
both IPv4 and IPv6 support and is independently configurable on each VRF.

Protocol and feature details

Key features

n Supports multiple address pools and static address bindings.

n Supports DHCP options, enabling the server to provide additional information about the network

when DHCP clients request an address.

n Supports BOOTP to distribute boot image files using an external TFTP server.

n VRF aware, meaning that DHCP client requests received on an interface are processed by the DHCP
server instance configured for a VRF. DHCP server responses are forwarded to clients on the VRF.

n Supports external storage of lease information on a remote host. This enables the DHCP server to
restore lease information after a reboot or a failure. Lease information is stored in a flat file on the
configured external device. It is important that the external device provide persistent external
storage to allow restoration of lease information. If external storage is not configured, then after a
failure or reboot, all existing lease information is lost.

DHCP relay interoperation

Both DHCP relay and DHCP server can be configured on the same VRF.

DHCP snooping interoperation

DHCP snooping can not be configured with DHCP server.

Supported platform and standards

The following table list the supported platforms for DHCPv4 server and DHCPv6 server.

Table 1: Support platforms for DHCPv4 server and DHCPv6 server

Platform

6200

DHCPv4 server

DHCPv6 server

Yes

Yes

The below limit is based on system stability.

DHCP | 93

n SingleVRF
o Maximumpools—64
o Maximumrange—64(Everypoolhavingonerange)
o Onestatichostperpool
o Maximumclients-8192(Everyrangeproviding128leases)
n Across32VRF's
o Maximumpools-64(EveryVRFhaving2pools)
o Maximumrange-64(Everypoolhavingonerange)
o Onestatichostperpool
o Maximumclients-8192(Everyrangeproviding128leases)
| Configuring | a DHCPv4 | server on | a VRF |
| ----------- | -------- | --------- | ----- |
Prerequisites
Anenabledlayer3interface.
n
n AVRF.
n AnexternalTFTPservertohostBOOTPimagefiles(optional).
n Anexternalstoragedeviceinstalledandconfigured(optional).
Procedure
1. AssigntheDHCPv4servertoaVRFwiththecommanddhcp-server vrf.Thisswitchestothe
DHCPv4serverconfigurationcontext.
2. IfyouwanttheDHCPv4servertobethesoleauthorityforIPaddressesontheVRF,enable
authoritativemodewiththecommandauthoritative.
3. DefineanaddresspoolfortheVRFwiththecommandpool.ThisswitchestotheDHCPv4server
poolcontext.Customizepoolsettingsasfollows:
| a. Definetherangeofaddressesinthepoolwiththecommandrange.    |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- |
| b. Settheleasetimeforaddressesinthepoolwiththecommandlease.  |     |     |     |
| c. Setthedomainnameforthepoolwiththecommanddomain-name.      |     |     |     |
| d. Defineuptofourdefaultrouterswiththecommanddefault-router. |     |     |     |
| e. DefineuptofourDNSserverswiththecommanddns-server.         |     |     |     |
f. Createstaticbindingsforspecificaddressesinthepoolwiththecommandstatic-bind.
g. ConfigurecustomDHCPv4optionsforthepoolwiththecommandoption.
h. ConfigureNetBIOSsupportwiththecommandsnetbios-name-serverandnetbios-node-
type.
| i. ConfigureBOOTPoptionswiththecommandbootp.         |     |     |     |
| ---------------------------------------------------- | --- | --- | --- |
| j. ExittheDHCPv4serverpoolcontextwiththecommandexit. |     |     |     |
4. EnabletheDHCPserverontheVRFwiththecommandenable.
5. ConfiguresupportforpersistentexternalstorageofDHCPsettingswiththecommanddhcp-
external-storage.
server
6. ViewDHCPv4serverconfigurationsettingswiththecommandshow dhcp-server all-vrfs.
Example
Thisexamplecreatesthefollowingconfiguration:
94
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

n ConfigurestheDHCPv4serveronVRFprimary-vrf.
n Enablesauthoritativemode.
Definesthepoolprimary-poolwiththefollowingsettings:
n
o Addressrange:10.0.0.1to10.0.0.100.
o Leasetime:12hours.
o Domainname:example.org.in.
o Defaultrouters:10.30.30.1and10.30.30.2.
o DNSservers:125.0.0.1and125.0.0.2.
o Staticbindingof10.0.0.11forMACaddress24:be:05:24:75:73.
o
DHCPcustomoption3withIPaddress10.30.30.3.
n EnablestheDHCPv4server.
| switch(config)#                  | dhcp-server | vrf primary       |                     |
| -------------------------------- | ----------- | ----------------- | ------------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |                     |
| switch(config-dhcp-server-pool)# |             | range             | 10.0.0.1 10.0.0.100 |
| switch(config-dhcp-server-pool)# |             | lease             | 12:00:00            |
| switch(config-dhcp-server-pool)# |             | domain-name       | example.org.in      |
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
5. ConfiguresupportforpersistentexternalstorageofDHCPsettingswiththecommanddhcpv6-
DHCP|95

| server external-storage. |     |     |     |
| ------------------------ | --- | --- | --- |
6. ViewDHCPv6serverconfigurationsettingswiththecommandshow dhcpv6-server all-vrfs.
Example
Thisexamplecreatesthefollowingconfiguration:
n ConfiguresaDHCPv6serveronVRFprimary-vrf.
n Enablesauthoritativemode.
n Definesthepoolprimary-poolwiththefollowingsettings:
o Addressrange:2001::1to2001::100.
o
Leasetime:12hours.
o DNSservers:2101::14and2101::14.
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
96
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

| switch(config)# | dhcp-server | vrf | primary |
| --------------- | ----------- | --- | ------- |
switch(config-dhcp-server)#
|                     |         | no      | authoritative |
| ------------------- | ------- | ------- | ------------- |
| Command History     |         |         |               |
| Release             |         |         | Modification  |
| 10.07orearlier      |         |         | --            |
| Command Information |         |         |               |
| Platforms           | Command | context | Authority     |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
bootp
bootp <REMOTE-URL>
| no bootp <REMOTE-URL> |     |     |     |
| --------------------- | --- | --- | --- |
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
<FILE>:SpecifiesthenameoftheBOOTPfile.Range:1to64
n
printableASCIIcharacters.
Example
DefinesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf  | primary      |
| --------------------------- | ----------- | ---- | ------------ |
| switch(config-dhcp-server)# |             | pool | primary-pool |
switch(config-dhcp-server-pool)# bootp tftp://10.0.0.1/mybootfile
DeletesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
DHCP|97

| switch(config)# | dhcp-server |     | vrf primary |     |
| --------------- | ----------- | --- | ----------- | --- |
switch(config-dhcp-server)#
|     |     |     | pool primary-pool |     |
| --- | --- | --- | ----------------- | --- |
switch(config-dhcp-server-pool)# no bootp tftp://10.0.0.1/mybootfile
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| clear dhcp-server | leases |     |     |     |
| ----------------- | ------ | --- | --- | --- |
clear dhcp-server leases [all-vrfs | <IPV4-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv4serverleaseinformation.TheDHCPv4servermustbedisabledbeforeclearinglease
information.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
all-vrfs
ClearsleasesforallVRFs.
<IPV4-ADDR> vrf <VRF-NAME> ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| vrf <VRF-NAME> |     |     | ClearsleasesforaspecificVRF. |     |
| -------------- | --- | --- | ---------------------------- | --- |
Examples
ClearingallDHCPv4serverleases.
| switch(config)#             | dhcp-server       |     | vrf primary |     |
| --------------------------- | ----------------- | --- | ----------- | --- |
| switch(config-dhcp-server)# |                   |     | disable     |     |
| switch(config-dhcp-server)# |                   |     | exit        |     |
| switch(config)#             | exit              |     |             |     |
| switch#                     | clear dhcp-server |     | leases      |     |
ClearingallDHCPv4serverleasesforVRFprimary-vrf.
| switch(config)#             | dhcp-server |     | vrf primary |     |
| --------------------------- | ----------- | --- | ----------- | --- |
| switch(config-dhcp-server)# |             |     | disable     |     |
| switch(config-dhcp-server)# |             |     | exit        |     |
98
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| switch(config)# |     | exit |     |     |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- |
switch#
|     | clear | dhcp-server |     | leases | vrf primary-vrf |     |
| --- | ----- | ----------- | --- | ------ | --------------- | --- |
CleartheDHCPv4serverleaseforIPaddress10.10.10.1onVRFprimary-vrf.
| switch(config)#             |             | dhcp-server |         | vrf     | primary      |                 |
| --------------------------- | ----------- | ----------- | ------- | ------- | ------------ | --------------- |
| switch(config-dhcp-server)# |             |             |         | disable |              |                 |
| switch(config-dhcp-server)# |             |             |         | exit    |              |                 |
| switch(config)#             |             | exit        |         |         |              |                 |
| switch#                     | clear       | dhcp-server |         | leases  | 10.10.10.1   | vrf primary-vrf |
| Command                     | History     |             |         |         |              |                 |
| Release                     |             |             |         |         | Modification |                 |
| 10.07orearlier              |             |             |         |         | --           |                 |
| Command                     | Information |             |         |         |              |                 |
| Platforms                   |             | Command     | context |         | Authority    |                 |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
default-router
| default-router    |     | <IPV4-ADDR-LIST> |     |     |     |     |
| ----------------- | --- | ---------------- | --- | --- | --- | --- |
| no default-router |     | <IPV4-ADDR-LIST> |     |     |     |     |
Description
DefinesuptofourdefaultroutersforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddefaultroutersfromthepool.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesofthedefaultroutersinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.Youcan
removeleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.Separate
addresseswithaspace.AmaximumoffourIPaddressescanbe
defined.
Example
Definestwodefaultrouters,10.0.0.1and10.0.0.10,fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             |     | dhcp-server |     | vrf  | primary      |     |
| --------------------------- | --- | ----------- | --- | ---- | ------------ | --- |
| switch(config-dhcp-server)# |     |             |     | pool | primary-pool |     |
switch(config-dhcp-server-pool)# default-router ip 10.0.0.1 10.0.0.10
Deletesthedefaultrouter10.0.0.1fromtheserverpoolprimary-poolonVRFprimary.
DHCP|99

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
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
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
DisablesstorageoftheleasefileonexternalstoragevolumeStorage1infileLeaseFile.
100
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

switch(config)# no dhcp-server external-storage Storage1 file LeaseFile delay 600
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcp-server    | vrf            |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| dhcp-server    | vrf <VRF-NAME> |     |     |     |
| no dhcp-server | vrf <VRF-NAME> |     |     |     |
Description
ConfigurestheDHCPv4servertosupportaVRFandchangestotheconfig-dhcp-servercontextfor
thatVRF.
ThenoformofthiscommandremovesDHCPv4serversupportonaVRF.
| Parameter  |     |     |     | Description |
| ---------- | --- | --- | --- | ----------- |
| <VRF-NAME> |     |     |     | NameofaVRF. |
Example
ConfiguresDHCPv4serversupportonVRFprimary.
| switch(config)# | dhcp-server |     | vrf | primary |
| --------------- | ----------- | --- | --- | ------- |
RemovesDHCPv4serversupportonVRFprimary.
| switch(config)#     | no  | dhcp-server |     | vrf primary  |
| ------------------- | --- | ----------- | --- | ------------ |
| Command History     |     |             |     |              |
| Release             |     |             |     | Modification |
| 10.07orearlier      |     |             |     | --           |
| Command Information |     |             |     |              |
DHCP|101

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
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
(x.x.x.x),wherexisadecimalnumberfrom0to255.Separate
addresseswithaspace.
Example
DefinesDNSserversfortheserverpoolprimary-poolonVRFprimary.
102
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| switch(config)# | dhcp-server |     | vrf primary |     |     |
| --------------- | ----------- | --- | ----------- | --- | --- |
switch(config-dhcp-server)#
|                                  |     |     | pool primary-pool |     |           |
| -------------------------------- | --- | --- | ----------------- | --- | --------- |
| switch(config-dhcp-server-pool)# |     |     | dns-server        |     | 10.0.20.1 |
DeletesaDNSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server |         | vrf primary       |            |           |
| -------------------------------- | ----------- | ------- | ----------------- | ---------- | --------- |
| switch(config-dhcp-server)#      |             |         | pool primary-pool |            |           |
| switch(config-dhcp-server-pool)# |             |         | no                | dns-server | 10.0.20.1 |
| Command History                  |             |         |                   |            |           |
| Release                          |             |         | Modification      |            |           |
| 10.07orearlier                   |             |         | --                |            |           |
| Command Information              |             |         |                   |            |           |
| Platforms                        | Command     | context |                   | Authority  |           |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
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
| switch(config)#                  | dhcp-server |     | vrf primary       |     |                |
| -------------------------------- | ----------- | --- | ----------------- | --- | -------------- |
| switch(config-dhcp-server)#      |             |     | pool primary-pool |     |                |
| switch(config-dhcp-server-pool)# |             |     | domain-name       |     | example.org.in |
Deletesadomainnamefromtheserverpoolprimary-poolonVRFprimary.
switch(config)#
|                                  | dhcp-server |     | vrf primary       |             |                |
| -------------------------------- | ----------- | --- | ----------------- | ----------- | -------------- |
| switch(config-dhcp-server)#      |             |     | pool primary-pool |             |                |
| switch(config-dhcp-server-pool)# |             |     | no                | domain-name | example.org.in |
DHCP|103

| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
enable
enable
Description
EnablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhen
configuredonaVRF.
Example
EnablestheDHCPv4serveronVRFprimary.
| switch(config)#             | dhcp-server |         | vrf primary  |     |
| --------------------------- | ----------- | ------- | ------------ | --- |
| switch(config-dhcp-server)# |             |         | enable       |     |
| Command History             |             |         |              |     |
| Release                     |             |         | Modification |     |
| 10.07orearlier              |             |         | --           |     |
| Command Information         |             |         |              |     |
| Platforms                   | Command     | context | Authority    |     |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lease
| lease {<TIME> | | infinite} |     |     |     |
| ------------- | ----------- | --- | --- | --- |
no lease
Description
SetsthelengthoftheDHCPv4leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv4clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv4leasetimetoitsdefaultvalue1hour.
104
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Parameter |     | Description                                     |     |
| --------- | --- | ----------------------------------------------- | --- |
| <TIME>    |     | SetstheDHCPv4leasetime.Format:DD:HH:MM.Default: |     |
01:00:00.
infinite SetstheDHCPv4leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
Example
SetstheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimaryto12hours.
| switch(config)#                  | dhcp-server | vrf primary       |          |
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
config-dhcp-server-pool
| 6200 |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
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
DHCP|105

DefinestwoWINSserversfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf  | primary      |     |
| --------------------------- | ----------- | ---- | ------------ | --- |
| switch(config-dhcp-server)# |             | pool | primary-pool |     |
switch(config-dhcp-server-pool)# netbios-name-server ip 10.0.20.1 10.0.30.10
DeletesaWINSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)# | dhcp-server | vrf | primary |     |
| --------------- | ----------- | --- | ------- | --- |
switch(config-dhcp-server)#
|     |     | pool | primary-pool |     |
| --- | --- | ---- | ------------ | --- |
switch(config-dhcp-server-pool)# no netbios-name-server ip 10.0.20.1
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
netbios-node-type
| netbios-node-type    | <TYPE> |     |     |     |
| -------------------- | ------ | --- | --- | --- |
| no netbios-node-type | <TYPE> |     |     |     |
Description
DefinestheNetBIOSnodetypeforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovestheNetBIOSnodetypeforthecurrentpool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<TYPE>
SpecifiestheNetBIOSnodetype:broadcast,hybrid,mixed,or
peer-to-peer.
Examples
DefinestheNetBIOSnodetypebroadcastfortheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf  | primary           |           |
| -------------------------------- | ----------- | ---- | ----------------- | --------- |
| switch(config-dhcp-server)#      |             | pool | primary-pool      |           |
| switch(config-dhcp-server-pool)# |             |      | netbios-node-type | broadcast |
DeletestheNetBIOSnodetypebroadcastfromtheDHCPv4serverpoolprimary-poolonVRFprimary.
106
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| switch(config)# | dhcp-server |     | vrf primary |     |
| --------------- | ----------- | --- | ----------- | --- |
switch(config-dhcp-server)#
|     |     |     | pool primary-pool |     |
| --- | --- | --- | ----------------- | --- |
switch(config-dhcp-server-pool)# no netbios-node-type broadcast
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
Description
DefinescustomDHCPv4optionsforthecurrentDHCPv4serverpool.DHCPv4optionsenablethe
DHCPv4servertoprovideadditionalinformationaboutthenetworkwhenDHCPv4clientsrequestan
address.
ThenoformofthiscommandremovescustomDHCPv4optionsfromthepool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<OPTION-NUM> SpecifiesaDHCPv4optionnumber.ForalistofDHCPv4option
numbers,seehttps://www.iana.org/assignments/bootp-dhcp-
parameters/bootp-dhcp-parameters.xhtml.Range:2to254.
ascii <ASCII-STR>
SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:
1to255ASCIIcharacters.
hex <HEX-STR> Specifiesavaluefortheselectedoptionasahexadecimalstring.
Range:1to255hexadecimalcharacters.
ip <IPV4-ADDR-LIST> SpecifiesalistofIPaddressesinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server |     | vrf primary       |                  |
| -------------------------------- | ----------- | --- | ----------------- | ---------------- |
| switch(config-dhcp-server)#      |             |     | pool primary-pool |                  |
| switch(config-dhcp-server-pool)# |             |     | option            | 3 ip 192.168.1.1 |
DeletesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
DHCP|107

| switch(config)# | dhcp-server |     | vrf primary |     |
| --------------- | ----------- | --- | ----------- | --- |
switch(config-dhcp-server)#
|                                  |         |         | pool primary-pool |                         |
| -------------------------------- | ------- | ------- | ----------------- | ----------------------- |
| switch(config-dhcp-server-pool)# |         |         | no                | option 3 ip 192.168.1.1 |
| Command History                  |         |         |                   |                         |
| Release                          |         |         | Modification      |                         |
| 10.07orearlier                   |         |         | --                |                         |
| Command Information              |         |         |                   |                         |
| Platforms                        | Command | context |                   | Authority               |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
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
<POOL-NAME> SpecifiestheDHCPv4poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |
| --------------------------- | ----------- | --- | ----------------- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |
switch(config-dhcp-server-pool)#
DeletestheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary |              |
| --------------------------- | ----------- | --- | ----------- | ------------ |
| switch(config-dhcp-server)# |             |     | no pool     | primary-pool |
| Command History             |             |     |             |              |
108
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Release             |         |         | Modification |     |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier      |         |         | --           |     |     |     |
| Command Information |         |         |              |     |     |     |
| Platforms           | Command | context | Authority    |     |     |     |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
range
| range <LOW-IPV4-ADDR>    |     | <HIGH-IPV4-ADDR> | [prefix-len | <MASK>] |     |     |
| ------------------------ | --- | ---------------- | ----------- | ------- | --- | --- |
| no range <LOW-IPV4-ADDR> |     | <HIGH-IPV4-ADDR> | [prefix-len | <MASK>] |     |     |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv4serverpool.Amaximumof64
rangesaresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
| Parameter |     |     | Description |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- |
<LOW-IPV4-ADDR> SpecifiesthelowestIPaddressinthepoolinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
<HIGH-IPV4-ADDR> SpecifiesthehighestIPaddressinthepoolinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
prefix-len <MASK> SpecifiesthenumberofbitsintheaddressmaskinCIDRformat(x),
wherexisadecimalnumberfrom0to32.
NOTE:Whenactivegatewayisconfiguredontheinterfaceserviced
bythepool,youmustspecifyaprefixlengththatmatchesthemask
ontheIPaddressassignedtotheinterface.Otherwise,client
stationswillgetaprefixlengthfromactivegatewaythatmaynotbe
consistentwiththeconfiguredrange,andaDHCPerrorwilloccur.In
thefollowingexample,theDHCPrangeprefixissetto16tomatch
themaskontheIPaddressassignedtointerfaceVLAN2.
|     |     |     | switch(config)#         | interface | vlan 2         |              |
| --- | --- | --- | ----------------------- | --------- | -------------- | ------------ |
|     |     |     | switch(config-if-vlan)# |           | ip address     | 200.1.1.1/16 |
|     |     |     | switch(config-if-vlan)# |           | active-gateway | ip 200.1.1.3 |
mac 00:aa:aa:aa:aa:aa
|     |     |     | switch(config-if-vlan)#          |             | exit |                   |
| --- | --- | --- | -------------------------------- | ----------- | ---- | ----------------- |
|     |     |     | switch(config)#                  | dhcp-server | vrf  | primary           |
|     |     |     | switch(config-dhcp-server)#      |             | pool | primary-pool      |
|     |     |     | switch(config-dhcp-server-pool)# |             |      | range 192.168.1.1 |
|     |     |     | 192.168.1.100                    | prefix-len  | 16   |                   |
Examples
Definestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfortheDHCPv4server
poolprimary-poolonVRFprimary.
DHCP|109

| switch(config)# | dhcp-server |     | vrf primary |     |
| --------------- | ----------- | --- | ----------- | --- |
switch(config-dhcp-server)#
|     |     |     | pool primary-pool |     |
| --- | --- | --- | ----------------- | --- |
switch(config-dhcp-server-pool)# 192.168.1.1 192.168.1.100 prefix-len 24
Deletestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfromtheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |
| --------------------------- | ----------- | --- | ----------------- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |
switch(config-dhcp-server-pool)# no 192.168.1.1 192.168.1.100 prefix-len 24
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
config-dhcp-server-pool
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
show dhcp-server
| show dhcp-server | [all-vrfs] |             |                  |             |
| ---------------- | ---------- | ----------- | ---------------- | ----------- |
| show dhcp-server | leases     | {all-vrfs   | | vrf            | <VRF-NAME>} |
| show dhcp-server | pool       | <POOL-NAME> | [vrf <VRF-NAME>] |             |
Description
ShowsconfigurationsettingsfortheDHCPv4server.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
all-vrfs
ShowsDHCPv4serverconfigurationsettingsforallVRFs.
leases {all-vrfs | vrf <VRF-NAME>} ShowsDHCPv4serverleaseprovidedbytheserverforallVRFs
oraspecificVRF.
pool <POOL-NAME> [vrf <VRF-NAME>] ShowsDHCPv4serverpoolconfigurationsettingsforallVRFs
oraspecificVRF.
Examples
ShowingallDHCPv4serverconfigurationsettings.
| switch#     | show dhcp-server |               |     |     |
| ----------- | ---------------- | ------------- | --- | --- |
| VRF Name    |                  | : default     |     |     |
| DHCP Server |                  | : enabled     |     |     |
| Operational | State            | : operational |     |     |
110
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Authoritative  | Mode | : false    |     |     |     |     |
| -------------- | ---- | ---------- | --- | --- | --- | --- |
| Config_status  |      | : Applied  |     |     |     |     |
| Pool Name      |      | : test     |     |     |     |     |
| Lease Duration |      | : 00:01:00 |     |     |     |     |
| DHCP dynamic   | IP   | allocation |     |     |     |     |
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
| Config_status  |             | : Applied     |     |             |     |     |
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
| Option-Number |     | Option-Type |     | Option-Value |          |                   |
| ------------- | --- | ----------- | --- | ------------ | -------- | ----------------- |
| ------------- |     | ----------- |     | ------------ |          |                   |
| 6             |     | ip          |     | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 10.0.0.6 |
DHCP|111

| 18          |        | ascii         | aswed |     |     |
| ----------- | ------ | ------------- | ----- | --- | --- |
| DHCP Server | static | IP allocation |       |     |     |
--------------------------------
| IP-Address    | Client-Hostname |     | MAC-Address       |     |     |
| ------------- | --------------- | --- | ----------------- | --- | --- |
| ----------    | --------------- |     | ----------------- |     |     |
| 10.0.0.1      |                 | *   | aa:bb:cc:11:12:a4 |     |     |
| 20.0.0.1      |                 | *   | 11:22:11:22:aa:dd |     |     |
| BOOTP Options |                 |     |                   |     |     |
---------------
| Boot-File-Name      |         | TFTP-Server-Name |              | State       | TFTP-Server-Address   |
| ------------------- | ------- | ---------------- | ------------ | ----------- | --------------------- |
| --------------      |         | ---------------- |              | ------      | --------------------- |
| boot.txt            |         | *                |              | OPERATIONAL | 10.0.0.10             |
| Command History     |         |                  |              |             |                       |
| Release             |         |                  | Modification |             |                       |
| 10.07orearlier      |         |                  | --           |             |                       |
| Command Information |         |                  |              |             |                       |
| Platforms           | Command | context          | Authority    |             |                       |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
static-bind
static-bind {ip <IPV4-ADDR>}|{ mac <MAC-ADDR>} [hostname <HOST>]
| no static-bind | <IPV4-ADDR-LIST> |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaspecificMACaddress.
ThiscausestheDHCPv4servertoonlyassignthespecifiedIPaddresstoaclientstationwiththe
specifiedMACaddress.
Thenoformofthiscommandremovesthespecifiedbinding.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IPV4-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.TheIPaddressmustbewithinthe
addressrangedefinedforthecurrentpool.
mac <MAC-ADDR> SpecifiesaclientstationMACaddress(xx:xx:xx:xx:xx:xx),
wherexisahexadecimalnumberfrom0toF.
| hostname | <HOST> |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
Specifiesthehostnameoftheclientstation.Range:1to255
printableASCIIcharacters
Examples
112
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- |

Definesastaticaddressfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |
| --------------------------- | ----------- | --- | ----------------- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
Deletesastaticaddressfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)# | dhcp-server |     | vrf primary |     |
| --------------- | ----------- | --- | ----------- | --- |
switch(config-dhcp-server)#
|     |     |     | pool primary-pool |     |
| --- | --- | --- | ----------------- | --- |
switch(config-dhcp-server-pool)# no static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| DHCP server | IPv6 | commands |     |     |
| ----------- | ---- | -------- | --- | --- |
authoritative
authoritative
no authoritative
Description
ConfigurestheDHCPv6serverasauthoritativeonthecurrentVRF.Thismeansthattheserveristhesole
authorityforthenetworkontheVRF.Itrespondstoclientsolicitmessageswithadvertisemessages
havingapriority/preferencevaluesetto255(themaximum),insteadof0(theminimum).Clientsalways
choosetheDHCPv6serverwiththehighestpriority/preferencevalue.IftwoDHCPv6serverssendan
advertisemessagewiththesamepriority/preferencevalue,thentheclientpicksoneanddiscardsthe
other.
ThenoformofthiscommanddisablesauthoritativemodeonthecurrentVRF.
Example
ConfiguresDHCPv6serverauthoritativemodeonVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary   |     |
| ----------------------------- | ------------- | --- | ------------- | --- |
| switch(config-dhcpv6-server)# |               |     | authoritative |     |
RemovesDHCPv6serverauthoritativemodeonVRFprimary.
DHCP|113

| switch(config)# | dhcpv6-server |     | vrf | primary |
| --------------- | ------------- | --- | --- | ------- |
switch(config-dhcpv6-server)#
no authoritative
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| clear dhcpv6-server | leases |     |     |     |
| ------------------- | ------ | --- | --- | --- |
clear dhcpv6-server leases [all-vrfs | <IPV6-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv6serverleaseinformation.TheDHCPv6servermustbedisabledbeforeclearinglease
information.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
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
| vrf <VRF-NAME> |     |     |     | ClearsleasesforaspecificVRF. |
| -------------- | --- | --- | --- | ---------------------------- |
Examples
ClearingallDHCPv6serverleases.
| switch(config)#               | dhcpv6-server       |     | vrf     | primary |
| ----------------------------- | ------------------- | --- | ------- | ------- |
| switch(config-dhcpv6-server)# |                     |     | disable |         |
| switch(config-dhcpv6-server)# |                     |     | exit    |         |
| switch(config)#               | exit                |     |         |         |
| switch#                       | clear dhcpv6-server |     | leases  |         |
ClearingallDHCPv6serverleasesforVRFprimary-vrf.
114
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| switch(config)# |     | dhcpv6-server |     | vrf | primary |     |
| --------------- | --- | ------------- | --- | --- | ------- | --- |
switch(config-dhcpv6-server)#
disable
| switch(config-dhcpv6-server)# |       |               |     | exit   |                 |     |
| ----------------------------- | ----- | ------------- | --- | ------ | --------------- | --- |
| switch(config)#               |       | exit          |     |        |                 |     |
| switch#                       | clear | dhcpv6-server |     | leases | vrf primary-vrf |     |
CleartheDHCPv6serverleaseforIPaddress2001::1onVRFprimary-vrf.
| switch(config)#               |     | dhcpv6-server |     | vrf     | primary |     |
| ----------------------------- | --- | ------------- | --- | ------- | ------- | --- |
| switch(config-dhcpv6-server)# |     |               |     | disable |         |     |
| switch(config-dhcpv6-server)# |     |               |     | exit    |         |     |
| switch(config)#               |     | exit          |     |         |         |     |
switch#
|                | clear       | dhcpv6-server |         | leases | 2001::1      | vrf primary-vrf |
| -------------- | ----------- | ------------- | ------- | ------ | ------------ | --------------- |
| Command        | History     |               |         |        |              |                 |
| Release        |             |               |         |        | Modification |                 |
| 10.07orearlier |             |               |         |        | --           |                 |
| Command        | Information |               |         |        |              |                 |
| Platforms      |             | Command       | context |        | Authority    |                 |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| dhcpv6-server |     | external-storage |     |     |     |     |
| ------------- | --- | ---------------- | --- | --- | --- | --- |
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
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<VOLUME-NAME>
Specifiestheexternalstoragevolumename.Range:1to64
printableASCIIcharacters.
file <LEASE-FILENAME> Specifiestheexternalstoragefilename.Range:1to255printable
ASCIIcharacters.
DHCP|115

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
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
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-server    | vrf          |     |     |
| ---------------- | ------------ | --- | --- |
| dhcpv6-server    | vrf VRF-NAME |     |     |
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
| switch(config)# | dhcpv6-server | vrf | primary |
| --------------- | ------------- | --- | ------- |
RemovestheDHCPv6serversupportonVRFprimary.
116
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| switch(config)#     | no      | dhcpv6-server | vrf primary  |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
disable
disable
Description
DisablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhen
configuredonaVRF.
Example
DisablestheDHCPv6serveronVRFprimary.
switch(config)#
|                               | dhcpv6-server |         | vrf primary  |
| ----------------------------- | ------------- | ------- | ------------ |
| switch(config-dhcpv6-server)# |               |         | disable      |
| Command History               |               |         |              |
| Release                       |               |         | Modification |
| 10.07orearlier                |               |         | --           |
| Command Information           |               |         |              |
| Platforms                     | Command       | context | Authority    |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
dns-server
| dns-server <IPVv6-ADDR-LIST> |                   |     |     |
| ---------------------------- | ----------------- | --- | --- |
| no dns-server                | <IPVv6-ADDR-LIST> |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
DHCP|117

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IPVv6-ADDR-LIST> SpecifiestheIPaddressesoftheDNSserversinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDNSserver2001::13fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server |     | vrf primary       |     |          |
| ---------------------------------- | ------------- | --- | ----------------- | --- | -------- |
| switch(config-dhcpv6-server)#      |               |     | pool primary-pool |     |          |
| switch(config-dhcpv6-server-pool)# |               |     | dns-server        |     | 2001::13 |
DeletesDNSserver2001::13fromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server |         | vrf primary       |            |          |
| ---------------------------------- | ------------- | ------- | ----------------- | ---------- | -------- |
| switch(config-dhcpv6-server)#      |               |         | pool primary-pool |            |          |
| switch(config-dhcpv6-server-pool)# |               |         | no                | dns-server | 2001::13 |
| Command History                    |               |         |                   |            |          |
| Release                            |               |         | Modification      |            |          |
| 10.07orearlier                     |               |         | --                |            |          |
| Command Information                |               |         |                   |            |          |
| Platforms                          | Command       | context |                   | Authority  |          |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
enable
enable
Description
EnablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhen
configuredonaVRF.
Example
EnablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary |     |     |
| ----------------------------- | ------------- | --- | ----------- | --- | --- |
| switch(config-dhcpv6-server)# |               |     | enable      |     |     |
| Command History               |               |     |             |     |     |
118
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lease
| lease {<TIME> | | infinite} |     |     |
| ------------- | ----------- | --- | --- |
no lease
Description
SetsthelengthoftheDHCPv6leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv6clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv6leasetimetothedefaultvalue1hour.
| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| <TIME>    |     |     | SetstheDHCPv6leasetime.Format:DD:HH:MM.Default: |
01:00:00.
infinite
SetstheDHCPv6leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
Example
SetstheleasetimeforDHCPv6serverpoolprimary-poolonVRFprimaryto12hours.
| switch(config)#                    | dhcpv6-server | vrf  | primary        |
| ---------------------------------- | ------------- | ---- | -------------- |
| switch(config-dhcpv6-server)#      |               | pool | primary-pool   |
| switch(config-dhcpv6-server-pool)# |               |      | lease 00:12:00 |
SetstheleasetimeforDHCPserverpoolprimary-poolonVRFprimarytothedefaultvalue.
| switch(config)#                    | dhcpv6-server | vrf  | primary           |
| ---------------------------------- | ------------- | ---- | ----------------- |
| switch(config-dhcpv6-server)#      |               | pool | primary-pool      |
| switch(config-dhcpv6-server-pool)# |               |      | no lease 00:12:00 |
| Command History                    |               |      |                   |
| Release                            |               |      | Modification      |
| 10.07orearlier                     |               |      | --                |
| Command Information                |               |      |                   |
DHCP|119

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
Description
DefinescustomDHCPv6optionsforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovescustomDHCPv6optionsfromthepool.
| Parameter    |     |     | Description                                |     |
| ------------ | --- | --- | ------------------------------------------ | --- |
| <OPTION-NUM> |     |     | SpecifiesaDHCPv6optionnumber.Range:2to254. |     |
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
| switch(config)#                    | dhcpv6-server |     | vrf primary       |                  |
| ---------------------------------- | ------------- | --- | ----------------- | ---------------- |
| switch(config-dhcpv6-server)#      |               |     | pool primary-pool |                  |
| switch(config-dhcpv6-server-pool)# |               |     | option            | 22 ipv6 2001::12 |
DeletesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
switch(config)#
|                                    | dhcpv6-server |     | vrf primary       |                         |
| ---------------------------------- | ------------- | --- | ----------------- | ----------------------- |
| switch(config-dhcpv6-server)#      |               |     | pool primary-pool |                         |
| switch(config-dhcpv6-server-pool)# |               |     | no                | option 22 ipv6 2001::12 |
| Command History                    |               |     |                   |                         |
| Release                            |               |     | Modification      |                         |
| 10.07orearlier                     |               |     | --                |                         |
| Command Information                |               |     |                   |                         |
120
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
pool
pool <POOL-NAME>
| no pool <POOL-NAME> |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
Description
CreatesaDHCPv6serverpoolforthecurrentVRFandswitchestotheconfig-dhcpv6-server-pool
contextforit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64
pools(IPv4andIPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv6serverpool.
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
config-dhcpv6-server
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
range
| range <LOW-IPV6-ADDR>    |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
| ------------------------ | --- | ---------------- | --- | ----------- | ------- |
| no range <LOW-IPV6-ADDR> |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
DHCP|121

Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv6serverpool.Amaximumof64
rangesaresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
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
| switch(config)#               | dhcpv6-server |     | vrf primary       |     |     |
| ----------------------------- | ------------- | --- | ----------------- | --- | --- |
| switch(config-dhcpv6-server)# |               |     | pool primary-pool |     |     |
switch(config-dhcpv6-server-pool)#
|     |     |     | range | 2001::1 2001::10 prefix-len | 64  |
| --- | --- | --- | ----- | --------------------------- | --- |
DeletesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary       |     |     |
| ----------------------------- | ------------- | --- | ----------------- | --- | --- |
| switch(config-dhcpv6-server)# |               |     | pool primary-pool |     |     |
switch(config-dhcpv6-server-pool)# no range 2001::1 2001::10 prefix-len 64
| Command History     |         |         |              |           |     |
| ------------------- | ------- | ------- | ------------ | --------- | --- |
| Release             |         |         | Modification |           |     |
| 10.07orearlier      |         |         | --           |           |     |
| Command Information |         |         |              |           |     |
| Platforms           | Command | context |              | Authority |     |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
show dhcpv6-server
| show dhcpv6-server | [all-vrfs] |             |                  |             |     |
| ------------------ | ---------- | ----------- | ---------------- | ----------- | --- |
| show dhcpv6-server | leases     | {all-vrfs   | | vrf            | <VRF-NAME>} |     |
| show dhcpv6-server | pool       | <POOL-NAME> | [vrf <VRF-NAME>] |             |     |
Description
ShowsconfigurationsettingsfortheDHCPv6server.
122
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| Parameter |     |     |     | Description                                       |
| --------- | --- | --- | --- | ------------------------------------------------- |
| all-vrfs  |     |     |     | ShowsDHCPv6serverconfigurationsettingsforallVRFs. |
leases {all-vrfs | vrf <VRF-NAME>} ShowsDHCPv6serverleaseprovidedbytheserverforallVRFs
oraspecificVRF.
| pool <POOL-NAME> | [vrf | <VRF-NAME>] |     |     |
| ---------------- | ---- | ----------- | --- | --- |
ShowsDHCPv6serverpoolconfigurationsettingsforallVRFs
oraspecificVRF.
Examples
ShowingallDHCPv6serverconfigurationsettings.
| switch# show   | dhcpv6-server |               |     |     |
| -------------- | ------------- | ------------- | --- | --- |
| VRF Name       |               | : default     |     |     |
| DHCPv6 Server  |               | : enabled     |     |     |
| Operational    | State         | : operational |     |     |
| Authoritative  | Mode          | : true        |     |     |
| Config_status  |               | : Applied     |     |     |
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
| DHCPv6 Server | static | IP          | allocation   |     |
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
| Config_status  |               | : Applied     |                 |     |
| Pool Name      |               | : test        |                 |     |
| Lease Duration |               | : 00:01:00    |                 |     |
| DHCPV6 dynamic | IP            | allocation    |                 |     |
-----------------------------
| Start-IPv6-Address |     | End-IPv6-Address |     | Prefix-Length |
| ------------------ | --- | ---------------- | --- | ------------- |
| ------------------ |     | ---------------- |     | ------------- |
| 2000::1            |     | 2000::20         |     | *             |
DHCP|123

| 2001::20      |     |         | 2001::50 |     | *   |     |
| ------------- | --- | ------- | -------- | --- | --- | --- |
| 2001::2       |     |         | 2001::10 |     | 64  |     |
| 2010::20      |     |         | 2010::40 |     | *   |     |
| DHCPv6 Server |     | options |          |     |     |     |
---------------------
| Option-Number |     | Option-Type |               | Option-Value |     |     |
| ------------- | --- | ----------- | ------------- | ------------ | --- | --- |
| ------------- |     | ----------- |               | ------------ |     |     |
| 7             |     | ipv6        |               | 2001::15     |     |     |
| 23            |     | ipv6        |               | 2001::30     |     |     |
| 30            |     | ipv6        |               | 2001::10     |     |     |
| DHCPv6 Server |     | static      | IP allocation |              |     |     |
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
| IPv6-Address        |         | Client-Hostname |         |              | State       | Client-Id          |
| ------------------- | ------- | --------------- | ------- | ------------ | ----------- | ------------------ |
| ------------        |         | --------------- |         |              | ----------- | ---------          |
| 2100::4             |         | *               |         |              | OPERATIONAL | 1:0:a0:24:ab:fb:9c |
| Command History     |         |                 |         |              |             |                    |
| Release             |         |                 |         | Modification |             |                    |
| 10.07orearlier      |         |                 |         | --           |             |                    |
| Command Information |         |                 |         |              |             |                    |
| Platforms           | Command |                 | context | Authority    |             |                    |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
124
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

static-bind
| static-bind    | ipv6 | <IPVv6-ADDR>      |     | client-id | <ID> [hostname | <HOST>] |
| -------------- | ---- | ----------------- | --- | --------- | -------------- | ------- |
| no static-bind | ipv6 | <IPVv6-ADDR-LIST> |     |           |                |         |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaclientidentifierorDUID.
ThiscausestheDHCPv6servertoonlyassignthespecifiedIPaddresstoaclientstationwiththe
specifiedclientidentifierorDUID.
Thenoformofthiscommandremovesthespecifiedstaticbindingfromthepool.
| Parameter   |     |     |     |     | Description                               |     |
| ----------- | --- | --- | --- | --- | ----------------------------------------- | --- |
| <IPV6-ADDR> |     |     |     |     | SpecifiestheIPaddresstoassigninIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Forexample,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| client-id | <ID> |     |     |     | SpecifiestheclientidentifierorDUID. |     |
| --------- | ---- | --- | --- | --- | ----------------------------------- | --- |
hostname <HOST> Specifiesthehostnameoftheclientstation.Range:1to255
printableASCIIcharacters
Example
DefinesastaticaddressfortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server |     | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | --- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               |     | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)# static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c
DeletesastaticaddressfromtheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server |     | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | --- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               |     | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)# no static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c
| Command        | History     |     |         |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
DHCP|125

Troubleshooting
| Client | not | getting | IP address |     |     |     |     |
| ------ | --- | ------- | ---------- | --- | --- | --- | --- |
CoPPdrop
n
IncaseofexcessiveDHCPtraffic,CoPPdoestheratelimitbydroppingsomeofthepackets.
CheckifclientpacketsaregettingdroppedbyCoPPusingshow copp statistics class dhcp-ipv4or
| show copp | statistics |     | class | dhcp-ipv6commands. |     |     |     |
| --------- | ---------- | --- | ----- | ------------------ | --- | --- | --- |
n Configurationissues
1. IPrangewithinthepoolshouldmatchtheclientconnectedinterfaceIPsubnet.
|     |     | dhcp-server |       | vrf default |              |     |     |
| --- | --- | ----------- | ----- | ----------- | ------------ | --- | --- |
|     |     | pool        | pool1 |             |              |     |     |
|     |     |             | range | 172.16.10.1 | 172.16.10.20 |     |     |
exit
enable
Ch2e.ckthescalenumberssupportedontheplatform.ForexamplethemaximumnumberofVRFs,
andpoolssupportedontheplatform.
3. CheckiftheDHCPServerisconfiguredinclientVRFandisinenabledstate.
|     | 4. Checkforserverpoolexhaustion. |     |     |     |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
n DHCPRelayco-existence
FromAOS-CX10.07onwards,youcanconfigureDHCPRelayandDHCPServersimultaneously.Ifbothare
enabledforanearlierrelease,theneithertheDHCPrelayortheDHCPserverwillfailtostart.
| DHCP | Server | daemon |     | taking | up high CPU | [dhcp-server-adapter] |     |
| ---- | ------ | ------ | --- | ------ | ----------- | --------------------- | --- |
n Duetoarchitecturallimitations,theDHCPServeronbootuptheCPUutilizationishighforabout2
minutes;thisisexpectedbehavior.
n IntheVSXsetup,whenthenumberofclientsintheleasetableismore,theserverdaemonwillhave
highCPUusagewhilesyncingleasesbetweenprimaryandsecondaryVSXpeers.Oncesyncingis
complete,thentheCPUutilizationcomesbacktonormal.
| Check | point | restore |     |     |     |     |     |
| ----- | ----- | ------- | --- | --- | --- | --- | --- |
DHCP-Serverconfigurationchangesarenotallowedwhenitisenabled.However,throughcheck-point
restoreorTFTPconfigurationdownloadorREST,youcanchangetheconfigurationinthemanagement
VRF.Thisconfigurationchangegetsappliedwhentheserverisdisabledandenabled.
From10.10onwards,aconfigurationflagiconisdisplayedinshow dhcp-servercommandtoindicateif
thereisanyconfigurationthatisnotapplied.
FAQ
| 1. What | ports | use | DHCP | for switch | assignments? |     |     |
| ------- | ----- | --- | ---- | ---------- | ------------ | --- | --- |
YoucansetupaDHCPswitchwithamanagementVRFport;ifthemanagementVRFportisunavailable,
useanIN-Banddataport.
| 2. Is DHCP |     | assignment |     | available | on boot | up from the | factory? |
| ---------- | --- | ---------- | --- | --------- | ------- | ----------- | -------- |
126
| AOS-CX10.11IPServicesGuide| |     |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- | --- |

Yes, DHCP assignment is available on boot up from the factory. This assists Zero Touch depending on
the platform; this can be a management VRF or an IN-Band data port on the default VLAN 1.

3. Is DHCP assignment available on both management VRF and IN-Band data ports
simultaneously?

Yes, DHCP assignment is possible on both management VRF and IN Band data ports, but it depends on
the platform.

If both ports can get a DHCP address, the DHCP address from the management VRF port is used for
Zero Touch Provisioning instead of the one from the IN-Band data port. The data ports will wait 30
seconds before taking ownership of Zero Touch Provisioning (ZTP).

4. Which VLAN is assigned a DHCP address?

The factory default VLAN to which the DHCP address is assigned is VLAN1.

Users can configure the VLAN for DHCP allocation on platforms supporting multiple VLAN
configurations. Only a single VLAN can support DHCP assignments.

5. Can DHCP assignments be disabled in an Aruba AOS-CX switch?

Use the no ip dhcp command on the required VLAN interface or management VRF port you can disable
the DHCP assignments in an Aruba AOS-CX switch.

A static configuration option is available on both ports.

6. Can IP DHCP switch assignment be carried out on a Routed only Port (RoP)?

No, RoP is not supported. Only VLAN and OOBM ports can be allocated an address with DHCP.

7. Can an Aruba AOS-CX switch support DHCP IPv6 Allocation?

Yes, an Aruba AOS-CX switch can support DHCP IPv6 allocation. However, for Zero Touch Provisioning
(ZTP), IPv4 is required.

8. Do Aruba AOS-CX switches support DHCP server?

Since the software release of AOS-CX 10.10, all platforms support DHCP server, except for 6100, 6000,
and 4100i.

9. Can Aruba AOS-CX switches support DHCP address exclusion from a subnet?

Not formally; however, you can use static bindings to unused MAC addresses as a workaround on a
smaller scale.

10. Do all Aruba AOS-CX switches support DHCP helper?

Since the software release of AOS-CX 10.10, all platforms support DHCP helper for IPv4 and IPv6.

11. Can DHCP Server and Relay simultaneously be supported on a switch?

Yes, since the software release AOS-CX 10.08, the platforms that support DHCP Server and Relay both
can be set up simultaneously.

12. How many helper addresses can be used?

The Switched Virtual Interface can use up to eight helper addresses for IPv4 and IPv6.

13. Is DHCP Relay supported for multi-netted addresses?

Yes, for both IPv4 and IPv6 DHCP Relay supports multi-netted addresses. The Gateway IP Address
(GIADDR) used in the DHCP request will be the lowest IP address configured on the interface.

DHCP | 127

You can override the lowest IP address using the bootp-gateway command. IPV6 does not support
bootp.

14. Can a multi-netted address support GIADDR from a different address?

Yes, for IPv4 only. For more information, see DHCP relay agent.

15. Can the binding of DHCP and IP remain after a switch reboot?

Yes, the binding of DHCP and IP remains by using an external storage option dhcpv4-snooping
external-storage.

16. If multiple ‘ip-helper’ IPs configured for DHCP relay on an interface or SVI, which
switch will forward the DHCP requests?

In case of multiple ‘ip-helper’ IPs configured for DHCP relay on an interface or SVI, the client will receive
multiple offers from different DHCP servers, and the client will choose which one to accept.

17. What happens when global dhcp-smart-relay is enabled in an interface or SVI with
multiple IP addresses (multi-netting) that services DHCP clients in different subnets?

On enabling global dhcp-smart-relay in an interface or SVI with multiple IP addresses (multi-netting)
that services DHCP clients in different subnets, the AOS-CX device will first use the primary interface or
SVI IP address as the unicast source to the DHCP server. If no response is received the AOS-CXdevice will
use the secondary IPs from the lowest-numbered IP to the highest until a DHCP response is received.

18. What are the troubleshooting for DHCP relay agent?

The initial troubleshooting for DHCP relay agent can be done using the following commands:

nshow dhcp-relay

nshow dhcp-relay bootp-gateway

nshow ip helper-address

Next level of troubleshooting can be done by taking packets captured at the DHCP server side and AOS-
CX side. For more information about AOS-CX packet capture, see Mirroring chapter of AOS-CX Monitoring
Guide.

Perform additional AOS-CX side DHCP debugging using debug dhcprelay and debug dhcpv6relay
commands. For more information, see Debug logging chapter of AOS-CX Diagnostics and Supportability
Guide.

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

128

Chapter 6

DHCP snooping

DHCP snooping

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

DHCPv6 guard

The DHCPv6 guard feature is an extension of DHCPv6 snooping. When the DHCPv6 snooping feature is
configured globally and on the VLAN, the ports are configured as trusted and untrusted ports on the
VLAN. DHCPv6 guard enhances this feature by creating a policy and applying it on a port and VLAN. This
policy contains multiple attributes which are compared against the packet that is received on trusted
ports. If the packet complies with the attributes of the policy, it is forwarded to the destination port;
otherwise the packet is dropped.

DHCP server interoperation

DHCP server can not be configured with DHCP snooping.

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

129

| DHCPv4 snooping | conditions | for dropping | DHCPv4 | packets |     |
| --------------- | ---------- | ------------ | ------ | ------- | --- |
AppliesonlytoDHCPv4snooping.
| Packet types | that are |            |              |             |     |
| ------------ | -------- | ---------- | ------------ | ----------- | --- |
|              |          | Conditions | for dropping | the packets |     |
dropped
DHCPOFFER,DHCPACK, n ApacketfromaDHCPserverisreceivedonanuntrustedport.
DHCPNACK
n TheswitchisconfiguredwithalistofauthorizedDHCPserveraddresses
andaDHCPresponsereceivedonatrustedport,butthesourceIP
addressisnotanauthorizedDHCPserver.
DHCPRELEASE,DHCPDECLINE n AbroadcastpacketthathasaMACaddressintheDHCPbindingdatabase,
buttheportintheDHCPbindingdatabasedoesnotmatchtheporton
whichthepacketisreceived.
AllDHCPpackettypes
n ADHCPpacketreceivedonanuntrustedportinwhichtheDHCPclient
hardwareMACaddressdoesnotmatchthesourceMACaddressinthe
packet.
n ADHCPpacketcontainingDHCPrelayinformation(option82)isreceived
onanuntrustedport.
| Protocol | details |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
1. Whenaportisconfiguredasatrustedport,allthedynamicIPbindingentrieslearnedonthat
portwillbedeleted.
2. Whenaclientisconnectedonatrustedport,thedynamicIPbindingentrieswillnotbelearned
ontheswitch,eventhoughtheclientgetsanIPaddress.
3. IfDHCPv4snoopingisenabledontwoback-to-backaccessswitches,DHCPpacketswillbe
dropped,Sincebydefaultoption82isenabledonDHCPv4snoopingandthedefaultpolicyis
drop.ThesecondswitchwithDHCPv4snoopingenableddropsthepackets.Inthisscenariothe
usershouldenableDHCPv4snoopingoption82ononeswitch,orelseyoucandisableonboth.
| Supported | platform | and | standards |     |     |
| --------- | -------- | --- | --------- | --- | --- |
ThefollowingtablelistthesupportedplatformsforDHCPsnooping.
Table1:Supportplatformsfor DHCPsnooping
| Platform |     |     | DHCP | snooping |     |
| -------- | --- | --- | ---- | -------- | --- |
| 6200     |     |     | Yes  |          |     |
Table2:Scale
| Platform | IP Bindings | per | port | IP Bindings | per device |
| -------- | ----------- | --- | ---- | ----------- | ---------- |
6200
|     | 1024 |     |     | 5120 |     |
| --- | ---- | --- | --- | ---- | --- |
Use case
DHCPsnooping|130

| DHCPv4 Snooping | uses case |     |     |     |
| --------------- | --------- | --- | --- | --- |
DHCPSnoopingisusedtoprotectfromrougeorunwantedattacksfromposingDHCPservices.
Inthefollowingusecase:
n SettheswitchforDHCPv4snooping.
AllowDHCPcommunicationfromtheuplinksintheEnterprisenetworkport1/1/51and1/1/52.
n
n ForCommunicationtooccur,identifyauthorizedDHCPservers10.19.69.15and10.19.71.15.
n LANfacinguserports1/1/1to1/1/15isnotconfiguredastrusted.
KeyconfigurationportionforabovesetupisshownwiththerelevantDHCPv4Snoopingparameters.
| dhcpv4-snooping |     |     | <--enable | DHCPv4 snooping |
| --------------- | --- | --- | --------- | --------------- |
dhcpv4-snooping authorized-server 10.19.69.15 <--allow authorized servers
| dhcpv4-snooping | authorized-server | 10.19.71.15 |     |     |
| --------------- | ----------------- | ----------- | --- | --- |
vlan 110
| description     | uplink |     |           |                 |
| --------------- | ------ | --- | --------- | --------------- |
| dhcpv4-snooping |        |     | <--enable | DHCPv4 snooping |
131
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

| on required | VLANs |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- |
vlan 111
| description |     | uplink |     |     |     |     |     |
| ----------- | --- | ------ | --- | --- | --- | --- | --- |
dhcpv4-snooping
vlan 120
| description |     | User |     |     |     |     |     |
| ----------- | --- | ---- | --- | --- | --- | --- | --- |
dhcpv4-snooping
| interface | 1/1/1 |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- |
no shutdown
| description |        | User |     |     |     |     |     |
| ----------- | ------ | ---- | --- | --- | --- | --- | --- |
| vlan        | access | 120  |     |     |     |     |     |
...
| interface | 1/1/15 |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- |
no shutdown
| description |        | User |     |     |             |           |                |
| ----------- | ------ | ---- | --- | --- | ----------- | --------- | -------------- |
| vlan        | access | 120  |     |     |             |           |                |
| interface   | 1/1/51 |      |     |     | <--Unplinks | on 1/1/51 | and 52 trusted |
no shutdown
| vlan            | trunk          | native 1        |     |     |     |     |     |
| --------------- | -------------- | --------------- | --- | --- | --- | --- | --- |
| vlan            | trunk          | allowed         | 110 |     |     |     |     |
| dhcpv4-snooping |                | trust           |     |     |     |     |     |
| interface       | 1/1/52         |                 |     |     |     |     |     |
| vlan            | trunk          | native 1        |     |     |     |     |     |
| vlan            | trunk          | allowed         | 111 |     |     |     |     |
| dhcpv4-snooping |                | trust           |     |     |     |     |     |
| interface       | vlan           | 110             |     |     |     |     |     |
| description     |                | uplink          |     |     |     |     |     |
| ip              | address        | 172.16.69.1/30  |     |     |     |     |     |
| interface       | vlan           | 111             |     |     |     |     |     |
| description     |                | uplink          |     |     |     |     |     |
| ip              | address        | 172.16.71.1/30  |     |     |     |     |     |
| interface       | vlan           | 120             |     |     |     |     |     |
| description     |                | User            |     |     |     |     |     |
| ip              | address        | 172.16.10.1/254 |     |     |     |     |     |
| ip              | helper-address | 10.19.69.15     |     |     |     |     |     |
| ip              | helper-address | 10.19.71.15     |     |     |     |     |     |
...
| ip route | 0.0.0.0/0 | 172.16.69.2 | distance | 10  |     |     |     |
| -------- | --------- | ----------- | -------- | --- | --- | --- | --- |
| ip route | 0.0.0.0/0 | 172.16.71.2 | distance | 20  |     |     |     |
...
Usingtheshowdhcpv4-snoopingcommand,youcanseesomeofthefollowingDHCPv4information:
n AppliedVLANsforsnooping,110-112and120
Theuntrustedpolicyissettodroppackets
n
n ThelistofauthorizedDHCPserversaresetto10.19.69.15and10,19.71.15
n SetthetrustedoruntrustedportsandanyDHCPbindingsforthoseports.Port1/1/1and1/1/2offer
DHCP.
show dhcpv4-snooping
| DHCPv4-Snooping |            | Information |       |            |         |               |     |
| --------------- | ---------- | ----------- | ----- | ---------- | ------- | ------------- | --- |
| DHCPv4-Snooping |            |             | : Yes | Verify MAC | Address | : Yes         |     |
| Allow           | Overwrite  | Binding     | : No  | Enabled    | VLANs   | : 110-111,120 |     |
| IP Binding      | Disabled   | VLANs       | :     |            |         |               |     |
| Static          | Attributes | : No        |       |            |         |               |     |
DHCPsnooping|132

| Client       | Event Logs          | : No           |          |           |                    |         |
| ------------ | ------------------- | -------------- | -------- | --------- | ------------------ | ------- |
| Option       | 82 Configurations   |                |          |           |                    |         |
| Untrusted    | Policy              | : drop         |          | Insertion |                    | : Yes   |
| Option       | 82 Remote-id        | : mac          |          |           |                    |         |
| External     | Storage             | Information    |          |           |                    |         |
| Volume       | Name                | : --           |          |           |                    |         |
| File         | Name                | : --           |          |           |                    |         |
| Inactive     | Since               | : --           |          |           |                    |         |
| Error        |                     | : --           |          |           |                    |         |
| Flash        | Storage Information |                |          |           |                    |         |
| File         | Write Delay         | : --           |          |           |                    |         |
| Active       | Storage             | : --           |          |           |                    |         |
| Authorized   | Server              | Configurations |          |           |                    |         |
| VRF          |                     |                |          |           | Authorized         | Servers |
| ------------ |                     |                |          |           | ------------------ |         |
| default      |                     |                |          |           | 10.19.69.15        |         |
| default      |                     |                |          |           | 10.19.71.15        |         |
| Port         | Information         |                |          |           |                    |         |
|              |                     | Max            | Static   | Dynamic   |                    |         |
| Port         | Trust               | Bindings       | Bindings | Bindings  |                    |         |
| --------     | -----               | --------       | -------- | --------  |                    |         |
| 1/1/51       | Yes                 | 0              | 0        | 0         |                    |         |
| 1/1/52       | Yes                 | 0              | 0        | 0         |                    |         |
| 1/1/1        | No                  | 1024           | 0        | 1         |                    |         |
| 1/1/2        | No                  | 1024           | 0        | 1         |                    |         |
!
| !output | omitted |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
!
| 1/1/14                | No       | 1024     | 0       | 0   |     |     |
| --------------------- | -------- | -------- | ------- | --- | --- | --- |
| 1/1/15                | No       | 1024     | 0       | 0   |     |     |
| DHCPv4                | snooping | commands |         |     |     |     |
| clear dhcpv4-snooping |          |          | binding |     |     |     |
clear dhcpv4-snooping binding {all | ip <IPV4-ADDR> vlan <VLAN-ID> | port <PORT-NUM> |
vlan <VLAN-ID>}
Description
ClearsDHCPv4snoopingbindingentries.
| Parameter |     |     | Description                                            |     |     |     |
| --------- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
| all       |     |     | SpecifiesthatallDHCPv4bindinginformationistobecleared. |     |     |     |
133
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
ip <IPV4-ADDR> vlan <VLAN-ID> SpecifiestheIPv4addressandVLANforwhichallDHCPv4binding
informationistobecleared.
port <PORT-NUM> SpecifiestheportnumberforwhichallDHCPv4binding
informationistobecleared.
vlan <VLAN-ID>
SpecifiestheVLANforwhichallDHCPv4bindinginformationisto
becleared.
Examples
ClearingallDHCPv4bindinginformationforIPaddress192.168.2.4andVLAN5:
switch(config)# clear dhcpv4-snooping binding ip 192.168.2.4 vlan 5
ClearingallDHCPv4bindinginformationforport1/1/1:
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
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| clear dhcpv4-snooping |     | statistics |     |     |
| --------------------- | --- | ---------- | --- | --- |
| clear dhcpv4-snooping |     | statistics |     |     |
Description
DHCPsnooping|134

ClearsallDHCPv4snoopingstatistics.
Examples
ClearallDHCPv4snoopingstatistics:
| switch#         | clear dhcpv4-snooping | statistics |                                                 |
| --------------- | --------------------- | ---------- | ----------------------------------------------- |
| Command History |                       |            |                                                 |
| Release         |                       |            | Modification                                    |
| 10.09.1000      |                       |            | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |                       |            | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
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
| switch(config)# | dhcpv4-snooping |     |     |
| --------------- | --------------- | --- | --- |
DisablingDHCPv4snooping:
| switch(config)# | no  | dhcpv4-snooping |     |
| --------------- | --- | --------------- | --- |
| Command History |     |                 |     |
135
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Release    |     |     | Modification                                    |
| ---------- | --- | --- | ----------------------------------------------- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping |     | (in config-vlan | context) |
| --------------- | --- | --------------- | -------- |
dhcpv4-snooping
no dhcpv4-snooping
Description
EnablesDHCPv4snoopingforthespecifiedVLANintheconfig-vlancontext.DHCPv4snoopingis
disabledbydefaultforallVLANs.
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
| Command Information |     |     |     |
| ------------------- | --- | --- | --- |
DHCPsnooping|136

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |                         | allow-overwrite-binding |     |     |
| ------------------ | ----------------------- | ----------------------- | --- | --- |
| dhcpv4-snooping    | allow-overwrite-binding |                         |     |     |
| no dhcpv4-snooping | allow-overwrite-binding |                         |     |     |
Description
AllowsbindingtobeoverwrittenforthesameIPaddress.Whenenabled,andaDHCPserveroffersa
hostanIPaddressthatisalreadyboundtoanexistinghostinthebindingtable,theexistingbindingis
overwrittenforthenewhostifthenewhostissuccessfullyabletoacquirethesameIPaddress.This
overwritingisdisabledbydefault,causingtheDHCPserverofferstobedropped.
ThenoformofthecommanddisablesDHCPv4snoopingoverwritebinding.
Examples
EnablingDHCPv4snoopingoverwritebinding:
| switch(config)# | dhcpv4-snooping |     | allow-overwrite-binding |     |
| --------------- | --------------- | --- | ----------------------- | --- |
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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping |                   | authorized-server |             |                  |
| --------------- | ----------------- | ----------------- | ----------- | ---------------- |
| dhcpv4-snooping | authorized-server |                   | <IPV4-ADDR> | [vrf <VRF-NAME>] |
no dhcpv4-snooping authorized-server <IPV4-ADDR> [vrf <VRF-NAME>]
Description
Addsanauthorized(trusted)DHCPservertoalistofauthorizedserversforusebyDHCPv4snooping.
Thiscommandcanbeissuedmultipletimes,addingamaximumof20authorizedserversperVRF.By
137
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

default,withanemptylistofauthorizedservers,allDHCPserversareconsideredtobetrustedfor
DHCPv4snoopingpurposes.
ThemgmtVRFcannotbeusedwiththiscommand.
ThenoformofthiscommanddeletesthespecifiedDHCPserverfromtheauthorizedlist.
| Parameter   |     |     | Description                                      |     |
| ----------- | --- | --- | ------------------------------------------------ | --- |
| <IPV4-ADDR> |     |     | SpecifiestheIPv4addressofthetrustedDHCPv4server. |     |
vrf <VRF-NAME>
SpecifiestheVRFname.Thenamemustbedefault.
Usage
Forauthorizedserverlookup,theVRFisderivedfromtheSwitchVirtualInterface(SVI)configuredfor
theincomingVLAN.IftheSVIisnotconfigured,thedefaultVRFisassumed.
Examples
AddingDHCPservers192.168.2.2,192.168.2.3,and192.168.2.10totheauthorizedserverlist:
| switch(config)# |     | dhcpv4-snooping | authorized-server | 192.168.2.2 |
| --------------- | --- | --------------- | ----------------- | ----------- |
switch(config)# dhcpv4-snooping authorized-server 192.168.2.3 vrf default
switch(config)# dhcpv4-snooping authorized-server 192.168.2.10 vrf default
RemovingDHCPserver192.168.2.3fromtheauthorizedserverlist:
switch(config)# no dhcpv4-snooping authorized-server 192.168.2.3 vrf default
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |           | event-log        | client |     |
| ------------------ | --------- | ---------------- | ------ | --- |
| dhcpv4-snooping    | event-log | client           |        |     |
| no dhcpv4-snooping |           | event-log client |        |     |
Description
ThiscommandenablesordisablesDHCPv4-snoopingclientleveleventlogsthathelpwithclient
telemetryonaremotemanagementstationsuchasArubaCentral.Bydefault,clientleveleventlogsare
disabled.Thenoformofthiscommanddisablesclient-leveleventlogsforDHCPv4snoopingafterthey
DHCPsnooping|138

areenabled.ViewtheseloggedDHCPv4snoopingeventsbyissuingthecommandshow events -c
dhcpv4-snooping.
Examples
EnablingDHCPv4clientleveleventlogs:
| switch(config)# | #   | dhcpv4-snooping | event-log | client |
| --------------- | --- | --------------- | --------- | ------ |
Disablingexternalstorage:
| witch(config)#      | # no    | dhcpv4-snooping | event-log          | client |
| ------------------- | ------- | --------------- | ------------------ | ------ |
| Command History     |         |                 |                    |        |
| Release             |         |                 | Modification       |        |
| 10.10               |         |                 | Commandintroduced. |        |
| Command Information |         |                 |                    |        |
| Platforms           | Command | context         | Authority          |        |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping |     | external-storage |     |     |
| --------------- | --- | ---------------- | --- | --- |
dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
no dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
Description
ConfiguresexternalstoragetobeusedforbackingupIPbindings(usedbyDHCPv4snooping)toafile.
Whenconfigured,theswitchstoresalltheIPbindingsinanexternalstoragefilesothattheyare
retainedaftertheswitchrestarts.Whentheswitchrestarts,itreadstheIPbindingsfromtheconfigured
externalstoragefiletopopulateitslocalcache.
WhenbothexternalstorageandflashstorageareconfiguredtostoreDHCPsnoopingIPbindings,theexternal
storagetakespriority,andisusedexclusivelyuntilitbecomesunconfigured,atwhichtimeflashstorage(if
configured)isused.Later,ifexternalstorageisconfiguredagain,flashstoragestopsandexternalstorage
resumes.
ThenoformofthiscommanddisablesthesavingofIPbindingsinanexternalstoragefile.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
volume <VOL-NAME> Specifiesthenameoftheexistingexternalstoragevolumewhere
theIPbindingsfilewillbesaved.Beforerunningthedhcpv4-
|     |     |     | snooping | external-storage volumecommand,firstcreate |
| --- | --- | --- | -------- | ------------------------------------------ |
theexternalstoragevolumeusingcommandexternal-storage
139
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VOLUME-NAME>.SeeExternalstoragecommandsinthe
Command-LineInterfaceGuide.
file <FILE-NAME> SpecifiesthefilenametouseforstoringIPbindings.Maximum
255characters.
ConfiguringIPbindingsstorageinfiledsnoop_ipbindingsonexistingvolumedhcp_snoop:
switch(config)# dhcpv4-snooping external-storage volume dhcp_snoop file dsnoop_
ipbindings
Disablingexternalstorage:
switch(config)# no dhcpv4-snooping external-storage volume dhcp_snoop
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
config
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |               | flash-storage |                 |
| ------------------ | ------------- | ------------- | --------------- |
| dhcpv4-snooping    | flash-storage |               | [delay <DELAY>] |
| no dhcpv4-snooping | flash-storage |               | [delay <DELAY>] |
Description
ConfiguresswitchflashstoragetobeusedforbackingupclientIPbindings(usedbyDHCPv4snooping).
Whenflashstorageisconfigured(andexternalstorageisnotalreadyconfiguredforthispurpose),the
DHCPsnooping|140

switchstorestheIPbindingsinswitchflashstorage.Whentheswitchrestarts,itreadstheIPbindings
fromtheswitchflashstoragetopopulateitslocalcache.
WritingtheIPbindingstoflashstorageonlyoccursaftertheconfigureddelayandiftherehasbeena
changeinclientIPbindings.WritingisskippedwhenclientIPbindingshavenotchangedsincethe
previouswrite.
| Omittingdelay | <DELAY> setsthedefaultdelayof900seconds. |     |     |     |
| ------------- | ---------------------------------------- | --- | --- | --- |
Toreduceswitchflashagingitisrecommendedthatyouuseexternalstorage(commanddhcpv4-snooping
external-storage)tobackupDHCPsnoopingIPbindings.Alternatively,considerconfiguringflashstoragewith
asubstantialdelaybetweenwrites.
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
ConfiguringswitchflashstorageforDHCPsnoopingIPbindingstoragewithawritedelayof1200
seconds:
| switch(config)# | dhcpv4-snooping |     | flash-storage | delay 1200 |
| --------------- | --------------- | --- | ------------- | ---------- |
Warning: Using flash storage reduces switch lifetime. It is recommended to use an
external-storage.
| Do you want | to continue | (y/n)? | y   |     |
| ----------- | ----------- | ------ | --- | --- |
switch(config)#
UnconfiguringusageofswitchflashstorageforIPbindings:
| switch(config)#     | no dhcpv4-snooping |     | flash-storage                                   |     |
| ------------------- | ------------------ | --- | ----------------------------------------------- | --- |
| Command History     |                    |     |                                                 |     |
| Release             |                    |     | Modification                                    |     |
| 10.09.1000          |                    |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09               |                    |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
| Command Information |                    |     |                                                 |     |
141
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |              | max-bindings |                |     |     |
| ------------------ | ------------ | ------------ | -------------- | --- | --- |
| dhcpv4-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |
| no dhcpv4-snooping |              | max-bindings | <MAX-BINDINGS> |     |     |
Description
SetsthemaximumnumberofDHCPbindingsallowedontheselectedinterface.Forallinterfaceson
whichthiscommandisnotrun,thedefaultmaxbindingisthemaximumvalueoftherange.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofDHCPbindings.Range1to
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
| Command History     |         |         |     |                                                 |     |
| ------------------- | ------- | ------- | --- | ----------------------------------------------- | --- |
| Release             |         |         |     | Modification                                    |     |
| 10.09.1000          |         |         |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09               |         |         |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
| Command Information |         |         |     |                                                 |     |
| Platforms           | Command | context |     | Authority                                       |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping |     | option | 82  |     |     |
| --------------- | --- | ------ | --- | --- | --- |
DHCPsnooping|142

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
Whenremote-idisomitted,itsdefault(mac)isused.Whenuntrusted-policyisomitted,itsdefault
(drop)isused.
ThenoformofthiscommanddisablesDHCPv4snoopingoption82.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
remote-id SpecifieswhataddresstouseastheremoteIDforthereplace
optionofuntrusted-policy.Specifyoneoftheseaddress
types:
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
switch(config)#
|     | dhcpv4-snooping |     | option | 82 untrusted-policy | keep |
| --- | --------------- | --- | ------ | ------------------- | ---- |
ConfiguringDHCPv4snoopingoption82withmgmt-ipastheremote-idandthereplaceaction:
switch(config)# dhcpv4-snooping option 82 remote-id mgmt-ip untrusted-policy
replace
DisablingDHCPv4snoopingoption82:
switch(config)# no dhcpv4-snooping option 82 untrusted-policy keep
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
143
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| Release    |     |     | Modification                                    |
| ---------- | --- | --- | ----------------------------------------------- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config)#     | no  | dhcpv4-snooping | static-attributes  |
| ------------------- | --- | --------------- | ------------------ |
| Command History     |     |                 |                    |
| Release             |     |                 | Modification       |
| 10.10               |     |                 | Commandintroduced. |
| Command Information |     |                 |                    |
DHCPsnooping|144

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |       | trust |     |     |
| ------------------ | ----- | ----- | --- | --- |
| dhcpv4-snooping    | trust |       |     |     |
| no dhcpv4-snooping |       | trust |     |     |
Description
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
| switch(config)#    |     | interface          | 2/2/1 |       |
| ------------------ | --- | ------------------ | ----- | ----- |
| switch(config-if)# |     | no dhcpv4-snooping |       | trust |
| switch(config-if)# |     | exit               |       |       |
switch(config)#
| Command History |     |     |     |                                                 |
| --------------- | --- | --- | --- | ----------------------------------------------- |
| Release         |     |     |     | Modification                                    |
| 10.09.1000      |     |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |     |           |
| ------------------- | ------- | ------- | --- | --------- |
| Platforms           | Command | context |     | Authority |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv4-snooping    |        | verify | mac |     |
| ------------------ | ------ | ------ | --- | --- |
| dhcpv4-snooping    | verify | mac    |     |     |
| no dhcpv4-snooping |        | verify | mac |     |
Description
145
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

ThiscommandenablesverificationofthehardwareaddressfieldinDHCPclientpackets.Whenenabled,
theDHCPclienthardwareaddressfieldandthesourceMACaddressmustbethesameforpackets
receivedonuntrustedportsorelsethepacketisdropped.ThisDHCPsnoopingMACverificationis
enabledbydefault.
ThenoformofthecommanddisablesDHCPv4snoopingMACverification.
Examples
EnablingDHCPv4snoopingMACverification:
| switch(config)# | dhcpv4-snooping |     | verify mac |     |     |     |
| --------------- | --------------- | --- | ---------- | --- | --- | --- |
DisablingDHCPv4snoopingMACverification:
| switch(config)# | no  | dhcpv4-snooping | verify mac                                      |     |     |     |
| --------------- | --- | --------------- | ----------------------------------------------- | --- | --- | --- |
| Command History |     |                 |                                                 |     |     |     |
| Release         |     |                 | Modification                                    |     |     |     |
| 10.09.1000      |     |                 | Commandintroducedforthe8360SwitchSeries.        |     |     |     |
| 10.09           |     |                 | Commandintroducedforthe6000and6100SwitchSeries. |     |     |     |
10.07orearlier
| Command Information |         |         |           |     |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- | --- |
| Platforms           | Command | context | Authority |     |     |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show dhcpv4-snooping
show dhcpv4-snooping
Description
ShowstheDHCPv4snoopingconfiguration.
Examples
ShowingtheDHCPv4snoopingconfiguration:
| switch#           | show dhcpv4-snooping |     |       |            |         |         |
| ----------------- | -------------------- | --- | ----- | ---------- | ------- | ------- |
| DHCPv4-Snooping   | Information          |     |       |            |         |         |
| DHCPv4-Snooping   |                      |     | : Yes | Verify MAC | Address | : Yes   |
| Allow Overwrite   | Binding              |     | : No  | Enabled    | VLANs   | : 1-100 |
| Static Attributes |                      |     | : Yes |            |         |         |
| Client Event      | Logs                 |     | : Yes |            |         |         |
DHCPsnooping|146

| Option        | 82 Configurations |                |             |                        |                 |         |           |       |
| ------------- | ----------------- | -------------- | ----------- | ---------------------- | --------------- | ------- | --------- | ----- |
| Untrusted     | Policy            |                |             |                        | : replace       |         | Insertion | : Yes |
| Option        | 82 Remote-id      |                |             |                        | : mac           |         |           |       |
| External      | Storage           | Information    |             |                        |                 |         |           |       |
| Volume        | Name              | : ipbinding    |             |                        |                 |         |           |       |
| File Name     |                   | : ipv4Bindings |             |                        |                 |         |           |       |
| Inactive      | Since             | : 01:23:20     |             | 09/10/2021             |                 |         |           |       |
| Error         |                   | : File         | Write       | Failure                |                 |         |           |       |
| Flash Storage |                   | Information    |             |                        |                 |         |           |       |
| File Write    | Delay             | :              | 300 seconds |                        |                 |         |           |       |
| Active        | Storage           | :              | External    |                        |                 |         |           |       |
| Authorized    | Server            | Configurations |             |                        |                 |         |           |       |
| VRF           |                   |                |             |                        | Authorized      | Servers |           |       |
| ------------  |                   |                |             | ---------------------- |                 |         |           |       |
| default       |                   |                |             |                        | 1.1.10.3        |         |           |       |
| default       |                   |                |             |                        | 10.10.10.1      |         |           |       |
| default       |                   |                |             |                        | 10.10.10.56     |         |           |       |
| default       |                   |                |             |                        | 200.10.10.3     |         |           |       |
| green         |                   |                |             |                        | 1.1.10.3        |         |           |       |
| green         |                   |                |             |                        | 1.10.10.3       |         |           |       |
| green         |                   |                |             |                        | 10.10.100.3     |         |           |       |
| red           |                   |                |             |                        | 192.168.122.53  |         |           |       |
| red           |                   |                |             |                        | 192.168.122.121 |         |           |       |
Port Information
|            |         |       | Max      |     | Static                                          |     | Dynamic  |     |
| ---------- | ------- | ----- | -------- | --- | ----------------------------------------------- | --- | -------- | --- |
| Port       |         | Trust | Bindings |     | Bindings                                        |     | Bindings |     |
| --------   |         | ----- | -------- |     | --------                                        |     | -------- |     |
| 1/1/2      |         | Yes   | 5000     |     | 50                                              |     | 0        |     |
| 1/1/3      |         | Yes   | 8192     |     | 0                                               |     | 0        |     |
| 1/1/5      |         | Yes   | 8192     |     | 0                                               |     | 22       |     |
| 1/1/16     |         | No    | 100      |     | 0                                               |     | 0        |     |
| 10/10/10   |         | No    | 8100     |     | 320                                             |     | 200      |     |
| lag120     |         | No    | 512      |     | 0                                               |     | 0        |     |
| Command    | History |       |          |     |                                                 |     |          |     |
| Release    |         |       |          |     | Modification                                    |     |          |     |
| 10.09.1000 |         |       |          |     | Commandintroducedforthe8360SwitchSeries.        |     |          |     |
| 10.09      |         |       |          |     | Commandintroducedforthe6000and6100SwitchSeries. |     |          |     |
| 10.08      |         |       |          |     | Updatedexamplewithflashstorageinformation.      |     |          |     |
10.07orearlier
| Command | Information |     |     |     |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
147
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

| Platforms | Command | context |     | Authority                                            |     |     |
| --------- | ------- | ------- | --- | ---------------------------------------------------- | --- | --- |
| 6200      |         |         |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv4-snooping |     |         | binding |     |     |     |
| -------------------- | --- | ------- | ------- | --- | --- | --- |
| show dhcpv4-snooping |     | binding |         |     |     |     |
Description
ShowstheDHCPv4snoopingbindingconfiguration.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
detail ShowsdetailedinformationforactiveIPbindingsonthesystem.
Examples
ShowingtheDHCPv4snoopingbindingconfiguration:
| switch(config)#   |     | show dhcpv4-snooping |     | binding |           |           |
| ----------------- | --- | -------------------- | --- | ------- | --------- | --------- |
| MacAddress        |     | IP                   |     | VLAN    | Interface | Time-Left |
| ----------------- |     | ---------------      |     | ----    | --------- | --------- |
| aa:b1:c1:dd:ee:ff |     | 10.2.3.4             |     | 1       | 1/1/2     | 582       |
| aa:b2:c2:dd:ee:ff |     | 10.2.3.5             |     | 1       | 1/1/2     | 584       |
ShowingdetailedinformationforactiveIPbindings:
| switch(config)# |             | show dhcpv4-snooping |                     | binding | detail  |     |
| --------------- | ----------- | -------------------- | ------------------- | ------- | ------- | --- |
| VLAN Id         | : 2, MAC    | : 00:50:56:96:74:46  |                     |         |         |     |
| IP              |             | Interface            | Time-Left           |         |         |     |
| --------------- |             | ---------            | ------------------- |         |         |     |
| 100.1.2.100     |             | 1/1/23               | 194                 |         |         |     |
| Static          | Attributes: |                      |                     |         |         |     |
| Default         | Router      | : 100.1.2.1,         | 192.1.1.1,          |         | 1.1.1.2 |     |
| Server          | IP          | : 10.1.84.2          |                     |         |         |     |
| Name Servers    |             | : 192.1.1.2,         | 2.2.2.2,            |         | 1.1.1.1 |     |
| VLAN Id         | : 3, MAC    | : 00:50:56:96:e5:8e  |                     |         |         |     |
| IP              |             | Interface            | Time-Left           |         |         |     |
| --------------- |             | ---------            | ------------------- |         |         |     |
| 100.1.3.100     |             | 2/1/22               | 145                 |         |         |     |
| Static          | Attributes: |                      |                     |         |         |     |
| Default         | Router      | : 100.1.3.1,         | 192.1.1.1,          |         | 1.1.1.2 |     |
| Server          | IP          | : 10.1.84.2          |                     |         |         |     |
| Name Servers    |             | : 192.1.1.2,         | 2.2.2.2,            |         | 1.1.1.1 |     |
| VLAN Id         | : 3, MAC    | : 00:11:01:00:00:03  |                     |         |         |     |
DHCPsnooping|148

| IP              |             | Interface     |     | Time-Left           |                                                 |         |             |     |
| --------------- | ----------- | ------------- | --- | ------------------- | ----------------------------------------------- | ------- | ----------- | --- |
| --------------- |             | ---------     |     | ------------------- |                                                 |         |             |     |
| 100.1.3.99      |             | 2/1/24        |     | 137                 |                                                 |         |             |     |
| Static          | Attributes: |               |     |                     |                                                 |         |             |     |
| Default         | Router      | : 100.1.3.1,  |     | 192.1.1.1,          |                                                 | 1.1.1.2 |             |     |
| Server          | IP          | : 10.1.84.2   |     |                     |                                                 |         |             |     |
| Name Servers    |             | :192.168.0.1, |     | 192.168.1.1,        |                                                 |         | 192.168.2.1 |     |
| Command History |             |               |     |                     |                                                 |         |             |     |
| Release         |             |               |     |                     | Modification                                    |         |             |     |
| 10.10           |             |               |     |                     | Detailparameteradded.                           |         |             |     |
| 10.09.1000      |             |               |     |                     | Commandintroducedforthe8360SwitchSeries.        |         |             |     |
| 10.09           |             |               |     |                     | Commandintroducedforthe6000and6100SwitchSeries. |         |             |     |
10.07orearlier
| Command Information |         |         |     |     |                                                      |     |     |     |
| ------------------- | ------- | ------- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
| Platforms           | Command | context |     |     | Authority                                            |     |     |     |
| 6200                |         |         |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |     |
Operator(>)orManager
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv4-snooping |     |            | statistics |     |     |     |     |     |
| -------------------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- |
| show dhcpv4-snooping |     | statistics |            |     |     |     |     |     |
Description
ShowstheDHCPv4snoopingstatistics.
Examples
ShowingtheDHCPv4snoopingstatistics:
| switch(config)# |         | show dhcpv4-snooping |                               |         | statistics  |           |       |           |
| --------------- | ------- | -------------------- | ----------------------------- | ------- | ----------- | --------- | ----- | --------- |
| Packet-Type     | Action  |                      | Reason                        |         |             |           |       | Count     |
| -----------     | ------- |                      | ----------------------------- |         |             |           |       | --------- |
| server          | forward |                      | from                          | trusted | port        |           |       | 5425      |
| client          | forward |                      | to trusted                    |         | port        |           |       | 3895      |
| server          | drop    |                      | received                      | on      | untrusted   |           | port  | 117       |
| server          | drop    |                      | unauthorized                  |         | server      |           |       | 214       |
| client          | drop    |                      | destination                   |         | on          | untrusted | port  | 78        |
| client          | drop    |                      | untrusted                     |         | option      | 82 field  |       | 85        |
| client          | drop    |                      | bad DHCP                      | release |             | request   |       | 0         |
| client          | drop    |                      | failed                        | verify  | MAC         | check     |       | 5         |
| client          | drop    |                      | failed                        | on      | max-binding |           | limit | 15        |
| Command History |         |                      |                               |         |             |           |       |           |
149
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

| Release    |     |     | Modification                                    |     |
| ---------- | --- | --- | ----------------------------------------------- | --- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
| Command   | Information |         |           |     |
| --------- | ----------- | ------- | --------- | --- |
| Platforms | Command     | context | Authority |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| DHCPv6                | snooping | commands |     |     |
| --------------------- | -------- | -------- | --- | --- |
| clear dhcpv6-snooping |          | binding  |     |     |
clear dhcpv6-snooping binding {all | ip <IPV6-ADDR> vlan <VLAN-ID> | interface <IFNAME> |
vlan <VLAN-ID>}
Description
ClearsDHCPv6snoopingbindingentries.
| Parameter |     |     | Description                                            |     |
| --------- | --- | --- | ------------------------------------------------------ | --- |
| all       |     |     | SpecifiesthatallDHCPv6bindinginformationistobecleared. |     |
ip <IPV6-ADDR> vlan <VLAN-ID> SpecifiestheIPv6addressandVLANforwhichallDHCPv6binding
informationistobecleared.
| interface | <IFNAME> |     |     |     |
| --------- | -------- | --- | --- | --- |
SpecifiestheinterfaceforwhichallDHCPv6bindinginformationis
tobecleared.
vlan <VLAN-ID> SpecifiestheVLANforwhichallDHCPv6bindinginformationisto
becleared.Range:1to4094.
Examples
ClearingallDHCPv6bindinginformationfor5000::1vlan1:
switch(config)# clear dhcpv6-snooping binding ip 5000::1 vlan 1
ClearingallDHCPv6bindinginformationforinterface1/1/10:
| switch(config)# | clear | dhcpv6-snooping | binding interface | 1/1/10 |
| --------------- | ----- | --------------- | ----------------- | ------ |
ClearingallDHCPv6bindinginformationforVLAN10:
DHCPsnooping|150

| switch(config)# | clear | dhcpv6-snooping |     | binding | vlan | 10  |
| --------------- | ----- | --------------- | --- | ------- | ---- | --- |
ClearingallDHCPv6bindinginformation:
| switch(config)# | clear | dhcpv6-snooping |                                                 | binding | all |     |
| --------------- | ----- | --------------- | ----------------------------------------------- | ------- | --- | --- |
| Command History |       |                 |                                                 |         |     |     |
| Release         |       |                 | Modification                                    |         |     |     |
| 10.09.1000      |       |                 | Commandintroducedforthe8360SwitchSeries.        |         |     |     |
| 10.09           |       |                 | Commandintroducedforthe6000and6100SwitchSeries. |         |     |     |
10.07orearlier
| Command Information |         |         |                                                      |     |     |     |
| ------------------- | ------- | ------- | ---------------------------------------------------- | --- | --- | --- |
| Platforms           | Command | context | Authority                                            |     |     |     |
| 6200                |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |     |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| clear dhcpv6-snooping |     | guard-policy |     |     | statistics |     |
| --------------------- | --- | ------------ | --- | --- | ---------- | --- |
clear dhcpv6-snooping guard-policy statistics [vlan <VLAN-ID> | interface <INTERFACE-
NAME>]
Description
ClearsallDHCPv6snoopingguardpolicystatisticsfromthespecifiedVLANorinterface.
| Parameter        |     |     | Description                      |     |     |     |
| ---------------- | --- | --- | -------------------------------- | --- | --- | --- |
| <VLAN-ID>        |     |     | SpecifiestheVLANID.Range:1-4094. |     |     |     |
| <INTERFACE-NAME> |     |     | Specifiestheinterfacename.       |     |     |     |
Examples
ClearingallDHCPv6snoopingguardpolicystatisticsfromVLAN100:
| switch# | clear dhcpv6-snooping |     | guard-policy |     | statistics | vlan 100 |
| ------- | --------------------- | --- | ------------ | --- | ---------- | -------- |
ClearingallDHCPv6snoopingguardpolicystatisticsfrominterface1/1/10:
switch# clear dhcpv6-snooping guard-policy statistics interface 1/1/10
| Command History |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- |
151
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

| Release             |         |         | Modification       |
| ------------------- | ------- | ------- | ------------------ |
| 10.10               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| clear dhcpv6-snooping |     | statistics |     |
| --------------------- | --- | ---------- | --- |
| clear dhcpv6-snooping |     | statistics |     |
Description
ClearsallDHCPv6snoopingstatistics.
Examples
ClearallDHCPv6snoopingstatistics:
| switch#         | clear dhcpv6-snooping | statistics |                                                 |
| --------------- | --------------------- | ---------- | ----------------------------------------------- |
| Command History |                       |            |                                                 |
| Release         |                       |            | Modification                                    |
| 10.09.1000      |                       |            | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |                       |            | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
dhcpv6-snooping
dhcpv6-snooping
no dhcpv6-snooping
Description
EnablesDHCPv6snooping.DHCPv6snoopingisdisabledbydefault.DHCPv6snoopingisnotsupported
onthemanagementinterface.
DHCPsnooping|152

ThenoformofthecommanddisablesDHCPv6snooping,flushingalltheIPbindingslearnedsince
DHCPv6snoopingwasenabled.
Examples
EnablingDHCPv6snooping:
| switch(config)# | dhcpv6-snooping |     |     |
| --------------- | --------------- | --- | --- |
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
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
153
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| switch(config)# | vlan | 100 |     |
| --------------- | ---- | --- | --- |
switch(config-vlan-100)#
no dhcpv6-snooping
| switch(config-vlan-100)# |     | exit |     |
| ------------------------ | --- | ---- | --- |
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
6200 config-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Parameter   |     |     | Description                                      |
| ----------- | --- | --- | ------------------------------------------------ |
| <IPV6-ADDR> |     |     | SpecifiestheIPv6addressofthetrustedDHCPv6server. |
vrf <VRF-NAME>
SpecifiestheVRFname.Thenamemustbedefault.
Usage
DHCPsnooping|154

Forauthorizedserverlookup,theVRFisderivedfromtheSwitchVirtualInterface(SVI)configuredfor
theincomingVLAN.IftheSVIisnotconfigured,thedefaultVRFisassumed.
Examples
AddingDHCPserversABCD:5ACD::2000,andABCD:5ACD::2010totheauthorizedserverlist:
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2010 vrf default
RemovingDHCPserverABCD:5ACD::2000fromtheauthorizedserverlist:
switch(config)# no dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
| Command History     |         |         |     |                   |     |
| ------------------- | ------- | ------- | --- | ----------------- | --- |
| Release             |         |         |     | Modification      |     |
| 10.07orearlier      |         |         |     | Commandintroduced |     |
| Command Information |         |         |     |                   |     |
| Platforms           | Command | context |     | Authority         |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-snooping    |           | event-log |        | client |     |
| ------------------ | --------- | --------- | ------ | ------ | --- |
| dhcpv6-snooping    | event-log |           | client |        |     |
| no dhcpv6-snooping |           | event-log | client |        |     |
Description
ThiscommandenablesordisablesDHCPv6snoopingclientleveleventlogsthathelpwithclient
telemetryonaremotemanagementstationsuchasArubaCentral.Bydefault,clientleveleventlogsare
disabled.Thenoformofthiscommanddisablesclient-leveleventlogsforDHCPv6snoopingafterthey
areenabled.ViewtheseloggedDHCPv6snoopingeventsbyissuingthecommandshow events -c
dhcpv6-snooping.
Examples
EnablingDHCPv6clientleveleventlogs:
| switch(config)# |     | # dhcpv6-snooping |     | event-log | client |
| --------------- | --- | ----------------- | --- | --------- | ------ |
Disablingexternalstorage:
| witch(config)#  | #   | no dhcpv6-snooping |     | event-log | client |
| --------------- | --- | ------------------ | --- | --------- | ------ |
| Command History |     |                    |     |           |        |
155
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

Release

10.10

Modification

Command introduced.

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

DHCP snooping | 156

Disablingexternalstoragewhenflashstorageisalsoconfigured(notethemessageindicatingthatflash
storagewillbeused):
switch(config)# no dhcpv6-snooping external-storage volume dhcp_snoop
DHCPv6-Snooping will use flash storage to store IP Binding database
switch(config)#
| Command History     |         |         |                                            |
| ------------------- | ------- | ------- | ------------------------------------------ |
| Release             |         |         | Modification                               |
| 10.08               |         |         | Updatedexamplewithflashstorageinformation. |
| 10.07orearlier      |         |         | Commandintroduced                          |
| Command Information |         |         |                                            |
| Platforms           | Command | context | Authority                                  |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
157
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
delay <DELAY> Specifiesthedelayinsecondsbetweenwrites(whennecessary)to
theflashstorage,Default:900.Range:300to86400.
Examples
ConfiguringswitchflashstorageforDHCPsnoopingIPbindingstoragewithawritedelayof1200
seconds:
| switch(config)# | dhcpv6-snooping |     |     | flash-storage | delay 1200 |
| --------------- | --------------- | --- | --- | ------------- | ---------- |
Warning: Using flash storage reduces switch lifetime. It is recommended to use an
external-storage.
| Do you want | to continue |     | (y/n)? | y   |     |
| ----------- | ----------- | --- | ------ | --- | --- |
switch(config)#
UnconfiguringusageofswitchflashstorageforIPbindings:
| switch(config)#     | no      | dhcpv6-snooping |     | flash-storage |                   |
| ------------------- | ------- | --------------- | --- | ------------- | ----------------- |
| Command History     |         |                 |     |               |                   |
| Release             |         |                 |     |               | Modification      |
| 10.07               |         |                 |     |               | Commandintroduced |
| Command Information |         |                 |     |               |                   |
| Platforms           | Command | context         |     | Authority     |                   |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-snooping    |              | max-bindings |                |     |     |
| ------------------ | ------------ | ------------ | -------------- | --- | --- |
| dhcpv6-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |
| no dhcpv6-snooping | max-bindings |              | <MAX-BINDINGS> |     |     |
Description
SetsthemaximumnumberofDHCPv6bindingsallowedontheselectedinterface.Forallinterfaceson
whichthiscommandisnotrun,thedefaultmaxbindingisthemaximumvalueoftherange.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<MAX-BINDINGS>
SpecifiesthemaximumnumberofDHCPbindings.Range1to
1024.
Examples
SettheDHCPv6maxbindingsto256oninterface1/1/1:
DHCPsnooping|158

| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
|                    |     | dhcpv6-snooping |     | max-bindings | 256 |
| ------------------ | --- | --------------- | --- | ------------ | --- |
| switch(config-if)# |     | exit            |     |              |     |
switch(config)#
RevertDHCPv6maxbindingstoitsdefaultoninterface1/1/1:
| switch(config)#    |     | interface          | 1/1/1 |              |     |
| ------------------ | --- | ------------------ | ----- | ------------ | --- |
| switch(config-if)# |     | no dhcpv6-snooping |       | max-bindings | 256 |
| switch(config-if)# |     | exit               |       |              |     |
switch(config)#
| Command History     |         |         |     |                   |     |
| ------------------- | ------- | ------- | --- | ----------------- | --- |
| Release             |         |         |     | Modification      |     |
| 10.07               |         |         |     | Commandintroduced |     |
| Command Information |         |         |     |                   |     |
| Platforms           | Command | context |     | Authority         |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| dhcpv6-snooping    |       | trust |     |     |     |
| ------------------ | ----- | ----- | --- | --- | --- |
| dhcpv6-snooping    | trust |       |     |     |     |
| no dhcpv6-snooping |       | trust |     |     |     |
Description
EnablesDHCPv6snoopingtrustontheselectedinterface.Onlyserverpacketsreceivedontrusted
interfacesareforwarded.Alltheinterfacesareuntrustedbydefault.
ThenoformofthecommanddisablesDHCPv6snoopingtrustontheselectedinterface.
config-if
Examples
EnablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface       | 2/2/1 |       |     |
| ------------------ | --- | --------------- | ----- | ----- | --- |
| switch(config-if)# |     | dhcpv6-snooping |       | trust |     |
| switch(config-if)# |     | exit            |       |       |     |
switch(config)#
DisablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface          | 2/2/1 |       |     |
| ------------------ | --- | ------------------ | ----- | ----- | --- |
| switch(config-if)# |     | no dhcpv6-snooping |       | trust |     |
| switch(config-if)# |     | exit               |       |       |     |
switch(config)#
159
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| Command   | History     |         |                   |     |
| --------- | ----------- | ------- | ----------------- | --- |
| Release   |             |         | Modification      |     |
| 10.07     |             |         | Commandintroduced |     |
| Command   | Information |         |                   |     |
| Platforms | Command     | context | Authority         |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| match server    | access-list |            |     |     |
| --------------- | ----------- | ---------- | --- | --- |
| match server    | access-list | <ACL-NAME> |     |     |
| no match server | access-list | <ACL-NAME> |     |     |
Description
ConfiguresanaccesslisttoaDHCPv6snoopingguardpolicy,enablingtheDHCPv6snoopingguard
policytoallowordenythespecificDHCPservertoassignanIPv6address.Ifnofiltersareapplied,DHCP
servertrafficfromanysourceIPaddressisallowedinthetrustedport.
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
| Command | History     |     |                    |     |
| ------- | ----------- | --- | ------------------ | --- |
| Release |             |     | Modification       |     |
| 10.10   |             |     | Commandintroduced. |     |
| Command | Information |     |                    |     |
DHCPsnooping|160

| Platforms |     | Command |     | context |     | Authority |     |
| --------- | --- | ------- | --- | ------- | --- | --------- | --- |
6200 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| match        | client | prefix-list |     |                    |     |     |     |
| ------------ | ------ | ----------- | --- | ------------------ | --- | --- | --- |
| match client |        | prefix-list |     | <PREFIX-LIST-NAME> |     |     |     |
| no match     | client | prefix-list |     | <PREFIX-LIST-NAME> |     |     |     |
Description
Configuresaprefix-listfortheDHCPv6snoopingguardpolicyenablingthepolicytoallowtheassigned
IPv6addresseswithinaspecificprefixrange.
ThenoformofthecommandremovesaprefixlistfromtheDHCPv6snoopingguardpolicy.
| Parameter          |     |     |     |     | Description                          |     |     |
| ------------------ | --- | --- | --- | --- | ------------------------------------ | --- | --- |
| <PREFIX-LIST-NAME> |     |     |     |     | SpecifiesthenameoftheIPv6prefixlist. |     |     |
Examples
Addingaprefixlistnamedpref1tothepol1DHCPv6snoopingguardpolicy:
switch(config)# ipv6 prefix-list pref1 permit 2001:db8::/64 le 128
| switch(config)#                     |     |     | dhcpv6-snooping |     | guard-policy | pol1        |             |
| ----------------------------------- | --- | --- | --------------- | --- | ------------ | ----------- | ----------- |
| switch(config-dhcpv6-guard-policy)# |     |     |                 |     | match        | client      | prefix-list |
| <ipv6-prefix-list-name>             |     |     |                 |     | IPv6         | prefix-list | name        |
switch(config-dhcpv6-guard-policy)# match client prefix-list pref1
Deletingtheprefixlistnamedprf1fromthepol1DHCPv6snoopingguardpolicy:
| switch(config)# |     |     | dhcpv6-snooping |     | guard-policy | pol1 |     |
| --------------- | --- | --- | --------------- | --- | ------------ | ---- | --- |
switch(config-dhcpv6-guard-policy)# no match client prefix-list <ipv6-prefix-list-
name>
| Command   | History     |         |     |         |                    |           |     |
| --------- | ----------- | ------- | --- | ------- | ------------------ | --------- | --- |
| Release   |             |         |     |         | Modification       |           |     |
| 10.10     |             |         |     |         | Commandintroduced. |           |     |
| Command   | Information |         |     |         |                    |           |     |
| Platforms |             | Command |     | context |                    | Authority |     |
6200 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
preference
| preference | [minimum |     | | maximum | ]   | <VALUE> |     |     |
| ---------- | -------- | --- | --------- | --- | ------- | --- | --- |
161
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

no preference
Description
EnablesaDHCPv6snoopingguardpolicytoallowordenytheDHCPv6serversinthespecifiedserver
preferencerange.Ifnotconfiguredtheminimumpreferenceissetto0andmaximumpreferenceisset
to255.
ThenoformofthecommandremovestheserverpreferencelimitsonthespecifiedDHCPv6snooping
guardpolicy.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
minimum <VALUE> Specifiestheminimumvaluefortheserverpreferencerange.
Range:1-255.
maximum <VALUE> Specifiesthemaximumvaluefortheserverpreferencerange.
Range:1-255.
Examples
Settingtheminimumandmaximumserverpreferencerangeto6-250onDHCPv6snoopingguard
policypol1:
| switch(config)#                     | dhcpv6-snooping |     | guard-policy | pol1    |
| ----------------------------------- | --------------- | --- | ------------ | ------- |
| switch(config-dhcpv6-guard-policy)# |                 |     | preference   | min 6   |
| switch(config-dhcpv6-guard-policy)# |                 |     | preference   | max 250 |
DisablingtheserverpreferencerangeonDHCPv6snoopingguardpolicypol1:
| switch(config)#                     | dhcpv6-snooping |         | guard-policy       | pol1       |
| ----------------------------------- | --------------- | ------- | ------------------ | ---------- |
| switch(config-dhcpv6-guard-policy)# |                 |         | no                 | preference |
| Command History                     |                 |         |                    |            |
| Release                             |                 |         | Modification       |            |
| 10.10                               |                 |         | Commandintroduced. |            |
| Command Information                 |                 |         |                    |            |
| Platforms                           | Command         | context |                    | Authority  |
6200 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
show dhcpv6-snooping
show dhcpv6-snooping
Description
ShowstheDHCPv6snoopingconfiguration.
Examples
DHCPsnooping|162

ShowingtheDHCPv6snoopingconfiguration:
| switch#         | show            | dhcpv6-snooping |         |              |            |                    |                 |
| --------------- | --------------- | --------------- | ------- | ------------ | ---------- | ------------------ | --------------- |
| DHCPv6-Snooping |                 | Information     |         |              |            |                    |                 |
|                 | DHCPv6-Snooping |                 | :       | Yes Enabled  | VLANs      |                    | : 1,5,7,100-110 |
|                 | Trusted Port    | Bindings        | Enabled |              | VLANs :    |                    |                 |
|                 | Client Event    | Logs            |         |              | : Yes      |                    |                 |
| External        | Storage         | Information     |         |              |            |                    |                 |
|                 | Volume Name     |                 |         | : dhcp_snoop |            |                    |                 |
|                 | File Name       |                 |         | : ip_binding |            |                    |                 |
|                 | Inactive        | Since           |         | : 01:23:20   | 09/10/2021 |                    |                 |
|                 | Error           |                 |         | : Failed     | to write   | external           | storage         |
| Flash           | Storage         | Information     |         |              |            |                    |                 |
|                 | File Write      | Delay           |         | : 300        | seconds    |                    |                 |
|                 | Active          | Storage         |         | : External   |            |                    |                 |
| Authorized      | Server          | Configurations  |         |              |            |                    |                 |
| VRF             |                 |                 |         |              |            | Authorized         | Servers         |
| ------------    |                 |                 |         |              |            | ------------------ |                 |
default
2001:0db8:85a3:0000:0000:8a2e:0370:7334
| default |     |     |     |     |     | 2002::2 |     |
| ------- | --- | --- | --- | --- | --- | ------- | --- |
| default |     |     |     |     |     | 2004::1 |     |
| red     |     |     |     |     |     | 2002::1 |     |
| red     |     |     |     |     |     | 2002::2 |     |
| red     |     |     |     |     |     | 2002::9 |     |
| green   |     |     |     |     |     | 5000::1 |     |
| green   |     |     |     |     |     | 5000::2 |     |
| green   |     |     |     |     |     | 5000::3 |     |
| green   |     |     |     |     |     | 5000::7 |     |
| green   |     |     |     |     |     | 5000::8 |     |
Port Information
|                |             |       |     | Max      | Static                                     | Dynamic  |     |
| -------------- | ----------- | ----- | --- | -------- | ------------------------------------------ | -------- | --- |
| Port           |             | Trust |     | Bindings | Bindings                                   | Bindings |     |
| --------       |             | ----- |     | -------- | --------                                   | -------- |     |
| 1/1/2          |             | Yes   |     | 0        | 0                                          | 0        |     |
| 1/1/3          |             | Yes   |     | 0        | 3                                          | 0        |     |
| 1/1/5          |             | Yes   |     | 0        | 22                                         | 0        |     |
| 1/1/16         |             | No    |     | 256      | 0                                          | 20       |     |
| 10/10/10       |             | No    |     | 256      | 12                                         | 7        |     |
| lag120         |             | No    |     | 256      | 3                                          | 0        |     |
| Command        | History     |       |     |          |                                            |          |     |
| Release        |             |       |     |          | Modification                               |          |     |
| 10.08          |             |       |     |          | Updatedexamplewithflashstorageinformation. |          |     |
| 10.07orearlier |             |       |     |          | Commandintroduced                          |          |     |
| Command        | Information |       |     |          |                                            |          |     |
163
AOS-CX10.11IPServicesGuide| (6200SwitchSeries)

| Platforms | Command | context |     | Authority                                            |     |
| --------- | ------- | ------- | --- | ---------------------------------------------------- | --- |
| 6200      |         |         |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |         | binding |     |     |
| -------------------- | --- | ------- | ------- | --- | --- |
| show dhcpv6-snooping |     | binding |         |     |     |
Description
ShowstheDHCPv6snoopingbindingconfiguration.
Examples
ShowingtheDHCPv6snoopingbindingconfiguration:
| switch#    | show dhcpv6-snooping |     | binding |     |     |
| ---------- | -------------------- | --- | ------- | --- | --- |
| IP Binding | Information          |     |         |     |     |
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
| Command Information |         |         |     |           |     |
| ------------------- | ------- | ------- | --- | --------- | --- |
| Platforms           | Command | context |     | Authority |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| dhcpv6-snooping    |              | guard-policy |               |     |     |
| ------------------ | ------------ | ------------ | ------------- | --- | --- |
| dhcpv6-snooping    | guard-policy |              | <POLICY-NAME> |     |     |
| no dhcpv6-snooping |              | guard-policy | <POLICY-NAME> |     |     |
Description
DHCPsnooping|164

ConfiguresaDHCPv6snoopingguardpolicywiththegivennameandenterstheguardpolicy
configurationcontext.
Thenoformofthecommanddisablesthespecifiedguardpolicy.
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
| switch(config)#          |           | vlan 100 |                 |                    |                                           |     |      |
| ------------------------ | --------- | -------- | --------------- | ------------------ | ----------------------------------------- | --- | ---- |
| switch(config-vlan-100)# |           |          | dhcpv6-snooping |                    | guard-policy                              |     | pol1 |
| Command History          |           |          |                 |                    |                                           |     |      |
| Release                  |           |          |                 | Modification       |                                           |     |      |
| 10.10                    |           |          |                 | Commandintroduced. |                                           |     |      |
| Command Information      |           |          |                 |                    |                                           |     |      |
| Platforms                | Command   |          | context         |                    | Authority                                 |     |      |
| 6200                     | config    |          |                 |                    | Administratorsorlocalusergroupmemberswith |     |      |
|                          | config-if |          |                 |                    | executionrightsforthiscommand.            |     |      |
config-dhcpv6-guard-policy
config-vlan-<VLAN-ID>
| show dhcpv6-snooping |     |                             | guard-policy |     |     |     |     |
| -------------------- | --- | --------------------------- | ------------ | --- | --- | --- | --- |
| show dhcpv6-snooping |     | guard-policy[<POLICY_NAME>] |              |     |     |     |     |
165
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- |

Description
ShowstheDHCPv6snoopingguardpolicyconfiguration.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<POLICY-NAME> SpecifiestheDHCPv6snoopingguardpolicyforwhichthe
informationisdisplayed.
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
DHCPsnooping|166

| Command Information |         |         |     |           |     |     |
| ------------------- | ------- | ------- | --- | --------- | --- | --- |
| Platforms           | Command | context |     | Authority |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |              | guard-policy |            | interface         |     |
| -------------------- | --- | ------------ | ------------ | ---------- | ----------------- | --- |
| show dhcpv6-snooping |     | guard-policy |              | [interface | <INTERFACE-NAME>] |     |
Description
ShowstheDHCPv6snoopingguardpolicyconfigurationandstatisticsforthespecifiedinterface.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-NAME> SpecifiestheinterfacenameforwhichtheDHCPv6guardcounter
informationisdisplayed.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfigurationandstatisticsforinterface1/1/1:
| switch# | show dhcpv6-snooping |                 |     | guard-policy | int 1/1/1 |     |
| ------- | -------------------- | --------------- | --- | ------------ | --------- | --- |
| DHCPv6  | Guard                | Policy Applied  |     | : pol1       |           |     |
| DHCPv6  | Guard                | Policy Counters |     |              |           |     |
==========================
| DHCPv6              | Packets | Received  |     | : 20               |                  |     |
| ------------------- | ------- | --------- | --- | ------------------ | ---------------- | --- |
| DHCPv6              | Packets | Forwarded |     | : 5                |                  |     |
| DHCPv6              | Packets | Dropped   |     | : 15               | [Total]          |     |
|                     |         |           |     | Access             | list error       | [7] |
|                     |         |           |     | Prefix             | list error       | [8] |
|                     |         |           |     | Server             | preference error | [0] |
| Command History     |         |           |     |                    |                  |     |
| Release             |         |           |     | Modification       |                  |     |
| 10.10               |         |           |     | Commandintroduced. |                  |     |
| Command Information |         |           |     |                    |                  |     |
| Platforms           | Command | context   |     | Authority          |                  |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |              | guard-policy |                  | vlan |     |
| -------------------- | --- | ------------ | ------------ | ---------------- | ---- | --- |
| show dhcpv6-snooping |     | guard-policy |              | [vlan <VLAN-ID>] |      |     |
Description
167
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

ShowstheDHCPv6snoopingguardpolicyconfigurationandstatisticsforthespecifiedVLAN.
| Parameter |     |     |     | Description                                      |     |     |
| --------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| <VLAN-ID> |     |     |     | SpecifiestheVLANID forwhichtheDHCPv6guardcounter |     |     |
informationisdisplayed.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfigurationandstatisticsforVLAN100:
| switch# | show dhcpv6-snooping |          | guard-policy |        | vlan 2 |     |
| ------- | -------------------- | -------- | ------------ | ------ | ------ | --- |
| DHCPv6  | Guard Policy         | Applied  |              | : pol1 |        |     |
| DHCPv6  | Guard Policy         | Counters |              |        |        |     |
==========================
| DHCPv6              | Packets Received  |         |     | : 20               |                  |     |
| ------------------- | ----------------- | ------- | --- | ------------------ | ---------------- | --- |
| DHCPv6              | Packets Forwarded |         |     | : 5                |                  |     |
| DHCPv6              | Packets Dropped   |         |     | : 15 [Total]       |                  |     |
|                     |                   |         |     | Access             | list error       | [0] |
|                     |                   |         |     | Prefix             | list error       | [8] |
|                     |                   |         |     | Server             | preference error | [7] |
| Command History     |                   |         |     |                    |                  |     |
| Release             |                   |         |     | Modification       |                  |     |
| 10.10               |                   |         |     | Commandintroduced. |                  |     |
| Command Information |                   |         |     |                    |                  |     |
| Platforms           | Command           | context |     | Authority          |                  |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |            |     | statistics |     |     |     |
| -------------------- | ---------- | --- | ---------- | --- | --- | --- |
| show dhcpv6-snooping | statistics |     |            |     |     |     |
Description
ShowstheDHCPv6snoopingstatistics.
Examples
ShowingtheDHCPv6snoopingstatistics:
| switch(config)# | show    | dhcpv6-snooping               |         | statistics |     |           |
| --------------- | ------- | ----------------------------- | ------- | ---------- | --- | --------- |
| Packet-Type     | Action  | Reason                        |         |            |     | Count     |
| -----------     | ------- | ----------------------------- |         |            |     | --------- |
| server          | forward | from                          | trusted | port       |     | 12        |
| client          | forward | to                            | trusted | port       |     | 20        |
DHCPsnooping|168

| server     |         | drop | received     |      | on untrusted                                    |           | port  | 5   |
| ---------- | ------- | ---- | ------------ | ---- | ----------------------------------------------- | --------- | ----- | --- |
| server     |         | drop | unauthorized |      | server                                          |           |       | 4   |
| client     |         | drop | destination  |      | on                                              | untrusted | port  | 2   |
| client     |         | drop | bad          | DHCP | release                                         | request   |       | 5   |
| server     |         | drop | relay        |      | reply on                                        | untrusted | port  | 2   |
| client     |         | drop | failed       |      | on max-binding                                  |           | limit | 5   |
| Command    | History |      |              |      |                                                 |           |       |     |
| Release    |         |      |              |      | Modification                                    |           |       |     |
| 10.09.1000 |         |      |              |      | Commandintroducedforthe8360SwitchSeries.        |           |       |     |
| 10.09      |         |      |              |      | Commandintroducedforthe6000and6100SwitchSeries. |           |       |     |
10.07orearlier
| Command   | Information |         |         |     |           |     |     |     |
| --------- | ----------- | ------- | ------- | --- | --------- | --- | --- | --- |
| Platforms |             | Command | context |     | Authority |     |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
Troubleshooting
| DHCP client | not | receiving | IP  |     |     |     |     |     |
| ----------- | --- | --------- | --- | --- | --- | --- | --- | --- |
1. Trustedportconfiguration
Checkiftheserverreachableportisconfiguredastrusted.
2. ValidatePacketdropcounters
Useshow dhcpv4-snooping statisticsandshow dhcpv6-snooping statisticscommandstoview
thepacketdropcounters.ThishelpstoidentifyapossiblereasonfortheterminationofDHCPpacket
exchangebetweenclientandserver.Afewpossiblereasonsarelistedbelow:
| n Maximumbindinglimitreached |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
o System-widelimit—ThemaximumbindinglimitissharedbetweenDHCPv4-Snooping,
DHCPv6-Snooping,ND-Snooping,andIP-Source-Bindings.Onreachingthelimit,DHCP
clientrequestsgetdropped.Tocheckthelimit,usetheshow capacities ip-bindings
command.
o Perportlimit:Thisisaperportconfigurablevalueforaprotocol.Onreachingthelimit,the
subsequentclientrequestsaredropped.
n ConflictswithIP-Source-Bindings—User-configuredIP-Source-Bindingsaregivenpriorityover
dynamicallylearnedbindings.Validateifthedynamicclientisconflictingwithanyofthe
existingIP-Source-Binding.
n Authorizedservercheckfailures—Authorizedserverconfigurationisglobal.Whenoneormore
authorizedserversaresetup,allserverrepliesshouldcomefromoneoftheauthorizedserver
IPaddresses.
169
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |

n CoPP packet drops—If the rate of the DHCP packets entering is higher than the configured

value, excessive packets are dropped by CoPP. Check CoPP statistics for the DHCP class and
configure the value accordingly. Higher CoPP values could cause other protocols to misbehave
depending on the platform.

3. Server configuration and reachability

Validate the following to ensure that the DHCP Server is reachable and configured correctly.

a. Check that the server is reachable over one of the trusted ports.

b. Check the server logs to understand the DHCP exchange status between client and server.

c. Check if DHCP Server pools are exhausted.

4. Option-82 configuration issues (Specific to DHCP Snooping IPv4)

a. This configuration usually arises when DHCP Snooping and Relay are configured on the same
VLAN. Option 82 at DHCP Snooping IPv4 should be disabled when configured for Inter-VRF
DHCP-Relay. Use no dhcpv4-snooping option 82 command to disable the functionality.

b. Option 82 is enabled by default, and the drop policy is set. If client packets are received with

option 82, then they are dropped with this configuration.

5. Server and client are connected to same the VLAN

a. Check if the server is reachable on the same VLAN as the client.

b.

If the server is on a different L3 network, configure DHCP-Relay to forward the packets
between the client and server.

6. Authorized server configurations—When configured, the server assigning IP address should be

one of the IP addresses from the authorized server list.

In DHCP snooping IPv6, if DHCP Relay is between a test device and a server, the authorised server
configuration should include a link to the local IP address of the relay interface. This is because, while
forwarding the server's response to the client, it will stamp a link to the local IP address as the source
IP of the packet.

IP-Binding mismatch in VSX topologies

1. Both primary and secondary VSX peers should have the same clock value. If not, there is a

possibility of inconsistent ip-bindings that could result in ip-binding sync in a loop. There is no
straight-forward way to check the inconsistencies but by looking at the number of bindings and
debug log analysis

2. Ensure the ISL state is up and operational.

DHCP client IP traffic is dropped at data path

1. This can happen when IP-Source-Lockdown is used along with DHCP snooping. Ensure IP-

Bindings are learned for clients that are experiencing traffic failure issues

2. Check the hardware programming state of the IP-Binding entry by IP-Source-Lockdown. Use show

ipv4 source-lockdown bindings or show ipv6 source-lockdown bindings commands.

DHCP snooping | 170

Chapter 7
DHCP Options
DHCP Options
AnumberofdeploymentsprovideaccesstoWANorpublicnetworkonlythroughaproxyserverforthe
networksecurity.ThissectionprovidesinformationaboutthevariousmethodsofHTTPproxy
configurationontheswitch.TheHTTPproxyconfiguredisusedtoconnecttoArubaActivateandAruba
Centralasperthezero-touchprovisioningrequirement.
HTTPproxylocationcanbeconfiguredusingtheCLIorRESTinterfaceorauto-configuredthroughthe
DHCP serverconnectedtotheswitch.
n TherearethreesourcesforHTTPproxylocation:
o
UserconfiguredHTTPproxyviaCLI orRESTinterface.
o DHCP optionsreceivedviamanagementVRFport.
o DHCPoptionsreceivedviaVLAN1onsupportedswitchplatforms.
nn OperationalconfigurationforHTTPproxylocationisdeterminedbythesourcewiththehighest
priority.Sourcepriority:
| 1.  | Userconfigured.                           |     |
| --- | ----------------------------------------- | --- |
| 2.  | DHCPoptionsreceivedviamanagement VRFport. |     |
| 3.  | DHCP optionsreceivedviaVLAN1.             |     |
n HTTPproxylocationcanonlybeaFQDNoranIPV4address.
n WhenHTTPproxylocationandVRFareconfigured,theyoverrideanyexistingHTTPproxylocationandVRF.
n IfthiscommandisexecutedwithouttheVRFparameter,thedefaultVRFwillbeused.
n PortnumbermayneedtobespecifiedattheendoftheIPaddressforFQDNtoconnectviaHTTPproxy.
o Forexample,8088istheTCPportnumber:http-proxy192.168.248.248:8088
| DHCP | options commands |     |
| ---- | ---------------- | --- |
http-proxy
| http-proxy    | {<FQDN | IPV4-ADDR>} | [vrf <VRF-NAME>] |
| ------------- | -------------------- | ---------------- |
| no http-proxy | [<FQDN | IPV4-ADDR>] | [vrf <VRF-NAME>] |
Description
SpecifiesHTTPproxylocationandVRF.
ThenoformofthiscommandremovesaspecifiedHTTPproxylocation.
| Parameter |     | Description                         |
| --------- | --- | ----------------------------------- |
| <FQDN>    |     | SpecifiesFQDNforHTTP proxylocation. |
171
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |
| --------------------------- | ------------------ | --- |

| Parameter   |     |     | Description                               |     |
| ----------- | --- | --- | ----------------------------------------- | --- |
| <IPV4-ADDR> |     |     | SpecifiesIPV4addressforHTTPproxylocation. |     |
| <VRF-NAME>  |     |     | SpecifiesVRF forHTTP proxy.               |     |
AFQDN orIPV4addressareoptionalinthenoformofthecommand.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
DHCPOptions|172

Chapter 8

ND snooping

ND snooping

Overview
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

When RA guard policy is enabled (with ipv6 nd-snooping ra-guard policy), RA packets received on
trusted ports are validated against a set of parameters configured on the policy and assigned to a port
or VLAN.

For more information on RA guard including RA guard policies, see this related video on the Aruba AirHeads

Broadcasting Channel.

Dynamic IPv6 lockdown is performed for ND snooping entries. Based on the DAD NS received from the
hosts by the switch, ND snooping entries are programmed into the IP binding table and the hardware
(as allowed). And ND Binding table entries are added when NA packets are received from hosts.
Therefore, data packets from invalid hosts and transit traffic are blocked.

Statically-configured IP binding information supersedes any information collected dynamically by ND snooping

for the same client.

ND snooping commands

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

173

| clear nd-snooping | binding |     |     |     |
| ----------------- | ------- | --- | --- | --- |
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
vlan <VLAN-ID> SpecifiestheVLANforwhichallNDbindinginformationistobe
cleared.Range:1to4094.
Examples
ClearingallNDbindinginformationfor5000::1vlan1:
| switch(config)# | clear nd-snooping | bindings ipv6 | 5000::1 vlan | 1   |
| --------------- | ----------------- | ------------- | ------------ | --- |
ClearingallNDbindinginformationforport1/1/10:
| switch(config)# | clear nd-snooping | bindings port | 1/1/10 |     |
| --------------- | ----------------- | ------------- | ------ | --- |
ClearingallNDbindinginformationforVLAN10:
| switch(config)# | clear nd-snooping | bindings vlan | 10  |     |
| --------------- | ----------------- | ------------- | --- | --- |
ClearingallNDbindinginformation:
| switch(config)# | clear nd-snooping | bindings all |     |     |
| --------------- | ----------------- | ------------ | --- | --- |
Command History
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
Command Information
NDsnooping|174

| Platforms | Command | context | Authority                                            |     |     |
| --------- | ------- | ------- | ---------------------------------------------------- | --- | --- |
| 6200      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
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
| switch# | clear nd-snooping | ra-guard-policy |     | statistics | vlan 10 |
| ------- | ----------------- | --------------- | --- | ---------- | ------- |
ClearallRAGuardpolicystatisticsforinterface1/1/10
switch# clear nd-snooping ra-guard-policy statistics interface 1/1/10
| Command History     |         |         |                    |     |     |
| ------------------- | ------- | ------- | ------------------ | --- | --- |
| Release             |         |         | Modification       |     |     |
| 10.10               |         |         | Commandintroduced. |     |     |
| Command Information |         |         |                    |     |     |
| Platforms           | Command | context | Authority          |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| clear nd-snooping |            | statistics |     |     |     |
| ----------------- | ---------- | ---------- | --- | --- | --- |
| clear nd-snooping | statistics |            |     |     |     |
Description
ClearsallNDsnoopingstatistics.
175
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

Examples
ClearallNDsnoopingstatistics:
switch#
|                     | clear nd-snooping | statistics |              |
| ------------------- | ----------------- | ---------- | ------------ |
| Command History     |                   |            |              |
| Release             |                   |            | Modification |
| 10.07orearlier      |                   |            | --           |
| Command Information |                   |            |              |
| Platforms           | Command           | context    | Authority    |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
nd-snooping
| nd-snooping    | {enable|disable} |     |     |
| -------------- | ---------------- | --- | --- |
| no nd-snooping | {enable|disable} |     |     |
Description
EnablesordisablesNDsnooping.NDsnoopingisdisabledbydefault.NDsnoopingisnotsupportedon
themanagementinterface.
Examples
EnablingNDsnooping:
| switch(config)# | nd-snooping | enable |     |
| --------------- | ----------- | ------ | --- |
DisablingNDsnooping:
| switch(config)#     | nd-snooping | disable |              |
| ------------------- | ----------- | ------- | ------------ |
| Command History     |             |         |              |
| Release             |             |         | Modification |
| 10.07orearlier      |             |         | --           |
| Command Information |             |         |              |
| Platforms           | Command     | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
NDsnooping|176

| nd-snooping | (in config-vlan |     | context) |
| ----------- | --------------- | --- | -------- |
nd-snooping
no nd-snooping
Description
EnablesNDsnoopingintheconfig-vlancontext.NDsnoopingisdisabledbydefaultforallVLANs.
ThenoformofthecommanddisablesNDsnoopingonthespecifiedVLAN,flushingalltheIPv6bindings
learnedforthisVLANsinceNDsnoopingwasenabledforthisVLAN.
Examples
EnablingNDsnoopingonVLAN100:
| switch(config)#          | vlan | 100         |     |
| ------------------------ | ---- | ----------- | --- |
| switch(config-vlan-100)# |      | nd-snooping |     |
| switch(config-vlan-100)# |      | exit        |     |
switch(config)#
DisablingNDsnoopingonVLAN100:
| switch(config)#          | vlan | 100            |     |
| ------------------------ | ---- | -------------- | --- |
| switch(config-vlan-100)# |      | no nd-snooping |     |
switch(config-vlan-100)#
exit
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | mac-check |     |     |
| -------------- | --------- | --- | --- |
| nd-snooping    | mac-check |     |     |
| no nd-snooping | mac-check |     |     |
Description
ThiscommandenablesverificationofthehardwareaddressfieldinNDsnoopingpackets.When
enabled,theICMPv6targetlinklayeraddressfieldandthesourceMACaddressmustbethesamefor
packetsreceivedonuntrustedportsorelsethepacketsaredropped.ThisNDsnoopingMACverification
isenabledbydefault.
ThenoformofthecommanddisablesNDsnoopingMACverification.
Examples
177
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

EnablingNDsnoopingMACverification:
| switch(config)# |     | nd-snooping |     | mac-check |     |     |
| --------------- | --- | ----------- | --- | --------- | --- | --- |
DisablingNDsnoopingMACverification:
| switch(config)# |             | no  | nd-snooping |     | mac-check    |     |
| --------------- | ----------- | --- | ----------- | --- | ------------ | --- |
| Command         | History     |     |             |     |              |     |
| Release         |             |     |             |     | Modification |     |
| 10.07orearlier  |             |     |             |     | --           |     |
| Command         | Information |     |             |     |              |     |
| Platforms       | Command     |     | context     |     | Authority    |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    |             | prefix-list |             |     |     |     |
| -------------- | ----------- | ----------- | ----------- | --- | --- | --- |
| nd-snooping    | prefix-list |             | <IPV6-ADDR> |     |     |     |
| no nd-snooping | prefix-list |             | <IPV6-ADDR> |     |     |     |
Description
ConfigurestheNDsnoopingprefixlistfortheselectedVLANandthespecifiedIPv6addressprefix.ND
snoopingmustbeenabledbothgloballyandonthisVLANbeforethisprefixlistconfigurationtakes
effect.
ThenoformofthiscommandremovestheprefixlistconfigurationfortheselectedVLANandIPv6
address.
| Parameter   |     |     |     |     | Description              |     |
| ----------- | --- | --- | --- | --- | ------------------------ | --- |
| <IPV6-ADDR> |     |     |     |     | SpecifiestheIPv6address. |     |
Examples
ConfiguringNDsnoopingprefix-listonVLAN1:
| switch(config)#        |     | vlan | 1           |     |             |            |
| ---------------------- | --- | ---- | ----------- | --- | ----------- | ---------- |
| switch(config-vlan-1)# |     |      | nd-snooping |     | prefix-list | 2001::1/64 |
| switch(config-vlan-1)# |     |      | exit        |     |             |            |
switch(config)#
RemoveconfigurationofNDsnoopingprefix-listonVLAN100:
NDsnooping|178

| switch(config)# |     | vlan | 1   |     |     |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- | --- |
switch(config-vlan-1)#
|                        |     |     | no nd-snooping |     | prefix-list |     | 2001::1/64 |
| ---------------------- | --- | --- | -------------- | --- | ----------- | --- | ---------- |
| switch(config-vlan-1)# |     |     | exit           |     |             |     |            |
switch(config)#
| Command        | History     |     |         |     |              |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- |
| Release        |             |     |         |     | Modification |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |
| Command        | Information |     |         |     |              |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |
6200 config-vlan-<VLAN-ID> OperatorsorAdministratorsorlocalusergroupmembers
withexecutionrightsforthiscommand.Operatorscan
executethiscommandfromtheoperatorcontext(>)only.
| nd-snooping    |              | max-bindings |                |     |     |     |     |
| -------------- | ------------ | ------------ | -------------- | --- | --- | --- | --- |
| nd-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |     |     |
| no nd-snooping | max-bindings |              |                |     |     |     |     |
Description
SetsthemaximumnumberofNDbindingsallowedontheselectedinterface.Forallinterfacesonwhich
thiscommandisnotrun,thedefaultmaxbindingsapplies.
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
| switch(config)#    |     | interface | 2/2/1          |     |              |     |     |
| ------------------ | --- | --------- | -------------- | --- | ------------ | --- | --- |
| switch(config-if)# |     |           | no nd-snooping |     | max-bindings |     |     |
switch(config-if)#
exit
switch(config)#
| Command | History |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
179
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

| Release             |         |         |     | Modification |     |
| ------------------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier      |         |         |     | --           |     |
| Command Information |         |         |     |              |     |
| Platforms           | Command | context |     | Authority    |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | nd-guard |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- |
| nd-snooping    | nd-guard |     |     |     |     |
| no nd-snooping | nd-guard |     |     |     |     |
Description
ThiscommandenablesNDguardontheselectedVLAN.
ThenoformofthecommanddisablesNDguardanddeletesalltheIPv6bindingslearnedontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
Examples
EnablingNDsnoopingNDguardonVLAN100:
| switch(config)# | nd-snooping |     | enable |     |     |
| --------------- | ----------- | --- | ------ | --- | --- |
switch(config)#
|                          | vlan | 100 |             |     |          |
| ------------------------ | ---- | --- | ----------- | --- | -------- |
| switch(config-vlan-100)# |      |     | nd-snooping |     | nd-guard |
| switch(config-vlan-100)# |      |     | exit        |     |          |
switch(config)#
DisablingNDsnoopingNDguardonVLAN100:
| switch(config)#          | vlan | 100 |                |     |          |
| ------------------------ | ---- | --- | -------------- | --- | -------- |
| switch(config-vlan-100)# |      |     | no nd-snooping |     | nd-guard |
| switch(config-vlan-100)# |      |     | exit           |     |          |
switch(config)#
| Command History     |     |     |     |              |     |
| ------------------- | --- | --- | --- | ------------ | --- |
| Release             |     |     |     | Modification |     |
| 10.07orearlier      |     |     |     | --           |     |
| Command Information |     |     |     |              |     |
NDsnooping|180

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| nd-snooping    | ra-guard       |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| nd-snooping    | ra-guard [log] |     |     |     |
| no nd-snooping | ra-guard       |     |     |     |
Description
ThiscommandenablesRoutingAdvertisement(RA)guardontheselectedVLAN.Whenenabled,ingress
RoutingAdvertisement(RA)andRoutingRedirect(RR)packetsontheselectedVLANareblockedon
untrustedports.Thepacketsareforwardedwhenreceivedontrustedports.
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
| switch(config)# | vlan | 100 |     |     |
| --------------- | ---- | --- | --- | --- |
switch(config-vlan-100)#
|                          |     |     | no nd-snooping | ra-guard |
| ------------------------ | --- | --- | -------------- | -------- |
| switch(config-vlan-100)# |     |     | exit           |          |
switch(config)#
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
181
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
6200 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
switch(config)#
|                          | nd-snooping |     | enable      | vlan 100 |
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
| Command History     |     |     |     |              |
| ------------------- | --- | --- | --- | ------------ |
| Release             |     |     |     | Modification |
| 10.07orearlier      |     |     |     | --           |
| Command Information |     |     |     |              |
NDsnooping|182

| Platforms | Command | context |     |     | Authority |
| --------- | ------- | ------- | --- | --- | --------- |
6200 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| nd-snooping    | trust |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- |
| nd-snooping    | trust |     |     |     |     |
| no nd-snooping | trust |     |     |     |     |
Description
EnablesNDsnoopingtrustontheselectedinterface(port).Onlyserverpacketsreceivedontrusted
portsareforwarded.Alltheportsareuntrustedbydefault.
ThenoformofthecommanddisablesNDsnoopingtrustontheselectedport.
Examples
EnablingNDsnoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface   | 2/2/1 |       |     |
| ------------------ | --- | ----------- | ----- | ----- | --- |
| switch(config-if)# |     | nd-snooping |       | trust |     |
| switch(config-if)# |     | exit        |       |       |     |
switch(config)#
DisablingNDsnoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface      | 2/2/1 |     |       |
| ------------------ | --- | -------------- | ----- | --- | ----- |
| switch(config-if)# |     | no nd-snooping |       |     | trust |
| switch(config-if)# |     | exit           |       |     |       |
switch(config)#
| Command History     |         |         |     |     |              |
| ------------------- | ------- | ------- | --- | --- | ------------ |
| Release             |         |         |     |     | Modification |
| 10.07orearlier      |         |         |     |     | --           |
| Command Information |         |         |     |     |              |
| Platforms           | Command | context |     |     | Authority    |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show nd-snooping
| show nd-snooping | [vlan | <VLAN-ID>] |     |     |     |
| ---------------- | ----- | ---------- | --- | --- | --- |
Description
ShowseitherallNDsnoopingconfigurationortheconfigurationforthespecifiedVLAN.
183
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vlan <VLAN-ID> SpecifiestheVLANforwhichtheNDconfigurationistobeshown.
Range:1to4094.
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
| ND Snooping         |               | : Enabled  |                   |     |
| ------------------- | ------------- | ---------- | ----------------- | --- |
| MAC Address         | Check         | : Disabled |                   |     |
| Trusted Port        | Bindings      | : Enabled  |                   |     |
| ND Guard            |               | : Enabled  |                   |     |
| RA Guard            |               | : Disabled |                   |     |
| RA Drop             |               | : Disabled |                   |     |
| PORT TRUST          | MAX-BINDINGS  |            | CURRENT-BINDINGS  |     |
| ------- ------      | ------------- |            | ----------------- |     |
| 1/1/1 Yes           |               |            |                   |     |
| 1/1/2 Yes           |               |            |                   |     |
| 1/1/3 No            | 100           |            | 10                |     |
| Command History     |               |            |                   |     |
| Release             |               |            | Modification      |     |
| 10.07orearlier      |               |            | --                |     |
| Command Information |               |            |                   |     |
NDsnooping|184

| Platforms | Command | context | Authority                                            |     |     |
| --------- | ------- | ------- | ---------------------------------------------------- | --- | --- |
| 6200      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show nd-snooping |          | binding |     |     |     |
| ---------------- | -------- | ------- | --- | --- | --- |
| show nd-snooping | bindings |         |     |     |     |
Description
ShowstheNDsnoopingbindingconfiguration.
Examples
ShowingtheNDsnoopingbindingconfiguration:
| switch# | show nd-snooping | binding |     |             |            |
| ------- | ---------------- | ------- | --- | ----------- | ---------- |
| PORT    | IPV6-ADDRESS     |         |     | MAC-ADDRESS | VLAN TIME- |
LEFT STATE
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
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show nd-snooping |             | prefix-list |     |     |     |
| ---------------- | ----------- | ----------- | --- | --- | --- |
| show nd-snooping | prefix-list |             |     |     |     |
Description
ShowstheNDsnoopingprefixlistinformation.
Examples
ShowingtheNDsnoopingprefixlistinformation:
185
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| switch#             | show nd-snooping                            | prefix-list |           |              |          |     |     |
| ------------------- | ------------------------------------------- | ----------- | --------- | ------------ | -------- | --- | --- |
| VLAN                | IPV6-ADDRESS-PREFIX                         |             |           |              | SOURCE   |     |     |
| -----               | ------------------------------------------- |             |           |              | -------- |     |     |
| 1                   | 2001::/64                                   |             |           |              | Static   |     |     |
| 4094                | 3001::/64                                   |             |           |              | Dynamic  |     |     |
| Command History     |                                             |             |           |              |          |     |     |
| Release             |                                             |             |           | Modification |          |     |     |
| 10.07orearlier      |                                             |             |           | --           |          |     |     |
| Command Information |                                             |             |           |              |          |     |     |
| Platforms           | Command                                     | context     | Authority |              |          |     |     |
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
(Appliestothe6200,6300,6400,8360.)ShowingglobalNDsnoopingstatistics:
| switch(config)# | show   | nd-snooping | statistics |     |     |     |       |
| --------------- | ------ | ----------- | ---------- | --- | --- | --- | ----- |
| PACKET-TYPE     | ACTION | REASON      |            |     |     |     | COUNT |
------------ -------- ----------------------------------------------- --------
| RA              | forward | RA packets | received     | on trusted     | port       |        | 20  |
| --------------- | ------- | ---------- | ------------ | -------------- | ---------- | ------ | --- |
| RA              | drop    | RA packets | received     | on untrusted   | port       |        | 45  |
| NS              | forward | NS packets | received     | on trusted     | port       |        | 52  |
| NS              | forward | NS packets | received     | on untrusted   | port       |        | 95  |
| NS              | drop    | NS packets | failed       | MAC check      |            |        | 14  |
| NS              | drop    | NS packets | failed       | Prefix check   |            |        | 12  |
| NS              | drop    | NS packets | failed       | on max-binding | limit      |        | 0   |
| NS              | drop    | NS packets | failed       | ND snooping    | validation | checks | 20  |
| NA              | forward | NA packets | received     | on trusted     | port       |        | 17  |
| NA              | forward | NA packets | received     | on untrusted   | port       |        | 30  |
| NA              | drop    | NA packets | failed       | Prefix check   |            |        | 15  |
| NA              | drop    | NA packets | failed       | on max-binding | limit      |        | 2   |
| NA              | drop    | NA packets | failed       | ND snooping    | validation | checks | 5   |
| Command History |         |            |              |                |            |        |     |
| Release         |         |            | Modification |                |            |        |     |
| 10.07orearlier  |         |            | --           |                |            |        |     |
NDsnooping|186

| Command   | Information |         |         |           |     |     |
| --------- | ----------- | ------- | ------- | --------- | --- | --- |
| Platforms |             | Command | context | Authority |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| RA guard |     | policy | commands |     |     |     |
| -------- | --- | ------ | -------- | --- | --- | --- |
hop limit
| hop limit | [minimum |          | | maximum] <HOP-LIMIT> |             |     |     |
| --------- | -------- | -------- | ---------------------- | ----------- | --- | --- |
| no hop    | limit    | [minimum | | maximum]             | <HOP-LIMIT> |     |     |
Description
EnablesverificationoftheadvertisedhopcountlimitiftheRAguardpolicyisappliedonaVLANor
interface.RApacketswiththehoplimitwithinthespecifiedminimumandmaximumvaluesare
processed.Ifnoneofthevaluesarespecifiedforhoplimit,thedefaultrangeis1-255.Ifhoplimitisnot
enabled,packetsarenotvalidatedforhoplimit.
ThenoformofthecommanddisablesthehoplimitonthespecifiedRAguardpolicy.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter   |     |     |     | Description                             |     |     |
| ----------- | --- | --- | --- | --------------------------------------- | --- | --- |
| <HOP-LIMIT> |     |     |     | Specifiesthehop-limitvalue.Range:1-255. |     |     |
minimum Specifiestheminimumvalueforthehop-limitrange.Default:1,
Range1-255.
Therangeisminimum–255ifonlyaminimumvalueisspecified.
maximum Specifiesthemaximumvalueforthehop-limitrange.Default:
255,Range1-255.
Therangeis1–maximumifonlyamaximumvalueisspecified.
Examples
EnablingthehoplimitontheRAguardpolicyandaddingminimumandmaximumvaluesforhoplimit
onthepolicy:
| switch(config)#                |     |     | ipv6 nd-snooping | ra-guard  | policy  | <POLICY-NAME> |
| ------------------------------ | --- | --- | ---------------- | --------- | ------- | ------------- |
| switch(config-raguard-policy)# |     |     |                  | hop-limit | enable  |               |
| switch(config-raguard-policy)# |     |     |                  | hop-limit | maximum | 150           |
| switch(config-raguard-policy)# |     |     |                  | hop-limit | minimum | 50            |
DisablingthehoplimitontheRAguardpolicy:
| switch(config)#                |     |     | ipv6 nd-snooping | ra-guard     | policy | <POLICY-NAME> |
| ------------------------------ | --- | --- | ---------------- | ------------ | ------ | ------------- |
| switch(config-raguard-policy)# |     |     |                  | no hop-limit | enable |               |
187
| AOS-CX10.11IPServicesGuide| |     |     | (6200SwitchSeries) |     |     |     |
| --------------------------- | --- | --- | ------------------ | --- | --- | --- |

RemovingminimumandmaximumvaluesforthehoplimitontheRAguardpolicy:
| switch(config)#                |         | ipv6 nd-snooping | ra-guard |                    | policy <POLICY-NAME> |
| ------------------------------ | ------- | ---------------- | -------- | ------------------ | -------------------- |
| switch(config-raguard-policy)# |         |                  | no       | hop-limit          | maximum 150          |
| switch(config-raguard-policy)# |         |                  | no       | hop-limit          | minimum 50           |
| switch(config-raguard-policy)# |         |                  | no       | hop-limit          | maximum              |
| switch(config-raguard-policy)# |         |                  | no       | hop-limit          | minimum              |
| Command History                |         |                  |          |                    |                      |
| Release                        |         |                  |          | Modification       |                      |
| 10.10                          |         |                  |          | Commandintroduced. |                      |
| Command Information            |         |                  |          |                    |                      |
| Platforms                      | Command | context          |          | Authority          |                      |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd-snooping    |          | ra-guard        | policy        |     |     |
| ------------------- | -------- | --------------- | ------------- | --- | --- |
| ipv6 nd-snooping    | ra-guard | policy          | <POLICY-NAME> |     |     |
| no ipv6 nd-snooping |          | ra-guard policy | <POLICY-NAME> |     |     |
Description
CreatestheRouterAdvertisement(RA)guardpolicywiththegivennameandenterstheRAguardpolicy
configurationcontext.
ThenoformofthecommandremovesthespecifiedRAguardpolicyfromtheswitch.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<POLICY-NAME> SpecifiesthenameoftheRAguardpolicy.Maximumlength:64.
Examples
CreatingtheRAguardpolicygloballywithaspecifiedname:
| switch(config)# |     | ipv6 nd-snooping | ra-guard |     | policy <POLICY-NAME> |
| --------------- | --- | ---------------- | -------- | --- | -------------------- |
switch(config-raguard-policy)#
DeletingthespecifiedRAguardpolicy:
switch(config)# no ipv6 nd-snooping ra-guard policy <POLICY-NAME>
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
NDsnooping|188

| Release             |         |         | Modification       |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| 10.10               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
managed-config-flag
| managed-config-flag    | [on | | off]     |     |     |
| ---------------------- | --- | ---------- | --- | --- |
| no managed-config-flag |     | [on | off] |     |     |
Description
Enablestheverificationoftheadvertisedmanageconfigurationflag.Verifiesthattheadvertised
managedaddressconfigurationflagisOnorOffbasedontheconfiguredvalue.
Thenoformofthecommanddisablesthemanageconfigurationflagverification.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
on Verifiesthattheadvertisedmanagedaddressconfigurationflagis
On.
off
Verifiesthattheadvertisedmanagedaddressconfigurationflagis
Off.
Examples
Enablingmanagedconfigurationflagverification:
| switch(config)#                | ipv6 | nd-snooping | ra-guard policy     | <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | ------------------- | ------------- |
| switch(config-raguard-policy)# |      |             | managed-config-flag | off           |
| switch(config-raguard-policy)# |      |             | managed-config-flag | on            |
Disablingmanagedconfigurationflagverification:
| switch(config)#                | ipv6 | nd-snooping | ra-guard policy        | <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | ---------------------- | ------------- |
| switch(config-raguard-policy)# |      |             | no managed-config-flag |               |
| switch(config-raguard-policy)# |      |             | no managed-config-flag | off           |
| switch(config-raguard-policy)# |      |             | no managed-config-flag | on            |
| Command History                |      |             |                        |               |
189
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Release             |         |         | Modification       |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| 10.10               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| match access-list    |            |     |     |     |
| -------------------- | ---------- | --- | --- | --- |
| match access-list    | <ACL-NAME> |     |     |     |
| no match access-list | <ACL-NAME> |     |     |     |
Description
ConfigurestheaccesslisttoanRAguardpolicy.Theaccesslisthastobecreatedwiththedesiredmatch
criteriabeforeaddingitintoRAguardpolicy.Advertisedpacketsareverifiedforthematchcriteriawhen
anRAguardpolicywithmatchedaccesslistisenabledonatrustedportorVLANs.
ThenoformofthecommandremovestheaccesslistfromtheRAguardpolicy.
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
| Command History     |     |     |                    |     |
| ------------------- | --- | --- | ------------------ | --- |
| Release             |     |     | Modification       |     |
| 10.10               |     |     | Commandintroduced. |     |
| Command Information |     |     |                    |     |
NDsnooping|190

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| match prefix-list    |                    |     |     |     |
| -------------------- | ------------------ | --- | --- | --- |
| match prefix-list    | <PREFIX-LIST-NAME> |     |     |     |
| no match prefix-list | <PREFIX-LIST-NAME> |     |     |     |
Description
Configuresaprefix-listfortheRAguardpolicy.AdvertisedprefixesinRApacketsarecomparedagainst
theconfiguredprefix-listandifthereisnomatch,theRApacketsaredropped.IftheRAprefixlistisnot
configured,thischeckisnotperformed.
ThenoformofthecommandremovestheprefixlistfromtheRAguardpolicy.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<PREFIX-LIST-NAME> Specifiesthenameoftheprefixlisttobematched.
Examples
AddingaprefixlistnamedPREFIX_LIST_EXAMPLEtothePOLICY1RAguardpolicy:
| switch(config)# | ipv6 | nd-snooping | ra-guard policy | POLICY1 |
| --------------- | ---- | ----------- | --------------- | ------- |
switch(config-raguard-policy)# match prefix-list PREFIX_LIST_EXAMPLE
DeletingtheprefixlistnamedPREFIX_LIST_EXAMPLEfromthePOLICY1RAguardpolicy:
switch(config)#
|     | ipv6 | nd-snooping | ra-guard policy | POLICY1 |
| --- | ---- | ----------- | --------------- | ------- |
switch(config-raguard-policy)# no match pefix-list PREFIX_LIST_EXAMPLE
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.10               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| nd-snooping | ra-guard | attach-policy |     |     |
| ----------- | -------- | ------------- | --- | --- |
191
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| nd-snooping    | ra-guard | attach-policy |     | <POLICY-NAME> |
| -------------- | -------- | ------------- | --- | ------------- |
| no nd-snooping | ra-guard | attach-policy |     | <POLICY-NAME> |
Description
AppliesthecreatedRAguardpolicytoaspecificL2portorVLAN.
ThenoformofthecommanddetachesthespecifiedRAguardpolicyfromtheL2portorVLAN.
| Parameter     |     |     |     | Description                         |
| ------------- | --- | --- | --- | ----------------------------------- |
| <POLICY-NAME> |     |     |     | SpecifiesthenameoftheRAguardpolicy. |
Usage
Intheinterfaceconfiguration(config-if)context:
n RAguardmustbeenabledonmemberVLANsoftheportforwhichRApacketsneedtobeinspected
usingthepolicy.
Intheinterfaceconfiguration(config-if)andVLANconfiguration(config-vlan)contexts:
n RA packetsreceivedonuntrustedportsaredroppedwithoutanyinspection.
n RA packetsreceivedontrustedportsarevalidatedagainstthepolicy.
n TheappliedpolicytakeseffectonlyifNDsnoopingisenabledgloballyandbothND snoopingandRA
guardareenabledundertheVLANcontext.
PolicyprecedencebetweenVLANandport:
n IfthepolicyisattachedtobothVLANandport,theportpolicytakesprecedenceovertheVLAN
policy.
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
| switch(config-if)# |     | no routing  |     |       |
| ------------------ | --- | ----------- | --- | ----- |
| switch(config-if)# |     | nd-snooping |     | trust |
switch(config-if)# nd-snooping ra-guard attach-policy POLICY_NAME
switch(config-if)#6300(config-if)# nd-snooping ra-guard attach-policy POLICY_NOT_
NDsnooping|192

CREATED
| RA guard           | policy  | does      | not         | exist.   |               |     |
| ------------------ | ------- | --------- | ----------- | -------- | ------------- | --- |
| Do you             | want to | create    | (y/n)?      |          |               |     |
| switch(config)#    |         | interface |             | 1/1/10   |               |     |
| switch(config-if)# |         |           | nd-snooping | ra-guard | attach-policy | AA  |
RA Guard policy is ineffective, as 1/1/10 is configured as untrusted port.
AttachingtheRAguardpolicytoaVLAN:
| switch(config)# |     | vlan | 10  |     |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- |
switch(config-vlan-10)# nd-snooping ra-guard attach-policy POLICY_NAME
DetachingtheRAguardpolicy:
| switch(config)# |     | interface |     | 1/1/10 |     |     |
| --------------- | --- | --------- | --- | ------ | --- | --- |
switch(config-if)# no nd-snooping ra-guard attach-policy POLICY_NAME
AttemptingtodetachaRAguardpolicywhichisnotappliedontheportorVLAN:
| switch(config)# |     | interface |     | 1/1/10 |     |     |
| --------------- | --- | --------- | --- | ------ | --- | --- |
switch(config-if)# no nd-snooping ra-guard attach-policy POLICY_NAME
| RA Guard | Policy | POLICY_NAME |     | is not | applied on this | port. |
| -------- | ------ | ----------- | --- | ------ | --------------- | ----- |
Attemptingtodetachanon-existentRAguardpolicy:
switch(config-if)# no nd-snooping ra-guard attach-policy POLICY_NOT_CREATED
| Could not | find        | the | policy  | POLICY_NOT_CREATED. |                    |     |
| --------- | ----------- | --- | ------- | ------------------- | ------------------ | --- |
| Command   | History     |     |         |                     |                    |     |
| Release   |             |     |         |                     | Modification       |     |
| 10.10     |             |     |         |                     | Commandintroduced. |     |
| Command   | Information |     |         |                     |                    |     |
| Platforms | Command     |     | context |                     | Authority          |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-vlan-<VLAN-ID> |     |     |     | rightsforthiscommand. |     |
| --- | --------------------- | --- | --- | --- | --------------------- | --- |
other-config-flag
| other-config-flag    |     | [on | | off] |     |     |     |
| -------------------- | --- | --- | ------ | --- | --- | --- |
| no other-config-flag |     | [on | | off] |     |     |     |
Description
Enablestheverificationoftheadvertisedotherconfigurationflag.VerifiesthattheadvertisedOther
StatefulConfigurationflagisOnorOffbasedontheconfiguredvalue.
193
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

Thenoformofthecommanddisablesotherconfigurationflagverification.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
on
VerifiesthattheadvertisedOtherStatefulConfigurationflagisOn.
off VerifiesthattheadvertisedOtherStatefulConfigurationflagis
Off.
Examples
Enablingotherconfigurationflagverification:
| switch(config)#                |     | ipv6 nd-snooping | ra-guard          | policy | <POLICY-NAME> |
| ------------------------------ | --- | ---------------- | ----------------- | ------ | ------------- |
| switch(config-raguard-policy)# |     |                  | other-config-flag |        | off           |
| switch(config-raguard-policy)# |     |                  | other-config-flag |        | on            |
Disablingotherconfigurationflagverification:
| switch(config)#                |         | ipv6 nd-snooping | ra-guard | policy             | <POLICY-NAME> |
| ------------------------------ | ------- | ---------------- | -------- | ------------------ | ------------- |
| switch(config-raguard-policy)# |         |                  | no       | other-config-flag  |               |
| switch(config-raguard-policy)# |         |                  | no       | other-config-flag  | off           |
| switch(config-raguard-policy)# |         |                  | no       | other-config-flag  | on            |
| Command History                |         |                  |          |                    |               |
| Release                        |         |                  |          | Modification       |               |
| 10.10                          |         |                  |          | Commandintroduced. |               |
| Command Information            |         |                  |          |                    |               |
| Platforms                      | Command | context          |          | Authority          |               |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
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
NDsnooping|194

| Parameter |     |     | Description                             |     |
| --------- | --- | --- | --------------------------------------- | --- |
| high      |     |     | Setsthemaximumrouterpreferencetohigh.   |     |
| medium    |     |     | Setsthemaximumrouterpreferencetomedium. |     |
| low       |     |     | Setsthemaximumrouterpreferencetolow.    |     |
Examples
Enablingrouterpreferenceverificationwiththemaximumrouterpreferencesettohigh:
| switch(config)#                | ipv6 | nd-snooping | ra-guard policy   | <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | ----------------- | ------------- |
| switch(config-raguard-policy)# |      |             | router-preference | high          |
Disablingrouterpreferenceverification:
| switch(config)#                | ipv6    | nd-snooping | ra-guard policy      | <POLICY-NAME> |
| ------------------------------ | ------- | ----------- | -------------------- | ------------- |
| switch(config-raguard-policy)# |         |             | no router-preference |               |
| Command History                |         |             |                      |               |
| Release                        |         |             | Modification         |               |
| 10.10orearlier                 |         |             | Commandintroduced.   |               |
| Command Information            |         |             |                      |               |
| Platforms                      | Command | context     | Authority            |               |
config-raguard-policy
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| show nd-snooping |          | ra-guard  | interface      |     |
| ---------------- | -------- | --------- | -------------- | --- |
| show nd-snooping | ra-guard | interface | <INTERFACE-ID> |     |
Description
ShowsRAguardcountersforthespecifiedinterface.CountersareclearedoncetheRAguardpolicyis
detachedfromtheinterface.
Parameter Description
<INTERFACE-ID> SpecifiestheinterfaceforwhichtheRAguardcountersare
displayed.
Examples
ShowingRAguardcountersforinterface1/1/1:
195
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

|     | switch#  | show nd-snooping |          | ra-guard | interface | 1/1/1 |     |     |
| --- | -------- | ---------------- | -------- | -------- | --------- | ----- | --- | --- |
|     | RA Guard | Policy           | Counters |          |           |       |     |     |
========================
|           | RA Guard    | Policy    | Applied |         | : POLICY_2         |                     |     |     |
| --------- | ----------- | --------- | ------- | ------- | ------------------ | ------------------- | --- | --- |
|           | RA Packets  | Received  |         |         | : 10               |                     |     |     |
|           | RA Packets  | Forwarded |         |         | : 5                |                     |     |     |
|           | RA Packets  | Dropped   |         |         | : 5 [Total]        |                     |     |     |
|           |             |           |         | reason  | : Managed          | flag error          | [0] |     |
|           |             |           |         |         | Other              | flag error          | [0] |     |
|           |             |           |         |         | Access             | list error          | [0] |     |
|           |             |           |         |         | Prefix             | list error          | [0] |     |
|           |             |           |         |         | Router             | preference error[0] |     |     |
|           |             |           |         |         | Hop limit          | error               | [5] |     |
| Command   | History     |           |         |         |                    |                     |     |     |
| Release   |             |           |         |         | Modification       |                     |     |     |
| 10.10     |             |           |         |         | Commandintroduced. |                     |     |     |
| Command   | Information |           |         |         |                    |                     |     |     |
| Platforms |             | Command   |         | context | Authority          |                     |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | nd-snooping |          | ra-guard |        | policy          |     |     |     |
| ---- | ----------- | -------- | -------- | ------ | --------------- | --- | --- | --- |
| show | nd-snooping | ra-guard |          | policy | [<POLICY-NAME>] |     |     |     |
Description
ShowstheRAguardpolicyconfiguration.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
<POLICY-NAME> SpecifiesthenameoftheRAguardpolicytobedisplayed.
Examples
ShowingRAguardconfiguration:
|     | switch#  | show nd-snooping |     | ra-guard | policy  |       |     |               |
| --- | -------- | ---------------- | --- | -------- | ------- | ----- | --- | ------------- |
|     | RA Guard | Policy           |     |          | Applied | Ports |     | Applied VLANs |
----------------------------------------------------------------------------------
--------
|     | POLICY_NAME1 |     | 1/1/25,1/1/27,1/1/29-1/1/44,1/1/46 |     |     |     |     | 10,20,50-100 |
| --- | ------------ | --- | ---------------------------------- | --- | --- | --- | --- | ------------ |
|     | POLICY_NAME2 |     | 1/1/1-1/1/24                       |     |     |     |     |              |
NDsnooping|196

|     | switch#  | show nd-snooping |             | ra-guard | policy | POLICY_NAME1 |
| --- | -------- | ---------------- | ----------- | -------- | ------ | ------------ |
|     | RA Guard | policy           | Information |          |        |              |
========================
|           | Policy name       |             |     | : POLICY_NAME1                       |                    |     |
| --------- | ----------------- | ----------- | --- | ------------------------------------ | ------------------ | --- |
|           | Policy Applied    | Ports       |     | : 1/1/25,1/1/27,1/1/29-1/1/44,1/1/46 |                    |     |
|           | Policy Applied    | VLANs       |     | : 10,20,50-100                       |                    |     |
|           | Hop Limit         |             |     | : enabled                            |                    |     |
|           | minimum           |             |     | : 50                                 |                    |     |
|           | maximum           |             |     | : 150                                |                    |     |
|           | Managed           | config flag |     | : On                                 |                    |     |
|           | Other config      | flag        |     | : On                                 |                    |     |
|           | Access List       |             |     | : ACL1                               |                    |     |
|           | Prefix List       |             |     | : PREFIX_LIST_NAME                   |                    |     |
|           | Router Preference |             |     | : high                               |                    |     |
| Command   | History           |             |     |                                      |                    |     |
| Release   |                   |             |     |                                      | Modification       |     |
| 10.10     |                   |             |     |                                      | Commandintroduced. |     |
| Command   | Information       |             |     |                                      |                    |     |
| Platforms |                   | Command     |     | context                              | Authority          |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | nd-snooping |          |     | ra-guard        | vlan |     |
| ---- | ----------- | -------- | --- | --------------- | ---- | --- |
| show | nd-snooping | ra-guard |     | vlan <VLAN-ID>] |      |     |
Description
ShowsRAguardcountersforthespecifiedVLAN.CountersareclearedoncetheRAguardpolicyis
detachedfromtheVLAN.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<VLAN-ID> SpecifiesaVLANIDforwhichtheRAguardcountersaredisplayed.
Range:1to4094.
Examples
ShowingRAguardcountersforVLAN2:
|     | switch#  | show nd-snooping |          | ra-guard | vlan | 2   |
| --- | -------- | ---------------- | -------- | -------- | ---- | --- |
|     | RA Guard | Policy           | Counters |          |      |     |
========================
|     | RA Guard | Policy | Applied |     | : POLICY_1 |     |
| --- | -------- | ------ | ------- | --- | ---------- | --- |
197
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

| RA Packets          | Received  |         | : 20               |                     |     |
| ------------------- | --------- | ------- | ------------------ | ------------------- | --- |
| RA Packets          | Forwarded |         | : 5                |                     |     |
| RA Packets          | Dropped   |         | : 15 [Total]       |                     |     |
|                     |           | reason  | : Managed          | flag error          | [1] |
|                     |           |         | Other              | flag error          | [4] |
|                     |           |         | Access             | list error          | [1] |
|                     |           |         | Prefix             | list error          | [4] |
|                     |           |         | Router             | preference error[0] |     |
|                     |           |         | Hop limit          | error               | [5] |
| Command History     |           |         |                    |                     |     |
| Release             |           |         | Modification       |                     |     |
| 10.10               |           |         | Commandintroduced. |                     |     |
| Command Information |           |         |                    |                     |     |
| Platforms           | Command   | context | Authority          |                     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
NDsnooping|198

Chapter 9
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
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
199
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- |

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
| switch(config)#         | vlan | 10                     |     |     |
| ----------------------- | ---- | ---------------------- | --- | --- |
| switch(config-vlan-10)# |      | ipv6 destination-guard |     |     |
DisablingIPv6destinationguardpolicyonaVLAN:
| switch(config-vlan-10)# |             | no ipv6 | destination-guard  |     |
| ----------------------- | ----------- | ------- | ------------------ | --- |
| Command                 | History     |         |                    |     |
| Release                 |             |         | Modification       |     |
| 10.10                   |             |         | Commandintroduced. |     |
| Command                 | Information |         |                    |     |
| Platforms               | Command     | context | Authority          |     |
6200 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
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
| switch# | show ipv6   | destination-guard | statistics | vlan 10 |
| ------- | ----------- | ----------------- | ---------- | ------- |
| Packets | dropped for | VLAN 10 : 25467   |            |         |
ShowingIPv6destination-guardstatisticsforallVLANs:
| switch#             | show ipv6   | destination-guard | statistics         |     |
| ------------------- | ----------- | ----------------- | ------------------ | --- |
| Packets             | dropped for | VLAN 10 : 25467   |                    |     |
| Packets             | dropped for | VLAN 30 : 434     |                    |     |
| Packets             | dropped for | VLAN 50 : 8767    |                    |     |
| Command History     |             |                   |                    |     |
| Release             |             |                   | Modification       |     |
| 10.10               |             |                   | Commandintroduced. |     |
| Command Information |             |                   |                    |     |
| Platforms           | Command     | context           | Authority          |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
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
| switch#                | show ipv6 | destination-guard |                    |     |
| ---------------------- | --------- | ----------------- | ------------------ | --- |
| IPv6 Destination-Guard |           | information       |                    |     |
| Enabled                | VLANs     | : 10,20,31-35     |                    |     |
| Command History        |           |                   |                    |     |
| Release                |           |                   | Modification       |     |
| 10.10                  |           |                   | Commandintroduced. |     |
| Command Information    |           |                   |                    |     |
201
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Platforms | Command | context | Authority                                            |
| --------- | ------- | ------- | ---------------------------------------------------- |
| 6200      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
IPv6destinationguard|202

Chapter 10

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

IP tunnels supported features

n Up to 127 tunnels can be defined on a switch shared between different tunnel types.

Unsupported features

n Key support can be added for security and identification purposes when there are multiple

applications.

n VPN across public IP network.

Configuring an IP tunnel

Prerequisites

An enabled layer 3 interface with an IP address assigned to it, created with the command interface.

Procedure

1. Create an IP tunnel with the command interface tunnel .

2. Set the IP address for the tunnel. For an IPv6 in IPv4 or an IPv6 in IPv6 tunnel, enter the command

ipv6 address.

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

203

3. SetthesourceIPaddressforthetunnel.ForanIPv6inIPv4tunnel,enterthecommandsource
ip.ForanIPv6inIPv6tunnel,enterthecommandsource ipv6.
4. SetthedestinationIPaddressforthetunnel.ForanIPv6inIPv4tunnel,enterthecommand
destination ip.ForanIPv6inIPv6tunnel,enterthecommanddestination ipv6.
5. Optionally,settheTTL(hopcount)forthetunnelwiththecommandttl.
6. Optionally,settheMTUforthetunnelwiththecommandip mtu.
7. Optionally,addadescriptiontothetunnelwiththecommanddescription.
| 8.  | Enablethetunnelwiththecommandno |     |     |     | shutdown. |     |     |
| --- | ------------------------------- | --- | --- | --- | --------- | --- | --- |
9. Reviewtunnelsettingswiththecommandshow tunnel.
interface
| Creating | an IPv6 | in  | IPv4 | tunnel |     | for traversing | a public |
| -------- | ------- | --- | ---- | ------ | --- | -------------- | -------- |
network
ThisexamplecreatesanIPv6inIPv4tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
Procedure
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
|     | switch(config)#       | interface |             | tunnel  | 10          | mode ip 6in4   |     |
| --- | --------------------- | --------- | ----------- | ------- | ----------- | -------------- | --- |
|     | switch(config-ip-if)# |           | ipv6        | address |             | 2001:DB8::1/62 |     |
|     | switch(config-ip-if)# |           | source      |         | ip 10.1.1.1 |                |     |
|     | switch(config-ip-if)# |           | destination |         |             | ip 20.1.1.1    |     |
IPTunnels |204

|     | switch(config-ip-if)# |     | no   | shutdown |     |     |     |
| --- | --------------------- | --- | ---- | -------- | --- | --- | --- |
|     | switch(config-ip-if)# |     | exit |          |     |     |     |
d. Definesroutessothattrafficfromnetwork1canreachnetwork2throughthetunnel.
|     | switch(config)# | ip   | route | 20.1.1.0/24 |     | 10.1.1.2 |     |
| --- | --------------- | ---- | ----- | ----------- | --- | -------- | --- |
|     | switch(config)# | ipv6 | route | 290::0/64   |     | tunnel10 |     |
2. Onswitch2:
|     | a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit. |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
switch# config
|     | switch(config)#    | interface |            | 1/1/1 |             |     |     |
| --- | ------------------ | --------- | ---------- | ----- | ----------- | --- | --- |
|     | switch(config-if)# |           | ip address |       | 20.1.1.1/24 |     |     |
switch(config-if)#
no shutdown
|     | b. Enableinterface1/1/2andassigntheIPaddress2090::2/64toit. |           |             |         |            |     |     |
| --- | ----------------------------------------------------------- | --------- | ----------- | ------- | ---------- | --- | --- |
|     | switch(config)#                                             | interface |             | 1/1/2   |            |     |     |
|     | switch(config-if)#                                          |           | ipv6        | address | 2090::2/64 |     |     |
|     | switch(config-if)#                                          |           | no shutdown |         |            |     |     |
|     | switch(config-if)#                                          |           | exit        |         |            |     |     |
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
switch(config)#
|          |                 | ip  | route | 10.1.1.0/24 |     | 20.1.1.2       |          |
| -------- | --------------- | --- | ----- | ----------- | --- | -------------- | -------- |
|          | switch(config)# | ip  | route | 2080::0/64  |     | tunnel10       |          |
| Creating | an IPv6         | in  | IPv6  | tunnel      |     | for traversing | a public |
network
ThisexamplecreatesanIPv6inIPv6tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
Procedure
205
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- | --- |

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
IPTunnels |206

AssociatesatextdescriptionwithanIPtunnelforidentificationpurposes.
ThenoformofthiscommandremovesthedescriptionfromanIPtunnel.
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
switch(config)#
|                       | interface | tunnel      | 8 mode  | ip 6in6    |
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
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| destination    | ip             |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| destination    | ip <IPV4-ADDR> |     |     |     |
| no destination | ip <IPV4-ADDR> |     |     |     |
Description
207
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

SetsthedestinationIPaddressforanIPtunnel.Specifytheaddressoftheinterfaceontheremote
devicetowhichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPaddressfromanIPtunnel.
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
| switch(config)# | interface | tunnel | 27  |
| --------------- | --------- | ------ | --- |
switch(config-ip-if)#
|                     |         | no destination | ip 10.10.20.1 |
| ------------------- | ------- | -------------- | ------------- |
| Command History     |         |                |               |
| Release             |         |                | Modification  |
| 10.07orearlier      |         |                | --            |
| Command Information |         |                |               |
| Platforms           | Command | context        | Authority     |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| destination    | ipv6              |     |     |
| -------------- | ----------------- | --- | --- |
| destination    | ipv6 <IPVv6-ADDR> |     |     |
| no destination | ipv6 [IPV6-ADDR]  |     |     |
Description
SetsthedestinationIPv6addressforanIPtunnel.Specifytheaddressoftheinterfaceontheremote
devicetowhichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPv6addressfromanIPtunnel.
| Parameter   |     |     | Description                             |
| ----------- | --- | --- | --------------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Thisisoptionalinthenoformofthecommand.
IPTunnels |208

Examples
DefinesthedestinationIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel
switch(config)#
|                       | interface | tunnel      | 8 mode | ip 6in6     |
| --------------------- | --------- | ----------- | ------ | ----------- |
| switch(config-ip-if)# |           | destination | ipv6   | 2001:DB8::1 |
DeletesthedestinationIPv6address2001:DB8::1fromIPv6inIPv6tunnel8.
| switch(config)#       | interface | tunnel         | 8            |                  |
| --------------------- | --------- | -------------- | ------------ | ---------------- |
| switch(config-ip-if)# |           | no destination |              | ipv6 2001:DB8::1 |
| Command History       |           |                |              |                  |
| Release               |           |                | Modification |                  |
| 10.07orearlier        |           |                | --           |                  |
| Command Information   |           |                |              |                  |
| Platforms             | Command   | context        | Authority    |                  |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
|     |     |     |     | n ip 6in4:CreatesanIPv4tunnelforIPv6traffic. |
| --- | --- | --- | --- | -------------------------------------------- |
|     |     |     |     | n ip 6in6:CreatesanIPv6tunnelforIPv6traffic. |
Thisisoptionalinthenoform,unlessamodehas
alreadybeenentered.
<TUNNEL-NUMBER> Specifiesthenumberforanewtunnel.Range:1to127.
Numberingissharedbetweenalltunnels,sothesametunnel
numbercannotbeusedforanIPv6inIPv4tunnelandaGRE
209
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
tunnel.
<EXISTING-TUNNEL-NUMBER> SpecifiesthenumberforanexistingIPtunnel.Range:1to
127.
Examples
DefinesanewIPv6inIPv4tunnelwithnumber27.
| switch(config)# | interface |     | tunnel | 27 mode ip 6in4 |
| --------------- | --------- | --- | ------ | --------------- |
switch(config-ip-if)#
Switchestotheconfig-ip-ifcontextforexistingtunnel27.
| switch(config)# | interface |     | tunnel | 27  |
| --------------- | --------- | --- | ------ | --- |
switch(config-ip-if)#
DeletesIPv6inIPv4tunnel27.
| switch(config)# | no  | interface | tunnel | 27  |
| --------------- | --- | --------- | ------ | --- |
DefinesanewIPv6inIPv6tunnelwithnumber8.
| switch(config)# | interface |     | tunnel | 8 mode ip 6in6 |
| --------------- | --------- | --- | ------ | -------------- |
switch(config-ip-if)#
DeletesIPv6inIPv6tunnelwithnumber3.
| switch(config)#     | no      | interface | tunnel | 33 mode gre ipv4 |
| ------------------- | ------- | --------- | ------ | ---------------- |
| Command History     |         |           |        |                  |
| Release             |         |           |        | Modification     |
| 10.07orearlier      |         |           |        | --               |
| Command Information |         |           |        |                  |
| Platforms           | Command | context   |        | Authority        |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config |     |     | forthiscommand. |
| --- | ------ | --- | --- | --------------- |
ip address
| ip address <IPV4-ADDR>/<MASK> |                    |     |     |     |
| ----------------------------- | ------------------ | --- | --- | --- |
| no ip address                 | <IPV4-ADDR>/<MASK> |     |     |     |
IPTunnels |210

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
| switch(config)# | interface | tunnel | 33  |
| --------------- | --------- | ------ | --- |
switch(config-gre-if)#
|                     |         | no ip address | 10.10.10.1/24 |
| ------------------- | ------- | ------------- | ------------- |
| Command History     |         |               |               |
| Release             |         |               | Modification  |
| 10.07orearlier      |         |               | --            |
| Command Information |         |               |               |
| Platforms           | Command | context       | Authority     |
6200 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ipv6 address
| ipv6 address    | <IPV6-ADDR>/<MASK> |     |     |
| --------------- | ------------------ | --- | --- |
| no ipv6 address | <IPV6-ADDR>/<MASK> |     |     |
Description
SetsthelocalIPaddressofanIPv6toIPv4tunnelorofanIPv6toIPv6tunnel.Thisaddressidentifiesthe
tunnelinterfaceforrouting.Itmustbeonthesamesubnetasthetunneladdressassignedonthe
remotedevice.
ThenoformofthiscommanddeletesthelocalIPaddressassignedtoanIPv6toIPv4tunnel.
211
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

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
| Platforms             | Command   | context         | Authority    |                  |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if |     | forthiscommand. |     |
| --- | --------- | --- | --------------- | --- |
ip mtu
ip mtu <VALUE>
Description
SetstheMTU(maximumtransmissionunit)foranIPinterface.Thedefaultvalueis1500bytes.
ThenoformofthiscommandsetstheMTUtothedefaultvalueof1500bytes.
| Parameter |     |     | Description                                          |     |
| --------- | --- | --- | ---------------------------------------------------- | --- |
| <VALUE>   |     |     | SpecifiestheMTUinbytes.Range:1,280bytesto9,192bytes. |     |
Usage
TheIPMTUisthelargestIPpacketthatcanbesentorreceivedbytheinterface.Foratunnel,theIP
MTUisthemaximumsizeoftheIPpayload.Toenablejumbopacketforwardingthroughthetunnel,set
theIPMTUofthetunneltoavaluegreaterthan1500.AlsosettheMTUandtheIPMTUvaluesforthe
underlyingphysicalinterfacethatthetunnelisusingtoavaluegreaterthan1,500bytes.TheIPMTUof
IPTunnels |212

thetunnelmustalsobegreaterthanorequaltotheMTUoftheingressinterfaceontheswitch.TheIP
MTUvalueofthetunnelmustalsobelessthanorequaltotheIPMToftheunderlyinginterfacethatthe
tunnelisusing.
Examples
SetstheMTUonIPv6inIPv4tunnel27to1000bytes.
| switch(config)#       | interface | tunnel   | 27 mode | ip 6in4 |
| --------------------- | --------- | -------- | ------- | ------- |
| switch(config-ip-if)# |           | mtu 1000 |         |         |
SetstheMTUonIPv6inIPv4tunnel27tothedefaultvalue.
| switch(config)#       | interface | tunnel | 27 mode | ip 6in4 |
| --------------------- | --------- | ------ | ------- | ------- |
| switch(config-ip-if)# |           | ip mtu |         |         |
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
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface | tunnel                  |     |     |     |
| -------------- | ----------------------- | --- | --- | --- |
| show interface | tunnel[<TUNNEL-NUMBER>] |     |     |     |
Description
ShowsconfigurationsettingsforallIPtunnels,oraspecifictunnel.
| Parameter       |     |     | Description                                  |     |
| --------------- | --- | --- | -------------------------------------------- | --- |
| <TUNNEL-NUMBER> |     |     | SpecifiesthenumberofanIPtunnel.Range:1to127. |     |
213
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

Examples
Showsconfigurationsettingsfortunnel12,whichisanIPv6inIPv6tunnelinthefollowingexample.
switch#
|     |              | show        | interface |         | tunnel12 |         |      |     |       |     |
| --- | ------------ | ----------- | --------- | ------- | -------- | ------- | ---- | --- | ----- | --- |
|     | Interface    | tunnel12    |           | is      | up       |         |      |     |       |     |
|     | Admin        | state       | is up     |         |          |         |      |     |       |     |
|     | tunnel       | type        | IPv6      | in IPv6 |          |         |      |     |       |     |
|     | tunnel       | interface   |           | IPv6    | address  | 4::1/64 |      |     |       |     |
|     | tunnel       | source      | IPv6      | address |          | 2::1    |      |     |       |     |
|     | tunnel       | destination |           | IPv6    | address  |         | 2::2 |     |       |     |
|     | tunnel       | ttl         | 60        |         |          |         |      |     |       |     |
|     | Description: |             | Network2  |         | Tunnel   |         |      |     |       |     |
|     | Statistics   |             |           |         |          | RX      |      | TX  | Total |     |
------------- -------------------- -------------------- --------------------
|                | L3 Packets |             |         |     |         |     | 0            | 0   |     | 0   |
| -------------- | ---------- | ----------- | ------- | --- | ------- | --- | ------------ | --- | --- | --- |
|                | L3 Bytes   |             |         |     |         |     | 0            | 0   |     | 0   |
| Command        |            | History     |         |     |         |     |              |     |     |     |
| Release        |            |             |         |     |         |     | Modification |     |     |     |
| 10.07orearlier |            |             |         |     |         |     | --           |     |     |     |
| Command        |            | Information |         |     |         |     |              |     |     |     |
| Platforms      |            |             | Command |     | context |     | Authority    |     |     |     |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show | running-config |     |     |           | interface             |     | tunnel |     |     |     |
| ---- | -------------- | --- | --- | --------- | --------------------- | --- | ------ | --- | --- | --- |
| show | running-config |     |     | interface | tunnel<TUNNEL-NUMBER> |     |        |     |     |     |
Description
ShowsthecommandsusedtoconfigureanIPtunnel.
| Parameter       |     |     |     |     |     |     | Description                                  |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
| <TUNNEL-NUMBER> |     |     |     |     |     |     | SpecifiesthenumberofanIPtunnel.Range:1to127. |     |     |     |
Examples
ShowstheconfigurationforIPv6inIPv4tunnel.
|     | switch#     | show | running-config   |             |     | interface | tunnel5 |     |     |     |
| --- | ----------- | ---- | ---------------- | ----------- | --- | --------- | ------- | --- | --- | --- |
|     | interface   |      | tunnel5          | mode        | ip  | 6in4      |         |     |     |     |
|     | source      | ip   | 10.10.10.12      |             |     |           |         |     |     |     |
|     | destination |      | ip               | 22.20.20.20 |     |           |         |     |     |     |
|     | ip6 address |      | 2001:DB8:5::1/64 |             |     |           |         |     |     |     |
|     | ttl 60      |      |                  |             |     |           |         |     |     |     |
IPTunnels |214

no shutdown
| description | Network10 |     |     |     |
| ----------- | --------- | --- | --- | --- |
ShowstheconfigurationforIPv6inIPv6tunnel.
| switch#             | show running-config |         | interface | tunnel1      |
| ------------------- | ------------------- | ------- | --------- | ------------ |
| interface           | tunnel              | 1 mode  | ip 6in6   |              |
| description         | Network2            | Tunnel  |           |              |
| source              | ipv6 2::1           |         |           |              |
| destination         | ipv6                | 2::2    |           |              |
| ipv6 address        | 4::1/64             |         |           |              |
| ttl 60              |                     |         |           |              |
| Command History     |                     |         |           |              |
| Release             |                     |         |           | Modification |
| 10.07orearlier      |                     |         |           | --           |
| Command Information |                     |         |           |              |
| Platforms           | Command             | context |           | Authority    |
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
| switch(config)#       | interface |     | tunnel   | 27 mode ip 6in4 |
| --------------------- | --------- | --- | -------- | --------------- |
| switch(config-ip-if)# |           | no  | shutdown |                 |
DisablesIPv6inIPv4interface27.
| switch(config)#       | interface |          | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | -------- | ------ | --------------- |
| switch(config-ip-if)# |           | shutdown |        |                 |
| Command History       |           |          |        |                 |
215
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
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
| Command History       |           |           |               |
| Release               |           |           | Modification  |
| 10.07orearlier        |           |           | --            |
| Command Information   |           |           |               |
| Platforms             | Command   | context   | Authority     |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
IPTunnels |216

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
| switch(config)#       | interface | tunnel    | 8            |             |
| --------------------- | --------- | --------- | ------------ | ----------- |
| switch(config-ip-if)# |           | no source | ipv6         | 2001:DB8::1 |
| Command History       |           |           |              |             |
| Release               |           |           | Modification |             |
| 10.07orearlier        |           |           | --           |             |
| Command Information   |           |           |              |             |
| Platforms             | Command   | context   | Authority    |             |
6200 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ttl
ttl <COUNT>
no ttl
Description
SetstheTTL(time-to-live),alsoknownasthehopcount,fortunneledpackets.Ifnotconfigured,the
defaultvalueof64isusedforthetunnel.(Thehopcountoftheoriginalpacketsisnotchanged.)A
maximumoffourdifferentTTLvaluescanbeusedatthesametimebyalltunnelsontheswitch.For
example,iftunnel-1hasTTL10,tunnel-2hasTTL20,tunnel-3hasTTL30,andtunnel-4hasTTL40,then
217
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

tunnel-5cannothaveauniqueTTLvalue,itmustreuseoneofthevaluesassignedtotheothertunnels
(10,20,30,40).
ThenoformofthiscommandsetsTTLtothedefaultvalueof64.
| Parameter |     |     | Description                                   |
| --------- | --- | --- | --------------------------------------------- |
| <COUNT>   |     |     | Specifiesthehopcount.Range:1to255.Default:64. |
Examples
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
config-ip-if
6200 Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
IPTunnels |218

Chapter 11

Internet Control Message Protocol
(ICMP)

Internet Control Message Protocol (ICMP)

The Internet Control Message Protocol (ICMP) is a supporting protocol in the Internet protocol suite. The
protocol is used by network devices, including routers, to send error messages and operational
information. For example, an ICMP message might indicate that a requested service is not available.
Another example of an ICMP message might be that a host or router could not be reached.

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

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

219

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
n ThesubnetornetworkofthesourceIPaddressisonthesamesubnetornetworkofthenext-hopIP
addressoftheroutedpacket.
n Thedatagramisnotsource-routed.
n Thedestinationunicastaddressisunreachable.Inthiscase,theroutergeneratestheICMP
destinationunreachablemessagetoinformthesourcehostaboutthesituation.
| ICMP    | commands      |     |     |     |
| ------- | ------------- | --- | --- | --- |
| ip icmp | redirect      |     |     |     |
| ip icmp | redirect      |     |     |     |
| no ip   | icmp redirect |     |     |     |
Description
EnablesthesendingofICMPv4andICMPv6redirectmessagestothesourcehost.Enabledbydefault.
ICMPredirectandactiveforwardingaremutuallyexclusive.
ThenoformofthiscommanddisablesICMPv4andICMPv6redirectmessagestothesourcehost.
Examples
EnablingICMPredirectmessages:
| switch(config)# |     | ip icmp | redirect |     |
| --------------- | --- | ------- | -------- | --- |
DisablingICMPredirectmessages:
| switch(config)# |         | no ip icmp | redirect |     |
| --------------- | ------- | ---------- | -------- | --- |
| Command         | History |            |          |     |
InternetControlMessageProtocol(ICMP)|220

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
<PACKET-INTERVAL>
SpecifiestheICMPv4/v6packetintervalinseconds.Default:1
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
221
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
InternetControlMessageProtocol(ICMP)|222

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

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

223

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
| switch(config)# |         | no ip dns | domain-list | domain1.com |
| --------------- | ------- | --------- | ----------- | ----------- |
| Command         | History |           |             |             |
DNS|224

| Release        |             |         |         |     | Modification |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | domain-name |     |               |     |       |            |     |
| --------- | ----------- | --- | ------------- | --- | ----- | ---------- | --- |
| ip dns    | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
| no ip dns | domain-name |     | <DOMAIN-NAME> |     | [ vrf | <VRF-NAME> | ]   |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.
Bydefault,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip
dns domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<DOMAIN-NAME>
SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     |     | ip dns | domain-name |     | domain.com |     |
| --------------- | --- | --- | ------ | ----------- | --- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |             |     | no ip dns | domain-name |              | domain.com |     |
| --------------- | ----------- | --- | --------- | ----------- | ------------ | ---------- | --- |
| Command         | History     |     |           |             |              |            |     |
| Release         |             |     |           |             | Modification |            |     |
| 10.07orearlier  |             |     |           |             | --           |            |     |
| Command         | Information |     |           |             |              |            |     |
225
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

| Platforms |     | Command | context |     | Authority |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip dns    | host |             |           |           |                  |     |     |
| --------- | ---- | ----------- | --------- | --------- | ---------------- | --- | --- |
| ip dns    | host | <HOST-NAME> | <IP-ADDR> |           | [ vrf <VRF-NAME> | ]   |     |
| no ip dns | host | <HOST-NAME> |           | <IP-ADDR> | [ vrf <VRF-NAME> |     | ]   |
Description
AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadof
queryingaDNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFis
defined,thedefaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
host <HOST-NAME> Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
| ThisexampledefinesanIPv4addressof     |             |     |        |            | 3.3.3.3forhost1.  |     |       |
| ------------------------------------- | ----------- | --- | ------ | ---------- | ----------------- | --- | ----- |
| switch(config)#                       |             | ip  | dns    | host host1 | 3.3.3.3           |     |       |
| ThisexampledefinesanIPv6addressofb::5 |             |     |        |            | forhost 1.        |     |       |
| switch(config)#                       |             | ip  | dns    | host host1 | b::5              |     |       |
| Thisexampledefinesremovestheentryfor  |             |     |        |            | host 1withaddress |     | b::5. |
| switch(config)#                       |             | no  | ip dns | host       | host1 b::5        |     |       |
| Command                               | History     |     |        |            |                   |     |       |
| Release                               |             |     |        |            | Modification      |     |       |
| 10.07orearlier                        |             |     |        |            | --                |     |       |
| Command                               | Information |     |        |            |                   |     |       |
DNS|226

| Platforms |     | Command | context |     | Authority |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- |
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
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
| switch(config)# |     |     | ip dns | server-address |     | 1.1.1.1 |     |
| --------------- | --- | --- | ------ | -------------- | --- | ------- | --- |
Thisexampledefinesanameserverata::1.
switch(config)#
|     |     |     | ip dns | server-address |     | a::1 |     |
| --- | --- | --- | ------ | -------------- | --- | ---- | --- |
Thisexampleremovesanameserverata::1.
| switch(config)# |             |     | no ip dns | server-address |              | a::1 |     |
| --------------- | ----------- | --- | --------- | -------------- | ------------ | ---- | --- |
| Command         | History     |     |           |                |              |      |     |
| Release         |             |     |           |                | Modification |      |     |
| 10.07orearlier  |             |     |           |                | --           |      |     |
| Command         | Information |     |           |                |              |      |     |
227
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- |

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip dns |      |             |     |     |     |
| ----------- | ---- | ----------- | --- | --- | --- |
| show ip dns | [vrf | <VRF-NAME>] |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
| switch(config)# |     | ip  | dns domain-name |     | domain.com  |
| --------------- | --- | --- | --------------- | --- | ----------- |
| switch(config)# |     | ip  | dns domain-list |     | domain5.com |
| switch(config)# |     | ip  | dns domain-list |     | domain8.com |
switch(config)#
|                 |           | ip         | dns server-address |         | 4.4.4.4     |
| --------------- | --------- | ---------- | ------------------ | ------- | ----------- |
| switch(config)# |           | ip         | dns server-address |         | 6.6.6.6     |
| switch(config)# |           | ip         | dns host           | host3   | 5.5.5.5     |
| switch(config)# |           | ip         | dns host           | host3   | c::12       |
| switch#         | show      | ip dns     |                    |         |             |
| VRF Name        | : default |            |                    |         |             |
| Domain Name     | :         | domain.com |                    |         |             |
| DNS Domain      | list      | :          | domain5.com,       |         | domain8.com |
| Name Server(s)  |           | : 4.4.4.4, |                    | 6.6.6.6 |             |
| Host Name       |           | Address    |                    |         |             |
-------------------------------
| host3          |             | 5.5.5.5 |         |     |              |
| -------------- | ----------- | ------- | ------- | --- | ------------ |
| host3          |             | c::12   |         |     |              |
| Command        | History     |         |         |     |              |
| Release        |             |         |         |     | Modification |
| 10.07orearlier |             |         |         |     | --           |
| Command        | Information |         |         |     |              |
| Platforms      | Command     |         | context |     | Authority    |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|228

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

Dynamic arp inspection is provided as a mechanism for making ARP more secure.

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

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

229

Several defense mechanisms can be put in place on a switch to protect against attacks:

n Limit the amount of ARP activity allowed from a host or on a port.

n Ensure that all ARP packets are consistent with one or more binding databases, which can be created

through various means.

n Enforce integrity checks on the ARP packets to check against different MAC or IP addresses in the

Ethernet or IP header and ARP header.

 The following is supported:

n Enabling and disabling of Dynamic ARP Inspection on a VLAN level (it does not have to be SVI).

n Defining the member ports of a VLAN as either trusted or untrusted.

n Only ARP traffic on untrusted ports subjected to checks.

n Routed ports (RoPs) always treated as trusted.

n Listening to the DHCP Bindings table and check every ARP packet to match against the binding.

ARP ACLs are not supported and the DHCP snooping table is the only source of binding.

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

ARP | 230

ARP commands
arp inspection
arp inspection
Description
EnablesDynamicARPinspectiononthecurrentVLAN,whichmeansthatARPpacketsreceivedfrom
untrustedinterfacesarediscardediftheyhaveanInvalidIP-to-MACaddressbinding.
ThenoformofthiscommanddisablesDynamicARPInspectionontheVLAN.
Examples
EnablingdynamicARPinspection:
| switch#              | configure | terminal       |     |
| -------------------- | --------- | -------------- | --- |
| switch(config)#      | vlan      | 1              |     |
| switch(config-vlan)# |           | arp inspection |     |
DisablingdynamicARPinspection:
| switch#              | configure | terminal          |              |
| -------------------- | --------- | ----------------- | ------------ |
| switch(config)#      | vlan      | 1                 |              |
| switch(config-vlan)# |           | no arp inspection |              |
| Command History      |           |                   |              |
| Release              |           |                   | Modification |
| 10.07orearlier       |           |                   | --           |
| Command Information  |           |                   |              |
| Platforms            | Command   | context           | Authority    |
6200 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| arp inspection    | trust |     |     |
| ----------------- | ----- | --- | --- |
| arp inspection    | trust |     |     |
| no arp inspection | trust |     |     |
Description
Configurestheinterfaceasatrusted.Allinterfacesareuntrustedbydefault.
Thenoformofthiscommandreturnstheinterfacetothedefaultstate(untrusted).
Example
Settinganinterfaceastrusted:
| switch(config-if)# |     | arp inspection | trust |
| ------------------ | --- | -------------- | ----- |
231
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Command        | History     |     |         |              |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| Release        |             |     |         | Modification |     |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| arp ipv4    | mac         |     |                |     |     |
| ----------- | ----------- | --- | -------------- | --- | --- |
| arp ipv4    | <IPV4_ADDR> | mac | <MAC_ADDR>     |     |     |
| no arp ipv4 | <IPV4_ADDR> |     | mac <MAC_ADDR> |     |     |
Description
SpecifiesapermanentstaticneighborentryintheARPtable(forIPv4neighbors).
ThenoformofthiscommanddeletesapermanentstaticneighborentryfromtheARPtable.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
ipv4 <IPV4-ADDR> SpecifiestheIPaddressoftheneighbororthevirtualIPaddress
oftheclusterinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255..Range:4096to131072.Default:131072.
mac <MAC-ADDR> SpecifiestheMACaddressoftheneighbororthemulticastMAC
addressinIANAformat(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
Example
ConfiguringastaticARPentryonainterfaceVLAN10:
| switch(config)#         |     | interface | vlan     | 10      |                       |
| ----------------------- | --- | --------- | -------- | ------- | --------------------- |
| switch(config-if-vlan)# |     |           | arp ipv4 | 2.2.2.2 | mac 01:00:5e:00:00:01 |
RemovingastaticARPentryoninterfaceVLAN10:
| switch(config)# |     | interface | vlan | 10  |     |
| --------------- | --- | --------- | ---- | --- | --- |
switch(config-if-vlan)# no arp ipv4 2.2.2.2 mac 01:00:5e:00:00:01
| Command        | History     |     |     |              |     |
| -------------- | ----------- | --- | --- | ------------ | --- |
| Release        |             |     |     | Modification |     |
| 10.07orearlier |             |     |     | --           |     |
| Command        | Information |     |     |              |     |
ARP|232

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |
| --- | -------------- | --- | --------------- |
arp process-grat-arp
arp process-grat-arp
no arp process-grat-arp
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
| switch(config)#                | interface | vlan | 2-100                   |
| ------------------------------ | --------- | ---- | ----------------------- |
| switch(config-if-vlan<2-100>)# |           |      | no shutdown             |
| switch(config-if-vlan<2-100>)# |           |      | no arp process-grat-arp |
| Command History                |           |      |                         |
233
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |
| --- | -------------- | --- | --------------- |
config-subif
clear arp
| clear arp | [port <PORT-ID> | | vrf {all-vrfs | | <VRF-NAME>}] |
| --------- | --------------- | --------------- | -------------- |
Description
ClearsIPv4andIPv6neighborentriesfromtheARPtable.Ifyoudonotspecifyanyparameters,ARP
tableentriesareclearedforthedefaultVRF.
| Parameter |           |     | Description                               |
| --------- | --------- | --- | ----------------------------------------- |
| port      | <PORT-ID> |     | Specifiesaphysicalportontheswitch.Format: |
member/slot/port.Forexample:1/1/1..
all-vrfs
SelectsallVRFs.
| <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |
| ---------- | --- | --- | --------------------------------------- |
Examples
ClearingallIPv4andIPv6neighborARPentriesforthedefaultVRF:
| switch# | clear arp |     |     |
| ------- | --------- | --- | --- |
ClearingallARPneighborentriesforaport:
| switch#        | clear arp   | 1/1/35  |              |
| -------------- | ----------- | ------- | ------------ |
| Command        | History     |         |              |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ARP|234

debug arp-security
| debug arp-security    | <LOG-CATEGORY>   | [severity |           | <LEVEL>] |          |
| --------------------- | ---------------- | --------- | --------- | -------- | -------- |
| no debug arp-security | [<LOG-CATEGORY>] |           | [severity |          | <LEVEL>] |
Description
EnablesARPsecuritydebuglogs.If<SEVERITY>isomitted,allseveritiesarelogged.
ThenoformofthiscommanddisablesARPsecuritydebuglogs.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<LOG-CATEGORY> SelectstheARPsecuritydebuglogcategory.Available
categoriesare::
|     |     |     | n all:SelectsallARPsecuritydebuglogcategories. |     |     |
| --- | --- | --- | ---------------------------------------------- | --- | --- |
config:SelectstheARPsecurityconfigdebuglogcategory.
n
|     |     |     | n inspection:SelectstheARPsecurityinspectiondebuglog |     |     |
| --- | --- | --- | ---------------------------------------------------- | --- | --- |
category.
|     |     |     | n packet:SelectstheARPsecuritypacketdebuglogcategory. |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
severity <LEVEL> SpecifieshowtofiltertheARPsecuritydebugloggingby
settingtheminimumseveritylevelforwhichdebuglogging
willbeperformed.Theselectedseveritylevelandall
severitiesabove(moresevere)willbeincludedinthelogging.
|     |     |     | n emerg:SetsARPsecuritydebuglogfilteringtoEmergencyonly. |     |     |
| --- | --- | --- | -------------------------------------------------------- | --- | --- |
|     |     |     | n alert:SetsARPsecuritydebuglogfilteringtoAlertandabove. |     |     |
critical:SetsARPsecuritydebuglogfilteringtoCriticaland
n
above.
|     |     |     | n error:SetsARPsecuritydebuglogfilteringtoErrorand |     |     |
| --- | --- | --- | -------------------------------------------------- | --- | --- |
above.
|     |     |     | n warning:SetsARPsecuritydebuglogfilteringtoWarningand |     |     |
| --- | --- | --- | ------------------------------------------------------ | --- | --- |
above.
|     |     |     | n notice:SetsARPsecuritydebuglogfilteringtoNoticeand |     |     |
| --- | --- | --- | ---------------------------------------------------- | --- | --- |
above.
info:SetsARPsecuritydebuglogfilteringtoInfoandabove.
n
|     |     |     | n debug:SetsARPsecuritydebuglogfilteringtoallseverities. |     |     |
| --- | --- | --- | -------------------------------------------------------- | --- | --- |
Examples
EnableARPsecuritydebugloggingforallcategoriesandallseverities:
| switch# debug | arp-security | all |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- |
EnableARPsecurityconfigdebuglogforseveritylevelErrorandabove:
| switch# debug | arp-security | config | severity |     | error |
| ------------- | ------------ | ------ | -------- | --- | ----- |
EnableARPsecurityinspectiondebuglogforseveritylevelNoticeandabove:
| switch# debug | arp-security | inspection |     | severity | notice |
| ------------- | ------------ | ---------- | --- | -------- | ------ |
EnableARPsecuritydebugpacketforseveritylevelCriticalandabove:
235
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

| switch# | debug arp-security | packet | severity | critical |
| ------- | ------------------ | ------ | -------- | -------- |
EnableARPsecuritydebugloggingforallcategoriesandseveritylevelAlertandabove:
| switch# | debug arp-security | all | severity | alert |
| ------- | ------------------ | --- | -------- | ----- |
DisableARPsecuritydebuglogging:
| switch#             | no debug arp-security |         |              |     |
| ------------------- | --------------------- | ------- | ------------ | --- |
| Command History     |                       |         |              |     |
| Release             |                       |         | Modification |     |
| 10.07orearlier      |                       |         | --           |     |
| Command Information |                       |         |              |     |
| Platforms           | Command               | context | Authority    |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
ip local-proxy-arp
ip local-proxy-arp
no ip local-proxy-arp
Description
EnableslocalproxyARPonthespecifiedinterface.LocalproxyARPissupportedonLayer3physical
interfacesandonVLANinterfaces.ToenablelocalproxyARPonaninterface,routingmustbeenabled
onthatinterface.
ThenoformofthiscommanddisableslocalproxyARPonthespecifiedinterface.
Examples
EnablinglocalproxyARPoninterface1/1/1:
| switch#            | interface | 1/1/1              |     |     |
| ------------------ | --------- | ------------------ | --- | --- |
| switch(config-if)# |           | ip local proxy-arp |     |     |
EnablinglocalproxyARPoninterfaceVLAN3:
| switch#                 | interface | vlan 3             |     |     |
| ----------------------- | --------- | ------------------ | --- | --- |
| switch(config-if-vlan)# |           | ip local-proxy-arp |     |     |
DisablinglocalproxyARPononinterface1/1/1.
ARP|236

| switch# | interface | 1/1/1 |     |
| ------- | --------- | ----- | --- |
switch(config-if)#
no ip local-proxy-arp
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |
| --- | -------------- | --- | --------------- |
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
| switch#                 | interface | 1/1/1        |     |
| ----------------------- | --------- | ------------ | --- |
| switch(config-if)#      |           | ip proxy-arp |     |
| EnablingproxyARPonVLAN  |           | 3:           |     |
| switch#                 | interface | vlan 3       |     |
| switch(config-if-vlan)# |           | ip proxy-arp |     |
EnablingproxyARPonaLAG11:
| switch(config)#        | int | lag 11       |     |
| ---------------------- | --- | ------------ | --- |
| switch(config-lag-if)# |     | ip proxy-arp |     |
DisablingproxyARPoninterface1/1/1:
| switch#            | interface | 1/1/1           |     |
| ------------------ | --------- | --------------- | --- |
| switch(config-if)# |           | no ip proxy-arp |     |
| Command History    |           |                 |     |
237
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |
| --------------------------- | ------------------ | --- | --- |

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan |     | forthiscommand. |
| --- | -------------- | --- | --------------- |
config-lag-vlan
| ipv6 neighbor    | mac         |                |     |
| ---------------- | ----------- | -------------- | --- |
| ipv6 neighbor    | <IPV6-ADDR> | mac <MAC-ADDR> |     |
| no ipv6 neighbor | <IPV6-ADDR> | mac <MAC-ADDR> |     |
Description
SpecifiesapermanentstaticneighborentryintheARPtable(forIPv6neighbors).
ThenoformofthiscommanddeletesapermanentstaticneighborentryfromtheARPtable.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV6-ADDR>>
SpecifiesanIPaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
mac <MAC-ADDR>>
SpecifiestheMACaddressoftheneighbor
(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0
toF.Range:4096to131072.Default:131072.
Example
| CreatesastaticARPentryoninterface |           |       | 1/1/1. |
| --------------------------------- | --------- | ----- | ------ |
| switch(config)#                   | interface | 1/1/1 |        |
switch(config-if)# arp ipv6 neighbor 2001:0db8:85a3::8a2e:0370:7334 mac
00:50:56:96:df:c8
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ARP|238

| show arp |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
show arp
Description
ShowstheentriesintheARP(AddressResolutionProtocol)table.
Usage
ThiscommanddisplaysinformationaboutARPentries,includingtheIPaddress,MACaddress,port,and
state.
Whennoparametersarespecified,theshow arpcommandshowsallARPentriesforthedefaultVRF
(VirtualRouterForwarding)instance.
Examples
| switch#      | show | arp |     |     |      |     |               |     |       |
| ------------ | ---- | --- | --- | --- | ---- | --- | ------------- | --- | ----- |
| IPv4 Address |      | MAC |     |     | Port |     | Physical Port |     | State |
-------------------------------------------------------------------------------
| 192.168.1.2 |        |        | 00:50:56:96:7b:e0 |         |     | vlan10 | 1/1/29 | stale     |     |
| ----------- | ------ | ------ | ----------------- | ------- | --- | ------ | ------ | --------- | --- |
| 192.168.1.3 |        |        | 00:50:56:96:7b:ac |         |     | vlan10 | 1/1/1  | reachable |     |
| Total       | Number | Of ARP | Entries           | Listed- | 2.  |        |        |           |     |
-------------------------------------------------------------------------------
| Command        | History     |     |         |     |              |     |     |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- |
| Release        |             |     |         |     | Modification |     |     |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |     |     |
| Command        | Information |     |         |     |              |     |     |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show arp            | inspection |           | interface |            |     |                  |     |     |     |
| ------------------- | ---------- | --------- | --------- | ---------- | --- | ---------------- | --- | --- | --- |
| show arp inspection |            | interface |           | [<IFNAME>] |     | [vlan <VLAN-ID>] |     |     |     |
Description
ShowsthecurrentconfigurationofdynamicARPinspectiononaninterface.
| Parameter |     |     |     |     | Description            |     |     |     |     |
| --------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
| <IFNAME>  |     |     |     |     | Specifiestheinterface. |     |     |     |     |
<VLAN-ID>
SpecifiestheVLANID.Range:1to4094.
Examples
239
| AOS-CX10.11IPServicesGuide| |     | (6200SwitchSeries) |     |     |     |     |     |     |     |
| --------------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |

ShowingcurrentconfigurationofdynamicARPinspectiononallinterfaces:
| switch# | show | arp inspection |     | interface |     |
| ------- | ---- | -------------- | --- | --------- | --- |
---------------------------------------------------------------------------
| Interface |     |     | Trust-State |     |     |
| --------- | --- | --- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 |     |     | Untrusted |     |     |
| ----- | --- | --- | --------- | --- | --- |
---------------------------------------------------------------------------
ShowingcurrentconfigurationofdynamicARPinspectiononaparticularinterface:
| switch# | show | arp inspection |     | interface | 1/1/1 |
| ------- | ---- | -------------- | --- | --------- | ----- |
---------------------------------------------------------------------------
| Interface |     |     | Trust-State |     |     |
| --------- | --- | --- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 |     |     | Untrusted |     |     |
| ----- | --- | --- | --------- | --- | --- |
---------------------------------------------------------------------------
ShowingcurrentconfigurationofdynamicARPinspectiononinterfaceVLAN2:
| switch# | show | arp inspection |     | interface | vlan 2 |
| ------- | ---- | -------------- | --- | --------- | ------ |
-----------------------------------------------------------------
| Interface |     |     | Trust-State |     |     |
| --------- | --- | --- | ----------- | --- | --- |
-----------------------------------------------------------------
| vlan2 |     |     | Trusted |     |     |
| ----- | --- | --- | ------- | --- | --- |
-----------------------------------------------------------------
| Command        | History     |     |         |     |              |
| -------------- | ----------- | --- | ------- | --- | ------------ |
| Release        |             |     |         |     | Modification |
| 10.07orearlier |             |     |         |     | --           |
| Command        | Information |     |         |     |              |
| Platforms      | Command     |     | context |     | Authority    |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp            | inspection |            | statistics |      |             |
| ------------------- | ---------- | ---------- | ---------- | ---- | ----------- |
| show arp inspection |            | statistics |            | vlan | [<VLAN-ID>] |
Description
ShowsstatisticsaboutforwardedanddroppedARPpackets.When<VLAN-ID>isnotspecified,
informationisshownforallconfiguredVLANs.
ARP|240

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<VLAN-ID>
SpecifiestheVLANIDorrangeofIDsseparatedbyadash"-".
Range:1to4094.
Examples
ShowingARPpacketstatisticsforarangeofVLANs:
| switch# | show arp inspection |     | statistics | vlan | 1-100 |
| ------- | ------------------- | --- | ---------- | ---- | ----- |
-----------------------------------------------------------------
| VLAN | Name |     | Forwarded |     | Dropped |
| ---- | ---- | --- | --------- | --- | ------- |
-----------------------------------------------------------------
| 1   | DEFAULT_VLAN_1 |     | 0   |     | 0   |
| --- | -------------- | --- | --- | --- | --- |
-----------------------------------------------------------------
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp            | inspection | vlan        |     |     |     |
| ------------------- | ---------- | ----------- | --- | --- | --- |
| show arp inspection | vlan       | [<VLAN-ID>] |     |     |     |
Description
ShowsthecurrentconfigurationofdynamicARPinspectiononaVLAN.When<VLAN-ID>isnotspecified,
informationisshownforallconfiguredVLANs.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<VLAN-ID>
SpecifiestheVLANIDorrangeofIDsseparatedbyadash"-".
Range:1to4094.
Examples
ShowingdynamicARPconfigurationforallVLANs:
switch#
|     | show arp inspection |     | vlan |     |     |
| --- | ------------------- | --- | ---- | --- | --- |
-----------------------------------------------------------------
| VLAN | Name |     | ARP Inspection |     |     |
| ---- | ---- | --- | -------------- | --- | --- |
241
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

-----------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     | -       |     |
| ---------------- | --- | ------- | --- |
| 100 VLAN100      |     | -       |     |
| 200 VLAN200      |     | Enabled |     |
-----------------------------------------------------------------
ShowingdynamicARPconfigurationforaparticularVLAN:
| switch# | show arp inspection | vlan | 1   |
| ------- | ------------------- | ---- | --- |
-----------------------------------------------------------------
| VLAN Name |     | ARP Inspection |     |
| --------- | --- | -------------- | --- |
-----------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     | -   |     |
| ---------------- | --- | --- | --- |
-----------------------------------------------------------------
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp | state |     |     |
| -------- | ----- | --- | --- |
show arp state {all | failed | incomplete | permanent | reachable | stale}
Description
ShowsARP(AddressResolutionProtocol)cacheentriesthatareinthespecifiedstate.
| Parameter |     |     | Description                                    |
| --------- | --- | --- | ---------------------------------------------- |
| all       |     |     | ShowstheARPcacheentriesforallVRF(VirtualRouter |
Forwarding)instances.
failed
ShowstheARPcacheentriesthatareinfailedstate.The
neighbormighthavebeendeleted.
incomplete
ShowstheARPcacheentriesthatareinincompletestate.
Anincompletestatemeansthataddressresolutionisinprogress
andthelink-layeraddressoftheneighborhasnotyetbeen
determined.Asolicitationrequestwassent,andtheswitchis
waitingforasolicitationreplyoratimeout.
| permanent |     |     | ShowstheARPcacheentriesthatareinpermanentstate.ARP |
| --------- | --- | --- | -------------------------------------------------- |
entriesthatareinapermanentstatecanberemovedby
administrativeactiononly.
ARP|242

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
reachable
ShowstheARPcacheentriesthatareinreachablestate,
meaningthattheneighborisknowntohavebeenreachable
recently.
stale
ShowsARPcacheentriesthatareinstalestate.
ARPcacheentriesareinthestalestateiftheelapsedtimeisin
excessoftheARPtimeoutinsecondssincethelastpositive
confirmationthattheforwardingpathwasfunctioningproperly.
Examples
| switch#      | show arp state | failed |      |               |       |
| ------------ | -------------- | ------ | ---- | ------------- | ----- |
| IPv4 Address | MAC            |        | Port | Physical Port | State |
---------------------------------------------------------------------------
| 192.168.1.4         |         |         | vlan10       |     | failed |
| ------------------- | ------- | ------- | ------------ | --- | ------ |
| Command History     |         |         |              |     |        |
| Release             |         |         | Modification |     |        |
| 10.07orearlier      |         |         | --           |     |        |
| Command Information |         |         |              |     |        |
| Platforms           | Command | context | Authority    |     |        |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp         | summary   |                   |     |     |     |
| ---------------- | --------- | ----------------- | --- | --- | --- |
| show arp summary | [all-vrfs | | vrf <VRF-NAME>] |     |     |     |
Description
ShowsasummaryoftheIPv4andIPv6neighborentriesontheswitchforallVRFsoraspecificVRF.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
all-vrfs
SelectsallVRFs.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |     |     |
| -------------- | --- | --- | ----------------------- | --- | --- |
Examples
ShowingsummaryARPinformationforallVRFs:
243
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- |

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
| Command        | History     |         |              |     |
| -------------- | ----------- | ------- | ------------ | --- |
| Release        |             |         | Modification |     |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
ARP|244

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
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
<INTERFACE>
Specifiesaphysicalport,VLAN,orLAGontheswitch.Forphysical
ports,usetheformatmember/slot/port(forexample,1/3/1).
Examples
ShowingARPtimeoutinformationforaport:
| switch# | show arp timeout | 1/1/1 |     |     |
| ------- | ---------------- | ----- | --- | --- |
ARP Timeout:
------------------
| Port                | VRF     |         |              | Timeout |
| ------------------- | ------- | ------- | ------------ | ------- |
| 1/1/1               | default |         |              | 600     |
| Command History     |         |         |              |         |
| Release             |         |         | Modification |         |
| 10.07orearlier      |         |         | --           |         |
| Command Information |         |         |              |         |
| Platforms           | Command | context | Authority    |         |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show arp           | vrf   |             |     |     |
| ------------------ | ----- | ----------- | --- | --- |
| show arp {all-vrfs | | vrf | <VRF-NAME>} |     |     |
Description
ShowstheARPtableforallVRFinstances,orforthenamedVRF.
245
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

| Parameter |     |     |     |     | Description       |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
| all-vrfs  |     |     |     |     | SpecifiesallVRFs. |     |     |     |     |
vrf <VRF-NAME> SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
Examples
ShowingARPentriesforVRFvrf1.
| switch# | show    | arp vrf | test |     |      |          |      |     |       |
| ------- | ------- | ------- | ---- | --- | ---- | -------- | ---- | --- | ----- |
| IPv4    | Address | MAC     |      |     | Port | Physical | Port |     | State |
VRF
----------------------------------------------------------------------------------
------------
| 100.1.250.50 |     | 00:50:56:8d:44:13 |     |     | vlan1001 | 1/1/2 |     |     |     |
| ------------ | --- | ----------------- | --- | --- | -------- | ----- | --- | --- | --- |
| reachable    |     | vrf1              |     |     |          |       |     |     |     |
100.2.250.60 00:50:56:8d:45:63 vlan1002 vxlan1(1920:1680:1:1::2)
| permanent |        | vrf1   |         |         |     |     |     |     |     |
| --------- | ------ | ------ | ------- | ------- | --- | --- | --- | --- | --- |
| Total     | Number | Of ARP | Entries | Listed: | 2.  |     |     |     |     |
----------------------------------------------------------------------------------
------------
ThisexamplefromadifferentnetworkshowsARPentriesforallVRFs.
| switch# | show          | arp all-vrfs |     |     |     |     |     |     |     |
| ------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| ARP     | IPv4 Entries: |              |     |     |     |     |     |     |     |
-------------------------------------------------------
| IPv4           | Address | MAC               |     |     | Port Physical | Port | State     | VRF  |     |
| -------------- | ------- | ----------------- | --- | --- | ------------- | ---- | --------- | ---- | --- |
| 192.168.120.10 |         | 00:50:56:bd:10:be |     |     | 1/1/32 1/1/32 |      | reachable | red  |     |
| 10.20.30.40    |         | 00:50:56:bd:6a:c5 |     |     | 1/1/29 1/1/29 |      | reachable | test |     |
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
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show      | ipv6      | neighbors |     |       |             |     |     |     |     |
| --------- | --------- | --------- | --- | ----- | ----------- | --- | --- | --- | --- |
| show ipv6 | neighbors | {all-vrfs |     | | vrf | <VRF-NAME>} |     |     |     |     |
ARP|246

Description
ShowsentriesintheARPtableforallIPv6neighborsforallVRFsorforaspecificVRF.
Whennoparametersarespecified,thiscommandshowsallARPentriesforthedefaultVRF,andstate
informationforreachableandstaleentriesonly.
| Parameter |     |     | Description       |     |     |     |
| --------- | --- | --- | ----------------- | --- | --- | --- |
| all-vrfs  |     |     | SpecifiesallVRFs. |     |     |     |
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
Examples
| switch#       | show ipv6 | neighbors |     |     |     |     |
| ------------- | --------- | --------- | --- | --- | --- | --- |
| IPv6 Entries: |           |           |     |     |     |     |
-------------------------------------------------------
| IPv6 Address |     |     | MAC | Port | Physical Port | State |
| ------------ | --- | --- | --- | ---- | ------------- | ----- |
fe80::a21d:48ff:fe8f:2700 a0:1d:48:8f:27:00 vlan2300 1/1/31 reachable
fe80::f603:43ff:fe80:a600 f4:03:43:80:a6:00 vlan2300 1/1/30 reachable
-------------------------------------------------------
| Total Number | Of IPv6 | Neighbors | Entries Listed: | 2.  |     |     |
| ------------ | ------- | --------- | --------------- | --- | --- | --- |
-------------------------------------------------------
| Command        | History     |         |              |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         | Modification |     |     |     |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
(#)
| show ipv6 | neighbors | state |     |     |     |     |
| --------- | --------- | ----- | --- | --- | --- | --- |
show ipv6 neighbors state {all | failed | incomplete | permanent | reachable | stale}
Description
ShowsallIPv6neighborARP(AddressResolutionProtocol)cacheentries,orthosecacheentriesthatare
inthespecifiedstate.
247
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- | --- | --- |

| Parameter |     |     | Description                                          |     |     |
| --------- | --- | --- | ---------------------------------------------------- | --- | --- |
| all       |     |     | ShowsallARPcacheentries.                             |     |     |
| failed    |     |     | ShowsARPcacheentriesthatareinfailedstate.Theneighbor |     |     |
mighthavebeendeleted.Settheneighbortobeunreachable.
| incomplete |     |     | ShowsARPcacheentriesthatareinincompletestate. |     |     |
| ---------- | --- | --- | --------------------------------------------- | --- | --- |
Anincompletestatemeansthataddressresolutionisinprogress
andthelink-layeraddressoftheneighborhasnotyetbeen
determined.Thismeansthatasolicitationrequestwassent,and
youarewaitingforasolicitationreplyoratimeout.
| permanent |     |     | ShowsARPcacheentriesthatareinpermanentstate. |     |     |
| --------- | --- | --- | -------------------------------------------- | --- | --- |
reachable ShowsARPcacheentriesthatareinreachablestate,meaning
thattheneighborisknowntohavebeenreachablerecently.
| stale |     |     | ShowsARPcacheentriesthatareinstalestate. |     |     |
| ----- | --- | --- | ---------------------------------------- | --- | --- |
ARPcacheentriesareinthestalestateiftheelapsedtimeisin
excessoftheARPtimeoutinsecondssincethelastpositive
confirmationthattheforwardingpathwasfunctioningproperly.
Example
| switch#      | show ipv6 | neighbors | state all |               |            |
| ------------ | --------- | --------- | --------- | ------------- | ---------- |
| IPv6 Address |           |           | MAC       | Port Physical | Port State |
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
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
ARP|248

| show tech | arp-security |     |     |     |
| --------- | ------------ | --- | --- | --- |
| show tech | arp-security |     |     |     |
Description
Showstheoutputofthesethreecommands:
| n show arp | inspection | statistics | vlan |     |
| ---------- | ---------- | ---------- | ---- | --- |
| n show arp | inspection | vlan       |      |     |
| show arp   | inspection | interface  |      |     |
n
Examples
ShowingtheoutputofthethreeARP securityshowcommands:
| switch(config-if)# |     | show tech | arp-security |     |
| ------------------ | --- | --------- | ------------ | --- |
====================================================
| Show | Tech executed | on Mon | Nov 28 09:53:54 | 2019 |
| ---- | ------------- | ------ | --------------- | ---- |
====================================================
====================================================
| [Begin] | Feature | arp-security |     |     |
| ------- | ------- | ------------ | --- | --- |
====================================================
*********************************
| Command | : show arp | inspection | statistics | vlan |
| ------- | ---------- | ---------- | ---------- | ---- |
*********************************
-----------------------------------------------------------------
| VLAN | Name | Forwarded |     | Dropped |
| ---- | ---- | --------- | --- | ------- |
-----------------------------------------------------------------
| 1   | DEFAULT_VLAN_1 | 0   |     | 0   |
| --- | -------------- | --- | --- | --- |
| 200 | VLAN200        | 0   |     | 0   |
-----------------------------------------------------------------
*********************************
| Command | : show arp | inspection | vlan |     |
| ------- | ---------- | ---------- | ---- | --- |
*********************************
-----------------------------------------------------------------
| VLAN | Name | ARP-Inspection |     |     |
| ---- | ---- | -------------- | --- | --- |
-----------------------------------------------------------------
| 1   | DEFAULT_VLAN_1 | -       |     |     |
| --- | -------------- | ------- | --- | --- |
| 200 | VLAN200        | Enabled |     |     |
-----------------------------------------------------------------
*********************************
| Command | : show arp | inspection | interface |     |
| ------- | ---------- | ---------- | --------- | --- |
*********************************
---------------------------------------------------------------------------
| Interface |     | Trust-State |     |     |
| --------- | --- | ----------- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1  |     | Untrusted |     |     |
| ------ | --- | --------- | --- | --- |
| lag100 |     | Trusted   |     |     |
---------------------------------------------------------------------------
====================================================
| [End] | Feature arp-security |     |     |     |
| ----- | -------------------- | --- | --- | --- |
====================================================
249
| AOS-CX10.11IPServicesGuide| | (6200SwitchSeries) |     |     |     |
| --------------------------- | ------------------ | --- | --- | --- |

====================================================
| Show Tech | commands | executed successfully |     |
| --------- | -------- | --------------------- | --- |
====================================================
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ARP|250

Support and Other Resources

Chapter 14

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

Airheads social
forums and
Knowledge Base

AOS-CX Switch
Software
Documentation
Portal

Aruba Hardware
Documentation
and Translations

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

251

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
SupportandOtherResources|252

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

AOS-CX 10.11 IP Services Guide | (6200 Switch Series)

253