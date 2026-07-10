AOS-CX 10.06 Link Aggregation Guide
6100, 6200, 6300, 6400, 8320, 8325, 8360, 8400 Switch Series

Part Number: 5200-7710a
Published: January 2021
Edition: 2

© Copyright 2020, 2021 Hewlett Packard Enterprise Development LP

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

Chapter 1 About this document...................................................................... 5
Applicable products........................................................................................................................................5
Latest version available online......................................................................................................................5
Command syntax notation conventions..................................................................................................... 5
About the examples....................................................................................................................................... 6
Identifying switch ports and interfaces .......................................................................................................7
Identifying modular switch components ....................................................................................................8

Chapter 2 Link Aggregation.............................................................................. 9
Overview.......................................................................................................................................................... 9
Aggregation group, member port, and aggregate interface..................................................................... 9
Link aggregation modes.............................................................................................................................. 10
LACP............................................................................................................................................................... 10
LACP operating modes..................................................................................................................... 10
LAG interface states..................................................................................................................................... 11
How static link aggregation groups are built............................................................................................ 12
How dynamic link aggregation groups are built....................................................................................... 13
LAG configuration guidelines...................................................................................................................... 13
Layer 2 aggregation groups........................................................................................................................ 14
Configuring a Layer 2 static aggregation group............................................................................ 15
Configuring a Layer 2 dynamic aggregation group.......................................................................17
Layer 3 aggregation groups........................................................................................................................ 19
Configuring a Layer 3 static aggregation group............................................................................ 19
Configuring a Layer 3 dynamic aggregation group.......................................................................22
Removing a LAG............................................................................................................................................24
Removing an interface from a LAG............................................................................................................ 25
Changing the LAG membership for an interface......................................................................................26
Configuration of an aggregate interface................................................................................................... 29
Configuring the description of an aggregate interface................................................................ 29
Setting the MTU for a Layer 2 member link interface.................................................................. 29
Setting the MTU for a Layer 3 aggregate interface....................................................................... 30
Impact of shutting down or bringing up an aggregate interface................................................ 30
Shutting down an aggregate interface........................................................................................... 30
Supported hashing algorithms................................................................................................................... 31
LACP configuration settings........................................................................................................................ 31
Interface LACP settings................................................................................................................................ 32
Configuration verification............................................................................................................................33
BFD reports a LAG as down even when healthy links are still available................................................33
LACP and LAG commands........................................................................................................................... 34
description.................................................................................................................................... 34
hash....................................................................................................................................................35
interface lag............................................................................................................................... 35
ip address...................................................................................................................................... 36
ipv6 address..................................................................................................................................37
lacp hash........................................................................................................................................ 38
lacp mode........................................................................................................................................ 38
lacp port-id..................................................................................................................................39
lacp port-priority.................................................................................................................... 40

Contents

3

lacp rate........................................................................................................................................ 40
lacp system-priority................................................................................................................41
lag...................................................................................................................................................... 42
show interface............................................................................................................................. 43
show lacp aggregates................................................................................................................44
show lacp configuration......................................................................................................... 45
show lacp interfaces................................................................................................................45
shutdown...........................................................................................................................................48
vlan trunk native...................................................................................................................... 49

Chapter 3 Support and other resources...................................................... 51
Accessing Aruba Support............................................................................................................................ 51
Accessing updates........................................................................................................................................ 51
Warranty information.................................................................................................................................. 52
Regulatory information............................................................................................................................... 52
Documentation feedback............................................................................................................................ 52

4

AOS-CX 10.06 Link Aggregation Guide

Chapter 1
About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

• Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

• Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

• Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A, JL667A,

JL668A, JL762A)

• Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

• Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

• Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

• Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A, JL711A)

• Aruba 8400 Switch Series (JL375A, JL376A)

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

Table Continued

Chapter 1 About this document

5

Convention

Usage

Any of the following:

• <example-text>

• <example-text>

• example-text

•

example-text

|

{ }

[ ]

… or

...

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

6

AOS-CX 10.06 Link Aggregation Guide

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

On the 6300 Switch Series

• member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

•

slot: Always 1. This is not a modular switch, so there are no slots.

• port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Specifies physical location of a module in the switch chassis.

Chapter 1 About this document

7

◦ Management modules are on the front of the switch in slots 1/1 and 1/2.

◦

Line modules are on the front of the switch starting in slot 1/3.

• port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on member 1.

On the 83xx Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Always 1. These are not a modular switches, so there are no slots.

• port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

NOTE: If using breakout cables, the port designation changes to x:y, where x is the physical port
and y is the lane when split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in
software is associated with lane 2 on physical port 4 in slot 1 on member 1.

On the 8400 Switch Series

• member: Always 1. VSF is not supported on this switch.

•

slot: Specifies physical location of a module in the switch chassis.

◦ Management modules are on the front of the switch in slots 1/5 and 1/6.

◦

Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

• port: Physical number of a port on a line module.

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

AOS-CX 10.06 Link Aggregation Guide

Chapter 2
Link Aggregation

Overview
Ethernet link aggregation bundles multiple physical Ethernet links into one logical link, called a link
aggregation group (LAG).

Link aggregation has the following benefits:

•

•

Increased bandwidth beyond the limits of any single link. In an aggregate link, traffic is distributed across
the member ports.

Improved link reliability. The member ports dynamically back up one another. When a member port fails,
its traffic is automatically switched to other member ports.

As shown in the following figure Device A and Device B are connected by three physical Ethernet links.
These physical Ethernet links are combined into an aggregate link called link aggregation 1. The
bandwidth of this aggregate link can reach up to the total bandwidth of the three physical Ethernet links.
At the same time, the three Ethernet links back up one another. When a physical Ethernet link fails, the
traffic originally intended for the failed link is switched to the remaining active links.

Figure 1: Ethernet link aggregation diagram

Aggregation group, member port, and aggregate
interface
An aggregation group is a collection of physical interfaces that are bundled together for the purpose of load
distribution and redundancy. These physical interfaces are called member ports. They are configured
through a logical aggregate interface.

An aggregate interface can be one of the following types:

• Layer 2: The member ports of the corresponding Link Aggregation Group can only be Layer 2 Ethernet

interfaces.

• Layer 3: The member ports of the corresponding Link Aggregation Group can only be Layer 3 interfaces.

NOTE: Layer 3 aggregation groups are not supported on the 6100 and 6200 Switch Series.

Chapter 2 Link Aggregation

9

Switch AINT1/1/1Switch BLink aggregation 1INT1/1/2INT1/1/3INT1/1/1INT1/1/2INT1/1/3

The effective port rate of an aggregate interface equals the total rate of its member ports. Only full duplex
mode members are eligible for aggregation.

Link aggregation modes
An aggregation group operates in one of the following modes:

• Static LAG: In the static LAG mode of operation, Link failure is not detected as there is no keep alive PDU
communication between the devices. A misconfiguration on one side can cause much trouble and be
difficult to troubleshoot, because no signaling takes place between the two peers.

• Dynamic LAG or LACP: The local device and the peer device automatically maintain the aggregation

