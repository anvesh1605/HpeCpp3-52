|        | AOS-CX      |       | 10.08 |        | Link   |       |
| ------ | ----------- | ----- | ----- | ------ | ------ | ----- |
|        | Aggregation |       |       |        | Guide  |       |
| 4100i, | 6000,       | 6100, | 6200, | 6300,  | 6400,  | 8320, |
|        | 8325,       | 8360, | 8400  | Switch | Series |       |
Published:November2021
Edition:3

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

| 2

Contents
Contents
| Contents                                          |                                            | 3   |
| ------------------------------------------------- | ------------------------------------------ | --- |
| About this                                        | document                                   | 5   |
| Applicableproducts                                |                                            | 5   |
| Latestversionavailableonline                      |                                            | 5   |
| Commandsyntaxnotationconventions                  |                                            | 5   |
| Abouttheexamples                                  |                                            | 6   |
| Identifyingswitchportsandinterfaces               |                                            | 7   |
| Identifyingmodularswitchcomponents                |                                            | 8   |
| Link Aggregation                                  |                                            | 9   |
| Overview                                          |                                            | 9   |
| Aggregationgroup,memberport,andaggregateinterface |                                            | 9   |
| Linkaggregationmodes                              |                                            | 10  |
| LACP                                              |                                            | 10  |
|                                                   | LACPoperatingmodes                         | 10  |
| LAGinterfacestates                                |                                            | 10  |
| Howstaticlinkaggregationgroupsarebuilt            |                                            | 11  |
|                                                   | Referenceportselectionprocess              | 11  |
|                                                   | Settingtheaggregationstateofeachmemberport | 11  |
Settingtheaggregationstateofamemberportinastaticaggregationgroup 12
| Howdynamiclinkaggregationgroupsarebuilt                   |                                                      | 12  |
| --------------------------------------------------------- | ---------------------------------------------------- | --- |
|                                                           | Choosingareferenceport                               | 12  |
|                                                           | Settingtheaggregationstateofeachmemberport           | 13  |
| LAGconfigurationguidelines                                |                                                      | 13  |
|                                                           | Aggregationmemberinterfacerestrictions               | 13  |
|                                                           | Requirementsforaddinginterfaces                      | 13  |
| Layer2aggregationgroups                                   |                                                      | 14  |
|                                                           | ConfiguringaLayer2staticaggregationgroup             | 14  |
|                                                           | ConfiguringaLayer2dynamicaggregationgroup            | 17  |
| Layer3aggregationgroups                                   |                                                      | 20  |
|                                                           | ConfiguringaLayer3staticaggregationgroup             | 20  |
|                                                           | ConfiguringaLayer3dynamicaggregationgroup            | 23  |
| RemovingaLAG                                              |                                                      | 26  |
| RemovinganinterfacefromaLAG                               |                                                      | 27  |
| ChangingtheLAGmembershipforaninterface                    |                                                      | 28  |
| ConfigurationofanaggregateInterface                       |                                                      | 31  |
|                                                           | Configuringthedescriptionofanaggregateinterface      | 31  |
|                                                           | SettingtheMTUforaLayer2memberlinkinterface           | 32  |
|                                                           | SettingtheMTUforaLayer3aggregateinterface            | 32  |
|                                                           | Impactofshuttingdownorbringingupanaggregateinterface | 33  |
|                                                           | Shuttingdownanaggregateinterface                     | 33  |
| Supportedhashingalgorithms                                |                                                      | 33  |
| LACPconfigurationsettings                                 |                                                      | 33  |
| InterfaceLACPsettings                                     |                                                      | 34  |
| Configurationverification                                 |                                                      | 34  |
| BFDreportsaLAGasdownevenwhenhealthylinksarestillavailable |                                                      | 35  |
| LACPandLAGcommands                                        |                                                      | 36  |
3
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

|                          | description                    |           | 36  |
| ------------------------ | ------------------------------ | --------- | --- |
|                          | hash                           |           | 37  |
|                          | interfacelag                   |           | 37  |
|                          | ipaddress                      |           | 39  |
|                          | ipv6address                    |           | 39  |
|                          | lacphash                       |           | 40  |
|                          | lacpmode                       |           | 41  |
|                          | lacpport-id                    |           | 42  |
|                          | lacpport-priority              |           | 43  |
|                          | lacprate                       |           | 44  |
|                          | lacpsystem-priority            |           | 45  |
|                          | lag                            |           | 45  |
|                          | showinterface                  |           | 46  |
|                          | showlacpaggregates             |           | 48  |
|                          | showlacpconfiguration          |           | 49  |
|                          | showlacpinterfaces             |           | 50  |
|                          | shutdown                       |           | 53  |
|                          | vlantrunknative                |           | 53  |
| Smartlink                |                                |           | 56  |
| Guidelinesandlimitations |                                |           | 56  |
| Smartlinkcommands        |                                |           | 57  |
|                          | Configurationcommands          |           | 57  |
|                          | smartlinkgroup                 |           | 57  |
|                          | smartlinkrecv-control-vlan     |           | 57  |
|                          | Groupcontextcommands           |           | 58  |
|                          | description                    |           | 58  |
|                          | primary-port                   |           | 59  |
|                          | smartlinkgroupsecondary-port   |           | 60  |
|                          | control-vlan                   |           | 60  |
|                          | protected-vlans                |           | 61  |
|                          | preemption                     |           | 62  |
|                          | preemption-delay               |           | 62  |
|                          | Displaycommands                |           | 63  |
|                          | showsmartlinkgroup             |           | 63  |
|                          | showsmartlinkgroupall          |           | 64  |
|                          | showsmartlinkgroupdetail       |           | 65  |
|                          | showsmartlinkflush-statistics  |           | 65  |
|                          | clearsmartlinkgroupstatistics  |           | 66  |
|                          | clearsmartlinkflush-statistics |           | 67  |
|                          | showrunning-config             |           | 67  |
|                          | Supportabilitycommands         |           | 68  |
|                          | showcapacitiessmartlink        |           | 68  |
| Support                  | and Other                      | Resources | 70  |
| AccessingArubaSupport    |                                |           | 70  |
| AccessingUpdates         |                                |           | 70  |
|                          | ArubaSupportPortal             |           | 70  |
|                          | MyNetworking                   |           | 71  |
| WarrantyInformation      |                                |           | 71  |
| RegulatoryInformation    |                                |           | 71  |
| DocumentationFeedback    |                                |           | 71  |
Contents|4

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A)

n Aruba 8400 Switch Series (JL375A, JL376A)

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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables are
enclosed in angle brackets (< >). Substitute the text—including the
enclosing angle brackets—with an actual value.

AOS-CX 10.08 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

5

Convention

Usage

|

{ }

[ ]

… or

...

n For output formats where italic text can be displayed, variables might

or might not be enclosed in angle brackets. Substitute the text
including the enclosing angle brackets, if any, with an actual value.

Vertical bar. A logical OR that separates multiple items from which you can
choose only one.
Any spaces that are on either side of the vertical bar are included for
readability and are not a required part of the command syntax.

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

About this document | 6

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 4100i Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6000 and 6100 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

On the 6200 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10. The

primary switch is always member 1. If the switch is not a member of a VSF stack, then member is 1.

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

On the 83xx Switch Series

AOS-CX 10.08 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

7

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split to 4 x 10G or 4 x 25G. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on

physical port 4 in slot 1 on member 1.

On the 8400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/5 and 1/6.

o Line modules are on the front of the switch in slots 1/1 through 1/4, and 1/7 through 1/10.

n port: Physical number of a port on a line module

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on member 1.

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

About this document | 8

Chapter 2

Link Aggregation

Link Aggregation

Overview
Ethernet link aggregation bundles multiple physical Ethernet links into one logical link, called a link
aggregation group (LAG).

Link aggregation has the following benefits:

n Increased bandwidth beyond the limits of any single link. In an aggregate link, traffic is distributed across

the member ports.

n Improved link reliability. The member ports dynamically back up one another. When a member port fails,
its traffic is automatically switched to other member ports. As shown in the following figure Device A and
Device B are connected by three physical Ethernet links. These physical Ethernet links are combined into
an aggregate link called link aggregation 1. The bandwidth of this aggregate link can reach up to the total
bandwidth of the three physical Ethernet links. At the same time, the three Ethernet links back up one
another. When a physical Ethernet link fails, the traffic originally intended for the failed link is switched to
the remaining active links.

Ethernet link aggregation diagram

Aggregation group, member port, and aggregate interface
An aggregation group is a collection of physical interfaces that are bundled together for the purpose of load
distribution and redundancy. These physical interfaces are called member ports. They are configured
through a logical aggregate interface.

An aggregate interface can be one of the following types:

n Layer 2: The member ports of the corresponding Link Aggregation Group can only be Layer 2 Ethernet

interfaces.

n Layer 3: The member ports of the corresponding Link Aggregation Group can only be Layer 3 interfaces.

Layer 3 aggregation groups are not supported on the 4100i, 6000, 6100, and 6200 Switch Series.

The effective port rate of an aggregate interface equals the total rate of its member ports. Only full duplex
mode members are eligible for aggregation.

AOS-CX 10.08 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

9

Link aggregation modes
An aggregation group operates in one of the following modes:

n Static LAG: In the static LAG mode of operation, Link failure is not detected as there is no keep alive

PDU communication between the devices. A misconfiguration on one side can cause much trouble and
be difficult to troubleshoot, because no signaling takes place between the two peers.

n Dynamic LAG or LACP: The local device and the peer device automatically maintain the aggregation

states of the member ports, resulting in link failure being quickly detected by exchanging the PDU. LACP
reduces the workload of network administrators.

Dynamic LAG uses LACP packets to establish the association between two peers. This configuration results in
the reduction of the misconfiguration probability. Also, link failures are intelligently handled by two
participating devices through the LACP protocol, which is adaptive/dynamic to these network failures.

Layer 2 aggregation groups and Layer 3 aggregation groups support both the static and dynamic modes.

LACP
Dynamic aggregation is implemented through the IEEE 802.3ad Link Aggregation Control Protocol (LACP).

LACP uses LACPDUs to exchange aggregation information between LACP-enabled devices. Each member
port in a dynamic aggregation group can exchange information with its peer. When a member port receives
an LACPDU, it compares the received information with information received on the other member ports. In
this way, the two systems agree on which ports are placed in Selected state.

The LACPDU fields convey data for the LACP functions, including:

n System LACP priority

n System MAC address

n Port priority

n Port number

n Operational key

LACP operating modes

LACP can operate in active or passive mode.

n Active mode: When the LACP is operating in active mode on either end of a link, both ports can send

PDUs. The "active" LACP initiates an LACP connection by sending LACPDUs. The "passive" LACP will wait
for the remote end to initiate the link.

n Passive mode: When the LACP is operating in passive mode on a local member port and as its peer port,

both ports cannot send PDUs.

Two peer ports operating in "passive" mode will never establish an LACP link.

For an LACP LAG, one side must have LACP in active mode and the peer must have an LACP configuration of
active or passive mode. If you do not enable LACP on a LAG, it is treated as a static LAG and the peer cannot
negotiate LACP with the LAG.

LAG interface states
The output from the CLI commands show lacp interfaces and show lacp interfaces multi-chassis
display the following interface states:

Link Aggregation | 10

Interface state

Description

A - Active

An active LACP interface.

C - Collecting

Data frames are received through the aggregate link and sent onto the intended

destination.

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

With the long timeout, an LACPDU is sent every 30 seconds. If no response comes

from its partner after three LACPDUs are sent (90 seconds), a timeout event occurs.
The LACP state machine then transitions to the appropriate state based on its

current state.

N - InSync

The physical port is connected to the aggregate port that was last chosen by the

logical election. The state variable selected is still true.

O - OutofSync

The hardware might be out of sync with the modified protocol information. If the

hardware also has a status of collecting, do not transmit frames because they will

be misdelivered.

P - Passive

The port participates in the protocol, as long as it has an active partner.

S - Short-timeout

In the short timeout configuration, an LACPDU is sent every second. If no response

comes from its partner after three LACPDUs are sent, a timeout event occurs. The

LACP state machine then transitions to the appropriate state based on its current

state.

X - State m/c
expired

The "current while" timer has expired. The "current while" timer then restarts with

the short-timeout enabled.

The term State m/c refers to a state machine.

How static link aggregation groups are built

Reference port selection process

When setting the aggregation states of the ports in an aggregation group, the system automatically chooses
a member port as the reference port. A selected port must have the same operational key and attribute
configurations as the reference port.

The system chooses a reference port from the member ports in the up state. The first member interface
which is operationally up is selected as reference port.

Setting the aggregation state of each member port

AOS-CX 10.08 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

11

Afterthereferenceportischosen,thesystemsetstheaggregationstateofeachmemberportinthestatic
aggregationgroup.
| Setting     | the aggregation |     | state | of a member | port | in a static |
| ----------- | --------------- | --- | ----- | ----------- | ---- | ----------- |
| aggregation | group           |     |       |             |      |             |
AfterthemaximumlimitofmembersisreachedinaLAG,anadditionalportcannotbeaddedtothe
aggregationgroup.Ifaportbelongstoacardtypewithadifferentspeedthantheotheraggregation
members,theportcanstillbeaddedtotheaggregationgroup.IfdynamicLAGisenabled,anyportmember
withaspeeddifferentthanotheraggregationmembersisblockedorineligiblefromthesameaggregation
group.Anyoperationalkeys/attributesorconfigurationchangesmightaffecttheaggregationstatesofthe
memberports.
| How      | dynamic     | link | aggregation | groups | are | built |
| -------- | ----------- | ---- | ----------- | ------ | --- | ----- |
| Choosing | a reference |      | port        |        |     |       |
Thesystemchoosesareferenceportfromthememberportsinupstate.Aselectedportmusthavethe
sameoperationalkeyandattributeconfigurationsasthereferenceport.
LinkAggregation|12

The process by which the local system (the actor) and the peer system (the partner) negotiate a reference
port occurs as follows:

1. The two systems determine the system with the smaller system ID. A system ID contains the system

LACP priority and the system MAC address.
a. The two systems compare their LACP priority values.

The lower the LACP priority, the smaller the system ID. If the LACP priority values are the same,
the two systems proceed to step b.

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

n A dynamic link aggregation group chooses only full-duplex ports as the selected ports.

n For stable aggregation and service continuity, do not change the operational key or attribute

configurations on any member port.

LAG configuration guidelines

Aggregation member interface restrictions

n If any features in the following list are configured on the interface, you cannot assign an interface to a

Layer 2 aggregation group:

o MAC authentication

