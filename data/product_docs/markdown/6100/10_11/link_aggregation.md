AOS-CX 10.11 Link
Aggregation Guide

All Switch Series

Published: February 2023
Edition: 2

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
|                                                   | LACPconfigurationsettings                  | 11  |
|                                                   | InterfaceLACPsettings                      | 12  |
| LAGinterfacestates                                |                                            | 12  |
| Howstaticlinkaggregationgroupsarebuilt            |                                            | 13  |
|                                                   | Referenceportselectionprocess              | 13  |
|                                                   | Settingtheaggregationstateofeachmemberport | 14  |
Settingtheaggregationstateofamemberportinastaticaggregationgroup 14
| Howdynamiclinkaggregationgroupsarebuilt                   |                                                      | 14  |
| --------------------------------------------------------- | ---------------------------------------------------- | --- |
|                                                           | Choosingareferenceport                               | 14  |
|                                                           | Settingtheaggregationstateofeachmemberport           | 15  |
| LAGconfigurationguidelines                                |                                                      | 15  |
|                                                           | Aggregationmemberinterfacerestrictions               | 15  |
|                                                           | Requirementsforaddinginterfaces                      | 15  |
| Layer2aggregationgroups                                   |                                                      | 16  |
|                                                           | Configuringalayer2staticaggregationgroup             | 16  |
|                                                           | Configuringalayer2dynamicaggregationgroup            | 19  |
| Layer3aggregationgroups                                   |                                                      | 22  |
|                                                           | Configuringalayer3staticaggregationgroup             | 22  |
|                                                           | Configuringalayer3dynamicaggregationgroup            | 25  |
| RemovingaLAG                                              |                                                      | 28  |
| RemovinganinterfacefromaLAG                               |                                                      | 29  |
| ChangingtheLAGmembershipforaninterface                    |                                                      | 30  |
| ConfigurationofanaggregateInterface                       |                                                      | 33  |
|                                                           | Configuringthedescriptionofanaggregateinterface      | 33  |
|                                                           | SettingtheMTUforalayer2memberlinkinterface           | 34  |
|                                                           | SettingtheMTUforalayer3aggregateinterface            | 34  |
|                                                           | Impactofshuttingdownorbringingupanaggregateinterface | 35  |
|                                                           | Shuttingdownanaggregateinterface                     | 35  |
| Supportedhashingalgorithms                                |                                                      | 35  |
| Configurationverification                                 |                                                      | 35  |
| BFDreportsaLAGasdownevenwhenhealthylinksarestillavailable |                                                      | 36  |
| LACPandLAGcommands                                        |                                                      | 37  |
3
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

| description(lag)                    |                                |            | 37  |
| ----------------------------------- | ------------------------------ | ---------- | --- |
| hash                                |                                |            | 38  |
| interfacelag                        |                                |            | 39  |
| ipaddress(interfacelag)             |                                |            | 40  |
| ipv6address (lag)                   |                                |            | 41  |
| lacpfallback                        |                                |            | 42  |
| lacpfallback-static                 |                                |            | 43  |
| lacphash                            |                                |            | 44  |
| lacpmode                            |                                |            | 45  |
| lacpport-id                         |                                |            | 46  |
| lacpport-priority                   |                                |            | 46  |
| lacprate                            |                                |            | 47  |
| lacpsystem-priority                 |                                |            | 48  |
| lag                                 |                                |            | 49  |
| showinterface(LAG)                  |                                |            | 50  |
| showlacpaggregates(LAG)             |                                |            | 52  |
| showlacpconfiguration               |                                |            | 53  |
| showlacpinterfaces                  |                                |            | 54  |
| showlag                             |                                |            | 57  |
| showrunning-configinterfacelag      |                                |            | 59  |
| shutdown(interfacelag)              |                                |            | 59  |
| vlantrunknative(LAG)                |                                |            | 60  |
| Smartlink                           |                                |            | 63  |
| Guidelinesandlimitations            |                                |            | 63  |
| Smartlinkcommands                   |                                |            | 64  |
| Configurationcommands               |                                |            | 64  |
|                                     | smartlinkgroup                 |            | 64  |
|                                     | smartlinkrecv-control-vlan     |            | 65  |
| Groupcontextcommands                |                                |            | 66  |
|                                     | description(smartlinkgroup)    |            | 66  |
|                                     | diag-dumpsmartlinkbasic        |            | 67  |
|                                     | primary-port                   |            | 68  |
|                                     | smartlinkgroupsecondary-port   |            | 69  |
|                                     | control-vlan                   |            | 69  |
|                                     | protected-vlans                |            | 70  |
|                                     | preemption                     |            | 71  |
|                                     | preemption-delay               |            | 72  |
| Displaycommands                     |                                |            | 73  |
|                                     | showsmartlinkgroup             |            | 73  |
|                                     | showsmartlinkgroupall          |            | 74  |
|                                     | showsmartlinkgroupdetail       |            | 75  |
|                                     | showsmartlinkflush-statistics  |            | 76  |
|                                     | clearsmartlinkgroupstatistics  |            | 77  |
|                                     | clearsmartlinkflush-statistics |            | 77  |
|                                     | showrunning-config(smartlink)  |            | 78  |
| Supportabilitycommands              |                                |            | 79  |
|                                     | showcapacitiessmartlink        |            | 79  |
| UFD (Uplink                         | Failure                        | Detection) | 81  |
| Guidelinesandlimitations            |                                |            | 81  |
| BasicUFDconfiguration               |                                |            | 81  |
| UFD(UplinkFailureDetection)commands |                                |            | 82  |
| ufdenable                           |                                |            | 82  |
| ufdsession-id                       |                                |            | 83  |
| links-to-monitor                    |                                |            | 84  |
Contents|4

|                       | links-to-disable      |           | 85  |
| --------------------- | --------------------- | --------- | --- |
|                       | delay                 |           | 87  |
|                       | showufd               |           | 88  |
|                       | showcapacitiesufd     |           | 89  |
|                       | showrunning-configufd |           | 90  |
|                       | showtechufd           |           | 91  |
|                       | debugufdall           |           | 92  |
| Support               | and Other             | Resources | 94  |
| AccessingArubaSupport |                       |           | 94  |
| AccessingUpdates      |                       |           | 95  |
|                       | ArubaSupportPortal    |           | 95  |
|                       | MyNetworking          |           | 95  |
| WarrantyInformation   |                       |           | 95  |
| RegulatoryInformation |                       |           | 95  |
| DocumentationFeedback |                       |           | 96  |
5
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 4100i Switch Series (JL817A, JL818A)

n Aruba 6000 Switch Series (R8N85A, R8N86A, R8N87A, R8N88A, R8N89A, R9Y03A)

n Aruba 6100 Switch Series (JL675A, JL676A, JL677A, JL678A, JL679A)

n Aruba 6200 Switch Series (JL724A, JL725A, JL726A, JL727A, JL728A, R8Q67A, R8Q68A, R8Q69A, R8Q70A,

R8Q71A, R8V08A, R8V09A, R8V10A, R8V11A, R8V12A, R8Q72A)

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A, R8S89A, R8S90A, R8S91A, R8S92A)

n Aruba 6400 Switch Series (R0X31A, R0X38B, R0X38C, R0X39B, R0X39C, R0X40B, R0X40C, R0X41A,
R0X41C, R0X42A, R0X42C, R0X43A, R0X43C, R0X44A, R0X44C, R0X45A, R0X45C, R0X26A, R0X27A,
JL741A)

n Aruba 8320 Switch Series (JL479A, JL579A, JL581A)

n Aruba 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n Aruba 8360 Switch Series (JL700A, JL701A, JL702A, JL703A, JL706A, JL707A, JL708A, JL709A, JL710A,

JL711A, JL700C, JL701C, JL702C, JL703C, JL706C, JL707C, JL708C, JL709C, JL710C, JL711C, JL704C, JL705C,
JL719C, JL718C, JL717C, JL720C, JL722C, JL721C )

n Aruba 8400 Switch Series (JL366A, JL363A, JL687A)

n Aruba 9300 Switch Series (R9A29A, R9A30A, R8Z96A)

n Aruba 10000 Switch Series (R8P13A, R8P14A)

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

AOS-CX 10.11 Link Aggregation Guide | (All Switch Series)

6

Convention

Usage

example-text

In code and screen examples, indicates text entered by a user.

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

About this document | 7

| Variable information |     | in CLI prompts |     |
| -------------------- | --- | -------------- | --- |
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
| On the 4100i | Switch | Series |     |
| ------------ | ------ | ------ | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6000 | and 6100 | Switch Series |     |
| ----------- | -------- | ------------- | --- |
n member:Always1.VSFisnotsupportedonthisswitch.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4ontheswitch.
| On the 6200 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to8.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4inslot1on
member1.
| On the 6300 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis
1.
n slot:Always1.Thisisnotamodularswitch,sotherearenoslots.
n port:Physicalnumberofaportontheswitch.
Forexample,thelogicalinterface1/1/4insoftwareisassociatedwithphysicalport4onmember1.
| On the 6400 | Switch | Series |     |
| ----------- | ------ | ------ | --- |
8
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

n member: Always 1. VSF is not supported on this switch.

n slot: Specifies physical location of a module in the switch chassis.

o Management modules are on the front of the switch in slots 1/1 and 1/2.

o Line modules are on the front of the switch starting in slot 1/3.

n port: Physical number of a port on a line module.

For example, the logical interface 1/3/4 in software is associated with physical port 4 in slot 3 on
member 1.

On the 83xx, 9300, and 10000 Switch Series

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

n Layer 2: The member ports of the corresponding Link Aggregation Group can only be layer 2

Ethernet interfaces.

n Layer 3: The member ports of the corresponding Link Aggregation Group can only be layer 3

interfaces.

Layer 3 aggregation groups are not supported on the 4100i, 6000, 6100, and 6200 Switch Series.

The effective port rate of an aggregate interface equals the total rate of its member ports. Only full
duplex mode members are eligible for aggregation.

AOS-CX 10.11 Link Aggregation Guide | (All Switch Series)

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
two participating devices through the LACP protocol, which is adaptive or dynamic to these network
failures.

Layer 2 aggregation groups and layer 3 aggregation groups support both static and dynamic modes.

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

LACP configuration settings

Link Aggregation | 11

| Task | Command |     |     | Example |     |
| ---- | ------- | --- | --- | ------- | --- |
SettingtheLACPmodeto lacp mode {active | passive} switch(config-lag-if)# lacp
activeorpassive.
mode active
SettingtheLACPmodetooff. no lacp mode {active | passive} switch(config-lag-if)# no
|     |     |     |     | lacp mode active |     |
| --- | --- | --- | --- | ---------------- | --- |
Settingthehashtype. For6000,6100,and8400Switch For6000,6100,and8400Switch
|     | Series:                        |             |            | Series:                     |           |
| --- | ------------------------------ | ----------- | ---------- | --------------------------- | --------- |
|     | lacp hash                      | [l2-src-dst | | l3-src-  | switch(config)#             | lacp hash |
|     | dst | l4-src-dst]              |             |            | l2-src-dst                  |           |
|     | For8320,8325,6200,6300,6400and |             |            | For8320,8325,6200,6300,6400 |           |
|     | 10000SwitchSeries:             |             |            | and10000SwitchSeries:       |           |
|     | hash [l2-src-dst               | |           | l3-src-dst | | switch(config-lag-if)#    | hash      |
|     | l4-src-dst]                    |             |            | l2-src-dst                  |           |
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
| LAGport.              |          |     |     | lag 1           |           |
switch(config-lag-if)#
shutdown
Resettingeveryinterfacein no shutdown switch(config-lag-if)# no
theLAGtothedefault(up)
shutdown
| Interface LACP settings |         |     |     |         |     |
| ----------------------- | ------- | --- | --- | ------- | --- |
| Task                    | Command |     |     | Example |     |
SettingtheLACPportID. lacp port-id <ID> switch(config-if)# lacp port-
id 100
SettingtheLACPportIDtothe no lacp port-id switch(config-if)# no lacp
| default. |     |     |     | port-id |     |
| -------- | --- | --- | --- | ------- | --- |
SettingtheLACPportpriority. lacp port-priority <PORT- switch(config-if)# lacp port-
|     | PRIORITY> |     |     | priority 100 |     |
| --- | --------- | --- | --- | ------------ | --- |
SettingtheLACPportpriority no lacp port-priority switch(config-if)# no lacp
| tothedefault         |     |     |     | port-priority |     |
| -------------------- | --- | --- | --- | ------------- | --- |
| LAG interface states |     |     |     |               |     |
12
| AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries) |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- |

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

