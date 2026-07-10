AOS-CX MPLS Guide (6400 (ROX44C, ROX45C), 8360 Switch Series)

Published: February 2026

AOS-CX MPLS Guide ( 6400 (ROX44C, ROX45C), 8360 Switch Series)

Published: February 2026

© Copyright 2026 – Hewlett Packard Enterprise Development LP

Notices

The information provided here is subject to change without notice. Hewlett Packard Enterprise's products
and services are covered only by the express warranty statements that come with them. This document
does not constitute an additional warranty. Hewlett Packard Enterprise is not responsible for any technical
or editorial errors or omissions in this document.

Confidential computer software. You must have a valid license from Hewlett Packard Enterprise to possess,
use, or copy the software. In accordance with FAR 12.211 and 12.212, Commercial Computer Software,
Computer Software Documentation, and Technical Data for Commercial Items are licensed to the U.S.
Government under the vendor's standard commercial license.

Links to third-party websites will take you outside of the Hewlett Packard Enterprise website. Hewlett
Packard Enterprise has no control over and is not responsible for the information outside the Hewlett
Packard Enterprise website.

Open source code

This product includes code licensed under certain open source licenses which require source compliance.
The corresponding source for these components is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, please check if the
code is available in the HPE Software Center at https://myenterpriselicense.hpe.com/cwp-ui/software
but, if not, send a written request for specific software version and product for which you want the open
source code. Along with the request, please send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company

Attn: General Counsel

WW Corporate Headquarters

1701 E Mossy Oaks Rd, Spring, TX 77389

United States of America.

Public