states of the member ports, resulting in link failure being quickly detected by exchanging the PDU. LACP
reduces the workload of network administrators.

Dynamic LAG uses LACP packets to establish the association between two peers. This configuration
results in the reduction of the misconfiguration probability. Also, link failures are intelligently handled by
two participating devices through the LACP protocol, which is adaptive/dynamic to these network
failures.

Layer 2 aggregation groups and Layer 3 aggregation groups support both the static and dynamic modes.

LACP
Dynamic aggregation is implemented through the IEEE 802.3ad Link Aggregation Control Protocol (LACP).

LACP uses LACPDUs to exchange aggregation information between LACP-enabled devices. Each member
port in a dynamic aggregation group can exchange information with its peer. When a member port receives
an LACPDU, it compares the received information with information received on the other member ports. In
this way, the two systems agree on which ports are placed in Selected state.

The LACPDU fields convey data for the LACP functions, including:

• System LACP priority

• System MAC address

• Port priority

• Port number

• Operational key

LACP operating modes

LACP can operate in active or passive mode.

• Active mode: When the LACP is operating in active mode on either end of a link, both ports can send

PDUs. The "active" LACP initiates an LACP connection by sending LACPDUs. The "passive" LACP will wait
for the remote end to initiate the link.

• Passive mode: When the LACP is operating in passive mode on a local member port and as its peer port,

both ports cannot send PDUs.

NOTE: Two peer ports operating in "passive" mode will never establish an LACP link.

10

AOS-CX 10.06 Link Aggregation Guide

For an LACP LAG, one side must have LACP in active mode and the peer must have an LACP configuration of
active or passive mode. If you do not enable LACP on a LAG, it is treated as a static LAG and the peer cannot
negotiate LACP with the LAG.

LAG interface states
The output from the CLI commands show lacp interfaces and show lacp interfaces multi-
chassis display the following interface states:

Interface state

Description

A - Active

An active LACP interface.

C - Collecting

Data frames are received through the aggregate link and sent onto the
intended destination.

D - Distributing

Data frames are transmitted through the aggregate link to reach the intended
destination.

F - Aggregable

The link can be used as part of an aggregate.

E - Default neighbor
state

The link has the default state of the neighbor switch.

I - Individual

The link is used as an individual link.

L - Long-timeout

With the long timeout, an LACPDU is sent every 30 seconds. If no response
comes from its partner after three LACPDUs are sent (90 seconds), a timeout
event occurs. The LACP state machine then transitions to the appropriate
state based on its current state.

N - InSync

O - OutofSync

The physical port is connected to the aggregate port that was last chosen by
the logical election. The state variable selected is still true.

The hardware might be out of sync with the modified protocol information. If
the hardware also has a status of collecting, do not transmit frames because
they will be misdelivered.

P - Passive

The port participates in the protocol, as long as it has an active partner.

S - Short-timeout

In the short timeout configuration, an LACPDU is sent every second. If no
response comes from its partner after three LACPDUs are sent, a timeout
event occurs. The LACP state machine then transitions to the appropriate
state based on its current state.

X - State m/c expired The "current while" timer has expired. The "current while" timer then restarts

with the short-timeout enabled.

The term State m/c refers to a state machine.

Chapter 2 Link Aggregation

11

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

Figure 2: Setting the aggregation state of a member port in a static aggregation group

After the maximum limit of members is reached in a LAG, an additional port cannot be added to the
aggregation group. If a port belongs to a card type with a different speed than the other aggregation
members, the port can still be added to the aggregation group. If dynamic LAG is enabled, any port member
with a speed different than other aggregation members is blocked or ineligible from the same aggregation
group. Any operational keys/attributes or configuration changes might affect the aggregation states of the
member ports.

12

AOS-CX 10.06 Link Aggregation Guide

Set the aggregationstate of a member port.Isthere any hardwarerestriction?Morecandidate portsthan max numberof addedports?Isport operationallyup?Operationalkey/Attributes configurationssame as referenceport?Set the portas selected state.Do not add themember in aggregation.Set the portas unselected state.YesYesYesYesNoNoNoNo

How dynamic link aggregation groups are built

Choosing a reference port

The system chooses a reference port from the member ports in up state. A selected port must have the
same operational key and attribute configurations as the reference port.

The process by which the local system (the actor) and the peer system (the partner) negotiate a reference
port occurs as follows:

1. The two systems determine the system with the smaller system ID.

A system ID contains the system LACP priority and the system MAC address.

a. The two systems compare their LACP priority values.

The lower the LACP priority, the smaller the system ID. If the LACP priority values are the same, the
two systems proceed to step b.

b. The two systems compare their MAC addresses.

The lower the MAC address, the smaller the system ID.

2. The system with the smaller system ID chooses the first operationally up port as the reference port.

A port ID contains a port priority and a port number. The lower the port priority, the smaller the port ID.

Setting the aggregation state of each member port

After the reference port is chosen, the system with the smaller system ID sets the state of each member
port on its side.

The system with the greater system ID can detect the aggregation state changes on the peer system. The
system with the greater system ID sets the aggregation state of local member ports the same as their peer
ports.

When you aggregate interfaces in dynamic mode, follow these guidelines:

• A dynamic link aggregation group chooses only full-duplex ports as the selected ports.

•

For stable aggregation and service continuity, do not change the operational key or attribute
configurations on any member port.

LAG configuration guidelines

Aggregation member interface restrictions

•

If any features in the following list are configured on the interface, you cannot assign an interface to a
Layer 2 aggregation group:

◦ MAC authentication

◦ Port security

◦ 802.1X

• Do not assign a reflector port for port mirroring to an aggregation group.

Chapter 2 Link Aggregation

13

Requirements for adding interfaces

Keep in mind the following requirements when adding interfaces to a LAG:

• To determine the maximum number of LAG interfaces for your type of switch, look at the output from
the show capacities lag command; however, the number of LAGs that can be created depends on
the availability of the physical interface since each LAG interface needs at least one physical interface as a
member link.

After the maximum limit of members is reached in a LAG, an additional port cannot be added to the
aggregation group. If a port belongs to a card type with a different speed than the other aggregation
members, the port can still be added to the aggregation group. If dynamic LAG is enabled, any port
member with a speed different than other aggregation members is blocked or ineligible from the same
aggregation group. Any operational keys/attributes or configuration changes might affect the aggregation
states of the member ports.

• The nondefaults configuration on an interface is removed automatically when the interface is added to a
link aggregation. For example: Assume that you remove a member interface from an existing LAG and
add it to another LAG. The software removes the nondefault configurations on the interface when it is
added to the new LAG.

Configuration consistency requirements

• Configure at least one active mode aggregation in two devices.

•

•

For a successful static aggregation, make sure the ports at both ends of each link are in the same
aggregation state.

For a successful dynamic aggregation, make sure the peer ports of the ports aggregated at one end are
also aggregated, and that one of the ends is configured as "active". The two ends can automatically
negotiate the aggregation state of each member port.

Removing interfaces

• Deleting an aggregate interface also deletes its aggregation group and causes all member ports to leave

the aggregation group.

• When a member interface is removed from a LAG:

◦ 6100, 6200, 6300, and 6400 switches: The interface goes to its default status of unshut.

◦ 8320, 8325, 8360, or 8400 switches: The interface becomes disabled.

Disabling an interface

When an interface LAG is disabled with the shutdown command, all its members also become operationally
down.

Layer 2 aggregation groups
All switches support static and dynamic layer 2 aggregation groups.

NOTE: On the 6400 Switch Series, port identification differs. Line card ports start at 1/3/1.

14

AOS-CX 10.06 Link Aggregation Guide

Configuring a Layer 2 static aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Create a Layer 2 aggregate interface and access the Layer 2 aggregate interface view by entering:

switch(config)# interface lag <ID>

The range of the LAG interface ID is 1 to 256.

While creating the Layer 2 aggregate interface, the system automatically creates a Layer 2 static
aggregation group numbered the same.

2. Set the operational state of every interface in the LAG to up by entering:

switch(config-lag-if)# no shutdown

NOTE: This command does not impact the administrative state of the member interfaces
because the command was entered at the level of the LAG. To change the administrative
state of a member interface, enter the command at the interface level. For example:

switch(config)# interface 1/1/2
switch(config-if)# no shutdown

3. On the 8320, 8325, 8360, and 8400, disable routing by entering:

switch(config-lag-if)# no routing

See the Command-Line Interface Guide for your switch and software version for more information about
the no routing command.

NOTE: On the 6100 and 6200 Switch Series, routing is not supported on physical interfaces.

On the 6300 and 6400 Switch Series, routing is disabled by default.

4. Assign a native VLAN ID to a trunk interface on the LAG by entering:

switch(config-lag-if)# vlan trunk native <VLAN-ID>

For example:

switch(config-lag-if)# vlan trunk native 1

5. Use the following steps to add a maximum of 16 interfaces to the LAG:

a. To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

Chapter 2 Link Aggregation

15

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the interface <PORT-ID> command.

b. Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

switch(config-if-<1/1/1-1/1/4>)# lag 100

c. Set the administrative state of the member interface to up:

switch(config-if-<1/1/1-1/1/4>)# no shutdown

6. View the configuration by entering the following:

For 6100, 6200, 6300, and 6400 switch series:

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

For 8320, 8325, 8360, and 8400 switch series:

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

16

AOS-CX 10.06 Link Aggregation Guide

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

Configuring a Layer 2 dynamic aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Create a Layer 2 aggregate interface and access the Layer 2 aggregate interface view by entering:

switch(config)# interface lag <ID>

The range of the LAG interface ID is 1 to 256.

While creating the Layer 2 aggregate interface, the system automatically creates a Layer 2 dynamic
aggregation group numbered the same.

2. Set the operational state of every interface in the LAG to up by entering:

switch(config-lag-if)# no shutdown

NOTE: This command does not impact the administrative state of the member interfaces
because the command was entered at the level of the LAG. To change the administrative
state of a member interface, enter the command at the interface level. For example:

switch(config)# interface 1/1/2
switch(config-if)# no shutdown

3. On the 8320, 8325, 8360, and 8400, disable routing by entering:

switch(config-lag-if)# no routing

See the Command-Line Interface Guide for your switch and software version for more information about
the no routing command.

NOTE: On the 6100 and 6200 Switch Series, routing is not supported on physical interfaces.

On the 6300 and 6400 Switch Series, routing is disabled by default.

4. Configure the aggregation group to operate in dynamic mode by entering:

Chapter 2 Link Aggregation

17

switch(config-lag-if)# lacp mode {active | passive}

For example:

switch(config-lag-if)# lacp mode active

5. Configure the aggregation group to operate in fast or slow mode by entering:

switch(config-lag-if)# lacp rate {fast | slow}

For example:

switch(config-lag-if)# lacp rate fast

6. Assign a native VLAN ID to a trunk interface by entering:

switch(config-lag-if)# vlan trunk native <VLAN-ID>

For example:

switch(config-lag-if)# vlan trunk native 1

7. Use the following steps to add a maximum of 16 interfaces to the LAG:

a. To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the interface <PORT-ID> command.

b. Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

switch(config-if-<1/1/1-1/1/4>)# lag 20

c. Set the administrative state of the member interface to up:

switch(config-if-<1/1/1-1/1/4>)# no shutdown

8. View the configuration by entering:

For 6100, 6200, 6300, and 6400 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:
!
vlan 1
interface lag 20
    no shutdown
    vlan trunk native 1

18

AOS-CX 10.06 Link Aggregation Guide

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

For 8320, 8325, 8360, and 8400 switch series:

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
Layer 3 aggregation groups are supported on all switch series except 6100 and 6200 Switch Series.

Configuring a Layer 3 static aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Create a Layer 3 aggregate interface and access the Layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

The range of the LAG interface ID is 1 to 256.

Chapter 2 Link Aggregation

19

While creating the Layer 3 aggregate interface, the system automatically creates a Layer 3 static
aggregation group numbered the same.

2. Set the operational state of every interface in the LAG to up by entering:

•

For 6300 and 6400 switch series:

switch(config-lag-if)# no shutdown
switch(config-lag-if)# routing

NOTE: This command does not impact the administrative state of the member interfaces
because the command was entered at the level of the LAG. To change the administrative
state of a member interface, enter the command at the interface level. For example:

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# routing

•

For 8320, 8325, 8360, and 8400 switch series:

switch(config-lag-if)# no shutdown

NOTE: This command does not impact the administrative state of the member interfaces
because the command was entered at the level of the LAG. To change the administrative
state of a member interface, enter the command at the interface level. For example:

switch(config)# interface 1/1/2
switch(config-if)# no shutdown

3. Set the IP address on the LAG interface by entering:

switch(config-lag-if)# ip address <IPV4-ADDR>/<MASK>

For example:

switch(config-lag-if)# ip address 192.0.2.1/30

4. Use the following steps to add a maximum of 16 interfaces to the LAG:

a. To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the interface <PORT-ID> command.

b. Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

20

AOS-CX 10.06 Link Aggregation Guide

switch(config-if-<1/1/1-1/1/4>)# lag 100

c. Set the administrative state of the member interface to up:

switch(config-if-<1/1/1-1/1/4>)# no shutdown

5. View the configuration by entering the following:

For 6300 and 6400 switch series:

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

For 8320, 8325, 8360, and 8400 switch series:

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
    no shutdown
    lag 100
interface 1/1/3
    no shutdown
    lag 100
interface 1/1/4
    no shutdown
    lag 100

switch(config-if-<1/1/1-1/1/4>)# show lacp aggregates

Chapter 2 Link Aggregation

21

Aggregate name   : lag100
Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2
Heartbeat rate   : N/A
Hash             : l3-src-dst
Aggregate mode   : Off

Configuring a Layer 3 dynamic aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Create a Layer 3 aggregate interface and access the Layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

The range of the LAG interface ID is 1 to 256.

While creating the Layer 3 aggregate interface, the system automatically creates a Layer 3 dynamic
aggregation group numbered the same.

2. Set the operational state of every interface in the LAG to up by entering:

•

For 6300 and 6400 switch series:

switch(config-lag-if)# no shutdown
switch(config-lag-if)# routing

NOTE: This command does not impact the administrative state of the member interfaces
because the command was entered at the level of the LAG. To change the administrative
state of a member interface, enter the command at the interface level. For example:

switch(config)# interface 1/1/2
switch(config-if)# no shutdown
switch(config-if)# routing

•

For 8320, 8325, 8360, and 8400 switch series:

switch(config-lag-if)# no shutdown

NOTE: This command does not impact the administrative state of the member interfaces
because the command was entered at the level of the LAG. To change the administrative
state of a member interface, enter the command at the interface level. For example:

switch(config)# interface 1/1/2
switch(config-if)# no shutdown

3. Configure the aggregation group to operate in dynamic mode by entering:

switch(config-lag-if)# lacp mode {active | passive}

For example:

switch(config-lag-if)# lacp mode active

4. Configure the aggregation group to operate in fast or slow mode by entering:

22

AOS-CX 10.06 Link Aggregation Guide

switch(config-lag-if)# lacp rate {fast | slow}

For example:

switch(config-lag-if)# lacp rate fast

5. Set the IP address on the LAG interface by entering:

switch(config-lag-if)# ip address <IPV4-ADDR>/<MASK>

For example:

switch(config-lag-if)# ip address 192.0.3.1/30

6. Use the following steps to add a maximum of 16 interfaces to the LAG:

a. To assign an interface to the LAG:

switch(config-lag-if)# interface <PORT-ID>

To assign a range of interfaces to a LAG:

switch(config-lag-if)# interface <PORT-ID>-<PORT-ID>

For example:

switch(config-lag-if)# interface 1/1/1-1/1/4

See the Command-Line Interface Guide for your switch and software version for more information
about the interface <PORT-ID> command.

b. Assign an ID to the LAG:

switch(config-if)# lag <ID>

For example:

switch(-<1/1/1-1/1/4>)# lag 100

c. Set the administrative state of the member interface to up:

switch(-<1/1/1-1/1/4>)# no shutdown

7. View the configuration by entering:

For 6300 and 6400 switch series:

switch(config-if-<1/1/1-1/1/4>)# show running-config

Current configuration:
!
vlan 1
interface lag 100
    no shutdown
    routing
    ip address 192.0.3.1/30
    lacp mode active
    lacp rate fast
interface 1/1/1
    no shutdown
    lag 100
interface 1/1/2
    no shutdown

Chapter 2 Link Aggregation

23

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

For 8320, 8325, 8360, and 8400 switch series:

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
Interfaces       : 1/1/3 1/1/1 1/1/4 1/1/2
Heartbeat rate   : Fast
Hash             : l3-src-dst
Aggregate mode   : Active

Removing a LAG

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Delete the LAG. Enter:

switch(config)# no interface lag <ID>

24

AOS-CX 10.06 Link Aggregation Guide

For example:

switch(config)# no interface lag 100

All interfaces assigned to the LAG are automatically removed from the LAG as part of the deletion process
of the LAG. After removing a physical interface from a LAG,

• 6100, 6200, 6300, and 6400 switches: The interface associated with the LAG becomes layer 2 ports

with the default layer 2 configurations and admin status enabled.

• 8320, 8235, 8360, and 8400 switches: The interface associated with the LAG becomes layer 3 ports

with default layer 3 configurations and administrative down.

Removing an interface from a LAG

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Remove an interface from the LAG. Enter:

switch(config)# interface <PORT-NUM>
switch(config-if)# no lag <ID>

For example:

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

• 6100, 6200, 6300, and 6400 switches: The interface associated with LAG becomes layer 2 ports with

default layer 2 configurations and with admin status of enabled.

• 8320, 8325, 8360, and 8400 switches: The interface associated with the LAG becomes L3 ports with
default L3 configurations and administrative down. For example, suppose interface 1/1/1 was part of
LAG 3 and you had administratively enabled the interface. If you later remove interface 1/1/1 from

Chapter 2 Link Aggregation

25

LAG 3, the administrative status automatically changes to down. If you want to use the interface again,
you must administratively enable it again.

Changing the LAG membership for an interface

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Remove an interface from the LAG. Enter:

switch(config)# interface <PORT-NUM>
switch(config-if)# no lag <ID>

For example:

For 6100, 6200, 6300, and 6400 switch series:

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
interface 1/1/2
    no shutdown
    lag 100
switch(config-if)#

For 8320, 8325, 8360, and 8400 switch series:

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
    lag 100
switch(config-if)#

26

AOS-CX 10.06 Link Aggregation Guide

After removing a physical interface from a LAG, the interface associated with the LAG becomes L3 ports
with default L3 configurations and administrative down. For example, suppose interface 1/1/1 was part of
LAG 3 and you had administratively enabled the interface. If you later remove interface 1/1/1 from LAG 3,
the administrative status automatically changes to down. If you want to use the interface again, you must
administratively enable it again.

On 6100 and 6200 Switch Series, after removing a physical interface from a LAG, the interface associated
with the LAG becomes layer 2 ports with default layer 2 configurations and admin status enabled.

2. Create the LAG to which you want to add the interface:

switch(config-if)# interface lag 10

For example:

For 6100, 6200, 6300, and 6400 switch series:

switch(config-if)# interface lag 10
switch(config-lag-if)# no shutdown
switch(config-lag-if)# vlan trunk native 1

For 8320, 8325, 8360, and 8400 switch series:

switch(config-if)# interface lag 10
switch(config-lag-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-lag-if)# vlan trunk native 1

3. Add the interface from Step 1 to the newly created LAG:

switch(config)# interface 1/1/1
switch(config-if)# lag 10

For example:

For 6100, 6200, 6300, and 6400 switch series:

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
interface 1/1/2
    no shutdown
    lag 100

For 8320, 8325, 8360, and 8400 switch series:

switch(config)# interface 1/1/1
switch(config-if)# lag 10
switch(config-if)# show running-config

Chapter 2 Link Aggregation

27

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

Notice that interface 1/1/1 in the previous example is still not active, even though it has been added to
LAG 10. To change the administrative state of the member interface, enter the no shutdown command
at the interface level.

For example:

For 6100, 6200, 6300, and 6400 switch series:

switch(config-if)# interface 1/1/1
switch(config-if)# no shutdown
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
    no shutdown
    lag 10
interface 1/1/2
    no shutdown
    lag 100

For 8320, 8325, 8360, and 8400 switch series:

switch(config-if)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# show running-config
Current configuration:
!
...
!
vlan 1
interface lag 10
    no shutdown

28

AOS-CX 10.06 Link Aggregation Guide

no routing
    vlan trunk native 1
    vlan trunk allowed all
interface lag 100
    no shutdown
    no routing
    vlan trunk native 1
    vlan trunk allowed all
interface 1/1/1
    no shutdown
    lag 10
interface 1/1/2
    no shutdown
    lag 100

Configuration of an aggregate interface

Configuring the description of an aggregate interface

You can configure the description of an aggregate interface for administration purposes, for example,
describing the purpose of the interface.

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Create a Layer 3 aggregate interface and enter Layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

