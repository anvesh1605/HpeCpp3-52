AOS-CX 10.06 VXLAN EVPN Guide
6200, 6300, 6400, 8325, 8360, 8400 Switch Series

Part Number: 5200-7728
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

Chapter 1 About this document...................................................................... 5
Applicable products........................................................................................................................................5
Latest version available online......................................................................................................................5
Command syntax notation conventions..................................................................................................... 5
About the examples....................................................................................................................................... 6
Identifying switch ports and interfaces .......................................................................................................7
Identifying modular switch components ....................................................................................................8

Chapter 2 VXLAN overview............................................................................... 9
VXLAN network model................................................................................................................................... 9
VXLAN packet format................................................................................................................................... 11
Supported RFCs............................................................................................................................................ 11

Chapter 3 Static VXLAN................................................................................... 12
Configuring a static VXLAN..........................................................................................................................12
Static VXLAN with a single VNI between two VTEPs................................................................................. 13
Static VXLAN with multiple VNIs between two VTEPs.............................................................................. 15

Chapter 4 VXLAN with BGP EVPN.................................................................. 19
Ethernet VPN (EVPN)-based VXLAN overview........................................................................................... 20
Asymmetric IRB.............................................................................................................................................20
Symmetric IRB...............................................................................................................................................21
Example of external connectivity and IVRL with symmetric IRB.............................................................23
MP-BGP extension for EVPN....................................................................................................................... 28
Auto-discovery via EVPN.............................................................................................................................. 28
Layer 2 forwarding....................................................................................................................................... 28
MAC learning..................................................................................................................................... 28
Unicast................................................................................................................................................29
Flood .................................................................................................................................................. 31
Layer 3 forwarding....................................................................................................................................... 31
Centralized L3 gateway deployment...............................................................................................32
Distributed L3 Anycast gateway ..................................................................................................... 33
Symmetric IRB .................................................................................................................................. 33
Symmetric IRB with distributed Anycast Gateway.............................................................33
VXLAN/EVPN symmetric IRB distributed L3 gateways example.......................................35
EVPN VSX support........................................................................................................................................ 51
Sample configuration for iBGP VSX EVPN...................................................................................... 53
VSX failure scenarios.........................................................................................................................56
eBGP support for EVPN............................................................................................................................... 57
MAC mobility................................................................................................................................................. 62
EVPN MAC dampening.................................................................................................................................62
EVPN commands.......................................................................................................................................... 63
active-gateway............................................................................................................................. 63
arp-suppression........................................................................................................................... 65
evpn....................................................................................................................................................66
mac-move-detection count timer......................................................................................... 66
nd-suppression............................................................................................................................. 67

Contents

3

rd........................................................................................................................................................ 68
redistribute host-route......................................................................................................... 68
redistribute local-svi........................................................................................................... 69
route-target..................................................................................................................................70
route-target {evpn}.................................................................................................................. 71
show evpn evi............................................................................................................................... 71
show evpn evi summary.................................................................................................. 72
show evpn evi <EVI-ID>................................................................................................ 73
show evpn evi detail.................................................................................................... 74
show evpn evi <EVI-ID> detail................................................................................ 76
show evpn mac-ip.........................................................................................................................76
show evpn mac-ip evi.................................................................................................... 77
show evpn vtep-neighbor......................................................................................................... 78
show running-config evpn.......................................................................................................78
virtual-mac.................................................................................................................................... 79
vlan....................................................................................................................................................80

Chapter 5 VXLAN commands......................................................................... 81
interface vxlan...................................................................................................................................... 81
routing........................................................................................................................................................ 81
show interface vxlan1.........................................................................................................................82
show interface vxlan vni ................................................................................................................83
show interface vxlan vteps............................................................................................................. 84
shutdown...................................................................................................................................................... 86
source ip....................................................................................................................................................86
system vlan-client-presence-detect........................................................................................... 87
vlan............................................................................................................................................................... 88
vni................................................................................................................................................................. 89
vrf................................................................................................................................................................. 90
vtep-peer....................................................................................................................................................90
vxlan-counters aggregate.................................................................................................................. 91

Chapter 6 Hardware switch controller (HSC)............................................. 92
Connecting to a remote controller............................................................................................................. 92
Scenario 1...................................................................................................................................................... 93
HSC commands ........................................................................................................................................... 96
bfd enable...................................................................................................................................... 96
bfd disable.................................................................................................................................... 97
disable............................................................................................................................................. 97
enable............................................................................................................................................... 98
hsc...................................................................................................................................................... 98
manager ip...................................................................................................................................... 99
manager port................................................................................................................................100

Chapter 7 Support and other resources.................................................... 101
Accessing Aruba Support.......................................................................................................................... 101
Accessing updates......................................................................................................................................101
Warranty information................................................................................................................................ 102
Regulatory information............................................................................................................................. 102
Documentation feedback..........................................................................................................................102

4

AOS-CX 10.06 VXLAN EVPN Guide

Chapter 1
About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

• Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A) Supports static VXLANs only.

• Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A, JL667A,

JL668A, JL762A)

• Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

• Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

• Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A, JL711A)

• Aruba 8400 Switch Series (JL375A, JL376A) Does not support static VXLANs.

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

Chapter 1 About this document

Table Continued

5

Convention

|

{ }

[ ]

… or

...

Usage

Vertical bar. A logical OR that separates multiple items from which you
can choose only one.

Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

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

6

AOS-CX 10.06 VXLAN EVPN Guide

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:

member/slot/port

On the 6200 Switch Series

• member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The
primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•

slot: Line module number. Always 1.

• port: Physical number of a port on a line module.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6300 Switch Series

• member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•

slot: Line module number. Always 1.

• port: Physical number of a port on a line module.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6400 Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Specifies physical location of a module in the switch chassis.

◦ Management modules are on the front of the switch in slots 1/1 and 1/2.

◦

Line modules are on the front of the switch starting in slot 1/3.

• port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

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

7

On the 8400 Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Specifies physical location of a module in the switch chassis.

◦ Management modules are on the front of the switch in slots 1/5 and 1/6.

◦

Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

• port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

Identifying modular switch components

• Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

◦ member: 1.

◦ power supply: 1 to 4.

•

Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

◦ member: 1.

◦

◦

tray: 1 to 4.

fan: 1 to 4.

•

Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

◦ member: 1.

◦ member: 1 or 2.

• The display module on the rear of the switch is not labeled with a member or slot number.

8

AOS-CX 10.06 VXLAN EVPN Guide

Chapter 2
VXLAN overview

Virtual eXtensible LAN (VXLAN) is a MAC-in-UDP technology that provides layer 2 connectivity between
networks across an IP network. VXLAN is typically used to extend layer 2 segments across an entire data
center or between remote data centers. It is also used to provide multi-tenant services, where the same
IP/MAC addresses or VLANs are used on different network segments.

VXLAN benefits

• Supports more virtual switched domains than VLANs: Each VXLAN is uniquely identified by a 24-bit VXLAN

ID, called the VXLAN Network Identifier (VNI). The total number of VXLANs can reach 16 million. This
makes VXLAN a better choice than 802.1Q VLAN for isolating traffic for user terminals.

• A VXLAN segment differentiates individual logical networks so that several isolated layer 2 VXLAN

networks can coexist on a common layer 3 infrastructure. (Hosts in different VXLAN segments cannot
communicate with each other. Each VXLAN segment can be treated as a tenant in a data center
topology.)

• Easy to deploy and maintain: VXLAN only needs to be deployed on the edge devices of the transport

network. Devices in the transport network perform typical layer 3 forwarding.

VXLAN network model
A VXLAN is a virtual layer 2 network (known as the overlay network) built on top of an existing physical layer
3 network (known as the underlay network). VXLAN uses a logical tunnel to transport traffic between two
endpoints.

VXLAN encapsulates layer 2 Ethernet frames in layer 3 UDP packets, meaning virtual layer 2 subnets can
span underlying layer 3 networks. A VXLAN network identifier (VNI) is used to segment each layer 2 subnet
in a similar way as traditional VLAN IDs.

A VXLAN tunnel endpoint (VTEP) is a VXLAN-capable device that encapsulates and de-encapsulates packets.
In the physical network, a switch typically functions as a layer 2 or layer 3 VXLAN gateway and is considered
a hardware VTEP. The virtual network equivalents are known as software VTEPs, which are hosted in
hypervisors such as VMware ESXi or vSphere.

A tunnel endpoint is called a virtual tunnel endpoint (VTEP). VTEPs are responsible for encapsulation and
decapsulation of network traffic.

Chapter 2 VXLAN overview

9

Static VXLAN uses flood and learn (or ingress replication) to learn the MACs of the remote host, which
involves manual configurations of remote VXLAN Tunnel End Points (VTEPs) in the flood list. MP-BGP EVPN is
used to discover remote VTEPs and advertise MAC address and MAC/IP bindings in the VXLAN overlay, thus
eliminating the flood and learn. MP-BGP supports a new EVPN Network Layer Reachability Information
(NLRI) carried in BGP using Multiprotocol BGP Extensions with a newly defined Address Family Identifier (AFI)
and Subsequent Address Family Identifier (SAFI). Route Distinguisher (RD) is a unique number prepended to
the advertised address within the VRF, ensuring support for overlapping IP addresses and MACs across
different tenants. Routes can be imported and exported across VLANs and VRFs using a BGP extended
community called Route Target (RT) that are advertised along with the EVPN routes.

NOTE:

• Configuring static VTEPs is not supported when EVPN is enabled.

• The 6200 Switch Series supports static VXLAN only.

• VMware NSX-V integration and EVPN are mutually exclusive and cannot be configured

together.

• EVPN control pane is supported on the 6300, 6400, 8325, 8360, and 8400 Switch Series.

10

AOS-CX 10.06 VXLAN EVPN Guide

Overlay network VXLAN tunnelVNI/VXLAN 10VNI/VXLAN 20TerminalTerminalVNI/VXLAN 10VNI/VXLAN 20Underlay network TransportnetworkVTEP 1VTEP 2PSite 1 Site 2TerminalTerminal

VXLAN packet format
A VTEP encapsulates a frame in the following headers:

• 8-byte VXLAN header: VXLAN information for the frame.

◦ 24-bit VXLAN Network Identifier: Identifies the VXLAN of the frame. It is also called the virtual network

identifier (VNI).

◦ 8-bit flags: If the fifth bit (I flag) is 1, the VNI is valid. If the I flag is 0, the VNI is invalid. All other bits are

reserved and set to 0.

• 8-byte outer UDP header for VXLAN: The default VXLAN destination UDP port number is 4789.

• 20-byte outer IP header: Valid addresses of VTEPs or VXLAN multicast groups on the transport network.

Devices in the transport network forward VXLAN packets based on the outer IP header.

• 24-bit and 8-bit reserved fields.

Supported RFCs
VXLAN

• RFC 7348 - Virtual eXtensible Local Area Network (VXLAN)

• RFC 8365 - EVPN over NVE (VXLAN)

EVPN

• RFC 4760 - Multiprotocol Extensions for BGP-4

• RFC 7432 - BGP MPLS-Based Ethernet VPN

Chapter 2 VXLAN overview

11

Chapter 3
Static VXLAN

Static VXLAN (also know as unicast VXLAN), is the easiest way to connect two VTEPs. In this method, the
VXLAN uses a flooding-and-learning technique in the VXLAN data plane to learn the address of hosts.

Static VxLAN for IPv6 overlay is not supported. IPv4 overlay over static VxLAN has limitations with silent
hosts.

Configuring a static VXLAN

Prerequisites

• A enabled layer 3 interface with an IP address assigned to it, created with the command interface.

• A layer 3 VLAN.

Procedure

1. Create loopback interface 1 using the command interface loopback and assign a source IP to it.

2. Create VXLAN interface 1 with the command interface vxlan.

3. Enable VXLAN interface 1 with the command no shutdown.

4. Set the source IP address for the VXLAN tunnel with the command source ip.

5. Create a VNI with the command vni.

6. Define the IP address of the peer VTEP with the command vtep-peer.

7. Review VXLAN settings with the commands show interface vxlan1, show interface vxlan vni ,

and show interface vxlan vteps.

Example

This example creates a static VXLAN as follows:

• Creates loopback interface 1 with IP address 10.1.1.1/24.

• Creates VLAN 2.

• Creates VXLAN interface 1.

• Sets the source IP address for the VXLAN tunnel to 10.1.1.1.

• Creates VNI 2.

• Sets the VTEP peer to 200.1.1.1.

• Associates VLAN 2 with VNI 2.

switch(config)# loopback 1
switch(config-if)# ip address 10.1.1.1/24
switch(config-if)# exit

12

AOS-CX 10.06 VXLAN EVPN Guide

switch(config)# interface vxlan 1
switch(config-vxlan-if)# no shutdown
switch(config-vxlan-if)# source ip 10.1.1.1
switch(config-vxlan-if)# vni 2
switch(config-vni-2)# vtep-peer 200.1.1.1
switch(config-vni-2)# vlan 2
switch(config-vni-2)# exit
switch(config-vxlan-if)# exit
switch(config-if)# exit

Static VXLAN with a single VNI between two VTEPs
This example creates a static VXLAN tunnel between two switches, enabling traffic from two networks to
traverse an underlay IP network.

Procedure

1. On switch 1:

a. Enable loopback interface 1 and assign the IP address 10.10.10.1/24 to it.

switch# config
switch(config)# interface loopback 1
switch(config-loopback-if)# ip address 10.10.10.1/24
switch(config-if)# exit
switch(config)#

b. Enable interface 1/1/1 and assign the IP address 100.1.1.1/24 to it.

switch(config)# interface 1/1/1
switch(config-if)# routing (6300/6400 only)
switch(config-if)# ip address 100.1.1.1/24
switch(config-if)# no shutdown
switch(config-if)# exit
switch(config)#

c. Create VLAN 10.

switch(config)# vlan 10
switch(config-vlan-10)# exit

Chapter 3 Static VXLAN

13

d. Enable interface 1/1/2 and assign VLAN 10 to it.

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing  (8325/8360/8400 only)
switch(config-if)# vlan access 10
switch(config-if)# exit

e. Create VXLAN interface 1 and assign the loopback source IP address 10.10.10.1 to it.

switch(config)# interface vxlan 1
switch(config-vxlan-if)# source ip 10.10.10.1
switch(config-vxlan-if)# no shutdown

f. Create VNI 10, and assign the VTEP peer address 20.20.20.1 and VLAN 10 to it.

switch(config-vxlan-if)# vni 10
switch(config-vni)# vtep-peer 20.20.20.1
switch(config-vni)# vlan 10
switch(config-vni)# exit
switch(config-vxlan-if)# exit

g. Add a route to the peer VTEP peer address 20.20.20.1.

switch(config)# ip route 20.20.20.1 100.1.1.2

2. On switch 2:

a. Enable loopback interface 2 and assign the IP address 20.20.20.1/24 to it.

switch# config
switch(config)# interface loopback 2
switch(config-loopback-if)# ip address 20.20.20.1/24
switch(config-if)# exit
switch(config)#

b. Enable interface 1/1/1 and assign the IP address 200.1.1.1/24 to it.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# routing  (6300/6400 only)
switch(config-if)# ip address 200.1.1.1/24
switch(config-if)# no shutdown
switch(config-if)# exit

c. Create VLAN 10.

switch(config)# vlan 10
switch(config-vlan-10)# exit

d. Enable interface 1/1/2 and assign and VLAN 10 to it.

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing  (8325/8360/8400 only)
switch(config-if)# vlan access 10
switch(config-if)# exit

14

AOS-CX 10.06 VXLAN EVPN Guide

e. Create VXLAN interface 1 and assign the source IP address 20.20.20.1 to it.

switch(config)# interface vxlan 1
switch(config-vxlan-if)# source ip 20.20.20.1
switch(config-vxlan-if)# no shutdown

f. Create VNI 10, and assign the VTEP peer address 10.10.10.1 and VLAN 10 to it.

switch(config-vxlan-if)# vni 10
switch(config-vni)# vtep-peer 10.10.10.1
switch(config-vni)# vlan 10
switch(config-vni)# exit
switch(config-vxlan-if)# exit
switch(config)#

g. Add a route to the peer VTEP peer address 10.10.10.1.

switch(config)# ip route 10.10.10.1 200.1.1.2

Static VXLAN with multiple VNIs between two VTEPs
This example creates two static VXLAN tunnels between two switches, enabling traffic from two networks to
traverse underlay IP network.

Chapter 3 Static VXLAN

15

Procedure

1. On switch 1:

a. Enable loopback interface 1 and assign the IP address 10.10.10.1/24 to it.

switch# config
switch(config)# interface loopback 1
switch(config-loopback-if)# ip address 10.10.10.1/24
switch(config-if)# exit
switch(config)#

b. Enable interface 1/1/1 and assign the IP address 100.1.1.1/24 to it.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# routing  (6300/6400 only)
switch(config-if)# ip address 100.1.1.1/24
switch(config-if)# no shutdown
switch(config-if)# exit
switch(config)#

c. Create VLAN 10 and VLAN 20.

switch(config)# vlan 10,20
switch(config-vlan-10)# exit

d. Enable interface 1/1/2 and assign VLAN 10 to it.

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing  (8325/8360/8400 only)
switch(config-if)# vlan access 10
switch(config-if)# exit
switch(config)#

e. Enable interface 1/1/3 and assign VLAN 20 to it.

switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing  (8325/8360/8400 only)
switch(config-if)# vlan access 20
switch(config-if)# exit
switch(config)#

f. Create VXLAN interface 1 and assign the source IP address 10.10.10.1 to it.

switch(config)# interface vxlan 1
switch(config-vxlan-if)# source ip 10.10.10.1
switch(config-vxlan-if)# no shutdown

g. Create VNI 10, and assign the VTEP peer address 20.20.20.1 and VLAN 10 to it.

switch(config-vxlan-if)# vni 10
switch(config-vni)# vtep-peer 20.20.20.1
switch(config-vni)# vlan 10

16

AOS-CX 10.06 VXLAN EVPN Guide

switch(config-vni)# exit
switch(config-vxlan-if)# exit

h. Create VNI 20, and assign the VTEP peer address 20.20.20.1 and VLAN 20 to it.

switch(config-vxlan-if)# vni 20
switch(config-vni)# vtep-peer 20.20.20.1
switch(config-vni)# vlan 20
switch(config-vni)# exit
switch(config-vxlan-if)# exit
switch(config)#

2. On switch 2:

a. Enable loopback interface 2 and assign the IP address 20.20.20.1/24 to it.

switch# config
switch(config)# interface loopback 2
switch(config-loopback-if)# ip address 20.20.20.1/24
switch(config-if)# exit
switch(config)#

b. Enable interface 1/1/1 and assign the IP address 200.1.1.1/24 to it.

switch# config
switch(config)# interface 1/1/1
switch(config-if)# routing  (6300/6400 only)
switch(config-if)# ip address 200.1.1.1/24
switch(config-if)# no shutdown
switch(config-if)# exit
switch(config)#

c. Create VLAN 10 and VLAN 20.

switch(config)# vlan 10,20
switch(config-vlan-10)# exit

d. Enable interface 1/1/2 and assign VLAN 10 to it.

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# no routing  (8325/8360/8400 only)
switch(config-if)# vlan access 10
switch(config-if)# exit
switch(config)#