AOS-CX MPLS Guide ( 6400 (ROX44C, ROX45C), 8360 Sw...

A
O
S
-
C
X

M
P
L
S

G
u
i
d
e

(

6
4
0
0

(
R
O
X
4
4
C
,

R
O
X
4
5
C
)
,

8
3
6
0

S
w
.
.
.

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX MPLS Guide ( 6400 (ROX44C, ROX45C), 8360 Sw...

Table of contents

About this document..................................................................................................................................................................................6

Latest version available online.................................................................................................................................................6

Command syntax notation conventions.............................................................................................................................6

About the examples....................................................................................................................................................................... 7

Identifying switch ports and interfaces...............................................................................................................................8

Overview............................................................................................................................................................................................................ 9

MPLS L3 VPN................................................................................................................................................................................. 10

Protocol and feature details................................................................................................................................................................ 11

LDP and downstream label allocation.............................................................................................................................. 11

Label-based forwarding............................................................................................................................................................12

MPLS L3 VPN forwarding........................................................................................................................................................13

MPLS L3 VPN requirements and recommendations............................................................................................... 14

MPLS L3 VPN QoS.......................................................................................................................................................................15

MPLS L3 VPN traffic load balancing................................................................................................................................. 16

Same CE AS......................................................................................................................................................................................17

LDP packet capture.....................................................................................................................................................................18

VPNv4 packet capture...............................................................................................................................................................18

Supported features and standards..................................................................................................................................................19

Configuration task list.............................................................................................................................................................................23

Configuring MPLS and LDP globally.................................................................................................................................23

Configuring MPLS and LDP on an interface................................................................................................................. 23

Configuring IBGP VPNv4 peering.......................................................................................................................................24

Configuring VPN........................................................................................................................................................................... 25

Configuring EBGP peering between PE and CE......................................................................................................... 25

Use cases........................................................................................................................................................................................................26

Use case 1: MPLS L3 VPN with dual homed VSX CE.............................................................................................. 26

Use case 2: MPLS L3 VPN with hub and spoke VRFs..........................................................................................120

MPLS commands.................................................................................................................................................................................... 175

MPLS commands....................................................................................................................................................................... 175

bind ipv4 (lsp label imposition) ...........................................................................................................................176

bind ipv4 input (static lsp binding) ...................................................................................................................179

clear mpls statistics .................................................................................................................................................... 180

crossconnect input (static lsp binding label swap) ..................................................................................181

enable (mpls globally) ...............................................................................................................................................184

Public

Table of contents 4

enable mpls (interface) ............................................................................................................................................ 185

enable (mpls ldp) ......................................................................................................................................................... 186

enable (mpls static lsp) ............................................................................................................................................ 187

graceful-restart (mpls ldp) ..................................................................................................................................... 189

graceful-restart-timers (mpls ldp) ..................................................................................................................... 190

label-protocol ldp .........................................................................................................................................................192

label-range (static lsp) ..............................................................................................................................................193

mpls ..................................................................................................................................................................................... 195

mpls ldp discovery hello hold time (global) ................................................................................................. 196

mpls ldp discovery hello hold time (interface) ........................................................................................... 197

mpls ldp enable .............................................................................................................................................................199

graceful-restart-timers (mpls ldp) ..................................................................................................................... 200

mpls ldp session holdtime (interface) ..............................................................................................................203

ping mpls .......................................................................................................................................................................... 204

router-id (mpls ldp) .................................................................................................................................................... 206

session hold time (mpls ldp globally) .............................................................................................................. 209

show bgp vpnv4 unicast ..........................................................................................................................................210

show capacities mpls .................................................................................................................................................216

show mpls forwarding ...............................................................................................................................................218

show mpls label-range static-lsp ........................................................................................................................220

show mpls ldp bindings ............................................................................................................................................221

show mpls ldp discovery ......................................................................................................................................... 222

show mpls ldp graceful-restart ............................................................................................................................224

show mpls ldp neighbor ...........................................................................................................................................225

static-lsp ............................................................................................................................................................................226

traceroute mpls .............................................................................................................................................................227

Debugging and troubleshooting....................................................................................................................................................229

Troubleshooting steps............................................................................................................................................................ 230

Frequently asked questions.................................................................................................................................................239

Support and Other Resources.........................................................................................................................................................240

Accessing HPE Aruba Networking Support...............................................................................................................240

Accessing Updates....................................................................................................................................................................242

Warranty Information.............................................................................................................................................................. 242

Regulatory Information.......................................................................................................................................................... 242

Documentation Feedback.....................................................................................................................................................243

Public

Table of contents 5

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing HPE Aruba Networking switches on a network.

Subtopics

Latest version available online
Command syntax notation conventions
About the examples
Identifying switch ports and interfaces

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example‐text

example‐text

Any of the following:

•  <example‐text>
•  <example‐text>
•  example‐text
•  example‐text

Usage

Identifies commands and their options and operands
, code examples, filenames, pathnames, and output d
isplayed in a command window. Items that appear li
ke the example text in the previous column are to be
entered exactly as shown and are required unless en
closed in brackets ([ ]).

In code and screen examples, indicates text entered
by a user.

Identifies a placeholder—such as a parameter or a va
riable—that you must substitute with an actual valu
e in a command or in code:

•  For output formats where italic text cannot be di
splayed, variables are enclosed in angle brackets
(< >). Substitute the text—including the enclosin
g angle brackets—with an actual value.

Public

About this document 6

Convention

Usage

|

{ }

[ ]

… or

...

•  For output formats where italic text can be displ
ayed, variables might or might not be enclosed i
n angle brackets. Substitute the text including th
e enclosing angle brackets, if any, with an actual
value.

Vertical bar. A logical OR that separates multiple ite
ms from which you can choose only one.

Any spaces that are on either side of the vertical bar
are included for readability and are not a required pa
rt of the command syntax.

Braces. Indicates that at least one of the enclosed ite
ms is required.

Brackets. Indicates that the enclosed item or items a
re optional.

Ellipsis:

•

•

In code and screen examples, a vertical or horizo
ntal ellipsis indicates an omission of information.
In syntax using brackets and braces, an ellipsis i
ndicates items that can be repeated. When an ite
m followed by ellipses is enclosed in brackets, ze
ro or more items can be specified.

About the examples

Examples in this document are representative and might not match your particular switch or environment.

The slot and port numbers in this document are for illustration only and might be unavailable on your switch.

Understanding the CLI prompts

When illustrating the prompts in the command line interface (CLI), this document uses the generic term
switch, instead of the host name of the switch. For example:

switch>
The CLI prompt indicates the current command context. For example:

switch>
Indicates the operator command context.

Public

About the examples 7

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
format: member/slot/port.

On the HPE Aruba Networking 6400 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Specifies physical location of a module in the switch chassis.

◦  Management modules are on the front of the switch in slots 1/1 and 1/2.

◦  Line modules are on the front of the switch starting in slot 1/3.

•  port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

On the HPE Aruba Networking 8xxx, 93xx, and 10xxx Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

Public

Identifying switch ports and interfaces 8

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

NOTE

If using breakout cables, the port designation changes to x:y, where x is the
physical port and y is the lane when split. For example, the logical interface
1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on
member 1.

Overview

About this task

Multiprotocol Label Switching (MPLS) is a routing technique in telecommunications networks that directs
data from one node to the next based on short path labels rather than long network addresses. The labels
identify virtual links (paths) between distant nodes rather than endpoints. MPLS can encapsulate packets of
various network protocols, hence the "multiprotocol" reference on its name.

NOTE

Any features not explicitly mentioned in this document are not supported as of
the 10.09 release.

MPLS switches are termed Label Switch Routers (LSRs).

Procedure

1.  At the ingress edge LSR, label imposition or label push is used to classify and label packets.

2.  At the transit core LSR, label switching or label swapping is used to forward traffic based on labels

instead of IP.

3.  At the egress edge LSR, label disposition or label pop is used to remove labels and forward IP packets.

Results

A unidirectional label switched path (LSP) is a chain of labels that are swapped at each hop to get from one
LSR to another. Label Distribution Protocol (LDP) sessions are established between LSRs to distribute labels.

Penultimate Hop Popping (PHP) optimizes MPLS performance by reducing 1 less lookup at the egress edge
LSR. With PHP, the egress edge LSR will just need to perform IP lookup instead of removing label and
performing IP lookup. The figure below depicts the main MPLS concepts:

Public

Overview 9

Subtopics

MPLS L3 VPN

MPLS L3 VPN

MPLS L3 VPNs are deployed by service providers to provide L3 network connectivity and multi-tenant
traffic isolation using an MPLS network.

In the figure below, the MPLS L3 VPN uses BGP Autonomous System (AS) 65001, CEs in Virtual Routing
and Forwarding (VRF1) utilize AS 65101/65102, CEs in VRF2 utilize AS 65201/65202. VRF1 and VRF2
may utilize overlapping IP subnets if desired.

In this example, VRF1 consists of CE1 (LAN subnet 10.1.11.0/24) and CE3 (LAN subnet 10.1.12.0/24).
VRF2 consists of CE2 (LAN subnet 10.1.11.0/24) and CE4 (LAN subnet 10.1.12.0/24). The Core LSR now
functions as Provider (P) or Route Reflector (RR). The Edge LSR now functions as Provider Edge (PE).
Customer Edge (CE) routers are not part of the MPLS L3VPN network but are attached to it. VRFs (without
MPLS or VPNv4) could be enabled on CEs to provide locally significant L3 network isolation.

Public

MPLS L3 VPN 10

Multi Protocol BGP (MP-BGP) is used between PE routers to exchange VPNv4 addresses, extended
communities and labels. Full mesh IBGP peering is avoided within the MPLS L3 VPN network when P
routers function as VPNv4 RR. PE would peer to dual RRs for redundancy.

Protocol and feature details

The following details provide additional information regarding the configuration of MPLS features.

Subtopics

LDP and downstream label allocation
Label-based forwarding
MPLS L3 VPN forwarding
MPLS L3 VPN requirements and recommendations
MPLS L3 VPN QoS
MPLS L3 VPN traffic load balancing
Same CE AS
LDP packet capture
VPNv4 packet capture

LDP and downstream label allocation

About this task

LDP is used for downstream label allocation, Figure 3 describes this MPLS concept. Assuming 10.1.1.0/24
and 10.1.2.0/24 on the right are destination subnets.

From a right to left direction:

Procedure

1.  LSR3 informs LSR2 to use label 2001 for 10.1.1.0/24.

2.  LSR4 informs LSR2 to use label 2002 for 10.1.2.0/24.

3.  LSR2 will in turn inform LSR1 to use label 1001 for 10.1.1.0/24 and label 1002 for 10.1.2.0/24.

Results

The figure below shows LDP and downstream label allocation:

Public

Protocol and feature details 11

Label-based forwarding

About this task

Once the labels are allocated in the downstream direction, label based forwarding in the upstream direction
is used next.

Procedure

1.  Data destined for 10.1.1.0/24 arrives at LSR1, LSR1 will refer to the MPLS label table and push 1001

into the packet towards LSR2.

2.  LSR2 will receive the packet, see inbound label 1001, swap it with label 2001 and send it towards LSR3.

3.  LSR3 will receive the packet, see inbound label 2001, pop it and send the packet using its IP routing

table to the destination.

Results

The figure shows label-based forwarding, from the left to right direction:

Public

Label-based forwarding 12

MPLS L3 VPN forwarding

About this task

MPLS L3 VPN requires a 2 label stack in order to forward traffic. The outer label (based on LDP) is used to
forward traffic towards remote PE loopbacks, while the inner label (based on VPNv4) are used to forward
traffic towards CE subnets.

Procedure

1.  Data destined for 10.1.1.0/24 arrives at PE1, PE1 will refer to the LDP, MPLS BGP VPNv4 tables and

push both 43 (outer) and 2001 (inner) labels into the packet towards P2.

2.  Because of PHP from PE3 to P2, P2 will receive the packet, see inbound label 43, remove outer LDP

label and send it towards PE3.

3.  PE3 will receive the packet with VPNv4 label, see inbound label 2001, pop it and send the packet using

it's IP routing table to the destination.

Results

The figure below shows MPLS L3 VPN forwarding from the left to right direction:

Public

MPLS L3 VPN forwarding 13

MPLS L3 VPN requirements and recommendations

MPLS L3 VPN has the following requirements:

•  OSPF is required to exchange loopback IPs between PE/P

•  LDP is required to exchange outer labels

•

IBGP MP-BGP VPNv4 peering between PE/P(RR) loopbacks are used to exchange inner VPNv4 labels

•  EBGP IPv4 peering is recommended between CE and PE

High availability recommendations:

•  Dual standalone Ps

•  Dual standalone RRs

•  Dual standalone PEs for a site

•  Dual CEs (could be VSX or 2 standalone switches)

•  Redundant Equal Cost Multi Pathing (ECMP) links

Public

MPLS L3 VPN requirements and recommendations 14

MPLS L3 VPN QoS

About this task

MPLS packets interact with Quality of Service features, such as queueing and scheduling. AOS-CX supports
static Uniform mode queueing and remarking behavior as described below.

At tunnel entry, packets are prioritized and enqueued before entering the MPLS tunnel. Therefore, a device
performing tunnel entry assigns a local priority and queue number to packets identically to non-MPLS
packets: local priority is derived from both the packet's priority codepoints and the ingress port's QoS
trust mode. Refer to the Quality of Service Guide for more information about trust mode and local-priority-
to-queue mapping. When an IP packet enters an MPLS tunnel, the uppermost 3 bits of the DSCP field will be
written into the egress packet's EXP value in the newly pushed MPLS header.

At MPLS transit and tunnel exit, packets are assigned a local priority equal to the EXP value of the incoming
packet's outermost MPLS label. The COS and DSCP values of an incoming MPLS packet, and the trust mode
of the ingress port, are ignored. EXP values are NOT subject to the CoS map or DSCP map applied on the
system, but the local priority derived from the EXP value is still translated to a queue number through the
queue profile applied on the system.

At tunnel exit, the device operates in Uniform mode. For IP packets, the EXP value from the popped MPLS
label is written to the upper 3 bits of the DSCP field of the egress IP packet's header. The remaining bits of
the DSCP field will be set to 0.

For MPLS Layer 3 Virtual Private Network (L3VPN), the protocols that are currently supported for
communication between Customer Edge (CE) and Provider Edge (PE) are Open Shortest Path First (OSPF)
and Border Gateway Protocol (BGP). Routing Information Protocol(RIP) is not currently supported for
communication between Customer Edge and Provider Edge.

MPLS L3 VPN supports QoS for congestion management. In the figure below implicit null/PHP is enabled on
egress PE3 towards P2.

Public

MPLS L3 VPN QoS 15

Procedure

1.

If CE1 sends traffic to PE1 with CS6 DSCP marking PE1 will automatically copy the CS6 DSCP marking
to MPLS EXP 6 for both inner and outer labels

2.  P2 will remove the outer label and forward traffic to interface towards PE3 with EXP 6 marking

3.  PE3 will receive, pop the VPNv4 label and forward traffic with DSCP CS6

Results

MPLS L3 VPN traffic load balancing

About this task

MPLS L3 VPN supports traffic load balancing via MPLS Equal Cost Multi Pathing (ECMP) across Link
Aggregation Group (LAG) and links over multiple paths that have the same cost.

In the figure below, when ingress PE has 2 way ECMP towards egress PE loopback (2.2.2.2/32) via 2
intermediate P routers:

Procedure

1.  Traffic from ingress PE to egress PE will be load balanced across the links via the 2 P routers on a per

flow basis

2.  On ingress PE, some flows will use outbound label (2001) via top P router, while other flows will use

outbound label (2002) via bottom P router

Public

MPLS L3 VPN traffic load balancing 16

Results

Same CE AS

CEs should be deployed using unique AS numbers to help identify which AS a route originates from, however
it is possible to deploy the same CE AS as shown in the figure below, where VRF1 uses AS 65101 and VRF2
uses AS 65102. This is achieved by allowing the same inbound on the CE as a BGP router will (by default)
drop routes from the same AS it is configured.

Public

Same CE AS 17

LDP packet capture

As shown in the figure below, a packet capture of LDP traffic between 2 LSRs is provided for reference.
This example shows how a PE loopback IP of 2.2.2.2/32 is advertised with outer label of hex 0x12. Packet
captures might be required if there is a need to troubleshoot LDP between 2 LSRs.

VPNv4 packet capture

As shown in the figure below, a packet capture of MP-BGP VPNv4 traffic between 2 PEs is provided for
reference. This example shows how a VRF tenant subnet of 20.0.2.0/24 is advertised with inner label of
decimal 22. Packet captures might be required if there is a need to troubleshoot VPNv4 labels between 2
PEs. CEs should be deployed using unique AS numbers to help identify which AS a route originates from,
however it is possible to deploy duplicate CE AS as shown in Figure 10, where VRF1 uses AS 65101 and
VRF2 uses AS 65102. This is achieved by allowing the same inbound on the CE, as a BGP router will (by
default) drop routes from the same AS it is configured.

Public

LDP packet capture 18

Supported features and standards

Default behaviors

•  Default QoS mode: Uniform

•  Default TTL propagation mode: Uniform

•  Default egress label: Explicit null

•  Per-VPN/VRF label

Supported features

•  MPLS L3 VPN

◦

IPv4 unicast

•  Static LSP

•  OSPF between P/RR and PE/P

•  LDP between P/RR and PE/P

Public

Supported features and standards 19

•  MP-BGP VPNv4 RR on PE
•  MP-BGP VPNv4 RR client on PE
•  QoS uniform mode only
•  Label bindings are supported with /32 address. For example, if the network between P and PE is
X.0.0.0/24 with an interface address of P as X.0.0.1/24 and address of PE as X.0.0.2/24, the LDP
binding on PE for the X.0.0.0/24 network will be shown as X.0.0.1/32
•  VRFs (intranet and extranet VRF with route leaking)
•  Multi-VRF (VRF-Lite) CE
•  PE-CE connectivity:
◦  EBGP
◦  Static route
◦  Default route
◦  Connected route (PE acting as an L3 first hop)
•  Ping over MPLS networks
•  Traceroute over MPLS networks
Scale
8360 Switch Series Profile: Aggregation‐Leaf (Defa Profile: Core‐Spine
ult)
| Max VPNv4 VRFs/EBGP as PE‐C |     | 256 | 256 |     |
| --------------------------- | --- | --- | --- | --- |
E protocol
| Max VPNv4 neighbors/Max dyna |     | 256 | 256 |     |
| ---------------------------- | --- | --- | --- | --- |
mic LSPs
| Max VPNv4 VRF routes |     | 65,000 | 600,000 |     |
| -------------------- | --- | ------ | ------- | --- |
Max VPNv4 neighbors/Max routes 256 neighbors/32,000 routes 256 neighbors/600,000 routes
| Max LDP neighbors |        | 128  | 128                              |     |
| ----------------- | ------ | ---- | -------------------------------- | --- |
| Max static LSP    |        | 4096 | 4096                             |     |
|                   | Public |      | Supported features and standards | 20  |

6400v2T Switch Series Profile: v2‐Aggregatio Profile: v2‐Leaf‐E Profile: v2‐Core‐High
n‐High‐Bandwidth (n xtended‐High‐Bandw ‐Bandwidth(non‐defa
on‐default) idth(non‐default)
ult)
| Max VPNv4 VRFs/EBGP | 256 | 256 | 256 |     |
| ------------------- | --- | --- | --- | --- |
as PE‐CE protocol
| Max VPNv4 neighbors/M | 256 | 256 | 256 |     |
| --------------------- | --- | --- | --- | --- |
ax dynamic LSPs
| Max VPNv4 VRF routes | 65,000 | 65,000 | 600,000 |     |
| -------------------- | ------ | ------ | ------- | --- |
Max VPNv4 neighbors/M 256 neighbors/32,000 ro 256 neighbors/32,000 ro 256 neighbors/600,000
| ax routes         | utes | utes | routes |     |
| ----------------- | ---- | ---- | ------ | --- |
| Max LDP neighbors | 128  | 128  | 128    |     |
| Max static LSP    | 4096 | 4096 | 4096   |     |
Best practices
Recommended best practices for MPLS configuration are as follows:
•  Use single area OSPF within the MPLS network to advertise and learn LSR loopbacks
•  Use a single AS for the MPLS network
•  Utilize EBGP between CE and PE for dynamic routing, use unique CE AS# if possible
•  Use redundant VPNv4 RRs to avoid full mesh IBGP peers
•  Use peer groups to simplify configs on both P/RR and PE
router bgp 65001
neighbor RR-client peer-group
neighbor RR-client remote-as 65001
neighbor RR-client description all RR clients
neighbor RR-client update-source loopback 0
neighbor 1.1.1.1 peer-group RR-client
neighbor 2.2.2.2 peer-group RR-client
address-family vpnv4 unicast
        neighbor RR-client route-reflector-client
        neighbor RR-client send-community both
        neighbor 1.1.1.1 activate
        neighbor 2.2.2.2 activate
•  The l3vpn-only command should only be configured under the VRF context
|     | Public |     | Supported features and standards | 21  |
| --- | ------ | --- | -------------------------------- | --- |

•  Implicit null is not supported, explicit null has to be configured on 3rd party egress PE towards AOS-CX
P
•  If egress PE and P are AOS-CX switches, changing it to explicit null is not required as explicit null is
automatically sent
Supported RFCs and standards
The MPLS and MPLS L3 VPN implementation uses standards based protocols as described in the following
RFCs:
•  RFC 2547, BGP/MPLS VPNs
•  RFC 3031, Multiprotocol Label Switching Architecture
•  RFC 3032, MPLS Label Stack Encoding
•  RFC 3036, LDP Specification
•  RFC 3443, Time To Live (TTL) Processing in Multi-Protocol Label Switching (MPLS) Networks
•  RFC 4182, Removing a Restriction on the use of MPLS Explicit NULL
•  RFC 4364, BGP/MPLS IP Virtual Private Networks (VPNs)
•  RFC 6388, Label Distribution Protocol Extensions for Point-to-Multipoint and Multipoint-to-Multipoint
Label Switched Paths
| Max VPNv4 VRFs/EBGP | 256 | 256 | 256 |     |
| ------------------- | --- | --- | --- | --- |
as PE‐CE protocol
| Max VPNv4 neighbors/M | 256 | 256 | 256 |     |
| --------------------- | --- | --- | --- | --- |
ax dynamic LSPs
| Max VPNv4 VRF routes | 65,000 | 65,000 | 600,000 |     |
| -------------------- | ------ | ------ | ------- | --- |
Max VPNv4 neighbors/M 256 neighbors/32,000 ro 256 neighbors/32,000 ro 256 neighbors/600,000
| ax routes         | utes | utes | routes |     |
| ----------------- | ---- | ---- | ------ | --- |
| Max LDP neighbors | 128  | 128  | 128    |     |
| Max static LSP    | 4096 | 4096 | 4096   |     |

|     | Public |     | Supported features and standards | 22  |
| --- | ------ | --- | -------------------------------- | --- |

Configuration task list
The following examples provide configuration steps to follow for basic MPLS configuration. For commands
related to BGP configuration refer to the Border Gateway Protocol (BGP) chapter of the IP Routing Guide.
Subtopics
Configuring MPLS and LDP globally
Configuring MPLS and LDP on an interface
Configuring IBGP VPNv4 peering
Configuring VPN
Configuring EBGP peering between PE and CE

Configuring MPLS and LDP globally
| Step                    |     | Command            | Comments |     |     |
| ----------------------- | --- | ------------------ | -------- | --- | --- |
| 1. Enter MPLS context   |     | mpls               |          |     |     |
| 2. Enable MPLS globally |     | enable             |          |     |     |
| 3. Enter LDP context    |     | label‐protocol ldp |          |     |     |
| 4. Enable LDP globally  |     | enable             |          |     |     |
5. Specify loopback as LDP router Refer to the IP Routing Guide for c
router‐id <IP‐ADDR>
| ‐ID |     |     | ommand description. |     |     |
| --- | --- | --- | ------------------- | --- | --- |

Configuring MPLS and LDP on an interface
| Step |     | Command | Comments |     |     |
| ---- | --- | ------- | -------- | --- | --- |
1. Enter desired interface interface <IFNAME> Desired IP address and OSPF will a
lso need to be added.
| 2. Enable MPLS |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |

|     | Public |     |     | Configuration task list | 23  |
| --- | ------ | --- | --- | ----------------------- | --- |

| Step |     | Command | Comments |     |
| ---- | --- | ------- | -------- | --- |

mpls enable

| 3. Enable LDP |     | mpls ldp enable |     |     |
| ------------- | --- | --------------- | --- | --- |

Configuring IBGP VPNv4 peering
| Step                 |     | Command                | Comments |     |
| -------------------- | --- | ---------------------- | -------- | --- |
| 1. Enter BGP context |     | router bgp <AS‐NUMBER> |          |     |
2. Specify remote BGP neighbor a neighbor <IP‐ADDRESS>  The same AS number should be us
| nd remote AS |     |     | ed between P/PE. OSPF should be |     |
| ------------ | --- | --- | ------------------------------- | --- |
remote‐as <AS‐NUMBER>
enabled before BGP to advertise l
oopback IPs between LSRs.
| 3. Specify source IP/interface for I |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- |
neighbor <IP‐ADDRESS>
BGP peering
update‐source
loopback <NUMBER>
| 4. Enter VPNv4 address family |     | address‐family vpnv4  |     |     |
| ----------------------------- | --- | --------------------- | --- | --- |
unicast
| 5. Activate IBGP neighbor |     | neighbor <IP‐ADDRESS>  |     |     |
| ------------------------- | --- | ---------------------- | --- | --- |
activate
| 6. Send extended communities |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- |
neighbor <IP‐ADDRESS>
send‐community
extended
NOTE
The descriptions, syntax, and examples for the commands listed above can be
found in the IP Routing Guide.

|     | Public |     | Configuring IBGP VPNv4 peering | 24  |
| --- | ------ | --- | ------------------------------ | --- |

Configuring VPN
| Step                  |     | Command | Comments                         |     |     |
| --------------------- | --- | ------- | -------------------------------- | --- | --- |
| 1. Create desired VRF |     |         | This command can be found in the |     |     |
vrf <VRF‐NAME>
IP Routing Guide.
2. Specify a unique RD per PE, per This command can be found in the
rd number:number
| VRF |     |     | VXLAN Guide. |     |     |
| --- | --- | --- | ------------ | --- | --- |
3. Enable VPNv4 address family l3vpn‐only l3vpn‐only under VRF con
text is required for VPNv4 address
family to be active.
4. Enter IPv4 unicast address famil address‐family ipv4  This command can be found in the
| y   |     | unicast | IP Routing Guide. |     |     |
| --- | --- | ------- | ----------------- | --- | --- |
5. Specify desired route‐target fo The route target both number:n
route‐target export
| r export |     |     | umber command may also be use |     |     |
| -------- | --- | --- | ----------------------------- | --- | --- |
<AS‐NUMBER:ID> | <IP‐
d as an alternative.This command
ADDRESS:ID
can be found in the VXLAN Guide.
| 6. Specify desired route‐target fo |     | route‐target import   |     |     |     |
| ---------------------------------- | --- | --------------------- | --- | --- | --- |
| r import                           |     | <AS‐NUMBER:ID> | <IP‐ |     |     |     |
ADDRESS:ID

Configuring EBGP peering between PE and CE
| Step |     | Command | Comments |     |     |
| ---- | --- | ------- | -------- | --- | --- |
1. Enter interface facing CE interface <IFNAME> Desired IP address will also need
to be added.
| 2. Attach VRF to interface |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- |
vrf attach <VRF‐NAME>
| 3. Enter BGP context         |     | router bgp <AS‐NUMBER> |     |     |     |
| ---------------------------- | --- | ---------------------- | --- | --- | --- |
| 4. Enter desired VRF context |     |                        |     |     |     |
vrf <VRF‐NAME>
5. Specify remote CE IP neighbor <IP‐ADDRESS>  EBGP should be used between CE
|     |        | remote‐as <AS‐NUMBER> | /PE with different AS . |                 |     |
| --- | ------ | --------------------- | ----------------------- | --------------- | --- |
|     | Public |                       |                         | Configuring VPN | 25  |

Step

Command

Comments

6. Enter IPv4 unicast context for V
RF

address‐family ipv4
unicast

7. Active the EBGP neighbor

8. Redistribute connected route to
remote PEs and CEs

neighbor IP‐address
activate

redistribute connected

Optional. Only required if connecte
d routes need to be advertised.

NOTE

The descriptions, syntax, and examples for the commands listed above can be
found in the IP Routing Guide.

Use cases

The following use cases provide examples of networks using MPLS VPNs.

Subtopics

Use case 1: MPLS L3 VPN with dual homed VSX CE
Use case 2: MPLS L3 VPN with hub and spoke VRFs

Use case 1: MPLS L3 VPN with dual homed VSX CE

This use case covers:

•  An MPLS L3 VPN network with redundant PEs, Ps and VRFs across the MPLS network

•  Redundant VSX CEs at Site1 and standalone CE at Site2 with locally significant VRFs

•  BGP community is used inbound/outbound on PE1 and PE2 to prevent loops from Site1

•  Sample configurations

•  Relevant verification commands

MPLS L3 VPN with dual homed VSX CE diagram

Public

Use cases 26

CE1 configuration

CE1# show running

Current configuration:

!

!Version ArubaOS-CX GL.10.09.0001BF

!export-password: default

hostname CE1

no ip icmp redirect

profile l3-core

logging console severity crit

vrf vrf_1

vrf vrf_2

cli-session

    timeout 0

!

!

!

!
!

ssh server vrf mgmt

vlan 1,2001-2002,2011-2012,2021-2022

interface mgmt

    no shutdown

    ip dhcp

system interface-group 1 speed 10g

    !interface group 1 contains ports 1/1/1-1/1/12

system interface-group 4 speed 10g

    !interface group 4 contains ports 1/1/37-1/1/48

interface lag 99 multi-chassis

    no shutdown

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 27

description Towards L2SW

    no routing

    vlan trunk native 1

    vlan trunk allowed 2001-2002

    lacp mode active

interface lag 256

    no shutdown

    description Towards ISL

    no routing

    vlan trunk native 1 tag

    vlan trunk allowed all

    lacp mode active

interface 1/1/1

    no shutdown

    mtu 9000

    description Towards L2SW

    lag 99

interface 1/1/2

    no shutdown

    mtu 9000

    description Towards ISL

    lag 256

interface 1/1/3

    no shutdown

    mtu 9000

    description Towards ISL

    lag 256

interface 1/1/46

    no shutdown

    mtu 9000

    description Towards KA

    ip mtu 9000
    ip address 99.0.0.1/24

interface 1/1/47

    no shutdown

    mtu 9000

    description Towards PE1

    no routing

    vlan trunk native 1

    vlan trunk allowed 2011-2012

interface 1/1/48

    no shutdown

    mtu 9000

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 28

description Towards PE2

    no routing

    vlan trunk native 1

    vlan trunk allowed 2021-2022

interface vlan 2001

    vrf attach vrf_1

    description Towards LAN

    ip mtu 9000

    vsx active-forwarding

    ip address 20.0.1.2/24

interface vlan 2002

    vrf attach vrf_2

    description Towards LAN

    ip mtu 9000

    vsx active-forwarding

    ip address 20.0.1.2/24

interface vlan 2011

    vrf attach vrf_1

    description Towards PE1

    ip mtu 9000

    ip address 20.1.1.1/24

interface vlan 2012

    vrf attach vrf_2

    description Towards PE1

    ip mtu 9000

    ip address 20.1.1.1/24

interface vlan 2021

    vrf attach vrf_1

    description Towards PE2

    ip mtu 9000

    ip address 20.2.1.1/24

interface vlan 2022
    vrf attach vrf_2

    description Towards PE2

    ip mtu 9000

    ip address 20.2.1.1/24

vsx

    inter-switch-link lag 256

    role primary

    keepalive peer 99.0.0.2 source 99.0.0.1

!

!

!

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 29

!

!

router bgp 100

!

    vrf vrf_1

        neighbor 20.0.1.1 remote-as 100

        neighbor 20.0.1.1 description Towards LAN

        neighbor 20.0.1.3 remote-as 100

        neighbor 20.0.1.3 description Towards CE2

        neighbor 20.1.1.2 remote-as 6488163

        neighbor 20.1.1.2 description Towards PE1

        neighbor 20.2.1.2 remote-as 6488163

        neighbor 20.2.1.2 description Towards PE2

        address-family ipv4 unicast

            neighbor 20.0.1.1 activate

            neighbor 20.0.1.1 next-hop-self

            neighbor 20.0.1.1 send-community both

            neighbor 20.0.1.1 soft-reconfiguration inbound

            neighbor 20.0.1.3 activate

            neighbor 20.0.1.3 allowas-in 1

            neighbor 20.0.1.3 next-hop-self

            neighbor 20.0.1.3 send-community both

            neighbor 20.0.1.3 soft-reconfiguration inbound

            neighbor 20.1.1.2 activate

            neighbor 20.1.1.2 allowas-in 1

            neighbor 20.1.1.2 send-community both

            neighbor 20.1.1.2 soft-reconfiguration inbound

            neighbor 20.2.1.2 activate

            neighbor 20.2.1.2 allowas-in 1

            neighbor 20.2.1.2 send-community both

            neighbor 20.2.1.2 soft-reconfiguration inbound

        exit-address-family
!

    vrf vrf_2

        neighbor 20.0.1.1 remote-as 100

        neighbor 20.0.1.1 description Towards LAN

        neighbor 20.0.1.3 remote-as 100

        neighbor 20.0.1.3 description Towards CE2

        neighbor 20.1.1.2 remote-as 6488163

        neighbor 20.1.1.2 description Towards PE1

        neighbor 20.2.1.2 remote-as 6488163

        neighbor 20.2.1.2 description Towards PE2

        address-family ipv4 unicast

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 30

neighbor 20.0.1.1 activate

            neighbor 20.0.1.1 next-hop-self

            neighbor 20.0.1.1 send-community both

            neighbor 20.0.1.1 soft-reconfiguration inbound

            neighbor 20.0.1.3 activate

            neighbor 20.0.1.3 allowas-in 1

            neighbor 20.0.1.3 next-hop-self

            neighbor 20.0.1.3 send-community both

            neighbor 20.0.1.3 soft-reconfiguration inbound

            neighbor 20.1.1.2 activate

            neighbor 20.1.1.2 allowas-in 1

            neighbor 20.1.1.2 send-community both

            neighbor 20.1.1.2 soft-reconfiguration inbound

            neighbor 20.2.1.2 activate

            neighbor 20.2.1.2 allowas-in 1

            neighbor 20.2.1.2 send-community both

            neighbor 20.2.1.2 soft-reconfiguration inbound

        exit-address-family

!

https-server vrf mgmt

CE1 verification

CE1# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 99.0.0.1

 Peers                  : 0            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast
-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : L2VPN EVPN

-----------------------------

VRF : vrf_1

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 20.2.1.1

 Peers                  : 4            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 31

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.0.1.1        100         56      63      00h:26m:24s  Established   Up

 20.0.1.3        100         37      36      00h:29m:13s  Established   Up

 20.1.1.2        6488163     37      36      00h:28m:34s  Established   Up

 20.2.1.2        6488163     35      35      00h:28m:01s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

VRF : vrf_2

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 20.2.1.1

 Peers                  : 4            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.0.1.1        100         58      65      00h:26m:25s  Established   Up

 20.0.1.3        100         38      38      00h:29m:18s  Established   Up

 20.1.1.2        6488163     37      40      00h:28m:33s  Established   Up

 20.2.1.2        6488163     38      38      00h:27m:57s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

CE1#  show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete
VRF : default

Local Router-ID 99.0.0.1

Address-family : IPv4 Unicast

-----------------------------

    Network           Nexthop     Metric    LocPrf   Weight Path

Total number of entries 0

Address-family : IPv6 Unicast

-----------------------------

    Network           Nexthop     Metric    LocPrf   Weight Path

Total number of entries 0

Address-family : L2VPN EVPN

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 32

-----------------------------

    Network           Nexthop     Metric    LocPrf   Weight Path

------------------------------

Total number of entries 0

VRF : vrf_1

Local Router-ID 20.2.1.1

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*>i 101.0.0.0/24       20.0.1.1        0          0          0       i

* i 201.0.0.0/24       20.0.1.3        0          100        0

6488163 100 i

*>e 201.0.0.0/24       20.1.1.2        0          100        0

6488163 100 i

*=e 201.0.0.0/24       20.2.1.2        0          100        0

6488163 100 i

Total number of entries 4

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

VRF : vrf_2

Local Router-ID 20.2.1.1

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*>i 102.0.0.0/24       20.0.1.1        0          0          0       i

* i 202.0.0.0/24       20.0.1.3        0          100        0

6488163 100 i

*=e 202.0.0.0/24       20.1.1.2        0          100        0

6488163 100 i

*>e 202.0.0.0/24       20.2.1.2        0          100        0
6488163 100 i

Total number of entries 4

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

CE1# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 33

IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

99.0.0.0/24         -                1/1/46        -

C         [0/0]        -

99.0.0.1/32         -                1/1/46        -

L         [0/0]        -

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.0.1.0/24         -                vlan2001      -

C         [0/0]        -

20.0.1.2/32         -                vlan2001      -

L         [0/0]        -

20.1.1.0/24         -                vlan2011      -

C         [0/0]        -

20.1.1.1/32         -                vlan2011      -

L         [0/0]        -

20.2.1.0/24         -                vlan2021      -

C         [0/0]        -

20.2.1.1/32         -                vlan2021      -

L         [0/0]        -
101.0.0.0/24        20.0.1.1         vlan2001      -

B/I       [200/0]      01h:11m:54s

201.0.0.0/24        20.1.1.2         vlan2011      -

B/E       [20/0]       01h:10m:33s

                    20.2.1.2         vlan2021

-                           [20/0]       01h:10m:33s

VRF: vrf_2

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 34

----------------------------------------------------------------------------

------------------

20.0.1.0/24         -                vlan2002      -

C         [0/0]        -

20.0.1.2/32         -                vlan2002      -

L         [0/0]        -

20.1.1.0/24         -                vlan2012      -

C         [0/0]        -

20.1.1.1/32         -                vlan2012      -

L         [0/0]        -

20.2.1.0/24         -                vlan2022      -

C         [0/0]        -

20.2.1.1/32         -                vlan2022      -

L         [0/0]        -

102.0.0.0/24        20.0.1.1         vlan2002      -

B/I       [200/0]      00h:54m:05s

202.0.0.0/24        20.2.1.2         vlan2022      -

B/E       [20/0]       00h:54m:05s

                    20.1.1.2         vlan2012

-                           [20/0]       00h:54m:05s

Total Route Count : 18

CE2 configuration

CE2# show running-config

Current configuration:

!

!Version ArubaOS-CX GL.10.09.0001BF

!export-password: default

hostname CE2

no ip icmp redirect

profile l3-core
logging console severity crit

vrf vrf_1

vrf vrf_2

cli-session

    timeout 0

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2001-2002,2031-2032,2041-2042

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 35

interface mgmt

    no shutdown

    ip dhcp

system interface-group 1 speed 10g

    !interface group 1 contains ports 1/1/1-1/1/12

system interface-group 4 speed 10g

    !interface group 4 contains ports 1/1/37-1/1/48

interface lag 99 multi-chassis

    no shutdown

    description Towards L2SW

    no routing

    vlan trunk native 1

    vlan trunk allowed 2001-2002

    lacp mode active

interface lag 256

    no shutdown

    description Towards ISL

    no routing

    vlan trunk native 1 tag

    vlan trunk allowed all

    lacp mode active

interface 1/1/1

    no shutdown

    mtu 9000

    description Towards L2SW

    lag 99

interface 1/1/2

    no shutdown

    mtu 9000

    description Towards ISL

    lag 256

interface 1/1/3
    no shutdown

    mtu 9000

    description Towards ISL

    lag 256

interface 1/1/46

    no shutdown

    mtu 9000

    description Towards KA

    ip mtu 9000

    ip address 99.0.0.2/24

interface 1/1/47

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 36

no shutdown

    mtu 9000

    description Towards PE1

    no routing

    vlan trunk native 1

    vlan trunk allowed 2031-2032

interface 1/1/48

    no shutdown

    mtu 9000

    description Towards PE2

    no routing

    vlan trunk native 1

    vlan trunk allowed 2041-2042

interface vlan 2001

    vrf attach vrf_1

    description Towards LAN

    ip mtu 9000

    vsx active-forwarding

    ip address 20.0.1.3/24

interface vlan 2002

    vrf attach vrf_2

    description Towards LAN

    ip mtu 9000

    vsx active-forwarding

    ip address 20.0.1.3/24

interface vlan 2031

    vrf attach vrf_1

    description Towards PE1

    ip mtu 9000

    ip address 20.3.1.1/24

interface vlan 2032

    vrf attach vrf_2
    description Towards PE1

    ip mtu 9000

    ip address 20.3.1.1/24

interface vlan 2041

    vrf attach vrf_1

    description Towards PE2

    ip mtu 9000

    ip address 20.4.1.1/24

interface vlan 2042

    vrf attach vrf_2

    description Towards PE2

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 37

ip mtu 9000

    ip address 20.4.1.1/24

vsx

    inter-switch-link lag 256

    role secondary

    keepalive peer 99.0.0.1 source 99.0.0.2

!

!

!

!

!

router bgp 100

!

    vrf vrf_1

        neighbor 20.0.1.1 remote-as 100

        neighbor 20.0.1.1 description Towards LAN

        neighbor 20.0.1.2 remote-as 100

        neighbor 20.0.1.2 description Towards CE1

        neighbor 20.3.1.2 remote-as 6488163

        neighbor 20.3.1.2 description Towards PE1

        neighbor 20.4.1.2 remote-as 6488163

        neighbor 20.4.1.2 description Towards PE2

        address-family ipv4 unicast

            neighbor 20.0.1.1 activate

            neighbor 20.0.1.1 next-hop-self

            neighbor 20.0.1.1 send-community both

            neighbor 20.0.1.1 soft-reconfiguration inbound

            neighbor 20.0.1.2 activate

            neighbor 20.0.1.2 allowas-in 1

            neighbor 20.0.1.2 next-hop-self

            neighbor 20.0.1.2 send-community both

            neighbor 20.0.1.2 soft-reconfiguration inbound
            neighbor 20.3.1.2 activate

            neighbor 20.3.1.2 allowas-in 1

            neighbor 20.3.1.2 send-community both

            neighbor 20.3.1.2 soft-reconfiguration inbound

            neighbor 20.4.1.2 activate

            neighbor 20.4.1.2 allowas-in 1

            neighbor 20.4.1.2 send-community both

            neighbor 20.4.1.2 soft-reconfiguration inbound

        exit-address-family

!

    vrf vrf_2

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 38

neighbor 20.0.1.1 remote-as 100

        neighbor 20.0.1.1 description Towards LAN

        neighbor 20.0.1.2 remote-as 100

        neighbor 20.0.1.2 description Towards CE1

        neighbor 20.3.1.2 remote-as 6488163

        neighbor 20.3.1.2 description Towards PE1

        neighbor 20.4.1.2 remote-as 6488163

        neighbor 20.4.1.2 description Towards PE2

        address-family ipv4 unicast

            neighbor 20.0.1.1 activate

            neighbor 20.0.1.1 next-hop-self

            neighbor 20.0.1.1 send-community both

            neighbor 20.0.1.1 soft-reconfiguration inbound

            neighbor 20.0.1.2 activate

            neighbor 20.0.1.2 allowas-in 1

            neighbor 20.0.1.2 next-hop-self

            neighbor 20.0.1.2 send-community both

            neighbor 20.0.1.2 soft-reconfiguration inbound

            neighbor 20.3.1.2 activate

            neighbor 20.3.1.2 allowas-in 1

            neighbor 20.3.1.2 send-community both

            neighbor 20.3.1.2 soft-reconfiguration inbound

            neighbor 20.4.1.2 activate

            neighbor 20.4.1.2 allowas-in 1

            neighbor 20.4.1.2 send-community both

            neighbor 20.4.1.2 soft-reconfiguration inbound

        exit-address-family

!

https-server vrf mgmt

CE2 verification

CE2#  show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 99.0.0.2

 Peers                  : 0            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 39

Address-family : L2VPN EVPN

-----------------------------

VRF : vrf_1

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 20.4.1.1

 Peers                  : 4            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.0.1.1        100         56      65      00h:26m:24s  Established   Up

 20.0.1.2        100         36      37      00h:29m:13s  Established   Up

 20.3.1.2        6488163     36      36      00h:28m:34s  Established   Up

 20.4.1.2        6488163     35      35      00h:27m:58s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

VRF : vrf_2

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 20.4.1.1

 Peers                  : 4            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.0.1.1        100         58      65      00h:26m:25s  Established   Up

 20.0.1.2        100         38      38      00h:29m:18s  Established   Up
 20.3.1.2        6488163     38      40      00h:28m:43s  Established   Up

 20.4.1.2        6488163     37      38      00h:27m:56s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

CE2#  show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 99.0.0.2

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 40

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : L2VPN EVPN

-----------------------------

     Network                                               Nexthop

Metric     LocPrf    Weight   Path

----------------------------------------------------------------------------

--------------------------------

Total number of entries 0

VRF : vrf_1

Local Router-ID 20.4.1.1

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*>i 101.0.0.0/24       20.0.1.1        0          0          0       i

* i 201.0.0.0/24       20.0.1.2        0          100        0

6488163 100 i

*>e 201.0.0.0/24       20.3.1.2        0          100        0

6488163 100 i

*=e 201.0.0.0/24       20.4.1.2        0          100        0

6488163 100 i

Total number of entries 4

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0
VRF : vrf_2

Local Router-ID 20.4.1.1

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*>i 102.0.0.0/24       20.0.1.1        0          0          0       i

* i 202.0.0.0/24       20.0.1.2        0          100        0

6488163 100 i

*=e 202.0.0.0/24       20.3.1.2        0          100        0

6488163 100 i

*>e 202.0.0.0/24       20.4.1.2        0          100        0

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 41

6488163 100 i

Total number of entries 4

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

CE2# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop     Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

-------------

99.0.0.0/24         -                1/1/46        -

C         [0/0]        -

99.0.0.2/32         -                1/1/46        -

L         [0/0]        -

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.0.1.0/24         -                vlan2001      -
C         [0/0]        -

20.0.1.3/32         -                vlan2001      -

L         [0/0]        -

20.3.1.0/24         -                vlan2031      -

C         [0/0]        -

20.3.1.1/32         -                vlan2031      -

L         [0/0]        -

20.4.1.0/24         -                vlan2041      -

C         [0/0]        -

20.4.1.1/32         -                vlan2041      -

L         [0/0]        -

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 42

101.0.0.0/24        20.0.1.1         vlan2001      -

B/I       [200/0]      01h:11m:55s

201.0.0.0/24        20.4.1.2         vlan2041      -

B/E       [20/0]       01h:10m:34s

                    20.3.1.2         vlan2031

-                           [20/0]       01h:10m:34s

VRF: vrf_2

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.0.1.0/24         -                vlan2002      -

C         [0/0]        -

20.0.1.3/32         -                vlan2002      -

L         [0/0]        -

20.3.1.0/24         -                vlan2032      -

C         [0/0]        -

20.3.1.1/32         -                vlan2032      -

L         [0/0]        -

20.4.1.0/24         -                vlan2042      -

C         [0/0]        -

20.4.1.1/32         -                vlan2042      -

L         [0/0]        -

102.0.0.0/24        20.0.1.1         vlan2002      -

B/I       [200/0]      00h:54m:06s

202.0.0.0/24        20.4.1.2         vlan2042      -

B/E       [20/0]       00h:54m:06s

                    20.3.1.2         vlan2032

-                           [20/0]       00h:54m:06s

Total Route Count : 18

CE3 configuration

CE3# show running-config

Current configuration:

!

!Version ArubaOS-CX GL.10.09.0001BF

!export-password: default
hostname CE3

profile l3-core

logging console severity crit

vrf vrf_1

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 43

vrf vrf_2

cli-session

    timeout 0

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2051-2052,2061-2062

interface mgmt

    no shutdown

    ip dhcp

system interface-group 4 speed 10g

    !interface group 4 contains ports 1/1/37-1/1/48

interface 1/1/41

    no shutdown

    mtu 9000

    description Towards PE3

    no routing

    vlan trunk native 1

    vlan trunk allowed 2051-2052

interface 1/1/42

    no shutdown

    mtu 9000

    description Towards LAN

    no routing

    vlan trunk native 1

    vlan trunk allowed 2061-2062

interface vlan 2051

    vrf attach vrf_1

    description Towards PE3
    ip mtu 9000

    ip address 20.5.1.2/24

interface vlan 2052

    vrf attach vrf_2

    description Towards PE3

    ip mtu 9000

    ip address 20.5.1.2/24

interface vlan 2061

    vrf attach vrf_1

    description Towards LAN

    ip mtu 9000

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 44

ip address 20.6.1.1/24

interface vlan 2062

    vrf attach vrf_2

    description Towards LAN

    ip mtu 9000

    ip address 20.6.1.1/24

!

!

!

!

!

router bgp 100

!

    vrf vrf_1

        neighbor 20.5.1.1 remote-as 6488163

        neighbor 20.5.1.1 description Towards PE3

        neighbor 20.6.1.2 remote-as 100

        neighbor 20.6.1.2 description Towards LAN

        address-family ipv4 unicast

            neighbor 20.5.1.1 activate

            neighbor 20.5.1.1 allowas-in 1

            neighbor 20.5.1.1 send-community both

            neighbor 20.5.1.1 soft-reconfiguration inbound

            neighbor 20.6.1.2 activate

            neighbor 20.6.1.2 next-hop-self

            neighbor 20.6.1.2 send-community both

            neighbor 20.6.1.2 soft-reconfiguration inbound

        exit-address-family

!

    vrf vrf_2

        neighbor 20.5.1.1 remote-as 6488163

        neighbor 20.5.1.1 description Towards PE3
        neighbor 20.6.1.2 remote-as 100

        neighbor 20.6.1.2 description Towards LAN

        address-family ipv4 unicast

            neighbor 20.5.1.1 activate

            neighbor 20.5.1.1 allowas-in 1

            neighbor 20.5.1.1 send-community both

            neighbor 20.5.1.1 soft-reconfiguration inbound

            neighbor 20.6.1.2 activate

            neighbor 20.6.1.2 next-hop-self

            neighbor 20.6.1.2 send-community both

            neighbor 20.6.1.2 soft-reconfiguration inbound

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 45

exit-address-family

!

https-server vrf mgmt

CE3 verification

CE3#  show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : (null)

 Peers                  : 0            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : L2VPN EVPN

-----------------------------

VRF : vrf_1

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 20.6.1.1

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.5.1.1        6488163     34      33      00h:25m:12s  Established   Up
 20.6.1.2        100         54      62      00h:25m:04s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

VRF : vrf_2

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 20.6.1.1

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 46

Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.5.1.1        6488163     34      34      00h:25m:11s  Established   Up

 20.6.1.2        100         56      63      00h:25m:04s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

CE3#  show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Router-ID not configured

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : L2VPN EVPN

-----------------------------

     Network                                               Nexthop

Metric     LocPrf    Weight   Path

----------------------------------------------------------------------------

--------------------------------

Total number of entries 0

VRF : vrf_1

Local Router-ID 20.6.1.1

Address-family : IPv4 Unicast

-----------------------------
    Network            Nexthop         Metric     LocPrf     Weight Path

*>e 101.0.0.0/24       20.5.1.1        0          100        0

6488163 100 i

*>i 201.0.0.0/24       20.6.1.2        0          0          0       i

Total number of entries 2

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

VRF : vrf_2

Local Router-ID 20.6.1.1

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 47

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*>e 102.0.0.0/24       20.5.1.1        0          100        0

6488163 100 i

*>i 202.0.0.0/24       20.6.1.2        0          0          0       i

Total number of entries 2

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

CE3# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.5.1.0/24         -                vlan2051      -

C         [0/0]        -

20.5.1.2/32         -                vlan2051      -

L         [0/0]        -

20.6.1.0/24         -                vlan2061      -

C         [0/0]        -

20.6.1.1/32         -                vlan2061      -
L         [0/0]        -

101.0.0.0/24        20.5.1.1         vlan2051      -

B/E       [20/0]       01h:10m:42s

201.0.0.0/24        20.6.1.2         vlan2061      -

B/I       [200/0]      01h:10m:34s

VRF: vrf_2

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 48

------------------

20.5.1.0/24         -                vlan2052      -

C         [0/0]        -

20.5.1.2/32         -                vlan2052      -

L         [0/0]        -

20.6.1.0/24         -                vlan2062      -

C         [0/0]        -

20.6.1.1/32         -                vlan2062      -

L         [0/0]        -

102.0.0.0/24        20.5.1.1         vlan2052      -

B/E       [20/0]       00h:54m:06s

202.0.0.0/24        20.6.1.2         vlan2062      -

B/I       [200/0]      00h:54m:06s

Total Route Count : 12

P1 configuration

P1# show running-config

Current configuration:

!

!Version ArubaOS-CX LL.10.09.0001BF

!export-password: default

hostname P1

profile core-spine

logging console severity crit

cli-session

    timeout 0

!

!

!

!

!
!

ssh server vrf mgmt

vlan 1

interface mgmt

    no shutdown

    ip dhcp

system interface-group 1 speed 10g

    !interface group 1 contains ports 1/1/1-1/1/4

interface lag 99

    no shutdown

    description Towards PE3

    ip mtu 9198

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 49

ip address 30.0.2.1/24

    lacp mode active

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/14

    no shutdown

    mtu 9198

    description Towards PE1

    ip mtu 9198

    ip address 30.0.0.2/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/15

    no shutdown

    mtu 9198

    description Towards PE2

    ip mtu 9198

    ip address 30.0.1.2/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/16

    no shutdown

    mtu 9198

    description Towards PE3

    lag 99

interface 1/1/17

    no shutdown

    mtu 9198

    description Towards PE3
    lag 99

interface 1/1/27

    description Towards PE3

interface 1/1/28

    description Towards PE3

interface loopback 0

    ip address 4.4.4.4/32

    ip ospf 1 area 0.0.0.0

!

!

!

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 50

!

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 1.1.1.1 remote-as 6488163

    neighbor 1.1.1.1 description Towards PE1

    neighbor 1.1.1.1 update-source loopback 0

    neighbor 2.2.2.2 remote-as 6488163

    neighbor 2.2.2.2 description Towards PE2

    neighbor 2.2.2.2 update-source loopback 0

    neighbor 3.3.3.3 remote-as 6488163

    neighbor 3.3.3.3 description Towards PE2

    neighbor 3.3.3.3 update-source loopback 0

    neighbor 5.5.5.5 remote-as 6488163

    neighbor 5.5.5.5 description Towards RR2

    neighbor 5.5.5.5 update-source loopback 0

    address-family vpnv4 unicast

        neighbor 1.1.1.1 activate

        neighbor 1.1.1.1 route-reflector-client

        neighbor 1.1.1.1 send-community both

        neighbor 2.2.2.2 activate

        neighbor 2.2.2.2 route-reflector-client

        neighbor 2.2.2.2 send-community both

        neighbor 3.3.3.3 activate

        neighbor 3.3.3.3 route-reflector-client

        neighbor 3.3.3.3 send-community both

        neighbor 5.5.5.5 activate

        neighbor 5.5.5.5 send-community both

    exit-address-family

!

https-server vrf mgmt
mpls

    enable

    label-protocol ldp

        enable

        router-id loopback0

P1 verification

P1# show ip ospf neighbors

VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 3

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 51

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

1.1.1.1          1         FULL/DR           30.0.0.1           1/1/14

2.2.2.2          1         FULL/BDR          30.0.1.1           1/1/15

3.3.3.3          1         FULL/BDR          30.0.2.2           lag99

P1# show mpls ldp neighbor

Local LDP Identifier: 4.4.4.4:0, Peer LDP Identifier: 2.2.2.2:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:36

    State: operational

    LDP Discovery Sources: 1/1/15

    Addresses bound to this peer:

         2.2.2.2 30.0.1.1 30.0.4.1

Local LDP Identifier: 4.4.4.4:0, Peer LDP Identifier: 3.3.3.3:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:12:42

    State: operational

    LDP Discovery Sources: lag99

    Addresses bound to this peer:

         3.3.3.3 30.0.2.2 30.0.5.2

Local LDP Identifier: 4.4.4.4:0, Peer LDP Identifier: 1.1.1.1:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:36

    State: operational

    LDP Discovery Sources: 1/1/14

    Addresses bound to this peer:

         1.1.1.1 30.0.0.1 30.0.3.1

P1# show mpls ldp binding

30.0.4.1/32
        No local binding

        remote binding: lsr:2.2.2.2:0 label: exp-null

30.0.2.1/32

        local binding: label: exp-null

        No remote binding

30.0.1.2/32

        local binding: label: exp-null

        No remote binding

30.0.0.1/32

        No local binding

        remote binding: lsr:1.1.1.1:0 label: exp-null

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 52

30.0.1.1/32

        No local binding

        remote binding: lsr:2.2.2.2:0 label: exp-null

30.0.5.2/32

        No local binding

        remote binding: lsr:3.3.3.3:0 label: exp-null

30.0.2.2/32

        No local binding

        remote binding: lsr:3.3.3.3:0 label: exp-null

2.2.2.2/32

        local binding: label: 18

        remote binding: lsr:1.1.1.1:0 label:18

        remote binding: lsr:3.3.3.3:0 label:17

        remote binding: lsr:2.2.2.2:0 label: exp-null

5.5.5.5/32

        local binding: label: 17

        remote binding: lsr:1.1.1.1:0 label:17

        remote binding: lsr:3.3.3.3:0 label:19

        remote binding: lsr:2.2.2.2:0 label:18

30.0.0.2/32

        local binding: label: exp-null

        No remote binding

3.3.3.3/32

        local binding: label: 19

        remote binding: lsr:1.1.1.1:0 label:19

        remote binding: lsr:3.3.3.3:0 label: exp-null

        remote binding: lsr:2.2.2.2:0 label:19

4.4.4.4/32

        local binding: label: exp-null

        remote binding: lsr:1.1.1.1:0 label:16

        remote binding: lsr:3.3.3.3:0 label:18

        remote binding: lsr:2.2.2.2:0 label:17
30.0.3.1/32

        No local binding

        remote binding: lsr:1.1.1.1:0 label: exp-null

1.1.1.1/32

        local binding: label: 16

        remote binding: lsr:1.1.1.1:0 label: exp-null

        remote binding: lsr:3.3.3.3:0 label:16

        remote binding: lsr:2.2.2.2:0 label:16

P1# show mpls forwarding

MPLS Bindings

Entry Bindings   : 4

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 53

Exit Bindings    : 2

Transit Bindings : 4

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix      Ingress  Nexthop    Outgoing  Egress     Egress   Status

                   VRF      Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    5.5.5.5/32  default  30.0.2.2   19        lag99      default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

static   n/a                 exp-null  -         default

operational

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

LDP     1.1.1.1/32   16        1/1/14     default  30.0.0.1  exp-null

Operational

LDP     5.5.5.5/32   17        lag99      default  30.0.2.2  19

Operational

LDP     2.2.2.2/32   18        1/1/15     default  30.0.1.1  exp-null
Operational

LDP     3.3.3.3/32   19        lag99      default  30.0.2.2  exp-null

Operational

P1# show bgp vpnv4 un neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 1.1.1.1 (Internal)

    Description         : Towards PE1

    Peer-group          :

    Remote Router Id    : 1.1.1.1            Local Router Id    : 4.4.4.4

    Remote AS           : 6488163            Local AS           : 6488163

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 54

Remote Port         : 42093              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:55s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      7        3

    Keepalives                  18       18

    Route Refresh                0        0

    Total                       26       22

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No
    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : Yes                 Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 55

Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 2.2.2.2 (Internal)

    Description         : Towards PE2

    Peer-group          :

    Remote Router Id    : 2.2.2.2            Local Router Id    : 4.4.4.4

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 44703              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:21s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----
    Open                         1        1

    Notification                 0        0

    Updates                      5        3

    Keepalives                  17       18

    Route Refresh                0        0

    Total                       23       22

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 56

Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : Yes                 Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 3.3.3.3 (Internal)

    Description         : Towards PE2

    Peer-group          :

    Remote Router Id    : 3.3.3.3            Local Router Id    : 4.4.4.4

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 33231

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:14m:48s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :
    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 57

Open                         1        1

    Notification                 0        0

    Updates                      3        3

    Keepalives                  18       17

    Route Refresh                0        0

    Total                       22       21

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : Yes                 Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 5.5.5.5 (Internal)

    Description         : Towards RR2

    Peer-group          :

    Remote Router Id    : 5.5.5.5            Local Router Id    : 4.4.4.4
    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 40545

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:33s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 58

Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      7        6

    Keepalives                  17       17

    Route Refresh                0        0

    Total                       25       24

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :
    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

P1#  show bgp vpnv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 59

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 4.4.4.4

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 102.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 10

P1# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 4.4.4.4

 Peers                  : 4            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast
------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 1.1.1.1         6488163     36      43      00h:27m:27s  Established   Up

 2.2.2.2         6488163     37      40      00h:26m:53s  Established   Up

 3.3.3.3         6488163     35      40      00h:26m:20s  Established   Up

 5.5.5.5         6488163     39      40      00h:27m:05s  Established   Up

Address-family : L2VPN EVPN

-----------------------------

P1#  show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 60

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 4.4.4.4

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : VPNv4 Unicast

------------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 102.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 10

Address-family : L2VPN EVPN
-----------------------------

     Network                                               Nexthop

Metric     LocPrf    Weight   Path

----------------------------------------------------------------------------

--------------------------------

Total number of entries 0

P1# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 61

IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          30.0.0.1         1/1/14        -

O         [110/100]    01h:13m:03s

2.2.2.2/32          30.0.1.1         1/1/15        -

O         [110/100]    01h:12m:33s

3.3.3.3/32          30.0.2.2         lag99         -

O         [110/50]     01h:11m:57s

4.4.4.4/32          -                loopback0     -

L         [0/0]        -

5.5.5.5/32          30.0.2.2         lag99         -

O         [110/100]    01h:11m:52s

30.0.0.0/24         -                1/1/14        -

C         [0/0]        -

30.0.0.2/32         -                1/1/14        -

L         [0/0]        -

30.0.1.0/24         -                1/1/15        -

C         [0/0]        -

30.0.1.2/32         -                1/1/15        -

L         [0/0]        -

30.0.2.0/24         -                lag99         -

C         [0/0]        -

30.0.2.1/32         -                lag99         -

L         [0/0]        -

30.0.3.0/24         30.0.0.1         1/1/14        -
O         [110/200]    01h:11m:52s

                    30.0.2.2         lag99

-                           [110/200]    01h:11m:52s

30.0.4.0/24         30.0.1.1         1/1/15        -

O         [110/200]    01h:11m:52s

                    30.0.2.2         lag99

-                           [110/200]    01h:11m:52s

30.0.5.0/24         30.0.2.2         lag99         -

O         [110/100]    01h:11m:57s

Total Route Count : 14

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 62

P2 configuration

P2# show running

Current configuration:

!

!Version ArubaOS-CX LL.10.09.0001BF

!export-password: default

hostname P2

profile core-spine

logging console severity crit

cli-session

    timeout 0

!

!

!

!

!

!

ssh server vrf mgmt

vlan 1

interface mgmt

    no shutdown

    ip dhcp

system interface-group 1 speed 10g

    !interface group 1 contains ports 1/1/1-1/1/4

interface lag 100

    no shutdown

    description Towards PE3

    ip mtu 9198

    ip address 30.0.5.1/24

    lacp mode active

    ip ospf 1 area 0.0.0.0
    mpls enable

    mpls ldp enable

interface 1/1/25

    no shutdown

    mtu 9198

    description Towards PE1

    ip mtu 9198

    ip address 30.0.3.2/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/26

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 63

no shutdown

    mtu 9198

    description Towards PE2

    ip mtu 9198

    ip address 30.0.4.2/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/27

    no shutdown

    mtu 9198

    description Towards PE3

    lag 100

interface 1/1/28

    no shutdown

    mtu 9198

    description Towards PE3

    lag 100

interface loopback 0

    ip address 5.5.5.5/32

    ip ospf 1 area 0.0.0.0

!

!

!

!

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 1.1.1.1 remote-as 6488163

    neighbor 1.1.1.1 description Towards PE1

    neighbor 1.1.1.1 update-source loopback 0
    neighbor 2.2.2.2 remote-as 6488163

    neighbor 2.2.2.2 description Towards PE2

    neighbor 2.2.2.2 update-source loopback 0

    neighbor 3.3.3.3 remote-as 6488163

    neighbor 3.3.3.3 description Towards PE3

    neighbor 3.3.3.3 update-source loopback 0

    neighbor 4.4.4.4 remote-as 6488163

    neighbor 4.4.4.4 description Towards RR1

    neighbor 4.4.4.4 update-source loopback 0

    address-family vpnv4 unicast

        neighbor 1.1.1.1 activate

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 64

neighbor 1.1.1.1 route-reflector-client

        neighbor 1.1.1.1 send-community both

        neighbor 2.2.2.2 activate

        neighbor 2.2.2.2 route-reflector-client

        neighbor 2.2.2.2 send-community both

        neighbor 3.3.3.3 activate

        neighbor 3.3.3.3 route-reflector-client

        neighbor 3.3.3.3 send-community both

        neighbor 4.4.4.4 activate

        neighbor 4.4.4.4 send-community both

    exit-address-family

!

https-server vrf mgmt

mpls

    enable

    label-protocol ldp

        enable

        router-id loopback0

P2 verification

P2# show ip ospf neighbors

VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 3

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

1.1.1.1          1         FULL/DR           30.0.3.1           1/1/25

2.2.2.2          1         FULL/DR           30.0.4.1           1/1/26

3.3.3.3          1         FULL/BDR          30.0.5.2           lag100

P2#  show mpls ldp neighbor

Local LDP Identifier: 5.5.5.5:0, Peer LDP Identifier: 3.3.3.3:0
    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:12:42

    State: operational

    LDP Discovery Sources: lag100

    Addresses bound to this peer:

         3.3.3.3 30.0.2.2 30.0.5.2

Local LDP Identifier: 5.5.5.5:0, Peer LDP Identifier: 1.1.1.1:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:19

    State: operational

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 65

LDP Discovery Sources: 1/1/25

    Addresses bound to this peer:

         1.1.1.1 30.0.0.1 30.0.3.1

Local LDP Identifier: 5.5.5.5:0, Peer LDP Identifier: 2.2.2.2:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:14

    State: operational

    LDP Discovery Sources: 1/1/26

    Addresses bound to this peer:

         2.2.2.2 30.0.1.1 30.0.4.1

P2#  show mpls ldp binding

30.0.3.2/32

        local binding: label: exp-null

        No remote binding

30.0.1.1/32

        No local binding

        remote binding: lsr:2.2.2.2:0 label: exp-null

2.2.2.2/32

        local binding: label: 18

        remote binding: lsr:1.1.1.1:0 label:18

        remote binding: lsr:3.3.3.3:0 label:17

        remote binding: lsr:2.2.2.2:0 label: exp-null

30.0.5.1/32

        local binding: label: exp-null

        No remote binding

30.0.4.2/32

        local binding: label: exp-null

        No remote binding

5.5.5.5/32

        local binding: label: exp-null

        remote binding: lsr:1.1.1.1:0 label:17
        remote binding: lsr:3.3.3.3:0 label:19

        remote binding: lsr:2.2.2.2:0 label:18

30.0.0.1/32

        No local binding

        remote binding: lsr:1.1.1.1:0 label: exp-null

30.0.2.2/32

        No local binding

        remote binding: lsr:3.3.3.3:0 label: exp-null

30.0.5.2/32

        No local binding

        remote binding: lsr:3.3.3.3:0 label: exp-null

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 66

4.4.4.4/32

        local binding: label: 17

        remote binding: lsr:1.1.1.1:0 label:16

        remote binding: lsr:3.3.3.3:0 label:18

        remote binding: lsr:2.2.2.2:0 label:17

30.0.4.1/32

        No local binding

        remote binding: lsr:2.2.2.2:0 label: exp-null

1.1.1.1/32

        local binding: label: 16

        remote binding: lsr:1.1.1.1:0 label: exp-null

        remote binding: lsr:3.3.3.3:0 label:16

        remote binding: lsr:2.2.2.2:0 label:16

3.3.3.3/32

        local binding: label: 19

        remote binding: lsr:1.1.1.1:0 label:19

        remote binding: lsr:3.3.3.3:0 label: exp-null

        remote binding: lsr:2.2.2.2:0 label:19

30.0.3.1/32

        No local binding

        remote binding: lsr:1.1.1.1:0 label: exp-null

P2# show mpls forwarding

MPLS Bindings

Entry Bindings   : 4

Exit Bindings    : 2

Transit Bindings : 4

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix      Ingress  Nexthop    Outgoing  Egress     Egress   Status

                   VRF      Address    Label     Interface  VRF
----------------------------------------------------------------------------

---

LDP    4.4.4.4/32  default  30.0.5.2   18        lag100     default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

static   n/a                 exp-null  -         default

operational

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 67

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

LDP     1.1.1.1/32   16        1/1/25     default  30.0.3.1  exp-null

operational

LDP     4.4.4.4/32   17        lag100     default  30.0.5.2  18

operational  LDP     2.2.2.2/32   18        1/1/26     default  30.0.4.1

exp-null  operational  LDP     3.3.3.3/32   18        lag100     default

30.0.5.2  exp-null  operational

P2# show bgp vpnv4 un neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 1.1.1.1 (Internal)

    Description         : Towards PE1

    Peer-group          :

    Remote Router Id    : 1.1.1.1            Local Router Id    : 5.5.5.5

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 40029              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:40s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :
    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 68

Open                         1        1

    Notification                 0        0

    Updates                      5        3

    Keepalives                  16       17

    Route Refresh                0        0

    Total                       22       21

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : Yes                 Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 2.2.2.2 (Internal)

    Description         : Towards PE2

    Peer-group          :

    Remote Router Id    : 2.2.2.2            Local Router Id    : 5.5.5.5
    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 33107

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:30s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 69

Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      5        3

    Keepalives                  17       17

    Route Refresh                0        0

    Total                       23       21

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : Yes                 Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :
    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 3.3.3.3 (Internal)

    Description         : Towards PE3

    Peer-group          :

    Remote Router Id    : 3.3.3.3            Local Router Id    : 5.5.5.5

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 70

Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 39781

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:14m:46s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      3        3

    Keepalives                  17       17

    Route Refresh                0        0

    Total                       21       21

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes
    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : Yes                 Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 71

Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 4.4.4.4 (Internal)

    Description         : Towards RR1

    Peer-group          :

    Remote Router Id    : 4.4.4.4            Local Router Id    : 5.5.5.5

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 40545              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:33s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd
    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      6        7

    Keepalives                  17       17

    Route Refresh                0        0

    Total                       24       25

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 72

Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

P2# show bgp vpnv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 5.5.5.5

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 2:1                  (Label 21)

*>i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       2.2.2.2         0          100        0       100 i

Route Distinguisher: 1:1                  (Label 20)

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 20)
*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 5

P2# show mpls forwarding

MPLS Bindings

Entry Bindings   : 4

Exit Bindings    : 2

Transit Bindings : 4

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 73

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix      Ingress  Nexthop    Outgoing  Egress     Egress   Status

                   VRF      Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    4.4.4.4/32  default  30.0.5.2   18        lag100     default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

static   n/a                 exp-null  -         default

operational

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

------

LDP     1.1.1.1/32   16        1/1/25     default  30.0.3.1  exp-null

operational

LDP     4.4.4.4/32   17        lag100     default  30.0.5.2  18

operational  LDP     2.2.2.2/32   18        1/1/26     default  30.0.4.1

exp-null  operational  LDP     3.3.3.3/32   18        lag100     default

30.0.5.2  exp-null  operational

P2# show bgp vpnv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =
multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 5.5.5.5

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 74

*>i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 102.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 10

P2# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 5.5.5.5

 Peers                  : 4            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast

------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 1.1.1.1         6488163     34      39      00h:27m:12s  Established   Up

 2.2.2.2         6488163     35      41      00h:27m:02s  Established   Up

 3.3.3.3         6488163     36      39      00h:26m:17s  Established   Up

 4.4.4.4         6488163     40      39      00h:27m:05s  Established   Up

Address-family : L2VPN EVPN

-----------------------------
P2# show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 5.5.5.5

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 75

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : VPNv4 Unicast

------------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 102.0.0.0/24       2.2.2.2         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 10

Address-family : L2VPN EVPN

-----------------------------

     Network                                               Nexthop

Metric     LocPrf    Weight   Path

----------------------------------------------------------------------------

--------------------------------

Total number of entries 0

P2# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local
              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 76

1.1.1.1/32          30.0.3.1         1/1/25        -

O         [110/100]    01h:12m:46s

2.2.2.2/32          30.0.4.1         1/1/26        -

O         [110/100]    01h:12m:21s

3.3.3.3/32          30.0.5.2         lag100        -

O         [110/50]     01h:11m:52s

4.4.4.4/32          30.0.5.2         lag100        -

O         [110/100]    01h:11m:52s

5.5.5.5/32          -                loopback0     -

L         [0/0]        -

30.0.0.0/24         30.0.5.2         lag100        -

O         [110/200]    01h:11m:52s

                    30.0.3.1         1/1/25

-                           [110/200]    01h:11m:52s

30.0.1.0/24         30.0.4.1         1/1/26        -

O         [110/200]    01h:11m:52s

                    30.0.5.2         lag100

-                           [110/200]    01h:11m:52s

30.0.2.0/24         30.0.5.2         lag100        -

O         [110/100]    01h:11m:52s

30.0.3.0/24         -                1/1/25        -

C         [0/0]        -

30.0.3.2/32         -                1/1/25        -

L         [0/0]        -

30.0.4.0/24         -                1/1/26        -

C         [0/0]        -

30.0.4.2/32         -                1/1/26        -

L         [0/0]        -

30.0.5.0/24         -                lag100        -

C         [0/0]        -

30.0.5.1/32         -                lag100        -

L         [0/0]        -
Total Route Count : 14

PE1 configuration

PE1# show running

Current configuration:

!

!Version ArubaOS-CX LL.10.09.0001BF
!export-password: default

hostname PE1

profile core-spine

logging console severity crit

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 77

vrf vrf_1

    rd 1:1

    l3vpn-only

    address-family ipv4 unicast

        route-target export 1:1

        route-target import 1:1

    exit-address-family

vrf vrf_2

    rd 2:1

    l3vpn-only

    address-family ipv4 unicast

        route-target export 2:1

        route-target import 2:1

    exit-address-family

cli-session

    timeout 0

!

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2011-2012,2031-2032

interface mgmt

    no shutdown

    ip dhcp

interface 1/1/37

    no shutdown

    mtu 9000

    description Towards CE1

    no routing
    vlan trunk native 1

    vlan trunk allowed 2011-2012

interface 1/1/38

    no shutdown

    mtu 9000

    description Towards CE2

    no routing

    vlan trunk native 1

    vlan trunk allowed 2031-2032

interface 1/1/39

    no shutdown

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 78

mtu 9198

    description Towards P1

    ip mtu 9198

    ip address 30.0.0.1/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/40

    no shutdown

    mtu 9198

    description Towards P2

    ip mtu 9198

    ip address 30.0.3.1/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface loopback 0

    ip address 1.1.1.1/32

    ip ospf 1 area 0.0.0.0

interface vlan 2011

    vrf attach vrf_1

    description Towards CE1

    ip mtu 9000

    ip address 20.1.1.2/24

interface vlan 2012

    vrf attach vrf_2

    description Towards CE1

    ip mtu 9000

    ip address 20.1.1.2/24

interface vlan 2031

    vrf attach vrf_1

    description Towards CE2
    ip mtu 9000

    ip address 20.3.1.2/24

interface vlan 2032

    vrf attach vrf_2

    description Towards CE2

    ip mtu 9000

    ip address 20.3.1.2/24

!

ip community-list standard site1_community description

For_setting_community_From_Site1

ip community-list standard site1_community seq 10 permit 99:99

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 79

!

!

!

route-map rmap1 permit seq 10

     description For_setting_community_For Site1_Received_EBGP_routes

     set community 99:99

route-map rmap2 deny seq 10

     description For_Denying_routes_with_Site1_community_To_EBGP_Peer

     match community-list site1_community

route-map rmap2 permit seq 20

     description For_Allowing_all_other_route

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 4.4.4.4 remote-as 6488163

    neighbor 4.4.4.4 description Towards RR1{P1}

    neighbor 4.4.4.4 update-source loopback 0

    neighbor 5.5.5.5 remote-as 6488163

    neighbor 5.5.5.5 description Towards RR2{P2}

    neighbor 5.5.5.5 update-source loopback 0

    address-family vpnv4 unicast

        neighbor 4.4.4.4 activate

        neighbor 4.4.4.4 send-community both

        neighbor 5.5.5.5 activate

        neighbor 5.5.5.5 send-community both

    exit-address-family

!

    vrf vrf_1

        neighbor 20.1.1.1 remote-as 100

        neighbor 20.1.1.1 description Towards CE1

        neighbor 20.3.1.1 remote-as 100
        neighbor 20.3.1.1 description Towards CE2

        address-family ipv4 unicast

            neighbor 20.1.1.1 activate

            neighbor 20.1.1.1 route-map rmap1 in

            neighbor 20.1.1.1 route-map rmap2 out

            neighbor 20.1.1.1 send-community both

            neighbor 20.1.1.1 soft-reconfiguration inbound

            neighbor 20.3.1.1 activate

            neighbor 20.3.1.1 route-map rmap1 in

            neighbor 20.3.1.1 route-map rmap2 out

            neighbor 20.3.1.1 send-community both

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 80

neighbor 20.3.1.1 soft-reconfiguration inbound

        exit-address-family

!

    vrf vrf_2

        neighbor 20.1.1.1 remote-as 100

        neighbor 20.1.1.1 description Towards CE1

        neighbor 20.3.1.1 remote-as 100

        neighbor 20.3.1.1 description Towards CE2

        address-family ipv4 unicast

            neighbor 20.1.1.1 activate

            neighbor 20.1.1.1 route-map rmap1 in

            neighbor 20.1.1.1 route-map rmap2 out

            neighbor 20.1.1.1 send-community both

            neighbor 20.1.1.1 soft-reconfiguration inbound

            neighbor 20.3.1.1 activate

            neighbor 20.3.1.1 route-map rmap1 in

            neighbor 20.3.1.1 route-map rmap2 out

            neighbor 20.3.1.1 send-community both

            neighbor 20.3.1.1 soft-reconfiguration inbound

        exit-address-family

!

https-server vrf mgmt

mpls

    enable

    label-protocol ldp

        enable

        router-id loopback0

PE1 verification

PE1# show ip ospf neighbors

VRF : default                          Process : 1
===================================================

Total Number of Neighbors : 2

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

4.4.4.4          1         FULL/BDR          30.0.0.2           1/1/39

5.5.5.5          1         FULL/BDR          30.0.3.2           1/1/40

PE1# show mpls ldp neighbor

Local LDP Identifier: 1.1.1.1:0, Peer LDP Identifier: 4.4.4.4:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:36

    State: operational

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 81

LDP Discovery Sources: 1/1/39

    Addresses bound to this peer:

         30.0.0.2 30.0.1.2 30.0.2.1 4.4.4.4

Local LDP Identifier: 1.1.1.1:0, Peer LDP Identifier: 5.5.5.5:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:19

    State: operational

    LDP Discovery Sources: 1/1/40

    Addresses bound to this peer:

         30.0.3.2 30.0.4.2 30.0.5.1 5.5.5.5

PE1# show mpls ldp binding

5.5.5.5/32

        local binding: label: 17

        remote binding: lsr:5.5.5.5:0 label: exp-null

        remote binding: lsr:4.4.4.4:0 label:17

30.0.1.2/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

30.0.3.2/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

30.0.2.1/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

1.1.1.1/32

        local binding: label: exp-null

        remote binding: lsr:5.5.5.5:0 label:16

        remote binding: lsr:4.4.4.4:0 label:16

4.4.4.4/32

        local binding: label: 16

        remote binding: lsr:5.5.5.5:0 label:17
        remote binding: lsr:4.4.4.4:0 label: exp-null

30.0.0.1/32

        local binding: label: exp-null

        No remote binding

3.3.3.3/32

        local binding: label: 19

        remote binding: lsr:5.5.5.5:0 label:19

        remote binding: lsr:4.4.4.4:0 label:19

30.0.0.2/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 82

30.0.4.2/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

2.2.2.2/32

        local binding: label: 18

        remote binding: lsr:5.5.5.5:0 label:18

        remote binding: lsr:4.4.4.4:0 label:18

30.0.3.1/32

        local binding: label: exp-null

        No remote binding

30.0.5.1/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

PE1# show mpls forwarding

MPLS Bindings

Entry Bindings   : 8

Exit Bindings    : 4

Transit Bindings : 6

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix       Ingress  Nexthop    Outgoing  Egress     Egress   Status

                    VRF      Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    2.2.2.2/32   default  30.0.3.2   18        1/1/40     default

operational

LDP    2.2.2.2/32   default  30.0.0.2   18        1/1/39     default

operational

LDP    3.3.3.3/32   default  30.0.3.2   19        1/1/40     default

operational
LDP    3.3.3.3/32   default  30.0.0.2   19        1/1/39     default

operational

BGP    201.0.0.0/24 vrf_1    3.3.3.3    21        1/1/40     default

operational

BGP    202.0.0.0/24 vrf_2    3.3.3.3    22        1/1/40     default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 83

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  20        vrf_1

operational

BGP      n/a                 imp-null  22        vrf_2

operational

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

-----

LDP     4.4.4.4/32   16        1/1/39     default  30.0.0.2  exp-null

operational

LDP     5.5.5.5/32   17        1/1/40     default  30.0.3.2  exp-null

operational

LDP     2.2.2.2/32   18        1/1/40     default  30.0.3.2  18

operational

LDP     2.2.2.2/32   18        1/1/39     default  30.0.0.2  18

operational

LDP     3.3.3.3/32   19        1/1/40     default  30.0.3.2  19

operational

LDP     3.3.3.3/32   19        1/1/39     default  30.0.0.2  19

operational

PE1# show bgp vpnv4 un neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 4.4.4.4 (Internal)

    Description         : Towards RR1{P1}
    Peer-group          :

    Remote Router Id    : 4.4.4.4            Local Router Id    : 1.1.1.1

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 42093

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:55s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 84

BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      3        7

    Keepalives                  18       18

    Route Refresh                0        0

    Total                       22       26

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both
    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 5.5.5.5 (Internal)

    Description         : Towards RR2{P2}

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 85

Peer-group          :

    Remote Router Id    : 5.5.5.5            Local Router Id    : 1.1.1.1

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 40029

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:40s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      3        5

    Keepalives                  17       16

    Route Refresh                0        0

    Total                       21       22

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------
    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 86

Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE1# show bgp vpnv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 1.1.1.1

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>  101.0.0.0/24       0.0.0.0         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>  102.0.0.0/24       0.0.0.0         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 6

PE1# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------
 Local AS               : 6488163      BGP Router Identifier  : 1.1.1.1

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast

------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 87

AdminStatus

 4.4.4.4         6488163     43      36      00h:27m:27s  Established   Up

 5.5.5.5         6488163     39      34      00h:27m:12s  Established   Up

Address-family : L2VPN EVPN

-----------------------------

VRF : vrf_1

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.3.1.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.1.1.1        100         36      37      00h:28m:34s  Established   Up

 20.3.1.1        100         36      36      00h:28m:34s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

VRF : vrf_2

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.3.1.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.1.1.1        100         40      37      00h:28m:33s  Established   Up
 20.3.1.1        100         40      38      00h:28m:42s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

PE1# show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 1.1.1.1

Address-family : IPv4 Unicast

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 88

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : VPNv4 Unicast

------------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>  101.0.0.0/24       0.0.0.0         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>  102.0.0.0/24       0.0.0.0         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 6

Address-family : L2VPN EVPN

-----------------------------

     Network                                               Nexthop

Metric     LocPrf    Weight   Path

----------------------------------------------------------------------------

--------------------------------

Total number of entries 0

VRF : vrf_1

Local Router-ID 20.3.1.2

Address-family : IPv4 Unicast

-----------------------------
    Network            Nexthop         Metric     LocPrf     Weight Path

*=e 101.0.0.0/24       20.1.1.1        0          100        0       100 i

*>e 101.0.0.0/24       20.3.1.1        0          100        0       100 i

*>  201.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 3

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

VRF : vrf_2

Local Router-ID 20.3.1.2

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 89

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*=e 102.0.0.0/24       20.1.1.1        0          100        0       100 i

*>e 102.0.0.0/24       20.3.1.1        0          100        0       100 i

*>  202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 3

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

PE1# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          -                loopback0     -

L         [0/0]        -

2.2.2.2/32          30.0.3.2         1/1/40        -

O         [110/200]    01h:12m:16s

                    30.0.0.2         1/1/39

-                           [110/200]    01h:12m:16s

3.3.3.3/32          30.0.3.2         1/1/40        -
O         [110/150]    01h:11m:52s

                    30.0.0.2         1/1/39

-                           [110/150]    01h:11m:52s

4.4.4.4/32          30.0.0.2         1/1/39        -

O         [110/100]    01h:13m:07s

5.5.5.5/32          30.0.3.2         1/1/40        -

O         [110/100]    01h:12m:46s

30.0.0.0/24         -                1/1/39        -

C         [0/0]        -

30.0.0.1/32         -                1/1/39        -

L         [0/0]        -

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 90

30.0.1.0/24         30.0.0.2         1/1/39        -

O         [110/200]    01h:13m:07s

30.0.2.0/24         30.0.0.2         1/1/39        -

O         [110/150]    01h:12m:42s

30.0.3.0/24         -                1/1/40        -

C         [0/0]        -

30.0.3.1/32         -                1/1/40        -

L         [0/0]        -

30.0.4.0/24         30.0.3.2         1/1/40        -

O         [110/200]    01h:12m:46s

30.0.5.0/24         30.0.3.2         1/1/40        -

O         [110/150]    01h:12m:41s

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.1.1.0/24         -                vlan2011      -

C         [0/0]        -

20.1.1.2/32         -                vlan2011      -

L         [0/0]        -

20.3.1.0/24         -                vlan2031      -

C         [0/0]        -

20.3.1.2/32         -                vlan2031      -

L         [0/0]        -

101.0.0.0/24        20.3.1.1         vlan2031      -

B/E       [20/0]       01h:11m:55s

                    20.1.1.1         vlan2011

-                           [20/0]       01h:11m:55s

201.0.0.0/24        3.3.3.3          1/1/40        default
B/V       [200/0]      01h:10m:34s

VRF: vrf_2

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.1.1.0/24         -                vlan2012      -

C         [0/0]        -

20.1.1.2/32         -                vlan2012      -

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 91

L         [0/0]        -

20.3.1.0/24         -                vlan2032      -

C         [0/0]        -

20.3.1.2/32         -                vlan2032      -

L         [0/0]        -

102.0.0.0/24        20.3.1.1         vlan2032      -

B/E       [20/0]       00h:54m:06s

                    20.1.1.1         vlan2012

-                           [20/0]       00h:54m:06s

202.0.0.0/24        3.3.3.3          1/1/40        default

B/V       [200/0]      00h:54m:06s

Total Route Count : 25

PE2 configuration

PE2# show running

Current configuration:

!

!Version ArubaOS-CX LL.10.09.0001BF

!export-password: default

hostname PE2

profile core-spine

logging console severity crit

vrf vrf_1

    rd 1:1

    l3vpn-only

    address-family ipv4 unicast

        route-target export 1:1

        route-target import 1:1

    exit-address-family

vrf vrf_2

    rd 2:1
    l3vpn-only

    address-family ipv4 unicast

        route-target export 2:1

        route-target import 2:1

    exit-address-family

cli-session

    timeout 0

!

!

!

!

!

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 92

!

ssh server vrf mgmt

vlan 1,2021-2022,2041-2042

interface mgmt

    no shutdown

    ip dhcp

interface 1/1/43

    no shutdown

    mtu 9000

    description Towards CE1

    no routing

    vlan trunk native 1

    vlan trunk allowed 2021-2022

interface 1/1/44

    no shutdown

    mtu 9000

    description Towards CE2

    no routing

    vlan trunk native 1

    vlan trunk allowed 2041-2042

interface 1/1/45

    no shutdown

    mtu 9198

    description Towards P1

    ip mtu 9198

    ip address 30.0.1.1/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/46

    no shutdown

    mtu 9198
    description Towards P2

    ip mtu 9198

    ip address 30.0.4.1/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface loopback 0

    ip address 2.2.2.2/32

    ip ospf 1 area 0.0.0.0

interface vlan 2021

    vrf attach vrf_1

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 93

description Towards CE1

    ip mtu 9000

    ip address 20.2.1.2/24

interface vlan 2022

    vrf attach vrf_2

    description Towards CE1

    ip mtu 9000

    ip address 20.2.1.2/24

interface vlan 2041

    vrf attach vrf_1

    description Towards CE2

    ip mtu 9000

    ip address 20.4.1.2/24

interface vlan 2042

    vrf attach vrf_2

    description Towards CE2

    ip mtu 9000

    ip address 20.4.1.2/24

!

ip community-list standard site1_community description

For_setting_community_From_Site1

ip community-list standard site1_community seq 10 permit 99:99

!

!

!

route-map rmap1 permit seq 10

     description For_setting_community_For Site1_Received_EBGP_routes

     set community 99:99

route-map rmap2 deny seq 10

     description For_Denying_routes_with_Site1_community_To_EBGP_Peer

     match community-list site1_community

route-map rmap2 permit seq 20
     description For_Allowing_all_other_route

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 4.4.4.4 remote-as 6488163

    neighbor 4.4.4.4 description Towards RR1{P1}

    neighbor 4.4.4.4 update-source loopback 0

    neighbor 5.5.5.5 remote-as 6488163

    neighbor 5.5.5.5 description Towards RR2{P2}

    neighbor 5.5.5.5 update-source loopback 0

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 94

address-family vpnv4 unicast

        neighbor 4.4.4.4 activate

        neighbor 4.4.4.4 send-community both

        neighbor 5.5.5.5 activate

        neighbor 5.5.5.5 send-community both

    exit-address-family

!

    vrf vrf_1

        neighbor 20.2.1.1 remote-as 100

        neighbor 20.2.1.1 description Towards CE1

        neighbor 20.4.1.1 remote-as 100

        neighbor 20.4.1.1 description Towards CE2

        address-family ipv4 unicast

            neighbor 20.2.1.1 activate

            neighbor 20.2.1.1 route-map rmap1 in

            neighbor 20.2.1.1 route-map rmap2 out

            neighbor 20.2.1.1 send-community both

            neighbor 20.2.1.1 soft-reconfiguration inbound

            neighbor 20.4.1.1 activate

            neighbor 20.4.1.1 route-map rmap1 in

            neighbor 20.4.1.1 route-map rmap2 out

            neighbor 20.4.1.1 send-community both

            neighbor 20.4.1.1 soft-reconfiguration inbound

        exit-address-family

!

    vrf vrf_2

        neighbor 20.2.1.1 remote-as 100

        neighbor 20.2.1.1 description Towards CE1

        neighbor 20.4.1.1 remote-as 100

        neighbor 20.4.1.1 description Towards CE2

        address-family ipv4 unicast

            neighbor 20.2.1.1 activate
            neighbor 20.2.1.1 route-map rmap1 in

            neighbor 20.2.1.1 route-map rmap2 out

            neighbor 20.2.1.1 send-community both

            neighbor 20.2.1.1 soft-reconfiguration inbound

            neighbor 20.4.1.1 activate

            neighbor 20.4.1.1 route-map rmap1 in

            neighbor 20.4.1.1 route-map rmap2 out

            neighbor 20.4.1.1 send-community both

            neighbor 20.4.1.1 soft-reconfiguration inbound

        exit-address-family

!

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 95

https-server vrf mgmt

mpls

    enable

    label-protocol ldp

        enable

        router-id loopback0

PE2# show ip ospf neighbors

VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 2

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

4.4.4.4          1         FULL/DR           30.0.1.2           1/1/45

5.5.5.5          1         FULL/BDR          30.0.4.2           1/1/46

PE2#  show mpls ldp neighbor

Local LDP Identifier: 2.2.2.2:0, Peer LDP Identifier: 4.4.4.4:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:36

    State: operational

    LDP Discovery Sources: 1/1/45

    Addresses bound to this peer:

         30.0.0.2 30.0.1.2 30.0.2.1 4.4.4.4

Local LDP Identifier: 2.2.2.2:0, Peer LDP Identifier: 5.5.5.5:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:14

    State: operational

    LDP Discovery Sources: 1/1/46

    Addresses bound to this peer:

         30.0.3.2 30.0.4.2 30.0.5.1 5.5.5.5

PE2# show mpls ldp binding
30.0.3.2/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

4.4.4.4/32

        local binding: label: 17

        remote binding: lsr:5.5.5.5:0 label:17

        remote binding: lsr:4.4.4.4:0 label: exp-null

30.0.4.2/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

3.3.3.3/32

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 96

local binding: label: 19

        remote binding: lsr:5.5.5.5:0 label:19

        remote binding: lsr:4.4.4.4:0 label:19

5.5.5.5/32

        local binding: label: 18

        remote binding: lsr:5.5.5.5:0 label: exp-null

        remote binding: lsr:4.4.4.4:0 label:17

30.0.1.1/32

        local binding: label: exp-null

        No remote binding

30.0.1.2/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

30.0.4.1/32

        local binding: label: exp-null

        No remote binding

1.1.1.1/32

        local binding: label: 16

        remote binding: lsr:5.5.5.5:0 label:16

        remote binding: lsr:4.4.4.4:0 label:16

30.0.0.2/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

2.2.2.2/32

        local binding: label: exp-null

        remote binding: lsr:5.5.5.5:0 label:18

        remote binding: lsr:4.4.4.4:0 label:18

30.0.5.1/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

30.0.2.1/32

        No local binding
        remote binding: lsr:4.4.4.4:0 label: exp-null

PE2# show mpls forwarding

MPLS Bindings

Entry Bindings   : 8

Exit Bindings    : 4

Transit Bindings : 6

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix       Ingress  Nexthop    Outgoing  Egress     Egress   Status

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 97

VRF      Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    1.1.1.1/32   default  30.0.1.2   16        1/1/45     default

operational

LDP    1.1.1.1/32   default  30.0.4.2   16        1/1/46     default

operational

LDP    3.3.3.3/32   default  30.0.4.2   19        1/1/46     default

operational

LDP    3.3.3.3/32   default  30.0.1.2   19        1/1/45     default

operational

BGP    201.0.0.0/24 vrf_1    3.3.3.3    21        1/1/46     default

operational

BGP    202.0.0.0/24 vrf_2    3.3.3.3    22        1/1/46     default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  20        vrf_1

operational

BGP      n/a                 imp-null  22        vrf_2

operational

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address
Label

----------------------------------------------------------------------------

-----

LDP     4.4.4.4/32   16        1/1/39     default  30.0.0.2  exp-null

operational

LDP     1.1.1.1/32   16        1/1/45     default  30.0.1.2  16

operational

LDP     1.1.1.1/32   16        1/1/46     default  30.0.4.2  16

operational

LDP     4.4.4.4/32   17        1/1/45     default  30.0.1.2  exp-null

operational

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 98

LDP     5.5.5.5/32   18        1/1/46     default  30.0.4.2  exp-null

operational

LDP     3.3.3.3/32   19        1/1/45     default  30.0.1.2  19

operational

LDP     3.3.3.3/32   19        1/1/46     default  30.0.4.2  19

operational

PE2# show bgp vpnv4 un neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 4.4.4.4 (Internal)

    Description         : Towards RR1{P1}

    Peer-group          :

    Remote Router Id    : 4.4.4.4            Local Router Id    : 2.2.2.2

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 44703

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:21s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No
    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      3        5

    Keepalives                  18       17

    Route Refresh                0        0

    Total                       22       23

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 99

Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 5.5.5.5 (Internal)

    Description         : Towards RR2{P2}

    Peer-group          :

    Remote Router Id    : 5.5.5.5            Local Router Id    : 2.2.2.2

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 33107              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:15m:30s        Connect-Retry Time : 120
    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 100

Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      3        5

    Keepalives                  17       17

    Route Refresh                0        0

    Total                       21       23

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE2# show bgp vpnv4 unicast
Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 2.2.2.2

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>  101.0.0.0/24       0.0.0.0         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 101

Route Distinguisher: 2:1                  (Label 22)

*>  102.0.0.0/24       0.0.0.0         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 10

PE2#  show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 2.2.2.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast

------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 4.4.4.4         6488163     40      37      00h:26m:53s  Established   Up

 5.5.5.5         6488163     41      35      00h:27m:02s  Established   Up

Address-family : L2VPN EVPN

-----------------------------

VRF : vrf_1
BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.4.1.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.2.1.1        100         35      35      00h:28m:01s  Established   Up

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 102

20.4.1.1        100         35      35      00h:27m:58s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

VRF : vrf_2

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.4.1.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.2.1.1        100         38      38      00h:27m:57s  Established   Up

 20.4.1.1        100         38      37      00h:27m:56s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

PE2# show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 2.2.2.2

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path
Total number of entries 0

Address-family : VPNv4 Unicast

------------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>  101.0.0.0/24       0.0.0.0         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>  102.0.0.0/24       0.0.0.0         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 103

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 201.0.0.0/24       3.3.3.3         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

* i 202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 10

Address-family : L2VPN EVPN

-----------------------------

     Network                                               Nexthop

Metric     LocPrf    Weight   Path

----------------------------------------------------------------------------

--------------------------------

Total number of entries 0

VRF : vrf_1

Local Router-ID 20.4.1.2

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*=e 101.0.0.0/24       20.2.1.1        0          100        0       100 i

*>e 101.0.0.0/24       20.4.1.1        0          100        0       100 i

*>  201.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 3

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

VRF : vrf_2

Local Router-ID 20.4.1.2

Address-family : IPv4 Unicast

-----------------------------
    Network            Nexthop         Metric     LocPrf     Weight Path

*=e 102.0.0.0/24       20.2.1.1        0          100        0       100 i

*>e 102.0.0.0/24       20.4.1.1        0          100        0       100 i

*>  202.0.0.0/24       3.3.3.3         0          100        0       100 i

Total number of entries 3

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

PE2# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 104

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          30.0.1.2         1/1/45        -

O         [110/200]    01h:12m:16s

                    30.0.4.2         1/1/46

-                           [110/200]    01h:12m:16s

2.2.2.2/32          -                loopback0     -

L         [0/0]        -

3.3.3.3/32          30.0.1.2         1/1/45        -

O         [110/150]    01h:11m:52s

                    30.0.4.2         1/1/46

-                           [110/150]    01h:11m:52s

4.4.4.4/32          30.0.1.2         1/1/45        -

O         [110/100]    01h:12m:33s

5.5.5.5/32          30.0.4.2         1/1/46        -

O         [110/100]    01h:12m:16s

30.0.0.0/24         30.0.1.2         1/1/45        -

O         [110/200]    01h:12m:33s

30.0.1.0/24         -                1/1/45        -

C         [0/0]        -

30.0.1.1/32         -                1/1/45        -

L         [0/0]        -
30.0.2.0/24         30.0.1.2         1/1/45        -

O         [110/150]    01h:12m:33s

30.0.3.0/24         30.0.4.2         1/1/46        -

O         [110/200]    01h:12m:16s

30.0.4.0/24         -                1/1/46        -

C         [0/0]        -

30.0.4.1/32         -                1/1/46        -

L         [0/0]        -

30.0.5.0/24         30.0.4.2         1/1/46        -

O         [110/150]    01h:12m:16s

VRF: vrf_1

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 105

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.2.1.0/24         -                vlan2021      -

C         [0/0]        -

20.2.1.2/32         -                vlan2021      -

L         [0/0]        -

20.4.1.0/24         -                vlan2041      -

C         [0/0]        -

20.4.1.2/32         -                vlan2041      -

L         [0/0]        -

101.0.0.0/24        20.4.1.1         vlan2041      -

B/E       [20/0]       01h:11m:55s

                    20.2.1.1         vlan2021

-                           [20/0]       01h:11m:55s

201.0.0.0/24        3.3.3.3          1/1/46        default

B/V       [200/0]      01h:10m:34s

VRF: vrf_2

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.2.1.0/24         -                vlan2022      -

C         [0/0]        -

20.2.1.2/32         -                vlan2022      -

L         [0/0]        -

20.4.1.0/24         -                vlan2042      -
C         [0/0]        -

20.4.1.2/32         -                vlan2042      -

L         [0/0]        -

102.0.0.0/24        20.4.1.1         vlan2042      -

B/E       [20/0]       00h:54m:06s

                    20.2.1.1         vlan2022

-                           [20/0]       00h:54m:06s

202.0.0.0/24        3.3.3.3          1/1/46        default

B/V       [200/0]      00h:54m:06s

Total Route Count : 25

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 106

PE3 configuration

PE3# show running

Current configuration:

!

!Version ArubaOS-CX LL.10.09.0001BF

!export-password: default

hostname PE3

profile core-spine

logging console severity crit

vrf vrf_1

    rd 1:3

    l3vpn-only

    address-family ipv4 unicast

        route-target export 1:1

        route-target import 1:1

    exit-address-family

vrf vrf_2

    rd 2:3

    l3vpn-only

    address-family ipv4 unicast

        route-target export 2:1

        route-target import 2:1

    exit-address-family

cli-session

    timeout 0

!

!

!

!

!

!
ssh server vrf mgmt

vlan 1,2051-2052

interface mgmt

    no shutdown

    ip dhcp

system interface-group 1 speed 10g

    !interface group 1 contains ports 1/1/1-1/1/4

interface lag 99

    no shutdown

    description Towards P1

    ip mtu 9198

    ip address 30.0.2.2/24

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 107

lacp mode active

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface lag 100

    no shutdown

    description Towards P2

    ip mtu 9198

    ip address 30.0.5.2/24

    lacp mode active

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface 1/1/19

    no shutdown

    mtu 9198

    description Towards P1

    lag 99

interface 1/1/20

    no shutdown

    mtu 9198

    description Towards P1

    lag 99

interface 1/1/21

    no shutdown

    mtu 9000

    description Towards CE3

    no routing

    vlan trunk native 1

    vlan trunk allowed 2051-2052

interface 1/1/22

    no shutdown
    mtu 9198

    description Towards P2

    lag 100

interface 1/1/23

    no shutdown

    mtu 9198

    description Towards P2

    lag 100

interface loopback 0

    ip address 3.3.3.3/32

    ip ospf 1 area 0.0.0.0

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 108

interface vlan 2051

    vrf attach vrf_1

    description Towards CE3

    ip mtu 9000

    ip address 20.5.1.1/24

interface vlan 2052

    vrf attach vrf_2

    description Towards CE3

    ip mtu 9000

    ip address 20.5.1.1/24

!

!

!

!

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 4.4.4.4 remote-as 6488163

    neighbor 4.4.4.4 description Towards RR1{P1}

    neighbor 4.4.4.4 update-source loopback 0

    neighbor 5.5.5.5 remote-as 6488163

    neighbor 5.5.5.5 description Towards RR2{P2}

    neighbor 5.5.5.5 update-source loopback 0

    address-family vpnv4 unicast

        neighbor 4.4.4.4 activate

        neighbor 4.4.4.4 send-community both

        neighbor 5.5.5.5 activate

        neighbor 5.5.5.5 send-community both

    exit-address-family

!

    vrf vrf_1
        neighbor 20.5.1.2 remote-as 100

        neighbor 20.5.1.2 description Towards CE3

        address-family ipv4 unicast

            neighbor 20.5.1.2 activate

            neighbor 20.5.1.2 send-community both

            neighbor 20.5.1.2 soft-reconfiguration inbound

        exit-address-family

!

    vrf vrf_2

        neighbor 20.5.1.2 remote-as 100

        neighbor 20.5.1.2 description Towards CE3

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 109

address-family ipv4 unicast

            neighbor 20.5.1.2 activate

            neighbor 20.5.1.2 send-community both

            neighbor 20.5.1.2 soft-reconfiguration inbound

        exit-address-family

!

https-server vrf mgmt

mpls

    enable

    label-protocol ldp

        enable

        router-id loopback0

PE3 verification

PE3# show ip ospf neighbors

VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 2

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

5.5.5.5          1         FULL/DR           30.0.5.1           lag100

4.4.4.4          1         FULL/DR           30.0.2.1           lag99

PE3#  show mpls ldp neighbor

Local LDP Identifier: 3.3.3.3:0, Peer LDP Identifier: 4.4.4.4:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:12:42

    State: operational

    LDP Discovery Sources: lag99

    Addresses bound to this peer:

         30.0.0.2 30.0.1.2 30.0.2.1 4.4.4.4
Local LDP Identifier: 3.3.3.3:0, Peer LDP Identifier: 5.5.5.5:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:12:42

    State: operational

    LDP Discovery Sources: lag100

    Addresses bound to this peer:

         30.0.3.2 30.0.4.2 30.0.5.1 5.5.5.5

PE3#  show mpls ldp binding

30.0.5.2/32

        local binding: label: exp-null

        No remote binding

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 110

2.2.2.2/32

        local binding: label: 17

        remote binding: lsr:5.5.5.5:0 label:18

        remote binding: lsr:4.4.4.4:0 label:18

30.0.1.2/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

4.4.4.4/32

        local binding: label: 18

        remote binding: lsr:5.5.5.5:0 label:17

        remote binding: lsr:4.4.4.4:0 label: exp-null

30.0.4.2/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

30.0.5.1/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

30.0.3.2/32

        No local binding

        remote binding: lsr:5.5.5.5:0 label: exp-null

30.0.2.2/32

        local binding: label: exp-null

        No remote binding

30.0.0.2/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

1.1.1.1/32

        local binding: label: 16

        remote binding: lsr:5.5.5.5:0 label:16

        remote binding: lsr:4.4.4.4:0 label:16

5.5.5.5/32

        local binding: label: 19
        remote binding: lsr:5.5.5.5:0 label: exp-null

        remote binding: lsr:4.4.4.4:0 label:17

3.3.3.3/32

        local binding: label: exp-null

        remote binding: lsr:5.5.5.5:0 label:19

        remote binding: lsr:4.4.4.4:0 label:19

30.0.2.1/32

        No local binding

        remote binding: lsr:4.4.4.4:0 label: exp-null

PE3# show mpls forwarding

MPLS Bindings

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 111

Entry Bindings   : 8

Exit Bindings    : 4

Transit Bindings : 6

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix       Ingress  Nexthop    Outgoing  Egress     Egress   Status

                    VRF      Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    1.1.1.1/32   default  30.0.5.1   16        lag100     default

operational

LDP    1.1.1.1/32   default  30.0.2.1   16        lag99      default

operational

LDP    2.2.2.2/32   default  30.0.2.1   18        lag99      default

operational

LDP    2.2.2.2/32   default  30.0.5.1   18        lag100     default

operational

BGP    101.0.0.0/24 vrf_1    1.1.1.1    20        lag100     default

operational

BGP    102.0.0.0/24 vrf_2    1.1.1.1    22        lag100     default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  21        vrf_1

operational
BGP      n/a                 imp-null  22        vrf_2

operational

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

---

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 112

LDP     1.1.1.1/32   16        lag100     default  30.0.5.1  16

operational

LDP     1.1.1.1/32   16        lag99      default  30.0.2.1  16

operational

LDP     2.2.2.2/32   17        lag100     default  30.0.5.1  18

operational

LDP     2.2.2.2/32   17        lag99      default  30.0.2.1  18

operational

LDP     4.4.4.4/32   18        lag99      default  30.0.2.1  exp-null

operational

LDP     5.5.5.5/32   19        lag100     default  30.0.5.1  exp-null

operational

PE3# show bgp vpnv4 un neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 4.4.4.4 (Internal)

    Description         : Towards RR1{P1}

    Peer-group          :

    Remote Router Id    : 4.4.4.4            Local Router Id    : 3.3.3.3

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 33231              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:14m:47s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error
    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 113

Updates                      3        3

    Keepalives                  17       18

    Route Refresh                0        0

    Total                       21       22

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 5.5.5.5 (Internal)

    Description         : Towards RR2{P2}

    Peer-group          :

    Remote Router Id    : 5.5.5.5            Local Router Id    : 3.3.3.3

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 39781              Local Port         : 179
    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:14m:45s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 114

Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      3        3

    Keepalives                  17       17

    Route Refresh                0        0

    Total                       21       21

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :
    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE3# show bgp vpnv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 115

Local Router-ID 3.3.3.3

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

*>  201.0.0.0/24       0.0.0.0         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>  202.0.0.0/24       0.0.0.0         0          100        0       100 i

Total number of entries 6

PE3# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 3.3.3.3

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast

------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 4.4.4.4         6488163     40      35      00h:26m:19s  Established   Up

 5.5.5.5         6488163     39      36      00h:26m:17s  Established   Up

Address-family : L2VPN EVPN
-----------------------------

VRF : vrf_1

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.5.1.1

 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 116

AdminStatus

 20.5.1.2        100         33      34      00h:25m:12s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

VRF : vrf_2

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.5.1.1

 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.5.1.2        100         34      34      00h:25m:11s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

PE3#  show bgp all-vrf all

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 3.3.3.3

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path
Total number of entries 0

Address-family : VPNv4 Unicast

------------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 20)

*>i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 101.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 2:1                  (Label 22)

*>i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

* i 102.0.0.0/24       1.1.1.1         0          100        0       100 i

Route Distinguisher: 1:3                  (Label 21)

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 117

*>  201.0.0.0/24       0.0.0.0         0          100        0       100 i

Route Distinguisher: 2:3                  (Label 22)

*>  202.0.0.0/24       0.0.0.0         0          100        0       100 i

Total number of entries 6

Address-family : L2VPN EVPN

-----------------------------

     Network                                               Nexthop

Metric     LocPrf    Weight   Path

----------------------------------------------------------------------------

--------------------------------

Total number of entries 0

VRF : vrf_1

Local Router-ID 20.5.1.1

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*>  101.0.0.0/24       1.1.1.1         0          100        0       100 i

*>e 201.0.0.0/24       20.5.1.2        0          100        0       100 i

Total number of entries 2

Address-family : IPv6 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

VRF : vrf_2

Local Router-ID 20.5.1.1

Address-family : IPv4 Unicast

-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

*>  102.0.0.0/24       1.1.1.1         0          100        0       100 i

*>e 202.0.0.0/24       20.5.1.2        0          100        0       100 i

Total number of entries 2

Address-family : IPv6 Unicast
-----------------------------

    Network            Nexthop         Metric     LocPrf     Weight Path

Total number of entries 0

PE3# show ip route all-vrf

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 118

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          30.0.5.1         lag100        -

O         [110/150]    01h:11m:56s

                    30.0.2.1         lag99

-                           [110/150]    01h:11m:56s

2.2.2.2/32          30.0.5.1         lag100        -

O         [110/150]    01h:11m:56s

                    30.0.2.1         lag99

-                           [110/150]    01h:11m:56s

3.3.3.3/32          -                loopback0     -

L         [0/0]        -

4.4.4.4/32          30.0.2.1         lag99         -

O         [110/50]     01h:11m:57s

5.5.5.5/32          30.0.5.1         lag100        -

O         [110/50]     01h:11m:56s

30.0.0.0/24         30.0.2.1         lag99         -

O         [110/150]    01h:11m:57s

30.0.1.0/24         30.0.2.1         lag99         -

O         [110/150]    01h:11m:57s

30.0.2.0/24         -                lag99         -

C         [0/0]        -

30.0.2.2/32         -                lag99         -

L         [0/0]        -

30.0.3.0/24         30.0.5.1         lag100        -

O         [110/150]    01h:11m:56s

30.0.4.0/24         30.0.5.1         lag100        -

O         [110/150]    01h:11m:56s
30.0.5.0/24         -                lag100        -

C         [0/0]        -

30.0.5.2/32         -                lag100        -

L         [0/0]        -

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

Public

Use case 1: MPLS L3 VPN with dual homed VSX CE 119

20.5.1.0/24         -                vlan2051      -

C         [0/0]        -

20.5.1.1/32         -                vlan2051      -

L         [0/0]        -

101.0.0.0/24        1.1.1.1          lag100        default

B/V       [200/0]      01h:11m:49s

201.0.0.0/24        20.5.1.2         vlan2051      -

B/E       [20/0]       01h:10m:34s

VRF: vrf_2

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

20.5.1.0/24         -                vlan2052      -

C         [0/0]        -

20.5.1.1/32         -                vlan2052      -

L         [0/0]        -

102.0.0.0/24        1.1.1.1          lag100        default

B/V       [200/0]      00h:54m:06s

202.0.0.0/24        20.5.1.2         vlan2052      -

B/E       [20/0]       00h:54m:06s

Total Route Count : 21

Use case 2: MPLS L3 VPN with hub and spoke VRFs

This use case covers:

•  An MPLS L3 VPN network with a shared hub VRF that has connectivity to spoke VRFs, while spoke

VRFs that are isolated between each other

•  CEs in hub VRF are expected to provide hub connectivity between CE spoke subnets (101.0.0.0/24 and

201.0.0.0/24) and hub subnets (151.0.0.0/24 and 0.0.0.0/0 default route)

•  PE3 should not allow direct spoke to spoke connectivity, this is achieved through:

◦  Using hub_import VRF to advertise spoke CE subnets from PE1/PE2 to CE3

◦  Using hub_export VRF to advertise hub and spoke CE subnets from CE4 to PE1/PE2

•  Sample configurations

•  Relevant verification commands

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 120

MPLS L3 VPN with hub and spoke VRFs:

CE1 Configuration

CE1# show run

Current configuration:

!

!Version ArubaOS-CX TL.10.09.0001AX

!export-password: default

hostname CE1

profile l3-core

logging console severity crit

cli-session

    timeout 0

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2001,2071

interface mgmt
    no shutdown

    ip dhcp

interface 1/1/43

    no shutdown

    description Towards 101 subnet

    no routing

    vlan trunk native 1

    vlan trunk allowed 2071

interface 1/1/44

    no shutdown

    description Towards PE1

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 121

no routing

    vlan trunk native 1

    vlan trunk allowed 2001

interface vlan 2001

    description Towards PE1

    ip address 20.0.1.1/24

interface vlan 2071

    description Towards 101 subnet

    ip address 20.7.1.2/24

    ip ospf 1 area 0.0.0.0

!

!

!

!

!

router ospf 1

    area 0.0.0.0

router bgp 100

    neighbor 20.0.1.2 remote-as 6488163

    neighbor 20.0.1.2 description Towards PE1

    neighbor 20.7.1.1 remote-as 100

    neighbor 20.7.1.1 description Towards 101 subnet

    address-family ipv4 unicast

        neighbor 20.0.1.2 activate

        neighbor 20.0.1.2 send-community both

        neighbor 20.0.1.2 soft-reconfiguration inbound

        neighbor 20.7.1.1 activate

        neighbor 20.7.1.1 next-hop-self

    exit-address-family

!

https-server vrf mgmt

CE1 Verification

CE1# show bgp ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 20.0.1.2 (External)

    Description         : Towards PE1

    Peer-group          :
    Remote Router Id    : 20.0.1.2           Local Router Id    : 20.7.1.2

    Remote AS           : 6488163            Local AS           : 100

    Remote Port         : 57770              Local Port         : 179

    State               : Established        Admin Status       : Up

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 122

Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:23m:45s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      2        9

    Keepalives                  27       23

    Route Refresh                0        0

    Total                       30       33

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          Yes             Yes
    Address family IPv6 Unicast          No              No

    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 128000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 123

ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 20.7.1.1 (Internal)

    Description         : Towards Ixia1-SPOKE1

    Peer-group          :

    Remote Router Id    : 196.0.0.1          Local Router Id    : 20.7.1.2

    Remote AS           : 100                Local AS           : 100

    Remote Port         : 32802              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 90                 Neg. Keep Alive    : 30

    Up/Down Time        : 00h:20m:28s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      8        1

    Keepalives                  45       42
    Route Refresh                0        0

    Total                       54       44

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             No

    Add-Path                             No              No

    Four Octet ASN                       Yes             No

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              Yes

    Address Family : IPv4 Unicast

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 124

-----------------------------

    Rt. Reflect. Client : No                  Send Community    :

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 128000              Soft Reconfig In  :

    Nexthop-Self        : Yes                 Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

CE1# show bgp ipv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 20.7.1.2

    Network            Nexthop         Metric     LocPrf     Weight Path

*>e 0.0.0.0/0          20.0.1.2        0          100        0

6488163 102 ?

*>e 20.4.1.0/24        20.0.1.2        0          100        0

6488163 102 ?

*>e 20.5.1.0/24        20.0.1.2        0          100        0

6488163 102 ?

*>e 20.6.1.0/24        20.0.1.2        0          100        0

6488163 102 ?

*>i 101.0.0.0/24       20.7.1.1        0          100        0       i

*>e 151.0.0.0/24       20.0.1.2        0          100        0

6488163 102 ?

*>e 201.0.0.0/24       20.0.1.2        0          100        0

6488163 102 ?
Total number of entries 7

CE1#

CE1# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 20.7.1.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 125

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.0.1.2        6488163     40      37      00h:29m:45s  Established   Up

 20.7.1.1        100         56      68      00h:26m:28s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

CE1#

CE1# show ip route all-vrfs

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           20.0.1.2         vlan2001      -

B/E       [20/0]       00h:23m:22s

20.0.1.0/24         -                vlan2001      -

C         [0/0]        -

20.0.1.1/32         -                vlan2001      -

L         [0/0]        -

20.4.1.0/24         20.0.1.2         vlan2001      -

B/E       [20/0]       00h:29m:54s

20.5.1.0/24         20.0.1.2         vlan2001      -

B/E       [20/0]       00h:30m:36s
20.6.1.0/24         20.0.1.2         vlan2001      -

B/E       [20/0]       00h:24m:12s

20.7.1.0/24         -                vlan2071      -

C         [0/0]        -

20.7.1.2/32         -                vlan2071      -

L         [0/0]        -

101.0.0.0/24        20.7.1.1         vlan2071      -

B/I       [200/0]      00h:28m:22s

151.0.0.0/24        20.0.1.2         vlan2001      -

B/E       [20/0]       00h:23m:22s

201.0.0.0/24        20.0.1.2         vlan2001      -

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 126

B/E       [20/0]       00h:28m:22s

Total Route Count : 11

CE2 Configuration

CE2# show run

Current configuration:

!

!Version ArubaOS-CX TL.10.09.0001AX

!export-password: default

hostname CE2

profile l3-core

logging console severity crit

cli-session

    timeout 0

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2011,2081

interface mgmt

    no shutdown

    ip dhcp

interface 1/1/1

    no shutdown

    description Towards 201 subnet

    no routing

    vlan trunk native 1

    vlan trunk allowed 2081

interface 1/1/2

    no shutdown

    description Towards PE2

    no routing

    vlan trunk native 1

    vlan trunk allowed 2011

interface vlan 2011

    description Towards PE2

    ip address 20.1.1.1/24

interface vlan 2081

    description Towards 201 subnet

    ip address 20.8.1.2/24

    ip ospf 1 area 0.0.0.0

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 127

!

!

!

!

!

router ospf 1

    area 0.0.0.0

router bgp 101

    neighbor 20.1.1.2 remote-as 6488163

    neighbor 20.1.1.2 description Towards PE2

    neighbor 20.8.1.1 remote-as 101

    neighbor 20.8.1.1 description Towards 201 subnet

    address-family ipv4 unicast

        neighbor 20.1.1.2 activate

        neighbor 20.1.1.2 send-community both

        neighbor 20.1.1.2 soft-reconfiguration inbound

        neighbor 20.8.1.1 activate

        neighbor 20.8.1.1 next-hop-self

    exit-address-family

!

https-server vrf mgmt

CE2 Verification

CE2# show bgp ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 20.1.1.2 (External)

    Description         : Towards PE2

    Peer-group          :

    Remote Router Id    : 20.1.1.2           Local Router Id    : 20.8.1.2

    Remote AS           : 6488163            Local AS           : 101

    Remote Port         : 60400              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:23m:27s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 128

Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      2        9

    Keepalives                  26       22

    Route Refresh                0        0

    Total                       29       32

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              No

    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 128000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :
    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 20.8.1.1 (Internal)

    Description         : Towards Ixia2-SPOKE2

    Peer-group          :

    Remote Router Id    : 195.0.0.1          Local Router Id    : 20.8.1.2

    Remote AS           : 101                Local AS           : 101

    Remote Port         : 32798              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 129

Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 90                 Neg. Keep Alive    : 30

    Up/Down Time        : 00h:20m:27s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      8        1

    Keepalives                  44       42

    Route Refresh                0        0

    Total                       53       44

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             No

    Add-Path                             No              No

    Four Octet ASN                       Yes             No

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              Yes
    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    :

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 128000              Soft Reconfig In  :

    Nexthop-Self        : Yes                 Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 130

ORF capability      :

CE2# show bgp ipv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 20.8.1.2

    Network            Nexthop         Metric     LocPrf     Weight Path

*>e 0.0.0.0/0          20.1.1.2        0          100        0

6488163 102 ?

*>e 20.4.1.0/24        20.1.1.2        0          100        0

6488163 102 ?

*>e 20.5.1.0/24        20.1.1.2        0          100        0

6488163 102 ?

*>e 20.6.1.0/24        20.1.1.2        0          100        0

6488163 102 ?

*>e 101.0.0.0/24       20.1.1.2        0          100        0

6488163 102 ?

*>e 151.0.0.0/24       20.1.1.2        0          100        0

6488163 102 ?

*>i 201.0.0.0/24       20.8.1.1        0          100        0       i

Total number of entries 7

CE2#

CE2# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 101          BGP Router Identifier  : 20.8.1.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0
Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.1.1.2        6488163     39      36      00h:29m:27s  Established   Up

 20.8.1.1        101         56      67      00h:26m:28s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

CE2#

CE2# show ip route all-vrfs

Displaying ipv4 routes selected for forwarding

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 131

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           20.1.1.2         vlan2011      -

B/E       [20/0]       00h:23m:22s

20.1.1.0/24         -                vlan2011      -

C         [0/0]        -

20.1.1.1/32         -                vlan2011      -

L         [0/0]        -

20.4.1.0/24         20.1.1.2         vlan2011      -

B/E       [20/0]       00h:29m:54s

20.5.1.0/24         20.1.1.2         vlan2011      -

B/E       [20/0]       00h:30m:36s

20.6.1.0/24         20.1.1.2         vlan2011      -

B/E       [20/0]       00h:24m:12s

20.8.1.0/24         -                vlan2081      -

C         [0/0]        -

20.8.1.2/32         -                vlan2081      -

L         [0/0]        -

101.0.0.0/24        20.1.1.2         vlan2011      -

B/E       [20/0]       00h:28m:22s

151.0.0.0/24        20.1.1.2         vlan2011      -

B/E       [20/0]       00h:23m:22s
201.0.0.0/24        20.8.1.1         vlan2081      -

B/I       [200/0]      00h:28m:22s

Total Route Count : 11

CE3 Configuration

CE3# show run

Current configuration:
!

!Version ArubaOS-CX TL.10.09.0001AX

!export-password: default

hostname CE3

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 132

profile l3-core

logging console severity crit

cli-session

    timeout 0

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2021,2041

interface mgmt

    no shutdown

    ip dhcp

interface 1/1/1

    no shutdown

    description Towards PE3

    no routing

    vlan trunk native 1

    vlan trunk allowed 2021

interface 1/1/2

    no shutdown

    description Towards 151 and default subnet

    no routing

    vlan trunk native 1

    vlan trunk allowed 2041

interface vlan 2021

    description Towards PE3

    ip address 20.2.1.2/24

interface vlan 2041

    description Towards 151 and default subnet

    ip address 20.4.1.1/24
    ip ospf 1 area 0.0.0.0

!

!

!

!

!

router ospf 1

    redistribute bgp

    area 0.0.0.0

router bgp 102

    neighbor 20.2.1.1 remote-as 6488163

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 133

neighbor 20.2.1.1 description Towards PE3

    address-family ipv4 unicast

        neighbor 20.2.1.1 activate

        neighbor 20.2.1.1 send-community both

        neighbor 20.2.1.1 soft-reconfiguration inbound

        redistribute ospf

    exit-address-family

!

https-server vrf mgmt

CE3#

CE3# show ip ospf neighbors

VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 1

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

20.4.1.2         1         FULL/BDR          20.4.1.2           vlan2041

CE3 Verification

CE3# show bgp ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 20.2.1.1 (External)

    Description         : Towards PE3

    Peer-group          :

    Remote Router Id    : 20.2.1.1           Local Router Id    : 20.4.1.1

    Remote AS           : 6488163            Local AS           : 102

    Remote Port         : 179                Local Port         : 48554

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:23m:06s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 134

TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      8        3

    Keepalives                  23       27

    Route Refresh                0        0

    Total                       32       31

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              No

    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 5                   Advt. Interval    : 30

    Max. Prefix         : 128000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

CE3# show bgp ipv4 unicast
Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 20.4.1.1

    Network            Nexthop         Metric     LocPrf     Weight Path

*>  0.0.0.0/0          20.4.1.2        0          100        0       ?

*>  20.4.1.0/24        0.0.0.0         0          100        0       ?

*>  20.5.1.0/24        20.4.1.2        0          100        0       ?

*>  20.6.1.0/24        20.4.1.2        0          100        0       ?

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 135

*>e 101.0.0.0/24       20.2.1.1        0          100        0

6488163 100 i

*>  151.0.0.0/24       20.4.1.2        0          100        0       ?

*>e 201.0.0.0/24       20.2.1.1        0          100        0

6488163 101 i

Total number of entries 7

CE3# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 102          BGP Router Identifier  : 20.4.1.1

 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.2.1.1        6488163     38      39      00h:29m:07s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

CE3# show ip route all-vrfs

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type
Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           20.4.1.2         vlan2041      -

O/IA      [110/200]    00h:23m:22s

20.2.1.0/24         -                vlan2021      -

C         [0/0]        -

20.2.1.2/32         -                vlan2021      -

L         [0/0]        -

20.4.1.0/24         -                vlan2041      -

C         [0/0]        -

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 136

20.4.1.1/32         -                vlan2041      -

L         [0/0]        -

20.5.1.0/24         20.4.1.2         vlan2041      -

O         [110/200]    00h:29m:54s

20.6.1.0/24         20.4.1.2         vlan2041      -

O         [110/200]    00h:24m:12s

101.0.0.0/24        20.2.1.1         vlan2021      -

B/E       [20/0]       00h:28m:23s

151.0.0.0/24        20.4.1.2         vlan2041      -

O/IA      [110/200]    00h:23m:22s

201.0.0.0/24        20.2.1.1         vlan2021      -

B/E       [20/0]       00h:28m:22s

Total Route Count : 10

CE4 Configuration

CE4# show run

Current configuration:

!

!Version ArubaOS-CX TL.10.09.0001AX

!export-password: default

hostname CE4

profile l3-core

logging console severity crit

cli-session

    timeout 0

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2031,2051

interface mgmt

    no shutdown

    ip dhcp

interface 1/1/1

    no shutdown

    description Towards PE3

    no routing

    vlan trunk native 1

    vlan trunk allowed 2031

interface 1/1/2

    no shutdown

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 137

description Towards 151 and default subnet

    no routing

    vlan trunk native 1

    vlan trunk allowed 2051

interface vlan 2031

    description Towards PE3

    ip address 20.3.1.2/24

interface vlan 2051

    description Towards 151 and default subnet

    ip address 20.5.1.1/24

    ip ospf 1 area 0.0.0.0

!

!

!

!

!

router ospf 1

    redistribute bgp

    area 0.0.0.0

router bgp 102

    neighbor 20.3.1.1 remote-as 6488163

    neighbor 20.3.1.1 description Towards PE3

    address-family ipv4 unicast

        neighbor 20.3.1.1 activate

        neighbor 20.3.1.1 send-community both

        neighbor 20.3.1.1 soft-reconfiguration inbound

        redistribute ospf

    exit-address-family

!

https-server vrf mgmt

CE4#

CE4# show ip ospf neighbors
VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 1

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

20.4.1.2         1         FULL/DR           20.5.1.2           vlan2051

CE4 Verification

CE4# show bgp ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : default

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 138

BGP Neighbor 20.3.1.1 (External)

    Description         : Towards PE3

    Peer-group          :

    Remote Router Id    : 20.3.1.1           Local Router Id    : 20.5.1.1

    Remote AS           : 6488163            Local AS           : 102

    Remote Port         : 52062              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:22m:47s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      9        1

    Keepalives                  22       26

    Route Refresh                0        0

    Total                       32       28
    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              No

    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 139

Allow-AS in         : 5                   Advt. Interval    : 30

    Max. Prefix         : 128000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

CE4#

CE4# show bgp ipv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 20.5.1.1

    Network            Nexthop         Metric     LocPrf     Weight Path

*>  0.0.0.0/0          20.5.1.2        0          100        0       ?

*>  20.4.1.0/24        20.5.1.2        0          100        0       ?

*>  20.5.1.0/24        0.0.0.0         0          100        0       ?

*>  20.6.1.0/24        20.5.1.2        0          100        0       ?

*>  101.0.0.0/24       20.5.1.2        0          100        0       ?

*>  151.0.0.0/24       20.5.1.2        0          100        0       ?

*>  201.0.0.0/24       20.5.1.2        0          100        0       ?

Total number of entries 7

CE4#

CE4# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 102          BGP Router Identifier  : 20.5.1.1
 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.3.1.1        6488163     35      39      00h:28m:48s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

CE4# show ip route all-vrfs

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 140

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           20.5.1.2         vlan2051      -

O/IA      [110/200]    00h:23m:22s

20.3.1.0/24         -                vlan2031      -

C         [0/0]        -

20.3.1.2/32         -                vlan2031      -

L         [0/0]        -

20.4.1.0/24         20.5.1.2         vlan2051      -

O         [110/200]    00h:29m:55s

20.5.1.0/24         -                vlan2051      -

C         [0/0]        -

20.5.1.1/32         -                vlan2051      -

L         [0/0]        -

20.6.1.0/24         20.5.1.2         vlan2051      -

O         [110/200]    00h:24m:12s

101.0.0.0/24        20.5.1.2         vlan2051      -

O/E2      [110/25]     00h:28m:22s

151.0.0.0/24        20.5.1.2         vlan2051      -

O/IA      [110/200]    00h:23m:22s

201.0.0.0/24        20.5.1.2         vlan2051      -
O/E2      [110/25]     00h:28m:22s

Total Route Count : 10

PE1 Configuration

PE1# show run

Current configuration:

!
!Version ArubaOS-CX LL.10.09.0001AX

!export-password: default

hostname PE1

profile core-spine

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 141

logging console severity crit

vrf spoke_1

    rd 1:1

    l3vpn-only

    address-family ipv4 unicast

        route-target export 1:1

        route-target import 1:0

    exit-address-family

cli-session

    timeout 0

!

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2001

interface mgmt

    no shutdown

    ip dhcp

interface 1/1/37

    no shutdown

    description Towards CE1

    no routing

    vlan trunk native 1

    vlan trunk allowed 2001

interface 1/1/38

    no shutdown

    mtu 9198

    description Towards P1

    ip address 30.0.1.1/24
    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface loopback 0

    ip address 1.1.1.1/32

    ip ospf 1 area 0.0.0.0

interface vlan 2001

    vrf attach spoke_1

    description Towards CE1

    ip address 20.0.1.2/24

!

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 142

!

!

!

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 2.2.2.2 remote-as 6488163

    neighbor 2.2.2.2 description Towards PE2-SPOKE2

    neighbor 2.2.2.2 update-source loopback 0

    neighbor 3.3.3.3 remote-as 6488163

    neighbor 3.3.3.3 description Towards PE3-HUB

    neighbor 3.3.3.3 update-source loopback 0

    address-family vpnv4 unicast

        neighbor 2.2.2.2 activate

        neighbor 2.2.2.2 send-community both

        neighbor 3.3.3.3 activate

        neighbor 3.3.3.3 send-community both

    exit-address-family

!

    vrf spoke_1

        neighbor 20.0.1.1 remote-as 100

        neighbor 20.0.1.1 description Towards CE1

        address-family ipv4 unicast

            neighbor 20.0.1.1 activate

            neighbor 20.0.1.1 send-community both

            neighbor 20.0.1.1 soft-reconfiguration inbound

        exit-address-family

!

https-server vrf mgmt

mpls

    enable
    label-protocol ldp

        enable

        router-id loopback0

PE1 Verification

PE1# show ip ospf neighbors

VRF : default                          Process : 1
===================================================

Total Number of Neighbors : 1

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 143

4.4.4.4          1         FULL/BDR          30.0.1.2           1/1/38

PE1# show mpls ldp neighbor

Local LDP Identifier: 1.1.1.1:0, Peer LDP Identifier: 4.4.4.4:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:17:58

    State: operational

    LDP Discovery Sources: 1/1/38

    Addresses bound to this peer:

         30.0.1.2 30.0.2.2 30.0.3.1 4.4.4.4

PE1# show mpls forwarding

MPLS Bindings

Entry Bindings   : 9

Exit Bindings    : 3

Transit Bindings : 3

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix       Ingress  Nexthop    Outgoing  Egress     Egress   Status

                    VRF      Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    2.2.2.2/32   default  30.0.1.2   17        1/1/38     default

operational

LDP    3.3.3.3/32   default  30.0.1.2   18        1/1/38     default

operational

BGP    0.0.0.0/0    spoke_1  3.3.3.3    19        1/1/38     default

operational

BGP    20.4.1.0/24  spoke_1  3.3.3.3    19        1/1/38     default

operational

BGP    20.5.1.0/24  spoke_1  3.3.3.3    19        1/1/38     default
operational

BGP    20.6.1.0/24  spoke_1  3.3.3.3    19        1/1/38     default

operational

BGP    151.0.0.0/24 spoke_1  3.3.3.3    19        1/1/38     default

operational

BGP    201.0.0.0/24 spoke_1  3.3.3.3    19        1/1/38     default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 144

---

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  19        spoke_1

operational

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

---

LDP     4.4.4.4/32   16        1/1/38     default  30.0.1.2  exp-null

operational

LDP     2.2.2.2/32   17        1/1/38     default  30.0.1.2  17

operational

LDP     3.3.3.3/32   18        1/1/38     default  30.0.1.2  18

operational

PE1# show bgp vpnv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 2.2.2.2 (Internal)

    Description         : Towards PE2-SPOKE2

    Peer-group          :

    Remote Router Id    : 2.2.2.2            Local Router Id    : 1.1.1.1

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 39729

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0
    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:19m:46s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 145

Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      2        2

    Keepalives                  22       22

    Route Refresh                0        0

    Total                       25       25

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :
    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 3.3.3.3 (Internal)

    Description         : Towards PE3-HUB

    Peer-group          :

    Remote Router Id    : 3.3.3.3            Local Router Id    : 1.1.1.1

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 43547              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 146

Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:19m:18s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      2        9

    Keepalives                  22       18

    Route Refresh                0        0

    Total                       25       28

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes
    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 147

ORF type            : Prefix-list

    ORF capability      :

PE1# show bgp vrf spoke_1 ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : spoke_1

BGP Neighbor 20.0.1.1 (External)

    Description         : Towards CE1

    Peer-group          :

    Remote Router Id    : 20.7.1.2           Local Router Id    : 20.0.1.2

    Remote AS           : 100                Local AS           : 6488163

    Remote Port         : 179                Local Port         : 57770

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:21m:38s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1
    Notification                 0        0

    Updates                      9        2

    Keepalives                  21       25

    Route Refresh                0        0

    Total                       31       28

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 148

Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         No              No

    Address family L2VPN EVPN            No              No

    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE1# show bgp vrf spoke_1 ipv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : spoke_1

Local Router-ID 20.0.1.2

    Network            Nexthop         Metric     LocPrf     Weight Path

    Route Distinguisher: 1:1

*>  0.0.0.0/0          3.3.3.3         0          100        0       102 ?

*>  20.4.1.0/24        3.3.3.3         0          100        0       102 ?

*>  20.5.1.0/24        3.3.3.3         0          100        0       102 ?

*>  20.6.1.0/24        3.3.3.3         0          100        0       102 ?

*>e 101.0.0.0/24       20.0.1.1        0          100        0       100 i

*>  151.0.0.0/24       3.3.3.3         0          100        0       102 ?

*>  201.0.0.0/24       3.3.3.3         0          100        0       102 ?
Total number of entries 7

PE1# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 1.1.1.1

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 149

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast

------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 2.2.2.2         6488163     37      36      00h:29m:42s  Established   Up

 3.3.3.3         6488163     40      36      00h:29m:14s  Established   Up

Address-family : L2VPN EVPN

-----------------------------

VRF : spoke_1

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.0.1.2

 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.0.1.1        100         37      40      00h:29m:45s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

PE1# show ip route all-vrfs

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default
Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          -                loopback0     -

L         [0/0]        -

2.2.2.2/32          30.0.1.2         1/1/38        -

O         [110/200]    00h:31m:42s

3.3.3.3/32          30.0.1.2         1/1/38        -

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 150

O         [110/150]    00h:31m:21s

4.4.4.4/32          30.0.1.2         1/1/38        -

O         [110/100]    00h:32m:18s

30.0.1.0/24         -                1/1/38        -

C         [0/0]        -

30.0.1.1/32         -                1/1/38        -

L         [0/0]        -

30.0.2.0/24         30.0.1.2         1/1/38        -

O         [110/200]    00h:32m:18s

30.0.3.0/24         30.0.1.2         1/1/38        -

O         [110/150]    00h:32m:06s

VRF: spoke_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           3.3.3.3          1/1/38        default

B/V       [200/0]      00h:23m:22s

20.0.1.0/24         -                vlan2001      -

C         [0/0]        -

20.0.1.2/32         -                vlan2001      -

L         [0/0]        -

20.4.1.0/24         3.3.3.3          1/1/38        default

B/V       [200/0]      00h:29m:55s

20.5.1.0/24         3.3.3.3          1/1/38        default

B/V       [200/0]      00h:30m:37s

20.6.1.0/24         3.3.3.3          1/1/38        default

B/V       [200/0]      00h:24m:12s

101.0.0.0/24        20.0.1.1         vlan2001      -

B/E       [20/0]       00h:28m:23s
151.0.0.0/24        3.3.3.3          1/1/38        default

B/V       [200/0]      00h:23m:22s

201.0.0.0/24        3.3.3.3          1/1/38        default

B/V       [200/0]      00h:28m:22s

Total Route Count : 17

PE2 Configuration

PE2# show running-config

Current configuration:

!

!Version ArubaOS-CX LL.10.09.0001AX

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 151

!export-password: default

hostname PE2

profile core-spine

logging console severity crit

vrf spoke_2

    rd 1:1

    l3vpn-only

    address-family ipv4 unicast

        route-target export 1:1

        route-target import 1:0

    exit-address-family

cli-session

    timeout 0

!

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2011

interface mgmt

    no shutdown

    ip dhcp

interface 1/1/43

    no shutdown

    description Towards CE1

    no routing

    vlan trunk native 1

    vlan trunk allowed 2011

interface 1/1/44

    no shutdown
    mtu 9198

    description Towards P1

    ip address 30.0.2.1/24

    ip ospf 1 area 0.0.0.0

    mpls enable

    mpls ldp enable

interface loopback 0

    ip address 2.2.2.2/32

    ip ospf 1 area 0.0.0.0

interface vlan 2011

    vrf attach spoke_2

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 152

description Towards CE1

    ip address 20.1.1.2/24

!

!

!

!

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 1.1.1.1 remote-as 6488163

    neighbor 1.1.1.1 description Towards PE1-SPOKE1

    neighbor 1.1.1.1 update-source loopback 0

    neighbor 3.3.3.3 remote-as 6488163

    neighbor 3.3.3.3 description Towards PE3-HUB

    neighbor 3.3.3.3 update-source loopback 0

    address-family vpnv4 unicast

        neighbor 1.1.1.1 activate

        neighbor 1.1.1.1 send-community both

        neighbor 3.3.3.3 activate

        neighbor 3.3.3.3 send-community both

    exit-address-family

!

    vrf spoke_2

        neighbor 20.1.1.1 remote-as 101

        neighbor 20.1.1.1 description Towards CE2

        address-family ipv4 unicast

            neighbor 20.1.1.1 activate

            neighbor 20.1.1.1 send-community both

            neighbor 20.1.1.1 soft-reconfiguration inbound

        exit-address-family

!
https-server vrf mgmt

mpls

    enable

    label-protocol ldp

        enable

        router-id loopback0

PE2# show ip ospf neighbors

VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 1

Neighbor ID      Priority  State             Nbr Address       Interface

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 153

-------------------------------------------------------------------------

4.4.4.4          1         FULL/DR           30.0.2.2           1/1/44

PE2 Verification

PE2# show mpls ldp neighbor

Local LDP Identifier: 2.2.2.2:0, Peer LDP Identifier: 4.4.4.4:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:17:57

    State: operational

    LDP Discovery Sources: 1/1/44

    Addresses bound to this peer:

         30.0.1.2 30.0.2.2 30.0.3.1 4.4.4.4

PE2# show mpls forwarding

MPLS Bindings

Entry Bindings   : 9

Exit Bindings    : 3

Transit Bindings : 3

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix       Ingress  Nexthop    Outgoing  Egress     Egress   Status

                    VRF      Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    1.1.1.1/32   default  30.0.2.2   16        1/1/44     default

operational

LDP    3.3.3.3/32   default  30.0.2.2   18        1/1/44     default

operational

BGP    0.0.0.0/0    spoke_2  3.3.3.3    19        1/1/44     default

operational

BGP    20.4.1.0/24  spoke_2  3.3.3.3    19        1/1/44     default

operational

BGP    20.5.1.0/24  spoke_2  3.3.3.3    19        1/1/44     default

operational

BGP    20.6.1.0/24  spoke_2  3.3.3.3    19        1/1/44     default

operational

BGP    101.0.0.0/24 spoke_2  3.3.3.3    19        1/1/44     default

operational

BGP    151.0.0.0/24 spoke_2  3.3.3.3    19        1/1/44     default

operational

Exit Bindings:

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 154

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  19        spoke_2

operational

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

---

LDP     1.1.1.1/32   16        1/1/44     default  30.0.2.2  16

operational

LDP     4.4.4.4/32   17        1/1/44     default  30.0.2.2  exp-null

operational

LDP     3.3.3.3/32   18        1/1/44     default  30.0.2.2  18

operational

PE2# show bgp vpnv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 1.1.1.1 (Internal)

    Description         : Towards PE1-SPOKE1

    Peer-group          :

    Remote Router Id    : 1.1.1.1            Local Router Id    : 2.2.2.2

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 39729              Local Port         : 179
    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:19m:46s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 155

Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      2        2

    Keepalives                  22       22

    Route Refresh                0        0

    Total                       25       25

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :
    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 3.3.3.3 (Internal)

    Description         : Towards PE3-HUB

    Peer-group          :

    Remote Router Id    : 3.3.3.3            Local Router Id    : 2.2.2.2

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 38293

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 156

State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:19m:28s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      2        9

    Keepalives                  22       17

    Route Refresh                0        0

    Total                       25       27

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes
    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 157

Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE2# show bgp vrf spoke_2 ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : spoke_2

BGP Neighbor 20.1.1.1 (External)

    Description         : Towards CE2

    Peer-group          :

    Remote Router Id    : 20.8.1.2           Local Router Id    : 20.1.1.2

    Remote AS           : 101                Local AS           : 6488163

    Remote Port         : 179                Local Port         : 60400

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:21m:33s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No
    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      9        2

    Keepalives                  20       24

    Route Refresh                0        0

    Total                       30       27

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 158

Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         No              No

    Address family L2VPN EVPN            No              No

    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE2# show bgp vrf spoke_2 ipv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : spoke_2

Local Router-ID 20.1.1.2

    Network            Nexthop         Metric     LocPrf     Weight Path

    Route Distinguisher: 1:1

*>  0.0.0.0/0          3.3.3.3         0          100        0       102 ?

*>  20.4.1.0/24        3.3.3.3         0          100        0       102 ?

*>  20.5.1.0/24        3.3.3.3         0          100        0       102 ?

*>  20.6.1.0/24        3.3.3.3         0          100        0       102 ?
*>  101.0.0.0/24       3.3.3.3         0          100        0       102 ?

*>  151.0.0.0/24       3.3.3.3         0          100        0       102 ?

*>e 201.0.0.0/24       20.1.1.1        0          100        0       101 i

Total number of entries 7

PE2# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 2.2.2.2

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 159

Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast

------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 1.1.1.1         6488163     36      37      00h:29m:42s  Established   Up

 3.3.3.3         6488163     39      37      00h:29m:24s  Established   Up

Address-family : L2VPN EVPN

-----------------------------

VRF : spoke_2

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.1.1.2

 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.1.1.1        101         36      39      00h:29m:27s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

PE2# show ip route all-vrfs

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN
              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          30.0.2.2         1/1/44        -

O         [110/200]    00h:31m:42s

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 160

2.2.2.2/32          -                loopback0     -

L         [0/0]        -

3.3.3.3/32          30.0.2.2         1/1/44        -

O         [110/150]    00h:31m:21s

4.4.4.4/32          30.0.2.2         1/1/44        -

O         [110/100]    00h:31m:42s

30.0.1.0/24         30.0.2.2         1/1/44        -

O         [110/200]    00h:31m:42s

30.0.2.0/24         -                1/1/44        -

C         [0/0]        -

30.0.2.1/32         -                1/1/44        -

L         [0/0]        -

30.0.3.0/24         30.0.2.2         1/1/44        -

O         [110/150]    00h:31m:42s

VRF: spoke_2

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           3.3.3.3          1/1/44        default

B/V       [200/0]      00h:23m:22s

20.1.1.0/24         -                vlan2011      -

C         [0/0]        -

20.1.1.2/32         -                vlan2011      -

L         [0/0]        -

20.4.1.0/24         3.3.3.3          1/1/44        default

B/V       [200/0]      00h:29m:55s

20.5.1.0/24         3.3.3.3          1/1/44        default

B/V       [200/0]      00h:30m:37s

20.6.1.0/24         3.3.3.3          1/1/44        default
B/V       [200/0]      00h:24m:12s

101.0.0.0/24        3.3.3.3          1/1/44        default

B/V       [200/0]      00h:28m:22s

151.0.0.0/24        3.3.3.3          1/1/44        default

B/V       [200/0]      00h:23m:22s

201.0.0.0/24        20.1.1.1         vlan2011      -

B/E       [20/0]       00h:28m:22s

Total Route Count : 17

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 161

PE3 Configuration

PE3# show running-config

Current configuration:

!

!Version ArubaOS-CX LL.10.09.0001AX

!export-password: default

hostname PE3

profile core-spine

logging console severity crit

vrf hub_export

    rd 1:0

    l3vpn-only

    address-family ipv4 unicast

        route-target export 1:0

    exit-address-family

vrf hub_import

    rd 0:1

    l3vpn-only

    address-family ipv4 unicast

        route-target import 1:1

    exit-address-family

cli-session

    timeout 0

!

!

!

!

!

!

ssh server vrf mgmt

vlan 1,2021,2031

interface mgmt

    no shutdown

    ip dhcp

system interface-group 1 speed 10g

    !interface group 1 contains ports 1/1/1-1/1/4

interface lag 99

    no shutdown

    description Towards P1

    ip address 30.0.3.2/24

    lacp mode active

    ip ospf 1 area 0.0.0.0

    mpls enable

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 162

mpls ldp enable

interface 1/1/31

    no shutdown

    mtu 9198

    description Towards P1 LAG 99

    lag 99

interface 1/1/32

    no shutdown

    mtu 9198

    description Towards P1 LAG 99

    lag 99

interface 1/1/33

    no shutdown

    description Towards CE3

    no routing

    vlan trunk native 1

    vlan trunk allowed 2021

interface 1/1/34

    no shutdown

    description Towards CE4

    no routing

    vlan trunk native 1

    vlan trunk allowed 2031

interface loopback 0

    ip address 3.3.3.3/32

    ip ospf 1 area 0.0.0.0

interface vlan 2021

    vrf attach hub_import

    description Towards CE3

    ip address 20.2.1.1/24

interface vlan 2031

    vrf attach hub_export
    description Towards CE4

    ip address 20.3.1.1/24

!

!

!

!

!

router ospf 1

    area 0.0.0.0

router bgp 6488163

    neighbor 1.1.1.1 remote-as 6488163

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 163

neighbor 1.1.1.1 description Towards PE1-SPOKE1

    neighbor 1.1.1.1 update-source loopback 0

    neighbor 2.2.2.2 remote-as 6488163

    neighbor 2.2.2.2 description Towards PE2-SPOKE2

    neighbor 2.2.2.2 update-source loopback 0

    address-family vpnv4 unicast

        neighbor 1.1.1.1 activate

        neighbor 1.1.1.1 send-community both

        neighbor 2.2.2.2 activate

        neighbor 2.2.2.2 send-community both

    exit-address-family

!

    vrf hub_export

        neighbor 20.3.1.2 remote-as 102

        neighbor 20.3.1.2 description Towards CE3

        address-family ipv4 unicast

            neighbor 20.3.1.2 activate

            neighbor 20.3.1.2 send-community both

            neighbor 20.3.1.2 soft-reconfiguration inbound

        exit-address-family

!

    vrf hub_import

        neighbor 20.2.1.2 remote-as 102

        neighbor 20.2.1.2 description Towards CE4

        address-family ipv4 unicast

            neighbor 20.2.1.2 activate

            neighbor 20.2.1.2 send-community both

            neighbor 20.2.1.2 soft-reconfiguration inbound

        exit-address-family

!

https-server vrf mgmt

mpls
    enable

    label-protocol ldp

        enable

        router-id loopback0

PE3# show ip ospf neighbors

VRF : default                          Process : 1

===================================================

Total Number of Neighbors : 1

Neighbor ID      Priority  State             Nbr Address       Interface

-------------------------------------------------------------------------

4.4.4.4          1         FULL/DR           30.0.3.1           lag99

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 164

PE3 Verification

PE3# show mpls ldp neighbor

Local LDP Identifier: 3.3.3.3:0, Peer LDP Identifier: 4.4.4.4:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:17:21

    State: operational

    LDP Discovery Sources: lag99

    Addresses bound to this peer:

         30.0.1.2 30.0.2.2 30.0.3.1 4.4.4.4

PE3# show mpls forwarding

MPLS Bindings

Entry Bindings   : 5

Exit Bindings    : 3

Transit Bindings : 3

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin Prefix       Ingress   Nexthop    Outgoing  Egress     Egress

Status

                    VRF       Address    Label     Interface  VRF

----------------------------------------------------------------------------

---

LDP    1.1.1.1/32   default   30.0.3.1   16        lag99      default

operational

LDP    2.2.2.2/32   default   30.0.3.1   17        lag99      default

operational

LDP    4.4.4.4/32   default   30.0.3.1   exp-null  lag99      default

operational

BGP    101.0.0.0/24 hub_import 1.1.1.1   19        lag99      default

operational

BGP    201.0.0.0/24 hub_import 2.2.2.2   19        lag99      default

operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  19        hub_export

operational

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 165

static   n/a                 7         -         default

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop   Outgoing

Status

                     Label     Interface  VRF      Address

Label

----------------------------------------------------------------------------

---

LDP     1.1.1.1/32   16        lag99      default  30.0.3.1  16

operational

LDP     2.2.2.2/32   17        lag99      default  30.0.3.1  17

operational

LDP     4.4.4.4/32   18        lag99      default  30.0.3.1  exp-null

operational

PE3# show bgp vpnv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 1.1.1.1 (Internal)

    Description         : Towards PE1-SPOKE1

    Peer-group          :

    Remote Router Id    : 1.1.1.1            Local Router Id    : 3.3.3.3

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 179                Local Port         : 43547

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:19m:18s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled
    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 166

-------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      9        2

    Keepalives                  18       22

    Route Refresh                0        0

    Total                       28       25

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

BGP Neighbor 2.2.2.2 (Internal)

    Description         : Towards PE2-SPOKE2

    Peer-group          :
    Remote Router Id    : 2.2.2.2            Local Router Id    : 3.3.3.3

    Remote AS           : 6488163            Local AS           : 6488163

    Remote Port         : 38293              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:19m:28s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 167

Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      9        2

    Keepalives                  17       22

    Route Refresh                0        0

    Total                       27       25

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30
    Max. Prefix         : 300000              Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE3# show bgp vrf hub_import ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : hub_import

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 168

BGP Neighbor 20.2.1.2 (External)

    Description         : Towards CE4

    Peer-group          :

    Remote Router Id    : 20.4.1.1           Local Router Id    : 20.2.1.1

    Remote AS           : 102                Local AS           : 6488163

    Remote Port         : 48554              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:22m:06s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      3        8

    Keepalives                  26       22

    Route Refresh                0        0

    Total                       30       31
    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         No              No

    Address family L2VPN EVPN            No              No

    Address Family : IPv4 Unicast

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 169

-----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE3# show bgp vrf hub_export ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : hub_export

BGP Neighbor 20.3.1.2 (External)

    Description         : Towards CE3

    Peer-group          :

    Remote Router Id    : 20.5.1.1           Local Router Id    : 20.3.1.1

    Remote AS           : 102                Local AS           : 6488163

    Remote Port         : 179                Local Port         : 52062

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:21m:56s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error
    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 1                  Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      1        9

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 170

Keepalives                  25       21

    Route Refresh                0        0

    Total                       27       31

    Capability                           Advertised      Received

    ----------------------------         -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          Yes             Yes

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         No              No

    Address family L2VPN EVPN            No              No

    Address Family : IPv4 Unicast

    -----------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 300000              Soft Reconfig In  : Yes

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       : Disable

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :

PE3# show bgp vrf hub_import ipv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : hub_import

Local Router-ID 20.2.1.1
    Network            Nexthop         Metric     LocPrf     Weight Path

    Route Distinguisher: 0:1

*>e 0.0.0.0/0          20.2.1.2        0          100        0       102 ?

*>e 20.4.1.0/24        20.2.1.2        0          100        0       102 ?

*>e 20.5.1.0/24        20.2.1.2        0          100        0       102 ?

*>e 20.6.1.0/24        20.2.1.2        0          100        0       102 ?

*>  101.0.0.0/24       1.1.1.1         0          100        0       100 i

*>e 151.0.0.0/24       20.2.1.2        0          100        0       102 ?

*>  201.0.0.0/24       2.2.2.2         0          100        0       101 i

Total number of entries 7

PE3# show bgp vrf hub_export ipv4 unicast

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 171

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : hub_export

Local Router-ID 20.3.1.1

    Network            Nexthop         Metric     LocPrf     Weight Path

    Route Distinguisher: 1:0

*>e 0.0.0.0/0          20.3.1.2        0          100        0       102 ?

*>e 20.4.1.0/24        20.3.1.2        0          100        0       102 ?

*>e 20.5.1.0/24        20.3.1.2        0          100        0       102 ?

*>e 20.6.1.0/24        20.3.1.2        0          100        0       102 ?

*>e 101.0.0.0/24       20.3.1.2        0          100        0       102 ?

*>e 151.0.0.0/24       20.3.1.2        0          100        0       102 ?

*>e 201.0.0.0/24       20.3.1.2        0          100        0       102 ?

Total number of entries 7

PE3# show bgp all-vrf all summary

VRF : default

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 3.3.3.3

 Peers                  : 2            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

Address-family : IPv6 Unicast

-----------------------------

Address-family : VPNv4 Unicast

------------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus
 1.1.1.1         6488163     36      40      00h:29m:14s  Established   Up

 2.2.2.2         6488163     37      39      00h:29m:24s  Established   Up

Address-family : L2VPN EVPN

-----------------------------

VRF : hub_export

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.3.1.1

 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 172

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.3.1.2        102         39      35      00h:28m:48s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

VRF : hub_import

BGP Summary

-----------

 Local AS               : 6488163      BGP Router Identifier  : 20.2.1.1

 Peers                  : 1            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

Address-family : IPv4 Unicast

-----------------------------

 Neighbor        Remote-AS   MsgRcvd MsgSent Up/Down Time State

AdminStatus

 20.2.1.2        102         39      38      00h:29m:07s  Established   Up

Address-family : IPv6 Unicast

-----------------------------

PE3# show ip route all-vrfs

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type
Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          30.0.3.1         lag99         -

O         [110/150]    00h:31m:22s

2.2.2.2/32          30.0.3.1         lag99         -

O         [110/150]    00h:31m:22s

3.3.3.3/32          -                loopback0     -

L         [0/0]        -

4.4.4.4/32          30.0.3.1         lag99         -

O         [110/50]     00h:31m:22s

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 173

30.0.1.0/24         30.0.3.1         lag99         -

O         [110/150]    00h:31m:22s

30.0.2.0/24         30.0.3.1         lag99         -

O         [110/150]    00h:31m:22s

30.0.3.0/24         -                lag99         -

C         [0/0]        -

30.0.3.2/32         -                lag99         -

L         [0/0]        -

VRF: hub_export

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           20.3.1.2         vlan2031      -

B/E       [20/0]       00h:23m:22s

20.3.1.0/24         -                vlan2031      -

C         [0/0]        -

20.3.1.1/32         -                vlan2031      -

L         [0/0]        -

20.4.1.0/24         20.3.1.2         vlan2031      -

B/E       [20/0]       00h:29m:55s

20.5.1.0/24         20.3.1.2         vlan2031      -

B/E       [20/0]       00h:30m:37s

20.6.1.0/24         20.3.1.2         vlan2031      -

B/E       [20/0]       00h:24m:12s

101.0.0.0/24        20.3.1.2         vlan2031      -

B/E       [20/0]       00h:28m:22s

151.0.0.0/24        20.3.1.2         vlan2031      -

B/E       [20/0]       00h:23m:22s

201.0.0.0/24        20.3.1.2         vlan2031      -
B/E       [20/0]       00h:28m:22s

VRF: hub_import

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

0.0.0.0/0           20.2.1.2         vlan2021      -

B/E       [20/0]       00h:23m:22s

20.2.1.0/24         -                vlan2021      -

Public

Use case 2: MPLS L3 VPN with hub and spoke VRFs 174

C         [0/0]        -

20.2.1.1/32         -                vlan2021      -

L         [0/0]        -

20.4.1.0/24         20.2.1.2         vlan2021      -

B/E       [20/0]       00h:30m:57s

20.5.1.0/24         20.2.1.2         vlan2021      -

B/E       [20/0]       00h:29m:55s

20.6.1.0/24         20.2.1.2         vlan2021      -

B/E       [20/0]       00h:24m:12s

101.0.0.0/24        1.1.1.1          lag99         default

B/V       [200/0]      00h:28m:23s

151.0.0.0/24        20.2.1.2         vlan2021      -

B/E       [20/0]       00h:23m:22s

201.0.0.0/24        2.2.2.2          lag99         default

B/V       [200/0]      00h:28m:23s

Total Route Count : 26

MPLS commands

Subtopics

MPLS commands

MPLS commands

Select a command from the list in the left navigation menu..

Subtopics

bind ipv4 (lsp label imposition)
bind ipv4 input (static lsp binding)
clear mpls statistics
crossconnect input (static lsp binding label swap)
enable (mpls globally)
enable mpls (interface)
enable (mpls ldp)
enable (mpls static lsp)
graceful-restart (mpls ldp)
graceful-restart-timers (mpls ldp)
label-protocol ldp
label-range (static lsp)

Public

MPLS commands 175

mpls
mpls ldp discovery hello hold time (global)
mpls ldp discovery hello hold time (interface)
mpls ldp enable
graceful-restart-timers (mpls ldp)
mpls ldp session holdtime (interface)
ping mpls
router-id (mpls ldp)
session hold time (mpls ldp globally)
show bgp vpnv4 unicast
show capacities mpls
show mpls forwarding
show mpls label-range static-lsp
show mpls ldp bindings
show mpls ldp discovery
show mpls ldp graceful-restart
show mpls ldp neighbor
static-lsp
traceroute mpls

bind ipv4 (lsp label imposition)

Syntax

bind ipv4 {<IP-ADDR>/<MASK> | <IP-ADDR>

            <MASK>} output <IFNAME>

            <IP-ADDR>

            <OUT-LABEL>

no bind ipv4 {<IP-ADDR>/<MASK> | <IP-ADDR>

            <MASK>} output <IFNAME>
            <IP-ADDR>

            <OUT-LABEL>

Description

Performs LSP label imposition by adding label to an ingress packet (push operation).

The no form of this command removes the ingress packet label.

Public

bind ipv4 (lsp label imposition) 176

Parameter

Description

ipv4 <IP‐ADDR>/
<MASK>

ipv4 <IP‐ADDR> <MASK>

Specifies the IPv4 destination in x.x.x.x format, where x is a dec
imal value from 0 to 255 and the number of bits in an IPv4 add
ress mask in CIDR format (x), where x is a decimal number from
0 to 32.

Specifies the IPv4 destination in x.x.x.x format, where x is a dec
imal value from 0 to 255 and the destination IP subnet mask in
x.x.x.x format, where x is a decimal value from 0 to 255.

Specifies the egress interface of the binding.

<IFNAME>

<IP‐ADDR>

<OUT‐LABEL>

Usage

Specifies he next hop IP address of the binding.

Specifies the MPLS label to apply. Range: 16‐1048575.

•  The no form of both the mpls and static-lsp commands deletes all static LSP bindings.

•  The static LSP label range must be allocated before configuring static LSP bindings.

•  Specifying an outgoing label outside the range of 16-1048575 is not allowed. An outgoing label is not

bound by allocated static LSP label range.

•  Types of valid egress interfaces are: System, LAG, VLAN, and Tunnel.

◦  Routing must be enabled for egress interfaces.

◦

Interfaces must be configured before performing the bind command.

◦  LAG member interfaces are not allowed as egress interfaces.

Examples

Configuring binding:

Public

bind ipv4 (lsp label imposition) 177

switch(config-mpls-static-lsp)# bind ipv4 2.2.2.0/24 output 1/1/1 20.0.0.2

20

Unconfiguring binding:

switch(config-mpls-static-lsp)# no bind ipv4 2.2.2.0/24 output 1/1/1

20.0.0.2 20

Configuring binding with an invalid egress interface:

switch(config-mpls-static-lsp)# bind ipv4 2.2.2.0/24 output 1/1/1 20.0.0.2

20

 The output must be a layer 3 interface with routing enabled.
Configuring binding with an interface that does not have an IP address assigned:

switch(config-mpls-static-lsp)# bind ipv4 2.2.2.0/24 output 1/1/1 20.0.0.2

20

 The egress interface must have an IP address assigned.
Configuring binding with a next hop IP that is not in the same subnet as egress interface:

switch(config-if)# interface 1/1/1

switch(config-if)# no shutdown

switch(config-if)# ip address 10.0.0.1/24

switch(config-if)# mpls enable

switch(config-if)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# bind ipv4 2.2.2.0/24 output 1/1/1 60.0.0.20

40

 The next hop IP address must be in the same subnet as interface 1/1/1.
Configuring binding with a next hop IP that is the same as the egress interface IP:

switch(config-if)# int 1/1/1

switch(config-if)# no shutdown

switch(config-if)# ip address 10.0.0.1/24
switch(config-if)# mpls enable

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# bind ipv4 2.2.2.0/24 output 1/1/1 10.0.0.1

40

 The next hop IP address cannot be the same as any interface 1/1/1 primary

or secondary addresses.

Public

bind ipv4 (lsp label imposition) 178

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐
static‐lsp

Administrators or local user group members with execution righ
ts for this command.

bind ipv4 input (static lsp binding)

Syntax

bind ipv4 input <in-label>

no bind ipv4 input <in-label>

Description

Performs label disposition by removing label from an egress packet (pop operation).

The no form of this command removes the static LSP binding configuration.

Parameter

Description

Specifies the MPLS label to bind. Range: 16‐1048575.

<in‐label>

Usage

•  The no form of both the mpls and static-lsp commands deletes all MPLS binding configurations.

•  The static LSP label range must be allocated before configuring static LSP bindings.

•  Specifying an incoming label outside the range of 16-1048575 is not allowed. An incoming label is

bound by the allocated static LSP label range.

Public

bind ipv4 input (static lsp binding) 179

Examples

Configuring static LSP binding for label disposition:

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# bind ipv4 input 20

Removing the configuration for static LSP binding:

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# no bind ipv4 input 20

Configuring static LSP binding outside the label range:

switch(config-mpls-static-lsp)# bind ipv4 input 200

The input label must be within the range specified by label-range.
Configuring static LSP binding without first allocating a label range:

switch(config-mpls-static-lsp)# bind ipv4 input 20A label range must be

allocated before configuring bindings.

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐hpe_anw‐
central

Administrators or local user group members with execution righ
ts for this command.

clear mpls statistics

Syntax

clear mpls statistics {ingress | egress} <LABEL>

no syntax

Public

clear mpls statistics 180

Description
Clears MPLS statistics per label for all sessions.
| Parameter        |     | Description                 |
| ---------------- | --- | --------------------------- |
| ingress          |     | Selects ingress statistics. |
| egress           |     | Selects egress statistics.  |
Specifies the label for which statistics will be cleared.

<LABEL>

Examples
Clearing ingress MPLS statistics for a specific label:
switch# clear mpls statistics ingress 20

Command History
Release Modification
10.09 Command introduced
Command Information
| Platforms | Command context | Authority |
| --------- | --------------- | --------- |
8360 Operator (>) or Manage Administrators or local user group members with execution righ
|     | r (# ) | ts for this command. |
| --- | ------ | -------------------- |

crossconnect input (static lsp binding label
swap)
Public crossconnect input (static lsp binding label swap) 181

Syntax

crossconnect input <in-label> output <IFNAME>

            <ID-ADDR> {<out-label> | explicit-null}

no crossconnect input <in-label> output <IFNAME>

            <ID-ADDR> {<out-label> | explicit-null}

Description

Configures a static LSP binding to swap labels and route to the given next hop.

The no form of this command removes the static LSP binding label swap configuration.

Parameter

Description

Specifies the MPLS label to bind. Range: 16‐1048575.

<in‐label>

<IFNAME>

<IP‐ADDR>

<out‐label>

Specifies the egress interface of the binding.

Specifies the next hop IP address of the binding.

Specifies the MPLS label to apply. Range: 16‐1048575.

explicit‐null

Specifies an IETF MPLS IPv4 explicit null label (0).

Usage

•  A static LSP label range must be allocated before configuring static LSP bindings.

•  An incoming label must be within the allocated static LSP label range. Outgoing labels are not bound by

the allocated static LSP label range, but must still be within the range of 16-1048575.

•  The types of valid outgoing interfaces are: System, LAG, VLAN, and Tunnel.

◦  Routing must be enabled for egress interfaces.

◦  LAG member interfaces cannot be used with this command.

Public

crossconnect input (static lsp binding label swap) 182

•  Next hop and outgoing label pairs must be unique for each crossconnect binding.

Examples

Configuring crossconnect with an incoming and outgoing label:

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# crossconnect input 20 output 1/1/2 11.0.3.2

21

Configuring explicit-null PHP:

switch(config-mpls-static-lsp)# crossconnect input 20 output 1/1/2 11.0.3.2

explicit-null

Removing crossconnect binding:

switch(config-mpls-static-lsp)# no crossconnect input 20 output 1/1/2

11.0.3.2 21

Configuring crossconnect with an incoming label outside the allocated range:

switch(config-mpls-static-lsp)# crossconnect input 20 output 11.0.3.2 99

 Failed to configure static LSP binding. Incoming label not in range

allocated for static LSP.
Configuring crossconnect with an interface that does not have routing enabled:

switch(config-mpls-static-lsp)# crossconnect input 20 output 1/1/8 11.0.3.2

21

The egress interface must have an IP address assigned.
Configuring crossconnect with a nexthop IP that is not in the same subnet as egress interface:

switch(config-if)# int 1/1/1

switch(config-if)# no shutdown

switch(config-if)# ip address 10.0.0.1/24
switch(config-if)# mpls enable

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# crossconnect input 35 output 1/1/1

60.0.0.20 40

The next hop IP address must be in the same subnet as interface 1/1/1.
Configuring crossconnect with a nexthop IP that is the same as the egress interface IP:

switch(config-if)# int 1/1/1

switch(config-if)# no shutdown

switch(config-if)# ip address 10.0.0.1/24

switch(config-if)# mpls enable

Public

crossconnect input (static lsp binding label swap) 183

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# crossconnect input 35 output 1/1/1

10.0.0.1  40

The next hop IP address cannot be the same as any interface 1/1/1 primary

or secondary addresses.
Configuring crossconect with a nexthop IP and outgoing label of an already existing binding:

switch(config-if)# int 1/1/1

switch(config-if)# no shutdown

switch(config-if)# ip address 10.0.0.1/24

switch(config-if)# mpls enable

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# crossconnect input 35 output 1/1/1 10.0.0.2

40

switch(config-mpls-static-lsp)# crossconnect input 36 output 1/1/1 10.0.0.2

40

 A static LSP binding with the same nexthop and outgoing label already

exists.

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐
static‐lsp

Administrators or local user group members with execution righ
ts for this command.

enable (mpls globally)

Syntax

enable

no enable

Public

enable (mpls globally) 184

Description

Enables MPLS forwarding of IPv4 traffic globally.

The no form of this command disables MPLS forwarding of IPv4 traffic globally.

Examples

Enabling MPLS forwarding of IPv4 traffic:

switch(config)# mpls

switch(config-mpls)# enable

Disabling MPLS forwarding of IPv4 traffic:

switch(config)# mpls

switch(config-mpls)# no enable

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls

Administrators or local user group members with execution righ
ts for this command.

enable mpls (interface)

Syntax

mpls enable

no mpls enable

Description

Enables MPLS forwarding of IP traffic for the interface.

The no form of this command disables MPLS forwarding of IP traffic for the interface.

Public

enable mpls (interface) 185

Usage

•  Routing must be configured before enabling MPLS on an interface.

Examples

Enabling MPLS forwarding:

switch(config)# interface 1/1/1

switch(config-if)# routing

switch(config-if)# mpls enable

Enabling MPLS on a layer 2 interface:

switch(config)# interface 1/1/2

switch(config-if)# mpls enable

Routing must be enabled on this interface to use MPLS
Disabling MPLS forwarding:

switch(config)# interface 1/1/2

switch(config-if)# no mpls enable

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐if

Administrators or local user group members with execution righ
ts for this command.

enable (mpls ldp)

Syntax

enable

no enable

Public

enable (mpls ldp) 186

Description

Enables MPLS LDP.

The no form of this command disable MPLS LDP.

Usage

The LDP back off timer cannot be configured. It is set to exponentially back off session retry attempts with
initial value of 15 seconds and a maximum of 2 minutes.

Examples

Enabling MPLS LDP:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# enable

Disabling MPLS LDP:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no enable

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐ldp

Administrators or local user group members with execution righ
ts for this command.

enable (mpls static lsp)

Public

enable (mpls static lsp) 187

Syntax

enable

no enable

Description

Enables MPLS static LSPs.

The no form of this command disables static LSPs.

Usage

A static LSP binding will be processed when MPLS is globally enabled, static LSP is enabled, and the ingress
and egress interface has MPLS enabled.

Examples

Enabling MPLS static LSPs:

switch(config)# mpls

switch(config-mpls)# enable

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# enable

Disabling static LSPs:

switch(config)# mpls

switch(config-mpls)# static-lsp

switch(config-mpls-static-lsp)# no enable

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

8360

config
config‐mpls
config‐mpls‐
static‐lsp

Administrators or local user group members with execution righ
ts for this command.

Public

enable (mpls static lsp) 188

graceful-restart (mpls ldp)

Syntax

graceful-restart

Description

Enables LDP graceful restart. Graceful restart is enabled by default. With graceful restart enabled, the MPLS
forwarding state will be temporarily retained if the control plane restarts. The switch will wait after losing
LDP neighbors before deleting bindings from that neighbor. See mpls ldp graceful restart timers for details.
Graceful restart is enabled for LDP sessions only when the LDP setting and the overall router setting are
enabled. If either is disabled, then graceful restart will not occur for LDP sessions.

Upon being disabled or enabled, any LDP sessions will be restarted, which may result in temporary traffic
loss.

The no form of this command disables LDP graceful restart

Examples

Enabling MPLS LDP graceful restart:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# graceful-restart

Enabling graceful restart will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Disabling MPLS LDP graceful restart:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp
switch(config-mpls-ldp)# no graceful-restart

Enabling graceful restart will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Command History

Release

10.11

Modification

Command introduced.

Public

graceful-restart (mpls ldp) 189

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐ldp

Administrators or local user group members with execution righ
ts for this command.

graceful-restart-timers (mpls ldp)

Syntax

graceful-restart-timers {forwarding-holding <SECONDS> | max-recovery

<SECONDS> | neighbor-liveness <SECONDS>}

no graceful-restart-timers {forwarding-holding <SECONDS> | max-recovery

<SECONDS> | neighbor-liveness <SECONDS>}

Description

Configures MPLS LDP discovery hold time for peers found via hello packets.

The no form of this command resets the discovery hello hold time to its default value of 15 seconds.

NOTE

The BGP restart timer must be configured as 180 seconds or higher for graceful
restart to work with MPLS.

NOTE

It is recommended to configure the OSPF graceful restart timer as lower than the
LDP forward-holding timer, which in turn should be configured as lower than the
BGP graceful restart timer.

Parameter

Description

forwarding‐holding
<SECONDS>

max‐recovery <SECONDS>

Specifies the amount of time in seconds that the MPLS forwardi
ng state should be preserved after the control plane restarts. Ra
nge: 30‐600. Default: 150.

Specifies the amount of time in seconds that the stale label bin
dings should be kept on the router after the LDP session has be
en reestablished. Range: 15‐600. Default: 120.

Public

graceful-restart-timers (mpls ldp) 190

Parameter

Description

neighbor‐liveness <SECONDS>

Specifies the amount of time in seconds that the router will wai
t for the LDP session to be reestablished. If the router cannot re
establish the LDP session within that time, the router deletes all
the stale LDP bindings received from that LDP neighbor. Range:
5‐300. Default: 120.

Examples

Configuring the MPLS LDP graceful restart forwarding holding time for 30 seconds:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# graceful-restart-timers forwarding-holding 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Resetting the MPLS LDP graceful restart forwarding holding time to default:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no graceful-restart-timers forwarding-holding

switch(config-mpls-ldp)# no graceful-restart-timers forwarding-holding 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Configuring the MPLS LDP graceful restart max recovery time for 30 seconds:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# graceful-restart-timers max-recovery 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Resetting the MPLS LDP graceful restart max recovery time to default:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp
switch(config-mpls-ldp)# no graceful-restart-timers max-recovery
switch(config-mpls-ldp)# no graceful-restart-timers max-recovery 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Public

graceful-restart-timers (mpls ldp) 191

Continue (y/n)? y

Configuring the MPLS LDP graceful restart neighbor liveness timefor 30 seconds:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# graceful-restart-timers neighbor-liveness 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Resetting the MPLS LDP graceful restart neighbor liveness to default:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no graceful-restart-timers neighbor-liveness

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Command History

Release

10.10

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐ldp

Administrators or local user group members with execution righ
ts for this command.

label-protocol ldp

Syntax

label-protocol ldp

no label-protocol ldp

Public

label-protocol ldp 192

Description

Configures the Label Distribution Protocol (LDP).

The no form of this command removes all LDP-related configuration.

Examples

Configuring LDP:

switch(config-mpls)# label-protocol ldp

Removing all LDP-related configuration:

switch(config-mpls)# no label-protocol ldp

All MPLS LDP configuration will be deleted.

Continue (y/n)? y

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls

Administrators or local user group members with execution righ
ts for this command.

label-range (static lsp)

Syntax

label-range <start-label-range> <end-label-range>

no label-range <start-label-range> <end-label-range>

Description

Allocates MPLS labels for use exclusively by static LSP.

Public

label-range (static lsp) 193

The no form of this command removes the configured allocation, returning to the default state with no labels
allocated for static LSP usage.

Parameter

Description

Selects the start of the static LSP label range. Range: 16‐104
8575.

Selects the end of the static LSP label range. Range: 16‐1048
575.

<start‐label‐range>

<end‐label‐range>

Usage

•  The range arguments are inclusive. Configuring a range of 20-30 will allocate the labels 20, 21, ..., 29,

30.

•  Static LSP labels must not overlap with labels used by any other protocol, i.e. LDP. This label range

allocation command will fail if any labels are shared between protocols.

•  Any change to the static LSP label allocation will fail if any static LSP bindings are configured. All

bindings must be removed before the static LSP label range can be reallocated.

•  Allocated label range affects only the ingress packets. Labels for the outgoing packets must be within

the allocated label range of the next hop device.

Examples

Allocating a valid static LSP label range:

switch(config-mpls-static-lsp)# label-range 100 2000

Changing the static LSP label range while LSP bindings are configured:

switch(config-mpls-static-lsp)# label-range 100 2000

All static LSP bindings must first be deleted.
Deallocating static LSP label range; use either command:

switch(config-mpls-static-lsp)# no label-range 100 2000

switch(config-mpls-static-lsp)# no label-range

Configuring a static LSP range that intersects with LDP:

switch(config-mpls-static-lsp)# label-range 30 99

 The static LSP label range cannot overlap with any other MPLS range.

Public

label-range (static lsp) 194

Deallocating static LSP range when bindings are still configured:

switch(config-mpls-static-lsp)# no label-range

 All static LSP bindings must be removed before removing the label range.

 All static LSP bindings must be removed before removing the label range.

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐
static‐lsp

Administrators or local user group members with execution righ
ts for this command.

mpls

Syntax

mpls

no mpls

Description

Configures MPLS forwarding of IPv4 traffic globally.

The no form of the command removes all MPLS-related configuration.

Examples

Configuring MPLS forwarding for IPv4 traffic:

switch(config)# mpls

Removing MPLS configuration for IPv4 traffic:

switch(config)# no mpls

All MPLS configuration will be deleted.

Public

mpls 195

Continue (y/n)? y

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config

Administrators or local user group members with execution righ
ts for this command.

mpls ldp discovery hello hold time (global)

Syntax

discovery hello holdtime <SECONDS>

no discovery hello holdtime <SECONDS>

Description

Configures MPLS LDP discovery hold time for peers found via hello packets.

The no form of this command resets the discovery hello hold time to its default value of 15 seconds.

Parameter

Description

Specifies the discovery hold time in seconds. Range: 15‐6553
5. Default: 15.

<SECONDS>

Usage

•  The default value of discovery hello hold time is 15 seconds

Public

mpls ldp discovery hello hold time (global) 196

•  The discovery hello hold time configured on an interface supersedes the global configuration.

•  The discovery hello interval time is auto-computed as one third of the hello hold time.

Examples

Configuring the MPLS LDP discovery hello hold time:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# discovery hello holdtime 30

Changing discovery hello hold time:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# discovery hello holdtime 50

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐ldp

Administrators or local user group members with execution righ
ts for this command.

mpls ldp discovery hello hold time (interface
)

Syntax

mpls ldp discovery hello holdtime <SECONDS>
no mpls ldp discovery hello holdtime <SECONDS>

Public

mpls ldp discovery hello hold time (interface) 197

Description

Overrides the global MPLS LDP discovery hold time for peers found via hello packets from the given
interface.

The no form of this command resets the discovery hello hold time for the given interface to the global value
(if configured) or default value of 15 seconds if global value is not specified.

Parameter

Description

Specifies the discover hello hold time on an interface. Range: 15
‐65535. Default: 15.

<SECONDS>

Usage

•  The interface LDP discovery hello hold time overrides global hello hold time.

•  Routing must be configured before changing the LDP discovery hold time on an interface.

Examples

Configuring the interface MPLS LDP discovery hello hold time:

switch(config)# interface 1/1/1

switch(config-if)# routing

switch(config-if)# mpls ldp discovery hello holdtime 30

Removing the interface MPLS LDP discovery hello hold time configuration:

switch(config)# interface 1/1/1

switch(config-if)# no mpls ldp discovery hello holdtime

Configuring the interface MPLS LDP discovery hello hold time on a Layer 2 interface:

switch(config)# interface 1/1/2

switch(config-if)# mpls ldp discovery hello holdtime 30

Routing must be enabled on this interface to use MPLS.

Command History

Release

10.09

Modification

Command introduced

Public

mpls ldp discovery hello hold time (interface) 198

Command Information

Platforms

Command context

Authority

8360

config‐if

Administrators or local user group members with execution righ
ts for this command.

mpls ldp enable

Syntax

mpls ldp enable

no mpls ldp enable

Description

Enables LDP protocol in the interface level.

The no form of this command disables LDP.

Enabling/disabling interface level LDP will also enable/disable php-mode-explicit-null by default. php-
mode-explicit-null is currently the only mode supported and there is no option to disable it when LDP is
enabled on an interface.

Usage

•  Routing must be configured before enabling LDP on an interface.

•  MPLS must be enabled on the interface prior to enabling LDP.

Examples

Enabling the LDP protocol:

switch(config)# interface 1/1/1

switch(config-if)# routing

switch(config-if)# mpls enable

switch(config-if)# mpls ldp enable

Enabling LDP prior to enabling MPLS:

switch(config)# interface 1/1/2
switch(config-if)# routing

switch(config-if)# mpls ldp enable

MPLS must be enabled on this interface to use LDP.

Public

mpls ldp enable 199

Enabling MPLS on a layer 2 interface:

switch(config)# interface 1/1/2

switch(config-if)# mpls ldp enable

Routing must be enabled on this interface to use MPLS.
Disabling MPLS forwarding:

switch(config)# interface 1/1/2

switch(config-if)# no mpls ldp enable

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐if

Administrators or local user group members with execution righ
ts for this command.

graceful-restart-timers (mpls ldp)

Syntax

graceful-restart-timers {forwarding-holding <SECONDS> | max-recovery
<SECONDS> | neighbor-liveness <SECONDS>}

no graceful-restart-timers {forwarding-holding <SECONDS> | max-recovery

<SECONDS> | neighbor-liveness <SECONDS>}

Description

Configures MPLS LDP discovery hold time for peers found via hello packets.

Public

graceful-restart-timers (mpls ldp) 200

The no form of this command resets the discovery hello hold time to its default value of 15 seconds.

NOTE

The BGP restart timer must be configured as 180 seconds or higher for graceful
restart to work with MPLS.

NOTE

It is recommended to configure the OSPF graceful restart timer as lower than the
LDP forward-holding timer, which in turn should be configured as lower than the
BGP graceful restart timer.

Parameter

Description

forwarding‐holding
<SECONDS>

max‐recovery <SECONDS>

neighbor‐liveness <SECONDS>

Specifies the amount of time in seconds that the MPLS forwardi
ng state should be preserved after the control plane restarts. Ra
nge: 30‐600. Default: 150.

Specifies the amount of time in seconds that the stale label bin
dings should be kept on the router after the LDP session has be
en reestablished. Range: 15‐600. Default: 120.

Specifies the amount of time in seconds that the router will wai
t for the LDP session to be reestablished. If the router cannot re
establish the LDP session within that time, the router deletes all
the stale LDP bindings received from that LDP neighbor. Range:
5‐300. Default: 120.

Examples

Configuring the MPLS LDP graceful restart forwarding holding time for 30 seconds:

switch(config)# mpls
switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# graceful-restart-timers forwarding-holding 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Resetting the MPLS LDP graceful restart forwarding holding time to default:

switch(config)# mpls
switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no graceful-restart-timers forwarding-holding

switch(config-mpls-ldp)# no graceful-restart-timers forwarding-holding 30

Public

graceful-restart-timers (mpls ldp) 201

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Configuring the MPLS LDP graceful restart max recovery time for 30 seconds:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# graceful-restart-timers max-recovery 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Resetting the MPLS LDP graceful restart max recovery time to default:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no graceful-restart-timers max-recovery

switch(config-mpls-ldp)# no graceful-restart-timers max-recovery 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Configuring the MPLS LDP graceful restart neighbor liveness timefor 30 seconds:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# graceful-restart-timers neighbor-liveness 30

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Resetting the MPLS LDP graceful restart neighbor liveness to default:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no graceful-restart-timers neighbor-liveness

Changing the timer value will restart any LDP sessions.

This may result in traffic loss.

Continue (y/n)? y

Public

graceful-restart-timers (mpls ldp) 202

Command History

Release

10.10

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐ldp

Administrators or local user group members with execution righ
ts for this command.

mpls ldp session holdtime (interface)

Syntax

mpls ldp session holdtime <TIME>

no mpls ldp session holdtime <TIME>

Description

Configures MPLS LDP session hold time for an interface.

The no form of this command resets the session hold time to its default value of 15 seconds.

Parameter

Description

Specifies the session hold time for the interface in seconds. Ran
ge: 15‐65535. Default: 40.

<TIME>

Usage

•  The interface LDP session hold time overrides global hello hold time.

•  Routing must be configured before changing LDP session holdtime on an interface.

Public

mpls ldp session holdtime (interface) 203

Examples

Configuring the MPLS LDP session hold time for an interface:

switch(config)# interface 1/1/1

switch(config-if)# routing

switch(config-if)# mpls ldp session holdtime 30

Removing the MPLS LDP session hold time for the interface:

switch(config)# interface 1/1/1

switch(config-if)# no mpls ldp session holdtime 30

Configuring the MPLS LDP session hold time on a layer 2 interface:

switch(config)# interface 1/1/2

switch(config-if)# mpls ldp session holdtime 30

Routing must be enabled on this interface to use MPLS.

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐if

Administrators or local user group members with execution righ
ts for this command.

ping mpls

Syntax

ping mpls ipv4 <IP-ADDR/MASK> [source <IP-ADDR> | destination <IP-ADDR> |

ttl <HOPS> |
size <BYTES> | repeat <NUMBER> | timeout <TIME> | interval <TIME>]

Public

ping mpls 204

Description

Ping MPLS is a command which sends LSP ping packets on the MPLS network and displays the responses
from the remote target. It is used as a debugging and analytics tool to verify connectivity within MPLS
networks.

Parameter

Description

ipv4 <IP‐ADDR/MASK>

Specifies target IP address and mask of the remote subnet to pi
ng.

source <IP‐ADDR>

Specifies the source IPv4 address for the request packet.

destination <IP‐ADDR>

Specifies the destination address for the request packet. Defaul
t: 127.0.0.1.

ttl <HOPS>

size <BYTES>

repeat <NUMBER>

timeout <TIME>

interval <TIME>

Examples

Specifies the max number of hops a packet can take en route to
its destination. Range: 1‐255. Default: 64.

Specifies the size of the packet to be sent in bytes. Range: 0‐9
600. Default: 0.

Specifies the number of packets to be sent. Range 1‐10000.
Default: 5.

Specifies the amount of time in seconds after which a packet is
considered dropped. Range 1‐60. Default: 2.

Specifies the interval time between packets in seconds. Range:
1‐60 seconds. Default: 1.

Sending 5 successful pings to the destination to the 10.10.10.10/32 subnet with a source IP address
20.20.20.1, a destination IP of 127.0.0.1, a zero byte payload, 64 hop time to live, 3 second interval
between packets, and a 5 second timeout:

switch# ping mpls ipv4 10.10.10.10/32 source 20.20.20.1 destination

127.0.0.1 repeat 5 size 0 ttl 64 interval 3 timeout 5

Sending 5 MPLS Echo packets of size 0 bytes to 10.10.10.0/32 from source

20.20.20.1,

timeout is 5 sec, send interval is 3 sec:

Codes: '!' - success, 'Q' - request not sent, '.' - timeout,

       'U' - unreachable, 'M' - malformed request, 'T' - unsupported TLV,
       'E' - malformed response, 'R' - transit router

Type escape sequence (Ctrl + C) to abort.

!!!!!

1908 Success rate is 100 percent (5/5), round-trip min/avg/max = 7/10/13 ms

Public

ping mpls 205

Sending an unsuccessful ping that fails because the network is unreachable:

switch# ping mpls ipv4 10.10.10.10/32 source 20.20.20.1 destination

127.0.0.1 repeat 5 size 0

Sending 5 MPLS Echo packets of size 0 bytes to 10.10.10.0/32 from source

20.20.20.1,

timeout is 2 sec, send interval is 1 sec:

Codes: '!' - success, 'Q' - request not sent, '.' - timeout,

       'U' - unreachable, 'M' - malformed request, 'T' - unsupported TLV,

       'E' - malformed response, 'R' - transit router

Type escape sequence (Ctrl + C) to abort.

Network unreachable

Command History

Release

10.10

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

router-id (mpls ldp)

Syntax

router-id <IFNAME> [confirm]

no router-id <IFNAME> [confirm]

Description

Configures MPLS LDP router ID which is the IP address of a loopback interface.

The no form of this command removes the MPLS LDP router ID configuration.

Public

router-id (mpls ldp) 206

Parameter

Description

Specifies the loopback interface for the MPLS LDP router ID.

<IFNAME>

Usage

•  There is a possibility of MPLS traffic disruption whenever a router ID is deleted or updated to another

loopback interface.

•  The MPLS router ID interface must be a loopback interface with an IPv4 address configured.

•  The confirmation prompt is skipped if the router ID is being configured for the first time by the user.

•  Changing the IP address of the loopback interface may interrupt MPLS traffic.

Examples

Configuring an MPLS LDP router ID:

switch(config)# interface loopback 1

switch(config-loopback-if)# ip address 1.1.1.1/32

switch(config)# mpls

switch(config-mpls)# enable

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# enable

switch(config-mpls-ldp)# router-id loopback1

Changing the MPLS LDP router ID loopback interface:

switch(config)# interface loopback 2

switch(config-loopback-if)# ip address 2.2.2.2/32
switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# router-id loopback2

Changing the router ID interface may disrupt MPLS traffic.

Continue (y/n)?
Changing the MPLS LDP router ID interface without prompting for confirmation:

switch(config)# interface loopback 2
switch(config-loopback-if)# ip address 2.2.2.2/24
switch(config)# mpls

switch(config-mpls)# label-protocol ldp

Public

router-id (mpls ldp) 207

switch(config-mpls-ldp)# router-id loopback2 confirm

Removing the MPLS LDP router ID configuration:

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no router-id loopback2

Removing the router ID interface may disrupt MPLS traffic.

Continue (y/n)?
Removing the MPLS LDP router ID without providing loopback interface name:

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no router-id

Removing the router ID interface may disrupt MPLS traffic.

Continue (y/n)?
Removing the configuration of an MPLS LDP router ID with an interface name which is different than the one
configured as router ID:

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# router-id loopback1 confirm

switch(config-mpls-ldp)# no router-id loopback2

The value to disable does not match the currently configured value.
Removing the MPLS LDP router ID configuration prompting for confirmation:

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# no router-id loopback2 confirm

Configuring an MPLS LDP router ID with system interface:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# enable

switch(config-mpls-ldp)# router-id 1/1/1

The router ID must be a loopback interface with an IP address assigned.
Configuring MPLS LDP router ID with a loopback interface without an IPv4 address configured:

switch(config)# interface loopback 1

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# enable

switch(config-mpls-ldp)# router-id loopback1

The router ID interface must have an IP address assigned.

Public

router-id (mpls ldp) 208

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐
loopback‐if
config‐mpls‐ldp

Administrators or local user group members with execution righ
ts for this command.

session hold time (mpls ldp globally)

Syntax

session holdtime <SECONDS>

no session holdtime <SECONDS>

Description

Configures MPLS LDP session hold time.

The no form of this command resets the session hold time to its default value of 40 seconds.

Parameter

Description

Specifies the session hold time in seconds. Range: 15‐65535.
Default: 40.

<SECONDS>

Usage

•  The default session hold time is 40 seconds

•  The session hold time configured on an interface supersedes the global configuration.

•  The session keepalive interval time is auto computed as one sixth of the hold time.

Public

session hold time (mpls ldp globally) 209

Examples

Configuring the MPLS LDP session hold time:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(config-mpls-ldp)# session holdtime 30

Changing the session hold time:

switch(config)# mpls

switch(config-mpls)# label-protocol ldp

switch(switch(config-mpls-ldp)# session holdtime 50)# session holdtime 50

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls‐ldp

Administrators or local user group members with execution righ
ts for this command.

show bgp vpnv4 unicast

Syntax

show bgp VPNv4 unicast [[<IP-ADDR>/<MASK>] | community | extcommunity |

neighbors [<IP-ADDR>] | paths | summary | vsx-peer]

Description

Shows all vpnv4 entries in the BGP routing table .

Public

show bgp vpnv4 unicast 210

Parameter

Description

Specifies the IP network and mask of a specific BGP route in IPv
4 format (x.x.x.x/M), where x is a decimal number from 0 to 255
and M is the number of bits in CIDR format from 0 to 32.

Selects routes that belong to specified BGP communities.

Selects unicast routes with extended communities.

Selects BGP neighbor connection parameters for all neighbors
or the IP address of a specific neighbor in IPv4 format (x.x.x.x)
where x is a decimal number from 0 to 255.

Selects AS Path information of the vpnv4 routes in BGP RIB.

Selects a summary of BGP neighbor status.

Selects VSX peer switch information.

<IP‐ADDR>/<MASK>

community

extcommunity

neighbors [<IP‐ADDR>]

paths

summary

vsx‐peer

Examples

Showing all VPNv4 entries in the BGP routing table:

switch# show bgp vpnv4 unicast

VRF : default

BGP Summary

-----------

 Local AS               : 100          BGP Router Identifier  : 4.4.4.4

 Peers                  : 0            Log Neighbor Changes   : No

 Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

 Confederation Id       : 0

PE2# show bgp vpnv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 4.4.4.4

    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 100:100              (Label 22)

*>i 11.1.1.0/30        1.1.1.1         0          100        0       ?

Route Distinguisher: 1.1.1.1:200          (Label 23)

*>i 11.1.2.0/30        1.1.1.1         0          100        0       ?

Public

show bgp vpnv4 unicast 211

Route Distinguisher: 100:300              (Label 24)

*>i 11.1.3.0/30        1.1.1.1         0          100        0       ?

Route Distinguisher: 100:400              (Label 25)

*>i 11.1.4.0/30        1.1.1.1         0          100        0       ?

Total number of entries 4
Showing entries in the BGP routing table for the 11.1.3.0/30 network:

switch# show bgp vpnv4 unicast 11.1.3.0/30

VRF : default

BGP Local AS 100         BGP Router-id 4.4.4.4

   Network           : 11.1.3.0/30               Nexthop             :

1.1.1.1

   Peer              : 1.1.1.1                   Origin              :

incomplete

   Metric            : 0                         Local Pref          : 100

   Weight            : 0                         Calc. Local Pref    : 100

   Best              : Yes                       Valid               : Yes

   Type              : internal                  Stale               : No

   Originator ID     : 0.0.0.0                   Path ID             : 0

   Aggregator ID     :

   Aggregator AS     :

   Atomic Aggregate  :

   AS-Path           :

   Cluster List      :

   Communities       :

   Ext-Communities   :
Showing entries in the BGP routing table for routes with extended communities:

switch# show bgp vpnv4 unicast extcommunity

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete
VRF : default

Local Router-ID 4.4.4.4

    Network             Next Hop           Ecommunity

*>i 11.1.1.0/30         1.1.1.1            100:100

*>i 11.1.2.0/30         1.1.1.1            4.4.4.4:200

*>i 11.1.3.0/30         1.1.1.1            100:300

*>i 11.1.4.0/30         1.1.1.1            100:400

Total number of entries 4
Showing BGP neighbor connection parameters for all neighbors:

switch# show bgp vpnv4 unicast neighbors

Codes: ^ Inherited from peer-group

Public

show bgp vpnv4 unicast 212

VRF : default

BGP Neighbor 1.1.1.1 (Internal)

    Description         : MPBGP Session to PE2

    Peer-group          :

    Remote Router Id    : 1.1.1.1            Local Router Id    : 4.4.4.4

    Remote AS           : 100                Local AS           : 100

    Remote Port         : 179                Local Port         : 38335

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:56m:46s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

    Notification                 0        0

    Updates                      7        7

    Keepalives                  64       65

    Route Refresh                0        0
    Total                       72       73

    Capability                           Advertised      Received

    -----------                          -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

Public

show bgp vpnv4 unicast 213

Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 32500               Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :
Showing BGP neighbor connection parameters for the neighbor with IP address 1.1.1.1:

switch# show bgp vpnv4 unicast neighbors 1.1.1.1

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 1.1.1.1 (Internal)

    Description         : MPBGP Session to PE2

    Peer-group          :

    Remote Router Id    : 1.1.1.1            Local Router Id    : 4.4.4.4

    Remote AS           : 100                Local AS           : 100

    Remote Port         : 179                Local Port         : 38335

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      : loopback0

    Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:58m:52s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : No Error

    Last SubErr Sent    : No Error

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

    Graceful-Restart    : Enabled            Gr. Restart Time   : 120

    Gr. Stalepath Time  : 300                Remove Private-AS  : No

    TTL                 : 255                Local Cluster-ID   :

    Weight              : 0                  Fall-over          : No

    Confederation-Peers : No

    Message statistics        Sent     Rcvd

    -------------------      -----    -----

    Open                         1        1

Public

show bgp vpnv4 unicast 214

Notification                 0        0

    Updates                      7        7

    Keepalives                  67       67

    Route Refresh                0        0

    Total                       75       75

    Capability                           Advertised      Received

    -----------                          -----------     ----------

    Route Refresh                        Yes             Yes

    Graceful Restart                     Yes             Yes

    Add-Path                             No              No

    Four Octet ASN                       Yes             Yes

    Address family IPv4 Unicast          No              No

    Address family IPv6 Unicast          No              No

    Address family VPNv4 Unicast         Yes             Yes

    Address family L2VPN EVPN            No              No

    Address Family : VPNv4 Unicast

    ------------------------------

    Rt. Reflect. Client : No                  Send Community    : both

    Allow-AS in         : 0                   Advt. Interval    : 30

    Max. Prefix         : 32500               Soft Reconfig In  :

    Nexthop-Self        :                     Default-Originate :

    Cfg. Add-Path       :

    Neg. Add-Path       :

    Routemap In         :

    Routemap Out        :

    ORF type            : Prefix-list

    ORF capability      :
Showing AS Path information of the vpnv4 routes in BGP RIB:

switch# show bgp vpnv4 unicast paths

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

VRF : default

Local Router-ID 4.4.4.4

    Network            Next Hop        PathID      Path

Route Distinguisher: 100:100              (Label 22)

* i 11.1.1.0/30        1.1.1.1         0            ?

Route Distinguisher: 1.1.1.1:200          (Label 23)

* i 11.1.2.0/30        1.1.1.1         0            ?

Route Distinguisher: 100:300              (Label 24)

* i 11.1.3.0/30        1.1.1.1         0            ?

Route Distinguisher: 100:400              (Label 25)

Public

show bgp vpnv4 unicast 215

* i 11.1.4.0/30        1.1.1.1         0            ?

Total number of entries 4
Showing a summary of BGP neighbor status:

switch(config-bgp)# show bgp vpnv4 unicast summary

VRF : default

BGP Summary

Local AS               : 100          BGP Router Identifier  : 4.4.4.4

Peers                  : 0            Log Neighbor Changes   : No

Cfg. Hold Time         : 180          Cfg. Keep Alive        : 60

Confederation Id       : 0

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

show capacities mpls

Syntax

show capacities mpls

show capacities-status mpls

Description

For capacities command, shows the maximum number of label endpoints, label switch entries, and service
label entries that can be configured on the device. For capacities-status command, shows the total number
of label endpoints, label switch entries, and service label entries that are currently configured on the device.

Examples

Showing capacities of configurable MPLS options:

Public

show capacities mpls 216

switch# show capacities mpls

System Capacities: Filter MPLS

Capacities

Name

                       Value

----------------------------------------------------------------------------

---------------------------------------

Maximum number of MPLS Label Endpoints configurable in a

system                                                8192

Maximum number of MPLS Label Switch entries configurable in a

system                                           8192

Maximum number of MPLS Service Label entries configurable in a

system                                          8192
Showing the configuration of currently configured MPLS options in relation to their capacities:

switch# show capacities-status mpls

System Capacities Status: Filter MPLS

Capacities Status

Name

               Value Maximum

----------------------------------------------------------------------------

-------------

Number of MPLS Label Endpoints currently

configured

0    8192

Number of MPLS Label Switch entries currently

configured                                                         0    8192

Number of MPLS Service Label entries currently

configured                                                        0    8192

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Manager ( # )

Administrators or local user group members with execution righ
ts for this command.

Public

show capacities mpls 217

show mpls forwarding

Syntax

show mpls forwarding [detail]

Description

Shows the MPLS forwarding table.

Usage

•  Forwarding table filters will be implemented at a later date.

•  When running this command on a huge-scale setup, showing the full tables might take a while.

Examples

Showing the MPLS forwarding table:

switch# show mpls forwarding

MPLS Bindings

Entry Bindings   : 2

Exit Bindings    : 2

Transit Bindings : 1

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin   Prefix              Ingress           Nexthop

Outgoing  Egress        Egress            Status

                             VRF               Address

Label     Interface     VRF

----------------------------------------------------------------------------

---------------------------------------------

LDP      4.4.4.4/32          default           192.168.10.2

3002      1/1/6         default           operational

BGP      20.20.20.0/24       vrf-blue          4.4.4.4

5001      1/1/6         default           operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

Label     Label     VRF

----------------------------------------------------------------------------

---

Public

show mpls forwarding 218

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  2001      vrf-blue

operational

Transit Bindings:

Origin  Prefix       Incoming  Egress     Egress   Nexthop        Outgoing

Status

                     Label     Interface  VRF      Address        Label

----------------------------------------------------------------------------

-----------

LDP     4.4.4.4/32   2002      1/1/6      default  192.168.10.2   3002

operational

switch# show mpls forwarding detail

MPLS Bindings

Entry Bindings   : 2

Exit Bindings    : 2

Transit Bindings : 1

PHP Mode         : Explicit-Null

QoS Mode         : Uniform

TTL Propagation  : Uniform

Entry Bindings:

Origin   Prefix              Ingress           Nexthop

Outgoing  Egress        Egress            Status                 Tx

Packets             Tx Bytes

VRF               Address             Label     Interface     VRF

----------------------------------------------------------------------------

----------------------------------------------------------------------------

-----------

LDP      4.4.4.4/32          default           192.168.10.2

3002      1/1/6         default           operational

99                  100

BGP      20.20.20.0/24       vrf-blue          4.4.4.4
5001      1/1/6         default           operational

66                   88

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress

Status                 Rx Packets             Rx Bytes

Label     Label     VRF

----------------------------------------------------------------------------

---------------------------------------------

static   n/a                 exp-null  -         default

operational                    33                   44

BGP      n/a                 imp-null  2001      vrf-blue

Public

show mpls forwarding 219

operational                    22                   33

Transit Bindings:

Origin   Prefix              Incoming  Egress        Egress

Nexthop             Outgoing  Status                 Rx Packets

Rx Bytes           Tx Packets             Tx Bytes

Label     Interface     VRF               Address             Label

----------------------------------------------------------------------------

----------------------------------------------------------------------------

---------------------------------------------

LDP      4.4.4.4/32          2002      1/1/6         default

192.168.10.2        3002      operational

11                   22                   22                   33

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

show mpls label-range static-lsp

Syntax

show mpls label-range static-lsp

Description

Shows the range of MPLS labels allocated for use in static LSP bindings and the range of labels currently
used by static LSP bindings.

Examples

Showing the range and usage of static LSp labels on the switch:

Public

show mpls label-range static-lsp 220

switch# show mpls label-range static-lsp

     Static LSP Labels

       Allocated : 16-100

       In use    : 16-30,35

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show mpls ldp bindings

Syntax

show mpls ldp bindings

Description

Shows information about all MPLS LDP bindings.

Examples

Showing information about MPLS LDP bindings:

switch# show mpls ldp bindings

10.10.2.0/24

        local binding: label: imp-null

        remote binding: lsr:10.255.255.255:0, label:16

        remote binding: lsr:10.256.256.256:0, label: exp-null
10.10.3.0/24

        local binding: label:20

        remote binding: lsr:10.256.256.256:0, label:22

5.43.9.98/32

Public

show mpls ldp bindings 221

local binding: label:21

        No remote binding

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

show mpls ldp discovery

Syntax

show mpls ldp discovery [<IP-ADDR>]

no syntax

Description

Shows information about discovered LDP peers.

Parameter

Description

Specifies the peer MPLS LDP router ID in x.x.x.x format, where
x is a decimal value from 0 to 255.

<IP‐ADDR>

Examples

Showing information about discovered LDP peers:

switch# show mpls ldp discovery

Local LDP Identifier: 10.44.44.44:0

Discovery Sources:

Public

show mpls ldp discovery 222

Interfaces:

         1/1/1 : recv

         LDP Id: 10.33.33.33:0, Transport address: 10.33.33.33

 Path vector limit: 10

 Distribution type: Downstream-on-demand

 Adjacency type: Link

 Hold time: 15 sec (local: 15 sec, peer: 15 sec, remaining: 10s)

 BFD status: Activating

         1/1/2 : recv

         LDP Id: 10.33.33.34:0, Transport address: 10.33.33.33

                 Path vector limit: 10

                 Distribution type: Downstream-unsolicited

 Adjacency type: Targeted

 Hold time: 15 sec (local: 15 sec, peer: 15 sec, remaining: 10s)

 BFD status: Active

Local LDP Identifier: 10.44.44.44:2

Discovery Sources:

    Interfaces:

        1/1/3 : recv

        LDP Id: 10.33.38.33:0, Transport address: 10.43.33.33

                Path vector limit: 10

Distribution type: Downstream-unsolicited

Adjacency type: Link

Hold time: 15 sec (local: 15 sec, peer: 15 sec, remaining: 10s)

BFD status: Active
Showingu information about a specific LDP peer:

switch# show mpls ldp discovery 10.33.33.34

Local LDP Identifier: 10.44.44.44:0

Discovery Sources:

    Interfaces:

        1/1/2 : recv

        LDP Id: 10.33.33.34:0, Transport address: 10.33.33.33

                Path vector limit: 10

Distribution type: Downstream-unsolicited

Adjacency type: Targeted

Hold time: 15 sec (local: 15 sec, peer: 15 sec, remaining: 10s)

BFD status: Active

Public

show mpls ldp discovery 223

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

show mpls ldp graceful-restart

Syntax

show mpls ldp graceful-restart

Description

Shows graceful restart parameters and status.

Examples

Showing graceful restart parameters and status when graceful restart is not configured:

switch# show mpls ldp graceful-restart

Max recovery time                      : 50 sec

Neighbor liveness time                 : 50 sec
Forwarding holding time                : 70 sec

Number of graceful restart events      : 7

Graceful restart in progress           : true

Forwarding holding time remaining      : 300 sec

Current graceful restart status        : in-progress

Graceful restart exit history (last 5) : complete, complete, complete,

cancelled, cancelled

Public

show mpls ldp graceful-restart 224

Command History

Release

10.10

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

8360

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

show mpls ldp neighbor

Syntax

show mpls ldp neighbor

Description

Shows information about LDP neighbors in the current session(s). The reconnect and recovery time are the
times advertised by the peer device.

Examples

Showing LDP neighbors:

switch# show mpls ldp neighbor

Local LDP Identifier: 10.44.44.44:0, Peer LDP Identifier: 10.22.22.22:0
    TCP connection: 10.22.22.22:646 - 10.33.33.33:65530

    Graceful Restart: No

    Session Holdtime: 180 sec

    State: Operational; Msgs sent/rcvd: 46/43

    Up time: 00:31:21

    LDP Discovery Sources: 1/1/1

    Addresses bound to this peer:

         10.22.22.22 10.10.2.1
Showing LDP neighbors when graceful restart has been configured:

switch# show mpls ldp neighbor

Local LDP Identifier: 1.1.1.1:0, Peer LDP Identifier: 11.1.1.2:0

Public

show mpls ldp neighbor 225

Graceful Restart: Yes

    Peer Reconnect Time: 120 sec

    Peer Recovery Time: 300 sec

    Session Holdtime: 40 sec

    Up time: 00:02:59

    State: operational

    LDP Discovery Sources: 1/1/32

    Addresses bound to this peer:

         11.1.1.2 12.1.1.1 2.2.2.2

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Operator ( > ) or Manage
r ( # )

Administrators or local user group members with execution righ
ts for this command.

static-lsp

Syntax

static-lsp
no static-lsp

Description

Configures MPLS static Label Switched Paths (LSP).

The no form of this command removes all static LSP configurations including label range allocation and
static LSP binding.

Examples

Configuring MPLS static LSP:

Public

static-lsp 226

switch(config-mpls)# static-lsp

Removing MPLS static LSP configuration:

switch(config-mpls)# no static-lsp

Command History

Release

10.09

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

config‐mpls

Administrators or local user group members with execution righ
ts for this command.

traceroute mpls

Syntax

traceroute mpls ipv4 <IP-ADDR/MASK> [source <IP-ADDR> | destination <IP-

ADDR> | ttl <HOPS> | timeout <TIME> | fec-type ldp]

Description

Send LSP ping packets on the MPLS network and display the responses all intermediate routers as well as
the destination host. Use this command as a debugging and analytics tool to verify connectivity within the
MPLS networks.

Parameter

Description

ipv4 <IP‐ADDR/MASK>

Specifies the IP address and netmask of the remote subnet to t
raceroute.

source <IP‐ADDR>

Specifies the source IPv4 address for the request packet.

destination <IP‐ADDR>

Specifies the destination IPv4 address for the request packet

Public

traceroute mpls 227

Parameter

ttl <HOPS>

Description

Specifies the max number of hops a packet can take en route to
its destination. Range: 1‐255. Default: 255.

timeout <SECONDS>

Specifies the number of seconds after which a packet is conside
red dropped. Range: 1‐60 seconds. Default: 2.

fec‐type ldp

Selects the target Forward Equivalence Class (FEC) type. The o
nly supported option is the default value of ldp.

Example

Successfully tracing the route a target with IP address 1.1.4.1/32 with a maximum TTL of 3 hops and a 3
second timeout:

switch# traceroute mpls ipv4 1.1.4.1/32 ttl 3 timeout 3

Tracing MPLS Label Switched Path to 1.1.4.1/32 from source 10.0.0.2,

timeout is 3 seconds and ttl is 3

Codes: '!' - success, 'Q' - request not sent, '.' - timeout, 'N' - no label

entry,

  'R' - transit router, 'D' - DS Map mismatch, 'F' - no FEC mapping,

  'M' - malformed request, ‘T' - unsupported tlvs, ‘Z' - return code 0

Type escape sequence to abort.

  0 10.0.0.2 MRU 1500 [Labels: 17]

R 1 10.0.0.1 MRU 1500 [Labels: explicit-null] 10 ms

! 2 10.0.1.2 1 ms

Command History

Release

10.10

Modification

Command introduced

Command Information

Platforms

Command context

Authority

8360

Manager (#)

Administrators or local user group members with execution righ
ts for this command.

Public

traceroute mpls 228

Debugging and troubleshooting

The following is recommended prior to beginning the troubleshooting process:

•  Have a topology diagram ready

•  Ensure IPs, interface, and AS details are included

•  Check physical cabling and generate  show tech  when opening a TAC case

•  Check network:

◦  Run show LLDP neighbor

◦  Ensure unicast network works using ping and traceroute between loopbacks and interfaces

◦  Fix any issues found

The figure below provides an example:

Mirror traffic and packet capture if required:

mirror session 1

    enable

    destination interface 1/1/40

    source interface 1/1/51 both
If requested by TAC engineer:

diagnostics

diag-dump mpls basic

debug mpls all

sh debug buffer

no debug all
The recommended MPLS troubleshooting flow is provided in the diagram below.

Public

Debugging and troubleshooting 229

Subtopics

Troubleshooting steps
Frequently asked questions

Troubleshooting steps

Follow the process outlines below to troubleshoot MPLS-related issues:

Step 1: Verify that MPLS configurations are correct

Refer to the Use cases section for CE, PE and P sample configurations.

Step 2: Check unicast routing between P/RR and PE

On PE, verify loopbacks from remote P and PE have been learned. If not seen, verify that OSPF is enabled
and advertising loopbacks on remote P and PE:

PE1# show ip route
Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

Public

Troubleshooting steps 230

IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix              Nexthop          Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

1.1.1.1/32          -                loopback0      -

L         [0/0]        -

2.2.2.2/32          30.0.0.2         1/1/38         -

O         [110/20]     00h:12m:32s

3.3.3.3/32          30.0.0.2         1/1/38         -

O         [110/10]     00h:12m:52s

30.0.0.0/24         -                1/1/38         -

C         [0/0]        -

30.0.0.1/32         -                1/1/38         -

L         [0/0]        -

30.1.0.0/24         30.0.0.2         1/1/38         -

O         [110/20]     00h:12m:52s

Total Route Count : 6

Step 3: Check LDP peering and MPLS bindings

Verify LDP neighbor is up:

PE1# show mpls ldp neighbor

Local LDP Identifier: 1.1.1.1:0, Peer LDP Identifier: 3.3.3.3:0

    Graceful Restart: No

    Session Holdtime: 40 sec

    Up time: 00:13:49

    State: operational
    LDP Discovery Sources: 1/1/38

    Addresses bound to this peer:

         3.3.3.3 30.0.0.2 30.1.0.1
Verify labels and MPLS bindings for remote P and PE exist:

PE1# show mpls ldp bindings

30.1.0.1/32

        No local binding
        remote binding: lsr:3.3.3.3:0 label: exp-null

1.1.1.1/32

        local binding: label: exp-null

        remote binding: lsr:3.3.3.3:0 label:16

Public

Troubleshooting steps 231

30.0.0.1/32

        local binding: label: exp-null

        No remote binding

30.0.0.2/32

        No local binding

        remote binding: lsr:3.3.3.3:0 label: exp-null

3.3.3.3/32

        local binding: label: 17

        remote binding: lsr:3.3.3.3:0 label: exp-null

2.2.2.2/32

        local binding: label: 18

        remote binding: lsr:3.3.3.3:0 label:17

If the bolded examples are not seen, verify that remote PE has LDP established.

Step 4: Check MPLS forwarding table

Verify nexthop, labels, and routes exist for remote VPNv4 (outgoing label 18) and PE (outgoing label 17):

PE1# show mpls forwarding

MPLS Bindings

Entry Bindings   : 4

Exit Bindings    : 3

Transit Bindings : 2

Entry Bindings:

Origin  Prefix         Ingress   Nexthop    Outgoing  Egress      Egress

Status

                       VRF       Address    Label     Interface

VRF

----------------------------------------------------------------------------

----------

LDP   2.2.2.2/32    default   30.0.0.2   17        1/1/38      default
operational

LDP   3.3.3.3/32    default   30.0.0.2   exp-null  1/1/38      default

operational

BGP   20.2.0.0/24    vrf_1     2.2.2.2   18        1/1/38      default

operationalBGP   201.0.0.0/24   vrf_1     2.2.2.2   18        1/1/38

default   operational

Exit Bindings:

Origin   Prefix              Incoming  Service   Egress            Status

                             Label     Label     VRF

----------------------------------------------------------------------------

---

Public

Troubleshooting steps 232

static   n/a                 exp-null  -         default

operational

BGP      n/a                 imp-null  16        vrf_1

operational

static   n/a                 7         -         default

operational

Step 5: Check MP-BGP VPNv4 peering between PE/RR

Verify that MP-BGP VPNv4 peering is established. If it’s down, verify and fix network reachability between
source and destination peering IPs.

PE1# show bgp vpnv4 un neighbors

Codes: ^ Inherited from peer-group

VRF : default

BGP Neighbor 3.3.3.3 (Internal)

Description         :

    Peer-group          :

    Remote Router Id    : 3.3.3.3            Local Router Id    :

1.1.1.1

    Remote AS           : 200                Local AS           :

200

    Remote Port         : 43923              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 2                  Conn. Dropped      : 1

    Passive             : No                 Update-Source      : loopback0

Step 6: Check peering between PE and CE

Verify EBGP peering to CE on the PE

PE1# show bgp vrf vrf_1 ipv4 unicast neighbors

Codes: ^ Inherited from peer-group

VRF : vrf_1

BGP Neighbor 20.1.0.1 (External)

    Description         :

    Peer-group          :

    Remote Router Id    : 20.1.0.1           Local Router Id    : 20.1.0.2

    Remote AS           : 100                Local AS           : 200

    Remote Port         : 51588              Local Port         : 179

    State               : Established        Admin Status       : Up

    Conn. Established   : 1                  Conn. Dropped      : 0

    Passive             : No                 Update-Source      :

Public

Troubleshooting steps 233

Cfg. Hold Time      : 180                Cfg. Keep Alive    : 60

    Neg. Hold Time      : 180                Neg. Keep Alive    : 60

    Up/Down Time        : 00h:20m:28s        Connect-Retry Time : 120

    Local-AS Prepend    : No                 Alt. Local-AS      : 0

    BFD                 : Disabled

    Password            :

    Last Err Sent       : Cease

    Last SubErr Sent    : Administrative Shutdown

    Last Err Rcvd       : No Error

    Last SubErr Rcvd    : No Error

Step 7: Check connectivity between PEs and between CEs

Ping from CE to remote CE WAN and LAN to verify MPLS L3 VPN connectivity:

CE1# ping 20.2.0.2

PING 20.2.0.2 (20.2.0.2) 100(128) bytes of data.

108 bytes from 20.2.0.2: icmp_seq=1 ttl=61 time=0.307 ms

108 bytes from 20.2.0.2: icmp_seq=2 ttl=61 time=0.328 ms

108 bytes from 20.2.0.2: icmp_seq=3 ttl=61 time=0.340 ms

108 bytes from 20.2.0.2: icmp_seq=4 ttl=61 time=0.335 ms

108 bytes from 20.2.0.2: icmp_seq=5 ttl=61 time=0.354 ms
Traceroute from CE to remote CE to verify the hop information over MPLS L3 VPN:

CE1# traceroute 20.2.0.2

traceroute to 20.2.0.2 (20.2.0.2), 1 hops min, 30 hops max, 3 sec. timeout,

3 probes

  1   20.1.0.2  0.177ms  0.121ms  0.087ms

  2   30.0.0.2  0.233ms  0.120ms  0.122ms

  3   30.1.0.2  0.260ms  0.123ms  0.125ms

  4   20.2.0.2  0.189ms  0.149ms  0.144ms
Ping from PE to remote PE to verify MPLS L3 VPN connectivity:

PE1# ping 20.2.0.1 vrf vrf_1
PING 20.2.0.1 (20.2.0.1) 100(128) bytes of data.

108 bytes from 20.2.0.1: icmp_seq=1 ttl=60 time=0.334 ms

108 bytes from 20.2.0.1: icmp_seq=2 ttl=60 time=0.279 ms

108 bytes from 20.2.0.1: icmp_seq=3 ttl=60 time=0.280 ms

108 bytes from 20.2.0.1: icmp_seq=4 ttl=60 time=0.315 ms

108 bytes from 20.2.0.1: icmp_seq=5 ttl=60 time=0.291 ms

--- 20.2.0.1 ping statistics ---

5 packets transmitted, 5 received, 0% packet loss, time 4091ms

rtt min/avg/max/mdev = 0.279/0.299/0.334/0.021 ms
Traceroute from PE to remote PE to verify hop information over MPLS L3 VPN:

Public

Troubleshooting steps 234

PE1# traceroute 20.2.0.1 vrf vrf_1

traceroute to 20.2.0.1 (20.2.0.1), 1 hops min, 30 hops max, 3 sec. timeout,

3 probes

  1   30.0.0.2  0.224ms  0.156ms  0.158ms

  2   30.1.0.2  0.186ms  0.138ms  0.136ms

  3   20.2.0.1  0.160ms  0.147ms  0.127ms

Step 8: Check VRF tables at ingress PE for EBGP routes

On ingress PE, verify that routes from both the connected CE and remote PE are learned. If the expected
route is not learned, check if the CE and remote PE are learning and advertising routes. In the example
below, 20.2.0.0/24 is the route from the remote PE and 101.0.0.0/24 is the route from the directly
connected CE:

PE1# show ip rib vrf vrf_1

Displaying ipv4 routes in RIB

Origin Codes: R - RIP, O - OSPFv2, B - BGP

              C - connected, S - static, L - local

Type Codes:   E - External BGP, I - Internal BGP

              IA - OSPF inter area, ia - OSPF intra area

              E1 - OSPF external type 1, E2 - OSPF external type 2

              EV - BGP EVPN, V - BGP VPN

* indicates selected for forwarding

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

*20.1.0.0/24         -                 1/1/37        -             C

[0/0]        -

*20.1.0.2/32         -                 1/1/37        -             L
[0/0]        -

*20.2.0.0/24         2.2.2.2           -             -             B/V

[200/0]      00h:24m:27s

*101.0.0.0/24        20.1.0.1          -             -             B/E

[20/0]       00h:14m:53s

*201.0.0.0/24        2.2.2.2           -             -             B/V

[200/0]      00h:14m:50s

Total Route Count : 5

PE1# show ip route vrf vrf_1

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Public

Troubleshooting steps 235

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: vrf_1

Prefix              Nexthop          Interface     VRF(egress)   Origin/

Distance/    Age

                                                                 Type

Metric

----------------------------------------------------------------------------

------------------

20.1.0.0/24         -                1/1/37        -             C

[0/0]        -

20.1.0.2/32         -                1/1/37        -             L

[0/0]        -

20.2.0.0/24         2.2.2.2          1/1/38        default       B/V

[200/0]      00h:26m:51s

101.0.0.0/24        20.1.0.1         1/1/37        -             B/E

[20/0]       00h:11m:42s

201.0.0.0/24        2.2.2.2          1/1/38        default       B/V

[200/0]      00h:11m:42s

Total Route Count : 5

Step 9: Check VPNv4 routes at egress PE for EBGP routes

Verify CE LAN routes appear in the output:

PE2# show bgp vpnv4 unicast

Status codes: s suppressed, d damped, h history, * valid, > best, =

multipath,

              i internal, e external S Stale, R Removed, a additional-paths

Origin codes: i - IGP, e - EGP, ? - incomplete

VRF : default

Local Router-ID 2.2.2.2
    Network            Nexthop         Metric     LocPrf     Weight Path

Route Distinguisher: 1:1                  (Label 16)

*>i 20.1.0.0/24        1.1.1.1         0          100        0       ?

Route Distinguisher: 1:2                  (Label 16)

*>  20.2.0.0/24        0.0.0.0         0          100        0       ?

Route Distinguisher: 1:1                  (Label 16)
         * > i 101.0.0.0/24       1.1.1.1         0          100
0       100 i

Route Distinguisher: 1:2                  (Label 16)

         * >   201.0.0.0/24       0.0.0.0         0          100

Public

Troubleshooting steps 236

0       100 i

Total number of entries 4

Step 10: Check VRF tables at egress PE for EBGP routes

Verify CE LAN routes appear in the output:

PE2# show ip rib vrf vrf_1

Displaying ipv4 routes in RIB

Origin Codes: R - RIP, O - OSPFv2, B - BGP

              C - connected, S - static, L - local

Type Codes:   E - External BGP, I - Internal BGP

              IA - OSPF inter area, ia - OSPF intra area

              E1 - OSPF external type 1, E2 - OSPF external type 2

              EV - BGP EVPN, V - BGP VPN

* indicates selected for forwarding

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric

----------------------------------------------------------------------------

------------------

*20.1.0.0/24         1.1.1.1           -             -             B/V

[200/0]      00h:23m:48s

*20.2.0.0/24         -                 1/1/26        -             C

[0/0]        -

*20.2.0.1/32         -                 1/1/26        -             L

[0/0]        -

*101.0.0.0/24        1.1.1.1           -             -             B/V

[200/0]      00h:14m:14s

*201.0.0.0/24        20.2.0.2          -             -             B/E

[20/0]       00h:14m:12s
Total Route Count : 5

PE2# show ip route vrf vrf_1

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: vrf_1

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

Public

Troubleshooting steps 237

Type

Metric

----------------------------------------------------------------------------

------------------

20.1.0.0/24         1.1.1.1          1/1/25        default

B/V       [200/0]      00h:21m:20s

20.2.0.0/24         -                1/1/26        -

C         [0/0]        -

20.2.0.1/32         -                1/1/26        -

L         [0/0]        -

101.0.0.0/24        1.1.1.1          1/1/25        default

B/V       [200/0]      00h:11m:46s

201.0.0.0/24        20.2.0.2         1/1/26        -

B/E       [20/0]       00h:11m:44s

Total Route Count : 5

Step 11: Check CE routing table

Check routes on CE and verify that remote CE routes have been learned. In the output below, 20.2.0.0/24 is
the remote CE WAN subnet and 201.0.0.0/24 is the remote CE LAN subnet:

CE1# show ip route

Displaying ipv4 routes selected for forwarding

Origin Codes: C - connected, S - static, L - local

              R - RIP, B - BGP, O - OSPF

Type Codes:   E - External BGP, I - Internal BGP, V - VPN, EV - EVPN

              IA - OSPF internal area, E1 - OSPF external type 1

              E2 - OSPF external type 2

VRF: default

Prefix               Nexthop           Interface     VRF(egress)   Origin/

Distance/    Age

                                                                   Type

Metric
----------------------------------------------------------------------------

------------------

20.0.0.0/24         -                1/1/43        -

C         [0/0]        -

20.0.0.2/32         -                1/1/43        -

L         [0/0]        -

20.1.0.0/24         -                1/1/44        -

C         [0/0]        -

20.1.0.1/32         -                1/1/44        -

L         [0/0]        -

20.2.0.0/24         20.1.0.2         1/1/44        -

Public

Troubleshooting steps 238

B/E       [20/0]       00h:13m:15s

101.0.0.0/24        20.0.0.1         1/1/43        -

B/I       [200/0]      00h:01m:10s

101.0.1.0/24        20.0.0.1         1/1/43        -

B/I       [200/0]      00h:01m:10s

101.0.2.0/24        20.0.0.1         1/1/43        -

B/I       [200/0]      00h:01m:10s

101.0.3.0/24        20.0.0.1         1/1/43        -

B/I       [200/0]      00h:01m:10s

101.0.4.0/24        20.0.0.1         1/1/43        -

B/I       [200/0]      00h:01m:12s

201.0.0.0/24        20.1.0.2         1/1/44        -

B/E       [20/0]       00h:01m:12s

201.0.1.0/24        20.1.0.2         1/1/44        -

B/E       [20/0]       00h:01m:12s

201.0.2.0/24        20.1.0.2         1/1/44        -

B/E       [20/0]       00h:01m:12s

201.0.3.0/24        20.1.0.2         1/1/44        -

B/E       [20/0]       00h:01m:12s

201.0.4.0/24        20.1.0.2         1/1/44        -

B/E       [20/0]       00h:01m:12s

Total Route Count : 15

Frequently asked questions

1. Can L2 subnets be extended across an MPLS L3 VPN network?

No, only L3 routing between CEs is supported across MPLS L3 VPN network. VXLAN can be used on CEs to
provide L2 subnet stretching over the MPLS L3 VPN network.

2. Is multicast and IPv6 routing and supported across an MPLS L3 VPN network with 10.09?

No, 10.09 MPLS L3 VPN only supports IPv4 unicast routing. VXLAN can be used on CEs to provide
multicast and IPv6 routing over the MPLS L3 VPN network.

3. Is VSX required on PEs for high availability?

VSX is not required on PEs as L3 routing across 2 standalone PEs (from a dual homed CE) provides PE
redundancy.

4. How does the L3VPN solution enable site redundancy?

Site redundancy can be achieved using dual standalone PE devices connected to the site CE device that
requires redundancy instead of using the PE devices in VSX mode. In order to ensure optimal best path
selection, BGP configurations should implemented as explained in the examples above with same RD
configurations on both PE devices.

Public

Frequently asked questions 239

5. Are non-L3VPN forwarding deployments supported?

Non-L3VPN forwarding deployments are supported with static LSP. Please refer to the l sp label imposition
command for configuration details. LDP/BGP need to be configured on devices as explained in the examples
above for all L3VPN deployments.

6. Why is BGP peer establishment failing with a non-HPE Aruba Networking device as PE and HPE
Aruba Networking P device as a router?

It is important to make sure that explicit-null is correctly configured on the non-HPE Aruba Networking
PE device for forwarding between the HPE Aruba Networking P device and non-HPE Aruba Networking
PE device. The HPE Aruba Networking P device requires proper explicit-null configuration for LDP label
distribution. This enables BGP session establishment through the MPLS core.

7. Why is BGP peer establishment causing intermittent flaps in the MPLS domain?

Make sure that all interfaces that are enabled for MPLS are also configured to support jumbo frames. If
MPLS-enabled interfaces do not support jumbo frames it's possible that the BGP route exchanges could be
bigger than the configured MTU. Configuring jumbo frame support across the MPLS domain will prevent any
traffic interruptions due to BGP session flaps.

8. Are IP/ICMP Ping IP options and dual homing supported with MPLS?

Packets over MPLS with IP options will get dropped. Ping or traceroute over MPLS paths on a dual-home
network will fail and packets would be dropped.

Support and Other Resources

Access HPE Aruba Networking support and updates, and view warranty and regulatory information

Subtopics

Accessing HPE Aruba Networking Support
Accessing Updates
Warranty Information
Regulatory Information
Documentation Feedback

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.hpe.com/us/en/networking/hpe‐aru
ba‐networking‐support‐services.html

Public

Support and Other Resources 240

AOS‐CX Switch Software Documentation Portal

https://arubanetworking.hpe.com/techdocs/Aruba
DocPortal/content/new-portal/aoscx.html

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1‐800‐943‐4526 (US & Canada Toll‐Free Nu
mber)

+1‐650‐750‐0350 (Backup—Toll Number)

International telephone

https://www.hpe.com/psnow/doc/a50011948enw

Be sure to collect the following information before contacting Support:

•  Technical support registration number (if applicable)

•  Product name, model or version, and serial number

•  Operating system name and version

•  Firmware version

•  Error messages

•  Product-specific reports and logs

•  Add-on products or components

•  Third-party products or components

Other useful sites

Other websites that can be used to find information:

HPE Aruba Networking Developer Hub

https://developer.arubanetworks.com/hpe‐aruba
‐networking‐aoscx/docs/about

Airheads social forums and Knowledge Base

https://community.arubanetworks.com/

AOS‐CX Software Technical Update channel on You
Tube.

Videos on new features introduced in this release
: https://www.youtube.com/playlist?list=PLsYGHu
NuBZcbWPEjjHuVMqP‐Q_UL3CskS

HPE Aruba Networking Hardware Documentation an
d Translations Portal

Public

Accessing HPE Aruba Networking Support 241

HPE Aruba Networking software

https://networkingsupport.hpe.com/downloads h
ttps://networkingsupport.hpe.com/downloads

Software licensing and Feature Packs

https://licensemanagement.hpe.com/

End‐of‐Life information

https://networkingsupport.hpe.com/end‐of‐life

Accessing Updates

You can access updates from the HPE Aruba Networking Support Portal at https://
networkingsupport.hpe.com.

Some software products provide a mechanism for accessing software updates through the product interface.
Review your product documentation to identify the recommended software update method.

To subscribe to eNewsletters and alerts:

https://networkingsupport.hpe./notifications/subscriptions (requires an active HPE Aruba Networking
Support Portal account to manage subscriptions). Security notices are viewable without an HPE Aruba
Networking Support Portal account.

Warranty Information

To view warranty information for your product, go to https://www.arubanetworks.com/support-services/
product-warranties/.

Regulatory Information

To view the regulatory information for your product, view the Safety and Compliance Information for
Server, Storage, Power, Networking, and Rack Products, available at https://www.hpe.com/support/Safety-
Compliance-EnterpriseProducts

Additional regulatory information

HPE Aruba Networking is committed to providing our customers with information about the chemical
substances in our products as needed to comply with legal requirements, environmental data (company
programs, product recycling, energy efficiency), and safety information and compliance data, (RoHS and

Public

Accessing Updates 242

WEEE). For more information, see https://www.arubanetworks.com/company/about-us/environmental-
citizenship/.

Documentation Feedback

HPE Aruba Networking is committed to providing documentation that meets your needs. To help us improve
the documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition, and
publication date located on the front cover of the document. For online help content, include the product
name, product version, help edition, and publication date located on the legal notices page.

Public

Documentation Feedback 243