o Port security

o 802.1X

n Do not assign a reflector port for port mirroring to an aggregation group.

Requirements for adding interfaces

Keep in mind the following requirements when adding interfaces to a LAG:

n To determine the maximum number of LAG interfaces for your type of switch, look at the output from

the show capacities lag command; however, the number of LAGs that can be created depends on the
availability of the physical interface since each LAG interface needs at least one physical interface as a
member link. fter the maximum limit of members is reached in a LAG, an additional port cannot be
added to the aggregation group. If a port belongs to a card type with a different speed than the other
aggregation members, the port can still be added to the aggregation group. If dynamic LAG is enabled,
any port member with a speed different than other aggregation members is blocked or ineligible from
the same aggregation group. Any operational keys/attributes or configuration changes might affect the

AOS-CX 10.08 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

13

aggregation states of the member ports.

n The nondefaults configuration on an interface is removed automatically when the interface is added to a
link aggregation. For example: Assume that you remove a member interface from an existing LAG and
add it to another LAG. The software removes the nondefault configurations on the interface when it is
added to the new LAG.

Configuration consistency requirements

n Configure at least one active mode aggregation in two devices.

n For a successful static aggregation, make sure the ports at both ends of each link are in the same

aggregation state.

n For a successful dynamic aggregation, make sure the peer ports of the ports aggregated at one end are
also aggregated, and that one of the ends is configured as "active". The two ends can automatically
negotiate the aggregation state of each member port.

Removing interfaces

n Deleting an aggregate interface also deletes its aggregation group and causes all member ports to leave

the aggregation group.

n When a member interface is removed from a LAG:

o 4100i, 6000, 6100, 6200, 6300, and 6400 switches: The interface goes to its default status of

unshut.

o 8320, 8325, 8360, or 8400 switches: The interface becomes disabled.

Disabling an interface

When an interface LAG is disabled with the shutdown command, all its members also become operationally
down.

Layer 2 aggregation groups
All switches support static and dynamic layer 2 aggregation groups.

On the 6400 Switch Series, port identification differs. Line card ports start at 1/3/1.

Configuring a Layer 2 static aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#.

Procedure

1. Create a Layer 2 aggregate interface and access the Layer 2 aggregate interface view by entering:

switch(config)# interface lag <ID>

The range of the LAG interface ID is 1 to 256.

While creating the Layer 2 aggregate interface, the system automatically creates a Layer 2 static
aggregation group numbered the same.

Link Aggregation | 14

2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
| switch(config-lag-if)# |     | no shutdown |     |
| ---------------------- | --- | ----------- | --- |
Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecausethe
commandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofamember
interface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface   | 1/1/2 |
| --- | ------------------ | ----------- | ----- |
|     | switch(config-if)# | no shutdown |       |
3. Onthe8320,8325,8360,and8400,disableroutingbyentering:
| switch(config-lag-if)# |     | no routing |     |
| ---------------------- | --- | ---------- | --- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformationabout
theno routingcommand.
Onthe4100i,6000,6100,and6200SwitchSeries,routingisnotsupportedonphysicalinterfaces.
Onthe6300and6400SwitchSeries,routingisdisabledbydefault.
4. AssignanativeVLANIDtoatrunkinterfaceontheLAGbyentering:
| switch(config-lag-if)# |     | vlan trunk | native <VLAN-ID> |
| ---------------------- | --- | ---------- | ---------------- |
Forexample:
| switch(config-lag-if)# |     | vlan trunk | native 1 |
| ---------------------- | --- | ---------- | -------- |
5. Usethefollowingstepstoaddamaximumof16interfacestotheLAG:
a. ToassignaninterfacetotheLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID> |
| ---------------------- | --- | --------- | --------- |
ToassignarangeofinterfacestoaLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID>-<PORT-ID> |
| ---------------------- | --- | --------- | ------------------- |
Forexample:
| switch(config-lag-if)# |     | interface | 1/1/1-1/1/4 |
| ---------------------- | --- | --------- | ----------- |
15
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformore
| informationabouttheinterface |     | <PORT-ID>command. |     |
| ---------------------------- | --- | ----------------- | --- |
b. AssignanIDtotheLAG:
switch(config-if)# lag <ID>
Forexample:
switch(config-if-<1/1/1-1/1/4>)# lag 100
c. Settheadministrativestateofthememberinterfacetoup:
switch(config-if-<1/1/1-1/1/4>)# no shutdown
6. Viewtheconfigurationbyenteringthefollowing:
For4100i,6000,6100,6200,6300,and6400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     | show running-config |     |
| -------------------------------- | --- | ------------------- | --- |
Current configuration:
!
vlan 1
| interface lag | 100 |     |     |
| ------------- | --- | --- | --- |
no shutdown
| vlan trunk      | native 1    |     |     |
| --------------- | ----------- | --- | --- |
| vlan trunk      | allowed all |     |     |
| interface 1/1/1 |             |     |     |
no shutdown
lag 100
| interface 1/1/2 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| interface 1/1/3 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| interface 1/1/4 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| switch(config-if-<1/1/1-1/1/4>)# |               | show lacp   | aggregates |
| -------------------------------- | ------------- | ----------- | ---------- |
| Aggregate name                   | : lag100      |             |            |
| Interfaces                       | : 1/1/3 1/1/1 | 1/1/4 1/1/2 |            |
| Heartbeat rate                   | : N/A         |             |            |
| Hash                             | : l3-src-dst  |             |            |
| Aggregate mode                   | : Off         |             |            |
For8320,8325,8360,and8400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     | show running-config |     |
| -------------------------------- | --- | ------------------- | --- |
Current configuration:
!
LinkAggregation|16

| vlan      | 1   |         |     |     |     |     |
| --------- | --- | ------- | --- | --- | --- | --- |
| interface |     | lag 100 |     |     |     |     |
no shutdown
no routing
|           | vlan | trunk native  | 1   |     |     |     |
| --------- | ---- | ------------- | --- | --- | --- | --- |
|           | vlan | trunk allowed | all |     |     |     |
| interface |      | 1/1/1         |     |     |     |     |
no shutdown
lag 100
| interface |     | 1/1/2 |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| interface |     | 1/1/3 |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| interface |     | 1/1/4 |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| switch(config-if-<1/1/1-1/1/4>)# |     |         |               | show  | lacp aggregates |       |
| -------------------------------- | --- | ------- | ------------- | ----- | --------------- | ----- |
| Aggregate                        |     | name    | : lag100      |       |                 |       |
| Interfaces                       |     |         | : 1/1/3 1/1/1 | 1/1/4 | 1/1/2           |       |
| Heartbeat                        |     | rate    | : N/A         |       |                 |       |
| Hash                             |     |         | : l3-src-dst  |       |                 |       |
| Aggregate                        |     | mode    | : Off         |       |                 |       |
| Configuring                      |     | a Layer | 2 dynamic     |       | aggregation     | group |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer2aggregateinterfaceandaccesstheLayer2aggregateinterfaceviewbyentering:
|     | switch(config)# |     | interface | lag | <ID> |     |
| --- | --------------- | --- | --------- | --- | ---- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer2aggregateinterface,thesystemautomaticallycreatesaLayer2dynamic
aggregationgroupnumberedthesame.
2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
|     | switch(config-lag-if)# |     |     | no shutdown |     |     |
| --- | ---------------------- | --- | --- | ----------- | --- | --- |
17
| AOS-CX10.08LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecausethe
commandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofamember
interface,enterthecommandattheinterfacelevel.Forexample:
| switch(config)# | interface | 1/1/2 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)# no shutdown
3. Onthe8320,8325,8360,and8400,disableroutingbyentering:
| switch(config-lag-if)# | no routing |     |     |
| ---------------------- | ---------- | --- | --- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformationabout
theno routingcommand.
Onthe4100i,6000,6100,and6200SwitchSeries,routingisnotsupportedonphysical
interfaces.
Onthe6300and6400SwitchSeries,routingisdisabledbydefault.
4. Configuretheaggregationgrouptooperateindynamicmodebyentering:
| switch(config-lag-if)# | lacp mode | {active | | passive} |
| ---------------------- | --------- | ------- | ---------- |
Forexample:
| switch(config-lag-if)# | lacp mode | active |     |
| ---------------------- | --------- | ------ | --- |
5. Configuretheaggregationgrouptooperateinfastorslowmodebyentering:
| switch(config-lag-if)# | lacp rate | {fast | | slow} |
| ---------------------- | --------- | ------- | ----- |
Forexample:
| switch(config-lag-if)# | lacp rate | fast |     |
| ---------------------- | --------- | ---- | --- |
6. AssignanativeVLANIDtoatrunkinterfacebyentering:
| switch(config-lag-if)# | vlan trunk | native | <VLAN-ID> |
| ---------------------- | ---------- | ------ | --------- |
Forexample:
| switch(config-lag-if)# | vlan trunk | native | 1   |
| ---------------------- | ---------- | ------ | --- |
LinkAggregation|18

7. Usethefollowingstepstoaddamaximumof16interfacestotheLAG:
a. ToassignaninterfacetotheLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID> |
| ---------------------- | --- | --------- | --------- |
ToassignarangeofinterfacestoaLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID>-<PORT-ID> |
| ---------------------- | --- | --------- | ------------------- |
Forexample:
| switch(config-lag-if)# |     | interface | 1/1/1-1/1/4 |
| ---------------------- | --- | --------- | ----------- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformore
| informationabouttheinterface |     | <PORT-ID>command. |     |
| ---------------------------- | --- | ----------------- | --- |
b. AssignanIDtotheLAG:
switch(config-if)#
lag <ID>
Forexample:
switch(config-if-<1/1/1-1/1/4>)# lag 20
c. Settheadministrativestateofthememberinterfacetoup:
switch(config-if-<1/1/1-1/1/4>)# no shutdown
8. Viewtheconfigurationbyentering:
For4100i,6000,6100,6200,6300,and6400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     | show | running-config |
| -------------------------------- | --- | ---- | -------------- |
Current configuration:
!
vlan 1
| interface lag | 20  |     |     |
| ------------- | --- | --- | --- |
no shutdown
| vlan trunk      | native 1    |     |     |
| --------------- | ----------- | --- | --- |
| vlan trunk      | allowed all |     |     |
| lacp mode       | active      |     |     |
| lacp rate       | fast        |     |     |
| interface 1/1/1 |             |     |     |
no shutdown
lag 20
| switch(config-if-<1/1/1-1/1/4>)# |               | show        | lacp aggregates |
| -------------------------------- | ------------- | ----------- | --------------- |
| Aggregate name                   | : lag100      |             |                 |
| Interfaces                       | : 1/1/3 1/1/1 | 1/1/4 1/1/2 |                 |
19
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

| Heartbeat |     | rate | : Fast       |     |     |     |     |
| --------- | --- | ---- | ------------ | --- | --- | --- | --- |
| Hash      |     |      | : l3-src-dst |     |     |     |     |
| Aggregate |     | mode | : Active     |     |     |     |     |
For8320,8325,8360,and8400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     |                |     |     | show running-config |     |     |
| -------------------------------- | --- | -------------- | --- | --- | ------------------- | --- | --- |
| Current                          |     | configuration: |     |     |                     |     |     |
!
| vlan      | 1   |        |     |     |     |     |     |
| --------- | --- | ------ | --- | --- | --- | --- | --- |
| interface |     | lag 20 |     |     |     |     |     |
no shutdown
no routing
|           | vlan | trunk native  | 1   |     |     |     |     |
| --------- | ---- | ------------- | --- | --- | --- | --- | --- |
|           | vlan | trunk allowed |     | all |     |     |     |
|           | lacp | mode active   |     |     |     |     |     |
|           | lacp | rate fast     |     |     |     |     |     |
| interface |      | 1/1/1         |     |     |     |     |     |
no shutdown
lag 20
| switch(config-if-<1/1/1-1/1/4>)# |               |      |              |        | show lacp   | aggregates |     |
| -------------------------------- | ------------- | ---- | ------------ | ------ | ----------- | ---------- | --- |
| Aggregate                        |               | name | : lag100     |        |             |            |     |
| Interfaces                       |               |      | : 1/1/3      | 1/1/1  | 1/1/4 1/1/2 |            |     |
| Heartbeat                        |               | rate | : Fast       |        |             |            |     |
| Hash                             |               |      | : l3-src-dst |        |             |            |     |
| Aggregate                        |               | mode | : Active     |        |             |            |     |
| Layer                            | 3 aggregation |      |              | groups |             |            |     |
Layer3aggregationgroupsaresupportedonallswitchseriesexcept6000,6100,and6200SwitchSeries.
| Configuring |     | a Layer | 3   | static | aggregation |     | group |
| ----------- | --- | ------- | --- | ------ | ----------- | --- | ----- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer3aggregateinterfaceandaccesstheLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# |     | interface |     | lag <ID> |     |     |
| --- | --------------- | --- | --------- | --- | -------- | --- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer3aggregateinterface,thesystemautomaticallycreatesaLayer3static
aggregationgroupnumberedthesame.
LinkAggregation|20

2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
n For6300and6400switchseries:
|     | switch(config-lag-if)# |     |     | no shutdown |     |
| --- | ---------------------- | --- | --- | ----------- | --- |
|     | switch(config-lag-if)# |     |     | routing     |     |
Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     |     | switch(config)#    |     | interface | 1/1/2    |
| --- | --- | ------------------ | --- | --------- | -------- |
|     |     | switch(config-if)# |     | no        | shutdown |
|     |     | switch(config-if)# |     | routing   |          |
For8320,8325,8360,and8400switchseries:
n
|     | switch(config-lag-if)# |     |     | no shutdown |     |
| --- | ---------------------- | --- | --- | ----------- | --- |
Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     |     | switch(config)#    |     | interface | 1/1/2    |
| --- | --- | ------------------ | --- | --------- | -------- |
|     |     | switch(config-if)# |     | no        | shutdown |
3. SettheIPaddressontheLAGinterfacebyentering:
|     | switch(config-lag-if)# |     |     | ip address | <IPV4-ADDR>/<MASK> |
| --- | ---------------------- | --- | --- | ---------- | ------------------ |
Forexample:
| switch(config-lag-if)# |     |     | ip address | 192.0.2.1/30 |     |
| ---------------------- | --- | --- | ---------- | ------------ | --- |
4. Usethefollowingstepstoaddamaximumof16interfacestotheLAG:
a. ToassignaninterfacetotheLAG:
|     | switch(config-lag-if)# |     |     | interface | <PORT-ID> |
| --- | ---------------------- | --- | --- | --------- | --------- |
ToassignarangeofinterfacestoaLAG:
|     | switch(config-lag-if)# |     |     | interface | <PORT-ID>-<PORT-ID> |
| --- | ---------------------- | --- | --- | --------- | ------------------- |
21
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

