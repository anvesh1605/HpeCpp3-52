AOS-CX 10.08 IP Services
Guide

8320, 8325, 8360 Switch Series

Published: February 2022
Edition: 3

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
| About this                          | document                            | 7   |
| Applicableproducts                  |                                     | 7   |
| Latestversionavailableonline        |                                     | 7   |
| Commandsyntaxnotationconventions    |                                     | 7   |
| Abouttheexamples                    |                                     | 8   |
| Identifyingswitchportsandinterfaces |                                     | 8   |
| IRDP                                |                                     | 10  |
| ConfiguringIRDP                     |                                     | 11  |
| IRDPcommands                        |                                     | 12  |
|                                     | diag-dumpirdpbasic                  | 12  |
|                                     | ipirdp                              | 12  |
|                                     | ipirdpholdtime                      | 13  |
|                                     | ipirdpmaxadvertinterval             | 14  |
|                                     | ipirdpminadvertinterval             | 15  |
|                                     | ipirdppreference                    | 16  |
|                                     | showipirdp                          | 17  |
| IPv6 Router                         | Advertisement                       | 19  |
| ConfiguringIPv6RA                   |                                     | 19  |
| IPv6RAscenario                      |                                     | 21  |
| IPv6RAcommands                      |                                     | 21  |
|                                     | ipv6address<global-unicast-address> | 22  |
|                                     | ipv6addressautoconfig               | 22  |
|                                     | ipv6addresslink-local               | 23  |
|                                     | ipv6ndcache-limit                   | 24  |
|                                     | ipv6nddadattempts                   | 25  |
|                                     | ipv6ndhop-limit                     | 25  |
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
|                                     | showipv6ndradnssearch-list          | 43  |
3
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

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
http-proxy
lease
netbios-name-server
netbios-node-type
option
pool

43

45
45
46
47
48
51
51
52
53
54
55
55
56
57
57
58
59

61
61
61
61
62
62
63
64
65
66
67
75
75
76
77
78
83
83
84
85
86
86
87
88
89
90
91
92
92
93
94
95
96
97
98
99

Contents | 4

|                                                       | range                             |         |          |        | 100 |
| ----------------------------------------------------- | --------------------------------- | ------- | -------- | ------ | --- |
|                                                       | showdhcp-server                   |         |          |        | 101 |
|                                                       | static-bind                       |         |          |        | 103 |
|                                                       | DHCPserverIPv6commands            |         |          |        | 104 |
|                                                       | authoritative                     |         |          |        | 104 |
|                                                       | cleardhcpv6-serverleases          |         |          |        | 105 |
|                                                       | dhcv6p-serverexternal-storage     |         |          |        | 106 |
|                                                       | dhcpv6-servervrf                  |         |          |        | 107 |
|                                                       | disable                           |         |          |        | 108 |
|                                                       | dns-server                        |         |          |        | 108 |
|                                                       | enable                            |         |          |        | 109 |
|                                                       | lease                             |         |          |        | 110 |
|                                                       | option                            |         |          |        | 110 |
|                                                       | pool                              |         |          |        | 111 |
|                                                       | range                             |         |          |        | 112 |
|                                                       | showdhcpv6-server                 |         |          |        | 113 |
|                                                       | static-bind                       |         |          |        | 115 |
| IP Tunnels                                            |                                   |         |          |        | 117 |
| ConfiguringanIPtunnel                                 |                                   |         |          |        | 118 |
| CreatingaGREtunnelfortraversingapublicnetwork         |                                   |         |          |        | 118 |
| CreatingtwoGREtunnelstodifferentdestinationaddresses  |                                   |         |          |        | 120 |
| CreatinganIPv6inIPv4tunnelfortraversingapublicnetwork |                                   |         |          |        | 122 |
| CreatinganIPv6inIPv6tunnelfortraversingapublicnetwork |                                   |         |          |        | 123 |
| IPtunnelscommands                                     |                                   |         |          |        | 125 |
|                                                       | description                       |         |          |        | 125 |
|                                                       | destinationip                     |         |          |        | 126 |
|                                                       | destinationipv6                   |         |          |        | 127 |
|                                                       | interfacetunnel                   |         |          |        | 128 |
|                                                       | ipaddress                         |         |          |        | 130 |
|                                                       | ipv6address                       |         |          |        | 131 |
|                                                       | ipmtu                             |         |          |        | 131 |
|                                                       | showinterfacetunnel               |         |          |        | 133 |
|                                                       | showrunning-configinterfacetunnel |         |          |        | 135 |
|                                                       | shutdown                          |         |          |        | 136 |
|                                                       | sourceip                          |         |          |        | 137 |
|                                                       | sourceipv6                        |         |          |        | 138 |
|                                                       | ttl                               |         |          |        | 139 |
|                                                       | vrfattach                         |         |          |        | 140 |
| Internet                                              | Control                           | Message | Protocol | (ICMP) | 142 |
| ICMPmessagetypes                                      |                                   |         |          |        | 142 |
| WhenICMPmessagesaresent                               |                                   |         |          |        | 142 |
| ICMPredirectmessages                                  |                                   |         |          |        | 143 |
| WhenICMPredirectmessagesaresent                       |                                   |         |          |        | 143 |
| ICMPcommands                                          |                                   |         |          |        | 143 |
|                                                       | ipicmpredirect                    |         |          |        | 143 |
|                                                       | ipicmpthrottle                    |         |          |        | 144 |
|                                                       | ipicmpunreachable                 |         |          |        | 145 |
| DNS                                                   |                                   |         |          |        | 146 |
| DNSclient                                             |                                   |         |          |        | 146 |
| ConfiguringtheDNSclient                               |                                   |         |          |        | 146 |
| DNSclientcommands                                     |                                   |         |          |        | 147 |
|                                                       | ipdnsdomain-list                  |         |          |        | 147 |
|                                                       | ipdnsdomain-name                  |         |          |        | 148 |
5
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |     |     |
| --------------------------- | ----- | ------------- | --- | --- | --- |

|                          | ipdnshost                   |           | 149 |
| ------------------------ | --------------------------- | --------- | --- |
|                          | ipdnsserveraddress          |           | 150 |
|                          | showipdns                   |           | 151 |
| ARP                      |                             |           | 154 |
| ConfiguringproxyARP      |                             |           | 155 |
| ConfiguringlocalproxyARP |                             |           | 155 |
| DynamicARPInspection     |                             |           | 156 |
| ARPcommands              |                             |           | 157 |
|                          | arpinspection               |           | 157 |
|                          | arpinspectiontrust          |           | 157 |
|                          | arpipv4mac                  |           | 158 |
|                          | cleararp                    |           | 159 |
|                          | iplocal-proxy-arp           |           | 160 |
|                          | ipv6neighbormac             |           | 161 |
|                          | ipproxy-arp                 |           | 161 |
|                          | showarp                     |           | 162 |
|                          | showarpinspectioninterface  |           | 163 |
|                          | showarpinspectionstatistics |           | 164 |
|                          | showarpstate                |           | 165 |
|                          | showarpsummary              |           | 166 |
|                          | showarptimeout              |           | 168 |
|                          | showarpvrf                  |           | 168 |
|                          | showipv6neighbors           |           | 170 |
|                          | showipv6neighborsstate      |           | 171 |
| Network                  | Load Balancing              | (NLB)     | 173 |
| NLBcommands              |                             |           | 173 |
|                          | arpipv4mac                  |           | 173 |
|                          | showarp                     |           | 174 |
|                          | showipigmpsnoopingvlangroup |           | 175 |
| Support                  | and Other                   | Resources | 176 |
| AccessingArubaSupport    |                             |           | 176 |
| AccessingUpdates         |                             |           | 176 |
|                          | ArubaSupportPortal          |           | 176 |
|                          | MyNetworking                |           | 177 |
| WarrantyInformation      |                             |           | 177 |
| RegulatoryInformation    |                             |           | 177 |
| DocumentationFeedback    |                             |           | 177 |
Contents|6

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

7

Convention

Usage

{ }

[ ]

… or

...

Braces. Indicates that at least one of the enclosed items is required.

Brackets. Indicates that the enclosed item or items are optional.

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

On the 83xx Switch Series

About this document | 8

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

9

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

10

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

IRDP | 11

| switch(config-if)# |     | ip  | irdp holdtime | 5000 |     |
| ------------------ | --- | --- | ------------- | ---- | --- |
switch(config-if)#
|                    |     | ip  | irdp maxadvertinterval |     | 30  |
| ------------------ | --- | --- | ---------------------- | --- | --- |
| switch(config-if)# |     | ip  | irdp minadvertinterval |     | 25  |
| switch(config-if)# |     | ip  | irdp preference        | 25  |     |
IRDP commands
| diag-dump      | irdp  | basic |     |     |     |
| -------------- | ----- | ----- | --- | --- | --- |
| diag-dump irdp | basic |       |     |     |     |
Description
DisplaysdiagnosticinformationforIRDP.
Example
switch#
|     | diag-dump | irdp | basic |     |     |
| --- | --------- | ---- | ----- | --- | --- |
=========================================================================
| [Start] | Feature | irdp Time | : Thu | Jun 8 09:50:28 | 2017 |
| ------- | ------- | --------- | ----- | -------------- | ---- |
=========================================================================
-------------------------------------------------------------------------
| [Start] | Daemon hpe-rdiscd |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| Interface: | 1/1/1 | (state | : Up) |     |     |
| ---------- | ----- | ------ | ----- | --- | --- |
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
| Router IPs | - 192.168.1.2, |        |       |     |     |
| ---------- | -------------- | ------ | ----- | --- | --- |
| Interface: | 1/1/2          | (state | : Up) |     |     |
rdisc ipv4 (enabled: 0, max:600, min:450, hold:1800, pref:0, isBcast:0)
| Router IPs | - 192.168.2.2, |     |     |     |     |
| ---------- | -------------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
| [End] Daemon | hpe-rdiscd |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- |
-------------------------------------------------------------------------
=========================================================================
| [End] Feature | irdp |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- |
=========================================================================
| Diagnostic | dump | captured | for feature | irdp |     |
| ---------- | ---- | -------- | ----------- | ---- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
ip irdp
12
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

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
EnablingIRDPoninterface1/1/1withpackettypesettothedefaultvalue(multicast).
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | ip irdp   |       |
EnablingIRDPoninterface1/1/1withpackettypesettobroadcast.
| switch(config)#    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | ip irdp   | broadcast |
DisablingIRDP.
| switch(config)#    | interface | 1/1/1 |
| ------------------ | --------- | ----- |
| switch(config-if)# | no ip     | irdp  |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp holdtime    |        |     |
| ------------------- | ------ | --- |
| ip irdp holdtime    | <TIME> |     |
| no ip irdp holdtime | <TIME> |     |
Description
IRDP|13

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
Settingtheholdtimeforinterface1/1/1to5000seconds:
| switch(config)#    |     | interface | 1/1/1         |      |
| ------------------ | --- | --------- | ------------- | ---- |
| switch(config-if)# |     | ip        | irdp holdtime | 5000 |
Removingthetheholdtimeforinterface1/1/1to5000seconds:
| switch(config)#    |     | interface | 1/1/1            |      |
| ------------------ | --- | --------- | ---------------- | ---- |
| switch(config-if)# |     | no        | ip irdp holdtime | 5000 |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp    | maxadvertinterval |     |        |     |
| ---------- | ----------------- | --- | ------ | --- |
| ip irdp    | maxadvertinterval |     | <TIME> |     |
| no ip irdp | maxadvertinterval |     | <TIME> |     |
Description
Specifiesthemaximumrouteradvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumrouteradvertisementintervalandrevertsto
thedefaultvalue.
14
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |
| --------------------------- | --- | ------------------- | --- | --- |

| Parameter |     |     |     | Description                                       |     |
| --------- | --- | --- | --- | ------------------------------------------------- | --- |
| <TIME>    |     |     |     | Specifiesthemaximumtimeallowedbetweenthesendingof |     |
unsolicitedrouteradvertisements.Range:4to1800seconds.
Default:600seconds.
Example
Settingtheadvertisementintervalforinterface1/1/1to30seconds:
| switch(config)#    |     | interface | 1/1/1                  |     |     |
| ------------------ | --- | --------- | ---------------------- | --- | --- |
| switch(config-if)# |     | ip        | irdp maxadvertinterval |     | 30  |
Removingtheadvertisementintervalforinterface1/1/1to30seconds:
| switch(config)#    |     | interface | 1/1/1                     |     |     |
| ------------------ | --- | --------- | ------------------------- | --- | --- |
| switch(config-if)# |     | no        | ip irdp maxadvertinterval |     | 30  |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
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
IRDP|15

Settingtheminimumadvertisementintervalforinterface1/1/1to25seconds:
| switch(config)#    |     | interface | 1/1/1             |     |     |
| ------------------ | --- | --------- | ----------------- | --- | --- |
| switch(config-if)# |     | ip irdp   | minadvertinterval |     | 25  |
Removingtheminimumadvertisementintervalforinterface1/1/1to25seconds:
| switch(config)#    |     | interface | 1/1/1                  |     |     |
| ------------------ | --- | --------- | ---------------------- | --- | --- |
| switch(config-if)# |     | no ip     | irdp minadvertinterval |     | 25  |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ip irdp    | preference |         |     |     |     |
| ---------- | ---------- | ------- | --- | --- | --- |
| ip irdp    | preference | <LEVEL> |     |     |     |
| no ip irdp | preference | <LEVEL> |     |     |     |
Description
SpecifiestheIRDPpreferencelevel.Ifahostreceivesmultiplerouteradvertisementmessagesfrom
differentrouters,thehostselectstherouterthatsentthemessagewiththehighestpreferenceasthe
defaultgateway.
ThenoformofthiscommandremovesthespecifiedIRDPpreferencelevelandrevertstothedefaultvalue.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<LEVEL>
SpecifiestheIRDPpreferencelevel.Range:-2147483648to
2147483647.Default:0.
Example
SettingtheIRDPpreferencelevelforinterface1/1/1to25.
| switch(config)#    |     | interface | 1/1/1      |     |     |
| ------------------ | --- | --------- | ---------- | --- | --- |
| switch(config-if)# |     | ip irdp   | preference | 25  |     |
RemovingtheIRDPpreferencelevelforinterface1/1/1to25.
16
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|     |     |     | no ip irdp | preference | 25  |     |
| --- | --- | --- | ---------- | ---------- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip      | irdp       |     |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- | --- |
| show ip irdp | [vsx-peer] |     |     |     |     |     |
Description
DisplaysIRDPconfigurationsettings.
| Parameter  |     |     |     | Description                |     |     |
| ---------- | --- | --- | --- | -------------------------- | --- | --- |
| <location> |     |     |     | Specifiesoneofthesevalues: |     |     |
<FQDN>:afullyqualifieddomainname.
n
n <IPV4>:anIPv4address.
<IPV6>:anIPv6address.
n
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISLisdown,the
outputfromtheVSXpeerswitchisnotdisplayed.ThisparameterisavailableonswitchesthatsupportVSX.
Example
| switch#     | show      | ip irdp |          |     |     |     |
| ----------- | --------- | ------- | -------- | --- | --- | --- |
| ICMP Router | Discovery |         | Protocol |     |     |     |
Interface Status Advertising Minimum Maximum Holdtime Preference
|     |     |     | Address | Interval | Interval |     |
| --- | --- | --- | ------- | -------- | -------- | --- |
--------- -------- ----------- -------- -------- -------- -----------
| 1/1/1 | Enabled  |     | multicast | 6   | 8   | 10 10    |
| ----- | -------- | --- | --------- | --- | --- | -------- |
| 1/1/2 | Disabled |     | multicast | 450 | 600 | 1800 0   |
| 1/1/3 | Enabled  |     | broadcast | 450 | 600 | 1800 115 |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
IRDP|17

CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
18
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

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
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

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
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |
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
(DAD)foraunicastaddressconfiguredonaninterface.
Thenoformofthiscommandsetsthenumberofattemptstothedefaultvalue.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
dad attempts <NUM-ATTEMPTS> Specifiesthenumberofneighborsolicitationstosend.Range:0-
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
| ipv6 nd | hop-limit |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
25
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

