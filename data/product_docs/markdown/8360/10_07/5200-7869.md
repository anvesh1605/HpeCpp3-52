|       | AOS-CX      |       | 10.07  | Link   |       |       |
| ----- | ----------- | ----- | ------ | ------ | ----- | ----- |
|       | Aggregation |       |        | Guide  |       |       |
| 6100, | 6200,       | 6300, | 6400,  | 8320,  | 8325, | 8360, |
|       |             | 8400  | Switch | Series |       |       |
PartNumber:5200-7869
Published:November2021
Edition:2

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
|                                                   | Settingtheaggregationstateofeachmemberport | 12  |
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
AOS-CX10.07LinkAggregationGuide| (6xxx,8xxxSwitchSeries)

|                          | description                    |           | 36  |
| ------------------------ | ------------------------------ | --------- | --- |
|                          | hash                           |           | 37  |
|                          | interfacelag                   |           | 37  |
|                          | ipaddress                      |           | 38  |
|                          | ipv6address                    |           | 39  |
|                          | lacphash                       |           | 40  |
|                          | lacpmode                       |           | 40  |
|                          | lacpport-id                    |           | 41  |
|                          | lacpport-priority              |           | 42  |
|                          | lacprate                       |           | 42  |
|                          | lacpsystem-priority            |           | 43  |
|                          | lag                            |           | 44  |
|                          | showinterface                  |           | 45  |
|                          | showlacpaggregates             |           | 46  |
|                          | showlacpconfiguration          |           | 47  |
|                          | showlacpinterfaces             |           | 48  |
|                          | shutdown                       |           | 51  |
|                          | vlantrunknative                |           | 51  |
| Smartlink                |                                |           | 53  |
| Guidelinesandlimitations |                                |           | 53  |
| Smartlinkcommands        |                                |           | 54  |
|                          | Configurationcommands          |           | 54  |
|                          | smartlinkgroup                 |           | 54  |
|                          | smartlinkrecv-control-vlan     |           | 54  |
|                          | Groupcontextcommands           |           | 55  |
|                          | description                    |           | 55  |
|                          | primary-port                   |           | 56  |
|                          | smartlinkgroupsecondary-port   |           | 56  |
|                          | control-vlan                   |           | 57  |
|                          | protected-vlans                |           | 57  |
|                          | preemption                     |           | 58  |
|                          | preemption-delay               |           | 58  |
|                          | Displaycommands                |           | 59  |
|                          | showsmartlinkgroup             |           | 59  |
|                          | showsmartlinkgroupall          |           | 60  |
|                          | showsmartlinkgroupdetail       |           | 60  |
|                          | showsmartlinkflush-statistics  |           | 61  |
|                          | clearsmartlinkgroupstatistics  |           | 62  |
|                          | clearsmartlinkflush-statistics |           | 62  |
|                          | showrunning-config             |           | 63  |
|                          | Supportabilitycommands         |           | 64  |
|                          | showcapacitiessmartlink        |           | 64  |
| Support                  | and Other                      | Resources | 65  |
| AccessingArubaSupport    |                                |           | 65  |
| AccessingUpdates         |                                |           | 65  |
|                          | ArubaSupportPortal             |           | 65  |
|                          | MyNetworking                   |           | 66  |
| WarrantyInformation      |                                |           | 66  |
| RegulatoryInformation    |                                |           | 66  |
| DocumentationFeedback    |                                |           | 66  |
Contents|4

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

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

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

5

Convention

Usage

Any of the following:
n <example-text>
n <example-text>
n example-text

n example-text

|

{ }

[ ]

… or

...

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

About this document | 6

switch(config-vlan-100)#

When referring to this context, this document uses the syntax:
switch(config-vlan-<VLAN-ID>)#

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 6100 Switch Series

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

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

7

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

Layer 3 aggregation groups are not supported on the 6100 and 6200 Switch Series.

The effective port rate of an aggregate interface equals the total rate of its member ports. Only full duplex
mode members are eligible for aggregation.

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

9

Link aggregation modes
An aggregation group operates in one of the following modes:

n Static LAG: In the static LAG mode of operation, Link failure is not detected as there is no keep alive

PDU communication between the devices. A misconfiguration on one side can cause much trouble and
be difficult to troubleshoot, because no signaling takes place between the two peers.

n Dynamic LAG or LACP: The local device and the peer device automatically maintain the aggregation

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

Link Aggregation | 10

TheoutputfromtheCLIcommandsshow lacp interfacesandshow lacp interfaces multi-chassis
displaythefollowinginterfacestates:
| Interface  | state | Description            |     |     |
| ---------- | ----- | ---------------------- | --- | --- |
| A - Active |       | AnactiveLACPinterface. |     |     |
C - Collecting
Dataframesarereceivedthroughtheaggregatelinkandsentonto
theintendeddestination.
D - Distributing Dataframesaretransmittedthroughtheaggregatelinktoreach
theintendeddestination.
| F - Aggregable |     | Thelinkcanbeusedaspartofanaggregate. |     |     |
| -------------- | --- | ------------------------------------ | --- | --- |
E - Default neighbor state Thelinkhasthedefaultstateoftheneighborswitch.
| I - Individual |     | Thelinkisusedasanindividuallink. |     |     |
| -------------- | --- | -------------------------------- | --- | --- |
L - Long-timeout Withthelongtimeout,anLACPDUissentevery30seconds.Ifno
responsecomesfromitspartnerafterthreeLACPDUsaresent(90
seconds),atimeouteventoccurs.TheLACPstatemachinethen
transitionstotheappropriatestatebasedonitscurrentstate.
N - InSync
Thephysicalportisconnectedtotheaggregateportthatwaslast
chosenbythelogicalelection.Thestatevariableselectedisstill
true.
O - OutofSync Thehardwaremightbeoutofsyncwiththemodifiedprotocol
information.Ifthehardwarealsohasastatusofcollecting,donot
transmitframesbecausetheywillbemisdelivered.
P - Passive
Theportparticipatesintheprotocol,aslongasithasanactive
partner.
S - Short-timeout Intheshorttimeoutconfiguration,anLACPDUissenteverysecond.
IfnoresponsecomesfromitspartnerafterthreeLACPDUsare
sent,atimeouteventoccurs.TheLACPstatemachinethen
transitionstotheappropriatestatebasedonitscurrentstate.
| X - State | m/c expired |     |     |     |
| --------- | ----------- | --- | --- | --- |
The"currentwhile"timerhasexpired.The"currentwhile"timer
thenrestartswiththeshort-timeoutenabled.
|            |                  | ThetermState |        | m/creferstoastatemachine. |
| ---------- | ---------------- | ------------ | ------ | ------------------------- |
| How static | link aggregation |              | groups | are built                 |
| Reference  | port selection   | process      |        |                           |
Whensettingtheaggregationstatesoftheportsinanaggregationgroup,thesystemautomaticallychooses
amemberportasthereferenceport.Aselectedportmusthavethesameoperationalkeyandattribute
configurationsasthereferenceport.
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 11

Thesystemchoosesareferenceportfromthememberportsintheupstate.Thefirstmemberinterface
whichisoperationallyupisselectedasreferenceport.
| Setting | the aggregation |     | state | of each member | port |     |
| ------- | --------------- | --- | ----- | -------------- | ---- | --- |
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
LinkAggregation|12

The system chooses a reference port from the member ports in up state. A selected port must have the
same operational key and attribute configurations as the reference port.

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

A port ID contains a port priority and a port number. The lower the port priority, the smaller the port
ID.

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

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

13

aggregation members, the port can still be added to the aggregation group. If dynamic LAG is enabled,
any port member with a speed different than other aggregation members is blocked or ineligible from
the same aggregation group. Any operational keys/attributes or configuration changes might affect the
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

o 6100, 6200, 6300, and 6400 switches: The interface goes to its default status of unshut.

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

Link Aggregation | 14

WhilecreatingtheLayer2aggregateinterface,thesystemautomaticallycreatesaLayer2static
aggregationgroupnumberedthesame.
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
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformation
| abouttheno | routingcommand. |     |     |
| ---------- | --------------- | --- | --- |
Onthe6100and6200SwitchSeries,routingisnotsupportedonphysicalinterfaces.
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
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 15

| switch(config-lag-if)# |     | interface | 1/1/1-1/1/4 |
| ---------------------- | --- | --------- | ----------- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformore
| informationabouttheinterface |     | <PORT-ID>command. |     |
| ---------------------------- | --- | ----------------- | --- |
b. AssignanIDtotheLAG:
| switch(config-if)# | lag | <ID> |     |
| ------------------ | --- | ---- | --- |
Forexample:
| switch(config-if-<1/1/1-1/1/4>)# |     |     | lag 100 |
| -------------------------------- | --- | --- | ------- |
c. Settheadministrativestateofthememberinterfacetoup:
| switch(config-if-<1/1/1-1/1/4>)# |     |     | no shutdown |
| -------------------------------- | --- | --- | ----------- |
6. Viewtheconfigurationbyenteringthefollowing:
For6100,6200,6300,and6400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     | show | running-config |
| -------------------------------- | --- | ---- | -------------- |
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
| switch(config-if-<1/1/1-1/1/4>)# |              | show        | lacp aggregates |
| -------------------------------- | ------------ | ----------- | --------------- |
| Aggregate name                   | : lag100     |             |                 |
| Interfaces                       | : 1/1/3      | 1/1/1 1/1/4 | 1/1/2           |
| Heartbeat rate                   | : N/A        |             |                 |
| Hash                             | : l3-src-dst |             |                 |
| Aggregate mode                   | : Off        |             |                 |
LinkAggregation|16

