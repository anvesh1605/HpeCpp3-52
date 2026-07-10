AOS-CX 10.10 IP Services
Guide

6200 Switch Series

Published: October 2023

Version: 3

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

3

Contents
| About this                          | document                            | 9   |
| ----------------------------------- | ----------------------------------- | --- |
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
| IPv6RAcommands                      |                                     | 23  |
|                                     | ipv6address<global-unicast-address> | 23  |
|                                     | ipv6addressautoconfig               | 23  |
|                                     | ipv6addresslink-local               | 24  |
|                                     | ipv6ndcache-limit                   | 25  |
|                                     | ipv6nddadattempts                   | 26  |
|                                     | ipv6ndhop-limit                     | 26  |
|                                     | ipv6ndmtu                           | 27  |
|                                     | ipv6ndns-interval                   | 28  |
|                                     | ipv6ndprefix                        | 28  |
|                                     | ipv6ndradnssearch-list              | 30  |
|                                     | ipv6ndradnsserver                   | 31  |
|                                     | ipv6ndralifetime                    | 32  |
|                                     | ipv6ndramanaged-config-flag         | 32  |
|                                     | ipv6ndramax-interval                | 33  |
|                                     | ipv6ndramin-interval                | 34  |
|                                     | ipv6ndraother-config-flag           | 35  |
|                                     | ipv6ndrareachable-time              | 36  |
|                                     | ipv6ndraretrans-timer               | 36  |
|                                     | ipv6ndroute                         | 37  |
|                                     | ipv6ndrouter-preference             | 38  |
|                                     | ipv6ndsuppress-ra                   | 39  |
|                                     | showipv6ndglobaltraffic             | 40  |
|                                     | showipv6ndinterface                 | 41  |
|                                     | showipv6ndinterfaceprefix           | 43  |
|                                     | showipv6ndinterfaceroute            | 44  |
|                                     | showipv6ndradnssearch-list          | 45  |
|                                     | showipv6ndradnsserver               | 46  |
4
AOS-CX10.10IPServicesGuide| (6200SwitchSeries)

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
show dhcp-server
static-bind

DHCP server IPv6 commands

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
58
60
60
61

64
64
64
64
65
65
66
66
67
69
70
79
79
80
84
85
86
87
87
88
89
90
91
92
93
93
94
95
96
97
98
99
99
100
101
103
104
105

| 5

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

105
106
107
108
109
110
110
111
112
113
114
115
117

119
119
120
120
120
120
120
121
122
123
124
124
125
126
127
129
130
131
132
133
133
135
136
137
137
138
139
140
140
141
142
143
144
145
146
147
148
149
150
151
152
153

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

6

|                                 | showdhcpv6-snoopingguard-policyinterface  |         |          |        | 154 |
| ------------------------------- | ----------------------------------------- | ------- | -------- | ------ | --- |
|                                 | showdhcpv6-snoopingguard-policyvlan       |         |          |        | 155 |
|                                 | showdhcpv6-snoopingstatistics             |         |          |        | 156 |
| ND snooping                     |                                           |         |          |        | 157 |
| Overview                        |                                           |         |          |        | 157 |
| NDsnoopingcommands              |                                           |         |          |        | 157 |
|                                 | clearnd-snoopingbinding                   |         |          |        | 158 |
|                                 | clearnd-snoopingra-guard-policystatistics |         |          |        | 159 |
|                                 | clearnd-snoopingstatistics                |         |          |        | 159 |
|                                 | nd-snooping                               |         |          |        | 160 |
|                                 | nd-snooping(inconfig-vlancontext)         |         |          |        | 161 |
|                                 | nd-snoopingmac-check                      |         |          |        | 161 |
|                                 | nd-snoopingprefix-list                    |         |          |        | 162 |
|                                 | nd-snoopingmax-bindings                   |         |          |        | 163 |
|                                 | nd-snoopingnd-guard                       |         |          |        | 164 |
|                                 | nd-snoopingra-guard                       |         |          |        | 165 |
|                                 | nd-snoopingra-drop                        |         |          |        | 166 |
|                                 | nd-snoopingtrust                          |         |          |        | 166 |
|                                 | shownd-snooping                           |         |          |        | 167 |
|                                 | shownd-snoopingbindings                   |         |          |        | 168 |
|                                 | shownd-snoopingprefix-list                |         |          |        | 169 |
|                                 | shownd-snoopingstatistics                 |         |          |        | 170 |
| RAguardpolicycommands           |                                           |         |          |        | 171 |
|                                 | hoplimit                                  |         |          |        | 171 |
|                                 | ipv6nd-snoopingra-guardpolicy             |         |          |        | 172 |
|                                 | managed-config-flag                       |         |          |        | 173 |
|                                 | matchaccess-list                          |         |          |        | 174 |
|                                 | matchprefix-list                          |         |          |        | 175 |
|                                 | nd-snoopingra-guardattach-policy          |         |          |        | 175 |
|                                 | other-config-flag                         |         |          |        | 177 |
|                                 | router-preference                         |         |          |        | 178 |
|                                 | shownd-snoopingra-guardinterface          |         |          |        | 179 |
|                                 | shownd-snoopingra-guardpolicy             |         |          |        | 180 |
|                                 | shownd-snoopingra-guardvlan               |         |          |        | 181 |
| IPv6 destination                |                                           | guard   |          |        | 183 |
| IPv6destinationguardcommands    |                                           |         |          |        | 183 |
|                                 | clearipv6destination-guardstatisticsvlan  |         |          |        | 183 |
|                                 | ipv6destinationguard                      |         |          |        | 184 |
|                                 | showipv6destination-guardstatisticsvlan   |         |          |        | 184 |
|                                 | showipv6destination-guard                 |         |          |        | 185 |
| Internet                        | Control                                   | Message | Protocol | (ICMP) | 187 |
| ICMPmessagetypes                |                                           |         |          |        | 187 |
| WhenICMPmessagesaresent         |                                           |         |          |        | 187 |
| ICMPredirectmessages            |                                           |         |          |        | 188 |
| WhenICMPredirectmessagesaresent |                                           |         |          |        | 188 |
| ICMPcommands                    |                                           |         |          |        | 188 |
|                                 | ipicmpredirect                            |         |          |        | 188 |
|                                 | ipicmpthrottle                            |         |          |        | 189 |
|                                 | ipicmpunreachable                         |         |          |        | 190 |
| DNS                             |                                           |         |          |        | 191 |
| DNSclient                       |                                           |         |          |        | 191 |
| ConfiguringtheDNSclient         |                                           |         |          |        | 191 |
|7

| DNSclientcommands        |                             |           | 192 |
| ------------------------ | --------------------------- | --------- | --- |
|                          | ipdnsdomain-list            |           | 192 |
|                          | ipdnsdomain-name            |           | 193 |
|                          | ipdnshost                   |           | 194 |
|                          | ipdnsserveraddress          |           | 194 |
|                          | showipdns                   |           | 195 |
| ARP                      |                             |           | 197 |
| ConfiguringproxyARP      |                             |           | 198 |
| ConfiguringlocalproxyARP |                             |           | 198 |
| ARPcommands              |                             |           | 199 |
|                          | arpinspection               |           | 199 |
|                          | arpinspectiontrust          |           | 199 |
|                          | arpprocess-grat-arp         |           | 200 |
|                          | arpipv4mac                  |           | 201 |
|                          | cleararp                    |           | 202 |
|                          | iplocal-proxy-arp           |           | 203 |
|                          | ipv6neighbormac             |           | 203 |
|                          | ipproxy-arp                 |           | 204 |
|                          | showarp                     |           | 205 |
|                          | showarpinspectioninterface  |           | 206 |
|                          | showarpinspectionstatistics |           | 207 |
|                          | showarpstate                |           | 207 |
|                          | showarpsummary              |           | 209 |
|                          | showarptimeout              |           | 210 |
|                          | showarpvrf                  |           | 211 |
|                          | showipv6neighbors           |           | 212 |
|                          | showipv6neighborsstate      |           | 213 |
| Support                  | and Other                   | Resources | 215 |
| AccessingArubaSupport    |                             |           | 215 |
| AccessingUpdates         |                             |           | 216 |
|                          | ArubaSupportPortal          |           | 216 |
|                          | MyNetworking                |           | 216 |
| WarrantyInformation      |                             |           | 216 |
| RegulatoryInformation    |                             |           | 216 |
| DocumentationFeedback    |                             |           | 217 |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 8

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products

This document applies to the following products:

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

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

|

{ }

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

9

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

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
| Diagnostic-dump |             | captured | for     | feature | irdp         |     |     |
| --------------- | ----------- | -------- | ------- | ------- | ------------ | --- | --- |
| Command         | History     |          |         |         |              |     |     |
| Release         |             |          |         |         | Modification |     |     |
| 10.07orearlier  |             |          |         |         | --           |     |     |
| Command         | Information |          |         |         |              |     |     |
| Platforms       | Command     |          | context |         | Authority    |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 14

ip irdp
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
multicast Advertisementsaresentasmulticastpacketstothemulticast
groupwithIPaddress24.0.0.1.Default.
Examples
EnablingIRDPoninterfacevlan2withpackettypesettothedefaultvalue(multicast).
| switch(config)#         | interface | vlan    | 2   |
| ----------------------- | --------- | ------- | --- |
| switch(config-if-vlan)# |           | ip irdp |     |
EnablingIRDPoninterface1/1/1withpackettypesettobroadcast.
| switch(config)# | interface | vlan | 2   |
| --------------- | --------- | ---- | --- |
switch(config-if-vlan)#
|     |     | ip irdp | broadcast |
| --- | --- | ------- | --------- |
DisablingIRDP.
| switch(config)#         | interface | vlan       | 2            |
| ----------------------- | --------- | ---------- | ------------ |
| switch(config-if-vlan)# |           | no ip irdp |              |
| Command History         |           |            |              |
| Release                 |           |            | Modification |
| 10.07orearlier          |           |            | --           |
| Command Information     |           |            |              |
| Platforms               | Command   | context    | Authority    |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip irdp    | maxadvertinterval |     |        |     |     |
| ---------- | ----------------- | --- | ------ | --- | --- |
| ip irdp    | maxadvertinterval |     | <TIME> |     |     |
| no ip irdp | maxadvertinterval |     | <TIME> |     |     |
Description
Specifiesthemaximumrouteradvertisementinterval.
Thenoformofthiscommandremovesthespecifiedmaximumrouteradvertisementintervaland
revertstothedefaultvalue.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 16

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
| switch(config)# |     | interface | vlan | 2   |     |
| --------------- | --- | --------- | ---- | --- | --- |
switch(config-if-vlan)#
|                |             |     | no ip irdp | maxadvertinterval | 30  |
| -------------- | ----------- | --- | ---------- | ----------------- | --- |
| Command        | History     |     |            |                   |     |
| Release        |             |     |            | Modification      |     |
| 10.07orearlier |             |     |            | --                |     |
| Command        | Information |     |            |                   |     |
| Platforms      | Command     |     | context    | Authority         |     |
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
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
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
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
SettingtheIRDPpreferencelevelforVLANinterface2to25.
| switch(config)#         |     | interface | vlan    | 2          |     |     |
| ----------------------- | --- | --------- | ------- | ---------- | --- | --- |
| switch(config-if-vlan)# |     |           | ip irdp | preference | 25  |     |
RemovingtheIRDPpreferencelevelforVLANinterface2to25.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 18

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
Allplatforms config-if-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show ip irdp |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |
show ip irdp
Description
DisplaysIRDPconfigurationsettings.
Example
| switch# sh  | ip        | irdp |          |     |     |     |
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
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries)

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

22

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 24

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
IPv6RouterAdvertisement|25

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 26

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
IPv6RouterAdvertisement|27

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 28

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
IPv6RouterAdvertisement|29

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 30

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
IPv6RouterAdvertisement|31

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 32

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
IPv6RouterAdvertisement|33

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 34

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
IPv6RouterAdvertisement|35

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 36

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
IPv6RouterAdvertisement|37

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 38

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
IPv6RouterAdvertisement|39

| Release        |     |             |         |         |     | Modification |     |
| -------------- | --- | ----------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier |     |             |         |         |     | --           |     |
| Command        |     | Information |         |         |     |              |     |
| Platforms      |     |             | Command | context |     | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show | ipv6    | nd     | global  | traffic |     |     |     |
| ---- | ------- | ------ | ------- | ------- | --- | --- | --- |
| show | ipv6 nd | global | traffic |         |     |     |     |
Description
DisplaysIPV6NeighborDiscoverytrafficdetailsonadevice.
Examples
|                | switch#     | show           | ipv6 nd        | global  | traffic         |              |      |
| -------------- | ----------- | -------------- | -------------- | ------- | --------------- | ------------ | ---- |
|                | ICMPv6      | packet         | Statistics     |         | (sent/received) |              |      |
|                | Total       | Messages       |                |         |                 | :            | 18/0 |
|                | Error       | Messages       |                |         |                 | :            | 0/0  |
|                | Destination |                | Unreachables   |         |                 | :            | 0/0  |
|                | Time        | Exceeded       |                |         |                 | :            | 0/0  |
|                | Parameter   |                | Problems       |         |                 | :            | 0/0  |
|                | Echo        | Request        |                |         |                 | :            | 0/0  |
|                | Echo        | Replies        |                |         |                 | :            | 0/0  |
|                | Redirects   |                |                |         |                 | :            | 0/0  |
|                | Packet      | Too            | Big            |         |                 | :            | 0/0  |
|                | Router      | Advertisements |                |         |                 | :            | 4/0  |
|                | Router      | Solicitations  |                |         |                 | :            | 0/0  |
|                | Neighbor    |                | Advertisements |         |                 | :            | 0/0  |
|                | Neighbor    |                | Solicitations  |         |                 | :            | 3/0  |
|                | Duplicate   |                | router         | RA      | received        | :            | 0/0  |
|                | ICMPv6      | MLD            | Statistics     |         | (sent/received) |              |      |
|                | V1          | Queries        | :              |         | 0/0             |              |      |
|                | V2          | Queries        | :              |         | 0/0             |              |      |
|                | V1          | Reports        | :              |         | 0/0             |              |      |
|                | V2          | Reports        | :              |         | 11/0            |              |      |
|                | V1          | Leaves         | :              |         | 0/0             |              |      |
| Command        |             | History        |                |         |                 |              |      |
| Release        |             |                |                |         |                 | Modification |      |
| 10.07orearlier |             |                |                |         |                 | --           |      |
| Command        |             | Information    |                |         |                 |              |      |
| Platforms      |             |                | Command        | context |                 | Authority    |      |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 40

| show | ipv6    | nd        | interface  |     |     |            |                   |     |
| ---- | ------- | --------- | ---------- | --- | --- | ---------- | ----------------- | --- |
| show | ipv6 nd | interface | [<IF-NAME> |     |     | | all-vrfs | | vrf <VRF-NAME>] |     |
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
Examples
ShowinginformationforallVRFs:
|     | switch# show         | ipv6                 | nd        | interface   |                              | all-vrfs |             |         |
| --- | -------------------- | -------------------- | --------- | ----------- | ---------------------------- | -------- | ----------- | ------- |
|     | List of IPv6         | Interfaces           |           | for         | VRF                          | default  |             |         |
|     | Interface            | 1/1/1                | is up     |             |                              |          |             |         |
|     | Admin state          | is                   | up        |             |                              |          |             |         |
|     | IPv6 address:        |                      |           |             |                              |          |             |         |
|     | IPv6 link-local      |                      | address:  |             | fe80::7272:cfff:fee7:a8b9/64 |          |             | [VALID] |
|     | ICMPv6 active        |                      | timers:   |             |                              |          |             |         |
|     | Last                 | Router-Advertisement |           |             |                              | sent:    |             |         |
|     | Next                 | Router-Advertisement |           |             |                              | sent in: |             |         |
|     | Router-Advertisement |                      |           | parameters: |                              |          |             |         |
|     | Periodic             |                      | interval: | 200         | to                           | 600 secs |             |         |
|     | Router               | Preference:          |           | medium      |                              |          |             |         |
|     | Send                 | "Managed             | Address   |             | Configuration"               |          | flag: false |         |
|     | Send                 | "Other               | Stateful  |             | Configuration"               |          | flag: false |         |
|     | Send                 | "Current             | Hop       | Limit"      |                              | field:   | 64          |         |
|     | Send                 | "MTU"                | option    | value:      |                              | 1500     |             |         |
|     | Send                 | "Router              | Lifetime" |             | field:                       | 1800     |             |         |
|     | Send                 | "Reachable           |           | Time"       | field:                       | 0        |             |         |
|     | Send                 | "Retrans             | Timer"    |             | field:                       | 0        |             |         |
|     | Suppress             |                      | RA: true  |             |                              |          |             |         |
|     | Suppress             |                      | MTU in    | RA:         | true                         |          |             |         |
|     | ICMPv6 error         |                      | message   | parameters: |                              |          |             |         |
|     | Send                 | redirects:           |           | false       |                              |          |             |         |
|     | ICMPv6 DAD           | parameters:          |           |             |                              |          |             |         |
|     | Current              | DAD                  | attempt:  |             | 1                            |          |             |         |
|     | List of IPv6         | Interfaces           |           | for         | VRF                          | red      |             |         |
|     | Interface            | 1/1/2                | is up     |             |                              |          |             |         |
|     | Admin state          | is                   | up        |             |                              |          |             |         |
|     | IPv6 address:        |                      |           |             |                              |          |             |         |
|     | 2001::1/64           |                      | [VALID]   |             |                              |          |             |         |
|     | IPv6 link-local      |                      | address:  |             | fe80::7272:cfff:fee7:a8b9/64 |          |             | [VALID] |
|     | ICMPv6 active        |                      | timers:   |             |                              |          |             |         |
|     | Last                 | Router-Advertisement |           |             |                              | sent:    |             |         |
|     | Next                 | Router-Advertisement |           |             |                              | sent in: |             |         |
IPv6RouterAdvertisement|41

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
| Admin     | state   | is         | up    |           |     |         |     |     |
IPv6 address:
|                      | 2001::1/64 |                      | [VALID]   |             |                              |          |        |         |
| -------------------- | ---------- | -------------------- | --------- | ----------- | ---------------------------- | -------- | ------ | ------- |
| IPv6                 | link-local |                      | address:  |             | fe80::7272:cfff:fee7:a8b9/64 |          |        | [VALID] |
| ICMPv6               | active     |                      | timers:   |             |                              |          |        |         |
|                      | Last       | Router-Advertisement |           |             |                              | sent: 6  | Secs   |         |
|                      | Next       | Router-Advertisement |           |             |                              | sent in: | 7 Secs |         |
| Router-Advertisement |            |                      |           | parameters: |                              |          |        |         |
|                      | Periodic   |                      | interval: | 3           | to 13                        | secs     |        |         |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 42

|                | Router      | Preference:     |              |             | medium         |              |             |
| -------------- | ----------- | --------------- | ------------ | ----------- | -------------- | ------------ | ----------- |
|                | Send        | "Managed        |              | Address     | Configuration" |              | flag: false |
|                | Send        | "Other          | Stateful     |             | Configuration" |              | flag: false |
|                | Send        | "Current        |              | Hop         | Limit"         | field: 64    |             |
|                | Send        | "MTU"           | option       |             | value:         | 1500         |             |
|                | Send        | "Router         |              | Lifetime"   | field:         | 1900         |             |
|                | Send        | "Reachable      |              | Time"       | field:         | 0            |             |
|                | Send        | "Retrans        |              | Timer"      | field:         | 0            |             |
|                | Suppress    |                 | RA:          | true        |                |              |             |
|                | Suppress    |                 | MTU          | in RA:      | true           |              |             |
| ICMPv6         |             | error           | message      | parameters: |                |              |             |
|                | Send        | redirects:      |              | false       |                |              |             |
| ICMPv6         |             | DAD parameters: |              |             |                |              |             |
|                | Current     |                 | DAD attempt: |             | 1              |              |             |
| Command        | History     |                 |              |             |                |              |             |
| Release        |             |                 |              |             |                | Modification |             |
| 10.07orearlier |             |                 |              |             |                | --           |             |
| Command        | Information |                 |              |             |                |              |             |
| Platforms      |             | Command         |              | context     |                | Authority    |             |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show      | ipv6 | nd        | interface |        | prefix    |     |                 |
| --------- | ---- | --------- | --------- | ------ | --------- | --- | --------------- |
| show ipv6 | nd   | interface |           | prefix | [all-vrfs | |   | vrf <VRF-NAME>] |
Description
ShowsIPv6prefixinformationforallVRFsoraspecificVRF.Ifnooptionsarespecified,shows
informationforthedefaultVRF.
| Parameter      |     |     |     |     |     | Description                       |     |
| -------------- | --- | --- | --- | --- | --- | --------------------------------- | --- |
| all-vrfs       |     |     |     |     |     | ShowsprefixinformationforallVRFs. |     |
| vrf <VRF-NAME> |     |     |     |     |     | NameofaVRF.                       |     |
Examples
ShowingprefixinformationforthedefaultVRF:
| switch# | show      | ipv6        | nd  | interface  |         | prefix   |     |
| ------- | --------- | ----------- | --- | ---------- | ------- | -------- | --- |
| List    | of IPv6   | Interfaces  |     |            | for VRF | default  |     |
| List    | of IPv6   | Prefix      |     | advertised |         | on 1/1/1 |     |
|         | Prefix    | : 4545::/65 |     |            |         |          |     |
|         | Enabled   | : Yes       |     |            |         |          |     |
|         | Validlife | time        | :   | 2592000    |         |          |     |
IPv6RouterAdvertisement|43

|     | Preferred  | lifetime | :   | 604800 |     |     |
| --- | ---------- | -------- | --- | ------ | --- | --- |
|     | On-link    | : Yes    |     |        |     |     |
|     | Autonomous | :        | Yes |        |     |     |
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
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | ipv6    | nd interface |       | route     |       |             |
| ---- | ------- | ------------ | ----- | --------- | ----- | ----------- |
| show | ipv6 nd | interface    | route | [all-vrfs | | vrf | <VRF-NAME>] |
Description
DisplaysrouteinformationofallinterfacesinthedefaultVRF.
| Parameter |     |     | Description                                  |     |     |     |
| --------- | --- | --- | -------------------------------------------- | --- | --- | --- |
| all-vrfs  |     |     | DisplaysinformationaboutinterfacesinallVRFs. |     |     |     |
vrf <VRF-NAME> DisplaysinformationaboutinterfacesinaparticularVRF.Or,if<VRF-NAME>isnot
specified,displaysinformationforthedefaultVRF.
Examples
Showingroutinginformationforinterface1/1/1inthedefaultVRF:
|     | switch# | show ipv6       | nd interface |         | route   |     |
| --- | ------- | --------------- | ------------ | ------- | ------- | --- |
|     | List of | IPv6 Interfaces |              | for VRF | default |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 44

List of IPv6 Routes advertised on 1/1/1

Route : 1::/64
Enabled : Yes
Route lifetime : 200
Route preference : high

Showing routing information for interface 1/1/1 in VRF red:

switch# show ipv6 nd interface route vrf red

List of IPv6 Interfaces for VRF red
List of IPv6 Routes advertised on 1/1/2

Route : 2::/64
Enabled : No
Route lifetime : 1800
Route preference : low

Command History

Release

10.10

Command Information

Modification

Command introduced

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

lifetime

1800

Command History

Release

10.07 or earlier

Modification

--

IPv6 Router Advertisement | 45

| Command   |     | Information |     |         |     |           |     |
| --------- | --- | ----------- | --- | ------- | --- | --------- | --- |
| Platforms |     | Command     |     | context |     | Authority |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | ipv6 | nd    | ra         | dns | server |     |     |
| ---- | ---- | ----- | ---------- | --- | ------ | --- | --- |
| show | ipv6 | nd ra | dns server |     |        |     |     |
Description
DisplaysDNSserverinformationonallinterfaces.
Examples
| switch(config)#    |          |             | interface |         | 1/1/1 |              |         |
| ------------------ | -------- | ----------- | --------- | ------- | ----- | ------------ | ------- |
| switch(config-if)# |          |             |           | ipv6    | nd ra | dns server   | 2001::1 |
| switch#            |          | show        | ipv6      | nd ra   | dns   | server       |         |
| Recursive          |          | DNS         | Server    | List    | on:   | 1            |         |
|                    | Suppress |             | DNS       | Server  | List: | Yes          |         |
|                    | DNS      | Server      | 1:        | 2001::1 |       | lifetime     | 1800    |
| Command            |          | History     |           |         |       |              |         |
| Release            |          |             |           |         |       | Modification |         |
| 10.07orearlier     |          |             |           |         |       | --           |         |
| Command            |          | Information |           |         |       |              |         |
| Platforms          |          | Command     |           | context |       | Authority    |         |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 46

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

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

n sFlow is not configurable via SNMP

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
n ConfiguresansFlowcollectorwiththeIPaddress10.10.20.209.
n EnablesthesFlowagentonallinterfaces.
n DefinesthesFlowagentIPaddresstobe10.10.1.5.
switch(config)#
|                 | sflow collector | 10.10.20.209 |     |     |     |
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 49

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 51

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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 53

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
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
| Command History |     |                |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 55