| ipv6 nd | hop-limit    | <HOPLIMIT>   |     |     |     |
| ------- | ------------ | ------------ | --- | --- | --- |
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
<MTU-VALUE>
SpecifiestheMTUsize.Range:1280-65535bytes.Default:1500
bytes.
Examples
| switch(config)#    |     | interface | 1/1/1  |      |     |
| ------------------ | --- | --------- | ------ | ---- | --- |
| switch(config-if)# |     | ipv6      | nd mtu | 1300 |     |
CommandHistory
IPv6RouterAdvertisement|26

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
ConfigurestheNDtimebetweenDADneighborsolicitationssentforanunresolveddestination,orbetween
duplicateaddressdetectionneighborsolicitationrequests.Increasethissettingwhenneighborsolicitation
retriesorfailuresareoccurring,orinaslow(WAN)network.
Thenoformofthiscommandsetsthens-intervaltothedefaultvalue.
|     | Parameter |     |     |     | Description |     |
| --- | --------- | --- | --- | --- | ----------- | --- |
<TIME>
Specifiestheneighborsolicitationinterval.Range:1000-3600000
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
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| ipv6 | nd                | prefix                          |                          |                  |              |               |
| ---- | ----------------- | ------------------------------- | ------------------------ | ---------------- | ------------ | ------------- |
| ipv6 | nd                | prefix <IPV6-ADDR>/<PREFIX-LEN> |                          |                  |              |               |
|      | [no-advertise     |                                 | | [valid                 | <LIFETIME-VALUE> |              | preferred     |
|      | <LIFETIME-VALUE>] |                                 | | no-autoconfig          |                  | | no-onlink] |               |
| no   | ipv6              | nd prefix                       | <IPV6-ADDR>/<PREFIX-LEN> |                  |              | [no-advertise |
27
| AOS-CX10.08IPServicesGuide| |     |     | (83xx SwitchSeries) |     |     |     |
| --------------------------- | --- | --- | ------------------- | --- | --- | --- |

| | [valid          | <LIFETIME-VALUE>      | preferred       | <LIFETIME-VALUE>        |     |     |
| ----------------- | --------------------- | --------------- | ----------------------- | --- | --- |
| ] | no-autoconfig | | no-onlink]          |                 |                         |     |     |
| ipv6 nd prefix    | default [no-advertise | |               | [valid <LIFETIME-VALUE> |     |     |
| preferred         | <LIFETIME-VALUE>]     | | no-autoconfig | | no-onlink]}           |     |     |
no ipv6 nd prefix default [no-advertise | [valid <LIFETIME-VALUE>
| preferred | <LIFETIME-VALUE>] | | no-autoconfig | | no-onlink]} |     |     |
| --------- | ----------------- | --------------- | ------------- | --- | --- |
Description
SpecifiesprefixesfortheroutingswitchtoincludeinRAstransmittedontheinterface.IPv6hostsusethe
prefixesinRAstoautoconfigurethemselveswithglobalunicastaddresses.Theautoconfiguredaddressofa
hostiscomposedoftheadvertisedprefixandtheinterfaceidentifierinthecurrentlink-localaddressofthe
host.
Bydefault,advertise,autoconfig,andonlinkareset.
Thenoformofthiscommandremovestheconfigurationontheinterface.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IPV6-ADDR>/<PREFIX-LEN> SpecifiestheIPv6prefixtoadvertiseinRA.Format:X:X::X:X/M
default Specifiesapplyconfigurationtoallon-linkprefixesthatarenot
|     |     |     | individuallysetbytheipv6 | ra prefix | <IPV6-ADDR>/<PREFIX- |
| --- | --- | --- | ------------------------ | --------- | -------------------- |
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
| no-advertise |     |     | SpecifiesdonotadvertiseprefixinRA. |     |     |
| ------------ | --- | --- | ---------------------------------- | --- | --- |
valid <LIFETIME-VALUE> Specifiesthetotaltime,inseconds,theprefixremainsavailable
beforebecomingunusable.Afterpreferred-lifetimeexpiration,
anyautoconfiguredaddressisdeprecatedandusedonlyfor
transactionsonlybeforepreferred-lifetimeexpires.Ifthevalid
lifetimeexpires,theaddressbecomesinvalid.
|     |     |     | Youcanenteravalueinsecondsorentervalid |     | infinitewhich |
| --- | --- | --- | -------------------------------------- | --- | ------------- |
setsinfinitelifetime.Default:2,592,000secondswhichis30days.
Range:0–4294967294seconds.
| preferred | <LIFETIME-VALUE> |     |     |     |     |
| --------- | ---------------- | --- | --- | --- | --- |
Specifiesthespanoftimeduringwhichtheaddresscanbefreely
usedasasourceanddestinationfortraffic.Thissettingmustbe
lessthanorequaltothecorrespondingvalid–lifetimesetting.
Youcanenteravalueinsecondsorenterpreferred infinite
whichsetsinfinitelifetime.Default:604,800secondswhichis
sevendays.Range:0–4294967294seconds.
| no-autoconfig |     |     | Specifiesdonotuseprefixforautoconfiguration. |     |     |
| ------------- | --- | --- | -------------------------------------------- | --- | --- |
no-onlink
Specifiesdonotuseprefixforonlinkdetermination.
Examples
IPv6RouterAdvertisement|28

| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)#
ipv6 nd prefix 4001::1/64 valid 30 preferred 10 no-autoconfig no-
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
| Parameter     |        |     |     | Description                           |     |
| ------------- | ------ | --- | --- | ------------------------------------- | --- |
| <DOMAIN-NAME> |        |     |     | SpecifiesthedomainnamesforDNSqueries. |     |
| lifetime      | <TIME> |     |     |                                       |     |
Specifieslifetimeinseconds.Range:4-4294967295seconds.
Default:1800seconds.
Usage
DNSSLcontainsthedomainnamesofDNSsuffixesorIPv6hoststoappendtoshort,unqualifieddomain
n
namesforDNSqueries.
MultipleDNSdomainnamescanbeaddedtotheDNSSLbyusingthecommandrepeatedly.
n
Amaximumofeightserveraddressesareallowed.
n
Examples
| switch(config)# |     | interface | 1/1/1 |     |     |
| --------------- | --- | --------- | ----- | --- | --- |
switch(config-if)# ipv6 nd ra dns search-list test.com lifetime 500
CommandHistory
29
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |
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
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |
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
| AOS-CX10.08IPServicesGuide| |     | (83xx | SwitchSeries) |     |     |
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
| AOS-CX10.08IPServicesGuide| |     | (83xx | SwitchSeries) |     |     |
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
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |
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
| show | ipv6    | nd     | global  | traffic    |     |     |     |
| ---- | ------- | ------ | ------- | ---------- | --- | --- | --- |
| show | ipv6 nd | global | traffic | [vsx-peer] |     |     |     |
Description
DisplaysIPV6NeighborDiscoverytrafficdetailsonadevice.
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
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
IPv6RouterAdvertisement|38

| V2 Reports | :   | 11/0 |     |     |
| ---------- | --- | ---- | --- | --- |
| V1 Leaves  | :   | 0/0  |     |     |
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
| show ipv6 | nd interface |     |     |     |
| --------- | ------------ | --- | --- | --- |
show ipv6 nd interface [<IF-NAME> | all-vrfs | vrf <VRF-NAME>] [vsx-peer]
Description
Displaysneighbordiscoveryinformationforaninterface.Ifnooptionsarespecified,displaysinformation
forthedefaultVRF.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IF-NAME>
DisplaysinformationaboutthespecifiedIPv6enabledinterface.
| all-vrfs |     |     | DisplaysinformationaboutinterfacesinallVRFs. |     |
| -------- | --- | --- | -------------------------------------------- | --- |
vrf <VRF-NAME>
DisplaysinformationaboutinterfacesinaparticularVRF.Or,if
<VRF-NAME>isnotspecified,informationforthedefaultVRFis
displayed.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowinginformationforallVRFs:
| switch#         | show ipv6 nd         | interface                    | all-vrfs    |         |
| --------------- | -------------------- | ---------------------------- | ----------- | ------- |
| List of         | IPv6 Interfaces      | for                          | VRF default |         |
| Interface       | 1/1/1 is up          |                              |             |         |
| Admin           | state is up          |                              |             |         |
| IPv6 address:   |                      |                              |             |         |
| IPv6 link-local | address:             | fe80::7272:cfff:fee7:a8b9/64 |             | [VALID] |
| ICMPv6          | active timers:       |                              |             |         |
| Last            | Router-Advertisement |                              | sent:       |         |
| Next            | Router-Advertisement |                              | sent in:    |         |
39
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| Router-Advertisement |          |             |           | parameters: |                |           |             |     |
| -------------------- | -------- | ----------- | --------- | ----------- | -------------- | --------- | ----------- | --- |
|                      | Periodic |             | interval: | 200         | to             | 600 secs  |             |     |
|                      | Router   | Preference: |           | medium      |                |           |             |     |
|                      | Send     | "Managed    | Address   |             | Configuration" |           | flag: false |     |
|                      | Send     | "Other      | Stateful  |             | Configuration" |           | flag: false |     |
|                      | Send     | "Current    | Hop       | Limit"      |                | field: 64 |             |     |
|                      | Send     | "MTU"       | option    | value:      |                | 1500      |             |     |
|                      | Send     | "Router     | Lifetime" |             | field:         | 1800      |             |     |
|                      | Send     | "Reachable  |           | Time"       | field:         | 0         |             |     |
|                      | Send     | "Retrans    | Timer"    |             | field:         | 0         |             |     |
|                      | Suppress |             | RA: true  |             |                |           |             |     |
|                      | Suppress |             | MTU in    | RA:         | true           |           |             |     |
| ICMPv6               | error    |             | message   | parameters: |                |           |             |     |
|                      | Send     | redirects:  |           | false       |                |           |             |     |
| ICMPv6               | DAD      | parameters: |           |             |                |           |             |     |
|                      | Current  | DAD         | attempt:  |             | 1              |           |             |     |
| List                 | of IPv6  | Interfaces  |           | for         | VRF            | red       |             |     |
| Interface            |          | 1/1/2       | is up     |             |                |           |             |     |
| Admin                | state    | is          | up        |             |                |           |             |     |
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
IPv6RouterAdvertisement|40

