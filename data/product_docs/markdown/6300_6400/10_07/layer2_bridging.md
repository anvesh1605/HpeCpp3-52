| AOS-CX | 10.07 |     | Layer | 2 Bridging |
| ------ | ----- | --- | ----- | ---------- |
Guide
|     | 6300, | 6400 | Switch | Series |
| --- | ----- | ---- | ------ | ------ |
PartNumber:5200-7866
Published:April2021
Edition:1

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

Acknowledgment

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in the
United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

| 2

Contents
Contents
| Contents                            |                                               | 3   |
| ----------------------------------- | --------------------------------------------- | --- |
| About this                          | document                                      | 7   |
| Applicableproducts                  |                                               | 7   |
| Latestversionavailableonline        |                                               | 7   |
| Commandsyntaxnotationconventions    |                                               | 7   |
| Abouttheexamples                    |                                               | 8   |
| Identifyingswitchportsandinterfaces |                                               | 8   |
| Identifyingmodularswitchcomponents  |                                               | 9   |
| Introduction                        |                                               | 10  |
| MAC address                         | table                                         | 11  |
| MACaddresstablecommands             |                                               | 12  |
|                                     | clearmac-address                              | 12  |
|                                     | mac-address-tableage-time                     | 13  |
|                                     | mac-lockout                                   | 13  |
|                                     | showmac-address-table                         | 14  |
|                                     | showmac-address-tableaddress                  | 15  |
|                                     | showmac-address-tablecount                    | 16  |
|                                     | showmac-address-tabledynamic                  | 17  |
|                                     | showmac-address-tablelockout                  | 18  |
|                                     | showmac-address-tableport                     | 19  |
|                                     | showmac-address-tablestatic                   | 19  |
|                                     | showmac-address-tablevlan                     | 20  |
|                                     | static-mac                                    | 20  |
| VLANs                               |                                               | 22  |
| VLANinterfaces                      |                                               | 22  |
|                                     | Accessinterface                               | 22  |
|                                     | Trunkinterface                                | 23  |
|                                     | Traffichandlingsummary                        | 24  |
|                                     | ComparingVLANcommandsonPVOS,Comware,andAOS-CX | 25  |
| VLANnumbering                       |                                               | 26  |
| ConfiguringVLANs                    |                                               | 26  |
|                                     | CreatingandenablingaVLAN                      | 26  |
|                                     | DisablingaVLAN                                | 26  |
|                                     | AssigningaVLANtoaninterface                   | 27  |
|                                     | AssigningaVLANIDtoanaccessinterface           | 27  |
|                                     | AssigningaVLANIDtoatrunkinterface             | 27  |
|                                     | AssigninganativeVLANIDtoatrunkinterface       | 28  |
|                                     | ViewingVLANconfigurationinformation           | 29  |
| VLANscenario                        |                                               | 30  |
| VLANcommands                        |                                               | 34  |
|                                     | description                                   | 34  |
|                                     | name                                          | 35  |
|                                     | showcapacitiessvi-count                       | 35  |
|                                     | showvlan                                      | 36  |
|                                     | showvlanport                                  | 37  |
3
AOS-CX10.07Layer2BridgingGuide| for6300and6400Switches

|                                       | showvlansummary                         | 38  |
| ------------------------------------- | --------------------------------------- | --- |
|                                       | showvlantranslation                     | 38  |
|                                       | shutdown                                | 39  |
|                                       | systemvlan-client-presence-detect       | 40  |
|                                       | vlan                                    | 40  |
|                                       | vlanaccess                              | 41  |
|                                       | vlantranslate                           | 42  |
|                                       | vlantrunkallowed                        | 43  |
|                                       | vlantrunknative                         | 44  |
|                                       | vlantrunknativetag                      | 45  |
|                                       | voice                                   | 46  |
| Loop protection                       |                                         | 48  |
| Interactionwithotherprotocols         |                                         | 48  |
| Configuringloopprotection             |                                         | 49  |
| Loopprotectcommands                   |                                         | 50  |
|                                       | loop-protect                            | 50  |
|                                       | loop-protectaction                      | 51  |
|                                       | loop-protectre-enable-timer             | 51  |
|                                       | loop-protecttransmit-interval           | 52  |
|                                       | loop-protecttraploop-detected           | 53  |
|                                       | loop-protectvlan                        | 53  |
|                                       | showloop-protect                        | 54  |
| Spanning                              | tree protocols                          | 56  |
| Comparingspanningtreeoptions          |                                         | 56  |
| Preparingforspanningtreeconfiguration |                                         | 56  |
| STP                                   |                                         | 57  |
|                                       | STPprotocolpackets                      | 57  |
|                                       | STPkeyconcepts                          | 58  |
|                                       | Rootbridge                              | 58  |
|                                       | Rootport                                | 58  |
|                                       | Designatedbridgeanddesignatedport       | 58  |
|                                       | Pathcost                                | 59  |
|                                       | STPtimers                               | 59  |
|                                       | BPDUforwardingmechanism                 | 59  |
|                                       | STPcalculation                          | 60  |
|                                       | Simplifiedcalculationoverview           | 60  |
|                                       | Calculationexample                      | 61  |
| RPVST+                                |                                         | 65  |
|                                       | ConfiguringRPVST+                       | 67  |
|                                       | ViewingRPVST+information                | 70  |
|                                       | RPVST+scenario                          | 70  |
|                                       | RPVST+commands                          | 72  |
|                                       | showspanning-tree                       | 72  |
|                                       | showspanning-treeinconsistent-ports     | 74  |
|                                       | showspanning-treesummaryport            | 75  |
|                                       | showspanning-treesummaryroot            | 76  |
|                                       | showspanning-treevlan                   | 77  |
|                                       | spanning-treebpdu-guardtimeout          | 79  |
|                                       | spanning-treeextend-system-id           | 79  |
|                                       | spanning-treeignore-pvid-inconsistency  | 80  |
|                                       | spanning-treelink-type                  | 81  |
|                                       | spanning-treemode                       | 82  |
|                                       | spanning-treepathcost-type              | 83  |
|                                       | spanning-treerpvst-mstpinterconnectvlan | 83  |
Contents|4

spanning-tree tcn-guard
spanning-tree vlan
spanning-tree vlan cost
spanning-tree vlan port-priority
spanning-tree trap

MSTP

MSTP key concepts
Preparing for MSTP configuration
MSTP scenario
MSTP commands

show spanning-tree
show spanning-tree detail
show spanning-tree inconsistent-ports
show spanning-tree mst
show spanning-tree mst-config
show spanning-tree mst detail
show spanning-tree mst <INSTANCE-ID>
show spanning-tree mst <INSTANCE-ID> detail
show spanning-tree mst interface
show spanning-tree summary port
show spanning-tree summary root
spanning-tree
spanning-tree bdpu-filter
spanning-tree bpdu-guard
spanning-tree bpdu-guard timeout
spanning-tree config-name
spanning-tree config-revision
spanning-tree cost
spanning-tree forward-delay
spanning-tree hello-time
spanning-tree instance cost
spanning-tree instance port-priority
spanning-tree instance priority
spanning-tree instance vlan
spanning-tree link-type
spanning-tree loop-guard
spanning-tree max-age
spanning-tree max-hops
spanning-tree mode
spanning-tree port-priority
spanning-tree port-type
spanning-tree priority
spanning-tree root-guard
spanning-tree rpvst-filter
spanning-tree rpvst-guard
spanning-tree rpvst-mstp interconnect vlan
spanning-tree tcn-guard
spanning-tree transmit-hold-count
spanning-tree trap

MVRP

MVRP functionality and limitations
MRP messages

Join message
New message
Leave message

84
85
86
86
87
89
89
93
94
98
98
99
101
102
104
104
107
108
110
110
111
112
112
113
114
115
116
116
117
118
118
119
120
121
121
122
123
124
125
125
126
127
128
128
129
130
130
131
132

134
134
135
135
135
135

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

5

|                       | LeaveAllmessage     |           | 136 |
| --------------------- | ------------------- | --------- | --- |
| ConfiguringMVRP       |                     |           | 136 |
| MVRPscenario1         |                     |           | 137 |
| MVRPscenario2         |                     |           | 141 |
| MVRPcommands          |                     |           | 148 |
|                       | clearmvrpstatistics |           | 148 |
|                       | mvrp                |           | 149 |
|                       | mvrpregistration    |           | 149 |
|                       | mvrptimer           |           | 150 |
|                       | showmvrpconfig      |           | 151 |
|                       | showmvrpstate       |           | 152 |
|                       | showmvrpstatistics  |           | 153 |
| UDLD                  |                     |           | 155 |
| ConfiguringUDLD       |                     |           | 156 |
| UDLDscenario          |                     |           | 157 |
| UDLDcommands          |                     |           | 158 |
|                       | clearudldstatistics |           | 158 |
|                       | showudld            |           | 159 |
|                       | udld                |           | 161 |
|                       | udldinterval        |           | 161 |
|                       | udldmode            |           | 163 |
|                       | udldretries         |           | 165 |
| Support               | and other           | resources | 166 |
| AccessingArubaSupport |                     |           | 166 |
| Accessingupdates      |                     |           | 166 |
|                       | ArubaSupportPortal  |           | 166 |
|                       | MyNetworking        |           | 167 |
| Warrantyinformation   |                     |           | 167 |
| Regulatoryinformation |                     |           | 167 |
| Documentationfeedback |                     |           | 167 |
Contents|6

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for administrators
responsible for installing, configuring, and managing Aruba switches on a network.

Applicable products
This document applies to the following products:

n Aruba 6300 Switch Series (JL658A, JL659A, JL660A, JL661A, JL662A, JL663A, JL664A, JL665A, JL666A,

JL667A, JL668A, JL762A)

n Aruba 6400 Switch Series (JL741A, R0X26A, R0X27A, R0X29A, R0X30A)

Latest version available online
Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and other resources.

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

|

{ }

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

7

| Convention |     | Usage                                                    |     |
| ---------- | --- | -------------------------------------------------------- | --- |
| [ ]        |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| …or        |     | Ellipsis:                                                |     |
... n Incodeandscreenexamples,averticalorhorizontalellipsisindicatesan
omissionofinformation.
n Insyntaxusingbracketsandbraces,anellipsisindicatesitemsthatcanbe
repeated.Whenanitemfollowedbyellipsesisenclosedinbrackets,zero
ormoreitemscanbespecified.
| About the | examples |     |     |
| --------- | -------- | --- | --- |
Examplesinthisdocumentarerepresentativeandmightnotmatchyourparticularswitchorenvironment.
Theslotandportnumbersinthisdocumentareforillustrationonlyandmightbeunavailableonyour
switch.
| Understandingthe | CLI prompts |     |     |
| ---------------- | ----------- | --- | --- |
Whenillustratingthepromptsinthecommandlineinterface(CLI),thisdocumentusesthegenericterm
switch,insteadofthehostnameoftheswitch.Forexample:
switch>
TheCLIpromptindicatesthecurrentcommandcontext.Forexample:
switch>
Indicatestheoperatorcommandcontext.
switch#
Indicatesthemanagercommandcontext.
switch(CONTEXT-NAME)#
Indicatestheconfigurationcontextforafeature.Forexample:
switch(config-if)#
Identifiestheinterfacecontext.
| Variable information | in  | CLI prompts |     |
| -------------------- | --- | ----------- | --- |
Incertainconfigurationcontexts,thepromptmayincludevariableinformation.Forexample,wheninthe
VLANconfigurationcontext,aVLANnumberappearsintheprompt:
switch(config-vlan-100)#
Whenreferringtothiscontext,thisdocumentusesthesyntax:
switch(config-vlan-<VLAN-ID>)#
Where<VLAN-ID>isavariablerepresentingtheVLANnumber.
| Identifying | switch | ports and | interfaces |
| ----------- | ------ | --------- | ---------- |
Physicalportsontheswitchandtheircorrespondinglogicalsoftwareinterfacesareidentifiedusingthe
format:
member/slot/port
| On the 6300Switch | Series |     |     |
| ----------------- | ------ | --- | --- |
n member:MembernumberoftheswitchinaVirtualSwitchingFramework(VSF)stack.Range:1to10.
Theprimaryswitchisalwaysmember1.IftheswitchisnotamemberofaVSFstack,thenmemberis1.
Aboutthisdocument|8

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

9

Chapter 2

Introduction

Introduction

Switches use network bridging to facilitate the interconnection of local area networks (LANs) so that traffic
can be exchanged between devices. Bridging occurs at layer 2 of the OSI model.

When creating network bridges on HPE switches, network administrators can configure MAC addressing,
VLANs, and various loop prevention protocols.

Devices on a network are identified by their MAC address. The switch maintains a MAC address table where it
stores information about the other Ethernet interfaces to which a switch is connected. The table enables the
switch to send outgoing data (Ethernet frames) on the specific port required to reach its destination, instead
of broadcasting the data on all ports (flooding).

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

n MSTP: Multiple-Instance spanning tree protocol (MSTP) ensures that only one active path exists between
any two nodes in a spanning tree instance. A spanning tree instance comprises a unique set of VLANs,
and belongs to a specific spanning tree region. A region can comprise multiple spanning tree instances
(each with a different set of VLANs), and allows one active path among regions in a network.

n RPVST+: Rapid Per VLAN Spanning Tree+ (RPVST+) is an updated implementation of STP (Spanning Tree

Protocol). It enables the creation of a separate spanning tree for each VLAN on a switch, and ensures that
only one active, loop-free path exists between any two nodes on a given VLAN.

n Loop Protection: In cases where spanning tree protocols cannot be used to prevent loops at the edge of

the network, loop protection may provide a suitable alternative. Loop protection can find loops in
untagged layer 2 links, as well as on tagged VLANs.

AOS-CX also supports the MVRP (Multiple VLAN Registration Protocol), a registration protocol defined by
IEEE, which propagates VLAN information dynamically across devices. It also enables devices to learn and
automatically synchronize VLAN configuration information, reducing the configuration workload.

Additionally, AOS-CX supports the Unidirectional Link Detection (UDLD) protocol. UDLD monitors the link
between two network devices, and if the link fails, blocks the ports on both ends of the link. UDLD is useful
for detecting failures in fiber links and trunks.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

10

Chapter 3

MAC address table

MAC address table

The MAC address table is where the switch stores information about the other Ethernet interfaces to which it
is connected on a network. The table enables the switch to send outgoing data (Ethernet frames) on the
specific port required to reach its destination, instead of broadcasting the data on all ports (flooding).

The MAC address table can contain two types of entries:

n Static: Static entries are manually added to the table by a switch administrator. Static entries have higher

priority than dynamic entries. Static entries remain active until they are removed by the switch
administrator.

n Dynamic: Dynamic entries are automatically added to the table through a process called MAC learning, in

which the switch retrieves the source MAC address (and VLAN ID, if present) of each Ethernet frame
received on a port. If the retrieved address does not exist in the table, it is added. Dynamic entries remain
in the table for a predetermined amount of time (defined with the command mac-address-table age-
time), after which they are automatically deleted.

Dynamic MAC address learning does not distinguish between illegitimate and legitimate frames, which can
invite security hazards. When Host A is connected to port A, a MAC address entry will be learned for the MAC
address of Host A (for example, MAC A). When an illegal user sends frames with MAC A as the source MAC
address to port B, the device performs the following operations:

1. Learns a new MAC address entry with port B as the outgoing interface and overwrites the old entry

for MAC A.

2. Forwards frames destined for MAC A out of port B to the illegal user.

As a result, the illegal user obtains the data of Host A. To improve the security for Host A, manually configure
a static entry to bind Host A to port A. Then, the frames destined for Host A are always sent out of port A.
Other hosts using the forged MAC address of Host A cannot obtain the frames destined for Host A.

For example, in the following topology, switch A learns the MAC addresses of ports on switch B, C, and D.
This way, traffic between any two switches is not broadcast to the other switches. For example, if server 1
sends traffic to server 3, it does not get broadcast onto the link to switch C, only on the link to switch D.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

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

On the 6400 Switch Series, interface identification differs.

Clearing the learned MAC addresses on a port:

switch# clear mac-address port 1/1/1

MAC address table | 12

ClearingthelearnedMACaddressesonacombinationofaVLANandaport:
| switch# clear     | mac-address | port 1/1/1  | vlan 20 |
| ----------------- | ----------- | ----------- | ------- |
| switch# clear     | mac-address | vlan 2 port | 1/1/3   |
| mac-address-table | age-time    |             |         |
Syntax
| mac-address-table    | age-time | <SECONDS>   |     |
| -------------------- | -------- | ----------- | --- |
| no mac-address-table | age-time | [<SECONDS>] |     |
Description
SetsthemaximumamountoftimeaMACaddressremainsintheMACaddresstable.Whenthistime
expires,theMACaddressisremoved.
ThenoformofthiscommandresetstheMACagingtimertothedefaultvalue(300seconds).
Commandcontext
config
Parameters
age-time <SECONDS>
SpecifiestheMACaddressagingtimeinseconds.Range:60to3600.Default:300.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
switch(config)#
|     | mac-address-table |     | age-time 120 |
| --- | ----------------- | --- | ------------ |
mac-lockout
Syntax
| mac-lockout <MAC-ADDR> |            |     |     |
| ---------------------- | ---------- | --- | --- |
| no mac-lockout         | <MAC-ADDR> |     |     |
Description
LocksaMACaddressgloballyontheswitchandallVLANS.Theswitchdropsalldatapacketsaddressedtoor
fromthegivenaddress.
ThenoformofthiscommandunlockstheMACaddressgloballyontheswitchandallVLANs.
Commandcontext
config
Parameters
<MAC-ADDR>
SpecifiestheMACaddress.
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 13

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

On the 6400 Switch Series, interface identification differs.

Showing output when table entries exist:

MAC address table | 14

