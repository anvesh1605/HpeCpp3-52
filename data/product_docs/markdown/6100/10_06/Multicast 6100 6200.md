AOS-CX 10.06 Multicast Guide
6100, 6200 Switch Series

Part Number: 5200-7716a
Published: January 2021
Edition: 2

© Copyright 2020 Hewlett Packard Enterprise Development LP

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
Enterprise has no control over and is not responsible for information outside the Hewlett Packard Enterprise
website.

Contents

Chapter 1 About this document...................................................................... 7
Applicable products........................................................................................................................................7
Latest version available online......................................................................................................................7
Command syntax notation conventions..................................................................................................... 7
About the examples....................................................................................................................................... 8
Identifying switch ports and interfaces .......................................................................................................8

Chapter 2 Multicast overview........................................................................ 10
Introduction to multicast.............................................................................................................................10
Multicast protocols.......................................................................................................................................10
Multicast addresses..................................................................................................................................... 10

Chapter 3 Internet Group Management Protocol (IGMP)........................12
Internet Group Management Protocol (IGMP) overview......................................................................... 12
IGMP defaults, protocols, and supported configuration......................................................................... 12
How the IGMP protocol works.................................................................................................................... 12
Considerations when configuring IGMP.................................................................................................... 13
IGMP configuration task list........................................................................................................................ 14
Enabling or disabling IGMP......................................................................................................................... 14
Specifying the IGMP version....................................................................................................................... 15
Configuring IGMP static groups.................................................................................................................. 15
Configuring IGMP query and response parameters................................................................................ 16
Disabling IGMP..............................................................................................................................................16
Viewing IGMP information.......................................................................................................................... 17
IGMP configuration example...................................................................................................................... 17
IGMP commands.......................................................................................................................................... 18
ip igmp............................................................................................................................................. 18
ip igmp apply access-list.................................................................................................... 19
ip igmp last-member-query-interval................................................................................ 19
ip igmp querier........................................................................................................................... 20
ip igmp querier interval.......................................................................................................21
ip igmp querier query-max-response-time.....................................................................21
ip igmp robustness.................................................................................................................... 22
ip igmp static-group................................................................................................................23
ip igmp version........................................................................................................................... 23
ip igmp version strict........................................................................................................... 24
no ip igmp...................................................................................................................................... 24
show ip igmp..................................................................................................................................25
show ip igmp counters............................................................................................................. 26
show ip igmp group.................................................................................................................... 27
show ip igmp groups.................................................................................................................. 29
show ip igmp interface........................................................................................................... 31
show ip igmp interface counters....................................................................................... 31
show ip igmp interface group..............................................................................................32
show ip igmp interface groups........................................................................................... 33
show ip igmp interface statistics.................................................................................. 34
show ip igmp static-groups.................................................................................................. 35

Contents

3

show ip igmp statistics......................................................................................................... 36

Chapter 4 IGMP snooping................................................................................37
IGMP snooping overview............................................................................................................................. 37
IGMP snooping defaults, protocols, and supported configuration........................................................37
How IGMP snooping works......................................................................................................................... 38
IGMP snooping configuration task list....................................................................................................... 39
Enabling or disabling IGMP snooping........................................................................................................ 39
Specifying the IGMP snooping version...................................................................................................... 39
Configuring IGMP snooping static groups.................................................................................................40
Enabling drop-unknown filters................................................................................................................... 40
Configuring IGMP snooping fast learn ports globally.............................................................................. 40
Configuring IGMP snooping per port filtering.......................................................................................... 41
Disabling IGMP snooping............................................................................................................................ 41
Viewing IGMP snooping information......................................................................................................... 42
IGMP Snooping commands.........................................................................................................................42
ip igmp snooping {enable|disable}.................................................................................. 42
ip igmp snooping apply access-list................................................................................ 43
ip igmp snooping auto............................................................................................................. 44
ip igmp snooping blocked.......................................................................................................45
ip igmp snooping drop-unknown........................................................................................... 45
ip igmp snooping fastlearn.................................................................................................. 46
ip igmp snooping fastleave.................................................................................................. 47
ip igmp snooping forced fastleave.................................................................................. 48
ip igmp snooping forward.......................................................................................................48
ip igmp snooping static-group........................................................................................... 49
ip igmp snooping version.......................................................................................................50
no ip igmp snooping.................................................................................................................. 50
show ip igmp snooping............................................................................................................. 51
show ip igmp snooping counters......................................................................................... 51
show ip igmp snooping groups..............................................................................................52
show ip igmp snooping static-groups.............................................................................. 53
show ip igmp snooping statistics.....................................................................................53
show ip igmp snooping vlan.................................................................................................. 54
show ip igmp snooping vlan counters.............................................................................. 56
show ip igmp snooping vlan group port......................................................................... 57
show ip igmp snooping vlan statistics......................................................................... 58

Chapter 5 MLD snooping commands........................................................... 59
MLD snooping functionality........................................................................................................................ 59
MLD snooping global configuration commands...................................................................................... 59
[no] ipv6 mld snooping [drop-unknown [vlan-shared | vlan-exclusive]]... 59
MLD snooping VLAN configuration commands........................................................................................60
ipv6 mld snooping...................................................................................................................... 60
ipv6 mld snooping fastlearn................................................................................................ 60
ipv6 mld snooping fastleave................................................................................................ 61
ipv6 mld snooping forced fastleave................................................................................ 62
ipv6 mld snooping [version <ver>].................................................................................. 62
ipv6 mld snooping apply access-list.............................................................................. 63
ipv6 mld snooping [auto <port-list>]............................................................................64
ipv6 mld snooping [blocked <port-list>].....................................................................64
ipv6 mld snooping [forward <port-list>].....................................................................65
ipv6 mld snooping [static-group <X:X::X:X>]............................................................65

4

AOS-CX 10.06 Multicast Guide

MLD snooping show commands................................................................................................................ 66
show ipv6 mld snooping........................................................................................................... 66
show ipv6 mld snooping [counters].................................................................................. 67
show ipv6 mld snooping [groups]....................................................................................... 68
show ipv6 mld snooping [statistics].............................................................................. 68
show ipv6 mld snooping [vlan <vlan-id> [counters]]............................................ 69
show ipv6 mld snooping [vlan <vlan-id> [statistics]]........................................70
show ipv6 mld snooping [vlan <vlan-id> [group [<group-ip>] [source
<source-ip>]]]............................................................................................................................. 71
show ipv6 mld snooping [vlan <vlan-id> [group [port <port_id>]]...............73
show ipv6 mld snooping [static-groups]....................................................................... 74
MLD configuration commands for interface VLAN.................................................................................. 74
ipv6 mld {enable | disable}................................................................................................ 74
ipv6 mld apply access-list.................................................................................................. 75
no ipv6 mld.................................................................................................................................... 76
ipv6 mld querier.........................................................................................................................76
ipv6 mld querier [interval <interval-value>]..........................................................77
ipv6 mld last-member-query-interval <interval-value>........................................77
ipv6 mld querier query-max-response-time <response-time>...............................78
ipv6 mld robustness.................................................................................................................. 78
ipv6 mld static-group <multicast-group-ip>.............................................................. 79
ipv6 mld version <version>.................................................................................................. 80
ipv6 mld version <version> [strict].............................................................................. 80
MLD show commands for interface VLAN................................................................................................ 81
show ipv6 mld............................................................................................................................... 81
show ipv6 mld [interface <intf_id> | vlan <vlan-id>]........................................81
show ipv6 mld [all-vrfs ].................................................................................................... 82
show ipv6 mld [interface <intf-id> | vlan <vlan-id>] [counters]]............ 83
show ipv6 mld [interface <intf-id> | vlan <vlan-id>] [groups]]................. 84
show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group
<group_ip>] [source <source_ip>]]]].............................................................................. 85
show ipv6 mld [groups]........................................................................................................... 86
show ipv6 mld groups [all-vrfs]....................................................................................... 87
show ipv6 mld [interface <intf-id> [counters]]..................................................... 88
show ipv6 mld [interface <intf-id> [statistics]].................................................89
show ipv6 mld [interface <intf-id> [groups]]..........................................................89
show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group
<group_ip>] [source <source_ip>]]]].............................................................................. 90
show ipv6 mld [group <group_ip> [all-vrfs]]............................................................91
show ipv6 mld [group <group_ip> [source <source_ip> [all-vrfs]]]............ 92
show ipv6 mld [interface vlan <vlan-id> [statistics]]..................................... 93
show ipv6 mld [static-groups [all-vrfs]]...................................................................94
show ipv6 mld counters........................................................................................................... 95
MLD configuration commands for interface.............................................................................................96
ipv6 mld {enable | disable}................................................................................................ 96
ipv6 mld apply access-list.................................................................................................. 96
no ipv6 mld.................................................................................................................................... 97
ipv6 mld querier.........................................................................................................................98
ipv6 mld querier [interval <interval-value>]..........................................................98
ipv6 mld last-member-query-interval.............................................................................. 99
ipv6 mld querier query-max-response-time...................................................................99
ipv6 mld robustness................................................................................................................100
ipv6 mld static-group........................................................................................................... 100
ipv6 mld version.......................................................................................................................101

Contents

5

ipv6 mld version [strict].................................................................................................. 101

Chapter 6 Support and other resources.................................................... 103
Accessing Aruba Support.......................................................................................................................... 103
Accessing updates......................................................................................................................................103
Warranty information................................................................................................................................ 104
Regulatory information............................................................................................................................. 104
Documentation feedback..........................................................................................................................104

6

AOS-CX 10.06 Multicast Guide

Chapter 1
About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

• Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

• Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and other resources.

Command syntax notation conventions

Convention

example-text

Usage

Identifies commands and their options and operands, code examples,
filenames, pathnames, and output displayed in a command window.
Items that appear like the example text in the previous column are to be
entered exactly as shown and are required unless enclosed in brackets
([ ]).

example-text

In code and screen examples, indicates text entered by a user.

Any of the following:

• <example-text>

• <example-text>

• example-text

•

example-text

|

{ }

Identifies a placeholder—such as a parameter or a variable—that you
must substitute with an actual value in a command or in code:

•

•

For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

For output formats where italic text can be displayed, variables might
or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

Vertical bar. A logical OR that separates multiple items from which you
can choose only one.

Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

Braces. Indicates that at least one of the enclosed items is required.

Chapter 1 About this document

Table Continued

7

Convention

Usage

[ ]

… or

...

Brackets. Indicates that the enclosed item or items are optional.

Ellipsis:

•

•

In code and screen examples, a vertical or horizontal ellipsis indicates
an omission of information.

In syntax using brackets and braces, an ellipsis indicates items that
can be repeated. When an item followed by ellipses is enclosed in
brackets, zero or more items can be specified.

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

8

AOS-CX 10.06 Multicast Guide

On the 6100 Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Always 1. This is not a modular switch, so there are no slots.

• port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6200 Switch Series

• member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The
primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•

slot: Always 1. This is not a modular switch, so there are no slots.

• port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

Chapter 1 About this document

9

Chapter 2
Multicast overview

Introduction to multicast
Multicast addressing allows one-to-many or many-to-many communication among hosts on a network.
Typical applications of multicast communication include: audio and video streaming, desktop conferencing,
collaborative computing, and similar applications.

IGMP snooping (Internet Group Management Protocol controls) can be configured per-VLAN basis to reduce
unnecessary bandwidth usage. In the factory default state (IGMP and IGMP snooping disabled), the switch
simply floods all IP multicast traffic it receives on a given VLAN through all ports on that VLAN (except the
port on which it received the traffic). This can result in significant and unnecessary bandwidth usage in
networks where IP multicast traffic is a factor. Enabling IGMP allows the ports to detect IGMP queries and
report packets and manage IP multicast traffic through the switch. IGMP will be configured on the hosts, and
multicast traffic will be generated by one or more servers (inside or outside of the local network). Switches in
the network (that support IGMP snooping) can then be configured to direct the multicast traffic to only the
ports where needed. If multiple VLANs are configured, you can configure IGMP snooping on a per-VLAN
basis.

Multicast Listener Discovery (MLD) is an IPv6 protocol used on a local link for multicast group management.
MLD snooping is a subset of the MLD protocol that operates at the port level and conserves network
bandwidth by reducing the flooding of multicast IPv6 packets.

Multicast protocols
Layer 3 multicast protocols include:

•

IGMP (Internet Group Management Protocol) for last-hop multicast group management. Current RFCs
include:

◦

◦

IGMPv2 (RFC 2236)

IGMPv3 (RFC 3376)

• MLD (Multicast Listener Discovery) v1 and v2

◦ MLD v1 - RFC 2710

◦ MLD v2 - RFC 3810

Layer 2 multicast protocol:

•

IGMP snooping for IPv4 multicast filtering.

• MLD snooping for IPv6 multicast filtering.

Multicast addresses
Each multicast host group is identified by a single IP address in the range of 224.0.0.0 through
239.255.255.255.

10

AOS-CX 10.06 Multicast Guide

• For the 6100 switch: AOS-CX supports 512 IPv4 multicast flows.

• For the 6200 switch: AOS-CX supports 1K IPv4 multicast flows.

For a list of all reserved and well known multicast addresses, see the standards document at the following
links:

• https://www.iana.org/assignments/multicast-addresses/multicast-addresses.xhtml

• https://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml

Chapter 2 Multicast overview

11

Chapter 3
Internet Group Management Protocol (IGMP)

Internet Group Management Protocol (IGMP) overview
In a network where IP multicast traffic is transmitted for various multimedia applications, you can use the
switch to reduce unnecessary bandwidth usage on a per-port basis by configuring IGMP (Internet Group
Management Protocol). IGMPv3 (RFC 3376) and IGMPv2 (RFC 2236) are the current RFCs for IGMP.

In the factory default state (IGMP disabled), the switch simply floods all IP multicast traffic it receives on a
given VLAN through all ports on that VLAN (except the port on which it received the traffic). This can result in
significant and unnecessary bandwidth usage in networks where IP multicast traffic is a factor. Enabling
IGMP allows the ports to detect IGMP queries and report packets and manage IP multicast traffic through
the switch.

IGMP is useful in multimedia applications such as LAN TV, desktop conferencing, and collaborative
computing, where there is MultiPoint communication; that is, communication from one to many hosts, or
communication originating from many hosts and destined for many other hosts.

In such MultiPoint applications, IGMP will be configured on the hosts, and multicast traffic will be generated
by one or more servers (inside or outside of the local network). Switches in the network (that support IGMP)
can then be configured to direct the multicast traffic to only the ports where needed. If multiple VLANs are
configured, you can configure IGMP on a per-VLAN basis.

Enabling IGMP allows the router to become querier. If there is another querier in the LAN, the router will
resume non querier functionality and will respond to query/report packets.

IGMP defaults, protocols, and supported configuration
IGMP default configuration:

•

IGMP is disabled by default.

• The default IGMP version is IGMPv3.

IGMP supported protocols include:

•

•

IGMPv2 (RFC 2236)

IGMPv3 (RFC 3376)

Static groups:

You can configure a maximum of 512 (6100 switch) or 32 (6200 switch) IGMP static groups.