e. Enable interface 1/1/3 and assign VLAN 20 to it.

switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing  (8325/8360/8400 only)
switch(config-if)# vlan access 20
switch(config-if)# exit
switch(config)#

f. Create VXLAN interface 1 and assign the source IP address 20.20.20.1 to it.

switch(config)# interface vxlan 1
switch(config-vxlan-if)# source ip 20.20.20.1
switch(config-vxlan-if)# no shutdown

Chapter 3 Static VXLAN

17

g. Create VNI 10, and assign the VTEP peer address 10.10.10.1 and VLAN 10 to it.

switch(config-vxlan-if)# vni 10
switch(config-vni)# vtep-peer 10.10.10.1
switch(config-vni)# vlan 10
switch(config-vni)# exit
switch(config-vxlan-if)# exit

h. Create VNI 20, and assign the VTEP peer address 10.10.10.1 and VLAN 20 to it.

switch(config-vxlan-if)# vni 20
switch(config-vni)# vtep-peer 10.10.10.1
switch(config-vni)# vlan 20
switch(config-vni)# exit
switch(config-vxlan-if)# exit
switch(config)#

18

AOS-CX 10.06 VXLAN EVPN Guide

Chapter 4
VXLAN with BGP EVPN

(Not supported on the 6200 Switch Series.)

Ethernet VPN (EVPN) is used as the overlay control plane to exchange layer 2 and layer 3 connectivity
information between different layer 2/3 domains over an IP or IP/MPLS underlay network.

The initial EVPN standard RFC 7432 defined the BGP EVPN control plane and specifies an MPLS data-plane.
The control plane with an MPLS data plane was extended to consider additional data plane encapsulations
models. These models include VXLAN, NVGRE, and MPLS over GRE which is detailed in RFC 8365. This
section focuses on EVPN and its operation with a VXLAN data plane for building overlay networks.

EVPN, as an overlay, supports multi-tenancy and is highly extensible, often using resources from different
overlay fabric networks (like data centers) to deliver a single service. It can provide layer 2 connectivity over
physical infrastructure for devices in a virtual network, or enable layer 3 routing.

In a Clos topology (leaf-spine) deployment of a Vxlan fabric, leaf nodes are configured as VTEPs to provide
VXLAN services and spine nodes perform layer-3 routing on the outer headers IP/UDP encapsulation. If all
VTEPs and underlay network devices of an EVPN network belong to the same AS, the spine nodes can act as
route reflectors (RRs) to reflect routes between the VTEPs. In this scenario, the spine nodes receive and
advertise BGP EVPN routes, but do not perform VXLAN encapsulation and de-encapsulation. If eBGP is used,
the spines will forward the routes from one leaf to the other as inherent functionality of eBGP.

The IETF specifies two methods for supporting inter-subnet routing with EVPN: symmetric and asymmetric
integrated routing and bridging (IRB). The main difference between the two methods is that the symmetric
method supports both routing and bridged on both the ingress and egress VTEPs, where the asymmetric
method supports routing on the ingress, but only bridging on the egress.

AOS-CX supports Centralized L3 gateways and Symmetric IRB Distributed L3 gateways.

Chapter 4 VXLAN with BGP EVPN

19

Ethernet VPN (EVPN)-based VXLAN overview
Ethernet VPN (EVPN) is a standards-based BGP control plane to advertise MAC addresses, MAC/IP bindings,
IP Prefixes, and so on. The initial EVPN standard RFC 7432 defined the BGP EVPN control plane and specifies
an MPLS data-plane. The control plane with an MPLS data plane was extended to consider additional data
plane encapsulations models. These models include VXLAN, NVGRE, and MPLS over GRE which is detailed in
RFC 8365. This section focuses on EVPN and its operation with a VXLAN data plane for building overlay
networks.

Static VXLAN uses flood and learn (or ingress replication) to learn the MACs of the remote host, which
involves manual configurations of remote VXLAN Tunnel End Points (VTEPs) in the flood list. MP-BGP EVPN is
used to discover remote VTEPs and advertise MAC address and MAC/IP bindings in the VXLAN overlay, thus
eliminating the flood and learn. MP-BGP supports a new EVPN Network Layer Reachability Information
(NLRI) carried in BGP using Multiprotocol BGP Extensions with a newly defined Address Family Identifier (AFI)
and Subsequent Address Family Identifier (SAFI). Route Distinguisher (RD) is a unique number prepended to
the advertised address within the VRF, ensuring support for overlapping IP addresses and MACs across
different tenants. Routes can be imported and exported across VLANs and VRFs using a BGP extended
community called Route Target (RT) that are advertised along with the EVPN routes.

NOTE: Configuring static VTEPs is not supported when EVPN is enabled.

VMware NSX-V integration and EVPN are mutually exclusive and cannot be configured together.

EVPN control pane is supported on the 6300, 6400, 8325, 8360, and 8400 switches.

See also Border Gateway Protocol (BGP) in the IP Routing Guide.

Asymmetric IRB
Asymmetric IRB uses different VNIs for bi-directional traffic between 2 hosts on different Layer-2 VNIs. For
example:

20

AOS-CX 10.06 VXLAN EVPN Guide

1. Host1 in VLAN 10/VNI 10 connected to VTEP1 sends traffic to Host2 in VLAN 20/VNI 20 connected to

VTEP2.

a. Traffic from Host1 is sent to VTEP1 VLAN 10/ VNI 10 gateway MAC.

2. VTEP1 routes traffic to VNI 20, encapsulates frame with VXLAN, adds outer Source/Destination IP, VNI info

and sends traffic to VTEP2.

a. VTEP1 should already have a MAC/ARP entry for Host2.

b. The inner Source MAC is changed to VTEP1 VLAN 20 gateway MAC and inner Destination MAC is

changed to MAC2 which belongs to Host2.

3. VTEP2 decapsulates outer VXLAN, bridges and sends the traffic to Host2 on VLAN 20/VNI 20.

a. Host2 will see source MAC as VTEP1.

Return traffic from Host2 to Host1 is similar. Traffic from Host2 is sent to VTEP2 VLAN20/VNI 20 gateway
MAC. VTEP2 routes traffic to VNI 10, encapsulates and sends the traffic to VTEP1. VTEP1 will decapsulate,
bridge and send the traffic to Host1 on VLAN 10/VNI 10.

As seen from the traffic flow:

• Asymmetric IRB needs both source and destination Layer-2 VNIs to be configured on the ingress VTEP.

• Routing and bridging is used on the ingress VTEP.

• Bridging is used on the egress VTEP.

• Bi-directional traffic uses asymmetric paths:

◦ Host1 to Host2 uses VNI 10 -> VNI 20.

◦ Host2 to Host1 uses VNI 20 -> VNI 10.

• Asymmetric IRB will lead to increased ARP/MAC scale on VTEPs as they need to contain MAC/ARP of both

source/destination hosts.

•

If Asymmetric IRB is used, all subnets/VNIs have to be configured on all VTEPs. As previously shown, it is
not mandatory for a subnet to span across all VTEPs in both Data Center and Campus networks, e.g.
10.10.220.0/24 only exists on Leaf1A/1B, Leaf2A/2B in Figure 2, 10.10.220.0/24 only exists in Building#1.

Symmetric IRB
Symmetric IRB uses the same Layer-3 VNI for bi-directional traffic between two hosts on different VLANs/
VNIs. For example:

Chapter 4 VXLAN with BGP EVPN

21

1. Host1 in VLAN 10/VNI 10 connected to VTEP1 sends traffic to Host2 in VLAN 20/VNI 20 connected to

VTEP2.

a. Traffic from Host1 is sent to VTEP1 VLAN 10/ VNI 10 gateway MAC.

2. VTEP1 routes traffic in the VRF (mapping to L3-VNI 1020), encapsulates traffic with VXLAN, adds outer

Source/Destination IP, VNI info and sends traffic to VTEP2.

a. VTEP1 does not need to have a MAC/ARP entry for Host2.

b. VTEP1 learns the prefix route and/or host route corresponding to Host2 via EVPN Route type 5 or 2

respectively thus facilitating routing to the destination.

c. The inner Source MAC is changed to VTEP1 router MAC and inner Destination MAC is changed to

VTEP2 router MAC.

3. VTEP2 decapsulates outer VXLAN, routes and sends the traffic to Host2 on VLAN 20/VNI 20.

a. Host2 will see source MAC as VTEP2 gateway MAC.

Return traffic from Host2 to Host1 is similar, traffic from Host2 is sent to VTEP2 VLAN20/VNI 20 gateway
MAC. VTEP2 routes traffic to L3 VNI 1020, encapsulates and sends the traffic to VTEP1. VTEP1 decapsulates,
route and send the traffic to Host1 on VLAN 10/VNI 10.

As seen from the traffic flow:

• Routing is used on both ingress and egress VTEPs.

• Bi-directional traffic uses symmetric path; same L3 VNI in both directions.

• VTEPs do not need to hold unnecessary ARP/MAC resources.

• Destination VLAN/VNI does not have to be configured on source VTEP.

22

AOS-CX 10.06 VXLAN EVPN Guide

Example of external connectivity and IVRL with
symmetric IRB
In symmetric IRB deployment, IVRL is typically configured at the border VTEPs.

At the border VTEP, host routes (published by remote VTEPS via route type-2) are installed. Similarly, the
EVPN type-5 prefixes advertised by other VTEPs get installed as prefix-routes (for example, a /24 prefix for
IPv4 overlay network). These routes can further be aggregated and leaked to a different VRF (for example, a
VRF named external) and then be advertised to external network via protocols such as OSPF or EBGP.

Similarly, at the border VTEP, the routes at VRF external can be leaked to EVPN overlay VRFs and then be
advertised as type-5 prefixes to all other VTEPs.

Example

This example shows the topology and sample configuration where IVRL is used along with symmetric IRB:

There are 2 VTEPs, namely VTEP1 and VTEP2. VTEP2 is the Border VTEP. Both the VTEPs have two tenant
VRFs, namely VRF red and VRF blue. At VTEP2, there is an additional VRF external configured to have an
external connectivity with EXT_RTR. EXT_RTR is a router running OSPF. At VTEP2, OSPF routes received from
EXT_RTR at VRF external are leaked to VRF red and VRF blue (by configuring redistribute ospf in the
router bgp context and configuring route targets required for route leaking), and then the leaked routes
are advertised as EVPN type 5 prefixes to VTEP1.

Also at VTEP2, EVPN overlay routes in VRF red and VRF blue are leaked to VRF external and then the leaked
routes are advertised by OSPF (by configuring redistribute bgp in the router ospf context) to the
external router.

SPINE:
-----
!
router ospf 1
    router-id 2.2.2.2
    area 0.0.0.0
interface 1/1/1
    no shutdown
    routing

Chapter 4 VXLAN with BGP EVPN

23

ip address 10.10.10.2/24
    ip ospf 1 area 0.0.0.0
interface 1/1/2
    no shutdown
    routing
    ip address 20.20.20.2/24
    ip ospf 1 area 0.0.0.0
interface loopback 1
    ip address 2.2.2.2/24
    ip ospf 1 area 0.0.0.0
router bgp 1
    neighbor 1.1.1.1 remote-as 1
    neighbor 1.1.1.1 update-source loopback 1
    neighbor 3.3.3.3 remote-as 1
    neighbor 3.3.3.3 update-source loopback 1
    address-family l2vpn evpn
        neighbor 1.1.1.1 activate
        neighbor 1.1.1.1 route-reflector-client
        neighbor 1.1.1.1 send-community extended
        neighbor 3.3.3.3 activate
        neighbor 3.3.3.3 route-reflector-client
        neighbor 3.3.3.3 send-community extended
    exit-address-family

LEAF1:
-----
vrf blue
    rd 1:100
    route-target export 1:100 evpn
    route-target import 1:100 evpn
vrf red
    rd 1:200
    route-target export 1:200 evpn
    route-target import 1:200 evpn
!
vlan 1,20,40
virtual-mac 00:01:00:00:00:00
!
router ospf 1
    router-id 1.1.1.1
    area 0.0.0.0
evpn
    vlan 20
        rd auto
        route-target export auto
        route-target import auto
    vlan 40
        rd auto
        route-target export auto
        route-target import auto
interface 1/1/1
    no shutdown
    routing
    ip address 10.10.10.1/24
    ip ospf 1 area 0.0.0.0
interface 1/1/2
    no shutdown
    no routing
    vlan access 20
interface 1/1/3
    no shutdown
    no routing
    vlan access 40
interface loopback 1

24

AOS-CX 10.06 VXLAN EVPN Guide

ip address 1.1.1.1/24
    ip ospf 1 area 0.0.0.0
interface vlan20
    vrf attach blue
    ip address 100.100.20.2/24
    active-gateway ip mac 00:01:00:00:00:01
    active-gateway ip 100.100.20.1
interface vlan40
    vrf attach red
    ip address 200.200.40.2/24
    active-gateway ip mac 00:01:00:00:00:01
    active-gateway ip 200.200.40.1
interface vxlan 1
    source ip 1.1.1.1
    no shutdown
    vni 20
        vlan 20
    !
    vni 40
        vlan 40
    !
    vni 10000
        routing
        vrf blue
    vni 20000
        routing
        vrf red
router bgp 1
    neighbor 2.2.2.2 remote-as 1
    neighbor 2.2.2.2 update-source loopback 1
    address-family l2vpn evpn
        neighbor 2.2.2.2 activate
        neighbor 2.2.2.2 send-community extended
    exit-address-family
!
    vrf blue
        address-family ipv4 unicast
            redistribute connected
        exit-address-family
!
    vrf red
        address-family ipv4 unicast
            redistribute connected
        exit-address-family
!

LEAF2: (Border leaf)
-----
vrf blue
    rd 1:100
    route-target export 1:100 evpn
    route-target import 1:100 evpn
    address-family ipv4 unicast
        route-target export 1:100
        route-target import 1:300
    exit-address-family
vrf red
    rd 1:200
    route-target export 1:200 evpn
    route-target import 1:200 evpn
    address-family ipv4 unicast
        route-target export 1:200
        route-target import 1:300
    exit-address-family

Chapter 4 VXLAN with BGP EVPN

25

vrf external
    rd 1:300
    address-family ipv4 unicast
        route-target export 1:300
        route-target import 1:100
        route-target import 1:200
    exit-address-family
vlan 1,10,30
virtual-mac 00:02:00:00:00:00
!
router ospf 1
    router-id 3.3.3.3
    area 0.0.0.0
router ospf 1 vrf external
    router-id 30.1.1.1
    redistribute bgp
    area 0.0.0.0
evpn
    vlan 10
        rd auto
        route-target export auto
        route-target import auto
    vlan 30
        rd auto
        route-target export auto
        route-target import auto
interface 1/1/1
    no shutdown
    routing
    ip address 20.20.20.1/24
    ip ospf 1 area 0.0.0.0
interface 1/1/2
    no shutdown
    no routing
    vlan access 10
interface 1/1/3
    no shutdown
    no routing
    vlan access 30
interface 1/1/4
    no shutdown
    routing
    vrf attach shared
    ip address 30.1.1.1/24
    ip ospf 1 area 0.0.0.0
interface loopback 1
    ip address 3.3.3.3/24
    ip ospf 1 area 0.0.0.0
interface vlan10
    vrf attach blue
    ip address 100.100.10.2/24
    active-gateway ip mac 00:02:00:00:00:02
    active-gateway ip 100.100.10.1
interface vlan30
    vrf attach red
    ip address 200.200.30.2/24
    active-gateway ip mac 00:02:00:00:00:02
    active-gateway ip 200.200.30.1
interface vxlan 1
    source ip 3.3.3.3
    no shutdown
    vni 10
        vlan 10
    !

26

AOS-CX 10.06 VXLAN EVPN Guide

vni 30
        vlan 30
    !
    vni 10000
        routing
        vrf blue
    !
    vni 20000
        routing
        vrf red
    !
router bgp 1
    neighbor 2.2.2.2 remote-as 1
    neighbor 2.2.2.2 update-source loopback 1
    address-family l2vpn evpn
        neighbor 2.2.2.2 activate
        neighbor 2.2.2.2 send-community extended
    exit-address-family
!
    vrf blue
        address-family ipv4 unicast
            redistribute connected
        exit-address-family
!
    vrf red
        address-family ipv4 unicast
            redistribute connected
        exit-address-family
!
    vrf external
        address-family ipv4 unicast
            redistribute connected
            redistribute ospf
        exit-address-family
!

EXT_RTR(OSPF): Router connected to border leaf
-------------
vrf external
router ospf 1 vrf external
    router-id 30.1.1.2
    area 0.0.0.0
interface 1/1/1
    no shutdown
    routing
    vrf attach external
    ip address 30.1.1.2/24
    ip ospf 1 area 0.0.0.0
interface 1/1/2
    no shutdown
    routing
    vrf attach external
    ip address 40.1.1.1/24
    ip ospf 1 area 0.0.0.0

NOTE: The locally learned neighbor entries (ARP/ND) on a VTEP, dynamically learned (via data
plane) over client/tenant-facing SVI, can be published as host routes via Route Type-2 only over
the BGP-EVPN control plane. These dynamic entries cannot be redistributed as host routes in a
non BGP-EVPN routing domain. For example, in the figure above, redistribute host-route
is configured under the EVPN-VLAN context to ensure that locally learned ARP entries at VTEP2
are advertised in Route Type-2 as /32 prefixes to VTEP1. However, these ARP entries cannot be
advertised as /32 routes to EXT_RTR.

Chapter 4 VXLAN with BGP EVPN

27

MP-BGP extension for EVPN
The following are some important EVPN route types:

• Ethernet auto-discovery route (Route 1)—Advertises Ethernet Segment (ES) information in

multihomed sites.

• MAC/IP advertisement route (Route 2)—Advertises MAC, MAC/IP(v6) bindings (mapping to neighbor

entry and/or host route) of the locally learned host.

•

Inclusive Multicast Ethernet tag (IMET) route (Route 3)—Advertises VTEP and VXLAN mappings for
automating VTEP discovery, VXLAN tunnel establishment, and VXLAN tunnel assignment.

• Ethernet Segment route (Route 4)—Advertises ES and VTEP mappings.

•

IP Prefix advertisement route (Route 5)—Advertises BGP IPv4 or IPv6 unicast routes as IP prefixes.

MP-BGP uses the route distinguisher (RD) field to differentiate BGP EVPN routes of different L2 domains and
uses route targets to control the advertisement and acceptance of BGP EVPN routes. MP-BGP supports the
following types of route targets:

• Export Route Target—A VTEP sets the export targets for BGP EVPN routes learned from the local site

before advertising them to remote VTEPs.

•

Import Route Target—A VTEP which receives the EVPN routes imports them if any of the route targets in
the received route matches with any of the locally configured import route targets.

NOTE: The current release supports only MAC and MAC/IP advertisement (route type 2),
Inclusive multicast Ethernet tag (IMET) routes (route type 3), and IP prefix route advertisement
(route type 5).

Auto-discovery via EVPN
VTEPs use BGP EVPN routes to discover VTEP neighbors, establish VXLAN tunnels, and assign the tunnels to
VNIs.

•