Forexample:
| switch(config-lag-if)# |     | interface | 1/1/1-1/1/4 |
| ---------------------- | --- | --------- | ----------- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformore
| informationabouttheinterface |     | <PORT-ID>command. |     |
| ---------------------------- | --- | ----------------- | --- |
b. AssignanIDtotheLAG:
switch(config-if)# lag <ID>
Forexample:
switch(config-if-<1/1/1-1/1/4>)# lag 100
c. Settheadministrativestateofthememberinterfacetoup:
switch(config-if-<1/1/1-1/1/4>)# no shutdown
5. Viewtheconfigurationbyenteringthefollowing:
For6300and6400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     | show | running-config |
| -------------------------------- | --- | ---- | -------------- |
Current configuration:
!
vlan 1
| interface lag | 100 |     |     |
| ------------- | --- | --- | --- |
no shutdown
routing
| ip address      | 192.0.2.1/30 |     |     |
| --------------- | ------------ | --- | --- |
| interface 1/1/1 |              |     |     |
no shutdown
lag 100
| interface 1/1/2 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| interface 1/1/3 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| interface 1/1/4 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| switch(config-if-<1/1/1-1/1/4>)# |               | show        | lacp aggregates |
| -------------------------------- | ------------- | ----------- | --------------- |
| Aggregate name                   | : lag100      |             |                 |
| Interfaces                       | : 1/1/3 1/1/1 | 1/1/4 1/1/2 |                 |
| Heartbeat rate                   | : N/A         |             |                 |
| Hash                             | : l3-src-dst  |             |                 |
| Aggregate mode                   | : Off         |             |                 |
LinkAggregation|22

For8320,8325,8360,and8400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     |                |     | show | running-config |     |
| -------------------------------- | --- | -------------- | --- | ---- | -------------- | --- |
| Current                          |     | configuration: |     |      |                |     |
!
| vlan      | 1   |         |     |     |     |     |
| --------- | --- | ------- | --- | --- | --- | --- |
| interface |     | lag 100 |     |     |     |     |
no shutdown
|           | ip address | 192.0.2.1/30 |     |     |     |     |
| --------- | ---------- | ------------ | --- | --- | --- | --- |
| interface |            | 1/1/1        |     |     |     |     |
no shutdown
lag 100
| interface |     | 1/1/2 |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| interface |     | 1/1/3 |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| interface |     | 1/1/4 |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| switch(config-if-<1/1/1-1/1/4>)# |     |         |               | show  | lacp aggregates |       |
| -------------------------------- | --- | ------- | ------------- | ----- | --------------- | ----- |
| Aggregate                        |     | name    | : lag100      |       |                 |       |
| Interfaces                       |     |         | : 1/1/3 1/1/1 | 1/1/4 | 1/1/2           |       |
| Heartbeat                        |     | rate    | : N/A         |       |                 |       |
| Hash                             |     |         | : l3-src-dst  |       |                 |       |
| Aggregate                        |     | mode    | : Off         |       |                 |       |
| Configuring                      |     | a Layer | 3 dynamic     |       | aggregation     | group |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer3aggregateinterfaceandaccesstheLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# |     | interface | lag | <ID> |     |
| --- | --------------- | --- | --------- | --- | ---- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer3aggregateinterface,thesystemautomaticallycreatesaLayer3dynamic
aggregationgroupnumberedthesame.
2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
For6300and6400switchseries:
n
|     | switch(config-lag-if)# |     |     | no shutdown |     |     |
| --- | ---------------------- | --- | --- | ----------- | --- | --- |
|     | switch(config-lag-if)# |     |     | routing     |     |     |
23
| AOS-CX10.08LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface | 1/1/2       |     |
| --- | ------------------ | --------- | ----------- | --- |
|     | switch(config-if)# |           | no shutdown |     |
|     | switch(config-if)# |           | routing     |     |
For8320,8325,8360,and8400switchseries:
n
| switch(config-lag-if)# |     | no shutdown |     |     |
| ---------------------- | --- | ----------- | --- | --- |
Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface | 1/1/2       |     |
| --- | ------------------ | --------- | ----------- | --- |
|     | switch(config-if)# |           | no shutdown |     |
3. Configuretheaggregationgrouptooperateindynamicmodebyentering:
| switch(config-lag-if)# |     | lacp mode | {active | | passive} |
| ---------------------- | --- | --------- | ------- | ---------- |
Forexample:
| switch(config-lag-if)# |     | lacp mode | active |     |
| ---------------------- | --- | --------- | ------ | --- |
4. Configuretheaggregationgrouptooperateinfastorslowmodebyentering:
| switch(config-lag-if)# |     | lacp rate | {fast | | slow} |
| ---------------------- | --- | --------- | ------- | ----- |
Forexample:
| switch(config-lag-if)# |     | lacp rate | fast |     |
| ---------------------- | --- | --------- | ---- | --- |
5. SettheIPaddressontheLAGinterfacebyentering:
| switch(config-lag-if)# |     | ip address | <IPV4-ADDR>/<MASK> |     |
| ---------------------- | --- | ---------- | ------------------ | --- |
Forexample:
LinkAggregation|24

| switch(config-lag-if)# | ip address | 192.0.3.1/30 |
| ---------------------- | ---------- | ------------ |
6. Usethefollowingstepstoaddamaximumof16interfacestotheLAG:
a. ToassignaninterfacetotheLAG:
| switch(config-lag-if)# | interface | <PORT-ID> |
| ---------------------- | --------- | --------- |
ToassignarangeofinterfacestoaLAG:
| switch(config-lag-if)# | interface | <PORT-ID>-<PORT-ID> |
| ---------------------- | --------- | ------------------- |
Forexample:
| switch(config-lag-if)# | interface | 1/1/1-1/1/4 |
| ---------------------- | --------- | ----------- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformore
| informationabouttheinterface | <PORT-ID>command. |     |
| ---------------------------- | ----------------- | --- |
b. AssignanIDtotheLAG:
| switch(config-if)# | lag <ID> |     |
| ------------------ | -------- | --- |
Forexample:
| switch(-<1/1/1-1/1/4>)# | lag | 100 |
| ----------------------- | --- | --- |
c. Settheadministrativestateofthememberinterfacetoup:
switch(-<1/1/1-1/1/4>)#
|     | no  | shutdown |
| --- | --- | -------- |
7. Viewtheconfigurationbyentering:
For6300and6400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# | show | running-config |
| -------------------------------- | ---- | -------------- |
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
25
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

no shutdown
lag 100
| interface 1/1/3 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| interface 1/1/4 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| switch(config-if-<1/1/1-1/1/4>)# |               | show lacp   | aggregates |
| -------------------------------- | ------------- | ----------- | ---------- |
| Aggregate name                   | : lag100      |             |            |
| Interfaces                       | : 1/1/3 1/1/1 | 1/1/4 1/1/2 |            |
| Heartbeat rate                   | : Fast        |             |            |
| Hash                             | : l3-src-dst  |             |            |
| Aggregate mode                   | : Active      |             |            |
For8320,8325,8360,and8400switchseries:
switch(config-if-<1/1/1-1/1/4>)#
show running-config
Current configuration:
!
vlan 1
| interface lag | 100 |     |     |
| ------------- | --- | --- | --- |
no shutdown
| ip address      | 192.0.3.1/30 |     |     |
| --------------- | ------------ | --- | --- |
| lacp mode       | active       |     |     |
| lacp rate       | fast         |     |     |
| interface 1/1/1 |              |     |     |
no shutdown
lag 100
| interface 1/1/2 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| interface 1/1/3 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| interface 1/1/4 |     |     |     |
| --------------- | --- | --- | --- |
no shutdown
lag 100
| switch(config-if-<1/1/1-1/1/4>)# |               | show lacp   | aggregates |
| -------------------------------- | ------------- | ----------- | ---------- |
| Aggregate name                   | : lag100      |             |            |
| Interfaces                       | : 1/1/3 1/1/1 | 1/1/4 1/1/2 |            |
| Heartbeat rate                   | : Fast        |             |            |
| Hash                             | : l3-src-dst  |             |            |
| Aggregate mode                   | : Active      |             |            |
| Removing a                       | LAG           |             |            |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
LinkAggregation|26

DeletetheLAG.Enter:
| switch(config)# | no interface |     | lag <ID> |     |
| --------------- | ------------ | --- | -------- | --- |
Forexample:
| switch(config)# | no interface |     | lag 100 |     |
| --------------- | ------------ | --- | ------- | --- |
AllinterfacesassignedtotheLAGareautomaticallyremovedfromtheLAGaspartofthedeletionprocessof
theLAG.AfterremovingaphysicalinterfacefromaLAG,
n 4100i, 6000, 6100, 6200, 6300, and6400 switches: TheinterfaceassociatedwiththeLAGbecomes
layer2portswiththedefaultlayer2configurationsandadminstatusenabled.
n 8320, 8235, 8360, and8400 switches: TheinterfaceassociatedwiththeLAGbecomeslayer3ports
withdefaultlayer3configurationsandadministrativedown.
| Removing | an interface |     | from | a LAG |
| -------- | ------------ | --- | ---- | ----- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
RemoveaninterfacefromtheLAG.Enter:
| switch(config)#    | interface | <PORT-NUM> |     |     |
| ------------------ | --------- | ---------- | --- | --- |
| switch(config-if)# | no        | lag <ID>   |     |     |
Forexample:
| switch(config)# | interface | 1/1/1 |     |     |
| --------------- | --------- | ----- | --- | --- |
switch(config-if)#
|                    | no   | lag 100        |     |     |
| ------------------ | ---- | -------------- | --- | --- |
| switch(config-if)# | show | running-config |     |     |
...
!
| vlan 1    |         |     |     |     |
| --------- | ------- | --- | --- | --- |
| interface | lag 100 |     |     |     |
| interface | 1/1/1   |     |     |     |
| interface | 1/1/2   |     |     |     |
lag 100
switch(config-if)#
ToassignarangeofinterfacestoaLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID>-<PORT-ID> |     |
| ---------------------- | --- | --------- | ------------------- | --- |
Forexample:
| switch(config-lag-if)# |     | interface | 1/1/1-1/1/4 |     |
| ---------------------- | --- | --------- | ----------- | --- |
27
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

AfterremovingaphysicalinterfacefromaLAG:
4100i, 6000, 6100, 6200, 6300, and6400 switches:TheinterfaceassociatedwithLAGbecomeslayer
n
2portswithdefaultlayer2configurationsandwithadminstatusofenabled
8320, 8325, 8360, and8400 switches:TheinterfaceassociatedwiththeLAGbecomesL3portswith
n
defaultL3configurationsandadministrativedown.Forexample,supposeinterface1/1/1waspartof
LAG3andyouhadadministrativelyenabledtheinterface.Ifyoulaterremoveinterface1/1/1fromLAG
3,theadministrativestatusautomaticallychangestodown.Ifyouwanttousetheinterfaceagain,you
mustadministrativelyenableitagain.
| Changing | the LAG | membership |     | for an | interface |
| -------- | ------- | ---------- | --- | ------ | --------- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. RemoveaninterfacefromtheLAG.Enter:
| switch(config)#    |     | interface | <PORT-NUM> |     |     |
| ------------------ | --- | --------- | ---------- | --- | --- |
| switch(config-if)# |     | no lag    | <ID>       |     |     |
Forexample:
For4100i,6000,6100,6200,6300,and6400switchseries:
| switch(config)#    |     | interface | 1/1/1          |     |     |
| ------------------ | --- | --------- | -------------- | --- | --- |
| switch(config-if)# |     | no lag    | 100            |     |     |
| switch(config-if)# |     | show      | running-config |     |     |
Current configuration:
!
...
!
vlan 1
| interface | lag | 100 |     |     |     |
| --------- | --- | --- | --- | --- | --- |
no shutdown
|     | vlan trunk | native 1 |     |     |     |
| --- | ---------- | -------- | --- | --- | --- |
|     | vlan trunk | allowed  | all |     |     |
interface 1/1/1
interface 1/1/2
no shutdown
lag 100
switch(config-if)#
For8320,8325,8360,and8400switchseries:
| switch(config)#    |     | interface | 1/1/1          |     |     |
| ------------------ | --- | --------- | -------------- | --- | --- |
| switch(config-if)# |     | no lag    | 100            |     |     |
| switch(config-if)# |     | show      | running-config |     |     |
Current configuration:
!
...
!
LinkAggregation|28

vlan 1
| interface lag | 100 |     |     |
| ------------- | --- | --- | --- |
no shutdown
no routing
vlan trunk native 1
| vlan trunk      | allowed | all |     |
| --------------- | ------- | --- | --- |
| interface 1/1/1 |         |     |     |
| interface 1/1/2 |         |     |     |
no shutdown
lag 100
switch(config-if)#
AfterremovingaphysicalinterfacefromaLAG,theinterfaceassociatedwiththeLAGbecomesL3
portswithdefaultL3configurationsandadministrativedown.Forexample,supposeinterface1/1/1
waspartofLAG3andyouhadadministrativelyenabledtheinterface.Ifyoulaterremoveinterface
1/1/1fromLAG3,theadministrativestatusautomaticallychangestodown.Ifyouwanttousethe
interfaceagain,youmustadministrativelyenableitagain.
On4100i,6000,6100,and6200SwitchSeries,afterremovingaphysicalinterfacefromaLAG,the
interfaceassociatedwiththeLAGbecomeslayer2portswithdefaultlayer2configurationsand
adminstatusenabled.
2. CreatetheLAGtowhichyouwanttoaddtheinterface:
| switch(config-if)# | interface |     | lag 10 |
| ------------------ | --------- | --- | ------ |
Forexample:
For4100i,6000,6100,6200,6300,and6400switchseries:
| switch(config-if)#     | interface | lag      | 10       |
| ---------------------- | --------- | -------- | -------- |
| switch(config-lag-if)# | no        | shutdown |          |
| switch(config-lag-if)# | vlan      | trunk    | native 1 |
For8320,8325,8360,and8400switchseries:
| switch(config-if)#     | interface | lag      | 10       |
| ---------------------- | --------- | -------- | -------- |
| switch(config-lag-if)# | no        | shutdown |          |
| switch(config-lag-if)# | no        | routing  |          |
| switch(config-lag-if)# | vlan      | trunk    | native 1 |
3. AddtheinterfacefromStep1tothenewlycreatedLAG:
| switch(config)#    | interface |     | 1/1/1 |
| ------------------ | --------- | --- | ----- |
| switch(config-if)# | lag       | 10  |       |
Forexample:
For4100i,6000,6100,6200,6300,and6400switchseries:
| switch(config)#    | interface |     | 1/1/1 |
| ------------------ | --------- | --- | ----- |
| switch(config-if)# | lag       | 10  |       |
29
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