E - Default
neighbor state

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

Link Aggregation | 13

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
14
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- | --- |

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

n If any features in the following list are configured on the interface, you cannot assign an interface to

a Layer 2 aggregation group:

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

Link Aggregation | 15

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

o 8320, 8325, 8360, 8400, 9300, or 10000 switches: The interface becomes disabled.

Disabling an interface

When an interface LAG is disabled with the shutdown command, all its members also become
operationally down.

Layer 2 aggregation groups
All switches support static and dynamic layer 2 aggregation groups.

On the 6400 Switch Series, port identification differs. Line card ports start at 1/3/1.

Configuring a layer 2 static aggregation group

Prerequisites

You must be in the global configuration context: switch(config)#.

Procedure

1. Create a layer 2 aggregate interface and access the layer 2 aggregate interface view by entering:

switch(config)# interface lag <ID>

AOS-CX 10.11 Link Aggregation Guide | (All Switch Series)

16

TherangeoftheLAGinterfaceIDis1to256.
Whilecreatingthelayer2aggregateinterface,thesystemautomaticallycreatesalayer2static
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
3. Onthe8320,8325,8360,8400,9300and10000,disableroutingbyentering:
| switch(config-lag-if)# |     | no routing |     |
| ---------------------- | --- | ---------- | --- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformation
abouttheno routingcommand.
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
LinkAggregation|17

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
18
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

For8320,8325,8360,8400,9300and10000switchseries:
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
| Configuring | a    | layer 2 dynamic | aggregation | group |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. Createalayer2aggregateinterfaceandaccessthelayer2aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |
| --- | --------------- | --------- | -------- | --- |
TherangeoftheLAGinterfaceIDis1to256.
Whilecreatingthelayer2aggregateinterface,thesystemautomaticallycreatesalayer2dynamic
aggregationgroupnumberedthesame.
2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
|     | switch(config-lag-if)# |     | no shutdown |     |
| --- | ---------------------- | --- | ----------- | --- |
LinkAggregation|19

Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecausethe
commandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofamember
interface,enterthecommandattheinterfacelevel.Forexample:
| switch(config)# | interface | 1/1/2 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)# no shutdown
3. Onthe8320,8325,8360,8400,9300and10000,disableroutingbyentering:
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
20
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

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
LinkAggregation|21

| Heartbeat |     | rate | : Fast       |     |     |     |
| --------- | --- | ---- | ------------ | --- | --- | --- |
| Hash      |     |      | : l3-src-dst |     |     |     |
| Aggregate |     | mode | : Active     |     |     |     |
For8320,8325,8360,8400,9300and10000switchseries:
| switch(config-if-<1/1/1-1/1/4>)# |     |                |     |     | show running-config |     |
| -------------------------------- | --- | -------------- | --- | --- | ------------------- | --- |
| Current                          |     | configuration: |     |     |                     |     |
!
| vlan      | 1   |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |
| interface |     | lag | 20  |     |     |     |
no shutdown
no routing
|           | vlan | trunk | native  | 1   |     |     |
| --------- | ---- | ----- | ------- | --- | --- | --- |
|           | vlan | trunk | allowed | all |     |     |
|           | lacp | mode  | active  |     |     |     |
|           | lacp | rate  | fast    |     |     |     |
| interface |      | 1/1/1 |         |     |     |     |
no shutdown
lag 20
| switch(config-if-<1/1/1-1/1/4>)# |               |      |              |        | show lacp   | aggregates |
| -------------------------------- | ------------- | ---- | ------------ | ------ | ----------- | ---------- |
| Aggregate                        |               | name | : lag100     |        |             |            |
| Interfaces                       |               |      | : 1/1/3      | 1/1/1  | 1/1/4 1/1/2 |            |
| Heartbeat                        |               | rate | : Fast       |        |             |            |
| Hash                             |               |      | : l3-src-dst |        |             |            |
| Aggregate                        |               | mode | : Active     |        |             |            |
| Layer                            | 3 aggregation |      |              | groups |             |            |
Layer3aggregationgroupsaresupportedonallswitchseriesexcept6000,and6100SwitchSeries.
| Configuring |     | a   | layer 3 | static | aggregation | group |
| ----------- | --- | --- | ------- | ------ | ----------- | ----- |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. Createalayer3aggregateinterfaceandaccessthelayer3aggregateinterfaceviewbyentering:
|     | switch(config)# |     | interface |     | lag <ID> |     |
| --- | --------------- | --- | --------- | --- | -------- | --- |
TherangeoftheLAGinterfaceIDis1to256.
Whilecreatingthelayer3aggregateinterface,thesystemautomaticallycreatesalayer3static
aggregationgroupnumberedthesame.
22
| AOS-CX10.11LinkAggregationGuide| |     |     | (AllSwitchSeries) |     |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- | --- |

2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
n For6200,6300and6400switchseries:
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
n For8320,8325,8360,8400,9300and10000switchseries:
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
LinkAggregation|23

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
For8320,8325,8360,8400,9300and10000switchseries:
24
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

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
| Configuring                      | a    | layer 3 dynamic | aggregation |            | group |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. Createalayer3aggregateinterfaceandaccessthelayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |     |
| --- | --------------- | --------- | -------- | --- | --- |
TherangeoftheLAGinterfaceIDis1to256.
Whilecreatingthelayer3aggregateinterface,thesystemautomaticallycreatesalayer3dynamic
aggregationgroupnumberedthesame.
2. SettheoperationalstateofeveryinterfaceintheLAGtoupbyentering:
|     | n For6200,6300and6400switchseries: |     |             |     |     |
| --- | ---------------------------------- | --- | ----------- | --- | --- |
|     | switch(config-lag-if)#             |     | no shutdown |     |     |
|     | switch(config-lag-if)#             |     | routing     |     |     |
LinkAggregation|25

Thiscommanddoesnotimpacttheadministrativestateofthememberinterfacesbecause
thecommandwasenteredattheleveloftheLAG.Tochangetheadministrativestateofa
memberinterface,enterthecommandattheinterfacelevel.Forexample:
|     | switch(config)#    | interface | 1/1/2    |     |
| --- | ------------------ | --------- | -------- | --- |
|     | switch(config-if)# | no        | shutdown |     |
|     | switch(config-if)# | routing   |          |     |
n For8320,8325,8360,8400,9300and10000switchseries:
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
26
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

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
LinkAggregation|27

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
For8320,8325,8360,8400,9300and10000switchseries:
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
28
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

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
LinkAggregation|29

AfterremovingaphysicalinterfacefromaLAG:
n 4100i, 6000, 6100, 6200, 6300, and 6400 switches:TheinterfaceassociatedwithLAGbecomeslayer
2portswithdefaultlayer2configurationsandwithadminstatusofenabled
n 8320, 8325, 8360, 8400, 9300 and 10000 switches:TheinterfaceassociatedwiththeLAGbecomes
L3portswithdefaultL3configurationsandadministrativedown.Forexample,supposeinterface
1/1/1waspartofLAG3andyouhadadministrativelyenabledtheinterface.Ifyoulaterremove
interface1/1/1fromLAG3,theadministrativestatusautomaticallychangestodown.Ifyouwantto
usetheinterfaceagain,youmustadministrativelyenableitagain.
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
For8320,8325,8360,8400,9300and10000switchseries:
| switch(config)#    |     | interface | 1/1/1          |     |     |
| ------------------ | --- | --------- | -------------- | --- | --- |
| switch(config-if)# |     | no lag    | 100            |     |     |
| switch(config-if)# |     | show      | running-config |     |     |
Current configuration:
!
...
!
30
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- |

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
For8320,8325,8360,8400,9300and10000switchseries:
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
LinkAggregation|31

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
For8320,8325,8360,8400,9300and10000switchseries:
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
32
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

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
For8320,8325,8360,8400,9300and10000switchseries:
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
LinkAggregation|33

1. Createalayer3aggregateinterfaceandenterlayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <ID> |     |
| --- | --------------- | --------- | -------- | --- |
2. Configurethedescriptionoftheaggregateinterface:
|         | switch(config-if)# | description | <text>   |                |
| ------- | ------------------ | ----------- | -------- | -------------- |
| Setting | the MTU            | for a layer | 2 member | link interface |
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. Enteralayer2memberlinkinterfaceviewbyentering:
|     | switch(config)# | interface | <INTERFACE-ID> |     |
| --- | --------------- | --------- | -------------- | --- |
2. SettheMTUforthelayer2memberlinkinterface:
|     | switch(config-if)# | mtu | <VALUE> |     |
| --- | ------------------ | --- | ------- | --- |
SeetheCommand-LineInterfaceGuideforyourswitchandsoftwareversionformoreinformation
aboutthemtu <VALUE>command.Whenallowingjumboframesunderalayer2aggregation
interface,makesurethattheMTUvalueissetappropriatelyunderallmemberinterfaces.
| Setting | the MTU | for a layer | 3 aggregate | interface |
| ------- | ------- | ----------- | ----------- | --------- |
Layer3aggregationgroupsarenotsupportedonthe4100i,6000,6100,and6200SwitchSeries.
TheMTUofaninterfaceaffectsIPpacketsfragmentationandreassemblyontheinterface.
Prerequisites
Youmustbeintheglobalconfigurationcontext:switch(config)#.
Procedure
1. Enterlayer3aggregateinterfaceviewbyentering:
|     | switch(config)# | interface | lag <INTERFACE-ID> |     |
| --- | --------------- | --------- | ------------------ | --- |
2. SettheMTUforthelayer3aggregateinterface:
|     | switch(config-lag-if)# |     | ip mtu <VALUE> |     |
| --- | ---------------------- | --- | -------------- | --- |
34
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------- | --- | --- |

See the Command-Line Interface Guide for your switch and software version for more information
about the ip mtu <VALUE> command. When allowing jumbo frames under a layer 2 aggregation
interface, make sure that the MTU value is set appropriately under all member interfaces.

If the IP MTU is configured as 9198, the MTU on the physical interfaces must also be configured as 9198.

Impact of shutting down or bringing up an aggregate interface

By default, an aggregate interface is down. Shutting down or bringing up an aggregate interface affects
the aggregation states and link states of member ports in the corresponding aggregation group as
follows:

n When an aggregate interface is shut down, all Selected ports in the corresponding aggregation group

become Unselected ports and all member ports go to an operationally down state.

n When an aggregate interface is brought up, the aggregation states of member ports in the

corresponding aggregation group are recalculated. LAG members, which are administratively up, will
become operationally up. The members that are not administratively up will be in the same state and
not made eligible for aggregation.

Shutting down an aggregate interface

Prerequisites

You must be in the global configuration context: switch(config)#.

Procedure

Enter the layer 3 aggregate interface view by entering:

switch(config)# interface lag <ID>

Shut down the aggregate interface:

switch(config-lag-if)# shutdown

Supported hashing algorithms

n Source MAC and destination MAC

n Source IP and destination IP

n Source port and destination port.

Configuration verification

Task

Command

Example

Viewing LACP

global

information

show lacp
configuration

switch# show lacp configuration

Link Aggregation | 35