| Release             |         |         | Modification |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Settingtheheadersizetothedefaultvalueof128bytes:
| switch(config)# | no  | sflow header-size |     |
| --------------- | --- | ----------------- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 57

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow max-datagram-size
| sflow max-datagram-size    |     | <SIZE>   |     |
| -------------------------- | --- | -------- | --- |
| no sflow max-datagram-size |     | [<SIZE>] |     |
Description
SetsthemaximumnumberofbytesthataresentinonesFlowdatagram.
Thenoformofthiscommandsetsmaximumnumberofbytestothedefaultvalueof1400.
| Parameter         |        |     | Description |
| ----------------- | ------ | --- | ----------- |
| max-datagram-size | <SIZE> |     |             |
Specifiesthemaximumdatagramsizeinbytes.Range:1to9000.
Default:1400.
Examples
Settingthedatagramsizeto1000bytes:
switch(config)#
|     | sflow | max-datagram-size | 1000 |
| --- | ----- | ----------------- | ---- |
Settingtheheadersizetothedefaultvalueof1400bytes:
| switch(config)#     | no      | sflow max-datagram-size |              |
| ------------------- | ------- | ----------------------- | ------------ |
| Command History     |         |                         |              |
| Release             |         |                         | Modification |
| 10.07orearlier      |         |                         | --           |
| Command Information |         |                         |              |
| Platforms           | Command | context                 | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
sflow mode
sFlow|58

