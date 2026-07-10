|        | AOS-CX      |       | 10.09 |        | Link   |       |
| ------ | ----------- | ----- | ----- | ------ | ------ | ----- |
|        | Aggregation |       |       |        | Guide  |       |
| 4100i, | 6000,       | 6100, | 6200, | 6300,  | 6400,  | 8320, |
|        | 8325,       | 8360, | 8400  | Switch | Series |       |
Published:January2023
Edition:4

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

Open Source Code

This product includes code licensed under the GNU General Public License, the GNU Lesser General
Public License, and/or certain other open source licenses. A complete machine-readable copy of the
source code corresponding to such code is available upon request. This offer is valid to anyone in
receipt of this information and shall expire three years following the date of the final distribution of this
product version by Hewlett Packard Enterprise Company. To obtain such source code, send a check or
money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
6280 America Center Drive
San Jose, CA 95002
USA

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

| 2

Contents
Contents
| Contents                                          |                                            | 3   |
| ------------------------------------------------- | ------------------------------------------ | --- |
| About this                                        | document                                   | 6   |
| Applicableproducts                                |                                            | 6   |
| Latestversionavailableonline                      |                                            | 6   |
| Commandsyntaxnotationconventions                  |                                            | 6   |
| Abouttheexamples                                  |                                            | 7   |
| Identifyingswitchportsandinterfaces               |                                            | 8   |
| Identifyingmodularswitchcomponents                |                                            | 9   |
| Link Aggregation                                  |                                            | 10  |
| Overview                                          |                                            | 10  |
| Aggregationgroup,memberport,andaggregateinterface |                                            | 10  |
| Linkaggregationmodes                              |                                            | 11  |
| LACP                                              |                                            | 11  |
|                                                   | LACPoperatingmodes                         | 11  |
| LAGinterfacestates                                |                                            | 11  |
| Howstaticlinkaggregationgroupsarebuilt            |                                            | 12  |
|                                                   | Referenceportselectionprocess              | 12  |
|                                                   | Settingtheaggregationstateofeachmemberport | 13  |
Settingtheaggregationstateofamemberportinastaticaggregationgroup 13
| Howdynamiclinkaggregationgroupsarebuilt                   |                                                      | 13  |
| --------------------------------------------------------- | ---------------------------------------------------- | --- |
|                                                           | Choosingareferenceport                               | 13  |
|                                                           | Settingtheaggregationstateofeachmemberport           | 14  |
| LAGconfigurationguidelines                                |                                                      | 14  |
|                                                           | Aggregationmemberinterfacerestrictions               | 14  |
|                                                           | Requirementsforaddinginterfaces                      | 14  |
| Layer2aggregationgroups                                   |                                                      | 15  |
|                                                           | ConfiguringaLayer2staticaggregationgroup             | 15  |
|                                                           | ConfiguringaLayer2dynamicaggregationgroup            | 18  |
| Layer3aggregationgroups                                   |                                                      | 21  |
|                                                           | ConfiguringaLayer3staticaggregationgroup             | 21  |
|                                                           | ConfiguringaLayer3dynamicaggregationgroup            | 24  |
| RemovingaLAG                                              |                                                      | 27  |
| RemovinganinterfacefromaLAG                               |                                                      | 28  |
| ChangingtheLAGmembershipforaninterface                    |                                                      | 29  |
| ConfigurationofanaggregateInterface                       |                                                      | 32  |
|                                                           | Configuringthedescriptionofanaggregateinterface      | 32  |
|                                                           | SettingtheMTUforaLayer2memberlinkinterface           | 33  |
|                                                           | SettingtheMTUforaLayer3aggregateinterface            | 33  |
|                                                           | Impactofshuttingdownorbringingupanaggregateinterface | 34  |
|                                                           | Shuttingdownanaggregateinterface                     | 34  |
| Supportedhashingalgorithms                                |                                                      | 34  |
| LACPconfigurationsettings                                 |                                                      | 34  |
| InterfaceLACPsettings                                     |                                                      | 35  |
| Configurationverification                                 |                                                      | 35  |
| BFDreportsaLAGasdownevenwhenhealthylinksarestillavailable |                                                      | 36  |
| LACPandLAGcommands                                        |                                                      | 37  |
3
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

| description(lag)                    |                                |            | 37  |
| ----------------------------------- | ------------------------------ | ---------- | --- |
| hash                                |                                |            | 38  |
| interfacelag                        |                                |            | 38  |
| ipaddress(interfacelag)             |                                |            | 40  |
| ipv6address (lag)                   |                                |            | 40  |
| lacphash                            |                                |            | 41  |
| lacpmode                            |                                |            | 42  |
| lacpport-id                         |                                |            | 43  |
| lacpport-priority                   |                                |            | 44  |
| lacprate                            |                                |            | 45  |
| lacpsystem-priority                 |                                |            | 46  |
| lag                                 |                                |            | 46  |
| showinterface(LAG)                  |                                |            | 47  |
| showlacpaggregates(LAG)             |                                |            | 49  |
| showlacpconfiguration               |                                |            | 50  |
| showlacpinterfaces                  |                                |            | 51  |
| shutdown(interfacelag)              |                                |            | 54  |
| vlantrunknative(LAG)                |                                |            | 54  |
| Smartlink                           |                                |            | 57  |
| Guidelinesandlimitations            |                                |            | 57  |
| Smartlinkcommands                   |                                |            | 58  |
| Configurationcommands               |                                |            | 58  |
|                                     | smartlinkgroup                 |            | 58  |
|                                     | smartlinkrecv-control-vlan     |            | 59  |
| Groupcontextcommands                |                                |            | 59  |
|                                     | description(smartlinkgroup)    |            | 59  |
|                                     | primary-port                   |            | 60  |
|                                     | smartlinkgroupsecondary-port   |            | 61  |
|                                     | control-vlan                   |            | 61  |
|                                     | protected-vlans                |            | 62  |
|                                     | preemption                     |            | 63  |
|                                     | preemption-delay               |            | 64  |
| Displaycommands                     |                                |            | 64  |
|                                     | showsmartlinkgroup             |            | 64  |
|                                     | showsmartlinkgroupall          |            | 65  |
|                                     | showsmartlinkgroupdetail       |            | 66  |
|                                     | showsmartlinkflush-statistics  |            | 67  |
|                                     | clearsmartlinkgroupstatistics  |            | 67  |
|                                     | clearsmartlinkflush-statistics |            | 68  |
|                                     | showrunning-config             |            | 69  |
| Supportabilitycommands              |                                |            | 70  |
|                                     | showcapacitiessmartlink        |            | 70  |
| UFD (Uplink                         | Failure                        | Detection) | 72  |
| Guidelinesandlimitations            |                                |            | 72  |
| BasicUFDconfiguration               |                                |            | 72  |
| UFD(UplinkFailureDetection)commands |                                |            | 73  |
| ufdenable                           |                                |            | 73  |
| ufdsession-id                       |                                |            | 74  |
| links-to-monitor                    |                                |            | 75  |
| links-to-disable                    |                                |            | 76  |
| delay                               |                                |            | 77  |
| showufd                             |                                |            | 78  |
| showcapacitiesufd                   |                                |            | 79  |
| showrunning-configufd               |                                |            | 80  |
Contents|4

|                       | show-techufd       |           | 81  |
| --------------------- | ------------------ | --------- | --- |
|                       | debugufdall        |           | 82  |
| Support               | and Other          | Resources | 84  |
| AccessingArubaSupport |                    |           | 84  |
| AccessingUpdates      |                    |           | 85  |
|                       | ArubaSupportPortal |           | 85  |
|                       | MyNetworking       |           | 85  |
| WarrantyInformation   |                    |           | 85  |
| RegulatoryInformation |                    |           | 85  |
| DocumentationFeedback |                    |           | 86  |
5
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

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

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL704C, JL705C, JL706A, JL707A, JL708A,

JL709A, JL710A, JL711A, JL717C, JL718C)