| switch(config-if)# | show running-config |     |
| ------------------ | ------------------- | --- |
Current configuration:
!
...
!
vlan 1
| interface lag 10 |     |     |
| ---------------- | --- | --- |
no shutdown
| vlan trunk native  | 1   |     |
| ------------------ | --- | --- |
| vlan trunk allowed | all |     |
| interface lag 100  |     |     |
no shutdown
| vlan trunk native  | 1   |     |
| ------------------ | --- | --- |
| vlan trunk allowed | all |     |
interface 1/1/1
lag 10
interface 1/1/2
no shutdown
lag 100
For8320,8325,8360,and8400switchseries:
switch(config)#
interface 1/1/1
| switch(config-if)# | lag 10              |     |
| ------------------ | ------------------- | --- |
| switch(config-if)# | show running-config |     |
Current configuration:
!
...
!
vlan 1
| interface lag 10 |     |     |
| ---------------- | --- | --- |
no shutdown
no routing
| vlan trunk native  | 1   |     |
| ------------------ | --- | --- |
| vlan trunk allowed | all |     |
| interface lag 100  |     |     |
no shutdown
no routing
| vlan trunk native  | 1   |     |
| ------------------ | --- | --- |
| vlan trunk allowed | all |     |
interface 1/1/1
lag 10
interface 1/1/2
no shutdown
lag 100
Noticethatinterface1/1/1inthepreviousexampleisstillnotactive,eventhoughithasbeenadded
toLAG10.Tochangetheadministrativestateofthememberinterface,entertheno shutdown
commandattheinterfacelevel.
Forexample:
For4100i,6000,6100,6200,6300,and6400switchseries:
| switch(config-if)# | interface           | 1/1/1 |
| ------------------ | ------------------- | ----- |
| switch(config-if)# | no shutdown         |       |
| switch(config-if)# | show running-config |       |
Current configuration:
LinkAggregation|30

!
...
!
vlan 1
|     | interface | lag 10 |     |     |     |
| --- | --------- | ------ | --- | --- | --- |
no shutdown
|     | vlan      | trunk native 1    |     |     |     |
| --- | --------- | ----------------- | --- | --- | --- |
|     | vlan      | trunk allowed all |     |     |     |
|     | interface | lag 100           |     |     |     |
no shutdown
|     | vlan      | trunk native 1    |     |     |     |
| --- | --------- | ----------------- | --- | --- | --- |
|     | vlan      | trunk allowed all |     |     |     |
|     | interface | 1/1/1             |     |     |     |
no shutdown
|     | lag 10    |       |     |     |     |
| --- | --------- | ----- | --- | --- | --- |
|     | interface | 1/1/2 |     |     |     |
no shutdown
|     | lag 100 |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
For8320,8325,8360,and8400switchseries:
|     | switch(config-if)# | interface | 1/1/1 |     |     |
| --- | ------------------ | --------- | ----- | --- | --- |
switch(config-if)#
|     |                        | no shutdown         |     |     |     |
| --- | ---------------------- | ------------------- | --- | --- | --- |
|     | switch(config-if)#     | show running-config |     |     |     |
|     | Current configuration: |                     |     |     |     |
!
...
!
vlan 1
|     | interface | lag 10 |     |     |     |
| --- | --------- | ------ | --- | --- | --- |
no shutdown
no routing
|     | vlan      | trunk native 1    |     |     |     |
| --- | --------- | ----------------- | --- | --- | --- |
|     | vlan      | trunk allowed all |     |     |     |
|     | interface | lag 100           |     |     |     |
no shutdown
no routing
|     | vlan      | trunk native 1    |     |     |     |
| --- | --------- | ----------------- | --- | --- | --- |
|     | vlan      | trunk allowed all |     |     |     |
|     | interface | 1/1/1             |     |     |     |
no shutdown
|     | lag 10    |       |     |     |     |
| --- | --------- | ----- | --- | --- | --- |
|     | interface | 1/1/2 |     |     |     |
no shutdown
|               | lag 100 |                 |       |           |           |
| ------------- | ------- | --------------- | ----- | --------- | --------- |
| Configuration |         | of an aggregate |       | Interface |           |
| Configuring   | the     | description     | of an | aggregate | interface |
Youcanconfigurethedescriptionofanaggregateinterfaceforadministrationpurposes,forexample,
describingthepurposeoftheinterface.
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
31
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- |

1. CreateaLayer3aggregateinterfaceandenterLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |
| --- | --------------- | --------- | -------- | --- |
2. Configurethedescriptionoftheaggregateinterface:
|         | switch(config-if)# | description | <text>   |                |
| ------- | ------------------ | ----------- | -------- | -------------- |
| Setting | the MTU            | for a Layer | 2 member | link interface |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. EnteraLayer2memberlinkinterfaceviewbyentering:
|     | switch(config)# | interface | <INTERFACE-ID> |     |
| --- | --------------- | --------- | -------------- | --- |
2. SettheMTUfortheLayer2memberlinkinterface:
|     | switch(config-if)# | mtu | <VALUE> |     |
| --- | ------------------ | --- | ------- | --- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformation
aboutthemtu <VALUE>command.Whenallowingjumboframesunderalayer2aggregation
interface,makesurethattheMTUvalueissetappropriatelyunderallmemberinterfaces.
| Setting | the MTU | for a Layer | 3 aggregate | interface |
| ------- | ------- | ----------- | ----------- | --------- |
Layer3aggregationgroupsarenotsupportedonthe4100i,6000,6100,and6200SwitchSeries.
TheMTUofaninterfaceaffectsIPpacketsfragmentationandreassemblyontheinterface.
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. EnterLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <INTERFACE-ID> |     |
| --- | --------------- | --------- | ------------------ | --- |
2. SettheMTUfortheLayer3aggregateinterface:
|     | switch(config-lag-if)# |     | ip mtu <VALUE> |     |
| --- | ---------------------- | --- | -------------- | --- |
LinkAggregation|32

SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformation
abouttheip mtu <VALUE>command.Whenallowingjumboframesunderalayer2aggregation
interface,makesurethattheMTUvalueissetappropriatelyunderallmemberinterfaces.
IftheIPMTUisconfiguredas9198,theMTUonthephysicalinterfacesmustalsobeconfiguredas9198.
Impact of shutting down or bringing up an aggregate interface
Bydefault,anaggregateinterfaceisdown.Shuttingdownorbringingupanaggregateinterfaceaffectsthe
aggregationstatesandlinkstatesofmemberportsinthecorrespondingaggregationgroupasfollows:
n Whenanaggregateinterfaceisshutdown,allSelectedportsinthecorrespondingaggregationgroup
becomeUnselectedportsandallmemberportsgotoanoperationallydownstate.
Whenanaggregateinterfaceisbroughtup,theaggregationstatesofmemberportsinthecorresponding
n
aggregationgrouparerecalculated.LAGmembers,whichareadministrativelyup,willbecome
operationallyup.Themembersthatarenotadministrativelyupwillbeinthesamestateandnotmade
eligibleforaggregation.
| Shutting | down an | aggregate | interface |     |
| -------- | ------- | --------- | --------- | --- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
EntertheLayer3aggregateinterfaceviewbyentering:
| switch(config)# | interface | lag <ID> |     |     |
| --------------- | --------- | -------- | --- | --- |
Shutdowntheaggregateinterface:
| switch(config-lag-if)# |         | shutdown   |     |     |
| ---------------------- | ------- | ---------- | --- | --- |
| Supported              | hashing | algorithms |     |     |
n SourceMACanddestinationMAC
SourceIPanddestinationIP
n
Sourceportanddestinationport.
n
| LACP | configuration | settings |     |         |
| ---- | ------------- | -------- | --- | ------- |
| Task |               | Command  |     | Example |
SettingtheLACPmodeto lacp mode {active | passive} switch(config-lag-if)# lacp
| activeorpassive. |     |     |     | mode active |
| ---------------- | --- | --- | --- | ----------- |
SettingtheLACPmodetooff. no lacp mode {active | passive} switch(config-lag-if)# no
33
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

| Task | Command |     |     | Example   |        |     |
| ---- | ------- | --- | --- | --------- | ------ | --- |
|      |         |     |     | lacp mode | active |     |
Settingthehashtype.
|     | For6000,6100,and           | 8400        | Switch     | For6000,6100,and           | 8400    | Switch |
| --- | -------------------------- | ----------- | ---------- | -------------------------- | ------- | ------ |
|     | Series:                    |             |            | Series:                    |         |        |
|     | lacp hash                  | [l2-src-dst | | l3-src-  | switch(config)#            | lacp    | hash   |
|     | dst | l4-src-dst]          |             |            | l2-src-dst                 |         |        |
|     | For8320,8325,6200,6300,and |             | 6400       | For8320,8325,6200,6300,and |         |        |
|     | Switch                     | Series:     |            | 6400 Switch                | Series: |        |
|     | hash [l2-src-dst           | |           | l3-src-dst | | switch(config-lag-if)#   |         | hash   |
|     | l4-src-dst]                |             |            | l2-src-dst                 |         |        |
SettingtheLACPratetofast. lacp rate fast switch(config)# interface
lag 1
|     |     |     |     | switch(config-lag-if)# |     | lacp |
| --- | --- | --- | --- | ---------------------- | --- | ---- |
rate fast
SettingtheLACPratetoslow. lacp rate slow switch(config)# interface
lag 1
|     |     |     |     | switch(config-lag-if)# |     | lacp |
| --- | --- | --- | --- | ---------------------- | --- | ---- |
rate slow
| Applyingshutdownonthe | shutdown |     |     | switch(config)# | interface |     |
| --------------------- | -------- | --- | --- | --------------- | --------- | --- |
| LAGport.              |          |     |     | lag 1           |           |     |
switch(config-lag-if)#
shutdown
Resettingeveryinterfacein no shutdown switch(config-lag-if)# no
| theLAGtothedefault(up)  |         |     |     | shutdown |     |     |
| ----------------------- | ------- | --- | --- | -------- | --- | --- |
| Interface LACP settings |         |     |     |          |     |     |
| Task                    | Command |     |     | Example  |     |     |
SettingtheLACPportID. lacp port-id <ID> switch(config-if)# lacp port-
id 100
SettingtheLACPportIDtothe no lacp port-id switch(config-if)# no lacp
| default. |     |     |     | port-id |     |     |
| -------- | --- | --- | --- | ------- | --- | --- |
SettingtheLACPportpriority. lacp port-priority <PORT- switch(config-if)# lacp port-
|     | PRIORITY> |     |     | priority | 100 |     |
| --- | --------- | --- | --- | -------- | --- | --- |
SettingtheLACPportpriorityto no lacp port-priority switch(config-if)# no lacp
thedefault
port-priority
| Configuration verification |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- |
LinkAggregation|34

| Task | Command   |               | Example |     |     |
| ---- | --------- | ------------- | ------- | --- | --- |
|      | show lacp | configuration |         |     |     |
ViewingLACPglobal
|     |     |     | switch# | show lacp configuration |     |
| --- | --- | --- | ------- | ----------------------- | --- |
information
|     |     |     | System-id                    | : 70:72:cf:ef:fc:d9 |      |
| --- | --- | --- | ---------------------------- | ------------------- | ---- |
|     |     |     | System-priority              | : 65534             |      |
|     |     |     | Hash                         | : l3-src-dst        |      |
|     |     |     | Theoutputdisplayedfortheshow |                     | lacp |
configurationisfromthe8400seriesswitch.
|     | show lacp | aggregates |     |     |     |
| --- | --------- | ---------- | --- | --- | --- |
ViewingLACP
|     |     |     | switch# | show lacp aggregates |     |
| --- | --- | --- | ------- | -------------------- | --- |
aggregate
Aggregate-name : lag100
| information |     |     | Aggregated-interfaces |      | : 1/1/2 |
| ----------- | --- | --- | --------------------- | ---- | ------- |
|             |     |     | Heartbeat             | rate | : N/A   |
Hash : l3-src-dst
|     |     |     | Aggregate | mode | : off |
| --- | --- | --- | --------- | ---- | ----- |
Aggregate-name : lag110
Aggregated-interfaces : 1/1/1,
1/1/3
|     |     |     | Heartbeat | rate | : slow |
| --- | --- | --- | --------- | ---- | ------ |
Hash : l3-src-dst
|             |           |            | Aggregate | mode                 | : active |
| ----------- | --------- | ---------- | --------- | -------------------- | -------- |
| ViewingLACP | show lacp | aggregates |           |                      |          |
|             | lag100    |            | switch#   | show lacp aggregates | lag100   |
aggregate
Aggregate-name : lag100
| informationfora |     |     | Aggregated-interfaces |      | :     |
| --------------- | --- | --- | --------------------- | ---- | ----- |
| LAG             |     |     | Heartbeat             | rate | : N/A |
Hash : l3-src-dst
|             |           |            | Aggregate | mode | : off |
| ----------- | --------- | ---------- | --------- | ---- | ----- |
| ViewingLACP | show lacp | interfaces |           |      |       |
switch#
|     |     |     |     | show lacp interfaces |     |
| --- | --- | --- | --- | -------------------- | --- |
interfacedetails
Theoutputistoowidetodisplayinacolumn.The
commandoutputisprovidedintheCLItopicforthe
command.
| BFD reports | a LAG | as down | even when | healthy | links are |
| ----------- | ----- | ------- | --------- | ------- | --------- |
still available
Symptom
BFDisnotsupportedonthe4100i,6000,6100,and6200SwitchSeries.
TheBidirectionalForwardDetection(BFD)featurereportsaLinkAggregation(LAG),asbeingdown,even
thoughtherearehealthyLAGlinksavailable.TheLAG,containingthedownedlink,willeventuallyrebalance
thetraffictoitsotherlinks.
Cause
35
| AOS-CX10.08LinkAggregationGuide| | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| -------------------------------- | ----------------------------- | --- | --- | --- | --- |

