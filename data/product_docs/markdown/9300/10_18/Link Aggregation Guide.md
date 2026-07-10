AOS-CX 10.18.xxxx Link Aggregation Guide

Published: May 2026

AOS-CX 10.18.xxxx Link Aggregation Guide

Published: May 2026

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

AOS-CX 10.18.xxxx Link Aggregation Guide

Legal disclaimer

The resource assets in this document may include abbreviated and/or legacy terminology for products. See
www.arubanetworks.com for current and complete product lines and names.

Public

AOS-CX 10.18.xxxx Link Aggregation Guide

Table of contents

About this document..................................................................................................................................................................................7

Applicable products........................................................................................................................................................................7

Latest version available online.................................................................................................................................................8

Command syntax notation conventions.............................................................................................................................8

About the examples....................................................................................................................................................................... 9

Identifying switch ports and interfaces........................................................................................................................... 10

Identifying modular switch components.........................................................................................................................12

Link Aggregation....................................................................................................................................................................................... 13

Overview............................................................................................................................................................................................ 13

Aggregation group, member port, and aggregate interface................................................................................15

Link aggregation modes...........................................................................................................................................................15

LACP.....................................................................................................................................................................................................15

LACP operating modes.................................................................................................................................................16

LACP configuration settings..................................................................................................................................... 16

Interface LACP settings............................................................................................................................................... 17

LAG interface states....................................................................................................................................................................18

How static link aggregation groups are built............................................................................................................... 19

How dynamic link aggregation groups are built.........................................................................................................21

LAG configuration guidelines................................................................................................................................................ 22

Layer 2 aggregation groups...................................................................................................................................................23

Configuring a layer 2 static aggregation group.............................................................................................23

Configuring a layer 2 dynamic aggregation group...................................................................................... 27

Layer 3 aggregation groups...................................................................................................................................................30

Configuring a layer 3 static aggregation group.............................................................................................31

Configuring a layer 3 dynamic aggregation group...................................................................................... 34

Removing a LAG............................................................................................................................................................................38

Removing an interface from a LAG.................................................................................................................................... 38

Changing the LAG membership for an interface........................................................................................................39

Configuration of an aggregate Interface.........................................................................................................................42

Configuring the description of an aggregate interface............................................................................. 43

Setting the MTU for a layer 2 member link interface................................................................................. 43

Setting the MTU for a layer 3 aggregate interface......................................................................................44

Impact of shutting down or bringing up an aggregate interface.........................................................44

Shutting down an aggregate interface................................................................................................................45

Public

Table of contents 4

Supported hashing algorithms..............................................................................................................................................45

Configuration verification........................................................................................................................................................ 45

BFD reports a LAG as down even when healthy links are still available...................................................... 47

LACP and LAG commands...................................................................................................................................................... 48

description ..........................................................................................................................................................................48

hash ........................................................................................................................................................................................ 49

interface lag ....................................................................................................................................................................... 51

interface persona lag ....................................................................................................................................................52

ip address ............................................................................................................................................................................54

ipv6 address ...................................................................................................................................................................... 55

lacp fallback ....................................................................................................................................................................... 57

lacp fallback-static ..........................................................................................................................................................59

lacp hash ..............................................................................................................................................................................60

lacp mode ............................................................................................................................................................................61

lacp port-id ......................................................................................................................................................................... 62

lacp port-priority .............................................................................................................................................................63

lacp rate ................................................................................................................................................................................64

lacp system-priority ...................................................................................................................................................... 66

lag ............................................................................................................................................................................................ 67

persona custom ............................................................................................................................................................... 68

show interface .................................................................................................................................................................. 70

show interface persona ............................................................................................................................................... 73

show lacp aggregates ...................................................................................................................................................73

show lacp configuration ..............................................................................................................................................75

show lacp interfaces ......................................................................................................................................................76

show lag ............................................................................................................................................................................... 82

show running-config interface ................................................................................................................................84

shutdown .............................................................................................................................................................................87

vlan trunk native ............................................................................................................................................................. 88

Smartlink.........................................................................................................................................................................................................91

Guidelines and limitations........................................................................................................................................................92

Smartlink commands.................................................................................................................................................................. 93

Configuration commands............................................................................................................................................ 93

smartlink group ...................................................................................................................................................93

smartlink recv-control-vlan ..........................................................................................................................95

Group context commands...........................................................................................................................................96

description ............................................................................................................................................................. 97

diag-dump smartlink basic ...........................................................................................................................98

Public

Table of contents 5

primary-port ...................................................................................................................................................... 100

smartlink group secondary-port ............................................................................................................ 101

control-vlan ........................................................................................................................................................ 102

protected-vlans ................................................................................................................................................104

preemption ......................................................................................................................................................... 105

preemption-delay ........................................................................................................................................... 106

Display commands....................................................................................................................................................... 108

show smartlink group ...................................................................................................................................108

show smartlink group all .............................................................................................................................109

show smartlink group detail ..................................................................................................................... 110

show smartlink flush-statistics ............................................................................................................... 112

clear smartlink group statistics ...............................................................................................................113

clear smartlink flush-statistics ................................................................................................................ 114

show running-config .....................................................................................................................................115

Supportability commands........................................................................................................................................117

show capacities smartlink ..........................................................................................................................117

UFD (Uplink Failure Detection)...................................................................................................................................................... 118

Basic UFD configuration........................................................................................................................................................ 119

UFD (Uplink Failure Detection) commands................................................................................................................120

debug ufd all ...................................................................................................................................................................121

delay ....................................................................................................................................................................................121

links-to-disable ............................................................................................................................................................. 123

links-to-monitor ............................................................................................................................................................125

show capacities ufd .................................................................................................................................................... 126

show running-config ufd ......................................................................................................................................... 127

show-tech ufd ................................................................................................................................................................ 128

show ufd ............................................................................................................................................................................130

ufd enable ........................................................................................................................................................................ 132

ufd session-id .................................................................................................................................................................133

Support and Other Resources.........................................................................................................................................................134

Accessing HPE Aruba Networking Support...............................................................................................................134

Accessing Updates....................................................................................................................................................................136

Warranty Information.............................................................................................................................................................. 136

Regulatory Information.......................................................................................................................................................... 136

Documentation Feedback.....................................................................................................................................................137

Public

Table of contents 6

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing HPE Aruba Networking switches on a network.

Subtopics

Applicable products
Latest version available online
Command syntax notation conventions
About the examples
Identifying switch ports and interfaces
Identifying modular switch components

Applicable products

This document applies to the following products:

•  HPE Aruba Networking 4100i Switch Series (JL817A, JL818A)

•  HPE Aruba Networking 5420 Switch Series (S0U67A, S0U55A, S0U63A, S0U64A, S0U65A, S0U75A,

S0U72A, S0U78A, S0U58A, S0U73A, S0U74A, S0U71A, S0U76A, S0U70A, S0U77A, S0U60A,
S0U61A, S0U62A, S0U66A, S0U68A)

•  HPE Aruba Networking 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A,

S4R20A, S4R21A, S4R22A, S4R23A, S4R24A, S4R25A, S4R26A, S4R27A, S4R28, S4R29A)

•  HPE Aruba Networking 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

•  HPE Aruba Networking 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A,
R8Q68A, R8Q69A, R8Q70A, R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A,
JL724B, JL725B, JL726B, JL727B, JL728B, S0M81A, S0M82A, S0M83A, S0M84A, S0M85A, S0M86A,
S0M87A, S0M88A, S0M89A, S0M90A, S0G13A, S0G14A, S0G15A, S0G16A, S0G17A)

•  HPE Aruba Networking 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A,

JL664A, JL665A, JL666A, JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A, S0E91A,
S0X44A, S3L75A, S3L76A, S3L77A, S4P41A,S4P42A, S4P43A, S4P44A, S4P45A, S4P46A, S4P47A,
S4P48A)

•  HPE Aruba Networking 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B,

R0X40C, R0X41A, R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C,
R0X26A, R0X27A, JL741A, S0E48A,S0E48A #0D1, S1T83A, S1T83A #0D1)

Public

About this document 7

•  HPE Aruba Networking 8100 Switch Series (R9W94A, R9W95A, R9W96A, R9W97A)

•  HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

•  HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

•  HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

•  HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

•  HPE Aruba Networking 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A,
JL708A, JL709A, JL710A, JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C,
JL709C, JL710C, JL711C, JL704C, JL705C, JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

•  HPE Aruba Networking 8400 Switch Series (JL366A, JL363A, JL687A)

•  HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A)

•  HPE Aruba Networking 9300S Switch Series (S0F81A, S0F82A, S0F83A, S0F84A, S0F85A, S0F86A,

S0F88A, S0F95A, S0F96A)

•  HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