|     | Send     | "Router         |              | Lifetime"   | field: | 1800 |     |     |
| --- | -------- | --------------- | ------------ | ----------- | ------ | ---- | --- | --- |
|     | Send     | "Reachable      |              | Time"       | field: | 0    |     |     |
|     | Send     | "Retrans        |              | Timer"      | field: | 0    |     |     |
|     | Suppress |                 | RA:          | true        |        |      |     |     |
|     | Suppress |                 | MTU          | in RA:      | true   |      |     |     |
|     | ICMPv6   | error           | message      | parameters: |        |      |     |     |
|     | Send     | redirects:      |              | false       |        |      |     |     |
|     | ICMPv6   | DAD parameters: |              |             |        |      |     |     |
|     | Current  |                 | DAD attempt: |             | 1      |      |     |     |
ShowinginformationforthedefaultVRF:
switch#
|     |                      | show ipv6            | nd           | interface   |                              |           |             |         |
| --- | -------------------- | -------------------- | ------------ | ----------- | ---------------------------- | --------- | ----------- | ------- |
|     | List of              | IPv6 Interfaces      |              | for         | VRF                          | default   |             |         |
|     | Interface            | 1/1/1                | is           | up          |                              |           |             |         |
|     | Admin                | state                | is up        |             |                              |           |             |         |
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
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | ipv6 | nd  | interface |     | prefix |     |     |     |
| ---- | ---- | --- | --------- | --- | ------ | --- | --- | --- |
show ipv6 nd interface prefix [all-vrfs | vrf <VRF-NAME>] [vsx-peer]
41
| AOS-CX10.08IPServicesGuide| |     |     | (83xx | SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ----- | ------------- | --- | --- | --- | --- |

Description
ShowsIPv6prefixinformationforallVRFsoraspecificVRF.Ifnooptionsarespecified,showsinformation
forthedefaultVRF.
| Parameter      |     |     | Description                       |
| -------------- | --- | --- | --------------------------------- |
| all-vrfs       |     |     | ShowsprefixinformationforallVRFs. |
| vrf <VRF-NAME> |     |     | NameofaVRF.                       |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingprefixinformationforthedefaultVRF:
| switch#    | show ipv6 nd           | interface | prefix   |
| ---------- | ---------------------- | --------- | -------- |
| List of    | IPv6 Interfaces        | for VRF   | default  |
| List of    | IPv6 Prefix advertised |           | on 1/1/1 |
| Prefix     | : 4545::/65            |           |          |
| Enabled    | : Yes                  |           |          |
| Validlife  | time : 2592000         |           |          |
| Preferred  | lifetime               | : 604800  |          |
| On-link    | : Yes                  |           |          |
| Autonomous | : Yes                  |           |          |
ShowinginformationforVRFred:
| switch#    | show ipv6 nd           | interface | prefix vrf red |
| ---------- | ---------------------- | --------- | -------------- |
| List of    | IPv6 Interfaces        | for VRF   | red            |
| List of    | IPv6 Prefix advertised |           | on 1/1/2       |
| Prefix     | : 2001::/64            |           |                |
| Enabled    | : Yes                  |           |                |
| Validlife  | time : 2592000         |           |                |
| Preferred  | lifetime               | : 604800  |                |
| On-link    | : Yes                  |           |                |
| Autonomous | : Yes                  |           |                |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
IPv6RouterAdvertisement|42

Platforms

Command context

Authority

(#)

execution rights for this command. Operators can execute this
command from the operator context (>) only.

show ipv6 nd ra dns search-list
show ipv6 nd ra dns search-list [vsx-peer]

Description

Displays domain name information on all interfaces.

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

show ipv6 nd ra dns server
show ipv6 nd ra dns server [vsx-peer]

Description

Displays DNS server information on all interfaces.

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

43

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

IPv6 Router Advertisement | 44

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

45

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

sFlow | 46

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
47
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

|     | switch(config-if)# |     | ip address | 10.10.12.1/24 |
| --- | ------------------ | --- | ---------- | ------------- |
|     | switch(config)#    |     | quit       |               |
8. VerifysFlowconfiguration
Thefollowingexampleisonlyapplicableforthe8360seriesswitch
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
sFlow|48

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
49
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

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
sFlow|50

|       | c. Configureinterface1/1/1.                          |                    |          |             |            |                   |     |
| ----- | ---------------------------------------------------- | ------------------ | -------- | ----------- | ---------- | ----------------- | --- |
|       | switch(config)#                                      |                    |          | interface   | 1/1/1      |                   |     |
|       | switch(config-if)#                                   |                    |          | no shutdown |            |                   |     |
|       | switch(config-lag-if)#                               |                    |          |             | no routing |                   |     |
|       | switch(config-if)#                                   |                    |          | vlan        | access     | 8                 |     |
|       | d. Configureinterface1/1/2and1/1/3asmembersofLAG100. |                    |          |             |            |                   |     |
|       | switch#                                              | (config)#interface |          |             | 1/1/2      |                   |     |
|       | switch(config-if)#                                   |                    |          | no shutdown |            |                   |     |
|       | switch(config-if)#                                   |                    |          | lag         | 100        |                   |     |
|       | switch(config-if)#                                   |                    |          | exit        |            |                   |     |
|       | switch(config)-if#                                   |                    |          | interface   |            | 1/1/3             |     |
|       | switch(config-if)#                                   |                    |          | no shutdown |            |                   |     |
|       | switch(config-if)#                                   |                    |          | lag         | 100        |                   |     |
|       | switch(config-if)#                                   |                    |          | exit        |            |                   |     |
| sFlow | agent                                                |                    | commands |             |            |                   |     |
| clear | sflow                                                | statistics         |          |             |            |                   |     |
| clear | sflow                                                | statistics         | {global  | |           | interface  | <INTERFACE-NAME>} |     |
Description
ThiscommandclearsthesFlowsamplestatisticscounterto0eithergloballyorforaspecificinterface.
| Parameter |     |                  |     |     |     | Description                        |     |
| --------- | --- | ---------------- | --- | --- | --- | ---------------------------------- | --- |
| global    |     |                  |     |     |     | Specifiesallinterfacesontheswitch. |     |
| interface |     | <INTERFACE-NAME> |     |     |     |                                    |     |
Specifiesthenameofaninterfaceontheswitch.
Examples
ClearingtheglobalsFlowsamplestatisticscounterto0globally:
| switch(config)# |     |     | clear | sflow | statistics | global |     |
| --------------- | --- | --- | ----- | ----- | ---------- | ------ | --- |
ClearingtheglobalsFlowsamplestatisticscounterto0forinterface1/1/1:
| switch(config)# |     |     | clear | sflow | statistics | interface | 1/1/1 |
| --------------- | --- | --- | ----- | ----- | ---------- | --------- | ----- |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |
CommandInformation
| Platforms |     | Commandcontext |     |     |     | Authority |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
51
| AOS-CX10.08IPServicesGuide| |     | (83xx | SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- | --- | --- |

sflow
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
CommandHistory
sFlow|52

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
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
n doesnotchangewithtime
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
53
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

CommandHistory
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
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
collector <IP-ADDR> SpecifiestheIPaddressofacollectorinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
port <PORT> SpecifiestheUDPportonwhichtosendinformationtothesFlow
collector.Range:0to65536.Default:6343.
vrf <VRF>
SpecifiestheVRFonwhichtosendinformationtothesFlow
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
sFlow|54

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| Parameter   |        | Description |
| ----------- | ------ | ----------- |
| header-size | <SIZE> |             |
SpecifiesthesFlowheadersizeinbytes.Range:64to256.Default:
128.
Examples
Settingtheheadersizeto64bytes:
switch(config)#
|     | sflow header-size | 64  |
| --- | ----------------- | --- |
55
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

Settingtheheadersizetothedefaultvalueof128bytes:
| switch(config)# | no sflow header-size |     |
| --------------- | -------------------- | --- |
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
sFlow|56

| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| sflow      | mode          |     |          |         |     |
| ---------- | ------------- | --- | -------- | ------- | --- |
| sflow mode | {ingress      | |   | egress   | | both} |     |
| no sflow   | mode {ingress |     | | egress | | both} |     |
Description
SetsthesFlowsamplingmode.Thedefaultmodeisingress.
Thenoformofthecommandsetsthesamplingmodetoingress.Executingthenoformofthecommand
withtheingressoptionwillhavenoimpactasingressisthedefaultmode.
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
ResettingthesFlowsamplingmodetothedefaultofingressfrompreviouslyconfiguredmodeofegress:
switch#
|                 | configure |     | terminal |             |     |
| --------------- | --------- | --- | -------- | ----------- | --- |
| switch(config)# |           | no  | sflow    | mode egress |     |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
8360 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| sflow         | polling    |              |     |     |     |
| ------------- | ---------- | ------------ | --- | --- | --- |
| sflow polling | <INTERVAL> |              |     |     |     |
| no sflow      | polling    | [<INTERVAL>] |     |     |     |
57
| AOS-CX10.08IPServicesGuide| |     | (83xx | SwitchSeries) |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- |

Description
DefinestheglobalpollingintervalforsFlowinseconds.
Thenoformofthiscommandsetsthepollingintervaltothedefaultvalueof30seconds.
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
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
sFlow|58

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
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show       | sflow      |                   |     |            |
| ---------- | ---------- | ----------------- | --- | ---------- |
| show sflow | [interface | <INTERFACE-NAME>] |     | [vsx-peer] |
Description
ShowssFlowconfigurationsettingsandstatisticsforallinterfaces,orforaspecificinterface
| Parameter |                  |     |     | Description |
| --------- | ---------------- | --- | --- | ----------- |
| interface | <INTERFACE-NAME> |     |     |             |
Specifiesthenameofaninterfaceontheswitch.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Thefollowingexamplesareonlyapplicableforthe8360seriesswitch
| switch# | show   | sflow         |     |     |
| ------- | ------ | ------------- | --- | --- |
| sFlow   | Global | Configuration |     |     |
-----------------------------------------
| sFlow |     |     |     | enabled |
| ----- | --- | --- | --- | ------- |
59
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |
| --------------------------- | --- | ------------------- | --- | --- |

| Collector     | IP/Port/Vrf |     | 10.10.10.2/6343/default |     |
| ------------- | ----------- | --- | ----------------------- | --- |
| Agent Address |             |     | 10.0.0.1                |     |
| Sampling      | Rate        |     | 1024                    |     |
| Polling       | Interval    |     | 30                      |     |
| Header        | Size        |     | 128                     |     |
| Max Datagram  | Size        |     | 1400                    |     |
| Sampling      | Mode        |     | both                    |     |
| sFlow Status  |             |     |                         |     |
-----------------------------------------
| Running       | - Yes |             |     |     |
| ------------- | ----- | ----------- | --- | --- |
| sFlow enabled | on    | Interfaces: |     |     |
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
sFlow|60

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
By default, the switch operates as a DHCP client on the management interface allowing it to automatically
obtain an IP address from a DHCP server on the network to which it is connected.

DHCP client commands

ip dhcp

ip dhcp

Description

Enables the DHCP client on the management interface enabling the interface to automatically obtain an IP
address from a DHCP server on the network. By default, the DHCP client is enabled.

Examples

This example enables the DHCP client on the management interface.

switch(config)# interface mgmt
switch(config-if-mgmt)# ip dhcp
switch(config-if-mgmt)# no shutdown

If the interface is not enabled, you can enable it by entering the no shutdown command.

Command History

Release

10.07 or earlier

Command Information

Modification

--

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

61

Platforms

Command context

Authority

All platforms

config-if-mgmt

Administrators or local user group members with execution rights
for this command.

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

Inter-VRF DHCP relay

The DHCP relay agent supports anycast gateway using option 82 sub-option 5 (RFC 3527). The DHCP relay
discovery packet is filled with the client's gateway IP address in sub-option 5 (discovery packet). The DHCP
server uses this information to offer an IP address from the right pool. Pool selection occurs by matching

DHCP | 62

the default gateway configuration settings on the DHCP server with the requested gateway IP address in
sub-option 5 in the discovery packet.

The switch uses DHCP relay sub-option 151 to enable DHCP relay to forward discovery and reply packets
between VXLAN DHCP clients and DHCP servers even when they are on different overlay or underlay VRFs
and the DHCP-server is reachable on the default VRF or one of the overlay VRFs.

In general deployments, a renewal of a DHCP client's IP occurs when the client sends a request to the DHCP
server directly. In the case of EVPN VXLAN clients, the DHCP server is not directly reachable. Instead, the
renewal request is sent to the DHCP relay. DHCP relay agent fills the option 82 sub-option 11 field in the
DHCP discovery packet with the client's gateway IP on the VTEP (which is the relay interface IP address of
the VTEP) and the DHCP server returns a DHCP offer reply packet with option 54 set to the DHCP server
Identifier. When the reply packet is received by the client, the client uses the IP in option 54 to sent
subsequent renewal requests to this IP (VTEP's Relay Interface IP) using sub-option 11 (also known as the
Server ID Override Sub-option). Refer to RFC 5107 for more details.

Sub-options 5,11,151,152 are filled in the discover packet, only if a source IP address is defined (using the
command ip source-address) for the given DHCP server's source VRF. If the server does not understand
sub-option 151, then the server will add sub-option 152 in offer packet.

In an inter-VRF situation, when both DHCP relay and DHCP snooping are enabled on the switch with option
82, DHCPv4 clients will not receive an IP address.

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

63

EnablestheDHCPv4relayagent.
n
Enablesinterface1/1/1andassignsanIPv4addresstoit.(Bydefault,allinterfacesarelayer3and
n
disabled.)
DefinesanIPhelperaddressof10.10.20.209ontheinterface.
n
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
Procedure
DHCP|64

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
| switch(config-if)# |     |           | ip        | helper-address          | 192.168.1.1 |     |
| switch(config-if)# |     |           | quit      |                         |             |     |
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
|     | 50                |           | 8              |                   | 50  | 8   |
| --- | ----------------- | --------- | -------------- | ----------------- | --- | --- |
|     | switch#           | show ip   | helper-address |                   |     |     |
|     | IP Helper         | Addresses |                |                   |     |     |
|     | Interface:        | 1/1/1     |                |                   |     |     |
|     | IP Helper         | Address   |                | VRF               |     |     |
|     | ----------------- |           |                | ----------------- |     |     |
|     | 192.168.1.1       |           |                | default           |     |     |
|     | Interface:        | 1/1/2     |                |                   |     |     |
|     | IP Helper         | Address   |                | VRF               |     |     |
|     | ----------------- |           |                | ----------------- |     |     |
|     | 192.168.1.1       |           |                | default           |     |     |
DHCPv4relayscenario2
Inthisscenario,thetwohostcomputerscommunicatewithtwodifferentDHCPservers.Eachserveris
reachedonadifferentVRF.Thephysicaltopologyofthenetworklookslikethis:
65
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

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
DHCP|66

Procedure
1. Onswitch1:
a. CreateLAG100andassignanIPaddresstoit.
switch# config
| switch(config)#        | interface |      | lag 100 |              |
| ---------------------- | --------- | ---- | ------- | ------------ |
| switch(config-lag-if)# |           | ip   | address | 10.0.10.1/24 |
| switch(config-lag-if)# |           | lacp | mode    | active       |
| switch(config-lag-if)# |           | exit |         |              |
switch(config)#
b. AssignanIPaddresstointerface1/1/1andaanIPhelperaddresstoreachtheDHCPserver.
| switch(config)#    | interface |                | 1/1/1      |         |
| ------------------ | --------- | -------------- | ---------- | ------- |
| switch(config-if)# | ip        | address        | 20.0.0.1/8 |         |
| switch(config-if)# | ip        | helper-address |            | 9.0.0.2 |
c. Assigninterfaces1/1/2and1/1/3toLAG100
| switch(config-if)# | interface |     | 1/1/2 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | interface |     | 1/1/3 |     |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | exit      |     |       |     |
switch(config)#
d. Createaroutebetween10.0.10.2and9.0.0.0.
| switch(config)# | ip route | 9.0.0.0/24 |     | 10.0.10.2 |
| --------------- | -------- | ---------- | --- | --------- |
2. Onswitch2:
a. CreateLAG100andassignanIPaddresstoit.
switch# config
| switch(config)#        | interface |      | lag 100 |              |
| ---------------------- | --------- | ---- | ------- | ------------ |
| switch(config-lag-if)# |           | ip   | address | 10.0.10.2/24 |
| switch(config-lag-if)# |           | lacp | mode    | active       |
| switch(config-lag-if)# |           | exit |         |              |
switch(config)#
b. Assigninterfaces1/1/1and1/1/2toLAG100
| switch(config-if)# | interface |     | 1/1/2 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | interface |     | 1/1/3 |     |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | exit      |     |       |     |
switch(config)#
c. AssignanIPaddresstointerface1/1/3.
| switch(config)#    | interface |         | 1/1/3      |     |
| ------------------ | --------- | ------- | ---------- | --- |
| switch(config-if)# | ip        | address | 9.0.0.1/24 |     |
d. Createaroutebetween20.0.0.0and10.0.10.1.
| switch(config)# | ip route | 20.0.0.0/8 |     | 10.0.10.1 |
| --------------- | -------- | ---------- | --- | --------- |
DHCPv4relaycommands
67
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

dhcp-relay
dhcp-relay
no dhcp-relay
Description
EnablesDHCPrelaysupport.DHCPrelayisenabledbydefault.DHCPrelayisnotsupportedonthe
managementinterface.
ThenoformofthiscommanddisablesDHCPrelaysupport.
Examples
ThisexampleenablesDHCPrelaysupport.
| switch(config)# | dhcp-relay |     |
| --------------- | ---------- | --- |
ThisexampleremovesDHCPrelaysupport.
| switch(config)# | no dhcp-relay |     |
| --------------- | ------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
| dhcp-relay hop-count-increment |                     |     |
| ------------------------------ | ------------------- | --- |
| dhcp-relay hop-count-increment |                     |     |
| no dhcp-relay                  | hop-count-increment |     |
Description
EnablestheDHCPrelayhopcountincrementfeature,whichcausestheDHCPrelayagenttoincrementthe
hopcountinallrelayedDHCPpackets.Hopcountisenabledbydefault.
Thenoformofthiscommanddisablesthehopcountincrementfeature.
Examples
Enablingthehopcountincrementfeature.
| switch(config)# | dhcp-relay | hop-count-increment |
| --------------- | ---------- | ------------------- |
Disablingthehopcountincrementfeature.
DHCP|68

| switch(config)# |     | no dhcp-relay | hop-count-increment |     |     |     |     |     |
| --------------- | --- | ------------- | ------------------- | --- | --- | --- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |     |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- | --- |
8360
| dhcp-relay    | l2vpn-clients |     |     |     |     |     |     |     |
| ------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| dhcp-relay    | l2vpn-clients |     |     |     |     |     |     |     |
| no dhcp-relay | l2vpn-clients |     |     |     |     |     |     |     |
Description
EnablesforwardingofpacketsfromL2VPNclients.Forwardingisenabledbydefault.
ThenoformofthiscommanddisablesforwardingofpacketsfromL2VPNclients.
Example
EnablingforwardingofpacketsfromL2VPNclients.
| switch(config)# |     | dhcp-relay    | l2vpn-clients |     |     |     |     |     |
| --------------- | --- | ------------- | ------------- | --- | --- | --- | --- | --- |
| switch(config)# |     | no dhcp-relay | l2vpn-clients |     |     |     |     |     |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |     |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- | --- |
8360
| dhcp-relay    | option | 82                 |            |     |          |            |              |        |
| ------------- | ------ | ------------------ | ---------- | --- | -------- | ---------- | ------------ | ------ |
| dhcp-relay    | option | 82 {replace        | [validate] |     | | drop   | [validate] | |            |        |
|               | keep   | | source-interface |            | |   | validate | [replace   | | drop]} [ip | | mac] |
| no dhcp-relay | option | 82 {replace        | [validate] |     | | drop   | [validate] | |            |        |
|               | keep   | | source-interface |            | |   | validate | [replace   | | drop]} [ip | | mac] |
69
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |

Description
ConfiguresthebehaviorofDHCPrelayoption82.ADHCPrelayagentcanreceiveamessagefromanother
DHCPrelayagenthavingoption82.Therelayinformationfromthepreviousrelayagentisreplacedby
default.
ThenoformofthiscommanddisablestheDHCPrelayoption82configurations.
| Parameter |     |     | Description                                          |
| --------- | --- | --- | ---------------------------------------------------- |
| replace   |     |     | Replacetheexistingoption82fieldinaninboundclientDHCP |
packetwiththeinformationfromtheswitch.TheremoteIDand
circuitIDinformationfromthefirstrelayagentislost.Default.
| validate |     |     | Validateoption82informationinDHCPserverresponsesand |
| -------- | --- | --- | --------------------------------------------------- |
dropinvalidresponses.
| drop |     |     | DropanyinboundclientDHCPpacketthatcontainsoption82 |
| ---- | --- | --- | -------------------------------------------------- |
information.
keep
Keeptheexistingoption82fieldinaninboundclientDHCPpacket.
TheremoteIDandcircuitIDinformationfromthefirstrelayagent
ispreserved.
source-interface ConfigurestheDHCPrelaytouseaconfiguredsourceIPaddress
forinter-VRFserverreachability.SetthesourceIPaddresswith
thecommandip source-interface.
| ip  |     |     | UsetheIPaddressoftheinterfaceonwhichtheclientDHCP |
| --- | --- | --- | ------------------------------------------------- |
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
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
ipbootp-gateway
DHCP|70

| ip bootp-gateway    | <IPV4-ADDR> |             |     |     |
| ------------------- | ----------- | ----------- | --- | --- |
| no ip bootp-gateway |             | <IPV4-ADDR> |     |     |
Description
ConfiguresagatewayaddressfortheDHCPrelayagenttouseforDHCPrequests.BydefaultDHCPrelay
agentpicksthelowest-numberedIPaddressontheinterface.
Thenoformofthiscommandremovesthegatewayaddress.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiestheIPaddressofthegatewayinIPv4format(x.x.x.x),
wherexisaisadecimalnumberfrom0to255.
Examples
SetstheIPaddressofthegatewayforinterface1/1/1to10.10.10.10.
| switch(config)#    |     | interface        | 1/1/1 |             |
| ------------------ | --- | ---------------- | ----- | ----------- |
| switch(config-if)# |     | ip bootp-gateway |       | 10.10.10.10 |
CommandHistory
| Release        |     |     |     | Modification |
| -------------- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |
| --------- | -------------- | --- | --- | --------- |
8320 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --------------- |
8360
iphelper-address
| ip helper-address    |     | <IPV4-ADDR> | [vrf | <VRF-NAME>] |
| -------------------- | --- | ----------- | ---- | ----------- |
| no ip helper-address |     | <IPV4-ADDR> | [vrf | <VRF-NAME>] |
Description
DefinestheaddressofaremoteDHCPserverorDHCPrelayagent.Uptoeightaddressescanbedefined.
TheDHCPagentforwardsDHCPclientrequeststoalldefinedservers.
ThiscommandrequiresthatyoudefineasourceIPaddressforDHCPrelaywiththecommand ip source-
interface.TheconfiguredsourceIPontheVRFisusedtoforwardDHCPpacketstotheserver.
AhelperaddresscannotbedefinedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
| Parameter      |             |     |     | Description |
| -------------- | ----------- | --- | --- | ----------- |
| helper-address | <IPV4-ADDR> |     |     |             |
SpecifiesthehelperIPaddressinIPv4format(x.x.x.x),wherex
71
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |
| --------------------------- | --- | ------------------- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
isadecimalnumberfrom0to255.
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |     |
| -------------- | --- | --- | --------------------------------------- | --- |
Examples
DefiningtheIPhelperaddress10.10.10.209oninterface1/1/1.
| switch(config)#    | interface         | 1/1/1 |              |     |
| ------------------ | ----------------- | ----- | ------------ | --- |
| switch(config-if)# | ip helper-address |       | 10.10.10.209 |     |
RemovingtheIPhelperaddress10.10.10.209oninterface1/1/1.
| switch(config-if)# | no ip | helper-address | 10.10.10.209 |     |
| ------------------ | ----- | -------------- | ------------ | --- |
DefiningtheIPhelperaddress10.10.10.209oninterface1/1/2onVRFmyvrf.
| switch(config)#    | interface         | 1/1/2 |              |           |
| ------------------ | ----------------- | ----- | ------------ | --------- |
| switch(config-if)# | ip helper-address |       | 10.10.10.209 | vrf myvrf |
RemovingtheIPhelperaddress10.10.10.209oninterface1/1/2onVRFmyvrf.
| switch(config-if)# | no ip | helper-address | 10.10.10.209 | vrf myvrf |
| ------------------ | ----- | -------------- | ------------ | --------- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 config-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8360
showdhcp-relay
| show dhcp-relay | [vsx-peer] |     |     |     |
| --------------- | ---------- | --- | --- | --- |
Description
ShowsDHCPrelayconfigurationsettings.
DHCP|72

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
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
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325           |               |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| -------------- | ------------- | --- | --- | ----------------------------------------------------- | --- |
| 8360           |               |     |     | commandfromtheoperatorcontext(>)only.                 |     |
| showdhcp-relay | bootp-gateway |     |     |                                                       |     |
show dhcp-relay bootp-gateway [interface <INTERFACE-NAME>] [vsx-peer]
Description
Showsthebootpgatewaydefinedforallinterfacesoraspecificinterface.
73
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-NAME>
Specifiesaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#              | show dhcp-relay | bootp-gateway   |           |       |
| -------------------- | --------------- | --------------- | --------- | ----- |
| BOOTP Gateway        | Entries         |                 |           |       |
| Interface            |                 | Source          | IP        |       |
| -------------------- |                 | --------------- |           |       |
| 1/1/1                |                 | 1.1.1.1         |           |       |
| 1/1/2                |                 | 1.1.1.2         |           |       |
| switch#              | show ip         | helper-address  | interface | 1/1/1 |
| BOOTP Gateway        | Entries         |                 |           |       |
| Interface            |                 | Source          | IP        |       |
| -------------------- |                 | --------------- |           |       |
| 1/1/1                |                 | 1.1.1.1         |           |       |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
| 8360 |     |     | commandfromtheoperatorcontext(>)only.                 |     |
showiphelper-address
| show ip helper-address |     | [interface | <INTERFACE-ID>] | [vsx-peer] |
| ---------------------- | --- | ---------- | --------------- | ---------- |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
| Parameter |                |     | Description |     |
| --------- | -------------- | --- | ----------- | --- |
| interface | <INTERFACE-ID> |     |             |     |
Specifiesaninterface.Format:member/slot/port.
DHCP|74

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#           | show ip helper-address |                   |           |       |
| ----------------- | ---------------------- | ----------------- | --------- | ----- |
| IP Helper         | Addresses              |                   |           |       |
| Interface:        | 1/1/1                  |                   |           |       |
| IP Helper         | Address                | VRF               |           |       |
| ----------------- |                        | ----------------- |           |       |
| 192.168.20.1      |                        | default           |           |       |
| 192.168.10.1      |                        | default           |           |       |
| Interface:        | 1/1/2                  |                   |           |       |
| IP Helper         | Address                | VRF               |           |       |
| ----------------- |                        | ----------------- |           |       |
| 192.168.30.1      |                        | RED               |           |       |
| switch#           | show ip helper-address |                   | interface | 1/1/1 |
| IP Helper         | Addresses              |                   |           |       |
| Interface:        | 1/1/1                  |                   |           |       |
| IP Helper         | Address                | VRF               |           |       |
| ----------------- |                        | ----------------- |           |       |
| 192.168.20.1      |                        | default           |           |       |
| 192.168.10.1      |                        | default           |           |       |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
8325
| 8360            |              |     | commandfromtheoperatorcontext(>)only. |     |
| --------------- | ------------ | --- | ------------------------------------- | --- |
| DHCPv6 relay    | agent        |     |                                       |     |
| SupportingVXLAN | topologiesor |     | inter-VRFdeployment                   |     |
WhendeployingEVPNVXLANorinter-VRFtopologieswherethesourceVRFsfortheDHCPandDHCPclient
aredifferent,itisrecommendedthatyouinstalltheDHCPv6serverintheunderlaysothatthereisonlyone
instanceoftheDHCPv6serverservingoverlayclients.
| Configuringthe | DHCPv6relayagent |     |     |     |
| -------------- | ---------------- | --- | --- | --- |
75
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

Prerequisites
Anenabledlayer3interface.
n
Procedure
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
n Enablesinterface1/1/2andassignsanIPv6addresstoit.(Bydefault,allinterfacesarelayer3and
disabled.)
n DefinesanIPhelperaddressofFF01::1:1000oninterface1/1/2.
n EnablesDHCPoption79.
| switch(config)#    | dhcpv6-relay |       |     |
| ------------------ | ------------ | ----- | --- |
| switch(config)#    | interface    | 1/1/2 |     |
| switch(config-if)# | no shutdown  |       |     |
switch(config-if)#
|                    | ipv6              | address 2001:0db8:85a3::8a2e:0370:7334/24 |              |
| ------------------ | ----------------- | ----------------------------------------- | ------------ |
| switch(config-if)# | ip helper-address |                                           | FF01::1:1000 |
| switch(config-if)# | exit              |                                           |              |
| switch(config)#    | dhcpv6-relay      | option                                    | 79           |
DHCPv6relayscenario1
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
DHCP|76

Procedure
1. EnableDHCPrelay.
| switch# config |     |     |     |     |
| -------------- | --- | --- | --- | --- |
switch(config)#
dhcpv6-relay
2. DefineanIPv6helperaddressoninterfaces1/1/1and1/1/2.
| switch(config)#    | interface | 1/1/1               |         |     |
| ------------------ | --------- | ------------------- | ------- | --- |
| switch(config-if)# | ipv6      | address 2002::22/64 |         |     |
| switch(config-if)# | ipv6      | helper-address      | 2001::1 |     |
switch(config-if)#
|                    | interface | 1/1/2               |         |     |
| ------------------ | --------- | ------------------- | ------- | --- |
| switch(config-if)# | ipv6      | address 2002::21/64 |         |     |
| switch(config-if)# | ipv6      | helper-address      | 2001::1 |     |
| switch(config-if)# | quit      |                     |         |     |
3. VerifyDHCPrelayconfiguration.
switch#
show dhcpv6-relay
| DHCPv6 Relay                                   | Agent :             | Enabled  |     |             |
| ---------------------------------------------- | ------------------- | -------- | --- | ----------- |
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
Inthisscenario,thetwohostcomputerscommunicatewithtwodifferentDHCPservers.Eachserveris
reachedonadifferentVRF.Thephysicaltopologyofthenetworklookslikethis:
77
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

Procedure
1. CreatethetwoVRFs.
switch# config
| switch(config)# | vrf vrf 1 |     |     |
| --------------- | --------- | --- | --- |
| switch(config)# | vrf vrf 2 |     |     |
2. Configureinterface1/1/1.SetitsIPaddress,associateitwithVRF1,anddefinethehelperIPaddress
toreachDHCPserver1.
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
5. Configureinterface1/1/4.SetitsIPaddress,associateitwithVRF2,anddefinethehelperIPaddress
toreachDHCPserver2.
| switch(configif)#        | interface           | 1/1/4       |                 |
| ------------------------ | ------------------- | ----------- | --------------- |
| switch(configif)#        | vrf attach          | vrf2        |                 |
| switch(configif)#        | ipv6 address        | 4040::1/120 |                 |
| switch(configif)#        | ipv6 helper-address |             | unicast 3030::2 |
| DHCPrelay(IPv6) commands |                     |             |                 |
dhcpv6-relay
dhcpv6-relay
no dhcpv6-relay
DHCP|78

Description
EnablesDHCPv6relaysupport.DHCPv6relayisdisabledbydefault.
DHCPrelayisnotsupportedonthemanagementinterface
ThenoformofthiscommanddisablesDHCPrelaysupport.
Examples
EnablesDHCPv6relaysupport.
| switch(config)# | dhcpv6-relay |     |
| --------------- | ------------ | --- |
RemovesDHCPv6relaysupport.
| switch(config)# | no dhcpv6-relay |     |
| --------------- | --------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | forthiscommand. |
| ---- | --- | --------------- |
8360
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
| switch(config)# | no dhcpv6-relay | option 79 |
| --------------- | --------------- | --------- |
CommandHistory
79
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

8320
8325
8360

config

Administrators or local user group members with execution rights
for this command.

ipv6 helper-address

ipv6 helper-address unicast <UNICAST-IPV6-ADDR>
no ipv6 helper-address unicast <UNICAST-IPV6-ADDR>
ipv6 helper-address multicast {all-dhcp-servers | <MULTICAST-IPV6-ADDR>} egress <PORT-NUM>
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

DHCP | 80

switch(config-if)# no ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress
1/1/2
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
showdhcpv6-relay
| show dhcpv6-relay | [vsx-peer] |     |
| ----------------- | ---------- | --- |
Description
ShowsDHCPrelayconfigurationsettings.
| Parameter |     | Description |
| --------- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch# | show dhcpv6-relay     |     |
| ------- | --------------------- | --- |
| DHCPv6  | Relay Agent : Enabled |     |
| Option  | 79 : Enabled          |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | ----------------------------------------------------- |
| 8360 |     | commandfromtheoperatorcontext(>)only.                 |
81
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| showipv6  | helper-address |            |                 |            |
| --------- | -------------- | ---------- | --------------- | ---------- |
| show ipv6 | helper-address | [interface | <INTERFACE-ID>] | [vsx-peer] |
Description
ShowsthehelperIPaddressesdefinedforallinterfacesoraspecificinterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
interface <INTERFACE-ID> Specifiesaninterface.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
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
| ---------------------------------------------- |                |                |           | ----------- |
| 2001:db8:0:1::                                 |                |                |           | -           |
| FF01::1:1000                                   |                |                |           | 1/1/2       |
| switch#                                        | show ipv6      | helper-address | interface | 1/1/1       |
| Interface:                                     | 1/1/1          |                |           |             |
| IPv6                                           | Helper Address |                |           | Egress Port |
| ---------------------------------------------- |                |                |           | ----------- |
| 2001:db8:0:1::                                 |                |                |           | -           |
| FF01::1:1000                                   |                |                |           | 1/1/2       |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
DHCP|82

Platforms

Command context

Authority

8320
8325
8360

Manager (#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

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
configurations. For more information on VSX support, see the Virtual Switching Extension (VSX) Guide.

DHCP relay interoperation

Both DHCP relay and DHCP server can be configured on the same VRF.

DHCP snooping interoperation

DHCP snooping may not be configured with DHCP server.

Configuring a DHCPv4 server on a VRF

Prerequisites

n An enabled layer 3 interface.

n A VRF.

n An external TFTP server to host BOOTP image files (optional).

n An external storage device installed and configured (optional).

Procedure

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

83

1. AssigntheDHCPv4servertoaVRFwiththecommanddhcp-server vrf.Thisswitchestothe
DHCPv4serverconfigurationcontext.
2. IfyouwanttheDHCPv4servertobethesoleauthorityforIPaddressesontheVRF,enable
authoritativemodewiththecommandauthoritative.
3. DefineanaddresspoolfortheVRFwiththecommandpool.ThisswitchestotheDHCPv4serverpool
context.Customizepoolsettingsasfollows:
| a. Definetherangeofaddressesinthepoolwiththecommandrange.    |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- |
| b. Settheleasetimeforaddressesinthepoolwiththecommandlease.  |     |     |     |     |
| c. Setthedomainnameforthepoolwiththecommanddomain-name.      |     |     |     |     |
| d. Defineuptofourdefaultrouterswiththecommanddefault-router. |     |     |     |     |
| e. DefineuptofourDNSserverswiththecommanddns-server.         |     |     |     |     |
f. Createstaticbindingsforspecificaddressesinthepoolwiththecommandstatic-bind.
g. ConfigurecustomDHCPv4optionsforthepoolwiththecommandoption.
h. ConfigureNetBIOSsupportwiththecommandsnetbios-name-serverandnetbios-node-type.
| i. ConfigureBOOTPoptionswiththecommandbootp.         |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- |
| j. ExittheDHCPv4serverpoolcontextwiththecommandexit. |     |     |     |     |
4. EnabletheDHCPserverontheVRFwiththecommandenable.
5. ConfiguresupportforpersistentexternalstorageofDHCPsettingswiththecommanddhcp-server
external-storage.
6. ViewDHCPv4serverconfigurationsettingswiththecommandshow dhcp-server all-vrfs.
Example
Thisexamplecreatesthefollowingconfiguration:
n ConfigurestheDHCPv4serveronVRFprimary-vrf.
n Enablesauthoritativemode.
Definesthepoolprimary-poolwiththefollowingsettings:
n
Addressrange:10.0.0.1to10.0.0.100.
o
o Leasetime:12hours.
o Domainname:example.org.in.
Defaultrouters:10.30.30.1and10.30.30.2.
o
o DNSservers:125.0.0.1and125.0.0.2.
o Staticbindingof10.0.0.11forMACaddress24:be:05:24:75:73.
o DHCPcustomoption3withIPaddress10.30.30.3.
EnablestheDHCPv4server.
n
| switch(config)#                  | dhcp-server | vrf primary       |                |     |
| -------------------------------- | ----------- | ----------------- | -------------- | --- |
| switch(config-dhcp-server)#      |             | pool primary-pool |                |     |
| switch(config-dhcp-server-pool)# |             | range 10.0.0.1    | 10.0.0.100     |     |
| switch(config-dhcp-server-pool)# |             | lease 12:00:00    |                |     |
| switch(config-dhcp-server-pool)# |             | domain-name       | example.org.in |     |
switch(config-dhcp-server-pool)# default-router ip 10.30.30.1 10.30.30.2
| switch(config-dhcp-server-pool)# |     | dns-server | 125.0.0.1 | 125.0.0.2 |
| -------------------------------- | --- | ---------- | --------- | --------- |
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.11 mac 24:be:05:24:75:73
| switch(config-dhcp-server-pool)# |            | option    | 3 ip 10.30.30.3 |     |
| -------------------------------- | ---------- | --------- | --------------- | --- |
| switch(config-dhcp-server-pool)# |            | exit      |                 |     |
| switch(config-dhcp-server)#      |            | enable    |                 |     |
| Configuring                      | the DHCPv6 | server on | a VRF           |     |
DHCP|84

Prerequisites

n An enabled layer 3 interface.

n A VRF.

n An external storage device installed and configured (optional).

Procedure

1. Assign the DHCPv6 server to a VRF with the command dhcpv6-server vrf. This switches to the

DHCPv6 server configuration context.

2.

If you want the DHCP server to be the sole authority for IP addresses on the VRF, enable
authoritative mode with the command authoritative.

3. Define an address pool for the VRF with the command pool. This switches to the DHCPv6 server pool

context. Customize pool settings as follows:
a. Define the range of addresses in the pool with the command range.
b. Set the DHCP lease time for addresses in the pool with the command lease.
c. Define up to four DNS servers with the command dns-server.
d. Create static bindings for specific addresses in the pool with the command static-bind.
e. Configure custom DHCP options for the pool with the command option.
f. Exit the DHCP server pool context with the command exit.

4. Enable the DHCPv6 server on the VRF with the command enable.

5. Configure support for persistent external storage of DHCP settings with the command dhcv6p-

server external-storage.

6. View DHCPv6 server configuration settings with the command show dhcpv6-server all-vrfs.

Example

This example creates the following configuration:

n Configures a DHCPv6 server on VRF primary-vrf.

n Enables authoritative mode.

n Defines the pool primary-pool with the following settings:

o Address range: 2001::1 to 2001::100.

o Lease time: 12 hours.

o DNS servers: 2101::14 and 2101::14.

o Static binding of 2001::101 for client ID 1:0:a0:24:ab:fb:9c.

o DHCP custom option: 22 with IP address 2101::15.

n Enables the DHCPv6 server.

switch(config)# dhcpv6-server vrf primary
switch(config-dhcpv6-server)# pool primary-pool
switch(config-dhcpv6-server-pool)# range 2001::1 2001::100 prefix-len 64
switch(config-dhcpv6-server-pool)# lease 12:00:00
switch(config-dhcpv6-server-pool)# dns-server 2101::13 2101::14
switch(config-dhcpv6-server-pool)# static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c
switch(config-dhcpv6-server-pool)# option 22 ipv6 2101::15
switch(config-dhcpv6-server-pool)# exit
switch(config-dhcpv6-server)# enable

DHCP server IPv4 commands

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

85

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
switch(config)#
|                             | dhcp-server | vrf primary   |
| --------------------------- | ----------- | ------------- |
| switch(config-dhcp-server)# |             | authoritative |
RemovestheDHCPv4serverauthoritativemodeonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary      |
| --------------------------- | ----------- | ---------------- |
| switch(config-dhcp-server)# |             | no authoritative |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | forthiscommand. |
| ---- | --- | --------------- |
8360
bootp
bootp <REMOTE-URL>
no bootp <REMOTE-URL>
Description
SetstheBOOTPoptionsthatarereturnedbytheDHCPv4serverforthecurrentpool.BOOTPprovidesa
waytodistributeanIPaddressandbootimagefiletoclientstations.TheDHCPv4serverreturnstheIP
addressandthelocationofthebootimagefile,whichmustbestoredonanexternalTFTPserver.
ThenoformofthiscommanddisablessupportforBOOTP.
DHCP|86

| Parameter |     | Description |
| --------- | --- | ----------- |
<REMOTE-URL> SpecifiesthenameandlocationofaBOOTPfileonaTFTPserver
intheformat:
tftp://{<IP> | <HOST>}/<FILE>
<IP>:SpecifiestheIPaddressoftheTFTPserverhostingthe
n
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
| switch(config)#             | dhcp-server | vrf primary       |
| --------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)# |             | pool primary-pool |
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
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
| clear dhcp-server | leases |     |
| ----------------- | ------ | --- |
clear dhcp-server leases [all-vrfs | <IPV4-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv4serverleaseinformation.TheDHCPv4servermustbedisabledbeforeclearinglease
information.
87
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Parameter |     |     | Description             |     |
| --------- | --- | --- | ----------------------- | --- |
| all-vrfs  |     |     | ClearsleasesforallVRFs. |     |
<IPV4-ADDR> vrf <VRF-NAME> ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| vrf <VRF-NAME> |     |     | ClearsleasesforaspecificVRF. |     |
| -------------- | --- | --- | ---------------------------- | --- |
Examples
ClearingallDHCPv4serverleases.
| switch(config)#             | dhcp-server       | vrf     | primary |     |
| --------------------------- | ----------------- | ------- | ------- | --- |
| switch(config-dhcp-server)# |                   | disable |         |     |
| switch(config-dhcp-server)# |                   | exit    |         |     |
| switch(config)#             | exit              |         |         |     |
| switch#                     | clear dhcp-server | leases  |         |     |
ClearingallDHCPv4serverleasesforVRFprimary-vrf.
| switch(config)#             | dhcp-server       | vrf     | primary         |     |
| --------------------------- | ----------------- | ------- | --------------- | --- |
| switch(config-dhcp-server)# |                   | disable |                 |     |
| switch(config-dhcp-server)# |                   | exit    |                 |     |
| switch(config)#             | exit              |         |                 |     |
| switch#                     | clear dhcp-server | leases  | vrf primary-vrf |     |
CleartheDHCPv4serverleaseforIPaddress10.10.10.1onVRFprimary-vrf.
| switch(config)#             | dhcp-server       | vrf     | primary    |                 |
| --------------------------- | ----------------- | ------- | ---------- | --------------- |
| switch(config-dhcp-server)# |                   | disable |            |                 |
| switch(config-dhcp-server)# |                   | exit    |            |                 |
| switch(config)#             | exit              |         |            |                 |
| switch#                     | clear dhcp-server | leases  | 10.10.10.1 | vrf primary-vrf |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
8360
default-router
DHCP|88

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
| switch(config)# | dhcp-server | vrf primary |     |
| --------------- | ----------- | ----------- | --- |
switch(config-dhcp-server)#
pool primary-pool
| switch(config-dhcp-server-pool)# |     | no default-router | ip 10.0.0.1 |
| -------------------------------- | --- | ----------------- | ----------- |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
| dhcp-server | external-storage |     |     |
| ----------- | ---------------- | --- | --- |
dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcp-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
Description
ConfigurestheexternalstoragefilelocationforDHCPv4serverleaseinformation.Thisfileprovides
persistentstorage,enablingDHCPv4serversettingstoberestoredwhentheswitchisrestarted.Lease
informationisstoredinaflatfileontheconfiguredexternaldevice.
89
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

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

Platforms

Command context

Authority

8320
8325
8360

config

Administrators or local user group members with execution rights
for this command.

dhcp-server vrf

dhcp-server vrf VRF-NAME
no dhcp-server vrf VRF-NAME

Description

Configures the DHCPv4 server to support a VRF and changes to the config-dhcp-server context for that
VRF.

The no form of this command removes DHCPv4 server support on a VRF.

DHCP | 90

| Parameter |     | Description |
| --------- | --- | ----------- |
| VRF-NAME  |     | NameofaVRF. |
Example
ConfiguresDHCPv4serversupportonVRFprimary.
| switch(config)# | dhcp-server | vrf primary |
| --------------- | ----------- | ----------- |
RemovesDHCPv4serversupportonVRFprimary.
| switch(config)# | no dhcp-server | vrf primary |
| --------------- | -------------- | ----------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | forthiscommand. |
| ---- | --- | --------------- |
8360
disable
disable
Description
DisablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
DisablestheDHCPv4serveronVRFprimary.
| switch(config)#             | dhcp-server | vrf primary |
| --------------------------- | ----------- | ----------- |
| switch(config-dhcp-server)# |             | disable     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
91
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |     |
| ---- | --- | --- | --------------- | --- |
8360
dns-server
| dns-server <IPV4-ADDR-LIST> |                  |     |     |     |
| --------------------------- | ---------------- | --- | --- | --- |
| no dns-server               | <IPV4-ADDR-LIST> |     |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesoftheDNSserversinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.Separate
addresseswithaspace.
Example
DefinestwoDNSserversfortheserverpoolprimary-poolonVRFprimary.
| switch(config)# | dhcp-server | vrf primary |     |     |
| --------------- | ----------- | ----------- | --- | --- |
switch(config-dhcp-server)#
pool primary-pool
| switch(config-dhcp-server-pool)# |     |     | dns-server | 10.0.20.1 |
| -------------------------------- | --- | --- | ---------- | --------- |
DeletesaDNSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary |               |           |
| -------------------------------- | ----------- | ----------- | ------------- | --------- |
| switch(config-dhcp-server)#      |             | pool        | primary-pool  |           |
| switch(config-dhcp-server-pool)# |             |             | no dns-server | 10.0.20.1 |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
8360
domain-name
| domain-name    | <DOMAIN-NAME> |     |     |     |
| -------------- | ------------- | --- | --- | --- |
| no domain-name | <DOMAIN-NAME> |     |     |     |
DHCP|92

Description
DefinesadomainnameforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddomainnamefromthepool.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<DOMAIN-NAME> Specifiesadomainname.Range:1to255printableASCII
characters.
Example
Definesadomainnamefortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)#
|     |     | domain-name | example.org.in |
| --- | --- | ----------- | -------------- |
Deletesadomainnamefromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |                |
| -------------------------------- | ----------- | ----------------- | -------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |                |
| switch(config-dhcp-server-pool)# |             | no domain-name    | example.org.in |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
8325 rightsforthiscommand.
8360
enable
enable
Description
EnablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
EnablestheDHCPv4serveronVRFprimary.
switch(config)#
|                             | dhcp-server | vrf primary |     |
| --------------------------- | ----------- | ----------- | --- |
| switch(config-dhcp-server)# |             | enable      |     |
93
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
http-proxy
| http-proxy    | {<FQDN | IPV4-ADDR>} | [vrf | <VRF-NAME>]      |
| ------------- | -------------------- | ---- | ---------------- |
| no http-proxy | [<FQDN | IPV4-ADDR>] |      | [vrf <VRF-NAME>] |
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
DHCP optionsreceivedviamanagement/OOBMport.
o
o DHCPoptionsreceivedviaVLAN1onsupportedswitchplatforms.
OperationalconfigurationforHTTPproxylocationisdeterminedbythesourcewiththehighestpriority.
nn
Sourcepriority:
| 1.  | Userconfigured.                             |     |     |
| --- | ------------------------------------------- | --- | --- |
| 2.  | DHCPoptionsreceivedviamanagement/OOBM port. |     |     |
| 3.  | DHCP optionsreceivedviaVLAN1.               |     |     |
DHCP|94

HTTPproxylocationcanonlybeaFQDNoranIPV4address.
n
n WhenHTTPproxylocationandVRFareconfigured,theyoverrideanyexistingHTTPproxylocationandVRF.
n IfthiscommandisexecutedwithouttheVRFparameter,thedefaultVRFwillbeused.
n PortnumbermayneedtobespecifiedattheendoftheIPaddressforFQDNtoconnectviaHTTPproxy.
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
SetsthelengthoftheDHCPv4leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv4clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv4leasetimetoitsdefaultvalue1hour.
| Parameter |     | Description                                     |     |
| --------- | --- | ----------------------------------------------- | --- |
| <TIME>    |     | SetstheDHCPv4leasetime.Format:DD:HH:MM.Default: |     |
01:00:00.
infinite SetstheDHCPv4leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
95
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Example
SetstheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimaryto12hours.
switch(config)#
|                                  | dhcp-server | vrf primary       |
| -------------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |
| switch(config-dhcp-server-pool)# |             | lease 00:12:00    |
DeletestheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |
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
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
8325 rightsforthiscommand.
8360
netbios-name-server
| netbios-name-server | <IPV4-ADDR-LIST> |     |
| ------------------- | ---------------- | --- |
no netbios-name-server <IPV4-ADDR-LIST>
Description
DefinesuptofourNetBIOSWINSserversforthecurrentDHCPv4serverpool.WINSisusedbyMicrosoft
DHCPclientstomatchhostnameswithIPaddresses.
ThenoformofthiscommandremovesthespecifiedWINSserversfromthepool.
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
DHCP|96

DeletesaWINSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# no netbios-name-server ip 10.0.20.1
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
8325 rightsforthiscommand.
8360
netbios-node-type
| netbios-node-type    | <TYPE> |     |     |
| -------------------- | ------ | --- | --- |
| no netbios-node-type | <TYPE> |     |     |
Description
DefinestheNetBIOSnodetypeforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovestheNetBIOSnodetypeforthecurrentpool.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<TYPE>
SpecifiestheNetBIOSnodetype:broadcast,hybrid,mixed,or
peer-to-peer.
Examples
DefinestheNetBIOSnodetypebroadcastfortheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary       |           |
| -------------------------------- | ----------- | ----------------- | --------- |
| switch(config-dhcp-server)#      |             | pool primary-pool |           |
| switch(config-dhcp-server-pool)# |             | netbios-node-type | broadcast |
DeletestheNetBIOSnodetypebroadcastfromtheDHCPv4serverpoolprimary-poolonVRFprimary.
switch(config)#
|                                  | dhcp-server | vrf primary          |           |
| -------------------------------- | ----------- | -------------------- | --------- |
| switch(config-dhcp-server)#      |             | pool primary-pool    |           |
| switch(config-dhcp-server-pool)# |             | no netbios-node-type | broadcast |
CommandHistory
97
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
8360
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
Description
DefinescustomDHCPv4optionsforthecurrentDHCPv4serverpool.DHCPv4optionsenabletheDHCPv4
servertoprovideadditionalinformationaboutthenetworkwhenDHCPv4clientsrequestanaddress.
ThenoformofthiscommandremovescustomDHCPv4optionsfromthepool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<OPTION-NUM> SpecifiesaDHCPv4optionnumber.ForalistofDHCPv4option
numbers,seehttps://www.iana.org/assignments/bootp-dhcp-
parameters/bootp-dhcp-parameters.xhtml.Range:2to254.
ascii <ASCII-STR> SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:
1to255ASCIIcharacters.
hex <HEX-STR>
Specifiesavaluefortheselectedoptionasahexadecimalstring.
Range:1to255hexadecimalcharacters.
ip <IPV4-ADDR-LIST> SpecifiesalistofIPaddressesinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary |              |                |
| -------------------------------- | ----------- | ----------- | ------------ | -------------- |
| switch(config-dhcp-server)#      |             | pool        | primary-pool |                |
| switch(config-dhcp-server-pool)# |             |             | option 3     | ip 192.168.1.1 |
DeletesDHCPv4option3fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf primary |              |                  |
| -------------------------------- | ----------- | ----------- | ------------ | ---------------- |
| switch(config-dhcp-server)#      |             | pool        | primary-pool |                  |
| switch(config-dhcp-server-pool)# |             |             | no option    | 3 ip 192.168.1.1 |
CommandHistory
DHCP|98

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
8325 rightsforthiscommand.
8360
pool
pool <POOL-NAME>
no pool <POOL-NAME>
Description
CreatesaDHCPv4serverpoolforthecurrentVRFandswitchestotheconfig-dhcp-server-poolcontext
forit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64pools(IPv4and
IPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv4serverpool.
| Parameter |     | Description |
| --------- | --- | ----------- |
<POOL-NAME> SpecifiestheDHCPv4poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |
| --------------------------- | ----------- | ----------------- |
| switch(config-dhcp-server)# |             | pool primary-pool |
switch(config-dhcp-server-pool)#
DeletestheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary          |
| --------------------------- | ----------- | -------------------- |
| switch(config-dhcp-server)# |             | no pool primary-pool |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
99
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
8320 config-dhcp-server Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     |     | forthiscommand. |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- |
8360
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
<HIGH-IPV4-ADDR>
SpecifiesthehighestIPaddressinthepoolinIPv4format
(x.x.x.x),wherexisadecimalnumberfrom0to255.
| prefix-len | <MASK> |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- |
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
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
Examples
Definestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfortheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)#             |     | dhcp-server | vrf  | primary      |     |     |     |
| --------------------------- | --- | ----------- | ---- | ------------ | --- | --- | --- |
| switch(config-dhcp-server)# |     |             | pool | primary-pool |     |     |     |
switch(config-dhcp-server-pool)# 192.168.1.1 192.168.1.100 prefix-len 24
Deletestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfromtheDHCPv4server
poolprimary-poolonVRFprimary.
DHCP|100

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
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
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
pool <POOL-NAME> [vrf <VRF-NAME>] ShowsDHCPv4serverpoolconfigurationsettingsforallVRFsora
specificVRF.
Examples
ShowingallDHCPv4serverconfigurationsettings.
| switch#        | show dhcp-server    |     |     |
| -------------- | ------------------- | --- | --- |
| VRF Name       | : default           |     |     |
| DHCP Server    | : enabled           |     |     |
| Operational    | State : operational |     |     |
| Authoritative  | Mode : false        |     |     |
| Pool Name      | : test              |     |     |
| Lease Duration | : 00:01:00          |     |     |
| DHCP dynamic   | IP allocation       |     |     |
--------------------------
101
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

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
| Option-Number |        | Option-Type |            | Option-Value |          |                   |
| ------------- | ------ | ----------- | ---------- | ------------ | -------- | ----------------- |
| ------------- |        | ----------- |            | ------------ |          |                   |
| 6             |        | ip          |            | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 10.0.0.6 |
| 18            |        | ascii       |            | aswed        |          |                   |
| DHCP Server   | static | IP          | allocation |              |          |                   |
--------------------------------
| IP-Address | Client-Hostname |     |     | MAC-Address       |     |     |
| ---------- | --------------- | --- | --- | ----------------- | --- | --- |
| ---------- | --------------- |     |     | ----------------- |     |     |
| 10.0.0.1   |                 | *   |     | aa:bb:cc:11:12:a4 |     |     |
| 20.0.0.1   |                 | *   |     | 11:22:11:22:aa:dd |     |     |
DHCP|102

| BOOTP | Options |     |     |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- |
---------------
| Boot-File-Name |     | TFTP-Server-Name |     | State       |     | TFTP-Server-Address   |
| -------------- | --- | ---------------- | --- | ----------- | --- | --------------------- |
| -------------- |     | ---------------- |     | ------      |     | --------------------- |
| boot.txt       |     | *                |     | OPERATIONAL |     | 10.0.0.10             |
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
| 8360 |     |     |     | commandfromtheoperatorcontext(>)only.                 |     |     |
static-bind
| static-bind    | ip <IPV4-ADDR>   |     | mac <MAC-ADDR> | [hostname | <HOST>] |     |
| -------------- | ---------------- | --- | -------------- | --------- | ------- | --- |
| no static-bind | <IPV4-ADDR-LIST> |     |                |           |         |     |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaspecificMACaddress.This
causestheDHCPv4servertoonlyassignthespecifiedIPaddresstoaclientstationwiththespecifiedMAC
address.
Thenoformofthiscommandremovesthespecifiedbinding.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.TheIPaddressmustbewithinthe
addressrangedefinedforthecurrentpool.
mac <MAC-ADDR>
SpecifiesaclientstationMACaddress(xx:xx:xx:xx:xx:xx),
wherexisahexadecimalnumberfrom0toF.
hostname <HOST> Specifiesthehostnameoftheclientstation.Range:1to255
printableASCIIcharacters
Examples
Definesastaticaddressfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             |     | dhcp-server | vrf  | primary      |     |     |
| --------------------------- | --- | ----------- | ---- | ------------ | --- | --- |
| switch(config-dhcp-server)# |     |             | pool | primary-pool |     |     |
switch(config-dhcp-server-pool)# static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
Deletesastaticaddressfromtheserverpoolprimary-poolonVRFprimary.
103
| AOS-CX10.08IPServicesGuide| |     | (83xx | SwitchSeries) |     |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- | --- |

| switch(config)# | dhcp-server | vrf primary |
| --------------- | ----------- | ----------- |
switch(config-dhcp-server)#
pool primary-pool
switch(config-dhcp-server-pool)# no static-bind ip 10.0.0.1 mac 24:be:05:24:75:73
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config-dhcp-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
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
| switch(config)#               | dhcpv6-server | vrf primary      |
| ----------------------------- | ------------- | ---------------- |
| switch(config-dhcpv6-server)# |               | no authoritative |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
DHCP|104

CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
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
| switch(config)#               | dhcpv6-server       | vrf     | primary |
| ----------------------------- | ------------------- | ------- | ------- |
| switch(config-dhcpv6-server)# |                     | disable |         |
| switch(config-dhcpv6-server)# |                     | exit    |         |
| switch(config)#               | exit                |         |         |
| switch#                       | clear dhcpv6-server | leases  |         |
ClearingallDHCPv6serverleasesforVRFprimary-vrf.
| switch(config)#               | dhcpv6-server       | vrf     | primary         |
| ----------------------------- | ------------------- | ------- | --------------- |
| switch(config-dhcpv6-server)# |                     | disable |                 |
| switch(config-dhcpv6-server)# |                     | exit    |                 |
| switch(config)#               | exit                |         |                 |
| switch#                       | clear dhcpv6-server | leases  | vrf primary-vrf |
CleartheDHCPv6serverleaseforIPaddress2001::1onVRFprimary-vrf.
| switch(config)#               | dhcpv6-server | vrf     | primary |
| ----------------------------- | ------------- | ------- | ------- |
| switch(config-dhcpv6-server)# |               | disable |         |
105
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| switch(config-dhcpv6-server)# |     | exit |     |
| ----------------------------- | --- | ---- | --- |
switch(config)#
exit
| switch# | clear dhcpv6-server | leases 2001::1 | vrf primary-vrf |
| ------- | ------------------- | -------------- | --------------- |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
8325
| 8360          |                  | commandfromtheoperatorcontext(>)only. |     |
| ------------- | ---------------- | ------------------------------------- | --- |
| dhcv6p-server | external-storage |                                       |     |
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
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
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
DHCP|106

switch(config)# no dhcpv6-server external-storage Storage1 file LeaseFile delay 600
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | forthiscommand. |
| ---- | --- | --------------- |
8360
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
| switch(config)# | no dhcpv6-server | vrf primary |
| --------------- | ---------------- | ----------- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
107
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | forthiscommand. |
| ---- | --- | --------------- |
8360
disable
disable
Description
DisablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
DisablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcpv6-server | vrf primary |
| ----------------------------- | ------------- | ----------- |
| switch(config-dhcpv6-server)# |               | disable     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | forthiscommand. |
| ---- | --- | --------------- |
8360
dns-server
| dns-server <IPVv6-ADDR-LIST> |                   |     |
| ---------------------------- | ----------------- | --- |
| no dns-server                | <IPVv6-ADDR-LIST> |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
| Parameter |     | Description |
| --------- | --- | ----------- |
<IPVv6-ADDR-LIST>
SpecifiestheIPaddressesoftheDNSserversinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDNSserver2001::13fortheserverpoolprimary-poolonVRFprimary.
DHCP|108

| switch(config)# | dhcpv6-server | vrf primary |     |     |
| --------------- | ------------- | ----------- | --- | --- |
switch(config-dhcpv6-server)#
pool primary-pool
| switch(config-dhcpv6-server-pool)# |     |     | dns-server | 2001::13 |
| ---------------------------------- | --- | --- | ---------- | -------- |
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
8320 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --------------------- | --- |
8360
enable
enable
Description
EnablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhenconfigured
onaVRF.
Example
EnablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcp-server | vrf primary |     |     |
| ----------------------------- | ----------- | ----------- | --- | --- |
| switch(config-dhcpv6-server)# |             | enable      |     |     |
CommandHistory
| Release        |     | Modification |     |     |
| -------------- | --- | ------------ | --- | --- |
| 10.07orearlier |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecutionrights
109
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| Platforms | Commandcontext | Authority       |
| --------- | -------------- | --------------- |
| 8325      |                | forthiscommand. |
8360
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
infinite SetstheDHCPv6leasetimetoinfinite.Thismeansthataddresses
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
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config-dhcpv6-server-pool
8320 Administratorsorlocalusergroupmemberswithexecution
8325 rightsforthiscommand.
8360
option
DHCP|110

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
ip <IPV6-ADDR-LIST> SpecifiesalistofIPaddressesfortheoptioninIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Example
DefinesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server | vrf primary |              |
| ----------------------------- | ------------- | ----------- | ------------ |
| switch(config-dhcpv6-server)# |               | pool        | primary-pool |
switch(config-dhcpv6-server-pool)#
|     |     |     | option 22 ipv6 2001::12 |
| --- | --- | --- | ----------------------- |
DeletesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server | vrf primary |                            |
| ---------------------------------- | ------------- | ----------- | -------------------------- |
| switch(config-dhcpv6-server)#      |               | pool        | primary-pool               |
| switch(config-dhcpv6-server-pool)# |               |             | no option 22 ipv6 2001::12 |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
pool
pool <POOL-NAME>
no pool <POOL-NAME>
111
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Description
CreatesaDHCPv6serverpoolforthecurrentVRFandswitchestotheconfig-dhcpv6-server-poolcontext
forit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64pools(IPv4and
IPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
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
| switch(config)# |     | dhcpv6-server | vrf | primary |     |
| --------------- | --- | ------------- | --- | ------- | --- |
switch(config-dhcpv6-server)#
|     |     |     | no  | pool primary-pool |     |
| --- | --- | --- | --- | ----------------- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
8320 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
range
| range <LOW-IPV6-ADDR>    |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
| ------------------------ | --- | ---------------- | --- | ----------- | ------- |
| no range <LOW-IPV6-ADDR> |     | <HIGH-IPV6-ADDR> |     | [prefix-len | <MASK>] |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv6serverpool.Amaximumof64ranges
aresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
DHCP|112

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
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
| switch(config)#               | dhcpv6-server | vrf primary |              |
| ----------------------------- | ------------- | ----------- | ------------ |
| switch(config-dhcpv6-server)# |               | pool        | primary-pool |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::10 prefix-len 64
DeletesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server | vrf primary |              |
| ----------------------------- | ------------- | ----------- | ------------ |
| switch(config-dhcpv6-server)# |               | pool        | primary-pool |
switch(config-dhcpv6-server-pool)# no range 2001::1 2001::10 prefix-len 64
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |
| ---- | --- | --- | --------------------- |
8360
show dhcpv6-server
| show dhcpv6-server | [all-vrfs]       |       |             |
| ------------------ | ---------------- | ----- | ----------- |
| show dhcpv6-server | leases {all-vrfs | | vrf | <VRF-NAME>} |
| show dhcpv6-server | pool <POOL-NAME> | [vrf  | <VRF-NAME>] |
Description
ShowsconfigurationsettingsfortheDHCPv6server.
113
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

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
DHCP|114

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
| 8320      |                |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Manager(#)
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
| 8360 |     |     |     | commandfromtheoperatorcontext(>)only.                 |     |     |
static-bind
115
| AOS-CX10.08IPServicesGuide| |     | (83xx | SwitchSeries) |     |     |     |
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
8320 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
8325
8360
DHCP|116

Chapter 6

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

n Up to 127 tunnels can be defined on a switch shared between different tunnel types: GRE, IPv6 in IPv4,

and IPv6 in IPv6.

n A maximum of 16 source IP addresses are supported. Tunnels can have the same source IP address and
different destination IP addresses. The source IP, destination IP, and VRF combine to uniquely identify a
tunnel.

Unsupported features

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

117

GREIPv4overIPv6.
n
QoScannotbeappliedtoaGREtunnelinterface.
n
Keysupportcanbeaddedforsecurityandidentificationpurposeswhentherearemultipleapplications.
n
n VPNacrosspublicIPnetwork.
n MPLSoverGRE.
n MultipointGREforscalablenetworktoreachmultipleremotesites.
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
|     | ip.ForanIPv6inIPv6tunnel,enterthecommandsource |     |     |     |     | ipv6. |     |
| --- | ---------------------------------------------- | --- | --- | --- | --- | ----- | --- |
source
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
CreatesGREtunnel33.
n
SetthetunnelIPaddressto10.10.20.209/24.
n
n SetsthetunnelsourceIPaddressto10.10.10.1.
n SetsthetunneldestinationIPaddressto10.10.10.2.
n Enablesthetunnel.
| switch(config)#        | interface |        | tunnel      | 33 mode         | gre ipv4   |          |         |
| ---------------------- | --------- | ------ | ----------- | --------------- | ---------- | -------- | ------- |
| switch(config-gre-if)# |           |        | ip address  | 10.10.20.209/24 |            |          |         |
| switch(config-gre-if)# |           |        | source      | ip address      | 10.10.10.1 |          |         |
| switch(config-gre-if)# |           |        | destination | ip address      | 10.10.10.2 |          |         |
| switch(config-gre-if)# |           |        | no shutdown |                 |            |          |         |
| Creating               | a GRE     | tunnel |             | for traversing  |            | a public | network |
IPTunnels |118

ThisexamplecreatesaGREtunnelbetweentwoswitches,enablingtrafficfromtwonetworkstotraversea
publicnetwork.
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
c. CreateGREtunnel10andassigntheIPaddress192.168.10.1/24,sourceaddress10.1.1.1,and
destinationaddress20.1.1.1toit.
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
119
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

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
Procedure
IPTunnels |120

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
d. CreateGREtunnel10andassigntheIPaddress192.168.10.1/24,sourceaddress10.1.1.1,and
destinationaddress20.1.1.1toit.
| switch(config)#        | interface | tunnel      |     | 10 mode gre ipv4 |
| ---------------------- | --------- | ----------- | --- | ---------------- |
| switch(config-gre-if)# |           | ip address  |     | 192.168.10.1/24  |
| switch(config-gre-if)# |           | source      | ip  | 10.1.1.1         |
| switch(config-gre-if)# |           | destination |     | ip 20.1.1.1      |
| switch(config-gre-if)# |           | no shutdown |     |                  |
| switch(config-gre-if)# |           | exit        |     |                  |
e. CreateGREtunnel20andassigntheIPaddress192.168.20.1/24,sourceaddress30.1.1.1,and
destinationaddress40.1.1.1toit.
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
c. CreateGREtunnel10andassigntheIPaddress192.168.10.2/24,sourceaddress20.1.1.1,and
destinationaddress10.1.1.1toit.
| switch(config)#        | interface | tunnel     |     | 10 mode gre ipv4 |
| ---------------------- | --------- | ---------- | --- | ---------------- |
| switch(config-gre-if)# |           | ip address |     | 192.168.10.2/24  |
121
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

|     | switch(config-gre-if)# |     | source      |          | ip 20.1.1.1 |          |     |
| --- | ---------------------- | --- | ----------- | -------- | ----------- | -------- | --- |
|     | switch(config-gre-if)# |     | destination |          | ip          | 10.1.1.1 |     |
|     | switch(config-gre-if)# |     | no          | shutdown |             |          |     |
switch(config-gre-if)#
exit
d. Definesroutessothattrafficfromnetwork2canreachnetwork1throughtunnel10.
|     | switch(config)# | ip route |     | 10.1.1.0/24   |     | 20.1.1.2 |     |
| --- | --------------- | -------- | --- | ------------- | --- | -------- | --- |
|     | switch(config)# | ip route |     | 180.1.10.0/24 |     | tunnel10 |     |
3. Onswitch3:
|     | a. Enableinterface1/1/1andassigntheIPaddress40.1.1.1/24toit. |     |     |     |     |     |     |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
switch# config
|     | switch(config)#                                                | interface |          | 1/1/1 |             |     |     |
| --- | -------------------------------------------------------------- | --------- | -------- | ----- | ----------- | --- | --- |
|     | switch(config-if)#                                             | ip        | address  |       | 40.1.1.1/24 |     |     |
|     | switch(config-if)#                                             | no        | shutdown |       |             |     |     |
|     | b. Enableinterface1/1/2andassigntheIPaddress200.1.10.2/24toit. |           |          |       |             |     |     |
|     | switch(config)#                                                | interface |          | 1/1/2 |             |     |     |
switch(config-if)#
|     |                    | ip   | address  |     | 200.1.10.2/24 |     |     |
| --- | ------------------ | ---- | -------- | --- | ------------- | --- | --- |
|     | switch(config-if)# | no   | shutdown |     |               |     |     |
|     | switch(config-if)# | exit |          |     |               |     |     |
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
Procedure
IPTunnels |122

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
123
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |     |     |     |     |
| --------------------------- | ----- | ------------- | --- | --- | --- | --- | --- |

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
IPTunnels |124

parameters for this tunnel interface.
switch(config)# interface tunnel 10 mode ip 6in6
switch(config-ip-if)# ipv6 address 2001:DB8::2/62
switch(config-ip-if)# source ipv6 2001:DB8:9::1
switch(config-ip-if)# destination ipv6 2001:DB8:5::1
switch(config-ip-if)# no shutdown
switch(config-ip-if)# exit

d. Defines routes so that traffic from network 2 can reach network 1 through the tunnel.

switch(config)# ipv6 route 2001:DB8:5::0/64 2001:DB8:9::2
switch(config)# ipv6 route 2080::0/64 tunnel10

IP tunnels commands

description
description <DESC>
no description

Description

Associates a text description with an IP tunnel for identification purposes.

The no form of this command removes the description from an IP tunnel.

Parameter

<DESC>

Examples

Description

Specifies the descriptive text to associate with the IP tunnel.
Range: 1 to 64 printable ASCII characters.

Defines a description for GRE tunnel 33.

switch(config)# interface tunnel 33 mode gre ipv4
switch(config-gre-if)# description Network A Tunnel C

Removes the description for GRE tunnel 33.

switch(config)# interface tunnel 33
switch(config-gre-if)# no description

Defines a description for IPv6 in IPv4 tunnel 27.

switch(config)# interface tunnel 27 mode ip 6in4
switch(config-ip-if)# description Network 3 Tunnel 27

Removes the description for IPv6 in IPv4 tunnel 27.

switch(config)# interface tunnel 27
switch(config-ip-if)# no description

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

125

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
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | config-ip-if |     | forthiscommand. |     |
| ---- | ------------ | --- | --------------- | --- |
8360
| destination    | ip             |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| destination    | ip <IPV4-ADDR> |     |     |     |
| no destination | ip <IPV4-ADDR> |     |     |     |
Description
SetsthedestinationIPaddressforanIPtunnel.Specifytheaddressoftheinterfaceontheremotedeviceto
whichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPaddressfromanIPtunnel.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IPV4-ADDR> SpecifiesthedestinationIPaddressinIPv4format(x.x.x.x),
wherexisadecimalnumberfrom0to255.
Examples
DefinesthedestinationIPaddresstobe10.10.10.1forGREtunnel33.
| switch(config)#        | interface | tunnel      | 33 mode       | gre ipv4 |
| ---------------------- | --------- | ----------- | ------------- | -------- |
| switch(config-gre-if)# |           | destination | ip 10.10.10.1 |          |
IPTunnels |126

DeletesthedestinationIPaddress10.10.10.1fromGREtunnel33.
| switch(config)#        | interface | tunnel         | 33  |               |
| ---------------------- | --------- | -------------- | --- | ------------- |
| switch(config-gre-if)# |           | no destination |     | ip 10.10.10.1 |
DefinesthedestinationIPaddresstobe10.10.20.1forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel      | 27  | mode ip 6in4 |
| --------------------- | --------- | ----------- | --- | ------------ |
| switch(config-ip-if)# |           | destination | ip  | 10.10.20.1   |
DeletesthedestinationIPaddress10.10.20.1fromIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel         | 27  |               |
| --------------------- | --------- | -------------- | --- | ------------- |
| switch(config-ip-if)# |           | no destination |     | ip 10.10.20.1 |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
config-gre-if
8320 Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | config-ip-if |     | forthiscommand. |     |
| ---- | ------------ | --- | --------------- | --- |
8360
| destination    | ipv6              |     |     |     |
| -------------- | ----------------- | --- | --- | --- |
| destination    | ipv6 <IPVv6-ADDR> |     |     |     |
| no destination | ipv6 [IPV6-ADDR]  |     |     |     |
Description
SetsthedestinationIPv6addressforanIPtunnel.Specifytheaddressoftheinterfaceontheremotedevice
towhichthetunnelwillbeestablished.
ThenoformofthiscommanddeletesthedestinationIPv6addressfromanIPtunnel.
| Parameter   |     |     | Description                             |     |
| ----------- | --- | --- | --------------------------------------- | --- |
| <IPV6-ADDR> |     |     | SpecifiesthetunnelIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Thisisoptionalinthenoformofthecommand.
Examples
DefinesthedestinationIPv6addresstobe2001:DB8::1forIPv6inIPv6tunnel
127
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |     |
| --------------------------- | ----- | ------------- | --- | --- |

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
8320 Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
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
n gre ipv4:CreatesaGREtunnel.
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
IPTunnels |128

Examples
DefinesanewGREtunnelwithnumber27.
switch(config)#
|     | interface | tunnel | 33 mode gre ipv4 |
| --- | --------- | ------ | ---------------- |
switch(config-gre-if)#
Switchestotheconfig-gre-ifcontextforexistingtunnel33.
| switch(config)# | interface | tunnel | 33  |
| --------------- | --------- | ------ | --- |
switch(config-gre-if)#
DeletesGREtunnel33.
| switch(config)# | no interface | tunnel | 33  |
| --------------- | ------------ | ------ | --- |
DefinesanewIPv6inIPv4tunnelwithnumber27.
| switch(config)# | interface | tunnel | 27 mode ip 6in4 |
| --------------- | --------- | ------ | --------------- |
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
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
129
AOS-CX10.08IPServicesGuide| (83xx SwitchSeries)

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | config-ip-if |     | forthiscommand. |
| ---- | ------------ | --- | --------------- |
| 8360 | config       |     |                 |
ip address
| ip address <IPV4-ADDR>/<MASK> |                    |     |     |
| ----------------------------- | ------------------ | --- | --- |
| no ip address                 | <IPV4-ADDR>/<MASK> |     |     |
Description
SetsthelocalIPaddressofaGREtunnel.Thisaddressidentifiesthetunnelinterfaceforrouting.Itmustbe
onthesamesubnetasthetunneladdressassignedontheremotedevice.
ThenoformofthiscommanddeletesthelocalIPaddressassignedtoaGREtunnel.
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
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8360
IPTunnels |130

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
8320 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | config-if |     | forthiscommand. |
| ---- | --------- | --- | --------------- |
8360
ip mtu
ip mtu <VALUE>
Description
SetstheMTU(maximumtransmissionunit)foranIPinterface.Thedefaultvalueis1500bytes.
131
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |
| --------------------------- | ----- | ------------- | --- |

ThenoformofthiscommandsetstheMTUtothedefaultvalueof1500bytes.
| Parameter |     |     | Description                                          |
| --------- | --- | --- | ---------------------------------------------------- |
| <VALUE>   |     |     | SpecifiestheMTUinbytes.Range:1,280bytesto9,192bytes. |
Usage
TheIPMTUisthelargestIPpacketthatcanbesentorreceivedbytheinterface.Foratunnel,theIPMTUis
themaximumsizeoftheIPpayload.Toenablejumbopacketforwardingthroughthetunnel,settheIPMTU
ofthetunneltoavaluegreaterthan1500.AlsosettheMTUandtheIPMTUvaluesfortheunderlying
physicalinterfacethatthetunnelisusingtoavaluegreaterthan1,500bytes.TheIPMTUofthetunnel
mustalsobegreaterthanorequaltotheMTUoftheingressinterfaceontheswitch.TheIPMTUvalueof
thetunnelmustalsobelessthanorequaltotheIPMToftheunderlyinginterfacethatthetunnelisusing.
WhendefiningaGREtunnel,theMTUhastoaccountfor28bytesofIPlayeroverhead,plusaGREheader.
ItmustbelargerthantheMTUoftheinterfacethatthetunnelisusing.PacketslargerthantheMTUare
dropped.
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
IPTunnels |132

CommandHistory
| Release        |     |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --- | --------- | --- | --- | --- |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 |     | config-ip-if |     |     | forthiscommand. |     |     |     |
| ---- | --- | ------------ | --- | --- | --------------- | --- | --- | --- |
8360
| show interface |     |                         | tunnel |     |            |     |     |     |
| -------------- | --- | ----------------------- | ------ | --- | ---------- | --- | --- | --- |
| show interface |     | tunnel[<TUNNEL-NUMBER>] |        |     | [vsx-peer] |     |     |     |
Description
ShowsconfigurationsettingsforallIPtunnels,oraspecifictunnel.
| Parameter       |     |     |     |     | Description                                  |     |     |     |
| --------------- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
| <TUNNEL-NUMBER> |     |     |     |     | SpecifiesthenumberofanIPtunnel.Range:1to127. |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showsconfigurationsettingsfortunnel10,whichisaGREtunnelinthefollowingexample.
switch#
|            | show        | interface | tunnel10     |         |              |     |       |     |
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
| switch#   | show     | interface | tunnel12 |     |     |     |     |     |
| --------- | -------- | --------- | -------- | --- | --- | --- | --- | --- |
| Interface | tunnel12 |           | is up    |     |     |     |     |     |
133
| AOS-CX10.08IPServicesGuide| |     | (83xx | SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ----- | ------------- | --- | --- | --- | --- | --- |

| Admin        | state       | is up    |              |         |         |     |       |     |
| ------------ | ----------- | -------- | ------------ | ------- | ------- | --- | ----- | --- |
| tunnel       | type        | IPv6     | in IPv6      |         |         |     |       |     |
| tunnel       | interface   |          | IPv6 address |         | 4::1/64 |     |       |     |
| tunnel       | source      | IPv6     | address      | 2::1    |         |     |       |     |
| tunnel       | destination |          | IPv6         | address | 2::2    |     |       |     |
| tunnel       | ttl         | 60       |              |         |         |     |       |     |
| Description: |             | Network2 | Tunnel       |         |         |     |       |     |
| Statistics   |             |          |              |         | RX      | TX  | Total |     |
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
| L3 Packets   |             |           |         |              | 0            | 0   |       | 0   |
| ------------ | ----------- | --------- | ------- | ------------ | ------------ | --- | ----- | --- |
| L3 Bytes     |             |           |         |              | 0            | 0   |       | 0   |
| Interface    | tunnel11    |           | is up   |              |              |     |       |     |
| Admin        | state       | is up     |         |              |              |     |       |     |
| tunnel       | type        | IPv6      | in IPv4 |              |              |     |       |     |
| tunnel       | source      | IPv4      | address | 198.51.100.0 |              |     |       |     |
| tunnel       | destination |           | IPv4    | address      | 198.51.200.5 |     |       |     |
| tunnel       | ttl         | 80        |         |              |              |     |       |     |
| Description: |             | Network11 |         |              |              |     |       |     |
| Statistics   |             |           |         |              | RX           | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets   |             |          |              |         | 0       | 0   |       | 0   |
| ------------ | ----------- | -------- | ------------ | ------- | ------- | --- | ----- | --- |
| L3 Bytes     |             |          |              |         | 0       | 0   |       | 0   |
| Interface    | tunnel12    |          | is up        |         |         |     |       |     |
| Admin        | state       | is up    |              |         |         |     |       |     |
| tunnel       | type        | IPv6     | in IPv6      |         |         |     |       |     |
| tunnel       | interface   |          | IPv6 address |         | 4::1/64 |     |       |     |
| tunnel       | source      | IPv6     | address      | 2::1    |         |     |       |     |
| tunnel       | destination |          | IPv6         | address | 2::2    |     |       |     |
| tunnel       | ttl         | 60       |              |         |         |     |       |     |
| Description: |             | Network2 | Tunnel       |         |         |     |       |     |
| Statistics   |             |          |              |         | RX      | TX  | Total |     |
------------- -------------------- -------------------- --------------------
| L3 Packets |     |     |     |     | 0   | 0   |     | 0   |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3 Bytes   |     |     |     |     | 0   | 0   |     | 0   |
CommandHistory
IPTunnels |134

| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
8360
| show running-config |     |           | interface             | tunnel |            |
| ------------------- | --- | --------- | --------------------- | ------ | ---------- |
| show running-config |     | interface | tunnel<TUNNEL-NUMBER> |        | [vsx-peer] |
Description
ShowsthecommandsusedtoconfigureanIPtunnel.
| Parameter       |     |     |     | Description                                  |     |
| --------------- | --- | --- | --- | -------------------------------------------- | --- |
| <TUNNEL-NUMBER> |     |     |     | SpecifiesthenumberofanIPtunnel.Range:1to127. |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowstheconfigurationforaGREtunnel.
| switch#     | show           | running-config | interface     | tunnel2 |     |
| ----------- | -------------- | -------------- | ------------- | ------- | --- |
| interface   | tunnel         | 2              | mode gre ipv4 |         |     |
| source      | ip 10.10.20.11 |                |               |         |     |
| destination |                | ip 10.20.1.2   |               |         |     |
| ip          | address        | 10.10.10.1/24  |               |         |     |
| ttl         | 60             |                |               |         |     |
ShowstheconfigurationforIPv6inIPv4tunnel.
switch#
|             | show           | running-config   | interface | tunnel5 |     |
| ----------- | -------------- | ---------------- | --------- | ------- | --- |
| interface   | tunnel5        | mode             | ip 6in4   |         |     |
| source      | ip 10.10.10.12 |                  |           |         |     |
| destination |                | ip 22.20.20.20   |           |         |     |
| ip6         | address        | 2001:DB8:5::1/64 |           |         |     |
| ttl         | 60             |                  |           |         |     |
| no          | shutdown       |                  |           |         |     |
| description |                | Network10        |           |         |     |
ShowstheconfigurationforIPv6inIPv6tunnel.
135
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- |

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
8320 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
| 8325 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| ---- | --- | --- | ----------------------------------------------------- |
| 8360 |     |     | commandfromtheoperatorcontext(>)only.                 |
shutdown
shutdown
no shutdown
Description
ThiscommanddisablesanIPinterface.IPinterfacesaredisabledbydefaultwhencreated.
ThenoformofthiscommandenablesanIPinterface.
Examples
EnablesGREinterface33.
| switch(config)#        | interface | tunnel      | 33 mode gre ipv4 |
| ---------------------- | --------- | ----------- | ---------------- |
| switch(config-gre-if)# |           | no shutdown |                  |
DisablesGREinterface33.
switch(config)#
|                        | interface | tunnel   | 33 mode gre ipv4 |
| ---------------------- | --------- | -------- | ---------------- |
| switch(config-gre-if)# |           | shutdown |                  |
EnablesIPv6inIPv4interface27.
| switch(config)#       | interface | tunnel   | 27 mode ip 6in4 |
| --------------------- | --------- | -------- | --------------- |
| switch(config-ip-if)# | no        | shutdown |                 |
DisablesIPv6inIPv4interface27.
IPTunnels |136

| switch(config)#       | interface | tunnel   | 27 mode ip 6in4 |
| --------------------- | --------- | -------- | --------------- |
| switch(config-ip-if)# |           | shutdown |                 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-ip-if |     | forthiscommand. |
| --- | ------------ | --- | --------------- |
8325
8360
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
<IPV4-ADDR>
SpecifiesthesourceIPaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
Examples
DefinesthesourceIPaddresstobe10.10.20.1forGREtunnel33.
| switch(config)#        | interface | tunnel | 33 mode gre ipv4 |
| ---------------------- | --------- | ------ | ---------------- |
| switch(config-gre-if)# |           | source | ip 10.10.20.1    |
DeletesthesourceIPaddress10.1.20.1fromGREtunnel33.
| switch(config)#        | interface | tunnel    | 33            |
| ---------------------- | --------- | --------- | ------------- |
| switch(config-gre-if)# |           | no source | ip 10.10.20.1 |
DefinesthesourceIPaddresstobe10.10.10.1forIPv6inIPv4tunnel27.
switch(config)#
|                       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# |           | source | ip 10.10.10.1   |
DeletesthesourceIPaddress10.1.10.1fromIPv6inIPv4tunnel27.
137
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |
| --------------------------- | ----- | ------------- | --- |

| switch(config)# | interface | tunnel | 27  |     |
| --------------- | --------- | ------ | --- | --- |
switch(config-ip-if)#
|     |     | no source | ip 10.10.10.1 |     |
| --- | --- | --------- | ------------- | --- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-ip-if |     | forthiscommand. |     |
| --- | ------------ | --- | --------------- | --- |
8325
8360
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
IPTunnels |138

CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-ip-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
8325
8360
ttl
ttl <COUNT>
no ttl
Description
SetstheTTL(time-to-live),alsoknownasthehopcount,fortunneledpackets.Ifnotconfigured,thedefault
valueof64isusedforthetunnel.(Thehopcountoftheoriginalpacketsisnotchanged.)Amaximumof
fourdifferentTTLvaluescanbeusedatthesametimebyalltunnelsontheswitch.Forexample,iftunnel-1
hasTTL10,tunnel-2hasTTL20,tunnel-3hasTTL30,andtunnel-4hasTTL40,thentunnel-5cannothavea
uniqueTTLvalue,itmustreuseoneofthevaluesassignedtotheothertunnels(10,20,30,40).
ThenoformofthiscommandsetsTTLtothedefaultvalueof64.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<COUNT>
Specifiesthehopcount.Range:1to255.Default:64.
Examples
DefinesaTTLof99forGREtunnel33.
| switch(config)# | interface | tunnel | 33 mode gre ipv4 |
| --------------- | --------- | ------ | ---------------- |
switch(config-gre-if)#
ttl 99
SetstheTTLforGREtunnel33tothedefaultvalueof64.
| switch(config)#        | interface | tunnel | 33  |
| ---------------------- | --------- | ------ | --- |
| switch(config-gre-if)# |           | no ttl |     |
DefinesaTTLof55forIPv6inIPv4tunnel27.
| switch(config)#       | interface | tunnel | 27 mode ip 6in4 |
| --------------------- | --------- | ------ | --------------- |
| switch(config-ip-if)# | ttl       | 55     |                 |
SetstheTTLforIPv6inIPv4tunnel27tothedefaultvalueof64.
| switch(config)#       | interface | tunnel | 27  |
| --------------------- | --------- | ------ | --- |
| switch(config-ip-if)# | no        | ttl    |     |
CommandHistory
139
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
8320 config-gre-if Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | config-ip-if |     | forthiscommand. |
| ---- | ------------ | --- | --------------- |
8360
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
Examples
AssignsGREtunnel33tovrf1.
| switch(config)#        | interface | tunnel     | 33 mode gre ipv4 |
| ---------------------- | --------- | ---------- | ---------------- |
| switch(config-gre-if)# |           | vrf attach | vrf1             |
ReassignsGREtunnel33tothedefaultVRF.
| switch(config)#        | interface | tunnel | 33          |
| ---------------------- | --------- | ------ | ----------- |
| switch(config-gre-if)# |           | no vrf | attach vrf1 |
AssignsIPv6inIPv4tunnel27tovrf2.
| switch(config)#       | interface | tunnel     | 27 mode gre ipv4 |
| --------------------- | --------- | ---------- | ---------------- |
| switch(config-ip-if)# |           | vrf attach | vrf2             |
ReassignsIPv6inIPv4tunnel27tothedefaultVRF.
| switch(config)#       | interface | tunnel        | 27   |
| --------------------- | --------- | ------------- | ---- |
| switch(config-ip-if)# |           | no vrf attach | vrf2 |
AssignsIPv6inIPv6tunnel8tovrf3.
IPTunnels |140

| switch(config)# | interface | tunnel | 8 mode ip 6in6 |
| --------------- | --------- | ------ | -------------- |
switch(config-ip-if)#
|     |     | vrf attach | vrf3 |
| --- | --- | ---------- | ---- |
ReassignsIPv6inIPv6tunnel8tothedefaultVRF.
| switch(config)#       | interface | tunnel        | 8    |
| --------------------- | --------- | ------------- | ---- |
| switch(config-ip-if)# |           | no vrf attach | vrf3 |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-gre-if
8320 Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | config-ip-if |     | forthiscommand. |
| ---- | ------------ | --- | --------------- |
8360
141
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |
| --------------------------- | ----- | ------------- | --- |

Internet Control Message Protocol
(ICMP)

Chapter 7

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

142

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
EnablesthesendingofICMPv4andICMPv6redirectmessagestothesourcehost.Enabledbydefault.
ThenoformofthiscommanddisablesICMPv4andICMPv6redirectmessagestothesourcehost.
Examples
EnablingICMPredirectmessages:
| switch(config)# |     | ip icmp | redirect |     |
| --------------- | --- | ------- | -------- | --- |
DisablingICMPredirectmessages:
| switch(config)# |     | no ip icmp | redirect |     |
| --------------- | --- | ---------- | -------- | --- |
CommandHistory
InternetControlMessageProtocol(ICMP)|143

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
144
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
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
InternetControlMessageProtocol(ICMP)|145

Chapter 8

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

146

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
| DNS       | client      | commands      |      |                  |     |
| --------- | ----------- | ------------- | ---- | ---------------- | --- |
| ip dns    | domain-list |               |      |                  |     |
| ip dns    | domain-list | <DOMAIN-NAME> | [vrf | <VRF-NAME>]      |     |
| no ip dns | domain-list | <DOMAIN-NAME> |      | [vrf <VRF-NAME>] |     |
Description
ConfiguresoneormoredomainnamesthatareappendedtotheDNSrequest.TheDNSclientappends
eachnameinsuccessionuntiltheDNSserverreplies.DomainscanbeeitherIPv4orIPv6.Bydefault,
requestsareforwardedonthedefaultVRF.
DNS|147

Thenoformofthiscommandremovesadomainfromthelist.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
list <DOMAIN-NAME> Specifiesadomainname.Uptosixdomainscanbeaddedtothe
list.Length:1to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
Thisexampledefinesalistwithtwoentries:domain1.comanddomain2.com.
| switch(config)# |     | ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | ------ | ----------- | --- | ----------- | --- |
| switch(config)# |     | ip dns | domain-list |     | domain2.com |     |
Thisexampledefinesalistwithtwoentries,domain2.comanddomain5.com,withrequestsbeingsenton
mainvrf.
| switch(config)# |     | ip dns | domain-list |     | domain2.com | vrf mainvrf |
| --------------- | --- | ------ | ----------- | --- | ----------- | ----------- |
| switch(config)# |     | ip dns | domain-list |     | domain5.com | vrf mainvrf |
Thisexampleremovestheentrydomain1.com.
| switch(config)# |     | no ip dns | domain-list |     | domain1.com |     |
| --------------- | --- | --------- | ----------- | --- | ----------- | --- |
CommandHistory
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
148
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- |

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DOMAIN-NAME> SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     | ip  | dns | domain-name | domain.com |     |
| --------------- | --- | --- | --- | ----------- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |     | no  | ip dns | domain-name | domain.com |     |
| --------------- | --- | --- | ------ | ----------- | ---------- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     | --           |     |
CommandInformation
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
<IP-ADDR> SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- |
DNS|149

Examples
| ThisexampledefinesanIPv4addressof |     |     |     |     | 3.3.3.3forhost1. |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
switch(config)#
|                                          |     |     | ip dns    | host | host1 | 3.3.3.3           |     |
| ---------------------------------------- | --- | --- | --------- | ---- | ----- | ----------------- | --- |
| ThisexampledefinesanIPv6addressofb::5    |     |     |           |      |       | forhost           | 1.  |
| switch(config)#                          |     |     | ip dns    | host | host1 | b::5              |     |
| Thisexampledefinesremovestheentryforhost |     |     |           |      |       | 1withaddressb::5. |     |
| switch(config)#                          |     |     | no ip dns | host | host1 | b::5              |     |
CommandHistory
| Release        |     |     |     |     |     | Modification |     |
| -------------- | --- | --- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     |     |     | --           |     |
CommandInformation
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
150
| AOS-CX10.08IPServicesGuide| |     |     | (83xx SwitchSeries) |     |     |     |     |
| --------------------------- | --- | --- | ------------------- | --- | --- | --- | --- |

| switch(config)# | ip dns | server-address | 1.1.1.1 |
| --------------- | ------ | -------------- | ------- |
Thisexampledefinesanameserverata::1.
| switch(config)# | ip dns | server-address | a::1 |
| --------------- | ------ | -------------- | ---- |
Thisexampleremovesanameserverata::1.
| switch(config)# | no ip dns | server-address | a::1 |
| --------------- | --------- | -------------- | ---- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show ip dns |                            |     |     |
| ----------- | -------------------------- | --- | --- |
| show ip dns | [vrf <VRF-NAME>][vsx-peer] |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
TheseexamplesdefineDNSsettingsandthenshowhowtheyaredisplayedwiththeshow ip dns
command.
| switch(config)# | ip dns | domain-name    | domain.com  |
| --------------- | ------ | -------------- | ----------- |
| switch(config)# | ip dns | domain-list    | domain5.com |
| switch(config)# | ip dns | domain-list    | domain8.com |
| switch(config)# | ip dns | server-address | 4.4.4.4     |
| switch(config)# | ip dns | server-address | 6.6.6.6     |
DNS|151

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
| host3 |     | 5.5.5.5 |     |     |     |     |     |
| ----- | --- | ------- | --- | --- | --- | --- | --- |
| host3 |     | c::12   |     |     |     |     |     |
CommandHistory
152
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- | --- |

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
DNS|153

Chapter 9

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

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

154

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
ARP|155

1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtoaninterfacewiththecommandinterface,ortoaninterfaceVLANwiththecommand
| interface | vlan,ortoaLAGwiththecommandinterface |     | lag. |
| --------- | ------------------------------------ | --- | ---- |
3. EnablelocalproxyARPwiththecommandip local-proxy-arp.
Examples
ThisexampleconfigureslocalproxyARPoninterface1/1/2
| switch# config     |                    |       |     |
| ------------------ | ------------------ | ----- | --- |
| switch(config)#    | interface          | 1/1/2 |     |
| switch(config-if)# | ip local-proxy-arp |       |     |
ThisexampleconfigureslocalproxyARPoninterfaceVLAN30.
| switch# config          |                |                    |     |
| ----------------------- | -------------- | ------------------ | --- |
| switch(config)#         | interface      | vlan 30            |     |
| switch(config-vlan-30)# |                | ip local-proxy-arp |     |
| Dynamic                 | ARP Inspection |                    |     |
ARPisusedforresolvingIPagainstMACaddressesonabroadcastnetworksegmentliketheEthernetand
wasoriginallydefinedbyInternetStandardRFC826.ARPdoesnotsupportanyinherentsecurity
mechanismandassuchdependsonsimpledatagramexchangesfortheresolution,withmanyofthese
beingbroadcast.
Becauseitisanunreliableandnon-secureprotocol,ARPisvulnerabletoattacks.Someattacksmaybe
targetedtowardthenetworkswhereasotherattacksmaybetargetedtowardtheswitchitself.Theattacks
primarilyintendtocreatedenialofservice(DoS)fortheotherentitiespresentinthenetwork.
Mostoftheattacksarecarriedoutinoneofthefollowingthreeforms:
n OverwhelmingtheswitchcontrolplanewithtoomanyARPpackets.
n Overwhelmingtheswitchcontrolplanewithtoomanyunresolveddatapackets.
n Masqueradingasatrustedgateway/serverbywronglyadvertisingARPs.
Severaldefensemechanismscanbeputinplaceonaswitchtoprotectagainstattacks:
n LimittheamountofARPactivityallowedfromahostoronaport.
n EnsurethatallARPpacketsareconsistentwithoneormorebindingdatabases,whichcanbecreated
throughvariousmeans.
n EnforceintegritychecksontheARPpacketstocheckagainstdifferentMACorIPaddressesinthe
EthernetorIPheaderandARPheader.
ThisreleaseimplementsDynamicARPInspectiontoenforceDHCPsnoopingbindingonallARPpacketsand
issupportedonthe6300,6400,and8400platforms.Thefeaturewillbedisabledfromthecode,CLI,and
schemabytheuseofappropriateconfigflagsforotherplatforms.
Onlythefollowingissupported:
EnablinganddisablingofDynamicARPInspectiononaVLANlevel(itdoesnothavetobeSVI).
n
DefiningthememberportsofaVLANaseithertrustedoruntrusted.
n
n OnlyARPtrafficonuntrustedportssubjectedtochecks.
156
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |
| --------------------------- | ------------------- | --- | --- |

Routedports(RoPs)alwaystreatedastrusted.
n
ListeningtotheDHCPBindingstableandcheckeveryARPpackettomatchagainstthebinding.
n
ARPACLsarenotsupportedinthisreleaseandtheDHCPsnoopingtablewillbetheonlysourceofbinding.
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
ARP|157

Example
Settinganinterfaceastrusted:
switch(config-if)#
|     |     | arp | inspection | trust |
| --- | --- | --- | ---------- | ----- |
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
158
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |
| --------------------------- | --- | ------------------- | --- | --- |

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
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
ClearingallIPv4andIPv6neighborARPentriesforallVRFs:
| switch# | clear arp vrf | all-vrfs |     |
| ------- | ------------- | -------- | --- |
ClearingallIPv4andIPv6neighborARPentriesforaspecificVRFinstance:
| switch# | clear arp vrf | RED |     |
| ------- | ------------- | --- | --- |
CommandHistory
ARP|159

| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip local-proxy-arp
ip local-proxy-arp
no ip local-proxy-arp
Description
EnableslocalproxyARPonthespecifiedinterface.LocalproxyARPissupportedonLayer3physical
interfacesandonVLANinterfaces.ToenablelocalproxyARPonaninterface,routingmustbeenabledon
thatinterface.
ThenoformofthiscommanddisableslocalproxyARPonthespecifiedinterface.
Examples
EnablinglocalproxyARPoninterface1/1/1:
| switch#            | interface 1/1/1    |     |
| ------------------ | ------------------ | --- |
| switch(config-if)# | ip local proxy-arp |     |
EnablinglocalproxyARPoninterfaceVLAN3:
| switch#                 | interface vlan 3   |     |
| ----------------------- | ------------------ | --- |
| switch(config-if-vlan)# | ip local-proxy-arp |     |
DisablinglocalproxyARPononinterface1/1/1.
| switch# | interface 1/1/1 |     |
| ------- | --------------- | --- |
switch(config-if)#
no ip local-proxy-arp
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
160
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IPV6-ADDR>>
SpecifiesanIPaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
| mac <MAC-ADDR>> |     |     | SpecifiestheMACaddressoftheneighbor |
| --------------- | --- | --- | ----------------------------------- |
(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0
toF.Range:4096to131072.Default:131072.
Example
| CreatesastaticARPentryoninterface |           | 1/1/1. |     |
| --------------------------------- | --------- | ------ | --- |
| switch(config)#                   | interface | 1/1/1  |     |
switch(config-if)# arp ipv6 neighbor 2001:0db8:85a3::8a2e:0370:7334 mac
00:50:56:96:df:c8
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ip proxy-arp
ip proxy-arp
no ip proxy-arp
Description
ARP|161

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
| switch#                 | interface vlan 3 |     |
| ----------------------- | ---------------- | --- |
| switch(config-if-vlan)# | ip proxy-arp     |     |
EnablingproxyARPonaLAG11:
| switch(config)# | int lag 11 |     |
| --------------- | ---------- | --- |
switch(config-lag-if)# ip proxy-arp
DisablingproxyARPoninterface1/1/1:
| switch#            | interface 1/1/1 |     |
| ------------------ | --------------- | --- |
| switch(config-if)# | no ip proxy-arp |     |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if-vlan | forthiscommand. |
| --- | -------------- | --------------- |
config-lag-vlan
show arp
show arp [vsx-peer]
Description
ShowstheentriesintheARP(AddressResolutionProtocol)table.
162
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
ThiscommanddisplaysinformationaboutARPentries,includingtheIPaddress,MACaddress,port,and
state.
Whennoparametersarespecified,theshow arpcommandshowsallARPentriesforthedefaultVRF(Virtual
RouterForwarding)instance.
Examples
| switch#      | show arp |     |     |      |               |     |       |
| ------------ | -------- | --- | --- | ---- | ------------- | --- | ----- |
| IPv4 Address |          | MAC |     | Port | Physical Port |     | State |
-------------------------------------------------------------------------------
| 192.168.1.2 |           |             | 00:50:56:96:7b:e0 | vlan10 | 1/1/29 | stale     |     |
| ----------- | --------- | ----------- | ----------------- | ------ | ------ | --------- | --- |
| 192.168.1.3 |           |             | 00:50:56:96:7b:ac | vlan10 | 1/1/1  | reachable |     |
| Total       | Number Of | ARP Entries | Listed-           | 2.     |        |           |     |
-------------------------------------------------------------------------------
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show arp            | inspection |           | interface |     |     |     |     |
| ------------------- | ---------- | --------- | --------- | --- | --- | --- | --- |
| show arp inspection |            | interface |           |     |     |     |     |
Description
DisplaysthecurrentconfigurationofdynamicARPinspectiononaVLANorinterface.
Examples
| switch# | show arp | inspection | interface |     |     |     |     |
| ------- | -------- | ---------- | --------- | --- | --- | --- | --- |
---------------------------------------------------------------------------
| Interface |     | Trust-State |     |     |     |     |     |
| --------- | --- | ----------- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------
ARP|163

| 1/1/1 | Untrusted |     |     |     |
| ----- | --------- | --- | --- | --- |
---------------------------------------------------------------------------
| switch# | show arp inspection | interface | vsx-peer |     |
| ------- | ------------------- | --------- | -------- | --- |
---------------------------------------------------------------------------
| Interface | Trust-State |     |     |     |
| --------- | ----------- | --- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1  | Untrusted |     |     |     |
| ------ | --------- | --- | --- | --- |
| lag100 | Trusted   |     |     |     |
---------------------------------------------------------------------------
| switch# | show arp inspection | interface | 1/1/1 |     |
| ------- | ------------------- | --------- | ----- | --- |
---------------------------------------------------------------------------
| Interface | Trust-State |     |     |     |
| --------- | ----------- | --- | --- | --- |
---------------------------------------------------------------------------
| 1/1/1 | Untrusted |     |     |     |
| ----- | --------- | --- | --- | --- |
---------------------------------------------------------------------------
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
164
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

| switch# | show arp inspection | statistics | vlan |     |
| ------- | ------------------- | ---------- | ---- | --- |
-----------------------------------------------------------------
| VLAN Name |     | Forwarded |     | Dropped |
| --------- | --- | --------- | --- | ------- |
-----------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     | 0   |     | 0   |
| ---------------- | --- | --- | --- | --- |
| 200 VLAN200      |     | 0   |     | 0   |
-----------------------------------------------------------------
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show arp | state |     |     |     |
| -------- | ----- | --- | --- | --- |
show arp state {all | failed | incomplete | permanent | reachable | stale} [vsx-peer]
Description
ShowsARP(AddressResolutionProtocol)cacheentriesthatareinthespecifiedstate.
| Parameter |     |     | Description                                    |     |
| --------- | --- | --- | ---------------------------------------------- | --- |
| all       |     |     | ShowstheARPcacheentriesforallVRF(VirtualRouter |     |
Forwarding)instances.
| failed |     |     | ShowstheARPcacheentriesthatareinfailedstate.The |     |
| ------ | --- | --- | ----------------------------------------------- | --- |
neighbormighthavebeendeleted.
| incomplete |     |     | ShowstheARPcacheentriesthatareinincompletestate. |     |
| ---------- | --- | --- | ------------------------------------------------ | --- |
Anincompletestatemeansthataddressresolutionisinprogress
andthelink-layeraddressoftheneighborhasnotyetbeen
determined.Asolicitationrequestwassent,andtheswitchis
waitingforasolicitationreplyoratimeout.
| permanent |     |     | ShowstheARPcacheentriesthatareinpermanentstate.ARP |     |
| --------- | --- | --- | -------------------------------------------------- | --- |
entriesthatareinapermanentstatecanberemovedby
administrativeactiononly.
| reachable |     |     | ShowstheARPcacheentriesthatareinreachablestate, |     |
| --------- | --- | --- | ----------------------------------------------- | --- |
meaningthattheneighborisknowntohavebeenreachable
recently.
| stale |     |     | ShowsARPcacheentriesthatareinstalestate. |     |
| ----- | --- | --- | ---------------------------------------- | --- |
ARPcacheentriesareinthestalestateiftheelapsedtimeisin
ARP|165

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
excessoftheARPtimeoutinsecondssincethelastpositive
confirmationthattheforwardingpathwasfunctioningproperly.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
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
| show arp         | summary   |                   |            |     |     |
| ---------------- | --------- | ----------------- | ---------- | --- | --- |
| show arp summary | [all-vrfs | | vrf <VRF-NAME>] | [vsx-peer] |     |     |
Description
ShowsasummaryoftheIPv4andIPv6neighborentriesontheswitchforallVRFsoraspecificVRF.
| Parameter      |     |     | Description             |     |     |
| -------------- | --- | --- | ----------------------- | --- | --- |
| all-vrfs       |     |     | SelectsallVRFs.         |     |     |
| vrf <VRF-NAME> |     |     | SpecifiesthenameofaVRF. |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingsummaryARPinformationforallVRFs:
166
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |     |     |
| --------------------------- | ----- | ------------- | --- | --- | --- |

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
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
ARP|167

| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp         | timeout       |            |     |     |
| ---------------- | ------------- | ---------- | --- | --- |
| show arp timeout | [<INTERFACE>] | [vsx-peer] |     |     |
Description
Showstheage-outperiodforeachARP(AddressResolutionProtocol)entryforaport,LAG,orVLAN
interface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE>
Specifiesaphysicalport,VLAN,orLAGontheswitch.Forphysical
ports,usetheformatmember/slot/port(forexample,1/3/1).
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingARPtimeoutinformationforaport:
| switch#      | show arp timeout | 1/1/1 |     |     |
| ------------ | ---------------- | ----- | --- | --- |
| ARP Timeout: |                  |       |     |     |
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
| show arp           | vrf   |             |            |     |
| ------------------ | ----- | ----------- | ---------- | --- |
| show arp {all-vrfs | | vrf | <VRF-NAME>} | [vsx-peer] |     |
168
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |     |     |
| --------------------------- | ------------------- | --- | --- | --- |

Description
ShowstheARPtableforallVRFinstances,orforthenamedVRF.
| Parameter |     | Description       |     |     |
| --------- | --- | ----------------- | --- | --- |
| all-vrfs  |     | SpecifiesallVRFs. |     |     |
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
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
ARP|169

| Platforms |     | Commandcontext |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show      | ipv6      | neighbors |       |             |            |     |     |
| --------- | --------- | --------- | ----- | ----------- | ---------- | --- | --- |
| show ipv6 | neighbors | {all-vrfs | | vrf | <VRF-NAME>} | [vsx-peer] |     |     |
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
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
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
170
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- | --- |

| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Operator(>)orManager
|           | (#)       |       | forthiscommand. |     |     |
| --------- | --------- | ----- | --------------- | --- | --- |
| show ipv6 | neighbors | state |                 |     |     |
show ipv6 neighbors state {all | failed | incomplete | permanent | reachable | stale} [vsx-
peer]
Description
ShowsallIPv6neighborARP(AddressResolutionProtocol)cacheentries,orthosecacheentriesthatarein
thespecifiedstate.
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
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#      | show ipv6 neighbors | state | all |               |            |
| ------------ | ------------------- | ----- | --- | ------------- | ---------- |
| IPv6 Address |                     | MAC   |     | Port Physical | Port State |
--------------------------------------------------------------------------------
| 100::2 |     | 48:0f:cf:af:f1:cc |     | lag1 lag1    | reachable |
| ------ | --- | ----------------- | --- | ------------ | --------- |
| 300::3 |     | 48:0f:cf:af:33:be |     | vlan3 1/4/20 | reachable |
fe80::4a0f:cfff:feaf:f1cc 48:0f:cf:af:f1:cc lag1 lag1 reachable
| 200::3 |     | 48:0f:cf:af:33:be |     | 1/4/11 1/4/11 | reachable |
| ------ | --- | ----------------- | --- | ------------- | --------- |
fe80::4a0f:cfff:feaf:33be 48:0f:cf:af:33:be vlan3 1/4/20 reachable
| Total Number | Of IPv6 Neighbors |     | Entries Listed- | 5.  |     |
| ------------ | ----------------- | --- | --------------- | --- | --- |
---------------------------------------------------------------------------------
ARP|171

CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
172
| AOS-CX10.08IPServicesGuide| | (83xx SwitchSeries) |     |
| --------------------------- | ------------------- | --- |

Chapter 10
|         |      |           |       | Network | Load Balancing | (NLB) |
| ------- | ---- | --------- | ----- | ------- | -------------- | ----- |
| Network | Load | Balancing | (NLB) |         |                |       |
NetworkLoadBalancing(NLB)isaloadbalancingtechnologyforserverclustering.NLBsupportsload
sharingandredundancyamongserverswithinacluster.Toimplementfastfailover,NLBrequiresthatthe
switchforwardsnetworktraffictooneorallserversinthecluster.Eachserverfiltersouttheunexpected
traffic.Formoreinformation,seeConfiguringnetworkinfrastructuretosupporttheNLBoperationmode
NLBisusedtospreadincomingrequestsacrossasmanyas32servers.Currently,NLBinAOS-CXsupports
onlyIGMPmulticastmode.TheIGMPmulticastmodesendsthepacketsoutoftheportswhichconnectto
theclustermembers.AssignastaticmulticastMACaddresswithintheInternetAssignedNumbersAuthority
(IANA)rangetothecluster'svirtualunicastIPaddress.TheclusteredserverssendIGMPjoinstothe
configuredmulticastclustergroup.IfIGMPsnoopingisenabled,theswitchdynamicallypopulatestheIGMP
snoopingtablewiththeclusteredservers,whichpreventsunicastflooding.
NLB commands
| arp ipv4 | mac              |     |                |     |     |     |
| -------- | ---------------- | --- | -------------- | --- | --- | --- |
| arp ipv4 | <IPv4-ADDR>      | mac | <MAC-ADDR>     |     |     |     |
| no arp   | ipv4 <IPv4-ADDR> |     | mac <MAC-ADDR> |     |     |     |
Description
ConfiguresstaticARPmulticastontheinterface.
ThenoformofthiscommandremovesthestaticARPmulticastconfiguration.
| Parameter   |     |     | Description                           |     |     |     |
| ----------- | --- | --- | ------------------------------------- | --- | --- | --- |
| <IPv4-ADDR> |     |     | Specifiescluster'svirtualIPv4address. |     |     |     |
<MAC-ADDR> SpecifiesmulticastMACaddressinIANAformat(xx:xx:xx:xx:xx:xx)
andnonIANAformat(xxxx.xxxx.xxxx).
Examples
ConfiguringstaticARPmulticastonaninterface:
| switch(config)# |     | vlan | 10  |     |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- |
switch(config-vlan-10)#
no shutdown
| switch(config-vlan-10)# |     |           | ip igmp snooping | enable |     |     |
| ----------------------- | --- | --------- | ---------------- | ------ | --- | --- |
| switch(config-vlan-10)# |     |           | exit             |        |     |     |
| switch(config)#         |     | interface | vlan10           |        |     |     |
| switch(config-if-vlan)# |     |           | ip igmp enable   |        |     |     |
switch(config-if-vlan)# arp ipv4 10.1.30.254 mac 01:00:5e:7F:1E:FE
173
| AOS-CX10.08IPServicesGuide| |     | (83xx SwitchSeries) |     |     |     |     |
| --------------------------- | --- | ------------------- | --- | --- | --- | --- |

IfyourNLBVirtualIPaddressis10.1.30.254,thentheserverwilljointhe239.255.30.254IGMPgroup.ThisIGMP
groupismappedtothedestinationMACaddressof01:00:5e:7F:1E:FE.
On8320and8325:
TheclusterssendstheIGMPjointoanyvalidmulticastgroupIPaddressthatiswithintherangefrom224.0.0.0to
239.255.255.255exceptreservedgroupIPaddresses.
CommandHistory
| Release        |     | Modification                        |     |     |
| -------------- | --- | ----------------------------------- | --- | --- |
| 10.08          |     | AddedNLBsupportfor8360Switchseries. |     |     |
| 10.07orearlier |     | --                                  |     |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |     |
| --------- | -------------- | --------- | --- | --- |
8320 config-ifandconfig- Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| 8325 | if-vlan |     |     |     |
| ---- | ------- | --- | --- | --- |
8360
show arp
show arp
Description
DisplaysthestaticARPmulticastinformation.
Examples
DisplayingthestaticARPmulticastinformation:
| switch#      | show arp |      |               |       |
| ------------ | -------- | ---- | ------------- | ----- |
| IPv4 Address | MAC      | Port | Physical Port | State |
---------------------------------------------------------------------------
| 3.3.3.3      | 01:00:5e:00:00:02 |            | 1/1/1 | permanent |
| ------------ | ----------------- | ---------- | ----- | --------- |
| 2.2.2.2      | 01:00:5e:00:00:01 | vlan10     |       | permanent |
| Total Number | Of ARP Entries    | Listed- 2. |       |           |
---------------------------------------------------------------------------
CommandHistory
| Release        |     | Modification                        |     |     |
| -------------- | --- | ----------------------------------- | --- | --- |
| 10.08          |     | AddedNLBsupportfor8360Switchseries. |     |     |
| 10.07orearlier |     | --                                  |     |     |
CommandInformation
NetworkLoadBalancing(NLB)|174

| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
8320 Administratorsorlocalusergroupmemberswithexecutionrights
Operator(>)orManager
| 8325 | (#) |     |     | forthiscommand. |     |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- | --- |
8360
| show    | ip igmp snooping |                | vlan | group            |     |     |     |     |
| ------- | ---------------- | -------------- | ---- | ---------------- | --- | --- | --- | --- |
| show ip | igmp snooping    | vlan <VLAN-ID> |      | group IGMP-Group |     |     |     |     |
Description
Displaysmulticastjoins(membersofthecluster)participatingintheIGMPgroup.
Examples
DisplayingmulticastjoinsparticipatingintheIGMPgroup:
| switch# | show ip igmp             | snooping | vlan    | 10 group | 239.255.30.254 |       |           |         |
| ------- | ------------------------ | -------- | ------- | -------- | -------------- | ----- | --------- | ------- |
| VLAN    | ID : 10                  |          |         |          |                |       |           |         |
| VLAN    | Name : VLAN10            |          |         |          |                |       |           |         |
| Group   | Address : 239.255.30.254 |          |         |          |                |       |           |         |
| Last    | Reporter : 10.1.30.254   |          |         |          |                |       |           |         |
| Group   | Type : Filter            |          |         |          |                |       |           |         |
|         |                          |          |         | V1       |                | V2    | Sources   | Sources |
| Port    | Vers Mode                | Uptime   | Expires | Timer    |                | Timer | Forwarded | Blocked |
--------- ---- ---- --------- --------- --------- --------- --------- --------
| 1/1/6 | 2 EXC | 0m 21s | 1m  | 12s |     | 2m 48s | 0   | 0   |
| ----- | ----- | ------ | --- | --- | --- | ------ | --- | --- |
CommandHistory
| Release        |     |     |     | Modification                        |     |     |     |     |
| -------------- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
| 10.08          |     |     |     | AddedNLBsupportfor8360Switchseries. |     |     |     |     |
| 10.07orearlier |     |     |     | --                                  |     |     |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- | --- | --- |
8320 Operator(>)orManager Administratorsorlocalusergroupmemberswithexecutionrights
| 8325 | (#) |     |     | forthiscommand. |     |     |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- | --- | --- |
8360
175
| AOS-CX10.08IPServicesGuide| | (83xx | SwitchSeries) |     |     |     |     |     |     |
| --------------------------- | ----- | ------------- | --- | --- | --- | --- | --- | --- |

Support and Other Resources

Chapter 11

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

Airheads social forums and Knowledge
Base

https://community.arubanetworks.com/

Software licensing

https://lms.arubanetworks.com/

End-of-Life information

https://www.arubanetworks.com/support-services/end-of-life/

Aruba software and documentation

https://asp.arubanetworks.com/downloads

Accessing Updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX 10.08 IP Services Guide | (83xx Switch Series)

176

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

Support and Other Resources | 177