| sflow mode | {ingress      | |   | egress   | | both} |       |
| ---------- | ------------- | --- | -------- | ------- | ----- |
| no sflow   | mode {ingress |     | | egress | |       | both} |
Description
SetsthesFlowsamplingmode.Thedefaultmodeisingress.
Thenoformofthecommandsetsthesamplingmodetoingress.Executingthenoformofthe
commandwiththeingressoptionwillhavenoimpactasingressisthedefaultmode.
| Parameter |     |     |     |     | Description                |
| --------- | --- | --- | --- | --- | -------------------------- |
| ingress   |     |     |     |     | Samplesonlyingresstraffic. |
egress
Samplesonlyegresstraffic.
| both |     |     |     |     | Samplesbothingressandegresstraffic. |
| ---- | --- | --- | --- | --- | ----------------------------------- |
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
| switch#         | configure   |     | terminal |             |              |
| --------------- | ----------- | --- | -------- | ----------- | ------------ |
| switch(config)# |             | no  | sflow    | mode egress |              |
| Command         | History     |     |          |             |              |
| Release         |             |     |          |             | Modification |
| 10.07orearlier  |             |     |          |             | --           |
| Command         | Information |     |          |             |              |
| Platforms       | Command     |     | context  |             | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 59

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
| switch(config)#     | no      | sflow polling |              |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
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
sFlow|60

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
switch(config)#
|     |     | sflow | sampling | 1000 |
| --- | --- | ----- | -------- | ---- |
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
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show       | sflow      |     |                   |     |
| ---------- | ---------- | --- | ----------------- | --- |
| show sflow | [interface |     | <INTERFACE-NAME>] |     |
Description
ShowssFlowconfigurationsettingsandstatisticsforallinterfaces,orforaspecificinterface.Italso
displaysthecurrentstatusofsFlowonthedeviceandreportsanyerrorsthatrequireattention.
IfsFlowisenabledontheinterfacesassociatedwithalaginterface,thentheinterfaceswillnotbeshownas
separateentriesundersFlow enabled on Interfaceintheoutput.Onlytheassociatedlaginterfacewillhave
anentryinthecolumn.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 61

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
Allplatforms Administratorsorlocalusergroupmemberswithexecution
Manager(#)
rightsforthiscommand.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 63

Chapter 5

DHCP

DHCP

The Dynamic Host Configuration Protocol (DHCP) enables the automatic assignment of IP addresses and
other configuration settings to network devices.

The DHCP relay agent acts an intermediary, forwarding DHCP requests/response between DHCP
clients/servers on different networks. This enables DHCP clients to use the services of DHCP servers that
are not on the same subnet on which they are located.

DHCP client

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

switch(config)# interface vlan 1
switch(config-if-vlan)# ip dhcp
switch(config-if-vlan)# no shutdown

Disabling the DHCP client on the interface vlan 1:

switch(config)# interface vlan 1
switch(config-if-vlan)# no ip dhcp

If the interface is not enabled, you can enable it by entering the no shutdown command.

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

64

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
| vlan1               | 10.254.239.10/27 |         |                    | domain.com | default 50.0.0.2, |
| ------------------- | ---------------- | ------- | ------------------ | ---------- | ----------------- |
| 50.0.0.3,           | 50.0.0.4         |         |                    |            |                   |
| Command History     |                  |         |                    |            |                   |
| Release             |                  |         | Modification       |            |                   |
| 10.09orearlier      |                  |         | Commandintroduced. |            |                   |
| Command Information |                  |         |                    |            |                   |
| Platforms           | Command          | context | Authority          |            |                   |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| DHCP relay | agent |     |     |     |     |
| ---------- | ----- | --- | --- | --- | --- |
ThefunctionoftheDHCPrelayagentistoforwardtheDHCPmessagestoothersubnetssothatthe
DHCPserverdoesnothavetobeonthesamesubnetastheDHCPclients.TheDHCPrelayagent
DHCP|65

transfers DHCP messages from the DHCP clients located on a subnet without a DHCP server, to other
subnets. It also relays answers from DHCP servers to DHCP clients.

Supported interfaces

The DHCP relay agent is supported on layer 3 VLAN interfaces, and LAG interfaces. DHCP relay is not
supported on the management interface.

DHCPv4 relay agent

Hop count in DHCP requests

When a DHCP client broadcasts request, the DHCP relay agent in the switch receives the packets and
forwards them to the DHCP server as unicast requests. During this process, the DHCP relay agent
increments the hop count before forwarding DHCP packets to the server. The DHCP server, in turn,
includes the hop count in the DHCP header in the response sent back to a DHCP client.

DHCP relay option 82

Option 82 is called the relay agent information option. When a DHCP relay agent forwards client-
originated DHCP packets to a DHCP server, the option 82 field is inserted/replaced, or the packet with
this option is dropped. Servers recognizing the relay agent information option may use the information
to implement policies for the assignment of IP addresses and other parameters. The relay agent relays
the server-to-client replies to the client.

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

When configuring a bootp-gateway, dhcp-smart-relay will be ineffective. This can occur with dhcp-relay as well.

Configuring the DHCPv4 relay agent

Prerequisites

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

66

5. Ifrequired,enablethehopcountincrementfeaturewiththecommanddhcp-relay hop-count-
increment.
6. ReviewDHCPv4relayagentconfigurationsettingswiththecommandsshow dhcp-relay,show ip
|     | helper-address,andshow |     |     |     | dhcp-relay | bootp-gateway. |     |     |
| --- | ---------------------- | --- | --- | --- | ---------- | -------------- | --- | --- |
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablestheDHCPv4relayagent.
n Enablesinterface1/1/1andassignsanIPv4addresstoit.(Bydefault,allinterfacesarelayer3and
disabled.)
n DefinesanIPhelperaddressof10.10.20.209ontheinterface.
n EnablesDHCPoption82supportandreplacesalloption82informationwiththevaluesfromthe
switchwiththeswitchMACaddressastheremoteID.
On4100i,6000and6100seriesswitches,onlySVIsaresupported.
|     | switch(config)#         |             | dhcp-relay |      |                   |                 |              |     |
| --- | ----------------------- | ----------- | ---------- | ---- | ----------------- | --------------- | ------------ | --- |
|     | switch(config)#         |             | interface  |      | 1/1/1             |                 |              |     |
|     | switch(config-if)#      |             |            | vlan | access            | 100             |              |     |
|     | switch(config-if)#      |             |            | exit |                   |                 |              |     |
|     | switch(config)#         |             | interface  |      | vlan              | 100             |              |     |
|     | switch(config-if-vlan)# |             |            |      | ip address        | 198.51.100.1/24 |              |     |
|     | switch(config-if-vlan)# |             |            |      | ip helper-address |                 | 10.10.20.209 |     |
|     | switch(config-if)#      |             |            | exit |                   |                 |              |     |
|     | switch(config)#         |             | dhcp-relay |      | option            | 82 replace      | mac          |     |
|     | switch#                 | show        | dhcp-relay |      |                   |                 |              |     |
|     | DHCP Relay              | Agent       |            |      |                   | : enabled       |              |     |
|     | DHCP Request            |             | Hop Count  |      | Increment         | : enabled       |              |     |
|     | Option                  | 82          |            |      |                   | : disabled      |              |     |
|     | Source-Interface        |             |            |      |                   | : disabled      |              |     |
|     | Response                | Validation  |            |      |                   | : disabled      |              |     |
|     | Option                  | 82 Handle   | Policy     |      |                   | : replace       |              |     |
|     | Remote                  | ID          |            |      |                   | : mac           |              |     |
|     | DHCP Relay              | Statistics: |            |      |                   |                 |              |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|     | 60         |        | 10  |                |     | 60  |     | 10  |
| --- | ---------- | ------ | --- | -------------- | --- | --- | --- | --- |
|     | DHCP Relay | Option |     | 82 Statistics: |     |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
|        | 50    |          | 8   |     |     | 50  |     | 8   |
| ------ | ----- | -------- | --- | --- | --- | --- | --- | --- |
| DHCPv4 | relay | scenario |     | 1   |     |     |     |     |
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
DHCP|67

Procedure
1. DHCPrelayisenabledbydefault.Ifitwaspreviouslydisabled,enableit.
| switch#         | config |            |     |     |     |     |
| --------------- | ------ | ---------- | --- | --- | --- | --- |
| switch(config)# |        | dhcp-relay |     |     |     |     |
2. DefineanIPv4helperaddressoninterfacevlan100
| switch(config)#    |     | interface | 1/1/1       |     |     |     |
| ------------------ | --- | --------- | ----------- | --- | --- | --- |
| switch(config-if)# |     |           | vlan access | 100 |     |     |
| switch(config-if)# |     |           | exit        |     |     |     |
| switch(config)#    |     | interface | 1/1/2       |     |     |     |
| switch(config-if)# |     |           | vlan access | 100 |     |     |
| switch(config-if)# |     |           | exit        |     |     |     |
| switch(config)#    |     | interface | vlan        | 100 |     |     |
switch(config-if-vlan)#
|                         |     |     | ip address        | 192.168.2.11/24 |             |     |
| ----------------------- | --- | --- | ----------------- | --------------- | ----------- | --- |
| switch(config-if-vlan)# |     |     | ip helper-address |                 | 192.168.1.1 |     |
3. VerifyDHCPrelayconfiguration.
switch#
show dhcp-relay
| DHCP Relay       | Agent       |           |           | : enabled  |     |     |
| ---------------- | ----------- | --------- | --------- | ---------- | --- | --- |
| DHCP Request     |             | Hop Count | Increment | : enabled  |     |     |
| Option           | 82          |           |           | : disabled |     |     |
| Source-Interface |             |           |           | : disabled |     |     |
| Response         | Validation  |           |           | : disabled |     |     |
| Option           | 82 Handle   | Policy    |           | : replace  |     |     |
| Remote           | ID          |           |           | : mac      |     |     |
| DHCP Relay       | Statistics: |           |           |            |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
-------------- ---------------- --------------- -----------------
| 60         |        | 10  |                | 60  |     | 10  |
| ---------- | ------ | --- | -------------- | --- | --- | --- |
| DHCP Relay | Option |     | 82 Statistics: |     |     |     |
Valid Requests Dropped Requests Valid Responses Dropped Responses
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 68

-------------- ---------------- --------------- -----------------
|        | 50              |                   | 8         |      |                   | 50  |                   | 8   |
| ------ | --------------- | ----------------- | --------- | ---- | ----------------- | --- | ----------------- | --- |
|        | switch(config)# |                   |           | show | ip helper-address |     |                   |     |
|        | IP              | Helper            | Addresses |      |                   |     |                   |     |
|        | Interface:      |                   | vlan100   |      |                   |     |                   |     |
|        |                 | IP Helper         | Address   |      |                   |     | VRF               |     |
|        |                 | ----------------- |           |      |                   |     | ----------------- |     |
|        |                 | 192.168.1.1       |           |      |                   |     | default           |     |
| DHCPv4 | relay           | scenario          | 2         |      |                   |     |                   |     |
Inthisscenario,hostonswitch1reachestheDHCPserveronswitchtwoviaaLAG.Thephysical
topologyofthenetworklookslikethis:
Procedure
1. Onswitch1:
|     | a. CreateLAG100andassignanIPaddresstoit. |        |     |           |             |             |              |     |
| --- | ---------------------------------------- | ------ | --- | --------- | ----------- | ----------- | ------------ | --- |
|     | switch#                                  | config |     |           |             |             |              |     |
|     | switch(config)#                          |        |     | interface | lag         | 100         |              |     |
|     | switch(config-lag-if)#                   |        |     |           | no shutdown |             |              |     |
|     | switch(config-lag-if)#                   |        |     |           | vlan        | access      | 200          |     |
|     | switch(config-lag-if)#                   |        |     |           | lacp        | mode active |              |     |
|     | switch(config-lag-if)#                   |        |     |           | exit        |             |              |     |
|     | switch(config)#                          |        |     | interface | vlan        | 200         |              |     |
|     | switch(config-if-vlan)#                  |        |     |           | ip address  |             | 10.0.10.1/24 |     |
b. AssignanIPaddresstointerfacevlan100andanIPhelperaddresstoreachtheDHCPserver.
|     | switch(config)#         |     |     | interface | 1/1/1             |     |            |     |
| --- | ----------------------- | --- | --- | --------- | ----------------- | --- | ---------- | --- |
|     | switch(config-if)#      |     |     | no        | shutdown          |     |            |     |
|     | switch(config-if)#      |     |     | vlan      | access            | 100 |            |     |
|     | switch(config-if)#      |     |     | exit      |                   |     |            |     |
|     | switch(config)#         |     |     | interface | vlan              | 100 |            |     |
|     | switch(config-if-vlan)# |     |     |           | ip address        |     | 20.0.0.1/8 |     |
|     | switch(config-if-vlan)# |     |     |           | ip helper-address |     | 9.0.0.2    |     |
DHCP|69

c. Assigninterfaces1/1/2and1/1/3toLAG100.
| switch(config-if)# | interface |     | 1/1/2 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | interface |     | 1/1/3 |     |
switch(config-if)#
lag 100
d. Createaroutebetween10.0.10.2and9.0.0.0.
| switch(config)# | ip route | 9.0.0.0/24 |     | 10.0.10.2 |
| --------------- | -------- | ---------- | --- | --------- |
2. Onswitch2:
a. CreateLAG100andassignanIPaddresstoit.
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
c. Assigninterfaces1/1/2and1/1/3toLAG100.
| switch(config-if)# | interface |     | 1/1/2 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 100 |       |     |
| switch(config-if)# | interface |     | 1/1/3 |     |
| switch(config-if)# | lag       | 100 |       |     |
d. Createaroutebetween20.0.0.0and10.0.10.1.
| switch(config)# | ip route | 20.0.0.0/8 |     | 10.0.10.1 |
| --------------- | -------- | ---------- | --- | --------- |
DHCPv4 relay commands
dhcp-relay
dhcp-relay
no dhcp-relay
Description
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 70

EnablesDHCPrelaysupport.DHCPrelayisenabledbydefault.DHCPrelayisnotsupportedonthe
managementinterface.
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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
DHCP|71

| Release        |             |     |         | Modification |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
source-interface
ConfigurestheDHCPrelaytouseaconfiguredsourceIPaddress
forinter-VRFserverreachability.SetthesourceIPaddresswith
thecommandip source-interface.
ip
UsetheIPaddressoftheinterfaceonwhichtheclientDHCP
packetenteredtheswitchastheoption82remoteID.
| mac |     |     |     | UsetheMACaddressoftheswitchastheoption82remoteID. |     |
| --- | --- | --- | --- | ------------------------------------------------- | --- |
Default.
Example
ThisexampleenablesDHCPoption82supportandreplacesalloption82informationwiththevalues
fromtheswitch,withtheswitchMACaddressastheremoteID.
| switch(config)# |     | dhcp-relay | option | 82 replace mac |     |
| --------------- | --- | ---------- | ------ | -------------- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 72

| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
config
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
| diag-dump | dhcp-relay | basic |     |
| --------- | ---------- | ----- | --- |
| diag-dump | dhcp-relay | basic |     |
DHCP|73

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 74

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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip bootp-gateway
| ip bootp-gateway    |     | <IPV4-ADDR> |     |     |     |     |     |     |     |     |
| ------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| no ip bootp-gateway |     | <IPV4-ADDR> |     |     |     |     |     |     |     |     |
Description
ConfiguresagatewayaddressfortheDHCPrelayagenttouseforDHCPrequests.BydefaultDHCP
relayagentpicksthelowest-numberedIPaddressontheinterface.
Thenoformofthiscommandremovesthegatewayaddress.
| Parameter |     |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
<IPV4-ADDR> SpecifiestheIPaddressofthegatewayinIPv4format(x.x.x.x),
wherexisaisadecimalnumberfrom0to255.
Examples
SettingtheIPaddressofthegatewayforinterfacevlan100to10.10.10.10:
DHCP|75

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
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ip helper-address
| ip helper-address    |     | <IPV4-ADDR> |     | [vrf <VRF-NAME>] |     |
| -------------------- | --- | ----------- | --- | ---------------- | --- |
| no ip helper-address |     | <IPV4-ADDR> |     | [vrf <VRF-NAME>] |     |
Description
DefinestheaddressofaremoteDHCPserverorDHCPrelayagent.Uptoeightaddressescanbe
defined.TheDHCPagentforwardsDHCPclientrequeststoalldefinedservers.
ThiscommandrequiresthatyoudefineasourceIPaddressforDHCPrelaywiththecommand ip
source-interface.TheconfiguredsourceIPontheVRFisusedtoforwardDHCPpacketstotheserver.
AhelperaddresscannotbedefinedontheOOBMinterface.
ThenoformofthiscommandremovesanIPhelperaddress.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
helper-address <IPV4-ADDR> SpecifiesthehelperIPaddressinIPv4format(x.x.x.x),wherex
isadecimalnumberfrom0to255.
vrf <VRF-NAME>
SpecifiesthenameofaVRF.Default:default.
Examples
DefiningtheIPhelperaddress10.10.10.209oninterfacevlan100:
| switch(config)#         |     | interface |     | vlan100        |              |
| ----------------------- | --- | --------- | --- | -------------- | ------------ |
| switch(config-if-vlan)# |     |           | ip  | helper-address | 10.10.10.209 |
RemovingtheIPhelperaddress10.10.10.209oninterfacevlan100:
| switch(config-if-vlan)# |     |     | no  | ip helper-address | 10.10.10.209 |
| ----------------------- | --- | --- | --- | ----------------- | ------------ |
| Command History         |     |     |     |                   |              |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 76

| Release        |             |     |         | Modification |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| 50             |             | 8   |         | 50           | 8   |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| Command        | History     |     |         |              |     |
| Release        |             |     |         | Modification |     |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
DHCP|77

| Platforms | Command | context |     |     | Authority |
| --------- | ------- | ------- | --- | --- | --------- |
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
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
interface <INTERFACE-ID> Specifiesaninterface.Format:member/slot/port.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 78

Examples
ShowingtheIPhelperaddressesforallinterfaces:
switch(config)#
|     |                   |           | show | ip helper-address |     |                   |     |
| --- | ----------------- | --------- | ---- | ----------------- | --- | ----------------- | --- |
|     | IP Helper         | Addresses |      |                   |     |                   |     |
|     | Interface:        | vlan11    |      |                   |     |                   |     |
|     | IP Helper         | Address   |      |                   |     | VRF               |     |
|     | ----------------- |           |      |                   |     | ----------------- |     |
|     | 10.10.10.209      |           |      |                   |     | default           |     |
|     | Interface:        | vlan20    |      |                   |     |                   |     |
|     | IP Helper         | Address   |      |                   |     | VRF               |     |
|     | ----------------- |           |      |                   |     | ----------------- |     |
|     | 3.3.3.3           |           |      |                   |     | default           |     |
|     | 20.20.20.20       |           |      |                   |     | default           |     |
ShowingtheIPhelperaddressesforinterfacevlan20:
|                | switch(config)#   |             | show | ip helper-address |                                                      | interface         | vlan20 |
| -------------- | ----------------- | ----------- | ---- | ----------------- | ---------------------------------------------------- | ----------------- | ------ |
|                | IP Helper         | Addresses   |      |                   |                                                      |                   |        |
|                | Interface:        | vlan20      |      |                   |                                                      |                   |        |
|                | IP Helper         | Address     |      |                   |                                                      | VRF               |        |
|                | ----------------- |             |      |                   |                                                      | ----------------- |        |
|                | 3.3.3.3           |             |      |                   |                                                      | default           |        |
|                | 20.20.20.20       |             |      |                   |                                                      | default           |        |
| Command        |                   | History     |      |                   |                                                      |                   |        |
| Release        |                   |             |      |                   | Modification                                         |                   |        |
| 10.07orearlier |                   |             |      |                   | --                                                   |                   |        |
| Command        |                   | Information |      |                   |                                                      |                   |        |
| Platforms      |                   | Command     |      | context           | Authority                                            |                   |        |
| 6200           |                   |             |      |                   | OperatorsorAdministratorsorlocalusergroupmemberswith |                   |        |
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| DHCPv6 |       | relay    | agent |     |     |     |     |
| ------ | ----- | -------- | ----- | --- | --- | --- | --- |
| DHCPv6 | relay | scenario |       | 1   |     |     |     |
Inthisscenario,DHCPrelayontheserverenablestwohoststoobtaintheirIPaddressesfromaDHCP
serveronadifferentsubnet.Thephysicaltopologyofthenetworklookslikethis:
DHCP|79

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
| DHCPv6 Relay                                   | Agent :             | enabled  |     |             |
| ---------------------------------------------- | ------------------- | -------- | --- | ----------- |
| Option 79                                      | :                   | disabled |     |             |
| switch# show                                   | ipv6 helper-address |          |     |             |
| Interface:                                     | 1/1/1               |          |     |             |
| IPv6 Helper                                    | Address             |          |     | Egress Port |
| ---------------------------------------------- |                     |          |     | ----------- |
| 2001::1                                        |                     |          |     | 1/1/3       |
| Interface:                                     | 1/1/2               |          |     |             |
| IPv6 Helper                                    | Address             |          |     | Egress Port |
| --------------------------------------------   |                     |          |     | ----------- |
| 2001::1                                        |                     |          |     | 1/1/3       |
| DHCP relay (IPv6)                              | commands            |          |     |             |
dhcpv6-relay
dhcpv6-relay
no dhcpv6-relay
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 80

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
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
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
DHCP|81

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

Administrators or local user group members with execution
rights for this command.

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

82

switch(config-if)# no ipv6 helper-address multicast 2001:DB8:0:0:0:0:0:1 egress
1/1/2
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
DHCP|83

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
interface <INTERFACE-ID> Specifiesaninterface.Format:member/slot/port.
Examples
| switch# show                                   | ipv6 helper-address |         |              |             |
| ---------------------------------------------- | ------------------- | ------- | ------------ | ----------- |
| Interface:                                     | 1/1/1               |         |              |             |
| IPv6 Helper                                    | Address             |         |              | Egress Port |
| ---------------------------------------------- |                     |         |              | ----------- |
| 2001:db8:0:1::                                 |                     |         |              | -           |
| FF01::1:1000                                   |                     |         |              | 1/1/2       |
| Interface:                                     | 1/1/2               |         |              |             |
| IPv6 Helper                                    | Address             |         |              | Egress Port |
| --------------------------------------------   |                     |         |              | ----------- |
| 2001:db8:0:1::                                 |                     |         |              | -           |
| switch# show                                   | ipv6 helper-address |         | interface    | 1/1/1       |
| Interface:                                     | 1/1/1               |         |              |             |
| IPv6 Helper                                    | Address             |         |              | Egress Port |
| ---------------------------------------------- |                     |         |              | ----------- |
| 2001:db8:0:1::                                 |                     |         |              | -           |
| FF01::1:1000                                   |                     |         |              | 1/1/2       |
| switch# show                                   | ipv6 helper-address |         | interface    | 1/1/1       |
| Interface:                                     | 1/1/1               |         |              |             |
| IPv6 Helper                                    | Address             |         |              | Egress Port |
| ---------------------------------------------- |                     |         |              | ----------- |
| 2001:db8:0:1::                                 |                     |         |              | -           |
| FF01::1:1000                                   |                     |         |              | 1/1/2       |
| Command History                                |                     |         |              |             |
| Release                                        |                     |         | Modification |             |
| 10.07orearlier                                 |                     |         | --           |             |
| Command Information                            |                     |         |              |             |
| Platforms                                      | Command             | context | Authority    |             |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| DHCP server |     |     |     |     |
| ----------- | --- | --- | --- | --- |
Overview
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 84

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
| DHCP relay interoperation |     |     |     |
| ------------------------- | --- | --- | --- |
BothDHCPrelayandDHCPservercanbeconfiguredonthesameVRF.
| DHCP snooping | interoperation |     |     |
| ------------- | -------------- | --- | --- |
DHCPsnoopingmaynotbeconfiguredwithDHCPserver.
| Configuring | a DHCPv4 | server on | a VRF |
| ----------- | -------- | --------- | ----- |
Prerequisites
n Anenabledlayer3interface.
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
DHCP|85

h. ConfigureNetBIOSsupportwiththecommandsnetbios-name-serverandnetbios-node-
type.
| i. ConfigureBOOTPoptionswiththecommandbootp.         |     |     |     |
| ---------------------------------------------------- | --- | --- | --- |
| j. ExittheDHCPv4serverpoolcontextwiththecommandexit. |     |     |     |
4. EnabletheDHCPserverontheVRFwiththecommandenable.
5. ConfiguresupportforpersistentexternalstorageofDHCPsettingswiththecommanddhcp-
| server | external-storage. |     |     |
| ------ | ----------------- | --- | --- |
6. ViewDHCPv4serverconfigurationsettingswiththecommandshow dhcp-server all-vrfs.
Example
Thisexamplecreatesthefollowingconfiguration:
n ConfigurestheDHCPv4serveronVRFprimary-vrf.
n Enablesauthoritativemode.
n Definesthepoolprimary-poolwiththefollowingsettings:
o Addressrange:10.0.0.1to10.0.0.100.
o Leasetime:12hours.
o
Domainname:example.org.in.
o Defaultrouters:10.30.30.1and10.30.30.2.
o DNSservers:125.0.0.1and125.0.0.2.
o Staticbindingof10.0.0.11forMACaddress24:be:05:24:75:73.
o DHCPcustomoption3withIPaddress10.30.30.3.
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
Anenabledlayer3interface.
n
n AVRF.
n Anexternalstoragedeviceinstalledandconfigured(optional).
Procedure
1. AssigntheDHCPv6servertoaVRFwiththecommanddhcpv6-server vrf.Thisswitchestothe
DHCPv6serverconfigurationcontext.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 86

2.

If you want the DHCP server to be the sole authority for IP addresses on the VRF, enable
authoritative mode with the command authoritative.

3. Define an address pool for the VRF with the command pool. This switches to the DHCPv6 server

pool context. Customize pool settings as follows:
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

authoritative

authoritative
no authoritative

Description

Configures the DHCPv4 server as authoritative on the current VRF. This means that the server is the sole
authority for the network on the VRF. Therefore, if a client requests an IP address lease for which the
server has no record, the server responds with DHCPNAK, indicating that the client must no longer use

DHCP | 87

thatIPaddress.Iftheserverisnotauthoritative,thenitwillignoreDHCPv4requestsreceivedfor
unknownleasesfromunknownhosts.
ThenoformofthiscommanddisablesauthoritativemodeonthecurrentVRF.
Example
ConfiguresDHCPv4serverauthoritativemodeonVRFprimary.
| switch(config)#             | dhcp-server | vrf           | primary |
| --------------------------- | ----------- | ------------- | ------- |
| switch(config-dhcp-server)# |             | authoritative |         |
RemovestheDHCPv4serverauthoritativemodeonVRFprimary.
| switch(config)#             | dhcp-server | vrf     | primary       |
| --------------------------- | ----------- | ------- | ------------- |
| switch(config-dhcp-server)# |             | no      | authoritative |
| Command History             |             |         |               |
| Release                     |             |         | Modification  |
| 10.07orearlier              |             |         | --            |
| Command Information         |             |         |               |
| Platforms                   | Command     | context | Authority     |
config-dhcp-server
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
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
<REMOTE-URL>
SpecifiesthenameandlocationofaBOOTPfileonaTFTPserver
intheformat:
tftp://{<IP> | <HOST>}/<FILE>
<IP>:SpecifiestheIPaddressoftheTFTPserverhostingthe
n
fileinIPv4format(x.x.x.x),wherexisadecimalnumber
from0to255.Youcanremoveleadingzeros.Forexample,the
address192.169.005.100becomes192.168.5.100.
n <HOST>:Specifiesthefully-qualifieddomainnameoftheTFTP
serverhostingthefile.Range:1to64printableASCII
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 88

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
characters.
n <FILE>:SpecifiesthenameoftheBOOTPfile.Range:1to64
printableASCIIcharacters.
Example
DefinesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# bootp tftp://10.0.0.1/mybootfile
DeletesBOOTPsupportontheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# no bootp tftp://10.0.0.1/mybootfile
| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| clear dhcp-server | leases |     |     |
| ----------------- | ------ | --- | --- |
clear dhcp-server leases [all-vrfs | <IPV4-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv4serverleaseinformation.TheDHCPv4servermustbedisabledbeforeclearinglease
information.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
all-vrfs
ClearsleasesforallVRFs.
<IPV4-ADDR> vrf <VRF-NAME> ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv4format(x.x.x.x),wherexisadecimal
numberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| vrf <VRF-NAME> |     | ClearsleasesforaspecificVRF. |     |
| -------------- | --- | ---------------------------- | --- |
DHCP|89

Examples
ClearingallDHCPv4serverleases.
switch(config)#
|                             | dhcp-server |     | vrf primary |     |     |
| --------------------------- | ----------- | --- | ----------- | --- | --- |
| switch(config-dhcp-server)# |             |     | disable     |     |     |
| switch(config-dhcp-server)# |             |     | exit        |     |     |
| switch(config)#             | exit        |     |             |     |     |
| switch# clear               | dhcp-server |     | leases      |     |     |
ClearingallDHCPv4serverleasesforVRFprimary-vrf.
| switch(config)#             | dhcp-server |     | vrf primary |     |     |
| --------------------------- | ----------- | --- | ----------- | --- | --- |
| switch(config-dhcp-server)# |             |     | disable     |     |     |
| switch(config-dhcp-server)# |             |     | exit        |     |     |
switch(config)#
exit
| switch# clear | dhcp-server |     | leases vrf | primary-vrf |     |
| ------------- | ----------- | --- | ---------- | ----------- | --- |
CleartheDHCPv4serverleaseforIPaddress10.10.10.1onVRFprimary-vrf.
| switch(config)#             | dhcp-server |         | vrf primary       |              |                 |
| --------------------------- | ----------- | ------- | ----------------- | ------------ | --------------- |
| switch(config-dhcp-server)# |             |         | disable           |              |                 |
| switch(config-dhcp-server)# |             |         | exit              |              |                 |
| switch(config)#             | exit        |         |                   |              |                 |
| switch# clear               | dhcp-server |         | leases 10.10.10.1 |              | vrf primary-vrf |
| Command History             |             |         |                   |              |                 |
| Release                     |             |         |                   | Modification |                 |
| 10.07orearlier              |             |         |                   | --           |                 |
| Command Information         |             |         |                   |              |                 |
| Platforms                   | Command     | context |                   | Authority    |                 |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
default-router
| default-router    | <IPV4-ADDR-LIST> |     |     |     |     |
| ----------------- | ---------------- | --- | --- | --- | --- |
| no default-router | <IPV4-ADDR-LIST> |     |     |     |     |
Description
DefinesuptofourdefaultroutersforthecurrentDHCPv4serverpool.
Thenoformofthiscommandremovesthespecifieddefaultroutersfromthepool.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<IPV4-ADDR-LIST>
SpecifiestheIPaddressesofthedefaultroutersinIPv4format
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 90

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
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
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)#
no default-router ip 10.0.0.1
| Command History     |         |              |           |
| ------------------- | ------- | ------------ | --------- |
| Release             |         | Modification |           |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| dhcp-server | external-storage |     |     |
| ----------- | ---------------- | --- | --- |
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
DHCP|91

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VOLUME-NAME> Specifiestheexternalstoragevolumename.Range:1to64
printableASCIIcharacters.
file <LEASE-FILENAME>
Specifiestheexternalstoragefilename.Range:1to255printable
ASCIIcharacters.
delay <DELAY> Specifiestheintervalinsecondsbetweenupdatestotheexternal
storagefile.Range:15to86400.Default:300.
Example
StorestheleasefileonexternalstoragevolumeStorage1infileLeaseFileatanintervalof600seconds.
switch(config)# dhcp-server external-storage Storage1 file LeaseFile delay 600
DisablesstorageoftheleasefileonexternalstoragevolumeStorage1infileLeaseFile.
switch(config)# no dhcp-server external-storage Storage1 file LeaseFile delay 600
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcp-server    | vrf            |     |     |
| -------------- | -------------- | --- | --- |
| dhcp-server    | vrf <VRF-NAME> |     |     |
| no dhcp-server | vrf <VRF-NAME> |     |     |
Description
ConfigurestheDHCPv4servertosupportaVRFandchangestotheconfig-dhcp-servercontextfor
thatVRF.
ThenoformofthiscommandremovesDHCPv4serversupportonaVRF.
| Parameter  |     |     | Description |
| ---------- | --- | --- | ----------- |
| <VRF-NAME> |     |     | NameofaVRF. |
Example
ConfiguresDHCPv4serversupportonVRFprimary.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 92

| switch(config)# | dhcp-server |     | vrf | primary |
| --------------- | ----------- | --- | --- | ------- |
RemovesDHCPv4serversupportonVRFprimary.
| switch(config)#     | no      | dhcp-server |     | vrf primary  |
| ------------------- | ------- | ----------- | --- | ------------ |
| Command History     |         |             |     |              |
| Release             |         |             |     | Modification |
| 10.07orearlier      |         |             |     | --           |
| Command Information |         |             |     |              |
| Platforms           | Command | context     |     | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
disable
disable
Description
DisablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhen
configuredonaVRF.
Example
DisablestheDHCPv4serveronVRFprimary.
| switch(config)#             | dhcp-server |         | vrf     | primary      |
| --------------------------- | ----------- | ------- | ------- | ------------ |
| switch(config-dhcp-server)# |             |         | disable |              |
| Command History             |             |         |         |              |
| Release                     |             |         |         | Modification |
| 10.07orearlier              |             |         |         | --           |
| Command Information         |             |         |         |              |
| Platforms                   | Command     | context |         | Authority    |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
dns-server
| dns-server <IPV4-ADDR-LIST> |                  |     |     |     |
| --------------------------- | ---------------- | --- | --- | --- |
| no dns-server               | <IPV4-ADDR-LIST> |     |     |     |
DHCP|93

Description
DefinesuptofourDNSserversforthecurrentDHCPv4serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<IPV4-ADDR-LIST> SpecifiestheIPaddressesoftheDNSserversinIPv4format
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 94

Definesadomainnamefortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server |     | vrf  | primary      |                |
| -------------------------------- | ----------- | --- | ---- | ------------ | -------------- |
| switch(config-dhcp-server)#      |             |     | pool | primary-pool |                |
| switch(config-dhcp-server-pool)# |             |     |      | domain-name  | example.org.in |
Deletesadomainnamefromtheserverpoolprimary-poolonVRFprimary.
| switch(config)# | dhcp-server |     | vrf | primary |     |
| --------------- | ----------- | --- | --- | ------- | --- |
switch(config-dhcp-server)#
|                                  |         |         | pool | primary-pool   |                |
| -------------------------------- | ------- | ------- | ---- | -------------- | -------------- |
| switch(config-dhcp-server-pool)# |         |         |      | no domain-name | example.org.in |
| Command History                  |         |         |      |                |                |
| Release                          |         |         |      | Modification   |                |
| 10.07orearlier                   |         |         |      | --             |                |
| Command Information              |         |         |      |                |                |
| Platforms                        | Command | context |      | Authority      |                |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
enable
enable
Description
EnablestheDHCPv4serveronthecurrentVRF.TheDHCPv4serverisdisabledbydefaultwhen
configuredonaVRF.
Example
EnablestheDHCPv4serveronVRFprimary.
switch(config)#
|                             | dhcp-server |         | vrf    | primary      |     |
| --------------------------- | ----------- | ------- | ------ | ------------ | --- |
| switch(config-dhcp-server)# |             |         | enable |              |     |
| Command History             |             |         |        |              |     |
| Release                     |             |         |        | Modification |     |
| 10.07orearlier              |             |         |        | --           |     |
| Command Information         |             |         |        |              |     |
| Platforms                   | Command     | context |        | Authority    |     |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
DHCP|95

http-proxy
| http-proxy    | {<FQDN | | IPV4-ADDR>} | [vrf <VRF-NAME>] |     |
| ------------- | ------ | ------------- | ---------------- | --- |
| no http-proxy | [<FQDN | | IPV4-ADDR>] | [vrf <VRF-NAME>] |     |
Description
SpecifiesHTTPproxylocationandVRF.
ThenoformofthiscommandremovesaspecifiedHTTPproxylocation.
| Parameter |     |     | Description                         |     |
| --------- | --- | --- | ----------------------------------- | --- |
| <FQDN>    |     |     | SpecifiesFQDNforHTTP proxylocation. |     |
<IPV4-ADDR>
SpecifiesIPV4addressforHTTPproxylocation.
| <VRF-NAME> |     |     | SpecifiesVRF forHTTP proxy. |     |
| ---------- | --- | --- | --------------------------- | --- |
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
| 1.  | Userconfigured.                             |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- |
| 2.  | DHCPoptionsreceivedviamanagement/OOBM port. |     |     |     |
| 3.  | DHCP optionsreceivedviaVLAN1.               |     |     |     |
n HTTPproxylocationcanonlybeaFQDNoranIPV4address.
n WhenHTTPproxylocationandVRFareconfigured,theyoverrideanyexistingHTTPproxylocationandVRF.
n IfthiscommandisexecutedwithouttheVRFparameter,thedefaultVRFwillbeused.
n PortnumbermayneedtobespecifiedattheendoftheIPaddressforFQDNtoconnectviaHTTPproxy.
o Forexample,8088istheTCPportnumber:http-proxy192.168.248.248:8088
Examples
SpecifyingaFQDNforHTTPproxylocationandMGMTVRF:
| switch(config)# |     | http-proxy | http-proxy.aruba.com | vrf mgmt |
| --------------- | --- | ---------- | -------------------- | -------- |
RemovingHTTPproxylocation
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 96

| switch(config)#     | no      | http-proxy |              |
| ------------------- | ------- | ---------- | ------------ |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
lease
| lease {<TIME> | | infinite} |     |     |
| ------------- | ----------- | --- | --- |
no lease
Description
SetsthelengthoftheDHCPv4leasetimeforthecurrentpool.TheleasetimedetermineshowlonganIP
addressisvalidbeforeaDHCPv4clientmustrequestthatitberenewed.
ThenoformofthiscommandreturnstheDHCPv4leasetimetoitsdefaultvalue1hour.
| Parameter |     |     | Description                                     |
| --------- | --- | --- | ----------------------------------------------- |
| <TIME>    |     |     | SetstheDHCPv4leasetime.Format:DD:HH:MM.Default: |
01:00:00.
infinite SetstheDHCPv4leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
Example
SetstheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimaryto12hours.
| switch(config)#                  | dhcp-server | vrf  | primary        |
| -------------------------------- | ----------- | ---- | -------------- |
| switch(config-dhcp-server)#      |             | pool | primary-pool   |
| switch(config-dhcp-server-pool)# |             |      | lease 00:12:00 |
DeletestheleasetimeforDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#                  | dhcp-server | vrf  | primary           |
| -------------------------------- | ----------- | ---- | ----------------- |
| switch(config-dhcp-server)#      |             | pool | primary-pool      |
| switch(config-dhcp-server-pool)# |             |      | no lease 00:12:00 |
| Command History                  |             |      |                   |
DHCP|97

| Release             |         | Modification |           |
| ------------------- | ------- | ------------ | --------- |
| 10.07orearlier      |         | --           |           |
| Command Information |         |              |           |
| Platforms           | Command | context      | Authority |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
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
Separateaddresseswithaspace.AmaximumoffourIPaddresses
canbedefined.
Example
DefinestwoWINSserversfortheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# netbios-name-server ip 10.0.20.1 10.0.30.10
DeletesaWINSserverfromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server | vrf primary       |     |
| --------------------------- | ----------- | ----------------- | --- |
| switch(config-dhcp-server)# |             | pool primary-pool |     |
switch(config-dhcp-server-pool)# no netbios-name-server ip 10.0.20.1
| Command History     |     |              |     |
| ------------------- | --- | ------------ | --- |
| Release             |     | Modification |     |
| 10.07orearlier      |     | --           |     |
| Command Information |     |              |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 98

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
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
| switch(config)#             | dhcp-server | vrf  | primary      |     |
| --------------------------- | ----------- | ---- | ------------ | --- |
| switch(config-dhcp-server)# |             | pool | primary-pool |     |
switch(config-dhcp-server-pool)# no netbios-node-type broadcast
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
option
option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
no option <OPTION-NUM> {ascii <ASCII-STR> | hex <HEX-STR> | ip <IPV4-ADDR-LIST>}
Description
DHCP|99

DefinescustomDHCPv4optionsforthecurrentDHCPv4serverpool.DHCPv4optionsenablethe
DHCPv4servertoprovideadditionalinformationaboutthenetworkwhenDHCPv4clientsrequestan
address.
ThenoformofthiscommandremovescustomDHCPv4optionsfromthepool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<OPTION-NUM>
SpecifiesaDHCPv4optionnumber.ForalistofDHCPv4option
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
| switch(config)#                  | dhcp-server | vrf  | primary      |                  |
| -------------------------------- | ----------- | ---- | ------------ | ---------------- |
| switch(config-dhcp-server)#      |             | pool | primary-pool |                  |
| switch(config-dhcp-server-pool)# |             |      | option       | 3 ip 192.168.1.1 |
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
6200 config-dhcp-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
pool
pool <POOL-NAME>
no pool <POOL-NAME>
Description
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 100

CreatesaDHCPv4serverpoolforthecurrentVRFandswitchestotheconfig-dhcp-server-pool
contextforit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64
pools(IPv4andIPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv4serverpool.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<POOL-NAME>
SpecifiestheDHCPv4poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             |     | dhcp-server | vrf  | primary      |     |
| --------------------------- | --- | ----------- | ---- | ------------ | --- |
| switch(config-dhcp-server)# |     |             | pool | primary-pool |     |
switch(config-dhcp-server-pool)#
DeletestheDHCPv4serverpoolprimary-poolonVRFprimary.
| switch(config)#             |         | dhcp-server | vrf | primary           |     |
| --------------------------- | ------- | ----------- | --- | ----------------- | --- |
| switch(config-dhcp-server)# |         |             | no  | pool primary-pool |     |
| Command History             |         |             |     |                   |     |
| Release                     |         |             |     | Modification      |     |
| 10.07orearlier              |         |             |     | --                |     |
| Command Information         |         |             |     |                   |     |
| Platforms                   | Command | context     |     | Authority         |     |
6200 config-dhcp-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
range
| range <LOW-IPV4-ADDR>    |     | <HIGH-IPV4-ADDR> |     | [prefix-len | <MASK>] |
| ------------------------ | --- | ---------------- | --- | ----------- | ------- |
| no range <LOW-IPV4-ADDR> |     | <HIGH-IPV4-ADDR> |     | [prefix-len | <MASK>] |
Description
DefinestherangeofIPaddressessupportedbythecurrentDHCPv4serverpool.Amaximumof64
rangesaresupportedperswitchacrossallVRFs.
Thenoformofthiscommanddeletestheaddressrangeforthecurrentpool.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<LOW-IPV4-ADDR> SpecifiesthelowestIPaddressinthepoolinIPv4format(x.x.x.x),
DHCP|101

| Parameter |     |     | Description |     |     |     |     |
| --------- | --- | --- | ----------- | --- | --- | --- | --- |
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
|     |     |     | switch(config)#         |     | interface | vlan 2         |              |
| --- | --- | --- | ----------------------- | --- | --------- | -------------- | ------------ |
|     |     |     | switch(config-if-vlan)# |     |           | ip address     | 200.1.1.1/16 |
|     |     |     | switch(config-if-vlan)# |     |           | active-gateway | ip 200.1.1.3 |
mac 00:aa:aa:aa:aa:aa
|     |     |     | switch(config-if-vlan)#          |     |             | exit |                   |
| --- | --- | --- | -------------------------------- | --- | ----------- | ---- | ----------------- |
|     |     |     | switch(config)#                  |     | dhcp-server | vrf  | primary           |
|     |     |     | switch(config-dhcp-server)#      |     |             | pool | primary-pool      |
|     |     |     | switch(config-dhcp-server-pool)# |     |             |      | range 192.168.1.1 |
|     |     |     | 192.168.1.100                    |     | prefix-len  | 16   |                   |
Examples
Definestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfortheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |     |     |     |
| --------------------------- | ----------- | --- | ----------------- | --- | --- | --- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |     |     |     |
switch(config-dhcp-server-pool)# 192.168.1.1 192.168.1.100 prefix-len 24
Deletestheaddressrange192.168.1.1to192.168.1.100withamaskof24bitsfromtheDHCPv4server
poolprimary-poolonVRFprimary.
| switch(config)#             | dhcp-server |     | vrf primary       |     |     |     |     |
| --------------------------- | ----------- | --- | ----------------- | --- | --- | --- | --- |
| switch(config-dhcp-server)# |             |     | pool primary-pool |     |     |     |     |
switch(config-dhcp-server-pool)# no 192.168.1.1 192.168.1.100 prefix-len 24
| Command History     |         |         |              |           |     |     |     |
| ------------------- | ------- | ------- | ------------ | --------- | --- | --- | --- |
| Release             |         |         | Modification |           |     |     |     |
| 10.07orearlier      |         |         | --           |           |     |     |     |
| Command Information |         |         |              |           |     |     |     |
| Platforms           | Command | context |              | Authority |     |     |     |
config-dhcp-server-pool
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswith |     |     |     |
| ---- | --- | --- | --- | ----------------------------------------- | --- | --- | --- |
executionrightsforthiscommand.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 102

show dhcp-server
| show dhcp-server | [all-vrfs] |             |      |                 |     |
| ---------------- | ---------- | ----------- | ---- | --------------- | --- |
| show dhcp-server | leases     | {all-vrfs   | |    | vrf <VRF-NAME>} |     |
| show dhcp-server | pool       | <POOL-NAME> | [vrf | <VRF-NAME>]     |     |
Description
ShowsconfigurationsettingsfortheDHCPv4server.
| Parameter        |     |                   |     | Description                                       |     |
| ---------------- | --- | ----------------- | --- | ------------------------------------------------- | --- |
| all-vrfs         |     |                   |     | ShowsDHCPv4serverconfigurationsettingsforallVRFs. |     |
| leases {all-vrfs |     | | vrf <VRF-NAME>} |     |                                                   |     |
ShowsDHCPv4serverleaseconfigurationsettingsforallVRFs
oraspecificVRF.
pool <POOL-NAME> [vrf <VRF-NAME>] ShowsDHCPv4serverpoolconfigurationsettingsforallVRFs
oraspecificVRF.
Examples
ShowingallDHCPv4serverconfigurationsettings.
| switch# show   | dhcp-server |               |     |     |     |
| -------------- | ----------- | ------------- | --- | --- | --- |
| VRF Name       |             | : default     |     |     |     |
| DHCP Server    |             | : enabled     |     |     |     |
| Operational    | State       | : operational |     |     |     |
| Authoritative  | Mode        | : false       |     |     |     |
| Pool Name      |             | : test        |     |     |     |
| Lease Duration |             | : 00:01:00    |     |     |     |
| DHCP dynamic   | IP          | allocation    |     |     |     |
--------------------------
| Start-IP-Address |         | End-IP-Address |     | Prefix-Length  |     |
| ---------------- | ------- | -------------- | --- | -------------- | --- |
| ---------------- |         | -------------- |     | -------------- |     |
| 192.168.1.1      |         | 192.168.1.20   |     | 24             |     |
| DHCP Server      | options |                |     |                |     |
-------------------
| Option-Number |        | Option-Type   | Option-Value |          |                   |
| ------------- | ------ | ------------- | ------------ | -------- | ----------------- |
| ------------- |        | -----------   | ------------ |          |                   |
| 6             |        | ip            | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 10.0.0.6 |
| DHCP Server   | static | IP allocation |              |          |                   |
--------------------------------
| IP-Address    |     | Client-Hostname  |     | State       | MAC-Address       |
| ------------- | --- | ---------------- | --- | ----------- | ----------------- |
| -----------   |     | ---------------- |     | ------      | ------------      |
| 10.0.0.3      |     | *                |     | OPERATIONAL | aa:aa:aa:aa:aa:aa |
| BOOTP Options |     |                  |     |             |                   |
---------------
| Boot-File-Name |     | TFTP-Server-Name |     | TFTP-Server-Address   |     |
| -------------- | --- | ---------------- | --- | --------------------- | --- |
| -------------- |     | ---------------- |     | --------------------- |     |
| boot.txt       |     | *                |     | 10.0.0.10             |     |
DHCP|103

ShowingDHCPserverconfigurationsettingsforVRFprimary-vrf.
| switch# show   | dhcp-server |               | vrf | primary-vrf |     |     |     |
| -------------- | ----------- | ------------- | --- | ----------- | --- | --- | --- |
| VRF Name       |             | : primary-vrf |     |             |     |     |     |
| DHCP Server    |             | : disabled    |     |             |     |     |     |
| Operational    | State       | : disabled    |     |             |     |     |     |
| Authoritative  | Mode        | : false       |     |             |     |     |     |
| Pool Name      |             | : test        |     |             |     |     |     |
| Lease Duration |             | : 00:01:00    |     |             |     |     |     |
| DHCP dynamic   | IP          | allocation    |     |             |     |     |     |
--------------------------
| Start-IP-Address |         | End-IP-Address |     |     | Prefix-Length  |     |     |
| ---------------- | ------- | -------------- | --- | --- | -------------- | --- | --- |
| ---------------- |         | -------------- |     |     | -------------- |     |     |
| 10.0.0.1         |         | 10.0.0.30      |     |     | *              |     |     |
| 192.168.1.1      |         | 192.168.1.20   |     |     | 24             |     |     |
| 192.168.10.30    |         | 192.168.10.60  |     |     | 16             |     |     |
| DHCP Server      | options |                |     |     |                |     |     |
-------------------
| Option-Number |        | Option-Type |            | Option-Value |          |          |          |
| ------------- | ------ | ----------- | ---------- | ------------ | -------- | -------- | -------- |
| ------------- |        | ----------- |            | ------------ |          |          |          |
| 6             |        | ip          |            | 10.0.0.3     | 10.0.0.4 | 10.0.0.5 | 10.0.0.6 |
| 18            |        | ascii       |            | aswed        |          |          |          |
| DHCP Server   | static | IP          | allocation |              |          |          |          |
--------------------------------
| IP-Address    | Client-Hostname |     |     | MAC-Address       |     |     |     |
| ------------- | --------------- | --- | --- | ----------------- | --- | --- | --- |
| ----------    | --------------- |     |     | ----------------- |     |     |     |
| 10.0.0.1      |                 | *   |     | aa:bb:cc:11:12:a4 |     |     |     |
| 20.0.0.1      |                 | *   |     | 11:22:11:22:aa:dd |     |     |     |
| BOOTP Options |                 |     |     |                   |     |     |     |
---------------
| Boot-File-Name      |         | TFTP-Server-Name |         |     | State        |     | TFTP-Server-Address   |
| ------------------- | ------- | ---------------- | ------- | --- | ------------ | --- | --------------------- |
| --------------      |         | ---------------- |         |     | ------       |     | --------------------- |
| boot.txt            |         | *                |         |     | OPERATIONAL  |     | 10.0.0.10             |
| Command History     |         |                  |         |     |              |     |                       |
| Release             |         |                  |         |     | Modification |     |                       |
| 10.07orearlier      |         |                  |         |     | --           |     |                       |
| Command Information |         |                  |         |     |              |     |                       |
| Platforms           | Command |                  | context |     | Authority    |     |                       |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
static-bind
static-bind {ip <IPV4-ADDR>}|{ mac <MAC-ADDR>} [hostname <HOST>]
| no static-bind | <IPV4-ADDR-LIST> |     |     |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 104

Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaspecificMACaddress.
ThiscausestheDHCPv4servertoonlyassignthespecifiedIPaddresstoaclientstationwiththe
specifiedMACaddress.
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
config-dhcp-server-pool
| 6200 |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
| DHCP server | IPv6 | commands |     |
| ----------- | ---- | -------- | --- |
authoritative
authoritative
no authoritative
Description
DHCP|105

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
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| clear dhcpv6-server | leases |     |     |
| ------------------- | ------ | --- | --- |
clear dhcpv6-server leases [all-vrfs | <IPV6-ADDR> vrf <VRF-NAME>] | vrf <VRF-NAME>]
Description
ClearsDHCPv6serverleaseinformation.TheDHCPv6servermustbedisabledbeforeclearinglease
information.
| Parameter   |                |     | Description             |
| ----------- | -------------- | --- | ----------------------- |
| all-vrfs    |                |     | ClearsleasesforallVRFs. |
| <IPV6-ADDR> | vrf <VRF-NAME> |     |                         |
ClearstheleaseforaspecificclientonaspecificVRF.Specifythe
clientaddressinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseahextetoffourzerostoasingle0.For
example,thisaddress
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 106

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| vrf <VRF-NAME> |     |     |     | ClearsleasesforaspecificVRF. |     |
| -------------- | --- | --- | --- | ---------------------------- | --- |
Examples
ClearingallDHCPv6serverleases.
| switch(config)#               | dhcpv6-server |     | vrf     | primary |     |
| ----------------------------- | ------------- | --- | ------- | ------- | --- |
| switch(config-dhcpv6-server)# |               |     | disable |         |     |
| switch(config-dhcpv6-server)# |               |     | exit    |         |     |
| switch(config)#               | exit          |     |         |         |     |
| switch# clear                 | dhcpv6-server |     | leases  |         |     |
ClearingallDHCPv6serverleasesforVRFprimary-vrf.
| switch(config)#               | dhcpv6-server |     | vrf     | primary         |     |
| ----------------------------- | ------------- | --- | ------- | --------------- | --- |
| switch(config-dhcpv6-server)# |               |     | disable |                 |     |
| switch(config-dhcpv6-server)# |               |     | exit    |                 |     |
| switch(config)#               | exit          |     |         |                 |     |
| switch# clear                 | dhcpv6-server |     | leases  | vrf primary-vrf |     |
CleartheDHCPv6serverleaseforIPaddress2001::1onVRFprimary-vrf.
| switch(config)# | dhcpv6-server |     | vrf | primary |     |
| --------------- | ------------- | --- | --- | ------- | --- |
switch(config-dhcpv6-server)#
disable
| switch(config-dhcpv6-server)# |               |         | exit   |              |                 |
| ----------------------------- | ------------- | ------- | ------ | ------------ | --------------- |
| switch(config)#               | exit          |         |        |              |                 |
| switch# clear                 | dhcpv6-server |         | leases | 2001::1      | vrf primary-vrf |
| Command History               |               |         |        |              |                 |
| Release                       |               |         |        | Modification |                 |
| 10.07orearlier                |               |         |        | --           |                 |
| Command Information           |               |         |        |              |                 |
| Platforms                     | Command       | context |        | Authority    |                 |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| dhcv6p-server | external-storage |     |     |     |     |
| ------------- | ---------------- | --- | --- | --- | --- |
dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
no dhcpv6-server external-storage <VOLUME-NAME> file <LEASE-FILENAME> [delay <DELAY>]
Description
DHCP|107

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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-server    | vrf          |     |     |
| ---------------- | ------------ | --- | --- |
| dhcpv6-server    | vrf VRF-NAME |     |     |
| no dhcpv6-server | vrf VRF-NAME |     |     |
Description
ConfigurestheDHCPv6servertosupportaVRFandchangestotheconfig-dhcpv6-servercontextfor
thatVRF.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 108

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
config
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
rightsforthiscommand.
disable
disable
Description
DisablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhen
configuredonaVRF.
Example
DisablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary  |
| ----------------------------- | ------------- | --- | ------------ |
| switch(config-dhcpv6-server)# |               |     | disable      |
| Command History               |               |     |              |
| Release                       |               |     | Modification |
| 10.07orearlier                |               |     | --           |
| Command Information           |               |     |              |
DHCP|109

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
dns-server
| dns-server <IPVv6-ADDR-LIST> |                   |     |     |     |     |
| ---------------------------- | ----------------- | --- | --- | --- | --- |
| no dns-server                | <IPVv6-ADDR-LIST> |     |     |     |     |
Description
DefinesuptofourDNSserversforthecurrentDHCPv6serverpool.
ThenoformofthiscommandremovesthespecifiedDNSserversfromthepool.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<IPVv6-ADDR-LIST> SpecifiestheIPaddressesoftheDNSserversinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Separateaddresseswitha
space.AmaximumoffourIPaddressescanbedefined.
Example
DefinesDNSserver2001::13fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server |     | vrf  | primary      |          |
| ---------------------------------- | ------------- | --- | ---- | ------------ | -------- |
| switch(config-dhcpv6-server)#      |               |     | pool | primary-pool |          |
| switch(config-dhcpv6-server-pool)# |               |     |      | dns-server   | 2001::13 |
DeletesDNSserver2001::13fromtheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server |         | vrf  | primary       |          |
| ---------------------------------- | ------------- | ------- | ---- | ------------- | -------- |
| switch(config-dhcpv6-server)#      |               |         | pool | primary-pool  |          |
| switch(config-dhcpv6-server-pool)# |               |         |      | no dns-server | 2001::13 |
| Command History                    |               |         |      |               |          |
| Release                            |               |         |      | Modification  |          |
| 10.07orearlier                     |               |         |      | --            |          |
| Command Information                |               |         |      |               |          |
| Platforms                          | Command       | context |      | Authority     |          |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
enable
enable
Description
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 110

EnablestheDHCPv6serveronthecurrentVRF.TheDHCPv6serverisdisabledbydefaultwhen
configuredonaVRF.
Example
EnablestheDHCPv6serveronVRFprimary.
| switch(config)#               | dhcpv6-server | vrf     | primary      |
| ----------------------------- | ------------- | ------- | ------------ |
| switch(config-dhcpv6-server)# |               | enable  |              |
| Command History               |               |         |              |
| Release                       |               |         | Modification |
| 10.07orearlier                |               |         | --           |
| Command Information           |               |         |              |
| Platforms                     | Command       | context | Authority    |
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
infinite SetstheDHCPv6leasetimetoinfinite.Thismeansthataddresses
donotneedtoberenewed.
Example
SetstheleasetimeforDHCPv6serverpoolprimary-poolonVRFprimaryto12hours.
| switch(config)#                    | dhcpv6-server | vrf  | primary        |
| ---------------------------------- | ------------- | ---- | -------------- |
| switch(config-dhcpv6-server)#      |               | pool | primary-pool   |
| switch(config-dhcpv6-server-pool)# |               |      | lease 00:12:00 |
SetstheleasetimeforDHCPserverpoolprimary-poolonVRFprimarytothedefaultvalue.
DHCP|111

| switch(config)# | dhcpv6-server |     | vrf primary |     |
| --------------- | ------------- | --- | ----------- | --- |
switch(config-dhcpv6-server)#
pool primary-pool
| switch(config-dhcpv6-server-pool)# |         |         | no           | lease 00:12:00 |
| ---------------------------------- | ------- | ------- | ------------ | -------------- |
| Command History                    |         |         |              |                |
| Release                            |         |         | Modification |                |
| 10.07orearlier                     |         |         | --           |                |
| Command Information                |         |         |              |                |
| Platforms                          | Command | context |              | Authority      |
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
ascii <ASCII-STR>
SpecifiesavaluefortheselectedoptionasanASCIIstring.Range:
1to255ASCIIcharacters.
hex <HEX-STR> Specifiesavaluefortheselectedoptionasahexadecimalstring.
Range:1to255hexadecimalcharacters.
ip <IPV6-ADDR-LIST> SpecifiesalistofIPaddressesfortheoptioninIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
Example
DefinesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
| switch(config)#                    | dhcpv6-server |     | vrf primary       |                  |
| ---------------------------------- | ------------- | --- | ----------------- | ---------------- |
| switch(config-dhcpv6-server)#      |               |     | pool primary-pool |                  |
| switch(config-dhcpv6-server-pool)# |               |     | option            | 22 ipv6 2001::12 |
DeletesDHCPv6option22fortheserverpoolprimary-poolonVRFprimary.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 112

| switch(config)# | dhcpv6-server |     | vrf primary |     |
| --------------- | ------------- | --- | ----------- | --- |
switch(config-dhcpv6-server)#
pool primary-pool
| switch(config-dhcpv6-server-pool)# |         |         | no           | option 22 ipv6 2001::12 |
| ---------------------------------- | ------- | ------- | ------------ | ----------------------- |
| Command History                    |         |         |              |                         |
| Release                            |         |         | Modification |                         |
| 10.07orearlier                     |         |         | --           |                         |
| Command Information                |         |         |              |                         |
| Platforms                          | Command | context |              | Authority               |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
pool
pool <POOL-NAME>
no pool <POOL-NAME>
Description
CreatesaDHCPv6serverpoolforthecurrentVRFandswitchestotheconfig-dhcpv6-server-pool
contextforit.Multiplepools,eachwithadistinctrange,canbeassignedtoaVRF.Amaximumof64
pools(IPv4andIPv6),64addressranges,and8182clientsaresupportedontheswitchacrossallVRFs.
ThenoformofthiscommanddeletesthespecifiedDHCPv6serverpool.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<POOL-NAME> SpecifiestheDHCPv6poolname.Amaximumof64pools(IPv4
andIPv6)aresupportedacrossVRFsontheswitch.Range:1to32
printableASCIIcharacters.Firstcharactermustbealetteror
number.
Example
CreatestheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary       |     |
| ----------------------------- | ------------- | --- | ----------------- | --- |
| switch(config-dhcpv6-server)# |               |     | pool primary-pool |     |
switch(config-dhcpv6-server-pool)#
DeletestheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               | dhcpv6-server |     | vrf primary |              |
| ----------------------------- | ------------- | --- | ----------- | ------------ |
| switch(config-dhcpv6-server)# |               |     | no pool     | primary-pool |
| Command History               |               |     |             |              |
DHCP|113

| Release             |         |         |     | Modification |     |
| ------------------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier      |         |         |     | --           |     |
| Command Information |         |         |     |              |     |
| Platforms           | Command | context |     | Authority    |     |
6200 config-dhcpv6-server Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
<HIGH-IPV6-ADDR> SpecifiesthehighestIPaddressinthepoolinIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
prefix-len <MASK> SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom64to128.
Example
DefinesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
switch(config)#
|                               |     | dhcpv6-server | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)# range 2001::1 2001::10 prefix-len 64
DeletesanaddressrangefortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server | vrf  | primary      |     |
| ----------------------------- | --- | ------------- | ---- | ------------ | --- |
| switch(config-dhcpv6-server)# |     |               | pool | primary-pool |     |
switch(config-dhcpv6-server-pool)# no range 2001::1 2001::10 prefix-len 64
| Command History |     |     |     |              |     |
| --------------- | --- | --- | --- | ------------ | --- |
| Release         |     |     |     | Modification |     |
| 10.07orearlier  |     |     |     | --           |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 114