IMET route—VTEPs advertise their locally configured L2 VNIs through IMET routes. Two VTEPs configured
with the same L2 VNI provision VXLAN tunnel mapping to remote VTEP and L2 VNI. IMET is leveraged to
create the replication list for the forwarding of Broadcast, Unknown Unicast, and Multicast (BUM) traffic.

• MAC/IP advertisement route and IP prefix advertisement route—In the EVPN deployment, VTEPs
advertise MAC/IP advertisement routes or IP prefix advertisement routes which are imported by the
other VTEPs based on route targets.

Layer 2 forwarding

MAC learning

The VTEP learns MAC addresses by using the following methods:

28

AOS-CX 10.06 VXLAN EVPN Guide

• Local MAC learning—The VTEP automatically learns the source MAC addresses of frames sent from the

local site. The outgoing interfaces of local MAC address entries are interfaces on which the MAC
addresses are learned.

• Remote MAC learning—The VTEP uses MP-BGP to advertise local MAC reachability information to

remote VTEPs and learn MAC reachability information from remote VTEPs. The outgoing interfaces of
MAC address entries advertised from a remote site are VXLAN tunnel interfaces. A remote host's MAC
address entries are not learned from the dataplane over the VXLAN fabric.

Unicast

In the following example, VTEP 1 performs Layer 2 forwarding for local MAC learning and forwarding:

In the following example, VTEP 1 performs remote MAC learning and forwarding:

Chapter 4 VXLAN with BGP EVPN

29

VTEP1VTEP2UnderlaynetworkMAC table on VTEP 1VLANMACInterfaceVLAN 10MAC_T1Interface AVLAN 20MAC_T4Interface AInterface BVXLAN tunnelInterface BHost 4Host 5Host 6Host 7Host 8Host 9Host 1Host 2Host 3

MAC table on VTEP 1
Host 1
|     |     | VLAN | MAC | Interface |     |     |     |
| --- | --- | ---- | --- | --------- | --- | --- | --- |
Host 2
|        |     | VLAN 10 | MAC_T1 | Interface A |     |     |     |
| ------ | --- | ------- | ------ | ----------- | --- | --- | --- |
| Host 3 |     | VLAN 10 | MAC_T7 | Tunnel 1    |     |     |     |
Host 7
VXLAN tunnel 1
Interface A
Host 8
Interface A
Interface B
Host 9
| Host 4 | VTEP1 |     |     | Underlay |     | VTEP2 |     |
| ------ | ----- | --- | --- | -------- | --- | ----- | --- |
network
Host 5
MAC table on VTEP 2
Host 6
|     |     |     |     |     | VLAN    | MAC    | Interface   |
| --- | --- | --- | --- | --- | ------- | ------ | ----------- |
|     |     |     |     |     | VLAN 10 | MAC_T1 | Tunnel 1    |
|     |     |     |     |     | VLAN 10 | MAC_T7 | Interface A |
The following process applies to remote MAC learning and forwarding:
1. The source VTEP encapsulates the Ethernet frame in the VXLAN/UDP/IP header.
In the outer IP header, the source IP address is the source VTEP's VXLAN tunnel source IP address. The
destination IP address is the VXLAN tunnel destination IP address.
2. The source VTEP forwards the encapsulated packet out of the outgoing VXLAN tunnel interface.
3. The intermediate underlay devices forward the packet to the destination VTEP by using the outer IP
header.
4. The destination VTEP removes the headers on top of the inner Ethernet frame. It then performs MAC
address table lookup in the VXLAN's VNI to forward the frame out of the matching outgoing interface.
30 AOS-CX 10.06 VXLAN EVPN Guide

Flood

A VTEP floods a Broadcast, Unknown Unicast, and Multicast (BUM) traffic to all local interfaces excluding the
incoming interface. The source VTEP also replicates the flood frame, and then sends one replica to the
destination IP address of each VXLAN tunnel in the VXLAN. Each destination VTEP floods the inner Ethernet
frame to all the host/tenant facing interfaces. To avoid loops, the default VXLAN split horizon rule applies
where the destination VTEPs do not flood the frame to VXLAN tunnels.

NOTE: For BUM traffic flooding, only Head End Replication (HER) is supported.

Layer 3 forwarding
EVPN uses either Centralized L3 gateway or Distributed L3 gateways to provide Layer 3 forwarding services
for hosts in VXLANs.

• Centralized L3 gateway: Uses one VTEP to provide Layer 3 forwarding for VXLANs. Typically, the

gateway-collocated VTEP connects to other VTEPs and the external network.

• Distributed L3 gateway: Deploys one EVPN gateway on each VTEP to provide optimized Layer 3

forwarding for directly connected hosts.

In either design, the gateways use virtual Layer 3 interfaces as gateway interfaces for VXLANs. An AOS-CX
switch cannot participate in both Centralized L3 gateway and Distributed L3 gateway topologies at the same
time.

Chapter 4 VXLAN with BGP EVPN

31

VTEP1VTEP2VTEP3Replicate and encapsulateVXLAN tunnelVXLAN tunnelVXLAN tunnelHost 4Host 5Host 6Host 10Host 11Host 12UnderlaynetworkHost 7Host 8Host 9Host 1Host 2Host 3

Centralized L3 gateway deployment

In the following topology, a VTEP acts as a routing (Layer 3) gateway for hosts. This is the only VTEP in the
VXLAN fabric, that performs Layer 3 forwarding (routing). All other VTEPs are configured to perform Layer 2
bridging.

The network uses the following process to forward Layer 3 traffic from a host to the destination:

1. The centralized gateway (VTEP) publishes the gateway MAC(s) for all Layer-3 Gateway SVIs (with a L2 VNI

mapping), to all other VTEPs.

2. Traffic is triggered by VM in VPNA (for example, 10.1.1.10/24) to VM (for example, 10.1.2.11/24) behind

remote VTEP in VPNB (see the topology diagram for network details).

3. The host sends an ARP request to obtain the MAC address of the SVI interface that acts as the gateway,

and then sends the Layer 3 traffic to the Centralized L3 gateway.

4. The first hop VTEP looks up the matching MAC address table and forwards the traffic to the Centralized

L3 gateway through a VXLAN tunnel.

5. The Centralized L3 gateway removes the VXLAN encapsulation and performs route lookup. In case the
corresponding neighbor entry (ARP/ND) is found missing for the destination IP address, it performs
neighbor resolution (ARP/ND) in the context Layer-2 VNI, that maps to the corresponding gateway SVI
interface.

6. After resolving the neighbor entry, for subsequent packets received with same credentials, the

centralized gateway performs VXLAN encapsulation of the packet with the destination VNI and forwards
the packet to the destination VTEP.

7. Any return traffic follows the same set of procedures described above.

NOTE: From release 10.04 onwards, Active Gateway must be configured for Centralized L3
gateway deployments (both VSX and standalone).

32

AOS-CX 10.06 VXLAN EVPN Guide

Distributed L3 Anycast gateway

As the name suggests, all VTEPs, that are connected to hosts or clients belonging to same subnet, are
configured with same gateway IP and MAC address (for the subnet), thus making this configuration anycast
in nature. The (anycast) gateway IP and MAC address is configured on the client/tenant facing SVI interface.

Anycast gateway configuration is done using the active-gateway command under an SVI interface. For
example:

switch(config)# interface vlan 10
switch(config-if-vlan)# active-gateway ip 10.1.1.1 mac 00:00:02:02:02:02

Active-gateway configuration recommendations for an EVPN environment

• The active gateway virtual IP configuration must not be the same as the physical IP configuration of the

interface.

• Same active gateway virtual IP and physical IP cannot be configured for an EVPN environment. If

configured, it can lead to flooding of data traffic.

• Physical IP addresses configured on the SVI interface on VSX-primary and VSX-secondary must be

different. (Note that the same rule would also apply if active gateway is configured on each VTEP to
implement asymmetric IRB with distributed gateway.)

• The Active Gateway MAC for both IPv6 and IPv4 on the tenant SVI should be identical for Anycast

Gateway configuration.

• The Active Gateway IPv6 address should be a link local address and identical on both VSX peers.

Symmetric IRB

Symmetric IRB involves routing and bridging on both ingress and egress VTEPs. Thus ensuring that
bidirectional traffic is tagged with same L3VNI, indicating routing operation to be performed on the egress
VTEP. Ingress VTEP routes the traffic between the source subnet and destination subnet, in a VRF (Virtual
Routing and Forwarding), and sends the packet to the egress VTEP, encapsulated with L3VNI. Both ingress
and egress VTEPs have the VRF mapped to the same L3VNI. The egress VTEP, routes the packet to, the
destination subnet in the VRF (mapped to Layer3-VNI).

Symmetric IRB is an optimal solution in a large-scale network, as VTEPs can be selectively configured as
gateway for the subnets present on the directly connected hosts.

Symmetric IRB with distributed Anycast Gateway

Virtual Extensible LAN (VXLAN) tunnels created by Multi-Protocol BGP (MP-BGP) Ethernet VPN (EVPN) are
typically deployed on VXLAN Tunnel End Points (VTEPs) to provide L2 network connectivity over a L3 Data
Center network deployed in a Pod or Availability Zone. For example:

Chapter 4 VXLAN with BGP EVPN

33

VSX Leaf switches in a rack form a logical VTEP and border leafs connect the EVPN domain to a L3 DC core
via EBGP IPv4 peering. OSPF/IBGP EVPN is used within the Pod. Spine switches are configured as IBGP EVPN
Route Reflectors (RRs), while Leaf VTEPs are configured as EVPN RR clients.

Distributed L3 Gateways can be deployed across the overlay network to optimize L3 network connectivity
and minimize latency between Virtual Machines (VMs) within a rack as follows:

With Distributed L3 Gateways, the anycast 10.10.10.1/24 and 10.10.11.1/24 IPs are configured on Leaf1A/
Leaf1B and Leaf2A/Leaf2B. Traffic between VMs 10.10.10.10/24 and 10.10.11.10/24 is routed directly on
Leaf1A/Leaf1B, while traffic between VMs 10.10.10.11/24 and 10.10.11.11/24 is routed directly on Leaf2A/
Leaf2B.

Distributed L3 Gateways can also be deployed in a campus network to optimize L3 network connectivity and
minimize latency between clients connected to the same access switch. For example:

34

AOS-CX 10.06 VXLAN EVPN Guide

With Distributed L3 Gateways, the anycast 10.10.10.1/24 and 10.10.11.1/24 IPs are configured on access VSF
6300 and access 6400 in Campus building #1. Traffic between clients 10.10.10.10/24 and 10.10.11.10/24 is
routed directly on access VSF 6300, while traffic between clients 10.10.10.11/24 and 10.10.11.11/24 is routed
directly on access 6400.
VRFs can be added to VTEPs for L3 multi-tenancy across a VXLAN/EVPN overlay network.
In a campus, it is typical for different buildings to utilize different subnets. L3 VXLAN routing between
different subnets on building #1 and building #2 would utilize the L3 VXLAN Network Identifier (VNI)
assigned to its VRF. It is also possible to extend L2 VXLAN across buildings for IoT devices that need to
remain on the same subnet.
VXLAN/EVPN symmetric IRB distributed L3 gateways example
This example provides an overview of a VXLAN/EVPN symmetric IRB distributed L3 gateways deployment.
Pod1
|     | Spine1 Spine2 |     |     |
| --- | ------------- | --- | --- |
OSPF Area 0
AS#65001
Overlay
|     | RR1 | RR2 |     |
| --- | --- | --- | --- |
VXLAN
Tunnel
VRF1 Default Gateways VRF1 L3 VNI 10101 VRF1 Default Gateways
Int VLAN 10 - 10.1.10.1/24 fe80::10 Int VLAN 10 - 10.1.10.1/24 fe80::10
Int VLAN 11 - 10.1.11.1/24 fe80::11 Int VLAN 11 - 10.1.12.1/24 fe80::12
|               | Logical Logical |        |               |
| ------------- | --------------- | ------ | ------------- |
| Leaf1A        | Leaf1B          | Leaf2A | Leaf2B        |
|               | VTEP#1 VTEP#2   |        |               |
| VMs           |                 |        | VMs           |
| 10.1.10.10/24 |                 |        | 10.1.10.11/24 |
| 10.1.11.10/24 |                 |        | 10.1.12.10/24 |
Topology details
Chapter 4 VXLAN with BGP EVPN 35

•