2. Configure the description of the aggregate interface:

switch(config-if)# description <text>

Setting the MTU for a Layer 2 member link interface

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Enter a Layer 2 member link interface view by entering:

switch(config)# interface <INTERFACE-ID>

2. Set the MTU for the Layer 2 member link interface:

switch(config-if)# mtu <VALUE>

See the Command-Line Interface Guide for your switch and software version for more information about
the mtu <VALUE> command. When allowing jumbo frames under a layer 2 aggregation interface, make
sure that the MTU value is set appropriately under all member interfaces.

Chapter 2 Link Aggregation

29

Setting the MTU for a Layer 3 aggregate interface

NOTE: Layer 3 aggregation groups are not supported on the 6100 and 6200 Switch Series.

The MTU of an interface affects IP packets fragmentation and reassembly on the interface.

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Enter Layer 3 aggregate interface view by entering:

switch(config)# interface lag <INTERFACE-ID>

2. Set the MTU for the Layer 3 aggregate interface:

switch(config-lag-if)# ip mtu <VALUE>

See the Command-Line Interface Guide for your switch and software version for more information about
the ip mtu <VALUE> command. When allowing jumbo frames under a layer 2 aggregation interface,
make sure that the MTU value is set appropriately under all member interfaces.

NOTE: If the IP MTU is configured as 9198, the MTU on the physical interfaces must also be
configured as 9198.

Impact of shutting down or bringing up an aggregate interface

By default, an aggregate interface is down. Shutting down or bringing up an aggregate interface affects the
aggregation states and link states of member ports in the corresponding aggregation group as follows:

• When an aggregate interface is shut down, all Selected ports in the corresponding aggregation group

become Unselected ports and all member ports go to an operationally down state.

• When an aggregate interface is brought up, the aggregation states of member ports in the corresponding

aggregation group are recalculated. LAG members, which are administratively up, will become
operationally up. The members that are not administratively up will be in the same state and not made
eligible for aggregation.

Shutting down an aggregate interface

Prerequisites

You must be in the global configuration context: switch(config)#

Procedure

1. Enter Layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

2. Shut down the aggregate interface:

30

AOS-CX 10.06 Link Aggregation Guide

switch(config-lag-if)# shutdown

Supported hashing algorithms

• Source MAC and destination MAC

• Source IP and destination IP

• Source port and destination port.

LACP configuration settings

Task

Command

Example

Setting the LACP mode to
active or passive.

lacp mode
{active |
passive}

Setting the LACP mode to
off.

no lacp mode
{active |
passive}

switch(config-lag-if)# lacp mode active

switch(config-lag-if)# no lacp mode active

For 6100 and 8400 Switch Series:

switch(config)# lacp hash l2-src-dst

For 8320, 8325, 6200, 6300, and 6400 Switch Series:

switch(config-lag-if)# hash l2-src-dst

Setting the hash type.

For 6100 and 8400
Switch Series:

lacp hash [l2-
src-dst | l3-
src-dst | l4-
src-dst]

For 8320, 8325,
6200, 6300, and
6400 Switch Series:

hash [l2-src-
dst | l3-src-
dst]

Setting the LACP rate to
fast.

Setting the LACP rate to
slow.

lacp rate fast

switch(config)# interface lag 1

switch(config-lag-if)# lacp rate fast

lacp rate slow

switch(config)# interface lag 1

switch(config-lag-if)# lacp rate slow

Table Continued

Chapter 2 Link Aggregation

31

| Task | Command | Example |
| ---- | ------- | ------- |
Applying shutdown on the shutdown switch(config)# interface lag 1
LAG port.
switch(config-lag-if)# shutdown
Resetting every interface no shutdown switch(config-lag-if)# no shutdown
in the LAG to the default
(up)
Interface LACP settings
| Task | Command | Example |
| ---- | ------- | ------- |
Setting the LACP port ID. lacp port-id switch(config-if)# lacp port-id 100
<ID>
Setting the LACP port ID to no lacp port-id switch(config-if)# no lacp port-id
the default.
Setting the LACP port lacp port- switch(config-if)# lacp port-priority 100
| priority. | priority <PORT- |     |
| --------- | --------------- | --- |
PRIORITY>
Setting the LACP port no lacp port- switch(config-if)# no lacp port-priority
| priority to the default | priority |     |
| ----------------------- | -------- | --- |
32 AOS-CX 10.06 Link Aggregation Guide

Configuration verification

Task

Command

Example

Viewing LACP global
information

show lacp
configuration

Viewing LACP aggregate
information

show lacp
aggregates

Viewing LACP aggregate
information for a LAG

show lacp
aggregates
lag100

switch# show lacp configuration
System-id       : 70:72:cf:ef:fc:d9
System-priority : 65534
Hash            : l3-src-dst

The output displayed for the show lacp
configuration is from the 8400 series switch.

switch# show lacp aggregates
Aggregate-name          : lag100
Aggregated-interfaces   : 1/1/2
Heartbeat rate          : N/A
Hash                    : l3-src-dst
Aggregate mode          : off

Aggregate-name          : lag110
Aggregated-interfaces   : 1/1/1, 1/1/3
Heartbeat rate          : slow
Hash                    : l3-src-dst
Aggregate mode          : active

switch# show lacp aggregates lag100
Aggregate-name          : lag100
Aggregated-interfaces   :
Heartbeat rate          : N/A
Hash                    : l3-src-dst
Aggregate mode          : off

Viewing LACP interface
details

show lacp
interfaces

switch# show lacp interfaces

The output is too wide to display in a column. The
command output is provided in the CLI topic for the
command.

BFD reports a LAG as down even when healthy links are
still available
Symptom

NOTE: BFD is not supported on the 6100 and 6200 Switch Series.

The Bidirectional Forward Detection (BFD) feature reports a Link Aggregation (LAG), as being down, even
though there are healthy LAG links available. The LAG, containing the downed link, will eventually rebalance
the traffic to its other links.

Cause

This notification occurs when the minimum BFD control packet reception interval is set at a faster rate than
the Link Aggregation Control Protocol (LACP) rate and LAG rebalancing occurs. BFD assumes that the link is
down without realizing that the LAG is rebalancing the traffic load.

Chapter 2 Link Aggregation

33

Action

1. Set the minimum BFD control packet reception interval to a slower rate than the LACP rate or set the

LACP rate to a faster rate than the minimum BFD control packet reception interval.

a. To find the current settings of the minimum BFD control packet reception interval, enter the show

running-config command.

The minimum BFD control packet reception interval setting is listed as bfd min-receive-interval
in the command output and the measurement is in ms.

b. To find the current rate of LACP, enter the show lacp aggregates command.

The LACP rate is listed as the Heatbeat rate in the command output.

c. To change the minimum BFD control packet reception interval, enter the bfd min-receive-

interval command.

d. To change the LACP rate, enter the lacp rate {fast | slow} command.

LACP and LAG commands

description

Syntax

description <TEXT>

no description <TEXT>

Description

Provides a brief description of the LAG interface. The description text is saved in the configuration of the
LAG. It is available even after a reboot.