| Command Information |         |     |         |     |           |
| ------------------- | ------- | --- | ------- | --- | --------- |
| Platforms           | Command |     | context |     | Authority |
config-dhcpv6-server-pool
| 6200 |     |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | --- | ----------------------------------------- |
executionrightsforthiscommand.
show dhcpv6-server
| show dhcpv6-server |     | [all-vrfs] |             |       |             |
| ------------------ | --- | ---------- | ----------- | ----- | ----------- |
| show dhcpv6-server |     | leases     | {all-vrfs   | | vrf | <VRF-NAME>} |
| show dhcpv6-server |     | pool       | <POOL-NAME> | [vrf  | <VRF-NAME>] |
Description
ShowsconfigurationsettingsfortheDHCPv6server.
| Parameter |     |     |     |     | Description                                       |
| --------- | --- | --- | --- | --- | ------------------------------------------------- |
| all-vrfs  |     |     |     |     | ShowsDHCPv6serverconfigurationsettingsforallVRFs. |
leases {all-vrfs | vrf <VRF-NAME>} ShowsDHCPv6serverleaseconfigurationsettingsforallVRFs
oraspecificVRF.
pool <POOL-NAME> [vrf <VRF-NAME>] ShowsDHCPv6serverpoolconfigurationsettingsforallVRFs
oraspecificVRF.
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
DHCP|115

| switch# show   | dhcpv6-server |               | vrf         | primary-vrf |     |     |
| -------------- | ------------- | ------------- | ----------- | ----------- | --- | --- |
| VRF Name       |               | :             | primary-vrf |             |     |     |
| DHCPv6 Server  |               | :             | disabled    |             |     |     |
| Operational    | State         | :             | standby     |             |     |     |
| Authoritative  | Mode          | :             | false       |             |     |     |
| Pool Name      |               | :             | test        |             |     |     |
| Lease Duration |               | :             | 00:01:00    |             |     |     |
| DHCPV6 dynamic |               | IP allocation |             |             |     |     |
-----------------------------
| Start-IPv6-Address |         | End-IPv6-Address |     |     | Prefix-Length |     |
| ------------------ | ------- | ---------------- | --- | --- | ------------- | --- |
| ------------------ |         | ---------------- |     |     | ------------- |     |
| 2000::1            |         | 2000::20         |     |     | *             |     |
| 2001::20           |         | 2001::50         |     |     | *             |     |
| 2001::2            |         | 2001::10         |     |     | 64            |     |
| 2010::20           |         | 2010::40         |     |     | *             |     |
| DHCPv6 Server      | options |                  |     |     |               |     |
---------------------
| Option-Number |        | Option-Type |               | Option-Value |     |     |
| ------------- | ------ | ----------- | ------------- | ------------ | --- | --- |
| ------------- |        | ----------- |               | ------------ |     |     |
| 7             |        | ipv6        |               | 2001::15     |     |     |
| 23            |        | ipv6        |               | 2001::30     |     |     |
| 30            |        | ipv6        |               | 2001::10     |     |     |
| DHCvP6 Server | static |             | IP allocation |              |     |     |
-----------------------------------
| DHCPv6 Server  | static |               | host is | not configured. |     |     |
| -------------- | ------ | ------------- | ------- | --------------- | --- | --- |
| Pool Name      |        | : v6test      |         |                 |     |     |
| Lease Duration |        | : 00:01:00    |         |                 |     |     |
| DHCPv6 dynamic |        | IP allocation |         |                 |     |     |
-----------------------------
| Start-IPv6-Address |         |     | End-IPv6-Address |     | Prefix-Length |     |
| ------------------ | ------- | --- | ---------------- | --- | ------------- | --- |
| ------------------ |         |     | ---------------- |     | ------------- |     |
| 2001::1            |         |     | 2001::20         |     | 64            |     |
| 2010::10           |         |     | 2010::30         |     | *             |     |
| 2020::20           |         |     | 2020::60         |     | *             |     |
| DHCPv6 Server      | options |     |                  |     |               |     |
---------------------
| Option-Number |     | Option-Type |     | Option-Value                            |     |     |
| ------------- | --- | ----------- | --- | --------------------------------------- | --- | --- |
| ------------- |     | ----------- |     | -----------------                       |     |     |
| 7             |     | ipv6        |     | 2001::20                                |     |     |
| 23            |     | ipv6        |     | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |     |     |
2001:0db8:85a3:0000:0000:8a2e:0370:7335
2001:0db8:85a3:0000:0000:8a2e:0370:7336
2001:0db8:85a3:0000:0000:8a2e:0370:7337
| DHCPv6 Server | static |     | IP allocation |     |     |     |
| ------------- | ------ | --- | ------------- | --- | --- | --- |
------------------------------------
| IPv6-Address    |     | Client-Hostname |     |     | State       | Client-Id          |
| --------------- | --- | --------------- | --- | --- | ----------- | ------------------ |
| ------------    |     | --------------- |     |     | ----------- | ---------          |
| 2100::4         |     | *               |     |     | OPERATIONAL | 1:0:a0:24:ab:fb:9c |
| Command History |     |                 |     |     |             |                    |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 116

| Release        |             |     |         |     | Modification |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |             |     |         |     | --           |     |     |
| Command        | Information |     |         |     |              |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |
6200 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
static-bind
| static-bind    | ipv6 | <IPVv6-ADDR>      |     | client-id | <ID> [hostname | <HOST>] |     |
| -------------- | ---- | ----------------- | --- | --------- | -------------- | ------- | --- |
| no static-bind | ipv6 | <IPVv6-ADDR-LIST> |     |           |                |         |     |
Description
CreatesastaticbindingthatassociatesanIPaddressinthecurrentpoolwithaclientidentifierorDUID.
ThiscausestheDHCPv6servertoonlyassignthespecifiedIPaddresstoaclientstationwiththe
specifiedclientidentifierorDUID.
Thenoformofthiscommandremovesthespecifiedstaticbindingfromthepool.
| Parameter   |     |     |     |     | Description                               |     |     |
| ----------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- |
| <IPV6-ADDR> |     |     |     |     | SpecifiestheIPaddresstoassigninIPv6format |     |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Forexample,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| client-id | <ID> |     |     |     | SpecifiestheclientidentifierorDUID. |     |     |
| --------- | ---- | --- | --- | --- | ----------------------------------- | --- | --- |
hostname <HOST> Specifiesthehostnameoftheclientstation.Range:1to255
printableASCIIcharacters
Example
DefinesastaticaddressfortheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server |     | vrf  | primary      |     |     |
| ----------------------------- | --- | ------------- | --- | ---- | ------------ | --- | --- |
| switch(config-dhcpv6-server)# |     |               |     | pool | primary-pool |     |     |
switch(config-dhcpv6-server-pool)#
|     |     |     |     |     | static-bind | ipv6 2001::10 | client-id |
| --- | --- | --- | --- | --- | ----------- | ------------- | --------- |
1:0:a0:24:ab:fb:9c
DeletesastaticaddressfromtheDHCPv6serverpoolprimary-poolonVRFprimary.
| switch(config)#               |     | dhcpv6-server |     | vrf  | primary      |     |     |
| ----------------------------- | --- | ------------- | --- | ---- | ------------ | --- | --- |
| switch(config-dhcpv6-server)# |     |               |     | pool | primary-pool |     |     |
switch(config-dhcpv6-server-pool)# no static-bind ipv6 2001::10 client-id
1:0:a0:24:ab:fb:9c
| Command | History |     |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- |
DHCP|117

Release Modification
10.07orearlier --
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 config-dhcpv6-server-pool Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 118

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

119

DHCP server interoperation

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

1. When a port is configured as a trusted port, all the dynamic IP binding entries learned on that

port will be deleted.

2. When a client is connected on a trusted port, the dynamic IP binding entries will not be learned

on the switch, even though the client gets an IP address.

3.

If DHCPv4 snooping is enabled on two back-to-back access switches, DHCP packets will be
dropped, Since by default option 82 is enabled on DHCPv4 snooping and the default policy is
drop. The second switch with DHCPv4 snooping enabled drops the packets. In this scenario the
user should enable DHCPv4 snooping option 82 on one switch, or else you can disable on both.

DHCPv4 snooping commands

clear dhcpv4-snooping binding
clear dhcpv4-snooping binding {all | ip <IPV4-ADDR> vlan <VLAN-ID> | port <PORT-NUM> |
vlan <VLAN-ID>}

Description

Clears DHCPv4 snooping binding entries.

DHCP snooping | 120

| Parameter |     |     | Description                                            |     |
| --------- | --- | --- | ------------------------------------------------------ | --- |
| all       |     |     | SpecifiesthatallDHCPv4bindinginformationistobecleared. |     |
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
switch(config)#
|                 | clear | dhcpv4-snooping | binding all                                     |     |
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 121

Description
ClearsallDHCPv4snoopingstatistics.
Examples
ClearallDHCPv4snoopingstatistics:
| switch# clear   | dhcpv4-snooping | statistics |                                                 |
| --------------- | --------------- | ---------- | ----------------------------------------------- |
| Command History |                 |            |                                                 |
| Release         |                 |            | Modification                                    |
| 10.09.1000      |                 |            | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |                 |            | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
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
| switch(config)# | no  | dhcpv4-snooping |     |
| --------------- | --- | --------------- | --- |
| Command History |     |                 |     |
DHCPsnooping|122

| Release    |     |     | Modification                                    |
| ---------- | --- | --- | ----------------------------------------------- |
| 10.09.1000 |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09      |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
switch(config-vlan-100)#
exit
switch(config)#
| Command History |     |     |                                                 |
| --------------- | --- | --- | ----------------------------------------------- |
| Release         |     |     | Modification                                    |
| 10.09.1000      |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |     |     |     |
| ------------------- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 123

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping |                   | authorized-server |             |                  |
| --------------- | ----------------- | ----------------- | ----------- | ---------------- |
| dhcpv4-snooping | authorized-server |                   | <IPV4-ADDR> | [vrf <VRF-NAME>] |
no dhcpv4-snooping authorized-server <IPV4-ADDR> [vrf <VRF-NAME>]
Description
Addsanauthorized(trusted)DHCPservertoalistofauthorizedserversforusebyDHCPv4snooping.
Thiscommandcanbeissuedmultipletimes,addingamaximumof20authorizedserversperVRF.By
DHCPsnooping|124

default,withanemptylistofauthorizedservers,allDHCPserversareconsideredtobetrustedfor
DHCPv4snoopingpurposes.
ThemgmtVRFcannotbeusedwiththiscommand.
ThenoformofthiscommanddeletesthespecifiedDHCPserverfromtheauthorizedlist.
| Parameter      |     |     | Description                                      |     |     |
| -------------- | --- | --- | ------------------------------------------------ | --- | --- |
| <IPV4-ADDR>    |     |     | SpecifiestheIPv4addressofthetrustedDHCPv4server. |     |     |
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.Thenamemustbedefault.        |     |     |
Usage
Forauthorizedserverlookup,theVRFisderivedfromtheSwitchVirtualInterface(SVI)configuredfor
theincomingVLAN.IftheSVIisnotconfigured,thedefaultVRFisassumed.
Examples
AddingDHCPservers192.168.2.2,192.168.2.3,and192.168.2.10totheauthorizedserverlist:
| switch(config)# |     | dhcpv4-snooping | authorized-server | 192.168.2.2 |     |
| --------------- | --- | --------------- | ----------------- | ----------- | --- |
switch(config)# dhcpv4-snooping authorized-server 192.168.2.3 vrf default
switch(config)#
|     |     | dhcpv4-snooping | authorized-server | 192.168.2.10 | vrf default |
| --- | --- | --------------- | ----------------- | ------------ | ----------- |
RemovingDHCPserver192.168.2.3fromtheauthorizedserverlist:
switch(config)# no dhcpv4-snooping authorized-server 192.168.2.3 vrf default
| Command History |     |     |                                                 |     |     |
| --------------- | --- | --- | ----------------------------------------------- | --- | --- |
| Release         |     |     | Modification                                    |     |     |
| 10.09.1000      |     |     | Commandintroducedforthe8360SwitchSeries.        |     |     |
| 10.09           |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |
10.07orearlier
| Command Information |         |         |           |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Platforms           | Command | context | Authority |     |     |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |           | event-log        | client |     |     |
| ------------------ | --------- | ---------------- | ------ | --- | --- |
| dhcpv4-snooping    | event-log | client           |        |     |     |
| no dhcpv4-snooping |           | event-log client |        |     |     |
Description
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 125