Leaf1A/Leaf1B (logical VTEP#1) are in rack1, Leaf2A/Leaf2B (logical VTEP#2) are in rack2.

• VSX 8325, 8360 logical VTEPs within a rack utilize anycast Lo 1 IP as VXLAN tunnel source.

• VLAN 10 has distributed L3 gateways with anycast IP 10.1.10.1/24 and anycast IPv6 address fe80::10 in

both racks.

•

L2 VXLAN is used between VMs on different racks within VLAN 10/VNI 10.

• Optimized L3 network connectivity is provided for VMs in rack 1 between VLANs 10 and 11, this traffic

does not need to leave the rack.

• Optimized L3 network connectivity is provided for VMs in rack 2 between VLANs 10 and 12, this traffic

does not need to leave the rack.

•

L3 VNI 10101 is only used for L3 network connectivity between different subnets/racks, e.g.

◦ VLAN 10/VNI 10 in rack1 <-> VLAN12/VNI 12 in rack2

◦ VLAN 11/VNI 11 in rack1 <-> VLAN12/VNI 12 in rack2

◦ VLAN 11/VNI 11 in rack1 <-> VLAN10/VNI 10 in rack2

Sample spine 1 configuration

hostname Spine1
user admin group administrators password ciphertext AQBap!snip
!
!
ssh server vrf mgmt
!
interface mgmt
    no shutdown
    ip static 10.136.40.245/24
    default-gateway 10.136.40.6

! downlinks towards VTEPs
interface 1/1/25
    no shutdown
    mtu 9198
    routing
    ip mtu 9198
    ip address 192.168.3.0/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/26
    no shutdown
    mtu 9198
    routing
    ip mtu 9198
    ip address 192.168.3.2/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/27
    no shutdown
    mtu 9198
    routing
    ip mtu 9198
    ip address 192.168.3.4/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/28
    no shutdown
    mtu 9198

36

AOS-CX 10.06 VXLAN EVPN Guide

routing
    ip mtu 9198
    ip address 192.168.3.6/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point

! Lo0 used for EVPN peering with VTEPs
interface loopback 0
    ip address 192.168.1.1/32
    ip ospf 1 area 0.0.0.0
!
!
router ospf 1
    router-id 192.168.1.1
    area 0.0.0.0
router bgp 65001
    bgp router-id 192.168.1.1
    neighbor leaf peer-group
    neighbor leaf remote-as 65001
    neighbor leaf description Leaf RR clients
    neighbor leaf update-source loopback 0
    neighbor 192.168.1.3 peer-group leaf
    neighbor 192.168.1.4 peer-group leaf
    neighbor 192.168.1.5 peer-group leaf
    neighbor 192.168.1.6 peer-group leaf
    address-family l2vpn evpn
        neighbor leaf route-reflector-client
        neighbor leaf send-community extended
        neighbor 192.168.1.3 activate
        neighbor 192.168.1.4 activate
        neighbor 192.168.1.5 activate
        neighbor 192.168.1.6 activate
! Lo0 used for EVPN peering with VTEPs
    exit-address-family
!
https-server vrf default
https-server vrf mgmt

Sample spine 2 configuration

hostname Spine2
user admin group administrators password ciphertext AQBap!snip
!
!
ssh server vrf mgmt
!
interface mgmt
    no shutdown
    ip static 10.136.40.246/24
    default-gateway 10.136.40.6

! downlinks towards VTEPs
interface 1/1/25
    no shutdown
    mtu 9198
    routing
    ip mtu 9198
    ip address 192.168.3.8/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/26
    no shutdown
    mtu 9198
    routing

Chapter 4 VXLAN with BGP EVPN

37

ip mtu 9198
    ip address 192.168.3.10/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/27
    no shutdown
    mtu 9198
    routing
    ip mtu 9198
    ip address 192.168.3.12/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/28
    no shutdown
    mtu 9198
    routing
    ip mtu 9198
    ip address 192.168.3.14/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point

! Lo0 used for EVPN peering with VTEPs
interface loopback 0
    ip address 192.168.1.2/32
    ip ospf 1 area 0.0.0.0
!
router ospf 1
    router-id 192.168.1.2
    area 0.0.0.0
router bgp 65001
    bgp router-id 192.168.1.2
    neighbor leaf peer-group
    neighbor leaf remote-as 65001
    neighbor leaf description Leaf RR clients
    neighbor leaf update-source loopback 0
    neighbor 192.168.1.3 peer-group leaf
    neighbor 192.168.1.4 peer-group leaf
    neighbor 192.168.1.5 peer-group leaf
    neighbor 192.168.1.6 peer-group leaf
    address-family l2vpn evpn
        neighbor leaf route-reflector-client
        neighbor leaf send-community extended
        neighbor 192.168.1.3 activate
        neighbor 192.168.1.4 activate
        neighbor 192.168.1.5 activate
        neighbor 192.168.1.6 activate
! Lo0 used for EVPN peering with VTEPs
    exit-address-family
!
https-server vrf default
https-server vrf mgmt

Sample Leaf1A Configuration

hostname Leaf1A
user admin group administrators password ciphertext AQBap!snip
vrf KA
vrf VRF1
    rd 65001:1
    route-target export 65001:1 evpn
    route-target import 65001:1 evpn
!
ssh server vrf mgmt
vlan 1
vlan 2
    vsx-sync
vlan 10
    vsx-sync

38

AOS-CX 10.06 VXLAN EVPN Guide

vlan 11
    vsx-sync
virtual-mac 02:00:00:00:01:00
! A unique virtual-mac is required on all symmetric IRB distributed L3 gateway VTEPs.
! It should be the same for a VSX logical VTEP pair, different virtual-macs should be used
! for other VSX VTEP pairs
! This is the inner D-MAC/egress VTEP router MAC

evpn
    vlan 10
        rd auto
        route-target export auto
        route-target import auto
        redistribute host-route
    vlan 11
        rd auto
        route-target export auto
        route-target import auto
        redistribute host-route
! redistribute host-route is used to advertise host routes (/32 for IPv4, /128 to IPv6) to remote VTEPs
! e.g. 10.1.10.100/32 and/or IPv6 address 1010::100/128 is connected to Leaf1A/Leaf1B
! 10.1.12.10/32 or IPv6 address 1012::10/128 is connected to Leaf2A/Leaf2B
! This is required as the same subnet is spread across multiple VTEPs
! Without host routes, a remote VTEP would not be aware of the correct destination VTEP
! to send traffic
!
interface mgmt
    no shutdown
    ip static 10.136.40.237/24
    default-gateway 10.136.40.6

! Southbound server facing ports
interface lag 1 multi-chassis
    no shutdown
    description Server
    no routing
    vlan trunk native 1
    vlan trunk allowed 10-11
    lacp mode active
interface 1/1/1
    no shutdown
    description Server
    lag 1

! Northbound uplink ports
interface 1/1/23
    no shutdown
    description Spine1
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.1/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/24
    no shutdown
    description Spine2
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.9/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point

! VSX ports
interface 1/1/41
    no shutdown
    vrf attach KA
    description VSX KeepAlive
    ip address 192.168.0.0/31
interface lag 256
    vsx-sync vlans
    no shutdown
    description ISL
    no routing
    vlan trunk native 1 tag
    vlan trunk allowed all
    lacp mode active
interface 1/1/49
    no shutdown
    mtu 9198
    description VSX ISL link
    lag 256
interface 1/1/50
    no shutdown
    mtu 9198
    description VSX ISL link

Chapter 4 VXLAN with BGP EVPN

39

lag 256

! Unique Lo0 on each VTEP
interface loopback 0
    ip address 192.168.1.3/32
    ip ospf 1 area 0.0.0.0

! Shared anycast Lo1 between a VSX logical VTEP pair
interface loopback 1
    ip address 192.168.11.3/32
    ip ospf 1 area 0.0.0.0

! Transit VLAN between VSX nodes for IGP continuity
interface vlan 2
    ip mtu 9198
    ip address 192.168.3.200/31
    ip ospf 1 area 0.0.0.0
    ip ospf cost 50
    ip ospf network point-to-point

! In 10.6, SVI IP (and/or IPv6) address must be different from the anycast Active Gateway IP(and/or IPv6)address
! this provides easier troubleshooting while sourcing traffic from the SVI IP (and/or IPv6) that is not
! common to all VTEPs
! Configuration simplification with same IP address for SVI and Active Gateway is an
! enhancement for a future release.
interface vlan 10
    vsx-sync active-gateways
    vrf attach VRF1
    ip address 10.1.10.2/24
    ipv6 address 1010::2/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway ip 10.1.10.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway ipv6 fe80::10
interface vlan 11
    vsx-sync active-gateways
    vrf attach VRF1
    ip address 10.1.11.2/24
    ipv6 address 1011::2/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway ip 10.1.11.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway ipv6 fe80::11

interface vxlan 1
    source ip 192.168.11.3
    no shutdown
    vni 10010
        vlan 10
    vni 10011
        vlan 11
    vni 100001
        routing
        vrf VRF1
! L3 VNI with VRF attached

vsx
! The same virtual-mac and VSX system-mac are recommended for a VSX logical VTEP pair
    system-mac 02:00:00:00:01:00
    inter-switch-link lag 256
    role primary
    keepalive peer 192.168.0.1 source 192.168.0.0 vrf KA
!
!
router ospf 1
    router-id 192.168.1.3
    area 0.0.0.0
router bgp 65001
    bgp router-id 192.168.1.3
    neighbor spine-RR peer-group
    neighbor spine-RR remote-as 65001
    neighbor spine-RR description Spine and RR peer-group
    neighbor spine-RR update-source loopback 0
    neighbor 192.168.1.1 peer-group spine-RR
    neighbor 192.168.1.2 peer-group spine-RR
    address-family l2vpn evpn
        neighbor spine-RR send-community extended
        neighbor 192.168.1.1 activate
        neighbor 192.168.1.2 activate
! Peer to EVPN RRs
  exit-address-family
!
    vrf VRF1
        address-family ipv4 unicast
            redistribute connected
        exit-address-family

40

AOS-CX 10.06 VXLAN EVPN Guide

address-family ipv6 unicast
            redistribute connected
        exit-address-family
! Used to advertise EVPN type 5 ip prefix routes
!
https-server vrf mgmt

The virtual-mac must be added to symmetric IRB Distributed L3 Gateways deployments. To help
understand, a packet capture of the virtual-mac that is changed in the inner destination MAC field is
shown below.

All remote VTEPs will send L3 VXLAN traffic with inner destination MAC changed to 02:00:00:00:01:00 as
Leaf1A and Leaf1B are logically 1 VTEP and should have the same inner destination MAC.

Sample Leaf1B Configuration

hostname Leaf1B
user admin group administrators password ciphertext AQBap!snip
vrf KA
vrf VRF1
    rd 65001:1
    route-target export 65001:1 evpn
    route-target import 65001:1 evpn
!
!
ssh server vrf mgmt
vlan 1
vlan 2
    vsx-sync
vlan 10
    vsx-sync
vlan 11
    vsx-sync
virtual-mac 02:00:00:00:01:00
! A unique virtual-mac is required on all symmetric IRB distributed L3 gateway VTEPs.
! It should be the same for a VSX logical VTEP pair, different virtual-macs should be used
! for other VSX VTEP pairs
! This is the inner D-MAC/egress VTEP router MAC

evpn
    vlan 10
        rd auto
        route-target export auto
        route-target import auto
        redistribute host-route
    vlan 11
        rd auto
        route-target export auto
        route-target import auto
        redistribute host-route

interface mgmt
    no shutdown
    ip static 10.136.40.238/24
    default-gateway 10.136.40.6
    nameserver 10.136.40.60

! Southbound server facing ports
interface lag 1 multi-chassis
    no shutdown

Chapter 4 VXLAN with BGP EVPN

41

description Server
    no routing
    vlan trunk native 1
    vlan trunk allowed 10-11
    lacp mode active
interface 1/1/1
    no shutdown
    lag 1

! Northbound uplink ports
interface 1/1/23
    no shutdown
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.3/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point
interface 1/1/24
    no shutdown
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.11/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point

! VSX ports
interface 1/1/41
    no shutdown
    vrf attach KA
    description VSX KeepAlive
    ip address 192.168.0.1/31
interface lag 256
    vsx-sync vlans
    no shutdown
    description ISL
    no routing
    vlan trunk native 1 tag
    vlan trunk allowed all
    lacp mode active
interface 1/1/49
    no shutdown
    mtu 9148
    description VSX ISL link
    lag 256
interface 1/1/50
    no shutdown
    mtu 9148
    description VSX ISL link
    lag 256

! Unique Lo0 on each VTEP
interface loopback 0
    ip address 192.168.1.4/32
    ip ospf 1 area 0.0.0.0

! Shared anycast Lo1 between a VSX logical VTEP pair
interface loopback 1
    ip address 192.168.11.3/32
    ip ospf 1 area 0.0.0.0

! Transit VLAN between VSX nodes for IGP continuity
interface vlan 2
    ip mtu 9198
    ip address 192.168.3.201/31
    ip ospf 1 area 0.0.0.0
    ip ospf cost 50
    ip ospf network point-to-point

! In 10.6, SVI IP (and/or IPv6) address must be different from the anycast Active Gateway IP(and/or IPv6)address
! this provides easier troubleshooting while sourcing traffic from the SVI IP (and/or IPv6) that is not
! common to all VTEPs
! Configuration simplification with same IP address for SVI and Active Gateway is an
! enhancement for a future release.
interface vlan 10
    vsx-sync active-gateways
    vrf attach VRF1
    ip address 10.1.10.3/24
    ipv6 address 1010::3/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway ip 10.1.10.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway ipv6 fe80::10
    ip helper-address 192.168.3.242 vrf default
interface vlan 11
    vsx-sync active-gateways
    vrf attach VRF1

42

AOS-CX 10.06 VXLAN EVPN Guide

ip address 10.1.11.3/24
    ipv6 address 1011::3/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway 10.1.11.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway fe80::11
interface vxlan 1
    source ip 192.168.11.3
    vxlan-counters aggregate
    no shutdown
    vni 10010
        vlan 10
    vni 10011
        vlan 11
    vni 10020
        vlan 20
    vni 100001
        routing
        vrf VRF1
! L3 VNI with VRF attached

vsx
! The same virtual-mac and VSX system-mac are recommended for a VSX logical VTEP pair
    system-mac 02:00:00:00:01:00
    inter-switch-link lag 256
    role secondary
    keepalive peer 192.168.0.0 source 192.168.0.1 vrf KA
!
!
router ospf 1
    router-id 192.168.1.4
    area 0.0.0.0
router bgp 65001
    bgp router-id 192.168.1.4
    neighbor spine-RR peer-group
    neighbor spine-RR remote-as 65001
    neighbor spine-RR description Spine and RR peer-group
    neighbor spine-RR update-source loopback 0
    neighbor 192.168.1.1 peer-group spine-RR
    neighbor 192.168.1.2 peer-group spine-RR
    address-family l2vpn evpn
        neighbor spine-RR send-community extended
        neighbor 192.168.1.1 activate
        neighbor 192.168.1.2 activate
! Peer to EVPN RRs
    exit-address-family
!
    vrf VRF1
        address-family ipv4 unicast
            redistribute connected
        exit-address-family
        address-family ipv6 unicast
            redistribute connected
        exit-address-family
! Used to advertise EVPN type 5 ip prefix routes
!
https-server vrf mgmt

Sample Leaf2A Configuration

hostname Leaf2A
user admin group administrators password ciphertext AQBap!snip
vrf KA
vrf VRF1
    rd 65001:2
    route-target export 65001:1 evpn
    route-target import 65001:1 evpn
!
!
ssh server vrf mgmt
vlan 1
vlan 2
    vsx-sync
vlan 10
    vsx-sync
vlan 12
    vsx-sync
virtual-mac 02:00:00:00:02:00
! A unique virtual-mac is required on all symmetric IRB distributed L3 gateway VTEPs.
! It should be the same for a VSX logical VTEP pair, different virtual-macs should be used
! for other VSX VTEP pairs
! This is the inner D-MAC/egress VTEP router MAC

evpn
    vlan 10

Chapter 4 VXLAN with BGP EVPN

43

rd auto
        route-target export auto
        route-target import auto
        redistribute host-route
    vlan 12
        rd auto
        route-target export auto
        route-target import auto
        redistribute host-route
! redistribute host-route is used to advertise host routes (/32 for IPv4, /128 for IPv6) to remote VTEPs
! e.g. 10.1.10.100/32 and/or IPv6 address 1010::100/128 is connected to Leaf1A/Leaf1B
! 10.1.12.10/32 and/or IPv6 address 1012::10/128 is connected to Leaf2A/Leaf2B
! This is required as the same subnet is spread across multiple VTEPs
! Without host routes, a remote VTEP would not be aware of the correct destination VTEP
! to send traffic
!

interface mgmt
    no shutdown
    ip static 10.136.40.233/24
    default-gateway 10.136.40.6

! Southbound server facing ports
interface lag 37 multi-chassis
    no shutdown
    description Server
    no routing
    vlan trunk native 1
    vlan trunk allowed 10
    lacp mode active
interface lag 39 multi-chassis
    no shutdown
    description Server
    no routing
    vlan trunk native 1
    vlan trunk allowed 12
    lacp mode active
interface 1/1/37
    no shutdown
    lag 37
interface 1/1/39
    no shutdown
    lag 39

! Northbound uplink ports
interface 1/1/23
    no shutdown
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.5/31
    ip ospf 1 area 0.0.0.0
    no ip ospf passive
    ip ospf network point-to-point
interface 1/1/24
    no shutdown
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.13/31
    ip ospf 1 area 0.0.0.0
    no ip ospf passive
    ip ospf network point-to-point

! VSX ports
interface 1/1/25
    no shutdown
    vrf attach KA
    description VSX KeepAlive
    ip address 192.168.0.2/31
interface lag 256
    vsx-sync vlans
    no shutdown
    description ISL LAG
    no routing
    vlan trunk native 1 tag
    vlan trunk allowed all
    lacp mode active
interface 1/1/55
    no shutdown
    mtu 9198
    description VSX ISL link
    lag 256
interface 1/1/56
    no shutdown
    mtu 9198
    description VSX ISL link
    lag 256

44

AOS-CX 10.06 VXLAN EVPN Guide

! Unique Lo0 on each VTEP
interface loopback 0
    ip address 192.168.1.5/32
    ip ospf 1 area 0.0.0.0

! Shared anycast Lo1 between a VSX logical VTEP pair
interface loopback 1
    ip address 192.168.11.5/32
    ip ospf 1 area 0.0.0.0

! Transit VLAN between VSX nodes for IGP continuity
interface vlan 2
    ip mtu 9198
    ip address 192.168.3.202/31
    ip ospf 1 area 0.0.0.0
    no ip ospf passive
    ip ospf cost 50
    ip ospf network point-to-point

! In 10.6, SVI IP (and/or IPv6) address must be different from the anycast Active Gateway IP(and/or IPv6)address
! this provides easier troubleshooting while sourcing traffic from the SVI IP (and/or IPv6) that is not
! common to all VTEPs
! Configuration simplification with same IP address for SVI and Active Gateway is an
! enhancement for a future release.
interface vlan 10
    vsx-sync active-gateways
    vrf attach VRF1
    ip address 10.1.10.4/24
    ipv6 address 1010::4/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway ip 10.1.10.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway ipv6 fe80::10
interface vlan 12
    vsx-sync active-gateways
    vrf attach VRF1
    ip address 10.1.12.2/24
    ipv6 address 1012::2/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway ip 10.1.12.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway ipv6 fe80::12

interface vxlan 1
    source ip 192.168.11.5
    no shutdown
    vni 10010
        vlan 10
    vni 10012
        vlan 12
    !
    vni 100001
        routing
        vrf VRF1
! L3 VNI with VRF attached

vsx
! the same virtual-mac and VSX system-mac are recommended for a VSX logical VTEP pair
    system-mac 02:00:00:00:02:00
    inter-switch-link lag 256
    role primary
    keepalive peer 192.168.0.3 source 192.168.0.2 vrf KA
!
router ospf 1
    router-id 192.168.1.5
    area 0.0.0.0
router bgp 65001
    bgp router-id 192.168.1.5
    neighbor spine-RR peer-group
    neighbor spine-RR remote-as 65001
    neighbor spine-RR description Spine and RR peer-group
    neighbor spine-RR update-source loopback 0
    neighbor 192.168.1.1 peer-group spine-RR
    neighbor 192.168.1.2 peer-group spine-RR
    address-family l2vpn evpn
        neighbor spine-RR send-community extended
        neighbor 192.168.1.1 activate
        neighbor 192.168.1.2 activate
! Peer to EVPN RRs
    exit-address-family
!
    vrf VRF1
        address-family ipv4 unicast
            exit-address-family
        address-family ipv6 unicast

Chapter 4 VXLAN with BGP EVPN

45

redistribute connected
        exit-address-family
! Used to advertise EVPN type 5 ip prefix routes
!
https-server vrf mgmt

Sample Leaf2B Configuration

hostname Leaf2B
user admin group administrators password ciphertext AQBap!snip
vrf KA
vrf VRF1
    rd 65001:2
    route-target export 65001:1 evpn
    route-target import 65001:1 evpn
!
!
ssh server vrf mgmt
vlan 1
vlan 2
    vsx-sync
vlan 10
    vsx-sync
vlan 12
    vsx-sync

virtual-mac 02:00:00:00:02:00
! A unique virtual-mac is required on all symmetric IRB distributed L3 gateway VTEPs.
! It should be the same for a VSX logical VTEP pair, different virtual-macs should be used
! for other VSX VTEP pairs.
! This is the inner D-MAC/egress VTEP router MAC.

evpn
    vlan 10
        rd auto
        route-target export auto
        route-target import auto
        redistribute host-route
    vlan 12
        rd auto
        route-target export auto
        route-target import auto
        redistribute host-route
! redistribute host-route is used to advertise host routes (/32 for IPv4, /128 for IPv6) to remote VTEPs
! e.g. 10.1.10.100/32 or an IPv6 address 1010::100/128 is connected to Leaf1A/Leaf1B
! 10.1.12.10/32 or IPv6 address 1012::100/128 is connected to Leaf2A/Leaf2B
! This is required as the same subnet is spread across multiple VTEPs
! Without host routes, a remote VTEP would not be aware of the correct destination VTEP
! to send traffic
!

interface mgmt
    no shutdown
    ip static 10.136.40.234/24
    default-gateway 10.136.40.6

! Southbound server facing ports
interface lag 37 multi-chassis
    no shutdown
    description Server
    no routing
    vlan trunk native 1
    vlan trunk allowed 10
    lacp mode active
interface lag 39 multi-chassis
    no shutdown
    description Server
    no routing
    vlan trunk native 1
    vlan trunk allowed 12
    lacp mode active
interface 1/1/37
    no shutdown
    lag 37
interface 1/1/39
    no shutdown
    lag 39

! Northbound uplink ports
interface 1/1/23
    no shutdown
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.7/31
    ip ospf 1 area 0.0.0.0

46

AOS-CX 10.06 VXLAN EVPN Guide

ip ospf network point-to-point
interface 1/1/24
    no shutdown
    mtu 9198
    ip mtu 9198
    ip address 192.168.3.15/31
    ip ospf 1 area 0.0.0.0
    ip ospf network point-to-point

! VSX ports
interface 1/1/25
    no shutdown
    vrf attach KA
    description keepalive
    ip address 192.168.0.3/31
interface lag 256
    vsx-sync vlans
    no shutdown
    description ISL LAG
    no routing
    vlan trunk native 1 tag
    vlan trunk allowed all
    lacp mode active
interface 1/1/55
    no shutdown
    mtu 9198
    description VSX ISL link
    lag 256
interface 1/1/56
    no shutdown
    mtu 9198
    description VSX ISL link
    lag 256

! Unique Lo0 on each VTEP
interface loopback 0
    ip address 192.168.1.6/32
    ip ospf 1 area 0.0.0.0

! Shared anycast Lo1 between a VSX logical VTEP pair
interface loopback 1
    ip address 192.168.11.5/32
    ip ospf 1 area 0.0.0.0

! Transit VLAN between VSX nodes for IGP continuity
interface vlan 2
    ip mtu 9198
    ip address 192.168.3.203/31
    ip ospf 1 area 0.0.0.0
    ip ospf cost 50
    ip ospf network point-to-point

! In 10.6, SVI IP (and/or IPv6) address must be different from the anycast Active Gateway IP(and/or IPv6)address
! this provides easier troubleshooting while sourcing traffic from the SVI IP (and/or IPv6) that is not
! common to all VTEPs
! Configuration simplification with same IP address for SVI and Active Gateway is an
! enhancement for a future release.
interface vlan 10
    vsx-sync active-gateways
    vrf attach VRF1
    ip address 10.1.10.5/24
    ipv6 address 1010::5/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway ip 10.1.10.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway ipv6 fe80::10
interface vlan 12
    vsx-sync active-gateways
    vrf attach VRF1
    ip address 10.1.12.3/24
    ipv6 address 1012::3/64
    active-gateway ip mac 12:00:00:00:01:00
    active-gateway ip 10.1.12.1
    active-gateway ipv6 mac 12:00:00:00:01:00
    active-gateway ipv6 fe80::12
interface vxlan 1
    source ip 192.168.11.5
    no shutdown
    vni 10010
        vlan 10
    vni 10012
        vlan 12
    !
    vni 100001
        routing
        vrf VRF1

Chapter 4 VXLAN with BGP EVPN

47

! L3 VNI with VRF attached

vsx
! the same virtual-mac and VSX system-mac are recommended for a VSX logical VTEP pair
    system-mac 02:00:00:00:02:00
    inter-switch-link lag 256
    role secondary
    keepalive peer 192.168.0.2 source 192.168.0.3 vrf KA
!
router ospf 1
    router-id 192.168.1.6
    area 0.0.0.0
router bgp 65001
    bgp router-id 192.168.1.6
    neighbor spine-RR peer-group
    neighbor spine-RR remote-as 65001
    neighbor spine-RR description Spine and RR peer-group
    neighbor spine-RR update-source loopback 0
    neighbor 192.168.1.1 peer-group spine-RR
    neighbor 192.168.1.2 peer-group spine-RR
    address-family l2vpn evpn
        neighbor spine-RR send-community extended
        neighbor 192.168.1.1 activate
        neighbor 192.168.1.2 activate
! Peer to EVPN RRs
    exit-address-family
!
    vrf VRF1
        address-family ipv4 unicast
            redistribute connected
        exit-address-family
        address-family ipv6 unicast
            redistribute connected
        exit-address-family
! Used to advertise EVPN type 5 ip prefix routes
!
https-server vrf mgmt

Sample DHCP relay with Ubuntu DHCP Server Configuration

Update and install the DHCP server:

sudo apt get update
sudo apt-get install isc-dhcp-server -y

Editing dhcpd.conf

sudo vi /etc/dhcp/dhcpd.conf
option domain-name "local.******.net";
option domain-name-servers 8.8.8.8, 8.8.8.4;
authoritative;

subnet 192.168.3.240 netmask 255.255.255.248 {}
# isc-dhcp-server requires local subnet on DHCP server to be configured in order to start

# Here are 2 example DHCP scopes
# Routers and dhcp-server-identifier would match Active Gateway IP(and/or IPv6)on the SVIs
subnet 10.1.10.0 netmask 255.255.255.0 {
  range 10.1.10.10 10.1.10.40;
  option routers 10.1.10.1;
  option dhcp-server-identifier 10.1.10.1;
}

subnet 10.1.11.0 netmask 255.255.255.0 {
  range 10.1.11.10 10.1.11.40;
  option routers 10.1.11.1;
  option dhcp-server-identifier 10.1.11.1;
}
# save and exit editor

VRFs with overlapping subnets

sudo vi /etc/dhcp/dhcpd.conf
option domain-name "local.******.net";
option domain-name-servers 8.8.8.8, 8.8.8.4;

48

AOS-CX 10.06 VXLAN EVPN Guide

authoritative;

subnet 192.168.3.240 netmask 255.255.255.248 {}
# isc-dhcp-server requires local subnet on DHCP server to be configured in order to start

# The AOS-CX DHCP relay VTEP will send VRF name as part of option 82, sub-option 151
class "VRF1"
{
    match if substring (option agent.unknown-151,1,100) = "VRF1";
}
class "VRF2"
{
    match if substring (option agent.unknown-151,1,100) = "VRF2";
}
subnet 10.1.10.0 netmask 255.255.255.0 {
  option routers 10.1.10.1;
  pool {
   allow members of “VRF1”;
   range 10.1.10.10 10.1.10.40;
  }
  pool {
   allow members of “VRF2”;
   range 10.1.10.41 10.1.10.60;
  }
}
# save and exit editor

Start and check DHCP server status

sudo systemctl start isc-dhcp-server.service
sudo systemctl status isc-dhcp-server.service

Additional configuration required on a VTEP for DHCP relay, ensure network connectivity works between Lo0
and DHCP server through VRF default

interface loopback 0
 ip address 192.168.1.3/32
!
ip source-interface dhcp_relay interface loopback0
dhcp-relay option 82 source-interface
! The above commands ensure that VTEP DHCP relay communication uses Lo0 to DHCP server
! and DHCP-relay option 82, sub-option 5, 11 and 151 are sent to the DHCP server using Lo0 IP
!
interface vlan10
 vrf attach VRF1
 ip address 10.1.10.2/24
 ip helper-address 192.168.3.242 vrf default
! Point to DHCP server in VRF default
 active-gateway ip mac 12:00:00:00:01:00
 active-gateway ip 10.1.10.1
!
interface vlan11
 vrf attach VRF2
 ip address 10.1.11.2/24
 ip helper-address 192.168.3.242 vrf default
! Point to DHCP server in VRF default
 active-gateway ip mac 12:00:00:00:01:00
 active-gateway ip 10.1.11.1

A packet capture of the interaction between the DHCP relay VTEP and DHCP server is shown below with
option 82 and sub-options 5, 11 and 151 with VRF1 in the contents of VRF name field.

Chapter 4 VXLAN with BGP EVPN

49

Sample DHCP relay with Windows DHCP Server Configuration

The Windows Server 2016 DHCP server requires VTEP loopbacks to be added as scopes that are excluded
from DHCP allocation. For example, Scope 10.1.2.0 and 10.1.1.0 are IP ranges assigned to VTEP loopbacks.

If VTEP loopback scopes are not added, DHCP clients would not be able to correctly grab DHCP IPs.

50

AOS-CX 10.06 VXLAN EVPN Guide

Windows Server 2016 DHCP server does not require additional dhcp-server-identifier option to be
added when compared to Ubuntu DHCP server.

EVPN VSX support

NOTE: Not applicable to 6300 switch series, since 6300 supports VSF virtualization technology
instead of VSX.

VSX is a virtualization technology that presents the VSX pair as a single device to the layer 2 clients and as
independent devices at layer 3. The VSX pair provides an MCLAG link towards the clients. The clients see the
VSX-pair as a single switch, providing a redundant L2 connection to the clients. VSX acts in active-active
mode which also provides load-balancing to the connected clients.

EVPN is supported with VSX. The two VSX nodes act as independent BGP routing entities to the other VTEPs
or spines for control packets. However, in the datapath, both of them act as a single logical VTEP. This is
achieved by using different IP addresses for establishing the BGP session and using a common IP as next-
hop to represent the VTEP.

EVPN VSX support: Logical VTEP

Chapter 4 VXLAN with BGP EVPN

51

Both the VSX pairs are configured with a common Logical VTEP. The configuration has to be done on a
loopback interface on both the VSX pairs. The underlay routing protocol (OSPF or even BGP) distributes this
logical VTEP IP address to all other VTEPs.

The Overlay routes are redistributed with the next-hop as the Logical VTEP IP address. The Overlay packets
reaching the Ingress VTEP get VXLAN encapsulated with the destination as the next-hop IP (common Logical
VTEP if the destination is the VSX pair) and sent to one of the Spines.

The Spine does ECMP on the VXLAN packet and sends it to either Leaf1 or Leaf1’ since both VSX switches
have connectivity to the common Logical VTEP.

Configuration recommendations for EVPN VSX support

• Split recovery is enabled by default. While using EVPN and VSX together, this mode must be kept disabled

to ensure that traffic always flows through the primary when ISL and Keepalive are both down.

• All the single homed hosts must be connected to the primary VSX Node. This is to ensure that traffic to

single homed hosts are not affected when ISL/Secondary goes down.

• The same Route Distinguisher (RD) are configured in both the VSX peers. The RD must be unique across

all the leafs except between VSX Peers.

• Even in case of EBGP peering, both the VSX peers must be in the same AS.

• The same VTEP IP must be configured on both the VSX peers.

• The BGP source IP must be configured in both the VSX peers and it must be different from the logical

VTEP. This is to ensure that logical VTEP is not used as the source IP for the BGP session establishment
with the neighbor.

52

AOS-CX 10.06 VXLAN EVPN Guide

OverlayVxLANTunnels

• Routing session between VSX peers is recommended in case of upstream connectivity failure.

• virtual-mac is required for VSX distributed L3 gateways. The virtual-mac must be the same as the

VSX system-mac for a logical VTEP. The virtual-mac must be unique on each VTEP.

NOTE: VSX active-sync is not supported for the VXLAN interface. Ensure that the configurations
are manually configured between the VSX switches.

Overlay VLANs must be allowed on the ISL for MAC/ARP sync so both devices can forward
traffic.

vsx-sync is not supported in EVPN feature-group.

For more details on VSX configurations, see the Virtual Switching Extension (VSX) Guide.

Sample configuration for iBGP VSX EVPN

The following sample configuration solution shows the relevant EVPN/VSX configurations on the primary
and secondary VSX switches.

Spine configuration

interface loopback 1
    ip address 3.3.3.3/32
    ip ospf 1 area 0.0.0.0
router bgp 1
    bgp router-id 3.3.3.3
    neighbor 2.2.2.2 remote-as 1
    neighbor 2.2.2.2 update-source 3.3.3.3
    neighbor 10.10.10.10 remote-as 1
    neighbor 10.10.10.10 update-source 3.3.3.3
    neighbor 20.20.20.20 remote-as 1
    neighbor 20.20.20.20 update-source 3.3.3.3
    address-family l2vpn evpn
        neighbor 2.2.2.2 activate
        neighbor 2.2.2.2 route-reflector-client
        neighbor 2.2.2.2 send-community extended
        neighbor 10.10.10.10 activate
        neighbor 10.10.10.10 route-reflector-client
        neighbor 10.10.10.10 send-community extended
        neighbor 20.20.20.20 activate
        neighbor 20.20.20.20 route-reflector-client
        neighbor 20.20.20.20 send-community extended
    exit-address-family

Leaf1 configuration (Primary VTEP)

vlan 1-2
evpn
    vlan 2
        rd 1.1.1.1:2
        route-target export 2:2
        route-target import 2:2
interface 1/1/17
    no shutdown
    no routing
    vlan trunk native 1 tag
    vlan trunk allowed all
interface loopback 1

Chapter 4 VXLAN with BGP EVPN

53

description “vxlan source-ip”
    ip address 1.1.1.1/32
    ip ospf 1 area 0.0.0.0
interface loopback 2
    ip address 10.10.10.10/32
    ip ospf 1 area 0.0.0.0
interface vlan2
    ip address 10.1.1.5/24
    active-gateway ip mac 00:00:00:00:00:33
    active-gateway ip 10.1.1.10
vsx
    inter-switch-link 1/1/17
    role primary
    keepalive peer 20.1.1.2 source 20.1.1.1

interface vxlan 1
    source ip 1.1.1.1
    no shutdown
    vni 100
        vlan 2
    !
router bgp 1
    bgp router-id 10.10.10.10
    neighbor 3.3.3.3 remote-as 1
    neighbor 3.3.3.3 update-source 10.10.10.10
    address-family l2vpn evpn
        neighbor 3.3.3.3 activate
        neighbor 3.3.3.3 send-community extended
    exit-address-family

Leaf1' configuration (Secondary VTEP)

vlan 1-2
evpn
    vlan 2
        rd 1.1.1.1:2
        route-target export 2:2
        route-target import 2:2
interface 1/1/23
    no shutdown
    no routing
    vlan trunk native 1 tag
    vlan trunk allowed all
interface loopback 1
description “vxlan source-ip”
    ip address 1.1.1.1/32
    ip ospf 1 area 0.0.0.0
interface loopback 2
    ip address 20.20.20.20/32
    ip ospf 1 area 0.0.0.0
interface vlan2
    ip address 10.1.1.6/24
    active-gateway ip mac 00:00:00:00:00:33
    active-gateway ip 10.1.1.10
vsx
    inter-switch-link 1/1/23
    role secondary
    keepalive peer 20.1.1.1 source 20.1.1.2

54

AOS-CX 10.06 VXLAN EVPN Guide

interface vxlan 1
    source ip 1.1.1.1
    no shutdown
    vni 100
        vlan 2
    !
router bgp 1
    bgp router-id 20.20.20.20
    neighbor 3.3.3.3 remote-as 1
    neighbor 3.3.3.3 update-source 20.20.20.20
    address-family l2vpn evpn
        neighbor 3.3.3.3 activate
        neighbor 3.3.3.3 send-community extended
    exit-address-family

Leaf2 configuration

vlan 1-2
evpn
    vlan 2
        rd 2.2.2.2:2
        route-target export 2:2
        route-target import 2:2
interface loopback 1
    ip address 2.2.2.2/32
    ip ospf 1 area 0.0.0.0
interface vlan2
    ip address 10.1.1.7/24
    active-gateway ip mac 00:00:00:00:00:33
    active-gateway ip 10.1.1.10
interface vxlan 1
    source ip 2.2.2.2
    no shutdown
    vni 100
        vlan 2
    !
router bgp 1
    neighbor 3.3.3.3 remote-as 1
    neighbor 3.3.3.3 update-source 2.2.2.2
    address-family l2vpn evpn
        neighbor 3.3.3.3 activate
        neighbor 3.3.3.3 send-community extended
    exit-address-family

Chapter 4 VXLAN with BGP EVPN

55

VSX failure scenarios

Failure scenarios

Result with split recovery off

Result with split recovery on
(default)

VTEP uplink failure

No impact to logical VTEP.
Loopback connectivity between
VTEPs will reroute through other
available links using OSPF/BGP.

No impact to logical VTEP.
Loopback connectivity between
VTEPs will reroute through other
available links using OSPF/BGP.

VTEP downlink failure

No impact to logical VTEP. Only
VSX LAG to server is impacted.

No impact to logical VTEP. Only
VSX LAG to server is impacted.

a) VSX Keepalive down. ISL up.