For8320,8325,8360,and8400switchseries:
|     | switch(config-if-<1/1/1-1/1/4>)# |     | show running-config |     |
| --- | -------------------------------- | --- | ------------------- | --- |
Current configuration:
!
vlan 1
|     | interface lag | 100 |     |     |
| --- | ------------- | --- | --- | --- |
no shutdown
no routing
|     | vlan trunk      | native 1 |     |     |
| --- | --------------- | -------- | --- | --- |
|     | vlan trunk      | allowed  | all |     |
|     | interface 1/1/1 |          |     |     |
no shutdown
lag 100
|     | interface 1/1/2 |     |     |     |
| --- | --------------- | --- | --- | --- |
no shutdown
lag 100
|     | interface 1/1/3 |     |     |     |
| --- | --------------- | --- | --- | --- |
no shutdown
lag 100
|     | interface 1/1/4 |     |     |     |
| --- | --------------- | --- | --- | --- |
no shutdown
lag 100
switch(config-if-<1/1/1-1/1/4>)#
|             |                |              | show lacp aggregates |       |
| ----------- | -------------- | ------------ | -------------------- | ----- |
|             | Aggregate name | : lag100     |                      |       |
|             | Interfaces     | : 1/1/3      | 1/1/1 1/1/4 1/1/2    |       |
|             | Heartbeat rate | : N/A        |                      |       |
|             | Hash           | : l3-src-dst |                      |       |
|             | Aggregate mode | : Off        |                      |       |
| Configuring | a Layer        | 2 dynamic    | aggregation          | group |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer2aggregateinterfaceandaccesstheLayer2aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |
| --- | --------------- | --------- | -------- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer2aggregateinterface,thesystemautomaticallycreatesaLayer2dynamic
aggregationgroupnumberedthesame.
2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
|     | switch(config-lag-if)# |     | no shutdown |     |
| --- | ---------------------- | --- | ----------- | --- |
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 17

Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecausethe
commandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofamember
interface,enterthecommandattheinterfacelevel.Forexample:
| switch(config)# | interface | 1/1/2 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)# no shutdown
3. Onthe8320,8325,8360,and8400,disableroutingbyentering:
| switch(config-lag-if)# | no routing |     |     |
| ---------------------- | ---------- | --- | --- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformation
abouttheno routingcommand.
Onthe6100and6200SwitchSeries,routingisnotsupportedonphysicalinterfaces.
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
|     | lag | <ID> |     |
| --- | --- | ---- | --- |
Forexample:
| switch(config-if-<1/1/1-1/1/4>)# |     |     | lag 20 |
| -------------------------------- | --- | --- | ------ |
c. Settheadministrativestateofthememberinterfacetoup:
| switch(config-if-<1/1/1-1/1/4>)# |     |     | no shutdown |
| -------------------------------- | --- | --- | ----------- |
8. Viewtheconfigurationbyentering:
For6100,6200,6300,and6400switchseries:
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
| switch(config-if-<1/1/1-1/1/4>)# |          | show        | lacp aggregates |
| -------------------------------- | -------- | ----------- | --------------- |
| Aggregate name                   | : lag100 |             |                 |
| Interfaces                       | : 1/1/3  | 1/1/1 1/1/4 | 1/1/2           |
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 19

|     | Heartbeat rate | : Fast       |     |     |
| --- | -------------- | ------------ | --- | --- |
|     | Hash           | : l3-src-dst |     |     |
|     | Aggregate mode | : Active     |     |     |
For8320,8325,8360,and8400switchseries:
|     | switch(config-if-<1/1/1-1/1/4>)# |     | show running-config |     |
| --- | -------------------------------- | --- | ------------------- | --- |
Current configuration:
!
vlan 1
|     | interface lag | 20  |     |     |
| --- | ------------- | --- | --- | --- |
no shutdown
no routing
|     | vlan trunk      | native 1 |     |     |
| --- | --------------- | -------- | --- | --- |
|     | vlan trunk      | allowed  | all |     |
|     | lacp mode       | active   |     |     |
|     | lacp rate       | fast     |     |     |
|     | interface 1/1/1 |          |     |     |
no shutdown
lag 20
|       | switch(config-if-<1/1/1-1/1/4>)# |              | show lacp         | aggregates |
| ----- | -------------------------------- | ------------ | ----------------- | ---------- |
|       | Aggregate name                   | : lag100     |                   |            |
|       | Interfaces                       | : 1/1/3      | 1/1/1 1/1/4 1/1/2 |            |
|       | Heartbeat rate                   | : Fast       |                   |            |
|       | Hash                             | : l3-src-dst |                   |            |
|       | Aggregate mode                   | : Active     |                   |            |
| Layer | 3 aggregation                    | groups       |                   |            |
Layer3aggregationgroupsaresupportedonallswitchseriesexcept6100and6200SwitchSeries.
| Configuring | a Layer | 3 static | aggregation | group |
| ----------- | ------- | -------- | ----------- | ----- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer3aggregateinterfaceandaccesstheLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |
| --- | --------------- | --------- | -------- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer3aggregateinterface,thesystemautomaticallycreatesaLayer3static
aggregationgroupnumberedthesame.
LinkAggregation|20

2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
n For6300and6400switchseries:
| switch(config-lag-if)# |     | no shutdown |     |
| ---------------------- | --- | ----------- | --- |
| switch(config-lag-if)# |     | routing     |     |
Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface | 1/1/2    |
| --- | ------------------ | --------- | -------- |
|     | switch(config-if)# | no        | shutdown |
|     | switch(config-if)# | routing   |          |
For8320,8325,8360,and8400switchseries:
n
| switch(config-lag-if)# |     | no shutdown |     |
| ---------------------- | --- | ----------- | --- |
Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface | 1/1/2    |
| --- | ------------------ | --------- | -------- |
|     | switch(config-if)# | no        | shutdown |
3. SettheIPaddressontheLAGinterfacebyentering:
| switch(config-lag-if)# |     | ip address | <IPV4-ADDR>/<MASK> |
| ---------------------- | --- | ---------- | ------------------ |
Forexample:
| switch(config-lag-if)# |     | ip address | 192.0.2.1/30 |
| ---------------------- | --- | ---------- | ------------ |
4. Usethefollowingstepstoaddamaximumof16interfacestotheLAG:
a. ToassignaninterfacetotheLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID> |
| ---------------------- | --- | --------- | --------- |
ToassignarangeofinterfacestoaLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID>-<PORT-ID> |
| ---------------------- | --- | --------- | ------------------- |
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 21

Forexample:
| switch(config-lag-if)# |     | interface | 1/1/1-1/1/4 |
| ---------------------- | --- | --------- | ----------- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformore
| informationabouttheinterface |     | <PORT-ID>command. |     |
| ---------------------------- | --- | ----------------- | --- |
b. AssignanIDtotheLAG:
| switch(config-if)# | lag | <ID> |     |
| ------------------ | --- | ---- | --- |
Forexample:
| switch(config-if-<1/1/1-1/1/4>)# |     |     | lag 100 |
| -------------------------------- | --- | --- | ------- |
c. Settheadministrativestateofthememberinterfacetoup:
| switch(config-if-<1/1/1-1/1/4>)# |     |     | no shutdown |
| -------------------------------- | --- | --- | ----------- |
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
| switch(config-if-<1/1/1-1/1/4>)# |              | show        | lacp aggregates |
| -------------------------------- | ------------ | ----------- | --------------- |
| Aggregate name                   | : lag100     |             |                 |
| Interfaces                       | : 1/1/3      | 1/1/1 1/1/4 | 1/1/2           |
| Heartbeat rate                   | : N/A        |             |                 |
| Hash                             | : l3-src-dst |             |                 |
| Aggregate mode                   | : Off        |             |                 |
LinkAggregation|22