Thiscommandenables/disablesDHCPv4clientleveleventlogsthathelpwithclienttelemetryona
remotemanagementstationsuchasArubaCentral.Bydefault,clientleveleventlogsaredisabled.The
noformofthiscommanddisablesclient-leveleventlogsforDHCPv4snoopingaftertheyareenabled.
ViewtheseloggedDHCPv4snoopingeventsbyissuingthecommandshow events -c dhcpv4-
snooping.
Examples
EnablingDHCPv4clientleveleventlogs:
| switch(config)# | # dhcpv4-snooping |     | event-log | client |
| --------------- | ----------------- | --- | --------- | ------ |
Disablingexternalstorage:
| witch(config)#      | # no    | dhcpv4-snooping | event-log          | client |
| ------------------- | ------- | --------------- | ------------------ | ------ |
| Command History     |         |                 |                    |        |
| Release             |         |                 | Modification       |        |
| 10.10               |         |                 | Commandintroduced. |        |
| Command Information |         |                 |                    |        |
| Platforms           | Command | context         | Authority          |        |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
DHCPsnooping|126

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
theIPbindingsfilewillbesaved.Beforerunningthedhcpv4-
snooping external-storage volumecommand,firstcreate
theexternalstoragevolumeusingcommandexternal-storage
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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |               | flash-storage |                 |
| ------------------ | ------------- | ------------- | --------------- |
| dhcpv4-snooping    | flash-storage |               | [delay <DELAY>] |
| no dhcpv4-snooping | flash-storage |               | [delay <DELAY>] |
Description
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 127

ConfiguresswitchflashstoragetobeusedforbackingupclientIPbindings(usedbyDHCPv4snooping).
Whenflashstorageisconfigured(andexternalstorageisnotalreadyconfiguredforthispurpose),the
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
| switch(config)# | no dhcpv4-snooping |     | flash-storage                                   |     |
| --------------- | ------------------ | --- | ----------------------------------------------- | --- |
| Command History |                    |     |                                                 |     |
| Release         |                    |     | Modification                                    |     |
| 10.09.1000      |                    |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |                    |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.08
DHCPsnooping|128

| Command Information |         |     |         |           |     |
| ------------------- | ------- | --- | ------- | --------- | --- |
| Platforms           | Command |     | context | Authority |     |
config
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
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
| Command History |     |     |     |                                                 |     |
| --------------- | --- | --- | --- | ----------------------------------------------- | --- |
| Release         |     |     |     | Modification                                    |     |
| 10.09.1000      |     |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
| Command Information |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 129

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
Whenremote-idisomitted,itsdefault(mac)isused.Whenuntrusted-policyisomitted,itsdefault
(drop)isused.
ThenoformofthiscommanddisablesDHCPv4snoopingoption82.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
remote-id
SpecifieswhataddresstouseastheremoteIDforthereplace
optionofuntrusted-policy.Specifyoneoftheseaddress
types:
| mac       |     |     | Thedefault.UsestheswitchMACaddressastheremoteID. |     |     |
| --------- | --- | --- | ------------------------------------------------ | --- | --- |
| subnet-ip |     |     | UsestheIPaddressoftheclientVLANastheremoteID.    |     |     |
untrusted-policy
SpecifieswhatactiontotakeforDHCPpackets(withoption82)
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
switch(config)# dhcpv4-snooping option 82 untrusted-policy keep
ConfiguringDHCPv4snoopingoption82withmgmt-ipastheremote-idandthereplaceaction:
DHCPsnooping|130

switch(config)# dhcpv4-snooping option 82 remote-id mgmt-ip untrusted-policy
replace
DisablingDHCPv4snoopingoption82:
switch(config)# no dhcpv4-snooping option 82 untrusted-policy keep
| Command History |     |     |                                                 |
| --------------- | --- | --- | ----------------------------------------------- |
| Release         |     |     | Modification                                    |
| 10.09.1000      |     |     | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |     | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 config Administratorsorlocalusergroupmemberswithexecution
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 131

| switch(config)#     |         | no dhcpv4-snooping |     | static-attributes  |
| ------------------- | ------- | ------------------ | --- | ------------------ |
| Command History     |         |                    |     |                    |
| Release             |         |                    |     | Modification       |
| 10.10               |         |                    |     | Commandintroduced. |
| Command Information |         |                    |     |                    |
| Platforms           | Command | context            |     | Authority          |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| Command Information |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
DHCPsnooping|132

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv4-snooping    |        | verify mac |     |
| ------------------ | ------ | ---------- | --- |
| dhcpv4-snooping    | verify | mac        |     |
| no dhcpv4-snooping | verify | mac        |     |
Description
ThiscommandenablesverificationofthehardwareaddressfieldinDHCPclientpackets.Whenenabled,
theDHCPclienthardwareaddressfieldandthesourceMACaddressmustbethesameforpackets
receivedonuntrustedportsorelsethepacketisdropped.ThisDHCPsnoopingMACverificationis
enabledbydefault.
ThenoformofthecommanddisablesDHCPv4snoopingMACverification.
Examples
EnablingDHCPv4snoopingMACverification:
| switch(config)# | dhcpv4-snooping |     | verify mac |
| --------------- | --------------- | --- | ---------- |
DisablingDHCPv4snoopingMACverification:
| switch(config)# | no  | dhcpv4-snooping | verify mac                                      |
| --------------- | --- | --------------- | ----------------------------------------------- |
| Command History |     |                 |                                                 |
| Release         |     |                 | Modification                                    |
| 10.09.1000      |     |                 | Commandintroducedforthe8360SwitchSeries.        |
| 10.09           |     |                 | Commandintroducedforthe6000and6100SwitchSeries. |
10.07orearlier
| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show dhcpv4-snooping
show dhcpv4-snooping
Description
ShowstheDHCPv4snoopingconfiguration.
Examples
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 133

ShowingtheDHCPv4snoopingconfiguration:
| switch(config)# |                | show           | dhcpv4-snooping |                    |            |         |         |
| --------------- | -------------- | -------------- | --------------- | ------------------ | ---------- | ------- | ------- |
| DHCPv4-Snooping |                | Information    |                 |                    |            |         |         |
| DHCPv4-Snooping |                |                |                 | : Yes              | Verify MAC | Address | : Yes   |
| Allow Overwrite |                | Binding        |                 | : No               | Enabled    | VLANs   | : 1-100 |
| IP Binding      | Disabled       |                | VLANs           | :                  |            |         |         |
| Static          | Attributes     |                | : Yes           |                    |            |         |         |
| Client          | Event          | Logs           | : No            |                    |            |         |         |
| Option 82       | Configurations |                |                 |                    |            |         |         |
| Untrusted       | Policy         |                | :               | replace            | Insertion  |         | : Yes   |
| Option          | 82 Remote-id   |                | :               | mac                |            |         |         |
| External        | Storage        | Information    |                 |                    |            |         |         |
| Volume          | Name           | : ipbinding    |                 |                    |            |         |         |
| File Name       | :              | ipv4Bindings   |                 |                    |            |         |         |
| Inactive        | Since          | : 01:23:20     |                 | 09/10/2021         |            |         |         |
| Error :         | File           | Write          | Failure         |                    |            |         |         |
| Flash Storage   |                | Information    |                 |                    |            |         |         |
| File Write      | Delay          | :              | 300 seconds     |                    |            |         |         |
| Active Storage  |                | : External     |                 |                    |            |         |         |
| Authorized      | Server         | Configurations |                 |                    |            |         |         |
| VRF             |                |                |                 | Authorized         | Servers    |         |         |
| ------------    |                |                |                 | ------------------ |            |         |         |
| default         |                |                |                 | 1.1.10.3           |            |         |         |
| default         |                |                |                 | 10.10.10.1         |            |         |         |
| default         |                |                |                 | 10.10.10.56        |            |         |         |
| default         |                |                |                 | 200.10.10.3        |            |         |         |
| green           |                |                |                 | 1.1.10.3           |            |         |         |
| green           |                |                |                 | 1.10.10.3          |            |         |         |
| green           |                |                |                 | 10.10.100.3        |            |         |         |
| red             |                |                |                 | 192.168.122.53     |            |         |         |
| red             |                |                |                 | 192.168.122.121    |            |         |         |
Port Information
|          |       | Max      |     | Static   | Dynamic  |     |     |
| -------- | ----- | -------- | --- | -------- | -------- | --- | --- |
| Port     | Trust | Bindings |     | Bindings | Bindings |     |     |
| -------- | ----- | -------- |     | -------- | -------- |     |     |
| 1/1/2    | Yes   | 5000     |     | 50       | 0        |     |     |
| 1/1/3    | Yes   | 8192     |     | 0        | 0        |     |     |
| 1/1/5    | Yes   | 8192     |     | 0        | 22       |     |     |
| 1/1/16   | No    | 100      |     | 0        | 0        |     |     |
| 10/10/10 | No    | 8100     |     | 320      | 200      |     |     |
| lag120   | No    | 512      |     | 0        | 0        |     |     |
Command History
| Release    |     |     |     |     | Modification                             |     |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- |
| 10.09.1000 |     |     |     |     | Commandintroducedforthe8360SwitchSeries. |     |     |
DHCPsnooping|134

| Release |     |     |     | Modification                                    |     |     |
| ------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
| 10.09   |     |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |     |
| 10.08   |     |     |     | Updatedexamplewithflashstorageinformation.      |     |     |
10.07orearlier
| Command Information |         |         |     |           |     |     |
| ------------------- | ------- | ------- | --- | --------- | --- | --- |
| Platforms           | Command | context |     | Authority |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
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
| VLAN Id :       | 2, MAC      | : 00:50:56:96:74:46  |                     |         |         |     |
| IP              |             | Interface            | Time-Left           |         |         |     |
| --------------- |             | ---------            | ------------------- |         |         |     |
| 100.1.2.100     |             | 1/1/23               | 194                 |         |         |     |
| Static          | Attributes: |                      |                     |         |         |     |
| Default         | Router      | : 100.1.2.1,         | 192.1.1.1,          |         | 1.1.1.2 |     |
| Server          | IP          | : 10.1.84.2          |                     |         |         |     |
| Name Servers    |             | : 192.1.1.2,         | 2.2.2.2,            |         | 1.1.1.1 |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 135

| VLAN Id :       | 3, MAC      | : 00:50:56:96:e5:8e |                     |                                                 |             |     |
| --------------- | ----------- | ------------------- | ------------------- | ----------------------------------------------- | ----------- | --- |
| IP              |             | Interface           | Time-Left           |                                                 |             |     |
| --------------- |             | ---------           | ------------------- |                                                 |             |     |
| 100.1.3.100     |             | 2/1/22              | 145                 |                                                 |             |     |
| Static          | Attributes: |                     |                     |                                                 |             |     |
| Default         | Router      | : 100.1.3.1,        | 192.1.1.1,          |                                                 | 1.1.1.2     |     |
| Server          | IP          | : 10.1.84.2         |                     |                                                 |             |     |
| Name Servers    |             | : 192.1.1.2,        | 2.2.2.2,            |                                                 | 1.1.1.1     |     |
| VLAN Id :       | 3, MAC      | : 00:11:01:00:00:03 |                     |                                                 |             |     |
| IP              |             | Interface           | Time-Left           |                                                 |             |     |
| --------------- |             | ---------           | ------------------- |                                                 |             |     |
| 100.1.3.99      |             | 2/1/24              | 137                 |                                                 |             |     |
| Static          | Attributes: |                     |                     |                                                 |             |     |
| Default         | Router      | : 100.1.3.1,        | 192.1.1.1,          |                                                 | 1.1.1.2     |     |
| Server          | IP          | : 10.1.84.2         |                     |                                                 |             |     |
| Name Servers    |             | :192.168.0.1,       | 192.168.1.1,        |                                                 | 192.168.2.1 |     |
| Command History |             |                     |                     |                                                 |             |     |
| Release         |             |                     |                     | Modification                                    |             |     |
| 10.10           |             |                     |                     | Detailparameteradded.                           |             |     |
| 10.09.1000      |             |                     |                     | Commandintroducedforthe8360SwitchSeries.        |             |     |
| 10.09           |             |                     |                     | Commandintroducedforthe6000and6100SwitchSeries. |             |     |
10.07orearlier
| Command Information |         |         |     |                                                      |     |     |
| ------------------- | ------- | ------- | --- | ---------------------------------------------------- | --- | --- |
| Platforms           | Command | context |     | Authority                                            |     |     |
| 6200                |         |         |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv4-snooping |     |            | statistics |     |     |     |
| -------------------- | --- | ---------- | ---------- | --- | --- | --- |
| show dhcpv4-snooping |     | statistics |            |     |     |     |
Description
ShowstheDHCPv4snoopingstatistics.
Examples
ShowingtheDHCPv4snoopingstatistics:
| switch(config)# |        | show dhcpv4-snooping |     | statistics |     |       |
| --------------- | ------ | -------------------- | --- | ---------- | --- | ----- |
| Packet-Type     | Action | Reason               |     |            |     | Count |
DHCPsnooping|136

| ----------- |         | ------- | ----------------------------- |         |                                                 |           |       | --------- |
| ----------- | ------- | ------- | ----------------------------- | ------- | ----------------------------------------------- | --------- | ----- | --------- |
| server      |         | forward | from                          | trusted | port                                            |           |       | 5425      |
| client      |         | forward | to                            | trusted | port                                            |           |       | 3895      |
| server      |         | drop    | received                      |         | on untrusted                                    |           | port  | 117       |
| server      |         | drop    | unauthorized                  |         | server                                          |           |       | 214       |
| client      |         | drop    | destination                   |         | on                                              | untrusted | port  | 78        |
| client      |         | drop    | untrusted                     |         | option                                          | 82        | field | 85        |
| client      |         | drop    | bad                           | DHCP    | release                                         | request   |       | 0         |
| client      |         | drop    | failed                        |         | verify                                          | MAC check |       | 5         |
| client      |         | drop    | failed                        |         | on max-binding                                  |           | limit | 15        |
| Command     | History |         |                               |         |                                                 |           |       |           |
| Release     |         |         |                               |         | Modification                                    |           |       |           |
| 10.09.1000  |         |         |                               |         | Commandintroducedforthe8360SwitchSeries.        |           |       |           |
| 10.09       |         |         |                               |         | Commandintroducedforthe6000and6100SwitchSeries. |           |       |           |
10.07orearlier
| Command   | Information |         |         |     |           |     |     |     |
| --------- | ----------- | ------- | ------- | --- | --------- | --- | --- | --- |
| Platforms |             | Command | context |     | Authority |     |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
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
ip <IPV6-ADDR> vlan <VLAN-ID> SpecifiestheIPv6addressandVLANforwhichallDHCPv6binding
informationistobecleared.
| interface | <IFNAME> |     |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
SpecifiestheinterfaceforwhichallDHCPv6bindinginformationis
tobecleared.
vlan <VLAN-ID> SpecifiestheVLANforwhichallDHCPv6bindinginformationisto
becleared.Range:1to4094.
Examples
ClearingallDHCPv6bindinginformationfor5000::1vlan1:
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 137

switch(config)# clear dhcpv6-snooping binding ip 5000::1 vlan 1
ClearingallDHCPv6bindinginformationforinterface1/1/10:
| switch(config)# | clear | dhcpv6-snooping | binding | interface | 1/1/10 |
| --------------- | ----- | --------------- | ------- | --------- | ------ |
ClearingallDHCPv6bindinginformationforVLAN10:
| switch(config)# | clear | dhcpv6-snooping | binding | vlan | 10  |
| --------------- | ----- | --------------- | ------- | ---- | --- |
ClearingallDHCPv6bindinginformation:
| switch(config)# | clear | dhcpv6-snooping | binding                                         | all |     |
| --------------- | ----- | --------------- | ----------------------------------------------- | --- | --- |
| Command History |       |                 |                                                 |     |     |
| Release         |       |                 | Modification                                    |     |     |
| 10.09.1000      |       |                 | Commandintroducedforthe8360SwitchSeries.        |     |     |
| 10.09           |       |                 | Commandintroducedforthe6000and6100SwitchSeries. |     |     |
10.07orearlier
| Command Information |         |         |           |     |     |
| ------------------- | ------- | ------- | --------- | --- | --- |
| Platforms           | Command | context | Authority |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
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
DHCPsnooping|138

| switch# clear | dhcpv6-snooping | guard-policy | statistics | vlan 100 |
| ------------- | --------------- | ------------ | ---------- | -------- |
ClearingallDHCPv6snoopingguardpolicystatisticsfrominterface1/1/10:
switch# clear dhcpv6-snooping guard-policy statistics interface 1/1/10
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.10               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| clear dhcpv6-snooping |     | statistics |     |     |
| --------------------- | --- | ---------- | --- | --- |
| clear dhcpv6-snooping |     | statistics |     |     |
Description
ClearsallDHCPv6snoopingstatistics.
Examples
ClearallDHCPv6snoopingstatistics:
| switch# clear   | dhcpv6-snooping | statistics |                                                 |     |
| --------------- | --------------- | ---------- | ----------------------------------------------- | --- |
| Command History |                 |            |                                                 |     |
| Release         |                 |            | Modification                                    |     |
| 10.09.1000      |                 |            | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |                 |            | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 139

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
config
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
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
DHCPsnooping|140

| switch(config)# | vlan | 100 |     |
| --------------- | ---- | --- | --- |
switch(config-vlan-100)#
dhcpv6-snooping
| switch(config-vlan-100)# |     | exit |     |
| ------------------------ | --- | ---- | --- |
switch(config)#
DisablingDHCPv6snoopingonVLAN100:
| switch(config)#          | vlan | 100                |     |
| ------------------------ | ---- | ------------------ | --- |
| switch(config-vlan-100)# |      | no dhcpv6-snooping |     |
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
6200 config-vlan Administratorsorlocalusergroupmemberswithexecution
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 141

| Parameter   |     |     | Description                                      |     |
| ----------- | --- | --- | ------------------------------------------------ | --- |
| <IPV6-ADDR> |     |     | SpecifiestheIPv6addressofthetrustedDHCPv6server. |     |
vrf <VRF-NAME>
SpecifiestheVRFname.Thenamemustbedefault.
Usage
Forauthorizedserverlookup,theVRFisderivedfromtheSwitchVirtualInterface(SVI)configuredfor
theincomingVLAN.IftheSVIisnotconfigured,thedefaultVRFisassumed.
Examples
AddingDHCPserversABCD:5ACD::2000,andABCD:5ACD::2010totheauthorizedserverlist:
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
switch(config)# dhcpv6-snooping authorized-server ABCD:5ACD::2010 vrf default
RemovingDHCPserverABCD:5ACD::2000fromtheauthorizedserverlist:
switch(config)# no dhcpv6-snooping authorized-server ABCD:5ACD::2000 vrf default
| Command History     |         |         |                   |     |
| ------------------- | ------- | ------- | ----------------- | --- |
| Release             |         |         | Modification      |     |
| 10.07orearlier      |         |         | Commandintroduced |     |
| Command Information |         |         |                   |     |
| Platforms           | Command | context | Authority         |     |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping    |           | event-log        | client |     |
| ------------------ | --------- | ---------------- | ------ | --- |
| dhcpv6-snooping    | event-log | client           |        |     |
| no dhcpv6-snooping |           | event-log client |        |     |
Description
Thiscommandenables/disablesDHCPv6clientleveleventlogsthathelpwithclienttelemetryona
remotemanagementstationsuchasArubaCentral.Bydefault,clientleveleventlogsaredisabled.The
noformofthiscommanddisablesclient-leveleventlogsforDHCPv6snoopingaftertheyareenabled.
ViewtheseloggedDHCPv6snoopingeventsbyissuingthecommandshow
events -c dhcpv6-
snooping.
Examples
EnablingDHCPv6clientleveleventlogs:
| switch(config)# |     | # dhcpv6-snooping | event-log | client |
| --------------- | --- | ----------------- | --------- | ------ |
DHCPsnooping|142

Disablingexternalstorage:
| witch(config)#      | # no    | dhcpv6-snooping | event-log          | client |
| ------------------- | ------- | --------------- | ------------------ | ------ |
| Command History     |         |                 |                    |        |
| Release             |         |                 | Modification       |        |
| 10.10               |         |                 | Commandintroduced. |        |
| Command Information |         |                 |                    |        |
| Platforms           | Command | context         | Authority          |        |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| dhcpv6-snooping |     | external-storage |     |     |
| --------------- | --- | ---------------- | --- | --- |
dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
no dhcpv6-snooping external-storage volume <VOL-NAME> file <FILE-NAME>
Description
ConfiguresexternalstoragetobeusedforbackingupIPv6bindings(usedbyDHCPv6snooping)toa
file.Whenconfigured,theswitchstoresalltheIPbindingsinanexternalstoragefilesothattheyare
retainedaftertheswitchrestarts.Whentheswitchrestarts,itreadstheIPv6bindingsfromthe
configuredexternalstoragefiletopopulateitslocalcache.
WhenbothexternalstorageandflashstorageareconfiguredtostoreDHCPsnoopingIPbindings,theexternal
storagetakespriority,andisusedexclusivelyuntilitbecomesunconfigured,atwhichtimeflashstorage(if
configured)isused.Later,ifexternalstorageisconfiguredagain,flashstoragestopsandexternalstorage
resumes.
ThenoformofthiscommanddisablesthesavingofIPv6bindingsinanexternalstoragefile.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
volume <VOL-NAME> Specifiesthenameoftheexistingexternalstoragevolumewhere
theIPv6bindingsfilewillbesaved.Beforerunningthedhcpv6-
|     |     |     | snooping | external-storage volumecommand,firstcreate |
| --- | --- | --- | -------- | ------------------------------------------ |
theexternalstoragevolumeusingcommandexternal-storage
<VOLUME-NAME>.SeeExternalstoragecommandsintheCommand-
LineInterfaceGuide.
file <FILE-NAME> SpecifiesthefilenametouseforstoringIPv6bindings.Maximum
255characters.
Examples
ConfiguringIPv6bindingsstorageinfileipv6Bindingsonexistingvolumedhcp_snoop:
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 143

switch(config)# dhcpv6-snooping external-storage volume dhcp_snoop file
ipv6Bindings
Disablingexternalstorage:
switch(config)# no dhcpv6-snooping external-storage volume dhcp_snoop
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
6200 config Administratorsorlocalusergroupmemberswithexecution
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
DHCPsnooping|144

WhenbothexternalstorageandflashstorageareconfiguredtostoreDHCPsnoopingIPbindings,theexternal
storagetakespriority,andisusedexclusivelyuntilitbecomesunconfigured,atwhichtimeflashstorage(if
configured)isused.Later,ifexternalstorageisconfiguredagain,flashstoragestopsandexternalstorage
resumes.
ThenoformofthiscommanddisablesthesavingofIPbindingsinflashstorage.
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
config
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- |
rightsforthiscommand.
| dhcpv6-snooping    |              | max-bindings |                |     |     |
| ------------------ | ------------ | ------------ | -------------- | --- | --- |
| dhcpv6-snooping    | max-bindings |              | <MAX-BINDINGS> |     |     |
| no dhcpv6-snooping | max-bindings |              | <MAX-BINDINGS> |     |     |
Description
SetsthemaximumnumberofDHCPv6bindingsallowedontheselectedinterface.Forallinterfaceson
whichthiscommandisnotrun,thedefaultmaxbindingisthemaximumvalueoftherange.
Thenoformofthecommandrevertsmaxbindingsfortheselectedinterfacetoitsdefault.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 145

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<MAX-BINDINGS> SpecifiesthemaximumnumberofDHCPbindings.Range0to
1024.
Examples
SettheDHCPv6maxbindingsto256oninterface1/1/1:
| switch(config)#    |     | interface       | 1/1/1 |              |     |
| ------------------ | --- | --------------- | ----- | ------------ | --- |
| switch(config-if)# |     | dhcpv6-snooping |       | max-bindings | 256 |
| switch(config-if)# |     | exit            |       |              |     |
switch(config)#
RevertDHCPv6maxbindingstoitsdefaultoninterface1/1/1:
switch(config)#
|                    |     | interface          | 1/1/1 |              |     |
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
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
DHCPsnooping|146