b) Then after sometime, ISL goes
down.

No impact to logical VTEP (but loss
of split detection).

No impact to logical VTEP (but loss
of split detection).

No impact to logical VTEP (but loss
of split detection and ISL sync).

No impact to logical VTEP (but loss
of split detection and ISL sync).

NOTE: Without ISL
ARP sync, in routing
scenarios, this split
condition may lead to
traffic loss where ARP
request originated
from a VSX device
and reply lands on
the peer VSX device.

a) ISL down, VSX Keepalive up.

Secondary VSX node tears down
VSX LAG member ports and brings
down logical VTEP to ensure that
VXLAN traffic is only sent to the
primary VSX switch.

Secondary VSX node tears down
VSX LAG member ports and brings
down logical VTEP to ensure
VXLAN traffic is only sent to the
primary VSX switch.

Table Continued

56

AOS-CX 10.06 VXLAN EVPN Guide

Failure scenarios

Result with split recovery off

Result with split recovery on
(default)

a) ISL down, VSX Keepalive up.

b) Then, after sometime, VSX
Keepalive down as well.

Secondary VSX node tears down
VSX LAG member ports and brings
down logical VTEP to ensure
VXLAN traffic is only sent to the
primary VSX switch.

Secondary VSX node tears down
VSX LAG member ports and brings
down logical VTEP to ensure that
VXLAN traffic is only sent to the
primary VSX switch.

Secondary VSX LAGs and logical
VTEP stay down.

Secondary VSX node restores VSX
LAG member ports and brings up
logical VTEP.

NOTE: Without ISL
ARP sync, in routing
scenarios, this split
condition may lead to
traffic loss where ARP
request originated
from a VSX device
and reply lands on
the peer VSX device.

a) ISL and keepalive are down

b) Keepalive restore

Secondary VSX node tears down
VSX LAG member ports and brings
down logical VTEP(If it was UP
earlier) to ensure that VXLAN
traffic is only sent to primary VSX
switch.

Secondary VSX node tears down
VSX LAG member ports and brings
down logical VTEP to ensure that
VXLAN traffic is only sent to
primary VSX switch.

For more details on VSX failure scenarios, see Troubleshooting in the Virtual Switching Extension (VSX) Guide.

eBGP support for EVPN
The BGP session for underlay and overlay can be either iBGP or eBGP. eBGP EVPN is used for Data Center
use cases. Dual-AS and Multi-AS eBGP topologies are supported.

In a Dual-AS topology, all spines share a common AS number and all leafs share another common AS
number. For example:

Chapter 4 VXLAN with BGP EVPN

57

In a Dual-AS topology, since the peer VTEPs (leafs) receive the route from another leaf with the same AS
number, the route would be rejected. To avoid this, use the following allowas-in command:

switch(config-bgp-l2vpn-evpn)# neighbor 1.1.1.1 allowas-in 1

A sample Dual-AS configuration is shown below.

Leaf 1 configuration

vlan 1-2
evpn
    vlan 2
        rd 5:5
        route-target export 1:1
        route-target import 1:1
interface 1/1/1
    no shutdown
    ip address 11.1.1.2/24
interface loopback 1
    ip address 2.2.2.2/32
interface vxlan 1
    source ip 2.2.2.2
    no shutdown
    vni 100
interface vlan 2
router bgp 65501
    neighbor 1.1.1.1 remote-as 65501
    neighbor 1.1.1.1 update-source 2.2.2.2
    neighbor 11.1.1.1 remote-as 65501
    address-family ipv4 unicast
        neighbor 11.1.1.1 activate
        neighbor 11.1.1.1 allowas-in 1
        network 2.2.2.2/32
    exit-address-family
    address-family l2vpn evpn
        neighbor 1.1.1.1 activate
        neighbor 1.1.1.1 allowas-in 1

58

AOS-CX 10.06 VXLAN EVPN Guide

neighbor 1.1.1.1 send-community extended
    exit-address-family

Leaf 2 configuration

vlan 1-2
evpn
    vlan 2
        rd 5:5
        route-target export 1:1
        route-target import 1:1
interface 1/1/24
    no shutdown
    ip address 12.1.1.2/24
interface loopback 1
    ip address 3.3.3.3/32
interface vxlan 1
    source ip 3.3.3.3
    no shutdown
    vni 100
interface vlan 2
    !
router bgp 65501
    neighbor 1.1.1.1 remote-as 65501
    neighbor 1.1.1.1 update-source 3.3.3.3
    neighbor 12.1.1.1 remote-as 65501
    address-family ipv4 unicast
        neighbor 12.1.1.1 activate
        network 3.3.3.3/32
    exit-address-family
    address-family l2vpn evpn
        neighbor 1.1.1.1 activate
        neighbor 1.1.1.1 allowas-in 1
        neighbor 1.1.1.1 send-community extended
    exit-address-family

Spine configuration

vlan 1-2

interface 1/1/2
    no shutdown
    ip address 11.1.1.1/24
interface 1/1/5
    no shutdown
    ip address 12.1.1.1/24
interface loopback 1
    ip address 1.1.1.1/32
router bgp 65500
    neighbor 2.2.2.2 remote-as 65500
    neighbor 2.2.2.2 update-source 1.1.1.1
    neighbor 3.3.3.3 remote-as 65500
    neighbor 3.3.3.3 update-source 1.1.1.1
    neighbor 11.1.1.2 remote-as 65500
    neighbor 12.1.1.2 remote-as 65500
    address-family ipv4 unicast
        neighbor 11.1.1.2 activate

Chapter 4 VXLAN with BGP EVPN

59

neighbor 12.1.1.2 activate
        network 1.1.1.1/32
    exit-address-family
    address-family l2vpn evpn
        neighbor 2.2.2.2 activate
        neighbor 2.2.2.2 next-hop-unchanged
        neighbor 2.2.2.2 send-community extended
        neighbor 3.3.3.3 activate
        neighbor 3.3.3.3 next-hop-unchanged
        neighbor 3.3.3.3 send-community extended
    exit-address-family

In a Multi-AS Topology, all spines share a common AS number and all leafs have different AS numbers.

Figure 1: Multi-AS Topology

A sample Multi-AS configuration is shown below.

Leaf 1 configuration

vlan 1-2
evpn
    vlan 2
        rd 5:5
        route-target export 1:1
        route-target import 1:1
interface 1/1/1
    no shutdown
    ip address 11.1.1.2/24
interface loopback 1
    ip address 2.2.2.2/32
interface vxlan 1

60

AOS-CX 10.06 VXLAN EVPN Guide

source ip 2.2.2.2
    no shutdown
    vni 100
