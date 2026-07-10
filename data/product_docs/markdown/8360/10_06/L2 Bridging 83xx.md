AOS-CX 10.06 Layer 2 Bridging Guide
8320, 8325, 8360 Switch Series

Part Number: 5200-7735
Published: November 2020
Edition: 1

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

Acknowledgments

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of Intel
Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in the
United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

Contents

Chapter 1 About this document...................................................................... 7
Applicable products........................................................................................................................................7
Latest version available online......................................................................................................................7
Command syntax notation conventions..................................................................................................... 7
About the examples....................................................................................................................................... 8
Identifying switch ports and interfaces .......................................................................................................9

Chapter 2 Introduction.................................................................................... 10

Chapter 3 MAC address table......................................................................... 11
MAC address table commands................................................................................................................... 12
clear mac-address...................................................................................................................... 12
mac-address-table age-time.................................................................................................. 13
mac-lockout.................................................................................................................................... 13
show mac-address-table........................................................................................................... 14
show mac-address-table address......................................................................................... 15
show mac-address-table count..............................................................................................16
show mac-address-table dynamic......................................................................................... 17
show mac-address-table lockout......................................................................................... 18
show mac-address-table port................................................................................................ 18
show mac-address-table static........................................................................................... 19
show mac-address-table vlan................................................................................................ 20
static-mac...................................................................................................................................... 20

Chapter 4 VLANs............................................................................................... 22
VLAN interfaces............................................................................................................................................ 22
Access interface.................................................................................................................................22
Trunk interface.................................................................................................................................. 23
Traffic handling summary................................................................................................................ 24
Comparing VLAN commands on PVOS, Comware, and AOS-CX................................................. 25
VLAN numbering.......................................................................................................................................... 26
Configuring VLANs........................................................................................................................................27
Creating and enabling a VLAN......................................................................................................... 27
Disabling a VLAN............................................................................................................................... 27
Assigning a VLAN to an interface.................................................................................................... 27
Assigning a VLAN ID to an access interface........................................................................ 27
Assigning a VLAN ID to a trunk interface............................................................................ 28
Assigning a native VLAN ID to a trunk interface.................................................................29
Viewing VLAN configuration information....................................................................................... 30
VLAN scenario............................................................................................................................................... 31
VLAN commands.......................................................................................................................................... 35
description.................................................................................................................................... 35
name....................................................................................................................................................36
show capacities svi-count.................................................................................................... 36
show system internal-vlan-range....................................................................................... 37
show vlan........................................................................................................................................ 37

Contents

3

show vlan port............................................................................................................................. 38
show vlan summary...................................................................................................................... 39
show vlan translation............................................................................................................. 39
shutdown...........................................................................................................................................40
system internal-vlan-range.................................................................................................. 41
system vlan-client-presence-detect................................................................................ 42
vlan....................................................................................................................................................42
vlan access.................................................................................................................................... 43
vlan translate............................................................................................................................. 44
vlan trunk allowed.................................................................................................................... 45
vlan trunk native...................................................................................................................... 46
vlan trunk native tag............................................................................................................. 47
voice..................................................................................................................................................48

Chapter 5 Loop protection..............................................................................49
Interaction with other protocols.................................................................................................................50
Configuring loop protection........................................................................................................................50
Loop protect commands............................................................................................................................. 51
loop-protect..................................................................................................................................51
loop-protect action.................................................................................................................. 52
loop-protect re-enable-timer..............................................................................................53
loop-protect transmit-interval ....................................................................................... 53
loop-protect trap loop-detected....................................................................................... 54
loop-protect vlan...................................................................................................................... 55
show loop-protect...................................................................................................................... 55

Chapter 6 Spanning tree protocols............................................................... 57
Comparing spanning tree options............................................................................................................. 57
Preparing for spanning tree configuration................................................................................................57
STP..................................................................................................................................................................58
STP protocol packets........................................................................................................................ 58
STP key concepts............................................................................................................................... 59
Root bridge............................................................................................................................. 59
Root port................................................................................................................................. 59
Designated bridge and designated port............................................................................. 59
Path cost ................................................................................................................................ 60
STP timers............................................................................................................................... 60
BPDU forwarding mechanism.............................................................................................. 61
STP calculation...................................................................................................................................61
Simplified calculation overview............................................................................................ 61
Calculation example.............................................................................................................. 62
RPVST+........................................................................................................................................................... 68
Configuring RPVST+.......................................................................................................................... 70
Viewing RPVST+ information........................................................................................................... 72
RPVST+ scenario................................................................................................................................ 73
RPVST+ commands........................................................................................................................... 75
show spanning-tree......................................................................................................... 75
show spanning-tree inconsistent-ports.............................................................. 77
show spanning-tree summary port............................................................................78
show spanning-tree summary root............................................................................78
show spanning-tree vlan..............................................................................................79
spanning-tree bpdu-guard timeout......................................................................... 80
spanning-tree extend-system-id.............................................................................. 81

4

AOS-CX 10.06 Layer 2 Bridging Guide

spanning-tree ignore-pvid-inconsistency..........................................................82
spanning-tree link-type..............................................................................................83
spanning-tree mode......................................................................................................... 83
spanning-tree pathcost-type.....................................................................................84
spanning-tree tcn-guard..............................................................................................85
spanning-tree vlan......................................................................................................... 85
spanning-tree vlan cost..............................................................................................87
spanning-tree vlan port-priority......................................................................... 88
spanning-tree trap......................................................................................................... 88
MSTP.............................................................................................................................................................. 90
MSTP key concepts............................................................................................................................90
Preparing for MSTP configuration...................................................................................................94
MSTP scenario................................................................................................................................... 95
MSTP commands ............................................................................................................................. 99
show spanning-tree......................................................................................................... 99
show spanning-tree detail....................................................................................... 100
show spanning-tree inconsistent-ports............................................................ 101
show spanning-tree mst..............................................................................................102
show spanning-tree mst-config.............................................................................. 103
show spanning-tree mst detail.............................................................................. 104
show spanning-tree mst <INSTANCE-ID>.............................................................. 106
show spanning-tree mst <INSTANCE-ID> detail.............................................. 107
show spanning-tree mst interface....................................................................... 108
show spanning-tree summary port......................................................................... 109
show spanning-tree summary root......................................................................... 110
spanning-tree.................................................................................................................. 110
spanning-tree bdpu-filter....................................................................................... 111
spanning-tree bpdu-guard......................................................................................... 112
spanning-tree bpdu-guard timeout....................................................................... 113
spanning-tree config-name....................................................................................... 113
spanning-tree config-revision.............................................................................. 114
spanning-tree cost.......................................................................................................115
spanning-tree forward-delay.................................................................................. 116
spanning-tree hello-time......................................................................................... 116
spanning-tree instance cost.................................................................................. 117
spanning-tree instance port-priority.............................................................. 118
spanning-tree instance priority......................................................................... 118
spanning-tree instance vlan.................................................................................. 119
spanning-tree link-type............................................................................................120
spanning-tree loop-guard......................................................................................... 121
spanning-tree max-age................................................................................................ 122
spanning-tree max-hops..............................................................................................122
spanning-tree mode.......................................................................................................123
spanning-tree port-priority.................................................................................. 124
spanning-tree port-type............................................................................................124
spanning-tree priority..............................................................................................125
spanning-tree root-guard......................................................................................... 126
spanning-tree rpvst-filter.....................................................................................127
spanning-tree rpvst-guard....................................................................................... 128
spanning-tree tcn-guard............................................................................................128
spanning-tree transmit-hold-count..................................................................... 129
spanning-tree trap.......................................................................................................129

Contents

5

Chapter 7 MVRP...............................................................................................131
MVRP functionality and limitations.......................................................................................................... 131
MRP messages............................................................................................................................................132
Join message....................................................................................................................................132
New message.................................................................................................................................. 132
Leave message................................................................................................................................ 133
LeaveAll message............................................................................................................................133
Configuring MVRP...................................................................................................................................... 133
MVRP scenario 1.........................................................................................................................................134
MVRP scenario 2.........................................................................................................................................138
MVRP commands....................................................................................................................................... 144
clear mvrp statistics........................................................................................................... 144
mvrp..................................................................................................................................................145
mvrp registration.................................................................................................................... 145
mvrp timer.................................................................................................................................... 146
show mvrp config.......................................................................................................................147
show mvrp state.........................................................................................................................148
show mvrp statistics..............................................................................................................149

Chapter 8 UDLD............................................................................................... 151
Configuring UDLD...................................................................................................................................... 152
UDLD scenario............................................................................................................................................ 153
UDLD commands ...................................................................................................................................... 154
clear udld statistics........................................................................................................... 154
show udld...................................................................................................................................... 155
udld ............................................................................................................................................... 156
udld interval............................................................................................................................. 157
udld mode...................................................................................................................................... 159
udld retries................................................................................................................................161

Chapter 9 Support and other resources.................................................... 162
Accessing Aruba Support.......................................................................................................................... 162
Accessing updates......................................................................................................................................162
Warranty information................................................................................................................................ 163
Regulatory information............................................................................................................................. 163
Documentation feedback..........................................................................................................................163

6

AOS-CX 10.06 Layer 2 Bridging Guide

Chapter 1
About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

• Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

• Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

• Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A, JL711A)

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

Chapter 1 About this document

Table Continued

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

8

AOS-CX 10.06 Layer 2 Bridging Guide

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:

member/slot/port

On the 83xx Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Line module number. Always 1.

• port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

NOTE: If using breakout cables, the port designation changes to x:y, where x is the physical port
and y is the lane when split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in
software is associated with lane 2 on physical port 4 in slot 1 on member 1.

Chapter 1 About this document

9

Chapter 2
Introduction

Switches use network bridging to facilitate the interconnection of local area networks (LANs) so that traffic
can be exchanged between devices. Bridging occurs at layer 2 of the OSI model.

When creating network bridges on HPE switches, network administrators can configure MAC addressing,
VLANs, and various loop prevention protocols.

Devices on a network are identified by their MAC address. The switch maintains a MAC address table where
it stores information about the other Ethernet interfaces to which a switch is connected. The table enables
the switch to send outgoing data (Ethernet frames) on the specific port required to reach its destination,
instead of broadcasting the data on all ports (flooding).

VLANs are primarily used to provide network segmentation at layer 2. VLANs enable the grouping of users
by logical function instead of physical location. Layer 2 VLANs can be associated with a single physical port,
or multiple aggregated ports (referred to as LAG, short form for Link Aggregation). Link Aggregation enables
a logical grouping of individual interfaces to function as a single, higher-speed link, providing dramatically
increased bandwidth. This mechanism provides network resiliency when individual link failures occur. Aruba
switches include advanced network resiliency through MCLAG (Multi Chassis Link Aggregation) which offers
network resiliency on individual device failure as well.

When multiple individual links are connected to one another, there is a possibility that multiple paths (loops)
will exist between devices. Loops reduce network operational efficiency. AOS-CX provides several features to
detect and avoid loops, including:

• MSTP: Multiple-Instance spanning tree protocol (MSTP) ensures that only one active path exists between
any two nodes in a spanning tree instance. A spanning tree instance comprises a unique set of VLANs,
and belongs to a specific spanning tree region. A region can comprise multiple spanning tree instances
(each with a different set of VLANs), and allows one active path among regions in a network.

• RPVST+: Rapid Per VLAN Spanning Tree+ (RPVST+) is an updated implementation of STP (Spanning Tree

Protocol). It enables the creation of a separate spanning tree for each VLAN on a switch, and ensures that
only one active, loop-free path exists between any two nodes on a given VLAN.

•

Loop Protection: In cases where spanning tree protocols cannot be used to prevent loops at the edge of
the network, loop protection may provide a suitable alternative. Loop protection can find loops in
untagged layer 2 links, as well as on tagged VLANs.

AOS-CX also supports the MVRP (Multiple VLAN Registration Protocol), a registration protocol defined by
IEEE, which propagates VLAN information dynamically across devices. It also enables devices to learn and
automatically synchronize VLAN configuration information, reducing the configuration workload.

Additionally, AOS-CX supports the Unidirectional Link Detection (UDLD) protocol. UDLD monitors the link
between two network devices, and if the link fails, blocks the ports on both ends of the link. UDLD is useful
for detecting failures in fiber links and trunks.

10

AOS-CX 10.06 Layer 2 Bridging Guide

Chapter 3
MAC address table

The MAC address table is where the switch stores information about the other Ethernet interfaces to which
it is connected on a network. The table enables the switch to send outgoing data (Ethernet frames) on the
specific port required to reach its destination, instead of broadcasting the data on all ports (flooding).

The MAC address table can contain two types of entries:

• Static: Static entries are manually added to the table by a switch administrator. Static entries have higher

priority than dynamic entries. Static entries remain active until they are removed by the switch
administrator.

• Dynamic: Dynamic entries are automatically added to the table through a process called MAC learning, in

which the switch retrieves the source MAC address (and VLAN ID, if present) of each Ethernet frame
received on a port. If the retrieved address does not exist in the table, it is added. Dynamic entries remain
in the table for a predetermined amount of time (defined with the command mac-address-table
age-time), after which they are automatically deleted.

Dynamic MAC address learning does not distinguish between illegitimate and legitimate frames, which can
invite security hazards. When Host A is connected to port A, a MAC address entry will be learned for the MAC
address of Host A (for example, MAC A). When an illegal user sends frames with MAC A as the source MAC
address to port B, the device performs the following operations:

1. Learns a new MAC address entry with port B as the outgoing interface and overwrites the old entry for

MAC A.

2. Forwards frames destined for MAC A out of port B to the illegal user.

As a result, the illegal user obtains the data of Host A. To improve the security for Host A, manually configure
a static entry to bind Host A to port A. Then, the frames destined for Host A are always sent out of port A.
Other hosts using the forged MAC address of Host A cannot obtain the frames destined for Host A.

For example, in the following topology, switch A learns the MAC addresses of ports on switch B, C, and D.
This way, traffic between any two switches is not broadcast to the other switches. For example, if server 1
sends traffic to server 3, it does not get broadcast onto the link to switch C, only on the link to switch D.

Chapter 3 MAC address table

11

MAC address table commands

clear mac-address

Syntax

clear mac-address {port <PORT-NUM> [vlan <VLAN-ID>] | vlan <VLAN-ID> [port <PORT-NUM>]}

Description

Clears the dynamic learned MAC addresses on the specified port, VLAN, or combination of port and VLAN.

Command context