How the IGMP protocol works
IGMP manages multicast group memberships based on the query and response mechanism.

IGMP is an internal protocol of the IP suite. IP manages multicast traffic by using switches, multicast routers,
and hosts that support IGMP. A multicast router is not necessary as long as a switch is configured to support
IGMP with the querier feature enabled. A set of hosts, routers, and/or switches that send or receive

12

AOS-CX 10.06 Multicast Guide

multicast data streams to or from the same sources, is called a multicast group. All devices in the group use
the same multicast group address.

The multicast group uses three fundamental types of messages to communicate:

• Query: A message sent from the querier (multicast router or switch) asking for a response from each host
belonging to the multicast group. If a multicast router supporting IGMP is not present, the switch must
assume this function to elicit group membership information from the hosts on the network.

•

•

Join: A message sent by a host to the querier to indicate that the host wants to be or is a member of a
given group indicated in the join message.

Leave group: A message sent by a host to the querier to indicate that the host has ceased to be a
member of a specific multicast group.

An IP multicast packet includes the multicast group (address) to which the packet belongs. When an IGMP
client connected to a switch port needs to receive multicast traffic from a specific group, it joins the group by
sending an IGMP join request to the network. (The multicast group specified in the join request is
determined by the requesting application running on the IGMP client.)

When the client is ready to leave the multicast group, it sends a Leave Group message to the network and
ceases to be a group member. When the leave request is detected, the appropriate IGMP device ceases
transmitting traffic for the designated multicast group through the port on which the leave request was
received (as long as there are no other current members of that group on the affected port.)

Thus, IGMP identifies members of a multicast group (within a subnet) and allows IGMP-configured hosts
(and routers) to join or leave multicast groups.

Considerations when configuring IGMP
With the factory default setting, multicast data transmitted from the sources will be flooded on all ports in
the VLAN. Configuring IGMP snooping avoids flooding and causes the switch to forward data only to the
receivers.

The function of the IGMP querier is to poll other IGMP-enabled devices in an IGMP-enabled interface to elicit
group membership information. On enabling IGMP, the router performs this function if there is no other
device in the interface to act as querier.

Basic steps to configure IGMP:

1. Configure VLANs.

2. Configure ports and assign them to the VLANs.

3. Configure the L3 interface (an interface VLAN) and assign an IP address to the interface.

4. Enable IGMP.

5. Choose the desired IGMP version. The default is version 3.

IGMP configuration considerations:

•

For IGMP to be operational, the interface has to be administratively up. For interface VLANs, the L2 VLAN
has to be up and one of the ports in the VLAN has to be up.

• The IP address must be assigned for the interface to become querier. Without an IP address, the device

will remain in a non querier state.

• A querier is required for proper IGMP operation. For this reason, you must enable IGMP on the L3

Interface. If the querier functionality is not configured or disabled, you must ensure that there is an IGMP
querier in the same VLAN.

Chapter 3 Internet Group Management Protocol (IGMP)

13

•

•

•

For IGMP snooping to be operational on a VLAN, the VLAN has to be administratively up and at least one
port in the VLAN has to be up.

If IGMP snooping is enabled on the VLAN, and IGMP is enabled on the interface VLAN, and the configured
version does not match, the lowest version is chosen as the operating version.

If the switch becomes the querier for a particular interface, then subsequently detects queries
transmitted from another device on the same VLAN, the switch ceases to operate as the querier for that
interface.

• The switch automatically ceases querier operation in an IGMP-enabled interface if it detects another

querier on the interface. You can also use the switch CLI to disable the querier capability.

• Multicast traffic will be flooded on the VLAN, if TTL=1 or TTL>255 regardless of IGMP joins and group

membership within the VLAN.

IGMP configuration task list
Tasks at a glance.

• Enabling or disabling IGMP

• Specifying the IGMP version

• Configuring IGMP static groups

• Configuring IGMP query and response parameters

• Disabling IGMP

• Viewing IGMP information

Enabling or disabling IGMP

Prerequisites

You must be in an interface configuration context, as indicated by the switch(config-if-vlan)# prompt.

For IGMP to be operational, the interface has to be up. To become querier, the interface must have an IP
address associated with it.

Procedure

IGMP is disabled by default. Enable IGMP on an interface using the following command.

ip igmp {enable | disable}

For example, the following command enables IGMP on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp enable

14

AOS-CX 10.06 Multicast Guide

Use the disable parameter to disable IGMP on an interface.

Specifying the IGMP version
The version can be either 2 (IGMPv2) or 3 (IGMPv3). The default is 3. IGMPv2 supports filtering based on
groups. IGMPv3 is more advanced and includes filtering based on source and groups.

If using the strict option, packets that do not match the configured version will be dropped.

Prerequisites

You must be in an interface configuration context, as indicated by the switch(config-if-vlan)# prompt.

Procedure

Specify the IGMP version for an interface using one of the following commands.

ip igmp version <VERSION>

ip igmp version <VERSION> strict

For example, the following command sets the IGMP version to 2 on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp version 2

And the following command sets IGMP strict version to 2 on interface VLAN 5:

switch(config)# interface vlan 5
switch(config-if-vlan)# ip igmp version 2 strict
switch(config-if-vlan)# no ip igmp version 2 strict

Configuring IGMP static groups
The switch will always flood the traffic destined for a group configured as static group. So the hosts will
receive the traffic for static groups even if they have not subscribed for that group. You can configure a
maximum of 32 IGMP static groups.

Prerequisites

You must be in an interface configuration context, as indicated by the switch(config-if-vlan)# prompt.

Procedure

Configure an IGMP static group on an interface using the following command.

ip igmp static-group <MULTICAST-GROUP-IP>

For example, the following command configures an IGMP static multicast group as 239.1.1.1 on interface
VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp static-group 239.1.1.1

Chapter 3 Internet Group Management Protocol (IGMP)

15

The no form of the command removes an IGMP static group.

Configuring IGMP query and response parameters
Configure query and response parameters such as querier interval, last member query interval, max
response time, and robustness.

Prerequisites

You must be in an interface configuration context, as indicated by the switch(config-if-vlan)# prompt.

Procedure

1. Configure IGMP query and response parameters on an interface using the following commands.

• Make sure that the IGMP querier is enabled. (In IGMPv3 the IGMP querier is enabled by default.)
Configure the IGMP querier on an interface using the following command: ip igmp querier.

• Configure the IGMP querier interval on an interface using the following command: ip igmp querier

interval <INTERVAL-VALUE>. The interval is from 5-300 seconds, with a default of 125.

• Configure the IGMP last member query interval value in seconds on an interface using the following

command: ip igmp last-member-query-interval <INTERVAL-VALUE>. The interval is from 1-2
seconds, with a default of 1.

• Configure the IGMP max response time value in seconds on an interface using the following

command: ip igmp querier query-max-response-time <RESPONSE-TIME>. The response time
is from 10-128 seconds, with a default of 10.

• Configure the IGMP robustness (the number of times to retry a query) on an interface using the

following command: ip igmp robustness <VALUE>. The robustness value is from 1-7 with default
of 2.

For example, the following command configures the IGMP querier interface interval as 100 on interface
VLAN 2. The no form of the command sets the interval to the default.

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp querier interval 100
switch(config-if-vlan)# no ip igmp querier interval

Disabling IGMP

Prerequisites

You must be in an interface configuration context, as indicated by the switch(config-if-vlan)# prompt.

Procedure

Remove IGMP from an interface using the following command.

no ip igmp

For example, the following command removes IGMP on interface VLAN 2:

16

AOS-CX 10.06 Multicast Guide

switch(config)# interface vlan 2
switch(config-if-vlan)# no ip igmp

Viewing IGMP information
For some commands, you can specify viewing information by interface or by VRF.

Prerequisites