interface vlan 2
router bgp 65500
    neighbor 1.1.1.1 remote-as 65500
    neighbor 1.1.1.1 update-source 2.2.2.2
    neighbor 11.1.1.1 remote-as 65500
    address-family ipv4 unicast
        neighbor 11.1.1.1 activate
        network 2.2.2.2/32
    exit-address-family
    address-family l2vpn evpn
        neighbor 1.1.1.1 activate
        neighbor 1.1.1.1 send-community extended
    exit-address-family

Leaf 2 configuration

vlan 1-2
evpn
    vlan 2
        rd 5:5
        route-target export 1:1
        route-target import 1:1
interface 1/1/24
    no shutdown
    ip address 12.1.1.2/24
interface loopback 1
    ip address 3.3.3.3/32
interface vxlan 1
    source ip 3.3.3.3
    no shutdown
    vni 100
interface vlan 2
    !
router bgp 65500
    neighbor 1.1.1.1 remote-as 65500
    neighbor 1.1.1.1 update-source 3.3.3.3
    neighbor 12.1.1.1 remote-as 65500
    address-family ipv4 unicast
        neighbor 12.1.1.1 activate
        network 3.3.3.3/32
    exit-address-family
    address-family l2vpn evpn
        neighbor 1.1.1.1 activate
        neighbor 1.1.1.1 send-community extended
    exit-address-family

Spine configuration

vlan 1-2
interface 1/1/2
    no shutdown
    ip address 11.1.1.1/24
interface 1/1/5
    no shutdown

Chapter 4 VXLAN with BGP EVPN

61

ip address 12.1.1.1/24
interface loopback 1
    ip address 1.1.1.1/32
router bgp 65501
    neighbor 2.2.2.2 remote-as 65501
    neighbor 2.2.2.2 update-source 1.1.1.1
    neighbor 3.3.3.3 remote-as 65502
    neighbor 3.3.3.3 update-source 1.1.1.1
    neighbor 11.1.1.2 remote-as 65503
    neighbor 12.1.1.2 remote-as 65504
    address-family ipv4 unicast
        neighbor 11.1.1.2 activate
        neighbor 12.1.1.2 activate
        network 1.1.1.1/32
    exit-address-family
    address-family l2vpn evpn
        neighbor 2.2.2.2 activate
        neighbor 2.2.2.2 next-hop-unchanged
        neighbor 2.2.2.2 send-community extended
        neighbor 3.3.3.3 activate
        neighbor 3.3.3.3 next-hop-unchanged
        neighbor 3.3.3.3 send-community extended
    exit-address-family

The tunnel endpoints are communicated as next-hops in the EVPN routes. By default, the next hop of a
route is preserved when advertising the route to an iBGP peer, but is updated when advertising the route to
an eBGP peer. Setting this to 'true' over-rides this behavior and preserves the next hop when routes are
advertised to eBGP peer. To retain the next-hop (or tunnel endpoint info), an extra configuration is required
as shown in the following command:

switch(config-bgp-l2vpn-evpn)# neighbor 2.2.2.2 next-hop-unchanged

NOTE: When VSX is used with eBGP, the VSX peers must be in same AS.

Route-targets must be manually configured for switches running eBGP since auto generated
RT's (route-target auto) would lead to different export/import route-targets (Applicable for both
VSX/non-VSX).

MAC mobility
MAC mobility refers to the movement of a user terminal from one VTEP to another. The source VTEP is
unaware of the MAC move event. To notify other VTEPs of the change, the destination VTEP advertises a
MAC advertisement route. The source VTEP withdraws the old route for the MAC address after receiving the
new route. The MAC advertisement route has a sequence number that increases when the MAC address
moves. The sequence number identifies the most recent move if the MAC address moves multiple times.

EVPN MAC dampening
Supported on the 6300, 6400, 8325, 8360, and 8400 Switch Series only

EVPN MAC dampening is used to detect duplicate MAC addresses in the network and provide a mechanism
to protect against endless MAC moves.

As per RFC 7432, same MAC address is learned by different VTEPs in the same VLAN because two or more
hosts were configured incorrectly with the same MAC address. The traffic from the hosts triggers continuous
MAC moves among the VTEPs attached to the hosts. Every MAC mobility event for a given MAC address will
contain a sequence number of MAC routers received in route type-2. Based on this sequence number of the

62

AOS-CX 10.06 VXLAN EVPN Guide

MAC received and the MAC that is learnt locally, a decision to further withdraw or send a route update is
taken.

A VTEP receiving a MAC or IP advertisement route for a MAC address with a sequence number higher than
the one it had previously advertised, withdraws its MAC or IP advertisement route.

A VTEP detecting a locally attached MAC address for which it had previously received a MAC or IP
advertisement route, advertises the MAC address in a MAC or IP advertisement route. This advertisement
route is tagged with a MAC Mobility extended community attribute with a sequence number one greater
than the sequence number in the MAC Mobility extended community attribute of the received MAC or IP
advertisement route.

For the switch to recognize such instances and prevent the sequence number to increment infinitely, the
VTEP starts a timer when it detects a MAC mobility event involving a locally learnt MAC address. If the VTEP
detects a MAC move before the timer expires, it concludes that a duplicate MAC situation has occurred. The
VTEP alerts the operator through the event log and stops sending and processing any BGP MAC or IP
advertisement routes for the MAC address until the right action is provided.

NOTE: In a VSX setup, MAC dampening does not work as expected. Because, the VSX primary
dampens the MAC, but the VSX secondary will continue to advertise the dampened MAC.

Following is the command syntax to configure EVPN MAC dampening:

mac-move-detection count <mac-move-count> timer <mac-move-timer>

EVPN commands

active-gateway

Syntax

active-gateway {ip | ipv6} [<IP-ADDRESS>] [mac <MAC-ADDRESS>]

no active-gateway {ip | ipv6} [<IP-ADDRESS>] [mac]

Description

Configures an EVPN Anycast gateway that can be used on multiple VTEPs. The Active Gateway supports both
IPv4 and IPv6 addresses. The Active Gateway MAC address used along with an IPv4 and IPv6 address must
match on a given interface, for the EVPN Anycast Gateway solution to work as expected.

The no form of this command removes the active gateway for active-active routing.

Command context

config-if-vlan

Parameters
ip

Specifies the configuration of an IPv4 address.

ipv6

Specifies the configuration of an IPv6 address.

<IP-ADDRESS>

Specifies the IPv4 or IPv6 address.

Chapter 4 VXLAN with BGP EVPN

63

• Syntax for IPv4: A.B.C.D

• Syntax for IPv6: A:B::C:D

<MAC-ADDRESS>

Specifies the Virtual MAC address. Syntax: xx:xx:xx:xx:xx:xx

Authority

Administrators or local user group members with execution rights for this command.

Usage

Before configuring active gateway, confirm that an IP address is on the SVI that is in the same subnet as the
active gateway IP you are trying to configure. If an active gateway IP does not have an SVI IP with the same
subnet, the CLI allows the configuration, but the active gateway IP will not be programmed in the kernel,
resulting the active gateway to be unreachable.

Active forwarding cannot be configured when ICMP redirect is enabled. Enter the no ip icmp redirect
command for disabling ICMP redirect.

It is highly recommended that you use an IPv6 link-local address as a gateway (VIP) on the active gateway
IPv6 configuration.

If VRRP or active forwarding is configured on an SVI, active gateway cannot be configured. Active gateway
with overlapping networks is not allowed. Maximum of 16 unique virtual MACs are supported in a system.

The maximum number of supported active gateways per switch is 4,000. Since a maximum of 31 secondary
IPv4 addresses can be configured on an SVI, 32 IPv4 active gateways (along with the primary IPv4 address)
can be configured per SVI with IP multinetting support. This support is also the same for IPv6 addresses.

NOTE: Do not use peer system MAC address as an active-gateway VMAC. If same MAC address
is used, the VSX synchronization will try to sync the configuration on secondary switch and
cause traffic disruptions.

Examples

Configuring active-gateway when the IP address is different from the SVI IP address on both VSX peers (valid
for IPv6 and IPv4):

Switch 1:

Switch1(config)# int vlan 10
Switch1(config-if-vlan)# vrf attach VRF1
Switch1(config-if-vlan)# ip address 10.1.10.2/24
Switch1(config-if-vlan)# active-gateway ip mac 12:00:00:00:01:00
Switch1(config-if-vlan)# active-gateway ip 10.1.10.1
Switch1(config-if-vlan)# ipv6 address fd00:10:1:10::2/64
Switch1(config-if-vlan)# active-gateway ipv6 mac 12:00:00:00:01:00
Switch1(config-if-vlan)# active-gateway ipv6 fe80::1

Switch 2:

Switch2(config)# interface vlan10
Switch2(config-if-vlan)# vrf attach VRF1
Switch2(config-if-vlan)# ip address 10.1.10.3/24
Switch2(config-if-vlan)# active-gateway ip mac 12:00:00:00:01:00
Switch2(config-if-vlan)# active-gateway ip 10.1.10.1
Switch2(config-if-vlan)# ipv6 address fd00:10:1:10::3/64
Switch2(config-if-vlan)# active-gateway ipv6 mac 12:00:00:00:01:00
Switch2(config-if-vlan)# active-gateway ipv6 fe80::1

64

AOS-CX 10.06 VXLAN EVPN Guide

Configuring active-gateway when the IP address is the same as the SVI IP address on both VSX peers (valid
for IPv4 only):

Switch 1:

Switch1(config)# int vlan 10
Switch1(config-if-vlan)# vrf attach VRF1
Switch1(config-if-vlan)# ip address 10.1.10.2/24
Switch1(config-if-vlan)# active-gateway ip mac 12:00:00:00:01:00
Switch1(config-if-vlan)# active-gateway ip 10.1.10.1

Switch 2:

Switch2(config)# int vlan 10
Switch2(config-if-vlan)# vrf attach VRF1
Switch2(config-if-vlan)# ip address 10.1.10.3/24
Switch2(config-if-vlan)# active-gateway ip mac 12:00:00:00:01:00
Switch2(config-if-vlan)# active-gateway ip 10.1.10.1

Configuring only the active gateway address:

switch(config-if-vlan)# ip address 192.168.1.250/24
switch(config-if-vlan)# active-gateway ip 192.168.1.251

Configuring only the active gateway IP MAC address:

switch2(config-if-vlan)# ip address 192.168.1.250/24
switch2(config-if-vlan)# active-gateway ip mac 00:00:00:01:00:01

Removing the active gateway for active-active routing (IPv6 and IPv4):

switch(config-if-vlan)# no active-gateway ip
switch(config-if-vlan)# no active-gateway ipv6

Removing the active gateway for active-active routing for an IP address:

switch(config-if-vlan)# no active-gateway ip 192.168.1.250

Removing the active gateway for active-active routing for virtual MAC addresses:

switch(config-if-vlan)# no active-gateway ip mac

arp-suppression

Not supported on the 8400 Switch Series.

Syntax

arp-suppression

no arp-suppression

Description

Enables ARP suppression for EVPN-VXLAN globally across all Layer 2 VNIs configured on the VTEP. If the
target address is present in the neighbor cache, the switch responds to the broadcast or unicast ARP
request. ARP suppression is disabled by default. If the target IP/MAC is not present, the switch forwards arp
request over the VXLAN data plane for neighbor resolution.

The no form of this command disables the ARP suppression.

Chapter 4 VXLAN with BGP EVPN

65

Command context

config-evpn

Command context

config-evpn-vlan

Examples

Configuring ARP suppression in EVPN:

switch(config-evpn)# arp-suppression
switch(config-evpn)# no arp-suppression

evpn

Syntax

evpn

no evpn

Description

Specifies the EVPN context which provides the configurations for VLAN-based EVPN service mode.

The no form of this command removes this configuration.

Command context

config-evpn

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the EVPN context:

switch(config)# evpn
switch(config-evpn)#

Removing the EVPN configuration context:

switch(config-evpn)# no evpn

mac-move-detection count timer

Syntax

mac-move-detection count <MAC-MOVE-COUNT> timer <MAC-MOVE-TIMER>

no mac-move-detection count <MAC-MOVE-COUNT> timer <MAC-MOVE-TIMER>

Description

Configures EVPN MAC dampening for duplicate MAC and MAC-move count and timer across VTEPs.

The no form of this command resets the value of the count and timer to the default values of 5 and 180
seconds respectively.

66

AOS-CX 10.06 VXLAN EVPN Guide

NOTE: EVPN MAC dampening is always enabled. Links to the VTEPs must be always up for EVPN
MAC dampening to be activated.

Command context

config-evpn

Parameters
count <MAC-MOVE-COUNT>

Specifies the number of MAC-moves for MAC dampening to take effect. Range: 2 to 10. Default: 5.

timer <MAC-MOVE-TIMER>

Specifies the MAC-move time limit in seconds for MAC dampening to take effect. Range: 1 to 1000
seconds. Default: 180 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring EVPN MAC dampening:

switch(config-evpn)# mac-move-detection count 6 timer 199

The above command dampens a MAC if the MAC moves six times within 199 seconds.

switch(config-evpn)# mac-move-detection count 8

The above command dampens a MAC if the MAC moves eight times within 180 seconds.

switch(config-evpn)# mac-move-detection timer 255

The above command dampens a MAC if the MAC moves five times within 255 seconds.

nd-suppression

Not supported on the 8400 Switch Series.

Syntax

nd-suppression

no nd-suppression

Description

Enables ND suppression for EVPN-VXLAN globally. If the target address is present in the NDMD cache, the
switch responds to the IPv6 multicast or unicast neighbor solicitation. ND suppression is disabled by default.
This feature is not supported on 8400 platform.

The no form of this command disables the ND suppression.

Command context

config-evpn

Authority

Administrators or local user group members with execution rights for this command.

Chapter 4 VXLAN with BGP EVPN

67

Examples

Configuring ND suppression in EVPN:

switch(config-evpn)# nd-suppression
switch(config-evpn)# no nd-suppression

rd

Syntax

rd {auto | <AS-NUMBER:ID> | <IP-ADDRESS:ID>}

no rd {auto | <AS-NUMBER:ID> | <IP-ADDRESS:ID>}

Description

Specifies a unique number prepended to the advertised routes within the VLAN. It ensures support for
overlapping IP addresses and MACs across different tenants. The default value is NULL. Route Distinguisher
(RD) has to be manually configured by a user.

The no form of this command removes the currently configured value.

Command context

config-evpn-vlan

Parameters
auto

Specifies automatic route filtering.

<AS-NUMBER:ID>

Specifies the AS number. It can be a 1-byte or 4-byte value. If the AS number is a 2-byte value, the
administrative number is a 4-byte value and if the AS number is 4-byte value, the administrative number
is a 2-byte value.

<IP-ADDRESS:ID>

Specifies the IP address. It is a 4-byte value and the id is 2 bytes.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring Route Distinguisher for EVPN VLAN:

switch(config-evpn)# vlan 10
switch(config-evpn-vlan-10)# rd 6800:1
switch(config-evpn)# vlan 20
switch(config-evpn-vlan-20)# rd auto

redistribute host-route

Syntax

redistribute host-route

no redistribute host-route

68

AOS-CX 10.06 VXLAN EVPN Guide

Description

Enables type-2 route advertisement to include the L3VNI, RT, and router MAC of the associated IP-VRF. It is
applicable only in Symmetric routing where L3VNI is configured.

The no form of this command disables the redistribution of host routes.

Command context

config-evpn-vlan

Parameters
host-route

Specifies redistribution of host routes.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring Redistribute host-route in EVPN:

switch(config-evpn)# vlan 10
switch(config-evpn-vlan-10)# redistribute host-route

redistribute local-svi

Syntax

redistribute local-svi

no redistribute local-svi

Description

Enables type-2 route advertisement for the local IP address and MAC address of the SVI interfaces
corresponding to the EVPN-enabled VLANs.

The no form of this command disables type-2 route advertisement for the local IP address and MAC address
of the SVI interfaces corresponding to the EVPN-enabled VLANs.

Command context

config-evpn

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling type-2 route advertisement:

switch(config)# evpn
switch(config-evpn)# redistribute local-svi

Disabling type-2 route advertisement:

switch(config)# evpn
switch(config-evpn)# no redistribute local-svi

Chapter 4 VXLAN with BGP EVPN

69

route-target

Syntax

route-target {import | export | both} {auto | <AS-NUMBER:ID> | <IP-ADDRESS:ID>}

no route-target {import | export | both} {auto | <AS-NUMBER:ID> | <IP-ADDRESS:ID>}

Description

Controls the import and export of VPN routes only to the systems in the network for which routes are
needed. The default value is NULL. Route Targets (RT) have to be manually configured by a user.

The no form of this command removes the currently configured value.

Command context

config-evpn-vlan

Parameters
import

Configures the route-target to import EVPN routes.

export

Configures the route-target to export EVPN routes.

both

Configures the route-target to import and export EVPN routes.

auto

Specifies automatic route filtering.

<AS-NUMBER:ID>

Specifies the AS number. It can be a 1-byte or 4-byte value. If the AS number is a 2-byte value, the
administrative number is a 4-byte value and if the AS number is 4-byte value, the administrative number
is a 2-byte value.

<IP-ADDRESS:ID>

Specifies the IP address. It is a 4-byte value and the id is 2 bytes.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring Route Targets for EVPN VLAN:

switch(config-evpn)# vlan 10
switch(config-evpn-vlan-10)# route-target import 6800:1
switch(config-evpn-vlan-10)# route-target export 6800:1
switch(config-evpn)# vlan 20
switch(config-evpn-vlan-20)# route-target both 6900:1

70

AOS-CX 10.06 VXLAN EVPN Guide

route-target {evpn}

Syntax

route-target {import | export | both} {auto | <AS-NUMBER:ID> | <IP-ADDRESS:ID>} evpn

no route-target {import | export | both} {auto | <AS-NUMBER:ID> | <IP-ADDRESS:ID>} evpn

Description

Configures the route target (RT) for EVPN VRF to control the import and export of VPN routes only to the
systems in the network for which routes are needed. The default value is NULL. Route targets have to be
manually configured by a user.

The no form of this command removes the RT in EVPN VRF.

Command context

config-vrf

Parameters
import

Imports the VRF routes that match the RT.

export

Exports the RT in the VRF routes.

both

Configures both import and export of routes for the VRF.

auto

Specifies automatic route filtering.

<AS-NUMBER:ID>

Specifies the AS number. It can be a 1-byte or 4-byte value. If the AS number is a 2-byte value, the
administrative number is a 4-byte value. If the AS number is 4-byte value, the administrative number is a
2-byte value.

<IP-ADDRESS:ID>

Specifies the IP address. It is a 4-byte value and the id is 2 byte value.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring Route Targets for EVPN VRF:

switch(config-vrf)# route-target import 6800:1 evpn
switch(config-vrf)# route-target export 6800:1 evpn
switch(config-vrf)# route-target both 6800:1 evpn

show evpn evi

Syntax

show evpn evi

Chapter 4 VXLAN with BGP EVPN

71

Description

Shows the information of EVPN instances.

Command context

Operator (>) or Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing information for EVPN instances:

switch# show evpn evi