| switch#      | show mac-address-table |       |         |      |
| ------------ | ---------------------- | ----- | ------- | ---- |
| MAC age-time |                        | : 300 | seconds |      |
| Number       | of MAC addresses       | : 5   |         |      |
| MAC Address  |                        | VLAN  | Type    | Port |
--------------------------------------------------
| 00:00:00:00:00:05 |     | 1   | dynamic | 1/1/2            |
| ----------------- | --- | --- | ------- | ---------------- |
| 00:00:00:00:00:06 |     | 2   | dynamic | 1/1/1            |
| 00:00:00:00:00:08 |     | 3   | hsc     | vxlan1(10.1.1.1) |
| 00:00:00:00:00:12 |     | 3   | hsc     | vxlan1(10.1.1.3) |
| 00:00:00:00:00:34 |     | 3   | hsc     | vxlan1(10.1.1.4) |
ShowingoutputwhentherearenoMACtableentries:
| switch# | show mac-address-table |     |     |     |
| ------- | ---------------------- | --- | --- | --- |
| No MAC  | entries found.         |     |     |     |
ShowingonlyMACaddressdiscoveredbytheHSCmanager:
| switch#     | show mac-address-table |      | hsc  |      |
| ----------- | ---------------------- | ---- | ---- | ---- |
| Number      | of MAC addresses       | : 3  |      |      |
| MAC Address |                        | VLAN | Type | Port |
---------------------------------------------------------
| 00:00:00:00:00:08      |     | 3   | hsc     | vxlan1(10.1.1.1) |
| ---------------------- | --- | --- | ------- | ---------------- |
| 00:00:00:00:00:12      |     | 3   | hsc     | vxlan1(10.1.1.3) |
| 00:00:00:00:00:34      |     | 3   | hsc     | vxlan1(10.1.1.4) |
| show mac-address-table |     |     | address |                  |
Syntax
| show mac-address-table |     | address | <MAC-ADDR> | [vsx-peer] |
| ---------------------- | --- | ------- | ---------- | ---------- |
Description
ShowsMACaddresstableinformationforaspecificMACaddress.
Commandcontext
Operator(>)orManager(#)
Parameters
<MAC-ADDR>
SpecifiestheMACaddress.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 15

Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch#      | show mac-address-table |       | address | 00:00:00:00:00:01 |
| ------------ | ---------------------- | ----- | ------- | ----------------- |
| MAC age-time |                        | : 300 | seconds |                   |
| Number       | of MAC addresses       | : 2   |         |                   |
| MAC Address  |                        | VLAN  | Type    | Port              |
--------------------------------------------------
| 00:00:00:00:00:01      |     | 2   | dynamic | 1/1/1 |
| ---------------------- | --- | --- | ------- | ----- |
| 00:00:00:00:00:01      |     | 1   | dynamic | 1/1/1 |
| show mac-address-table |     |     | count   |       |
Syntax
| show mac-address-table |        | count      |                   |            |
| ---------------------- | ------ | ---------- | ----------------- | ---------- |
| [dynamic               | | port | <PORT-NUM> | | vlan <VLAN-ID>] | [vsx-peer] |
Description
DisplaysthenumberofMACaddresses.
Commandcontext
Operator(>)orManager(#)
Parameters
dynamic
ShowthecountofdynamicallylearnedMACaddresses.
<PORT-NUM>
Specifiesaphysicalportontheswitch.Format:member/slot/port.
vlan <VLAN-ID>
SpecifiesthenumberofaVLAN.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
ShowingthenumberofMACaddresses:
| switch# | show mac-address-table |     | count |     |
| ------- | ---------------------- | --- | ----- | --- |
| Number  | of MAC addresses       | : 8 |       |     |
ShowingthenumberofdynamicallylearnedMACaddresses:
| switch# | show mac-address-table |     | count dynamic |     |
| ------- | ---------------------- | --- | ------------- | --- |
| Number  | of MAC addresses       | : 8 |               |     |
ShowingthenumberofMACaddressesperphysicalportontheswitch:
MACaddresstable|16

| switch# | show mac-address-table | count | port 1/1/1 |
| ------- | ---------------------- | ----- | ---------- |
| Number  | of MAC addresses       | : 2   |            |
ShowingthenumberofMACaddressesperVLAN:
| switch# | show mac-address-table | count | vlan 100 |
| ------- | ---------------------- | ----- | -------- |
| Number  | of MAC addresses       | : 5   |          |
ShowingthenumberofMACaddressesontheVSXprimaryandsecondary(peer)switch:
| vsx-primary#           | show mac-address-table |         | count          |
| ---------------------- | ---------------------- | ------- | -------------- |
| Number                 | of MAC addresses       | : 26114 |                |
| vsx-primary#           | show mac-address-table |         | count vsx-peer |
| Number                 | of MAC addresses       | : 26113 |                |
| show mac-address-table |                        | dynamic |                |
Syntax
show mac-address-table dynamic [port <PORT-NUM> | vlan <VLAN-ID>] [vsx-peer]
Description
ShowsMACaddresstableinformationaboutdynamicallylearnedMACaddresses.
Commandcontext
Operator(>)orManager(#)
Parameters
<PORT-NUM>
Specifiesaphysicalportontheswitch.Format:member/slot/port.
<VLAN-ID>
SpecifiesthenumberofaVLAN.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingalldynamicMACaddresstableentries:
| switch#      | show mac-address-table | dynamic       |     |
| ------------ | ---------------------- | ------------- | --- |
| MAC age-time |                        | : 300 seconds |     |
| Number       | of MAC addresses       | : 2           |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 17

| MAC Address |     | VLAN | Type | Port |
| ----------- | --- | ---- | ---- | ---- |
--------------------------------------------------
| 00:00:00:00:00:05 |     | 1   | dynamic | 1/1/2 |
| ----------------- | --- | --- | ------- | ----- |
| 00:00:00:00:00:06 |     | 2   | dynamic | 1/1/1 |
ShowingdynamicMACaddresstableentriesforVLAN1:
| switch#      | show mac-address-table |       | dynamic | vlan 1 |
| ------------ | ---------------------- | ----- | ------- | ------ |
| MAC age-time |                        | : 300 | seconds |        |
| Number       | of MAC addresses       | : 1   |         |        |
| MAC Address  |                        | VLAN  | Type    | Port   |
--------------------------------------------------
| 00:00:00:00:00:05 |     | 1   | dynamic | 1/1/2 |
| ----------------- | --- | --- | ------- | ----- |
ShowingdynamicMACaddresstableentriesforport1/1/1:
| switch#      | show mac-address-table |       | dynamic | port 1/1/1 |
| ------------ | ---------------------- | ----- | ------- | ---------- |
| MAC age-time |                        | : 300 | seconds |            |
| Number       | of MAC addresses       | : 1   |         |            |
| MAC Address  |                        | VLAN  | Type    | Port       |
--------------------------------------------------
| 00:00:00:00:00:06      |     | 2   | dynamic | 1/1/1 |
| ---------------------- | --- | --- | ------- | ----- |
| show mac-address-table |     |     | lockout |       |
Syntax
| show mac-address-table |     | lockout | [vsx-peer] |     |
| ---------------------- | --- | ------- | ---------- | --- |
Description
ShowsMAClockouttableinformation.
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
| switch# | show mac-address-table |           | lockout |     |
| ------- | ---------------------- | --------- | ------- | --- |
| Number  | of MAC lockout         | addresses | :       |     |
MACaddresstable|18

| 2MAC Address |     | Type |     |     |
| ------------ | --- | ---- | --- | --- |
------------------------------------------
| 00:00:00:00:01:10      |     | static |      |     |
| ---------------------- | --- | ------ | ---- | --- |
| 00:00:00:00:10:03      |     | static |      |     |
| show mac-address-table |     |        | port |     |
Syntax
| show mac-address-table |     | port <PORT-NUM> | [vsx-peer] |     |
| ---------------------- | --- | --------------- | ---------- | --- |
Description
ShowstheMACaddresstableentriesforthespecifiedport.
Commandcontext
Operator(>)orManager(#)
Parameters
<PORT-NUM>
Specifiesaphysicalportontheswitch.Format:member/slot/port.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingtheMACaddresstableentriesforport1/1/1:
| switch#      | show mac-address-table |       | port 1/1/1 |      |
| ------------ | ---------------------- | ----- | ---------- | ---- |
| MAC age-time |                        | : 300 | seconds    |      |
| Number       | of MAC addresses       | : 1   |            |      |
| MAC Address  |                        | VLAN  | Type       | Port |
--------------------------------------------------
| 00:00:00:00:00:01      |     | 2   | dynamic | 1/1/1 |
| ---------------------- | --- | --- | ------- | ----- |
| show mac-address-table |     |     | static  |       |
Syntax
| show mac-address-table |     | static |     |     |
| ---------------------- | --- | ------ | --- | --- |
Description
ShowsallstaticallyconfiguredMACaddresses.
Commandcontext
Operator(>)orManager(#)
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 19

Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch#     | show mac-address-table |      | static |     |
| ----------- | ---------------------- | ---- | ------ | --- |
| Number      | of MAC addresses       | : 2  |        |     |
| MAC Address |                        | VLAN | Port   |     |
--------------------------------------
| 00:00:00:00:10:02      |     | 1   | 1/1/1 |     |
| ---------------------- | --- | --- | ----- | --- |
| 00:00:00:00:10:03      |     | 1   | 1/1/1 |     |
| show mac-address-table |     |     | vlan  |     |
Syntax
| show mac-address-table |     | vlan <VLAN-ID> | [vsx-peer] |     |
| ---------------------- | --- | -------------- | ---------- | --- |
Description
ShowsMACaddresseslearnedbyorconfiguredonthespecifiedVLAN.
Commandcontext
Operator(>)orManager(#)
Parameters
vlan <VLAN-ID>
SpecifiestheVLANID.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch#      | show mac-address-table |       | vlan 1  |      |
| ------------ | ---------------------- | ----- | ------- | ---- |
| MAC age-time |                        | : 300 | seconds |      |
| Number       | of MAC addresses       | : 1   |         |      |
| MAC Address  |                        | VLAN  | Type    | Port |
--------------------------------------------------
| 00:00:00:00:00:01 |     | 1   | dynamic | 1/1/1 |
| ----------------- | --- | --- | ------- | ----- |
static-mac
MACaddresstable|20

Syntax
| static-mac    | <MAC-ADDR> | vlan | <VLAN-ID> | port <PORT-NUM> |            |     |
| ------------- | ---------- | ---- | --------- | --------------- | ---------- | --- |
| no static-mac | <MAC-ADDR> | vlan | <VLAN-ID> | port            | <PORT-NUM> |     |
Description
AddsastaticMACaddresstotheMACaddresstableandassociatesitwithaportorexistingVLAN.Static
MACaddressescanonlybeassignedtolayer2(non-routed)interfaces.StaticMACaddressesarenot
affectedbytheMACaddressagingtime.
ThenoformofthiscommanddeletesastaticMACaddress.
Commandcontext
config
Parameters
<MAC-ADDR>
SpecifiesaMACaddress(xx:xx:xx:xx:xx:xx),wherexisahexadecimalnumberfrom0toF.
vlan <VLAN-ID>
SpecifiesnumberofanexistingVLAN.
port <PORT-NUM>
Specifiesaphysicalportontheswitch.Format:member/slot/port.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch(config)# |     | static-mac | 00:00:00:00:00:01 |     | vlan 1 port | 1/1/1 |
| --------------- | --- | ---------- | ----------------- | --- | ----------- | ----- |
switch(config)# no static-mac 00:00:00:00:00:01 vlan 1 port 1/1/1
| switch(config)# |             | static-mac | 00:00:00:00:00:01 |     | vlan 1 port | 1/1/2 |
| --------------- | ----------- | ---------- | ----------------- | --- | ----------- | ----- |
| 1/1/2           | is not      | an L2 port |                   |     |             |       |
| switch(config)# |             | static-mac | 00:00:00:00:00:01 |     | vlan 2 port | 1/1/1 |
| VLAN            | 2 not found |            |                   |     |             |       |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 21

Chapter 4

VLANs

VLANs

VLANs are primarily used to provide network segmentation at layer 2. VLANs enable the grouping of users
by logical function instead of physical location. They make managing bandwidth usage within networks
possible by:

n Allowing grouping of high-bandwidth users on low-traffic segments

n Organizing users from different LAN segments according to their need for common resources and

individual protocols

n Improving traffic control at the edge of networks by separating traffic of different protocol types.

n Enhancing network security by creating subnets to control in-band access to specific network resources

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

On the 6400 Switch Series, interface identification differs.

This example shows ingress and egress traffic behavior for an access interface.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

22

n An ingress tagged frame with VLAN ID of 100 arrives on interface 1/2/32. The switch accepts this frame

and sends it to its target address on interface 1/1/32, where it egresses untagged.

n An ingress untagged frame arrives on interface 1/2/32. The switch accepts this frame and sends it to its

target address on interface 1/1/32, where it egresses untagged.

n An ingress tagged frame with VLAN ID of 50 arrives on interface 1/2/32. The switch drops this frame as

VLAN ID 50 is not configured on the interface.

Trunk interface

A trunk interface can carry traffic for one or more VLAN IDs. In most cases, a trunk interface is used to
transport data to other switches or routers.

A trunk interface has two important settings:

n Native VLAN: This is the VLAN to which incoming untagged traffic is assigned. Only one VLAN can be

assigned as the native VLAN. By default, VLAN 1 is assigned as the native VLAN for all trunk interfaces.

n Allowed VLANs: This is the list of VLANs that can be transported by the trunk. If the native VLAN is not

included in the allowed list, all untagged frames that ingress on the trunk interface are dropped.

Example 1: Native untagged VLAN

On the 6400 Switch Series, interface identification differs.

This example shows ingress and egress traffic behavior when a trunk interface has a native untagged VLAN.

n An ingress tagged frame with VLAN ID of 25 arrives on interface 1/1/1. The switch accepts this frame and
sends it to its target address on interface 1/1/2, where it egresses with a VLAN ID of 25 untagged since
port 1/1/2 is configured with a native VLAN ID of 25.

n An ingress untagged frame arrives on interface 1/1/1. The switch accepts this frame and sends it to its
target address on interface 1/1/2, where it egresses with a VLAN ID of 25 untagged since port 1/1/2 is
configured with a native VLAN ID of 25.

n An ingress tagged frame with VLAN ID of 4 arrives on interface 1/1/1. The switch accepts this frame and
sends it to its target address on interface 1/1/2, where it egresses with a VLAN ID of 4 tagged since port
1/1/2 is configured to allow traffic with a VLAN ID of 4.

n An ingress tagged frame with VLAN ID of 50 arrives on interface 1/1/1. The switch drops this frame as

VLAN ID 50 is not in the allowed list for interface 1/1/1.

Example 2: Native tagged VLAN

On the 6400 Switch Series, interface identification differs.

This example shows ingress and egress traffic behavior when a trunk interface has a native tagged VLAN.

VLANs | 23

n AningresstaggedframewithVLANIDof6arrivesoninterface1/1/13.Theswitchacceptsthisframeand
sendsittoitstargetaddressoninterface1/1/21,whereitegresseswithaVLANIDof6taggedsinceport
1/1/2isconfiguredwithanativeVLANIDof6.
Aningressuntaggedframearrivesoninterface1/1/13.Theswitchdropsthisframesincetheinterfaceis
n
configuredasnativetagged(alluntaggedframesadroppedinsuchaconfiguration).
n AningresstaggedframewithVLANIDof17arrivesoninterface1/1/13.Theswitchacceptsthisframe
andsendsittoitstargetaddressoninterface1/1/21,whereitegresseswithaVLANIDof17taggedsince
port1/1/2isconfiguredtoallowtrafficwithaVLANIDof17.
n AningresstaggedframewithVLANIDof50arrivesoninterface1/1/13.Theswitchdropsthisframeas
VLANID50isnotintheallowedlistforinterface1/1/13.
| Traffic handling summary |                 |                |
| ------------------------ | --------------- | -------------- |
| VLAN configuration       | Ingress traffic | Egress traffic |
Accessinterfacewith:
|     | 1. Untagged | 1. UntaggedonVLANX |
| --- | ----------- | ------------------ |
VLANID=X
|     | 2. TaggedwithVLANID=X       | 2. UntaggedonVLANX |
| --- | --------------------------- | ------------------ |
|     | 3. TaggedwithanyotherVLANID | 3. Dropped         |
Trunkinterfacewith:
|     | 1. Untagged | 1. UntaggedonVLANX |
| --- | ----------- | ------------------ |
n UntaggedNativeVLANID=
|     | 2. TaggedwithVLANID=X | 2. UntaggedonVLANX |
| --- | --------------------- | ------------------ |
X
|     | 3. TaggedwithVLANID=Y | 3. TaggedonVLANY |
| --- | --------------------- | ---------------- |
n AllowedVLANIDs=X,Y,Z
|     | 4. TaggedwithVLANID=Z       | 4. TaggedonVLANZ |
| --- | --------------------------- | ---------------- |
|     | 5. TaggedwithanyotherVLANID | 5. Dropped       |
Trunkinterfacewith:
|     | 1. Untagged | 1. UntaggedonVLANX |
| --- | ----------- | ------------------ |
n UntaggedNativeVLANID=
|     | 2. TaggedwithVLANID=X | 2. UntaggedonVLANX |
| --- | --------------------- | ------------------ |
X
|     | 3. TaggedwithaVLANIDdefined | 3. TaggedonthematchingVLAN |
| --- | --------------------------- | -------------------------- |
AllowedVLANIDs=ALL
n
|     | ontheswitch | 4. Dropped |
| --- | ----------- | ---------- |
4. TaggedwithaVLANIDnot
definedontheswitch
Trunkinterfacewith:
|     | 1. Untagged | 1. Dropped |
| --- | ----------- | ---------- |
TaggedNativeVLANID=X
n
|     | 2. TaggedwithVLANID=X | 2. TaggedonVLANX |
| --- | --------------------- | ---------------- |
n AllowedVLANIDs=X,Y,Z
|     | 3. TaggedwithVLANID=Y | 3. TaggedonVLANY |
| --- | --------------------- | ---------------- |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 24

| VLAN configuration |     | Ingress | traffic                  |     |     |     | Egress           | traffic |     |
| ------------------ | --- | ------- | ------------------------ | --- | --- | --- | ---------------- | ------- | --- |
|                    |     | 4.      | TaggedwithVLANID=Z       |     |     |     | 4. TaggedonVLANZ |         |     |
|                    |     | 5.      | TaggedwithanyotherVLANID |     |     |     | 5. Dropped       |         |     |
Trunkinterfacewith:
|     |     | 1.  | Untagged |     |     |     | 1. Dropped |     |     |
| --- | --- | --- | -------- | --- | --- | --- | ---------- | --- | --- |
n TaggedNativeVLANID=X
|     |     | 2.  | TaggedwithVLANID=X |     |     |     | 2. TaggedonVLANX |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | ---------------- | --- | --- |
n AllowedVLANIDs=ALL
|     |     | 3.  | TaggedwithaVLANIDdefined |     |     |     | 3. TaggedonthematchingVLAN |     |     |
| --- | --- | --- | ------------------------ | --- | --- | --- | -------------------------- | --- | --- |
ontheswitch
4. Dropped
4. TaggedwithaVLANIDnot
definedontheswitch
Trunkinterfacewith:
|     |     | 1.  | Untagged |     |     |     | 1. Dropped |     |     |
| --- | --- | --- | -------- | --- | --- | --- | ---------- | --- | --- |
n UntaggedNativeVLANID=
|     |     | 2.  | TaggedwithVLANID=X |     |     |     | 2. TaggedonVLANX |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | ---------------- | --- | --- |
A
|     |     | 3.  | TaggedwithVLANID=Y |     |     |     | 3. TaggedonVLANY |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | ---------------- | --- | --- |
n AllowedVLANIDs=X,Y,Z
|           |               | 4.  | TaggedwithVLANID=Z       |          |          |     | 4. TaggedonVLANZ |        |     |
| --------- | ------------- | --- | ------------------------ | -------- | -------- | --- | ---------------- | ------ | --- |
|           |               | 5.  | TaggedwithanyotherVLANID |          |          |     | 5. Dropped       |        |     |
| Comparing | VLAN commands |     |                          | on PVOS, | Comware, |     | and              | AOS-CX |     |
ThefollowingexamplescomparethecommandsneededtoimplementtypicalVLANconfigurationson
differentHPEproducts.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| AOS-CX    |       |     | PVOS      |     |     | Comware   |     |        |     |
| --------- | ----- | --- | --------- | --- | --- | --------- | --- | ------ | --- |
| interface | 1/1/1 |     | interface | A1  |     | Interface |     | G1/0/1 |     |
vlan trunk native 1 tagged vlan 10,30,50 port link type trunk
vlan trunk allowed 10,30,50 no untagged vlan 1 port trunk permit vlan 10,30,50
| AnativeVLANmustbedefinedon     |     |     |     |     |     | port                      | trunk | pvid vlan | 1   |
| ------------------------------ | --- | --- | --- | --- | --- | ------------------------- | ----- | --------- | --- |
| theswitch.Bydefault,thisisVLAN |     |     |     |     |     | PVID1isthedefaultsetting. |       |           |     |
1.SinceonlyVLANs10,30,and50
areallowedonthetrunk,all
untaggedtrafficisdropped.
| AOS-CX |     |     | PVOS |     |     |     | Comware |     |     |
| ------ | --- | --- | ---- | --- | --- | --- | ------- | --- | --- |
interface 1/1/1 Notdirectlysupportedin NotdirectlysupportedinComware.A
vlan trunk native 10 tag PVOS.Scenario1isa possibleworkaroundis:
vlan trunk allowed 10,30,50 workaroundifthereisno interface g1/0/1
Sameasscenario1,butallows needtosupportuntagged port link-mode bridge
untaggedtrafficonVLAN10aswell. traffic. port link-type hybrid
|            |          |     |           |      |     |     | port      | hybrid protocol-vlan |           |
| ---------- | -------- | --- | --------- | ---- | --- | --- | --------- | -------------------- | --------- |
|            |          |     |           |      |     |     | vlan 10   |                      |           |
|            |          |     |           |      |     |     | port      | hybrid vlan          | 10 tagged |
|            |          |     |           |      |     |     | port      | hybrid vlan          | 30 tagged |
|            |          |     |           |      |     |     | port      | hybrid vlan          | 50 tagged |
| AOS-CX     |          |     | PVOS      |      |     |     | Comware   |                      |           |
| interface  | 1/1/1    |     | interface | A1   |     |     | interface | G1/0/1               |           |
| vlan trunk | native 5 |     | untagged  | vlan | 5   |     | Port      | link-mode            | bridge    |
vlan trunk allowed 5, 10,30,50 no tagged vlan 10,30,50 port link-type trunk
VLANs|25

|     |     |     |     |     | port trunk | pvid vlan | 5   |
| --- | --- | --- | --- | --- | ---------- | --------- | --- |
VLAN5mustbeallowedonthetrunkso
| thatuntaggedtrafficisnotdropped. |     |     |     |     | port trunk | permit | vlan |
| -------------------------------- | --- | --- | --- | --- | ---------- | ------ | ---- |
5,10,30,50
link-modeisonlyneededon
laterComware7devices.5930is
portlink-moderoutebydefault.
5900isbridgebydefault.
| ArubaOS-CX  |           |     | PVOS          |     | Comware   |                  |     |
| ----------- | --------- | --- | ------------- | --- | --------- | ---------------- | --- |
| interface   | 1/1/1     |     | interface A1  |     | interface | G1/0/0           |     |
| vlan access | 5         |     | untagged vlan | 5   | port      | link-mode bridge |     |
|             |           |     |               |     | port      | access vlan      | 5   |
| VLAN        | numbering |     |               |     |           |                  |     |
VLANsarenumberedintherange1to4094.
Bydefault,VLAN1(thedefaultVLAN)isassociatedwithallinterfacesontheswitch.VLAN1cannotbe
removedfromtheswitch.
| Configuring | VLANs        |        |     |     |     |     |     |
| ----------- | ------------ | ------ | --- | --- | --- | --- | --- |
| Creating    | and enabling | a VLAN |     |     |     |     |     |
Procedure
1. Switchtotheconfigurationcontextwiththecommandconfig.
2. CreateanewVLANwiththecommandvlan.
Example
| ThisexamplecreatesVLAN | 10.TheVLANisenabledbydefault. |     |     |     |     |     |     |
| ---------------------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
| switch#                | config                        |     |     |     |     |     |     |
| switch(config)#        | vlan 10                       |     |     |     |     |     |     |
switch(config-vlan-10)#
| Disabling | a VLAN |     |     |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- | --- | --- |
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. SwitchtoconfigurationcontextfortheVLANyouwanttodisablewiththecommandvlan.
3. DisabletheVLANwiththecommandshutdown.
Example
| ThisexampledisablesVLAN                               | 10. |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches |     |     |     |     |     |     | 26  |

| switch(config)# |     | config |     |     |
| --------------- | --- | ------ | --- | --- |
switch(config)#
|                         |     | vlan | 10       |           |
| ----------------------- | --- | ---- | -------- | --------- |
| switch(config-vlan-10)# |     |      | shutdown |           |
| Assigning               | a   | VLAN | to an    | interface |
TouseaVLAN,itmustbeassignedtoaninterfaceontheswitch.VLANscanonlybeassignedtonon-routed
(layer2)interfaces.Allinterfacesarerouted(layer3)bydefaultwhencreated.Usetheno routing
commandtodisableroutingonaninterface.
| Assigninga | VLAN | ID toan | accessinterface |     |
| ---------- | ---- | ------- | --------------- | --- |
Prerequisites
AtleastonedefinedVLAN.
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtotheinterfacethatyouwanttodefineasanaccessinterfacewiththecommandinterface.
3. ConfiguretheaccessinterfaceandassignaVLANIDwiththecommandvlan access.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexampleconfiguresinterface1/1/2asanaccessinterfacewithVLANIDsetto20.
| switch#                 | config |           |             |     |
| ----------------------- | ------ | --------- | ----------- | --- |
| switch(config)#         |        | vlan      | 20          |     |
| switch(config-vlan-20)# |        |           | exit        |     |
| switch(config)#         |        | interface | 1/1/2       |     |
| switch(config-if)#      |        |           | vlan access | 20  |
ThisexampleconfiguresLAG1asanaccessinterfacewithVLANIDsetto30.
| switch#                 | config |           |                |           |
| ----------------------- | ------ | --------- | -------------- | --------- |
| switch(config)#         |        | vlan      | 30             |           |
| switch(config-vlan-30)# |        |           | exit           |           |
| switch(config)#         |        | interface | lag            | 1         |
| switch(config-lag-if)#  |        |           | no shutdown    |           |
| switch(config-lag-if)#  |        |           | vlan           | access 30 |
| Assigninga              | VLAN   | ID toa    | trunkinterface |           |
Prerequisites
AtleastonedefinedVLAN.
Procedure
VLANs|27

1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtotheinterfacethatyouwanttodefineasatrunkinterfacewiththecommandinterface.
3. ConfigurethetrunkinterfaceandassignaVLANIDwiththecommandvlan allowed.
trunk
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDsetto20.
| switch#                 | config |           |            |            |
| ----------------------- | ------ | --------- | ---------- | ---------- |
| switch(config)#         |        | vlan      | 20         |            |
| switch(config-vlan-20)# |        |           | exit       |            |
| switch(config)#         |        | interface | 1/1/2      |            |
| switch(config-if)#      |        |           | vlan trunk | allowed 20 |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDs2,3,and4.
| switch#            | config |           |            |               |
| ------------------ | ------ | --------- | ---------- | ------------- |
| switch(config)#    |        | vlan      | 2,3,4      |               |
| switch(config)#    |        | interface | 1/1/2      |               |
| switch(config-if)# |        |           | vlan trunk | allowed 2,3,4 |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDs2to8.
| switch#            | config |           |            |             |
| ------------------ | ------ | --------- | ---------- | ----------- |
| switch(config)#    |        | vlan      | 2-8        |             |
| switch(config)#    |        | interface | 1/1/2      |             |
| switch(config-if)# |        |           | vlan trunk | allowed 2-8 |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDs2 to8and10.
| switch#            | config |           |            |                |
| ------------------ | ------ | --------- | ---------- | -------------- |
| switch(config)#    |        | vlan      | 2-8,10     |                |
| switch(config)#    |        | interface | 1/1/2      |                |
| switch(config-if)# |        |           | vlan trunk | allowed 2-8,10 |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficonallconfiguredVLANIDs(20-
100).
| switch#            | config |           |            |                |
| ------------------ | ------ | --------- | ---------- | -------------- |
| switch(config)#    |        | vlan      | 20-100     |                |
| switch(config)#    |        | interface | 1/1/2      |                |
| switch(config-if)# |        |           | vlan trunk | allowed all    |
| Assigninga         | native | VLAN      | ID toa     | trunkinterface |
Prerequisites
AtleastonedefinedVLAN.
Procedure
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 28

1. Switchtoconfigurationcontextwiththecommandconfig.
2. SwitchtothetrunkinterfacetowhichyouwanttoassignthenativeVLANIDwiththecommand
interface.
3. AssignthenativeVLANIDwiththecommandvlan trunk native.Iftaggingisrequired,usethe
| commandvlan |     | trunk native | tag. |     |
| ----------- | --- | ------------ | ---- | --- |
4. AllowtraffictaggedwiththenativeVLANIDtobetransportedbythetrunkusingthecommandvlan
| trunk | allowed. |     |     |     |
| ----- | -------- | --- | --- | --- |
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ThisexampleassignsnativeVLANID20totrunkinterface1/1/2.
| switch#                 | config |           |              |     |
| ----------------------- | ------ | --------- | ------------ | --- |
| switch(config)#         |        | vlan 20   |              |     |
| switch(config-vlan-20)# |        |           | exit         |     |
| switch(config)#         |        | interface | 1/1/2        |     |
| switch(config-if)#      |        | vlan      | trunk native | 20  |
ThisexampleassignsnativeVLANID40totrunkinterface1/1/5,enablestagging,andallowstrafficwith
VLANID40tobetransportedbythetrunk.
| switch#                 | config |           |              |        |
| ----------------------- | ------ | --------- | ------------ | ------ |
| switch(config)#         |        | vlan 40   |              |        |
| switch(config-vlan-40)# |        |           | exit         |        |
| switch(config)#         |        | interface | 1/1/5        |        |
| switch(config-if)#      |        | vlan      | trunk native | 40 tag |
switch(config-if)#
|         |      | vlan          | trunk allow | 40          |
| ------- | ---- | ------------- | ----------- | ----------- |
| Viewing | VLAN | configuration |             | information |
Prerequisites
AtleastonedefinedVLAN.
Procedure
1. ViewasummaryofVLANconfigurationinformationwiththecommandshow vlan summary.
2. ViewVLANconfigurationsettingswiththecommandshow vlan.
3. ViewVLANsconfiguredforaspecificlayer2interfacewiththecommandshow vlan port.
4. ViewthecommandsusedtoconfigureVLANsettingswiththecommandshow
running-config
interface.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ThisexampledisplaysasummaryofallVLANs.
| switch# | show        | vlan summary |     |     |
| ------- | ----------- | ------------ | --- | --- |
| Number  | of existing | VLANs:       | 11  |     |
| Number  | of static   | VLANs:       | 11  |     |
| Number  | of dynamic  | VLANs:       | 0   |     |
VLANs|29

ThisexampledisplaysconfigurationinformationforalldefinedVLANs.
| switch# show | vlan |     |     |     |     |
| ------------ | ---- | --- | --- | --- | --- |
-----------------------------------------------------------------------------------
| VLAN Name |     | Status Reason |     | Type | Interfaces |
| --------- | --- | ------------- | --- | ---- | ---------- |
-----------------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1                                   |     | up ok           |     | static | 1/1/3-1/1/4             |
| -------------------------------------------------- | --- | --------------- | --- | ------ | ----------------------- |
| 2 UserVLAN1                                        |     | up ok           |     | static | 1/1/1,1/1/3,1/1/5       |
| 3 UserVLAN2                                        |     | up ok           |     | static | 1/1/2-1/1/3,1/1/5-1/1/6 |
| 5 UserVLAN3                                        |     | up ok           |     | static | 1/1/3                   |
| 10 TestNetwork                                     |     | up ok           |     | static | 1/1/3,1/1/5             |
| 11 VLAN11                                          |     | up ok           |     | static | 1/1/3                   |
| 12 VLAN12                                          |     | up ok           |     | static | 1/1/3,1/1/6,lag1-lag2   |
| 13 VLAN13                                          |     | up ok           |     | static | 1/1/3,1/1/6             |
| 14 VLAN14                                          |     | up ok           |     | static | 1/1/3,1/1/6             |
| 20 ManagementVLAN                                  |     | down admin_down |     | static | 1/1/3,1/1/10            |
| ThisexampledisplaysconfigurationinformationforVLAN |     |                 |     | 2.     |                         |
switch#
show vlan 2
-----------------------------------------------------------------------------------
| VLAN Name |     | Status | Reason | Type | Interfaces |
| --------- | --- | ------ | ------ | ---- | ---------- |
-----------------------------------------------------------------------------------
| 2 UserVLAN1 |     | up  | ok  | static | 1/1/1,1/1/3,1/1/5 |
| ----------- | --- | --- | --- | ------ | ----------------- |
ThisexampledisplaystheVLANsconfiguredoninterface1/1/3.
| switch# show | vlan port | 1/1/3 |     |     |     |
| ------------ | --------- | ----- | --- | --- | --- |
------------------------------------------------------
| VLAN Name |     |     | Mode |     |     |
| --------- | --- | --- | ---- | --- | --- |
------------------------------------------------------
| 1 DEFAULT_VLAN_1  |     |     | native-untagged |     |     |
| ----------------- | --- | --- | --------------- | --- | --- |
| 2 UserVLAN1       |     |     | trunk           |     |     |
| 3 UserVLAN2       |     |     | trunk           |     |     |
| 5 UserVLAN3       |     |     | trunk           |     |     |
| 10 TestNetwork    |     |     | trunk           |     |     |
| 11 VLAN11         |     |     | trunk           |     |     |
| 12 VLAN12         |     |     | trunk           |     |     |
| 13 VLAN13         |     |     | trunk           |     |     |
| 14 VLAN14         |     |     | trunk           |     |     |
| 20 ManagementVLAN |     |     | trunk           |     |     |
ThisexampledisplaysVLANconfigurationcommandsforinterface1/1/16.
| switch# show | running-config | interface | 1/1/16 |     |     |
| ------------ | -------------- | --------- | ------ | --- | --- |
| interface    | 1/1/16         |           |        |     |     |
no routing
| vlan trunk | native  | 108 |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
| vlan trunk | allowed | all |     |     |     |
exit
VLAN scenario
ThisscenarioshowshowtoassignVLANIDstoaccessandtrunkinterfacesforthefollowingdeployment:
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 30

Onthe6400SwitchSeries,interfaceidentificationdiffers.
Inthisscenario,VLANsareusedtoisolatethetrafficfromdifferentdevices.
n VLAN25carriestaggedanduntaggedtrafficfromcomputersconnectedtoswitchB.
n VLAN4carriestaggedtrafficfromcomputersconnectedtoswitchB.
VLAN6carriestaggedanduntaggedtrafficfromcomputersconnectedtoswitchC.
n
VLAN17carriestaggedtrafficfromcomputersconnectedtoswitchC.
n
n VLAN100carriesuntaggedtrafficfromtheserver.
Procedure
1. ExecutethefollowingcommandsonswitchAandB.
a. CreateVLANs4and25.
switch# config
| switch(config)# | vlan 4,25 |     |     |
| --------------- | --------- | --- | --- |
b. DefineLAG1andassigntheVLANstoit.
| switch(config)# | interface | lag 1 |     |
| --------------- | --------- | ----- | --- |
switch(config-lag-if)#
|                        |     | no shutdown |              |
| ---------------------- | --- | ----------- | ------------ |
| switch(config-lag-if)# |     | vlan trunk  | native 25    |
| switch(config-lag-if)# |     | vlan trunk  | allowed 4,25 |
c. Addports1/1/1and1/2/1toLAG1.
| switch(config-lag-if)# |     | interface | 1/1/1 |
| ---------------------- | --- | --------- | ----- |
VLANs|31

| switch(config-if)# |     | no shutdown |     |       |     |     |
| ------------------ | --- | ----------- | --- | ----- | --- | --- |
| switch(config-if)# |     | lag         | 1   |       |     |     |
| switch(config-if)# |     | interface   |     | 1/2/1 |     |     |
| switch(config-if)# |     | no shutdown |     |       |     |     |
| switch(config-if)# |     | lag         | 1   |       |     |     |
2. ExecutethefollowingcommandsonswitchAandC.
a. CreateVLANs6and17.
| switch# config  |      |      |     |     |     |     |
| --------------- | ---- | ---- | --- | --- | --- | --- |
| switch(config)# | vlan | 6,17 |     |     |     |     |
b. DefineLAG3andassigntheVLANstoit.
| switch(config)#        | interface |     | lag         | 3                  |     |     |
| ---------------------- | --------- | --- | ----------- | ------------------ | --- | --- |
| switch(config-lag-if)# |           |     | no shutdown |                    |     |     |
| switch(config-lag-if)# |           |     | vlan        | trunk native 6 tag |     |     |
| switch(config-lag-if)# |           |     | vlan        | trunk allowed 6,17 |     |     |
c. Addports1/1/13and1/2/13toLAG3.
| switch(config-lag-if)# |     |             | interface | 1/1/13 |     |     |
| ---------------------- | --- | ----------- | --------- | ------ | --- | --- |
| switch(config-if)#     |     | no shutdown |           |        |     |     |
| switch(config-if)#     |     | lag         | 3         |        |     |     |
| switch(config-if)#     |     | interface   |           | 1/2/13 |     |     |
| switch(config-if)#     |     | no shutdown |           |        |     |     |
| switch(config-if)#     |     | no routing  |           |        |     |     |
| switch(config-if)#     |     | lag         | 3         |        |     |     |
3. ExecutethefollowingcommandsonswitchAtoconfiguretheconnectiontotheserver.Configure
interface1/2/13asanaccessinterfacewithVLANIDsetto100.
switch# config
| switch (config)#         | vlan | 100       |     |        |     |     |
| ------------------------ | ---- | --------- | --- | ------ | --- | --- |
| switch(config-vlan-100)# |      | interface |     | 1/2/32 |     |     |
| switch(config-if)#       | no   | shutdown  |     |        |     |     |
| switch(config-if)#       | vlan | access    | 100 |        |     |     |
| switch(config-if)#       | exit |           |     |        |     |     |
4. VerifyVLANconfigurationbyrunningthecommandshow vlan.Forexample:
| switch# show vlan |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- |
---------------------------------------------------------------------------
| VLAN Name |     | Status |     | Reason | Type | Interfaces |
| --------- | --- | ------ | --- | ------ | ---- | ---------- |
---------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     | down |     | no_member_port | default |      |
| ---------------- | --- | ---- | --- | -------------- | ------- | ---- |
| 4 VLAN4          |     | up   |     | ok             | static  | lag1 |
| 6 VLAN6          |     | up   |     | ok             | static  | lag3 |
| 17 VLAN17        |     | up   |     | ok             | static  | lag3 |
| 25 VLAN25        |     | up   |     | ok             | static  | lag1 |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 32

| 100 VLAN100 |     |     | up  | ok  | static | 1/2/32 |
| ----------- | --- | --- | --- | --- | ------ | ------ |
5. VerifythattheconnectiontotheDHCPserverissending/receivingdatawiththecommandshow
interface.CheckthattheRxandTxfieldsareincrementing.Forexample:
| switch#   | show interface | 1/2/32 |     |     |     |     |
| --------- | -------------- | ------ | --- | --- | --- | --- |
| Interface | 1/2/32         | is up  |     |     |     |     |
| Admin     | state is up    |        |     |     |     |     |
Description:
| Hardware: | Ethernet, | MAC | Address: | 70:72:cf:3a:8a:0b |     |     |
| --------- | --------- | --- | -------- | ----------------- | --- | --- |
MTU 1500
Type SFP+LR
| qos trust        | none         |         |        |              |        |     |
| ---------------- | ------------ | ------- | ------ | ------------ | ------ | --- |
| Speed            | 10000 Mb/s   |         |        |              |        |     |
| Auto-Negotiation |              | is off  |        |              |        |     |
| Input            | flow-control | is off, | output | flow-control | is off |     |
| VLAN Mode:       | access       |         |        |              |        |     |
| Access           | VLAN: 100    |         |        |              |        |     |
Rx
|     | 20 input | packets |     | 1280      | bytes |     |
| --- | -------- | ------- | --- | --------- | ----- | --- |
|     | 0 input  | error   |     | 0 dropped |       |     |
0 CRC/FCS
Tx
|     | 9 output | packets |     | 1054      | bytes |     |
| --- | -------- | ------- | --- | --------- | ----- | --- |
|     | 0 input  | error   |     | 0 dropped |       |     |
0 collision
6. VerifyLAGinterfaceconfigurationwiththecommandshow interface.Checkthefieldsadminstate,
MACaddress,Aggregated-interfaces,VLANMode,NativeVLAN,AllowedVLAN,Rxcount,andTx
count.Forexample:
| switch#               | show interface  | lag1      |                   |       |     |     |
| --------------------- | --------------- | --------- | ----------------- | ----- | --- | --- |
| Aggregate-name        | lag1            |           |                   |       |     |     |
| Description           | :               |           |                   |       |     |     |
| Admin                 | state           | :         | up                |       |     |     |
| MAC Address           |                 | :         | 94:f1:28:21:63:00 |       |     |     |
| Aggregated-interfaces |                 | :         | 1/1/1             | 1/2/1 |     |     |
| Aggregation-key       |                 | :         | 1                 |       |     |     |
| Speed                 |                 | :         | 1000 Mb/s         |       |     |     |
| L3 Counters:          | Rx              | Disabled, | Tx Disabled       |       |     |     |
| qos trust             | none            |           |                   |       |     |     |
| VLAN Mode:            | native-untagged |           |                   |       |     |     |
| Native                | VLAN: 25        |           |                   |       |     |     |
| Allowed               | VLAN List:      | 4,25      |                   |       |     |     |
Rx
|     | 10 input | packets |     | 1280      | bytes |     |
| --- | -------- | ------- | --- | --------- | ----- | --- |
|     | 0 input  | error   |     | 0 dropped |       |     |
0 CRC/FCS
Tx
|     | 8 output | packets |     | 980       | bytes |     |
| --- | -------- | ------- | --- | --------- | ----- | --- |
|     | 0 input  | error   |     | 0 dropped |       |     |
0 collision
VLANs|33

| switch#               | show interface | lag3      |                   |        |     |
| --------------------- | -------------- | --------- | ----------------- | ------ | --- |
| Aggregate-name        | lag3           |           |                   |        |     |
| Description           | :              |           |                   |        |     |
| Admin state           |                | :         | up                |        |     |
| MAC Address           |                | :         | 94:f1:28:21:63:00 |        |     |
| Aggregated-interfaces |                | :         | 1/1/13            | 1/2/13 |     |
| Aggregation-key       |                | :         | 3                 |        |     |
| Speed 1000            | Mb/s           |           |                   |        |     |
| L3 Counters:          | Rx             | Disabled, | Tx Disabled       |        |     |
| qos trust             | none           |           |                   |        |     |
| VLAN Mode:            | native-tagged  |           |                   |        |     |
| Native                | VLAN: 6        |           |                   |        |     |
| Allowed               | VLAN List:     | 6,17      |                   |        |     |
Rx
|     | 19 input | packets |     |     | 1280 bytes |
| --- | -------- | ------- | --- | --- | ---------- |
|     | 0 input  | error   |     |     | 0 dropped  |
0 CRC/FCS
Tx
|     | 15 output | packets |     |     | 1000 bytes |
| --- | --------- | ------- | --- | --- | ---------- |
|     | 0 input   | error   |     |     | 0 dropped  |
0 Collision
7. Verifythephysicalinterfaces(1/1/1,1/2/1,1/1/13,1/2/13)withthecommandshow interface.
CheckthattheRxandTxfieldsareincrementing.Forexample:
| switch#     | show interface | 1/1/1 |     |     |     |
| ----------- | -------------- | ----- | --- | --- | --- |
| Interface   | 1/1/1 is       | up    |     |     |     |
| Admin state | is up          |       |     |     |     |
Description:
| Hardware: | Ethernet, | MAC | Address: | 94:f1:28:21:73:ff |     |
| --------- | --------- | --- | -------- | ----------------- | --- |
MTU 1500
Type SFP+LR
| qos trust          | none |         |        |              |        |
| ------------------ | ---- | ------- | ------ | ------------ | ------ |
| Speed 1000         | Mb/s |         |        |              |        |
| Auto-Negotiation   |      | is off  |        |              |        |
| Input flow-control |      | is off, | output | flow-control | is off |
Rx
|     | 6 input | packets |     |     | 620 bytes |
| --- | ------- | ------- | --- | --- | --------- |
|     | 0 input | error   |     |     | 0 dropped |
0 CRC/FCS
Tx
|     | 4 output | packets |     |     | 422 bytes |
| --- | -------- | ------- | --- | --- | --------- |
|     | 0 input  | error   |     |     | 0 dropped |
0 collision
VLAN commands
description
Syntax
description <DESCRIPTION>
Description
SpecifiesadescriptiveforaVLAN.
Commandcontext
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 34

config-vlan-<VLAN-ID>

Parameters

<DESCRIPTION>

Specifies a description for the VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Examples

Assigning a description to VLAN 20:

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

VLANs | 35

Manager(#)
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ShowingswitchSVIcapacity:
| switch#    | show        | capacities | svi-count |       |     |       |
| ---------- | ----------- | ---------- | --------- | ----- | --- | ----- |
| System     | Capacities: | Filter     | SVI       | count |     |       |
| Capacities |             | Name       |           |       |     | Value |
---------------------------------------------------------------------
| Maximum | number | of SVIs | supported | in the system |     | 128 |
| ------- | ------ | ------- | --------- | ------------- | --- | --- |
| show    | vlan   |         |           |               |     |     |
Syntax
| show vlan | [<VLAN-ID>] | [vsx-peer] |     |     |     |     |
| --------- | ----------- | ---------- | --- | --- | --- | --- |
Description
DisplaysconfigurationinformationforallVLANsoraspecificVLAN.
Commandcontext
| Manager | (#) |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- |
Parameters
<VLAN-ID>
SpecifiesaVLANID.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
DisplayingconfigurationinformationforVLAN2:
| switch# | show | vlan 2 |     |     |     |     |
| ------- | ---- | ------ | --- | --- | --- | --- |
----------------------------------------------------------------------------------
| VLAN | Name |     |     | Status Reason | Type | Interfaces |
| ---- | ---- | --- | --- | ------------- | ---- | ---------- |
----------------------------------------------------------------------------------
| 2   | UserVLAN1 |     |     | up ok | static | 1/1/1,1/1/3,1/1/5 |
| --- | --------- | --- | --- | ----- | ------ | ----------------- |
DisplayingconfigurationinformationforalldefinedVLANs:
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 36

| switch# | show vlan |     |     |     |
| ------- | --------- | --- | --- | --- |
----------------------------------------------------------------------------------
| VLAN | Name | Status Reason | Type | Interfaces |
| ---- | ---- | ------------- | ---- | ---------- |
-----------------------------------------------------------------------------------
| 1    | DEFAULT_VLAN_1 | up ok           | static | 1/1/3-1/1/4             |
| ---- | -------------- | --------------- | ------ | ----------------------- |
| 2    | UserVLAN1      | up ok           | static | 1/1/1,1/1/3,1/1/5       |
| 3    | UserVLAN2      | up ok           | static | 1/1/2-1/1/3,1/1/5-1/1/6 |
| 5    | UserVLAN3      | up ok           | static | 1/1/3                   |
| 10   | TestNetwork    | up ok           | static | 1/1/3,1/1/5             |
| 11   | VLAN11         | up ok           | static | 1/1/3                   |
| 12   | VLAN12         | up ok           | static | 1/1/3,1/1/6,lag1-lag2   |
| 13   | VLAN13         | up ok           | static | 1/1/3,1/1/6             |
| 14   | VLAN14         | up ok           | static | 1/1/3,1/1/6             |
| 20   | ManagementVLAN | down admin_down | static | 1/1/3,1/1/10            |
| show | vlan port      |                 |        |                         |
Syntax
| show vlan | port <INTERFACE-ID> | [vsx-peer] |     |     |
| --------- | ------------------- | ---------- | --- | --- |
Description
DisplaystheVLANsconfiguredforaspecificlayer2interface.
Commandcontext
Manager(#)
Parameters
<INTERFACE-ID>
SpecifiesaninterfaceID.Format:member/slot/port.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
DisplayingtheVLANsconfiguredoninterface1/1/3:
| switch# | show vlan port | 1/1/3 |     |     |
| ------- | -------------- | ----- | --- | --- |
------------------------------------------------------
| VLAN | Name | Mode |     |     |
| ---- | ---- | ---- | --- | --- |
------------------------------------------------------
| 1   | DEFAULT_VLAN_1 | native-untagged |     |     |
| --- | -------------- | --------------- | --- | --- |
| 2   | UserVLAN1      | trunk           |     |     |
| 3   | UserVLAN2      | trunk           |     |     |
| 5   | UserVLAN3      | trunk           |     |     |
| 10  | TestNetwork    | trunk           |     |     |
| 11  | VLAN11         | trunk           |     |     |
VLANs|37

| 12   | VLAN12         |     | trunk |     |
| ---- | -------------- | --- | ----- | --- |
| 13   | VLAN13         |     | trunk |     |
| 14   | VLAN14         |     | trunk |     |
| 20   | ManagementVLAN |     | trunk |     |
| show | vlan summary   |     |       |     |
Syntax
| show vlan | summary[vsx-peer] |     |     |     |
| --------- | ----------------- | --- | --- | --- |
Description
DisplaysasummaryoftheVLANconfigurationontheswitch.
Commandcontext
Manager(#)
Parameters
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
DisplayingasummaryoftheVLANconfigurationontheswitch:
| switch# | show vlan        | summary |     |     |
| ------- | ---------------- | ------- | --- | --- |
| Number  | of existing      | VLANs:  | 11  |     |
| Number  | of static        | VLANs:  | 11  |     |
| Number  | of dynamic       | VLANs:  | 0   |     |
| show    | vlan translation |         |     |     |
Syntax
| show vlan | translation | [interface | <INTERFACE-NAME>] | [vsx-peer] |
| --------- | ----------- | ---------- | ----------------- | ---------- |
Description
ShowsasummaryofallVLANtranslationsrulesdefinedontheswitch,ortherulesdefinedforaspecific
interface.
Commandcontext
Manager(#)
Parameters
| interface | <INTERFACE-NAME> |     |     |     |
| --------- | ---------------- | --- | --- | --- |
Specifiesthenameofalayer2interface.Format:member/slot/port.
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 38

[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
DisplayingasummaryofallVLANtranslationsrulesdefinedontheswitch:
| switch# | show vlan translation |     |     |
| ------- | --------------------- | --- | --- |
-------------------------------------------
| Interface | VLAN-1 | VLAN-2 |     |
| --------- | ------ | ------ | --- |
-------------------------------------------
| 1/1/5        | 10             | 20        |     |
| ------------ | -------------- | --------- | --- |
| 1/1/5        | 30             | 40        |     |
| 1/1/5        | 50             | 100       |     |
| 1/1/6        | 100            | 200       |     |
| Total number | of translation | rules : 4 |     |
DisplayingasummaryofallVLANtranslationsrulesdefinedoninterface1/1/5:
| switch# | show vlan translation | interface | 1/1/5 |
| ------- | --------------------- | --------- | ----- |
-------------------------------------------
| Interface | VLAN-1 | VLAN-2 |     |
| --------- | ------ | ------ | --- |
-------------------------------------------
| 1/1/5 | 10  | 20  |     |
| ----- | --- | --- | --- |
| 1/1/5 | 30  | 40  |     |
| 1/1/5 | 50  | 100 |     |
shutdown
Syntax
shutdown
no shutdown
Description
DisablesaVLAN.(Bydefault,aVLANisautomaticallyenabledwhenitiscreatedwiththevlancommand.)
ThenoformofthiscommandenablesaVLAN.
Commandcontext
config-vlan-<VLAN-ID>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingVLAN20:
VLANs|39

switch(config)# vlan 20
switch(config-vlan-20)# no shutdown

Disabling VLAN 20:

switch(config)# vlan 20
switch(config-vlan-20)# shutdown

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

40

Command context

config

Parameters

<VLAN-LIST>

Specifies a single ID, or a series of IDs separated by commas (2, 3, 4), dashes (2-4), or both (2-4,6). Range:
1 to 4094.

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
routed (layer 3) when created. Use the no routing command to disable routing on an interface and change
the interface to a layer 2 interface.

The no form of this command removes an access VLAN from the interface in the current context and sets it
to the default VLAN ID of 1.

Command context

config-if

Parameters

VLANs | 41

<VLAN-ID>
SpecifiesasingleID,oraseriesofIDsseparatedbycommas(2,3,4),dashes(2-4),orboth(2-4,6).Range:
1to4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Configuringinterface1/1/2asanaccessinterfacewithVLANIDsetto20:
| switch(config)# | interface | 1/1/2 |
| --------------- | --------- | ----- |
switch(config-if)#
|     | vlan | access 20 |
| --- | ---- | --------- |
RemovingVLANID20frominterface1/1/2:
| switch(config)#    | interface | 1/1/2     |
| ------------------ | --------- | --------- |
| switch(config-if)# | no vlan   | access 20 |
or:
| switch(config)#    | interface | 1/1/2  |
| ------------------ | --------- | ------ |
| switch(config-if)# | no vlan   | access |
vlan translate
Syntax
| vlan translate <VLAN-1> | <VLAN-2> |          |
| ----------------------- | -------- | -------- |
| no vlan translate       | <VLAN-1> | <VLAN-2> |
Description
DefinesabidirectionalVLANtranslationrulethatmapsanexternalVLANIDtoaninternalVLANIDonaLAG
orlayer2interface.Appliestobothincomingandoutgoingtraffic.
ThenoformofthiscommandremovesanexistingVLANtranslationruleonthecurrentinterface.
VLANtranslationandMVRPcannotbeenabledonthesameinterface.
Commandcontext
config-if
config-lag-if
Parameters
<VLAN-1>
SpecifiesthenumberofanexternalVLAN.
<VLAN-2>
SpecifiesthenumberofanexternalVLAN.
Authority
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 42

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
TranslatesexternalVLAN200tointernalVLAN20oninterface1/1/2.
| switch#                 | config |            |               |        |
| ----------------------- | ------ | ---------- | ------------- | ------ |
| switch(config)#         |        | vlan 20    |               |        |
| switch(config-vlan-20)# |        |            | exit          |        |
| switch(config)#         |        | interface  | 1/1/2         |        |
| switch(config-if)#      |        | no routing |               |        |
| switch(config-if)#      |        | vlan       | trunk allowed | 20     |
| switch(config-if)#      |        | vlan       | translate     | 200 20 |
TranslatesexternalVLANs100and300tointernalVLANs10and20oninterface1/1/2.
| switch#                 | config  |            |               |        |
| ----------------------- | ------- | ---------- | ------------- | ------ |
| switch(config)#         |         | vlan 10,30 |               |        |
| switch(config-vlan-20)# |         |            | exit          |        |
| switch(config)#         |         | interface  | 1/1/2         |        |
| switch(config-if)#      |         | no routing |               |        |
| switch(config-if)#      |         | vlan       | trunk allowed | 10,30  |
| switch(config-if)#      |         | vlan       | translate     | 100 10 |
| switch(config-if)#      |         | vlan       | translate     | 300 30 |
| vlan trunk              | allowed |            |               |        |
Syntax
| vlan trunk | allowed       | [<VLAN-LIST>  | |   | all] |
| ---------- | ------------- | ------------- | --- | ---- |
| no vlan    | trunk allowed | [<VLAN-LIST>] |     |      |
Description
AssignsaVLANIDtoantrunkinterface.MultipleVLANIDscanbeassignedtoatrunkinterface.TheseVLAN
IDsdefinewhichVLANtrafficisallowedacrossthetrunkinterface.
VLANscanbeassignedonlytoanon-routed(layer2)interfaceorLAGinterface.Bydefault,allinterfacesare
routed(layer3)whencreated.Usetheno routingcommandtodisableroutingonaninterface.
ThenoformofthiscommandremovesoneormoreVLANIDsfromatrunkinterface.WhenthelastVLANis
removedfromatrunkinterface,theinterfacecontinuestooperateintrunkmode,andwilltrunkallthe
VLANscurrentlydefinedontheswitch,andanynewVLANsdefinedinthefuture.Todisablethetrunk
interface,usetheshutdowncommand.
Commandcontext
config-if
Parameters
<VLAN-LIST>
SpecifiesasingleID,oraseriesofIDsseparatedbycommas(2,3,4),dashes(2-4),orboth(2-4,6).Range:
1to4094.
all
ConfiguresthetrunkinterfacetoallowalltheVLANscurrentlyconfiguredontheswitchandanynew
VLANsthatareconfiguredinthefuture.
Authority
VLANs|43

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
AssigningVLANs2,3,and4totrunkinterface1/1/2:
| switch(config)#    | interface | 1/1/2               |
| ------------------ | --------- | ------------------- |
| switch(config-if)# | vlan      | trunk allowed 2,3,4 |
AssigningVLANIDs2to8totrunkinterface1/1/2:
| switch(config)#    | interface | 1/1/2             |
| ------------------ | --------- | ----------------- |
| switch(config-if)# | vlan      | trunk allowed 2-8 |
AssigningVLANIDs2to8and10totrunkinterface1/1/2:
| switch(config)#    | interface | 1/1/2                |
| ------------------ | --------- | -------------------- |
| switch(config-if)# | vlan      | trunk allowed 2-8,10 |
RemovingVLANIDs2,3,and4fromtrunkinterface1/1/2:
| switch(config)#    | interface | 1/1/2               |
| ------------------ | --------- | ------------------- |
| switch(config-if)# | no vlan   | trunk allowed 2,3,4 |
RemovingallVLANsassignedtotrunkinterface1/1/2:
| switch(config)#    | interface | 1/1/2         |
| ------------------ | --------- | ------------- |
| switch(config-if)# | no vlan   | trunk allowed |
| vlan trunk native  |           |               |
Syntax
| vlan trunk native    | <VLAN-ID>   |     |
| -------------------- | ----------- | --- |
| no vlan trunk native | [<VLAN-ID>] |     |
Description
AssignsanativeVLANIDtoatrunkinterface.Bydefault,VLANID1isassignedasthenativeVLANIDforall
trunkinterfaces.VLANscanonlybeassignedtoanon-routed(layer2)interfaceorLAGinterface.Onlyone
VLANIDcanbeassignedasthenativeVLAN.
WhenanativeVLANisdefined,theswitchautomaticallyexecutesthevlan trunk allowed allcommandto
ensurethatthedefaultVLANisallowedonthetrunk.ToonlyallowspecificVLANsonthetrunk,issuethevlan
trunk allowedcommandspecifyingonlyspecificVLANs.
ThenoformofthiscommandremovesanativeVLANfromatrunkinterfaceandassignsVLANID1asits
nativeVLAN.
Commandcontext
config-if
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 44

Parameters
<VLAN-ID>
SpecifiesaVLANID.Range:1to4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
AssigningnativeVLANID20totrunkinterface1/1/2:
| switch(config)#    |     | interface | 1/1/2 |           |
| ------------------ | --- | --------- | ----- | --------- |
| switch(config-if)# |     | vlan      | trunk | native 20 |
RemovingnativeVLAN20fromtrunkinterface1/1/2andreturningtothedefaultVLAN1asthenative
VLAN.
| switch(config)#    |     | interface | 1/1/2 |                 |
| ------------------ | --- | --------- | ----- | --------------- |
| switch(config-if)# |     | no        | vlan  | trunk native 20 |
or:
| switch(config)#    |     | interface | 1/1/2 |              |
| ------------------ | --- | --------- | ----- | ------------ |
| switch(config-if)# |     | no        | vlan  | trunk native |
AssigningnativeVLANID20totrunkinterface1/1/2andthenremovingitfromthelistofallowedVLANs.
(OnlyallowVLAN10onthetrunk.)
| switch(config)#    |        | interface | 1/1/2 |            |
| ------------------ | ------ | --------- | ----- | ---------- |
| switch(config-if)# |        | vlan      | trunk | native 20  |
| switch(config-if)# |        | vlan      | trunk | allowed 10 |
| vlan trunk         | native | tag       |       |            |
Syntax
| vlan trunk | native       | <VLAN-ID> | tag |     |
| ---------- | ------------ | --------- | --- | --- |
| no vlan    | trunk native | <VLAN-ID> |     | tag |
Description
EnablestaggingonanativeVLAN.OnlyincomingpacketsthataretaggedwiththematchingVLANIDare
accepted.IncomingpacketsthatareuntaggedaredroppedexceptforBPDUs.Egresspacketsaretagged.
ThenoformofthiscommandremovestaggingonanativeVLAN.
Commandcontext
config-if
Parameters
<VLAN-ID>
VLANs|45

SpecifiesthenumberofaVLAN.Range:1to4094.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingtaggingonnativeVLAN20ontrunkinterface1/1/2:
| switch(config)#    | interface | 1/1/2 |        |        |
| ------------------ | --------- | ----- | ------ | ------ |
| switch(config-if)# | vlan      | trunk | native | 20     |
| switch(config-if)# | vlan      | trunk | native | 20 tag |
RemovingtaggingonnativeVLAN20assignedtotrunkinterface1/1/2:
| switch(config)#    | interface | 1/1/2 |              |        |
| ------------------ | --------- | ----- | ------------ | ------ |
| switch(config-if)# | no        | vlan  | trunk native | 20 tag |
EnablingtaggingonnativeVLAN20assignedtoLAGtrunkinterface2:
| switch(config)#        | interface | lag  | 2            |        |
| ---------------------- | --------- | ---- | ------------ | ------ |
| switch(config-lag-if)# |           | vlan | trunk native | 20     |
| switch(config-lag-if)# |           | vlan | trunk native | 20 tag |
voice
Syntax
voice
no voice
Description
ConfiguresaVLANasavoiceVLAN.
ThenoformofthiscommandremovesvoiceconfigurationfromaVLAN.
Commandcontext
config-vlan-<VLAN-ID>
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ConfiguringVLAN10asavoiceVLAN:
| switch(config)#         | vlan | 10    |     |     |
| ----------------------- | ---- | ----- | --- | --- |
| switch(config-vlan-10)# |      | voice |     |     |
RemovingvoicefromVLAN10:
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 46

switch(config-vlan-10)# no voice

VLANs | 47

Chapter 5

Loop protection

Loop protection

In cases where spanning tree protocols cannot be used to prevent loops at the edge of the network, loop
protection may provide a suitable alternative. Loop protection can find loops in untagged layer 2 links, as
well as on tagged VLANs.

The cases where loop protection might be chosen ahead of spanning tree to detect and prevent loops are:

n On ports with client authentication: When spanning tree is enabled on a switch that uses 802.1X, web
authentication, or MAC authentication, loops may go undetected. For example, spanning tree packets
that are looped back to an edge port will not be processed because they have a different
broadcast/multicast MAC address from the client-authenticated MAC address. To ensure that client-
authenticated edge ports get blocked when loops occur, you should enable loop protection on those
ports.

n On ports connected to unmanaged devices: Spanning tree cannot detect the formation of loops where
there is an unmanaged device on the network that does not process spanning tree packets and simply
drops them. Loop protection has no such limitation, and can be used to prevent loops on unmanaged
switches.

Loop protection finds loops by sending loop protection packets on each port, LAG, or VLAN on which loop
protection is enabled. If a loop protection packet is received by the same switch that sent it, it indicates a
loop exists and one of the following actions is taken:

n Discovery of the loop is logged but port states are not changed.

n The sending port is disabled.

n The sending and receiving ports are both disabled.

Interaction with other protocols

n When loop protection is enabled before STP, and if there is an L2 loop, then the loop will be detected and

the port will be disabled.

n When STP is enabled before loop protection, and if there is a L2 loop, then the port will be moved to the
blocked state by STP. When a port is blocked, the loop protection packet will not reach the sending

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

48

switch, and the loop will not be detected by loop protection. When multiple instances of STP are
configured and different spanning trees are formed for different instances, the PSPO state will be
forwarding. In this case, loop- protection will consider those ports as normal forwarding ports and will
override the STP states.

n STP is mutually exclusive with loop protection. If STP and loop protection are both enabled on the same

VLAN, STP takes precedence. This means that loop protection does not take any action on a port blocked
by STP.

n MVRP and the loop protection interoperate with each other. However, dynamic VLANs cannot be tagged
to a port through user configuration. Therefore, it is not possible to configure a dynamic VLAN as a loop
protection enabled VLAN.

n If MCLAG has marked a port as transmit disable (mclag_pdu_tx_disable is set to true), then loop-protect
will not transmit packets on the port. Similarly, if the loop_detect_source column is set to mclag then
loop protection will not re-enable the port when the re-enable timer expires on that port.

Configuring loop protection

Procedure

1. Enable loop protection on each layer 2 interface (port, LAG, or VLAN) for which loop protection is

needed, with the commands loop-protect and loop-protect vlan.

2. Define the action to be taken when a loop is detected with the command loop-protect action. The
default action is tx-disable, which means that the port that transmitted the loop detection packet is
disabled. When this action is enabled, environments with N loops must have loop protection
configured on at least N-1 ports to ensure a loop free topology.

When the default action (tx-disable) is used, it is optional to enable loop protect in all
interfaces. By enabling loop protect in a single interface, the loop is detected and the default

action is executed. So when the packet from a loop protect-enabled port is received back on an

interface where loop protect is not enabled, the loop protect receiver action corresponding to the

receiving interface is executed. Please note that all the L2 ports will have a default receiver
action of tx-disable even when loop protect is not enabled.

3.

4.

If required, change the interval at which loop protection messages are sent with the command loop-
protect transmit-interval.

If required, change the length of time the switch waits before re-enabling an interface with the
command loop-protect re-enable-timer.

5. Review loop protection configuration settings with the command show loop-protect.

Example

On the 6400 Switch Series, interface identification differs.

This example creates the following configuration:

n Enables loop protection on data port 1/1/1 and sets the loop detection action to disable the transmit

port.

n Enables loop protection on LAG 25 and sets the loop detection action to disable both transmit and

receive ports.

n Enables loop protection on VLANs 100-125 and 200.

Loop protection | 49

Setsthere-enabletimerto10seconds.
n
Setsthetransmit-intervalto30seconds.
n
| switch(config)#        |          | interface    |              | 1/1/1           |               |     |
| ---------------------- | -------- | ------------ | ------------ | --------------- | ------------- | --- |
| switch(config-if)#     |          |              | loop-protect |                 |               |     |
| switch(config-if)#     |          |              | loop-protect | action          | tx-disable    |     |
| switch(config-if)#     |          |              | exit         |                 |               |     |
| switch(config)#        |          | interface    |              | lag 25          |               |     |
| switch(config-lag-if)# |          |              | loop-protect |                 |               |     |
| switch(config-if)#     |          |              | loop-protect | action          | tx-rx-disable |     |
| switch(config-if)#     |          |              | loop-protect | vlan            | 100-125,200   |     |
| switch(config-if)#     |          |              | exit         |                 |               |     |
| switch(config)#        |          | loop-protect |              | re-enable-timer |               | 30  |
| switch(config)#        |          | exit         |              |                 |               |     |
| switch#                | show     | loop-protect |              |                 |               |     |
| Status and             | Counters |              | - Loop       | Protection      | Information   |     |
| Transmit               | Interval |              |              | : 30            | (sec)         |     |
| Port Re-enable         |          | Timer        |              | : 10            | (sec)         |     |
| Interface              | 1/1/1    |              |              |                 |               |     |
| Loop-protect           |          | enabled      |              | : Yes           |               |     |
| Loop-Protect           |          | enabled      | VLANs        | :               |               |     |
| Action                 | on loop  | detection    |              | : TX            | disable       |     |
| Loop detected          |          | count        |              | : 0             |               |     |
| Loop detected          |          |              |              | : No            |               |     |
| Interface              | status   |              |              | : up            |               |     |
| Interface              | lag      | 25           |              |                 |               |     |
| Loop-protect           |          | enabled      |              | : Yes           |               |     |
| Loop-Protect           |          | enabled      | VLANs        | : 100-125,200   |               |     |
| Action                 | on loop  | detection    |              | : TX-RX         | disable       |     |
| Loop detected          |          | count        |              | : 0             |               |     |
| Loop detected          |          |              |              | : No            |               |     |
| Interface              | status   |              |              | : up            |               |     |
| Loop protect           |          | commands     |              |                 |               |     |
loop-protect
Syntax
loop-protect
no loop-protect
Description
Enablesloopprotectiononalayer2interfaceorLAG.Loopprotectionpacketsaresent/receivedontheLAG
andnottheinterfacewhicharemembersoftheLAG.Loopprotectiononlyworksonlayer2interfaces.Ifa
layer2interfaceischangedtoalayer3interface,allloopprotectionconfigurationsettingsarelostforthat
interface.
Thenoformofthiscommanddisablesloopprotectiononalayer2interfaceorLAG.
Commandcontext
config-if
config-lag-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 50

Examples

On the 6400 Switch Series, interface identification differs.

Enabling loop protection on interface 1/1/1:

switch# config
switch(config)# interface 1/1/1
switch(config-if)# loop-protect

Enabling loop protection on LAG 25:

switch# config
switch(config)# interface lag 25
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

tx-disable

The port that transmitted the loop detection packet is disabled. When this setting is enabled,
environments with N loops, must have loop protection be configured on at least N-1 ports to have a
loop free topology. Default.

tx-rx-disable

The ports that transmitted and received the loop detection packet are disabled.

Authority

Administrators or local user group members with execution rights for this command.

Example

switch(config-if)# loop-protect action do-not-disable
switch(config-if)# no loop-protect action do-not-disable

loop-protect re-enable-timer

Loop protection | 51

Syntax
| loop-protect    | re-enable-timer |                 | <TIME> |        |     |
| --------------- | --------------- | --------------- | ------ | ------ | --- |
| no loop-protect |                 | re-enable-timer |        | <TIME> |     |
Description
Configuresthetimeintervalafterwhichaninterfacedisabledbyloopprotectionisre-enabled.Theloop
protectiontimerisdisabledbydefault.
Thenoformofthiscommanddisablestheloopprotecttimer.
Commandcontext
config
Parameters
<TIME>
Specifythenumberofsecondsafterwhichadisabledinterfaceisre-enabled.Range:15to604800.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
| switch#         | config |                   |     |                 |     |
| --------------- | ------ | ----------------- | --- | --------------- | --- |
| switch(config)# |        | loop-protect      |     | re-enable-timer | 60  |
| loop-protect    |        | transmit-interval |     |                 |     |
Syntax
| loop-protect    | transmit-interval |                   |     | <TIME>   |     |
| --------------- | ----------------- | ----------------- | --- | -------- | --- |
| no loop-protect |                   | transmit-interval |     | [<TIME>] |     |
Description
Configuresthetimeintervalbetweensuccessiveloopprotectpacketssentonaninterface.
Thenoformofthiscommandsetsthetimeintervaltothedefaultvalueof5seconds.
Commandcontext
config
Parameters
<TIME>
Configuresthetransmitintervalinseconds.Range:5to10.Default:5.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
| switch(config)# |     | loop-protect    |     | transmit-interval | 10  |
| --------------- | --- | --------------- | --- | ----------------- | --- |
| switch(config)# |     | no loop-protect |     | transmit-interval |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 52

| loop-protect | trap | loop-detected |
| ------------ | ---- | ------------- |
Syntax
| loop-protect    | trap loop-detected |     |
| --------------- | ------------------ | --- |
| no loop-protect | trap loop-detected |     |
Description
EnablessendingSNMPtrapsforloop-protectrelatedevents.
ThenoformofthiscommanddisablessendingSNMPtrapsforloop-protectrelatedevents.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingthesendingofSNMPtraps:
| switch# | loop-protect | trap loop-detected |
| ------- | ------------ | ------------------ |
DisablingthesendingofSNMPtraps:
| switch#      | no loop-protect | trap loop-detected |
| ------------ | --------------- | ------------------ |
| loop-protect | vlan            |                    |
Syntax
| loop-protect    | vlan <VLAN-LIST> |     |
| --------------- | ---------------- | --- |
| no loop-protect | vlan             |     |
Description
SpecifiesthetrunkallowedVLANsonwhichloopprotectionpacketsaresent.Bydefault,loopprotection
packetsareonlysentonaccessVLANsandnativeVLANsonaport.Tosendloopprotectionpacketson
trunkallowedVLANs,theVLANsmustbeexplicitlyaddedusingthiscommand.
Loopprotectioncanbeconfiguredonamaximumof4094VLANsacrossallinterfaces.
ThenoformofthiscommandremovesloopprotectionfromallVLANsontheinterface.
Commandcontext
config-if
Parameters
<VLAN-LIST>
SpecifiesthenumberofasingleVLAN,oraseriesofnumbersforarangeofVLANs,separatedby
commas(1,2,3,4),dashes(1-4),orboth(1-4,6).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Loopprotection|53

Example
|      | switch(config-if)# |     | loop-protect |     | vlan 2-6,10,15-20 |
| ---- | ------------------ | --- | ------------ | --- | ----------------- |
| show | loop-protect       |     |              |     |                   |
Syntax
| show | loop-protect |     | [<INTERFACE-NAME>] |     | [vsx-peer] |
| ---- | ------------ | --- | ------------------ | --- | ---------- |
Description
Showsloopprotectioninformationforallinterfacesorforaspecificinterface.
Commandcontext
Operator(>)orManager(#)
Parameters
<INTERFACE-NAME>
Specifiesthenameofalogicalinterfaceontheswitch.Thiscanbeoneofthefollowing:
n AnEthernetinterfaceassociatedwithaphysicalport.Format:member/slot/port.
ALAG(linkaggregationgroup).SpecifytheIDofLAG.Forexample:lag100.
n
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
|     | switch# show   | loop-protect |               |     |            |
| --- | -------------- | ------------ | ------------- | --- | ---------- |
|     | Transmit       | Interval     | (sec)         |     | : 5        |
|     | Port Re-enable |              | Timer (sec)   |     | : Disabled |
|     | Loop Detected  | Trap         |               |     | : Enabled  |
|     | Interface      | 1/1/1        |               |     |            |
|     | Loop-protect   |              | enabled       | :   | Yes        |
|     | Loop-Protect   |              | enabled VLANs | :   |            |
|     | Action         | on loop      | detection     | :   | TX disable |
|     | Loop detected  |              | count         | :   | 0          |
|     | Loop detected  |              |               | :   | No         |
|     | Interface      | status       |               | :   | up         |
|     | Interface      | 1/1/2        |               |     |            |
|     | Loop-protect   |              | enabled       | :   | Yes        |
|     | Loop-Protect   |              | enabled VLANs | :   |            |
|     | Action         | on loop      | detection     | :   | TX disable |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 54

| Loop detected  |          | count        |        | : 0        |             |
| -------------- | -------- | ------------ | ------ | ---------- | ----------- |
| Loop detected  |          |              |        | : No       |             |
| Interface      | status   |              |        | : up       |             |
| switch#        | show     | loop-protect | 1/1/3  |            |             |
| Status and     | Counters |              | - Loop | Protection | Information |
| Transmit       | Interval | (sec)        |        | : 5        |             |
| Port Re-enable |          | Timer        | (sec)  | : 0        |             |
| Loop Detected  |          | Trap         |        | : Disabled |             |
| Interface      | 1        |              |        |            |             |
| Loop-protect   |          | enabled      |        | : Yes      |             |
| Loop-Protect   |          | enabled      | VLANs  | :          |             |
| Action         | on loop  | detection    |        | : TX       | disable     |
| Loop detected  |          | count        |        | : 0        |             |
| Loop detected  |          |              |        | : No       |             |
| Interface      | status   |              |        | : up       |             |
Loopprotection|55

Chapter 6

Spanning tree protocols

Spanning tree protocols

Spanning tree protocols eliminate loops in a physical link-redundant network by selectively blocking
redundant links and putting them in a standby state.

Recent versions of STP include the Rapid Per-VLAN Spanning Tree Protocol (RPVST+) and the Multiple
Spanning Tree Protocol (MSTP).

Comparing spanning tree options
Without spanning tree, having more than one active path between a pair of network devices causes loops in
the network that can result in duplication of messages, leading to a broadcast storm that can bring down the
network.

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

n Determine the spanning tree protocol to be used: RPVST+ or MSTP. RPVST+ is ideal in networks having

fewer than 100 VLANs. In networks having 100 or more VLANs, MSTP is the recommended spanning tree
choice due to the increased load on the switch CPU.

n Plan the device roles (the root bridge or leaf node) by adjusting instance priority.

When you configure spanning tree protocols, follow these guidelines:

n If MSTP is enabled on the switch, MSTP takes all MSTI information along with the packet. To advertise a
specific VLAN within the network through MSTP, make sure that the VLAN is mapped to an MSTI when
you configure the VLAN-to-instance table.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

56

n STP is mutually exclusive with loop protection. If STP and loop protection are both enabled on the same

VLAN, STP takes precedence. This means that loop protection does not take any action on a port blocked
by STP.

n A switch running RPVST+ transmits IEEE spanning tree BPDUs. It interoperates with IEEE RSTP and MSTP
spanning tree regions, and opens or blocks links from these regions as needed to maintain a loop-free
topology with one physical path between regions. RPVST+ interoperates with RSTP and MSTP on rpvst-
mstp-interconnect-vlan. RPVST MSTP Interconnect vlan is configurable, and the default value is 1.

n One spanning tree variant can be run on the switch at any given time. On a switch running RPVST+, MSTP
cannot be enabled. However, any MSTP-specific configuration settings in the startup configuration file
will be maintained.

n The following features cannot run concurrently with RPVST+:

o Multiple VLAN Registration Protocol (MVRP).

o Filter multicast in RPVST+ mode (The multicast MAC address value cannot be set to the PVST MAC

address 01:00:0c:cc:cc:cd.)

n Spanning tree mode cannot be set to RPVST+ when MVRP is enabled. MVRP cannot be enabled when

RPVST+ is enabled.

n Configurations made on an aggregation member port can take effect only after the port is removed from

the aggregation group.

n After you enable a spanning tree protocol on a layer 2 aggregate interface, the system performs

spanning tree calculation on the layer 2 aggregate interface. It does not perform the spanning tree
calculation on the aggregation member ports. The spanning tree protocol enable state and forwarding
state of each selected member port is consistent with the state of the corresponding layer 2 aggregate
interface.

n The member ports of an aggregation group do not participate in spanning tree calculations. However,

the ports reserve their spanning tree configurations for participation in spanning tree calculations after
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

STP uses the following types of BPDUs:

n Configuration BPDUs: Used by the network devices to calculate a spanning tree and maintain the

spanning tree topology.

n Topology change notification (TCN) BPDUs: Use to notify network devices of network topology changes.

Spanning tree protocols | 57

Configuration BPDUs contain sufficient information for network devices to complete spanning tree
calculation. Important fields in a configuration BPDU include the following:

n Root bridge ID: Priority and MAC address of the root bridge.

n Root path cost: Cost of the path to the root bridge indicated by the root identifier from the transmitting

bridge.

n Designated bridge ID: Priority and MAC address of the designated bridge.

n Designated port ID: Priority and global port number of the designated port.

n Message age: Age of the configuration BPDU while it propagates in the network.

n Max age: Maximum age of the configuration BPDU stored on the switch.

n Hello time: Configuration BPDU transmission interval.

n Forward delay: Delay that STP bridges use to transit port state.

STP key concepts

The following sections describe key concepts for using STP

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

n For a device: Device directly connected with the local device and responsible for forwarding BPDUs to the

local device.

n For a LAN: Device responsible for forwarding BPDUs to this LAN segment.

The designated port:

n For a device: Port through which the designated bridge forwards BPDUs to this device.

n For a LAN: Port through which the designated bridge forwards BPDUs to this LAN segment.

In the following topology, Device B and Device C are directly connected to a LAN.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

58

If Device A forwards BPDUs to Device B through port A1, the designated bridge and designated port are as
follows:

n The designated bridge for Device B is Device A.

n The designated port of Device B is port A1 on Device A.

If Device B forwards BPDUs to the LAN, the designated bridge and designated port are as follows:

n The designated bridge for the LAN is Device B.

n The designated port for the LAN is port B2 on Device B.

Path cost

Path cost is a reference value used for link selection in STP. To prune the network into a loop-free tree, STP
calculates path costs to select the most robust links and block redundant links that are less robust.

STP timers

The most important timing parameters in STP calculation are forward delay, hello time, and max age.

n Forward delay: Forward delay is the delay time for port state transition. A path failure can cause

spanning tree recalculation to adapt the spanning tree structure to the change. However, the resulting
new configuration BPDU cannot propagate throughout the network immediately. If the newly elected
root ports and designated ports start to forward data immediately, a temporary loop will likely occur. The
newly elected root ports or designated ports require twice the forward delay time before they transit to
the forwarding state. This allows the new configuration BPDU to propagate throughout the network.

n Hello time: The device sends hello packets at the hello time interval to the neighboring devices to make

sure the paths are fault-free.

n Max age: The device uses the max age to determine whether a stored configuration BPDU has expired

and discards it if the max age is exceeded.

BPDU forwarding mechanism

The configuration BPDUs of STP are forwarded according to these guidelines:

Spanning tree protocols | 59

n Upon network initiation, every device regards itself as the root bridge and generates configuration
BPDUs with itself as the root. Then it sends the configuration BPDUs at a regular hello interval.

n If the root port received a configuration BPDU superior to the configuration BPDU of the port, the

device performs the following tasks:

o Increases the message age carried in the configuration BPDU.

o Starts a timer to time the configuration BPDU.

o Sends this configuration BPDU through the designated port.

n If a designated port receives a configuration BPDU with a lower priority than its configuration BPDU, the

port immediately responds with its configuration BPDU.

n If a path fails, the root port on this path no longer receives new configuration BPDUs and the old

configuration BPDUs will be discarded due to timeout. The device generates a configuration BPDU with
itself as the root and sends the BPDUs and TCN BPDUs. This triggers a new spanning tree calculation
process to establish a new path to restore the network connectivity.

However, the newly calculated configuration BPDU cannot be propagated throughout the network
immediately. As a result, the old root ports and designated ports that have not detected the topology
change continue forwarding data along the old path. If the new root ports and designated ports begin to
forward data as soon as they are elected, a temporary loop might occur.

STP calculation

This section give an overview and example of a simple STP calculation.

Simplified calculation overview

A tree-shape topology forms once the root bridge, root ports, and designated ports are selected.

1. Upon initialization of a device, each port generates a BPDU with the following contents:

n The port as the designated port.

n The device as the root bridge.

n 0 as the root path cost.

n The device ID as the designated bridge ID.

2.

Initially, each STP-enabled device on the network assumes itself to be the root bridge, with its own
device ID as the root bridge ID. By exchanging configuration BPDUs, the devices compare their root
bridge IDs to elect the device with the smallest root bridge ID as the root bridge.

3. Root port and designated ports selection on the non-root bridges.

n A non-root–bridge device regards the port on which it received the optimum configuration BPDU

as the root port.

o Upon receiving a configuration BPDU on a port, the device compares the priority of the

received configuration BPDU with that of the configuration BPDU generated by the port. If the
former priority is lower, the device discards the received configuration BPDU and keeps the
configuration BPDU the port generated. If the former priority is higher, the device replaces the
content of the configuration BPDU generated by the port with the content of the received
configuration BPDU.

o The device compares the configuration BPDUs of all the ports and chooses the optimum

configuration BPDU.

n Based on the configuration BPDU and the path cost of the root port, the device calculates a

designated port configuration BPDU for each of the other ports.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

60

o The root bridge ID is replaced with that of the configuration BPDU of the root port.

o The root path cost is replaced with that of the configuration BPDU of the root port plus the

path cost of the root port.

o The designated bridge ID is replaced with the ID of this device.

o The designated port ID is replaced with the ID of this port.

n The device compares the calculated configuration BPDU with the configuration BPDU on the port

whose port role will be determined, and acts depending on the result of the comparison:

o If the calculated configuration BPDU is superior, the device performs the following tasks:

l Considers this port as the designated port.

l Replaces the configuration BPDU on the port with the calculated configuration BPDU.

l Periodically sends the calculated configuration BPDU.

o If the configuration BPDU on the port is superior, the device blocks this port without updating

its configuration BPDU. The blocked port can receive BPDUs, but cannot send BPDUs or
forward data traffic.

When the network topology is stable, only the root port and designated ports forward user traffic.
Other ports are all in the blocked state to receive BPDUs but not to forward BPDUs or user traffic.

4. The principles of configuration BPDU comparison:

n The configuration BPDU with the lowest root bridge ID has the highest priority.

n If configuration BPDUs have the same root bridge ID, their root path costs are compared. For

example, the root path cost in a configuration BPDU plus the path cost of a receiving port is S. The
configuration BPDU with the smallest S value has the highest priority.

n If all configuration BPDUs have the same root bridge ID and S value, the following attributes are

compared in sequence: Designated bridge IDs, Designated port IDs, and IDs of the receiving ports.

The configuration BPDU that contains a smaller designated bridge ID, designated port ID, or receiving
port ID is selected.

Calculation example

The following topology is used to illustrate an STP calculation. The priority values of Device A, Device B, and
Device C are 0, 1, and 2, respectively. The path costs of links among the three devices are 5, 10, and 4.

Each configuration BPDU contains the following fields: root bridge ID, root path cost, designated bridge ID,
and designated port ID.

Spanning tree protocols | 61

1. TheinitialstateoftheBPDUsoneachdeviceis:
| Device  |     | Port name | Configuration  | BPDUon the | port |
| ------- | --- | --------- | -------------- | ---------- | ---- |
| DeviceA |     | PortA1    | {0,0,0,PortA1} |            |      |
|         |     | PortA2    | {0,0,0,PortA2} |            |      |
| DeviceB |     | PortB1    | {1,0,1,PortB1} |            |      |
|         |     | PortB2    | {1,0,1,PortB2} |            |      |
| DeviceC |     | PortC1    | {2,0,2,PortC1} |            |      |
|         |     | PortC2    | {2,0,2,PortC2} |            |      |
2. BPDUcomparisononeachdeviceoccursasfollows:
|        |            |         | Configuration | BPDUon |     |
| ------ | ---------- | ------- | ------------- | ------ | --- |
| Device | Comparison | process |               |        |     |
ports aftercomparison
| DeviceA | PortA1performsthefollowingtasks: |     |     |     |     |
| ------- | -------------------------------- | --- | --- | --- | --- |
n PortA1:{0,0,0,PortA1}
1. ReceivestheconfigurationBPDUofPortB1{1, PortA2:{0,0,0,PortA2}
n
0,1,PortB1}.
2. Determinesthatitsexistingconfiguration
BPDU{0,0,0,PortA1}issuperiortothe
receivedconfigurationBPDU.
3. Discardsthereceivedone.
PortA2performsthefollowingtasks:
1. ReceivestheconfigurationBPDUofPortC1{2,
0,2,PortC1}.
2. Determinesthatitsexistingconfiguration
BPDU{0,0,0,PortA2}issuperiortothe
receivedconfigurationBPDU.
3. Discardsthereceivedone.
DeviceAdeterminesthatitisboththerootbridge
anddesignatedbridgeintheconfigurationBPDUs
ofallitsports.Itconsidersitselfastherootbridge.
ItdoesnotchangetheconfigurationBPDUofany
portandstartstoperiodicallysendconfiguration
BPDUs.
| DeviceB | PortB1performsthefollowingtasks: |     |     |     |     |
| ------- | -------------------------------- | --- | --- | --- | --- |
n PortB1:{0,0,0,PortA1}
1. ReceivestheconfigurationBPDUofPortA1{0, PortB2:{1,0,1,PortB2}
n
0,0,PortA1}.
2. Determinesthatthereceivedconfiguration
BPDUissuperiortoitsexistingconfiguration
BPDU{1,0,1,PortB1}.
3. UpdatesitsconfigurationBPDU.
PortB2performsthefollowingtasks:
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 62

Device

Comparison process

Configuration BPDU on
ports after comparison

1. Receives the configuration BPDU of Port C2 {2,

0, 2, Port C2}.

2. Determines that its existing configuration

BPDU {1, 0, 1,Port B2} is superior to the

received configuration BPDU.

3. Discards the received BPDU.

Device B performs the following tasks:

n Root port (Port B1): {0, 0,

1. Compares the configuration BPDUs of all its

0, Port A1}

ports.

n Designated port (Port B2):

2. Decides that the configuration BPDU of Port

{0, 5, 1, Port B2}

B1 is the optimum.

3. Selects Port B1 as the root port with the

configuration BPDU unchanged.

Based on the configuration BPDU and path cost of
the root port, Device B calculates a designated
port configuration BPDU for Port B2 {0, 5, 1, Port
B2}. Device B compares it with the existing
configuration BPDU of Port B2 {1, 0, 1, Port B2}.
Device B determines that the calculated one is
superior, and determines that Port B2 is the
designated port. It replaces the configuration
BPDU on Port B2 with the calculated one, and
periodically sends the calculated configuration
BPDU.

Device C

Port C1 performs the following tasks:

1. Receives the configuration BPDU of Port A2 {0,

0, 0, Port A2}.

2. Determines that the received configuration

BPDU is superior to its existing configuration

BPDU {2, 0, 2, Port C1}.

3. Updates its configuration BPDU.
Port C2 performs the following tasks:

1. Receives the original configuration BPDU of

Port B2 {1, 0,1, Port B2}.

2. Determines that the received configuration

BPDU is superior to the existing configuration

BPDU {2, 0, 2, Port C2}.

3. Updates its configuration BPDU.

n Port C1: {0, 0, 0, Port A2}
n Port C2: {1, 0, 1, Port B2}

Device C performs the following tasks:

n Root port (Port C1): {0, 0,

1. Compares the configuration BPDUs of all its

0, Port A2}

ports.

2. Decides that the configuration BPDU of Port

C1 is the optimum.

n Designated port (Port C2):

{0, 10, 2, Port C2}

Spanning tree protocols | 63

Device

Comparison process

Configuration BPDU on
ports after comparison

3. Selects Port C1 as the root port with the

configuration BPDU unchanged.

Based on the configuration BPDU and path cost of
the root port, Device C calculates the configuration
BPDU of Port C2 {0, 10, 2, Port C2}. Device C
compares it with the existing configuration BPDU
of Port C2 {1, 0, 1, Port B2}.
Device C determines that the calculated
configuration BPDU is superior to the existing one,
selects Port C2 as the designated port, and
replaces the configuration BPDU of Port C2 with
the calculated one.

Port C2 performs the following tasks:

1. Receives the configuration BPDU of Port B2 {0,

n Port C1: {0, 0, 0, Port A2}
n Port C2: {0, 5, 1, Port B2}

5, 1, Port B2}.

2. Determines that the received configuration

BPDU is superior to its existing configuration

BPDU {0, 10, 2, Port C2}.

3. Updates its configuration BPDU.
Port C1 performs the following tasks:

1. Receives a periodic configuration BPDU {0, 0,

0, Port A2} from Port A2.

2. Determines that it is the same as the existing

configuration BPDU.

3. Discards the received BPDU.

Device C determines that the root path cost of Port
C1 (10) (root path cost of the received
configuration BPDU (0) plus path cost of Port C1
(10)) is larger than that of Port C2 (9) (root path
cost of the received configuration BPDU (5) plus
path cost of Port C2 (4)). Device C determines that
the configuration BPDU of Port C2 is the optimum,
and selects Port C2 as the root port with the
configuration BPDU unchanged.
Based on the configuration BPDU and path cost of
the root port, Device C performs the following
tasks:

1. Calculates a designated port configuration

BPDU for Port C1 {0, 9, 2, Port C1}.

2. Compares it with the existing configuration

BPDU of Port C1 {0, 0, 0, Port A2}.

3. Determines that the existing configuration

BPDU is superior to the calculated one and

blocks Port C1 with the configuration BPDU

unchanged.

n Blocked port (Port C1): {0,

0, 0, Port A2}

n Root port (Port C2): {0, 5,

1, Port B2}

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

64

Device

Comparison process

Configuration BPDU on
ports after comparison

Port C1 does not forward data until a new event
triggers a spanning tree calculation process: for
example, the link between Device B and Device C
is down.

3. After the comparison, a spanning tree with Device A as the root bridge is established as shown:

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

Spanning tree protocols | 65

There will not be any traffic through the link between switch “B” and switch “D” and therefore the link
bandwidth is wasted. On the other hand, RPVST+ runs different spanning trees for different VLANs.

RVPST+ creates a spanning tree for VLAN 10.

RVPST+ creates another spanning tree for VLAN 20.

The two topologies above are the same as the first topology, but now the switches run RPVST+ and can span
different trees for different VLANs. Switch A is the root switch for the VLAN 10 spanning tree and switch D is
the root switch for the VLAN 20 spanning tree. The link between switch B and switch D is only blocked for
VLAN 10 traffic but VLAN 20 traffic goes through that link. Similarly the link between switch A and switch C is
blocked only for VLAN 20 traffic but VLAN 10 traffic goes through that link. Here, traffic passes through all
the available links, and network availability and bandwidth utilization increase.

The following figure shows a further example of shared links and redundant path-blocking in a network
running RPVST+.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

66

In the factory default configuration, spanning tree operation is enabled on access devices with MSTP
operation. Configuring the spanning tree mode as RPVST+ on a switch and then enabling spanning tree
automatically creates a spanning tree instance for each VLAN on the switch. Configuration with default
settings is automatic, and in many cases does not require any adjustments. This includes operation with
spanning tree regions in your network running STP, MSTP, or RSTP.

Also, the switch retains its currently configured spanning tree parameter settings when spanning tree is
disabled. Thus, if you disable, then later re-enable spanning tree, the parameter settings will be the same as
before spanning tree was disabled.

RPVST+ interoperates with devices that run legacy IEEE 802.1D STP.

RPVST+ applies one RSTP tree per-VLAN. Each of these RSTP trees can have a different root switch and span
the network through shared or different links.

The switch automatically senses port identity and type, and automatically defines spanning tree parameters for

each type, and parameters that apply across the switch. Although these parameters can be adjusted, HPE

strongly recommends leaving these settings in their default configurations unless the proposed changes have

been supplied by an experienced network administrator who has a strong understanding of RPVST+ operation.

The 6300 switch supports 64 RPVST instances. The 6400 supports 254 RPVST instances.

Configuring RPVST+

Procedure

1. Set RPVST+ as the spanning tree mode with the command spanning-tree mode rpvst.

2. Enable spanning tree with the command spanning-tree.

3. For each layer 2 interface or LAG, configure the list of VLANs that are part of the spanning tree with

the command spanning-tree vlan.

4. Set the cost and priority for each VLAN with the commands spanning-tree vlan cost and

spanning-tree vlan port-priority.

5. For most deployments, the default values for the following settings do not need to be changed. If

your deployment requires different settings, change the default values with the indicated

Spanning tree protocols | 67

commands:
| RPVST+ | setting |     |     |     | Default | value | Commandtochange |     | it  |
| ------ | ------- | --- | --- | --- | ------- | ----- | --------------- | --- | --- |
IncludeVLANIDinspanningtree Enabled. spanning-tree extend-system-id
packets.
BlocklinkswhenVLANmismatchis Disabled. spanning-tree ignore-pvid-
detected.
inconsistency
| STPlinktype. |     |     |     |     | Point-to-point. |     | spanning-tree | link-type |     |
| ------------ | --- | --- | --- | --- | --------------- | --- | ------------- | --------- | --- |
Supportextendedrangeofpathscosts Enabled. spanning-tree pathcost-type
forhigh-speedlinks.
Propagatetopologychangestoother Disabled. spanning-tree tcn-guard
ports.
6. ReviewRPVST+configurationsettingswiththecommandshow spanning tree.
Example
Thisexamplecreatesthefollowingconfiguration:
Setsthespanningtreemodetorpvst.
n
Enablesspanningtree.
n
n DefinesspanningtreesupportforVLANs2-5.
n SetsthepriorityforeachVLAN.
| switch#         | config |               |     |      |            |     |     |     |     |
| --------------- | ------ | ------------- | --- | ---- | ---------- | --- | --- | --- | --- |
| switch(config)# |        | spanning-tree |     | mode | rpvst      |     |     |     |     |
| switch(config)# |        | spanning-tree |     |      |            |     |     |     |     |
| switch(config)# |        | spanning-tree |     | vlan | 2-5        |     |     |     |     |
| switch(config)# |        | spanning-tree |     | vlan | 2 priority | 5   |     |     |     |
switch(config)#
|                  |                    | spanning-tree |       | vlan       | 3 priority | 4   |       |     |     |
| ---------------- | ------------------ | ------------- | ----- | ---------- | ---------- | --- | ----- | --- | --- |
| switch(config)#  |                    | spanning-tree |       | vlan       | 4 priority | 3   |       |     |     |
| switch(config)#  |                    | spanning-tree |       | vlan       | 5 priority | 2   |       |     |     |
| switch(config)#  |                    | exit          |       |            |            |     |       |     |     |
| switch#          | show               | spanning-tree |       |            |            |     |       |     |     |
| Spanning         | tree               | status        |       | : Enabled  | Protocol:  |     | RPVST |     |     |
| Extended         | System-id          |               |       | : Enabled  |            |     |       |     |     |
| Ignore           | PVID Inconsistency |               |       | : Disabled |            |     |       |     |     |
| Path cost        | method             |               |       | : Long     |            |     |       |     |     |
| RPVST-MSTP       | Interconnect       |               | VLAN  | : 1        |            |     |       |     |     |
| RPVST-Configured |                    | VLAN          |       | : all      |            |     |       |     |     |
| RPVST-Enabled    |                    | VLAN          |       | : 1        |            |     |       |     |     |
| Current          | Virtual            | Ports         | Count | : 28       |            |     |       |     |     |
| Maximum          | Allowed            | Virtual       | Ports | : 2048     |            |     |       |     |     |
VLAN1
| Root | ID  | Priority      | : 32768           |             |     |        |             |     |     |
| ---- | --- | ------------- | ----------------- | ----------- | --- | ------ | ----------- | --- | --- |
|      |     | MAC-Address:  | 38:21:c7:5c:df:c0 |             |     |        |             |     |     |
|      |     | Hello time(in |                   | seconds):2  | Max | Age(in | seconds):20 |     |     |
|      |     | Forward       | Delay(in          | seconds):15 |     |        |             |     |     |
VLAN2
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 68

| Root ID   | Priority      | : 20480              |            |             |      |
| --------- | ------------- | -------------------- | ---------- | ----------- | ---- |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | This bridge   | is the root          |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Bridge ID | Priority      | : 20480              |            |             |      |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Port      | Role          | State                | Cost       | Priority    | Type |
------------ -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | ---------- | ----- | --- | -------------- |
VLAN3
| Root ID   | Priority      | : 16384              |            |             |      |
| --------- | ------------- | -------------------- | ---------- | ----------- | ---- |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | This bridge   | is the root          |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Bridge ID | Priority      | : 16384              |            |             |      |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Port      | Role          | State                | Cost       | Priority    | Type |
------------ -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | ---------- | ----- | --- | -------------- |
VLAN4
| Root ID   | Priority      | : 12288              |            |             |      |
| --------- | ------------- | -------------------- | ---------- | ----------- | ---- |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | This bridge   | is the root          |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Bridge ID | Priority      | : 12288              |            |             |      |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Port      | Role          | State                | Cost       | Priority    | Type |
------------ -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | ---------- | ----- | --- | -------------- |
VLAN5
| Root ID   | Priority      | : 8192               |            |             |      |
| --------- | ------------- | -------------------- | ---------- | ----------- | ---- |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | This bridge   | is the root          |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Bridge ID | Priority      | : 8192               |            |             |      |
|           | MAC-Address:  | 70:72:cf:38:21:e5    |            |             |      |
|           | Hello time(in | seconds):2           | Max Age(in | seconds):20 |      |
|           | Forward       | Delay(in seconds):15 |            |             |      |
| Port      | Role          | State                | Cost       | Priority    | Type |
------------ -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | ---------- | ----- | --- | -------------- |
Spanningtreeprotocols|69

| Viewing | RPVST+ | information |
| ------- | ------ | ----------- |
Prerequisites
Thesecommandsareinthemanagercontext,asindicatedbytheswitch#prompt.
Procedure
ToviewvariousaspectsofRPVST+information,usethefollowingcommands.
n Toviewinformationonspanning-treemodeandtheRPVST+instances,use:
| show | spanning-tree |     |
| ---- | ------------- | --- |
n Toviewinformationonspanning-treemodeandtheRPVST+instanceofaspecificVLAN,use:
| show | spanning-tree | vlan |
| ---- | ------------- | ---- |
n Toviewasummaryofthespanning-treeconfigurationsrelatedtoaport,use:
| show | spanning-tree | summary port |
| ---- | ------------- | ------------ |
n Toviewasummaryofthespanning-treeconfigurations,use:
| show   | spanning-tree | summary root |
| ------ | ------------- | ------------ |
| RPVST+ | scenario      |              |
Inthisscenario,fourswitchesareinterconnected.VLANs10and20aredefinedonallswitches,causinga
networkloop.
Toeliminatetheloop,RPVST+isenabledandswitchAandBaredefinedashigh-priorityforVLAN10and20
respectively.RPVST+theneliminatestheloopbyassigningswitchAastherootforVLAN10andswitchB
designatedastherootforVLAN20,andblockingaccessononeofthelinks.
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 70

Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. ConfigureswitchA.
a. CreateVLANs1,10,and20.
switch# config
| switch(config)# | vlan 1, | 10, 20 |     |
| --------------- | ------- | ------ | --- |
b. EnableRPVST+andassigntheVLANs10and20toit.Assignapriorityof5toVLAN10.Thiswill
forceswitchAtobecometherootofthespanningtreeforVLAN10.
| switch(config)# | spanning-tree | mode rpvst       |     |
| --------------- | ------------- | ---------------- | --- |
| switch(config)# | spanning-tree |                  |     |
| switch(config)# | spanning-tree | vlan 10,20       |     |
| switch(config)# | spanning-tree | vlan 10 priority | 5   |
c. Defineinterfaces1/1/1and1/1/2.
| switch(config)#    | interface   | 1/1/1             |     |
| ------------------ | ----------- | ----------------- | --- |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
| switch(config-if)# | interface   | 1/1/2             |     |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
2. ConfigureswitchBandswitchCwiththesamesettings.
a. CreateVLANs1,10,and20.
switch# config
switch(config)#
|     | vlan 1, | 10, 20 |     |
| --- | ------- | ------ | --- |
b. EnableRPVST+andassigntheVLANs10and20toit.
| switch(config)# | spanning-tree | mode rpvst |     |
| --------------- | ------------- | ---------- | --- |
| switch(config)# | spanning-tree |            |     |
| switch(config)# | spanning-tree | vlan 10,20 |     |
c. Defineinterfaces1/1/1and1/1/2.
| switch(config)#    | interface   | 1/1/1             |     |
| ------------------ | ----------- | ----------------- | --- |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
| switch(config-if)# | interface   | 1/1/2             |     |
Spanningtreeprotocols|71

| switch(config-if)# | no shutdown |                   |     |
| ------------------ | ----------- | ----------------- | --- |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
3. ConfigureswitchD.
a. CreateVLANs1,10,and20.
switch# config
| switch(config)# | vlan 1, | 10, 20 |     |
| --------------- | ------- | ------ | --- |
b. EnableRPVST+andassigntheVLANs10and20toit.Assignapriorityof5toVLAN20.Thiswill
forceswitchDtobecometherootofthespanningtreeforVLAN20.
| switch(config)# | spanning-tree | mode rpvst       |     |
| --------------- | ------------- | ---------------- | --- |
| switch(config)# | spanning-tree |                  |     |
| switch(config)# | spanning-tree | vlan 10,20       |     |
| switch(config)# | spanning-tree | vlan 20 priority | 5   |
c. Defineinterfaces1/1/1and1/1/2.
| switch(config)#    | interface   | 1/1/1             |     |
| ------------------ | ----------- | ----------------- | --- |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
| switch(config-if)# | interface   | 1/1/2             |     |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
RPVST+ commands
show spanning-tree
Syntax
| show spanning-tree [detail] | [vsx-peer] |     |     |
| --------------------------- | ---------- | --- | --- |
Description
ShowsthespanningtreemodeandinformationontheRPVSTinstancesandoptionallyshowsdetailsonthe
RPVSTinstances.
Commandcontext
Operator(>)orManager(#)
Parameters
detail
SpecifiesshowingdetailsontheRPVSTinstances.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingspanningtreemodeandRPVSTinstanceinformation:
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 72

| switch#    | show               | spanning-tree |     |      |           |     |           |       |     |     |
| ---------- | ------------------ | ------------- | --- | ---- | --------- | --- | --------- | ----- | --- | --- |
| Spanning   | tree               | status        |     |      | : Enabled |     | Protocol: | RPVST |     |     |
| Extended   | System-id          |               |     |      | : Enabled |     |           |       |     |     |
| Ignore     | PVID Inconsistency |               |     |      | : Enabled |     |           |       |     |     |
| Path cost  | method             |               |     |      | : Long    |     |           |       |     |     |
| RPVST-MSTP | Interconnect       |               |     | VLAN | : 1       |     |           |       |     |     |
VLAN1
| Root   | ID     | Priority     |          | : 32768           |             |     |          |             |         |         |
| ------ | ------ | ------------ | -------- | ----------------- | ----------- | --- | -------- | ----------- | ------- | ------- |
|        |        | MAC-Address: |          | 70:72:cf:31:c9:23 |             |     |          |             |         |         |
|        |        | This         | bridge   | is the            | root        |     |          |             |         |         |
|        |        | Hello        | time(in  | seconds):2        |             | Max | Age(in   | seconds):20 |         |         |
|        |        | Forward      | Delay(in |                   | seconds):15 |     |          |             |         |         |
| Bridge | ID     | Priority     | :        | 32768             |             |     |          |             |         |         |
|        |        | MAC-Address: |          | 70:72:cf:31:c9:23 |             |     |          |             |         |         |
|        |        | Hello        | time(in  | seconds):2        |             | Max | Age(in   | seconds):20 |         |         |
|        |        | Forward      | Delay(in |                   | seconds):15 |     |          |             |         |         |
| PORT   | ROLE   |              | STATE    |                   | COST        |     | PRIORITY | TYPE        | BPDU-Tx | BPDU-Rx |
| TCN-Tx | TCN-Rx |              |          |                   |             |     |          |             |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |        |            |     |       |         |     |          |     |     |
| ------------- | ----------- | ------ | ---------- | --- | ----- | ------- | --- | -------- | --- | --- |
| 1/1/1         | Designated  |        | Forwarding |     | 20000 |         | 128 | P2P Edge | 100 | 60  |
| 20            | 10          |        |            |     |       |         |     |          |     |     |
| 1/1/2         | Designated  |        | Forwarding |     | 20000 |         | 128 | P2P      | 100 | 60  |
| 20            | 10          |        |            |     |       |         |     |          |     |     |
| 1/1/3         | Designated  |        | Forwarding |     | 20000 |         | 128 | Shr      | 100 | 60  |
| 20            | 10          |        |            |     |       |         |     |          |     |     |
| 1/1/4         | Designated  |        | Forwarding |     | 20000 |         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |        |            |     |       |         |     |          |     |     |
| 1/1/5         | Alternate   |        | Loop-Inc   |     | 20000 |         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |        |            |     |       |         |     |          |     |     |
| 1/1/6         | Alternate   |        | Root-Inc   |     | 20000 |         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |        |            |     |       |         |     |          |     |     |
| Number        | of topology |        | changes    |     | : 4   |         |     |          |     |     |
| Last topology |             | change | occurred   |     | : 516 | seconds | ago |          |     |     |
ShowingspanningtreemodeanddetailedRPVSTinstanceinformation:
| switch#    | show               | spanning-tree |       | detail |           |     |           |       |     |     |
| ---------- | ------------------ | ------------- | ----- | ------ | --------- | --- | --------- | ----- | --- | --- |
| Spanning   | tree               | status        |       |        | : Enabled |     | Protocol: | RPVST |     |     |
| Extended   | System-id          |               |       |        | : Enabled |     |           |       |     |     |
| Ignore     | PVID Inconsistency |               |       |        | : Enabled |     |           |       |     |     |
| Path cost  | method             |               |       |        | : Long    |     |           |       |     |     |
| RPVST-MSTP | Interconnect       |               |       | VLAN   | : 1       |     |           |       |     |     |
| Current    | Virtual            | Ports         | Count |        | : 0       |     |           |       |     |     |
| Maximum    | Allowed            | Virtual       |       | Ports  | : 2048    |     |           |       |     |     |
VLAN1
| Root   | ID  | Priority     |          | : 32768           |             |     |        |             |     |     |
| ------ | --- | ------------ | -------- | ----------------- | ----------- | --- | ------ | ----------- | --- | --- |
|        |     | MAC-Address: |          | 70:72:cf:31:c9:23 |             |     |        |             |     |     |
|        |     | This         | bridge   | is the            | root        |     |        |             |     |     |
|        |     | Hello        | time(in  | seconds):2        |             | Max | Age(in | seconds):20 |     |     |
|        |     | Forward      | Delay(in |                   | seconds):15 |     |        |             |     |     |
| Bridge | ID  | Priority     | :        | 32768             |             |     |        |             |     |     |
|        |     | MAC-Address: |          | 70:72:cf:31:c9:23 |             |     |        |             |     |     |
|        |     | Hello        | time(in  | seconds):2        |             | Max | Age(in | seconds):20 |     |     |
|        |     | Forward      | Delay(in |                   | seconds):15 |     |        |             |     |     |
Spanningtreeprotocols|73

| PORT   | ROLE   |     | STATE |     | COST | PRIORITY | TYPE | BPDU-Tx | BPDU-Rx |
| ------ | ------ | --- | ----- | --- | ---- | -------- | ---- | ------- | ------- |
| TCN-Tx | TCN-Rx |     |       |     |      |          |      |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |          |            |     |               |         |     |          |     |
| ------------- | ----------- | -------- | ---------- | --- | ------------- | ------- | --- | -------- | --- |
| 1/1/1         | Designated  |          | Forwarding |     | 20000         | 128     | P2P | Edge 100 | 60  |
| 20            | 10          |          |            |     |               |         |     |          |     |
| 1/1/2         | Designated  |          | Forwarding |     | 20000         | 128     | P2P | 100      | 60  |
| 20            | 10          |          |            |     |               |         |     |          |     |
| 1/1/3         | Designated  |          | Forwarding |     | 20000         | 128     | Shr | 100      | 60  |
| 20            | 10          |          |            |     |               |         |     |          |     |
| 1/1/4         | Designated  |          | Forwarding |     | 20000         | 128     | Shr | Edge 100 | 60  |
| 20            | 10          |          |            |     |               |         |     |          |     |
| 1/1/5         | Alternate   |          | Loop-Inc   |     | 20000         | 128     | Shr | Edge 100 | 60  |
| 20            | 10          |          |            |     |               |         |     |          |     |
| 1/1/6         | Alternate   |          | Root-Inc   |     | 20000         | 128     | Shr | Edge 100 | 60  |
| 20            | 10          |          |            |     |               |         |     |          |     |
| Topology      | change      | flag     | : False    |     |               |         |     |          |     |
| Number        | of topology |          | changes    | : 1 |               |         |     |          |     |
| Last topology |             | change   | occurred   | :   | 33293 seconds | ago     |     |          |     |
| Port 1/1/1    |             |          |            |     |               |         |     |          |     |
| Designated    | Root        | Priority |            |     |               | : 32768 |     | Address: |     |
48:0F:CF:AF:22:1D
| Designated | Bridge |     | Priority |     |     | : 32768 |     | Address: |     |
| ---------- | ------ | --- | -------- | --- | --- | ------- | --- | -------- | --- |
48:0F:CF:AF:22:1D
| Designated       | Port  |             |     |      |     | : 1/1/1 |     |          |     |
| ---------------- | ----- | ----------- | --- | ---- | --- | ------- | --- | -------- | --- |
| Forwarding-State |       | transitions |     |      |     | : 0     |     |          |     |
| BPDUs sent       | 1582, | received    |     | 1506 |     |         |     |          |     |
| TCN_Tx:          | 10,   | TCN_Rx:     | 10  |      |     |         |     |          |     |
| Port lag1        |       |             |     |      |     |         |     |          |     |
| Designated       | Root  | Priority    |     |      |     | : 32768 |     | Address: |     |
48:0F:CF:AF:22:1D
| Designated | Bridge |     | Priority |     |     | : 32768 |     | Address: |     |
| ---------- | ------ | --- | -------- | --- | --- | ------- | --- | -------- | --- |
48:0F:CF:AF:22:1D
| Designated         | Port  |             |                    |      |     | : lag1   |     |     |     |
| ------------------ | ----- | ----------- | ------------------ | ---- | --- | -------- | --- | --- | --- |
| Forwarding-State   |       | transitions |                    |      |     | : 0      |     |     |     |
| BPDUs sent         | 1402, | received    |                    | 1316 |     |          |     |     |     |
| TCN_Tx:            | 10,   | TCN_Rx:     | 10                 |      |     |          |     |     |     |
| Multi-chassis      |       | role        |                    |      |     | : active |     |     |     |
| show spanning-tree |       |             | inconsistent-ports |      |     |          |     |     |     |
Syntax
| show spanning-tree |     | inconsistent-ports |     |     | [vlan | <VLAN-ID>] |     |     |     |
| ------------------ | --- | ------------------ | --- | --- | ----- | ---------- | --- | --- | --- |
Description
ShowsportsblockedbySTPprotectionfunctionssuchasRootguard,Loopguard,BPDUguard,andRPVST
guard.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiesaVLANIDnumber.
Authority
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 74

OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showinginconsistentportinformation:
| switch# show | spanning-tree  | inconsistent-ports |     |
| ------------ | -------------- | ------------------ | --- |
| VLAN ID      | Blocked Port   | Reason             |     |
| ------------ | -------------- | ------------       |     |
| 1            | 1/1/1          | BPDU Guard         |     |
| 2            | 1/1/1          | BPDU Guard         |     |
| 3            | 1/1/1          | BPDU Guard         |     |
| 4            | 1/1/1          | BPDU Guard         |     |
| 5            | 1/1/1          | BPDU Guard         |     |
| 6            | 1/1/1          | BPDU Guard         |     |
| 7            | 1/1/1          | BPDU Guard         |     |
| 8            | 1/1/1          | BPDU Guard         |     |
| 9            | 1/1/1          | BPDU Guard         |     |
| 10           | 1/1/1          | BPDU Guard         |     |
ShowinginconsistentportinformationforVLANs1to4:
| switch# show       | spanning-tree  | inconsistent-ports | vlan 1-4 |
| ------------------ | -------------- | ------------------ | -------- |
| VLAN ID            | Blocked Port   | Reason             |          |
| ------------       | -------------- | ------------       |          |
| 1                  | 1/1/3          | Root Guard         |          |
| 2                  | 1/1/7          | BPDU Guard         |          |
| 3                  | 1/1/9          | Loop Guard         |          |
| 4                  | 1/1/37         | RPVST Guard        |          |
| show spanning-tree | summaryport    |                    |          |
Syntax
| show spanning-tree | summary | port |     |
| ------------------ | ------- | ---- | --- |
Description
Showsasummaryofport-relatedspanning-treeconfigurationandstatus.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingasummaryofport-relatedspanningtreeinformation:
Spanningtreeprotocols|75

| switch#                | show spanning-tree | summary    | port      |                     |     |
| ---------------------- | ------------------ | ---------- | --------- | ------------------- | --- |
| STP status             |                    |            | : Enabled |                     |     |
| Protocol               |                    |            | : RPVST   |                     |     |
| BPDU guard             | Timeout value      |            | : None    |                     |     |
| BPDU guard             | enabled interfaces |            | : None    |                     |     |
| BPDU filter            | enabled            | interfaces | : None    |                     |     |
| Root guard             | enabled interfaces |            | : None    |                     |     |
| Loop guard             | enabled interfaces |            | : None    |                     |     |
| TCN guard              | enabled interfaces |            | : None    |                     |     |
| RPVST filter           | enabled            | interfaces | : None    |                     |     |
| RPVST guard            | enabled            | interfaces | : None    |                     |     |
| Interface              | count by state     |            |           |                     |     |
| VLAN                   |                    | Blocking   | Listening | Learning Forwarding |     |
| ---------------------- |                    | --------   | --------- | -------- ---------- |     |
| VLAN1                  |                    |            | 28        | 0 0                 | 0   |
| VLAN2                  |                    |            | 0         | 0 0                 | 0   |
| VLAN3                  |                    |            | 0         | 0 0                 | 0   |
| VLAN4                  |                    |            | 0         | 0 0                 | 0   |
| VLAN5                  |                    |            | 0         | 0 0                 | 0   |
| VLAN6                  |                    |            | 0         | 0 0                 | 0   |
| VLAN7                  |                    |            | 0         | 0 0                 | 0   |
| VLAN8                  |                    |            | 0         | 0 0                 | 0   |
| VLAN9                  |                    |            | 0         | 0 0                 | 0   |
| VLAN10                 |                    |            | 0         | 0 0                 | 0   |
| ---------------------- |                    | --------   | --------- | -------- ---------- |     |
| Total =                | 10                 |            | 28        | 0 0                 | 0   |
| show spanning-tree     | summaryroot        |            |           |                     |     |
Syntax
| show spanning-tree | summary | root |     |     |     |
| ------------------ | ------- | ---- | --- | --- | --- |
Description
ShowsthesummaryofspanningtreerootandconfigurationsforallVLANs.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingsummaryofspanningtreeconfigurations:
| switch#    | show spanning-tree | summary             | root |     |     |
| ---------- | ------------------ | ------------------- | ---- | --- | --- |
| STP status |                    | : Enabled           |      |     |     |
| Protocol   |                    | : RPVST             |      |     |     |
| System     | ID                 | : f8:60:f0:c9:70:40 |      |     |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 76

| Root bridge | for VLANs     | : 1-10 |     |            |         |      |      |
| ----------- | ------------- | ------ | --- | ---------- | ------- | ---- | ---- |
|             |               |        |     | Root Hello | Max Fwd |      |      |
| VLAN        | Priority Root | ID     |     | cost Time  | Age Dly | Root | Port |
-------- -------- ----------------- --------- ----- --- --- ------------
| VLAN1              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| ------------------ | ----------------------- | --- | --- | --- | ------- | --- | --- |
| VLAN2              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN3              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN4              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN5              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN6              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN7              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN8              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN9              | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| VLAN10             | 32768 f8:60:f0:c9:70:40 |     |     | 0   | 2 20 15 |     | 0   |
| show spanning-tree | vlan                    |     |     |     |         |     |     |
Syntax
| show spanning-tree | vlan | <VLAN-ID> | [detail] | [vsx-peer] |     |     |     |
| ------------------ | ---- | --------- | -------- | ---------- | --- | --- | --- |
Description
DisplaysthespanningtreemodeandinformationontheRPVSTinstanceofthespecifiedVLANand
optionallydisplaysdetailsontheRPVSTinstancefortheVLAN.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiesthenumberofaVLAN.
[detail]
SpecifiesdisplayingdetailsontheRPVSTinstancefortheVLAN.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingspanningtreemodeandRPVSTinstanceinformationforVLAN2:
switch#
| show | spanning-tree |     | vlan 2 |     |     |     |     |
| ---- | ------------- | --- | ------ | --- | --- | --- | --- |
VLAN2
| Spanning | tree status: | Enabled           | Protocol: | RPVST |     |     |     |
| -------- | ------------ | ----------------- | --------- | ----- | --- | --- | --- |
| Root ID  | Priority     | : 32768           |           |       |     |     |     |
|          | MAC-Address: | 70:72:cf:76:43:2a |           |       |     |     |     |
Spanningtreeprotocols|77

|        | This         | bridge is         | the root    |            |             |         |         |
| ------ | ------------ | ----------------- | ----------- | ---------- | ----------- | ------- | ------- |
|        | Hello        | time(in           | seconds):2  | Max Age(in | seconds):20 |         |         |
|        | Forward      | Delay(in          | seconds):15 |            |             |         |         |
| Bridge | ID Priority  | : 32768           |             |            |             |         |         |
|        | MAC-Address: | 70:72:cf:76:43:2a |             |            |             |         |         |
|        | Hello        | time(in           | seconds):2  | Max Age(in | seconds):20 |         |         |
|        | Forward      | Delay(in          | seconds):15 |            |             |         |         |
| PORT   | ROLE         | STATE             | COST        | PRIORITY   | TYPE        | BPDU-Tx | BPDU-Rx |
| TCN-Tx | TCN-Rx       |                   |             |            |             |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |            |       |             |          |     |     |
| ------------- | ----------- | ---------- | ----- | ----------- | -------- | --- | --- |
| 1/1/1         | Designated  | Forwarding | 20000 | 128         | P2P Edge | 100 | 60  |
| 20            | 10          |            |       |             |          |     |     |
| 1/1/2         | Designated  | Forwarding | 20000 | 128         | P2P      | 100 | 60  |
| 20            | 10          |            |       |             |          |     |     |
| 1/1/3         | Designated  | Forwarding | 20000 | 128         | Shr      | 100 | 60  |
| 20            | 10          |            |       |             |          |     |     |
| 1/1/4         | Designated  | Forwarding | 20000 | 128         | Shr Edge | 100 | 60  |
| 20            | 10          |            |       |             |          |     |     |
| 1/1/5         | Alternate   | Loop-Inc   | 20000 | 128         | Shr Edge | 100 | 60  |
| 20            | 10          |            |       |             |          |     |     |
| 1/1/6         | Alternate   | Root-Inc   | 20000 | 128         | Shr Edge | 100 | 60  |
| 20            | 10          |            |       |             |          |     |     |
| Number        | of topology | changes    | : 4   |             |          |     |     |
| Last topology | change      | occurred   | : 516 | seconds ago |          |     |     |
ShowingspanningtreemodeanddetailedRPVSTinstanceinformationforVLAN2:
| switch# | show spanning-tree |     | vlan 2 detail |     |     |     |     |
| ------- | ------------------ | --- | ------------- | --- | --- | --- | --- |
VLAN2
| Spanning | tree status: | Enabled           | Protocol:   | RPVST      |             |         |         |
| -------- | ------------ | ----------------- | ----------- | ---------- | ----------- | ------- | ------- |
| Root     | ID Priority  | : 32768           |             |            |             |         |         |
|          | MAC-Address: | 70:72:cf:76:43:2a |             |            |             |         |         |
|          | This         | bridge is         | the root    |            |             |         |         |
|          | Hello        | time(in           | seconds):2  | Max Age(in | seconds):20 |         |         |
|          | Forward      | Delay(in          | seconds):15 |            |             |         |         |
| Bridge   | ID Priority  | : 32768           |             |            |             |         |         |
|          | MAC-Address: | 70:72:cf:76:43:2a |             |            |             |         |         |
|          | Hello        | time(in           | seconds):2  | Max Age(in | seconds):20 |         |         |
|          | Forward      | Delay(in          | seconds):15 |            |             |         |         |
| PORT     | ROLE         | STATE             | COST        | PRIORITY   | TYPE        | BPDU-Tx | BPDU-Rx |
| TCN-Tx   | TCN-Rx       |                   |             |            |             |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ---------- | ---------- |            |       |     |          |     |     |
| ---------- | ---------- | ---------- | ----- | --- | -------- | --- | --- |
| 1/1/1      | Designated | Forwarding | 20000 | 128 | P2P Edge | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/2      | Designated | Forwarding | 20000 | 128 | P2P      | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/3      | Designated | Forwarding | 20000 | 128 | Shr      | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/4      | Designated | Forwarding | 20000 | 128 | Shr Edge | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/5      | Alternate  | Loop-Inc   | 20000 | 128 | Shr Edge | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/6      | Alternate  | Root-Inc   | 20000 | 128 | Shr Edge | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 78

| Topology      | change            | flag     | : False      |            |         |          |                   |
| ------------- | ----------------- | -------- | ------------ | ---------- | ------- | -------- | ----------------- |
| Number        | of topology       |          | changes      | : 1        |         |          |                   |
| Last topology |                   | change   | occurred     |            | : 33293 | seconds  | ago               |
| Port 1/1/1    |                   |          |              |            |         |          |                   |
| Designated    | root              | has      | priority     | :32768     |         | Address: | 48:0f:cf:af:22:1d |
| Designated    | bridge            |          | has priority |            | :32768  | Address: | 48:0f:cf:af:22:1d |
| Designated    | port              | :1       |              |            |         |          |                   |
| Number        | of transitions    |          | to           | forwarding |         | state    | : 0               |
| BPDUs sent    | 1582,             | received |              | 1506       |         |          |                   |
| TCN_Tx:       | 10, TCN_Rx:       |          | 10           |            |         |          |                   |
| spanning-tree | bpdu-guardtimeout |          |              |            |         |          |                   |
Syntax
| spanning-tree    | bpdu-guard |            | timeout |         | <INTERVAL> |     |     |
| ---------------- | ---------- | ---------- | ------- | ------- | ---------- | --- | --- |
| no spanning-tree |            | bpdu-guard |         | timeout |            |     |     |
Description
Enablesandconfigurestheautore-enabletimeoutinsecondsforallinterfaceswithBPDUguardenabled.
WhenaninterfaceisdisabledafterreceivinganunauthorizedBPDUitwillautomaticallybere-enabledafter
thetimeoutexpires.Thedefaultisfortheinterfacetostaydisableduntilmanuallyre-enabled.
ThenoformofthecommanddisablesBPDUguardtimeoutontheinterface.Thisisthedefault.
Commandcontext
config
Parameters
<INTERVAL>
Specifiesthere-enabletimeoutinseconds.Range:1to65535.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingtheBPDUguardtimeoutoninterface1/1/1:
| switch(config)#    |     | interface |               | 1/1/1 |            |     |            |
| ------------------ | --- | --------- | ------------- | ----- | ---------- | --- | ---------- |
| switch(config-if)# |     |           | spanning-tree |       | bpdu-guard |     | timeout 10 |
DisablingBPDUguardtimeoutoninterface1/1/1:
| switch(config)#    |                  | interface |                  | 1/1/1 |     |            |     |
| ------------------ | ---------------- | --------- | ---------------- | ----- | --- | ---------- | --- |
| switch(config-if)# |                  |           | no spanning-tree |       |     | bpdu-guard |     |
| spanning-tree      | extend-system-id |           |                  |       |     |            |     |
Syntax
Spanningtreeprotocols|79

| spanning-tree    | extend-system-id | {enable | | disable} |     |
| ---------------- | ---------------- | ------- | ---------- | --- |
| no spanning-tree | extend-system-id |         |            |     |
Description
ConfiguresuseofextendedsystemID.Whenenabled,theVLANIDisincludedinspanningtreepackets.
Whendisabled,theVLANIDissettoNULLinthespanningtreepackets.
Bydefault,extendedsystemIDisenabled.IfyoudisableextendedsystemID,thebridgeidentifierfieldin
thespanningtreepacketisfilledwithzeros.
ThenoformofthiscommanddisablesextendedsystemID.
Commandcontext
config
Parameters
enable
SpecifiesenablinguseofextendedsystemID.
disable
SpecifiesdisablinguseofextendedsystemID.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingextendedsystemID:
| switch#         | config        |                  |     |        |
| --------------- | ------------- | ---------------- | --- | ------ |
| switch(config)# | spanning-tree | extend-system-id |     | enable |
DisablingextendedsystemID:
| switch#         | config                    |                  |     |         |
| --------------- | ------------------------- | ---------------- | --- | ------- |
| switch(config)# | spanning-tree             | extend-system-id |     | disable |
| switch(config)# | no spanning-tree          | extend-system-id |     |         |
| spanning-tree   | ignore-pvid-inconsistency |                  |     |         |
Syntax
| spanning-tree    | ignore-pvid-inconsistency |     | {enable | | disable} |
| ---------------- | ------------------------- | --- | ------- | ---------- |
| no spanning-tree | ignore-pvid-inconsistency |     |         |            |
Description
Configuresportbehaviorwhenper-VLANIDinconsistenciesarepresent.Forexample,whentheportson
bothendsofapoint-to-pointlinkareuntaggedmembersofdifferentVLANs,enablingthisoptionallows
RPVST+toprocessuntaggedRPVST+packetsbelongingtothepeer’suntaggedVLANasiftheywere
receivedonthecurrentdevice’suntaggedVLAN.Whenthisoptionisdisabled,RPVST+blocksthelink,
causingtrafficonthemismatchedVLANstobedropped.
Ifthisoptionisenabledonmultipleswitchesconnectedbyhubs,therecouldbemorethantwoVLANs
involvedinPVIDmismatchesthatwillbeignoredbyRPVST+.
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 80

IfportVLANmembershipsismisconfiguredonaswitchinthenetwork,thenenablingthisoptionprevents
RPVST+fromdetectingtheproblem,whichmayresultinpacketduplicationinthenetworksinceRPVST+
wouldnotconvergecorrectly.
ThiscommandaffectsallportsontheswitchbelongingtoVLANsonwhichRPVST+isenabled.
Bydefaultignoreper-VLANIDinconsistencyisdisabled.
Thenoformofthiscommandsetstheignoreper-VLANIDinconsistenciestodisabled.
Commandcontext
config
Parameters
enable
Specifiesignoreper-VLANIDinconsistenciesandallowRPVSTtorunonmismatchedlinks.
disable
Disablestheignoreper-VLANIDinconsistenciesfunctionality.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingignoreper-VLANIDinconsistencies:
| switch#         | config        |     |                           |        |
| --------------- | ------------- | --- | ------------------------- | ------ |
| switch(config)# | spanning-tree |     | ignore-pvid-inconsistency | enable |
Disablingignoreper-VLANIDinconsistencies:
| switch#         | config        |               |                           |         |
| --------------- | ------------- | ------------- | ------------------------- | ------- |
| switch(config)# | spanning-tree |               | ignore-pvid-inconsistency | disable |
| switch(config)# | no            | spanning-tree | ignore-pvid-inconsistency |         |
| spanning-tree   | link-type     |               |                           |         |
Syntax
| spanning-tree    | link-type | {point-to-point | | shared} |     |
| ---------------- | --------- | --------------- | --------- | --- |
| no spanning-tree | link-type |                 |           |     |
Description
Configuresthelinktypeofaport.
Thenoformofthiscommandsetsthespanningtreelinktypetothedefaultvalueofpoint-to-point.
Commandcontext
config-if
Parameters
point-to-point
Setsthespanningtreelinktypeaspoint-to-point.Usethisforfull-duplexportsthatprovideapoint-to-
pointlinktodevicessuchasaswitch,bridge,orend-node.Default.
shared
Spanningtreeprotocols|81

Setsthespanningtreelinktypeasshared.Usethiswhentheportisconnectedtoahub.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Settingspanningtreelinktypetoshared:
| switch(config)#    | interface     | 1/1/1 |                  |
| ------------------ | ------------- | ----- | ---------------- |
| switch(config-if)# | spanning-tree |       | link-type shared |
Settingspanningtreelinktypetopoint-to-pointforaport:
| switch(config)#    | interface        | 1/1/1 |           |
| ------------------ | ---------------- | ----- | --------- |
| switch(config-if)# | no spanning-tree |       | link-type |
| spanning-tree mode |                  |       |           |
Syntax
| spanning-tree mode | {mstp|rpvst} |     |     |
| ------------------ | ------------ | --- | --- |
Description
SetsthespanningtreemodetoeitherMSTPmode(Multiple-instanceSpanningTreeProtocol)orRPVST
mode(RapidPerVLANSpanningTree).
Thenoformofthiscommandsetsthespanningtreemodetothedefaultvaluemstp.
Commandcontext
config
Parameters
mstp
SetsthemodetoMSTP(Multiple-instanceSpanningTreeProtocol),whichappliestheSTP(spanningtree
protocol)separatelyforeachsetofVLANs(calledanMSTI-multiplespanningtreeinstance).
rpvst
SetsthemodetoRPVST(RapidPerVLANSpanningTree).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
EnablingMSTPmode:
| switch(config)# | spanning-tree | mode | mstp |
| --------------- | ------------- | ---- | ---- |
EnablingRPVSTmode:
| switch(config)# | spanning-tree | mode | rpvst |
| --------------- | ------------- | ---- | ----- |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 82

| spanning-tree | pathcost-type |     |     |     |
| ------------- | ------------- | --- | --- | --- |
Syntax
| spanning-tree    | pathcost-type | {long | | short} |     |
| ---------------- | ------------- | ----- | -------- | --- |
| no spanning-tree | pathcost-type |       |          |     |
Description
Configuresthespanningtreepathcosttype.Thelongmodeprovidessupportforthewiderrangeoflink
speedsrequiredbyhigh-speedinterfaces.Allswitchesinthenetworkmustusethesamepathcosttypeor
errorscanoccurinthespanningtree.
Thenoformofthiscommandsetsthespanningtreepathcosttypetothedefaultvalueoflong.
Commandcontext
config
Parameters
long
Specifiesthespanningtreepathcosttypeasa32-bitvalue,allowingportcostvaluestobesetinthe
range1-200,000,000.Default.
short
Specifiesthespanningtreepathcosttypeasa16-bitvalue,allowingportcostvaluestobesetinthe
range1-65535.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingspanningtreepathcosttypetoshort:
| switch#         | config        |     |               |       |
| --------------- | ------------- | --- | ------------- | ----- |
| switch(config)# | spanning-tree |     | pathcost-type | short |
Settingspanningtreepathcosttypetolong:
| switch# | config |     |     |     |
| ------- | ------ | --- | --- | --- |
switch(config)#
|     | spanning-tree |     | pathcost-type | long |
| --- | ------------- | --- | ------------- | ---- |
Settingspanningtreepathcosttodefaultoflong:
| switch#         | config                     |     |               |     |
| --------------- | -------------------------- | --- | ------------- | --- |
| switch(config)# | no spanning-tree           |     | pathcost-type |     |
| spanning-tree   | rpvst-mstpinterconnectvlan |     |               |     |
Syntax
| spanning-tree    | rpvst-mstp-interconnect-vlan |     | <VLAN-ID> |     |
| ---------------- | ---------------------------- | --- | --------- | --- |
| no spanning-tree | rpvst-mstp-interconnect-vlan |     |           |     |
Description
Spanningtreeprotocols|83

Configures the VLAN that has to be used to interconnect RPVST and MSTP domains. VLAN 1 is used by
default.

The no form of this command removes the VLAN configuration.

n It is required to create the interconnect VLAN and then configure RPVST spanning tree on it.

n The same interconnect VLAN must be kept on all the switches in the network.

n Adding or deleting the interconnect VLAN triggers a re-convergence in the network.

n Deleting a VLAN that is configured as the interconnect VLAN does not reset the value to the default.

Command context

config

Parameters

<VLAN-ID>

Specifies the number of a VLAN.

Authority

Administrators or local user group members with execution rights for this command.

Examples

This example configures VLAN 10 to used to interconnect RPVST and MSTP domains.

switch#(config)# spanning-tree rpvst-mstp-interconnect-vlan 10

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

84

| switch(config-if)# | no spanning-tree | tcn-guard |     |
| ------------------ | ---------------- | --------- | --- |
| spanning-tree vlan |                  |           |     |
Syntax
spanning-tree vlan <VLAN-LIST> [{hello-time | foward-delay | max-age | priority} <VALUE>]
no spanning-tree vlan <VLAN-LIST> [hello-time | foward-delay | max-age | priority]
Description
CreatesanRPVSTinstanceforthespecifiedVLAN.ThiscommandalsoallowsforconfigurationofRPVST
instance-specifictimeparameters.
ThenoformofthiscommandremovestheRPVSTinstanceassociatedwiththespecifiedVLAN,and
configuresdefaultvaluesforRPVSTinstance-specificparameters.
Commandcontext
config
Parameters
<VLAN-LIST>
SpecifiesthenumberofasingleVLAN,oraseriesofnumbersforarangeofVLANs,separatedby
commas(1,2,3,4),dashes(1-4),orboth(1-4,6).
hello-time <VALUE>
Specifiesthehello-timeinsecondsfortheRPVSTinstance.Range:2-10seconds.Default:2seconds.
| forward-delay <VALUE> |     |     |     |
| --------------------- | --- | --- | --- |
Specifiestheforward-delaytimeinsecondsfortheRPVSTinstance.Range:4-30seconds.Default:15
seconds.
max-age <VALUE>
SpecifiesthemaximumagetimeinsecondsfortheRPVSTinstance.Range:6-40seconds.Default:20
seconds.
priority <VALUE>
SpecifiesthepriorityfortheRPVSTinstance.Priorityvalueisconfiguredasamultipleof4096.Range:0-
15.Default:8whichis32768.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
CreatinganRPVSTinstanceforalistofVLANsandconfiguringvarioustimeparameters:
switch# config
| switch(config)# | spanning-tree | vlan 2-5               |     |
| --------------- | ------------- | ---------------------- | --- |
| switch(config)# | spanning-tree | vlan 2-5 hello-time    | 5   |
| switch(config)# | spanning-tree | vlan 5 max-age         | 10  |
| switch(config)# | spanning-tree | vlan 2-5 forward-delay | 25  |
| switch(config)# | spanning-tree | vlan 2-5 priority      | 5   |
RemovinganRPVSTinstanceforalistofVLANsandsettingvarioustimeparameterstothedefault:
Spanningtreeprotocols|85

| switch# | config |     |     |     |
| ------- | ------ | --- | --- | --- |
switch(config)#
|                 |      | no spanning-tree | vlan 2-5 |              |
| --------------- | ---- | ---------------- | -------- | ------------ |
| switch(config)# |      | no spanning-tree | vlan 2-5 | hello-time   |
| switch(config)# |      | no spanning-tree | vlan 2-5 | forward-time |
| switch(config)# |      | no spanning-tree | vlan 2-5 | max-age      |
| switch(config)# |      | no spanning-tree | vlan 2-5 | priority     |
| spanning-tree   | vlan | cost             |          |              |
Syntax
| spanning-tree    | vlan | <VLAN-LIST> | cost <PORT-COST> |     |
| ---------------- | ---- | ----------- | ---------------- | --- |
| no spanning-tree | vlan | <VLAN-LIST> | cost             |     |
Description
ConfiguresthespanningtreecostfortheVLAN.Thisisthecosttoreachtherootport.
Thenoformofthiscommandsetstheportcosttothedefaultvalue.
Commandcontext
config-if
Parameters
<VLAN-LIST>
SpecifiesthenumberofasingleVLAN,oraseriesofnumbersforarangeofVLANs,separatedby
commas(1,2,3,4),dashes(1-4),orboth(1-4,6).
<PORT-COST>
SpecifiesthespanningtreecostfortheVLAN.Range:1-200,000,000.Defaultiscalculatedfromtheport
linkspeed:
n 10Mbpslinkspeedequalsapathcostof2,000,000.
n 100Mbpslinkspeedequalsapathcostof200,000.
n 1Gbpslinkspeedequalsapathcostof20,000.
2Gbpslinkspeedequalsapathcostof10,000.
n
10Gbpslinkspeedequalsapathcostof2,000.
n
100Gbpslinkspeedequalsapathcostof200.
n
n 1Tbpslinkspeedequalsapathcostof20.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingportcost:
| switch(config-if)# |     | spanning-tree | vlan 5 cost | 100000 |
| ------------------ | --- | ------------- | ----------- | ------ |
Settingportcosttothedefault:
| switch(config-if)# |      | no spanning-tree | vlan 5 | cost |
| ------------------ | ---- | ---------------- | ------ | ---- |
| spanning-tree      | vlan | port-priority    |        |      |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 86

Syntax

spanning-tree vlan <VLAN-LIST> port-priority <PRIORITY>
no spanning-tree vlan <VLAN-LIST> port-priority

Description

Configures port priority. A port with the lowest priority number has the highest priority for use in
forwarding traffic.

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

Command context

config

Parameters

Spanning tree protocols | 87

new-root
EnablesSNMPnotificationwhenanewrootiselectedonanyPVSTvlanontheswitch.
topology-change
EnablesSNMPnotificationwhenatopologychangeeventoccurredinspecifiedPVSTvlanontheswitch.
errant-bpdu
EnablesSNMPnotificationwhenanerrantbpduisreceivedbyanyPVSTvlanontheswitch.
root-guard-inconsistency
EnablesSNMPnotificationwhentheroot-guardfindstheportinconsistentforanyPVSTvlanonthe
switch.
loop-guard-inconsistency
EnablesSNMPnotificationwhentheloop-guardfindstheportinconsistentforanyPVSTvlanonthe
switch.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Commandsenablingspanning-treetrapfeatures:
| switch(config)# | spanning-tree | trap |     |
| --------------- | ------------- | ---- | --- |
new-root Enable notifications which are sent when a new root is
elected
topology-change Enable notifications which are sent when a topology
change occurs
errant-bpdu Enable notifications which are sent when an errant bpdu
is received
root-guard-inconsistency Enable notifications which are sent when root guard
| inconsistency | occurs |     |     |
| ------------- | ------ | --- | --- |
loop-guard-inconsistency Enable notifications which are sent when root guard
| inconsistency   | occurs        |               |     |
| --------------- | ------------- | ------------- | --- |
| switch(config)# | spanning-tree | trap new-root |     |
<cr>
| switch(config)# | spanning-tree | trap topology-change |     |
| --------------- | ------------- | -------------------- | --- |
vlan Enable topology change notification for the specified PVST vlan id.
| switch(config)# | spanning-tree | trap topology-change | vlan |
| --------------- | ------------- | -------------------- | ---- |
<0-64> Enable topology change information on the specified vlan id.
| switch(config)# | spanning-tree | trap topology-change | vlan 1 |
| --------------- | ------------- | -------------------- | ------ |
<cr>
| switch(config)# | spanning-tree | trap errant-bpdu |     |
| --------------- | ------------- | ---------------- | --- |
<cr>
| switch(config)# | spanning-tree | trap root-guard-inconsistency |     |
| --------------- | ------------- | ----------------------------- | --- |
<cr>
| switch(config)# | spanning-tree | trap loop-guard-inconsistency |     |
| --------------- | ------------- | ----------------------------- | --- |
<cr>
Commandsdisablingspanning-treetrapfeatures:
| switch(config)# | no spanning-tree | trap |     |
| --------------- | ---------------- | ---- | --- |
new-root Disable notifications which are sent when a new root is
elected
topology-change Disable notifications which are sent when a topology
change occurs
errant-bpdu Disable notifications which are sent when an errant bpdu
is received
root-guard-inconsistency Disable notifications which are sent when root guard
| inconsistency | occurs |     |     |
| ------------- | ------ | --- | --- |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 88

loop-guard-inconsistency Disable notifications which are sent when root guard

inconsistency occurs
switch(config)# no spanning-tree trap new-root

<cr>

switch(config)# no spanning-tree trap topology-change

instance Disable topology change notification for the specified PVST vlan id.

switch(config)# no spanning-tree trap topology-change vlan

<0-64> Disable topology change information on the specified PVST vlan id.

switch(config)# no spanning-tree trap topology-change vlan 0

<cr>

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

n MSTP divides a switched network into multiple regions, each of which contains multiple spanning trees

that are independent of one another.

n MSTP supports mapping VLANs to spanning tree instances by means of a VLAN-to-instance mapping
table. MSTP can reduce communication overheads and resource usage by mapping multiple VLANs to
one instance.

n MSTP prunes a loop network into a loop-free tree, which avoids proliferation and endless cycling of

packets in a loop network. In addition, it supports load balancing of VLAN data by providing multiple
redundant paths for data forwarding.

n MSTP is compatible with STP and RSTP, and partially compatible with PVST.

MSTP key concepts

MSTP divides an entire Layer 2 network into multiple MST regions, which are connected by a calculated CST.
Inside an MST region, multiple spanning trees, called MSTIs, are calculated. Among these MSTIs, MSTI 0 is the
internal spanning tree (IST).

The following diagram shows a switched network that comprises four MST regions, with each MST region
comprising four MSTP devices.

Spanning tree protocols | 89

The following diagram shows the networking topology of MST region 3.

MST region

A multiple spanning tree region (MST region) consists of multiple devices in a switched network and the
network segments between them. All these devices have the following characteristics:

n A spanning tree protocol enabled.

n Same region name.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

90

n Same VLAN-to-instance mapping configuration.

n Same MSTP revision level.

n Physically linked together.

Multiple MST regions can exist in a switched network. You can assign multiple devices to the same MST
region.

n The switched network comprises four MST regions, MST region 1 through MST region 4.

n All devices in each MST region have the same MST region configuration.

MSTI

MSTP can generate multiple independent spanning trees in an MST region, and each spanning tree is
mapped to specific VLANs. Each spanning tree is referred to as a multiple spanning tree instance (MSTI). In
the diagrams, MST region 3 comprises three MSTIs, MSTI 1, MSTI 2, and MSTI 0.

MSTI 0

VLAN-to-instance mapping table

As an attribute of an MST region, the VLAN-to-instance mapping table describes the mapping relationships
between VLANs and MSTIs.

In the diagrams, the VLAN-to-instance mapping table of MST region 3 is as follows:

n VLAN 1 to MSTI 1. (Ports which are not part of any VLAN are by default part of VLAN 1.)

n VLAN 2 and VLAN 3 to MSTI 2.

n Other VLANs to MSTI 0. (VLANs that are not configured as part of any MSTI are by default part of MSTI

0.)

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
the topology, different spanning trees in an MST region might have different regional roots, as shown in
MST region 3 in the diagrams:

Spanning tree protocols | 91

n The regional root of MSTI 1 is Device B.

n The regional root of MSTI 2 is Device C.

n The regional root of MSTI 0 (also known as the IST) is Device A.

Common root bridge

The common root bridge is the root bridge of the CIST. In the diagrams, the common root bridge is a device
in MST region 1.

Port roles

A port can play different roles in different MSTIs. In the following diagram, an MST region comprises Device
A, Device B, Device C, and Device D. Port A1 and port A2 of Device A connect to the common root bridge.
Port B2 and Port B3 of Device B form a loop. Port C3 and Port C4 of Device C connect to other MST regions.
Port D3 of Device D directly connects to a host.

MSTP calculation involves the following port roles:

n Root port: Forwards data for a non-root bridge to the root bridge. The root bridge does not have any

root port.

n Designated port: Forwards data to the downstream network segment or device.

n Alternate port: Acts as the backup port for a root port or master port. When the root port or master port

is blocked, the alternate port takes over.

n Backup port: Acts as the backup port of a designated port. When the designated port is invalid, the

backup port becomes the new designated port. A loop occurs when two ports of the same spanning tree
device are connected, so the device blocks one of the ports. The blocked port acts as the backup.

n Edge port: Does not connect to any network device or network segment, but directly connects to a user

host.

n Master port: Acts as a port on the shortest path from the local MST region to the common root bridge.
The master port is not always located on the regional root. It is a root port on the IST or CIST and still a
master port on the other MSTIs.

n Boundary port: Connects an MST region to another MST region or to an STP/RSTP-running device. In

MSTP calculation, a boundary port's role on an MSTI is consistent with its role on the CIST. However, that
is not true with master ports. A master port on MSTIs is a root port on the CIST.

Port states

In MSTP, a port can be in one of the following states:

n Forwarding: The port receives and sends BPDUs, learns MAC addresses, and forwards user traffic.

n Learning: The port receives and sends BPDUs, learns MAC addresses, but does not forward user traffic.

Learning is an intermediate port state.

n Discarding: The port receives and sends BPDUs, but does not learn MAC addresses or forward user

traffic.

When in different MSTIs, a port can be in different states.

A port state is not exclusively associated with a port role. The following table lsts the port states that each
port role supports. (An X indicates that the port supports this state, while a dash [—] indicates that the port
does not support this state.)

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

92

Port state

Root port/master
port

Designated port

Alternate port

Backup port

Port role

Forwarding

Learning

Discarding

X

X

X

CIST calculation

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

n The device with the highest priority is elected as the root bridge of the CIST.

n MSTP generates an IST within each MST region through calculation.

n MSTP regards each MST region as a single device and generates a CST among these MST regions through

calculation.

The CST and ISTs constitute the CIST of the entire network.

MSTI calculation

Within an MST region, MSTP generates different MSTIs for different VLANs based on the VLAN-to-instance
mappings. For each spanning tree, MSTP performs a separate calculation process similar to spanning tree
calculation in STP.

In MSTP, a VLAN packet is forwarded along the following paths:

n Within an MST region, the packet is forwarded along the corresponding MSTI.

n Between two MST regions, the packet is forwarded along the CST.

MSTP on VSX

See the Virtual Switching Extension (VSX) Guide for important information when configuring MSTP with VSX.

Preparing for MSTP configuration

n Ensure that the VLAN configuration in your network supports all of the forwarding paths necessary for
the desired connectivity. All ports connecting one switch to another within a region and one switch to
another between regions should be configured as members of all VLANs configured in the region.

n Configure all ports or trunks connecting one switch to another within a region as members of all VLANs in

the region. Otherwise, some VLANs could be blocked from access to the spanning tree root for an
instance or for the region.

n Plan individual MST regions based on VLAN groupings. That is, plan on all MSTP switches in a given region

supporting the same set of VLANs. Within each region, determine the VLAN membership for each
spanning tree instance. (Each instance represents a single forwarding path for all VLANs in that instance.)

n Verify that there is one logical spanning tree path through the following:

o Any interregional links

o Any IST (Internal Spanning Tree) or MSTI within a region

Spanning tree protocols | 93

o Any legacy (802.1D or 802.1w) switch or group of switches. (Where multiple paths exist between an
MST region and a legacy switch, expect the CST (Common Spanning Tree) to block all but one such
path.)

n Determine the root bridge and root port for each MSTI.

n Determine the designated bridge and designated port for each LAN segment.

n Determine which VLANs to assign to each MST instance and use port trunks with 802.1Q VLAN tagging

where separate links for separate VLANs would result in a blocked link preventing communication
between nodes on the same VLAN.

n Set the admin-edge port type to admin-edge for edge ports connected to end nodes.

n Set the admin-edge port type to admin-network for ports connected to another switch, a bridge, or a

half-duplex repeater.

MSTP scenario

On the 6400 Switch Series, interface identification differs.

In this scenario, all four switches are in same region. VLANs 10, 20, 30, 40, 50, and 60 are defined on all
switches, causing a network loop. The physical topology of the network looks like this:

To eliminate the loop, MSTP is enabled on all the switches, with the following configuration:

n Switch SW-TR is the root for CIST, MST1, and MST2.

n CIST: VLANs 10, 20

n Instance-1: VLANs 30,40

n Instance-2: VLANs 50,60

n All four switches are in the same MSTP region.

To understand how MSTP works in this scenario, it is useful to view each instance as a separate logical
topology as illustrated in the following diagrams:

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

94

Spanning tree protocols | 95

Loops are avoided by blocking the alternate links for each network segment. All ports designated A
(Alternate) are blocked and do not forward traffic. Although this strategy eliminates the loops, it is not the
most effective way to configure the MST regions because network resources are not fully used. By changing
the root for each instance, more effective load sharing can be achieved as follows:

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

96

Withthisconfiguration,thelinks/portsthatwerepreviouslyunusedarenowbeingusedbydifferent
instances.Also,thenetworkloopiseliminatedandloadsharingisachieved.
Procedure
ConfigureallswitcheswiththesameVLANs,interfaces,andspanningtreeinstances.
1. CreateVLANs10,20,30,40,50,and60andassignthemtointerfaces.
switch# config
| switch(config)# | vlan 10,20,30,40,50,60 |       |
| --------------- | ---------------------- | ----- |
| switch(config)# | interface              | 1/1/1 |
Spanningtreeprotocols|97

| switch(config-if)# | no shutdown |     |     |
| ------------------ | ----------- | --- | --- |
switch(config-if)#
|                    | vlan trunk  | allowed 10,20,30,40,50,60 |     |
| ------------------ | ----------- | ------------------------- | --- |
| switch(config-if)# | interface   | 1/1/2                     |     |
| switch(config-if)# | no shutdown |                           |     |
| switch(config-if)# | vlan trunk  | allowed 10,20,30,40,50,60 |     |
| switch(config-if)# | interface   | 1/1/3                     |     |
| switch(config-if)# | no shutdown |                           |     |
| switch(config-if)# | vlan trunk  | allowed 10,20,30,40,50,60 |     |
| switch(config-if)# | interface   | 1/1/4                     |     |
| switch(config-if)# | no shutdown |                           |     |
| switch(config-if)# | vlan trunk  | allowed 10,20,30,40,50,60 |     |
switch(config-if)#
exit
2. Configurespanningtreeandenableit.
| switch(config)# | spanning-tree | config-name | reg |
| --------------- | ------------- | ----------- | --- |
switch(config)#
|                 | spanning-tree | config-revision | 1   |
| --------------- | ------------- | --------------- | --- |
| switch(config)# | spanning-tree | inst 1 vlan     | 30  |
| switch(config)# | spanning-tree | inst 1 vlan     | 40  |
| switch(config)# | spanning-tree | inst 2 vlan     | 50  |
| switch(config)# | spanning-tree | inst 2 vlan     | 60  |
| switch(config)# | spanning-tree |                 |     |
3. OnswitchSW-TL,setinstance1topriority0.
| sw-tl(config)# | spanning-tree | inst 1 priority | 0   |
| -------------- | ------------- | --------------- | --- |
4. OnswitchSW-BL,setinstance2topriority0.
| sw-bl(config)# | spanning-tree | inst 2 priority | 0   |
| -------------- | ------------- | --------------- | --- |
5. OnswitchSW-TR,setthebridgepriorityto0.
| sw-tr(config)# | spanning-tree | priority 0 |     |
| -------------- | ------------- | ---------- | --- |
MSTP commands
show spanning-tree
Syntax
| show spanning-tree [vsx-peer] |     |     |     |
| ----------------------------- | --- | --- | --- |
Description
Showspriority,address,Hello-time,Max-age,andForward-delayforbridgeandrootnode.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 98

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingspanningtreestandardinformation:
| switch#  | show spanning-tree |           |           |      |     |     |
| -------- | ------------------ | --------- | --------- | ---- | --- | --- |
| Spanning | tree status        | : Enabled | Protocol: | MSTP |     |     |
MST0
Root ID
| Priority    | : 32768,            | Root    |     |     |     |     |
| ----------- | ------------------- | ------- | --- | --- | --- | --- |
| MAC-Address | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| Hello       | time : 2 seconds    |         |     |     |     |     |
| Max         | Age : 20            | seconds |     |     |     |     |
| Forward     | Delay : 15          | seconds |     |     |     |     |
| Bridge      | ID                  |         |     |     |     |     |
| Priority    | : 32768             |         |     |     |     |     |
| MAC-Address | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| Hello       | time : 2 seconds    |         |     |     |     |     |
| Max         | Age : 20            | seconds |     |     |     |     |
| Forward     | Delay : 15          | seconds |     |     |     |     |
PORT ROLE STATE COST PRIORITY TYPE BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------ ----------- ---------- ------ -------- -------- ------- ------- ------ ------
| 1/1/1         | Designated Forwarding | 20000 | 128     | P2P Edge 100 | 60 20 | 10  |
| ------------- | --------------------- | ----- | ------- | ------------ | ----- | --- |
| 1/1/2         | Designated Forwarding | 20000 | 128     | P2P 100      | 60 20 | 10  |
| 1/1/3         | Designated Forwarding | 20000 | 128     | Shr 100      | 60 20 | 10  |
| 1/1/4         | Designated Forwarding | 20000 | 128     | Shr Edge 100 | 60 20 | 10  |
| 1/1/5         | Alternate Loop-Inc    | 20000 | 128     | Shr Edge 100 | 60 20 | 10  |
| 1/1/6         | Alternate Root-Inc    | 20000 | 128     | Shr Edge 100 | 60 20 | 10  |
| Number        | of topology changes   | : 4   |         |              |       |     |
| Last topology | change occurred       | : 516 | seconds | ago          |       |     |
show spanning-tree detail
Syntax
| show spanning-tree | detail | [vsx-peer] |     |     |     |     |
| ------------------ | ------ | ---------- | --- | --- | --- | --- |
Description
ShowsspanningtreedetailincludingCISTandcorrespondingportinformation.
Commandcontext
Operator(>)orManager(#)
Parameters
[vsx-peer]
Spanningtreeprotocols|99

ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingspanningtreedetailedinformation:
| switch#  | show | spanning-tree |     | detail    |     |           |      |     |     |     |
| -------- | ---- | ------------- | --- | --------- | --- | --------- | ---- | --- | --- | --- |
| Spanning | tree | status        |     | : Enabled |     | Protocol: | MSTP |     |     |     |
MST0
| Root   | ID     | Priority     |          | : 32768           |             |     |          |             |         |         |
| ------ | ------ | ------------ | -------- | ----------------- | ----------- | --- | -------- | ----------- | ------- | ------- |
|        |        | MAC-Address: |          | 48:0f:cf:af:04:76 |             |     |          |             |         |         |
|        |        | This         | bridge   | is the            | root        |     |          |             |         |         |
|        |        | Hello        | time(in  | seconds):2        |             | Max | Age(in   | seconds):20 |         |         |
|        |        | Forward      | Delay(in |                   | seconds):15 |     |          |             |         |         |
| Bridge | ID     | Priority     |          | : 32768           |             |     |          |             |         |         |
|        |        | MAC-Address: |          | 48:0f:cf:af:04:76 |             |     |          |             |         |         |
|        |        | Hello        | time(in  | seconds):2        |             | Max | Age(in   | seconds):20 |         |         |
|        |        | Forward      | Delay(in |                   | seconds):15 |     |          |             |         |         |
| PORT   | ROLE   |              | STATE    |                   | COST        |     | PRIORITY | TYPE        | BPDU-Tx | BPDU-Rx |
| TCN-Tx | TCN-Rx |              |          |                   |             |     |          |             |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |        |            |     |         |         |        |          |     |     |
| ------------- | ----------- | ------ | ---------- | --- | ------- | ------- | ------ | -------- | --- | --- |
| 1/1/1         | Designated  |        | Forwarding |     | 20000   |         | 128    | P2P Edge | 100 | 60  |
| 20            | 10          |        |            |     |         |         |        |          |     |     |
| 1/1/2         | Designated  |        | Forwarding |     | 20000   |         | 128    | P2P      | 100 | 60  |
| 20            | 10          |        |            |     |         |         |        |          |     |     |
| 1/1/3         | Designated  |        | Forwarding |     | 20000   |         | 128    | Shr      | 100 | 60  |
| 20            | 10          |        |            |     |         |         |        |          |     |     |
| 1/1/4         | Designated  |        | Forwarding |     | 20000   |         | 128    | Shr Edge | 100 | 60  |
| 20            | 10          |        |            |     |         |         |        |          |     |     |
| 1/1/5         | Alternate   |        | Loop-Inc   |     | 20000   |         | 128    | Shr Edge | 100 | 60  |
| 20            | 10          |        |            |     |         |         |        |          |     |     |
| 1/1/6         | Alternate   |        | Root-Inc   |     | 20000   |         | 128    | Shr Edge | 100 | 60  |
| 20            | 10          |        |            |     |         |         |        |          |     |     |
| Topology      | change      | flag   |            |     | : True  |         |        |          |     |     |
| Number        | of topology |        | changes    |     | : 4     |         |        |          |     |     |
| Last topology |             | change | occurred   |     | : 516   | seconds | ago    |          |     |     |
| Timers:       | Hello       | expiry |            | 1 , | Forward | delay   | expiry | 18       |     |     |
Port 1/1/1
Designated root has priority :32768 Address: 48:0f:cf:af:04:76
Designated bridge has priority :32768 Address: 48:0f:cf:af:04:76
| Designated | port           |          |     |            |     |       | :1/1/1 |     |     |     |
| ---------- | -------------- | -------- | --- | ---------- | --- | ----- | ------ | --- | --- | --- |
| Number     | of transitions |          | to  | forwarding |     | state | : 3    |     |     |     |
| Bpdus sent | 347,           | received |     | 9          |     |       |        |     |     |     |
| TCN_Tx:    | 20, TCN_Rx:    |          | 10  |            |     |       |        |     |     |     |
Port 1/1/2
Designated root has priority :32768 Address: 48:0f:cf:af:04:76
Designated bridge has priority :32768 Address: 48:0f:cf:af:04:76
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 100

| Designated | port           |          |          |            |       | :1/1/2  |          |
| ---------- | -------------- | -------- | -------- | ---------- | ----- | ------- | -------- |
| Number     | of transitions |          | to       | forwarding | state | : 3     |          |
| Bpdus sent | 350,           | received |          | 11         |       |         |          |
| TCN_Tx:    | 20,            | TCN_Rx:  | 10       |            |       |         |          |
| Port lag1  | ID             | 321      |          |            |       |         |          |
| Designated | root           | has      | priority |            |       | : 32768 | Address: |
48:0F:CF:AF:04:76
| Designated | bridge | has | priority |     |     | : 32768 | Address: |
| ---------- | ------ | --- | -------- | --- | --- | ------- | -------- |
48:0F:CF:AF:04:76
| Designated         | port           | id                 |     |            |       | : 321    |     |
| ------------------ | -------------- | ------------------ | --- | ---------- | ----- | -------- | --- |
| Multi-Chassis      |                | role               |     |            |       | : active |     |
| Number             | of transitions |                    | to  | forwarding | state | : 3      |     |
| BPDUs sent         |                |                    |     |            |       | : 340    |     |
| BPDUs received     |                |                    |     |            |       | : 5      |     |
| TCN_Tx:            | 20,            | TCN_Rx:            | 10  |            |       |          |     |
| show spanning-tree |                | inconsistent-ports |     |            |       |          |     |
Syntax
| show spanning-tree |     | inconsistent-ports |     |     | [instance | <INSTANCE-ID>] |     |
| ------------------ | --- | ------------------ | --- | --- | --------- | -------------- | --- |
Description
ShowsportsblockedbySTPprotectionfunctionssuchasRootguard,Loopguard,BPDUguard,andRPVST
guardinadditiontoMSTIinformation.
Commandcontext
Operator(>)orManager(#)
Parameters
<INSTANCE-ID>
SpecifiestheMSTPinstanceID.Range:0to64.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingspanningtreeinconsistentports:
| switch#      | show | spanning-tree  |      | inconsistent-ports |       |     |     |
| ------------ | ---- | -------------- | ---- | ------------------ | ----- | --- | --- |
| Instance     | ID   | Blocked        | Port | Reason             |       |     |     |
| ------------ |      | -------------- |      | ------------       |       |     |     |
| 0            |      | 1/1/13         |      | BPDU               | Guard |     |     |
Showinginconsistentportinformationforinstances1-4:
| switch#      | show | spanning-tree  |      | inconsistent-ports |       | instance 1-4 |     |
| ------------ | ---- | -------------- | ---- | ------------------ | ----- | ------------ | --- |
| Instance     | ID   | Blocked        | Port | Reason             |       |              |     |
| ------------ |      | -------------- |      | ------------       |       |              |     |
| 1            |      | 1/1/3          |      | Root               | Guard |              |     |
Spanningtreeprotocols|101

| 2                  | 1/1/7  |     | BPDU Guard  |     |     |     |     |
| ------------------ | ------ | --- | ----------- | --- | --- | --- | --- |
| 3                  | 1/1/9  |     | Loop Guard  |     |     |     |     |
| 4                  | 1/1/37 |     | RPVST Guard |     |     |     |     |
| show spanning-tree |        | mst |             |     |     |     |     |
Syntax
| show spanning-tree | mst | [vsx-peer] |     |     |     |     |     |
| ------------------ | --- | ---------- | --- | --- | --- | --- | --- |
Description
ShowsMSTPconfigurationandstatusinformationforeachinstance.
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
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingMSTPconfigurationandstatusinformation:
| switch# show | spanning-tree |     | mst |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- |
#### MST0
| Vlans mapped   | : 2,4-4094          |     |     |     |     |     |     |
| -------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| Bridge Address | : 48:0F:CF:AF:04:76 |     |     |     |     |     |     |
| Priority       | : 32768             |     |     |     |     |     |     |
Root
| Regional Root |          |       |                     |          |             |         |            |
| ------------- | -------- | ----- | ------------------- | -------- | ----------- | ------- | ---------- |
| Operational   | Hello    | time  | : 2 seconds         |          | Forward     | delay:  | 15 seconds |
|               | Max-age  |       | : 20 seconds        |          | TxHoldCount |         | : 6 pps    |
| Configured    | Hello    | time  | : 2 seconds         |          | Forward     | delay:  | 15 seconds |
|               | Max-age  |       | : 20 seconds        |          | Max-Hops    |         | : 20       |
| Root          | Address  |       | : 48:0F:CF:AF:04:76 |          | Priority    |         | : 32768    |
|               | Port     |       | : 0                 |          | Path        | cost    | : 0        |
| Regional Root | Address  |       | : 48:0F:CF:AF:04:76 |          | Priority    |         | : 32768    |
|               | Internal | cost: | 0                   |          | Rem         | Hops    | : 20       |
| PORT ROLE     |          | STATE | COST                | PRIORITY | TYPE        | BPDU-Tx | BPDU-Rx    |
| TCN-Tx        | TCN-Rx   |       |                     |          |             |         |            |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------       | ---------- |            |       |     |          |     |     |
| ---------------- | ---------- | ---------- | ----- | --- | -------- | --- | --- |
| 1/1/1 Designated |            | Forwarding | 20000 | 128 | P2P Edge | 100 | 60  |
| 20               | 10         |            |       |     |          |     |     |
| 1/1/2 Designated |            | Forwarding | 20000 | 128 | P2P      | 100 | 60  |
| 20               | 10         |            |       |     |          |     |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 102

| 1/1/3         | Designated  | Forwarding | 20000         | 128 | Shr      | 100 | 60  |
| ------------- | ----------- | ---------- | ------------- | --- | -------- | --- | --- |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/4         | Designated  | Forwarding | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/5         | Alternate   | Loop-Inc   | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/6         | Alternate   | Root-Inc   | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| Topology      | change flag |            | : True        |     |          |     |     |
| Number        | of topology | changes    | : 4           |     |          |     |     |
| Last topology | change      | occurred   | : 516 seconds | ago |          |     |     |
#### MST1
| Vlans mapped: | 1       |                     |      |          |           |         |         |
| ------------- | ------- | ------------------- | ---- | -------- | --------- | ------- | ------- |
| Bridge        | Address | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          | Address | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               | Port    | : 0                 |      |          | Cost      | : 0     |         |
|               | Rem     | Hops: 20            |      |          |           |         |         |
| PORT          | ROLE    | STATE               | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        | TCN-Rx  |                     |      |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |            |               |     |          |     |     |
| ------------- | ----------- | ---------- | ------------- | --- | -------- | --- | --- |
| 1/1/1         | Designated  | Forwarding | 20000         | 128 | P2P Edge | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/2         | Designated  | Forwarding | 20000         | 128 | P2P      | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/3         | Designated  | Forwarding | 20000         | 128 | Shr      | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/4         | Designated  | Forwarding | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/5         | Alternate   | Loop-Inc   | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| 1/1/6         | Alternate   | Root-Inc   | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| Topology      | change flag |            | : True        |     |          |     |     |
| Number        | of topology | changes    | : 4           |     |          |     |     |
| Last topology | change      | occurred   | : 516 seconds | ago |          |     |     |
#### MST2
| Vlans mapped: | 3       |                     |      |          |           |         |         |
| ------------- | ------- | ------------------- | ---- | -------- | --------- | ------- | ------- |
| Bridge        | Address | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          | Address | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               | Port    | : 0                 |      |          | Cost      | : 0     |         |
|               | Rem     | Hops: 20            |      |          |           |         |         |
| PORT          | ROLE    | STATE               | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        | TCN-Rx  |                     |      |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ---------- | ---------- |            |       |     |          |     |     |
| ---------- | ---------- | ---------- | ----- | --- | -------- | --- | --- |
| 1/1/1      | Designated | Forwarding | 20000 | 128 | P2P Edge | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/2      | Designated | Forwarding | 20000 | 128 | P2P      | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/3      | Designated | Forwarding | 20000 | 128 | Shr      | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/4      | Designated | Forwarding | 20000 | 128 | Shr Edge | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
| 1/1/5      | Alternate  | Loop-Inc   | 20000 | 128 | Shr Edge | 100 | 60  |
| 20         | 10         |            |       |     |          |     |     |
Spanningtreeprotocols|103

| 1/1/6              | Alternate   | Root-Inc   | 20000         | 128 | Shr Edge | 100 | 60  |
| ------------------ | ----------- | ---------- | ------------- | --- | -------- | --- | --- |
| 20                 | 10          |            |               |     |          |     |     |
| Topology           | change flag |            | : True        |     |          |     |     |
| Number             | of topology | changes    | : 4           |     |          |     |     |
| Last topology      | change      | occurred   | : 516 seconds | ago |          |     |     |
| show spanning-tree |             | mst-config |               |     |          |     |     |
Syntax
| show spanning-tree | mst-config |     | [vsx-peer] |     |     |     |     |
| ------------------ | ---------- | --- | ---------- | --- | --- | --- | --- |
Description
ShowsMSTPinstanceandcorrespondingVLANinformation.
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
ShowingconfigurationinformationforMSTinstancesandcorrespondingVLANs:
| switch#            | show spanning-tree                 |                                    | mst-config |     |     |     |     |
| ------------------ | ---------------------------------- | ---------------------------------- | ---------- | --- | --- | --- | --- |
| MST configuration  |                                    | information                        |            |     |     |     |     |
| MST                | config ID                          | : reg                              |            |     |     |     |     |
| MST                | config revision                    | : 1                                |            |     |     |     |     |
| MST                | config digest                      | : 2D2BC9A32097B463C48EE1817673FA2D |            |     |     |     |     |
| Number             | of instances                       | : 2                                |            |     |     |     |     |
| Instance           | ID Member                          | VLANs                              |            |     |     |     |     |
| ---------------    | ---------------------------------- |                                    |            |     |     |     |     |
| 0                  | 2,4-4094                           |                                    |            |     |     |     |     |
| 1                  | 1                                  |                                    |            |     |     |     |     |
| 2                  | 3                                  |                                    |            |     |     |     |     |
| show spanning-tree |                                    | mstdetail                          |            |     |     |     |     |
Syntax
| show spanning-tree | mst | detail | [vsx-peer] |     |     |     |     |
| ------------------ | --- | ------ | ---------- | --- | --- | --- | --- |
Description
ShowsdetailedinformationforallMSTinstances.
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 104

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
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingdetailedinformationforallMSTinstances:
| switch# | show | spanning-tree |     | mst | detail |     |     |     |     |     |
| ------- | ---- | ------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
#### MST0
| Vlans mapped: |     | 2,4-4094 |     |                   |     |     |           |     |       |     |
| ------------- | --- | -------- | --- | ----------------- | --- | --- | --------- | --- | ----- | --- |
| Bridge        |     | Address: |     | 48:0F:CF:AF:04:76 |     |     | Priority: |     | 32768 |     |
Root
| Regional    | Root   |          |       |       |                   |          |      |             |         |            |
| ----------- | ------ | -------- | ----- | ----- | ----------------- | -------- | ---- | ----------- | ------- | ---------- |
| Operational |        | Hello    | time  | :     | 2 seconds         |          |      | Forward     | delay:  | 15 seconds |
|             |        | Max-age  |       | :     | 20 seconds        |          |      | TxHoldCount |         | : 6 pps    |
| Configured  |        | Hello    | time  | :     | 2 seconds         |          |      | Forward     | delay:  | 15 seconds |
|             |        | Max-age  |       | :     | 20 seconds        |          |      | Max-Hops    |         | : 20       |
| Root        |        | Address  |       | :     | 48:0F:CF:AF:04:76 |          |      | Priority    |         | : 32768    |
|             |        | Port     |       | :     | 0                 |          |      | Path        | cost    | : 0        |
| Regional    | Root   | Address  |       | :     | 48:0F:CF:AF:04:76 |          |      | Priority    |         | : 32768    |
|             |        | Internal |       | cost: | 0                 |          |      | Rem         | Hops    | : 20       |
| PORT        | ROLE   |          | STATE |       | COST              | PRIORITY | TYPE |             | BPDU-Tx | BPDU-Rx    |
| TCN-Tx      | TCN-Rx |          |       |       |                   |          |      |             |         |            |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |        |            |     |               |     |     |      |     |     |
| ------------- | ----------- | ------ | ---------- | --- | ------------- | --- | --- | ---- | --- | --- |
| 1/1/1         | Designated  |        | Forwarding |     | 20000         | 128 | P2P | Edge | 100 | 60  |
| 20            | 10          |        |            |     |               |     |     |      |     |     |
| 1/1/2         | Designated  |        | Forwarding |     | 20000         | 128 | P2P |      | 100 | 60  |
| 20            | 10          |        |            |     |               |     |     |      |     |     |
| 1/1/3         | Designated  |        | Forwarding |     | 20000         | 128 | Shr |      | 100 | 60  |
| 20            | 10          |        |            |     |               |     |     |      |     |     |
| 1/1/4         | Designated  |        | Forwarding |     | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            | 10          |        |            |     |               |     |     |      |     |     |
| 1/1/5         | Alternate   |        | Loop-Inc   |     | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            | 10          |        |            |     |               |     |     |      |     |     |
| 1/1/6         | Alternate   |        | Root-Inc   |     | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            | 10          |        |            |     |               |     |     |      |     |     |
| Topology      | change      | flag   |            |     | : True        |     |     |      |     |     |
| Number        | of topology |        | changes    |     | : 4           |     |     |      |     |     |
| Last topology |             | change | occurred   |     | : 516 seconds | ago |     |      |     |     |
Port 1/1/1
| Designated | root     | address |         |         | : 48:0F:CF:AF:04:76 |     |     |     |     |     |
| ---------- | -------- | ------- | ------- | ------- | ------------------- | --- | --- | --- | --- | --- |
| Designated | regional |         | root    | address | : 48:0F:CF:AF:04:76 |     |     |     |     |     |
| Designated | bridge   |         | address |         | : 48:0F:CF:AF:04:76 |     |     |     |     |     |
Spanningtreeprotocols|105

| Priority       |             |        |     | : 32768    |         |     |     |     |
| -------------- | ----------- | ------ | --- | ---------- | ------- | --- | --- | --- |
| BPDUs sent     |             |        |     | : 638      |         |     |     |     |
| BPDUs received |             |        |     | : 9        |         |     |     |     |
| Message        | expiry      |        |     | : 1 second |         |     |     |     |
| Forward        | delay       | expiry |     | : 18       | seconds |     |     |     |
| Forward        | transitions |        |     | : 3        |         |     |     |     |
| TCN_Tx:        | 10, TCN_Rx: | 10     |     |            |         |     |     |     |
Port 1/1/2
| Designated     | root        | address |         | : 48:0F:CF:AF:04:76 |         |     |     |     |
| -------------- | ----------- | ------- | ------- | ------------------- | ------- | --- | --- | --- |
| Designated     | regional    | root    | address | : 48:0F:CF:AF:04:76 |         |     |     |     |
| Designated     | bridge      | address |         | : 48:0F:CF:AF:04:76 |         |     |     |     |
| Priority       |             |         |         | : 32768             |         |     |     |     |
| BPDUs sent     |             |         |         | : 641               |         |     |     |     |
| BPDUs received |             |         |         | : 11                |         |     |     |     |
| Message        | expiry      |         |         | : 1 second          |         |     |     |     |
| Forward        | delay       | expiry  |         | : 18                | seconds |     |     |     |
| Forward        | transitions |         |         | : 3                 |         |     |     |     |
| TCN_Tx:        | 10, TCN_Rx: | 10      |         |                     |         |     |     |     |
#### MST1
| Vlans mapped: |        | 1         |                     |      |          |           |         |         |
| ------------- | ------ | --------- | ------------------- | ---- | -------- | --------- | ------- | ------- |
| Bridge        |        | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          |        | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               |        | Port      | : 0                 |      |          | Cost      | : 0     |         |
|               |        | Rem Hops: | 20                  |      |          |           |         |         |
| PORT          | ROLE   | STATE     |                     | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        | TCN-Rx |           |                     |      |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |                 |     |               |     |          |     |     |
| ------------- | ----------- | --------------- | --- | ------------- | --- | -------- | --- | --- |
| 1/1/1         | Designated  | Forwarding      |     | 20000         | 128 | P2P Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/2         | Designated  | Forwarding      |     | 20000         | 128 | P2P      | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/3         | Designated  | Forwarding      |     | 20000         | 128 | Shr      | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/4         | Designated  | Forwarding      |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/5         | Alternate   | Loop-Inc        |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/6         | Alternate   | Root-Inc        |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| Topology      | change      | flag            |     | : True        |     |          |     |     |
| Number        | of topology | changes         |     | : 4           |     |          |     |     |
| Last topology |             | change occurred |     | : 516 seconds | ago |          |     |     |
Port 1/1/1
| Designated     | root        | address |     | : 48:0F:CF:AF:04:76 |         |     |     |     |
| -------------- | ----------- | ------- | --- | ------------------- | ------- | --- | --- | --- |
| Designated     | bridge      | address |     | : 48:0F:CF:AF:04:76 |         |     |     |     |
| Priority       |             |         |     | : 32768             |         |     |     |     |
| BPDUs sent     |             |         |     | : 638               |         |     |     |     |
| BPDUs received |             |         |     | : 9                 |         |     |     |     |
| Message        | expiry      |         |     | : 1 second          |         |     |     |     |
| Forward        | delay       | expiry  |     | : 18                | seconds |     |     |     |
| Forward        | transitions |         |     | : 4                 |         |     |     |     |
| TCN_Tx:        | 10, TCN_Rx: | 10      |     |                     |         |     |     |     |
Port 1/1/2
| Designated | root   | address |     | : 48:0F:CF:AF:04:76 |     |     |     |     |
| ---------- | ------ | ------- | --- | ------------------- | --- | --- | --- | --- |
| Designated | bridge | address |     | : 48:0F:CF:AF:04:76 |     |     |     |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 106

| Priority       |             |         |                     | : 32768    |          |           |         |         |
| -------------- | ----------- | ------- | ------------------- | ---------- | -------- | --------- | ------- | ------- |
| BPDUs sent     |             |         |                     | : 641      |          |           |         |         |
| BPDUs received |             |         |                     | : 11       |          |           |         |         |
| Message        | expiry      |         |                     | : 1 second |          |           |         |         |
| Forward        | delay       | expiry  |                     | : 18       | seconds  |           |         |         |
| Forward        | transitions |         |                     | : 4        |          |           |         |         |
| TCN_Tx:        | 10,         | TCN_Rx: | 10                  |            |          |           |         |         |
| #### MST2      |             |         |                     |            |          |           |         |         |
| Vlans mapped:  |             | 3       |                     |            |          |           |         |         |
| Bridge         |             | Address | : 48:0F:CF:AF:04:76 |            |          | Priority: | 32768   |         |
| Root           |             | Address | : 48:0F:CF:AF:04:76 |            |          | Priority: | 32768   |         |
|                |             | Port    | : 0                 |            |          | Cost      | : 0     |         |
|                |             | Rem     | Hops: 20            |            |          |           |         |         |
| PORT           | ROLE        |         | STATE               | COST       | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx         | TCN-Rx      |         |                     |            |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------         | ----------  |         |                  |                     |         |          |     |     |
| ------------------ | ----------- | ------- | ---------------- | ------------------- | ------- | -------- | --- | --- |
| 1/1/1              | Designated  |         | Forwarding       | 20000               | 128     | P2P Edge | 100 | 60  |
| 20                 | 10          |         |                  |                     |         |          |     |     |
| 1/1/2              | Designated  |         | Forwarding       | 20000               | 128     | P2P      | 100 | 60  |
| 20                 | 10          |         |                  |                     |         |          |     |     |
| 1/1/3              | Designated  |         | Forwarding       | 20000               | 128     | Shr      | 100 | 60  |
| 20                 | 10          |         |                  |                     |         |          |     |     |
| 1/1/4              | Designated  |         | Forwarding       | 20000               | 128     | Shr Edge | 100 | 60  |
| 20                 | 10          |         |                  |                     |         |          |     |     |
| 1/1/5              | Alternate   |         | Loop-Inc         | 20000               | 128     | Shr Edge | 100 | 60  |
| 20                 | 10          |         |                  |                     |         |          |     |     |
| 1/1/6              | Alternate   |         | Root-Inc         | 20000               | 128     | Shr Edge | 100 | 60  |
| 20                 | 10          |         |                  |                     |         |          |     |     |
| Topology           | change      | flag    |                  | : True              |         |          |     |     |
| Number             | of topology |         | changes          | : 4                 |         |          |     |     |
| Last topology      |             | change  | occurred         | : 516 seconds       | ago     |          |     |     |
| Port 1/1/1         |             |         |                  |                     |         |          |     |     |
| Designated         | root        | address |                  | : 48:0F:CF:AF:04:76 |         |          |     |     |
| Designated         | bridge      |         | address          | : 48:0F:CF:AF:04:76 |         |          |     |     |
| Priority           |             |         |                  | : 32768             |         |          |     |     |
| BPDUs sent         |             |         |                  | : 638               |         |          |     |     |
| BPDUs received     |             |         |                  | : 9                 |         |          |     |     |
| Message            | expiry      |         |                  | : 1 second          |         |          |     |     |
| Forward            | delay       | expiry  |                  | : 18                | seconds |          |     |     |
| Forward            | transitions |         |                  | : 3                 |         |          |     |     |
| TCN_Tx:            | 10,         | TCN_Rx: | 10               |                     |         |          |     |     |
| Port 1/1/2         |             |         |                  |                     |         |          |     |     |
| Designated         | root        | address |                  | : 48:0F:CF:AF:04:76 |         |          |     |     |
| Designated         | bridge      |         | address          | : 48:0F:CF:AF:04:76 |         |          |     |     |
| Priority           |             |         |                  | : 32768             |         |          |     |     |
| BPDUs sent         |             |         |                  | : 641               |         |          |     |     |
| BPDUs received     |             |         |                  | : 11                |         |          |     |     |
| Message            | expiry      |         |                  | : 1 second          |         |          |     |     |
| Forward            | delay       | expiry  |                  | : 18                | seconds |          |     |     |
| Forward            | transitions |         |                  | : 3                 |         |          |     |     |
| TCN_Tx:            | 10,         | TCN_Rx: | 10               |                     |         |          |     |     |
| show spanning-tree |             |         | mst<INSTANCE-ID> |                     |         |          |     |     |
Syntax
| show spanning-tree |     | mst | <INSTANCE-ID> | [vsx-peer] |     |     |     |     |
| ------------------ | --- | --- | ------------- | ---------- | --- | --- | --- | --- |
Spanningtreeprotocols|107

Description
DisplaysMSTPconfigurationsforthegiveninstanceID.
Commandcontext
Operator(>)orManager(#)
Parameters
<INSTANCE-ID>
SpecifiestheMSTPinstancenumber.Range:0to64.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch#       | show   | spanning-tree |       | mst               | 1    |          |           |         |         |
| ------------- | ------ | ------------- | ----- | ----------------- | ---- | -------- | --------- | ------- | ------- |
| #### MST1     |        |               |       |                   |      |          |           |         |         |
| Vlans mapped: |        | 1             |       |                   |      |          |           |         |         |
| Bridge        |        | Address       | :     | 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          |        | Address       | :     | 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               |        | Port          | :     | 0                 |      |          | Cost      | : 0     |         |
|               |        | Rem           | Hops: | 20                |      |          |           |         |         |
| PORT          | ROLE   |               | STATE |                   | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        | TCN-Rx |               |       |                   |      |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------         | ----------  |        |                        |     |               |     |          |     |     |
| ------------------ | ----------- | ------ | ---------------------- | --- | ------------- | --- | -------- | --- | --- |
| 1/1/1              | Designated  |        | Forwarding             |     | 20000         | 128 | P2P Edge | 100 | 60  |
| 20                 | 10          |        |                        |     |               |     |          |     |     |
| 1/1/2              | Designated  |        | Forwarding             |     | 20000         | 128 | P2P      | 100 | 60  |
| 20                 | 10          |        |                        |     |               |     |          |     |     |
| 1/1/3              | Designated  |        | Forwarding             |     | 20000         | 128 | Shr      | 100 | 60  |
| 20                 | 10          |        |                        |     |               |     |          |     |     |
| 1/1/4              | Designated  |        | Forwarding             |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20                 | 10          |        |                        |     |               |     |          |     |     |
| 1/1/5              | Alternate   |        | Loop-Inc               |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20                 | 10          |        |                        |     |               |     |          |     |     |
| 1/1/6              | Alternate   |        | Root-Inc               |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20                 | 10          |        |                        |     |               |     |          |     |     |
| Topology           | change      | flag   |                        |     | : True        |     |          |     |     |
| Number             | of topology |        | changes                |     | : 4           |     |          |     |     |
| Last topology      |             | change | occurred               |     | : 516 seconds | ago |          |     |     |
| show spanning-tree |             |        | mst<INSTANCE-ID>detail |     |               |     |          |     |     |
Syntax
| show spanning-tree |     | mst | <INSTANCE-ID> |     | detail | [vsx-peer] |     |     |     |
| ------------------ | --- | --- | ------------- | --- | ------ | ---------- | --- | --- | --- |
Description
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 108

DisplaysMSTPconfigurationsforthegiveninstanceIDwithcorrespondingportdetails.
Commandcontext
Operator(>)orManager(#)
Parameters
<INSTANCE-ID>
SpecifiestheMSTPinstancenumber.Range:0to64.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
| switch# | show | spanning-tree | mst | 1 detail |     |     |     |     |
| ------- | ---- | ------------- | --- | -------- | --- | --- | --- | --- |
#### MST1
| Vlans mapped: |        | 1         |                     |      |          |           |         |         |
| ------------- | ------ | --------- | ------------------- | ---- | -------- | --------- | ------- | ------- |
| Bridge        |        | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          |        | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               |        | Port      | : 0                 |      |          | Cost      | : 0     |         |
|               |        | Rem Hops: | 20                  |      |          |           |         |         |
| PORT          | ROLE   | STATE     |                     | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        | TCN-Rx |           |                     |      |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- ----------
| ----------    | ----------  |                 |     |               |     |          |     |     |
| ------------- | ----------- | --------------- | --- | ------------- | --- | -------- | --- | --- |
| 1/1/1         | Designated  | Forwarding      |     | 20000         | 128 | P2P Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/2         | Designated  | Forwarding      |     | 20000         | 128 | P2P      | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/3         | Designated  | Forwarding      |     | 20000         | 128 | Shr      | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/4         | Designated  | Forwarding      |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/5         | Alternate   | Loop-Inc        |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| 1/1/6         | Alternate   | Root-Inc        |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |                 |     |               |     |          |     |     |
| Topology      | change      | flag            |     | : True        |     |          |     |     |
| Number        | of topology | changes         |     | : 4           |     |          |     |     |
| Last topology |             | change occurred |     | : 516 seconds | ago |          |     |     |
Port 1/1/1
| Designated     | root   | address |     | : 48:0F:CF:AF:04:76 |         |     |     |     |
| -------------- | ------ | ------- | --- | ------------------- | ------- | --- | --- | --- |
| Designated     | bridge | address |     | : 48:0F:CF:AF:04:76 |         |     |     |     |
| Priority       |        |         |     | : 32768             |         |     |     |     |
| BPDUs sent     |        |         |     | : 667               |         |     |     |     |
| BPDUs received |        |         |     | : 9                 |         |     |     |     |
| Message        | expiry |         |     | : 0 second          |         |     |     |     |
| Forward        | delay  | expiry  |     | : 18                | seconds |     |     |     |
Spanningtreeprotocols|109

| Forward | transitions    | : 4 |     |     |     |
| ------- | -------------- | --- | --- | --- | --- |
| TCN_Tx: | 10, TCN_Rx: 10 |     |     |     |     |
Port 1/1/2
| Designated         | root address   | : 48:0F:CF:AF:04:76 |         |     |     |
| ------------------ | -------------- | ------------------- | ------- | --- | --- |
| Designated         | bridge address | : 48:0F:CF:AF:04:76 |         |     |     |
| Priority           |                | : 32768             |         |     |     |
| BPDUs sent         |                | : 670               |         |     |     |
| BPDUs received     |                | : 11                |         |     |     |
| Message            | expiry         | : 0 second          |         |     |     |
| Forward            | delay expiry   | : 18                | seconds |     |     |
| Forward            | transitions    | : 4                 |         |     |     |
| TCN_Tx:            | 10, TCN_Rx: 10 |                     |         |     |     |
| show spanning-tree | mstinterface   |                     |         |     |     |
Syntax
show spanning-tree mst <INSTANCE-ID> interface <IFNAME> [vsx-peer]
Description
ShowsMSTPconfigurationsforthegiveninstanceIDwithcorrespondingportdetails.
Commandcontext
Operator(>)orManager(#)
Parameters
<INSTANCE-ID>
SpecifiestheMSTPinstancenumber.Range:0to64.
<IFNAME>
Specifiesaninterface.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
ShowingMSTconfigurationandportdetails:
switch#
|     | show spanning-tree | mst 1 interface | 1/1/1 |     |     |
| --- | ------------------ | --------------- | ----- | --- | --- |
Port 1/1/1
| Instance | Role | State | Cost | Priority | Vlans mapped |
| -------- | ---- | ----- | ---- | -------- | ------------ |
-------------- -------------- ------------ ---------- ---------- ----------
| 1                  | Designated  | Forwarding | 20000 | 128 | 1   |
| ------------------ | ----------- | ---------- | ----- | --- | --- |
| show spanning-tree | summaryport |            |       |     |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 110

Syntax
| show spanning-tree | summary | port |     |     |
| ------------------ | ------- | ---- | --- | --- |
Description
Showsspanningtreeportsummaryinformation.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingsummaryofspanningtreeports:
| switch#    | show spanning-tree | summary | port      |     |
| ---------- | ------------------ | ------- | --------- | --- |
| STP status |                    |         | : Enabled |     |
| Protocol   |                    |         | : MSTP    |     |
| BPDU guard | timeout            | value   | : None    |     |
BPDU guard enabled interfaces : 1/1/1-1/1/9,1/1/11,1/1/13,1/1/15,1/1/17,1/1/19,
1/1/21,lag1,lag2
| BPDU filter        | enabled     | interfaces  | : None              |     |
| ------------------ | ----------- | ----------- | ------------------- | --- |
| Root guard         | enabled     | interfaces  | : 1/1/3             |     |
| Loop guard         | enabled     | interfaces  | : 1/1/2             |     |
| TCN guard          | enabled     | interfaces  | : 1/1/1-1/1/3       |     |
| Interface          | count by    | state       |                     |     |
| Instance           | ID Blocking | Listening   | Learning Forwarding |     |
| -------------      | --------    | ---------   | -------- ---------- |     |
| 0                  |             | 2           | 0 0                 | 15  |
| 1                  |             | 2           | 0 0                 | 15  |
| 2                  |             | 2           | 0 0                 | 15  |
| -------------      | --------    | ---------   | -------- ---------- |     |
| Total =            | 3           | 6           | 0 0                 | 45  |
| show spanning-tree |             | summaryroot |                     |     |
Syntax
| show spanning-tree | summary | root |     |     |
| ------------------ | ------- | ---- | --- | --- |
Description
Showsspanningtreerootsummaryinformation.
Commandcontext
Operator(>)orManager(#)
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Spanningtreeprotocols|111

Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Showingspanningtreerootsummary:
| switch# show | spanning-tree |              | summary root        |            |         |           |
| ------------ | ------------- | ------------ | ------------------- | ---------- | ------- | --------- |
| STP status   |               |              | : Enabled           |            |         |           |
| Protocol     |               |              | : MSTP              |            |         |           |
| System ID    |               |              | : 70:72:cf:32:50:f5 |            |         |           |
| Root bridge  | for           | STP Instance | : 0,1,2             |            |         |           |
|              |               |              |                     | Root Hello | Max Fwd |           |
| Instance     | ID            | Priority     | Root ID             | cost Time  | Age Dly | Root Port |
--------------- -------- ----------------- --------- ----- --- --- ------------
| 0   |     | 32768 | 70:72:cf:32:50:f5 | 0   | 2 20 15 | n/a   |
| --- | --- | ----- | ----------------- | --- | ------- | ----- |
| 1   |     | 32768 | 70:72:cf:32:50:f5 | 0   | 2 20 15 | n/a   |
| 2   |     | 32768 | 70:72:cf:32:50:f5 | 200 | 2 20 15 | 1/1/1 |
spanning-tree
Syntax
spanning-tree
no spanning-tree
Description
Enablesthespanningtreeprotocolontheswitch.
Thenoformofthiscommanddisablesthespanningtreeprotocolontheswitch.
Commandcontext
config
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Enablingspanningtree:
| switch(config)# |     | spanning-tree |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | --- | --- |
Disablingspanningtree:
| switch(config)# |             | no spanning-tree |     |     |     |     |
| --------------- | ----------- | ---------------- | --- | --- | --- | --- |
| spanning-tree   | bdpu-filter |                  |     |     |     |     |
Syntax
| spanning-tree    | bdpu-filter |     |     |     |     |     |
| ---------------- | ----------- | --- | --- | --- | --- | --- |
| no spanning-tree | bdpu-filter |     |     |     |     |     |
Description
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 112

Enables the BDPU filter for the interface.

The BPDU filter feature allows control of spanning tree participation on a per-port basis. It can be used to
exclude specific ports from becoming part of spanning tree operations. A port with the BPDU filter enabled
will ignore incoming BPDU packets and stay locked in the spanning tree forwarding state. All other ports
maintain their role. Typical uses for this parameter include:

n To have MSTP operations running on selected ports of the switch rather than every port of the switch at

a time.

n To prevent the spread of errant BPDU frames.

n To eliminate the need for a topology change when a port's link status changes. For example, ports that
connect to servers and workstations can be configured to remain outside of spanning tree operations.

n To protect the network from denial of service attacks that use spoofing BPDUs by dropping incoming
BPDU frames. For this scenario, BPDU protection offers a more secure alternative, implementing port
shut down and a detection alert when errant BPDU frames are received.

Ports configured with the BPDU filter mode remain active (learning and forward frames). However, spanning tree

cannot receive or transmit BPDUs on the port. The port remains in a forwarding state, permitting all broadcast

traffic. This can create a network storm if there are any loops (that is, redundant links) using these ports. If you

suddenly have a high load, disconnect the link and disable the BPDU filter (using the no command.)

The no form of the command sets the BDPU filter status to the default of disabled on the interface.

Command context

config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

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

Spanning tree protocols | 113

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

On the 6400 Switch Series, interface identification differs.

Enabling the BPDU guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree bpdu-guard

Disabling BPDU guard on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree bpdu-guard

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

<INTERVAL>

Specifies the re-enable timeout in seconds. Range: 1 to 65535.

Authority

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

114

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingtheBPDUguardtimeoutoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1         |     |            |            |
| ------------------ | --- | --------- | ------------- | --- | ---------- | ---------- |
| switch(config-if)# |     |           | spanning-tree |     | bpdu-guard | timeout 10 |
DisablingBPDUguardtimeoutoninterface1/1/1:
| switch(config)#    |             | interface | 1/1/1            |     |            |     |
| ------------------ | ----------- | --------- | ---------------- | --- | ---------- | --- |
| switch(config-if)# |             |           | no spanning-tree |     | bpdu-guard |     |
| spanning-tree      | config-name |           |                  |     |            |     |
Syntax
| spanning-tree    | config-name |             | <CONFIG-NAME>   |     |     |     |
| ---------------- | ----------- | ----------- | --------------- | --- | --- | --- |
| no spanning-tree |             | config-name | [<CONFIG-NAME>] |     |     |     |
Description
SetstheconfigurationnamefortheMSTregioninwhichtheswitchresides.
AllswitcheswithinanMSTregionmusthaveidenticalconfigurationnames.FormorethanoneMSTPswitch
inthesameMSTregion,theidenticalregionnamemustbeconfiguredonallsuchswitches.Ifthedefault
configurationnameisretainedonaswitch,itcannotexistinthesameMSTregionwithanotherswitch.
Thenoformofthiscommandoverwritesthecurrentlyconfigurednamewiththedefaultname.Thedefault
nameisatextstringusingthehexadecimalrepresentationofthesystemMACaddress.
Commandcontext
config
Parameters
<CONFIG-NAME>
SpecifiestheconfigurationnamefortheMSTregioninwhichtheswitchresides.Default:textstring
usingthehexadecimalrepresentationoftheMACaddressoftheswitch.Range:1-32nonblank
characters(case-sensitive).
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
SettingtheconfigurationnametoMST0:
| switch(config)# |     | spanning-tree |     | config-name |     | MST0 |
| --------------- | --- | ------------- | --- | ----------- | --- | ---- |
Settingtheconfigurationnametothedefaultvalue:
| switch(config)# |     | no  | spanning-tree |     | config-name |     |
| --------------- | --- | --- | ------------- | --- | ----------- | --- |
Spanningtreeprotocols|115

| spanning-tree | config-revision |     |     |
| ------------- | --------------- | --- | --- |
Syntax
| spanning-tree    | config-revision | <REVISION-NUMBER>   |     |
| ---------------- | --------------- | ------------------- | --- |
| no spanning-tree | config-revision | [<REVISION-NUMBER>] |     |
Description
ConfigurestherevisionnumberfortheMSTregioninwhichtheswitchresides.AllswitcheswithinanMST
regionmusthaveidenticalrevisionnumbers.Usethissettingtodifferentiatebetweenregion
configurations.Forexample,whenchangingconfigurationsettingswithinaregionwhereyouwanttotrack
theconfigurationversionsyouuse,orwhencreatinganewregionfromasubsetofswitchesinacurrent
regionandyouwanttomaintainthesameregionname.
ThenoformofthiscommandoverwritesthecurrentlyconfiguredrevisionnumberoftheMSTregionand
setsittothedefaultvalueof0.
Commandcontext
config
Parameters
<REVISION-NUMBER>
SpecifiestherevisionnumberfortheMSTregioninwhichtheswitchresides.Range:0-65535.Default:
0.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingtherevisionto40:
| switch(config)# | spanning-tree | config-revision | 40  |
| --------------- | ------------- | --------------- | --- |
Settingtherevisiontothedefaultvalue:
| switch(config)# | no spanning-tree | config-revision |     |
| --------------- | ---------------- | --------------- | --- |
| spanning-tree   | cost             |                 |     |
Syntax
| spanning-tree    | cost <PORT-COST>   |     |     |
| ---------------- | ------------------ | --- | --- |
| no spanning-tree | cost [<PORT-COST>] |     |     |
Description
SetsindividualportcostforMSTI0.
Foragivenport,thepathcostsettingcanbedifferentfordifferentMSTIstowhichtheportmaybelong.
TheswitchusesthepathcosttodeterminewhichportsaretheforwardingportsintheMSTI;thatis,which
linkstousefortheactivetopologyoftheMSTIandwhichportstoblock.
ThenoformofthecommandsetstheportcostforMSTI0instancetothedefaultvalue.
Commandcontext
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 116

config-if

Parameters

<PORT-COST>

Specifies the cost of the port for MSTI 0. Range: 1-200,000,000. Default is calculated from the port link
speed:

n 10 Mbps link speed equals a path cost of 2,000,000.

n 100 Mbps link speed equals a path cost of 200,000.

n 1 Gbps link speed equals a path cost of 20,000.

n 2 Gbps link speed equals a path cost of 10,000.

n 10 Gbps link speed equals a path cost of 2,000.

n 100 Gbps link speed equals a path cost of 200.

n 1 Tbps link speed equals a path cost of 20.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Setting the cost to 2000 on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree cost 2000

Setting the cost to the default on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# no spanning-tree cost

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

Spanning tree protocols | 117

Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingforwarddelayto6seconds:
| switch(config)# |     | spanning-tree |     | forward-delay |     | 6   |
| --------------- | --- | ------------- | --- | ------------- | --- | --- |
Settingforwarddelaytothedefaultof15seconds:
| switch(config)# |            | no  | spanning-tree |     | forward-delay |     |
| --------------- | ---------- | --- | ------------- | --- | ------------- | --- |
| spanning-tree   | hello-time |     |               |     |               |     |
Syntax
| spanning-tree    | hello-time |            | <HELLO-IN-SECS>   |     |     |     |
| ---------------- | ---------- | ---------- | ----------------- | --- | --- | --- |
| no spanning-tree |            | hello-time | [<HELLO-IN-SECS>] |     |     |     |
Description
ConfiguresthetransmissionintervalbetweenconsecutiveBridgeProtocolDataUnits(BPDU)thatthe
switchsendsasarootbridge.ThehellotimeintervalisinsertedinoutboundBPDUs.
Thenoformofthiscommandsetshellotimetothedefaultof2seconds.
Commandcontext
config
Parameters
<HELLO-IN-SECS>
Specifiesthehellotimeintervalinseconds.Default:2seconds.Range:2-10.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthehellotimeintervalto6seconds:
| switch(config)# |     | spanning-tree |     | hello-time |     | 6   |
| --------------- | --- | ------------- | --- | ---------- | --- | --- |
Settingthehellotimeintervaltothedefaultof2seconds:
| switch(config)# |          | no  | spanning-tree |     | hello-time |     |
| --------------- | -------- | --- | ------------- | --- | ---------- | --- |
| spanning-tree   | instance |     | cost          |     |            |     |
Syntax
| spanning-tree    | instance |          | <INSTANCE-ID> |     | cost <PORT-COST> |               |
| ---------------- | -------- | -------- | ------------- | --- | ---------------- | ------------- |
| no spanning-tree |          | instance | <INSTANCE-ID> |     | cost             | [<PORT-COST>] |
Description
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 118

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

Specifies the cost of the port for the MSTI. Range: 1-200000000. Default value is calculated from the
port link speed:

n 10 Mbps link speed equals a path cost of 2000000.

n 100 Mbps link speed equals a path cost of 200000.

n 1 Gbps link speed equals a path cost of 20000.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Setting the port 1/1/1 cost for MSTI 1 to 2000:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree instance 1 cost 2000

Setting the port 1/1/1 cost for MSTI 1 to the default:

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

Spanning tree protocols | 119

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

On the 6400 Switch Series, interface identification differs.

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

120

Examples
Settingtheprioritymultiplierforinstance1to5:
switch(config)#
|     |     | spanning-tree |     | instance | 1   | priority 5 |
| --- | --- | ------------- | --- | -------- | --- | ---------- |
Settingtheprioritymultiplierforinstance1tothedefaultof8:
| switch(config)# |          | no  | spanning-tree |     | instance | 1 priority |
| --------------- | -------- | --- | ------------- | --- | -------- | ---------- |
| spanning-tree   | instance |     | vlan          |     |          |            |
Syntax
| spanning-tree    | instance |          | <INSTANCE-ID> |     | vlan <VLAN-ID> |           |
| ---------------- | -------- | -------- | ------------- | --- | -------------- | --------- |
| no spanning-tree |          | instance | <INSTANCE-ID> |     | vlan           | <VLAN-ID> |
Description
CreatesanewinstancewithVLANsmappedormapsVLANstoanexistinginstance.
EachinstancemusthaveatleastoneVLANmappedtoit.WhenVLANsaremappedtoaninstance,theyare
automaticallyunmappedfromtheinstancetheyweremappedtobefore.AnyMSTPinstancecanhaveall
theVLANsconfiguredontheswitch.
ThenoformofthiscommandremovesthespecifiedVLANfromtheMSTPinstance.
Commandcontext
config
Parameters
<INSTANCE-ID>
SpecifiestheMSTPinstancenumber.Range:1to64.
<VLAN-ID>
SpecifiesaVLANIDnumber.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
MappingVLAN1toinstance1:
| switch(config)# |     | spanning-tree |     | instance | 1   | vlan 1 |
| --------------- | --- | ------------- | --- | -------- | --- | ------ |
RemovingVLAN1frominstance1:
| switch(config)# |           | no  | spanning-tree |     | instance | 1 vlan 1 |
| --------------- | --------- | --- | ------------- | --- | -------- | -------- |
| spanning-tree   | link-type |     |               |     |          |          |
Syntax
| spanning-tree | link-type |     | {point-to-point|shared} |     |     |     |
| ------------- | --------- | --- | ----------------------- | --- | --- | --- |
Spanningtreeprotocols|121

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

On the 6400 Switch Series, interface identification differs.

Setting the link type to point-to-point on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# spanning-tree link-type point-to-point

Setting the link type to shared on interface 1/1/1:

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

122

Loopguardcausesthenon-designatedporttogointotheMSTPloopinconsistentstateinsteadofthe
forwardingstate.IntheloopinconsistentstatetheportpreventsdatatrafficandBPDUtransmission
throughthelink,thereforeavoidingtheloopcreation.WhenBPDUsagainarereceivedontheinconsistent
port,itresumesnormalMSTPoperationautomatically.
Inthisexample,thetransmissionfromswitch1port10toswitch2prt20isblockedduetoahardware
failure.Switch2port2doesnotrecieveBPDUsandgoesintoaforwardingstate,creatingaloop.
Whenloopguardisconfiguredforswitch2port20,thisportgoesfromaforwardingstatetoan
inconsistentstate,anddoesnotforwardthetrafficthroughthelink,thusavoidingloopcreation.
Examples
Enablingtheloopguardoninterface1/1/1:
| switch(config)#    | interface     | 1/1/1 |            |
| ------------------ | ------------- | ----- | ---------- |
| switch(config-if)# | spanning-tree |       | loop-guard |
Disablingloopguardoninterface1/1/1:
| switch(config)#       | interface        | 1/1/1 |            |
| --------------------- | ---------------- | ----- | ---------- |
| switch(config-if)#    | no spanning-tree |       | loop-guard |
| spanning-tree max-age |                  |       |            |
Syntax
| spanning-tree max-age | <AGE-IN-SECS>           |     |     |
| --------------------- | ----------------------- | --- | --- |
| no spanning-tree      | max-age [<AGE-IN-SECS>] |     |     |
Description
Setsthemaximumagetimer,whichspecifiesthemaximumagevaluethattheswitchinsertsinoutbound
BPDUpacketsitsendsasarootbridge.Max-ageistheinterval,specifiedintheBPDU,thatBPDUdata
remainsvalidafteritsreception.
ThebridgerecomputesthespanningtreetopologyifitdoesnotreceiveanewBPDUbeforemax-age
expiry.
Thenoformofthiscommandsetsthemax-agevaluetothedefaultof20seconds.
Commandcontext
config
Spanningtreeprotocols|123

Parameters
<AGE-IN-SECS>
Specifiesthemax-ageinseconds.Range:6to40.Default:20.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthemax-ageto10seconds:
| switch(config)# | spanning-tree | max-age 10 |
| --------------- | ------------- | ---------- |
Settingthemax-agetothedefaultof20seconds:
| switch(config)#        | no spanning-tree | max-age |
| ---------------------- | ---------------- | ------- |
| spanning-tree max-hops |                  |         |
Syntax
| spanning-tree max-hops | <HOP-COUNT>            |     |
| ---------------------- | ---------------------- | --- |
| no spanning-tree       | max-hops [<HOP-COUNT>] |     |
Description
ConfiguresthemaxhopsettingthattheswitchinsertsintoBPDUsthatitsendsoutastherootbridge.The
maxhopsettingdeterminesthenumberofbridgesinanMSTregionthataBPDUcantraversebeforeitis
discarded.
Thenoformofthiscommandsetsthemaximumnumberofhopstothedefaultof20.
Commandcontext
config
Parameters
<HOP-COUNT>
Specifiesthemaximumnumberofhops.Range:1to40.Default:20.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthehopcountto10:
| switch(config)# | spanning-tree | max-hops 10 |
| --------------- | ------------- | ----------- |
Settingthemax-agetothedefaultof20:
| switch(config)# | no spanning-tree | max-hops |
| --------------- | ---------------- | -------- |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 124

spanning-tree mode

Syntax

spanning-tree mode {mstp|rpvst}

Description

Sets the spanning tree mode to either MSTP mode (Multiple-instance Spanning Tree Protocol) or RPVST
mode (Rapid Per VLAN Spanning Tree).

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

switch(config)# spanning-tree mode rpvst

spanning-tree port-priority

Syntax

spanning-tree port-priority <PRIORITY-MULTIPLIER>
no spanning-tree port-priority [<PRIORITY-MULTIPLIER>]

Description

Configures the port priority. The priority of a port can be different for each MST instance to which it
belongs.

The no form of the command sets the port priority for MST instance 0 to the default of 8. The default
priority value is derived by multiplying 8 by 8. For LAG interfaces the default is 4.

Command context

config-if

Parameters

<PRIORITY-MULTIPLIER>

Spanning tree protocols | 125

Specifies the port priority as a multiplier. Default: 8, except for LAG interfaces where the default is 4.
Range: 0 to15.

The priority range for a port in a given MSTI is 0 to 255. However, this command specifies the priority as
a multiplier (0 to 15) of 16. When you specify a priority multiplier of 0 to15, the actual priority assigned
to the switch is: (priority-multiplier) x 16.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

126

Onthe6400SwitchSeries,interfaceidentificationdiffers.
Settingtheporttypetoadmin-edgeoninterface1/1/1:
| switch(config)#    | interface     | 1/1/1 |                      |
| ------------------ | ------------- | ----- | -------------------- |
| switch(config-if)# | spanning-tree |       | port-type admin-edge |
Settingtheporttypetoadmin-networkoninterface1/1/1:
| switch(config)#    | interface     | 1/1/1 |                         |
| ------------------ | ------------- | ----- | ----------------------- |
| switch(config-if)# | spanning-tree |       | port-type admin-network |
Settingtheporttypetothedefaultofadmin-networkoninterface1/1/1:
| switch(config)#        | interface        | 1/1/1 |           |
| ---------------------- | ---------------- | ----- | --------- |
| switch(config-if)#     | no spanning-tree |       | port-type |
| spanning-tree priority |                  |       |           |
Syntax
| spanning-tree priority | <PRIORITY-MULTIPLIER> |                         |     |
| ---------------------- | --------------------- | ----------------------- | --- |
| no spanning-tree       | priority              | [<PRIORITY-MULTIPLIER>] |     |
Description
Configurestheswitch(bridge)priorityforthedesignatedregioninwhichtheswitchresides.
Theswitchcomparesthisprioritywiththeprioritiesofotherswitchesinthesameregiontodeterminethe
rootswitchfortheregion.Thelowerthepriorityvalue,thehigherthepriority.
Thenoformofthiscommandsetsthebridgeprioritytothedefaultof8.Thedefaultpriorityvalueisderived
bymultiplying8by4096.
Commandcontext
config
Parameters
<PRIORITY-MULTIPLIER>
Specifiesthepriorityasamultiplier.Range:0to15.Default:8.
ThepriorityrangeforanMSTPswitchis0-61440.However,thiscommandspecifiesthepriorityasa
multiplier(0to15)of4096.Thatis,whenyouspecifyaprioritymultipliervalueof0to15,theactual
priorityassignedtotheswitchis:(priority-multiplier)x4096.Forexample,with2asthepriority-
multiplieronagivenMSTPswitch,theswitchprioritysettingis8,192.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Usage
EveryswitchrunninganinstanceofMSTPhasaBridgeIdentifier,whichisauniqueidentifierthathelps
distinguishthisswitchfromallothers.TheswitchwiththelowestBridgeIdentifieriselectedastherootfor
thetree.TheBridgeIdentifieriscomposedofaconfigurableprioritycomponent(2bytes)andthebridge's
MACaddress(6bytes).Youcanchangetheprioritycomponentprovidesflexibilityindeterminingwhich
switchwillbetherootforthetree,regardlessofitsMACaddress.
Spanningtreeprotocols|127

Examples
Settingtheprioritymultiplierto12:
switch(config)#
|     | spanning-tree | priority | 12  |
| --- | ------------- | -------- | --- |
Settingtheprioritymultipliertothedefaultof8:
| switch(config)#          | no spanning-tree |     | priority |
| ------------------------ | ---------------- | --- | -------- |
| spanning-tree root-guard |                  |     |          |
Syntax
| spanning-tree root-guard |            |     |     |
| ------------------------ | ---------- | --- | --- |
| no spanning-tree         | root-guard |     |     |
Description
Enablestherootguardontheinterface.
Whenaportisenabledasroot-guard,itcannotbeselectedastherootportevenifitreceivessuperiorSTP
BPDUs.Theportisassignedan"alternate"portroleandentersablockingstateifitreceivessuperiorMSTP
BPDUs.
AsuperiorBPDUcontainsboth"better"informationontherootbridgeandpathcosttotherootbridge,
whichwouldnormallyreplacethecurrentrootbridgeselection.
Thenoformofthecommandsetstherootguardstatustothedefaultofdisabledontheinterface.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Enablingtherootguardoninterface1/1/1:
| switch(config)#    | interface     | 1/1/1 |            |
| ------------------ | ------------- | ----- | ---------- |
| switch(config-if)# | spanning-tree |       | root-guard |
Disablingrootguardoninterface1/1/1:
| switch(config)#            | interface        | 1/1/1 |            |
| -------------------------- | ---------------- | ----- | ---------- |
| switch(config-if)#         | no spanning-tree |       | root-guard |
| spanning-tree rpvst-filter |                  |       |            |
Syntax
| spanning-tree rpvst-filter |              |     |     |
| -------------------------- | ------------ | --- | --- |
| no spanning-tree           | rpvst-filter |     |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 128

Description
EnablestheRPVSTfilterfortheinterface.
WhentheRPVSTfilterisenabled,theingressingRPVSTproprietaryBPDUsaredroppedaftercopyingtoCPU
whereasthestandardIEEERPVSTBPDUsarestillallowed.ThishelpsinpreventingthefloodingofRPVST
proprietaryBPDUsunderanMSTP-RPVSTinteropenvironment.
IftheneighboringswitchisrunningRPVSTthenthispairofswitcheswillnotconvergeasRPVSTBPDUswillnot
reachthem.
IfenablingRPVSTfiltercausesahightrafficload,shutdowntheportandreconfiguretheBPDUfilterwith
| theCLIcommand:no | spanning | tree | rpvst-filter. |
| ---------------- | -------- | ---- | ------------- |
RPVSTfilterisdisabledbydefault.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingtheRPVSTfilteroninterface1/1/1:
| switch# configure  | terminal      |       |              |
| ------------------ | ------------- | ----- | ------------ |
| switch(config)#    | interface     | 1/1/1 |              |
| switch(config-if)# | spanning-tree |       | rpvst-filter |
DisablingRPVSTfilteroninterface1/1/1:
| switch# configure         | terminal         |       |              |
| ------------------------- | ---------------- | ----- | ------------ |
| switch(config)#           | interface        | 1/1/1 |              |
| switch(config-if)#        | no spanning-tree |       | rpvst-filter |
| spanning-tree rpvst-guard |                  |       |              |
Syntax
| spanning-tree rpvst-guard |             |     |     |
| ------------------------- | ----------- | --- | --- |
| no spanning-tree          | rpvst-guard |     |     |
Description
EnablesRPVSTguardontheswitchinterface.WhenRPVSTguardisenabledonaninterface,itwilldisable
thatinterfaceifRPVSTBPDUsarereceivedonit.
ThenoformofthecommandsetstheRPVSTguardstatustothedefaultofdisabledontheinterface.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Spanningtreeprotocols|129

Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingRPVSTguardoninterface1/1/1:
| switch#            | configure | terminal        |             |     |     |
| ------------------ | --------- | --------------- | ----------- | --- | --- |
| switch(config)#    |           | interface 1/1/1 |             |     |     |
| switch(config-if)# |           | spanning-tree   | rpvst-guard |     |     |
DisablingRPVSTguardoninterface1/1/1:
| switch#         | configure | terminal        |     |     |     |
| --------------- | --------- | --------------- | --- | --- | --- |
| switch(config)# |           | interface 1/1/1 |     |     |     |
switch(config-if)#
|               |                            | no spanning-tree |     | rpvst-guard |     |
| ------------- | -------------------------- | ---------------- | --- | ----------- | --- |
| spanning-tree | rpvst-mstpinterconnectvlan |                  |     |             |     |
Syntax
| spanning-tree    | rpvst-mstp-interconnect-vlan |     |     | <VLAN-ID> |     |
| ---------------- | ---------------------------- | --- | --- | --------- | --- |
| no spanning-tree | rpvst-mstp-interconnect-vlan |     |     |           |     |
Description
ConfigurestheVLANthathastobeusedtointerconnectRPVSTandMSTPdomains.VLAN1isusedby
default.
ThenoformofthiscommandremovestheVLANconfiguration.
ItisrequiredtocreatetheinterconnectVLANandthenconfigureRPVSTspanningtreeonit.
n
n ThesameinterconnectVLANmustbekeptonalltheswitchesinthenetwork.
n AddingordeletingtheinterconnectVLANtriggersare-convergenceinthenetwork.
n DeletingaVLANthatisconfiguredastheinterconnectVLANdoesnotresetthevaluetothedefault.
Commandcontext
config
Parameters
<VLAN-ID>
SpecifiesthenumberofaVLAN.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
ThisexampleconfiguresVLAN10tousedtointerconnectRPVSTandMSTPdomains.
| switch#(config)# |           | spanning-tree | rpvst-mstp-interconnect-vlan |     | 10  |
| ---------------- | --------- | ------------- | ---------------------------- | --- | --- |
| spanning-tree    | tcn-guard |               |                              |     |     |
Syntax
| spanning-tree | tcn-guard |     |     |     |     |
| ------------- | --------- | --- | --- | --- | --- |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 130

| no spanning-tree |     | tcn-guard |     |     |
| ---------------- | --- | --------- | --- | --- |
Description
EnablestheTCN(TopologyChangeNotification)guardintheinterface.Whenenabledforaport,theport
stopspropagatingreceivedtopologychangenotificationsandtopologychangestootherports.
ThenoformofthecommandsetstheTCNguardstatustothedefaultofdisabledontheinterface.
Commandcontext
config-if
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingTCNguardoninterface1/1/1:
| switch(config)#    |     | interface     | 1/1/1 |           |
| ------------------ | --- | ------------- | ----- | --------- |
| switch(config-if)# |     | spanning-tree |       | tcn-guard |
DisablingTCNguardoninterface1/1/1:
| switch(config)#    |                     | interface        | 1/1/1 |           |
| ------------------ | ------------------- | ---------------- | ----- | --------- |
| switch(config-if)# |                     | no spanning-tree |       | tcn-guard |
| spanning-tree      | transmit-hold-count |                  |       |           |
Syntax
| spanning-tree    | transmit-hold-count |                     |     | <COUNT>   |
| ---------------- | ------------------- | ------------------- | --- | --------- |
| no spanning-tree |                     | transmit-hold-count |     | [<COUNT>] |
Description
SetsthemaximumnumberofBPDUspersecondthattheswitchcansendfromaninterface.
Thenoformofthiscommandsetsthetransmit-hold-counttothedefaultof6.
Commandcontext
config
Parameters
<COUNT>
SpecifiesthenumberofBPDUsthatcanbesentpersecond.Range:1to10.Default:6.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Settingthetransmit-hold-countto5:
Spanningtreeprotocols|131

switch(config)# spanning-tree transmit-hold-count 5

Setting the transmit-hold-count to the default of 6:

switch(config)# no spanning-tree transmit-hold-count

spanning-tree trap

Syntax

spanning-tree trap {new-root|topology-change [instance <0-64>] | errant-bpdu |

root-guard-inconsistency | loop-guard-inconsistency}

no spanning-tree trap {new-root|topology-change [instance <0-64>] | errant-bpdu |

root-guard-inconsistency | loop-guard-inconsistency}

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

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

132

| switch(config)# | spanning-tree | trap topology-change |     |
| --------------- | ------------- | -------------------- | --- |
EnablingSNMPnotificationwhenatopologychangeeventoccursoninstance1:
| switch(config)# | spanning-tree | trap topology-change | instance 1 |
| --------------- | ------------- | -------------------- | ---------- |
DisablingSNMPtrapswhenatopologychangeeventnotificationoccursoninstance1:
| switch(config)# | no spanning-tree | trap topology-change | instance 1 |
| --------------- | ---------------- | -------------------- | ---------- |
Spanningtreeprotocols|133

Chapter 7

MVRP

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

Each MRP-enabled interface is called an MRP participant, and each MVRP-enabled interface is called an MVRP
participant. When the VLAN configuration on an MVRP participant changes, it sends a Protocol Data Unit
(PDU) to notify other MVRP participants to register and deregister the changed VLAN. MRP rapidly
propagates the configuration information of an MRP participant throughout the layer 2 network.

MRP registers and deregisters VLAN attributes as follows:

n When an interface receives a declaration for a VLAN, the interface registers the VLAN and joins the VLAN.

n When an interface receives a withdrawal for a VLAN, the interface deregisters the VLAN and leaves the

VLAN.

MVRP only applies to trunk interfaces.

MVRP functionality and limitations

MIB support

The MVRP feature supports objects in the following standard MIBs:

n IEEE8021-Q-BRIDGE-MIB (Version 200810150000Z)

n IEEE8021-BRIDGE-MIB (Version 200810150000Z)

It also supports MVRP objects in the HPE proprietary MIB:

HPE-MVRP-MIB (hpeMvrp.mib)

MVRP limitations

n MVRP is only supported on L2 trunk ports.

n MVRP and VLAN translation cannot be enabled on the same interface.

n MVRP will propagate only the first 1024 VLANs. This number includes existing static VLANs locally. For

example, if a peer device already has 100 static VLANs, then it can only learn 924 VLANs.

n MVRP and PVST cannot be enabled at the same time.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

134

n For security purposes, MVRP is disabled by default. MVRP packets are blocked on MVRP disabled ports,

but can be enabled on ports that are security enabled.

n MVRP supports 1024 VLANs and 512 logical ports.

n If MVRP is enabled globally, MVRP is automatically enabled on LAG interfaces and cannot be disabled.

MRP messages
MRP messages include the following types:

n Declaration: Includes Join and New messages.

n Withdrawal: Includes Leave and LeaveAll messages.

Join message

An MRP participant sends a Join message to request the peer participant to register attributes in the Join
message.

When receiving a Join message from the peer participant, an MRP participant performs the following tasks:

n Registers the attributes in the Join message.

n Propagates the Join message to all other participants on the device.

After receiving the Join message, other participants send the Join message to their respective peer
participants.

Join messages sent from a local participant to its peer participant include the following types:

n JoinEmpty: Declares an unregistered attribute. For example, when an MRP participant joins an

unregistered static VLAN, it sends a JoinEmpty message. VLANs created manually and locally are called
static VLANs. VLANs learned through MRP are called dynamic VLANs.

n JoinIn: Declares a registered attribute. A JoinIn message is used in one of the following situations:

o An MRP participant joins an existing static VLAN and sends a JoinIn message after registering the

VLAN.

o The MRP participant receives a Join message propagated by another participant on the device and

sends a JoinIn message after registering the VLAN.

New message

Similar to a Join message, a New message enables MRP participants to register attributes.

When the MSTP topology changes, an MRP participant sends a New message to the peer participant to
declare the topology change.

Upon receiving a New message from the peer participant, an MRP participant performs the following tasks:

n Registers the attributes in the message.

n Propagates the New message to all other participants on the device.

After receiving the New message, other participants send the New message to their respective peer
participants.

Leave message

An MRP participant sends a Leave message to the peer participant when it wants the peer participant to
deregister attributes that it has deregistered.

MVRP | 135

When the peer participant receives the Leave message, it performs the following tasks:

n Deregisters the attribute in the Leave message.

n Propagates the Leave message to all other participants on the device.

After a participant on the device receives the Leave message, it determines whether to send the Leave
message to its peer participant depending on the attribute status on the device.

n If the VLAN in the Leave message is a dynamic VLAN not registered by any participants on the device,

both of the following events occur:

o The VLAN is deleted on the device.

o The participant sends the Leave message to its peer participant.

n If the VLAN in a Leave message is a static VLAN, the participant will not send the Leave message to its

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

Prerequisites

MVRP must be enabled globally to facilitate dynamic VLAN learning.

Procedure

1. Enable MVRP globally on all interfaces or only for specific interfaces with the command mvrp. (For

Dynamic LAGs, MVRP is enabled by default).

2. By default, MVRP supports dynamic registration and deregistration of VLANs on all interfaces. If
required, customize the behavior for each interface with the command mvrp registration.

3.

If required, adjust the MVRP timers from their default values with the command mvrp timer. To
avoid frequent registrations and deregistrations, use the same MVRP timer values throughout the
network.

4. Review your MVRP configuration settings with the commands show mvrp config, show mvrp state,

and show mvrp statistics.

Example

On the 6400 Switch Series, interface identification differs.

This example creates the following configuration:

n Enables MVRP on all interfaces.

n Sets interface 1/1/1 to ignore VLAN 100.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

136

| switch(config)# |     |     | mvrp |     |     |     |     |
| --------------- | --- | --- | ---- | --- | --- | --- | --- |
switch(config)#
|                    |          |           | interface    | 1/1/1             |       |           |                   |
| ------------------ | -------- | --------- | ------------ | ----------------- | ----- | --------- | ----------------- |
| switch(config-if)# |          |           |              | mvrp registration |       | forbidden | 100               |
| switch(config-if)# |          |           |              | mvrp              |       |           |                   |
| switch(config-if)# |          |           |              | quit              |       |           |                   |
| switch#            | show     | mvrp      | config       |                   |       |           |                   |
| Configuration      |          |           | and Status   | - MVRP            |       |           |                   |
| Global             | MVRP     | status    |              | : Disabled        |       |           |                   |
| Port               | Status   |           | Registration |                   | Join  | Leave     | LeaveAll Periodic |
|                    |          |           | Type         |                   | Timer | Timer     | Timer Timer       |
| -------            | -------- |           | --------     |                   | ----- | -----     | ------ --------   |
| 1/1/1              | Disabled |           | Normal       |                   | 20    | 300       | 1000 100          |
| switch#            | show     | mvrp      | state        | 1/1/1             |       |           |                   |
| Configuration      |          |           | and Status   | - MVRP            | state | for       | VLAN 1            |
| Port               | VLAN     | Registrar |              | Applicant         |       |           |                   |
|                    |          | State     |              | State             |       |           |                   |
| -----              | ----     | --------  |              | ---------         |       |           |                   |
| 1/1/1              | 1        | MT        |              | QA                |       |           |                   |
| MVRP               | scenario |           |              | 1                 |       |           |                   |
ThisscenarioillustratestheconfigurationofasimpleMVRPdeployment.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. OnswitchA,enableMVRPglobally,defineVLANsoninterface1/1/1and1/1/2,andenableMVRPon
eachinterface.
|     | switch#            |     | config |           |          |     |     |
| --- | ------------------ | --- | ------ | --------- | -------- | --- | --- |
|     | switch(config)#    |     |        | mvrp      |          |     |     |
|     | switch(config)#    |     |        | interface | 1/1/1    |     |     |
|     | switch(config-if)# |     |        | no        | shutdown |     |     |
MVRP|137

| switch(config-if)# |           | vlan        | trunk native | 1   |     |     |     |
| ------------------ | --------- | ----------- | ------------ | --- | --- | --- | --- |
| switch(config-if)# |           | mvrp        |              |     |     |     |     |
| switch(config-if)# |           | exit        |              |     |     |     |     |
| switch(config)#    | interface |             | 1/1/2        |     |     |     |     |
| switch(config-if)# |           | no shutdown |              |     |     |     |     |
| switch(config-if)# |           | vlan        | trunk native | 1   |     |     |     |
| switch(config-if)# |           | mvrp        |              |     |     |     |     |
2. OnswitchB,enableMVRPglobally,defineVLANs10and20,assignatrunknativeVLANtointerface
1/1/3,andenableMVRPonthisinterface.
| switch# config     |           |             |       |     |     |     |     |
| ------------------ | --------- | ----------- | ----- | --- | --- | --- | --- |
| switch(config)#    | mvrp      |             |       |     |     |     |     |
| switch(config)#    | vlan      | 10          |       |     |     |     |     |
| switch(config)#    | vlan      | 20          |       |     |     |     |     |
| switch(config)#    | interface |             | 1/1/3 |     |     |     |     |
| switch(config-if)# |           | no shutdown |       |     |     |     |     |
switch(config-if)#
|                    |     | vlan | trunk native | 1   |     |     |     |
| ------------------ | --- | ---- | ------------ | --- | --- | --- | --- |
| switch(config-if)# |     | mvrp |              |     |     |     |     |
3. OnswitchC,enableMVRPglobally,defineVLAN20,assignatrunknativeVLANtointerface1/1/3,
andenableMVRPonthisinterface.
| switch# config  |      |     |     |     |     |     |     |
| --------------- | ---- | --- | --- | --- | --- | --- | --- |
| switch(config)# | mvrp |     |     |     |     |     |     |
| switch(config)# | vlan | 20  |     |     |     |     |     |
switch(config)#
|                    | interface |             | 1/1/3        |     |     |     |     |
| ------------------ | --------- | ----------- | ------------ | --- | --- | --- | --- |
| switch(config-if)# |           | no shutdown |              |     |     |     |     |
| switch(config-if)# |           | vlan        | trunk native | 1   |     |     |     |
| switch(config-if)# |           | mvrp        |              |     |     |     |     |
4. VerifyVLANconfigurationbyrunningthecommandshow vlan.ItshouldshowthatVLAN10and20
arelearnedbyswitchA,andVLAN10shouldbelearnedbyswitchC.Forexample:
OnswitchA:
| switch# show | vlan |     |     |     |     |     |     |
| ------------ | ---- | --- | --- | --- | --- | --- | --- |
-----------------------------------------------------------------------------
| VLAN Name |     |     | Status | Reason |     | Type | Interfaces |
| --------- | --- | --- | ------ | ------ | --- | ---- | ---------- |
-----------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     |     | up  | ok  |     | default | 1/1/1-1/1/2 |
| ---------------- | --- | --- | --- | --- | --- | ------- | ----------- |
| 10 VLAN10        |     |     | up  | ok  |     | dynamic | 1/1/2       |
| 20 VLAN20        |     |     | up  | ok  |     | dynamic | 1/1/1-1/1/2 |
switch#
| switch# show     | mvrp   | config       |        |               |          |          |     |
| ---------------- | ------ | ------------ | ------ | ------------- | -------- | -------- | --- |
| Configuration    | and    | Status       | - MVRP |               |          |          |     |
| Global MVRP      | status | : Enabled    |        |               |          |          |     |
| Port Status      |        | Registration |        | Join Leave    | LeaveAll | Periodic |     |
|                  |        | Type         |        | Timer Timer   | Timer    | Timer    |     |
| ------- -------- |        | --------     |        | ----- ------- | -------  | -------- |     |
| 1/1/1 Enabled    |        | normal       |        | 20 300        | 1000     | 100      |     |
| 1/1/2 Enabled    |        | normal       |        | 20 300        | 1000     | 100      |     |
| switch# show     | mvrp   | state        |        |               |          |          |     |
| Configuration    | and    | Status       | - MVRP | state         |          |          |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 138

| Port            | VLAN         | Registrar |            | Applicant | Forbid    |     |     |     |
| --------------- | ------------ | --------- | ---------- | --------- | --------- | --- | --- | --- |
|                 |              | State     |            | State     | Mode      |     |     |     |
| ----            | ----         | --------- |            | --------- | --------- |     |     |     |
| 1/1/1           | 1            | IN        |            | QA        | No        |     |     |     |
| 1/1/1           | 10           | MT        |            | QA        | No        |     |     |     |
| 1/1/1           | 20           | IN        |            | QA        | No        |     |     |     |
| 1/1/2           | 1            | IN        |            | QA        | No        |     |     |     |
| 1/1/2           | 10           | IN        |            | VO        | No        |     |     |     |
| 1/1/2           | 20           | IN        |            | QA        | No        |     |     |     |
| switch#         | show         | mvrp      | statistics |           |           |     |     |     |
| Status          | and Counters |           | -          | MVRP      |           |     |     |     |
| MVRP statistics |              | for       | port       | : 1/1/1   |           |     |     |     |
----------------------------
| Failed          | registration |              |        | : 0                 |          |      |     |     |
| --------------- | ------------ | ------------ | ------ | ------------------- | -------- | ---- | --- | --- |
| Last PDU        | origin       |              |        | : e0:07:1b:cb:01:ab |          |      |     |     |
| Total PDU       | Transmitted  |              |        | : 313               |          |      |     |     |
| Total PDU       | Received     |              |        | : 377               |          |      |     |     |
| Frames          | Discarded    |              |        | : 0                 |          |      |     |     |
| Message         | type         | Transmitted  |        |                     | Received |      |     |     |
| --------------  |              | ------------ |        | ------------        |          |      |     |     |
| New             |              |              |        | 0                   |          | 0    |     |     |
| Empty           |              |              | 179105 |                     |          | 2264 |     |     |
| In              |              |              |        | 0                   |          | 346  |     |     |
| Join Empty      |              |              |        | 366                 |          | 62   |     |     |
| Join In         |              |              |        | 342                 |          | 692  |     |     |
| Leave           |              |              |        | 0                   |          | 0    |     |     |
| Leaveall        |              |              |        | 43                  |          | 32   |     |     |
| Status          | and Counters |              | -      | MVRP                |          |      |     |     |
| MVRP statistics |              | for          | port   | : 1/1/2             |          |      |     |     |
----------------------------
| Failed         | registration |              |        | : 0                 |          |     |     |     |
| -------------- | ------------ | ------------ | ------ | ------------------- | -------- | --- | --- | --- |
| Last PDU       | origin       |              |        | : e0:07:1b:cb:22:54 |          |     |     |     |
| Total PDU      | Transmitted  |              |        | : 450               |          |     |     |     |
| Total PDU      | Received     |              |        | : 84                |          |     |     |     |
| Frames         | Discarded    |              |        | : 0                 |          |     |     |     |
| Message        | type         | Transmitted  |        |                     | Received |     |     |     |
| -------------- |              | ------------ |        | ------------        |          |     |     |     |
| New            |              |              |        | 0                   |          | 0   |     |     |
| Empty          |              |              | 173629 |                     |          | 382 |     |     |
| In             |              |              |        | 328                 |          | 0   |     |     |
| Join Empty     |              |              |        | 83                  |          | 93  |     |     |
| Join In        |              |              |        | 711                 |          | 65  |     |     |
| Leave          |              |              |        | 0                   |          | 0   |     |     |
| Leaveall       |              |              |        | 41                  |          | 33  |     |     |
OnswitchB:
| switch# | show | vlan |     |     |     |     |     |     |
| ------- | ---- | ---- | --- | --- | --- | --- | --- | --- |
------------------------------------------------------------------------------
| VLAN Name |     |     |     | Status |     | Reason | Type | Interfaces |
| --------- | --- | --- | --- | ------ | --- | ------ | ---- | ---------- |
------------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     |     |     | up  |     | ok  | default | 1/1/3 |
| ---------------- | --- | --- | --- | --- | --- | --- | ------- | ----- |
| 10 VLAN10        |     |     |     | up  |     | ok  | static  | 1/1/3 |
| 20 VLAN20        |     |     |     | up  |     | ok  | static  | 1/1/3 |
SW1-8320#
| SW1-8320#     | show | mvrp | config |        |     |     |     |     |
| ------------- | ---- | ---- | ------ | ------ | --- | --- | --- | --- |
| Configuration |      | and  | Status | - MVRP |     |     |     |     |
MVRP|139

| Global          | MVRP         | status    | : Enabled    |           |           |         |          |          |     |
| --------------- | ------------ | --------- | ------------ | --------- | --------- | ------- | -------- | -------- | --- |
| Port            | Status       |           | Registration |           | Join      | Leave   | LeaveAll | Periodic |     |
|                 |              |           | Type         |           | Timer     | Timer   | Timer    | Timer    |     |
| -------         | --------     |           | --------     |           | -----     | ------- | -------  | -------- |     |
| 1/1/3           | Enabled      |           | normal       |           |           | 20 300  | 1000     | 100      |     |
| SW1-8320#       | show         | mvrp      | state        |           |           |         |          |          |     |
| Configuration   |              | and       | Status       | - MVRP    | state     |         |          |          |     |
| Port            | VLAN         | Registrar |              | Applicant | Forbid    |         |          |          |     |
|                 |              | State     |              | State     | Mode      |         |          |          |     |
| ----            | ----         | --------- |              | --------- | --------- |         |          |          |     |
| 1/1/3           | 1            | IN        |              | QA        | No        |         |          |          |     |
| 1/1/3           | 10           | MT        |              | QA        | No        |         |          |          |     |
| 1/1/3           | 20           | IN        |              | QA        | No        |         |          |          |     |
| SW1-8320#       | show         | mvrp      | statistics   |           |           |         |          |          |     |
| Status          | and Counters |           | -            | MVRP      |           |         |          |          |     |
| MVRP statistics |              | for       | port         | : 1/1/3   |           |         |          |          |     |
----------------------------
| Failed         | registration |              |        | : 0                 |              |      |     |     |     |
| -------------- | ------------ | ------------ | ------ | ------------------- | ------------ | ---- | --- | --- | --- |
| Last PDU       | origin       |              |        | : 48:0f:cf:af:f2:fa |              |      |     |     |     |
| Total PDU      | Transmitted  |              |        | : 77                |              |      |     |     |     |
| Total PDU      | Received     |              |        | : 303               |              |      |     |     |     |
| Frames         | Discarded    |              |        | : 0                 |              |      |     |     |     |
| Message        | type         | Transmitted  |        |                     | Received     |      |     |     |     |
| -------------- |              | ------------ |        |                     | ------------ |      |     |     |     |
| New            |              |              |        | 0                   |              | 0    |     |     |     |
| Empty          |              |              | 115067 |                     |              | 1754 |     |     |     |
| In             |              |              |        | 0                   |              | 268  |     |     |     |
| Join Empty     |              |              |        | 100                 |              | 1    |     |     |     |
| Join In        |              |              |        | 53                  |              | 581  |     |     |     |
| Leave          |              |              |        | 0                   |              | 0    |     |     |     |
| Leaveall       |              |              |        | 28                  |              | 27   |     |     |     |
OnswitchC:
| switch# | show | vlan |     |     |     |     |     |     |     |
| ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
------------------------------------------------------------------------------
| VLAN Name |     |     |     |     | Status | Reason |     | Type | Interfaces |
| --------- | --- | --- | --- | --- | ------ | ------ | --- | ---- | ---------- |
------------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     |     |     |     | up  | ok  |     | default | 1/1/3 |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- |
| 10 VLAN10        |     |     |     |     | up  | ok  |     | dynamic | 1/1/3 |
| 20 VLAN20        |     |     |     |     | up  | ok  |     | static  | 1/1/3 |
switch#
| switch#       | show     | mvrp      | config       |           |           |         |          |          |     |
| ------------- | -------- | --------- | ------------ | --------- | --------- | ------- | -------- | -------- | --- |
| Configuration |          | and       | Status       | - MVRP    |           |         |          |          |     |
| Global        | MVRP     | status    | : Enabled    |           |           |         |          |          |     |
| Port          | Status   |           | Registration |           | Join      | Leave   | LeaveAll | Periodic |     |
|               |          |           | Type         |           | Timer     | Timer   | Timer    | Timer    |     |
| -------       | -------- |           | --------     |           | -----     | ------- | -------  | -------- |     |
| 1/1/3         | Enabled  |           | normal       |           |           | 20 300  | 1000     | 100      |     |
| switch#       | show     | mvrp      | state        |           |           |         |          |          |     |
| Configuration |          | and       | Status       | - MVRP    | state     |         |          |          |     |
| Port          | VLAN     | Registrar |              | Applicant | Forbid    |         |          |          |     |
|               |          | State     |              | State     | Mode      |         |          |          |     |
| ----          | ----     | --------- |              | --------- | --------- |         |          |          |     |
| 1/1/3         | 1        | IN        |              | QA        |           | No      |          |          |     |
| 1/1/3         | 10       | IN        |              | VO        |           | No      |          |          |     |
| 1/1/3         | 20       | IN        |              | QA        |           | No      |          |          |     |
switch#
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 140

|     | switch#         | show         | mvrp statistics |        |         |     |     |
| --- | --------------- | ------------ | --------------- | ------ | ------- | --- | --- |
|     | Status          | and Counters |                 | - MVRP |         |     |     |
|     | MVRP statistics |              | for             | port   | : 1/1/3 |     |     |
----------------------------
|      | Failed         | registration |              | :     | 0                 |          |     |
| ---- | -------------- | ------------ | ------------ | ----- | ----------------- | -------- | --- |
|      | Last PDU       | origin       |              | :     | 48:0f:cf:af:f2:fb |          |     |
|      | Total PDU      | Transmitted  |              | :     | 203               |          |     |
|      | Total PDU      | Received     |              | :     | 95                |          |     |
|      | Frames         | Discarded    |              | :     | 0                 |          |     |
|      | Message        | type         | Transmitted  |       |                   | Received |     |
|      | -------------- |              | ------------ |       | ------------      |          |     |
|      | New            |              |              |       | 0                 |          | 0   |
|      | Empty          |              |              | 72915 |                   |          | 586 |
|      | In             |              |              |       | 183               |          | 0   |
|      | Join Empty     |              |              |       | 40                |          | 101 |
|      | Join In        |              |              |       | 366               |          | 176 |
|      | Leave          |              |              |       | 0                 |          | 0   |
|      | Leaveall       |              |              |       | 17                |          | 16  |
| MVRP | scenario       |              | 2            |       |                   |          |     |
ThisscenarioillustratestheconfigurationofanMVRPdeploymentwithtwoMSTIs.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
TwoMSTIsaredefinedforthisscenario:
n VLAN10assignedtoMSTI1
n VLAN20assignedtoMSTI2
n AllotherVLANsassignedtothedefaultMSTI0
MVRP|141

Procedure
1. OnswitchA:
| switch# config  |     |               |     |                 |        |     |     |
| --------------- | --- | ------------- | --- | --------------- | ------ | --- | --- |
| switch(config)# |     | mvrp          |     |                 |        |     |     |
| switch(config)# |     | vlan 10       |     |                 |        |     |     |
| switch(config)# |     | spanning-tree |     |                 |        |     |     |
| switch(config)# |     | spanning-tree |     | priority        | 1      |     |     |
| switch(config)# |     | spanning-tree |     | config-name     | sp1    |     |     |
| switch(config)# |     | spanning-tree |     | config-revision |        | 1   |     |
| switch(config)# |     | spanning-tree |     | instance        | 1 vlan | 10  |     |
| switch(config)# |     | spanning-tree |     | instance        | 2 vlan | 20  |     |
switch(config)#
|                    |     | interface | 1/1/1    |          |     |     |     |
| ------------------ | --- | --------- | -------- | -------- | --- | --- | --- |
| switch(config-if)# |     | no        | shutdown |          |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native 1 |     |     |     |
| switch(config-if)# |     | mvrp      |          |          |     |     |     |
| switch(config-if)# |     | exit      |          |          |     |     |     |
| switch(config)#    |     | interface | 1/1/2    |          |     |     |     |
| switch(config-if)# |     | no        | shutdown |          |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native 1 |     |     |     |
| switch(config-if)# |     | mvrp      |          |          |     |     |     |
| switch(config-if)# |     | exit      |          |          |     |     |     |
switch(config)#
|                    |           | interface    | 1/1/3     |            |         |                   |     |
| ------------------ | --------- | ------------ | --------- | ---------- | ------- | ----------------- | --- |
| switch(config-if)# |           | no           | shutdown  |            |         |                   |     |
| switch(config-if)# |           | vlan         | trunk     | native 1   |         |                   |     |
| switch(config-if)# |           | mvrp         |           |            |         |                   |     |
| switch(config-if)# |           | exit         |           |            |         |                   |     |
| switch# show       | mvrp      | config       |           |            |         |                   |     |
| Configuration      | and       | Status       | -         | MVRP       |         |                   |     |
| Global MVRP        | status    | : Enabled    |           |            |         |                   |     |
| Port Status        |           | Registration |           | Join       | Leave   | LeaveAll Periodic |     |
|                    |           | Type         |           | Timer      | Timer   | Timer Timer       |     |
| ------- --------   |           | --------     |           | -----      | ------- | ------- --------  |     |
| 1/1/1              | Enabled   | normal       |           | 20         | 300     | 1000              | 100 |
| 1/1/3              | Enabled   | normal       |           | 20         | 300     | 1000              | 100 |
| 1/1/2              | Enabled   | normal       |           | 20         | 300     | 1000              | 100 |
| switch# show       | mvrp      | state        |           |            |         |                   |     |
| Configuration      | and       | Status       | -         | MVRP state |         |                   |     |
| Port VLAN          | Registrar |              | Applicant | Forbid     |         |                   |     |
|                    | State     |              | State     | Mode       |         |                   |     |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 142

| ---- ----    | ---------     | --------- | --------- |     |     |     |
| ------------ | ------------- | --------- | --------- | --- | --- | --- |
| 1/1/1 1      | IN            | QA        | No        |     |     |     |
| 1/1/1 20     | MT            | QA        | No        |     |     |     |
| 1/1/3 1      | IN            | QA        | No        |     |     |     |
| 1/1/3 20     | IN            | VO        | No        |     |     |     |
| 1/1/2 1      | MT            | QA        | No        |     |     |     |
| 1/1/2 20     | MT            | QA        | No        |     |     |     |
| switch# show | spanning-tree |           | mst       |     |     |     |
#### MST0
| Vlans mapped: | 1-9,11-19,21-4094         |     |     |               |     |     |
| ------------- | ------------------------- | --- | --- | ------------- | --- | --- |
| Bridge        | Address:48:0f:cf:af:f1:82 |     |     | priority:4096 |     |     |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |     | txHoldCount(i6 |     |     |     |     |
| ------------------ | --- | -------------- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |                                | txHoldCount(i6 |       |               |          |      |
| ------------------ | ------------------------------ | -------------- | ----- | ------------- | -------- | ---- |
| Root               | Address:48:0f:cf:af:14:0a      |                |       | Priority:4096 |          |      |
|                    | Port:1/1/3                     |                |       | Path cost:0   |          |      |
| Regional           | Root Address:48:0f:cf:af:14:0a |                |       | Priority:4096 |          |      |
|                    | Internal                       | cost:20000     |       | Rem Hops:19   |          |      |
| Port               | Role                           |                | State | Cost          | Priority | Type |
-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/1 | Designated |     | Forwarding | 20000 | 128 | point_to_ |
| ----- | ---------- | --- | ---------- | ----- | --- | --------- |
point
| 1/1/2 | Designated |     | Forwarding | 20000 | 128 | point_to_ |
| ----- | ---------- | --- | ---------- | ----- | --- | --------- |
point
| 1/1/3 | Root |     | Forwarding | 20000 | 128 | point_to_ |
| ----- | ---- | --- | ---------- | ----- | --- | --------- |
point
#### MST1
| Vlans mapped: | 10                        |     |             |                |          |      |
| ------------- | ------------------------- | --- | ----------- | -------------- | -------- | ---- |
| Bridge        | Address:48:0f:cf:af:f1:82 |     |             | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |     |             | Priority:32768 |          |      |
|               | Port:1/1/3,               |     | Cost:20000, | Rem Hops:19    |          |      |
| Port          | Role                      |     | State       | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated |     | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | --- | ---------- | ----- | --- | -------------- |
| 1/1/2 | Designated |     | Forwarding | 20000 | 128 | point_to_point |
| 1/1/3 | Root       |     | Forwarding | 20000 | 128 | point_to_point |
#### MST2
| Vlans mapped: | 20                        |     |             |                |          |      |
| ------------- | ------------------------- | --- | ----------- | -------------- | -------- | ---- |
| Bridge        | Address:48:0f:cf:af:f1:82 |     |             | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |     |             | Priority:32768 |          |      |
|               | Port:1/1/3,               |     | Cost:20000, | Rem Hops:19    |          |      |
| Port          | Role                      |     | State       | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated |     | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | --- | ---------- | ----- | --- | -------------- |
| 1/1/2 | Designated |     | Forwarding | 20000 | 128 | point_to_point |
| 1/1/3 | Root       |     | Forwarding | 20000 | 128 | point_to_point |
2. OnswitchB:
| switch# config |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- |
MVRP|143

| switch(config)# |     | mvrp |     |     |     |     |     |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
switch(config)#
|                    |     | vlan          | 20          |        |                 |        |     |     |     |
| ------------------ | --- | ------------- | ----------- | ------ | --------------- | ------ | --- | --- | --- |
| switch(config)#    |     | spanning-tree |             |        |                 |        |     |     |     |
| switch(config)#    |     | spanning-tree |             |        | priority        | 1      |     |     |     |
| switch(config)#    |     | spanning-tree |             |        | config-name     | sp1    |     |     |     |
| switch(config)#    |     | spanning-tree |             |        | config-revision |        | 1   |     |     |
| switch(config)#    |     | spanning-tree |             |        | instance        | 1 vlan | 10  |     |     |
| switch(config)#    |     | spanning-tree |             |        | instance        | 2 vlan | 20  |     |     |
| switch(config)#    |     | interface     |             | 1/1/18 |                 |        |     |     |     |
| switch(config-if)# |     |               | no shutdown |        |                 |        |     |     |     |
| switch(config-if)# |     |               | vlan        | trunk  | native 1        |        |     |     |     |
switch(config-if)#
|                    |     |           | vlan        | trunk  | allowed  | all |     |     |     |
| ------------------ | --- | --------- | ----------- | ------ | -------- | --- | --- | --- | --- |
| switch(config-if)# |     |           | mvrp        |        |          |     |     |     |     |
| switch(config-if)# |     |           | exit        |        |          |     |     |     |     |
| switch(config)#    |     | interface |             | 1/1/20 |          |     |     |     |     |
| switch(config-if)# |     |           | no shutdown |        |          |     |     |     |     |
| switch(config-if)# |     |           | vlan        | trunk  | native 1 |     |     |     |     |
| switch(config-if)# |     |           | vlan        | trunk  | allowed  | all |     |     |     |
| switch(config-if)# |     |           | mvrp        |        |          |     |     |     |     |
| switch(config-if)# |     |           | exit        |        |          |     |     |     |     |
| switch(config)#    |     | interface |             | 1/1/22 |          |     |     |     |     |
switch(config-if)#
|                    |               |              | no shutdown |        |           |         |          |          |     |
| ------------------ | ------------- | ------------ | ----------- | ------ | --------- | ------- | -------- | -------- | --- |
| switch(config-if)# |               |              | vlan        | trunk  | native 1  |         |          |          |     |
| switch(config-if)# |               |              | vlan        | trunk  | allowed   | all     |          |          |     |
| switch(config-if)# |               |              | mvrp        |        |           |         |          |          |     |
| switch(config-if)# |               |              | exit        |        |           |         |          |          |     |
| switch# show       | mvrp          | config       |             |        |           |         |          |          |     |
| Configuration      |               | and Status   |             | - MVRP |           |         |          |          |     |
| Global MVRP        | status        |              | : Enabled   |        |           |         |          |          |     |
| Port Status        |               | Registration |             |        | Join      | Leave   | LeaveAll | Periodic |     |
|                    |               | Type         |             |        | Timer     | Timer   | Timer    | Timer    |     |
| ------- --------   |               | --------     |             |        | -----     | ------- | -------  | -------- |     |
| 1/1/18             | Enabled       |              | normal      |        | 20        | 300     | 1000     |          | 100 |
| 1/1/20             | Enabled       |              | normal      |        | 20        | 300     | 1000     |          | 100 |
| 1/1/22             | Enabled       |              | normal      |        | 20        | 300     | 1000     |          | 100 |
| switch# show       | mvrp          | state        |             |        |           |         |          |          |     |
| Configuration      |               | and Status   |             | - MVRP | state     |         |          |          |     |
| Port VLAN          | Registrar     |              | Applicant   |        | Forbid    |         |          |          |     |
|                    | State         |              | State       |        | Mode      |         |          |          |     |
| ---- ----          | ---------     |              | ---------   |        | --------- |         |          |          |     |
| 1/1/20 1           | MT            |              | AA          |        | No        |         |          |          |     |
| 1/1/20 10          | MT            |              | AA          |        | No        |         |          |          |     |
| 1/1/20 20          | MT            |              | AA          |        | No        |         |          |          |     |
| 1/1/22 1           | IN            |              | AP          |        | No        |         |          |          |     |
| 1/1/22 10          | IN            |              | VO          |        | No        |         |          |          |     |
| 1/1/22 20          | MT            |              | VP          |        | No        |         |          |          |     |
| switch# show       | spanning-tree |              |             | mst    |           |         |          |          |     |
#### MST0
| Vlans mapped: |     | 1-9,11-19,21-4094         |     |     |     |     |               |     |     |
| ------------- | --- | ------------------------- | --- | --- | --- | --- | ------------- | --- | --- |
| Bridge        |     | Address:e0:07:1b:cb:22:1c |     |     |     |     | priority:4096 |     |     |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age
| (in seconds):20 |     | txHoldCount(in |     |     | pp6 |     |     |     |     |
| --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age
| (in seconds):20 |      | Max-Hops:20               |     |            |       |               |         |          |      |
| --------------- | ---- | ------------------------- | --- | ---------- | ----- | ------------- | ------- | -------- | ---- |
| Root            |      | Address:48:0f:cf:af:14:0a |     |            |       | Priority:4096 |         |          |      |
|                 |      | Port:1/1/22               |     |            |       | Path          | cost:0  |          |      |
| Regional        | Root | Address:48:0f:cf:af:14:0a |     |            |       | Priority:4096 |         |          |      |
|                 |      | Internal                  |     | cost:20000 |       | Rem           | Hops:19 |          |      |
| Port            |      | Role                      |     |            | State |               | Cost    | Priority | Type |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 144

-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/18 | Alternate | Blocking | 20000 | 128 | point_to_ |
| ------ | --------- | -------- | ----- | --- | --------- |
point
| 1/1/20 | Designated | Forwarding | 20000 | 128 | point_to_ |
| ------ | ---------- | ---------- | ----- | --- | --------- |
point
| 1/1/22 | Root | Forwarding | 20000 | 128 | point_to_ |
| ------ | ---- | ---------- | ----- | --- | --------- |
point
#### MST1
| Vlans mapped: | 10                        |             |                |          |      |
| ------------- | ------------------------- | ----------- | -------------- | -------- | ---- |
| Bridge        | Address:e0:07:1b:cb:22:1c |             | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |             | Priority:32768 |          |      |
|               | Port:1/1/22,              | Cost:20000, | Rem Hops:19    |          |      |
| Port          | Role                      | State       | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/18 | Alternate  | Blocking   | 20000 | 128 | point_to_point |
| ------ | ---------- | ---------- | ----- | --- | -------------- |
| 1/1/20 | Designated | Forwarding | 20000 | 128 | point_to_point |
| 1/1/22 | Root       | Forwarding | 20000 | 128 | point_to_point |
#### MST2
| Vlans mapped: | 20                        |             |                |          |      |
| ------------- | ------------------------- | ----------- | -------------- | -------- | ---- |
| Bridge        | Address:e0:07:1b:cb:22:1c |             | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |             | Priority:32768 |          |      |
|               | Port:1/1/22,              | Cost:20000, | Rem Hops:19    |          |      |
| Port          | Role                      | State       | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/18 | Alternate  | Blocking   | 20000 | 128 | point_to_point |
| ------ | ---------- | ---------- | ----- | --- | -------------- |
| 1/1/20 | Designated | Forwarding | 20000 | 128 | point_to_point |
| 1/1/22 | Root       | Forwarding | 20000 | 128 | point_to_point |
3. OnswitchC:
| switch# config  |               |                 |           |     |     |
| --------------- | ------------- | --------------- | --------- | --- | --- |
| switch(config)# | mvrp          |                 |           |     |     |
| switch(config)# | vlan 1,20     |                 |           |     |     |
| switch(config)# | spanning-tree |                 |           |     |     |
| switch(config)# | spanning-tree | priority        | 1         |     |     |
| switch(config)# | spanning-tree | config-name     | sp1       |     |     |
| switch(config)# | spanning-tree | config-revision | 1         |     |     |
| switch(config)# | spanning-tree | instance        | 1 vlan 10 |     |     |
| switch(config)# | spanning-tree | instance        | 2 vlan 20 |     |     |
switch(config)#
|                    | interface   | 1/1/25        |     |     |     |
| ------------------ | ----------- | ------------- | --- | --- | --- |
| switch(config-if)# | no shutdown |               |     |     |     |
| switch(config-if)# | vlan        | trunk native  | 1   |     |     |
| switch(config-if)# | vlan        | trunk allowed | all |     |     |
| switch(config-if)# | mvrp        |               |     |     |     |
| switch(config-if)# | exit        |               |     |     |     |
| switch(config)#    | interface   | 1/1/27        |     |     |     |
| switch(config-if)# | no shutdown |               |     |     |     |
| switch(config-if)# | vlan        | trunk native  | 1   |     |     |
| switch(config-if)# | vlan        | trunk allowed | all |     |     |
switch(config-if)#
mvrp
| switch(config-if)# | exit        |     |     |     |     |
| ------------------ | ----------- | --- | --- | --- | --- |
| switch# show       | mvrp config |     |     |     |     |
MVRP|145

| Configuration    | and           | Status       | -         | MVRP       |         |          |          |     |
| ---------------- | ------------- | ------------ | --------- | ---------- | ------- | -------- | -------- | --- |
| Global MVRP      | status        | : Enabled    |           |            |         |          |          |     |
| Port Status      |               | Registration |           | Join       | Leave   | LeaveAll | Periodic |     |
|                  |               | Type         |           | Timer      | Timer   | Timer    | Timer    |     |
| ------- -------- |               | --------     |           | -----      | ------- | -------  | -------- |     |
| 1/1/25           | Enabled       | normal       |           | 20         | 300     | 1000     |          | 100 |
| 1/1/27           | Enabled       | normal       |           | 20         | 300     | 1000     |          | 100 |
| switch# show     | mvrp          | state        |           |            |         |          |          |     |
| Configuration    | and           | Status       | -         | MVRP state |         |          |          |     |
| Port VLAN        | Registrar     |              | Applicant | Forbid     |         |          |          |     |
|                  | State         |              | State     | Mode       |         |          |          |     |
| ---- ----        | ---------     |              | --------- | ---------  |         |          |          |     |
| 1/1/25 1         | IN            |              | QA        | No         |         |          |          |     |
| 1/1/25 10        | IN            |              | VO        | No         |         |          |          |     |
| 1/1/25 20        | IN            |              | VO        | No         |         |          |          |     |
| switch# show     | spanning-tree |              |           | mst        |         |          |          |     |
#### MST0
| Vlans mapped: |     | 1-9,11-19,21-4094         |     |     |     |               |     |     |
| ------------- | --- | ------------------------- | --- | --- | --- | ------------- | --- | --- |
| Bridge        |     | Address:e0:07:1b:cb:01:7a |     |     |     | priority:4096 |     |     |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age
| (in seconds):20 |     | txHoldCount(6 |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age
| (in seconds):20 |      | Max-Hops:20               |            |       |               |         |          |      |
| --------------- | ---- | ------------------------- | ---------- | ----- | ------------- | ------- | -------- | ---- |
| Root            |      | Address:48:0f:cf:af:14:0a |            |       | Priority:4096 |         |          |      |
|                 |      | Port:1/1/25               |            |       | Path          | cost:0  |          |      |
| Regional        | Root | Address:48:0f:cf:af:14:0a |            |       | Priority:4096 |         |          |      |
|                 |      | Internal                  | cost:40000 |       | Rem           | Hops:18 |          |      |
| Port            |      | Role                      |            | State | Cost          |         | Priority | Type |
-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/25 |     | Root      |     | Forwarding | 20000 |     | 128 | point_to_point |
| ------ | --- | --------- | --- | ---------- | ----- | --- | --- | -------------- |
| 1/1/27 |     | Alternate |     | Blocking   | 20000 |     | 128 | point_to_point |
#### MST1
| Vlans mapped: |     | 10                        |     |             |      |                |          |      |
| ------------- | --- | ------------------------- | --- | ----------- | ---- | -------------- | -------- | ---- |
| Bridge        |     | Address:e0:07:1b:cb:01:7a |     |             |      | Priority:32768 |          |      |
| Root          |     | Address:48:0f:cf:af:14:0a |     |             |      | Priority:32768 |          |      |
|               |     | Port:1/1/25,              |     | Cost:40000, | Rem  | Hops:18        |          |      |
| Port          |     | Role                      |     | State       | Cost |                | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/25 |     | Root      |     | Forwarding | 20000 |     | 128 | point_to_point |
| ------ | --- | --------- | --- | ---------- | ----- | --- | --- | -------------- |
| 1/1/27 |     | Alternate |     | Blocking   | 20000 |     | 128 | point_to_point |
#### MST2
| Vlans mapped: |     | 20                        |     |             |      |                |          |      |
| ------------- | --- | ------------------------- | --- | ----------- | ---- | -------------- | -------- | ---- |
| Bridge        |     | Address:e0:07:1b:cb:01:7a |     |             |      | Priority:32768 |          |      |
| Root          |     | Address:48:0f:cf:af:14:0a |     |             |      | Priority:32768 |          |      |
|               |     | Port:1/1/25,              |     | Cost:40000, | Rem  | Hops:18        |          |      |
| Port          |     | Role                      |     | State       | Cost |                | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/25 |     | Root      |     | Forwarding | 20000 |     | 128 | point_to_point |
| ------ | --- | --------- | --- | ---------- | ----- | --- | --- | -------------- |
| 1/1/27 |     | Alternate |     | Blocking   | 20000 |     | 128 | point_to_point |
4. OnswitchD:
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 146

| switch# config |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
switch(config)#
mvrp
| switch(config)#    |     | vlan 1        |          |                 |        |     |     |     |
| ------------------ | --- | ------------- | -------- | --------------- | ------ | --- | --- | --- |
| switch(config)#    |     | spanning-tree |          |                 |        |     |     |     |
| switch(config)#    |     | spanning-tree |          | priority        | 1      |     |     |     |
| switch(config)#    |     | spanning-tree |          | config-name     | sp1    |     |     |     |
| switch(config)#    |     | spanning-tree |          | config-revision |        | 1   |     |     |
| switch(config)#    |     | spanning-tree |          | instance        | 1 vlan | 10  |     |     |
| switch(config)#    |     | spanning-tree |          | instance        | 2 vlan | 20  |     |     |
| switch(config)#    |     | interface     | 1/1/1    |                 |        |     |     |     |
| switch(config-if)# |     | no            | shutdown |                 |        |     |     |     |
switch(config-if)#
|                    |     | vlan      | trunk    | native 1 |     |     |     |     |
| ------------------ | --- | --------- | -------- | -------- | --- | --- | --- | --- |
| switch(config-if)# |     | vlan      | trunk    | allowed  | all |     |     |     |
| switch(config-if)# |     | mvrp      |          |          |     |     |     |     |
| switch(config-if)# |     | exit      |          |          |     |     |     |     |
| switch(config)#    |     | interface | 1/1/2    |          |     |     |     |     |
| switch(config-if)# |     | no        | shutdown |          |     |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native 1 |     |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | allowed  | all |     |     |     |
| switch(config-if)# |     | mvrp      |          |          |     |     |     |     |
| switch(config-if)# |     | exit      |          |          |     |     |     |     |
switch#
show mvrp config
| Configuration    | and       | Status       | -         | MVRP       |         |          |          |     |
| ---------------- | --------- | ------------ | --------- | ---------- | ------- | -------- | -------- | --- |
| Global MVRP      | status    | : Enabled    |           |            |         |          |          |     |
| Port Status      |           | Registration |           | Join       | Leave   | LeaveAll | Periodic |     |
|                  |           | Type         |           | Timer      | Timer   | Timer    | Timer    |     |
| ------- -------- |           | --------     |           | -----      | ------- | -------  | -------- |     |
| 1/1/1            | Enabled   | normal       |           | 20         | 300     | 1000     |          | 100 |
| 1/1/2            | Enabled   | normal       |           | 20         | 300     | 1000     |          | 100 |
| switch# show     | mvrp      | state        |           |            |         |          |          |     |
| Configuration    | and       | Status       | -         | MVRP state |         |          |          |     |
| Port VLAN        | Registrar |              | Applicant | Forbid     |         |          |          |     |
|                  | State     |              | State     | Mode       |         |          |          |     |
| ---- ----        | --------- |              | --------- | ---------  |         |          |          |     |
| 1/1/1 1          | IN        |              | QA        | No         |         |          |          |     |
| 1/1/1 10         | MT        |              | QA        | No         |         |          |          |     |
| 1/1/1 20         | IN        |              | VO        | No         |         |          |          |     |
| 1/1/2 1          | IN        |              | AA        | No         |         |          |          |     |
| 1/1/2 10         | IN        |              | VO        | No         |         |          |          |     |
| 1/1/2 20         | MT        |              | AA        | No         |         |          |          |     |
switch#
| show | spanning-tree |     |     | mst |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
#### MST0
| Vlans mapped: |     | 1-9,11-19,21-4094         |     |     |     |               |     |     |
| ------------- | --- | ------------------------- | --- | --- | --- | ------------- | --- | --- |
| Bridge        |     | Address:48:0f:cf:af:14:0a |     |     |     | priority:4096 |     |     |
Root
| Regional | Root |     |     |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |     | txHoldC6 |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |      | Max-Hop0                  |        |       |               |         |          |      |
| ------------------ | ---- | ------------------------- | ------ | ----- | ------------- | ------- | -------- | ---- |
| Root               |      | Address:48:0f:cf:af:14:0a |        |       | Priority:4096 |         |          |      |
|                    |      | Port:0                    |        |       | Path          | cost:0  |          |      |
| Regional           | Root | Address:48:0f:cf:af:14:0a |        |       | Priority:4096 |         |          |      |
|                    |      | Internal                  | cost:0 |       | Rem           | Hops:20 |          |      |
| Port               |      | Role                      |        | State |               | Cost    | Priority | Type |
-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/1 |     | Designated |     | Forwarding |     | 20000 | 128 | point_to_ |
| ----- | --- | ---------- | --- | ---------- | --- | ----- | --- | --------- |
point
| 1/1/2 |     | Designated |     | Forwarding |     | 20000 | 128 | point_to_ |
| ----- | --- | ---------- | --- | ---------- | --- | ----- | --- | --------- |
MVRP|147

point
#### MST1
|     | Vlans mapped: | 10                        |             |                |      |
| --- | ------------- | ------------------------- | ----------- | -------------- | ---- |
|     | Bridge        | Address:48:0f:cf:af:14:0a |             | Priority:32768 |      |
|     | Root          | Address:48:0f:cf:af:14:0a |             | Priority:32768 |      |
|     |               | Port:0,                   | Cost:0, Rem | Hops:20        |      |
|     | Port          | Role                      | State       | Cost Priority  | Type |
-------------- -------------- ------------ ------- ---------- ----------
|     | 1/1/1 | Designated | Forwarding | 20000 128 | point_to_point |
| --- | ----- | ---------- | ---------- | --------- | -------------- |
|     | 1/1/2 | Designated | Forwarding | 20000 128 | point_to_point |
#### MST2
|     | Vlans mapped: | 20                        |             |                |      |
| --- | ------------- | ------------------------- | ----------- | -------------- | ---- |
|     | Bridge        | Address:48:0f:cf:af:14:0a |             | Priority:32768 |      |
|     | Root          | Address:48:0f:cf:af:14:0a |             | Priority:32768 |      |
|     |               | Port:0,                   | Cost:0, Rem | Hops:20        |      |
|     | Port          | Role                      | State       | Cost Priority  | Type |
-------------- -------------- ------------ ------- ---------- ----------
|       | 1/1/1           | Designated | Forwarding | 20000 128 | point_to_point |
| ----- | --------------- | ---------- | ---------- | --------- | -------------- |
|       | 1/1/2           | Designated | Forwarding | 20000 128 | point_to_point |
| MVRP  | commands        |            |            |           |                |
| clear | mvrp statistics |            |            |           |                |
Syntax
| clear mvrp | statistics | [<PORT-NUM> | | <PORT-LIST> | | LAG <LAG-NUM>] |     |
| ---------- | ---------- | ----------- | ------------- | ---------------- | --- |
Commandcontext
Manager(#)
Description
ResetstheMVRPstatisticcountersgloballyorforthespecifiedportsorLAG.
Parameters
<PORT-NUM>
Specifiesaportnumber.
<PORT-LIST>
Specifiesalistofports.
LAG <LAG-NUM>
SpecifiesaLinkAggregationnumber.Range:1to128.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 148

switch# clear mvrp statistics 1/1/1

mvrp

Syntax

mvrp
no mvrp

Description

Enables the MVRP feature globally or on a specific interface. By default, MVRP is disabled.

The no form of this command disables MVRP.

MVRP and VLAN translation cannot be enabled on the same interface.

Command context

config
config-if

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

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

Parameters

MVRP | 149

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

Sets the join timer. You can use the timer to space MVRP join messages. To ensure that join messages are
transmitted to other participants, an MRP participant waits for the specified period of the join timer
before sending a join message. The Join timer must be less than half of the Leave Timer. Range: 20 to
100 in centiseconds. Default: 20.

leave <TIME>

Sets the leave timer for the port, specifying the time that the registrar state machine waits in the LV state
before transiting to the MT state. The leave timer must be at least twice the join timer and must be less
than the leave all timer. Range: 40 - 1000000 centiseconds. Default: 300 centiseconds.

leaveall <TIME>

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

150

Sets the leave all timer for the port, specifying the frequency with which the leave all state machine
generates leave alll PDUs. Range: 500 to1000000 centiseconds. Default: 1000.

periodic <TIME>

Sets the periodic timer for the port, specifying the frequency with which the periodic transmission state
machine generates periodic events. The periodic timer is set to 1 second when it is started. Range: 100 to
1000000 centiseconds. Default: 100.

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

On the 6400 Switch Series, interface identification differs.

switch# show mvrp config
Configuration and Status - MVRP
Global MVRP status : Disabled
Port

Status

Registration Join Leave LeaveAll Periodic
Timer Timer Timer
Type

Timer

MVRP | 151

| ------- | -------- |          | -------- |        | ----- | ----- | ------ -------- |
| ------- | -------- | -------- | -------- | ------ | ----- | ----- | --------------- |
| 1/1/1   |          | Disabled |          | Normal | 20    | 300   | 1000 100        |
| 1/1/2   |          | Disabled |          | Normal | 20    | 300   | 1000 100        |
| 1/1/3   |          | Disabled |          | Normal | 20    | 300   | 1000 100        |
| show    | mvrp     | state    |          |        |       |       |                 |
Syntax
| show mvrp | state | [<VLAN-ID> |     | | <VLAN-ID> |     | <PORT-NUM>] |     |
| --------- | ----- | ---------- | --- | ----------- | --- | ----------- | --- |
[vsx-peer]
Description
DisplaystheMVRPRegistrarandApplicantstatemachineinformationforallportsonwhichMVRPis
enabled,orforspecificports.
Commandcontext
Operator(>)orManager(#)
Parameters
<VLAN-ID>
SpecifiesthenumberofaVLAN.
<PORT-NUM>
Specifiesaphysicalportontheswitch.Forrmat:member/slot/port.
[vsx-peer]
ShowstheoutputfromtheVSXpeerswitch.IftheswitchesdonothavetheVSXconfigurationortheISL
isdown,theoutputfromtheVSXpeerswitchisnotdisplayed.Thisparameterisavailableonswitches
thatsupportVSX.
Authority
OperatorsorAdministratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Operatorscanexecutethiscommandfromtheoperatorcontext(>)only.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
| switch#       | show | mvrp      | state      | 1         |           |     |         |
| ------------- | ---- | --------- | ---------- | --------- | --------- | --- | ------- |
| Configuration |      |           | and Status | - MVRP    | state     | for | VLAN 1  |
| Port          | VLAN | Registrar |            | Applicant |           |     |         |
|               |      | State     |            | State     |           |     |         |
| ----          | ---- | --------  |            | --------- |           |     |         |
| 1/1/1         | 1    | MT        |            | QA        |           |     |         |
| switch#       | show | mvrp      | state      | 10 1/1/1  |           |     |         |
| Configuration |      |           | and Status | - MVRP    | state     | for | VLAN 10 |
| Port          | VLAN | Registrar |            | Applicant | Forbid    |     |         |
|               |      | State     |            | State     | Mode      |     |         |
| ----          | ---- | --------- |            | --------- | --------- |     |         |
| 1/1/1         | 10   | MT        |            | LO        | Yes       |     |         |
switch#
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 152

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

On the 6400 Switch Series, interface identification differs.

: 0
: 48:0f:cf:af:b1:76

switch# show mvrp statistics
Status and Counters - MVRP
MVRP statistics for port : 1/1/1
----------------------------
Failed registration
Last PDU origin
Total PDU Transmitted : 13127
Total PDU Received
Frames Discarded
Message type
Received
-------------- ------------ ------------
0
New
1264
Empty
4
In
48
Join Empty
555
Join In
0
Leave
25
Leaveall

0
50029394
0
1425
563
0
12218

Transmitted

: 327
: 0

switch# show mvrp statistics 1/1/1

Status and Counters - MVRP
MVRP statistics for port : 1/1/1
----------------------------
Failed registration
Last PDU origin

: 0
: 48:0f:cf:af:b1:76

MVRP | 153

| Total PDU      | Transmitted |              | : 14874  |              |      |
| -------------- | ----------- | ------------ | -------- | ------------ | ---- |
| Total PDU      | Received    |              | : 327    |              |      |
| Frames         | Discarded   |              | : 0      |              |      |
| Message        | type        | Transmitted  |          | Received     |      |
| -------------- |             | ------------ |          | ------------ |      |
| New            |             |              |          | 0            | 0    |
| Empty          |             |              | 57181612 |              | 1264 |
| In             |             |              |          | 0            | 4    |
| Join Empty     |             |              | 1425     |              | 48   |
| Join In        |             |              | 563      |              | 555  |
| Leave          |             |              |          | 0            | 0    |
| Leaveall       |             |              | 13965    |              | 25   |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 154

Chapter 8

UDLD

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
interval). If a port does not receive a health-check packet from the port at the other end of the link within
the keepalive interval, the port waits for four more intervals. If the port still does not receive a health-check
packet after waiting for five intervals, the port concludes that the link has failed and blocks the UDLD-
enabled port.

When a port is blocked by UDLD, the event is recorded in the switch log and other port blocking protocols,
like spanning tree or meshing, will not use the bad link to load balance packets. The port will remain blocked
until the link is unplugged, disabled, or fixed. The port can also be unblocked by disabling UDLD on the port.

Port blocking behavior is dependant on the UDLD mode in use. The previous paragraphs describe RFC5171
Aggressive mode. Other modes behave as follows:

n RFC 5171 normal: The port is not blocked but a notification is triggered.

n Aruba OS verify-then-forward: The links are considered blocked until bi-directionality is confirmed. After a
link is considered bidirectional, if the retries are met and no packets are received, the link is marked as
blocked.

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

155

ArubaOSforward-then-verify:Thelinksstartupasunblocked.Afteralinkisconsideredbidirectional,if
n
theretriesaremetandnopacketsarereceived,thelinkismarkedasblocked.
| Configuring | UDLD |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- |
Procedure
1. EnableUDLDonaninterfacewiththecommandudld.
2. Formostdeployments,thedefaultvaluesforthefollowingsettingsdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicatedcommand:
| UDLD setting            |     | Default | value | Commandtochange | it  |
| ----------------------- | --- | ------- | ----- | --------------- | --- |
| Packettransmissiondelay |     | 7000ms  |       | udld interval   |     |
interval.
| Operatingmode. |     | InterconnectwithHPE |     | udld mode |     |
| -------------- | --- | ------------------- | --- | --------- | --- |
PVOS/Brocade/Foundryswitchesin
forward-then-verifymode.
| Retrycount.                                          |     | 4   |       | udld retries |     |
| ---------------------------------------------------- | --- | --- | ----- | ------------ | --- |
| 3. ReviewUDLDconfigurationsettingswiththecommandshow |     |     | udld. |              |     |
Example
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Thisexamplecreatesthefollowingconfiguration:
n EnablesUDLDoninterface1/1/1.
| n SetstheUDLDmodetorfc5171 |     | aggressive. |     |     |     |
| -------------------------- | --- | ----------- | --- | --- | --- |
n SetstheUDLDintervalto1000.
n SetstheUDLDretriesto3.
| switch(config)# | interface | 1/1/1 |     |     |     |
| --------------- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|                    | mode      | rfc5171 aggressive |       |     |     |
| ------------------ | --------- | ------------------ | ----- | --- | --- |
| switch(config-if)# | interval  | 10000              |       |     |     |
| switch(config-if)# | retries   | 3                  |       |     |     |
| switch(config-if)# | udld      |                    |       |     |     |
| switch(config-if)# | quit      |                    |       |     |     |
| switch(config)#    | show udld | interface          | 1/1/1 |     |     |
| Interface 1/1/1    |           |                    |       |     |     |
| Config: enabled    |           |                    |       |     |     |
State: active
| Substate: bidirectional |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- |
Link: unblock
| Version: rfc5171 |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
Mode: aggressive
| Interval: 10000 | milliseconds |     |     |     |     |
| --------------- | ------------ | --- | --- | --- | --- |
| Retries: 3      |              |     |     |     |     |
Tx: 0 packets
| Rx: 0 packets,    | 0 discarded | packets, | 0 dropped packets |     |     |
| ----------------- | ----------- | -------- | ----------------- | --- | --- |
| Port transitions: | 0           |          |                   |     |     |
UDLD|156

UDLD scenario
ThisscenariodescribeshowtouseUDLDonasinglephysicalinterfaceaswellasaLAG.
Onthe6400SwitchSeries,interfaceidentificationdiffers.
Procedure
1. OnswitchA:
a. ConfiguretheUDLDsessionbetweenswitchAandB.
| switch# config     |           |     |       |
| ------------------ | --------- | --- | ----- |
| switch(config-if)# | interface |     | 1/1/1 |
| switch(config-if)# | udld      |     |       |
switch(config-if)#
exit
switch(config)#
b. ConfiguretheUDLDsessionbetweenswitchAandC.
| switch(config)#    | interface | 1/1/2    |                              |
| ------------------ | --------- | -------- | ---------------------------- |
| switch(config-if)# | no        | shutdown |                              |
| switch(config-if)# | lag       | 1        |                              |
| switch(config-if)# | udld      | interval | 400                          |
| switch(config-if)# | udld      | mode     | aruba-os verify-then-forward |
| switch(config-if)# | udld      | retries  | 5                            |
switch(config)#
exit
| switch(config)#    | interface | 1/1/3    |                              |
| ------------------ | --------- | -------- | ---------------------------- |
| switch(config-if)# | no        | shutdown |                              |
| switch(config-if)# | lag       | 1        |                              |
| switch(config-if)# | udld      | interval | 400                          |
| switch(config-if)# | udld      | mode     | aruba-os verify-then-forward |
| switch(config-if)# | udld      | retries  | 5                            |
2. OnswitchB,configuretheUDLDsessionbetweenswitchBandA.
switch# config
| switch(config-if)# | interface | 1/1/1 |     |
| ------------------ | --------- | ----- | --- |
switch(config-if)#
udld
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 157

|     | switch(config-if)# |     |     | exit |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
3. OnswitchC,configuretheUDLDsessionbetweenswitchCandA.
|     | switch#         | config |           |     |       |     |     |     |     |     |
| --- | --------------- | ------ | --------- | --- | ----- | --- | --- | --- | --- | --- |
|     | switch(config)# |        | interface |     | 1/1/2 |     |     |     |     |     |
switch(config-if)#
no shutdown
|     | switch(config-if)# |     |           | lag         | 1        |          |                     |     |     |     |
| --- | ------------------ | --- | --------- | ----------- | -------- | -------- | ------------------- | --- | --- | --- |
|     | switch(config-if)# |     |           | udld        | interval | 400      |                     |     |     |     |
|     | switch(config-if)# |     |           | udld        | mode     | aruba-os | verify-then-forward |     |     |     |
|     | switch(config-if)# |     |           | udld        | retries  | 5        |                     |     |     |     |
|     | switch(config)#    |     | exit      |             |          |          |                     |     |     |     |
|     | switch(config)#    |     | interface |             | 1/1/3    |          |                     |     |     |     |
|     | switch(config-if)# |     |           | no shutdown |          |          |                     |     |     |     |
|     | switch(config-if)# |     |           | lag         | 1        |          |                     |     |     |     |
|     | switch(config-if)# |     |           | udld        | interval | 400      |                     |     |     |     |
switch(config-if)#
|     |                    |     |     | udld | mode    | aruba-os | verify-then-forward |     |     |     |
| --- | ------------------ | --- | --- | ---- | ------- | -------- | ------------------- | --- | --- | --- |
|     | switch(config-if)# |     |     | udld | retries | 5        |                     |     |     |     |
4. OnswitchA,verifyUDLDconfigurationbyrunningthecommandshow udld.(Apacketmustarrive
oneachswitchforittounblocktheinterface.)
|     | switch# | show | udld |     |     |     |     |     |     |     |
| --- | ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
Abbreviations:
|     | VTF - Verify |      | then   | forward |     | FTV | - Forward  | then verify |     |     |
| --- | ------------ | ---- | ------ | ------- | --- | --- | ---------- | ----------- | --- | --- |
|     | NOR - RFC    | 5171 | normal |         |     | AGG | - RFC 5171 | aggressive  |     |     |
------------------------------------------------------------------------------
--------------------------------------------------
|     | Interface | UDLD   |      | UDLD  |      | UDLD     |     | UDLD Mode   | Interval |     |
| --- | --------- | ------ | ---- | ----- | ---- | -------- | --- | ----------- | -------- | --- |
|     | Retries   | Tx     | Rx   | Rx    |      | Rx       |     | Transitions |          |     |
|     |           | Config |      | State |      | Substate |     | Link        |          |     |
|     | Pkts      | Pkts   | Pkts | disc. | Pkts | drop.    |     |             |          |     |
------------------------------------------------------------------------------
--------------------------------------------------
|       | 1/1/1           | enabled |     | active |     | Bidirectional |     | unblock FTV | 7000 | 4   |
| ----- | --------------- | ------- | --- | ------ | --- | ------------- | --- | ----------- | ---- | --- |
|       | 0               | 0       | 0   |        | 0   |               | 0   |             |      |     |
|       | 1/1/2           | enabled |     | active |     | Bidirectional |     | unblock VTF | 400  | 5   |
|       | 2               | 2       | 0   |        | 0   |               | 1   |             |      |     |
|       | 1/1/3           | enabled |     | active |     | Bidirectional |     | unblock VTF | 400  | 5   |
|       | 2               | 2       | 0   |        | 0   |               | 1   |             |      |     |
| UDLD  | commands        |         |     |        |     |               |     |             |      |     |
| clear | udld statistics |         |     |        |     |               |     |             |      |     |
Syntax
| clear | udld statistics |     | [interface |     | <INTERFACE-NAME>] |     |     |     |     |     |
| ----- | --------------- | --- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- |
Description
ClearsUDLDstatisticsforallinterfacesoraspecificinterface.
Commandcontext
Manager(#)
UDLD|158

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

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

n An Ethernet interface associated with a physical port. Use the format member/slot/port (for example,

1/3/1).

n UDLD runs only on physical interfaces. LAGs, tunnels, and the like are not supported. However, UDLD
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

On the 6400 Switch Series, interface identification differs.

Displaying all UDLD information:

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

159

| switch# | show udld |     |     |     |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Abbreviations:
| VTF - | Verify-then-forward |        |     | FTV | - Forward-then-verify |           |     |     |     |
| ----- | ------------------- | ------ | --- | --- | --------------------- | --------- | --- | --- | --- |
| NOR - | RFC 5171            | normal |     | AGG | - RFC 5171            | aggresive |     |     |     |
----------------------------------------------------------------------
| Interface | UDLD   | UDLD  |     | UDLD     |     | UDLD Mode | Interval |     |     |
| --------- | ------ | ----- | --- | -------- | --- | --------- | -------- | --- | --- |
|           | Config | State |     | Substate |     | Link      |          |     |     |
----------------------------------------------------------------------
| 1/1/1 | Disabled | Inactive |     | Undetermined  |     | Unblock FTV | 8000 |     |     |
| ----- | -------- | -------- | --- | ------------- | --- | ----------- | ---- | --- | --- |
| 1/1/2 | Enabled  | Active   |     | Bidirectional |     | Unblock FTV | 7000 |     |     |
| 1/1/3 | Enabled  | Active   |     | Blocked       |     | Block FTV   | 7000 |     |     |
| 1/1/4 | Enabled  | Inactive |     | Uninitialized |     | Unblock NOR | 7000 |     |     |
| 1/1/5 | Enabled  | Active   |     | ErrDisabled   |     | Block AGG   | 7000 |     |     |
| 1/1/6 | Disabled | Active   |     | Detection     |     | Unblock NOR | 7000 |     |     |
---------------------------------------------------------------
| Retries | Tx   | Rx   | Rx   |       | Rx   | Transitions |     |     |     |
| ------- | ---- | ---- | ---- | ----- | ---- | ----------- | --- | --- | --- |
|         | Pkts | Pkts | Pkts | disc. | Pkts | drop.       |     |     |     |
---------------------------------------------------------------
| 4   | 4       | 54      | 123   |     | 123     | 1   |     |     |     |
| --- | ------- | ------- | ----- | --- | ------- | --- | --- | --- | --- |
| 7   | 1234567 | 1548421 | 23214 |     | 1878981 | 3   |     |     |     |
| 4   | 3       | 77871   | 2157  |     | 81878   | 1   |     |     |     |
| 5   | 50      | 0       | 0     |     | 0       | 0   |     |     |     |
| 3   | 150     | 25      | 0     |     | 2       | 1   |     |     |     |
| 3   | 6       | 54      | 123   |     | 23      | 1   |     |     |     |
Displayinginformationforinterface1/1/1:
| switch#   | show udld     | interface |     | 1/1/1 |     |     |     |     |     |
| --------- | ------------- | --------- | --- | ----- | --- | --- | --- | --- | --- |
| Interface | 1/1/1         |           |     |       |     |     |     |     |     |
| Config:   | Enabled       |           |     |       |     |     |     |     |     |
| State:    | Active        |           |     |       |     |     |     |     |     |
| Substate: | Bidirectional |           |     |       |     |     |     |     |     |
Link: Unblock
| Version:    | Aruba   | OS           |     |     |     |     |     |     |     |
| ----------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| Mode:       | Forward | then verify  |     |     |     |     |     |     |     |
| Interval:   | 7000    | milliseconds |     |     |     |     |     |     |     |
| Retries:    | 7       |              |     |     |     |     |     |     |     |
| Tx: 1234567 | packets |              |     |     |     |     |     |     |     |
Rx: 1548421 packets, 23214 discarded packets, 1878981 dropped packets
| Port | transitions: | 3   |     |     |     |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
DisplayingtheUDLDenableinterfacesinformation:
| switch# | show udld | enabled |     |     |     |     |     |     |     |
| ------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Abbreviations:
| VTF - | Verify-then-forward |        |     | FTV | - Forward-then-verify |           |     |     |     |
| ----- | ------------------- | ------ | --- | --- | --------------------- | --------- | --- | --- | --- |
| NOR - | RFC 5171            | normal |     | AGG | - RFC 5171            | aggresive |     |     |     |
------------------------------------------------------------------------------------
-------------------------------------------------
| Interface | UDLD   | UDLD  |      | UDLD     |             | UDLD Mode | Interval | Retries | Tx   |
| --------- | ------ | ----- | ---- | -------- | ----------- | --------- | -------- | ------- | ---- |
| Rx        | Rx     |       | Rx   |          | Transitions |           |          |         |      |
|           | Config | State |      | Substate |             | Link      |          |         | Pkts |
| Pkts      | Pkts   | disc. | Pkts | drop.    |             |           |          |         |      |
UDLD|160

------------------------------------------------------------------------------------
-------------------------------------------------
| 2       | Enabled | Active   |       | Bidirectional |     | Unblock FTV | 7000 | 7     |
| ------- | ------- | -------- | ----- | ------------- | --- | ----------- | ---- | ----- |
| 1234567 | 1548421 | 23214    |       | 1878981       | 3   |             |      |       |
| 3       | Enabled | Active   |       | Blocked       |     | Block FTV   | 7000 | 4 3   |
| 77871   | 2157    |          | 81878 |               | 1   |             |      |       |
| 4       | Enabled | Inactive |       | Uninitialized |     | Unblock NOR | 7000 | 5 50  |
| 0       | 0       |          | 0     |               | 0   |             |      |       |
| 5       | Enabled | Active   |       | ErrDisabled   |     | Block AGG   | 7000 | 3 150 |
| 25      | 0       |          | 2     |               | 1   |             |      |       |
udld
Syntax
udld [disable]
no udld
Description
EnablesUDLDsupportonaphysicalinterface.UDLDisdisabledbydefault.UDLDisconfiguredonaper-
portbasisandmustbeenabledatbothendsofthelink.
UDLDrunsonlyonphysicalinterfaces.LAGs,tunnels,andthelikearenotsupported.However,UDLDcan
beconfiguredindividuallyoneachportofaLAGortrunkgroup.ConfiguringUDLDonatrunkgroup's
primaryportenablesUDLDonthatportonly.
ThenoformofthiscommanddisablesUDLDsupportandresetsallconfigurationvaluestotheirdefault
settings.
Commandcontext
config-if
Parameters
disable
DisablesUDLDontheinterfacebutretainsallUDLDconfigurationsettings.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
EnablingUDLDoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1 |     |     |     |     |     |
| ------------------ | --- | --------- | ----- | --- | --- | --- | --- | --- |
| switch(config-if)# |     | udld      |       |     |     |     |     |     |
DisablingUDLDoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1 |     |     |     |     |     |
| ------------------ | --- | --------- | ----- | --- | --- | --- | --- | --- |
| switch(config-if)# |     | no        | udld  |     |     |     |     |     |
udld interval
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 161

Syntax

udld interval <TIME>
no udld interval

Description

Sets the packet transmission interval.

The no form of this command sets the packet transmission interval to the default value of 7000 ms.

The allowed values vary depending on the operation mode.

The default interval is 7000 ms (7 seconds) for both ArubaOS-Switch and RFC5171 operation modes.

Values must be specified as multiples of 10 ms (7000 ms is allowed but 7005 ms is not a valid setting).

Switch mode can be configured to support under 100ms unidirectional link detection times.

Sessions under 100ms total detection time are susceptible to increasing processing load on the system. It is

advisable to experiment with values that provide adequate detection times and system/protocol stability. Aruba

recommends additional testing prior to configuring these sessions on a production environment.

However, these settings are recommended for specific deployments only, such as using UDLD for Ethernet
Ring Protection Switching (ERPS) link-failure detection. The minimum detection time appropriate for your
environment depends on the specific device family and configuration on which the protocol and system
load is running. Aruba recommends additional testing for these configurations. During testing, monitor for
unexpected false positive detections (i.e., UDLD records a failure when there was not any) on the interfaces
running UDLD. Such false positive failures are an indication that the interval configuration requires tuning
and that the system load might not allow such configuration.

When configuring detection times under 100ms for LAG interfaces, consider adding the interface first to the LAG

and then enabling UDLD in the interface, to avoid false positive link failure detections. Adding an interface to a
LAG causes momentary control plane traffic interruption for up to 100ms, which UDLD detects as a link failure if

the detection time is following the control traffic interruption interval.

Command context

config-if

Parameters

<TIME>

Specifies the packet transmission interval. Range: 200 ms to 90000 ms (in increments of 10).

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Setting the packet transmission interval to 1000 ms on interface 1/1/1.

switch(config)# interface 1/1/1
switch(config-if)# udld interval 1000

Setting the packet transmission interval on interface 1/1/1 to the default value.

UDLD | 162

| switch(config)# |     | interface | 1/1/1 |     |
| --------------- | --- | --------- | ----- | --- |
switch(config-if)#
|     |     | no udld | interval |     |
| --- | --- | ------- | -------- | --- |
Tryingtosetthepacketintervalto1055msoninterface1isrejectedbecausetheintervalmustbespecified
asamultipleof10:
switch(config)#
|                    |     | interface | 1        |      |
| ------------------ | --- | --------- | -------- | ---- |
| switch(config-if)# |     | udld      | interval | 1055 |
Invalid interval. The interval value must be between 20ms and 90000ms and should be
specified as a multiple of 10, for example: 20, 100, 3000 or 90000.
Tryingtosetthepacketintervaltolessthan7000msoninterface1isrejectedifusingtheRFC5171mode.
| switch(config)#    |     | interface | 1            |        |
| ------------------ | --- | --------- | ------------ | ------ |
| switch(config-if)# |     | udld      | mode rfc5171 | normal |
| switch(config-if)# |     | udld      | interval     | 1000   |
Invalid interval. The interval must be equal or greater than 7000ms.
udld mode
Syntax
| udld mode | aruba-os | {verify-then-forward |     | | forward-then-verify} |
| --------- | -------- | -------------------- | --- | ---------------------- |
| udld mode | rfc5171  | <RFC5171-MODE>       |     |                        |
| no udld   | mode     |                      |     |                        |
Description
Setstheoperatingmode.
Thenoformofthiscommandsetstheoperatingmodetothedefaultvalueofaruba-osandforward-then-
verify.
Commandcontext
config-if
Parameters
| aruba-os | {verify-then-forward |     | | forward-then-verify} |     |
| -------- | -------------------- | --- | ---------------------- | --- |
SelectstheArubaOSmodetouse.UsethismodewheninterconnectingwithHPE
PVOS/Brocade/Foundryswitches.
verify-then-forward
Inthismode:
| n   | Interfacesstartasunblocked. |     |     |     |
| --- | --------------------------- | --- | --- | --- |
n Onceaninterfaceisdeterminedtobebidirectional,itisblockediftheretrylimitisreachedwithout
receivinganyUDLDpackets.
| n   | InterfacesautomaticallyunblockifaUDLDpacketisreceived. |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- |
n Onfailover,theUDLDstatedoesnotchangeifthe(interval*retries)timeisaround6seconds.
forward-then-verify
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 163

In this mode:

n Interfaces start as unblocked.

n Interfaces transition to the unblocked state when receiving UDLD packets.

n Once an interface is determined to be bidirectional, it is blocked if the retry limit is reached without

receiving any UDLD packets.

n Interfaces automatically unblock if a UDLD packet is received.

rfc5171 <RFC5171-MODE>

Selects the RFC5171 mode to use. Use this mode when interconnecting with third-party switches.
normal

In this mode:

n Interfaces start as unblocked.

n Interfaces do not block when the retry limit is reached without receiving any UDLD packets (plus 8

extra packets sent to the peer). Instead, an event is generated.

n Interfaces automatically unblock if a UDLD packet is received.

aggressive

In this mode:

n Interfaces start as unblocked.

n Once an interface is determined to be bidirectional, an interface will block when the retry limit is

reached without receiving any UDLD packets (plus 8 extra packets sent to the peer).

n Interfaces implement a limited/reduced errDisabled recovery mechanism. When the interface's
state goes to errDisabled, a maximum of 3 attempts (5 minutes apart) are triggered to try and
bring up the interface in case the remote endpoint is still sending UDLD packets. After these 3
retries, the interface will remain blocked even if UDLD packets are received. The only way to
unblock the interface when this occurs is to disable (and optionally re-enable) UDLD on the
interface. The retry limit is reset once the interface becomes unblocked.

Authority

Administrators or local user group members with execution rights for this command.

Examples

On the 6400 Switch Series, interface identification differs.

Setting the operating mode to aruba-os and forward-then-verify on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# udld mode aruba-os forward-then-verify

Setting the operating mode to rfc5171 and aggressive on interface 1/1/1:

switch(config)# interface 1/1/1
switch(config-if)# udld mode rfc5171 aggressive

Setting the operating mode on interface 1/1/1 to the default value:

switch(config)# interface 1/1/1
switch(config-if)# no udld mode

UDLD | 164

udld retries
Syntax
| udld retries <COUNT> |     |     |
| -------------------- | --- | --- |
no retries
Description
SetstheUDLDretrycount.
Thenoformofthiscommandsetstheretrycounttothedefaultvalue.
Commandcontext
config-if
Parameters
<COUNT>
SpecifiestheUDLDretrycount.Range:3to10.Default:4.
Authority
Administratorsorlocalusergroupmemberswithexecutionrightsforthiscommand.
Examples
Onthe6400SwitchSeries,interfaceidentificationdiffers.
SettingtheUDLDretrycountto5oninterface1/1/1:
| switch(config)#    | interface | 1/1/1     |
| ------------------ | --------- | --------- |
| switch(config-if)# | udld      | retries 5 |
SettingtheUDLDretrycountoninterface1/1/1tothedefaultvalue:
| switch(config)#    | interface | 1/1/1   |
| ------------------ | --------- | ------- |
| switch(config-if)# | no udld   | retries |
AOS-CX10.07Layer2BridgingGuide|for6300and6400Switches 165

Support and other resources

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

Accessing updates
You can access updates from the Aruba Support Portal or the HPE My Networking Website.

Aruba Support Portal

AOS-CX 10.07 Layer 2 Bridging Guide | for 6300 and 6400 Switches

166

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

Support and other resources | 167