•  HPE Aruba Networking 10040 Switch Series (S4R58A, S4R59A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example‐text

Usage

Identifies commands and their options and operands
, code examples, filenames, pathnames, and output d
isplayed in a command window. Items that appear li
ke the example text in the previous column are to be
entered exactly as shown and are required unless en
closed in brackets ([ ]).

Public

Latest version available online 8

Convention

example‐text

Any of the following:

•  <example‐text>
•  <example‐text>
•  example‐text
•  example‐text

|

{ }

[ ]

… or

...

Usage

In code and screen examples, indicates text entered
by a user.

Identifies a placeholder—such as a parameter or a va
riable—that you must substitute with an actual valu
e in a command or in code:

•  For output formats where italic text cannot be di
splayed, variables are enclosed in angle brackets
(< >). Substitute the text—including the enclosin
g angle brackets—with an actual value.

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

Public

About the examples 9

The slot and port numbers in this document are for illustration only and might be unavailable on your switch.

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
format: member/slot/port.

On the HPE Aruba Networking 4100i Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

Public

Identifying switch ports and interfaces 10

On the HPE Aruba Networking 6000 and 6100 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the HPE Aruba Networking 6200 Switch Series

•  member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the HPE Aruba Networking 6300 Switch Series

•  member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•  slot: Always 1. This is not a modular switch, so there are no slots.

•  port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the HPE Aruba Networking 6400 and 5420 Switch Series

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

Identifying switch ports and interfaces 11

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

NOTE

If using breakout cables, the port designation changes to x:y, where x is the
physical port and y is the lane when split. For example, the logical interface
1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on
member 1.

On the HPE Aruba Networking 8400 Switch Series

•  member: Always 1. VSF is not supported on this switch.

•  slot: Specifies physical location of a module in the switch chassis.

◦  Management modules are on the front of the switch in slots 1/5 and 1/6.

◦  Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

•  port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

Identifying modular switch components

•  Power supplies are on the front of the switch behind the bezel above the management modules. Power

supplies are labeled in software in the format: member/power supply:

◦  member: 1.

◦  power supply: 1 to 4.

•  Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

◦  member: 1.

◦  tray: 1 to 4.

◦  fan: 1 to 4.

•  Fabric modules are not labeled on the switch but are labeled in software in the format: member/module:

◦  member: 1.

◦  member: 1 or 2.

•  The display module on the rear of the switch is not labeled with a member or slot number.

Public

Identifying modular switch components 12

Link Aggregation

Subtopics

Overview
Aggregation group, member port, and aggregate interface
Link aggregation modes
LACP
LAG interface states
How static link aggregation groups are built
How dynamic link aggregation groups are built
LAG configuration guidelines
Layer 2 aggregation groups
Layer 3 aggregation groups
Removing a LAG
Removing an interface from a LAG
Changing the LAG membership for an interface
Configuration of an aggregate Interface
Supported hashing algorithms
Configuration verification
BFD reports a LAG as down even when healthy links are still available
LACP and LAG commands

Overview

Ethernet link aggregation bundles multiple physical Ethernet links into one logical link, called a link
aggregation group (LAG).

Link aggregation has the following benefits:

•

•

Increased bandwidth beyond the limits of any single link. In an aggregate link, traffic is distributed across
the member ports.

Improved link reliability. The member ports dynamically back up one another. When a member port fails,
its traffic is automatically switched to other member ports. As shown in the following figure Device A
and Device B are connected by three physical Ethernet links. These physical Ethernet links are combined
into an aggregate link called link aggregation 1. The bandwidth of this aggregate link can reach up to
the total bandwidth of the three physical Ethernet links. At the same time, the three Ethernet links back
up one another. When a physical Ethernet link fails, the traffic originally intended for the failed link is
switched to the remaining active links.

Public

Link Aggregation 13

Ethernet link aggregation diagram
Switch Capacities Per Platform
Platform Max interfaces per Max interfaces per Max LAG interfac Max multi‐chassis
LAG interface multi‐chassis LAG e configurations all LAG interfaces confi
|             |     | interface | owed | guration allowed |
| ----------- | --- | --------- | ---- | ---------------- |
| 10000       | 16  | 16        | 128  | 128              |
| 9300/9300S  | 16  | 16        | 128  | 128              |
| 8400        | 16  | 16        | 256  | 256              |
| 8320        | 16  | 16        | 128  | 128              |
| 8325/8325H  | 16  | 16        | 54   | 54               |
| 8325P       | 16  | 16        | 128  | 128              |
| 5420        | 16  | 16        | 144  | 144              |
| 6000/6100   | 8   | 0         | 8    | 0                |
| 4100i       | 8   | 0         | 8    | 0                |
| 6200/6200v2 | 16  | 16        | 48   | 32               |
| 6300M/F     | 16  | 16        | 256  | 32               |
| 6300L       | 16  | 0         | 256  | 0                |
| 6400        | 16  | 16        | 480  | 480              |

Aggregation group, member port, and aggregate inte...
Public Aggregation group, member port, and aggregate inte... 14

Aggregation group, member port, and aggregate interface

An aggregation group is a collection of physical interfaces that are bundled together for the purpose of
load distribution and redundancy. These physical interfaces are called member ports. They are configured
through a logical aggregate interface.

An aggregate interface can be one of the following types:

•  Layer 2: The member ports of the corresponding Link Aggregation Group can only be layer 2 Ethernet

interfaces.

•  Layer 3: The member ports of the corresponding Link Aggregation Group can only be layer 3 interfaces.

NOTE

Layer 3 aggregation groups are not supported on the 4100i, 5420, 6000,
6100, and 6200 Switch Series.

The effective port rate of an aggregate interface equals the total rate of its member ports. Only full duplex
mode members are eligible for aggregation.

Link aggregation modes

An aggregation group operates in one of the following modes:

•  Static LAG: In the static LAG mode of operation, Link failure is not detected as there is no keep alive

PDU communication between the devices. A misconfiguration on one side can cause much trouble and
be difficult to troubleshoot, because no signaling takes place between the two peers.

•  Dynamic LAG or LACP: The local device and the peer device automatically maintain the aggregation

states of the member ports, resulting in link failure being quickly detected by exchanging the PDU. LACP
reduces the workload of network administrators.
Dynamic LAG uses LACP packets to establish the association between two peers. This configuration
results in the reduction of the misconfiguration probability. Also, link failures are intelligently handled
by two participating devices through the LACP protocol, which is adaptive or dynamic to these network
failures.

Layer 2 aggregation groups and layer 3 aggregation groups support both static and dynamic modes.

LACP

Dynamic aggregation is implemented through the IEEE 802.3ad Link Aggregation Control Protocol (LACP).

Public

Link aggregation modes 15

LACP uses LACPDUs to exchange aggregation information between LACP-enabled devices. Each member
port in a dynamic aggregation group can exchange information with its peer. When a member port receives
an LACPDU, it compares the received information with information received on the other member ports. In
this way, the two systems agree on which ports are placed in Selected state.

The LACPDU fields convey data for the LACP functions, including:

•  System LACP priority

•  System MAC address

•  Port priority

•  Port number

•  Operational key

Subtopics

LACP operating modes
LACP configuration settings
Interface LACP settings

LACP operating modes

LACP can operate in active or passive mode.

•  Active mode: When the LACP is operating in active mode on either end of a link, both ports can send
PDUs. The "active" LACP initiates an LACP connection by sending LACPDUs. The "passive" LACP will
wait for the remote end to initiate the link.

•  Passive mode: When the LACP is operating in passive mode on a local member port and as its peer port,

both ports cannot send PDUs.

NOTE

Two peer ports operating in "passive" mode will never establish an LACP link.

For an LACP LAG, one side must have LACP in active mode and the peer must have an LACP configuration
of active or passive mode. If you do not enable LACP on a LAG, it is treated as a static LAG and the peer
cannot negotiate LACP with the LAG.

LACP configuration settings

Public

LACP operating modes 16

| Task |     | Command | Example |     |
| ---- | --- | ------- | ------- | --- |
Setting the LACP mode to active o lacp mode {active | p switch(config‐lag‐if)
| r passive. |     | assive} | # lacp mode active |     |
| ---------- | --- | ------- | ------------------ | --- |
Setting the LACP mode to off. no lacp mode {active switch(config‐lag‐if)
|     |     | | passive} | # no lacp mode active |     |
| --- | --- | ---------- | --------------------- | --- |
Setting the hash type. For 6000, 6100, and 8400 Switch For 6000, 6100, and 8400 Switch
|     |     | Series:               | Series:              |     |
| --- | --- | --------------------- | -------------------- | --- |
|     |     | lacp hash [l2‐src‐dst | switch(config)# lacp |     |
|     |     | | l3‐src‐dst | l4‐src | hash l2‐src‐dst      |     |
‐dst]
For 8320, 8325/8325P/8325H, 5
|     |     | For 8320, 8325/8325P/8325H, 5  | 420, 6200, 6300, 6400 and 1000 |     |
| --- | --- | ------------------------------ | ------------------------------ | --- |
|     |     | 420, 6200, 6300, 6400 and 1000 | 0 Switch Series:               |     |
0 Switch Series:
switch(config‐lag‐if)
|     |     | hash [l2‐src‐dst | l3 | # hash l2‐src‐dst |     |
| --- | --- | --------------------- | ----------------- | --- |
‐src‐dst | l4‐src‐dst
]
Setting the LACP rate to fast. lacp rate fast switch(config)# inter
face lag 1
switch(config‐lag‐if)
# lacp rate fast
Setting the LACP rate to slow. lacp rate slow switch(config)# inter
face lag 1
switch(config‐lag‐if)
# lacp rate slow
Applying shutdown on the LAG po shutdown switch(config)# inter
| rt. |     |     | face lag 1 |     |
| --- | --- | --- | ---------- | --- |
switch(config‐lag‐if)
# shutdown
Resetting every interface in the L no shutdown switch(config‐lag‐if)
| AG to the default (up) |     |     | # no shutdown |     |
| ---------------------- | --- | --- | ------------- | --- |

Interface LACP settings
|     | Public |     | Interface LACP settings | 17  |
| --- | ------ | --- | ----------------------- | --- |

| Task |     | Command | Example |     |     |
| ---- | --- | ------- | ------- | --- | --- |
Setting the LACP port ID. lacp port‐id <ID> switch(config‐if)# la
cp port‐id 100
Setting the LACP port ID to the de no lacp port‐id switch(config‐if)# no
| fault. |     |     | lacp port‐id |     |     |
| ------ | --- | --- | ------------ | --- | --- |
Setting the LACP port priority. lacp port‐priority <P switch(config‐if)# la
|     |     | ORT‐PRIORITY> | cp port‐priority 100 |     |     |
| --- | --- | ------------- | -------------------- | --- | --- |
Setting the LACP port priority to t no lacp port‐priority switch(config‐if)# no
| he default |     |     | lacp port‐priority |     |     |
| ---------- | --- | --- | ------------------ | --- | --- |

LAG interface states
The output from the CLI commands show lacp interfaces  and  show lacp interfaces
| multi-chassis |  display the following interface states: |     |     |     |     |
| ------------- | ---------------------------------------- | --- | --- | --- | --- |
Interface state Description
A ‐ Active An active LACP interface.
C ‐ Collecting Data frames are received through the aggregate link
and sent onto the intended destination.
D ‐ Distributing Data frames are transmitted through the aggregate li
nk to reach the intended destination.
F ‐ Aggregable The link can be used as part of an aggregate.
E ‐ Default neighbor state The link has the default state of the neighbor switch.
I ‐ Individual The link is used as an individual link.
L ‐ Long‐timeout With the long timeout, an LACPDU is sent every 30 s
econds. If no response comes from its partner after t
hree LACPDUs are sent (90 seconds), a timeout eve
nt occurs. The LACP state machine then transitions
to the appropriate state based on its current state.
|     | Public |     |     | LAG interface states | 18  |
| --- | ------ | --- | --- | -------------------- | --- |

Interface state

N ‐ InSync

O ‐ OutofSync

P ‐ Passive

S ‐ Short‐timeout

X ‐ State m/c expired

Description

The physical port is connected to the aggregate po
rt that was last chosen by the logical election. The
state variable selected is still true.

The hardware might be out of sync with the modifi
ed protocol information. If the hardware also has a
status of collecting, do not transmit frames because t
hey will be misdelivered.

The port participates in the protocol, as long as it ha
s an active partner.

In the short timeout configuration, an LACPDU is sen
t every second. If no response comes from its partne
r after three LACPDUs are sent, a timeout event occu
rs. The LACP state machine then transitions to the a
ppropriate state based on its current state.

The "current while" timer has expired. The "current w
hile" timer then restarts with the short‐timeout ena
bled.

The term  State m/c  refers to a state machine.

How static link aggregation groups are built

Reference port selection process

When setting the aggregation states of the ports in an aggregation group, the system automatically chooses
a member port as the reference port. A selected port must have the same operational key and attribute
configurations as the reference port.

The system chooses a reference port from the member ports in the up state. The first member interface
which is operationally up is selected as reference port.

Setting the aggregation state of each member port

After the reference port is chosen, the system sets the aggregation state of each member port in the static
aggregation group.

Setting the aggregation state of a member port in a static aggregation group

Public

How static link aggregation groups are built 19

After the maximum limit of members is reached in a LAG, an additional port cannot be added to the
aggregation group. If a port belongs to a card type with a different speed than the other aggregation
members, the port can still be added to the aggregation group. If dynamic LAG is enabled, any port member
with a speed different than other aggregation members is blocked or ineligible from the same aggregation

Public

How static link aggregation groups are built 20

group. Any operational keys/attributes or configuration changes might affect the aggregation states of the
member ports.

How dynamic link aggregation groups are built

Choosing a reference port

About this task

The system chooses a reference port from the member ports in up state. A selected port must have the same
operational key and attribute configurations as the reference port.

The process by which the local system (the actor) and the peer system (the partner) negotiate a reference
port occurs as follows:

Procedure

1.  The two systems determine the system with the smaller system ID. A system ID contains the system

LACP priority and the system MAC address.

a.  The two systems compare their LACP priority values.The lower the LACP priority, the smaller the

system ID. If the LACP priority values are the same, the two systems proceed to step b.

b.  The two systems compare their MAC addresses.The lower the MAC address, the smaller the system

ID.

2.  The system with the smaller system ID chooses the first operationally up port as the reference port. A
port ID contains a port priority and a port number. The lower the port priority, the smaller the port ID.

Setting the aggregation state of each member port

After the reference port is chosen, the system with the smaller system ID sets the state of each member port
on its side.

The system with the greater system ID can detect the aggregation state changes on the peer system. The
system with the greater system ID sets the aggregation state of local member ports the same as their peer
ports.

When you aggregate interfaces in dynamic mode, follow these guidelines:

•  A dynamic link aggregation group chooses only full-duplex ports as the selected ports.

•  For stable aggregation and service continuity, do not change the operational key or attribute

configurations on any member port.

Public

How dynamic link aggregation groups are built 21

LAG configuration guidelines

Aggregation member interface restrictions

•

If any features in the following list are configured on the interface, you cannot assign an interface to a
Layer 2 aggregation group:

◦  MAC authentication

◦  Port security

◦  802.1X

•  Do not assign a reflector port for port mirroring to an aggregation group.

Requirements for adding interfaces

Keep in mind the following requirements when adding interfaces to a LAG:

•  To determine the maximum number of LAG interfaces for your type of switch, look at the output

from the  show capacities lag  command; however, the number of LAGs that can be created
depends on the availability of the physical interface since each LAG interface needs at least one physical
interface as a member link. fter the maximum limit of members is reached in a LAG, an additional port
cannot be added to the aggregation group. If a port belongs to a card type with a different speed
than the other aggregation members, the port can still be added to the aggregation group. If dynamic
LAG is enabled, any port member with a speed different than other aggregation members is blocked or
ineligible from the same aggregation group. Any operational keys/attributes or configuration changes
might affect the aggregation states of the member ports.

•  The nondefaults configuration on an interface is removed automatically when the interface is added to
a link aggregation. For example: Assume that you remove a member interface from an existing LAG and
add it to another LAG. The software removes the nondefault configurations on the interface when it is
added to the new LAG.

Configuration consistency requirements

•  Configure at least one active mode aggregation in two devices.

•  For a successful static aggregation, make sure the ports at both ends of each link are in the same

aggregation state.

•  For a successful dynamic aggregation, make sure the peer ports of the ports aggregated at one end

are also aggregated, and that one of the ends is configured as "active". The two ends can automatically
negotiate the aggregation state of each member port.

Public

LAG configuration guidelines 22

Removing interfaces

•  Deleting an aggregate interface also deletes its aggregation group and causes all member ports to leave

the aggregation group.

•  When a member interface is removed from a LAG:

◦  4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switches: The interface goes to its default status

of  unshut .

◦  8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300, or 10000 switches: The interface becomes

disabled.

Disabling an interface

When an interface LAG is disabled with the  shutdown  command, all its members also become
operationally down.

Layer 2 aggregation groups

All switches support static and dynamic layer 2 aggregation groups.

NOTE
On the 6400 Switch Series, port identification differs. Line card ports start at  1/
3/1 .

Subtopics

Configuring a layer 2 static aggregation group
Configuring a layer 2 dynamic aggregation group

Configuring a layer 2 static aggregation group

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

1.  Create a layer 2 aggregate interface and access the layer 2 aggregate interface view by entering:

switch(config)# interface lag <ID>

Public

Layer 2 aggregation groups 23

The range of the LAG interface ID is 1 to 256.

While creating the layer 2 aggregate interface, the system automatically creates a layer 2 static
aggregation group numbered the same.

2.  Set the operational state of every interface in the LAG to up by entering:

switch(config-lag-if)# no shutdown

NOTE

This command does not impact the administrative state of the member
interfaces because the command was entered at the level of the LAG. To
change the administrative state of a member interface, enter the command at
the interface level. For example:

switch(config)# interface 1/1/2

switch(config-if)# no shutdown

3.  On the 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000, disable routing by

entering:
switch(config-lag-if)# no routing

See the Command-Line Interface Guide for your switch and software version for more information about
the no routing command.

NOTE

On the 4100i, 6000, 6100, and 6200 Switch Series, routing is not supported
on physical interfaces.

On the 6300 and 6400 Switch Series, routing is disabled by default.

For example:

4.  Assign a native VLAN ID to a trunk interface on the LAG by entering:
switch(config-lag-if)# vlan trunk native <VLAN-ID>

switch(config-lag-if)# vlan trunk native 1

5.  Use the following steps to add a maximum of 16 interfaces to the LAG:

a.  To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

Public

Configuring a layer 2 static aggregation group 24

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the  interface <PORT-ID>  command.

b.  Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

switch(config-if-<1/1/1-1/1/4>)# lag 100

c.  Set the administrative state of the member interface to up:

switch(config-if-<1/1/1-1/1/4>)# no shutdown

6.  View the configuration by entering the following:

For 4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 100

    no shutdown

    vlan trunk native 1

    vlan trunk allowed all

interface 1/1/1

    no shutdown
    lag 100

interface 1/1/2

    no shutdown

    lag 100

interface 1/1/3

    no shutdown

    lag 100

interface 1/1/4

    no shutdown

    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Public

Configuring a layer 2 static aggregation group 25

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : N/A

Hash             : l3-src-dst

Aggregate mode   : Off
For 4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 100

    no shutdown

    vlan trunk native 1

    vlan trunk allowed all

interface 1/1/1

    no shutdown

    lag 100

interface 1/1/2

    no shutdown

    lag 100

interface 1/1/3

    no shutdown

    lag 100

interface 1/1/4

    no shutdown

    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : N/A

Hash             : l3-src-dst

Aggregate mode   : Off
For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 100

    no shutdown
    no routing
    vlan trunk native 1

    vlan trunk allowed all

interface 1/1/1

Public

Configuring a layer 2 static aggregation group 26

no shutdown

    lag 100

interface 1/1/2

    no shutdown

    lag 100

interface 1/1/3

    no shutdown

    lag 100

interface 1/1/4

    no shutdown

    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : N/A

Hash             : l3-src-dst

Aggregate mode   : Off

Configuring a layer 2 dynamic aggregation group

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

1.  Create a layer 2 aggregate interface and access the layer 2 aggregate interface view by entering:

switch(config)# interface lag <ID>

While creating the layer 2 aggregate interface, the system automatically creates a layer 2 dynamic
aggregation group numbered the same.

The range of the LAG interface ID is 1 to 256.

2.  Set the operational state of every interface in the LAG to up by entering:

Public

Configuring a layer 2 dynamic aggregation group 27

switch(config-lag-if)# no shutdown

NOTE

This command does not impact the administrative state of the member
interfaces because the command was entered at the level of the LAG. To
change the administrative state of a member interface, enter the command at
the interface level. For example:

switch(config)# interface 1/1/2

switch(config-if)# no shutdown

3.  On the 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000, disable routing by

entering:
switch(config-lag-if)# no routing

See the Command-Line Interface Guide for your switch and software version for more information about
the  no routing  command.

NOTE

On the 4100i, 6000, 6100, and 6200 Switch Series, routing is not supported
on physical interfaces.

On the 6300 and 6400 Switch Series, routing is disabled by default.

4.  Configure the aggregation group to operate in dynamic mode by entering:
switch(config-lag-if)# lacp mode {active | passive}

For example:

switch(config-lag-if)# lacp mode active

5.  Configure the aggregation group to operate in fast or slow mode by entering:

switch(config-lag-if)# lacp rate {fast | slow}

For example:

switch(config-lag-if)# lacp rate fast

6.  Assign a native VLAN ID to a trunk interface by entering:

switch(config-lag-if)# vlan trunk native <VLAN-ID>

Public

Configuring a layer 2 dynamic aggregation group 28

For example:

switch(config-lag-if)# vlan trunk native 1

7.  Use the following steps to add a maximum of 16 interfaces to the LAG:

a.  To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the  interface <PORT-ID>  command.

b.  Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

switch(config-if-<1/1/1-1/1/4>)# lag 20

c.  Set the administrative state of the member interface to up:

switch(config-if-<1/1/1-1/1/4>)# no shutdown

8.  View the configuration by entering:

For 4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 20

    no shutdown

    vlan trunk native 1
    vlan trunk allowed all

    lacp mode active

    lacp rate fast

interface 1/1/1

Public

Configuring a layer 2 dynamic aggregation group 29

no shutdown

    lag 20

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : Fast

Hash             : l3-src-dst

Aggregate mode   : Active
For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 20

    no shutdown

    no routing

    vlan trunk native 1

    vlan trunk allowed all

    lacp mode active

    lacp rate fast

interface 1/1/1

    no shutdown

    lag 20

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : Fast

Hash             : l3-src-dst

Aggregate mode   : Active

Layer 3 aggregation groups

Layer 3 aggregation groups are supported on all switch series except 6000, and 6100 Switch Series.

Subtopics

Configuring a layer 3 static aggregation group
Configuring a layer 3 dynamic aggregation group

Public

Layer 3 aggregation groups 30

Configuring a layer 3 static aggregation group

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

1.  Create a layer 3 aggregate interface and access the layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

The range of the LAG interface ID is 1 to 256.

While creating the layer 3 aggregate interface, the system automatically creates a layer 3 static
aggregation group numbered the same.

2.  Set the operational state of every interface in the LAG to up by entering:

•  For 5420, 6200, 6300 and 6400 switch series:
switch(config-lag-if)# no shutdown

switch(config-lag-if)# routing

NOTE

This command does not impact the administrative state of the member
interfaces because the command was entered at the level of the LAG. To
change the administrative state of a member interface, enter the command
at the interface level. For example:

switch(config)# interface 1/1/2

switch(config-if)# no shutdown

switch(config-if)# routing

•  For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000 switch series:

Public

Configuring a layer 3 static aggregation group 31

switch(config-lag-if)# no shutdown

NOTE

This command does not impact the administrative state of the member
interfaces because the command was entered at the level of the LAG. To
change the administrative state of a member interface, enter the command
at the interface level. For example:

switch(config)# interface 1/1/2

switch(config-if)# no shutdown

3.  Set the IP address on the LAG interface by entering:

switch(config-lag-if)# ip address <IPV4-ADDR>/<MASK>

For example:

switch(config-lag-if)# ip address 192.0.2.1/30

4.  Use the following steps to add a maximum of 16 interfaces to the LAG:

a.  To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the  interface <PORT-ID>  command.

b.  Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

switch(config-if-<1/1/1-1/1/4>)# lag 100

c.  Set the administrative state of the member interface to up:

Public

Configuring a layer 3 static aggregation group 32

switch(config-if-<1/1/1-1/1/4>)# no shutdown

5.  View the configuration by entering the following:
For 5420, 6200, 6300 and 6400 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 100

    no shutdown

    routing

    ip address 192.0.2.1/30

interface 1/1/1

    no shutdown

    lag 100

interface 1/1/2

    no shutdown

    lag 100

interface 1/1/3

    no shutdown

    lag 100

interface 1/1/4

    no shutdown

    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : N/A

Hash             : l3-src-dst

Aggregate mode   : Off
For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 100

    no shutdown
    ip address 192.0.2.1/30
interface 1/1/1

    no shutdown

    lag 100

interface 1/1/2

Public

Configuring a layer 3 static aggregation group 33

no shutdown

    lag 100

interface 1/1/3

    no shutdown

    lag 100

interface 1/1/4

    no shutdown

    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : N/A

Hash             : l3-src-dst

Aggregate mode   : Off

Configuring a layer 3 dynamic aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#.

Procedure

1.  Create a layer 3 aggregate interface and access the layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

The range of the LAG interface ID is 1 to 256.

While creating the layer 3 aggregate interface, the system automatically creates a layer 3 dynamic
aggregation group numbered the same.

2.  Set the operational state of every interface in the LAG to up by entering:

•  For 5420, 6200, 6300 and 6400 switch series:

Public

Configuring a layer 3 dynamic aggregation group 34

switch(config-lag-if)# no shutdown

switch(config-lag-if)# routing

NOTE

This command does not impact the administrative state of the member
interfaces because the command was entered at the level of the LAG. To
change the administrative state of a member interface, enter the command
at the interface level. For example:

switch(config)# interface 1/1/2

switch(config-if)# no shutdown

switch(config-if)# routing

•  For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000 switch series:

switch(config-lag-if)# no shutdown

NOTE

This command does not impact the administrative state of the member
interfaces because the command was entered at the level of the LAG. To
change the administrative state of a member interface, enter the command
at the interface level. For example:

switch(config)# interface 1/1/2

switch(config-if)# no shutdown

3.  Configure the aggregation group to operate in dynamic mode by entering:
switch(config-lag-if)# lacp mode {active | passive}

For example:

switch(config-lag-if)# lacp mode active

4.  Configure the aggregation group to operate in fast or slow mode by entering:

switch(config-lag-if)# lacp rate {fast | slow}

For example:

switch(config-lag-if)# lacp rate fast

5.  Set the IP address on the LAG interface by entering:

Public

Configuring a layer 3 dynamic aggregation group 35

switch(config-lag-if)# ip address <IPV4-ADDR>/<MASK>

For example:

switch(config-lag-if)# ip address 192.0.3.1/30

6.  Use the following steps to add a maximum of 16 interfaces to the LAG:

a.  To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the  interface <PORT-ID>  command.

b.  Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

switch(-<1/1/1-1/1/4>)# lag 100

c.  Set the administrative state of the member interface to up:

switch(-<1/1/1-1/1/4>)# no shutdown

7.  View the configuration by entering:

For 5420, 6200, 6300 and 6400 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 100
    no shutdown

    routing

    ip address 192.0.3.1/30

    lacp mode active

Public

Configuring a layer 3 dynamic aggregation group 36

lacp rate fast

interface 1/1/1

    no shutdown

    lag 100

interface 1/1/2

    no shutdown

    lag 100

interface 1/1/3

    no shutdown

    lag 100

interface 1/1/4

    no shutdown

    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : Fast

Hash             : l3-src-dst

Aggregate mode   : Active
For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:

!

vlan 1

interface lag 100

    no shutdown

    ip address 192.0.3.1/30

    lacp mode active

    lacp rate fast

interface 1/1/1

    no shutdown
    lag 100

interface 1/1/2

    no shutdown

    lag 100

interface 1/1/3

    no shutdown

    lag 100

interface 1/1/4

    no shutdown

    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Aggregate name   : lag100

Public

Configuring a layer 3 dynamic aggregation group 37

Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2

Heartbeat rate   : Fast

Hash             : l3-src-dst

Aggregate mode   : Active

Removing a LAG

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

Delete the LAG. Enter:

switch(config)# no interface lag <ID>

For example:

switch(config)# no interface lag 100

All interfaces assigned to the LAG are automatically removed from the LAG as part of the deletion process of
the LAG. After removing a physical interface from a LAG,

•  4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switches: The interface associated with the LAG

becomes layer 2 ports with the default layer 2 configurations and admin status enabled.

•  8100, 8320, 8235, 8360, and 8400 switches: The interface associated with the LAG becomes layer 3

ports with default layer 3 configurations and administrative down.

Removing an interface from a LAG

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

Remove an interface from the LAG. Enter:

switch(config)# interface <PORT-NUM>

switch(config-if)# no lag <ID>

For example:

Public

Removing a LAG 38

switch(config)# interface 1/1/1

switch(config-if)# no lag 100

switch(config-if)# show running-config

...

!

vlan 1

interface lag 100

interface 1/1/1

interface 1/1/2

    lag 100

switch(config-if)#
To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

After removing a physical interface from a LAG:

•  4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switches: The interface associated with LAG becomes

layer 2 ports with default layer 2 configurations and with admin status of enabled

•  8100, 8320, 8325/8325H/8325P, 8360, 8400, 9300/9300S and 10000 switches: The interface

associated with the LAG becomes L3 ports with default L3 configurations and administrative down. For
example, suppose interface 1/1/1 was part of LAG 3 and you had administratively enabled the interface.
If you later remove interface 1/1/1 from LAG 3, the administrative status automatically changes to
down. If you want to use the interface again, you must administratively enable it again.

Changing the LAG membership for an interface

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

1.  Remove an interface from the LAG. Enter:

switch(config)# interface <PORT-NUM>
switch(config-if)# no lag <ID>

For example:

For 4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switch series:

Public

Changing the LAG membership for an interface 39

switch(config)# interface 1/1/1

switch(config-if)# no lag 100

switch(config-if)# show running-config

Current configuration:

!

...

!

vlan 1

interface lag 100

    no shutdown

    vlan trunk native 1

    vlan trunk allowed all

interface 1/1/1

    no shutdown

interface 1/1/2

    no shutdown

    lag 100

switch(config-if)#
For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 9300/9300S and 10000 switch series:

switch(config)# interface 1/1/1

switch(config-if)# no lag 100

switch(config-if)# show running-config

Current configuration:

!

...

!

vlan 1

interface lag 100

    no shutdown

    no routing

    vlan trunk native 1
    vlan trunk allowed all

interface 1/1/1

interface 1/1/2

    no shutdown

    no routing

   vlan access 1

switch(config-if)#
After removing a physical interface from a LAG, the interface associated with the LAG becomes L3 ports
with default L3 configurations and administrative down. For example, suppose interface 1/1/1 was part
of LAG 3 and you had administratively enabled the interface. If you later remove interface 1/1/1 from
LAG 3, the administrative status automatically changes to down.

Public

Changing the LAG membership for an interface 40

On 4100i, 5420, 6000, 6100, and 6200 Switch Series, after removing a physical interface from a LAG,
the interface associated with the LAG becomes layer 2 ports with default layer 2 configurations and
admin status enabled.

2.  Create the LAG to which you want to add the interface:
switch(config-if)# interface lag 10

For 4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switch series:

switch(config-if)# interface lag 10

switch(config-lag-if)# no shutdown

switch(config-lag-if)# vlan trunk native 1

For example:

For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 930/9300Sand 10000 switch series:

switch(config-if)# interface lag 10 switch(config-lag-if)# no shutdown switch(config-lag-if)# no
routing switch(config-lag-if)# vlan trunk native 1

3.  Add the interface from Step 1 to the newly created LAG:

switch(config)# interface 1/1/1

switch(config-if)# lag 10

For example:

For 4100i, 5420, 6000, 6100, 6200, 6300, and 6400 switch series:

switch(config)# interface 1/1/1

switch(config-if)# lag 10

switch(config-if)# show running-config

Current configuration:

!

...
!

vlan 1

interface lag 10

    no shutdown

    vlan trunk native 1

    vlan trunk allowed all

interface lag 100

    no shutdown

    vlan trunk native 1

    vlan trunk allowed all

interface 1/1/1

    lag 10

Public

Changing the LAG membership for an interface 41

interface 1/1/2

    no shutdown

    lag 100
For 8100, 8320, 8325/8325P/8325H, 8360, 8400, 930/9300Sand 10000 switch series:

switch(config)# interface 1/1/1

switch(config-if)# lag 10

switch(config-if)# show running-config

Current configuration:

!

...

!

vlan 1

interface lag 10

    no shutdown

    no routing

    vlan trunk native 1

    vlan trunk allowed all

interface lag 100

    no shutdown

    no routing

    vlan trunk native 1

    vlan trunk allowed all

interface 1/1/1

    lag 10

interface 1/1/2

    no shutdown

    lag 100

The interface is enabled by default when it is added to the LAG.

Configuration of an aggregate Interface

Subtopics

Configuring the description of an aggregate interface
Setting the MTU for a layer 2 member link interface
Setting the MTU for a layer 3 aggregate interface
Impact of shutting down or bringing up an aggregate interface
Shutting down an aggregate interface

Public

Configuration of an aggregate Interface 42

C
o
n
fi
g
u
r
i
n
g

t
h
e

d
e
s
c
r
i
p
t
i
o
n

o
f

a
n

a
g
g
r
e
g
a
t
e

i
n
t
e
r
f
.
.
.

Configuring the description of an aggregate interface

You can configure the description of an aggregate interface for administration purposes, for example,
describing the purpose of the interface.

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

1.  Create a layer 3 aggregate interface and enter layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

2.  Configure the description of the aggregate interface:
switch(config-if)# description <text>

Setting the MTU for a layer 2 member link interface

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

1.  Enter a layer 2 member link interface view by entering:
switch(config)# interface <INTERFACE-ID>

2.  Set the MTU for the layer 2 member link interface:

switch(config-if)# mtu <VALUE>

See the Command-Line Interface Guide for your switch and software version for more information about
the mtu <VALUE> command. When allowing jumbo frames under a layer 2 aggregation interface, make
sure that the MTU value is set appropriately under all member interfaces.

Public

Setting the MTU for a layer 2 member link interfac... 43

S
e
t
t
i
n
g

t
h
e

M
T
U

f
o
r

a

l
a
y
e
r

2

m
e
m
b
e
r

l
i
n
k

i
n
t
e
r
f
a
c
.
.
.

Setting the MTU for a layer 3 aggregate interface

NOTE

Layer 3 aggregation groups are not supported on the 4100i, 5420, 6000, 6100,
and 6200 Switch Series.

The MTU of an interface affects IP packets fragmentation and reassembly on the interface.

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

1.  Enter layer 3 aggregate interface view by entering:

switch(config)# interface lag <INTERFACE-ID>

2.  Set the MTU for the layer 3 aggregate interface:

switch(config-lag-if)# ip mtu <VALUE>

See the Command-Line Interface Guide for your switch and software version for more information about
the ip mtu <VALUE> command. When allowing jumbo frames under a layer 2 aggregation interface,
make sure that the MTU value is set appropriately under all member interfaces.

NOTE

If the IP MTU is configured as 9198, the MTU on the physical interfaces must
also be configured as 9198.

Impact of shutting down or bringing up an aggregate interface

By default, an aggregate interface is down. Shutting down or bringing up an aggregate interface affects the
aggregation states and link states of member ports in the corresponding aggregation group as follows:

•  When an aggregate interface is shut down, all Selected ports in the corresponding aggregation group

become Unselected ports and all member ports go to an operationally down state.

•  When an aggregate interface is brought up, the aggregation states of member ports in the

corresponding aggregation group are recalculated. LAG members, which are administratively up, will
become operationally up. The members that are not administratively up will be in the same state and not
made eligible for aggregation.

Public

Setting the MTU for a layer 3 aggregate interface 44

I
m
p
a
c
t

o
f

s
h
u
t
t
i
n
g

d
o
w
n

o
r

b
r
i
n
g
i
n
g

u
p

a
n

a
g
g
r
e
g
a
t
.
.
.

Shutting down an aggregate interface

Prerequisites

You must be in the global configuration context:  switch(config)# .

Procedure

Enter the layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

Shut down the aggregate interface:

switch(config-lag-if)# shutdown

Supported hashing algorithms

•  Source MAC and destination MAC

•  Source IP and destination IP

•  Source port and destination port.

Configuration verification

Task

Command

Example

Viewing LACP global information

show lacp configurati
on

switch# show lacp

configuration
System‐id       :
70:72:cf:ef:fc:d9
System‐priority :
65534
Hash            : l3‐
src‐dst

Public

Shutting down an aggregate interface 45

Task

Command

Example

The output displayed for the  sho
w lacp configuration  is
from the 8400 series switch.

show lacp aggregates

switch# show lacp

Viewing LACP aggregate informati
on

aggregates
Aggregate‐
name          : lag100
Aggregated‐
interfaces   : 1/1/2

Heartbeat

rate          : N/A

Hash
  : l3‐src‐dst
Aggregate

mode          : off
Aggregate‐
name          : lag110
Aggregated‐
interfaces   : 1/1/1,

1/1/3

Heartbeat

rate          : slow

Hash
  : l3‐src‐dst
Aggregate

mode          : active

switch# show lacp

aggregates lag100
Aggregate‐
name          : lag100
Aggregated‐
interfaces   :

Heartbeat

rate          : N/A

Hash
  : l3‐src‐dst
Aggregate

mode          : off

Viewing LACP aggregate informati
on for a LAG

show lacp aggregates
lag100

Viewing LACP interface details

show lacp interfaces

switch# show lacp

interfaces

Public

Configuration verification 46

Task

Command

Example

The output is too wide to display i
n a column. The command output i
s provided in the CLI topic for the
command.

BFD reports a LAG as down even when healthy links are still
available

Symptom

NOTE

BFD is not supported on the 4100i, 5420, 6000, 6100, and 6200 Switch Series.

The Bidirectional Forward Detection (BFD) feature reports a Link Aggregation (LAG), as being down, even
though there are healthy LAG links available. The LAG, containing the downed link, will eventually rebalance
the traffic to its other links.

Cause

This notification occurs when the minimum BFD control packet reception interval is set at a faster rate than
the Link Aggregation Control Protocol (LACP) rate and LAG rebalancing occurs. BFD assumes that the link is
down without realizing that the LAG is rebalancing the traffic load.

Action

Set the minimum BFD control packet reception interval to a slower rate than the LACP rate or set the LACP
rate to a faster rate than the minimum BFD control packet reception interval.

1.  To find the current settings of the minimum BFD control packet reception interval, enter the  show ru

nning-config  command.
The minimum BFD control packet reception interval setting is listed as bfd min-receive-interval in the
command output and the measurement is in ms.

2.  To find the current rate of LACP, enter the  show lacp aggregates  command.

The LACP rate is listed as the Heatbeat rate in the command output.

3.  To change the minimum BFD control packet reception interval, enter the  bfd min-receive-int

erval  command.

4.  To change the LACP rate, enter the  lacp rate {fast | slow}  command.

Public

BFD reports a LAG as down even when healthy links ... 47

B
F
D

r
e
p
o
r
t
s

a

L
A
G

a
s

d
o
w
n

e
v
e
n

w
h
e
n

h
e
a
l
t
h
y

l
i
n
k
s

.
.
.

LACP and LAG commands

Select a command from the list in the left navigation menu.

Subtopics

description
hash
interface lag
interface persona lag
ip address
ipv6 address
lacp fallback
lacp fallback-static
lacp hash
lacp mode
lacp port-id
lacp port-priority
lacp rate
lacp system-priority
lag
persona custom
show interface
show interface persona
show lacp aggregates
show lacp configuration
show lacp interfaces
show lag
show running-config interface
shutdown
vlan trunk native

description

Syntax

description <TEXT>

no description <TEXT>

Description

Provides a brief description of the LAG interface. The description text is saved in the configuration of the
LAG. It is available even after a reboot.

Public

LACP and LAG commands 48

The no form of this command removes the description of the LAG interface from the configuration.

Parameter

Description

Specifies the description of the LAG interface.

<TEXT>

Example

switch(config)# interface lag 10

switch(config-lag-if)# description This LAG is used for an example.

switch(config-lag-if)# show running-config

...

vlan 1

interface lag 10

     description This LAG is used for an example.

interface lag 60

switch(config-lag-if)#

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

hash

Syntax

hash [l2-src-dst | l3-src-dst | l4-src-dst]

Public

hash 49

Description

This command controls the selection of an interface in a group of aggregate interfaces. The hash type value
helps transmit a frame. This configuration must be done at the LAG interface level.

Parameter

l2‐src‐dst

l3‐src‐dst

l4‐src‐dst

Example

Description

Specifies the load‐balancing calculation to include only layer
2 items, such as source and destination MAC addresses.

Specifies the load‐balancing calculation to include only layer
3 items, such as source and destination IP addresses. Default s
etting.

Specifies the load‐balancing calculation to include only layer
4 items, such as source and destination UDP/TCP ports.

switch(config-lag-if)# hash l2-src-dst

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

5420

6200

6300

6400

8100

8320

8325

8325H

8325P

Public

hash 50

Platforms

Command context

Authority

10000

interface lag

Syntax

interface lag <ID>

no interface lag <ID>

Description

Creates a Link Aggregation Group (LAG) interface represented by an ID.

The no form of this command deletes a LAG interface represented by an ID.

Parameter

Description

Specifies a LAG interface ID.

<ID>

Usage

Keep in mind the following requirements when adding interfaces to a LAG:

•  To determine the maximum number of LAG interfaces for your type of switch, look at the output from
the show capacities lag command; however, the number of LAGs that can be created depends on the
availability of the physical interface since each LAG interface needs at least one physical interface as a
member link.

•  After the maximum limit of members is reached in a LAG, an additional port cannot be added to the
aggregation group. If a port belongs to a card type with a different speed than the other aggregation
members, the port can still be added to the aggregation group. If dynamic LAG is enabled, any port
member with a speed different than other aggregation members is blocked or ineligible from the
same aggregation group. Any operational keys/attributes or configuration changes might affect the
aggregation states of the member ports.

•  The nondefaults configuration on an interface is removed automatically when the interface is added to
a link aggregation. For example: Assume that you remove a member interface from an existing LAG and

Public

interface lag 51

add it to another LAG. The software removes the nondefault configurations on the interface when it is
added to the new LAG.

Examples

Creating a Link Aggregation Group (LAG) interface represented by an ID of 100:

switch(config)# interface lag 100

Deleting a Link Aggregation Group (LAG) interface represented by an ID of 100:

switch(config)# no interface lag 100

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

interface persona lag

Syntax

interface persona lag <NAME>

no interface persona lag <NAME>

Description

Creates a persona LAG, a template for LAG (Link Aggregation Group) interfaces. A persona LAG defines
configuration options that can be applied to multiple LAGs for consistency and simplified management. Only
LAG interfaces can reference persona LAG templates. The persona LAG name cannot use reserved interface
names or formats, such as vlan, lag, or loopback. Configurations defined in a persona LAG are valid only for
LAG interfaces.

Public

interface persona lag 52

The no form of this command deletes the persona LAG interface.

Parameter

Description

Specifies the name of the persona LAG.

<NAME>

Usage

Keep in mind the following requirements when adding interfaces to a LAG:

•  Persona LAG names must not match reserved interface names or formats (e.g., vlan, lag, loopback).

•  Only LAG interfaces can use persona LAGs.

•  Configuration applied to a persona LAG is only applicable to LAG interfaces.

•  The persona LAG name is case-sensitive and can contain up to 54 characters.

•  Names can include any characters, but avoid spaces or characters that may interfere with CLI parsing.

•  Multi-chassis LAG interfaces do not support personas.

Examples

Creating a persona LAG template:

switch(config)# interface persona lag server-uplink

switch(config-persona-lag)# no shutdown

switch(config-persona-lag)# mtu 9000

switch(config-persona-lag)# description "Server uplink template"

Deleting a persona LAG template:

switch(config)# no interface persona lag server-uplink

Command History

Release

Modification

10.17.1000

Command introduced on 10040 Switch Series.

10.17

Command introduced.

Public

interface persona lag 53

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

ip address

Syntax

ip address <IPV4-ADDR>/<MASK> [secondary]

no ip address <IPV4-ADDR>/<MASK> [secondary]

Description

Sets an IPv4 address and subnet mask to a LAG interface. One primary and up to 31 secondary address can
be configured per interface.

The no form of this command removes the IPv4 address from the interface.

Parameter

Description

Specifies an IP address in IPv4 format (x.x.x.x), where x is a de
cimal number from 0 to 255. You can remove leading zeros. For
example, the address 192.169.005.100 becomes 192.168.5.1
00.

Specifies the number of bits in the address mask in CIDR format
(x), where x is a decimal number from 0 to 32.

Specifies a secondary IP address.

<IPV4‐ADDR>

<MASK>

secondary

Examples

Setting an IP address on the LAG interface 1 to 198.51.100.1 with a mask of 24 bits:

switch(config)# interface lag 1

switch(config-lag-if)# ip address 198.51.100.1/24
Removing the IP address 198.51.100.1 with a mask of 24 bits from LAG interface 1:

Public

ip address 54

switch(config)# interface lag 1

switch(config-lag-if)# no ip address 198.51.100.1/24

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

5420

6200

6300

6400

8100

8320

8325

8325H

8325P

8360

8400

9300

9300S

10000

10040

ipv6 address

Public

ipv6 address 55

Syntax

ipv6 address <IPV6-ADDR>/<MASK>

no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets an IPv6 address and subnet mask to a LAG interface.

The no form of this command removes the IPv6 address from the interface.

Parameter

Description

Specifies the IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:
xxxx:xxxx:xxxx:xxxx), where x is a hexadecimal number from
0 to F. You can use two colons (::) to represent consecutive zero
s (but only once), remove leading zeros, and collapse a quartet
of four zeros to a single 0. For example, this address 2222:00
00:3333:0000:0000:0000:4444:0055 becomes 2222:0:3333:
:4444:55.