L2VNI : 100
    Route Distinguisher        : 10.10.10.1:10
    VLAN                       : 10
    Status                     : Up
    RT Import                  : 1.1.1.1:1, 2.2.2.2:1, 3.3.3.3:1, 5:1
    RT Export                  : 4.4.4.4:61, 1000:21
    Local MACs                 : 30
    Remote MACs                : 945
    Peer VTEPs                 : 8

L2VNI : 200
    Route Distinguisher        :
    VLAN                       : 20
    Status                     : Down, No RD
    RT Import                  : 1.1.1.1:2, 2.2.2.2:2, 3.3.3.3:2, 4.4.4.4:2,
                                 5.5.5.5:2, 5:2
    RT Export                  : 4.4.4.4:62, 1000:22
    Local MACs                 :
    Remote MACs                :
    Peer VTEPs                 :

L2VNI : 300
    Route Distinguisher        : 10.10.10.1:30
    VLAN                       : 30
    Status                     : Up
    RT Import                  : 1.1.1.1:3, 2.2.2.2:3, 3.3.3.3:3, 5:3
    RT Export                  : 4.4.4.4:63, 1000:23
    Local MACs                 : 30
    Remote MACs                : 945
    Peer VTEPs                 : 12

L3VNI : 1000
    Route Distinguisher        : 10.10.10.1:1000
    VRF                        : vrf1000
    Status                     : Up
    RT Import                  : 1.1.1.1:4, 2.2.2.2:4, 3.3.3.3:4, 5:4
    RT Export                  : 4.4.4.4:64, 1000:24
    Local Type-5 Routes        : 2
    Remote Type-5 Routes       : 3
    Peer VTEPs                 : 6

show evpn evi summary

Syntax

show evpn evi summary

72

AOS-CX 10.06 VXLAN EVPN Guide

Description

Shows the summary information for EVPN instances.

Command context

Operator (>) or Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing summary information for EVPN instances:

switch# show evpn evi summary

    L2VNI    VLAN                Status
    -------------------------------------
    100      10                  Up
    200      20                  Down, RT conflict
    210      21                  Up
    220      22                  Down, No RT
    230      23                  Down, No RT
    240      24                  Up
    250      25                  Up
    260      26                  Up
    270      27                  Up
    280      28                  Up
    290      29                  Up
    310      31                  Up

    L3VNI    VRF                 Status
    -------------------------------------
    1000     vrf1000             Up
    1001     vrf1001             Down, RT conflict
    1002     vrf1002             Down, No RD
    1004     vrf1003             Down, Administratively down
    1005     vrf1003             Up

    EVPN instances     : 17
    EVPN instances Up  : 11

show evpn evi <EVI-ID>

Syntax

show evpn evi <EVI-ID>

Description

Shows the information for the particular EVPN instance.

Command context