| Task | Command |     | Example                      |                     |                      |
| ---- | ------- | --- | ---------------------------- | ------------------- | -------------------- |
|      |         |     | System-id                    | : 70:72:cf:ef:fc:d9 |                      |
|      |         |     | System-priority              | : 65534             |                      |
|      |         |     | Hash                         | : l3-src-dst        |                      |
|      |         |     | Theoutputdisplayedfortheshow |                     | lacp configurationis |
fromthe8400seriesswitch.
|     | show lacp | aggregates |     |     |     |
| --- | --------- | ---------- | --- | --- | --- |
ViewingLACP
|     |     |     | switch# | show lacp aggregates |     |
| --- | --- | --- | ------- | -------------------- | --- |
aggregate
|             |           |            | Aggregate-name        |                      | : lag100       |
| ----------- | --------- | ---------- | --------------------- | -------------------- | -------------- |
| information |           |            | Aggregated-interfaces |                      | : 1/1/2        |
|             |           |            | Heartbeat             | rate                 | : N/A          |
|             |           |            | Hash                  |                      | : l3-src-dst   |
|             |           |            | Aggregate             | mode                 | : off          |
|             |           |            | Aggregate-name        |                      | : lag110       |
|             |           |            | Aggregated-interfaces |                      | : 1/1/1, 1/1/3 |
|             |           |            | Heartbeat             | rate                 | : slow         |
|             |           |            | Hash                  |                      | : l3-src-dst   |
|             |           |            | Aggregate             | mode                 | : active       |
| ViewingLACP | show lacp | aggregates |                       |                      |                |
|             |           |            | switch#               | show lacp aggregates | lag100         |
lag100
| aggregate |     |     | Aggregate-name |     | : lag100 |
| --------- | --- | --- | -------------- | --- | -------- |
informationfor
|             |           |            | Aggregated-interfaces |                      | :            |
| ----------- | --------- | ---------- | --------------------- | -------------------- | ------------ |
| aLAG        |           |            | Heartbeat             | rate                 | : N/A        |
|             |           |            | Hash                  |                      | : l3-src-dst |
|             |           |            | Aggregate             | mode                 | : off        |
| ViewingLACP | show lacp | interfaces |                       |                      |              |
|             |           |            | switch#               | show lacp interfaces |              |
interfacedetails
Theoutputistoowidetodisplayinacolumn.Thecommand
outputisprovidedintheCLItopicforthecommand.
| BFD reports | a LAG | as down | even when | healthy | links are |
| ----------- | ----- | ------- | --------- | ------- | --------- |
still available
Symptom
BFDisnotsupportedonthe4100i,6000,6100,and6200SwitchSeries.
TheBidirectionalForwardDetection(BFD)featurereportsaLinkAggregation(LAG),asbeingdown,even
thoughtherearehealthyLAGlinksavailable.TheLAG,containingthedownedlink,willeventually
rebalancethetraffictoitsotherlinks.
Cause
ThisnotificationoccurswhentheminimumBFDcontrolpacketreceptionintervalissetatafasterrate
thantheLinkAggregationControlProtocol(LACP)rateandLAGrebalancingoccurs.BFDassumesthat
thelinkisdownwithoutrealizingthattheLAGisrebalancingthetrafficload.
36
| AOS-CX10.11LinkAggregationGuide| | (AllSwitchSeries) |     |     |     |     |
| -------------------------------- | ----------------- | --- | --- | --- | --- |

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
4. TochangetheLACPrate,enterthelacp slow}command.
rate {fast |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
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
l2-src-dst Specifiestheload-balancingcalculationtoincludeonlylayer2
items,suchassourceanddestinationMACaddresses.
l3-src-dst Specifiestheload-balancingcalculationtoincludeonlylayer3
items,suchassourceanddestinationIPaddresses.Default
setting.
l4-src-dst
Specifiestheload-balancingcalculationtoincludeonlylayer4
items,suchassourceanddestinationUDP/TCPports.
Example
| switch(config-lag-if)# |     | hash l2-src-dst |     |
| ---------------------- | --- | --------------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6200 config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
38
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

| Platforms | Command | context | Authority       |
| --------- | ------- | ------- | --------------- |
| 6300      |         |         | forthiscommand. |
6400
8320
8325
10000
| interface     | lag      |     |     |
| ------------- | -------- | --- | --- |
| interface lag | <ID>     |     |     |
| no interface  | lag <ID> |     |     |
Description
CreatesaLinkAggregationGroup(LAG)interfacerepresentedbyanID.
ThenoformofthiscommanddeletesaLAGinterfacerepresentedbyanID.
| Parameter |     |     | Description               |
| --------- | --- | --- | ------------------------- |
| <ID>      |     |     | SpecifiesaLAGinterfaceID. |
Usage
KeepinmindthefollowingrequirementswhenaddinginterfacestoaLAG:
n TodeterminethemaximumnumberofLAGinterfacesforyourtypeofswitch,lookattheoutput
fromtheshow lagcommand;however,thenumberofLAGsthatcanbecreated
capacities
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
| switch(config)# | no  | interface | lag 100 |
| --------------- | --- | --------- | ------- |
LinkAggregation|39

Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |     |         |     |              |
| -------------- | ----------- | --- | ------- | --- | ------------ |
| Release        |             |     |         |     | Modification |
| 10.07orearlier |             |     |         |     | --           |
| Command        | Information |     |         |     |              |
| Platforms      | Command     |     | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
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
| switch(config)# |     | interface |     | lag 1 |     |
| --------------- | --- | --------- | --- | ----- | --- |
switch(config-lag-if)#
|     |     |     |     | no ip address | 198.51.100.1/24 |
| --- | --- | --- | --- | ------------- | --------------- |
40
| AOS-CX10.11LinkAggregationGuide| |     |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- |

Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6300 config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
ipv6 address (lag)
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
<MASK>
SpecifiesthenumberofbitsintheaddressmaskinCIDRformat
(x),wherexisadecimalnumberfrom0to128.
Examples
SettingtheIPv6addressonLAGinterface1to2001:0db8:85a3::8a2e:0370:7334withamaskof24bits:
| switch(config)# | interface | lag 1 |     |
| --------------- | --------- | ----- | --- |
switch(config-lag-if)# ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
LinkAggregation|41

RemovingtheIPaddress2001:0db8:85a3::8a2e:0370:7334withmaskof24bitswithamaskof24bits
fromLAGinterface1:
| switch(config)# | interface | lag | 1   |
| --------------- | --------- | --- | --- |
switch(config-lag-if)# no ipv6 address 2001:0db8:85a3::8a2e:0370:7334/24
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
6300 config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
| 6400 |     |     | forthiscommand. |
| ---- | --- | --- | --------------- |
8320
8325
8360
8400
9300
10000
lacp fallback
lacp fallback
no lacp fallback
Description
ConfigurestheLACPfallbackonLAGport.
ThenoformofthiscommandsetstheLAGtoBLOCKstateifnoLACPpartnerisdetected.
Usage
ThismakesmembersoftheLAGfunctionasnon-bondedinterfaceswhennoLACP partnerisdetected.
ThisconfigurationisonlyapplicablewhentheLAGisoftypeMCLAG.Ifthememberportdoesnotgetan
LACPframe,theportisinIE state.
Examples
ConfiguringLACPfallbackonLAG port.
| switch(config)# | int | lag 1 multi-chassis |     |
| --------------- | --- | ------------------- | --- |
switch(config-lag-if)#
no sh
| switch(config-lag-if)# |     | lacp mode     | active |
| ---------------------- | --- | ------------- | ------ |
| switch(config-lag-if)# |     | lacp fallback |        |
42
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

ConfiguringtheLAGtoBLOCKstatewhennoLACPpartnerisdetected.
| switch(config)#        | int     | lag 1 multi-chassis |              |
| ---------------------- | ------- | ------------------- | ------------ |
| switch(config-lag-if)# |         | no sh               |              |
| switch(config-lag-if)# |         | lacp mode           | active       |
| switch(config-lag-if)# |         | no lacp             | fallback     |
| Release                |         |                     | Modification |
| 10.07orearlier         |         |                     | --           |
| Command Information    |         |                     |              |
| Platforms              | Command | context             | Authority    |
6400 config-if OperatorsorAdministratorsorlocalusergroupmemberswith
8320 config-lag-if executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
8325
8400
9300
10000
lacp fallback-static
lacp fallback-static
no lacp fallback-static
Description
ConfigurestheLACPfallback-staticonLAGport.
ThenoformofthiscommandsetstheLAGtoBLOCKstateifnoLACPpartnerisdetected.
Usage
ThismakesmembersoftheLAGfunctionasnon-bondedinterfaceswhennoLACP partnerisdetected.
OnememberinterfacethatispartoftheLAGstaysupandforwardstraffic,whiletheothermembers
arein lacp-blockstate.ThisconfigurationisapplicablewhenthelagisoftypeLACPandignoredinother
cases.Whenthiscommandisconfigured,onlyonememberofLAG isselectedtobeUP.Enabling
multiplemembersresultsinconfigurationmismatchonpeer,loop,mac-learningissues,andmore.
Examples
ConfiguringLACPfallback-staticonLAG port.
| switch(config)#        | interface | lag                  | 1      |
| ---------------------- | --------- | -------------------- | ------ |
| switch(config-lag-if)# |           | lacp mode            | active |
| switch(config-lag-if)# |           | lacp fallback-static |        |
ConfiguringtheLAGtoBLOCKstatewhennoLACPpartnerisdetected.
| switch(config)#        | interface | lag     | 1               |
| ---------------------- | --------- | ------- | --------------- |
| switch(config-lag-if)# |           | no lacp | fallback-static |
ConfiguringLACPfallback-staticonstaticport.
LinkAggregation|43

| switch(config-lag-if)# |             |                      |         | lacp | fallback-static    |      |
| ---------------------- | ----------- | -------------------- | ------- | ---- | ------------------ | ---- |
| Cannot                 | enable      | LACP fallback-static |         |      | on static          | LAG. |
| Release                |             |                      |         |      | Modification       |      |
| 10.11                  |             |                      |         |      | Commandintroduced. |      |
| Command                | Information |                      |         |      |                    |      |
| Platforms              |             | Command              | context |      | Authority          |      |
Allplatforms config-if OperatorsorAdministratorsorlocalusergroupmemberswith
config-lag-if executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
lacp hash
| lacp hash | [l2-src-dst |             | | l3-src-dst |            | | l4-src-dst] |     |
| --------- | ----------- | ----------- | ------------ | ---------- | ------------- | --- |
| no lacp   | hash        | [l2-src-dst | |            | l3-src-dst | | l4-src-dst] |     |
Description
Controlstheselectionofaninterfaceinagroupofaggregateinterfaces.Thehashtypevaluehelps
transmitaframe.Thisconfigurationmustbedoneatthegloballevel.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
l2-src-dst Specifiestheload-balancingcalculationtoincludeonlylayer2
items,suchassourceanddestinationMACaddresses.
l3-src-dst
Specifiestheload-balancingcalculationtoincludeonlylayer3
items,suchassourceanddestinationIPaddresses.
l4-src-dst Specifiestheload-balancingcalculationtoincludeonlylayer4
items,suchassourceanddestinationUDP/TCPports.
Example
| switch(config)# |     |     | lacp hash | l2-src-dst |     |     |
| --------------- | --- | --- | --------- | ---------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |     |     |     |              |     |
| -------------- | ----------- | --- | --- | --- | ------------ | --- |
| Release        |             |     |     |     | Modification |     |
| 10.07orearlier |             |     |     |     | --           |     |
| Command        | Information |     |     |     |              |     |
44
| AOS-CX10.11LinkAggregationGuide| |     |     | (AllSwitchSeries) |     |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- | --- |

| Platforms |     | Command |     | context | Authority |
| --------- | --- | ------- | --- | ------- | --------- |
6000 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6100 |     |     |     |     | forthiscommand. |
| ---- | --- | --- | --- | --- | --------------- |
8400
9300
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
passive SpecifiesthatthelocalswitchwilllistenforLACPDUsfromthe
remotedeviceforLACPnegotiation.
NOTE:
AmomentarytrafficdropoccursbecauseLACPpartnersreconverge
whenchangingthemodefromactivetopassiveorfrompassivetoactive.
Examples
SettingtheLACPmodetoactive:
| switch(config)#        |     |     | interface | lag       | 1      |
| ---------------------- | --- | --- | --------- | --------- | ------ |
| switch(config-lag-if)# |     |     |           | lacp mode | active |
SettingtheLACPmodetooff:
| switch(config)#        |     |     | interface | lag     | 1           |
| ---------------------- | --- | --- | --------- | ------- | ----------- |
| switch(config-lag-if)# |     |     |           | no lacp | mode active |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History |     |     |     |              |
| -------------- | ------- | --- | --- | --- | ------------ |
| Release        |         |     |     |     | Modification |
| 10.07orearlier |         |     |     |     | --           |
LinkAggregation|45

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
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
| switch(config-if)# |     | lacp port-id | 10  |
| ------------------ | --- | ------------ | --- |
RemovingtheLACPportIDvalue:
| switch(config-if)# |     | no lacp port-id |     |
| ------------------ | --- | --------------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp port-priority
| lacp port-priority | <PORT-PRIORITY> |     |     |
| ------------------ | --------------- | --- | --- |
no lacp port-priority
46
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

Description
SetsanLACPportpriorityvalueforthememberinterfaceoftheLAG.
ThenoformofthiscommandrevertstheLACPportprioritytothedefault,whichis1.
| Parameter       |     |     | Description                                 |
| --------------- | --- | --- | ------------------------------------------- |
| <PORT-PRIORITY> |     |     | Specifiesaportpriorityvalue.Range:1to65535. |
Examples
SettingaLACPportpriorityvalueof10:
| switch(config-if)# |     | lacp port-priority | 10  |
| ------------------ | --- | ------------------ | --- |
RevertingtheLACPportIDtothedefault:
switch(config-if)#
no lacp port-priority
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp rate
| lacp rate {fast | | slow}       |     |     |
| --------------- | ------------- | --- | --- |
| no lacp rate    | {fast | slow} |     |     |
Description
SetsanLACPheartbeatrequesttimetofastorslow.
ThenoformofthecommandsetsanLACPratetoslow.
| Parameter |     |     | Description                                             |
| --------- | --- | --- | ------------------------------------------------------- |
| fast      |     |     | Specifiestheheartbeatrequesttoeverysecond,andthetimeout |
periodisathree-consecutiveheartbeatlossthatis3seconds.
LinkAggregation|47

| Parameter |     |     | Description                                             |
| --------- | --- | --- | ------------------------------------------------------- |
| slow      |     |     | Specifiestheheartbeatrequesttoevery30seconds.Thetimeout |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
config-lag-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
lacp system-priority
| lacp system-priority    | <SYSTEM-PRIORITY-VALUE> |                         |     |
| ----------------------- | ----------------------- | ----------------------- | --- |
| no lacp system-priority |                         | <SYSTEM-PRIORITY-VALUE> |     |
Description
SetsaLinkAggregationControlProtocol(LACP)systempriority.
ThenoformofthiscommandsetsanLACPsystemprioritytothedefault,whichis65534.
48
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<SYSTEM-PRIORITY-VALUE> Specifiesasystempriorityvalue.Range:0to65535.
Examples
SettingaLinkAggregationControlProtocol(LACP)systempriorityto100:
| switch(config)# | lacp | system-priority | 100 |
| --------------- | ---- | --------------- | --- |
SettinganLACPsystemprioritytothedefault(65534):
| switch(config)# | no  | lacp system-priority |     |
| --------------- | --- | -------------------- | --- |
AmomentarytrafficdropcanbeseenincasetheLACPstatemachinemustrenegotiate.
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
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
ThenoformofthiscommandremovesaninterfacefromaspecifiedLAGinterfaceID.Themember
losesitsLACPconfigurationwhenremovedfromtheLAG.Thememberalsoreachesthedefaultstate
withanadministrativeshutdown.For6300and6400seriesswitches,theadministrativestateis
enabled.Configurations,suchasMTUandUDLD,areretained.
| Parameter |     |     | Description                            |
| --------- | --- | --- | -------------------------------------- |
| <ID>      |     |     | SpecifiesaLAGinterfaceID.Range:1to256. |
Usage
LinkAggregation|49

n AllmembersoftheLAGmusthavethesamespeed.Ifamembercomesuplatewithadifferent
speed,itwillnotparticipateintheLAG/LACP.Thehardwarerestrictionisappliedbeforeaddingan
interfacetoLAG.Thememberbelongstothecardtypethathasthesamemaximumspeedasthe
referenceportcardtype.
TomoveaninterfacefromLagAtoLagB,firstremovetheinterfacefromLagAandthenadditto
n
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
| switch(config)#    | interface | 1/1/1      |     |
| ------------------ | --------- | ---------- | --- |
| switch(config-if)# |           | no lag 100 |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show interface  | (LAG)      |            |     |
| --------------- | ---------- | ---------- | --- |
| show interfaces | <LAG-NAME> | [vsx-peer] |     |
Description
DisplaysinformationaboutaspecificLAG.
50
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

| Parameter  |     |     |     | Description        |     |     |
| ---------- | --- | --- | --- | ------------------ | --- | --- |
| <LAG-NAME> |     |     |     | SpecifiesaLAGname. |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayinginformationaboutLAG100:
| switch#               | show interface | lag100    |     |                     |     |       |
| --------------------- | -------------- | --------- | --- | ------------------- | --- | ----- |
| Aggregate             | lag100         | is up     |     |                     |     |       |
| Admin                 | state is up    |           |     |                     |     |       |
| Description           | :              |           |     |                     |     |       |
| MAC Address           |                |           |     | : 48:0f:cf:af:43:9c |     |       |
| Aggregated-interfaces |                |           |     | : 1/1/2             |     |       |
| Aggregation-key       |                |           |     | : 100               |     |       |
| Aggregate             | mode           |           |     | : active            |     |       |
| Speed                 |                |           |     | : 2000 Mb/s         |     |       |
| L3 Counters:          | Rx             | Disabled, | Tx  | Disabled            |     |       |
| qos trust             | none           |           |     |                     |     |       |
| VLAN Mode:            | access         |           |     |                     |     |       |
| Access                | VLAN: 1        |           |     |                     |     |       |
| Statistics            |                |           |     | RX                  | TX  | Total |
------------- -------------------- -------------------- --------------------
| Packets   |        |     |     | 20   | 45   | 65   |
| --------- | ------ | --- | --- | ---- | ---- | ---- |
| Unicast   |        |     |     | 5    | 5    | 10   |
| Multicast |        |     |     | 5    | 15   | 20   |
| Broadcast |        |     |     | 10   | 25   | 35   |
| Bytes     |        |     |     | 5658 | 2584 | 8242 |
| Jumbos    |        |     |     | 0    | 0    | 0    |
| Dropped   |        |     |     | 0    | 0    | 0    |
| Filtered  |        |     |     | 0    | 0    | 0    |
| Pause     | Frames |     |     | 0    | 0    | 0    |
| Errors    |        |     |     | 0    | 0    | 0    |
| CRC/FCS   |        |     |     | 0    | n/a  | 0    |
| Collision |        |     |     | n/a  | 0    | 0    |
| Runts     |        |     |     | 0    | n/a  | 0    |
| Giants    |        |     |     | 0    | n/a  | 0    |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |     |     |              |     |     |
| -------------- | ----------- | --- | --- | ------------ | --- | --- |
| Release        |             |     |     | Modification |     |     |
| 10.07orearlier |             |     |     | --           |     |     |
| Command        | Information |     |     |              |     |     |
LinkAggregation|51

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
| switch#               |     | show lacp | aggregates |              |        |        |
| --------------------- | --- | --------- | ---------- | ------------ | ------ | ------ |
| Aggregate-name        |     |           |            | : lag1       |        |        |
| Aggregated-interfaces |     |           |            | : 1/1/27     | 1/1/28 | 1/1/29 |
| Heartbeat             |     | rate      |            | : slow       |        |        |
| Hash                  |     |           |            | : l3-src-dst |        |        |
| Aggregate             |     | mode      |            | : active     |        |        |
| Aggregate-name        |     |           |            | : lag2       |        |        |
| Aggregated-interfaces |     |           |            | : 1/1/48     |        |        |
| Heartbeat             |     | rate      |            | : slow       |        |        |
| Hash                  |     |           |            | : l2-src-dst |        |        |
| Aggregate             |     | mode      |            | : passive    |        |        |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command | History |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
52
| AOS-CX10.11LinkAggregationGuide| |     |     | (AllSwitchSeries) |     |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- | --- |

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
| switch#         | show lacp | configuration     |     |
| --------------- | --------- | ----------------- | --- |
| System-id       | :         | 70:72:cf:ef:fc:d9 |     |
| System-priority | :         | 65534             |     |
| Hash            | :         | l3-src-dst        |     |
DisplayingglobalLACPconfiguration:
switch#
|                 | show lacp | configuration     |     |
| --------------- | --------- | ----------------- | --- |
| System-id       | :         | 98:f2:b3:68:40:a0 |     |
| System-priority | :         | 65534             |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |     |              |
| -------------- | ----------- | --- | ------------ |
| Release        |             |     | Modification |
| 10.07orearlier |             |     | --           |
| Command        | Information |     |              |
LinkAggregation|53

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
54
| AOS-CX10.11LinkAggregationGuide| |     |     | (AllSwitchSeries) |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |

| 1/1/3 | lag128 |     | 14 1 |     | PLFNCD | 70:72:cf:8c:60:a7 |     | 65534 | 128 |
| ----- | ------ | --- | ---- | --- | ------ | ----------------- | --- | ----- | --- |
1/1/4 lag128
1/1/5 lag20
DisplayingstaticLAG:
lacp fallback-staticcannotbeconfiguredonstaticlag.Attemptstoconfigurelacp fallback-staticon
astaticLAGresultsinthefollowingmessage:
CannotenableLACP-fallbackstaticonstaticLAG.
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
LinkAggregation|55

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
| 1/3/2 | lag1(mc) 131 1 | ALFNCD f8:60:f0:06:87:00 |     | 65534 1 |     |
| ----- | -------------- | ------------------------ | --- | ------- | --- |
| 1/9/3 | lag2(mc)       |                          |     |         |     |
DisplayinganLACPconfigurationwithLACP fallback:
| switch# | show lacp interfaces |     |     |     |     |
| ------- | -------------------- | --- | --- | --- | --- |
State abbreviations :
| A - Active        | P - Passive      | F - Aggregable | I - | Individual |     |
| ----------------- | ---------------- | -------------- | --- | ---------- | --- |
| S - Short-timeout | L - Long-timeout | N - InSync     | O - | OutofSync  |     |
56
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

| C - Collecting |             | D - Distributing |             |                |     |     |
| -------------- | ----------- | ---------------- | ----------- | -------------- | --- | --- |
| X - State      | m/c expired |                  | E - Default | neighbor state |     |     |
| Actor details  | of all      | interfaces:      |             |                |     |     |
----------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr | Forwarding |
| ---- | ---- | --------- | --------------- | --- | ----------- | ---------- |
|      | Name | Id Pri    |                 |     | Pri Key     | State      |
----------------------------------------------------------------------------------
| 1/1/4   | lag10      | 5 1             | IE ec:eb:b8:e4:29:00 |     | 65534 10 | up         |
| ------- | ---------- | --------------- | -------------------- | --- | -------- | ---------- |
| 1/1/5   | lag10      | 6 1             | IE ec:eb:b8:e4:29:00 |     | 65534 10 | lacp-block |
| 1/1/6   | lag10      | 7 1             | IE ec:eb:b8:e4:29:00 |     | 65534 10 | lacp-block |
| 1/3/27  | lag10      | 156 1           | IE ec:eb:b8:e4:29:00 |     | 65534 10 | lacp-block |
| 1/1/9   | lag20(mc)  | 9 1             | IE ec:eb:b8:e4:29:00 |     | 65534 10 | up         |
| Partner | details of | all interfaces: |                      |     |          |            |
----------------------------------------------------------------------------------
| Intf | Aggr | Port Port | State System-ID |     | System Aggr |     |
| ---- | ---- | --------- | --------------- | --- | ----------- | --- |
|      | Name | Id Pri    |                 |     | Pri Key     |     |
----------------------------------------------------------------------------------
| 1/1/4  | lag10     | 0 0 | IE 00:00:00:00:00:00 |     | 0 0 |     |
| ------ | --------- | --- | -------------------- | --- | --- | --- |
| 1/1/5  | lag10     | 0 0 | IE 00:00:00:00:00:00 |     | 0 0 |     |
| 1/1/6  | lag10     | 0 0 | IE 00:00:00:00:00:00 |     | 0 0 |     |
| 1/3/27 | lag10     | 0 0 | IE 00:00:00:00:00:00 |     | 0 0 |     |
| 1/1/9  | lag20(mc) | 0 0 | IE 00:00:00:00:00:00 |     | 0 0 |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |         |                                            |     |     |     |
| -------------- | ----------- | ------- | ------------------------------------------ | --- | --- | --- |
| Release        |             |         | Modification                               |     |     |     |
| 10.11          |             |         | LACPfallback-staticadded.                  |     |     |     |
| 10.11          |             |         | LACPfallbackaddedonVSX-supportedplatforms. |     |     |     |
| 10.07orearlier |             |         | --                                         |     |     |     |
| Command        | Information |         |                                            |     |     |     |
| Platforms      | Command     | context | Authority                                  |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
show lag
| show lag | <LAG-ID> |     |     |     |     |     |
| -------- | -------- | --- | --- | --- | --- | --- |
Description
Displaysthelag.
| Parameter |     |     | Description        |     |     |     |
| --------- | --- | --- | ------------------ | --- | --- | --- |
| <LAG-ID>  |     |     | SpecifiesthelagID. |     |     |     |
LinkAggregation|57

Examples
Displayingthelag.
switch#
show lag
| System-ID                | :        | f4:03:43:80:4a:00         |                     |         |
| ------------------------ | -------- | ------------------------- | ------------------- | ------- |
| System-priority          | :        | 65534                     |                     |         |
| Hash                     | :        | l3-src-dst                |                     |         |
| Aggregate                | lag1 is  | down                      |                     |         |
| Admin                    | state is | down                      |                     |         |
| Description              | :        |                           |                     |         |
| Type                     |          |                           | : normal            |         |
| Lacp                     | Fallback |                           | : n/a               |         |
| MAC                      | Address  |                           | : f4:03:43:80:4a:00 |         |
| Aggregated-interfaces    |          |                           | :                   |         |
| Aggregation-key          |          |                           | : 1                 |         |
| Aggregate                | mode     |                           | : static            |         |
| LACP                     | rate     |                           | : n/a               |         |
| Speed                    |          |                           | : 0 Mb/s            |         |
| Mode                     |          |                           | : routed            |         |
| Aggregate                | lag128   | is down                   |                     |         |
| Admin                    | state is | down                      |                     |         |
| Description              | :        |                           |                     |         |
| Type                     |          |                           | : normal            |         |
| Lacp                     | Fallback |                           | : n/a               |         |
| MAC Address              |          |                           | : f4:03:43:80:4a:00 |         |
| -- MORE                  | --, next | page: Space,              | next line: Enter,   | quit: q |
| Displayingthelagwhenlacp |          | fallback-staticisenabled. |                     |         |
| switch#                  | show lag |                           |                     |         |
| System-ID                | :        | 90:20:c2:24:60:00         |                     |         |
| System-priority          | :        | 65534                     |                     |         |
| Aggregate                | lag1 is  | up                        |                     |         |
| Admin                    | state is | up                        |                     |         |
| Description              | :        |                           |                     |         |
| Type                     |          |                           | : normal            |         |
| Lacp                     | Fallback |                           | : Enabled           |         |
| MAC                      | Address  |                           | : 90:20:c2:24:60:00 |         |
Aggregated-interfaces : 1/1/1 1/1/2 1/1/3 1/1/46 1/1/47 1/1/48
| Aggregation-key |             |     | : 1                       |     |
| --------------- | ----------- | --- | ------------------------- | --- |
| Aggregate       | mode        |     | : active                  |     |
| Hash            |             |     | : l3-src-dst              |     |
| LACP            | rate        |     | : slow                    |     |
| Speed           |             |     | : 1000 Mb/s               |     |
| Mode            |             |     | : trunk                   |     |
| Release         |             |     | Modification              |     |
| 10.11           |             |     | LACPfallback-staticadded. |     |
| 10.07orearlier  |             |     | --                        |     |
| Command         | Information |     |                           |     |
58
AOS-CX10.11LinkAggregationGuide| (AllSwitchSeries)

| Platforms | Command |     | context |     | Authority |
| --------- | ------- | --- | ------- | --- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show running-config |     |           |     | interface | lag |
| ------------------- | --- | --------- | --- | --------- | --- |
| show running-config |     | interface |     | lag       |     |
Description
Displaystherunningconfigurationforinterfacelag.
Examples
Displayingtherunningconfigurationforinterfacelag.
| switch#     | show  | running-config   |       | interface | lag |
| ----------- | ----- | ---------------- | ----- | --------- | --- |
| interface   | lag   | 10 multi-chassis |       |           |     |
| no shutdown |       |                  |       |           |     |
| no routing  |       |                  |       |           |     |
| vlan        | trunk | native           | 1     |           |     |
| vlan        | trunk | allowed          | 10-12 |           |     |
| lacp        | mode  | active           |       |           |     |
exit
| interface   | lag   | 11 multi-chassis |            |     |     |
| ----------- | ----- | ---------------- | ---------- | --- | --- |
| no shutdown |       |                  |            |     |     |
| no routing  |       |                  |            |     |     |
| vlan        | trunk | native           | 1          |     |     |
| vlan        | trunk | allowed          | 10-12,2001 |     |     |
| lacp        | mode  | active           |            |     |     |
exit
| interface   | lag   | 256     |     |     |     |
| ----------- | ----- | ------- | --- | --- | --- |
| description |       | VSX_ISL |     |     |     |
| no shutdown |       |         |     |     |     |
| no routing  |       |         |     |     |     |
| vlan        | trunk | native  | 1   | tag |     |
| vlan        | trunk | allowed | all |     |     |
| lacp        | mode  | active  |     |     |     |
exit
Displayingtherunningconfigurationforinterfacelagwithlacp fallback-staticconfigured.
| switch#     | show            | running-config |     | interface | lag |
| ----------- | --------------- | -------------- | --- | --------- | --- |
| interface   | lag             | 1              |     |           |     |
| no shutdown |                 |                |     |           |     |
| no routing  |                 |                |     |           |     |
| vlan        | trunk           | native         | 1   |           |     |
| vlan        | trunk           | allowed        | all |           |     |
| lacp        | mode            | active         |     |           |     |
| lacp        | fallback-static |                |     |           |     |
| shutdown    | (interface      |                |     | lag)      |     |
shutdown
no shutdown
Description
LinkAggregation|59

SetseveryinterfaceintheLAGoperationallydown.
Thenoformofthiscommandsetseveryinterfaceoperationallyup.
Examples
SettingeveryinterfaceintheLAGtoshutdown:
| switch(config)#        | interface | lag 1    |     |
| ---------------------- | --------- | -------- | --- |
| switch(config-lag-if)# |           | shutdown |     |
ResettingeveryinterfaceintheLAGtothedefault(up):
| switch(config)#        | interface | lag 1       |     |
| ---------------------- | --------- | ----------- | --- |
| switch(config-lag-if)# |           | no shutdown |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-lag-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| vlan trunk        | native             | (LAG) |     |
| ----------------- | ------------------ | ----- | --- |
| vlan trunk native | <VLAN-ID>          |       |     |
| no vlan trunk     | native [<VLAN-ID>] |       |     |
Description
AssignsanativeVLANIDtoaLAGinterface.
ThenoformofthiscommandremovesanativeVLANfromaLAGinterfaceandassignsVLANID1asits
nativeVLAN.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-ID> SpecifiesthenumberoftheVLANIDtoassign.TheVLANIDmust
exist.
MaximumnumberofVLANssupported:512(4100i)
MaximumnumberofVLANssupported:512(6000and6100)
MaximumnumberofVLANssupported:2048(6200)
MaximumnumberofVLANssupported:4096(6300,6400)
MaximumnumberofVLANssupported:4096(8320)
60
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
MaximumnumberofVLANssupported:4096(8325)
MaximumnumberofVLANssupported:4096(10000)
MaximumnumberofVLANssupported:4096(9300)
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
Configuringalayer2dynamicaggregationgroupwithnativeVLANID1assignedtoLAG1:
For6000,6100,and6200switchseries:
| switch(config)#        | interface | lag 1       |           |
| ---------------------- | --------- | ----------- | --------- |
| switch(config-lag-if)# |           | no shutdown |           |
| switch(config-lag-if)# |           | lacp mode   | active    |
| switch(config-lag-if)# |           | vlan trunk  | native 1  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 1 |
For6300,6400,8320,8325,8360,8400,9300,and10000switchseries:
| switch(config)#        | interface | lag 1       |           |
| ---------------------- | --------- | ----------- | --------- |
| switch(config-lag-if)# |           | no shutdown |           |
| switch(config-lag-if)# |           | no routing  |           |
| switch(config-lag-if)# |           | lacp mode   | active    |
| switch(config-lag-if)# |           | vlan trunk  | native 1  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 1 |
Configuringalayer2dynamicaggregationgroupwithnativeVLANID20assignedtoLAG1:
For6000,6100,and6200switchseries:
| switch(config)#        | interface | lag 1       |            |
| ---------------------- | --------- | ----------- | ---------- |
| switch(config-lag-if)# |           | no shutdown |            |
| switch(config-lag-if)# |           | lacp mode   | active     |
| switch(config-lag-if)# |           | vlan trunk  | native 20  |
| switch(config-lag-if)# |           | vlan trunk  | allowed 20 |
For6300,6400,8320,8325,8360,8400,9300,and10000switchseries:
| switch(config)#        | interface | lag 1       |        |
| ---------------------- | --------- | ----------- | ------ |
| switch(config-lag-if)# |           | no shutdown |        |
| switch(config-lag-if)# |           | no routing  |        |
| switch(config-lag-if)# |           | lacp mode   | active |
LinkAggregation|61

| switch(config-lag-if)# |     | vlan trunk | native 20  |
| ---------------------- | --- | ---------- | ---------- |
| switch(config-lag-if)# |     | vlan trunk | allowed 20 |
RemovinganativeVLANfromLAG1:
| switch(config)#        | interface | lag     | 1            |
| ---------------------- | --------- | ------- | ------------ |
| switch(config-lag-if)# |           | no vlan | trunk native |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-lag-if |     | forthiscommand. |
| --- | ------------- | --- | --------------- |
62
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

Chapter 3

Smartlink

Smartlink

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

Smartlink is supported by the following switch platforms:

n 6000 Switch Series

n 6100 Switch Series

n 6200 Switch Series

n 6300 Switch Series

n 6400 Switch Series

n 8360 Switch Series

Benefits

Smartlink provides faster failover compared to STP. If an active link fails, a Smartlink group contains
configuration information that determines which port should be forwarding for a protected VLAN group.

Guidelines and limitations

n For faster convergence of routed traffic over Smartlink ports, ip neighbor-flood must be enabled on

respective SVI interfaces.

n Smartlink uses ERPS copp class for flush packets.

n The Aruba 6000 and 6100 Switch Series use separate Smartlink coPP policies as ERPS is not

supported in matrix platforms.

Limitations:

n VSX, ISL and MCLAGs cannot be included in Smartlink groups.

n Switches with both Smartlink and STP enabled exclude Smartlink ports from STP.

n On switches with both Smartlink and STP enabled, loops involving Smartlink and STP are not

detected.

n On switches with both Smartlink and ERPS enabled, loops involving Smartlink and ERPS are not

detected.

AOS-CX 10.11 Link Aggregation Guide | (All Switch Series)

63

n ERPS and Smartlink cannot be enabled on the same port.

n Dynamic VLANs (MVRP) and Smartlink cannot be enabled on the same port.

n Loop Protect and Smartlink cannot be enabled on the same port.

n Multicast fast convergence is not supported.

n Uplink Failure Detection (UFD) is not supported.

n MIB and WebUI are not supported.

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

The no form of this command removes the Smartlink group and all associated configurations for a
specified ID.

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

For more information on features that use this command, refer to the Link Aggregation Guide for your switch

model.

Command History

Smartlink | 64

| Release        |             |     |         | Modification |     |
| -------------- | ----------- | --- | ------- | ------------ | --- |
| 10.07orearlier |             |     |         | --           |     |
| Command        | Information |     |         |              |     |
| Platforms      | Command     |     | context | Authority    |     |
6000 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6100 |     |     |     | forthiscommand. |     |
| ---- | --- | --- | --- | --------------- | --- |
6200
6300
6400
8360
| smartlink    | recv-control-vlan |     |            |     |     |
| ------------ | ----------------- | --- | ---------- | --- | --- |
| smartlink    | recv-control-vlan |     | <VID-LIST> |     |     |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |     |     |              |     |
| -------------- | ----------- | --- | --- | ------------ | --- |
| Release        |             |     |     | Modification |     |
| 10.07orearlier |             |     |     | --           |     |
| Command        | Information |     |     |              |     |
65
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- |

| Platforms | Command | context |     | Authority |     |     |
| --------- | ------- | ------- | --- | --------- | --- | --- |
6000 config Administratorsorlocalusergroupmemberswithexecutionrights
| 6100 |     |     |     | forthiscommand. |     |     |
| ---- | --- | --- | --- | --------------- | --- | --- |
6200
6300
6400
8360
| Group       | context    | commands |     |     |     |     |
| ----------- | ---------- | -------- | --- | --- | --- | --- |
| description | (smartlink | group)   |     |     |     |     |
| description | <DESC>     |          |     |     |     |     |
no description
Description
AddsdescriptiontoaSmartlinkgroup.
ThenoformofthiscommandremovesadescriptionfromaSmartlinkgroup.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
<DESC>
SpecifiesdescriptionforaSmartlinkgroup.1to64printableASCII
charactersareallowed.
Examples
AddingadescriptiontoaSmartlinkgroup:
| switch(config)#             |     | smartlink | group       | 3   |           |     |
| --------------------------- | --- | --------- | ----------- | --- | --------- | --- |
| switch(config-smartlink-3)# |     |           | Description |     | for group | 3   |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |         |     |              |           |     |
| -------------- | ----------- | ------- | --- | ------------ | --------- | --- |
| Release        |             |         |     | Modification |           |     |
| 10.07orearlier |             |         |     | --           |           |     |
| Command        | Information |         |     |              |           |     |
| Platforms      | Command     | context |     |              | Authority |     |
6000 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6100 |     |     |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | ------------------------------ | --- |
6200
6300
6400
8360
Smartlink|66

| diag-dump | smartlink |     | basic |     |     |     |     |     |     |     |
| --------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| diag-dump | smartlink |     | basic |     |     |     |     |     |     |     |
Description
DumpstheSmartlinkconfiguration,stateandstatistics.
Examples
DumpofSmartlinkconfiguration,state,andstatistics:
| switch# | diag-dump |     | smartlink |     | basic |     |     |     |     |     |
| ------- | --------- | --- | --------- | --- | ----- | --- | --- | --- | --- | --- |
=========================================================================
| [Start] | Feature |     | smartlink |     | Time | : Tue | Jul | 7 10:08:31 | 2020 |     |
| ------- | ------- | --- | --------- | --- | ---- | ----- | --- | ---------- | ---- | --- |
=========================================================================
-------------------------------------------------------------------------
| [Start] | Daemon |     | smartlinkd |     |     |     |     |     |     |     |
| ------- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
SL Group 1: Primary port 1/1/1 Secondary port 1/1/2 Control VLAN 4,
|     |     | Preemption |     | disabled, |     | Preemption-delay |     |     | 1 Preemption | Timer OFF, |
| --- | --- | ---------- | --- | --------- | --- | ---------------- | --- | --- | ------------ | ---------- |
State primary_with_backup, Active port PRIMARY, Backup port SECONDARY
| Port | 1/1/1: | member_groups |     |     | 1 SL | Groups | ids: | 1, 0 |     |     |
| ---- | ------ | ------------- | --- | --- | ---- | ------ | ---- | ---- | --- | --- |
| Port | 1/1/2: | member_groups |     |     | 1 SL | Groups | ids: | 1, 0 |     |     |
or
| SL  | Group | 1: Primary |     | port | lag1 | (mclag: | local_up_remote_up) |     |     |     |
| --- | ----- | ---------- | --- | ---- | ---- | ------- | ------------------- | --- | --- | --- |
Secondary port lag2 (mclag: local_down_remote_up), Control VLAN 4,
|     |     | Preemption |     | disabled, |     | Preemption-delay |     |     | 1 Preemption | Timer OFF, |
| --- | --- | ---------- | --- | --------- | --- | ---------------- | --- | --- | ------------ | ---------- |
State primary_with_backup, Active port PRIMARY, Backup port SECONDARY
| Port | lag1: | member_groups |                      |     | 1 SL | Groups | ids: | 1, 0 |     |     |
| ---- | ----- | ------------- | -------------------- | --- | ---- | ------ | ---- | ---- | --- | --- |
| Port | lag2: | member_groups |                      |     | 1 SL | Groups | ids: | 1, 0 |     |     |
| VSX  | Oper  | Status:       | Primary/Secondary/NA |     |      |        |      |      |     |     |
-------------------------------------------------------------------------
| [End] | Daemon | smartlinkd |     |     |     |     |     |     |     |     |
| ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
-------------------------------------------------------------------------
| [Start] | Daemon |     | ops-switchd |     |     |     |     |     |     |     |
| ------- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
Group-ID | Port Name | Port Status | Vlan-ID | HW-Port-State | Vlan-Type
| 1   |     | | 1/1/1 |     | | Active |     |     | | 4 | |   | Forwarding | | Control   |
| --- | --- | ------- | --- | -------- | --- | --- | --- | --- | ---------- | ----------- |
| 1   |     | | 1/1/1 |     | | Active |     |     | | 3 | |   | Forwarding | | Protected |
| 1   |     | | 1/1/1 |     | | Active |     |     | | 2 | |   | Forwarding | | Protected |
| 1   |     | | 1/1/1 |     | | Active |     |     | | 1 | |   | Forwarding | | Protected |
| 1   |     | | 1/1/2 |     | | Backup |     |     | | 4 | |   | Blocking   | | Control   |
| 1   |     | | 1/1/2 |     | | Backup |     |     | | 3 | |   | Blocking   | | Protected |
| 1   |     | | 1/1/2 |     | | Backup |     |     | | 2 | |   | Blocking   | | Protected |
| 1   |     | | 1/1/2 |     | | Backup |     |     | | 1 | |   | Blocking   | | Protected |
-------------------------------------------------------------------------
| [End] | Daemon | ops-switchd |     |     |     |     |     |     |     |     |
| ----- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------
=========================================================================
| [End] | Feature | smartlink |     |     |     |     |     |     |     |     |
| ----- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
=========================================================================
| Diagnostic-dump |     |     | captured |     | for feature |     | smartlink |     |     |     |
| --------------- | --- | --- | -------- | --- | ----------- | --- | --------- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
67
| AOS-CX10.11LinkAggregationGuide| |     |     | (AllSwitchSeries) |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |

| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6000 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | ------------------------------------- | --- |
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
| Parameter        |     |     | Description                       |     |
| ---------------- | --- | --- | --------------------------------- | --- |
| <INTERFACE-NAME> |     |     | Specifiesinterfaceforprimaryport. |     |
Examples
ConfiguringprimaryportforaSmartlinkgroup:
| switch(config)#             | smartlink |     | group 3      |       |
| --------------------------- | --------- | --- | ------------ | ----- |
| switch(config-smartlink-3)# |           |     | primary-port | 1/1/1 |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |     |     |              |     |
| ------------------- | --- | --- | ------------ | --- |
| Release             |     |     | Modification |     |
| 10.07orearlier      |     |     | --           |     |
| Command Information |     |     |              |     |
Smartlink|68

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
6000 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6100 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6200
6300
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
| switch(config)#             | smartlink |     | group 3        |       |
| --------------------------- | --------- | --- | -------------- | ----- |
| switch(config-smartlink-3)# |           |     | secondary-port | 1/1/2 |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6000 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6100 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8360
control-vlan
| control-vlan | <VLAN-ID> |     |     |     |
| ------------ | --------- | --- | --- | --- |
69
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------- | --- | --- |

| no control-vlan | <VLAN-ID> |     |     |     |
| --------------- | --------- | --- | --- | --- |
Description
ConfigurescontrolVLANinaSmartlinkgroup.
ThenoformofthiscommandremovescontrolVLANfromaSmartlinkgroup.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<VLAN-ID>
SpecifiesVLANIDforaSmartlinkgroup.
Usage
n InaSmartlinkgroup,thecontrolVLAN isusedtosendflushmessages.
ControlVLANisconfiguredonthedeviceintendedtosendflushmessages.
n
n EachSmartlinkgroupmustuseauniquecontrolVLAN.
n ControlVLANisprotectedintheSmartlinkgrouptoavoidloops.
Examples
ConfiguringcontrolVLAN inaSmartlinkgroup:
| switch(config)#             | smartlink |     | group 3      |     |
| --------------------------- | --------- | --- | ------------ | --- |
| switch(config-smartlink-3)# |           |     | control-vlan | 10  |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
6000 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6100 |     |     |     | executionrightsforthiscommand. |
| ---- | --- | --- | --- | ------------------------------ |
6200
6300
6400
8360
protected-vlans
| protected-vlans    | <VLAN-ID-LIST> |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
| no protected-vlans | <VLAN-ID-LIST> |     |     |     |
Description
SpecifiesVLANsprotectedbyaSmartlinkgroup.
Smartlink|70

ThenoformofthiscommandremovesVLANsprotectedbyaSmartlinkgroup.
| Parameter      |     |     | Description                            |     |
| -------------- | --- | --- | -------------------------------------- | --- |
| <VLAN-ID-LIST> |     |     | SpecifieslistofVLANIDs.Rangeis1to4094. |     |
Examples
ConfiguringprotectedVLANsforaSmartlinkgroup.:
| switch(config)#             | smartlink |     | group 3         |          |
| --------------------------- | --------- | --- | --------------- | -------- |
| switch(config-smartlink-3)# |           |     | protected-vlans | 1, 10-50 |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
config-smartlink-<GROUP>
| 6000 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
| 6100 |     |     |     | executionrightsforthiscommand.            |
6200
6300
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
Ifpreemptionisdisabled,arecoveredprimaryportservesasabackupinterfaceanddoesnot
n
forwardtraffic.
Examples
ConfiguringpreemptioninaSmartlinkgroup:
71
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------- | --- | --- |

| switch(config)# | smartlink |     | group 3 |     |
| --------------- | --------- | --- | ------- | --- |
switch(config-smartlink-3)#
preemption
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |           |
| ------------------- | ------- | ------- | ------------ | --------- |
| Release             |         |         | Modification |           |
| 10.07orearlier      |         |         | --           |           |
| Command Information |         |         |              |           |
| Platforms           | Command | context |              | Authority |
config-smartlink-<GROUP>
| 6000 |     |     |     | Administratorsorlocalusergroupmemberswith |
| ---- | --- | --- | --- | ----------------------------------------- |
| 6100 |     |     |     | executionrightsforthiscommand.            |
6200
6300
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
<SECONDS>
Specifiespreemptiondelayinseconds.Rangeis0to300seconds.
Usage
Whenpreemptionisenabled,arecoveredprimaryportalwayspreemptstheactiveinterfaceafterthe
configuredpreemptiondelay.
Examples
ConfiguringpreemptiondelayonaSmartlinkgroup:
| switch(config)#             | smartlink |     | group 3          |     |
| --------------------------- | --------- | --- | ---------------- | --- |
| switch(config-smartlink-3)# |           |     | preemption       |     |
| switch(config-smartlink-3)# |           |     | preemption-delay | 10  |
Smartlink|72

Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |     |         |              |           |     |
| -------------- | ----------- | --- | ------- | ------------ | --------- | --- |
| Release        |             |     |         | Modification |           |     |
| 10.07orearlier |             |     |         | --           |           |     |
| Command        | Information |     |         |              |           |     |
| Platforms      | Command     |     | context |              | Authority |     |
6000 config-smartlink-<GROUP> Administratorsorlocalusergroupmemberswith
| 6100 |     |     |     |     | executionrightsforthiscommand. |     |
| ---- | --- | --- | --- | --- | ------------------------------ | --- |
6200
6300
6400
8360
| Display        | commands |            |     |     |     |     |
| -------------- | -------- | ---------- | --- | --- | --- | --- |
| show smartlink | group    |            |     |     |     |     |
| show smartlink | group    | <GROUP-ID> |     |     |     |     |
Description
ShowsinformationforaspecificSmartlinkgroup.
| Parameter  |     |     |     | Description                |     |     |
| ---------- | --- | --- | --- | -------------------------- | --- | --- |
| <GROUP-ID> |     |     |     | SpecifiesSmartlinkgroupID. |     |     |
Examples
ShowingSmartlinkgroupinformation:
| switch#   | show smartlink |                | group | 1   |     |     |
| --------- | -------------- | -------------- | ----- | --- | --- | --- |
| Smartlink | Group          | 1 Information: |       |     |     |     |
=============================
| Group description |       |       |     | : Uplink1   |            |      |
| ----------------- | ----- | ----- | --- | ----------- | ---------- | ---- |
| Protected         | VLANs |       |     | : 20-30     |            |      |
| Control           | VLAN  |       |     | : 10        |            |      |
| Preemption        |       |       |     | : ON        |            |      |
| Preemption        | Delay |       |     | : 10        |            |      |
| Ports             | Role  | State |     | Flush Count | Last Flush | Time |
------ --------- ---------- ----------- -------------------------
| 1/1/1 | Primary   | Active |     | 2   | Sat Oct | 17 19:09:10 2020 |
| ----- | --------- | ------ | --- | --- | ------- | ---------------- |
| 1/1/2 | Secondary | Backup |     | 0   |         |                  |
73
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- | --- |

Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
6000 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- |
6300
6400
8360
| show smartlink | group     | all |     |     |     |
| -------------- | --------- | --- | --- | --- | --- |
| show smartlink | group all |     |     |     |     |
Description
ShowsinformationforallconfiguredSmartlinkgroups.
Examples
ShowinginformationforallconfiguredSmartlinkgroups:
| switch#   | show smartlink     | group all |     |     |     |
| --------- | ------------------ | --------- | --- | --- | --- |
| Smartlink | Group Information: |           |     |     |     |
=============================
| Primary  | Secondary | Active | Backup Ctrl | Preemption | Preemption |
| -------- | --------- | ------ | ----------- | ---------- | ---------- |
| Grp Port | Port      | Port   | Port Vlan   |            | Delay      |
---- ------- --------- ------ ------- --------- ---------- ----------
| 1 1/1/1 | 1/1/2 | 1/1/1 | 1/1/2 10 | OFF | 1   |
| ------- | ----- | ----- | -------- | --- | --- |
| 2 1/1/5 | 1/1/6 | 1/1/5 | 1/1/6 11 | OFF | 1   |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |     |     |              |     |     |
| ------------------- | --- | --- | ------------ | --- | --- |
| Release             |     |     | Modification |     |     |
| 10.07orearlier      |     |     | --           |     |     |
| Command Information |     |     |              |     |     |
Smartlink|74

| Platforms | Command | context | Authority                                            |     |     |
| --------- | ------- | ------- | ---------------------------------------------------- | --- | --- |
| 6000      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |
Operator(>)orManager
6100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- |
6300
6400
8360
| show smartlink | group        | detail |     |     |     |
| -------------- | ------------ | ------ | --- | --- | --- |
| show smartlink | group detail |        |     |     |     |
Description
ShowsdetailedinformationforallconfiguredSmartlinkgroups.
Examples
ShowingdetailedinformationforallconfiguredSmartlinkgroups:
| switch#   | show smartlink | group detail |     |     |     |
| --------- | -------------- | ------------ | --- | --- | --- |
| Smartlink | Group 1        | Information: |     |     |     |
===============================
| Protected  | VLAN  | :     | 1-3         |            |      |
| ---------- | ----- | ----- | ----------- | ---------- | ---- |
| Control    | VLAN  | :     | 1           |            |      |
| Preemption |       | :     | OFF         |            |      |
| Preemption | Delay | :     | 1           |            |      |
| Ports      | Role  | State | Flush Count | Last Flush | Time |
-------- ------------ ------------ ------------ ------------------------
| 1/3/1     | Primary   | Backup       | 0   |     |     |
| --------- | --------- | ------------ | --- | --- | --- |
| 1/3/2     | Secondary | Active       | 0   |     |     |
| Smartlink | Group 2   | Information: |     |     |     |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |     |              |     |     |
| -------------- | ----------- | --- | ------------ | --- | --- |
| Release        |             |     | Modification |     |     |
| 10.07orearlier |             |     | --           |     |     |
| Command        | Information |     |              |     |     |
75
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- |

| Platforms | Command | context | Authority                                            |     |     |     |
| --------- | ------- | ------- | ---------------------------------------------------- | --- | --- | --- |
| 6000      |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |     |     |     |
Operator(>)orManager
6100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- | --- |
6300
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
| Flush Packets | Received     |                       |          | : 2             |             |      |
| ------------- | ------------ | --------------------- | -------- | --------------- | ----------- | ---- |
| Last Flush    | Packet       | Received On Interface |          | : 1/1/1         |             |      |
| Last Flush    | Packet       | Received On           |          | : Sat Oct       | 17 19:09:10 | 2020 |
| Device        | Id Of Last   | Flush Packet          | Received | : 5065f3-127080 |             |      |
| Control       | VLAN Of Last | Flush Packet          | Received | : 10            |             |      |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |         |              |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| Release        |             |         | Modification |     |     |     |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
6000 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |     |     |     |
| ---- | --- | --- | ------------------------------------- | --- | --- | --- |
6300
6400
8360
Smartlink|76

| clear smartlink | group | statistics   |            |
| --------------- | ----- | ------------ | ---------- |
| clear smartlink | group | [<GROUP-ID>] | statistics |
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
| switch(config)# | clear | smartlink | group statistics |
| --------------- | ----- | --------- | ---------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |                                                      |
| ------------------- | ------- | ------- | ---------------------------------------------------- |
| Release             |         |         | Modification                                         |
| 10.07orearlier      |         |         | --                                                   |
| Command Information |         |         |                                                      |
| Platforms           | Command | context | Authority                                            |
| 6000                |         |         | OperatorsorAdministratorsorlocalusergroupmemberswith |
Operator(>)orManager
6100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     | commandfromtheoperatorcontext(>)only. |
| ---- | --- | --- | ------------------------------------- |
6300
6400
8360
| clear smartlink | flush-statistics |     |     |
| --------------- | ---------------- | --- | --- |
| clear smartlink | flush-statistics |     |     |
Description
ClearsSmartlinkflushstatistics.
Usage
Thiscommandmustbeexecutedontheuplinkdeviceconfiguredwithrecv-control-vlan.
77
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

Examples
ClearingSmartlinkflushstatistics:
switch#
|     | clear smartlink | flush-statistics |     |     |     |
| --- | --------------- | ---------------- | --- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |     |              |     |
| ------------------- | ------- | ------- | --- | ------------ | --- |
| Release             |         |         |     | Modification |     |
| 10.07orearlier      |         |         |     | --           |     |
| Command Information |         |         |     |              |     |
| Platforms           | Command | context |     | Authority    |     |
6000 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
6100 (#) executionrightsforthiscommand.Operatorscanexecutethis
| 6200 |     |     |     | commandfromtheoperatorcontext(>)only. |     |
| ---- | --- | --- | --- | ------------------------------------- | --- |
6300
6400
8360
| show running-config | (smartlink) |     |     |     |     |
| ------------------- | ----------- | --- | --- | --- | --- |
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
Smartlink|78

!
!
| smart-link      | group 1 |       |     |     |
| --------------- | ------- | ----- | --- | --- |
| primary-port    | 1/1/1   |       |     |     |
| secondary-port  | 1/1/2   |       |     |     |
| control-vlan    | 10      |       |     |     |
| protected-vlans |         | 20-30 |     |     |
preemption
| preemption-delay |     | 10  |     |     |
| ---------------- | --- | --- | --- | --- |
exit
| smart-link      | group 2 |       |     |     |
| --------------- | ------- | ----- | --- | --- |
| primary-port    | 1/1/8   |       |     |     |
| secondary-port  | 1/1/9   |       |     |     |
| control-vlan    | 11      |       |     |     |
| protected-vlans |         | 20-30 |     |     |
exit
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
6000 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 6100 |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| ---- | --- | --- | ----------------------------------------------------- | --- |
(#)
commandfromtheoperatorcontext(>)only.
6200
6300
6400
8360
| Supportability  | commands  |                          |     |           |
| --------------- | --------- | ------------------------ | --- | --------- |
| show capacities | smartlink |                          |     |           |
| show capacities | smartlink | | show capacities-status |     | smartlink |
Description
ShowsSmartlinkcapacitiesorSmartlinkcapacitiesandstatus.
Examples
ShowingSmartlinkcapacities:
| switch#            | show capacities | smartlink        |     |     |
| ------------------ | --------------- | ---------------- | --- | --- |
| System Capacities: |                 | Filter SMARTLINK |     |     |
79
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------- | --- | --- |

| Capacities | Name |     |     |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- | --- | --- |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command        | History     |         |         |     |              |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- |
| Release        |             |         |         |     | Modification |     |     |
| 10.07orearlier |             |         |         |     | --           |     |     |
| Command        | Information |         |         |     |              |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |
6000 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
| 6100 |     |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| ---- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
(#)
commandfromtheoperatorcontext(>)only.
6200
6300
6400
8360
Smartlink|80

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

AOS-CX 10.11 Link Aggregation Guide | (All Switch Series)

81

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
UFD(UplinkFailureDetection)|82

| switch(config)# | no  | ufd enable |     |     |
| --------------- | --- | ---------- | --- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.09               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
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
| switch(config)#       | ufd | enable           |     |             |
| --------------------- | --- | ---------------- | --- | ----------- |
| switch(config)#       | ufd | session-id       | 1   |             |
| switch(config-ufd-1)# |     | links-to-monitor |     | 1/1/1,1/1/2 |
switch(config-ufd-1)#
|                       |     | links-to-disable |         | 1/1/11,1/1/12 |
| --------------------- | --- | ---------------- | ------- | ------------- |
| switch(config-ufd-1)# |     | delay            | down 10 |               |
| switch(config-ufd-1)# |     | delay            | up 10   |               |
| switch(config-ufd-1)# |     | exit             |         |               |
switch(config)#
CreatingUFDsession2andthenenteringitscontext:
| switch(config)#       | ufd | session-id       | 2   |             |
| --------------------- | --- | ---------------- | --- | ----------- |
| switch(config-ufd-2)# |     | links-to-monitor |     | lag18-lag20 |
83
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------- | --- | --- |

| switch(config-ufd-2)# |     | links-to-disable | 1/1/3-1/1/5 |
| --------------------- | --- | ---------------- | ----------- |
switch(config-ufd-2)#
exit
switch(config)#
DeletingUFDsession1:
| switch(config)# | no  | ufd session-id | 1   |
| --------------- | --- | -------------- | --- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.09               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
links-to-monitor
| links-to-monitor    | <IF/LAG-LIST> |     |     |
| ------------------- | ------------- | --- | --- |
| no links-to-monitor | <IF/LAG-LIST> |     |     |
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
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<IF/LAG-LIST> ListofL2interfacesorLAGs.Separateinterfaces/LAGswith
commas(forindividualinterfaces/LAGs)orhyphens(fora
consecutiverangeofinterfaces/LAGs).
Examples
UFD(UplinkFailureDetection)|84

ConfiguringtwouplinkstomonitorforUFDsession1:
| switch(config)#       | ufd | enable           |         |               |
| --------------------- | --- | ---------------- | ------- | ------------- |
| switch(config)#       | ufd | session-id       | 1       |               |
| switch(config-ufd-1)# |     | links-to-monitor |         | 1/1/1,1/1/2   |
| switch(config-ufd-1)# |     | links-to-disable |         | 1/1/11,1/1/12 |
| switch(config-ufd-1)# |     | delay            | down 10 |               |
| switch(config-ufd-1)# |     | delay            | up 10   |               |
switch(config-ufd-1)#
exit
switch(config)#
ConfiguringarangeofuplinkLAGstomonitorforUFDsession2:
| switch(config)#       | ufd | session-id       | 2   |             |
| --------------------- | --- | ---------------- | --- | ----------- |
| switch(config-ufd-2)# |     | links-to-monitor |     | lag18-lag20 |
| switch(config-ufd-2)# |     | links-to-disable |     | 1/1/3-1/1/5 |
| switch(config-ufd-2)# |     | exit             |     |             |
switch(config)#
DeletingbothlinkstomonitorforUFDsession1:
| switch(config-ufd-1)# |     | no links-to-monitor |     | 1/1/1,1/1/2 |
| --------------------- | --- | ------------------- | --- | ----------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.09               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
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
85
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------- | --- | --- |

ThenoformofthiscommanddeletesthespecifiedlinkstodisablelistwithintheselectedUFD session
context.
ALAGmemberinterfacecannotbeaddedasalinktodisable.Ainterfaceconfiguredasalinktodisablecannot
beaddedasaLAGmemberinterface.
| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
<IF/LAG-LIST> ListofL2interfacesorLAGs.Separateinterfaces/LAGswith
commas(forindividualinterfaces/LAGs)orhyphens(fora
consecutiverangeofinterfaces/LAGs).
Examples
Configuringtwolinkstobedisabled:
| switch(config)# | ufd enable |     |     |
| --------------- | ---------- | --- | --- |
switch(config)#
|                       | ufd session-id   | 1       |               |
| --------------------- | ---------------- | ------- | ------------- |
| switch(config-ufd-1)# | links-to-monitor |         | 1/1/1,1/1/2   |
| switch(config-ufd-1)# | links-to-disable |         | 1/1/11,1/1/12 |
| switch(config-ufd-1)# | delay            | down 10 |               |
| switch(config-ufd-1)# | delay            | up 10   |               |
| switch(config-ufd-1)# | exit             |         |               |
switch(config)#
Configuringarangeofinterfacestodisable:
| switch(config)# | ufd session-id | 2   |     |
| --------------- | -------------- | --- | --- |
switch(config-ufd-2)#
|                       | links-to-monitor |     | lag18-lag20 |
| --------------------- | ---------------- | --- | ----------- |
| switch(config-ufd-2)# | links-to-disable |     | 1/1/3-1/1/5 |
| switch(config-ufd-2)# | exit             |     |             |
switch(config)#
Deletingthelinkstodisablefortwointerfaces:
| switch(config-ufd-1)# | no links-to-disable |     | 1/1/11,1/1/12 |
| --------------------- | ------------------- | --- | ------------- |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
Command History
| Release |     | Modification       |     |
| ------- | --- | ------------------ | --- |
| 10.09   |     | Commandintroduced. |     |
Command Information
UFD(UplinkFailureDetection)|86

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
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
UFDdisablestheinterfaces/LAGsconfiguredasLinks-to-Disable(LtD).Similarly,withdelay up 10,If
any of the LtM links come back upandremainupafter10seconds,thenalltheLtDlinksarebrought
backup.
Inadditiontoanyconfigureddelaythereisanadditionaldelayof3to5secondsbeforebringinganyLinks-to-
Disable(LtD)downorbackup.Sowiththedefaultdelayof0seconds,adelayof3to5secondsdoesoccur.
Thenoformofthiscommandrestoresthedelaytoitsdefaultof0seconds.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<DELAY>
Speciesthedelayinseconds.Range0to180seconds.Default:0
seconds.
Examples
Settingtheupanddowndelaysto10seconds:
switch(config)#
|                       | ufd | enable           |         |               |
| --------------------- | --- | ---------------- | ------- | ------------- |
| switch(config)#       | ufd | session-id       | 1       |               |
| switch(config-ufd-1)# |     | links-to-monitor |         | 1/1/1,1/1/2   |
| switch(config-ufd-1)# |     | links-to-disable |         | 1/1/11,1/1/12 |
| switch(config-ufd-1)# |     | delay            | down 10 |               |
| switch(config-ufd-1)# |     | delay            | up 10   |               |
| switch(config-ufd-1)# |     | exit             |         |               |
switch(config)#
Resettingtheupanddowndelaystotheirdefaultof0:
switch(config-ufd-1)#
|                       |     | no delay | down  | 10  |
| --------------------- | --- | -------- | ----- | --- |
| switch(config-ufd-1)# |     | no delay | up 10 |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
87
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |
| -------------------------------- | --- | ----------------- | --- | --- |

| Release             |         |         | Modification       |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| 10.09               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
Allplatforms config-ufd-<ID> Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show ufd
| show ufd [session-id |     | <ID>] |     |     |
| -------------------- | --- | ----- | --- | --- |
Description
ShowsinformationonallUFDsessionsorthespecifiedUFDsession.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<ID>
SpecifiesanexistingUFD sessionID.Range:1to128.
Example
ShowinginformationonallconfiguredUFDsessions:
switch#
show ufd
| Global UFD            | Status | : Enabled |                 |             |
| --------------------- | ------ | --------- | --------------- | ----------- |
| UFD session-id        |        |           | : 1             |             |
| UFD Links-to-Monitor  |        | status    | : Up            |             |
| Up Delay              |        |           | : 10 sec        |             |
| Down Delay            |        |           | : 10 sec        |             |
| Links-to-Monitor      |        |           | : 1/1/1,1/1/2   |             |
| Links-to-Disable      |        |           | : 1/1/11,1/1/12 |             |
| Last Links-to-Monitor |        | Down Time | : 2021-11-03    | 15:22:05:37 |
| UFD session-id        |        |           | : 2             |             |
| UFD Links-to-Monitor  |        | status    | : Up            |             |
| Up Delay              |        |           | : 5 sec         |             |
| Down Delay            |        |           | : 5 sec         |             |
| Links-to-Monitor      |        |           | : lag18-lag20   |             |
| Links-to-Disable      |        |           | : 1/1/3-1/1/5   |             |
| Last Links-to-Monitor |        | Down Time | : 2021-11-01    | 12:14:42:56 |
ShowinginformationonUFDsession2:
switch#
|                      | show ufd session | 2      |               |     |
| -------------------- | ---------------- | ------ | ------------- | --- |
| UFD session-id       |                  |        | : 2           |     |
| UFD Links-to-Monitor |                  | status | : Up          |     |
| Up Delay             |                  |        | : 5 sec       |     |
| Down Delay           |                  |        | : 5 sec       |     |
| Links-to-Monitor     |                  |        | : lag18-lag20 |     |
UFD(UplinkFailureDetection)|88

| Links-to-Disable      |     |      |      | : 1/1/3-1/1/5 |             |     |     |
| --------------------- | --- | ---- | ---- | ------------- | ----------- | --- | --- |
| Last Links-to-Monitor |     | Down | Time | : 2021-11-01  | 12:14:42:56 |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
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
| show capacities        |     | ufd |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| show capacities        | ufd |     |     |     |     |     |     |
| show capacities-status |     | ufd |     |     |     |     |     |
Description
Commandshow capacities ufdshowsUFDsessioncapacity.Commandshow capacities-status ufd
showsUFDsessioncapacityandthenumberofUFDsessionsconfigured.
Example
ShowingUFDsessioncapacity:
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
89
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |     |     |     |     |
| -------------------------------- | --- | ----------------- | --- | --- | --- | --- | --- |

Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |                    |     |
| ------------------- | ------- | ------- | ------------------ | --- |
| Release             |         |         | Modification       |     |
| 10.09               |         |         | Commandintroduced. |     |
| Command Information |         |         |                    |     |
| Platforms           | Command | context | Authority          |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show running-config |     | ufd |     |     |
| ------------------- | --- | --- | --- | --- |
| show running-config | ufd |     |     |     |
Description
ShowstherunningconfigurationforUFD.
Example
ShowingtheUFDportionofrunningconfigurationinformation:
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
| switch# | show running-config |     | ufd |     |
| ------- | ------------------- | --- | --- | --- |
| Current | configuration:      |     |     |     |
ufd enable
| ufd session-id   | 1       |               |     |     |
| ---------------- | ------- | ------------- | --- | --- |
| delay            | up 10   |               |     |     |
| delay            | down 10 |               |     |     |
| links-to-monitor |         | 1/1/1,1/1/2   |     |     |
| links-to-disable |         | 1/1/11,1/1/12 |     |     |
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History |     |     |     |     |
| --------------- | --- | --- | --- | --- |
UFD(UplinkFailureDetection)|90

| Release   |             |         | Modification       |
| --------- | ----------- | ------- | ------------------ |
| 10.09     |             |         | Commandintroduced. |
| Command   | Information |         |                    |
| Platforms | Command     | context | Authority          |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show tech | ufd |     |     |
| --------- | --- | --- | --- |
| show tech | ufd |     |     |
Description
Executestheshow ufdcommandfollowedbytheshow running-config ufdcommand.
Example
Runningtheshow ufdcommandfollowedbytheshow running-config ufdcommand:
| switch# | show tech | ufd |     |
| ------- | --------- | --- | --- |
====================================================
| Show Tech | executed | on Tue Nov | 23 11:32:08 2021 |
| --------- | -------- | ---------- | ---------------- |
====================================================
====================================================
| [Begin] | Feature ufd |     |     |
| ------- | ----------- | --- | --- |
====================================================
*********************************
| Command | : show ufd |     |     |
| ------- | ---------- | --- | --- |
*********************************
| Global                | UFD Status | : Enabled |             |
| --------------------- | ---------- | --------- | ----------- |
| UFD session-id        |            |           | : 10        |
| UFD Links-to-Monitor  |            | status    | : Up        |
| Up Delay              |            |           | : 20 sec    |
| Down Delay            |            |           | : 10 sec    |
| Links-to-Monitor      |            |           | : None      |
| Links-to-Disable      |            |           | : None      |
| Last Links-to-Monitor |            | Down      | Time : None |
| UFD session-id        |            |           | : 20        |
| UFD Links-to-Monitor  |            | status    | : Up        |
| Up Delay              |            |           | : 0 sec     |
| Down Delay            |            |           | : 0 sec     |
| Links-to-Monitor      |            |           | : None      |
| Links-to-Disable      |            |           | : None      |
| Last Links-to-Monitor |            | Down      | Time : None |
*********************************
| Command | : show running-config |     | ufd |
| ------- | --------------------- | --- | --- |
*********************************
ufd enable
| ufd session-id | 10  |     |     |
| -------------- | --- | --- | --- |
91
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

| delay | down | 10  |     |     |     |
| ----- | ---- | --- | --- | --- | --- |
| delay | up   | 20  |     |     |     |
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
Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
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
DisablingUFDdebuglogs:
| switch(config)# |     | no  | debug | ufd all |     |
| --------------- | --- | --- | ----- | ------- | --- |
UFD(UplinkFailureDetection)|92

Formoreinformationonfeaturesthatusethiscommand,refertotheLinkAggregationGuideforyourswitch
model.
| Command History     |         |         |                    |
| ------------------- | ------- | ------- | ------------------ |
| Release             |         |         | Modification       |
| 10.09               |         |         | Commandintroduced. |
| Command Information |         |         |                    |
| Platforms           | Command | context | Authority          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
93
| AOS-CX10.11LinkAggregationGuide| |     | (AllSwitchSeries) |     |
| -------------------------------- | --- | ----------------- | --- |

Support and Other Resources

Chapter 5

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

https://community.arubanetworks.com/

https://www.arubanetworks.com/techdocs/AOS-CX/help_portal/Content/home.htm

https://www.arubanetworks.com/techdocs/hardware/DocumentationPortal/Content/home.
htm

AOS-CX 10.11 Link Aggregation Guide | (All Switch Series)

94

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
SupportandOtherResources|95

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

AOS-CX 10.11 Link Aggregation Guide | (All Switch Series)

96