n Aruba 8400 Switch Series (JL375A, JL376A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

Usage

example-text

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

Identifies a placeholder—such as a parameter or a variable—that you must
substitute with an actual value in a command or in code:

n For output formats where italic text cannot be displayed, variables
are enclosed in angle brackets (< >). Substitute the text—including
the enclosing angle brackets—with an actual value.

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

6

Convention

Usage

|

{ }

[ ]

… or

...

n For output formats where italic text can be displayed, variables

might or might not be enclosed in angle brackets. Substitute the
text including the enclosing angle brackets, if any, with an actual
value.

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
Examples in this document are representative and might not match your particular switch or
environment.

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

About this document | 7

Where <VLAN-ID> is a variable representing the VLAN number.

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

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 8.

The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

On the 6300 Switch Series

n member: Member number of the switch in a Virtual Switching Framework (VSF) stack. Range: 1 to 10.
The primary switch is always member 1. If the switch is not a member of a VSF stack, then member is
1.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on member 1.

On the 6400 Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

8

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the 83xx Switch Series

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

For example, the logical interface 1/1/4 in software is associated with physical port 4 in slot 1 on
member 1.

Identifying modular switch components

n Power supplies are on the front of the switch behind the bezel above the management modules.

Power supplies are labeled in software in the format: member/power supply:

o member: 1.

o power supply: 1 to 4.

n Fans are on the rear of the switch and are labeled in software as: member/tray/fan:

o member: 1.

o tray: 1 to 4.

o fan: 1 to 4.

n Fabric modules are not labeled on the switch but are labeled in software in the format:

member/module:

o member: 1.

o member: 1 or 2.

n The display module on the rear of the switch is not labeled with a member or slot number.

About this document | 9

Chapter 2

Link Aggregation

Link Aggregation

Overview
Ethernet link aggregation bundles multiple physical Ethernet links into one logical link, called a link
aggregation group (LAG).

Link aggregation has the following benefits:

n Increased bandwidth beyond the limits of any single link. In an aggregate link, traffic is distributed

across the member ports.

n Improved link reliability. The member ports dynamically back up one another. When a member port
fails, its traffic is automatically switched to other member ports. As shown in the following figure
Device A and Device B are connected by three physical Ethernet links. These physical Ethernet links
are combined into an aggregate link called link aggregation 1. The bandwidth of this aggregate link
can reach up to the total bandwidth of the three physical Ethernet links. At the same time, the three
Ethernet links back up one another. When a physical Ethernet link fails, the traffic originally intended
for the failed link is switched to the remaining active links.

Ethernet link aggregation diagram

Aggregation group, member port, and aggregate interface
An aggregation group is a collection of physical interfaces that are bundled together for the purpose of
load distribution and redundancy. These physical interfaces are called member ports. They are
configured through a logical aggregate interface.

An aggregate interface can be one of the following types:

n Layer 2: The member ports of the corresponding Link Aggregation Group can only be Layer 2

Ethernet interfaces.

n Layer 3: The member ports of the corresponding Link Aggregation Group can only be Layer 3

interfaces.

Layer 3 aggregation groups are not supported on the 4100i, 6000, 6100, and 6200 Switch Series.

The effective port rate of an aggregate interface equals the total rate of its member ports. Only full
duplex mode members are eligible for aggregation.

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

10

Link aggregation modes
An aggregation group operates in one of the following modes:

n Static LAG: In the static LAG mode of operation, Link failure is not detected as there is no keep alive
PDU communication between the devices. A misconfiguration on one side can cause much trouble
and be difficult to troubleshoot, because no signaling takes place between the two peers.

n Dynamic LAG or LACP: The local device and the peer device automatically maintain the aggregation
states of the member ports, resulting in link failure being quickly detected by exchanging the PDU.
LACP reduces the workload of network administrators.

Dynamic LAG uses LACP packets to establish the association between two peers. This configuration
results in the reduction of the misconfiguration probability. Also, link failures are intelligently handled by
two participating devices through the LACP protocol, which is adaptive/dynamic to these network failures.

Layer 2 aggregation groups and Layer 3 aggregation groups support both the static and dynamic modes.

LACP
Dynamic aggregation is implemented through the IEEE 802.3ad Link Aggregation Control Protocol
(LACP).

LACP uses LACPDUs to exchange aggregation information between LACP-enabled devices. Each
member port in a dynamic aggregation group can exchange information with its peer. When a member
port receives an LACPDU, it compares the received information with information received on the other
member ports. In this way, the two systems agree on which ports are placed in Selected state.

The LACPDU fields convey data for the LACP functions, including:

n System LACP priority

n System MAC address

n Port priority

n Port number

n Operational key

LACP operating modes

LACP can operate in active or passive mode.

n Active mode: When the LACP is operating in active mode on either end of a link, both ports can send
PDUs. The "active" LACP initiates an LACP connection by sending LACPDUs. The "passive" LACP will
wait for the remote end to initiate the link.

n Passive mode: When the LACP is operating in passive mode on a local member port and as its peer

port, both ports cannot send PDUs.

Two peer ports operating in "passive" mode will never establish an LACP link.

For an LACP LAG, one side must have LACP in active mode and the peer must have an LACP
configuration of active or passive mode. If you do not enable LACP on a LAG, it is treated as a static LAG
and the peer cannot negotiate LACP with the LAG.

LAG interface states

Link Aggregation | 11

The output from the CLI commands show lacp interfaces and show lacp interfaces multi-chassis
display the following interface states:

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

When setting the aggregation states of the ports in an aggregation group, the system automatically
chooses a member port as the reference port. A selected port must have the same operational key and
attribute configurations as the reference port.

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

12

Thesystemchoosesareferenceportfromthememberportsintheupstate.Thefirstmemberinterface
whichisoperationallyupisselectedasreferenceport.
| Setting | the aggregation |     | state | of each member | port |     |
| ------- | --------------- | --- | ----- | -------------- | ---- | --- |
Afterthereferenceportischosen,thesystemsetstheaggregationstateofeachmemberportinthe
staticaggregationgroup.
| Setting     | the aggregation |     | state | of a member | port | in a static |
| ----------- | --------------- | --- | ----- | ----------- | ---- | ----------- |
| aggregation | group           |     |       |             |      |             |
AfterthemaximumlimitofmembersisreachedinaLAG,anadditionalportcannotbeaddedtothe
aggregationgroup.Ifaportbelongstoacardtypewithadifferentspeedthantheotheraggregation
members,theportcanstillbeaddedtotheaggregationgroup.IfdynamicLAGisenabled,anyport
memberwithaspeeddifferentthanotheraggregationmembersisblockedorineligiblefromthesame
aggregationgroup.Anyoperationalkeys/attributesorconfigurationchangesmightaffectthe
aggregationstatesofthememberports.
| How      | dynamic     | link aggregation |      | groups | are | built |
| -------- | ----------- | ---------------- | ---- | ------ | --- | ----- |
| Choosing | a reference |                  | port |        |     |       |
LinkAggregation|13

The system chooses a reference port from the member ports in up state. A selected port must have the
same operational key and attribute configurations as the reference port.

The process by which the local system (the actor) and the peer system (the partner) negotiate a
reference port occurs as follows:

1. The two systems determine the system with the smaller system ID. A system ID contains the

system LACP priority and the system MAC address.
a. The two systems compare their LACP priority values.

The lower the LACP priority, the smaller the system ID. If the LACP priority values are the
same, the two systems proceed to step b.

b. The two systems compare their MAC addresses.

The lower the MAC address, the smaller the system ID.

2. The system with the smaller system ID chooses the first operationally up port as the reference

port.

A port ID contains a port priority and a port number. The lower the port priority, the smaller the port
ID.

Setting the aggregation state of each member port

After the reference port is chosen, the system with the smaller system ID sets the state of each member
port on its side.

The system with the greater system ID can detect the aggregation state changes on the peer system.
The system with the greater system ID sets the aggregation state of local member ports the same as
their peer ports.

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

n To determine the maximum number of LAG interfaces for your type of switch, look at the output
from the show capacities lag command; however, the number of LAGs that can be created
depends on the availability of the physical interface since each LAG interface needs at least one
physical interface as a member link. fter the maximum limit of members is reached in a LAG, an

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

14

additional port cannot be added to the aggregation group. If a port belongs to a card type with a
different speed than the other aggregation members, the port can still be added to the aggregation
group. If dynamic LAG is enabled, any port member with a speed different than other aggregation
members is blocked or ineligible from the same aggregation group. Any operational keys/attributes
or configuration changes might affect the aggregation states of the member ports.

n The nondefaults configuration on an interface is removed automatically when the interface is added
to a link aggregation. For example: Assume that you remove a member interface from an existing
LAG and add it to another LAG. The software removes the nondefault configurations on the interface
when it is added to the new LAG.

Configuration consistency requirements

n Configure at least one active mode aggregation in two devices.

n For a successful static aggregation, make sure the ports at both ends of each link are in the same

aggregation state.

n For a successful dynamic aggregation, make sure the peer ports of the ports aggregated at one end

are also aggregated, and that one of the ends is configured as "active". The two ends can
automatically negotiate the aggregation state of each member port.

Removing interfaces

n Deleting an aggregate interface also deletes its aggregation group and causes all member ports to

leave the aggregation group.

n When a member interface is removed from a LAG:

o 4100i, 6000, 6100, 6200, 6300, and 6400 switches: The interface goes to its default status of

unshut.

o 8320, 8325, 8360, or 8400 switches: The interface becomes disabled.

Disabling an interface

When an interface LAG is disabled with the shutdown command, all its members also become
operationally down.

Layer 2 aggregation groups
All switches support static and dynamic layer 2 aggregation groups.

On the 6400 Switch Series, port identification differs. Line card ports start at 1/3/1.

Configuring a Layer 2 static aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#.

Procedure

1. Create a Layer 2 aggregate interface and access the Layer 2 aggregate interface view by entering:

switch(config)# interface lag <ID>

Link Aggregation | 15

TherangeoftheLAGinterfaceIDis1to256.
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
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformationabout
theno routingcommand.
Onthe4100i,6000,6100,and6200SwitchSeries,routingisnotsupportedonphysicalinterfaces.
Onthe6300and6400SwitchSeries,routingisdisabledbydefault.
4. AssignanativeVLANIDtoatrunkinterfaceontheLAGbyentering:
| switch(config-lag-if)# |     | vlan trunk | native <VLAN-ID> |
| ---------------------- | --- | ---------- | ---------------- |
Forexample:
switch(config-lag-if)#
|     |     | vlan trunk | native 1 |
| --- | --- | ---------- | -------- |
5. Usethefollowingstepstoaddamaximumof16interfacestotheLAG:
a. ToassignaninterfacetotheLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID> |
| ---------------------- | --- | --------- | --------- |
ToassignarangeofinterfacestoaLAG:
| switch(config-lag-if)# |     | interface | <PORT-ID>-<PORT-ID> |
| ---------------------- | --- | --------- | ------------------- |
Forexample:
16
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

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
6. Viewtheconfigurationbyenteringthefollowing:
For4100i,6000,6100,6200,6300,and6400switchseries:
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
| switch(config-if-<1/1/1-1/1/4>)# |               | show        | lacp aggregates |
| -------------------------------- | ------------- | ----------- | --------------- |
| Aggregate name                   | : lag100      |             |                 |
| Interfaces                       | : 1/1/3 1/1/1 | 1/1/4 1/1/2 |                 |
| Heartbeat rate                   | : N/A         |             |                 |
| Hash                             | : l3-src-dst  |             |                 |
| Aggregate mode                   | : Off         |             |                 |
LinkAggregation|17

For8320,8325,8360,and8400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |                |     | show running-config |     |
| -------------------------------- | -------------- | --- | ------------------- | --- |
| Current                          | configuration: |     |                     |     |
!
| vlan      | 1   |     |     |     |
| --------- | --- | --- | --- | --- |
| interface | lag | 100 |     |     |
no shutdown
no routing
|           | vlan trunk | native 1    |     |     |
| --------- | ---------- | ----------- | --- | --- |
|           | vlan trunk | allowed all |     |     |
| interface | 1/1/1      |             |     |     |
no shutdown
lag 100
| interface | 1/1/2 |     |     |     |
| --------- | ----- | --- | --- | --- |
no shutdown
lag 100
| interface | 1/1/3 |     |     |     |
| --------- | ----- | --- | --- | --- |
no shutdown
lag 100
| interface | 1/1/4 |     |     |     |
| --------- | ----- | --- | --- | --- |
no shutdown
lag 100
switch(config-if-<1/1/1-1/1/4>)#
show lacp aggregates
| Aggregate   | name | : lag100        |             |       |
| ----------- | ---- | --------------- | ----------- | ----- |
| Interfaces  |      | : 1/1/3 1/1/1   | 1/1/4 1/1/2 |       |
| Heartbeat   | rate | : N/A           |             |       |
| Hash        |      | : l3-src-dst    |             |       |
| Aggregate   | mode | : Off           |             |       |
| Configuring | a    | Layer 2 dynamic | aggregation | group |
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
18
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

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
LinkAggregation|19

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
20
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

| Heartbeat |     | rate | : Fast       |     |     |     |     |
| --------- | --- | ---- | ------------ | --- | --- | --- | --- |
| Hash      |     |      | : l3-src-dst |     |     |     |     |
| Aggregate |     | mode | : Active     |     |     |     |     |
For8320,8325,8360,and8400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     |                |     |     | show running-config |     |     |
| -------------------------------- | --- | -------------- | --- | --- | ------------------- | --- | --- |
| Current                          |     | configuration: |     |     |                     |     |     |
!
| vlan      | 1   |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- |
| interface |     | lag | 20  |     |     |     |     |
no shutdown
no routing
|           | vlan | trunk | native  | 1   |     |     |     |
| --------- | ---- | ----- | ------- | --- | --- | --- | --- |
|           | vlan | trunk | allowed | all |     |     |     |
|           | lacp | mode  | active  |     |     |     |     |
|           | lacp | rate  | fast    |     |     |     |     |
| interface |      | 1/1/1 |         |     |     |     |     |
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
Layer3aggregationgroupsaresupportedonallswitchseriesexcept6000,and6100SwitchSeries.
| Configuring |     | a   | Layer 3 | static | aggregation |     | group |
| ----------- | --- | --- | ------- | ------ | ----------- | --- | ----- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer3aggregateinterfaceandaccesstheLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# |     | interface |     | lag <ID> |     |     |
| --- | --------------- | --- | --------- | --- | -------- | --- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer3aggregateinterface,thesystemautomaticallycreatesaLayer3static
aggregationgroupnumberedthesame.
LinkAggregation|21

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
n For8320,8325,8360,and8400switchseries:
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
22
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

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
For6200,6300and6400switchseries:
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
LinkAggregation|23

For8320,8325,8360,and8400switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |                |     | show running-config |     |     |
| -------------------------------- | -------------- | --- | ------------------- | --- | --- |
| Current                          | configuration: |     |                     |     |     |
!
| vlan      | 1   |     |     |     |     |
| --------- | --- | --- | --- | --- | --- |
| interface | lag | 100 |     |     |     |
no shutdown
|           | ip address | 192.0.2.1/30 |     |     |     |
| --------- | ---------- | ------------ | --- | --- | --- |
| interface | 1/1/1      |              |     |     |     |
no shutdown
lag 100
| interface | 1/1/2 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| interface | 1/1/3 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| interface | 1/1/4 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
lag 100
| switch(config-if-<1/1/1-1/1/4>)# |      |                 | show lacp   | aggregates |       |
| -------------------------------- | ---- | --------------- | ----------- | ---------- | ----- |
| Aggregate                        | name | : lag100        |             |            |       |
| Interfaces                       |      | : 1/1/3 1/1/1   | 1/1/4 1/1/2 |            |       |
| Heartbeat                        | rate | : N/A           |             |            |       |
| Hash                             |      | : l3-src-dst    |             |            |       |
| Aggregate                        | mode | : Off           |             |            |       |
| Configuring                      | a    | Layer 3 dynamic | aggregation |            | group |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. CreateaLayer3aggregateinterfaceandaccesstheLayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |     |
| --- | --------------- | --------- | -------- | --- | --- |
TherangeoftheLAGinterfaceIDis1to256.
WhilecreatingtheLayer3aggregateinterface,thesystemautomaticallycreatesaLayer3dynamic
aggregationgroupnumberedthesame.
2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
|     | n For6200,6300and6400switchseries: |     |             |     |     |
| --- | ---------------------------------- | --- | ----------- | --- | --- |
|     | switch(config-lag-if)#             |     | no shutdown |     |     |
|     | switch(config-lag-if)#             |     | routing     |     |     |
24
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- |

Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface | 1/1/2    |     |
| --- | ------------------ | --------- | -------- | --- |
|     | switch(config-if)# | no        | shutdown |     |
|     | switch(config-if)# | routing   |          |     |
n For8320,8325,8360,and8400switchseries:
| switch(config-lag-if)# |     | no shutdown |     |     |
| ---------------------- | --- | ----------- | --- | --- |
Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface | 1/1/2    |     |
| --- | ------------------ | --------- | -------- | --- |
|     | switch(config-if)# | no        | shutdown |     |
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
LinkAggregation|25

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
For6200,6300and6400switchseries:
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
26
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

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
LinkAggregation|27

DeletetheLAG.Enter:
| switch(config)# | no interface |     | lag <ID> |     |
| --------------- | ------------ | --- | -------- | --- |
Forexample:
| switch(config)# | no interface |     | lag 100 |     |
| --------------- | ------------ | --- | ------- | --- |
AllinterfacesassignedtotheLAGareautomaticallyremovedfromtheLAGaspartofthedeletion
processoftheLAG.AfterremovingaphysicalinterfacefromaLAG,
n 4100i, 6000, 6100, 6200, 6300, and 6400 switches: TheinterfaceassociatedwiththeLAGbecomes
layer2portswiththedefaultlayer2configurationsandadminstatusenabled.
n 8320, 8235, 8360, and 8400 switches: TheinterfaceassociatedwiththeLAGbecomeslayer3ports
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
28
| AOS-CX10.09LinkAggregationGuide| | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | ----------------------------- | --- | --- | --- |

AfterremovingaphysicalinterfacefromaLAG:
n 4100i, 6000, 6100, 6200, 6300, and 6400 switches:TheinterfaceassociatedwithLAGbecomes
layer2portswithdefaultlayer2configurationsandwithadminstatusofenabled
n 8320, 8325, 8360, and 8400 switches:TheinterfaceassociatedwiththeLAGbecomesL3portswith
defaultL3configurationsandadministrativedown.Forexample,supposeinterface1/1/1waspartof
LAG3andyouhadadministrativelyenabledtheinterface.Ifyoulaterremoveinterface1/1/1from
LAG3,theadministrativestatusautomaticallychangestodown.Ifyouwanttousetheinterface
again,youmustadministrativelyenableitagain.
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
LinkAggregation|29

vlan 1
| interface lag | 100 |     |     |
| ------------- | --- | --- | --- |
no shutdown
no routing
| vlan trunk      | native  | 1   |     |
| --------------- | ------- | --- | --- |
| vlan trunk      | allowed | all |     |
| interface 1/1/1 |         |     |     |
| interface 1/1/2 |         |     |     |
no shutdown
lag 100
switch(config-if)#
AfterremovingaphysicalinterfacefromaLAG,theinterfaceassociatedwiththeLAGbecomesL3
portswithdefaultL3configurationsandadministrativedown.Forexample,supposeinterface
1/1/1waspartofLAG3andyouhadadministrativelyenabledtheinterface.Ifyoulaterremove
interface1/1/1fromLAG3,theadministrativestatusautomaticallychangestodown.Ifyouwant
tousetheinterfaceagain,youmustadministrativelyenableitagain.
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
30
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

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
Noticethatinterface1/1/1inthepreviousexampleisstillnotactive,eventhoughithasbeen
addedtoLAG10.Tochangetheadministrativestateofthememberinterface,entertheno
shutdowncommandattheinterfacelevel.
Forexample:
For4100i,6000,6100,6200,6300,and6400switchseries:
| switch(config-if)# | interface           | 1/1/1 |
| ------------------ | ------------------- | ----- |
| switch(config-if)# | no shutdown         |       |
| switch(config-if)# | show running-config |       |
Current configuration:
LinkAggregation|31

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
|     |                        | no shutdown |                |     |     |
| --- | ---------------------- | ----------- | -------------- | --- | --- |
|     | switch(config-if)#     | show        | running-config |     |     |
|     | Current configuration: |             |                |     |     |
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
32
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
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
LinkAggregation|33

SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformation
abouttheip mtu <VALUE>command.Whenallowingjumboframesunderalayer2aggregation
interface,makesurethattheMTUvalueissetappropriatelyunderallmemberinterfaces.
IftheIPMTUisconfiguredas9198,theMTUonthephysicalinterfacesmustalsobeconfiguredas9198.
Impact of shutting down or bringing up an aggregate interface
Bydefault,anaggregateinterfaceisdown.Shuttingdownorbringingupanaggregateinterfaceaffects
theaggregationstatesandlinkstatesofmemberportsinthecorrespondingaggregationgroupas
follows:
n Whenanaggregateinterfaceisshutdown,allSelectedportsinthecorrespondingaggregationgroup
becomeUnselectedportsandallmemberportsgotoanoperationallydownstate.
n Whenanaggregateinterfaceisbroughtup,theaggregationstatesofmemberportsinthe
correspondingaggregationgrouparerecalculated.LAGmembers,whichareadministrativelyup,will
becomeoperationallyup.Themembersthatarenotadministrativelyupwillbeinthesamestateand
notmadeeligibleforaggregation.
| Shutting | down an | aggregate | interface |     |
| -------- | ------- | --------- | --------- | --- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
EntertheLayer3aggregateinterfaceviewbyentering:
switch(config)#
|     | interface | lag <ID> |     |     |
| --- | --------- | -------- | --- | --- |
Shutdowntheaggregateinterface:
| switch(config-lag-if)# |         | shutdown   |     |     |
| ---------------------- | ------- | ---------- | --- | --- |
| Supported              | hashing | algorithms |     |     |
n SourceMACanddestinationMAC
n SourceIPanddestinationIP
n Sourceportanddestinationport.
| LACP | configuration | settings |     |         |
| ---- | ------------- | -------- | --- | ------- |
| Task |               | Command  |     | Example |
SettingtheLACPmodeto lacp mode {active | passive} switch(config-lag-if)# lacp
activeorpassive.
mode active
34
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

| Task | Command |     |     | Example |     |
| ---- | ------- | --- | --- | ------- | --- |
SettingtheLACPmodetooff. no lacp mode {active | passive} switch(config-lag-if)# no
|     |     |     |     | lacp mode active |     |
| --- | --- | --- | --- | ---------------- | --- |
Settingthehashtype. For6000,6100,and8400Switch For6000,6100,and8400Switch
|     | Series:                        |             |            | Series:                    |           |
| --- | ------------------------------ | ----------- | ---------- | -------------------------- | --------- |
|     | lacp hash                      | [l2-src-dst | | l3-src-  | switch(config)#            | lacp hash |
|     | dst | l4-src-dst]              |             |            | l2-src-dst                 |           |
|     | For8320,8325,6200,6300,and6400 |             |            | For8320,8325,6200,6300,and |           |
|     | SwitchSeries:                  |             |            | 6400SwitchSeries:          |           |
|     | hash [l2-src-dst               | |           | l3-src-dst | | switch(config-lag-if)#   | hash      |
|     | l4-src-dst]                    |             |            | l2-src-dst                 |           |
SettingtheLACPratetofast. lacp rate fast switch(config)# interface
lag 1
|     |     |     |     | switch(config-lag-if)# | lacp |
| --- | --- | --- | --- | ---------------------- | ---- |
rate fast
SettingtheLACPratetoslow. lacp rate slow switch(config)# interface
lag 1
|     |     |     |     | switch(config-lag-if)# | lacp |
| --- | --- | --- | --- | ---------------------- | ---- |
rate slow
| Applyingshutdownonthe | shutdown |     |     | switch(config)# | interface |
| --------------------- | -------- | --- | --- | --------------- | --------- |
LAGport.
lag 1
switch(config-lag-if)#
shutdown
Resettingeveryinterfacein no shutdown switch(config-lag-if)# no
| theLAGtothedefault(up)  |         |     |     | shutdown |     |
| ----------------------- | ------- | --- | --- | -------- | --- |
| Interface LACP settings |         |     |     |          |     |
| Task                    | Command |     |     | Example  |     |
SettingtheLACPportID. lacp port-id <ID> switch(config-if)# lacp port-
id 100
SettingtheLACPportIDtothe no lacp port-id switch(config-if)# no lacp
default.
port-id
SettingtheLACPportpriority. lacp port-priority <PORT- switch(config-if)# lacp port-
|     | PRIORITY> |     |     | priority 100 |     |
| --- | --------- | --- | --- | ------------ | --- |
SettingtheLACPportpriority no lacp port-priority switch(config-if)# no lacp
| tothedefault               |     |     |     | port-priority |     |
| -------------------------- | --- | --- | --- | ------------- | --- |
| Configuration verification |     |     |     |               |     |
LinkAggregation|35

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
|                |           |            | Aggregate-name        |      |                 | : lag100     |
| -------------- | --------- | ---------- | --------------------- | ---- | --------------- | ------------ |
| informationfor |           |            | Aggregated-interfaces |      |                 | :            |
| aLAG           |           |            | Heartbeat             | rate |                 | : N/A        |
|                |           |            | Hash                  |      |                 | : l3-src-dst |
|                |           |            | Aggregate             | mode |                 | : off        |
| ViewingLACP    | show lacp | interfaces |                       |      |                 |              |
|                |           |            | switch#               | show | lacp interfaces |              |
interfacedetails
Theoutputistoowidetodisplayinacolumn.Thecommand
outputisprovidedintheCLItopicforthecommand.
| BFD reports | a LAG | as down | even | when | healthy | links are |
| ----------- | ----- | ------- | ---- | ---- | ------- | --------- |
still available
Symptom
BFDisnotsupportedonthe4100i,6000,6100,and6200SwitchSeries.
TheBidirectionalForwardDetection(BFD)featurereportsaLinkAggregation(LAG),asbeingdown,even
thoughtherearehealthyLAGlinksavailable.TheLAG,containingthedownedlink,willeventually
rebalancethetraffictoitsotherlinks.
Cause
36
| AOS-CX10.09LinkAggregationGuide| | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |     |
| -------------------------------- | ----------------------------- | --- | --- | --- | --- | --- |

ThisnotificationoccurswhentheminimumBFDcontrolpacketreceptionintervalissetatafasterrate
thantheLinkAggregationControlProtocol(LACP)rateandLAGrebalancingoccurs.BFDassumesthat
thelinkisdownwithoutrealizingthattheLAGisrebalancingthetrafficload.
Action
SettheminimumBFDcontrolpacketreceptionintervaltoaslowerratethantheLACPrateorsetthe
LACPratetoafasterratethantheminimumBFDcontrolpacketreceptioninterval.
1. TofindthecurrentsettingsoftheminimumBFDcontrolpacketreceptioninterval,entertheshow
running-configcommand.
TheminimumBFDcontrolpacketreceptionintervalsettingislistedasbfd min-receive-
intervalinthecommandoutputandthemeasurementisinms.
2. TofindthecurrentrateofLACP,entertheshow lacp aggregatescommand.
| TheLACPrateislistedastheHeatbeat |     | rateinthecommandoutput. |     |
| -------------------------------- | --- | ----------------------- | --- |
3. TochangetheminimumBFDcontrolpacketreceptioninterval,enterthebfd min-receive-
intervalcommand.
4. TochangetheLACPrate,enterthelacp rate {fast | slow}command.
| LACP and LAG      | commands |     |     |
| ----------------- | -------- | --- | --- |
| description (lag) |          |     |     |
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
Command History
LinkAggregation|37

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
hash
| hash [l2-src-dst | | l3-src-dst | | l4-src-dst] |     |
| ---------------- | ------------ | ------------- | --- |
Description
Thiscommandcontrolstheselectionofaninterfaceinagroupofaggregateinterfaces.Thehashtype
valuehelpstransmitaframe.ThisconfigurationmustbedoneattheLAGinterfacelevel.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
l2-src-dst Specifiestheload-balancingcalculationtoincludeonlyLayer2
items,suchassourceanddestinationMACaddresses.
l3-src-dst Specifiestheload-balancingcalculationtoincludeonlyLayer3
items,suchassourceanddestinationIPaddresses.Default
setting.
l4-src-dst
Specifiestheload-balancingcalculationtoincludeonlyLayer4
items,suchassourceanddestinationUDP/TCPports.
Example
| switch(config-lag-if)# |         | hash l2-src-dst |              |
| ---------------------- | ------- | --------------- | ------------ |
| Command History        |         |                 |              |
| Release                |         |                 | Modification |
| 10.07orearlier         |         |                 | --           |
| Command Information    |         |                 |              |
| Platforms              | Command | context         | Authority    |
config-lag-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| interface     | lag      |     |     |
| ------------- | -------- | --- | --- |
| interface lag | <ID>     |     |     |
| no interface  | lag <ID> |     |     |
38
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

Description
CreatesaLinkAggregationGroup(LAG)interfacerepresentedbyanID.
ThenoformofthiscommanddeletesaLAGinterfacerepresentedbyanID.
| Parameter |     |     | Description               |
| --------- | --- | --- | ------------------------- |
| <ID>      |     |     | SpecifiesaLAGinterfaceID. |
Usage
KeepinmindthefollowingrequirementswhenaddinginterfacestoaLAG:
n TodeterminethemaximumnumberofLAGinterfacesforyourtypeofswitch,lookattheoutput
fromtheshow capacities lagcommand;however,thenumberofLAGsthatcanbecreated
dependsontheavailabilityofthephysicalinterfacesinceeachLAGinterfaceneedsatleastone
physicalinterfaceasamemberlink.
n AfterthemaximumlimitofmembersisreachedinaLAG,anadditionalportcannotbeaddedtothe
aggregationgroup.Ifaportbelongstoacardtypewithadifferentspeedthantheotheraggregation
members,theportcanstillbeaddedtotheaggregationgroup.IfdynamicLAGisenabled,anyport
memberwithaspeeddifferentthanotheraggregationmembersisblockedorineligiblefromthe
sameaggregationgroup.Anyoperationalkeys/attributesorconfigurationchangesmightaffectthe
aggregationstatesofthememberports.
n Thenondefaultsconfigurationonaninterfaceisremovedautomaticallywhentheinterfaceisadded
toalinkaggregation.Forexample:Assumethatyouremoveamemberinterfacefromanexisting
LAGandaddittoanotherLAG.Thesoftwareremovesthenondefaultconfigurationsontheinterface
whenitisaddedtothenewLAG.
Examples
CreatingaLinkAggregationGroup(LAG)interfacerepresentedbyanIDof100:
| switch(config)# | interface |     | lag 100 |
| --------------- | --------- | --- | ------- |
DeletingaLinkAggregationGroup(LAG)interfacerepresentedbyanIDof100:
| switch(config)#     | no      | interface | lag 100      |
| ------------------- | ------- | --------- | ------------ |
| Command History     |         |           |              |
| Release             |         |           | Modification |
| 10.07orearlier      |         |           | --           |
| Command Information |         |           |              |
| Platforms           | Command | context   | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
LinkAggregation|39

| ip address    | (interface         |     |     | lag)        |     |
| ------------- | ------------------ | --- | --- | ----------- | --- |
| ip address    | <IPV4-ADDR>/<MASK> |     |     | [secondary] |     |
| no ip address | <IPV4-ADDR>/<MASK> |     |     | [secondary] |     |
Description
SetsanIPv4addressandsubnetmasktoaLAGinterface.Oneprimaryandupto31secondaryaddress
canbeconfiguredperinterface.
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
| switch(config)#        |     | interface |     | lag 1      |                 |
| ---------------------- | --- | --------- | --- | ---------- | --------------- |
| switch(config-lag-if)# |     |           |     | ip address | 198.51.100.1/24 |
RemovingtheIPaddress198.51.100.1withamaskof24bitsfromLAGinterface1:
| switch(config)#        |             | interface |         | lag 1         |                 |
| ---------------------- | ----------- | --------- | ------- | ------------- | --------------- |
| switch(config-lag-if)# |             |           |         | no ip address | 198.51.100.1/24 |
| Command                | History     |           |         |               |                 |
| Release                |             |           |         |               | Modification    |
| 10.07orearlier         |             |           |         |               | --              |
| Command                | Information |           |         |               |                 |
| Platforms              | Command     |           | context |               | Authority       |
6300 config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8320
8325
8360
8400
ipv6 address (lag)
40
| AOS-CX10.09LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- |

| ipv6 address    | <IPV6-ADDR>/<MASK> |     |     |
| --------------- | ------------------ | --- | --- |
| no ipv6 address | <IPV6-ADDR>/<MASK> |     |     |
Description
SetsanIPv6addressandsubnetmasktoaLAGinterface.
ThenoformofthiscommandremovestheIPv6addressfromtheinterface.
| Parameter   |     |     | Description                       |
| ----------- | --- | --- | --------------------------------- |
| <IPV6-ADDR> |     |     | SpecifiestheIPaddressinIPv6format |
(xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx),wherexisa
hexadecimalnumberfrom0toF.Youcanusetwocolons(::)to
representconsecutivezeros(butonlyonce),removeleading
zeros,andcollapseaquartetoffourzerostoasingle0.For
example,thisaddress
2222:0000:3333:0000:0000:0000:4444:0055becomes
2222:0:3333::4444:55.
| <MASK> |     |     | SpecifiesthenumberofbitsintheaddressmaskinCIDRformat |
| ------ | --- | --- | ---------------------------------------------------- |
(x),wherexisadecimalnumberfrom0to128.
Examples
SettingtheIPv6addressonLAGinterface1to2001:0db8:85a3::8a2e:0370:7334withamaskof24bits:
| switch(config)# | interface | lag 1 |     |
| --------------- | --------- | ----- | --- |
switch(config-lag-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
RemovingtheIPaddress2001:0db8:85a3::8a2e:0370:7334withmaskof24bitswithamaskof24bits
fromLAGinterface1:
| switch(config)# | interface | lag 1 |     |
| --------------- | --------- | ----- | --- |
switch(config-lag-if)#
|                     |         | no ipv6 | address 2001:0db8:85a3::8a2e:0370:7334/24 |
| ------------------- | ------- | ------- | ----------------------------------------- |
| Command History     |         |         |                                           |
| Release             |         |         | Modification                              |
| 10.07orearlier      |         |         | --                                        |
| Command Information |         |         |                                           |
| Platforms           | Command | context | Authority                                 |
6300 config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
6400
8320
8325
8360
8400
lacp hash
LinkAggregation|41

| lacp hash | [l2-src-dst |             |     | | l3-src-dst | | l4-src-dst] |
| --------- | ----------- | ----------- | --- | ------------ | ------------- |
| no lacp   | hash        | [l2-src-dst |     | | l3-src-dst | | l4-src-dst] |
Description
Controlstheselectionofaninterfaceinagroupofaggregateinterfaces.Thehashtypevaluehelps
transmitaframe.Thisconfigurationmustbedoneatthegloballevel.
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
| switch(config)# |             |         | lacp | hash l2-src-dst |              |
| --------------- | ----------- | ------- | ---- | --------------- | ------------ |
| Command         | History     |         |      |                 |              |
| Release         |             |         |      |                 | Modification |
| 10.07orearlier  |             |         |      |                 | --           |
| Command         | Information |         |      |                 |              |
| Platforms       |             | Command |      | context         | Authority    |
config
4100i Administratorsorlocalusergroupmemberswithexecutionrights
| 6000 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
6100
8400
lacp mode
| lacp mode | {active |         | | passive} |          |     |
| --------- | ------- | ------- | ---------- | -------- | --- |
| no lacp   | mode    | {active | |          | passive} |     |
Description
SetsanLACPmodetoactiveorpassive.
ThenoformofthiscommandsetstheLACPmodetooff,returningtheLAGtoastaticmode
aggregation.
| Parameter |     |     |     |     | Description                                          |
| --------- | --- | --- | --- | --- | ---------------------------------------------------- |
| active    |     |     |     |     | SpecifiesthatthelocalswitchwilltransmitLACPDataUnits |
(LACPDUs)toattempttonegotiatewiththeremotedevice.
42
| AOS-CX10.09LinkAggregationGuide| |     |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | --- | --- | ----------------------------- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
passive SpecifiesthatthelocalswitchwilllistenforLACPDUsfromthe
remotedeviceforLACPnegotiation.
NOTE:
AmomentarytrafficdropoccursbecauseLACPpartnersreconverge
whenchangingthemodefromactivetopassiveorfrompassivetoactive.
Examples
SettingtheLACPmodetoactive:
| switch(config)#        | interface | lag       | 1      |
| ---------------------- | --------- | --------- | ------ |
| switch(config-lag-if)# |           | lacp mode | active |
SettingtheLACPmodetooff:
| switch(config)#        | interface | lag     | 1            |
| ---------------------- | --------- | ------- | ------------ |
| switch(config-lag-if)# |           | no lacp | mode active  |
| Command History        |           |         |              |
| Release                |           |         | Modification |
| 10.07orearlier         |           |         | --           |
| Command Information    |           |         |              |
| Platforms              | Command   | context | Authority    |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
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
LinkAggregation|43

| switch(config-if)# |     | lacp port-id | 10  |
| ------------------ | --- | ------------ | --- |
RemovingtheLACPportIDvalue:
| switch(config-if)#  |         | no lacp port-id |              |
| ------------------- | ------- | --------------- | ------------ |
| Command History     |         |                 |              |
| Release             |         |                 | Modification |
| 10.07orearlier      |         |                 | --           |
| Command Information |         |                 |              |
| Platforms           | Command | context         | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp port-priority
| lacp port-priority | <PORT-PRIORITY> |     |     |
| ------------------ | --------------- | --- | --- |
no lacp port-priority
Description
SetsanLACPportpriorityvalueforthememberinterfaceoftheLAG.
ThenoformofthiscommandrevertstheLACPportprioritytothedefault,whichis1.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PORT-PRIORITY>
Specifiesaportpriorityvalue.Range:1to65535.
Examples
SettingaLACPportpriorityvalueof10:
| switch(config-if)# |     | lacp port-priority | 10  |
| ------------------ | --- | ------------------ | --- |
RevertingtheLACPportIDtothedefault:
| switch(config-if)#  |     | no lacp port-priority |              |
| ------------------- | --- | --------------------- | ------------ |
| Command History     |     |                       |              |
| Release             |     |                       | Modification |
| 10.07orearlier      |     |                       | --           |
| Command Information |     |                       |              |
44
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
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
| switch(config)#        | interface | lag       | 1            |
| ---------------------- | --------- | --------- | ------------ |
| switch(config-lag-if)# |           | lacp rate | slow         |
| Command History        |           |           |              |
| Release                |           |           | Modification |
| 10.07orearlier         |           |           | --           |
| Command Information    |           |           |              |
LinkAggregation|45

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp system-priority
| lacp system-priority    | <SYSTEM-PRIORITY-VALUE> |                         |     |
| ----------------------- | ----------------------- | ----------------------- | --- |
| no lacp system-priority |                         | <SYSTEM-PRIORITY-VALUE> |     |
Description
SetsaLinkAggregationControlProtocol(LACP)systempriority.
ThenoformofthiscommandsetsanLACPsystemprioritytothedefault,whichis65534.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<SYSTEM-PRIORITY-VALUE>
Specifiesasystempriorityvalue.Range:0to65535.
Examples
SettingaLinkAggregationControlProtocol(LACP)systempriorityto100:
| switch(config)# | lacp | system-priority | 100 |
| --------------- | ---- | --------------- | --- |
SettinganLACPsystemprioritytothedefault(65534):
| switch(config)# | no  | lacp system-priority |     |
| --------------- | --- | -------------------- | --- |
AmomentarytrafficdropcanbeseenincasetheLACPstatemachinemustrenegotiate.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lag
lag <ID>
no lag <ID>
Description
AddsaninterfacetoaspecifiedLAGinterfaceID.
46
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

ThenoformofthiscommandremovesaninterfacefromaspecifiedLAGinterfaceID.Themember
losesitsLACPconfigurationwhenremovedfromtheLAG.Thememberalsoreachesthedefaultstate
withanadministrativeshutdown.For6300and6400seriesswitches,theadministrativestateis
enabled.Configurations,suchasMTUandUDLD,areretained.
| Parameter |     |     | Description                            |
| --------- | --- | --- | -------------------------------------- |
| <ID>      |     |     | SpecifiesaLAGinterfaceID.Range:1to256. |
Usage
AllmembersoftheLAGmusthavethesamespeed.Ifamembercomesuplatewithadifferent
n
speed,itwillnotparticipateintheLAG/LACP.Thehardwarerestrictionisappliedbeforeaddingan
interfacetoLAG.Thememberbelongstothecardtypethathasthesamemaximumspeedasthe
referenceportcardtype.
n TomoveaninterfacefromLagAtoLagB,firstremovetheinterfacefromLagAandthenadditto
LagB.WhenamemberisattachedtoaLAG,thenondefaultconfigurationsonthememberare
removedsilently.
n AfterremovingaphysicalinterfacefromaLAG,theinterfaceassociatedwiththeLAGbecomesL3
portswithdefaultL3configurationsandadministrativedown.Forexample,supposeinterface1/1/1
waspartofLAG3andyouhadadministrativelyenabledtheinterface.Ifyoulaterremoveinterface
1/1/1fromLAG3,theadministrativestatusautomaticallychangestodown.Ifyouwanttousethe
interfaceagain,youmustadministrativelyenableitagain.
Examples
AddinganinterfacetoaLinkAggregationGroup(LAG)representedbyanIDof100:
| switch(config)#    | interface | 1/1/1   |     |
| ------------------ | --------- | ------- | --- |
| switch(config-if)# |           | lag 100 |     |
DeletinganinterfacefromaLinkAggregationGroup(LAG)representedbyanIDof100:
| switch(config)#     | interface | 1/1/1      |              |
| ------------------- | --------- | ---------- | ------------ |
| switch(config-if)#  |           | no lag 100 |              |
| Command History     |           |            |              |
| Release             |           |            | Modification |
| 10.07orearlier      |           |            | --           |
| Command Information |           |            |              |
| Platforms           | Command   | context    | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface | (LAG) |     |     |
| -------------- | ----- | --- | --- |
LinkAggregation|47

| show | interfaces | <LAG-NAME> |     | [vsx-peer] |     |     |     |
| ---- | ---------- | ---------- | --- | ---------- | --- | --- | --- |
Description
DisplaysinformationaboutaspecificLAG.
| Parameter  |     |     |     |     | Description        |     |     |
| ---------- | --- | --- | --- | --- | ------------------ | --- | --- |
| <LAG-NAME> |     |     |     |     | SpecifiesaLAGname. |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
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
|                | Packets   |             |     |     | 20           | 45   | 65   |
| -------------- | --------- | ----------- | --- | --- | ------------ | ---- | ---- |
|                | Unicast   |             |     |     | 5            | 5    | 10   |
|                | Multicast |             |     |     | 5            | 15   | 20   |
|                | Broadcast |             |     |     | 10           | 25   | 35   |
|                | Bytes     |             |     |     | 5658         | 2584 | 8242 |
|                | Jumbos    |             |     |     | 0            | 0    | 0    |
|                | Dropped   |             |     |     | 0            | 0    | 0    |
|                | Filtered  |             |     |     | 0            | 0    | 0    |
|                | Pause     | Frames      |     |     | 0            | 0    | 0    |
|                | Errors    |             |     |     | 0            | 0    | 0    |
|                | CRC/FCS   |             |     |     | 0            | n/a  | 0    |
|                | Collision |             |     |     | n/a          | 0    | 0    |
|                | Runts     |             |     |     | 0            | n/a  | 0    |
|                | Giants    |             |     |     | 0            | n/a  | 0    |
| Command        |           | History     |     |     |              |      |      |
| Release        |           |             |     |     | Modification |      |      |
| 10.07orearlier |           |             |     |     | --           |      |      |
| Command        |           | Information |     |     |              |      |      |
48
| AOS-CX10.09LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- |

| Platforms |     | Command |     | context | Authority |     |
| --------- | --- | ------- | --- | ------- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show      | lacp       | aggregates |              | (LAG) |            |     |
| --------- | ---------- | ---------- | ------------ | ----- | ---------- | --- |
| show lacp | aggregates |            | [<LAG-NAME>] |       | [vsx-peer] |     |
Description
DisplaysallLACPaggregateinformationconfiguredforallLAGs,orforaspecificLAG.
| Parameter  |     |     |     |     | Description                 |     |
| ---------- | --- | --- | --- | --- | --------------------------- | --- |
| <LAG-NAME> |     |     |     |     | Optional:Specifiesalagname. |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingLACPaggregateinformationconfiguredforlag10:
| switch#               |     | show lacp | aggregates |              | lag10 |     |
| --------------------- | --- | --------- | ---------- | ------------ | ----- | --- |
| Aggregate-name        |     |           |            | : lag10      |       |     |
| Aggregated-interfaces |     |           |            | : 1/1/1      | 1/1/2 |     |
| Heartbeat             |     | rate      |            | : slow       |       |     |
| Hash                  |     |           |            | : l3-src-dst |       |     |
| Aggregate             |     | mode      |            | : active     |       |     |
DisplayingLACPaggregates:
| switch#               |         | show lacp | aggregates |              |        |        |
| --------------------- | ------- | --------- | ---------- | ------------ | ------ | ------ |
| Aggregate-name        |         |           |            | : lag1       |        |        |
| Aggregated-interfaces |         |           |            | : 1/1/27     | 1/1/28 | 1/1/29 |
| Heartbeat             |         | rate      |            | : slow       |        |        |
| Hash                  |         |           |            | : l3-src-dst |        |        |
| Aggregate             |         | mode      |            | : active     |        |        |
| Aggregate-name        |         |           |            | : lag2       |        |        |
| Aggregated-interfaces |         |           |            | : 1/1/48     |        |        |
| Heartbeat             |         | rate      |            | : slow       |        |        |
| Hash                  |         |           |            | : l2-src-dst |        |        |
| Aggregate             |         | mode      |            | : passive    |        |        |
| Command               | History |           |            |              |        |        |
LinkAggregation|49

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show      | lacp configuration |            |     |
| --------- | ------------------ | ---------- | --- |
| show lacp | configuration      | [vsx-peer] |     |
Description
DisplaysglobalLACPconfiguration.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingglobalLACPconfiguration(outputisapplicablefor8400seriesswitches):
| switch#         | show lacp   | configuration     |     |
| --------------- | ----------- | ----------------- | --- |
| System-id       | :           | 70:72:cf:ef:fc:d9 |     |
| System-priority | :           | 65534             |     |
| Hash            | :l3-src-dst |                   |     |
DisplayingglobalLACPconfiguration(outputisapplicablefor8320,6300,and6400seriesswitches):
switch#
|                 | show lacp   | configuration     |              |
| --------------- | ----------- | ----------------- | ------------ |
| System-id       | :           | 98:f2:b3:68:40:a0 |              |
| System-priority | :           | 65534             |              |
| Command         | History     |                   |              |
| Release         |             |                   | Modification |
| 10.07orearlier  |             |                   | --           |
| Command         | Information |                   |              |
50
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

| Platforms |     | Command |     | context |     | Authority |     |     |     |     |
| --------- | --- | ------- | --- | ------- | --- | --------- | --- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show      | lacp       | interfaces |            |     |            |     |     |     |     |     |
| --------- | ---------- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
| show lacp | interfaces |            | [<IFNAME>] |     | [vsx-peer] |     |     |     |     |     |
Description
DisplaysanLACPconfigurationofthephysicalinterfaces,includingVSXs.Ifaninterfacenameispassed
asargument,itonlydisplaysanLACPconfigurationofaspecifiedinterface.
| Parameter |     |     |     |     |     | Description                        |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
| <IFNAME>  |     |     |     |     |     | Optional:Specifiesaninterfacename. |     |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ThisexampledisplaysanLACPconfigurationofthephysicalinterfaces.Oneoftheinterfaceshasthe
lacp-blockforwardingstate.IfaVSXswitchhasloopprotectenabledonaninterfaceandaloopoccurs,
VSXblockstheinterfacetostoptheloop.Theforwardingstateoftheblockedinterfaceissettolacp-
block.
| switch# |               | show lacp | interfaces |                |     |     |            |          |            |     |
| ------- | ------------- | --------- | ---------- | -------------- | --- | --- | ---------- | -------- | ---------- | --- |
| State   | abbreviations |           |            | :              |     |     |            |          |            |     |
| A -     | Active        |           | P          | - Passive      |     | F - | Aggregable | I -      | Individual |     |
| S -     | Short-timeout |           | L          | - Long-timeout |     | N - | InSync     | O -      | OutofSync  |     |
| C -     | Collecting    |           | D          | - Distributing |     |     |            |          |            |     |
| X -     | State         | m/c       | expired    |                |     | E - | Default    | neighbor | state      |     |
| Actor   | details       |           | of all     | interfaces:    |     |     |            |          |            |     |
----------------------------------------------------------------------------------
--
| Intf | Aggr |     | Port | Port | State | System-id |     |     | System Aggr | Forwarding |
| ---- | ---- | --- | ---- | ---- | ----- | --------- | --- | --- | ----------- | ---------- |
|      | name |     | id   | Pri  |       |           |     |     | Pri Key     | State      |
----------------------------------------------------------------------------------
--
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
LinkAggregation|51

| 1/1/3 | lag128 |     | 14 1 |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
| ----- | ------ | --- | ---- | --- | ------ | ----------------- | --- | ----- | --- |
1/1/4 lag128
1/1/5 lag20
DisplayingstaticLAG:
| switch# | show          | lacp        | interfaces       |     |     |              |          |              |     |
| ------- | ------------- | ----------- | ---------------- | --- | --- | ------------ | -------- | ------------ | --- |
| State   | abbreviations |             | :                |     |     |              |          |              |     |
| A -     | Active        |             | P - Passive      |     | F   | - Aggregable | I        | - Individual |     |
| S -     | Short-timeout |             | L - Long-timeout |     | N   | - InSync     | O        | - OutofSync  |     |
| C -     | Collecting    |             | D - Distributing |     |     |              |          |              |     |
| X -     | State         | m/c expired |                  |     | E   | - Default    | neighbor | state        |     |
| Actor   | details       | of          | all interfaces:  |     |     |              |          |              |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State |     | System-id |     | System Aggr | Forwarding |
| ---- | ---- | ---- | ---- | ----- | --- | --------- | --- | ----------- | ---------- |
|      | Name | Id   | Pri  |       |     |           |     | Pri Key     | State      |
------------------------------------------------------------------------------
| 1/1/1   | lag10   |     |                    |     |     |     |     |     | up  |
| ------- | ------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
| 1/1/2   | lag10   |     |                    |     |     |     |     |     | up  |
| Partner | details |     | of all interfaces: |     |     |     |     |     |     |
------------------------------------------------------------------------------
| Intf | Aggr | Port | Port | State |     | System-id |     | System Aggr |     |
| ---- | ---- | ---- | ---- | ----- | --- | --------- | --- | ----------- | --- |
|      | Name | Id   | Pri  |       |     |           |     | Pri Key     |     |
------------------------------------------------------------------------------
1/1/1 lag10
1/1/2 lag10
DisplayinganLACPconfigurationofthe1/1/1interface:
| switch#        | show          | lacp        | interfaces       | 1/1/1 |     |              |          |              |     |
| -------------- | ------------- | ----------- | ---------------- | ----- | --- | ------------ | -------- | ------------ | --- |
| State          | abbreviations |             | :                |       |     |              |          |              |     |
| A -            | Active        |             | P - Passive      |       | F   | - Aggregable | I        | - Individual |     |
| S -            | Short-timeout |             | L - Long-timeout |       | N   | - InSync     | O        | - OutofSync  |     |
| C -            | Collecting    |             | D - Distributing |       |     |              |          |              |     |
| X -            | State         | m/c expired |                  |       | E   | - Default    | neighbor | state        |     |
| Aggregate-name |               |             | : lag1           |       |     |              |          |              |     |
-------------------------------------------------
|     |     |     | Actor |     |     | Partner |     |     |     |
| --- | --- | --- | ----- | --- | --- | ------- | --- | --- | --- |
-------------------------------------------------
| Port-id         |     |     | | 28                |     |     | | 31                |     |     |     |
| --------------- | --- | --- | ------------------- | --- | --- | ------------------- | --- | --- | --- |
| Port-priority   |     |     | | 1                 |     |     | | 1                 |     |     |     |
| Key             |     |     | | 1                 |     |     | | 1                 |     |     |     |
| State           |     |     | | ALFNCD            |     |     | | ALFNCD            |     |     |     |
| System-id       |     |     | | 98:f2:b3:68:40:a0 |     |     | | 98:f2:b3:68:60:a6 |     |     |     |
| System-priority |     |     | | 65534             |     |     | | 65534             |     |     |     |
DisplayinganLACPconfigurationafterloop-protectisenabledontheprimaryVSXswitch:
| switch# | show          | lacp | interfaces  |     |     |              |     |              |     |
| ------- | ------------- | ---- | ----------- | --- | --- | ------------ | --- | ------------ | --- |
| State   | abbreviations |      | :           |     |     |              |     |              |     |
| A -     | Active        |      | P - Passive |     | F   | - Aggregable | I   | - Individual |     |
52
AOS-CX10.09LinkAggregationGuide| (4100i,6xxx,8xxxSwitchSeries)

| S - Short-timeout | L - Long-timeout | N - InSync | O - | OutofSync |     |
| ----------------- | ---------------- | ---------- | --- | --------- | --- |
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
| switch# | show lacp interfaces |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- |
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
| 1/3/2          | lag1(mc) 131 1 | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 |     |
| -------------- | -------------- | ------------------------ | --- | ------- | --- |
| 1/9/3          | lag2(mc)       |                          |     |         |     |
| Command        | History        |                          |     |         |     |
| Release        |                | Modification             |     |         |     |
| 10.07orearlier |                | --                       |     |         |     |
| Command        | Information    |                          |     |         |     |
LinkAggregation|53

| Platforms | Command |     | context | Authority |
| --------- | ------- | --- | ------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| shutdown | (interface |     | lag) |     |
| -------- | ---------- | --- | ---- | --- |
shutdown
no shutdown
Description
SetseveryinterfaceintheLAGoperationallydown.
Thenoformofthiscommandsetseveryinterfaceoperationallyup.
Examples
SettingeveryinterfaceintheLAGtoshutdown:
| switch(config)#        |     | interface | lag 1    |     |
| ---------------------- | --- | --------- | -------- | --- |
| switch(config-lag-if)# |     |           | shutdown |     |
ResettingeveryinterfaceintheLAGtothedefault(up):
| switch(config)#        |             | interface | lag 1       |              |
| ---------------------- | ----------- | --------- | ----------- | ------------ |
| switch(config-lag-if)# |             |           | no shutdown |              |
| Command                | History     |           |             |              |
| Release                |             |           |             | Modification |
| 10.07orearlier         |             |           |             | --           |
| Command                | Information |           |             |              |
| Platforms              | Command     |           | context     | Authority    |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| vlan trunk    | native | (LAG)       |     |     |
| ------------- | ------ | ----------- | --- | --- |
| vlan trunk    | native | <VLAN-ID>   |     |     |
| no vlan trunk | native | [<VLAN-ID>] |     |     |
Description
AssignsanativeVLANIDtoaLAGinterface.
ThenoformofthiscommandremovesanativeVLANfromaLAGinterfaceandassignsVLANID1asits
nativeVLAN.
54
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-ID> SpecifiesthenumberoftheVLANIDtoassign.TheVLANIDmust
exist.
MaximumnumberofVLANssupported:512(4100i)
MaximumnumberofVLANssupported:512(6000and6100)
MaximumnumberofVLANssupported:2048(6200)
MaximumnumberofVLANssupported:4096(6300,6400)
MaximumnumberofVLANssupported:4096(8320)
MaximumnumberofVLANssupported:4096(8325)
MaximumnumberofVLANssupported:4096(8360)
MaximumnumberofVLANssupported:4096(8400)
VLANIDrange:2to4094.
Usage
Bydefault,VLANID1isassignedastheLAGVLANIDforallLAGinterfaces.VLANscanonlybeassigned
toanonrouted(layer2)interfaceorLAGinterface.
OnlyoneVLANIDcanbeassignedasthenativeVLAN.FortheinterfacetoforwardthenativeVLAN
traffic,theinterfacehastobeallowedexplicitlybyenteringvlan trunk allowed <ID>wheretheIDis
thenativeVLANID.Thissettingisalsoapplicabletothephysicalinterface.
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
LinkAggregation|55

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
| Command History        |           |         |              |
| Release                |           |         | Modification |
| 10.07orearlier         |           |         | --           |
| Command Information    |           |         |              |
| Platforms              | Command   | context | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-lag-if |     | forthiscommand. |
| --- | ------------- | --- | --------------- |
56
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

Chapter 3

Smartlink

Smartlink

Smartlink is available only on the 6200, 6300, 6400, and 8360 Switch Series.

Smartlink provides simple and fast-converging link redundancy in network topologies with dual uplink
between different layers of the network. It requires an active (primary) and backup (secondary) link. The
active link carries the traffic. If the active link fails, a switchover is triggered and the traffic is directed to
the backup link.

The active interface forwards traffic for a group of VLANs (referred to as protected VLAN group). The
secondary interface is in backup mode for this protected group. If the active port goes down, the backup
port starts forwarding traffic for the protected VLAN group. If the active port recovers, it switches to
backup mode and does not forward traffic. Secondary port continues forwarding traffic.

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

n On switches with both Smartlink and STP enabled, loops involving Smartlink and STP are not

detected.

n On switches with both Smartlink and ERPS enabled, loops involving Smartlink and ERPS are not

detected.

n ERPS and Smartlink cannot be enabled on the same port.

n Dynamic VLANs (MVRP) and Smartlink cannot be enabled on the same port.

n Loop Protect and Smartlink cannot be enabled on the same port.

n Multicast fast convergence is not supported.

n Uplink Failure Detection (UFD) is not supported.

n MIB and WebUI are not supported.

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

57

n VLANsthatincludeSmartlinkportsmustbeincludedintheprotectedVLANlistofatleastoneSmartlink
group.IfaVLANincludesSmartlinkportsandisnotincludedintheprotectedVLANlist,theVLAN-port
combinationwillnotbemanagedbySmartlinkorSTP,resultinginanundefinedportstatefortheVLAN,
whichwillcausealoopinthenetwork.
n WhenusingUDLDwithSmartlinks,redundancyswitchoverisnothitlessandwillresultintrafficloss.
| Smartlink       | commands         |     |     |
| --------------- | ---------------- | --- | --- |
| Configuration   | commands         |     |     |
| smartlink group |                  |     |     |
| smartlink group | <GROUP-ID>       |     |     |
| no smartlink    | group <GROUP-ID> |     |     |
Description
CreatesaSmartlinkgroupwithspecifiedID.
ThenoformofthiscommandremovestheSmartlinkgroupandallassociatedconfigurationsfora
specifiedID.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<GROUP-ID>
SpecifiesIDfortheSmartlinkgroup.
Usage
ThemaximumnumberofSmartlinkgroupsis24.
Examples
ConfiguringaSmartlinkgroup:
| switch(config)# | smartlink | group | 2   |
| --------------- | --------- | ----- | --- |
switch(config-smartlink-2)#
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
6400
8360
Smartlink|58

| smartlink    | recv-control-vlan |                   |     |            |     |     |
| ------------ | ----------------- | ----------------- | --- | ---------- | --- | --- |
| smartlink    | recv-control-vlan |                   |     | <VID-LIST> |     |     |
| no smartlink |                   | recv-control-vlan |     | <VID-LIST> |     |     |
Description
ConfigurescontrolVLANstoreceiveflushmessages.
ThenoformofthiscommanddisablesVLANsfromreceivingflushmessages.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<VID-LIST>
SpecifiesVLANID.
Usage
n ConfigurethiscommandonuplinkdeviceswhereMACflushisrequired.
AflushmessageclearsstaleMAC andARP entriesenablingfasttrafficconvergence.
n
Examples
ConfiguringcontrolVLANtoreceiveflushmessages:
| switch(config)# |             | smartlink |     | recv-control-vlan |              | 2,3 |
| --------------- | ----------- | --------- | --- | ----------------- | ------------ | --- |
| Command         | History     |           |     |                   |              |     |
| Release         |             |           |     |                   | Modification |     |
| 10.07orearlier  |             |           |     |                   | --           |     |
| Command         | Information |           |     |                   |              |     |
| Platforms       |             | Command   |     | context           | Authority    |     |
6200 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6300 |     |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --- | --------------- | --- |
6400
8360
| Group       | context | commands   |        |     |     |     |
| ----------- | ------- | ---------- | ------ | --- | --- | --- |
| description |         | (smartlink | group) |     |     |     |
| description |         | <DESC>     |        |     |     |     |
no description
Description
AddsdescriptiontoaSmartlinkgroup.
ThenoformofthiscommandremovesadescriptionfromaSmartlinkgroup.
59
| AOS-CX10.09LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- | --- |

| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<DESC> SpecifiesdescriptionforaSmartlinkgroup.1to64printableASCII
charactersareallowed.
Examples
AddingadescriptiontoaSmartlinkgroup:
| switch(config)#             | smartlink | group 3      |           |     |
| --------------------------- | --------- | ------------ | --------- | --- |
| switch(config-smartlink-3)# |           | Description  | for group | 3   |
| Command History             |           |              |           |     |
| Release                     |           | Modification |           |     |
| 10.07orearlier              |           | --           |           |     |
| Command Information         |           |              |           |     |
| Platforms                   | Command   | context      | Authority |     |
6200 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
executionrightsforthiscommand.
6300
6400
8360
primary-port
| primary-port | <INTERFACE-NAME> |     |     |     |
| ------------ | ---------------- | --- | --- | --- |
no primary-port
Description
ConfiguresprimaryportforaSmartlinkgroup.
ThenoformofthiscommandremovesprimaryportfromaSmartlinkgroup.
| Parameter        |     | Description                       |     |     |
| ---------------- | --- | --------------------------------- | --- | --- |
| <INTERFACE-NAME> |     | Specifiesinterfaceforprimaryport. |     |     |
Examples
ConfiguringprimaryportforaSmartlinkgroup:
| switch(config)#             | smartlink | group 3      |       |     |
| --------------------------- | --------- | ------------ | ----- | --- |
| switch(config-smartlink-3)# |           | primary-port | 1/1/1 |     |
| Command History             |           |              |       |     |
Smartlink|60

| Release             |         |         | Modification |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6200 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6300 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6400
8360
| smartlink group | secondary-port   |     |     |     |
| --------------- | ---------------- | --- | --- | --- |
| secondary-port  | <INTERFACE-NAME> |     |     |     |
no secondary-port
Description
ConfiguressecondaryportforaSmartlinkgroup.
ThenoformofthiscommandremovessecondaryportfromaSmartlinkgroup.
| Parameter        |     |     | Description                         |     |
| ---------------- | --- | --- | ----------------------------------- | --- |
| <INTERFACE-NAME> |     |     | Specifiesinterfaceforsecondaryport. |     |
Examples
ConfiguringsecondaryportforaSmartlinkgroup:
| switch(config)#             | smartlink |         | group 3        |           |
| --------------------------- | --------- | ------- | -------------- | --------- |
| switch(config-smartlink-3)# |           |         | secondary-port | 1/1/2     |
| Command History             |           |         |                |           |
| Release                     |           |         | Modification   |           |
| 10.07orearlier              |           |         | --             |           |
| Command Information         |           |         |                |           |
| Platforms                   | Command   | context |                | Authority |
config-smartlink-<GROUP>
| 6200 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
| 6300 |     |     |     | executionrightsforthiscommand.            |
6400
8360
control-vlan
| control-vlan    | <VLAN-ID> |     |     |     |
| --------------- | --------- | --- | --- | --- |
| no control-vlan | <VLAN-ID> |     |     |     |
61
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

Description
ConfigurescontrolVLANinaSmartlinkgroup.
ThenoformofthiscommandremovescontrolVLANfromaSmartlinkgroup.
| Parameter |     |     | Description                        |     |
| --------- | --- | --- | ---------------------------------- | --- |
| <VLAN-ID> |     |     | SpecifiesVLANIDforaSmartlinkgroup. |     |
Usage
n InaSmartlinkgroup,thecontrolVLAN isusedtosendflushmessages.
n ControlVLANisconfiguredonthedeviceintendedtosendflushmessages.
n EachSmartlinkgroupmustuseauniquecontrolVLAN.
n ControlVLANisprotectedintheSmartlinkgrouptoavoidloops.
Examples
ConfiguringcontrolVLAN inaSmartlinkgroup:
| switch(config)#             | smartlink |         | group 3      |           |
| --------------------------- | --------- | ------- | ------------ | --------- |
| switch(config-smartlink-3)# |           |         | control-vlan | 10        |
| Command History             |           |         |              |           |
| Release                     |           |         | Modification |           |
| 10.07orearlier              |           |         | --           |           |
| Command Information         |           |         |              |           |
| Platforms                   | Command   | context |              | Authority |
6200 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6300 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6400
8360
protected-vlans
| protected-vlans    | <VLAN-ID-LIST> |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
| no protected-vlans | <VLAN-ID-LIST> |     |     |     |
Description
SpecifiesVLANsprotectedbyaSmartlinkgroup.
ThenoformofthiscommandremovesVLANsprotectedbyaSmartlinkgroup.
| Parameter      |     |     | Description                            |     |
| -------------- | --- | --- | -------------------------------------- | --- |
| <VLAN-ID-LIST> |     |     | SpecifieslistofVLANIDs.Rangeis1to4094. |     |
Examples
Smartlink|62

ConfiguringprotectedVLANsforaSmartlinkgroup.:
| switch(config)#             | smartlink |         | group 3         |           |
| --------------------------- | --------- | ------- | --------------- | --------- |
| switch(config-smartlink-3)# |           |         | protected-vlans | 1, 10-50  |
| Command History             |           |         |                 |           |
| Release                     |           |         | Modification    |           |
| 10.07orearlier              |           |         | --              |           |
| Command Information         |           |         |                 |           |
| Platforms                   | Command   | context |                 | Authority |
6200 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6300 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6400
8360
preemption
preemption
no preemption
Description
ConfigurespreemptioninaSmartlinkgroup.
ThenoformofthiscommanddisablespreemptioninaSmartlinkgroup.
Usage
n Ifpreemptionisenabled,arecoveredprimaryportpreemptstheactiveinterfaceaftertheconfigured
preemptiondelay.
n Ifpreemptionisdisabled,arecoveredprimaryportservesasabackupinterfaceanddoesnot
forwardtraffic.
Examples
ConfiguringpreemptioninaSmartlinkgroup:
| switch(config)#             | smartlink |     | group 3      |     |
| --------------------------- | --------- | --- | ------------ | --- |
| switch(config-smartlink-3)# |           |     | preemption   |     |
| Command History             |           |     |              |     |
| Release                     |           |     | Modification |     |
| 10.07orearlier              |           |     | --           |     |
| Command Information         |           |     |              |     |
63
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6200 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6300 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6400
8360
preemption-delay
| preemption-delay | <SECONDS> |     |     |     |
| ---------------- | --------- | --- | --- | --- |
no preemption-delay
Description
SpecifiespreemptiondelayforaSmartlinkgroup.
ThenoformofthiscommandremovespreviouslyconfiguredpreemptiondelayfromaSmartlinkgroup
andsetsittothedefaultof1second.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<SECONDS> Specifiespreemptiondelayinseconds.Rangeis0to300seconds.
Usage
Whenpreemptionisenabled,arecoveredprimaryportalwayspreemptstheactiveinterfaceafterthe
configuredpreemptiondelay.
Examples
ConfiguringpreemptiondelayonaSmartlinkgroup:
| switch(config)#             | smartlink |         | group 3          |           |
| --------------------------- | --------- | ------- | ---------------- | --------- |
| switch(config-smartlink-3)# |           |         | preemption       |           |
| switch(config-smartlink-3)# |           |         | preemption-delay | 10        |
| Command History             |           |         |                  |           |
| Release                     |           |         | Modification     |           |
| 10.07orearlier              |           |         | --               |           |
| Command Information         |           |         |                  |           |
| Platforms                   | Command   | context |                  | Authority |
6200 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6300 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6400
8360
| Display commands |                  |     |     |     |
| ---------------- | ---------------- | --- | --- | --- |
| show smartlink   | group            |     |     |     |
| show smartlink   | group <GROUP-ID> |     |     |     |
Smartlink|64

Description
ShowsinformationforaspecificSmartlinkgroup.
| Parameter  |     |     |     |     | Description                |     |     |     |
| ---------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
| <GROUP-ID> |     |     |     |     | SpecifiesSmartlinkgroupID. |     |     |     |
Examples
ShowingSmartlinkgroupinformation:
| switch#   |     | show smartlink |                | group 1 |     |     |     |     |
| --------- | --- | -------------- | -------------- | ------- | --- | --- | --- | --- |
| Smartlink |     | Group          | 1 Information: |         |     |     |     |     |
=============================
| Group      | description |       |       | : Uplink1 |       |            |      |     |
| ---------- | ----------- | ----- | ----- | --------- | ----- | ---------- | ---- | --- |
| Protected  |             | VLANs |       | : 20-30   |       |            |      |     |
| Control    |             | VLAN  |       | : 10      |       |            |      |     |
| Preemption |             |       |       | : ON      |       |            |      |     |
| Preemption |             | Delay |       | : 10      |       |            |      |     |
| Ports      | Role        |       | State | Flush     | Count | Last Flush | Time |     |
------ --------- ---------- ----------- -------------------------
| 1/1/1          | Primary   |             | Active | 2       |              | Sat Oct | 17 19:09:10 | 2020 |
| -------------- | --------- | ----------- | ------ | ------- | ------------ | ------- | ----------- | ---- |
| 1/1/2          | Secondary |             | Backup | 0       |              |         |             |      |
| Command        |           | History     |        |         |              |         |             |      |
| Release        |           |             |        |         | Modification |         |             |      |
| 10.07orearlier |           |             |        |         | --           |         |             |      |
| Command        |           | Information |        |         |              |         |             |      |
| Platforms      |           | Command     |        | context | Authority    |         |             |      |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6300 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6400 |     |     |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
| ---- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
8360
| show | smartlink | group |     | all |     |     |     |     |
| ---- | --------- | ----- | --- | --- | --- | --- | --- | --- |
| show | smartlink | group | all |     |     |     |     |     |
Description
ShowsinformationforallconfiguredSmartlinkgroups.
Examples
ShowinginformationforallconfiguredSmartlinkgroups:
| switch#   |     | show smartlink |              | group all |     |     |     |     |
| --------- | --- | -------------- | ------------ | --------- | --- | --- | --- | --- |
| Smartlink |     | Group          | Information: |           |     |     |     |     |
=============================
|     | Primary | Secondary |     | Active | Backup | Ctrl | Preemption | Preemption |
| --- | ------- | --------- | --- | ------ | ------ | ---- | ---------- | ---------- |
65
| AOS-CX10.09LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |

| Grp Port | Port | Port | Port | Vlan |     | Delay |
| -------- | ---- | ---- | ---- | ---- | --- | ----- |
---- ------- --------- ------ ------- --------- ---------- ----------
| 1 1/1/1        | 1/1/2       | 1/1/1   | 1/1/2                                                | 10  | OFF | 1   |
| -------------- | ----------- | ------- | ---------------------------------------------------- | --- | --- | --- |
| 2 1/1/5        | 1/1/6       | 1/1/5   | 1/1/6                                                | 11  | OFF | 1   |
| Command        | History     |         |                                                      |     |     |     |
| Release        |             |         | Modification                                         |     |     |     |
| 10.07orearlier |             |         | --                                                   |     |     |     |
| Command        | Information |         |                                                      |     |     |     |
| Platforms      | Command     | context | Authority                                            |     |     |     |
| 6200           |             |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |     |
Operator(>)orManager
6300 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6400 |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- | --- |
8360
| show smartlink | group        | detail |     |     |     |     |
| -------------- | ------------ | ------ | --- | --- | --- | --- |
| show smartlink | group detail |        |     |     |     |     |
Description
ShowsdetailedinformationforallconfiguredSmartlinkgroups.
Examples
ShowingdetailedinformationforallconfiguredSmartlinkgroups:
| switch#   | show smartlink | group        | detail |     |     |     |
| --------- | -------------- | ------------ | ------ | --- | --- | --- |
| Smartlink | Group 1        | Information: |        |     |     |     |
===============================
| Protected  | VLAN  |       | : 1-3 |       |            |      |
| ---------- | ----- | ----- | ----- | ----- | ---------- | ---- |
| Control    | VLAN  |       | : 1   |       |            |      |
| Preemption |       |       | : OFF |       |            |      |
| Preemption | Delay |       | : 1   |       |            |      |
| Ports      | Role  | State | Flush | Count | Last Flush | Time |
-------- ------------ ------------ ------------ ------------------------
| 1/3/1     | Primary   | Backup       | 0   |     |     |     |
| --------- | --------- | ------------ | --- | --- | --- | --- |
| 1/3/2     | Secondary | Active       | 0   |     |     |     |
| Smartlink | Group 2   | Information: |     |     |     |     |
===============================
| Protected  | VLAN  |       | : 4-6 |       |            |      |
| ---------- | ----- | ----- | ----- | ----- | ---------- | ---- |
| Control    | VLAN  |       | : 4   |       |            |      |
| Preemption |       |       | : OFF |       |            |      |
| Preemption | Delay |       | : 1   |       |            |      |
| Ports      | Role  | State | Flush | Count | Last Flush | Time |
-------- ------------ ------------ ------------ ------------------------
| 1/3/2   | Primary   | Active | 0   |     |     |     |
| ------- | --------- | ------ | --- | --- | --- | --- |
| 1/3/1   | Secondary | Backup | 0   |     |     |     |
| Command | History   |        |     |     |     |     |
Smartlink|66

| Release        |             |         | Modification |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 6300 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| ---- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
(#)
commandfromtheoperatorcontext(>)only.
6400
8360
| show smartlink | flush-statistics |     |     |     |     |     |
| -------------- | ---------------- | --- | --- | --- | --- | --- |
| show smartlink | flush-statistics |     |     |     |     |     |
Description
Showsinformationforreceivedflushmessages.
Usage
Thiscommandmustbeexecutedonanuplinkorpeerdeviceconfiguredwithrecv-control-vlan.
Examples
Showinginformationforreceivedflushmessages:
| switch#    | show smartlink | flush-statistics |     |     |     |     |
| ---------- | -------------- | ---------------- | --- | --- | --- | --- |
| Last Flush | Packet         | Detail:          |     |     |     |     |
========================
| Flush Packets  | Received     |                       |              | : 2             |             |      |
| -------------- | ------------ | --------------------- | ------------ | --------------- | ----------- | ---- |
| Last Flush     | Packet       | Received On Interface |              | : 1/1/1         |             |      |
| Last Flush     | Packet       | Received On           |              | : Sat Oct       | 17 19:09:10 | 2020 |
| Device         | Id Of Last   | Flush Packet          | Received     | : 5065f3-127080 |             |      |
| Control        | VLAN Of Last | Flush Packet          | Received     | : 10            |             |      |
| Command        | History      |                       |              |                 |             |      |
| Release        |              |                       | Modification |                 |             |      |
| 10.07orearlier |              |                       | --           |                 |             |      |
| Command        | Information  |                       |              |                 |             |      |
| Platforms      | Command      | context               | Authority    |                 |             |      |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6300 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6400 |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- | --- |
8360
| clear smartlink | group | statistics |     |     |     |     |
| --------------- | ----- | ---------- | --- | --- | --- | --- |
67
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |

| clear smartlink | group | [<GROUP-ID>] | statistics |
| --------------- | ----- | ------------ | ---------- |
Description
ClearsSmartlinkstatisticsforthespecifiedSmartlinkgrouporallSmartlinkgroups.
| Parameter  |     |     | Description              |
| ---------- | --- | --- | ------------------------ |
| <GROUP-ID> |     |     | SpecifiesSmartlinkgroup. |
Examples
ClearingSmartlinkstatisticsforaspecifiedSmartlinkgroup:
| switch# | clear smartlink | group | 1 statistics |
| ------- | --------------- | ----- | ------------ |
ClearingallSmartlinkstatisticsforallSmartlinkgroups:
| switch(config)#     | clear   | smartlink | group statistics |
| ------------------- | ------- | --------- | ---------------- |
| Command History     |         |           |                  |
| Release             |         |           | Modification     |
| 10.07orearlier      |         |           | --               |
| Command Information |         |           |                  |
| Platforms           | Command | context   | Authority        |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
| 6300 | (#) |     |                                       |
| ---- | --- | --- | ------------------------------------- |
| 6400 |     |     | commandfromtheoperatorcontext(>)only. |
8360
| clear smartlink | flush-statistics |     |     |
| --------------- | ---------------- | --- | --- |
| clear smartlink | flush-statistics |     |     |
Description
ClearsSmartlinkflushstatistics.
Usage
Thiscommandmustbeexecutedontheuplinkdeviceconfiguredwithrecv-control-vlan.
Examples
ClearingSmartlinkflushstatistics:
| switch#         | clear smartlink | flush-statistics |     |
| --------------- | --------------- | ---------------- | --- |
| Command History |                 |                  |     |
Smartlink|68

| Release             |         |         |     | Modification |     |
| ------------------- | ------- | ------- | --- | ------------ | --- |
| 10.07orearlier      |         |         |     | --           |     |
| Command Information |         |         |     |              |     |
| Platforms           | Command | context |     | Authority    |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 6300 |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- |
(#)
commandfromtheoperatorcontext(>)only.
6400
8360
show running-config
show running-config
Description
Showscurrentrunningconfiguration.
Examples
Showingcurrentlyrunningconfiguration:
| switch#                     | configure           | terminal |                  |     |         |
| --------------------------- | ------------------- | -------- | ---------------- | --- | ------- |
| switch(config)#             | smartlink           |          | group            | 1   |         |
| switch(config-smartlink-1)# |                     |          | description      |     | Uplink1 |
| switch(config-smartlink-1)# |                     |          | primary-port     |     | 1/1/1   |
| switch(config-smartlink-1)# |                     |          | secondary-port   |     | 1/1/2   |
| switch(config-smartlink-1)# |                     |          | control-vlan     |     | 10      |
| switch(config-smartlink-1)# |                     |          | protected-vlans  |     | 20-30   |
| switch(config-smartlink-1)# |                     |          | preemption       |     |         |
| switch(config-smartlink-1)# |                     |          | preemption-delay |     | 10      |
| switch(config)#             | smartlink           |          | group            | 2   |         |
| switch(config-smartlink-2)# |                     |          | primary-port     |     | 1/1/8   |
| switch(config-smartlink-2)# |                     |          | secondary-port   |     | 1/1/9   |
| switch(config-smartlink-2)# |                     |          | control-vlan     |     | 11      |
| switch(config-smartlink-2)# |                     |          | protected-vlans  |     | 20-30   |
| switch#                     | show running-config |          |                  |     |         |
| Current                     | configuration:      |          |                  |     |         |
!
!
!
| smart-link      | group 1 |       |     |     |     |
| --------------- | ------- | ----- | --- | --- | --- |
| primary-port    | 1/1/1   |       |     |     |     |
| secondary-port  | 1/1/2   |       |     |     |     |
| control-vlan    | 10      |       |     |     |     |
| protected-vlans |         | 20-30 |     |     |     |
preemption
| preemption-delay |     | 10  |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
exit
| smart-link      | group 2 |       |     |     |     |
| --------------- | ------- | ----- | --- | --- | --- |
| primary-port    | 1/1/8   |       |     |     |     |
| secondary-port  | 1/1/9   |       |     |     |     |
| control-vlan    | 11      |       |     |     |     |
| protected-vlans |         | 20-30 |     |     |     |
exit
| Command History |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
69
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- |

| Release        |             |         |         |     | Modification |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
6200 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 6300 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
(#)
commandfromtheoperatorcontext(>)only.
6400
8360
| Supportability  |     | commands  |     |      |                   |           |     |
| --------------- | --- | --------- | --- | ---- | ----------------- | --------- | --- |
| show capacities |     | smartlink |     |      |                   |           |     |
| show capacities |     | smartlink | |   | show | capacities-status | smartlink |     |
Description
ShowsSmartlinkcapacitiesorSmartlinkcapacitiesandstatus.
Examples
ShowingSmartlinkcapacities:
| switch#    | show        | capacities | smartlink |           |     |     |     |
| ---------- | ----------- | ---------- | --------- | --------- | --- | --- | --- |
| System     | Capacities: |            | Filter    | SMARTLINK |     |     |     |
| Capacities | Name        |            |           |           |     |     |     |
Value
----------------------------------------------------------------------------------
--
| Maximum | number | of  | SMARTLINK | GROUPS | configurable | in a system |     |
| ------- | ------ | --- | --------- | ------ | ------------ | ----------- | --- |
24
ShowingSmartlinkcapacitiesandstatus:
| switch#    | show       | capacities-status |         |        | smartlink |     |       |
| ---------- | ---------- | ----------------- | ------- | ------ | --------- | --- | ----- |
| System     | Capacities |                   | Status: | Filter | SMARTLINK |     |       |
| Capacities | Status     |                   | Name    |        |           |     | Value |
Maximum
----------------------------------------------------------------------------------
--
| Number | of SMARTLINK |     | GROUPS | currently | configured |     | 1   |
| ------ | ------------ | --- | ------ | --------- | ---------- | --- | --- |
24
| Command        | History     |     |     |     |              |     |     |
| -------------- | ----------- | --- | --- | --- | ------------ | --- | --- |
| Release        |             |     |     |     | Modification |     |     |
| 10.07orearlier |             |     |     |     | --           |     |     |
| Command        | Information |     |     |     |              |     |     |
Smartlink|70

| Platforms | Command | context | Authority                                            |
| --------- | ------- | ------- | ---------------------------------------------------- |
| 6200      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
6300 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6400 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
8360
71
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |
| -------------------------------- | --- | ----------------------------- | --- |

UFD (Uplink Failure Detection)

Chapter 4

UFD (Uplink Failure Detection)

Uplink Failure Detection (UFD) is used to help achieve network path redundancy. UFD monitors (tracks
the forwarding state of) the interfaces/LAGs configured as Links-to-Monitor (LtM) and when all LtM
links go down, UFD disables the interfaces/LAGs configured as Links-to-Disable (LtD). If any of the LtM
links come back up, then all the LtD links are brought back up.

This process triggers the re-convergence of the traffic to the redundant path that is typically set up using
another switch or network. A common example is the teaming NIC software in servers that is used to fail
over from the primary NIC to the secondary NIC upon primary NIC failure.

To avoid unnecessary switching in the downlink redundant path during a frequent network flap in the
uplink ports, delays can be configured. For example, if all the monitored uplinks are still down after the
configured down delay, all the links to disable interfaces/LAGs are brought down. Similarly, if any of the
monitored uplinks are still up after the configured up delay, all the disabled interfaces/LAGs are brought
back up.

In this simplistic topology, switch sw2 uses UFD to monitor the links (LtM) to switch sw1, disabling the
links (LtD) to switch sw3 upon failure of the links from switch sw2 to switch sw1. When sw3 detects that
the links from switch sw2 have gone down, it then switches to its redundant path.

Although UFD can be used alone, consider using it with Smartlink which automates fail over from links that have

gone down to redundant links. Smartlink is available on the 6200, 6300, 6400, and 8360 Switch Series.

Guidelines and limitations

n UFD is supported only on L2 interfaces and LAGs. It is not supported on ROP and SVI.

n UFD is not supported with VSX, meaning that ISL and MCLAGs are not supported.

Basic UFD configuration
To help understand how to configure UFD, a basic configuration is presented, followed by detailed
descriptions of the available commands under UFD (Uplink Failure Detection) commands.

Enabling UFD:

switch(config)# ufd enable

Creating UFD session 1 and then entering its context:

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

72

| switch(config)# | ufd | session-id |     | 1   |     |     |
| --------------- | --- | ---------- | --- | --- | --- | --- |
switch(config-ufd-1)#
Configuringtwolinkstobemonitoredandtwolinkstodisable:
| switch(config-ufd-1)# |     | links-to-monitor |     |     | 1/1/1,1/1/2   |     |
| --------------------- | --- | ---------------- | --- | --- | ------------- | --- |
| switch(config-ufd-1)# |     | links-to-disable |     |     | 1/1/11,1/1/12 |     |
Settingtheupanddowndelaysto10seconds:
| switch(config-ufd-1)# |     | delay | down | 10  |     |     |
| --------------------- | --- | ----- | ---- | --- | --- | --- |
| switch(config-ufd-1)# |     | delay | up   | 10  |     |     |
ShowinginformationforUFDsession1:
| switch# show          | ufd session |        | 1          |                 |     |             |
| --------------------- | ----------- | ------ | ---------- | --------------- | --- | ----------- |
| UFD session-id        |             |        |            | : 1             |     |             |
| UFD Links-to-Monitor  |             | status |            | : Up            |     |             |
| Up Delay              |             |        |            | : 10            | sec |             |
| Down Delay            |             |        |            | : 10            | sec |             |
| Links-to-Monitor      |             |        |            | : 1/1/1,1/1/2   |     |             |
| Links-to-Disable      |             |        |            | : 1/1/11,1/1/12 |     |             |
| Last Links-to-Monitor |             | Down   | Time       | : 2021-11-03    |     | 15:22:05:37 |
| UFD (Uplink           | Failure     |        | Detection) |                 |     | commands    |
ufd enable
ufd enable
no ufd enable
Description
EnablesUFD(UplinkFailureDetection).UFD isdisabledbydefault.Thiscommandmustbeissued
beforetheconfigurationthatissetwithrelatedUFD commandstakeseffect.
ThenoformofthiscommanddisablesUFD.
Examples
EnablingUFD:
| switch(config)#       | ufd | enable           |     |     |               |     |
| --------------------- | --- | ---------------- | --- | --- | ------------- | --- |
| switch(config)#       | ufd | session-id       |     | 1   |               |     |
| switch(config-ufd-1)# |     | links-to-monitor |     |     | 1/1/1,1/1/2   |     |
| switch(config-ufd-1)# |     | links-to-disable |     |     | 1/1/11,1/1/12 |     |
switch(config-ufd-1)#
|                       |     | delay | down | 10  |     |     |
| --------------------- | --- | ----- | ---- | --- | --- | --- |
| switch(config-ufd-1)# |     | delay | up   | 10  |     |     |
| switch(config-ufd-1)# |     | exit  |      |     |     |     |
switch(config)#
DisablingUFD:
UFD(UplinkFailureDetection)|73

| switch(config)#     | no      | ufd enable |                    |     |
| ------------------- | ------- | ---------- | ------------------ | --- |
| Command History     |         |            |                    |     |
| Release             |         |            | Modification       |     |
| 10.09               |         |            | Commandintroduced. |     |
| Command Information |         |            |                    |     |
| Platforms           | Command | context    | Authority          |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
ufd session-id
| ufd session-id    | <ID> |     |     |     |
| ----------------- | ---- | --- | --- | --- |
| no ufd session-id | <ID> |     |     |     |
Description
CreatesthespecifiedUFD(UplinkFailureDetection)sessionandthenentersitscontext.Ifthespecified
sessionalreadyexists,thiscommandentersitscontext.
Thenoformofthiscommanddeletesthespecifiedsessionconfiguration.
| Parameter |     |     | Description                             |     |
| --------- | --- | --- | --------------------------------------- | --- |
| <ID>      |     |     | SpecifiestheUFD sessionID.Range:1to128. |     |
Examples
CreatingUFDsession1andthenenteringitscontext:
| switch(config)#       | ufd | enable           |         |               |
| --------------------- | --- | ---------------- | ------- | ------------- |
| switch(config)#       | ufd | session-id       | 1       |               |
| switch(config-ufd-1)# |     | links-to-monitor |         | 1/1/1,1/1/2   |
| switch(config-ufd-1)# |     | links-to-disable |         | 1/1/11,1/1/12 |
| switch(config-ufd-1)# |     | delay            | down 10 |               |
| switch(config-ufd-1)# |     | delay            | up 10   |               |
| switch(config-ufd-1)# |     | exit             |         |               |
switch(config)#
CreatingUFDsession2andthenenteringitscontext:
| switch(config)#       | ufd | session-id       | 2   |             |
| --------------------- | --- | ---------------- | --- | ----------- |
| switch(config-ufd-2)# |     | links-to-monitor |     | lag18-lag20 |
| switch(config-ufd-2)# |     | links-to-disable |     | 1/1/3-1/1/5 |
| switch(config-ufd-2)# |     | exit             |     |             |
switch(config)#
DeletingUFDsession1:
74
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

| switch(config)#     | no      | ufd session-id | 1                  |     |
| ------------------- | ------- | -------------- | ------------------ | --- |
| Command History     |         |                |                    |     |
| Release             |         |                | Modification       |     |
| 10.09               |         |                | Commandintroduced. |     |
| Command Information |         |                |                    |     |
| Platforms           | Command | context        | Authority          |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
links-to-monitor
| links-to-monitor    | <IF/LAG-LIST> |     |     |     |
| ------------------- | ------------- | --- | --- | --- |
| no links-to-monitor | <IF/LAG-LIST> |     |     |     |
Description
WithintheselectedUFD(UplinkFailureDetection)sessioncontext,specifiestheuplinkinterfacesor
LAGstomonitorforUFD.
ForproperUFDoperation,links-to-monitorandlinks-to-disablemustbothbeconfigured.Use
commandlinks-to-disabletospecifyacorrespondinglistofinterfaces/LAGstodisableifthe
monitoreduplinksgodown.
ThenoformofthiscommanddeletesthespecifiedlinkstomonitorlistwithintheselectedUFD session
context.
ALAGmemberinterfacecannotbeaddedasalinktomonitor.Ainterfaceconfiguredasalinktomonitorcannot
beaddedasaLAGmemberinterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IF/LAG-LIST>
ListofL2interfacesorLAGs.Separateinterfaces/LAGswith
commas(forindividualinterfaces/LAGs)orhyphens(fora
consecutiverangeofinterfaces/LAGs).
Examples
ConfiguringtwouplinkstomonitorforUFDsession1:
| switch(config)#       | ufd | enable           |         |               |
| --------------------- | --- | ---------------- | ------- | ------------- |
| switch(config)#       | ufd | session-id       | 1       |               |
| switch(config-ufd-1)# |     | links-to-monitor |         | 1/1/1,1/1/2   |
| switch(config-ufd-1)# |     | links-to-disable |         | 1/1/11,1/1/12 |
| switch(config-ufd-1)# |     | delay            | down 10 |               |
| switch(config-ufd-1)# |     | delay            | up 10   |               |
| switch(config-ufd-1)# |     | exit             |         |               |
switch(config)#
UFD(UplinkFailureDetection)|75

ConfiguringarangeofuplinkLAGstomonitorforUFDsession2:
| switch(config)#       | ufd | session-id       | 2   |             |
| --------------------- | --- | ---------------- | --- | ----------- |
| switch(config-ufd-2)# |     | links-to-monitor |     | lag18-lag20 |
| switch(config-ufd-2)# |     | links-to-disable |     | 1/1/3-1/1/5 |
| switch(config-ufd-2)# |     | exit             |     |             |
switch(config)#
DeletingbothlinkstomonitorforUFDsession1:
| switch(config-ufd-1)# |         | no links-to-monitor |                    | 1/1/1,1/1/2 |
| --------------------- | ------- | ------------------- | ------------------ | ----------- |
| Command History       |         |                     |                    |             |
| Release               |         |                     | Modification       |             |
| 10.09                 |         |                     | Commandintroduced. |             |
| Command Information   |         |                     |                    |             |
| Platforms             | Command | context             | Authority          |             |
Allplatforms config-ufd-<ID> Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
links-to-disable
| links-to-disable    | <IF/LAG-LIST> |     |     |     |
| ------------------- | ------------- | --- | --- | --- |
| no links-to-disable | <IF/LAG-LIST> |     |     |     |
Description
WithintheselectedUFD(UplinkFailureDetection)sessioncontext,specifiestheinterfacesorLAGsto
disablewhenthemonitoreduplinkinterfacesgodown.
ForproperUFDoperation,links-to-disableandlinks-to-monitormustbothbeconfigured.Use
commandlinks-to-monitortospecifyacorrespondinglistofinterfaces/LAGstomonitor.
ThenoformofthiscommanddeletesthespecifiedlinkstodisablelistwithintheselectedUFD session
context.
ALAGmemberinterfacecannotbeaddedasalinktodisable.Ainterfaceconfiguredasalinktodisablecannot
beaddedasaLAGmemberinterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<IF/LAG-LIST> ListofL2interfacesorLAGs.Separateinterfaces/LAGswith
commas(forindividualinterfaces/LAGs)orhyphens(fora
consecutiverangeofinterfaces/LAGs).
Examples
Configuringtwolinkstobedisabled:
76
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

| switch(config)# | ufd | enable |     |     |
| --------------- | --- | ------ | --- | --- |
switch(config)#
|                       | ufd | session-id       | 1       |               |
| --------------------- | --- | ---------------- | ------- | ------------- |
| switch(config-ufd-1)# |     | links-to-monitor |         | 1/1/1,1/1/2   |
| switch(config-ufd-1)# |     | links-to-disable |         | 1/1/11,1/1/12 |
| switch(config-ufd-1)# |     | delay            | down 10 |               |
| switch(config-ufd-1)# |     | delay            | up 10   |               |
| switch(config-ufd-1)# |     | exit             |         |               |
switch(config)#
Configuringarangeofinterfacestodisable:
| switch(config)# | ufd | session-id | 2   |     |
| --------------- | --- | ---------- | --- | --- |
switch(config-ufd-2)#
|                       |     | links-to-monitor |     | lag18-lag20 |
| --------------------- | --- | ---------------- | --- | ----------- |
| switch(config-ufd-2)# |     | links-to-disable |     | 1/1/3-1/1/5 |
| switch(config-ufd-2)# |     | exit             |     |             |
switch(config)#
Deletingthelinkstodisablefortwointerfaces:
| switch(config-ufd-1)# |         | no links-to-disable |                    | 1/1/11,1/1/12 |
| --------------------- | ------- | ------------------- | ------------------ | ------------- |
| Command History       |         |                     |                    |               |
| Release               |         |                     | Modification       |               |
| 10.09                 |         |                     | Commandintroduced. |               |
| Command Information   |         |                     |                    |               |
| Platforms             | Command | context             | Authority          |               |
Allplatforms config-ufd-<ID> Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
delay
| delay {down    | | up} <DELAY> |     |     |     |
| -------------- | ------------- | --- | --- | --- |
| no delay {down | | up} <DELAY> |     |     |     |
Description
WithintheselectedUFD(UplinkFailureDetection)sessioncontext,specifiestheamountoftime(in
seconds)todelaybeforebringingupordowntheconfiguredLinkstoDisable(LtD)afterthe
correspondingLinkstoMonitor(LtM)comebackuporgodown.
Forexample,withdelay down 10,whenall LtM links go downandremaindownafter10seconds,
UFDdisablestheinterfaces/LAGsconfiguredasLinks-to-Disable(LtD).Similarly,withdelay 10,If
up
any of the LtM links come back upandremainupafter10seconds,thenalltheLtDlinksarebrought
backup.
Inadditiontoanyconfigureddelaythereisanadditionaldelayof3to5secondsbeforebringinganyLinks-to-
Disable(LtD)downorbackup.Sowiththedefaultdelayof0seconds,adelayof3to5secondsdoesoccur.
Thenoformofthiscommandrestoresthedelaytoitsdefaultof0seconds.
UFD(UplinkFailureDetection)|77

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<DELAY> Speciesthedelayinseconds.Range0to180seconds.Default:0
seconds.
Examples
Settingtheupanddowndelaysto10seconds:
| switch(config)#       | ufd | enable           |         |               |
| --------------------- | --- | ---------------- | ------- | ------------- |
| switch(config)#       | ufd | session-id       | 1       |               |
| switch(config-ufd-1)# |     | links-to-monitor |         | 1/1/1,1/1/2   |
| switch(config-ufd-1)# |     | links-to-disable |         | 1/1/11,1/1/12 |
| switch(config-ufd-1)# |     | delay            | down 10 |               |
| switch(config-ufd-1)# |     | delay            | up 10   |               |
| switch(config-ufd-1)# |     | exit             |         |               |
switch(config)#
Resettingtheupanddowndelaystotheirdefaultof0:
| switch(config-ufd-1)# |         | no delay | down               | 10  |
| --------------------- | ------- | -------- | ------------------ | --- |
| switch(config-ufd-1)# |         | no delay | up 10              |     |
| Command History       |         |          |                    |     |
| Release               |         |          | Modification       |     |
| 10.09                 |         |          | Commandintroduced. |     |
| Command Information   |         |          |                    |     |
| Platforms             | Command | context  | Authority          |     |
Allplatforms config-ufd-<ID> Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show ufd
| show ufd [session-id | <ID>] |     |     |     |
| -------------------- | ----- | --- | --- | --- |
Description
ShowsinformationonallUFDsessionsorthespecifiedUFDsession.
| Parameter |     |     | Description                                    |     |
| --------- | --- | --- | ---------------------------------------------- | --- |
| <ID>      |     |     | SpecifiesanexistingUFD sessionID.Range:1to128. |     |
Example
ShowinginformationonallconfiguredUFDsessions:
78
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- |

| switch#               | show ufd |           |                 |             |
| --------------------- | -------- | --------- | --------------- | ----------- |
| Global UFD            | Status   | : Enabled |                 |             |
| UFD session-id        |          |           | : 1             |             |
| UFD Links-to-Monitor  |          | status    | : Up            |             |
| Up Delay              |          |           | : 10 sec        |             |
| Down Delay            |          |           | : 10 sec        |             |
| Links-to-Monitor      |          |           | : 1/1/1,1/1/2   |             |
| Links-to-Disable      |          |           | : 1/1/11,1/1/12 |             |
| Last Links-to-Monitor |          | Down Time | : 2021-11-03    | 15:22:05:37 |
| UFD session-id        |          |           | : 2             |             |
| UFD Links-to-Monitor  |          | status    | : Up            |             |
| Up Delay              |          |           | : 5 sec         |             |
| Down Delay            |          |           | : 5 sec         |             |
| Links-to-Monitor      |          |           | : lag18-lag20   |             |
| Links-to-Disable      |          |           | : 1/1/3-1/1/5   |             |
| Last Links-to-Monitor |          | Down Time | : 2021-11-01    | 12:14:42:56 |
ShowinginformationonUFDsession2:
| switch#               | show ufd session | 2         |                    |             |
| --------------------- | ---------------- | --------- | ------------------ | ----------- |
| UFD session-id        |                  |           | : 2                |             |
| UFD Links-to-Monitor  |                  | status    | : Up               |             |
| Up Delay              |                  |           | : 5 sec            |             |
| Down Delay            |                  |           | : 5 sec            |             |
| Links-to-Monitor      |                  |           | : lag18-lag20      |             |
| Links-to-Disable      |                  |           | : 1/1/3-1/1/5      |             |
| Last Links-to-Monitor |                  | Down Time | : 2021-11-01       | 12:14:42:56 |
| Command History       |                  |           |                    |             |
| Release               |                  |           | Modification       |             |
| 10.09                 |                  |           | Commandintroduced. |             |
| Command Information   |                  |           |                    |             |
| Platforms             | Command          | context   | Authority          |             |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show capacities        |     | ufd |     |     |
| ---------------------- | --- | --- | --- | --- |
| show capacities        | ufd |     |     |     |
| show capacities-status |     | ufd |     |     |
Description
Commandshow capacities ufdshowsUFDsessioncapacity.Commandshow capacities-status ufd
showsUFDsessioncapacityandthenumberofUFDsessionsconfigured.
Example
ShowingUFDsessioncapacity:
UFD(UplinkFailureDetection)|79

| switch#            | show capacities |        | ufd |     |     |     |       |
| ------------------ | --------------- | ------ | --- | --- | --- | --- | ----- |
| System Capacities: |                 | Filter | UFD |     |     |     |       |
| Capacities         | Name            |        |     |     |     |     | Value |
----------------------------------------------------------------------------------
---
Maximum number of Uplink Failure Detection sessions configurable in a system 128
ShowingUFDsessioncapacityandthenumberofUFDsessionsconfigured:
| switch(config)#   |        | show    | capacities-status |     | ufd |       |     |
| ----------------- | ------ | ------- | ----------------- | --- | --- | ----- | --- |
| System Capacities |        | Status: | Filter            | UFD |     |       |     |
| Capacities        | Status | Name    |                   |     |     | Value |     |
Maximum
----------------------------------------------------------------------------------
---
Number of Uplink Failure Detection sessions currently configured 1 128
| Command   | History     |     |         |                    |     |     |     |
| --------- | ----------- | --- | ------- | ------------------ | --- | --- | --- |
| Release   |             |     |         | Modification       |     |     |     |
| 10.09     |             |     |         | Commandintroduced. |     |     |     |
| Command   | Information |     |         |                    |     |     |     |
| Platforms | Command     |     | context | Authority          |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show running-config |     |     | ufd |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- |
| show running-config |     | ufd |     |     |     |     |     |
Description
ShowstherunningconfigurationforUFD.
Example
ShowingtheUFDportionofrunningconfigurationinformation:
| switch(config)# |     | ufd enable |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- | --- | --- |
switch(config)#
|                       |     | ufd session-id |                  | 1   |               |     |     |
| --------------------- | --- | -------------- | ---------------- | --- | ------------- | --- | --- |
| switch(config-ufd-1)# |     |                | links-to-monitor |     | 1/1/1,1/1/2   |     |     |
| switch(config-ufd-1)# |     |                | links-to-disable |     | 1/1/11,1/1/12 |     |     |
| switch(config-ufd-1)# |     |                | delay down       | 10  |               |     |     |
| switch(config-ufd-1)# |     |                | delay up         | 10  |               |     |     |
| switch(config-ufd-1)# |     |                | exit             |     |               |     |     |
switch(config)#
| switch# | show running-config |     | ufd |     |     |     |     |
| ------- | ------------------- | --- | --- | --- | --- | --- | --- |
80
| AOS-CX10.09LinkAggregationGuide| |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |     |     |     |
| -------------------------------- | --- | ----------------------------- | --- | --- | --- | --- | --- |

| Current        | configuration: |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| ufd enable     |                |     |     |     |
| ufd session-id | 1              |     |     |     |
delay up 10
delay down 10
| links-to-monitor |             | 1/1/1,1/1/2   |                    |     |
| ---------------- | ----------- | ------------- | ------------------ | --- |
| links-to-disable |             | 1/1/11,1/1/12 |                    |     |
| Command          | History     |               |                    |     |
| Release          |             |               | Modification       |     |
| 10.09            |             |               | Commandintroduced. |     |
| Command          | Information |               |                    |     |
| Platforms        | Command     | context       | Authority          |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show-tech | ufd |     |     |     |
| --------- | --- | --- | --- | --- |
| show-tech | ufd |     |     |     |
Description
Executestheshow ufdcommandfollowedbytheshow running-config ufdcommand.
Example
| Runningtheshow | ufdcommandfollowedbytheshow |     |     | ufdcommand: |
| -------------- | --------------------------- | --- | --- | ----------- |
running-config
switch#
|     | show tech | ufd |     |     |
| --- | --------- | --- | --- | --- |
====================================================
| Show Tech | executed | on Tue Nov | 23 11:32:08 2021 |     |
| --------- | -------- | ---------- | ---------------- | --- |
====================================================
====================================================
| [Begin] | Feature ufd |     |     |     |
| ------- | ----------- | --- | --- | --- |
====================================================
*********************************
| Command | : show ufd |     |     |     |
| ------- | ---------- | --- | --- | --- |
*********************************
| Global                | UFD Status | : Enabled |          |     |
| --------------------- | ---------- | --------- | -------- | --- |
| UFD session-id        |            |           | : 10     |     |
| UFD Links-to-Monitor  |            | status    | : Up     |     |
| Up Delay              |            |           | : 20 sec |     |
| Down Delay            |            |           | : 10 sec |     |
| Links-to-Monitor      |            |           | : None   |     |
| Links-to-Disable      |            |           | : None   |     |
| Last Links-to-Monitor |            | Down Time | : None   |     |
UFD(UplinkFailureDetection)|81

| UFD session-id        |     |     |        |      | : 20    |
| --------------------- | --- | --- | ------ | ---- | ------- |
| UFD Links-to-Monitor  |     |     | status |      | : Up    |
| Up Delay              |     |     |        |      | : 0 sec |
| Down Delay            |     |     |        |      | : 0 sec |
| Links-to-Monitor      |     |     |        |      | : None  |
| Links-to-Disable      |     |     |        |      | : None  |
| Last Links-to-Monitor |     |     | Down   | Time | : None  |
*********************************
| Command | : show | running-config |     |     | ufd |
| ------- | ------ | -------------- | --- | --- | --- |
*********************************
ufd enable
| ufd session-id |      | 10  |     |     |     |
| -------------- | ---- | --- | --- | --- | --- |
| delay          | down | 10  |     |     |     |
| delay          | up   | 20  |     |     |     |
exit
| ufd session-id |     | 20  |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
exit
====================================================
| [End] Feature |     | ufd |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
====================================================
====================================================
| Show Tech | commands |     | executed | successfully |     |
| --------- | -------- | --- | -------- | ------------ | --- |
====================================================
| Command   | History     |     |         |     |                    |
| --------- | ----------- | --- | ------- | --- | ------------------ |
| Release   |             |     |         |     | Modification       |
| 10.09     |             |     |         |     | Commandintroduced. |
| Command   | Information |     |         |     |                    |
| Platforms | Command     |     | context |     | Authority          |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| debug ufd    | all |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- |
| debug ufd    | all |     |     |     |     |
| no debug ufd | all |     |     |     |     |
Description
EnablestheUFDdebuglogs.
ThenoformofthiscommanddisablestheUFDdebuglogs.
Examples
EnablingUFDdebuglogs:
| switch(config)# |     | debug | ufd | all |     |
| --------------- | --- | ----- | --- | --- | --- |
82
| AOS-CX10.09LinkAggregationGuide| |     |     | (4100i,6xxx,8xxxSwitchSeries) |     |     |
| -------------------------------- | --- | --- | ----------------------------- | --- | --- |

DisablingUFDdebuglogs:
| switch(config)#     | no      | debug ufd all |                    |
| ------------------- | ------- | ------------- | ------------------ |
| Command History     |         |               |                    |
| Release             |         |               | Modification       |
| 10.09               |         |               | Commandintroduced. |
| Command Information |         |               |                    |
| Platforms           | Command | context       | Authority          |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
UFD(UplinkFailureDetection)|83

Support and Other Resources

Chapter 5

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

Airheads social
forums and
Knowledge Base

AOS-CX Switch
Software
Documentation
Portal

Aruba Hardware
Documentation
and Translations
Portal

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

84

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
Arubaiscommittedtoprovidingourcustomerswithinformationaboutthechemicalsubstancesinour
productsasneededtocomplywithlegalrequirements,environmentaldata(companyprograms,
SupportandOtherResources|85

product recycling, energy efficiency), and safety information and compliance data, (RoHS and WEEE). For
more information, see https://www.arubanetworks.com/company/about-us/environmental-citizenship/.

Documentation Feedback
Aruba is committed to providing documentation that meets your needs. To help us improve the
documentation, send any errors, suggestions, or comments to Documentation Feedback (docsfeedback-
switching@hpe.com). When submitting your feedback, include the document title, part number, edition,
and publication date located on the front cover of the document. For online help content, include the
product name, product version, help edition, and publication date located on the legal notices page.

AOS-CX 10.09 Link Aggregation Guide | (4100i, 6xxx, 8xxx Switch Series)

86