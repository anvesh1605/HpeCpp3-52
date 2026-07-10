| AOS-CX |     | 10.07 | IP  | Services |
| ------ | --- | ----- | --- | -------- |
Guide
|     | 6300, | 6400 | Switch | Series |
| --- | ----- | ---- | ------ | ------ |
PartNumber:5200-7862
Published:April2021
Edition:1

Copyright Information

© Copyright 2021 Hewlett Packard Enterprise Development LP.

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
Contents 3
| About this | document |     | 8   |
| ---------- | -------- | --- | --- |
Applicableproducts 8
Latestversionavailableonline 8
Commandsyntaxnotationconventions 8
Abouttheexamples 9
Identifyingswitchportsandinterfaces 9
Identifyingmodularswitchcomponents 10
IRDP 11
ConfiguringIRDP 12
IRDPcommands 13
|             | diag-dumpirdpbasic      |     | 13  |
| ----------- | ----------------------- | --- | --- |
|             | ipirdp                  |     | 13  |
|             | ipirdpholdtime          |     | 14  |
|             | ipirdpmaxadvertinterval |     | 15  |
|             | ipirdpminadvertinterval |     | 15  |
|             | ipirdppreference        |     | 16  |
|             | showipirdp              |     | 17  |
| IPv6 Router | Advertisement           |     | 18  |
ConfiguringIPv6RA 18
IPv6RAscenario 20
IPv6RAcommands 21
|     | ipv6address<global-unicast-address> |     | 21  |
| --- | ----------------------------------- | --- | --- |
|     | ipv6addressautoconfig               |     | 21  |
|     | ipv6addresslink-local               |     | 22  |
|     | ipv6ndcache-limit                   |     | 23  |
|     | ipv6nddadattempts                   |     | 23  |
|     | ipv6ndhop-limit                     |     | 24  |
|     | ipv6ndmtu                           |     | 25  |
|     | ipv6ndns-interval                   |     | 25  |
|     | ipv6ndprefix                        |     | 26  |
|     | ipv6ndradnssearch-list              |     | 27  |
|     | ipv6ndradnsserver                   |     | 28  |
|     | ipv6ndralifetime                    |     | 29  |
|     | ipv6ndramanaged-config-flag         |     | 29  |
|     | ipv6ndramax-interval                |     | 30  |
|     | ipv6ndramin-interval                |     | 31  |
|     | ipv6ndraother-config-flag           |     | 32  |
|     | ipv6ndrareachable-time              |     | 32  |
|     | ipv6ndraretrans-timer               |     | 33  |
|     | ipv6ndrouter-preference             |     | 33  |
|     | ipv6ndsuppress-ra                   |     | 34  |
|     | showipv6ndglobaltraffic             |     | 35  |
|     | showipv6ndinterface                 |     | 36  |
|     | showipv6ndinterfaceprefix           |     | 38  |
3
| AOS-CX10.07IPServicesGuide| | (6300and6400 | SwitchSeries) |     |
| --------------------------- | ------------ | ------------- | --- |

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

DHCP client commands

ip dhcp
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
http proxy
lease
netbios-name-server
netbios-node-type
option

39
40

41
41
42
43
44
47
47
47
49
49
50
51
51
52
53
53
54

56
56
56
56
57
57
58
59
60
61
62
69
69
70
71
72
76
76
78
79
79
79
80
81
82
83
83
84
85
85
86
87
88
88
89

Contents | 4

pool
range
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

DHCPv4 snooping commands

clear dhcpv4-snooping binding
clear dhcpv4-snooping statistics
dhcpv4-snooping
dhcpv4-snooping (in config-vlan context)
dhcpv4-snooping allow-overwrite-binding
dhcpv4-snooping authorized-server
dhcpv4-snooping external-storage
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
nd-snooping
nd-snooping (in config-vlan context)
nd-snooping mac-check

90
91
92
94
95
95
95
96
97
98
98
99
99
100
101
102
102
104

106
107
107
108
108
109
110
110
111
112
113
114
114
115
116
117
117
117
118
119
119
120
121
122
123
123
124
125

127
127
127
127
128
129
129
130

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

5

|                                                       | nd-snoopingprefix-list            |         |          |        | 131 |
| ----------------------------------------------------- | --------------------------------- | ------- | -------- | ------ | --- |
|                                                       | nd-snoopingmax-bindings           |         |          |        | 131 |
|                                                       | nd-snoopingnd-guard               |         |          |        | 132 |
|                                                       | nd-snoopingra-guard               |         |          |        | 133 |
|                                                       | nd-snoopingra-drop                |         |          |        | 134 |
|                                                       | nd-snoopingtrust                  |         |          |        | 135 |
|                                                       | shownd-snooping                   |         |          |        | 135 |
|                                                       | shownd-snoopingbinding            |         |          |        | 137 |
|                                                       | shownd-snoopingprefix-list        |         |          |        | 137 |
|                                                       | shownd-snoopingstatistics         |         |          |        | 138 |
| IP Tunnels                                            |                                   |         |          |        | 140 |
| ConfiguringanIPtunnel                                 |                                   |         |          |        | 141 |
| CreatingaGREtunnelfortraversingapublicnetwork         |                                   |         |          |        | 141 |
| CreatingtwoGREtunnelstodifferentdestinationaddresses  |                                   |         |          |        | 143 |
| CreatinganIPv6inIPv4tunnelfortraversingapublicnetwork |                                   |         |          |        | 145 |
| CreatinganIPv6inIPv6tunnelfortraversingapublicnetwork |                                   |         |          |        | 147 |
| IPtunnelscommands                                     |                                   |         |          |        | 148 |
|                                                       | description                       |         |          |        | 148 |
|                                                       | destinationip                     |         |          |        | 149 |
|                                                       | destinationipv6                   |         |          |        | 150 |
|                                                       | interfacetunnel                   |         |          |        | 151 |
|                                                       | ipaddress                         |         |          |        | 152 |
|                                                       | ipv6address                       |         |          |        | 153 |
|                                                       | ipmtu                             |         |          |        | 154 |
|                                                       | showinterfacetunnel               |         |          |        | 155 |
|                                                       | showrunning-configinterfacetunnel |         |          |        | 157 |
|                                                       | shutdown                          |         |          |        | 158 |
|                                                       | sourceip                          |         |          |        | 159 |
|                                                       | sourceipv6                        |         |          |        | 160 |
|                                                       | ttl                               |         |          |        | 160 |
|                                                       | vrfattach                         |         |          |        | 161 |
| IP Source                                             | Lockdown                          |         |          |        | 163 |
| IPv4sourcelockdowncommands                            |                                   |         |          |        | 163 |
|                                                       | ipv4source-binding                |         |          |        | 163 |
|                                                       | ipv4source-lockdown               |         |          |        | 164 |
|                                                       | ipv4source-lockdownhardwareretry  |         |          |        | 165 |
|                                                       | showipv4source-binding            |         |          |        | 165 |
|                                                       | showipv4source-lockdown           |         |          |        | 166 |
| IPv6sourcelockdowncommands                            |                                   |         |          |        | 169 |
|                                                       | ipv6source-binding                |         |          |        | 169 |
|                                                       | ipv6source-lockdown               |         |          |        | 170 |
|                                                       | ipv6source-lockdownhardwareretry  |         |          |        | 170 |
|                                                       | showipv6source-binding            |         |          |        | 171 |
|                                                       | showipv6source-lockdown           |         |          |        | 171 |
| Internet                                              | Control                           | Message | Protocol | (ICMP) | 175 |
| ICMPmessagetypes                                      |                                   |         |          |        | 175 |
| WhenICMPmessagesaresent                               |                                   |         |          |        | 175 |
| ICMPredirectmessages                                  |                                   |         |          |        | 176 |
| WhenICMPredirectmessagesaresent                       |                                   |         |          |        | 176 |
| ICMPcommands                                          |                                   |         |          |        | 176 |
|                                                       | ipicmpredirect                    |         |          |        | 176 |
|                                                       | ipicmpthrottle                    |         |          |        | 177 |
|                                                       | ipicmpunreachable                 |         |          |        | 177 |
Contents|6

DNS 179
| DNSclient               |                    |     | 179 |
| ----------------------- | ------------------ | --- | --- |
| ConfiguringtheDNSclient |                    |     | 179 |
| DNSclientcommands       |                    |     | 180 |
|                         | ipdnsdomain-list   |     | 180 |
|                         | ipdnsdomain-name   |     | 181 |
|                         | ipdnshost          |     | 182 |
|                         | ipdnsserveraddress |     | 183 |
|                         | showipdns          |     | 184 |
ARP 186
| ConfiguringproxyARP                     |                             |               | 187 |
| --------------------------------------- | --------------------------- | ------------- | --- |
| ConfiguringlocalproxyARP                |                             |               | 187 |
| DynamicARPInspection                    |                             |               | 188 |
| ARPcommands                             |                             |               | 189 |
|                                         | arpcache-limit              |               | 189 |
|                                         | arpinspection               |               | 189 |
|                                         | arpinspectiontrust          |               | 190 |
|                                         | arpipv4mac                  |               | 190 |
|                                         | cleararp                    |               | 191 |
|                                         | iplocal-proxy-arp           |               | 192 |
|                                         | ipv6neighbormac             |               | 193 |
|                                         | ipproxy-arp                 |               | 193 |
|                                         | showarp                     |               | 194 |
|                                         | showarpinspectioninterface  |               | 195 |
|                                         | showarpinspectionstatistics |               | 196 |
|                                         | showarpstate                |               | 196 |
|                                         | showarpsummary              |               | 197 |
|                                         | showarptimeout              |               | 199 |
|                                         | showarpvrf                  |               | 199 |
|                                         | showipv6neighbors           |               | 201 |
|                                         | showipv6neighborsstate      |               | 201 |
| Support                                 | and other                   | resources     | 203 |
| AccessingArubaSupport                   |                             |               | 203 |
| Accessingupdates                        |                             |               | 203 |
|                                         | ArubaSupportPortal          |               | 203 |
|                                         | MyNetworking                |               | 204 |
| Warrantyinformation                     |                             |               | 204 |
| Regulatoryinformation                   |                             |               | 204 |
| Documentationfeedback                   |                             |               | 204 |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                             | SwitchSeries) | 7   |

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and other resources.

Command syntax notation conventions

Convention

Usage

example-text

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window. Items that
appear like the example text in the previous column are to be entered exactly
as shown and are required unless enclosed in brackets ([ ]).

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:
n <example-text>
n <example-text>
n example-text

n example-text

|

{ }

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables are
enclosed in angle brackets (< >). Substitute the text—including the
enclosing angle brackets—with an actual value.

n For output formats where italic text can be displayed, variables might

or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

Braces. Indicates that at least one of the enclosed items is required.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

8

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
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchorenvironment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understandingthe | CLI prompts |     |     |
| ---------------- | ----------- | --- | --- |
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
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,wheninthe
VLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 6300Switch | Series |     |     |
| ----------------- | ------ | --- | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
Aboutthisdocument|9

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

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

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

10

Chapter 2

IRDP

IRDP

ICMP Router Discovery Protocol (IRDP), an extension of the ICMP, is independent of any routing protocol. It
allows hosts to discover the IP addresses of neighboring routers that can act as default gateways to reach
devices on other IP networks.

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

Destination address of RA

An RA uses either of the following destination IP addresses:

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

11

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

n Enables IRDP on the layer 3 interface 1/1/1 with packet type set to broadcast.

n Sets the hold time to 5000 seconds.

n Sets the advertisement interval to 30 seconds.

n Sets the minimum advertisement interval to 25 seconds.

n Sets the IRDP preference level to 25.

switch(config)# interface 1/1/1
switch(config-if)# ip irdp broadcast

IRDP | 12

|     | switch(config-if)# | ip  | irdp holdtime | 5000 |     |     |
| --- | ------------------ | --- | ------------- | ---- | --- | --- |
switch(config-if)#
|     |                    | ip         | irdp maxadvertinterval |     | 30  |     |
| --- | ------------------ | ---------- | ---------------------- | --- | --- | --- |
|     | switch(config-if)# | ip         | irdp minadvertinterval |     | 25  |     |
|     | switch(config-if)# | ip         | irdp preference        | 25  |     |     |
|     | IRDP commands      |            |                        |     |     |     |
|     | diag-dump          | irdp basic |                        |     |     |     |
Syntax
|     | diag-dump irdp | basic |     |     |     |     |
| --- | -------------- | ----- | --- | --- | --- | --- |
Description
DisplaysdiagnosticinformationforIRDP.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch# | diag-dump irdp | basic |     |     |     |
| --- | ------- | -------------- | ----- | --- | --- | --- |
=========================================================================
|     | [Start] | Feature irdp | Time : Thu Jun | 8 09:50:28 | 2017 |     |
| --- | ------- | ------------ | -------------- | ---------- | ---- | --- |
=========================================================================
-------------------------------------------------------------------------
|     | [Start] | Daemon hpe-rdiscd |     |     |     |     |
| --- | ------- | ----------------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
|     | Interface: | 1/1/1 (state | : Up) |     |     |     |
| --- | ---------- | ------------ | ----- | --- | --- | --- |
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
|     | Router IPs | - 192.168.1.2, |       |     |     |     |
| --- | ---------- | -------------- | ----- | --- | --- | --- |
|     | Interface: | 1/1/2 (state   | : Up) |     |     |     |
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
|     | Router IPs | - 192.168.2.2, |     |     |     |     |
| --- | ---------- | -------------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
|     | [End] Daemon | hpe-rdiscd |     |     |     |     |
| --- | ------------ | ---------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
=========================================================================
|     | [End] Feature | irdp |     |     |     |     |
| --- | ------------- | ---- | --- | --- | --- | --- |
=========================================================================
|     | Diagnostic | dump captured | for feature | irdp |     |     |
| --- | ---------- | ------------- | ----------- | ---- | --- | --- |
|     | ip irdp    |               |             |      |     |     |
Syntax
|                                         | ip irdp [broadcast | | multicast] |               |     |     |     |
| --------------------------------------- | ------------------ | ------------ | ------------- | --- | --- | --- |
|                                         | no ip irdp         |              |               |     |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |              | SwitchSeries) |     |     | 13  |

Description

Enables IRDP on an interface and specifies the packet type that is used to send advertisements. By default,
the packet type is set to multicast. IRDP is only supported on layer 3 interfaces.

The no form of this command disables IRDP on an interface.

Command context

config-if

Parameters

broadcast

Advertisements are sent as broadcast packets to IP address 255.255.255.255.

multicast

Advertisements are sent as multicast packets to the multicast group with IP address 24.0.0.1. Default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling IRDP on interface 1/1/1 with packet type set to the default value (multicast).

switch(config)# interface 1/1/1
switch(config-if)# ip irdp

Enabling IRDP on interface 1/1/1 with packet type set to broadcast.

switch(config)# interface 1/1/1
switch(config-if)# ip irdp broadcast

Disabling IRDP.

switch(config)# interface 1/1/1
switch(config-if)# no ip irdp

ip irdp holdtime

Syntax

ip irdp holdtime <TIME>

Description

Specifies the maximum amount of time the host will consider an advertisement to be valid until a newer
advertisement arrives. When a new advertisement arrives, hold time is reset. Hold time must be greater
than or equal to the maximum advertisement interval. Therefore, if the hold time for an advertisement
expires, the host can reasonably conclude that the router interface that sent the advertisement is no longer
available. The default hold time is three times the maximum advertisement interval.

Command context

config-if

IRDP | 14

Parameters
<TIME>
Specifiesthelifetimeofrouteradvertisementssentfromthisinterface.Range:4to9000seconds.
Default:1800seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Settingtheholdtimeforinterface1/1/1to5000seconds:
|     | switch(config)#           | interface | 1/1/1    |      |     |
| --- | ------------------------- | --------- | -------- | ---- | --- |
|     | switch(config-if)#        | ip irdp   | holdtime | 5000 |     |
|     | ip irdp maxadvertinterval |           |          |      |     |
Syntax
|     | ip irdp maxadvertinterval |     | <TIME> |     |     |
| --- | ------------------------- | --- | ------ | --- | --- |
Description
Specifiesthemaximumrouteradvertisementinterval.
Commandcontext
config-if
Parameters
<TIME>
Specifiesthemaximumtimeallowedbetweenthesendingofunsolicitedrouteradvertisements.Range:4
to1800seconds.Default:600seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Settingtheadvertisementintervalforinterface1/1/1to30seconds:
|     | switch(config)#           | interface | 1/1/1             |     |     |
| --- | ------------------------- | --------- | ----------------- | --- | --- |
|     | switch(config-if)#        | ip irdp   | maxadvertinterval | 30  |     |
|     | ip irdp minadvertinterval |           |                   |     |     |
Syntax
|     | ip irdp minadvertinterval |     | <TIME> |     |     |
| --- | ------------------------- | --- | ------ | --- | --- |
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 15  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

Specifies the minimum amount of time the switch waits between sending router advertisements. By
default, this value is automatically set by the switch to be 75% of the value configured for maximum router
advertisement interval. Use this command to override the automatically configured value.

Command context

config-if

Parameters

<TIME>

Specifies the minimum time allowed between the sending of unsolicited router advertisements. Range: 3
to 1800 seconds. Default: 450 seconds (75% of the default value for maximum router advertisement
interval).

Authority

Administrators or local user group members with execution rights for this command.

Example

On the 6400 Switch Series, interface identification differs.

Setting the minimum advertisement interval for interface 1/1/1 to 25 seconds:

switch(config)# interface 1/1/1
switch(config-if)# ip irdp minadvertinterval 25

ip irdp preference

Syntax

ip irdp preference <LEVEL>

Description

Specifies the IRDP preference level. If a host receives multiple router advertisement messages from
different routers, the host selects the router that sent the message with the highest preference as the
default gateway.

Command context

config-if

Parameters

<LEVEL>

Specifies the IRDP preference level. Range: -2147483648 to 2147483647. Default: 0.

Authority

Administrators or local user group members with execution rights for this command.

Example

On the 6400 Switch Series, interface identification differs.

Setting the IRDP preference level for interface 1/1/1 to 25.

IRDP | 16

|     | switch(config)# | interface | 1/1/1 |     |     |     |
| --- | --------------- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|     |         |      | ip irdp preference | 25  |     |     |
| --- | ------- | ---- | ------------------ | --- | --- | --- |
|     | show ip | irdp |                    |     |     |     |
Syntax
|     | show ip irdp | [vsx-peer] |     |     |     |     |
| --- | ------------ | ---------- | --- | --- | --- | --- |
Description
DisplaysIRDPconfigurationsettings.
Commandcontext
Manager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
switch#
show ip irdp
|     | ICMP Router | Discovery | Protocol |     |     |     |
| --- | ----------- | --------- | -------- | --- | --- | --- |
Interface Status Advertising Minimum Maximum Holdtime Preference
|     |     |     | Address | Interval Interval |     |     |
| --- | --- | --- | ------- | ----------------- | --- | --- |
--------- -------- ----------- -------- -------- -------- -----------
|                                         | 1/1/1 | Enabled  | multicast     | 6 8     | 10 10    |     |
| --------------------------------------- | ----- | -------- | ------------- | ------- | -------- | --- |
|                                         | 1/1/2 | Disabled | multicast     | 450 600 | 1800 0   |     |
|                                         | 1/1/3 | Enabled  | broadcast     | 450 600 | 1800 115 |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |       |          | SwitchSeries) |         |          | 17  |

Chapter 3
IPv6 Router Advertisement
| IPv6 | Router Advertisement |     |     |     |     |     |
| ---- | -------------------- | --- | --- | --- | --- | --- |
IPV6RAprovidesamethodforlocalIPV6hoststoautomaticallyconfiguretheirownIPaddress(andother
settingssuchasapreferredDNSserver)basedoninformationadvertisedbyswitches/routersoperatingon
thenetwork.
IPv6flags
BehaviorofIPv6hoststoIPv6RAmessagesiscontrolledbythemanagedaddressconfigurationflag(M
flag),andotherstatefulconfigurationflag(Oflag).
| M   | flag | O flag |     | Description                                              |     |     |
| --- | ---- | ------ | --- | -------------------------------------------------------- | --- | --- |
| 0   |      | 0      |     | IndicatesthatnoinformationisavailableviaDHCPv6.          |     |     |
| 0   |      | 1      |     | Indicatesthatotherconfigurationinformationisavailablevia |     |     |
DHCPv6.ExamplesofsuchinformationareDNS-related
informationorinformationonotherserverswithinthenetwork.
| 1   |     | 0   |     | IndicatesthataddressesareavailableviaDynamicHost |     |     |
| --- | --- | --- | --- | ------------------------------------------------ | --- | --- |
ConfigurationProtocol(DHCPv6).
| 1   |     | 1   |     | IftheMflagisset,theOflagisredundantandcanbeignored |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | --- |
becauseDHCPv6willreturnallavailableconfiguration
information.
| Configuring |     | IPv6 RA |     |     |     |     |
| ----------- | --- | ------- | --- | --- | --- | --- |
Procedure
1. EnabletransmissionofIPv6routeradvertisementswiththecommandno ipv6 nd suppress-ra.
2. Optionally,configureIPv6unicastaddressprefixeswiththecommandipv6 prefix.
nd
3. Optionally,configuresupportforDNSnameresolutionwiththecommandsipv6 nd ra dns server
|     | andipv6 | nd ra dns search-list. |     |     |     |     |
| --- | ------- | ---------------------- | --- | --- | --- | --- |
4. Formostdeployments,thedefaultvaluesforthefollowingfeaturesdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
|     | IPv6 RAsetting                    |     |     | Default value | Commandtochange   | it  |
| --- | --------------------------------- | --- | --- | ------------- | ----------------- | --- |
|     | Numberofneighborsolicitationstobe |     |     | 1             | ipv6nddadattempts |     |
sentwhenperformingDAD.
|     | NumberofneighborentriesintheND |     |     | 131072 | ipv6 nd cache-limit |     |
| --- | ------------------------------ | --- | --- | ------ | ------------------- | --- |
cache.
|     | HoplimittobesentintheRAmessages. |     |     | 64  | ipv6 nd hop-limit |     |
| --- | -------------------------------- | --- | --- | --- | ----------------- | --- |
18
| AOS-CX10.07IPServicesGuide| |     | (6300and6400 | SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------ | ------------- | --- | --- | --- |

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
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexamplecreatesthefollowingconfiguration:
n EnablesIPV6RAoninterface1/1/3.
n SetstherecursiveDNSserveraddressto4001::1withalifetimeof400seconds.
n Setstheminimumintervalbetweentransmissionsto3seconds.
Setsthemaximumintervalbetweentransmissionsto13seconds.
n
Setsthelifetimeofadefaultrouterto1900seconds.
n
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
| 2006::1/64      | [VALID]              |                             |        |         |     |     |
| --------------- | -------------------- | --------------------------- | ------ | ------- | --- | --- |
| IPv6 link-local | address:             | fe80::98f2:b321:368:6dc6/64 |        | [VALID] |     |     |
| ICMPv6 active   | timers:              |                             |        |         |     |     |
| Last            | Router-Advertisement | sent:                       | 0 Secs |         |     |     |
IPv6RouterAdvertisement|19

|     |           | Next                 | Router-Advertisement |             |           |                | sent in:       | 13 Secs     |     |
| --- | --------- | -------------------- | -------------------- | ----------- | --------- | -------------- | -------------- | ----------- | --- |
|     |           | Router-Advertisement |                      |             |           | parameters:    |                |             |     |
|     |           | Periodic             |                      | interval:   |           | 3 to           | 13 secs        |             |     |
|     |           | Router               |                      | Preference: |           | medium         |                |             |     |
|     |           | Send                 | "Managed             |             | Address   |                | Configuration" | flag: false |     |
|     |           | Send                 | "Other               |             | Stateful  | Configuration" |                | flag: false |     |
|     |           | Send                 | "Current             |             | Hop       | Limit"         | field: 64      |             |     |
|     |           | Send                 | "MTU"                | option      |           | value:         | 1500           |             |     |
|     |           | Send                 | "Router              |             | Lifetime" |                | field: 1900    |             |     |
|     |           | Send                 | "Reachable           |             | Time"     |                | field: 0       |             |     |
|     |           | Send                 | "Retrans             |             | Timer"    | field:         | 0              |             |     |
|     |           | Suppress             |                      | RA:         | false     |                |                |             |     |
|     |           | Suppress             |                      | MTU         | in RA:    | true           |                |             |     |
|     |           | ICMPv6               | error                | message     |           | parameters:    |                |             |     |
|     |           | Send                 | redirects:           |             | false     |                |                |             |     |
|     |           | ICMPv6               | DAD                  | parameters: |           |                |                |             |     |
|     |           | Current              |                      | DAD         | attempt:  | 1              |                |             |     |
|     | switch#   |                      | show                 | ipv6        | nd ra     | dns            | server         |             |     |
|     | Recursive |                      | DNS                  | Server      | List      | on:            | 1/1/3          |             |     |
|     |           | Suppress             |                      | DNS         | Server    | List:          | No             |             |     |
|     |           | DNS                  | Server               | 1:          | 2001::1   |                | lifetime       | 400         |     |
|     | IPv6      | RA                   | scenario             |             |           |                |                |             |     |
Inthisscenario,twohostcomputersareauto-configuredwithIPaddressesusingIPv6RA.Inaddition,the
switchprovidesthehostswithanaddressofarecursiveDNSserver.Thephysicaltopologyofthenetwork
lookslikethis:
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. ConfiguretheinterfaceswithIPv6addresses.
|     |     | switch#            | config |     |           |         |            |     |     |
| --- | --- | ------------------ | ------ | --- | --------- | ------- | ---------- | --- | --- |
|     |     | switch(config)#    |        |     | interface |         | 1/1/1      |     |     |
|     |     | switch(config-if)# |        |     | ipv6      | address | 2001::1/64 |     |     |
|     |     | switch(config)#    |        |     | interface |         | 1/1/2      |     |     |
|     |     | switch(config-if)# |        |     | ipv6      | address | 3001::1/64 |     |     |
|     |     | switch(config)#    |        |     | interface |         | 1/1/3      |     |     |
|     |     | switch(config-if)# |        |     | ipv6      | address | 4001::1/64 |     |     |
2. EnabletransmissionofallIPv6RAmessages.
|                                         |     | switch(config-if)# |     |     | no  | ipv6          | nd suppress-ra |     |     |
| --------------------------------------- | --- | ------------------ | --- | --- | --- | ------------- | -------------- | --- | --- |
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |                    |     |     |     | SwitchSeries) |                |     | 20  |

| IPv6 RA commands |                          |     |     |
| ---------------- | ------------------------ | --- | --- |
| ipv6 address     | <global-unicast-address> |     |     |
Syntax
| ipv6 address <global-unicast-address> |                          |     |     |
| ------------------------------------- | ------------------------ | --- | --- |
| no ipv6 address                       | <global-unicast-address> |     |     |
Description
Setsaglobalunicastaddressontheinterface.
Thenoformofthiscommandremovestheglobalunicastaddressontheinterface.
ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotaddthe
ipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,thelink-local
addressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6 address
link-localcommand.
Commandcontext
config-if
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Enablingaglobalunicastaddress:
| switch(config)#    | interface | 1/1/1   |                    |
| ------------------ | --------- | ------- | ------------------ |
| switch(config-if)# | ipv6      | address | 3731:54:65fe:2::a7 |
Disablingaglobalunicastaddress:
| switch(config)#    | interface  | 1/1/1        |                    |
| ------------------ | ---------- | ------------ | ------------------ |
| switch(config-if)# | no         | ipv6 address | 3731:54:65fe:2::a7 |
| ipv6 address       | autoconfig |              |                    |
Syntax
| ipv6 address autoconfig |            |     |     |
| ----------------------- | ---------- | --- | --- |
| no ipv6 address         | autoconfig |     |     |
Description
EnablestheinterfacetoautomaticallyobtainanIPv6addressusingrouteradvertisementinformationand
theEUI-64identifier.
Thenoformofthiscommanddisablesaddressauto-configuration.
IPv6RouterAdvertisement|21

Amaximumof15autoconfiguredaddressesaresupported.
n
n ThiscommandautomaticallycreatesanIPv6link-localaddressontheinterface.However,itdoesnotadd
theipv6 address link-localcommandtotherunningconfiguration.IfyouremovetheIPv6address,the
link-localaddressisalsoremoved.Tomaintainthelink-localaddress,youmustmanuallyexecutetheipv6
|     | address | link-localcommand. |     |     |     |     |
| --- | ------- | ------------------ | --- | --- | --- | --- |
Commandcontext
config-if
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
TheIPv6SLAACfeatureletstherouterobtaintheIPv6addressfortheinterfaceitisconfiguredthroughthe
SLAACmethod.ThisfeatureisnotavailableonthemgmtVRF.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Enablingunicastautoconfiguring:
|     | switch(config)#    |     | interface | 1/1/1   |            |     |
| --- | ------------------ | --- | --------- | ------- | ---------- | --- |
|     | switch(config-if)# |     | ipv6      | address | autoconfig |     |
Disablingunicastautoconfiguring:
|     | switch(config)#    |            | interface | 1/1/1   |            |     |
| --- | ------------------ | ---------- | --------- | ------- | ---------- | --- |
|     | switch(config-if)# |            | no ipv6   | address | autoconfig |     |
|     | ipv6 address       | link-local |           |         |            |     |
Syntax
|     | ipv6 address | link-local | [<IPV6-ADDR>/<MASK>] |     |     |     |
| --- | ------------ | ---------- | -------------------- | --- | --- | --- |
Description
EnablesIPv6onthecurrentinterface.Ifnoaddressisspecified,anIPv6link-localaddressisauto-generated
fortheinterface.Ifanaddressisspecified,auto-configurationisdisabledandthespecifiedaddress/maskis
assignedtotheinterface.
TodisableIPv6link-localontheinterface,removeipv6 address link-local,ipv6 address <global-
|     | ipv6-address>,andipv6 |     | address | autoconfigfromtheinterface. |     |     |
| --- | --------------------- | --- | ------- | --------------------------- | --- | --- |
ThisfeatureisnotavailableonthemanagementVRF.
Commandcontext
config-if
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) |     | 22  |
| --------------------------------------- | --- | --- | --- | ------------- | --- | --- |

Parameters

<IPV6-ADDR>

Specifies the IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. You can use two colons (::) to represent consecutive zeros (but only
once), remove leading zeros, and collapse a hextet of four zeros to a single 0. For example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes 2222:0:3333::4444:55.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 128.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

On the 6400 Switch Series, interface identification differs.

Enabling IPv6 link-local on the interface:

switch(config)# interface 1/1/1
switch(config-if)# ipv6 address link-local

ipv6 nd cache-limit

Syntax

ipv6 nd cache-limit <CACHELIMIT>
no ipv6 nd cache-limit [<CACHELIMIT>]

Description

Configures the limit on the number of neighbor entries in the ND cache.

The no form of this command sets the cache limit to the default value.

Command context

config

Parameters

<CACHELIMIT>

Specifies the neighbor cache entries limit. Range: 1-131072. Default: 131072.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the cache limit to 20.

switch(config)# ipv6 nd cache-limit 20

ipv6 nd dad attempts

IPv6 Router Advertisement | 23

Syntax
|     | ipv6 nd dad attempts    | <NUM-ATTEMPTS>   |     |     |
| --- | ----------------------- | ---------------- | --- | --- |
|     | no ipv6 nd dad attempts | [<NUM-ATTEMPTS>] |     |     |
Description
Configuresthenumberofneighborsolicitationstobesentwhenperformingduplicateaddressdetection
(DAD)foraunicastaddressconfiguredonaninterface.
Thenoformofthiscommandsetsthenumberofattemptstothedefaultvalue.
Commandcontext
config-if
Parameters
|     | dad attempts <NUM-ATTEMPTS> |     |     |     |
| --- | --------------------------- | --- | --- | --- |
Specifiesthenumberofneighborsolicitationstosend.Range:0-15.Default:1.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch(config)#    | interface | 1/1/1             |     |
| --- | ------------------ | --------- | ----------------- | --- |
|     | switch(config-if)# | ipv6      | nd dad attempts 5 |     |
|     | ipv6 nd hop-limit  |           |                   |     |
Syntax
|     | ipv6 nd hop-limit    | <HOPLIMIT>   |     |     |
| --- | -------------------- | ------------ | --- | --- |
|     | no ipv6 nd hop-limit | [<HOPLIMIT>] |     |     |
Description
ConfiguresthehoplimittobesentinRAs.
Thenoformofthiscommandresetsthehoplimitto0.ThisreseteliminatesthehoplimitfromtheRAsthat
originateontheinterface,sothehostdeterminesthehoplimit.
Commandcontext
config-if
Parameters
|     | hop-limit <HOPLIMIT> |     |     |     |
| --- | -------------------- | --- | --- | --- |
Specifiesthehoplimit.Range:0-255.Default:64.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 24  |
| --------------------------------------- | --- | --- | ------------- | --- |

| switch(config)# |     | interface | 1/1/1 |
| --------------- | --- | --------- | ----- |
switch(config-if)#
|         |     | ipv6 | nd hop-limit 64 |
| ------- | --- | ---- | --------------- |
| ipv6 nd | mtu |      |                 |
Syntax
| ipv6 nd | mtu <MTU-VALUE>      |     |     |
| ------- | -------------------- | --- | --- |
| no ipv6 | nd mtu [<MTU-VALUE>] |     |     |
Description
ConfigurestheMTUsizetobesentintheRAmessages.
Thenoformofthiscommandsetshoplimittothedefaultvalue.
Commandcontext
config-if
Parameters
<MTU-VALUE>
SpecifiestheMTUsize.Range:1280-65535bytes.Default:1500bytes.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |             | interface | 1/1/1       |
| ------------------ | ----------- | --------- | ----------- |
| switch(config-if)# |             | ipv6      | nd mtu 1300 |
| ipv6 nd            | ns-interval |           |             |
Syntax
| ipv6 nd | ns-interval    | <TIME>   |     |
| ------- | -------------- | -------- | --- |
| no ipv6 | nd ns-interval | [<TIME>] |     |
Description
ConfigurestheNDtimebetweenDADneighborsolicitationssentforanunresolveddestination,orbetween
duplicateaddressdetectionneighborsolicitationrequests.Increasethissettingwhenneighborsolicitation
retriesorfailuresareoccurring,orinaslow(WAN)network.
Thenoformofthiscommandsetsthens-intervaltothedefaultvalue.
Commandcontext
config-if
Parameters
<TIME>
Specifiestheneighborsolicitationinterval.Range:1000-3600000milliseconds.Default:1000
milliseconds.
IPv6RouterAdvertisement|25

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     |      | switch(config)#    |        | interface | 1/1/1          |     |      |     |     |
| --- | ---- | ------------------ | ------ | --------- | -------------- | --- | ---- | --- | --- |
|     |      | switch(config-if)# |        | ipv6      | nd ns-interval |     | 1200 |     |     |
|     | ipv6 | nd                 | prefix |           |                |     |      |     |     |
Syntax
|     | ipv6 | nd                | prefix <IPV6-ADDR>/<PREFIX-LEN> |                          |                  |               |                  |                  |     |
| --- | ---- | ----------------- | ------------------------------- | ------------------------ | ---------------- | ------------- | ---------------- | ---------------- | --- |
|     |      | [no-advertise     |                                 | | [valid                 | <LIFETIME-VALUE> |               | preferred        |                  |     |
|     |      | <LIFETIME-VALUE>] |                                 | | no-autoconfig          |                  |               | | no-onlink]     |                  |     |
|     | no   | ipv6              | nd prefix                       | <IPV6-ADDR>/<PREFIX-LEN> |                  |               | [no-advertise    |                  |     |
|     |      | | [valid          | <LIFETIME-VALUE>                |                          | preferred        |               | <LIFETIME-VALUE> |                  |     |
|     |      | ] |               | no-autoconfig                   | | no-onlink]             |                  |               |                  |                  |     |
|     | ipv6 | nd                | prefix default                  | [no-advertise            |                  | |             | [valid           | <LIFETIME-VALUE> |     |
|     |      | preferred         | <LIFETIME-VALUE>]               |                          | |                | no-autoconfig |                  | | no-onlink]}    |     |
no ipv6 nd prefix default [no-advertise | [valid <LIFETIME-VALUE>
|     |     | preferred | <LIFETIME-VALUE>] |     | |   | no-autoconfig |     | | no-onlink]} |     |
| --- | --- | --------- | ----------------- | --- | --- | ------------- | --- | ------------- | --- |
Description
SpecifiesprefixesfortheroutingswitchtoincludeinRAstransmittedontheinterface.IPv6hostsusethe
prefixesinRAstoautoconfigurethemselveswithglobalunicastaddresses.Theautoconfiguredaddressofa
hostiscomposedoftheadvertisedprefixandtheinterfaceidentifierinthecurrentlink-localaddressofthe
host.
Bydefault,advertise,autoconfig,andonlinkareset.
Thenoformofthiscommandremovestheconfigurationontheinterface.
Commandcontext
config-if
Parameters
<IPV6-ADDR>/<PREFIX-LEN>
SpecifiestheIPv6prefixtoadvertiseinRA.Format:X:X::X:X/M
default
Specifiesapplyconfigurationtoallon-linkprefixesthatarenotindividuallysetbytheipv6 ra prefix
<IPV6-ADDR>/<PREFIX-LEN>command.Itappliesthesamevalidandpreferredlifetimes,linkstate,
autoconfigurationstate,andadvertiseoptionstotheadvertisementssentforallon-linkprefixesthatare
notindividuallyconfiguredwithauniquelifetime.Thisalsoappliestotheprefixesforanyglobalunicast
addressesconfiguredlateronthesameinterface.
Usingdefaultonce,andthenusingitagainwithanynewparametervaluesresultsinthenewvalues
replacingtheformervaluesinadvertisements.Ifdefaultisusedwithouttheno–advertise,no–
autoconfig,orno-onlinkparameter,theadvertisementsettingfortheabsentparameterisreturnedto
itsdefaultsetting.
no-advertise
SpecifiesdonotadvertiseprefixinRA.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     |     | SwitchSeries) |     |     |     | 26  |
| --------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |

valid <LIFETIME-VALUE>

Specifies the total time, in seconds, the prefix remains available before becoming unusable. After
preferred-lifetime expiration, any autoconfigured address is deprecated and used only for transactions
only before preferred-lifetime expires. If the valid lifetime expires, the address becomes invalid.

You can enter a value in seconds or enter valid infinite which sets infinite lifetime. Default: 2,592,000
seconds which is 30 days. Range: 0–4294967294 seconds.

preferred <LIFETIME-VALUE>

Specifies the span of time during which the address can be freely used as a source and destination for
traffic. This setting must be less than or equal to the corresponding valid–lifetime setting.

You can enter a value in seconds or enter preferred infinite which sets infinite lifetime. Default:
604,800 seconds which is seven days. Range: 0–4294967294 seconds.

no-autoconfig

Specifies do not use prefix for autoconfiguration.

no-onlink

Specifies do not use prefix for onlink determination.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd prefix 4001::1/64 valid 30 preferred 10 no-autoconfig no-
onlink

ipv6 nd ra dns search-list

Syntax

ipv6 nd ra dns search-list <DOMAIN-NAME> [lifetime <TIME>]
no ipv6 nd ra dns search-list <DOMAIN-NAME>

Description

Configures the DNS Search List (DNSSL) to include in Router Advertisements (RAs) transmitted on the
interface.

The no form of this command removes the DNS Search List from the RAs transmitted on the interface.

Command context

config-if

Parameters

<DOMAIN-NAME>

Specifies the domain names for DNS queries.

lifetime <TIME>

Specifies lifetime in seconds. Range: 4-4294967295 seconds. Default: 1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

IPv6 Router Advertisement | 27

n DNSSL contains the domain names of DNS suffixes or IPv6 hosts to append to short, unqualified domain

names for DNS queries.

n Multiple DNS domain names can be added to the DNSSL by using the command repeatedly.

n A maximum of eight server addresses are allowed.

Examples

On the 6400 Switch Series, interface identification differs.

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra dns search-list test.com lifetime 500

ipv6 nd ra dns server

Syntax

ipv6 nd ra dns server <IPV6-ADDR> [lifetime <TIME>]
no ipv6 nd ra dns server <IPV6-ADDR>

Description

Configures the IPv6 address of a preferred Recursive DNS Server (RDNSS) to be included in Router
Advertisements (RAs) transmitted on the interface.

The no form of this command removes the configured DNS server from the RAs transmitted on the
interface.

Command context

config-if

Parameters

<IPV6-ADDR>

Specifies the RDNSS address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. You can use two colons (::) to represent consecutive zeros (but only
once), remove leading zeros, and collapse a hextet of four zeros to a single 0. For example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes 2222:0:3333::4444:55.

lifetime <TIME>

Specifies IPv6 DNS server lifetime in seconds. Range: 4-4294967295 seconds. Default: 1800 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n Including RDNSS information in RAs provides DNS server configuration for connected IPv6 hosts without

requiring DHCPv6.

n Multiple servers can be configured on the interface by using the command repeatedly.

n A maximum of eight server addresses are allowed.

Examples

On the 6400 Switch Series, interface identification differs.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

28

| switch(config)# |     | interface 1/1/1 |     |     |     |
| --------------- | --- | --------------- | --- | --- | --- |
switch(config-if)#
|         |             | ipv6 nd | ra dns server | 2001::1 lifetime | 400 |
| ------- | ----------- | ------- | ------------- | ---------------- | --- |
| ipv6 nd | ra lifetime |         |               |                  |     |
Syntax
| ipv6 nd | ra lifetime    | <TIME>   |     |     |     |
| ------- | -------------- | -------- | --- | --- | --- |
| no ipv6 | nd ra lifetime | [<TIME>] |     |     |     |
Description
Configuresthelifetime,inseconds,fortheroutingswitchtobeusedasadefaultrouterbyhostsonthe
currentinterface.
Thenoformofthiscommandsetslifetimetothedefaultof1800seconds.
Commandcontext
config-if
Parameters
<TIME>
Specifieslifetimeinsecondsofadefaultrouter.Asettingof0fordefaultrouterlifetimeinanRA
indicatesthattheroutingswitchisnotadefaultrouterontheinterface.Range:0-9000seconds.
Default:1800seconds.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n Agivenhostonaninterfacerefreshesthedefaultrouterlifetimeforaspecificroutereachtimethehost
receivesanRAfromthatrouter.
n Aspecificrouterceasestobeadefaultroutercandidateforagivenhostifthedefaultrouterlifetime
expiresbeforethehostisupdatedwithanewRAfromtherouter.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |                        | interface 1/1/1 |             |      |     |
| ------------------ | ---------------------- | --------------- | ----------- | ---- | --- |
| switch(config-if)# |                        | ipv6 nd         | ra lifetime | 1200 |     |
| ipv6 nd            | ra managed-config-flag |                 |             |      |     |
Syntax
| ipv6 nd | ra managed-config-flag    |     |     |     |     |
| ------- | ------------------------- | --- | --- | --- | --- |
| no ipv6 | nd ra managed-config-flag |     |     |     |     |
Description
ControlstheMflagsettinginRAstheroutertransmitsonthecurrentinterface.EnabletheMflagtoindicate
thathostscanobtainIPaddressthroughDHCPv6.TheMflagisdisabledbydefault.
Thenoformofthiscommandturnsoff(disables)theMflag.
IPv6RouterAdvertisement|29

Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n EnablingtheMflagdirectshoststoacquiretheirIPv6addressingforthecurrentinterfacefroma
DHCPv6server.
n WhentheM-bitisenabled,receivinghostsignoretheOflagsetting,whichisconfiguredusingthe
|     | commandipv6 |     | nd ra other-config-flag. |     |     |     |
| --- | ----------- | --- | ------------------------ | --- | --- | --- |
WhentheM-bitisdisabled(thedefault),receivinghostsexpecttoreceivetheirIPv6addressesfromRA.
n
|     | M flag |     | O   | flag | Description                                              |     |
| --- | ------ | --- | --- | ---- | -------------------------------------------------------- | --- |
|     | 0      |     | 0   |      | IndicatesthatnoinformationisavailableviaDHCPv6.          |     |
|     | 0      |     | 1   |      | Indicatesthatotherconfigurationinformationisavailablevia |     |
DHCPv6.ExamplesofsuchinformationareDNS-related
informationorinformationonotherserverswithinthenetwork.
|     | 1   |     | 0   |     | IndicatesthataddressesareavailableviaDynamicHost |     |
| --- | --- | --- | --- | --- | ------------------------------------------------ | --- |
ConfigurationProtocol(DHCPv6).
|     | 1   |     | 1   |     | IftheMflagisset,theOflagisredundantandcanbeignored |     |
| --- | --- | --- | --- | --- | -------------------------------------------------- | --- |
becauseDHCPv6willreturnallavailableconfiguration
information.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch(config)#    |                 | interface | 1/1/1 |                        |     |
| --- | ------------------ | --------------- | --------- | ----- | ---------------------- | --- |
|     | switch(config-if)# |                 | ipv6      | nd    | ra managed-config-flag |     |
|     | ipv6 nd            | ra max-interval |           |       |                        |     |
Syntax
|     | ipv6 nd | ra max-interval    |     | <TIME>   |     |     |
| --- | ------- | ------------------ | --- | -------- | --- | --- |
|     | no ipv6 | nd ra max-interval |     | [<TIME>] |     |     |
Description
ConfiguresthemaximumintervalbetweentransmissionsofIPv6RAsontheinterface.Theintervalbetween
RAtransmissionsonaninterfaceisarandomvaluethatchangeseverytimeanRAissent.Theintervalis
calculatedtobeavaluebetweenthecurrentmax-intervalandmin-intervalsettings.
Thenoformofthiscommandreturnsthesettingtoitsdefault,providedthedefaultvalueislessthanthe
defaultlifetimevalue.
Commandcontext
config-if
Parameters
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) |     | 30  |
| --------------------------------------- | --- | --- | --- | ------------- | --- | --- |

<TIME>

Specifies the maximum advertisement time in seconds. Range: 4-1800. Default: 600 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n This value has one setting per interface. The setting does not apply to RAs sent in response to a router

solicitation received from another device.

n Attempting to set max-interval to a value that is not sufficiently larger than the current min-interval also

results in an error message.

Examples

On the 6400 Switch Series, interface identification differs.

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd ra max-interval 30

ipv6 nd ra min-interval

Syntax

ipv6 nd ra min-interval <TIME>
no ipv6 nd ra min-interval [<TIME>]

Description

Configures the minimum interval between transmissions of IPv6 RAs on the interface. The interval between
RA transmissions on an interface is a random value that changes every time an RA is sent. The interval is
calculated to be a value between the current max-interval and min-interval settings.

The no form of this command returns the setting to its default, provided the default value is less than the
current max-interval setting.

Command context

config-if

Parameters

<TIME>

Specifies a minimum advertisement time in seconds. Range: 3-1350. Default: 200 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n This value has one setting per interface and does not apply to RAs sent in response to a router

solicitation received from another device.

n The min-interval must be less than the max-interval. Attempting to set min-interval to a higher value

results in an error message.

Examples

IPv6 Router Advertisement | 31

Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch(config)#              | interface | 1/1/1              |     |     |
| --- | ---------------------------- | --------- | ------------------ | --- | --- |
|     | switch(config-if)#           | ipv6      | nd ra min-interval | 25  |     |
|     | ipv6 nd ra other-config-flag |           |                    |     |     |
Syntax
|     | ipv6 nd ra other-config-flag    |     |     |     |     |
| --- | ------------------------------- | --- | --- | --- | --- |
|     | no ipv6 nd ra other-config-flag |     |     |     |     |
Description
ControlstheO-bitinRAstheroutertransmitsonthecurrentinterface;butisignoredunlesstheM-bitis
disabledinRAs.ConfiguretosettheO-bitinRAmessagesforhosttoobtainnetworkparametersthrough
DHCPv6.Theother-config-flagisdisabledbydefault.
FormoreinformationonconfiguringtheM-bit,see ipv6 nd ra managed-config-flag.
Thenoformofthiscommandturnsoff(disables)thesettingforthiscommandinRAs.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
EnablingtheO-bitwhiletheM-bitisdisableddirectshostsontheinterfacetoacquiretheirother
configurationinformationfromDHCPv6.ExamplesofsuchinformationareDNS-relatedinformationor
informationonotherserverswithinthenetwork.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch(config)# | interface | 1/1/1 |     |     |
| --- | --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|     |                           | ipv6 | nd ra other-config-flag |     |     |
| --- | ------------------------- | ---- | ----------------------- | --- | --- |
|     | ipv6 nd ra reachable-time |      |                         |     |     |
Syntax
|     | ipv6 nd ra reachable-time    |     | <TIME>   |     |     |
| --- | ---------------------------- | --- | -------- | --- | --- |
|     | no ipv6 nd ra reachable-time |     | [<TIME>] |     |     |
Description
Setstheamountoftimethattheinterfaceconsidersadevicetobereachableafterreceivingareachability
confirmationfromthedevice.
Thenoformofthiscommandsetsthereachabletimetothedefaultvalueof0.(nolimit).
Commandcontext
config-if
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 32  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

Parameters
<TIME>
Specifiesthereachabletimeinmilliseconds.Range:1000-3600000.Default:0(nolimit).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |                  | interface | 1/1/1   |                   |     |      |
| ------------------ | ---------------- | --------- | ------- | ----------------- | --- | ---- |
| switch(config-if)# |                  |           | ipv6 nd | ra reachable-time |     | 2000 |
| ipv6 nd            | ra retrans-timer |           |         |                   |     |      |
Syntax
| ipv6 nd | ra retrans-timer    |     | <TIME>   |     |     |     |
| ------- | ------------------- | --- | -------- | --- | --- | --- |
| no ipv6 | nd ra retrans-timer |     | [<TIME>] |     |     |     |
Description
Configurestheperiod(retransmittimer)betweenNDsolicitationssentbyahostforanunresolved
destination,orbetweenDADneighborsolicitationrequests.Bydefault,hostsontheinterfaceusetheirown
locallyconfiguredNS-intervalsettingsinsteadofusingthevaluereceivedintheRAs.
Increasethistimerwhenneighborsolicitationretriesorfailuresareoccur,orina"slow"(WAN)network.
Thenoformofthiscommandsetsthevaluetothedefaultof0.
Commandcontext
config-if
Parameters
<TIME>
Specifiestheretransmittimervalueinmilliseconds.Range:0-4294967295milliseconds.Default:0(Use
locallyconfiguredNS-interval).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)#    |                   | interface | 1/1/1   |                  |     |     |
| ------------------ | ----------------- | --------- | ------- | ---------------- | --- | --- |
| switch(config-if)# |                   |           | ipv6 nd | ra retrans-timer |     | 400 |
| ipv6 nd            | router-preference |           |         |                  |     |     |
Syntax
| ipv6 nd | router-preference    |     | {high | | medium | | low} |        |
| ------- | -------------------- | --- | ----- | -------- | ------ | ------ |
| no ipv6 | nd router-preference |     | [high | | medium |        | | low] |
IPv6RouterAdvertisement|33

Description

Specifies the value that is set in the Default Router Preference (DRP) field of Router Advertisements (RAs)
that the switch sends from an interface. An interface with a DRP value of high will be preferred by other
devices on the network over interfaces with an RA value of medium or low.

The no form of this command set the value to the default of medium.

Command context

config-if

Parameters

high

Sets DRP to high.

medium

Sets DRP to medium. Default.

low

Sets DRP to low.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

switch(config)# interface 1/1/1
switch(config-if)# ipv6 nd router-preference high

ipv6 nd suppress-ra

Syntax

ipv6 nd suppress-ra [<SUPPRESS-OPTION>]
no ipv6 nd ra supress-ra [<SUPPRESS-OPTION>]

Description

Configures suppression of IPv6 Router Advertisement transmissions on an interface.

The no form of this command restores transmission of IPv6 Router Advertisement and options.

Command context

config-if

Parameters

suppress-ra [<SUPPRESS-OPTION>]

Specifies suppressing RA transmissions. Entering suppress-ra without any options, suppresses all RA
messages (default). Or you can enter one of the following options.
dnssl

Specifies suppressing DNSSL options in RA messages.

mtu

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

34

SpecifiessuppressingMTUoptionsinRAmessages.
rdnss
SpecifiessuppressingRDNSSoptionsinRAmessages.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|      | switch(config)#    |     | interface | 1/1/1   |                |           |             |
| ---- | ------------------ | --- | --------- | ------- | -------------- | --------- | ----------- |
|      | switch(config-if)# |     | ipv6      | nd      | suppress-ra    | mtu dnssl | rdnss       |
|      | switch(config-if)# |     | no        | ipv6    | nd suppress-ra | mtu       | dnssl rdnss |
| show | ipv6               | nd  | global    | traffic |                |           |             |
Syntax
| show | ipv6 nd | global | traffic | [vsx-peer] |     |     |     |
| ---- | ------- | ------ | ------- | ---------- | --- | --- | --- |
Description
DisplaysIPV6NeighborDiscoverytrafficdetailsonadevice.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
|     | switch#     | show           | ipv6 nd        | global | traffic         |      |     |
| --- | ----------- | -------------- | -------------- | ------ | --------------- | ---- | --- |
|     | ICMPv6      | packet         | Statistics     |        | (sent/received) |      |     |
|     | Total       | Messages       |                |        | :               | 18/0 |     |
|     | Error       | Messages       |                |        | :               | 0/0  |     |
|     | Destination |                | Unreachables   |        | :               | 0/0  |     |
|     | Time        | Exceeded       |                |        | :               | 0/0  |     |
|     | Parameter   |                | Problems       |        | :               | 0/0  |     |
|     | Echo        | Request        |                |        | :               | 0/0  |     |
|     | Echo        | Replies        |                |        | :               | 0/0  |     |
|     | Redirects   |                |                |        | :               | 0/0  |     |
|     | Packet      | Too            | Big            |        | :               | 0/0  |     |
|     | Router      | Advertisements |                |        | :               | 4/0  |     |
|     | Router      | Solicitations  |                |        | :               | 0/0  |     |
|     | Neighbor    |                | Advertisements |        | :               | 0/0  |     |
IPv6RouterAdvertisement|35

|     | Neighbor   | Solicitations | :               | 3/0 |     |     |
| --- | ---------- | ------------- | --------------- | --- | --- | --- |
|     | Duplicate  | router        | RA received :   | 0/0 |     |     |
|     | ICMPv6 MLD | Statistics    | (sent/received) |     |     |     |
|     | V1 Queries | :             | 0/0             |     |     |     |
|     | V2 Queries | :             | 0/0             |     |     |     |
|     | V1 Reports | :             | 0/0             |     |     |     |
|     | V2 Reports | :             | 11/0            |     |     |     |
|     | V1 Leaves  | :             | 0/0             |     |     |     |
|     | show ipv6  | nd interface  |                 |     |     |     |
Syntax
show ipv6 nd interface [<IF-NAME> | all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
Displaysneighbordiscoveryinformationforaninterface.Ifnooptionsarespecified,displaysinformation
forthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
<IF-NAME>
DisplaysinformationaboutthespecifiedIPv6enabledinterface.
all-vrfs
DisplaysinformationaboutinterfacesinallVRFs.
|     | vrf <VRF-NAME> |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
DisplaysinformationaboutinterfacesinaparticularVRF.Or,if<VRF-NAME>isnotspecified,information
forthedefaultVRFisdisplayed.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowinginformationforallVRFs:
|     | switch# show | ipv6 nd     | interface all-vrfs |     |     |     |
| --- | ------------ | ----------- | ------------------ | --- | --- | --- |
|     | List of IPv6 | Interfaces  | for VRF default    |     |     |     |
|     | Interface    | 1/1/1 is up |                    |     |     |     |
|     | Admin state  | is up       |                    |     |     |     |
IPv6 address:
|                                         | IPv6 link-local | address:             | fe80::7272:cfff:fee7:a8b9/64 |     | [VALID] |     |
| --------------------------------------- | --------------- | -------------------- | ---------------------------- | --- | ------- | --- |
|                                         | ICMPv6 active   | timers:              |                              |     |         |     |
|                                         | Last            | Router-Advertisement | sent:                        |     |         |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                 |                      | SwitchSeries)                |     |         | 36  |

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
IPv6RouterAdvertisement|37

|     |     | Send     | "MTU"           | option       | value:      |        | 1500 |     |     |     |
| --- | --- | -------- | --------------- | ------------ | ----------- | ------ | ---- | --- | --- | --- |
|     |     | Send     | "Router         |              | Lifetime"   | field: | 1800 |     |     |     |
|     |     | Send     | "Reachable      |              | Time"       | field: | 0    |     |     |     |
|     |     | Send     | "Retrans        |              | Timer"      | field: | 0    |     |     |     |
|     |     | Suppress |                 | RA:          | true        |        |      |     |     |     |
|     |     | Suppress |                 | MTU          | in RA:      | true   |      |     |     |     |
|     |     | ICMPv6   | error           | message      | parameters: |        |      |     |     |     |
|     |     | Send     | redirects:      |              | false       |        |      |     |     |     |
|     |     | ICMPv6   | DAD parameters: |              |             |        |      |     |     |     |
|     |     | Current  |                 | DAD attempt: |             | 1      |      |     |     |     |
ShowinginformationforthedefaultVRF:
|     |      | switch#              | show ipv6            | nd           | interface   |                              |           |             |         |     |
| --- | ---- | -------------------- | -------------------- | ------------ | ----------- | ---------------------------- | --------- | ----------- | ------- | --- |
|     |      | List of              | IPv6 Interfaces      |              | for         | VRF                          | default   |             |         |     |
|     |      | Interface            | 1/1/1                | is           | up          |                              |           |             |         |     |
|     |      | Admin                | state                | is up        |             |                              |           |             |         |     |
|     |      | IPv6                 | address:             |              |             |                              |           |             |         |     |
|     |      | 2001::1/64           |                      | [VALID]      |             |                              |           |             |         |     |
|     |      | IPv6                 | link-local           | address:     |             | fe80::7272:cfff:fee7:a8b9/64 |           |             | [VALID] |     |
|     |      | ICMPv6               | active               | timers:      |             |                              |           |             |         |     |
|     |      | Last                 | Router-Advertisement |              |             |                              | sent: 6   | Secs        |         |     |
|     |      | Next                 | Router-Advertisement |              |             |                              | sent in:  | 7 Secs      |         |     |
|     |      | Router-Advertisement |                      |              | parameters: |                              |           |             |         |     |
|     |      | Periodic             |                      | interval:    |             | 3 to 13                      | secs      |             |         |     |
|     |      | Router               | Preference:          |              |             | medium                       |           |             |         |     |
|     |      | Send                 | "Managed             |              | Address     | Configuration"               |           | flag: false |         |     |
|     |      | Send                 | "Other               | Stateful     |             | Configuration"               |           | flag: false |         |     |
|     |      | Send                 | "Current             |              | Hop Limit"  |                              | field: 64 |             |         |     |
|     |      | Send                 | "MTU"                | option       | value:      |                              | 1500      |             |         |     |
|     |      | Send                 | "Router              |              | Lifetime"   | field:                       | 1900      |             |         |     |
|     |      | Send                 | "Reachable           |              | Time"       | field:                       | 0         |             |         |     |
|     |      | Send                 | "Retrans             |              | Timer"      | field:                       | 0         |             |         |     |
|     |      | Suppress             |                      | RA:          | true        |                              |           |             |         |     |
|     |      | Suppress             |                      | MTU          | in RA:      | true                         |           |             |         |     |
|     |      | ICMPv6               | error                | message      | parameters: |                              |           |             |         |     |
|     |      | Send                 | redirects:           |              | false       |                              |           |             |         |     |
|     |      | ICMPv6               | DAD parameters:      |              |             |                              |           |             |         |     |
|     |      | Current              |                      | DAD attempt: |             | 1                            |           |             |         |     |
|     | show | ipv6                 | nd                   | interface    |             | prefix                       |           |             |         |     |
Syntax
show ipv6 nd interface prefix [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
ShowsIPv6prefixinformationforallVRFsoraspecificVRF.Ifnooptionsarespecified,showsinformation
forthedefaultVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
ShowsprefixinformationforallVRFs.
|                                         | vrf | <VRF-NAME> |     |     |     |               |     |     |     |     |
| --------------------------------------- | --- | ---------- | --- | --- | --- | ------------- | --- | --- | --- | --- |
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |            |     |     |     | SwitchSeries) |     |     |     | 38  |

NameofaVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingprefixinformationforthedefaultVRF:
|     | switch#    | show        | ipv6 nd           | interface | prefix      |     |
| --- | ---------- | ----------- | ----------------- | --------- | ----------- | --- |
|     | List of    | IPv6        | Interfaces        | for       | VRF default |     |
|     | List of    | IPv6        | Prefix advertised |           | on 1/1/1    |     |
|     | Prefix     | : 4545::/65 |                   |           |             |     |
|     | Enabled    | :           | Yes               |           |             |     |
|     | Validlife  |             | time : 2592000    |           |             |     |
|     | Preferred  |             | lifetime          | : 604800  |             |     |
|     | On-link    | :           | Yes               |           |             |     |
|     | Autonomous |             | : Yes             |           |             |     |
ShowinginformationforVRFred:
|      | switch#    | show        | ipv6 nd           | interface   | prefix vrf | red |
| ---- | ---------- | ----------- | ----------------- | ----------- | ---------- | --- |
|      | List of    | IPv6        | Interfaces        | for         | VRF red    |     |
|      | List of    | IPv6        | Prefix advertised |             | on 1/1/2   |     |
|      | Prefix     | : 2001::/64 |                   |             |            |     |
|      | Enabled    | :           | Yes               |             |            |     |
|      | Validlife  |             | time : 2592000    |             |            |     |
|      | Preferred  |             | lifetime          | : 604800    |            |     |
|      | On-link    | :           | Yes               |             |            |     |
|      | Autonomous |             | : Yes             |             |            |     |
| show | ipv6       | nd          | ra dns            | search-list |            |     |
Syntax
| show | ipv6 nd | ra dns | search-list |     | [vsx-peer] |     |
| ---- | ------- | ------ | ----------- | --- | ---------- | --- |
Description
Displaysdomainnameinformationonallinterfaces.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
IPv6RouterAdvertisement|39

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch(config)#    |          |        | interface |          | 1/1/1  |                 |      |          |     |
| --- | ------------------ | -------- | ------ | --------- | -------- | ------ | --------------- | ---- | -------- | --- |
|     | switch(config-if)# |          |        |           | ipv6     | nd ra  | dns search-list |      | test.com |     |
|     | switch#            |          | show   | ipv6      | nd ra    | dns    | search-list     |      |          |     |
|     | Recursive          |          | DNS    | Search    | List     | on:    | 1               |      |          |     |
|     |                    | Suppress |        | DNS       | Search   | List:  | Yes             |      |          |     |
|     |                    | DNS      | Search | 1:        | test.com |        | lifetime        | 1800 |          |     |
|     | show               | ipv6     | nd     | ra        | dns      | server |                 |      |          |     |
Syntax
|     | show | ipv6 | nd ra | dns server |     | [vsx-peer] |     |     |     |     |
| --- | ---- | ---- | ----- | ---------- | --- | ---------- | --- | --- | --- | --- |
Description
DisplaysDNSserverinformationonallinterfaces.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|                                         | switch(config)#    |          |        | interface |         | 1/1/1         |            |         |     |     |
| --------------------------------------- | ------------------ | -------- | ------ | --------- | ------- | ------------- | ---------- | ------- | --- | --- |
|                                         | switch(config-if)# |          |        |           | ipv6    | nd ra         | dns server | 2001::1 |     |     |
|                                         | switch#            |          | show   | ipv6      | nd ra   | dns           | server     |         |     |     |
|                                         | Recursive          |          | DNS    | Server    | List    | on:           | 1          |         |     |     |
|                                         |                    | Suppress |        | DNS       | Server  | List:         | Yes        |         |     |     |
|                                         |                    | DNS      | Server | 1:        | 2001::1 |               | lifetime   | 1800    |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |          |        |           |         | SwitchSeries) |            |         |     | 40  |

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

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

41

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

sFlow | 42

ConfiguresansFlowcollectorwiththeIPaddress10.10.20.209.
n
EnablesthesFlowagentonallinterfaces.
n
DefinesthesFlowagentIPaddresstobe10.10.1.5.
n
|     | switch(config)# | sflow collector |     | 10.10.20.209 |     |
| --- | --------------- | --------------- | --- | ------------ | --- |
|     | switch(config)# | sflow           |     |              |     |
|     | switch(config)# | sflow agent-ip  |     | 10.0.0.1     |     |
|     | sFlow scenario  |                 |     |              |     |
Inthisscenario,twohostssendsFlowtrafficthroughaswitchtoansFlowcollector.Thephysicaltopologyof
thenetworklookslikethis:
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. EnablesFlowglobally.
|     | switch# config  |       |     |     |     |
| --- | --------------- | ----- | --- | --- | --- |
|     | switch(config)# | sflow |     |     |     |
2. SetthesFlowagentIPaddressto10.10.12.1.
|     | switch(config)# | sflow | agent-ip | 10.10.12.1 |     |
| --- | --------------- | ----- | -------- | ---------- | --- |
3. SetthesFlowcollectorIPaddressto10.10.12.2.
|     | switch(config)# | sflow | collector | 18.2.2.2 |     |
| --- | --------------- | ----- | --------- | -------- | --- |
4. ConfiguresFLowsamplingrateandpollinginterval.
|     | switch(config)# | sflow | sampling | 5000 |     |
| --- | --------------- | ----- | -------- | ---- | --- |
|     | switch(config)# | sflow | polling  | 20   |     |
5. Configureinterface1/1/1withIPaddress10.10.10.1/24.
|     | switch(config)#    | interface | 1/1/1    |               |     |
| --- | ------------------ | --------- | -------- | ------------- | --- |
|     | switch(config-if)# | no        | shutdown |               |     |
|     | switch(config-if)# | ip        | address  | 10.10.10.1/24 |     |
|     | switch(config)#    | quit      |          |               |     |
6. Configureinterface1/1/2withIPaddress10.10.11.1/24.
|     | switch(config)#    | interface | 1/1/2    |               |     |
| --- | ------------------ | --------- | -------- | ------------- | --- |
|     | switch(config-if)# | no        | shutdown |               |     |
|     | switch(config-if)# | ip        | address  | 10.10.11.1/24 |     |
|     | switch(config)#    | quit      |          |               |     |
7. Configureinterface1/1/3withIPaddress10.10.12.1/24.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 43  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

|     | switch(config)#    |     | interface   | 1/1/3         |
| --- | ------------------ | --- | ----------- | ------------- |
|     | switch(config-if)# |     | no shutdown |               |
|     | switch(config-if)# |     | ip address  | 10.10.12.1/24 |
|     | switch(config)#    |     | quit        |               |
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
sFlow|44

Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. Configureswitch1.
a. EnablesFlowglobally.
switch# config
|     | switch(config)# | sflow |     |     |
| --- | --------------- | ----- | --- | --- |
b. SetthesFlowagentIPaddressto10.10.12.1.
|     | switch(config)# | sflow agent-ip | 10.10.12.1 |     |
| --- | --------------- | -------------- | ---------- | --- |
c. SetthesFlowcollectorIPaddressto10.10.12.2.
|     | switch(config)# | sflow collector | 10.10.12.2 |     |
| --- | --------------- | --------------- | ---------- | --- |
d. ConfiguresFLowsamplingrateandpollinginterval.
|     | switch(config)# | sflow sampling | 5000 |     |
| --- | --------------- | -------------- | ---- | --- |
switch(config)#
|     |     | sflow polling | 10  |     |
| --- | --- | ------------- | --- | --- |
e. CreateVLAN8.
|                                         | switch(config)#                  | vlan 8        |                  |     |
| --------------------------------------- | -------------------------------- | ------------- | ---------------- | --- |
|                                         | switch(config-vlan-8)#           |               | no shutdown      |     |
|                                         | switch(config)#                  | exit          |                  |     |
|                                         | f. DefineLAG100andassignVLANvlan |               | 8toit.           |     |
|                                         | switch(config)#                  | interface     | lag 100          |     |
|                                         | switch(config-lag-if)#           |               | no shutdown      |     |
|                                         | switch(config-lag-if)#           |               | vlan access 8    |     |
|                                         | switch(config-lag-if)#           |               | lacp mode active |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                                  | SwitchSeries) |                  | 45  |

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
sFlow|46

|     |       | switch(config-if)#                                   |                    | no shutdown |       |     |     |
| --- | ----- | ---------------------------------------------------- | ------------------ | ----------- | ----- | --- | --- |
|     |       | switch(config-if)#                                   |                    | vlan access | 8     |     |     |
|     |       | d. Configureinterface1/1/2and1/1/3asmembersofLAG100. |                    |             |       |     |     |
|     |       | switch#                                              | (config)#interface |             | 1/1/2 |     |     |
|     |       | switch(config-if)#                                   |                    | no shutdown |       |     |     |
|     |       | switch(config-if)#                                   |                    | lag 100     |       |     |     |
|     |       | switch(config-if)#                                   |                    | exit        |       |     |     |
|     |       | switch(config)-if#                                   |                    | interface   | 1/1/3 |     |     |
|     |       | switch(config-if)#                                   |                    | no shutdown |       |     |     |
|     |       | switch(config-if)#                                   |                    | lag 100     |       |     |     |
|     |       | switch(config-if)#                                   |                    | exit        |       |     |     |
|     | sFlow | agent                                                | commands           |             |       |     |     |
|     | clear | sflow statistics                                     |                    |             |       |     |     |
Syntax
|     | clear | sflow statistics | {global | | interface | <INTERFACE-NAME>} |     |     |
| --- | ----- | ---------------- | ------- | ----------- | ----------------- | --- | --- |
Description
ThiscommandclearsthesFlowsamplestatisticscounterto0eithergloballyorforaspecificinterface.
Commandcontext
config
Parameters
global
Specifiesallinterfacesontheswitch.
|     | interface | <INTERFACE-NAME> |     |     |     |     |     |
| --- | --------- | ---------------- | --- | --- | --- | --- | --- |
Specifiesthenameofaninterfaceontheswitch.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ClearingtheglobalsFlowsamplestatisticscounterto0globally:
|     | switch(config)# |     | clear | sflow statistics | global |     |     |
| --- | --------------- | --- | ----- | ---------------- | ------ | --- | --- |
ClearingtheglobalsFlowsamplestatisticscounterto0forinterface1/1/1:
|     | switch(config)# |     | clear | sflow statistics | interface | 1/1/1 |     |
| --- | --------------- | --- | ----- | ---------------- | --------- | ----- | --- |
sflow
Syntax
sflow
|     | no sflow |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) |     |     | 47  |
| --------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- |

EnablesthesFlowagent.
Intheconfigcontext,thiscommandenablesthesFlowagentgloballyonallinterfaces.
n
n Inanconfig-ifcontext,thiscommandenablesthesFlowagentonaspecificinterface.sFlowcannotbe
enabledonamemberofaLAG,onlyontheLAG.
ThesFlowagentisdisabledbydefault.
ThenoformofthiscommanddisablesthesFlowagentanddeletesallsFlowconfigurationsettings,either
globally,orforaspecificinterface.
Commandcontext
config
config-if
Parameters
None.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingsFlowgloballyonallinterfaces:
| switch(config)# | sflow |     |
| --------------- | ----- | --- |
DisablingsFlowgloballyonallinterfaces:
| switch(config)# | no sflow |     |
| --------------- | -------- | --- |
EnablingsFlowoninterface1/1/1:
switch(config)#
|                    | interface | 1/1/1 |
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
sFlow|48

|     | switch(config)# | interface | lag100 |     |
| --- | --------------- | --------- | ------ | --- |
switch(config-if)#
no sflow
|     | sflow agent-ip |     |     |     |
| --- | -------------- | --- | --- | --- |
Syntax
|     | sflow agent-ip <IP-ADDR> |             |     |     |
| --- | ------------------------ | ----------- | --- | --- |
|     | no sflow agent-ip        | [<IP-ADDR>] |     |     |
Description
DefinestheIPaddressofthesFlowagenttouseinsFlowdatagrams.ThisaddressmustbedefinedforsFlow
tofunction.HPErecommendsthattheaddress:
|     | n canuniquelyidentifytheswitch |     |     |     |
| --- | ------------------------------ | --- | --- | --- |
isreachablebythesFlowcollector
n
doesnotchangewithtime
n
ThenoformofthiscommanddeletestheIPaddressofthesFlowagent.ThiscausessFlowtostopworking
andnodatagramswillbesenttothesFlowcollector.
Commandcontext
config
Parameters
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255,orIPv6
format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisahexadecimalnumberfrom0toF.
TheagentaddressisusedtoidentifytheswitchinallsFlowdatagramssenttosFlowcollectors.Itis
usuallysettoanIPaddressontheswitchthatisreachablefromansFlowcollector.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingtheagentaddressto10.10.10.100:
switch(config)#
|     |     | sflow agent-ip | 10.0.0.100 |     |
| --- | --- | -------------- | ---------- | --- |
Settingtheagentaddressto2001:0db8:85a3:0000:0000:8a2e:0370:7334:
switch(config)# sflow agent-ip 2001:0db8:85a3:0000:0000:8a2e:0370:7334
Removingtheaddressconfigurationfromtheswitch,whichresultsinsFlowbeingdisabled:
|                                         | switch(config)# | no sflow | agent-ip      |     |
| --------------------------------------- | --------------- | -------- | ------------- | --- |
|                                         | sflow collector |          |               |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                 |          | SwitchSeries) | 49  |

Syntax

sflow collector <IP-ADDR> [port <PORT>] [vrf <VRF>]
no sflow collector <IP-ADDR> [port <PORT>] [vrf <VRF>]

Description

Defines a collector to which the sFlow agent sends data. Up to three collectors can be defined. At least one
collector should be defined, and it must be reachable from the switch for sFlow to work.

Command context

config

Parameters

collector <IP-ADDR>

Specifies the IP address of a collector in IPv4 format (x.x.x.x), where x is a decimal number from 0 to
255, or IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number
from 0 to F.

port <PORT>

Specifies the UDP port on which to send information to the sFlow collector. Range: 0 to 65536. Default:
6343.
vrf <VRF>

Specifies the VRF on which to send information to the sFlow collector. The VRF must be defined on the
switch. If no VRF is specified, the default VRF (default) is used.

Authority

Administrators or local user group members with execution rights for this command.

Example

Defining a collector with IP address 10.10.10.100 on UDP port 6400:

switch(config)# sflow collector 10.0.0.1 port 6400

sflow disable

Syntax

sflow disable

Description

Disables the sFlow agent, but retains any existing sFlow configuration settings. The settings become active if
the sFlow agent is re-enabled.

Command context

config

Parameters

None.

Authority

Administrators or local user group members with execution rights for this command.

sFlow | 50

Example
DisablingsFlowsupport:
switch(config)#
sflow disable
|     | sflow header-size |     |     |     |
| --- | ----------------- | --- | --- | --- |
Syntax
|     | sflow header-size    | <SIZE>   |     |     |
| --- | -------------------- | -------- | --- | --- |
|     | no sflow header-size | [<SIZE>] |     |     |
Description
SetsthesFlowheadersizeinbytes.
Thenoformofthiscommandsetstheheadersizetothedefaultvalueof128.
Commandcontext
config
Parameters
header-size <SIZE>
SpecifiesthesFlowheadersizeinbytes.Range:64to256.Default:128.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingtheheadersizeto64bytes:
|     | switch(config)# | sflow header-size | 64  |     |
| --- | --------------- | ----------------- | --- | --- |
Settingtheheadersizetothedefaultvalueof128bytes:
|     | switch(config)#         | no sflow | header-size |     |
| --- | ----------------------- | -------- | ----------- | --- |
|     | sflow max-datagram-size |          |             |     |
Syntax
|     | sflow max-datagram-size    | <SIZE> |          |     |
| --- | -------------------------- | ------ | -------- | --- |
|     | no sflow max-datagram-size |        | [<SIZE>] |     |
Description
SetsthemaximumnumberofbytesthataresentinonesFlowdatagram.
Thenoformofthiscommandsetsmaximumnumberofbytestothedefaultvalueof1400.
Commandcontext
config
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 51  |
| --------------------------------------- | --- | --- | ------------- | --- |

Parameters
| max-datagram-size |     | <SIZE> |     |     |
| ----------------- | --- | ------ | --- | --- |
Specifiesthemaximumdatagramsizeinbytes.Range:1to9000.Default:1400.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthedatagramsizeto1000bytes:
| switch(config)# |     | sflow max-datagram-size |     | 1000 |
| --------------- | --- | ----------------------- | --- | ---- |
Settingtheheadersizetothedefaultvalueof1400bytes:
| switch(config)# |      | no sflow | max-datagram-size |     |
| --------------- | ---- | -------- | ----------------- | --- |
| sflow           | mode |          |                   |     |
Syntax
| sflow mode | {ingress      | | egress | | both} |     |
| ---------- | ------------- | -------- | ------- | --- |
| no sflow   | mode {ingress | | egress | | both} |     |
Description
SetsthesFlowsamplingmode.Thedefaultmodeisingress.
Thenoformofthecommandsetsthesamplingmodetoingress.Executingthenoformofthecommand
withtheingressoptionwillhavenoimpactasingressisthedefaultmode.
Commandcontext
config
Parameters
ingress
Samplesonlyingresstraffic.
egress
Samplesonlyegresstraffic.
both
Samplesbothingressandegresstraffic.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingthesFlowmodetoonlysampleegresstraffic:
| switch#         | configure | terminal   |        |     |
| --------------- | --------- | ---------- | ------ | --- |
| switch(config)# |           | sflow mode | egress |     |
sFlow|52

ResettingthesFlowsamplingmodetothedefaultofingressfrompreviouslyconfiguredmodeofegress:
|     | switch# configure | terminal |             |     |
| --- | ----------------- | -------- | ----------- | --- |
|     | switch(config)#   | no sflow | mode egress |     |
|     | sflow polling     |          |             |     |
Syntax
|     | sflow polling <INTERVAL> |              |     |     |
| --- | ------------------------ | ------------ | --- | --- |
|     | no sflow polling         | [<INTERVAL>] |     |     |
Description
DefinestheglobalpollingintervalforsFlowinseconds.
Thenoformofthiscommandsetsthepollingintervaltothedefaultvalueof30seconds.
Commandcontext
config
Parameters
<INTERVAL>
Specifiesthepollingintervalinseconds.Range:10to3600.Default:30.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthepollingintervalto10:
|     | switch(config)# | sflow polling | 10  |     |
| --- | --------------- | ------------- | --- | --- |
Settingthepollingintervaltothedefaultvalue.
|     | switch(config)# | no sflow | polling |     |
| --- | --------------- | -------- | ------- | --- |
|     | sflow sampling  |          |         |     |
Syntax
|     | sflow sampling <RATE> |          |     |     |
| --- | --------------------- | -------- | --- | --- |
|     | no sflow sampling     | [<RATE>] |     |     |
Description
DefinestheglobalsamplingrateforsFlowinnumberofpackets.Thedefaultsamplingrateis4096,which
meansthatoneinevery4096packetsissampled.Awarningmessageisdisplayedwhenthesamplingrateis
settolessthan4096andproceedsonlyafteruserconfirmation.
Thenoformofthiscommandsetsthesamplingratetothedefaultvalueof4096.
Commandcontext
config
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 53  |
| --------------------------------------- | --- | --- | ------------- | --- |

Parameters
| sampling | <RATE> |     |     |     |
| -------- | ------ | --- | --- | --- |
Specifiesthesamplingrate.Range:1to1000000000.Default:4096.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthesamplingrateto5000:
| switch(config)# |     | sflow | sampling | 5000 |
| --------------- | --- | ----- | -------- | ---- |
Settingthesamplingratetothedefault:
| switch(config)# |     | no sflow | sampling |     |
| --------------- | --- | -------- | -------- | --- |
Settingthesamplingrateto1000:
| switch(config)# |     | sflow | sampling | 1000 |
| --------------- | --- | ----- | -------- | ---- |
Setting the sFlow sampling rate lower than 4096 is not recommended and might
| affect | system  | performance. |        |     |
| ------ | ------- | ------------ | ------ | --- |
| Do you | want to | continue     | [y/n]? | y   |
switch(config)#
| show | sflow |     |     |     |
| ---- | ----- | --- | --- | --- |
Syntax
| show sflow | [interface | <INTERFACE-NAME>] |     | [vsx-peer] |
| ---------- | ---------- | ----------------- | --- | ---------- |
Description
ShowssFlowconfigurationsettingsandstatisticsforallinterfaces,orforaspecificinterface
Commandcontext
Manager(#)
Parameters
| interface | <INTERFACE-NAME> |     |     |     |
| --------- | ---------------- | --- | --- | --- |
Specifiesthenameofaninterfaceontheswitch.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
sFlow|54

|     | switch#      | show sflow    |     |     |     |
| --- | ------------ | ------------- | --- | --- | --- |
|     | sFlow Global | Configuration |     |     |     |
-----------------------------------------
|     | sFlow         |             |     | enabled                 |     |
| --- | ------------- | ----------- | --- | ----------------------- | --- |
|     | Collector     | IP/Port/Vrf |     | 10.10.10.2/6343/default |     |
|     | Agent Address |             |     | 10.0.0.1                |     |
|     | Sampling      | Rate        |     | 1024                    |     |
|     | Polling       | Interval    |     | 30                      |     |
|     | Header        | Size        |     | 128                     |     |
|     | Max Datagram  | Size        |     | 1400                    |     |
|     | Sampling      | Mode        |     | both                    |     |
sFlow Status
-----------------------------------------
|     | Running       | - Yes |             |     |     |
| --- | ------------- | ----- | ----------- | --- | --- |
|     | sFlow enabled | on    | Interfaces: |     |     |
-----------------------------------------
lag100
sFlow Statistics
-----------------------------------------
|     | Number | of Ingress | Samples | 200 |     |
| --- | ------ | ---------- | ------- | --- | --- |
|     | Number | of Egress  | Samples | 0   |     |
ShowingsFlowinformationforinterface1/1/1:
|     | switch#             | show sflow | interface   | 1/1/1 |     |
| --- | ------------------- | ---------- | ----------- | ----- | --- |
|     | sFlow configuration |            | - Interface | 1/1/1 |     |
-----------------------------------------
|                                         | sFlow          |            |               | enabled |     |
| --------------------------------------- | -------------- | ---------- | ------------- | ------- | --- |
|                                         | Sampling       | Rate       |               | 1024    |     |
|                                         | Sampling       | Mode       |               | both    |     |
|                                         | Number         | of Ingress | Samples       | 81      |     |
|                                         | Number         | of Egress  | Samples       | 20      |     |
|                                         | sFlow Sampling | Status     |               | success |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                |            | SwitchSeries) |         | 55  |

Chapter 5

DHCP

DHCP

The Dynamic Host Configuration Protocol (DHCP) enables the automatic assignment of IP addresses and
other configuration settings to network devices.

DHCP is composed of three components: DHCP server, DHCP client, and DHCP relay agent.

The DHCP server contains the IP addresses and configuration settings for a network as defined by a network
administrator. It responds to DHCP requests issued by DHCP clients, returning the requested network
configuration settings.

The DHCP client runs on a network device. It issues a request to a DHCP server to obtain an IP address for
the network device, and other network settings.

The DHCP relay agent acts an intermediary, forwarding DHCP requests/response between DHCP
clients/servers on different networks. This enables DHCP clients to use the services of DHCP servers that are
not on the same subnet on which they are located.

DHCP client
By default, the switch operates as a DHCP client on VLAN 1 or the management interface allowing it to
automatically obtain an IP address from a DHCP server on the network to which it is connected.

DHCP client commands

ip dhcp

Syntax

ip dhcp

Description

Enables the DHCP client on the management interface enabling the interface to automatically obtain an IP
address from a DHCP server on the network. By default, the DHCP client is enabled.

Command context

config-if-mgmt

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example enables the DHCP client on the management interface.

switch(config)# interface mgmt
switch(config-if-mgmt)# ip dhcp
switch(config-if-mgmt)# no shutdown

If the interface is not enabled, you can enable it by entering the no shutdown command.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

56

DHCP relay agent
The function of the DHCP relay agent is to forward the DHCP messages to other subnets so that the DHCP
server does not have to be on the same subnet as the DHCP clients. The DHCP relay agent transfers DHCP
messages from the DHCP clients located on a subnet without a DHCP server, to other subnets. It also relays
answers from DHCP servers to DHCP clients.

Supported interfaces

The DHCP relay agent is supported on layer 3 interfaces, layer 3 VLAN interfaces, and LAG interfaces. DHCP
relay is not supported on the management interface.

VRF support

The DHCP relay agent is VRF aware and behaves as follows when VRFs are defined on the switch:

n DHCP client requests received on an interface are forwarded to the configured servers via the VRF that

the interface is part of.

n DHCP server responses received on an interface are forwarded to the client that is reachable via the VRF

that the interface is part of.

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
both relay agents to decide the IP address for the client..

Inter-VRF DHCP relay

The DHCP relay agent supports anycast gateway using option 82 sub-option 5 (RFC 3527). The DHCP relay
discovery packet is filled with the client's gateway IP address in sub-option 5 (discovery packet). The DHCP
server uses this information to offer an IP address from the right pool. Pool selection occurs by matching
the default gateway configuration settings on the DHCP server with the requested gateway IP address in
sub-option 5 in the discovery packet.

The switch uses DHCP relay sub-option 151 to enable DHCP relay to forward discovery and reply packets
between VXLAN DHCP clients and DHCP servers even when they are on different overlay or underlay VRFs
and the DHCP-server is reachable on the default VRF or one of the overlay VRFs.

In general deployments, a renewal of a DHCP client's IP occurs when the client sends a request to the DHCP
server directly. In the case of EVPN VXLAN clients, the DHCP server is not directly reachable. Instead, the
renewal request is sent to the DHCP relay. DHCP relay agent fills the option 82 sub-option 11 field in the
DHCP discovery packet with the client's gateway IP on the VTEP (which is the relay interface IP address of

DHCP | 57

the VTEP) and the DHCP server returns a DHCP offer reply packet with option 54 set to the DHCP server
Identifier. When the reply packet is received by the client, the client uses the IP in option 54 to sent
subsequent renewal requests to this IP (VTEP's Relay Interface IP) using sub-option 11 (also known as the
Server ID Override Sub-option). Refer to RFC 5107 for more details.

Sub-options 5,11,151,152 are filled in the discover packet, only if a source IP address is defined (using the
command ip source-address) for the given DHCP server's source VRF. If the server does not understand
sub-option 151, then the server will add sub-option 152 in offer packet.

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

n Enables DHCP option 82 support and replaces all option 82 information with the values from the switch

with the switch MAC address as the remote ID.

switch(config)# dhcp-relay
switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# ip address 198.51.100.1/24

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

58

| switch(config-if)# |     |     | ip helper-address |     |     | 10.10.20.209 |     |
| ------------------ | --- | --- | ----------------- | --- | --- | ------------ | --- |
switch(config-if)#
exit
| switch(config)# |             | dhcp-relay |        | option    |     | 82 replace mac |     |
| --------------- | ----------- | ---------- | ------ | --------- | --- | -------------- | --- |
| switch#         | show        | dhcp-relay |        |           |     |                |     |
| DHCP Relay      | Agent       |            |        |           |     | : Enabled      |     |
| DHCP Request    |             | Hop        | Count  | Increment |     | : Enabled      |     |
| Option          | 82          |            |        |           |     | : Disabled     |     |
| Response        | Validation  |            |        |           |     | : Disabled     |     |
| Option          | 82 Handle   |            | Policy |           |     | : replace      |     |
| Remote          | ID          |            |        |           |     | : mac          |     |
| DHCP Relay      | Statistics: |            |        |           |     |                |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |                |     |     | 60  | 10  |
| ---------- | ------ | --- | -------------- | --- | --- | --- | --- |
| DHCP Relay | Option |     | 82 Statistics: |     |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50  |     | 8   |     |     |     | 50  | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |
DHCPv4relayscenario1
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
Procedure
1. DHCPrelayisenabledbydefault.Ifitwaspreviouslydisabled,enableit.
| switch#         | config |     |            |     |     |     |     |
| --------------- | ------ | --- | ---------- | --- | --- | --- | --- |
| switch(config)# |        |     | dhcp-relay |     |     |     |     |
2. DefineanIPv4helperaddressoninterfaces1/1/1and1/1/2.
| switch(config)#    |     |     | interface | 1/1/1          |                 |             |     |
| ------------------ | --- | --- | --------- | -------------- | --------------- | ----------- | --- |
| switch(config-if)# |     |     | ip        | address        | 192.168.2.11/24 |             |     |
| switch(config-if)# |     |     | ip        | helper-address |                 | 192.168.1.1 |     |
| switch(config-if)# |     |     | interface |                | 1/1/2           |             |     |
switch(config-if)#
|                    |     |     | ip   | address        | 192.168.2.12/24 |             |     |
| ------------------ | --- | --- | ---- | -------------- | --------------- | ----------- | --- |
| switch(config-if)# |     |     | ip   | helper-address |                 | 192.168.1.1 |     |
| switch(config-if)# |     |     | quit |                |                 |             |     |
DHCP|59

3. VerifyDHCPrelayconfiguration.
|     | switch#          | show dhcp-relay |                 |            |     |     |
| --- | ---------------- | --------------- | --------------- | ---------- | --- | --- |
|     | DHCP Relay       | Agent           |                 | : Enabled  |     |     |
|     | DHCP Request     | Hop             | Count Increment | : Enabled  |     |     |
|     | L2VPN Clients    |                 |                 | : Disabled |     |     |
|     | Option           | 82              |                 | : Disabled |     |     |
|     | Source-Interface |                 |                 | : Disabled |     |     |
|     | Response         | Validation      |                 | : Disabled |     |     |
|     | Option           | 82 Handle       | Policy          | : replace  |     |     |
|     | Remote           | ID              |                 | : mac      |     |     |
|     | DHCP Relay       | Statistics:     |                 |            |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|     | 60         |        | 10             | 60  | 10  |     |
| --- | ---------- | ------ | -------------- | --- | --- | --- |
|     | DHCP Relay | Option | 82 Statistics: |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|     | 50                |                        | 8                 | 50  | 8   |     |
| --- | ----------------- | ---------------------- | ----------------- | --- | --- | --- |
|     | switch#           | show ip helper-address |                   |     |     |     |
|     | IP Helper         | Addresses              |                   |     |     |     |
|     | Interface:        | 1/1/1                  |                   |     |     |     |
|     | IP Helper         | Address                | VRF               |     |     |     |
|     | ----------------- |                        | ----------------- |     |     |     |
|     | 192.168.1.1       |                        | default           |     |     |     |
|     | Interface:        | 1/1/2                  |                   |     |     |     |
|     | IP Helper         | Address                | VRF               |     |     |     |
|     | ----------------- |                        | ----------------- |     |     |     |
|     | 192.168.1.1       |                        | default           |     |     |     |
DHCPv4relayscenario2
(Thisscenarioisnotsupportedonthe6200SwitchSeries.)
Inthisscenario,thetwohostcomputerscommunicatewithtwodifferentDHCPservers.Eachserveris
reachedonadifferentVRF.Thephysicaltopologyofthenetworklookslikethis:
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 60  |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

Procedure
1. CreatethetwoVRFs.
switch# config
| switch(config)# | vrf vrf 1 |     |
| --------------- | --------- | --- |
| switch(config)# | vrf vrf 2 |     |
2. Configureinterface1/1/1.SetitsIPaddress,associateitwithVRF1,anddefinethehelperIPaddress
toreachDHCPserver1.
| switch(configif)# | interface         | 1/1/1      |
| ----------------- | ----------------- | ---------- |
| switch(configif)# | vrf attach        | vrf1       |
| switch(configif)# | ip address        | 20.0.0.1/8 |
| switch(configif)# | ip helper-address | 10.0.10.2  |
3. Configureinterface1/1/2.SetitsIPaddressandassociateitwithVRF1.
switch(configif)#
|                   | interface  | 1/1/2        |
| ----------------- | ---------- | ------------ |
| switch(configif)# | vrf attach | vrf1         |
| switch(configif)# | ip address | 10.0.10.1/24 |
4. Configureinterface1/1/3.SetitsIPaddressandassociateitwithVRF1.
| switch(configif)# | interface  | 1/1/3      |
| ----------------- | ---------- | ---------- |
| switch(configif)# | vrf attach | vrf2       |
| switch(configif)# | ip address | 9.0.0.1/24 |
5. Configureinterface1/1/4.SetitsIPaddress,associateitwithVRF2,anddefinethehelperIPaddress
toreachDHCPserver2.
| switch(configif)# | interface         | 1/1/4      |
| ----------------- | ----------------- | ---------- |
| switch(configif)# | vrf attach        | vrf2       |
| switch(configif)# | ip address        | 30.0.0.1/8 |
| switch(configif)# | ip helper-address | 9.0.0.2    |
DHCPv4relayscenario3
Inthisscenario,hostonswitch1reachestheDHCPserveronswitchtwoviaaLAG.Thephysicaltopologyof
thenetworklookslikethis:
DHCP|61

Procedure
1. Onswitch1:
a. CreateLAG100andassignanIPaddresstoit.
switch# config
|     | switch(config)#        | interface |      | lag 100 |              |     |
| --- | ---------------------- | --------- | ---- | ------- | ------------ | --- |
|     | switch(config-lag-if)# |           | ip   | address | 10.0.10.1/24 |     |
|     | switch(config-lag-if)# |           | lacp | mode    | active       |     |
|     | switch(config-lag-if)# |           | exit |         |              |     |
switch(config)#
b. AssignanIPaddresstointerface1/1/1andaanIPhelperaddresstoreachtheDHCPserver.
|     | switch(config)#    | interface |                   | 1/1/1      |         |     |
| --- | ------------------ | --------- | ----------------- | ---------- | ------- | --- |
|     | switch(config-if)# |           | ip address        | 20.0.0.1/8 |         |     |
|     | switch(config-if)# |           | ip helper-address |            | 9.0.0.2 |     |
c. Assigninterfaces1/1/2and1/1/3toLAG100
|     | switch(config-if)# |     | interface | 1/1/2 |     |     |
| --- | ------------------ | --- | --------- | ----- | --- | --- |
|     | switch(config-if)# |     | lag 100   |       |     |     |
|     | switch(config-if)# |     | interface | 1/1/3 |     |     |
|     | switch(config-if)# |     | lag 100   |       |     |     |
|     | switch(config-if)# |     | exit      |       |     |     |
switch(config)#
d. Createaroutebetween10.0.10.2and9.0.0.0.
|     | switch(config)# | ip  | route 9.0.0.0/24 |     | 10.0.10.2 |     |
| --- | --------------- | --- | ---------------- | --- | --------- | --- |
2. Onswitch2:
a. CreateLAG100andassignanIPaddresstoit.
switch# config
|     | switch(config)#        | interface |      | lag 100 |              |     |
| --- | ---------------------- | --------- | ---- | ------- | ------------ | --- |
|     | switch(config-lag-if)# |           | ip   | address | 10.0.10.2/24 |     |
|     | switch(config-lag-if)# |           | lacp | mode    | active       |     |
|     | switch(config-lag-if)# |           | exit |         |              |     |
switch(config)#
b. Assigninterfaces1/1/1and1/1/2toLAG100
|     | switch(config-if)# |     | interface | 1/1/2 |     |     |
| --- | ------------------ | --- | --------- | ----- | --- | --- |
|     | switch(config-if)# |     | lag 100   |       |     |     |
|     | switch(config-if)# |     | interface | 1/1/3 |     |     |
|     | switch(config-if)# |     | lag 100   |       |     |     |
|     | switch(config-if)# |     | exit      |       |     |     |
switch(config)#
c. AssignanIPaddresstointerface1/1/3.
|     | switch(config)#    | interface |            | 1/1/3      |     |     |
| --- | ------------------ | --------- | ---------- | ---------- | --- | --- |
|     | switch(config-if)# |           | ip address | 9.0.0.1/24 |     |     |
d. Createaroutebetween20.0.0.0and10.0.10.1.
|     | switch(config)# | ip  | route 20.0.0.0/8 |     | 10.0.10.1 |     |
| --- | --------------- | --- | ---------------- | --- | --------- | --- |
DHCPv4relaycommands
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 62  |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

dhcp-relay

Syntax

dhcp-relay
no dhcp-relay

Description

Enables DHCP relay support. DHCP relay is enabled by default. DHCP relay is not supported on the
management interface.

The no form of this command disables DHCP relay support.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example enables DHCP relay support.

switch(config)# dhcp-relay

This example removes DHCP relay support.

switch(config)# no dhcp-relay

dhcp-relay hop-count-increment

Syntax

dhcp-relay hop-count-increment
no dhcp-relay hop-count-increment

Description

Enables the DHCP relay hop count increment feature, which causes the DHCP relay agent to increment the
hop count in all relayed DHCP packets. Hop count is enabled by default.

The no form of this command disables the hop count increment feature.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the hop count increment feature.

switch(config)# dhcp-relay hop-count-increment

Disabling the hop count increment feature.

DHCP | 63

|     | switch(config)# | no            | dhcp-relay | hop-count-increment |     |
| --- | --------------- | ------------- | ---------- | ------------------- | --- |
|     | dhcp-relay      | l2vpn-clients |            |                     |     |
Syntax
|     | dhcp-relay    | l2vpn-clients |     |     |     |
| --- | ------------- | ------------- | --- | --- | --- |
|     | no dhcp-relay | l2vpn-clients |     |     |     |
Description
EnablesforwardingofpacketsfromL2VPNclients.Forwardingisenabledbydefault.
ThenoformofthiscommanddisablesforwardingofpacketsfromL2VPNclients.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
EnablingforwardingofpacketsfromL2VPNclients.
|     | switch(config)# | dhcp-relay |            | l2vpn-clients |     |
| --- | --------------- | ---------- | ---------- | ------------- | --- |
|     | switch(config)# | no         | dhcp-relay | l2vpn-clients |     |
|     | dhcp-relay      | option 82  |            |               |     |
Syntax
dhcp-relay option 82 {replace [validate] | drop [validate] | keep | source-interface |
|     | validate [replace | | drop]} |                     | [ip | mac] |     |
| --- | ----------------- | -------- | ------------------- | ---------- | --- |
|     | no dhcp-relay     | option   | 82 source-interface |            |     |
Description
ConfiguresthebehaviorofDHCPrelayoption82.ADHCPrelayagentcanreceiveamessagefromanother
DHCPrelayagenthavingoption82.Therelayinformationfromthepreviousrelayagentisreplacedby
default.
ThenoformofthiscommanddisablessupportforDHCPrelayoption82.
Commandcontext
config
Parameters
replace
Replacetheexistingoption82fieldinaninboundclientDHCPpacketwiththeinformationfromthe
switch.TheremoteIDandcircuitIDinformationfromthefirstrelayagentislost.Default.
validate
Validateoption82informationinDHCPserverresponsesanddropinvalidresponses.
drop
DropanyinboundclientDHCPpacketthatcontainsoption82information.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) | 64  |
| --------------------------------------- | --- | --- | --- | ------------- | --- |

keep

Keep the existing option 82 field in an inbound client DHCP packet. The remote ID and circuit ID
information from the first relay agent is preserved.

source-interface

Configures the DHCP relay to use a configured source IP address for inter-VRF server reachability. Set the
source IP address with the command ip source-interface.

ip

Use the IP address of the interface on which the client DHCP packet entered the switch as the option 82
remote ID.

mac

Use the MAC address of the switch as the option 82 remote ID. Default.

Authority

Administrators or local user group members with execution rights for this command.

Example

This example enables DHCP option 82 support and replaces all option 82 information with the values from
the switch, with the switch MAC address as the remote ID.

switch(config)# dhcp-relay option 82 replace mac

ip bootp-gateway

Syntax

ip bootp-gateway <IPV4-ADDR>
no ip bootp-gateway <IPV4-ADDR>

Description

Configures a gateway address for the DHCP relay agent to use for DHCP requests. By default DHCP relay
agent picks the lowest-numbered IP address on the interface.

The no form of this command removes the gateway address.

Command context

config-if

Parameters

<IPV4-ADDR>

Specifies the IP address of the gateway in IPv4 format (x.x.x.x), where x is a is a decimal number from 0
to 255.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Sets the IP address of the gateway for interface 1/1/1 to 10.10.10.10.

DHCP | 65

|     | switch(config)# | interface | 1/1/1 |     |     |     |
| --- | --------------- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|     |     | ip bootp-gateway |     | 10.10.10.10 |     |     |
| --- | --- | ---------------- | --- | ----------- | --- | --- |
iphelper-address
Syntax
|     | ip helper-address    | <IPV4-ADDR> | [vrf <VRF-NAME>] |             |     |     |
| --- | -------------------- | ----------- | ---------------- | ----------- | --- | --- |
|     | no ip helper-address | <IPV4-ADDR> | [vrf             | <VRF-NAME>] |     |     |
Description
DefinestheaddressofaremoteDHCPserverorDHCPrelayagent.Uptoeightaddressescanbedefined.
TheDHCPagentforwardsDHCPclientrequeststoalldefinedservers.
ThiscommandrequiresthatyoudefineasourceIPaddressforDHCPrelaywiththecommand ip source-
interface.TheconfiguredsourceIPontheVRFisusedtoforwardDHCPpacketstotheserver.
AhelperaddresscannotbedefinedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
Commandcontext
config-if
Parameters
|     | helper-address | <IPV4-ADDR> |     |     |     |     |
| --- | -------------- | ----------- | --- | --- | --- | --- |
SpecifiesthehelperIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
|     | vrf <VRF-NAME> |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
SpecifiesthenameofaVRF.Default:default.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
DefiningtheIPhelperaddress10.10.10.209oninterface1/1/1.
|     | switch(config)#    | interface         | 1/1/1 |              |     |     |
| --- | ------------------ | ----------------- | ----- | ------------ | --- | --- |
|     | switch(config-if)# | ip helper-address |       | 10.10.10.209 |     |     |
RemovingtheIPhelperaddress10.10.10.209oninterface1/1/1.
|     | switch(config-if)# | no ip | helper-address | 10.10.10.209 |     |     |
| --- | ------------------ | ----- | -------------- | ------------ | --- | --- |
DefiningtheIPhelperaddress10.10.10.209oninterface1/1/2onVRFmyvrf.
|                                         | switch(config)#    | interface         | 1/1/2         |              |           |     |
| --------------------------------------- | ------------------ | ----------------- | ------------- | ------------ | --------- | --- |
|                                         | switch(config-if)# | ip helper-address |               | 10.10.10.209 | vrf myvrf |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |                   | SwitchSeries) |              |           | 66  |

RemovingtheIPhelperaddress10.10.10.209oninterface1/1/2onVRFmyvrf.
| switch(config-if)# |     |     | no ip helper-address |     | 10.10.10.209 | vrf myvrf |
| ------------------ | --- | --- | -------------------- | --- | ------------ | --------- |
showdhcp-relay
Syntax
| show dhcp-relay | [vsx-peer] |     |     |     |     |     |
| --------------- | ---------- | --- | --- | --- | --- | --- |
Description
ShowsDHCPrelayconfigurationsettings.
Commandcontext
Manager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Example
| switch#          | show dhcp-relay |           |           |            |     |     |
| ---------------- | --------------- | --------- | --------- | ---------- | --- | --- |
| DHCP Relay       | Agent           |           |           | : Enabled  |     |     |
| DHCP Request     |                 | Hop Count | Increment | : Enabled  |     |     |
| L2VPN Clients    |                 |           |           | : Disabled |     |     |
| Option           | 82              |           |           | : Disabled |     |     |
| Source-Interface |                 |           |           | : Disabled |     |     |
| Response         | Validation      |           |           | : Disabled |     |     |
| Option           | 82 Handle       | Policy    |           | : replace  |     |     |
| Remote           | ID              |           |           | : mac      |     |     |
| DHCP Relay       | Statistics:     |           |           |            |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |                | 60  |     | 10  |
| ---------- | ------ | --- | -------------- | --- | --- | --- |
| DHCP Relay | Option |     | 82 Statistics: |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 50             |               | 8   |     | 50  |     | 8   |
| -------------- | ------------- | --- | --- | --- | --- | --- |
| showdhcp-relay | bootp-gateway |     |     |     |     |     |
Syntax
show dhcp-relay bootp-gateway [interface <INTERFACE-NAME>] [vsx-peer]
DHCP|67

Description
Showsthebootpgatewaydefinedforallinterfacesoraspecificinterface.
Commandcontext
Manager(#)
Parameters
<INTERFACE-NAME>
Specifiesaninterface.Format:member/slot/port.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch# show         | dhcp-relay        | bootp-gateway   |       |     |
| --- | -------------------- | ----------------- | --------------- | ----- | --- |
|     | BOOTP Gateway        | Entries           |                 |       |     |
|     | Interface            |                   | Source IP       |       |     |
|     | -------------------- |                   | --------------- |       |     |
|     | 1/1/1                |                   | 1.1.1.1         |       |     |
|     | 1/1/2                |                   | 1.1.1.2         |       |     |
|     | switch# show         | ip helper-address | interface       | 1/1/1 |     |
|     | BOOTP Gateway        | Entries           |                 |       |     |
|     | Interface            |                   | Source IP       |       |     |
|     | -------------------- |                   | --------------- |       |     |
|     | 1/1/1                |                   | 1.1.1.1         |       |     |
showiphelper-address
Syntax
|     | show ip helper-address | [interface | <INTERFACE-ID>] | [vsx-peer] |     |
| --- | ---------------------- | ---------- | --------------- | ---------- | --- |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
Commandcontext
Manager(#)
Parameters
|                                         | interface <INTERFACE-ID> |     |               |     |     |
| --------------------------------------- | ------------------------ | --- | ------------- | --- | --- |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                          |     | SwitchSeries) |     | 68  |

Specifiesaninterface.Format:member/slot/port.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch# show      | ip helper-address |                     |       |
| ----------------- | ----------------- | ------------------- | ----- |
| IP Helper         | Addresses         |                     |       |
| Interface:        | 1/1/1             |                     |       |
| IP Helper         | Address           | VRF                 |       |
| ----------------- |                   | -----------------   |       |
| 192.168.20.1      |                   | default             |       |
| 192.168.10.1      |                   | default             |       |
| Interface:        | 1/1/2             |                     |       |
| IP Helper         | Address           | VRF                 |       |
| ----------------- |                   | -----------------   |       |
| 192.168.30.1      |                   | RED                 |       |
| switch# show      | ip helper-address | interface           | 1/1/1 |
| IP Helper         | Addresses         |                     |       |
| Interface:        | 1/1/1             |                     |       |
| IP Helper         | Address           | VRF                 |       |
| ----------------- |                   | -----------------   |       |
| 192.168.20.1      |                   | default             |       |
| 192.168.10.1      |                   | default             |       |
| DHCPv6 relay      | agent             |                     |       |
| SupportingVXLAN   | topologiesor      | inter-VRFdeployment |       |
WhendeployingEVPNVXLANorinter-VRFtopologieswherethesourceVRFsfortheDHCPandDHCPclient
aredifferent,itisrecommendedthatyouinstalltheDHCPv6serverintheunderlaysothatthereisonlyone
instanceoftheDHCPv6serverservingoverlayclients.
| Configuringthe | DHCPv6relayagent |     |     |
| -------------- | ---------------- | --- | --- |
Prerequisites
n Anenabledlayer3interface.
Procedure
DHCP|69

1. EnabletheDHCPv6agentwiththecommanddhcpv6-relay.
2. ConfigureoneormoreIPhelperaddresseswiththecommandipv6 helper-address.This
determineswheretheDHCPv6agentforwardDHCPrequests.
3. IfyouwanttoenableDHCPoption79supporttoforwardclientlink-layeraddresses,usethe
|     | commanddhcpv6-relay |     | option 79. |     |     |
| --- | ------------------- | --- | ---------- | --- | --- |
4. ReviewDHCPv6relayagentconfigurationsettingswiththecommandsshow dhcpv6-relayandshow
ipv6 helper-address.
Example
Thisexamplecreatesthefollowingconfiguration:
|     | n EnablestheDHCPv6relayagent. |     |     |     |     |
| --- | ----------------------------- | --- | --- | --- | --- |
Enablesinterface1/1/2andassignsanIPv6addresstoit.(Bydefault,allinterfacesarelayer3and
n
disabled.)
|     | n DefinesanIPhelperaddressofFF01::1:1000oninterface1/1/2. |     |     |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- | --- |
EnablesDHCPoption79.
n
|     | switch(config)#    | dhcpv6-relay |       |     |     |
| --- | ------------------ | ------------ | ----- | --- | --- |
|     | switch(config)#    | interface    | 1/1/2 |     |     |
|     | switch(config-if)# | no shutdown  |       |     |     |
switch(config-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
|     | switch(config-if)# | ip helper-address |        | FF01::1:1000 |     |
| --- | ------------------ | ----------------- | ------ | ------------ | --- |
|     | switch(config-if)# | exit              |        |              |     |
|     | switch(config)#    | dhcpv6-relay      | option | 79           |     |
DHCPv6relayscenario1
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
Procedure
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 70  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

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
DHCPv6relayscenario2
(Thisscenarioisnotsupportedonthe6200SwitchSeries.)
Inthisscenario,thetwohostcomputerscommunicatewithtwodifferentDHCPservers.Eachserveris
reachedonadifferentVRF.Thephysicaltopologyofthenetworklookslikethis:
Procedure
DHCP|71

1. CreatethetwoVRFs.
switch# config
|     | switch(config)# | vrf vrf 1 |     |     |     |
| --- | --------------- | --------- | --- | --- | --- |
|     | switch(config)# | vrf vrf 2 |     |     |     |
2. Configureinterface1/1/1.SetitsIPaddress,associateitwithVRF1,anddefinethehelperIPaddress
toreachDHCPserver1.
switch(configif)#
|     |                   | interface           | 1/1/1      |                 |     |
| --- | ----------------- | ------------------- | ---------- | --------------- | --- |
|     | switch(configif)# | vrf attach          | vrf1       |                 |     |
|     | switch(configif)# | ipv6 address        | 20.0.0.1/8 |                 |     |
|     | switch(configif)# | ipv6 helper-address |            | unicast 1040::2 |     |
3. Configureinterface1/1/2.SetitsIPaddressandassociateitwithVRF1.
|     | switch(configif)# | interface    | 1/1/2       |     |     |
| --- | ----------------- | ------------ | ----------- | --- | --- |
|     | switch(configif)# | vrf attach   | vrf1        |     |     |
|     | switch(configif)# | ipv6 address | 1040::1/120 |     |     |
4. Configureinterface1/1/3.SetitsIPaddressandassociateitwithVRF1.
|     | switch(configif)# | interface    | 1/1/3       |     |     |
| --- | ----------------- | ------------ | ----------- | --- | --- |
|     | switch(configif)# | vrf attach   | vrf2        |     |     |
|     | switch(configif)# | ipv6 address | 3030::1/120 |     |     |
5. Configureinterface1/1/4.SetitsIPaddress,associateitwithVRF2,anddefinethehelperIPaddress
toreachDHCPserver2.
|                 | switch(configif)# | interface           | 1/1/4       |                 |     |
| --------------- | ----------------- | ------------------- | ----------- | --------------- | --- |
|                 | switch(configif)# | vrf attach          | vrf2        |                 |     |
|                 | switch(configif)# | ipv6 address        | 4040::1/120 |                 |     |
|                 | switch(configif)# | ipv6 helper-address |             | unicast 3030::2 |     |
| DHCPrelay(IPv6) | commands          |                     |             |                 |     |
dhcpv6-relay
Syntax
dhcpv6-relay
| no  | dhcpv6-relay |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- |
Description
EnablesDHCPv6relaysupport.DHCPv6relayisdisabledbydefault.
DHCPrelayisnotsupportedonthemanagementinterface
ThenoformofthiscommanddisablesDHCPrelaysupport.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablesDHCPv6relaysupport.
|     | switch(config)# dhcpv6-relay |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- |
RemovesDHCPv6relaysupport.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     | SwitchSeries) |     |     | 72  |
| --------------------------------------- | --- | ------------- | --- | --- | --- |

| switch(config)#     | no dhcpv6-relay |     |
| ------------------- | --------------- | --- |
| dhcpv6-relay option | 79              |     |
Syntax
| dhcpv6-relay option | 79        |     |
| ------------------- | --------- | --- |
| no dhcpv6-relay     | option 79 |     |
Description
EnablessupportforDHCPrelayoption79.Whenenabled,theDHCPv6relayagentforwardsthelink-layer
addressoftheclient.Thisoptionisdisabledbydefault.
ThenoformofthiscommanddisablessupportforDHCPrelayoption79.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablesDHCPoption79support.
| switch(config)# | dhcpv6-relay | option 79 |
| --------------- | ------------ | --------- |
DisablesDHCPoption79support.
| switch(config)# | no dhcpv6-relay | option 79 |
| --------------- | --------------- | --------- |
ipv6 helper-address
Syntax
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
Commandcontext
config-if
DHCP|73

Parameters

<UNICAST-IPV6-ADDR>

Specifies the unicast helper IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
where x is a hexadecimal number from 0 to F.

<MULTICAST-IPV6-ADDR>

Specifies the multicast helper IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
where x is a hexadecimal number from 0 to F.

all-dhcp-servers

Specifies all the DHCP server IPv6 addresses for the interface.

egress <PORT-NUM>

Specifies the port number on which DHCPv6 service requests are relayed to a multicast destination. The
egress port must be different than the one on which the multicast helper address is configured. Format:
member/slot/port.

vrf <VRF-NAME>

Specifies the name of the VRF from which the specified protocol sets its source IP address.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Defining a multicast IPv6 helper address of 2001:DB8::1 on port 1/1/2:

switch(config-if)# ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress 1/1/2

Removing the IP helper address of 2001:DB8::1 on port 1/1/2:

switch(config-if)# no ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress
1/1/2

show dhcpv6-relay

Syntax

show dhcpv6-relay [vsx-peer]

Description

Shows DHCP relay configuration settings.

Command context

Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

74

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#  | show dhcpv6-relay |           |     |     |
| -------- | ----------------- | --------- | --- | --- |
| DHCPv6   | Relay Agent       | : Enabled |     |     |
| Option   | 79                | : Enabled |     |     |
| showipv6 | helper-address    |           |     |     |
Syntax
| show ipv6 | helper-address | [interface | <INTERFACE-ID>] | [vsx-peer] |
| --------- | -------------- | ---------- | --------------- | ---------- |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
Commandcontext
| Manager | (#) |     |     |     |
| ------- | --- | --- | --- | --- |
Parameters
| interface | <INTERFACE-ID> |     |     |     |
| --------- | -------------- | --- | --- | --- |
Specifiesaninterface.Format:member/slot/port.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch#                                        | show ipv6      | helper-address |           |             |
| ---------------------------------------------- | -------------- | -------------- | --------- | ----------- |
| Interface:                                     | 1/1/1          |                |           |             |
| IPv6                                           | Helper Address |                |           | Egress Port |
| ---------------------------------------------- |                |                |           | ----------- |
| 2001:db8:0:1::                                 |                |                |           | -           |
| FF01::1:1000                                   |                |                |           | 1/1/2       |
| Interface:                                     | 1/1/2          |                |           |             |
| IPv6                                           | Helper Address |                |           | Egress Port |
| --------------------------------------------   |                |                |           | ----------- |
| 2001:db8:0:1::                                 |                |                |           | -           |
| switch#                                        | show ipv6      | helper-address | interface | 1/1/1       |
| Interface:                                     | 1/1/1          |                |           |             |
| IPv6                                           | Helper Address |                |           | Egress Port |
DHCP|75

---------------------------------------------- -----------
2001:db8:0:1::
FF01::1:1000

-
1/1/2

switch# show ipv6 helper-address interface 1/1/1

Interface: 1/1/1
IPv6 Helper Address
Egress Port
---------------------------------------------- -----------
2001:db8:0:1::
FF01::1:1000

-
1/1/2

DHCP server

Overview

The dynamic host configuration protocol (DHCP) enables a server to automate the assignment of IP
addresses, and other networking settings, to host computers. The DHCP server on the switch provides both
IPv4 and IPv6 support and is independently configurable on each VRF.

Key features

n Supports multiple address pools and static address bindings.

n Supports DHCP options, enabling the server to provide additional information about the network when

DHCP clients request an address.

n Supports BOOTP to distribute boot image files using an external TFTP server.

n VRF aware, meaning that DHCP client requests received on an interface are processed by the DHCP
server instance configured for a VRF. DHCP server responses are forwarded to clients on the VRF.

n Supports external storage of lease information on a remote host. This enables the DHCP server to
restore lease information after a reboot or a failure. Lease information is stored in a flat file on the
configured external device. It is important that the external device provide persistent external storage to
allow restoration of lease information. If external storage is not configured, then after a failure or reboot,
all existing lease information is lost.

n Supports VSX. In a VSX setup, one switch acts as primary and the other switch acts as secondary. The

DHCP server is active only on the primary switch. After a failover, the DHCP server is enabled based on
the state and role of the switch. The state of the DHCP server indicates the operational state of the
server. VSX synchronization supports DHCPv4 and DHCPv6 server, including external storage
configurations. For more information on VSX support, see the ArubaOS-CX Virtual Switching Extension
(VSX) Guide.

DHCP relay interoperation

DHCP server and DHCP relay cannot both be active on interfaces belonging to the same VRF.

Configuring a DHCPv4 server on a VRF

Prerequisites

n An enabled layer 3 interface.

n A VRF.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

76

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

switch(config)# dhcp-server vrf primary
switch(config-dhcp-server)# pool primary-pool
switch(config-dhcp-server-pool)# range 10.0.0.1 10.0.0.100
switch(config-dhcp-server-pool)# lease 12:00:00
switch(config-dhcp-server-pool)# domain-name example.org.in
switch(config-dhcp-server-pool)# default-router ip 10.30.30.1 10.30.30.2

DHCP | 77

|     | switch(config-dhcp-server-pool)# |     | dns-server | 125.0.0.1 | 125.0.0.2 |     |
| --- | -------------------------------- | --- | ---------- | --------- | --------- | --- |
switch(config-dhcp-server-pool)#
|     |                                  |            | static-bind | ip 10.0.0.11    | mac 24:be:05:24:75:73 |     |
| --- | -------------------------------- | ---------- | ----------- | --------------- | --------------------- | --- |
|     | switch(config-dhcp-server-pool)# |            | option      | 3 ip 10.30.30.3 |                       |     |
|     | switch(config-dhcp-server-pool)# |            | exit        |                 |                       |     |
|     | switch(config-dhcp-server)#      |            | enable      |                 |                       |     |
|     | Configuring                      | the DHCPv6 | server on   | a VRF           |                       |     |
Prerequisites
|     | n Anenabledlayer3interface.                                |     |     |     |     |     |
| --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
|     | n AVRF.                                                    |     |     |     |     |     |
|     | n Anexternalstoragedeviceinstalledandconfigured(optional). |     |     |     |     |     |
Procedure
1. AssigntheDHCPv6servertoaVRFwiththecommanddhcpv6-server vrf.Thisswitchestothe
DHCPv6serverconfigurationcontext.
2. IfyouwanttheDHCPservertobethesoleauthorityforIPaddressesontheVRF,enable
authoritativemodewiththecommandauthoritative.
3. DefineanaddresspoolfortheVRFwiththecommandpool.ThisswitchestotheDHCPv6serverpool
context.Customizepoolsettingsasfollows:
a. Definetherangeofaddressesinthepoolwiththecommandrange.
b. SettheDHCPleasetimeforaddressesinthepoolwiththecommandlease.
c. DefineuptofourDNSserverswiththecommanddns-server.
d. Createstaticbindingsforspecificaddressesinthepoolwiththecommandstatic-bind.
e. ConfigurecustomDHCPoptionsforthepoolwiththecommandoption.
f. ExittheDHCPserverpoolcontextwiththecommandexit.
4. EnabletheDHCPv6serverontheVRFwiththecommandenable.
5. ConfiguresupportforpersistentexternalstorageofDHCPsettingswiththecommanddhcv6p-
external-storage.
server
6. ViewDHCPv6serverconfigurationsettingswiththecommandshow dhcpv6-server all-vrfs.
Example
Thisexamplecreatesthefollowingconfiguration:
|     | n ConfiguresaDHCPv6serveronVRFprimary-vrf. |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- |
|     | n Enablesauthoritativemode.                |     |     |     |     |     |
Definesthepoolprimary-poolwiththefollowingsettings:
n
o Addressrange:2001::1to2001::100.
o Leasetime:12hours.
o DNSservers:2101::14and2101::14.
Staticbindingof2001::101forclientID1:0:a0:24:ab:fb:9c.
o
o DHCPcustomoption:22withIPaddress2101::15.
|                                         | n EnablestheDHCPv6server. |     |               |     |     |     |
| --------------------------------------- | ------------------------- | --- | ------------- | --- | --- | --- |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                           |     | SwitchSeries) |     |     | 78  |

| switch(config)# | dhcpv6-server | vrf primary |     |
| --------------- | ------------- | ----------- | --- |
switch(config-dhcpv6-server)#
pool primary-pool
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
Syntax
authoritative
no authoritative
Description
ConfigurestheDHCPv4serverasauthoritativeonthecurrentVRF.Thismeansthattheserveristhesole
authorityforthenetworkontheVRF.Therefore,ifaclientrequestsanIPaddressleaseforwhichtheserver
hasnorecord,theserverrespondswithDHCPNAK,indicatingthattheclientmustnolongerusethatIP
address.Iftheserverisnotauthoritative,thenitwillignoreDHCPv4requestsreceivedforunknownleases
fromunknownhosts.
ThenoformofthiscommanddisablesauthoritativemodeonthecurrentVRF.
Commandcontext
config-dhcp-server
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguresDHCPv4serverauthoritativemodeonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary   |     |
| --------------------------- | ----------- | ------------- | --- |
| switch(config-dhcp-server)# |             | authoritative |     |
RemovestheDHCPv4serverauthoritativemodeonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary      |     |
| --------------------------- | ----------- | ---------------- | --- |
| switch(config-dhcp-server)# |             | no authoritative |     |
bootp
Syntax
bootp <REMOTE-URL>
no bootp <REMOTE-URL>
DHCP|79

Description
SetstheBOOTPoptionsthatarereturnedbytheDHCPv4serverforthecurrentpool.BOOTPprovidesa
waytodistributeanIPaddressandbootimagefiletoclientstations.TheDHCPv4serverreturnstheIP
addressandthelocationofthebootimagefile,whichmustbestoredonanexternalTFTPserver.
ThenoformofthiscommanddisablessupportforBOOTP.
Commandcontext
config-dhcp-server-pool
Parameters
<REMOTE-URL>
SpecifiesthenameandlocationofaBOOTPfileonaTFTPserverintheformat:
|     | tftp://{<IP> | | <HOST>}/<FILE> |     |     |
| --- | -------------- | -------------- | --- | --- |
n <IP>:SpecifiestheIPaddressoftheTFTPserverhostingthefileinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.
n <HOST>:Specifiesthefully-qualifieddomainnameoftheTFTPserverhostingthefile.Range:1to64
printableASCIIcharacters.
<FILE>:SpecifiesthenameoftheBOOTPfile.Range:1to64printableASCIIcharacters.
n
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DefinesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
|     | switch(config)#             | dhcp-server | vrf primary       |     |
| --- | --------------------------- | ----------- | ----------------- | --- |
|     | switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# bootp tftp://10.0.0.1/mybootfile
DeletesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
|     | switch(config)#             | dhcp-server | vrf primary       |     |
| --- | --------------------------- | ----------- | ----------------- | --- |
|     | switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)#
no bootp tftp://10.0.0.1/mybootfile
|     | clear dhcp-server | leases |     |     |
| --- | ----------------- | ------ | --- | --- |
Syntax
clear dhcp-server leases [all-vrfs | <IPV4-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv4serverleaseinformation.TheDHCPv4servermustbedisabledbeforeclearinglease
information.
Commandcontext
|     | Manager (#) |     |     |     |
| --- | ----------- | --- | --- | --- |
Parameters
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 80  |
| --------------------------------------- | --- | --- | ------------- | --- |

all-vrfs
ClearsleasesforallVRFs.
| <IPV4-ADDR> vrf | <VRF-NAME> |     |     |
| --------------- | ---------- | --- | --- |
ClearstheleaseforaspecificclientonaspecificVRF.SpecifytheclientaddressinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.Youcanremoveleadingzeros.Forexample,theaddress
192.169.005.100becomes192.168.5.100.
vrf <VRF-NAME>
ClearsleasesforaspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ClearingallDHCPv4serverleases.
| switch(config)#             | dhcp-server | vrf primary |     |
| --------------------------- | ----------- | ----------- | --- |
| switch(config-dhcp-server)# |             | disable     |     |
| switch(config-dhcp-server)# |             | exit        |     |
| switch(config)#             | exit        |             |     |
| switch# clear               | dhcp-server | leases      |     |
ClearingallDHCPv4serverleasesforVRFprimary-vrf.
| switch(config)#             | dhcp-server | vrf primary |             |
| --------------------------- | ----------- | ----------- | ----------- |
| switch(config-dhcp-server)# |             | disable     |             |
| switch(config-dhcp-server)# |             | exit        |             |
| switch(config)#             | exit        |             |             |
| switch# clear               | dhcp-server | leases vrf  | primary-vrf |
CleartheDHCPv4serverleaseforIPaddress10.10.10.1onVRFprimary-vrf.
| switch(config)#             | dhcp-server | vrf primary       |                 |
| --------------------------- | ----------- | ----------------- | --------------- |
| switch(config-dhcp-server)# |             | disable           |                 |
| switch(config-dhcp-server)# |             | exit              |                 |
| switch(config)#             | exit        |                   |                 |
| switch# clear               | dhcp-server | leases 10.10.10.1 | vrf primary-vrf |
default-router
Syntax
| default-router    | <IPV4-ADDR-LIST> |     |     |
| ----------------- | ---------------- | --- | --- |
| no default-router | <IPV4-ADDR-LIST> |     |     |
Description
DefinesuptofourdefaultroutersforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddefaultroutersfromthepool.
Commandcontext
config-dhcp-server-pool
DHCP|81

Parameters
<IPV4-ADDR-LIST>
SpecifiestheIPaddressesofthedefaultroutersinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255.Youcanremoveleadingzeros.Forexample,theaddress192.169.005.100becomes
192.168.5.100.Separateaddresseswithaspace.AmaximumoffourIPaddressescanbedefined.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Definestwodefaultrouters,10.0.0.1and10.0.0.10,fortheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#             | dhcp-server | vrf primary       |     |     |
| --- | --------------------------- | ----------- | ----------------- | --- | --- |
|     | switch(config-dhcp-server)# |             | pool primary-pool |     |     |
switch(config-dhcp-server-pool)# default-router ip 10.0.0.1 10.0.0.10
Deletesthedefaultrouter10.0.0.1fromtheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#                  | dhcp-server | vrf primary       |             |     |
| --- | -------------------------------- | ----------- | ----------------- | ----------- | --- |
|     | switch(config-dhcp-server)#      |             | pool primary-pool |             |     |
|     | switch(config-dhcp-server-pool)# |             | no default-router | ip 10.0.0.1 |     |
|     | dhcp-server external-storage     |             |                   |             |     |
Syntax
dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
Description
ConfigurestheexternalstoragefilelocationforDHCPv4serverleaseinformation.Thisfileprovides
persistentstorage,enablingDHCPv4serversettingstoberestoredwhentheswitchisrestarted.Lease
informationisstoredinaflatfileontheconfiguredexternaldevice.
Ifexternalstorageisnotconfigured,thenafterafailureorreboot,allexistingleaseinformationislost.
Leaseinformationissavedtoexternalstorageeachtimethedelaytimerexpires,whichbydefaultisevery
300seconds.
Leaseinformationisnotrestoredwhenissuingthecommanddhcp-server enable.
ThenoformofthiscommandremovesexternalstoragesupportfortheDHCPv4server.
Commandcontext
config
Parameters
<VOLUME-NAME>
Specifiestheexternalstoragevolumename.Range:1to64printableASCIIcharacters.
|     | file <LEASE-FILENAME> |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- |
Specifiestheexternalstoragefilename.Range:1to255printableASCIIcharacters.
|     | delay <DELAY> |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- |
Specifiestheintervalinsecondsbetweenupdatestotheexternalstoragefile.Range:15to86400.
Default:300.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 82  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

Authority

Administrators or local user group members with execution rights for this command.

Example

Stores the lease file on external storage volume Storage1 in file LeaseFile at an interval of 600 seconds.

switch(config)# dhcp-server external-storage Storage1 file LeaseFile delay 600

Disables storage of the lease file on external storage volume Storage1 in file LeaseFile.

switch(config)# no dhcp-server external-storage Storage1 file LeaseFile delay 600

dhcp-server vrf

Syntax

dhcp-server vrf VRF-NAME
no dhcp-server vrf VRF-NAME

Description

Configures the DHCPv4 server to support a VRF and changes to the config-dhcp-server context for
that VRF.

The no form of this command removes DHCPv4 server support on a VRF.

Command context

config

Parameters

VRF-NAME

Name of a VRF.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configures DHCPv4 server support on VRF primary.

switch(config)# dhcp-server vrf primary

Removes DHCPv4 server support on VRF primary.

switch(config)# no dhcp-server vrf primary

disable

Syntax

disable

Description

DHCP | 83

DisablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhenconfigured
onaVRF.
Commandcontext
config-dhcp-server
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DisablestheDHCPv4serveronVRFprimary.
|     | switch(config)#             | dhcp-server | vrf primary |     |     |
| --- | --------------------------- | ----------- | ----------- | --- | --- |
|     | switch(config-dhcp-server)# |             | disable     |     |     |
dns-server
Syntax
|     | dns-server <IPV4-ADDR-LIST>    |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- |
|     | no dns-server <IPV4-ADDR-LIST> |     |     |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
Commandcontext
config-dhcp-server-pool
Parameters
<IPV4-ADDR-LIST>
SpecifiestheIPaddressesoftheDNSserversinIPv4format(x.x.x.x),wherexisadecimalnumberfrom
0to255.Separateaddresseswithaspace.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DefinestwoDNSserversfortheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#                  | dhcp-server | vrf primary       |           |     |
| --- | -------------------------------- | ----------- | ----------------- | --------- | --- |
|     | switch(config-dhcp-server)#      |             | pool primary-pool |           |     |
|     | switch(config-dhcp-server-pool)# |             | dns-server        | 10.0.20.1 |     |
DeletesaDNSserverfromtheserverpoolprimary-poolonVRFprimary.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 84  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

| switch(config)# | dhcp-server | vrf primary |     |
| --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
pool primary-pool
| switch(config-dhcp-server-pool)# |     | no dns-server | 10.0.20.1 |
| -------------------------------- | --- | ------------- | --------- |
domain-name
Syntax
| domain-name <DOMAIN-NAME> |               |     |     |
| ------------------------- | ------------- | --- | --- |
| no domain-name            | <DOMAIN-NAME> |     |     |
Description
DefinesadomainnameforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddomainnamefromthepool.
Commandcontext
config-dhcp-server-pool
Parameters
<DOMAIN-NAME>
Specifiesadomainname.Range:1to255printableASCIIcharacters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Definesadomainnamefortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |                |
| -------------------------------- | ----------- | ----------------- | -------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |                |
| switch(config-dhcp-server-pool)# |             | domain-name       | example.org.in |
Deletesadomainnamefromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |                |
| -------------------------------- | ----------- | ----------------- | -------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |                |
| switch(config-dhcp-server-pool)# |             | no domain-name    | example.org.in |
enable
Syntax
enable
Description
EnablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhenconfigured
onaVRF.
Commandcontext
config-dhcp-server
DHCP|85

Authority

Administrators or local user group members with execution rights for this command.

Example

Enables the DHCPv4 server on VRF primary.

switch(config)# dhcp-server vrf primary
switch(config-dhcp-server)# enable

http proxy

Syntax

http-proxy {<FQDN | IPV4-ADDR>} [vrf <VRF-NAME>]
no http-proxy

Description

Specifies HTTP proxy location and VRF.

The no form of this command removes a specified HTTP proxy location.

Command context

config

Parameters

<FQDN>

Specifies FQDN for HTTP proxy location.

<IPV4-ADDR>

Specifies IPV4 address for HTTP proxy location.

<VRF-NAME>

Specifies VRF for HTTP proxy.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n HTTP proxy location can be configured using the CLI/REST interface or auto-configured through the

DHCP server connected to the switch.

n There are three sources for HTTP proxy location:

o User configured HTTP proxy via CLI or REST interface.

o DHCP options received via management/OOBM port.

o DHCP options received via VLAN 1 on supported switch platforms.

nn Operational configuration for HTTP proxy location is determined by the source with the highest priority.

Source priority:

1. User configured.

2. DHCP options received via management/OOBM port.

3. DHCP options received via VLAN 1.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

86

n HTTP proxy location can only be a FQDN or an IPV4 address.

n When HTTP proxy location and VRF are configured, they override any existing HTTP proxy location and VRF.

n If this command is executed without the VRF parameter, the default VRF will be used.

n Port number may need to be specified at the end of the IP address for FQDN to connect via HTTP proxy.

o For example, 8088 is the TCP port number: http-proxy 192.168.248.248:8088

Examples

Specifying a FQDN for HTTP proxy location and MGMT VRF:

switch(config)# http-proxy http-proxy.aruba.com vrf mgmt

Removing HTTP proxy location

switch(config)# no http-proxy

lease

Syntax

lease {<TIME> | infinite}
no lease

Description

Sets the length of the DHCPv4 lease time for the current pool. The lease time determines how long an IP
address is valid before a DHCPv4 client must request that it be renewed.

The no form of this command returns the DHCPv4 lease time to its default value 1 hour.

Command context

config-dhcp-server-pool

Parameters

<TIME>

Sets the DHCPv4 lease time. Format: DD:HH:MM. Default: 01:00:00.

infinite

Sets the DHCPv4 lease time to infinite. This means that addresses do not need to be renewed.

Authority

Administrators or local user group members with execution rights for this command.

Example

Sets the lease time for DHCPv4 server pool primary-pool on VRF primary to 12 hours.

DHCP | 87

|     | switch(config)# | dhcp-server | vrf primary |     |
| --- | --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
pool primary-pool
|     | switch(config-dhcp-server-pool)# |     | lease 00:12:00 |     |
| --- | -------------------------------- | --- | -------------- | --- |
DeletestheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimary.
|     | switch(config)#                  | dhcp-server | vrf primary       |     |
| --- | -------------------------------- | ----------- | ----------------- | --- |
|     | switch(config-dhcp-server)#      |             | pool primary-pool |     |
|     | switch(config-dhcp-server-pool)# |             | no lease 00:12:00 |     |
netbios-name-server
Syntax
|     | netbios-name-server    | <IPV4-ADDR-LIST> |     |     |
| --- | ---------------------- | ---------------- | --- | --- |
|     | no netbios-name-server | <IPV4-ADDR-LIST> |     |     |
Description
DefinesuptofourNetBIOSWINSserversforthecurrentDHCPv4serverpool.WINSisusedbyMicrosoft
DHCPclientstomatchhostnameswithIPaddresses.
ThenoformofthiscommandremovesthespecifiedWINSserversfromthepool.
Commandcontext
config-dhcp-server-pool
Parameters
<IPV4-ADDR-LIST>
SpecifiestheIPaddressesofNetBIOS(WINS)serversinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.Separateaddresseswithaspace.AmaximumoffourIPaddressescanbe
defined.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DefinestwoWINSserversfortheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#             | dhcp-server | vrf primary       |     |
| --- | --------------------------- | ----------- | ----------------- | --- |
|     | switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# netbios-name-server ip 10.0.20.1 10.0.30.10
DeletesaWINSserverfromtheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#             | dhcp-server | vrf primary       |     |
| --- | --------------------------- | ----------- | ----------------- | --- |
|     | switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# no netbios-name-server ip 10.0.20.1
netbios-node-type
Syntax
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 88  |
| --------------------------------------- | --- | --- | ------------- | --- |

| netbios-node-type    | <TYPE> |     |     |
| -------------------- | ------ | --- | --- |
| no netbios-node-type | <TYPE> |     |     |
Description
DefinestheNetBIOSnodetypeforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovestheNetBIOSnodetypeforthecurrentpool.
Commandcontext
config-dhcp-server-pool
Parameters
<TYPE>
SpecifiestheNetBIOSnodetype:broadcast,hybrid,mixed,orpeer-to-peer.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DefinestheNetBIOSnodetypebroadcastfortheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |           |
| -------------------------------- | ----------- | ----------------- | --------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |           |
| switch(config-dhcp-server-pool)# |             | netbios-node-type | broadcast |
DeletestheNetBIOSnodetypebroadcastfromtheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary          |           |
| -------------------------------- | ----------- | -------------------- | --------- |
| switch(config-dhcp-server)#      |             | pool primary-pool    |           |
| switch(config-dhcp-server-pool)# |             | no netbios-node-type | broadcast |
option
Syntax
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
Description
DefinescustomDHCPv4optionsforthecurrentDHCPv4serverpool.DHCPv4optionsenabletheDHCPv4
servertoprovideadditionalinformationaboutthenetworkwhenDHCPv4clientsrequestanaddress.
ThenoformofthiscommandremovescustomDHCPv4optionsfromthepool.
Commandcontext
config-dhcp-server-pool
Parameters
<OPTION-NUM>
SpecifiesaDHCPv4optionnumber.ForalistofDHCPv4optionnumbers,see
https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml.Range:2to
254.
ascii <ASCII-STR>
DHCP|89

SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:1to255ASCIIcharacters.
|     | hex <HEX-STR> |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- |
Specifiesavaluefortheselectedoptionasahexadecimalstring.Range:1to255hexadecimalcharacters.
|     | ip <IPV4-ADDR-LIST> |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
SpecifiesalistofIPaddressesinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
Separateaddresseswithaspace.AmaximumoffourIPaddressescanbedefined.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DefinesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#                  | dhcp-server | vrf primary       |                  |     |
| --- | -------------------------------- | ----------- | ----------------- | ---------------- | --- |
|     | switch(config-dhcp-server)#      |             | pool primary-pool |                  |     |
|     | switch(config-dhcp-server-pool)# |             | option            | 3 ip 192.168.1.1 |     |
DeletesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#                  | dhcp-server | vrf primary       |                  |     |
| --- | -------------------------------- | ----------- | ----------------- | ---------------- | --- |
|     | switch(config-dhcp-server)#      |             | pool primary-pool |                  |     |
|     | switch(config-dhcp-server-pool)# |             | no option         | 3 ip 192.168.1.1 |     |
pool
Syntax
|     | pool <POOL-NAME>    |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- |
|     | no pool <POOL-NAME> |     |     |     |     |
Description
CreatesaDHCPv4serverpoolforthecurrentVRFandswitchestotheconfig-dhcp-server-poolcontext
forit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64pools(IPv4and
IPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv4serverpool.
Commandcontext
config-dhcp-server
Parameters
<POOL-NAME>
SpecifiestheDHCPv4poolname.Amaximumof64pools(IPv4andIPv6)aresupportedacrossVRFson
theswitch.Range:1to32printableASCIIcharacters.Firstcharactermustbealetterornumber.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
CreatestheDHCv4serverpoolprimary-poolonVRFprimary.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 90  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

| switch(config)# |     | dhcp-server | vrf | primary |     |     |
| --------------- | --- | ----------- | --- | ------- | --- | --- |
switch(config-dhcp-server)#
|     |     |     | pool | primary-pool |     |     |
| --- | --- | --- | ---- | ------------ | --- | --- |
switch(config-dhcp-server-pool)#
DeletestheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             |     | dhcp-server | vrf | primary |              |     |
| --------------------------- | --- | ----------- | --- | ------- | ------------ | --- |
| switch(config-dhcp-server)# |     |             | no  | pool    | primary-pool |     |
range
Syntax
| range <LOW-IPV4-ADDR>    |     | <HIGH-IPV4-ADDR> |                  |     | [prefix-len | <MASK>] |
| ------------------------ | --- | ---------------- | ---------------- | --- | ----------- | ------- |
| no range <LOW-IPV4-ADDR> |     |                  | <HIGH-IPV4-ADDR> |     | [prefix-len | <MASK>] |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv4serverpool.Amaximumof64ranges
aresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
Commandcontext
config-dhcp-server-pool
Parameters
<LOW-IPV4-ADDR>
SpecifiesthelowestIPaddressinthepoolinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0
to255.
<HIGH-IPV4-ADDR>
SpecifiesthehighestIPaddressinthepoolinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0
to255.
| prefix-len <MASK> |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- |
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat(x),wherexisadecimalnumberfrom0
to32.
Whenactivegatewayisconfiguredontheinterfaceservicedbythepool,youmustspecifyaprefixlengththat
matchesthemaskontheIPaddressassignedtotheinterface.Otherwise,clientstationswillgetaprefixlength
fromactivegatewaythatmaynotbeconsistentwiththeconfiguredrange,andaDHCPerrorwilloccur.Inthe
followingexample,theDHCPrangeprefixissetto16tomatchthemaskontheIPaddressassignedtointerface
VLAN2.
| switch(config)#         | interface |     | vlan 2  |              |     |     |
| ----------------------- | --------- | --- | ------- | ------------ | --- | --- |
| switch(config-if-vlan)# |           | ip  | address | 200.1.1.1/16 |     |     |
switch(config-if-vlan)# active-gateway ip 200.1.1.3 mac 00:aa:aa:aa:aa:aa
| switch(config-if-vlan)#     |             | exit |      |              |     |     |
| --------------------------- | ----------- | ---- | ---- | ------------ | --- | --- |
| switch(config)#             | dhcp-server |      | vrf  | primary      |     |     |
| switch(config-dhcp-server)# |             |      | pool | primary-pool |     |     |
switch(config-dhcp-server-pool)# range 192.168.1.1 192.168.1.100 prefix-len 16
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
DHCP|91

Example
Definestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfortheDHCPv4server
poolprimary-poolonVRFprimary.
|     | switch(config)#             | dhcp-server | vrf primary       |     |
| --- | --------------------------- | ----------- | ----------------- | --- |
|     | switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# 192.168.1.1 192.168.1.100 prefix-len 24
Deletestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfromtheDHCPv4server
poolprimary-poolonVRFprimary.
|     | switch(config)# | dhcp-server | vrf primary |     |
| --- | --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
pool primary-pool
switch(config-dhcp-server-pool)# no 192.168.1.1 192.168.1.100 prefix-len 24
|     | show dhcp-server |     |     |     |
| --- | ---------------- | --- | --- | --- |
Syntax
|     | show dhcp-server | [all-vrfs]       |                   |     |
| --- | ---------------- | ---------------- | ----------------- | --- |
|     | show dhcp-server | leases {all-vrfs | | vrf <VRF-NAME>} |     |
|     | show dhcp-server | pool <POOL-NAME> | [vrf <VRF-NAME>]  |     |
Description
ShowsconfigurationsettingsfortheDHCPv4server.
Commandcontext
Manager(#)
Parameters
all-vrfs
ShowsDHCPv4serverconfigurationsettingsforallVRFs.
|     | leases {all-vrfs | | vrf <VRF-NAME>} |     |     |
| --- | ---------------- | ----------------- | --- | --- |
ShowsDHCPv4serverleaseconfigurationsettingsforallVRFsoraspecificVRF.
|     | pool <POOL-NAME> | [vrf <VRF-NAME>] |     |     |
| --- | ---------------- | ---------------- | --- | --- |
ShowsDHCPv4serverpoolconfigurationsettingsforallVRFsoraspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingallDHCPv4serverconfigurationsettings.
|                                         | switch# show | dhcp-server |               |     |
| --------------------------------------- | ------------ | ----------- | ------------- | --- |
|                                         | VRF Name     | : default   |               |     |
|                                         | DHCP Server  | : enabled   |               |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |              |             | SwitchSeries) | 92  |

| Operational    | State | : operational |     |     |     |     |
| -------------- | ----- | ------------- | --- | --- | --- | --- |
| Authoritative  | Mode  | : false       |     |     |     |     |
| Pool Name      |       | : test        |     |     |     |     |
| Lease Duration |       | : 00:01:00    |     |     |     |     |
| DHCP dynamic   | IP    | allocation    |     |     |     |     |
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
| Option-Number |     | Option-Type |     | Option-Value |          |                   |
| ------------- | --- | ----------- | --- | ------------ | -------- | ----------------- |
| ------------- |     | ----------- |     | ------------ |          |                   |
| 6             |     | ip          |     | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 10.0.0.6 |
| 18            |     | ascii       |     | aswed        |          |                   |
DHCP|93

|     | DHCP | Server static | IP  | allocation |     |     |     |     |     |
| --- | ---- | ------------- | --- | ---------- | --- | --- | --- | --- | --- |
--------------------------------
|     | IP-Address |     | Client-Hostname |     | MAC-Address       |     |     |     |     |
| --- | ---------- | --- | --------------- | --- | ----------------- | --- | --- | --- | --- |
|     | ---------- |     | --------------- |     | ----------------- |     |     |     |     |
|     | 10.0.0.1   |     | *               |     | aa:bb:cc:11:12:a4 |     |     |     |     |
|     | 20.0.0.1   |     | *               |     | 11:22:11:22:aa:dd |     |     |     |     |
BOOTP Options
---------------
|     | Boot-File-Name |     | TFTP-Server-Name |     |     | State       |     | TFTP-Server-Address   |     |
| --- | -------------- | --- | ---------------- | --- | --- | ----------- | --- | --------------------- | --- |
|     | -------------- |     | ---------------- |     |     | ------      |     | --------------------- |     |
|     | boot.txt       |     | *                |     |     | OPERATIONAL |     | 10.0.0.10             |     |
static-bind
Syntax
|     | static-bind    | ip <IPV4-ADDR>   |     | mac <MAC-ADDR> |     | [hostname | <HOST>] |     |     |
| --- | -------------- | ---------------- | --- | -------------- | --- | --------- | ------- | --- | --- |
|     | no static-bind | <IPV4-ADDR-LIST> |     |                |     |           |         |     |     |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaspecificMACaddress.This
causestheDHCPv4servertoonlyassignthespecifiedIPaddresstoaclientstationwiththespecifiedMAC
address.
Thenoformofthiscommandremovesthespecifiedbinding.
Commandcontext
config-dhcp-server-pool
Parameters
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.TheIP
addressmustbewithintheaddressrangedefinedforthecurrentpool.
|     | mac <MAC-ADDR> |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
SpecifiesaclientstationMACaddress(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0to
F.
|     | hostname | <HOST> |     |     |     |     |     |     |     |
| --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Specifiesthehostnameoftheclientstation.Range:1to255printableASCIIcharacters
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Definesastaticaddressfortheserverpoolprimary-poolonVRFprimary.
|     | switch(config)#             |     | dhcp-server | vrf  | primary      |     |     |     |     |
| --- | --------------------------- | --- | ----------- | ---- | ------------ | --- | --- | --- | --- |
|     | switch(config-dhcp-server)# |     |             | pool | primary-pool |     |     |     |     |
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
Deletesastaticaddressfromtheserverpoolprimary-poolonVRFprimary.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) |     |     |     |     | 94  |
| --------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |

switch(config)# dhcp-server vrf primary
switch(config-dhcp-server)# pool primary-pool
switch(config-dhcp-server-pool)# no static-bind ip 10.0.0.1 mac 24:be:05:24:75:73

DHCP server IPv6 commands

authoritative

Syntax

authoritative
no authoritative

Description

Configures the DHCPv6 server as authoritative on the current VRF. This means that the server is the sole
authority for the network on the VRF. It responds to client solicit messages with advertise messages having
a priority/preference value set to 255 (the maximum), instead of 0 (the minimum). Clients always choose
the DHCPv6 server with the highest priority/preference value. If two DHCPv6 servers send an advertise
message with the same priority/preference value, then the client picks one and discards the other.

The no form of this command disables authoritative mode on the current VRF.

Command context

config-dhcpv6-server

Authority

Administrators or local user group members with execution rights for this command.

Example

Configures DHCPv6 server authoritative mode on VRF primary.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# authoritative

Removes DHCPv6 server authoritative mode on VRF primary.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# no authoritative

clear dhcpv6-server leases

Syntax

clear dhcpv6-server leases [all-vrfs | <IPV6-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]

Description

Clears DHCPv6 server lease information. The DHCPv6 server must be disabled before clearing lease
information.

Command context

Manager (#)

DHCP | 95

Parameters
all-vrfs
ClearsleasesforallVRFs.
|     | <IPV6-ADDR> vrf | <VRF-NAME> |     |     |     |
| --- | --------------- | ---------- | --- | --- | --- |
ClearstheleaseforaspecificclientonaspecificVRF.SpecifytheclientaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisahexadecimalnumberfrom0toF.Youcan
usetwocolons(::)torepresentconsecutivezeros(butonlyonce),removeleadingzeros,andcollapsea
hextetoffourzerostoasingle0.Forexample,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes2222:0:3333::4444:55.
|     | vrf <VRF-NAME> |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- |
ClearsleasesforaspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ClearingallDHCPv6serverleases.
|     | switch(config)#               | dhcpv6-server | vrf primary |     |     |
| --- | ----------------------------- | ------------- | ----------- | --- | --- |
|     | switch(config-dhcpv6-server)# |               | disable     |     |     |
|     | switch(config-dhcpv6-server)# |               | exit        |     |     |
|     | switch(config)#               | exit          |             |     |     |
|     | switch# clear                 | dhcpv6-server | leases      |     |     |
ClearingallDHCPv6serverleasesforVRFprimary-vrf.
|     | switch(config)#               | dhcpv6-server | vrf primary |             |     |
| --- | ----------------------------- | ------------- | ----------- | ----------- | --- |
|     | switch(config-dhcpv6-server)# |               | disable     |             |     |
|     | switch(config-dhcpv6-server)# |               | exit        |             |     |
|     | switch(config)#               | exit          |             |             |     |
|     | switch# clear                 | dhcpv6-server | leases vrf  | primary-vrf |     |
CleartheDHCPv6serverleaseforIPaddress2001::1onVRFprimary-vrf.
|     | switch(config)#               | dhcpv6-server    | vrf primary    |                 |     |
| --- | ----------------------------- | ---------------- | -------------- | --------------- | --- |
|     | switch(config-dhcpv6-server)# |                  | disable        |                 |     |
|     | switch(config-dhcpv6-server)# |                  | exit           |                 |     |
|     | switch(config)#               | exit             |                |                 |     |
|     | switch# clear                 | dhcpv6-server    | leases 2001::1 | vrf primary-vrf |     |
|     | dhcv6p-server                 | external-storage |                |                 |     |
Syntax
dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
Description
ConfigurestheexternalstoragefilelocationforDHCPv6serverleaseinformation.Thisfileprovides
persistentstorage,enablingDHCPv6serversettingstoberestoredwhentheswitchisrestarted.Lease
informationisstoredinaflatfileontheconfiguredexternaldevice.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 96  |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

If external storage is not configured, then after a failure or reboot, all existing lease information is lost.

Lease information is saved to external storage each time the delay timer expires, which by default is every
300 seconds.

Lease information is not restored when issuing the command dhcp-server enable.

The no form of this command removes external storage support for the DHCPv6 server.

Command context

config

Parameters

<VOLUME-NAME>

Specifies the external storage volume name. Range: 1 to 64 printable ASCII characters.

file <LEASE-FILENAME>

Specifies the external storage filename. Range: 1 to 255 printable ASCII characters.

delay <DELAY>

Specifies the interval in seconds between updates to the external storage file. Range: 15 to 86400.
Default: 300.

Authority

Administrators or local user group members with execution rights for this command.

Example

Stores the lease file on external storage volume Storage1 in file LeaseFile at an interval of 600 seconds.

switch(config)# dhcpv6-server external-storage Storage1 file LeaseFile delay 600

Disables storage of the lease file on external storage volume Storage1 in file LeaseFile.

switch(config)# no dhcpv6-server external-storage Storage1 file LeaseFile delay 600

dhcpv6-server vrf

Syntax

dhcpv6-server vrf VRF-NAME
no dhcpv6-server vrf VRF-NAME

Description

Configures the DHCPv6 server to support a VRF and changes to the config-dhcpv6-server context for that
VRF.

The no form of this command removes DHCPv6 server support on a VRF.

Command context

config

Parameters

VRF-NAME

Name of a VRF.

DHCP | 97

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfiguresDHCPv6serversupportonVRFprimary.
|     | switch(config)# | dhcpv6-server | vrf primary |     |
| --- | --------------- | ------------- | ----------- | --- |
RemovestheDHCPv6serversupportonVRFprimary.
|     | switch(config)# | no dhcpv6-server | vrf primary |     |
| --- | --------------- | ---------------- | ----------- | --- |
disable
Syntax
disable
Description
DisablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhenconfigured
onaVRF.
Commandcontext
config-dhcpv6-server
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DisablestheDHCPv6serveronVRFprimary.
|     | switch(config)#               | dhcpv6-server | vrf primary |     |
| --- | ----------------------------- | ------------- | ----------- | --- |
|     | switch(config-dhcpv6-server)# |               | disable     |     |
dns-server
Syntax
|     | dns-server <IPVv6-ADDR-LIST>    |     |     |     |
| --- | ------------------------------- | --- | --- | --- |
|     | no dns-server <IPVv6-ADDR-LIST> |     |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
Commandcontext
config-dhcpv6-server-pool
Parameters
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 98  |
| --------------------------------------- | --- | --- | ------------- | --- |

<IPVv6-ADDR-LIST>
SpecifiestheIPaddressesoftheDNSserversinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisahexadecimalnumberfrom0toF.Separate
addresseswithaspace.AmaximumoffourIPaddressescanbedefined.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DefinesDNSserver2001::13fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf primary       |          |
| ---------------------------------- | ------------- | ----------------- | -------- |
| switch(config-dhcpv6-server)#      |               | pool primary-pool |          |
| switch(config-dhcpv6-server-pool)# |               | dns-server        | 2001::13 |
DeletesDNSserver2001::13fromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf primary       |          |
| ---------------------------------- | ------------- | ----------------- | -------- |
| switch(config-dhcpv6-server)#      |               | pool primary-pool |          |
| switch(config-dhcpv6-server-pool)# |               | no dns-server     | 2001::13 |
enable
Syntax
enable
Description
EnablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhenconfigured
onaVRF.
Commandcontext
config-dhcpv6-server
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
EnablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcp-server | vrf primary |     |
| ----------------------------- | ----------- | ----------- | --- |
| switch(config-dhcpv6-server)# |             | enable      |     |
lease
Syntax
| lease {<TIME> | | infinite} |     |     |
| --------------- | --------- | --- | --- |
no lease
Description
DHCP|99

SetsthelengthoftheDHCPv6leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv6clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv6leasetimetothedefaultvalue1hour.
Commandcontext
config-dhcpv6-server-pool
Parameters
<TIME>
SetstheDHCPv6leasetime.Format:DD:HH:MM.Default:01:00:00.
infinite
SetstheDHCPv6leasetimetoinfinite.Thismeansthataddressesdonotneedtoberenewed.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
SetstheleasetimeforDHCPv6serverpoolprimary-poolonVRFprimaryto12hours.
|     | switch(config)#               | dhcpv6-server | vrf primary       |     |
| --- | ----------------------------- | ------------- | ----------------- | --- |
|     | switch(config-dhcpv6-server)# |               | pool primary-pool |     |
switch(config-dhcpv6-server-pool)# lease 00:12:00
SetstheleasetimeforDHCPserverpoolprimary-poolonVRFprimarytothedefaultvalue.
|     | switch(config)#               | dhcpv6-server | vrf primary       |     |
| --- | ----------------------------- | ------------- | ----------------- | --- |
|     | switch(config-dhcpv6-server)# |               | pool primary-pool |     |
switch(config-dhcpv6-server-pool)# no lease 00:12:00
option
Syntax
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV6-ADDR-LIST>}
Description
DefinescustomDHCPv6optionsforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovescustomDHCPv6optionsfromthepool.
Commandcontext
config-dhcpv6-server-pool
Parameters
<OPTION-NUM>
SpecifiesaDHCPv6optionnumber.Range:2to254.
|     | ascii <ASCII-STR> |     |     |     |
| --- | ----------------- | --- | --- | --- |
SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:1to255ASCIIcharacters.
|     | hex <HEX-STR> |     |     |     |
| --- | ------------- | --- | --- | --- |
Specifiesavaluefortheselectedoptionasahexadecimalstring.Range:1to255hexadecimalcharacters.
|                                         | ip <IPV6-ADDR-LIST> |     |               |     |
| --------------------------------------- | ------------------- | --- | ------------- | --- |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                     |     | SwitchSeries) | 100 |

Specifies a list of IP addresses for the option in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from 0 to F.

Authority

Administrators or local user group members with execution rights for this command.

Example

Defines DHCPv6 option 22 for the server pool primary-pool on VRF primary.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# pool primary-pool
switch(config-dhcpv6-server-pool)# option 22 ipv6 2001::12

Deletes DHCPv6 option 22 for the server pool primary-pool on VRF primary.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# pool primary-pool
switch(config-dhcpv6-server-pool)# no option 22 ipv6 2001::12

pool

Syntax

pool <POOL-NAME>
no pool <POOL-NAME>

Description

Creates a DHCPv6 server pool for the current VRF and switches to the config-dhcpv6-server-pool context
for it. Multiple pools, each with a distinct range, can be assigned to a VRF. A maximum of 64 pools (IPv4 and
IPv6), 64 address ranges, and 8182 clients are supported on the switch across all VRFs.

The no form of this command deletes the specified DHCPv6 server pool.

Command context

config-dhcpv6-server

Parameters

<POOL-NAME>

Specifies the DHCPv6 pool name. A maximum of 64 pools (IPv4 and IPv6) are supported across VRFs on the
switch. Range: 1 to 32 printable ASCII characters. First character must be a letter or number.

Authority

Administrators or local user group members with execution rights for this command.

Example

Creates the DHCPv6 server pool primary-pool on VRF primary.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# pool primary-pool
switch(config-dhcpv6-server-pool)#

Deletes the DHCPv6 server pool primary-pool on VRF primary.

DHCP | 101

|     | switch(config)# | dhcpv6-server |     | vrf primary |     |     |
| --- | --------------- | ------------- | --- | ----------- | --- | --- |
switch(config-dhcpv6-server)#
|     |     |     |     | no pool primary-pool |     |     |
| --- | --- | --- | --- | -------------------- | --- | --- |
range
Syntax
|     | range <LOW-IPV6-ADDR>    | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |     |
| --- | ------------------------ | ---------------- | --- | ----------- | ------- | --- |
|     | no range <LOW-IPV6-ADDR> | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |     |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv6serverpool.Amaximumof64ranges
aresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
Commandcontext
config-dhcpv6-server-pool
Parameters
<LOW-IPV6-ADDR>
SpecifiesthelowestIPaddressinthepoolinIPv6format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),
wherexisahexadecimalnumberfrom0toF.
<HIGH-IPV6-ADDR>
SpecifiesthehighestIPaddressinthepoolinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisahexadecimalnumberfrom0toF.
|     | prefix-len <MASK> |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- |
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat(x),wherexisadecimalnumberfrom64
to128.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
DefinesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
|     | switch(config)#               | dhcpv6-server |     | vrf primary       |     |     |
| --- | ----------------------------- | ------------- | --- | ----------------- | --- | --- |
|     | switch(config-dhcpv6-server)# |               |     | pool primary-pool |     |     |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::10 prefix-len 64
DeletesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
|     | switch(config)#               | dhcpv6-server |     | vrf primary       |     |     |
| --- | ----------------------------- | ------------- | --- | ----------------- | --- | --- |
|     | switch(config-dhcpv6-server)# |               |     | pool primary-pool |     |     |
switch(config-dhcpv6-server-pool)# no range 2001::1 2001::10 prefix-len 64
|     | show dhcpv6-server |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
Syntax
|                                         | show dhcpv6-server | [all-vrfs]       |               |                   |     |     |
| --------------------------------------- | ------------------ | ---------------- | ------------- | ----------------- | --- | --- |
|                                         | show dhcpv6-server | leases {all-vrfs |               | | vrf <VRF-NAME>} |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |                  | SwitchSeries) |                   |     | 102 |

| show dhcpv6-server |     | pool | <POOL-NAME> | [vrf | <VRF-NAME>] |
| ------------------ | --- | ---- | ----------- | ---- | ----------- |
Description
ShowsconfigurationsettingsfortheDHCPv6server.
Commandcontext
Manager(#)
Parameters
all-vrfs
ShowsDHCPv6serverconfigurationsettingsforallVRFs.
| leases {all-vrfs | |   | vrf <VRF-NAME>} |     |     |     |
| ---------------- | --- | --------------- | --- | --- | --- |
ShowsDHCPv6serverleaseconfigurationsettingsforallVRFsoraspecificVRF.
| pool <POOL-NAME> | [vrf | <VRF-NAME>] |     |     |     |
| ---------------- | ---- | ----------- | --- | --- | --- |
ShowsDHCPv6serverpoolconfigurationsettingsforallVRFsoraspecificVRF.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingallDHCPv6serverconfigurationsettings.
| switch# show   | dhcpv6-server |               |             |     |     |
| -------------- | ------------- | ------------- | ----------- | --- | --- |
| VRF Name       |               | :             | default     |     |     |
| DHCPv6 Server  |               | :             | enabled     |     |     |
| Operational    | State         | :             | operational |     |     |
| Authoritative  | Mode          | :             | true        |     |     |
| Pool Name      |               | :             | test        |     |     |
| Lease Duration |               | :             | 00:01:00    |     |     |
| DHCPV6 dynamic |               | IP allocation |             |     |     |
-----------------------------
| Start-IPv6-Address |         | End-IPv6-Address |     |     | Prefix-Length |
| ------------------ | ------- | ---------------- | --- | --- | ------------- |
| ------------------ |         | ---------------- |     |     | ------------- |
| 2001::2            |         | 2001::10         |     |     | 64            |
| DHCPv6 Server      | options |                  |     |     |               |
---------------------
| Option-Number |        | Option-Type |               | Option-Value |     |
| ------------- | ------ | ----------- | ------------- | ------------ | --- |
| ------------- |        | ----------- |               | ------------ |     |
| 7             |        | ipv6        |               | 2001::15     |     |
| DHCvP6 Server | static |             | IP allocation |              |     |
-----------------------------------
| DHCPv6 Server | static |     | host is | not configured. |     |
| ------------- | ------ | --- | ------- | --------------- | --- |
ShowingDHCPv6serverconfigurationsettingsforVRFprimary-vrf.
| switch# show | dhcpv6-server |     | vrf         | primary-vrf |     |
| ------------ | ------------- | --- | ----------- | ----------- | --- |
| VRF Name     |               | :   | primary-vrf |             |     |
DHCP|103

|     | DHCPv6        | Server   |               | : disabled |     |     |     |     |
| --- | ------------- | -------- | ------------- | ---------- | --- | --- | --- | --- |
|     | Operational   | State    |               | : standby  |     |     |     |     |
|     | Authoritative |          | Mode          | : false    |     |     |     |     |
|     | Pool          | Name     |               | : test     |     |     |     |     |
|     | Lease         | Duration |               | : 00:01:00 |     |     |     |     |
|     | DHCPV6        | dynamic  | IP allocation |            |     |     |     |     |
-----------------------------
|     | Start-IPv6-Address |        |         | End-IPv6-Address |     | Prefix-Length |     |     |
| --- | ------------------ | ------ | ------- | ---------------- | --- | ------------- | --- | --- |
|     | ------------------ |        |         | ---------------- |     | ------------- |     |     |
|     | 2000::1            |        |         | 2000::20         |     | *             |     |     |
|     | 2001::20           |        |         | 2001::50         |     | *             |     |     |
|     | 2001::2            |        |         | 2001::10         |     | 64            |     |     |
|     | 2010::20           |        |         | 2010::40         |     | *             |     |     |
|     | DHCPv6             | Server | options |                  |     |               |     |     |
---------------------
|     | Option-Number |        | Option-Type |               | Option-Value |     |     |     |
| --- | ------------- | ------ | ----------- | ------------- | ------------ | --- | --- | --- |
|     | ------------- |        | ----------- |               | ------------ |     |     |     |
|     | 7             |        | ipv6        |               | 2001::15     |     |     |     |
|     | 23            |        | ipv6        |               | 2001::30     |     |     |     |
|     | 30            |        | ipv6        |               | 2001::10     |     |     |     |
|     | DHCvP6        | Server | static      | IP allocation |              |     |     |     |
-----------------------------------
|     | DHCPv6 | Server   | static        | host is | not configured. |     |     |     |
| --- | ------ | -------- | ------------- | ------- | --------------- | --- | --- | --- |
|     | Pool   | Name     | : v6test      |         |                 |     |     |     |
|     | Lease  | Duration | : 00:01:00    |         |                 |     |     |     |
|     | DHCPv6 | dynamic  | IP allocation |         |                 |     |     |     |
-----------------------------
|     | Start-IPv6-Address |        |         | End-IPv6-Address |     | Prefix-Length |     |     |
| --- | ------------------ | ------ | ------- | ---------------- | --- | ------------- | --- | --- |
|     | ------------------ |        |         | ---------------- |     | ------------- |     |     |
|     | 2001::1            |        |         | 2001::20         |     | 64            |     |     |
|     | 2010::10           |        |         | 2010::30         |     | *             |     |     |
|     | 2020::20           |        |         | 2020::60         |     | *             |     |     |
|     | DHCPv6             | Server | options |                  |     |               |     |     |
---------------------
|     | Option-Number |     | Option-Type |     | Option-Value                            |     |     |     |
| --- | ------------- | --- | ----------- | --- | --------------------------------------- | --- | --- | --- |
|     | ------------- |     | ----------- |     | -----------------                       |     |     |     |
|     | 7             |     | ipv6        |     | 2001::20                                |     |     |     |
|     | 23            |     | ipv6        |     | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |     |     |
2001:0db8:85a3:0000:0000:8a2e:0370:7335
2001:0db8:85a3:0000:0000:8a2e:0370:7336
2001:0db8:85a3:0000:0000:8a2e:0370:7337
|     | DHCPv6 | Server | static | IP allocation |     |     |     |     |
| --- | ------ | ------ | ------ | ------------- | --- | --- | --- | --- |
------------------------------------
|     | IPv6-Address |     | Client-Hostname |     |     | State       | Client-Id          |     |
| --- | ------------ | --- | --------------- | --- | --- | ----------- | ------------------ | --- |
|     | ------------ |     | --------------- |     |     | ----------- | ---------          |     |
|     | 2100::4      |     | *               |     |     | OPERATIONAL | 1:0:a0:24:ab:fb:9c |     |
static-bind
Syntax
|                                         | static-bind | ipv6 | <IPVv6-ADDR> | client-id     |     | <ID> [hostname | <HOST>] |     |
| --------------------------------------- | ----------- | ---- | ------------ | ------------- | --- | -------------- | ------- | --- |
| AOS-CX10.07IPServicesGuide|(6300and6400 |             |      |              | SwitchSeries) |     |                |         | 104 |

no static-bind ipv6 <IPVv6-ADDR-LIST>

Description

Creates a static binding that associates an IP address in the current pool with a client identifier or DUID. This
causes the DHCPv6 server to only assign the specified IP address to a client station with the specified client
identifier or DUID.

The no form of this command removes the specified static binding from the pool.

Command context

config-dhcpv6-server-pool

Parameters

<IPV6-ADDR>

Specifies the IP address to assign in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x
is a hexadecimal number from 0 to F. For example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes 2222:0:3333::4444:55.

client-id <ID>

Specifies the client identifier or DUID.

hostname <HOST>

Specifies the host name of the client station. Range: 1 to 255 printable ASCII characters

Authority

Administrators or local user group members with execution rights for this command.

Example

Defines a static address for the DHCPv6 server pool primary-pool on VRF primary.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# pool primary-pool
switch(config-dhcpv6-server-pool)# static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c

Deletes a static address from the DHCPv6 server pool primary-pool on VRF primary.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# pool primary-pool
switch(config-dhcpv6-server-pool)# no static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c

DHCP | 105

Chapter 6

DHCP snooping

DHCP snooping

Overview

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
legitimate DHCP servers, and untrusted ports connected to general users. DHCP packets are forwarded
between trusted ports without inspection. DHCP packets received on other switch ports are inspected
before being forwarded. DHCP Packets from untrusted sources are dropped.

In addition, in support of the separate IP source lockdown feature, DHCP snooping also dynamically collects
client information (VLAN, IPv4 address, MAC address, interface), adding the information to the switch IP
binding database. Alternatively, also in support of IP lockdown, the IP binding database can be statically
updated using the ipv4 source-binding or ipv6 source-binding commands. Statically configured IP
binding information supersedes any dynamically collected information for the same client.

DHCP Snooping and DHCP relay can be configured on the same switch.

When DHCP snooping and DHCP relay are both enabled on a VLAN, the following actions occur:

n

n

Received packet: DHCP snooping processes the DHCP packet before (possibly) handing it to

DHCP relay.

Transmitted packet: DHCP packets sent by DHCP relay are intercepted by DHCP snooping to

learn IP bindings.

For even more rigorous security that is applied in hardware on a packet-by-packet basis, you can use IP source
lockdown feature as described in IP source lockdown.

DHCPv4 snooping conditions for dropping DHCPv4 packets

Applies only to DHCPv4 snooping.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

106

Packet types that are
dropped

DHCPOFFER, DHCPACK,
DHCPNACK

Conditions for dropping the packets

n A packet from a DHCP server is received on an untrusted port.
n The switch is configured with a list of authorized DHCP server addresses

and a packet is received from a DHCP server on a trusted port with a

source IP address that is not in the list of authorized DHCP server

addresses.

DHCPRELEASE, DHCPDECLINE

A broadcast packet that has a MAC address in the DHCP binding database,

but the port in the DHCP binding database does not match the port on which

the packet is received.

All DHCP packet types

n When enabled (the default) a DHCP packet received on an untrusted port

in which the DHCP client hardware MAC address does not match the

source MAC address in the packet.

n When enabled (the default), a DHCP packet containing DHCP relay

information (option 82) is received from an untrusted port.

DHCPv4 snooping commands

clear dhcpv4-snooping binding

Syntax

clear dhcpv4-snooping binding {all | ip <IPV4-ADDR> vlan <VLAN-ID> |

port <PORT-NUM> | vlan <VLAN-ID>}

Description

Clears DHCPv4 snooping binding entries.

Command context

Operator (>) or Manager (#)

Parameters

all

Specifies that all DHCPv4 binding information is to be cleared.

ip <IPV4-ADDR> vlan <VLAN-ID>

Specifies the IPv4 address and VLAN for which all DHCPv4 binding information is to be cleared.

port <PORT-NUM>

Specifies the port number for which all DHCPv4 binding information is to be cleared.

vlan <VLAN-ID>

Specifies the VLAN for which all DHCPv4 binding information is to be cleared.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

DHCP snooping | 107

ClearingallDHCPv4bindinginformationforIPaddress192.168.2.4andVLAN5:
switch(config)# clear dhcpv4-snooping binding ip 192.168.2.4 vlan 5
ClearingallDHCPv4bindinginformationforport1/1/1:
|     | switch(config)# | clear dhcpv4-snooping |     | binding port | 1/1/1 |     |
| --- | --------------- | --------------------- | --- | ------------ | ----- | --- |
ClearingallDHCPv4bindinginformationforVLAN10:
switch(config)#
|     |     | clear dhcpv4-snooping |     | binding vlan | 10  |     |
| --- | --- | --------------------- | --- | ------------ | --- | --- |
ClearingallDHCPv4bindinginformation:
|     | switch(config)#       | clear dhcpv4-snooping |            | binding all |     |     |
| --- | --------------------- | --------------------- | ---------- | ----------- | --- | --- |
|     | clear dhcpv4-snooping |                       | statistics |             |     |     |
Syntax
|     | clear dhcpv4-snooping | statistics |     |     |     |     |
| --- | --------------------- | ---------- | --- | --- | --- | --- |
Description
ClearsallDHCPv4snoopingstatistics.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ClearallDHCPv4snoopingstatistics:
|     | switch# clear | dhcpv4-snooping | statistics |     |     |     |
| --- | ------------- | --------------- | ---------- | --- | --- | --- |
dhcpv4-snooping
Syntax
dhcpv4-snooping
|     | no dhcpv4-snooping |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
Description
EnablesDHCPv4snooping.DHCPv4snoopingisdisabledbydefault.DHCPsnoopingisnotsupported
onthemanagementinterface.
ThenoformofthecommanddisablesDHCPv4snooping,flushingalltheIPbindingslearnedsince
DHCPv4snoopingwasenabled.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 108 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingDHCPv4snooping:
| switch(config)# dhcpv4-snooping |     |     |
| ------------------------------- | --- | --- |
DisablingDHCPv4snooping:
| switch(config)# no | dhcpv4-snooping |          |
| ------------------ | --------------- | -------- |
| dhcpv4-snooping    | (in config-vlan | context) |
Syntax
dhcpv4-snooping
no dhcpv4-snooping
Description
EnablesDHCPv4snoopingintheconfig-vlancontext.DHCPv4snoopingisdisabledbydefaultforall
VLANs.
ThenoformofthecommanddisablesDHCPv4snoopingonthespecifiedVLAN,flushingalltheIPbindings
learnedforthisVLANsinceDHCPv4snoopingwasenabledforthisVLAN.
Commandcontext
config-vlan
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingDHCPv4snoopingonVLAN100:
| switch(config)# vlan     | 100             |     |
| ------------------------ | --------------- | --- |
| switch(config-vlan-100)# | dhcpv4-snooping |     |
| switch(config-vlan-100)# | exit            |     |
switch(config)#
DisablingDHCPv4snoopingonVLAN100:
| switch(config)# vlan     | 100                |     |
| ------------------------ | ------------------ | --- |
| switch(config-vlan-100)# | no dhcpv4-snooping |     |
| switch(config-vlan-100)# | exit               |     |
switch(config)#
DHCPsnooping|109

|     | dhcpv4-snooping | allow-overwrite-binding |     |     |     |
| --- | --------------- | ----------------------- | --- | --- | --- |
Syntax
|     | dhcpv4-snooping    | allow-overwrite-binding |     |     |     |
| --- | ------------------ | ----------------------- | --- | --- | --- |
|     | no dhcpv4-snooping | allow-overwrite-binding |     |     |     |
Description
AllowsbindingtobeoverwrittenforthesameIPaddress.Whenenabled,andaDHCPserveroffersahostan
IPaddressthatisalreadyboundtoanexistinghostinthebindingtable,theexistingbindingisoverwritten
forthenewhostifthenewhostissuccessfullyabletoacquirethesameIPaddress.Thisoverwritingis
disabledbydefault,causingtheDHCPserverofferstobedropped.
ThenoformofthecommanddisablesDHCPv4snoopingoverwritebinding.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingDHCPv4snoopingoverwritebinding:
|     | switch(config)# | dhcpv4-snooping | allow-overwrite-binding |     |     |
| --- | --------------- | --------------- | ----------------------- | --- | --- |
DisablingDHCPv4snoopingoverwritebinding:
|     | switch(config)# | no dhcpv4-snooping | allow-overwrite-binding |     |     |
| --- | --------------- | ------------------ | ----------------------- | --- | --- |
|     | dhcpv4-snooping | authorized-server  |                         |     |     |
Syntax
|     | dhcpv4-snooping | authorized-server | <IPV4-ADDR> | [vrf <VRF-NAME>] |     |
| --- | --------------- | ----------------- | ----------- | ---------------- | --- |
no dhcpv4-snooping authorized-server <IPV4-ADDR> [vrf <VRF-NAME>]
Description
Addsanauthorized(trusted)DHCPservertoalistofauthorizedserversforusebyDHCPv4snooping.This
commandcanbeissuedmultipletimes,addingamaximumof20authorizedserversperVRF.Bydefault,
withanemptylistofauthorizedservers,allDHCPserversareconsideredtobetrustedforDHCPv4
snoopingpurposes.
ThemgmtVRFcannotbeusedwiththiscommand.
ThenoformofthiscommanddeletesthespecifiedDHCPserverfromtheauthorizedlist.
Commandcontext
config
Parameters
<IPV4-ADDR>
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 110 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

Specifies the IPv4 address of the trusted DHCPv4 server.

vrf <VRF-NAME>

Specifies the VRF name. The name can be default or a configured VRF instance but it cannot be mgmt.

Authority

Administrators or local user group members with execution rights for this command.

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

dhcpv4-snooping external-storage

Syntax

dhcpv4-snooping external-storage volume <VOL-NAME> file <FILE-NAME>

no dhcpv4-snooping external-storage

Description

Configures external storage to be used for backing up IP bindings (used by DHCPv4 snooping) to a file.
When configured, the switch stores all the IP bindings in an external storage file so that they are retained
after the switch restarts. When the switch restarts, it reads the IP bindings from the configured external
storage file to populate its local cache.

The no form of this command disables the saving of IP bindings in an external storage file.

Command context

config

Parameters

volume <VOL-NAME>

Specifies the name of the existing external storage volume where the IP bindings file will be saved.
Before running the dhcpv4-snooping external-storage volume command, first create the external
storage volume using command external-storage <VOLUME-NAME>. See External storage commands in
the Command-Line Interface Guide.

file <FILE-NAME>

Specifies the file name to use for storing IP bindings. Maximum 255 characters.

Authority

Administrators or local user group members with execution rights for this command.

DHCP snooping | 111

Examples
ConfiguringIPbindingsstorageinfiledsnoop_ipbindingsonexistingvolumedhcp_snoop:
switch(config)#
|     |     | dhcpv4-snooping |     | external-storage | volume dhcp_snoop | file dsnoop_ |     |
| --- | --- | --------------- | --- | ---------------- | ----------------- | ------------ | --- |
ipbindings
Disablingexternalstorage:
|     | switch(config)# | no dhcpv4-snooping |     | external-storage |     |     |     |
| --- | --------------- | ------------------ | --- | ---------------- | --- | --- | --- |
|     | dhcpv4-snooping | max-bindings       |     |                  |     |     |     |
Syntax
|     | dhcpv4-snooping    | max-bindings | <MAX-BINDINGS> |     |     |     |     |
| --- | ------------------ | ------------ | -------------- | --- | --- | --- | --- |
|     | no dhcpv4-snooping | max-bindings |                |     |     |     |     |
Description
SetsthemaximumnumberofDHCPbindingsallowedontheselectedinterface.Forallinterfacesonwhich
thiscommandisnotrun,thedefaultmaxbindingsapplies.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
Commandcontext
config-if
Parameters
<MAX-BINDINGS>
SpecifiesthemaximumnumberofDHCPbindings.Youcanusetheshow capacitiescommandtosee
themaximumavailableforyourswitchmodel.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
SettheDHCPmaxbindingsto512oninterface2/2/1:
|     | switch(config)#    | interface       | 2/2/1 |              |     |     |     |
| --- | ------------------ | --------------- | ----- | ------------ | --- | --- | --- |
|     | switch(config-if)# | dhcpv4-snooping |       | max-bindings | 512 |     |     |
switch(config-if)#
exit
switch(config)#
RevertDHCPmaxbindingstoitsdefaultoninterface2/2/1:
|     | switch(config)#    | interface | 2/2/1           |              |     |     |     |
| --- | ------------------ | --------- | --------------- | ------------ | --- | --- | --- |
|     | switch(config-if)# | no        | dhcpv4-snooping | max-bindings |     |     |     |
|     | switch(config-if)# | exit      |                 |              |     |     |     |
switch(config)#
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     |     | 112 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- |

dhcpv4-snooping option 82

Syntax

dhcpv4-snooping option 82 [remote-id {mac | subnet-ip | mgmt-ip}]

[untrusted-policy {drop | keep | replace}]

no dhcpv4-snooping option 82

Description

Configures the addition of option 82 DHCP relay information to DHCP client packets that are being
forwarded on trusted ports. DHCP relay is enabled by default.

In the switch default state and when this command is entered without parameters (dhcpv4-snooping
option 82), this default configuration is used:
dhcpv4-snooping option 82 remote-id mac untrusted-policy drop

When remote-id is omitted, its default (mac) is used. When untrusted-policy is omitted, its default (drop) is
used.

The no form of this command disables DHCPv4 snooping option 82.

Command context

config

Parameters

remote-id

Specifies what address to use as the remote ID for the replace option of untrusted-policy. Specify one
of these address types:
mac

The default. Uses the switch MAC address as the remote ID.

subnet-ip

Uses the IP address of the client VLAN as the remote ID.

mgmt-ip

Uses the management interface IP address as the remote ID.

untrusted-policy

Specifies what action to take for DHCP packets (with option 82) that are received on untrusted ports.
Specify one of these actions:
drop

The default. Drop DHCP packets (with option 82) without forwarding them.

keep

Forward DHCP packets (with option 82).

replace

Replace the option 82 information in the DHCP packets with whatever is set for remote-id (one of:
mac, subnet-ip, or mgmt-ip) and forward the packets.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring DHCPv4 snooping option 82 with the keep action:

DHCP snooping | 113

|     | switch(config)# | dhcpv4-snooping | option | 82 untrusted-policy | keep |     |
| --- | --------------- | --------------- | ------ | ------------------- | ---- | --- |
ConfiguringDHCPv4snoopingoption82withmgmt-ipastheremote-idandthereplaceaction:
switch(config)# dhcpv4-snooping option 82 remote-id mgmt-ip untrusted-policy replace
DisablingDHCPv4snoopingoption82:
|     | switch(config)# | no dhcpv4-snooping |     | option 82 |     |     |
| --- | --------------- | ------------------ | --- | --------- | --- | --- |
|     | dhcpv4-snooping | trust              |     |           |     |     |
Syntax
|     | dhcpv4-snooping    | trust |     |     |     |     |
| --- | ------------------ | ----- | --- | --- | --- | --- |
|     | no dhcpv4-snooping | trust |     |     |     |     |
Description
EnablesDHCPv4snoopingtrustontheselectedport.Onlyserverpacketsreceivedontrustedportsare
forwarded.Alltheportsareuntrustedbydefault.
ThenoformofthecommanddisablesDHCPv4snoopingtrustontheselectedport.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingDHCPv4snoopingtrustoninterface2/2/1:
|     | switch(config)#    | interface       | 2/2/1 |       |     |     |
| --- | ------------------ | --------------- | ----- | ----- | --- | --- |
|     | switch(config-if)# | dhcpv4-snooping |       | trust |     |     |
|     | switch(config-if)# | exit            |       |       |     |     |
switch(config)#
DisablingDHCPv4snoopingtrustoninterface2/2/1:
|     | switch(config)#    | interface          | 2/2/1 |       |     |     |
| --- | ------------------ | ------------------ | ----- | ----- | --- | --- |
|     | switch(config-if)# | no dhcpv4-snooping |       | trust |     |     |
|     | switch(config-if)# | exit               |       |       |     |     |
switch(config)#
|     | dhcpv4-snooping | verify | mac |     |     |     |
| --- | --------------- | ------ | --- | --- | --- | --- |
Syntax
|                                         | dhcpv4-snooping    | verify mac |               |     |     |     |
| --------------------------------------- | ------------------ | ---------- | ------------- | --- | --- | --- |
|                                         | no dhcpv4-snooping | verify     | mac           |     |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |            | SwitchSeries) |     |     | 114 |

Description

This command enables verification of the hardware address field in DHCP client packets. When enabled, the
DHCP client hardware address field and the source MAC address must be the same for packets received on
untrusted ports or else the packet is dropped. This DHCP snooping MAC verification is enabled by default.

The no form of the command disables DHCPv4 snooping MAC verification.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv4 snooping MAC verification:

switch(config)# dhcpv4-snooping verify mac

Disabling DHCPv4 snooping MAC verification:

switch(config)# no dhcpv4-snooping verify mac

show dhcpv4-snooping

Syntax

show dhcpv4-snooping [vsx-peer]

Description

Shows the DHCPv4 snooping configuration.

Command context

Operator (>) or Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Showing the DHCPv4 snooping configuration:

DHCP snooping | 115

|     | switch(config)# | show                  | dhcpv4-snooping |                    |             |             |     |
| --- | --------------- | --------------------- | --------------- | ------------------ | ----------- | ----------- | --- |
|     | DHCPv4-Snooping | Information           |                 |                    |             |             |     |
|     | DHCPv4-Snooping |                       | : Yes           | Verify             | MAC Address | : Yes       |     |
|     | Allow Overwrite | Binding               | : No            | Enabled            | VLANs       | : 1751-2000 |     |
|     | Option 82       | Configurations        |                 |                    |             |             |     |
|     | Untrusted       | Policy                | : drop          | Insertion          |             | : Yes       |     |
|     | Option          | 82 Remote-id          | : mac           |                    |             |             |     |
|     | External        | Storage Information   |                 |                    |             |             |     |
|     | Volume          | Name                  | :               |                    |             |             |     |
|     | File Name       |                       | :               |                    |             |             |     |
|     | Inactive        | Since                 | : -             |                    |             |             |     |
|     | Error           |                       | : -             |                    |             |             |     |
|     | Authorized      | Server Configurations |                 |                    |             |             |     |
|     | VRF             |                       |                 | Authorized         | Servers     |             |     |
|     | ------------    |                       |                 | ------------------ |             |             |     |
Port Information
|      |                 | Max            | Static   | Dynamic  |     |     |     |
| ---- | --------------- | -------------- | -------- | -------- | --- | --- | --- |
|      | Port            | Trust Bindings | Bindings | Bindings |     |     |     |
|      | --------        | ----- -------- | -------- | -------- |     |     |     |
|      | 1/1/24          | No 512         | 1        | 100      |     |     |     |
|      | lag13           | Yes 0          | 0        | 0        |     |     |     |
| show | dhcpv4-snooping |                | binding  |          |     |     |     |
Syntax
| show | dhcpv4-snooping | binding | [vsx-peer] |     |     |     |     |
| ---- | --------------- | ------- | ---------- | --- | --- | --- | --- |
Description
ShowstheDHCPv4snoopingbindingconfiguration.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingtheDHCPv4snoopingbindingconfiguration:
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     |     | 116 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- |

switch(config)# show dhcpv4-snooping binding

MacAddress
VLAN Interface Time-Left
----------------- --------------- ---- --------- ---------
aa:b1:c1:dd:ee:ff 10.2.3.4
aa:b2:c2:dd:ee:ff 10.2.3.5

1/1/2
1/1/2

582
584

1
1

IP

show dhcpv4-snooping statistics

Syntax

show dhcpv4-snooping statistics [vsx-peer]

Description

Shows the DHCPv4 snooping statistics.

Command context

Operator (>) or Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing the DHCPv4 snooping statistics:

switch(config)# show dhcpv4-snooping statistics

Count

Reason

Packet-Type Action
----------- ------- ----------------------------- ---------
server
client
server
server
client
client
client
client
client

forward from trusted port
forward to trusted port
drop
drop
drop
drop
drop
drop
drop

received on untrusted port
unauthorized server
destination on untrusted port 78
85
untrusted option 82 field
0
bad DHCP release request
5
failed verify MAC check
15
failed on max-binding limit

5425
3895
117
214

DHCPv6 snooping commands

clear dhcpv6-snooping binding

Syntax

DHCP snooping | 117

clear dhcpv6-snooping binding {all | ip <IPV6-ADDR> vlan <VLAN-ID> |
|     | interface | <IFNAME> | | vlan <VLAN-ID>} |     |     |     |     |
| --- | --------- | -------- | ----------------- | --- | --- | --- | --- |
Description
ClearsDHCPv6snoopingbindingentries.
Commandcontext
Operator(>)orManager(#)
Parameters
all
SpecifiesthatallDHCPv6bindinginformationistobecleared.
|     | ip <IPV6-ADDR> | vlan <VLAN-ID> |     |     |     |     |     |
| --- | -------------- | -------------- | --- | --- | --- | --- | --- |
SpecifiestheIPv6addressandVLANforwhichallDHCPv6bindinginformationistobecleared.
|     | interface <IFNAME> |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- |
SpecifiestheinterfaceforwhichallDHCPv6bindinginformationistobecleared.
|     | vlan <VLAN-ID> |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- |
SpecifiestheVLANforwhichallDHCPv6bindinginformationistobecleared.Range:1to4094.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ClearingallDHCPv6bindinginformationfor5000::1vlan1:
|     | switch(config)# | clear | dhcpv6-snooping | binding | ip 5000::1 vlan | 1   |     |
| --- | --------------- | ----- | --------------- | ------- | --------------- | --- | --- |
ClearingallDHCPv6bindinginformationforinterface1/1/10:
|     | switch(config)# | clear | dhcpv6-snooping | binding | interface 1/1/10 |     |     |
| --- | --------------- | ----- | --------------- | ------- | ---------------- | --- | --- |
ClearingallDHCPv6bindinginformationforVLAN10:
|     | switch(config)# | clear | dhcpv6-snooping | binding | vlan 10 |     |     |
| --- | --------------- | ----- | --------------- | ------- | ------- | --- | --- |
ClearingallDHCPv6bindinginformation:
|     | switch(config)#       | clear | dhcpv6-snooping | binding | all |     |     |
| --- | --------------------- | ----- | --------------- | ------- | --- | --- | --- |
|     | clear dhcpv6-snooping |       | statistics      |         |     |     |     |
Syntax
|     | clear dhcpv6-snooping |     | statistics |     |     |     |     |
| --- | --------------------- | --- | ---------- | --- | --- | --- | --- |
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     |     | 118 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- |

Clears all DHCPv6 snooping statistics.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Clear all DHCPv6 snooping statistics:

switch# clear dhcpv6-snooping statistics

dhcpv6-snooping

Syntax

dhcpv6-snooping
no dhcpv6-snooping

Description

Enables DHCPv6 snooping. DHCPv6 snooping is disabled by default. DHCPv6 snooping is not supported on
the management interface.

The no form of the command disables DHCPv6 snooping, flushing all the IP bindings learned since DHCPv6
snooping was enabled.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv6 snooping:

switch(config)# dhcpv6-snooping

Disabling DHCPv6 snooping:

switch(config)# no dhcpv6-snooping

dhcpv6-snooping (in config-vlan context)

Syntax

dhcpv6-snooping
no dhcpv6-snooping

Description

DHCP snooping | 119

Enables DHCPv6 snooping in the config-vlan context. DHCPv6 snooping is disabled by default for all
VLANs.

The no form of the command disables DHCPv6 snooping on the specified VLAN, flushing all the IPv6
bindings learned for this VLAN since DHCPv6 snooping was enabled for this VLAN.

Command context

config-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling DHCPv6 snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# dhcpv6-snooping
switch(config-vlan-100)# exit
switch(config)#

Disabling DHCPv6 snooping on VLAN 100:

switch(config)# vlan 100
switch(config-vlan-100)# no dhcpv6-snooping
switch(config-vlan-100)# exit
switch(config)#

dhcpv6-snooping authorized-server

Syntax

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

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

120

Command context

config

Parameters

<IPV6-ADDR>

Specifies the IPv6 address of the trusted DHCPv6 server.

vrf <VRF-NAME>

Specifies the VRF name. The name can be default or a configured VRF instance but it cannot be mgmt.

Authority

Administrators or local user group members with execution rights for this command.

Usage

For authorized server lookup, the VRF is derived from the Switch Virtual Interface (SVI) configured for the
incoming VLAN. If the SVI is not configured, the default VRF is assumed.

Examples

Adding DHCP servers ABCD:5ACD::2000, and ABCD:5ACD::2010 to the authorized server list:

switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2010 vrf default

Removing DHCP server ABCD:5ACD::2000 from the authorized server list:

switch(config)# no dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default

dhcpv6-snooping external-storage

Syntax

dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
no dhcpv6-snooping external-storage

Description

Configures external storage to be used for backing up IPv6 bindings (used by DHCPv6 snooping) to a file.
When configured, the switch stores all the IP bindings in an external storage file so that they are retained
after the switch restarts. When the switch restarts, it reads the IPv6 bindings from the configured external
storage file to populate its local cache.

The no form of this command disables the saving of IPv6 bindings in an external storage file.

Command context

config

Parameters

volume <VOL-NAME>

Specifies the name of the existing external storage volume where the IPv6 bindings file will be saved.
Before running the dhcpv6-snooping external-storage volume command, first create the external
storage volume using command external-storage <VOLUME-NAME>. See External storage commands in
the Command-Line Interface Guide.

file <FILE-NAME>

DHCP snooping | 121

SpecifiesthefilenametouseforstoringIPv6bindings.Maximum255characters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringIPv6bindingsstorageinfileipv6Bindingsonexistingvolumedhcp_snoop:
switch(config)# dhcpv6-snooping external-storage volume dhcp_snoop file ipv6Bindings
Disablingexternalstorage:
|     | switch(config)# | no dhcpv6-snooping |     | external-storage |     |     |
| --- | --------------- | ------------------ | --- | ---------------- | --- | --- |
|     | dhcpv6-snooping | max-bindings       |     |                  |     |     |
Syntax
|     | dhcpv6-snooping    | max-bindings | <MAX-BINDINGS> |     |     |     |
| --- | ------------------ | ------------ | -------------- | --- | --- | --- |
|     | no dhcpv6-snooping | max-bindings |                |     |     |     |
Description
SetsthemaximumnumberofDHCPv6bindingsallowedontheselectedinterface.Forallinterfaceson
whichthiscommandisnotrun,thedefaultmaxbindingsapplies.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
Commandcontext
config-if
Parameters
<MAX-BINDINGS>
SpecifiesthemaximumnumberofDHCPv6bindings.Youcanusetheshow capacitiescommandtosee
themaximumavailableforyourswitchmodel.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
SettheDHCPv6maxbindingsto512oninterface2/2/1:
|     | switch(config)#    | interface       | 2/2/1 |              |     |     |
| --- | ------------------ | --------------- | ----- | ------------ | --- | --- |
|     | switch(config-if)# | dhcpv6-snooping |       | max-bindings | 512 |     |
|     | switch(config-if)# | exit            |       |              |     |     |
switch(config)#
RevertDHCPv6maxbindingstoitsdefaultoninterface2/2/1:
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 122 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

| switch(config)# | interface | 2/2/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|                    | no dhcpv6-snooping |     | max-bindings |
| ------------------ | ------------------ | --- | ------------ |
| switch(config-if)# | exit               |     |              |
switch(config)#
| dhcpv6-snooping | trust |     |     |
| --------------- | ----- | --- | --- |
Syntax
| dhcpv6-snooping    | trust |     |     |
| ------------------ | ----- | --- | --- |
| no dhcpv6-snooping | trust |     |     |
Description
EnablesDHCPv6snoopingtrustontheselectedinterface.Onlyserverpacketsreceivedontrusted
interfacesareforwarded.Alltheinterfacesareuntrustedbydefault.
ThenoformofthecommanddisablesDHCPv6snoopingtrustontheselectedinterface.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    | interface       | 2/2/1 |       |
| ------------------ | --------------- | ----- | ----- |
| switch(config-if)# | dhcpv6-snooping |       | trust |
| switch(config-if)# | exit            |       |       |
switch(config)#
DisablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    | interface          | 2/2/1 |       |
| ------------------ | ------------------ | ----- | ----- |
| switch(config-if)# | no dhcpv6-snooping |       | trust |
| switch(config-if)# | exit               |       |       |
switch(config)#
show dhcpv6-snooping
Syntax
| show dhcpv6-snooping | [vsx-peer] |     |     |
| -------------------- | ---------- | --- | --- |
Description
ShowstheDHCPv6snoopingconfiguration.
Commandcontext
Operator(>)orManager(#)
DHCPsnooping|123

Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingtheDHCPv6snoopingconfiguration:
|     | switch(config)# | show                | dhcpv6-snooping |                                         |                 |     |
| --- | --------------- | ------------------- | --------------- | --------------------------------------- | --------------- | --- |
|     | DHCPv6-Snooping | Information         |                 |                                         |                 |     |
|     | DHCPv6-Snooping |                     | : Yes           | Enabled VLANs                           | : 1,5,7,100-110 |     |
|     | External        | Storage Information |                 |                                         |                 |     |
|     | Volume          | Name                | : dhcp_snoop    |                                         |                 |     |
|     | File Name       |                     | : ip_binding    |                                         |                 |     |
|     | Inactive        | Since               | : 01:23:20      | 01/01/2019                              |                 |     |
|     | Error           |                     | : Failed        | to write external                       | storage         |     |
|     | Authorized      | Server              | Configurations  |                                         |                 |     |
|     | VRF             |                     |                 | Authorized                              | Servers         |     |
|     | ------------    |                     |                 | ------------------                      |                 |     |
|     | default         |                     |                 | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |                 |     |
|     | default         |                     |                 | 2002::2                                 |                 |     |
|     | default         |                     |                 | 2004::1                                 |                 |     |
|     | red             |                     |                 | 2002::1                                 |                 |     |
|     | red             |                     |                 | 2002::2                                 |                 |     |
|     | red             |                     |                 | 2002::9                                 |                 |     |
|     | green           |                     |                 | 5000::1                                 |                 |     |
|     | green           |                     |                 | 5000::2                                 |                 |     |
|     | green           |                     |                 | 5000::3                                 |                 |     |
|     | green           |                     |                 | 5000::7                                 |                 |     |
|     | green           |                     |                 | 5000::8                                 |                 |     |
Port Information
|      |                 |       | Max Static        | Dynamic  |     |     |
| ---- | --------------- | ----- | ----------------- | -------- | --- | --- |
|      | Port            | Trust | Bindings Bindings | Bindings |     |     |
|      | --------        | ----- | -------- -------- | -------- |     |     |
|      | 1/1/2           | Yes   | 0 0               | 0        |     |     |
|      | 1/1/3           | Yes   | 0 3               | 0        |     |     |
|      | 1/1/5           | Yes   | 0 22              | 0        |     |     |
|      | 1/1/16          | No    | 100 0             | 20       |     |     |
|      | 10/10/10        | No    | 512 12            | 7        |     |     |
|      | lag120          | No    | 256 3             | 0        |     |     |
| show | dhcpv6-snooping |       | binding           |          |     |     |
Syntax
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 124 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

| show dhcpv6-snooping | binding | [vsx-peer] |     |     |
| -------------------- | ------- | ---------- | --- | --- |
Description
ShowstheDHCPv6snoopingbindingconfiguration.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingtheDHCPv6snoopingbindingconfiguration:
| switch# show | dhcpv6-snooping | binding |     |     |
| ------------ | --------------- | ------- | --- | --- |
| IP Binding   | Information     |         |     |     |
======================
| MAC-ADDRESS | IPV6-ADDRESS |     | VLAN INTERFACE | TIME- |
| ----------- | ------------ | --- | -------------- | ----- |
LEFT
---------------- ---------------------------------------- ---- --------- ------
----
00:50:56:96:e4:cf aaaa:bbbb:cccc:dddd:eeee:1234:5678:abcd 1 1/1/1
584
| 00:50:56:96:04:4d | 1000::3 |     | 134 1/1/2 |     |
| ----------------- | ------- | --- | --------- | --- |
435
| 00:50:56:96:d8:3d | 2000:1000::4 |     | 2002 lag123 |     |
| ----------------- | ------------ | --- | ----------- | --- |
21234
| show dhcpv6-snooping |     | statistics |     |     |
| -------------------- | --- | ---------- | --- | --- |
Syntax
| show dhcpv6-snooping | statistics | [vsx-peer] |     |     |
| -------------------- | ---------- | ---------- | --- | --- |
Description
ShowstheDHCPv6snoopingstatistics.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
DHCPsnooping|125

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingtheDHCPv6snoopingstatistics:
|                                         | switch(config)# | show dhcpv6-snooping |                               |                | statistics |       |           |     |
| --------------------------------------- | --------------- | -------------------- | ----------------------------- | -------------- | ---------- | ----- | --------- | --- |
|                                         | Packet-Type     | Action               | Reason                        |                |            |       | Count     |     |
|                                         | -----------     | -------              | ----------------------------- |                |            |       | --------- |     |
|                                         | server          | forward              | from trusted                  | port           |            |       | 12        |     |
|                                         | client          | forward              | to trusted                    | port           |            |       | 20        |     |
|                                         | server          | drop                 | received                      | on untrusted   |            | port  | 5         |     |
|                                         | server          | drop                 | unauthorized                  | server         |            |       | 4         |     |
|                                         | client          | drop                 | destination                   | on             | untrusted  | port  | 2         |     |
|                                         | client          | drop                 | bad DHCP                      | release        | request    |       | 5         |     |
|                                         | server          | drop                 | relay                         | reply on       | untrusted  | port  | 2         |     |
|                                         | client          | drop                 | failed                        | on max-binding |            | limit | 5         |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                 |                      | SwitchSeries)                 |                |            |       |           | 126 |

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

Syntax

clear nd-snooping binding {all | ipv6 <IPV6-ADDR> vlan <VLAN-ID> |

port <PORT-NUM> | vlan <VLAN-ID>}

Description

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

127

ClearsNDsnoopingbindingentries.
Commandcontext
Operator(>)orManager(#)
Parameters
all
SpecifiesthatallNDbindinginformationistobecleared.
| ip <IPV6-ADDR> vlan | <VLAN-ID> |     |     |     |
| ------------------- | --------- | --- | --- | --- |
SpecifiestheIPv6addressandVLANforwhichallNDbindinginformationistobecleared.
port <PORT-NUM>
SpecifiestheportforwhichallNDbindinginformationistobecleared.
vlan <VLAN-ID>
SpecifiestheVLANforwhichallNDbindinginformationistobecleared.Range:1to4094.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
| switch(config)#   | clear nd-snooping | binding all |     |     |
| ----------------- | ----------------- | ----------- | --- | --- |
| clear nd-snooping | statistics        |             |     |     |
Syntax
| clear nd-snooping | statistics |     |     |     |
| ----------------- | ---------- | --- | --- | --- |
NDsnooping|128

Description
ClearsallNDsnoopingstatistics.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ClearallNDsnoopingstatistics:
|     | switch# clear | nd-snooping | statistics |     |
| --- | ------------- | ----------- | ---------- | --- |
nd-snooping
Syntax
|     | nd-snooping {enable|disable} |                  |     |     |
| --- | ---------------------------- | ---------------- | --- | --- |
|     | no nd-snooping               | {enable|disable} |     |     |
Description
EnablesordisablesNDsnooping.NDsnoopingisdisabledbydefault.NDsnoopingisnotsupportedonthe
managementinterface.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingNDsnooping:
|     | switch(config)# | nd-snooping | enable |     |
| --- | --------------- | ----------- | ------ | --- |
DisablingNDsnooping:
|     | switch(config)# | nd-snooping     | disable  |     |
| --- | --------------- | --------------- | -------- | --- |
|     | nd-snooping     | (in config-vlan | context) |     |
Syntax
nd-snooping
|     | no nd-snooping |     |     |     |
| --- | -------------- | --- | --- | --- |
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 129 |
| --------------------------------------- | --- | --- | ------------- | --- |

EnablesNDsnoopingintheconfig-vlancontext.NDsnoopingisdisabledbydefaultforallVLANs.
ThenoformofthecommanddisablesNDsnoopingonthespecifiedVLAN,flushingalltheIPv6bindings
learnedforthisVLANsinceNDsnoopingwasenabledforthisVLAN.
Commandcontext
config-vlan
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingNDsnoopingonVLAN100:
| switch(config)#          | vlan 100 |             |
| ------------------------ | -------- | ----------- |
| switch(config-vlan-100)# |          | nd-snooping |
| switch(config-vlan-100)# |          | exit        |
switch(config)#
DisablingNDsnoopingonVLAN100:
| switch(config)#          | vlan 100 |                |
| ------------------------ | -------- | -------------- |
| switch(config-vlan-100)# |          | no nd-snooping |
| switch(config-vlan-100)# |          | exit           |
switch(config)#
| nd-snooping | mac-check |     |
| ----------- | --------- | --- |
Syntax
nd-snooping mac-check
| no nd-snooping mac-check |     |     |
| ------------------------ | --- | --- |
Description
ThiscommandenablesverificationofthehardwareaddressfieldinNDsnoopingpackets.Whenenabled,
theICMPv6targetlinklayeraddressfieldandthesourceMACaddressmustbethesameforpackets
receivedonuntrustedportsorelsethepacketsaredropped.ThisNDsnoopingMACverificationisenabled
bydefault.
ThenoformofthecommanddisablesNDsnoopingMACverification.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingNDsnoopingMACverification:
| switch(config)# | nd-snooping | mac-check |
| --------------- | ----------- | --------- |
NDsnooping|130

DisablingNDsnoopingMACverification:
|     | switch(config)# |     | no          | nd-snooping | mac-check |     |     |     |
| --- | --------------- | --- | ----------- | ----------- | --------- | --- | --- | --- |
|     | nd-snooping     |     | prefix-list |             |           |     |     |     |
Syntax
|     | nd-snooping    | prefix-list |     | <IPV6-ADDR> |     |     |     |     |
| --- | -------------- | ----------- | --- | ----------- | --- | --- | --- | --- |
|     | no nd-snooping | prefix-list |     | <IPV6-ADDR> |     |     |     |     |
Description
ConfigurestheNDsnoopingprefixlistfortheselectedVLANandthespecifiedIPv6addressprefix.ND
snoopingmustbeenabledbothgloballyandonthisVLANbeforethisprefixlistconfigurationtakeseffect.
ThenoformofthiscommandremovestheprefixlistconfigurationfortheselectedVLANandIPv6address.
Commandcontext
config-vlan
Parameters
<IPV6-ADDR>
SpecifiestheIPv6address.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ConfiguringNDsnoopingprefix-listonVLAN1:
|     | switch(config)#        |     | vlan | 1           |     |             |            |     |
| --- | ---------------------- | --- | ---- | ----------- | --- | ----------- | ---------- | --- |
|     | switch(config-vlan-1)# |     |      | nd-snooping |     | prefix-list | 2001::1/64 |     |
|     | switch(config-vlan-1)# |     |      | exit        |     |             |            |     |
switch(config)#
RemoveconfigurationofNDsnoopingprefix-listonVLAN100:
|     | switch(config)#        |     | vlan | 1              |     |             |            |     |
| --- | ---------------------- | --- | ---- | -------------- | --- | ----------- | ---------- | --- |
|     | switch(config-vlan-1)# |     |      | no nd-snooping |     | prefix-list | 2001::1/64 |     |
|     | switch(config-vlan-1)# |     |      | exit           |     |             |            |     |
switch(config)#
|     | nd-snooping |     | max-bindings |     |     |     |     |     |
| --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
Syntax
|     | nd-snooping    | max-bindings |     | <MAX-BINDINGS> |     |     |     |     |
| --- | -------------- | ------------ | --- | -------------- | --- | --- | --- | --- |
|     | no nd-snooping | max-bindings |     |                |     |     |     |     |
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) |     |     |     | 131 |
| --------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- |

SetsthemaximumnumberofNDbindingsallowedontheselectedinterface.Forallinterfacesonwhichthis
commandisnotrun,thedefaultmaxbindingsapplies.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
Commandcontext
config-if
Parameters
<MAX-BINDINGS>
SpecifiesthemaximumnumberofNDbindings.Youcanusetheshow capacitiescommandtoseethe
maximumavailableforyourswitchmodel.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
SettheNDmaxbindingsto768oninterface2/2/1:
| switch(config)#    | interface   | 2/2/1        |     |
| ------------------ | ----------- | ------------ | --- |
| switch(config-if)# | nd-snooping | max-bindings | 768 |
| switch(config-if)# | exit        |              |     |
switch(config)#
RevertNDmaxbindingstoitsdefaultoninterface2/2/1:
switch(config)#
|                    | interface      | 2/2/1        |     |
| ------------------ | -------------- | ------------ | --- |
| switch(config-if)# | no nd-snooping | max-bindings |     |
| switch(config-if)# | exit           |              |     |
switch(config)#
| nd-snooping | nd-guard |     |     |
| ----------- | -------- | --- | --- |
Syntax
nd-snooping nd-guard
| no nd-snooping nd-guard |     |     |     |
| ----------------------- | --- | --- | --- |
Description
ThiscommandenablesNDguardontheselectedVLAN.
ThenoformofthecommanddisablesNDguardanddeletesalltheIPv6bindingslearnedontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcanbe
used.
Commandcontext
config-vlan
Authority
NDsnooping|132

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingNDsnoopingNDguardonVLAN100:
|     | switch(config)#          | nd-snooping | enable      |          |     |
| --- | ------------------------ | ----------- | ----------- | -------- | --- |
|     | switch(config)#          | vlan 100    |             |          |     |
|     | switch(config-vlan-100)# |             | nd-snooping | nd-guard |     |
|     | switch(config-vlan-100)# |             | exit        |          |     |
switch(config)#
DisablingNDsnoopingNDguardonVLAN100:
|     | switch(config)#          | vlan 100 |                |          |     |
| --- | ------------------------ | -------- | -------------- | -------- | --- |
|     | switch(config-vlan-100)# |          | no nd-snooping | nd-guard |     |
|     | switch(config-vlan-100)# |          | exit           |          |     |
switch(config)#
|     | nd-snooping | ra-guard |     |     |     |
| --- | ----------- | -------- | --- | --- | --- |
Syntax
|     | nd-snooping ra-guard    | [log] |     |     |     |
| --- | ----------------------- | ----- | --- | --- | --- |
|     | no nd-snooping ra-guard |       |     |     |     |
Description
ThiscommandenablesRoutingAdvertisement(RA)guardontheselectedVLAN.Whenenabled,ingress
RoutingAdvertisement(RA)andRoutingRedirect(RR)packetsontheselectedVLANareblockedon
untrustedports.Thepacketsareforwardedwhenreceivedontrustedports.
ThenoformofthecommanddisablesRAguardontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcanbe
used.
Commandcontext
config-vlan
Parameters
[log]
Logsmessagesalongwithdropfunctionality.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingNDsnoopingRAguardonVLAN100:
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 133 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

| switch(config)# | nd-snooping | enable |     |
| --------------- | ----------- | ------ | --- |
switch(config)#
vlan 100
| switch(config-vlan-100)# |     | nd-snooping | ra-guard |
| ------------------------ | --- | ----------- | -------- |
| switch(config-vlan-100)# |     | exit        |          |
switch(config)#
EnablingNDsnoopingRAguardonVLAN100witheventloggingondroppedpackets:
| switch(config)#          | nd-snooping | enable      |              |
| ------------------------ | ----------- | ----------- | ------------ |
| switch(config)#          | vlan 100    |             |              |
| switch(config-vlan-100)# |             | nd-snooping | ra-guard log |
| switch(config-vlan-100)# |             | exit        |              |
switch(config)#
DisablingNDsnoopingRAguardonVLAN100:
| switch(config)#          | vlan 100 |                |          |
| ------------------------ | -------- | -------------- | -------- |
| switch(config-vlan-100)# |          | no nd-snooping | ra-guard |
| switch(config-vlan-100)# |          | exit           |          |
switch(config)#
| nd-snooping | ra-drop |     |     |
| ----------- | ------- | --- | --- |
Syntax
nd-snooping ra-drop
| no nd-snooping ra-drop |     |     |     |
| ---------------------- | --- | --- | --- |
Description
ThiscommandenablesRoutingAdvertisement(RA)dropontheselectedVLAN.Whenenabled,ingressRA
packetsontheselectedVLANareblockedonbothtrustedanduntrustedports.Whendisabled,RApackets
areforwardedontheselectedVLANwithNDsnoopingtrustedportvalidation.RAdropisdisabledby
default.
NDsnoopingmustbeenabledinboththeconfigcontextandtheconfig-vlancontextbeforethiscommandcanbe
used.
ThenoformofthecommanddisablesNDsnoopingRAdropontheselectedVLAN.
Commandcontext
config-vlan
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingNDsnoopingRAdroponVLAN100:
| switch(config)#          | nd-snooping | enable vlan | 100     |
| ------------------------ | ----------- | ----------- | ------- |
| switch(config-vlan-100)# |             | nd-snooping | ra-drop |
NDsnooping|134

|     | switch(config-vlan-100)# |     | exit |     |     |
| --- | ------------------------ | --- | ---- | --- | --- |
switch(config)#
DisablingNDsnoopingRAdroponVLAN100:
|     | switch(config)#          | vlan 100 |                |         |     |
| --- | ------------------------ | -------- | -------------- | ------- | --- |
|     | switch(config-vlan-100)# |          | no nd-snooping | ra-drop |     |
|     | switch(config-vlan-100)# |          | exit           |         |     |
switch(config)#
|     | nd-snooping | trust |     |     |     |
| --- | ----------- | ----- | --- | --- | --- |
Syntax
|     | nd-snooping trust |       |     |     |     |
| --- | ----------------- | ----- | --- | --- | --- |
|     | no nd-snooping    | trust |     |     |     |
Description
EnablesNDsnoopingtrustontheselectedinterface(port).Onlyserverpacketsreceivedontrustedports
areforwarded.Alltheportsareuntrustedbydefault.
ThenoformofthecommanddisablesNDsnoopingtrustontheselectedport.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingNDsnoopingtrustoninterface2/2/1:
|     | switch(config)#    | interface   | 2/2/1 |       |     |
| --- | ------------------ | ----------- | ----- | ----- | --- |
|     | switch(config-if)# | nd-snooping |       | trust |     |
|     | switch(config-if)# | exit        |       |       |     |
switch(config)#
DisablingNDsnoopingtrustoninterface2/2/1:
|     | switch(config)#    | interface | 2/2/1       |       |     |
| --- | ------------------ | --------- | ----------- | ----- | --- |
|     | switch(config-if)# | no        | nd-snooping | trust |     |
|     | switch(config-if)# | exit      |             |       |     |
switch(config)#
|     | show nd-snooping |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- |
Syntax
|     | show nd-snooping | [vlan <VLAN-ID>] |     | [vsx-peer] |     |
| --- | ---------------- | ---------------- | --- | ---------- | --- |
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 135 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

ShowseitherallNDsnoopingconfigurationortheconfigurationforthespecifiedVLAN.
Commandcontext
Operator(>)orManager(#)
Parameters
vlan <VLAN-ID>
SpecifiestheVLANforwhichtheNDconfigurationistobeshown.Range:1to4094.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
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
NDsnooping|136

|     | show nd-snooping |     | binding |     |     |     |
| --- | ---------------- | --- | ------- | --- | --- | --- |
Syntax
|     | show nd-snooping | binding | [vsx-peer] |     |     |     |
| --- | ---------------- | ------- | ---------- | --- | --- | --- |
Description
ShowstheNDsnoopingbindingconfiguration.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingtheNDsnoopingbindingconfiguration:
|     | switch# show | nd-snooping  | binding |             |            |     |
| --- | ------------ | ------------ | ------- | ----------- | ---------- | --- |
|     | PORT         | IPV6-ADDRESS |         | MAC-ADDRESS | VLAN TIME- |     |
LEFT STATE
------- ---------------------------------------- ------------------ ----- --------
- ---------
|     | 1/1/1 | 2001::1 |     | 00:00:0A:01:02:03 | 1 600 |     |
| --- | ----- | ------- | --- | ----------------- | ----- | --- |
Valid
|     | 1/1/2 | fe80::250:56ff:fe9a:143c |     | 00:00:0B:01:02:03 | 2 - |     |
| --- | ----- | ------------------------ | --- | ----------------- | --- | --- |
Tentative
1/1/3 2001:1111:2222:3333:4444:5555:6666:7777 00:00:0C:01:02:03 4094 -
Testing
|     | show nd-snooping |     | prefix-list |     |     |     |
| --- | ---------------- | --- | ----------- | --- | --- | --- |
Syntax
|     | show nd-snooping | prefix-list | [vsx-peer] |     |     |     |
| --- | ---------------- | ----------- | ---------- | --- | --- | --- |
Description
ShowstheNDsnoopingprefixlistinformation.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 137 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingtheNDsnoopingprefixlistinformation:
| switch# show                                      | nd-snooping | prefix-list |     |     |          |     |
| ------------------------------------------------- | ----------- | ----------- | --- | --- | -------- | --- |
| VLAN IPV6-ADDRESS-PREFIX                          |             |             |     |     | SOURCE   |     |
| ----- ------------------------------------------- |             |             |     |     | -------- |     |
| 1 2001::/64                                       |             |             |     |     | Static   |     |
| 4094 3001::/64                                    |             |             |     |     | Dynamic  |     |
| show nd-snooping                                  |             | statistics  |     |     |          |     |
Syntax
| show nd-snooping | statistics | [vsx-peer] |     |     |     |     |
| ---------------- | ---------- | ---------- | --- | --- | --- | --- |
Description
ShowstheglobalNDsnoopingstatistics.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingtheglobalNDsnoopingstatistics:
| switch(config)# | show   | nd-snooping | statistics |     |     |       |
| --------------- | ------ | ----------- | ---------- | --- | --- | ----- |
| PACKET-TYPE     | ACTION | REASON      |            |     |     | COUNT |
------------ -------- ----------------------------------------------- --------
| RA  | forward | RA packets | received | on trusted   | port | 20  |
| --- | ------- | ---------- | -------- | ------------ | ---- | --- |
| RA  | drop    | RA packets | received | on untrusted | port | 45  |
| NS  | forward | NS packets | received | on trusted   | port | 52  |
| NS  | forward | NS packets | received | on untrusted | port | 95  |
| NS  | drop    | NS packets | failed   | MAC check    |      | 14  |
NDsnooping|138

|                                         | NS  | drop    | NS packets failed   | Prefix check   |            | 12        |     |
| --------------------------------------- | --- | ------- | ------------------- | -------------- | ---------- | --------- | --- |
|                                         | NS  | drop    | NS packets failed   | on max-binding | limit      | 0         |     |
|                                         | NS  | drop    | NS packets failed   | ND snooping    | validation | checks 20 |     |
|                                         | NA  | forward | NA packets received | on trusted     | port       | 17        |     |
|                                         | NA  | forward | NA packets received | on untrusted   | port       | 30        |     |
|                                         | NA  | drop    | NA packets failed   | Prefix check   |            | 15        |     |
|                                         | NA  | drop    | NA packets failed   | on max-binding | limit      | 2         |     |
|                                         | NA  | drop    | NA packets failed   | ND snooping    | validation | checks 5  |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |         | SwitchSeries)       |                |            |           | 139 |

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

For example, the following diagram shows an IP tunnel (using GRE) that connects two IPv4 networks over an
IPv4 network.

If network 1 and network 3 are using IPv6 addressing, the tunnel connects them by encapsulating the IPv6
traffic in IPv4 packets to traverse network 2. The intermediate network devices do not know about Network
1 and Network 2 because the packets are encapsulated.

An IP tunnel can also be used to create a point-to-point link for IPv6 traffic over an IPv6 network.

IP tunnels supported features

n Up to 127 tunnels can be defined on a switch shared between different tunnel types.

Unsupported features

n GRE IPv4 over IPv6.

n QoS cannot be applied to a GRE tunnel interface.

n Key support can be added for security and identification purposes when there are multiple applications.

n VPN across public IP network.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

140

MPLSoverGRE.
n
MultipointGREforscalablenetworktoreachmultipleremotesites.
n
| Configuring | an  | IP  | tunnel |     |     |     |     |
| ----------- | --- | --- | ------ | --- | --- | --- | --- |
Prerequisites
Anenabledlayer3interfacewithanIPaddressassignedtoit,createdwiththecommandinterface.
Procedure
| 1. CreateanIPtunnelwiththecommandinterface |     |     |     |     | tunnel. |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ------- | --- | --- |
2. SettheIPaddressforthetunnel.ForaGREtunnel,enterthecommandip address.ForanIPv6in
| IPv4oranIPv6inIPv6tunnel,enterthecommandipv6 |     |     |     |     |     | address. |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- |
3. SetthesourceIPaddressforthetunnel.ForaGREoranIPv6inIPv4tunnel,enterthecommand
| source | ip.ForanIPv6inIPv6tunnel,enterthecommandsource |     |     |     |     | ipv6. |     |
| ------ | ---------------------------------------------- | --- | --- | --- | --- | ----- | --- |
4. SetthedestinationIPaddressforthetunnel.ForaGREoranIPv6inIPv4tunnel,enterthecommand
destination ip.ForanIPv6inIPv6tunnel,enterthecommanddestination ipv6.
5. Optionally,settheTTL(hopcount)forthetunnelwiththecommandttl.
| 6. Optionally,settheMTUforthetunnelwiththecommandip |     |     |     |     |     | mtu. |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- |
7. Optionally,addadescriptiontothetunnelwiththecommanddescription.
8. Bydefault,thetunnelisattachedtothedefaultVRF.AttachittoadifferentVRFwiththecommand
| vrf attach.                                |     |     |     |           |           |         |     |
| ------------------------------------------ | --- | --- | --- | --------- | --------- | ------- | --- |
| 9. Enablethetunnelwiththecommandno         |     |     |     | shutdown. |           |         |     |
| 10. Reviewtunnelsettingswiththecommandshow |     |     |     |           | interface | tunnel. |     |
Example
Thisexamplecreatesthefollowingconfiguration:
n CreatesGREtunnel33.
n SetthetunnelIPaddressto10.10.20.209/24.
n SetsthetunnelsourceIPaddressto10.10.10.1.
n SetsthetunneldestinationIPaddressto10.10.10.2.
Enablesthetunnel.
n
| switch(config)#        | interface |        | tunnel      | 33 mode         | gre ipv4   |          |         |
| ---------------------- | --------- | ------ | ----------- | --------------- | ---------- | -------- | ------- |
| switch(config-gre-if)# |           |        | ip address  | 10.10.20.209/24 |            |          |         |
| switch(config-gre-if)# |           |        | source      | ip address      | 10.10.10.1 |          |         |
| switch(config-gre-if)# |           |        | destination | ip address      | 10.10.10.2 |          |         |
| switch(config-gre-if)# |           |        | no shutdown |                 |            |          |         |
| Creating               | a GRE     | tunnel |             | for traversing  |            | a public | network |
ThisexamplecreatesaGREtunnelbetweentwoswitches,enablingtrafficfromtwonetworkstotraversea
publicnetwork.
IPTunnels |141

Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress10.1.1.1/24toit.
switch#
config
|     | switch(config)#    | interface | 1/1/1   |             |     |     |
| --- | ------------------ | --------- | ------- | ----------- | --- | --- |
|     | switch(config-if)# | routing   |         |             |     |     |
|     | switch(config-if)# | ip        | address | 10.1.1.1/24 |     |     |
switch(config-if)#
no shutdown
b. Enableinterface1/1/2andassigntheIPaddress180.1.10.2/24toit.
switch# config
|     | switch(config)#    | interface | 1/1/2    |               |     |     |
| --- | ------------------ | --------- | -------- | ------------- | --- | --- |
|     | switch(config-if)# | routing   |          |               |     |     |
|     | switch(config-if)# | ip        | address  | 180.1.10.2/24 |     |     |
|     | switch(config-if)# | no        | shutdown |               |     |     |
|     | switch(config-if)# | exit      |          |               |     |     |
c. CreateGREtunnel10andassigntheIPaddress192.168.10.1/24,sourceaddress10.1.1.1,and
destinationaddress20.1.1.1toit.
|     | switch(config)#        | interface | tunnel      |     | 10 mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | --- | ---------------- | --- |
|     | switch(config-gre-if)# |           | ip address  |     | 192.168.10.1/24  |     |
|     | switch(config-gre-if)# |           | source      | ip  | 10.1.1.1         |     |
|     | switch(config-gre-if)# |           | destination |     | ip 20.1.1.1      |     |
|     | switch(config-gre-if)# |           | no shutdown |     |                  |     |
|     | switch(config-gre-if)# |           | exit        |     |                  |     |
d. Definesroutessothattrafficfromnetwork1canreachnetwork2throughthetunnel.
|     | switch(config)# | ip route | 20.1.1.0/24   |     | 10.1.1.2 |     |
| --- | --------------- | -------- | ------------- | --- | -------- | --- |
|     | switch(config)# | ip route | 190.1.10.0/24 |     | tunnel10 |     |
2. Onswitch2:
a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit.
switch# config
|     | switch(config)#    | interface | 1/1/1    |             |     |     |
| --- | ------------------ | --------- | -------- | ----------- | --- | --- |
|     | switch(config-if)# | routing   |          |             |     |     |
|     | switch(config-if)# | ip        | address  | 20.1.1.1/24 |     |     |
|     | switch(config-if)# | no        | shutdown |             |     |     |
b. Enableinterface1/1/2andassigntheIPaddress190.1.10.2/24toit.
|                                         | switch(config)#    | interface | 1/1/2         |               |     |     |
| --------------------------------------- | ------------------ | --------- | ------------- | ------------- | --- | --- |
|                                         | switch(config-if)# | routing   |               |               |     |     |
|                                         | switch(config-if)# | ip        | address       | 190.1.10.2/24 |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |           | SwitchSeries) |               |     | 142 |

|     | switch(config-if)# | no   | shutdown |     |     |     |
| --- | ------------------ | ---- | -------- | --- | --- | --- |
|     | switch(config-if)# | exit |          |     |     |     |
c. CreateGREtunnel10andassigntheIPaddress192.168.10.2/24,sourceaddress20.1.1.1,and
destinationaddress10.1.1.1toit.
|     | switch(config)#        | interface | tunnel      |     | 10 mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | --- | ---------------- | --- |
|     | switch(config-gre-if)# |           | ip address  |     | 192.168.10.2/24  |     |
|     | switch(config-gre-if)# |           | source      | ip  | 20.1.1.1         |     |
|     | switch(config-gre-if)# |           | destination |     | ip 10.1.1.1      |     |
|     | switch(config-gre-if)# |           | no shutdown |     |                  |     |
|     | switch(config-gre-if)# |           | exit        |     |                  |     |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
|          | switch(config)# | ip route | 10.1.1.0/24   |     | 20.1.1.2  |             |
| -------- | --------------- | -------- | ------------- | --- | --------- | ----------- |
|          | switch(config)# | ip route | 180.1.10.0/24 |     | tunnel10  |             |
| Creating | two GRE         | tunnels  |               | to  | different | destination |
addresses
ThisexamplecreatestwoGREtunnelstodifferentdestinationaddresses.Trafficfromnetwork1canreach
eithernetwork2ornetwork3usingtheappropriatetunnel.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
IPTunnels |143

1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress10.1.1.1/24toit.
switch# config
|     | switch(config)#    | interface | 1/1/1    |             |     |     |
| --- | ------------------ | --------- | -------- | ----------- | --- | --- |
|     | switch(config-if)# | routing   |          |             |     |     |
|     | switch(config-if)# | ip        | address  | 10.1.1.1/24 |     |     |
|     | switch(config-if)# | no        | shutdown |             |     |     |
b. Enableinterface1/1/2andassigntheIPaddress180.1.10.2/24toit.
switch# config
|     | switch(config)#    | interface | 1/1/2    |               |     |     |
| --- | ------------------ | --------- | -------- | ------------- | --- | --- |
|     | switch(config-if)# | routing   |          |               |     |     |
|     | switch(config-if)# | ip        | address  | 180.1.10.2/24 |     |     |
|     | switch(config-if)# | no        | shutdown |               |     |     |
|     | switch(config-if)# | exit      |          |               |     |     |
c. Enableinterface1/1/3andassigntheIPaddress30.1.1.1/24toit.
switch# config
|     | switch(config)#    | interface   | 1/1/3    |     |     |     |
| --- | ------------------ | ----------- | -------- | --- | --- | --- |
|     | switch(config-if)# | routing     |          |     |     |     |
|     | switch(config-if)# | 30.1.1.1/24 |          |     |     |     |
|     | switch(config-if)# | no          | shutdown |     |     |     |
|     | switch(config-if)# | exit        |          |     |     |     |
d. CreateGREtunnel10andassigntheIPaddress192.168.10.1/24,sourceaddress10.1.1.1,and
destinationaddress20.1.1.1toit.
|     | switch(config)#        | interface | tunnel      |     | 10 mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | --- | ---------------- | --- |
|     | switch(config-gre-if)# |           | ip address  |     | 192.168.10.1/24  |     |
|     | switch(config-gre-if)# |           | source      | ip  | 10.1.1.1         |     |
|     | switch(config-gre-if)# |           | destination |     | ip 20.1.1.1      |     |
|     | switch(config-gre-if)# |           | no shutdown |     |                  |     |
|     | switch(config-gre-if)# |           | exit        |     |                  |     |
e. CreateGREtunnel20andassigntheIPaddress192.168.20.1/24,sourceaddress30.1.1.1,and
destinationaddress40.1.1.1toit.
|     | switch(config)#        | interface | tunnel     |     | 20 mode gre ipv4 |     |
| --- | ---------------------- | --------- | ---------- | --- | ---------------- | --- |
|     | switch(config-gre-if)# |           | ip address |     | 192.168.20.1/24  |     |
switch(config-gre-if)#
|     |                        |     | source      | ip  | 30.1.1.1    |     |
| --- | ---------------------- | --- | ----------- | --- | ----------- | --- |
|     | switch(config-gre-if)# |     | destination |     | ip 40.1.1.1 |     |
|     | switch(config-gre-if)# |     | no shutdown |     |             |     |
|     | switch(config-gre-if)# |     | exit        |     |             |     |
f. Definesroutessothattrafficfromnetwork1canreachnetwork2throughtunnel10.
|     | switch(config)# | ip route | 20.1.1.0/24   |     | 10.1.1.2 |     |
| --- | --------------- | -------- | ------------- | --- | -------- | --- |
|     | switch(config)# | ip route | 190.1.10.0/24 |     | tunnel10 |     |
g. Definesroutessothattrafficfromnetwork1canreachnetwork3throughthetunnel20.
|     | switch(config)# | ip route | 40.1.1.0/24   |     | 30.1.1.2 |     |
| --- | --------------- | -------- | ------------- | --- | -------- | --- |
|     | switch(config)# | ip route | 200.1.10.0/24 |     | tunnel20 |     |
2. Onswitch2:
a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit.
switch#
config
|     | switch(config)#    | interface | 1/1/1   |             |     |     |
| --- | ------------------ | --------- | ------- | ----------- | --- | --- |
|     | switch(config-if)# | routing   |         |             |     |     |
|     | switch(config-if)# | ip        | address | 20.1.1.1/24 |     |     |
switch(config-if)#
no shutdown
b. Enableinterface1/1/2andassigntheIPaddress190.1.10.2/24toit.
|                                         | switch(config)#    | interface | 1/1/2         |               |     |     |
| --------------------------------------- | ------------------ | --------- | ------------- | ------------- | --- | --- |
|                                         | switch(config-if)# | routing   |               |               |     |     |
|                                         | switch(config-if)# | ip        | address       | 190.1.10.2/24 |     |     |
|                                         | switch(config-if)# | no        | shutdown      |               |     |     |
|                                         | switch(config-if)# | exit      |               |               |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |           | SwitchSeries) |               |     | 144 |

c. CreateGREtunnel10andassigntheIPaddress192.168.10.2/24,sourceaddress20.1.1.1,and
destinationaddress10.1.1.1toit.
|     | switch(config)#        | interface |             | tunnel   | 10              | mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | -------- | --------------- | ------------- | --- |
|     | switch(config-gre-if)# |           | ip          | address  | 192.168.10.2/24 |               |     |
|     | switch(config-gre-if)# |           | source      |          | ip 20.1.1.1     |               |     |
|     | switch(config-gre-if)# |           | destination |          | ip              | 10.1.1.1      |     |
|     | switch(config-gre-if)# |           | no          | shutdown |                 |               |     |
|     | switch(config-gre-if)# |           | exit        |          |                 |               |     |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughtunnel10.
|     | switch(config)# | ip route |     | 10.1.1.0/24   |     | 20.1.1.2 |     |
| --- | --------------- | -------- | --- | ------------- | --- | -------- | --- |
|     | switch(config)# | ip route |     | 180.1.10.0/24 |     | tunnel10 |     |
3. Onswitch3:
|     | a. Enableinterface1/1/1andassigntheIPaddress40.1.1.1/24toit. |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
switch# config
|     | switch(config)#                                                | interface |          | 1/1/1 |               |     |     |
| --- | -------------------------------------------------------------- | --------- | -------- | ----- | ------------- | --- | --- |
|     | switch(config-if)#                                             | routing   |          |       |               |     |     |
|     | switch(config-if)#                                             | ip        | address  |       | 40.1.1.1/24   |     |     |
|     | switch(config-if)#                                             | no        | shutdown |       |               |     |     |
|     | b. Enableinterface1/1/2andassigntheIPaddress200.1.10.2/24toit. |           |          |       |               |     |     |
|     | switch(config)#                                                | interface |          | 1/1/2 |               |     |     |
|     | switch(config-if)#                                             | routing   |          |       |               |     |     |
|     | switch(config-if)#                                             | ip        | address  |       | 200.1.10.2/24 |     |     |
|     | switch(config-if)#                                             | no        | shutdown |       |               |     |     |
|     | switch(config-if)#                                             | exit      |          |       |               |     |     |
c. CreateGREtunnel20andassigntheIPaddress192.168.20.2/24,sourceaddress40.1.1.1,and
destinationaddress30.1.1.1toit.
|     | switch(config)#        | interface |             | tunnel   | 10              | mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | -------- | --------------- | ------------- | --- |
|     | switch(config-gre-if)# |           | ip          | address  | 192.168.20.2/24 |               |     |
|     | switch(config-gre-if)# |           | source      |          | ip 40.1.1.1     |               |     |
|     | switch(config-gre-if)# |           | destination |          | ip              | 30.1.1.1      |     |
|     | switch(config-gre-if)# |           | no          | shutdown |                 |               |     |
|     | switch(config-gre-if)# |           | exit        |          |                 |               |     |
d. Definesroutessothattrafficfromnetwork3canreachnetwork1throughtunnel20.
|          | switch(config)# | ip route |      | 30.1.1.0/24   |     | 40.1.1.2       |          |
| -------- | --------------- | -------- | ---- | ------------- | --- | -------------- | -------- |
|          | switch(config)# | ip route |      | 180.1.10.0/24 |     | tunnel20       |          |
| Creating | an IPv6         | in       | IPv4 | tunnel        |     | for traversing | a public |
network
ThisexamplecreatesanIPv6inIPv4tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
IPTunnels |145

Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress10.1.1.1/24toit.
switch#
config
|     | switch(config)#    | interface |            | 1/1/1 |             |     |     |
| --- | ------------------ | --------- | ---------- | ----- | ----------- | --- | --- |
|     | switch(config-if)# |           | routing    |       |             |     |     |
|     | switch(config-if)# |           | ip address |       | 10.1.1.1/24 |     |     |
switch(config-if)#
no shutdown
b. Enableinterface1/1/2andassigntheIPaddress2080::2/64toit.
switch# config
|     | switch(config)#    | interface |             | 1/1/2   |            |     |     |
| --- | ------------------ | --------- | ----------- | ------- | ---------- | --- | --- |
|     | switch(config-if)# |           | routing     |         |            |     |     |
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
a. Enableinterface1/1/1andassigntheIPaddress20.1.1.1/24toit.
switch# config
|     | switch(config)#    | interface |             | 1/1/1 |             |     |     |
| --- | ------------------ | --------- | ----------- | ----- | ----------- | --- | --- |
|     | switch(config-if)# |           | routing     |       |             |     |     |
|     | switch(config-if)# |           | ip address  |       | 20.1.1.1/24 |     |     |
|     | switch(config-if)# |           | no shutdown |       |             |     |     |
b. Enableinterface1/1/2andassigntheIPaddress2090::2/64toit.
|                                         | switch(config)#    | interface |               | 1/1/2   |            |     |     |
| --------------------------------------- | ------------------ | --------- | ------------- | ------- | ---------- | --- | --- |
|                                         | switch(config-if)# |           | routing       |         |            |     |     |
|                                         | switch(config-if)# |           | ipv6          | address | 2090::2/64 |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                    |           | SwitchSeries) |         |            |     | 146 |

|     | switch(config-if)# |     | no shutdown |     |     |     |     |
| --- | ------------------ | --- | ----------- | --- | --- | --- | --- |
|     | switch(config-if)# |     | exit        |     |     |     |     |
c. CreateIPv6inIPv4tunnel10andassigntheIPaddress2001:DB8::2/32,sourceaddress
10.1.1.1,anddestinationaddress20.1.1.1toit.
|     | switch(config)#       | interface |             | tunnel   | 10             | mode ip 6in4 |     |
| --- | --------------------- | --------- | ----------- | -------- | -------------- | ------------ | --- |
|     | switch(config-ip-if)# |           | ipv6        | address  | 2001:DB8::2/62 |              |     |
|     | switch(config-ip-if)# |           | source      | ip       | 20.1.1.1       |              |     |
|     | switch(config-ip-if)# |           | destination |          | ip             | 10.1.1.1     |     |
|     | switch(config-ip-if)# |           | no          | shutdown |                |              |     |
|     | switch(config-ip-if)# |           | exit        |          |                |              |     |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
|          | switch(config)# | ip  | route | 10.1.1.0/24 |     | 20.1.1.2       |          |
| -------- | --------------- | --- | ----- | ----------- | --- | -------------- | -------- |
|          | switch(config)# | ip  | route | 2080::0/64  |     | tunnel10       |          |
| Creating | an IPv6         | in  | IPv6  | tunnel      |     | for traversing | a public |
network
ThisexamplecreatesanIPv6inIPv6tunnelbetweentwoswitches,enablingtrafficfromtwonetworksto
traverseapublicnetwork.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. Onswitch1:
a. Enableinterface1/1/1andassigntheIPaddress2001:DB8:5::1/64toit.
switch# config
|     | switch(config)#                                             | interface |              | 1/1/1 |                  |     |     |
| --- | ----------------------------------------------------------- | --------- | ------------ | ----- | ---------------- | --- | --- |
|     | switch(config-if)#                                          |           | routing      |       |                  |     |     |
|     | switch(config-if)#                                          |           | ipv6 address |       | 2001:DB8:5::1/64 |     |     |
|     | switch(config-if)#                                          |           | no shutdown  |       |                  |     |     |
|     | b. Enableinterface1/1/2andassigntheIPaddress2080::2/64toit. |           |              |       |                  |     |     |
switch# config
|     | switch(config)#    | interface |              | 1/1/2 |            |     |     |
| --- | ------------------ | --------- | ------------ | ----- | ---------- | --- | --- |
|     | switch(config-if)# |           | routing      |       |            |     |     |
|     | switch(config-if)# |           | ipv6 address |       | 2080::2/64 |     |     |
|     | switch(config-if)# |           | no shutdown  |       |            |     |     |
|     | switch(config-if)# |           | exit         |       |            |     |     |
IPTunnels |147

c. CreateIPv6inIPv6tunnel10andassigntheIPaddress2001:DB8::1/32,sourceaddress
2001:DB8:5::1,anddestinationaddress2001:DB8:9::1toit.(Optional)SettheMTUandTTL
parametersforthistunnelinterface.
|     | switch(config)#       | interface | tunnel       | 10  | mode           | ip 6in6 |     |
| --- | --------------------- | --------- | ------------ | --- | -------------- | ------- | --- |
|     | switch(config-ip-if)# |           | ipv6 address |     | 2001:DB8::1/62 |         |     |
switch(config-ip-if)#
|     |                       |     | source      | ipv6 2001:DB8:5::1 |               |     |     |
| --- | --------------------- | --- | ----------- | ------------------ | ------------- | --- | --- |
|     | switch(config-ip-if)# |     | destination | ipv6               | 2001:DB8:9::1 |     |     |
|     | switch(config-ip-if)# |     | no shutdown |                    |               |     |     |
|     | switch(config-ip-if)# |     | exit        |                    |               |     |     |
d. Definesroutessothattrafficfromnetwork1canreachnetwork2throughthetunnel.
|     | switch(config)# | ipv6 | route 2001:DB8:9::0/64 |     |          | 2001:DB8:5::2 |     |
| --- | --------------- | ---- | ---------------------- | --- | -------- | ------------- | --- |
|     | switch(config)# | ipv6 | route 2090::0/64       |     | tunnel10 |               |     |
2. Onswitch2:
a. Enableinterface1/1/1andassigntheIPaddress2001:DB8:9::1/64toit.
switch# config
|     | switch(config)#    | interface | 1/1/1        |                  |     |     |     |
| --- | ------------------ | --------- | ------------ | ---------------- | --- | --- | --- |
|     | switch(config-if)# |           | routing      |                  |     |     |     |
|     | switch(config-if)# |           | ipv6 address | 2001:DB8:9::1/64 |     |     |     |
|     | switch(config-if)# |           | no shutdown  |                  |     |     |     |
b. Enableinterface1/1/2andassigntheIPaddress2090::2/64toit.
|     | switch(config)# | interface | 1/1/2 |     |     |     |     |
| --- | --------------- | --------- | ----- | --- | --- | --- | --- |
switch(config-if)#
routing
|     | switch(config-if)# |     | ipv6 address | 2090::2/64 |     |     |     |
| --- | ------------------ | --- | ------------ | ---------- | --- | --- | --- |
|     | switch(config-if)# |     | no shutdown  |            |     |     |     |
|     | switch(config-if)# |     | exit         |            |     |     |     |
c. CreateIPv6inIPv6tunnel10andassigntheIPaddress2001:DB8::2/32,sourceaddress
2001:DB8:5::1,anddestinationaddress2001:DB8:9::1toit.(Optional)SettheMTUandTTL
parametersforthistunnelinterface.
|     | switch(config)#       | interface | tunnel       | 10                 | mode           | ip 6in6 |     |
| --- | --------------------- | --------- | ------------ | ------------------ | -------------- | ------- | --- |
|     | switch(config-ip-if)# |           | ipv6 address |                    | 2001:DB8::2/62 |         |     |
|     | switch(config-ip-if)# |           | source       | ipv6 2001:DB8:9::1 |                |         |     |
switch(config-ip-if)#
|     |                       |     | destination | ipv6 | 2001:DB8:5::1 |     |     |
| --- | --------------------- | --- | ----------- | ---- | ------------- | --- | --- |
|     | switch(config-ip-if)# |     | no shutdown |      |               |     |     |
|     | switch(config-ip-if)# |     | exit        |      |               |     |     |
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughthetunnel.
|            | switch(config)# | ipv6 | route 2001:DB8:5::0/64 |     |          | 2001:DB8:9::2 |     |
| ---------- | --------------- | ---- | ---------------------- | --- | -------- | ------------- | --- |
|            | switch(config)# | ipv6 | route 2080::0/64       |     | tunnel10 |               |     |
| IP tunnels | commands        |      |                        |     |          |               |     |
description
Syntax
| description    | <DESC> |     |     |     |     |     |     |
| -------------- | ------ | --- | --- | --- | --- | --- | --- |
| no description |        |     |     |     |     |     |     |
Description
AssociatesatextdescriptionwithanIPtunnelforidentificationpurposes.
ThenoformofthiscommandremovesthedescriptionfromanIPtunnel.
Commandcontext
config-gre-if
config-ip-if
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     |     | 148 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- |

Parameters
<DESC>
SpecifiesthedescriptivetexttoassociatewiththeIPtunnel.Range:1to64printableASCIIcharacters.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefinesadescriptionforGREtunnel33.
| switch(config)#        | interface | tunnel      | 33 mode | gre ipv4   |
| ---------------------- | --------- | ----------- | ------- | ---------- |
| switch(config-gre-if)# |           | description | Network | A Tunnel C |
RemovesthedescriptionforGREtunnel33.
| switch(config)#        | interface | tunnel         | 33  |     |
| ---------------------- | --------- | -------------- | --- | --- |
| switch(config-gre-if)# |           | no description |     |     |
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
| destination           | ip        |                |     |     |
Syntax
| destination ip <IPV4-ADDR> |             |     |     |     |
| -------------------------- | ----------- | --- | --- | --- |
| no destination ip          | <IPV4-ADDR> |     |     |     |
Description
SetsthedestinationIPaddressforanIPtunnel.Specifytheaddressoftheinterfaceontheremotedeviceto
whichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPaddressfromanIPtunnel.
IPTunnels |149

Commandcontext
config-gre-if
config-ip-if
Parameters
<IPV4-ADDR>
SpecifiesthedestinationIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefinesthedestinationIPaddresstobe10.10.10.1forGREtunnel33.
|     | switch(config)#        | interface | tunnel      | 33 mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | ---------------- | --- |
|     | switch(config-gre-if)# |           | destination | ip 10.10.10.1    |     |
DeletesthedestinationIPaddress10.10.10.1fromGREtunnel33.
|     | switch(config)#        | interface | tunnel         | 33            |     |
| --- | ---------------------- | --------- | -------------- | ------------- | --- |
|     | switch(config-gre-if)# |           | no destination | ip 10.10.10.1 |     |
DefinesthedestinationIPaddresstobe10.10.20.1forIPv6inIPv4tunnel27.
|     | switch(config)#       | interface | tunnel      | 27 mode ip 6in4 |     |
| --- | --------------------- | --------- | ----------- | --------------- | --- |
|     | switch(config-ip-if)# |           | destination | ip 10.10.20.1   |     |
DeletesthedestinationIPaddress10.10.20.1fromIPv6inIPv4tunnel27.
|     | switch(config)#       | interface | tunnel         | 27            |     |
| --- | --------------------- | --------- | -------------- | ------------- | --- |
|     | switch(config-ip-if)# |           | no destination | ip 10.10.20.1 |     |
|     | destination           | ipv6      |                |               |     |
Syntax
|     | destination ipv6    | <IPVv6-ADDR> |     |     |     |
| --- | ------------------- | ------------ | --- | --- | --- |
|     | no destination ipv6 | <IPV6-ADDR>  |     |     |     |
Description
SetsthedestinationIPv6addressforanIPtunnel.Specifytheaddressoftheinterfaceontheremotedevice
towhichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPv6addressfromanIPtunnel.
Commandcontext
config-ip-if
Parameters
<IPV6-ADDR>
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 150 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

SpecifiesthetunnelIPaddressinIPv6format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexis
ahexadecimalnumberfrom0toF.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefinesthedestinationIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel
| switch(config)# |     | interface | tunnel 8 | mode ip 6in6 |
| --------------- | --- | --------- | -------- | ------------ |
switch(config-ip-if)#
|     |     |     | destination ipv6 | 2001:DB8::1 |
| --- | --- | --- | ---------------- | ----------- |
DeletesthedestinationIPv6address2001:DB8::1fromIPv6inIPv6tunnel8.
| switch(config)#       |        | interface | tunnel 8       |                  |
| --------------------- | ------ | --------- | -------------- | ---------------- |
| switch(config-ip-if)# |        |           | no destination | ipv6 2001:DB8::1 |
| interface             | tunnel |           |                |                  |
Syntax
interface tunnel <TUNNEL-NUMBER> mode {gre ipv4 | ip 6in4 | ip 6in6}
| interface    | tunnel | <EXISTING-TUNNEL-NUMBER> |     |     |
| ------------ | ------ | ------------------------ | --- | --- |
| no interface | tunnel | <EXISTING-TUNNEL-NUMBER> |     |     |
Description
CreatesorupdatesanIPtunnel.Afteryouenterthecommand,thefirmwareswitchestotheconfiguration
contextforthetunnel.
Ifthespecifiedtunnelexists,thiscommandswitchestothecontextforthetunnel.
Bydefault,alltunnelsareautomaticallyassignedtothedefaultVRFwhentheyarecreated.
ThenoformofthiscommanddeletesanexistingIPtunnel.
Commandcontext
config
Parameters
| mode {gre | ipv4 | | ip 6in4 | | ip 6in6} |     |
| --------- | ------ | ------- | ---------- | --- |
CreatesanIPtunnel.Chooseoneofthefollowingoptions:
| n gre | ipv4:CreatesaGREtunnel.                 |     |     |     |
| ----- | --------------------------------------- | --- | --- | --- |
| n ip  | 6in4:CreatesanIPv4tunnelforIPv6traffic. |     |     |     |
| n ip  | 6in6:CreatesanIPv6tunnelforIPv6traffic. |     |     |     |
<TUNNEL-NUMBER>
Specifiesthenumberforanewtunnel.Range:1to127.Numberingissharedbetweenalltunnels,sothe
sametunnelnumbercannotbeusedforanIPv6inIPv4tunnelandaGREtunnel.
<EXISTING-TUNNEL-NUMBER>
SpecifiesthenumberforanexistingIPtunnel.Range:1to127.
Commandcontext
config-gre-if
IPTunnels |151

config-ip-if
Examples
DefinesanewGREtunnelwithnumber27.
|     | switch(config)# | interface | tunnel | 33 mode gre ipv4 |     |
| --- | --------------- | --------- | ------ | ---------------- | --- |
switch(config-gre-if)#
Switchestotheconfig-gre-ifcontextforexistingtunnel33.
|     | switch(config)# | interface | tunnel | 33  |     |
| --- | --------------- | --------- | ------ | --- | --- |
switch(config-gre-if)#
DeletesGREtunnel33.
|     | switch(config)# | no interface | tunnel | 33  |     |
| --- | --------------- | ------------ | ------ | --- | --- |
DefinesanewIPv6inIPv4tunnelwithnumber27.
|     | switch(config)# | interface | tunnel | 27 mode ip 6in4 |     |
| --- | --------------- | --------- | ------ | --------------- | --- |
switch(config-ip-if)#
Switchestotheconfig-ip-ifcontextforexistingtunnel27.
|     | switch(config)# | interface | tunnel | 27  |     |
| --- | --------------- | --------- | ------ | --- | --- |
switch(config-ip-if)#
DeletesIPv6inIPv4tunnel27.
|     | switch(config)# | no interface | tunnel | 27  |     |
| --- | --------------- | ------------ | ------ | --- | --- |
DefinesanewIPv6inIPv6tunnelwithnumber8.
|     | switch(config)# | interface | tunnel | 8 mode ip 6in6 |     |
| --- | --------------- | --------- | ------ | -------------- | --- |
switch(config-ip-if)#
|     | ip address |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- |
Syntax
|     | ip address <IPV4-ADDR>/<MASK>    |     |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- |
|     | no ip address <IPV4-ADDR>/<MASK> |     |     |     |     |
Description
SetsthelocalIPaddressofaGREtunnel.Thisaddressidentifiesthetunnelinterfaceforrouting.Itmustbe
onthesamesubnetasthetunneladdressassignedontheremotedevice.
ThenoformofthiscommanddeletesthelocalIPaddressassignedtoaGREtunnel.
Commandcontext
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 152 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

config-gre-if

Parameters

<IPV4-ADDR>

Specifies the tunnel IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255. You
can remove leading zeros. For example, the address 192.169.005.100 becomes 192.168.5.100.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 32.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Defines the local IP address 10.10.10.1 for GRE tunnel 33.

switch(config)# interface tunnel 33 mode gre ipv4
switch(config-gre-if)# ip address 10.10.10.1/24

Deletes the local IP address 10.10.10.1 for GRE tunnel 33.

switch(config)# interface tunnel 33
switch(config-gre-if)# no ip address 10.10.10.1/24

ipv6 address

Syntax

ipv6 address <IPV6-ADDR>/<MASK>
no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets the local IP address of an IPv6 to IPv4 tunnel or of an IPv6 to IPv6 tunnel. This address identifies the
tunnel interface for routing. It must be on the same subnet as the tunnel address assigned on the remote
device.

The no form of this command deletes the local IP address assigned to an IPv6 to IPv4 tunnel.

Command context

config-ip-if

config-if

Parameters

<IPV6-ADDR>

Specifies the tunnel IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is
a hexadecimal number from 0 to F.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 32.

IP Tunnels | 153

Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefinesthelocalIPaddress2001:DB8:5::1/64fortunnel8foranIPv6toIPv6tunnel.
|     | switch(config)#       | interface | tunnel 8 | mode ip 6in6     |     |
| --- | --------------------- | --------- | -------- | ---------------- | --- |
|     | switch(config-ip-if)# | ipv6      | address  | 2001:DB8:5::1/64 |     |
DeletesthelocalIPaddress2001:DB8::1/32fortunnel8.
|     | switch(config)#       | interface | tunnel 8     |                  |     |
| --- | --------------------- | --------- | ------------ | ---------------- | --- |
|     | switch(config-ip-if)# | no        | ipv6 address | 2001:DB8:5::1/64 |     |
|     | ip mtu                |           |              |                  |     |
Syntax
|     | ip mtu <VALUE> |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- |
Description
SetstheMTU(maximumtransmissionunit)foranIPinterface.Thedefaultvalueis1500bytes.
ThenoformofthiscommandsetstheMTUtothedefaultvalueof1500bytes.
Commandcontext
config-gre-if
config-ip-if
Parameters
<VALUE>
SpecifiestheMTUinbytes.Range:1,280bytesto9,192bytes.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
TheIPMTUisthelargestIPpacketthatcanbesentorreceivedbytheinterface.Foratunnel,theIPMTUis
themaximumsizeoftheIPpayload.Toenablejumbopacketforwardingthroughthetunnel,settheIPMTU
ofthetunneltoavaluegreaterthan1500.AlsosettheMTUandtheIPMTUvaluesfortheunderlying
physicalinterfacethatthetunnelisusingtoavaluegreaterthan1,500bytes.TheIPMTUofthetunnel
mustalsobegreaterthanorequaltotheMTUoftheingressinterfaceontheswitch.TheIPMTUvalueof
thetunnelmustalsobelessthanorequaltotheIPMToftheunderlyinginterfacethatthetunnelisusing.
WhendefiningaGREtunnel,theMTUhastoaccountfor28bytesofIPlayeroverhead,plusaGREheader.It
mustbelargerthantheMTUoftheinterfacethatthetunnelisusing.PacketslargerthantheMTUare
dropped.
Examples
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 154 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

SetstheMTUonGREinterface33to1300bytes.
| switch(config)#        | interface | tunnel   | 33 mode gre ipv4 |
| ---------------------- | --------- | -------- | ---------------- |
| switch(config-gre-if)# |           | mtu 1300 |                  |
SetstheMTUonGREinterface33tothedefaultvalue.
| switch(config)#        | interface | tunnel | 33 mode gre ipv4 |
| ---------------------- | --------- | ------ | ---------------- |
| switch(config-gre-if)# |           | ip mtu |                  |
SetstheMTUonIPv6inIPv4tunnel27to1000bytes.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | mtu       | 1000   |                 |
SetstheMTUonIPv6inIPv4tunnel27tothedefaultvalue.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | ip        | mtu    |                 |
SetstheMTUonIPv6inIPv6tunnel8to900bytes.
switch(config)#
|                       | interface | tunnel   | 8 mode ip 6in6 |
| --------------------- | --------- | -------- | -------------- |
| switch(config-ip-if)# | ip        | mtu 9000 |                |
SetstheMTUonIPv6inIPv6tunnel8tothedefaultvalue.
| switch(config)#       | interface | tunnel | 8 mode ip 6in6 |
| --------------------- | --------- | ------ | -------------- |
| switch(config-ip-if)# | ip        | mtu    |                |
| show interface        | tunnel    |        |                |
Syntax
| show interface | tunnel[<TUNNEL-NUMBER>] |     | [vsx-peer] |
| -------------- | ----------------------- | --- | ---------- |
Description
ShowsconfigurationsettingsforallIPtunnels,oraspecifictunnel.
Commandcontext
Manager(#)
Parameters
<TUNNEL-NUMBER>
SpecifiesthenumberofanIPtunnel.Range:1to127.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
IPTunnels |155

Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showsconfigurationsettingsfortunnel10,whichisaGREtunnelinthefollowingexample.
|     | switch#    | show interface |              | tunnel10 |              |     |       |     |
| --- | ---------- | -------------- | ------------ | -------- | ------------ | --- | ----- | --- |
|     | Interface  | tunnel10       | is up        |          |              |     |       |     |
|     | Admin      | state is       | up           |          |              |     |       |     |
|     | tunnel     | type GRE       | IPv4         |          |              |     |       |     |
|     | tunnel     | interface      | IPv4         | address  | 192.0.2.0/24 |     |       |     |
|     | tunnel     | source         | IPv4 address | 1.1.1.1  |              |     |       |     |
|     | tunnel     | destination    | IPv4         | address  | 2.2.2.2      |     |       |     |
|     | tunnel     | ttl 60         |              |          |              |     |       |     |
|     | Statistics |                |              |          | RX           | TX  | Total |     |
------------- -------------------- -------------------- --------------------
|     | L3 Packets |     |     |     | 0   | 0   | 0   |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     | L3 Bytes   |     |     |     | 0   | 0   | 0   |     |
Showsconfigurationsettingsfortunnel12,whichisanIPv6inIPv6tunnelinthefollowingexample.
|     | switch#      | show interface |              | tunnel12 |         |     |       |     |
| --- | ------------ | -------------- | ------------ | -------- | ------- | --- | ----- | --- |
|     | Interface    | tunnel12       | is up        |          |         |     |       |     |
|     | Admin        | state is       | up           |          |         |     |       |     |
|     | tunnel       | type IPv6      | in IPv6      |          |         |     |       |     |
|     | tunnel       | interface      | IPv6         | address  | 4::1/64 |     |       |     |
|     | tunnel       | source         | IPv6 address | 2::1     |         |     |       |     |
|     | tunnel       | destination    | IPv6         | address  | 2::2    |     |       |     |
|     | tunnel       | ttl 60         |              |          |         |     |       |     |
|     | Description: | Network2       |              | Tunnel   |         |     |       |     |
|     | Statistics   |                |              |          | RX      | TX  | Total |     |
------------- -------------------- -------------------- --------------------
|     | L3 Packets |     |     |     | 0   | 0   | 0   |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     | L3 Bytes   |     |     |     | 0   | 0   | 0   |     |
Showsconfigurationsettingsforalltunnels.
|     | switch#    | show interface |              | tunnel  |              |     |       |     |
| --- | ---------- | -------------- | ------------ | ------- | ------------ | --- | ----- | --- |
|     | Interface  | tunnel10       | is up        |         |              |     |       |     |
|     | Admin      | state is       | up           |         |              |     |       |     |
|     | tunnel     | type GRE       | IPv4         |         |              |     |       |     |
|     | tunnel     | interface      | IPv4         | address | 192.0.2.0/24 |     |       |     |
|     | tunnel     | source         | IPv4 address | 1.1.1.1 |              |     |       |     |
|     | tunnel     | destination    | IPv4         | address | 2.2.2.2      |     |       |     |
|     | tunnel     | ttl 60         |              |         |              |     |       |     |
|     | Statistics |                |              |         | RX           | TX  | Total |     |
------------- -------------------- -------------------- --------------------
|                                         | L3 Packets |     |     |               | 0   | 0   | 0   |     |
| --------------------------------------- | ---------- | --- | --- | ------------- | --- | --- | --- | --- |
|                                         | L3 Bytes   |     |     |               | 0   | 0   | 0   |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |            |     |     | SwitchSeries) |     |     |     | 156 |

| Interface    | tunnel11    |           | is up   |              |              |     |     |     |       |     |
| ------------ | ----------- | --------- | ------- | ------------ | ------------ | --- | --- | --- | ----- | --- |
| Admin        | state       | is up     |         |              |              |     |     |     |       |     |
| tunnel       | type        | IPv6      | in IPv4 |              |              |     |     |     |       |     |
| tunnel       | source      | IPv4      | address | 198.51.100.0 |              |     |     |     |       |     |
| tunnel       | destination |           | IPv4    | address      | 198.51.200.5 |     |     |     |       |     |
| tunnel       | ttl         | 80        |         |              |              |     |     |     |       |     |
| Description: |             | Network11 |         |              |              |     |     |     |       |     |
| Statistics   |             |           |         |              | RX           |     |     | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets   |             |          |         |         |         | 0   |     | 0   |       | 0   |
| ------------ | ----------- | -------- | ------- | ------- | ------- | --- | --- | --- | ----- | --- |
| L3 Bytes     |             |          |         |         |         | 0   |     | 0   |       | 0   |
| Interface    | tunnel12    |          | is up   |         |         |     |     |     |       |     |
| Admin        | state       | is up    |         |         |         |     |     |     |       |     |
| tunnel       | type        | IPv6     | in IPv6 |         |         |     |     |     |       |     |
| tunnel       | interface   |          | IPv6    | address | 4::1/64 |     |     |     |       |     |
| tunnel       | source      | IPv6     | address | 2::1    |         |     |     |     |       |     |
| tunnel       | destination |          | IPv6    | address | 2::2    |     |     |     |       |     |
| tunnel       | ttl         | 60       |         |         |         |     |     |     |       |     |
| Description: |             | Network2 |         | Tunnel  |         |     |     |     |       |     |
| Statistics   |             |          |         |         | RX      |     |     | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets          |     |     |     |           |     | 0      |     | 0   |     | 0   |
| ------------------- | --- | --- | --- | --------- | --- | ------ | --- | --- | --- | --- |
| L3 Bytes            |     |     |     |           |     | 0      |     | 0   |     | 0   |
| show running-config |     |     |     | interface |     | tunnel |     |     |     |     |
Syntax
| show running-config |     |     | interface | tunnel<TUNNEL-NUMBER> |     |     | [vsx-peer] |     |     |     |
| ------------------- | --- | --- | --------- | --------------------- | --- | --- | ---------- | --- | --- | --- |
Description
ShowsthecommandsusedtoconfigureanIPtunnel.
Commandcontext
| Manager (#) |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Parameters
<TUNNEL-NUMBER>
SpecifiesthenumberofanIPtunnel.Range:1to127.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowstheconfigurationforaGREtunnel.
IPTunnels |157

|     | switch# show | running-config | interface | tunnel2 |     |
| --- | ------------ | -------------- | --------- | ------- | --- |
|     | interface    | tunnel 2 mode  | gre ipv4  |         |     |
|     | source       | ip 10.10.20.11 |           |         |     |
|     | destination  | ip 10.20.1.2   |           |         |     |
|     | ip address   | 10.10.10.1/24  |           |         |     |
ttl 60
ShowstheconfigurationforIPv6inIPv4tunnel.
|     | switch# show | running-config   | interface | tunnel5 |     |
| --- | ------------ | ---------------- | --------- | ------- | --- |
|     | interface    | tunnel5 mode     | ip 6in4   |         |     |
|     | source       | ip 10.10.10.12   |           |         |     |
|     | destination  | ip 22.20.20.20   |           |         |     |
|     | ip6 address  | 2001:DB8:5::1/64 |           |         |     |
ttl 60
no shutdown
|     | description | Network10 |     |     |     |
| --- | ----------- | --------- | --- | --- | --- |
ShowstheconfigurationforIPv6inIPv6tunnel.
|     | switch# show | running-config | interface | tunnel1 |     |
| --- | ------------ | -------------- | --------- | ------- | --- |
|     | interface    | tunnel 1 mode  | ip 6in6   |         |     |
|     | description  | Network2       | Tunnel    |         |     |
|     | source       | ipv6 2::1      |           |         |     |
|     | destination  | ipv6 2::2      |           |         |     |
|     | ipv6 address | 4::1/64        |           |         |     |
ttl 60
shutdown
Syntax
shutdown
|     | no shutdown |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- |
Description
ThiscommanddisablesanIPinterface.IPinterfacesaredisabledbydefaultwhencreated.
ThenoformofthiscommandenablesanIPinterface.
Commandcontext
config-gre-if
config-ip-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablesGREinterface33.
|     | switch(config)#        | interface | tunnel      | 33 mode gre ipv4 |     |
| --- | ---------------------- | --------- | ----------- | ---------------- | --- |
|     | switch(config-gre-if)# |           | no shutdown |                  |     |
DisablesGREinterface33.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 158 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

| switch(config)#        | interface | tunnel   | 33 mode gre ipv4 |
| ---------------------- | --------- | -------- | ---------------- |
| switch(config-gre-if)# |           | shutdown |                  |
EnablesIPv6inIPv4interface27.
| switch(config)#       | interface | tunnel   | 27 mode ip 6in4 |
| --------------------- | --------- | -------- | --------------- |
| switch(config-ip-if)# | no        | shutdown |                 |
DisablesIPv6inIPv4interface27.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | shutdown  |        |                 |
source ip
Syntax
source ip <IPV4-ADDR>
| no source ip <IPV4-ADDR> |     |     |     |
| ------------------------ | --- | --- | --- |
Description
SetsthesourceIPaddressforanIPtunnel.SpecifytheIPaddressofalayer3interfaceontheswitch.
TunnelscanhavethesamesourceIPaddressanddifferentdestinationIPaddresses.
ThenoformofthiscommanddeletesthesourceIPaddressforanIPtunnel.
Commandcontext
config-gre-if
config-ip-if
Parameters
<IPV4-ADDR>
SpecifiesthesourceIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefinesthesourceIPaddresstobe10.10.20.1forGREtunnel33.
| switch(config)# | interface | tunnel | 33 mode gre ipv4 |
| --------------- | --------- | ------ | ---------------- |
switch(config-gre-if)#
|     |     | source ip | 10.10.20.1 |
| --- | --- | --------- | ---------- |
DeletesthesourceIPaddress10.1.20.1fromGREtunnel33.
| switch(config)#        | interface | tunnel    | 33            |
| ---------------------- | --------- | --------- | ------------- |
| switch(config-gre-if)# |           | no source | ip 10.10.20.1 |
DefinesthesourceIPaddresstobe10.10.10.1forIPv6inIPv4tunnel27.
IPTunnels |159

|     | switch(config)# | interface | tunnel | 27 mode ip 6in4 |     |
| --- | --------------- | --------- | ------ | --------------- | --- |
switch(config-ip-if)#
|     |     | source | ip 10.10.10.1 |     |     |
| --- | --- | ------ | ------------- | --- | --- |
DeletesthesourceIPaddress10.1.10.1fromIPv6inIPv4tunnel27.
|     | switch(config)#       | interface | tunnel    | 27         |     |
| --- | --------------------- | --------- | --------- | ---------- | --- |
|     | switch(config-ip-if)# | no        | source ip | 10.10.10.1 |     |
|     | source ipv6           |           |           |            |     |
Syntax
|     | source ipv6 <IPV6-ADDR> |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- |
|     | no source ipv6          |     |     |     |     |
Description
SetsthesourceIPv6addresstobeusedfortheencapsulation.
ThenoformofthiscommanddeletesthesourceIPv6addressforanIPtunnel.
Commandcontext
config-ip-if
Parameters
<IPV6-ADDR>
SpecifiesthetunnelIPaddressinIPv6format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexis
ahexadecimalnumberfrom0toF.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefinesthesourceIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel8.
|     | switch(config)#       | interface | tunnel | 8 mode ip 6in6 |     |
| --- | --------------------- | --------- | ------ | -------------- | --- |
|     | switch(config-ip-if)# | source    | ipv6   | 2001:DB8::1    |     |
DeletesthesourceIPaddress2001:DB8::1fromIPv6inIPv6tunnel8.
|     | switch(config)#       | interface | tunnel      | 8           |     |
| --- | --------------------- | --------- | ----------- | ----------- | --- |
|     | switch(config-ip-if)# | no        | source ipv6 | 2001:DB8::1 |     |
ttl
Syntax
|     | ttl <COUNT> |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- |
|     | no ttl      |     |     |     |     |
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 160 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

SetstheTTL(time-to-live),alsoknownasthehopcount,fortunneledpackets.Ifnotconfigured,thedefault
valueof64isusedforthetunnel.(Thehopcountoftheoriginalpacketsisnotchanged.)Amaximumof
fourdifferentTTLvaluescanbeusedatthesametimebyalltunnelsontheswitch.Forexample,iftunnel-1
hasTTL10,tunnel-2hasTTL20,tunnel-3hasTTL30,andtunnel-4hasTTL40,thentunnel-5cannothavea
uniqueTTLvalue,itmustreuseoneofthevaluesassignedtotheothertunnels(10,20,30,40).
ThenoformofthiscommandsetsTTLtothedefaultvalueof64.
Commandcontext
config-gre-if
config-ip-if
Parameters
<COUNT>
Specifiesthehopcount.Range:1to255.Default:64.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
DefinesaTTLof99forGREtunnel33.
| switch(config)#        | interface | tunnel | 33 mode gre ipv4 |
| ---------------------- | --------- | ------ | ---------------- |
| switch(config-gre-if)# |           | ttl 99 |                  |
SetstheTTLforGREtunnel33tothedefaultvalueof64.
| switch(config)#        | interface | tunnel | 33  |
| ---------------------- | --------- | ------ | --- |
| switch(config-gre-if)# |           | no ttl |     |
DefinesaTTLof55forIPv6inIPv4tunnel27.
switch(config)#
|                       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | ttl       | 55     |                 |
SetstheTTLforIPv6inIPv4tunnel27tothedefaultvalueof64.
| switch(config)#       | interface | tunnel | 27  |
| --------------------- | --------- | ------ | --- |
| switch(config-ip-if)# | no        | ttl    |     |
vrf attach
Syntax
vrf attach <VRF-NAME>
| no vrf attach <VRF-NAME> |     |     |     |
| ------------------------ | --- | --- | --- |
Description
AssignsanIPtunneltoaVRF.Bydefault,alltunnelsareautomaticallyassignedtothedefaultVRFwhen
theyarecreated.
ThenoformofthiscommandassignsatunneltothedefaultVRF(default).
IPTunnels |161

Commandcontext
config-gre-if
config-ip-if
Parameters
<VRF-NAME>
SpecifiestheVRFnametowhichtoassignthetunnel.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
AssignsGREtunnel33tovrf1.
|     | switch(config)#        | interface | tunnel     | 33 mode | gre ipv4 |     |
| --- | ---------------------- | --------- | ---------- | ------- | -------- | --- |
|     | switch(config-gre-if)# |           | vrf attach | vrf1    |          |     |
ReassignsGREtunnel33tothedefaultVRF.
|     | switch(config)#        | interface | tunnel | 33     |      |     |
| --- | ---------------------- | --------- | ------ | ------ | ---- | --- |
|     | switch(config-gre-if)# |           | no vrf | attach | vrf1 |     |
AssignsIPv6inIPv4tunnel27tovrf2.
|     | switch(config)#       | interface | tunnel     | 27 mode | gre ipv4 |     |
| --- | --------------------- | --------- | ---------- | ------- | -------- | --- |
|     | switch(config-ip-if)# |           | vrf attach | vrf2    |          |     |
ReassignsIPv6inIPv4tunnel27tothedefaultVRF.
|     | switch(config)#       | interface | tunnel        | 27   |     |     |
| --- | --------------------- | --------- | ------------- | ---- | --- | --- |
|     | switch(config-ip-if)# |           | no vrf attach | vrf2 |     |     |
AssignsIPv6inIPv6tunnel8tovrf3.
|     | switch(config)#       | interface | tunnel     | 8 mode | ip 6in6 |     |
| --- | --------------------- | --------- | ---------- | ------ | ------- | --- |
|     | switch(config-ip-if)# |           | vrf attach | vrf3   |         |     |
ReassignsIPv6inIPv6tunnel8tothedefaultVRF.
|                                         | switch(config)#       | interface | tunnel        | 8    |     |     |
| --------------------------------------- | --------------------- | --------- | ------------- | ---- | --- | --- |
|                                         | switch(config-ip-if)# |           | no vrf attach | vrf3 |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                       |           | SwitchSeries) |      |     | 162 |

Chapter 9

IP Source Lockdown

IP Source Lockdown

IP source lockdown provides added security by preventing IP source address spoofing on a per-port basis.
Every packet is inspected for this purpose in hardware. When IP source lockdown is enabled, IP traffic
received on an interface (port) is forwarded only if the VLAN, IP address, MAC address, interface (port)
matches the IP binding database entry.

It is best to configure IP source lockdown during a switch maintenance period as enabling it may cause client

traffic to be dropped for 10 to 15 seconds.

To use IPv4 source lockdown, the IPv4 binding database must be populated. The binding database is
typically dynamically populated by DHCPv4 snooping that learns and saves the binding information.
Alternatively, the IPv4 binding database can be statically populated with the ipv4 source-binding
command described in this chapter. Often DHCPv4 snooping is used to dynamically populate most of the IP
binding database along with the ipv4 source-binding command that is used to add the binding
information for several known and trusted clients, typically administrators. For dynamic IP binding database
population with DHCPv4 snooping, see DHCP snooping.

To use IPv6 source lockdown, the IPv6 binding database must be populated. The binding database is
typically dynamically populated by DHCPv6 snooping that learns and saves the binding information.
Alternatively, the IPv6 binding database can be statically populated with the ipv6 source-binding
command described in this chapter. Often DHCPv6 snooping is used to dynamically populate most of the
IPv6 binding database along with the ipv6 source-binding command that is used to add the binding
information for several known and trusted clients, typically administrators. For dynamic IPv6 binding
database population with DHCPv6 snooping, see DHCP snooping.

IP source lockdown should not be configured on ISL (inter-switch link) ports.

IPv4 source lockdown commands

ipv4 source-binding

Syntax

ipv4 source-binding <VLAN-ID> <IPV4-ADDR> <MAC-ADDR> <IFNAME>
no ipv4 source-binding <VLAN-ID> <IPV4-ADDR> <MAC-ADDR> <IFNAME>

Description

Adds static IPv4 client source binding information to the switch IP binding database. Although DHCPv4
snooping is often used to dynamically populate the binding database, this command is available for
manually adding entries to the switch IP binding database.

Statically configured IP binding information supersedes any dynamically collected binding information for the

same client.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

163

The no form of this command removes the specified binding that was statically configured with the ipv4
source-binding command. The no form has no effect on bindings that were dynamically configured with
DHCPv4 snooping.

Command context

config

Parameters

<VLAN-ID>

Specifies the ID of an existing VLAN on which the client is connected. Range: 1 to 4094.

<IPV4-ADDR>

Specifies the client IPv4 unicast address.

<MAC-ADDR>

Specifies the client MAC address.

<IFNAME>

Specifies the interface on which the client is connected.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Adding a static IPv4 binding:

switch(config)# ipv4 source-binding 1 10.2.1.4 00:50:56:96:e4:cf 1/1/1

Removing a IPv4 binding:

switch(config)# no ipv4 source-binding 1 10.2.1.4 00:50:56:96:e4:cf 1/1/1

ipv4 source-lockdown

Syntax

ipv4 source-lockdown
no ipv4 source-lockdown

Description

Enables IPv4 source lockdown for all VLANs on the selected interface (port).

The no form of this command disables IPv4 source lockdown for the selected interface (port).

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

IP Source Lockdown | 164

EnablingIPv4sourcelockdownoninterface1/1/1:
|     | switch(config)#    | interface | 1/1/1           |     |     |     |
| --- | ------------------ | --------- | --------------- | --- | --- | --- |
|     | switch(config-if)# | ipv4      | source-lockdown |     |     |     |
EnablingIPv4sourcelockdownoninterfacelag112:
|     | switch(config)#    | interface | lag112          |     |     |     |
| --- | ------------------ | --------- | --------------- | --- | --- | --- |
|     | switch(config-if)# | ipv4      | source-lockdown |     |     |     |
DisablingIPv4sourcelockdownoninterface1/1/1:
|     | switch(config)#      | interface | 1/1/1           |       |     |     |
| --- | -------------------- | --------- | --------------- | ----- | --- | --- |
|     | switch(config-if)#   | no ipv4   | source-lockdown |       |     |     |
|     | ipv4 source-lockdown |           | hardware        | retry |     |     |
Syntax
|     | ipv4 source-lockdown | hardware | retry <VLAN-ID> | <IPV4-ADDR> |     |     |
| --- | -------------------- | -------- | --------------- | ----------- | --- | --- |
Description
RetriestheIPv4sourcelockdownhardwareprogrammingforaclientidentifiedbyVLANandIPv4address.
Commandcontext
config
Parameters
<VLAN-ID>
SpecifiestheIDofanexistingVLANonwhichtheclientisconnected.Range:1to4094.
<IPV4-ADDR>
SpecifiestheclientIPv4unicastaddress.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfigureIPv4sourcelockdownhardwareretryfortheclientonVLAN10.
switch(config)#
|     |                          | ipv4 source-lockdown |     | hardware retry | 10 1.1.2.1 |     |
| --- | ------------------------ | -------------------- | --- | -------------- | ---------- | --- |
|     | show ipv4 source-binding |                      |     |                |            |     |
Syntax
|     | show ipv4 source-binding | [vsx-peer] |     |     |     |     |
| --- | ------------------------ | ---------- | --- | --- | --- | --- |
Description
ShowsallIPv4staticsourcebindinginformationirrespectiveofsourcelockdownconfiguration..
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 165 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

Command context

Operator (>) or Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

On the 6400 Switch Series, interface identification differs.

Showing all IPv4 source binding information:

switch# show ipv4 source-binding

VLAN

PORT
-------------- --------- ----------------- --------- -------- -------------
1/1/1
1/1/2

aa:bb:cc:dd:ee:ff Yes
aa:ab:cc:dd:ee:ff Yes

1.2.3.4
10.20.30.40

HW-STATUS FROM

static
static

IPv4-ADDRESS

MAC-ADDRESS

2
12

show ipv4 source-lockdown

Syntax

show ipv4 source-lockdown [binding [interface <IFNAME> | ip <IPV4-ADDR> | mac <MAC-ADDR> |
vlan <VLAN-ID>] | interface <IFNAME>] [vsx-peer]

Description

Shows summary or detailed IPv4 source lockdown information. When entered without parameters,
summary status information for all interfaces (ports) in the binding database is shown.

Command context

Operator (>) or Manager (#)

Parameters

binding

Specifies that detailed lockdown binding record information is to be displayed. The binding database
record can be identified by any one of interface (port), ip, mac, or vlan.

interface <IFNAME>

Specifies the client interface (port). When entered without the binding parameter, the summary status
information is displayed for the specified interface.

ip <IPV4-ADDR>

Specifies the client IPv4 unicast address.

mac <MAC-ADDR>

Specifies the client MAC address.

vlan <VLAN-ID>

IP Source Lockdown | 166

SpecifiestheIDofanexistingVLANonwhichtheclientisconnected.Range:1to4094.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingthesummarystatusinformationforallinterfacesinthebindingdatabase:
|     | switch#   | show ipv4 source-lockdown |           |     |     |     |
| --- | --------- | ------------------------- | --------- | --- | --- | --- |
|     | INTERFACE | LOCKDOWN                  | HW-STATUS |     |     |     |
|     | --------- | --------                  | --------- |     |     |     |
|     | 1/1/1     | Yes                       | Yes       |     |     |     |
|     | 1/1/2     | Yes                       | No        |     |     |     |
|     | lag112    | Yes                       | Yes       |     |     |     |
Showingthesummarystatusinformationforthespecifiedinterfaceinthebindingdatabase:
|     | switch#   | show ipv4 source-lockdown |           | interface | 1/1/2 |     |
| --- | --------- | ------------------------- | --------- | --------- | ----- | --- |
|     | INTERFACE | LOCKDOWN                  | HW-STATUS |           |       |     |
|     | --------- | --------                  | --------- |           |       |     |
|     | 1/1/2     | Yes                       | No        |           |       |     |
Showingthedetailedbindingrecordandrelatedinformationforallinterfacesinthebindingdatabase:
|                                         | switch#        | show ipv4 source-lockdown |                     | binding     |     |     |
| --------------------------------------- | -------------- | ------------------------- | ------------------- | ----------- | --- | --- |
|                                         | Interface      | Name                      | : 1/1/1             |             |     |     |
|                                         | VLAN Id        |                           | : 2000              |             |     |     |
|                                         | MAC Address    |                           | : 00:50:56:96:e4:cf |             |     |     |
|                                         | IP Address     |                           | : 192.168.142.113   |             |     |     |
|                                         | Time Remaining |                           | : static            |             |     |     |
|                                         | Lockdown       | Status                    | : Yes               |             |     |     |
|                                         | Hardware       | Status                    | : Yes               |             |     |     |
|                                         | Hardware       | Error Reason              | : --                |             |     |     |
|                                         | Interface      | Name                      | : 1/1/2             |             |     |     |
|                                         | VLAN Id        |                           | : 100               |             |     |     |
|                                         | MAC Address    |                           | : 00:50:56:96:04:4d |             |     |     |
|                                         | IP Address     |                           | : 120.168.43.52     |             |     |     |
|                                         | Time Remaining |                           | : 115 seconds       |             |     |     |
|                                         | Lockdown       | Status                    | : Yes               |             |     |     |
|                                         | Hardware       | Status                    | : No                |             |     |     |
|                                         | Hardware       | Error Reason              | : Resource          | unavailable |     |     |
|                                         | Interface      | Name                      | : lag112            |             |     |     |
|                                         | VLAN Id        |                           | : 12                |             |     |     |
|                                         | MAC Address    |                           | : 00:50:56:96:d8:3d |             |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                |                           | SwitchSeries)       |             |     | 167 |

| IP Address     |              | : 120.168.76.182 |     |     |
| -------------- | ------------ | ---------------- | --- | --- |
| Time Remaining |              | : static         |     |     |
| Lockdown       | Status       | : Yes            |     |     |
| Hardware       | Status       | : Yes            |     |     |
| Hardware       | Error Reason | : --             |     |     |
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
Showingthedetailedbindingrecordandrelatedinformationforinterfacelag112(identifiedinthisexample
commandbytheIPaddress):
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
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/1(identifiedinthisexample
commandbytheMACaddress):
| switch#        | show ipv4 source-lockdown |                     | binding | mac 00:50:56:96:e4:cf |
| -------------- | ------------------------- | ------------------- | ------- | --------------------- |
| Interface      | Name                      | : 1/1/1             |         |                       |
| VLAN Id        |                           | : 2000              |         |                       |
| MAC Address    |                           | : 00:50:56:96:e4:cf |         |                       |
| IP Address     |                           | : 192.168.142.113   |         |                       |
| Time Remaining |                           | : static            |         |                       |
| Lockdown       | Status                    | : Yes               |         |                       |
| Hardware       | Status                    | : Yes               |         |                       |
| Hardware       | Error Reason              | : --                |         |                       |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/2(identifiedinthisexample
commandbytheVLAN):
| switch#     | show ipv4 source-lockdown |                     | binding | vlan 100 |
| ----------- | ------------------------- | ------------------- | ------- | -------- |
| Interface   | Name                      | : 1/1/2             |         |          |
| VLAN Id     |                           | : 100               |         |          |
| MAC Address |                           | : 00:50:56:96:04:4d |         |          |
IPSourceLockdown|168

|      | IP Address      |          | : 120.168.43.52 |             |     |     |     |
| ---- | --------------- | -------- | --------------- | ----------- | --- | --- | --- |
|      | Time Remaining  |          | : 115 seconds   |             |     |     |     |
|      | Lockdown Status |          | : Yes           |             |     |     |     |
|      | Hardware Status |          | : No            |             |     |     |     |
|      | Hardware Error  | Reason   | : Resource      | unavailable |     |     |     |
| IPv6 | source          | lockdown |                 | commands    |     |     |     |
| ipv6 | source-binding  |          |                 |             |     |     |     |
Syntax
| ipv6 | source-binding      | <VLAN-ID> | <IPV6-ADDR> |     | <MAC-ADDR> | <IFNAME> |     |
| ---- | ------------------- | --------- | ----------- | --- | ---------- | -------- | --- |
| no   | ipv6 source-binding | <VLAN-ID> | <IPV6-ADDR> |     | <MAC-ADDR> | <IFNAME> |     |
Description
AddsstaticIPv6clientsourcebindinginformationtotheswitchIPv6bindingdatabase.AlthoughDHCPv6
snoopingisoftenusedtodynamicallypopulatethebindingdatabase,thiscommandisavailablefor
manuallyaddingentriestotheswitchIPv6bindingdatabase.
StaticallyconfiguredIPv6bindinginformationsupersedesanydynamicallycollectedbindinginformationforthe
sameclient.
Thenoformofthiscommandremovesthespecifiedbindingthatwasstaticallyconfiguredwiththeipv6
source-bindingcommand.Thenoformhasnoeffectonbindingsthatweredynamicallyconfiguredwith
DHCPv6snooping.
Commandcontext
config
Parameters
<VLAN-ID>
SpecifiestheIDofanexistingVLANonwhichtheclientisconnected.Range:1to4094.
<IPV6-ADDR>
SpecifiestheclientIPv6address.
<MAC-ADDR>
SpecifiestheclientMACaddress.
<IFNAME>
Specifiestheinterfaceonwhichtheclientisconnected.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
AddingastaticIPv6binding:
switch(config)# ipv6 source-binding 2 2000::2 00:12:11:44:55:12 1/1/28
RemovingaIPv6binding:
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     |     | 169 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- | --- |

switch(config)# no ipv6 source-binding 2 2000::2 00:12:11:44:55:12 1/1/28
ipv6 source-lockdown
Syntax
ipv6 source-lockdown
no ipv6 source-lockdown
Description
EnablesIPv6sourcelockdownforallVLANsontheselectedinterface(port).
ThenoformofthiscommanddisablesIPv6sourcelockdownfortheselectedinterface(port).
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingIPv6sourcelockdownoninterface1/1/1:
| switch(config)#    | interface | 1/1/1           |     |
| ------------------ | --------- | --------------- | --- |
| switch(config-if)# | ipv6      | source-lockdown |     |
EnablingIPv6sourcelockdownoninterfacelag112:
| switch(config)#    | interface | lag112          |     |
| ------------------ | --------- | --------------- | --- |
| switch(config-if)# | ipv6      | source-lockdown |     |
DisablingIPv6sourcelockdownoninterface1/1/1:
| switch(config)#      | interface | 1/1/1           |       |
| -------------------- | --------- | --------------- | ----- |
| switch(config-if)#   | no ipv6   | source-lockdown |       |
| ipv6 source-lockdown |           | hardware        | retry |
Syntax
| ipv6 source-lockdown | hardware | retry <VLAN-ID> | <IPV6-ADDR> |
| -------------------- | -------- | --------------- | ----------- |
Description
RetriestheIPV6sourcelockdownhardwareprogrammingforaclientidentifiedbyVLANandIPv6address.
Commandcontext
config
Parameters
IPSourceLockdown|170

<VLAN-ID>
SpecifiestheIDofanexistingVLANonwhichtheclientisconnected.Range:1to4094.
<IPV6-ADDR>
SpecifiestheclientIPv6address.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
ConfigureIPv6sourcelockdownhardwareretryfortheclientonVLAN1.
|     | switch(config)# |                     | ipv6 source-lockdown |     | hardware | retry 1 2000::2 |     |     |     |
| --- | --------------- | ------------------- | -------------------- | --- | -------- | --------------- | --- | --- | --- |
|     | show            | ipv6 source-binding |                      |     |          |                 |     |     |     |
Syntax
|     | show ipv6 | source-binding | [vsx-peer] |     |     |     |     |     |     |
| --- | --------- | -------------- | ---------- | --- | --- | --- | --- | --- | --- |
Description
ShowsallIPv6staticsourcebindinginformationirrespectiveofsourcelockdownconfiguration.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingallIPv6sourcebindinginformation:
|     |      | switch# | show | ipv6 source-binding |     |           |      |              |     |
| --- | ---- | ------- | ---- | ------------------- | --- | --------- | ---- | ------------ | --- |
|     | PORT |         | VLAN | MAC-ADDRESS         |     | HW-STATUS | FROM | IPv6-ADDRESS |     |
-------------- --------- ----------------- --------- -------- -------------
|     | 1/1/1  |                      | 1234 | 00:50:56:96:e4:cf |     | --  | static | 3000::1 |     |
| --- | ------ | -------------------- | ---- | ----------------- | --- | --- | ------ | ------- | --- |
|     | 1/1/1  |                      | 1    | 00:50:56:96:04:4d |     | --  | static | 3000::2 |     |
|     | 1/1/24 |                      | 1    | 00:01:01:00:00:01 |     | Yes | static | 1001::1 |     |
|     | show   | ipv6 source-lockdown |      |                   |     |     |        |         |     |
Syntax
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) |     |     |     |     | 171 |
| --------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |

show ipv6 source-lockdown [binding [interface <IFNAME> | ip <IPV6-ADDR> | mac <MAC-ADDR> |
| vlan <VLAN-ID>] | |   | interface | <IFNAME>] | [vsx-peer] |     |
| --------------- | --- | --------- | --------- | ---------- | --- |
Description
ShowssummaryordetailedIPv6sourcelockdowninformation.Whenenteredwithoutparameters,
summarystatusinformationforallinterfaces(ports)inthebindingdatabaseisshown.
Commandcontext
Operator(>)orManager(#)
Parameters
binding
Specifiesthatdetailedlockdownbindingrecordinformationistobedisplayed.Thebindingdatabase
recordcanbeidentifiedbyanyoneofinterface(port),ip,mac,orvlan.
| interface | <IFNAME> |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- |
Specifiestheclientinterface(port).Whenenteredwithoutthebindingparameter,thesummarystatus
informationisdisplayedforthespecifiedinterface.
ip <IPV6-ADDR>
SpecifiestheclientIPv6address.
mac <MAC-ADDR>
SpecifiestheclientMACaddress.
vlan <VLAN-ID>
SpecifiestheIDofanexistingVLANonwhichtheclientisconnected.Range:1to4094.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingthesummarystatusinformationforallinterfacesinthebindingdatabase:
| switch#   | show ipv6 | source-lockdown |           |     |     |
| --------- | --------- | --------------- | --------- | --- | --- |
| INTERFACE | LOCKDOWN  |                 | HW-STATUS |     |     |
| --------- | --------  |                 | --------- |     |     |
| 1/1/1     | Yes       |                 | Yes       |     |     |
| 1/1/2     | Yes       |                 | Yes       |     |     |
| lag112    | Yes       |                 | --        |     |     |
Showingthesummarystatusinformationforthespecifiedinterfaceinthebindingdatabase:
switch#
|           | show ipv6 | source-lockdown |           | interface | 1/1/2 |
| --------- | --------- | --------------- | --------- | --------- | ----- |
| INTERFACE | LOCKDOWN  |                 | HW-STATUS |           |       |
| --------- | --------  |                 | --------- |           |       |
| 1/1/2     | Yes       |                 | No        |           |       |
IPSourceLockdown|172

Showingthedetailedbindingrecordandrelatedinformationforallinterfacesinthebindingdatabase:
|     | switch#        | show ipv6 source-lockdown |                                 | binding     |     |     |
| --- | -------------- | ------------------------- | ------------------------------- | ----------- | --- | --- |
|     | Interface      | Name                      | : 1/1/1                         |             |     |     |
|     | VLAN Id        |                           | : 1234                          |             |     |     |
|     | MAC Address    |                           | : 00:50:56:96:e4:cf             |             |     |     |
|     | IP Address     |                           | : aaaa:bbbb:cccc:dddd:eeee:1234 |             |     |     |
|     | Time Remaining |                           | : static                        |             |     |     |
|     | Lockdown       | Status                    | : Yes                           |             |     |     |
|     | Hardware       | Status                    | : Yes                           |             |     |     |
|     | Hardware       | Error Reason              | : --                            |             |     |     |
|     | Interface      | Name                      | : 1/1/2                         |             |     |     |
|     | VLAN Id        |                           | : 1234                          |             |     |     |
|     | MAC Address    |                           | : 00:50:56:96:04:4d             |             |     |     |
|     | IP Address     |                           | : 4000::1                       |             |     |     |
|     | Time Remaining |                           | : 3290 seconds                  |             |     |     |
|     | Lockdown       | Status                    | : Yes                           |             |     |     |
|     | Hardware       | Status                    | : No                            |             |     |     |
|     | Hardware       | Error Reason              | : Resource                      | unavailable |     |     |
|     | Interface      | Name                      | : lag112                        |             |     |     |
|     | VLAN Id        |                           | : 151                           |             |     |     |
|     | MAC Address    |                           | : 00:50:56:96:d8:3d             |             |     |     |
|     | IP Address     |                           | : 1001::5                       |             |     |     |
|     | Time Remaining |                           | : 1200 seconds                  |             |     |     |
|     | Lockdown       | Status                    | : No                            |             |     |     |
|     | Hardware       | Status                    | : --                            |             |     |     |
|     | Hardware       | Error Reason              | : --                            |             |     |     |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/2:
|     | switch#        | show ipv6 source-lockdown |                     | binding     | interface 1/1/2 |     |
| --- | -------------- | ------------------------- | ------------------- | ----------- | --------------- | --- |
|     | Interface      | Name                      | : 1/1/2             |             |                 |     |
|     | VLAN Id        |                           | : 1234              |             |                 |     |
|     | MAC Address    |                           | : 00:50:56:96:04:4d |             |                 |     |
|     | IP Address     |                           | : 4000::1           |             |                 |     |
|     | Time Remaining |                           | : 3290 seconds      |             |                 |     |
|     | Lockdown       | Status                    | : Yes               |             |                 |     |
|     | Hardware       | Status                    | : No                |             |                 |     |
|     | Hardware       | Error Reason              | : Resource          | unavailable |                 |     |
Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/2(identifiedinthisexample
commandbytheIPaddress):
|                                         | switch#        | show ipv6 source-lockdown |                     | binding | ip 4000::1 |     |
| --------------------------------------- | -------------- | ------------------------- | ------------------- | ------- | ---------- | --- |
|                                         | Interface      | Name                      | : 1/1/2             |         |            |     |
|                                         | VLAN Id        |                           | : 1234              |         |            |     |
|                                         | MAC Address    |                           | : 00:50:56:96:04:4d |         |            |     |
|                                         | IP Address     |                           | : 4000::1           |         |            |     |
|                                         | Time Remaining |                           | : 515 seconds       |         |            |     |
|                                         | Lockdown       | Status                    | : No                |         |            |     |
|                                         | Hardware       | Status                    | : --                |         |            |     |
|                                         | Hardware       | Error Reason              | : --                |         |            |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |                |                           | SwitchSeries)       |         |            | 173 |

Showingthedetailedbindingrecordandrelatedinformationforinterface1/1/1(identifiedinthisexample
commandbytheMACaddress):
| switch#    | show ipv6 | source-lockdown                 | binding mac | 00:50:56:96:e4:cf |
| ---------- | --------- | ------------------------------- | ----------- | ----------------- |
| Interface  | Name      | : 1/1/1                         |             |                   |
| VLAN       | Id        | : 1234                          |             |                   |
| MAC        | Address   | : 00:50:56:96:e4:cf             |             |                   |
| IP Address |           | : aaaa:bbbb:cccc:dddd:eeee:1234 |             |                   |
| Time       | Remaining | : static                        |             |                   |
| Lockdown   | Status    | : Yes                           |             |                   |
| Hardware   | Status    | : Yes                           |             |                   |
| Hardware   | Error     | Reason : --                     |             |                   |
Showingthedetailedbindingrecordandrelatedinformationforinterfacelag112(identifiedinthisexample
commandbytheVLAN):
switch#
|            | show ipv6 | source-lockdown     | binding vlan | 151 |
| ---------- | --------- | ------------------- | ------------ | --- |
| Interface  | Name      | : lag112            |              |     |
| VLAN       | Id        | : 151               |              |     |
| MAC        | Address   | : 00:50:56:96:d8:3d |              |     |
| IP Address |           | : 1001::5           |              |     |
| Time       | Remaining | : 1200 seconds      |              |     |
| Lockdown   | Status    | : No                |              |     |
| Hardware   | Status    | : --                |              |     |
| Hardware   | Error     | Reason : --         |              |     |
IPSourceLockdown|174

Chapter 10

Internet Control Message Protocol
(ICMP)

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

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

175

ICMP messages are sent when one or more of the following scenarios occur:

n A datagram cannot reach its destination.

n The gateway does not have the buffering capacity to forward a datagram.

n The gateway can direct the host to send traffic on a shorter route.

ICMP redirect messages
ICMP redirect messages are used by routers to notify the hosts on the data link that a better route is
available for a particular destination.

When ICMP redirect messages are sent
The switch is configured to send redirects by default. ICMP redirect messages are sent when one or more of
the following scenarios occur:

n The interface on which the packet comes into the router is the same interface on which the packet gets

routed out.

n The subnet or network of the source IP address is on the same subnet or network of the next-hop IP

address of the routed packet.

n The datagram is not source-routed.

n The destination unicast address is unreachable. In this case, the router generates the ICMP destination

unreachable message to inform the source host about the situation.

ICMP commands

ip icmp redirect

Syntax

ip icmp redirect
no ip icmp redirect

Description

Enables the sending of ICMPv4 and ICMPv6 redirect messages to the source host. Enabled by default.

The no form of this command disables ICMPv4 and ICMPv6 redirect messages to the source host.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ICMP redirect messages:

switch(config)# ip icmp redirect

Disabling ICMP redirect messages:

Internet Control Message Protocol (ICMP) | 176

|     | switch(config)#  | no ip icmp | redirect |     |
| --- | ---------------- | ---------- | -------- | --- |
|     | ip icmp throttle |            |          |     |
Syntax
|     | ip icmp throttle    | <packet-interval> |     |     |
| --- | ------------------- | ----------------- | --- | --- |
|     | no ip icmp throttle |                   |     |     |
Description
UsedtoconfigurethethrottleparameterforbothICMPv4andICMPv6errormessagesandredirect
messages.
ThenoformofthiscommanddisablesthethrottleparameterforbothICMPv4andICMPv6errormessages
andredirectmessages.
Commandcontext
config
Parameters
<packet-interval>
SpecifiestheICMPv4/v6packetintervalinseconds.Default:1second.Range:1-86400.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingthethrottleparameterforbothICMPv4andICMPv6errormessagesandredirectmessages:
|     | switch(config)# | ip icmp | throttle 3000 |     |
| --- | --------------- | ------- | ------------- | --- |
DisablingthethrottleparameterforbothICMPv4andICMPv6errormessagesandredirectmessages:
|     | switch(config)#     | no ip icmp | throttle |     |
| --- | ------------------- | ---------- | -------- | --- |
|     | ip icmp unreachable |            |          |     |
Syntax
|     | ip icmp unreachable    |     |     |     |
| --- | ---------------------- | --- | --- | --- |
|     | no ip icmp unreachable |     |     |     |
Description
EnablesthesendingofICMPv4andICMPv6destinationunreachablemessagesontheswitchtoasource
hostwhenaspecifichostisunreachable.Theunreachablehostaddressoriginatesfromthefailedpacked.
Defaultsetting.
ThenoformofthiscommanddisablesthesendingofICMPv4andICMPv6destinationunreachable
messagesfromtheswitchtoasourcehostwhenaspecifichostisunreachable.Thiscommanddoesnot
preventotherhostsfromsendinganICMPunreachablemessage.
Commandcontext
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) | 177 |
| --------------------------------------- | --- | --- | ------------- | --- |

config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingICMPv4andICMPv6destinationunreachablemessagestoasourcehost:
| switch(config)# | ip icmp | unreachable |
| --------------- | ------- | ----------- |
DisablingICMPv4andICMPv6destinationunreachablemessagestoasourcehost:
| switch(config)# | no ip icmp | unreachable |
| --------------- | ---------- | ----------- |
InternetControlMessageProtocol(ICMP)|178

Chapter 11

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

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

179

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
n DefinesthreedomainstoappendtoDNSrequestsdomain1.com,domain2.com,domain3.comwith
trafficforwardingonVRFmainvrf.
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
| DNS    | client      | commands |     |     |     |
| ------ | ----------- | -------- | --- | --- | --- |
| ip dns | domain-list |          |     |     |     |
Syntax
| ip dns    | domain-list | <DOMAIN-NAME> | [vrf | <VRF-NAME>]      |     |
| --------- | ----------- | ------------- | ---- | ---------------- | --- |
| no ip dns | domain-list | <DOMAIN-NAME> |      | [vrf <VRF-NAME>] |     |
Description
DNS|180

ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
Thenoformofthiscommandremovesadomainfromthelist.
Commandcontext
config
Parameters
|     | list <DOMAIN-NAME> |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
Specifiesadomainname.Uptosixdomainscanbeaddedtothelist.Length:1to256characters.
|     | vrf <VRF-NAME> |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
SpecifiesaVRFname.Default:default.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
|     | switch(config)# | ip dns | domain-list | domain1.com |     |     |
| --- | --------------- | ------ | ----------- | ----------- | --- | --- |
|     | switch(config)# | ip dns | domain-list | domain2.com |     |     |
Thisexampledefinesalistwithtwoentries,domain2.comanddomain5.com,withrequestsbeingsenton
mainvrf.
|     | switch(config)# | ip dns | domain-list | domain2.com | vrf mainvrf |     |
| --- | --------------- | ------ | ----------- | ----------- | ----------- | --- |
|     | switch(config)# | ip dns | domain-list | domain5.com | vrf mainvrf |     |
Thisexampleremovestheentrydomain1.com.
|     | switch(config)#    | no ip dns | domain-list | domain1.com |     |     |
| --- | ------------------ | --------- | ----------- | ----------- | --- | --- |
|     | ip dns domain-name |           |             |             |     |     |
Syntax
|     | ip dns domain-name    | <DOMAIN-NAME> | [ vrf | <VRF-NAME>       | ]   |     |
| --- | --------------------- | ------------- | ----- | ---------------- | --- | --- |
|     | no ip dns domain-name | <DOMAIN-NAME> |       | [ vrf <VRF-NAME> | ]   |     |
Description
ConfiguresadomainnamethatisappendedtotheDNSrequest.ThedomaincanbeeitherIPv4orIPv6.By
default,requestsareforwardedonthedefaultVRF.Ifadomainlistisdefinedwiththecommandip dns
domain-list,thedomainnamedefinedwiththiscommandisignored.
Thenoformofthiscommandremovesthedomainname.
Commandcontext
config
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 181 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

Parameters

<DOMAIN-NAME>

Specifies the domain name to append to DNS requests. Length: 1 to 256 characters.

vrf <VRF-NAME>

Specifies a VRF name. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the default domain name to domain.com:

switch(config)# ip dns domain-name domain.com

Removing the default domain name domain.com:

switch(config)# no ip dns domain-name domain.com

ip dns host

Syntax

ip dns host <HOST-NAME> <IP-ADDR> [ vrf <VRF-NAME> ]

no ip dns host <HOST-NAME> <IP-ADDR> [ vrf <VRF-NAME> ]

Description

Associates a static IP address with a hostname. The DNS client returns this IP address instead of querying a
DNS server for an IP address for the hostname. Up to six hosts can be defined. If no VRF is defined, the
default VRF is used.

The no form of this command removes a static IP address associated with a hostname.

Command context

config

Parameters

host <HOST-NAME>

Specifies the name of a host. Length: 1 to 256 characters.

<IP-ADDR>

Specifies an IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255, or IPv6
format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from 0 to F.

vrf <VRF-NAME>

Specifies a VRF name. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example defines an IPv4 address of 3.3.3.3 for host1.

DNS | 182

|     | switch(config)#                          |        | ip dns    | host host1 | 3.3.3.3           |     |     |
| --- | ---------------------------------------- | ------ | --------- | ---------- | ----------------- | --- | --- |
|     | ThisexampledefinesanIPv6addressofb::5    |        |           |            | forhost           | 1.  |     |
|     | switch(config)#                          |        | ip dns    | host host1 | b::5              |     |     |
|     | Thisexampledefinesremovestheentryforhost |        |           |            | 1withaddressb::5. |     |     |
|     | switch(config)#                          |        | no ip dns | host host1 | b::5              |     |     |
|     | ip dns                                   | server | address   |            |                   |     |     |
Syntax
|     | ip dns    | server-address | <IP-ADDR> | [ vrf | <VRF-NAME> | ]   |     |
| --- | --------- | -------------- | --------- | ----- | ---------- | --- | --- |
|     | no ip dns | server-address | <IP-ADDR> | [ vrf | <VRF-NAME> | ]   |     |
Description
ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
Commandcontext
config
Parameters
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisadecimalnumberfrom0to255,orIPv6
format(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisahexadecimalnumberfrom0toF.
|     | vrf <VRF-NAME> |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- |
SpecifiesaVRFname.Default:default.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Thisexampledefinesanameserverat1.1.1.1.
|     | switch(config)# |     | ip dns | server-address | 1.1.1.1 |     |     |
| --- | --------------- | --- | ------ | -------------- | ------- | --- | --- |
Thisexampledefinesanameserverata::1.
|     | switch(config)# |     | ip dns | server-address | a::1 |     |     |
| --- | --------------- | --- | ------ | -------------- | ---- | --- | --- |
Thisexampleremovesanameserverata::1.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     |     | SwitchSeries) |     |     | 183 |
| --------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- |

| switch(config)# |     | no ip | dns server-address |     | a::1 |     |
| --------------- | --- | ----- | ------------------ | --- | ---- | --- |
| show ip         | dns |       |                    |     |      |     |
Syntax
| show ip dns | [vrf | <VRF-NAME>] | [vsx-peer] |     |     |     |
| ----------- | ---- | ----------- | ---------- | --- | --- | --- |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
Commandcontext
Manager(#)
Parameters
vrf <VRF-NAME>
SpecifiestheVRFforwhichtoshowinformation.IfnoVRFisdefined,thedefaultVRFisused.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
TheseexamplesdefineDNSsettingsandthenshowhowtheyaredisplayedwiththeshow
ip dns
command.
| switch(config)# |     | ip dns | domain-name |     | domain.com  |     |
| --------------- | --- | ------ | ----------- | --- | ----------- | --- |
| switch(config)# |     | ip dns | domain-list |     | domain5.com |     |
| switch(config)# |     | ip dns | domain-list |     | domain8.com |     |
switch(config)#
|                 |     | ip dns | server-address |               | 4.4.4.4        |         |
| --------------- | --- | ------ | -------------- | ------------- | -------------- | ------- |
| switch(config)# |     | ip dns | server-address |               | 6.6.6.6        |         |
| switch(config)# |     | ip dns | host           | host3 5.5.5.5 |                |         |
| switch(config)# |     | ip dns | host           | host2 2.2.2.2 |                |         |
| switch(config)# |     | ip dns | host           | host3 c::12   |                |         |
| switch(config)# |     | ip dns | domain-name    |               | reddomain.com  | vrf red |
| switch(config)# |     | ip dns | domain-list    |               | reddomain5.com | vrf red |
| switch(config)# |     | ip dns | domain-list    |               | reddomain8.com | vrf red |
| switch(config)# |     | ip dns | server-address |               | 4.4.4.5        | vrf red |
| switch(config)# |     | ip dns | server-address |               | 6.6.6.7        | vrf red |
switch(config)#
|                 |           | ip dns         | host    | host3 5.5.5.6 | vrf     | red |
| --------------- | --------- | -------------- | ------- | ------------- | ------- | --- |
| switch(config)# |           | ip dns         | host    | host2 2.2.2.3 | vrf     | red |
| switch(config)# |           | ip dns         | host    | host3 c::13   | vrf red |     |
| switch#         | show      | ip dns         |         |               |         |     |
| VRF Name        | : default |                |         |               |         |     |
| Domain          | Name      | : domain.com   |         |               |         |     |
| DNS Domain      | list      | : domain5.com, |         | domain8.com   |         |     |
| Name            | Server(s) | : 4.4.4.4,     | 6.6.6.6 |               |         |     |
| Host            | Name      | Address        |         |               |         |     |
DNS|184

-------------------------------
|     | host2          |       | 2.2.2.2           |         |     |                |     |     |     |
| --- | -------------- | ----- | ----------------- | ------- | --- | -------------- | --- | --- | --- |
|     | host3          |       | 5.5.5.5           |         |     |                |     |     |     |
|     | host3          |       | c::12             |         |     |                |     |     |     |
|     | VRF Name       | : red |                   |         |     |                |     |     |     |
|     | Domain Name    | :     | reddomain.com     |         |     |                |     |     |     |
|     | DNS Domain     | list  | : reddomain5.com, |         |     | reddomain8.com |     |     |     |
|     | Name Server(s) |       | : 4.4.4.5,        | 6.6.6.7 |     |                |     |     |     |
|     | Host Name      |       | Address           |         |     |                |     |     |     |
-------------------------------
|     | host2           |       | 2.2.2.3        |                |             |             |     |         |     |
| --- | --------------- | ----- | -------------- | -------------- | ----------- | ----------- | --- | ------- | --- |
|     | host3           |       | 5.5.5.6        |                |             |             |     |         |     |
|     | host3           |       | c::13          |                |             |             |     |         |     |
|     | switch(config)# |       | ip dns         | domain-name    |             | domain.com  |     | vrf red |     |
|     | switch(config)# |       | ip dns         | domain-list    |             | domain5.com |     | vrf red |     |
|     | switch(config)# |       | ip dns         | domain-list    |             | domain8.com |     | vrf red |     |
|     | switch(config)# |       | ip dns         | server-address |             | 4.4.4.4     |     | vrf red |     |
|     | switch(config)# |       | ip dns         | server-address |             | 6.6.6.6     |     | vrf red |     |
|     | switch(config)# |       | ip dns         | host           | host3       | 5.5.5.5     | vrf | red     |     |
|     | switch(config)# |       | no ip          | dns host       | host2       | 2.2.2.2     |     | vrf red |     |
|     | switch(config)# |       | ip dns         | host           | host3       | c::12       | vrf | red     |     |
|     | switch#         | show  | ip dns vrf     | red            |             |             |     |         |     |
|     | VRF Name        | : red |                |                |             |             |     |         |     |
|     | Domain Name     | :     | domain.com     |                |             |             |     |         |     |
|     | DNS Domain      | list  | : domain5.com, |                | domain8.com |             |     |         |     |
|     | Name Server(s)  |       | : 4.4.4.4,     | 6.6.6.6        |             |             |     |         |     |
|     | Host Name       |       | Address        |                |             |             |     |         |     |
-------------------------------
|                                         | host3 |     | 5.5.5.5 |               |     |     |     |     |     |
| --------------------------------------- | ----- | --- | ------- | ------------- | --- | --- | --- | --- | --- |
|                                         | host3 |     | c::12   |               |     |     |     |     |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |       |     |         | SwitchSeries) |     |     |     |     | 185 |

Chapter 12

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

Dynamic ARP Inspection

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

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

186

Severaldefensemechanismscanbeputinplaceonaswitchtoprotectagainstattacks:
LimittheamountofARPactivityallowedfromahostoronaport.
n
n EnsurethatallARPpacketsareconsistentwithoneormorebindingdatabases,whichcanbecreated
throughvariousmeans.
EnforceintegritychecksontheARPpacketstocheckagainstdifferentMACorIPaddressesinthe
n
EthernetorIPheaderandARPheader.
ThisreleaseimplementsDynamicARPInspectiontoenforceDHCPsnoopingbindingonallARPpacketsand
islimitedtothe8400platform.Thefeaturewillbedisabledfromthecode,CLI,andschemabytheuseof
appropriateconfigflagsforotherplatforms.
Onlythefollowingissupported:
n EnablinganddisablingofDynamicARPInspectiononaVLANlevel(itdoesnothavetobeSVI).
n DefiningthememberportsofaVLANaseithertrustedoruntrusted.
n OnlyARPtrafficonuntrustedportssubjectedtochecks.
Routedports(RoPs)alwaystreatedastrusted.
n
ListeningtotheDHCPBindingstableandcheckeveryARPpackettomatchagainstthebinding.
n
ARPACLsarenotsupportedinthisreleaseandtheDHCPsnoopingtablewillbetheonlysourceofbinding.
| Configuring | proxy | ARP |     |
| ----------- | ----- | --- | --- |
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtoaninterfacewiththecommandinterface,ortoaninterfaceVLANwiththecommand
| interface | vlan,ortoaLAGwiththecommandinterface |     | lag. |
| --------- | ------------------------------------ | --- | ---- |
3. EnablelocalproxyARPwiththecommandip proxy-arp.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ThisexampleconfiguresproxyARPoninterface1/1/2
| switch# config     |           |           |     |
| ------------------ | --------- | --------- | --- |
| switch(config)#    | interface | 1/1/2     |     |
| switch(config)#    | routing   |           |     |
| switch(config-if)# | ip        | proxy-arp |     |
.
ThisexampleconfiguresproxyARPoninterfaceVLAN30.
| switch# config          |           |              |     |
| ----------------------- | --------- | ------------ | --- |
| switch(config)#         | interface | vlan 30      |     |
| switch(config-vlan-30)# |           | ip proxy-arp |     |
| Configuring             | local     | proxy ARP    |     |
Procedure
ARP|187

1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtoaninterfacewiththecommandinterface,ortoaninterfaceVLANwiththecommand
|     | interface | vlan,ortoaLAGwiththecommandinterface |     | lag. |     |
| --- | --------- | ------------------------------------ | --- | ---- | --- |
3. EnablelocalproxyARPwiththecommandip local-proxy-arp.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ThisexampleconfigureslocalproxyARPoninterface1/1/2
|     | switch# config     |                    |       |     |     |
| --- | ------------------ | ------------------ | ----- | --- | --- |
|     | switch(config)#    | interface          | 1/1/2 |     |     |
|     | switch(config)#    | routing            |       |     |     |
|     | switch(config-if)# | ip local-proxy-arp |       |     |     |
ThisexampleconfigureslocalproxyARPoninterfaceVLAN30.
|     | switch# config          |                |                    |     |     |
| --- | ----------------------- | -------------- | ------------------ | --- | --- |
|     | switch(config)#         | interface      | vlan 30            |     |     |
|     | switch(config-vlan-30)# |                | ip local-proxy-arp |     |     |
|     | Dynamic                 | ARP Inspection |                    |     |     |
ARPisusedforresolvingIPagainstMACaddressesonabroadcastnetworksegmentliketheEthernetand
wasoriginallydefinedbyInternetStandardRFC826.ARPdoesnotsupportanyinherentsecurity
mechanismandassuchdependsonsimpledatagramexchangesfortheresolution,withmanyofthese
beingbroadcast.
Becauseitisanunreliableandnon-secureprotocol,ARPisvulnerabletoattacks.Someattacksmaybe
targetedtowardthenetworkswhereasotherattacksmaybetargetedtowardtheswitchitself.Theattacks
primarilyintendtocreatedenialofservice(DoS)fortheotherentitiespresentinthenetwork.
Mostoftheattacksarecarriedoutinoneofthefollowingthreeforms:
|     | n OverwhelmingtheswitchcontrolplanewithtoomanyARPpackets. |     |     |     |     |
| --- | --------------------------------------------------------- | --- | --- | --- | --- |
n Overwhelmingtheswitchcontrolplanewithtoomanyunresolveddatapackets.
Masqueradingasatrustedgateway/serverbywronglyadvertisingARPs.
n
Severaldefensemechanismscanbeputinplaceonaswitchtoprotectagainstattacks:
LimittheamountofARPactivityallowedfromahostoronaport.
n
EnsurethatallARPpacketsareconsistentwithoneormorebindingdatabases,whichcanbecreated
n
throughvariousmeans.
EnforceintegritychecksontheARPpacketstocheckagainstdifferentMACorIPaddressesinthe
n
EthernetorIPheaderandARPheader.
ThisreleaseimplementsDynamicARPInspectiontoenforceDHCPsnoopingbindingonallARPpacketsand
issupportedonthe6300,6400,and8400platforms.Thefeaturewillbedisabledfromthecode,CLI,and
schemabytheuseofappropriateconfigflagsforotherplatforms.
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 188 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

Only the following is supported:

n Enabling and disabling of Dynamic ARP Inspection on a VLAN level (it does not have to be SVI).

n Defining the member ports of a VLAN as either trusted or untrusted.

n Only ARP traffic on untrusted ports subjected to checks.

n Routed ports (RoPs) always treated as trusted.

n Listening to the DHCP Bindings table and check every ARP packet to match against the binding.

ARP ACLs are not supported in this release and the DHCP snooping table will be the only source of binding.

ARP commands

arp cache-limit

Syntax

arp cache-limit <LIMIT>

Description

Specifies the maximum number of entries in the ARP (Address Resolution Protocol) cache.

Command context

config

Parameters

<LIMIT>

Specifies the maximum number of entries in the ARP cache. Range: 4096 to 131072. Default: 131072.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# arp cache-limit 4097

arp inspection

Syntax

arp inspection

Description

Enables Dynamic ARP Inspection on the current VLAN, forcing all ARP packets from untrusted ports to be
subjected to a MAC-IP association check against a binding table.

The no form of this command disables Dynamic ARP Inspection on the VLAN.

Command context

config-vlan-<VLAN-ID>

Authority

ARP | 189

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingdynamicARPinspection:
|     | switch# configure    | terminal       |     |     |
| --- | -------------------- | -------------- | --- | --- |
|     | switch(config)#      | vlan 1         |     |     |
|     | switch(config-vlan)# | arp inspection |     |     |
DisablingdynamicARPinspection:
|     | switch# configure    | terminal          |     |     |
| --- | -------------------- | ----------------- | --- | --- |
|     | switch(config)#      | vlan 1            |     |     |
|     | switch(config-vlan)# | no arp inspection |     |     |
|     | arp inspection       | trust             |     |     |
Syntax
|     | arp inspection trust    |     |     |     |
| --- | ----------------------- | --- | --- | --- |
|     | no arp inspection trust |     |     |     |
Description
Configurestheinterfaceasatrusted.Allinterfacesareuntrustedbydefault.
Thenoformofthiscommandreturnstheinterfacetothedefaultstate(untrusted).
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Settinganinterfaceastrusted:
|     | switch(config-if)# | arp inspection | trust |     |
| --- | ------------------ | -------------- | ----- | --- |
|     | arp ipv4 mac       |                |       |     |
Syntax
|     | arp ipv4 <IPV4_ADDR>    | mac <MAC_ADDR> |     |     |
| --- | ----------------------- | -------------- | --- | --- |
|     | no arp ipv4 <IPV4_ADDR> | mac <MAC_ADDR> |     |     |
Description
SpecifiesapermanentstaticneighborentryintheARPtable(forIPv4neighbors).
ThenoformofthiscommanddeletesapermanentstaticneighborentryfromtheARPtable.
Commandcontext
config-if
config-if-vlan
| AOS-CX10.07IPServicesGuide|(6300and6400 |     | SwitchSeries) |     | 190 |
| --------------------------------------- | --- | ------------- | --- | --- |

Parameters

ipv4 <IPV4-ADDR>

Specifies the IP address of the neighbor or the virtual IP address of the cluster in IPv4 format (x.x.x.x),
where x is a decimal number from 0 to 255. . Range: 4096 to 131072. Default: 131072.

mac <MAC-ADDR>

Specifies the MAC address of the neighbor or the multicast MAC address in IANA format
(xx:xx:xx:xx:xx:xx), where x is a hexadecimal number from 0 to F. Range: 4096 to 131072. Default:
131072.

Authority

Administrators or local user group members with execution rights for this command.

Example

On the 6400 Switch Series, interface identification differs.

Configuring a static ARP entry on a interface VLAN 10:

switch(config)# interface vlan 10
switch(config-if-vlan)# arp ipv4 2.2.2.2 mac 01:00:5e:00:00:01

Removing a static ARP entry on interface VLAN10:

switch(config)# interface vlan 10
switch(config-if-vlan)# no arp ipv4 2.2.2.2 mac 01:00:5e:00:00:01

clear arp

Syntax

clear arp [port <PORT-ID> | vrf {all-vrfs | <VRF-NAME>}]

Description

Clears IPv4 and IPv6 neighbor entries from the ARP table. If you do not specify any parameters, ARP table
entries are cleared for the default VRF.

Command context

Manager (#)

Parameters

port <PORT-ID>

Specifies a physical port on the switch. Format: member/slot/port. For example: 1/1/1. .

all-vrfs

Selects all VRFs.

<VRF-NAME>

Specifies the name of a VRF. Default: default.

Authority

Administrators or local user group members with execution rights for this command.

Examples

ARP | 191

Clearing all IPv4 and IPv6 neighbor ARP entries for the default VRF:

switch# clear arp

Clearing all ARP neighbor entries for a port (On the 6400 Switch Series, interface identification differs.):

switch# clear arp 1/1/35

Clearing all IPv4 and IPv6 neighbor ARP entries for all VRFs:

switch# clear arp vrf all-vrfs

Clearing all IPv4 and IPv6 neighbor ARP entries for a specific VRF instance:

switch# clear arp vrf RED

ip local-proxy-arp

Syntax

ip local-proxy-arp
no ip local-proxy-arp

Description

Enables local proxy ARP on the specified interface. Local proxy ARP is supported on Layer 3 physical
interfaces and on VLAN interfaces. To enable local proxy ARP on an interface, routing must be enabled on
that interface.

The no form of this command disables local proxy ARP on the specified interface.

Command context

config-if
config-if-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Enabling local proxy ARP on interface 1/1/1:

switch# interface 1/1/1
switch(config-if)# ip local proxy-arp

Enabling local proxy ARP on interface VLAN 3:

switch# interface vlan 3
switch(config-if-vlan)# ip local-proxy-arp

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

192

Disabling local proxy ARP on on interface 1/1/1.

switch# interface 1/1/1
switch(config-if)# no ip local-proxy-arp

ipv6 neighbor mac

Syntax

ipv6 neighbor <IPV6-ADDR> mac <MAC-ADDR>
no ipv6 neighbor <IPV6-ADDR> mac <MAC-ADDR>

Description

Specifies a permanent static neighbor entry in the ARP table (for IPv6 neighbors).

The no form of this command deletes a permanent static neighbor entry from the ARP table.

Command context

config-if

Parameters

<IPV6-ADDR>>

Specifies an IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. Range: 4096 to 131072. Default: 131072.

mac <MAC-ADDR>>

Specifies the MAC address of the neighbor (xx:xx:xx:xx:xx:xx), where x is a hexadecimal number from
0 to F. Range: 4096 to 131072. Default: 131072.

Authority

Administrators or local user group members with execution rights for this command.

Example

On the 6400 Switch Series, interface identification differs.

Creates a static ARP entry on interface 1/1/1.

switch(config)# interface 1/1/1
switch(config-if)# arp ipv6 neighbor 2001:0db8:85a3::8a2e:0370:7334 mac
00:50:56:96:df:c8

ip proxy-arp

Syntax

ip proxy-arp
no ip proxy-arp

Description

Enables proxy ARP for the specified Layer 3 interface. Proxy ARP is supported on Layer 3 physical interfaces,
LAG interfaces, and VLAN interfaces. It is disabled by default. To enable proxy ARP on an interface, routing
must be enabled on that interface.

The no form of this command disables proxy ARP for the specified interface.

ARP | 193

Command context

config-if
config-if-vlan
config-lag-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling proxy ARP on interface 1/1/1:

switch# interface 1/1/1
switch(config-if)# ip proxy-arp

Enabling proxy ARP on VLAN 3:

switch# interface vlan 3
switch(config-if-vlan)# ip proxy-arp

Enabling proxy ARP on a LAG 11:

switch(config)# int lag 11
switch(config-lag-if)# ip proxy-arp

Disabling proxy ARP on interface 1/1/1:

switch# interface 1/1/1
switch(config-if)# no ip proxy-arp

show arp

Syntax

show arp [vsx-peer]

Description

Shows the entries in the ARP (Address Resolution Protocol) table.

Command context

Manager (#)

Parameters

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Administrators or local user group members with execution rights for this command.

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

194

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
| 192.168.1.2 |               | 00:50:56:96:7b:e0 | vlan10 | 1/1/29 | stale     |     |
| ----------- | ------------- | ----------------- | ------ | ------ | --------- | --- |
| 192.168.1.3 |               | 00:50:56:96:7b:ac | vlan10 | 1/1/1  | reachable |     |
| Total       | Number Of ARP | Entries Listed-   | 2.     |        |           |     |
-------------------------------------------------------------------------------
| show arp | inspection | interface |     |     |     |     |
| -------- | ---------- | --------- | --- | --- | --- | --- |
Syntax
| show arp inspection | interface |     |     |     |     |     |
| ------------------- | --------- | --- | --- | --- | --- | --- |
Description
DisplaysthecurrentconfigurationofdynamicARPinspectiononaVLANorinterface.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch# | show arp inspection | interface |     |     |     |     |
| ------- | ------------------- | --------- | --- | --- | --- | --- |
---------------------------------------------------------------------------
| Interface |     | Trust-State |     |     |     |     |
| --------- | --- | ----------- | --- | --- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 |     | Untrusted |     |     |     |     |
| ----- | --- | --------- | --- | --- | --- | --- |
---------------------------------------------------------------------------
| switch# | show arp inspection | interface | vsx-peer |     |     |     |
| ------- | ------------------- | --------- | -------- | --- | --- | --- |
---------------------------------------------------------------------------
| Interface |     | Trust-State |     |     |     |     |
| --------- | --- | ----------- | --- | --- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 |     | Untrusted |     |     |     |     |
| ----- | --- | --------- | --- | --- | --- | --- |
ARP|195

|     | lag100 | Trusted |     |     |     |
| --- | ------ | ------- | --- | --- | --- |
---------------------------------------------------------------------------
|     | switch# show | arp inspection | interface | 1/1/1 |     |
| --- | ------------ | -------------- | --------- | ----- | --- |
---------------------------------------------------------------------------
|     | Interface | Trust-State |     |     |     |
| --- | --------- | ----------- | --- | --- | --- |
---------------------------------------------------------------------------
|     | 1/1/1 | Untrusted |     |     |     |
| --- | ----- | --------- | --- | --- | --- |
---------------------------------------------------------------------------
|     | show arp | inspection | statistics |     |     |
| --- | -------- | ---------- | ---------- | --- | --- |
Syntax
|     | show arp inspection | statistics |     |     |     |
| --- | ------------------- | ---------- | --- | --- | --- |
Description
DisplaysstatisticsaboutforwardedanddroppedARPpackets.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
|     | switch# show | arp inspection | statistics | vlan 1-200 |     |
| --- | ------------ | -------------- | ---------- | ---------- | --- |
-----------------------------------------------------------------
|     | VLAN Name |     | Forwarded | Dropped |     |
| --- | --------- | --- | --------- | ------- | --- |
-----------------------------------------------------------------
|     | 1 DEFAULT_VLAN_1 |     | 0   | 0   |     |
| --- | ---------------- | --- | --- | --- | --- |
-----------------------------------------------------------------
|     | switch# show | arp inspection | statistics | vlan |     |
| --- | ------------ | -------------- | ---------- | ---- | --- |
-----------------------------------------------------------------
|     | VLAN Name |     | Forwarded | Dropped |     |
| --- | --------- | --- | --------- | ------- | --- |
-----------------------------------------------------------------
|     | 1 DEFAULT_VLAN_1 |     | 0   | 0   |     |
| --- | ---------------- | --- | --- | --- | --- |
|     | 200 VLAN200      |     | 0   | 0   |     |
-----------------------------------------------------------------
|     | show arp | state |     |     |     |
| --- | -------- | ----- | --- | --- | --- |
Syntax
show arp state {all | failed | incomplete | permanent | reachable | stale} [vsx-peer]
Description
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     | 196 |
| --------------------------------------- | --- | --- | ------------- | --- | --- |

Shows ARP (Address Resolution Protocol) cache entries that are in the specified state.

Command context

Operator (>) or Manager (#)

Parameters

all

Shows the ARP cache entries for all VRF (Virtual Router Forwarding) instances.

failed

Shows the ARP cache entries that are in failed state. The neighbor might have been deleted.

incomplete

Shows the ARP cache entries that are in incomplete state.

An incomplete state means that address resolution is in progress and the link-layer address of the
neighbor has not yet been determined. A solicitation request was sent, and the switch is waiting for a
solicitation reply or a timeout.

permanent

Shows the ARP cache entries that are in permanent state. ARP entries that are in a permanent state can
be removed by administrative action only.

reachable

Shows the ARP cache entries that are in reachable state, meaning that the neighbor is known to have
been reachable recently.

stale

Shows ARP cache entries that are in stale state.

ARP cache entries are in the stale state if the elapsed time is in excess of the ARP timeout in seconds
since the last positive confirmation that the forwarding path was functioning properly.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show arp state failed

IPv4 Address
Port
---------------------------------------------------------------------------
192.168.1.4

Physical Port

failed

vlan10

State

MAC

show arp summary

Syntax

show arp summary [all-vrfs | vrf <VRF-NAME>] [vsx-peer]

Description

Shows a summary of the IPv4 and IPv6 neighbor entries on the switch for all VRFs or a specific VRF.

ARP | 197

Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SelectsallVRFs.
|     | vrf <VRF-NAME> |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
SpecifiesthenameofaVRF.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingsummaryARPinformationforallVRFs:
|     | switch#     | show arp | summary all-vrfs |        |      |     |
| --- | ----------- | -------- | ---------------- | ------ | ---- | --- |
|     | ARP Entry's | State    |                  | : IPv4 | IPv6 |     |
-------------------------------------------------------
|     | Number | of Reachable  | ARP entries | : 2 | 0   |     |
| --- | ------ | ------------- | ----------- | --- | --- | --- |
|     | Number | of Stale ARP  | entries     | : 0 | 0   |     |
|     | Number | of Failed     | ARP entries | : 2 | 2   |     |
|     | Number | of Incomplete | ARP entries | : 0 | 0   |     |
|     | Number | of Permanent  | ARP entries | : 0 | 0   |     |
-------------------------------------------------------
|     | Total ARP | Entries: | 6   | : 4 | 2   |     |
| --- | --------- | -------- | --- | --- | --- | --- |
-------------------------------------------------------
ShowingasummaryofallIPv4andIPv6neighborentriesontheprimaryandsecondary(peer)switches:
vsx-primary#
|     |             | show  | arp summary |      |      |     |
| --- | ----------- | ----- | ----------- | ---- | ---- | --- |
|     | ARP Entry's | State |             | IPv4 | IPv6 |     |
---------------------------------------------------------
|     | Number | of Reachable  | ARP entries | 25858 | 32231 |     |
| --- | ------ | ------------- | ----------- | ----- | ----- | --- |
|     | Number | of Stale ARP  | entries     | 0     | 1     |     |
|     | Number | of Failed     | ARP entries | 0     | 257   |     |
|     | Number | of Incomplete | ARP entries | 0     | 0     |     |
|     | Number | of Permanent  | ARP entries | 0     | 0     |     |
---------------------------------------------------------
|                                         | Total ARP    | Entries- | 58347         | 25858    | 32489 |     |
| --------------------------------------- | ------------ | -------- | ------------- | -------- | ----- | --- |
|                                         | vsx-primary# | show     | arp summary   | vsx-peer |       |     |
| AOS-CX10.07IPServicesGuide|(6300and6400 |              |          | SwitchSeries) |          |       | 198 |

| ARP Entry's |     | State |     |     | IPv4 | IPv6 |
| ----------- | --- | ----- | --- | --- | ---- | ---- |
---------------------------------------------------------
| Number | of Reachable  |     | ARP     | entries | 25858 | 32168 |
| ------ | ------------- | --- | ------- | ------- | ----- | ----- |
| Number | of Stale      | ARP | entries |         | 0     | 3     |
| Number | of Failed     | ARP | entries |         | 0     | 317   |
| Number | of Incomplete |     | ARP     | entries | 0     | 0     |
| Number | of Permanent  |     | ARP     | entries | 0     | 0     |
---------------------------------------------------------
| Total ARP | Entries- |     | 58346 |     | 25858 | 32488 |
| --------- | -------- | --- | ----- | --- | ----- | ----- |
---------------------------------------------------------
| show arp | timeout |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- |
Syntax
| show arp timeout |     | [<INTERFACE>] |     | [vsx-peer] |     |     |
| ---------------- | --- | ------------- | --- | ---------- | --- | --- |
Description
Showstheage-outperiodforeachARP(AddressResolutionProtocol)entryforaport,LAG,orVLAN
interface.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE>
Specifiesaphysicalport,VLAN,orLAGontheswitch.Forphysicalports,usetheformat
member/slot/port(forexample,1/3/1).
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingARPtimeoutinformationforaport:
| switch#      | show | arp timeout |     | 1/1/1 |     |     |
| ------------ | ---- | ----------- | --- | ----- | --- | --- |
| ARP Timeout: |      |             |     |       |     |     |
------------------
| Port     |     | VRF     |     |     |     | Timeout |
| -------- | --- | ------- | --- | --- | --- | ------- |
| 1/1/1    |     | default |     |     |     | 600     |
| show arp | vrf |         |     |     |     |         |
Syntax
| show arp {all-vrfs |     | |   | vrf <VRF-NAME>} |     | [vsx-peer] |     |
| ------------------ | --- | --- | --------------- | --- | ---------- | --- |
ARP|199

Description
ShowstheARPtableforallVRFinstances,orforthenamedVRF.
Commandcontext
Operator(>)orManager(#)
Parameters
all-vrfs
SpecifiesallVRFs.
|     | vrf <VRF-NAME> |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
SpecifiesthenameofaVRF.Length:1to32alphanumericcharacters.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingARPentriesforVRFtest.
|     | switch# show      | arp vrf test |     |     |     |     |
| --- | ----------------- | ------------ | --- | --- | --- | --- |
|     | ARP IPv4 Entries: |              |     |     |     |     |
-------------------------------------------------------
|     | IPv4 Address | MAC               | Port Physical | Port State | VRF  |     |
| --- | ------------ | ----------------- | ------------- | ---------- | ---- | --- |
|     | 10.20.30.40  | 00:50:56:bd:6a:c5 | 1/1/29 1/1/29 | reachable  | test |     |
-------------------------------------------------------
|     | Total Number | Of ARP Entries | Listed: 1. |     |     |     |
| --- | ------------ | -------------- | ---------- | --- | --- | --- |
-------------------------------------------------------
|     | switch# show      | arp all-vrfs |     |     |     |     |
| --- | ----------------- | ------------ | --- | --- | --- | --- |
|     | ARP IPv4 Entries: |              |     |     |     |     |
-------------------------------------------------------
|     | IPv4 Address   | MAC               | Port Physical | Port State | VRF  |     |
| --- | -------------- | ----------------- | ------------- | ---------- | ---- | --- |
|     | 192.168.120.10 | 00:50:56:bd:10:be | 1/1/32 1/1/32 | reachable  | red  |     |
|     | 10.20.30.40    | 00:50:56:bd:6a:c5 | 1/1/29 1/1/29 | reachable  | test |     |
-------------------------------------------------------
|     | Total Number | Of ARP Entries | Listed: 2. |     |     |     |
| --- | ------------ | -------------- | ---------- | --- | --- | --- |
-------------------------------------------------------
ShowingARPentriesforallVRFs.
|     | switch# show      | arp all-vrfs |     |     |     |     |
| --- | ----------------- | ------------ | --- | --- | --- | --- |
|     | ARP IPv4 Entries: |              |     |     |     |     |
-------------------------------------------------------
|     | IPv4 Address   | MAC               | Port Physical | Port State | VRF  |     |
| --- | -------------- | ----------------- | ------------- | ---------- | ---- | --- |
|     | 192.168.120.10 | 00:50:56:bd:10:be | 1/1/32 1/1/32 | reachable  | red  |     |
|     | 10.20.30.40    | 00:50:56:bd:6a:c5 | 1/1/29 1/1/29 | reachable  | test |     |
-------------------------------------------------------
|     | Total Number | Of ARP Entries | Listed: 2. |     |     |     |
| --- | ------------ | -------------- | ---------- | --- | --- | --- |
-------------------------------------------------------
| AOS-CX10.07IPServicesGuide|(6300and6400 |     |     | SwitchSeries) |     |     | 200 |
| --------------------------------------- | --- | --- | ------------- | --- | --- | --- |

show ipv6 neighbors

Syntax

show ipv6 neighbors {all-vrfs | vrf <VRF-NAME>} [vsx-peer]

Description

Shows entries in the ARP table for all IPv6 neighbors for all VRFs or for a specific VRF.

When no parameters are specified, this command shows all ARP entries for the default VRF, and state
information for reachable and stale entries only.

Command context

Operator (>) or Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Parameters

all-vrfs

Specifies all VRFs.

vrf <VRF-NAME>

Specifies a VRF name. Length: 1 to 32 alphanumeric characters.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Examples

switch# show ipv6 neighbors
IPv6 Entries:

-------------------------------------------------------

IPv6 Address

MAC

Port

Physical Port State

fe80::a21d:48ff:fe8f:2700

a0:1d:48:8f:27:00 vlan2300 1/1/31

reachable

fe80::f603:43ff:fe80:a600

f4:03:43:80:a6:00 vlan2300 1/1/30

reachable

-------------------------------------------------------

Total Number Of IPv6 Neighbors Entries Listed: 2.

-------------------------------------------------------

show ipv6 neighbors state

Syntax

show ipv6 neighbors state {all | failed | incomplete | permanent | reachable | stale} [vsx-
peer]

Description

ARP | 201

Shows all IPv6 neighbor ARP (Address Resolution Protocol) cache entries, or those cache entries that are in
the specified state.

Command context

Operator (>) or Manager (#)

Parameters

all

Shows all ARP cache entries.

failed

Shows ARP cache entries that are in failed state. The neighbor might have been deleted. Set the
neighbor to be unreachable.

incomplete

Shows ARP cache entries that are in incomplete state.

An incomplete state means that address resolution is in progress and the link-layer address of the
neighbor has not yet been determined. This means that a solicitation request was sent, and you are
waiting for a solicitation reply or a timeout.

permanent

Shows ARP cache entries that are in permanent state.

reachable

Shows ARP cache entries that are in reachable state, meaning that the neighbor is known to have been
reachable recently.

stale

Shows ARP cache entries that are in stale state.

ARP cache entries are in the stale state if the elapsed time is in excess of the ARP timeout in seconds
since the last positive confirmation that the forwarding path was functioning properly.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

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

AOS-CX 10.07 IP Services Guide | (6300 and 6400 Switch Series)

202

Chapter 13
|           |           |           | Support | and other | resources |
| --------- | --------- | --------- | ------- | --------- | --------- |
| Support   | and other | resources |         |           |           |
| Accessing | Aruba     | Support   |         |           |           |
ArubaSupportServices https://www.arubanetworks.com/support-services/
ArubaSupportPortal https://asp.arubanetworks.com/
NorthAmericatelephone
1-800-943-4526(US&CanadaToll-FreeNumber)
+1-408-754-1200(Primary-TollNumber)
+1-650-385-6582(Backup-TollNumber-Useonlywhenallother
numbersarenotworking)
Internationaltelephone https://www.arubanetworks.com/support-services/contact-
support/
BesuretocollectthefollowinginformationbeforecontactingSupport:
| n Technicalsupportregistrationnumber(ifapplicable) |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- |
| n Productname,modelorversion,andserialnumber       |     |     |     |     |     |
| n Operatingsystemnameandversion                    |     |     |     |     |     |
| n Firmwareversion                                  |     |     |     |     |     |
Errormessages
n
Product-specificreportsandlogs
n
| n Add-onproductsorcomponents      |             |     |     |     |     |
| --------------------------------- | ----------- | --- | --- | --- | --- |
| n Third-partyproductsorcomponents |             |     |     |     |     |
| Other                             | usefulsites |     |     |     |     |
Otherwebsitesthatcanbeusedtofindinformation:
AirheadssocialforumsandKnowledge https://community.arubanetworks.com/
Base
Softwarelicensing https://lms.arubanetworks.com/
End-of-Lifeinformation https://www.arubanetworks.com/support-services/end-of-life/
Arubasoftwareanddocumentation https://asp.arubanetworks.com/downloads
| Accessing | updates |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- |
YoucanaccessupdatesfromtheArubaSupportPortalortheHPEMyNetworkingWebsite.
| Aruba | Support | Portal |     |     |     |
| ----- | ------- | ------ | --- | --- | --- |
203
| AOS-CX10.07IPServicesGuide| | (6300and6400 | SwitchSeries) |     |     |     |
| --------------------------- | ------------ | ------------- | --- | --- | --- |

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

Warranty information
To view warranty information for your product, go to https://www.arubanetworks.com/support-
services/product-warranties/.

Regulatory information
To view the regulatory information for your product, view the Safety and Compliance Information for Server,
Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

Aruba is committed to providing our customers with information about the chemical substances in our
products as needed to comply with legal requirements, environmental data (company programs, product
recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For more
information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

Support and other resources | 204