Specifies the number of bits in the address mask in CIDR format
(x), where x is a decimal number from 0 to 128.

<IPV6‐ADDR>

<MASK>

Examples

Setting the IPv6 address on LAG interface 1 to 2001:0db8:85a3::8a2e:0370:7334 with a mask of 24 bits:

switch(config)# interface lag 1

switch(config-lag-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Removing the IP address 2001:0db8:85a3::8a2e:0370:7334 with mask of 24 bits with a mask of 24 bits
from LAG interface 1:

switch(config)# interface lag 1

switch(config-lag-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Command History

Release

Modification

10.07 or earlier

‐‐

Public

ipv6 address 56

Command Information

Platforms

Command context

Authority

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

5420

6200

6300

6400

8100

8320

8325

8325H

8325P

8360

8400

9300

9300S

10000

10040

lacp fallback

Syntax

lacp fallback

no lacp fallback

Description

Configures the LACP fallback on LAG port.

The no form of this command sets the LAG to BLOCK state if no LACP partner is detected.

Usage

This makes members of the LAG function as non-bonded interfaces when no LACP partner is detected. This
configuration is only applicable when the LAG is of type MCLAG. If the member port does not get an LACP
frame, the port is in IE state.

Public

lacp fallback 57

Examples

Configuring LACP fallback on LAG port.

switch(config)# int lag 1 multi-chassis

switch(config-lag-if)# no sh

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# lacp fallback

Configuring the LAG to BLOCK state when no LACP partner is detected.

switch(config)# int lag 1 multi-chassis

switch(config-lag-if)# no sh

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# no lacp fallback

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐if
config‐lag‐if

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6200

6400

8100

8320

8325

8325H

8325P

8400

9300

9300S

10000

10040

Public

lacp fallback 58

lacp fallback-static

Syntax

lacp fallback-static

no lacp fallback-static

Description

Configures the LACP fallback-static on LAG port.

The no form of this command sets the LAG to BLOCK state if no LACP partner is detected.

Usage

This makes members of the LAG function as non-bonded interfaces when no LACP partner is detected.
One member interface that is part of the LAG stays up and forwards traffic, while the other members are in
lacp-block state. This configuration is applicable when the lag is of type LACP and ignored in other cases.
When this command is configured, only one member of LAG is selected to be UP. Enabling multiple members
results in configuration mismatch on peer, loop, mac-learning issues, and more.

Examples

Configuring LACP fallback-static on LAG port.

switch(config)# interface lag 1

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# lacp fallback-static

Configuring the LAG to BLOCK state when no LACP partner is detected.

switch(config)# interface lag 1

switch(config-lag-if)# no lacp fallback-static

Configuring LACP fallback-static on static port.

switch(config-lag-if)# lacp fallback-static
Cannot enable LACP fallback-static on static LAG.

Release

10.11

Modification

Command introduced.

Public

lacp fallback-static 59

Command Information

Platforms

Command context

Authority

All platforms

config‐if
config‐lag‐if

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

lacp hash

Syntax

lacp hash [l2-src-dst | l3-src-dst | l4-src-dst]

no lacp hash [l2-src-dst | l3-src-dst | l4-src-dst]

Description

Controls the selection of an interface in a group of aggregate interfaces. The hash type value helps transmit
a frame. This configuration must be done at the global level.

Parameter

l2‐src‐dst

l3‐src‐dst

l4‐src‐dst

Example

Description

Specifies the load‐balancing calculation to include only layer
2 items, such as source and destination MAC addresses.

Specifies the load‐balancing calculation to include only layer
3 items, such as source and destination IP addresses.

Specifies the load‐balancing calculation to include only layer
4 items, such as source and destination UDP/TCP ports.

switch(config)# lacp hash l2-src-dst

Command History

Release

Modification

10.07 or earlier

‐‐

Public

lacp hash 60

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

6000

6100

8400

9300

lacp mode

Syntax

lacp mode {active | passive}

no lacp mode {active | passive}

Description

Sets an LACP mode to active or passive.

The no form of this command sets the LACP mode to off, returning the LAG to a static mode aggregation.

Parameter

active

passive

Description

Specifies that the local switch will transmit LACP Data Units (L
ACPDUs) to attempt to negotiate with the remote device.

Specifies that the local switch will listen for LACPDUs from the
remote device for LACP negotiation.

NOTE

A momentary traffic drop occurs because LACP
partners reconverge when changing the mode f
rom active to passive or from passive to active.

Examples

Setting the LACP mode to  active :

Public

lacp mode 61

switch(config)# interface lag 1

switch(config-lag-if)# lacp mode active

Setting the LACP mode to  off :

switch(config)# interface lag 1

switch(config-lag-if)# no lacp mode active

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

lacp port-id

Syntax

lacp port-id <PORT-ID>

no lacp port-id

Description

Sets the LACP port ID value of the member interface of the LAG.

The no form of this command removes the LACP port ID value from the interface.

Parameter

Description

Specifies a port ID value. Range: 1 to 65535.

<PORT‐ID>

Public

lacp port-id 62

Examples

Setting an LACP port ID to a value of 10:

switch(config-if)# lacp port-id 10

Removing the LACP port ID value:

switch(config-if)# no lacp port-id

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐if

Administrators or local user group members with execution righ
ts for this command.

lacp port-priority

Syntax

lacp port-priority <PORT-PRIORITY>

no lacp port-priority

Description

Sets an LACP port priority value for the member interface of the LAG.

The no form of this command reverts the LACP port priority to the default, which is 1.

Parameter

Description

Specifies a port priority value. Range: 1 to 65535.

Public

lacp port-priority 63

Parameter

<PORT‐PRIORITY>

Description

Examples

Setting a LACP port priority value of 10:

switch(config-if)# lacp port-priority 10

Reverting the LACP port ID to the default:

switch(config-if)# no lacp port-priority

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐if

Administrators or local user group members with execution righ
ts for this command.

lacp rate

Syntax

lacp rate {fast | slow}

no lacp rate {fast | slow}

Description

Sets an LACP heartbeat request time to fast or slow.

The no form of the command sets an LACP rate to slow.

Public

lacp rate 64

Parameter

fast

slow

Examples

Description

Specifies the heartbeat request to every second, and the timeo
ut period is a three‐consecutive heartbeat loss that is 3 secon
ds.

Specifies the heartbeat request to every 30 seconds. The timeo
ut period is three‐consecutive heartbeat loss that is 90 secon
ds. Default setting.

Setting the LACP heartbeat request time to  fast :

switch(config)# interface lag 1

switch(config-lag-if)# lacp rate fast

Resetting the LACP heartbeat request time to the default, which is  slow :

switch(config)# interface lag 1

switch(config-lag-if)# no lacp rate

Another way to set the LACP heartbeat request time to the default, which is  slow :

switch(config)# interface lag 1

switch(config-lag-if)# lacp rate slow

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

Public

lacp rate 65

lacp system-priority

Syntax

lacp system-priority <SYSTEM-PRIORITY-VALUE>

no lacp system-priority <SYSTEM-PRIORITY-VALUE>

Description

Sets a Link Aggregation Control Protocol (LACP) system priority.

The no form of this command sets an LACP system priority to the default, which is 65534.

Parameter

Description

Specifies a system priority value. Range: 0 to 65535.

<SYSTEM‐PRIORITY‐VALUE>

Examples

Setting a Link Aggregation Control Protocol (LACP) system priority to 100:

switch(config)# lacp system-priority 100

Setting an LACP system priority to the default (65534):

switch(config)# no lacp system-priority

A momentary traffic drop can be seen in case the LACP state machine must renegotiate.

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

Public

lacp system-priority 66

lag

Syntax

lag <ID>

no lag <ID>

Description

Adds an interface to a specified LAG interface ID.

The no form of this command removes an interface from a specified LAG interface ID. The member
loses its LACP configuration when removed from the LAG. The member also reaches the default state
with an administrative shutdown. For 6300 and 6400 series switches, the administrative state is enabled.
Configurations, such as MTU and UDLD, are retained.

Parameter

Description

Specifies a LAG interface ID. Range: 1 to 256.

<ID>

Usage

•  All members of the LAG must have the same speed. If a member comes up late with a different speed,
it will not participate in the LAG/LACP. The hardware restriction is applied before adding an interface
to LAG. The member belongs to the card type that has the same maximum speed as the reference port
card type.

•  To move an interface from LagA to LagB, first remove the interface from LagA and then add it to

LagB. When a member is attached to a LAG, the nondefault configurations on the member are removed
silently.

•  After removing a physical interface from a LAG, the interface associated with the LAG becomes L3 ports
with default L3 configurations and administrative down. For example, suppose interface 1/1/1 was part
of LAG 3 and you had administratively enabled the interface. If you later remove interface 1/1/1 from
LAG 3, the administrative status automatically changes to down. If you want to use the interface again,
you must administratively enable it again.

Examples

Adding an interface to a Link Aggregation Group (LAG) represented by an ID of 100:

Public

lag 67

switch(config)# interface 1/1/1

switch(config-if)# lag 100

Deleting an interface from a Link Aggregation Group (LAG) represented by an ID of 100:

switch(config)# interface 1/1/1

switch(config-if)# no lag 100

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐if

Administrators or local user group members with execution righ
ts for this command.

persona custom

Syntax

persona custom <NAME> {copy | attach}

no persona custom <NAME> {copy | attach}

Description

Assigns a persona LAG (Link Aggregation Group) to a LAG interface. The persona LAG is used to apply a
common configuration to multiple LAGs. There are two modes for applying a persona LAG:  copy  and  at
tach .

The no form of this command deletes the persona LAG.

Parameter

Description

Specifies the custom interface persona name. Range: 1 to 54 ch
aracters.

Public

persona custom 68

Parameter

<NAME>

copy

attach

Description

Performs a one‐time copy of the template LAG configuration.
Subsequent changes to the template are not applied. If the spec
ified persona LAG does not exist, the system displays the messa
ge  persona LAG <name> not found .

Performs an initial copy of the template LAG configuration, and
any subsequent changes to the template are automatically appl
ied to all attached LAGs. The template LAG does not need to ex
ist before other LAGs are attached to it. After attachment, the c
opied settings can be modified on an individual LAG. However,
any later change to the template overwrites the modified values
with the updated template values. Existing LAG configuration p
rior to attachment is discarded and is not restored if the templ
ate is removed.

Usage

Keep in mind the following when assigning a persona LAG:

•  Only LAG interfaces can be assigned a persona LAG.

•  Physical interfaces cannot be assigned a persona LAG.

•  When using the  copy  option, the persona LAG must exist before it can be used; for the  attach

option, it is created if it does not already exist.

•

If a persona LAG is deleted, all LAGs referencing it retain their last applied settings.

•  LAG configuration that existed prior to attaching a persona LAG is discarded and is not restored if the

template is removed.

•  When using the  attach  option, changes to the persona LAG template are immediately applied to all

attached LAGs.

Examples

Creating a persona LAG template and assigning it to a LAG with the  attach  option:

switch(config)# interface persona lag server-uplink

switch(config-persona-lag)# mtu 9000
switch(config-persona-lag)# description "Server uplink LAG"
switch(config-persona-lag)# exit

switch(config)# interface lag 10

switch(config-lag-if)# persona custom server-uplink attach

Public

persona custom 69

Creating a persona LAG template and assigning it to a LAG with the  copy  option:

switch(config)# interface persona lag server-uplink

switch(config-persona-lag)# mtu 9000

switch(config-persona-lag)# description "Server uplink LAG"

switch(config-persona-lag)# exit

switch(config)# interface lag 11

switch(config-lag-if)# persona custom server-uplink copy

switch(config-lag-if)# end

Removing a persona LAG from a LAG:

switch(config)# interface lag 11

switch(config-lag-if)# no persona custom server-uplink attach

Removing a persona LAG assignment completely:

switch(config)# interface lag 11

switch(config-lag-if)# no persona custom server-uplink

Command History

Release

Modification

10.17.1000

Command introduced on 10040 Switch Series.

10.17

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

show interface

Public

show interface 70

Syntax

show interfaces <LAG-NAME>

             [vsx-peer]

Description

Displays information about a specific LAG.

Parameter

<LAG‐NAME>

vsx‐peer

Description

Specifies a LAG name.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Examples

Displaying information about LAG 100:

switch# show interface lag100

Aggregate lag100 is up

 Admin state is up

 Description :

 MAC Address                 : 48:0f:cf:af:43:9c

 Aggregated-interfaces       : 1/1/2

 Aggregation-key             : 100

 Aggregate mode              : active

 Speed                       : 2000 Mb/s

 L3 Counters: Rx Disabled, Tx Disabled

 qos trust none

 VLAN Mode: access

 Access VLAN: 1

 Statistics                      RX                   TX

Total

 ------------- -------------------- --------------------

--------------------

 Packets                         20                   45

65

   Unicast                        5                    5

Public

show interface 71

10

   Multicast                      5                   15

20

   Broadcast                     10                   25

35

 Bytes                         5658                 2584

8242

 Jumbos                           0                    0

0

 Dropped                          0                    0

0

 Filtered                         0                    0

0

 Pause Frames                     0                    0

0

 Errors                           0                    0

0

   CRC/FCS                        0                  n/a

0

   Collision                    n/a                    0

0

   Runts                          0                  n/a

0

   Giants                         0                  n/a

0

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Public

show interface 72

show interface persona

Syntax

show interface persona

Description

Shows all interface personas and their attached interfaces.

Examples

Showing all interface personas and their attached interfaces:

switch(config)# show interface persona

-------------------------------------------------------

Persona           Type              Attached Interfaces

-------------------------------------------------------

access            physical          1/1/1

persona1          physical          1/1/1-1/1/2

persona2          physical          --

access_lag        lag               lag20,lag30

Command History

Release

Modification

10.17.1000

Command introduced on 10040 Switch Series.

10.17

10.12

Added support for persona LAG interfaces.

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

show lacp aggregates

Public

show interface persona 73

Syntax

show lacp aggregates [<LAG-NAME>] [vsx-peer]

Description

Displays all LACP aggregate information configured for all LAGs, or for a specific LAG.

Parameter

Description

Optional: Specifies a lag name.

<LAG‐NAME>

vsx‐peer

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Examples

Displaying LACP aggregate information configured for lag10:

switch# show lacp aggregates lag10

Aggregate-name        : lag10

Aggregated-interfaces : 1/1/1 1/1/2

Heartbeat rate        : slow

Hash                  : l3-src-dst

Aggregate mode        : active
Displaying LACP aggregates:

switch# show lacp aggregates

Aggregate-name        : lag1
Aggregated-interfaces : 1/1/27 1/1/28 1/1/29

Heartbeat rate        : slow

Hash                  : l3-src-dst

Aggregate mode        : active

Aggregate-name        : lag2

Aggregated-interfaces : 1/1/48

Heartbeat rate        : slow

Hash                  : l2-src-dst

Aggregate mode        : passive

Public

show lacp aggregates 74

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show lacp configuration

Syntax

show lacp configuration [vsx-peer]

Description

Displays global LACP configuration.

Parameter

vsx‐peer

Examples

Description

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Displaying global LACP configuration (output is applicable for 8400 series switches):

switch# show lacp configuration
System-id       : 70:72:cf:ef:fc:d9

System-priority : 65534

Hash            : l3-src-dst
Displaying global LACP configuration:

Public

show lacp configuration 75

switch# show lacp configuration

System-id       : 98:f2:b3:68:40:a0

System-priority : 65534

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show lacp interfaces

Syntax

show lacp interfaces [<IFNAME>] [vsx-peer]

Description

Displays an LACP configuration of the physical interfaces, including VSXs. If an interface name is passed as
argument, it only displays an LACP configuration of a specified interface.

Parameter

Description

Optional: Specifies an interface name.

<IFNAME>

vsx‐peer

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Public

show lacp interfaces 76

Examples

This example displays an LACP configuration of the physical interfaces. One of the interfaces has the
lacp-block forwarding state. If a VSX switch has loop protect enabled on an interface and a loop occurs, VSX
blocks the interface to stop the loop. The forwarding state of the blocked interface is set to lacp-block.

switch# show lacp interfaces

State abbreviations :

A - Active        P - Passive      F - Aggregable I - Individual

S - Short-timeout L - Long-timeout N - InSync     O - OutofSync

C - Collecting    D - Distributing

X - State m/c expired              E - Default neighbor state

IE - LACP Fallback mode is active

Actor details of all interfaces:

----------------------------------------------------------------------------

--------

Intf   Aggr    Port    Port   State   System-id          System  Aggr

Forwarding

       name    id      Pri                               Pri     Key  State

----------------------------------------------------------------------------

--------

1/1/1  lag10   17      1      ALFOE   70:72:cf:37:a3:5c  20      10   lacp-

block

1/1/2  lag128  69      1      ALFNCD  70:72:cf:37:a3:5c  20      128  up

1/1/3  lag128  14      1      ALFNCD  70:72:cf:37:a3:5c  20      128  up

1/1/4  lag128                                                         down

1/1/5  lag20                                                          up

Partner details of all interfaces:

----------------------------------------------------------------------------

--

Intf   Aggr    Partner Port     State     System-id       System   Aggr
       name    Port-id Pri                                Priority Key

----------------------------------------------------------------------------

--

1/1/1  lag10   0       65534    PLFOEX  00:00:00:00:00:00 65534    0

1/1/2  lag128  69      1        PLFNCD  70:72:cf:8c:60:a7 65534    128

1/1/3  lag128  14      1        PLFNCD  70:72:cf:8c:60:a7 65534    128

1/1/4  lag128

1/1/5  lag20

Public

show lacp interfaces 77

Displaying static LAG:

NOTE
lacp fallback-staticcannot be configured on static lag. Attempts to configure
lacp fallback-static on a static LAG results in the following message:
Cannot enable LACP-fallback static on static LAG.

switch# show lacp interfaces

State abbreviations :

A - Active        P - Passive      F - Aggregable I - Individual

S - Short-timeout L - Long-timeout N - InSync     O - OutofSync

C - Collecting    D - Distributing

X - State m/c expired              E - Default neighbor state

IE - LACP Fallback mode is active

Actor details of all interfaces:

----------------------------------------------------------------------------

--

Intf   Aggr   Port    Port   State   System-id         System  Aggr

Forwarding

       Name   Id      Pri                              Pri     Key  State

----------------------------------------------------------------------------

--

1/1/1  lag10                                                        up

1/1/2  lag10                                                        up

Partner details of all interfaces:

----------------------------------------------------------------------------

--

Intf   Aggr   Port    Port   State   System-id         System  Aggr

       Name   Id      Pri                              Pri     Key
----------------------------------------------------------------------------

--

1/1/1  lag10

1/1/2  lag10

State abbreviations :

A - Active        P - Passive      F - Aggregable I - Individual

S - Short-timeout L - Long-timeout N - InSync     O - OutofSync

C - Collecting    D - Distributing

X - State m/c expired              E - Default neighbor state

IE - LACP Fallback mode is active

Public

show lacp interfaces 78

Actor details of all interfaces:

----------------------------------------------------------------------------

--

Intf   Aggr   Port    Port   State   System-id         System  Aggr

Forwarding

       Name   Id      Pri                              Pri     Key  State

----------------------------------------------------------------------------

--

1/1/1  lag10                                                        up

1/1/2  lag10                                                        up

Partner details of all interfaces:

----------------------------------------------------------------------------

--

Intf   Aggr   Port    Port   State   System-id         System  Aggr

       Name   Id      Pri                              Pri     Key

----------------------------------------------------------------------------

--

1/1/1  lag10

1/1/2  lag10
Displaying an LACP configuration of the 1/1/1 interface:

switch# show lacp interfaces 1/1/1

State abbreviations :

A - Active        P - Passive      F - Aggregable I - Individual

S - Short-timeout L - Long-timeout N - InSync     O - OutofSync

C - Collecting    D - Distributing

X - State m/c expired              E - Default neighbor state

IE - LACP Fallback mode is active

Aggregate-name : lag1

-------------------------------------------------

                       Actor             Partner

-------------------------------------------------

Port-id            | 28                 | 31

Port-priority      | 1                  | 1

Key                | 1                  | 1

State              | ALFNCD             | ALFNCD

System-id          | 98:f2:b3:68:40:a0  | 98:f2:b3:68:60:a6

System-priority    | 65534              | 65534
Displaying an LACP configuration after loop-protect is enabled on the primary VSX switch:

switch# show lacp interfaces

State abbreviations :

A - Active        P - Passive      F - Aggregable I - Individual

Public

show lacp interfaces 79

S - Short-timeout L - Long-timeout N - InSync     O - OutofSync

C - Collecting    D - Distributing

X - State m/c expired              E - Default neighbor state

IE - LACP Fallback mode is active

Actor details of all interfaces:

----------------------------------------------------------------------------

--

Intf    Aggr       Port  Port  State   System-ID         System Aggr

Forwarding

        Name       Id    Pri                             Pri    Key  State

----------------------------------------------------------------------------

--

1/4/14  lag1(mc)   206   1     ALFNCD  f8:60:f0:06:49:00 65534  1    up

1/5/15  lag2(mc)                                                     down

Partner details of all interfaces:

----------------------------------------------------------------------------

--

Intf    Aggr       Port  Port  State   System-ID         System Aggr

        Name       Id    Pri                             Pri    Key

----------------------------------------------------------------------------

--

1/4/14  lag1(mc)   130   1     ALFNCD  f8:60:f0:06:87:00 65534  1

1/5/15  lag2(mc)
Displaying an LACP configuration after loop-protect is enabled on the secondary VSX switch:

switch# show lacp interfaces

State abbreviations :

A - Active        P - Passive      F - Aggregable I - Individual

S - Short-timeout L - Long-timeout N - InSync     O - OutofSync

C - Collecting    D - Distributing

X - State m/c expired              E - Default neighbor state

IE - LACP Fallback mode is active

Actor details of all interfaces:

----------------------------------------------------------------------------

--

Intf    Aggr       Port  Port  State   System-ID         System Aggr

Forwarding

        Name       Id    Pri                             Pri    Key  State

----------------------------------------------------------------------------

--

Public

show lacp interfaces 80

1/3/2   lag1(mc)   1130  1     ALFNCD  f8:60:f0:06:49:00 65534  1    up

1/9/3   lag2(mc)                                                     down

Partner details of all interfaces:

----------------------------------------------------------------------------

--

Intf    Aggr       Port  Port  State   System-ID         System Aggr

        Name       Id    Pri                             Pri    Key

----------------------------------------------------------------------------

--

1/3/2   lag1(mc)   131   1     ALFNCD  f8:60:f0:06:87:00 65534  1

1/9/3   lag2(mc)
Displaying an LACP configuration with LACP fallback:

switch# show lacp interfaces

State abbreviations :

A - Active        P - Passive      F - Aggregable I - Individual

S - Short-timeout L - Long-timeout N - InSync     O - OutofSync

C - Collecting    D - Distributing

X - State m/c expired              E - Default neighbor state

IE - LACP Fallback mode is active

Actor details of all interfaces:

----------------------------------------------------------------------------

------

Intf       Aggr       Port  Port  State   System-ID         System Aggr

Forwarding

           Name       Id    Pri                             Pri    Key

State

----------------------------------------------------------------------------

------

1/1/4      lag10      5     1     IE      ec:eb:b8:e4:29:00 65534  10   up

1/1/5      lag10      6     1     IE      ec:eb:b8:e4:29:00 65534  10

lacp-block

1/1/6      lag10      7     1     IE      ec:eb:b8:e4:29:00 65534  10

lacp-block

1/3/27     lag10      156   1     IE      ec:eb:b8:e4:29:00 65534  10

lacp-block

1/1/9      lag20(mc)  9     1     IE      ec:eb:b8:e4:29:00 65534  10   up

Partner details of all interfaces:

----------------------------------------------------------------------------

------

Intf       Aggr       Port  Port  State   System-ID         System Aggr

           Name       Id    Pri                             Pri    Key

Public

show lacp interfaces 81

----------------------------------------------------------------------------

------

1/1/4      lag10      0     0     IE      00:00:00:00:00:00 0      0

1/1/5      lag10      0     0     IE      00:00:00:00:00:00 0      0

1/1/6      lag10      0     0     IE      00:00:00:00:00:00 0      0

1/3/27     lag10      0     0     IE      00:00:00:00:00:00 0      0

1/1/9      lag20(mc)  0     0     IE      00:00:00:00:00:00 0      0

Command History

Release

10.18

10.11

10.11

Modification

"IE – LACP Fallback mode is active" added as a state abbreviation.

LACP fallback‐static added.

LACP fallback added on VSX‐supported platforms.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show lag

Syntax

show  lag <LAG-ID>

Description

Displays the lag.

Public

show lag 82

Description

Specifies the lag ID.

Parameter

<LAG‐ID>

Examples

Displaying the lag.

switch# show lag

System-ID       : f4:03:43:80:4a:00

System-priority : 65534

Hash            : l3-src-dst

Aggregate lag1 is down

   Admin state is down

   Description :

   Type                        : normal

   Lacp Fallback               : n/a

   MAC Address                 : f4:03:43:80:4a:00

   Aggregated-interfaces       :

   Aggregation-key             : 1

   Aggregate mode              : static

   LACP rate                   : n/a

   Speed                       : 0 Mb/s

   Mode                        : routed

Aggregate lag128 is down

  Admin state is down

  Description :

  Type                        : normal

  Lacp Fallback               : n/a
  MAC Address                 : f4:03:43:80:4a:00

-- MORE --, next page: Space, next line: Enter, quit: q
Displaying the lag when  lacp fallback-static  is enabled.

switch# show lag

System-ID       : 90:20:c2:24:60:00

System-priority : 65534

Aggregate lag1 is up
   Admin state is up

   Description :

   Type                        : normal

   Lacp Fallback               : Enabled

Public

show lag 83

MAC Address                 : 90:20:c2:24:60:00

   Aggregated-interfaces       : 1/1/1 1/1/2 1/1/3 1/1/46 1/1/47 1/1/48

   Aggregation-key             : 1

   Aggregate mode              : active

   Hash                        : l3-src-dst

   LACP rate                   : slow

   Speed                       : 1000 Mb/s

   Mode                        : trunk

Release

10.11

Modification

LACP fallback‐static added.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show running-config interface

Syntax

show running-config interface

   [IFNAME | IFRANGE | lag <LAGNUM.ID> | loopback <NUMBER> | mgmt | persona
| tunnel <ID> | vlan <ID> | vsx-peer | vxlan] {vsx-peer}

Description

Displays the running configuration for the interface.

Parameter

Description

Displays the interface name.

<IFNAME>

Public

show running-config interface 84

Parameter

Description

Displays the PORT identifier range.

<IFRANGE>

lag <LAGNUM.ID>

Displays the LAG interface information. Range: 1 to 4094.

loopback <NUMBER>

Displays the loopback interface information. Range: 0 to 255.

mgmt

persona

Displays the management interface information.

Displays the interface persona information.

tunnel <ID>

Displays the tunnel interface information. Range: 1 to 1255.

•

•

•

◦  gre ip: Displays the details of GRE IPv4 tunnel interface

.

◦  ip 6in4: Displays the details of IPv6 in IPv4 tunnel infor

mation.

◦  ip 6in6: Displays the details of IPv6 in IPv6 tunnel infor

mation.

Displays the VLAN interface information. Range: 1 to 4094.

Shows the output from the VSX peer switch. If the switches do
not have the VSX configuration or the ISL is down, the output f
rom the VSX peer switch is not displayed. This parameter is avai
lable on switches that support VSX.

Displays the VXLAN interface information. Default: 1.

vlan <ID>

vsx‐peer

vxlan

Examples

Displaying the running configuration for the interface.

switch# show running-config interface

interface lag 10

    no shutdown

    mtu 9000

Public

show running-config interface 85

description "Server uplink LAG"

    persona custom server-uplink attach

interface lag 11

    no shutdown

    mtu 9000

    description "Server uplink LAG"

    persona custom server-uplink

interface persona lag server-uplink

    no shutdown

    mtu 9000

    description "Server uplink LAG"
Displaying the running configuration for interface lag.

switch# show running-config interface lag

interface lag 10 multi-chassis

   no shutdown

   no routing

   vlan trunk native 1

   vlan trunk allowed 10-12

   lacp mode active

   exit

interface lag 11 multi-chassis

   no shutdown

   no routing

   vlan trunk native 1

   vlan trunk allowed 10-12,2001

   lacp mode active

   exit

interface lag 256

   description VSX_ISL

   no shutdown

   no routing

   vlan trunk native 1 tag

   vlan trunk allowed all

   lacp mode active

   exit
Displaying the running configuration for interface lag with lacp fallback-static configured.

switch# show running-config interface lag

interface lag 1
   no shutdown
   no routing

   vlan trunk native 1

   vlan trunk allowed all

Public

show running-config interface 86

lacp mode active

   lacp fallback-static
Displaying the running configuration for interface persona.

switch# show running-config interface persona

interface persona access

    shutdown

    no routing

    vlan access 1

    exit

interface persona persona1

    shutdown

    no routing

    vlan access 1

    exit

interface persona persona2

    shutdown

    no routing

    vlan access 1

    exit

Command History

Release

10.17

Modification

Added support for persona LAG interfaces.

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

shutdown

Public

shutdown 87

Syntax

shutdown

no shutdown

Description

Sets every interface in the LAG operationally down.

The no form of this command sets every interface operationally up.

Examples

Setting every interface in the LAG to shutdown:

switch(config)# interface lag 1

switch(config-lag-if)#
Resetting every interface in the LAG to the default (up):

switch(config)# interface lag 1

switch(config-lag-if)# no shutdown

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

All platforms

config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

vlan trunk native

Syntax

vlan trunk native <VLAN-ID>

no vlan trunk native [<VLAN-ID>]

Public

vlan trunk native 88

Description

Assigns a native VLAN ID to a LAG interface.

The no form of this command removes a native VLAN from a LAG interface and assigns VLAN ID 1 as its
native VLAN.

Parameter

Description

<VLAN‐ID>

Maximum number of VLANs supported: 512 (4100i)

Specifies the number of the VLAN ID to assign. The VLAN ID m
ust exist.

Maximum number of VLANs supported: 512 (6000 and 6100)

Maximum number of VLANs supported: 2048 (5420, 6200)

Maximum number of VLANs supported: 4096 (6300, 6400)

Maximum number of VLANs supported: 4096 (8320)

Maximum number of VLANs supported: 4096 (8325)

Maximum number of VLANs supported: 4096 (10000)

Maximum number of VLANs supported: 4096 (9300/9300S)

Maximum number of VLANs supported: 4096 (8360)

Maximum number of VLANs supported: 1024 (8100)

Maximum number of VLANs supported: 4096 (8400)

VLAN ID range: 2 to 4094.

Usage

By default, VLAN ID 1 is assigned as the LAG VLAN ID for all LAG interfaces. VLANs can only be assigned to
a nonrouted (layer 2) interface or LAG interface.

Only one VLAN ID can be assigned as the native VLAN. For the interface to forward the native VLAN traffic,
the interface has to be allowed explicitly by entering vlan trunk allowed <ID> where the ID is the native
VLAN ID. This setting is also applicable to the physical interface.

Examples

Configuring a layer 2 dynamic aggregation group with native VLAN ID 1 assigned to LAG 1:

For HPE Aruba Networking 5420, 6000, 6100, and 6200 Switch series:

switch(config)# interface lag 1
switch(config-lag-if)# no shutdown

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# vlan trunk native 1

switch(config-lag-if)# vlan trunk allowed 1

Public

vlan trunk native 89

For HPE Aruba Networking 6300, 6400, 8100, 8320, 8325, 8360, 8400, 9300/9300S, and 10000 Switch
series:

switch(config)# interface lag 1

switch(config-lag-if)# no shutdown

switch(config-lag-if)# no routing

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# vlan trunk native 1

switch(config-lag-if)# vlan trunk allowed 1

Configuring a layer 2 dynamic aggregation group with native VLAN ID 20 assigned to LAG 1:

For HPE Aruba Networking 5420, 6000, 6100, and 6200 Switch series:

switch(config)# interface lag 1

switch(config-lag-if)# no shutdown

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# vlan trunk native 20

switch(config-lag-if)# vlan trunk allowed 20

For HPE Aruba Networking 6300, 6400, 8100, 8320, 8325, 8360, 8400, 9300/9300S, and 10000 Switch
series:

switch(config)# interface lag 1

switch(config-lag-if)# no shutdown

switch(config-lag-if)# no routing

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# vlan trunk native 20

switch(config-lag-if)# vlan trunk allowed 20

Removing a native VLAN from LAG 1:

switch(config)# interface lag 1

switch(config-lag-if)# no vlan trunk native

Command History

Release

Modification

10.07 or earlier

‐‐

Public

vlan trunk native 90

Command Information

Platforms

Command context

Authority

All platforms

config‐if
config‐lag‐if

Administrators or local user group members with execution righ
ts for this command.

Smartlink

Smartlink provides simple and fast-converging link redundancy in network topologies with dual uplink
between different layers of the network. It requires an active (primary) and backup (secondary) link. The
active link carries the traffic. If the active link fails, a switchover is triggered and the traffic is directed to the
backup link.

The active interface forwards traffic for a group of VLANs (referred to as protected VLAN group). The
secondary interface is in backup mode for this protected group. If the active port goes down, the backup
port starts forwarding traffic for the protected VLAN group. If the active port recovers, it switches to backup
mode and does not forward traffic. Secondary port continues forwarding traffic.

If preemption is enabled, a failed active port (that has recovered) becomes active after the configured
"preemption-delay" time has elapsed.

Smartlink is supported by the following switch platforms:

•  4100 Switch Series

•  5420 Switch Series

•  6000 Switch Series

•  6100 Switch Series

•  6200 Switch Series

•  6300 Switch Series

•  6400 Switch Series

•  8100 Switch Series

•  8360 Switch Series

Benefits

Smartlink provides faster failover compared to STP. If an active link fails, a Smartlink group contains
configuration information that determines which port should be forwarding for a protected VLAN group.

Public

Smartlink 91

Subtopics

Guidelines and limitations
Smartlink commands

Guidelines and limitations

•  For faster convergence of routed traffic over Smartlink ports, ip neighbor-flood must be enabled on

respective SVI interfaces.

•  Smartlink uses ERPS copp class for flush packets.

•  The Aruba 6000 and 6100 Switch Series use separate Smartlink coPP policies as ERPS is not supported

in matrix platforms.

Limitations:

•  VSX, ISL and MCLAGs cannot be included in Smartlink groups.

•  Switches with both Smartlink and STP enabled exclude Smartlink ports from STP.

•  On switches with both Smartlink and STP enabled, loops involving Smartlink and STP are not detected.

•  On switches with both Smartlink and ERPS enabled, loops involving Smartlink and ERPS are not

detected.

•  ERPS and Smartlink cannot be enabled on the same port.

•  Dynamic VLANs (MVRP) and Smartlink cannot be enabled on the same port.

•  Loop Protect and Smartlink cannot be enabled on the same port.

•  Multicast fast convergence is not supported.

•  Uplink Failure Detection (UFD) is not supported.

Public

Guidelines and limitations 92

•  MIB and WebUI are not supported.

NOTE

•  VLANs that include Smartlink ports must be included in the protected VLAN
list of at least one Smartlink group. If a VLAN includes Smartlink ports and is
not included in the protected VLAN list, the VLAN-port combination will not
be managed by Smartlink or STP, resulting in an undefined port state for the
VLAN, which will cause a loop in the network.

•  When using UDLD with Smartlinks, redundancy switchover is not hitless and

will result in traffic loss.

Smartlink commands

Select a command from the list in the left navigation menu.

Subtopics

Configuration commands
Group context commands
Display commands
Supportability commands

Configuration commands

Select a command category from the list in the left navigation menu.

Subtopics

smartlink group
smartlink recv-control-vlan

smartlink group

Public

Smartlink commands 93

Syntax

smartlink group <GROUP-ID>

no smartlink group <GROUP-ID>

Description

Creates a Smartlink group with specified ID.

The no form of this command removes the Smartlink group and all associated configurations for a specified
ID.

Parameter

Description

Specifies ID for the Smartlink group.

<GROUP‐ID>

Usage

The maximum number of Smartlink groups is 24.

Examples

Configuring a Smartlink group:

switch(config)# smartlink group 2

switch(config-smartlink-2)#

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

Public

smartlink group 94

Platforms

Command context

Authority

6300

6400

8100

8360

smartlink recv-control-vlan

Syntax

smartlink recv-control-vlan <VID-LIST>

no smartlink recv-control-vlan <VID-LIST>

Description

Configures control VLANs to receive flush messages.

The no form of this command disables VLANs from receiving flush messages.

Description

Specifies VLAN ID.

Parameter

<VID‐LIST>

Usage

•  Configure this command on uplink devices where MAC flush is required.

•  A flush message clears stale MAC and ARP entries enabling fast traffic convergence.

Examples

Configuring control VLAN to receive flush messages:

switch(config)# smartlink recv-control-vlan 2,3

Public

smartlink recv-control-vlan 95

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

6300

6400

8100

8360

Group context commands

Select a command category from the list in the left navigation menu.

Subtopics

description
diag-dump smartlink basic
primary-port
smartlink group secondary-port
control-vlan
protected-vlans
preemption
preemption-delay

Public

Group context commands 96

description

Syntax

description <DESC>

no description

Description

Adds description to a Smartlink group.

The no form of this command removes a description from a Smartlink group.

Parameter

Description

Specifies description for a Smartlink group. 1 to 64 printable AS
CII characters are allowed.

<DESC>

Examples

Adding a description to a Smartlink group:

switch(config)# smartlink group 3

switch(config-smartlink-3)# Description for group 3

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐
smartlink‐
<GROUP>

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

6300

Public

description 97

Platforms

Command context

Authority

6400

8100

8360

diag-dump smartlink basic

Syntax

diag-dump smartlink basic

Description

Dumps the Smartlink configuration, state and statistics.

Examples

Dump of Smartlink configuration, state, and statistics:

switch# diag-dump smartlink basic

=========================================================================

[Start] Feature smartlink Time : Tue Jul  7 10:08:31 2020

=========================================================================

-------------------------------------------------------------------------

[Start] Daemon smartlinkd

-------------------------------------------------------------------------

SL Group 1: Primary port 1/1/1 Secondary port 1/1/2 Control VLAN 4,

            Preemption disabled, Preemption-delay 1 Preemption Timer OFF,

            State primary_with_backup, Active port PRIMARY, Backup port

SECONDARY

Port 1/1/1: member_groups 1 SL Groups ids: 1, 0

Port 1/1/2: member_groups 1 SL Groups ids: 1, 0

or

SL Group 1: Primary port lag1   (mclag: local_up_remote_up)

            Secondary port lag2 (mclag: local_down_remote_up), Control VLAN

4,

            Preemption disabled, Preemption-delay 1 Preemption Timer OFF,

            State primary_with_backup, Active port PRIMARY, Backup port

SECONDARY

Port lag1: member_groups 1 SL Groups ids: 1, 0

Port lag2: member_groups 1 SL Groups ids: 1, 0

Public

diag-dump smartlink basic 98

VSX Oper Status: Primary/Secondary/NA

-------------------------------------------------------------------------

[End] Daemon smartlinkd

-------------------------------------------------------------------------

-------------------------------------------------------------------------

[Start] Daemon ops-switchd

-------------------------------------------------------------------------

Group-ID | Port Name | Port Status | Vlan-ID | HW-Port-State | Vlan-Type

1        | 1/1/1     | Active      | 4       | Forwarding    | Control

1        | 1/1/1     | Active      | 3       | Forwarding    | Protected

1        | 1/1/1     | Active      | 2       | Forwarding    | Protected

1        | 1/1/1     | Active      | 1       | Forwarding    | Protected

1        | 1/1/2     | Backup      | 4       | Blocking      | Control

1        | 1/1/2     | Backup      | 3       | Blocking      | Protected

1        | 1/1/2     | Backup      | 2       | Blocking      | Protected

1        | 1/1/2     | Backup      | 1       | Blocking      | Protected

-------------------------------------------------------------------------

[End] Daemon ops-switchd

-------------------------------------------------------------------------

=========================================================================

[End] Feature smartlink

=========================================================================

Diagnostic-dump captured for feature smartlink

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6000

6100

6200

6300

6400

Public

diag-dump smartlink basic 99

Platforms

Command context

Authority

8100

8360

primary-port

Syntax

primary-port <INTERFACE-NAME>

no primary-port

Description

Configures primary port for a Smartlink group.

The no form of this command removes primary port from a Smartlink group.

Parameter

Description

Specifies interface for primary port.

<INTERFACE‐NAME>

Examples

Configuring primary port for a Smartlink group:

switch(config)# smartlink group 3

switch(config-smartlink-3)# primary-port 1/1/1

Command History

Release

Modification

10.07 or earlier

‐‐

Public

primary-port 100

Command Information

Platforms

Command context

Authority

config‐
smartlink‐
<GROUP>

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

6300

6400

8100

8360

smartlink group secondary-port

Syntax

secondary-port <INTERFACE-NAME>

no secondary-port

Description

Configures secondary port for a Smartlink group.

The no form of this command removes secondary port from a Smartlink group.

Parameter

Description

Specifies interface for secondary port.

<INTERFACE‐NAME>

Examples

Configuring secondary port for a Smartlink group:

switch(config)# smartlink group 3

switch(config-smartlink-3)# secondary-port 1/1/2

Public

smartlink group secondary-port 101

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐
smartlink‐
<GROUP>

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

6300

6400

8100

8360

control-vlan

Syntax

control-vlan <VLAN-ID>

no control-vlan <VLAN-ID>

Description

Configures control VLAN in a Smartlink group.

The no form of this command removes control VLAN from a Smartlink group.

Parameter

Description

Specifies VLAN ID for a Smartlink group.

Public

control-vlan 102

Description

Parameter

<VLAN‐ID>

Usage

•

In a Smartlink group, the control VLAN is used to send flush messages.

•  Control VLAN is configured on the device intended to send flush messages.

•  Each Smartlink group must use a unique control VLAN.

•  Control VLAN is protected in the Smartlink group to avoid loops.

Examples

Configuring control VLAN in a Smartlink group:

switch(config)# smartlink group 3

switch(config-smartlink-3)# control-vlan 10

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐
smartlink‐
<GROUP>

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

6300

6400

8100

8360

Public

control-vlan 103

protected-vlans

Syntax

protected-vlans <VLAN-ID-LIST>

no protected-vlans <VLAN-ID-LIST>

Description

Specifies VLANs protected by a Smartlink group.

The no form of this command removes VLANs protected by a Smartlink group.

Parameter

Description

Specifies list of VLAN IDs. Range is 1 to 4094.

<VLAN‐ID‐LIST>

Examples

Configuring protected VLANs for a Smartlink group.:

switch(config)# smartlink group 3

switch(config-smartlink-3)# protected-vlans 1, 10-50

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

5420

6000

config‐
smartlink‐
<GROUP>

Administrators or local user group members with execution righ
ts for this command.

Public

protected-vlans 104

Platforms

Command context

Authority

6100

6200

6300

6400

8100

8360

preemption

Syntax

preemption

no preemption

Description

Configures preemption in a Smartlink group.

The no form of this command disables preemption in a Smartlink group.

Usage

•

•

If preemption is enabled, a recovered primary port preempts the active interface after the configured
preemption delay.

If preemption is disabled, a recovered primary port serves as a backup interface and does not forward
traffic.

Examples

Configuring preemption in a Smartlink group:

switch(config)# smartlink group 3

switch(config-smartlink-3)# preemption

Public

preemption 105

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐
smartlink‐
<GROUP>

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

6300

6400

8100

8360

preemption-delay

Syntax

preemption-delay <SECONDS>

no preemption-delay

Description

Specifies preemption delay for a Smartlink group.

The no form of this command removes previously configured preemption delay from a Smartlink group and
sets it to the default of 1 second.

Parameter

Description

Specifies preemption delay in seconds. Range is 0 to 300 secon
ds.

Public

preemption-delay 106

Description

Parameter

<SECONDS>

Usage

When preemption is enabled, a recovered primary port always preempts the active interface after the
configured preemption delay.

Examples

Configuring preemption delay on a Smartlink group:

switch(config)# smartlink group 3

switch(config-smartlink-3)# preemption

switch(config-smartlink-3)# preemption-delay 10

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

config‐
smartlink‐
<GROUP>

Administrators or local user group members with execution righ
ts for this command.

5420

6000

6100

6200

6300

6400

8100

8360

Public

preemption-delay 107

Display commands

Select a command category from the list in the left navigation menu.

Subtopics

show smartlink group
show smartlink group all
show smartlink group detail
show smartlink flush-statistics
clear smartlink group statistics
clear smartlink flush-statistics
show running-config

show smartlink group

Syntax

show smartlink group <GROUP-ID>

Description

Shows information for a specific Smartlink group.

Parameter

Description

Specifies Smartlink group ID.

<GROUP‐ID>

Examples

Showing Smartlink group information:

switch# show smartlink group 1

Smartlink Group 1 Information:

=============================
Group description         : Uplink1
Protected VLANs           : 20-30

Control VLAN              : 10

Preemption                : ON

Preemption Delay          : 10

Public

Display commands 108

Ports  Role      State      Flush Count Last Flush Time

------ --------- ---------- ----------- -------------------------

1/1/1  Primary   Active     2           Sat Oct 17 19:09:10 2020

1/1/2  Secondary Backup     0

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6000

6100

6200

6300

6400

8100

8360

show smartlink group all

Syntax

show smartlink group all

Description

Shows information for all configured Smartlink groups.

Examples

Showing information for all configured Smartlink groups:

Public

show smartlink group all 109

switch# show smartlink group all

Smartlink Group Information:

=============================

     Primary Secondary  Active  Backup   Ctrl      Preemption Preemption

Grp  Port    Port       Port    Port     Vlan                 Delay

---- ------- ---------  ------  -------  --------- ---------- ----------

1    1/1/1   1/1/2      1/1/1   1/1/2    10          OFF        1

2    1/1/5   1/1/6      1/1/5   1/1/6    11          OFF        1

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6000

6100

6200

6300

6400

8100

8360

show smartlink group detail

Syntax

show smartlink group detail

Description

Shows detailed information for all configured Smartlink groups.

Public

show smartlink group detail 110

Examples

Showing detailed information for all configured Smartlink groups:

switch# show smartlink group detail

Smartlink Group 1 Information:

===============================

Protected VLAN                : 1-3

Control VLAN                  : 1

Preemption                    : OFF

Preemption Delay              : 1

Ports    Role         State        Flush Count  Last Flush Time

-------- ------------ ------------ ------------ ------------------------

1/3/1    Primary      Backup       0

1/3/2    Secondary    Active       0

Smartlink Group 2 Information:

===============================

Protected VLAN                : 4-6

Control VLAN                  : 4

Preemption                    : OFF

Preemption Delay              : 1

Ports    Role         State        Flush Count  Last Flush Time

-------- ------------ ------------ ------------ ------------------------

1/3/2    Primary      Active       0

1/3/1    Secondary    Backup       0

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6000

6100

6200

6300

6400

Public

show smartlink group detail 111

Platforms

Command context

Authority

8100

8360

show smartlink flush-statistics

Syntax

show smartlink flush-statistics

Description

Shows information for received flush messages.

Usage

This command must be executed on an uplink or peer device configured with recv-control-vlan.

Examples

Showing information for received flush messages:

switch# show smartlink flush-statistics

Last Flush Packet Detail:

========================

Flush Packets Received                      : 2

Last Flush Packet Received On Interface     : 1/1/1

Last Flush Packet Received On               : Sat Oct 17 19:09:10 2020

Device Id Of Last Flush Packet Received     : 5065f3-127080

Control VLAN Of Last Flush Packet Received  : 10

Command History

Release

Modification

10.07 or earlier

‐‐

Public

show smartlink flush-statistics 112

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6000

6100

6200

6300

6400

8100

8360

clear smartlink group statistics

Syntax

clear smartlink group [<GROUP-ID>] statistics

Description

Clears Smartlink statistics for the specified Smartlink group or all Smartlink groups.

Parameter

Description

Specifies Smartlink group.

<GROUP‐ID>

Examples

Clearing Smartlink statistics for a specified Smartlink group:

switch# clear smartlink group 1 statistics

Clearing all Smartlink statistics for all Smartlink groups:

switch(config)# clear smartlink group statistics

Public

clear smartlink group statistics 113

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6000

6100

6200

6300

6400

8100

8360

clear smartlink flush-statistics

Syntax

clear smartlink flush-statistics

Description

Clears Smartlink flush statistics.

Usage

This command must be executed on the uplink device configured with recv-control-vlan.

Examples

Clearing Smartlink flush statistics:

switch# clear smartlink flush-statistics

Public

clear smartlink flush-statistics 114

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

5420

6000

6100

6200

6300

6400

8100

8360

show running-config

Syntax

show running-config

Description

Shows current running configuration.

Examples

Showing currently running configuration:

switch# configure terminal

switch(config)# smartlink group 1
switch(config-smartlink-1)# description Uplink1

switch(config-smartlink-1)# primary-port 1/1/1

switch(config-smartlink-1)# secondary-port 1/1/2

switch(config-smartlink-1)# control-vlan 10

Public

show running-config 115

switch(config-smartlink-1)# protected-vlans 20-30

switch(config-smartlink-1)# preemption

switch(config-smartlink-1)# preemption-delay 10

switch(config)# smartlink group 2

switch(config-smartlink-2)# primary-port 1/1/8

switch(config-smartlink-2)# secondary-port 1/1/9

switch(config-smartlink-2)# control-vlan 11

switch(config-smartlink-2)# protected-vlans 20-30

switch# show running-config

Current configuration:

!

!

!

smart-link group 1

  primary-port 1/1/1

  secondary-port 1/1/2

  control-vlan 10

  protected-vlans 20-30

  preemption

  preemption-delay 10

  exit

smart-link group 2

  primary-port 1/1/8

  secondary-port 1/1/9

  control-vlan 11

  protected-vlans 20-30

  exit

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

5420

6000

6100

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Public

show running-config 116

Platforms

Command context

Authority

6200

6300

6400

8100

8360

Supportability commands

Select a command category from the list in the left navigation menu.

Subtopics

show capacities smartlink

show capacities smartlink

Syntax

show capacities smartlink | show capacities-status smartlink

Description

Shows Smartlink capacities or Smartlink capacities and status.

Examples

Showing Smartlink capacities:

switch# show capacities smartlink

System Capacities: Filter SMARTLINK

Capacities

Name                                                                Value

----------------------------------------------------------------------------

--------
Maximum number of SMARTLINK GROUPS configurable in a

system                       24
Showing Smartlink capacities and status:

Public

Supportability commands 117

switch# show capacities-status smartlink

System Capacities Status: Filter SMARTLINK

Capacities Status Name                                                Value

Maximum

----------------------------------------------------------------------------

--------

Number of SMARTLINK GROUPS currently configured

1      24

Command History

Release

Modification

10.07 or earlier

‐‐

Command Information

Platforms

Command context

Authority

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

4100i

5420

6000

6100

6200

6300

6400

8100

8360

UFD (Uplink Failure Detection)

Uplink Failure Detection (UFD) is used to help achieve network path redundancy. UFD monitors (tracks the
forwarding state of) the interfaces/LAGs configured as Links-to-Monitor (LtM) and when all LtM links go
down, UFD disables the interfaces/LAGs configured as Links-to-Disable (LtD). If any of the LtM links come
back up, then all the LtD links are brought back up.

Public

UFD (Uplink Failure Detection) 118

This process triggers the re-convergence of the traffic to the redundant path that is typically set up using
another switch or network. A common example is the teaming NIC software in servers that is used to fail
over from the primary NIC to the secondary NIC upon primary NIC failure.

To avoid unnecessary switching in the downlink redundant path during a frequent network flap in the uplink
ports, delays can be configured. For example, if all the monitored uplinks are still down after the configured
down delay, all the links to disable interfaces/LAGs are brought down. Similarly, if any of the monitored
uplinks are still up after the configured up delay, all the disabled interfaces/LAGs are brought back up.

In this simplistic topology, switch sw2 uses UFD to monitor the links (LtM) to switch sw1, disabling the links
(LtD) to switch sw3 upon failure of the links from switch sw2 to switch sw1. When sw3 detects that the links
from switch sw2 have gone down, it then switches to its redundant path.

NOTE

Although UFD can be used alone, consider using it with Smartlink which
automates fail over from links that have gone down to redundant links. Smartlink
is available on the 5420, 6200, 6300, 6400, 8100, and 8360 Switch Series.

Guidelines and limitations

•  UFD is supported only on L2 interfaces and LAGs. It is not supported on ROP and SVI.

•  UFD is not supported with VSX, meaning that ISL and MCLAGs are not supported.

Subtopics

Basic UFD configuration
UFD (Uplink Failure Detection) commands

Basic UFD configuration

To help understand how to configure UFD, a basic configuration is presented, followed by detailed
descriptions of the available commands under UFD (Uplink Failure Detection) commands.

Enabling UFD:

switch(config)# ufd enable

Creating UFD session 1 and then entering its context:

Public

Basic UFD configuration 119

switch(config)# ufd session-id 1

switch(config-ufd-1)#
Configuring two links to be monitored and two links to disable:

switch(config-ufd-1)# links-to-monitor 1/1/1,1/1/2

switch(config-ufd-1)# links-to-disable 1/1/11,1/1/12

Setting the up and down delays to 10 seconds:

switch(config-ufd-1)# delay down 10

switch(config-ufd-1)# delay up 10

Showing information for UFD session 1:

switch# show ufd session 1

UFD session-id                   : 1

UFD Links-to-Monitor status      : Up

Up Delay                         : 10 sec

Down Delay                       : 10 sec

Links-to-Monitor                 : 1/1/1,1/1/2

Links-to-Disable                 : 1/1/11,1/1/12

Last Links-to-Monitor Down Time  : 2021-11-03 15:22:05:37

UFD (Uplink Failure Detection) commands

Select a command from the list in the left navigation menu.

Subtopics

debug ufd all
delay
links-to-disable
links-to-monitor
show capacities ufd
show running-config ufd
show-tech ufd
show ufd
ufd enable
ufd session-id

Public

UFD (Uplink Failure Detection) commands 120

debug ufd all

Syntax

debug ufd all

no debug ufd all

Description

Enables the UFD debug logs.

The no form of this command disables the UFD debug logs.

Examples

Enabling UFD debug logs:

switch(config)# debug ufd all

Disabling UFD debug logs:

switch(config)# no debug ufd all

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

delay

Public

debug ufd all 121

Syntax

delay {down | up} <DELAY>

no delay {down | up} <DELAY>

Description

Within the selected UFD (Uplink Failure Detection) session context, specifies the amount of time (in
seconds) to delay before bringing up or down the configured Links to Disable (LtD) after the corresponding
Links to Monitor (LtM) come back up or go down.

For example, with delay down 10, when all LtM links go down and remain down after 10 seconds, UFD
disables the interfaces/LAGs configured as Links-to-Disable (LtD). Similarly, with delay up 10, If any of the
LtM links come back up and remain up after 10 seconds, then all the LtD links are brought back up.

NOTE

In addition to any configured delay there is an additional delay of 3 to 5 seconds
before bringing any Links-to-Disable (LtD) down or back up. So with the default
delay of 0 seconds, a delay of 3 to 5 seconds does occur.

The no form of this command restores the delay to its default of 0 seconds.

Parameter

Description

Species the delay in seconds. Range 0 to 180 seconds. Default:
0 seconds.

<DELAY>

Examples

Setting the up and down delays to 10 seconds:

switch(config)# ufd enable

switch(config)# ufd session-id 1

switch(config-ufd-1)# links-to-monitor 1/1/1,1/1/2

switch(config-ufd-1)# links-to-disable 1/1/11,1/1/12

switch(config-ufd-1)# delay down 10

switch(config-ufd-1)# delay up 10

switch(config-ufd-1)# exit

switch(config)#
Resetting the up and down delays to their default of 0:

switch(config-ufd-1)# no delay down 10

Public

delay 122

switch(config-ufd-1)# no delay up 10

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config‐ufd‐<ID>

Administrators or local user group members with execution righ
ts for this command.

links-to-disable

Syntax

links-to-disable <IF/LAG-LIST>

no links-to-disable <IF/LAG-LIST>

Description

Within the selected UFD (Uplink Failure Detection) session context, specifies the interfaces or LAGs to
disable when the monitored uplink interfaces go down.

For proper UFD operation, links-to-disable and links-to-monitor must both be configured. Use command
links-to-monitor to specify a corresponding list of interfaces/LAGs to monitor.

The no form of this command deletes the specified links to disable list within the selected UFD session
context.

NOTE
A LAG member interface cannot be added as a link to disable. A interface
configured as a link to disable cannot be added as a LAG member interface.

Public

links-to-disable 123

Parameter

Description

<IF/LAG‐LIST>

List of L2 interfaces or LAGs. Separate interfaces/LAGs with co
mmas (for individual interfaces/LAGs) or hyphens (for a consec
utive range of interfaces/LAGs).

Examples

Configuring two links to be disabled:

switch(config)# ufd enable

switch(config)# ufd session-id 1

switch(config-ufd-1)# links-to-monitor 1/1/1,1/1/2

switch(config-ufd-1)# links-to-disable 1/1/11,1/1/12

switch(config-ufd-1)# delay down 10

switch(config-ufd-1)# delay up 10

switch(config-ufd-1)# exit

switch(config)#
Configuring a range of interfaces to disable:

switch(config)# ufd session-id 2

switch(config-ufd-2)# links-to-monitor lag18-lag20

switch(config-ufd-2)# links-to-disable 1/1/3-1/1/5

switch(config-ufd-2)# exit

switch(config)#
Deleting the links to disable for two interfaces:

switch(config-ufd-1)# no links-to-disable 1/1/11,1/1/12

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config‐ufd‐<ID>

Administrators or local user group members with execution righ
ts for this command.

Public

links-to-disable 124

links-to-monitor

Syntax

links-to-monitor <IF/LAG-LIST>

no links-to-monitor <IF/LAG-LIST>

Description

Within the selected UFD (Uplink Failure Detection) session context, specifies the uplink interfaces or LAGs to
monitor for UFD.

For proper UFD operation, links-to-monitor and links-to-disable must both be configured. Use command
links-to-disable to specify a corresponding list of interfaces/LAGs to disable if the monitored uplinks go
down.

The no form of this command deletes the specified links to monitor list within the selected UFD session
context.

NOTE

A LAG member interface cannot be added as a link to monitor. A interface
configured as a link to monitor cannot be added as a LAG member interface.

Parameter

Description

List of L2 interfaces or LAGs. Separate interfaces/LAGs with co
mmas (for individual interfaces/LAGs) or hyphens (for a consec
utive range of interfaces/LAGs).

<IF/LAG‐LIST>

Examples

Configuring two uplinks to monitor for UFD session 1:

switch(config)# ufd enable

switch(config)# ufd session-id 1

switch(config-ufd-1)# links-to-monitor 1/1/1,1/1/2

switch(config-ufd-1)# links-to-disable 1/1/11,1/1/12
switch(config-ufd-1)# delay down 10
switch(config-ufd-1)# delay up 10

switch(config-ufd-1)# exit

switch(config)#
Configuring a range of uplink LAGs to monitor for UFD session 2:

Public

links-to-monitor 125

switch(config)# ufd session-id 2

switch(config-ufd-2)# links-to-monitor lag18-lag20

switch(config-ufd-2)# links-to-disable 1/1/3-1/1/5

switch(config-ufd-2)# exit

switch(config)#
Deleting both links to monitor for UFD session 1:

switch(config-ufd-1)# no links-to-monitor 1/1/1,1/1/2

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config‐ufd‐<ID>

Administrators or local user group members with execution righ
ts for this command.

show capacities ufd

Syntax

show capacities ufd
show capacities-status ufd

Description

Command show capacities ufd shows UFD session capacity. Command show capacities-status ufd shows
UFD session capacity and the number of UFD sessions configured.

Example

Showing UFD session capacity:

switch# show capacities ufd

System Capacities: Filter UFD

Capacities

Public

show capacities ufd 126

Name                                                              Value

----------------------------------------------------------------------------

---------

Maximum number of Uplink Failure Detection sessions configurable in a

system  128
Showing UFD session capacity and the number of UFD sessions configured:

switch(config)# show capacities-status ufd

System Capacities Status: Filter UFD

Capacities Status Name

Value Maximum

----------------------------------------------------------------------------

---------

Number of Uplink Failure Detection sessions currently configured

1    128

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show running-config ufd

Syntax

show running-config ufd

Description

Shows the running configuration for UFD.

Public

show running-config ufd 127

Example

Showing the UFD portion of running configuration information:

switch(config)# ufd enable

switch(config)# ufd session-id 1

switch(config-ufd-1)# links-to-monitor 1/1/1,1/1/2

switch(config-ufd-1)# links-to-disable 1/1/11,1/1/12

switch(config-ufd-1)# delay down 10

switch(config-ufd-1)# delay up 10

switch(config-ufd-1)# exit

switch(config)#

switch# show running-config ufd

Current configuration:

ufd enable

ufd session-id 1

    delay up 10

    delay down 10

    links-to-monitor 1/1/1,1/1/2

    links-to-disable 1/1/11,1/1/12

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show-tech ufd

Syntax

show-tech ufd

Public

show-tech ufd 128

Description

Executes the show ufd command followed by the show running-config ufd command.

Example

Running the show ufd command followed by the show running-config ufd command:

switch# show tech ufd

====================================================

Show Tech executed on Tue Nov 23 11:32:08 2021

====================================================

====================================================

[Begin] Feature ufd

====================================================

*********************************

Command : show ufd

*********************************

Global UFD Status : Enabled

UFD session-id                   : 10

UFD Links-to-Monitor status      : Up

Up Delay                         : 20 sec

Down Delay                       : 10 sec

Links-to-Monitor                 : None

Links-to-Disable                 : None

Last Links-to-Monitor Down Time  : None

UFD session-id                   : 20

UFD Links-to-Monitor status      : Up

Up Delay                         : 0 sec

Down Delay                       : 0 sec

Links-to-Monitor                 : None

Links-to-Disable                 : None

Last Links-to-Monitor Down Time  : None

*********************************
Command : show running-config ufd

*********************************

ufd enable

ufd session-id 10

    delay down 10

    delay up 20

    exit

ufd session-id 20

    exit

====================================================

[End] Feature ufd

Public

show-tech ufd 129

====================================================

====================================================

Show Tech commands executed successfully

====================================================

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

show ufd

Syntax

show ufd [session-id <ID>]

Description

Shows information on all UFD sessions or the specified UFD session.

Parameter

Description

Specifies an existing UFD session ID. Range: 1 to 128.

<ID>

Example

Showing information on all configured UFD sessions:

Public

show ufd 130

switch# show ufd

Global UFD Status : Enabled

UFD session-id                   : 1

UFD Links-to-Monitor status      : Up

Up Delay                         : 10 sec

Down Delay                       : 10 sec

Links-to-Monitor                 : 1/1/1,1/1/2

Links-to-Disable                 : 1/1/11,1/1/12

Last Links-to-Monitor Down Time  : 2021-11-03 15:22:05:37

UFD session-id                   : 2

UFD Links-to-Monitor status      : Up

Up Delay                         : 5 sec

Down Delay                       : 5 sec

Links-to-Monitor                 : lag18-lag20

Links-to-Disable                 : 1/1/3-1/1/5

Last Links-to-Monitor Down Time  : 2021-11-01 12:14:42:56
Showing information on UFD session 2:

switch# show ufd session 2

UFD session-id                   : 2

UFD Links-to-Monitor status      : Up

Up Delay                         : 5 sec

Down Delay                       : 5 sec

Links-to-Monitor                 : lag18-lag20

Links-to-Disable                 : 1/1/3-1/1/5

Last Links-to-Monitor Down Time  : 2021-11-01 12:14:42:56

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

Operator ( > ) or Manage
r ( # )

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this c
ommand from the operator context (>) only.

Public

show ufd 131

ufd enable

Syntax

ufd enable

no ufd enable

Description

Enables UFD (Uplink Failure Detection). UFD is disabled by default. This command must be issued before
the configuration that is set with related UFD commands takes effect.

The no form of this command disables UFD.

Examples

Enabling UFD:

switch(config)# ufd enable

switch(config)# ufd session-id 1

switch(config-ufd-1)# links-to-monitor 1/1/1,1/1/2

switch(config-ufd-1)# links-to-disable 1/1/11,1/1/12

switch(config-ufd-1)# delay down 10

switch(config-ufd-1)# delay up 10

switch(config-ufd-1)# exit

switch(config)#
Disabling UFD:

switch(config)# no ufd enable

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

Public

ufd enable 132

ufd session-id

Syntax

ufd session-id <ID>

no ufd session-id <ID>

Description

Creates the specified UFD (Uplink Failure Detection) session and then enters its context. If the specified
session already exists, this command enters its context.

The no form of this command deletes the specified session configuration.

Parameter

Description

Specifies the UFD session ID. Range: 1 to 128.

<ID>

Examples

Creating UFD session 1 and then entering its context:

switch(config)# ufd enable

switch(config)# ufd session-id 1

switch(config-ufd-1)# links-to-monitor 1/1/1,1/1/2

switch(config-ufd-1)# links-to-disable 1/1/11,1/1/12

switch(config-ufd-1)# delay down 10

switch(config-ufd-1)# delay up 10

switch(config-ufd-1)# exit

switch(config)#
Creating UFD session 2 and then entering its context:

switch(config)# ufd session-id 2

switch(config-ufd-2)# links-to-monitor lag18-lag20

switch(config-ufd-2)# links-to-disable 1/1/3-1/1/5

switch(config-ufd-2)# exit

switch(config)#
Deleting UFD session 1:

switch(config)# no ufd session-id 1

Public

ufd session-id 133

Command History

Release

10.09

Modification

Command introduced.

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution righ
ts for this command.

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

AOS‐CX Switch Software Documentation Portal

https://www.hpe.com/us/en/networking/hpe‐aru
ba‐networking‐support‐services.html

https://arubanetworking.hpe.com/techdocs/Aruba
DocPortal/content/new-portal/aoscx.html

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

Public

Support and Other Resources 134

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

HPE Aruba Networking software

https://networkingsupport.hpe.com/downloads h
ttps://networkingsupport.hpe.com/downloads

Software licensing and Feature Packs

https://licensemanagement.hpe.com/

Public

Accessing HPE Aruba Networking Support 135

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
WEEE). For more information, see https://www.arubanetworks.com/company/about-us/environmental-
citizenship/.

Public

Accessing Updates 136

Documentation Feedback

HPE Aruba Networking is committed to providing documentation that meets your needs. To help us improve
the documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition, and
publication date located on the front cover of the document. For online help content, include the product
name, product version, help edition, and publication date located on the legal notices page.

Public

Documentation Feedback 137