For8320,8325,8360,and8400switchseries:
|     | switch(config-if-<1/1/1-1/1/4>)# |     | show running-config |     |
| --- | -------------------------------- | --- | ------------------- | --- |
Current configuration:
!
vlan 1
|     | interface lag | 100 |     |     |
| --- | ------------- | --- | --- | --- |
no shutdown
|     | ip address      | 192.0.2.1/30 |     |     |
| --- | --------------- | ------------ | --- | --- |
|     | interface 1/1/1 |              |     |     |
no shutdown
lag 100
|     | interface 1/1/2 |     |     |     |
| --- | --------------- | --- | --- | --- |
no shutdown
lag 100
|     | interface 1/1/3 |     |     |     |
| --- | --------------- | --- | --- | --- |
no shutdown
lag 100
|     | interface 1/1/4 |     |     |     |
| --- | --------------- | --- | --- | --- |
no shutdown
lag 100
|             | switch(config-if-<1/1/1-1/1/4>)# |              | show lacp         | aggregates |
| ----------- | -------------------------------- | ------------ | ----------------- | ---------- |
|             | Aggregate name                   | : lag100     |                   |            |
|             | Interfaces                       | : 1/1/3      | 1/1/1 1/1/4 1/1/2 |            |
|             | Heartbeat rate                   | : N/A        |                   |            |
|             | Hash                             | : l3-src-dst |                   |            |
|             | Aggregate mode                   | : Off        |                   |            |
| Configuring | a Layer                          | 3 dynamic    | aggregation       | group      |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer3aggregateinterfaceandaccesstheLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |
| --- | --------------- | --------- | -------- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer3aggregateinterface,thesystemautomaticallycreatesaLayer3dynamic
aggregationgroupnumberedthesame.
2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
For6300and6400switchseries:
n
|     | switch(config-lag-if)# |     | no shutdown |     |
| --- | ---------------------- | --- | ----------- | --- |
|     | switch(config-lag-if)# |     | routing     |     |
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 23

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
| switch(config-if-<1/1/1-1/1/4>)# |     | show running-config |
| -------------------------------- | --- | ------------------- |
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
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 25

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
| Removing a LAG                   |               |             |            |
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
n 6100, 6200, 6300, and6400 switches: TheinterfaceassociatedwiththeLAGbecomeslayer2ports
withthedefaultlayer2configurationsandadminstatusenabled.
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
| switch(config)#    | interface | 1/1/1          |     |     |
| ------------------ | --------- | -------------- | --- | --- |
| switch(config-if)# | no        | lag 100        |     |     |
| switch(config-if)# | show      | running-config |     |     |
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
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 27

AfterremovingaphysicalinterfacefromaLAG:
6100, 6200, 6300, and6400 switches:TheinterfaceassociatedwithLAGbecomeslayer2portswith
n
defaultlayer2configurationsandwithadminstatusofenabled
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
For6100,6200,6300,and6400switchseries:
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
| interface lag | 100 |     |     |     |
| ------------- | --- | --- | --- | --- |
no shutdown
no routing
| vlan trunk      | native  | 1   |     |     |
| --------------- | ------- | --- | --- | --- |
| vlan trunk      | allowed | all |     |     |
| interface 1/1/1 |         |     |     |     |
| interface 1/1/2 |         |     |     |     |
no shutdown
lag 100
switch(config-if)#
AfterremovingaphysicalinterfacefromaLAG,theinterfaceassociatedwiththeLAGbecomesL3
portswithdefaultL3configurationsandadministrativedown.Forexample,supposeinterface1/1/1
waspartofLAG3andyouhadadministrativelyenabledtheinterface.Ifyoulaterremoveinterface
1/1/1fromLAG3,theadministrativestatusautomaticallychangestodown.Ifyouwanttousethe
interfaceagain,youmustadministrativelyenableitagain.
On6100and6200SwitchSeries,afterremovingaphysicalinterfacefromaLAG,theinterface
associatedwiththeLAGbecomeslayer2portswithdefaultlayer2configurationsandadminstatus
enabled.
2. CreatetheLAGtowhichyouwanttoaddtheinterface:
| switch(config-if)# | interface |     | lag | 10  |
| ------------------ | --------- | --- | --- | --- |
Forexample:
For6100,6200,6300,and6400switchseries:
| switch(config-if)#     | interface |      | lag      | 10       |
| ---------------------- | --------- | ---- | -------- | -------- |
| switch(config-lag-if)# |           | no   | shutdown |          |
| switch(config-lag-if)# |           | vlan | trunk    | native 1 |
For8320,8325,8360,and8400switchseries:
| switch(config-if)#     | interface |      | lag      | 10       |
| ---------------------- | --------- | ---- | -------- | -------- |
| switch(config-lag-if)# |           | no   | shutdown |          |
| switch(config-lag-if)# |           | no   | routing  |          |
| switch(config-lag-if)# |           | vlan | trunk    | native 1 |
3. AddtheinterfacefromStep1tothenewlycreatedLAG:
| switch(config)#    | interface |     | 1/1/1 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 10  |       |     |
Forexample:
For6100,6200,6300,and6400switchseries:
| switch(config)#    | interface |     | 1/1/1 |     |
| ------------------ | --------- | --- | ----- | --- |
| switch(config-if)# | lag       | 10  |       |     |
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 29

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
For6100,6200,6300,and6400switchseries:
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
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 31

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
Layer3aggregationgroupsarenotsupportedonthe6100and6200SwitchSeries.
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
| Shutting | down | an aggregate |     | interface |
| -------- | ---- | ------------ | --- | --------- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
EntertheLayer3aggregateinterfaceviewbyentering:
| switch(config)# |     | interface | lag <ID> |     |
| --------------- | --- | --------- | -------- | --- |
Shutdowntheaggregateinterface:
| switch(config-lag-if)# |     |         | shutdown   |     |
| ---------------------- | --- | ------- | ---------- | --- |
| Supported              |     | hashing | algorithms |     |
n SourceMACanddestinationMAC
SourceIPanddestinationIP
n
Sourceportanddestinationport.
n
| LACP | configuration |         | settings |         |
| ---- | ------------- | ------- | -------- | ------- |
| Task |               | Command |          | Example |
SettingtheLACP lacp mode {active | switch(config-lag-if)# lacp mode active
| modetoactiveor |     | passive} |     |     |
| -------------- | --- | -------- | --- | --- |
passive.
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 33

| Task | Command | Example |     |     |
| ---- | ------- | ------- | --- | --- |
SettingtheLACP no lacp mode {active switch(config-lag-if)# no lacp mode active
modetooff.
| passive}
Settingthehashtype. For6100 and 8400 For6100 and 8400 Switch Series:
|     | Switch Series: | switch(config)# | lacp hash | l2-src-dst |
| --- | -------------- | --------------- | --------- | ---------- |
lacp hash [l2-src- For8320,8325,6200,6300,and 6400 Switch Series:
|     | dst | l3-src-dst | |                        |     |                 |
| --- | ------------------ | ---------------------- | --- | --------------- |
|     |                    | switch(config-lag-if)# |     | hash l2-src-dst |
l4-src-dst]
For8320,8325,6200,
6300,and 6400 Switch
Series:
|     | hash [l2-src-dst | |     |     |     |
| --- | ------------------ | --- | --- | --- |
l3-src-dst | l4-src-
dst]
SettingtheLACPrate lacp rate fast switch(config)# interface lag 1
tofast.
|     |     | switch(config-lag-if)# |     | lacp rate fast |
| --- | --- | ---------------------- | --- | -------------- |
SettingtheLACPrate lacp rate slow switch(config)# interface lag 1
| toslow.            |          | switch(config-lag-if)# |           | lacp rate slow |
| ------------------ | -------- | ---------------------- | --------- | -------------- |
| Applyingshutdownon | shutdown | switch(config)#        | interface | lag 1          |
theLAGport.
|     |     | switch(config-lag-if)# |     | shutdown |
| --- | --- | ---------------------- | --- | -------- |
Resettingevery no shutdown switch(config-lag-if)# no shutdown
interfaceintheLAG
tothedefault(up)
| Interface LACP | settings |         |     |     |
| -------------- | -------- | ------- | --- | --- |
| Task           | Command  | Example |     |     |
SettingtheLACPport lacp port-id <ID> switch(config-if)# lacp port-id 100
ID.
SettingtheLACPport no lacp port-id switch(config-if)# no lacp port-id
IDtothedefault.
SettingtheLACPport lacp port-priority switch(config-if)# lacp port-priority 100
| priority. | <PORT-PRIORITY> |     |     |     |
| --------- | --------------- | --- | --- | --- |
SettingtheLACPport no lacp port- switch(config-if)# no lacp port-priority
| prioritytothedefault | priority     |     |     |     |
| -------------------- | ------------ | --- | --- | --- |
| Configuration        | verification |     |     |     |
LinkAggregation|34