The no form of this command removes the description of the LAG interface from the configuration.

Command context

config-lag-if

Parameters
<TEXT>

Specifies the description of the LAG interface.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# interface lag 10
switch(config-lag-if)# description This LAG is used for an example.
switch(config-lag-if)# show running-config
...
vlan 1
interface lag 10
     description This LAG is used for an example.

34

AOS-CX 10.06 Link Aggregation Guide

interface lag 60
switch(config-lag-if)#

hash

Syntax

hash [l2-src-dst | l3-src-dst | l4-src-dst]

Description

This command controls the selection of an interface in a group of aggregate interfaces. The hash type value
helps transmit a frame. This configuration must be done at the LAG interface level.

Command context

config-lag-if

Parameters
l2-src-dst

Specifies the load-balancing calculation to include only Layer 2 items, such as source and destination
MAC addresses.

l3-src-dst

Specifies the load-balancing calculation to include only Layer 3 items, such as source and destination IP
addresses. Default setting.

l4-src-dst

Specifies the load-balancing calculation to include only Layer 4 items, such as source and destination
UDP/TCP ports.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config-lag-if)# hash l2-src-dst

interface lag

Syntax

interface lag <ID>

no interface lag <ID>

Description

Creates a Link Aggregation Group (LAG) interface represented by an ID.

The no form of this command deletes a LAG interface represented by an ID.

Command context

config

Parameters
<ID>

Specifies a LAG interface ID.

Chapter 2 Link Aggregation

35

Authority

Administrators or local user group members with execution rights for this command.

Usage

Keep in mind the following requirements when adding interfaces to a LAG:

• To determine the maximum number of LAG interfaces for your type of switch, look at the output from
the show capacities lag command; however, the number of LAGs that can be created depends on
the availability of the physical interface since each LAG interface needs at least one physical interface as a
member link.

• After the maximum limit of members is reached in a LAG, an additional port cannot be added to the
aggregation group. If a port belongs to a card type with a different speed than the other aggregation
members, the port can still be added to the aggregation group. If dynamic LAG is enabled, any port
member with a speed different than other aggregation members is blocked or ineligible from the same
aggregation group. Any operational keys/attributes or configuration changes might affect the aggregation
states of the member ports.

• The nondefaults configuration on an interface is removed automatically when the interface is added to a
link aggregation. For example: Assume that you remove a member interface from an existing LAG and
add it to another LAG. The software removes the nondefault configurations on the interface when it is
added to the new LAG.

Examples

Creating a Link Aggregation Group (LAG) interface represented by an ID of 100:

switch(config)# interface lag 100

Deleting a Link Aggregation Group (LAG) interface represented by an ID of 100:

switch(config)# no interface lag 100

ip address
Not supported on the 6100 and 6200 Switch Series.

Syntax

ip address <IPV4-ADDR>/<MASK> [secondary]

no ip address <IPV4-ADDR>/<MASK> [secondary]

Description

Sets an IPv4 address and subnet mask to a LAG interface. One primary and up to 31 secondary address can
be configured per interface.

The no form of this command removes the IPv4 address from the interface.

Command context

config-lag-if

36

AOS-CX 10.06 Link Aggregation Guide

Parameters
<IPV4-ADDR>

Specifies an IP address in IPv4 format (x.x.x.x), where x is a decimal number from 0 to 255. You can
remove leading zeros. For example, the address 192.169.005.100 becomes 192.168.5.100.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 32.

secondary

Specifies a secondary IP address.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting an IP address on the LAG interface 1 to 198.51.100.1 with a mask of 24 bits:

switch(config)# interface lag 1
switch(config-lag-if)# ip address 198.51.100.1/24

Removing the IP address 198.51.100.1 with a mask of 24 bits from LAG interface 1:

switch(config)# interface lag 1
switch(config-lag-if)# no ip address 198.51.100.1/24

ipv6 address
Not supported on the 6100 and 6200 Switch Series.

Syntax

ipv6 address <IPV6-ADDR>/<MASK>

no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets an IPv6 address and subnet mask to a LAG interface.

The no form of this command removes the IPv6 address from the interface.

Command context

config-lag-if

Parameters
<IPV6-ADDR>