Use these show commands from the Operator (>) or Manager (#) context.

Procedure

1. To view IGMP information, use the following commands.

• To view IGMP configuration details and status, use: show ip igmp or use show ip igmp

interface.

• To view IGMP statistics and groups joined, use: show ip igmp statistics or use show ip igmp

interface statistics.

• To view IGMP counters, use: show ip igmp counters or use show ip igmp interface

counters.

• To view IGMP static groups, use: show ip igmp static-groups.

• To view IGMP group information, use: show ip igmp groups or use show ip igmp interface

groups.

• To view IGMP group details for a specific group and source, use: show ip igmp group or use show

ip igmp interface group. Optionally you can also display joined group details by VRF.

IGMP configuration example
The output of the following show running-config command shows an example of an IGMP configuration
with IGMP snooping.

switch# show running-config
Current configuration:
!
!
!
!
!
vlan 1
    no shutdown
vlan 2
    ip igmp snooping enable
    ip igmp snooping version 2
    ip igmp snooping forward 1/1/1
    ip igmp snooping blocked 1/1/3
    ip igmp snooping static group 239.1.1.10
    ip igmp snooping static group 239.1.1.11
interface 1/1/1
    no shutdown
    vlan access 2
interface 1/1/2
    no shutdown

Chapter 3 Internet Group Management Protocol (IGMP)

17

    vlan access 2
interface 1/1/3
    no shutdown
    vlan access 2
interface vlan2
    no shutdown
    ip address 20.1.1.1/24
    ip igmp enable
    ip igmp version 2
    ip igmp querier interval 5
    ip igmp robustness 5
    ip igmp last-member-query-interval 2
    ip igmp query-max-response-time 50
    ip igmp static-group 239.1.1.1

IGMP commands
For commands in the interface configuration context, the interface must be an L3 interface. The supported
contexts includes: config-if-vlan.

ip igmp

Syntax

ip igmp {enable | disable}

Description

Enables or disables IGMP on the current interface. IGMP is disabled by default.

Command context

config-if-vlan

Parameters
enable

Enable IGMP.

disable

Disable IGMP.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling IGMP on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp enable

Disabling IGMP on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp disable

18

AOS-CX 10.06 Multicast Guide

ip igmp apply access-list

Syntax

ip igmp apply access-list <ACL-NAME>

no ip igmp apply access-list <ACL-NAME>

Description

Configures the ACL on a particular interface to filter the IGMP join or leave packets based on rules set in the
particular ACL name.

The no form of this command unconfigures the rules set for the ACL.

NOTE: This configuration will override the ACL associated with IGMP snooping on the
corresponding L2 VLAN.

Command context

config-if-vlan

Parameters
access-list

Associates an ACL with the IGMP.

<ACL-NAME>

Specifies the name of the ACL.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Existing classifier commands are used to configure the ACL. In case an IGMPv3 packet with multiple group
addresses is received, it will only process the permitted group addresses based on the ACL rule set, and any
existing joins will time out. If there is no match or if there is a deny rule match, the packet is dropped.

Examples

Configuring the ACL on a VLAN to filter IGMP packets based on rules set in access list mygroup:

switch(config)# access-list ip mygroup
switch(config-acl-ip)# permit igmp any 239.1.1.1
switch(config-acl-ip)# exit
switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp apply access-list mygroup

Configuring the ACL to remove the rules set in access list mygroup:

switch(config-if-vlan)# no ip igmp apply access-list mygroup

ip igmp last-member-query-interval

Syntax

ip igmp last-member-query-interval <INTERVAL-VALUE>

no ip igmp last-member-query-interval <INTERVAL-VALUE>

Chapter 3 Internet Group Management Protocol (IGMP)

19

Description

Configures an IGMP last member query interval value in seconds on an interface, depending on the
command context you are in.

The no form of this command sets the value to a default of 1 second on an interface.

Command context

config-if-vlan

Parameters
<INTERVAL-VALUE>

Specifies an IGMP last-member-query-interval on the interface. Default: 1 second. Range: 1-2 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring an IGMP last member query interval of 2 on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp last-member-query-interval 2
switch(config-if-vlan)# no ip igmp last-member-query-interval

ip igmp querier

Syntax

ip igmp querier

no ip igmp querier

Description

Configures an IGMP querier on an interface, depending on the command context you are in. This
functionality will allow an interface to join in the querier-election process.

The no form of this command disables IGMP querier on an interface.

Command context

config-if-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring an IGMP querier on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp querier
switch(config-if-vlan)# no ip igmp querier

20

AOS-CX 10.06 Multicast Guide

ip igmp querier interval

Syntax

ip igmp querier interval <INTERVAL-VALUE>

no ip igmp querier interval

Description

Configures the interval between IGMP queries on an interface, depending on the command context you are
in.

The no form of this command sets the IGMP querier interval to the default value of 125 seconds on an
interface.

Command context

config-if-vlan

Parameters
<INTERVAL-VALUE>

Specifies the IGMP querier interval in seconds on the interface. Default: 125 seconds. Range: 5-300.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring an IGMP querier interface interval of 100 on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp querier interval 100

Resetting an IGMP querier interval to the default value:

switch(config-if-vlan)# no ip igmp querier interval

ip igmp querier query-max-response-time

Syntax

ip igmp querier query-max-response-time <RESPONSE-TIME>

no ip igmp querier query-max-response-time <RESPONSE-TIME>

Description

Configures the IGMP querier max response time value in seconds on an interface, depending on the
command context you are in.

The no form of this command sets the querier max response time value to the default of 10 seconds on an
interface.

Command context

config-if-vlan

Chapter 3 Internet Group Management Protocol (IGMP)

21

Parameters
<RESPONSE-TIME>

Specifies the IGMP querier max response time value on the interface. Default: 10 seconds. Range:
10-128 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the IGMP querier maximum response time of 50 for interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp query-max-response-time 50

Resetting an IGMP querier interval to the default value:

switch(config-if-vlan)# no ip igmp query-max-response-time

ip igmp robustness

Syntax

ip igmp robustness <VALUE>

no ip igmp robustness <VALUE>

Description

Configures IGMP robustness on an interface, depending on the command context. The robustness
parameter allows tuning for the expected packet loss on a subnet.

The no form of this command sets the robustness value to the default of 2 on an interface.

Command context

config-if-vlan

Parameters
<VALUE>

Specifies an IGMP robustness value on the interface. Default: 2. Range: 1-7.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring an IGMP robustness of 5 on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp robustness 5

Resetting the IGMP robustness to the default:

switch(config-if-vlan)# no ip igmp robustness

22

AOS-CX 10.06 Multicast Guide

ip igmp static-group

Syntax

ip igmp static-group <MULTICAST-GROUP-IP>

no ip igmp static-group <MULTICAST-GROUP-IP>

Description

Configures an IGMP static multicast group on an interface, depending on the command context you are in.
You can configure a maximum of 32 IGMP static groups.

The no form of the command unconfigures IGMP static multicast group on an interface.

Command context

config-if-vlan

Parameters
<MULTICAST-GROUP-IP>

Specifies an IGMP static multicast group IP address on the interface. Format: A.B.C.D

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring an IGMP static group on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp static-group 239.1.1.1

Resetting an IGMP static group on an interface to the default (none):

switch(config-if)# no ip igmp static-group 239.1.1.10

ip igmp version

Syntax

ip igmp version <VERSION>

Description

Configures the IGMP version on an interface, depending on the command context you are in.

Command context

config-if-vlan

Parameters
<VERSION>

Specifies the IGMP version on the interface. Select 2 for IGMPv2 (RFC2236). Select 3 for IGMPv3
(RFC3376). Values: 2 or 3.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 3 Internet Group Management Protocol (IGMP)

23

Examples

Configuring an IGMP version on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp version 2

ip igmp version strict

Syntax

ip igmp version <VERSION> strict

no ip igmp version <VERSION> strict

Description

Configures an IGMP strict version on an interface, depending on the command context you are in. Drops
packets that do not match the configured version.

The no form of the command removes the strict version configuration from the interface.

Command context

config-if-vlan

Parameters
<VERSION>

Specifies the IGMP version on the interface. Select 2 for IGMPv2 (RFC2236). Select 3 for IGMPv3
(RFC3376). Values: 2 or 3.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the IGMP strict version to 2 on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# ip igmp version 2 strict

Resetting the IGMP strict version to the default (none):

switch(config-if)# no ip igmp version 2 strict

no ip igmp

Syntax

no ip igmp

Description

Disables all IGMP configurations on an interface, depending on the command context you are in.

Command context

config-if-vlan

24

AOS-CX 10.06 Multicast Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Removes IGMP on interface VLAN 2:

switch(config)# interface vlan 2
switch(config-if-vlan)# no ip igmp

show ip igmp

Syntax

show ip igmp [all-vrfs]

Description

Shows IGMP configuration information and status, or shows information by VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

To show information for all VRFs, specify all-vrfs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP configuration and status:

switch# show ip igmp

VRF Name  : default
Interface : vlan2
IGMP Configured Version    : 3
IGMP Operating Version     : 3
Querier State              : Querier
Querier IP [this switch]   : 20.1.1.1
Querier Uptime             : 1m 4s
Querier Expiration Time    : 0m 1s
IGMP Snoop Enabled on VLAN : True

Showing IGMP information for all VRFs:

switch# show ip igmp all-vrfs

VRF Name  : default
Interface  : vlan5
IGMP Configured Version    : 3
IGMP Operating Version     : 2
Querier State              : Querier
Querier IP [this switch]   : 50.1.1.1
Querier Uptime             : 1m 1s

Chapter 3 Internet Group Management Protocol (IGMP)

25

Querier Expiration Time    : 0m 4s
IGMP Snoop Enabled on VLAN : False

show ip igmp counters

Syntax

show ip igmp counters [all-vrfs]

Description

Shows IGMP counter details, or shows counters by VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Specify all-vrfs to show information for all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP counters:

switch# show ip igmp counters

IGMP Counters

Interface Name      : vlan2
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------
V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             12
V3 All Hosts Queries                         0             0
V2 Group Specific Queries                    0             0
V3 Group Specific Queries                    0             0
Group And Source Specific Queries            0             0
V3 Member Reports                            0             N/A
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A
V2 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

Showing IGMP counters for the default VRF:

switch# show ip igmp counters vrf default

IGMP Counters

Interface Name      : vlan2
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------

26

AOS-CX 10.06 Multicast Guide

V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             12
V3 All Hosts Queries                         0             0
V2 Group Specific Queries                    0             0
V3 Group Specific Queries                    0             0
Group And Source Specific Queries            0             0
V3 Member Reports                            0             N/A
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A
V2 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

show ip igmp group

Syntax

show ip igmp group <GROUP-IP> [source <SOURCE-IP>] [all-vrfs]

Description

Shows IGMP joined group information for the specified group, or shows joined group source and display
information by VRF.

Command context

Operator (>) or Manager (#)

Parameters
<GROUP-IP>

Specifies the IP address of the group. Format: A.B.C.D

source <SOURCE-IP>

Specifies the IP address of the source. Format: A.B.C.D

all-vrfs

Specify all-vrfs to show information for all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP joined group details for group 239.1.1.10:

switch# show ip igmp group 239.1.1.10

IGMP group information for group 239.1.1.10

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.10
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  16m 34s   2m 27s

Chapter 3 Internet Group Management Protocol (IGMP)

27

Showing IGMP joined group details for group 239.1.1.10 and source 10.1.1.10:

switch# show ip igmp group 239.1.1.10 source 10.1.1.10

Interface Name  : vlan2
VRF Name  : default
Group Address  : 239.1.1.10
Source Address : 10.1.1.10

Mode Uptime    Expire
---- --------- -------
     0m 13s    4m 7s

Showing IGMP joined group details for group 239.1.1.10 for all VRFs:

switch# show ip igmp group 239.1.1.10 all-vrfs

IGMP group information for group 239.1.1.10

Interface Name   : vlan10
VRF Name         : default

Group Address    : 239.1.1.10
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  17m 5s    4m 2s

Showing IGMP joined group details for group 239.1.1.10 source 10.1.1.10 for all VRFs:

switch# show ip igmp group 239.1.1.10 source 10.1.1.10 all-vrfs

Interface Name  : vlan10
VRF Name  : default
Group Address  : 239.1.1.10
Source Address : 10.1.1.10

Mode Uptime    Expire
---- --------- -------
     0m 39s    3m 41s

Showing IGMP joined group details group 239.1.1.10 for the default VRF:

switch# show ip igmp group 239.1.1.10 vrf default

IGMP group information for group 239.1.1.10

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.10
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  17m 35s   3m 32s

Showing IGMP joined group details group 239.1.1.10 source 10.1.1.10 for the default VRF:

28

AOS-CX 10.06 Multicast Guide

switch# show ip igmp group 239.1.1.10 source 10.1.1.10 vrf default

Interface Name  : vlan10
VRF Name  : default
Group Address  : 239.1.1.10
Source Address : 10.1.1.10

Mode Uptime    Expire
---- --------- -------
     0m 59s    3m 21s

show ip igmp groups

Syntax

show ip igmp groups [all-vrfs]

Description

Shows IGMP group information, or you can display group information by VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Specify all-vrfs to show information for all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP group information:

switch# show ip igmp groups

IGMP group information for group 239.1.1.10

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.10
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  0m 36s    3m 44s

IGMP group information for group 239.1.1.11

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.11
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources

Chapter 3 Internet Group Management Protocol (IGMP)

29

Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  0m 36s    3m 44s

Showing IGMP groups for all VRFs:

switch# show ip igmp groups all-vrfs

IGMP group information for group 239.1.1.1

Interface Name   : vlan20
VRF Name         : default

Group Address    : 239.1.1.1
Last Reporter    : 200.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  0m 13s    4m 7s

IGMP group information for group 239.1.1.2

Interface Name   : vlan20
VRF Name         : default

Group Address    : 239.1.1.2
Last Reporter    : 200.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  0m 13s    4m 7s

Showing IGMP groups for the default VRF:

switch# show ip igmp groups vrf default

IGMP group information for group 239.1.1.10

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.10
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  9m 23s    3m 20s

IGMP group information for group 239.1.1.11

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.11
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    EXC  9m 23s    3m 20s

30

AOS-CX 10.06 Multicast Guide

show ip igmp interface

Syntax

show ip igmp interface {vlan <VLAN-ID>}

Description

Shows IGMP configuration information for a specific interface (VLAN).

Command context

Operator (>) or Manager (#)

Parameters
vlan <VLAN-ID>

Specifies a VLAN. Values: 1-4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP configuration information for interface VLAN 2:

switch# show ip igmp interface vlan 2

IGMP Configured Version  : 3
IGMP Operating Version   : 3
Querier State            : Querier
Querier IP [this switch] : 20.1.1.1
Querier Uptime           : 1m 46s
Querier Expiration Time  : 0m 1s
Snoop Enabled on VLAN    : True

show ip igmp interface counters

Syntax

show ip igmp interface {vlan <VLAN-ID>} counters

Description

Shows IGMP counter details for a specific interface or VLAN interface.

Command context

Operator (>) or Manager (#)

Parameters
vlan <VLAN-ID>

Specifies a VLAN. Values: 1-4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Chapter 3 Internet Group Management Protocol (IGMP)

31

Examples

Showing IGMP counters for interface VLAN 2:

switch# show ip igmp interface vlan 2 counters

IGMP Counters

Interface Name      : vlan2
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------
V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             0
V3 All Hosts Queries                         0             29
V2 Group Specific Queries                    0             0
V3 Group Specific Queries                    0             2
Group And Source Specific Queries            0             2
V3 Member Reports                            0             N/A
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A
V2 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

show ip igmp interface group

Syntax

show ip igmp interface {vlan <VLAN-ID>} group <GROUP-ID> [source <SOURCE-IP>]

Description

Shows IGMP joined group information for a specific interface or VLAN interface, or specify a source IP.

Command context

Operator (>) or Manager (#)

Parameters
vlan <VLAN-ID>

Specifies a VLAN. Values: 1-4094.

<GROUP-ID>

Specifies the IP address of the group. Format: A.B.C.D

source <SOURCE-IP>

Specifies the IP address of the source. Format: A.B.C.D

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP joined group details for group 239.1.1.1 for interface VLAN 10:

switch# show ip igmp interface vlan 10 group 239.1.1.1

IGMP group information for group 239.1.1.1

32

AOS-CX 10.06 Multicast Guide

Interface Name   : vlan10
VRF Name         : default

Group Address    : 239.1.1.1
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    INC  8m 10s    2m 21s                        1

Group Address  : 239.1.1.1
Source Address : 10.1.1.1

Mode Uptime    Expire
---- --------- -------
INC  8m 10s    2m 21s

Showing IGMP joined group details for group 239.1.1.1 for interface VLAN 10 with source details for 10.1.1.1:

switch# show ip igmp interface vlan 10 group 239.1.1.1 source 10.1.1.1

Interface Name  : vlan10
VRF Name  : default
Group Address  : 239.1.1.1
Source Address : 10.1.1.1

Mode Uptime    Expire
---- --------- -------
INC  8m 52s    3m 51s

show ip igmp interface groups

Syntax

show ip igmp interface {vlan <VLAN-ID>} groups

Description

Shows IGMP group information for a specific interface or VLAN interface.

Command context

Operator (>) or Manager (#)

Parameters
vlan <VLAN-ID>

Specifies a VLAN. Values: 1-4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP groups for interface VLAN 2:

switch# show ip igmp interface vlan 2 groups

IGMP group information for group 239.1.1.1

Chapter 3 Internet Group Management Protocol (IGMP)

33

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.1
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    INC  4m 40s    3m 51s                        1

Group Address  : 239.1.1.1
Source Address : 10.1.1.1

Mode Uptime    Expire
----------------------
INC  4m 40s    3m 51s

IGMP group information for group 239.1.1.2

Interface Name   : vlan2
VRF Name         : default

Group Address    : 239.1.1.2
Last Reporter    : 100.1.1.10

                              V1        V2        Sources   Sources
Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------- --------
3    INC  4m 40s    3m 51s                        1

Group Address  : 239.1.1.2
Source Address : 10.1.1.1

Mode Uptime    Expire
---- --------- -------
INC  4m 40s    3m 51s

show ip igmp interface statistics

Syntax

show ip igmp interface {vlan <VLAN-ID>} statistics

Description

Shows IGMP statistics for a specific interface or VLAN interface, including groups joined.

Command context

Operator (>) or Manager (#)

Parameters
vlan <VLAN-ID>

Specifies a VLAN. Values: 1-4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

34

AOS-CX 10.06 Multicast Guide

Examples

Showing IGMP statistics for interface VLAN 2:

switch# show ip igmp interface vlan 2 statistics

IGMP statistics

Interface Name : vlan2
VRF Name       : default

Number of Include Groups       :   2
Number of Exclude Groups       :   0
Number of Static Groups        :   0
Total Multicast Groups Joined  :   2

show ip igmp static-groups

Syntax

show ip igmp static-groups [all-vrfs]

Description

Shows IGMP static groups, or shows information by VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Specify all-vrfs to show information for all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP static-group information:

switch# show ip igmp static-groups

IGMP Static Group Address Information

VRF Name    default
Interface Name   Group Address
--------------- -----------------
vlan10            238.1.1.1

Showing IGMP statics-group information for all VRFs:

switch# show ip igmp static-groups all-vrfs

IGMP Static Group Address Information

VRF Name   :default
Interface Name   Group Address

Chapter 3 Internet Group Management Protocol (IGMP)

35

--------------- -----------------
vlan10            238.1.1.1

show ip igmp statistics

Syntax

show ip igmp statistics [all-vrfs]

Description

Shows IGMP statistics, including groups joined, or shows statistics by VRF.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Specify all-vrfs to show information for all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP statistics:

switch# show ip igmp statistics
IGMP statistics

VRF Name       : default

Number of Include Groups       :   1
Number of Exclude Groups       :   0
Number of Static Groups        :   0
Total Multicast Groups Joined  :   1

Showing IGMP statistics for all VRFs:

switch# show ip igmp statistics all-vrfs
IGMP statistics

VRF Name       : default

Number of Include Groups       :   1
Number of Exclude Groups       :   0
Number of Static Groups        :   0
Total Multicast Groups Joined  :   1

36

AOS-CX 10.06 Multicast Guide

Chapter 4
IGMP snooping

IGMP snooping overview
IGMP snooping runs on a Layer 2 device as a multicast constraining mechanism to improve multicast
forwarding efficiency. It creates Layer 2 multicast forwarding entries from IGMP packets that are exchanged
between the hosts and the router.

When IGMP snooping is not enabled, the snooping switch floods multicast packets to all hosts in a VLAN.
IGMP L2 snooping switch provides the benefit of conserving bandwidth on those segments of the network
where no node has expressed interest in receiving packets addressed to the group address. When IGMP
snooping is enabled, the L2 snooping switch forwards multicast packets of known multicast groups to only
the receivers.

IGMP snooping defaults, protocols, and supported
configuration
IGMP snooping default configuration:

•

IGMP snooping is disabled by default.

• Version 3 is used by default.

IGMP snooping related protocols:

•

•

IGMPv2 (RFC 2236)

IGMPv3 (RFC 2276)

• Considerations for Internet Group Management Protocol (IGMP) and Multicast Listener Discovery

(MLD) Snooping Switches (RFC 4541)

Chapter 4 IGMP snooping

37

Static groups:

You can configure a maximum of 32 IGMP snooping static groups.

How IGMP snooping works
IGMP message types include: Query, Report (Join), and Leave Group. An IGMP snooping enabled Layer 2
device performs differently depending on the message type.

Query

A message sent from the querier (multicast router or switch) asking for a response from each host
belonging to the multicast group. If a multicast router supporting IGMP is not present, then the switch must
assume this function in order to elicit group membership information from the hosts on the network.

The IGMP querier periodically sends IGMP general queries to all hosts and routers on the local subnet to
check for the existence of multicast group members. After receiving an IGMP general query, the snooping
switch forwards the query to all ports in the VLAN except the receiving port.

Report (Join)

A message sent by a host to the querier to indicate that the host wants to be or is a member of a given
group indicated in the report message.

A host sends an IGMP report to the IGMP querier for the following purposes:

• Responds to queries if the host is a multicast group member.

• Applies for a multicast group membership.

After receiving an IGMP report from a host, the snooping switch forwards the report through all the router
ports in the VLAN. It also looks up the forwarding table for a matching entry as follows:

•

•

•

If no match is found, the snooping switch creates a forwarding entry with the receiving port as an
outgoing interface. It also starts group membership expiry timer for the port to track the amount of time
that must pass before a multicast router decides there are no more members of a group on a network.

If a match is found but the matching forwarding entry does not contain the receiving port, the snooping
switch adds the receiving port to the outgoing interface list. It also starts group membership expiry timer
for the port.

If a match is found and the matching forwarding entry contains the receiving port, the snooping switch
restarts the group membership expiry timer for the port.

Leave Group

A message sent by a host to the querier to indicate that the host has ceased to be a member of a specific
multicast group.

An IGMPv1 receiver host does not send any leave messages when it leaves a multicast group. The snooping
switch cannot immediately update the status of the port that connects to the receiver host. The snooping
switch does not remove the port from the outgoing interface list in the associated forwarding entry until the
group membership timer expires.

An IGMPv2 or IGMPv3 host sends an IGMP leave message when it leaves a multicast group. Upon receiving
leave message, the switch forwards the IGMP leave message to all router ports in the VLAN . IGMP querier
then sends an IGMP group-specific query to the multicast group to identify whether the group has active
receivers attached to the receiving port.

After receiving the IGMP group-specific query, the switch forwards the query through all router ports and
member ports of the group in the VLAN. Then, it waits for the responding IGMP report message from the

38

AOS-CX 10.06 Multicast Guide

directly connected hosts. If the port does not receive an IGMP report message when the group membership
timer expires, the snooping switch removes the port from the forwarding entry for the multicast group.

IGMP snooping configuration task list

• Enabling or disabling IGMP snooping

• Specifying the IGMP snooping version

• Configuring IGMP snooping static groups

• Enabling drop-unknown filters

• Configuring IGMP snooping fast learn ports globally

• Configuring IGMP snooping per port filtering

• Disabling IGMP snooping

• Viewing IGMP snooping information

Enabling or disabling IGMP snooping
IGMP snooping is disabled by default. The default behavior is to flood multicast traffic in the VLAN. Use the
following to enable IGMP snooping.

Prerequisites

You must be in the VLAN configuration context, as indicated by the switch(config-vlan)# prompt.

The VLAN has to be configured and up.

Procedure

Enable IGMP snooping on a VLAN using the following command.

ip igmp snooping {enable | disable}

For example, the following command enables IGMP snooping on VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping enable

Use the no command to disable IGMP snooping on a VLAN.

Specifying the IGMP snooping version
The IGMP snooping version can be either 2 (IGMPv2) or 3 (IGMPv3). The default is 3. IGMPv2 supports
filtering based on groups. IGMPv3 is more advanced and includes filtering based on source and groups.

Prerequisites

You must be in the VLAN configuration context, as indicated by the switch(config-vlan)# prompt.

Procedure

Specify the IGMP snooping version for a VLAN using the following command.

Chapter 4 IGMP snooping

39

ip igmp snooping version <VERSION>

For example, the following command sets the IGMP snooping version to 2 on VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping version 2

Configuring IGMP snooping static groups
Configure IGMP snooping static groups.

Prerequisites

You must be in the VLAN configuration context, as indicated by the switch(config-vlan)# prompt.

Procedure

Configure an IGMP snooping static group on a VLAN using the following command.

ip igmp snooping static-group <MULTICAST-IP-ADDRESS>

For example, the following command configures the IGMP snooping static multicast group as 239.1.1.1 on
VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping static-group 239.1.1.1

The no form of the command removes the IGMP snooping static group.

Enabling drop-unknown filters
While IGMP snooping is enabled, the traffic will be forwarded only to joined ports. Configuring drop
unknown filters, ensures that packets are not forwarded to ports where a request for the traffic stream has
not been received.

This could either be a filter across all VLANs (vlan-shared) or per VLAN (vlan-exclusive). The default is
vlan-shared.

Prerequisites

You must be in the configuration context, as indicated by the switch(config)# prompt.

Procedure

Globally enable dropping multicast data using the following command.

ip igmp snooping drop-unknown {vlan-shared | vlan-exclusive}

For example, the following command configures a shared VLAN filter on the switch:

switch(config)# ip igmp snooping drop-unknown vlan-shared

Configuring IGMP snooping fast learn ports globally
Configuring fast learn on a port enables faster response to topology change notifications. When spanning
tree changes the port state from blocked to forwarding, the device acting as querier will immediately send a

40

AOS-CX 10.06 Multicast Guide

general query on the fast learn enabled port. Then the device acting as a non-querier will replay the joins.
This will help in faster convergence of multicast flows.

Prerequisites

You must be in the configuration context, as indicated by the switch(config)# prompt.

Procedure

Configure one or more ports as IGMP snooping fast learn ports using the following command.

ip igmp snooping fastlearn <PORT-LIST>

For example, the following command configures ports 1/1/1-1/1/3 as fast learn ports:

switch(config)# ip igmp snooping fastlearn 1/1/1-1/1/3

Configuring IGMP snooping per port filtering
Configure IGMP snooping traffic handling by specifying auto, blocked, or forward for a port, list of ports or
range of ports. In auto mode traffic flow is controlled by the IGMP joins/leaves. Auto mode is the default. In
blocked mode, joins and traffic are always blocked on this port. In forward mode traffic is always forwarded
on this port, irrespective of joins.

Prerequisites

You must be in the VLAN configuration context, as indicated by the switch(config-vlan)# prompt.

Procedure

1. Configure IGMP snooping traffic handling for ports on a VLAN using the following commands.

• Configure the specified ports in auto mode using the following command: ip igmp snooping auto

<PORT-LIST>.

• Configure the specified ports in blocked mode using the following command: ip igmp snooping

blocked <PORT-LIST>.

• Configure the specified ports in forward mode using the following command: ip igmp snooping

forward <PORT-LIST>.

For example, the following command configures ports 1/1/1, 1/1/2, and 1/1/3 in auto mode for VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping auto 1/1/1,1/1/2-1/1/3

Disabling IGMP snooping

Prerequisites

You must be in the VLAN configuration context, as indicated by the switch(config-vlan)# prompt.

Procedure

Disable IGMP snooping on a VLAN using the following command.

Chapter 4 IGMP snooping

41

no ip igmp snooping

For example, the following command removes IGMP snooping on VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# no ip igmp snooping

Viewing IGMP snooping information

Prerequisites

Use these show commands from the Operator (>) or Manager (#) context.

Procedure

1. To view IGMP snooping information, use the following commands.

• To view IGMP snooping configuration details and status, use: show ip igmp snooping.

• To view IGMP snooping query packet Tx, Rx, and Error packet counter details, use: show ip igmp

snooping counters.

• To view IGMP snooping group information, use: show ip igmp snooping groups.

• To view IGMP snooping protocol information and the number of groups joined, use: show ip igmp

snooping statistics.

• To view IGMP snooping query packet Tx, Rx, and Error packet counters for the specified VLAN, use:

show ip igmp snooping vlan counters.

• To view IGMP snooping statistics details for the specified VLAN including the number of different

groups joined for the VLAN, use: show ip igmp snooping vlan statistics.

• To view IGMP snooping group information for the specified VLAN, use: show ip igmp snooping

vlan.

• To view IGMP snooping group details for the specified VLAN including information about all IGMP
snooping groups or sources learned on a particular port, use: show ip igmp snooping vlan
group port.

• To view IGMP snooping static groups details for the specified VLAN, use: show ip igmp snooping

static-groups.

IGMP Snooping commands

ip igmp snooping {enable|disable}

Syntax

ip igmp snooping {enable | disable}

Description

Enables or disables IGMP snooping on the VLAN. By default, IGMP snooping is disabled.

42

AOS-CX 10.06 Multicast Guide

Command context

config-vlan

Parameters
{enable | disable}

Specifies enabling or disabling IGMP snooping on the VLAN. Default: disable.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enable IGMP snooping on a VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping enable

Disable IGMP snooping on a VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping disable

ip igmp snooping apply access-list

Syntax

ip igmp snooping apply access-list <ACL-NAME>

no ip igmp snooping apply access-list <ACL-NAME>

Description

Configures the ACL on a particular interface to filter the IGMP join or leave packets based on rules set in the
particular ACL name.

The no form of this command unconfigures the rules set for the ACL.

NOTE: This configuration will override the ACL associated with IGMP snooping on the
corresponding L2 VLAN.

Command context

config-vlan

Parameters
access-list

Associates an ACL with the IGMP.

<ACL-NAME>

Specifies the name of the ACL.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 4 IGMP snooping

43

Usage

Existing classifier commands are used to configure the ACL. In case an IGMPv3 packet with multiple group
addresses is received, it will only process the permitted group addresses based on the ACL rule set, and any
existing joins will time out. If there is no match or if there is a deny rule match, the packet is dropped.

NOTE: If the access list is configured for both L2 VLAN and L3 VLAN, the L3 VLAN configuration
will be applied.

Examples

Configuring the ACL to filter IGMP packets based on rules set in access list mygroup:

switch(config)# access-list ip mygroup
switch(config-acl-ip)# permit igmp any 239.1.1.1
switch(config-acl-ip)# exit
switch(config)# interface vlan 2
switch(config-vlan)# ip igmp snooping apply access-list mygroup

Configuring the ACL to remove the rules set in access list mygroup:

switch(config-vlan)# no ip igmp snooping apply access-list mygroup

ip igmp snooping auto

Syntax

ip igmp snooping auto <PORT-LIST>

no ip igmp snooping auto <PORT-LIST>

Description

Configures the specified ports in auto mode. In auto mode traffic flow is controlled by the IGMP joins/leaves.
Auto mode is the default.

The no form of this command removes auto mode ports for the VLAN.

Command context

config-vlan

Parameters
auto <PORT-LIST>

Specifies a list of ports to be configured as auto ports. You can specify a single port, a comma-separated
list of ports, or a range of ports such as 1/1/1-1/1/3.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configure auto ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping auto 1/1/1
switch(config-vlan)# ip igmp snooping auto 1/1/1,1/1/2-1/1/3

44

AOS-CX 10.06 Multicast Guide

ip igmp snooping blocked

Syntax

ip igmp snooping blocked <PORT-LIST>

no ip igmp snooping blocked <PORT-LIST>

Description

Configures the specified ports in blocked mode. In blocked mode, joins and traffic are always blocked on this
port.

The no form of this command disables blocked ports.

Command context

config-vlan

Parameters
blocked <PORT-LIST>

Specifies a list of ports to be configured in blocked mode. You can specify a single port, a comma-
separated list of ports or a range of ports such as 1/1/1-1/1/3.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring blocked ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping blocked 1/1/1
switch(config-vlan)# ip igmp snooping blocked 1/1/1-1/1/2
switch(config-vlan)# ip igmp snooping blocked 1/1/3,1/1/4-1/1/6
switch(config-vlan)# no ip igmp snooping blocked 1/1/1
switch(config-vlan)# no ip igmp snooping blocked 1/1/1-1/1/2

ip igmp snooping drop-unknown

Syntax

ip igmp snooping drop-unknown {vlan-shared | vlan-exclusive}

no ip igmp snooping drop-unknown

Description

Configures drop-unknown mode. While IGMP snooping is enabled, the traffic will be forwarded only to ports
that made an IGMP request for the multicast. Drop unknown filters ensure that packets are not forwarded
to ports that did not make a request for the traffic stream. This could either be a filter across all VLANs
(vlan-shared) or per VLAN (vlan-exclusive). The default is vlan-shared.

The no form of this command disables drop unknown on the switch.

Command context

config

Chapter 4 IGMP snooping

45

Parameters
vlan-shared

Enables shared VLAN filter on the switch. Default: vlan-shared.

vlan-exclusive

Enables exclusive drop unknown filter per VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring shared VLAN filter on the switch:

switch(config)# ip igmp snooping drop-unknown vlan-shared

Configuring exclusive drop unknown filter per VLAN:

switch(config)# ip igmp snooping drop-unknown vlan-exclusive

Disabling drop unknown on the switch:

switch(config)# no ip igmp snooping drop-unknown

ip igmp snooping fastlearn

Syntax

ip igmp snooping fastlearn <PORT-LIST>

no ip igmp snooping fastlearn <PORT-LIST>

Description

Enables the port to learn group information when receiving a topology change notification. By default, fast
learn is not enabled on ports.

The no form of this command disables fast learn on the specified ports.

Command context

config

Parameters
fastlearn <PORT-LIST>

Specifies a list of one or more ports to be configured as fast learn ports. You can specify a single port, a
comma-separated list of ports or a range of ports such as 1/1/1-1/1/3. You may also enter an L2 LAG
(1-128).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring fast learn ports:

46

AOS-CX 10.06 Multicast Guide

switch(config)# ip igmp snooping fastlearn 1/1/3
switch(config)# ip igmp snooping fastlearn 1/1/1-1/1/2
switch(config)# ip igmp snooping fastlearn 1/1/5,1/1/6

ip igmp snooping fastleave

Syntax

ip igmp snooping fastleave <PORT-LIST>

no ip igmp snooping fastleave <PORT-LIST>

Description

Enables the switch to immediately remove the IGMP client from its IGMP table and cease transmitting
multicast traffic to the client.

The no form of this command disables fastleave on the specified ports.

Command context

config-vlan

Parameters
fastleave <PORT-LIST>

Specifies a list of one or more ports to be configured as fastleave ports. You can specify a single port, a
comma-separated list of ports or a range of ports such as 1/1/1-1/1/3.

Authority

Administrators or local user group members with execution rights for this command.

Usage

IGMP fastleave is configured for ports on a per-VLAN basis. Upon receiving a Leave Group message, the
querier sends an IGMP Group-Specific Query message out of the interface to ensure that no other receivers
are connected to the interface. If receivers are directly attached to the switch, it is inefficient to send the
membership query as the receiver wanting to leave is the only connected host.

When a fastleave enabled switch port is connected to a single host and receives a leave, the switch does not
wait for the querier status update interval, but instead immediately removes the IGMP client from its IGMP
table and ceases transmitting multicast traffic to the client. (If the switch detects multiple end nodes on the
port, Fastleave does not activate regardless of whether one or more of these end nodes are IGMP clients.)
This processing speeds up the overall leave process and also eliminates the CPU overhead of having to
generate an IGMP Group-Specific Query message.

Examples

Configuring fastleave ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping fastleave 1/1/1
switch(config-vlan)# ip igmp snooping fastleave 1/1/1-1/1/2
switch(config-vlan)# ip igmp snooping fastleave 1/1/1,1/1/2-1/1/3
switch(config-vlan)# no ip igmp snooping fastleave 1/1/1
switch(config-vlan)# no ip igmp snooping fastleave 1/1/1-1/1/2

Chapter 4 IGMP snooping

47

ip igmp snooping forced fastleave

Syntax

ip igmp snooping forced-fastleave <PORT-LIST>

no ip igmp snooping forced-fastleave <PORT-LIST>

Description

Configures the specified ports in forced fastleave mode.

The no form of this command disables forced fastleave on the specified ports.

Command context

config-vlan

Parameters
fastleave <PORT-LIST>

Specifies a list of one or more ports to be configured as forced fastleave ports. You can specify a single
port, a comma-separated list of ports or a range of ports such as 1/1/1-1/1/3.

Authority

Administrators or local user group members with execution rights for this command.

Usage

With forced fastleave enabled, IGMP speeds up the process of blocking unnecessary multicast traffic to a
switch port that is connected to multiple end nodes. When a port having multiple end nodes receives a leave
group request from one end node for a given multicast group, forced fastleave activates and waits for a
second to receive a join request from any other member of the same group on that port. If the port does
not receive a join request for that group within the forced fastleave interval, the switch then blocks any
further traffic to that group on that port.

Examples

Configuring forced-fastleave ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping forced-fastleave 1/1/1
switch(config-vlan)# ip igmp snooping forced-fastleave 1/1/1-1/1/2
switch(config-vlan)# ip igmp snooping forced-fastleave 1/1/1,1/1/2-1/1/3
switch(config-vlan)# no ip igmp snooping forced-fastleave 1/1/1
switch(config-vlan)# no ip igmp snooping forced-fastleave 1/1/1-1/1/2

ip igmp snooping forward

Syntax

ip igmp snooping forward <PORT-LIST>

no ip igmp snooping forward <PORT-LIST>

Description

Configures the specified ports in forward mode. In forward mode, traffic is always forwarded on this port,
irrespective of joins.

48

AOS-CX 10.06 Multicast Guide

The no form of this command disables forward ports.

Command context

config-vlan

Parameters
forward <PORT-LIST>

Specifies a list of ports to be configured in forward mode. You can specify a single port, a comma-
separated list of ports or a range of ports such as 1/1/1-1/1/3.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring forward ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping forward 1/1/1
switch(config-vlan)# ip igmp snooping forward 1/1/1-1/1/2
switch(config-vlan)# ip igmp snooping forward 1/1/1,1/1/2-1/1/3
switch(config-vlan)# no ip igmp snooping forward 1/1/1
switch(config-vlan)# no ip igmp snooping forward 1/1/1-1/1/2

ip igmp snooping static-group

Syntax

ip igmp snooping static-group <MULTICAST-IP-ADDRESS>

no ip igmp snooping static-group <MULTICAST-IP-ADDRESS>

Description

Configures an IGMP snooping static multicast group. You can configure a maximum of 32 IGMP snooping
static groups.

The no form of this command disables static multicast group.

Command context

config-vlan

Parameters
<MULTICAST-IP-ADDRESS>

Specifies the IGMP static multicast group IP address. Format: A.B.C.D

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring IGMP snooping static group:

Chapter 4 IGMP snooping

49

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping static-group 239.1.1.1
switch(config-vlan)# no ip igmp snooping static-group 239.1.1.1

ip igmp snooping version

Syntax

ip igmp snooping version <VERSION>

Description

Configures the IGMP snooping version on the VLAN.

Command context

config-vlan

Parameters
<VERSION>

Specifies the IGMP snooping version. Select 2 for IGMPv2 (RFC2236). Select 3 for IGMPv3 (RFC3376).
Values: 2 or 3.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring IGMP snooping version on the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ip igmp snooping version 2

no ip igmp snooping

Syntax

no ip igmp snooping

Description

Disables all IGMP snooping configurations on the VLAN.

Command context

config-vlan

Authority

Administrators or local user group members with execution rights for this command.

Examples

Disabling all IGMP snooping configurations on the VLAN:

switch(config)# vlan 2
switch(config-vlan)# no ip igmp snooping

50

AOS-CX 10.06 Multicast Guide

show ip igmp snooping

Syntax

show ip igmp snooping

Description

Shows IGMP snooping configuration information and status for all VLANs.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping configuration and status:

switch# show ip igmp snooping

IGMP Snooping Protocol Info

Total VLANs with IGMP enabled             : 1
IGMP Drop Unknown Multicast               : Global

VLAN ID : 1
VLAN Name : DEFAULT_VLAN_1
IGMP Snooping is not enabled

VLAN ID : 2
VLAN Name : VLAN2
IGMP Configured Version : 3
IGMP Operating Version : 3
Querier Address [this switch] : 20.1.1.1
Querier Port :
Querier UpTime :0m 21s
Querier Expiration Time :0m 2s

show ip igmp snooping counters

Syntax

show ip igmp snooping counters

Description

Shows IGMP snooping query packet Tx, Rx, and Error packet counter details.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Chapter 4 IGMP snooping

51

Examples

Showing IGMP snooping packet counters:

switch# show ip igmp snooping counters
IGMP Snooping VLAN Counters

Rx Counters :

V1 All Hosts Queries                             0
V2 All Hosts Queries                             0
V3 All Hosts Queries                             3
V2 Group Specific Queries                        0
V3 Group Specific Queries                        0
Group And Source Specific Queries                0
V1 Member Reports                                0
V2 Member Reports                                0
V3 Member Reports                                2
V2 Member Leaves                                 0

Tx Counters :

Flood on vlan                                    44
V2 Group Specific Queries                        0
V3 Group Specific Queries                        0

Errors:

Unknown Message Type                             0
Malformed Packets                                0
Bad Checksum                                     0
Packet received on IGMP-disabled Interface       0
Interface Wrong Version Queries                  0
Packets dropped by ACL                           0

Port Counters:

Membership Timeout                               0

show ip igmp snooping groups

Syntax

show ip igmp snooping groups

Description

Shows IGMP snooping group information.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping groups:

52

AOS-CX 10.06 Multicast Guide

switch# show ip igmp snooping groups
IGMP Group Address Information

VLAN ID Group Address   Expires   UpTime    Last Reporter   Type
-----------------------------------------------------------------
2       239.1.1.3       0m 4s     0m 10s    10.1.1.1        Filter

show ip igmp snooping static-groups

Syntax

show ip igmp snooping static-groups

Description

Shows IGMP snooping static group details.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping static group details:

switch# show ip igmp snooping static-groups

IGMP Static Group Address Information

VLAN ID Group Address
------------------------
10      239.1.1.10
10      239.1.1.11

show ip igmp snooping statistics

Syntax

show ip igmp snooping statistics

Description

Shows IGMP snooping protocol information and the joined group statistics.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping statistics:

Chapter 4 IGMP snooping

53

switch# show ip igmp snooping statistics
IGMP Snooping Protocol Info

Total VLANs with IGMP enabled             : 1
IGMP Drop Unknown Multicast               : Global

IGMP Snooping Joined Groups Statistics

VLAN ID VLAN Name        Total  Static INCLUDE  EXCLUDE
------- ---------------- ------ ------ -------  -------
1       DEFAULT_VLAN_1   0      0      0        0
2       VLAN10           2      2      0        0

show ip igmp snooping vlan

Syntax

show ip igmp snooping vlan <VLAN-ID> [group [<group-ip>]
     [source <source-ip>]]

Description

Shows IGMP snooping protocol information for the specified VLAN. You can also specify a group and source
to show group and source information.

Command context

Operator (>) or Manager (#)

Parameters
<VLAN-ID>

Specifies a VLAN. Range: 1-4094.

group <group-ip>

Specifies a group to display port and group information. Format: A.B.C.D

source <source-ip>

Specifies a source to display source information for the group. Format: A.B.C.D

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping protocol information for VLAN 2:

switch# show ip igmp snooping vlan 2

IGMP Snooping Protocol Info

Total VLANs with IGMP enabled             : 1
IGMP Drop Unknown Multicast               : Global

VLAN ID : 2
VLAN Name : VLAN2
IGMP Configured Version : 3
IGMP Operating Version : 3
Querier Address : 20.1.1.1

54

AOS-CX 10.06 Multicast Guide

Querier Port : 1/1/1
Querier UpTime :
Querier Expiration Time :

Active Group Address   Tracking  Vers Mode Uptime    Expires
--------------------- ---------- ---- ---- --------- ----------
239.1.1.2              Filter    3    INC  0m 27s    0m 13s

Showing IGMP snooping group information for group 239.1.1.2 on VLAN 2:

switch# show ip igmp snooping vlan 2 group 239.1.1.2

IGMP ports and group information for group 239.1.1.2

VLAN ID   : 2
VLAN Name : VLAN2

Group Address : 239.1.1.2
Last Reporter : 10.1.1.1
Group Type    : Filter

                                        V1        V2        Sources   Sources
Port      Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
--------- ---- ---- --------- --------- --------- --------- --------- --------
1/1/6     3    INC  0m 41s    3m 39s                        3         0

Group Address  : 239.1.1.2
Source Address : 30.1.1.1
Source Type    : Filter

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/6     INC  0m 41s    3m 39s    Auto

Group Address  : 239.1.1.2
Source Address : 30.1.1.2
Source Type    : Filter

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/6     INC  0m 41s    3m 39s    Auto

Group Address  : 239.1.1.2
Source Address : 30.1.1.3
Source Type    : Filter

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/6     INC  0m 41s    3m 39s    Auto

Showing IGMP snooping group information for group 239.1.1.2 on VLAN 2 and source 30.1.1.1:

switch# show ip igmp snooping vlan 2 group 239.1.1.2 source 30.1.1.1

VLAN ID   : 2
VLAN Name : VLAN2
Group Address  : 239.1.1.2
Source Address : 30.1.1.1
Source Type    : Filter

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/6     INC  0m 41s    3m 39s    Auto

Chapter 4 IGMP snooping

55

show ip igmp snooping vlan counters

Syntax

show ip igmp snooping vlan <VLAN-ID> counters

Description

Shows IGMP snooping query packet Tx, Rx, Error packet counters for the specified VLAN.

Command context

Operator (>) or Manager (#)

Parameters
<VLAN-ID>

Specifies a VLAN. Range: 1-4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping counters for VLAN 2:

Switch# show ip igmp snooping vlan 2 counters
IGMP Snooping VLAN Counters

VLAN ID   :   2
VLAN Name : VLAN2

Rx Counters :

V1 All Hosts Queries                             0
V2 All Hosts Queries                             0
V3 All Hosts Queries                             3
V2 Group Specific Queries                        0
V3 Group Specific Queries                        0
Group And Source Specific Queries                0
V1 Member Reports                                0
V2 Member Reports                                0
V3 Member Reports                                2
V2 Member Leaves                                 0

Tx Counters :

Flood on vlan                                    71
V2 Group Specific Queries                        0
V3 Group Specific Queries                        0

Errors:

Unknown Message Type                             0
Malformed Packets                                0
Bad Checksum                                     0
Packet received on IGMP-disabled Interface       0
Interface Wrong Version Queries                  0
Packet dropped by ACL                            0

Port Counters:

56

AOS-CX 10.06 Multicast Guide

Membership Timeout                               0
Switch#

show ip igmp snooping vlan group port

Syntax

show ip igmp snooping vlan <VLAN-ID> group port
     <PORT-ID>

Description

Shows IGMP snooping group details for the specified VLAN. It shows information about all IGMP snooping
groups or sources learned on a particular port.

Command context

Operator (>) or Manager (#)

Parameters
<VLAN-ID>

Specifies a VLAN. Range: 1-4094.

<PORT-ID>

Specifies a port of a VLAN to display information about all IGMPv3 snooping groups/sources learn on a
particular port.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping group details for VLAN 2 port 1/1/6:

switch# show ip igmp snooping vlan 2 group port 1/1/6

VLAN ID   : 2
VLAN Name : VLAN2

Group Address : 239.1.1.1
Last Reporter : 10.1.1.1
Group Type    : Filter

                                        V1        V2        Sources   Sources
Port      Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked
--------- ---- ---- --------- --------- --------- --------- --------- --------
1/1/6     2    EXC  0m 21s    1m 12s              2m 48s    0         0

VLAN ID   : 2
VLAN Name : VLAN2

Group Address : 239.1.1.2
Last Reporter : 10.1.1.1
Group Type    : Filter

                                        V1        V2        Sources   Sources
Port      Vers Mode Uptime    Expires   Timer     Timer     Forwarded Blocked

Chapter 4 IGMP snooping

57

--------- ---- ---- --------- --------- --------- --------- --------- --------
1/1/6     2    EXC  0m 21s    1m 32s              2m 48s    0         0

show ip igmp snooping vlan statistics

Syntax

show ip igmp snooping vlan <VLAN-ID> statistics

Description

Shows IGMP snooping statistics details for the specified VLAN. It also shows information on the different
groups joined in the VLAN.

Command context

Operator (>) or Manager (#)

Parameters
<VLAN-ID>

Specifies a VLAN. Range: 1-4094.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing IGMP snooping statistics for VLAN 2:

switch# show ip igmp snooping vlan 2 statistics
IGMP Snooping statistics

VLAN ID   :   2
VLAN Name : VLAN2

Number of Include Groups       :   1
Number of Exclude Groups       :   0
Number of Static Groups        :   1
Total Multicast Groups Joined  :   2

58

AOS-CX 10.06 Multicast Guide

Chapter 5
MLD snooping commands

MLD snooping functionality
Multicast Listener Discovery (MLD) snooping optimizes multicast traffic across the network to prevent traffic
from flooding ports on a VLAN.

•

For example, one of the features of MLD snooping lets you configure the network so that traffic is
forwarded only to ports that initiate an MLD request for multicast.

• Another feature of MLD lets you enable a setting so that packets that do not match the configured

version are dropped.

• You can also block ports from traffic.

MLD snooping global configuration commands

[no] ipv6 mld snooping [drop-unknown [vlan-shared | vlan-
exclusive]]

Syntax

[no] ipv6 mld snooping [drop-unknown [vlan-shared | vlan-exclusive]]

Description

This command configures the drop unknown mode. While MLD snooping is enabled, the traffic will be
forwarded only to ports that initiate an MLD request for multicast. Drop unknown mode can be a filter
across all VLANs (vlan-shared) or per VLAN (exclusive-vlan). The default configuration is vlan-shared.

The no form of this command disables drop unknown mode on the switch.

Command context

config

Parameters
vlan-shared

Required: Enable shared VLAN filter on the switch.

vlan-exclusive

Required: Enable exclusive drop unknown filter per VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 5 MLD snooping commands

59

Example

switch(config)# ipv6 mld snooping drop-unknown vlan-shared
switch(config)# ipv6 mld snooping drop-unknown vlan-exclusive
switch(config)# no ipv6 mld snooping drop-unknown

MLD snooping VLAN configuration commands

ipv6 mld snooping

Syntax

ipv6 mld snooping {enable | disable}

Description

This command enables or disables MLD snooping on the VLAN.

The no form of this command disables all MLD snooping configurations on the VLAN.

Command context

config-vlan-<VLAN-ID>

Parameters
enable

Required: Enable MLD snooping on the VLAN.

disable

Required: Disable MLD snooping on the VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Example

Enable MLD snooping on VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping enable
switch(config-vlan)# ipv6 mld snooping disable

Remove all MLD snooping configurations on VLAN 2:

switch(config)# vlan 2
switch(config-vlan)# no ipv6 mld snooping

ipv6 mld snooping fastlearn

Syntax

ipv6 mld snooping fastlearn <port-list>

Description

This command enables the port to learn group information on receiving topology change notification.

The no form of this command disables fastlearn on the ports.

60

AOS-CX 10.06 Multicast Guide

Command context

config

Parameters
port-list

Required: 1/1/1-1/1/2, ports to be configured as fastlearn ports.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# ipv6 mld snooping fastlearn 1/1/3
switch(config)# ipv6 mld snooping fastlearn 1/1/1-1/1/2
switch(config)# ipv6 mld snooping fastlearn 1/1/5,1/1/6

ipv6 mld snooping fastleave

Syntax

ipv6 mld snooping fastleave <port-list>

Description

Enables the switch to immediately remove an interface from the bridge table upon receiving the leave group
message.

The no form of this command disables fastleave configuration on the ports.

Command context

config-vlan

Parameters
fastleave <PORT-LIST>

Specifies a list of one or more ports to be configured as fastleave ports. You can specify a single port, a
comma-separated list of ports or a range of ports such as 1/1/1-1/1/3.

Authority

Administrators or local user group members with execution rights for this command.

Usage

MLD fastleave is configured for ports on a per-VLAN basis. By default, the querier sends a MLD Group-
Specific Query message out of the interface, upon which the leave group message is received to ensure that
no other receivers are connected to the interface. If receivers are directly attached to the switch, it is
inefficient to send the membership query as the receiver wanting to leave is the only connected host.
Fastleave processing eliminates the MLD Group-Specific Query message. Thus, it allows the switch to
immediately remove an interface from the bridge table upon receiving the leave Group message. This
processing speeds up the overall leave process and also eliminates the CPU overhead of having to generate
an MLD Group-Specific Query message.

Example

Configure fastleave ports for the VLAN:

Chapter 5 MLD snooping commands

61

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping fastleave 1/1/1
switch(config-vlan)# ipv6 mld snooping fastleave 1/1/1-1/1/2
switch(config-vlan)# ipv6 mld snooping fastleave 1/1/1,1/1/2-1/1/3
switch(config-vlan)# no ipv6 mld snooping fastleave 1/1/1
switch(config-vlan)# no ipv6 mld snooping fastleave 1/1/1-1/1/2

ipv6 mld snooping forced fastleave

Syntax

ipv6 mld snooping forced fastleave <port-list>

Description

Configures the given ports in forced fastleave mode.

The no form of this command disables forced fastleave configuration on the ports.

Command context

config-vlan

Parameters
fastleave <PORT-LIST>

Specifies a list of one or more ports to be configured as forced fastleave ports. You can specify a single
port, a comma-separated list of ports or a range of ports such as 1/1/1-1/1/3.

Authority

Administrators or local user group members with execution rights for this command.

Usage

With forced fastleave enabled, MLD speeds up the process of blocking unnecessary multicast traffic to a
switch port that is connected to multiple end nodes. When a port having multiple end nodes receives a leave
group request from one end node for a given multicast group, forced fastleave activates and waits a small
amount of time to receive a join request from any other member of the same group on that port. If the port
does not receive a join request for that group within the forced fastleave interval, the switch then blocks any
further traffic to that group on that port.

Example

Configure forced-fastleave ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping forced-fastleave 1/1/1
switch(config-vlan)# ipv6 mld snooping forced-fastleave 1/1/1-1/1/2
switch(config-vlan)# ipv6 mld snooping forced-fastleave 1/1/1,1/1/2-1/1/3
switch(config-vlan)# no ipv6 mld snooping forced-fastleave 1/1/1
switch(config-vlan)# no ipv6 mld snooping forced-fastleave 1/1/1-1/1/2

ipv6 mld snooping [version <ver>]

Syntax

ipv6 mld snooping [version <ver>]

Description

This command configures the MLD snooping version on the VLAN. MLD version 2 is the default.

62

AOS-CX 10.06 Multicast Guide

Command context

config-vlan-<VLAN-ID>

Parameters
ver

Required: 1-2, MLD snooping version.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping version 2

ipv6 mld snooping apply access-list

Syntax

ipv6 mld snooping apply access-list <ACL-NAME>

no ipv6 mld snooping apply access-list <ACL-NAME>

Description

Configures the ACL on a particular interface to filter the MLD join or leave packets based on rules set in the
particular ACL name.

The no form of this command disables the rules set for the ACL.

NOTE: This configuration will override the ACL associated with IGMP snooping on the
corresponding L2 VLAN.

Command context

config-vlan

Parameters
access-list

Associates an ACL with the IGMP.

<ACL-NAME>

Specifies the name of the ACL.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Existing classifier commands are used to configure the ACL. In case an MLDv2 packet with multiple group
addresses is received, it will only process the permitted group addresses based on the ACL rule set, and any
existing joins will time out. If there is no match or if there is a deny rule match, the packet is dropped.

NOTE: If the access list is configured for both L2 VLAN and L3 VLAN, the L3 VLAN configuration
will be applied.

Chapter 5 MLD snooping commands

63

Examples

Configuring the ACL to filter MLD packets based on rules set in access list mygroup:

switch(config)# access-list ipv6 mygroup
switch(config-acl-ip)# permit icmpv6 any ff55::1
switch(config-acl-ip)# exit
switch(config)# interface vlan 2
switch(config-vlan)# ipv6 mld snooping apply access-list mygroup

Configuring the ACL to remove the rules set in access list mygroup:

switch(config-vlan)# no ipv6 mld snooping apply access-list mygroup

ipv6 mld snooping [auto <port-list>]

Syntax

ipv6 mld snooping [auto <port-list>]

Description

This command configures the given ports in auto mode, which is the default port mode.

Command context

config-vlan-<VLAN-ID>

Parameters
port-list

Required: 1/1/1-1/1/2, ports to be configured as auto ports.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configure auto ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping auto 1/1/1
switch(config-vlan)# ipv6 mld snooping auto 1/1/1,1/1/2-1/1/3

ipv6 mld snooping [blocked <port-list>]

Syntax

ipv6 mld snooping [blocked <port-list>]

Description

By default ports are configured in auto mode. This command configures the given ports in blocked mode.

The no form of this command removes blocked ports.

Command context

config-vlan-<VLAN-ID>

64

AOS-CX 10.06 Multicast Guide

Parameters
port-list

Required: 1/1/1-1/1/2, ports to be configured as blocked ports.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configure blocked ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping blocked 1/1/1
switch(config-vlan)# ipv6 mld snooping blocked 1/1/1-1/1/2
switch(config-vlan)# ipv6 mld snooping blocked 1/1/3,1/1/4-1/1/6
switch(config-vlan)# no ipv6 mld snooping blocked 1/1/1
switch(config-vlan)# no ipv6 mld snooping blocked 1/1/1-1/1/2

ipv6 mld snooping [forward <port-list>]

Syntax

ipv6 mld snooping [forward <port-list>]

Description

By default ports are configured in auto mode. This command configures the given ports in forward mode.

The no form of this command disables forward ports.

Command context

config-vlan-<VLAN-ID>

Parameters
port-list

Required: 1/1/1-1/1/2, ports to be configured as forward ports.

Authority

Administrators or local user group members with execution rights for this command.

Example

Configure forward ports for the VLAN:

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping forward 1/1/1
switch(config-vlan)# ipv6 mld snooping forward 1/1/1-1/1/2
switch(config-vlan)# ipv6 mld snooping forward 1/1/1,1/1/2-1/1/3
switch(config-vlan)# no ipv6 mld snooping forward 1/1/1
switch(config-vlan)# no ipv6 mld snooping forward 1/1/1-1/1/2

ipv6 mld snooping [static-group <X:X::X:X>]

Syntax

 ipv6 mld snooping [static-group <X:X::X:X>]

Chapter 5 MLD snooping commands

65

Description

This command configures static multicast group.

The no form of this command disables static multicast group.

Command context

config-vlan-<VLAN-ID>

Parameters
static-group

Required: <X:X::X:X>, MLD static multicast group.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# vlan 2
switch(config-vlan)# ipv6 mld snooping static-group ff12::c
switch(config-vlan)# no ipv6 mld snooping static-group ff12::c

MLD snooping show commands

show ipv6 mld snooping

Syntax

show ipv6 mld snooping

Description

This command shows MLD snooping configuration details for all VLANs.

Command context

Manager (#)

Parameters

None

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld snooping

MLD Snooping Protocol Info

Total VLANs with MLD enabled             : 1
Current count of multicast groups joined : 0

MLD Drop Unknown Multicast               : Global

66

AOS-CX 10.06 Multicast Guide

VLAN ID                                  : 1
VLAN Name                                : DEFAULT_VLAN_1
MLD Snooping is not enabled

VLAN ID                                  : 2
VLAN Name                                : VLAN2
MLD Configured Version                   : 2
MLD Operating Version                    : 2
Querier Address [this switch]            : fe80::218:71ff:fec4:2f00
Querier Port                             :
Querier UpTime                           :0m 21s
Querier Expiration Time                  :0m 2s

show ipv6 mld snooping [counters]

Syntax

show ipv6 mld snooping [counters]

Description

This command shows MLD snooping query packet Tx, Rx, and Error packet counter details.

Command context

Manager (#)

Parameters
counters

Optional, show MLD snooping counters.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld snooping counters
MLD Snooping VLAN Counters

Rx Counters :

V1 All Hosts Queries                             0
V2 All Hosts Queries                             0
V2 Group Specific Queries                        0
Group And Source Specific Queries                0
V1 Member Reports                                0
V2 Member Reports                                0
V1 Member Leaves                                 0

Tx Counters :

Flood on vlan                                    44
V1 Group Specific Queries                        0

Chapter 5 MLD snooping commands

67

V2 Group Specific Queries                        0

Errors:

Unknown Message Type                             0
Malformed Packets                                0
Bad Checksum                                     0
Packet received on MLD-disabled Interface        0
Interface Wrong Version Queries                  0
Packets dropped by ACL                           0

Port Counters:

Membership Timeout                               0
switch#

show ipv6 mld snooping [groups]

Syntax

show ipv6 mld snooping [groups]

Description

This command shows MLD snooping group details for the specified VLAN.

Command context

Manager (#)

Parameters
groups

Optional, show MLD snooping groups information.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld snooping groups

MLD Group Address Information

VLAN ID Group Address                           Expires   UpTime    Last Reporter                           Type
------- --------------------------------------- --------- --------- --------------------------------------- ----
10      ff12::c                                 3m 54s    0m 26s    2001::1                                 Filter
10      ff12::d                                 4m 17s    0m 3s     2001::1

show ipv6 mld snooping [statistics]

Syntax

show ipv6 mld snooping [statistics]

Description

This command shows MLD snooping statistics information.

68

AOS-CX 10.06 Multicast Guide

Command context

Manager (#)

Parameters
statistics

Optional, show MLD snooping statistics.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld snooping statistics
MLD Snooping Protocol Info

Total VLANs with MLD enabled             : 1
Current count of multicast groups joined : 2

MLD Drop Unknown Multicast               : Global

MLD Snooping Joined Groups Statistics

VLAN ID VLAN Name        Total  Static INCLUDE  EXCLUDE
------- ---------------- ------ ------ -------  -------
1       DEFAULT_VLAN_1   0      0      0        0
2       VLAN2            2      2      0        0

show ipv6 mld snooping [vlan <vlan-id> [counters]]

Syntax

show ipv6 mld snooping [vlan <vlan-id> [counters]]

Description

This command shows MLD snooping protocol information and number of different groups joined for the
VLAN.

Command context

Manager (#)

Parameters
vlan-id

Required, 1-4094, shows MLD snooping information.

counters

Optional, shows MLD query packet Tx, Rx, Error packet counters on a specified VLAN.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Chapter 5 MLD snooping commands

69

Example

switch# show ipv6 mld snooping vlan 2 counters
MLD Snooping VLAN Counters

VLAN ID   :   2
VLAN Name :   VLAN2

Rx Counters :

V1 All Hosts Queries                             0
V2 All Hosts Queries                             0
V1 Group Specific Queries                        0
V2 Group Specific Queries                        0
Group And Source Specific Queries                0
V1 Member Reports                                0
V2 Member Reports                                0
V1 Member Leaves                                 0

Tx Counters :

Flood on vlan                                    71
V1 Group Specific Queries                        0
V2 Group Specific Queries                        0

Errors:

Unknown Message Type                             0
Malformed Packets                                0
Bad Checksum                                     0
Packet received on MLD-disabled Interface        0
Interface Wrong Version Queries                  0
Packets dropped by ACL                           0

Port Counters:

Membership Timeout                               0
switch#

show ipv6 mld snooping [vlan <vlan-id> [statistics]]

Syntax

show ipv6 mld snooping [vlan <vlan-id> [statistics]]

Description

This command shows MLD snooping statistics details for the specified VLAN, including the number of
different groups joined for the VLAN.

Command context

Manager (#)

Parameters
vlan-id

Required, 1-4094, shows MLD query packet Tx, Rx, error packet counters on VLAN.

70

AOS-CX 10.06 Multicast Guide

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld snooping vlan 2 statistics
MLD Snooping statistics

VLAN ID   :   2
VLAN Name :   VLAN2

Number of Include Groups       :   1
Number of Exclude Groups       :   0
Number of Static Groups        :   1
Total Multicast Groups Joined  :   2

show ipv6 mld snooping [vlan <vlan-id> [group [<group-ip>]
[source <source-ip>]]]

Syntax

show ipv6 mld snooping [vlan <vlan-id> [group [<group-ip>] [source <source-ip>]]]

Description

This command shows MLD snooping details for the specified VLAN, including the number of different
groups joined for the VLAN.

Command context

Manager (#)

Parameters
vlan-id

Required: 1-4094, shows MLD protocol information for the specified VLAN.

group-ip

Optional: X:X::X:X, MLD source information for the specified group.

source-ip

Optional: X:X::X:X, MLD source information for the specified group.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld snooping vlan 2

MLD Snooping Protocol Info

Total VLANs with MLD enabled             : 2
Current count of multicast groups joined : 0

Chapter 5 MLD snooping commands

71

MLD Drop Unknown Multicast               : Global

VLAN ID                                  : 2
VLAN Name                                : VLAN2
MLD Configured Version                   : 2
MLD Operating Version                    : 2
Querier Address [this switch]            : fe80::218:71ff:fec4:2f00
Querier Port                             :
Querier UpTime                           :0m 21s
Querier Expiration Time                  :0m 2s

Active Group Address                         Tracking Vers Mode  Uptime    Expires
------------------------------------------- --------- ---- ----- --------- ---------
ff05::2:1                                    Filter    2    EXC  0m 17s    4m 3s

switch# show ipv6 mld snooping vlan 2 group

MLD ports and group information for group ff05::2:1

VLAN ID                                  : 2
VLAN Name                                : VLAN2

Group Address                            : ff05::2:1
Last Reporter                            : 2001::1
Group Type                               : Filter

                                        V1        Sources   Sources
Port      Vers Mode Uptime    Expires   Timer     Forwarded Blocked
--------- ---- ---- --------- --------- --------- --------- --------
1/1/1     2    EXC  0m 5s     4m 15s    4m 15s    0         0

switch# show ipv6 mld snooping vlan 2 group ff05::2:1

MLD ports and group information for group ff05::2:1

VLAN ID                                  : 2
VLAN Name                                : VLAN2

Group Address                            : ff05::2:1
Last Reporter                            : 2001::1
Group Type                               : Filter

                                        V1        Sources   Sources
Port      Vers Mode Uptime    Expires   Timer     Forwarded Blocked
--------- ---- ---- --------- --------- --------- --------- --------
1/1/1     2    EXC  0m 5s     4m 15s    4m 15s    0         0

switch# show ipv mld snooping vlan 2 group ff05::2:1 source 3000::3

VLAN ID                                 : 2
VLAN Name                               : VLAN2
Group Address                           : ff05::2:1
Source Address                          : 3000::3
Source Type                             : Filter

72

AOS-CX 10.06 Multicast Guide

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/1     INC  0m 27s    3m 53s    Auto

show ipv6 mld snooping [vlan <vlan-id> [group [port
<port_id>]]

Syntax

show ipv6 mld snooping [vlan <vlan-id> [group [port <port_id>]]

Description

This command shows MLD snooping details for the specified VLAN, including the number of different
groups joined for the VLAN.

Command context

Manager (#)

Parameters
port-id

Required: <PORT>, shows MLD protocol information for the specified port of a VLAN.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv mld snooping vlan 2 group port 1/1/1

VLAN ID   : 2
VLAN Name : VLAN2

Group Address : ff05::2:1
Last Reporter : fe80::1
Group Type    : Filter

                                        V1        Sources   Sources
Port      Vers Mode Uptime    Expires   Timer     Forwarded Blocked
--------- ---- ---- --------- --------- --------- --------- --------
1/1/1     2    INC  1m 46s    2m 34s              3         0

Group Address  : ff05::2:1
Source Address : 3000::1
Source Type    : Filter

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/1     INC  1m 46s    2m 34s    Auto

Group Address  : ff05::2:1
Source Address : 3000::2

Chapter 5 MLD snooping commands

73

Source Type    : Filter

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/1     INC  1m 46s    2m 34s    Auto

Group Address  : ff05::2:1
Source Address : 3000::3
Source Type    : Filter

Port      Mode Uptime    Expires   Configured Mode
--------- ---- --------- --------- ----------------
1/1/1     INC  1m 46s    2m 34s    Auto

show ipv6 mld snooping [static-groups]

Syntax

show ipv6 mld snooping [static-groups]

Description

This command shows MLD snooping static group details, including the number of static groups joined.

Command context

Manager (#)

Parameters

None

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld snooping static-groups

MLD Static Group Address Information

VLAN ID Group Address
------- ----------------------------------------
10      ff12::1
10      ff12::2

MLD configuration commands for interface VLAN

ipv6 mld {enable | disable}

Syntax

ipv6 mld {enable | disable}

74

AOS-CX 10.06 Multicast Guide

Description

This command enables or disables MLD on the interface VLAN.

Command context

config-if-vlan

Parameters
enable

Required: Enable MLD on the interface VLAN.

disable

Required: Disable MLD on the interface VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld enable
switch(config-if-vlan)# ipv6 mld disable

ipv6 mld apply access-list

Syntax

ipv6 mld apply access-list <ACL-NAME>

no ipv6 mld apply access-list <ACL-NAME>

Description

Configures the ACL on a particular interface to filter the MLD join or leave packets based on rules set in the
particular ACL name.

The no form of this command disables the rules set for the ACL.

Command context

config-vlan

Parameters
access-list

Associates an ACL with the IGMP.

<ACL-NAME>

Specifies the name of the ACL.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Existing classifier commands are used to configure the ACL. In case an MLDv2 packet with multiple group
addresses is received, it will only process the permitted group addresses based on the ACL rule set, and any
existing joins will time out. If there is no match or if there is a deny rule match, the packet is dropped.

Chapter 5 MLD snooping commands

75

Examples

Configuring the ACL to filter MLD packets based on rules set in access list mygroup:

switch(config)# access-list ipv6 mygroup
switch(config-acl-ip)# permit icmpv6 any ff55::1
switch(config-acl-ip)# exit
switch(config)# interface vlan 2
switch(config-vlan)# ipv6 mld apply access-list mygroup

Configuring the ACL to remove the rules set in access list mygroup:

switch(config-vlan)# no ipv6 mld apply access-list mygroup

no ipv6 mld

Syntax

no ipv6 mld

Description

This command removes all MLD configurations on the interface.

Authority

Administrators or local user group members with execution rights for this command.

Parameters

None

Command context

config-if

Example

switch(config)# interface vlan 1
switch(config-if)# no ipv6 mld

ipv6 mld querier

Syntax

ipv6 mld querier

Description

This command configures MLD querier.

The no form of this command disables MLD querier.

Command context

config-if-vlan

Parameters

None

76

AOS-CX 10.06 Multicast Guide

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld querier
switch(config-if-vlan)# no ipv6 mld querier

ipv6 mld querier [interval <interval-value>]

Syntax

ipv6 mld querier [interval <interval-value>]

Description

This command configures MLD querier interval. The default interval-value is 125.

Command context

config-if-vlan

Parameters
interval-value

Required: 5-300, configures MLD querier interval.

NOTE: Default interval-value is 125. Use the no ipv6 mld querier interval command to
set interval-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld querier interval 100
switch(config-if-vlan)# no ipv6 mld querier interval

ipv6 mld last-member-query-interval <interval-value>

Syntax

ipv6 mld last-member-query-interval <interval-value>

Description

This command configures MLD last member query interval value in seconds. The default interval-value is 1
second.

Command context

config-if-vlan

Chapter 5 MLD snooping commands

77

Parameters
interval-value

Required: 1-2, configures MLD last-member-query-interval.

NOTE: Default interval-value is 1 second. Use the no ipv6 mld last-member-query-
interval command to set interval-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld last-member-query-interval 2
switch(config-if-vlan)# no ipv6 mld last-member-query-interval

ipv6 mld querier query-max-response-time <response-time>

Syntax

ipv6 mld querier query-max-response-time <response-time>

Description

This command configures MLD max response time value in seconds. The default max-response-time-value
is 10 seconds.

Command context

config-if-vlan

Parameters
max-response-time-value

Required: 10-128, configures MLD querier max-response-time.

NOTE: Default max-response-time-value is 10 seconds. Use the no ipv6 mld querier
query-max-response-time command to set max-response-time-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld query-max-response-time 50
switch(config-if-vlan)# no ipv6 mld query-max-response-time

ipv6 mld robustness

Syntax

ipv6 mld robustness <value>

78

AOS-CX 10.06 Multicast Guide

Description

This command configures MLD robustness. The robustness value represents the number of times the
querier retries queries on the connected subnets. The default robustness-value is 2 seconds.

Command context

config-if-vlan

Parameters
robustness-value

Required: 1-7, configures MLD robustness.

NOTE: Default robustness-value is 2 seconds. Use the no ipv6 mld robustness command to
set robustness-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld robustness 5
switch(config-if-vlan)# no ipv6 mld robustness

ipv6 mld static-group <multicast-group-ip>

Syntax

ipv6 mld static-group <multicast-group-ip>

Description

This command configures MLD static group.

Command context

config-if-vlan

Parameters
multicast-group-ip

Required: X:X::X:X, configures MLD static group.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld static-group ff12::c
switch(config-if-vlan)# no ipv6 mld static-group ff12::c

Chapter 5 MLD snooping commands

79

ipv6 mld version <version>

Syntax

ipv6 mld version <version>

Description

This command configures MLD version.

Command context

config-if-vlan

Parameters
version

Required: 1-2, configures MLD version.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld version 2

ipv6 mld version <version> [strict]

Syntax

ipv6 mld version <version> [strict]

Description

This command configures MLD strict version. Packets that do not match the configured version will be
dropped. By default, strict option is not enabled.

Command context

config-if-vlan

Parameters
version

Required: 1-2, configures MLD version.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 2
switch(config-if-vlan)# ipv6 mld version 2 strict
switch(config-if-vlan)# no ipv6 mld version 2 strict

80

AOS-CX 10.06 Multicast Guide

MLD show commands for interface VLAN

show ipv6 mld

Syntax

show ipv6 mld

Description

This command shows MLD configuration on VLAN.

Command context

Manager (#)

Parameters

None

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld

VRF Name                   : default
Interface                  : vlan10
MLD Configured Version     : 2
MLD Operating Version      : 2
Querier State              : Querier
Querier IP [this switch]   : fe80::7272:cfff:fe96:d3ec
Querier Uptime             : 39m 44s
Querier Expiration Time    : 0m 31s
MLD Snoop Enabled on VLAN  : True

show ipv6 mld [interface <intf_id> | vlan <vlan-id>]

Syntax

show ipv6 mld [interface <intf_id> | vlan <vlan-id>]

Description

This command shows MLD configuration on a specific VLAN.

Command context

Manager (#)

Parameters
vlan-id

Required: 1-4094, shows MLD configuration on a specified VLAN.

Chapter 5 MLD snooping commands

81

intf-id

Required: IFNAME, shows MLD configuration on a specified interface.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld interface vlan 10

MLD Configured Version   : 2
MLD Operating Version    : 2
Querier State              : Querier
Querier IP [this switch]   : fe80::7272:cfff:fe96:d3ec
Querier Uptime             : 40m 42s
Querier Expiration Time    : 1m 39s
MLD Snoop Enabled on VLAN  : True

switch# show ipv6 mld interface 1/1/2

MLD Configured Version   : 2
MLD Operating Version    : 2
Querier State              : Querier
Querier IP [this switch]   : fe80::7272:cfff:fe96:d3ec
Querier Uptime             : 40m 42s
Querier Expiration Time    : 1m 39s
MLD Snoop Enabled on VLAN  : True

show ipv6 mld [all-vrfs ]

Syntax

show ipv6 mld [all-vrfs ]

Description

This command shows MLD information for the specified VRF.

Command context

Manager (#)

Parameters
all-vrfs

Optional: shows MLD information status for all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch(config)# show ipv6 mld all-vrfs
VRF Name   : default
Interface  : vlan2

82

AOS-CX 10.06 Multicast Guide

MLD Configured Version   : 2
MLD Operating Version    : 2
Querier State              : Querier
Querier IP [this switch]   : fe80::a00:9ff:fe06:67cd
Querier Uptime             : 23m 53s
Querier Expiration Time    : 0m 17s
MLD Snoop Enabled on VLAN  : True

Active Group Address                         Vers Mode Uptime    Expires
-------------------------------------------- ---- ---- --------- ---------
ff05::2:1                                    2    INC  3m 56s    1m 47s

show ipv6 mld [interface <intf-id> | vlan <vlan-id>]
[counters]]

Syntax

show ipv6 mld [interface <intf-id> | vlan <vlan-id>] [counters]]

Description

This command shows MLD query packet Tx and Rx on a specific VLAN.

Command context

Manager (#)

Parameters
vlan-id

Required: 1-4094, shows MLD configuration on a specified VLAN.

intf-id

Required: IFNAME, shows MLD configuration on a specified interface.

counters

Optional: Shows MLD query packet counter Tx-Rx on a specified VLAN.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld interface vlan 2 counters

MLD Counters

Interface Name      : vlan2
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------
V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             0
V1 Group Specific Queries                    0             0
V2 Group Specific Queries                    0             2

Chapter 5 MLD snooping commands

83

Group And Source Specific Queries            0             2
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A
V1 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

switch# show ipv6 mld interface 1/1/1 counters

MLD Counters

Interface Name      : 1/1/1
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------
V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             0
V1 Group Specific Queries                    0             0
V2 Group Specific Queries                    0             0
Group And Source Specific Queries            0             0
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A
V1 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

show ipv6 mld [interface <intf-id> | vlan <vlan-id>]
[groups]]

Syntax

show ipv6 mld [interface <intf-id> | vlan <vlan-id>] [groups]]

Description

This command shows MLD groups joined details.

Command context

Manager (#)

Parameters
vlan-id

Required: 1-4094, shows MLD information on a specified VLAN.

intf-id

Required: IFNAME, shows MLD information on a specified interface.

groups

Optional: Shows MLD groups information on a specified interface.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

84

AOS-CX 10.06 Multicast Guide

Example

switch# show ipv mld interface vlan 2 groups

MLD group information for group ff05::2:1

Interface Name   : vlan2
VRF Name         : default

Group Address    : ff05::2:1
Last Reporter    : fe80::1

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
2    INC  6m 2s     0m 4s               1

Group Address  : ff05::2:1
Source Address : 3000::1

Mode Uptime    Expire
---- -------- --------
INC  6m 2s     0m 4s

show ipv6 mld [interface (<intf-id> | vlan <vlan-id>)
[group <group_ip>] [source <source_ip>]]]]

Syntax

show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group <group_ip>] [source <source_ip>]]]]

Description

This command shows MLD joined group details on a specified interface.

Command context

Manager (#)

Parameters
group_ip

Required: X:X::X:X, shows MLD joined group details.

source_ip

Required: X:X::X:X, shows MLD joined group details for a specified source.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv mld interface vlan 2 group ff55::5

MLD group information for group ff55::5

Interface Name   : vlan2

Chapter 5 MLD snooping commands

85

VRF Name         : default

Group Address    : ff55::5
Last Reporter    : fe80::1

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
2    INC  6m 2s     0m 4s               1

Group Address    : ff55::5
Source Address   : 3000::1

Mode Uptime    Expire
---- -------- --------
INC  6m 2s     0m 4s

switch# show ipv mld interface vlan 2 group ff55::5 source 3000::1

Interface Name   : vlan2
VRF Name         : default
Group Address    : ff55::5
Source Address   : 3000::1

Mode Uptime    Expire
---- -------- --------
INC  9m 37s    2m 0s

show ipv6 mld [groups]

Syntax

show ipv6 mld [groups]

Description

This command shows MLD groups joined details.

Command context

Manager (#)

Parameters
groups

Options: shows MLD groups information.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld groups

MLD group information for group ff05::2:11

Interface Name   : vlan2

86

AOS-CX 10.06 Multicast Guide

VRF Name         : default

Group Address    : ff05::2:11
Last Reporter    : 2001::1

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
1         2m 27s    1m 53s    1m 53s

MLD group information for group ff05::2:12

Interface Name   : vlan2
VRF Name         : default

Group Address    : ff05::2:12
Last Reporter    : 2001::1

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
1         0m 3s     4m 18s    4m 18s

show ipv6 mld groups [all-vrfs]

Syntax

show ipv6 mld groups [all-vrfs]

Description

This command shows MLD groups joined details on VRFs.

Command context

Manager (#)

Parameters
all-vrfs

Optional: shows MLD groups joined in all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld groups all-vrfs

MLD group information for group ff05::2:11

Interface Name   : vlan1
VRF Name         : default

Group Address    : ff05::2:11
Last Reporter    : 2001::1

                              V1        Sources   Sources

Chapter 5 MLD snooping commands

87

Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
1         4m 4s     2m 38s    2m 38s

switch# show ipv6 mld groups vrf default

MLD group information for group ff05::2:11

Interface Name   : vlan2
VRF Name         : default

Group Address    : ff05::2:11
Last Reporter    : 2001::1

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
1         5m 25s    1m 17s    1m 17s

show ipv6 mld [interface <intf-id> [counters]]

Syntax

show ipv6 mld [interface <intf-id> [counters]]

Description

This command shows MLD query packet Tx and Rx on a specific interface.

Command context

Manager (#)

Parameters
intf-id

Required: shows MLD configuration on a specified interface.

counters

Optional: shows MLD query packet counter Tx-Rx on a specified interface.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld interface 1/1/1 counters

MLD Counters

Interface Name      : 1/1/1
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------
V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             9
V1 Group Specific Queries                    0             0
V2 Group Specific Queries                    0             0

88

AOS-CX 10.06 Multicast Guide

Group And Source Specific Queries            0             0
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A
V1 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

show ipv6 mld [interface <intf-id> [statistics]]

Syntax

show ipv6 mld [interface <intf-id> [statistics]]

Description

This command shows MLD statistics on a specific interface.

Command context

Manager (#)

Parameters
intf-id

Required: shows MLD statistics on a specified interface.

statistics

Optional: shows MLD statistics on a specified interface.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld interface 1/1/1 statistics

MLD statistics

Interface Name : 1/1/1
VRF Name       : default

Number of Include Groups       :   2
Number of Exclude Groups       :   0
Number of Static Groups        :   0
Total Multicast Groups Joined  :   2

show ipv6 mld [interface <intf-id> [groups]]

Syntax

show ipv6 mld [interface <intf-id> [groups]]

Description

This command shows MLD groups joined details.

Command context

Manager (#)

Chapter 5 MLD snooping commands

89

Parameters
intf-id

Required: shows MLD configuration on a specified interface.

groups

Optional: shows MLD groups information.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld interface 1/1/1 groups

MLD group information for group ff55::1

Interface Name   : 1/1/1
VRF Name         : default

Group Address    : ff55::1
Last Reporter    : fe80::a00:9ff:fe77:1062

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
2    EXC  0m 14s    4m 6s

show ipv6 mld [interface (<intf-id> | vlan <vlan-id>)
[group <group_ip>] [source <source_ip>]]]]

Syntax

show ipv6 mld [interface (<intf-id> | vlan <vlan-id>) [group <group_ip>] [source <source_ip>]]]]

Description

This command shows MLD joined group details on a specified interface.

Command context

Manager (#)

Parameters
group_ip

Required: X:X::X:X, shows MLD joined group details.

source_ip

Required: X:X::X:X, shows MLD joined group details for a specified source.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

90

AOS-CX 10.06 Multicast Guide

Example

switch# show ipv mld interface vlan 2 group ff55::5

MLD group information for group ff55::5

Interface Name   : vlan2
VRF Name         : default

Group Address    : ff55::5
Last Reporter    : fe80::1

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
2    INC  6m 2s     0m 4s               1

Group Address    : ff55::5
Source Address   : 3000::1

Mode Uptime    Expire
---- -------- --------
INC  6m 2s     0m 4s

switch# show ipv mld interface vlan 2 group ff55::5 source 3000::1

Interface Name   : vlan2
VRF Name         : default
Group Address    : ff55::5
Source Address   : 3000::1

Mode Uptime    Expire
---- -------- --------
INC  9m 37s    2m 0s

show ipv6 mld [group <group_ip> [all-vrfs]]

Syntax

show ipv6 mld [group <group_ip> [all-vrfs]]

Description

This command shows MLD joined group details on VRF.

Command context

Manager (#)

Parameters
group_ip

Required: X:X::X:X, shows MLD joined group details.

all-vrfs

Optional: shows MLD groups joined in all VRFs.

Chapter 5 MLD snooping commands

91

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld group ff55::1

MLD group information for group ff55::1

Interface Name   : 1/1/1
VRF Name         : default

Group Address    : ff55::1
Last Reporter    : fe80::a00:9ff:fe77:1062

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
2    EXC  3m 12s    3m 46s

switch# show ipv6 mld group ff05::2:11 all-vrfs

MLD group information for group ff05::2:11

Interface Name   : vlan2
VRF Name         : default

Group Address    : ff05::2:11
Last Reporter    : 2001::1

                              V1        Sources   Sources
Vers Mode Uptime    Expires   Timer     Forwarded Blocked
---- ---- --------- --------- --------- --------- --------
1         1m 16s    3m 4s     3m 4s

show ipv6 mld [group <group_ip> [source <source_ip> [all-
vrfs]]]

Syntax

show ipv6 mld [group <group_ip> [source <source_ip> [all-vrfs]]]

Description

This command shows MLD joined group details for a source on VRF.

Command context

Manager (#)

Parameters
group_ip

Required: X:X::X:X, shows MLD joined group details.

source_ip

Required: X:X::X:X, shows MLD joined group details for a source.

92

AOS-CX 10.06 Multicast Guide

all-vrfs

Optional: shows MLD groups joined in all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld group ff05::2:1 source 3000::1

Interface Name  : vlan2
VRF Name  : default
Group Address  : ff05::2:1
Source Address : 3000::1

Mode Uptime    Expire
---- -------- --------
INC  0m 53s    3m 27s

switch# show ipv6 mld group ff05::2:1 source 3000::1 all-vrfs

Interface Name  : vlan2
VRF Name  : default
Group Address  : ff05::2:1
Source Address : 3000::1

Mode Uptime    Expire
---- -------- --------
INC  1m 38s    4m 5s

show ipv6 mld [interface vlan <vlan-id> [statistics]]

Syntax

show ipv6 mld [interface vlan <vlan-id> [statistics]]

Description

This command shows MLD statistics on a specific interface VLAN.

Command context

Manager (#)

Parameters
vlan-id

Required: 1-4094, shows MLD information on a specified VLAN.

statistics

Optional: shows MLD query packet Tx, Rx, Error packet counters on a specified VLAN.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Chapter 5 MLD snooping commands

93

Example

switch# show ipv6 mld interface vlan 2  statistics

MLD statistics

Interface Name : vlan2
VRF Name       : default

Number of Include Groups       :   2
Number of Exclude Groups       :   0
Number of Static Groups        :   0
Total Multicast Groups Joined  :   2

show ipv6 mld [static-groups [all-vrfs]]

Syntax

show ipv6 mld [static-groups [all-vrfs]]

Description

This command shows MLD static groups.

Command context

Manager (#)

Parameters
all-vrfs

Optional: shows MLD groups joined in all VRFs.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld static-groups

MLD Static Group Address Information

VRF Name   :default
Interface Name   Group Address
--------------- -----------------------------------------
vlan2           ff12::c
vlan2           ff12::d

switch# show ipv6 mld static-groups all-vrfs

MLD Static Group Address Information

VRF Name   :default
Interface Name   Group Address
--------------- -----------------------------------------
vlan2           ff12::c
vlan2           ff12::d

94

AOS-CX 10.06 Multicast Guide

show ipv6 mld counters

Syntax

show ipv6 mld [counters]

Description

This command shows MLD counters.

Command context

Manager (#)

Parameters
vrf

Optional: shows MLD counter status in a specific VRF.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show ipv6 mld counters

MLD Counters

Interface Name      : vlan2
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------
V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             12
V1 Group Specific Queries                    0             0
V2 Group Specific Queries                    0             0
Group And Source Specific Queries            0             0
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A
V1 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

switch# show ipv6 mld counters vrf default

MLD Counters

Interface Name      : vlan2
VRF Name            : default
Membership Timeout  : 0
                                             Rx            Tx
                                             ------------- -------------
V1 All Hosts Queries                         0             0
V2 All Hosts Queries                         0             12
V1 Group Specific Queries                    0             0
V2 Group Specific Queries                    0             0
Group And Source Specific Queries            0             0
V2 Member Reports                            0             N/A
V1 Member Reports                            0             N/A

Chapter 5 MLD snooping commands

95

V1 Member Leaves                             0             N/A
Packets dropped by ACL                       0             N/A

MLD configuration commands for interface

ipv6 mld {enable | disable}

Syntax

ipv6 mld {enable | disable}

Description

This command enables or disables MLD on the interface.

Command context

config-if

Parameters
enable

Required: Enable MLD on the interface.

disable

Required: Disable MLD on the interface.

x

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld enable
switch(config-if)# ipv6 mld disable

ipv6 mld apply access-list

Syntax

ipv6 mld apply access-list <ACL-NAME>

no ipv6 mld apply access-list <ACL-NAME>

Description

Configures the ACL on a particular interface to filter the MLD join or leave packets based on rules set in the
particular ACL name.

The no form of this command removes the rules set for the ACL.

Command context

config-vlan

96

AOS-CX 10.06 Multicast Guide

Parameters
access-list

Associates an ACL with the IGMP.

<ACL-NAME>

Specifies the name of the ACL.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Existing classifier commands are used to configure the ACL. In case an MLDv2 packet with multiple group
addresses is received, it will only process the permitted group addresses based on the ACL rule set, and any
existing joins will time out. If there is no match or if there is a deny rule match, the packet is dropped.

Examples

Configuring the ACL to filter MLD packets based on rules set in access list mygroup:

switch(config)# access-list ipv6 mygroup
switch(config-acl-ip)# permit icmpv6 any ff55::1
switch(config-acl-ip)# exit
switch(config)# interface vlan 1
switch(config-vlan)# ipv6 mld apply access-list mygroup

Configuring the ACL to remove the rules set in access list mygroup:

switch(config-vlan)# no ipv6 mld apply access-list mygroup

no ipv6 mld

Syntax

no ipv6 mld

Description

This command removes all MLD configurations on the interface.

Authority

Administrators or local user group members with execution rights for this command.

Parameters

None

Command context

config-if

Example

switch(config)# interface vlan 1
switch(config-if)# no ipv6 mld

Chapter 5 MLD snooping commands

97

ipv6 mld querier

Syntax

ipv6 mld querier

Description

This command configures MLD querier. This functionality will allow the interface to join in the querier-
election process.

Command context

config-if

Parameters

None

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld querier
switch(config-if)# no ipv6 mld querier

ipv6 mld querier [interval <interval-value>]

Syntax

ipv6 mld querier [interval <interval-value>]

Description

This command configures MLD querier interval. The default interval-value is 125.

Command context

config-if

Parameters
interval-value

Required: 5-300, configures MLD querier interval.

NOTE: Default interval-value is 125. Use the no ipv6 mld querier interval command to
set interval-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld querier interval 100
switch(config-if)# no ipv6 mld querier interval

98

AOS-CX 10.06 Multicast Guide

ipv6 mld last-member-query-interval

Syntax

ipv6 mld last-member-query-interval <interval-value>

Description

This command configures MLD last member query interval value in seconds. The default interval-value is 1
second.

Command context

config-if

Parameters
interval-value

Required: 1-2, configures MLD last-member-query-interval.

NOTE: Default interval-value is 1 second. Use the no ipv6 mld last-member-query-
interval command to set interval-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld last-member-query-interval 2
switch(config-if)# no ipv6 mld last-member-query-interval

ipv6 mld querier query-max-response-time

Syntax

ipv6 mld querier query-max-response-time <response-time>

Description

This command configures MLD max response time value in seconds. The default max-response-time-value
is 10 seconds.

Command context

config-if

Parameters
max-response-time-value

Required: 10-128, configures MLD querier max-response-time.

NOTE: Default max-response-time-value is 10 seconds. Use the no ipv6 mld querier
query-max-response-time command to set max-response-time-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 5 MLD snooping commands

99

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld query-max-response-time 50
switch(config-if)# no ipv6 mld query-max-response-time

ipv6 mld robustness

Syntax

ipv6 mld robustness <value>

Description

This command configures MLD robustness. The robustness value represents the number of times the
querier retries queries on the connected subnets. The default robustness-value is 2 seconds.

Command context

config-if

Parameters
robustness-value

Required: 1-7, configures MLD robustness.

NOTE: Default robustness-value is 2 seconds. Use the no ipv6 mld robustness command to
set robustness-value to the default.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld robustness 5
switch(config-if)# no ipv6 mld robustness

ipv6 mld static-group

Syntax

ipv6 mld static-group <multicast-group-ip>

Description

This command configures MLD static group.

Command context

config-if

Parameters
multicast-group-ip

Required: X:X::X:X, configures MLD static group.

100

AOS-CX 10.06 Multicast Guide

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld static-group ff12::c
switch(config-if)# no ipv6 mld static-group ff12::c

ipv6 mld version

Syntax

ipv6 mld version <version>

Description

This command configures MLD version.

Command context

config-if

Parameters
version

Required: 1-2, configures MLD version.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld version 2

ipv6 mld version [strict]

Syntax

ipv6 mld version <version> [strict]

Description

This command configures MLD strict version. Packets that do not match the configured version will be
dropped. By default, strict option is not enabled.

Command context

config-if

Parameters
version

Required: 1-2, configures MLD version.

Authority

Administrators or local user group members with execution rights for this command.

Chapter 5 MLD snooping commands

101

Example

switch(config)# interface vlan 1
switch(config-if)# ipv6 mld version 2 strict
switch(config-if)# no ipv6 mld version 2 strict

102

AOS-CX 10.06 Multicast Guide

Chapter 6
Support and other resources

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

• Technical support registration number (if applicable)

• Product name, model or version, and serial number

• Operating system name and version

•

Firmware version

• Error messages

• Product-specific reports and logs

• Add-on products or components

• Third-party products or components

Other useful sites

Other websites that can be used to find information:

Airheads social forums and
Knowledge Base

https://community.arubanetworks.com/

Software licensing

https://lms.arubanetworks.com/

End-of-Life information

https://www.arubanetworks.com/support-services/end-of-life/

Aruba software and
documentation

https://asp.arubanetworks.com/downloads

Accessing updates
To download product updates:

Chapter 6 Support and other resources

103

Aruba Support Portal

https://asp.arubanetworks.com/downloads

If you are unable to find your product in the Aruba Support Portal, you may need to search My Networking,
where older networking products can be found:

My Networking

https://www.hpe.com/networking/support

To view and update your entitlements, and to link your contracts and warranties with your profile, go to the
Hewlett Packard Enterprise Support Center More Information on Access to Support Materials page:

https://support.hpe.com/portal/site/hpsc/aae/home/

IMPORTANT: Access to some updates might require product entitlement when accessed
through the Hewlett Packard Enterprise Support Center. You must have an HP Passport set up
with relevant entitlements.

Some software products provide a mechanism for accessing software updates through the product
interface. Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://asp.arubanetworks.com/notifications/subscriptions (requires an active Aruba Support Portal
(ASP) account to manage subscriptions). Security notices are viewable without an ASP account.

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

104

AOS-CX 10.06 Multicast Guide