| switch(config-if)# |     | exit |     |     |     |     |
| ------------------ | --- | ---- | --- | --- | --- | --- |
switch(config)#
DisablingDHCPv6snoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface | 2/2/1              |     |       |     |
| ------------------ | --- | --------- | ------------------ | --- | ----- | --- |
| switch(config-if)# |     |           | no dhcpv6-snooping |     | trust |     |
| switch(config-if)# |     |           | exit               |     |       |     |
switch(config)#
| Command   | History     |     |         |                   |     |     |
| --------- | ----------- | --- | ------- | ----------------- | --- | --- |
| Release   |             |     |         | Modification      |     |     |
| 10.07     |             |     |         | Commandintroduced |     |     |
| Command   | Information |     |         |                   |     |     |
| Platforms | Command     |     | context | Authority         |     |     |
config
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswithexecution |     |     |
| ---- | --- | --- | --- | -------------------------------------------------- | --- | --- |
rightsforthiscommand.
| match server    |             | access-list |            |     |     |     |
| --------------- | ----------- | ----------- | ---------- | --- | --- | --- |
| match server    | access-list |             | <ACL-NAME> |     |     |     |
| no match server |             | access-list | <ACL-NAME> |     |     |     |
Description
ConfiguresanaccesslisttoaDHCPv6snoopingguardpolicy,enablingtheDHCPv6snoopingguard
policytoallowordenythespecificDHCPservertoassignanIPv6address.Ifnofiltersareapplied,DHCP
servertrafficfromanysourceIPaddressisallowedinthetrustedport.
ThenoformofthecommandremovesthespecifiedaccesslistfromtheDHCPv6snoopingguardpolicy.
| Parameter  |     |     |     | Description                                     |     |     |
| ---------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
| <ACL-NAME> |     |     |     | SpecifiesthenameoftheIPv6accesslisttobematched. |     |     |
Examples
Creatinganaccess-listacl1onDHCPv6snoopingguardpolicypol1:
| switch(config)# |     | dhcpv6-snooping |     | guard-policy |     | pol1 |
| --------------- | --- | --------------- | --- | ------------ | --- | ---- |
switch(config-dhcpv6-guard-policy)# match server access-list acl1
Deletingtheaccesslistacl1fromtheDHCPv6snoopingguardpolicypol1:
| switch(config)# |     | dhcpv6-snooping |     | guard-policy |     | pol1 |
| --------------- | --- | --------------- | --- | ------------ | --- | ---- |
switch(config-dhcpv6-guard-policy)# no match server access-list acl1
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 147

| Command   | History     |     |         |                    |           |     |
| --------- | ----------- | --- | ------- | ------------------ | --------- | --- |
| Release   |             |     |         | Modification       |           |     |
| 10.10     |             |     |         | Commandintroduced. |           |     |
| Command   | Information |     |         |                    |           |     |
| Platforms | Command     |     | context |                    | Authority |     |
6200 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
| match client    |             | prefix-list |                    |     |     |     |
| --------------- | ----------- | ----------- | ------------------ | --- | --- | --- |
| match client    | prefix-list |             | <PREFIX-LIST-NAME> |     |     |     |
| no match client |             | prefix-list | <PREFIX-LIST-NAME> |     |     |     |
Description
Configuresaprefix-listfortheDHCPv6snoopingguardpolicyenablingthepolicytoallowtheassigned
IPv6addresseswithinaspecificprefixrange.
ThenoformofthecommandremovesaprefixlistfromtheDHCPv6snoopingguardpolicy.
| Parameter          |     |     |     | Description                          |     |     |
| ------------------ | --- | --- | --- | ------------------------------------ | --- | --- |
| <PREFIX-LIST-NAME> |     |     |     | SpecifiesthenameoftheIPv6prefixlist. |     |     |
Examples
Addingaprefixlistnamedpref1tothepol1DHCPv6snoopingguardpolicy:
switch(config)# ipv6 prefix-list pref1 permit 2001:db8::/64 le 128
| switch(config)#                     |     | dhcpv6-snooping |     | guard-policy | pol1        |             |
| ----------------------------------- | --- | --------------- | --- | ------------ | ----------- | ----------- |
| switch(config-dhcpv6-guard-policy)# |     |                 |     | match        | client      | prefix-list |
| <ipv6-prefix-list-name>             |     |                 |     | IPv6         | prefix-list | name        |
switch(config-dhcpv6-guard-policy)# match client prefix-list pref1
Deletingtheprefixlistnamedprf1fromthepol1DHCPv6snoopingguardpolicy:
| switch(config)# |     | dhcpv6-snooping |     | guard-policy | pol1 |     |
| --------------- | --- | --------------- | --- | ------------ | ---- | --- |
switch(config-dhcpv6-guard-policy)# no match client prefix-list <ipv6-prefix-list-
name>
| Command | History     |     |     |                    |     |     |
| ------- | ----------- | --- | --- | ------------------ | --- | --- |
| Release |             |     |     | Modification       |     |     |
| 10.10   |             |     |     | Commandintroduced. |     |     |
| Command | Information |     |     |                    |     |     |
DHCPsnooping|148

| Platforms | Command |     | context |     |     | Authority |
| --------- | ------- | --- | ------- | --- | --- | --------- |
6200 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
preference
| preference | [minimum | |   | maximum | ] <VALUE> |     |     |
| ---------- | -------- | --- | ------- | --------- | --- | --- |
no preference
Description
EnablesaDHCPv6snoopingguardpolicytoallowordenytheDHCPv6serversinthespecifiedserver
preferencerange.Ifnotconfiguredtheminimumpreferenceissetto0andmaximumpreferenceisset
to255.
ThenoformofthecommandremovestheserverpreferencelimitsonthespecifiedDHCPv6snooping
guardpolicy.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
minimum <VALUE> Specifiestheminimumvaluefortheserverpreferencerange.
Range:1-255.
maximum <VALUE> Specifiesthemaximumvaluefortheserverpreferencerange.
Range:1-255.
Examples
Settingtheminimumandmaximumserverpreferencerangeto6-250onDHCPv6snoopingguardpolicy
pol1:
| switch(config)#                     |     | dhcpv6-snooping |     | guard-policy |            | pol1    |
| ----------------------------------- | --- | --------------- | --- | ------------ | ---------- | ------- |
| switch(config-dhcpv6-guard-policy)# |     |                 |     |              | preference | min 6   |
| switch(config-dhcpv6-guard-policy)# |     |                 |     |              | preference | max 250 |
DisablingtheserverpreferencerangeonDHCPv6snoopingguardpolicypol1:
| switch(config)#                     |             | dhcpv6-snooping |         | guard-policy |                    | pol1       |
| ----------------------------------- | ----------- | --------------- | ------- | ------------ | ------------------ | ---------- |
| switch(config-dhcpv6-guard-policy)# |             |                 |         |              | no                 | preference |
| Command                             | History     |                 |         |              |                    |            |
| Release                             |             |                 |         |              | Modification       |            |
| 10.10                               |             |                 |         |              | Commandintroduced. |            |
| Command                             | Information |                 |         |              |                    |            |
| Platforms                           | Command     |                 | context |              |                    | Authority  |
6200 config-dhcpv6-guard-policy Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 149

show dhcpv6-snooping
show dhcpv6-snooping
Description
ShowstheDHCPv6snoopingconfiguration.
Examples
ShowingtheDHCPv6snoopingconfiguration:
| switch(config)# |             | show dhcpv6-snooping |              |            |                                         |                 |
| --------------- | ----------- | -------------------- | ------------ | ---------- | --------------------------------------- | --------------- |
| DHCPv6-Snooping |             | Information          |              |            |                                         |                 |
| DHCPv6-Snooping |             |                      | : Yes        | Enabled    | VLANs                                   | : 1,5,7,100-110 |
| External        | Storage     | Information          |              |            |                                         |                 |
| Volume          | Name        |                      | : dhcp_snoop |            |                                         |                 |
| File Name       |             |                      | : ip_binding |            |                                         |                 |
| Inactive        | Since       |                      | : 01:23:20   | 09/10/2021 |                                         |                 |
| Error           |             |                      | : Failed     | to write   | external                                | storage         |
| Flash Storage   | Information |                      |              |            |                                         |                 |
| File Write      | Delay       | : 300                | seconds      |            |                                         |                 |
| Active Storage  |             | : External           |              |            |                                         |                 |
| Authorized      | Server      | Configurations       |              |            |                                         |                 |
| VRF             |             |                      |              |            | Authorized                              | Servers         |
| ------------    |             |                      |              |            | ------------------                      |                 |
| default         |             |                      |              |            | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 |                 |
| default         |             |                      |              |            | 2002::2                                 |                 |
| default         |             |                      |              |            | 2004::1                                 |                 |
| red             |             |                      |              |            | 2002::1                                 |                 |
| red             |             |                      |              |            | 2002::2                                 |                 |
| red             |             |                      |              |            | 2002::9                                 |                 |
| green           |             |                      |              |            | 5000::1                                 |                 |
| green           |             |                      |              |            | 5000::2                                 |                 |
| green           |             |                      |              |            | 5000::3                                 |                 |
| green           |             |                      |              |            | 5000::7                                 |                 |
| green           |             |                      |              |            | 5000::8                                 |                 |
Port Information
|          |       | Max      | Static   |     | Dynamic  |     |
| -------- | ----- | -------- | -------- | --- | -------- | --- |
| Port     | Trust | Bindings | Bindings |     | Bindings |     |
| -------- | ----- | -------- | -------- |     | -------- |     |
| 1/1/2    | Yes   | 0        | 0        |     | 0        |     |
| 1/1/3    | Yes   | 0        | 3        |     | 0        |     |
| 1/1/5    | Yes   | 0        | 22       |     | 0        |     |
| 1/1/16   | No    | 256      | 0        |     | 20       |     |
| 10/10/10 | No    | 256      | 12       |     | 7        |     |
| lag120   | No    | 256      | 3        |     | 0        |     |
Command History
DHCPsnooping|150

| Release             |         |         | Modification                                         |     |
| ------------------- | ------- | ------- | ---------------------------------------------------- | --- |
| 10.08               |         |         | Updatedexamplewithflashstorageinformation.           |     |
| 10.07orearlier      |         |         | Commandintroduced                                    |     |
| Command Information |         |         |                                                      |     |
| Platforms           | Command | context | Authority                                            |     |
| 6200                |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |         | binding |     |
| -------------------- | --- | ------- | ------- | --- |
| show dhcpv6-snooping |     | binding |         |     |
Description
ShowstheDHCPv6snoopingbindingconfiguration.
Examples
ShowingtheDHCPv6snoopingbindingconfiguration:
| switch# show | dhcpv6-snooping |     | binding |     |
| ------------ | --------------- | --- | ------- | --- |
| IP Binding   | Information     |     |         |     |
======================
| MAC-ADDRESS |     | IPV6-ADDRESS |     | VLAN INTERFACE |
| ----------- | --- | ------------ | --- | -------------- |
TIME-LEFT
---------------- ---------------------------------------- ---- --------- ----
------
00:50:56:96:e4:cf aaaa:bbbb:cccc:dddd:eeee:1234:5678:abcd 1 1/1/1
584
| 00:50:56:96:04:4d |     | 1000::3 |     | 134 1/1/2 |
| ----------------- | --- | ------- | --- | --------- |
435
| 00:50:56:96:d8:3d |     | 2000:1000::4 |     | 2002 lag123 |
| ----------------- | --- | ------------ | --- | ----------- |
21234
| Command History |     |     |                                                 |     |
| --------------- | --- | --- | ----------------------------------------------- | --- |
| Release         |     |     | Modification                                    |     |
| 10.09.1000      |     |     | Commandintroducedforthe8360SwitchSeries.        |     |
| 10.09           |     |     | Commandintroducedforthe6000and6100SwitchSeries. |     |
10.07orearlier
| Command Information |         |         |           |     |
| ------------------- | ------- | ------- | --------- | --- |
| Platforms           | Command | context | Authority |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 151