ThisnotificationoccurswhentheminimumBFDcontrolpacketreceptionintervalissetatafasterratethan
theLinkAggregationControlProtocol(LACP)rateandLAGrebalancingoccurs.BFDassumesthatthelinkis
downwithoutrealizingthattheLAGisrebalancingthetrafficload.
Action
SettheminimumBFDcontrolpacketreceptionintervaltoaslowerratethantheLACPrateorsettheLACP
ratetoafasterratethantheminimumBFDcontrolpacketreceptioninterval.
1. TofindthecurrentsettingsoftheminimumBFDcontrolpacketreceptioninterval,entertheshow
running-configcommand.
TheminimumBFDcontrolpacketreceptionintervalsettingislistedasbfd min-receive-intervalin
thecommandoutputandthemeasurementisinms.
2. TofindthecurrentrateofLACP,entertheshow lacp aggregatescommand.
| TheLACPrateislistedastheHeatbeat |     | rateinthecommandoutput. |     |
| -------------------------------- | --- | ----------------------- | --- |
3. TochangetheminimumBFDcontrolpacketreceptioninterval,enterthebfd min-receive-interval
command.
4. TochangetheLACPrate,enterthelacp rate {fast | slow}command.
| LACP and LAG | commands |     |     |
| ------------ | -------- | --- | --- |
description
description <TEXT>
| no description <TEXT> |     |     |     |
| --------------------- | --- | --- | --- |
Description
ProvidesabriefdescriptionoftheLAGinterface.Thedescriptiontextissavedintheconfigurationofthe
LAG.Itisavailableevenafterareboot.
ThenoformofthiscommandremovesthedescriptionoftheLAGinterfacefromtheconfiguration.
| Parameter |     | Description                               |     |
| --------- | --- | ----------------------------------------- | --- |
| <TEXT>    |     | SpecifiesthedescriptionoftheLAGinterface. |     |
Example
| switch(config)# | interface | lag 10 |     |
| --------------- | --------- | ------ | --- |
switch(config-lag-if)# description This LAG is used for an example.
| switch(config-lag-if)# |     | show running-config |     |
| ---------------------- | --- | ------------------- | --- |
...
vlan 1
| interface lag | 10       |             |             |
| ------------- | -------- | ----------- | ----------- |
| description   | This LAG | is used for | an example. |
| interface lag | 60       |             |             |
switch(config-lag-if)#
CommandHistory
LinkAggregation|36

Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
hash
| hash [l2-src-dst | | l3-src-dst | | l4-src-dst] |
| ---------------- | ------------ | ------------- |
Description
Thiscommandcontrolstheselectionofaninterfaceinagroupofaggregateinterfaces.Thehashtypevalue
helpstransmitaframe.ThisconfigurationmustbedoneattheLAGinterfacelevel.
Parameter Description
l2-src-dst Specifiestheload-balancingcalculationtoincludeonlyLayer2
items,suchassourceanddestinationMACaddresses.
l3-src-dst Specifiestheload-balancingcalculationtoincludeonlyLayer3
items,suchassourceanddestinationIPaddresses.Default
setting.
l4-src-dst
Specifiestheload-balancingcalculationtoincludeonlyLayer4
items,suchassourceanddestinationUDP/TCPports.
Example
| switch(config-lag-if)# |     | hash l2-src-dst |
| ---------------------- | --- | --------------- |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
config-lag-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| interface     | lag      |     |
| ------------- | -------- | --- |
| interface lag | <ID>     |     |
| no interface  | lag <ID> |     |
37
| AOS-CX10.08LinkAggregationGuide| | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | ----------------------------- | --- |

Description

Creates a Link Aggregation Group (LAG) interface represented by an ID.

The no form of this command deletes a LAG interface represented by an ID.

Parameter

Description

<ID>

Usage

Specifies a LAG interface ID.

Keep in mind the following requirements when adding interfaces to a LAG:

n To determine the maximum number of LAG interfaces for your type of switch, look at the output from

the show capacities lag command; however, the number of LAGs that can be created depends on the
availability of the physical interface since each LAG interface needs at least one physical interface as a
member link.

n After the maximum limit of members is reached in a LAG, an additional port cannot be added to the
aggregation group. If a port belongs to a card type with a different speed than the other aggregation
members, the port can still be added to the aggregation group. If dynamic LAG is enabled, any port
member with a speed different than other aggregation members is blocked or ineligible from the same
aggregation group. Any operational keys/attributes or configuration changes might affect the
aggregation states of the member ports.

n The nondefaults configuration on an interface is removed automatically when the interface is added to a
link aggregation. For example: Assume that you remove a member interface from an existing LAG and
add it to another LAG. The software removes the nondefault configurations on the interface when it is
added to the new LAG.

Examples

Creating a Link Aggregation Group (LAG) interface represented by an ID of 100:

switch(config)# interface lag 100

Deleting a Link Aggregation Group (LAG) interface represented by an ID of 100:

switch(config)# no interface lag 100

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

config

Administrators or local user group members with execution rights
for this command.

Link Aggregation | 38

ip address
| ip address    | <IPV4-ADDR>/<MASK> |     |     | [secondary] |     |
| ------------- | ------------------ | --- | --- | ----------- | --- |
| no ip address | <IPV4-ADDR>/<MASK> |     |     | [secondary] |     |
Description
SetsanIPv4addressandsubnetmasktoaLAGinterface.Oneprimaryandupto31secondaryaddresscan
beconfiguredperinterface.
ThenoformofthiscommandremovestheIPv4addressfromtheinterface.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<IPV4-ADDR>
SpecifiesanIPaddressinIPv4format(x.x.x.x),wherexisa
decimalnumberfrom0to255.Youcanremoveleadingzeros.For
example,theaddress192.169.005.100becomes
192.168.5.100.
| <MASK> |     |     |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to32.
| secondary |     |     |     |     | SpecifiesasecondaryIPaddress. |
| --------- | --- | --- | --- | --- | ----------------------------- |
Examples
SettinganIPaddressontheLAGinterface1to198.51.100.1withamaskof24bits:
| switch(config)#        |     | interface |     | lag 1   |                 |
| ---------------------- | --- | --------- | --- | ------- | --------------- |
| switch(config-lag-if)# |     |           | ip  | address | 198.51.100.1/24 |
RemovingtheIPaddress198.51.100.1withamaskof24bitsfromLAGinterface1:
| switch(config)#        |     | interface |     | lag 1      |                 |
| ---------------------- | --- | --------- | --- | ---------- | --------------- |
| switch(config-lag-if)# |     |           | no  | ip address | 198.51.100.1/24 |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |
| --------- | -------------- | --- | --- | --- | --------- |
6300 config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8320
8325
8360
8400
ipv6 address
39
| AOS-CX10.08LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- |

ipv6 address <IPV6-ADDR>/<MASK>
no ipv6 address <IPV6-ADDR>/<MASK>

Description

Sets an IPv6 address and subnet mask to a LAG interface.

The no form of this command removes the IPv6 address from the interface.

Parameter

<IPV6-ADDR>

<MASK>

Examples

Description

Specifies the IP address in IPv6 format
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx), where x is a
hexadecimal number from 0 to F. You can use two colons (::) to
represent consecutive zeros (but only once), remove leading
zeros, and collapse a quartet of four zeros to a single 0. For
example, this address
2222:0000:3333:0000:0000:0000:4444:0055 becomes
2222:0:3333::4444:55.

Specifies the number of bits in the address mask in CIDR format
(x), where x is a decimal number from 0 to 128.

Setting the IPv6 address on LAG interface 1 to 2001:0db8:85a3::8a2e:0370:7334 with a mask of 24 bits:

