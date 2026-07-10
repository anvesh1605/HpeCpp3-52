AOS-CX 10.12 Layer-2
Bridging Guide

8400 Switch Series

Published: July 2023
Edition: 1

Copyright Information

© Copyright 2023 Hewlett Packard Enterprise Development LP.

This product includes code licensed under certain open source licenses which require source
compliance. The corresponding source for these components is available upon request. This offer is
valid to anyone in receipt of this information and shall expire three years following the date of the final
distribution of this product version by Hewlett Packard Enterprise Company. To obtain such source
code, please check if the code is available in the HPE Software Center at
https://myenterpriselicense.hpe.com/cwp-ui/software but, if not, send a written request for specific
software version and product for which you want the open source code. Along with the request, please
send a check or money order in the amount of US $10.00 to:

Hewlett Packard Enterprise Company
Attn: General Counsel
WW Corporate Headquarters
1701 E Mossy Oaks Rd Spring, TX 77389
United States of America.

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

Acknowledgment

Intel®, Itanium®, Optane™, Pentium®, Xeon®, Intel Inside®, and the Intel Inside logo are trademarks of
Intel Corporation in the U.S. and other countries.

Microsoft® and Windows® are either registered trademarks or trademarks of Microsoft Corporation in
the United States and/or other countries.

Adobe® and Acrobat® are trademarks of Adobe Systems Incorporated.

Java® and Oracle® are registered trademarks of Oracle and/or its affiliates.

UNIX® is a registered trademark of The Open Group.

All third-party marks are property of their respective owners.

| 2

Contents
Contents
| Contents                            |                                               | 3   |
| ----------------------------------- | --------------------------------------------- | --- |
| About this                          | document                                      | 8   |
| Applicableproducts                  |                                               | 8   |
| Latestversionavailableonline        |                                               | 8   |
| Commandsyntaxnotationconventions    |                                               | 8   |
| Abouttheexamples                    |                                               | 9   |
| Identifyingswitchportsandinterfaces |                                               | 9   |
| Identifyingmodularswitchcomponents  |                                               | 10  |
| Introduction                        |                                               | 11  |
| MAC address                         | table                                         | 12  |
| MACaddresstablecommands             |                                               | 13  |
|                                     | clearmac-address                              | 13  |
|                                     | mac-address-tableage-time                     | 14  |
|                                     | showmac-address-table                         | 15  |
|                                     | showmac-address-tableaddress                  | 16  |
|                                     | showmac-address-tablecount                    | 17  |
|                                     | showmac-address-tabledynamic                  | 18  |
|                                     | showmac-address-tableinterface                | 20  |
|                                     | showmac-address-tablelockout                  | 20  |
|                                     | showmac-address-tableport                     | 21  |
|                                     | showmac-address-tablestatic                   | 22  |
|                                     | showmac-address-tablevlan                     | 23  |
|                                     | static-mac                                    | 23  |
| VLANs                               |                                               | 25  |
| VLANinterfaces                      |                                               | 25  |
|                                     | Accessinterface                               | 25  |
|                                     | Trunkinterface                                | 26  |
|                                     | Traffichandlingsummary                        | 27  |
|                                     | ComparingVLANcommandsonPVOS,Comware,andAOS-CX | 28  |
|                                     | Protocol-mappedVLANs                          | 29  |
|                                     | VLANtranslation                               | 29  |
|                                     | AssigningaVLANtoaninterface                   | 30  |
|                                     | AssigningaVLANIDtoanaccessinterface           | 30  |
|                                     | AssigningaVLANIDtoatrunkinterface             | 31  |
|                                     | AssigninganativeVLANIDtoatrunkinterface       | 32  |
| VLANnumbering                       |                                               | 33  |
| ConfiguringVLANs                    |                                               | 33  |
|                                     | CreatingandenablingaVLAN                      | 33  |
|                                     | DisablingaVLAN                                | 33  |
|                                     | ViewingVLANconfigurationinformation           | 34  |
| VLANscenario                        |                                               | 36  |
| UUFB                                |                                               | 42  |
| VLANcommands                        |                                               | 43  |
|                                     | description                                   | 43  |
3
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

vlan name
show capacities-status vlan-count
show capacities svi-count
show capacities vlan-count
show capacities-status vlan-translation
show vlan
show vlan port
show vlan summary
show vlan translation
show vlan translation pending
show vlan voice
shutdown
trunk-dynamic-vlan-include
uufb
vlan
vlan access
vlan protocol
vlan translate
vlan trunk allowed
vlan trunk native
vlan trunk native tag
voice

QinQ

QinQ feature interactions
QinQ types

Selective QinQ
Transparent QinQ
Configuring and displaying QinQ
QinQ limitations
QinQ commands

debug vlan qinq
diag-dump l2vlan basic
qinq port-type
qinq vlan-map
show qinq
show qinq detail
show qinq interface
show running-config qinq
show tech qinq
svlan

Loop protection

Interaction with other protocols
Configuring loop protection
Loop protect commands
loop-protect
loop-protect action
loop-protect re-enable-timer
loop-protect transmit-interval
loop-protect trap loop-detected
loop-protect vlan
show loop-protect

MVRP

MVRP functionality and limitations

43
44
44
45
46
46
48
49
49
51
51
52
53
54
54
56
57
58
59
61
62
63

64
64
65
65
65
66
67
68
68
68
69
70
70
71
72
73
74
75

77
78
78
80
80
81
82
83
83
84
85

88
88

Contents | 4

| MRPmessages                        |                                       |       | 89  |
| ---------------------------------- | ------------------------------------- | ----- | --- |
|                                    | Joinmessage                           |       | 89  |
|                                    | Newmessage                            |       | 89  |
|                                    | Leavemessage                          |       | 90  |
|                                    | LeaveAllmessage                       |       | 90  |
| ConfiguringMVRP                    |                                       |       | 90  |
| MVRPscenario1                      |                                       |       | 91  |
| MVRPscenario2                      |                                       |       | 95  |
| MVRPcommands                       |                                       |       | 102 |
|                                    | clearmvrpstatistics                   |       | 102 |
|                                    | mvrp                                  |       | 103 |
|                                    | mvrpregistration                      |       | 104 |
|                                    | mvrptimer                             |       | 105 |
|                                    | showmvrpconfig                        |       | 106 |
|                                    | showmvrpstate                         |       | 106 |
|                                    | showmvrpstatistics                    |       | 107 |
| Spanning                           | tree protocols                        | (STP) | 110 |
| Protocolsandfeaturedetails         |                                       |       | 110 |
| STP                                |                                       |       | 110 |
|                                    | Rootbridge                            |       | 110 |
|                                    | Rootport                              |       | 110 |
|                                    | Designatedbridgeanddesignatedport     |       | 110 |
|                                    | Pathcost                              |       | 111 |
|                                    | STPtimers                             |       | 111 |
|                                    | BPDUforwardingmechanism               |       | 112 |
|                                    | STPprotocolpackets                    |       | 112 |
|                                    | Comparingspanningtreeoptions          |       | 113 |
|                                    | Preparingforspanningtreeconfiguration |       | 113 |
|                                    | STPcostcalculation                    |       | 114 |
|                                    | Simplifiedcalculationoverview         |       | 114 |
|                                    | Calculationexample                    |       | 115 |
| STPsupportedplatformsandscale      |                                       |       | 120 |
|                                    | Scale                                 |       | 120 |
| MSTPprotocolandfeaturedetails      |                                       |       | 120 |
|                                    | MSTPkeyconcepts                       |       | 121 |
| MSTPconfigurationtasks             |                                       |       | 124 |
| MSTPconsiderationsandbestpractices |                                       |       | 125 |
| MSTPusecases                       |                                       |       | 126 |
|                                    | MSTPusecase:Preventingloops           |       | 126 |
|                                    | MSTPusecase:Deterministicrootbridges  |       | 129 |
|                                    | SwitchAconfiguration                  |       | 130 |
|                                    | SwitchBconfiguration                  |       | 130 |
|                                    | SwitchCandDconfiguration              |       | 131 |
|                                    | Checkingtheconfiguration              |       | 131 |
|                                    | Observeportbehaviorandstate           |       | 132 |
|                                    | MSTPusecase:BPDUprotection            |       | 134 |
|                                    | MSTPusecase:Rootprotection            |       | 136 |
|                                    | MSTPusecase:Spanningtreeonedgeports   |       | 139 |
| MSTPcommands                       |                                       |       | 142 |
|                                    | clearspanning-treestatistics          |       | 142 |
|                                    | showspanning-tree                     |       | 142 |
|                                    | showspanning-treedetail               |       | 143 |
|                                    | showspanning-treeinconsistent-ports   |       | 145 |
|                                    | showspanning-treemst                  |       | 146 |
|                                    | showspanning-treemst-config           |       | 148 |
5
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

show spanning-tree mst detail
show spanning-tree mst <INSTANCE-ID>
show spanning-tree mst <INSTANCE-ID> detail
show spanning-tree mst interface
show spanning-tree summary port
show spanning-tree summary root
spanning-tree
spanning-tree bpdu-filter
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
spanning-tree tcn-guard
spanning-tree transmit-hold-count
spanning-tree trap

MSTP debugging and troubleshooting
MSTP FAQ
RPVST+ protocol and feature details

RPVST+ vPorts
RPVST+ configuration tasks

Viewing RPVST+ information
RPVST+ Considerations and best practices
RPVST+ use cases

RPVST+ use case: Deterministic root bridges

Switch A configuration
Switch B configuration
Switch C and D configuration
Checking the configuration
Observe port behavior and state

RPVST+ use case: BPDU protection
RPVST+ use case: Root protection
RPVST+ use case: Spanning tree on edge ports
RPVST+ use case: Preventing loops

RPVST+ commands

clear spanning-tree statistics
show capacities rpvst
show capacities-status rpvst
show spanning-tree

149
153
154
155
156
157
158
158
159
160
161
162
163
164
164
165
166
167
168
169
170
171
171
172
174
175
176
177
177
178
179
180
180
183
184
186
189
190
192
192
194
194
195
196
196
197
197
200
203
205
206
209
209
209
210
210

Contents | 6

|                                   | showspanning-treedetail                 |           | 212 |
| --------------------------------- | --------------------------------------- | --------- | --- |
|                                   | showspanning-treeinconsistent-ports     |           | 213 |
|                                   | showspanning-treesummaryport            |           | 214 |
|                                   | showspanning-treesummaryroot            |           | 215 |
|                                   | showspanning-treevlan                   |           | 216 |
|                                   | showspanning-treevlandetail             |           | 217 |
|                                   | spanning-treebpdu-guardtimeout          |           | 219 |
|                                   | spanning-treeextend-system-id           |           | 220 |
|                                   | spanning-treeignore-pvid-inconsistency  |           | 220 |
|                                   | spanning-treelink-type                  |           | 222 |
|                                   | spanning-treemode                       |           | 222 |
|                                   | spanning-treepathcost-type              |           | 224 |
|                                   | spanning-treerpvst-mstpinterconnectvlan |           | 225 |
|                                   | spanning-treetcn-guard                  |           | 225 |
|                                   | spanning-treevlan                       |           | 226 |
|                                   | spanning-treevlancost                   |           | 227 |
|                                   | spanning-treevlanport-priority          |           | 228 |
|                                   | spanning-treetrap                       |           | 229 |
| RPVST+debuggingandtroubleshooting |                                         |           | 232 |
| RPVST+FAQ                         |                                         |           | 233 |
| UDLD                              |                                         |           | 234 |
| ConfiguringUDLD                   |                                         |           | 235 |
| UDLDscenario                      |                                         |           | 236 |
| UDLDcommands                      |                                         |           | 237 |
|                                   | clearudldstatistics                     |           | 237 |
|                                   | showudld                                |           | 238 |
|                                   | udld                                    |           | 240 |
|                                   | udldinterval                            |           | 241 |
|                                   | udldmode                                |           | 243 |
|                                   | udldretries                             |           | 244 |
| Support                           | and Other                               | Resources | 246 |
| AccessingArubaSupport             |                                         |           | 246 |
| AccessingUpdates                  |                                         |           | 247 |
|                                   | ArubaSupportPortal                      |           | 247 |
|                                   | MyNetworking                            |           | 247 |
| WarrantyInformation               |                                         |           | 247 |
| RegulatoryInformation             |                                         |           | 247 |
| DocumentationFeedback             |                                         |           | 248 |
7
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

Chapter 1
About this document
| About | this document |     |     |
| ----- | ------------- | --- | --- |
ThisdocumentdescribesfeaturesoftheAOS-CXnetworkoperatingsystem.Itisintendedfor
administratorsresponsibleforinstalling,configuring,andmanagingArubaswitchesonanetwork.
| Applicable | products |     |     |
| ---------- | -------- | --- | --- |
Thisdocumentappliestothefollowingproducts:
n Aruba8400SwitchSeries(JL366A,JL363A,JL687A)
| Latest | version | available | online |
| ------ | ------- | --------- | ------ |
Updatestothisdocumentcanoccurafterinitialpublication.Forthelatestversionsofproduct
documentation,seethelinksprovidedinSupportandOtherResources.
| Command    | syntax | notation | conventions |
| ---------- | ------ | -------- | ----------- |
| Convention |        | Usage    |             |
example-text Identifiescommandsandtheiroptionsandoperands,codeexamples,
filenames,pathnames,andoutputdisplayedinacommandwindow.Items
thatappearliketheexampletextinthepreviouscolumnaretobeentered
exactlyasshownandarerequiredunlessenclosedinbrackets([ ]).
example-text Incodeandscreenexamples,indicatestextenteredbyauser.
Anyofthefollowing: Identifiesaplaceholder—suchasaparameteroravariable—thatyoumust
n <example-text> substitutewithanactualvalueinacommandorincode:
<example-text>
n
|     |     | n Foroutputformatswhereitalictextcannotbedisplayed,variables |     |
| --- | --- | ------------------------------------------------------------ | --- |
n example-text
areenclosedinanglebrackets(< >).Substitutethetext—including
n example-text
theenclosinganglebrackets—withanactualvalue.
|     |     | n Foroutputformatswhereitalictextcanbedisplayed,variables |     |
| --- | --- | --------------------------------------------------------- | --- |
mightormightnotbeenclosedinanglebrackets.Substitutethe
textincludingtheenclosinganglebrackets,ifany,withanactual
value.
|
Verticalbar.AlogicalORthatseparatesmultipleitemsfromwhichyoucan
chooseonlyone.
Anyspacesthatareoneithersideoftheverticalbarareincludedfor
readabilityandarenotarequiredpartofthecommandsyntax.
{ } Braces.Indicatesthatatleastoneoftheencloseditemsisrequired.
| [ ] |     | Brackets.Indicatesthattheencloseditemoritemsareoptional. |     |
| --- | --- | -------------------------------------------------------- | --- |
8
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

Convention

… or

...

Usage

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

Where <VLAN-ID> is a variable representing the VLAN number.

Identifying switch ports and interfaces
Physical ports on the switch and their corresponding logical software interfaces are identified using the
format:
member/slot/port

On the 8400 Switch Series

About this document | 9

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

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

10

Chapter 2

Introduction

Introduction

Switches use network bridging to facilitate the interconnection of local area networks (LANs) so that
traffic can be exchanged between devices. Bridging occurs at layer 2 of the OSI model.

When creating network bridges on HPE switches, network administrators can configure MAC addressing,
VLANs, and various loop prevention protocols.

Devices on a network are identified by their MAC address. The switch maintains a MAC address table
where it stores information about the other Ethernet interfaces to which a switch is connected. The table
enables the switch to send outgoing data (Ethernet frames) on the specific port required to reach its
destination, instead of broadcasting the data on all ports (flooding).

VLANs are primarily used to provide network segmentation at layer 2. VLANs enable the grouping of
users by logical function instead of physical location. Layer 2 VLANs can be associated with a single
physical port, or multiple aggregated ports (referred to as LAG, short form for Link Aggregation). Link
Aggregation enables a logical grouping of individual interfaces to function as a single, higher-speed link,
providing dramatically increased bandwidth. This mechanism provides network resiliency when
individual link failures occur. Aruba switches include advanced network resiliency through MCLAG (Multi
Chassis Link Aggregation) which offers network resiliency on individual device failure as well.

When multiple individual links are connected to one another, there is a possibility that multiple paths
(loops) will exist between devices. Loops reduce network operational efficiency. AOS-CX provides several
features to detect and avoid loops, including:

n MSTP: Multiple-Instance spanning tree protocol (MSTP) ensures that only one active path exists

between any two nodes in a spanning tree instance. A spanning tree instance comprises a unique set
of VLANs, and belongs to a specific spanning tree region. A region can comprise multiple spanning
tree instances (each with a different set of VLANs), and allows one active path among regions in a
network.

n RPVST+: Rapid Per VLAN Spanning Tree+ (RPVST+) is an updated implementation of STP (Spanning
Tree Protocol). It enables the creation of a separate spanning tree for each VLAN on a switch, and
ensures that only one active, loop-free path exists between any two nodes on a given VLAN.

n Loop Protection: In cases where spanning tree protocols cannot be used to prevent loops at the edge
of the network, loop protection may provide a suitable alternative. Loop protection can find loops in
untagged layer 2 links, as well as on tagged VLANs.

AOS-CX also supports the MVRP (Multiple VLAN Registration Protocol), a registration protocol defined by
IEEE, which propagates VLAN information dynamically across devices. It also enables devices to learn
and automatically synchronize VLAN configuration information, reducing the configuration workload.

Additionally, AOS-CX supports the Unidirectional Link Detection (UDLD) protocol. UDLD monitors the link
between two network devices, and if the link fails, blocks the ports on both ends of the link. UDLD is
useful for detecting failures in fiber links and trunks.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

11

Chapter 3

MAC address table

MAC address table

The MAC address table is where the switch stores information about the other Ethernet interfaces to
which it is connected on a network. The table enables the switch to send outgoing data (Ethernet
frames) on the specific port required to reach its destination, instead of broadcasting the data on all
ports (flooding).

The MAC address table can contain two types of entries:

n Static: Static entries are manually added to the table by a switch administrator. Static entries have

higher priority than dynamic entries. Static entries remain active until they are removed by the switch
administrator.

n Dynamic: Dynamic entries are automatically added to the table through a process called MAC

learning, in which the switch retrieves the source MAC address (and VLAN ID, if present) of each
Ethernet frame received on a port. If the retrieved address does not exist in the table, it is added.
Dynamic entries remain in the table for a predetermined amount of time (defined with the command
mac-address-table age-time), after which they are automatically deleted.

Dynamic MAC address learning does not distinguish between illegitimate and legitimate frames, which
can invite security hazards. When Host A is connected to port A, a MAC address entry will be learned for
the MAC address of Host A (for example, MAC A). When an illegal user sends frames with MAC A as the
source MAC address to port B, the device performs the following operations:

1. Learns a new MAC address entry with port B as the outgoing interface and overwrites the old

entry for MAC A.

2. Forwards frames destined for MAC A out of port B to the illegal user.

As a result, the illegal user obtains the data of Host A. To improve the security for Host A, manually
configure a static entry to bind Host A to port A. Then, the frames destined for Host A are always sent
out of port A. Other hosts using the forged MAC address of Host A cannot obtain the frames destined
for Host A.

For example, in the following topology, switch A learns the MAC addresses of ports on switch B, C, and D.
This way, traffic between any two switches is not broadcast to the other switches. For example, if server
1 sends traffic to server 3, it does not get broadcast onto the link to switch C, only on the link to switch D.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

12

| MAC | address | table commands |     |     |
| --- | ------- | -------------- | --- | --- |
clear mac-address
clear mac-address {interface <INTERFACE> | port <PORT-NUM> [vlan <VLAN-ID>] | vlan <VLAN-
| ID> [port | <PORT-NUM>] | | <MAC-ADDR> | [vlan <VLAN-ID>] | [force]} |
| --------- | ----------- | ------------ | ---------------- | -------- |
Description
ClearsthedynamiclearnedMACaddressesonthespecifiedinterface,combinationofinterfaceand
VLAN,port,VLAN,combinationofportandVLAN,MAC address,orcombinationofMACaddressand
VLAN.Thecommanddoesnotclearanyport-securitylearnedMACaddresses.
Port-securityMAC addressesareclearedwhentheportonwhichtheMACaddresseswerelearnedare
shutdownortheport-access-securityfeatureisdisabledontheportortheswitch.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE> Specifiesthelistofinterfaces,forexample,1/1/1or1/1/1-
1/1/3orlag1orvxlan1.
| <PORT-NUM> |     |     | Specifiesaphysicalportontheswitch.Format: |     |
| ---------- | --- | --- | ----------------------------------------- | --- |
member/slot/port.
| <VLAN-ID>  |     |     | SpecifiesthenumberofaVLAN.                        |     |
| ---------- | --- | --- | ------------------------------------------------- | --- |
| <MAC-ADDR> |     |     | SpecifiestheMAC address.                          |     |
| force      |     |     | ClearsthespecifiedMACaddresseveniftheMACaddressis |     |
internallyprogrammedbyMACmanagement.
Examples
ClearingthelearnedMACaddressesonaport:
MACaddresstable|13

| switch# | clear | mac-address | port | 1/1/1 |     |
| ------- | ----- | ----------- | ---- | ----- | --- |
ClearingthelearnedMACaddressesonacombinationofaVLANandaport:
| switch# | clear | mac-address | port | 1/1/1 vlan | 20  |
| ------- | ----- | ----------- | ---- | ---------- | --- |
switch#
|     | clear | mac-address | vlan | 2 port 1/1/3 |     |
| --- | ----- | ----------- | ---- | ------------ | --- |
ClearingthelearnedMACaddressesonacombinationofaVLANandaninterfaceoralistofinterfaces:
| switch# | clear | mac-address | interface | 1/1/1       | vlan 10     |
| ------- | ----- | ----------- | --------- | ----------- | ----------- |
| switch# | clear | mac-address | vlan      | 1 interface | 1/1/1-1/1/3 |
ClearingthespecifiedMACaddressesentryontheVLAN:
| switch# | clear | mac-address | 14:FA:01:F1:8B:8F |     | vlan 1 |
| ------- | ----- | ----------- | ----------------- | --- | ------ |
ClearingthespecifiedMACaddressesentrybyforce:
| switch#        | clear       | mac-address | 14:FA:01:F1:8B:8F |                                           | force |
| -------------- | ----------- | ----------- | ----------------- | ----------------------------------------- | ----- |
| Command        | History     |             |                   |                                           |       |
| Release        |             |             |                   | Modification                              |       |
| 10.09          |             |             |                   | AddedparametersforinterfaceandMACaddress. |       |
| 10.07orearlier |             |             |                   | --                                        |       |
| Command        | Information |             |                   |                                           |       |
| Platforms      |             | Command     | context           | Authority                                 |       |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| mac-address-table    |     |          | age-time    |     |     |
| -------------------- | --- | -------- | ----------- | --- | --- |
| mac-address-table    |     | age-time | <SECONDS>   |     |     |
| no mac-address-table |     | age-time | [<SECONDS>] |     |     |
Description
SetsthemaximumamountoftimeaMACaddressremainsintheMACaddresstable.Whenthistime
expires,theMACaddressisremoved.
ThenoformofthiscommandresetstheMACagingtimertothedefaultvalue(300seconds).
14
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
age-time <SECONDS> SpecifiestheMACaddressagingtimeinseconds.Range:60to
3600.Default:300.
Example
| switch(config)# | mac-address-table |         | age-time     | 120 |
| --------------- | ----------------- | ------- | ------------ | --- |
| Command         | History           |         |              |     |
| Release         |                   |         | Modification |     |
| 10.07orearlier  |                   |         | --           |     |
| Command         | Information       |         |              |     |
| Platforms       | Command           | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show mac-address-table
| show mac-address-table |     | [hsc] [vsx-peer] |     |     |
| ---------------------- | --- | ---------------- | --- | --- |
Description
ShowsMACaddresstableinformation.IfHSCisenabled,MACaddressesdiscoveredbytheHSC
managerarealsodisplayed.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
[hsc]
DisplaysonlyMACaddressdiscoveredbytheHSCmanageronthe
remotecontroller.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingoutputwhentableentriesexist:
| switch#      | show mac-address-table |               |     |      |
| ------------ | ---------------------- | ------------- | --- | ---- |
| MAC age-time |                        | : 300 seconds |     |      |
| Number       | of MAC addresses       | : 5           |     |      |
| MAC Address  |                        | VLAN Type     |     | Port |
--------------------------------------------------
| 00:00:00:00:00:05 |     | 1 dynamic |     | 1/1/2 |
| ----------------- | --- | --------- | --- | ----- |
| 00:00:00:00:00:06 |     | 2 dynamic |     | 1/1/1 |
MACaddresstable|15

| 00:00:00:00:00:08 |     | 3 hsc | vxlan1(10.1.1.1) |     |
| ----------------- | --- | ----- | ---------------- | --- |
| 00:00:00:00:00:12 |     | 3 hsc | vxlan1(10.1.1.3) |     |
| 00:00:00:00:00:34 |     | 3 hsc | vxlan1(10.1.1.4) |     |
ShowingoutputthatincludesinformationaboutanIPv6VXLAN:
| 3C-T-6300-27# | show             | mac-address-table |     |      |
| ------------- | ---------------- | ----------------- | --- | ---- |
| MAC age-time  |                  | : 300 seconds     |     |      |
| Number        | of MAC addresses | : 2               |     |      |
| MAC Address   |                  | VLAN Type         |     | Port |
--------------------------------------------------------------
| 00:50:56:8d:44:13 |     | 1001 dynamic |     | 1/1/2                    |
| ----------------- | --- | ------------ | --- | ------------------------ |
| 00:50:56:8d:45:63 |     | 1002 evpn    |     | vxlan1(1920:1680:1:1::2) |
ShowingoutputwhentherearenoMACtableentries:
| switch# | show mac-address-table |     |     |     |
| ------- | ---------------------- | --- | --- | --- |
| No MAC  | entries found.         |     |     |     |
ShowingonlyMACaddressdiscoveredbytheHSCmanager:
switch#
|             | show mac-address-table |           | hsc  |     |
| ----------- | ---------------------- | --------- | ---- | --- |
| Number      | of MAC addresses       | : 3       |      |     |
| MAC Address |                        | VLAN Type | Port |     |
---------------------------------------------------------
| 00:00:00:00:00:08 |             | 3 hsc   | vxlan1(10.1.1.1) |     |
| ----------------- | ----------- | ------- | ---------------- | --- |
| 00:00:00:00:00:12 |             | 3 hsc   | vxlan1(10.1.1.3) |     |
| 00:00:00:00:00:34 |             | 3 hsc   | vxlan1(10.1.1.4) |     |
| Command           | History     |         |                  |     |
| Release           |             |         | Modification     |     |
| 10.07orearlier    |             |         | --               |     |
| Command           | Information |         |                  |     |
| Platforms         | Command     | context | Authority        |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show mac-address-table |     | address            |            |     |
| ---------------------- | --- | ------------------ | ---------- | --- |
| show mac-address-table |     | address <MAC-ADDR> | [vsx-peer] |     |
Description
ShowsMACaddresstableinformationforaspecificMACaddress.
16
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| Parameter  |     |     |     | Description             |     |
| ---------- | --- | --- | --- | ----------------------- | --- |
| <MAC-ADDR> |     |     |     | SpecifiestheMACaddress. |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#      | show mac-address-table |      |             | address | 00:00:00:00:00:01 |
| ------------ | ---------------------- | ---- | ----------- | ------- | ----------------- |
| MAC age-time |                        | :    | 300 seconds |         |                   |
| Number       | of MAC addresses       | :    | 2           |         |                   |
| MAC Address  |                        | VLAN | Type        |         | Port              |
--------------------------------------------------
| 00:00:00:00:00:01 |             | 2       | dynamic |              | 1/1/1 |
| ----------------- | ----------- | ------- | ------- | ------------ | ----- |
| 00:00:00:00:00:01 |             | 1       | dynamic |              | 1/1/1 |
| Command           | History     |         |         |              |       |
| Release           |             |         |         | Modification |       |
| 10.07orearlier    |             |         |         | --           |       |
| Command           | Information |         |         |              |       |
| Platforms         | Command     | context |         | Authority    |       |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show mac-address-table |        |            | count |                 |            |
| ---------------------- | ------ | ---------- | ----- | --------------- | ---------- |
| show mac-address-table |        | count      |       |                 |            |
| [dynamic               | | port | <PORT-NUM> | |     | vlan <VLAN-ID>] | [vsx-peer] |
Description
DisplaysthenumberofMACaddresses.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
dynamic
ShowthecountofdynamicallylearnedMACaddresses.
| <PORT-NUM> |     |     |     | Specifiesaphysicalportontheswitch.Format: |     |
| ---------- | --- | --- | --- | ----------------------------------------- | --- |
member/slot/port.
| vlan <VLAN-ID> |     |     |     | SpecifiesthenumberofaVLAN. |     |
| -------------- | --- | --- | --- | -------------------------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
MACaddresstable|17

Examples
ShowingthenumberofMACaddresses:
switch#
|        | show mac-address-table |     | count |     |
| ------ | ---------------------- | --- | ----- | --- |
| Number | of MAC addresses       | : 8 |       |     |
ShowingthenumberofdynamicallylearnedMACaddresses:
| switch# | show mac-address-table |     | count dynamic |     |
| ------- | ---------------------- | --- | ------------- | --- |
| Number  | of MAC addresses       | : 8 |               |     |
ShowingthenumberofMACaddressesperphysicalportontheswitch:
| switch# | show mac-address-table |     | count port | 1/1/1 |
| ------- | ---------------------- | --- | ---------- | ----- |
| Number  | of MAC addresses       | : 2 |            |       |
ShowingthenumberofMACaddressesperVLAN:
| switch# | show mac-address-table |     | count vlan | 100 |
| ------- | ---------------------- | --- | ---------- | --- |
| Number  | of MAC addresses       | : 5 |            |     |
ShowingthenumberofMACaddressesontheVSXprimaryandsecondary(peer)switch:
| vsx-primary#   | show             | mac-address-table | count        |          |
| -------------- | ---------------- | ----------------- | ------------ | -------- |
| Number         | of MAC addresses | : 26114           |              |          |
| vsx-primary#   | show             | mac-address-table | count        | vsx-peer |
| Number         | of MAC addresses | : 26113           |              |          |
| Command        | History          |                   |              |          |
| Release        |                  |                   | Modification |          |
| 10.07orearlier |                  |                   | --           |          |
| Command        | Information      |                   |              |          |
| Platforms      | Command          | context           | Authority    |          |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show mac-address-table |     |     | dynamic |     |
| ---------------------- | --- | --- | ------- | --- |
show mac-address-table dynamic [port <PORT-NUM> | vlan <VLAN-ID>] [vsx-peer]
Description
ShowsMACaddresstableinformationaboutdynamicallylearnedMACaddresses.
18
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| Parameter  |     |     | Description                               |     |
| ---------- | --- | --- | ----------------------------------------- | --- |
| <PORT-NUM> |     |     | Specifiesaphysicalportontheswitch.Format: |     |
member/slot/port.
| <VLAN-ID> |     |     | SpecifiesthenumberofaVLAN. |     |
| --------- | --- | --- | -------------------------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingalldynamicMACaddresstableentries:
| switch#      | show mac-address-table |       | dynamic |      |
| ------------ | ---------------------- | ----- | ------- | ---- |
| MAC age-time |                        | : 300 | seconds |      |
| Number       | of MAC addresses       | : 2   |         |      |
| MAC Address  |                        | VLAN  | Type    | Port |
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
| 00:00:00:00:00:06 |             | 2   | dynamic      | 1/1/1 |
| ----------------- | ----------- | --- | ------------ | ----- |
| Command           | History     |     |              |       |
| Release           |             |     | Modification |       |
| 10.07orearlier    |             |     | --           |       |
| Command           | Information |     |              |       |
MACaddresstable|19

| Platforms | Command | context | Authority |     |
| --------- | ------- | ------- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show mac-address-table |     |           | interface   |     |
| ---------------------- | --- | --------- | ----------- | --- |
| show mac-address-table |     | interface | <INTERFACE> |     |
Description
ShowstheMACaddresstableentriesforthespecifiedinterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<INTERFACE> Specifiesaninterfaceoralistofinterfacesontheswitch.
Examples
ShowingtheMACaddresstableentriesforinterface1/1/1:
| switch#      | show mac-address-table |      | interface   | 1/1/1     |
| ------------ | ---------------------- | ---- | ----------- | --------- |
| MAC age-time |                        | :    | 300 seconds |           |
| Number       | of MAC addresses       | :    | 1           |           |
| MAC Address  |                        | VLAN | Type        | Interface |
--------------------------------------------------
| 00:00:00:00:00:01 |             | 2       | dynamic           | 1/1/1 |
| ----------------- | ----------- | ------- | ----------------- | ----- |
| Command           | History     |         |                   |       |
| Release           |             |         | Modification      |       |
| 10.09             |             |         | Commandintroduced |       |
| Command           | Information |         |                   |       |
| Platforms         | Command     | context | Authority         |       |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show mac-address-table |     |         | lockout    |     |
| ---------------------- | --- | ------- | ---------- | --- |
| show mac-address-table |     | lockout | [vsx-peer] |     |
Description
ShowsMAClockouttableinformation.
20
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#      | show mac-address-table |           | lockout |
| ------------ | ---------------------- | --------- | ------- |
| Number       | of MAC lockout         | addresses | :       |
| 2MAC Address |                        | Type      |         |
------------------------------------------
| 00:00:00:00:01:10 |             | static  |              |
| ----------------- | ----------- | ------- | ------------ |
| 00:00:00:00:10:03 |             | static  |              |
| Command           | History     |         |              |
| Release           |             |         | Modification |
| 10.07orearlier    |             |         | --           |
| Command           | Information |         |              |
| Platforms         | Command     | context | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show mac-address-table |     |                 | port       |
| ---------------------- | --- | --------------- | ---------- |
| show mac-address-table |     | port <PORT-NUM> | [vsx-peer] |
Description
ShowstheMACaddresstableentriesforthespecifiedport.
| Parameter  |     |     | Description                               |
| ---------- | --- | --- | ----------------------------------------- |
| <PORT-NUM> |     |     | Specifiesaphysicalportontheswitch.Format: |
member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingtheMACaddresstableentriesforport1/1/1:
MACaddresstable|21

| switch#      | show mac-address-table |       | port 1/1/1 |      |
| ------------ | ---------------------- | ----- | ---------- | ---- |
| MAC age-time |                        | : 300 | seconds    |      |
| Number       | of MAC addresses       | : 1   |            |      |
| MAC Address  |                        | VLAN  | Type       | Port |
--------------------------------------------------
| 00:00:00:00:00:01 |             | 2       | dynamic      | 1/1/1 |
| ----------------- | ----------- | ------- | ------------ | ----- |
| Command           | History     |         |              |       |
| Release           |             |         | Modification |       |
| 10.07orearlier    |             |         | --           |       |
| Command           | Information |         |              |       |
| Platforms         | Command     | context | Authority    |       |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show mac-address-table |     |        | static |     |
| ---------------------- | --- | ------ | ------ | --- |
| show mac-address-table |     | static |        |     |
Description
ShowsallstaticallyconfiguredMACaddresses.
Examples
| switch#     | show mac-address-table |      | static |     |
| ----------- | ---------------------- | ---- | ------ | --- |
| Number      | of MAC addresses       | : 2  |        |     |
| MAC Address |                        | VLAN | Port   |     |
--------------------------------------
| 00:00:00:00:10:02 |             | 1       | 1/1/1        |     |
| ----------------- | ----------- | ------- | ------------ | --- |
| 00:00:00:00:10:03 |             | 1       | 1/1/1        |     |
| Command           | History     |         |              |     |
| Release           |             |         | Modification |     |
| 10.07orearlier    |             |         | --           |     |
| Command           | Information |         |              |     |
| Platforms         | Command     | context | Authority    |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
22
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| show                   | mac-address-table |     |      |           | vlan |            |
| ---------------------- | ----------------- | --- | ---- | --------- | ---- | ---------- |
| show mac-address-table |                   |     | vlan | <VLAN-ID> |      | [vsx-peer] |
Description
ShowsMACaddresseslearnedbyorconfiguredonthespecifiedVLAN.
| Parameter      |     |     |     |     |     | Description         |
| -------------- | --- | --- | --- | --- | --- | ------------------- |
| vlan <VLAN-ID> |     |     |     |     |     | SpecifiestheVLANID. |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch# | show     | mac-address-table |     |       | vlan    | 1    |
| ------- | -------- | ----------------- | --- | ----- | ------- | ---- |
| MAC     | age-time |                   |     | : 300 | seconds |      |
| Number  | of       | MAC addresses     |     | : 1   |         |      |
| MAC     | Address  |                   |     | VLAN  | Type    | Port |
--------------------------------------------------
| 00:00:00:00:00:01 |             |         |     | 1       | dynamic | 1/1/1        |
| ----------------- | ----------- | ------- | --- | ------- | ------- | ------------ |
| Command           | History     |         |     |         |         |              |
| Release           |             |         |     |         |         | Modification |
| 10.07orearlier    |             |         |     |         |         | --           |
| Command           | Information |         |     |         |         |              |
| Platforms         |             | Command |     | context |         | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
static-mac
| static-mac    | <MAC-ADDR> |            | vlan | <VLAN-ID>      |     | port <PORT-NUM> |
| ------------- | ---------- | ---------- | ---- | -------------- | --- | --------------- |
| no static-mac |            | <MAC-ADDR> |      | vlan <VLAN-ID> |     | port <PORT-NUM> |
Description
AddsastaticMACaddresstotheMACaddresstableandassociatesitwithaportorexistingVLAN.
StaticMACaddressescanonlybeassignedtolayer2(non-routed)interfaces.StaticMACaddressesare
notaffectedbytheMACaddressagingtime.
ThenoformofthiscommanddeletesastaticMACaddress.
MACaddresstable|23

| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<MAC-ADDR>
SpecifiesaMACaddress(xx:xx:xx:xx:xx:xx),wherexisa
hexadecimalnumberfrom0toF.
| vlan <VLAN-ID>  |     |     | SpecifiesnumberofanexistingVLAN.          |     |     |
| --------------- | --- | --- | ----------------------------------------- | --- | --- |
| port <PORT-NUM> |     |     | Specifiesaphysicalportontheswitch.Format: |     |     |
member/slot/port.
Examples
| switch(config)# | static-mac | 00:00:00:00:00:01 |     | vlan 1 port | 1/1/1 |
| --------------- | ---------- | ----------------- | --- | ----------- | ----- |
switch(config)# no static-mac 00:00:00:00:00:01 vlan 1 port 1/1/1
| switch(config)#     | static-mac | 00:00:00:00:00:01 |              | vlan 1 port | 1/1/2 |
| ------------------- | ---------- | ----------------- | ------------ | ----------- | ----- |
| 1/1/2 is            | not an L2  | port              |              |             |       |
| switch(config)#     | static-mac | 00:00:00:00:00:01 |              | vlan 2 port | 1/1/1 |
| VLAN 2 not          | found      |                   |              |             |       |
| Command History     |            |                   |              |             |       |
| Release             |            |                   | Modification |             |       |
| 10.07orearlier      |            |                   | --           |             |       |
| Command Information |            |                   |              |             |       |
| Platforms           | Command    | context           | Authority    |             |       |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
24
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

Chapter 4

VLANs

VLANs

VLANs are primarily used to provide network segmentation at layer 2. VLANs enable the grouping of
users by logical function instead of physical location. They make managing bandwidth usage within
networks possible by:

n Allowing grouping of high-bandwidth users on low-traffic segments

n Organizing users from different LAN segments according to their need for common resources and

individual protocols

n Improving traffic control at the edge of networks by separating traffic of different protocol types.

n Enhancing network security by creating subnets to control in-band access to specific network

resources

VLANs are generally assigned on an organizational basis rather than on a physical basis. For example, a
network administrator could assign all workstations and servers used by a particular workgroup to the
same VLAN, regardless of their physical locations.

Hosts in the same VLAN can directly communicate with one another. A router or a Layer 3 switch is
required for hosts in different VLANs to communicate with one another.

VLANs help reduce bandwidth waste, improve LAN security, and enable network administrators to
address issues such as scalability and network management.

Maximum VLANs allowed

Aruba Switch Series

Maximum VLANs Allowed

8400

4094

VLAN interfaces

Access interface

An access interface carries traffic for a single VLAN ID. Access interfaces are generally used to connect
end devices that do not support VLANs to the network. The devices connected to an access interface are
not aware of the VLAN. Access interface can carry traffic on only one VLAN, either tagged or untagged.

Example

This example shows ingress and egress traffic behavior for an access interface.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

25

n An ingress tagged frame with VLAN ID of 100 arrives on interface 1/2/32. The switch accepts this

frame and sends it to its target address on interface 1/1/32, where it egresses untagged.

n An ingress untagged frame arrives on interface 1/2/32. The switch accepts this frame and sends it to

its target address on interface 1/1/32, where it egresses untagged.

n An ingress tagged frame with VLAN ID of 50 arrives on interface 1/2/32. The switch drops this frame

as VLAN ID 50 is not configured on the interface.

Trunk interface

A trunk interface can carry traffic for one or more VLAN IDs. In most cases, a trunk interface is used to
transport data to other switches or routers.

A trunk interface has two important settings:

n Native VLAN: This is the VLAN to which incoming untagged traffic is assigned. Only one VLAN can be

assigned as the native VLAN. By default, VLAN 1 is assigned as the native VLAN for all trunk
interfaces.

n Allowed VLANs: This is the list of VLANs that can be transported by the trunk. If the native VLAN is not

included in the allowed list, all untagged frames that ingress on the trunk interface are dropped.

Example 1: Native untagged VLAN

This example shows ingress and egress traffic behavior when a trunk interface has a native untagged
VLAN.

n An ingress tagged frame with VLAN ID of 25 arrives on interface 1/1/1. The switch accepts this frame
and sends it to its target address on interface 1/1/2, where it egresses with a VLAN ID of 25 untagged

VLANs | 26

sinceport1/1/2isconfiguredwithanativeVLANIDof25.
n Aningressuntaggedframearrivesoninterface1/1/1.Theswitchacceptsthisframeandsendsitto
itstargetaddressoninterface1/1/2,whereitegresseswithaVLANIDof25untaggedsinceport
1/1/2isconfiguredwithanativeVLANIDof25.
n AningresstaggedframewithVLANIDof4arrivesoninterface1/1/1.Theswitchacceptsthisframe
andsendsittoitstargetaddressoninterface1/1/2,whereitegresseswithaVLANIDof4tagged
sinceport1/1/2isconfiguredtoallowtrafficwithaVLANIDof4.
AningresstaggedframewithVLANIDof50arrivesoninterface1/1/1.Theswitchdropsthisframeas
n
VLANID50isnotintheallowedlistforinterface1/1/1.
| Example | 2: Native | tagged | VLAN |     |
| ------- | --------- | ------ | ---- | --- |
Thisexampleshowsingressandegresstrafficbehaviorwhenatrunkinterfacehasanativetagged
VLAN.
n AningresstaggedframewithVLANIDof6arrivesoninterface1/1/13.Theswitchacceptsthisframe
andsendsittoitstargetaddressoninterface1/1/21,whereitegresseswithaVLANIDof6tagged
sinceport1/1/2isconfiguredwithanativeVLANIDof6.
n Aningressuntaggedframearrivesoninterface1/1/13.Theswitchdropsthisframesincethe
interfaceisconfiguredasnativetagged(alluntaggedframesadroppedinsuchaconfiguration).
AningresstaggedframewithVLANIDof17arrivesoninterface1/1/13.Theswitchacceptsthisframe
n
andsendsittoitstargetaddressoninterface1/1/21,whereitegresseswithaVLANIDof17tagged
sinceport1/1/2isconfiguredtoallowtrafficwithaVLANIDof17.
n AningresstaggedframewithVLANIDof50arrivesoninterface1/1/13.Theswitchdropsthisframe
asVLANID50isnotintheallowedlistforinterface1/1/13.
| Traffic | handling      | summary |                 |                |
| ------- | ------------- | ------- | --------------- | -------------- |
| VLAN    | configuration |         | Ingress traffic | Egress traffic |
Accessinterfacewith:
|     |     |     | 1. Untagged | 1. UntaggedonVLANX |
| --- | --- | --- | ----------- | ------------------ |
VLANID=X
|     |     |     | 2. TaggedwithVLANID=X       | 2. UntaggedonVLANX            |
| --- | --- | --- | --------------------------- | ----------------------------- |
|     |     |     | 3. TaggedwithanyotherVLANID | 3. Droppedatingressportitself |
Trunkinterfacewith:
|     |     |     | 1. Untagged | 1. UntaggedonVLANX |
| --- | --- | --- | ----------- | ------------------ |
n UntaggedNativeVLANID=
|     |     |     | 2. TaggedwithVLANID=X | 2. UntaggedonVLANX |
| --- | --- | --- | --------------------- | ------------------ |
27
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| VLAN configuration |     | Ingress               | traffic |     |     | Egress | traffic       |     |
| ------------------ | --- | --------------------- | ------- | --- | --- | ------ | ------------- | --- |
| X                  |     | 3. TaggedwithVLANID=Y |         |     |     | 3.     | TaggedonVLANY |     |
AllowedVLANIDs=X,Y,Z
| n   |     | 4. TaggedwithVLANID=Z       |     |     |     | 4.  | TaggedonVLANZ              |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | -------------------------- | --- |
|     |     | 5. TaggedwithanyotherVLANID |     |     |     | 5.  | Droppedatingressportitself |     |
Trunkinterfacewith:
|     |     | 1. Untagged |     |     |     | 1.  | UntaggedonVLANX |     |
| --- | --- | ----------- | --- | --- | --- | --- | --------------- | --- |
n UntaggedNativeVLANID=
|     |     | 2. TaggedwithVLANID=X |     |     |     | 2.  | UntaggedonVLANX |     |
| --- | --- | --------------------- | --- | --- | --- | --- | --------------- | --- |
X
n AllowedVLANIDs=ALL 3. TaggedwithaVLANIDdefined 3. TaggedonthematchingVLAN
ontheswitch
4. Droppedatingressportitself
4. TaggedwithaVLANIDnot
definedontheswitch
Trunkinterfacewith:
|     |     | 1. Untagged |     |     |     | 1.  | Droppedatingressportitself |     |
| --- | --- | ----------- | --- | --- | --- | --- | -------------------------- | --- |
n TaggedNativeVLANID=X
|     |     | 2. TaggedwithVLANID=X |     |     |     | 2.  | TaggedonVLANX |     |
| --- | --- | --------------------- | --- | --- | --- | --- | ------------- | --- |
n AllowedVLANIDs=X,Y,Z
|     |     | 3. TaggedwithVLANID=Y       |     |     |     | 3.  | TaggedonVLANY              |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | -------------------------- | --- |
|     |     | 4. TaggedwithVLANID=Z       |     |     |     | 4.  | TaggedonVLANZ              |     |
|     |     | 5. TaggedwithanyotherVLANID |     |     |     | 5.  | Droppedatingressportitself |     |
Trunkinterfacewith:
|     |     | 1. Untagged |     |     |     | 1.  | Droppedatingressportitself |     |
| --- | --- | ----------- | --- | --- | --- | --- | -------------------------- | --- |
n TaggedNativeVLANID=X
|     |     | 2. TaggedwithVLANID=X |     |     |     | 2.  | TaggedonVLANX |     |
| --- | --- | --------------------- | --- | --- | --- | --- | ------------- | --- |
n AllowedVLANIDs=ALL
|     |     | 3. TaggedwithaVLANIDdefined |     |     |     | 3.  | TaggedonthematchingVLAN |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | ----------------------- | --- |
ontheswitch
4. Droppedatingressportitself
4. TaggedwithaVLANIDnot
definedontheswitch
Trunkinterfacewith:
|     |     | 1. Untagged |     |     |     | 1.  | Droppedatingressportitself |     |
| --- | --- | ----------- | --- | --- | --- | --- | -------------------------- | --- |
n UntaggedNativeVLANID=
|     |     | 2. TaggedwithVLANID=X |     |     |     | 2.  | TaggedonVLANX |     |
| --- | --- | --------------------- | --- | --- | --- | --- | ------------- | --- |
A
|     |     | 3. TaggedwithVLANID=Y |     |     |     | 3.  | TaggedonVLANY |     |
| --- | --- | --------------------- | --- | --- | --- | --- | ------------- | --- |
n AllowedVLANIDs=X,Y,Z
|           |               | 4. TaggedwithVLANID=Z       |     |       |          | 4.  | TaggedonVLANZ              |     |
| --------- | ------------- | --------------------------- | --- | ----- | -------- | --- | -------------------------- | --- |
|           |               | 5. TaggedwithanyotherVLANID |     |       |          | 5.  | Droppedatingressportitself |     |
| Comparing | VLAN commands |                             | on  | PVOS, | Comware, |     | and AOS-CX                 |     |
ThefollowingexamplescomparethecommandsneededtoimplementtypicalVLANconfigurationson
differentHPEproducts.
| AOS-CX     |       | PVOS      |      |          |     | Comware   |                 |     |
| ---------- | ----- | --------- | ---- | -------- | --- | --------- | --------------- | --- |
| interface  | 1/1/1 | interface | A1   |          |     | Interface | G1/0/1          |     |
| no routing |       | tagged    | vlan | 10,30,50 |     | port      | link type trunk |     |
vlan trunk native 1 no untagged vlan 1 port trunk permit vlan
| vlan trunk | allowed 10,30,50 |     |     |     |     | 10,30,50 |                 |     |
| ---------- | ---------------- | --- | --- | --- | --- | -------- | --------------- | --- |
|            |                  |     |     |     |     | port     | trunk pvid vlan | 1   |
AnativeVLANmustbedefinedon
| theswitch.Bydefault,thisisVLAN |     |     |     |     |     | PVID1isthedefaultsetting. |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
1.SinceonlyVLANs10,30,and50
areallowedonthetrunk,all
untaggedtrafficisdropped.
VLANs|28

| AOS-CX |     |     | PVOS |     |     | Comware |     |     |     |     |     |
| ------ | --- | --- | ---- | --- | --- | ------- | --- | --- | --- | --- | --- |
interface 1/1/1 Notdirectlysupportedin NotdirectlysupportedinComware.A
| no routing |           |     | PVOS.Scenario1isa     |     |     | possibleworkaroundis: |     |        |     |     |     |
| ---------- | --------- | --- | --------------------- | --- | --- | --------------------- | --- | ------ | --- | --- | --- |
| vlan trunk | native 10 |     | workaroundifthereisno |     |     | interface             |     | g1/0/1 |     |     |     |
vlan trunk allowed 10,30,50 needtosupportuntagged port link-mode bridge
| Sameasscenario1,butallows |     |     | traffic. |     |     |     | port | link-type |               | hybrid |     |
| ------------------------- | --- | --- | -------- | --- | --- | --- | ---- | --------- | ------------- | ------ | --- |
|                           |     |     |          |     |     |     | port | hybrid    | protocol-vlan |        |     |
untaggedtrafficonVLAN10aswell.
|            |       |     |           |      |     | vlan | 10        |           |        |           |     |
| ---------- | ----- | --- | --------- | ---- | --- | ---- | --------- | --------- | ------ | --------- | --- |
|            |       |     |           |      |     |      | port      | hybrid    | vlan   | 10 tagged |     |
|            |       |     |           |      |     |      | port      | hybrid    | vlan   | 30 tagged |     |
|            |       |     |           |      |     |      | port      | hybrid    | vlan   | 50 tagged |     |
| AOS-CX     |       |     | PVOS      |      |     |      | Comware   |           |        |           |     |
| interface  | 1/1/1 |     | interface | A1   |     |      | interface |           | G1/0/1 |           |     |
| no routing |       |     | untagged  | vlan | 5   |      | Port      | link-mode |        | bridge    |     |
vlan trunk native 5 tagged vlan 10,30,50 port link-type trunk
| vlan trunk                       | allowed | 5, 10,30,50 |     |     |     |     | port       | trunk | pvid   | vlan | 5    |
| -------------------------------- | ------- | ----------- | --- | --- | --- | --- | ---------- | ----- | ------ | ---- | ---- |
| VLAN5mustbeallowedonthetrunkso   |         |             |     |     |     |     | port       | trunk | permit |      | vlan |
| thatuntaggedtrafficisnotdropped. |         |             |     |     |     |     | 5,10,30,50 |       |        |      |      |
link-modeisonlyneededon
laterComware7devices.5930is
portlink-moderoutebydefault.
5900isbridgebydefault.
| AOS-CX          |       |       | PVOS      |      |     |     | Comware   |      |           |        |     |
| --------------- | ----- | ----- | --------- | ---- | --- | --- | --------- | ---- | --------- | ------ | --- |
| interface       | 1/1/1 |       | interface | A1   |     |     | interface |      | G1/0/0    |        |     |
| no routing      |       |       | untagged  | vlan | 5   |     |           | port | link-mode | bridge |     |
| vlan access     | 5     |       |           |      |     |     |           | port | access    | vlan   | 5   |
| Protocol-mapped |       | VLANs |           |      |     |     |           |      |           |        |     |
Protocol-mappedVLANsprocesstrafficbasedonthespecifiedprotocol.Anaccessportcanbeapartof
multipleVLANswithonlyoneVLANbeingport-basedandothersbeingprotocol-mappedVLANS.
n Whenprotocol-mappedVLANsareconfigured,untaggedpacketsthatareingressingarecheckedfor
theprotocoltypeandswitchedaccordingtotheprotocol-mappedVLANconfigurationforthat
protocolontheinterface.
n Iftherearenoprotocol-mappedVLANsconfigured,alluntaggedpacketsareswitchedaspartofthe
port-basedVLANthatisconfigured.Packetsegressingonanaccessporthaveno802.1Qheader.Any
packetwithan802.1Qheaderwithanon-zeroVLANIDthatingressesonanaccessportisdropped,
exceptwhentheVLANspecifiedinits802.1QheadermatchestheVLANconfiguredontheaccess
port.
VLAN translation
VLANtranslationisusedtoconfigureasetofVLANtranslationrulesonaninterface.Oncetheserules
areapplied,VLAN-IDsintheincomingandoutgoingpacketsofthatinterfacearemappedtothe
appropriateVLAN-IDsfromthetranslationrules.Thisconfigurationcanbeusedincaseswherethe
VLANidentifiersontheframesneedtobemodifiedattheinterface.
VLANtranslationallowsyoutoconfigurebidirectionalVLANidentifiertranslation.Thisallowsyoutouse
uniqueVLANidentifiersinternallyandmaintainlegacyVLANidentifiersonlogicalinterfaces.Whenthis
configurationisappliedonaninterface,theingresstrafficforthatinterfaceistranslatedfromVLAN1-ID
toVLAN2-ID,andtheegresstrafficforthatinterfaceistranslatedfromVLAN2-IDtoVLAN1-ID.
29
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Formulti-tenancy,VLANtranslationisnotrequiredonISLport,sobestpracticesistoconfigureVLANtranslation
rulesonaccessportsonly.
OntheAruba8400SwitchSeries,IfVLANtranslationsisconfigured,VLANtrunkallowedVLANsare
respectedandtrafficisallowed.
IfaswitchisconfiguredwithaVT rule,thentrafficmustingresstothedeviceinterfacewiththe
VLAN withtheVTrule.IfthetrafficingressestothedeviceinterfacewithanyotherVLAN,trafficmaybe
dropped.
| Maximum   | VLAN          | translation | rules supported |                  |                 |
| --------- | ------------- | ----------- | --------------- | ---------------- | --------------- |
| Aruba     | Switch Series |             | Maximum         | VLAN Translation | Rules Supported |
| 8400      |               |             | 1024            |                  |                 |
| Assigning | a VLAN        | to          | an interface    |                  |                 |
TouseaVLAN,itmustbeassignedtoaninterfaceontheswitch.VLANscanonlybeassignedtonon-
routed(Layer2)interfaces.Allinterfacesarenon-routed(Layer2)bydefaultwhencreated.Userouting
andno routingcommandstomoveportsbetweenLayer3andLayer2interfaces;thismakestheport
anaccessportinVLAN1bydefault.
| Assigning | a VLAN | ID to an | access interface |     |     |
| --------- | ------ | -------- | ---------------- | --- | --- |
Prerequisites
AtleastonedefinedVLAN.
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtotheinterfacethatyouwanttodefineasanaccessinterfacewiththecommand
interface.
| 3. Disableroutingwiththecommandno |     |     |     | routing. |     |
| --------------------------------- | --- | --- | --- | -------- | --- |
4. ConfiguretheaccessinterfaceandassignaVLANIDwiththecommandvlan access.
Examples
Thisexampleconfiguresinterface1/1/2asanaccessinterfacewithVLANIDsetto20.
TheportmustbeanL2port;itcanbeconfiguredasanL2portusingthecommandno routing.
| switch#                 | config |           |       |     |     |
| ----------------------- | ------ | --------- | ----- | --- | --- |
| switch(config)#         |        | vlan 20   |       |     |     |
| switch(config-vlan-20)# |        |           | exit  |     |     |
| switch(config)#         |        | interface | 1/1/2 |     |     |
VLANs|30

| switch(config-lag-if)# |     |     | no  | routing |     |     |
| ---------------------- | --- | --- | --- | ------- | --- | --- |
switch(config-if)#
|     |     | vlan | access | 20  |     |     |
| --- | --- | ---- | ------ | --- | --- | --- |
Thisexamplearangeofinterfaces(1/1/4-1/1/9)asanaccessinterfacewithVLANIDsetto20.
| switch#                          | config |      |             |             |             |     |
| -------------------------------- | ------ | ---- | ----------- | ----------- | ----------- | --- |
| switch(config)#                  |        | vlan | 20          |             |             |     |
| switch(config-vlan-20)#          |        |      | exit        |             |             |     |
| switch(config)#interface         |        |      |             | 1/1/4-1/1/9 |             |     |
| switch(config-lag-if)#           |        |      | no          | routing     |             |     |
| switch(config)#                  |        | int  | 1/1/4-1/1/9 |             |             |     |
| switch(config-if-<1/1/4-1/1/9>)# |        |      |             |             | vlan access | 20  |
ThisexampleconfiguresLAG1asanaccessinterfacewithVLANIDsetto30.
| switch#                 | config |           |         |           |     |     |
| ----------------------- | ------ | --------- | ------- | --------- | --- | --- |
| switch(config)#         |        | vlan      | 30      |           |     |     |
| switch(config-vlan-30)# |        |           | exit    |           |     |     |
| switch(config)#         |        | interface |         | lag 1     |     |     |
| switch(config-lag-if)#  |        |           | no      | shutdown  |     |     |
| switch(config-lag-if)#  |        |           | no      | routing   |     |     |
| switch(config-lag-if)#  |        |           | vlan    | access    | 30  |     |
| Assigning               | a VLAN | ID to     | a trunk | interface |     |     |
Prerequisites
AtleastonedefinedVLAN.
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. Switchtotheinterfacethatyouwanttodefineasatrunkinterfacewiththecommandinterface.
| 3. Disableroutingwiththecommandno |     |     |     |     | routing. |     |
| --------------------------------- | --- | --- | --- | --- | -------- | --- |
4. ConfigurethetrunkinterfaceandassignaVLANIDwiththecommandvlan trunk allowed.
Examples
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDsetto20.
| switch#                 | config |      |      |     |     |     |
| ----------------------- | ------ | ---- | ---- | --- | --- | --- |
| switch(config)#         |        | vlan | 20   |     |     |     |
| switch(config-vlan-20)# |        |      | exit |     |     |     |
switch(config)#
|                        |     | interface |       | 1/1/2   |     |     |
| ---------------------- | --- | --------- | ----- | ------- | --- | --- |
| switch(config-lag-if)# |     |           | no    | routing |     |     |
| switch(config-if)#     |     | vlan      | trunk | allowed | 20  |     |
Thisexampleconfiguresarangeofinterfaces(1/1/4-1/1/9)asatrunkinterfacewithVLANIDsetto20.
| switch#                  | config |      |      |             |     |     |
| ------------------------ | ------ | ---- | ---- | ----------- | --- | --- |
| switch(config)#          |        | vlan | 20   |             |     |     |
| switch(config-vlan-20)#  |        |      | exit |             |     |     |
| switch(config)#interface |        |      |      | 1/1/4-1/1/9 |     |     |
31
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- |

| switch(config-lag-if)# |     |     | no routing |     |     |
| ---------------------- | --- | --- | ---------- | --- | --- |
switch(config)#
int 1/1/4-1/1/9
| switch(config-if-<1/1/4-1/1/9>)# |     |     |     | vlan trunk | allowed 20 |
| -------------------------------- | --- | --- | --- | ---------- | ---------- |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDs2,3,and4.
| switch#         | config |            |       |     |     |
| --------------- | ------ | ---------- | ----- | --- | --- |
| switch(config)# |        | vlan 2,3,4 |       |     |     |
| switch(config)# |        | interface  | 1/1/2 |     |     |
switch(config-lag-if)#
|                    |     |      | no routing |               |     |
| ------------------ | --- | ---- | ---------- | ------------- | --- |
| switch(config-if)# |     | vlan | trunk      | allowed 2,3,4 |     |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDs2to8.
| switch#                | config |           |            |             |     |
| ---------------------- | ------ | --------- | ---------- | ----------- | --- |
| switch(config)#        |        | vlan 2-8  |            |             |     |
| switch(config)#        |        | interface | 1/1/2      |             |     |
| switch(config-lag-if)# |        |           | no routing |             |     |
| switch(config-if)#     |        | vlan      | trunk      | allowed 2-8 |     |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficwithVLANIDs2 to 8and10.
| switch#                | config |             |            |                |     |
| ---------------------- | ------ | ----------- | ---------- | -------------- | --- |
| switch(config)#        |        | vlan 2-8,10 |            |                |     |
| switch(config)#        |        | interface   | 1/1/2      |                |     |
| switch(config-lag-if)# |        |             | no routing |                |     |
| switch(config-if)#     |        | vlan        | trunk      | allowed 2-8,10 |     |
Thisexampleconfiguresinterface1/1/2asatrunkinterfaceallowingtrafficonallconfiguredVLANIDs
(20-100).
| switch#                | config |             |            |             |     |
| ---------------------- | ------ | ----------- | ---------- | ----------- | --- |
| switch(config)#        |        | vlan 20-100 |            |             |     |
| switch(config)#        |        | interface   | 1/1/2      |             |     |
| switch(config-lag-if)# |        |             | no routing |             |     |
| switch(config-if)#     |        | vlan        | trunk      | allowed all |     |
Withtrunkconfiguration,whennativemembershipisnotspecified,theportautomaticallybecomesanative
memberofVLAN1.
| Assigning | a native | VLAN ID | to a trunk | interface |     |
| --------- | -------- | ------- | ---------- | --------- | --- |
Prerequisites
AtleastonedefinedVLAN.
Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. SwitchtothetrunkinterfacetowhichyouwanttoassignthenativeVLANIDwiththecommand
interface.
VLANs|32

| 3. Disableroutingwiththecommandno |     |     |     | routing. |     |
| --------------------------------- | --- | --- | --- | -------- | --- |
4. AssignthenativeVLANIDwiththecommandvlan trunk native.Iftaggingisrequiredforthe
| nativeVLAN,usethecommandvlan |     |     |     | trunk native | tag. |
| ---------------------------- | --- | --- | --- | ------------ | ---- |
5. AllowtraffictaggedwiththenativeVLANIDtobetransportedbythetrunkusingthecommand
| vlan | trunk | allowed. |     |     |     |
| ---- | ----- | -------- | --- | --- | --- |
Example
ThisexampleassignsnativeVLANID20totrunkinterface1/1/2.
| switch#                 | config |            |              |     |     |
| ----------------------- | ------ | ---------- | ------------ | --- | --- |
| switch(config)#         |        | vlan 20    |              |     |     |
| switch(config-vlan-20)# |        |            | exit         |     |     |
| switch(config)#         |        | interface  | 1/1/2        |     |     |
| switch(config-if)#      |        | no routing |              |     |     |
| switch(config-if)#      |        | vlan       | trunk native | 20  |     |
ThisexampleassignsnativeVLANID40totrunkinterface1/1/5,enablestagging,andallowstrafficwith
VLANID40tobetransportedbythetrunk.
| switch#                 | config    |            |              |        |     |
| ----------------------- | --------- | ---------- | ------------ | ------ | --- |
| switch(config)#         |           | vlan 40    |              |        |     |
| switch(config-vlan-40)# |           |            | exit         |        |     |
| switch(config)#         |           | interface  | 1/1/5        |        |     |
| switch(config-if)#      |           | no routing |              |        |     |
| switch(config-if)#      |           | vlan       | trunk native | 40 tag |     |
| switch(config-if)#      |           | vlan       | trunk allow  | 40     |     |
| VLAN                    | numbering |            |              |        |     |
VLANsarenumberedintherange1to4094.
Bydefault,VLAN1(thedefaultVLAN)isassociatedwithallinterfacesontheswitch.VLAN1cannotbe
removedfromtheswitch.
| Configuring |     | VLANs    |        |     |     |
| ----------- | --- | -------- | ------ | --- | --- |
| Creating    | and | enabling | a VLAN |     |     |
Procedure
1. Switchtotheconfigurationcontextwiththecommandconfig.
2. CreateanewVLANwiththecommandvlan.
Example
| ThisexamplecreatesVLAN |        | 10.TheVLANisenabledbydefault. |     |     |     |
| ---------------------- | ------ | ----------------------------- | --- | --- | --- |
| switch#                | config |                               |     |     |     |
| switch(config)#        |        | vlan 10                       |     |     |     |
switch(config-vlan-10)#
| Disabling | a VLAN |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
33
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

Procedure
1. Switchtoconfigurationcontextwiththecommandconfig.
2. SwitchtoconfigurationcontextfortheVLANyouwanttodisablewiththecommandvlan.
3. DisabletheVLANwiththecommandshutdown.
Example
| ThisexampledisablesVLAN |        | 10. |     |     |     |
| ----------------------- | ------ | --- | --- | --- | --- |
| switch(config)#         | config |     |     |     |     |
switch(config)#
vlan 10
| switch(config-vlan-10)# |                    | shutdown |             |     |     |
| ----------------------- | ------------------ | -------- | ----------- | --- | --- |
| Viewing                 | VLAN configuration |          | information |     |     |
Prerequisites
AtleastonedefinedVLAN.
Procedure
1. ViewasummaryofVLANconfigurationinformationwiththecommandshow vlan summary.
| 2. ViewVLANconfigurationsettingswiththecommandshow |     |     |     | vlan. |     |
| -------------------------------------------------- | --- | --- | --- | ----- | --- |
3. ViewVLANsconfiguredforaspecificlayer2interfacewiththecommandshow vlan port.
4. ViewthecommandsusedtoconfigureVLANsettingswiththecommandshow running-config
interface.
Example
ThisexampledisplaysasummaryofallVLANs.
| switch# | show vlan summary |           |     |     |     |
| ------- | ----------------- | --------- | --- | --- | --- |
| Number  | of existing       | VLANs : 2 |     |     |     |
| Number  | of static VLANs   | : 2       |     |     |     |
| Number  | of dynamic VLANs  | : 0       |     |     |     |
| Number  | of port-access    | VLANs: 0  |     |     |     |
ThisexampledisplaysconfigurationinformationforalldefinedVLANs.
| switch# | show vlan |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
-
| VLAN | Name | Status | Reason | Type | Interfaces |
| ---- | ---- | ------ | ------ | ---- | ---------- |
----------------------------------------------------------------------------------
-
| 1   | DEFAULT_VLAN_1 | up  | ok  | static | 1/1/3-1/1/4             |
| --- | -------------- | --- | --- | ------ | ----------------------- |
| 2   | UserVLAN1      | up  | ok  | static | 1/1/1,1/1/3,1/1/5       |
| 3   | UserVLAN2      | up  | ok  | static | 1/1/2-1/1/3,1/1/5-1/1/6 |
| 5   | UserVLAN3      | up  | ok  | static | 1/1/3                   |
| 10  | TestNetwork    | up  | ok  | static | 1/1/3,1/1/5             |
| 11  | VLAN11         | up  | ok  | static | 1/1/3                   |
| 12  | VLAN12         | up  | ok  | static | 1/1/3,1/1/6,lag1-lag2   |
| 13  | VLAN13         | up  | ok  | static | 1/1/3,1/1/6             |
VLANs|34

| 14 VLAN14                                          |      | up   | ok         |     | static | 1/1/3,1/1/6  |     |
| -------------------------------------------------- | ---- | ---- | ---------- | --- | ------ | ------------ | --- |
| 20 ManagementVLAN                                  |      | down | admin_down |     | static | 1/1/3,1/1/10 |     |
| ThisexampledisplaysconfigurationinformationforVLAN |      |      |            |     | 2.     |              |     |
| switch# show                                       | vlan | 2    |            |     |        |              |     |
----------------------------------------------------------------------------------
-
| VLAN Name |     |     | Status | Reason |     | Type | Interfaces |
| --------- | --- | --- | ------ | ------ | --- | ---- | ---------- |
----------------------------------------------------------------------------------
-
| 2 UserVLAN1 |     |     | up  | ok  |     | static | 1/1/1,1/1/3,1/1/5 |
| ----------- | --- | --- | --- | --- | --- | ------ | ----------------- |
ThisexampledisplaystheVLANsconfiguredoninterface1/1/3.
| switch# show | vlan | port 1/1/3 |     |     |     |     |     |
| ------------ | ---- | ---------- | --- | --- | --- | --- | --- |
-------------------------------------------------------------------------------
| VLAN Name |     |     |     | Mode |     | Mapping |     |
| --------- | --- | --- | --- | ---- | --- | ------- | --- |
-------------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1  |     |     |     | native-untagged |     | port |     |
| ----------------- | --- | --- | --- | --------------- | --- | ---- | --- |
| 2 UserVLAN1       |     |     |     | trunk           |     | port |     |
| 3 UserVLAN2       |     |     |     | trunk           |     | port |     |
| 5 UserVLAN3       |     |     |     | trunk           |     | port |     |
| 10 TestNetwork    |     |     |     | trunk           |     | port |     |
| 11 VLAN11         |     |     |     | trunk           |     | port |     |
| 12 VLAN12         |     |     |     | trunk           |     | port |     |
| 13 VLAN13         |     |     |     | trunk           |     | port |     |
| 14 VLAN14         |     |     |     | trunk           |     | port |     |
| 20 ManagementVLAN |     |     |     | trunk           |     | port |     |
| 30 VLAN30         |     |     |     | trunk           |     | port |     |
| 40 VLAN40         |     |     |     | trunk           |     | port |     |
| 50 VLAN50         |     |     |     | trunk           |     | port |     |
| 100 VLAN100       |     |     |     | trunk           |     | port |     |
| 200 VLAN200       |     |     |     | trunk           |     | port |     |
ThisexampledisplaysVLANconfigurationcommandsforinterface1/1/16.
| switch# show | running-config |     | interface | 1/1/16 |     |     |     |
| ------------ | -------------- | --- | --------- | ------ | --- | --- | --- |
| interface    | 1/1/16         |     |           |        |     |     |     |
| no routing   |                |     |           |        |     |     |     |
| vlan trunk   | native         | 108 |           |        |     |     |     |
| vlan trunk   | allowed        | all |           |        |     |     |     |
exit
ThisexampledisplaysVLANconfigurationcommandsforarangeofVLANs:20-30.
| Switch(config)#              | vlan | 20-30 |           |     |     |     |     |
| ---------------------------- | ---- | ----- | --------- | --- | --- | --- | --- |
| Switch(config-vlan-<20-30>)# |      |       | show vlan |     |     |     |     |
----------------------------------------------------------------------------
| VLAN Name |     | Status | Reason |     | Type | Interfaces |     |
| --------- | --- | ------ | ------ | --- | ---- | ---------- | --- |
----------------------------------------------------------------------------
1 DEFAULT_VLAN_1 down no_member_forwarding default 1/3/1-1/3/28,1/5/1-1/5/12,
1/6/1-1/6/12
| 10 VLAN10 |     | down | no_member_port |     | static |     |     |
| --------- | --- | ---- | -------------- | --- | ------ | --- | --- |
| 20 VLAN20 |     | down | no_member_port |     | static |     |     |
35
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- |

| 21 VLAN21 | down no_member_port | static |     |
| --------- | ------------------- | ------ | --- |
| 22 VLAN22 | down no_member_port | static |     |
| 23 VLAN23 | down no_member_port | static |     |
| 24 VLAN24 | down no_member_port | static |     |
| 25 VLAN25 | down no_member_port | static |     |
| 26 VLAN26 | down no_member_port | static |     |
| 27 VLAN27 | down no_member_port | static |     |
| 28 VLAN28 | down no_member_port | static |     |
| 29 VLAN29 | down no_member_port | static |     |
| 30 VLAN30 | down no_member_port | static |     |
6405(config-vlan-<20-30>)#
ThisexampledisplaysVLANconfigurationcommandsforVLANs15,20,25.
| Switch(config)# vlan | 15,20,25 |     |     |
| -------------------- | -------- | --- | --- |
Switch(config-vlan-<15,20,25>)# show vlan
--------------------------------------------------------------------------------------------
--------
| VLAN Name | Status Reason | Type | Interfaces |
| --------- | ------------- | ---- | ---------- |
--------------------------------------------------------------------------------------------
--------
1 DEFAULT_VLAN_1 down no_member_forwarding default 1/3/1-1/3/28,1/5/1-
1/5/12,
1/6/1-
1/6/12
| 15 VLAN15 | down no_member_port | static |     |
| --------- | ------------------- | ------ | --- |
| 20 VLAN20 | down no_member_port | static |     |
| 25 VLAN25 | down no_member_port | static |     |
switch(config-vlan-<15,20,25>)#
VLAN scenario
ThisscenarioshowshowtoassignVLANIDstoaccessandtrunkinterfacesforthefollowing
deployment:
VLANs|36

Inthisscenario,VLANsareusedtoisolatethetrafficfromdifferentdevices.
n VLAN25carriestaggedanduntaggedtrafficfromcomputersconnectedtoswitchB.
n VLAN4carriestaggedtrafficfromcomputersconnectedtoswitchB.
n VLAN6carriestaggedanduntaggedtrafficfromcomputersconnectedtoswitchC.
n VLAN17carriestaggedtrafficfromcomputersconnectedtoswitchC.
n VLAN100carriestagged/untaggedtrafficfromtheserverandonlyuntaggedtraffictotheserver.
Procedure
1. ExecutethefollowingcommandsonswitchAandB.
a. CreateVLANs4and25.
switch# config
| switch(config)# | vlan 4,25 |     |
| --------------- | --------- | --- |
b. DefineLAG1andassigntheVLANstoit.
| switch(config)#        | interface | lag 1                |
| ---------------------- | --------- | -------------------- |
| switch(config-lag-if)# |           | no shutdown          |
| switch(config-lag-if)# |           | no routing           |
| switch(config-lag-if)# |           | vlan trunk native 25 |
switch(config-lag-if)#
|     |     | vlan trunk allowed 4,25 |
| --- | --- | ----------------------- |
no routingisnotamandatorycommandtoaddtheinterfaceinLAG1;whenaddingthe
interfacetoLAG1,thetrunkorroutingtypeisautomaticallyassigned.
37
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

c. Addports1/1/1and1/2/1toLAG1.
| switch(config-lag-if)# |     | interface   |         | 1/1/1 |
| ---------------------- | --- | ----------- | ------- | ----- |
| switch(config-if)#     |     | no shutdown |         |       |
| switch(config-lag-if)# |     | no          | routing |       |
switch(config-if)#
|                        |     | lag 1       |         |     |
| ---------------------- | --- | ----------- | ------- | --- |
| switch(config-if)#     |     | interface   | 1/2/1   |     |
| switch(config-if)#     |     | no shutdown |         |     |
| switch(config-lag-if)# |     | no          | routing |     |
| switch(config-if)#     |     | lag 1       |         |     |
2. ExecutethefollowingcommandsonswitchAandC.
a. CreateVLANs6and17.
| switch# config  |      |      |     |     |
| --------------- | ---- | ---- | --- | --- |
| switch(config)# | vlan | 6,17 |     |     |
b. DefineLAG3andassigntheVLANstoit.
| switch(config)#        | interface |      | lag      | 3            |
| ---------------------- | --------- | ---- | -------- | ------------ |
| switch(config-lag-if)# |           | no   | shutdown |              |
| switch(config-lag-if)# |           | no   | routing  |              |
| switch(config-lag-if)# |           | vlan | trunk    | native 6 tag |
| switch(config-lag-if)# |           | vlan | trunk    | allowed 6,17 |
c. Addports1/1/13and1/2/13toLAG3.
| switch(config-lag-if)# |     | interface   |         | 1/1/13 |
| ---------------------- | --- | ----------- | ------- | ------ |
| switch(config-if)#     |     | no shutdown |         |        |
| switch(config-lag-if)# |     | no          | routing |        |
| switch(config-if)#     |     | lag 3       |         |        |
| switch(config-if)#     |     | interface   | 1/2/13  |        |
| switch(config-if)#     |     | no shutdown |         |        |
| switch(config-if)#     |     | no routing  |         |        |
| switch(config-if)#     |     | lag 3       |         |        |
3. ExecutethefollowingcommandsonswitchAtoconfiguretheconnectiontotheserver.Configure
interface1/2/13asanaccessinterfacewithVLANIDsetto100.
switch# config
| switch (config)#         | vlan | 100        |     |        |
| ------------------------ | ---- | ---------- | --- | ------ |
| switch(config-vlan-100)# |      | interface  |     | 1/2/32 |
| switch(config-if)#       | no   | shutdown   |     |        |
| switch(config-lag-if)#   |      | no routing |     |        |
| switch(config-if)#       | vlan | access     | 100 |        |
| switch(config-if)#       | exit |            |     |        |
4. VerifyVLANconfigurationbyrunningthecommandshow vlan.Forexample:
| switch# show vlan |     |     |     |     |
| ----------------- | --- | --- | --- | --- |
VLANs|38

---------------------------------------------------------------------------
| VLAN Name |     |     | Status | Reason | Type | Interfaces |
| --------- | --- | --- | ------ | ------ | ---- | ---------- |
---------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1 |     |     | down | no_member_port | default |        |
| ---------------- | --- | --- | ---- | -------------- | ------- | ------ |
| 4 VLAN4          |     |     | up   | ok             | static  | lag1   |
| 6 VLAN6          |     |     | up   | ok             | static  | lag3   |
| 17 VLAN17        |     |     | up   | ok             | static  | lag3   |
| 25 VLAN25        |     |     | up   | ok             | static  | lag1   |
| 100 VLAN100      |     |     | up   | ok             | static  | 1/2/32 |
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
6. VerifyLAGinterfaceconfigurationwiththecommandshow interface.Checkthefieldsadmin
state,MACaddress,Aggregated-interfaces,VLANMode,NativeVLAN,AllowedVLAN,Rxcount,
andTxcount.Forexample:
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
|     | 10 input | packets |     | 1280 | bytes |     |
| --- | -------- | ------- | --- | ---- | ----- | --- |
39
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

|     |     | 0 input | error |     |     |     | 0 dropped |     |     |
| --- | --- | ------- | ----- | --- | --- | --- | --------- | --- | --- |
0 CRC/FCS
Tx
|     |     | 8 output | packets |     |     |     | 980 bytes |     |     |
| --- | --- | -------- | ------- | --- | --- | --- | --------- | --- | --- |
|     |     | 0 input  | error   |     |     |     | 0 dropped |     |     |
0 collision
| switch#               | show  | interface     | lag3 |                   |          |     |     |     |     |
| --------------------- | ----- | ------------- | ---- | ----------------- | -------- | --- | --- | --- | --- |
| Aggregate-name        |       | lag3          |      |                   |          |     |     |     |     |
| Description           |       | :             |      |                   |          |     |     |     |     |
| Admin                 | state |               | :    | up                |          |     |     |     |     |
| MAC Address           |       |               | :    | 94:f1:28:21:63:00 |          |     |     |     |     |
| Aggregated-interfaces |       |               | :    | 1/1/13            | 1/2/13   |     |     |     |     |
| Aggregation-key       |       |               | :    | 3                 |          |     |     |     |     |
| Speed                 | 1000  | Mb/s          |      |                   |          |     |     |     |     |
| L3 Counters:          |       | Rx Disabled,  |      | Tx                | Disabled |     |     |     |     |
| qos trust             | none  |               |      |                   |          |     |     |     |     |
| VLAN Mode:            |       | native-tagged |      |                   |          |     |     |     |     |
| Native                | VLAN: | 6             |      |                   |          |     |     |     |     |
| Allowed               | VLAN  | List:         | 6,17 |                   |          |     |     |     |     |
Rx
|     |     | 19 input | packets |     |     |     | 1280 bytes |     |     |
| --- | --- | -------- | ------- | --- | --- | --- | ---------- | --- | --- |
|     |     | 0 input  | error   |     |     |     | 0 dropped  |     |     |
0 CRC/FCS
Tx
|     |     | 15 output | packets |     |     |     | 1000 bytes |     |     |
| --- | --- | --------- | ------- | --- | --- | --- | ---------- | --- | --- |
|     |     | 0 input   | error   |     |     |     | 0 dropped  |     |     |
0 Collision
a. TocheckjusttheLAGinterfacestatistics,youcanusetheshow interface lag 1 statistics
command:
Thefollowingoutputhasbeentruncatedfordisplaypurposesandappearsdifferentlyonthe
switch.
| switch(config-if)# |     | sho | interface |     | lag1 statistics |     |     |     |     |
| ------------------ | --- | --- | --------- | --- | --------------- | --- | --- | --- | --- |
-------------------------------------------------
| Interface |     |     | RX    |     | RX      | RX    |     |     |     |
| --------- | --- | --- | ----- | --- | ------- | ----- | --- | --- | --- |
|           |     |     | Bytes |     | Packets | Drops |     |     |     |
-------------------------------------------------
| 1/1/40 | - lag1 | 1663368814276 |     | 3249823417 |     |     | 0   |     |     |
| ------ | ------ | ------------- | --- | ---------- | --- | --- | --- | --- | --- |
| lag1   |        | 1663368814276 |     | 3249823417 |     |     | 0   |     |     |
-------------------------------------------------
| Interface |     |     | TX    |     | TX      |     | TX    |     |     |
| --------- | --- | --- | ----- | --- | ------- | --- | ----- | --- | --- |
|           |     |     | Bytes |     | Packets |     | Drops |     |     |
-------------------------------------------------------
| 1/1/40 | - lag1 | 2134926620343 |     |     | 4506158466 |     | 50555880 |     |     |
| ------ | ------ | ------------- | --- | --- | ---------- | --- | -------- | --- | --- |
| lag1   |        | 2134926620343 |     |     | 4506158466 |     | 50555880 |     |     |
-------------------------------------------------------
| Interface |     |     | RX        |     | RX        |     | TX        | TX        | RX TX |
| --------- | --- | --- | --------- | --- | --------- | --- | --------- | --------- | ----- |
|           |     |     | Broadcast |     | Multicast |     | Broadcast | Multicast | Pause |
Pause
--------------------------------------------------------------------------------------
VLANs|40

-
| 1/1/40 | -   | lag1 |     | 12823 | 629874 | 204989954 | 185789535 | 0   |
| ------ | --- | ---- | --- | ----- | ------ | --------- | --------- | --- |
0
| lag1 |     |     |     | 12823 | 629874 | 204989954 | 185789535 |     |
| ---- | --- | --- | --- | ----- | ------ | --------- | --------- | --- |
--------------------------------------------------------------------------------------
-
7. Verifythephysicalinterfaces(1/1/1,1/2/1,1/1/13,1/2/13)withthecommandshow interface.
CheckthattheRxandTxfieldsareincrementing.Forexample:
| switch#   | show  | interface |     | 1/1/1 |     |     |     |     |
| --------- | ----- | --------- | --- | ----- | --- | --- | --- | --- |
| Interface |       | 1/1/1 is  | up  |       |     |     |     |     |
| Admin     | state | is up     |     |       |     |     |     |     |
Description:
| Hardware: |     | Ethernet, | MAC | Address: | 94:f1:28:21:73:ff |     |     |     |
| --------- | --- | --------- | --- | -------- | ----------------- | --- | --- | --- |
MTU 1500
Type SFP+LR
| qos              | trust        | none |        |             |              |        |     |     |
| ---------------- | ------------ | ---- | ------ | ----------- | ------------ | ------ | --- | --- |
| Speed            | 1000         | Mb/s |        |             |              |        |     |     |
| Auto-Negotiation |              |      | is off |             |              |        |     |     |
| Input            | flow-control |      | is     | off, output | flow-control | is off |     |     |
Rx
|     |     | 6 input | packets |     | 620       | bytes |     |     |
| --- | --- | ------- | ------- | --- | --------- | ----- | --- | --- |
|     |     | 0 input | error   |     | 0 dropped |       |     |     |
0 CRC/FCS
Tx
|     |     | 4 output | packets |     | 422       | bytes |     |     |
| --- | --- | -------- | ------- | --- | --------- | ----- | --- | --- |
|     |     | 0 input  | error   |     | 0 dropped |       |     |     |
0 collision
8. Verifythelag1interfacewiththecommandshow running-config.Forexample:
switch#
|     | show | running-config |     | interface | lag 1 |     |     |     |
| --- | ---- | -------------- | --- | --------- | ----- | --- | --- | --- |
```
vlan 1
vlan 2
| name | UserVLAN1 |     |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
vlan 3
| name | UserVLAN2 |     |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
vlan 5
| name | UserVLAN3 |     |     |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
vlan 10
| name | TestNetwork |     |     |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
voice
| description |     | This | is  | a test | only VLAN |     |     |     |
| ----------- | --- | ---- | --- | ------ | --------- | --- | --- | --- |
vlan 11-14
vlan 20
| name | ManagementVLAN |     |     |     |     |     |     |     |
| ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
shutdown
vlan 30,40,50,100,200
trunk-dynamic-vlan-incude
| interface |     | lag 1 |     |     |     |     |     |     |
| --------- | --- | ----- | --- | --- | --- | --- | --- | --- |
no shutdown
no routing
| vlan      | access | 12    |     |     |     |     |     |     |
| --------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
| interface |        | lag 2 |     |     |     |     |     |     |
no shutdown
41
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

no routing
vlan access 12

interface 1/1/1
no shutdown
no routing
vlan protocol arp 3
vlan protocol ipv4 3
vlan protocol ipv6 5
vlan access 2

interface 1/1/2
no shutdown
no routing
vlan access 3

interface 1/1/3
no shutdown
no routing
vlan trunk native 1
vlan trunk allowed all

interface 1/1/4
no shutdown
no routing
vlan access 1

interface 1/1/5
no shutdown
no routing
vlan trunk native 1
vlan trunk allowed 2-3,10,20,30,40,50,100
vlan translate 10 20
vlan translate 30 40
vlan translate 50 100

interface 1/1/6
no shutdown
no routing
vlan trunk native 1 tag
vlan trunk allowed 3,12-14,100,200
vlan translate 100 200

interface 1/1/10

no shutdown
no routing
vlan access 20

interface 1/1/11

no shutdown
lag 1

interface 1/1/12

no shutdown
lag 2

```

UUFB
The Unknown Unicast Flood Block (UUFB) feature controls the flooding of unknown unicast packets. By
default, switches flood layer 2 packets to all interfaces within a VLAN if the layer 2 MAC destination
address (DA) is not present in the layer 2 forwarding table. In this scenario, UUFB can be used to block
unknown unicast flooding on a specific port. UUFB can be typically applied on access ports to prevent
flooding of layer 2 packets to other ports within the same VLAN.

UUFB is not supported on 6000 and 6100 Switch Series.

VLANs | 42

| VLAN commands |     |     |     |
| ------------- | --- | --- | --- |
description
| description | <DESCRIPTION> |     |     |
| ----------- | ------------- | --- | --- |
Description
SpecifiesadescriptiveforaVLAN.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<DESCRIPTION>
SpecifiesadescriptionfortheVLAN.
Examples
AssigningadescriptiontoVLAN20:
| switch(config)#         | vlan    | 20          |              |
| ----------------------- | ------- | ----------- | ------------ |
| switch(config-vlan-20)# |         | description | primary      |
| Command History         |         |             |              |
| Release                 |         |             | Modification |
| 10.07orearlier          |         |             | --           |
| Command Information     |         |             |              |
| Platforms               | Command | context     | Authority    |
Allplatforms config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
vlan name
name <VLAN-NAME>
Description
AssociatesanamewithaVLAN.
| Parameter   |     |     | Description                                     |
| ----------- | --- | --- | ----------------------------------------------- |
| <VLAN-NAME> |     |     | SpecifiesanameforaVLAN.Length:1to32alphanumeric |
characters,includingunderscore(_)andhyphen(-).
Usage
n EachnamedVLANmusthaveauniquename;therecannotbeduplicatenamesforVLANs.
n Bydefault,VLANsarecreatedwiththedefaultname:VLAN<VLAN-ID>
Examples
43
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

AssigningthenamebackuptoVLAN20:
| switch(config)#         |             | vlan | 20      |        |              |     |
| ----------------------- | ----------- | ---- | ------- | ------ | ------------ | --- |
| switch(config-vlan-20)# |             |      | name    | backup |              |     |
| Command                 | History     |      |         |        |              |     |
| Release                 |             |      |         |        | Modification |     |
| 10.07orearlier          |             |      |         |        | --           |     |
| Command                 | Information |      |         |        |              |     |
| Platforms               | Command     |      | context |        | Authority    |     |
Allplatforms config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show capacities-status |     |     | vlan-count |     |     |     |
| ---------------------- | --- | --- | ---------- | --- | --- | --- |
| show capacities-status |     |     | vlan-count |     |     |     |
Description
ShowsthenumberofVLANspresentontheswitchandthemaximumnumberofVLANsallowedonthe
switch.
Example
ShowingswitchVLANcapacitystatus:
| show capswitch#    |      | show | capacities-status |       | vlan-count |               |
| ------------------ | ---- | ---- | ----------------- | ----- | ---------- | ------------- |
| System Capacities: |      |      | Filter VLAN       | count |            |               |
| Capacities         | Name |      |                   |       |            | Value Maximum |
-------------------------------------------------------------------------
| Maximum        | number      | of  | VLANs currently |     | configured   | 1 xxxx |
| -------------- | ----------- | --- | --------------- | --- | ------------ | ------ |
| Command        | History     |     |                 |     |              |        |
| Release        |             |     |                 |     | Modification |        |
| 10.07orearlier |             |     |                 |     | --           |        |
| Command        | Information |     |                 |     |              |        |
| Platforms      | Command     |     | context         |     | Authority    |        |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show capacities |     | svi-count |     |     |     |     |
| --------------- | --- | --------- | --- | --- | --- | --- |
| show capacities |     | svi-count |     |     |     |     |
VLANs|44

Description
ShowsthemaximumnumberofSVIssupportedbytheswitch.
Examples
ShowingswitchSVIcapacity:
| switch#            | show | capacities | svi-count  |       |       |
| ------------------ | ---- | ---------- | ---------- | ----- | ----- |
| System Capacities: |      |            | Filter SVI | count |       |
| Capacities         | Name |            |            |       | Value |
---------------------------------------------------------------------
| Maximum | number | of  | SVIs supported | in the system | 128 |
| ------- | ------ | --- | -------------- | ------------- | --- |
ShowingswitchSVIcapacity:
| switch#            | show | capacities | svi-count  |       |       |
| ------------------ | ---- | ---------- | ---------- | ----- | ----- |
| System Capacities: |      |            | Filter SVI | count |       |
| Capacities         | Name |            |            |       | Value |
---------------------------------------------------------------------
| Maximum        | number      | of  | SVIs supported | in the system | 494 |
| -------------- | ----------- | --- | -------------- | ------------- | --- |
| Command        | History     |     |                |               |     |
| Release        |             |     |                | Modification  |     |
| 10.07orearlier |             |     |                | --            |     |
| Command        | Information |     |                |               |     |
| Platforms      | Command     |     | context        | Authority     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show capacities |     | vlan-count |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- |
| show capacities |     | vlan-count |     |     |     |
Description
ShowsthemaximumnumberofVLANsallowedontheswitch.
Example
ShowingswitchVLANcapacity:
| show capswitch#    |      | show | capacities  | vlan-count |       |
| ------------------ | ---- | ---- | ----------- | ---------- | ----- |
| System Capacities: |      |      | Filter VLAN | count      |       |
| Capacities         | Name |      |             |            | Value |
------------------------------------------------------------------------
| Maximum | number  | of  | VLANs supported | in the system | 4094 |
| ------- | ------- | --- | --------------- | ------------- | ---- |
| Command | History |     |                 |               |      |
45
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

| Release        |             |         |         |     | Modification |     |     |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- | --- | --- |
| 10.07orearlier |             |         |         |     | --           |     |     |     |
| Command        | Information |         |         |     |              |     |     |     |
| Platforms      |             | Command | context |     | Authority    |     |     |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show capacities-status |     |     |                  | vlan-translation |     |     |     |     |
| ---------------------- | --- | --- | ---------------- | ---------------- | --- | --- | --- | --- |
| show capacities-status |     |     | vlan-translation |                  |     |     |     |     |
Description
ShowsthenumberofVLANtranslationrulespresentontheswitchandthemaximumnumberofVLAN
translationrulesallowedontheswitch.ThemaximumnumberofVLANtranslationrulesallowedare
1024.
Example
ShowingswitchVLANtranslationrulescapacity:
| switch(config-vlan-100)# |             |     |        | show | capacities  | vlan-translation |     |       |
| ------------------------ | ----------- | --- | ------ | ---- | ----------- | ---------------- | --- | ----- |
| System                   | Capacities: |     | Filter | VLAN | Translation |                  |     |       |
| Capacities               | Name        |     |        |      |             |                  |     | Value |
------------------------------------------------------------------------
| Maximum | number | of  | VLAN Translation |     | rules | supported |     | 1024 |
| ------- | ------ | --- | ---------------- | --- | ----- | --------- | --- | ---- |
switch(config-vlan-100)#
switch(config-vlan-100)#
switch(config-vlan-100)#
switch(config-vlan-100)#
| switch(config-vlan-100)# |            |     |         | show   | capacities-st | vlan-translation |       |         |
| ------------------------ | ---------- | --- | ------- | ------ | ------------- | ---------------- | ----- | ------- |
| System                   | Capacities |     | Status: | Filter | VLAN          | Translation      |       |         |
| Capacities               | Status     |     | Name    |        |               |                  | Value | Maximum |
--------------------------------------------------------------------------
| Number         | of VLAN     | Translation |         | rules | currently    | configured |     | 1 1024 |
| -------------- | ----------- | ----------- | ------- | ----- | ------------ | ---------- | --- | ------ |
| Command        | History     |             |         |       |              |            |     |        |
| Release        |             |             |         |       | Modification |            |     |        |
| 10.07orearlier |             |             |         |       | --           |            |     |        |
| Command        | Information |             |         |       |              |            |     |        |
| Platforms      |             | Command     | context |       | Authority    |            |     |        |
8400 Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show vlan
VLANs|46

| show vlan | [<VLAN-ID>] | [vsx-peer] |     |     |     |     |
| --------- | ----------- | ---------- | --- | --- | --- | --- |
Description
DisplaysconfigurationinformationforallVLANsoraspecificVLAN.
| Parameter |     |     |     | Description       |     |     |
| --------- | --- | --- | --- | ----------------- | --- | --- |
| <VLAN-ID> |     |     |     | SpecifiesaVLANID. |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingconfigurationinformationforVLAN2:
| switch# | show vlan | 2   |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
| VLAN | Name |     |     | Status Reason | Type | Interfaces |
| ---- | ---- | --- | --- | ------------- | ---- | ---------- |
----------------------------------------------------------------------------------
| 2   | UserVLAN1 |     |     | up ok | static | 1/1/1,1/1/3,1/1/5 |
| --- | --------- | --- | --- | ----- | ------ | ----------------- |
DisplayingconfigurationinformationforalldefinedVLANs:
| switch# | show vlan |     |     |     |     |     |
| ------- | --------- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------------
| VLAN | Name |     | Status | Reason | Type | Interfaces |
| ---- | ---- | --- | ------ | ------ | ---- | ---------- |
----------------------------------------------------------------------------------
-
| 1              | DEFAULT_VLAN_1 |         | up   | ok           | static | 1/1/3-1/1/4             |
| -------------- | -------------- | ------- | ---- | ------------ | ------ | ----------------------- |
| 2              | UserVLAN1      |         | up   | ok           | static | 1/1/1,1/1/3,1/1/5       |
| 3              | UserVLAN2      |         | up   | ok           | static | 1/1/2-1/1/3,1/1/5-1/1/6 |
| 5              | UserVLAN3      |         | up   | ok           | static | 1/1/3                   |
| 10             | TestNetwork    |         | up   | ok           | static | 1/1/3,1/1/5             |
| 11             | VLAN11         |         | up   | ok           | static | 1/1/3                   |
| 12             | VLAN12         |         | up   | ok           | static | 1/1/3,1/1/6,lag1-lag2   |
| 13             | VLAN13         |         | up   | ok           | static | 1/1/3,1/1/6             |
| 14             | VLAN14         |         | up   | ok           | static | 1/1/3,1/1/6             |
| 20             | ManagementVLAN |         | down | admin_down   | static | 1/1/3,1/1/10            |
| Command        | History        |         |      |              |        |                         |
| Release        |                |         |      | Modification |        |                         |
| 10.07orearlier |                |         |      | --           |        |                         |
| Command        | Information    |         |      |              |        |                         |
| Platforms      | Command        | context |      | Authority    |        |                         |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
47
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- |

| show vlan      | port           |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| show vlan port | <INTERFACE-ID> |     |     |     |
Description
DisplaystheVLANsconfiguredforaspecificlayer2interface.
| Parameter |     | Description |     |     |
| --------- | --- | ----------- | --- | --- |
<INTERFACE-ID>
SpecifiesaninterfaceID.Format:member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingtheVLANsconfiguredoninterface1/1/1:
| switch# show | vlan port | 1/1/1 |     |     |
| ------------ | --------- | ----- | --- | --- |
-------------------------------------------------------------------------------
| VLAN Name |     |     | Mode | Mapping |
| --------- | --- | --- | ---- | ------- |
-------------------------------------------------------------------------------
| 2 UserVLAN1 |     |     | access | port     |
| ----------- | --- | --- | ------ | -------- |
| 3 UserVLAN2 |     |     | access | arp,ipv4 |
| 5 UserVLAN5 |     |     | access | ipv6     |
DisplayingtheVLANsconfiguredoninterface1/1/3:
| switch# show | vlan port | 1/1/3 |     |     |
| ------------ | --------- | ----- | --- | --- |
-------------------------------------------------------------------------------
| VLAN Name |     |     | Mode | Mapping |
| --------- | --- | --- | ---- | ------- |
-------------------------------------------------------------------------------
| 1 DEFAULT_VLAN_1    |     |              | native-untagged | port |
| ------------------- | --- | ------------ | --------------- | ---- |
| 2 UserVLAN1         |     |              | trunk           | port |
| 3 UserVLAN2         |     |              | trunk           | port |
| 5 UserVLAN3         |     |              | trunk           | port |
| 10 TestNetwork      |     |              | trunk           | port |
| 11 VLAN11           |     |              | trunk           | port |
| 12 VLAN12           |     |              | trunk           | port |
| 13 VLAN13           |     |              | trunk           | port |
| 14 VLAN14           |     |              | trunk           | port |
| 20 ManagementVLAN   |     |              | trunk           | port |
| 30 VLAN30           |     |              | trunk           | port |
| 40 VLAN40           |     |              | trunk           | port |
| 50 VLAN50           |     |              | trunk           | port |
| 100 VLAN100         |     |              | trunk           | port |
| 200 VLAN200         |     |              | trunk           | port |
| Command History     |     |              |                 |      |
| Release             |     | Modification |                 |      |
| 10.07orearlier      |     | --           |                 |      |
| Command Information |     |              |                 |      |
VLANs|48

| Platforms |     | Command | context |     | Authority |     |
| --------- | --- | ------- | ------- | --- | --------- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Manager(#)
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show      | vlan    | summary    |     |     |     |     |
| --------- | ------- | ---------- | --- | --- | --- | --- |
| show vlan | summary | [vsx-peer] |     |     |     |     |
Description
DisplaysasummaryoftheVLANconfigurationontheswitch.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingasummaryoftheVLANconfigurationontheswitch:
| switch#        |             | show vlan | summary |     |              |     |
| -------------- | ----------- | --------- | ------- | --- | ------------ | --- |
| Number         | of          | existing  | VLANs:  | 11  |              |     |
| Number         | of          | static    | VLANs:  | 11  |              |     |
| Number         | of          | dynamic   | VLANs:  | 0   |              |     |
| Command        | History     |           |         |     |              |     |
| Release        |             |           |         |     | Modification |     |
| 10.07orearlier |             |           |         |     | --           |     |
| Command        | Information |           |         |     |              |     |
| Platforms      |             | Command   | context |     | Authority    |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show      | vlan        | translation |            |                   |     |            |
| --------- | ----------- | ----------- | ---------- | ----------------- | --- | ---------- |
| show vlan | translation |             | [interface | <INTERFACE-NAME>] |     | [vsx-peer] |
Description
ShowsasummaryofallVLANtranslationsrulesdefinedontheswitch,ortherulesdefinedforaspecific
interface.
49
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
interface <INTERFACE-NAME> Specifiesthenameofalayer2interface.Format:
member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
DisplayingasummaryofallVLANtranslationsrulesdefinedontheswitch:
| switch# | show vlan | translation |     |     |
| ------- | --------- | ----------- | --- | --- |
-------------------------------------------
| Interface | VLAN-1 | VLAN-2 |     |     |
| --------- | ------ | ------ | --- | --- |
-------------------------------------------
| 1/1/5        | 10  | 20          |           |     |
| ------------ | --- | ----------- | --------- | --- |
| 1/1/5        | 30  | 40          |           |     |
| 1/1/5        | 50  | 100         |           |     |
| 1/1/6        | 100 | 200         |           |     |
| Total number | of  | translation | rules : 4 |     |
DisplayingasummaryofallVLANtranslationsrulesdefinedoninterface1/1/5:
| switch# | show vlan | translation | interface | 1/1/5 |
| ------- | --------- | ----------- | --------- | ----- |
-------------------------------------------
| Interface | VLAN-1 | VLAN-2 |     |     |
| --------- | ------ | ------ | --- | --- |
-------------------------------------------
| 1/1/5 | 10  | 20  |     |     |
| ----- | --- | --- | --- | --- |
| 1/1/5 | 30  | 40  |     |     |
| 1/1/5 | 50  | 100 |     |     |
DisplayingVLAN translationinformationwhenVSX peerisconfigured:
| switch(config-if)# |     | show vlan | translation | vsx-peer |
| ------------------ | --- | --------- | ----------- | -------- |
--------------------------
| Interface | VLAN-1 | VLAN-2 |     |     |
| --------- | ------ | ------ | --- | --- |
--------------------------
| 1/3/1        | 10  | 20          |           |     |
| ------------ | --- | ----------- | --------- | --- |
| Total number | of  | translation | rules : 1 |     |
DisplayingVLAN translationinformationwhenVSX peerisnotconfigured:
| switch(config-if)# |            | show vlan | translation  | vsx-peer |
| ------------------ | ---------- | --------- | ------------ | -------- |
| VSX is not         | configured |           |              |          |
| Command            | History    |           |              |          |
| Release            |            |           | Modification |          |
| 10.07orearlier     |            |           | --           |          |
VLANs|50

| Command   | Information |         |         |     |           |     |     |
| --------- | ----------- | ------- | ------- | --- | --------- | --- | --- |
| Platforms |             | Command | context |     | Authority |     |     |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show      | vlan        | translation |         | pending |     |     |     |
| --------- | ----------- | ----------- | ------- | ------- | --- | --- | --- |
| show vlan | translation |             | pending |         |     |     |     |
Description
ShowsalistofpendingVLANtranslationrules.
Examples
DisplayingalistofVLANtranslationsrulespendingontheswitch:
| switch# |     | show vlan | translation |     | pending |     |     |
| ------- | --- | --------- | ----------- | --- | ------- | --- | --- |
-------------------------------------------
| Interface |     | VLAN-1 |     | VLAN-2 |     |     |     |
| --------- | --- | ------ | --- | ------ | --- | --- | --- |
-------------------------------------------
| 1/1/5 |        | 10  |                  | 20  |       |                   |     |
| ----- | ------ | --- | ---------------- | --- | ----- | ----------------- | --- |
| 1/1/5 |        | 30  |                  | 40  |       |                   |     |
| 1/1/5 |        | 50  |                  | 100 |       |                   |     |
| 1/1/6 |        | 100 |                  | 200 |       |                   |     |
| Total | number | of  | VLAN translation |     | rules | that are pending: | 4   |
DisplayingtheoutputwhentherearenoVLANtranslationrulesinthependinglist:
| switch#        |             | show vlan | translation |       | interface    | 1/1/5 |     |
| -------------- | ----------- | --------- | ----------- | ----- | ------------ | ----- | --- |
| No             | pending     | VLAN      | translation | rules |              |       |     |
| Command        | History     |           |             |       |              |       |     |
| Release        |             |           |             |       | Modification |       |     |
| 10.08orearlier |             |           |             |       | --           |       |     |
| Command        | Information |           |             |       |              |       |     |
| Platforms      |             | Command   | context     |       | Authority    |       |     |
8400 Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
| show      | vlan  | voice |     |     |     |     |     |
| --------- | ----- | ----- | --- | --- | --- | --- | --- |
| show vlan | voice |       |     |     |     |     |     |
Description
51
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- |

DisplaysthevoiceVLANlistshowingtheVLANID,name,operationalstateoftheVLAN,andthe
interfacesassociatedwiththeVLAN.
Example
DisplayingthevoiceVLANslist:
| switch# | show vlan | voice |     |     |     |
| ------- | --------- | ----- | --- | --- | --- |
----------------------------------------------------------------------------------
------------
| VLAN Name |     |     | Status | Type | Interfaces |
| --------- | --- | --- | ------ | ---- | ---------- |
----------------------------------------------------------------------------------
------------
| 10 TestNetwork |     |     | up  | static |     |
| -------------- | --- | --- | --- | ------ | --- |
1/1/3,1/1/5
DisplayingtheinformationwhenvoiceVLANsarenotconfigured:
| switch#             | show vlan      | voice   |              |     |     |
| ------------------- | -------------- | ------- | ------------ | --- | --- |
| Voice VLAN          | not configured |         |              |     |     |
| Command History     |                |         |              |     |     |
| Release             |                |         | Modification |     |     |
| 10.07orearlier      |                |         | --           |     |     |
| Command Information |                |         |              |     |     |
| Platforms           | Command        | context | Authority    |     |     |
Allplatforms Manager(#) OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
commandfromtheoperatorcontext(>)only.
shutdown
shutdown
no shutdown
Description
DisablesaVLAN.(Bydefault,aVLANisautomaticallyenabledwhenitiscreatedwiththevlan
command.)
ThenoformofthiscommandenablesaVLAN.
Examples
EnablingVLAN20:
| switch(config)#         | vlan | 20          |     |     |     |
| ----------------------- | ---- | ----------- | --- | --- | --- |
| switch(config-vlan-20)# |      | no shutdown |     |     |     |
DisablingVLAN20:
VLANs|52

| switch(config)# | vlan | 20  |     |
| --------------- | ---- | --- | --- |
switch(config-vlan-20)#
shutdown
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
trunk-dynamic-vlan-include
trunk-dynamic-vlan-include
no trunk-dynamic-vlan-include
Description
IndicatesifdynamicallylearnedVLANsfromMVRPandport-accessshouldbeincludedorexcludedon
portsconfiguredwithvlan trunk allowed all.Bydefault,dynamicVLANsarenotincludedinthe
trunkallowedlist.Thiscommandisusedatthesystem-level.
ThenoformofthiscommanddisablestheinclusionofdynamicVLANsintheVLANstable.Thisisthe
default.
Examples
IncludingthedynamicVLANsintheVLANtable:
| switch(config)# | trunk-dynamic-vlan-include |     |     |
| --------------- | -------------------------- | --- | --- |
DisablingtheinclusionofdynamicVLANsintheVLANtable(default):
| switch(config)#     | no      | trunk-dynamic-vlan-include |                   |
| ------------------- | ------- | -------------------------- | ----------------- |
| Command History     |         |                            |                   |
| Release             |         |                            | Modification      |
| 10.08               |         |                            | Commandintroduced |
| Command Information |         |                            |                   |
| Platforms           | Command | context                    | Authority         |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
53
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

uufb
uufb
no uufb
Description
EnablestheUnknownUnicastFloodBlock(UUFB)featureonaphysicalinterface.Whenthisfeatureis
enabledonaphysicalinterface,unknownunicastpacketsareblockedfromegressingthephysical
interface.Thisfeatureisdisabledbydefault.
UUFBcanbeenabledonlyonthephysicalinterface.
UUFB cannotbeenabledon:
n Routedinterface
n LAGs
n VSXinter-switchlink
n InterfaceusedasanISL
Examples
EnablingUUFBonanL2accessport:
| switch(config)#    |     | interface | 1/1/1  |     |
| ------------------ | --- | --------- | ------ | --- |
| switch(config-if)# |     | vlan      | access | 1   |
| switch(config-if)# |     | uufb      |        |     |
EnableUUFBonanL2trunkport:
| switch(config)#    |     | interface | 1/1/1 |             |
| ------------------ | --- | --------- | ----- | ----------- |
| switch(config-if)# |     | vlan      | trunk | allowed all |
| switch(config-if)# |     | uufb      |       |             |
DisablingUUFBonanL2accessortrunkport:
| switch(config-if)#  |         | no uufb |     |                    |
| ------------------- | ------- | ------- | --- | ------------------ |
| Command History     |         |         |     |                    |
| Release             |         |         |     | Modification       |
| 10.11               |         |         |     | Commandintroduced. |
| Command Information |         |         |     |                    |
| Platforms           | Command | context |     | Authority          |
8400 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
vlan
VLANs|54

vlan <VLAN-LIST>
no vlan <VLAN-LIST>
Description
CreatesaVLANandchangestotheconfig-vlan-idcontextfortheVLAN.Bydefault,theVLANis
enabled.TodisableaVLAN,usetheshutdowncommand.
IfthespecifiedVLANexists,thiscommandchangestotheconfig-vlan-idcontextfortheVLAN.Ifa
rangeofVLANsisspecified,thecontextdoesnotchange.
VLANsusedforinternalpurposesusingthecommandsystem internal vlan rangecannotbeusedforany
other(L2)purposes.
ThenoformofthiscommandremovesaVLAN.VLAN1isthedefaultVLANandcannotbedeleted.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-LIST> SpecifiesasingleID,oraseriesofIDsseparatedbycommas(2,3,
4),dashes(2-4),orboth(2-4,6).Range:1to4094.
Examples
CreatingVLAN20:
| switch(config)# | vlan | 20  |     |
| --------------- | ---- | --- | --- |
switch(config-vlan-20)#
RemovingVLAN20:
| switch(config)# | no vlan | 20  |     |
| --------------- | ------- | --- | --- |
CreatingVLANs2to8and10:
switch(config)#
|     | vlan | 2-8,10 |     |
| --- | ---- | ------ | --- |
RemovingVLANs2to8and10:
| switch(config)# | no vlan | 2-8,10 |     |
| --------------- | ------- | ------ | --- |
CreatingaVLANwhichisalreadyconfiguredasaninternalVLAN:
| switch(config)# | vlan      | 3001        |               |
| --------------- | --------- | ----------- | ------------- |
| Ignoring the    | operation | on internal | VLAN(s) 3001. |
DeletinganunconfiguredVLANwhichisalreadyconfiguredasinternalVLAN:
switch(config)#
|                 | no vlan   | 300                |              |
| --------------- | --------- | ------------------ | ------------ |
| Ignoring the    | operation | for non-configured | VLAN(s) 300. |
| Command History |           |                    |              |
55
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
vlan access
| vlan access    | <VLAN-ID>   |     |     |     |
| -------------- | ----------- | --- | --- | --- |
| no vlan access | [<VLAN-ID>] |     |     |     |
Description
CreatesanaccessinterfaceandassignsanVLANIDtoit.OnlyoneVLANIDcanbeassignedtoeach
accessinterface.
VLANscanonlybeassignedtonon-routed(Layer2)interfaces.Allinterfacesarenon-routed(Layer2)by
defaultwhencreated.Useroutingandno routingcommandstomoveportsbetweenLayer3and
Layer2interfaces.
ThenoformofthiscommandremovesanaccessVLANfromtheinterfaceinthecurrentcontextand
setsittothedefaultVLANIDof1.
| Command context |     |     |     |             |
| --------------- | --- | --- | --- | ----------- |
| Parameter       |     |     |     | Description |
<VLAN-ID> SpecifiesasingleID,oraseriesofIDsseparatedbycommas(2,3,
4),dashes(2-4),orboth(2-4,6).Range:1to4094.
Examples
Configuringinterface1/1/2asanaccessinterfacewithVLANIDsetto20:
| switch(config)#    |     | interface  | 1/1/2  |     |
| ------------------ | --- | ---------- | ------ | --- |
| switch(config-if)# |     | no routing |        |     |
| switch(config-if)# |     | vlan       | access | 20  |
RemovingVLANID20frominterface1/1/2:
| switch(config)#    |     | interface | 1/1/2  |     |
| ------------------ | --- | --------- | ------ | --- |
| switch(config-if)# |     | no vlan   | access | 20  |
or:
| switch(config)#    |     | interface | 1/1/2  |     |
| ------------------ | --- | --------- | ------ | --- |
| switch(config-if)# |     | no vlan   | access |     |
| Command History    |     |           |        |     |
VLANs|56

| Release        |             |     |         |     | Modification |
| -------------- | ----------- | --- | ------- | --- | ------------ |
| 10.07orearlier |             |     |         |     | --           |
| Command        | Information |     |         |     |              |
| Platforms      | Command     |     | context |     | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
vlan protocol
| vlan protocol    | <PROTOCOL_NAME> |                 |     | <VLAN-ID> |           |
| ---------------- | --------------- | --------------- | --- | --------- | --------- |
| no vlan protocol |                 | <PROTOCOL_NAME> |     |           | <VLAN-ID> |
Description
AddsprotocolmappingtoaVLANonaninterface.
ThenoformofthiscommandremovesprotocolmappingfromtheVLANonaninterface.
| Parameter |     |     |     |     | Description                     |
| --------- | --- | --- | --- | --- | ------------------------------- |
| <VLAN-ID> |     |     |     |     | SpecifiesaVLANID.Range:2to4094. |
<PROTOCOL_NAME>
SpecifiestheprotocolthattheVLANisboundtoforagiven
interface.Optionsare:AppleTalk,ARP,IPv4,IPv6,IPX,NetBEUI,
andSNA.
Usage
Thiscommandisonlyapplicabletoaccessports.
n
n ProtocolVLANshouldbedifferentfromaccessVLANs.
n VLANshouldbeconfiguredontheswitch.
n Routingmustbedisabledontheinterface.
n InterfacemustbeaphysicalorLAGinterface.
n Thesameprotocol-mappedVLANisrecommendedforARPandIPv4protocolstoavoidIPv4traffic
loss.
Examples
AssigningaprotocolmappingtoaVLANonaninterface:
| switch(config)#    |     | interface |      | 1/1/2    |         |
| ------------------ | --- | --------- | ---- | -------- | ------- |
| switch(config-if)# |     |           | vlan | protocol | ipv4 10 |
AssigningaprotocolmappingtoaVLANonaLAGinterface:
| switch(config)#        |     | interface |     | lag           | 2       |
| ---------------------- | --- | --------- | --- | ------------- | ------- |
| switch(config-lag-if)# |     |           |     | vlan protocol | ipv6 10 |
RemovingaprotocolmappingfromaVLANonaninterface:
57
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

| switch(config)# | interface | 1/1/2 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
|     |     | no vlan protocol | ipv6 10 |
| --- | --- | ---------------- | ------- |
RemovingaprotocolmappingfromaVLANonaLAGinterface:
| switch(config)#        | interface | lag 2   |                  |
| ---------------------- | --------- | ------- | ---------------- |
| switch(config-lag-if)# |           | no vlan | protocol ipv6 10 |
| Command History        |           |         |                  |
| Release                |           |         | Modification     |
| 10.07orearlier         |           |         | --               |
| Command Information    |           |         |                  |
| Platforms              | Command   | context | Authority        |
config-if
8400 Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-lag-if |     | forthiscommand. |
| --- | ------------- | --- | --------------- |
vlan translate
| vlan translate    | <VLAN-1> | <VLAN-2> |     |
| ----------------- | -------- | -------- | --- |
| no vlan translate | <VLAN-1> | <VLAN-2> |     |
Description
DefinesabidirectionalVLANtranslationrulethatmapsanoriginalVLANID(VLAN-1)toatranslated
internalVLANID(VLAN-2)onaLAGorlayer2interface.Appliestobothincomingandoutgoingtraffic.
ThenoformofthiscommandremovesanexistingVLANtranslationruleonthecurrentinterface.
VLANtranslationandMVRPcannotbeenabledonthesameinterface.
AtranslatedVLANmustbepresentontheswitchbeforetheruleiscreated;theoriginalVLANneednotbe
present.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-1>
SpecifiesthenumberofanoriginVLAN.Range:1-4094.
<VLAN-2>
SpecifiesthenumberofatranslatedVLAN.Range:1-4094.
Usage
n Thisconfigurationcanbeappliedonlyonlayer2trunkports.
n Routingmustbedisabledontheinterface.
n Interfacemustbealayer2physicalorLAGinterface.
n MaximumuniqueVLANtranslationrulessupportedontheAruba8400SwitchSeries—1024
VLANs|58

Examples
TranslatesoriginVLAN200totranslatedVLAN20oninterface1/1/2.
switch#
config
| switch(config)#         |     | vlan      | 20             |         |        |
| ----------------------- | --- | --------- | -------------- | ------- | ------ |
| switch(config-vlan-20)# |     |           | exit           |         |        |
| switch(config)#         |     | interface |                | 1/1/2   |        |
| switch(config-if)#      |     |           | no routing     |         |        |
| switch(config-if)#      |     |           | vlan trunk     | allowed | 20     |
| switch(config-if)#      |     |           | vlan translate |         | 200 20 |
TranslatesoriginVLANs100and300totranslatedVLANs10and20oninterface1/1/2.
| switch# | config |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- |
switch(config)#
vlan 10,30
| switch(config-vlan-20)# |             |           | exit           |         |              |
| ----------------------- | ----------- | --------- | -------------- | ------- | ------------ |
| switch(config)#         |             | interface |                | 1/1/2   |              |
| switch(config-if)#      |             |           | no routing     |         |              |
| switch(config-if)#      |             |           | vlan trunk     | allowed | 10,30        |
| switch(config-if)#      |             |           | vlan translate |         | 100 10       |
| switch(config-if)#      |             |           | vlan translate |         | 300 30       |
| Command                 | History     |           |                |         |              |
| Release                 |             |           |                |         | Modification |
| 10.07orearlier          |             |           |                |         | --           |
| Command                 | Information |           |                |         |              |
| Platforms               | Command     |           | context        |         | Authority    |
8400 config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| vlan trunk | allowed       |              |               |     |      |
| ---------- | ------------- | ------------ | ------------- | --- | ---- |
| vlan trunk | allowed       | [<VLAN-LIST> |               | |   | all] |
| no vlan    | trunk allowed |              | [<VLAN-LIST>] |     |      |
Description
AssignsaVLANIDtoantrunkinterface.MultipleVLANIDscanbeassignedtoatrunkinterface.These
VLANIDsdefinewhichVLANtrafficisallowedacrossthetrunkinterface.
VLANscanonlybeassignedtonon-routed(Layer2)interfaces.Allinterfacesarenon-routed(Layer2)by
defaultwhencreated.Useroutingandno routingcommandstomoveportsbetweenLayer3and
Layer2interfaces.
ThenoformofthiscommandremovesoneormoreVLANIDsfromatrunkinterface.Whenthelast
VLANisremovedfromatrunkinterface,theinterfacecontinuestooperateintrunkmode,andwill
trunkalltheVLANscurrentlydefinedontheswitch,andanynewVLANsdefinedinthefuture.Todisable
thetrunkinterface,usethecommandshutdown.
59
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<VLAN-LIST> SpecifiesasingleID,oraseriesofIDsseparatedbycommas(2,3,
4),dashes(2-4),orboth(2-4,6).Range:1to4094.
| all |     |     |     | ConfiguresthetrunkinterfacetoallowalltheVLANscurrently |
| --- | --- | --- | --- | ------------------------------------------------------ |
configuredontheswitchandanynewVLANsthatareconfigured
inthefuture.
Examples
AssigningVLANs2,3,and4totrunkinterface1/1/2:
| switch(config)#    |     | interface  | 1/1/2 |               |
| ------------------ | --- | ---------- | ----- | ------------- |
| switch(config-if)# |     | no routing |       |               |
| switch(config-if)# |     | vlan       | trunk | allowed 2,3,4 |
AssigningVLANIDs2to8totrunkinterface1/1/2:
| switch(config)#    |     | interface  | 1/1/2 |             |
| ------------------ | --- | ---------- | ----- | ----------- |
| switch(config-if)# |     | no routing |       |             |
| switch(config-if)# |     | vlan       | trunk | allowed 2-8 |
AssigningVLANIDs2to8and10totrunkinterface1/1/2:
| switch(config)#    |     | interface  | 1/1/2 |                |
| ------------------ | --- | ---------- | ----- | -------------- |
| switch(config-if)# |     | no routing |       |                |
| switch(config-if)# |     | vlan       | trunk | allowed 2-8,10 |
RemovingVLANIDs2,3,and4fromtrunkinterface1/1/2:
| switch(config)#    |     | interface | 1/1/2 |               |
| ------------------ | --- | --------- | ----- | ------------- |
| switch(config-if)# |     | no vlan   | trunk | allowed 2,3,4 |
RemovingallVLANsassignedtotrunkinterface1/1/2:
| switch(config)#     |         | interface | 1/1/2 |              |
| ------------------- | ------- | --------- | ----- | ------------ |
| switch(config-if)#  |         | no vlan   | trunk | allowed 2    |
| Command History     |         |           |       |              |
| Release             |         |           |       | Modification |
| 10.07orearlier      |         |           |       | --           |
| Command Information |         |           |       |              |
| Platforms           | Command | context   |       | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
VLANs|60

| vlan trunk native    |             |     |
| -------------------- | ----------- | --- |
| vlan trunk native    | <VLAN-ID>   |     |
| no vlan trunk native | [<VLAN-ID>] |     |
Description
AssignsanativeVLANIDtoatrunkinterface.Bydefault,VLANID1isassignedasthenativeVLANIDfor
alltrunkinterfaces.VLANscanonlybeassignedtoanon-routed(layer2)interfaceorLAGinterface.
OnlyoneVLANIDcanbeassignedasthenativeVLAN.
WhenanativeVLANisdefined,theswitchautomaticallyexecutesthevlan trunk allowed allcommandto
ensurethatthedefaultVLANisallowedonthetrunk.ToonlyallowspecificVLANsonthetrunk,issuethevlan
trunk allowedcommandspecifyingonlyspecificVLANs.
ThenoformofthiscommandremovesanativeVLANfromatrunkinterfaceandassignsVLANID1asits
nativeVLAN.
Parameter Description
<VLAN-ID> SpecifiesaVLANID.Range:1to4094.
Examples
AssigningnativeVLANID20totrunkinterface1/1/2:
| switch(config)#    | interface  | 1/1/2           |
| ------------------ | ---------- | --------------- |
| switch(config-if)# | no routing |                 |
| switch(config-if)# | vlan       | trunk native 20 |
RemovingnativeVLAN20fromtrunkinterface1/1/2andreturningtothedefaultVLAN1asthenative
VLAN.
| switch(config)#    | interface | 1/1/2           |
| ------------------ | --------- | --------------- |
| switch(config-if)# | no vlan   | trunk native 20 |
or:
| switch(config)#    | interface | 1/1/2        |
| ------------------ | --------- | ------------ |
| switch(config-if)# | no vlan   | trunk native |
AssigningnativeVLANID20totrunkinterface1/1/2andthenremovingitfromthelistofallowed
VLANs.(OnlyallowVLAN10onthetrunk.)
| switch(config)#    | interface  | 1/1/2            |
| ------------------ | ---------- | ---------------- |
| switch(config-if)# | no routing |                  |
| switch(config-if)# | vlan       | trunk native 20  |
| switch(config-if)# | vlan       | trunk allowed 10 |
Command History
61
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| Release        |             |     |         |     | Modification |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| vlan trunk | native       |           | tag |     |     |     |
| ---------- | ------------ | --------- | --- | --- | --- | --- |
| vlan trunk | native       | <VLAN-ID> |     | tag |     |     |
| no vlan    | trunk native | <VLAN-ID> |     | tag |     |     |
Description
EnablestaggingonanativeVLAN.OnlyincomingpacketsthataretaggedwiththematchingVLANIDare
accepted.IncomingpacketsthatareuntaggedaredroppedexceptforBPDUs.Egresspacketsare
tagged.
ThenoformofthiscommandremovestaggingonanativeVLAN.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<VLAN-ID>
SpecifiesthenumberofaVLAN.Range:1to4094.
Examples
EnablingtaggingonnativeVLAN20ontrunkinterface1/1/2:
| switch(config)#    |     | interface |            | 1/1/2 |        |        |
| ------------------ | --- | --------- | ---------- | ----- | ------ | ------ |
| switch(config-if)# |     |           | no routing |       |        |        |
| switch(config-if)# |     |           | vlan       | trunk | native | 20     |
| switch(config-if)# |     |           | vlan       | trunk | native | 20 tag |
RemovingtaggingonnativeVLAN20assignedtotrunkinterface1/1/2:
| switch(config)#    |     | interface |         | 1/1/2 |        |        |
| ------------------ | --- | --------- | ------- | ----- | ------ | ------ |
| switch(config-if)# |     |           | no vlan | trunk | native | 20 tag |
EnablingtaggingonnativeVLAN20assignedtoLAGtrunkinterface2:
| switch(config)#        |         | interface |            | lag   | 2      |        |
| ---------------------- | ------- | --------- | ---------- | ----- | ------ | ------ |
| switch(config-if)#     |         |           | no routing |       |        |        |
| switch(config-lag-if)# |         |           | vlan       | trunk | native | 20     |
| switch(config-lag-if)# |         |           | vlan       | trunk | native | 20 tag |
| Command                | History |           |            |       |        |        |
VLANs|62

| Release             |         |         | Modification |
| ------------------- | ------- | ------- | ------------ |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
voice
voice
no voice
Description
ConfiguresaVLANasavoiceVLAN.
ThenoformofthiscommandremovesvoiceconfigurationfromaVLAN.
Examples
ConfiguringVLAN10asavoiceVLAN:
| switch(config)#         | vlan | 10    |     |
| ----------------------- | ---- | ----- | --- |
| switch(config-vlan-10)# |      | voice |     |
RemovingvoicefromVLAN10:
| switch(config-vlan-10)# |         | no voice |              |
| ----------------------- | ------- | -------- | ------------ |
| Command History         |         |          |              |
| Release                 |         |          | Modification |
| 10.07orearlier          |         |          | --           |
| Command Information     |         |          |              |
| Platforms               | Command | context  | Authority    |
config-vlan-<VLAN-ID>
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
63
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

Chapter 5

QinQ

QinQ

The QinQ is a technology that stacks multiple 802.1Q VLAN tags into a single frame, within the provider-
network that is transparent to the users. QinQ is an essential capability for implementing Metro
Ethernet Network (MAN) topologies.

IEEE 802.1Q specification has a VLAN limit of 4096. This creates an issue within a service-provider
network, that receives frames of various VLANs ranges utilized by different users. The VLAN used by the
user in a service-provider network might overlap, and traffic through the infrastructure can be mixed.
Assigning a unique range of VLAN IDs to every user limits the configurations and might easily exceed the
VLAN limit of 4096.

IEEE 802.1ad supplier bridge specification addresses the issue by allowing the use of a unique VLAN
(called a Service VLAN ID, or S-VID) to each user. Customer VLAN IDs (C-VIDs) are preserved and traffic
from different users is carried over to unique service VLAN that segregates each user traffic within the
service-provider network. The segregation is achieved by adding a secondary VLAN tag (Service VLAN tag
or S-tag with an ether-type of 0x88a8) on the existing C-VLAN tag (otherwise known as double-tagging)
once a frame enters the service supplier network. This is also called as stacked VLAN tags or QinQ. In
theory, it increases the VLAN ID space by a factor of 4096 providing for up to 16M VLAN IDs instead of
the 4K supported by 802.1Q compliant bridges. The S-tag is removed when exiting the service-provider
network restoring the original frame. The primary advantage for a service-provider is a reduced number
of VLANs that require to be supported within the provider-network for the same number of users.

The following table contains terminology and its behavior:

Terminology

Behavior

CVLAN

SVLAN

PN port

CN port

Customer VLAN is the regular IEEE 802.1Q VLAN used by the user
within their network.

Service VLAN is the secondary VLAN tag inserted on existing
CVLAN tag, used by a service-provider to switch user traffic across
provider core and edge networks.

Provider-Network port is a trunk port facing provider network,
that transmits and receives service tag frames for multiple users.

Customer-Network port is an access port facing user network, that
carries CVLANs traffic entering the port with QinQ tunnel using
SVLAN.

QinQ feature interactions

MSTP

CN and PN ports will not participate in Multiple Spanning Tree Protocol (MSTP). MSTPs Bridge Protocol
Data Units (BPDUs) are treated as data packets and QinQ tunneled.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

64

VSX
ItismandatorytoconfigureVSX-ISLlinkastrunkmemberofonlySVLANs.VSX-ISLlinkwillactasQinQ
PNportonbothVSXprimaryandsecondary.MCLAGinterfacecanbeconfiguredeitherasaQinQPN
portoraCNport.Existingcommandsvsx-syncundervlancontext,vsx-sync vlansunderinterface
contextandmclag-interfacesunderglobalvsx-synccontextwillsyncwithQinQspecific
configurationsfromVSXprimarytosecondary.
Loop-Protect
n SVLANcannotbeaLoop-Protect(LP)VLAN.
n QinQportscannotbeconfiguredwithLP.
n CNandPNportswillnotparticipateinLP.
n LPpacketsaretreatedasdatapacketsandQinQtunneled.
QinQ types
QinQtypesaresupportedonlyon8325and8400switchseries.
| Selective QinQ |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- |
SelectiveQinQallowstheserviceVLANtagtobeaddedbasedontheincomingcustomerVLANtag,
providingmoreflexibilityinhowtrafficisroutedonthenetwork.WithSelectiveQinQ,specificcustomer
VLANscanbemappedtospecificserviceVLANs.
ThefollowingisthesampleconfigurationforselectiveQinQ:
| switch(config)#                  | vlan      | 100, 200, | 300          |              |     |
| -------------------------------- | --------- | --------- | ------------ | ------------ | --- |
| switch(config-vlan-100,200,300)# |           |           | svlan        |              |     |
| switch(config)#                  | interface | 1/1/1     |              |              |     |
| switch(config-if)#               | vlan      | access    | 300          |              |     |
| switch(config-if)#               | qinq      | vlan-map  | 10-20        | service-vlan | 100 |
| switch(config-if)#               | qinq      | vlan-map  | 30-40        | service-vlan | 200 |
| switch(config-vlan-10)#          |           | interface | 1/1/2        |              |     |
| switch(config-if)#               | vlan      | trunk     | native 1     |              |     |
| switch(config-if)#               | vlan      | trunk     | allowed 100, | 200, 300     |     |
| Transparent                      | QinQ      |           |              |              |     |
TransparentQinQenablestransparenttransmissionforalistofVLANsonaport.WhenbasicQinQis
enabledonaport,allpacketspassingthroughitaredouble-taggedwithaserviceVLANtag.However,
byconfiguringtransparentVLANsontheQinQport,youcaninstructtheportnottoaddanoutertagto
packetscarryingspecificinnerVLANtags.Thisallowsthesepacketstobetransmittedontheservice
providernetworkwithasingletag.
ThefollowingisthesampleconfigurationfortransparentQinQ:
| switch(config)#         | vlan      | 10     |             |        |     |
| ----------------------- | --------- | ------ | ----------- | ------ | --- |
| switch(config-vlan-10)# |           | svlan  |             |        |     |
| switch(config)#         | vlan      | 30, 40 |             |        |     |
| switch(config)#         | interface | 1/1/1  |             |        |     |
| switch(config-if)#      | vlan      | trunk  | native 10   |        |     |
| switch(config-if)#      | vlan      | trunk  | allowed 10, | 30, 40 |     |
QinQ|65

| switch(config-if)#      |     | qinq | port-type  |         | customer-network |        |     |     |
| ----------------------- | --- | ---- | ---------- | ------- | ---------------- | ------ | --- | --- |
| switch(config-vlan-10)# |     |      | interface  |         | 1/1/2            |        |     |     |
| switch(config-if)#      |     | vlan | trunk      | native  | 1                |        |     |     |
| switch(config-if)#      |     | vlan | trunk      | allowed | 10,              | 30, 40 |     |     |
| Configuring             | and |      | displaying |         | QinQ             |        |     |     |
ThefollowingisthesampleconfigurationforenablingQinQ:
| switch(config)#         |     | vlan      | 10        |         |       |     |     |     |
| ----------------------- | --- | --------- | --------- | ------- | ----- | --- | --- | --- |
| switch(config-vlan-10)# |     |           | svlan     |         |       |     |     |     |
| switch(config-vlan-10)# |     |           | interface |         | 1/1/1 |     |     |     |
| switch(config-if)#      |     | vlan      | access    |         | 10    |     |     |     |
| switch(config-if)#      |     | interface |           | 1/1/2   |       |     |     |     |
| switch(config-if)#      |     | vlan      | trunk     | allowed | 10    |     |     |     |
ShowingtheconfiguredQinQinformation:
| switch#            | show qinq  |             |        |     |     |     |     |     |
| ------------------ | ---------- | ----------- | ------ | --- | --- | --- | --- | --- |
| QinQ Configuration |            | Information |        |     |     |     |     |     |
| Encapsulation      | Ethertype: |             | 0x88A8 |     |     |     |     |     |
| SVLAN List:        | 10         |             |        |     |     |     |     |     |
------------------------------------------------------
| Port | Type |     |     |     | VLAN | Membership |     |     |
| ---- | ---- | --- | --- | --- | ---- | ---------- | --- | --- |
------------------------------------------------------
| 1/1/1 | customer-network |     |     | (access) | 10  |     |     |     |
| ----- | ---------------- | --- | --- | -------- | --- | --- | --- | --- |
| 1/1/2 | provider-network |     |     | (trunk)  | 10  |     |     |     |
ShowingdetailinformationofallQinQports.
| switch#    | show qinq | detail      |     |      |                    |            |                 |       |
| ---------- | --------- | ----------- | --- | ---- | ------------------ | ---------- | --------------- | ----- |
| Interface: | 1/1/1     |             |     |      |                    |            |                 |       |
|            | QinQ      | port-type   |     |      | : customer-network |            |                 |       |
|            | QinQ      | transparent |     |      | vlan : 20,30,40-50 |            |                 |       |
|            | QinQ      | Service     |     | vlan | : 100              |            |                 |       |
| Interface: | 1/1/2     |             |     |      |                    |            |                 |       |
|            | QinQ      | port-type   |     |      | : customer-network |            |                 |       |
|            | QinQ      | transparent |     |      | vlan : None        |            |                 |       |
|            | QinQ      | Service     |     | vlan | : 100              |            |                 |       |
|            |           |             |     |      | : 200              | (selective | customer vlans: | 1000- |
2000,3001,3003)
|     |     |     |     |     | : 300 | (selective | customer vlans: | 2001-3000) |
| --- | --- | --- | --- | --- | ----- | ---------- | --------------- | ---------- |
66
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |

Interface: 1/1/3
| QinQ port-type   | : customer-network |        |
| ---------------- | ------------------ | ------ |
| QinQ transparent | vlan               | : None |
| QinQ Service     | vlan               | : 100  |
Interface: 1/1/3
| QinQ port-type   |                    | : provider-network |
| ---------------- | ------------------ | ------------------ |
| QinQ transparent | vlan : 20,30,40-50 |                    |
| QinQ Service     | vlan               | : 100,200,300      |
Interface: 1/1/4
| QinQ port-type   |      | : provider-network |
| ---------------- | ---- | ------------------ |
| QinQ transparent | vlan | : None             |
| QinQ Service     | vlan | : 100,200,300      |
QinQ limitations
ThefollowingfeaturesarenotsupportedforQinQ:
n Servicetagethertypeexcept0x88A8.
n ProviderBridgeMultipleSpanningTreeProtocol(PB-MSTP).
MACseconCNandPNports.
n
n SelectiveortransparentQinQ.
n Layer2ProtocolTunneling(L2PT).
ThefollowingfeaturesareincompatiblewithQinQandcannotbeenabledtogether:
ThesefeaturesareCLIrestrictedagainstQinQ.However,themutualexclusionforsecurityfeaturessuchasMAC-
auth,MACsec,Dot1x,andLMAisachievedthroughthePSPO.PSPOwillblocktrafficontheoffendingports,until
theconfigurationiscorrected.
n RPVST
n MVRP
n ERPS
n SmartLink
n VLANTranslation
PVLAN
n
n VxLAN
n L3Features
n SecurityandSecurityApplications
n Multicast
n IGMPSnooping
n IPenablementonSVLAN
QinQ|67

QinQtunnelingrequiresadditional4bytesinpacketpayloadtoaddS-tagandproviderbridgeEtherTypeon
provider-networkports.Therefore,itisrecommendedtoconfigureinterfaceMTUtoaccommodatethesameon
provider-networkports.
QinQ commands
| debug vlan      | qinq     |     |     |     |     |
| --------------- | -------- | --- | --- | --- | --- |
| debug vlan qinq | severity |     |     |     |     |
Description
EnablestheVLANdebuglogstotracetheQinQchangesandfilteringwithminimumlogseverity.
Examples
EnablingthedebuglogsforQinQ
| switch#  | debug vlan | qinq |          |                 |      |
| -------- | ---------- | ---- | -------- | --------------- | ---- |
| severity | Minimum    | log  | severity | to filter debug | logs |
<cr>
| switch#             | debug vlan | qinq severity |                                        |     |     |
| ------------------- | ---------- | ------------- | -------------------------------------- | --- | --- |
| Command History     |            |               |                                        |     |     |
| Release             |            |               | Modification                           |     |     |
| 10.11               |            |               | Commandintroducedonthe8400Seriesswitch |     |     |
| Command Information |            |               |                                        |     |     |
| Platforms           | Command    | context       | Authority                              |     |     |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| diag-dump        | l2vlan | basic |     |     |     |
| ---------------- | ------ | ----- | --- | --- | --- |
| diag-dump l2vlan | basic  |       |     |     |     |
Description
CollectsthedebuginformationinthecaseofanyissueintheQinQdaemon.DiagnosticforQinQispart
ofVLANdaemon.
Examples
ConfiguringdiagnosticdumpforQinQ
| switch#         | diag-dump | l2vlan | basic |     |     |
| --------------- | --------- | ------ | ----- | --- | --- |
| Command History |           |        |       |     |     |
68
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| Release             |         |         |     | Modification                           |
| ------------------- | ------- | ------- | --- | -------------------------------------- |
| 10.11               |         |         |     | Commandintroducedonthe8400Seriesswitch |
| Command Information |         |         |     |                                        |
| Platforms           | Command | context |     | Authority                              |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
qinq port-type
| qinq port-type | customer-network |     |     |     |
| -------------- | ---------------- | --- | --- | --- |
Description
Configuresalayer2portasacustomernetworkport.Toconfigureaportasacustomernetworkport,
theportshouldbeamemberofatleastoneserviceVLANandnativeVLANshouldalsobeaservice
VLAN.
ThenoformofthiscommandsetsQinQporttypetothedefaultvalue(auto).
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
customer-network
SetsQinQporttypeascustomer-networkport.
Examples
SettingQinQporttypeasthecustomer-networkport:
| switch(config)#    |     | interface | 1/1/1     |                  |
| ------------------ | --- | --------- | --------- | ---------------- |
| switch(config-if)# |     | qinq      | port-type | customer-network |
RemovingQinQporttype:
| switch(config)#      |         | interface | 1/1/1     |                                             |
| -------------------- | ------- | --------- | --------- | ------------------------------------------- |
| switch(config-if)#   |         | no qinq   | port-type | customer-network                            |
| Command History      |         |           |           |                                             |
| Release              |         |           |           | Modification                                |
| 10.12                |         |           |           | Commandintroducedforthe8325and8400switches. |
| Command Informmation |         |           |           |                                             |
| Platforms            | Command | context   |           | Authority                                   |
config Administratorsorlocalusergroupmemberswithexecutionrights
8400
|     | config-if |     |     | forthiscommand. |
| --- | --------- | --- | --- | --------------- |
QinQ|69

qinq vlan-map
| qinq vlan-map | <vid-list> |     | svlan <vid> |     |     |
| ------------- | ---------- | --- | ----------- | --- | --- |
Description
ConfiguresselectiveQinQforcustomernetworkports,basedonalistofcustomerVLANs(vlan-map)for
aspecifiedserviceVLAN.
ThenoformofthiscommandremovesselectivecustomerVLANlistforthespecifiedserviceVLAN.
Thiscommandisapplicableonlyforaccessport.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<vid-list> SpecifiesthelistofselectivecustomerVLANs.Range:1to4094.
<vid>
SpecifiestheserviceVLAN.Range:2to4094.
Examples
ConfiguringselectiveQinQforinterface1/1/1,withcustomerVLANs10-30andserviceVLAN100:
| switch(config)#    |     | interface | 1/1/1         |             |     |
| ------------------ | --- | --------- | ------------- | ----------- | --- |
| switch(config-if)# |     |           | qinq vlan-map | 10-30 svlan | 100 |
RemovingselectiveQinQforinterface1/1/1,withcustomerVLANs10andserviceVLAN100:
| switch(config)#    |             | interface | 1/1/1            |                                             |     |
| ------------------ | ----------- | --------- | ---------------- | ------------------------------------------- | --- |
| switch(config-if)# |             |           | no qinq vlan-map | 10 svlan                                    | 100 |
| Command            | History     |           |                  |                                             |     |
| Release            |             |           |                  | Modification                                |     |
| 10.12              |             |           |                  | Commandintroducedforthe8325and8400switches. |     |
| Command            | Information |           |                  |                                             |     |
| Platforms          | Command     |           | context          | Authority                                   |     |
8400 config Administratorsorlocalusergroupmemberswithexecutionrights
|           | config-if |     |     | forthiscommand. |     |
| --------- | --------- | --- | --- | --------------- | --- |
| show qinq |           |     |     |                 |     |
show qinq
Description
ShowstheconfigurationdetailsofQinQ.
70
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

Examples
ShowingtheQinQconfiguration
switch#
|               |               | show qinq |             |        |     |     |
| ------------- | ------------- | --------- | ----------- | ------ | --- | --- |
| QinQ          | Configuration |           | Information |        |     |     |
| Encapsulation |               |           | Ethertype:  | 0x88A8 |     |     |
| SVLAN         | List:         | 100-103   |             |        |     |     |
------------------------------------------------------
| Port |     | Type |     |     | VLAN | Membership |
| ---- | --- | ---- | --- | --- | ---- | ---------- |
------------------------------------------------------
| 1/1/1     |     | customer-network |     | (access) | 100                                    |     |
| --------- | --- | ---------------- | --- | -------- | -------------------------------------- | --- |
| 1/1/3     |     | provider-network |     | (trunk)  | 100-103                                |     |
| 1/1/5     |     | customer-network |     | (access) | 101                                    |     |
| 1/1/7     |     | customer-network |     | (access) | 102                                    |     |
| 1/1/9     |     | customer-network |     | (access) | 103                                    |     |
| Command   |     | History          |     |          |                                        |     |
| Release   |     |                  |     |          | Modification                           |     |
| 10.11     |     |                  |     |          | Commandintroducedonthe8400Seriesswitch |     |
| Command   |     | Information      |     |          |                                        |     |
| Platforms |     | Command          |     | context  | Authority                              |     |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show | qinq        | detail |     |     |     |     |
| ---- | ----------- | ------ | --- | --- | --- | --- |
| show | qinq detail |        |     |     |     |     |
Description
ShowsinformationofallQinQportsindetail.
Examples
ShowingthedetailinformationofallQinQports.
| switch#    |      | show qinq   | detail |                    |     |          |
| ---------- | ---- | ----------- | ------ | ------------------ | --- | -------- |
| Interface: |      | 1/1/1       |        |                    |     |          |
|            | QinQ | port-type   |        | : provider-network |     | (trunk)  |
|            | QinQ | ethertype   |        | : 0x88a8           |     |          |
|            | QinQ | transparent | vlans  | : 20,30,40-50      |     |          |
|            | QinQ | Service     | vlan   | : 100              |     |          |
| Interface: |      | 1/1/2       |        |                    |     |          |
|            | QinQ | port-type   |        | : customer-network |     | (access) |
|            | QinQ | ethertype   |        | : 0x88a8           |     |          |
QinQ|71

|            | QinQ        | transparent | vlans   | : None             |                                             |                 |                      |
| ---------- | ----------- | ----------- | ------- | ------------------ | ------------------------------------------- | --------------- | -------------------- |
|            | QinQ        | Service     | vlan    | : 100              |                                             |                 |                      |
|            |             |             |         | : 200              | (selective                                  | customer vlans: | 1000-2000,3001,3003) |
|            |             |             |         | : 300              | (selective                                  | customer vlans: | 2001-3000)           |
| Interface: |             | 1/1/3       |         |                    |                                             |                 |                      |
|            | QinQ        | port-type   |         | : customer-network |                                             | (access)        |                      |
|            | QinQ        | ethertype   |         | : 0x88a8           |                                             |                 |                      |
|            | QinQ        | transparent | vlans   | : None             |                                             |                 |                      |
|            | QinQ        | Service     | vlan    | : 300              |                                             |                 |                      |
| Interface: |             | 1/1/4       |         |                    |                                             |                 |                      |
|            | QinQ        | port-type   |         | : provider-network |                                             | (trunk)         |                      |
|            | QinQ        | ethertype   |         | : 0x88a8           |                                             |                 |                      |
|            | QinQ        | transparent | vlans   | : 20,30,40-50      |                                             |                 |                      |
|            | QinQ        | Service     | vlan    | : 100,200,300      |                                             |                 |                      |
| Interface: |             | 1/1/5       |         |                    |                                             |                 |                      |
|            | QinQ        | port-type   |         | : provider-network |                                             | (trunk)         |                      |
|            | QinQ        | ethertype   |         | : 0x88a8           |                                             |                 |                      |
|            | QinQ        | transparent | vlans   | : None             |                                             |                 |                      |
|            | QinQ        | Service     | vlan    | : 100,200,300      |                                             |                 |                      |
| Release    |             |             |         |                    | Modification                                |                 |                      |
| 10.12      |             |             |         |                    | Commandintroducedforthe8325and8400switches. |                 |                      |
| Command    | Information |             |         |                    |                                             |                 |                      |
| Platforms  |             | Command     | context |                    | Authority                                   |                 |                      |
OperatorsorAdministratorsorlocalusergroupmemberswith
| 8400 |     | Operator(>)orManager |     |     |                                                       |     |     |
| ---- | --- | -------------------- | --- | --- | ----------------------------------------------------- | --- | --- |
|      |     | (#)                  |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
commandfromtheoperatorcontext(>)only.
| show | qinq           | interface |            |     |     |     |     |
| ---- | -------------- | --------- | ---------- | --- | --- | --- | --- |
| show | qinq interface |           | <IF-NAME>> |     |     |     |     |
Description
ShowsinformationforthespecifiedQinQinterface.
Examples
Showinginformationfortheinterface1/1/1:
| switch#    |      | show qinq   | interface | 1/1/1              |     |         |     |
| ---------- | ---- | ----------- | --------- | ------------------ | --- | ------- | --- |
| Interface: |      | 1/1/1       |           |                    |     |         |     |
|            | QinQ | port-type   |           | : provider-network |     | (trunk) |     |
|            | QinQ | ethertype   |           | : 0x88a8           |     |         |     |
|            | QinQ | transparent | vlans     | : 20,30,40-50      |     |         |     |
|            | QinQ | Service     | vlan      | : 100              |     |         |     |
Showinginformationfortheinterface1/1/3:
72
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- |

| switch#    |             | show qinq    | interface | 1/1/3                                       |                 |                      |
| ---------- | ----------- | ------------ | --------- | ------------------------------------------- | --------------- | -------------------- |
| Interface: |             | 1/1/3        |           |                                             |                 |                      |
|            | QinQ        | port-type    |           | : customer-network                          | (access)        |                      |
|            | QinQ        | ethertype    |           | : 0x88a8                                    |                 |                      |
|            | QinQ        | transparent  | vlans     | : None                                      |                 |                      |
|            | QinQ        | Service vlan |           | : 100                                       |                 |                      |
|            |             |              |           | : 200 (selective                            | customer vlans: | 1000-2000,3001,3003) |
|            |             |              |           | : 300 (selective                            | customer vlans: | 2001-3000)           |
| Command    | History     |              |           |                                             |                 |                      |
| Release    |             |              |           | Modification                                |                 |                      |
| 10.12      |             |              |           | Commandintroducedforthe8325and8400switches. |                 |                      |
| Command    | Information |              |           |                                             |                 |                      |
| Platforms  |             | Command      | context   | Authority                                   |                 |                      |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | running-config |      | qinq |     |     |     |
| ---- | -------------- | ---- | ---- | --- | --- | --- |
| show | running-config | qinq |      |     |     |     |
Description
ShowsalltheQinQconfigurationsintheswitch.
Examples
ShowingtheQinQrunningconfiguration
| switch# |     | show running-config |     | qinq |     |     |
| ------- | --- | ------------------- | --- | ---- | --- | --- |
| Current |     | configuration:      |     |      |     |     |
...
vlan 300
svlan
```
| Command | History     |     |     |                                        |     |     |
| ------- | ----------- | --- | --- | -------------------------------------- | --- | --- |
| Release |             |     |     | Modification                           |     |     |
| 10.11   |             |     |     | Commandintroducedonthe8400Seriesswitch |     |     |
| Command | Information |     |     |                                        |     |     |
QinQ|73

| Platforms | Command | context |     | Authority                                            |     |
| --------- | ------- | ------- | --- | ---------------------------------------------------- | --- |
| 8400      |         |         |     | OperatorsorAdministratorsorlocalusergroupmemberswith |     |
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show tech      | qinq |     |     |     |     |
| -------------- | ---- | --- | --- | --- | --- |
| show tech qinq |      |     |     |     |     |
Description
ShowsthetechsupportforQinQfeature.
Examples
ShowingthetechsupportforQinQfeature
| switch# | show tech | qinq |     |     |     |
| ------- | --------- | ---- | --- | --- | --- |
====================================================
| Show Tech | executed | on Thu | Mar | 17 03:07:03 | 2022 |
| --------- | -------- | ------ | --- | ----------- | ---- |
====================================================
====================================================
| [Begin] | Feature qinq |     |     |     |     |
| ------- | ------------ | --- | --- | --- | --- |
====================================================
*********************************
| Command | : show running-config |     |     | qinq |     |
| ------- | --------------------- | --- | --- | ---- | --- |
*********************************
| vlan 300 |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- |
svlan
*********************************
| Command | : show qinq |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- |
*********************************
| switch#            | show qinq  |             |        |     |     |
| ------------------ | ---------- | ----------- | ------ | --- | --- |
| QinQ Configuration |            | Information |        |     |     |
| Encapsulation      | Ethertype: |             | 0x88A8 |     |     |
| SVLAN List:        | 100-103    |             |        |     |     |
---------------------------------------------------
| Port | Type |     |     |     | VLAN Membership |
| ---- | ---- | --- | --- | --- | --------------- |
---------------------------------------------------
| 1/1/1 | customer-network |     | (access) |     | 100     |
| ----- | ---------------- | --- | -------- | --- | ------- |
| 1/1/3 | provider-network |     | (trunk)  |     | 100-103 |
| 1/1/5 | customer-network |     | (access) |     | 101     |
| 1/1/7 | customer-network |     | (access) |     | 102     |
| 1/1/9 | customer-network |     | (access) |     | 103     |
====================================================
| [End] Feature | qinq |     |     |     |     |
| ------------- | ---- | --- | --- | --- | --- |
====================================================
====================================================
| Show Tech | commands | executed | successfully |     |     |
| --------- | -------- | -------- | ------------ | --- | --- |
| Command   | History  |          |              |     |     |
74
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| Release             |         |         | Modification                           |
| ------------------- | ------- | ------- | -------------------------------------- |
| 10.11               |         |         | Commandintroducedonthe8400Seriesswitch |
| Command Information |         |         |                                        |
| Platforms           | Command | context | Authority                              |
8400 Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
svlan
svlan
no svlan
Description
ConfiguresaVLANasaserviceVLAN.Aportwillimplicitlybecomecustomer-networkport,whenitisan
accessmember(untagged)ofSVLAN.Aportwillimplicitlybecomeprovider-networkport,whenitisa
trunkmember(tagged)ofSVLAN.
ThenoformofthiscommandremovestheserviceVLANconfiguration.
AQinQCNorPNport,whichwasamemberoftheSVLAN,willbecomenormalVLANportafterremovingservice
VLANconfigurationfromVLAN.
Usage
n VLAN1cannotbeconfiguredasanSVLAN.
n AnL2portcanbeamemberofeitherserviceVLANsornormalVLANsbutcannotbeusedonboth
theVLANs.
n AnL2portwithvlan trunk allowed allwillnotincludeserviceVLANs.
n NativeVLANconfigurationwillbenon-operationalonPNport.
Examples
ConfiguringVLAN300andenablingserviceVLANmode
| switch(config)#          | vlan | 300   |     |
| ------------------------ | ---- | ----- | --- |
| switch(config-vlan-300)# |      | svlan |     |
RemovingtheserviceVLANmodeconfigurationfromVLAN 300
| switch(config)#          | vlan | 100      |     |
| ------------------------ | ---- | -------- | --- |
| switch(config-vlan-100)# |      | no svlan |     |
| Command History          |      |          |     |
QinQ|75

| Release             |         |         | Modification                           |
| ------------------- | ------- | ------- | -------------------------------------- |
| 10.11               |         |         | Commandintroducedonthe8400Seriesswitch |
| Command Information |         |         |                                        |
| Platforms           | Command | context | Authority                              |
8400 config-vlan-<VLAN-ID> Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
76
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

Chapter 6

Loop protection

Loop protection

In cases where spanning tree protocols cannot be used to prevent loops at the edge of the network,
loop protection may provide a suitable alternative. Loop protection can find loops in untagged layer 2
links, as well as on tagged VLANs, and VXLAN networks.

The cases where loop protection might be chosen ahead of spanning tree to detect and prevent loops
are:

n On ports with client authentication: When spanning tree is enabled on a switch that uses 802.1X, web
authentication, or MAC authentication, loops may go undetected. For example, spanning tree packets
that are looped back to an edge port will not be processed because they have a different
broadcast/multicast MAC address from the client-authenticated MAC address. To ensure that client-
authenticated edge ports get blocked when loops occur, you should enable loop protection on those
ports.

n On ports connected to unmanaged devices: Spanning tree cannot detect the formation of loops

where there is an unmanaged device on the network that does not process spanning tree packets
and simply drops them. Loop protection has no such limitation, and can be used to prevent loops on
unmanaged switches.

Loop protection finds loops by sending loop protection packets on each port, LAG, VLAN, or VXLAN on
which loop protection is enabled. If a loop protection packet is received by the same switch that sent it, it
indicates a loop exists and one of the following actions is taken:

n Discovery of the loop is logged but port states are not changed.

n The sending port is disabled.

n The sending and receiving ports are both disabled.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

77

Loop protection on VXLAN interfaces is supported only on AOS-CX

6200,6300,6400,8360,8325,8400,9300,8100,10000 switch series.

Loop protect action is not supported on VXLAN interfaces and the default action for a VXLAN interface is rx-

disable. Hence, the receiving L2 port is always disabled.

Interaction with other protocols

n When loop protection is enabled before STP, and if there is an L2 loop, then the loop will be detected

and the port will be disabled.

n When STP is enabled before loop protection, and if there is a L2 loop, then the port will be moved to

the blocked state by STP. When a port is blocked, the loop protection packet will not reach the
sending switch, and the loop will not be detected by loop protection. When multiple instances of STP
are configured and different spanning trees are formed for different instances, the PSPO state will be
forwarding. In this case, loop- protection will consider those ports as normal forwarding ports and
will override the STP states.

n STP is mutually exclusive with loop protection. If STP and loop protection are both enabled on the
same VLAN, STP takes precedence. This means that loop protection does not take any action on a
port blocked by STP.

n MVRP and the loop protection interoperate with each other. However, dynamic VLANs cannot be
tagged to a port through user configuration. Therefore, it is not possible to configure a dynamic
VLAN as a loop protection enabled VLAN.

n If MCLAG has marked a port as transmit disable (mclag_pdu_tx_disable is set to true), then loop-
protect will not transmit packets on the port. Similarly, if the loop_detect_source column is set to
mclag then loop protection will not re-enable the port when the re-enable timer expires on that port.

n If the port-access security feature or any other feature blocks the port in PSPO, then loop protection

will not detect the loop.

Configuring loop protection

Procedure

1. Enable loop protection on each layer 2 interface (port, LAG, VLAN, or VXLAN) for which loop

protection is needed, with the commands loop-protect and loop-protect vlan.

2. Define the action to be taken when a loop is detected with the command loop-protect action.
The default action is tx-disable, which means that the port that transmitted the loop detection
packet is disabled. When this action is enabled, environments with N loops must have loop
protection configured on at least N-1 ports to ensure a loop free topology.

Loop protection | 78

Whenthedefaultaction(tx-disable)isused,itisoptionaltoenableloopprotectinall
interfaces.Byenablingloopprotectinasingleinterface,theloopisdetectedandthedefault
actionisexecuted.Sowhenthepacketfromaloopprotect-enabledportisreceivedbackonan
interfacewhereloopprotectisnotenabled,theloopprotectreceiveractioncorrespondingto
thereceivinginterfaceisexecuted.PleasenotethatalltheL2portswillhaveadefaultreceiver
actionoftx-disableevenwhenloopprotectisnotenabled.
LoopprotectactionisnotsupportedonVXLANinterfacesandthedefaultactionforaVXLAN
interfaceisrx-disable.
3. Ifrequired,changetheintervalatwhichloopprotectionmessagesaresentwiththecommand
| loop-protect |     | transmit-interval. |     |     |     |     |
| ------------ | --- | ------------------ | --- | --- | --- | --- |
4. Ifrequired,changethelengthoftimetheswitchwaitsbeforere-enablinganinterfacewiththe
| commandloop-protect |     |     | re-enable-timer. |     |     |     |
| ------------------- | --- | --- | ---------------- | --- | --- | --- |
5. Reviewloopprotectionconfigurationsettingswiththecommandshow loop-protect.
Example
Thisexamplecreatesthefollowingconfiguration:
n Enablesloopprotectionondataport1/1/1andsetstheloopdetectionactiontodisablethetransmit
port.
n EnablesloopprotectiononLAG25andsetstheloopdetectionactiontodisablebothtransmitand
receiveports.
n EnablesloopprotectiononVLANs100-125and200.
n EnablesloopprotectiononVXLAN1
n Setsthere-enabletimerto10seconds.
n Setsthetransmit-intervalto30seconds.
| switch(config)#          |          | interface    |              | 1/1/1           |               |       |
| ------------------------ | -------- | ------------ | ------------ | --------------- | ------------- | ----- |
| switch(config-if)#       |          |              | no routing   |                 |               |       |
| switch(config-if)#       |          |              | loop-protect |                 |               |       |
| switch(config-if)#       |          |              | loop-protect | action          | tx-disable    |       |
| switch(config-if)#       |          |              | exit         |                 |               |       |
| switch(config)#          |          | interface    |              | lag 25          |               |       |
| switch(config-lag-if)#   |          |              | loop-protect |                 |               |       |
| switch(config-if)#       |          |              | loop-protect | action          | tx-rx-disable |       |
| switch(config-if)#       |          |              | loop-protect | vlan            | 100-125,200   |       |
| switch(config-if)#       |          |              | exit         |                 |               |       |
| switch(config)#          |          | loop-protect |              | re-enable-timer |               | 30    |
| switch(config)#          |          | exit         |              |                 |               |       |
| switch(config)#          |          | interface    |              | vxlan 1         |               |       |
| switch(config-vxlan-if)# |          |              | loop         | protect         |               |       |
| switch(config-vxlan-if)# |          |              | loop         | protect         | vlan          | 2-100 |
| switch(config)#          |          | exit         |              |                 |               |       |
| switch#                  | show     | loop-protect |              |                 |               |       |
| Status and               | Counters |              | - Loop       | Protection      | Information   |       |
| Transmit                 | Interval |              |              | : 30            | (sec)         |       |
| Port Re-enable           |          | Timer        |              | : 10            | (sec)         |       |
| Interface                | 1/1/1    |              |              |                 |               |       |
| Loop-protect             |          | enabled      |              | : Yes           |               |       |
| Loop-Protect             |          | enabled      | VLANs        | :               |               |       |
| Action                   | on loop  | detection    |              | : TX            | disable       |       |
| Loop detected            |          | count        |              | : 0             |               |       |
79
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| Loop detected |         |           |       | : No            |
| ------------- | ------- | --------- | ----- | --------------- |
| Interface     | status  |           |       | : up            |
| Interface     | lag     | 25        |       |                 |
| Loop-protect  |         | enabled   |       | : Yes           |
| Loop-Protect  |         | enabled   | VLANs | : 100-125,200   |
| Action        | on loop | detection |       | : TX-RX disable |
| Loop detected |         | count     |       | : 0             |
| Loop detected |         |           |       | : No            |
| Interface     | status  |           |       | : up            |
| Interface     | vxlan1  |           |       |                 |
| Loop-protect  |         | enabled   |       | : Yes           |
| Loop-Protect  |         | enabled   | VLANs | : 2-100         |
| Action        | on loop | detection |       | : RX disable    |
| Loop detected |         | count     |       | : 0             |
| Loop detected |         |           |       | : No            |
| Interface     | status  |           |       | : up            |
| Loop protect  |         | commands  |       |                 |
loop-protect
loop-protect
no loop-protect
Description
Enablesloopprotectiononalayer2interface,VXLANinterface,orLAG.Loopprotectionpacketsare
sent/receivedontheLAGandnottheinterfacewhicharemembersoftheLAG.Loopprotectiononly
worksonlayer2interfaces.Ifalayer2interfaceischangedtoalayer3interface,allloopprotection
configurationsettingsarelostforthatinterface.
IfloopprotectionisenabledonaVXLANinterface,thelocalVTEPwillgenerateloopprotectpacketson
theVXLANtunnel.RemoteVTEPwillhardwareforwardthesameloopprotectpacket.IfalocalVTEP
receivesitsownpacketonanyL2interface,itwillbedetectedasaloopandwillbringdowntheL2
interfaceonwhichtheloopprotectcontrolpacketwasreceived.
Thenoformofthiscommanddisablesloopprotectiononalayer2interface,VXLANinterface,orLAG.
LoopprotectiononVXLANinterfacesissupportedonlyonAOS-CX
6200,6300,6400,8360,8325,8400,9300,8100,10000switchseries.
Examples
Enablingloopprotectiononinterface1/1/1:
| switch# config     |     |              |       |     |
| ------------------ | --- | ------------ | ----- | --- |
| switch(config)#    |     | interface    | 1/1/1 |     |
| switch(config-if)# |     | no routing   |       |     |
| switch(config-if)# |     | loop-protect |       |     |
EnablingloopprotectiononLAG25:
| switch# config |     |     |     |     |
| -------------- | --- | --- | --- | --- |
Loopprotection|80

| switch(config)# | interface | lag 25 |     |
| --------------- | --------- | ------ | --- |
switch(config-if)#
no routing
| switch(config-lag-if)# |     | loop-protect |     |
| ---------------------- | --- | ------------ | --- |
EnablingloopprotectiononVXLANinterface:
| switch#                  | config    |              |                                           |
| ------------------------ | --------- | ------------ | ----------------------------------------- |
| switch(config)#          | interface | vxlan        | 1                                         |
| switch(config-vxlan-if)# |           | loop-protect |                                           |
| Command History          |           |              |                                           |
| Release                  |           |              | Modification                              |
| 10.12                    |           |              | LoopprotectionsupportedonVXLANinterfaces. |
| 10.07orearlier           |           |              | --                                        |
| Command Information      |           |              |                                           |
| Platforms                | Command   | context      | Authority                                 |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-lag-if |     | forthiscommand. |
| --- | ------------- | --- | --------------- |
config-vxlan-if
| loop-protect | action |     |     |
| ------------ | ------ | --- | --- |
loop-protect action {do-not-disable | tx-disable | tx-rx-disable}
no loop-protect action {do-not-disable | tx-disable | tx-rx-disable}
Description
Setstheactiontobetakenwhenaloopprotectionpacketisreceivedonaport.
Ifanactionisconfiguredafteraloopisdetected,thenthenewactiononlytakeseffectafterthere-
enabletimerexpires.Tohavetheactiontakeeffectimmediately,disableandthenre-enableloop
protect.
Thenoformofthiscommandresetstheactiontothedefault(tx-disable).
ThiscommandisnotsupportedonaVXLANinterfaceandthedefaultactionforaVXLANinterfaceisrx-disable.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
do-not-disable Noportsaredisabled.Oneverytransmitinterval,theloopwillbe
detectedandthedetectionwillbereportedviaanSNMPtrapand
aneventlogmessage.
tx-disable Theportthattransmittedtheloopdetectionpacketisdisabled.
Whenthissettingisenabled,environmentswithNloops,must
haveloopprotectionbeconfiguredonatleastN-1portstohavea
loopfreetopology.Default.
81
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
tx-rx-disable Theportsthattransmittedandreceivedtheloopdetectionpacket
aredisabled.
Example
| switch(config-if)# |             |     | loop-protect    |     | action do-not-disable |                |
| ------------------ | ----------- | --- | --------------- | --- | --------------------- | -------------- |
| switch(config-if)# |             |     | no loop-protect |     | action                | do-not-disable |
| Command            | History     |     |                 |     |                       |                |
| Release            |             |     |                 |     | Modification          |                |
| 10.07orearlier     |             |     |                 |     | --                    |                |
| Command            | Information |     |                 |     |                       |                |
| Platforms          | Command     |     | context         |     | Authority             |                |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| loop-protect    |                 | re-enable-timer |     |        |     |     |
| --------------- | --------------- | --------------- | --- | ------ | --- | --- |
| loop-protect    | re-enable-timer |                 |     | <TIME> |     |     |
| no loop-protect |                 | re-enable-timer |     | <TIME> |     |     |
Description
Configuresthetimeintervalafterwhichaninterfacedisabledbyloopprotectionisre-enabled.Theloop
protectiontimerisdisabledbydefault.
Thenoformofthiscommanddisablestheloopprotecttimer.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<TIME> Specifythenumberofsecondsafterwhichadisabledinterfaceis
re-enabled.Range:15to604800.
Example
| switch#         | config      |              |     |                 |              |     |
| --------------- | ----------- | ------------ | --- | --------------- | ------------ | --- |
| switch(config)# |             | loop-protect |     | re-enable-timer |              | 60  |
| Command         | History     |              |     |                 |              |     |
| Release         |             |              |     |                 | Modification |     |
| 10.07orearlier  |             |              |     |                 | --           |     |
| Command         | Information |              |     |                 |              |     |
Loopprotection|82

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| loop-protect    |                   | transmit-interval |        |          |     |
| --------------- | ----------------- | ----------------- | ------ | -------- | --- |
| loop-protect    | transmit-interval |                   | <TIME> |          |     |
| no loop-protect |                   | transmit-interval |        | [<TIME>] |     |
Description
Configuresthetimeintervalbetweensuccessiveloopprotectpacketssentonaninterface.
Thenoformofthiscommandsetsthetimeintervaltothedefaultvalueof5seconds.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<TIME>
Configuresthetransmitintervalinseconds.Range:5to10.
Default:5.
Examples
| switch(config)# |             | loop-protect    | transmit-interval |                   | 10  |
| --------------- | ----------- | --------------- | ----------------- | ----------------- | --- |
| switch(config)# |             | no loop-protect |                   | transmit-interval |     |
| Command         | History     |                 |                   |                   |     |
| Release         |             |                 |                   | Modification      |     |
| 10.07orearlier  |             |                 |                   | --                |     |
| Command         | Information |                 |                   |                   |     |
| Platforms       | Command     | context         |                   | Authority         |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| loop-protect    |      | trap loop-detected |     |     |     |
| --------------- | ---- | ------------------ | --- | --- | --- |
| loop-protect    | trap | loop-detected      |     |     |     |
| no loop-protect |      | trap loop-detected |     |     |     |
Description
EnablessendingSNMPtrapsforloop-protectrelatedevents.
ThenoformofthiscommanddisablessendingSNMPtrapsforloop-protectrelatedevents.
Examples
EnablingthesendingofSNMPtraps:
| switch# | loop-protect | trap | loop-detected |     |     |
| ------- | ------------ | ---- | ------------- | --- | --- |
83
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

DisablingthesendingofSNMPtraps:
| switch#        | no loop-protect |     | trap    | loop-detected |
| -------------- | --------------- | --- | ------- | ------------- |
| Command        | History         |     |         |               |
| Release        |                 |     |         | Modification  |
| 10.07orearlier |                 |     |         | --            |
| Command        | Information     |     |         |               |
| Platforms      | Command         |     | context | Authority     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| loop-protect    |      | vlan        |     |     |
| --------------- | ---- | ----------- | --- | --- |
| loop-protect    | vlan | <VLAN-LIST> |     |     |
| no loop-protect |      | vlan        |     |     |
Description
SpecifiesthetrunkallowedVLANsonwhichloopprotectionpacketsaresent.Bydefault,loopprotection
packetsareonlysentonaccessVLANsandnativeVLANsonaport.Tosendloopprotectionpacketson
trunkallowedVLANs,theVLANsmustbeexplicitlyaddedusingthiscommand.
WhenloopprotectionisenabledonVXLANinterfaces,theswitchwillstarttransmittingloopprotect
packetstoeachVTEPpeerthatarepartofaVNI.
LoopprotectioncanbeconfiguredonamaximumofVLANsacrossallinterfaces.
LoopprotectiononVXLANinterfacescanbeenabledonamaximumof5000(totalofnumberofVTEPs*
numberofloopprotectenabledVLANs).Loopprotectionwillgenerateamaximum5000VXLAN
encapsulatedpacketswithinthedefaultloopprotecttimeintervalof5seconds.
ThenoformofthiscommandremovesloopprotectionfromallVLANsontheinterface.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<VLAN-LIST> SpecifiesthenumberofasingleVLAN,oraseriesofnumbersfor
arangeofVLANs,separatedbycommas(1,2,3,4),dashes(1-4),
orboth(1-4,6).
Example
| switch(config-if)# |     |     | loop-protect | vlan 2-6,10,15-20 |
| ------------------ | --- | --- | ------------ | ----------------- |
EnablingloopprotectiononVXLANinterface:
| switch#         | config |           |       |     |
| --------------- | ------ | --------- | ----- | --- |
| switch(config)# |        | interface | vxlan | 1   |
Loopprotection|84

| switch(config-lag-if)# |         | loop-protect | vlan 10                                   |
| ---------------------- | ------- | ------------ | ----------------------------------------- |
| Command History        |         |              |                                           |
| Release                |         |              | Modification                              |
| 10.12                  |         |              | LoopprotectionsupportedonVXLANinterfaces. |
| 10.07orearlier         |         |              | --                                        |
| Command Information    |         |              |                                           |
| Platforms              | Command | context      | Authority                                 |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-vxlan-if |     | forthiscommand. |
| --- | --------------- | --- | --------------- |
show loop-protect
| show loop-protect | [<INTERFACE-NAME>] |     | [vsx-peer] |
| ----------------- | ------------------ | --- | ---------- |
Description
Thiscommandshowsthefollowingglobalconfigurations.
n Transmitinterval.
Re-enabletimer.
n
n Per-portconfigurations.
n Loop-protectenableordisablestatus.
n Loopdetection.
n Loopdetectedcount.
n Timestampoflatestloopdetection.
n LoopisdetectedonVLAN.
Interfacestatus.
n
n ListofconfiguredVLAN'sforthatport.
n VTEPportinformation
Specifytheinterfacenameondisplayforthefilter.Whenrebootingtheswitchorafterswitchover,The
loop-detectedcountontheloopdetectedportisresettozero.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<INTERFACE-NAME>
Specifiesthenameofalogicalinterfaceontheswitch.Thiscanbe
oneofthefollowing:
n AnEthernetinterfaceassociatedwithaphysicalport.Format:
member/slot/port.
n ALAG(linkaggregationgroup).SpecifytheIDofLAG.For
example:lag100.
n AVXLANinterface.SpecifytheVXLANID.Forexample:vxlan
85
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
1.
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
LoopprotectiononVXLANinterfacesissupportedonAOS-CX6200,6300,6400,8360,8325,8400,9300,8100,
10000switchseries.
Examples
| switch#        | show     | loop-protect |        |            |             |
| -------------- | -------- | ------------ | ------ | ---------- | ----------- |
| Transmit       | Interval | (sec)        |        |            | : 5         |
| Port Re-enable |          | Timer        | (sec)  |            | : Disabled  |
| Loop Detected  |          | Trap         |        |            | : Enabled   |
| Interface      | 1/1/1    |              |        |            |             |
| Loop-protect   |          | enabled      |        | :          | Yes         |
| Loop-Protect   |          | enabled      | VLANs  | :          |             |
| Action         | on loop  | detection    |        | :          | TX disable  |
| Loop detected  |          | count        |        | :          | 0           |
| Loop detected  |          |              |        | :          | No          |
| Interface      | status   |              |        | :          | up          |
| Interface      | 1/1/2    |              |        |            |             |
| Loop-protect   |          | enabled      |        | :          | Yes         |
| Loop-Protect   |          | enabled      | VLANs  | :          |             |
| Action         | on loop  | detection    |        | :          | TX disable  |
| Loop detected  |          | count        |        | :          | 0           |
| Loop detected  |          |              |        | :          | No          |
| Interface      | status   |              |        | :          | up          |
| Interface      | vxlan    | 1            |        |            |             |
| Loop-protect   |          | enabled      |        | : Yes      |             |
| Loop-Protect   |          | enabled      | VLANs  | :          |             |
| Action         | on loop  | detection    |        | : RX       | disable     |
| Loop detected  |          | count        |        | : 0        |             |
| Loop detected  |          |              |        | : No       |             |
| Interface      | status   |              |        | : up       |             |
| switch#        | show     | loop-protect |        | 1/1/3      |             |
| Status and     | Counters |              | - Loop | Protection | Information |
| Transmit       | Interval | (sec)        |        | :          | 5           |
| Port Re-enable |          | Timer        | (sec)  | :          | 0           |
| Loop Detected  |          | Trap         |        | :          | Disabled    |
| Interface      | 1        |              |        |            |             |
| Loop-protect   |          | enabled      |        | :          | Yes         |
| Loop-Protect   |          | enabled      | VLANs  | :          |             |
| Action         | on loop  | detection    |        | :          | TX disable  |
| Loop detected  |          | count        |        | :          | 0           |
Loopprotection|86

Loop detected
Interface status

: No
: up

switch# show loop-protect
Status and Counters - Loop Protection Information

Transmit Interval
Port Re-enable Timer
Loop Detected Trap

Interface 1/5/48

Loop-protect enabled
Action on loop detection
Loop detected count
Loop detected
Detected on VLAN
Detected at
Interface status
Tx_port

: 5 (sec)
: Disabled
: Disabled

: No
: TX disable
: 1
: Yes

: 100
: 2023-03-20T00:01:17

: down
: VTEP_100.1.1.2

Interface vxlan1

Loop-protect enabled
Loop-Protect enabled VLANs
Action on loop detection
Loop detected count
Loop detected
Interface status

: Yes
: 100
: RX disable
: 0
: No
: up

Command History

Release

10.12

Modification

Loop protection supported on VXLAN interfaces.

10.07 or earlier

--

Command Information

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

Operators or Administrators or local user group members with
execution rights for this command. Operators can execute this
command from the operator context (>) only.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

87

Chapter 7

MVRP

MVRP

MVRP provides a mechanism to dynamically share VLAN configuration information across layer 2
switches on a network. MVRP eliminates the need to manually configure VLANs on each switch, enabling
the network to dynamically maintain VLANs based on the current network configuration. MVRP
propagates local VLAN information to other devices, receives VLAN information from other devices, and
dynamically updates local VLAN information. When the network topology changes, MVRP propagates
and learns VLAN information again according to the new topology.

MVRP is defined in the IEEE 802.1ak standard. It perform the same functions as Generic Attribute
Registration Protocol (GARP), while overcoming GARP limitations, such as bandwidth usage and
convergence time in networks with a large numbers of VLANs.

MVRP makes use of the Multiple Registration Protocol (MRP). MRP provides the mechanism for switches
on the same layer 2 network to transmit attribute values on a per MSTI (Multiple Spanning Tree
Instance) basis. (An MSTI is a group or set of VLANs, all of which are part of the same spanning tree.)

Each MRP-enabled interface is called an MRP participant, and each MVRP-enabled interface is called an
MVRP participant. When the VLAN configuration on an MVRP participant changes, it sends a Protocol
Data Unit (PDU) to notify other MVRP participants to register and deregister the changed VLAN. MRP
rapidly propagates the configuration information of an MRP participant throughout the layer 2 network.

MRP registers and deregisters VLAN attributes as follows:

n When an interface receives a declaration for a VLAN, the interface registers the VLAN and joins the

VLAN.

n When an interface receives a withdrawal for a VLAN, the interface deregisters the VLAN and leaves

the VLAN.

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

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

88

n MVRP and PVST cannot be enabled at the same time.

n For security purposes, MVRP is disabled by default. MVRP packets are blocked on MVRP disabled

ports, but can be enabled on ports that are security enabled.

n MVRP supports 1024 VLANs and 512 logical ports.

n If MVRP is enabled globally, MVRP is automatically enabled on LAG interfaces and cannot be

disabled.

MRP messages
MRP messages include the following types:

n Declaration: Includes Join and New messages.

n Withdrawal: Includes Leave and LeaveAll messages.

Join message

An MRP participant sends a Join message to request the peer participant to register attributes in the Join
message.

When receiving a Join message from the peer participant, an MRP participant performs the following
tasks:

n Registers the attributes in the Join message.

n Propagates the Join message to all other participants on the device.

After receiving the Join message, other participants send the Join message to their respective peer
participants.

Join messages sent from a local participant to its peer participant include the following types:

n JoinEmpty: Declares an unregistered attribute. For example, when an MRP participant joins an

unregistered static VLAN, it sends a JoinEmpty message. VLANs created manually and locally are
called static VLANs. VLANs learned through MRP are called dynamic VLANs.

n JoinIn: Declares a registered attribute. A JoinIn message is used in one of the following situations:

o An MRP participant joins an existing static VLAN and sends a JoinIn message after registering the

VLAN.

o The MRP participant receives a Join message propagated by another participant on the device and

sends a JoinIn message after registering the VLAN.

New message

Similar to a Join message, a New message enables MRP participants to register attributes.

When the MSTP topology changes, an MRP participant sends a New message to the peer participant to
declare the topology change.

Upon receiving a New message from the peer participant, an MRP participant performs the following
tasks:

n Registers the attributes in the message.

n Propagates the New message to all other participants on the device.

After receiving the New message, other participants send the New message to their respective peer
participants.

MVRP | 89

Leave message

An MRP participant sends a Leave message to the peer participant when it wants the peer participant to
deregister attributes that it has deregistered.

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

Each MRP participant starts its LeaveAll timer when starting up. When the timer expires, the MRP
participant sends LeaveAll messages to the peer participant.

Upon sending or receiving a LeaveAll message, the local participant starts the Leave timer. The local
participant determines whether to send a Join message depending on its the attribute status. A
participant can re-register the attributes in the received Join message before the Leave timer expires.

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

4. Review your MVRP configuration settings with the commands show mvrp config, show mvrp

state, and show mvrp statistics.

Example

This example creates the following configuration:

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

90

n EnablesMVRPonallinterfaces.
n Setsinterface1/1/1toignoreVLAN100.
| switch(config)#    |          |           | mvrp         |                   |       |           |                   |
| ------------------ | -------- | --------- | ------------ | ----------------- | ----- | --------- | ----------------- |
| switch(config)#    |          |           | interface    | 1/1/1             |       |           |                   |
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
Procedure
1. OnswitchA,enableMVRPglobally,defineVLANsoninterface1/1/1and1/1/2,andenableMVRP
oneachinterface.
|     | switch#         |     | config |      |     |     |     |
| --- | --------------- | --- | ------ | ---- | --- | --- | --- |
|     | switch(config)# |     |        | mvrp |     |     |     |
MVRP|91

| switch(config)#    | interface   | 1/1/1          |     |     |
| ------------------ | ----------- | -------------- | --- | --- |
| switch(config-if)# | no shutdown |                |     |     |
| switch(config-if)# | no routing  |                |     |     |
| switch(config-if)# | vlan        | trunk native 1 |     |     |
| switch(config-if)# | mvrp        |                |     |     |
| switch(config-if)# | exit        |                |     |     |
| switch(config)#    | interface   | 1/1/2          |     |     |
| switch(config-if)# | no shutdown |                |     |     |
switch(config-if)#
no routing
| switch(config-if)# | vlan | trunk native 1 |     |     |
| ------------------ | ---- | -------------- | --- | --- |
| switch(config-if)# | mvrp |                |     |     |
2. OnswitchB,enableMVRPglobally,defineVLANs10and20,assignatrunknativeVLANto
interface1/1/3,andenableMVRPonthisinterface.
switch# config
| switch(config)# | mvrp |     |     |     |
| --------------- | ---- | --- | --- | --- |
switch(config)#
vlan 10
| switch(config)#    | vlan 20     |                |     |     |
| ------------------ | ----------- | -------------- | --- | --- |
| switch(config)#    | interface   | 1/1/3          |     |     |
| switch(config-if)# | no shutdown |                |     |     |
| switch(config-if)# | no routing  |                |     |     |
| switch(config-if)# | vlan        | trunk native 1 |     |     |
| switch(config-if)# | mvrp        |                |     |     |
3. OnswitchC,enableMVRPglobally,defineVLAN20,assignatrunknativeVLANtointerface1/1/3,
andenableMVRPonthisinterface.
switch# config
| switch(config)#    | mvrp        |                |     |     |
| ------------------ | ----------- | -------------- | --- | --- |
| switch(config)#    | vlan 20     |                |     |     |
| switch(config)#    | interface   | 1/1/3          |     |     |
| switch(config-if)# | no shutdown |                |     |     |
| switch(config-if)# | no routing  |                |     |     |
| switch(config-if)# | vlan        | trunk native 1 |     |     |
| switch(config-if)# | mvrp        |                |     |     |
4. VerifyVLANconfigurationbyrunningthecommandshow vlan.ItshouldshowthatVLAN10and
20arelearnedbyswitchA,andVLAN10shouldbelearnedbyswitchC.Forexample:
OnswitchA:
| switch# show | vlan |     |     |     |
| ------------ | ---- | --- | --- | --- |
----------------------------------------------------------------------------
-
| VLAN Name |     | Status Reason | Type | Interfaces |
| --------- | --- | ------------- | ---- | ---------- |
----------------------------------------------------------------------------
-
| 1 DEFAULT_VLAN_1 |     | up ok | default | 1/1/1- |
| ---------------- | --- | ----- | ------- | ------ |
1/1/2
| 10 VLAN10 |     | up ok | dynamic | 1/1/2  |
| --------- | --- | ----- | ------- | ------ |
| 20 VLAN20 |     | up ok | dynamic | 1/1/1- |
1/1/2
switch#
92
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| switch#         | show         | mvrp      | config       |           |           |         |                   |     |
| --------------- | ------------ | --------- | ------------ | --------- | --------- | ------- | ----------------- | --- |
| Configuration   |              | and       | Status       | - MVRP    |           |         |                   |     |
| Global          | MVRP         | status    | : Enabled    |           |           |         |                   |     |
| Port            | Status       |           | Registration |           | Join      | Leave   | LeaveAll Periodic |     |
|                 |              |           | Type         |           | Timer     | Timer   | Timer Timer       |     |
| -------         | --------     |           | --------     |           | -----     | ------- | ------- --------  |     |
| 1/1/1           | Enabled      |           | normal       |           |           | 20 300  | 1000              | 100 |
| 1/1/2           | Enabled      |           | normal       |           |           | 20 300  | 1000              | 100 |
| switch#         | show         | mvrp      | state        |           |           |         |                   |     |
| Configuration   |              | and       | Status       | - MVRP    | state     |         |                   |     |
| Port            | VLAN         | Registrar |              | Applicant | Forbid    |         |                   |     |
|                 |              | State     |              | State     | Mode      |         |                   |     |
| ----            | ----         | --------- |              | --------- | --------- |         |                   |     |
| 1/1/1           | 1            | IN        |              | QA        | No        |         |                   |     |
| 1/1/1           | 10           | MT        |              | QA        | No        |         |                   |     |
| 1/1/1           | 20           | IN        |              | QA        | No        |         |                   |     |
| 1/1/2           | 1            | IN        |              | QA        | No        |         |                   |     |
| 1/1/2           | 10           | IN        |              | VO        | No        |         |                   |     |
| 1/1/2           | 20           | IN        |              | QA        | No        |         |                   |     |
| switch#         | show         | mvrp      | statistics   |           |           |         |                   |     |
| Status          | and Counters |           | -            | MVRP      |           |         |                   |     |
| MVRP statistics |              | for       | port         | : 1/1/1   |           |         |                   |     |
----------------------------
| Failed          | registration |              |        | : 0                 |              |      |     |     |
| --------------- | ------------ | ------------ | ------ | ------------------- | ------------ | ---- | --- | --- |
| Last PDU        | origin       |              |        | : e0:07:1b:cb:01:ab |              |      |     |     |
| Total PDU       | Transmitted  |              |        | : 313               |              |      |     |     |
| Total PDU       | Received     |              |        | : 377               |              |      |     |     |
| Frames          | Discarded    |              |        | : 0                 |              |      |     |     |
| Message         | type         | Transmitted  |        |                     | Received     |      |     |     |
| --------------  |              | ------------ |        |                     | ------------ |      |     |     |
| New             |              |              |        | 0                   |              | 0    |     |     |
| Empty           |              |              | 179105 |                     |              | 2264 |     |     |
| In              |              |              |        | 0                   |              | 346  |     |     |
| Join Empty      |              |              |        | 366                 |              | 62   |     |     |
| Join In         |              |              |        | 342                 |              | 692  |     |     |
| Leave           |              |              |        | 0                   |              | 0    |     |     |
| Leaveall        |              |              |        | 43                  |              | 32   |     |     |
| Status          | and Counters |              | -      | MVRP                |              |      |     |     |
| MVRP statistics |              | for          | port   | : 1/1/2             |              |      |     |     |
----------------------------
| Failed         | registration |              |        | : 0                 |              |     |     |     |
| -------------- | ------------ | ------------ | ------ | ------------------- | ------------ | --- | --- | --- |
| Last PDU       | origin       |              |        | : e0:07:1b:cb:22:54 |              |     |     |     |
| Total PDU      | Transmitted  |              |        | : 450               |              |     |     |     |
| Total PDU      | Received     |              |        | : 84                |              |     |     |     |
| Frames         | Discarded    |              |        | : 0                 |              |     |     |     |
| Message        | type         | Transmitted  |        |                     | Received     |     |     |     |
| -------------- |              | ------------ |        |                     | ------------ |     |     |     |
| New            |              |              |        | 0                   |              | 0   |     |     |
| Empty          |              |              | 173629 |                     |              | 382 |     |     |
| In             |              |              |        | 328                 |              | 0   |     |     |
| Join Empty     |              |              |        | 83                  |              | 93  |     |     |
| Join In        |              |              |        | 711                 |              | 65  |     |     |
| Leave          |              |              |        | 0                   |              | 0   |     |     |
| Leaveall       |              |              |        | 41                  |              | 33  |     |     |
OnswitchB:
MVRP|93

| switch# | show | vlan |     |     |     |     |     |     |     |
| ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
----------------------------------------------------------------------------
--
| VLAN Name |     |     |     |     | Status | Reason |     | Type |     |
| --------- | --- | --- | --- | --- | ------ | ------ | --- | ---- | --- |
Interfaces
----------------------------------------------------------------------------
--
| 1 DEFAULT_VLAN_1 |     |     |     |     | up  | ok  |     | default | 1/1/3 |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- |
| 10 VLAN10        |     |     |     |     | up  | ok  |     | static  | 1/1/3 |
| 20 VLAN20        |     |     |     |     | up  | ok  |     | static  | 1/1/3 |
SW1-8320#
| SW1-8320#       | show         | mvrp      | config       |           |           |         |          |          |     |
| --------------- | ------------ | --------- | ------------ | --------- | --------- | ------- | -------- | -------- | --- |
| Configuration   |              | and       | Status       | - MVRP    |           |         |          |          |     |
| Global          | MVRP         | status    | : Enabled    |           |           |         |          |          |     |
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
----------------------------------------------------------------------------
--
| VLAN Name |     |     |     |     | Status | Reason |     | Type |     |
| --------- | --- | --- | --- | --- | ------ | ------ | --- | ---- | --- |
Interfaces
----------------------------------------------------------------------------
--
| 1 DEFAULT_VLAN_1 |     |     |     |     | up  | ok  |     | default | 1/1/3 |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- |
| 10 VLAN10        |     |     |     |     | up  | ok  |     | dynamic | 1/1/3 |
| 20 VLAN20        |     |     |     |     | up  | ok  |     | static  | 1/1/3 |
switch#
94
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

|     | switch#       | show     | mvrp      | config       |           |           |         |                   |     |
| --- | ------------- | -------- | --------- | ------------ | --------- | --------- | ------- | ----------------- | --- |
|     | Configuration |          | and       | Status       | - MVRP    |           |         |                   |     |
|     | Global        | MVRP     | status    | : Enabled    |           |           |         |                   |     |
|     | Port          | Status   |           | Registration |           | Join      | Leave   | LeaveAll Periodic |     |
|     |               |          |           | Type         |           | Timer     | Timer   | Timer Timer       |     |
|     | -------       | -------- |           | --------     |           | -----     | ------- | ------- --------  |     |
|     | 1/1/3         | Enabled  |           | normal       |           |           | 20 300  | 1000              | 100 |
|     | switch#       | show     | mvrp      | state        |           |           |         |                   |     |
|     | Configuration |          | and       | Status       | - MVRP    | state     |         |                   |     |
|     | Port          | VLAN     | Registrar |              | Applicant | Forbid    |         |                   |     |
|     |               |          | State     |              | State     | Mode      |         |                   |     |
|     | ----          | ----     | --------- |              | --------- | --------- |         |                   |     |
|     | 1/1/3         | 1        | IN        |              | QA        | No        |         |                   |     |
|     | 1/1/3         | 10       | IN        |              | VO        | No        |         |                   |     |
|     | 1/1/3         | 20       | IN        |              | QA        | No        |         |                   |     |
switch#
|     | switch#         | show         | mvrp | statistics |         |     |     |     |     |
| --- | --------------- | ------------ | ---- | ---------- | ------- | --- | --- | --- | --- |
|     | Status          | and Counters |      | -          | MVRP    |     |     |     |     |
|     | MVRP statistics |              | for  | port       | : 1/1/3 |     |     |     |     |
----------------------------
|      | Failed         | registration |              |     | : 0                 |              |     |     |     |
| ---- | -------------- | ------------ | ------------ | --- | ------------------- | ------------ | --- | --- | --- |
|      | Last PDU       | origin       |              |     | : 48:0f:cf:af:f2:fb |              |     |     |     |
|      | Total PDU      | Transmitted  |              |     | : 203               |              |     |     |     |
|      | Total PDU      | Received     |              |     | : 95                |              |     |     |     |
|      | Frames         | Discarded    |              |     | : 0                 |              |     |     |     |
|      | Message        | type         | Transmitted  |     |                     | Received     |     |     |     |
|      | -------------- |              | ------------ |     |                     | ------------ |     |     |     |
|      | New            |              |              |     | 0                   |              | 0   |     |     |
|      | Empty          |              |              |     | 72915               |              | 586 |     |     |
|      | In             |              |              |     | 183                 |              | 0   |     |     |
|      | Join Empty     |              |              |     | 40                  |              | 101 |     |     |
|      | Join In        |              |              |     | 366                 |              | 176 |     |     |
|      | Leave          |              |              |     | 0                   |              | 0   |     |     |
|      | Leaveall       |              |              |     | 17                  |              | 16  |     |     |
| MVRP | scenario       |              | 2            |     |                     |              |     |     |     |
ThisscenarioillustratestheconfigurationofanMVRPdeploymentwithtwoMSTIs.
TwoMSTIsaredefinedforthisscenario:
MVRP|95

n VLAN10assignedtoMSTI1
n VLAN20assignedtoMSTI2
AllotherVLANsassignedtothedefaultMSTI0
n
Procedure
1. OnswitchA:
| switch# config  |     |               |     |                 |        |     |
| --------------- | --- | ------------- | --- | --------------- | ------ | --- |
| switch(config)# |     | mvrp          |     |                 |        |     |
| switch(config)# |     | vlan 10       |     |                 |        |     |
| switch(config)# |     | spanning-tree |     |                 |        |     |
| switch(config)# |     | spanning-tree |     | priority        | 1      |     |
| switch(config)# |     | spanning-tree |     | config-name     | sp1    |     |
| switch(config)# |     | spanning-tree |     | config-revision |        | 1   |
| switch(config)# |     | spanning-tree |     | instance        | 1 vlan | 10  |
switch(config)#
|                    |     | spanning-tree |          | instance | 2 vlan | 20  |
| ------------------ | --- | ------------- | -------- | -------- | ------ | --- |
| switch(config)#    |     | interface     | 1/1/1    |          |        |     |
| switch(config-if)# |     | no            | shutdown |          |        |     |
| switch(config-if)# |     | no            | routing  |          |        |     |
| switch(config-if)# |     | vlan          | trunk    | native 1 |        |     |
| switch(config-if)# |     | mvrp          |          |          |        |     |
| switch(config-if)# |     | exit          |          |          |        |     |
| switch(config)#    |     | interface     | 1/1/2    |          |        |     |
| switch(config-if)# |     | no            | shutdown |          |        |     |
| switch(config-if)# |     | no            | routing  |          |        |     |
switch(config-if)#
|                    |        | vlan         | trunk    | native 1 |       |                   |
| ------------------ | ------ | ------------ | -------- | -------- | ----- | ----------------- |
| switch(config-if)# |        | mvrp         |          |          |       |                   |
| switch(config-if)# |        | exit         |          |          |       |                   |
| switch(config)#    |        | interface    | 1/1/3    |          |       |                   |
| switch(config-if)# |        | no           | shutdown |          |       |                   |
| switch(config-if)# |        | no           | routing  |          |       |                   |
| switch(config-if)# |        | vlan         | trunk    | native 1 |       |                   |
| switch(config-if)# |        | mvrp         |          |          |       |                   |
| switch(config-if)# |        | exit         |          |          |       |                   |
| switch# show       | mvrp   | config       |          |          |       |                   |
| Configuration      | and    | Status       | -        | MVRP     |       |                   |
| Global MVRP        | status | : Enabled    |          |          |       |                   |
| Port Status        |        | Registration |          | Join     | Leave | LeaveAll Periodic |
96
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

|                  |               | Type     |           | Timer      | Timer   |     | Timer Timer      |     |
| ---------------- | ------------- | -------- | --------- | ---------- | ------- | --- | ---------------- | --- |
| ------- -------- |               | -------- |           | -----      | ------- |     | ------- -------- |     |
| 1/1/1            | Enabled       | normal   |           | 20         |         | 300 | 1000             | 100 |
| 1/1/3            | Enabled       | normal   |           | 20         |         | 300 | 1000             | 100 |
| 1/1/2            | Enabled       | normal   |           | 20         |         | 300 | 1000             | 100 |
| switch# show     | mvrp          | state    |           |            |         |     |                  |     |
| Configuration    | and           | Status   | -         | MVRP state |         |     |                  |     |
| Port VLAN        | Registrar     |          | Applicant | Forbid     |         |     |                  |     |
|                  | State         |          | State     | Mode       |         |     |                  |     |
| ---- ----        | ---------     |          | --------- | ---------  |         |     |                  |     |
| 1/1/1 1          | IN            |          | QA        | No         |         |     |                  |     |
| 1/1/1 20         | MT            |          | QA        | No         |         |     |                  |     |
| 1/1/3 1          | IN            |          | QA        | No         |         |     |                  |     |
| 1/1/3 20         | IN            |          | VO        | No         |         |     |                  |     |
| 1/1/2 1          | MT            |          | QA        | No         |         |     |                  |     |
| 1/1/2 20         | MT            |          | QA        | No         |         |     |                  |     |
| switch# show     | spanning-tree |          |           | mst        |         |     |                  |     |
#### MST0
| Vlans mapped: |     | 1-9,11-19,21-4094         |     |     |     |               |     |     |
| ------------- | --- | ------------------------- | --- | --- | --- | ------------- | --- | --- |
| Bridge        |     | Address:48:0f:cf:af:f1:82 |     |     |     | priority:4096 |     |     |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |     | txHoldCount(i6 |     |     |     |     |     |     |
| ------------------ | --- | -------------- | --- | --- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |      | txHoldCount(i6            |            |       |     |               |          |      |
| ------------------ | ---- | ------------------------- | ---------- | ----- | --- | ------------- | -------- | ---- |
| Root               |      | Address:48:0f:cf:af:14:0a |            |       |     | Priority:4096 |          |      |
|                    |      | Port:1/1/3                |            |       |     | Path          | cost:0   |      |
| Regional           | Root | Address:48:0f:cf:af:14:0a |            |       |     | Priority:4096 |          |      |
|                    |      | Internal                  | cost:20000 |       |     | Rem Hops:19   |          |      |
| Port               |      | Role                      |            | State |     | Cost          | Priority | Type |
-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/1 |     | Designated |     | Forwarding |     | 20000 | 128 | point_to_ |
| ----- | --- | ---------- | --- | ---------- | --- | ----- | --- | --------- |
point
| 1/1/2 |     | Designated |     | Forwarding |     | 20000 | 128 | point_to_ |
| ----- | --- | ---------- | --- | ---------- | --- | ----- | --- | --------- |
point
| 1/1/3 |     | Root |     | Forwarding |     | 20000 | 128 | point_to_ |
| ----- | --- | ---- | --- | ---------- | --- | ----- | --- | --------- |
point
#### MST1
| Vlans mapped: |     | 10                        |     |             |     |                |          |      |
| ------------- | --- | ------------------------- | --- | ----------- | --- | -------------- | -------- | ---- |
| Bridge        |     | Address:48:0f:cf:af:f1:82 |     |             |     | Priority:32768 |          |      |
| Root          |     | Address:48:0f:cf:af:14:0a |     |             |     | Priority:32768 |          |      |
|               |     | Port:1/1/3,               |     | Cost:20000, | Rem | Hops:19        |          |      |
| Port          |     | Role                      |     | State       |     | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/1 |     | Designated |     | Forwarding |     | 20000 | 128 | point_to_point |
| ----- | --- | ---------- | --- | ---------- | --- | ----- | --- | -------------- |
| 1/1/2 |     | Designated |     | Forwarding |     | 20000 | 128 | point_to_point |
| 1/1/3 |     | Root       |     | Forwarding |     | 20000 | 128 | point_to_point |
#### MST2
| Vlans mapped: |     | 20                        |     |             |     |                |          |      |
| ------------- | --- | ------------------------- | --- | ----------- | --- | -------------- | -------- | ---- |
| Bridge        |     | Address:48:0f:cf:af:f1:82 |     |             |     | Priority:32768 |          |      |
| Root          |     | Address:48:0f:cf:af:14:0a |     |             |     | Priority:32768 |          |      |
|               |     | Port:1/1/3,               |     | Cost:20000, | Rem | Hops:19        |          |      |
| Port          |     | Role                      |     | State       |     | Cost           | Priority | Type |
MVRP|97

-------------- -------------- ------------ ------- ---------- ----------
| 1/1/1 |     | Designated |     | Forwarding |     | 20000 128 | point_to_point |
| ----- | --- | ---------- | --- | ---------- | --- | --------- | -------------- |
| 1/1/2 |     | Designated |     | Forwarding |     | 20000 128 | point_to_point |
| 1/1/3 |     | Root       |     | Forwarding |     | 20000 128 | point_to_point |
2. OnswitchB:
| switch# config  |     |               |     |                 |        |     |     |
| --------------- | --- | ------------- | --- | --------------- | ------ | --- | --- |
| switch(config)# |     | mvrp          |     |                 |        |     |     |
| switch(config)# |     | vlan 20       |     |                 |        |     |     |
| switch(config)# |     | spanning-tree |     |                 |        |     |     |
| switch(config)# |     | spanning-tree |     | priority        | 1      |     |     |
| switch(config)# |     | spanning-tree |     | config-name     | sp1    |     |     |
| switch(config)# |     | spanning-tree |     | config-revision |        | 1   |     |
| switch(config)# |     | spanning-tree |     | instance        | 1 vlan | 10  |     |
| switch(config)# |     | spanning-tree |     | instance        | 2 vlan | 20  |     |
switch(config)#
|                    |     | interface | 1/1/18   |          |     |     |     |
| ------------------ | --- | --------- | -------- | -------- | --- | --- | --- |
| switch(config-if)# |     | no        | shutdown |          |     |     |     |
| switch(config-if)# |     | no        | routing  |          |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native 1 |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | allowed  | all |     |     |
| switch(config-if)# |     | mvrp      |          |          |     |     |     |
| switch(config-if)# |     | exit      |          |          |     |     |     |
| switch(config)#    |     | interface | 1/1/20   |          |     |     |     |
| switch(config-if)# |     | no        | shutdown |          |     |     |     |
| switch(config-if)# |     | no        | routing  |          |     |     |     |
switch(config-if)#
|                    |     | vlan      | trunk    | native 1 |     |     |     |
| ------------------ | --- | --------- | -------- | -------- | --- | --- | --- |
| switch(config-if)# |     | vlan      | trunk    | allowed  | all |     |     |
| switch(config-if)# |     | mvrp      |          |          |     |     |     |
| switch(config-if)# |     | exit      |          |          |     |     |     |
| switch(config)#    |     | interface | 1/1/22   |          |     |     |     |
| switch(config-if)# |     | no        | shutdown |          |     |     |     |
| switch(config-if)# |     | no        | routing  |          |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native 1 |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | allowed  | all |     |     |
| switch(config-if)# |     | mvrp      |          |          |     |     |     |
switch(config-if)#
exit
| switch# show     | mvrp          | config       |           |            |         |                   |     |
| ---------------- | ------------- | ------------ | --------- | ---------- | ------- | ----------------- | --- |
| Configuration    | and           | Status       | -         | MVRP       |         |                   |     |
| Global MVRP      | status        | : Enabled    |           |            |         |                   |     |
| Port Status      |               | Registration |           | Join       | Leave   | LeaveAll Periodic |     |
|                  |               | Type         |           | Timer      | Timer   | Timer Timer       |     |
| ------- -------- |               | --------     |           | -----      | ------- | ------- --------  |     |
| 1/1/18           | Enabled       | normal       |           | 20         | 300     | 1000              | 100 |
| 1/1/20           | Enabled       | normal       |           | 20         | 300     | 1000              | 100 |
| 1/1/22           | Enabled       | normal       |           | 20         | 300     | 1000              | 100 |
| switch# show     | mvrp          | state        |           |            |         |                   |     |
| Configuration    | and           | Status       | -         | MVRP state |         |                   |     |
| Port VLAN        | Registrar     |              | Applicant | Forbid     |         |                   |     |
|                  | State         |              | State     | Mode       |         |                   |     |
| ---- ----        | ---------     |              | --------- | ---------  |         |                   |     |
| 1/1/20 1         | MT            |              | AA        | No         |         |                   |     |
| 1/1/20 10        | MT            |              | AA        | No         |         |                   |     |
| 1/1/20 20        | MT            |              | AA        | No         |         |                   |     |
| 1/1/22 1         | IN            |              | AP        | No         |         |                   |     |
| 1/1/22 10        | IN            |              | VO        | No         |         |                   |     |
| 1/1/22 20        | MT            |              | VP        | No         |         |                   |     |
| switch# show     | spanning-tree |              |           | mst        |         |                   |     |
98
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

#### MST0
| Vlans mapped: | 1-9,11-19,21-4094         |     |     |               |     |     |
| ------------- | ------------------------- | --- | --- | ------------- | --- | --- |
| Bridge        | Address:e0:07:1b:cb:22:1c |     |     | priority:4096 |     |     |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 | txHoldCount(in |     | pp6 |     |     |     |
| ------------------ | -------------- | --- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 | Max-Hops:20               |       |     |               |          |      |
| ------------------ | ------------------------- | ----- | --- | ------------- | -------- | ---- |
| Root               | Address:48:0f:cf:af:14:0a |       |     | Priority:4096 |          |      |
|                    | Port:1/1/22               |       |     | Path cost:0   |          |      |
| Regional Root      | Address:48:0f:cf:af:14:0a |       |     | Priority:4096 |          |      |
|                    | Internal cost:20000       |       |     | Rem Hops:19   |          |      |
| Port               | Role                      | State |     | Cost          | Priority | Type |
-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/18 | Alternate | Blocking |     | 20000 | 128 | point_to_ |
| ------ | --------- | -------- | --- | ----- | --- | --------- |
point
| 1/1/20 | Designated | Forwarding |     | 20000 | 128 | point_to_ |
| ------ | ---------- | ---------- | --- | ----- | --- | --------- |
point
| 1/1/22 | Root | Forwarding |     | 20000 | 128 | point_to_ |
| ------ | ---- | ---------- | --- | ----- | --- | --------- |
point
#### MST1
| Vlans mapped: | 10                        |             |     |                |          |      |
| ------------- | ------------------------- | ----------- | --- | -------------- | -------- | ---- |
| Bridge        | Address:e0:07:1b:cb:22:1c |             |     | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |             |     | Priority:32768 |          |      |
|               | Port:1/1/22,              | Cost:20000, |     | Rem Hops:19    |          |      |
| Port          | Role                      | State       |     | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/18 | Alternate  | Blocking   |     | 20000 | 128 | point_to_point |
| ------ | ---------- | ---------- | --- | ----- | --- | -------------- |
| 1/1/20 | Designated | Forwarding |     | 20000 | 128 | point_to_point |
| 1/1/22 | Root       | Forwarding |     | 20000 | 128 | point_to_point |
#### MST2
| Vlans mapped: | 20                        |             |     |                |          |      |
| ------------- | ------------------------- | ----------- | --- | -------------- | -------- | ---- |
| Bridge        | Address:e0:07:1b:cb:22:1c |             |     | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |             |     | Priority:32768 |          |      |
|               | Port:1/1/22,              | Cost:20000, |     | Rem Hops:19    |          |      |
| Port          | Role                      | State       |     | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/18 | Alternate  | Blocking   |     | 20000 | 128 | point_to_point |
| ------ | ---------- | ---------- | --- | ----- | --- | -------------- |
| 1/1/20 | Designated | Forwarding |     | 20000 | 128 | point_to_point |
| 1/1/22 | Root       | Forwarding |     | 20000 | 128 | point_to_point |
3. OnswitchC:
| switch# config  |               |             |     |     |     |     |
| --------------- | ------------- | ----------- | --- | --- | --- | --- |
| switch(config)# | mvrp          |             |     |     |     |     |
| switch(config)# | vlan 1,20     |             |     |     |     |     |
| switch(config)# | spanning-tree |             |     |     |     |     |
| switch(config)# | spanning-tree | priority    |     | 1   |     |     |
| switch(config)# | spanning-tree | config-name |     | sp1 |     |     |
switch(config)#
|                 | spanning-tree | config-revision |     | 1         |     |     |
| --------------- | ------------- | --------------- | --- | --------- | --- | --- |
| switch(config)# | spanning-tree | instance        |     | 1 vlan 10 |     |     |
| switch(config)# | spanning-tree | instance        |     | 2 vlan 20 |     |     |
MVRP|99

| switch(config)# |     | interface | 1/1/25 |     |     |     |     |     |
| --------------- | --- | --------- | ------ | --- | --- | --- | --- | --- |
switch(config-if)#
|                    |     | no        | shutdown |         |     |     |     |     |
| ------------------ | --- | --------- | -------- | ------- | --- | --- | --- | --- |
| switch(config-if)# |     | no        | routing  |         |     |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native  | 1   |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | allowed | all |     |     |     |
| switch(config-if)# |     | mvrp      |          |         |     |     |     |     |
| switch(config-if)# |     | exit      |          |         |     |     |     |     |
| switch(config)#    |     | interface | 1/1/27   |         |     |     |     |     |
| switch(config-if)# |     | no        | shutdown |         |     |     |     |     |
| switch(config-if)# |     | no        | routing  |         |     |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native  | 1   |     |     |     |
switch(config-if)#
|                    |           | vlan         | trunk     | allowed    | all     |          |          |     |
| ------------------ | --------- | ------------ | --------- | ---------- | ------- | -------- | -------- | --- |
| switch(config-if)# |           | mvrp         |           |            |         |          |          |     |
| switch(config-if)# |           | exit         |           |            |         |          |          |     |
| switch# show       | mvrp      | config       |           |            |         |          |          |     |
| Configuration      | and       | Status       | -         | MVRP       |         |          |          |     |
| Global MVRP        | status    | : Enabled    |           |            |         |          |          |     |
| Port Status        |           | Registration |           | Join       | Leave   | LeaveAll | Periodic |     |
|                    |           | Type         |           | Timer      | Timer   | Timer    | Timer    |     |
| ------- --------   |           | --------     |           | -----      | ------- | -------  | -------- |     |
| 1/1/25             | Enabled   | normal       |           | 20         | 300     | 1000     |          | 100 |
| 1/1/27             | Enabled   | normal       |           | 20         | 300     | 1000     |          | 100 |
| switch# show       | mvrp      | state        |           |            |         |          |          |     |
| Configuration      | and       | Status       | -         | MVRP state |         |          |          |     |
| Port VLAN          | Registrar |              | Applicant | Forbid     |         |          |          |     |
|                    | State     |              | State     | Mode       |         |          |          |     |
| ---- ----          | --------- |              | --------- | ---------  |         |          |          |     |
| 1/1/25 1           | IN        |              | QA        | No         |         |          |          |     |
| 1/1/25 10          | IN        |              | VO        | No         |         |          |          |     |
| 1/1/25 20          | IN        |              | VO        | No         |         |          |          |     |
switch#
| show | spanning-tree |     |     | mst |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
#### MST0
| Vlans mapped: |     | 1-9,11-19,21-4094         |     |     |     |               |     |     |
| ------------- | --- | ------------------------- | --- | --- | --- | ------------- | --- | --- |
| Bridge        |     | Address:e0:07:1b:cb:01:7a |     |     |     | priority:4096 |     |     |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |     | txHoldCount(6 |     |     |     |     |     |     |
| ------------------ | --- | ------------- | --- | --- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 |      | Max-Hops:20               |            |       |               |         |          |      |
| ------------------ | ---- | ------------------------- | ---------- | ----- | ------------- | ------- | -------- | ---- |
| Root               |      | Address:48:0f:cf:af:14:0a |            |       | Priority:4096 |         |          |      |
|                    |      | Port:1/1/25               |            |       | Path          | cost:0  |          |      |
| Regional           | Root | Address:48:0f:cf:af:14:0a |            |       | Priority:4096 |         |          |      |
|                    |      | Internal                  | cost:40000 |       | Rem           | Hops:18 |          |      |
| Port               |      | Role                      |            | State | Cost          |         | Priority | Type |
-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/25 |     | Root |     | Forwarding | 20000 |     | 128 | point_to_ |
| ------ | --- | ---- | --- | ---------- | ----- | --- | --- | --------- |
point
| 1/1/27 |     | Alternate |     | Blocking | 20000 |     | 128 | point_to_ |
| ------ | --- | --------- | --- | -------- | ----- | --- | --- | --------- |
point
#### MST1
| Vlans mapped: |     | 10                        |     |             |      |                |          |      |
| ------------- | --- | ------------------------- | --- | ----------- | ---- | -------------- | -------- | ---- |
| Bridge        |     | Address:e0:07:1b:cb:01:7a |     |             |      | Priority:32768 |          |      |
| Root          |     | Address:48:0f:cf:af:14:0a |     |             |      | Priority:32768 |          |      |
|               |     | Port:1/1/25,              |     | Cost:40000, | Rem  | Hops:18        |          |      |
| Port          |     | Role                      |     | State       | Cost |                | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/25 |     | Root |     | Forwarding | 20000 |     | 128 | point_to_point |
| ------ | --- | ---- | --- | ---------- | ----- | --- | --- | -------------- |
100
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| 1/1/27 |     | Alternate |     | Blocking |     | 20000 128 | point_to_point |
| ------ | --- | --------- | --- | -------- | --- | --------- | -------------- |
#### MST2
| Vlans mapped: |     | 20                        |     |             |     |                |      |
| ------------- | --- | ------------------------- | --- | ----------- | --- | -------------- | ---- |
| Bridge        |     | Address:e0:07:1b:cb:01:7a |     |             |     | Priority:32768 |      |
| Root          |     | Address:48:0f:cf:af:14:0a |     |             |     | Priority:32768 |      |
|               |     | Port:1/1/25,              |     | Cost:40000, | Rem | Hops:18        |      |
| Port          |     | Role                      |     | State       |     | Cost Priority  | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/25 |     | Root      |     | Forwarding |     | 20000 128 | point_to_point |
| ------ | --- | --------- | --- | ---------- | --- | --------- | -------------- |
| 1/1/27 |     | Alternate |     | Blocking   |     | 20000 128 | point_to_point |
4. OnswitchD:
switch#
config
| switch(config)# |     | mvrp          |       |                 |        |     |     |
| --------------- | --- | ------------- | ----- | --------------- | ------ | --- | --- |
| switch(config)# |     | vlan 1        |       |                 |        |     |     |
| switch(config)# |     | spanning-tree |       |                 |        |     |     |
| switch(config)# |     | spanning-tree |       | priority        | 1      |     |     |
| switch(config)# |     | spanning-tree |       | config-name     | sp1    |     |     |
| switch(config)# |     | spanning-tree |       | config-revision |        | 1   |     |
| switch(config)# |     | spanning-tree |       | instance        | 1 vlan | 10  |     |
| switch(config)# |     | spanning-tree |       | instance        | 2 vlan | 20  |     |
| switch(config)# |     | interface     | 1/1/1 |                 |        |     |     |
switch(config-if)#
|                    |     | no        | shutdown |         |     |     |     |
| ------------------ | --- | --------- | -------- | ------- | --- | --- | --- |
| switch(config-if)# |     | no        | routing  |         |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native  | 1   |     |     |
| switch(config-if)# |     | vlan      | trunk    | allowed | all |     |     |
| switch(config-if)# |     | mvrp      |          |         |     |     |     |
| switch(config-if)# |     | exit      |          |         |     |     |     |
| switch(config)#    |     | interface | 1/1/2    |         |     |     |     |
| switch(config-if)# |     | no        | shutdown |         |     |     |     |
| switch(config-if)# |     | no        | routing  |         |     |     |     |
| switch(config-if)# |     | vlan      | trunk    | native  | 1   |     |     |
switch(config-if)#
|                    |               | vlan         | trunk     | allowed    | all     |                   |     |
| ------------------ | ------------- | ------------ | --------- | ---------- | ------- | ----------------- | --- |
| switch(config-if)# |               | mvrp         |           |            |         |                   |     |
| switch(config-if)# |               | exit         |           |            |         |                   |     |
| switch# show       | mvrp          | config       |           |            |         |                   |     |
| Configuration      | and           | Status       | -         | MVRP       |         |                   |     |
| Global MVRP        | status        | : Enabled    |           |            |         |                   |     |
| Port Status        |               | Registration |           | Join       | Leave   | LeaveAll Periodic |     |
|                    |               | Type         |           | Timer      | Timer   | Timer Timer       |     |
| ------- --------   |               | --------     |           | -----      | ------- | ------- --------  |     |
| 1/1/1              | Enabled       | normal       |           | 20         | 300     | 1000              | 100 |
| 1/1/2              | Enabled       | normal       |           | 20         | 300     | 1000              | 100 |
| switch# show       | mvrp          | state        |           |            |         |                   |     |
| Configuration      | and           | Status       | -         | MVRP state |         |                   |     |
| Port VLAN          | Registrar     |              | Applicant | Forbid     |         |                   |     |
|                    | State         |              | State     | Mode       |         |                   |     |
| ---- ----          | ---------     |              | --------- | ---------  |         |                   |     |
| 1/1/1 1            | IN            |              | QA        | No         |         |                   |     |
| 1/1/1 10           | MT            |              | QA        | No         |         |                   |     |
| 1/1/1 20           | IN            |              | VO        | No         |         |                   |     |
| 1/1/2 1            | IN            |              | AA        | No         |         |                   |     |
| 1/1/2 10           | IN            |              | VO        | No         |         |                   |     |
| 1/1/2 20           | MT            |              | AA        | No         |         |                   |     |
| switch# show       | spanning-tree |              |           | mst        |         |                   |     |
MVRP|101

#### MST0
| Vlans mapped: | 1-9,11-19,21-4094         |     |               |     |     |
| ------------- | ------------------------- | --- | ------------- | --- | --- |
| Bridge        | Address:48:0f:cf:af:14:0a |     | priority:4096 |     |     |
Root
| Regional Root |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 | txHoldC6 |     |     |     |     |
| ------------------ | -------- | --- | --- | --- | --- |
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-
| age(in seconds):20 | Max-Hop0                  |       |               |          |      |
| ------------------ | ------------------------- | ----- | ------------- | -------- | ---- |
| Root               | Address:48:0f:cf:af:14:0a |       | Priority:4096 |          |      |
|                    | Port:0                    |       | Path cost:0   |          |      |
| Regional Root      | Address:48:0f:cf:af:14:0a |       | Priority:4096 |          |      |
|                    | Internal cost:0           |       | Rem Hops:20   |          |      |
| Port               | Role                      | State | Cost          | Priority | Type |
-------------- -------------- ------------ ---------- ---------- ----------
| 1/1/1 | Designated | Forwarding | 20000 | 128 | point_to_ |
| ----- | ---------- | ---------- | ----- | --- | --------- |
point
| 1/1/2 | Designated | Forwarding | 20000 | 128 | point_to_ |
| ----- | ---------- | ---------- | ----- | --- | --------- |
point
#### MST1
| Vlans mapped: | 10                        |             |                |          |      |
| ------------- | ------------------------- | ----------- | -------------- | -------- | ---- |
| Bridge        | Address:48:0f:cf:af:14:0a |             | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |             | Priority:32768 |          |      |
|               | Port:0, Cost:0,           | Rem Hops:20 |                |          |      |
| Port          | Role                      | State       | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | ---------- | ----- | --- | -------------- |
| 1/1/2 | Designated | Forwarding | 20000 | 128 | point_to_point |
#### MST2
| Vlans mapped: | 20                        |             |                |          |      |
| ------------- | ------------------------- | ----------- | -------------- | -------- | ---- |
| Bridge        | Address:48:0f:cf:af:14:0a |             | Priority:32768 |          |      |
| Root          | Address:48:0f:cf:af:14:0a |             | Priority:32768 |          |      |
|               | Port:0, Cost:0,           | Rem Hops:20 |                |          |      |
| Port          | Role                      | State       | Cost           | Priority | Type |
-------------- -------------- ------------ ------- ---------- ----------
| 1/1/1 | Designated | Forwarding | 20000 | 128 | point_to_point |
| ----- | ---------- | ---------- | ----- | --- | -------------- |
| 1/1/2 | Designated | Forwarding | 20000 | 128 | point_to_point |
MVRP commands
clear mvrp statistics
clear mvrp statistics [<PORT-NUM> | <PORT-LIST> | LAG <LAG-NUM>]
Description
ResetstheMVRPstatisticcountersgloballyorforthespecifiedportsorLAG.
Parameter Description
<PORT-NUM> Specifiesaportnumber.
102
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| Parameter     |     |     | Description                                   |
| ------------- | --- | --- | --------------------------------------------- |
| <PORT-LIST>   |     |     | Specifiesalistofports.                        |
| LAG <LAG-NUM> |     |     | SpecifiesaLinkAggregationnumber.Range:1to128. |
Examples
| switch#             | clear mvrp | statistics | 1/1/1        |
| ------------------- | ---------- | ---------- | ------------ |
| Command History     |            |            |              |
| Release             |            |            | Modification |
| 10.07orearlier      |            |            | --           |
| Command Information |            |            |              |
| Platforms           | Command    | context    | Authority    |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
mvrp
mvrp
no mvrp
Description
EnablestheMVRPfeaturegloballyoronaspecificinterface.Bydefault,MVRPisdisabled.
ThenoformofthiscommanddisablesMVRP.
MVRPandVLANtranslationcannotbeenabledonthesameinterface.
Examples
EnablingMVRPglobally:
| switch(config)# | mvrp |     |     |
| --------------- | ---- | --- | --- |
EnablingMVRPonaninterface:
| switch(config)#    | interface | 1/1/1 |     |
| ------------------ | --------- | ----- | --- |
| switch(config-if)# |           | mvrp  |     |
| Command History    |           |       |     |
MVRP|103

| Release             |         |     |         | Modification |     |
| ------------------- | ------- | --- | ------- | ------------ | --- |
| 10.07orearlier      |         |     |         | --           |     |
| Command Information |         |     |         |              |     |
| Platforms           | Command |     | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|     | config-if |     |     | forthiscommand. |     |
| --- | --------- | --- | --- | --------------- | --- |
mvrp registration
| mvrp registration    |     | {normal   | | fixed       | | forbidden | [<VLAN-LIST>]} |
| -------------------- | --- | --------- | ------------- | ----------- | -------------- |
| no mvrp registration |     | forbidden | {<VLAN-LIST>} |             |                |
Description
ConfigurestheMVRPregistrarstatewhichdetermineshowanMVRPparticipantrespondstoMRP
messages.Thedefaultregistrationmodeisnormal.
ThenocommandremovesthespecifiedVLANsfromtheforbiddenlist.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
normal EnablesdynamicregistrationandderegistrationofVLANsonthe
interface,andpropagatesVLANinformationtootherswitcheson
thenetwork.Default.
| fixed |     |     |     | DisablesdynamicderegistrationofVLANsanddropsreceived |     |
| ----- | --- | --- | --- | ---------------------------------------------------- | --- |
MVRPframes.TheinterfacedoesnotderegisterdynamicVLANs
orregisternewdynamicVLANs.
forbidden DisablesdynamicregistrationofVLANsanddropsreceivedMVRP
frames.TheMVRPparticipantdoesnotregisternewdynamic
VLANsorre-registeraderegistereddynamicVLAN.
<VLAN-LIST> DisablesdynamicregistrationofVLANsanddropsreceivedMVRP
framesforspecificVLANsonly.Normalbehaviorappliestoall
otherVLANs.SpecifythenumberofasingleVLAN,oraseriesof
numbersforarangeofVLANs,separatedbycommas(1,2,3,4),
dashes(1-4),orboth(1-4,6).
Examples
switch(config)# switch(config-if)# mvrp registration forbidden 10
| switch(config-if)# |     | mvrp | registration | fixed     |           |
| ------------------ | --- | ---- | ------------ | --------- | --------- |
| switch(config-if)# |     | mvrp | registration | forbidden | 1,2,10-20 |
| Command History    |     |      |              |           |           |
104
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| Release        |             |         | Modification |     |
| -------------- | ----------- | ------- | ------------ | --- |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| mvrp       | timer         |                  |             |        |
| ---------- | ------------- | ---------------- | ----------- | ------ |
| mvrp timer | {join | leave | | leaveall       | | periodic} | <TIME> |
| no mvrp    | timer {join | | leave | leaveall | | periodic} |        |
Description
SetsanMVRPtimer.
Thenoformofthiscommandsetsthespecifiedtimertoitsdefaultvalue.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
join <TIME> Setsthejointimer.YoucanusethetimertospaceMVRPjoin
messages.Toensurethatjoinmessagesaretransmittedtoother
participants,anMRPparticipantwaitsforthespecifiedperiodof
thejointimerbeforesendingajoinmessage.TheJointimermust
belessthanhalfoftheLeaveTimer.Range:20to100in
centiseconds.Default:20.
leave <TIME> Setstheleavetimerfortheport,specifyingthetimethatthe
registrarstatemachinewaitsintheLVstatebeforetransitingto
theMTstate.Theleavetimermustbeatleasttwicethejointimer
andmustbelessthantheleavealltimer.Range:40-1000000
centiseconds.Default:300centiseconds.
leaveall <TIME> Setstheleavealltimerfortheport,specifyingthefrequencywith
whichtheleaveallstatemachinegeneratesleavealllPDUs.
Range:500to1000000centiseconds.Default:1000.
periodic <TIME> Setstheperiodictimerfortheport,specifyingthefrequencywith
whichtheperiodictransmissionstatemachinegeneratesperiodic
events.Theperiodictimerissetto1secondwhenitisstarted.
Range:100to1000000centiseconds.Default:100.
Examples
switch(config-if)#
|                |         | mvrp timer | join 22      |     |
| -------------- | ------- | ---------- | ------------ | --- |
| Command        | History |            |              |     |
| Release        |         |            | Modification |     |
| 10.07orearlier |         |            | --           |     |
MVRP|105

| Command Information |         |     |         |           |     |
| ------------------- | ------- | --- | ------- | --------- | --- |
| Platforms           | Command |     | context | Authority |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show mvrp | config |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
show mvrp config [<PORT-NUM> | <PORT-LIST> | LAG <LAG-NUM>] [vsx-peer]
Description
DisplaystheMVRPconfigurationforallL2portsoroptionallyfortheportsspecified.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<PORT-NUM> Specifiesdisplayinginformationforaparticularportnumber.
| <PORT-LIST> |     |     |     | Specifiesdisplayinginformationforalistofports. |     |
| ----------- | --- | --- | --- | ---------------------------------------------- | --- |
LAG <LAG-NUM> SpecifiesdisplayinginformationbyLAG.Range:1to128.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#             | show mvrp | config       |         |              |                   |
| ------------------- | --------- | ------------ | ------- | ------------ | ----------------- |
| Configuration       |           | and Status   | - MVRP  |              |                   |
| Global MVRP         | status    | : Disabled   |         |              |                   |
| Port                | Status    | Registration |         | Join Leave   | LeaveAll Periodic |
|                     |           | Type         |         | Timer Timer  | Timer Timer       |
| -------             | --------  | --------     |         | ----- -----  | ------ --------   |
| 1/1/1               | Disabled  | Normal       |         | 20 300       | 1000 100          |
| 1/1/2               | Disabled  | Normal       |         | 20 300       | 1000 100          |
| 1/1/3               | Disabled  | Normal       |         | 20 300       | 1000 100          |
| Command History     |           |              |         |              |                   |
| Release             |           |              |         | Modification |                   |
| 10.07orearlier      |           |              |         | --           |                   |
| Command Information |           |              |         |              |                   |
| Platforms           | Command   |              | context | Authority    |                   |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show mvrp | state |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
106
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| show mvrp | state | [<VLAN-ID> |     | | <VLAN-ID> |     | <PORT-NUM>] | [vsx-peer] |
| --------- | ----- | ---------- | --- | ----------- | --- | ----------- | ---------- |
Description
DisplaystheMVRPRegistrarandApplicantstatemachineinformationforallportsonwhichMVRPis
enabled,orforspecificports.
| Parameter |     |     |     |     | Description                             |     |     |
| --------- | --- | --- | --- | --- | --------------------------------------- | --- | --- |
| <VLAN-ID> |     |     |     |     | SpecifiesthenumberofaVLAN.Range:1-4094. |     |     |
<PORT-NUM>
Specifiesaphysicalportontheswitch.Forrmat:
member/slot/port.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
| switch#       |      | show mvrp | state      | 1         |           |          |     |
| ------------- | ---- | --------- | ---------- | --------- | --------- | -------- | --- |
| Configuration |      |           | and Status | - MVRP    | state     | for VLAN | 1   |
| Port          | VLAN | Registrar |            | Applicant |           |          |     |
|               |      | State     |            | State     |           |          |     |
| ----          | ---- | --------  |            | --------- |           |          |     |
| 1/1/1         | 1    | MT        |            | QA        |           |          |     |
| switch#       |      | show mvrp | state      | 10 1/1/1  |           |          |     |
| Configuration |      |           | and Status | - MVRP    | state     | for VLAN | 10  |
| Port          | VLAN | Registrar |            | Applicant | Forbid    |          |     |
|               |      | State     |            | State     | Mode      |          |     |
| ----          | ---- | --------- |            | --------- | --------- |          |     |
| 1/1/1         | 10   | MT        |            | LO        | Yes       |          |     |
switch#
| Command        | History     |         |     |         |              |     |     |
| -------------- | ----------- | ------- | --- | ------- | ------------ | --- | --- |
| Release        |             |         |     |         | Modification |     |     |
| 10.07orearlier |             |         |     |         | --           |     |     |
| Command        | Information |         |     |         |              |     |     |
| Platforms      |             | Command |     | context | Authority    |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show      | mvrp       | statistics |               |     |            |     |     |
| --------- | ---------- | ---------- | ------------- | --- | ---------- | --- | --- |
| show mvrp | statistics |            | [<PORT-LIST>] |     | [vsx-peer] |     |     |
Description
MVRP|107

Displays MVRP statistics for all ports or on the ports specified in the list.

Parameter

<PORT-LIST>

vsx-peer

Examples

Description

Specifies a list of ports. When specifying a list of ports, the ports
for which there are no statistics will be listed in the output.

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

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
In
4
48
Join Empty
555
Join In
Leave
0
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

switch# show mvrp statistics

1/1/1

: 0
: 48:0f:cf:af:b1:76

Status and Counters - MVRP
MVRP statistics for port : 1/1/1
----------------------------
Failed registration
Last PDU origin
Total PDU Transmitted : 14874
Total PDU Received
Frames Discarded
Message type
Received
-------------- ------------ ------------
New
0
1264
Empty
4
In
48
Join Empty
555
Join In
Leave
0
25
Leaveall

0
57181612
0
1425
563
0
13965

Transmitted

: 327
: 0

Command History

Release

10.07 or earlier

Modification

--

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

108

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
MVRP|109

Spanning tree protocols (STP)

Chapter 8

Spanning tree protocols (STP)

Protocols and feature details
Spanning tree protocols eliminate loops in a physical link-redundant network by selectively blocking
redundant links and putting them in a standby state.

Recent versions of STP include the Rapid Per-VLAN Spanning Tree Protocol (RPVST+) and the Multiple
Spanning Tree Protocol (MSTP).

STP
Spanning tree protocol (STP) was developed based on the 802.1d standard of IEEE to eliminate loops at
the data link layer in a LAN. Networks often have redundant links as backups in case of failures, but
loops are a very serious problem. Devices running STP detect loops in the network by exchanging
information with one another. They eliminate loops by selectively blocking certain ports to prune the
loop structure into a loop-free tree structure. This avoids proliferation and infinite cycling of packets that
would occur in a loop network.

In a narrow sense, STP refers to IEEE 802.1d STP. In a broad sense, STP refers to the IEEE 802.1d STP and
various enhanced spanning tree protocols derived from that protocol, such as MSTP and RPVST+.

Root bridge

A tree network must have a root bridge. The entire network contains only one root bridge, and all the
other bridges in the network are called leaf nodes. The root bridge is not permanent and can change
when there are changes in the network topology.

Upon initialization of a network, each device generates and periodically sends configuration BPDUs, with
itself as the root bridge. After network convergence, only the root bridge generates and periodically
sends configuration BPDUs. The other devices only forward the BPDUs.

Root port

On a non-root bridge, the port which has the least cost to reach the root bridge is the root port.

The root port communicates with the root bridge. Each non-root bridge has only one root port. The root
bridge has no root port.

Designated bridge and designated port

A designated bridge is a bridge on each LAN that provides the minimum root path cost. The designated
bridge of a LAN is the only bridge allowed to forward frames to and from the LAN.

The designated bridge:

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

110

n For a device: Device directly connected with the local device and responsible for forwarding BPDUs to

the local device.

n For a LAN: Device responsible for forwarding BPDUs to this LAN segment.

The designated port:

n For a device: Port through which the designated bridge forwards BPDUs to this device.

n For a LAN: Port through which the designated bridge forwards BPDUs to this LAN segment.

In the following topology, Device B and Device C are directly connected to a LAN.

Figure 1 Designated bridge and designated port

If Device A forwards BPDUs to Device B through port A1, the designated bridge and designated port are
as follows:

n The designated bridge for Device B is Device A.

n The designated port of Device B is port A1 on Device A.

If Device B forwards BPDUs to the LAN, the designated bridge and designated port are as follows:

n The designated bridge for the LAN is Device B.

n The designated port for the LAN is port B2 on Device B.

Path cost

Path cost is a reference value used for link selection in STP. To prune the network into a loop-free tree,
STP calculates path costs to select the most robust links and block redundant links that are less robust.

STP timers

The most important timing parameters in STP calculation are forward delay, hello time, and max age.

n Forward delay: Forward delay is the delay time for port state transition. A path failure can cause
spanning tree recalculation to adapt the spanning tree structure to the change. However, the
resulting new configuration BPDU cannot propagate throughout the network immediately. If the

Spanning tree protocols (STP) | 111

newly elected root ports and designated ports start to forward data immediately, a temporary loop
will likely occur. The newly elected root ports or designated ports require twice the forward delay
time before they transit to the forwarding state. This allows the new configuration BPDU to
propagate throughout the network.

n Hello time: The device sends hello packets at the hello time interval to the neighboring devices to

make sure the paths are fault-free.

n Max age: The device uses the max age to determine whether a stored configuration BPDU has

expired and discards it if the max age is exceeded.

BPDU forwarding mechanism

The configuration BPDUs of STP are forwarded according to these guidelines:

n Upon network initiation, every device regards itself as the root bridge and generates configuration
BPDUs with itself as the root. Then it sends the configuration BPDUs at a regular hello interval.

n If the root port received a configuration BPDU superior to the configuration BPDU of the port, the

device performs the following tasks:

o Increases the message age carried in the configuration BPDU.

o Starts a timer to time the configuration BPDU.

o Sends this configuration BPDU through the designated port.

n If a designated port receives a configuration BPDU with a lower priority than its configuration BPDU,

the port immediately responds with its configuration BPDU.

n If a path fails, the root port on this path no longer receives new configuration BPDUs and the old

configuration BPDUs will be discarded due to timeout. The device generates a configuration BPDU
with itself as the root and sends the BPDUs and TCN BPDUs. This triggers a new spanning tree
calculation process to establish a new path to restore the network connectivity.

However, the newly calculated configuration BPDU cannot be propagated throughout the network
immediately. As a result, the old root ports and designated ports that have not detected the topology
change continue forwarding data along the old path. If the new root ports and designated ports begin to
forward data as soon as they are elected, a temporary loop might occur.

STP protocol packets

STP uses bridge protocol data units (BPDUs), also known as configuration messages, as its protocol
packets. STP-enabled network devices exchange BPDUs to establish a spanning tree.

STP uses the following types of BPDUs:

n Configuration BPDUs: Used by the network devices to calculate a spanning tree and maintain the

spanning tree topology.

n Topology change notification (TCN) BPDUs: Use to notify network devices of network topology

changes.

Configuration BPDUs contain sufficient information for network devices to complete spanning tree
calculation. Important fields in a configuration BPDU include the following:

n Root bridge ID: Priority and MAC address of the root bridge.

n Root path cost: Cost of the path to the root bridge indicated by the root identifier from the

transmitting bridge.

n Designated bridge ID: Priority and MAC address of the designated bridge.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

112

n Designated port ID: Priority and global port number of the designated port.

n Message age: Age of the configuration BPDU while it propagates in the network.

n Max age: Maximum age of the configuration BPDU stored on the switch.

n Hello time: Configuration BPDU transmission interval.

n Forward delay: Delay that STP bridges use to transit port state.

Comparing spanning tree options

Without spanning tree, having more than one active path between a pair of network devices causes
loops in the network that can result in duplication of messages, leading to a broadcast storm that can
bring down the network.

The 802.1D spanning tree protocol operates without regard to a network's VLAN configuration, and
maintains one common spanning tree throughout a bridged network. This protocol maps one loop-free,
logical topology onto a given physical topology, resulting in the least optimal link utilization and longest
convergence times.

The 802.1s multiple spanning tree protocol (MSTP) uses multiple spanning tree instances with separate
forwarding topologies. Each instance is composed of one or more VLANs. This significantly improves
network link utilization and the speed of reconvergence after a failure in the network’s physical
topology. RPVST+ is a proprietary Cisco protocol, whereas MSTP is an open standard protocol based on
IEEE 802.1s. So, in multi-vendor environments, MSTP is the preferred option because of interoperability.

In RPVST+, the number of spanning tree instances is equal to the number of VLANs. RPVST+ may
become quite resource intensive as a result. The number of spanning tree instances in MSTP can
theoretically be the same as the number of VLANs, but in practice, the number of spanning tree
instances is limited to a number of physical topologies that is much fewer than the number of VLANs in
the network.

RPVST+ is a Cisco-proprietary enhancement to PVST+, which is itself a Cisco-proprietary enhancement
to 802.1D STP. PVST+ enables you to create one instance of spanning-tree per VLAN. Similar to PVST+,
RPVST+ also enables you to create one spanning-tree instance per VLAN. The difference is network
convergence is faster with RPVST+ than PVST+.

With RPVST+, VLAN tagging is applied to the ports in a multi-VLAN network to enable blocking of
redundant links in one VLAN, while allowing forwarding over the same links for non-redundant use by
another VLAN. Each RPVST+ tree can have a different root switch and therefore can span through
different links. Since different VLAN traffic can take different active paths from multiple possible
topologies, overall network utilization increases.

Preparing for spanning tree configuration

Before configuring a spanning tree:

n Determine the spanning tree protocol to be used: RPVST+ or MSTP. RPVST+ is ideal in networks
having fewer VLANs. In networks having more VLANs, MSTP is the recommended spanning tree
choice due to the increased load on the switch CPU. Even if you have more VLANs, MSTP supports 64
instances, which is more than enough to disperse the load. The switch can distribute the VLANs in
use among instances as evenly as feasible, allowing one instance to block redundant links while
allowing another instance to forward traffic over the same links for non-redundant use.

n Plan the device roles (the root bridge or leaf node) by adjusting instance priority.

When you configure spanning tree protocols, follow these guidelines:

Spanning tree protocols (STP) | 113

n If MSTP is enabled on the switch, MSTP takes all MSTI information along with the packet. To advertise
a specific VLAN within the network through MSTP, make sure that the VLAN is mapped to an MSTI
when you configure the VLAN-to-instance table.

n Configuring instances is not mandatory. It is optional. Simply enable spanning tree (with command
spanning-tree) and then MSTP works with CIST on all switches (CIST is the common instance for all
VLANs in the switch).

n STP is mutually exclusive with loop protection. If STP and loop protection are both enabled on the
same VLAN, STP takes precedence. This means that loop protection does not take any action on a
port blocked by STP.

n RPVST+ uses IEEE BPDU on the native VLAN and VLAN 1, to converge with MSTP. However RPVST+
uses proprietary PVST MAC address 01:00:0c:cc:cc:cd to converge with other RPVST VLANs. For
example, if we enable 'spanning-tree vlan 2' on two switches, these switches converge by exchanging
PVST proprietary MAC and not IEEE MAC. In this case, 'spanning-tree vlan 1' sends 1 IEEE MAC to
converge with the MSTP network and it also sends 1 PVST MAC to converge with RPVST network.

n One spanning tree variant can be run on the switch at any given time. On a switch running RPVST+,

MSTP cannot be enabled. However, any MSTP-specific configuration settings in the startup
configuration file will be maintained.

n The following features cannot run concurrently with RPVST+:

o Multiple VLAN Registration Protocol (MVRP).

o Filter multicast in RPVST+ mode (The multicast MAC address value cannot be set to the PVST MAC

address 01:00:0c:cc:cc:cd.)

n After you enable a spanning tree protocol on a layer 2 aggregate interface, the system performs

spanning tree calculation on the layer 2 aggregate interface. It does not perform the spanning tree
calculation on the aggregation member ports. The spanning tree protocol enable state and
forwarding state of each selected member port is consistent with the state of the corresponding
layer 2 aggregate interface.

n Before using AAA and RPVST IOP, you must configure RADIUS-based and MAC-based VLANs statically

and also enable RPVST on those VLANs.

STP cost calculation

Simplified calculation overview

A tree-shape topology forms once the root bridge, root ports, and designated ports are selected.

1. Upon initialization of a device, each port generates a BPDU with the following contents:

n The port as the designated port.

n The device as the root bridge.

n 0 as the root path cost.

n The device ID as the designated bridge ID.

2.

Initially, each STP-enabled device on the network assumes itself to be the root bridge, with its
own device ID as the root bridge ID. By exchanging configuration BPDUs, the devices compare
their root bridge IDs to elect the device with the smallest root bridge ID as the root bridge.

3. Root port and designated ports selection on the non-root bridges.

n A non-root–bridge device regards the port on which it received the optimum configuration

BPDU as the root port.

o Upon receiving a configuration BPDU on a port, the device compares the priority of the

received configuration BPDU with that of the configuration BPDU generated by the port. If

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

114

the former priority is lower, the device discards the received configuration BPDU and keeps
the configuration BPDU the port generated. If the former priority is higher, the device
replaces the content of the configuration BPDU generated by the port with the content of
the received configuration BPDU.

o The device compares the configuration BPDUs of all the ports and chooses the optimum

configuration BPDU.

n Based on the configuration BPDU and the path cost of the root port, the device calculates a

designated port configuration BPDU for each of the other ports.

o The root bridge ID is replaced with that of the configuration BPDU of the root port.

o The root path cost is replaced with that of the configuration BPDU of the root port plus the

path cost of the root port.

o The designated bridge ID is replaced with the ID of this device.

o The designated port ID is replaced with the ID of this port.

n The device compares the calculated configuration BPDU with the configuration BPDU on the

port whose port role will be determined, and acts depending on the result of the comparison:

o If the calculated configuration BPDU is superior, the device performs the following tasks:

l Considers this port as the designated port.

l Replaces the configuration BPDU on the port with the calculated configuration BPDU.

l Periodically sends the calculated configuration BPDU.

o If the configuration BPDU on the port is superior, the device blocks this port without

updating its configuration BPDU. The blocked port can receive BPDUs, but cannot send
BPDUs or forward data traffic.

When the network topology is stable, only the root port and designated ports forward user
traffic. Other ports are all in the blocked state to receive BPDUs but not to forward BPDUs or user
traffic.

4. The principles of configuration BPDU comparison:

n The configuration BPDU with the lowest root bridge ID has the highest priority.

n If configuration BPDUs have the same root bridge ID, their root path costs are compared. For
example, the root path cost in a configuration BPDU plus the path cost of a receiving port is S.
The configuration BPDU with the smallest S value has the highest priority.

n If all configuration BPDUs have the same root bridge ID and S value, the following attributes

are compared in sequence: Designated bridge IDs, Designated port IDs, and IDs of the
receiving ports.

The configuration BPDU that contains a smaller designated bridge ID, designated port ID, or
receiving port ID is selected.

Calculation example

The following topology is used to illustrate an STP calculation. The priority values of Device A, Device B,
and Device C are 0, 1, and 2, respectively. The path costs of links among the three devices are 5, 10, and
4.

Spanning tree protocols (STP) | 115

Figure2 STPcalculation
EachconfigurationBPDUcontainsthefollowingfields:rootbridgeID,rootpathcost,designatedbridge
ID,anddesignatedportID.
1. TheinitialstateoftheBPDUsoneachdeviceis:
| Device  |     | Port name | Configuration  | BPDU on | the port |
| ------- | --- | --------- | -------------- | ------- | -------- |
| DeviceA |     | PortA1    | {0,0,0,PortA1} |         |          |
|         |     | PortA2    | {0,0,0,PortA2} |         |          |
| DeviceB |     | PortB1    | {1,0,1,PortB1} |         |          |
|         |     | PortB2    | {1,0,1,PortB2} |         |          |
| DeviceC |     | PortC1    | {2,0,2,PortC1} |         |          |
|         |     | PortC2    | {2,0,2,PortC2} |         |          |
2. BPDUcomparisononeachdeviceoccursasfollows:
|        |            |         | Configuration | BPDU | on  |
| ------ | ---------- | ------- | ------------- | ---- | --- |
| Device | Comparison | process |               |      |     |
ports after comparison
DeviceA PortA1performsthefollowingtasks: n PortA1:{0,0,0,PortA1}
1. ReceivestheconfigurationBPDUofPortB1{1, n PortA2:{0,0,0,PortA2}
0,1,PortB1}.
2. Determinesthatitsexistingconfiguration
BPDU{0,0,0,PortA1}issuperiortothe
receivedconfigurationBPDU.
3. Discardsthereceivedone.
PortA2performsthefollowingtasks:
1. ReceivestheconfigurationBPDUofPortC1{2,
0,2,PortC1}.
116
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

Device

Comparison process

Configuration BPDU on
ports after comparison

2. Determines that its existing configuration

BPDU {0, 0, 0, Port A2} is superior to the

received configuration BPDU.

3. Discards the received one.
Device A determines that it is both the root bridge
and designated bridge in the configuration BPDUs
of all its ports. It considers itself as the root bridge.
It does not change the configuration BPDU of any
port and starts to periodically send configuration
BPDUs.

Device B

Port B1 performs the following tasks:

1. Receives the configuration BPDU of Port A1 {0,

0, 0, Port A1}.

2. Determines that the received configuration

BPDU is superior to its existing configuration
BPDU {1, 0, 1, Port B1}.

3. Updates its configuration BPDU.
Port B2 performs the following tasks:

1. Receives the configuration BPDU of Port C2 {2,

0, 2, Port C2}.

2. Determines that its existing configuration

BPDU {1, 0, 1,Port B2} is superior to the

received configuration BPDU.

3. Discards the received BPDU.

n Port B1: {0, 0, 0, Port A1}
n Port B2: {1, 0, 1, Port B2}

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

n Port C1: {0, 0, 0, Port A2}
n Port C2: {1, 0, 1, Port B2}

Spanning tree protocols (STP) | 117

Device

Comparison process

Configuration BPDU on
ports after comparison

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

Device C performs the following tasks:

n Root port (Port C1): {0, 0,

1. Compares the configuration BPDUs of all its

0, Port A2}

n Designated port (Port C2):

{0, 10, 2, Port C2}

ports.

2. Decides that the configuration BPDU of Port

C1 is the optimum.

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

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

118

Configuration BPDU on
ports after comparison

n Blocked port (Port C1): {0,

0, 0, Port A2}

n Root port (Port C2): {0, 5,

1, Port B2}

Device

Comparison process

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

Port C1 does not forward data until a new event
triggers a spanning tree calculation process: for
example, the link between Device B and Device C is
down.

3. After the comparison, a spanning tree with Device A as the root bridge is established as shown:

Figure 3 Device A as root bridge

Spanning tree protocols (STP) | 119

STP supported platforms and scale
PTP is supported on all AOS-CX switches.

Scale

Platform

RPVST+ VLANs

RPVST+ vPorts

MSTP instances

8400

254

2048

64

MSTP protocol and feature details
Multiple-Instance spanning tree protocol (MSTP) ensures that only one active path exists between any
two nodes in a spanning-tree instance. A spanning-tree instance comprises a unique set of VLANs, and
belongs to a specific spanning-tree region. A region can comprise multiple spanning-tree instances
(each with a different set of VLANs), and allows one active path among regions in a network.

Without spanning tree, having more than one active path between a pair of nodes causes loops in the
network, which can result in duplication of messages, leading to a “broadcast storm” that can bring
down the network.

Developed based on IEEE 802.1s, MSTP overcomes the limitations of STP, RSTP, and PVST. In addition to
supporting rapid network convergence, it allows data flows of different VLANs to be forwarded along
separate paths. This provides a better load sharing mechanism for redundant links.

MSTP provides the following features:

n MSTP divides a switched network into multiple regions, each of which contains multiple spanning

trees that are independent of one another.

n MSTP supports mapping VLANs to spanning tree instances by means of a VLAN-to-instance mapping
table. MSTP can reduce communication overheads and resource usage by mapping multiple VLANs
to one instance.

n MSTP prunes a loop network into a loop-free tree, which avoids proliferation and endless cycling of
packets in a loop network. In addition, it supports load balancing of VLAN data by providing multiple
redundant paths for data forwarding.

n MSTP is compatible with STP and RSTP, and partially compatible with PVST.

n Configuring instances is not mandatory. MSTP can work with the default instance CIST if spanning-

tree is just enabled. All existing VLANs in the switch will be part of CIST.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

120

MSTP key concepts

MSTP divides an entire Layer 2 network into multiple MST regions, which are connected by a calculated
CST. Inside an MST region, multiple spanning trees, called MSTIs, are calculated. Among these MSTIs,
MSTI 0 is the internal spanning tree (IST).

Figure 4 Network with four MST regions and four switches per region

Figure 5 MST region 3

Spanning tree protocols (STP) | 121

MST region

A multiple spanning tree region (MST region) consists of multiple devices in a switched network and the
network segments between them. All these devices have the following characteristics:

n A spanning tree protocol enabled.

n Same region name.

n Same VLAN-to-instance mapping configuration.

n Same MSTP revision level.

n Physically linked together.

Multiple MST regions can exist in a switched network. You can assign multiple devices to the same MST
region.

n The switched network comprises four MST regions, MST region 1 through MST region 4.

n All devices in each MST region have the same MST region configuration.

MSTI

MSTP can generate multiple independent spanning trees in an MST region, and each spanning tree is
mapped to specific VLANs. Each spanning tree is referred to as a multiple spanning tree instance (MSTI).
In the figures, MST region 3 comprises three MSTIs, MSTI 1, MSTI 2, and MSTI 0.

MSTI 0

VLAN-to-instance mapping table

As an attribute of an MST region, the VLAN-to-instance mapping table describes the mapping
relationships between VLANs and MSTIs.

In the figures, the VLAN-to-instance mapping table of MST region 3 is as follows:

n VLAN 1 to MSTI 1. (Ports which are not part of any VLAN are by default part of VLAN 1.)

n VLAN 2 and VLAN 3 to MSTI 2.

n Other VLANs to MSTI 0. (VLANs that are not configured as part of any MSTI are by default part of MSTI

0.)

MSTP achieves load balancing by means of the VLAN-to-instance mapping table.

CST

The common spanning tree (CST) is a single spanning tree that connects all MST regions in a switched
network. If you regard each MST region as a device, the CST is a spanning tree calculated by these
devices through STP or RSTP. The blue lines in the figures represent the CST.

IST

An internal spanning tree (IST) is a spanning tree that runs in an MST region. It is also called MSTI 0, a
special MSTI to which all VLANs are mapped by default. In the figures, MSTI 0 is the IST in MST region 3.

CIST

The common and internal spanning tree (CIST) is a single spanning tree that connects all devices in a
switched network. It consists of the ISTs in all MST regions and the CST. In the figures, the ISTs (MSTI 0)
in all MST regions plus the inter-region CST constitute the CIST of the entire network.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

122

Regional root

The root bridge of the IST or an MSTI within an MST region is the regional root of the IST or MSTI. Based
on the topology, different spanning trees in an MST region might have different regional roots, as
shown in MST region 3 in the figures:

n The regional root of MSTI 1 is Device B.

n The regional root of MSTI 2 is Device C.

n The regional root of MSTI 0 (also known as the IST) is Device A.

Common root bridge

The common root bridge is the root bridge of the CIST. In the figures, the common root bridge is a
device in MST region 1.

Port roles

A port can play different roles in different MSTIs. In the following figure, an MST region comprises
Device A, Device B, Device C, and Device D. Port A1 and port A2 of Device A connect to the common root
bridge. Port B2 and Port B3 of Device B form a loop. Port C3 and Port C4 of Device C connect to other
MST regions. Port D3 of Device D directly connects to a host.

MSTP calculation involves the following port roles:

n Root port: Forwards data for a non-root bridge to the root bridge. The root bridge does not have any

root port.

n Designated port: Forwards data to the downstream network segment or device.

n Alternate port: Acts as the backup port for a root port or conductor port. When the root port or

conductor port is blocked, the alternate port takes over.

n Backup port: Acts as the backup port of a designated port. When the designated port is invalid, the

backup port becomes the new designated port. A loop occurs when two ports of the same spanning
tree device are connected, so the device blocks one of the ports. The blocked port acts as the backup.

n Edge port: Does not connect to any network device or network segment, but directly connects to a

user host.

n Conductor port: Acts as a port on the shortest path from the local MST region to the common root
bridge. The conductor port is not always located on the regional root. It is a root port on the IST or
CIST and still a conductor port on the other MSTIs.

n Boundary port: Connects an MST region to another MST region or to an STP/RSTP-running device. In
MSTP calculation, a boundary port's role on an MSTI is consistent with its role on the CIST. However,
that is not true with conductor ports. A conductor port on MSTIs is a root port on the CIST.

Port states

In MSTP, a port can be in one of the following states:

n Forwarding: The port receives and sends BPDUs, learns MAC addresses, and forwards user traffic.

n Learning: The port receives and sends BPDUs, learns MAC addresses, but does not forward user

traffic. Learning is an intermediate port state.

n Discarding: The port receives and sends BPDUs, but does not learn MAC addresses or forward user

traffic.

When in different MSTIs, a port can be in different states.

Spanning tree protocols (STP) | 123

A port state is not exclusively associated with a port role. The following table lsts the port states that
each port role supports. (An X indicates that the port supports this state, while a dash [—] indicates that
the port does not support this state.)

Port state

Root port/
conductor port

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

n MSTP regards each MST region as a single device and generates a CST among these MST regions

through calculation.

The CST and ISTs constitute the CIST of the entire network.

MSTI calculation

Within an MST region, MSTP generates different MSTIs for different VLANs based on the VLAN-to-
instance mappings. For each spanning tree, MSTP performs a separate calculation process similar to
spanning tree calculation in STP.

In MSTP, a BPDU packet is forwarded along the following paths:

n Within an MST region, the packet is forwarded along the corresponding MSTI.

n Between two MST regions, the packet is forwarded along the CST.

MSTP on VSX

See the Virtual Switching Extension (VSX) Guide for important information when configuring MSTP with
VSX.

MSTP configuration tasks

n Configuring MSTP instances is not mandatory. Instances are required only if you need to reuse the
blocked links for some other VLAN path. To enable MSTP, simply configure the same 'configuration-
name' across all switches and enable 'spanning-tree' and leave the configuration-revision as default.
This is sufficient for MSTP.

n Ensure that the VLAN configuration in your network supports all of the forwarding paths necessary
for the desired connectivity. All ports connecting one switch to another within a region and one
switch to another between regions should be configured as members of all VLANs configured in the
region.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

124

n Configure all ports or trunks connecting one switch to another within a region as members of all

VLANs in the region. Otherwise, some VLANs could be blocked from access to the spanning tree root
for an instance or for the region.

n Plan individual MST regions based on VLAN groupings. That is, plan on all MSTP switches in a given
region supporting the same set of VLANs. Within each region, determine the VLAN membership for
each spanning tree instance. (Each instance represents a single forwarding path for all VLANs in that
instance.)

n Verify that there is one logical spanning tree path through the following:

o Any interregional links

o Any IST (Internal Spanning Tree) or MSTI within a region

o Any legacy (802.1D or 802.1w) switch or group of switches. (Where multiple paths exist between
an MST region and a legacy switch, expect the CST (Common Spanning Tree) to block all but one
such path.)

n Determine the root bridge and root port for each MSTI.

n Determine the designated bridge and designated port for each LAN segment.

n Determine which VLANs to assign to each MST instance and use port trunks with 802.1Q VLAN
tagging where separate links for separate VLANs would result in a blocked link preventing
communication between nodes on the same VLAN.

n Set the admin-edge port type to admin-edge for edge ports connected to end nodes.

n Set the admin-edge port type to admin-network for ports connected to another switch, a bridge, or a

half-duplex repeater.

MSTP considerations and best practices

n For the best MSTP experience, use at least AOS-CX 10.07.

n Topology Change Notifications (TCN) are an important part of STP. However, reducing unwanted
TCNs is important for things such as access ports which can go up and down with end-point
attachment and detachment at the network edge. It is recommended to use command spanning-
tree port-type admin-edge to remove unwanted TCNs from end points.

n The use of spanning tree Topology Change Notification (TCN) guard may also be used in certain

circumstances using command spanning-tree tcn-guard.

o If the access switch is rebooting or the link between access and core switches is flapping, then this
will cause TCNs towards the network core. Any TC on any interface on the core will clear all MACs
locally and propagate the TC on all other interfaces. This can cause a significant traffic disruption
on the network. If the network has a loop-free topology and mac-flush is not really needed on all
switches in the network, then it can be feasible to add tcn-guard on access switches facing L2
interfaces. This will avoid mac-flush and TC propagation on the core switch (STP root switch).

o If a core or aggregation switch in the network keeps getting TC messages due to unpredictable

behavior of an access switch, TCN guard can be applied (using command spanning-tree tcn-guard)
to the core or aggregation switch on the Layer 2 link facing the access switch.

n Stability in a spanning tree environment is paramount. It is recommended that default timers be

used, and any alteration of timers be carried out only under special circumstances and in
consultation with experts.

n Avoid automatic placement of root bridges. To enable a deterministic, predictable, and stable
network, the placement of Primary and Secondary root bridges should be considered using
command command spanning-tree vlan <VALUE> priority <VALUE>.

Spanning tree protocols (STP) | 125

n To further provide stability and deterministic behavior additional security configuration should be

considered, such as:

o root-guard: Sets a port to ignore superior BPDUs to prevent it from becoming the root port. This
is typically carried out between the core that is required to be the root and access switches to
prevent ports that are not expected to originate root information such as server ports and access
switch ports.

o bpdu-guard: Disables the specific port if the port receives STP BPDUs. This is done to prevent any
inadvertent spanning tree or malicious attack, or switches being connected to the network and
causing STP processing. This will be on well-defined ports that are known from your network
design on which you never expect BPDUs. For example, user access ports or ports connected to
servers in the datacenter where other switches may exist, and technicians can inadvertently patch
into.

n With VSX configuration it is advisable that either the VSX pair acts as a STP root switch or that the STP

root switch is reachable only through mc-lags. An STP root switch connected to a VSX pair with
standalone interfaces (non-mc-lags) is not recommended.

MSTP use cases

MSTP use case: Preventing loops

In this use case, all four switches are in same region. VLANs 10, 20, 30, 40, 50, and 60 are defined on all
switches, causing a network loop. The physical topology of the network looks like this:

Figure 6 Physical topology before loop elimination

To eliminate the loop, MSTP is enabled on all the switches, with the following configuration:

n Switch B is the root for CIST, MST1, and MST2.

n CIST: VLANs 10, 20

n Instance-1: VLANs 30, 40

n Instance-2: VLANs 50, 60

n All four switches are in the same MSTP region.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

126

To understand how MSTP works in this use case, it is useful to view each instance as a separate logical
topology as illustrated in the following figures.

In this initial configuration, loops are avoided by blocking the alternate links for each network segment.
All ports designated A (Alternate) are blocked and do not forward traffic. Although this strategy
eliminates the loops, it is not the most effective way to configure the MST regions because network
resources are not fully used.

Figure 7 MSTP loop elimination, initial configuration

By changing the root for each instance, more effective load sharing can be achieved. With this refined
configuration, the links (ports) that were previously unused are now being used by different instances.
Also, the network loop is eliminated and load sharing is achieved:

Figure 8 MSTP loop elimination, refined configuration

Procedure

Configure all switches with the same VLANs, interfaces, and spanning tree instances.

1. Create VLANs 10, 20, 30, 40, 50, and 60 and assign them to interfaces.

switch# config
switch(config)# vlan 10,20,30,40,50,60
switch(config)# interface 1/1/1-1/1/4
switch(config-if-<1/1/1-1/1/4>)# no shutdown
switch(config-if-<1/1/1-1/1/4>)# no routing
switch(config-if-<1/1/1-1/1/4>)# vlan trunk allowed 10,20,30,40,50,60

Spanning tree protocols (STP) | 127

| switch(config-if)# | exit |     |     |
| ------------------ | ---- | --- | --- |
2. Configurespanningtreeandenableit.
| switch(config)# | spanning-tree | config-name     | reg |
| --------------- | ------------- | --------------- | --- |
| switch(config)# | spanning-tree | config-revision | 1   |
switch(config)#
|                 | spanning-tree | inst 1 vlan | 30  |
| --------------- | ------------- | ----------- | --- |
| switch(config)# | spanning-tree | inst 1 vlan | 40  |
| switch(config)# | spanning-tree | inst 2 vlan | 50  |
| switch(config)# | spanning-tree | inst 2 vlan | 60  |
| switch(config)# | spanning-tree |             |     |
3. OnswitchA,setinstance1topriority0.
| switch-A(config)# | spanning-tree | inst 1 | priority 0 |
| ----------------- | ------------- | ------ | ---------- |
4. OnswitchC,setinstance2topriority0.
| switch-C(config)# | spanning-tree | inst 2 | priority 0 |
| ----------------- | ------------- | ------ | ---------- |
5. OnswitchBsettheMSTPdefaultCISTinstancepriorityto0.
| switch-B(config)# | spanning-tree | priority | 0   |
| ----------------- | ------------- | -------- | --- |
128
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

MSTP use case: Deterministic root bridges

Continuing from the previous MSTP use case and as mentioned in MSTP considerations and best
practices, the placement of root bridges is important in the Layer 2 network domain. Having
deterministic Root and Secondary Root bridges is a typically-accepted design that allows you to provide
predictability and protection in your network .

The Root and Secondary root are typically placed at the Core of the Layer 2 domain. Figure 9,
Deterministic root bridges (physical) shows the physical topology and Figure 10, Deterministic root
bridges (logical) shows the logical topology. Switch A and Switch B are the core/center of the Layer 2
domain, and they provide root redundancy for each other.

Figure 9 Deterministic root bridges (physical)

Figure 10 Deterministic root bridges (logical)

In this use case network example there are four VLANs 10, 11, 20 and 21, and the default other VLANs
and each group of VLANs has its own independent topology. The root bridges and VLANs are as follows:

n VLAN 10-11 is assigned to MSTP instance 1, Root bridge Switch A, and Secondary Root bridge Switch

B.

Spanning tree protocols (STP) | 129

n VLAN20-21isassignedtoMSTPinstance2,RootbridgeSwitchB,andSecondaryRootbridgeSwitch
A.
n AllotherVLANsareassignedtothedefaultMSTPinstance0.
SwitchesAthroughDareconfiguredasfollows:
Inthefollowingswitchconfigurationcommandsequences,configurationportions(typicallydefault)unrelatedto
MSTParerepresentedbyanellipsis"...".Also,descriptivecomments,precededby"<--",areincludedtothe
rightofsomecommands.
Switch A configuration
n AddVLANs10,11,20,21.
n ConfigureSTPmakingSwitchAtheRootforVLANs10and11,instance1andtheSecondaryRootfor
VLANs20and21instance2.
n TrunkallVLANsforinterface1/1/1to1/1/3.
n MakeSwitchAtheRootfortheCIST
config
vlan 10-11,20-21
exit
spanning-tree
| spanning-tree | config-name     | sp1          |           |             |          |
| ------------- | --------------- | ------------ | --------- | ----------- | -------- |
| spanning-tree | config-revision | 1            |           |             |          |
| spanning-tree | instance        | 1 vlan 10-11 | <-- Map   | VLANs to    | instance |
| spanning-tree | instance        | 2 vlan 20-21 |           |             |          |
| spanning-tree | priority        | 0            | <-- MST   | 0 Root      |          |
| spanning-tree | instance        | 1 priority   | 0 <-- MST | 1 Root      |          |
| spanning-tree | instance        | 2 priority   | 1 <-- MST | 2 Secondary | Root     |
int 1/1/1-1/1/3
| vlan trunk | 10-11,20-21 |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
| vlan trunk | native 1    |     |     |     |     |
exit
Switch B configuration
n AddVLANs10,11,20,21.
n ConfigureSTPmakingSwitchBtheRootforVLANs20and21,instance2andtheSecondaryRootfor
VLANs10and11instance1.
n TrunkallVLANsforinterface1/1/1to1/1/3.
SwitchB#
config
vlan 10-11,20-21
exit
spanning-tree
| spanning-tree | config-name     | sp1          |           |             |      |
| ------------- | --------------- | ------------ | --------- | ----------- | ---- |
| spanning-tree | config-revision | 1            |           |             |      |
| spanning-tree | instance        | 1 vlan 10-11 |           |             |      |
| spanning-tree | instance        | 2 vlan 20-21 |           |             |      |
| spanning-tree | instance        | 1 priority   | 1 <-- MST | 1 Secondary | Root |
| spanning-tree | instance        | 2 priority   | 0 <-- MST | 2 Root      |      |
int 1/1/1-1/1/3
| vlan trunk | 10-11,20-21 |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
130
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| vlan trunk | native 1 |     |     |
| ---------- | -------- | --- | --- |
exit
| Switch C and | D configuration |     |     |
| ------------ | --------------- | --- | --- |
n DefinetheVLANSforMSTPandthetrunk-requiredVLANSusingthesameconfigurationonbothC
andDexceptforthehostname.
vlan 10-11,20-21
exit
spanning-tree
| spanning-tree | config-name     |        | sp1   |
| ------------- | --------------- | ------ | ----- |
| spanning-tree | config-revision |        | 1     |
| spanning-tree | instance        | 1 vlan | 10-11 |
| spanning-tree | instance        | 2 vlan | 20-21 |
int 1/1/2-1/1/3
int 1/1/2-1/1/3
| vlan trunk | 10-11,20-21 |     |     |
| ---------- | ----------- | --- | --- |
| vlan trunk | native 1    |     |     |
exit
| Checking the | configuration |     |     |
| ------------ | ------------- | --- | --- |
Theappliedconfigurationscanbecheckedasfollows:
n CheckingMSTP
n CheckingthattheSystemIDmatchesRootfortheinstance.
| Checking Switch | A   |     |     |
| --------------- | --- | --- | --- |
Usecommandshow spanning-tree mst-configtocheckthegeneralconfigurationandmappings.
| SwitchA#          | show spanning-tree                 |       | mst-config                       |
| ----------------- | ---------------------------------- | ----- | -------------------------------- |
| MST configuration | information                        |       |                                  |
| MST config        | ID                                 | :     | sp1                              |
| MST config        | revision                           | :     | 1                                |
| MST config        | digest                             | :     | 098798F08296B22CADC0650E39604C10 |
| Number            | of instances                       | :     | 2                                |
| Instance          | ID Member                          | VLANs |                                  |
| ---------------   | ---------------------------------- |       |                                  |
| 0                 | 1-9,12-19,22-4094                  |       |                                  |
| 1                 | 10,11                              |       |                                  |
| 2                 | 20,21                              |       |                                  |
Usecommandshow spanning-tree summary roottocheckrootconfiguration.Asseenhere,SwitchA
isRootforinstance0and1,identifiedbytheSystemID,andInstance2Rootisanotherdevicewhichis
expectedtobeSwitchBbasedonpreviousconfigurations.
NoticethezeroRootPortcostindicatedinthefirsttworowsofoutput.
SwitchA#show
|             | spanning-tree    |     | summary root        |
| ----------- | ---------------- | --- | ------------------- |
| STP status  |                  |     | : Enabled           |
| Protocol    |                  |     | : MSTP              |
| System ID   |                  |     | : 08:00:09:8a:14:fa |
| Root bridge | for STP Instance |     | : 0,1               |
Spanningtreeprotocols(STP)|131

|          |     |          |     |         | Root Hello | Max      | Fwd |      |      |
| -------- | --- | -------- | --- | ------- | ---------- | -------- | --- | ---- | ---- |
| Instance | ID  | Priority |     | Root ID | cost       | Time Age | Dly | Root | Port |
--------------- -------- ----------------- --------- ----- --- --- ------------
| 0               |     |     | 0   | 08:00:09:8a:14:fa | 0     | 2 20 | 15  |       | 0   |
| --------------- | --- | --- | --- | ----------------- | ----- | ---- | --- | ----- | --- |
| 1               |     |     | 0   | 08:00:09:8a:14:fa | 0     | 2 20 | 15  |       | 0   |
| 2               |     |     | 0   | 08:00:09:12:8e:9e | 20000 | 2 20 | 15  | 1/1/1 |     |
| Checking Switch |     | B   |     |                   |       |      |     |       |     |
Usecommandshow spanning-tree summary roottocheckrootconfiguration.Asseenhere,SwitchB
isRootforInstance2andidentifiedbySystemIDwhichwasalsoshownintheaboveSwitchA
command.
NoticethezeroRootPortcostindicatedinthelastoutputrow.
| SwitchA#show |     | spanning-tree |          | summary root        |            |          |     |      |      |
| ------------ | --- | ------------- | -------- | ------------------- | ---------- | -------- | --- | ---- | ---- |
| STP status   |     |               |          | : Enabled           |            |          |     |      |      |
| Protocol     |     |               |          | : MSTP              |            |          |     |      |      |
| System       | ID  |               |          | : 08:00:09:12:8e:9e |            |          |     |      |      |
| Root bridge  |     | for STP       | Instance | : 2                 |            |          |     |      |      |
|              |     |               |          |                     | Root Hello | Max      | Fwd |      |      |
| Instance     | ID  | Priority      |          | Root ID             | cost       | Time Age | Dly | Root | Port |
--------------- -------- ----------------- --------- ----- --- --- ------------
| 0                 |     |       | 0   | 08:00:09:8a:14:fa | 20000 | 2 20 | 15  | 1/1/1 |     |
| ----------------- | --- | ----- | --- | ----------------- | ----- | ---- | --- | ----- | --- |
| 1                 |     |       | 0   | 08:00:09:8a:14:fa | 20000 | 2 20 | 15  | 1/1/1 |     |
| 2                 |     |       | 0   | 08:00:09:12:8e:9e | 0     | 2 20 | 15  |       |     |
| Checking Switches |     | C and | D   |                   |       |      |     |       |     |
Althoughnotillustrated,SwitchesCandDcanbecheckedinasimilarmannertotheotherswitches.
| Observe port | behavior |     | and | state |     |     |     |     |     |
| ------------ | -------- | --- | --- | ----- | --- | --- | --- | --- | --- |
Wecanobservetheportbehaviorandstateusingcommandshow spanning-tree msttoexaminethe
behaviorofportsandtheirstate.Thetopologyin Figure10,Deterministicrootbridges(logical)foreach
switchcanbeobservedshowingaloopfreeLayer2topology.
| Observing      | Switch | A             |     |      |     |     |     |     |     |
| -------------- | ------ | ------------- | --- | ---- | --- | --- | --- | --- | --- |
| Usecommandshow |        | spanning-tree |     | mst. |     |     |     |     |     |
AsseenhereSwitchAforinstance0and1,allportsareDesignatedandForwarding.Instance2has
Rootport1/1/1leadingtoSwitchBtheRootswitchforVLANs20and21,andotherportsare
ForwardingleadingtoSwitchesCandDrespectively.
Designated
| SwitchA#      | show spanning-tree        |     | mst |            |     |     |     |     |     |
| ------------- | ------------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
| ### Instance  | MST0                      |     |     |            |     |     |     |     |     |
| Vlans mapped: | 1-9,12-19,22-4094         |     |     |            |     |     |     |     |     |
| Bridge        | Address:08:00:09:8a:14:fa |     |     | priority:0 |     |     |     |     |     |
Root
| Regional | Root |     |     |     |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age(in seconds):20 txHoldCount(in pps): 6
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age(in seconds):20 Max-Hops:20
| Root     | Address:08:00:09:8a:14:fa      |        |     | Priority:0  |     |     |     |     |     |
| -------- | ------------------------------ | ------ | --- | ----------- | --- | --- | --- | --- | --- |
|          | Port:0                         |        |     | Path cost:0 |     |     |     |     |     |
| Regional | Root Address:08:00:09:8a:14:fa |        |     | Priority:0  |     |     |     |     |     |
|          | Internal                       | cost:0 |     | Rem Hops:20 |     |     |     |     |     |
132
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |

Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ---------- ---------- ---------------- ---------- ---------- ---------- -----
| 1/1/1         | Designated                | Forwarding      | 20000 128 P2P | 32900 28093 | 10 6 |
| ------------- | ------------------------- | --------------- | ------------- | ----------- | ---- |
| 1/1/2         | Designated                | Forwarding      | 20000 128 P2P | 32902 8     | 8 4  |
| 1/1/3         | Designated                | Forwarding      | 20000 128 P2P | 32898 5     | 2 3  |
| Topology      | change flag               | : True          |               |             |      |
| Number of     | topology changes          | : 9             |               |             |      |
| Last topology | change occurred           | : 55669 seconds | ago           |             |      |
| ### Instance  | MST1                      |                 |               |             |      |
| Vlans mapped: | 10,11                     |                 |               |             |      |
| Bridge        | Address:08:00:09:8a:14:fa |                 | Priority:0    |             |      |
| Root          | Address:08:00:09:8a:14:fa |                 | Priority:0    |             |      |
|               | Port:0, Cost:0,           | Rem Hops:20     |               |             |      |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- --------
| 1/1/1         | Designated                | Forwarding      | 20000 128 P2P | 32900 28093 | 10 6 |
| ------------- | ------------------------- | --------------- | ------------- | ----------- | ---- |
| 1/1/2         | Designated                | Forwarding      | 20000 128 P2P | 32902 8     | 8 4  |
| 1/1/3         | Designated                | Forwarding      | 20000 128 P2P | 32898 5     | 2 3  |
| Topology      | change flag               | : True          |               |             |      |
| Number of     | topology changes          | : 9             |               |             |      |
| Last topology | change occurred           | : 55669 seconds | ago           |             |      |
| ### Instance  | MST2                      |                 |               |             |      |
| Vlans mapped: | 20,21                     |                 |               |             |      |
| Bridge        | Address:08:00:09:8a:14:fa |                 | Priority:4096 |             |      |
| Root          | Address:08:00:09:12:8e:9e |                 | Priority:0    |             |      |
|               | Port:1/1/1,               | Cost:20000,     | Rem Hops:19   |             |      |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- --------
| 1/1/1         | Root             | Forwarding      | 20000 128 P2P | 32900 28093 | 10 6 |
| ------------- | ---------------- | --------------- | ------------- | ----------- | ---- |
| 1/1/2         | Designated       | Forwarding      | 20000 128 P2P | 32902 8     | 8 4  |
| 1/1/3         | Designated       | Forwarding      | 20000 128 P2P | 32898 5     | 2 3  |
| Topology      | change flag      | : True          |               |             |      |
| Number of     | topology changes | : 7             |               |             |      |
| Last topology | change occurred  | : 55673 seconds | ago           |             |      |
ThesamecommandcanbeusedtoobserveswitchesB,C,andD(notshownhere).
Spanningtreeprotocols(STP)|133

| MSTP use | case: | BPDU protection |     |     |     |
| -------- | ----- | --------------- | --- | --- | --- |
Varioussecuritymechanismsareinplacetoprotectspanningtrueconfigurationsfrominterferenceand
roguedevicesorunwarrantedchangestothenetwork.BPDUprotectionsecurestheactivetopologyby
preventingspoofedBPDUpacketsfromenteringthenetwork.Typically,BPDUprotectionisappliedon
edgeportsconnectedtoenduserdevicesthatdonotrunSTP.IfSTPBPDUpacketsarereceivedona
protectedport,BPDUguarddisablestheportandanalertissent.Asshownin Figure11,Roguedevice
needingBPDUguardwehavearougedeviceattemptingtoconnecttoSwitchDport1/1/8.
| Figure11 | RoguedeviceneedingBPDUguard |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- |
BPDUguardisconfiguredonswitchD.
SwitchD#
config
| interface | 1/1/8 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
no routing
vlan access 10
| spanning-tree |     | bpdu-guard |     |     |     |
| ------------- | --- | ---------- | --- | --- | --- |
exit
Usecommandshow spanning-tree summary vlan 10toobservethatport1/1/8isdisabledbecause
BPDUwasreceivedonitfromtherogueswitch.
Noticehowport1/1/8isdisableddueto"Bpdu-Error."A timeoutcanbeconfiguredtore-enablethe
port.
| SwitchD# | show spanning-tree | mst 1 |     |     |     |
| -------- | ------------------ | ----- | --- | --- | --- |
### MST1
| Vlans mapped: | 10,11                     |             |                |     |     |
| ------------- | ------------------------- | ----------- | -------------- | --- | --- |
| Bridge        | Address:08:00:09:ee:11:82 |             | Priority:32768 |     |     |
| Root          | Address:08:00:09:8a:14:fa |             | Priority:0     |     |     |
|               | Port:1/1/2,               | Cost:40000, | Rem Hops:18    |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- --------
| 1/1/2 | Root      | Forwarding | 20000 128 P2P | 9 210294  | 0 8 |
| ----- | --------- | ---------- | ------------- | --------- | --- |
| 1/1/3 | Alternate | Blocking   | 40001 128 P2P | 11 210295 | 4 4 |
134
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| 1/1/8         | Disabled         | Bpdu-Error 20000 | 128 P2P | 31 0 | 0 0 |
| ------------- | ---------------- | ---------------- | ------- | ---- | --- |
| Topology      | change flag      | : True           |         |      |     |
| Number of     | topology changes | : 7              |         |      |     |
| Last topology | change occurred  | : 350406 seconds | ago     |      |     |
Usecommandshow int 1/1/8toobservetheinterfacestate.Noticethatport1/1/8isdownas
expectedduetoBPDUerror.
| SwitchD#show | int         | 1/1/8 |     |     |     |
| ------------ | ----------- | ----- | --- | --- | --- |
| Interface    | 1/1/8 is    | down  |     |     |     |
| Admin        | state is up |       |     |     |     |
State information:
| Link | state: down  |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- |
| Link | transitions: | 0   |     |     |     |
Description:
| Hardware: | Ethernet, | MAC Address: | 08:00:09:ee:11:c4 |     |     |
| --------- | --------- | ------------ | ----------------- | --- | --- |
MTU 1500
Type --
Full-duplex
| qos trust        | none         |        |     |     |     |
| ---------------- | ------------ | ------ | --- | --- | --- |
| Speed            | 1000 Mb/s    |        |     |     |     |
| Auto-negotiation |              | is off |     |     |     |
| Flow-control:    | off          |        |     |     |     |
| Error-control:   | off          |        |     |     |     |
| MDI mode:        | none         |        |     |     |     |
| VLAN             | Mode: access |        |     |     |     |
| Access           | VLAN: 10     |        |     |     |     |
Spanningtreeprotocols(STP)|135

| MSTP use | case: Root | protection |
| -------- | ---------- | ---------- |
Rootprotectionsecurestheactivetopologybypreventingotherswitchesfromdeclaringtheirabilityto
propagatesuperiorBPDUs,containingbothbetterinformationontherootbridgeandpathcosttothe
rootbridgewhichwouldnormallyreplacethecurrentrootbridgeselection.
Asillustratedin Figure12,Rootprotection,byaddingrootguardoninterfaces1/1/2and1/1/3ofboth
coreswitches(AandB),thesetwoswitchesareprotectedinthecoreandpreventpropagationof
superiorBPDUsfromtheaccesslayer.
| Figure12 | Rootprotection |     |
| -------- | -------------- | --- |
ConfiguringSwitchesAandB:
SwitchA#
config
| interface     | 1/1/2      |     |
| ------------- | ---------- | --- |
| spanning-tree | root-guard |     |
exit
| interface     | 1/1/3      |     |
| ------------- | ---------- | --- |
| spanning-tree | root-guard |     |
exit
SwitchB#
Config
| interface     | 1/1/2      |     |
| ------------- | ---------- | --- |
| spanning-tree | root-guard |     |
| interface     | 1/1/3      |     |
| spanning-tree | root-guard |     |
exit
Toobservetheprotectionbehavior,wecan(inappropriately)makeswitchCtherootforinstance1
whichcoversVLAN10and11.
SwitchC#
config
136
| AOS-CX10.12Layer-2BridgingGuide| | 8400SwitchSeries |     |
| -------------------------------- | ---------------- | --- |

spanning-tree instance 1 priority 0 <-- Make Switch C Root for instance 1
exit
NoticehowasprotectionoccursonbothSwitchAandB,portsshowasAlternate Root-Inc(Alternate
Root-Inconsistent).ThisactionmaintainsLayer2stabilitybyprotectingtherestofthenetworkfromthe
(inaccurate)informationthatSwitchCissending“better”BPDUs.
SwitchAshowingasRootInconsistent:
| SwitchA# | show spanning-tree | mst |     |     |     |
| -------- | ------------------ | --- | --- | --- | --- |
### MST0
| Vlans mapped: | 1-9,12-19,22-4094         |     |            |     |     |
| ------------- | ------------------------- | --- | ---------- | --- | --- |
| Bridge        | Address:08:00:09:8a:14:fa |     | priority:0 |     |     |
Root
Regional Root
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age(in seconds):20 txHoldCount(in pps): 6
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age(in seconds):20 Max-Hops:20
| Root     | Address:08:00:09:8a:14:fa      |        | Priority:0  |     |     |
| -------- | ------------------------------ | ------ | ----------- | --- | --- |
|          | Port:0                         |        | Path cost:0 |     |     |
| Regional | Root Address:08:00:09:8a:14:fa |        | Priority:0  |     |     |
|          | Internal                       | cost:0 | Rem Hops:20 |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ---------- ---------- ---------------- ---------- ---------- ---------- -----
1/1/1 Designated Forwarding 20000 128 P2P 217571 217573 11 14
| 1/1/2         | Designated       | Forwarding    | 20000 128 P2P | 217566 565 | 15 8 |
| ------------- | ---------------- | ------------- | ------------- | ---------- | ---- |
| 1/1/3         | Designated       | Forwarding    | 20000 128 P2P | 217573 27  | 13 7 |
| Topology      | change flag      | : True        |               |            |      |
| Number of     | topology changes | : 15          |               |            |      |
| Last topology | change occurred  | : 908 seconds | ago           |            |      |
### MST1
| Vlans mapped: | 10,11                     |                     |            |     |     |
| ------------- | ------------------------- | ------------------- | ---------- | --- | --- |
| Bridge        | Address:08:00:09:8a:14:fa |                     | Priority:0 |     |     |
| Root          | Address:08:00:09:8a:14:fa |                     | Priority:0 |     |     |
|               | Port:0,                   | Cost:0, Rem Hops:20 |            |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- --------
1/1/1 Designated Forwarding 20000 128 P2P 217571 217573 11 14
| 1/1/2         | Alternate        | Root-Inc      | 20000 128 P2P | 217566 565 | 15 8 |
| ------------- | ---------------- | ------------- | ------------- | ---------- | ---- |
| 1/1/3         | Designated       | Forwarding    | 20000 128 P2P | 217573 27  | 13 7 |
| Topology      | change flag      | : True        |               |            |      |
| Number of     | topology changes | : 18          |               |            |      |
| Last topology | change occurred  | : 908 seconds | ago           |            |      |
### MST2
| Vlans mapped: | 20,21                     |             |               |     |     |
| ------------- | ------------------------- | ----------- | ------------- | --- | --- |
| Bridge        | Address:08:00:09:8a:14:fa |             | Priority:4096 |     |     |
| Root          | Address:08:00:09:12:8e:9e |             | Priority:0    |     |     |
|               | Port:1/1/1,               | Cost:20000, | Rem Hops:19   |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- --------
| 1/1/1 | Root       | Forwarding | 20000 128 P2P | 217571 217573 | 11 14 |
| ----- | ---------- | ---------- | ------------- | ------------- | ----- |
| 1/1/2 | Designated | Forwarding | 20000 128 P2P | 217566 565    | 15 8  |
Spanningtreeprotocols(STP)|137

| 1/1/3         | Designated       | Forwarding    | 20000 128 P2P | 217573 27 | 13 7 |
| ------------- | ---------------- | ------------- | ------------- | --------- | ---- |
| Topology      | change flag      | : True        |               |           |      |
| Number of     | topology changes | : 13          |               |           |      |
| Last topology | change occurred  | : 911 seconds | ago           |           |      |
SwitchBshowingasRootInconsistent:
| SwitchB# | show spanning-tree | mst0 |     |     |     |
| -------- | ------------------ | ---- | --- | --- | --- |
### MST0
| Vlans mapped: | 1-9,12-19,22-4094         |     |                |     |     |
| ------------- | ------------------------- | --- | -------------- | --- | --- |
| Bridge        | Address:08:00:09:12:8e:9e |     | priority:32768 |     |     |
Operational Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age(in seconds):20 txHoldCount(in pps): 6
Configured Hello time(in seconds): 2 Forward delay(in seconds):15 Max-age(in seconds):20 Max-Hops:20
| Root     | Address:08:00:09:8a:14:fa      |            | Priority:0  |     |     |
| -------- | ------------------------------ | ---------- | ----------- | --- | --- |
|          | Port:1/1/1                     |            | Path cost:0 |     |     |
| Regional | Root Address:08:00:09:8a:14:fa |            | Priority:0  |     |     |
|          | Internal                       | cost:20000 | Rem Hops:19 |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ---------- ---------- ---------------- ---------- ---------- ---------- -----
| 1/1/1         | Root             | Forwarding | 20000 128 P2P | 217900 217897 | 14 11 |
| ------------- | ---------------- | ---------- | ------------- | ------------- | ----- |
| 1/1/2         | Designated       | Forwarding | 20000 128 P2P | 217902 25     | 13 1  |
| 1/1/3         | Designated       | Forwarding | 20000 128 P2P | 217900 895    | 12 2  |
| Topology      | change flag      | : True     |               |               |       |
| Number of     | topology changes | : 16       |               |               |       |
| Last topology | change occurred  | : 1560     | seconds ago   |               |       |
### MST1
| Vlans mapped: | 10,11                     |             |               |     |     |
| ------------- | ------------------------- | ----------- | ------------- | --- | --- |
| Bridge        | Address:08:00:09:12:8e:9e |             | Priority:4096 |     |     |
| Root          | Address:08:00:09:8a:14:fa |             | Priority:0    |     |     |
|               | Port:1/1/1,               | Cost:20000, | Rem Hops:19   |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- --------
| 1/1/1         | Root             | Forwarding | 20000 128 P2P | 217900 217897 | 14 11 |
| ------------- | ---------------- | ---------- | ------------- | ------------- | ----- |
| 1/1/2         | Designated       | Forwarding | 20000 128 P2P | 217902 25     | 13 1  |
| 1/1/3         | Alternate        | Root-Inc   | 20000 128 P2P | 217900 895    | 12 2  |
| Topology      | change flag      | : True     |               |               |       |
| Number of     | topology changes | : 19       |               |               |       |
| Last topology | change occurred  | : 1560     | seconds ago   |               |       |
#### MST2
| Vlans mapped: | 20,21                     |                     |            |     |     |
| ------------- | ------------------------- | ------------------- | ---------- | --- | --- |
| Bridge        | Address:08:00:09:12:8e:9e |                     | Priority:0 |     |     |
| Root          | Address:08:00:09:12:8e:9e |                     | Priority:0 |     |     |
|               | Port:0,                   | Cost:0, Rem Hops:20 |            |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- --------
1/1/1 Designated Forwarding 20000 128 P2P 217900 217897 14 11
| 1/1/2    | Designated  | Forwarding | 20000 128 P2P | 217902 25  | 13 1 |
| -------- | ----------- | ---------- | ------------- | ---------- | ---- |
| 1/1/3    | Designated  | Forwarding | 20000 128 P2P | 217900 895 | 12 2 |
| Topology | change flag | : True     |               |            |      |
138
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| Number of     | topology changes | : 13           |     |     |
| ------------- | ---------------- | -------------- | --- | --- |
| Last topology | change occurred  | : 1561 seconds | ago |     |
Dependingonwhentheshowcommandisexecuted,itmayfirstshowtheprotectedportasDesignated
| BlockingbeforeitshowsitasAlternate |       |          | Root-Inc. |            |
| ---------------------------------- | ----- | -------- | --------- | ---------- |
| MSTP use                           | case: | Spanning | tree on   | edge ports |
Whenusingspanningtreeandtakingintoconsiderationtheedgeofthenetworkportsthatprovide
connectivitytoendpoints,thenetworkshouldnottypicallyparticipateinspanningtree.Considerthis
topologythatshowsanendpointconnectedtoport1/1/8onSwitchD:
| Figure13 | Spanningtreeonedgeports |     |     |     |
| -------- | ----------------------- | --- | --- | --- |
Endpointsthatconnecttoportsthatdoparticipateinspanningtree(STP)mayexperienceDHCP
assignmenttimeoutsorIPaddressassignmentdelaysplusextendedclientonboardingtimeand
authenticationissues.TheseproblemsoccurbecausetheportparticipatesinthefullSTPprocess.To
avoidsuchissuesconsidersettingtheportasaspanningtreeadministrativeedgeportbyusing
commandspanning-tree port-type admin-edge.Thiscommandremovestheportparticipationfrom
STPinteractionswhenonboardingdevices,enablingquickeronboarding.
Edgeportsstillneedtobeprotectedfrompossiblespanningtreeattacks.ForexampleBPDUguardcanbeused.
SeeMSTPusecase:BPDUprotection.
Beforeconfiguringaportasspanningtreeadministrativeedge,theportconfigurationlookslikethis:
| interface | 1/1/8 |     |     |     |
| --------- | ----- | --- | --- | --- |
no shutdown
vlan access 10
| spanning-tree |     | bpdu-guard |     |     |
| ------------- | --- | ---------- | --- | --- |
Spanningtreeprotocols(STP)|139

TheportStateisForwardingandtheTypeisP2P(PointtoPoint)bydefault.
| switch# show | spanning-tree | mst 1 |     |     |     |
| ------------ | ------------- | ----- | --- | --- | --- |
### MST1
| Vlans mapped: | 10,11                     |             |                |     |     |
| ------------- | ------------------------- | ----------- | -------------- | --- | --- |
| Bridge        | Address:38:21:c7:dc:50:60 |             | Priority:32768 |     |     |
| Root          | Address:88:3a:30:9a:39:00 |             | Priority:0     |     |     |
|               | Port:1/1/2,               | Cost:20000, | Rem Hops:19    |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- ----------
| 1/1/1         | Alternate        | Blocking      | 20000 128 P2P | 463 467 | 4 13 |
| ------------- | ---------------- | ------------- | ------------- | ------- | ---- |
| 1/1/2         | Root             | Forwarding    | 20000 128 P2P | 466 467 | 13 0 |
| 1/1/3         | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/4         | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/5         | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/6         | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/7         | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/8         | Designated       | Forwarding    | 20000 128 P2P | 2 0     | 0 0  |
| 1/1/9         | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/10        | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/11        | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/12        | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/13        | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/14        | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/15        | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| 1/1/16        | Disabled         | Down          | 20000 128 P2P | 0 0     | 0 0  |
| Topology      | change flag      | : True        |               |         |      |
| Number of     | topology changes | : 2           |               |         |      |
| Last topology | change occurred  | : 915 seconds | ago           |         |      |
Configuretheportasadminedgeasfollowswithcommandspanning-tree port-type admin-edge:
| interface | 1/1/8 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
| vlan          | access | 10         |            |     |     |
| ------------- | ------ | ---------- | ---------- | --- | --- |
| spanning-tree |        | bpdu-guard |            |     |     |
| spanning-tree |        | port-type  | admin-edge |     |     |
exit
NoticehowthattheportStateisnowForwardingandtheTypeisP2P Edgemeaningthattheportwill
gointotheforwardingstateandbypassthestandardSTPlisteningandlearningstates.
| switch# show | spanning-tree | mst 1 |     |     |     |
| ------------ | ------------- | ----- | --- | --- | --- |
### MST1
| Vlans mapped: | 10,11                     |             |                |     |     |
| ------------- | ------------------------- | ----------- | -------------- | --- | --- |
| Bridge        | Address:38:21:c7:dc:50:60 |             | Priority:32768 |     |     |
| Root          | Address:88:3a:30:9a:39:00 |             | Priority:0     |     |     |
|               | Port:1/1/2,               | Cost:20000, | Rem Hops:19    |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------------- -------------- ---------- ------- ---------- ---------------- ---------- ---------- ---------- ----------
| 1/1/1 | Alternate | Blocking   | 20000 128 P2P | 593 597 | 4 13 |
| ----- | --------- | ---------- | ------------- | ------- | ---- |
| 1/1/2 | Root      | Forwarding | 20000 128 P2P | 596 597 | 13 0 |
| 1/1/3 | Disabled  | Down       | 20000 128 P2P | 0 0     | 0 0  |
140
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| 1/1/4         | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| ------------- | ---------------- | -------------- | --------- | ------------ | --- | --- |
| 1/1/5         | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/6         | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/7         | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/8         | Designated       | Forwarding     | 20000 128 | P2P Edge 132 | 0 0 | 0   |
| 1/1/9         | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/10        | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/11        | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/12        | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/13        | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/14        | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/15        | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| 1/1/16        | Disabled         | Down           | 20000 128 | P2P 0        | 0 0 | 0   |
| Topology      | change flag      | : True         |           |              |     |     |
| Number of     | topology changes | : 2            |           |              |     |     |
| Last topology | change occurred  | : 1174 seconds | ago       |              |     |     |
Spanningtreeprotocols(STP)|141

MSTP commands
| clear spanning-tree |            | statistics |     |     |
| ------------------- | ---------- | ---------- | --- | --- |
| clear spanning-tree | statistics |            |     |     |
Description
ClearsthespanningtreeBPDUstatistics.
Example
ClearingthespanningtreeBPDUstatistics:
| switch(config)#     | clear   | spanning-tree | statistics   |     |
| ------------------- | ------- | ------------- | ------------ | --- |
| Command History     |         |               |              |     |
| Release             |         |               | Modification |     |
| 10.07orearlier      |         |               | --           |     |
| Command Information |         |               |              |     |
| Platforms           | Command | context       | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
show spanning-tree
| show spanning-tree | [vsx-peer] |     |     |     |
| ------------------ | ---------- | --- | --- | --- |
Description
Showspriority,address,Hello-time,Max-age,andForward-delayforbridgeandrootnode.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingspanningtreestandardinformation:
| switch#  | show spanning-tree |           |           |      |
| -------- | ------------------ | --------- | --------- | ---- |
| Spanning | tree status        | : Enabled | Protocol: | MSTP |
MST0
| Root ID     |     |                     |     |     |
| ----------- | --- | ------------------- | --- | --- |
| Priority    |     | : 32768, Root       |     |     |
| MAC-Address |     | : 48:0F:CF:AF:04:76 |     |     |
142
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

|      | Hello       | time(in  | seconds):2          | Max Age(in | seconds):20 |      |         |         |
| ---- | ----------- | -------- | ------------------- | ---------- | ----------- | ---- | ------- | ------- |
|      | Forward     | Delay(in | seconds):15         |            |             |      |         |         |
|      | Bridge      | ID       |                     |            |             |      |         |         |
|      | Priority    |          | : 32768             |            |             |      |         |         |
|      | MAC-Address |          | : 48:0F:CF:AF:04:76 |            |             |      |         |         |
|      | Hello       | time(in  | seconds):2          | Max Age(in | seconds):20 |      |         |         |
|      | Forward     | Delay(in | seconds):15         |            |             |      |         |         |
| PORT |             | ROLE     | STATE               | COST       | PRIORITY    | TYPE | BPDU-Tx | BPDU-Rx |
|      | TCN-Tx      | TCN-Rx   |                     |            |             |      |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| --             | ----------  | ---------- |            |                                  |     |          |     |     |
| -------------- | ----------- | ---------- | ---------- | -------------------------------- | --- | -------- | --- | --- |
| 1/1/1          |             | Designated | Forwarding | 20000                            | 128 | P2P Edge | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/2          |             | Designated | Forwarding | 20000                            | 128 | P2P      | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/3          |             | Designated | Forwarding | 20000                            | 128 | Shr      | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/4          |             | Designated | Forwarding | 20000                            | 128 | Shr Edge | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/5          |             | Alternate  | Loop-Inc   | 20000                            | 128 | Shr Edge | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/6          |             | Alternate  | Root-Inc   | 20000                            | 128 | Shr Edge | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/7          |             | Root       | Forwarding | 2000                             | 128 | P2P      | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/8          |             | Alternate  | Blocking   | 20000                            | 128 | P2P      | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| 1/1/9          |             | Disabled   | Down       | 20000                            | 128 | P2P      | 100 | 60  |
|                | 20          | 10         |            |                                  |     |          |     |     |
| Number         | of          | topology   | changes    | : 4                              |     |          |     |     |
| Last           | topology    | change     | occurred   | : 516 seconds                    | ago |          |     |     |
| Command        | History     |            |            |                                  |     |          |     |     |
| Release        |             |            |            | Modification                     |     |          |     |     |
| 10.09          |             |            |            | AnewstateDownisaddedintheoutput. |     |          |     |     |
| 10.07orearlier |             |            |            | --                               |     |          |     |     |
| Command        | Information |            |            |                                  |     |          |     |     |
| Platforms      |             | Command    | context    | Authority                        |     |          |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | spanning-tree |     | detail            |     |     |     |     |     |
| ---- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- |
| show | spanning-tree |     | detail [vsx-peer] |     |     |     |     |     |
Description
ShowsspanningtreedetailincludingCISTandcorrespondingportinformation.
Spanningtreeprotocols(STP)|143

| Parameter |     |     |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
Showingspanningtreedetailedinformation:
| switch#  | show | spanning-tree |     | detail |         |           |     |      |     |     |     |
| -------- | ---- | ------------- | --- | ------ | ------- | --------- | --- | ---- | --- | --- | --- |
| Spanning | tree | status        |     | :      | Enabled | Protocol: |     | MSTP |     |     |     |
MST0
Root ID
| Priority    |          |        | : 32768,            | Root |      |        |             |          |      |         |         |
| ----------- | -------- | ------ | ------------------- | ---- | ---- | ------ | ----------- | -------- | ---- | ------- | ------- |
| MAC-Address |          |        | : 48:0F:CF:AF:04:76 |      |      |        |             |          |      |         |         |
| Hello       | time(in  |        | seconds):2          |      | Max  | Age(in | seconds):20 |          |      |         |         |
| Forward     | Delay(in |        | seconds):15         |      |      |        |             |          |      |         |         |
| Bridge      | ID       |        |                     |      |      |        |             |          |      |         |         |
| Priority    |          |        | : 32768             |      |      |        |             |          |      |         |         |
| MAC-Address |          |        | : 48:0F:CF:AF:04:76 |      |      |        |             |          |      |         |         |
| Hello       | time(in  |        | seconds):2          |      | Max  | Age(in | seconds):20 |          |      |         |         |
| Forward     | Delay(in |        | seconds):15         |      |      |        |             |          |      |         |         |
| PORT        | ROLE     |        | STATE               |      | COST |        |             | PRIORITY | TYPE | BPDU-Tx | BPDU-Rx |
| TCN-Tx      |          | TCN-Rx |                     |      |      |        |             |          |      |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- |             | ---------- |            |     |        |         |     |     |     |          |     |
| ------------- | ----------- | ---------- | ---------- | --- | ------ | ------- | --- | --- | --- | -------- | --- |
| 1/1/1         | Designated  |            | Forwarding |     | 20000  |         |     | 128 | P2P | Edge 100 | 60  |
| 20            |             | 10         |            |     |        |         |     |     |     |          |     |
| 1/1/2         | Designated  |            | Forwarding |     | 20000  |         |     | 128 | P2P | 100      | 60  |
| 20            |             | 10         |            |     |        |         |     |     |     |          |     |
| 1/1/3         | Designated  |            | Forwarding |     | 20000  |         |     | 128 | Shr | 100      | 60  |
| 20            |             | 10         |            |     |        |         |     |     |     |          |     |
| 1/1/4         | Designated  |            | Forwarding |     | 20000  |         |     | 128 | Shr | Edge 100 | 60  |
| 20            |             | 10         |            |     |        |         |     |     |     |          |     |
| 1/1/5         | Alternate   |            | Loop-Inc   |     | 20000  |         |     | 128 | Shr | Edge 100 | 60  |
| 20            |             | 10         |            |     |        |         |     |     |     |          |     |
| 1/1/6         | Alternate   |            | Root-Inc   |     | 20000  |         |     | 128 | Shr | Edge 100 | 60  |
| 20            |             | 10         |            |     |        |         |     |     |     |          |     |
| 1/1/7         | Disabled    |            | Down       |     | 20000  |         |     | 128 | P2P | 100      | 60  |
| 20            |             | 10         |            |     |        |         |     |     |     |          |     |
| Topology      | change      | flag       |            |     | : True |         |     |     |     |          |     |
| Number        | of topology |            | changes    |     | : 4    |         |     |     |     |          |     |
| Last topology |             | change     | occurred   |     | : 516  | seconds |     | ago |     |          |     |
| Hello expiry  |             |            |            |     | : 1    | second  |     |     |     |          |     |
| Forward       | delay       | expiry     |            |     | : 18   | seconds |     |     |     |          |     |
Port 1/1/1
| Designated | root | has | priority |     |     |     | :   | 32768 |     | Address: |     |
| ---------- | ---- | --- | -------- | --- | --- | --- | --- | ----- | --- | -------- | --- |
48:0F:CF:AF:04:76
| Designated | bridge |     | has priority |     |     |     | :   | 32768 |     | Address: |     |
| ---------- | ------ | --- | ------------ | --- | --- | --- | --- | ----- | --- | -------- | --- |
48:0F:CF:AF:04:76
| Designated     | port           |     |     |            |     |       | :   | 1/1/1 |     |     |     |
| -------------- | -------------- | --- | --- | ---------- | --- | ----- | --- | ----- | --- | --- | --- |
| Number         | of transitions |     | to  | forwarding |     | state | :   | 3     |     |     |     |
| BPDUs sent     |                |     |     |            |     |       | :   | 347   |     |     |     |
| BPDUs received |                |     |     |            |     |       | :   | 9     |     |     |     |
144
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| TCN_Tx:    | 20, TCN_Rx: | 10       |     |         |          |
| ---------- | ----------- | -------- | --- | ------- | -------- |
| Port 1/1/2 |             |          |     |         |          |
| Designated | root has    | priority |     | : 32768 | Address: |
48:0F:CF:AF:04:76
| Designated | bridge | has priority |     | : 32768 | Address: |
| ---------- | ------ | ------------ | --- | ------- | -------- |
48:0F:CF:AF:04:76
| Designated     | port           |               |       | : 1/1/2 |          |
| -------------- | -------------- | ------------- | ----- | ------- | -------- |
| Number         | of transitions | to forwarding | state | : 3     |          |
| BPDUs sent     |                |               |       | : 350   |          |
| BPDUs received |                |               |       | : 11    |          |
| TCN_Tx:        | 20, TCN_Rx:    | 10            |       |         |          |
| Port lag1      | ID 321         |               |       |         |          |
| Designated     | root has       | priority      |       | : 32768 | Address: |
48:0F:CF:AF:04:76
| Designated | bridge | has priority |     | : 32768 | Address: |
| ---------- | ------ | ------------ | --- | ------- | -------- |
48:0F:CF:AF:04:76
| Designated     | port id        |               |                                  | : 321    |     |
| -------------- | -------------- | ------------- | -------------------------------- | -------- | --- |
| Multi-Chassis  | role           |               |                                  | : active |     |
| Number         | of transitions | to forwarding | state                            | : 3      |     |
| BPDUs sent     |                |               |                                  | : 340    |     |
| BPDUs received |                |               |                                  | : 5      |     |
| TCN_Tx:        | 20, TCN_Rx:    | 10            |                                  |          |     |
| Command        | History        |               |                                  |          |     |
| Release        |                |               | Modification                     |          |     |
| 10.09          |                |               | AnewstateDownisaddedintheoutput. |          |     |
| 10.07orearlier |                |               | --                               |          |     |
| Command        | Information    |               |                                  |          |     |
| Platforms      | Command        | context       | Authority                        |          |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show spanning-tree |                    | inconsistent-ports |           |                |     |
| ------------------ | ------------------ | ------------------ | --------- | -------------- | --- |
| show spanning-tree | inconsistent-ports |                    | [instance | <INSTANCE-ID>] |     |
Description
ShowsportsblockedbySTPprotectionfunctionssuchasRootguard,Loopguard,BPDUguard,and
RPVSTguardinadditiontoMSTIinformation.
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
<INSTANCE-ID>
SpecifiestheMSTPinstanceID.Range:0to64.
Example
Showingspanningtreeinconsistentports:
Spanningtreeprotocols(STP)|145

| switch#      | show spanning-tree | inconsistent-ports |       |     |
| ------------ | ------------------ | ------------------ | ----- | --- |
| Instance     | ID Blocked         | Port Reason        |       |     |
| ------------ | --------------     | ------------       |       |     |
| 0            | 1/1/13             | BPDU               | Guard |     |
Showinginconsistentportinformationforinstances1-4:
| switch#             | show spanning-tree | inconsistent-ports |              | instance 1-4 |
| ------------------- | ------------------ | ------------------ | ------------ | ------------ |
| Instance            | ID Blocked         | Port Reason        |              |              |
| ------------        | --------------     | ------------       |              |              |
| 1                   | 1/1/3              | Root               | Guard        |              |
| 2                   | 1/1/7              | BPDU               | Guard        |              |
| 3                   | 1/1/9              | Loop               | Guard        |              |
| 4                   | 1/1/37             | RPVST              | Guard        |              |
| Command History     |                    |                    |              |              |
| Release             |                    |                    | Modification |              |
| 10.07orearlier      |                    |                    | --           |              |
| Command Information |                    |                    |              |              |
| Platforms           | Command            | context            | Authority    |              |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show spanning-tree |     | mst        |     |     |
| ------------------ | --- | ---------- | --- | --- |
| show spanning-tree | mst | [vsx-peer] |     |     |
Description
ShowsMSTPconfigurationandstatusinformationforeachinstance.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingMSTPconfigurationandstatusinformation:
| switch# | show spanning-tree | mst |     |     |
| ------- | ------------------ | --- | --- | --- |
#### MST0
| Vlans mapped   | : 2,4-4094          |     |     |     |
| -------------- | ------------------- | --- | --- | --- |
| Bridge Address | : 48:0F:CF:AF:04:76 |     |     |     |
| Priority       | : 32768             |     |     |     |
Root
146
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| Regional    | Root |          |       |                     |          |      |             |         |            |
| ----------- | ---- | -------- | ----- | ------------------- | -------- | ---- | ----------- | ------- | ---------- |
| Operational |      | Hello    | time  | : 2 seconds         |          |      | Forward     | delay:  | 15 seconds |
|             |      | Max-age  |       | : 20 seconds        |          |      | TxHoldCount |         | : 6 pps    |
| Configured  |      | Hello    | time  | : 2 seconds         |          |      | Forward     | delay:  | 15 seconds |
|             |      | Max-age  |       | : 20 seconds        |          |      | Max-Hops    |         | : 20       |
| Root        |      | Address  |       | : 48:0F:CF:AF:04:76 |          |      | Priority    |         | : 32768    |
|             |      | Port     |       | : 0                 |          |      | Path        | cost    | : 0        |
| Regional    | Root | Address  |       | : 48:0F:CF:AF:04:76 |          |      | Priority    |         | : 32768    |
|             |      | Internal | cost: | 0                   |          |      | Rem         | Hops    | : 20       |
| PORT        | ROLE |          | STATE | COST                | PRIORITY | TYPE |             | BPDU-Tx | BPDU-Rx    |
| TCN-Tx      |      | TCN-Rx   |       |                     |          |      |             |         |            |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- |             | ---------- |            |               |     |     |      |     |     |
| ------------- | ----------- | ---------- | ---------- | ------------- | --- | --- | ---- | --- | --- |
| 1/1/1         | Designated  |            | Forwarding | 20000         | 128 | P2P | Edge | 100 | 60  |
| 20            |             | 10         |            |               |     |     |      |     |     |
| 1/1/2         | Designated  |            | Forwarding | 20000         | 128 | P2P |      | 100 | 60  |
| 20            |             | 10         |            |               |     |     |      |     |     |
| 1/1/3         | Designated  |            | Forwarding | 20000         | 128 | Shr |      | 100 | 60  |
| 20            |             | 10         |            |               |     |     |      |     |     |
| 1/1/4         | Designated  |            | Forwarding | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |               |     |     |      |     |     |
| 1/1/5         | Alternate   |            | Loop-Inc   | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |               |     |     |      |     |     |
| 1/1/6         | Alternate   |            | Root-Inc   | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |               |     |     |      |     |     |
| 1/1/7         | Disabled    |            | Down       | 20000         | 128 | P2P |      | 100 | 60  |
| 20            |             | 10         |            |               |     |     |      |     |     |
| Topology      | change      | flag       |            | : True        |     |     |      |     |     |
| Number        | of topology |            | changes    | : 4           |     |     |      |     |     |
| Last topology |             | change     | occurred   | : 516 seconds | ago |     |      |     |     |
#### MST1
| Vlans mapped: |      | 1       |       |                   |          |           |     |         |         |
| ------------- | ---- | ------- | ----- | ----------------- | -------- | --------- | --- | ------- | ------- |
| Bridge        |      | Address | :     | 48:0F:CF:AF:04:76 |          | Priority: |     | 32768   |         |
| Root          |      | Address | :     | 48:0F:CF:AF:04:76 |          | Priority: |     | 32768   |         |
|               |      | Port    | :     | 0                 |          | Cost      |     | : 0     |         |
|               |      | Rem     | Hops: | 20                |          |           |     |         |         |
| PORT          | ROLE |         | STATE | COST              | PRIORITY | TYPE      |     | BPDU-Tx | BPDU-Rx |
| TCN-Tx        |      | TCN-Rx  |       |                   |          |           |     |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- |             | ---------- |            |        |     |     |      |     |     |
| ------------- | ----------- | ---------- | ---------- | ------ | --- | --- | ---- | --- | --- |
| 1/1/1         | Designated  |            | Forwarding | 20000  | 128 | P2P | Edge | 100 | 60  |
| 20            |             | 10         |            |        |     |     |      |     |     |
| 1/1/2         | Designated  |            | Forwarding | 20000  | 128 | P2P |      | 100 | 60  |
| 20            |             | 10         |            |        |     |     |      |     |     |
| 1/1/3         | Designated  |            | Forwarding | 20000  | 128 | Shr |      | 100 | 60  |
| 20            |             | 10         |            |        |     |     |      |     |     |
| 1/1/4         | Designated  |            | Forwarding | 20000  | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |        |     |     |      |     |     |
| 1/1/5         | Alternate   |            | Loop-Inc   | 20000  | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |        |     |     |      |     |     |
| 1/1/6         | Alternate   |            | Root-Inc   | 20000  | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |        |     |     |      |     |     |
| 1/1/7         | Disabled    |            | Down       | 20000  | 128 | P2P |      | 100 | 60  |
| 20            |             | 10         |            |        |     |     |      |     |     |
| Topology      | change      | flag       |            | : True |     |     |      |     |     |
| Number        | of topology |            | changes    | : 4    |     |     |      |     |     |
Spanningtreeprotocols(STP)|147

| Last topology |      | change  | occurred |                     | : 516 seconds | ago      |           |         |         |
| ------------- | ---- | ------- | -------- | ------------------- | ------------- | -------- | --------- | ------- | ------- |
| #### MST2     |      |         |          |                     |               |          |           |         |         |
| Vlans mapped: |      | 3       |          |                     |               |          |           |         |         |
| Bridge        |      | Address |          | : 48:0F:CF:AF:04:76 |               |          | Priority: | 32768   |         |
| Root          |      | Address |          | : 48:0F:CF:AF:04:76 |               |          | Priority: | 32768   |         |
|               |      | Port    |          | : 0                 |               |          | Cost      | : 0     |         |
|               |      | Rem     | Hops:    | 20                  |               |          |           |         |         |
| PORT          | ROLE |         | STATE    |                     | COST          | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        |      | TCN-Rx  |          |                     |               |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ----------  |             | ---------- |            |     |                                  |     |          |     |     |
| -------------- | ----------- | ---------- | ---------- | --- | -------------------------------- | --- | -------- | --- | --- |
| 1/1/1          | Designated  |            | Forwarding |     | 20000                            | 128 | P2P Edge | 100 | 60  |
| 20             |             | 10         |            |     |                                  |     |          |     |     |
| 1/1/2          | Designated  |            | Forwarding |     | 20000                            | 128 | P2P      | 100 | 60  |
| 20             |             | 10         |            |     |                                  |     |          |     |     |
| 1/1/3          | Designated  |            | Forwarding |     | 20000                            | 128 | Shr      | 100 | 60  |
| 20             |             | 10         |            |     |                                  |     |          |     |     |
| 1/1/4          | Designated  |            | Forwarding |     | 20000                            | 128 | Shr Edge | 100 | 60  |
| 20             |             | 10         |            |     |                                  |     |          |     |     |
| 1/1/5          | Alternate   |            | Loop-Inc   |     | 20000                            | 128 | Shr Edge | 100 | 60  |
| 20             |             | 10         |            |     |                                  |     |          |     |     |
| 1/1/6          | Alternate   |            | Root-Inc   |     | 20000                            | 128 | Shr Edge | 100 | 60  |
| 20             |             | 10         |            |     |                                  |     |          |     |     |
| Topology       | change      | flag       |            |     | : True                           |     |          |     |     |
| Number         | of topology |            | changes    |     | : 4                              |     |          |     |     |
| Last topology  |             | change     | occurred   |     | : 516 seconds                    | ago |          |     |     |
| Command        | History     |            |            |     |                                  |     |          |     |     |
| Release        |             |            |            |     | Modification                     |     |          |     |     |
| 10.09          |             |            |            |     | AnewstateDownisaddedintheoutput. |     |          |     |     |
| 10.07orearlier |             |            |            |     | --                               |     |          |     |     |
| Command        | Information |            |            |     |                                  |     |          |     |     |
| Platforms      |             | Command    | context    |     | Authority                        |     |          |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |     |            |     | mst-config |     |     |     |     |     |
| ------------------ | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
| show spanning-tree |     | mst-config |     | [vsx-peer] |     |     |     |     |     |
Description
ShowsMSTPinstanceandcorrespondingVLANinformation.
148
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |

| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingconfigurationinformationforMSTinstancesandcorrespondingVLANs:
|                | switch#           | show spanning-tree                 |             | mst-config                         |              |
| -------------- | ----------------- | ---------------------------------- | ----------- | ---------------------------------- | ------------ |
|                | MST configuration |                                    | information |                                    |              |
|                | MST config        | ID                                 |             | : reg                              |              |
|                | MST config        | revision                           |             | : 1                                |              |
|                | MST config        | digest                             |             | : 2D2BC9A32097B463C48EE1817673FA2D |              |
|                | Number            | of instances                       |             | : 2                                |              |
|                | Instance          | ID Member                          |             | VLANs                              |              |
|                | ---------------   | ---------------------------------- |             |                                    |              |
|                | 0                 | 2,4-4094                           |             |                                    |              |
|                | 1                 | 1                                  |             |                                    |              |
|                | 2                 | 3                                  |             |                                    |              |
| Command        | History           |                                    |             |                                    |              |
| Release        |                   |                                    |             |                                    | Modification |
| 10.07orearlier |                   |                                    |             |                                    | --           |
| Command        | Information       |                                    |             |                                    |              |
| Platforms      |                   | Command                            | context     |                                    | Authority    |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show | spanning-tree |     |        | mst detail |     |
| ---- | ------------- | --- | ------ | ---------- | --- |
| show | spanning-tree | mst | detail | [vsx-peer] |     |
Description
ShowsdetailedinformationforallMSTinstances.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
ShowingdetailedinformationforallMSTinstances:
Spanningtreeprotocols(STP)|149

| switch# | show | spanning-tree |     | mst | detail |     |     |     |     |     |
| ------- | ---- | ------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
#### MST0
| Vlans mapped: |     | 2,4-4094 |     |                   |     |     |           |     |       |     |
| ------------- | --- | -------- | --- | ----------------- | --- | --- | --------- | --- | ----- | --- |
| Bridge        |     | Address: |     | 48:0F:CF:AF:04:76 |     |     | Priority: |     | 32768 |     |
Root
| Regional    | Root |          |       |       |                   |          |      |             |         |            |
| ----------- | ---- | -------- | ----- | ----- | ----------------- | -------- | ---- | ----------- | ------- | ---------- |
| Operational |      | Hello    | time  | :     | 2 seconds         |          |      | Forward     | delay:  | 15 seconds |
|             |      | Max-age  |       | :     | 20 seconds        |          |      | TxHoldCount |         | : 6 pps    |
| Configured  |      | Hello    | time  | :     | 2 seconds         |          |      | Forward     | delay:  | 15 seconds |
|             |      | Max-age  |       | :     | 20 seconds        |          |      | Max-Hops    |         | : 20       |
| Root        |      | Address  |       | :     | 48:0F:CF:AF:04:76 |          |      | Priority    |         | : 32768    |
|             |      | Port     |       | :     | 0                 |          |      | Path        | cost    | : 0        |
| Regional    | Root | Address  |       | :     | 48:0F:CF:AF:04:76 |          |      | Priority    |         | : 32768    |
|             |      | Internal |       | cost: | 0                 |          |      | Rem         | Hops    | : 20       |
| PORT        | ROLE |          | STATE |       | COST              | PRIORITY | TYPE |             | BPDU-Tx | BPDU-Rx    |
| TCN-Tx      |      | TCN-Rx   |       |       |                   |          |      |             |         |            |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- |             | ---------- |            |     |               |     |     |      |     |     |
| ------------- | ----------- | ---------- | ---------- | --- | ------------- | --- | --- | ---- | --- | --- |
| 1/1/1         | Designated  |            | Forwarding |     | 20000         | 128 | P2P | Edge | 100 | 60  |
| 20            |             | 10         |            |     |               |     |     |      |     |     |
| 1/1/2         | Designated  |            | Forwarding |     | 20000         | 128 | P2P |      | 100 | 60  |
| 20            |             | 10         |            |     |               |     |     |      |     |     |
| 1/1/3         | Designated  |            | Forwarding |     | 20000         | 128 | Shr |      | 100 | 60  |
| 20            |             | 10         |            |     |               |     |     |      |     |     |
| 1/1/4         | Designated  |            | Forwarding |     | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |     |               |     |     |      |     |     |
| 1/1/5         | Alternate   |            | Loop-Inc   |     | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |     |               |     |     |      |     |     |
| 1/1/6         | Alternate   |            | Root-Inc   |     | 20000         | 128 | Shr | Edge | 100 | 60  |
| 20            |             | 10         |            |     |               |     |     |      |     |     |
| 1/1/7         | Disabled    |            | Down       |     | 20000         | 128 | P2P |      | 100 | 60  |
| 20            |             | 10         |            |     |               |     |     |      |     |     |
| Topology      | change      | flag       |            |     | : True        |     |     |      |     |     |
| Number        | of topology |            | changes    |     | : 4           |     |     |      |     |     |
| Last topology |             | change     | occurred   |     | : 516 seconds | ago |     |      |     |     |
Port 1/1/1
| Designated     | root        | address |         |         | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| -------------- | ----------- | ------- | ------- | ------- | ------------------- | ------- | --- | --- | --- | --- |
| Designated     | regional    |         | root    | address | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| Designated     | bridge      |         | address |         | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| Priority       |             |         |         |         | : 32768             |         |     |     |     |     |
| BPDUs sent     |             |         |         |         | : 638               |         |     |     |     |     |
| BPDUs received |             |         |         |         | : 9                 |         |     |     |     |     |
| Message        | expiry      |         |         |         | : 1 second          |         |     |     |     |     |
| Forward        | delay       | expiry  |         |         | : 18                | seconds |     |     |     |     |
| Forward        | transitions |         |         |         | : 3                 |         |     |     |     |     |
| TCN_Tx:        | 10,         | TCN_Rx: | 10      |         |                     |         |     |     |     |     |
Port 1/1/2
| Designated     | root        | address |         |         | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| -------------- | ----------- | ------- | ------- | ------- | ------------------- | ------- | --- | --- | --- | --- |
| Designated     | regional    |         | root    | address | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| Designated     | bridge      |         | address |         | : 48:0F:CF:AF:04:76 |         |     |     |     |     |
| Priority       |             |         |         |         | : 32768             |         |     |     |     |     |
| BPDUs sent     |             |         |         |         | : 641               |         |     |     |     |     |
| BPDUs received |             |         |         |         | : 11                |         |     |     |     |     |
| Message        | expiry      |         |         |         | : 1 second          |         |     |     |     |     |
| Forward        | delay       | expiry  |         |         | : 18                | seconds |     |     |     |     |
| Forward        | transitions |         |         |         | : 3                 |         |     |     |     |     |
| TCN_Tx:        | 10,         | TCN_Rx: | 10      |         |                     |         |     |     |     |     |
150
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

#### MST1
| Vlans mapped: |      | 1         |                     |      |          |           |         |         |
| ------------- | ---- | --------- | ------------------- | ---- | -------- | --------- | ------- | ------- |
| Bridge        |      | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          |      | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               |      | Port      | : 0                 |      |          | Cost      | : 0     |         |
|               |      | Rem Hops: | 20                  |      |          |           |         |         |
| PORT          | ROLE | STATE     |                     | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        |      | TCN-Rx    |                     |      |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- |             | ----------      |     |               |     |          |     |     |
| ------------- | ----------- | --------------- | --- | ------------- | --- | -------- | --- | --- |
| 1/1/1         | Designated  | Forwarding      |     | 20000         | 128 | P2P Edge | 100 | 60  |
| 20            |             | 10              |     |               |     |          |     |     |
| 1/1/2         | Designated  | Forwarding      |     | 20000         | 128 | P2P      | 100 | 60  |
| 20            |             | 10              |     |               |     |          |     |     |
| 1/1/3         | Designated  | Forwarding      |     | 20000         | 128 | Shr      | 100 | 60  |
| 20            |             | 10              |     |               |     |          |     |     |
| 1/1/4         | Designated  | Forwarding      |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            |             | 10              |     |               |     |          |     |     |
| 1/1/5         | Alternate   | Loop-Inc        |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            |             | 10              |     |               |     |          |     |     |
| 1/1/6         | Alternate   | Root-Inc        |     | 20000         | 128 | Shr Edge | 100 | 60  |
| 20            |             | 10              |     |               |     |          |     |     |
| 1/1/7         | Disabled    | Down            |     | 20000         | 128 | P2P      | 100 | 60  |
| 20            |             | 10              |     |               |     |          |     |     |
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
| Designated     | root        | address |     | : 48:0F:CF:AF:04:76 |         |     |     |     |
| -------------- | ----------- | ------- | --- | ------------------- | ------- | --- | --- | --- |
| Designated     | bridge      | address |     | : 48:0F:CF:AF:04:76 |         |     |     |     |
| Priority       |             |         |     | : 32768             |         |     |     |     |
| BPDUs sent     |             |         |     | : 641               |         |     |     |     |
| BPDUs received |             |         |     | : 11                |         |     |     |     |
| Message        | expiry      |         |     | : 1 second          |         |     |     |     |
| Forward        | delay       | expiry  |     | : 18                | seconds |     |     |     |
| Forward        | transitions |         |     | : 4                 |         |     |     |     |
| TCN_Tx:        | 10, TCN_Rx: | 10      |     |                     |         |     |     |     |
#### MST2
| Vlans mapped: |      | 3         |                     |      |          |           |         |         |
| ------------- | ---- | --------- | ------------------- | ---- | -------- | --------- | ------- | ------- |
| Bridge        |      | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          |      | Address   | : 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               |      | Port      | : 0                 |      |          | Cost      | : 0     |         |
|               |      | Rem Hops: | 20                  |      |          |           |         |         |
| PORT          | ROLE | STATE     |                     | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        |      | TCN-Rx    |                     |      |          |           |         |         |
Spanningtreeprotocols(STP)|151

-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- | ----------  |            |               |     |          |     |     |
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
| 1/1/7         | Disabled    | Down       | 20000         | 128 | P2P      | 100 | 60  |
| 20            | 10          |            |               |     |          |     |     |
| Topology      | change flag |            | : True        |     |          |     |     |
| Number        | of topology | changes    | : 4           |     |          |     |     |
| Last topology | change      | occurred   | : 516 seconds | ago |          |     |     |
Port 1/1/1
| Designated     | root address |         | : 48:0F:CF:AF:04:76 |         |     |     |     |
| -------------- | ------------ | ------- | ------------------- | ------- | --- | --- | --- |
| Designated     | bridge       | address | : 48:0F:CF:AF:04:76 |         |     |     |     |
| Priority       |              |         | : 32768             |         |     |     |     |
| BPDUs sent     |              |         | : 638               |         |     |     |     |
| BPDUs received |              |         | : 9                 |         |     |     |     |
| Message        | expiry       |         | : 1 second          |         |     |     |     |
| Forward        | delay expiry |         | : 18                | seconds |     |     |     |
| Forward        | transitions  |         | : 3                 |         |     |     |     |
| TCN_Tx:        | 10, TCN_Rx:  | 10      |                     |         |     |     |     |
Port 1/1/2
| Designated     | root address |         | : 48:0F:CF:AF:04:76              |         |     |     |     |
| -------------- | ------------ | ------- | -------------------------------- | ------- | --- | --- | --- |
| Designated     | bridge       | address | : 48:0F:CF:AF:04:76              |         |     |     |     |
| Priority       |              |         | : 32768                          |         |     |     |     |
| BPDUs sent     |              |         | : 641                            |         |     |     |     |
| BPDUs received |              |         | : 11                             |         |     |     |     |
| Message        | expiry       |         | : 1 second                       |         |     |     |     |
| Forward        | delay expiry |         | : 18                             | seconds |     |     |     |
| Forward        | transitions  |         | : 3                              |         |     |     |     |
| TCN_Tx:        | 10, TCN_Rx:  | 10      |                                  |         |     |     |     |
| Command        | History      |         |                                  |         |     |     |     |
| Release        |              |         | Modification                     |         |     |     |     |
| 10.09          |              |         | AnewstateDownisaddedintheoutput. |         |     |     |     |
| 10.07orearlier |              |         | --                               |         |     |     |     |
| Command        | Information  |         |                                  |         |     |     |     |
| Platforms      | Command      | context | Authority                        |         |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
152
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- |

| show spanning-tree |     |     | mst           |     | <INSTANCE-ID> |     |     |     |     |
| ------------------ | --- | --- | ------------- | --- | ------------- | --- | --- | --- | --- |
| show spanning-tree |     | mst | <INSTANCE-ID> |     | [vsx-peer]    |     |     |     |     |
Description
DisplaysMSTPconfigurationsforthegiveninstanceID.
| Parameter     |     |     |     |     | Description                                 |     |     |     |     |
| ------------- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
| <INSTANCE-ID> |     |     |     |     | SpecifiestheMSTPinstancenumber.Range:0to64. |     |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#       | show | spanning-tree |       | mst               | 1    |          |           |         |         |
| ------------- | ---- | ------------- | ----- | ----------------- | ---- | -------- | --------- | ------- | ------- |
| #### MST1     |      |               |       |                   |      |          |           |         |         |
| Vlans mapped: |      | 1             |       |                   |      |          |           |         |         |
| Bridge        |      | Address       | :     | 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
| Root          |      | Address       | :     | 48:0F:CF:AF:04:76 |      |          | Priority: | 32768   |         |
|               |      | Port          | :     | 0                 |      |          | Cost      | : 0     |         |
|               |      | Rem           | Hops: | 20                |      |          |           |         |         |
| PORT          | ROLE |               | STATE |                   | COST | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        |      | TCN-Rx        |       |                   |      |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- |             | ---------- |            |     |               |     |           |     |     |
| ------------- | ----------- | ---------- | ---------- | --- | ------------- | --- | --------- | --- | --- |
| 1/1/1         | Designated  |            | Forwarding |     | 20000         | 128 | P2P Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/2         | Designated  |            | Forwarding |     | 20000         | 128 | P2P       | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/3         | Designated  |            | Forwarding |     | 20000         | 128 | Shr       | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/4         | Designated  |            | Forwarding |     | 20000         | 128 | Shr Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/5         | Alternate   |            | Loop-Inc   |     | 20000         | 128 | Shr Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/6         | Alternate   |            | Root-Inc   |     | 20000         | 128 | Shr Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/7         | Disabled    |            | Down       |     | 20000         | 128 | P2P Bound | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| Topology      | change      | flag       |            |     | : True        |     |           |     |     |
| Number        | of topology |            | changes    |     | : 4           |     |           |     |     |
| Last topology |             | change     | occurred   |     | : 516 seconds | ago |           |     |     |
| Command       | History     |            |            |     |               |     |           |     |     |
| Release       |             |            |            |     | Modification  |     |           |     |     |
10.09
AnewstateDownisaddedintheoutput.
| 10.07orearlier |             |     |     |     | --  |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Command        | Information |     |     |     |     |     |     |     |     |
Spanningtreeprotocols(STP)|153

| Platforms |     | Command | context |     | Authority |     |     |     |     |
| --------- | --- | ------- | ------- | --- | --------- | --- | --- | --- | --- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |     |     | mst           |     | <INSTANCE-ID> |            | detail |     |     |
| ------------------ | --- | --- | ------------- | --- | ------------- | ---------- | ------ | --- | --- |
| show spanning-tree |     | mst | <INSTANCE-ID> |     | detail        | [vsx-peer] |        |     |     |
Description
DisplaysMSTPconfigurationsforthegiveninstanceIDwithcorrespondingportdetails.
| Parameter     |     |     |     |     | Description                                 |     |     |     |     |
| ------------- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
| <INSTANCE-ID> |     |     |     |     | SpecifiestheMSTPinstancenumber.Range:0to64. |     |     |     |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Example
| switch#       | show | spanning-tree |       | mst               | 1 detail |          |           |         |         |
| ------------- | ---- | ------------- | ----- | ----------------- | -------- | -------- | --------- | ------- | ------- |
| #### MST1     |      |               |       |                   |          |          |           |         |         |
| Vlans mapped: |      | 1             |       |                   |          |          |           |         |         |
| Bridge        |      | Address       | :     | 48:0F:CF:AF:04:76 |          |          | Priority: | 32768   |         |
| Root          |      | Address       | :     | 48:0F:CF:AF:04:76 |          |          | Priority: | 32768   |         |
|               |      | Port          | :     | 0                 |          |          | Cost      | : 0     |         |
|               |      | Rem           | Hops: | 20                |          |          |           |         |         |
| PORT          | ROLE |               | STATE |                   | COST     | PRIORITY | TYPE      | BPDU-Tx | BPDU-Rx |
| TCN-Tx        |      | TCN-Rx        |       |                   |          |          |           |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- |             | ---------- |            |     |               |     |           |     |     |
| ------------- | ----------- | ---------- | ---------- | --- | ------------- | --- | --------- | --- | --- |
| 1/1/1         | Designated  |            | Forwarding |     | 20000         | 128 | P2P Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/2         | Designated  |            | Forwarding |     | 20000         | 128 | P2P       | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/3         | Designated  |            | Forwarding |     | 20000         | 128 | Shr       | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/4         | Designated  |            | Forwarding |     | 20000         | 128 | Shr Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/5         | Alternate   |            | Loop-Inc   |     | 20000         | 128 | Shr Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/6         | Alternate   |            | Root-Inc   |     | 20000         | 128 | Shr Edge  | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| 1/1/7         | Disabled    |            | Down       |     | 20000         | 128 | P2P Bound | 100 | 60  |
| 20            |             | 10         |            |     |               |     |           |     |     |
| Topology      | change      | flag       |            |     | : True        |     |           |     |     |
| Number        | of topology |            | changes    |     | : 4           |     |           |     |     |
| Last topology |             | change     | occurred   |     | : 516 seconds | ago |           |     |     |
| Port 1/1/1    |             |            |            |     |               |     |           |     |     |
154
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |

| Designated     | root address |         | : 48:0F:CF:AF:04:76 |
| -------------- | ------------ | ------- | ------------------- |
| Designated     | bridge       | address | : 48:0F:CF:AF:04:76 |
| Priority       |              |         | : 32768             |
| BPDUs sent     |              |         | : 667               |
| BPDUs received |              |         | : 9                 |
| Message        | expiry       |         | : 0 second          |
| Forward        | delay expiry |         | : 18 seconds        |
| Forward        | transitions  |         | : 4                 |
| TCN_Tx:        | 10, TCN_Rx:  | 10      |                     |
Port 1/1/2
| Designated     | root address |         | : 48:0F:CF:AF:04:76 |
| -------------- | ------------ | ------- | ------------------- |
| Designated     | bridge       | address | : 48:0F:CF:AF:04:76 |
| Priority       |              |         | : 32768             |
| BPDUs sent     |              |         | : 670               |
| BPDUs received |              |         | : 11                |
| Message        | expiry       |         | : 0 second          |
| Forward        | delay expiry |         | : 18 seconds        |
| Forward        | transitions  |         | : 4                 |
| TCN_Tx:        | 10, TCN_Rx:  | 10      |                     |
| Command        | History      |         |                     |
| Release        |              |         | Modification        |
10.09
AnewstateDownisaddedintheoutput.
| 10.07orearlier |             |         | --        |
| -------------- | ----------- | ------- | --------- |
| Command        | Information |         |           |
| Platforms      | Command     | context | Authority |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |     | mst interface |     |
| ------------------ | --- | ------------- | --- |
show spanning-tree mst <INSTANCE-ID> interface <IFNAME> [vsx-peer]
Description
ShowsMSTPconfigurationsforthegiveninstanceIDwithcorrespondingportdetails.
| Parameter     |     |     | Description                                 |
| ------------- | --- | --- | ------------------------------------------- |
| <INSTANCE-ID> |     |     | SpecifiestheMSTPinstancenumber.Range:0to64. |
| <IFNAME>      |     |     | Specifiesaninterface.                       |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Spanningtreeprotocols(STP)|155

ShowingMSTconfigurationandportdetails:
| switch#    | show | spanning-tree |     | mst | 1 interface | 1/1/1 |          |              |
| ---------- | ---- | ------------- | --- | --- | ----------- | ----- | -------- | ------------ |
| Port 1/1/1 |      |               |     |     |             |       |          |              |
| Instance   |      | Role          |     |     | State       | Cost  | Priority | Vlans mapped |
-------------- -------------- ------------ ---------- ---------- ----------
| 1              |             | Designated |         |     | Forwarding   | 20000 | 128 | 1   |
| -------------- | ----------- | ---------- | ------- | --- | ------------ | ----- | --- | --- |
| Command        | History     |            |         |     |              |       |     |     |
| Release        |             |            |         |     | Modification |       |     |     |
| 10.07orearlier |             |            |         |     | --           |       |     |     |
| Command        | Information |            |         |     |              |       |     |     |
| Platforms      |             | Command    | context |     | Authority    |       |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show spanning-tree |     |         | summary |      | port |     |     |     |
| ------------------ | --- | ------- | ------- | ---- | ---- | --- | --- | --- |
| show spanning-tree |     | summary |         | port |      |     |     |     |
Description
Showsspanningtreeportsummaryinformation.
Example
Showingsummaryofspanningtreeports:
| switch#    | show    | spanning-tree |       | summary | port      |     |     |     |
| ---------- | ------- | ------------- | ----- | ------- | --------- | --- | --- | --- |
| STP status |         |               |       |         | : Enabled |     |     |     |
| Protocol   |         |               |       |         | : MSTP    |     |     |     |
| BPDU guard | timeout |               | value |         | : None    |     |     |     |
BPDU guard enabled interfaces : 1/1/1-1/1/9,1/1/11,1/1/13,1/1/15,1/1/17,1/1/19,
1/1/21,lag1,lag2
| BPDU filter   |         | enabled  | interfaces |     | : None        |            |      |     |
| ------------- | ------- | -------- | ---------- | --- | ------------- | ---------- | ---- | --- |
| Root guard    | enabled |          | interfaces |     | : 1/1/3       |            |      |     |
| Loop guard    | enabled |          | interfaces |     | : 1/1/2       |            |      |     |
| TCN guard     | enabled |          | interfaces |     | : 1/1/1-1/1/3 |            |      |     |
| RPVST filter  |         | enabled  | interfaces |     | : 1/1/37      |            |      |     |
| RPVST guard   |         | enabled  | interfaces |     | : None        |            |      |     |
| Interface     | count   | by       | state      |     |               |            |      |     |
| Instance      | ID      | Blocking | Listening  |     | Learning      | Forwarding | Down |     |
| ------------- |         | -------- | ---------  |     | --------      | ---------- | ---- |     |
| 0             |         |          | 2          |     | 0             | 0          | 15 0 |     |
| 1             |         |          | 2          |     | 0             | 0          | 15 0 |     |
| 2             |         |          | 2          |     | 0             | 0          | 15 0 |     |
156
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- |

| -------------       | -------- | --------- |     | -------- ----------              | ---- |     |     |     |     |
| ------------------- | -------- | --------- | --- | -------------------------------- | ---- | --- | --- | --- | --- |
| Total = 3           |          | 6         | 0   | 0                                | 45 0 |     |     |     |     |
| Command History     |          |           |     |                                  |      |     |     |     |     |
| Release             |          |           |     | Modification                     |      |     |     |     |     |
| 10.09               |          |           |     | AnewstateDownisaddedintheoutput. |      |     |     |     |     |
| 10.07orearlier      |          |           |     | --                               |      |     |     |     |     |
| Command Information |          |           |     |                                  |      |     |     |     |     |
| Platforms           | Command  | context   |     | Authority                        |      |     |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show spanning-tree |     | summary |      | root |     |     |     |     |     |
| ------------------ | --- | ------- | ---- | ---- | --- | --- | --- | --- | --- |
| show spanning-tree |     | summary | root |      |     |     |     |     |     |
Description
Showsspanningtreerootsummaryinformation.
Example
Showingspanningtreerootsummary:
| switch#     | show spanning-tree |              | summary | root              |            |     |     |      |      |
| ----------- | ------------------ | ------------ | ------- | ----------------- | ---------- | --- | --- | ---- | ---- |
| STP status  |                    |              | :       | Enabled           |            |     |     |      |      |
| Protocol    |                    |              | :       | MSTP              |            |     |     |      |      |
| System ID   |                    |              | :       | 70:72:cf:32:50:f5 |            |     |     |      |      |
| Root bridge | for                | STP Instance | :       | 0,1,2             |            |     |     |      |      |
|             |                    |              |         |                   | Root Hello | Max | Fwd |      |      |
| Instance    | ID                 | Priority     | Root ID |                   | cost Time  | Age | Dly | Root | Port |
--------------- -------- ----------------- --------- ----- --- --- ------------
| 0                   |     | 32768 | 70:72:cf:32:50:f5 |              | 0   | 2 20 | 15  |     | n/a   |
| ------------------- | --- | ----- | ----------------- | ------------ | --- | ---- | --- | --- | ----- |
| 1                   |     | 32768 | 70:72:cf:32:50:f5 |              | 0   | 2 20 | 15  |     | n/a   |
| 2                   |     | 32768 | 70:72:cf:32:50:f5 |              | 200 | 2 20 | 15  |     | 1/1/1 |
| Command History     |     |       |                   |              |     |      |     |     |       |
| Release             |     |       |                   | Modification |     |      |     |     |       |
| 10.07orearlier      |     |       |                   | --           |     |      |     |     |       |
| Command Information |     |       |                   |              |     |      |     |     |       |
Spanningtreeprotocols(STP)|157

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
spanning-tree
spanning-tree
no spanning-tree
Description
Enablesthespanningtreeprotocolontheswitch.
Thenoformofthiscommanddisablesthespanningtreeprotocolontheswitch.
Examples
Enablingspanningtree:
| switch(config)# | spanning-tree |     |     |
| --------------- | ------------- | --- | --- |
Disablingspanningtree:
| switch(config)#     | no      | spanning-tree |              |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | bpdu-filter |     |     |
| ---------------- | ----------- | --- | --- |
| spanning-tree    | bpdu-filter |     |     |
| no spanning-tree | bpdu-filter |     |     |
Description
Enablesthebpdufilterfortheinterface.
TheBPDUfilterfeatureallowscontrolofspanningtreeparticipationonaper-portbasis.Itcanbeused
toexcludespecificportsfrombecomingpartofspanningtreeoperations.AportwiththeBPDUfilter
enabledwillignoreincomingBPDUpackets,doesnottransmitBPDU,andstayslockedinthespanning
treeforwardingstate.Allotherportsmaintaintheirrole.Typicalusesforthisparameterinclude:
158
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

n TohaveMSTPoperationsrunningonselectedportsoftheswitchratherthaneveryportoftheswitch
atatime.
n TopreventthespreadoferrantBPDUframes.
n Toeliminatetheneedforatopologychangewhenaport'slinkstatuschanges.Forexample,ports
thatconnecttoserversandworkstationscanbeconfiguredtoremainoutsideofspanningtree
operations.
n ToprotectthenetworkfromdenialofserviceattacksthatusespoofingBPDUsbydroppingincoming
BPDUframes.Forthisscenario,BPDUprotectionoffersamoresecurealternative,implementing
portshutdownandadetectionalertwhenerrantBPDUframesarereceived.
PortsconfiguredwiththeBPDUfiltermoderemainactive(learningandforwardframes).However,spanningtree
cannotreceiveortransmitBPDUsontheport.Theportremainsinaforwardingstate,permittingallbroadcast
traffic.Thiscancreateanetworkstormifthereareanyloops(thatis,redundantlinks)usingtheseports.Ifyou
suddenlyhaveahighload,disconnectthelinkanddisabletheBPDUfilter(usingthenocommand.)
Thenoformofthecommandsetsthebpdufilterstatustothedefaultofdisabledontheinterface.
Examples
Enablingthebpdufilteroninterface1/1/1:
| switch(config)#    |     | interface     | 1/1/1 |             |
| ------------------ | --- | ------------- | ----- | ----------- |
| switch(config-if)# |     | spanning-tree |       | bpdu-filter |
Disablingbpdufilteroninterface1/1/1:
| switch(config)#     |         | interface        | 1/1/1 |              |
| ------------------- | ------- | ---------------- | ----- | ------------ |
| switch(config-if)#  |         | no spanning-tree |       | bpdu-filter  |
| Command History     |         |                  |       |              |
| Release             |         |                  |       | Modification |
| 10.07orearlier      |         |                  |       | --           |
| Command Information |         |                  |       |              |
| Platforms           | Command | context          |       | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | bpdu-guard |     |     |     |
| ---------------- | ---------- | --- | --- | --- |
| spanning-tree    | bpdu-guard |     |     |     |
| no spanning-tree | bpdu-guard |     |     |     |
Description
EnablestheBPDUguardontheselectedswitchinterface.WhenBPDUguardisenabled,interfaces
receivingMSTPBPDUsbecomedisabled.
Spanningtreeprotocols(STP)|159

BPDUprotectionisasecurityfeaturedesignedtoprotecttheactiveMSTPtopologybypreventing
spoofedBPDUpacketsfromenteringtheMSTPdomain.Inatypicalimplementation,BPDUprotection
wouldbeappliedtoedgeportsconnectedtoenduserdevicesthatdonotrunMSTP.IfMSTPBPDU
packetsarereceivedonaprotectedport,thisfeaturedisablesthatportandalertsthenetworkmanager
usinganSNMPtrap.
OccasionallyahardwareorsoftwarefailurecancauseMSTPtofail,creatingforwardingloopsthatcan
causenetworkfailureswhereunidirectionallinksareused.Thenon-designatedporttransitionsina
faultymannerbecausetheportisnolongerreceivingMSTPBPDUs.
ThenoformofthecommanddisablesBPDUguardontheselectedinterface.
Examples
EnablingtheBPDUguardoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1         |     |            |
| ------------------ | --- | --------- | ------------- | --- | ---------- |
| switch(config-if)# |     |           | spanning-tree |     | bpdu-guard |
DisablingBPDUguardoninterface1/1/1:
| switch(config)#    |             | interface | 1/1/1            |     |              |
| ------------------ | ----------- | --------- | ---------------- | --- | ------------ |
| switch(config-if)# |             |           | no spanning-tree |     | bpdu-guard   |
| Command            | History     |           |                  |     |              |
| Release            |             |           |                  |     | Modification |
| 10.07orearlier     |             |           |                  |     | --           |
| Command            | Information |           |                  |     |              |
| Platforms          |             | Command   | context          |     | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |            | bpdu-guard |         | timeout    |              |
| ---------------- | ---------- | ---------- | ------- | ---------- | ------------ |
| spanning-tree    | bpdu-guard |            | timeout | <INTERVAL> |              |
| no spanning-tree |            | bpdu-guard | timeout |            | [<INTERVAL>] |
Description
Enablesandconfigurestheautore-enabletimeoutinsecondsforallinterfaceswithBPDUguard
enabled.WhenaninterfaceisdisabledafterreceivinganunauthorizedBPDUitwillautomaticallybere-
enabledafterthetimeoutexpires.Thedefaultisfortheinterfacetostaydisableduntilmanuallyre-
enabled.
ThenoformofthecommanddisablesBPDUguardtimeoutontheinterface.Thisisthedefault.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
<INTERVAL>
Specifiesthere-enabletimeoutinseconds.Range:1to65535.
160
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

Example
EnablingtheBPDUguardtimeoutoninterface1/1/1:
switch(config)#
|                    |     | interface | 1/1/1         |     |            |            |
| ------------------ | --- | --------- | ------------- | --- | ---------- | ---------- |
| switch(config-if)# |     |           | spanning-tree |     | bpdu-guard | timeout 10 |
DisablingBPDUguardtimeoutoninterface1/1/1:
| switch(config)#    |             | interface | 1/1/1            |     |              |     |
| ------------------ | ----------- | --------- | ---------------- | --- | ------------ | --- |
| switch(config-if)# |             |           | no spanning-tree |     | bpdu-guard   |     |
| Command            | History     |           |                  |     |              |     |
| Release            |             |           |                  |     | Modification |     |
| 10.07orearlier     |             |           |                  |     | --           |     |
| Command            | Information |           |                  |     |              |     |
| Platforms          | Command     |           | context          |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |             | config-name |                 |     |     |     |
| ---------------- | ----------- | ----------- | --------------- | --- | --- | --- |
| spanning-tree    | config-name |             | <CONFIG-NAME>   |     |     |     |
| no spanning-tree |             | config-name | [<CONFIG-NAME>] |     |     |     |
Description
SetstheconfigurationnamefortheMSTregioninwhichtheswitchresides.
AllswitcheswithinanMSTregionmusthaveidenticalconfigurationnames.FormorethanoneMSTP
switchinthesameMSTregion,theidenticalregionnamemustbeconfiguredonallsuchswitches.Ifthe
defaultconfigurationnameisretainedonaswitch,itcannotexistinthesameMSTregionwithanother
switch.
Thenoformofthiscommandoverwritesthecurrentlyconfigurednamewiththedefaultname.The
defaultnameisatextstringusingthehexadecimalrepresentationofthesystemMACaddress.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<CONFIG-NAME> SpecifiestheconfigurationnamefortheMSTregioninwhichthe
switchresides.Default:textstringusingthehexadecimal
representationoftheMACaddressoftheswitch.Range:1-32
nonblankcharacters(case-sensitive).
Examples
SettingtheconfigurationnametoMST0:
| switch(config)# |     | spanning-tree |     | config-name |     | MST0 |
| --------------- | --- | ------------- | --- | ----------- | --- | ---- |
Spanningtreeprotocols(STP)|161

Settingtheconfigurationnametothedefaultvalue:
| switch(config)# |             | no  | spanning-tree | config-name  |     |
| --------------- | ----------- | --- | ------------- | ------------ | --- |
| Command         | History     |     |               |              |     |
| Release         |             |     |               | Modification |     |
| 10.07orearlier  |             |     |               | --           |     |
| Command         | Information |     |               |              |     |
| Platforms       | Command     |     | context       | Authority    |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |                 | config-revision |     |                     |     |
| ---------------- | --------------- | --------------- | --- | ------------------- | --- |
| spanning-tree    | config-revision |                 |     | <REVISION-NUMBER>   |     |
| no spanning-tree |                 | config-revision |     | [<REVISION-NUMBER>] |     |
Description
ConfigurestherevisionnumberfortheMSTregioninwhichtheswitchresides.Allswitcheswithinan
MSTregionmusthaveidenticalrevisionnumbers.Usethissettingtodifferentiatebetweenregion
configurations.Forexample,whenchangingconfigurationsettingswithinaregionwhereyouwantto
tracktheconfigurationversionsyouuse,orwhencreatinganewregionfromasubsetofswitchesina
currentregionandyouwanttomaintainthesameregionname.
ThenoformofthiscommandoverwritesthecurrentlyconfiguredrevisionnumberoftheMSTregion
andsetsittothedefaultvalueof0.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<REVISION-NUMBER> SpecifiestherevisionnumberfortheMSTregioninwhichthe
switchresides.Range:0-65535.Default:0.
Examples
Settingtherevisionto40:
| switch(config)# |     | spanning-tree |     | config-revision | 40  |
| --------------- | --- | ------------- | --- | --------------- | --- |
Settingtherevisiontothedefaultvalue:
switch(config)#
|         |         | no  | spanning-tree | config-revision |     |
| ------- | ------- | --- | ------------- | --------------- | --- |
| Command | History |     |               |                 |     |
162
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | cost |               |     |     |
| ---------------- | ---- | ------------- | --- | --- |
| spanning-tree    | cost | <PORT-COST>   |     |     |
| no spanning-tree | cost | [<PORT-COST>] |     |     |
Description
SetsindividualportcostforMSTI0.
Foragivenport,thepathcostsettingcanbedifferentfordifferentMSTIstowhichtheportmaybelong.
TheswitchusesthepathcosttodeterminewhichportsaretheforwardingportsintheMSTI;thatis,
whichlinkstousefortheactivetopologyoftheMSTIandwhichportstoblock.
Costgetscalculatedbasedonphysicalinterfacelinkspeed.Itisnotbasedoncumulativespeedofall
physicallinksunderalag.Therefore,thecostwillbesamefora1Ginterfaceand2x1Glaginterfaces.
ThenoformofthecommandsetstheportcostforMSTI0instancetothedefaultvalue.
| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
<PORT-COST> SpecifiesthecostoftheportforMSTI0.Range:1-200,000,000.
Defaultiscalculatedfromtheportlinkspeed:
n 10Mbpslinkspeedequalsapathcostof2,000,000.
n 100Mbpslinkspeedequalsapathcostof200,000.
n 1Gbpslinkspeedequalsapathcostof20,000.
n 10Gbpslinkspeedequalsapathcostof2,000.
100Gbpslinkspeedequalsapathcostof200.
n
n 1Tbpslinkspeedequalsapathcostof20.
Examples
Settingthecostto2000oninterface1/1/1:
| switch(config)#    |     | interface     | 1/1/1 |           |
| ------------------ | --- | ------------- | ----- | --------- |
| switch(config-if)# |     | spanning-tree |       | cost 2000 |
Settingthecosttothedefaultoninterface1/1/1:
| switch(config)#    |     | interface        | 1/1/1 |      |
| ------------------ | --- | ---------------- | ----- | ---- |
| switch(config-if)# |     | no spanning-tree |       | cost |
| Command History    |     |                  |       |      |
Spanningtreeprotocols(STP)|163

| Release        |             |     |         |     | Modification |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |               | forward-delay |     |                   |     |     |
| ---------------- | ------------- | ------------- | --- | ----------------- | --- | --- |
| spanning-tree    | forward-delay |               |     | <DELAY-IN-SECS>   |     |     |
| no spanning-tree |               | forward-delay |     | [<DELAY-IN-SECS>] |     |     |
Description
Configuresthetimetheswitchwaitsbetweentransitionsfromlisteningtolearningandfromlearningto
forwardingstates.
Thenoformofthiscommandsetsforwarddelaytimeforthebridgetothedefaultof15seconds.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<DELAY-IN-SECS> Specifiestheforwarddelaytimeinseconds.Default:15seconds.
Range:4-30.
Examples
Settingforwarddelayto6seconds:
| switch(config)# |     | spanning-tree |     |     | forward-delay | 6   |
| --------------- | --- | ------------- | --- | --- | ------------- | --- |
Settingforwarddelaytothedefaultof15seconds:
| switch(config)# |             | no  | spanning-tree |     | forward-delay |     |
| --------------- | ----------- | --- | ------------- | --- | ------------- | --- |
| Command         | History     |     |               |     |               |     |
| Release         |             |     |               |     | Modification  |     |
| 10.07orearlier  |             |     |               |     | --            |     |
| Command         | Information |     |               |     |               |     |
| Platforms       | Command     |     | context       |     | Authority     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree |     | hello-time |     |     |     |     |
| ------------- | --- | ---------- | --- | --- | --- | --- |
164
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- |

| spanning-tree    | hello-time |            | <HELLO-IN-SECS> |                   |     |     |
| ---------------- | ---------- | ---------- | --------------- | ----------------- | --- | --- |
| no spanning-tree |            | hello-time |                 | [<HELLO-IN-SECS>] |     |     |
Description
ConfiguresthetransmissionintervalbetweenconsecutiveBridgeProtocolDataUnits(BPDU)thatthe
switchsendsasarootbridge.ThehellotimeintervalisinsertedinoutboundBPDUs.
Thenoformofthiscommandsetshellotimetothedefaultof2seconds.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<HELLO-IN-SECS>
Specifiesthehellotimeintervalinseconds.Default:2seconds.
Range:2-10.
Examples
Settingthehellotimeintervalto6seconds:
| switch(config)# |     | spanning-tree |     |     | hello-time | 6   |
| --------------- | --- | ------------- | --- | --- | ---------- | --- |
Settingthehellotimeintervaltothedefaultof2seconds:
| switch(config)# |             | no      | spanning-tree |     | hello-time   |     |
| --------------- | ----------- | ------- | ------------- | --- | ------------ | --- |
| Command         | History     |         |               |     |              |     |
| Release         |             |         |               |     | Modification |     |
| 10.07orearlier  |             |         |               |     | --           |     |
| Command         | Information |         |               |     |              |     |
| Platforms       |             | Command | context       |     | Authority    |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |          | instance |               | cost |      |               |
| ---------------- | -------- | -------- | ------------- | ---- | ---- | ------------- |
| spanning-tree    | instance |          | <INSTANCE-ID> |      | cost | <PORT-COST>   |
| no spanning-tree |          | instance | <INSTANCE-ID> |      | cost | [<PORT-COST>] |
Description
SetstheindividualportcostforanMSTI.Theswitchusesthepathcosttodeterminewhichlinkstouse
fortheactivetopologyoftheMSTI(forwardingports)andwhichportstoblock.Thepathcostsettingfor
aportcanbedifferentoneachMSTItowhichtheportbelongs.
ThenoformofthiscommandsetstheportcostforanMSTItothedefaultvalue.
Spanningtreeprotocols(STP)|165

| Parameter     |     |     |     | Description                        |     |
| ------------- | --- | --- | --- | ---------------------------------- | --- |
| <INSTANCE-ID> |     |     |     | SpecifiestheMSTInumber.Range:1-64. |     |
<PORT-COST> SpecifiesthecostoftheportfortheMSTI.Range:1-200000000.
Defaultvalueiscalculatedfromtheportlinkspeed:
n 10Mbpslinkspeedequalsapathcostof2000000.
n 100Mbpslinkspeedequalsapathcostof200000.
n 1Gbpslinkspeedequalsapathcostof20000.
Examples
Settingtheport1/1/1costforMSTI1to2000:
| switch(config)#    |     | interface     | 1/1/1 |          |             |
| ------------------ | --- | ------------- | ----- | -------- | ----------- |
| switch(config-if)# |     | spanning-tree |       | instance | 1 cost 2000 |
Settingtheport1/1/1costforMSTI1tothedefault:
| switch(config)#     |         | interface        | 1/1/1 |              |        |
| ------------------- | ------- | ---------------- | ----- | ------------ | ------ |
| switch(config-if)#  |         | no spanning-tree |       | instance     | 1 cost |
| Command History     |         |                  |       |              |        |
| Release             |         |                  |       | Modification |        |
| 10.07orearlier      |         |                  |       | --           |        |
| Command Information |         |                  |       |              |        |
| Platforms           | Command | context          |       | Authority    |        |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree | instance |     | port-priority |     |     |
| ------------- | -------- | --- | ------------- | --- | --- |
spanning-tree instance <INSTANCE-ID> port-priority <PRIORITY-MULTIPLIER>
no spanning-tree instance <INSTANCE-ID> port-priority [<PRIORITY-MULTIPLIER>]
Description
ConfiguresthepriorityasaprioritymultiplierforthespecifiedportsinthespecifiedMSTinstance.
Foragivenport,theprioritysettingcanbedifferentfordifferentMSTinstancestowhichtheportmay
belong.
Thenoformofthiscommandsetstheportprioritytothedefaultvalueof8fortheMSTinstance.The
defaultpriorityvalueisderivedbymultiplying8by16.
166
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| Parameter     |     |     |     | Description                                |     |     |
| ------------- | --- | --- | --- | ------------------------------------------ | --- | --- |
| <INSTANCE-ID> |     |     |     | SpecifiestheMSTPinstancenumber.Range:1-64. |     |     |
<PRIORITY-MULTIPLIER> Specifiesthepriorityasamultiplier.Default:8.Range:0to15.
ThepriorityrangeforaportinagivenMSTinstanceis0to255.
However,thiscommandspecifiesthepriorityasamultiplier(0to
15)of16.Whenyouspecifyaprioritymultiplierof0to15,the
actualpriorityassignedtotheswitchis:(priority-multiplier)x16.
Examples
Settingtheport1/1/1priorityforinstance1to8:
| switch(config)# |     | interface | 1/1/1 |     |     |     |
| --------------- | --- | --------- | ----- | --- | --- | --- |
switch(config-if)#
|     |     | spanning-tree |     | instance | 1 port-priority | 8   |
| --- | --- | ------------- | --- | -------- | --------------- | --- |
Settingtheport1/1/1priorityforinstance1tothedefault:
| switch(config)#     |         | interface        | 1/1/1 |              |                 |     |
| ------------------- | ------- | ---------------- | ----- | ------------ | --------------- | --- |
| switch(config-if)#  |         | no spanning-tree |       | instance     | 1 port-priority |     |
| Command History     |         |                  |       |              |                 |     |
| Release             |         |                  |       | Modification |                 |     |
| 10.07orearlier      |         |                  |       | --           |                 |     |
| Command Information |         |                  |       |              |                 |     |
| Platforms           | Command | context          |       | Authority    |                 |     |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree | instance |     | priority |     |     |     |
| ------------- | -------- | --- | -------- | --- | --- | --- |
spanning-tree instance <INSTANCE-ID> priority <PRIORITY-MULTIPLIER>
no spanning-tree instance <INSTANCE-ID> priority [<PRIORITY-MULTIPLIER>]
Description
SetstheswitchpriorityforthespecifiedMSTinstance.
Thenoformofthiscommandsetsthepriorityforthespecifiedinstancetothedefaultof8.
| Parameter     |     |     |     | Description                                 |     |     |
| ------------- | --- | --- | --- | ------------------------------------------- | --- | --- |
| <INSTANCE-ID> |     |     |     | SpecifiestheMSTPinstancenumber.Range:1to64. |     |     |
<PRIORITY-MULTIPLIER> Specifiesthepriorityasamultiplier.Default:8.Range:0to15.
ThepriorityrangeforanMSTPswitchis0-61440.However,this
commandspecifiesthepriorityasamultiplier(0-15)of4096.
Spanningtreeprotocols(STP)|167

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
Thatis,whenyouspecifyaprioritymultipliervalueof0-15,the
actualpriorityassignedtotheswitchis:(priority-multiplier)x
4096.Forexample,with2asthepriority-multiplieronagiven
MSTPswitch,theswitchprioritysettingis8,192.
Examples
Settingtheprioritymultiplierforinstance1to5:
| switch(config)# |     | spanning-tree |     |     | instance | 1 priority 5 |
| --------------- | --- | ------------- | --- | --- | -------- | ------------ |
Settingtheprioritymultiplierforinstance1tothedefaultof8:
| switch(config)# |             | no      | spanning-tree |     | instance     | 1 priority |
| --------------- | ----------- | ------- | ------------- | --- | ------------ | ---------- |
| Command         | History     |         |               |     |              |            |
| Release         |             |         |               |     | Modification |            |
| 10.07orearlier  |             |         |               |     | --           |            |
| Command         | Information |         |               |     |              |            |
| Platforms       |             | Command | context       |     | Authority    |            |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |          | instance |               | vlan |      |           |
| ---------------- | -------- | -------- | ------------- | ---- | ---- | --------- |
| spanning-tree    | instance |          | <INSTANCE-ID> |      | vlan | <VLAN-ID> |
| no spanning-tree |          | instance | <INSTANCE-ID> |      | vlan | <VLAN-ID> |
Description
CreatesanewinstancewithVLANsmappedormapsVLANstoanexistinginstance.
EachinstancemusthaveatleastoneVLANmappedtoit.WhenVLANsaremappedtoaninstance,they
areautomaticallyunmappedfromtheinstancetheyweremappedtobefore.AnyMSTPinstancecan
havealltheVLANsconfiguredontheswitch.
ThenoformofthiscommandremovesthespecifiedVLANfromtheMSTPinstance.
| Parameter     |     |     |     |     | Description                                 |     |
| ------------- | --- | --- | --- | --- | ------------------------------------------- | --- |
| <INSTANCE-ID> |     |     |     |     | SpecifiestheMSTPinstancenumber.Range:1to64. |     |
| <VLAN-ID>     |     |     |     |     | SpecifiesaVLANIDnumber.                     |     |
Examples
MappingVLAN1toinstance1:
168
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- |

| switch(config)# |     | spanning-tree |     | instance | 1 vlan 1 |
| --------------- | --- | ------------- | --- | -------- | -------- |
RemovingVLAN1frominstance1:
| switch(config)# |             | no  | spanning-tree | instance     | 1 vlan 1 |
| --------------- | ----------- | --- | ------------- | ------------ | -------- |
| Command         | History     |     |               |              |          |
| Release         |             |     |               | Modification |          |
| 10.07orearlier  |             |     |               | --           |          |
| Command         | Information |     |               |              |          |
| Platforms       | Command     |     | context       | Authority    |          |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree |           | link-type |                         |     |     |
| ------------- | --------- | --------- | ----------------------- | --- | --- |
| spanning-tree | link-type |           | {point-to-point|shared} |     |     |
Description
Specifiesthelinktypeoftheinterface,whichisnormallyderivedfromtheduplexsettingoftheport.
Thedefaultsettingdependsontheduplexmodeoftheport:full-duplexportsarepoint-to-point,half-
duplexportsareshared.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
point-to-point
Specifiesthelinktypeaspoint-to-point.
| shared |     |     |     | Specifiesthelinktypeasshared. |     |
| ------ | --- | --- | --- | ----------------------------- | --- |
Examples
Settingthelinktypetopoint-to-pointoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1         |           |                |
| ------------------ | --- | --------- | ------------- | --------- | -------------- |
| switch(config-if)# |     |           | spanning-tree | link-type | point-to-point |
Settingthelinktypetosharedoninterface1/1/1:
| switch(config)#    |         | interface | 1/1/1         |           |        |
| ------------------ | ------- | --------- | ------------- | --------- | ------ |
| switch(config-if)# |         |           | spanning-tree | link-type | shared |
| Command            | History |           |               |           |        |
Spanningtreeprotocols(STP)|169

| Release             |         |         |     | Modification |
| ------------------- | ------- | ------- | --- | ------------ |
| 10.07orearlier      |         |         |     | --           |
| Command Information |         |         |     |              |
| Platforms           | Command | context |     | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | loop-guard |     |     |     |
| ---------------- | ---------- | --- | --- | --- |
| spanning-tree    | loop-guard |     |     |     |
| no spanning-tree | loop-guard |     |     |     |
Description
Enablestheloopguardontheinterface.STPloopguardisbestappliedonblockingorforwardingports.
Thenoformofthecommandsetstheloopguardstatustothedefaultofdisabledontheinterface.
Usage
OccasionallyahardwareorsoftwarefailurecancauseMSTPtofail,creatingforwardingloopsthatcan
causenetworkfailureswhereunidirectionallinksareused.Thenon-designatedporttransitionsina
faultymannerbecausetheportisnolongerreceivingMSTPBPDUs.
Loopguardcausesthenon-designatedporttogointotheMSTPloopinconsistentstateinsteadofthe
forwardingstate.IntheloopinconsistentstatetheportpreventsdatatrafficandBPDUtransmission
throughthelink,thereforeavoidingtheloopcreation.WhenBPDUsagainarereceivedonthe
inconsistentport,itresumesnormalMSTPoperationautomatically.
Inthisexample,thetransmissionfromswitch1port10toswitch2port20isblockedduetoahardware
failure.Switch2port2doesnotreceiveBPDUsandgoesintoaforwardingstate,creatingaloop.
Whenloopguardisconfiguredforswitch2port20,thisportgoesfromaforwardingstatetoan
inconsistentstate,anddoesnotforwardthetrafficthroughthelink,thusavoidingloopcreation.
Examples
Enablingtheloopguardoninterface1/1/1:
| switch(config)#    |     | interface     | 1/1/1 |            |
| ------------------ | --- | ------------- | ----- | ---------- |
| switch(config-if)# |     | spanning-tree |       | loop-guard |
Disablingloopguardoninterface1/1/1:
| switch(config)#    |     | interface        | 1/1/1 |              |
| ------------------ | --- | ---------------- | ----- | ------------ |
| switch(config-if)# |     | no spanning-tree |       | loop-guard   |
| Command History    |     |                  |       |              |
| Release            |     |                  |       | Modification |
| 10.07orearlier     |     |                  |       | --           |
170
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| Command Information |         |         |           |
| ------------------- | ------- | ------- | --------- |
| Platforms           | Command | context | Authority |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | max-age |                 |     |
| ---------------- | ------- | --------------- | --- |
| spanning-tree    | max-age | <AGE-IN-SECS>   |     |
| no spanning-tree | max-age | [<AGE-IN-SECS>] |     |
Description
Setsthemaximumagetimer,whichspecifiesthemaximumagevaluethattheswitchinsertsin
outboundBPDUpacketsitsendsasarootbridge.Max-ageistheinterval,specifiedintheBPDU,that
BPDUdataremainsvalidafteritsreception.
ThebridgerecomputesthespanningtreetopologyifitdoesnotreceiveanewBPDUbeforemax-age
expiry.
Thenoformofthiscommandsetsthemax-agevaluetothedefaultof20seconds.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<AGE-IN-SECS> Specifiesthemax-ageinseconds.Range:6to40.Default:20.
Examples
Settingthemax-ageto10seconds:
| switch(config)# | spanning-tree |     | max-age 10 |
| --------------- | ------------- | --- | ---------- |
Settingthemax-agetothedefaultof20seconds:
| switch(config)#     | no      | spanning-tree | max-age      |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | max-hops |               |     |
| ---------------- | -------- | ------------- | --- |
| spanning-tree    | max-hops | <HOP-COUNT>   |     |
| no spanning-tree | max-hops | [<HOP-COUNT>] |     |
Spanningtreeprotocols(STP)|171

Description
ConfiguresthemaxhopsettingthattheswitchinsertsintoBPDUsthatitsendsoutastherootbridge.
ThemaxhopsettingdeterminesthenumberofbridgesinanMSTregionthataBPDUcantraverse
beforeitisdiscarded.
Thenoformofthiscommandsetsthemaximumnumberofhopstothedefaultof20.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<HOP-COUNT> Specifiesthemaximumnumberofhops.Range:1to40.Default:
20.
Examples
Settingthehopcountto10:
| switch(config)# | spanning-tree |     | max-hops 10 |
| --------------- | ------------- | --- | ----------- |
Settingthemax-agetothedefaultof20:
| switch(config)#     | no      | spanning-tree | max-hops     |
| ------------------- | ------- | ------------- | ------------ |
| Command History     |         |               |              |
| Release             |         |               | Modification |
| 10.07orearlier      |         |               | --           |
| Command Information |         |               |              |
| Platforms           | Command | context       | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree | mode |     |     |
| ------------- | ---- | --- | --- |
spanning-tree mode {mstp|rpvst [auto-vlan-enable [priority <NUMBER>]]}
no spanning-tree mode {mstp|rpvst [auto-vlan-enable [priority <NUMBER>]]}
Description
Setsthespanningtreeprotocol(STP)modetoeitherMSTPmode(Multiple-instanceSpanningTree
Protocol)orRPVSTmode(RapidPerVLANSpanningTree).EnablingtheRPVSTAutoVLANfeaturewill
runRPVSTonallVLANscurrentlyconfiguredontheswitch.Defaultpriorityof8willbeassignedtothe
VLANsbeingautocreated.
Thenoformofthiscommandsetsthespanningtreemodetothedefaultmstp.
172
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

Enablingauto-VLANcanleadtoanundeterministicstateifautoscaledbeyondthemaxsystemlimitmentionedin
thecapacity-status.
| Parameter |     | Description                                  |
| --------- | --- | -------------------------------------------- |
| mstp      |     | SetstheSTPmodetoMSTPwhichappliesspanningtree |
separatelyforeachsetofVLANscalledanMSTI(multiple
spanningtreeinstance).
rpvst
SetstheSTPmodetoRPVST.
| auto-vlan-enable |     | SelectsRPVSTautoVLANmode. |
| ---------------- | --- | ------------------------- |
priority <NUMBER>
SpecifiestheprioritesforallautocreatedRPVSTinstances.
Configuredasamultipleof4096.Default:8.
Examples
EnablingMSTPmode:
switch(config)#
|     | spanning-tree | mode mstp |
| --- | ------------- | --------- |
DisablingMSTPmode:
| switch(config)# | no spanning-tree | mode mstp |
| --------------- | ---------------- | --------- |
EnablingRPVSTmode:
| switch(config)# | spanning-tree | mode rpvst |
| --------------- | ------------- | ---------- |
DisablingRPVSTmode:
| switch(config)# | no spanning-tree | mode rpvst |
| --------------- | ---------------- | ---------- |
EnablingRPVSTautoVLANwithapriorityof1:
switch(config)# spanning-tree mode rpvst auto-vlan-enable priority 1
DisablingRPVSTautoVLANwithapriorityof1:
switch(config)# no spanning-tree mode rpvst auto-vlan-enable priority 1
Command History
Spanningtreeprotocols(STP)|173

| Release        |             |     |         |     | Modification         |     |
| -------------- | ----------- | --- | ------- | --- | -------------------- | --- |
| 10.12.1000     |             |     |         |     | AutoVLANenableadded. |     |
| 10.07orearlier |             |     |         |     | --                   |     |
| Command        | Information |     |         |     |                      |     |
| Platforms      | Command     |     | context |     | Authority            |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |               | port-priority |     |                         |     |     |
| ---------------- | ------------- | ------------- | --- | ----------------------- | --- | --- |
| spanning-tree    | port-priority |               |     | <PRIORITY-MULTIPLIER>   |     |     |
| no spanning-tree |               | port-priority |     | [<PRIORITY-MULTIPLIER>] |     |     |
Description
Configurestheportpriority.ThepriorityofaportcanbedifferentforeachMSTinstancetowhichit
belongs.
ThenoformofthecommandsetstheportpriorityforMSTinstance0tothedefaultof8.Thedefault
priorityvalueisderivedbymultiplying8by8.ForLAGinterfacesthedefaultis4.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<PRIORITY-MULTIPLIER> Specifiestheportpriorityasamultiplier.Default:8,exceptfor
LAGinterfaceswherethedefaultis4.Range:0to15.
ThepriorityrangeforaportinagivenMSTIis0to255.However,
thiscommandspecifiesthepriorityasamultiplier(0to15)of16.
Whenyouspecifyaprioritymultiplierof0to15,theactualpriority
assignedtotheswitchis:(priority-multiplier)x16.
Examples
Settingtheportpriorityto8oninterface1/1/1:
| switch(config)#    |     | interface |               | 1/1/1 |               |     |
| ------------------ | --- | --------- | ------------- | ----- | ------------- | --- |
| switch(config-if)# |     |           | spanning-tree |       | port-priority | 8   |
Settingtheportprioritytothedefaultoninterface1/1/1:
| switch(config)#    |             | interface |                  | 1/1/1 |               |     |
| ------------------ | ----------- | --------- | ---------------- | ----- | ------------- | --- |
| switch(config-if)# |             |           | no spanning-tree |       | port-priority |     |
| Command            | History     |           |                  |       |               |     |
| Release            |             |           |                  |       | Modification  |     |
| 10.07orearlier     |             |           |                  |       | --            |     |
| Command            | Information |           |                  |       |               |     |
174
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- |

| Platforms | Command |     | context | Authority |     |
| --------- | ------- | --- | ------- | --------- | --- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |           | port-type |                            |     |     |
| ---------------- | --------- | --------- | -------------------------- | --- | --- |
| spanning-tree    | port-type |           | {admin-edge|admin-network} |     |     |
| no spanning-tree |           | port-type | [admin-edge|admin-network] |     |     |
Description
SetstheSTPporttypefortheinterface.
Porttypesinclude:admin-edgeandadmin-network.
Thenoformofthecommandsetstheporttypetothedefaultofadmin-network.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
admin-edge Specifiestheporttypeasadministrativeedge.Duringspanning
treeestablishment,portswithadmin-edgeenabledtransition
immediatelytotheforwardingstate.
admin-network
Specifiestheporttypeasadministrativenetwork.Whenthis
optionisselected,theportlooksforBPDUsforthefirst3seconds.
Iftherearenone,theportisclassifiedasanedgeportand
immediatelystartsforwardingpackets.IfBPDUsareseenonthe
port,theportisclassifiedasanon-edgeportandnormalSTP
operationcommencesonthatport.
Examples
Settingtheporttypetoadmin-edgeoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1         |           |            |
| ------------------ | --- | --------- | ------------- | --------- | ---------- |
| switch(config-if)# |     |           | spanning-tree | port-type | admin-edge |
Settingtheporttypetoadmin-networkoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1         |           |               |
| ------------------ | --- | --------- | ------------- | --------- | ------------- |
| switch(config-if)# |     |           | spanning-tree | port-type | admin-network |
Settingtheporttypetothedefaultofadmin-networkoninterface1/1/1:
| switch(config)#    |             | interface | 1/1/1            |              |     |
| ------------------ | ----------- | --------- | ---------------- | ------------ | --- |
| switch(config-if)# |             |           | no spanning-tree | port-type    |     |
| Command            | History     |           |                  |              |     |
| Release            |             |           |                  | Modification |     |
| 10.07orearlier     |             |           |                  | --           |     |
| Command            | Information |           |                  |              |     |
Spanningtreeprotocols(STP)|175

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | priority |                         |     |
| ---------------- | -------- | ----------------------- | --- |
| spanning-tree    | priority | <PRIORITY-MULTIPLIER>   |     |
| no spanning-tree | priority | [<PRIORITY-MULTIPLIER>] |     |
Description
Configurestheswitch(bridge)priorityforthedesignatedregioninwhichtheswitchresides.
Theswitchcomparesthisprioritywiththeprioritiesofotherswitchesinthesameregiontodetermine
therootswitchfortheregion.Thelowerthepriorityvalue,thehigherthepriority.
Thenoformofthiscommandsetsthebridgeprioritytothedefaultof8.Thedefaultpriorityvalueis
derivedbymultiplying8by4096.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<PRIORITY-MULTIPLIER> Specifiesthepriorityasamultiplier.Range:0to15.Default:8.
ThepriorityrangeforanMSTPswitchis0-61440.However,this
commandspecifiesthepriorityasamultiplier(0to15)of4096.
Thatis,whenyouspecifyaprioritymultipliervalueof0to15,the
actualpriorityassignedtotheswitchis:(priority-multiplier)x
4096.Forexample,with2asthepriority-multiplieronagiven
MSTPswitch,theswitchprioritysettingis8,192.
Usage
EveryswitchrunninganinstanceofMSTPhasaBridgeIdentifier,whichisauniqueidentifierthathelps
distinguishthisswitchfromallothers.TheswitchwiththelowestBridgeIdentifieriselectedastheroot
forthetree.TheBridgeIdentifieriscomposedofaconfigurableprioritycomponent(2bytes)andthe
bridge'sMACaddress(6bytes).Youcanchangetheprioritycomponentprovidesflexibilityin
determiningwhichswitchwillbetherootforthetree,regardlessofitsMACaddress.
Examples
Settingtheprioritymultiplierto12:
| switch(config)# | spanning-tree | priority | 12  |
| --------------- | ------------- | -------- | --- |
Settingtheprioritymultipliertothedefaultof8:
switch(config)#
|                     | no  | spanning-tree | priority     |
| ------------------- | --- | ------------- | ------------ |
| Command History     |     |               |              |
| Release             |     |               | Modification |
| 10.07orearlier      |     |               | --           |
| Command Information |     |               |              |
176
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

| Platforms | Command | context |     | Authority |
| --------- | ------- | ------- | --- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | root-guard |     |     |     |
| ---------------- | ---------- | --- | --- | --- |
| spanning-tree    | root-guard |     |     |     |
| no spanning-tree | root-guard |     |     |     |
Description
Enablestherootguardontheinterface.
Whenaportisenabledasroot-guard,itcannotbeselectedastherootportevenifitreceivessuperior
STPBPDUs.Theportisassignedan"alternate"portroleandentersablockingstateifitreceives
superiorMSTPBPDUs.
AsuperiorBPDUcontainsboth"better"informationontherootbridgeandpathcosttotherootbridge,
whichwouldnormallyreplacethecurrentrootbridgeselection.
Thenoformofthecommandsetstherootguardstatustothedefaultofdisabledontheinterface.
Examples
Enablingtherootguardoninterface1/1/1:
| switch(config)#    |     | interface     | 1/1/1 |            |
| ------------------ | --- | ------------- | ----- | ---------- |
| switch(config-if)# |     | spanning-tree |       | root-guard |
Disablingrootguardoninterface1/1/1:
| switch(config)#     |         | interface        | 1/1/1 |              |
| ------------------- | ------- | ---------------- | ----- | ------------ |
| switch(config-if)#  |         | no spanning-tree |       | root-guard   |
| Command History     |         |                  |       |              |
| Release             |         |                  |       | Modification |
| 10.07orearlier      |         |                  |       | --           |
| Command Information |         |                  |       |              |
| Platforms           | Command | context          |       | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | rpvst-filter |     |     |     |
| ---------------- | ------------ | --- | --- | --- |
| spanning-tree    | rpvst-filter |     |     |     |
| no spanning-tree | rpvst-filter |     |     |     |
Description
Spanningtreeprotocols(STP)|177

EnablestheRPVSTfilterfortheinterface.ThiscommandisonlyapplicabletoMSTPmode.Itisnot
applicabletoRPVST+mode.
WhentheRPVSTfilterisenabled,theingressingRPVSTproprietaryBPDUsaredroppedaftercopyingto
CPUwhereasthestandardIEEERPVSTBPDUsarestillallowed.Thishelpsinpreventingthefloodingof
RPVSTproprietaryBPDUsunderanMSTP-RPVSTinteropenvironment.
IftheneighboringswitchisrunningRPVSTthenthispairofswitcheswillnotconvergeasRPVSTBPDUswillnot
reachthem.
IfenablingRPVSTfiltercausesahightrafficload,shutdowntheportandreconfiguretheBPDUfilter
| withtheCLIcommand:no |     |          |      | rpvst-filter. |
| -------------------- | --- | -------- | ---- | ------------- |
|                      |     | spanning | tree |               |
RPVSTfilterisdisabledbydefault.
Example
EnablingtheRPVSTfilteroninterface1/1/1:
| switch#            | configure | terminal      |       |              |
| ------------------ | --------- | ------------- | ----- | ------------ |
| switch(config)#    |           | interface     | 1/1/1 |              |
| switch(config-if)# |           | spanning-tree |       | rpvst-filter |
DisablingRPVSTfilteroninterface1/1/1:
| switch#             | configure | terminal         |       |              |
| ------------------- | --------- | ---------------- | ----- | ------------ |
| switch(config)#     |           | interface        | 1/1/1 |              |
| switch(config-if)#  |           | no spanning-tree |       | rpvst-filter |
| Command History     |           |                  |       |              |
| Release             |           |                  |       | Modification |
| 10.07orearlier      |           |                  |       | --           |
| Command Information |           |                  |       |              |
| Platforms           | Command   | context          |       | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | rpvst-guard |     |     |     |
| ---------------- | ----------- | --- | --- | --- |
| spanning-tree    | rpvst-guard |     |     |     |
| no spanning-tree | rpvst-guard |     |     |     |
Description
EnablesRPVSTguardontheswitchinterface.ThiscommandisonlyapplicabletoMSTPmode.Itisnot
applicabletoRPVST+mode.
WhenRPVSTguardisenabledonaninterface,itwilldisablethatinterfaceifRPVSTBPDUsarereceived
onit.
ThenoformofthecommandsetstheRPVSTguardstatustothedefaultofdisabledontheinterface.
178
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

Example
EnablingRPVSTguardoninterface1/1/1:
switch#
configure terminal
| switch(config)#    |     | interface     | 1/1/1 |             |
| ------------------ | --- | ------------- | ----- | ----------- |
| switch(config-if)# |     | spanning-tree |       | rpvst-guard |
DisablingRPVSTguardoninterface1/1/1:
| switch#             | configure | terminal         |       |              |
| ------------------- | --------- | ---------------- | ----- | ------------ |
| switch(config)#     |           | interface        | 1/1/1 |              |
| switch(config-if)#  |           | no spanning-tree |       | rpvst-guard  |
| Command History     |           |                  |       |              |
| Release             |           |                  |       | Modification |
| 10.07orearlier      |           |                  |       | --           |
| Command Information |           |                  |       |              |
| Platforms           | Command   | context          |       | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | tcn-guard |     |     |     |
| ---------------- | --------- | --- | --- | --- |
| spanning-tree    | tcn-guard |     |     |     |
| no spanning-tree | tcn-guard |     |     |     |
Description
EnablestheTCN(TopologyChangeNotification)guardintheinterface.Whenenabledforaport,the
portstopspropagatingreceivedtopologychangenotificationsandtopologychangestootherports.
ThenoformofthecommandsetstheTCNguardstatustothedefaultofdisabledontheinterface.
Examples
EnablingTCNguardoninterface1/1/1:
| switch(config)#    |     | interface     | 1/1/1 |           |
| ------------------ | --- | ------------- | ----- | --------- |
| switch(config-if)# |     | spanning-tree |       | tcn-guard |
DisablingTCNguardoninterface1/1/1:
| switch(config)#    |     | interface        | 1/1/1 |           |
| ------------------ | --- | ---------------- | ----- | --------- |
| switch(config-if)# |     | no spanning-tree |       | tcn-guard |
| Command History    |     |                  |       |           |
Spanningtreeprotocols(STP)|179

| Release        |             |         | Modification |     |
| -------------- | ----------- | ------- | ------------ | --- |
| 10.07orearlier |             |         | --           |     |
| Command        | Information |         |              |     |
| Platforms      | Command     | context | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | transmit-hold-count |     |           |     |
| ---------------- | ------------------- | --- | --------- | --- |
| spanning-tree    | transmit-hold-count |     | <COUNT>   |     |
| no spanning-tree | transmit-hold-count |     | [<COUNT>] |     |
Description
SetsthemaximumnumberofBPDUspersecondthattheswitchcansendfromaninterface.
Thenoformofthiscommandsetsthetransmit-hold-counttothedefaultof6.
| Parameter |     |     | Description                                      |     |
| --------- | --- | --- | ------------------------------------------------ | --- |
| <COUNT>   |     |     | SpecifiesthenumberofBPDUsthatcanbesentpersecond. |     |
Range:1to10.Default:6.
Examples
Settingthetransmit-hold-countto5:
| switch(config)# | spanning-tree |     | transmit-hold-count | 5   |
| --------------- | ------------- | --- | ------------------- | --- |
Settingthetransmit-hold-counttothedefaultof6:
| switch(config)# | no          | spanning-tree | transmit-hold-count |     |
| --------------- | ----------- | ------------- | ------------------- | --- |
| Command         | History     |               |                     |     |
| Release         |             |               | Modification        |     |
| 10.07orearlier  |             |               | --                  |     |
| Command         | Information |               |                     |     |
| Platforms       | Command     | context       | Authority           |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree | trap |     |     |     |
| ------------- | ---- | --- | --- | --- |
180
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

spanning-tree trap {new-root|topology-change [instance <INSTANCE-ID>] |
errant-bpdu | root-guard-inconsistency | loop-guard-inconsistency}
no spanning-tree trap {new-root|topology-change [instance <INSTANCE-ID>] |
errant-bpdu | root-guard-inconsistency | loop-guard-inconsistency}
Description
EnablesSNMPtrapsfornewroot,topologychangeevent,errant-bpdureceivedevent,root-guard
inconsistency,andloop-guardinconsistencynotifications.Itisdisabledbydefault.
ThenoformofthiscommanddisablesthenotificationsforSNMPtraps.
| Parameter |     | Description                                        |     |
| --------- | --- | -------------------------------------------------- | --- |
| new-root  |     | EnablingSNMPnotificationwhenanewrootiselectedonany |     |
MSTinstanceontheswitch.
topology-change EnablingSNMPnotificationwhenatopologychangeeventoccurs
inthespecifiedMSTinstanceontheswitch.
<INSTANCE-ID> SpecifiestheinstanceIDforthetopologychangetrap.Range:0to
64.
errant-bpdu
EnablingSNMPnotificationwhenanerrantbpduisreceivedby
anyMSTinstanceontheswitch.
root-guard-inconsistency EnablingSNMPnotificationwhentheroot-guardfindstheport
inconsistentforanyMSTinstanceontheswitch.
loop-guard-inconsistency EnablingSNMPnotificationwhentheloop-guardfindstheport
inconsistentforanyMSTinstanceontheswitch.
Examples
EnablingthenotificationsfortheSNMPtraps:
| switch(config)# | spanning-tree | trap |     |
| --------------- | ------------- | ---- | --- |
new-root Enable notifications which are sent when a new root is
elected
topology-change Enable notifications which are sent when a topology
change occurs
errant-bpdu Enable notifications which are sent when an errant
bpdu is received
root-guard-inconsistency Enable notifications which are sent when root guard
| inconsistency | occurs |     |     |
| ------------- | ------ | --- | --- |
loop-guard-inconsistency Enable notifications which are sent when loop guard
| inconsistency   | occurs        |               |     |
| --------------- | ------------- | ------------- | --- |
| switch(config)# | spanning-tree | trap new-root |     |
<cr>
| switch(config)# | spanning-tree | trap topology-change |     |
| --------------- | ------------- | -------------------- | --- |
instance Enable topology change notification for the specified MST instance id.
| switch(config)# | spanning-tree | trap topology-change | instance |
| --------------- | ------------- | -------------------- | -------- |
<0-64> Enable topology change information on the specified instance id.
switch(config)#
|     | spanning-tree | trap topology-change | instance 1 |
| --- | ------------- | -------------------- | ---------- |
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
Spanningtreeprotocols(STP)|181

DisablingthenotificationsfortheSNMPtraps:
| switch(config)# | no  | spanning-tree | trap |     |
| --------------- | --- | ------------- | ---- | --- |
new-root Disable notifications which are sent when a new root
is elected
topology-change Disable notifications which are sent when a topology
| change occurs |     |     |     |     |
| ------------- | --- | --- | --- | --- |
errant-bpdu Disable notifications which are sent when an errant
| bpdu is | received |     |     |     |
| ------- | -------- | --- | --- | --- |
root-guard-inconsistency Disable notifications which are sent when root guard
| inconsistency | occurs |     |     |     |
| ------------- | ------ | --- | --- | --- |
loop-guard-inconsistency Disable notifications which are sent when loop guard
| inconsistency   | occurs |               |               |     |
| --------------- | ------ | ------------- | ------------- | --- |
| switch(config)# | no     | spanning-tree | trap new-root |     |
<cr>
| switch(config)# | no  | spanning-tree | trap topology-change |     |
| --------------- | --- | ------------- | -------------------- | --- |
instance Disable topology change notification for the specified MST instance
| switch(config)# | no  | spanning-tree | trap topology-change | instance |
| --------------- | --- | ------------- | -------------------- | -------- |
<0-64> Disable topology change information on the specified instance id
switch(config)# no spanning-tree trap topology-change instance 1
<cr>
| switch(config)# | no  | spanning-tree | trap errant-bpdu |     |
| --------------- | --- | ------------- | ---------------- | --- |
<cr>
| switch(config)# | no  | spanning-tree | trap root-guard-inconsistency |     |
| --------------- | --- | ------------- | ----------------------------- | --- |
<cr>
| switch(config)# | no  | spanning-tree | trap loop-guard-inconsistency |     |
| --------------- | --- | ------------- | ----------------------------- | --- |
<cr>
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
182
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

| MSTP | debugging |     | and | troubleshooting |     |     |     |     |     |
| ---- | --------- | --- | --- | --------------- | --- | --- | --- | --- | --- |
WhentherearesuspectedconvergenceproblemswithMSTPwithrespecttotrafficforwardingand
convergencetime,usetheinformationprovidedinthissectiontohelpsolvetheproblems.
Check the forwarding path for each instance configured, root elected, and root port
| for each | node. |     |     |     |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
a. Usecommandshowspanning-tree.Notethegreenhighlightsshowingtheitemsofinterest.
show spanning-tree
|     | Spanning | tree status | : Enabled | Protocol: | MSTP |     |     |     |     |
| --- | -------- | ----------- | --------- | --------- | ---- | --- | --- | --- | --- |
MST0
|     | Root   | ID Priority  | : 0                |             |                        |     |     |     |     |
| --- | ------ | ------------ | ------------------ | ----------- | ---------------------- | --- | --- | --- | --- |
|     |        | MAC-Address: | 10:10:10:10:10:10  |             |                        |     |     |     |     |
|     |        | Hello        | time(in seconds):2 |             | Max Age(in seconds):20 |     |     |     |     |
|     |        | Forward      | Delay(in           | seconds):15 |                        |     |     |     |     |
|     | Bridge | ID Priority  | : 32768            |             |                        |     |     |     |     |
|     |        | MAC-Address: | 8c:85:c1:5a:67:80  |             |                        |     |     |     |     |
|     |        | Hello        | time(in seconds):2 |             | Max Age(in seconds):20 |     |     |     |     |
|     |        | Forward      | Delay(in           | seconds):15 |                        |     |     |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-
Rx
--------- ------------ ---------- -------- ---------- ----------- -------- -------- -------- -----
---
|     | 1/1/12        | Designated  | Forwarding | 20000        | 128 | P2P 9       | 0   | 0   | 0   |
| --- | ------------- | ----------- | ---------- | ------------ | --- | ----------- | --- | --- | --- |
|     | 2/1/1         | Designated  | Forwarding | 20000        | 128 | P2P 9       | 0   | 0   | 0   |
|     | 2/1/12        | Designated  | Forwarding | 20000        | 128 | P2P 9       | 0   | 0   | 0   |
|     | 3/1/11        | Designated  | Forwarding | 200000       | 128 | P2P 9       | 0   | 0   | 0   |
|     | 3/1/12        | Root        | Forwarding | 20000        | 128 | P2P 9       | 0   | 0   | 0   |
|     | lag1          | Root        | Forwarding | 20000        | 64  | P2P Bound 4 | 7   | 2   | 1   |
|     | Number        | of topology | changes    | : 1          |     |             |     |     |     |
|     | Last topology | change      | occurred   | : 16 seconds | ago |             |     |     |     |
Check whether MSTP is configured with Intra or Intra-region configurations.
a. Modifytheconfigurationasrequired.Tomakeallnodesuseintra-regionconvergence,confirm
thattheseitemsarethesame.
|                | a. MST config      | ID              |              |                                    |     |     |     |     |     |
| -------------- | ------------------ | --------------- | ------------ | ---------------------------------- | --- | --- | --- | --- | --- |
|                | b. MST config      |                 |              |                                    |     |     |     |     |     |
|                | c. Instance        | IDtoMember      | VLANmapping. |                                    |     |     |     |     |     |
| Usecommandshow |                    | spanning-tree   |              | mst-config.                        |     |     |     |     |     |
|                | show spanning-tree |                 | mst-config   |                                    |     |     |     |     |     |
|                | MST configuration  |                 | information  |                                    |     |     |     |     |     |
|                | MST                | config ID       |              | : reg                              |     |     |     |     |     |
|                | MST                | config revision |              | : 1                                |     |     |     |     |     |
|                | MST                | config digest   |              | : 2D2BC9A32097B463C48EE1817673FA2D |     |     |     |     |     |
|                | Number             | of instances    |              | : 2                                |     |     |     |     |     |
Spanningtreeprotocols(STP)|183

|          | Instance        |     | ID  | Member                             | VLANs     |     |
| -------- | --------------- | --- | --- | ---------------------------------- | --------- | --- |
|          | --------------- |     |     | ---------------------------------- |           |     |
|          | 0               |     |     | 2,4-4094                           |           |     |
|          | 1               |     |     | 1                                  |           |     |
|          | 2               |     |     | 3                                  |           |     |
| Avoiding | VSX-related     |     |     | problems                           | with MSTP |     |
VSXrequiresthatSTPconfigurationbethesameonbothprimaryandsecondaryVSXswitches.TheSTP
configurationsintheglobalandmc-lag-interfacecontextsmustbethesameacrossVSXpairs.Youcan
configureidenticalSTPconfigurationsonboththeVSX-primaryandVSX-secondaryoralternativelyuse
thevsx-syncfeaturetosyncallSTPrelatedconfigurations.
ExampleconfigurationincludingthesynchronizationofMSTPglobalconfigurationfromVSX-Primaryto
| VSX-secondaryusingcommandvsx-sync |     |     |     |     | stp-global: |     |
| --------------------------------- | --- | --- | --- | --- | ----------- | --- |
spanning-tree
|     | spanning-tree |     | mode | mstp       |     |     |
| --- | ------------- | --- | ---- | ---------- | --- | --- |
|     | spanning-tree |     | vlan | 1-100      |     |     |
|     | spanning-tree |     | vlan | 1 priority | 10  |     |
...
vsx
|     | vsx-sync | stp-global |     |     |     |     |
| --- | -------- | ---------- | --- | --- | --- | --- |
Exampleconfigurationincludingthesynchronizationofmc-lagconfigurationfromVSX-PrimarytoVSX-
| secondaryusingcommandvsx-sync |               |     |            |         | mclag-interfaces: |     |
| ----------------------------- | ------------- | --- | ---------- | ------- | ----------------- | --- |
|                               | interface     | lag | 10 mc-lag  |         |                   |     |
|                               | spanning-tree |     | vlan       | 150-200 | cost 5000         |     |
|                               | spanning-tree |     | port-prio  |         | 8                 |     |
|                               | spanning-tree |     | admin-edge |         |                   |     |
|                               | spanning-tree |     | tcn-guard  |         |                   |     |
...
vsx
|      | vsx-sync | mclag-interfaces |     |     |     |     |
| ---- | -------- | ---------------- | --- | --- | --- | --- |
| MSTP | FAQ      |                  |     |     |     |     |
1. Are there any specific loop-prevention recommendations for access switches?
IftheaccessswitchispronetoreceivingexcessBPDUs,considerenablingRPVST+orMSTP.
| 2. What | is the | default |     | spanning | tree protocol | (STP) mode? |
| ------- | ------ | ------- | --- | -------- | ------------- | ----------- |
ThedefaultSTPmodeisMSTP.RPVST+isalsosupported.SettheSPTmodewithcommandspanning-
tree mode.
| 3. Can | RPVST+ | and | MSTP | switches | be interconnected? |     |
| ------ | ------ | --- | ---- | -------- | ------------------ | --- |
Yes.TointerconnecttypicallyusethedefaultVLAN1.ThisisbasedontheRFCforinterconnection.
4. What network-resiliency features are available for physical links?
TheIndustry-standardfeatureunidirectionallinkdetection(UDLDonfiberlinks)isavailable.
184
| AOS-CX10.12Layer-2BridgingGuide| |     |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | --- | ---------------- | --- | --- |

| 5. What | is the maximum | number | of STP hops | supported? |
| ------- | -------------- | ------ | ----------- | ---------- |
Themaximumis40.Thedefaultis20.
6. For MST 0 how do I change the priority so I can determine the Root and Secondary
| Root for | the CIST? |     |     |     |
| -------- | --------- | --- | --- | --- |
Usecommandspanning-tree priority.ForMST0,thedefaultpriorityis8.Tosetthepriorityofother
| STPinstances,usecommandspanning-tree |               |              | instance | priority.    |
| ------------------------------------ | ------------- | ------------ | -------- | ------------ |
| 7. Does                              | MSTP have any | per-platform | capacity | differences? |
Yes.Refertotheplatform-specificnumberofMSTP instancesunderSTPsupportedplatformsand
scale.
Spanningtreeprotocols(STP)|185

RPVST+ protocol and feature details
Rapid Per VLAN Spanning Tree+ (RPVST+) is an updated implementation of STP (Spanning Tree
Protocol). It enables the creation of a separate spanning tree for each VLAN on a switch, and ensures
that only one active, loop-free path exists between any two nodes on a given VLAN.

Spanning tree protocols are used to prevent loops from occurring when multiple paths exist between
the devices on a network. They are also used to provide redundancy, enabling data to use an alternative
path when one link to a device fails. For example, in the following topology several paths exist between
each switch.

Figure 14 RSTP topology with VLANs 10 and 20 blocked

The above topology has four switches running RSTP. Switch “A” is the root switch. To prevent a loop,
RSTP blocks the link between switch “B” and switch “D”. There are two VLANs in this network (VLAN 10
and VLAN 20). Since RSTP does not have VLAN intelligence, it forces all VLANs in a layer 2 domain to
follow the same spanning tree.

In the following topologies, there will not be any traffic through the link between switch “B” and switch
“D” and therefore the link bandwidth is wasted. On the other hand, RPVST+ runs different spanning
trees for different VLANs.

RVPST+ creates a spanning tree for VLAN 10.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

186

Figure 15 RPVST+ topology with VLAN 10 blocked

RVPST+ creates another spanning tree for VLAN 20.

Figure 16 RPVST+ topology with VLAN 20 blocked

The two topologies above are the same as the first topology, but now the switches run RPVST+ and can
span different trees for different VLANs. Switch A is the root switch for the VLAN 10 spanning tree and
switch D is the root switch for the VLAN 20 spanning tree. The link between switch B and switch D is only
blocked for VLAN 10 traffic but VLAN 20 traffic goes through that link. Similarly the link between switch
A and switch C is blocked only for VLAN 20 traffic but VLAN 10 traffic goes through that link. Here, traffic
passes through all the available links, and network availability and bandwidth utilization increase.

Spanning tree protocols (STP) | 187

The following topology shows a further example of shared links and redundant path-blocking in a
network running RPVST+.

Figure 17 RPVST+ topology with shared links and redundant path blocking

In the factory default configuration, spanning tree operation is disabled. For STP, MSTP, and RSTP,
configuration with default settings is automatic, and in many cases does not require any adjustments.
Configuring spanning tree mode as RPVST+ and then enabling spanning tree, requires that spanning
tree VLAN instances be enabled manually for the intended VLANS.

Also, the switch retains its currently configured spanning tree parameter settings when spanning tree is
disabled. Thus, if you disable, then later re-enable spanning tree, the parameter settings will be the
same as before spanning tree was disabled.

RPVST+ interoperates with devices that run legacy IEEE 802.1D STP and MSTP-IEEE 802.1s.

RPVST+ applies one RSTP tree per-VLAN. Each of these RSTP trees can have a different root switch and
span the network through shared or different links.

The switch automatically senses port identity and type, and automatically defines spanning tree parameters for

each type, and parameters that apply across the switch. Although these parameters can be adjusted, HPE

strongly recommends leaving these settings in their default configurations unless the proposed changes have

been supplied by an experienced network administrator who has a strong understanding of RPVST+ operation.

The switch supports 254 RPVST instances.

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

188

RPVST+ vPorts

When considering vPorts these are defined as active spanning tree VLANs that are declared on an
interface. As vPorts increase the load on the CPU and switch resources increase as more BPDUs are
processed.

In the following example core switch CoreA has four links with three VLANs on each link, for a total of
12 vPorts (4 links x 3 VLANs), allocated on the switch. The four access switches (Access A through
Access D) use three vPorts each.

Figure 18 RPVST+ topology with vPorts

Configuration of switch CoreA seen in the above topology:

Hostname CoreA
vlan 1,10-11,20-21
spanning-tree mode rpvst
spanning-tree
spanning-tree vlan 1,10,11,20,21
interface 1/1/1
no shutdown
no routing
vlan trunk native 1
vlan trunk allowed 10-11

interface 1/1/2
no shutdown
no routing
vlan trunk native 1
vlan trunk allowed 10-11

interface 1/1/3
no shutdown
no routing
vlan trunk native 1
vlan trunk allowed 20-21

interface 1/1/4
no shutdown
no routing
vlan trunk native 1
vlan trunk allowed 20-21

Spanning tree protocols (STP) | 189

| RPVST+ | configuration | tasks |     |     |     |
| ------ | ------------- | ----- | --- | --- | --- |
Procedure
1. SetRPVST+asthespanningtreemodewiththecommandspanning-tree mode rpvst.
2. Enablespanningtreewiththecommandspanning-tree.
3. ConfigurethelistofVLANsthatarepartofthespanningtreewiththecommandspanning-tree
vlan.
4. SetthepriorityforeachVLANwiththecommandspanning-tree vlan port-priority.Ifyoudo
notusethis,STP willusethedefaultpriority,
5. SettheportcostandpriorityforeachVLANwiththecommandsspanning-tree vlan costand
port-priority.Ifyoudonotdothis,STPwillinternallycalculateportcost
spanning-tree vlan
basedonthelinkspeedandsetportprioritytoitsdefaultvalue.
6. Formostdeployments,thedefaultvaluesforthefollowingsettingsdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
commands:
| RPVST+ | setting | Default | value Command | to change | it  |
| ------ | ------- | ------- | ------------- | --------- | --- |
IncludeVLANIDinspanningtree Enabled. spanning-tree extend-system-id
packets.
BlocklinkswhenVLANmismatchis Disabled. spanning-tree ignore-pvid-
detected. inconsistency
| STPlinktype. |     | Point-to-point. | spanning-tree | link-type |     |
| ------------ | --- | --------------- | ------------- | --------- | --- |
Supportextendedrangeofpathscosts Enabled. spanning-tree pathcost-type
forhigh-speedlinks.
Propagatetopologychangestoother Disabled. spanning-tree tcn-guard
ports.
| 7. ReviewRPVST+configurationsettingswiththecommandshow |     |     |     | tree. |     |
| ------------------------------------------------------ | --- | --- | --- | ----- | --- |
spanning
Example
Thisexamplecreatesthefollowingconfiguration:
n Setsthespanningtreemodetorpvst.
n Enablesspanningtree.
n DefinesspanningtreesupportforVLANs2-5.
n SetsthepriorityforeachVLAN.
| switch#         | config        |            |     |     |     |
| --------------- | ------------- | ---------- | --- | --- | --- |
| switch(config)# | spanning-tree | mode rpvst |     |     |     |
switch(config)# spanning-tree
| switch(config)# | spanning-tree | vlan 2-5        |     |     |     |
| --------------- | ------------- | --------------- | --- | --- | --- |
| switch(config)# | spanning-tree | vlan 2 priority | 5   |     |     |
| switch(config)# | spanning-tree | vlan 3 priority | 4   |     |     |
| switch(config)# | spanning-tree | vlan 4 priority | 3   |     |     |
190
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| switch(config)# |     | spanning-tree |     | vlan 5 | priority | 2   |     |     |
| --------------- | --- | ------------- | --- | ------ | -------- | --- | --- | --- |
switch(config)#
exit
| switch#          | show               | spanning-tree |       |            |           |     |       |     |
| ---------------- | ------------------ | ------------- | ----- | ---------- | --------- | --- | ----- | --- |
| Spanning         | tree               | status        |       | : Enabled  | Protocol: |     | RPVST |     |
| Extended         | System-id          |               |       | : Enabled  |           |     |       |     |
| Ignore           | PVID Inconsistency |               |       | : Disabled |           |     |       |     |
| Path cost        | method             |               |       | : Long     |           |     |       |     |
| RPVST-MSTP       | Interconnect       |               | VLAN  | : 1        |           |     |       |     |
| RPVST-Configured |                    | VLAN          |       | : all      |           |     |       |     |
| RPVST-Enabled    |                    | VLAN          |       | : 1        |           |     |       |     |
| Current          | Virtual            | Ports         | Count | : 28       |           |     |       |     |
| Maximum          | Allowed            | Virtual       | Ports | : 2048     |           |     |       |     |
VLAN1
| Root | ID  | Priority      | :        | 32768             |     |        |             |     |
| ---- | --- | ------------- | -------- | ----------------- | --- | ------ | ----------- | --- |
|      |     | MAC-Address:  |          | 38:21:c7:5c:df:c0 |     |        |             |     |
|      |     | Hello time(in |          | seconds):2        | Max | Age(in | seconds):20 |     |
|      |     | Forward       | Delay(in | seconds):15       |     |        |             |     |
VLAN2
| Root   | ID  | Priority      | :        | 20480             |      |        |             |      |
| ------ | --- | ------------- | -------- | ----------------- | ---- | ------ | ----------- | ---- |
|        |     | MAC-Address:  |          | 70:72:cf:38:21:e5 |      |        |             |      |
|        |     | This bridge   |          | is the root       |      |        |             |      |
|        |     | Hello time(in |          | seconds):2        | Max  | Age(in | seconds):20 |      |
|        |     | Forward       | Delay(in | seconds):15       |      |        |             |      |
| Bridge | ID  | Priority      | :        | 20480             |      |        |             |      |
|        |     | MAC-Address:  |          | 70:72:cf:38:21:e5 |      |        |             |      |
|        |     | Hello time(in |          | seconds):2        | Max  | Age(in | seconds):20 |      |
|        |     | Forward       | Delay(in | seconds):15       |      |        |             |      |
| Port   |     | Role          |          | State             | Cost |        | Priority    | Type |
------------ -------------- ------------ ------- ---------- ----------
| 1/1/1 |     | Designated |     | Forwarding | 20000 |     | 128 | point_to_point |
| ----- | --- | ---------- | --- | ---------- | ----- | --- | --- | -------------- |
VLAN3
| Root   | ID  | Priority      | :        | 16384             |      |        |             |      |
| ------ | --- | ------------- | -------- | ----------------- | ---- | ------ | ----------- | ---- |
|        |     | MAC-Address:  |          | 70:72:cf:38:21:e5 |      |        |             |      |
|        |     | This bridge   |          | is the root       |      |        |             |      |
|        |     | Hello time(in |          | seconds):2        | Max  | Age(in | seconds):20 |      |
|        |     | Forward       | Delay(in | seconds):15       |      |        |             |      |
| Bridge | ID  | Priority      | :        | 16384             |      |        |             |      |
|        |     | MAC-Address:  |          | 70:72:cf:38:21:e5 |      |        |             |      |
|        |     | Hello time(in |          | seconds):2        | Max  | Age(in | seconds):20 |      |
|        |     | Forward       | Delay(in | seconds):15       |      |        |             |      |
| Port   |     | Role          |          | State             | Cost |        | Priority    | Type |
------------ -------------- ------------ ------- ---------- ----------
| 1/1/1 |     | Designated |     | Forwarding | 20000 |     | 128 | point_to_point |
| ----- | --- | ---------- | --- | ---------- | ----- | --- | --- | -------------- |
VLAN4
| Root   | ID  | Priority      | :        | 12288             |     |        |             |     |
| ------ | --- | ------------- | -------- | ----------------- | --- | ------ | ----------- | --- |
|        |     | MAC-Address:  |          | 70:72:cf:38:21:e5 |     |        |             |     |
|        |     | This bridge   |          | is the root       |     |        |             |     |
|        |     | Hello time(in |          | seconds):2        | Max | Age(in | seconds):20 |     |
|        |     | Forward       | Delay(in | seconds):15       |     |        |             |     |
| Bridge | ID  | Priority      | :        | 12288             |     |        |             |     |
|        |     | MAC-Address:  |          | 70:72:cf:38:21:e5 |     |        |             |     |
|        |     | Hello time(in |          | seconds):2        | Max | Age(in | seconds):20 |     |
Spanningtreeprotocols(STP)|191

|     |      |     | Forward |     | Delay(in | seconds):15 |      |     |          |      |
| --- | ---- | --- | ------- | --- | -------- | ----------- | ---- | --- | -------- | ---- |
|     | Port |     | Role    |     |          | State       | Cost |     | Priority | Type |
------------ -------------- ------------ ------- ---------- ----------
|     | 1/1/1 |     | Designated |     |     | Forwarding | 20000 |     | 128 | point_to_point |
| --- | ----- | --- | ---------- | --- | --- | ---------- | ----- | --- | --- | -------------- |
VLAN5
|     | Root   | ID  | Priority     |         | : 8192            |             |      |        |             |      |
| --- | ------ | --- | ------------ | ------- | ----------------- | ----------- | ---- | ------ | ----------- | ---- |
|     |        |     | MAC-Address: |         | 70:72:cf:38:21:e5 |             |      |        |             |      |
|     |        |     | This         | bridge  | is                | the root    |      |        |             |      |
|     |        |     | Hello        | time(in | seconds):2        |             | Max  | Age(in | seconds):20 |      |
|     |        |     | Forward      |         | Delay(in          | seconds):15 |      |        |             |      |
|     | Bridge | ID  | Priority     |         | : 8192            |             |      |        |             |      |
|     |        |     | MAC-Address: |         | 70:72:cf:38:21:e5 |             |      |        |             |      |
|     |        |     | Hello        | time(in | seconds):2        |             | Max  | Age(in | seconds):20 |      |
|     |        |     | Forward      |         | Delay(in          | seconds):15 |      |        |             |      |
|     | Port   |     | Role         |         |                   | State       | Cost |        | Priority    | Type |
------------ -------------- ------------ ------- ---------- ----------
|         | 1/1/1 |        | Designated |             |     | Forwarding | 20000 |     | 128 | point_to_point |
| ------- | ----- | ------ | ---------- | ----------- | --- | ---------- | ----- | --- | --- | -------------- |
| Viewing |       | RPVST+ |            | information |     |            |       |     |     |                |
Prerequisites
Thesecommandsareinthemanagercontext,asindicatedbytheswitch#prompt.
Procedure
ToviewvariousaspectsofRPVST+information,usethefollowingcommands.
n Toviewinformationonspanning-treemodeandtheRPVST+instances,use:
|     | show | spanning-tree |     |     |     |     |     |     |     |     |
| --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
n Toviewinformationonspanning-treemodeandtheRPVST+instanceofaspecificVLAN,use:
|     | show | spanning-tree |     | vlan |     |     |     |     |     |     |
| --- | ---- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
n Toviewasummaryofthespanning-treeconfigurationsrelatedtoaport,use:
|     | show | spanning-tree |     | summary | port |     |     |     |     |     |
| --- | ---- | ------------- | --- | ------- | ---- | --- | --- | --- | --- | --- |
n Toviewasummaryofthespanning-treeconfigurations,use:
|        | show | spanning-tree  |     | summary | root |     |      |           |     |     |
| ------ | ---- | -------------- | --- | ------- | ---- | --- | ---- | --------- | --- | --- |
| RPVST+ |      | Considerations |     |         |      | and | best | practices |     |     |
n ForthebestRPVST+experience,useatleastAOS-CX10.07.
n AsthenumberofVLANsincreaseinanRPVST+environmenttheconsumptionofswitchresources
increasesandyoushouldthereforeconsiderreducingVLANsprawl.IfVLANincreasesarerequired
andcanbemappedsensibly,considerusingMST
n DonotexceedtheavailablenumberofVLANsorvPortssupportedonyourswitch
CheckthenumberofRPVST+VLANsandvPortscurrentlyinuseandthemaximumnumberavailable
n
|     | usingcommandshow |     |     | capacities-status |     |     | rpvstlikethis: |     |     |     |
| --- | ---------------- | --- | --- | ----------------- | --- | --- | -------------- | --- | --- | --- |
192
| AOS-CX10.12Layer-2BridgingGuide| |     |     |     | 8400SwitchSeries |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |

switch# show capacities-status rpvst

System Capacities Status: Filter rpvst
Value Maximum
Capacities Status Name
------------------------------------------------------------------------------
Number of RPVST VLANs currently configured
Number of RPVST Vports currently configured

254
2048

3
9

n Only select the VLANs required on a specific link for the allowed list based on the requirement on

each port. For example for a link using VLANs 10,11,12 and 15 use command vlan trunk 10-12,15.

n To whatever degree possible, avoid using the catch all command vlan trunk allowed all.

n Topology Change Notifications (TCN) are an important part of STP. However, reducing unwanted
TCNs is important for things such as access ports which can go up and down with end-point
attachment and detachment at the network edge. It is recommended to use command spanning-
tree port-type admin-edge to remove unwanted TCNs from end points.

n The use of spanning tree Topology Change Notification (TCN) guard may also be used in certain

circumstances using command spanning-tree tcn-guard.

o If the access switch is rebooting or the link between access and core switches is flapping, then this
will cause TCNs towards the network core. Any TC on any interface on the core will clear all MACs
locally and propagate the TC on all other interfaces. This can cause a significant traffic disruption
on the network. If the network has a loop-free topology and mac-flush is not really needed on all
switches in the network, then it can be feasible to add tcn-guard on access switches facing L2
interfaces. This will avoid mac-flush and TC propagation on the core switch (STP root switch).

o If a core or aggregation switch in the network keeps getting TC messages due to unpredictable
behavior of an access switch, TCN guard can be applied (using command spanning-tree tcn-
guard) to the core or aggregation switch on the Layer 2 link facing the access switch.

n Stability in a spanning tree environment is paramount. It is recommended that default timers be

used, and any alteration of timers be carried out only under special circumstances and in
consultation with experts.

n Avoid automatic placement of root bridges. To enable a deterministic, predictable, and stable
network, the placement of Primary and Secondary root bridges should be considered using
command spanning-tree vlan <VALUE> priority <VALUE>.

n To further provide stability and deterministic behavior additional security configuration should be

considered, such as:

o root-guard: Sets a port to ignore superior BPDUs to prevent it from becoming the root port. This
is typically carried out between the core that is required to be the root and access switches to
prevent ports that are not expected to originate root information such as server ports and access
switch ports.

o rpvst-guard: Disables the specific port if the port receives RPVST+ BPDUs. This will be on well-
defined ports that are known from your network design on which you never expect RPVST+
BPDUs. For example, user access ports or ports connected to servers in the datacenter where
other switches may exist, and technicians can inadvertently patch into.

o bpdu-guard: Disables the specific port if the port receives STP BPDUs. This is done to prevent any
inadvertent spanning tree or malicious attack, or switches being connected to the network and
causing STP processing. This will be on well-defined ports that are known from your network
design on which you never expect BPDUs. For example, user access ports or ports connected to
servers in the datacenter where other switches may exist, and technicians can inadvertently patch
into.

Spanning tree protocols (STP) | 193

n WithVSXconfigurationitisadvisablethateithertheVSXpairactsasaSTProotswitchorthattheSTP
rootswitchisreachableonlythroughmc-lags.AnSTProotswitchconnectedtoaVSXpairwith
standaloneinterfaces(non-mc-lags)isnotrecommended.
n ForRPVSTautoVLAN,onlypriorityconfigurationissupported.Otherconfigurationssuchasforward-
delay,hello-time,max-age,cost,port-priority,andtopology-changetraparenotconfigurable.These
willhavedefaultvalueswhilerunninginanRPVSTautoVLANspanningtreeinstance.
| RPVST+ | use cases |               |              |
| ------ | --------- | ------------- | ------------ |
| RPVST+ | use case: | Deterministic | root bridges |
AsmentionedinRPVST+Considerationsandbestpractices,theplacementofrootbridgesisimportantin
theLayer2networkdomain.HavingdeterministicRootandSecondaryRootbridgesisatypically-
accepteddesignthatallowsyoutoprovidepredictabilityandprotectioninyournetwork.
TheRootandSecondaryrootaretypicallyplacedattheCoreoftheLayer2domain. Figure19,
Deterministicrootbridges(physical)showsthephysicaltopologyand Figure20,Deterministicroot
bridges(logical)showsthelogicaltopology.SwitchAandSwitchBarethecore/centeroftheLayer2
domain,andtheyproviderootredundancyforeachother.
| Figure19 | Deterministicrootbridges(physical) |     |     |
| -------- | ---------------------------------- | --- | --- |
194
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

Figure20 Deterministicrootbridges(logical)
InthisexamplenetworktherearefourVLANsandeachVLANhasitsownindependenttopology.The
rootbridgesandVLANsareasfollows:
n VLAN10RootbridgeSwitchA,SecondaryRootbridgeSwitchB
n VLAN11RootbridgeSwitchA,SecondaryRootbridgeSwitchB
n VLAN20RootbridgeSwitchB,SecondaryRootbridgeSwitchA
n VLAN21RootbridgeSwitchB,SecondaryRootbridgeSwitchA
SwitchesAthroughDareconfiguredasfollows:
Inthefollowingswitchconfigurationcommandsequences,configurationportions(typicallydefault)unrelatedto
RPVST+arerepresentedbyanellipsis"...".Also,descriptivecomments,precededby"<---",areincludedtothe
rightofsomecommands.
Switch A configuration
n AddVLANs10,11,20,21.
n ConfigureRPVST+makingSwitchAtherootforVLANs10and11andthesecondaryrootforVLANs
20,21.
n AllowtherequiredVLANsforinterfaces1/1/1to1/1/3.
SwitchA#
...
vlan 10-11,20-21
| spanning-tree | mode rpvst | <-- Enable | RPVST+ |     |
| ------------- | ---------- | ---------- | ------ | --- |
spanning-tree
| spanning-tree | vlan 10-11,20-21 | <-- Define | VLANs for | RPVST+ |
| ------------- | ---------------- | ---------- | --------- | ------ |
spanning-tree vlan 10 priority 1 <-- Make Switch A Root Bridge for VLANs
| spanning-tree | vlan 11 priority | 1   |     |     |
| ------------- | ---------------- | --- | --- | --- |
spanning-tree vlan 20 priority 2 <-- Make Switch A Secondary Root Bridge for
VLANs
| spanning-tree | vlan 21 priority | 2   |     |     |
| ------------- | ---------------- | --- | --- | --- |
...
| interface  | 1/1/1       |              |          |                    |
| ---------- | ----------- | ------------ | -------- | ------------------ |
|            |             | <-- Allocate | required | VLANs to interface |
| vlan trunk | 10-11,20-21 |              |          |                    |
| vlan trunk | native 1    |              |          |                    |
| interface  | 1/1/2       |              |          |                    |
| vlan trunk | 10-11,20-21 |              |          |                    |
| vlan trunk | native 1    |              |          |                    |
| interface  | 1/1/3       |              |          |                    |
| vlan trunk | 10-11,20-21 |              |          |                    |
Spanningtreeprotocols(STP)|195

| vlan trunk | native 1 |     |
| ---------- | -------- | --- |
...
Switch B configuration
n AddVLANs10,11,20,21.
n ConfigureRPVST+makingSwitchBtherootforVLANs20,21,andthesecondaryrootforVLANs10,
11.
n Configurethetrunk-requiredVLANsforinterfaces1/1/1to1/1/3.
SwitchB#
...
vlan 10-11,20-21
| spanning-tree | mode rpvst |     |
| ------------- | ---------- | --- |
spanning-tree
| spanning-tree | vlan 10-11,20-21 |     |
| ------------- | ---------------- | --- |
| spanning-tree | vlan 10 priority | 2   |
| spanning-tree | vlan 11 priority | 2   |
| spanning-tree | vlan 20 priority | 1   |
| spanning-tree | vlan 21 priority | 1   |
...
| interface  | 1/1/1       |     |
| ---------- | ----------- | --- |
| vlan trunk | 10-11,20-21 |     |
| vlan trunk | native 1    |     |
| interface  | 1/1/2       |     |
| vlan trunk | 10-11,20-21 |     |
| vlan trunk | native 1    |     |
| interface  | 1/1/3       |     |
| vlan trunk | 10-11,20-21 |     |
| vlan trunk | native 1    |     |
...
| Switch C and D | configuration |     |
| -------------- | ------------- | --- |
n DefinetheVLANSforRPVST+andthetrunk-requiredVLANSusingthesameconfigurationonbothC
andDexceptforthehostname.
vlan 10-11,20-21
exit
| spanning-tree | mode rpvst |     |
| ------------- | ---------- | --- |
spanning-tree
| spanning-tree | vlan 10-11,20-21 |     |
| ------------- | ---------------- | --- |
int 1/1/2-1/1/3
| vlan trunk | 10-11,20-21 |     |
| ---------- | ----------- | --- |
| vlan trunk | native 1    |     |
exit
...
vlan 10-11,20-21
| spanning-tree | mode rpvst |     |
| ------------- | ---------- | --- |
spanning-tree
| spanning-tree | vlan 10-11,20-21 |     |
| ------------- | ---------------- | --- |
...
| interface  | 1/1/2       |     |
| ---------- | ----------- | --- |
| vlan trunk | 10-11,20-21 |     |
| vlan trunk | native 1    |     |
| interface  | 1/1/3       |     |
| vlan trunk | 10-11,20-21 |     |
196
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| vlan trunk | native | 1   |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
...
| Checking the | configuration |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
Theappliedconfigurationscanbecheckedasfollows:
CheckingRPVST+
n
n CheckingthattheSystemIDmatchesRootfortheVLAN.
| Checking Switch | A   |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Usecommandshow spanning-tree summary root.Asseenhere,SwitchAisRootforVLAN10and11,
identifiedbytheSystemID,andVLAN20and21RootisanotherdevicewhichisexpectedtobeSwitchB
basedonpreviousconfigurations.
NoticethezeroRootPortcostindicatedinthefirsttworowsofoutput.
| SwitchA#show | spanning-tree |     | summary root      |     |        |     |     |     |
| ------------ | ------------- | --- | ----------------- | --- | ------ | --- | --- | --- |
| STP status   |               | :   | Enabled           |     |        |     |     |     |
| Protocol     |               | :   | RPVST             |     |        |     |     |     |
| System       | ID            | :   | 08:00:09:8a:14:fa | <-- | System | ID  |     |     |
Root bridge for VLANs : 10,11 <-- Identify root bridges for VLANs
|      |          |         |     | Root Hello | Max      | Fwd |      |      |
| ---- | -------- | ------- | --- | ---------- | -------- | --- | ---- | ---- |
| VLAN | Priority | Root ID |     | cost       | Time Age | Dly | Root | Port |
-------- -------- ----------------- --------- ----- --- --- ------------
| VLAN10          | 4096 | 08:00:09:8a:14:fa |     | 0     | 2   | 20 15 |       | 0   |
| --------------- | ---- | ----------------- | --- | ----- | --- | ----- | ----- | --- |
| VLAN11          | 4096 | 08:00:09:8a:14:fa |     | 0     | 2   | 20 15 |       | 0   |
| VLAN20          | 4096 | 08:00:09:12:8e:9e |     | 20000 | 2   | 20 15 | 1/1/1 |     |
| VLAN21          | 4096 | 08:00:09:12:8e:9e |     | 20000 | 2   | 20 15 | 1/1/1 |     |
| Checking Switch | B    |                   |     |       |     |       |       |     |
Asseenhere,SwitchBisRootforVLAN20and21identifiedbytheSystemID,andVLAN10and11Root
isSwitchAidentifiedbytheSystemID.
| SwitchA#show | spanning-tree |         | summary root      |            |          |     |      |      |
| ------------ | ------------- | ------- | ----------------- | ---------- | -------- | --- | ---- | ---- |
| STP status   |               | :       | Enabled           |            |          |     |      |      |
| Protocol     |               | :       | RPVST             |            |          |     |      |      |
| System       | ID            | :       | 08:00:09:12:8e:9e |            |          |     |      |      |
| Root bridge  | for           | VLANs : | 20,21             |            |          |     |      |      |
|              |               |         |                   | Root Hello | Max      | Fwd |      |      |
| VLAN         | Priority      | Root ID |                   | cost       | Time Age | Dly | Root | Port |
-------- -------- ----------------- --------- ----- --- --- ------------
| VLAN10            | 4096 | 08:00:09:8a:14:fa |     | 20000 | 2   | 20 15 | 1/1/1 |     |
| ----------------- | ---- | ----------------- | --- | ----- | --- | ----- | ----- | --- |
| VLAN11            | 4096 | 08:00:09:8a:14:fa |     | 20000 | 2   | 20 15 | 1/1/1 |     |
| VLAN20            | 4096 | 08:00:09:12:8e:9e |     | 0     | 2   | 20 15 |       | 0   |
| VLAN21            | 4096 | 08:00:09:12:8e:9e |     | 0     | 2   | 20 15 |       | 0   |
| Checking Switches | C    | and D             |     |       |     |       |       |     |
Althoughnotillustrated,SwitchesCandDcanbecheckedinasimilarmannertotheotherswitches.
| Observe port | behavior | and | state |     |     |     |     |     |
| ------------ | -------- | --- | ----- | --- | --- | --- | --- | --- |
Spanningtreeprotocols(STP)|197

Wecanobservetheportbehaviorandstateusingcommandshow spanning-tree.Thetopologyin
Figure20,Deterministicrootbridges(logical)foreachswitchcanbeobservedshowingaloopfreeLayer
2topology.ThefollowingcommandsequencesfocusonVLAN10.
| Observing | Switch A | for VLAN 10 |     |     |     |
| --------- | -------- | ----------- | --- | --- | --- |
Usecommandshow spanning-tree.Asseenhere,allportsshownonSwitchA,theRootBridgefor
| VLAN10,areDesignated |                    | Forwardingasexpected. |     |     |     |
| -------------------- | ------------------ | --------------------- | --- | --- | --- |
| SwitchA#             | show spanning-tree | vlan 10               |     |     |     |
VLAN10
| Spanning | tree status :    | Enabled Protocol: | RPVST                  |     |     |
| -------- | ---------------- | ----------------- | ---------------------- | --- | --- |
| Root     | ID Priority      | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | This bridge      | is the root       |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
| Bridge   | ID Priority      | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- ---------
| 1/1/1     | Designated               | Forwarding     | 20000 128 P2P | 2586 533 | 10 8 |
| --------- | ------------------------ | -------------- | ------------- | -------- | ---- |
| 1/1/2     | Designated               | Forwarding     | 20000 128 P2P | 2679 434 | 5 7  |
| 1/1/3     | Designated               | Forwarding     | 20000 128 P2P | 3106 5   | 6 2  |
| Number    | of topology changes      | : 6            |               |          |      |
| Last      | topology change occurred | : 4828 seconds | ago           |          |      |
| Observing | Switch B                 | for VLAN 10    |               |          |      |
Asseenhere,theRootBridgeforVLAN10isidentifiedbyitsMACaddress“08:00:09:8a:14:fa”whichis
SwitchA.TheportconnectingtoSwitchA1/1/1istheRootportandForwardingandtheothertwo
portsareDesignated ForwardingleadingtoSwitchCandDrespectively.AllportsfollowtheVLAN10
topology(asseeninUsecase:Deterministicrootbridgesexamplenetwork)asexpected.
| SwitchB# | show spanning-tree | vlan 10 |     |     |     |
| -------- | ------------------ | ------- | --- | --- | --- |
VLAN10
| Spanning | tree status :    | Enabled Protocol: | RPVST                  |     |     |
| -------- | ---------------- | ----------------- | ---------------------- | --- | --- |
| Root     | ID Priority      | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
| Bridge   | ID Priority      | : 8192            |                        |     |     |
|          | MAC-Address:     | 08:00:09:12:8e:9e |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- ---------
| 1/1/1 | Root       | Forwarding | 20000 128 P2P | 537 2770 | 8 9 |
| ----- | ---------- | ---------- | ------------- | -------- | --- |
| 1/1/2 | Designated | Forwarding | 20000 128 P2P | 3298 7   | 6 2 |
| 1/1/3 | Designated | Forwarding | 20000 128 P2P | 3298 9   | 9 3 |
198
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

Number of topology changes

: 3

Last topology change occurred : 5247 seconds ago

Spanning tree protocols (STP) | 199

| Observing | Switch C | for VLAN 10 |     |     |     |
| --------- | -------- | ----------- | --- | --- | --- |
Asseenhere,theRootBridgeforVLAN10isidentifiedbyitsMACaddress“08:00:09:8a:14:fa”whichis
SwitchA.TheportconnectingtoSwitchA1/1/2istheRootportandForwarding,andtheotherport
1/1/3towardsSwitchBisAlternate BlockingpreventingaloopedtopologyforVLAN10.Althoughnot
illustrated,SwitchDcanbeobservedinasimilarmanner.
| SwitchC# | show spanning-tree | vlan 10 |     |     |     |
| -------- | ------------------ | ------- | --- | --- | --- |
VLAN10
| Spanning | tree status :    | Enabled Protocol: | RPVST                  |     |     |
| -------- | ---------------- | ----------------- | ---------------------- | --- | --- |
| Root     | ID Priority      | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
| Bridge   | ID Priority      | : 32768           |                        |     |     |
|          | MAC-Address:     | 08:00:09:16:7b:7e |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- ---------
| 1/1/2  | Root                     | Forwarding     | 20000 128 P2P | 438 3553 | 7 4 |
| ------ | ------------------------ | -------------- | ------------- | -------- | --- |
| 1/1/3  | Alternate                | Blocking       | 20000 128 P2P | 9 3986   | 3 8 |
| Number | of topology changes      | : 5            |               |          |     |
| Last   | topology change occurred | : 6811 seconds | ago           |          |     |
| RPVST+ | use case:                | BPDU           | protection    |          |     |
Varioussecuritymechanismsareinplacetoprotectspanningtrueconfigurationsfrominterferenceand
roguedevicesorunwarrantedchangestothenetwork.BPDUprotectionsecurestheactivetopologyby
preventingspoofedBPDUpacketsfromenteringthenetwork.Typically,BPDUprotectionisappliedon
edgeportsconnectedtoenduserdevicesthatdonotrunSTP.IfSTPBPDUpacketsarereceivedona
protectedport,BPDUguarddisablestheportandanalertissent.Asshownin Figure21,Roguedevice
needingBPDUguardwehavearougedeviceattemptingtoconnecttoSwitchDport1/1/8.
Figure21
RoguedeviceneedingBPDUguard
BPDUguardisconfiguredonswitchD.
200
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

SwitchD#
config
| interface | 1/1/8 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
no routing
| vlan          | access | 10         |     |     |     |
| ------------- | ------ | ---------- | --- | --- | --- |
| spanning-tree |        | bpdu-guard |     |     |     |
exit
Usecommandshow spanning-tree summary vlan 10toobservethatport1/1/8isdisabledbecause
BPDUwasreceivedonitfromtherogueswitch.
Noticehowport1/1/8isdisableddueto"Bpdu-Error."A timeoutcanbeconfiguredtore-enablethe
port.
| SwitchD# | show spanning-tree | vlan 10 |     |     |     |
| -------- | ------------------ | ------- | --- | --- | --- |
VLAN10
| Spanning | tree status :    | Enabled Protocol: | RPVST                  |     |     |
| -------- | ---------------- | ----------------- | ---------------------- | --- | --- |
| Root ID  | Priority         | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
| Bridge   | ID Priority      | : 32768           |                        |     |     |
|          | MAC-Address:     | 08:00:09:ee:11:82 |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- ---------
| 1/1/2         | Root             | Forwarding  | 20000 128 P2P | 580 1237 | 400 395 |
| ------------- | ---------------- | ----------- | ------------- | -------- | ------- |
| 1/1/3         | Alternate        | Blocking    | 40001 128 P2P | 214 1057 | 212 303 |
| 1/1/8         | Disabled         | Bpdu-Error  | 20000 128 P2P | 81 0     | 0 0     |
| Number of     | topology changes | : 307       |               |          |         |
| Last topology | change occurred  | : 2 seconds | ago           |          |         |
Usecommandshow 1/1/8toobservetheinterfacestate.Noticethatport1/1/8isdownas
int
expectedduetoBPDUerror.
| SwitchD#show | int      | 1/1/8   |     |     |     |
| ------------ | -------- | ------- | --- | --- | --- |
| Interface    | 1/1/8    | is down |     |     |     |
| Admin        | state is | up      |     |     |     |
State information:
| Link | state: down  |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- |
| Link | transitions: | 0   |     |     |     |
Description:
| Hardware: | Ethernet, | MAC | Address: 08:00:09:ee:11:c4 |     |     |
| --------- | --------- | --- | -------------------------- | --- | --- |
MTU 1500
Type --
Full-duplex
| qos              | trust none   |        |     |     |     |
| ---------------- | ------------ | ------ | --- | --- | --- |
| Speed            | 1000 Mb/s    |        |     |     |     |
| Auto-negotiation |              | is off |     |     |     |
| Flow-control:    |              | off    |     |     |     |
| Error-control:   |              | off    |     |     |     |
| MDI              | mode: none   |        |     |     |     |
| VLAN             | Mode: access |        |     |     |     |
Spanningtreeprotocols(STP)|201

Access VLAN: 10

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

202

| RPVST+ | use case: | Root protection |
| ------ | --------- | --------------- |
Rootprotectionsecurestheactivetopologybypreventingotherswitchesfromdeclaringtheirabilityto
propagatesuperiorBPDUs,containingbothbetterinformationontherootbridgeandpathcosttothe
rootbridgewhichwouldnormallyreplacethecurrentrootbridgeselection.
Asillustratedin Figure22,Rootprotection,byaddingrootguardoninterfaces1/1/2and1/1/3ofboth
coreswitches(AandB),thesetwoswitchesareprotectedinthecoreandpreventpropagationof
superiorBPDUsfromtheaccesslayer.
| Figure22 | Rootprotection |     |
| -------- | -------------- | --- |
ConfiguringSwitchesAandB:
SwitchA#
config
| interface | 1/1/2         |            |
| --------- | ------------- | ---------- |
|           | spanning-tree | root-guard |
exit
| interface | 1/1/3         |            |
| --------- | ------------- | ---------- |
|           | spanning-tree | root-guard |
exit
SwitchB#
Config
| interface | 1/1/2         |            |
| --------- | ------------- | ---------- |
|           | spanning-tree | root-guard |
| interface | 1/1/3         |            |
|           | spanning-tree | root-guard |
exit
Toobservetheprotectionbehavior,wecan(inappropriately)makeswitchCtherootforVLAN10.
SwitchC#
config
Spanningtreeprotocols(STP)|203

spanning-tree vlan 10 priority 0 <-- Make Switch C Root for VLAN 10
exit
Noticehowasprotectionoccurs,VLAN10onbothSwitchAandBportsshowasAlternate Root-Inc
(AlternateRoot-Inconsistent).ThisactionmaintainsLayer2stabilitybyprotectingtherestofthe
networkfromthe(inaccurate)informationthatSwitchCissending“better”BPDUs.
SwitchA#
|     | show spanning-tree | vlan 10 |     |     |     |
| --- | ------------------ | ------- | --- | --- | --- |
VLAN10
| Spanning | tree status :    | Enabled Protocol: | RPVST                  |     |     |
| -------- | ---------------- | ----------------- | ---------------------- | --- | --- |
| Root ID  | Priority         | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | This bridge      | is the root       |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
| Bridge   | ID Priority      | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- ---------
| 1/1/1         | Designated       | Forwarding  | 20000 128 P2P | 1606 383 | 432 159 |
| ------------- | ---------------- | ----------- | ------------- | -------- | ------- |
| 1/1/2         | Alternate        | Root-Inc    | 20000 128 P2P | 1571 114 | 520 92  |
| 1/1/3         | Designated       | Forwarding  | 20000 128 P2P | 1567 172 | 447 167 |
| Number of     | topology changes | : 694       |               |          |         |
| Last topology | change occurred  | : 1 seconds | ago           |          |         |
SwitchB#
|     | show spanning-tree | vlan 10 |     |     |     |
| --- | ------------------ | ------- | --- | --- | --- |
VLAN10
| Spanning | tree status :    | Enabled Protocol: | RPVST                  |     |     |
| -------- | ---------------- | ----------------- | ---------------------- | --- | --- |
| Root ID  | Priority         | : 4096            |                        |     |     |
|          | MAC-Address:     | 08:00:09:8a:14:fa |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
| Bridge   | ID Priority      | : 8192            |                        |     |     |
|          | MAC-Address:     | 08:00:09:12:8e:9e |                        |     |     |
|          | Hello time(in    | seconds):2        | Max Age(in seconds):20 |     |     |
|          | Forward Delay(in | seconds):15       |                        |     |     |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- ---------
| 1/1/1         | Designated       | Learning    | 20000 128 P2P | 1127 551 | 608 125 |
| ------------- | ---------------- | ----------- | ------------- | -------- | ------- |
| 1/1/2         | Root             | Forwarding  | 20000 128 P2P | 1865 354 | 569 187 |
| 1/1/3         | Alternate        | Root-Inc    | 20000 128 P2P | 1717 479 | 627 88  |
| Number of     | topology changes | : 763       |               |          |         |
| Last topology | change occurred  | : 2 seconds | ago           |          |         |
Dependingonwhentheshowcommandisexecuted,itmayfirstshowtheprotectedportasDesignated
| BlockingbeforeitshowsitasAlternate |     |     | Root-Inc. |     |     |
| ---------------------------------- | --- | --- | --------- | --- | --- |
204
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| RPVST+ | use case: | Spanning | tree on | edge ports |     |
| ------ | --------- | -------- | ------- | ---------- | --- |
Whenusingspanningtreeandtakingintoconsiderationtheedgeofthenetworkportsthatprovide
connectivitytoendpoints,thenetworkshouldnottypicallyparticipateinspanningtree.Considerthis
topologythatshowsanendpointconnectedtoport1/1/8onSwitchD:
| Figure23 | Spanningtreeonedgeports |     |     |     |     |
| -------- | ----------------------- | --- | --- | --- | --- |
Endpointsthatconnecttoportsthatdoparticipateinspanningtree(STP)mayexperienceDHCP
assignmenttimeoutsorIPaddressassignmentdelaysplusextendedclientonboardingtimeand
authenticationissues.TheseproblemsoccurbecausetheportparticipatesinthefullSTPprocess.To
avoidsuchissuesconsidersettingtheportasaspanningtreeadministrativeedgeportbyusing
commandspanning-tree port-type admin-edge.Thiscommandremovestheportparticipationfrom
STPinteractionswhenonboardingdevices,enablingquickeronboarding.
Edgeportsstillneedtobeprotectedfrompossiblespanningtreeattacks.ForexampleBPDUguardcanbeused.
SeeRPVST+usecase:BPDUprotection.
Beforeconfiguringaportasspanningtreeadministrativeedge,theportconfigurationlookslikethis:
| interface | 1/1/8 |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- |
no shutdown
|     | vlan access   | 10         |     |     |     |
| --- | ------------- | ---------- | --- | --- | --- |
|     | spanning-tree | bpdu-guard |     |     |     |
TheportStateisForwardingandtheTypeisP2P(PointtoPoint)bydefault.
| switch# | show spanning-tree | vlan 10 |     |     |     |
| ------- | ------------------ | ------- | --- | --- | --- |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- --------
| 1/1/8 | Designated | Forwarding 2000000 | 128 | P2P 167 0 | 0 0 |
| ----- | ---------- | ------------------ | --- | --------- | --- |
Configuretheportasadminedgeasfollowswithcommandspanning-tree port-type admin-edge:
Spanningtreeprotocols(STP)|205

| interface | 1/1/8 |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- |
no shutdown
|     | vlan access   | 10         |            |     |     |     |
| --- | ------------- | ---------- | ---------- | --- | --- | --- |
|     | spanning-tree | bpdu-guard |            |     |     |     |
|     | spanning-tree | port-type  | admin-edge |     |     |     |
exit
NoticehowthattheportStateisnowForwardingandtheTypeisP2P Edgemeaningthattheportwill
gointotheforwardingstateandbypassthestandardSTPlisteningandlearningstates.
| switch# | show spanning-tree | vlan 10show | spanning-tree vlan 10 |     |     |     |
| ------- | ------------------ | ----------- | --------------------- | --- | --- | --- |
Port Role State Cost Priority Type BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
------------ -------------- ---------- -------------- ---------- ---------- ---------- ---------- ---------- --------
| 1/1/8  | Designated               | Forwarding  | 2000000 128 | P2P Edge 347 | 0 0 | 0   |
| ------ | ------------------------ | ----------- | ----------- | ------------ | --- | --- |
| Number | of topology changes      | : 0         |             |              |     |     |
| Last   | topology change occurred | : 0 seconds | ago         |              |     |     |
| RPVST+ | use case:                | Preventing  | loops       |              |     |     |
Inthisscenario,fourswitchesareinterconnected.VLANs10and20aredefinedonallswitches,causing
anetworkloop.
| Figure24 | Topologywithanundesiredloop |     |     |     |     |     |
| -------- | --------------------------- | --- | --- | --- | --- | --- |
Toeliminatetheloop,RPVST+isenabledandswitchAandBaredefinedashigh-priorityforVLAN10
and20respectively.RPVST+theneliminatestheloopbyassigningswitchAastherootforVLAN10and
switchBdesignatedastherootforVLAN20,andblockingaccessononeofthelinks.
206
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- |

Figure25 TopologywithloopeliminatedbyRPVST+
Procedure
1. ConfigureswitchA.
a. CreateVLANs1,10,and20.
switch#
config
| switch(config)# | vlan 1, | 10, 20 |     |
| --------------- | ------- | ------ | --- |
b. EnableRPVST+andassigntheVLANs10and20toit.Assignapriorityof5toVLAN10.This
willforceswitchAtobecometherootofthespanningtreeforVLAN10.
| switch(config)# | spanning-tree | mode rpvst       |     |
| --------------- | ------------- | ---------------- | --- |
| switch(config)# | spanning-tree |                  |     |
| switch(config)# | spanning-tree | vlan 10,20       |     |
| switch(config)# | spanning-tree | vlan 10 priority | 5   |
c. Defineinterfaces1/1/1and1/1/2.
| switch(config)#    | interface   | 1/1/1             |     |
| ------------------ | ----------- | ----------------- | --- |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | no routing  |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
| switch(config-if)# | interface   | 1/1/2             |     |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | no routing  |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
2. ConfigureswitchBandswitchCwiththesamesettings.
a. CreateVLANs1,10,and20.
switch# config
| switch(config)# | vlan 1, | 10, 20 |     |
| --------------- | ------- | ------ | --- |
b. EnableRPVST+andassigntheVLANs10and20toit.
| switch(config)# | spanning-tree | mode rpvst |     |
| --------------- | ------------- | ---------- | --- |
| switch(config)# | spanning-tree |            |     |
| switch(config)# | spanning-tree | vlan 10,20 |     |
c. Defineinterfaces1/1/1and1/1/2.
| switch(config)#    | interface   | 1/1/1 |     |
| ------------------ | ----------- | ----- | --- |
| switch(config-if)# | no shutdown |       |     |
| switch(config-if)# | no routing  |       |     |
Spanningtreeprotocols(STP)|207

| switch(config-if)# | vlan      | trunk native 1    |     |
| ------------------ | --------- | ----------------- | --- |
| switch(config-if)# | vlan      | trunk allowed all |     |
| switch(config-if)# | interface | 1/1/2             |     |
switch(config-if)#
no shutdown
| switch(config-if)# | no routing |                   |     |
| ------------------ | ---------- | ----------------- | --- |
| switch(config-if)# | vlan       | trunk native 1    |     |
| switch(config-if)# | vlan       | trunk allowed all |     |
3. ConfigureswitchD.
a. CreateVLANs1,10,and20.
switch# config
| switch(config)# | vlan 1, | 10, 20 |     |
| --------------- | ------- | ------ | --- |
b. EnableRPVST+andassigntheVLANs10and20toit.Assignapriorityof5toVLAN20.This
willforceswitchDtobecometherootofthespanningtreeforVLAN20.
| switch(config)# | spanning-tree | mode rpvst       |     |
| --------------- | ------------- | ---------------- | --- |
| switch(config)# | spanning-tree |                  |     |
| switch(config)# | spanning-tree | vlan 10,20       |     |
| switch(config)# | spanning-tree | vlan 20 priority | 5   |
c. Defineinterfaces1/1/1and1/1/2.
| switch(config)#    | interface   | 1/1/1             |     |
| ------------------ | ----------- | ----------------- | --- |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | no routing  |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
| switch(config-if)# | interface   | 1/1/2             |     |
| switch(config-if)# | no shutdown |                   |     |
| switch(config-if)# | no routing  |                   |     |
| switch(config-if)# | vlan        | trunk native 1    |     |
| switch(config-if)# | vlan        | trunk allowed all |     |
208
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| RPVST+              | commands   |            |           |     |     |
| ------------------- | ---------- | ---------- | --------- | --- | --- |
| clear spanning-tree |            | statistics |           |     |     |
| clear spanning-tree | statistics |            | [VLAN-ID] |     |     |
Description
ClearsthespanningtreeBPDUstatistics,eitherallstatisticsorthoserelatedtoaspecifiedVLAN.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
VLAN-ID
SpecifiestheVLANID.
Example
ClearingallspanningtreeBPDUstatistics:
| switch(config)# | clear | spanning-tree |     | statistics |     |
| --------------- | ----- | ------------- | --- | ---------- | --- |
ClearingspanningtreeBPDUstatisticsforaparticularVLAN:
| switch(config)#     | clear   | spanning-tree |     | statistics   | 10  |
| ------------------- | ------- | ------------- | --- | ------------ | --- |
| Command History     |         |               |     |              |     |
| Release             |         |               |     | Modification |     |
| 10.07orearlier      |         |               |     | --           |     |
| Command Information |         |               |     |              |     |
| Platforms           | Command | context       |     | Authority    |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| show capacities | rpvst |     |     |     |     |
| --------------- | ----- | --- | --- | --- | --- |
| show capacities | rpvst |     |     |     |     |
Description
ShowsthecapacitiesofRPVST VLANsconfigurableonasystemandRPVSTVPORTssupportedina
system.
Examples
Showingcapacities:
| switch#           | show capacities |          | rpvst |     |     |
| ----------------- | --------------- | -------- | ----- | --- | --- |
| System Capacities |                 | : Filter | RPVST |     |     |
Spanningtreeprotocols(STP)|209

| Capacities | Name |     |     |     |     |     |     | Value |
| ---------- | ---- | --- | --- | --- | --- | --- | --- | ----- |
--------------------------------------------------------------------------
| Maximum        | number      | of      | RPVST VLANs  | configurable |     | on the system |     | 254  |
| -------------- | ----------- | ------- | ------------ | ------------ | --- | ------------- | --- | ---- |
| Maximum        | number      | of      | RPVST VPORTs | supported    |     | in a system   |     | 2048 |
| Command        | History     |         |              |              |     |               |     |      |
| Release        |             |         |              | Modification |     |               |     |      |
| 10.07orearlier |             |         |              | --           |     |               |     |      |
| Command        | Information |         |              |              |     |               |     |      |
| Platforms      |             | Command | context      | Authority    |     |               |     |      |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show capacities-status |     |     |       | rpvst |     |     |     |     |
| ---------------------- | --- | --- | ----- | ----- | --- | --- | --- | --- |
| show capacities-status |     |     | rpvst |       |     |     |     |     |
Description
ShowsthenumberofRPVST VLANsandRPVSTVPORTscurrentlyconfigured.
Examples
Showingcapacities-status:
| switch#    | show       | capacities-status |          | rpvst        |       |     |         |     |
| ---------- | ---------- | ----------------- | -------- | ------------ | ----- | --- | ------- | --- |
| System     | Capacities |                   | Status : | Filter RPVST |       |     |         |     |
| Capacities | Status     |                   | Name     |              | Value |     | Maximum |     |
--------------------------------------------------------------------------
| Number         | of RPVST    | VLANs   | configured |              |     | 3   | 254  |     |
| -------------- | ----------- | ------- | ---------- | ------------ | --- | --- | ---- | --- |
| Number         | of RPVST    | VPORTs  | configured |              |     | 9   | 2048 |     |
| Command        | History     |         |            |              |     |     |      |     |
| Release        |             |         |            | Modification |     |     |      |     |
| 10.07orearlier |             |         |            | --           |     |     |      |     |
| Command        | Information |         |            |              |     |     |      |     |
| Platforms      |             | Command | context    | Authority    |     |     |      |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
show spanning-tree
210
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- |

| show spanning-tree |     | [vsx-peer] |     |     |     |     |     |     |     |
| ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Description
ShowsthespanningtreemodeandinformationontheRPVSTinstances.
WhenPortsecurityisenabledontheportandtheclientisnot-yetauthenticated,thesecurityfeature
keepstheportintheDownstate.STPalsokeepstheportintheBlockingstateandtheroleasDisabled
intheshow spanning-treecommandoutput,whereasinthehardware,thestateismaintainedas
Learning.Afterclientauthenticationissuccessful,theportstatechangestoForwarding.
| Parameter |     |     |     | Description |     |     |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingspanningtreemodeandRPVSTinstanceinformation:
| switch#     | show spanning-tree |             |              |           |       |     |     |     |     |
| ----------- | ------------------ | ----------- | ------------ | --------- | ----- | --- | --- | --- | --- |
| Spanning    | tree status        |             | : Enabled    | Protocol: | RPVST |     |     |     |     |
| Extended    | System-id          |             | : Enabled    |           |       |     |     |     |     |
| Ignore PVID | Inconsistency      |             | : Enabled    |           |       |     |     |     |     |
| Path cost   | method             |             | : Long       |           |       |     |     |     |     |
| RPVST-MSTP  | Interconnect       |             | VLAN : 1     |           |       |     |     |     |     |
| Current     | Virtual            | Ports Count | : 7          |           |       |     |     |     |     |
| Maximum     | Allowed            | Virtual     | Ports : 2048 |           |       |     |     |     |     |
VLAN1
| Root ID | Priority     |          | : 32768           |            |             |     |     |     |     |
| ------- | ------------ | -------- | ----------------- | ---------- | ----------- | --- | --- | --- | --- |
|         | MAC-Address: |          | 70:72:cf:31:c9:23 |            |             |     |     |     |     |
|         | This         | bridge   | is the root       |            |             |     |     |     |     |
|         | Hello        | time(in  | seconds):2        | Max Age(in | seconds):20 |     |     |     |     |
|         | Forward      | Delay(in | seconds):15       |            |             |     |     |     |     |
| Bridge  | ID Priority  |          | : 32768           |            |             |     |     |     |     |
|         | MAC-Address: |          | 70:72:cf:31:c9:23 |            |             |     |     |     |     |
|         | Hello        | time(in  | seconds):2        | Max Age(in | seconds):20 |     |     |     |     |
|         | Forward      | Delay(in | seconds):15       |            |             |     |     |     |     |
PORT ROLE STATE COST PRIORITY TYPE BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------- ----------- ---------- ------- --------- --------- --------- --------- --------- -------
| 1/1/1         | Designated | Forwarding | 20000 | 128         | P2P Edge | 100 | 60  | 20  | 10  |
| ------------- | ---------- | ---------- | ----- | ----------- | -------- | --- | --- | --- | --- |
| 1/1/2         | Designated | Forwarding | 20000 | 128         | P2P      | 100 | 60  | 20  | 10  |
| 1/1/3         | Designated | Forwarding | 20000 | 128         | Shr      | 100 | 60  | 20  | 10  |
| 1/1/4         | Designated | Forwarding | 20000 | 128         | Shr Edge | 100 | 60  | 20  | 10  |
| 1/1/5         | Alternate  | Loop-Inc   | 20000 | 128         | Shr Edge | 100 | 60  | 20  | 10  |
| 1/1/6         | Alternate  | Root-Inc   | 20000 | 128         | Shr Edge | 100 | 60  | 20  | 10  |
| 1/1/7         | Disabled   | Down       | 20000 | 128         | P2P      | 100 | 60  | 20  | 10  |
| Number of     | topology   | changes    | : 4   |             |          |     |     |     |     |
| Last topology | change     | occurred   | : 516 | seconds ago |          |     |     |     |     |
| Command       | History    |            |       |             |          |     |     |     |     |
Spanningtreeprotocols(STP)|211

| Release |     |     |     |     | Modification |
| ------- | --- | --- | --- | --- | ------------ |
10.09
AnewstateDownisaddedintheoutput.
| 10.07orearlier |             |         |         |     | --        |
| -------------- | ----------- | ------- | ------- | --- | --------- |
| Command        | Information |         |         |     |           |
| Platforms      |             | Command | context |     | Authority |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |
| --- | --- | --- | --- | --- | ----------------------------------------------------- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |     |        | detail     |     |     |
| ------------------ | --- | ------ | ---------- | --- | --- |
| show spanning-tree |     | detail | [vsx-peer] |     |     |
Description
ShowsthedetailedspanningtreemodeandinformationontheRPVSTinstances.
WhenPortsecurityisenabledontheportandtheclientisnot-yetauthenticated,thesecurityfeature
keepstheportintheDownstate.STPalsokeepstheportintheBlockingstateandtheroleasDisabled
intheshow spanning-treecommandoutput,whereasinthehardware,thestateismaintainedas
Learning.Afterclientauthenticationissuccessful,theportstatechangestoForwarding.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingspanningtreemodeanddetailedRPVSTinstanceinformation:
| switch#     | show spanning-tree |                  | detail                |           |                 |
| ----------- | ------------------ | ---------------- | --------------------- | --------- | --------------- |
| Spanning    | tree               | status           | : Enabled             | Protocol: | RPVST AUTO      |
| Extended    | System-id          |                  | : Enabled             |           |                 |
| Ignore PVID | Inconsistency      |                  | : Disabled            |           |                 |
| Path cost   | method             |                  | : Long                |           |                 |
| RPVST-MSTP  | Interconnect       |                  | VLAN : 1              |           |                 |
| Current     | Virtual            | Ports Count      | : 2032                |           |                 |
| Maximum     | Allowed            | Virtual          | Ports : 2048          |           |                 |
| Maximum     | Allowed            | RPVST Instances: | 254                   |           |                 |
| Configured  | RPVST              | Enable           | Vlans : 20-30,100     |           |                 |
| Configured  | RPVST              | Disable          | Vlans : 1-10          |           |                 |
| Auto RPVST  | Enable             | Vlans            | : 11-19,31-99,101-264 |           |                 |
| Vlans with  | no                 | RPVST Instance   | due to                | Max limit | reach : 265-300 |
VLAN1
| Root ID | Priority     |         | : 32768           |     |                    |
| ------- | ------------ | ------- | ----------------- | --- | ------------------ |
|         | MAC-Address: |         | 70:72:cf:31:c9:23 |     |                    |
|         | This         | bridge  | is the root       |     |                    |
|         | Hello        | time(in | seconds):2        | Max | Age(in seconds):20 |
212
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

|        | Forward Delay(in | seconds):15       |            |             |     |     |     |
| ------ | ---------------- | ----------------- | ---------- | ----------- | --- | --- | --- |
| Bridge | ID Priority      | : 32768           |            |             |     |     |     |
|        | MAC-Address:     | 70:72:cf:31:c9:23 |            |             |     |     |     |
|        | Hello time(in    | seconds):2        | Max Age(in | seconds):20 |     |     |     |
|        | Forward Delay(in | seconds):15       |            |             |     |     |     |
PORT ROLE STATE COST PRIORITY TYPE BPDU-Tx BPDU-Rx TCN-Tx TCN-Rx
-------- ----------- ---------- ------- --------- --------- --------- --------- --------- -------
| 1/1/1         | Designated Forwarding | 20000   | 128         | P2P Edge 100  | 60                | 20  | 10  |
| ------------- | --------------------- | ------- | ----------- | ------------- | ----------------- | --- | --- |
| 1/1/2         | Designated Forwarding | 20000   | 128         | P2P 100       | 60                | 20  | 10  |
| 1/1/3         | Designated Forwarding | 20000   | 128         | Shr 100       | 60                | 20  | 10  |
| 1/1/4         | Designated Forwarding | 20000   | 128         | Shr Edge 100  | 60                | 20  | 10  |
| 1/1/5         | Alternate Loop-Inc    | 20000   | 128         | Shr Edge 100  | 60                | 20  | 10  |
| 1/1/6         | Alternate Root-Inc    | 20000   | 128         | Shr Edge 100  | 60                | 20  | 10  |
| 1/1/7         | Disabled Down         | 20000   | 128         | P2P 100       | 60                | 20  | 10  |
| lag1          | Disabled Down         | 20000   | 128         | P2P Bound 100 | 60                | 20  | 10  |
| Topology      | change flag :         | False   |             |               |                   |     |     |
| Number of     | topology changes      | : 1     |             |               |                   |     |     |
| Last topology | change occurred       | : 33293 | seconds ago |               |                   |     |     |
| Port 1/1/1    |                       |         |             |               |                   |     |     |
| Designated    | Root Priority         |         | : 32768     | Address:      | 48:0F:CF:AF:22:1D |     |     |
Designated Bridge Priority : 32768 Address: 48:0F:CF:AF:22:1D
| Designated       | Port           |      | : 1/1/1 |          |                   |     |     |
| ---------------- | -------------- | ---- | ------- | -------- | ----------------- | --- | --- |
| Forwarding-State | transitions    |      | : 0     |          |                   |     |     |
| BPDUs sent       | 1582, received | 1506 |         |          |                   |     |     |
| TCN_Tx: 10,      | TCN_Rx: 10     |      |         |          |                   |     |     |
| Port lag1        |                |      |         |          |                   |     |     |
| Designated       | Root Priority  |      | : 32768 | Address: | 48:0F:CF:AF:22:1D |     |     |
Designated Bridge Priority : 32768 Address: 48:0F:CF:AF:22:1D
| Designated       | Port           |         | : lag1                           |     |     |     |     |
| ---------------- | -------------- | ------- | -------------------------------- | --- | --- | --- | --- |
| Forwarding-State | transitions    |         | : 0                              |     |     |     |     |
| BPDUs sent       | 1402, received | 1316    |                                  |     |     |     |     |
| TCN_Tx: 10,      | TCN_Rx: 10     |         |                                  |     |     |     |     |
| Multi-chassis    | role           |         | : active                         |     |     |     |     |
| Command          | History        |         |                                  |     |     |     |     |
| Release          |                |         | Modification                     |     |     |     |     |
| 10.09            |                |         | AnewstateDownisaddedintheoutput. |     |     |     |     |
| 10.07orearlier   |                |         | --                               |     |     |     |     |
| Command          | Information    |         |                                  |     |     |     |     |
| Platforms        | Command        | context | Authority                        |     |     |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |                    | inconsistent-ports |       |            |     |     |     |
| ------------------ | ------------------ | ------------------ | ----- | ---------- | --- | --- | --- |
| show spanning-tree | inconsistent-ports |                    | [vlan | <VLAN-ID>] |     |     |     |
Spanningtreeprotocols(STP)|213

Description
ShowsportsblockedbySTPprotectionfunctionssuchasRootguard,Loopguard,BPDUguard,and
RPVSTguard.
| Parameter |     |     |     | Description             |     |
| --------- | --- | --- | --- | ----------------------- | --- |
| <VLAN-ID> |     |     |     | SpecifiesaVLANIDnumber. |     |
Examples
Showinginconsistentportinformation:
| switch#      | show spanning-tree |      | inconsistent-ports |       |     |
| ------------ | ------------------ | ---- | ------------------ | ----- | --- |
| VLAN ID      | Blocked            | Port | Reason             |       |     |
| ------------ | --------------     |      | ------------       |       |     |
| 1            | 1/1/1              |      | BPDU               | Guard |     |
| 2            | 1/1/1              |      | BPDU               | Guard |     |
| 3            | 1/1/1              |      | BPDU               | Guard |     |
| 4            | 1/1/1              |      | BPDU               | Guard |     |
| 5            | 1/1/1              |      | BPDU               | Guard |     |
| 6            | 1/1/1              |      | BPDU               | Guard |     |
| 7            | 1/1/1              |      | BPDU               | Guard |     |
| 8            | 1/1/1              |      | BPDU               | Guard |     |
| 9            | 1/1/1              |      | BPDU               | Guard |     |
| 10           | 1/1/1              |      | BPDU               | Guard |     |
ShowinginconsistentportinformationforVLANs1to4:
| switch#             | show spanning-tree |         | inconsistent-ports |              | vlan 1-4 |
| ------------------- | ------------------ | ------- | ------------------ | ------------ | -------- |
| VLAN ID             | Blocked            | Port    | Reason             |              |          |
| ------------        | --------------     |         | ------------       |              |          |
| 1                   | 1/1/3              |         | Root               | Guard        |          |
| 2                   | 1/1/7              |         | BPDU               | Guard        |          |
| 3                   | 1/1/9              |         | Loop               | Guard        |          |
| 4                   | 1/1/37             |         | RPVST              | Guard        |          |
| Command History     |                    |         |                    |              |          |
| Release             |                    |         |                    | Modification |          |
| 10.07orearlier      |                    |         |                    | --           |          |
| Command Information |                    |         |                    |              |          |
| Platforms           | Command            | context |                    | Authority    |          |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |         | summary |     | port |     |
| ------------------ | ------- | ------- | --- | ---- | --- |
| show spanning-tree | summary | port    |     |      |     |
Description
214
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

Showsasummaryofport-relatedspanning-treeconfigurationandstatus.
Example
Showingasummaryofport-relatedspanningtreeinformation:
| switch#     | show spanning-tree |            | summary | port          |                     |      |
| ----------- | ------------------ | ---------- | ------- | ------------- | ------------------- | ---- |
| STP status  |                    |            |         | : Enabled     |                     |      |
| Protocol    |                    |            |         | : RPVST       |                     |      |
| BPDU guard  | timeout            | value      |         | : None        |                     |      |
| BPDU guard  | enabled            | interfaces |         | : 1/1/1       |                     |      |
| BPDU filter | enabled            | interfaces |         | : None        |                     |      |
| Root guard  | enabled            | interfaces |         | : 1/1/3       |                     |      |
| Loop guard  | enabled            | interfaces |         | : 1/1/2       |                     |      |
| TCN guard   | enabled            | interfaces |         | : 1/1/1-1/1/3 |                     |      |
| Interface   | count by           | state      |         |               |                     |      |
| VLAN        |                    | Blocking   |         | Listening     | Learning Forwarding | Down |
---------------------- -------- --------- -------- ---------- ----
| VLAN1 |     |     | 0   |     | 0 0 | 1 0 |
| ----- | --- | --- | --- | --- | --- | --- |
| VLAN2 |     |     | 0   |     | 0 0 | 1 0 |
---------------------- -------- --------- -------- ---------- ----
| Total =        | 2           |         | 0   |                                  | 0 0 | 2 0 |
| -------------- | ----------- | ------- | --- | -------------------------------- | --- | --- |
| Command        | History     |         |     |                                  |     |     |
| Release        |             |         |     | Modification                     |     |     |
| 10.09          |             |         |     | AnewstateDownisaddedintheoutput. |     |     |
| 10.07orearlier |             |         |     | --                               |     |     |
| Command        | Information |         |     |                                  |     |     |
| Platforms      | Command     | context |     | Authority                        |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |
| --- | --- | --- | --- | ----------------------------------------------------- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |         | summary |      | root |     |     |
| ------------------ | ------- | ------- | ---- | ---- | --- | --- |
| show spanning-tree | summary |         | root |      |     |     |
Description
ShowsthesummaryofspanningtreerootandconfigurationsforallVLANs.
Example
Showingsummaryofspanningtreeconfigurations:
| switch#    | show spanning-tree |     | summary | root |     |     |
| ---------- | ------------------ | --- | ------- | ---- | --- | --- |
| STP status |                    | :   | Enabled |      |     |     |
Spanningtreeprotocols(STP)|215

| Protocol    |           | : RPVST             |     |            |         |      |      |
| ----------- | --------- | ------------------- | --- | ---------- | ------- | ---- | ---- |
| System ID   |           | : f8:60:f0:c9:70:40 |     |            |         |      |      |
| Root bridge | for VLANs | : 1-10              |     |            |         |      |      |
|             |           |                     |     | Root Hello | Max Fwd |      |      |
| VLAN        | Priority  | Root ID             |     | cost Time  | Age Dly | Root | Port |
-------- -------- ----------------- --------- ----- --- --- ------------
| VLAN1               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| ------------------- | ------- | ----------------- | ------------ | --- | ------- | --- | --- |
| VLAN2               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN3               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN4               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN5               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN6               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN7               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN8               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN9               | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| VLAN10              | 32768   | f8:60:f0:c9:70:40 |              | 0   | 2 20 15 |     | 0   |
| Command History     |         |                   |              |     |         |     |     |
| Release             |         |                   | Modification |     |         |     |     |
| 10.07orearlier      |         |                   | --           |     |         |     |     |
| Command Information |         |                   |              |     |         |     |     |
| Platforms           | Command | context           | Authority    |     |         |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     | (#) |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |     |
| --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
| show spanning-tree |      | vlan      |            |     |     |     |     |
| ------------------ | ---- | --------- | ---------- | --- | --- | --- | --- |
| show spanning-tree | vlan | <VLAN-ID> | [vsx-peer] |     |     |     |     |
Description
DisplaysthespanningtreemodeandinformationontheRPVSTinstanceofthespecifiedVLAN.
| Parameter |     |     | Description                |     |     |     |     |
| --------- | --- | --- | -------------------------- | --- | --- | --- | --- |
| <VLAN-ID> |     |     | SpecifiesthenumberofaVLAN. |     |     |     |     |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingspanningtreemodeandRPVSTinstanceinformationforVLAN2:
216
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- |

|     | switch# | show | spanning-tree |     | vlan | 2   |     |     |     |     |     |
| --- | ------- | ---- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
VLAN2
|     | Spanning | tree | status:      | Enabled  |                   | Protocol:   | RPVST |          |             |         |         |
| --- | -------- | ---- | ------------ | -------- | ----------------- | ----------- | ----- | -------- | ----------- | ------- | ------- |
|     | Root     | ID   | Priority     |          | : 32768           |             |       |          |             |         |         |
|     |          |      | MAC-Address: |          | 70:72:cf:76:43:2a |             |       |          |             |         |         |
|     |          |      | This         | bridge   | is the            | root        |       |          |             |         |         |
|     |          |      | Hello        | time(in  | seconds):2        |             | Max   | Age(in   | seconds):20 |         |         |
|     |          |      | Forward      | Delay(in |                   | seconds):15 |       |          |             |         |         |
|     | Bridge   | ID   | Priority     | :        | 32768             |             |       |          |             |         |         |
|     |          |      | MAC-Address: |          | 70:72:cf:76:43:2a |             |       |          |             |         |         |
|     |          |      | Hello        | time(in  | seconds):2        |             | Max   | Age(in   | seconds):20 |         |         |
|     |          |      | Forward      | Delay(in |                   | seconds):15 |       |          |             |         |         |
|     | PORT     | ROLE |              | STATE    |                   | COST        |       | PRIORITY | TYPE        | BPDU-Tx | BPDU-Rx |
|     | TCN-Tx   |      | TCN-Rx       |          |                   |             |       |          |             |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
|                | -- ---------- |             | ---------- |            |     |                                  |         |     |          |     |     |
| -------------- | ------------- | ----------- | ---------- | ---------- | --- | -------------------------------- | ------- | --- | -------- | --- | --- |
|                | 1/1/1         | Designated  |            | Forwarding |     | 20000                            |         | 128 | P2P Edge | 100 | 60  |
|                | 20            |             | 10         |            |     |                                  |         |     |          |     |     |
|                | 1/1/2         | Designated  |            | Forwarding |     | 20000                            |         | 128 | P2P      | 100 | 60  |
|                | 20            |             | 10         |            |     |                                  |         |     |          |     |     |
|                | 1/1/3         | Designated  |            | Forwarding |     | 20000                            |         | 128 | Shr      | 100 | 60  |
|                | 20            |             | 10         |            |     |                                  |         |     |          |     |     |
|                | 1/1/4         | Designated  |            | Forwarding |     | 20000                            |         | 128 | Shr Edge | 100 | 60  |
|                | 20            |             | 10         |            |     |                                  |         |     |          |     |     |
|                | 1/1/5         | Alternate   |            | Loop-Inc   |     | 20000                            |         | 128 | Shr Edge | 100 | 60  |
|                | 20            |             | 10         |            |     |                                  |         |     |          |     |     |
|                | 1/1/6         | Alternate   |            | Root-Inc   |     | 20000                            |         | 128 | Shr Edge | 100 | 60  |
|                | 20            |             | 10         |            |     |                                  |         |     |          |     |     |
|                | 1/1/7         | Disabled    |            | Down       |     | 20000                            |         | 128 | P2P      | 100 | 60  |
|                | 20            |             | 10         |            |     |                                  |         |     |          |     |     |
|                | Number        | of topology |            | changes    |     | : 4                              |         |     |          |     |     |
|                | Last topology |             | change     | occurred   |     | : 516                            | seconds | ago |          |     |     |
| Command        |               | History     |            |            |     |                                  |         |     |          |     |     |
| Release        |               |             |            |            |     | Modification                     |         |     |          |     |     |
| 10.09          |               |             |            |            |     | AnewstateDownisaddedintheoutput. |         |     |          |     |     |
| 10.07orearlier |               |             |            |            |     | --                               |         |     |          |     |     |
| Command        |               | Information |            |            |     |                                  |         |     |          |     |     |
| Platforms      |               | Command     |            | context    |     | Authority                        |         |     |          |     |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
executionrightsforthiscommand.Operatorscanexecutethis
(#)
commandfromtheoperatorcontext(>)only.
| show | spanning-tree |     |      | vlan      |     | detail |            |     |     |     |     |
| ---- | ------------- | --- | ---- | --------- | --- | ------ | ---------- | --- | --- | --- | --- |
| show | spanning-tree |     | vlan | <VLAN-ID> |     | detail | [vsx-peer] |     |     |     |     |
Description
Spanningtreeprotocols(STP)|217

DisplaysthespanningtreemodeandinformationontheRPVSTinstanceofthespecifiedVLANand
optionallydisplaysdetailsontheRPVSTinstancefortheVLAN.
| Parameter |     |     |     | Description                |     |     |     |     |     |
| --------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
| <VLAN-ID> |     |     |     | SpecifiesthenumberofaVLAN. |     |     |     |     |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowingspanningtreemodeanddetailedRPVSTinstanceinformationforVLAN2:
| switch# | show spanning-tree |     | vlan | 2 detail |     |     |     |     |     |
| ------- | ------------------ | --- | ---- | -------- | --- | --- | --- | --- | --- |
VLAN2
| Spanning | tree status: | Enabled  |                   | Protocol:   | RPVST |          |             |         |         |
| -------- | ------------ | -------- | ----------------- | ----------- | ----- | -------- | ----------- | ------- | ------- |
| Root     | ID Priority  |          | : 32768           |             |       |          |             |         |         |
|          | MAC-Address: |          | 70:72:cf:76:43:2a |             |       |          |             |         |         |
|          | This         | bridge   | is the            | root        |       |          |             |         |         |
|          | Hello        | time(in  | seconds):2        |             | Max   | Age(in   | seconds):20 |         |         |
|          | Forward      | Delay(in |                   | seconds):15 |       |          |             |         |         |
| Bridge   | ID Priority  |          | : 32768           |             |       |          |             |         |         |
|          | MAC-Address: |          | 70:72:cf:76:43:2a |             |       |          |             |         |         |
|          | Hello        | time(in  | seconds):2        |             | Max   | Age(in   | seconds):20 |         |         |
|          | Forward      | Delay(in |                   | seconds):15 |       |          |             |         |         |
| PORT     | ROLE         | STATE    |                   | COST        |       | PRIORITY | TYPE        | BPDU-Tx | BPDU-Rx |
| TCN-Tx   | TCN-Rx       |          |                   |             |       |          |             |         |         |
-------- ----------- ---------- ---------- --------- --------- ---------- --------
| -- ---------- | ----------  |            |       |         |         |     |          |     |     |
| ------------- | ----------- | ---------- | ----- | ------- | ------- | --- | -------- | --- | --- |
| 1/1/1         | Designated  | Forwarding |       | 20000   |         | 128 | P2P Edge | 100 | 60  |
| 20            | 10          |            |       |         |         |     |          |     |     |
| 1/1/2         | Designated  | Forwarding |       | 20000   |         | 128 | P2P      | 100 | 60  |
| 20            | 10          |            |       |         |         |     |          |     |     |
| 1/1/3         | Designated  | Forwarding |       | 20000   |         | 128 | Shr      | 100 | 60  |
| 20            | 10          |            |       |         |         |     |          |     |     |
| 1/1/4         | Designated  | Forwarding |       | 20000   |         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |       |         |         |     |          |     |     |
| 1/1/5         | Alternate   | Loop-Inc   |       | 20000   |         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |       |         |         |     |          |     |     |
| 1/1/6         | Alternate   | Root-Inc   |       | 20000   |         | 128 | Shr Edge | 100 | 60  |
| 20            | 10          |            |       |         |         |     |          |     |     |
| 1/1/7         | Disabled    | Down       |       | 20000   |         | 128 | P2P      | 100 | 60  |
| 20            | 10          |            |       |         |         |     |          |     |     |
| Topology      | change flag | :          | False |         |         |     |          |     |     |
| Number        | of topology | changes    | :     | 1       |         |     |          |     |     |
| Last topology | change      | occurred   |       | : 33293 | seconds | ago |          |     |     |
Port 1/1/1
| Designated | root has | priority |     | :32768 | Address: | 48:0f:cf:af:22:1d |     |     |     |
| ---------- | -------- | -------- | --- | ------ | -------- | ----------------- | --- | --- | --- |
Designated bridge has priority :32768 Address: 48:0f:cf:af:22:1d
| Designated | port :1        |     |            |     |       |     |     |     |     |
| ---------- | -------------- | --- | ---------- | --- | ----- | --- | --- | --- | --- |
| Number     | of transitions | to  | forwarding |     | state | : 0 |     |     |     |
| BPDUs sent | 1582, received |     | 1506       |     |       |     |     |     |     |
| TCN_Tx:    | 10, TCN_Rx:    | 10  |            |     |       |     |     |     |     |
218
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| Command        | History     |         |         |     |                                  |     |
| -------------- | ----------- | ------- | ------- | --- | -------------------------------- | --- |
| Release        |             |         |         |     | Modification                     |     |
| 10.09          |             |         |         |     | AnewstateDownisaddedintheoutput. |     |
| 10.07orearlier |             |         |         |     | --                               |     |
| Command        | Information |         |         |     |                                  |     |
| Platforms      |             | Command | context |     | Authority                        |     |
Allplatforms Operator(>)orManager OperatorsorAdministratorsorlocalusergroupmemberswith
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- |
commandfromtheoperatorcontext(>)only.
| spanning-tree    |            | bpdu-guard |         | timeout    |              |     |
| ---------------- | ---------- | ---------- | ------- | ---------- | ------------ | --- |
| spanning-tree    | bpdu-guard |            | timeout | <INTERVAL> |              |     |
| no spanning-tree |            | bpdu-guard | timeout |            | [<INTERVAL>] |     |
Description
Enablesandconfigurestheautore-enabletimeoutinsecondsforallinterfaceswithBPDUguard
enabled.WhenaninterfaceisdisabledafterreceivinganunauthorizedBPDUitwillautomaticallybere-
enabledafterthetimeoutexpires.Thedefaultisfortheinterfacetostaydisableduntilmanuallyre-
enabled.
ThenoformofthecommanddisablesBPDUguardtimeoutontheinterface.Thisisthedefault.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<INTERVAL> Specifiesthere-enabletimeoutinseconds.Range:1to65535.
Example
EnablingtheBPDUguardtimeoutoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1         |     |            |            |
| ------------------ | --- | --------- | ------------- | --- | ---------- | ---------- |
| switch(config-if)# |     |           | spanning-tree |     | bpdu-guard | timeout 10 |
DisablingBPDUguardtimeoutoninterface1/1/1:
| switch(config)#    |             | interface | 1/1/1            |     |              |     |
| ------------------ | ----------- | --------- | ---------------- | --- | ------------ | --- |
| switch(config-if)# |             |           | no spanning-tree |     | bpdu-guard   |     |
| Command            | History     |           |                  |     |              |     |
| Release            |             |           |                  |     | Modification |     |
| 10.07orearlier     |             |           |                  |     | --           |     |
| Command            | Information |           |                  |     |              |     |
Spanningtreeprotocols(STP)|219

| Platforms | Command | context |     | Authority |     |
| --------- | ------- | ------- | --- | --------- | --- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | extend-system-id |     |         |            |     |
| ---------------- | ---------------- | --- | ------- | ---------- | --- |
| spanning-tree    | extend-system-id |     | {enable | | disable} |     |
| no spanning-tree | extend-system-id |     |         |            |     |
Description
ConfiguresuseofextendedsystemID.Whenenabled,theVLANIDisincludedinspanningtreepackets.
Whendisabled,theVLANIDissettoNULLinthespanningtreepackets.
Bydefault,extendedsystemIDisenabled.IfyoudisableextendedsystemID,thebridgeidentifierfield
inthespanningtreepacketisfilledwithzeros.
ThenoformofthiscommanddisablesextendedsystemID.
| Parameter |     |     |     | Description                              |     |
| --------- | --- | --- | --- | ---------------------------------------- | --- |
| enable    |     |     |     | SpecifiesenablinguseofextendedsystemID.  |     |
| disable   |     |     |     | SpecifiesdisablinguseofextendedsystemID. |     |
Examples
EnablingextendedsystemID:
| switch#         | config        |     |                  |     |        |
| --------------- | ------------- | --- | ---------------- | --- | ------ |
| switch(config)# | spanning-tree |     | extend-system-id |     | enable |
DisablingextendedsystemID:
| switch#         | config        |               |                  |                  |         |
| --------------- | ------------- | ------------- | ---------------- | ---------------- | ------- |
| switch(config)# | spanning-tree |               | extend-system-id |                  | disable |
| switch(config)# | no            | spanning-tree |                  | extend-system-id |         |
| Command         | History       |               |                  |                  |         |
| Release         |               |               |                  | Modification     |         |
| 10.07orearlier  |               |               |                  | --               |         |
| Command         | Information   |               |                  |                  |         |
| Platforms       | Command       | context       |                  | Authority        |         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree | ignore-pvid-inconsistency |     |     |         |            |
| ------------- | ------------------------- | --- | --- | ------- | ---------- |
| spanning-tree | ignore-pvid-inconsistency |     |     | {enable | | disable} |
220
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| no spanning-tree | ignore-pvid-inconsistency |     |     |     |
| ---------------- | ------------------------- | --- | --- | --- |
Description
Configuresportbehaviorwhenper-VLANIDinconsistenciesarepresent.Forexample,whentheports
onbothendsofapoint-to-pointlinkareuntaggedmembersofdifferentVLANs,enablingthisoption
allowsRPVST+toprocessuntaggedRPVST+packetsbelongingtothepeer’suntaggedVLANasifthey
werereceivedonthecurrentdevice’suntaggedVLAN.Whenthisoptionisdisabled,RPVST+blocksthe
link,causingtrafficonthemismatchedVLANstobedropped.
Ifthisoptionisenabledonmultipleswitchesconnectedbyhubs,therecouldbemorethantwoVLANs
involvedinPVIDmismatchesthatwillbeignoredbyRPVST+.
IfportVLANmembershipsismisconfiguredonaswitchinthenetwork,thenenablingthisoption
preventsRPVST+fromdetectingtheproblem,whichmayresultinpacketduplicationinthenetwork
sinceRPVST+wouldnotconvergecorrectly.
ThiscommandaffectsallportsontheswitchbelongingtoVLANsonwhichRPVST+isenabled.
Bydefaultignoreper-VLANIDinconsistencyisdisabled.
Thenoformofthiscommandsetstheignoreper-VLANIDinconsistenciestodisabled.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
enable Specifiesignoreper-VLANIDinconsistenciesandallowRPVSTto
runonmismatchedlinks.
disable Disablestheignoreper-VLANIDinconsistenciesfunctionality.
Examples
Enablingignoreper-VLANIDinconsistencies:
| switch#         | config        |     |                           |        |
| --------------- | ------------- | --- | ------------------------- | ------ |
| switch(config)# | spanning-tree |     | ignore-pvid-inconsistency | enable |
Disablingignoreper-VLANIDinconsistencies:
| switch# | config |     |     |     |
| ------- | ------ | --- | --- | --- |
switch(config)# spanning-tree ignore-pvid-inconsistency disable
| switch(config)#     | no      | spanning-tree | ignore-pvid-inconsistency |     |
| ------------------- | ------- | ------------- | ------------------------- | --- |
| Command History     |         |               |                           |     |
| Release             |         |               | Modification              |     |
| 10.07orearlier      |         |               | --                        |     |
| Command Information |         |               |                           |     |
| Platforms           | Command | context       | Authority                 |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Spanningtreeprotocols(STP)|221

| spanning-tree    |           | link-type |                 |           |     |
| ---------------- | --------- | --------- | --------------- | --------- | --- |
| spanning-tree    | link-type |           | {point-to-point | | shared} |     |
| no spanning-tree |           | link-type |                 |           |     |
Description
Configuresthelinktypeofaport.
Thenoformofthiscommandsetsthespanningtreelinktypetothedefaultvalueofpoint-to-point.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
point-to-point Setsthespanningtreelinktypeaspoint-to-point.Usethisforfull-
duplexportsthatprovideapoint-to-pointlinktodevicessuchasa
switch,bridge,orend-node.Default.
shared
Setsthespanningtreelinktypeasshared.Usethiswhentheport
isconnectedtoahub.
Examples
Settingspanningtreelinktypetoshared:
| switch(config)#    |     | interface | 1/1/1         |           |        |
| ------------------ | --- | --------- | ------------- | --------- | ------ |
| switch(config-if)# |     |           | spanning-tree | link-type | shared |
Settingspanningtreelinktypetopoint-to-pointforaport:
| switch(config)#    |             | interface | 1/1/1            |              |     |
| ------------------ | ----------- | --------- | ---------------- | ------------ | --- |
| switch(config-if)# |             |           | no spanning-tree | link-type    |     |
| Command            | History     |           |                  |              |     |
| Release            |             |           |                  | Modification |     |
| 10.07orearlier     |             |           |                  | --           |     |
| Command            | Information |           |                  |              |     |
| Platforms          | Command     |           | context          | Authority    |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree |     | mode |     |     |     |
| ------------- | --- | ---- | --- | --- | --- |
spanning-tree mode {mstp|rpvst [auto-vlan-enable [priority <NUMBER>]]}
no spanning-tree mode {mstp|rpvst [auto-vlan-enable [priority <NUMBER>]]}
Description
Setsthespanningtreeprotocol(STP)modetoeitherMSTPmode(Multiple-instanceSpanningTree
Protocol)orRPVSTmode(RapidPerVLANSpanningTree).EnablingtheRPVSTAutoVLANfeaturewill
222
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

runRPVSTonallVLANscurrentlyconfiguredontheswitch.Defaultpriorityof8willbeassignedtothe
VLANsbeingautocreated.
Thenoformofthiscommandsetsthespanningtreemodetothedefaultmstp.
Enablingauto-VLANcanleadtoanundeterministicstateifautoscaledbeyondthemaxsystemlimitmentionedin
thecapacity-status.
| Parameter |     | Description                                  |
| --------- | --- | -------------------------------------------- |
| mstp      |     | SetstheSTPmodetoMSTPwhichappliesspanningtree |
separatelyforeachsetofVLANscalledanMSTI(multiple
spanningtreeinstance).
| rpvst            |     | SetstheSTPmodetoRPVST.    |
| ---------------- | --- | ------------------------- |
| auto-vlan-enable |     | SelectsRPVSTautoVLANmode. |
priority <NUMBER> SpecifiestheprioritesforallautocreatedRPVSTinstances.
Configuredasamultipleof4096.Default:8.
Examples
EnablingMSTPmode:
| switch(config)# | spanning-tree | mode mstp |
| --------------- | ------------- | --------- |
DisablingMSTPmode:
| switch(config)# | no spanning-tree | mode mstp |
| --------------- | ---------------- | --------- |
EnablingRPVSTmode:
| switch(config)# | spanning-tree | mode rpvst |
| --------------- | ------------- | ---------- |
DisablingRPVSTmode:
| switch(config)# | no spanning-tree | mode rpvst |
| --------------- | ---------------- | ---------- |
EnablingRPVSTautoVLANwithapriorityof1:
switch(config)# spanning-tree mode rpvst auto-vlan-enable priority 1
DisablingRPVSTautoVLANwithapriorityof1:
switch(config)# no spanning-tree mode rpvst auto-vlan-enable priority 1
Command History
Spanningtreeprotocols(STP)|223

| Release        |             |     |         |     | Modification         |     |
| -------------- | ----------- | --- | ------- | --- | -------------------- | --- |
| 10.12.1000     |             |     |         |     | AutoVLANenableadded. |     |
| 10.07orearlier |             |     |         |     | --                   |     |
| Command        | Information |     |         |     |                      |     |
| Platforms      | Command     |     | context |     | Authority            |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |               | pathcost-type |     |              |          |     |
| ---------------- | ------------- | ------------- | --- | ------------ | -------- | --- |
| spanning-tree    | pathcost-type |               |     | {long        | | short} |     |
| no spanning-tree |               | pathcost-type |     | [long|short] |          |     |
Description
Configuresthespanningtreepathcosttype.Thelongmodeprovidessupportforthewiderrangeoflink
speedsrequiredbyhigh-speedinterfaces.Allswitchesinthenetworkmustusethesamepathcosttype
orerrorscanoccurinthespanningtree.
Thenoformofthiscommandsetsthespanningtreepathcosttypetothedefaultlong.
| Parameter |     |     |     |     | Description                                         |     |
| --------- | --- | --- | --- | --- | --------------------------------------------------- | --- |
| long      |     |     |     |     | Specifiesthespanningtreepathcosttypeasa32-bitvalue, |     |
allowingportcostvaluestobesetintherange1-200,000,000.
Default.
| short |     |     |     |     | Specifiesthespanningtreepathcosttypeasa16-bitvalue, |     |
| ----- | --- | --- | --- | --- | --------------------------------------------------- | --- |
allowingportcostvaluestobesetintherange1-65535.
Examples
Settingspanningtreepathcosttypetoshort:
| switch#         | config |               |     |     |               |       |
| --------------- | ------ | ------------- | --- | --- | ------------- | ----- |
| switch(config)# |        | spanning-tree |     |     | pathcost-type | short |
Settingspanningtreepathcosttypetolong:
| switch#         | config |               |     |     |               |      |
| --------------- | ------ | ------------- | --- | --- | ------------- | ---- |
| switch(config)# |        | spanning-tree |     |     | pathcost-type | long |
Settingspanningtreepathcosttodefaultoflong:
| switch#         | config  |     |               |     |               |     |
| --------------- | ------- | --- | ------------- | --- | ------------- | --- |
| switch(config)# |         | no  | spanning-tree |     | pathcost-type |     |
| Command         | History |     |               |     |               |     |
224
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- |

| Release        |             |         | Modification |     |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- | --- |
| 10.07orearlier |             |         | --           |     |     |     |
| Command        | Information |         |              |     |     |     |
| Platforms      | Command     | context | Authority    |     |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |                              | rpvst-mstp                   | interconnect |             | vlan |     |
| ---------------- | ---------------------------- | ---------------------------- | ------------ | ----------- | ---- | --- |
| spanning-tree    | rpvst-mstp-interconnect-vlan |                              |              | <VLAN-ID>   |      |     |
| no spanning-tree |                              | rpvst-mstp-interconnect-vlan |              | [<VLAN-ID>] |      |     |
Description
ConfigurestheVLANthathastobeusedtointerconnectRPVSTandMSTPdomains.VLAN1isusedby
default.
ThenoformofthiscommandsetstheVLAN configurationtothedefaultof1.
n ItisrequiredtocreatetheinterconnectVLANandthenconfigureRPVSTspanningtreeonit.
n ThesameinterconnectVLANmustbekeptonalltheswitchesinthenetwork.
n AddingordeletingtheinterconnectVLANtriggersare-convergenceinthenetwork.
n DeletingaVLANthatisconfiguredastheinterconnectVLANdoesnotresetthevaluetothedefault.
| Parameter |     |     | Description                |     |     |     |
| --------- | --- | --- | -------------------------- | --- | --- | --- |
| <VLAN-ID> |     |     | SpecifiesthenumberofaVLAN. |     |     |     |
Examples
ThisexampleconfiguresVLAN10tousedtointerconnectRPVSTandMSTPdomains.
| switch#(config)# |             | spanning-tree | rpvst-mstp-interconnect-vlan |     |     | 10  |
| ---------------- | ----------- | ------------- | ---------------------------- | --- | --- | --- |
| Command          | History     |               |                              |     |     |     |
| Release          |             |               | Modification                 |     |     |     |
| 10.07orearlier   |             |               | --                           |     |     |     |
| Command          | Information |               |                              |     |     |     |
| Platforms        | Command     | context       | Authority                    |     |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree |     | tcn-guard |     |     |     |     |
| ------------- | --- | --------- | --- | --- | --- | --- |
Spanningtreeprotocols(STP)|225

| spanning-tree    | tcn-guard |     |     |
| ---------------- | --------- | --- | --- |
| no spanning-tree | tcn-guard |     |     |
Description
Disablespropagationoftopologychangenotifications(TCNs)tootherSTPports.Usethiswhenyoudo
notwanttopologychangestobenoticedbypeerdevices.Bydefault,thepropagationisenabled.
Thenoformofthiscommand,enablespropagationoftopologychangeswhichisthedefault.
Examples
Enablingtcn-guard,whichdisablespropagationoftopologychanges:
| switch(config-if)# |     | spanning-tree | tcn-guard |
| ------------------ | --- | ------------- | --------- |
Disablingtcn-guard,whichenablespropagationoftopologychanges:
| switch(config-if)#  |         | no spanning-tree | tcn-guard    |
| ------------------- | ------- | ---------------- | ------------ |
| Command History     |         |                  |              |
| Release             |         |                  | Modification |
| 10.07orearlier      |         |                  | --           |
| Command Information |         |                  |              |
| Platforms           | Command | context          | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree | vlan |     |     |
| ------------- | ---- | --- | --- |
spanning-tree vlan <VLAN-LIST> [{hello-time | foward-delay | max-age | priority} <VALUE>]
no spanning-tree vlan <VLAN-LIST> [hello-time | foward-delay | max-age | priority]
Description
CreatesanRPVSTinstanceforthespecifiedVLAN.ThiscommandalsoallowsforconfigurationofRPVST
instance-specifictimeparameters.
ThenoformofthiscommandremovestheRPVSTinstanceassociatedwiththespecifiedVLAN,and
configuresdefaultvaluesforRPVSTinstance-specificparameters.
| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
<VLAN-LIST> SpecifiesthenumberofasingleVLAN,oraseriesofnumbersfor
arangeofVLANs,separatedbycommas(1,2,3,4),dashes(1-4),
orboth(1-4,6).
hello-time <VALUE> Specifiesthehello-timeinsecondsfortheRPVSTinstance.Range:
2-10seconds.Default:2seconds.
226
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |
| -------------------------------- | --- | ---------------- | --- |

| Parameter |     |     |     |     | Description |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- |
forward-delay <VALUE> Specifiestheforward-delaytimeinsecondsfortheRPVST
instance.Range:4-30seconds.Default:15seconds.
max-age <VALUE> SpecifiesthemaximumagetimeinsecondsfortheRPVST
instance.Range:6-40seconds.Default:20seconds.
| priority | <VALUE> |     |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- | --- |
SpecifiesthepriorityfortheRPVSTinstance.Priorityvalueis
configuredasamultipleof4096.Range:0-15.Default:8whichis
32768.
Examples
CreatinganRPVSTinstanceforalistofVLANsandconfiguringvarioustimeparameters:
| switch#         | config |               |     |     |                        |     |     |
| --------------- | ------ | ------------- | --- | --- | ---------------------- | --- | --- |
| switch(config)# |        | spanning-tree |     |     | vlan 2-5               |     |     |
| switch(config)# |        | spanning-tree |     |     | vlan 2-5 hello-time    |     | 5   |
| switch(config)# |        | spanning-tree |     |     | vlan 5 max-age         | 10  |     |
| switch(config)# |        | spanning-tree |     |     | vlan 2-5 forward-delay |     | 25  |
| switch(config)# |        | spanning-tree |     |     | vlan 2-5 priority      |     | 5   |
RemovinganRPVSTinstanceforalistofVLANsandsettingvarioustimeparameterstothedefault:
| switch#         | config      |     |               |     |              |              |     |
| --------------- | ----------- | --- | ------------- | --- | ------------ | ------------ | --- |
| switch(config)# |             | no  | spanning-tree |     | vlan 2-5     |              |     |
| switch(config)# |             | no  | spanning-tree |     | vlan 2-5     | hello-time   |     |
| switch(config)# |             | no  | spanning-tree |     | vlan 2-5     | forward-time |     |
| switch(config)# |             | no  | spanning-tree |     | vlan 2-5     | max-age      |     |
| switch(config)# |             | no  | spanning-tree |     | vlan 2-5     | priority     |     |
| Command         | History     |     |               |     |              |              |     |
| Release         |             |     |               |     | Modification |              |     |
| 10.07orearlier  |             |     |               |     | --           |              |     |
| Command         | Information |     |               |     |              |              |     |
| Platforms       | Command     |     | context       |     | Authority    |              |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    |      | vlan        | cost        |      |             |     |     |
| ---------------- | ---- | ----------- | ----------- | ---- | ----------- | --- | --- |
| spanning-tree    | vlan | <VLAN-LIST> |             | cost | <PORT-COST> |     |     |
| no spanning-tree |      | vlan        | <VLAN-LIST> |      | cost        |     |     |
Description
ConfiguresthespanningtreecostfortheVLAN.Thisisthecosttoreachtherootport.
Thenoformofthiscommandsetstheportcosttothedefaultvalue.
Spanningtreeprotocols(STP)|227

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
<VLAN-LIST> SpecifiesthenumberofasingleVLAN,oraseriesofnumbersfor
arangeofVLANs,separatedbycommas(1,2,3,4),dashes(1-4),
orboth(1-4,6).
| <PORT-COST> |     |     |     | SpecifiesthespanningtreecostfortheVLAN.Range:1- |     |
| ----------- | --- | --- | --- | ----------------------------------------------- | --- |
200,000,000.Defaultiscalculatedfromtheportlinkspeed:
|     |     |     |     | n 10Mbpslinkspeedequalsapathcostof2,000,000. |     |
| --- | --- | --- | --- | -------------------------------------------- | --- |
|     |     |     |     | n 100Mbpslinkspeedequalsapathcostof200,000.  |     |
|     |     |     |     | n 1Gbpslinkspeedequalsapathcostof20,000.     |     |
|     |     |     |     | n 2Gbpslinkspeedequalsapathcostof10,000.     |     |
|     |     |     |     | n 10Gbpslinkspeedequalsapathcostof2,000.     |     |
|     |     |     |     | n 100Gbpslinkspeedequalsapathcostof200.      |     |
|     |     |     |     | n 1Tbpslinkspeedequalsapathcostof20.         |     |
Examples
Settingportcost:
| switch(config-if)# |     | spanning-tree |     | vlan | 5 cost 100000 |
| ------------------ | --- | ------------- | --- | ---- | ------------- |
Settingportcosttothedefault:
| switch(config-if)# |             | no spanning-tree |     | vlan         | 5 cost |
| ------------------ | ----------- | ---------------- | --- | ------------ | ------ |
| Command            | History     |                  |     |              |        |
| Release            |             |                  |     | Modification |        |
| 10.07orearlier     |             |                  |     | --           |        |
| Command            | Information |                  |     |              |        |
| Platforms          | Command     | context          |     | Authority    |        |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree    | vlan | port-priority |               |               |            |
| ---------------- | ---- | ------------- | ------------- | ------------- | ---------- |
| spanning-tree    | vlan | <VLAN-LIST>   | port-priority |               | <PRIORITY> |
| no spanning-tree | vlan | <VLAN-LIST>   |               | port-priority |            |
Description
Configuresportpriority.Aportwiththelowestprioritynumberhasthehighestpriorityforusein
forwardingtraffic.
Thenoformofthiscommand,setstheportprioritytothedefaultof8.
228
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |     |
| -------------------------------- | --- | ---------------- | --- | --- | --- |

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<VLAN-LIST> SpecifiesthenumberofasingleVLAN,oraseriesofnumbersfor
arangeofVLANs,separatedbycommas(1,2,3,4),dashes(1-4),
orboth(1-4,6).
<PRIORITY> Specifiestheportpriority.Thevalue,configuredasamultipleof
16,helpsindeterminingthedesignatedport.Thelowerapriority
value,thehigherthepriority.Range:1to15.Default:8.
Examples
Settingportpriority:
| switch(config-if)# |     | spanning-tree | vlan 5 port-priority | 10  |
| ------------------ | --- | ------------- | -------------------- | --- |
Settingportprioritytothedefaultof8:
| switch(config-if)#  |         | no spanning-tree | vlan 5 port-priority |     |
| ------------------- | ------- | ---------------- | -------------------- | --- |
| Command History     |         |                  |                      |     |
| Release             |         |                  | Modification         |     |
| 10.07orearlier      |         |                  | --                   |     |
| Command Information |         |                  |                      |     |
| Platforms           | Command | context          | Authority            |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
| spanning-tree | trap |     |     |     |
| ------------- | ---- | --- | --- | --- |
spanning-tree trap {new-root | topology-change [vlan <VLAN-ID>] |
errant-bpdu | root-guard-inconsistency | loop-guard-inconsistency}
no spanning-tree trap {new-root | topology-change [vlan <VLAN-ID>] |
errant-bpdu | root-guard-inconsistency | loop-guard-inconsistency}
Description
EnablesSNMPtrapsfornewroot,topologychangeevent,errant-bpdureceivedevent,root-guard
inconsistency,andloop-guardinconsistencynotifications.Itisdisabledbydefault.
ThenoformofthiscommanddisablesthenotificationsforSNMPtraps.
| Parameter |     |     | Description                                       |     |
| --------- | --- | --- | ------------------------------------------------- | --- |
| new-root  |     |     | EnablesSNMPnotificationwhenanewrootiselectedonany |     |
PVSTvlanontheswitch.
topology-change EnablesSNMPnotificationwhenatopologychangeevent
Spanningtreeprotocols(STP)|229

| Parameter |     | Description |     |
| --------- | --- | ----------- | --- |
occurredinspecifiedPVSTvlanontheswitch.
<VLAN-ID> SpecifiestheVLAN IDforthetopologychangetrap.Range:1to
4094.
errant-bpdu
EnablesSNMPnotificationwhenanerrantbpduisreceivedbyany
PVSTvlanontheswitch.
root-guard-inconsistency EnablesSNMPnotificationwhentheroot-guardfindstheport
inconsistentforanyPVSTvlanontheswitch.
loop-guard-inconsistency EnablesSNMPnotificationwhentheloop-guardfindstheport
inconsistentforanyPVSTvlanontheswitch.
Examples
EnablingthenotificationsfortheSNMPtraps:
| switch(config)# | spanning-tree | trap |     |
| --------------- | ------------- | ---- | --- |
new-root Enable notifications which are sent when a new root is
elected
topology-change Enable notifications which are sent when a topology
change occurs
errant-bpdu Enable notifications which are sent when an errant
bpdu is received
root-guard-inconsistency Enable notifications which are sent when root guard
| inconsistency | occurs |     |     |
| ------------- | ------ | --- | --- |
loop-guard-inconsistency Enable notifications which are sent when loop guard
| inconsistency   | occurs        |               |     |
| --------------- | ------------- | ------------- | --- |
| switch(config)# | spanning-tree | trap new-root |     |
<cr>
| switch(config)# | spanning-tree | trap topology-change |     |
| --------------- | ------------- | -------------------- | --- |
vlan Enable topology change notification for the specified PVST vlan id.
| switch(config)# | spanning-tree | trap topology-change | vlan |
| --------------- | ------------- | -------------------- | ---- |
<1-4094> Enable topology change information on the specified vlan id.
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
DisablingthenotificationsfortheSNMPtraps:
| switch(config)# | no spanning-tree | trap |     |
| --------------- | ---------------- | ---- | --- |
new-root Disable notifications which are sent when a new root
is elected
topology-change Disable notifications which are sent when a topology
change occurs
errant-bpdu Disable notifications which are sent when an errant
bpdu is received
root-guard-inconsistency Disable notifications which are sent when root guard
| inconsistency | occurs |     |     |
| ------------- | ------ | --- | --- |
loop-guard-inconsistency Disable notifications which are sent when loop guard
| inconsistency | occurs |     |     |
| ------------- | ------ | --- | --- |
230
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| switch(config)# | no  | spanning-tree | trap new-root |     |
| --------------- | --- | ------------- | ------------- | --- |
<cr>
| switch(config)# | no  | spanning-tree | trap topology-change |     |
| --------------- | --- | ------------- | -------------------- | --- |
instance Disable topology change notification for the specified PVST vlan id.
| switch(config)# | no  | spanning-tree | trap topology-change | vlan |
| --------------- | --- | ------------- | -------------------- | ---- |
<1-4094> Disable topology change information on the specified PVST vlan id.
| switch(config)# | no  | spanning-tree | trap topology-change | vlan 1 |
| --------------- | --- | ------------- | -------------------- | ------ |
<cr>
| switch(config)# | no  | spanning-tree | trap errant-bpdu |     |
| --------------- | --- | ------------- | ---------------- | --- |
<cr>
| switch(config)# | no  | spanning-tree | trap root-guard-inconsistency |     |
| --------------- | --- | ------------- | ----------------------------- | --- |
<cr>
| switch(config)# | no  | spanning-tree | trap loop-guard-inconsistency |     |
| --------------- | --- | ------------- | ----------------------------- | --- |
<cr>
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
Spanningtreeprotocols(STP)|231

RPVST+ debugging and troubleshooting
When there are suspected convergence problems with RPVST+, use the information provided in this
section to help solve the problems. The main symptoms of a convergence problem are as follows:

Check L2 port VLAN configurations.

a.

If a ports is expected to be a root ports with direct connection but are not selected, check if the
port is enabled for that vlan using command show vlan.

b. For proper convergence, confirm that command show spanning-tree vlan shows all expected

ports of the VLAN.

c. Check the default cost and port-priority set for all configured interfaces (ports) and LAGS. Any
custom configurations should be justified and should not be affecting the path selection. For
example the undesired use of a 10G forwarding path instead of available redundant 25G or 40G
paths.

Set the RPVST instance priorities

a. Use command spanning-tree vlan <VLAN-LIST> priority <VALUE> to set the RPVST instance.

Eliminate mismatched path cost types across all devices in the network.

Aruba switches use Long path cost by default, other vendor switches might be using short path cost. Set
path cost the same on all devices.

a. Set spanning tree cost with command spanning-tree vlan cost.

If convergence is slow or improper, check if the vPort limit has been reached, and if so,
reduce Vport consumption.

It is recommended to not allow more vPorts to be used than the maximum shown with command show
capacities rpvst.

When excessive vPort consumption occurs (beyond the maximum indicated by the show capacities
rpvst command), convergence may slow or have problems.

Some typical symptoms of slowed or problematic convergence are as follows:

n For any link down, network segment down, or root change, the convergence takes more than 30

seconds, thus impacting traffic for more than 30 seconds.

n Root or designated or alternate port selection could be improper.

n The vPort limit is the maximum the system can process the RPVST PDUs within required time (to
allow convergence and process and send BPDUs within limits so that convergence is sustained),
hence sometime with less system load or with non-participating STP-ports (such as those connected
to end-hosts or other non-STP-devices). But careful evaluation of vPorts need to be done, so that we
shall not stress RPVST.

Use command show capacities status rpvst. Confirm that the number of RPVST vPorts does not
equal the maximum. When the number of configured vPorts is close to the maximum, RPVST+
convergence slows.

vPort consumption can be reduced as follows:

a. Check if you have configured unnecessary VLANs as part of a trunk, or if you have accidentally

configured vlan trunk allowed all. Remove unnecessary VLANs from L2 ports, to reduce vPort

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

232

consumption.

b. Reduce the number of unused L2 ports that are enabled. Although unused L2 ports are not

actively participating in convergence, they do consume vPorts.

c. Optimize the number of RPVST+ instances created. If there are VLANs without risk of loops or
VLANs local to edge switches, then delete such VLANs or delete the VLAN RPVST+ instances.

Alternatively, consider using MSTP instead of RPVST+. MSTP is not limited by the number of L2 ports
and VLANs configured.

RPVST+ FAQ

1. Are there any specific loop-prevention recommendations for access switches?

If the access switch is prone to receiving excess BPDUs, consider enabling RPVST+ or MSTP.

2. What is the default spanning tree protocol (STP) mode?

The default STP mode is MSTP. RPVST+ is also supported. Set the SPT mode with command spanning-
tree mode.

3. Can RPVST+ and MSTP switches be interconnected?

Yes. To interconnect typically use the default VLAN 1. This is based on the RFC for interconnection.

4. What network-resiliency features are available for physical links?

The Industry-standard feature unidirectional link detection (UDLD on fiber links) is available.

5. What is the maximum number of STP hops supported?

The maximum is 40. The default is 20.

6. When adding RPVST+ VLANs, will new VLANs be added to the STP instance
automatically?

No. Each VLAN that is added must be added to the STP instance using command spanning-tree vlan.

7. Does RPVST+ have any per-platform capacity differences?

Yes. Refer to the platform-specific number of RPVST+ VLANs and RPVST+ vPorts under STP supported
platforms and scale.

8. Do AOS-CX switches provide Uplink Fast or Backbone Fast for faster convergence?

These are proprietary features of other vendors. RPVST+ includes equivalent functionality.

Spanning tree protocols (STP) | 233

Chapter 9

UDLD

UDLD

The Unidirectional Link Detection (UDLD) protocol enables detection of unidirectional behavior of layer 2
link. For UDLD to work, both connected devices must run the same UDLD protocol on the respective
ports.

UDLD monitors the link between two network devices and blocks the ports on both ends of the link if
the link fails. UDLD is particularly useful for detecting failures in fiber links and trunks.

In the following example each switch load balances traffic across two ports in a trunk group. Without the
UDLD feature, a link failure on a link that is not directly attached to one of the HPE switches remains
undetected. As a result, each switch continues to send traffic on the ports connected to the failed link.
When UDLD is enabled on the trunk ports on each switch, the switches detect the failed link, block the
ports connected to the failed link, and use the remaining ports in the trunk group to forward the traffic.

Similarly, UDLD is effective for monitoring fiber optic links that use two uni-direction fibers to transmit
and receive packets. Without UDLD, if a fiber breaks in one direction, a fiber port may assume the link is
still good (because the other direction is operating normally) and continue to send traffic on the
connected ports. UDLD-enabled ports; however, will prevent traffic from being sent across a bad link by
blocking the ports in the event that either the individual transmitter or receiver for that connection fails.

Ports enabled for UDLD exchange health-check packets once every seven seconds (the link-keepalive
interval). If a port does not receive a health-check packet from the port at the other end of the link within
the keepalive interval, the port waits for four more intervals. If the port still does not receive a health-
check packet after waiting for five intervals, the port concludes that the link has failed and blocks the
UDLD-enabled port.

When a port is blocked by UDLD, the event is recorded in the switch log and other port blocking
protocols, like spanning tree or meshing, will not use the bad link to load balance packets. The port will
remain blocked until the link is unplugged, disabled, or fixed. The port can also be unblocked by
disabling UDLD on the port.

Port blocking behavior is dependant on the UDLD mode in use. The previous paragraphs describe
RFC5171 Aggressive mode. Other modes behave as follows:

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

234

n RFC5171normal:Theportisnotblockedbutanotificationistriggered.
n ArubaOSverify-then-forward:Thelinksareconsideredblockeduntilbi-directionalityisconfirmed.
Afteralinkisconsideredbidirectional,iftheretriesaremetandnopacketsarereceived,thelinkis
markedasblocked.
n ArubaOSforward-then-verify:Thelinksstartupasunblocked.Afteralinkisconsideredbidirectional,
iftheretriesaremetandnopacketsarereceived,thelinkismarkedasblocked.
| Configuring | UDLD |     |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- | --- |
Procedure
1. EnableUDLDonaninterfacewiththecommandudld.
2. Formostdeployments,thedefaultvaluesforthefollowingsettingsdonotneedtobechanged.If
yourdeploymentrequiresdifferentsettings,changethedefaultvalueswiththeindicated
command:
| UDLD setting            |     | Default | value | Command       | to change | it  |
| ----------------------- | --- | ------- | ----- | ------------- | --------- | --- |
| Packettransmissiondelay |     | 7000ms  |       | udld interval |           |     |
interval.
| Operatingmode. |     | InterconnectwithHPE |     | udld mode |     |     |
| -------------- | --- | ------------------- | --- | --------- | --- | --- |
PVOS/Brocade/Foundryswitchesin
forward-then-verifymode.
| Retrycount.                                          |     | 4   |       | udld retries |     |     |
| ---------------------------------------------------- | --- | --- | ----- | ------------ | --- | --- |
| 3. ReviewUDLDconfigurationsettingswiththecommandshow |     |     | udld. |              |     |     |
Example
Thisexamplecreatesthefollowingconfiguration:
n EnablesUDLDoninterface1/1/1.
| n SetstheUDLDmodetorfc5171 |     | aggressive. |     |     |     |     |
| -------------------------- | --- | ----------- | --- | --- | --- | --- |
n SetstheUDLDintervalto1000.
n SetstheUDLDretriesto3.
switch(config)#
|                    | interface | 1/1/1              |       |     |     |     |
| ------------------ | --------- | ------------------ | ----- | --- | --- | --- |
| switch(config-if)# | mode      | rfc5171 aggressive |       |     |     |     |
| switch(config-if)# | interval  | 10000              |       |     |     |     |
| switch(config-if)# | retries   | 3                  |       |     |     |     |
| switch(config-if)# | udld      |                    |       |     |     |     |
| switch(config-if)# | quit      |                    |       |     |     |     |
| switch(config)#    | show udld | interface          | 1/1/1 |     |     |     |
| Interface 1/1/1    |           |                    |       |     |     |     |
| Config: enabled    |           |                    |       |     |     |     |
State: active
| Substate: bidirectional |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- |
Link: unblock
| Version: rfc5171 |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- |
Mode: aggressive
UDLD|235

| Interval: | 10000 milliseconds |     |     |
| --------- | ------------------ | --- | --- |
| Retries:  | 3                  |     |     |
Tx: 0 packets
| Rx: 0 | packets, 0 discarded | packets, | 0 dropped packets |
| ----- | -------------------- | -------- | ----------------- |
| Port  | transitions: 0       |          |                   |
UDLD scenario
ThisscenariodescribeshowtouseUDLDonasinglephysicalinterfaceaswellasaLAG.
Procedure
1. OnswitchA:
a. ConfiguretheUDLDsessionbetweenswitchAandB.
switch# config
|     | switch(config-if)# | interface | 1/1/1 |
| --- | ------------------ | --------- | ----- |
|     | switch(config-if)# | udld      |       |
|     | switch(config-if)# | exit      |       |
switch(config)#
b. ConfiguretheUDLDsessionbetweenswitchAandC.
|     | switch(config)#    | interface   | 1/1/2                             |
| --- | ------------------ | ----------- | --------------------------------- |
|     | switch(config-if)# | no shutdown |                                   |
|     | switch(config-if)# | no routing  |                                   |
|     | switch(config-if)# | lag         | 1                                 |
|     | switch(config-if)# | udld        | interval 400                      |
|     | switch(config-if)# | udld        | mode aruba-os verify-then-forward |
|     | switch(config-if)# | udld        | retries 5                         |
|     | switch(config)#    | exit        |                                   |
|     | switch(config)#    | interface   | 1/1/3                             |
|     | switch(config-if)# | no shutdown |                                   |
|     | switch(config-if)# | no routing  |                                   |
|     | switch(config-if)# | lag         | 1                                 |
|     | switch(config-if)# | udld        | interval 400                      |
|     | switch(config-if)# | udld        | mode aruba-os verify-then-forward |
236
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| switch(config-if)# |     |     |     | udld retries |     | 5   |     |     |     |
| ------------------ | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
2. OnswitchB,configuretheUDLDsessionbetweenswitchBandA.
| switch#            | config |     |           |     |       |     |     |     |     |
| ------------------ | ------ | --- | --------- | --- | ----- | --- | --- | --- | --- |
| switch(config-if)# |        |     | interface |     | 1/1/1 |     |     |     |     |
| switch(config-if)# |        |     | udld      |     |       |     |     |     |     |
| switch(config-if)# |        |     | exit      |     |       |     |     |     |     |
3. OnswitchC,configuretheUDLDsessionbetweenswitchCandA.
| switch#            | config |           |             |       |     |     |     |     |     |
| ------------------ | ------ | --------- | ----------- | ----- | --- | --- | --- | --- | --- |
| switch(config)#    |        | interface |             | 1/1/2 |     |     |     |     |     |
| switch(config-if)# |        |           | no shutdown |       |     |     |     |     |     |
| switch(config-if)# |        |           | no routing  |       |     |     |     |     |     |
switch(config-if)#
lag 1
| switch(config-if)# |     |           | udld        | interval | 400      |                     |     |     |     |
| ------------------ | --- | --------- | ----------- | -------- | -------- | ------------------- | --- | --- | --- |
| switch(config-if)# |     |           | udld        | mode     | aruba-os | verify-then-forward |     |     |     |
| switch(config-if)# |     |           | udld        | retries  | 5        |                     |     |     |     |
| switch(config)#    |     | exit      |             |          |          |                     |     |     |     |
| switch(config)#    |     | interface |             | 1/1/3    |          |                     |     |     |     |
| switch(config-if)# |     |           | no shutdown |          |          |                     |     |     |     |
| switch(config-if)# |     |           | no routing  |          |          |                     |     |     |     |
| switch(config-if)# |     |           | lag         | 1        |          |                     |     |     |     |
| switch(config-if)# |     |           | udld        | interval | 400      |                     |     |     |     |
switch(config-if)#
|                    |     |     | udld | mode    | aruba-os | verify-then-forward |     |     |     |
| ------------------ | --- | --- | ---- | ------- | -------- | ------------------- | --- | --- | --- |
| switch(config-if)# |     |     | udld | retries | 5        |                     |     |     |     |
4. OnswitchA,verifyUDLDconfigurationbyrunningthecommandshow udld.(Apacketmust
arriveoneachswitchforittounblocktheinterface.)
| switch# | show | udld |     |     |     |     |     |     |     |
| ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
Abbreviations:
| VTF - Verify |      | then   | forward |     | FTV - | Forward  | then verify |     |     |
| ------------ | ---- | ------ | ------- | --- | ----- | -------- | ----------- | --- | --- |
| NOR - RFC    | 5171 | normal |         |     | AGG - | RFC 5171 | aggressive  |     |     |
----------------------------------------------------------------------------
----------------------------------------------------
| Interface | UDLD   |      | UDLD  |      | UDLD     |     | UDLD Mode   | Interval |     |
| --------- | ------ | ---- | ----- | ---- | -------- | --- | ----------- | -------- | --- |
| Retries   | Tx     | Rx   | Rx    |      | Rx       |     | Transitions |          |     |
|           | Config |      | State |      | Substate |     | Link        |          |     |
| Pkts      | Pkts   | Pkts | disc. | Pkts | drop.    |     |             |          |     |
----------------------------------------------------------------------------
----------------------------------------------------
| 1/1/1 | enabled |     | active |     | Bidirectional |     | unblock FTV | 7000 | 4   |
| ----- | ------- | --- | ------ | --- | ------------- | --- | ----------- | ---- | --- |
| 0     | 0       | 0   |        | 0   |               | 0   |             |      |     |
| 1/1/2 | enabled |     | active |     | Bidirectional |     | unblock VTF | 400  | 5   |
| 2     | 2       | 0   |        | 0   |               | 1   |             |      |     |
| 1/1/3 | enabled |     | active |     | Bidirectional |     | unblock VTF | 400  | 5   |
| 2     | 2       | 0   |        | 0   |               | 1   |             |      |     |
UDLD commands
clear udld statistics
UDLD|237

| clear udld | statistics |     | [interface | <INTERFACE-NAME>] |     |
| ---------- | ---------- | --- | ---------- | ----------------- | --- |
Description
ClearsUDLDstatisticsforallinterfacesoraspecificinterface.
Examples
ClearingallUDLDstatisticsonallinterfaces:
| switch# |     | clear | udld statistics |     |     |
| ------- | --- | ----- | --------------- | --- | --- |
ClearingallUDLDstatisticsoninterface1/1/1:
| switch#        |             | clear   | udld statistics | interface | 1/1/1        |
| -------------- | ----------- | ------- | --------------- | --------- | ------------ |
| Command        | History     |         |                 |           |              |
| Release        |             |         |                 |           | Modification |
| 10.07orearlier |             |         |                 |           | --           |
| Command        | Information |         |                 |           |              |
| Platforms      |             | Command | context         |           | Authority    |
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
Manager(#)
forthiscommand.
| show      | udld       |     |                   |     |            |
| --------- | ---------- | --- | ----------------- | --- | ---------- |
| show udld | [interface |     | <INTERFACE-NAME>] |     | [vsx-peer] |
Description
DisplaysUDLDinformationforallinterfacesorforaspecificinterface.
| Parameter |     |     |     |     | Description |
| --------- | --- | --- | --- | --- | ----------- |
interface <INTERFACE-NAME> Specifiesthenameofalogicalinterfaceontheswitch,whichcan
be:
n AnEthernetinterfaceassociatedwithaphysicalport.Usethe
formatmember/slot/port(forexample,1/3/1).
n UDLDrunsonlyonphysicalinterfaces.LAGs,tunnels,andthe
likearenotsupported.However,UDLDcanbeconfigured
individuallyoneachportofaLAGortrunkgroup.Configuring
UDLDonatrunkgroupprimaryportenablesUDLDonthat
portonly.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
238
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- |

Examples
DisplayingallUDLDinformation:
switch#
show udld
Abbreviations:
| VTF - | Verify-then-forward |        | FTV - | Forward-then-verify |           |     |
| ----- | ------------------- | ------ | ----- | ------------------- | --------- | --- |
| NOR - | RFC 5171            | normal | AGG - | RFC 5171            | aggresive |     |
----------------------------------------------------------------------
| Interface | UDLD   | UDLD  | UDLD     |     | UDLD Mode | Interval |
| --------- | ------ | ----- | -------- | --- | --------- | -------- |
|           | Config | State | Substate |     | Link      |          |
----------------------------------------------------------------------
| 1/1/1 | Disabled | Inactive | Undetermined  |     | Unblock FTV | 8000 |
| ----- | -------- | -------- | ------------- | --- | ----------- | ---- |
| 1/1/2 | Enabled  | Active   | Bidirectional |     | Unblock FTV | 7000 |
| 1/1/3 | Enabled  | Active   | Blocked       |     | Block FTV   | 7000 |
| 1/1/4 | Enabled  | Inactive | Uninitialized |     | Unblock NOR | 7000 |
| 1/1/5 | Enabled  | Active   | ErrDisabled   |     | Block AGG   | 7000 |
| 1/1/6 | Disabled | Active   | Detection     |     | Unblock NOR | 7000 |
---------------------------------------------------------------
| Retries | Tx   | Rx   | Rx         | Rx   | Transitions |     |
| ------- | ---- | ---- | ---------- | ---- | ----------- | --- |
|         | Pkts | Pkts | Pkts disc. | Pkts | drop.       |     |
---------------------------------------------------------------
| 4   | 4       | 54      | 123   | 123     | 1   |     |
| --- | ------- | ------- | ----- | ------- | --- | --- |
| 7   | 1234567 | 1548421 | 23214 | 1878981 | 3   |     |
| 4   | 3       | 77871   | 2157  | 81878   | 1   |     |
| 5   | 50      | 0       | 0     | 0       | 0   |     |
| 3   | 150     | 25      | 0     | 2       | 1   |     |
| 3   | 6       | 54      | 123   | 23      | 1   |     |
Displayinginformationforinterface1/1/1:
| switch#   | show udld     | interface | 1/1/1 |     |     |     |
| --------- | ------------- | --------- | ----- | --- | --- | --- |
| Interface | 1/1/1         |           |       |     |     |     |
| Config:   | Enabled       |           |       |     |     |     |
| State:    | Active        |           |       |     |     |     |
| Substate: | Bidirectional |           |       |     |     |     |
Link: Unblock
| Version:    | Aruba   | OS           |     |     |     |     |
| ----------- | ------- | ------------ | --- | --- | --- | --- |
| Mode:       | Forward | then verify  |     |     |     |     |
| Interval:   | 7000    | milliseconds |     |     |     |     |
| Retries:    | 7       |              |     |     |     |     |
| Tx: 1234567 | packets |              |     |     |     |     |
Rx: 1548421 packets, 23214 discarded packets, 1878981 dropped packets
| Port | transitions: | 3   |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- | --- |
DisplayingtheUDLDenableinterfacesinformation:
| switch# | show udld | enabled |     |     |     |     |
| ------- | --------- | ------- | --- | --- | --- | --- |
Abbreviations:
| VTF - | Verify-then-forward |        | FTV - | Forward-then-verify |           |     |
| ----- | ------------------- | ------ | ----- | ------------------- | --------- | --- |
| NOR - | RFC 5171            | normal | AGG - | RFC 5171            | aggresive |     |
----------------------------------------------------------------------------------
---------------------------------------------------
UDLD|239

| Interface |     | UDLD   | UDLD       |      | UDLD     | UDLD Mode   | Interval | Retries Tx |
| --------- | --- | ------ | ---------- | ---- | -------- | ----------- | -------- | ---------- |
|           | Rx  |        | Rx         | Rx   |          | Transitions |          |            |
|           |     | Config | State      |      | Substate | Link        |          |            |
| Pkts      |     | Pkts   | Pkts disc. | Pkts | drop.    |             |          |            |
----------------------------------------------------------------------------------
---------------------------------------------------
| 2              |             | Enabled | Active   |         | Bidirectional | Unblock FTV | 7000 | 7    |
| -------------- | ----------- | ------- | -------- | ------- | ------------- | ----------- | ---- | ---- |
| 1234567        |             | 1548421 | 23214    | 1878981 |               | 3           |      |      |
| 3              |             | Enabled | Active   |         | Blocked       | Block FTV   | 7000 | 4 3  |
|                | 77871       |         | 2157     | 81878   |               | 1           |      |      |
| 4              |             | Enabled | Inactive |         | Uninitialized | Unblock NOR | 7000 | 5 50 |
|                | 0           |         | 0        | 0       |               | 0           |      |      |
| 5              |             | Enabled | Active   |         | ErrDisabled   | Block AGG   | 7000 | 3    |
| 150            |             | 25      | 0        | 2       |               | 1           |      |      |
| Command        | History     |         |          |         |               |             |      |      |
| Release        |             |         |          |         | Modification  |             |      |      |
| 10.07orearlier |             |         |          |         | --            |             |      |      |
| Command        | Information |         |          |         |               |             |      |      |
| Platforms      |             | Command | context  |         | Authority     |             |      |      |
Allplatforms OperatorsorAdministratorsorlocalusergroupmemberswith
Operator(>)orManager
|     |     | (#) |     |     | executionrightsforthiscommand.Operatorscanexecutethis |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
commandfromtheoperatorcontext(>)only.
udld
udld [disable]
no udld [disable]
Description
EnablesUDLDsupportonaphysicalinterface.UDLDisdisabledbydefault.UDLDisconfiguredonaper-
portbasisandmustbeenabledatbothendsofthelink.
UDLDrunsonlyonphysicalinterfaces.LAGs,tunnels,andthelikearenotsupported.However,UDLD
canbeconfiguredindividuallyoneachportofaLAGortrunkgroup.ConfiguringUDLDonatrunk
group'sprimaryportenablesUDLDonthatportonly.
ThenoformofthiscommanddisablesUDLDsupportandresetsallconfigurationvaluestotheirdefault
settings.
| Parameter |     |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
disable DisablesUDLDontheinterfacebutretainsallUDLDconfiguration
settings.
Examples
EnablingUDLDoninterface1/1/1:
240
| AOS-CX10.12Layer-2BridgingGuide| |     |     | 8400SwitchSeries |     |     |     |     |     |
| -------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- |

| switch(config)# | interface | 1/1/1 |     |
| --------------- | --------- | ----- | --- |
switch(config-if)#
udld
DisablingUDLDoninterface1/1/1:
| switch(config)#     | interface | 1/1/1   |              |
| ------------------- | --------- | ------- | ------------ |
| switch(config-if)#  |           | no udld |              |
| Command History     |           |         |              |
| Release             |           |         | Modification |
| 10.07orearlier      |           |         | --           |
| Command Information |           |         |              |
| Platforms           | Command   | context | Authority    |
config-if
Allplatforms Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
udld interval
| udld interval    | <TIME>   |     |     |
| ---------------- | -------- | --- | --- |
| no udld interval | [<TIME>] |     |     |
Description
Setsthepackettransmissioninterval.
Thenoformofthiscommandsetsthepackettransmissionintervaltothedefaultvalueof7000ms.
Theallowedvaluesvarydependingontheoperationmode.
Thedefaultintervalis7000ms(7seconds)forbothArubaOS-SwitchandRFC5171operationmodes.
Valuesmustbespecifiedasmultiplesof10ms(7000msisallowedbut7005msisnotavalidsetting).
Sessionsunder100mstotaldetectiontimearesusceptibletoincreasingprocessingloadonthesystem.Itis
advisabletoexperimentwithvaluesthatprovideadequatedetectiontimesandsystem/protocolstability.Aruba
recommendsadditionaltestingpriortoconfiguringthesesessionsonaproductionenvironment.
However,thesesettingsarerecommendedforspecificdeploymentsonly,suchasusingUDLDfor
EthernetRingProtectionSwitching(ERPS)link-failuredetection.Theminimumdetectiontime
appropriateforyourenvironmentdependsonthespecificdevicefamilyandconfigurationonwhichthe
protocolandsystemloadisrunning.Arubarecommendsadditionaltestingfortheseconfigurations.
Duringtesting,monitorforunexpectedfalsepositivedetections(i.e.,UDLDrecordsafailurewhenthere
wasnotany)ontheinterfacesrunningUDLD.Suchfalsepositivefailuresareanindicationthatthe
intervalconfigurationrequirestuningandthatthesystemloadmightnotallowsuchconfiguration.
UDLD|241

Whenconfiguringdetectiontimesunder100msforLAGinterfaces,consideraddingtheinterfacefirsttotheLAG
andthenenablingUDLDintheinterface,toavoidfalsepositivelinkfailuredetections.Addinganinterfacetoa
LAGcausesmomentarycontrolplanetrafficinterruptionforupto100ms,whichUDLDdetectsasalinkfailureif
thedetectiontimeisfollowingthecontroltrafficinterruptioninterval.
Parameter Description
<TIME> Specifiesthepackettransmissioninterval.Range:200msto90000
ms(inincrementsof10).
Examples
Settingthepackettransmissionintervalto1000msoninterface1/1/1.
| switch(config)#    | interface | 1/1/1         |
| ------------------ | --------- | ------------- |
| switch(config-if)# | udld      | interval 1000 |
Settingthepackettransmissionintervaloninterface1/1/1tothedefaultvalue.
| switch(config)#    | interface | 1/1/1    |
| ------------------ | --------- | -------- |
| switch(config-if)# | no udld   | interval |
Tryingtosetthepacketintervalto1055msoninterface1isrejectedbecausetheintervalmustbe
specifiedasamultipleof10:
| switch(config)#    | interface | 1             |
| ------------------ | --------- | ------------- |
| switch(config-if)# | udld      | interval 1055 |
Invalid interval. The interval value must be between 20ms and 90000ms and should
be
specified as a multiple of 10, for example: 20, 100, 3000 or 90000.
Tryingtosetthepacketintervaltolessthan7000msoninterface1isrejectedifusingtheRFC5171
mode.
| switch(config)#    | interface | 1                   |
| ------------------ | --------- | ------------------- |
| switch(config-if)# | udld      | mode rfc5171 normal |
| switch(config-if)# | udld      | interval 1000       |
Invalid interval. The interval must be equal or greater than 7000ms.
Command History
Release Modification
10.07orearlier --
Command Information
242
AOS-CX10.12Layer-2BridgingGuide| 8400SwitchSeries

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
udld mode
| udld mode | aruba-os {verify-then-forward |     | | forward-then-verify} |
| --------- | ----------------------------- | --- | ---------------------- |
| udld mode | rfc5171 <RFC5171-MODE>        |     |                        |
no udld mode [[aruba-os [verify-then-forward | forward-then-verify]] | [rfc5171
[<RFC5171-MODE>]]]
Description
Setstheoperatingmode.
Thenoformofthiscommandsetstheoperatingmodetothedefaultvalueofaruba-osandforward-
then-verify.
| Parameter |                      |     | Description |
| --------- | -------------------- | --- | ----------- |
| aruba-os  | {verify-then-forward | |   |             |
SelectstheArubaOSmodetouse.Usethismodewhen
forward-then-verify} interconnectingwithHPEPVOS/Brocade/Foundryswitches.
| verify-then-forward |     |     | Inthismode: |
| ------------------- | --- | --- | ----------- |
n Interfacesstartasunblocked.
n Onceaninterfaceisdeterminedtobebidirectional,itis
blockediftheretrylimitisreachedwithoutreceivinganyUDLD
packets.
n InterfacesautomaticallyunblockifaUDLDpacketisreceived.
n Onfailover,theUDLDstatedoesnotchangeifthe(interval*
retries)timeisaround6seconds.
| forward-then-verify |     |     | Inthismode: |
| ------------------- | --- | --- | ----------- |
n Interfacesstartasunblocked.
n Interfacestransitiontotheunblockedstatewhenreceiving
UDLDpackets.
n Onceaninterfaceisdeterminedtobebidirectional,itis
blockediftheretrylimitisreachedwithoutreceivinganyUDLD
packets.
n InterfacesautomaticallyunblockifaUDLDpacketisreceived.
| rfc5171 | <RFC5171-MODE> |     |     |
| ------- | -------------- | --- | --- |
SelectstheRFC5171modetouse.Usethismodewhen
interconnectingwiththird-partyswitches.
| normal |     |     | Inthismode: |
| ------ | --- | --- | ----------- |
n Interfacesstartasunblocked.
n Interfacesdonotblockwhentheretrylimitisreachedwithout
receivinganyUDLDpackets(plus8extrapacketssenttothe
peer).Instead,aneventisgenerated.
n InterfacesautomaticallyunblockifaUDLDpacketisreceived.
| aggressive |     |     | Inthismode: |
| ---------- | --- | --- | ----------- |
n Interfacesstartasunblocked.
UDLD|243

| Parameter |     |     |     | Description |
| --------- | --- | --- | --- | ----------- |
n Onceaninterfaceisdeterminedtobebidirectional,an
interfacewillblockwhentheretrylimitisreachedwithout
receivinganyUDLDpackets(plus8extrapacketssenttothe
peer).
n Interfacesimplementalimited/reducederrDisabledrecovery
mechanism.Whentheinterface'sstategoestoerrDisabled,a
maximumof3attempts(5minutesapart)aretriggeredtotry
andbringuptheinterfaceincasetheremoteendpointisstill
sendingUDLDpackets.Afterthese3retries,theinterfacewill
remainblockedevenifUDLDpacketsarereceived.Theonly
waytounblocktheinterfacewhenthisoccursistodisable
(andoptionallyre-enable)UDLDontheinterface.Theretry
limitisresetoncetheinterfacebecomesunblocked.
Examples
Settingtheoperatingmodetoaruba-osandforward-then-verifyoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1         |                     |
| ------------------ | --- | --------- | ------------- | ------------------- |
| switch(config-if)# |     | udld      | mode aruba-os | forward-then-verify |
Settingtheoperatingmodetorfc5171andaggressiveoninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1        |            |
| ------------------ | --- | --------- | ------------ | ---------- |
| switch(config-if)# |     | udld      | mode rfc5171 | aggressive |
Settingtheoperatingmodeoninterface1/1/1tothedefaultvalue:
| switch(config)#     |         | interface | 1/1/1 |              |
| ------------------- | ------- | --------- | ----- | ------------ |
| switch(config-if)#  |         | no udld   | mode  |              |
| Command History     |         |           |       |              |
| Release             |         |           |       | Modification |
| 10.07orearlier      |         |           |       | --           |
| Command Information |         |           |       |              |
| Platforms           | Command | context   |       | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
udld retries
| udld retries    | <COUNT>   |     |     |     |
| --------------- | --------- | --- | --- | --- |
| no udld retries | [<COUNT>] |     |     |     |
244
| AOS-CX10.12Layer-2BridgingGuide| |     | 8400SwitchSeries |     |     |
| -------------------------------- | --- | ---------------- | --- | --- |

Description
SetstheUDLDretrycount.
Thenoformofthiscommandsetstheretrycounttothedefaultof4.
| Parameter |     |     |     | Description                                       |
| --------- | --- | --- | --- | ------------------------------------------------- |
| <COUNT>   |     |     |     | SpecifiestheUDLDretrycount.Range:3to10.Default:4. |
Examples
SettingtheUDLDretrycountto5oninterface1/1/1:
| switch(config)#    |     | interface | 1/1/1   |     |
| ------------------ | --- | --------- | ------- | --- |
| switch(config-if)# |     | udld      | retries | 5   |
SettingtheUDLDretrycountoninterface1/1/1tothedefaultvalue:
| switch(config)#     |         | interface | 1/1/1   |              |
| ------------------- | ------- | --------- | ------- | ------------ |
| switch(config-if)#  |         | no udld   | retries |              |
| Command History     |         |           |         |              |
| Release             |         |           |         | Modification |
| 10.07orearlier      |         |           |         | --           |
| Command Information |         |           |         |              |
| Platforms           | Command | context   |         | Authority    |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecutionrights
forthiscommand.
UDLD|245

Support and Other Resources

Chapter 10

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

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

246

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
SupportandOtherResources|247

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

AOS-CX 10.12 Layer-2 Bridging Guide | 8400 Switch Series

248