| Platforms | Command |     | context | Authority                                             |     |     |     |
| --------- | ------- | --- | ------- | ----------------------------------------------------- | --- | --- | --- |
|           | (#)     |     |         | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
commandfromtheoperatorcontext(>)only.
| dhcpv6-snooping    |              | guard-policy |               |               |     |     |     |
| ------------------ | ------------ | ------------ | ------------- | ------------- | --- | --- | --- |
| dhcpv6-snooping    | guard-policy |              | <POLICY-NAME> |               |     |     |     |
| no dhcpv6-snooping |              | guard-policy |               | <POLICY-NAME> |     |     |     |
Description
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
| switch(config)#          |     | vlan 100 |                 |                    |              |     |      |
| ------------------------ | --- | -------- | --------------- | ------------------ | ------------ | --- | ---- |
| switch(config-vlan-100)# |     |          | dhcpv6-snooping |                    | guard-policy |     | pol1 |
| Command History          |     |          |                 |                    |              |     |      |
| Release                  |     |          |                 | Modification       |              |     |      |
| 10.10                    |     |          |                 | Commandintroduced. |              |     |      |
DHCPsnooping|152

| Command   | Information |         |     |         |     |           |
| --------- | ----------- | ------- | --- | ------- | --- | --------- |
| Platforms |             | Command |     | context |     | Authority |
config
| 6200 |     |           |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --------- | --- | --- | --- | ----------------------------------------- |
|      |     | config-if |     |     |     | executionrightsforthiscommand.            |
config-dhcpv6-guard-policy
config-vlan-<VLAN-ID>
| show | dhcpv6-snooping |     |                             |     | guard-policy |     |
| ---- | --------------- | --- | --------------------------- | --- | ------------ | --- |
| show | dhcpv6-snooping |     | guard-policy[<POLICY_NAME>] |     |              |     |
Description
ShowstheDHCPv6snoopingguardpolicyconfiguration.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<POLICY-NAME>
SpecifiestheDHCPv6snoopingguardpolicyforwhichthe
informationisdisplayed.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfiguration:
| switch# | show            | dhcpv6-snooping |              |      | guard-policy |       |
| ------- | --------------- | --------------- | ------------ | ---- | ------------ | ----- |
|         | DHCPv6-Snooping |                 | guard-policy |      | Information  |       |
|         | DHCPV6          | Guard           | Policy       | name | : POL1       |       |
|         | Attached        | Access          |              | List | : ACL1       |       |
|         | Attached        | Prefix          |              | List | : PRF1       |       |
|         | Preference      |                 | Range        |      | : 0-255      |       |
|         | Applied         | on              | VLAN         |      | : 5,7        |       |
|         | Applied         | on              | Port         |      |              |       |
|         | DHCPV6          | Guard           | Policy       | name | : POL2       |       |
|         | Attached        | Access          |              | List | : ACL2       |       |
|         | Attached        | Prefix          |              | List | : PRF2       |       |
|         | Preference      |                 | Range        |      | : 2-20       |       |
|         | Applied         | on              | VLAN         |      |              |       |
|         | Applied         | on              | Port         |      | : 1/1/1,     | 1/1/2 |
|         | DHCPV6          | Guard           | Policy       | name | : POL3       |       |
|         | Attached        | Access          |              | List | : ACL3       |       |
|         | Attached        | Prefix          |              | List | : PRF3       |       |
|         | Preference      |                 | Range        |      | : 3-60       |       |
|         | Applied         | on              | VLAN         |      | : 4,6        |       |
|         | Applied         | on              | Port         |      |              |       |
ShowingtheDHCPv6snoopingguardpolicyconfigurationforthepolicynamedPOLICY_NAME1:
| switch# | show            | dhcpv6-snooping |              |     | guard-policy | POLICY_NAME1 |
| ------- | --------------- | --------------- | ------------ | --- | ------------ | ------------ |
|         | DHCPv6-Snooping |                 | guard-policy |     | Information  |              |
========================
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 153

|     | DHCPV6     | Guard  | Policy |      | name | : POLICY_NAME1 |     |     |
| --- | ---------- | ------ | ------ | ---- | ---- | -------------- | --- | --- |
|     | Attached   | Access |        | List |      | : ACL1         |     |     |
|     | Attached   | Prefix |        | List |      | : PRF1         |     |     |
|     | Preference |        | Range  |      |      | : 0-255        |     |     |
vsx-sync
|           | Applied     | on      | VLAN |         |     | : 5,7              |       |     |
| --------- | ----------- | ------- | ---- | ------- | --- | ------------------ | ----- | --- |
|           | Applied     | on      | Port |         |     | : 1/1/1,           | 1/1/2 |     |
| Command   | History     |         |      |         |     |                    |       |     |
| Release   |             |         |      |         |     | Modification       |       |     |
| 10.10     |             |         |      |         |     | Commandintroduced. |       |     |
| Command   | Information |         |      |         |     |                    |       |     |
| Platforms |             | Command |      | context |     | Authority          |       |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show | dhcpv6-snooping |     |              |     | guard-policy |            | interface         |     |
| ---- | --------------- | --- | ------------ | --- | ------------ | ---------- | ----------------- | --- |
| show | dhcpv6-snooping |     | guard-policy |     |              | [interface | <INTERFACE-NAME>] |     |
Description
ShowstheDHCPv6snoopingguardpolicyconfigurationandstatisticsforthespecifiedinterface.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
<INTERFACE-NAME> SpecifiestheinterfacenameforwhichtheDHCPv6guardcounter
informationisdisplayed.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfigurationandstatisticsforinterface1/1/1:
| switch# | show         | dhcpv6-snooping |        |          |     | guard-policy | int 1/1/1 |     |
| ------- | ------------ | --------------- | ------ | -------- | --- | ------------ | --------- | --- |
|         | DHCPv6 Guard |                 | Policy | Applied  |     | : pol1       |           |     |
|         | DHCPv6       | Guard           | Policy | Counters |     |              |           |     |
==========================
|         | DHCPv6 Packets |     | Received  |     |     | : 20   |                  |     |
| ------- | -------------- | --- | --------- | --- | --- | ------ | ---------------- | --- |
|         | DHCPv6 Packets |     | Forwarded |     |     | : 5    |                  |     |
|         | DHCPv6 Packets |     | Dropped   |     |     | : 15   | [Total]          |     |
|         |                |     |           |     |     | Access | list error       | [7] |
|         |                |     |           |     |     | Prefix | list error       | [8] |
|         |                |     |           |     |     | Server | preference error | [0] |
| Command | History        |     |           |     |     |        |                  |     |
DHCPsnooping|154

| Release             |         |         |     | Modification       |     |     |
| ------------------- | ------- | ------- | --- | ------------------ | --- | --- |
| 10.10               |         |         |     | Commandintroduced. |     |     |
| Command Information |         |         |     |                    |     |     |
| Platforms           | Command | context |     | Authority          |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show dhcpv6-snooping |     |              | guard-policy |                  | vlan |     |
| -------------------- | --- | ------------ | ------------ | ---------------- | ---- | --- |
| show dhcpv6-snooping |     | guard-policy |              | [vlan <VLAN-ID>] |      |     |
Description
ShowstheDHCPv6snoopingguardpolicyconfigurationandstatisticsforthespecifiedVLAN.
| Parameter |     |     |     | Description                                      |     |     |
| --------- | --- | --- | --- | ------------------------------------------------ | --- | --- |
| <VLAN-ID> |     |     |     | SpecifiestheVLANID forwhichtheDHCPv6guardcounter |     |     |
informationisdisplayed.
Examples
ShowingtheDHCPv6snoopingguardpolicyconfigurationandstatisticsforVLAN100:
| switch# show | dhcpv6-snooping |                 |     | guard-policy | vlan 2 |     |
| ------------ | --------------- | --------------- | --- | ------------ | ------ | --- |
| DHCPv6 Guard |                 | Policy Applied  |     | : pol1       |        |     |
| DHCPv6       | Guard           | Policy Counters |     |              |        |     |
==========================
| DHCPv6 Packets      |         | Received  |     | : 20               |                  |     |
| ------------------- | ------- | --------- | --- | ------------------ | ---------------- | --- |
| DHCPv6 Packets      |         | Forwarded |     | : 5                |                  |     |
| DHCPv6 Packets      |         | Dropped   |     | : 15 [Total]       |                  |     |
|                     |         |           |     | Access             | list error       | [0] |
|                     |         |           |     | Prefix             | list error       | [8] |
|                     |         |           |     | Server             | preference error | [7] |
| Command History     |         |           |     |                    |                  |     |
| Release             |         |           |     | Modification       |                  |     |
| 10.10               |         |           |     | Commandintroduced. |                  |     |
| Command Information |         |           |     |                    |                  |     |
| Platforms           | Command | context   |     | Authority          |                  |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 155

| show dhcpv6-snooping |            |     | statistics |     |     |     |     |
| -------------------- | ---------- | --- | ---------- | --- | --- | --- | --- |
| show dhcpv6-snooping | statistics |     |            |     |     |     |     |
Description
ShowstheDHCPv6snoopingstatistics.
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
| Command Information |         |         |     |     |                                                      |     |     |
| ------------------- | ------- | ------- | --- | --- | ---------------------------------------------------- | --- | --- |
| Platforms           | Command | context |     |     | Authority                                            |     |     |
| 6200                |         |         |     |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
DHCPsnooping|156

Chapter 7

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

157

| clear nd-snooping | binding |     |     |     |
| ----------------- | ------- | --- | --- | --- |
clear nd-snooping bindings {all | ipv6 <IPV6-ADDR> vlan <VLAN-ID> |
| port <PORT-NUM> | | vlan <VLAN-ID>} |     |     |     |
| --------------- | ----------------- | --- | --- | --- |
Description
ClearsNDsnoopingbindingentries.
Command context
| Parameter      |                | Description                                        |     |     |
| -------------- | -------------- | -------------------------------------------------- | --- | --- |
| all            |                | SpecifiesthatallNDbindinginformationistobecleared. |     |     |
| ip <IPV6-ADDR> | vlan <VLAN-ID> |                                                    |     |     |
SpecifiestheIPv6addressandVLANforwhichallNDbinding
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
NDsnooping|158

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
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
| interface <IFNAME> |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- |
ClearallRAGuardpolicyinformationonthespecifiedinterface
Examples
ClearallRAGuardpolicystatisticsforVLAN10:
| switch# clear | nd-snooping | ra-guard-policy |     | statistics | vlan 10 |
| ------------- | ----------- | --------------- | --- | ---------- | ------- |
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 159

Examples
ClearallNDsnoopingstatistics:
switch#
| clear               | nd-snooping | statistics |              |
| ------------------- | ----------- | ---------- | ------------ |
| Command History     |             |            |              |
| Release             |             |            | Modification |
| 10.07orearlier      |             |            | --           |
| Command Information |             |            |              |
| Platforms           | Command     | context    | Authority    |
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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
NDsnooping|160

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
| switch(config-vlan-100)# |      | exit           |     |
switch(config)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
EnablingNDsnoopingMACverification:
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 161

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
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| switch(config)#        |     | vlan | 1   |             |             |            |
| ---------------------- | --- | ---- | --- | ----------- | ----------- | ---------- |
| switch(config-vlan-1)# |     |      | no  | nd-snooping | prefix-list | 2001::1/64 |
NDsnooping|162

| switch(config-vlan-1)# |     |     | exit |     |     |     |
| ---------------------- | --- | --- | ---- | --- | --- | --- |
switch(config)#
| Command        | History     |     |         |              |           |     |
| -------------- | ----------- | --- | ------- | ------------ | --------- | --- |
| Release        |             |     |         | Modification |           |     |
| 10.07orearlier |             |     |         | --           |           |     |
| Command        | Information |     |         |              |           |     |
| Platforms      | Command     |     | context |              | Authority |     |
6200 config-vlan-<VLAN-ID> OperatorsorAdministratorsorlocalusergroupmembers
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
<MAX-BINDINGS>
SpecifiesthemaximumnumberofNDbindings.Youcanusethe
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
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 163

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
NDsnooping|164

| nd-snooping             | ra-guard |     |     |
| ----------------------- | -------- | --- | --- |
| nd-snooping ra-guard    | [log]    |     |     |
| no nd-snooping ra-guard |          |     |     |
Description
ThiscommandenablesRoutingAdvertisement(RA)guardontheselectedVLAN.Whenenabled,ingress
RoutingAdvertisement(RA)andRoutingRedirect(RR)packetsontheselectedVLANareblockedon
untrustedports.Thepacketsareforwardedwhenreceivedontrustedports.
ThenoformofthecommanddisablesRAguardontheVLAN.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     | Description                             |     |
| --------- | --- | --------------------------------------- | --- |
| [log]     |     | Logsmessagesalongwithdropfunctionality. |     |
Examples
EnablingNDsnoopingRAguardonVLAN100:
| switch(config)#          | nd-snooping | enable      |          |
| ------------------------ | ----------- | ----------- | -------- |
| switch(config)#          | vlan 100    |             |          |
| switch(config-vlan-100)# |             | nd-snooping | ra-guard |
switch(config-vlan-100)#
exit
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
Command History
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
Command Information
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 165

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
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
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
6200 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| nd-snooping | trust |     |     |     |
| ----------- | ----- | --- | --- | --- |
| nd-snooping | trust |     |     |     |
NDsnooping|166

| no nd-snooping | trust |     |     |     |
| -------------- | ----- | --- | --- | --- |
Description
EnablesNDsnoopingtrustontheselectedinterface(port).Onlyserverpacketsreceivedontrusted
portsareforwarded.Alltheportsareuntrustedbydefault.
ThenoformofthecommanddisablesNDsnoopingtrustontheselectedport.
Examples
EnablingNDsnoopingtrustoninterface2/2/1:
| switch(config)# |     | interface | 2/2/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
|                    |     | nd-snooping |     | trust |
| ------------------ | --- | ----------- | --- | ----- |
| switch(config-if)# |     | exit        |     |       |
switch(config)#
DisablingNDsnoopingtrustoninterface2/2/1:
| switch(config)#    |     | interface      | 2/2/1 |       |
| ------------------ | --- | -------------- | ----- | ----- |
| switch(config-if)# |     | no nd-snooping |       | trust |
| switch(config-if)# |     | exit           |       |       |
switch(config)#
| Command History     |         |         |     |              |
| ------------------- | ------- | ------- | --- | ------------ |
| Release             |         |         |     | Modification |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
6200 config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show nd-snooping
| show nd-snooping | [vlan | <VLAN-ID>] |     |     |
| ---------------- | ----- | ---------- | --- | --- |
Description
ShowseitherallNDsnoopingconfigurationortheconfigurationforthespecifiedVLAN.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
vlan <VLAN-ID> SpecifiestheVLANforwhichtheNDconfigurationistobeshown.
Range:1to4094.
Examples
(Appliestothe6200,6300,6400and8360.)ShowingallNDsnoopingconfiguration:
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 167

| switch(config)# |     | show        | nd-snooping |     |     |
| --------------- | --- | ----------- | ----------- | --- | --- |
| ND Snooping     |     | Information |             |     |     |
========================
| ND Snooping |         |               |         |                   | : Enabled  |
| ----------- | ------- | ------------- | ------- | ----------------- | ---------- |
| ND Snooping |         | Enabled       | VLANs   |                   | : 10       |
| Trusted     | Port    | Bindings      | Enabled | VLANs             | : 10       |
| ND Guard    | Enabled |               | VLANs   |                   | : 10       |
| RA Guard    | Enabled |               | VLANs   |                   | : 10       |
| RA Drop     | Enabled | VLANs         |         |                   | :          |
| MAC Address |         | Check         |         |                   | : Disabled |
| PORT        | TRUST   | MAX-BINDINGS  |         | CURRENT-BINDINGS  |            |
| -------     | ------  | ------------- |         | ----------------- |            |
| 1/1/1       | Yes     |               |         |                   |            |
| 1/1/2       | Yes     |               |         |                   |            |
| 1/1/3       | No      | 100           |         | 10                |            |
| 1/1/4       | No      | 200           |         | 10                |            |
| 1/1/5       | No      | 300           |         | 10                |            |
(Appliestothe6200,6300,6400,8360.)ShowingNDsnoopingconfigurationforVLAN2:
| switch(config)# |     | show        | nd-snooping | vlan | 2   |
| --------------- | --- | ----------- | ----------- | ---- | --- |
| ND Snooping     |     | Information |             |      |     |
=======================
| ND Snooping         |         |               | : Enabled  |                   |     |
| ------------------- | ------- | ------------- | ---------- | ----------------- | --- |
| MAC Address         |         | Check         | : Disabled |                   |     |
| Trusted             | Port    | Bindings      | : Enabled  |                   |     |
| ND Guard            |         |               | : Enabled  |                   |     |
| RA Guard            |         |               | : Disabled |                   |     |
| RA Drop             |         |               | : Disabled |                   |     |
| PORT                | TRUST   | MAX-BINDINGS  |            | CURRENT-BINDINGS  |     |
| -------             | ------  | ------------- |            | ----------------- |     |
| 1/1/1               | Yes     |               |            |                   |     |
| 1/1/2               | Yes     |               |            |                   |     |
| 1/1/3               | No      | 100           |            | 10                |     |
| Command History     |         |               |            |                   |     |
| Release             |         |               |            | Modification      |     |
| 10.07orearlier      |         |               |            | --                |     |
| Command Information |         |               |            |                   |     |
| Platforms           | Command |               | context    | Authority         |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show nd-snooping |     |          | bindings |     |     |
| ---------------- | --- | -------- | -------- | --- | --- |
| show nd-snooping |     | bindings |          |     |     |
NDsnooping|168

Description
ShowstheNDsnoopingbindingconfiguration.
Examples
ShowingtheNDsnoopingbindingconfiguration:
| switch# show | nd-snooping  | bindings |     |             |            |
| ------------ | ------------ | -------- | --- | ----------- | ---------- |
| PORT         | IPV6-ADDRESS |          |     | MAC-ADDRESS | VLAN TIME- |
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
| switch# show                                      | nd-snooping | prefix-list |     |          |     |
| ------------------------------------------------- | ----------- | ----------- | --- | -------- | --- |
| VLAN IPV6-ADDRESS-PREFIX                          |             |             |     | SOURCE   |     |
| ----- ------------------------------------------- |             |             |     | -------- |     |
| 1 2001::/64                                       |             |             |     | Static   |     |
| 4094 3001::/64                                    |             |             |     | Dynamic  |     |
| Command History                                   |             |             |     |          |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 169

| Release             |         |         |           | Modification |     |     |     |
| ------------------- | ------- | ------- | --------- | ------------ | --- | --- | --- |
| 10.07orearlier      |         |         |           | --           |     |     |     |
| Command Information |         |         |           |              |     |     |     |
| Platforms           | Command | context | Authority |              |     |     |     |
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
| RA                  | forward | RA packets | received     | on trusted     | port       |        | 20  |
| ------------------- | ------- | ---------- | ------------ | -------------- | ---------- | ------ | --- |
| RA                  | drop    | RA packets | received     | on untrusted   | port       |        | 45  |
| NS                  | forward | NS packets | received     | on trusted     | port       |        | 52  |
| NS                  | forward | NS packets | received     | on untrusted   | port       |        | 95  |
| NS                  | drop    | NS packets | failed       | MAC check      |            |        | 14  |
| NS                  | drop    | NS packets | failed       | Prefix check   |            |        | 12  |
| NS                  | drop    | NS packets | failed       | on max-binding | limit      |        | 0   |
| NS                  | drop    | NS packets | failed       | ND snooping    | validation | checks | 20  |
| NA                  | forward | NA packets | received     | on trusted     | port       |        | 17  |
| NA                  | forward | NA packets | received     | on untrusted   | port       |        | 30  |
| NA                  | drop    | NA packets | failed       | Prefix check   |            |        | 15  |
| NA                  | drop    | NA packets | failed       | on max-binding | limit      |        | 2   |
| NA                  | drop    | NA packets | failed       | ND snooping    | validation | checks | 5   |
| Command History     |         |            |              |                |            |        |     |
| Release             |         |            | Modification |                |            |        |     |
| 10.07orearlier      |         |            | --           |                |            |        |     |
| Command Information |         |            |              |                |            |        |     |
| Platforms           | Command | context    | Authority    |                |            |        |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
NDsnooping|170

| RA guard | policy | commands |     |     |     |
| -------- | ------ | -------- | --- | --- | --- |
hop limit
| hop limit | [minimum       | | maximum] <HOP-LIMIT> |             |     |     |
| --------- | -------------- | ---------------------- | ----------- | --- | --- |
| no hop    | limit [minimum | | maximum]             | <HOP-LIMIT> |     |     |
Description
EnablesverificationoftheadvertisedhopcountlimitiftheRAguardpolicyisappliedonaVLANor
interface.RApacketswiththehoplimitwithinthespecifiedminimumandmaximumvaluesare
processed.Ifnoneofthevaluesarespecifiedforhoplimit,thedefaultrangeis1-255.Ifhoplimitisnot
enabled,packetsarenotvalidatedforhoplimit.
ThenoformofthecommanddisablesthehoplimitonthespecifiedRAguardpolicy.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<HOP-LIMIT>
Specifiesthehop-limitvalue.Range:1-255.
minimum Specifiestheminimumvalueforthehop-limitrange.Default:1,
Range1-255.
Therangeisminimum–255ifonlyaminimumvalueisspecified.
maximum Specifiesthemaximumvalueforthehop-limitrange.Default:
255,Range1-255.
Therangeis1–maximumifonlyamaximumvalueisspecified.
Examples
EnablingthehoplimitontheRAguardpolicyandaddingminimumandmaximumvaluesforhoplimit
onthepolicy:
| switch(config)#                |     | ipv6 nd-snooping | ra-guard  | policy  | <POLICY-NAME> |
| ------------------------------ | --- | ---------------- | --------- | ------- | ------------- |
| switch(config-raguard-policy)# |     |                  | hop-limit | enable  |               |
| switch(config-raguard-policy)# |     |                  | hop-limit | maximum | 150           |
| switch(config-raguard-policy)# |     |                  | hop-limit | minimum | 50            |
DisablingthehoplimitontheRAguardpolicy:
switch(config)#
|                                |     | ipv6 nd-snooping | ra-guard     | policy | <POLICY-NAME> |
| ------------------------------ | --- | ---------------- | ------------ | ------ | ------------- |
| switch(config-raguard-policy)# |     |                  | no hop-limit | enable |               |
RemovingminimumandmaximumvaluesforthehoplimitontheRAguardpolicy:
| switch(config)#                |     | ipv6 nd-snooping | ra-guard     | policy  | <POLICY-NAME> |
| ------------------------------ | --- | ---------------- | ------------ | ------- | ------------- |
| switch(config-raguard-policy)# |     |                  | no hop-limit | maximum | 150           |
| switch(config-raguard-policy)# |     |                  | no hop-limit | minimum | 50            |
| switch(config-raguard-policy)# |     |                  | no hop-limit | maximum |               |
| switch(config-raguard-policy)# |     |                  | no hop-limit | minimum |               |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 171

| Command History     |         |     |         |                    |           |     |
| ------------------- | ------- | --- | ------- | ------------------ | --------- | --- |
| Release             |         |     |         | Modification       |           |     |
| 10.10               |         |     |         | Commandintroduced. |           |     |
| Command Information |         |     |         |                    |           |     |
| Platforms           | Command |     | context |                    | Authority |     |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ipv6 nd-snooping    |     |          | ra-guard | policy        |     |     |
| ------------------- | --- | -------- | -------- | ------------- | --- | --- |
| ipv6 nd-snooping    |     | ra-guard | policy   | <POLICY-NAME> |     |     |
| no ipv6 nd-snooping |     | ra-guard | policy   | <POLICY-NAME> |     |     |
Description
CreatestheRouterAdvertisement(RA)guardpolicywiththegivennameandenterstheRAguardpolicy
configurationcontext.
ThenoformofthecommandremovesthespecifiedRAguardpolicyfromtheswitch.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<POLICY-NAME> SpecifiesthenameoftheRAguardpolicy.Maximumlength:64.
Examples
CreatingtheRAguardpolicygloballywithaspecifiedname:
| switch(config)# |     | ipv6 | nd-snooping | ra-guard | policy | <POLICY-NAME> |
| --------------- | --- | ---- | ----------- | -------- | ------ | ------------- |
switch(config-raguard-policy)#
DeletingthespecifiedRAguardpolicy:
switch(config)# no ipv6 nd-snooping ra-guard policy <POLICY-NAME>
| Command History     |     |     |     |                    |     |     |
| ------------------- | --- | --- | --- | ------------------ | --- | --- |
| Release             |     |     |     | Modification       |     |     |
| 10.10               |     |     |     | Commandintroduced. |     |     |
| Command Information |     |     |     |                    |     |     |
NDsnooping|172

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6200 config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
on
Verifiesthattheadvertisedmanagedaddressconfigurationflagis
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
| switch(config)#                | ipv6 | nd-snooping | ra-guard policy        | <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | ---------------------- | ------------- |
| switch(config-raguard-policy)# |      |             | no managed-config-flag |               |
| switch(config-raguard-policy)# |      |             | no managed-config-flag | off           |
| switch(config-raguard-policy)# |      |             | no managed-config-flag | on            |
| Command History                |      |             |                        |               |
| Release                        |      |             | Modification           |               |
| 10.10                          |      |             | Commandintroduced.     |               |
| Command Information            |      |             |                        |               |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 173

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
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
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
NDsnooping|174

| match             | prefix-list |                    |     |     |     |     |
| ----------------- | ----------- | ------------------ | --- | --- | --- | --- |
| match prefix-list |             | <PREFIX-LIST-NAME> |     |     |     |     |
| no match          | prefix-list | <PREFIX-LIST-NAME> |     |     |     |     |
Description
Configuresaprefix-listfortheRAguardpolicy.AdvertisedprefixesinRApacketsarecomparedagainst
theconfiguredprefix-listandifthereisnomatch,theRApacketsaredropped.IftheRAprefixlistisnot
configured,thischeckisnotperformed.
ThenoformofthecommandremovestheprefixlistfromtheRAguardpolicy.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
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
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| nd-snooping    |          | ra-guard      | attach-policy |               |               |     |
| -------------- | -------- | ------------- | ------------- | ------------- | ------------- | --- |
| nd-snooping    | ra-guard | attach-policy |               | <POLICY-NAME> |               |     |
| no nd-snooping | ra-guard | attach-policy |               |               | <POLICY-NAME> |     |
Description
AppliesthecreatedRAguardpolicytoaspecificL2portorVLAN.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 175

The no form of the command detaches the specified RA guard policy from the L2 port or VLAN.

Parameter

<POLICY-NAME>

Usage

Description

Specifies the name of the RA guard policy.

In the interface configuration (config-if) context:

n RA guard must be enabled on member VLANs of the port for which RA packets need to be inspected

using the policy.

In the interface configuration (config-if) and VLAN configuration (config-vlan) contexts:

n RA packets received on untrusted ports are dropped without any inspection.

n RA packets received on trusted ports are validated against the policy.

n The applied policy takes effect only if ND snooping is enabled globally and both ND snooping and RA

guard are enabled under the VLAN context.

Policy precedence between VLAN and port:

n If the policy is attached to both VLAN and port, the port policy takes precedence over the VLAN

policy.

n Only one policy can be attached per VLAN or port.

n If the port belongs to a different VLAN (for example, in the case of a trunk port) the tagged VLAN

takes priority. If the packets are untagged, the native VLAN policy takes precedence.

Examples

Attaching the RA guard policy to an L2 port:

switch(config)# interface 1/1/10
switch(config-if)# nd-snooping ra-guard attach-policy POLICY_NAME

Attempting to attach the RA guard policy to a port where routing is enabled, the policy is not configured,
or it is an untrusted port:

(When prompted, enter "Y" to create the policy and attach it to the interface. )

switch(config)# interface 1/1/10
switch(config-if)# nd-snooping ra-guard attach-policy POLICY_NAME
RA Guard policy can't be attached to an interface with routing enabled.

switch(config-if)# no routing
switch(config-if)# nd-snooping trust
switch(config-if)# nd-snooping ra-guard attach-policy POLICY_NAME
switch(config-if)#6300(config-if)# nd-snooping ra-guard attach-policy POLICY_NOT_
CREATED
RA guard policy does not exist.
Do you want to create (y/n)?

switch(config)# interface 1/1/10

ND snooping | 176

| switch(config-if)# |     | nd-snooping |     | ra-guard | attach-policy | AA  |
| ------------------ | --- | ----------- | --- | -------- | ------------- | --- |
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
| Could not | find        | the | policy  | POLICY_NOT_CREATED. |           |     |
| --------- | ----------- | --- | ------- | ------------------- | --------- | --- |
| Command   | History     |     |         |                     |           |     |
| Release   |             |     |         | Modification        |           |     |
| 10.10     |             |     |         | Commandintroduced.  |           |     |
| Command   | Information |     |         |                     |           |     |
| Platforms | Command     |     | context |                     | Authority |     |
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
Thenoformofthecommanddisablesotherconfigurationflagverification.
NDsnoopingmustbeenabledinboththeglobalcontextandtheconfig-vlancontextbeforethiscommandcan
beused.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 177

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
on VerifiesthattheadvertisedOtherStatefulConfigurationflagisOn.
off
VerifiesthattheadvertisedOtherStatefulConfigurationflagis
Off.
Examples
Enablingotherconfigurationflagverification:
switch(config)#
|                                |     | ipv6 nd-snooping | ra-guard          | policy | <POLICY-NAME> |
| ------------------------------ | --- | ---------------- | ----------------- | ------ | ------------- |
| switch(config-raguard-policy)# |     |                  | other-config-flag |        | off           |
| switch(config-raguard-policy)# |     |                  | other-config-flag |        | on            |
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
| Parameter |     |     | Description                           |     |     |
| --------- | --- | --- | ------------------------------------- | --- | --- |
| high      |     |     | Setsthemaximumrouterpreferencetohigh. |     |     |
NDsnooping|178

| Parameter |     |     | Description                             |     |     |
| --------- | --- | --- | --------------------------------------- | --- | --- |
| medium    |     |     | Setsthemaximumrouterpreferencetomedium. |     |     |
| low       |     |     | Setsthemaximumrouterpreferencetolow.    |     |     |
Examples
Enablingrouterpreferenceverificationwiththemaximumrouterpreferencesettohigh:
| switch(config)#                | ipv6 | nd-snooping | ra-guard          |     | policy <POLICY-NAME> |
| ------------------------------ | ---- | ----------- | ----------------- | --- | -------------------- |
| switch(config-raguard-policy)# |      |             | router-preference |     | high                 |
Disablingrouterpreferenceverification:
| switch(config)#                | ipv6    | nd-snooping | ra-guard           |                   | policy <POLICY-NAME> |
| ------------------------------ | ------- | ----------- | ------------------ | ----------------- | -------------------- |
| switch(config-raguard-policy)# |         |             | no                 | router-preference |                      |
| Command History                |         |             |                    |                   |                      |
| Release                        |         |             | Modification       |                   |                      |
| 10.10orearlier                 |         |             | Commandintroduced. |                   |                      |
| Command Information            |         |             |                    |                   |                      |
| Platforms                      | Command | context     |                    | Authority         |                      |
6200 config-raguard-policy Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show nd-snooping |          | ra-guard  | interface      |     |     |
| ---------------- | -------- | --------- | -------------- | --- | --- |
| show nd-snooping | ra-guard | interface | <INTERFACE-ID> |     |     |
Description
ShowsRAguardcountersforthespecifiedinterface.CountersareclearedoncetheRAguardpolicyis
detachedfromtheinterface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<INTERFACE-ID> SpecifiestheinterfaceforwhichtheRAguardcountersare
displayed.
Examples
ShowingRAguardcountersforinterface1/1/1:
| switch# show | nd-snooping | ra-guard |     | interface | 1/1/1 |
| ------------ | ----------- | -------- | --- | --------- | ----- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 179

|     | RA Guard | Policy | Counters |     |     |     |     |     |     |
| --- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- |
========================
|           | RA Guard    | Policy    | Applied |         | : POLICY_2         |            |          |     |     |
| --------- | ----------- | --------- | ------- | ------- | ------------------ | ---------- | -------- | --- | --- |
|           | RA Packets  | Received  |         |         | : 10               |            |          |     |     |
|           | RA Packets  | Forwarded |         |         | : 5                |            |          |     |     |
|           | RA Packets  | Dropped   |         |         | : 5 [Total]        |            |          |     |     |
|           |             |           |         | reason  | : Managed          | flag       | error    | [0] |     |
|           |             |           |         |         | Other              | flag       | error    | [0] |     |
|           |             |           |         |         | Access             | list       | error    | [0] |     |
|           |             |           |         |         | Prefix             | list       | error    | [0] |     |
|           |             |           |         |         | Router             | preference | error[0] |     |     |
|           |             |           |         |         | Hop                | limit      | error    | [5] |     |
| Command   | History     |           |         |         |                    |            |          |     |     |
| Release   |             |           |         |         | Modification       |            |          |     |     |
| 10.10     |             |           |         |         | Commandintroduced. |            |          |     |     |
| Command   | Information |           |         |         |                    |            |          |     |     |
| Platforms |             | Command   |         | context | Authority          |            |          |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | nd-snooping |          | ra-guard |        | policy          |     |     |     |     |
| ---- | ----------- | -------- | -------- | ------ | --------------- | --- | --- | --- | --- |
| show | nd-snooping | ra-guard |          | policy | [<POLICY-NAME>] |     |     |     |     |
Description
ShowstheRAguardpolicyconfiguration.
| Parameter |     |     |     |     | Description |     |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
<POLICY-NAME>
SpecifiesthenameoftheRAguardpolicytobedisplayed.
Examples
ShowingRAguardconfiguration:
switch#
|     | show     | nd-snooping |     | ra-guard | policy  |       |     |     |               |
| --- | -------- | ----------- | --- | -------- | ------- | ----- | --- | --- | ------------- |
|     | RA Guard | Policy      |     |          | Applied | Ports |     |     | Applied VLANs |
----------------------------------------------------------------------------------
--------
|     | POLICY_NAME1 |             | 1/1/25,1/1/27,1/1/29-1/1/44,1/1/46 |          |        |              |     |     | 10,20,50-100 |
| --- | ------------ | ----------- | ---------------------------------- | -------- | ------ | ------------ | --- | --- | ------------ |
|     | POLICY_NAME2 |             | 1/1/1-1/1/24                       |          |        |              |     |     |              |
|     | switch# show | nd-snooping |                                    | ra-guard | policy | POLICY_NAME1 |     |     |              |
NDsnooping|180

|     | RA Guard | policy | Information |     |     |     |
| --- | -------- | ------ | ----------- | --- | --- | --- |
========================
|           | Policy name       |         |     | : POLICY_NAME1                       |                    |     |
| --------- | ----------------- | ------- | --- | ------------------------------------ | ------------------ | --- |
|           | Policy Applied    | Ports   |     | : 1/1/25,1/1/27,1/1/29-1/1/44,1/1/46 |                    |     |
|           | Policy Applied    | VLANs   |     | : 10,20,50-100                       |                    |     |
|           | Hop Limit         |         |     | : enabled                            |                    |     |
|           | minimum           |         |     | : 50                                 |                    |     |
|           | maximum           |         |     | : 150                                |                    |     |
|           | Managed config    | flag    |     | : On                                 |                    |     |
|           | Other config      | flag    |     | : On                                 |                    |     |
|           | Access List       |         |     | : ACL1                               |                    |     |
|           | Prefix List       |         |     | : PREFIX_LIST_NAME                   |                    |     |
|           | Router Preference |         |     | : high                               |                    |     |
| Command   | History           |         |     |                                      |                    |     |
| Release   |                   |         |     |                                      | Modification       |     |
| 10.10     |                   |         |     |                                      | Commandintroduced. |     |
| Command   | Information       |         |     |                                      |                    |     |
| Platforms |                   | Command |     | context                              | Authority          |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
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
|     | switch# show | nd-snooping |          | ra-guard | vlan | 2   |
| --- | ------------ | ----------- | -------- | -------- | ---- | --- |
|     | RA Guard     | Policy      | Counters |          |      |     |
========================
|     | RA Guard   | Policy    | Applied |     | : POLICY_1 |     |
| --- | ---------- | --------- | ------- | --- | ---------- | --- |
|     | RA Packets | Received  |         |     | : 20       |     |
|     | RA Packets | Forwarded |         |     | : 5        |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 181

| RA Packets          | Dropped |         | : 15 [Total]       |                     |     |
| ------------------- | ------- | ------- | ------------------ | ------------------- | --- |
|                     |         | reason  | : Managed          | flag error          | [1] |
|                     |         |         | Other              | flag error          | [4] |
|                     |         |         | Access             | list error          | [1] |
|                     |         |         | Prefix             | list error          | [4] |
|                     |         |         | Router             | preference error[0] |     |
|                     |         |         | Hop limit          | error               | [5] |
| Command History     |         |         |                    |                     |     |
| Release             |         |         | Modification       |                     |     |
| 10.10               |         |         | Commandintroduced. |                     |     |
| Command Information |         |         |                    |                     |     |
| Platforms           | Command | context | Authority          |                     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
NDsnooping|182

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
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
183
AOS-CX10.10IPServicesGuide|(6200SwitchSeries)

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
IPv6destinationguard|184

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
| switch# show           | ipv6 destination-guard |               |                    |     |
| ---------------------- | ---------------------- | ------------- | ------------------ | --- |
| IPv6 Destination-Guard |                        | information   |                    |     |
| Enabled VLANs          |                        | : 10,20,31-35 |                    |     |
| Command History        |                        |               |                    |     |
| Release                |                        |               | Modification       |     |
| 10.10                  |                        |               | Commandintroduced. |     |
| Command Information    |                        |               |                    |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 185

Platforms

Command context

Authority

6200

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

IPv6 destination guard | 186

Internet Control Message Protocol (ICMP)

Chapter 9

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

187

ICMPmessagesaresentwhenoneormoreofthefollowingscenariosoccur:
n Adatagramcannotreachitsdestination.
n Thegatewaydoesnothavethebufferingcapacitytoforwardadatagram.
n Thegatewaycandirectthehosttosendtrafficonashorterroute.
| ICMP | redirect messages |     |     |
| ---- | ----------------- | --- | --- |
ICMPredirectmessagesareusedbyrouterstonotifythehostsonthedatalinkthatabetterrouteis
availableforaparticulardestination.
| When | ICMP redirect | messages | are sent |
| ---- | ------------- | -------- | -------- |
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
| ICMP    | commands      |     |     |
| ------- | ------------- | --- | --- |
| ip icmp | redirect      |     |     |
| ip icmp | redirect      |     |     |
| no ip   | icmp redirect |     |     |
Description
EnablesthesendingofICMPv4andICMPv6redirectmessagestothesourcehost.Enabledbydefault.
ICMPredirectandactiveforwardingaremutuallyexclusive.
ThenoformofthiscommanddisablesICMPv4andICMPv6redirectmessagestothesourcehost.
Examples
EnablingICMPredirectmessages:
| switch(config)# | ip icmp | redirect |     |
| --------------- | ------- | -------- | --- |
DisablingICMPredirectmessages:
switch(config)#
no ip icmp redirect
| Command | History |     |     |
| ------- | ------- | --- | --- |
InternetControlMessageProtocol(ICMP)|188

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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 189

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
InternetControlMessageProtocol(ICMP)|190

Chapter 10

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

191

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
DNS|192

| Release        |             |         |         |     | Modification |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
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
| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
<DOMAIN-NAME> SpecifiesthedomainnametoappendtoDNSrequests.Length:1
to256characters.
| vrf <VRF-NAME> |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Settingthedefaultdomainnametodomain.com:
| switch(config)# |     |     | ip dns | domain-name |     | domain.com |     |
| --------------- | --- | --- | ------ | ----------- | --- | ---------- | --- |
Removingthedefaultdomainnamedomain.com:
| switch(config)# |             |         | no ip dns | domain-name |              | domain.com |     |
| --------------- | ----------- | ------- | --------- | ----------- | ------------ | ---------- | --- |
| Command         | History     |         |           |             |              |            |     |
| Release         |             |         |           |             | Modification |            |     |
| 10.07orearlier  |             |         |           |             | --           |            |     |
| Command         | Information |         |           |             |              |            |     |
| Platforms       |             | Command | context   |             | Authority    |            |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 193

| ip dns    | host |             |     |           |     |                  |     |     |
| --------- | ---- | ----------- | --- | --------- | --- | ---------------- | --- | --- |
| ip dns    | host | <HOST-NAME> |     | <IP-ADDR> |     | [ vrf <VRF-NAME> |     | ]   |
| no ip dns | host | <HOST-NAME> |     | <IP-ADDR> |     | [ vrf <VRF-NAME> |     | ]   |
Description
AssociatesastaticIPaddresswithahostname.TheDNSclientreturnsthisIPaddressinsteadof
queryingaDNSserverforanIPaddressforthehostname.Uptosixhostscanbedefined.IfnoVRFis
defined,thedefaultVRFisused.
ThenoformofthiscommandremovesastaticIPaddressassociatedwithahostname.
| Parameter |     |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- |
host <HOST-NAME> Specifiesthenameofahost.Length:1to256characters.
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
| ThisexampledefinesanIPv4addressof     |     |     |        |      |       | 3.3.3.3forhost1.  |     |       |
| ------------------------------------- | --- | --- | ------ | ---- | ----- | ----------------- | --- | ----- |
| switch(config)#                       |     |     | ip dns | host | host1 | 3.3.3.3           |     |       |
| ThisexampledefinesanIPv6addressofb::5 |     |     |        |      |       | forhost           | 1.  |       |
| switch(config)#                       |     |     | ip dns | host | host1 | b::5              |     |       |
| Thisexampledefinesremovestheentryfor  |     |     |        |      |       | host 1withaddress |     | b::5. |
switch(config)#
|                |             |         | no ip | dns     | host | host1 b::5   |     |     |
| -------------- | ----------- | ------- | ----- | ------- | ---- | ------------ | --- | --- |
| Command        | History     |         |       |         |      |              |     |     |
| Release        |             |         |       |         |      | Modification |     |     |
| 10.07orearlier |             |         |       |         |      | --           |     |     |
| Command        | Information |         |       |         |      |              |     |     |
| Platforms      |             | Command |       | context |      | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| ip dns | server         | address |           |     |       |            |     |     |
| ------ | -------------- | ------- | --------- | --- | ----- | ---------- | --- | --- |
| ip dns | server-address |         | <IP-ADDR> |     | [ vrf | <VRF-NAME> | ]   |     |
DNS|194

| no ip dns | server-address |     | <IP-ADDR> | [ vrf | <VRF-NAME> | ]   |
| --------- | -------------- | --- | --------- | ----- | ---------- | --- |
Description
ConfigurestheDNSnameserversthattheDNSclientqueriestoresolveDNSqueries.Uptosixname
serverscanbedefined.TheDNSclientqueriestheserversintheorderthattheyaredefined.IfnoVRFis
defined,thedefaultVRFisused.
Thenoformofthiscommandremovesanameserverfromthelist.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<IP-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255,orIPv6format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.
| vrf <VRF-NAME> |     |     |     | SpecifiesaVRFname.Default:default. |     |     |
| -------------- | --- | --- | --- | ---------------------------------- | --- | --- |
Examples
Thisexampledefinesanameserverat1.1.1.1.
| switch(config)# |     | ip  | dns server-address |     | 1.1.1.1 |     |
| --------------- | --- | --- | ------------------ | --- | ------- | --- |
Thisexampledefinesanameserverata::1.
| switch(config)# |     | ip  | dns server-address |     | a::1 |     |
| --------------- | --- | --- | ------------------ | --- | ---- | --- |
Thisexampleremovesanameserverata::1.
| switch(config)# |             | no  | ip dns server-address |              | a::1 |     |
| --------------- | ----------- | --- | --------------------- | ------------ | ---- | --- |
| Command         | History     |     |                       |              |      |     |
| Release         |             |     |                       | Modification |      |     |
| 10.07orearlier  |             |     |                       | --           |      |     |
| Command         | Information |     |                       |              |      |     |
| Platforms       | Command     |     | context               | Authority    |      |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show    | ip dns   |             |     |     |     |     |
| ------- | -------- | ----------- | --- | --- | --- | --- |
| show ip | dns [vrf | <VRF-NAME>] |     |     |     |     |
Description
ShowsallDNSclientconfigurationsettingsorthesettingsforaspecificVRF.
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 195

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vrf <VRF-NAME> SpecifiestheVRFforwhichtoshowinformation.IfnoVRFis
defined,thedefaultVRFisused.
Examples
| switch(config)# |           | ip             | dns domain-name    |         | domain.com  |
| --------------- | --------- | -------------- | ------------------ | ------- | ----------- |
| switch(config)# |           | ip             | dns domain-list    |         | domain5.com |
| switch(config)# |           | ip             | dns domain-list    |         | domain8.com |
| switch(config)# |           | ip             | dns server-address |         | 4.4.4.4     |
| switch(config)# |           | ip             | dns server-address |         | 6.6.6.6     |
| switch(config)# |           | ip             | dns host           | host3   | 5.5.5.5     |
| switch(config)# |           | ip             | dns host           | host3   | c::12       |
| switch#         | show      | ip dns         |                    |         |             |
| VRF Name        | : default |                |                    |         |             |
| Domain Name     | :         | domain.com     |                    |         |             |
| DNS Domain      | list      | : domain5.com, |                    |         | domain8.com |
| Name Server(s)  |           | : 4.4.4.4,     |                    | 6.6.6.6 |             |
| Host Name       |           | Address        |                    |         |             |
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
DNS|196

Chapter 11

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

197

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
| Configuring | proxy | ARP |
| ----------- | ----- | --- |
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. SwitchtoaninterfaceVLANwiththecommandinterface vlan.
3. EnablelocalproxyARPwiththecommandip proxy-arp.
Examples
ThisexampleconfiguresproxyARPoninterfaceVLAN30.
| switch# config          |           |              |
| ----------------------- | --------- | ------------ |
| switch(config)#         | interface | vlan 30      |
| switch(config-vlan-30)# |           | ip proxy-arp |
| Configuring             | local     | proxy ARP    |
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. SwitchtoaninterfaceVLANwiththecommandinterface vlan.
3. EnablelocalproxyARPwiththecommandip local-proxy-arp.
Examples
ThisexampleconfigureslocalproxyARPoninterfaceVLAN30.
| switch# config          |           |                    |
| ----------------------- | --------- | ------------------ |
| switch(config)#         | interface | vlan 30            |
| switch(config-vlan-30)# |           | ip local-proxy-arp |
ARP|198

ARP commands
arp inspection
arp inspection
Description
EnablesDynamicARPInspectiononthecurrentVLAN,forcingallARPpacketsfromuntrustedportsto
besubjectedtoaMAC-IPassociationcheckagainstabindingtable.
ThenoformofthiscommanddisablesDynamicARPInspectionontheVLAN.
Examples
EnablingdynamicARPinspection:
| switch# configure    | terminal |                |     |
| -------------------- | -------- | -------------- | --- |
| switch(config)#      | vlan     | 1              |     |
| switch(config-vlan)# |          | arp inspection |     |
DisablingdynamicARPinspection:
| switch# configure    | terminal |                   |              |
| -------------------- | -------- | ----------------- | ------------ |
| switch(config)#      | vlan     | 1                 |              |
| switch(config-vlan)# |          | no arp inspection |              |
| Command History      |          |                   |              |
| Release              |          |                   | Modification |
| 10.07orearlier       |          |                   | --           |
| Command Information  |          |                   |              |
| Platforms            | Command  | context           | Authority    |
config-vlan-<VLAN-ID>
| 6200 |     |     | Administratorsorlocalusergroupmemberswithexecution |
| ---- | --- | --- | -------------------------------------------------- |
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 199

| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
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
switch(config)#
|                    | interface | 1/1/1                |     |
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
ARP|200

| switch(config)# |     | interface | vlan | 2-100 |     |
| --------------- | --- | --------- | ---- | ----- | --- |
switch(config-if-vlan<2-100>)#
no shutdown
| switch(config-if-vlan<2-100>)# |             |     |         | no arp       | process-grat-arp |
| ------------------------------ | ----------- | --- | ------- | ------------ | ---------------- |
| Command                        | History     |     |         |              |                  |
| Release                        |             |     |         | Modification |                  |
| 10.07orearlier                 |             |     |         | --           |                  |
| Command                        | Information |     |         |              |                  |
| Platforms                      | Command     |     | context | Authority    |                  |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     |     | rightsforthiscommand. |     |
| --- | -------------- | --- | --- | --------------------- | --- |
config-subif
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
| Command | History |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 201

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     | rightsforthiscommand. |
| --- | -------------- | --- | --------------------- |
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
| all-vrfs   |     |     | SelectsallVRFs.                         |
| ---------- | --- | --- | --------------------------------------- |
| <VRF-NAME> |     |     | SpecifiesthenameofaVRF.Default:default. |
Examples
ClearingallIPv4andIPv6neighborARPentriesforthedefaultVRF:
| switch# | clear arp |     |     |
| ------- | --------- | --- | --- |
ClearingallARPneighborentriesforaport:
| switch#        | clear arp 1/1/35 |         |              |
| -------------- | ---------------- | ------- | ------------ |
| Command        | History          |         |              |
| Release        |                  |         | Modification |
| 10.07orearlier |                  |         | --           |
| Command        | Information      |         |              |
| Platforms      | Command          | context | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
ARP|202

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
| switch#            | interface 1/1/1 |                    |     |
| ------------------ | --------------- | ------------------ | --- |
| switch(config-if)# |                 | ip local proxy-arp |     |
EnablinglocalproxyARPoninterfaceVLAN3:
| switch#                 | interface vlan | 3                  |     |
| ----------------------- | -------------- | ------------------ | --- |
| switch(config-if-vlan)# |                | ip local-proxy-arp |     |
DisablinglocalproxyARPononinterface1/1/1.
switch#
|                    | interface 1/1/1 |                       |              |
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 203

| Parameter    |     |     | Description                      |     |
| ------------ | --- | --- | -------------------------------- | --- |
| <IPV6-ADDR>> |     |     | SpecifiesanIPaddressinIPv6format |     |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Range:4096to131072.Default:
131072.
| mac <MAC-ADDR>> |     |     | SpecifiestheMACaddressoftheneighbor |     |
| --------------- | --- | --- | ----------------------------------- | --- |
(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0
toF.Range:4096to131072.Default:131072.
Example
| CreatesastaticARPentryoninterface |           |       | 1/1/1. |     |
| --------------------------------- | --------- | ----- | ------ | --- |
| switch(config)#                   | interface | 1/1/1 |        |     |
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
| switch# interface      | 1/1/1 |              |     |     |
| ---------------------- | ----- | ------------ | --- | --- |
| switch(config-if)#     |       | ip proxy-arp |     |     |
| EnablingproxyARPonVLAN |       | 3:           |     |     |
ARP|204

| switch# interface |     | vlan 3 |     |     |     |     |
| ----------------- | --- | ------ | --- | --- | --- | --- |
switch(config-if-vlan)#
ip proxy-arp
EnablingproxyARPonaLAG11:
| switch(config)#        | int | lag 11       |     |     |     |     |
| ---------------------- | --- | ------------ | --- | --- | --- | --- |
| switch(config-lag-if)# |     | ip proxy-arp |     |     |     |     |
DisablingproxyARPoninterface1/1/1:
| switch# interface   |         | 1/1/1           |              |     |     |     |
| ------------------- | ------- | --------------- | ------------ | --- | --- | --- |
| switch(config-if)#  |         | no ip proxy-arp |              |     |     |     |
| Command History     |         |                 |              |     |     |     |
| Release             |         |                 | Modification |     |     |     |
| 10.07orearlier      |         |                 | --           |     |     |     |
| Command Information |         |                 |              |     |     |     |
| Platforms           | Command | context         | Authority    |     |     |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-if-vlan |     | rightsforthiscommand. |     |     |     |
| --- | -------------- | --- | --------------------- | --- | --- | --- |
config-lag-vlan
show arp
show arp
Description
ShowstheentriesintheARP(AddressResolutionProtocol)table.
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
| 192.168.1.2 |     | 00:50:56:96:7b:e0 | vlan10 | 1/1/29 | stale     |     |
| ----------- | --- | ----------------- | ------ | ------ | --------- | --- |
| 192.168.1.3 |     | 00:50:56:96:7b:ac | vlan10 | 1/1/1  | reachable |     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 205

| Total Number | Of ARP | Entries | Listed- | 2.  |
| ------------ | ------ | ------- | ------- | --- |
-------------------------------------------------------------------------------
| Command        | History     |         |     |              |
| -------------- | ----------- | ------- | --- | ------------ |
| Release        |             |         |     | Modification |
| 10.07orearlier |             |         |     | --           |
| Command        | Information |         |     |              |
| Platforms      | Command     | context |     | Authority    |
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
| Command | History |     |     |     |
| ------- | ------- | --- | --- | --- |
ARP|206

| Release        |             |         | Modification |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
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
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 207

show arp state {all | failed | incomplete | permanent | reachable | stale}
Description
ShowsARP(AddressResolutionProtocol)cacheentriesthatareinthespecifiedstate.
| Parameter |     |     | Description                                    |     |     |
| --------- | --- | --- | ---------------------------------------------- | --- | --- |
| all       |     |     | ShowstheARPcacheentriesforallVRF(VirtualRouter |     |     |
Forwarding)instances.
failed
ShowstheARPcacheentriesthatareinfailedstate.The
neighbormighthavebeendeleted.
| incomplete |     |     | ShowstheARPcacheentriesthatareinincompletestate. |     |     |
| ---------- | --- | --- | ------------------------------------------------ | --- | --- |
Anincompletestatemeansthataddressresolutionisinprogress
andthelink-layeraddressoftheneighborhasnotyetbeen
determined.Asolicitationrequestwassent,andtheswitchis
waitingforasolicitationreplyoratimeout.
permanent
ShowstheARPcacheentriesthatareinpermanentstate.ARP
entriesthatareinapermanentstatecanberemovedby
administrativeactiononly.
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
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
ARP|208

| show arp         | summary   |     |       |             |     |
| ---------------- | --------- | --- | ----- | ----------- | --- |
| show arp summary | [all-vrfs |     | | vrf | <VRF-NAME>] |     |
Description
ShowsasummaryoftheIPv4andIPv6neighborentriesontheswitchforallVRFsoraspecificVRF.
| Parameter |     |     |     | Description     |     |
| --------- | --- | --- | --- | --------------- | --- |
| all-vrfs  |     |     |     | SelectsallVRFs. |     |
vrf <VRF-NAME>
SpecifiesthenameofaVRF.
Examples
ShowingsummaryARPinformationforallVRFs:
| switch#     | show arp | summary | all-vrfs |        |      |
| ----------- | -------- | ------- | -------- | ------ | ---- |
| ARP Entry's | State    |         |          | : IPv4 | IPv6 |
-------------------------------------------------------
| Number | of Reachable  | ARP         | entries | : 2 | 0   |
| ------ | ------------- | ----------- | ------- | --- | --- |
| Number | of Stale ARP  | entries     |         | : 0 | 0   |
| Number | of Failed     | ARP entries |         | : 2 | 2   |
| Number | of Incomplete | ARP         | entries | : 0 | 0   |
| Number | of Permanent  | ARP         | entries | : 0 | 0   |
-------------------------------------------------------
| Total ARP | Entries: | 6   |     | : 4 | 2   |
| --------- | -------- | --- | --- | --- | --- |
-------------------------------------------------------
ShowingasummaryofallIPv4andIPv6neighborentriesontheprimaryandsecondary(peer)switches:
| vsx-primary# | show  | arp | summary |      |      |
| ------------ | ----- | --- | ------- | ---- | ---- |
| ARP Entry's  | State |     |         | IPv4 | IPv6 |
---------------------------------------------------------
| Number | of Reachable  | ARP         | entries | 25858 | 32231 |
| ------ | ------------- | ----------- | ------- | ----- | ----- |
| Number | of Stale ARP  | entries     |         | 0     | 1     |
| Number | of Failed     | ARP entries |         | 0     | 257   |
| Number | of Incomplete | ARP         | entries | 0     | 0     |
| Number | of Permanent  | ARP         | entries | 0     | 0     |
---------------------------------------------------------
| Total ARP    | Entries- | 58347 |         | 25858    | 32489 |
| ------------ | -------- | ----- | ------- | -------- | ----- |
| vsx-primary# | show     | arp   | summary | vsx-peer |       |
| ARP Entry's  | State    |       |         | IPv4     | IPv6  |
---------------------------------------------------------
| Number | of Reachable  | ARP         | entries | 25858 | 32168 |
| ------ | ------------- | ----------- | ------- | ----- | ----- |
| Number | of Stale ARP  | entries     |         | 0     | 3     |
| Number | of Failed     | ARP entries |         | 0     | 317   |
| Number | of Incomplete | ARP         | entries | 0     | 0     |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 209

| Number | of Permanent |     | ARP entries | 0   | 0   |
| ------ | ------------ | --- | ----------- | --- | --- |
---------------------------------------------------------
| Total ARP | Entries- |     | 58346 | 25858 | 32488 |
| --------- | -------- | --- | ----- | ----- | ----- |
---------------------------------------------------------
| Command        | History     |     |         |              |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| Release        |             |     |         | Modification |     |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show arp         | timeout |               |     |     |     |
| ---------------- | ------- | ------------- | --- | --- | --- |
| show arp timeout |         | [<INTERFACE>] |     |     |     |
Description
Showstheage-outperiodforeachARP(AddressResolutionProtocol)entryforaport,LAG,orVLAN
interface.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<INTERFACE> Specifiesaphysicalport,VLAN,orLAGontheswitch.Forphysical
ports,usetheformatmember/slot/port(forexample,1/3/1).
Examples
ShowingARPtimeoutinformationforaport:
| switch# | show arp | timeout | 1/1/1 |     |     |
| ------- | -------- | ------- | ----- | --- | --- |
ARP Timeout:
------------------
| Port           |             | VRF     |     |              | Timeout |
| -------------- | ----------- | ------- | --- | ------------ | ------- |
| 1/1/1          |             | default |     |              | 600     |
| Command        | History     |         |     |              |         |
| Release        |             |         |     | Modification |         |
| 10.07orearlier |             |         |     | --           |         |
| Command        | Information |         |     |              |         |
ARP|210

| Platforms | Command | context | Authority |     |     |
| --------- | ------- | ------- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show arp           | vrf   |             |     |     |     |
| ------------------ | ----- | ----------- | --- | --- | --- |
| show arp {all-vrfs | | vrf | <VRF-NAME>} |     |     |     |
Description
ShowstheARPtableforallVRFinstances,orforthenamedVRF.
| Parameter |     |     | Description       |     |     |
| --------- | --- | --- | ----------------- | --- | --- |
| all-vrfs  |     |     | SpecifiesallVRFs. |     |     |
vrf <VRF-NAME> SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
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
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 211

| Release        |             |         |         | Modification |     |     |     |
| -------------- | ----------- | ------- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier |             |         |         | --           |     |     |     |
| Command        | Information |         |         |              |     |     |     |
| Platforms      |             | Command | context | Authority    |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show      | ipv6      | neighbors |     |                   |     |     |     |
| --------- | --------- | --------- | --- | ----------------- | --- | --- | --- |
| show ipv6 | neighbors | {all-vrfs |     | | vrf <VRF-NAME>} |     |     |     |
Description
ShowsentriesintheARPtableforallIPv6neighborsforallVRFsorforaspecificVRF.
Whennoparametersarespecified,thiscommandshowsallARPentriesforthedefaultVRF,andstate
informationforreachableandstaleentriesonly.
| Parameter |     |     |     | Description       |     |     |     |
| --------- | --- | --- | --- | ----------------- | --- | --- | --- |
| all-vrfs  |     |     |     | SpecifiesallVRFs. |     |     |     |
vrf <VRF-NAME> SpecifiesthenameofaVRF.Length:1to32alphanumeric
characters.
Examples
| switch# | show     | ipv6 neighbors |     |     |     |     |     |
| ------- | -------- | -------------- | --- | --- | --- | --- | --- |
| IPv6    | Entries: |                |     |     |     |     |     |
-------------------------------------------------------
| IPv6 | Address |     |     | MAC | Port | Physical Port | State |
| ---- | ------- | --- | --- | --- | ---- | ------------- | ----- |
fe80::a21d:48ff:fe8f:2700 a0:1d:48:8f:27:00 vlan2300 1/1/31 reachable
fe80::f603:43ff:fe80:a600 f4:03:43:80:a6:00 vlan2300 1/1/30 reachable
-------------------------------------------------------
| Total | Number | Of IPv6 | Neighbors | Entries Listed: | 2.  |     |     |
| ----- | ------ | ------- | --------- | --------------- | --- | --- | --- |
-------------------------------------------------------
| Command        | History     |     |     |              |     |     |     |
| -------------- | ----------- | --- | --- | ------------ | --- | --- | --- |
| Release        |             |     |     | Modification |     |     |     |
| 10.07orearlier |             |     |     | --           |     |     |     |
| Command        | Information |     |     |              |     |     |     |
ARP|212

| Platforms | Command | context |     | Authority |     |     |
| --------- | ------- | ------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager Administratorsorlocalusergroupmemberswithexecution
|           | (#)       |       |     | rightsforthiscommand. |     |     |
| --------- | --------- | ----- | --- | --------------------- | --- | --- |
| show ipv6 | neighbors | state |     |                       |     |     |
show ipv6 neighbors state {all | failed | incomplete | permanent | reachable | stale}
Description
ShowsallIPv6neighborARP(AddressResolutionProtocol)cacheentries,orthosecacheentriesthatare
inthespecifiedstate.
| Parameter |     |     |     | Description                                          |     |     |
| --------- | --- | --- | --- | ---------------------------------------------------- | --- | --- |
| all       |     |     |     | ShowsallARPcacheentries.                             |     |     |
| failed    |     |     |     | ShowsARPcacheentriesthatareinfailedstate.Theneighbor |     |     |
mighthavebeendeleted.Settheneighbortobeunreachable.
| incomplete |     |     |     | ShowsARPcacheentriesthatareinincompletestate. |     |     |
| ---------- | --- | --- | --- | --------------------------------------------- | --- | --- |
Anincompletestatemeansthataddressresolutionisinprogress
andthelink-layeraddressoftheneighborhasnotyetbeen
determined.Thismeansthatasolicitationrequestwassent,and
youarewaitingforasolicitationreplyoratimeout.
| permanent |     |     |     | ShowsARPcacheentriesthatareinpermanentstate. |     |     |
| --------- | --- | --- | --- | -------------------------------------------- | --- | --- |
reachable ShowsARPcacheentriesthatareinreachablestate,meaning
thattheneighborisknowntohavebeenreachablerecently.
| stale |     |     |     | ShowsARPcacheentriesthatareinstalestate. |     |     |
| ----- | --- | --- | --- | ---------------------------------------- | --- | --- |
ARPcacheentriesareinthestalestateiftheelapsedtimeisin
excessoftheARPtimeoutinsecondssincethelastpositive
confirmationthattheforwardingpathwasfunctioningproperly.
Example
| switch#      | show ipv6 neighbors |     | state | all |               |            |
| ------------ | ------------------- | --- | ----- | --- | ------------- | ---------- |
| IPv6 Address |                     |     | MAC   |     | Port Physical | Port State |
--------------------------------------------------------------------------------
| 100::2 |     |     | 48:0f:cf:af:f1:cc |     | lag1 lag1 |     |
| ------ | --- | --- | ----------------- | --- | --------- | --- |
reachable
| 300::3 |     |     | 48:0f:cf:af:33:be |     | vlan3 1/4/20 |     |
| ------ | --- | --- | ----------------- | --- | ------------ | --- |
reachable
| fe80::4a0f:cfff:feaf:f1cc |     |     | 48:0f:cf:af:f1:cc |     | lag1 lag1 |     |
| ------------------------- | --- | --- | ----------------- | --- | --------- | --- |
reachable
| 200::3 |     |     | 48:0f:cf:af:33:be |     | 1/4/11 1/4/11 |     |
| ------ | --- | --- | ----------------- | --- | ------------- | --- |
reachable
| fe80::4a0f:cfff:feaf:33be |     |     | 48:0f:cf:af:33:be |     | vlan3 1/4/20 |     |
| ------------------------- | --- | --- | ----------------- | --- | ------------ | --- |
reachable
| Total Number | Of IPv6 | Neighbors |     | Entries Listed- | 5.  |     |
| ------------ | ------- | --------- | --- | --------------- | --- | --- |
---------------------------------------------------------------------------------
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
AOS-CX10.10IPServicesGuide|(6200SwitchSeries) 213

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
ARP|214

Chapter 12

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

215

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
SupportandOtherResources|216

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

AOS-CX 10.10 IP Services Guide | (6200 Switch Series)

217