Specifies the IP address in IPv6 format (xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. You can use two colons (::) to represent consecutive zeros (but only
once), remove leading zeros, and collapse a quartet of four zeros to a single 0. For example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes 2222:0:3333::4444:55.

<MASK>

Specifies the number of bits in the address mask in CIDR format (x), where x is a decimal number from 0
to 128.

Chapter 2 Link Aggregation

37

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the IPv6 address on LAG interface 1 to 2001:0db8:85a3::8a2e:0370:7334 with a mask of 24 bits:

switch(config)# interface lag 1
switch(config-lag-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Removing the IP address 2001:0db8:85a3::8a2e:0370:7334 with mask of 24 bits with a mask of 24 bits from
LAG interface 1:

switch(config)# interface lag 1
switch(config-lag-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

lacp hash
Supported only on the 6100 and 8400 Switch Series.

Syntax

lacp hash [l2-src-dst | l3-src-dst | l4-src-dst]

Description

This command controls the selection of an interface in a group of aggregate interfaces. The hash type value
helps transmit a frame. This configuration must be done at the global level.

Command context

config

Parameters
l2-src-dst

Specifies the load-balancing calculation to include only Layer 2 items, such as source and destination
MAC addresses.

l3-src-dst

Specifies the load-balancing calculation to include only Layer 3 items, such as source and destination IP
addresses.
l4-src-dst

Specifies the load-balancing calculation to include only Layer 4 items, such as source and destination
UDP/TCP ports.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config)# lacp hash l2-src-dst

lacp mode

Syntax

lacp mode {active | passive}

no lacp mode {active | passive}

38

AOS-CX 10.06 Link Aggregation Guide

Description

Sets an LACP mode to active or passive.

The no form of this command sets the LACP mode to off, returning the LAG to a static mode aggregation.

Command context

config-lag-if

Parameters
active

Specifies that the local switch will transmit LACP Data Units (LACPDUs) to attempt to negotiate with the
remote device.

passive

Specifies that the local switch will listen for LACPDUs from the remote device for LACP negotiation.

NOTE: A momentary traffic drop occurs because LACP partners reconverge when changing the
mode from active to passive or passive to active.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the LACP mode to active:

switch(config)# interface lag 1
switch(config-lag-if)# lacp mode active

Setting the LACP mode to off:

switch(config)# interface lag 1
switch(config-lag-if)# no lacp mode active

lacp port-id

Syntax

lacp port-id <PORT-ID>

no lacp port-id

Description

Sets the LACP port ID value of the member interface of the LAG.

The no form of this command removes the LACP port ID value from the interface.

Command context

config-if

Parameters
<PORT-ID>

Specifies a port ID value. Range: 1 to 65535.

Chapter 2 Link Aggregation

39

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting an LACP port ID to a value of 10:

switch(config-if)# lacp port-id 10

Removing the LACP port ID value:

switch(config-if)# no lacp port-id

lacp port-priority

Syntax

lacp port-priority <PORT-PRIORITY>

no lacp port-priority

Description

Sets an LACP port priority value for the member interface of the LAG.

The no form of this command reverts the LACP port priority to the default, which is 1.

Command context

config-if

Parameters
<PORT-PRIORITY>

Specifies a port priority value. Range: 1 to 65535.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting a LACP port priority value of 10:

switch(config-if)# lacp port-priority 10

Reverting the LACP port ID to the default:

switch(config-if)# no lacp port-priority

lacp rate

Syntax

lacp rate {fast | slow}

no lacp rate

Description

Sets an LACP heartbeat request time to fast or slow.

40

AOS-CX 10.06 Link Aggregation Guide

The no form of the command sets an LACP rate to slow.

Command context

config-lag-if

Parameters
fast

Specifies the heartbeat request to every second, and the timeout period is a three-consecutive heartbeat
loss that is 3 seconds.

slow

Specifies the heartbeat request to every 30 seconds. The timeout period is three-consecutive heartbeat
loss that is 90 seconds. Default setting.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting the LACP heartbeat request time to fast:

switch(config)# interface lag 1
switch(config-lag-if)# lacp rate fast

Resetting the LACP heartbeat request time to the default, which is slow:

switch(config)# interface lag 1
switch(config-lag-if)# no lacp rate

Another way to set the LACP heartbeat request time to the default, which is slow:

switch(config)# interface lag 1
switch(config-lag-if)# lacp rate slow

lacp system-priority

Syntax

lacp system-priority <SYSTEM-PRIORITY-VALUE>

no lacp system-priority

Description

Sets a Link Aggregation Control Protocol (LACP) system priority.

The no form of this command sets an LACP system priority to the default, which is 65534.

Command context

config

Parameters
<SYSTEM-PRIORITY-VALUE>

Specifies a system priority value. Range: 0 to 65535.

Chapter 2 Link Aggregation

41

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting a Link Aggregation Control Protocol (LACP) system priority to 100:

switch(config)# lacp system-priority 100

Setting an LACP system priority to the default (65534):

switch(config)# no lacp system-priority

A momentary traffic drop can be seen in case the LACP state machine must renegotiate.

lag

Syntax

lag <ID>

no lag <ID>

Description

Adds an interface to a specified LAG interface ID.

The no form of this command removes an interface from a specified LAG interface ID. The member loses its
LACP configuration when removed from the LAG. The member also reaches the default state with an
administrative shutdown. For 6300 and 6400 series switches, the administrative state is enabled.
Configurations, such as MTU and UDLD, are retained.

Command context

config-if

Parameters
<ID>

Specifies a LAG interface ID. Range: 1 to 256.

Authority

Administrators or local user group members with execution rights for this command.

Usage

• All members of the LAG must have the same speed. If a member comes up late with a different speed, it
will not participate in the LAG/LACP. The hardware restriction is applied before adding an interface to
LAG. The member belongs to the card type that has the same maximum speed as the reference port card
type.

• To move an interface from LagA to LagB, first remove the interface from LagA and then add it to LagB.
When a member is attached to a LAG, the nondefault configurations on the member are removed
silently.

• After removing a physical interface from a LAG, the interface associated with the LAG becomes L3 ports

with default L3 configurations and administrative down. For example, suppose interface 1/1/1 was part of
LAG 3 and you had administratively enabled the interface. If you later remove interface 1/1/1 from LAG 3,
the administrative status automatically changes to down. If you want to use the interface again, you must
administratively enable it again.

42

AOS-CX 10.06 Link Aggregation Guide

Examples

Adding an interface to a Link Aggregation Group (LAG) represented by an ID of 100:

switch(config)# interface 1/1/1
switch(config-if)# lag 100

Deleting an interface from a Link Aggregation Group (LAG) represented by an ID of 100:

switch(config)# interface 1/1/1
switch(config-if)# no lag 100

show interface

Syntax

show interfaces <LAG-NAME> [vsx-peer]

Description

Displays information about a specific LAG.

Command context

Operator (>) or Manager (#)

Parameters
<LAG-NAME>

Specifies a LAG name.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

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
 Rx
           20 input packets           2584 bytes
            0 input error                0 dropped
            0 CRC/FCS

Chapter 2 Link Aggregation

43

Tx
           45 output packets          5658 bytes
            0 input error                4 dropped
            0 collision

show lacp aggregates

Syntax

show lacp aggregates [<LAG-NAME>] [vsx-peer]

Description

Displays all LACP aggregate information configured for all LAGs, or for a specific LAG.

Command context

Operator (>) or Manager (#)

Parameters
<LAG-NAME>

Optional: Specifies a lag name.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

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

44

AOS-CX 10.06 Link Aggregation Guide

Hash                  : l2-src-dst
Aggregate mode        : passive

show lacp configuration

Syntax

show lacp configuration [vsx-peer]

Description

Displays global LACP configuration.

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

Displaying global LACP configuration (output is applicable for 8400 series switches):

switch# show lacp configuration
System-id       : 70:72:cf:ef:fc:d9
System-priority : 65534
Hash            :l3-src-dst

Displaying global LACP configuration (output is applicable for 8320, 6300, and 6400 series switches):

switch# show lacp configuration
System-id       : 98:f2:b3:68:40:a0
System-priority : 65534

show lacp interfaces

Syntax

show lacp interfaces [<IFNAME>] [vsx-peer]

Description

Displays an LACP configuration of the physical interfaces, including VSXs. If an interface name is passed as
argument, it only displays an LACP configuration of a specified interface.

Command context

Operator (>) or Manager (#)

Chapter 2 Link Aggregation

45

Parameters
<IFNAME>

Optional: Specifies an interface name.

[vsx-peer]

Shows the output from the VSX peer switch. If the switches do not have the VSX configuration or the ISL
is down, the output from the VSX peer switch is not displayed. This parameter is available on switches
that support VSX.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

Examples

This example displays an LACP configuration of the physical interfaces. One of the interfaces has the lacp-
block forwarding state. If a VSX switch has loop protect enabled on an interface and a loop occurs, VSX
blocks the interface to stop the loop. The forwarding state of the blocked interface is set to lacp-block.

switch# show lacp interfaces
State abbreviations :
A - Active        P - Passive      F - Aggregable I - Individual
S - Short-timeout L - Long-timeout N - InSync     O - OutofSync
C - Collecting    D - Distributing
X - State m/c expired              E - Default neighbor state

Actor details of all interfaces:
------------------------------------------------------------------------------------
Intf   Aggr    Port    Port   State   System-id          System  Aggr Forwarding
       name    id      Pri                               Pri     Key  State
------------------------------------------------------------------------------------
1/1/1  lag10   17      1      ALFOE   70:72:cf:37:a3:5c  20      10   lacp-block
1/1/2  lag128  69      1      ALFNCD  70:72:cf:37:a3:5c  20      128  up
1/1/3  lag128  14      1      ALFNCD  70:72:cf:37:a3:5c  20      128  up
1/1/4  lag128                                                         down
1/1/5  lag20                                                          up

Partner details of all interfaces:
------------------------------------------------------------------------------
Intf   Aggr    Partner Port     State     System-id       System   Aggr
       name    Port-id Pri                                Priority Key
------------------------------------------------------------------------------
1/1/1  lag10   0       65534    PLFOEX  00:00:00:00:00:00 65534    0
1/1/2  lag128  69      1        PLFNCD  70:72:cf:8c:60:a7 65534    128
1/1/3  lag128  14      1        PLFNCD  70:72:cf:8c:60:a7 65534    128
1/1/4  lag128
1/1/5  lag20

Displaying static LAG:

switch# show lacp interfaces
State abbreviations :
A - Active        P - Passive      F - Aggregable I - Individual
S - Short-timeout L - Long-timeout N - InSync     O - OutofSync
C - Collecting    D - Distributing
X - State m/c expired              E - Default neighbor state

Actor details of all interfaces:
------------------------------------------------------------------------------
Intf   Aggr   Port    Port   State   System-id         System  Aggr Forwarding
       Name   Id      Pri                              Pri     Key  State

46

AOS-CX 10.06 Link Aggregation Guide

------------------------------------------------------------------------------
1/1/1  lag10                                                        up
1/1/2  lag10                                                        up

Partner details of all interfaces:
------------------------------------------------------------------------------
Intf   Aggr   Port    Port   State   System-id         System  Aggr
       Name   Id      Pri                              Pri     Key
------------------------------------------------------------------------------
1/1/1  lag10
1/1/2  lag10

Displaying an LACP configuration of the 1/1/1 interface:

switch# show lacp interfaces 1/1/1

State abbreviations :
A - Active        P - Passive      F - Aggregable I - Individual
S - Short-timeout L - Long-timeout N - InSync     O - OutofSync
C - Collecting    D - Distributing
X - State m/c expired              E - Default neighbor state

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
S - Short-timeout L - Long-timeout N - InSync     O - OutofSync
C - Collecting    D - Distributing
X - State m/c expired              E - Default neighbor state

Actor details of all interfaces:
------------------------------------------------------------------------------
Intf    Aggr       Port  Port  State   System-ID         System Aggr Forwarding
        Name       Id    Pri                             Pri    Key  State
------------------------------------------------------------------------------
1/4/14  lag1(mc)   206   1     ALFNCD  f8:60:f0:06:49:00 65534  1    up
1/5/15  lag2(mc)                                                     down

Partner details of all interfaces:
------------------------------------------------------------------------------
Intf    Aggr       Port  Port  State   System-ID         System Aggr
        Name       Id    Pri                             Pri    Key
------------------------------------------------------------------------------
1/4/14  lag1(mc)   130   1     ALFNCD  f8:60:f0:06:87:00 65534  1
1/5/15  lag2(mc)

Displaying an LACP configuration after loop-protect is enabled on the secondary VSX switch:

Chapter 2 Link Aggregation

47

switch# show lacp interfaces

State abbreviations :
A - Active        P - Passive      F - Aggregable I - Individual
S - Short-timeout L - Long-timeout N - InSync     O - OutofSync
C - Collecting    D - Distributing
X - State m/c expired              E - Default neighbor state

Actor details of all interfaces:
------------------------------------------------------------------------------
Intf    Aggr       Port  Port  State   System-ID         System Aggr Forwarding
        Name       Id    Pri                             Pri    Key  State
------------------------------------------------------------------------------
1/3/2   lag1(mc)   1130  1     ALFNCD  f8:60:f0:06:49:00 65534  1    up
1/9/3   lag2(mc)                                                     down

Partner details of all interfaces:
------------------------------------------------------------------------------
Intf    Aggr       Port  Port  State   System-ID         System Aggr
        Name       Id    Pri                             Pri    Key
------------------------------------------------------------------------------
1/3/2   lag1(mc)   131   1     ALFNCD  f8:60:f0:06:87:00 65534  1
1/9/3   lag2(mc)

shutdown

Syntax

shutdown

no shutdown

Description

Sets every interface in the LAG operationally down.

The no form of this command sets every interface operationally up.

Command context

config-lag-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

Setting every interface in the LAG to shutdown:

switch(config)# interface lag 1
switch(config-lag-if)# shutdown

Resetting every interface in the LAG to the default (up):

switch(config)# interface lag 1
switch(config-lag-if)# no shutdown

48

AOS-CX 10.06 Link Aggregation Guide

vlan trunk native

Syntax

vlan trunk native <VLAN-ID>

no vlan trunk native [<VLAN-ID>]

Description

Assigns a native VLAN ID to a LAG interface.

The no form of this command removes a native VLAN from a LAG interface and assigns VLAN ID 1 as its
native VLAN.

Command context

config-lag-if

Command context

config-if

Parameters
<VLAN-ID>

Specifies the number of the VLAN ID to assign. The VLAN ID must exist.

Maximum number of VLANs supported: 512 (6100); 2048 (6200); 4096 (6300, 6400, 8320, 8325, 8360,
8400).

VLAN ID range: 2 to 4094.

Authority

Administrators or local user group members with execution rights for this command.

Usage

By default, VLAN ID 1 is assigned as the LAG VLAN ID for all LAG interfaces. VLANs can only be assigned to a
nonrouted (layer 2) interface or LAG interface.

Only one VLAN ID can be assigned as the native VLAN. For the interface to forward the native VLAN traffic,
the interface has to be allowed explicitly by entering vlan trunk allowed <ID> where the ID is the native
VLAN ID. This setting is also applicable to the physical interface.

Examples

Configuring a Layer 2 dynamic aggregation group with native VLAN ID 1 assigned to LAG 1:

For 6100 and 6200 switch series:

switch(config)# interface lag 1
switch(config-lag-if)# no shutdown
switch(config-lag-if)# lacp mode active
switch(config-lag-if)# vlan trunk native 1
switch(config-lag-if)# vlan trunk allowed 1

For 6300, 6400, 8320, 8325, 8360, and 8400 switch series:

switch(config)# interface lag 1
switch(config-lag-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-lag-if)# lacp mode active

Chapter 2 Link Aggregation

49

switch(config-lag-if)# vlan trunk native 1
switch(config-lag-if)# vlan trunk allowed 1

Configuring a Layer 2 dynamic aggregation group with native VLAN ID 20 assigned to LAG 1:

For 6100 and 6200 switch series:

switch(config)# interface lag 1
switch(config-lag-if)# no shutdown
switch(config-lag-if)# lacp mode active
switch(config-lag-if)# vlan trunk native 20
switch(config-lag-if)# vlan trunk allowed 20

For 6300, 6400, 8320, 8325, 8360, and 8400 switch series:

switch(config)# interface lag 1
switch(config-lag-if)# no shutdown
switch(config-lag-if)# no routing
switch(config-lag-if)# lacp mode active
switch(config-lag-if)# vlan trunk native 20
switch(config-lag-if)# vlan trunk allowed 20

Removing a native VLAN from LAG 1:

switch(config)# interface lag 1
switch(config-lag-if)# no vlan trunk native

50

AOS-CX 10.06 Link Aggregation Guide

Chapter 3
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

Chapter 3 Support and other resources

51

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

52

AOS-CX 10.06 Link Aggregation Guide