| Task | Command |     | Example |     |     |     |
| ---- | ------- | --- | ------- | --- | --- | --- |
show lacp
ViewingLACP
|             |               |     | switch#                      | show | lacp configuration  |                      |
| ----------- | ------------- | --- | ---------------------------- | ---- | ------------------- | -------------------- |
| global      | configuration |     |                              |      |                     |                      |
|             |               |     | System-id                    |      | : 70:72:cf:ef:fc:d9 |                      |
| information |               |     | System-priority              |      | : 65534             |                      |
|             |               |     | Hash                         |      | : l3-src-dst        |                      |
|             |               |     | Theoutputdisplayedfortheshow |      |                     | lacp configurationis |
fromthe8400seriesswitch.
|     | show lacp | aggregates |     |     |     |     |
| --- | --------- | ---------- | --- | --- | --- | --- |
ViewingLACP
|     |     |     | switch# | show | lacp aggregates |     |
| --- | --- | --- | ------- | ---- | --------------- | --- |
aggregate
|             |           |            | Aggregate-name        |      |     | : lag100       |
| ----------- | --------- | ---------- | --------------------- | ---- | --- | -------------- |
| information |           |            | Aggregated-interfaces |      |     | : 1/1/2        |
|             |           |            | Heartbeat             | rate |     | : N/A          |
|             |           |            | Hash                  |      |     | : l3-src-dst   |
|             |           |            | Aggregate             | mode |     | : off          |
|             |           |            | Aggregate-name        |      |     | : lag110       |
|             |           |            | Aggregated-interfaces |      |     | : 1/1/1, 1/1/3 |
|             |           |            | Heartbeat             | rate |     | : slow         |
|             |           |            | Hash                  |      |     | : l3-src-dst   |
|             |           |            | Aggregate             | mode |     | : active       |
| ViewingLACP | show lacp | aggregates |                       |      |     |                |
switch#
|     | lag100 |     |     | show | lacp aggregates | lag100 |
| --- | ------ | --- | --- | ---- | --------------- | ------ |
aggregate
|                 |           |            | Aggregate-name        |      |                 | : lag100     |
| --------------- | --------- | ---------- | --------------------- | ---- | --------------- | ------------ |
| informationfora |           |            | Aggregated-interfaces |      |                 | :            |
| LAG             |           |            | Heartbeat             | rate |                 | : N/A        |
|                 |           |            | Hash                  |      |                 | : l3-src-dst |
|                 |           |            | Aggregate             | mode |                 | : off        |
| ViewingLACP     | show lacp | interfaces |                       |      |                 |              |
|                 |           |            | switch#               | show | lacp interfaces |              |
interfacedetails
Theoutputistoowidetodisplayinacolumn.Thecommand
outputisprovidedintheCLItopicforthecommand.
| BFD reports | a LAG | as down | even | when | healthy | links are |
| ----------- | ----- | ------- | ---- | ---- | ------- | --------- |
still available
Symptom
BFDisnotsupportedonthe6100and6200SwitchSeries.
TheBidirectionalForwardDetection(BFD)featurereportsaLinkAggregation(LAG),asbeingdown,even
thoughtherearehealthyLAGlinksavailable.TheLAG,containingthedownedlink,willeventuallyrebalance
thetraffictoitsotherlinks.
Cause
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 35

This notification occurs when the minimum BFD control packet reception interval is set at a faster rate than
the Link Aggregation Control Protocol (LACP) rate and LAG rebalancing occurs. BFD assumes that the link is
down without realizing that the LAG is rebalancing the traffic load.

Action

Set the minimum BFD control packet reception interval to a slower rate than the LACP rate or set the LACP
rate to a faster rate than the minimum BFD control packet reception interval.

1. To find the current settings of the minimum BFD control packet reception interval, enter the show

running-config command.

The minimum BFD control packet reception interval setting is listed as bfd min-receive-interval in
the command output and the measurement is in ms.

2. To find the current rate of LACP, enter the show lacp aggregates command.

The LACP rate is listed as the Heatbeat rate in the command output.

3. To change the minimum BFD control packet reception interval, enter the bfd min-receive-interval

command.

4. To change the LACP rate, enter the lacp rate {fast | slow} command.

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

Link Aggregation | 36

vlan 1
| interface   | lag 10   |             |             |
| ----------- | -------- | ----------- | ----------- |
| description | This LAG | is used for | an example. |
| interface   | lag 60   |             |             |
switch(config-lag-if)#
hash
Supportedonlyonthe6200,6300,6400,8320,and8325SwitchSeries.
Syntax
| hash [l2-src-dst | | l3-src-dst | | l4-src-dst] |     |
| ---------------- | ------------ | ------------- | --- |
Description
Thiscommandcontrolstheselectionofaninterfaceinagroupofaggregateinterfaces.Thehashtypevalue
helpstransmitaframe.ThisconfigurationmustbedoneattheLAGinterfacelevel.
Commandcontext
config-lag-if
Parameters
l2-src-dst
Specifiestheload-balancingcalculationtoincludeonlyLayer2items,suchassourceanddestination
MACaddresses.
l3-src-dst
Specifiestheload-balancingcalculationtoincludeonlyLayer3items,suchassourceanddestinationIP
addresses.Defaultsetting.
l4-src-dst
Specifiestheload-balancingcalculationtoincludeonlyLayer4items,suchassourceanddestination
UDP/TCPports.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch(config-lag-if)# |     | hash l2-src-dst |     |
| ---------------------- | --- | --------------- | --- |
| interface lag          |     |                 |     |
Syntax
| interface lag    | <ID> |     |     |
| ---------------- | ---- | --- | --- |
| no interface lag | <ID> |     |     |
Description
CreatesaLinkAggregationGroup(LAG)interfacerepresentedbyanID.
ThenoformofthiscommanddeletesaLAGinterfacerepresentedbyanID.
Commandcontext
config
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 37

Parameters

<ID>

Specifies a LAG interface ID.

Authority

Administrators or local user group members with execution rights for this command.

Usage

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

Link Aggregation | 38

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

Authority

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

39

Administrators or local user group members with execution rights for this command.

Examples

Setting the IPv6 address on LAG interface 1 to 2001:0db8:85a3::8a2e:0370:7334 with a mask of 24 bits:

switch(config)# interface lag 1
switch(config-lag-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

Removing the IP address 2001:0db8:85a3::8a2e:0370:7334 with mask of 24 bits with a mask of 24 bits
from LAG interface 1:

switch(config)# interface lag 1
switch(config-lag-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24

lacp hash

Supported only on the 6100 and 8400 Switch Series.

Syntax

lacp hash [l2-src-dst | l3-src-dst | l4-src-dst]

Description

Controls the selection of an interface in a group of aggregate interfaces. The hash type value helps transmit
a frame. This configuration must be done at the global level.

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

Link Aggregation | 40

| lacp mode | {active      | | passive} |          |     |
| --------- | ------------ | ---------- | -------- | --- |
| no lacp   | mode {active | |          | passive} |     |
Description
SetsanLACPmodetoactiveorpassive.
ThenoformofthiscommandsetstheLACPmodetooff,returningtheLAGtoastaticmodeaggregation.
Commandcontext
config-lag-if
Parameters
active
SpecifiesthatthelocalswitchwilltransmitLACPDataUnits(LACPDUs)toattempttonegotiatewiththe
remotedevice.
passive
SpecifiesthatthelocalswitchwilllistenforLACPDUsfromtheremotedeviceforLACPnegotiation.
AmomentarytrafficdropoccursbecauseLACPpartnersreconvergewhenchangingthemodefromactiveto
passiveorfrompassivetoactive.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheLACPmodetoactive:
| switch(config)#        |     | interface | lag       | 1      |
| ---------------------- | --- | --------- | --------- | ------ |
| switch(config-lag-if)# |     |           | lacp mode | active |
SettingtheLACPmodetooff:
| switch(config)#        |     | interface | lag     | 1           |
| ---------------------- | --- | --------- | ------- | ----------- |
| switch(config-lag-if)# |     |           | no lacp | mode active |
lacp port-id
Syntax
| lacp port-id | <PORT-ID> |     |     |     |
| ------------ | --------- | --- | --- | --- |
| no lacp      | port-id   |     |     |     |
Description
SetstheLACPportIDvalueofthememberinterfaceoftheLAG.
ThenoformofthiscommandremovestheLACPportIDvaluefromtheinterface.
Commandcontext
config-if
Parameters
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 41

<PORT-ID>

Specifies a port ID value. Range: 1 to 65535.

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

Link Aggregation | 42

| lacp rate {fast | | slow} |     |
| --------------- | ------- | --- |
no lacp rate
Description
SetsanLACPheartbeatrequesttimetofastorslow.
ThenoformofthecommandsetsanLACPratetoslow.
Commandcontext
config-lag-if
Parameters
fast
Specifiestheheartbeatrequesttoeverysecond,andthetimeoutperiodisathree-consecutiveheartbeat
lossthatis3seconds.
slow
Specifiestheheartbeatrequesttoevery30seconds.Thetimeoutperiodisthree-consecutiveheartbeat
lossthatis90seconds.Defaultsetting.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheLACPheartbeatrequesttimetofast:
| switch(config)#        | interface | lag 1          |
| ---------------------- | --------- | -------------- |
| switch(config-lag-if)# |           | lacp rate fast |
ResettingtheLACPheartbeatrequesttimetothedefault,whichisslow:
| switch(config)#        | interface | lag 1        |
| ---------------------- | --------- | ------------ |
| switch(config-lag-if)# |           | no lacp rate |
AnotherwaytosettheLACPheartbeatrequesttimetothedefault,whichisslow:
| switch(config)#        | interface | lag 1          |
| ---------------------- | --------- | -------------- |
| switch(config-lag-if)# |           | lacp rate slow |
lacp system-priority
Syntax
| lacp system-priority | <SYSTEM-PRIORITY-VALUE> |     |
| -------------------- | ----------------------- | --- |
no lacp system-priority
Description
SetsaLinkAggregationControlProtocol(LACP)systempriority.
ThenoformofthiscommandsetsanLACPsystemprioritytothedefault,whichis65534.
Commandcontext
config
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 43

Parameters

<SYSTEM-PRIORITY-VALUE>

Specifies a system priority value. Range: 0 to 65535.

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

n All members of the LAG must have the same speed. If a member comes up late with a different speed, it
will not participate in the LAG/LACP. The hardware restriction is applied before adding an interface to
LAG. The member belongs to the card type that has the same maximum speed as the reference port card
type.

Link Aggregation | 44

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

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

45

|     | switch#               | show interface |              | lag100 |             |                   |     |       |
| --- | --------------------- | -------------- | ------------ | ------ | ----------- | ----------------- | --- | ----- |
|     | Aggregate             | lag100         | is           | up     |             |                   |     |       |
|     | Admin                 | state is       | up           |        |             |                   |     |       |
|     | Description           | :              |              |        |             |                   |     |       |
|     | MAC Address           |                |              |        | :           | 48:0f:cf:af:43:9c |     |       |
|     | Aggregated-interfaces |                |              |        | :           | 1/1/2             |     |       |
|     | Aggregation-key       |                |              |        | :           | 100               |     |       |
|     | Aggregate             | mode           |              |        | :           | active            |     |       |
|     | Speed                 |                |              |        | :           | 2000 Mb/s         |     |       |
|     | L3 Counters:          |                | Rx Disabled, |        | Tx Disabled |                   |     |       |
|     | qos trust             | none           |              |        |             |                   |     |       |
|     | VLAN Mode:            | access         |              |        |             |                   |     |       |
|     | Access                | VLAN:          | 1            |        |             |                   |     |       |
|     | Statistics            |                |              |        |             | RX                | TX  | Total |
------------- -------------------- -------------------- --------------------
|      | Packets   |            |     |     |     | 20   | 45   | 65   |
| ---- | --------- | ---------- | --- | --- | --- | ---- | ---- | ---- |
|      | Unicast   |            |     |     |     | 5    | 5    | 10   |
|      | Multicast |            |     |     |     | 5    | 15   | 20   |
|      | Broadcast |            |     |     |     | 10   | 25   | 35   |
|      | Bytes     |            |     |     |     | 5658 | 2584 | 8242 |
|      | Jumbos    |            |     |     |     | 0    | 0    | 0    |
|      | Dropped   |            |     |     |     | 0    | 0    | 0    |
|      | Filtered  |            |     |     |     | 0    | 0    | 0    |
|      | Pause     | Frames     |     |     |     | 0    | 0    | 0    |
|      | Errors    |            |     |     |     | 0    | 0    | 0    |
|      | CRC/FCS   |            |     |     |     | 0    | n/a  | 0    |
|      | Collision |            |     |     |     | n/a  | 0    | 0    |
|      | Runts     |            |     |     |     | 0    | n/a  | 0    |
|      | Giants    |            |     |     |     | 0    | n/a  | 0    |
| show | lacp      | aggregates |     |     |     |      |      |      |
Syntax
| show | lacp | aggregates | [<LAG-NAME>] |     |     | [vsx-peer] |     |     |
| ---- | ---- | ---------- | ------------ | --- | --- | ---------- | --- | --- |
Description
DisplaysallLACPaggregateinformationconfiguredforallLAGs,orforaspecificLAG.
Commandcontext
Operator(>)orManager(#)
Parameters
<LAG-NAME>
Optional:Specifiesalagname.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
LinkAggregation|46

DisplayingLACPaggregateinformationconfiguredforlag10:
| switch#               | show lacp | aggregates   | lag10 |     |
| --------------------- | --------- | ------------ | ----- | --- |
| Aggregate-name        |           | : lag10      |       |     |
| Aggregated-interfaces |           | : 1/1/1      | 1/1/2 |     |
| Heartbeat             | rate      | : slow       |       |     |
| Hash                  |           | : l3-src-dst |       |     |
| Aggregate             | mode      | : active     |       |     |
DisplayingLACPaggregates:
| switch#               | show lacp          | aggregates   |        |        |
| --------------------- | ------------------ | ------------ | ------ | ------ |
| Aggregate-name        |                    | : lag1       |        |        |
| Aggregated-interfaces |                    | : 1/1/27     | 1/1/28 | 1/1/29 |
| Heartbeat             | rate               | : slow       |        |        |
| Hash                  |                    | : l3-src-dst |        |        |
| Aggregate             | mode               | : active     |        |        |
| Aggregate-name        |                    | : lag2       |        |        |
| Aggregated-interfaces |                    | : 1/1/48     |        |        |
| Heartbeat             | rate               | : slow       |        |        |
| Hash                  |                    | : l2-src-dst |        |        |
| Aggregate             | mode               | : passive    |        |        |
| show                  | lacp configuration |              |        |        |
Syntax
| show lacp | configuration | [vsx-peer] |     |     |
| --------- | ------------- | ---------- | --- | --- |
Description
DisplaysglobalLACPconfiguration.
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
DisplayingglobalLACPconfiguration(outputisapplicablefor8400seriesswitches):
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 47

| switch#         | show | lacp configuration  |     |     |     |     |
| --------------- | ---- | ------------------- | --- | --- | --- | --- |
| System-id       |      | : 70:72:cf:ef:fc:d9 |     |     |     |     |
| System-priority |      | : 65534             |     |     |     |     |
| Hash            |      | :l3-src-dst         |     |     |     |     |
DisplayingglobalLACPconfiguration(outputisapplicablefor8320,6300,and6400seriesswitches):
| switch#         | show            | lacp configuration  |     |     |     |     |
| --------------- | --------------- | ------------------- | --- | --- | --- | --- |
| System-id       |                 | : 98:f2:b3:68:40:a0 |     |     |     |     |
| System-priority |                 | : 65534             |     |     |     |     |
| show            | lacp interfaces |                     |     |     |     |     |
Syntax
| show lacp | interfaces | [<IFNAME>] | [vsx-peer] |     |     |     |
| --------- | ---------- | ---------- | ---------- | --- | --- | --- |
Description
DisplaysanLACPconfigurationofthephysicalinterfaces,includingVSXs.Ifaninterfacenameispassedas
argument,itonlydisplaysanLACPconfigurationofaspecifiedinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<IFNAME>
Optional:Specifiesaninterfacename.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ThisexampledisplaysanLACPconfigurationofthephysicalinterfaces.Oneoftheinterfaceshasthelacp-
blockforwardingstate.IfaVSXswitchhasloopprotectenabledonaninterfaceandaloopoccurs,VSX
blockstheinterfacetostoptheloop.Theforwardingstateoftheblockedinterfaceissettolacp-block.
| switch# | show          | lacp interfaces    |                |          |            |     |
| ------- | ------------- | ------------------ | -------------- | -------- | ---------- | --- |
| State   | abbreviations | :                  |                |          |            |     |
| A -     | Active        | P - Passive        | F - Aggregable | I -      | Individual |     |
| S -     | Short-timeout | L - Long-timeout   | N - InSync     | O -      | OutofSync  |     |
| C -     | Collecting    | D - Distributing   |                |          |            |     |
| X -     | State m/c     | expired            | E - Default    | neighbor | state      |     |
| Actor   | details       | of all interfaces: |                |          |            |     |
------------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-id |     | System Aggr | Forwarding |
| ---- | ---- | --------- | --------------- | --- | ----------- | ---------- |
LinkAggregation|48

|     | name | id  | Pri |     |     |     |     | Pri | Key State |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --------- |
------------------------------------------------------------------------------------
| 1/1/1   | lag10   | 17  | 1               | ALFOE  | 70:72:cf:37:a3:5c |     |     | 20  | 10 lacp-block |
| ------- | ------- | --- | --------------- | ------ | ----------------- | --- | --- | --- | ------------- |
| 1/1/2   | lag128  | 69  | 1               | ALFNCD | 70:72:cf:37:a3:5c |     |     | 20  | 128 up        |
| 1/1/3   | lag128  | 14  | 1               | ALFNCD | 70:72:cf:37:a3:5c |     |     | 20  | 128 up        |
| 1/1/4   | lag128  |     |                 |        |                   |     |     |     | down          |
| 1/1/5   | lag20   |     |                 |        |                   |     |     |     | up            |
| Partner | details | of  | all interfaces: |        |                   |     |     |     |               |
------------------------------------------------------------------------------
| Intf | Aggr | Partner | Port |     | State | System-id |     | System   | Aggr |
| ---- | ---- | ------- | ---- | --- | ----- | --------- | --- | -------- | ---- |
|      | name | Port-id | Pri  |     |       |           |     | Priority | Key  |
------------------------------------------------------------------------------
| 1/1/1 | lag10  | 0   | 65534 |     | PLFOEX | 00:00:00:00:00:00 |     | 65534 | 0   |
| ----- | ------ | --- | ----- | --- | ------ | ----------------- | --- | ----- | --- |
| 1/1/2 | lag128 | 69  | 1     |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
| 1/1/3 | lag128 | 14  | 1     |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
1/1/4 lag128
1/1/5 lag20
DisplayingstaticLAG:
| switch# | show          | lacp interfaces |                |     |     |            |          |            |     |
| ------- | ------------- | --------------- | -------------- | --- | --- | ---------- | -------- | ---------- | --- |
| State   | abbreviations |                 | :              |     |     |            |          |            |     |
| A -     | Active        | P               | - Passive      |     | F - | Aggregable | I -      | Individual |     |
| S -     | Short-timeout | L               | - Long-timeout |     | N - | InSync     | O -      | OutofSync  |     |
| C -     | Collecting    | D               | - Distributing |     |     |            |          |            |     |
| X -     | State         | m/c expired     |                |     | E - | Default    | neighbor | state      |     |
| Actor   | details       | of all          | interfaces:    |     |     |            |          |            |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State | System-id |     |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---- | ----- | --------- | --- | --- | ----------- | ---------- |
|      | Name | Id   | Pri  |       |           |     |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag10   |     |                 |     |     |     |     |     | up  |
| ------- | ------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 1/1/2   | lag10   |     |                 |     |     |     |     |     | up  |
| Partner | details | of  | all interfaces: |     |     |     |     |     |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State | System-id |     |     | System Aggr |     |
| ---- | ---- | ---- | ---- | ----- | --------- | --- | --- | ----------- | --- |
|      | Name | Id   | Pri  |       |           |     |     | Pri Key     |     |
------------------------------------------------------------------------------
1/1/1 lag10
1/1/2 lag10
DisplayinganLACPconfigurationofthe1/1/1interface:
| switch#        | show          | lacp interfaces |                | 1/1/1 |     |            |          |            |     |
| -------------- | ------------- | --------------- | -------------- | ----- | --- | ---------- | -------- | ---------- | --- |
| State          | abbreviations |                 | :              |       |     |            |          |            |     |
| A -            | Active        | P               | - Passive      |       | F - | Aggregable | I -      | Individual |     |
| S -            | Short-timeout | L               | - Long-timeout |       | N - | InSync     | O -      | OutofSync  |     |
| C -            | Collecting    | D               | - Distributing |       |     |            |          |            |     |
| X -            | State         | m/c expired     |                |       | E - | Default    | neighbor | state      |     |
| Aggregate-name |               | : lag1          |                |       |     |            |          |            |     |
-------------------------------------------------
|     |     |     | Actor |     |     | Partner |     |     |     |
| --- | --- | --- | ----- | --- | --- | ------- | --- | --- | --- |
-------------------------------------------------
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 49

| Port-id         |     | | 28                |     | | 31                |     |     |
| --------------- | --- | ------------------- | --- | ------------------- | --- | --- |
| Port-priority   |     | | 1                 |     | | 1                 |     |     |
| Key             |     | | 1                 |     | | 1                 |     |     |
| State           |     | | ALFNCD            |     | | ALFNCD            |     |     |
| System-id       |     | | 98:f2:b3:68:40:a0 |     | | 98:f2:b3:68:60:a6 |     |     |
| System-priority |     | | 65534             |     | | 65534             |     |     |
DisplayinganLACPconfigurationafterloop-protectisenabledontheprimaryVSXswitch:
| switch#             | show lacp   | interfaces       |     |              |                |     |
| ------------------- | ----------- | ---------------- | --- | ------------ | -------------- | --- |
| State abbreviations |             | :                |     |              |                |     |
| A - Active          |             | P - Passive      | F   | - Aggregable | I - Individual |     |
| S - Short-timeout   |             | L - Long-timeout | N   | - InSync     | O - OutofSync  |     |
| C - Collecting      |             | D - Distributing |     |              |                |     |
| X - State           | m/c expired |                  | E   | - Default    | neighbor state |     |
| Actor details       | of          | all interfaces:  |     |              |                |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID | System Aggr | Forwarding |
| ---- | ---- | --------- | ----- | --------- | ----------- | ---------- |
|      | Name | Id Pri    |       |           | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/4/14  | lag1(mc) | 206 1              | ALFNCD | f8:60:f0:06:49:00 | 65534 1 | up   |
| ------- | -------- | ------------------ | ------ | ----------------- | ------- | ---- |
| 1/5/15  | lag2(mc) |                    |        |                   |         | down |
| Partner | details  | of all interfaces: |        |                   |         |      |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID | System Aggr |     |
| ---- | ---- | --------- | ----- | --------- | ----------- | --- |
|      | Name | Id Pri    |       |           | Pri Key     |     |
------------------------------------------------------------------------------
| 1/4/14 | lag1(mc) | 130 1 | ALFNCD | f8:60:f0:06:87:00 | 65534 1 |     |
| ------ | -------- | ----- | ------ | ----------------- | ------- | --- |
| 1/5/15 | lag2(mc) |       |        |                   |         |     |
DisplayinganLACPconfigurationafterloop-protectisenabledonthesecondaryVSXswitch:
| switch#             | show lacp   | interfaces       |     |              |                |     |
| ------------------- | ----------- | ---------------- | --- | ------------ | -------------- | --- |
| State abbreviations |             | :                |     |              |                |     |
| A - Active          |             | P - Passive      | F   | - Aggregable | I - Individual |     |
| S - Short-timeout   |             | L - Long-timeout | N   | - InSync     | O - OutofSync  |     |
| C - Collecting      |             | D - Distributing |     |              |                |     |
| X - State           | m/c expired |                  | E   | - Default    | neighbor state |     |
| Actor details       | of          | all interfaces:  |     |              |                |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID | System Aggr | Forwarding |
| ---- | ---- | --------- | ----- | --------- | ----------- | ---------- |
|      | Name | Id Pri    |       |           | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/3/2   | lag1(mc) | 1130 1             | ALFNCD | f8:60:f0:06:49:00 | 65534 1 | up   |
| ------- | -------- | ------------------ | ------ | ----------------- | ------- | ---- |
| 1/9/3   | lag2(mc) |                    |        |                   |         | down |
| Partner | details  | of all interfaces: |        |                   |         |      |
------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State | System-ID | System Aggr |     |
| ---- | ---- | --------- | ----- | --------- | ----------- | --- |
|      | Name | Id Pri    |       |           | Pri Key     |     |
------------------------------------------------------------------------------
LinkAggregation|50

| 1/3/2 lag1(mc) | 131 | 1 ALFNCD f8:60:f0:06:87:00 | 65534 1 |
| -------------- | --- | -------------------------- | ------- |
1/9/3 lag2(mc)
shutdown
Syntax
shutdown
no shutdown
Description
SetseveryinterfaceintheLAGoperationallydown.
Thenoformofthiscommandsetseveryinterfaceoperationallyup.
Commandcontext
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingeveryinterfaceintheLAGtoshutdown:
| switch(config)#        | interface | lag 1    |     |
| ---------------------- | --------- | -------- | --- |
| switch(config-lag-if)# |           | shutdown |     |
ResettingeveryinterfaceintheLAGtothedefault(up):
| switch(config)#        | interface | lag 1       |     |
| ---------------------- | --------- | ----------- | --- |
| switch(config-lag-if)# |           | no shutdown |     |
| vlan trunk native      |           |             |     |
Syntax
| vlan trunk native    | <VLAN-ID>   |     |     |
| -------------------- | ----------- | --- | --- |
| no vlan trunk native | [<VLAN-ID>] |     |     |
Description
AssignsanativeVLANIDtoaLAGinterface.
ThenoformofthiscommandremovesanativeVLANfromaLAGinterfaceandassignsVLANID1asits
nativeVLAN.
Commandcontext
config-if
config-lag-if
Parameters
<VLAN-ID>
SpecifiesthenumberoftheVLANIDtoassign.TheVLANIDmustexist.
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 51

MaximumnumberofVLANssupported:512(6100);2048(6200);4096(6300,6400,8320,8325,8360,
8400).
VLANIDrange:2to4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
Bydefault,VLANID1isassignedastheLAGVLANIDforallLAGinterfaces.VLANscanonlybeassignedtoa
nonrouted(layer2)interfaceorLAGinterface.
OnlyoneVLANIDcanbeassignedasthenativeVLAN.FortheinterfacetoforwardthenativeVLANtraffic,
theinterfacehastobeallowedexplicitlybyenteringvlan trunk allowed <ID>wheretheIDisthenative
VLANID.Thissettingisalsoapplicabletothephysicalinterface.
Examples
ConfiguringaLayer2dynamicaggregationgroupwithnativeVLANID1assignedtoLAG1:
For6100and6200switchseries:
| switch(config)#        | interface | lag 1       |           |
| ---------------------- | --------- | ----------- | --------- |
| switch(config-lag-if)# |           | no shutdown |           |
| switch(config-lag-if)# |           | lacp mode   | active    |
| switch(config-lag-if)# |           | vlan trunk  | native 1  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 1 |
For6300,6400,8320,8325,8360,and8400switchseries:
switch(config)#
|                        | interface | lag 1       |           |
| ---------------------- | --------- | ----------- | --------- |
| switch(config-lag-if)# |           | no shutdown |           |
| switch(config-lag-if)# |           | no routing  |           |
| switch(config-lag-if)# |           | lacp mode   | active    |
| switch(config-lag-if)# |           | vlan trunk  | native 1  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 1 |
ConfiguringaLayer2dynamicaggregationgroupwithnativeVLANID20assignedtoLAG1:
For6100and6200switchseries:
| switch(config)#        | interface | lag 1       |            |
| ---------------------- | --------- | ----------- | ---------- |
| switch(config-lag-if)# |           | no shutdown |            |
| switch(config-lag-if)# |           | lacp mode   | active     |
| switch(config-lag-if)# |           | vlan trunk  | native 20  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 20 |
For6300,6400,8320,8325,8360,and8400switchseries:
| switch(config)#        | interface | lag 1       |     |
| ---------------------- | --------- | ----------- | --- |
| switch(config-lag-if)# |           | no shutdown |     |
switch(config-lag-if)#
|                        |     | no routing |            |
| ---------------------- | --- | ---------- | ---------- |
| switch(config-lag-if)# |     | lacp mode  | active     |
| switch(config-lag-if)# |     | vlan trunk | native 20  |
| switch(config-lag-if)# |     | vlan trunk | allowed 20 |
RemovinganativeVLANfromLAG1:
LinkAggregation|52

switch(config)# interface lag 1
switch(config-lag-if)# no vlan trunk native

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

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

53

VLANsthatincludeSmartlinkportsmustbeincludedintheprotectedVLANlistofatleastoneSmartlink
n
group.IfaVLANincludesSmartlinkportsandisnotincludedintheprotectedVLANlist,theVLAN-port
combinationwillnotbemanagedbySmartlinkorSTP,resultinginanundefinedportstatefortheVLAN,
whichwillcausealoopinthenetwork.
n WhenusingUDLDwithSmartlinks,redundancyswitchoverisnothitlessandwillresultintrafficloss.
| Smartlink     |     | commands |     |
| ------------- | --- | -------- | --- |
| Configuration |     | commands |     |
smartlinkgroup
Syntax
| smartlink    | group | <GROUP-ID> |     |
| ------------ | ----- | ---------- | --- |
| no smartlink | group | <GROUP-ID> |     |
Description
CreatesaSmartlinkgroupwithspecifiedID.
ThenoformofthiscommandremovestheSmartlinkgroupandallassociatedconfigurationsforaspecified
ID.
Commandcontext
config
Parameters
<GROUP-ID>
SpecifiesIDfortheSmartlinkgroup.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
ThemaximumnumberofSmartlinkgroupsis24.
Examples
ConfiguringaSmartlinkgroup:
| switch(config)# |     | smartlink | group 2 |
| --------------- | --- | --------- | ------- |
switch(config-smartlink-2)#
smartlinkrecv-control-vlan
Syntax
| smartlink    | recv-control-vlan |     | <VID-LIST> |
| ------------ | ----------------- | --- | ---------- |
| no smartlink | recv-control-vlan |     | <VID-LIST> |
Description
Smartlink|54

Configures control VLANs to receive flush messages.

The no form of this command disables VLANs from receiving flush messages.

Command context

config

Parameters

<VID-LIST>

Specifies VLAN ID.

Authority

Administrators or local user group members with execution rights for this command.

Usage

n Configure this command on uplink devices where MAC flush is required.

n A flush message clears stale MAC and ARP entries enabling fast traffic convergence.

Examples

Configuring control VLAN to receive flush messages:

switch(config)# smartlink recv-control-vlan 2,3

Group context commands

description

Syntax

description <DESC>
no description

Description

Adds description to a Smartlink group.

The no form of this command removes a description from a Smartlink group.

Command context

config-smartlink-<GROUP>

Parameters

<DESC>

Specifies description for a Smartlink group. 1 to 64 printable ASCII characters are allowed.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Adding a description to a Smartlink group:

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

55

switch(config)# smartlink group 3
switch(config-smartlink-3)# Description for group 3

primary-port

Syntax

primary-port <INTERFACE-NAME>
no primary-port

Description

Configures primary port for a Smartlink group.

The no form of this command removes primary port from a Smartlink group.

Command context

config-smartlink-<GROUP>

Parameters

<INTERFACE-NAME>

Specifies interface for primary port.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring primary port for a Smartlink group:

switch(config)# smartlink group 3
switch(config-smartlink-3)# primary-port 1/1/1

smartlink group secondary-port

Syntax

secondary-port <INTERFACE-NAME>
no secondary-port

Description

Configures secondary port for a Smartlink group.

The no form of this command removes secondary port from a Smartlink group.

Command context

config-smartlink-<GROUP>

Parameters

<INTERFACE-NAME>

Specifies interface for secondary port.

Authority

Administrators or local user group members with execution rights for this command.

Smartlink | 56

Examples
ConfiguringsecondaryportforaSmartlinkgroup:
switch(config)#
|                             | smartlink | group 3        |       |
| --------------------------- | --------- | -------------- | ----- |
| switch(config-smartlink-3)# |           | secondary-port | 1/1/2 |
control-vlan
Syntax
| control-vlan <VLAN-ID> |           |     |     |
| ---------------------- | --------- | --- | --- |
| no control-vlan        | <VLAN-ID> |     |     |
Description
ConfigurescontrolVLANinaSmartlinkgroup.
ThenoformofthiscommandremovescontrolVLANfromaSmartlinkgroup.
Commandcontext
config-smartlink-<GROUP>
Parameters
<VLAN-ID>
SpecifiesVLANIDforaSmartlinkgroup.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
n InaSmartlinkgroup,thecontrolVLAN isusedtosendflushmessages.
n ControlVLANisconfiguredonthedeviceintendedtosendflushmessages.
n EachSmartlinkgroupmustuseauniquecontrolVLAN.
n ControlVLANisprotectedintheSmartlinkgrouptoavoidloops.
Examples
ConfiguringcontrolVLAN inaSmartlinkgroup:
| switch(config)#             | smartlink | group 3      |     |
| --------------------------- | --------- | ------------ | --- |
| switch(config-smartlink-3)# |           | control-vlan | 10  |
protected-vlans
Syntax
| protected-vlans    | <VLAN-ID-LIST> |     |     |
| ------------------ | -------------- | --- | --- |
| no protected-vlans | <VLAN-ID-LIST> |     |     |
Description
SpecifiesVLANsprotectedbyaSmartlinkgroup.
ThenoformofthiscommandremovesVLANsprotectedbyaSmartlinkgroup.
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 57

Command context

config-smartlink-<GROUP>

Parameters

<VLAN-ID-LIST>

Specifies list of VLAN IDs. Range is 1 to 4094.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Configuring protected VLANs for a Smartlink group.:

switch(config)# smartlink group 3
switch(config-smartlink-3)# protected-vlans 1, 10-50

preemption

Syntax

preemption
no preemption

Description

Configures preemption in a Smartlink group.

The no form of this command disables preemption in a Smartlink group.

Command context

config-smartlink-<GROUP>

Authority

Administrators or local user group members with execution rights for this command.

Usage

n If preemption is enabled, a recovered primary port preempts the active interface after the configured

preemption delay.

n If preemption is disabled, a recovered primary port serves as a backup interface and does not forward

traffic.

Examples

Configuring preemption in a Smartlink group:

switch(config)# smartlink group 3
switch(config-smartlink-3)# preemption

preemption-delay

Syntax

preemption-delay <SECONDS>

Smartlink | 58

no preemption-delay

Description

Specifies preemption delay for a Smartlink group.

The no form of this command removes previously configured preemption delay from a Smartlink group and
sets it to the default of 1 second.

Command context

config-smartlink-<GROUP>

Parameters

<SECONDS>

Specifies preemption delay in seconds. Range is 0 to 300 seconds.

Authority

Administrators or local user group members with execution rights for this command.

Usage

When preemption is enabled, a recovered primary port always preempts the active interface after the
configured preemption delay.

Examples

Configuring preemption delay on a Smartlink group:

switch(config)# smartlink group 3
switch(config-smartlink-3)# preemption
switch(config-smartlink-3)# preemption-delay 10

Display commands

show smartlink group

Syntax

show smartlink group <GROUP-ID>

Description

Shows information for a specific Smartlink group.

Command context

Operator (>) or Manager (#)

Parameters

<GROUP-ID>

Specifies Smartlink group ID.

Authority

Operators or Administrators or local user group members with execution rights for this command.
Operators can execute this command from the operator context (>) only.

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

59

Examples
ShowingSmartlinkgroupinformation:
switch#
|           | show smartlink |                | group 1 |     |     |     |
| --------- | -------------- | -------------- | ------- | --- | --- | --- |
| Smartlink | Group          | 1 Information: |         |     |     |     |
=============================
| Group description |       |       | : Uplink1   |            |      |     |
| ----------------- | ----- | ----- | ----------- | ---------- | ---- | --- |
| Protected         | VLANs |       | : 20-30     |            |      |     |
| Control           | VLAN  |       | : 10        |            |      |     |
| Preemption        |       |       | : ON        |            |      |     |
| Preemption        | Delay |       | : 10        |            |      |     |
| Ports             | Role  | State | Flush Count | Last Flush | Time |     |
------ --------- ---------- ----------- -------------------------
| 1/1/1 | Primary   | Active | 2   | Sat Oct | 17 19:09:10 | 2020 |
| ----- | --------- | ------ | --- | ------- | ----------- | ---- |
| 1/1/2 | Secondary | Backup | 0   |         |             |      |
show smartlinkgroupall
Syntax
| show smartlink | group | all |     |     |     |     |
| -------------- | ----- | --- | --- | --- | --- | --- |
Description
ShowsinformationforallconfiguredSmartlinkgroups.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowinginformationforallconfiguredSmartlinkgroups:
| switch#   | show smartlink |              | group all |     |     |     |
| --------- | -------------- | ------------ | --------- | --- | --- | --- |
| Smartlink | Group          | Information: |           |     |     |     |
=============================
| Primary  | Secondary |     | Active Backup | Ctrl | Preemption | Preemption |
| -------- | --------- | --- | ------------- | ---- | ---------- | ---------- |
| Grp Port | Port      |     | Port Port     | Vlan |            | Delay      |
---- ------- --------- ------ ------- --------- ---------- ----------
| 1 1/1/1 | 1/1/2 |     | 1/1/1 1/1/2 | 10  | OFF | 1   |
| ------- | ----- | --- | ----------- | --- | --- | --- |
| 2 1/1/5 | 1/1/6 |     | 1/1/5 1/1/6 | 11  | OFF | 1   |
show smartlinkgroupdetail
Syntax
| show smartlink | group | detail |     |     |     |     |
| -------------- | ----- | ------ | --- | --- | --- | --- |
Description
ShowsdetailedinformationforallconfiguredSmartlinkgroups.
Commandcontext
Smartlink|60

Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
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
show smartlinkflush-statistics
Syntax
| show smartlink | flush-statistics |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- |
Description
Showsinformationforreceivedflushmessages.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Thiscommandmustbeexecutedonanuplinkorpeerdeviceconfiguredwithrecv-control-vlan.
Examples
Showinginformationforreceivedflushmessages:
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 61

| switch#    | show smartlink | flush-statistics |     |     |     |
| ---------- | -------------- | ---------------- | --- | --- | --- |
| Last Flush | Packet Detail: |                  |     |     |     |
========================
| Flush Packets | Received         |                       | : 2             |             |      |
| ------------- | ---------------- | --------------------- | --------------- | ----------- | ---- |
| Last Flush    | Packet Received  | On Interface          | : 1/1/1         |             |      |
| Last Flush    | Packet Received  | On                    | : Sat Oct       | 17 19:09:10 | 2020 |
| Device        | Id Of Last Flush | Packet Received       | : 5065f3-127080 |             |      |
| Control       | VLAN Of Last     | Flush Packet Received | : 10            |             |      |
clear smartlinkgroupstatistics
Syntax
| clear smartlink | group [<GROUP-ID>] | statistics |     |     |     |
| --------------- | ------------------ | ---------- | --- | --- | --- |
Description
ClearsSmartlinkstatisticsforthespecifiedSmartlinkgrouporallSmartlinkgroups.
Commandcontext
Operator(>)orManager(#)
Parameters
<GROUP-ID>
SpecifiesSmartlinkgroup.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ClearingSmartlinkstatisticsforaspecifiedSmartlinkgroup:
| switch# | clear smartlink | group 1 statistics |     |     |     |
| ------- | --------------- | ------------------ | --- | --- | --- |
ClearingallSmartlinkstatisticsforallSmartlinkgroups:
| switch(config)# | clear | smartlink group statistics |     |     |     |
| --------------- | ----- | -------------------------- | --- | --- | --- |
clear smartlinkflush-statistics
Syntax
| clear smartlink | flush-statistics |     |     |     |     |
| --------------- | ---------------- | --- | --- | --- | --- |
Description
ClearsSmartlinkflushstatistics.
Commandcontext
Operator(>)orManager(#)
Authority
Smartlink|62

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Usage
Thiscommandmustbeexecutedontheuplinkdeviceconfiguredwithrecv-control-vlan.
Examples
ClearingSmartlinkflushstatistics:
| switch# clear | smartlink | flush-statistics |     |
| ------------- | --------- | ---------------- | --- |
show running-config
Syntax
show running-config
Description
Showscurrentrunningconfiguration.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Showingcurrentlyrunningconfiguration:
| switch# configure           | terminal       |                  |         |
| --------------------------- | -------------- | ---------------- | ------- |
| switch(config)#             | smartlink      | group 1          |         |
| switch(config-smartlink-1)# |                | description      | Uplink1 |
| switch(config-smartlink-1)# |                | primary-port     | 1/1/1   |
| switch(config-smartlink-1)# |                | secondary-port   | 1/1/2   |
| switch(config-smartlink-1)# |                | control-vlan     | 10      |
| switch(config-smartlink-1)# |                | protected-vlans  | 20-30   |
| switch(config-smartlink-1)# |                | preemption       |         |
| switch(config-smartlink-1)# |                | preemption-delay | 10      |
| switch(config)#             | smartlink      | group 2          |         |
| switch(config-smartlink-2)# |                | primary-port     | 1/1/8   |
| switch(config-smartlink-2)# |                | secondary-port   | 1/1/9   |
| switch(config-smartlink-2)# |                | control-vlan     | 11      |
| switch(config-smartlink-2)# |                | protected-vlans  | 20-30   |
| switch# show                | running-config |                  |         |
| Current configuration:      |                |                  |         |
!
!
!
| smart-link      | group 1 |     |     |
| --------------- | ------- | --- | --- |
| primary-port    | 1/1/1   |     |     |
| secondary-port  | 1/1/2   |     |     |
| control-vlan    | 10      |     |     |
| protected-vlans | 20-30   |     |     |
AOS-CX10.07LinkAggregationGuide|(6xxx,8xxxSwitchSeries) 63

preemption
| preemption-delay |     | 10  |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
exit
| smart-link      | group | 2     |     |     |     |     |     |     |
| --------------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
| primary-port    |       | 1/1/8 |     |     |     |     |     |     |
| secondary-port  |       | 1/1/9 |     |     |     |     |     |     |
| control-vlan    |       | 11    |     |     |     |     |     |     |
| protected-vlans |       | 20-30 |     |     |     |     |     |     |
exit
| Supportability |     | commands |     |     |     |     |     |     |
| -------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
show capacitiessmartlink
Syntax
| show capacities | smartlink |     | | show | capacities-status |     | smartlink |     |     |
| --------------- | --------- | --- | ------ | ----------------- | --- | --------- | --- | --- |
Description
ShowsSmartlinkcapacitiesorSmartlinkcapacitiesandstatus.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingSmartlinkcapacities:
| switch#    | show capacities |        | smartlink |     |     |     |     |       |
| ---------- | --------------- | ------ | --------- | --- | --- | --- | --- | ----- |
| System     | Capacities:     | Filter | SMARTLINK |     |     |     |     |       |
| Capacities | Name            |        |           |     |     |     |     | Value |
------------------------------------------------------------------------------------
Maximum number of SMARTLINK GROUPS configurable in a system 24
ShowingSmartlinkcapacitiesandstatus:
| switch#    | show capacities-status |         |        | smartlink |     |     |       |         |
| ---------- | ---------------------- | ------- | ------ | --------- | --- | --- | ----- | ------- |
| System     | Capacities             | Status: | Filter | SMARTLINK |     |     |       |         |
| Capacities | Status                 | Name    |        |           |     |     | Value | Maximum |
------------------------------------------------------------------------------------
| Number | of SMARTLINK | GROUPS | currently |     | configured |     | 1   | 24  |
| ------ | ------------ | ------ | --------- | --- | ---------- | --- | --- | --- |
Smartlink|64

Support and Other Resources

Chapter 3

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

AOS-CX 10.07 Link Aggregation Guide | (6xxx, 8xxx Switch Series)

65

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

Support and Other Resources | 66