switch(config)# interface lag 1
switch(config-lag-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Removing the IP address 2001:0db8:85a3::8a2e:0370:7334 with mask of 24 bits with a mask of 24 bits
from LAG interface 1:

switch(config)# interface lag 1
switch(config-lag-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

config-lag-if

Administrators or local user group members with execution rights
for this command.

6300
6400
8320
8325
8360
8400

lacp hash

Link Aggregation | 40

| lacp hash | [l2-src-dst |             | | l3-src-dst |            | | l4-src-dst] |
| --------- | ----------- | ----------- | ------------ | ---------- | ------------- |
| no lacp   | hash        | [l2-src-dst | |            | l3-src-dst | | l4-src-dst] |
Description
Controlstheselectionofaninterfaceinagroupofaggregateinterfaces.Thehashtypevaluehelpstransmit
aframe.Thisconfigurationmustbedoneatthegloballevel.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
l2-src-dst Specifiestheload-balancingcalculationtoincludeonlyLayer2
items,suchassourceanddestinationMACaddresses.
l3-src-dst Specifiestheload-balancingcalculationtoincludeonlyLayer3
items,suchassourceanddestinationIPaddresses.
l4-src-dst
Specifiestheload-balancingcalculationtoincludeonlyLayer4
items,suchassourceanddestinationUDP/TCPports.
Example
| switch(config)# |     |     | lacp hash | l2-src-dst |     |
| --------------- | --- | --- | --------- | ---------- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |
| -------------- | --- | --- | --- | --- | ------------ |
| 10.07orearlier |     |     |     |     | --           |
CommandInformation
| Platforms |     | Commandcontext |     |     | Authority |
| --------- | --- | -------------- | --- | --- | --------- |
config
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
6100
8400
lacp mode
| lacp mode | {active | |       | passive}   |     |     |
| --------- | ------- | ------- | ---------- | --- | --- |
| no lacp   | mode    | {active | | passive} |     |     |
Description
SetsanLACPmodetoactiveorpassive.
ThenoformofthiscommandsetstheLACPmodetooff,returningtheLAGtoastaticmodeaggregation.
| Parameter |     |     |     |     | Description                                          |
| --------- | --- | --- | --- | --- | ---------------------------------------------------- |
| active    |     |     |     |     | SpecifiesthatthelocalswitchwilltransmitLACPDataUnits |
(LACPDUs)toattempttonegotiatewiththeremotedevice.
41
| AOS-CX10.08LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
passive SpecifiesthatthelocalswitchwilllistenforLACPDUsfromthe
remotedeviceforLACPnegotiation.
NOTE:
AmomentarytrafficdropoccursbecauseLACPpartnersreconverge
whenchangingthemodefromactivetopassiveorfrompassiveto
active.
Examples
SettingtheLACPmodetoactive:
| switch(config)#        | interface | lag       | 1      |
| ---------------------- | --------- | --------- | ------ |
| switch(config-lag-if)# |           | lacp mode | active |
SettingtheLACPmodetooff:
| switch(config)#        | interface | lag     | 1           |
| ---------------------- | --------- | ------- | ----------- |
| switch(config-lag-if)# |           | no lacp | mode active |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-lag-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp port-id
| lacp port-id | <PORT-ID> |     |     |
| ------------ | --------- | --- | --- |
no lacp port-id
Description
SetstheLACPportIDvalueofthememberinterfaceoftheLAG.
ThenoformofthiscommandremovestheLACPportIDvaluefromtheinterface.
| Parameter |     |     | Description                           |
| --------- | --- | --- | ------------------------------------- |
| <PORT-ID> |     |     | SpecifiesaportIDvalue.Range:1to65535. |
Examples
SettinganLACPportIDtoavalueof10:
LinkAggregation|42

| switch(config-if)# | lacp port-id | 10  |
| ------------------ | ------------ | --- |
RemovingtheLACPportIDvalue:
| switch(config-if)# | no lacp port-id |     |
| ------------------ | --------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp port-priority
| lacp port-priority | <PORT-PRIORITY> |     |
| ------------------ | --------------- | --- |
no lacp port-priority
Description
SetsanLACPportpriorityvalueforthememberinterfaceoftheLAG.
ThenoformofthiscommandrevertstheLACPportprioritytothedefault,whichis1.
| Parameter |     | Description |
| --------- | --- | ----------- |
<PORT-PRIORITY>
Specifiesaportpriorityvalue.Range:1to65535.
Examples
SettingaLACPportpriorityvalueof10:
| switch(config-if)# | lacp port-priority | 10  |
| ------------------ | ------------------ | --- |
RevertingtheLACPportIDtothedefault:
| switch(config-if)# | no lacp port-priority |     |
| ------------------ | --------------------- | --- |
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
43
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp rate
| lacp rate {fast | | slow}       |     |     |
| --------------- | ------------- | --- | --- |
| no lacp rate    | {fast | slow} |     |     |
Description
SetsanLACPheartbeatrequesttimetofastorslow.
ThenoformofthecommandsetsanLACPratetoslow.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
fast
Specifiestheheartbeatrequesttoeverysecond,andthetimeout
periodisathree-consecutiveheartbeatlossthatis3seconds.
| slow |     |     | Specifiestheheartbeatrequesttoevery30seconds.Thetimeout |
| ---- | --- | --- | ------------------------------------------------------- |
periodisthree-consecutiveheartbeatlossthatis90seconds.
Defaultsetting.
Examples
SettingtheLACPheartbeatrequesttimetofast:
| switch(config)#        | interface | lag       | 1    |
| ---------------------- | --------- | --------- | ---- |
| switch(config-lag-if)# |           | lacp rate | fast |
ResettingtheLACPheartbeatrequesttimetothedefault,whichisslow:
| switch(config)#        | interface | lag     | 1    |
| ---------------------- | --------- | ------- | ---- |
| switch(config-lag-if)# |           | no lacp | rate |
AnotherwaytosettheLACPheartbeatrequesttimetothedefault,whichisslow:
| switch(config)#        | interface | lag       | 1    |
| ---------------------- | --------- | --------- | ---- |
| switch(config-lag-if)# |           | lacp rate | slow |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
LinkAggregation|44

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp system-priority
| lacp system-priority | <SYSTEM-PRIORITY-VALUE> |     |
| -------------------- | ----------------------- | --- |
no lacp system-priority <SYSTEM-PRIORITY-VALUE>
Description
SetsaLinkAggregationControlProtocol(LACP)systempriority.
ThenoformofthiscommandsetsanLACPsystemprioritytothedefault,whichis65534.
| Parameter |     | Description |
| --------- | --- | ----------- |
<SYSTEM-PRIORITY-VALUE>
Specifiesasystempriorityvalue.Range:0to65535.
Examples
SettingaLinkAggregationControlProtocol(LACP)systempriorityto100:
| switch(config)# | lacp system-priority | 100 |
| --------------- | -------------------- | --- |
SettinganLACPsystemprioritytothedefault(65534):
| switch(config)# | no lacp system-priority |     |
| --------------- | ----------------------- | --- |
AmomentarytrafficdropcanbeseenincasetheLACPstatemachinemustrenegotiate.
CommandHistory
| Release        |     | Modification |
| -------------- | --- | ------------ |
| 10.07orearlier |     | --           |
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lag
lag <ID>
no lag <ID>
Description
AddsaninterfacetoaspecifiedLAGinterfaceID.
45
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

The no form of this command removes an interface from a specified LAG interface ID. The member loses its
LACP configuration when removed from the LAG. The member also reaches the default state with an
administrative shutdown. For 6300 and 6400 series switches, the administrative state is enabled.
Configurations, such as MTU and UDLD, are retained.

Parameter

Description

<ID>

Usage

Specifies a LAG interface ID. Range: 1 to 256.

n All members of the LAG must have the same speed. If a member comes up late with a different speed, it
will not participate in the LAG/LACP. The hardware restriction is applied before adding an interface to
LAG. The member belongs to the card type that has the same maximum speed as the reference port card
type.

n To move an interface from LagA to LagB, first remove the interface from LagA and then add it to LagB.
When a member is attached to a LAG, the nondefault configurations on the member are removed
silently.

n After removing a physical interface from a LAG, the interface associated with the LAG becomes L3 ports
with default L3 configurations and administrative down. For example, suppose interface 1/1/1 was part
of LAG 3 and you had administratively enabled the interface. If you later remove interface 1/1/1 from
LAG 3, the administrative status automatically changes to down. If you want to use the interface again,
you must administratively enable it again.

Examples

Adding an interface to a Link Aggregation Group (LAG) represented by an ID of 100:

switch(config)# interface 1/1/1
switch(config-if)# lag 100

Deleting an interface from a Link Aggregation Group (LAG) represented by an ID of 100:

switch(config)# interface 1/1/1
switch(config-if)# no lag 100

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

config-if

Administrators or local user group members with execution rights
for this command.

show interface

Link Aggregation | 46

| show | interfaces | <LAG-NAME> |     | [vsx-peer] |     |     |     |
| ---- | ---------- | ---------- | --- | ---------- | --- | --- | --- |
Description
DisplaysinformationaboutaspecificLAG.
| Parameter  |     |     |     |     | Description                              |     |     |
| ---------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- |
| <LAG-NAME> |     |     |     |     | SpecifiesaLAGname.                       |     |     |
| vsx-peer   |     |     |     |     | ShowstheoutputfromtheVSXpeerswitch.Ifthe |     |     |
switchesdonothavetheVSXconfigurationortheISLis
down,theoutputfromtheVSXpeerswitchisnot
displayed.Thisparameterisavailableonswitchesthat
supportVSX.
Examples
DisplayinginformationaboutLAG100:
|     | switch#               | show interface | lag100    |     |                     |     |       |
| --- | --------------------- | -------------- | --------- | --- | ------------------- | --- | ----- |
|     | Aggregate             | lag100         | is up     |     |                     |     |       |
|     | Admin                 | state is up    |           |     |                     |     |       |
|     | Description           | :              |           |     |                     |     |       |
|     | MAC Address           |                |           |     | : 48:0f:cf:af:43:9c |     |       |
|     | Aggregated-interfaces |                |           |     | : 1/1/2             |     |       |
|     | Aggregation-key       |                |           |     | : 100               |     |       |
|     | Aggregate             | mode           |           |     | : active            |     |       |
|     | Speed                 |                |           |     | : 2000 Mb/s         |     |       |
|     | L3 Counters:          | Rx             | Disabled, | Tx  | Disabled            |     |       |
|     | qos trust             | none           |           |     |                     |     |       |
|     | VLAN Mode:            | access         |           |     |                     |     |       |
|     | Access                | VLAN: 1        |           |     |                     |     |       |
|     | Statistics            |                |           |     | RX                  | TX  | Total |
------------- -------------------- -------------------- --------------------
|     | Packets   |        |     |     | 20   | 45   | 65   |
| --- | --------- | ------ | --- | --- | ---- | ---- | ---- |
|     | Unicast   |        |     |     | 5    | 5    | 10   |
|     | Multicast |        |     |     | 5    | 15   | 20   |
|     | Broadcast |        |     |     | 10   | 25   | 35   |
|     | Bytes     |        |     |     | 5658 | 2584 | 8242 |
|     | Jumbos    |        |     |     | 0    | 0    | 0    |
|     | Dropped   |        |     |     | 0    | 0    | 0    |
|     | Filtered  |        |     |     | 0    | 0    | 0    |
|     | Pause     | Frames |     |     | 0    | 0    | 0    |
|     | Errors    |        |     |     | 0    | 0    | 0    |
|     | CRC/FCS   |        |     |     | 0    | n/a  | 0    |
|     | Collision |        |     |     | n/a  | 0    | 0    |
|     | Runts     |        |     |     | 0    | n/a  | 0    |
|     | Giants    |        |     |     | 0    | n/a  | 0    |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
47
| AOS-CX10.08LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

| Platforms |     | Commandcontext |     |     | Authority |
| --------- | --- | -------------- | --- | --- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show      | lacp       | aggregates |              |            |     |
| --------- | ---------- | ---------- | ------------ | ---------- | --- |
| show lacp | aggregates |            | [<LAG-NAME>] | [vsx-peer] |     |
Description
DisplaysallLACPaggregateinformationconfiguredforallLAGs,orforaspecificLAG.
| Parameter  |     |     |     |     | Description                              |
| ---------- | --- | --- | --- | --- | ---------------------------------------- |
| <LAG-NAME> |     |     |     |     | Optional:Specifiesalagname.              |
| vsx-peer   |     |     |     |     | ShowstheoutputfromtheVSXpeerswitch.Ifthe |
switchesdonothavetheVSXconfigurationortheISLis
down,theoutputfromtheVSXpeerswitchisnot
displayed.Thisparameterisavailableonswitchesthat
supportVSX.
Examples
DisplayingLACPaggregateinformationconfiguredforlag10:
| switch#               |     | show lacp | aggregates   | lag10 |     |
| --------------------- | --- | --------- | ------------ | ----- | --- |
| Aggregate-name        |     |           | : lag10      |       |     |
| Aggregated-interfaces |     |           | : 1/1/1      | 1/1/2 |     |
| Heartbeat             |     | rate      | : slow       |       |     |
| Hash                  |     |           | : l3-src-dst |       |     |
| Aggregate             |     | mode      | : active     |       |     |
DisplayingLACPaggregates:
| switch#               |     | show lacp | aggregates   |     |               |
| --------------------- | --- | --------- | ------------ | --- | ------------- |
| Aggregate-name        |     |           | : lag1       |     |               |
| Aggregated-interfaces |     |           | : 1/1/27     |     | 1/1/28 1/1/29 |
| Heartbeat             |     | rate      | : slow       |     |               |
| Hash                  |     |           | : l3-src-dst |     |               |
| Aggregate             |     | mode      | : active     |     |               |
| Aggregate-name        |     |           | : lag2       |     |               |
| Aggregated-interfaces |     |           | : 1/1/48     |     |               |
| Heartbeat             |     | rate      | : slow       |     |               |
| Hash                  |     |           | : l2-src-dst |     |               |
| Aggregate             |     | mode      | : passive    |     |               |
CommandHistory
LinkAggregation|48

| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show      | lacp configuration |            |     |
| --------- | ------------------ | ---------- | --- |
| show lacp | configuration      | [vsx-peer] |     |
Description
DisplaysglobalLACPconfiguration.
| Parameter |     |     | Description                              |
| --------- | --- | --- | ---------------------------------------- |
| vsx-peer  |     |     | ShowstheoutputfromtheVSXpeerswitch.Ifthe |
switchesdonothavetheVSXconfigurationortheISLis
down,theoutputfromtheVSXpeerswitchisnot
displayed.Thisparameterisavailableonswitchesthat
supportVSX.
Examples
DisplayingglobalLACPconfiguration(outputisapplicablefor8400seriesswitches):
| switch#         | show lacp   | configuration     |     |
| --------------- | ----------- | ----------------- | --- |
| System-id       | :           | 70:72:cf:ef:fc:d9 |     |
| System-priority | :           | 65534             |     |
| Hash            | :l3-src-dst |                   |     |
DisplayingglobalLACPconfiguration(outputisapplicablefor8320,6300,and6400seriesswitches):
| switch#         | show lacp | configuration     |     |
| --------------- | --------- | ----------------- | --- |
| System-id       | :         | 98:f2:b3:68:40:a0 |     |
| System-priority | :         | 65534             |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
49
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

| Platforms |     | Commandcontext |     |     |     | Authority |     |     |     |     |
| --------- | --- | -------------- | --- | --- | --- | --------- | --- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show      | lacp       | interfaces |            |     |            |     |     |     |     |     |
| --------- | ---------- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
| show lacp | interfaces |            | [<IFNAME>] |     | [vsx-peer] |     |     |     |     |     |
Description
DisplaysanLACPconfigurationofthephysicalinterfaces,includingVSXs.Ifaninterfacenameispassedas
argument,itonlydisplaysanLACPconfigurationofaspecifiedinterface.
| Parameter |     |     |     |     |     | Description                              |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
| <IFNAME>  |     |     |     |     |     | Optional:Specifiesaninterfacename.       |     |     |     |     |
| vsx-peer  |     |     |     |     |     | ShowstheoutputfromtheVSXpeerswitch.Ifthe |     |     |     |     |
switchesdonothavetheVSXconfigurationortheISLis
down,theoutputfromtheVSXpeerswitchisnot
displayed.Thisparameterisavailableonswitchesthat
supportVSX.
Examples
ThisexampledisplaysanLACPconfigurationofthephysicalinterfaces.Oneoftheinterfaceshasthelacp-
blockforwardingstate.IfaVSXswitchhasloopprotectenabledonaninterfaceandaloopoccurs,VSX
blockstheinterfacetostoptheloop.Theforwardingstateoftheblockedinterfaceissettolacp-block.
| switch# |               | show lacp | interfaces |                |     |     |            |          |            |     |
| ------- | ------------- | --------- | ---------- | -------------- | --- | --- | ---------- | -------- | ---------- | --- |
| State   | abbreviations |           |            | :              |     |     |            |          |            |     |
| A -     | Active        |           | P          | - Passive      |     | F - | Aggregable | I -      | Individual |     |
| S -     | Short-timeout |           | L          | - Long-timeout |     | N - | InSync     | O -      | OutofSync  |     |
| C -     | Collecting    |           | D          | - Distributing |     |     |            |          |            |     |
| X -     | State         | m/c       | expired    |                |     | E - | Default    | neighbor | state      |     |
| Actor   | details       |           | of all     | interfaces:    |     |     |            |          |            |     |
------------------------------------------------------------------------------------
| Intf | Aggr |     | Port | Port | State | System-id |     |     | System Aggr | Forwarding |
| ---- | ---- | --- | ---- | ---- | ----- | --------- | --- | --- | ----------- | ---------- |
|      | name |     | id   | Pri  |       |           |     |     | Pri Key     | State      |
------------------------------------------------------------------------------------
| 1/1/1   | lag10  |         | 17     | 1           | ALFOE  | 70:72:cf:37:a3:5c |     |     | 20 10  | lacp-block |
| ------- | ------ | ------- | ------ | ----------- | ------ | ----------------- | --- | --- | ------ | ---------- |
| 1/1/2   | lag128 |         | 69     | 1           | ALFNCD | 70:72:cf:37:a3:5c |     |     | 20 128 | up         |
| 1/1/3   | lag128 |         | 14     | 1           | ALFNCD | 70:72:cf:37:a3:5c |     |     | 20 128 | up         |
| 1/1/4   | lag128 |         |        |             |        |                   |     |     |        | down       |
| 1/1/5   | lag20  |         |        |             |        |                   |     |     |        | up         |
| Partner |        | details | of all | interfaces: |        |                   |     |     |        |            |
------------------------------------------------------------------------------
| Intf | Aggr |     | Partner | Port |     | State | System-id |     | System   | Aggr |
| ---- | ---- | --- | ------- | ---- | --- | ----- | --------- | --- | -------- | ---- |
|      | name |     | Port-id | Pri  |     |       |           |     | Priority | Key  |
------------------------------------------------------------------------------
| 1/1/1 | lag10  |     | 0   | 65534 |     | PLFOEX | 00:00:00:00:00:00 |     | 65534 | 0   |
| ----- | ------ | --- | --- | ----- | --- | ------ | ----------------- | --- | ----- | --- |
| 1/1/2 | lag128 |     | 69  | 1     |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
| 1/1/3 | lag128 |     | 14  | 1     |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
LinkAggregation|50

1/1/4 lag128
1/1/5 lag20
DisplayingstaticLAG:
| switch# | show          | lacp interfaces |                |     |              |          |              |     |
| ------- | ------------- | --------------- | -------------- | --- | ------------ | -------- | ------------ | --- |
| State   | abbreviations |                 | :              |     |              |          |              |     |
| A -     | Active        | P               | - Passive      | F   | - Aggregable | I        | - Individual |     |
| S -     | Short-timeout | L               | - Long-timeout | N   | - InSync     | O        | - OutofSync  |     |
| C -     | Collecting    | D               | - Distributing |     |              |          |              |     |
| X -     | State m/c     | expired         |                | E   | - Default    | neighbor | state        |     |
| Actor   | details       | of all          | interfaces:    |     |              |          |              |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State | System-id |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---- | ----- | --------- | --- | ----------- | ---------- |
|      | Name | Id   | Pri  |       |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag10   |     |                 |     |     |     |     | up  |
| ------- | ------- | --- | --------------- | --- | --- | --- | --- | --- |
| 1/1/2   | lag10   |     |                 |     |     |     |     | up  |
| Partner | details | of  | all interfaces: |     |     |     |     |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State | System-id |     | System Aggr |     |
| ---- | ---- | ---- | ---- | ----- | --------- | --- | ----------- | --- |
|      | Name | Id   | Pri  |       |           |     | Pri Key     |     |
------------------------------------------------------------------------------
1/1/1 lag10
1/1/2 lag10
DisplayinganLACPconfigurationofthe1/1/1interface:
| switch#        | show          | lacp interfaces |                | 1/1/1 |              |          |              |     |
| -------------- | ------------- | --------------- | -------------- | ----- | ------------ | -------- | ------------ | --- |
| State          | abbreviations |                 | :              |       |              |          |              |     |
| A -            | Active        | P               | - Passive      | F     | - Aggregable | I        | - Individual |     |
| S -            | Short-timeout | L               | - Long-timeout | N     | - InSync     | O        | - OutofSync  |     |
| C -            | Collecting    | D               | - Distributing |       |              |          |              |     |
| X -            | State m/c     | expired         |                | E     | - Default    | neighbor | state        |     |
| Aggregate-name |               | : lag1          |                |       |              |          |              |     |
-------------------------------------------------
|     |     |     | Actor |     | Partner |     |     |     |
| --- | --- | --- | ----- | --- | ------- | --- | --- | --- |
-------------------------------------------------
| Port-id         |     |     | | 28                |     | | 31                |     |     |     |
| --------------- | --- | --- | ------------------- | --- | ------------------- | --- | --- | --- |
| Port-priority   |     |     | | 1                 |     | | 1                 |     |     |     |
| Key             |     |     | | 1                 |     | | 1                 |     |     |     |
| State           |     |     | | ALFNCD            |     | | ALFNCD            |     |     |     |
| System-id       |     |     | | 98:f2:b3:68:40:a0 |     | | 98:f2:b3:68:60:a6 |     |     |     |
| System-priority |     |     | | 65534             |     | | 65534             |     |     |     |
DisplayinganLACPconfigurationafterloop-protectisenabledontheprimaryVSXswitch:
| switch# | show          | lacp interfaces |                |     |              |     |              |     |
| ------- | ------------- | --------------- | -------------- | --- | ------------ | --- | ------------ | --- |
| State   | abbreviations |                 | :              |     |              |     |              |     |
| A -     | Active        | P               | - Passive      | F   | - Aggregable | I   | - Individual |     |
| S -     | Short-timeout | L               | - Long-timeout | N   | - InSync     | O   | - OutofSync  |     |
51
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

C - Collecting D - Distributing
| X - State     | m/c expired        | E - Default | neighbor | state |     |
| ------------- | ------------------ | ----------- | -------- | ----- | --- |
| Actor details | of all interfaces: |             |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | -------------- | --------------- | --- | ----------- | ---------- |
|      | Name Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14  | lag1(mc) 206 1             | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------------------------- | ------------------------ | --- | ------- | ---- |
| 1/5/15  | lag2(mc)                   |                          |     |         | down |
| Partner | details of all interfaces: |                          |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr |     |
| ---- | -------------- | --------------- | --- | ----------- | --- |
|      | Name Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) 130 1 | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 |     |
| ------ | -------------- | ------------------------ | --- | ------- | --- |
| 1/5/15 | lag2(mc)       |                          |     |         |     |
DisplayinganLACPconfigurationafterloop-protectisenabledonthesecondaryVSXswitch:
switch#
show lacp interfaces
State abbreviations :
| A - Active        | P - Passive      | F - Aggregable | I - | Individual |     |
| ----------------- | ---------------- | -------------- | --- | ---------- | --- |
| S - Short-timeout | L - Long-timeout | N - InSync     | O - | OutofSync  |     |
C - Collecting D - Distributing
| X - State     | m/c expired        | E - Default | neighbor | state |     |
| ------------- | ------------------ | ----------- | -------- | ----- | --- |
| Actor details | of all interfaces: |             |          |       |     |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | -------------- | --------------- | --- | ----------- | ---------- |
|      | Name Id Pri    |                 |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/3/2   | lag1(mc) 1130 1            | ALFNCD f8:60:f0:06:49:00 |     | 65534 1 | up   |
| ------- | -------------------------- | ------------------------ | --- | ------- | ---- |
| 1/9/3   | lag2(mc)                   |                          |     |         | down |
| Partner | details of all interfaces: |                          |     |         |      |
------------------------------------------------------------------------------
| Intf | Aggr Port Port | State System-ID |     | System Aggr |     |
| ---- | -------------- | --------------- | --- | ----------- | --- |
|      | Name Id Pri    |                 |     | Pri Key     |     |
------------------------------------------------------------------------------
| 1/3/2 | lag1(mc) 131 1 | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 |     |
| ----- | -------------- | ------------------------ | --- | ------- | --- |
| 1/9/3 | lag2(mc)       |                          |     |         |     |
CommandHistory
| Release        |     | Modification |     |     |     |
| -------------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     | --           |     |     |     |
CommandInformation
LinkAggregation|52

| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
(#) executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
shutdown
shutdown
no shutdown
Description
SetseveryinterfaceintheLAGoperationallydown.
Thenoformofthiscommandsetseveryinterfaceoperationallyup.
Examples
SettingeveryinterfaceintheLAGtoshutdown:
| switch(config)#        | interface | lag 1    |
| ---------------------- | --------- | -------- |
| switch(config-lag-if)# |           | shutdown |
ResettingeveryinterfaceintheLAGtothedefault(up):
| switch(config)#        | interface | lag 1       |
| ---------------------- | --------- | ----------- |
| switch(config-lag-if)# |           | no shutdown |
CommandHistory
Release Modification
10.07orearlier --
CommandInformation
| Platforms | Commandcontext | Authority |
| --------- | -------------- | --------- |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| vlan trunk        | native             |     |
| ----------------- | ------------------ | --- |
| vlan trunk native | <VLAN-ID>          |     |
| no vlan trunk     | native [<VLAN-ID>] |     |
Description
AssignsanativeVLANIDtoaLAGinterface.
ThenoformofthiscommandremovesanativeVLANfromaLAGinterfaceandassignsVLANID1asits
nativeVLAN.
53
| AOS-CX10.08LinkAggregationGuide| | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | ----------------------------- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-ID> SpecifiesthenumberoftheVLANIDtoassign.TheVLANIDmust
exist.
MaximumnumberofVLANssupported:512(4100i)
MaximumnumberofVLANssupported:12(6000and6100)
MaximumnumberofVLANssupported:2048(6200)
MaximumnumberofVLANssupported:4096(6300,6400)
MaximumnumberofVLANssupported:4096(8320)
MaximumnumberofVLANssupported:4096(8325)
MaximumnumberofVLANssupported:4096(8360)
MaximumnumberofVLANssupported:4096(8400)
VLANIDrange:2to4094.
Usage
Bydefault,VLANID1isassignedastheLAGVLANIDforallLAGinterfaces.VLANscanonlybeassignedtoa
nonrouted(layer2)interfaceorLAGinterface.
OnlyoneVLANIDcanbeassignedasthenativeVLAN.FortheinterfacetoforwardthenativeVLANtraffic,
theinterfacehastobeallowedexplicitlybyenteringvlan trunk allowed <ID>wheretheIDisthenative
VLANID.Thissettingisalsoapplicabletothephysicalinterface.
Examples
ConfiguringaLayer2dynamicaggregationgroupwithnativeVLANID1assignedtoLAG1:
For6000,6100,and6200switchseries:
| switch(config)#        | interface | lag 1       |           |
| ---------------------- | --------- | ----------- | --------- |
| switch(config-lag-if)# |           | no shutdown |           |
| switch(config-lag-if)# |           | lacp mode   | active    |
| switch(config-lag-if)# |           | vlan trunk  | native 1  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 1 |
For6300,6400,8320,8325,8360,and8400switchseries:
| switch(config)#        | interface | lag 1       |           |
| ---------------------- | --------- | ----------- | --------- |
| switch(config-lag-if)# |           | no shutdown |           |
| switch(config-lag-if)# |           | no routing  |           |
| switch(config-lag-if)# |           | lacp mode   | active    |
| switch(config-lag-if)# |           | vlan trunk  | native 1  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 1 |
ConfiguringaLayer2dynamicaggregationgroupwithnativeVLANID20assignedtoLAG1:
For6000,6100,and6200switchseries:
| switch(config)#        | interface | lag 1       |            |
| ---------------------- | --------- | ----------- | ---------- |
| switch(config-lag-if)# |           | no shutdown |            |
| switch(config-lag-if)# |           | lacp mode   | active     |
| switch(config-lag-if)# |           | vlan trunk  | native 20  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 20 |
LinkAggregation|54

For6300,6400,8320,8325,8360,and8400switchseries:
| switch(config)#        | interface | lag         | 1          |
| ---------------------- | --------- | ----------- | ---------- |
| switch(config-lag-if)# |           | no shutdown |            |
| switch(config-lag-if)# |           | no routing  |            |
| switch(config-lag-if)# |           | lacp mode   | active     |
| switch(config-lag-if)# |           | vlan trunk  | native 20  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 20 |
RemovinganativeVLANfromLAG1:
| switch(config)#        | interface | lag     | 1            |
| ---------------------- | --------- | ------- | ------------ |
| switch(config-lag-if)# |           | no vlan | trunk native |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-lag-if |     | forthiscommand. |
| --- | ------------- | --- | --------------- |
55
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

Chapter 3

Smartlink

Smartlink

This chapter applies to the Aruba 6300, 6400 and 8360 Switch Series.

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

Benefits:

Failover is faster compared to STP. If the active link fails, a Smartlink group contains configuration
information that determines which port should be forwarding for a protected VLAN group.

Guidelines and limitations

n For faster convergence of routed traffic over Smartlink ports, ip neighbor-flood must be enabled on

respective SVI interfaces.

n Smartlink uses ERPS copp class for flush packets.

Limitations:

n VSX, ISL and MCLAGs cannot be included in Smartlink groups.

n Switches with both Smartlink and STP enabled exclude Smartlink ports from STP.

n On switches with both Smartlink and STP enabled, loops involving Smartlink and STP are not detected.

n On switches with both Smartlink and ERPS enabled, loops involving Smartlink and ERPS are not detected.

n ERPS and Smartlink cannot be enabled on the same port.

n Dynamic VLANs (MVRP) and Smartlink cannot be enabled on the same port.

n Loop Protect and Smartlink cannot be enabled on the same port.

n Multicast fast convergence is not supported.

n Uplink Failure Detection (UFD) is not supported.

n MIB and WebUI are not supported.

AOS-CX 10.08 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

56

n VLANs that include Smartlink ports must be included in the protected VLAN list of at least one Smartlink

group. If a VLAN includes Smartlink ports and is not included in the protected VLAN list, the VLAN-port

combination will not be managed by Smartlink or STP, resulting in an undefined port state for the VLAN,

which will cause a loop in the network.

n When using UDLD with Smartlinks, redundancy switchover is not hitless and will result in traffic loss.

Smartlink commands

Configuration commands

smartlink group

smartlink group <GROUP-ID>
no smartlink group <GROUP-ID>

Description

Creates a Smartlink group with specified ID.

The no form of this command removes the Smartlink group and all associated configurations for a specified
ID.

Parameter

<GROUP-ID>

Usage

Description

Specifies ID for the Smartlink group.

The maximum number of Smartlink groups is 24.

Examples

Configuring a Smartlink group:

switch(config)# smartlink group 2
switch(config-smartlink-2)#

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

config

Administrators or local user group members with execution rights
for this command.

smartlink recv-control-vlan

Smartlink | 57

| smartlink    | recv-control-vlan |     | <VID-LIST> |     |     |
| ------------ | ----------------- | --- | ---------- | --- | --- |
| no smartlink | recv-control-vlan |     | <VID-LIST> |     |     |
Description
ConfigurescontrolVLANstoreceiveflushmessages.
ThenoformofthiscommanddisablesVLANsfromreceivingflushmessages.
| Parameter  |     |     |     | Description      |     |
| ---------- | --- | --- | --- | ---------------- | --- |
| <VID-LIST> |     |     |     | SpecifiesVLANID. |     |
Usage
n ConfigurethiscommandonuplinkdeviceswhereMACflushisrequired.
n AflushmessageclearsstaleMAC andARP entriesenablingfasttrafficconvergence.
Examples
ConfiguringcontrolVLANtoreceiveflushmessages:
| switch(config)# |     | smartlink | recv-control-vlan |     | 2,3 |
| --------------- | --- | --------- | ----------------- | --- | --- |
CommandHistory
| Release        |     |     |     | Modification |     |
| -------------- | --- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |
| --------- | -------------- | --- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| Group | context | commands |     |     |     |
| ----- | ------- | -------- | --- | --- | --- |
description
| description | <DESC> |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- |
no description
Description
AddsdescriptiontoaSmartlinkgroup.
ThenoformofthiscommandremovesadescriptionfromaSmartlinkgroup.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<DESC> SpecifiesdescriptionforaSmartlinkgroup.1to64printableASCII
charactersareallowed.
58
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- |

Examples
AddingadescriptiontoaSmartlinkgroup:
switch(config)#
|                             | smartlink | group 3     |           |     |
| --------------------------- | --------- | ----------- | --------- | --- |
| switch(config-smartlink-3)# |           | Description | for group | 3   |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |
| --------- | -------------- | --- | --------- | --- |
Allplatforms config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
primary-port
| primary-port | <INTERFACE-NAME> |     |     |     |
| ------------ | ---------------- | --- | --- | --- |
no primary-port
Description
ConfiguresprimaryportforaSmartlinkgroup.
ThenoformofthiscommandremovesprimaryportfromaSmartlinkgroup.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE-NAME>
Specifiesinterfaceforprimaryport.
Examples
ConfiguringprimaryportforaSmartlinkgroup:
| switch(config)# | smartlink | group 3 |     |     |
| --------------- | --------- | ------- | --- | --- |
switch(config-smartlink-3)#
|     |     | primary-port | 1/1/1 |     |
| --- | --- | ------------ | ----- | --- |
CommandHistory
| Release        |     |     | Modification |     |
| -------------- | --- | --- | ------------ | --- |
| 10.07orearlier |     |     | --           |     |
CommandInformation
Smartlink|59

| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
smartlinkgroupsecondary-port
| secondary-port | <INTERFACE-NAME> |     |     |
| -------------- | ---------------- | --- | --- |
no secondary-port
Description
ConfiguressecondaryportforaSmartlinkgroup.
ThenoformofthiscommandremovessecondaryportfromaSmartlinkgroup.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<INTERFACE-NAME>
Specifiesinterfaceforsecondaryport.
Examples
ConfiguringsecondaryportforaSmartlinkgroup:
switch(config)#
|                             | smartlink | group 3        |       |
| --------------------------- | --------- | -------------- | ----- |
| switch(config-smartlink-3)# |           | secondary-port | 1/1/2 |
CommandHistory
| Release        |     | Modification |     |
| -------------- | --- | ------------ | --- |
| 10.07orearlier |     | --           |     |
CommandInformation
| Platforms | Commandcontext | Authority |     |
| --------- | -------------- | --------- | --- |
Allplatforms config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
control-vlan
| control-vlan    | <VLAN-ID> |     |     |
| --------------- | --------- | --- | --- |
| no control-vlan | <VLAN-ID> |     |     |
Description
ConfigurescontrolVLANinaSmartlinkgroup.
ThenoformofthiscommandremovescontrolVLANfromaSmartlinkgroup.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<VLAN-ID>
SpecifiesVLANIDforaSmartlinkgroup.
Usage
60
AOS-CX10.08LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

InaSmartlinkgroup,thecontrolVLAN isusedtosendflushmessages.
n
ControlVLANisconfiguredonthedeviceintendedtosendflushmessages.
n
EachSmartlinkgroupmustuseauniquecontrolVLAN.
n
n ControlVLANisprotectedintheSmartlinkgrouptoavoidloops.
Examples
ConfiguringcontrolVLAN inaSmartlinkgroup:
switch(config)#
|                             | smartlink | group 3      |     |
| --------------------------- | --------- | ------------ | --- |
| switch(config-smartlink-3)# |           | control-vlan | 10  |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
protected-vlans
| protected-vlans    | <VLAN-ID-LIST> |     |     |
| ------------------ | -------------- | --- | --- |
| no protected-vlans | <VLAN-ID-LIST> |     |     |
Description
SpecifiesVLANsprotectedbyaSmartlinkgroup.
ThenoformofthiscommandremovesVLANsprotectedbyaSmartlinkgroup.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-ID-LIST>
SpecifieslistofVLANIDs.Rangeis1to4094.
Examples
ConfiguringprotectedVLANsforaSmartlinkgroup.:
| switch(config)# | smartlink | group 3 |     |
| --------------- | --------- | ------- | --- |
switch(config-smartlink-3)#
|     |     | protected-vlans | 1, 10-50 |
| --- | --- | --------------- | -------- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
Smartlink|61

CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
preemption
preemption
no preemption
Description
ConfigurespreemptioninaSmartlinkgroup.
ThenoformofthiscommanddisablespreemptioninaSmartlinkgroup.
Usage
Ifpreemptionisenabled,arecoveredprimaryportpreemptstheactiveinterfaceaftertheconfigured
n
preemptiondelay.
n Ifpreemptionisdisabled,arecoveredprimaryportservesasabackupinterfaceanddoesnotforward
traffic.
Examples
ConfiguringpreemptioninaSmartlinkgroup:
| switch(config)#             | smartlink | group 3    |     |
| --------------------------- | --------- | ---------- | --- |
| switch(config-smartlink-3)# |           | preemption |     |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
preemption-delay
| preemption-delay | <SECONDS> |     |     |
| ---------------- | --------- | --- | --- |
no preemption-delay
Description
SpecifiespreemptiondelayforaSmartlinkgroup.
ThenoformofthiscommandremovespreviouslyconfiguredpreemptiondelayfromaSmartlinkgroupand
setsittothedefaultof1second.
62
| AOS-CX10.08LinkAggregationGuide| | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | ----------------------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<SECONDS> Specifiespreemptiondelayinseconds.Rangeis0to300seconds.
Usage
Whenpreemptionisenabled,arecoveredprimaryportalwayspreemptstheactiveinterfaceafterthe
configuredpreemptiondelay.
Examples
ConfiguringpreemptiondelayonaSmartlinkgroup:
| switch(config)#             | smartlink | group 3          |     |
| --------------------------- | --------- | ---------------- | --- |
| switch(config-smartlink-3)# |           | preemption       |     |
| switch(config-smartlink-3)# |           | preemption-delay | 10  |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
config-smartlink-<GROUP>
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| Display | commands |     |     |
| ------- | -------- | --- | --- |
show smartlinkgroup
| show smartlink | group <GROUP-ID> |     |     |
| -------------- | ---------------- | --- | --- |
Description
ShowsinformationforaspecificSmartlinkgroup.
| Parameter  |     |     | Description                |
| ---------- | --- | --- | -------------------------- |
| <GROUP-ID> |     |     | SpecifiesSmartlinkgroupID. |
Examples
ShowingSmartlinkgroupinformation:
| switch#   | show smartlink       | group 1 |     |
| --------- | -------------------- | ------- | --- |
| Smartlink | Group 1 Information: |         |     |
=============================
| Group description |       | : Uplink1 |     |
| ----------------- | ----- | --------- | --- |
| Protected         | VLANs | : 20-30   |     |
Smartlink|63

| Control    |      | VLAN  | : 10  |       |            |      |     |
| ---------- | ---- | ----- | ----- | ----- | ---------- | ---- | --- |
| Preemption |      |       | : ON  |       |            |      |     |
| Preemption |      | Delay | : 10  |       |            |      |     |
| Ports      | Role | State | Flush | Count | Last Flush | Time |     |
------ --------- ---------- ----------- -------------------------
| 1/1/1 | Primary   | Active | 2   |     | Sat Oct | 17 19:09:10 | 2020 |
| ----- | --------- | ------ | --- | --- | ------- | ----------- | ---- |
| 1/1/2 | Secondary | Backup | 0   |     |         |             |      |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
| Platforms |     | Commandcontext |     | Authority |     |     |     |
| --------- | --- | -------------- | --- | --------- | --- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
show smartlinkgroupall
| show | smartlink | group all |     |     |     |     |     |
| ---- | --------- | --------- | --- | --- | --- | --- | --- |
Description
ShowsinformationforallconfiguredSmartlinkgroups.
Examples
ShowinginformationforallconfiguredSmartlinkgroups:
switch#
|           |     | show smartlink     | group all |     |     |     |     |
| --------- | --- | ------------------ | --------- | --- | --- | --- | --- |
| Smartlink |     | Group Information: |           |     |     |     |     |
=============================
|     | Primary | Secondary | Active | Backup | Ctrl | Preemption | Preemption |
| --- | ------- | --------- | ------ | ------ | ---- | ---------- | ---------- |
| Grp | Port    | Port      | Port   | Port   | Vlan |            | Delay      |
---- ------- --------- ------ ------- --------- ---------- ----------
| 1   | 1/1/1 | 1/1/2 | 1/1/1 | 1/1/2 | 10  | OFF | 1   |
| --- | ----- | ----- | ----- | ----- | --- | --- | --- |
| 2   | 1/1/5 | 1/1/6 | 1/1/5 | 1/1/6 | 11  | OFF | 1   |
CommandHistory
| Release        |     |     |     | Modification |     |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |     |
CommandInformation
64
| AOS-CX10.08LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
show smartlinkgroupdetail
| show smartlink | group detail |     |     |     |     |
| -------------- | ------------ | --- | --- | --- | --- |
Description
ShowsdetailedinformationforallconfiguredSmartlinkgroups.
Examples
ShowingdetailedinformationforallconfiguredSmartlinkgroups:
| switch#   | show smartlink       | group detail |     |     |     |
| --------- | -------------------- | ------------ | --- | --- | --- |
| Smartlink | Group 1 Information: |              |     |     |     |
===============================
| Protected  | VLAN  | :     | 1-3         |            |      |
| ---------- | ----- | ----- | ----------- | ---------- | ---- |
| Control    | VLAN  | :     | 1           |            |      |
| Preemption |       | :     | OFF         |            |      |
| Preemption | Delay | :     | 1           |            |      |
| Ports      | Role  | State | Flush Count | Last Flush | Time |
-------- ------------ ------------ ------------ ------------------------
| 1/3/1     | Primary              | Backup | 0   |     |     |
| --------- | -------------------- | ------ | --- | --- | --- |
| 1/3/2     | Secondary            | Active | 0   |     |     |
| Smartlink | Group 2 Information: |        |     |     |     |
===============================
| Protected  | VLAN  | :     | 4-6         |            |      |
| ---------- | ----- | ----- | ----------- | ---------- | ---- |
| Control    | VLAN  | :     | 4           |            |      |
| Preemption |       | :     | OFF         |            |      |
| Preemption | Delay | :     | 1           |            |      |
| Ports      | Role  | State | Flush Count | Last Flush | Time |
-------- ------------ ------------ ------------ ------------------------
| 1/3/2 | Primary   | Active | 0   |     |     |
| ----- | --------- | ------ | --- | --- | --- |
| 1/3/1 | Secondary | Backup | 0   |     |     |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show smartlinkflush-statistics
| show smartlink | flush-statistics |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- |
Smartlink|65

Description
Showsinformationforreceivedflushmessages.
Usage
Thiscommandmustbeexecutedonanuplinkorpeerdeviceconfiguredwithrecv-control-vlan.
Examples
Showinginformationforreceivedflushmessages:
| switch#    | show smartlink | flush-statistics |     |     |     |
| ---------- | -------------- | ---------------- | --- | --- | --- |
| Last Flush | Packet Detail: |                  |     |     |     |
========================
| Flush Packets | Received         |              | : 2                      |             |      |
| ------------- | ---------------- | ------------ | ------------------------ | ----------- | ---- |
| Last Flush    | Packet Received  | On Interface | : 1/1/1                  |             |      |
| Last Flush    | Packet Received  | On           | : Sat Oct                | 17 19:09:10 | 2020 |
| Device        | Id Of Last Flush | Packet       | Received : 5065f3-127080 |             |      |
| Control       | VLAN Of Last     | Flush Packet | Received : 10            |             |      |
CommandHistory
| Release        |     |     | Modification |     |     |
| -------------- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     | Authority |     |     |
| --------- | -------------- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
clear smartlinkgroupstatistics
| clear smartlink | group [<GROUP-ID>] |     | statistics |     |     |
| --------------- | ------------------ | --- | ---------- | --- | --- |
Description
ClearsSmartlinkstatisticsforthespecifiedSmartlinkgrouporallSmartlinkgroups.
| Parameter  |     |     | Description              |     |     |
| ---------- | --- | --- | ------------------------ | --- | --- |
| <GROUP-ID> |     |     | SpecifiesSmartlinkgroup. |     |     |
Examples
ClearingSmartlinkstatisticsforaspecifiedSmartlinkgroup:
| switch# | clear smartlink | group 1 | statistics |     |     |
| ------- | --------------- | ------- | ---------- | --- | --- |
ClearingallSmartlinkstatisticsforallSmartlinkgroups:
66
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- |

| switch(config)# | clear | smartlink | group statistics |
| --------------- | ----- | --------- | ---------------- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
clear smartlinkflush-statistics
| clear smartlink | flush-statistics |     |     |
| --------------- | ---------------- | --- | --- |
Description
ClearsSmartlinkflushstatistics.
Usage
Thiscommandmustbeexecutedontheuplinkdeviceconfiguredwithrecv-control-vlan.
Examples
ClearingSmartlinkflushstatistics:
| switch# | clear smartlink | flush-statistics |     |
| ------- | --------------- | ---------------- | --- |
CommandHistory
| Release        |     |     | Modification |
| -------------- | --- | --- | ------------ |
| 10.07orearlier |     |     | --           |
CommandInformation
| Platforms | Commandcontext |     | Authority |
| --------- | -------------- | --- | --------- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show running-config
show running-config
Description
Showscurrentrunningconfiguration.
Smartlink|67

Examples
Showingcurrentlyrunningconfiguration:
switch#
configure terminal
| switch(config)#             | smartlink           |     | group            | 1   |         |       |
| --------------------------- | ------------------- | --- | ---------------- | --- | ------- | ----- |
| switch(config-smartlink-1)# |                     |     | description      |     | Uplink1 |       |
| switch(config-smartlink-1)# |                     |     | primary-port     |     | 1/1/1   |       |
| switch(config-smartlink-1)# |                     |     | secondary-port   |     |         | 1/1/2 |
| switch(config-smartlink-1)# |                     |     | control-vlan     |     | 10      |       |
| switch(config-smartlink-1)# |                     |     | protected-vlans  |     |         | 20-30 |
| switch(config-smartlink-1)# |                     |     | preemption       |     |         |       |
| switch(config-smartlink-1)# |                     |     | preemption-delay |     |         | 10    |
| switch(config)#             | smartlink           |     | group            | 2   |         |       |
| switch(config-smartlink-2)# |                     |     | primary-port     |     | 1/1/8   |       |
| switch(config-smartlink-2)# |                     |     | secondary-port   |     |         | 1/1/9 |
| switch(config-smartlink-2)# |                     |     | control-vlan     |     | 11      |       |
| switch(config-smartlink-2)# |                     |     | protected-vlans  |     |         | 20-30 |
| switch#                     | show running-config |     |                  |     |         |       |
| Current                     | configuration:      |     |                  |     |         |       |
!
!
!
| smart-link      | group 1 |     |     |     |     |     |
| --------------- | ------- | --- | --- | --- | --- | --- |
| primary-port    | 1/1/1   |     |     |     |     |     |
| secondary-port  | 1/1/2   |     |     |     |     |     |
| control-vlan    | 10      |     |     |     |     |     |
| protected-vlans | 20-30   |     |     |     |     |     |
preemption
| preemption-delay |     | 10  |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- |
exit
| smart-link      | group 2 |     |     |     |     |     |
| --------------- | ------- | --- | --- | --- | --- | --- |
| primary-port    | 1/1/8   |     |     |     |     |     |
| secondary-port  | 1/1/9   |     |     |     |     |     |
| control-vlan    | 11      |     |     |     |     |     |
| protected-vlans | 20-30   |     |     |     |     |     |
exit
CommandHistory
| Release        |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --------- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| Supportability | commands |     |     |     |     |     |
| -------------- | -------- | --- | --- | --- | --- | --- |
show capacitiessmartlink
| show capacities | smartlink | |   | show capacities-status |     |     | smartlink |
| --------------- | --------- | --- | ---------------------- | --- | --- | --------- |
Description
68
| AOS-CX10.08LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

ShowsSmartlinkcapacitiesorSmartlinkcapacitiesandstatus.
Examples
ShowingSmartlinkcapacities:
| switch#    | show capacities |        | smartlink |     |     |     |       |
| ---------- | --------------- | ------ | --------- | --- | --- | --- | ----- |
| System     | Capacities:     | Filter | SMARTLINK |     |     |     |       |
| Capacities | Name            |        |           |     |     |     | Value |
------------------------------------------------------------------------------------
Maximum number of SMARTLINK GROUPS configurable in a system 24
ShowingSmartlinkcapacitiesandstatus:
| switch#    | show capacities-status |         |        | smartlink |     |       |         |
| ---------- | ---------------------- | ------- | ------ | --------- | --- | ----- | ------- |
| System     | Capacities             | Status: | Filter | SMARTLINK |     |       |         |
| Capacities | Status                 | Name    |        |           |     | Value | Maximum |
------------------------------------------------------------------------------------
| Number | of SMARTLINK | GROUPS | currently |     | configured | 1   | 24  |
| ------ | ------------ | ------ | --------- | --- | ---------- | --- | --- |
CommandHistory
| Release        |     |     |     |     | Modification |     |     |
| -------------- | --- | --- | --- | --- | ------------ | --- | --- |
| 10.07orearlier |     |     |     |     | --           |     |     |
CommandInformation
| Platforms | Commandcontext |     |     |     | Authority |     |     |
| --------- | -------------- | --- | --- | --- | --------- | --- | --- |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
Smartlink|69

Support and Other Resources

Chapter 4

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

AOS-CX 10.08 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

70

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

Support and Other Resources | 71