Manager (#)

Parameters
<PORT-NUM>

Specifies a physical port on the switch. Format: member/slot/port.

<VLAN-ID>

Specifies the number of a VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing the learned MAC addresses on a port:

switch# clear mac-address port 1/1/1

12

AOS-CX 10.06 Layer 2 Bridging Guide

Clearing the learned MAC addresses on a combination of a VLAN and a port:

switch# clear mac-address port 1/1/1 vlan 20

switch# clear mac-address vlan 2 port 1/1/3

mac-address-table age-time

Syntax

mac-address-table age-time <SECONDS>

no mac-address-table age-time [<SECONDS>]

Description

Sets the maximum amount of time a MAC address remains in the MAC address table. When this time
expires, the MAC address is removed.

The no form of this command resets the MAC aging timer to the default value (300 seconds).

Command context

config

Parameters
age-time <SECONDS>

Specifies the MAC address aging time in seconds. Range: 60 to 3600. Default: 300.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# mac-address-table age-time 120

mac-lockout

Syntax

mac-lockout <MAC-ADDR>

no mac-lockout <MAC-ADDR>

Description

Locks a MAC address globally on the switch and all VLANS. The switch drops all data packets addressed to or
from the given address.

The no form of this command unlocks the MAC address globally on the switch and all VLANs.

Command context

config

Parameters
<MAC-ADDR>

Specifies the MAC address.

Chapter 3 MAC address table

13

Authority

Administrators or local user group members with execution rights for this command.

Usage

MAC lockout is implemented on each switch individually. MAC lockout overrides MAC lockdown, port
security (secure MAC), and 802.1X authentication. The MAC lockout feature is not intended to lock
broadcast/multicast MAC addresses and switch agent MACs.

A maximum of 200 MAC lockouts can be configured on a switch.

Example

Enabling MAC lockout:

switch(config)# mac-lockout 00:00:00:00:00:01

Disabling MAC lockout:

switch(config)# no mac-lockout 00:00:00:00:00:01

show mac-address-table

Syntax

show mac-address-table [hsc] [vsx-peer]

Description

Shows MAC address table information. If HSC is enabled, MAC addresses discovered by the HSC manager
are also displayed.

Command context

Operator (>) or Manager (#)

Parameters
[hsc]

Displays only MAC address discovered by the HSC manager on the remote controller.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing output when table entries exist:

switch# show mac-address-table
MAC age-time            : 300 seconds
Number of MAC addresses : 5

MAC Address          VLAN     Type       Port
--------------------------------------------------

14

AOS-CX 10.06 Layer 2 Bridging Guide

00:00:00:00:00:05    1        dynamic    1/1/2
00:00:00:00:00:06    2        dynamic    1/1/1
00:00:00:00:00:08    3        hsc        vxlan1(10.1.1.1)
00:00:00:00:00:12    3        hsc        vxlan1(10.1.1.3)
00:00:00:00:00:34    3        hsc        vxlan1(10.1.1.4)

Showing output when there are no MAC table entries:

switch# show mac-address-table
No MAC entries found.

Showing only MAC address discovered by the HSC manager:

switch# show mac-address-table hsc
Number of MAC addresses : 3
MAC Address          VLAN     Type       Port
---------------------------------------------------------
00:00:00:00:00:08    3        hsc        vxlan1(10.1.1.1)
00:00:00:00:00:12    3        hsc        vxlan1(10.1.1.3)
00:00:00:00:00:34    3        hsc        vxlan1(10.1.1.4)

show mac-address-table address

Syntax

show mac-address-table address <MAC-ADDR> [vsx-peer]

Description

Shows MAC address table information for a specific MAC address.

Command context

Operator (>) or Manager (#)

Parameters
<MAC-ADDR>

Specifies the MAC address.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show mac-address-table address 00:00:00:00:00:01
MAC age-time            : 300 seconds
Number of MAC addresses : 2

MAC Address          VLAN     Type       Port
--------------------------------------------------
00:00:00:00:00:01    2        dynamic    1/1/1
00:00:00:00:00:01    1        dynamic    1/1/1

Chapter 3 MAC address table

15

show mac-address-table count

Syntax

show mac-address-table count
     [dynamic | port <PORT-NUM> | vlan <VLAN-ID>] [vsx-peer]

Description

Displays the number of MAC addresses.

Command context

Operator (>) or Manager (#)

Parameters
dynamic

Show the count of dynamically learned MAC addresses.

<PORT-NUM>

Specifies a physical port on the switch. Format: member/slot/port.

vlan <VLAN-ID>

Specifies the number of a VLAN.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing the number of MAC addresses:

switch# show mac-address-table count
Number of MAC addresses : 8

Showing the number of dynamically learned MAC addresses:

switch# show mac-address-table count dynamic
Number of MAC addresses : 8

Showing the number of MAC addresses per physical port on the switch:

switch# show mac-address-table count port 1/1/1
Number of MAC addresses : 2

Showing the number of MAC addresses per VLAN:

switch# show mac-address-table count vlan 100
Number of MAC addresses : 5

Showing the number of MAC addresses on the VSX primary and secondary (peer) switch:

16

AOS-CX 10.06 Layer 2 Bridging Guide

vsx-primary# show mac-address-table count
Number of MAC addresses : 26114
vsx-primary# show mac-address-table count vsx-peer
Number of MAC addresses : 26113

show mac-address-table dynamic

Syntax

show mac-address-table dynamic [port <PORT-NUM> | vlan <VLAN-ID>]
     [vsx-peer]

Description

Shows MAC address table information about dynamically learned MAC addresses.

Command context

Operator (>) or Manager (#)

Parameters
<PORT-NUM>

Specifies a physical port on the switch. Format: member/slot/port.

<VLAN-ID>

Specifies the number of a VLAN.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing all dynamic MAC address table entries:

switch# show mac-address-table dynamic
MAC age-time            : 300 seconds
Number of MAC addresses : 2

MAC Address          VLAN     Type       Port
--------------------------------------------------
00:00:00:00:00:05    1        dynamic    1/1/2
00:00:00:00:00:06    2        dynamic    1/1/1

Showing dynamic MAC address table entries for VLAN 1:

switch# show mac-address-table dynamic vlan 1
MAC age-time            : 300 seconds
Number of MAC addresses : 1

MAC Address          VLAN     Type       Port
--------------------------------------------------
00:00:00:00:00:05    1        dynamic    1/1/2

Chapter 3 MAC address table

17

Showing dynamic MAC address table entries for port 1/1/1:

switch# show mac-address-table dynamic port 1/1/1
MAC age-time            : 300 seconds
Number of MAC addresses : 1

MAC Address          VLAN     Type       Port
--------------------------------------------------
00:00:00:00:00:06    2        dynamic    1/1/1

show mac-address-table lockout

Syntax

show mac-address-table lockout [vsx-peer]

Description

Shows MAC lockout table information.

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

switch# show mac-address-table lockout
Number of MAC lockout addresses :

2MAC Address          Type
------------------------------------------
00:00:00:00:01:10    static
00:00:00:00:10:03    static

show mac-address-table port

Syntax

show mac-address-table port <PORT-NUM> [vsx-peer]

Description

Shows the MAC address table entries for the specified port.

Command context

Operator (>) or Manager (#)

18

AOS-CX 10.06 Layer 2 Bridging Guide

Parameters
<PORT-NUM>

Specifies a physical port on the switch. Format: member/slot/port.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing the MAC address table entries for port 1/1/1:

switch# show mac-address-table port 1/1/1
MAC age-time            : 300 seconds
Number of MAC addresses : 1

MAC Address          VLAN     Type       Port
--------------------------------------------------
00:00:00:00:00:01    2        dynamic    1/1/1

show mac-address-table static

Syntax

show mac-address-table static

Description

Shows all statically configured MAC addresses.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show mac-address-table static
Number of MAC addresses : 2

MAC Address          VLAN     Port
--------------------------------------
00:00:00:00:10:02    1        1/1/1
00:00:00:00:10:03    1        1/1/1

Chapter 3 MAC address table

19

show mac-address-table vlan

Syntax

show mac-address-table vlan <VLAN-ID> [vsx-peer]

Description

Shows MAC addresses learned by or configured on the specified VLAN.

Command context

Operator (>) or Manager (#)

Parameters
vlan <VLAN-ID>

Specifies the VLAN ID.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show mac-address-table vlan 1
MAC age-time            : 300 seconds
Number of MAC addresses : 1

MAC Address          VLAN     Type       Port
--------------------------------------------------
00:00:00:00:00:01    1        dynamic    1/1/1

static-mac

Syntax

static-mac <MAC-ADDR> vlan <VLAN-ID> port <PORT-NUM>

no static-mac <MAC-ADDR> vlan <VLAN-ID> port <PORT-NUM>

Description

Adds a static MAC address to the MAC address table and associates it with a port or existing VLAN. Static
MAC addresses can only be assigned to layer 2 (non-routed) interfaces. Static MAC addresses are not
affected by the MAC address aging time.

The no form of this command deletes a static MAC address.

Command context

config

20

AOS-CX 10.06 Layer 2 Bridging Guide

Parameters
<MAC-ADDR>

Specifies a MAC address (xx:xx:xx:xx:xx:xx), where x is a hexadecimal number from 0 to F.

vlan <VLAN-ID>

Specifies number of an existing VLAN.

port <PORT-NUM>

Specifies a physical port on the switch. Format: member/slot/port.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# static-mac 00:00:00:00:00:01 vlan 1 port 1/1/1
switch(config)# no static-mac 00:00:00:00:00:01 vlan 1 port 1/1/1

switch(config)# static-mac 00:00:00:00:00:01 vlan 1 port 1/1/2
1/1/2 is not an L2 port

switch(config)# static-mac 00:00:00:00:00:01 vlan 2 port 1/1/1
VLAN 2 not found

Chapter 3 MAC address table

21

Chapter 4
VLANs

VLANs are primarily used to provide network segmentation at layer 2. VLANs enable the grouping of users
by logical function instead of physical location. They make managing bandwidth usage within networks
possible by:

• Allowing grouping of high-bandwidth users on low-traffic segments

• Organizing users from different LAN segments according to their need for common resources and

individual protocols

•

Improving traffic control at the edge of networks by separating traffic of different protocol types.

• Enhancing network security by creating subnets to control in-band access to specific network resources

VLANs are generally assigned on an organizational basis rather than on a physical basis. For example, a
network administrator could assign all workstations and servers used by a particular workgroup to the same
VLAN, regardless of their physical locations.

Hosts in the same VLAN can directly communicate with one another. A router or a Layer 3 switch is required
for hosts in different VLANs to communicate with one another.

VLANs help reduce bandwidth waste, improve LAN security, and enable network administrators to address
issues such as scalability and network management.

VLAN interfaces

Access interface

An access interface carries traffic for a single VLAN ID. Access interfaces are generally used to connect end
devices that do not support VLANs to the network. The devices connected to an access interface are not
aware of the VLAN. Access interface can carry traffic on only one VLAN, either tagged or untagged.

Example

This example shows ingress and egress traffic behavior for an access interface.

22

AOS-CX 10.06 Layer 2 Bridging Guide

• An ingress tagged frame with VLAN ID of 100 arrives on interface 1/2/32. The switch accepts this frame

and sends it to its target address on interface 1/1/32, where it egresses untagged.

• An ingress untagged frame arrives on interface 1/2/32. The switch accepts this frame and sends it to its

target address on interface 1/1/32, where it egresses untagged.

• An ingress tagged frame with VLAN ID of 50 arrives on interface 1/2/32. The switch drops this frame as

VLAN ID 50 is not configured on the interface.

Trunk interface

A trunk interface can carry traffic for one or more VLAN IDs. In most cases, a trunk interface is used to
transport data to other switches or routers.

A trunk interface has two important settings:

• Native VLAN: This is the VLAN to which incoming untagged traffic is assigned. Only one VLAN can be

assigned as the native VLAN. By default, VLAN 1 is assigned as the native VLAN for all trunk interfaces.

• Allowed VLANs: This is the list of VLANs that can be transported by the trunk. If the native VLAN is not
included in the allowed list, all untagged frames that ingress on the trunk interface are dropped.

Example 1: Native untagged VLAN

This example shows ingress and egress traffic behavior when a trunk interface has a native untagged VLAN.

• An ingress tagged frame with VLAN ID of 25 arrives on interface 1/1/1. The switch accepts this frame and
sends it to its target address on interface 1/1/2, where it egresses with a VLAN ID of 25 untagged since
port 1/1/2 is configured with a native VLAN ID of 25.

• An ingress untagged frame arrives on interface 1/1/1. The switch accepts this frame and sends it to its
target address on interface 1/1/2, where it egresses with a VLAN ID of 25 untagged since port 1/1/2 is
configured with a native VLAN ID of 25.

• An ingress tagged frame with VLAN ID of 4 arrives on interface 1/1/1. The switch accepts this frame and
sends it to its target address on interface 1/1/2, where it egresses with a VLAN ID of 4 tagged since port
1/1/2 is configured to allow traffic with a VLAN ID of 4.

• An ingress tagged frame with VLAN ID of 50 arrives on interface 1/1/1. The switch drops this frame as

VLAN ID 50 is not in the allowed list for interface 1/1/1.

Example 2: Native tagged VLAN

Chapter 4 VLANs

23

This example shows ingress and egress traffic behavior when a trunk interface has a native tagged VLAN.
• An ingress tagged frame with VLAN ID of 6 arrives on interface 1/1/13. The switch accepts this frame and
sends it to its target address on interface 1/1/21, where it egresses with a VLAN ID of 6 tagged since port
1/1/2 is configured with a native VLAN ID of 6.
• An ingress untagged frame arrives on interface 1/1/13. The switch drops this frame since the interface is
configured as native tagged (all untagged frames a dropped in such a configuration).
• An ingress tagged frame with VLAN ID of 17 arrives on interface 1/1/13. The switch accepts this frame
and sends it to its target address on interface 1/1/21, where it egresses with a VLAN ID of 17 tagged since
port 1/1/2 is configured to allow traffic with a VLAN ID of 17.
• An ingress tagged frame with VLAN ID of 50 arrives on interface 1/1/13. The switch drops this frame as
VLAN ID 50 is not in the allowed list for interface 1/1/13.
Traffic handling summary
| VLAN configuration | Ingress traffic | Egress traffic |
| ------------------ | --------------- | -------------- |
Access interface with:
|     | 1. Untagged | 1. Untagged on VLAN X |
| --- | ----------- | --------------------- |
VLAN ID = X
|                       | 2. Tagged with VLAN ID = X       | 2. Untagged on VLAN X |
| --------------------- | -------------------------------- | --------------------- |
|                       | 3. Tagged with any other VLAN ID | 3. Dropped            |
| Trunk interface with: | 1. Untagged                      | 1. Untagged on VLAN X |
• Untagged Native VLAN ID = X
|     | 2. Tagged with VLAN ID = X | 2. Untagged on VLAN X |
| --- | -------------------------- | --------------------- |
• Allowed VLAN IDs = X, Y, Z
|     | 3. Tagged with VLAN ID = Y       | 3. Tagged on VLAN Y |
| --- | -------------------------------- | ------------------- |
|     | 4. Tagged with VLAN ID = Z       | 4. Tagged on VLAN Z |
|     | 5. Tagged with any other VLAN ID | 5. Dropped          |
Table Continued
| 24  |     | AOS-CX 10.06 Layer 2 Bridging Guide |
| --- | --- | ----------------------------------- |

| VLAN configuration | Ingress traffic | Egress traffic |
| ------------------ | --------------- | -------------- |
Trunk interface with:
|     | 1. Untagged | 1. Untagged on VLAN X |
| --- | ----------- | --------------------- |
• Untagged Native VLAN ID = X
|     | 2. Tagged with VLAN ID = X | 2. Untagged on VLAN X |
| --- | -------------------------- | --------------------- |
• Allowed VLAN IDs = ALL
|     | 3. Tagged with a VLAN ID defined | 3. Tagged on the matching VLAN |
| --- | -------------------------------- | ------------------------------ |
on the switch
4. Dropped
4. Tagged with a VLAN ID not
defined on the switch
| Trunk interface with: | 1. Untagged | 1. Dropped |
| --------------------- | ----------- | ---------- |
• Tagged Native VLAN ID = X
|     | 2. Tagged with VLAN ID = X | 2. Tagged on VLAN X |
| --- | -------------------------- | ------------------- |
• Allowed VLAN IDs = X, Y, Z
|                       | 3. Tagged with VLAN ID = Y       | 3. Tagged on VLAN Y |
| --------------------- | -------------------------------- | ------------------- |
|                       | 4. Tagged with VLAN ID = Z       | 4. Tagged on VLAN Z |
|                       | 5. Tagged with any other VLAN ID | 5. Dropped          |
| Trunk interface with: | 1. Untagged                      | 1. Dropped          |
• Tagged Native VLAN ID = X
|     | 2. Tagged with VLAN ID = X | 2. Tagged on VLAN X |
| --- | -------------------------- | ------------------- |
• Allowed VLAN IDs = ALL
|     | 3. Tagged with a VLAN ID defined | 3. Tagged on the matching VLAN |
| --- | -------------------------------- | ------------------------------ |
on the switch
4. Dropped
4. Tagged with a VLAN ID not
defined on the switch
Trunk interface with:
|     | 1. Untagged | 1. Dropped |
| --- | ----------- | ---------- |
• Untagged Native VLAN ID = A
|     | 2. Tagged with VLAN ID = X | 2. Tagged on VLAN X |
| --- | -------------------------- | ------------------- |
• Allowed VLAN IDs = X, Y, Z
|     | 3. Tagged with VLAN ID = Y       | 3. Tagged on VLAN Y |
| --- | -------------------------------- | ------------------- |
|     | 4. Tagged with VLAN ID = Z       | 4. Tagged on VLAN Z |
|     | 5. Tagged with any other VLAN ID | 5. Dropped          |
Comparing VLAN commands on PVOS, Comware, and AOS-CX
The following examples compare the commands needed to implement typical VLAN configurations on
different HPE products.
Chapter 4 VLANs 25

| AOS-CX                      | PVOS                 | Comware                   |
| --------------------------- | -------------------- | ------------------------- |
| interface 1/1/1             | interface A1         | Interface G1/0/1          |
| no routing                  |   tagged vlan        |   port link type trunk    |
| vlan trunk native 1         | 10,30,50             |   port trunk permit vlan  |
| vlan trunk allowed 10,30,50 |   no untagged vlan 1 | 10,30,50                  |
  port trunk pvid vlan 1
A native VLAN must be defined on
the switch. By default, this is VLAN 1. PVID 1 is the default setting.
Since only VLANs 10, 30, and 50 are
allowed on the trunk, all untagged
traffic is dropped.
| AOS-CX | PVOS                      | Comware                              |
| ------ | ------------------------- | ------------------------------------ |
|        | Not directly supported in | Not directly supported in Comware. A |
interface 1/1/1
|     | PVOS. Scenario 1 is a | possible workaround is: |
| --- | --------------------- | ----------------------- |
no routing
workaround if there is no
| vlan trunk native 10 tag |     | interface g1/0/1 |
| ------------------------ | --- | ---------------- |
need to support untagged
| vlan trunk allowed 10,30,50 |     |   port link-mode bridge |
| --------------------------- | --- | ----------------------- |
traffic.
  port link-type hybrid
Same as scenario 1, but allows
  port hybrid protocol-vlan
| untagged traffic on VLAN 10 as well. |     | vlan 10 |
| ------------------------------------ | --- | ------- |
  port hybrid vlan 10 tagged
  port hybrid vlan 30 tagged
  port hybrid vlan 50 tagged
| AOS-CX | PVOS | Comware |
| ------ | ---- | ------- |
interface G1/0/1
| interface 1/1/1 | interface A1      |   Port link-mode bridge |
| --------------- | ----------------- | ----------------------- |
| no routing      |   untagged vlan 5 |                         |
  port link-type trunk
| vlan trunk native 5 |   no tagged vlan  |     |
| ------------------- | ----------------- | --- |
  port trunk pvid vlan 5
| vlan trunk allowed 5,  | 10,30,50 |   port trunk permit vlan  |
| ---------------------- | -------- | ------------------------- |
10,30,50
5,10,30,50
VLAN 5 must be allowed on the trunk link-mode is only needed on later
so that untagged traffic is not
Comware 7 devices. 5930 is port link-
dropped.
mode route by default. 5900 is bridge
by default.
| ArubaOS-CX      | PVOS              | Comware                 |
| --------------- | ----------------- | ----------------------- |
| interface 1/1/1 | interface A1      | interface G1/0/0        |
| no routing      |   untagged vlan 5 |   port link-mode bridge |
| vlan access 5   |                   |   port access vlan 5    |
VLAN numbering
VLANs are numbered in the range 1 to 4040.
| 26  |     | AOS-CX 10.06 Layer 2 Bridging Guide |
| --- | --- | ----------------------------------- |

By default, VLAN 1 (the default VLAN) is associated with all interfaces on the switch. VLAN 1 cannot be
removed from the switch.

Configuring VLANs

Creating and enabling a VLAN

Procedure

1. Switch to the configuration context with the command config.

2. Create a new VLAN with the command vlan.

Example

This example creates VLAN 10. The VLAN is enabled by default.

switch# config
switch(config)# vlan 10
switch(config-vlan-10)#

Disabling a VLAN

Procedure

1. Switch to configuration context with the command config.

2. Switch to configuration context for the VLAN you want to disable with the command vlan.

3. Disable the VLAN with the command shutdown.

Example

This example disables VLAN 10.

switch(config)# config
switch(config)# vlan 10
switch(config-vlan-10)# shutdown

Assigning a VLAN to an interface

To use a VLAN, it must be assigned to an interface on the switch. VLANs can only be assigned to non-routed
(layer 2) interfaces. All interfaces are routed (layer 3) by default when created. Use the no routing
command to disable routing on an interface.

Assigning a VLAN ID to an access interface

Prerequisites
At least one defined VLAN.

Chapter 4 VLANs

27

Procedure

1. Switch to configuration context with the command config.

2. Switch to the interface that you want to define as an access interface with the command interface.

3. Disable routing with the command no routing.

4. Configure the access interface and assign a VLAN ID with the command vlan access.

Examples

This example configures interface 1/1/2 as an access interface with VLAN ID set to 20.

switch# config
switch(config)# vlan 20
switch(config-vlan-20)# exit
switch(config)# interface 1/1/2
switch(config-lag-if)# no routing
switch(config-if)# vlan access 20

This example configures LAG 1 as an access interface with VLAN ID set to 30.

switch# config
switch(config)# vlan 30
switch(config-vlan-30)# exit
switch(config)# interface lag 1
switch(config-lag-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-lag-if)# vlan access 30

Assigning a VLAN ID to a trunk interface

Prerequisites
At least one defined VLAN.

Procedure

1. Switch to configuration context with the command config.

2. Switch to the interface that you want to define as a trunk interface with the command interface.

3. Disable routing with the command no routing.

4. Configure the trunk interface and assign a VLAN ID with the command vlan trunk allowed.

Examples

This example configures interface 1/1/2 as a trunk interface allowing traffic with VLAN ID set to 20.

switch# config
switch(config)# vlan 20
switch(config-vlan-20)# exit
switch(config)# interface 1/1/2
switch(config-lag-if)# no routing
switch(config-if)# vlan trunk allowed 20

This example configures interface 1/1/2 as a trunk interface allowing traffic with VLAN IDs 2, 3, and 4.

28

AOS-CX 10.06 Layer 2 Bridging Guide

switch# config
switch(config)# vlan 2,3,4
switch(config)# interface 1/1/2
switch(config-lag-if)# no routing
switch(config-if)# vlan trunk allowed 2,3,4

This example configures interface 1/1/2 as a trunk interface allowing traffic with VLAN IDs 2 to 8.

switch# config
switch(config)# vlan 2-8
switch(config)# interface 1/1/2
switch(config-lag-if)# no routing
switch(config-if)# vlan trunk allowed 2-8

This example configures interface 1/1/2 as a trunk interface allowing traffic with VLAN IDs 2 to 8 and 10.

switch# config
switch(config)# vlan 2-8,10
switch(config)# interface 1/1/2
switch(config-lag-if)# no routing
switch(config-if)# vlan trunk allowed 2-8,10

This example configures interface 1/1/2 as a trunk interface allowing traffic on all configured VLAN IDs
(20-100).

switch# config
switch(config)# vlan 20-100
switch(config)# interface 1/1/2
switch(config-lag-if)# no routing
switch(config-if)# vlan trunk allowed all

Assigning a native VLAN ID to a trunk interface

Prerequisites
At least one defined VLAN.

Procedure

1. Switch to configuration context with the command config.

2. Switch to the trunk interface to which you want to assign the native VLAN ID with the command

interface.

3. Disable routing with the command no routing.

4. Assign the native VLAN ID with the command vlan trunk native. If tagging is required, use the

command vlan trunk native tag.

5. Allow traffic tagged with the native VLAN ID to be transported by the trunk using the command vlan

trunk allowed.

Example

This example assigns native VLAN ID 20 to trunk interface 1/1/2.

switch# config
switch(config)# vlan 20
switch(config-vlan-20)# exit
switch(config)# interface 1/1/2

Chapter 4 VLANs

29

switch(config-if)# no routing
switch(config-if)# vlan trunk native 20

This example assigns native VLAN ID 40 to trunk interface 1/1/5, enables tagging, and allows traffic with
VLAN ID 40 to be transported by the trunk.

switch# config
switch(config)# vlan 40
switch(config-vlan-40)# exit
switch(config)# interface 1/1/5
switch(config-if)# no routing
switch(config-if)# vlan trunk native 40 tag
switch(config-if)# vlan trunk allow 40

Viewing VLAN configuration information

Prerequisites
At least one defined VLAN.

Procedure

1. View a summary of VLAN configuration information with the command show vlan summary.

2. View VLAN configuration settings with the command show vlan.

3. View VLANs configured for a specific layer 2 interface with the command show vlan port.

4. View the commands used to configure VLAN settings with the command show running-config

interface.

Example

This example displays a summary of all VLANs.

switch# show vlan summary

Number of existing VLANs: 11
Number of static VLANs:   11
Number of dynamic VLANs:  0

This example displays configuration information for all defined VLANs.

switch# show vlan

-----------------------------------------------------------------------------------
VLAN  Name             Status  Reason          Type      Interfaces
-----------------------------------------------------------------------------------
1     DEFAULT_VLAN_1     up      ok              static    1/1/3-1/1/4
2     UserVLAN1          up      ok              static    1/1/1,1/1/3,1/1/5
3     UserVLAN2          up      ok              static    1/1/2-1/1/3,1/1/5-1/1/6
5     UserVLAN3          up      ok              static    1/1/3
10    TestNetwork        up      ok              static    1/1/3,1/1/5
11    VLAN11             up      ok              static    1/1/3
12    VLAN12             up      ok              static    1/1/3,1/1/6,lag1-lag2
13    VLAN13             up      ok              static    1/1/3,1/1/6
14    VLAN14             up      ok              static    1/1/3,1/1/6
20    ManagementVLAN     down    admin_down      static    1/1/3,1/1/10

This example displays configuration information for VLAN 2.

30

AOS-CX 10.06 Layer 2 Bridging Guide

switch# show vlan 2
-----------------------------------------------------------------------------------
VLAN  Name                     Status  Reason          Type      Interfaces
-----------------------------------------------------------------------------------
2     UserVLAN1                up      ok              static    1/1/1,1/1/3,1/1/5

This example displays the VLANs configured on interface 1/1/3.

switch# show vlan port 1/1/3
------------------------------------------------------
VLAN  Name                            Mode
------------------------------------------------------
1     DEFAULT_VLAN_1                  native-untagged
2     UserVLAN1                       trunk
3     UserVLAN2                       trunk
5     UserVLAN3                       trunk
10    TestNetwork                     trunk
11    VLAN11                          trunk
12    VLAN12                          trunk
13    VLAN13                          trunk
14    VLAN14                          trunk
20    ManagementVLAN                  trunk

This example displays VLAN configuration commands for interface 1/1/16.

switch#  show running-config interface 1/1/16
interface 1/1/16
   no routing
   vlan trunk native 108
   vlan trunk allowed all
   exit

VLAN scenario
This scenario shows how to assign VLAN IDs to access and trunk interfaces for the following deployment:

Chapter 4 VLANs

31

In this scenario, VLANs are used to isolate the traffic from different devices.

• VLAN 25 carries tagged and untagged traffic from computers connected to switch B.

• VLAN 4 carries tagged traffic from computers connected to switch B.

• VLAN 6 carries tagged and untagged traffic from computers connected to switch C.

• VLAN 17 carries tagged traffic from computers connected to switch C.

• VLAN 100 carries untagged traffic from the server.

Procedure

1. Execute the following commands on switch A and B.

a. Create VLANs 4 and 25.

switch# config
switch(config)# vlan 4,25

b. Define LAG 1 and assign the VLANs to it.

switch(config)# interface lag 1
switch(config-lag-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-lag-if)# vlan trunk native 25
switch(config-lag-if)# vlan trunk allowed 4,25

c. Add ports 1/1/1 and 1/2/1 to LAG 1.

32

AOS-CX 10.06 Layer 2 Bridging Guide

switch(config-lag-if)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-if)# lag 1
switch(config-if)# interface 1/2/1
switch(config-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-if)# lag 1

2. Execute the following commands on switch A and C.

a. Create VLANs 6 and 17.

switch# config
switch(config)# vlan 6,17

b. Define LAG 3 and assign the VLANs to it.

switch(config)# interface lag 3
switch(config-lag-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-lag-if)# vlan trunk native 6 tag
switch(config-lag-if)# vlan trunk allowed 6,17

c. Add ports 1/1/13 and 1/2/13 to LAG 3.

switch(config-lag-if)# interface 1/1/13
switch(config-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-if)# lag 3
switch(config-if)# interface 1/2/13
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# lag 3

3. Execute the following commands on switch A to configure the connection to the server.

a. Configure interface 1/2/13 as an access interface with VLAN ID set to 100.

switch# config
switch (config)# vlan 100
switch(config-vlan-100)# interface 1/2/32
switch(config-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-if)# vlan access 100
switch(config-if)# exit

4. Verify VLAN configuration by running the command show vlan. For example:

switch# show vlan

--------------------------------------------------------------------------------------------------------------
VLAN  Name                              Status  Reason                Type      Interfaces
--------------------------------------------------------------------------------------------------------------
1     DEFAULT_VLAN_1                    down    no_member_port        default
4     VLAN4                             up      ok                    static    lag1
6     VLAN6                             up      ok                    static    lag3
17    VLAN17                            up      ok                    static    lag3
25    VLAN25                            up      ok                    static    lag1
100   VLAN100                           up      ok                    static    1/2/32

5. Verify that the connection to the DHCP server is sending/receiving data with the command show

interface. Check that the Rx and Tx fields are incrementing. For example:

Chapter 4 VLANs

33

switch# show interface 1/2/32
Interface 1/2/32 is up
 Admin state is up
 Description:
 Hardware: Ethernet, MAC Address: 70:72:cf:3a:8a:0b
 MTU 1500
 Type SFP+LR
 qos trust none
 Speed 10000 Mb/s
 Auto-Negotiation is off
 Input flow-control is off, output flow-control is off
 VLAN Mode: access
 Access VLAN: 100

 Rx
            20 input packets              1280 bytes
            0 input error                0 dropped
            0 CRC/FCS
 Tx
            9 output packets             1054 bytes
            0 input error                0 dropped
            0 collision

6. Verify LAG interface configuration with the command show interface. Check the fields admin state,
MAC address, Aggregated-interfaces, VLAN Mode, Native VLAN, Allowed VLAN, Rx count, and Tx count.
For example:

switch# show interface lag1
Aggregate-name lag1
 Description :
 Admin state           : up
 MAC Address           : 94:f1:28:21:63:00
 Aggregated-interfaces : 1/1/1 1/2/1
 Aggregation-key       : 1
 Speed 1000 Mb/s
 L3 Counters: Rx Disabled, Tx Disabled
 qos trust none
 VLAN Mode: native-untagged
 Native VLAN: 25
 Allowed VLAN List: 4,25
 Rx
            10 input packets              1280 bytes
            0 input error                0 dropped
            0 CRC/FCS
 Tx
            8 output packets             980 bytes
            0 input error                0 dropped
            0 collision

switch# show interface lag3
Aggregate-name lag3
 Description :
 Admin state           : up
 MAC Address           : 94:f1:28:21:63:00
 Aggregated-interfaces : 1/1/13 1/2/13
 Aggregation-key       : 3
 Speed 1000 Mb/s
 L3 Counters: Rx Disabled, Tx Disabled
 qos trust none
 VLAN Mode: native-tagged
 Native VLAN: 6
 Allowed VLAN List: 6,17

34

AOS-CX 10.06 Layer 2 Bridging Guide

Rx
            19 input packets              1280 bytes
            0 input error                0 dropped
            0 CRC/FCS
Tx
            15 output packets             1000 bytes
            0 input error                0 dropped
0    Collision

7. Verify the physical interfaces (1/1/1, 1/2/1, 1/1/13, 1/2/13) with the command show interface. Check

that the Rx and Tx fields are incrementing. For example:

switch# show interface 1/1/1
Interface 1/1/1 is up
 Admin state is up
 Description:
 Hardware: Ethernet, MAC Address: 94:f1:28:21:73:ff
 MTU 1500
 Type SFP+LR
 qos trust none
 Speed 1000 Mb/s
 Auto-Negotiation is off
 Input flow-control is off, output flow-control is off
 Rx
            6 input packets              620 bytes
            0 input error                0 dropped
            0 CRC/FCS
 Tx
            4 output packets             422 bytes
            0 input error                0 dropped
0    collision

VLAN commands

description

Syntax

description <DESCRIPTION>

Description

Specifies a descriptive for a VLAN.

Command context

config-vlan-<VLAN-ID>

Parameters
<DESCRIPTION>

Specifies a description for the VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Assigning a description to VLAN 20:

Chapter 4 VLANs

35

switch(config)# vlan 20
switch(config-vlan-20)# description primary

name

Syntax

name <VLAN-NAME>

Description

Associates a name with a VLAN.

Command context

config-vlan-<VLAN-ID>

Parameters
<VLAN-NAME>

Specifies a name for a VLAN. Length: 1 to 32 alphanumeric characters, including underscore (_) and
hyphen (-).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Assigning the name backup to VLAN 20:

switch(config)# vlan 20
switch(config-vlan-20)# name backup

show capacities svi-count

Syntax

show capacities svi-count

Description

Shows the maximum number of SVIs supported by the switch.

Command context

Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing switch SVI capacity:

switch# show capacities svi-count
System Capacities: Filter SVI count
Capacities Name                                                                                       Value
---------------------------------------------------------------------
Maximum number of SVIs supported in the system                    128

36

AOS-CX 10.06 Layer 2 Bridging Guide

show system internal-vlan-range

Syntax

show system internal-vlan-range

no system vlan-client-presence-detect

Description
Shows the VLAN range reserved for internal use.

Command context

manager

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing reserved VLANs:

switch(config)# show system internal-vlan-range
Internal VLAN range:          4041-4094

show vlan

Syntax

show vlan [<VLAN-ID>] [vsx-peer]

Description

Displays configuration information for all VLANs or a specific VLAN.

Command context

Manager (#)

Parameters
<VLAN-ID>

Specifies a VLAN ID.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying configuration information for VLAN 2:

Chapter 4 VLANs

37

switch# show vlan 2
----------------------------------------------------------------------------------
VLAN  Name                     Status  Reason          Type      Interfaces
----------------------------------------------------------------------------------
2     UserVLAN1                up      ok              static    1/1/1,1/1/3,1/1/5

Displaying configuration information for all defined VLANs:

switch# show vlan
----------------------------------------------------------------------------------
VLAN  Name                 Status  Reason        Type      Interfaces
-----------------------------------------------------------------------------------
1     DEFAULT_VLAN_1       up      ok            static    1/1/3-1/1/4
2     UserVLAN1            up      ok            static    1/1/1,1/1/3,1/1/5
3     UserVLAN2            up      ok            static    1/1/2-1/1/3,1/1/5-1/1/6
5     UserVLAN3            up      ok            static    1/1/3
10    TestNetwork          up      ok            static    1/1/3,1/1/5
11    VLAN11               up      ok            static    1/1/3
12    VLAN12               up      ok            static    1/1/3,1/1/6,lag1-lag2
13    VLAN13               up      ok            static    1/1/3,1/1/6
14    VLAN14               up      ok            static    1/1/3,1/1/6
20    ManagementVLAN       down    admin_down    static    1/1/3,1/1/10

show vlan port

Syntax

show vlan port <INTERFACE-ID> [vsx-peer]

Description

Displays the VLANs configured for a specific layer 2 interface.

Command context

Manager (#)

Parameters
<INTERFACE-ID>

Specifies an interface ID. Format: member/slot/port.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Displaying the VLANs configured on interface 1/1/3:

switch# show vlan port 1/1/3
------------------------------------------------------
VLAN  Name                            Mode
------------------------------------------------------
1     DEFAULT_VLAN_1                  native-untagged

38

AOS-CX 10.06 Layer 2 Bridging Guide

2     UserVLAN1                       trunk
3     UserVLAN2                       trunk
5     UserVLAN3                       trunk
10    TestNetwork                     trunk
11    VLAN11                          trunk
12    VLAN12                          trunk
13    VLAN13                          trunk
14    VLAN14                          trunk
20    ManagementVLAN                  trunk

show vlan summary

Syntax

show vlan summary [vsx-peer]

Description

Displays a summary of the VLAN configuration on the switch.

Command context

Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying a summary of the VLAN configuration on the switch:

switch# show vlan summary
Number of existing VLANs: 11
Number of static VLANs:   11
Number of dynamic VLANs:  0

show vlan translation

Syntax

show vlan translation [interface <INTERFACE-NAME>] [vsx-peer]

Description

Shows a summary of all VLAN translations rules defined on the switch, or the rules defined for a specific
interface.

Command context

Manager (#)

Chapter 4 VLANs

39

Parameters
interface <INTERFACE-NAME>

Specifies the name of a layer 2 interface. Format: member/slot/port.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying a summary of all VLAN translations rules defined on the switch:

switch# show vlan translation
-------------------------------------------
Interface  VLAN-1      VLAN-2
-------------------------------------------
1/1/5      10          20
1/1/5      30          40
1/1/5      50          100
1/1/6      100         200

Total number of translation rules : 4

Displaying a summary of all VLAN translations rules defined on interface 1/1/5:

switch# show vlan translation interface 1/1/5
-------------------------------------------
Interface  VLAN-1      VLAN-2
-------------------------------------------
1/1/5      10          20
1/1/5      30          40
1/1/5      50          100

shutdown

Syntax

shutdown

no shutdown

Description

Disables a VLAN. (By default, a VLAN is automatically enabled when it is created with the vlan command.)

The no form of this command enables a VLAN.

Command context

config-vlan-<VLAN-ID>

Authority

Administrators or local user group members with execution rights for this command.

40

AOS-CX 10.06 Layer 2 Bridging Guide

Examples

Enabling VLAN 20:

switch(config)# vlan 20
switch(config-vlan-20)# no shutdown

Disabling VLAN 20:

switch(config)# vlan 20
switch(config-vlan-20)# shutdown

system internal-vlan-range

Syntax

system internal-vlan-range {<VLAND-ID>-<VLAN-ID> | none } [confirm]

no system internal-vlan-range {<VLAND-ID>-<VLAN-ID> | none } [confirm]

Description
Configures the VLAN range reserved for internal use for route-only ports and LAGs. The internal VLAN range
cannot include any VLANs that are already in use.

If the number of internal VLANs is less than the number of route-only ports and LAGs, some ports will be
blocked and unable to be used. When the internal VLAN range is modified, traffic on route-only ports and
LAGs is briefly interrupted while they are moved to the new range.

The no' form of this command sets the range to the default of 4041 to 4094.

Command context

config

Parameters
<VLAND-ID>-<VLAN-ID>

Specifies the starting and ending VLAN number for the range. The reserved range must be between 2
and 4094 and cannot exceed 256 VLANs. Default: 4041-4094.

none

Do not reserve any internal VLANs.

confirm

Automatically acknowledge warning and skip confirmation prompt.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting a new internal VLAN range:

switch(config)# system internal-vlan-range 3041-3094
This will briefly interrupt traffic.

Continue (y/n)?

Setting a new internal VLAN range, skipping the prompt:

Chapter 4 VLANs

41

switch(config)# system internal-vlan-range 3041-3094 confirm

Removing all internal VLANs:

switch(config)# system internal-vlan-range none
All route-only ports and LAGs will be blocked.

Continue (y/n)?

system vlan-client-presence-detect

Syntax

system vlan-client-presence-detect

no system vlan-client-presence-detect

Description

Enables VNI mapped VLANs when detecting the presence of a client. When enabled, VNI mapped VLANs are
up only if there are authenticated clients on the VLAN, or if the VLAN has statically configured ports and
those ports are up. When not enabled, VNI mapped VLANs are always up.

The no form of this command disables detection of clients on VNI mapped VLANs.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling detection of clients:

switch(config)# system vlan-client-presence-detect

Disabling detection of clients:

switch(config)# no system vlan-client-presence-detect

vlan

Syntax

vlan <VLAN-LIST>

no vlan <VLAN-LIST>

Description

Creates a VLAN and changes to the config-vlan-id context for the VLAN. By default, the VLAN is enabled.
To disable a VLAN, use the no shutdown command.

If the specified VLAN exists, this command changes to the config-vlan-id context for the VLAN. If a range
of VLANs is specified, the context does not change.

The no form of this command removes a VLAN. VLAN 1 is the default VLAN and cannot be deleted.

42

AOS-CX 10.06 Layer 2 Bridging Guide

Command context

config

Parameters
<VLAN-LIST>

Specifies a single ID, or a series of IDs separated by commas (2, 3, 4), dashes (2-4), or both (2-4,6). Range:
1 to 4040.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating VLAN 20:

switch(config)# vlan 20
switch(config-vlan-20)#

Removing VLAN 20:

switch(config)# no vlan 20

Creating VLANs 2 to 8 and 10:

switch(config)# vlan 2-8,10

Removing VLANs 2 to 8 and 10:

switch(config)# no vlan 2-8,10

vlan access

Syntax

vlan access <VLAN-ID>

no vlan access [<VLAN-ID>]

Description

Creates an access interface and assigns an VLAN ID to it. Only one VLAN ID can be assigned to each access
interface.

VLANs can only be assigned to a non-routed (layer 2) interface or LAG interface. By default, all interfaces are
routed (layer 3) when created. Use the no routing command to disable routing on an interface and
change the interface to a layer 2 interface.

The no form of this command removes an access VLAN from the interface in the current context and sets it
to the default VLAN ID of 1.

Command context

config-if

Parameters
<VLAN-ID>

Specifies a single ID, or a series of IDs separated by commas (2, 3, 4), dashes (2-4), or both (2-4,6). Range:
1 to 4040.

Chapter 4 VLANs

43

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring interface 1/1/2 as an access interface with VLAN ID set to 20:

switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan access 20

Removing VLAN ID 20 from interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no vlan access 20

or:

switch(config)# interface 1/1/2
switch(config-if)# no vlan access

vlan translate

Syntax

vlan translate <VLAN-1> <VLAN-2>

no vlan translate <VLAN-1> <VLAN-2>

Description

Defines a bidirectional VLAN translation rule that maps an external VLAN ID to an internal VLAN ID on a LAG
or layer 2 interface. Applies to both incoming and outgoing traffic.

The no form of this command removes an existing VLAN translation rule on the current interface.

NOTE: VLAN translation and MVRP cannot be enabled on the same interface.

Command context

config-if

config-lag-if

Parameters
<VLAN-1>

Specifies the number of an external VLAN. Range: 1 - 4040.

<VLAN-2>

Specifies the number of an internal VLAN. Range: 1 - 4040.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Translates external VLAN 200 to internal VLAN 20 on interface 1/1/2.

44

AOS-CX 10.06 Layer 2 Bridging Guide

switch# config
switch(config)# vlan 20
switch(config-vlan-20)# exit
switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 20
switch(config-if)# vlan translate 200 20

Translates external VLANs 100 and 300 to internal VLANs 10 and 20 on interface 1/1/2.

switch# config
switch(config)# vlan 10,30
switch(config-vlan-20)# exit
switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 10,30
switch(config-if)# vlan translate 100 10
switch(config-if)# vlan translate 300 30

vlan trunk allowed

Syntax

vlan trunk allowed [<VLAN-LIST> | all]

no vlan trunk allowed [<VLAN-LIST>]

Description

Assigns a VLAN ID to an trunk interface. Multiple VLAN IDs can be assigned to a trunk interface. These VLAN
IDs define which VLAN traffic is allowed across the trunk interface.

VLANs can be assigned only to a non-routed (layer 2) interface or LAG interface. By default, all interfaces are
routed (layer 3) when created. Use the no routing command to disable routing on an interface.

The no form of this command removes one or more VLAN IDs from a trunk interface. When the last VLAN is
removed from a trunk interface, the interface continues to operate in trunk mode, and will trunk all the
VLANs currently defined on the switch, and any new VLANs defined in the future. To disable the trunk
interface, use the command shutdown.

Command context

config-if

Parameters
<VLAN-LIST>

Specifies a single ID, or a series of IDs separated by commas (2, 3, 4), dashes (2-4), or both (2-4,6). Range:
1 to 4040.

all

Configures the trunk interface to allow all the VLANs currently configured on the switch and any new
VLANs that are configured in the future.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Assigning VLANs 2, 3, and 4 to trunk interface 1/1/2:

Chapter 4 VLANs

45

switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 2,3,4

Assigning VLAN IDs 2 to 8 to trunk interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 2-8

Assigning VLAN IDs 2 to 8 and 10 to trunk interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 2-8,10

Removing VLAN IDs 2, 3, and 4 from trunk interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no vlan trunk allowed 2,3,4

Removing all VLANs assigned to trunk interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no vlan trunk allowed

vlan trunk native

Syntax

vlan trunk native <VLAN-ID>

no vlan trunk native [<VLAN-ID>]

Description

Assigns a native VLAN ID to a trunk interface. By default, VLAN ID 1 is assigned as the native VLAN ID for all
trunk interfaces. VLANs can only be assigned to a non-routed (layer 2) interface or LAG interface. Only one
VLAN ID can be assigned as the native VLAN.

NOTE: When a native VLAN is defined, the switch automatically executes the vlan trunk
allowed all command to ensure that the default VLAN is allowed on the trunk. To only allow
specific VLANs on the trunk, issue the vlan trunk allowed command specifying only specific
VLANs.

The no form of this command removes a native VLAN from a trunk interface and assigns VLAN ID 1 as its
native VLAN.

Command context

config-if

Parameters
<VLAN-ID>

Specifies a VLAN ID. Range: 1 to 4040.

Authority

Administrators or local user group members with execution rights for this command.

46

AOS-CX 10.06 Layer 2 Bridging Guide

Examples

Assigning native VLAN ID 20 to trunk interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan trunk native 20

Removing native VLAN 20 from trunk interface 1/1/2 and returning to the default VLAN 1 as the native
VLAN.

switch(config)# interface 1/1/2
switch(config-if)# no vlan trunk native 20

or:

switch(config)# interface 1/1/2
switch(config-if)# no vlan trunk native

Assigning native VLAN ID 20 to trunk interface 1/1/2 and then removing it from the list of allowed VLANs.
(Only allow VLAN 10 on the trunk.)

switch(config)# interface 1/1/2
switch(config-if)# no routing
switch(config-if)# vlan trunk native 20
switch(config-if)# vlan trunk allowed 10

vlan trunk native tag

Syntax

vlan trunk native <VLAN-ID> tag

no vlan trunk native <VLAN-ID> tag

Description

Enables tagging on a native VLAN. Only incoming packets that are tagged with the matching VLAN ID are
accepted. Incoming packets that are untagged are dropped except for BPDUs. Egress packets are tagged.

The no form of this command removes tagging on a native VLAN.

Command context

config-if

Parameters
<VLAN-ID>

Specifies the number of a VLAN. Range: 1 to 4040.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling tagging on native VLAN 20 on trunk interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no routing

Chapter 4 VLANs

47

switch(config-if)# vlan trunk native 20
switch(config-if)# vlan trunk native 20 tag

Removing tagging on native VLAN 20 assigned to trunk interface 1/1/2:

switch(config)# interface 1/1/2
switch(config-if)# no vlan trunk native 20 tag

Enabling tagging on native VLAN 20 assigned to LAG trunk interface 2:

switch(config)# interface lag 2
switch(config-if)# no routing
switch(config-lag-if)# vlan trunk native 20
switch(config-lag-if)# vlan trunk native 20 tag

voice

Syntax

voice

no voice

Description

Configures a VLAN as a voice VLAN.

The no form of this command removes voice configuration from a VLAN.

Command context

config-vlan-<VLAN-ID>

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring VLAN 10 as a voice VLAN:

switch(config)# vlan 10
switch(config-vlan-10)# voice

Removing voice from VLAN 10:

switch(config-vlan-10)# no voice

48

AOS-CX 10.06 Layer 2 Bridging Guide

Chapter 5
Loop protection

In cases where spanning tree protocols cannot be used to prevent loops at the edge of the network, loop
protection may provide a suitable alternative. Loop protection can find loops in untagged layer 2 links, as
well as on tagged VLANs.

The cases where loop protection might be chosen ahead of spanning tree to detect and prevent loops are:

• On ports with client authentication: When spanning tree is enabled on a switch that uses 802.1X, web
authentication, or MAC authentication, loops may go undetected. For example, spanning tree packets
that are looped back to an edge port will not be processed because they have a different broadcast/
multicast MAC address from the client-authenticated MAC address. To ensure that client-authenticated
edge ports get blocked when loops occur, you should enable loop protection on those ports.

• On ports connected to unmanaged devices: Spanning tree cannot detect the formation of loops where
there is an unmanaged device on the network that does not process spanning tree packets and simply
drops them. Loop protection has no such limitation, and can be used to prevent loops on unmanaged
switches.

Loop protection finds loops by sending loop protection packets on each port, LAG, or VLAN on which loop
protection is enabled. If a loop protection packet is received by the same switch that sent it, it indicates a
loop exists and one of the following actions is taken:

• Discovery of the loop is logged but port states are not changed.

• The sending port is disabled.

• The sending and receiving ports are both disabled.

Chapter 5 Loop protection

49

Interaction with other protocols.

• When loop protection is enabled before STP, and if there is an L2 loop, then the loop will be detected and

the port will be disabled.

• When STP is enabled before loop protection, and if there is a L2 loop, then the port will be moved to the
blocked state by STP. When a port is blocked, the loop protection packet will not reach the sending
switch, and the loop will not be detected by loop protection. When multiple instances of STP are
configured and different spanning trees are formed for different instances, the PSPO state will be
forwarding. In this case, loop- protection will consider those ports as normal forwarding ports and will
override the STP states.

• STP is mutually exclusive with loop protection. If STP and loop protection are both enabled on the same

VLAN, STP takes precedence. This means that loop protection does not take any action on a port blocked
by STP.

• MVRP and the loop protection interoperate with each other. However, dynamic VLANs cannot be tagged
to a port through user configuration. Therefore, it is not possible to configure a dynamic VLAN as a loop
protection enabled VLAN.

•

If MCLAG has marked a port as transmit disable (mclag_pdu_tx_disable is set to true), then loop-
protect will not transmit packets on the port. Similarly, if the loop_detect_source column is set to
mclag then loop protection will not re-enable the port when the re-enable timer expires on that port.

Configuring loop protection

Procedure

1. Enable loop protection on each layer 2 interface (port, LAG, or VLAN) for which loop protection is needed,

with the commands loop-protect and loop-protect vlan.

2. Define the action to be taken when a loop is detected with the command loop-protect action. The
default action is tx-disable, which means that the port that transmitted the loop detection packet is
disabled. When this action is enabled, environments with N loops must have loop protection configured
on at least N-1 ports to ensure a loop free topology.

NOTE: When the default action (tx-disable) is used, it is optional to enable loop protect in
all interfaces. By enabling loop protect in a single interface, the loop is detected and the
default action is executed. So when the packet from a loop protect-enabled port is received
back on an interface where loop protect is not enabled, the loop protect receiver action
corresponding to the receiving interface is executed. Please note that all the L2 ports will
have a default receiver action of tx-disable even when loop protect is not enabled.

3. If required, change the interval at which loop protection messages are sent with the command loop-

protect transmit-interval.

4. If required, change the length of time the switch waits before re-enabling an interface with the command

loop-protect re-enable-timer.

5. Review loop protection configuration settings with the command show loop-protect.

Example

This example creates the following configuration:

50

AOS-CX 10.06 Layer 2 Bridging Guide

• Enables loop protection on data port 1/1/1 and sets the loop detection action to disable the transmit

port.

• Enables loop protection on LAG 25 and sets the loop detection action to disable both transmit and

receive ports.

• Enables loop protection on VLANs 100-125 and 200.

• Sets the re-enable timer to 10 seconds.

• Sets the transmit-interval to 30 seconds.

switch(config)# interface 1/1/1
switch(config-if)# no routing

switch(config-if)# loop-protect
switch(config-if)# loop-protect action tx-disable
switch(config-if)# exit
switch(config)# interface lag 25
switch(config-lag-if)# loop-protect
switch(config-if)# loop-protect action tx-rx-disable
switch(config-if)# loop-protect vlan 100-125,200
switch(config-if)# exit
switch(config)# loop-protect re-enable-timer 30
switch(config)# exit
switch#  show loop-protect

Status and Counters - Loop Protection Information

Transmit Interval             : 30 (sec)
Port Re-enable Timer          : 10 (sec)

Interface 1/1/1
  Loop-protect enabled        : Yes
  Loop-Protect enabled VLANs  :
  Action on loop detection    : TX disable
  Loop detected count         : 0
  Loop detected               : No
  Interface status            : up

Interface lag 25
  Loop-protect enabled        : Yes
  Loop-Protect enabled VLANs  : 100-125,200
  Action on loop detection    : TX-RX disable
  Loop detected count         : 0
  Loop detected               : No
  Interface status            : up

Loop protect commands

loop-protect

Syntax

loop-protect

no loop-protect

Chapter 5 Loop protection

51

Description

Enables loop protection on a layer 2 interface or LAG. Loop protection packets are sent/received on the LAG
and not the interface which are members of the LAG. Loop protection only works on layer 2 interfaces. If a
layer 2 interface is changed to a layer 3 interface, all loop protection configuration settings are lost for that
interface.

The no form of this command disables loop protection on a layer 2 interface or LAG.

Command context

config-if

config-lag-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling loop protection on interface 1/1/1:

switch# config
switch(config)# interface 1/1/1
switch(config-if)# no routing
switch(config-if)# loop-protect

Enabling loop protection on LAG 25:

switch# config
switch(config)# interface lag 25
switch(config-lag-if)# no routing
switch(config-lag-if)# loop-protect

loop-protect action

Syntax

loop-protect action {do-not-disable | tx-disable | tx-rx-disable}

no loop-protect action {do-not-disable | tx-disable | tx-rx-disable}

Description

Sets the action to be taken when a loop protection packet is received on a port.

If an action is configured after a loop is detected, then the new action only takes effect after the re-enable
timer expires. To have the action take effect immediately, disable and then re-enable loop protect.

The no form of this command resets the action to the default (tx-disable).

Command context

config-if

Parameters
do-not-disable

No ports are disabled. On every transmit interval, the loop will be detected and the detection will be
reported via an SNMP trap and an event log message.

52

AOS-CX 10.06 Layer 2 Bridging Guide

tx-disable

The port that transmitted the loop detection packet is disabled. When this setting is enabled,
environments with N loops, must have loop protection be configured on at least N-1 ports to have a loop
free topology.Default.

tx-rx-disable

The ports that transmitted and received the loop detection packet are disabled.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config-if)# loop-protect action do-not-disable
switch(config-if)# no loop-protect action do-not-disable

loop-protect re-enable-timer

Syntax

loop-protect re-enable-timer <TIME>

no loop-protect re-enable-timer <TIME>

Description

Configures the time interval after which an interface disabled by loop protection is re-enabled. The loop
protection timer is disabled by default.

The no form of this command disables the loop protect timer.

Command context

config

Parameters
<TIME>

Specify the number of seconds after which a disabled interface is re-enabled. Range: 15 to 604800.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch# config
switch(config)# loop-protect re-enable-timer 60

loop-protect transmit-interval

Syntax

loop-protect transmit-interval <TIME>

no loop-protect transmit-interval [<TIME>]

Chapter 5 Loop protection

53

Description

Configures the time interval between successive loop protect packets sent on an interface.

The no form of this command sets the time interval to the default value of 5 seconds.

Command context

config

Parameters
<TIME>

Configures the transmit interval in seconds. Range: 5 to 10. Default: 5.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# loop-protect transmit-interval 10
switch(config)# no loop-protect transmit-interval

loop-protect trap loop-detected

Syntax

loop-protect trap loop-detected

no loop-protect trap loop-detected

Description

Enables sending SNMP traps for loop-protect related events.

The no form of this command disables sending SNMP traps for loop-protect related events.

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the sending of SNMP traps:

switch# loop-protect trap loop-detected

Disabling the sending of SNMP traps:

switch# no loop-protect trap loop-detected

54

AOS-CX 10.06 Layer 2 Bridging Guide

loop-protect vlan

Syntax

loop-protect vlan <VLAN-LIST>

no loop-protect vlan

Description

Specifies the trunk allowed VLANs on which loop protection packets are sent. By default, loop protection
packets are only sent on access VLANs and native VLANs on a port. To send loop protection packets on trunk
allowed VLANs, the VLANs must be explicitly added using this command.

Loop protection can be configured on a maximum of 4094 VLANs across all interfaces.

The no form of this command removes loop protection from all VLANs on the interface.

Command context

config-if

Parameters
<VLAN-LIST>

Specifies the number of a single VLAN, or a series of numbers for a range of VLANs, separated by
commas (1, 2, 3, 4), dashes (1-4), or both (1-4, 6).

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config-if)# loop-protect vlan 2-6,10,15-20

show loop-protect

Syntax

show loop-protect [<INTERFACE-NAME>] [vsx-peer]

Description

Shows loop protection information for all interfaces or for a specific interface.

Command context

Operator (>) or Manager (#)

Parameters
<INTERFACE-NAME>

Specifies the name of a logical interface on the switch. This can be one of the following:

• An Ethernet interface associated with a physical port. Format: member/slot/port.

• A LAG (link aggregation group). Specify the ID of LAG . For example: lag100.

Chapter 5 Loop protection

55

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show loop-protect

Transmit Interval (sec)            : 5
Port Re-enable Timer (sec)         : Disabled
Loop Detected Trap                 : Enabled

Interface 1/1/1
  Loop-protect enabled        : Yes
  Loop-Protect enabled VLANs  :
  Action on loop detection    : TX disable
  Loop detected count         : 0
  Loop detected               : No
  Interface status            : up

Interface 1/1/2
  Loop-protect enabled        : Yes
  Loop-Protect enabled VLANs  :
  Action on loop detection    : TX disable
  Loop detected count         : 0
  Loop detected               : No
  Interface status            : up

switch# show loop-protect 1/1/3

Status and Counters - Loop Protection Information

Transmit Interval (sec)       : 5
Port Re-enable Timer (sec)    : 0
Loop Detected Trap            : Disabled

Interface 1
  Loop-protect enabled        : Yes
  Loop-Protect enabled VLANs  :
  Action on loop detection    : TX disable
  Loop detected count         : 0
  Loop detected               : No
  Interface status            : up

56

AOS-CX 10.06 Layer 2 Bridging Guide

Chapter 6
Spanning tree protocols

Spanning tree protocols eliminate loops in a physical link-redundant network by selectively blocking
redundant links and putting them in a standby state.

Recent versions of STP include the Rapid Per-VLAN Spanning Tree Protocol (RPVST+) and the Multiple
Spanning Tree Protocol (MSTP).

Comparing spanning tree options
Without spanning tree, having more than one active path between a pair of network devices causes loops in
the network that can result in duplication of messages, leading to a broadcast storm that can bring down
the network.

The 802.1D spanning tree protocol operates without regard to a network's VLAN configuration, and
maintains one common spanning tree throughout a bridged network. This protocol maps one loop-free,
logical topology onto a given physical topology, resulting in the least optimal link utilization and longest
convergence times.

The 802.1s multiple spanning tree protocol (MSTP) uses multiple spanning tree instances with separate
forwarding topologies. Each instance is composed of one or more VLANs. This significantly improves
network link utilization and the speed of reconvergence after a failure in the network’s physical topology.
However, MSTP requires more configuration overhead and is more susceptible to dropped traffic due to
misconfiguration.

Rapid spanning tree protocol (RSTP) requires less configuration overhead, provides faster convergence on
point-to- point links, and speedier failure recovery with predetermined, alternative paths. RPVST+ was
introduced as an enhancement to Rapid spanning tree Protocol (RSTP) to improve the link utilization issue
and require less configuration overhead. Basically, RPVST+ is RSTP operating per-VLAN in a single layer 2
domain. VLAN tagging is applied to the ports in a multi-VLAN network to enable blocking of redundant links
in one VLAN, while allowing forwarding over the same links for nonredundant use by another VLAN. Each
RPVST+ tree can have a different root switch and therefore can span through different links. Since different
VLAN traffic can take different active paths from multiple possible topologies, overall network utilization
increases.

Preparing for spanning tree configuration
Before configuring a spanning tree:

• Determine the spanning tree protocol to be used: RPVST+ or MSTP. RPVST+ is ideal in networks having

fewer than 100 VLANs. In networks having 100 or more VLANs, MSTP is the recommended spanning tree
choice due to the increased load on the switch CPU.

• Plan the device roles (the root bridge or leaf node) by adjusting instance priority.

When you configure spanning tree protocols, follow these guidelines:

Chapter 6 Spanning tree protocols

57

•

If MSTP is enabled on the switch, MSTP takes all MSTI information along with the packet. To advertise a
specific VLAN within the network through MSTP, make sure that the VLAN is mapped to an MSTI when
you configure the VLAN-to-instance table.

• STP is mutually exclusive with loop protection. If STP and loop protection are both enabled on the same

VLAN, STP takes precedence. This means that loop protection does not take any action on a port blocked
by STP.

• A switch running RPVST+ transmits IEEE spanning tree BPDUs. It interoperates with IEEE RSTP and MSTP
spanning tree regions, and opens or blocks links from these regions as needed to maintain a loop-free
topology with one physical path between regions. RPVST+ interoperates with RSTP and MSTP only on
VLAN 1.

• One spanning tree variant can be run on the switch at any given time. On a switch running RPVST+, MSTP
cannot be enabled. However, any MSTP-specific configuration settings in the startup configuration file
will be maintained.

• The following features cannot run concurrently with RPVST+:

◦

◦

Features that dynamically assign ports to VLANs: MVRP, RADIUS-based VLAN assignments (802.1X,
WebAuth, MKA:C auth), and MAC-based VLANs.

Filter multicast in RPVST+ mode (The multicast MAC address value cannot be set to the PVST MAC
address 01:00:0c:cc:cc:cd.)

• Spanning tree mode cannot be set to RPVST+ when GVRP or MVRP is enabled. GVRP or MVRP cannot be

enabled when RPVST+ is enabled.

• Configurations made on an aggregation member port can take effect only after the port is removed from

the aggregation group.

• After you enable a spanning tree protocol on a layer 2 aggregate interface, the system performs

spanning tree calculation on the layer 2 aggregate interface. It does not perform the spanning tree
calculation on the aggregation member ports. The spanning tree protocol enable state and forwarding
state of each selected member port is consistent with the state of the corresponding layer 2 aggregate
interface.

• The member ports of an aggregation group do not participate in spanning tree calculations. However, the

ports reserve their spanning tree configurations for participation in spanning tree calculations after
leaving the aggregation group.

STP
Spanning tree protocol (STP) was developed based on the 802.1d standard of IEEE to eliminate loops at the
data link layer in a LAN. Networks often have redundant links as backups in case of failures, but loops are a
very serious problem. Devices running STP detect loops in the network by exchanging information with one
another. They eliminate loops by selectively blocking certain ports to prune the loop structure into a loop-
free tree structure. This avoids proliferation and infinite cycling of packets that would occur in a loop
network.

In a narrow sense, STP refers to IEEE 802.1d STP. In a broad sense, STP refers to the IEEE 802.1d STP and
various enhanced spanning tree protocols derived from that protocol, such as RPVST and MSTP.

STP protocol packets

STP uses bridge protocol data units (BPDUs), also known as configuration messages, as its protocol packets.
STP-enabled network devices exchange BPDUs to establish a spanning tree.

58

AOS-CX 10.06 Layer 2 Bridging Guide

STP uses the following types of BPDUs:

• Configuration BPDUs: Used by the network devices to calculate a spanning tree and maintain the

spanning tree topology.

• Topology change notification (TCN) BPDUs: Use to notify network devices of network topology changes.

Configuration BPDUs contain sufficient information for network devices to complete spanning tree
calculation. Important fields in a configuration BPDU include the following:

• Root bridge ID: Priority and MAC address of the root bridge.

• Root path cost: Cost of the path to the root bridge indicated by the root identifier from the transmitting

bridge.

• Designated bridge ID: Priority and MAC address of the designated bridge.

• Designated port ID: Priority and global port number of the designated port.

• Message age: Age of the configuration BPDU while it propagates in the network.

• Max age: Maximum age of the configuration BPDU stored on the switch.

• Hello time: Configuration BPDU transmission interval.

•

Forward delay: Delay that STP bridges use to transit port state.

STP key concepts

Root bridge

A tree network must have a root bridge. The entire network contains only one root bridge, and all the other
bridges in the network are called leaf nodes. The root bridge is not permanent, but can change with changes
of the network topology.

Upon initialization of a network, each device generates and periodically sends configuration BPDUs, with
itself as the root bridge. After network convergence, only the root bridge generates and periodically sends
configuration BPDUs. The other devices only forward the BPDUs.

Root port

On a non-root bridge, the port which has the least cost to reach the boot bridge is the root port.

The root port communicates with the root bridge. Each non-root bridge has only one root port. The root
bridge has no root port.

Designated bridge and designated port

The designated bridge:

•

•

For a device: Device directly connected with the local device and responsible for forwarding BPDUs to the
local device.

For a LAN: Device responsible for forwarding BPDUs to this LAN segment.

The designated port:

Chapter 6 Spanning tree protocols

59

•

•

For a device: Port through which the designated bridge forwards BPDUs to this device.

For a LAN: Port through which the designated bridge forwards BPDUs to this LAN segment.

In the following topology, Device B and Device C are directly connected to a LAN.

If Device A forwards BPDUs to Device B through port A1, the designated bridge and designated port are as
follows:

• The designated bridge for Device B is Device A.

• The designated port of Device B is port A1 on Device A.

If Device B forwards BPDUs to the LAN, the designated bridge and designated port are as follows:

• The designated bridge for the LAN is Device B.

• The designated port for the LAN is port B2 on Device B.

Path cost

Path cost is a reference value used for link selection in STP. To prune the network into a loop-free tree, STP
calculates path costs to select the most robust links and block redundant links that are less robust.

STP timers

The most important timing parameters in STP calculation are forward delay, hello time, and max age.

•

Forward delay: Forward delay is the delay time for port state transition. A path failure can cause spanning
tree recalculation to adapt the spanning tree structure to the change. However, the resulting new
configuration BPDU cannot propagate throughout the network immediately. If the newly elected root
ports and designated ports start to forward data immediately, a temporary loop will likely occur. The

60

AOS-CX 10.06 Layer 2 Bridging Guide

newly elected root ports or designated ports require twice the forward delay time before they transit to
the forwarding state. This allows the new configuration BPDU to propagate throughout the network.

• Hello time: The device sends hello packets at the hello time interval to the neighboring devices to make

sure the paths are fault-free.

• Max age: The device uses the max age to determine whether a stored configuration BPDU has expired

and discards it if the max age is exceeded.

BPDU forwarding mechanism

The configuration BPDUs of STP are forwarded according to these guidelines:

• Upon network initiation, every device regards itself as the root bridge and generates configuration BPDUs

with itself as the root. Then it sends the configuration BPDUs at a regular hello interval.

•

If the root port received a configuration BPDU superior to the configuration BPDU of the port, the device
performs the following tasks:

◦

Increases the message age carried in the configuration BPDU.

◦ Starts a timer to time the configuration BPDU.

◦ Sends this configuration BPDU through the designated port.

•

•

If a designated port receives a configuration BPDU with a lower priority than its configuration BPDU, the
port immediately responds with its configuration BPDU.

If a path fails, the root port on this path no longer receives new configuration BPDUs and the old
configuration BPDUs will be discarded due to timeout. The device generates a configuration BPDU with
itself as the root and sends the BPDUs and TCN BPDUs. This triggers a new spanning tree calculation
process to establish a new path to restore the network connectivity.

However, the newly calculated configuration BPDU cannot be propagated throughout the network
immediately. As a result, the old root ports and designated ports that have not detected the topology
change continue forwarding data along the old path. If the new root ports and designated ports begin to
forward data as soon as they are elected, a temporary loop might occur.

STP calculation

Simplified calculation overview

A tree-shape topology forms once the root bridge, root ports, and designated ports are selected.

1. Upon initialization of a device, each port generates a BPDU with the following contents:

• The port as the designated port.

• The device as the root bridge.

• 0 as the root path cost.

• The device ID as the designated bridge ID.

2. Initially, each STP-enabled device on the network assumes itself to be the root bridge, with its own device
ID as the root bridge ID. By exchanging configuration BPDUs, the devices compare their root bridge IDs to
elect the device with the smallest root bridge ID as the root bridge.

3. Root port and designated ports selection on the non-root bridges.

Chapter 6 Spanning tree protocols

61

• A non-root–bridge device regards the port on which it received the optimum configuration BPDU as

the root port.

◦ Upon receiving a configuration BPDU on a port, the device compares the priority of the received
configuration BPDU with that of the configuration BPDU generated by the port. If the former
priority is lower, the device discards the received configuration BPDU and keeps the configuration
BPDU the port generated. If the former priority is higher, the device replaces the content of the
configuration BPDU generated by the port with the content of the received configuration BPDU.

◦ The device compares the configuration BPDUs of all the ports and chooses the optimum

configuration BPDU.

• Based on the configuration BPDU and the path cost of the root port, the device calculates a

designated port configuration BPDU for each of the other ports.

◦ The root bridge ID is replaced with that of the configuration BPDU of the root port.

◦ The root path cost is replaced with that of the configuration BPDU of the root port plus the path

cost of the root port.

◦ The designated bridge ID is replaced with the ID of this device.

◦ The designated port ID is replaced with the ID of this port.

• The device compares the calculated configuration BPDU with the configuration BPDU on the port

whose port role will be determined, and acts depending on the result of the comparison:

◦

◦

If the calculated configuration BPDU is superior, the device performs the following tasks:

– Considers this port as the designated port.

– Replaces the configuration BPDU on the port with the calculated configuration BPDU.

– Periodically sends the calculated configuration BPDU.

If the configuration BPDU on the port is superior, the device blocks this port without updating its
configuration BPDU. The blocked port can receive BPDUs, but cannot send BPDUs or forward data
traffic.

When the network topology is stable, only the root port and designated ports forward user traffic. Other
ports are all in the blocked state to receive BPDUs but not to forward BPDUs or user traffic.

4. The principles of configuration BPDU comparison:

• The configuration BPDU with the lowest root bridge ID has the highest priority.

•

•

If configuration BPDUs have the same root bridge ID, their root path costs are compared. For example,
the root path cost in a configuration BPDU plus the path cost of a receiving port is S. The configuration
BPDU with the smallest S value has the highest priority.

If all configuration BPDUs have the same root bridge ID and S value, the following attributes are
compared in sequence: Designated bridge IDs, Designated port IDs, and IDs of the receiving ports.

The configuration BPDU that contains a smaller designated bridge ID, designated port ID, or receiving
port ID is selected.

Calculation example

The following topology is used to illustrate an STP calculation. The priority values of Device A, Device B, and
Device C are 0, 1, and 2, respectively. The path costs of links among the three devices are 5, 10, and 4.

62

AOS-CX 10.06 Layer 2 Bridging Guide

Each configuration BPDU contains the following fields: root bridge ID, root path cost, designated bridge ID,
and designated port ID.
1. The initial state of the BPDUs on each device is:
| Device   | Port name | Configuration BPDU on the port |
| -------- | --------- | ------------------------------ |
| Device A | Port A1   | {0, 0, 0, Port A1}             |
|          | Port A2   | {0, 0, 0, Port A2}             |
| Device B | Port B1   | {1, 0, 1, Port B1}             |
|          | Port B2   | {1, 0, 1, Port B2}             |
| Device C | Port C1   | {2, 0, 2, Port C1}             |
|          | Port C2   | {2, 0, 2, Port C2}             |
2. BPDU comparison on each device occurs as follows:
Chapter 6 Spanning tree protocols 63

Configuration BPDU
on ports after
comparison

• Port A1: {0, 0, 0,

Port A1}

• Port A2: {0, 0, 0,

Port A2}

Device

Comparison process

Device A

Port A1 performs the following tasks:

a. Receives the configuration BPDU of Port B1 {1, 0, 1, Port

B1}.

b. Determines that its existing configuration BPDU {0, 0, 0, Port

A1} is superior to the received configuration BPDU.

c. Discards the received one.

Port A2 performs the following tasks:

a. Receives the configuration BPDU of Port C1 {2, 0, 2, Port

C1}.

b. Determines that its existing configuration BPDU {0, 0, 0, Port

A2} is superior to the received configuration BPDU.

c. Discards the received one.

Device A determines that it is both the root bridge and
designated bridge in the configuration BPDUs of all its ports. It
considers itself as the root bridge. It does not change the
configuration BPDU of any port and starts to periodically send
configuration BPDUs.

• Port B1: {0, 0, 0,

Port A1}

• Port B2: {1, 0, 1,

Port B2}

Device B

Port B1 performs the following tasks:

a. Receives the configuration BPDU of Port A1 {0, 0, 0, Port

A1}.

b. Determines that the received configuration BPDU is

superior to its existing configuration BPDU {1, 0, 1, Port B1}.

c. Updates its configuration BPDU.

Port B2 performs the following tasks:

a. Receives the configuration BPDU of Port C2 {2, 0, 2, Port

C2}.

b. Determines that its existing configuration BPDU {1, 0, 1,Port

B2} is superior to the received configuration BPDU.

c. Discards the received BPDU.

Table Continued

64

AOS-CX 10.06 Layer 2 Bridging Guide

Device B performs the following tasks:

a. Compares the configuration BPDUs of all its ports.

b. Decides that the configuration BPDU of Port B1 is the

optimum.

• Root port (Port B1):
{0, 0, 0, Port A1}

• Designated port
(Port B2): {0, 5, 1,
Port B2}

c. Selects Port B1 as the root port with the configuration BPDU

unchanged.

Based on the configuration BPDU and path cost of the root
port, Device B calculates a designated port configuration BPDU
for Port B2 {0, 5, 1, Port B2}. Device B compares it with the
existing configuration BPDU of Port B2 {1, 0, 1, Port B2}.

Device B determines that the calculated one is superior, and
determines that Port B2 is the designated port. It replaces the
configuration BPDU on Port B2 with the calculated one, and
periodically sends the calculated configuration BPDU.

Device C

Port C1 performs the following tasks:

a. Receives the configuration BPDU of Port A2 {0, 0, 0, Port

A2}.

b. Determines that the received configuration BPDU is

superior to its existing configuration BPDU {2, 0, 2, Port C1}.

c. Updates its configuration BPDU.

Port C2 performs the following tasks:

a. Receives the original configuration BPDU of Port B2 {1, 0,1,

Port B2}.

b. Determines that the received configuration BPDU is

superior to the existing configuration BPDU {2, 0, 2, Port
C2}.

c. Updates its configuration BPDU.

• Port C1: {0, 0, 0,

Port A2}

• Port C2: {1, 0, 1,

Port B2}

Table Continued

Chapter 6 Spanning tree protocols

65

Device C performs the following tasks:

a. Compares the configuration BPDUs of all its ports.

b. Decides that the configuration BPDU of Port C1 is the

optimum.

• Root port (Port C1):
{0, 0, 0, Port A2}

• Designated port

(Port C2): {0, 10, 2,
Port C2}

c. Selects Port C1 as the root port with the configuration BPDU

unchanged.

Based on the configuration BPDU and path cost of the root
port, Device C calculates the configuration BPDU of Port C2 {0,
10, 2, Port C2}. Device C compares it with the existing
configuration BPDU of Port C2 {1, 0, 1, Port B2}.

Device C determines that the calculated configuration BPDU is
superior to the existing one, selects Port C2 as the designated
port, and replaces the configuration BPDU of Port C2 with the
calculated one.

Table Continued

66

AOS-CX 10.06 Layer 2 Bridging Guide

Port C2 performs the following tasks:

a. Receives the configuration BPDU of Port B2 {0, 5, 1, Port

B2}.

b. Determines that the received configuration BPDU is

superior to its existing configuration BPDU {0, 10, 2, Port
C2}.

• Port C1: {0, 0, 0,

Port A2}

• Port C2: {0, 5, 1,

Port B2}

c. Updates its configuration BPDU.

Port C1 performs the following tasks:

a. Receives a periodic configuration BPDU {0, 0, 0, Port A2}

from Port A2.

b. Determines that it is the same as the existing configuration

BPDU.

c. Discards the received BPDU.

Device C determines that the root path cost of Port C1 (10)
(root path cost of the received configuration BPDU (0) plus path
cost of Port C1 (10)) is larger than that of Port C2 (9) (root path
cost of the received configuration BPDU (5) plus path cost of
Port C2 (4)). Device C determines that the configuration BPDU
of Port C2 is the optimum, and selects Port C2 as the root port
with the configuration BPDU unchanged.

• Blocked port (Port
C1): {0, 0, 0, Port
A2}

• Root port (Port C2):
{0, 5, 1, Port B2}

Based on the configuration BPDU and path cost of the root
port, Device C performs the following tasks:

a. Calculates a designated port configuration BPDU for Port C1

{0, 9, 2, Port C1}.

b. Compares it with the existing configuration BPDU of Port C1

{0, 0, 0, Port A2}.

c. Determines that the existing configuration BPDU is superior

to the calculated one and blocks Port C1 with the
configuration BPDU unchanged.

Port C1 does not forward data until a new event triggers a
spanning tree calculation process: for example, the link
between Device B and Device C is down.

3. After the comparison, a spanning tree with Device A as the root bridge is established as shown:

Chapter 6 Spanning tree protocols

67

RPVST+
Rapid Per VLAN Spanning Tree+ (RPVST+) is an updated implementation of STP (Spanning Tree Protocol). It
enables the creation of a separate spanning tree for each VLAN on a switch, and ensures that only one
active, loop-free path exists between any two nodes on a given VLAN.

Spanning tree protocols are used to prevent loops from occurring when multiple paths exist between the
devices on a network. They are also used to provide redundancy, enabling data to use an alternative path
when one link to a device fails. For example, in the following topology several paths exist between each
switch.

The topology has four switches running RSTP. Switch “A” is the root switch. To prevent a loop, RSTP blocks
the link between switch “B” and switch “D”. There are two VLANs in this network (VLAN 10 and VLAN 20).
Since RSTP does not have VLAN intelligence, it forces all VLANs in a layer 2 domain to follow the same
spanning tree.

There will not be any traffic through the link between switch “B” and switch “D” and therefore the link
bandwidth is wasted. On the other hand, RPVST+ runs different spanning trees for different VLANs.

RVPST+ creates a spanning tree for VLAN 10.

68

AOS-CX 10.06 Layer 2 Bridging Guide

RVPST+ creates another spanning tree for VLAN 20.

The two topologies above are the same as the first topology, but now the switches run RPVST+ and can span
different trees for different VLANs. Switch A is the root switch for the VLAN 10 spanning tree and switch D is
the root switch for the VLAN 20 spanning tree. The link between switch B and switch D is only blocked for
VLAN 10 traffic but VLAN 20 traffic goes through that link. Similarly the link between switch A and switch C is
blocked only for VLAN 20 traffic but VLAN 10 traffic goes through that link. Here, traffic passes through all
the available links, and network availability and bandwidth utilization increase.

The following figure shows a further example of shared links and redundant path-blocking in a network
running RPVST+.

Chapter 6 Spanning tree protocols

69

In the factory default configuration, spanning tree operation is disabled. Configuring the spanning tree
mode as RPVST+ on a switch and then enabling spanning tree automatically creates a spanning tree
instance for each VLAN on the switch. Configuration with default settings is automatic, and in many cases
does not require any adjustments. This includes operation with spanning tree regions in your network
running STP, MSTP, or RSTP.

Also, the switch retains its currently configured spanning tree parameter settings when spanning tree is
disabled. Thus, if you disable, then later re-enable spanning tree, the parameter settings will be the same as
before spanning tree was disabled.

RPVST+ interoperates with devices that run legacy IEEE 802.1D STP.

RPVST+ applies one RSTP tree per-VLAN. Each of these RSTP trees can have a different root switch and span
the network through shared or different links.

NOTE: The switch automatically senses port identity and type, and automatically defines
spanning tree parameters for each type, and parameters that apply across the switch. Although
these parameters can be adjusted, HPE strongly recommends leaving these settings in their
default configurations unless the proposed changes have been supplied by an experienced
network administrator who has a strong understanding of RPVST+ operation.

The 6300 switch supports 64 RPVST instances. All other platforms support 254 RPVST instances.

Configuring RPVST+

Procedure

1. Set RPVST+ as the spanning tree mode with the command spanning-tree mode rpvst.

2. Enable spanning tree with the command spanning-tree.

3. For each layer 2 interface or LAG, configure the list of VLANs that are part of the spanning tree with the

command spanning-tree vlan.

4. Set the cost and priority for each VLAN with the commands spanning-tree vlan cost and

spanning-tree vlan port-priority.

5. For most deployments, the default values for the following settings do not need to be changed. If your

deployment requires different settings, change the default values with the indicated commands:

70

AOS-CX 10.06 Layer 2 Bridging Guide

RPVST+ setting

Default
value

Command to change it

Include VLAN ID in spanning tree packets.

Enabled.

spanning-tree extend-system-id

Block links when VLAN mismatch is detected. Disabled.

STP link type.

Point-to-
point.

spanning-tree ignore-pvid-
inconsistency

spanning-tree link-type

Support extended range of paths costs for
high-speed links.

Enabled.

spanning-tree pathcost-type

Propagate topology changes to other ports.

Disabled.

spanning-tree tcn-guard

6. Review RPVST+ configuration settings with the command show spanning tree.

Example

This example creates the following configuration:

• Sets the spanning tree mode to rpvst.

• Enables spanning tree.

• Defines spanning tree support for VLANs 2-5.

• Sets the priority for each VLAN.

switch# config
switch(config)# spanning-tree mode rpvst
switch(config)# spanning-tree
switch(config)# spanning-tree vlan 2-5
switch(config)# spanning-tree vlan 2 priority 5
switch(config)# spanning-tree vlan 3 priority 4
switch(config)# spanning-tree vlan 4 priority 3
switch(config)# spanning-tree vlan 5 priority 2
switch(config)# exit
switch# show spanning-tree

Spanning tree status      : Enabled Protocol: RPVST
Extended System-id        : Enabled
Ignore PVID Inconsistency : Disabled
Path cost method          : Long

VLAN2
  Root ID    Priority   : 20480
             MAC-Address: 70:72:cf:38:21:e5
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 20480
             MAC-Address: 70:72:cf:38:21:e5
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

Port         Role           State        Cost    Priority   Type
------------ -------------- ------------ ------- ---------- ----------
1/1/1        Designated     Forwarding   20000   128        point_to_point

Chapter 6 Spanning tree protocols

71

VLAN3
  Root ID    Priority   : 16384
             MAC-Address: 70:72:cf:38:21:e5
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 16384
             MAC-Address: 70:72:cf:38:21:e5
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

Port         Role           State        Cost    Priority   Type
------------ -------------- ------------ ------- ---------- ----------
1/1/1        Designated     Forwarding   20000   128        point_to_point

VLAN4
  Root ID    Priority   : 12288
             MAC-Address: 70:72:cf:38:21:e5
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 12288
             MAC-Address: 70:72:cf:38:21:e5
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

Port         Role           State        Cost    Priority   Type
------------ -------------- ------------ ------- ---------- ----------
1/1/1        Designated     Forwarding   20000   128        point_to_point

VLAN5
  Root ID    Priority   : 8192
             MAC-Address: 70:72:cf:38:21:e5
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 8192
             MAC-Address: 70:72:cf:38:21:e5
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

Port         Role           State        Cost    Priority   Type
------------ -------------- ------------ ------- ---------- ----------
1/1/1        Designated     Forwarding   20000   128        point_to_point

Viewing RPVST+ information

Prerequisites

These commands are in the manager context, as indicated by the switch# prompt.

Procedure

1. To view various aspects of RPVST+ information, use the following commands. For command details and

examples, click the links.

• To view information on spanning-tree mode and the RPVST+ instances, use:

72

AOS-CX 10.06 Layer 2 Bridging Guide

show spanning-tree

• To view information on spanning-tree mode and the RPVST+ instance of a specific VLAN, use:

show spanning-tree vlan

• To view a summary of the spanning-tree configurations related to a port, use:

show spanning-tree summary port

• To view a summary of the spanning-tree configurations, use:

show spanning-tree summary root

RPVST+ scenario

In this scenario, four switches are interconnected. VLANs 10 and 20 are defined on all switches, causing a
network loop.

To eliminate the loop, RPVST+ is enabled and switch A and B are defined as high-priority for VLAN 10 and 20
respectively. RPVST+ then eliminates the loop by assigning switch A as the root for VLAN 10 and switch B
designated as the root for VLAN 20, and blocking access on one of the links.

Chapter 6 Spanning tree protocols

73

Procedure

1. Configure switch A.

a. Create VLANs 1, 10, and 20.

switch# config
switch(config)# vlan 1, 10, 20

b. Enable RPVST+ and assign the VLANs 10 and 20 to it. Assign a priority of 5 to VLAN 10. This will force

switch A to become the root of the spanning tree for VLAN 10.

switch(config)# spanning-tree mode rpvst
switch(config)# spanning-tree
switch(config)# spanning-tree vlan 10,20
switch(config)# spanning-tree vlan 10 priority 5

c. Define interfaces 1/1/1 and 1/1/2.

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all

2. Configure switch B and switch C with the same settings.

a. Create VLANs 1, 10, and 20.

switch# config
switch(config)# vlan 1, 10, 20

b. Enable RPVST+ and assign the VLANs 10 and 20 to it.

switch(config)# spanning-tree mode rpvst
switch(config)# spanning-tree
switch(config)# spanning-tree vlan 10,20

c. Define interfaces 1/1/1 and 1/1/2.

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all

3. Configure switch D.

74

AOS-CX 10.06 Layer 2 Bridging Guide

a. Create VLANs 1, 10, and 20.

switch# config
switch(config)# vlan 1, 10, 20

b. Enable RPVST+ and assign the VLANs 10 and 20 to it. Assign a priority of 5 to VLAN 20. This will force

switch D to become the root of the spanning tree for VLAN 20.

switch(config)# spanning-tree mode rpvst
switch(config)# spanning-tree
switch(config)# spanning-tree vlan 10,20
switch(config)# spanning-tree vlan 20 priority 5

c. Define interfaces 1/1/1 and 1/1/2.

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all

RPVST+ commands

show spanning-tree

Syntax

show spanning-tree [detail] [vsx-peer]

Description

Shows the spanning tree mode and information on the RPVST instances and optionally shows details on the
RPVST instances.

Command context

Operator (>) or Manager (#)

Parameters
detail

Specifies showing details on the RPVST instances.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Chapter 6 Spanning tree protocols

75

Examples

Showing spanning tree mode and RPVST instance information:

switch# show spanning-tree
Spanning tree status           : Enabled Protocol: RPVST
Extended System-id             : Enabled
Ignore PVID Inconsistency      : Enabled
Path cost method               : Long
RPVST-MSTP Interconnect VLAN   : 1
VLAN1
  Root ID    Priority   : 32768
             MAC-Address: 70:72:cf:31:c9:23
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 32768
             MAC-Address: 70:72:cf:31:c9:23
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

Showing spanning tree mode and detailed RPVST instance information:

switch# show spanning-tree detail
Spanning tree status           : Enabled Protocol: RPVST
Extended System-id             : Enabled
Ignore PVID Inconsistency      : Enabled
Path cost method               : Long
RPVST-MSTP Interconnect VLAN   : 1

VLAN1
  Root ID    Priority   : 32768
             MAC-Address: 70:72:cf:31:c9:23
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 32768
             MAC-Address: 70:72:cf:31:c9:23
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag : False
Number of topology changes : 1
Last topology change occurred : 33293 seconds ago

Port 1/1/1
Designated Root Priority                  : 32768          Address: 48:0F:CF:AF:22:1D
Designated Bridge Priority                : 32768          Address: 48:0F:CF:AF:22:1D
Designated Port                           : 1/1/1
Forwarding-State transitions              : 0
BPDUs sent 1582, received 1506
TCN_Tx: 10, TCN_Rx: 10

Port lag1
Designated Root Priority                  : 32768          Address: 48:0F:CF:AF:22:1D
Designated Bridge Priority                : 32768          Address: 48:0F:CF:AF:22:1D

76

AOS-CX 10.06 Layer 2 Bridging Guide

Designated Port                           : lag1
Forwarding-State transitions              : 0
BPDUs sent 1402, received 1316
TCN_Tx: 10, TCN_Rx: 10
Multi-chassis role                        : active

show spanning-tree inconsistent-ports

Syntax

show spanning-tree inconsistent-ports [vlan <VLAN-ID>]

Description

Shows ports blocked by STP protection functions such as Root guard, Loop guard, BPDU guard, and RPVST
guard.

Command context

Operator (>) or Manager (#)

Parameters

<VLAN-ID>

Specifies a VLAN ID number.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing inconsistent port information:

switch# show spanning-tree inconsistent-ports
VLAN ID      Blocked Port   Reason
------------ -------------- ------------
1            1/1/1          BPDU Guard
2            1/1/1          BPDU Guard
3            1/1/1          BPDU Guard
4            1/1/1          BPDU Guard
5            1/1/1          BPDU Guard
6            1/1/1          BPDU Guard
7            1/1/1          BPDU Guard
8            1/1/1          BPDU Guard
9            1/1/1          BPDU Guard
10           1/1/1          BPDU Guard

Showing inconsistent port information for VLANs 1 to 4:

switch# show spanning-tree inconsistent-ports vlan 1-4
VLAN ID      Blocked Port   Reason
------------ -------------- ------------
1            1/1/3          Root Guard
2            1/1/7          BPDU Guard
3            1/1/9          Loop Guard
4            1/1/37         RPVST Guard

Chapter 6 Spanning tree protocols

77

show spanning-tree summary port

Syntax

show spanning-tree summary port

Description

Shows a summary of port-related spanning-tree configuration and status.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing a summary of port-related spanning tree information:

switch# show spanning-tree summary port

STP status                     : Enabled
Protocol                       : RPVST
BPDU guard timeout value       : None
BPDU guard enabled interfaces  : 1/1/1
BPDU filter enabled interfaces : None
Root guard enabled interfaces  : 1/1/3
Loop guard enabled interfaces  : 1/1/2
TCN guard enabled interfaces   : 1/1/1-1/1/3

Interface count by state

VLAN                   Blocking Listening Learning Forwarding
---------------------- -------- --------- -------- ----------
VLAN1                         0         0        0          1
VLAN2                         0         0        0          1
---------------------- -------- --------- -------- ----------
Total = 2                     0         0        0          2

show spanning-tree summary root

Syntax

show spanning-tree summary root

Description

Shows the summary of spanning tree root and configurations for all VLANs.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

78

AOS-CX 10.06 Layer 2 Bridging Guide

Example

Showing summary of spanning tree configurations:

switch# show spanning-tree summary root

STP status            : Enabled
Protocol              : RPVST
System ID             : 70:72:cf:32:50:f5

Root bridge for VLANs : 1,2

                                         Root Hello Max Fwd
VLAN     Priority Root ID                cost  Time Age Dly    Root Port
-------- -------- ----------------- --------- ----- --- --- ------------
VLAN1       32768 70:72:cf:32:50:f5         0     2  20  15          n/a
VLAN2       32768 70:72:cf:32:50:f5       200     2  20  15        1/1/1

show spanning-tree vlan

Syntax

show spanning-tree vlan <VLAN-ID> [detail] [vsx-peer]

Description

Displays the spanning tree mode and information on the RPVST instance of the specified VLAN and
optionally displays details on the RPVST instance for the VLAN.

Command context

Operator (>) or Manager (#)

Parameters
<VLAN-ID>

Specifies the number of a VLAN.

[detail]

Specifies displaying details on the RPVST instance for the VLAN.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing spanning tree mode and RPVST instance information for VLAN 2:

switch# show spanning-tree vlan 2
VLAN2
Spanning tree status: Enabled Protocol: RPVST
  Root ID    Priority   : 32768
             MAC-Address: 70:72:cf:76:43:2a
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

Chapter 6 Spanning tree protocols

79

Bridge ID  Priority  : 32768
             MAC-Address: 70:72:cf:76:43:2a
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

Showing spanning tree mode and detailed RPVST instance information for VLAN 2:

switch# show spanning-tree vlan 2 detail
VLAN2
Spanning tree status: Enabled Protocol: RPVST
  Root ID    Priority   : 32768
             MAC-Address: 70:72:cf:76:43:2a
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 32768
             MAC-Address: 70:72:cf:76:43:2a
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag : False
Number of topology changes : 1
Last topology change occurred : 33293 seconds ago

Port 1/1/1
Designated root has priority :32768 Address: 48:0f:cf:af:22:1d
Designated bridge has priority :32768 Address: 48:0f:cf:af:22:1d
Designated port :1
Number of transitions to forwarding state : 0
BPDUs sent 1582, received 1506
TCN_Tx: 10, TCN_Rx: 10

spanning-tree bpdu-guard timeout

Syntax

spanning-tree bpdu-guard timeout <INTERVAL>

no spanning-tree bpdu-guard timeout

Description

Enables and configures the auto re-enable timeout in seconds for all interfaces with BPDU guard enabled.
When an interface is disabled after receiving an unauthorized BPDU it will automatically be re-enabled after
the timeout expires. The default is for the interface to stay disabled until manually re-enabled.

The no form of the command disables BPDU guard timeout on the interface. This is the default.

Command context

config

80

AOS-CX 10.06 Layer 2 Bridging Guide

Parameters

<Interval>

Specifies the re-enable timeout in seconds. Range: 1 to 65535.

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling the BPDU guard timeout on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree bpdu-guard timeout 10

Disabling BPDU guard timeout on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree bpdu-guard

spanning-tree extend-system-id

Syntax

spanning-tree extend-system-id {enable | disable}

no spanning-tree extend-system-id

Description

Configures use of extended system ID. When enabled, the VLAN ID is included in spanning tree packets.
When disabled, the VLAN ID is set to NULL in the spanning tree packets.

By default, extended system ID is enabled. If you disable extended system ID, the bridge identifier field in
the spanning tree packet is filled with zeros.

The no form of this command disables extended system ID.

Command context

config

Parameters
enable

Specifies enabling use of extended system ID.

disable

Specifies disabling use of extended system ID.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling extended system ID:

switch# config
switch(config)# spanning-tree extend-system-id enable

Chapter 6 Spanning tree protocols

81

Disabling extended system ID:

switch# config
switch(config)# spanning-tree extend-system-id disable
switch(config)# no spanning-tree extend-system-id

spanning-tree ignore-pvid-inconsistency

Syntax

spanning-tree ignore-pvid-inconsistency {enable | disable}

no spanning-tree ignore-pvid-inconsistency

Description

Configures port behavior when per-VLAN ID inconsistencies are present. For example, when the ports on
both ends of a point-to-point link are untagged members of different VLANs, enabling this option allows
RPVST+ to process untagged RPVST+ packets belonging to the peer’s untagged VLAN as if they were received
on the current device’s untagged VLAN. When this option is disabled, RPVST+ blocks the link, causing traffic
on the mismatched VLANs to be dropped.

If this option is enabled on multiple switches connected by hubs, there could be more than two VLANs
involved in PVID mismatches that will be ignored by RPVST+.

If port VLAN memberships is misconfigured on a switch in the network, then enabling this option prevents
RPVST+ from detecting the problem, which may result in packet duplication in the network since RPVST+
would not converge correctly.

This command affects all ports on the switch belonging to VLANs on which RPVST+ is enabled.

By default ignore per-VLAN ID inconsistency is disabled.

The no form of this command sets the ignore per-VLAN ID inconsistencies to disabled.

Command context

config

Parameters
enable

Specifies ignore per-VLAN ID inconsistencies and allow RPVST to run on mismatched links.

disable

Disables the ignore per-VLAN ID inconsistencies functionality.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling ignore per-VLAN ID inconsistencies:

switch# config
switch(config)# spanning-tree ignore-pvid-inconsistency enable

Disabling ignore per-VLAN ID inconsistencies:

82

AOS-CX 10.06 Layer 2 Bridging Guide

switch# config
switch(config)# spanning-tree ignore-pvid-inconsistency disable
switch(config)# no spanning-tree ignore-pvid-inconsistency

spanning-tree link-type

Syntax

spanning-tree link-type {point-to-point | shared}

no spanning-tree link-type

Description

Configures the link type of a port.

The no form of this command sets the spanning tree link type to the default value of point-to-point.

Command context

config-if

Parameters
point-to-point

Sets the spanning tree link type as point-to-point. Use this for full-duplex ports that provide a point-to-
point link to devices such as a switch, bridge, or end-node. Default.

shared

Sets the spanning tree link type as shared. Use this when the port is connected to a hub.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting spanning tree link type to shared:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree link-type shared

Setting spanning tree link type to point-to-point for a port:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree link-type

spanning-tree mode

Syntax

spanning-tree mode {mstp|rpvst}

Description

Sets the spanning tree mode to either MSTP mode (Multiple-instance Spanning Tree Protocol) or RPVST
mode (Rapid Per VLAN Spanning Tree). If you want to change the spanning tree mode, you must first disable
spanning tree with the command no spanning-tree.

The no form of this command sets the spanning tree mode to the default value mstp.

Chapter 6 Spanning tree protocols

83

Command context

config

Parameters
mstp

Sets the mode to MSTP (Multiple-instance Spanning Tree Protocol), which applies the STP (spanning tree
protocol) separately for each set of VLANs (called an MSTI - multiple spanning tree instance).

rpvst

Sets the mode to RPVST (Rapid Per VLAN Spanning Tree).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling MSTP mode:

switch(config)# spanning-tree mode mstp

Enabling RPVST mode:

switch(config)# spanning-tree mode rpvst

spanning-tree pathcost-type

Syntax

spanning-tree pathcost-type {long | short}

no spanning-tree pathcost-type

Description

Configures the spanning tree path cost type. The long mode provides support for the wider range of link
speeds required by high-speed interfaces. All switches in the network must use the same path cost type or
errors can occur in the spanning tree.

The no form of this command sets the spanning tree path cost type to the default value of long.

Command context

config

Parameters
long

Specifies the spanning tree path cost type as a 32-bit value, allowing port cost values to be set in the
range 1-200,000,000. Default.

short

Specifies the spanning tree path cost type as a 16-bit value, allowing port cost values to be set in the
range 1-65535.

Authority

Administrators or local user group members with execution rights for this command.

84

AOS-CX 10.06 Layer 2 Bridging Guide

Examples

Setting spanning tree path cost type to short:

switch# config
switch(config)# spanning-tree pathcost-type short

Setting spanning tree path cost type to long:

switch# config
switch(config)# spanning-tree pathcost-type long

Setting spanning tree path cost to default of long:

switch# config
switch(config)# no spanning-tree pathcost-type

spanning-tree tcn-guard

Syntax

spanning-tree tcn-guard

no spanning-tree tcn-guard

Description

Disables propagation of topology change notifications (TCNs) to other STP ports. Use this when you do not
want topology changes to be noticed by peer devices.

The no form of this command, enables propagation of topology changes. By default, propagation is
disabled.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling tcn-guard, which disables propagation of topology changes:

switch(config-if)# spanning-tree tcn-guard

Disabling tcn-guard, which enables propagation of topology changes:

switch(config-if)# no spanning-tree tcn-guard

spanning-tree vlan

Syntax

spanning-tree vlan <VLAN-LIST> [{hello-time | foward-delay | max-age | priority} <VALUE>]

no spanning-tree vlan <VLAN-LIST> [hello-time | foward-delay | max-age | priority]

Chapter 6 Spanning tree protocols

85

Description

Creates an RPVST instance for the specified VLAN. This command also allows for configuration of RPVST
instance-specific time parameters.

The no form of this command removes the RPVST instance associated with the specified VLAN, and
configures default values for RPVST instance-specific parameters.

Command context

config

Parameters
<VLAN-LIST>

Specifies the number of a single VLAN, or a series of numbers for a range of VLANs, separated by
commas (1, 2, 3, 4), dashes (1-4), or both (1-4,6).

hello-time <VALUE>

Specifies the hello-time in seconds for the RPVST instance. Range: 2-10 seconds. Default: 2 seconds.

forward-delay <VALUE>

Specifies the forward-delay time in seconds for the RPVST instance. Range: 4-30 seconds. Default: 15
seconds.

max-age <VALUE>

Specifies the maximum age time in seconds for the RPVST instance. Range: 6-40 seconds. Default: 20
seconds.

priority <VALUE>

Specifies the priority for the RPVST instance. Priority value is configured as a multiple of 4096. Range:
0-15. Default: 8 which is 32768.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating an RPVST instance for a list of VLANs and configuring various time parameters:

switch# config
switch(config)# spanning-tree vlan 2-5
switch(config)# spanning-tree vlan 2-5 hello-time 5
switch(config)# spanning-tree vlan 5 max-age 10
switch(config)# spanning-tree vlan 2-5 forward-delay 25
switch(config)# spanning-tree vlan 2-5 priority 5

Removing an RPVST instance for a list of VLANs and setting various time parameters to the default:

switch# config
switch(config)# no spanning-tree vlan 2-5
switch(config)# no spanning-tree vlan 2-5 hello-time
switch(config)# no spanning-tree vlan 2-5 forward-time
switch(config)# no spanning-tree vlan 2-5 max-age
switch(config)# no spanning-tree vlan 2-5 priority

86

AOS-CX 10.06 Layer 2 Bridging Guide

spanning-tree vlan cost

Syntax

spanning-tree vlan <VLAN-LIST> cost <PORT-COST>

no spanning-tree vlan <VLAN-LIST> cost

Description

Configures the spanning tree cost for the VLAN. This is the cost to reach the root port.

The no form of this command sets the port cost to the default value.

Command context

config-if

Parameters
<VLAN-LIST>

Specifies the number of a single VLAN, or a series of numbers for a range of VLANs, separated by
commas (1, 2, 3, 4), dashes (1-4), or both (1-4,6).

<PORT-COST>

Specifies the spanning tree cost for the VLAN. Range: 1-200,000,000. Default is calculated from the port
link speed:

• 10 Mbps link speed equals a path cost of 2,000,000.

• 100 Mbps link speed equals a path cost of 200,000.

• 1 Gbps link speed equals a path cost of 20,000.

• 2 Gbps link speed equals a path cost of 10,000.

• 10 Gbps link speed equals a path cost of 2,000.

• 100 Gbps link speed equals a path cost of 200.

• 1 Tbps link speed equals a path cost of 20.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting port cost:

switch(config-if)# spanning-tree vlan 5 cost 100000

Setting port cost to the default:

switch(config-if)# no spanning-tree vlan 5 cost

Chapter 6 Spanning tree protocols

87

spanning-tree vlan port-priority

Syntax

spanning-tree vlan <VLAN-LIST> port-priority <PRIORITY>

no spanning-tree vlan <VLAN-LIST> port-priority

Description

Configures port priority. A port with the lowest priority number has the highest priority for use in forwarding
traffic.

The no form of this command, sets the port priority to the default of 8.

Command context

config-if

Parameters
<VLAN-LIST>

Specifies the number of a single VLAN, or a series of numbers for a range of VLANs, separated by
commas (1, 2, 3, 4), dashes (1-4), or both (1-4,6).

<PRIORITY>

Specifies the port priority. The value, configured as a multiple of 16, helps in determining the designated
port. The lower a priority value, the higher the priority. Range: 1 to15. Default: 8.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting port priority:

switch(config-if)# spanning-tree vlan 5 port-priority 10

Setting port priority to the default of 8:

switch(config-if)# no spanning-tree vlan 5 port-priority

spanning-tree trap

Syntax

spanning-tree trap {new-root | topology-change [vlan <VLAN-ID>] | errant-bpdu |
   root-guard-inconsistency | loop-guard-inconsistency}

no spanning-tree trap {new-root|topology-change [vlan <VLAN-ID>] | errant-bpdu |
   root-guard-inconsistency | loop-guard-inconsistency}

Description

This command enables SNMP traps for new root, topology change event, errant-bpdu received event, root-
guard inconsistency, and loop-guard inconsistency notifications. It is disabled by default.

The no form of this command disables SNMP traps for new root and topology change event notifications.

88

AOS-CX 10.06 Layer 2 Bridging Guide

Command context

config

Parameters
new-root

Enables SNMP notification when a new root is elected on any PVST vlan on the switch.

topology-change

Enables SNMP notification when a topology change event occurred in specified PVST vlan on the switch.

errant-bpdu

Enables SNMP notification when an errant bpdu is received by any PVST vlan on the switch.

root-guard-inconsistency

Enables SNMP notification when the root-guard finds the port inconsistent for any PVST vlan on the
switch.

loop-guard-inconsistency

Enables SNMP notification when the loop-guard finds the port inconsistent for any PVST vlan on the
switch.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Commands enabling spanning-tree trap features:

switch(config)# spanning-tree trap
  new-root                  Enable notifications which are sent when a new root is elected
  topology-change           Enable notifications which are sent when a topology change occurs
  errant-bpdu               Enable notifications which are sent when an errant bpdu is received
  root-guard-inconsistency  Enable notifications which are sent when root guard inconsistency occurs
  loop-guard-inconsistency  Enable notifications which are sent when root guard inconsistency occurs
switch(config)# spanning-tree trap new-root
  <cr>
switch(config)# spanning-tree trap topology-change
  vlan  Enable topology change notification for the specified PVST vlan id.
switch(config)# spanning-tree trap topology-change vlan
  <0-64>  Enable topology change information on the specified vlan id.
switch(config)# spanning-tree trap topology-change vlan 1
  <cr>
switch(config)# spanning-tree trap errant-bpdu
  <cr>
switch(config)# spanning-tree trap root-guard-inconsistency
  <cr>
switch(config)# spanning-tree trap loop-guard-inconsistency
  <cr>

Commands disabling spanning-tree trap features:

switch(config)# no spanning-tree trap
  new-root                  Disable notifications which are sent when a new root is elected
  topology-change           Disable notifications which are sent when a topology change occurs
  errant-bpdu               Disable notifications which are sent when an errant bpdu is received
  root-guard-inconsistency  Disable notifications which are sent when root guard inconsistency occurs
  loop-guard-inconsistency  Disable notifications which are sent when root guard inconsistency occurs
switch(config)# no spanning-tree trap new-root
  <cr>
switch(config)# no spanning-tree trap topology-change
  instance  Disable topology change notification for the specified PVST vlan id.
switch(config)# no spanning-tree trap topology-change vlan
  <0-64>  Disable topology change information on the specified PVST vlan id.
switch(config)# no spanning-tree trap topology-change vlan 0
  <cr>

Chapter 6 Spanning tree protocols

89

switch(config)# no spanning-tree trap errant-bpdu
  <cr>
switch(config)# no spanning-tree trap root-guard-inconsistency
  <cr>
switch(config)# no spanning-tree trap loop-guard-inconsistency
  <cr>

MSTP
Multiple-Instance spanning tree protocol (MSTP) ensures that only one active path exists between any two
nodes in a spanning-tree instance. A spanning-tree instance comprises a unique set of VLANs, and belongs
to a specific spanning-tree region. A region can comprise multiple spanning-tree instances (each with a
different set of VLANs), and allows one active path among regions in a network.

Without spanning tree, having more than one active path between a pair of nodes causes loops in the
network, which can result in duplication of messages, leading to a “broadcast storm” that can bring down
the network.

Developed based on IEEE 802.1s, MSTP overcomes the limitations of STP, RSTP, and PVST. In addition to
supporting rapid network convergence, it allows data flows of different VLANs to be forwarded along
separate paths. This provides a better load sharing mechanism for redundant links.

MSTP provides the following features:

• MSTP divides a switched network into multiple regions, each of which contains multiple spanning trees

that are independent of one another.

• MSTP supports mapping VLANs to spanning tree instances by means of a VLAN-to-instance mapping

table. MSTP can reduce communication overheads and resource usage by mapping multiple VLANs to
one instance.

• MSTP prunes a loop network into a loop-free tree, which avoids proliferation and endless cycling of
packets in a loop network. In addition, it supports load balancing of VLAN data by providing multiple
redundant paths for data forwarding.

• MSTP is compatible with STP and RSTP, and partially compatible with PVST.

MSTP key concepts

MSTP divides an entire Layer 2 network into multiple MST regions, which are connected by a calculated CST.
Inside an MST region, multiple spanning trees, called MSTIs, are calculated. Among these MSTIs, MSTI 0 is
the internal spanning tree (IST).

The following diagram shows a switched network that comprises four MST regions, with each MST region
comprising four MSTP devices.

90

AOS-CX 10.06 Layer 2 Bridging Guide

The following diagram shows the networking topology of MST region 3.

MST region

A multiple spanning tree region (MST region) consists of multiple devices in a switched network and the
network segments between them. All these devices have the following characteristics:

Chapter 6 Spanning tree protocols

91

• A spanning tree protocol enabled.

• Same region name.

• Same VLAN-to-instance mapping configuration.

• Same MSTP revision level.

• Physically linked together.

Multiple MST regions can exist in a switched network. You can assign multiple devices to the same MST
region.

• The switched network comprises four MST regions, MST region 1 through MST region 4.

• All devices in each MST region have the same MST region configuration.

MSTI

MSTP can generate multiple independent spanning trees in an MST region, and each spanning tree is
mapped to specific VLANs. Each spanning tree is referred to as a multiple spanning tree instance (MSTI). In
the diagrams, MST region 3 comprises three MSTIs, MSTI 1, MSTI 2, and MSTI 0.

MSTI 0

VLAN-to-instance mapping table

As an attribute of an MST region, the VLAN-to-instance mapping table describes the mapping relationships
between VLANs and MSTIs.

In the diagrams, the VLAN-to-instance mapping table of MST region 3 is as follows:

• VLAN 1 to MSTI 1. (Ports which are not part of any VLAN are by default part of VLAN 1.)

• VLAN 2 and VLAN 3 to MSTI 2.

• Other VLANs to MSTI 0. (VLANs that are not configured as part of any MSTI are by default part of MSTI 0. )

MSTP achieves load balancing by means of the VLAN-to-instance mapping table.

CST

The common spanning tree (CST) is a single spanning tree that connects all MST regions in a switched
network. If you regard each MST region as a device, the CST is a spanning tree calculated by these devices
through STP or RSTP. The blue lines in the diagrams represent the CST.

IST

An internal spanning tree (IST) is a spanning tree that runs in an MST region. It is also called MSTI 0, a special
MSTI to which all VLANs are mapped by default. In the diagrams, MSTI 0 is the IST in MST region 3.

CIST

The common and internal spanning tree (CIST) is a single spanning tree that connects all devices in a
switched network. It consists of the ISTs in all MST regions and the CST. In the diagrams, the ISTs (MSTI 0) in
all MST regions plus the inter-region CST constitute the CIST of the entire network.

Regional root

The root bridge of the IST or an MSTI within an MST region is the regional root of the IST or MSTI. Based on
the topology, different spanning trees in an MST region might have different regional roots, as shown in MST
region 3 in the diagrams:

92

AOS-CX 10.06 Layer 2 Bridging Guide

• The regional root of MSTI 1 is Device B.

• The regional root of MSTI 2 is Device C.

• The regional root of MSTI 0 (also known as the IST) is Device A.

Common root bridge

The common root bridge is the root bridge of the CIST. In the diagrams, the common root bridge is a device
in MST region 1.

Port roles

A port can play different roles in different MSTIs. In the following diagram, an MST region comprises Device
A, Device B, Device C, and Device D. Port A1 and port A2 of Device A connect to the common root bridge.
Port B2 and Port B3 of Device B form a loop. Port C3 and Port C4 of Device C connect to other MST regions.
Port D3 of Device D directly connects to a host.

MSTP calculation involves the following port roles:

• Root port: Forwards data for a non-root bridge to the root bridge. The root bridge does not have any root

port.

• Designated port: Forwards data to the downstream network segment or device.

• Alternate port: Acts as the backup port for a root port or master port. When the root port or master port

is blocked, the alternate port takes over.

• Backup port: Acts as the backup port of a designated port. When the designated port is invalid, the

backup port becomes the new designated port. A loop occurs when two ports of the same spanning tree
device are connected, so the device blocks one of the ports. The blocked port acts as the backup.

• Edge port: Does not connect to any network device or network segment, but directly connects to a user

host.

• Master port: Acts as a port on the shortest path from the local MST region to the common root bridge.
The master port is not always located on the regional root. It is a root port on the IST or CIST and still a
master port on the other MSTIs.

• Boundary port: Connects an MST region to another MST region or to an STP/RSTP-running device. In

MSTP calculation, a boundary port's role on an MSTI is consistent with its role on the CIST. However, that
is not true with master ports. A master port on MSTIs is a root port on the CIST.

Port states

In MSTP, a port can be in one of the following states:

•

•

Forwarding: The port receives and sends BPDUs, learns MAC addresses, and forwards user traffic.

Learning: The port receives and sends BPDUs, learns MAC addresses, but does not forward user traffic.
Learning is an intermediate port state.

• Discarding: The port receives and sends BPDUs, but does not learn MAC addresses or forward user

traffic.

NOTE: When in different MSTIs, a port can be in different states.

Chapter 6 Spanning tree protocols

93

A port state is not exclusively associated with a port role. The following table lsts the port states that each
port role supports. (An X indicates that the port supports this state, while a dash [—] indicates that the port
does not support this state.)

Port state

Forwarding

Learning

Discarding

CIST calculation

Port role

Root port/master
port

Designated port

Alternate port

Backup port

X

X

X

X

X

X

—

—

X

—

—

X

During the CIST calculation, the following process takes place:

• The device with the highest priority is elected as the root bridge of the CIST.

• MSTP generates an IST within each MST region through calculation.

• MSTP regards each MST region as a single device and generates a CST among these MST regions through

calculation.

The CST and ISTs constitute the CIST of the entire network.

MSTI calculation

Within an MST region, MSTP generates different MSTIs for different VLANs based on the VLAN-to-instance
mappings. For each spanning tree, MSTP performs a separate calculation process similar to spanning tree
calculation in STP.

In MSTP, a VLAN packet is forwarded along the following paths:

• Within an MST region, the packet is forwarded along the corresponding MSTI.

• Between two MST regions, the packet is forwarded along the CST.

MSTP on VSX

See the Virtual Switching Extension (VSX) Guide for important information when configuring MSTP with VSX.

Preparing for MSTP configuration

• Ensure that the VLAN configuration in your network supports all of the forwarding paths necessary for
the desired connectivity. All ports connecting one switch to another within a region and one switch to
another between regions should be configured as members of all VLANs configured in the region.

• Configure all ports or trunks connecting one switch to another within a region as members of all VLANs
in the region. Otherwise, some VLANs could be blocked from access to the spanning tree root for an
instance or for the region.

• Plan individual MST regions based on VLAN groupings. That is, plan on all MSTP switches in a given region

supporting the same set of VLANs. Within each region, determine the VLAN membership for each
spanning tree instance. (Each instance represents a single forwarding path for all VLANs in that instance.)

• Verify that there is one logical spanning tree path through the following:

94

AOS-CX 10.06 Layer 2 Bridging Guide

◦ Any interregional links

◦ Any IST (Internal Spanning Tree) or MSTI within a region

◦ Any legacy (802.1D or 802.1w) switch or group of switches. (Where multiple paths exist between an
MST region and a legacy switch, expect the CST (Common Spanning Tree) to block all but one such
path.)

• Determine the root bridge and root port for each MSTI.

• Determine the designated bridge and designated port for each LAN segment.

• Determine which VLANs to assign to each MST instance and use port trunks with 802.1Q VLAN tagging
where separate links for separate VLANs would result in a blocked link preventing communication
between nodes on the same VLAN.

• Set the admin-edge port type to admin-edge for edge ports connected to end nodes.

• Set the admin-edge port type to admin-network for ports connected to another switch, a bridge, or a

half-duplex repeater.

MSTP scenario

In this scenario, all four switches are in same region. VLANs 10, 20, 30, 40, 50, and 60 are defined on all
switches, causing a network loop. The physical topology of the network looks like this:

To eliminate the loop, MSTP is enabled on all the switches, with the following configuration:

• Switch SW-TR is the root for CIST, MST1, and MST2.

• CIST: VLANs 10, 20

•

•

Instance-1: VLANs 30,40

Instance-2: VLANs 50,60

• All four switches are in the same MSTP region.

To understand how MSTP works in this scenario, it is useful to view each instance as a separate logical
topology as illustrated in the following diagrams:

Chapter 6 Spanning tree protocols

95

96

AOS-CX 10.06 Layer 2 Bridging Guide

Loops are avoided by blocking the alternate links for each network segment. All ports designated A
(Alternate) are blocked and do not forward traffic. Although this strategy eliminates the loops, it is not the
most effective way to configure the MST regions because network resources are not fully used. By changing
the root for each instance, more effective load sharing can be achieved as follows:

Chapter 6 Spanning tree protocols

97

With this configuration, the links/ports that were previously unused are now being used by different
instances. Also, the network loop is eliminated and load sharing is achieved.

Procedure

1. Configure all switches with the same VLANs, interfaces, and spanning tree instances.

a. Create VLANs 10, 20, 30, 40, 50, and 60 and assign them to interfaces.

switch# config
switch(config)# vlan 10,20,30,40,50,60
switch(config)# interface 1/1/1

98

AOS-CX 10.06 Layer 2 Bridging Guide

switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 10,20,30,40,50,60
switch(config-if)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 10,20,30,40,50,60
switch(config-if)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 10,20,30,40,50,60
switch(config-if)# interface 1/1/4
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk allowed 10,20,30,40,50,60
switch(config-if)# exit

b. Configure spanning tree and enable it.

switch(config)# spanning-tree config-name reg
switch(config)# spanning-tree config-revision 1
switch(config)# spanning-tree inst 1 vlan 30
switch(config)# spanning-tree inst 1 vlan 40
switch(config)# spanning-tree inst 2 vlan 50
switch(config)# spanning-tree inst 2 vlan 60
switch(config)# spanning-tree

c. On switch SW-TL, set instance 1 to priority 0.

sw-tl(config)# spanning-tree inst 1 priority 0

d. On switch SW-BL, set instance 2 to priority 0.

sw-bl(config)# spanning-tree inst 2 priority 0

e. On switch SW-TR, set the bridge priority to 0.

sw-tr(config)# spanning-tree priority 0

MSTP commands

show spanning-tree

Syntax

show spanning-tree [vsx-peer]

Description

Shows priority, address, Hello-time, Max-age, and Forward-delay for bridge and root node.

Command context

Operator (>) or Manager (#)

Chapter 6 Spanning tree protocols

99

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing spanning tree standard information:

switch# show spanning-tree
Spanning tree status      : Enabled Protocol: MSTP

MST0
  Root ID
    Priority      : 32768, Root
    MAC-Address   : 48:0F:CF:AF:04:76
    Hello time    : 2 seconds
    Max Age       : 20 seconds
    Forward Delay : 15 seconds

  Bridge ID
    Priority      : 32768
    MAC-Address   : 48:0F:CF:AF:04:76
    Hello time    : 2 seconds
    Max Age       : 20 seconds
    Forward Delay : 15 seconds

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

show spanning-tree detail

Syntax

show spanning-tree detail [vsx-peer]

Description

Shows spanning tree detail including CIST and corresponding port information.

Command context

Operator (>) or Manager (#)

Parameters
[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

100

AOS-CX 10.06 Layer 2 Bridging Guide

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Showing spanning tree detailed information:

switch# show spanning-tree detail
Spanning tree status      : Enabled Protocol: MSTP

MST0
  Root ID    Priority   : 32768
             MAC-Address: 48:0f:cf:af:04:76
             This bridge is the root
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

  Bridge ID  Priority  : 32768
             MAC-Address: 48:0f:cf:af:04:76
             Hello time(in seconds):2  Max Age(in seconds):20
             Forward Delay(in seconds):15

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago
Timers:    Hello expiry  1 , Forward delay expiry 18

Port 1/1/1
Designated root has priority               :32768 Address: 48:0f:cf:af:04:76
Designated bridge has priority             :32768 Address: 48:0f:cf:af:04:76
Designated port                            :1/1/1
Number of transitions to forwarding state  : 3
Bpdus sent 347, received 9
TCN_Tx: 20, TCN_Rx: 10

Port 1/1/2
Designated root has priority               :32768 Address: 48:0f:cf:af:04:76
Designated bridge has priority             :32768 Address: 48:0f:cf:af:04:76
Designated port                            :1/1/2
Number of transitions to forwarding state  : 3
Bpdus sent 350, received 11
TCN_Tx: 20, TCN_Rx: 10

Port lag1 ID 321
Designated root has priority              : 32768          Address: 48:0F:CF:AF:04:76
Designated bridge has priority            : 32768          Address: 48:0F:CF:AF:04:76
Designated port id                        : 321
Multi-Chassis role                        : active
Number of transitions to forwarding state : 3
BPDUs sent                                : 340
BPDUs received                            : 5
TCN_Tx: 20, TCN_Rx: 10

show spanning-tree inconsistent-ports

Syntax

show spanning-tree inconsistent-ports [instance <INSTANCE-ID>]

Description

Shows ports blocked by STP protection functions such as Root guard, Loop guard, BPDU guard, and RPVST
guard in addition to MSTI information.

Chapter 6 Spanning tree protocols

101

Command context

Operator (>) or Manager (#)

Parameters
<INSTANCE-ID>

Specifies the MSTP instance ID. Range: 0 to 64.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

On the 6400 Switch Series, interface identification differs.

Showing spanning tree inconsistent ports:

switch# show spanning-tree inconsistent-ports
Instance ID  Blocked Port   Reason
------------ -------------- ------------
0            1/1/13         BPDU Guard

Showing inconsistent port information for instances 1-4:

switch# show spanning-tree inconsistent-ports instance 1-4
Instance ID  Blocked Port   Reason
------------ -------------- ------------
1            1/1/3          Root Guard
2            1/1/7          BPDU Guard
3            1/1/9          Loop Guard
4            1/1/37         RPVST Guard

show spanning-tree mst

Syntax

show spanning-tree mst [vsx-peer]

Description

Shows MSTP configuration and status information for each instance.

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

102

AOS-CX 10.06 Layer 2 Bridging Guide

Showing MSTP configuration and status information:

switch# show spanning-tree mst
#### MST0
Vlans mapped   : 2,4-4094
Bridge Address : 48:0F:CF:AF:04:76
Priority       : 32768
Root
Regional Root
Operational    Hello time   : 2 seconds                  Forward delay: 15 seconds
               Max-age      : 20 seconds                 TxHoldCount  : 6 pps
Configured     Hello time   : 2 seconds                  Forward delay: 15 seconds
               Max-age      : 20 seconds                 Max-Hops     : 20
Root           Address      : 48:0F:CF:AF:04:76          Priority     : 32768
               Port         : 0                          Path cost    : 0
Regional Root  Address      : 48:0F:CF:AF:04:76          Priority     : 32768
               Internal cost: 0                          Rem Hops     : 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

#### MST1
Vlans mapped:  1
Bridge         Address : 48:0F:CF:AF:04:76          Priority: 32768
Root           Address : 48:0F:CF:AF:04:76          Priority: 32768
               Port    : 0                          Cost    : 0
               Rem Hops: 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

#### MST2
Vlans mapped:  3
Bridge         Address : 48:0F:CF:AF:04:76          Priority: 32768
Root           Address : 48:0F:CF:AF:04:76          Priority: 32768
               Port    : 0                          Cost    : 0
               Rem Hops: 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

show spanning-tree mst-config

Syntax

show spanning-tree mst-config [vsx-peer]

Chapter 6 Spanning tree protocols

103

Description

Shows MSTP instance and corresponding VLAN information.

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

Showing configuration information for MST instances and corresponding VLANs:

switch# show spanning-tree mst-config
MST configuration information
   MST config ID        : reg
   MST config revision  : 1
   MST config digest    : 2D2BC9A32097B463C48EE1817673FA2D
   Number of instances  : 2

Instance ID     Member VLANs
--------------- ----------------------------------
0               2,4-4094
1               1
2               3

show spanning-tree mst detail

Syntax

show spanning-tree mst detail [vsx-peer]

Description

Shows detailed information for all MST instances.

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

104

AOS-CX 10.06 Layer 2 Bridging Guide

Example

Showing detailed information for all MST instances:

switch# show spanning-tree mst detail
#### MST0
Vlans mapped:  2,4-4094
Bridge         Address: 48:0F:CF:AF:04:76          Priority: 32768
Root
Regional Root
Operational    Hello time   : 2 seconds                  Forward delay: 15 seconds
               Max-age      : 20 seconds                 TxHoldCount  : 6 pps
Configured     Hello time   : 2 seconds                  Forward delay: 15 seconds
               Max-age      : 20 seconds                 Max-Hops     : 20
Root           Address      : 48:0F:CF:AF:04:76          Priority     : 32768
               Port         : 0                          Path cost    : 0
Regional Root  Address      : 48:0F:CF:AF:04:76          Priority     : 32768
               Internal cost: 0                          Rem Hops     : 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

Port 1/1/1
Designated root address            : 48:0F:CF:AF:04:76
Designated regional root address   : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768
BPDUs sent                         : 638
BPDUs received                     : 9
Message expiry                     : 1 second
Forward delay expiry               : 18 seconds
Forward transitions                : 3
TCN_Tx: 10, TCN_Rx: 10

Port 1/1/2
Designated root address            : 48:0F:CF:AF:04:76
Designated regional root address   : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768
BPDUs sent                         : 641
BPDUs received                     : 11
Message expiry                     : 1 second
Forward delay expiry               : 18 seconds
Forward transitions                : 3
TCN_Tx: 10, TCN_Rx: 10

#### MST1
Vlans mapped:  1
Bridge         Address : 48:0F:CF:AF:04:76          Priority: 32768
Root           Address : 48:0F:CF:AF:04:76          Priority: 32768
               Port    : 0                          Cost    : 0
               Rem Hops: 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

Port 1/1/1
Designated root address            : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768

Chapter 6 Spanning tree protocols

105

BPDUs sent                         : 638
BPDUs received                     : 9
Message expiry                     : 1 second
Forward delay expiry               : 18 seconds
Forward transitions                : 4
TCN_Tx: 10, TCN_Rx: 10

Port 1/1/2
Designated root address            : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768
BPDUs sent                         : 641
BPDUs received                     : 11
Message expiry                     : 1 second
Forward delay expiry               : 18 seconds
Forward transitions                : 4
TCN_Tx: 10, TCN_Rx: 10

#### MST2
Vlans mapped:  3
Bridge         Address : 48:0F:CF:AF:04:76          Priority: 32768
Root           Address : 48:0F:CF:AF:04:76          Priority: 32768
               Port    : 0                          Cost    : 0
               Rem Hops: 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

Port 1/1/1
Designated root address            : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768
BPDUs sent                         : 638
BPDUs received                     : 9
Message expiry                     : 1 second
Forward delay expiry               : 18 seconds
Forward transitions                : 3
TCN_Tx: 10, TCN_Rx: 10

Port 1/1/2
Designated root address            : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768
BPDUs sent                         : 641
BPDUs received                     : 11
Message expiry                     : 1 second
Forward delay expiry               : 18 seconds
Forward transitions                : 3
TCN_Tx: 10, TCN_Rx: 10

show spanning-tree mst <INSTANCE-ID>

Syntax

show spanning-tree mst <INSTANCE-ID> [vsx-peer]

Description

Displays MSTP configurations for the given instance ID.

Command context

Operator (>) or Manager (#)

106

AOS-CX 10.06 Layer 2 Bridging Guide

Parameters
<INSTANCE-ID>

Specifies the MSTP instance number. Range: 0 to 64.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show spanning-tree mst 1

#### MST1
Vlans mapped:  1
Bridge         Address : 48:0F:CF:AF:04:76          Priority: 32768
Root           Address : 48:0F:CF:AF:04:76          Priority: 32768
               Port    : 0                          Cost    : 0
               Rem Hops: 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

show spanning-tree mst <INSTANCE-ID> detail

Syntax

show spanning-tree mst <INSTANCE-ID> detail [vsx-peer]

Description

Displays MSTP configurations for the given instance ID with corresponding port details.

Command context

Operator (>) or Manager (#)

Parameters
<INSTANCE-ID>

Specifies the MSTP instance number. Range: 0 to 64.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Chapter 6 Spanning tree protocols

107

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

switch# show spanning-tree mst 1 detail

#### MST1
Vlans mapped:  1
Bridge         Address : 48:0F:CF:AF:04:76          Priority: 32768
Root           Address : 48:0F:CF:AF:04:76          Priority: 32768
               Port    : 0                          Cost    : 0
               Rem Hops: 20

PORT     ROLE        STATE      COST       PRIORITY  TYPE      BPDU-Tx    BPDU-Rx    TCN-Tx     TCN-Rx
-------- ----------- ---------- ---------- --------- --------- ---------- ---------- ---------- ----------
1/1/1    Designated  Forwarding 20000      128       P2P Edge  100        60         20         10
1/1/2    Designated  Forwarding 20000      128       P2P       100        60         20         10
1/1/3    Designated  Forwarding 20000      128       Shr       100        60         20         10
1/1/4    Designated  Forwarding 20000      128       Shr Edge  100        60         20         10
1/1/5    Alternate   Loop-Inc   20000      128       Shr Edge  100        60         20         10
1/1/6    Alternate   Root-Inc   20000      128       Shr Edge  100        60         20         10

Topology change flag          : True
Number of topology changes    : 4
Last topology change occurred : 516 seconds ago

Port 1/1/1
Designated root address            : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768
BPDUs sent                         : 667
BPDUs received                     : 9
Message expiry                     : 0 second
Forward delay expiry               : 18 seconds
Forward transitions                : 4
TCN_Tx: 10, TCN_Rx: 10

Port 1/1/2
Designated root address            : 48:0F:CF:AF:04:76
Designated bridge address          : 48:0F:CF:AF:04:76
Priority                           : 32768
BPDUs sent                         : 670
BPDUs received                     : 11
Message expiry                     : 0 second
Forward delay expiry               : 18 seconds
Forward transitions                : 4
TCN_Tx: 10, TCN_Rx: 10

show spanning-tree mst interface

Syntax

show spanning-tree mst <INSTANCE-ID> interface <IFNAME> [vsx-peer]

Description

Shows MSTP configurations for the given instance ID with corresponding port details.

Command context

Operator (>) or Manager (#)

Parameters
<INSTANCE-ID>

Specifies the MSTP instance number. Range: 0 to 64.

108

AOS-CX 10.06 Layer 2 Bridging Guide

<IFNAME>

Specifies an interface.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Showing MST configuration and port details:

switch# show spanning-tree mst 1 interface 1/1/1
Port 1/1/1

Instance       Role           State        Cost       Priority   Vlans mapped
-------------- -------------- ------------ ---------- ---------- ----------
1              Designated     Forwarding   20000      128        1

show spanning-tree summary port

Syntax

show spanning-tree summary port

Description

Shows spanning tree port summary information.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

On the 6400 Switch Series, interface identification differs.

Showing summary of spanning tree ports:

switch# show spanning-tree summary port

STP status                     : Enabled
Protocol                       : MSTP
BPDU guard timeout value       : None
BPDU guard enabled interfaces  : 1/1/1-1/1/9,1/1/11,1/1/13,1/1/15,1/1/17,1/1/19,
                                 1/1/21,lag1,lag2
BPDU filter enabled interfaces : None
Root guard enabled interfaces  : 1/1/3
Loop guard enabled interfaces  : 1/1/2
TCN guard enabled interfaces   : 1/1/1-1/1/3

Chapter 6 Spanning tree protocols

109

Interface count by state

Instance ID   Blocking Listening Learning Forwarding
------------- -------- --------- -------- ----------
0                    2         0        0         15
1                    2         0        0         15
2                    2         0        0         15
------------- -------- --------- -------- ----------
Total = 3            6         0        0         45

show spanning-tree summary root

Syntax

show spanning-tree summary root

Description

Shows spanning tree root summary information.

Command context

Operator (>) or Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

On the 6400 Switch Series, interface identification differs.

Showing spanning tree root summary:

switch# show spanning-tree summary root

STP status                   : Enabled
Protocol                     : MSTP
System ID                    : 70:72:cf:32:50:f5

Root bridge for STP Instance : 0,1,2

                                                Root Hello Max Fwd
Instance ID     Priority Root ID                cost  Time Age Dly    Root Port
--------------- -------- ----------------- --------- ----- --- --- ------------
0                  32768 70:72:cf:32:50:f5         0     2  20  15          n/a
1                  32768 70:72:cf:32:50:f5         0     2  20  15          n/a
2                  32768 70:72:cf:32:50:f5       200     2  20  15        1/1/1

spanning-tree

Syntax

spanning-tree

no spanning-tree

Description

Enables the spanning tree protocol on the switch.

The no form of this command disables the spanning tree protocol on the switch.

110

AOS-CX 10.06 Layer 2 Bridging Guide

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling spanning tree:

switch(config)# spanning-tree

Disabling spanning tree:

switch(config)# no spanning-tree

spanning-tree bdpu-filter

Syntax

spanning-tree bdpu-filter

no spanning-tree bdpu-filter

Description

Enables the BDPU filter for the interface.

The BPDU filter feature allows control of spanning tree participation on a per-port basis. It can be used to
exclude specific ports from becoming part of spanning tree operations. A port with the BPDU filter enabled
will ignore incoming BPDU packets and stay locked in the spanning tree forwarding state. All other ports
maintain their role. Typical uses for this parameter include:

• To have MSTP operations running on selected ports of the switch rather than every port of the switch at a

time.

• To prevent the spread of errant BPDU frames.

• To eliminate the need for a topology change when a port's link status changes. For example, ports that
connect to servers and workstations can be configured to remain outside of spanning tree operations.

• To protect the network from denial of service attacks that use spoofing BPDUs by dropping incoming
BPDU frames. For this scenario, BPDU protection offers a more secure alternative, implementing port
shut down and a detection alert when errant BPDU frames are received.

NOTE: Ports configured with the BPDU filter mode remain active (learning and forward frames).
However, spanning tree cannot receive or transmit BPDUs on the port. The port remains in a
forwarding state, permitting all broadcast traffic. This can create a network storm if there are
any loops (that is, redundant links) using these ports. If you suddenly have a high load,
disconnect the link and disable the BPDU filter (using the no command.)

The no form of the command sets the BDPU filter status to the default of disabled on the interface.

Command context

config-if

Chapter 6 Spanning tree protocols

111

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the BDPU filter on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree bdpu-filter

Disabling BDPU filter on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree bdpu-filter

spanning-tree bpdu-guard

Syntax

spanning-tree bpdu-guard

no spanning-tree bpdu-guard

Description

Enables the BPDU guard on the selected switch interface. When BPDU guard is enabled, interfaces receiving
MSTP BPDUs become disabled.

BPDU protection is a security feature designed to protect the active MSTP topology by preventing spoofed
BPDU packets from entering the MSTP domain. In a typical implementation, BPDU protection would be
applied to edge ports connected to end user devices that do not run MSTP. If MSTP BPDU packets are
received on a protected port, this feature disables that port and alerts the network manager using an SNMP
trap.

Occasionally a hardware or software failure can cause MSTP to fail, creating forwarding loops that can cause
network failures where unidirectional links are used. The non-designated port transitions in a faulty manner
because the port is no longer receiving MSTP BPDUs.

The no form of the command disables BPDU guard on the selected interface.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling the BPDU guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree bpdu-guard

Disabling BPDU guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree bpdu-guard

112

AOS-CX 10.06 Layer 2 Bridging Guide

spanning-tree bpdu-guard timeout

Syntax

spanning-tree bpdu-guard timeout <INTERVAL>

no spanning-tree bpdu-guard timeout

Description

Enables and configures the auto re-enable timeout in seconds for all interfaces with BPDU guard enabled.
When an interface is disabled after receiving an unauthorized BPDU it will automatically be re-enabled after
the timeout expires. The default is for the interface to stay disabled until manually re-enabled.

The no form of the command disables BPDU guard timeout on the interface. This is the default.

Command context

config

Parameters

<Interval>

Specifies the re-enable timeout in seconds. Range: 1 to 65535.

Authority

Administrators or local user group members with execution rights for this command.

Example

Enabling the BPDU guard timeout on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree bpdu-guard timeout 10

Disabling BPDU guard timeout on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree bpdu-guard

spanning-tree config-name

Syntax

spanning-tree config-name <CONFIG-NAME>

no spanning-tree config-name [<CONFIG-NAME>]

Description

Sets the configuration name for the MST region in which the switch resides.

All switches within an MST region must have identical configuration names. For more than one MSTP switch
in the same MST region, the identical region name must be configured on all such switches. If the default
configuration name is retained on a switch, it cannot exist in the same MST region with another switch.

The no form of this command overwrites the currently configured name with the default name. The default
name is a text string using the hexadecimal representation of the system MAC address.

Chapter 6 Spanning tree protocols

113

Command context

config

Parameters
<CONFIG-NAME>

Specifies the configuration name for the MST region in which the switch resides. Default: text string
using the hexadecimal representation of the MAC address of the switch. Range: 1 - 32 nonblank
characters (case-sensitive).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the configuration name to MST0:

switch(config)# spanning-tree config-name MST0

Setting the configuration name to the default value:

switch(config)# no spanning-tree config-name

spanning-tree config-revision

Syntax

spanning-tree config-revision <REVISION-NUMBER>

no spanning-tree config-revision [<REVISION-NUMBER>]

Description

Configures the revision number for the MST region in which the switch resides. All switches within an MST
region must have identical revision numbers. Use this setting to differentiate between region configurations.
For example, when changing configuration settings within a region where you want to track the
configuration versions you use, or when creating a new region from a subset of switches in a current region
and you want to maintain the same region name.

The no form of this command overwrites the currently configured revision number of the MST region and
sets it to the default value of 0.

Command context

config

Parameters
<REVISION-NUMBER>

Specifies the revision number for the MST region in which the switch resides.Range: 0 - 65535. Default: 0.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the revision to 40:

switch(config)# spanning-tree config-revision 40

114

AOS-CX 10.06 Layer 2 Bridging Guide

Setting the revision to the default value:

switch(config)# no spanning-tree config-revision

spanning-tree cost

Syntax

spanning-tree cost <PORT-COST>

no spanning-tree cost [<PORT-COST>]

Description

Sets individual port cost for MSTI 0.

For a given port, the path cost setting can be different for different MSTIs to which the port may belong.

The switch uses the path cost to determine which ports are the forwarding ports in the MSTI; that is, which
links to use for the active topology of the MSTI and which ports to block.

The no form of the command sets the port cost for MSTI 0 instance to the default value.

Command context

config-if

Parameters
<PORT-COST>

Specifies the cost of the port for MSTI 0. Range: 1-200,000,000. Default is calculated from the port link
speed:

• 10 Mbps link speed equals a path cost of 2,000,000.

• 100 Mbps link speed equals a path cost of 200,000.

• 1 Gbps link speed equals a path cost of 20,000.

• 2 Gbps link speed equals a path cost of 10,000.

• 10 Gbps link speed equals a path cost of 2,000.

• 100 Gbps link speed equals a path cost of 200.

• 1 Tbps link speed equals a path cost of 20.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the cost to 2000 on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree cost 2000

Setting the cost to the default on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree cost

Chapter 6 Spanning tree protocols

115

spanning-tree forward-delay

Syntax

spanning-tree forward-delay <DELAY-IN-SECS>

no spanning-tree forward-delay [<DELAY-IN-SECS>]

Description

Configures the time the switch waits between transitions from listening to learning and from learning to
forwarding states.

The no form of this command sets forward delay time for the bridge to the default of 15 seconds.

Command context

config

Parameters
<DELAY-IN-SECS>

Specifies the forward delay time in seconds. Default: 15 seconds. Range: 4-30.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting forward delay to 6 seconds:

switch(config)# spanning-tree forward-delay 6

Setting forward delay to the default of 15 seconds:

switch(config)# no spanning-tree forward-delay

spanning-tree hello-time

Syntax

spanning-tree hello-time <HELLO-IN-SECS>

no spanning-tree hello-time [<HELLO-IN-SECS>]

Description

Configures the transmission interval between consecutive Bridge Protocol Data Units (BPDU) that the switch
sends as a root bridge. The hello time interval is inserted in outbound BPDUs.

The no form of this command sets hello time to the default of 2 seconds.

Command context

config

Parameters
<HELLO-IN-SECS>

Specifies the hello time interval in seconds. Default: 2 seconds. Range: 2-10.

116

AOS-CX 10.06 Layer 2 Bridging Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the hello time interval to 6 seconds:

switch(config)# spanning-tree hello-time 6

Setting the hello time interval to the default of 2 seconds:

switch(config)# no spanning-tree hello-time

spanning-tree instance cost

Syntax

spanning-tree instance <INSTANCE-ID> cost <PORT-COST>

no spanning-tree instance <INSTANCE-ID> cost [<PORT-COST>]

Description

Sets the individual port cost for an MSTI. The switch uses the path cost to determine which links to use for
the active topology of the MSTI (forwarding ports) and which ports to block. The path cost setting for a port
can be different on each MSTI to which the port belongs.

The no form of this command sets the port cost for an MSTI to the default value.

Command context

config-if

Parameters
<INSTANCE-ID>

Specifies the MSTI number. Range: 1-64.

<PORT-COST>

Specifies the cost of the port for the MSTI. Range: 1-200000000. Default value is calculated from the port
link speed:

• 10 Mbps link speed equals a path cost of 2000000.

• 100 Mbps link speed equals a path cost of 200000.

• 1 Gbps link speed equals a path cost of 20000.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the port 1/1/1 cost for MSTI 1 to 2000:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree instance 1 cost 2000

Setting the port 1/1/1 cost for MSTI 1 to the default:

Chapter 6 Spanning tree protocols

117

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree instance 1 cost

spanning-tree instance port-priority

Syntax

spanning-tree instance <INSTANCE-ID> port-priority <PRIORITY-MULTIPLIER>

no spanning-tree instance <INSTANCE-ID> port-priority [<PRIORITY-MULTIPLIER>]

Description

Configures the priority as a priority multiplier for the specified ports in the specified MST instance.

For a given port, the priority setting can be different for different MST instances to which the port may
belong.

The no form of this command sets the port priority to the default value of 8 for the MST instance. The
default priority value is derived by multiplying 8 by 16.

Command context

config-if

Parameters
<INSTANCE-ID>

Specifies the MSTP instance number. Range: 1-64.

<PRIORITY-MULTIPLIER>

Specifies the priority as a multiplier. Default: 8. Range: 0 to 15.

The priority range for a port in a given MST instance is 0 to 255. However, this command specifies the
priority as a multiplier (0 to 15) of 16. When you specify a priority multiplier of 0 to 15, the actual priority
assigned to the switch is: (priority-multiplier) x 16.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the port 1/1/1 priority for instance 1 to 8:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree instance 1 port-priority 8

Setting the port 1/1/1 priority for instance 1 to the default:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree instance 1 port-priority

spanning-tree instance priority

Syntax

spanning-tree instance <INSTANCE-ID> priority <PRIORITY-MULTIPLIER>

no spanning-tree instance <INSTANCE-ID> priority [<PRIORITY-MULTIPLIER>]

118

AOS-CX 10.06 Layer 2 Bridging Guide

Description

Sets the switch priority for the specified MST instance.

The no form of this command sets the priority for the specified instance to the default of 8.

Command context

config

Parameters
<INSTANCE-ID>

Specifies the MSTP instance number. Range: 1 to 64.

<PRIORITY-MULTIPLIER>

Specifies the priority as a multiplier. Default: 8. Range: 0 to 15.

The priority range for an MSTP switch is 0-61440. However, this command specifies the priority as a
multiplier (0 - 15) of 4096. That is, when you specify a priority multiplier value of 0 - 15, the actual priority
assigned to the switch is: (priority-multiplier) x 4096. For example, with 2 as the priority-multiplier on a
given MSTP switch, the switch priority setting is 8,192.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the priority multiplier for instance 1 to 5:

switch(config)# spanning-tree instance 1 priority 5

Setting the priority multiplier for instance 1 to the default of 8:

switch(config)# no spanning-tree instance 1 priority

spanning-tree instance vlan

Syntax

spanning-tree instance <INSTANCE-ID> vlan <VLAN-ID>

no spanning-tree instance <INSTANCE-ID> vlan <VLAN-ID>

Description

Creates a new instance with VLANs mapped or maps VLANs to an existing instance.

Each instance must have at least one VLAN mapped to it. When VLANs are mapped to an instance, they are
automatically unmapped from the instance they were mapped to before. Any MSTP instance can have all
the VLANs configured on the switch.

The no form of this command removes the specified VLAN from the MSTP instance.

Command context

config

Chapter 6 Spanning tree protocols

119

Parameters
<INSTANCE-ID>

Specifies the MSTP instance number. Range: 1 to 64.

<VLAN-ID>

Specifies a VLAN ID number.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Mapping VLAN 1 to instance 1:

switch(config)# spanning-tree instance 1 vlan 1

Removing VLAN 1 from instance 1:

switch(config)# no spanning-tree instance 1 vlan 1

spanning-tree link-type

Syntax

spanning-tree link-type {point-to-point|shared}

Description

Specifies the link type of the interface, which is normally derived from the duplex setting of the port. The
default setting depends on the duplex mode of the port: full-duplex ports are point-to-point, half-duplex
ports are shared.

Command context

config-if

Parameters
point-to-point

Specifies the link type as point-to-point.

shared

Specifies the link type as shared.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the link type to point-to-point on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree link-type point-to-point

Setting the link type to shared on interface 1/1/1:

120

AOS-CX 10.06 Layer 2 Bridging Guide

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree link-type shared

spanning-tree loop-guard

Syntax

spanning-tree loop-guard

no spanning-tree loop-guard

Description

Enables the loop guard on the interface. STP loop guard is best applied on blocking or forwarding ports.

The no form of the command sets the loop guard status to the default of disabled on the interface.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Usage

Occasionally a hardware or software failure can cause MSTP to fail, creating forwarding loops that can cause
network failures where unidirectional links are used. The non-designated port transitions in a faulty manner
because the port is no longer receiving MSTP BPDUs.

Loop guard causes the non-designated port to go into the MSTP loop inconsistent state instead of the
forwarding state. In the loop inconsistent state the port prevents data traffic and BPDU transmission
through the link, therefore avoiding the loop creation. When BPDUs again are received on the inconsistent
port, it resumes normal MSTP operation automatically.

In this example, the transmission from switch 1 port 10 to switch 2 prt 20 is blocked due to a hardware
failure. Switch 2 port 2 does not recieve BPDUs and goes into a forwarding state, creating a loop.

When loop guard is configured for switch 2 port 20, this port goes from a forwarding state to an inconsistent
state, and does not forward the traffic through the link, thus avoiding loop creation.

Examples

Enabling the loop guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree loop-guard

Chapter 6 Spanning tree protocols

121

Disabling loop guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree loop-guard

spanning-tree max-age

Syntax

spanning-tree max-age <AGE-IN-SECS>

no spanning-tree max-age [<AGE-IN-SECS>]

Description

Sets the maximum age timer, which specifies the maximum age value that the switch inserts in outbound
BPDU packets it sends as a root bridge. Max-age is the interval, specified in the BPDU, that BPDU data
remains valid after its reception.

The bridge recomputes the spanning tree topology if it does not receive a new BPDU before max-age expiry.

The no form of this command sets the max-age value to the default of 20 seconds.

Command context

config

Parameters
<AGE-IN-SECS>

Specifies the max-age in seconds. Range: 6 to 40. Default: 20.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the max-age to 10 seconds:

switch(config)# spanning-tree max-age 10

Setting the max-age to the default of 20 seconds:

switch(config)# no spanning-tree max-age

spanning-tree max-hops

Syntax

spanning-tree max-hops <HOP-COUNT>

no spanning-tree max-hops [<HOP-COUNT>]

Description

Configures the max hop setting that the switch inserts into BPDUs that it sends out as the root bridge. The
max hop setting determines the number of bridges in an MST region that a BPDU can traverse before it is
discarded.

The no form of this command sets the maximum number of hops to the default of 20.

122

AOS-CX 10.06 Layer 2 Bridging Guide

Command context

config

Parameters
<HOP-COUNT>

Specifies the maximum number of hops. Range: 1 to 40. Default: 20.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the hop count to 10:

switch(config)# spanning-tree max-hops 10

Setting the max-age to the default of 20:

switch(config)# no spanning-tree max-hops

spanning-tree mode

Syntax

spanning-tree mode {mstp|rpvst}

Description

Sets the spanning tree mode to either MSTP mode (Multiple-instance Spanning Tree Protocol) or RPVST
mode (Rapid Per VLAN Spanning Tree). If you want to change the spanning tree mode, you must first disable
spanning tree with the command no spanning-tree.

The no form of this command sets the spanning tree mode to the default value mstp.

Command context

config

Parameters
mstp

Sets the mode to MSTP (Multiple-instance Spanning Tree Protocol), which applies the STP (spanning tree
protocol) separately for each set of VLANs (called an MSTI - multiple spanning tree instance).

rpvst

Sets the mode to RPVST (Rapid Per VLAN Spanning Tree).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling MSTP mode:

switch(config)# spanning-tree mode mstp

Enabling RPVST mode:

Chapter 6 Spanning tree protocols

123

switch(config)# spanning-tree mode rpvst

spanning-tree port-priority

Syntax

spanning-tree port-priority <PRIORITY-MULTIPLIER>

no spanning-tree port-priority [<PRIORITY-MULTIPLIER>]

Description

Configures the port priority. The priority of a port can be different for each MST instance to which it belongs.

The no form of the command sets the port priority for MST instance 0 to the default of 8. The default
priority value is derived by multiplying 8 by 8. For LAG interfaces the default is 4.

Command context

config-if

Parameters
<PRIORITY-MULTIPLIER>

Specifies the port priority as a multiplier. Default: 8, except for LAG interfaces where the default is 4.
Range: 0 to15.

The priority range for a port in a given MSTI is 0 to 255. However, this command specifies the priority as
a multiplier (0 to 15) of 16. When you specify a priority multiplier of 0 to15, the actual priority assigned to
the switch is: (priority-multiplier) x 16.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the port priority to 8 on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree port-priority 8

Setting the port priority to the default on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree port-priority

spanning-tree port-type

Syntax

spanning-tree port-type {admin-edge|admin-network}

no spanning-tree port-type [admin-edge|admin-network]

Description

Sets the STP port type for the interface.

Port types include: admin-edge and admin-network.

The no form of the command sets the port type to the default of admin-network.

124

AOS-CX 10.06 Layer 2 Bridging Guide

Command context

config-if

Parameters
admin-edge

Specifies the port type as administrative edge. During spanning tree establishment, ports with admin-
edge enabled transition immediately to the forwarding state.

admin-network

Specifies the port type as administrative network. When this option is selected, the port looks for BPDUs
for the first 3 seconds. If there are none, the port is classified as an edge port and immediately starts
forwarding packets. If BPDUs are seen on the port, the port is classified as a non-edge port and normal
STP operation commences on that port.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the port type to admin-edge on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree port-type admin-edge

Setting the port type to admin-network on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree port-type admin-network

Setting the port type to the default of admin-network on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree port-type

spanning-tree priority

Syntax

spanning-tree priority <PRIORITY-MULTIPLIER>

no spanning-tree priority [<PRIORITY-MULTIPLIER>]

Description

Configures the switch (bridge) priority for the designated region in which the switch resides.

The switch compares this priority with the priorities of other switches in the same region to determine the
root switch for the region. The lower the priority value, the higher the priority.

The no form of this command sets the bridge priority to the default of 8. The default priority value is derived
by multiplying 8 by 4096.

Command context

config

Chapter 6 Spanning tree protocols

125

Parameters
<PRIORITY-MULTIPLIER>

Specifies the priority as a multiplier. Range: 0 to 15. Default: 8.

The priority range for an MSTP switch is 0-61440. However, this command specifies the priority as a
multiplier (0 to 15) of 4096. That is, when you specify a priority multiplier value of 0 to 15, the actual
priority assigned to the switch is: (priority-multiplier) x 4096. For example, with 2 as the priority-
multiplier on a given MSTP switch, the switch priority setting is 8,192.

Authority

Administrators or local user group members with execution rights for this command.

Usage

Every switch running an instance of MSTP has a Bridge Identifier, which is a unique identifier that helps
distinguish this switch from all others. The switch with the lowest Bridge Identifier is elected as the root for
the tree. The Bridge Identifier is composed of a configurable priority component (2 bytes) and the bridge's
MAC address (6 bytes). You can change the priority component provides flexibility in determining which
switch will be the root for the tree, regardless of its MAC address.

Examples

Setting the priority multiplier to 12:

switch(config)# spanning-tree priority 12

Setting the priority multiplier to the default of 8:

switch(config)# no spanning-tree priority

spanning-tree root-guard

Syntax

spanning-tree root-guard

no spanning-tree root-guard

Description

Enables the root guard on the interface.

When a port is enabled as root-guard, it cannot be selected as the root port even if it receives superior STP
BPDUs. The port is assigned an "alternate" port role and enters a blocking state if it receives superior MSTP
BPDUs.

A superior BPDU contains both "better" information on the root bridge and path cost to the root bridge,
which would normally replace the current root bridge selection.

The no form of the command sets the root guard status to the default of disabled on the interface.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

126

AOS-CX 10.06 Layer 2 Bridging Guide

Enabling the root guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree root-guard

Disabling root guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree root-guard

spanning-tree rpvst-filter

Syntax

spanning-tree rpvst-filter

no spanning-tree rpvst-filter

Description

Enables the RPVST filter for the interface.

When the RPVST filter is enabled, the ingressing RPVST proprietary BPDUs are dropped after copying to CPU
whereas the standard IEEE RPVST BPDUs are still allowed. This helps in preventing the flooding of RPVST
proprietary BPDUs under an MSTP-RPVST interop environment.

NOTE: If the neighboring switch is running RPVST then this pair of switches will not converge as
RPVST BPDUs will not reach them.

If enabling RPVST filter causes a high traffic load, shutdown the port and reconfigure the BPDU filter with the
CLI command: no spanning tree rpvst-filter.

RPVST filter is disabled by default.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Example

On the 6400 Switch Series, interface identification differs.

Enabling the RPVST filter on interface 1/1/1:

switch# configure terminal
switch(config)# interface 1/1/1
switch(config-if)# spanning-tree rpvst-filter

Disabling RPVST filter on interface 1/1/1:

switch# configure terminal
switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree rpvst-filter

Chapter 6 Spanning tree protocols

127

spanning-tree rpvst-guard

Syntax

spanning-tree rpvst-guard

no spanning-tree rpvst-guard

Description

Enables RPVST guard on the switch interface. When RPVST guard is enabled on an interface, it will disable
that interface if RPVST BPDUs are received on it.

The no form of the command sets the RPVST guard status to the default of disabled on the interface.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Example

On the 6400 Switch Series, interface identification differs.

Enabling RPVST guard on interface 1/1/1:

switch# configure terminal
switch(config)# interface 1/1/1
switch(config-if)# spanning-tree rpvst-guard

Disabling RPVST guard on interface 1/1/1:

switch# configure terminal
switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree rpvst-guard

spanning-tree tcn-guard

Syntax

spanning-tree tcn-guard

no spanning-tree tcn-guard

Description

Enables the TCN (Topology Change Notification) guard in the interface. When enabled for a port, the port
stops propagating received topology change notifications and topology changes to other ports.

The no form of the command sets the TCN guard status to the default of disabled on the interface.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

128

AOS-CX 10.06 Layer 2 Bridging Guide

Examples

Enabling TCN guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree tcn-guard

Disabling TCN guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree tcn-guard

spanning-tree transmit-hold-count

Syntax

spanning-tree transmit-hold-count <COUNT>

no spanning-tree transmit-hold-count [<COUNT>]

Description

Sets the maximum number of BPDUs per second that the switch can send from an interface.

The no form of this command sets the transmit-hold-count to the default of 6.

Command context

config

Parameters
<COUNT>

Specifies the number of BPDUs that can be sent per second. Range: 1 to 10. Default: 6.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the transmit-hold-count to 5:

switch(config)# spanning-tree transmit-hold-count 5

Setting the transmit-hold-count to the default of 6:

switch(config)# no spanning-tree transmit-hold-count

spanning-tree trap

Syntax

spanning-tree trap {new-root|topology-change [instance <0-64>] | errant-bpdu |
   root-guard-inconsistency | loop-guard-inconsistency}

no spanning-tree trap {new-root|topology-change [instance <0-64>] | errant-bpdu |
   root-guard-inconsistency | loop-guard-inconsistency}

Chapter 6 Spanning tree protocols

129

Description

This command enables SNMP traps for new root, topology change event, errant-bpdu received event, root-
guard inconsistency, and loop-guard inconsistency notifications. It is disabled by default.

The no form of this command disables SNMP traps for new root and topology change event notifications.

Command context

config

Parameters
new-root

Enabling SNMP notification when a new root is elected on any MST instance on the switch.

topology-change

Enabling SNMP notification when a topology change event occurs in the specified MST instance on the
switch.

errant-bpdu

Enabling SNMP notification when an errant bpdu is received by any MST instance on the switch.

root-guard-inconsistency

Enabling SNMP notification when the root-guard finds the port inconsistent for any MST instance on the
switch.

loop-guard-inconsistency

Enabling SNMP notification when the loop-guard finds the port inconsistent for any MST instance on the
switch.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling SNMP notification when a new root is elected:

switch(config)# spanning-tree trap new-root

Enabling SNMP notification when a topology change event occurs:

switch(config)# spanning-tree trap topology-change

Enabling SNMP notification when a topology change event occurs on instance 1:

switch(config)# spanning-tree trap topology-change instance 1

Disabling SNMP traps when a topology change event notification occurs on instance 1:

switch(config)# no spanning-tree trap topology-change instance 1

130

AOS-CX 10.06 Layer 2 Bridging Guide

Chapter 7
MVRP

MVRP provides a mechanism to dynamically share VLAN configuration information across layer 2 switches
on a network. MVRP eliminates the need to manually configure VLANs on each switch, enabling the network
to dynamically maintain VLANs based on the current network configuration. MVRP propagates local VLAN
information to other devices, receives VLAN information from other devices, and dynamically updates local
VLAN information. When the network topology changes, MVRP propagates and learns VLAN information
again according to the new topology.

MVRP is defined in the IEEE 802.1ak standard. It perform the same functions as Generic Attribute
Registration Protocol (GARP), while overcoming GARP limitations, such as bandwidth usage and convergence
time in networks with a large numbers of VLANs.

MVRP makes use of the Multiple Registration Protocol (MRP). MRP provides the mechanism for switches on
the same layer 2 network to transmit attribute values on a per MSTI (Multiple Spanning Tree Instance) basis.
(An MSTI is a group or set of VLANs, all of which are part of the same spanning tree.)

Each MRP-enabled interface is called an MRP participant, and each MVRP-enabled interface is called an
MVRP participant. When the VLAN configuration on an MVRP participant changes, it sends a Protocol Data
Unit (PDU) to notify other MVRP participants to register and deregister the changed VLAN. MRP rapidly
propagates the configuration information of an MRP participant throughout the layer 2 network.

MRP registers and deregisters VLAN attributes as follows:

• When an interface receives a declaration for a VLAN, the interface registers the VLAN and joins the VLAN.

• When an interface receives a withdrawal for a VLAN, the interface deregisters the VLAN and leaves the

VLAN.

MVRP only applies to trunk interfaces.

MVRP functionality and limitations

MIB support

The MVRP feature supports objects in the following standard MIBs:

•

•

IEEE8021-Q-BRIDGE-MIB (Version 200810150000Z)

IEEE8021-BRIDGE-MIB (Version 200810150000Z)

It also supports MVRP objects in the HPE proprietary MIB:

HPE-MVRP-MIB (hpeMvrp.mib)

MVRP limitations

• MVRP is only supported on L2 trunk ports.

• MVRP and VLAN translation cannot be enabled on the same interface.

• MVRP will propagate only the first 1024 VLANs. This number includes existing static VLANs locally. For

example, if a peer device already has 100 static VLANs, then it can only learn 924 VLANs.

Chapter 7 MVRP

131

• MVRP and PVST cannot be enabled at the same time.

•

For security purposes, MVRP is disabled by default. MVRP packets are blocked on MVRP disabled ports,
but can be enabled on ports that are security enabled.

• MVRP supports 1024 VLANs and 512 logical ports.

•

If MVRP is enabled globally, MVRP is automatically enabled on LAG interfaces and cannot be disabled.

MRP messages
MRP messages include the following types:

• Declaration: Includes Join and New messages.

• Withdrawal: Includes Leave and LeaveAll messages

Join message

An MRP participant sends a Join message to request the peer participant to register attributes in the Join
message.

When receiving a Join message from the peer participant, an MRP participant performs the following tasks:

• Registers the attributes in the Join message.

• Propagates the Join message to all other participants on the device.

After receiving the Join message, other participants send the Join message to their respective peer
participants.

Join messages sent from a local participant to its peer participant include the following types:

•

JoinEmpty: Declares an unregistered attribute. For example, when an MRP participant joins an
unregistered static VLAN, it sends a JoinEmpty message. VLANs created manually and locally are called
static VLANs. VLANs learned through MRP are called dynamic VLANs.

•

JoinIn: Declares a registered attribute. A JoinIn message is used in one of the following situations:

◦ An MRP participant joins an existing static VLAN and sends a JoinIn message after registering the

VLAN.

◦ The MRP participant receives a Join message propagated by another participant on the device and

sends a JoinIn message after registering the VLAN.

New message

Similar to a Join message, a New message enables MRP participants to register attributes.

When the MSTP topology changes, an MRP participant sends a New message to the peer participant to
declare the topology change.

Upon receiving a New message from the peer participant, an MRP participant performs the following tasks:

• Registers the attributes in the message.

• Propagates the New message to all other participants on the device.

132

AOS-CX 10.06 Layer 2 Bridging Guide

After receiving the New message, other participants send the New message to their respective peer
participants.

Leave message

An MRP participant sends a Leave message to the peer participant when it wants the peer participant to
deregister attributes that it has deregistered.

When the peer participant receives the Leave message, it performs the following tasks:

• Deregisters the attribute in the Leave message.

• Propagates the Leave message to all other participants on the device.

After a participant on the device receives the Leave message, it determines whether to send the Leave
message to its peer participant depending on the attribute status on the device.

•

•

If the VLAN in the Leave message is a dynamic VLAN not registered by any participants on the device,
both of the following events occur:

◦ The VLAN is deleted on the device.

◦ The participant sends the Leave message to its peer participant.

If the VLAN in a Leave message is a static VLAN, the participant will not send the Leave message to its
peer participant.

LeaveAll message

Each MRP participant starts its LeaveAll timer when starting up. When the timer expires, the MRP participant
sends LeaveAll messages to the peer participant.

Upon sending or receiving a LeaveAll message, the local participant starts the Leave timer. The local
participant determines whether to send a Join message depending on its the attribute status. A participant
can re-register the attributes in the received Join message before the Leave timer expires.

When the Leave timer expires, a participant deregisters all attributes that have not been re-registered to
periodically clear useless attributes in the network.

Configuring MVRP

Procedure

1. Enable MVRP globally on all interfaces or only for specific interfaces with the command mvrp.

2. By default, MVRP supports dynamic registration and deregistration of VLANs on all interfaces. If required,

customize the behavior for each interface with the command mvrp registration.

3. If required, adjust the MVRP timers from their default values with the command mvrp timer. To avoid
frequent registrations and deregistrations, use the same MVRP timer values throughout the network.

4. Review your MVRP configuration settings with the commands show mvrp config, show mvrp state,

and show mvrp statistics.

Example

This example creates the following configuration:

Chapter 7 MVRP

133

• Enables MVRP on all interfaces.

• Sets interface 1/1/1 to ignore VLAN 100.

switch(config)# mvrp
switch(config)# interface 1/1/1
switch(config-if)# mvrp registration forbidden 100
switch(config-if)# mvrp
switch(config-if)# quit
switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Disabled
Port    Status    Registration Join  Leave  LeaveAll Periodic
                  Type         Timer Timer  Timer    Timer
------- -------- --------      -----  ----- ------   --------
1/1/1   Disabled  Normal         20   300   1000     100
switch# show mvrp state 1/1/1
Configuration and Status - MVRP state for VLAN 1
Port   VLAN Registrar Applicant
            State     State
-----  ---- -------- ---------
1/1/1  1     MT       QA

MVRP scenario 1
This scenario illustrates the configuration of a simple MVRP deployment.

Procedure

1. On switch A, enable MVRP globally, define VLANs on interface 1/1/1 and 1/1/2, and enable MVRP on

each interface.

switch# config
switch(config)# mvrp

134

AOS-CX 10.06 Layer 2 Bridging Guide

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# mvrp
switch(config-if)# exit
switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# mvrp

2. On switch B, enable MVRP globally, define VLANs 10 and 20, assign a trunk native VLAN to interface

1/1/3, and enable MVRP on this interface.

switch# config
switch(config)# mvrp
switch(config)# vlan 10
switch(config)# vlan 20
switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# mvrp

3. On switch C, enable MVRP globally, define VLAN 20, assign a trunk native VLAN to interface 1/1/3, and

enable MVRP on this interface.

switch# config
switch(config)# mvrp
switch(config)# vlan 20
switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# mvrp

4. Verify VLAN configuration by running the command show vlan. It should show that VLAN 10 and 20 are

learned by switch A, and VLAN 10 should be learned by switch C. For example:

On switch A:

switch# show vlan
------------------------------------------------------------------------------------------
VLAN  Name                              Status  Reason                Type      Interfaces
------------------------------------------------------------------------------------------
1     DEFAULT_VLAN_1                    up      ok                    default   1/1/1-1/1/2
10    VLAN10                            up      ok                    dynamic   1/1/2
20    VLAN20                            up      ok                    dynamic   1/1/1-1/1/2
switch#
switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Enabled
Port    Status    Registration Join   Leave    LeaveAll Periodic
                  Type         Timer  Timer    Timer    Timer
------- --------  --------     -----  -------  -------  --------
  1/1/1  Enabled    normal        20      300     1000       100
  1/1/2  Enabled    normal        20      300     1000       100
switch# show mvrp state
Configuration and Status - MVRP state

Chapter 7 MVRP

135

Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/1  1    IN        QA        No
1/1/1  10   MT        QA        No
1/1/1  20   IN        QA        No
1/1/2  1    IN        QA        No
1/1/2  10   IN        VO        No
1/1/2  20   IN        QA        No
switch# show mvrp statistics
Status and Counters - MVRP
MVRP statistics for port : 1/1/1
----------------------------
Failed registration   : 0
Last PDU origin       : e0:07:1b:cb:01:ab
Total PDU Transmitted : 313
Total PDU Received    : 377
Frames Discarded      : 0
Message type    Transmitted     Received
-------------- ------------ ------------
New                       0            0
Empty                179105         2264
In                        0          346
Join Empty              366           62
Join In                 342          692
Leave                     0            0
Leaveall                 43           32

Status and Counters - MVRP
MVRP statistics for port : 1/1/2
----------------------------
Failed registration   : 0
Last PDU origin       : e0:07:1b:cb:22:54
Total PDU Transmitted : 450
Total PDU Received    : 84
Frames Discarded      : 0
Message type    Transmitted     Received
-------------- ------------ ------------
New                       0            0
Empty                173629          382
In                      328            0
Join Empty               83           93
Join In                 711           65
Leave                     0            0
Leaveall                 41           33

On switch B:

switch# show vlan
------------------------------------------------------------------------------------------
VLAN  Name                              Status  Reason                Type      Interfaces
------------------------------------------------------------------------------------------
1     DEFAULT_VLAN_1                    up      ok                    default   1/1/3
10    VLAN10                            up      ok                    static    1/1/3
20    VLAN20                            up      ok                    static    1/1/3
SW1-8320#

SW1-8320# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Enabled
Port    Status    Registration Join   Leave    LeaveAll Periodic
                  Type         Timer  Timer    Timer    Timer

136

AOS-CX 10.06 Layer 2 Bridging Guide

------- --------  --------     -----  -------  -------  --------
 1/1/3   Enabled    normal        20      300     1000       100
SW1-8320# show mvrp state
Configuration and Status - MVRP state
Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/3  1    IN        QA        No
1/1/3  10   MT        QA        No
1/1/3  20   IN        QA        No
SW1-8320# show mvrp statistics
Status and Counters - MVRP
MVRP statistics for port : 1/1/3
----------------------------
Failed registration   : 0
Last PDU origin       : 48:0f:cf:af:f2:fa
Total PDU Transmitted : 77
Total PDU Received    : 303
Frames Discarded      : 0
Message type    Transmitted     Received
-------------- ------------ ------------
New                       0            0
Empty                115067         1754
In                        0          268
Join Empty              100            1
Join In                  53          581
Leave                     0            0
Leaveall                 28           27

On switch C:

switch# show vlan
------------------------------------------------------------------------------------------
VLAN  Name                              Status  Reason                Type      Interfaces
------------------------------------------------------------------------------------------
1     DEFAULT_VLAN_1                    up      ok                    default   1/1/3
10    VLAN10                            up      ok                    dynamic   1/1/3
20    VLAN20                            up      ok                    static    1/1/3
switch#

switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Enabled
Port    Status    Registration Join   Leave    LeaveAll Periodic
                  Type         Timer  Timer    Timer    Timer
------- --------  --------     -----  -------  -------  --------
 1/1/3   Enabled    normal        20      300     1000       100
switch# show mvrp state
Configuration and Status - MVRP state
Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/3   1    IN        QA        No
1/1/3   10   IN        VO        No
1/1/3   20   IN        QA        No
switch#

switch# show mvrp statistics
Status and Counters - MVRP
MVRP statistics for port : 1/1/3
----------------------------
Failed registration   : 0

Chapter 7 MVRP

137

Last PDU origin       : 48:0f:cf:af:f2:fb
Total PDU Transmitted : 203
Total PDU Received    : 95
Frames Discarded      : 0
Message type    Transmitted     Received
-------------- ------------ ------------
New                       0            0
Empty                 72915          586
In                      183            0
Join Empty               40          101
Join In                 366          176
Leave                     0            0
Leaveall                 17           16

MVRP scenario 2

This scenario illustrates the configuration of an MVRP deployment with two MSTIs.

Two MSTIs are defined for this scenario:

• VLAN 10 assigned to MSTI 1

• VLAN 20 assigned to MSTI 2

• All other VLANs assigned to the default MSTI 0

138

AOS-CX 10.06 Layer 2 Bridging Guide

Procedure

1. On switch A:

switch# config
switch(config)# mvrp
switch(config)# vlan 10
switch(config)# spanning-tree
switch(config)# spanning-tree priority 1
switch(config)# spanning-tree config-name sp1
switch(config)# spanning-tree config-revision 1
switch(config)# spanning-tree instance 1 vlan 10
switch(config)# spanning-tree instance 2 vlan 20
switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# mvrp
switch(config-if)# exit
switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# mvrp
switch(config-if)# exit
switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# mvrp
switch(config-if)# exit
switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Enabled
Port    Status    Registration Join   Leave    LeaveAll Periodic
                  Type         Timer  Timer    Timer    Timer
------- --------  --------     -----  -------  -------  --------
  1/1/1  Enabled    normal        20      300     1000       100
  1/1/3  Enabled    normal        20      300     1000       100
  1/1/2  Enabled    normal        20      300     1000       100
switch# show mvrp state
Configuration and Status - MVRP state
Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/1  1    IN        QA        No
1/1/1  20   MT        QA        No
1/1/3  1    IN        QA        No

Chapter 7 MVRP

139

1/1/3  20   IN        VO        No
1/1/2  1    MT        QA        No
1/1/2  20   MT        QA        No

switch# show spanning-tree mst
#### MST0
Vlans mapped:  1-9,11-19,21-4094
Bridge         Address:48:0f:cf:af:f1:82    priority:4096
Operational    Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  txHoldCount(i6
Configured     Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  txHoldCount(i6
Root           Address:48:0f:cf:af:14:0a  Priority:4096
               Port:1/1/3                 Path cost:0
Regional Root  Address:48:0f:cf:af:14:0a  Priority:4096
               Internal cost:20000        Rem Hops:19

Port           Role           State        Cost       Priority   Type
-------------- -------------- ------------ ---------- ---------- ----------
1/1/1          Designated     Forwarding   20000      128        point_to_point
1/1/2          Designated     Forwarding   20000      128        point_to_point
1/1/3          Root           Forwarding   20000      128        point_to_point

#### MST1
Vlans mapped:  10
Bridge         Address:48:0f:cf:af:f1:82    Priority:32768
Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:1/1/3, Cost:20000, Rem Hops:19

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------
1/1/1          Designated     Forwarding   20000   128        point_to_point
1/1/2          Designated     Forwarding   20000   128        point_to_point
1/1/3          Root           Forwarding   20000   128        point_to_point

#### MST2
Vlans mapped:  20
Bridge         Address:48:0f:cf:af:f1:82    Priority:32768
Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:1/1/3, Cost:20000, Rem Hops:19

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------
1/1/1          Designated     Forwarding   20000   128        point_to_point
1/1/2          Designated     Forwarding   20000   128        point_to_point
1/1/3          Root           Forwarding   20000   128        point_to_point

2. On switch B:

switch# config
switch(config)# mvrp
switch(config)# vlan 20
switch(config)# spanning-tree
switch(config)# spanning-tree priority 1
switch(config)# spanning-tree config-name sp1
switch(config)# spanning-tree config-revision 1
switch(config)# spanning-tree instance 1 vlan 10
switch(config)# spanning-tree instance 2 vlan 20

switch(config)# interface 1/1/18
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# mvrp
switch(config-if)# exit
switch(config)# interface 1/1/20
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# mvrp
switch(config-if)# exit
switch(config)# interface 1/1/22
switch(config-if)# no shutdown

140

AOS-CX 10.06 Layer 2 Bridging Guide

switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# mvrp
switch(config-if)# exit
switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Enabled
Port    Status    Registration Join   Leave    LeaveAll Periodic
                  Type         Timer  Timer    Timer    Timer
------- --------  --------     -----  -------  -------  --------
 1/1/18  Enabled    normal        20      300     1000       100
 1/1/20  Enabled    normal        20      300     1000       100
 1/1/22  Enabled    normal        20      300     1000       100
switch# show mvrp state
Configuration and Status - MVRP state
Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/20 1    MT        AA        No
1/1/20 10   MT        AA        No
1/1/20 20   MT        AA        No
1/1/22 1    IN        AP        No
1/1/22 10   IN        VO        No
1/1/22 20   MT        VP        No

switch# show spanning-tree mst
#### MST0
Vlans mapped:  1-9,11-19,21-4094
Bridge         Address:e0:07:1b:cb:22:1c    priority:4096
Operational    Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  txHoldCount(in pp6
Configured     Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  Max-Hops:20
Root           Address:48:0f:cf:af:14:0a  Priority:4096
               Port:1/1/22                Path cost:0
Regional Root  Address:48:0f:cf:af:14:0a  Priority:4096
               Internal cost:20000        Rem Hops:19

Port           Role           State        Cost       Priority   Type
-------------- -------------- ------------ ---------- ---------- ----------
1/1/18         Alternate      Blocking     20000      128        point_to_point
1/1/20         Designated     Forwarding   20000      128        point_to_point
1/1/22         Root           Forwarding   20000      128        point_to_point

#### MST1
Vlans mapped:  10
Bridge         Address:e0:07:1b:cb:22:1c    Priority:32768
Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:1/1/22, Cost:20000, Rem Hops:19

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------
1/1/18         Alternate      Blocking     20000   128        point_to_point
1/1/20         Designated     Forwarding   20000   128        point_to_point
1/1/22         Root           Forwarding   20000   128        point_to_point

#### MST2
Vlans mapped:  20
Bridge         Address:e0:07:1b:cb:22:1c    Priority:32768
Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:1/1/22, Cost:20000, Rem Hops:19

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------
1/1/18         Alternate      Blocking     20000   128        point_to_point
1/1/20         Designated     Forwarding   20000   128        point_to_point
1/1/22         Root           Forwarding   20000   128        point_to_point

3. On switch C:

switch# config
switch(config)# mvrp
switch(config)# vlan 1,20
switch(config)# spanning-tree
switch(config)# spanning-tree priority 1

Chapter 7 MVRP

141

switch(config)# spanning-tree config-name sp1
switch(config)# spanning-tree config-revision 1
switch(config)# spanning-tree instance 1 vlan 10
switch(config)# spanning-tree instance 2 vlan 20
switch(config)# interface 1/1/25
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# mvrp
switch(config-if)# exit
switch(config)# interface 1/1/27
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# mvrp
switch(config-if)# exit
switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Enabled
Port    Status    Registration Join   Leave    LeaveAll Periodic
                  Type         Timer  Timer    Timer    Timer
------- --------  --------     -----  -------  -------  --------
 1/1/25  Enabled    normal        20      300     1000       100
 1/1/27  Enabled    normal        20      300     1000       100
switch# show mvrp state
Configuration and Status - MVRP state
Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/25 1    IN        QA        No
1/1/25 10   IN        VO        No
1/1/25 20   IN        VO        No

switch# show spanning-tree mst
#### MST0
Vlans mapped:  1-9,11-19,21-4094
Bridge         Address:e0:07:1b:cb:01:7a    priority:4096
Operational    Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  txHoldCount(6
Configured     Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  Max-Hops:20
Root           Address:48:0f:cf:af:14:0a  Priority:4096
               Port:1/1/25                Path cost:0
Regional Root  Address:48:0f:cf:af:14:0a  Priority:4096
               Internal cost:40000        Rem Hops:18

Port           Role           State        Cost       Priority   Type
-------------- -------------- ------------ ---------- ---------- ----------
1/1/25         Root           Forwarding   20000      128        point_to_point
1/1/27         Alternate      Blocking     20000      128        point_to_point

#### MST1
Vlans mapped:  10
Bridge         Address:e0:07:1b:cb:01:7a    Priority:32768
Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:1/1/25, Cost:40000, Rem Hops:18

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------
1/1/25         Root           Forwarding   20000   128        point_to_point
1/1/27         Alternate      Blocking     20000   128        point_to_point

#### MST2
Vlans mapped:  20
Bridge         Address:e0:07:1b:cb:01:7a    Priority:32768
Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:1/1/25, Cost:40000, Rem Hops:18

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------

142

AOS-CX 10.06 Layer 2 Bridging Guide

1/1/25         Root           Forwarding   20000   128        point_to_point
1/1/27         Alternate      Blocking     20000   128        point_to_point

4. On switch D:

switch# config
switch(config)# mvrp
switch(config)# vlan 1
switch(config)# spanning-tree
switch(config)# spanning-tree priority 1
switch(config)# spanning-tree config-name sp1
switch(config)# spanning-tree config-revision 1
switch(config)# spanning-tree instance 1 vlan 10
switch(config)# spanning-tree instance 2 vlan 20

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# mvrp
switch(config-if)# exit
switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan trunk native 1
switch(config-if)# vlan trunk allowed all
switch(config-if)# mvrp
switch(config-if)# exit
switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Enabled
Port    Status    Registration Join   Leave    LeaveAll Periodic
                  Type         Timer  Timer    Timer    Timer
------- --------  --------     -----  -------  -------  --------
  1/1/1  Enabled    normal        20      300     1000       100
  1/1/2  Enabled    normal        20      300     1000       100
switch# show mvrp state
Configuration and Status - MVRP state
Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/1  1    IN        QA        No
1/1/1  10   MT        QA        No
1/1/1  20   IN        VO        No
1/1/2  1    IN        AA        No
1/1/2  10   IN        VO        No
1/1/2  20   MT        AA        No

switch# show spanning-tree mst
#### MST0
Vlans mapped:  1-9,11-19,21-4094
Bridge         Address:48:0f:cf:af:14:0a    priority:4096
Root
Regional Root
Operational    Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  txHoldC6
Configured     Hello time(in seconds): 2  Forward delay(in seconds):15  Max-age(in seconds):20  Max-Hop0
Root           Address:48:0f:cf:af:14:0a  Priority:4096
               Port:0                     Path cost:0
Regional Root  Address:48:0f:cf:af:14:0a  Priority:4096
               Internal cost:0            Rem Hops:20

Port           Role           State        Cost       Priority   Type
-------------- -------------- ------------ ---------- ---------- ----------
1/1/1          Designated     Forwarding   20000      128        point_to_point
1/1/2          Designated     Forwarding   20000      128        point_to_point

#### MST1
Vlans mapped:  10
Bridge         Address:48:0f:cf:af:14:0a    Priority:32768

Chapter 7 MVRP

143

Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:0, Cost:0, Rem Hops:20

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------
1/1/1          Designated     Forwarding   20000   128        point_to_point
1/1/2          Designated     Forwarding   20000   128        point_to_point

#### MST2
Vlans mapped:  20
Bridge         Address:48:0f:cf:af:14:0a    Priority:32768
Root           Address:48:0f:cf:af:14:0a    Priority:32768
               Port:0, Cost:0, Rem Hops:20

Port           Role           State        Cost    Priority   Type
-------------- -------------- ------------ ------- ---------- ----------
1/1/1          Designated     Forwarding   20000   128        point_to_point
1/1/2          Designated     Forwarding   20000   128        point_to_point

MVRP commands

clear mvrp statistics

Syntax

clear mvrp statistics [<PORT-NUM> | <PORT-LIST> | LAG <LAG-NUM>]

Command context

Manager (#)

Description

Resets the MVRP statistic counters globally or for the specified ports or LAG.

Parameters
<PORT-NUM>

Specifies a port number.

<PORT-LIST>

Specifies a list of ports.

LAG <LAG-NUM>

Specifies a Link Aggregation number. Range: 1 to 128.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch# clear mvrp statistics 1/1/1

144

AOS-CX 10.06 Layer 2 Bridging Guide

mvrp

Syntax

mvrp

no mvrp

Description

Enables the MVRP feature globally or on a specific interface. By default, MVRP is disabled.

The no form of this command disables MVRP.

NOTE: MVRP and VLAN translation cannot be enabled on the same interface.

Command context

config

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling MVRP globally:

switch(config)# mvrp

Enabling MVRP on an interface:

switch(config)# interface 1/1/1
switch(config-if)# mvrp

mvrp registration

Syntax

mvrp registration {normal | fixed | forbidden [<VLAN-LIST>]}

no mvrp registration forbidden {<VLAN-LIST>}

Description

Configures the MVRP registrar state which determines how an MVRP participant responds to MRP
messages. The default registration mode is normal.

The no command removes the specified VLANs from the forbidden list.

Command context

config-if

Chapter 7 MVRP

145

Parameters
normal

Enables dynamic registration and deregistration of VLANs on the interface, and propagates VLAN
information to other switches on the network. Default.

fixed

Disables dynamic deregistration of VLANs and drops received MVRP frames. The interface does not
deregister dynamic VLANs or register new dynamic VLANs.

forbidden

Disables dynamic registration of VLANs and drops received MVRP frames. The MVRP participant does
not register new dynamic VLANs or re-register a deregistered dynamic VLAN.

<VLAN-LIST>

Disables dynamic registration of VLANs and drops received MVRP frames for specific VLANs only. Normal
behavior applies to all other VLANs. Specify the number of a single VLAN, or a series of numbers for a
range of VLANs, separated by commas (1, 2, 3, 4), dashes (1-4), or both (1-4,6).

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config)# switch(config-if)# mvrp registration forbidden 10

switch(config-if)# mvrp registration fixed

switch(config-if)# mvrp registration forbidden 1,2,10-20

mvrp timer

Syntax

mvrp timer {join | leave | leaveall | periodic} <TIME>

no mvrp timer {join | leave | leaveall | periodic}

Description

Sets an MVRP timer.

The no form of this command sets the specified timer to its default value.

Command context

config-if

Parameters
join <TIME>

Sets the join timer. You can use the timer to space MVRP join messages. To ensure that join messages
are transmitted to other participants, an MRP participant waits for the specified period of the join timer
before sending a join message. The Join timer must be less than half of the Leave Timer. Range: 20 to
100 in centiseconds. Default: 20.

146

AOS-CX 10.06 Layer 2 Bridging Guide

leave <TIME>

Sets the leave timer for the port, specifying the time that the registrar state machine waits in the LV state
before transiting to the MT state. The leave timer must be at least twice the join timer and must be less
than the leave all timer. Range: 40 - 1000000 centiseconds. Default: 300 centiseconds.

leaveall <TIME>

Sets the leave all timer for the port, specifying the frequency with which the leave all state machine
generates leave alll PDUs. Range: 500 to1000000 centiseconds. Default: 1000.

periodic <TIME>

Sets the periodic timer for the port, specifying the frequency with which the periodic transmission state
machine generates periodic events. The periodic timer is set to 1 second when it is started. Range: 100
to 1000000 centiseconds. Default: 100.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config-if)# mvrp timer join 22

show mvrp config

Syntax

show mvrp config [<PORT-NUM> | <PORT-LIST> | LAG <LAG-NUM>] [vsx-peer]

Description

Displays the MVRP configuration for all L2 ports or optionally for the ports specified.

Command context

Operator (>) or Manager (#)

Parameters
<PORT-NUM>

Specifies displaying information for a particular port number.

<PORT-LIST>

Specifies displaying information for a list of ports.

LAG <LAG-NUM>

Specifies displaying information by LAG. Range: 1 to 128.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Chapter 7 MVRP

147

switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Disabled
Port    Status    Registration Join  Leave  LeaveAll Periodic
                  Type         Timer Timer  Timer    Timer
------- -------- --------      -----  ----- ------   --------
1/1/1    Disabled  Normal         20   300   1000     100
1/1/2    Disabled  Normal         20   300   1000     100
1/1/3    Disabled  Normal         20   300   1000     100

show mvrp state

Syntax

show mvrp state [<VLAN-ID> | <VLAN-ID> <PORT-NUM>]
     [vsx-peer]

Description

Displays the MVRP Registrar and Applicant state machine information for all ports on which MVRP is
enabled, or for specific ports.

Command context

Operator (>) or Manager (#)

Parameters
<VLAN-ID>

Specifies the number of a VLAN. Range: 1 - 4040.

<PORT-NUM>

Specifies a physical port on the switch. Forrmat: member/slot/port.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show mvrp state 1
Configuration and Status - MVRP state for VLAN 1
Port   VLAN Registrar Applicant
            State     State
----   ---- -------- ---------
1/1/1  1    MT       QA

switch# show mvrp state 10 1/1/1
Configuration and Status - MVRP state for VLAN 10
Port   VLAN Registrar Applicant Forbid
            State     State     Mode
----   ---- --------- --------- ---------
1/1/1  10   MT        LO        Yes
switch#

148

AOS-CX 10.06 Layer 2 Bridging Guide

show mvrp statistics

Syntax

show mvrp statistics [<PORT-LIST>] [vsx-peer]

Description

Displays MVRP statistics for all ports or on the ports specified in the list.

Command context

Operator (>) or Manager (#)

Parameters
<PORT-LIST>

Specifies a list of ports. When specifying a list of ports, the ports for which there are no statistics will be
listed in the output.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

switch# show mvrp statistics
Status and Counters - MVRP
MVRP statistics for port : 1/1/1
----------------------------
Failed registration   : 0
Last PDU origin       : 48:0f:cf:af:b1:76
Total PDU Transmitted : 13127
Total PDU Received    : 327
Frames Discarded      : 0
Message type    Transmitted     Received
-------------- ------------ ------------
New                       0            0
Empty              50029394         1264
In                        0            4
Join Empty             1425           48
Join In                 563          555
Leave                     0            0
Leaveall              12218           25

switch# show mvrp statistics  1/1/1

Status and Counters - MVRP
MVRP statistics for port : 1/1/1
----------------------------
Failed registration   : 0
Last PDU origin       : 48:0f:cf:af:b1:76
Total PDU Transmitted : 14874
Total PDU Received    : 327
Frames Discarded      : 0

Chapter 7 MVRP

149

Message type    Transmitted     Received
-------------- ------------ ------------
New                       0            0
Empty              57181612         1264
In                        0            4
Join Empty             1425           48
Join In                 563          555
Leave                     0            0
Leaveall              13965           25

150

AOS-CX 10.06 Layer 2 Bridging Guide

Chapter 8
UDLD

The Unidirectional Link Detection (UDLD) protocol enables detection of unidirectional behavior of layer 2
link. For UDLD to work, both connected devices must run the same UDLD protocol on the respective ports.

UDLD monitors the link between two network devices and blocks the ports on both ends of the link if the
link fails. UDLD is particularly useful for detecting failures in fiber links and trunks.

In the following example each switch load balances traffic across two ports in a trunk group. Without the
UDLD feature, a link failure on a link that is not directly attached to one of the HPE switches remains
undetected. As a result, each switch continues to send traffic on the ports connected to the failed link. When
UDLD is enabled on the trunk ports on each switch, the switches detect the failed link, block the ports
connected to the failed link, and use the remaining ports in the trunk group to forward the traffic.

Similarly, UDLD is effective for monitoring fiber optic links that use two uni-direction fibers to transmit and
receive packets. Without UDLD, if a fiber breaks in one direction, a fiber port may assume the link is still
good (because the other direction is operating normally) and continue to send traffic on the connected
ports. UDLD-enabled ports; however, will prevent traffic from being sent across a bad link by blocking the
ports in the event that either the individual transmitter or receiver for that connection fails.

Ports enabled for UDLD exchange health-check packets once every seven seconds (the link-keepalive
interval). If a port does not receive a health-check packet from the port at the other end of the link within the
keepalive interval, the port waits for four more intervals. If the port still does not receive a health-check
packet after waiting for five intervals, the port concludes that the link has failed and blocks the UDLD-
enabled port.

When a port is blocked by UDLD, the event is recorded in the switch log and other port blocking protocols,
like spanning tree or meshing, will not use the bad link to load balance packets. The port will remain blocked
until the link is unplugged, disabled, or fixed. The port can also be unblocked by disabling UDLD on the port.

Port blocking behavior is dependant on the UDLD mode in use. The previous paragraphs describe RFC5171
Aggressive mode. Other modes behave as follows:

Chapter 8 UDLD

151

• RFC 5171 normal: The port is not blocked but a notification is triggered.

• Aruba OS verify-then-forward: The links are considered blocked until bi-directionality is confirmed. After a
link is considered bidirectional, if the retries are met and no packets are received, the link is marked as
blocked.

• Aruba OS forward-then-verify: The links start up as unblocked. After a link is considered bidirectional, if

the retries are met and no packets are received, the link is marked as blocked.

Configuring UDLD

Procedure

1. Enable UDLD on an interface with the command udld.

2. For most deployments, the default values for the following settings do not need to be changed. If your

deployment requires different settings, change the default values with the indicated command:

UDLD setting

Default value

Packet transmission
delay interval.

Operating mode.

7000 ms

Command to change
it

udld interval

Interconnect with HPE PVOS/Brocade/Foundry
switches in forward-then-verify mode.

udld mode

Retry count.

4

udld retries

3. Review UDLD configuration settings with the command show udld.

Example

This example creates the following configuration:

• Enables UDLD on interface 1/1/1.

• Sets the UDLD mode to rfc5171 aggressive.

• Sets the UDLD interval to 1000.

• Sets the UDLD retries to 3.

switch(config)# interface 1/1/1
switch(config-if)# mode rfc5171 aggressive
switch(config-if)# interval 10000
switch(config-if)# retries 3
switch(config-if)# udld
switch(config-if)# quit
switch(config)# show udld interface 1/1/1
Interface 1/1/1
 Config: enabled
 State: active
 Substate: bidirectional
 Link: unblock
 Version: rfc5171
 Mode: aggressive
 Interval: 10000 milliseconds

152

AOS-CX 10.06 Layer 2 Bridging Guide

Retries: 3
 Tx: 0 packets
 Rx: 0 packets, 0 discarded packets, 0 dropped packets
 Port transitions: 0

UDLD scenario

This scenario describes how to use UDLD on a single physical interface as well as a LAG.

Procedure

1. On switch A:

a. Configure the UDLD session between switch A and B.

switch# config
switch(config-if)# interface 1/1/1
switch(config-if)# udld
switch(config-if)# exit
switch(config)#

b. Configure the UDLD session between switch A and C.

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# lag 1
switch(config-if)# udld interval 400
switch(config-if)# udld mode aruba-os verify-then-forward
switch(config-if)# udld retries 5
switch(config)# exit
switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# lag 1
switch(config-if)# udld interval 400

Chapter 8 UDLD

153

switch(config-if)# udld mode aruba-os verify-then-forward
switch(config-if)# udld retries 5

2. On switch B, configure the UDLD session between switch B and A.

switch# config
switch(config-if)# interface 1/1/1
switch(config-if)# udld
switch(config-if)# exit

3. On switch C, configure the UDLD session between switch C and A.

switch# config
switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# lag 1
switch(config-if)# udld interval 400
switch(config-if)# udld mode aruba-os verify-then-forward
switch(config-if)# udld retries 5
switch(config)# exit
switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# lag 1
switch(config-if)# udld interval 400
switch(config-if)# udld mode aruba-os verify-then-forward
switch(config-if)# udld retries 5

4. On switch A, verify UDLD configuration by running the command show udld. (A packet must arrive on

each switch for it to unblock the interface.)

switch# show udld
Abbreviations:
 VTF - Verify then forward    FTV - Forward then verify
 NOR - RFC 5171 normal        AGG - RFC 5171 aggressive

---------------------------------------------------------------------------------------------------------------------------
Interface  UDLD      UDLD    UDLD           UDLD     Mode Interval Retries  Tx    Rx    Rx          Rx         Transitions
           Config    State   Substate       Link                            Pkts  Pkts  Pkts disc.  Pkts drop.
---------------------------------------------------------------------------------------------------------------------------
1/1/1      enabled   active  Bidirectional  unblock  FTV  7000     4        0     0     0           0          0
1/1/2      enabled   active  Bidirectional  unblock  VTF  400      5        2     2     0           0          1
1/1/3      enabled   active  Bidirectional  unblock  VTF  400      5        2     2     0           0          1

UDLD commands

clear udld statistics

Syntax

clear udld statistics [interface <INTERFACE-NAME>]

Description

Clears UDLD statistics for all interfaces or a specific interface.

Command context

Manager (#)

154

AOS-CX 10.06 Layer 2 Bridging Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Clearing all UDLD statistics on all interfaces:

switch# clear udld statistics

Clearing all UDLD statistics on interface 1/1/1:

switch# clear udld statistics interface 1/1/1

show udld

Syntax

show udld [interface <INTERFACE-NAME>] [vsx-peer]

Description

Displays UDLD information for all interfaces or for a specific interface.

Command context

Operator (>) or Manager (#)

Parameters
interface <INTERFACE-NAME>

Specifies the name of a logical interface on the switch, which can be:

• An Ethernet interface associated with a physical port. Use the format member/slot/port (for

example, 1/3/1).

• UDLD runs only on physical interfaces. LAGs, tunnels, and the like are not supported. However, UDLD
can be configured individually on each port of a LAG or trunk group. Configuring UDLD on a trunk
group primary port enables UDLD on that port only.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

Displaying all UDLD information:

switch# show udld

Abbreviations:
 VTF - Verify-then-forward    FTV - Forward-then-verify
 NOR - RFC 5171 normal        AGG - RFC 5171 aggresive

Chapter 8 UDLD

155

----------------------------------------------------------------------
Interface  UDLD      UDLD      UDLD           UDLD    Mode  Interval
           Config    State     Substate       Link
----------------------------------------------------------------------
1/1/1      Disabled  Inactive  Undetermined   Unblock FTV   8000
1/1/2      Enabled   Active    Bidirectional  Unblock FTV   7000
1/1/3      Enabled   Active    Blocked        Block   FTV   7000
1/1/4      Enabled   Inactive  Uninitialized  Unblock NOR   7000
1/1/5      Enabled   Active    ErrDisabled    Block   AGG   7000
1/1/6      Disabled  Active    Detection      Unblock NOR   7000

---------------------------------------------------------------
Retries  Tx       Rx       Rx          Rx          Transitions
         Pkts     Pkts     Pkts disc.  Pkts drop.
---------------------------------------------------------------
4        4        54       123         123         1
7        1234567  1548421  23214       1878981     3
4        3        77871    2157        81878       1
5        50       0        0           0           0
3        150      25       0           2           1
3        6        54       123         23          1

Displaying information for interface 1/1/1:

switch# show udld interface 1/1/1

Interface 1/1/1
 Config: Enabled
 State: Active
 Substate: Bidirectional
 Link: Unblock
 Version: Aruba OS
 Mode: Forward then verify
 Interval: 7000 milliseconds
 Retries: 7
 Tx: 1234567 packets
 Rx: 1548421 packets, 23214 discarded packets, 1878981 dropped packets
 Port transitions: 3

Displaying the UDLD enable interfaces information:

switch# show udld enabled

Abbreviations:
 VTF - Verify-then-forward    FTV - Forward-then-verify
 NOR - RFC 5171 normal        AGG - RFC 5171 aggresive

-------------------------------------------------------------------------------------------------------------------------------------
Interface  UDLD      UDLD      UDLD           UDLD     Mode  Interval  Retries  Tx       Rx       Rx          Rx          Transitions
           Config    State     Substate       Link                              Pkts     Pkts     Pkts disc.  Pkts drop.
-------------------------------------------------------------------------------------------------------------------------------------
2          Enabled   Active    Bidirectional  Unblock  FTV   7000      7        1234567  1548421  23214       1878981     3
3          Enabled   Active    Blocked        Block    FTV   7000      4        3        77871    2157        81878       1
4          Enabled   Inactive  Uninitialized  Unblock  NOR   7000      5        50       0        0           0           0
5          Enabled   Active    ErrDisabled    Block    AGG   7000      3        150      25       0           2           1

udld

Syntax

udld [disable]

no udld

Description

Enables UDLD support on a physical interface. UDLD is disabled by default. UDLD is configured on a per-
port basis and must be enabled at both ends of the link.

156

AOS-CX 10.06 Layer 2 Bridging Guide

UDLD runs only on physical interfaces. LAGs, tunnels, and the like are not supported. However, UDLD can be
configured individually on each port of a LAG or trunk group. Configuring UDLD on a trunk group's primary
port enables UDLD on that port only.

The no form of this command disables UDLD support and resets all configuration values to their default
settings.

Command context

config-if

Parameters
disable

Disables UDLD on the interface but retains all UDLD configuration settings.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling UDLD on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# udld

Disabling UDLD on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no udld

udld interval

Syntax

udld interval <TIME>

no udld interval

Description

Sets the packet transmission interval.

The no form of this command sets the packet transmission interval to the default value of 7000 ms.

The allowed values vary depending on the operation mode.

The default interval is 7000 ms (7 seconds) for both ArubaOS-Switch and RFC5171 operation modes.

Values must be specified as multiples of 10 ms (7000 ms is allowed but 7005 ms is not a valid setting).

ArubaOS-Switch mode can be configured to support under 100ms (8325) unidirectional link detection times.

For example, for an 8325 switch to achieve 60ms failure detection times, interval can be set to 20ms and
retries to 3.

NOTE: Sessions under 100ms total detection time are susceptible to increasing processing load
on the system. It is advisable to experiment with values that provide adequate detection times
and system/protocol stability. Aruba recommends additional testing prior to configuring these
sessions on a production environment.

Chapter 8 UDLD

157

However, these settings are recommended for specific deployments only, such as using UDLD for Ethernet
Ring Protection Switching (ERPS) link-failure detection. The minimum detection time appropriate for your
environment depends on the specific device family and configuration on which the protocol and system load
is running. Aruba recommends additional testing for these configurations. During testing, monitor for
unexpected false positive detections (i.e., UDLD records a failure when there was not any) on the interfaces
running UDLD. Such false positive failures are an indication that the interval configuration requires tuning
and that the system load might not allow such configuration.

The following table shows the fastest failure detection times that have been tested as a function of the
UDLD enabled links. More UDLD links increase the processing load on the system and hence require higher
interval values. Setting the interval to a lower value than recommended following might cause unexpected
false positive detections. The values on this table are the unidimensional tested limits.

The values provided focus on the scalability of UDLD. The links column is the number of interfaces where
UDLD is enabled given as a range. The interval column is the minimum interval value recommended for that
scale. The detection time column is the total detection time that is achieved with those settings. For more
than 16 links, the interval must be set to 200ms or higher.

Table 1: 8325 switches

Links

1-4

5-8

9-16

16+

Interval

Retries

Detection Time

20ms

40ms

80ms

200ms

3

3

3

3

60ms

120ms

240ms

600ms

NOTE: When configuring detection times under 100ms for LAG interfaces, consider adding the
interface first to the LAG and then enabling UDLD in the interface, to avoid false positive link
failure detections. Adding an interface to a LAG causes momentary control plane traffic
interruption for up to 100ms, which UDLD detects as a link failure if the detection time is
following the control traffic interruption interval.

Command context

config-if

Parameters
<TIME>

Specifies the packet transmission interval. Range: 200 ms to 90000 ms (in increments of 10).

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the packet transmission interval to 1000 ms on interface 1/1/1.

switch(config)# interface 1/1/1
switch(config-if)# udld interval 1000

Setting the packet transmission interval on interface 1/1/1 to the default value.

switch(config)# interface 1/1/1
switch(config-if)# no udld interval

158

AOS-CX 10.06 Layer 2 Bridging Guide

Trying to set the packet interval to 1055 ms on interface 1 is rejected because the interval must be specified
as a multiple of 10:

switch(config)# interface 1
switch(config-if)# udld interval 1055
Invalid interval. The interval value must be between 20ms and 90000ms and should be
specified as a multiple of 10, for example: 20, 100, 3000 or 90000.

Trying to set the packet interval to less than 7000 ms on interface 1 is rejected if using the RFC5171 mode.

switch(config)# interface 1
switch(config-if)# udld mode rfc5171 normal
switch(config-if)# udld interval 500
Invalid interval. The interval must be equal or greater than 7000ms.

udld mode

Syntax

udld mode aruba-os {verify-then-forward | forward-then-verify}

udld mode rfc5171 <RFC5171-MODE>

no udld mode

Description

Sets the operating mode.

The no form of this command sets the operating mode to the default value of aruba-os and forward-
then-verify.

Command context

config-if

Parameters
aruba-os {verify-then-forward | forward-then-verify}

Selects the ArubaOS mode to use. Use this mode when interconnecting with HPE PVOS/Brocade/
Foundry switches.

verify-then-forward

In this mode:

•

Interfaces start as unblocked.

• Once an interface is determined to be bidirectional, it is blocked if the retry limit is reached

without receiving any UDLD packets.

•

Interfaces automatically unblock if a UDLD packet is received.

• On failover, the UDLD state does not change if the (interval * retries) time is around 6 seconds.

forward-then-verify

In this mode:

Chapter 8 UDLD

159

•

•

Interfaces start as unblocked.

Interfaces transition to the unblocked state when receiving UDLD packets.

• Once an interface is determined to be bidirectional, it is blocked if the retry limit is reached

without receiving any UDLD packets.

•

Interfaces automatically unblock if a UDLD packet is received.

rfc5171 <RFC5171-MODE>

Selects the RFC5171 mode to use. Use this mode when interconnecting with third-party switches.

normal

In this mode:

•

•

•

Interfaces start as unblocked.

Interfaces do not block when the retry limit is reached without receiving any UDLD packets (plus 8
extra packets sent to the peer). Instead, an event is generated.

Interfaces automatically unblock if a UDLD packet is received.

aggressive

In this mode:

•

Interfaces start as unblocked.

• Once an interface is determined to be bidirectional, an interface will block when the retry limit is

reached without receiving any UDLD packets (plus 8 extra packets sent to the peer).

•

Interfaces implement a limited/reduced errDisabled recovery mechanism. When the interface's
state goes to errDisabled, a maximum of 3 attempts (5 minutes apart) are triggered to try and
bring up the interface in case the remote endpoint is still sending UDLD packets. After these 3
retries, the interface will remain blocked even if UDLD packets are received. The only way to
unblock the interface when this occurs is to disable (and optionally re-enable) UDLD on the
interface. The retry limit is reset once the interface becomes unblocked.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the operating mode to aruba-os and forward-then-verify on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# udld mode aruba-os forward-then-verify

Setting the operating mode to rfc5171 and aggressive on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# udld mode rfc5171 aggressive

Setting the operating mode on interface 1/1/1 to the default value:

switch(config)# interface 1/1/1
switch(config-if)# no udld mode

160

AOS-CX 10.06 Layer 2 Bridging Guide

udld retries

Syntax

udld retries <COUNT>

no retries

Description

Sets the UDLD retry count.

The no form of this command sets the retry count to the default value.

Command context

config-if

Parameters
<COUNT>

Specifies the UDLD retry count. Range: 3 to 10. Default: 4.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the UDLD retry count to 5 on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# udld retries 5

Setting the UDLD retry count on interface 1/1/1 to the default value:

switch(config)# interface 1/1/1
switch(config-if)# no udld retries

Chapter 8 UDLD

161

Chapter 9
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

162

AOS-CX 10.06 Layer 2 Bridging Guide

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

Chapter 9 Support and other resources

163