Operator (>) or Manager (#)

Parameter
<EVI-ID>

Specifies the EVPN instance ID.

Chapter 4 VXLAN with BGP EVPN

73

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing information for the particular EVPN instance:

switch# show evpn evi 100
L2VNI : 100
    Route Distinguisher        : 10.10.10.1:10
    VLAN                       : 10
    Status                     : Up
    RT Import                  : 1.1.1.1:1, 2.2.2.2:1, 3.3.3.3:1, 5:1
    RT Export                  : 4.4.4.4:61, 1000:21
    Local MACs                 : 30
    Remote MACs                : 945
    Peer VTEPs                 : 8

show evpn evi detail

Syntax

show evpn evi detail

Description

Shows the detailed information for all EVPN instances.

Command context

Operator (>) or Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing detailed information for EVPN instances:

switch# show evpn evi detail

L2VNI : 100
    Route Distinguisher        : 10.10.10.1:10
    VLAN                       : 10
    Status                     : Up
    RT Import                  : 1.1.1.1:1, 2.2.2.2:1, 3.3.3.3:1, 5:1
    RT Export                  : 4.4.4.4:61, 1000:21
    Local MACs                 : 30
    Remote MACs                : 307
    Peer VTEPs                 : 8

    Peer VTEPs                                 Remote MACs
    ------------------------------------------------------
    10.10.10.2                                 40
    10.10.10.3                                 22
    10.10.10.4                                 15
    10.10.10.5                                 155
    10.10.10.6                                 25
    10.10.10.7                                 35
    10.10.10.8                                 50
    10.10.10.9                                 55

74

AOS-CX 10.06 VXLAN EVPN Guide

L2VNI : 200
    Route Distinguisher        :
    VLAN                       : 20
    Status                     : Down, No RD
    RT Import                  : 1.1.1.1:2, 2.2.2.2:2, 3.3.3.3:2, 4.4.4.4:2,
                                 5.5.5.5:2, 5:2
    RT Export                  : 4.4.4.4:62, 1000:22
    Local MACs                 :
    Remote MACs                :
    Peer VTEPs                 :

    Peer VTEPs                                  Remote MACs
    -------------------------------------------------------

L2VNI : 300
    Route Distinguisher         : 10.10.10.1:30
    VLAN                        : 30
    Status                      : Up
    RT Import                   : 1.1.1.1:3, 2.2.2.2:3, 3.3.3.3:3, 5:3
    RT Export                   : 4.4.4.4:63, 1000:23
    Local MACs                  : 30
    Remote MACs                 : 362
    Peer VTEPs                  : 12

    Peer VTEPs                                 Remote MACs
    ------------------------------------------------------
    10.10.10.2                                 60
    10.10.10.3                                 12
    10.10.10.4                                 13
    10.10.10.5                                 15
    10.10.10.6                                 15
    10.10.10.7                                 35
    10.10.10.8                                 53
    10.10.10.9                                 45
    10.10.10.10                                11
    10.10.10.11                                12
    10.10.10.12                                35
    10.10.10.13                                56

L3VNI : 1000
    Route Distinguisher        : 10.10.10.1:1000
    VRF                        : vrf1000
    Status                     : Up
    RT Import                  : 1.1.1.1:4, 2.2.2.2:4, 3.3.3.3:4, 5:4
    RT Export                  : 4.4.4.4:64, 1000:24
    Local Type-5 Routes        : 2
    Remote Type-5 Routes       : 30
    Peer VTEPs                 : 12

    Peer VTEPs                        Remote Type-5 Routes
    ------------------------------------------------------
    10.10.10.2                        2
    10.10.10.3                        1
    10.10.10.4                        1
    10.10.10.5                        1
    10.10.10.6                        1
    10.10.10.7                        3
    10.10.10.8                        5
    10.10.10.9                        4
    10.10.10.10                       1
    10.10.10.11                       3
    10.10.10.12                       3
    10.10.10.13                       5

Chapter 4 VXLAN with BGP EVPN

75

show evpn evi <EVI-ID> detail

Syntax

show evpn evi <EVI-ID> detail

Description

Shows the detailed information for the particular EVPN instance.

Command context

Operator (>) or Manager (#)

Parameter
<EVI-ID>

Specifies the EVPN instance ID.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing detailed information for the particular EVPN instance:

switch# show evpn evi 100 detail
L2VNI : 100
    Route Distinguisher        : 10.10.10.1:10
    VLAN                       : 10
    Status                     : Up
    RT Import                  : 1.1.1.1:1, 2.2.2.2:1, 3.3.3.3:1, 5:1
    RT Export                  : 4.4.4.4:61, 1000:21
    Local MACs                 : 30
    Remote MACs                : 397
    Peer VTEPs                 : 8

    Peer VTEPs                                 Remote MACs
    ------------------------------------------------------
    10.10.10.2                                 40
    10.10.10.3                                 22
    10.10.10.4                                 15
    10.10.10.5                                 155
    10.10.10.6                                 25
    10.10.10.7                                 35
    10.10.10.8                                 50
    10.10.10.9                                 55

show evpn mac-ip

Syntax

show evpn mac-ip

Description

Show the information about the EVPN MAC-IP for the EVPN instances.

Command context

Operator (>) or Manager (#)

76

AOS-CX 10.06 VXLAN EVPN Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing information about the EVPN MAC-IP for the EVPN instances:

switch# show evpn mac-ip
Flags:  Local(L), Remote(R)

EVI    MAC                  IP         Next-hop            Seq-Num   Flags
--------------------------------------------------------------------------
100    14:50:56:96:76:56               vxlan1(11.1.1.3)    0         R
100    14:50:56:96:76:56    3.3.4.5    vxlan1(11.1.1.3)    0         R
100    14:50:56:96:76:56    3.3.5.5    vxlan1(11.1.1.3)    0         R
100    24:50:56:96:76:56    3.3.3.2    vxlan1(11.1.1.3)    1         R
100    34:50:56:96:76:56    3.3.6.2                        2         L
100    44:50:56:96:76:56    3.3.7.3                        2         L
200    52:50:56:96:76:56    5.5.5.2                        0         L

MACs        : 5
Remote MACs : 2

show evpn mac-ip evi

Syntax

show evpn mac-ip evi <EVI-ID>

Description

Show the information about the EVPN MAC-IP for the particular EVPN instance.

Command context

Operator (>) or Manager (#)

Parameter
<EVI-ID>

Specifies the EVPN instance ID.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing information about the EVPN MAC-IP for the particular EVPN instance:

switch# show evpn mac-ip evi 100
Flags:  Local(L), Remote(R)

MAC                  IP         Next-hop            Seq-Num  Flags
------------------------------------------------------------------
14:50:56:96:76:56               vxlan1(11.1.1.2)    0        R
14:50:56:96:76:56    3.3.4.5    vxlan1(11.1.1.3)    0        R
14:50:56:96:76:56    3.3.5.4    vxlan1(11.1.1.2)    0        R
24:50:56:96:76:56    3.3.3.2    vxlan1(11.1.1.3)    1        R
34:50:56:96:76:56    3.3.6.2                        2        L
44:50:56:96:76:56    3.3.7.3                        2        L

Chapter 4 VXLAN with BGP EVPN

77

MACs        : 4
Remote MACs : 2

show evpn vtep-neighbor

Syntax

show evpn vtep-neighbor {all-vrfs | vrf <VRF-Name>}

Description

Shows the remote VTEPs MAC-IP binding. The state of the peer VTEP denotes whether VXLAN tunnel to the
VTEP is Up or Down.

Command context

Operator (>) or Manager (#)

Parameters
all-vrfs

Display information for all VRFs.

vrf <vrf-name>

Specify a VRF by VRF name (if no <VRF-NAME> is specified, the default VRF is implied.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing EVPN VTEP neighbor information for all VRFs:

switch# show evpn vtep-neighbor all-vrfs
VTEP-IP           L3VNI  MAC                VRF      State
------------------------------------------------------------------
2.2.2.2           1234   00:20:56:bd:27:bc  VRF1234  Up
2.2.2.2           6789   00:20:56:bd:27:bc  VRF6789  Up
3.3.3.3           1234   00:30:56:ef:aa:cc  VRF1234  Down
4.4.4.4           6789   00:40:56:12:34:44  VRF6789  Up
5.5.5.5           6789   00:50:56:ab:11:ee  VRF6789  Up

Showing EVPN VTEP neighbor information for the specified VRF name:

switch# show evpn vtep-neighbor vrf VRF1234
VTEP-IP           L3VNI  MAC                VRF      State
-----------------------------------------------------------------
2.2.2.2           1234   00:20:56:bd:27:bc  VRF1234  Up
3.3.3.3           1234   00:30:56:ef:aa:cc  VRF1234  Down

show running-config evpn

Syntax

show running-config evpn

Description

Shows all EVPN configurations.

78

AOS-CX 10.06 VXLAN EVPN Guide

Command context

Operator (>) or Manager (#)

Authority

Administrators or local user group members with execution rights for this command.

Examples

Showing all EVPN configurations:

switch# show running-config evpn
evpn
    vlan 10
        rd 6800:1
        route-target import 6800:1
        route-target export 6800:1
    vlan 20
        rd 6900:1
        route-target import 6900:1
        route-target export 6900:1

virtual-mac

Syntax

virtual-mac <MAC-ADDR>

no virtual-mac

Description

Configures the virtual MAC address for EVPN.

The no form of this command removes the virtual MAC address configuration.

Command context

config

Parameters
<MAC-ADDR>

Specifies the virtual MAC address.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring virtual MAC address for EVPN:

switch(config)# virtual-mac ab:12:33:33:03:22
switch(config)# no virtual-mac

NOTE: For EVPN symmetric IRB to work, virtual-mac must be configured and it must be
unique for all the VTEPs involved in EVPN except for VSX nodes. In the VSX pair switches, same
virtual-mac must be configured in both the VTEPs. In case of VSX VTEP, it is recommended to
use the same value as the VSX system-mac value in order to simplify the troubleshooting.

Chapter 4 VXLAN with BGP EVPN

79

vlan

Syntax

vlan <ID>

no vlan <ID>

Description

Specifies the VLAN ID and enters the VLAN context under EVPN.

The no form of this command removes this configuration.

Command context

config-evpn-vlan

Parameters
<ID>

Specifies the VLAN ID. Range: 2 - 4040.

Authority

Administrators or local user group members with execution rights for this command.

Examples

switch(config-evpn)# vlan 10
switch(config-evpn-vlan-10)#

80

AOS-CX 10.06 VXLAN EVPN Guide

Chapter 5
VXLAN commands

interface vxlan

Syntax

interface vxlan 1

no interface vxlan 1

Description

Creates VXLAN interface 1 and changes to the config-vxlan-if context. A maximum of one VXLAN
interface is supported. By default, the VXLAN is disabled. To enable the VXLAN, use the command no
shutdown.

The no form of this command removes VXLAN interface 1. This deletes the VXLAN tunnel, and all VNIs and
VLAN-to-VNI mappings associated with it.

Command context

config

Parameters
1

Only one VXLAN interface is supported.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating VXLAN interface 1:

switch(config)# interface vxlan 1
switch(config-vxlan-if)#

Deleting VXLAN interface 1:

switch(config)# no interface vxlan 1

routing

Syntax

vni <VNI-NUMBER>

no vni <VNI-NUMBER>

Chapter 5 VXLAN commands

81

Description

Enables a layer 3 VNI for EVPN VXLAN distributed L3 gateways with symmetric IRB. The VNI is automatically
assigned the default VRF. To assign another VRF, use the command vrf. Used with EVPN-based VXLANs.

The no form of this command disables symmetric routing on a VNI.

Command context

config-vni-<VNI-NUMBER>

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling L3 VNI 1000 for EVPN VXLAN distributed L3 gateways with symmetric IRB using VRF vrf-1:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)# routing
switch(config-vni-1000)# vrf vrf-1

Disabling L3 VNI 1000 for EVPN VXLAN distributed L3 gateways with symmetric IRB:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)# no routing

show interface vxlan1

Syntax

show interface vxlan1

Description

Shows detailed information about VXLAN interface 1.

Command context

Manager (#)

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

On the 6400 Switch Series, interface identification differs.

Showing settings for VXLAN interface 1.

switch# show interface vxlan1
Interface vxlan1 is up
Admin state is up
Description:VXLAN1
Underlay VRF: default
Destination UDP port: 4789
VTEP source IPv4 address: 1.1.1.1

82

AOS-CX 10.06 VXLAN EVPN Guide

VNI        Routing   VLAN  VRF       VTEP Peers        Origin
---------- --------  ----  --------  ----------------- --------
10         disabled  10    --        2.2.2.2           static
10         disabled  10    --        3.3.3.3           static
10         disabled  10    --        4.4.4.4           static
20         disabled  20    --        5.5.5.5           evpn
20         disabled  20    --        6.6.6.6           evpn
30         disabled  --    --        --                static
40         disabled  40    --        --                static
50         disabled  --    --        7.7.7.7           static
4000       enabled   --    default   22.1.1.2          evpn
4001       enabled   --    default   23.1.1.3          evpn

Aggregate Statistics
--------------------
 Decap:
      104222 input packets            15841744 bytes
         236 broadcast packets           26942 bytes
           0 drop packets
 Encap:
      108527 output packets           11068728 bytes
           6 BUM packets                   422 bytes
           0 drop packets

show interface vxlan vni

Syntax

show interface vxlan vni <VNI-NUMBER> vteps

Description

Shows detailed VNI information for VXLAN interface 1.

Command context

Manager (#)

Parameters
<VNI-NUMBER>

Specifies the number for a VNI. Range: 1 to 16777214.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Status can be one of the following:

• operational: Virtual network ID is fully programmed on the switch hardware.

•

configuration_error: Virtual network ID programming in the switch hardware failed due to
misconfiguration.

• no_hw_resources: Virtual network ID programming failed in the switch hardware due to insufficient

resources.

• activating: Initial state of virtual network ID when it is configured.

Chapter 5 VXLAN commands

83

When a tunnel endpoint is a directly connected via nexthop, then nexthop reachability appears empty (--).

Example

Showing VNI information:

switch# show interface vxlan vni
VNI        : 1000          VLAN  : 10
Routing    : disabled      VRF   : --
VNI-Status : operational

VNI        : 2000          VLAN  : 20
Routing    : enabled       VRF   : default
VNI-Status : activating
```
```
switch# show interface vxlan vni 1000
VNI        : 1000          VLAN  : 10
Routing    : disabled      VRF   : --
VNI-Status : operational

switch# show interface vxlan vni vteps
VNI        : 1000          VLAN  : 10
Routing    : disabled      VRF   : --
VNI-Status : operational
VTEPS
=====
    ORIGIN     SOURCE     DESTINATION  VRF      VTEP-STATUS
    ---------  ---------  -----------  -------  ------------
    static     11.0.0.1   11.0.0.2     default  operational

VNI        : 2000          VLAN  : 20
Routing    : enabled       VRF   : default
VNI-Status : operational
VTEPS
=====
    ORIGIN     SOURCE     DESTINATION  VRF      VTEP-STATUS
    ---------  ---------  -----------  -------  ------------
    evpn       11.0.0.1   14.0.0.2     default  activating

show interface vxlan vteps

Syntax

show interface vxlan vteps [detail | <IPV4-ADDR>]

Description

Shows information about the VTEPs on VXLAN interface 1.

Command context

Manager (#)

Parameters
detail

Show detailed information.

84

AOS-CX 10.06 VXLAN EVPN Guide

<IPV4-ADDR>

Specifies the IP address of a VTEP peer in IPv4 format (x.x.x.x), where x is a decimal number from 0 to
255.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Usage

Status can be one of the following:

• operational: Tunnel endpoint is fully programmed on the switch hardware.

•

configuration_error: Tunnel endpoint programming in the switch hardware failed due to
misconfiguration.

• no_hw_resources: Tunnel endpoint programming failed in the switch hardware due to insufficient

resources.

• activating: Initial state of tunnel endpoint when it is configured.

When a tunnel endpoint is a directly connected via nexthop, then nexthop reachability appears empty (--).

Example

On the 6400 Switch Series, interface identification differs.

Showing information for the VTEPs on VXLAN interface 1.

switch# show interface vxlan vteps
Source      Destination   Origin   Status           VNI    Routing   VLAN  VRF
----------- ------------- -------- ---------------- ------ --------  ----  --------
11.0.0.1    11.0.0.2      static   operational      1000   disabled  10    --
11.0.0.1    12.0.0.2      static   activating       2000   disabled  20    --
11.0.0.1    22.1.1.1      evpn     operational      4000   enabled   --    red
11.0.0.1    23.1.1.1      evpn     activating       4001   enabled   --    blue

Showing detailed information for the VTEPs on VXLAN interface 1.

switch# show interface vxlan vteps detail
Destination   : 22.22.22.1
Source        : 21.21.21.1
Origin        : static
VRF           : default
Status        : operational
Nexthops
========
    IP-ADDRESS  INTERFACE  NEXTHOP-MAC
    ----------  ---------  ------------------
      --        1/1/2      11:11:11:11:33:11

Destination   : 33.33.33.1
Source        : 21.21.21.1
Origin        : evpn
VRF           : default
Status        : operational
Nexthops
========
    IP-ADDRESS  INTERFACE  NEXTHOP-MAC
    ----------  ---------  ------------------

Chapter 5 VXLAN commands

85

2.2.3.1     1/1/1      11:11:11:11:44:11
    2.2.2.1     lag1       11:11:11:11:22:11
    2.2.1.1     vlan21     11:11:11:11:11:11
```
```
switch# show interface vxlan vteps 33.33.33.1
Destination   : 33.33.33.1
Source        : 21.21.21.1
Origin        : evpn
VRF           : default
Status        : operational
Nexthops
========
    IP-ADDRESS  INTERFACE  NEXTHOP-MAC
    ----------  ---------  ------------------
    2.2.3.1     1/1/1      11:11:11:11:44:11
    2.2.2.1     lag1       11:11:11:11:22:11
    2.2.1.1     vlan21     11:11:11:11:11:11

shutdown

Syntax

shutdown

no shutdown

Description

Disables the VXLAN interface and deletes all VXLAN tunnels, segments, and members on the interface.

The no form of this command starts the VXLAN interface and creates all VXLAN tunnels and segments. If
members are configured, they are added to the VXLAN segment.

Command context

config-vxlan-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Disabling VXLAN interface 1:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# shutdown

Enabling VXLAN interface 1:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# no shutdown

source ip

Syntax

source ip <IPV4-ADDR>

86

AOS-CX 10.06 VXLAN EVPN Guide

Description

Configures the source IP address for a VXLAN interface. All VXLAN encapsulated packets use this source IP
address in the outer IP header.

If you change an existing source IP address, all tunnels with the old source IP address are deleted, and new
tunnels are created with the new source IP address.

The no form of this command deletes the source IP address for the VXLAN interface and deletes all VXLAN
tunnels using this source IP address.

Command context

config-vxlan-if

Parameters
<IPV4-ADDR>

Specifies the IP address to assign to the VXLAN interface in IPv4 format (x.x.x.x), where x is a decimal
number from 0 to 255. This must be an address assigned to an existing switch interface, either a
loopback interface or a layer 3 interface.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Configuring the loopback IP address as the source IP address:

switch(config)# interface loopback 1
switch(config-loopback-if)# ip address 1.1.1.1/24
switch(config)# interface vxlan 1
switch(config-vxlan-if)# source ip 1.1.1.1

Configuring a layer 3 interface IP address as the source IP address:

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# routing  (6300/6400 only)
switch(config-if)# ip address 11.10.10.1/24
switch(config)# interface vxlan 1
switch(config-vxlan-if)# source ip 10.10.10.1

Deleting the source IP address for VXLAN interface 1:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# no source ip 10.10.10.1

system vlan-client-presence-detect

Supported on the 6300 and 6400 Switch Series only.

Syntax

system vlan-client-presence-detect

no system vlan-client-presence-detect

Chapter 5 VXLAN commands

87

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

vlan <VLAN-ID>

no vlan <VLAN-ID>

Description

Associates an existing VLAN with a VNI. Only one VLAN can be associated with a VNI and the VNI must have
symmetric routing disabled. To change the VLAN associated with a VNI, execute the command vlan with a
different VLAN ID.

The no form of this command removes the specified VLAN from a VNI. Traffic on the specified VLAN is no
longer bridged on the VXLAN interface.

Command context

config-vni-<VNI-NUMBER>

Parameters
<VLAN-ID>

Specifies the number of an existing VLAN. Range: 2 to 4040.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Assigning VLAN 10 to VNI 1000:

88

AOS-CX 10.06 VXLAN EVPN Guide

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)# vlan 10

Deleting VLAN 10 from VNI 1000:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
witch(config-vni-1000)# no vlan 10

vni

Syntax

vni <VNI-NUMBER>

no vni <VNI-NUMBER>

Description

Creates a VNI (Virtual Network Identifier) for the VXLAN interface and changes to the config-vni-<VNI-
NUMBER> context. The VNI identifies a VXLAN segment, which acts as a logical network. The VNI can be
associated with either a VLAN or VRF.

• When the VNI is associated with a VLAN, the VNI supports asymmetric routing.

• Enable support for asymmetric routing by executing the routing command. By default, the VNI is

associated with the default VRF. To use another VRF, execute the vrf command.

The no form of this command deletes the specified VNI from the VXLAN interface. All VXLAN tunnels, VXLAN
segments, and members associated with the VNI are deleted.

Command context

config-vxlan-if

Parameters
<VNI-NUMBER>

Specifies the number for a VNI. Range: 1 to 16777214.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating VNI 1000:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)#

Deleting VNI 1000:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# no vni 1000

Chapter 5 VXLAN commands

89

vrf

Syntax

vrf <VRF-NAME>

no vrf <VRF-NAME>

Description

Changes the VRF associated with an L3 VNI after symmetric routing is activated using the routing
command. The default VRF should not be configured as an EVPN-enabled VRF.

The no form of this command sets the VRF associated with an L3 VNI to the default VRF.

Command context

config-vni-<VNI-NUMBER>

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling L3 VNI 1000 using VRF vrf-1:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)# routing
switch(config-vni-1000)# vrf vrf-1

Setting the VRF on L3 VNI 1000 to the default VRF:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)# routing
switch(config-vni-1000)# no vrf vrf-1

vtep-peer

Syntax

vtep-peer <IPV4-ADDR>

no vtep-peer <IPV4-ADDR>

Description

Adds a VTEP peer to a VNI. The VMI must not have routing enabled. The VTEP peer IP address must be
reachable for a VXLAN tunnel to be established.

The no form of this command removes a VTEP peer from a VNI, which deletes the VXLAN tunnel to the peer.

Command context

config-vni-<VNI-NUMBER>

90

AOS-CX 10.06 VXLAN EVPN Guide

Parameters
<IPV4-ADDR>

Specifies the IP address of a VTEP peer in IPv4 format (x.x.x.x), where x is a decimal number from 0 to
255.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Adding VTEP peer 10.10.10.1 to VNI 1000:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)# vlan 10
switch(config-vni-1000)# vtep-peer 10.10.10.1

Deleting VTEP peer 10.10.10.1 from VNI 1000:

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vni 1000
switch(config-vni-1000)# no vtep-peer 10.10.10.1

vxlan-counters aggregate

Supported on the 8325 and 8360 Switch Series only. Enabled by default in the 8400 Switch Series.

Syntax

vxlan-counters aggregate

no vxlan-counters aggregate

Description

Attaches VXLAN counters to a VXLAN interface. The counters aggregate statistics for packets sent through
the interface. Display statistics with the command show interface vxlan. Statistics are only displayed
once a valid configuration is made on the interface.

Command context

config-vxlan-if

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Example

Enabling counters for VXLAN interface 1.

switch(config)# interface vxlan 1
switch(config-vxlan-if)# vxlan-counters aggregate

Disabling counters for VXLAN interface 1.

switch(config)# interface vxlan 1
switch(config-vxlan-if)# no vxlan-counters aggregate

Chapter 5 VXLAN commands

91

Chapter 6
Hardware switch controller (HSC)

Supported on the 8325, 8360, and 8400 Switch Series only.

Overview

The switch can function as a hardware layer 2 gateway, which enables the switch to extend VXLAN networks
to a remote hypervisor VTEP. Both the switch and hypervisor VTEP are controlled by a centralized controller
(such as VMware NSX-V 6.4.4).

The hardware layer 2 gateway encapsulates or decapsulates VXLAN traffic between the virtual machine and
VLANs connected to the switch.

Communication between the remote controller and the hardware layer 2 gateway is managed by the remote
controller. It communicates with a software module on the switch called the hardware switch controller
(HSC). The HSC runs an open source OVSDB server, and the remote controller connects to it as an OVSDB
client. OVSDB is the Open vSwitch Database Management Protocol detailed in RFC 7047.

Limitations

• HSC is mutually exclusive with EVPN.

• Broadcast, Unknown unicast and Multicast (BUM) traffic is not replicated by HSC. Instead, the NSX

Controller provides a list of Service Replication Nodes (RSNs) that the HSC will leverage for replication.

Connecting to a remote controller

Procedure

1. Create an HSC with the command hsc.

2. Configure the IP address of the HSC manager on the remote controller with the command manager ip.

The HSC manager must be reachable via the management port on the switch.

3. Optionally, change the TCP port on which the HSC communicates with the HSC manager with the

command manager port. By default, port 6640 is used. The remote controller OVSDB client listens on
this default port.

92

AOS-CX 10.06 VXLAN EVPN Guide

4. Enable the HSC with the command enable.

5. Obtain the default certificate on the HSC with the command show crypto pki certificate local-

cert pem. Copy the lines between ----BEGIN CERTIFICATE----- and -----END
CERTIFICATE-------. You need to provide this certificate when configuring the remote controller.

Example

switch(config)# hsc
switch(config-hsc)# enable
Trust Anchor (TA) profile configurations are not used for HSC
authentication. Instead HSC will store the CA certificate from the
HSC controller during the first TLS handshake and use it for all
future authentications with HSC servers. This CA certificate will
not be used for any other certificate-based authentication. Do you
want to continue (y/n)? y
switch(config-hsc)# exit
switch(config)# exit
switch# show crypto pki certificate local-cert pem
  Certificate name: local-cert
  Associated Applications:
     captive-portal, hsc, https-server, syslog-client
  Certificate status: installed
  Certificate type: self-signed
    -----BEGIN CERTIFICATE-----
    MIDITCDskKkeLkDKfjlsafkdjLdfkejwlisfuslekfjsdkfjelfrjsekfslkefjselfkjslde8383
    ...
    3md0k4o9vjksdoijeknkviocvhsksdoeo399((jifiIIIHFKwlIelId8rekILF:IofJe,kei(gfo9
    -----END CERTIFICATE------

Scenario 1
This example illustrates how an 8325 switch can be connected to a VMware NSX.

Chapter 6 Hardware switch controller (HSC)

93

Key components

• NSX controllers: Central control point for all logical switches in the network.

• Management network: Network on which the 8325 switch communicates with the NSX controllers.

• Hardware VTEP (8325 switch): Communication with the NSX controller occurs via the switch management
port (which operates as a DHCP client by default). Interface 1/1/1 links the switch to the layer 3 network.
Interface 1/1/3 extends the layer 2 domain over a VXLAN and links the switch to the bare metal server.
OSPF is used to enable the routed layer 3 underlay network.

• Bare metal server: Physical server providing network services.

•

Layer 3 transport network: The underlay network which provides routing functionality.

• Virtualization server: The virtualization server is managed by VMWare VSphere. It hosts software VTEPs

which perform VXLAN encapsulation for VMs deployed in virtual servers (such as an ESXi server).

Procedure

1. On the 8325 switch:

a. Enable interface 1/1/1, assign the IP address 100.1.1.1/24 to it, and configure OSPF.

94

AOS-CX 10.06 VXLAN EVPN Guide

switch# config
switch(config)# interface 1/1/1
switch(config-if)# ip address 100.1.1.10/24
switch(config-if)# ip ospf area 0
switch(config-if)# no shutdown
switch(config-if)# exit
switch(config)# router ospf 1
switch(config-ospf)# router-id 1.1.1.1
switch(config-ospf)# router-id 1.1.1.1
switch(config-ospf)# router-id 1.1.1.1

b. Create VLAN 10.

switch(config)# vlan 10
switch(config-vlan-10)# exit

c. Create a loopback interface 1 with IP address 100.1.1.1/32 and assign it to OSPF area 0 on the

default VRF.

switch(config)# router ospf 1 vrf default
switch(config-ospf-1)# exit
switch(config)# interface loopback 1
switch(config-loopback-if)# ip address 100.1.1.1/32
switch(config-loopback-if)# ip ospf 1 area 0
switch(config-loopback-if)# exit
switch(config)#

d. Enable interface 1/1/3 and assign VLAN 10 to it.

switch(config)# interface 1/1/3
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# vlan access 10
switch(config-if)# exit

e. Create VXLAN interface 1 and assign the source IP address 100.1.1.1/24 to it.

switch(config)# interface vxlan 1
switch(config-vxlan-if)# source ip 100.1.1.1
switch(config-vxlan-if)# no shutdown

f. Create VNI 5000, and assign VLAN 10 to it.

switch(config-vxlan-if)# vni 5000
switch(config-vni)# vlan 10
switch(config-vni)# exit
switch(config-vxlan-if)# exit

g. Configure the HSC manager address.

switch(config)# hsc
switch(config-hsc)# manager ip 10.10.10.1

h. Enable the HSC. You are prompted to use the default certificate installed on the switch to secure the

connection with the manager. Type y.

switch(config-hsc)# enable
Trust Anchor (TA) profile configurations are not used for HSC
authentication. Instead HSC will store the CA certificate from the
HSC controller during the first TLS handshake and use it for all
future authentications with HSC servers. This CA certificate will

Chapter 6 Hardware switch controller (HSC)

95

not be used for any other certificate-based authentication. Do you
want to continue (y/n)? y

i. Make a copy of the default certificate (local-cert) in PEM format. You need to configure this

certificate on the NSX manager.

switch# show crypto pki certificate local-cert pem
  Certificate name: local-cert
  Associated Applications:
     captive-portal, hsc, https-server, syslog-client
  Certificate status: installed
  Certificate type: self-signed
    -----BEGIN CERTIFICATE-----
    MIDITCDskKkeLkDKfjlsafkdjLdfkejwlisfuslekfjsdkfjelfrjsekfslkefjselfkjslde8383
    ...
    3md0k4o9vjksdoijeknkviocvhsksdoeo399((jifiIIIHFKwlIelId8rekILF:IofJe,kei(gfo9
    -----END CERTIFICATE------

Copy the lines between ----BEGIN CERTIFICATE----- and -----END CERTIFICATE-------.

2. On the NSX manager, add the switch certificate using the vSPhere Web Client. Select Networking &
Security and then Service Definitions. On the Hardware Devices tab, click Add (+) and paste the
certificate into the appropriate box.

switch# show crypto pki certificate local-cert pem
  Certificate name: local-cert
  Associated Applications:
     captive-portal, hsc, https-server, syslog-client
  Certificate status: installed
  Certificate type: self-signed
    -----BEGIN CERTIFICATE-----
    MIDITCDskKkeLkDKfjlsafkdjLdfkejwlisfuslekfjsdkfjelfrjsekfslkefjselfkjslde8383
    ...
    3md0k4o9vjksdoijeknkviocvhsksdoeo399((jifiIIIHFKwlIelId8rekILF:IofJe,kei(gfo9
    -----END CERTIFICATE------

For more information on configuring the NSX manager, refer to the VMware NSX documentation.

HSC commands

bfd enable

Syntax

bfd enable

no bfd enable

Description

Enables BFD support on an HSC.

The no form of this command disables BFD support on an HSC.

Command context

config-hsc

96

AOS-CX 10.06 VXLAN EVPN Guide

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling BFD:

switch(config-hsc)# bfd enable

Disabling BFD:

switch(config-hsc)# no bfd enable

bfd disable

Syntax

bfd disable

Description

Disables BFD support on an HSC.

Command context

config-hsc

Authority

Administrators or local user group members with execution rights for this command.

Examples

Disabling BFD:

switch(config-hsc)# bfd disable

disable

Syntax

disable

Description

Disables a hardware switch controller (HSC).

Command context

config-hsc

Authority

Administrators or local user group members with execution rights for this command.

Examples

Disabling an HSC:

switch(config)# hsc
switch(config-hsc)# disable

Chapter 6 Hardware switch controller (HSC)

97

enable

Syntax

enable

no enable

Description

Enables a hardware switch controller (HSC).

The no form of this command disables an HSC.

Command context

config-hsc

Authority

Administrators or local user group members with execution rights for this command.

Examples

Enabling an HSC:

switch(config)# hsc
switch(config-hsc)# enable
Trust Anchor (TA) profile configurations are not used for HSC
authentication. Instead HSC will store the CA certificate from the
HSC controller during the first TLS handshake and use it for all
future authentications with HSC servers. This CA certificate will
not be used for any other certificate-based authentication. Do you
want to continue (y/n)? y

Disabling an HSC:

switch(config)# hsc
switch(config-hsc)# no enable

hsc

Syntax

hsc

no hsc

Description

Creates a hardware switch controller (HSC) and changes to the config-hsc context for it. The switch uses
the HSC to communicate with a remote controller (such as VMware NSX) to create an extended a layer 2
VXLAN network.

The HSC runs an open-source OVSDB server. OVSDB is the Open vSwitch Database Management Protocol
detailed in RFC 7047. The remote controller connects to the server as an OVSDB client, and is responsible for
managing the interaction with the HSC. As a result, the remote controller is known as the HSC manager.

The no form of this command removes the HDC controller and deletes all configuration settings.

98

AOS-CX 10.06 VXLAN EVPN Guide

Command context

config

Authority

Administrators or local user group members with execution rights for this command.

Examples

Creating an HSC:

switch(config)# hsc
switch(config-hsc)#

Deleting an HSC:

switch(config)# no hsc
HSC configuration will be removed.
Do you want to continue (y/n)? y

manager ip

Syntax

manager ip <IPV4-ADDR>

no manager ip

Description

Configures the IP address of the HSC manager. The switch can connect with up to three managers.

The no form of this command deletes the IP address of the HSC manager.

NOTE: HSC configuration can only be modified when the HSC is disabled.

Command context

config-hsc

Parameters
<IPV4-ADDR>

Specifies the IP address of the HSC manager in IPv4 format (x.x.x.x), where x is a decimal number
from 0 to 255. The IP address must be reachable on the management VRF.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring the IP address of the HSC manager:

switch(config)# hsc
switch(config-hsc)# manager ip 1.1.1.1

Deleting the HSC manager IP address:

Chapter 6 Hardware switch controller (HSC)

99

switch(config)# hsc
switch(config-hsc)# disable
switch(config-hsc)# no manager ip

manager port

Syntax

manager port <PORT-NUM>

no manager port

Description

Configures the TCP port on which the HSC communicates with the HSC manager.

The no form of this command sets the management port to the default value (6640).

NOTE: HSC configuration can only be modified when the HSC is disabled.

Command context

config-hsc

Parameters
<PORT-NUM>

TCP port number. Range: 1024 to 65535. Default: 6640.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring port 1055 as the manager port:

switch(config)# hsc
switch(config-hsc)# manager port 1055

Setting the manager port to the default value:

switch(config)# hsc
switch(config-hsc)# disable
switch(config-hsc)# no manager port

100

AOS-CX 10.06 VXLAN EVPN Guide

Chapter 7
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

Chapter 7 Support and other resources

101

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

102

AOS-CX 10.06 VXLAN EVPN Guide