AOS-CX 10.16.xxxx ACLs and
Classifier Policies Guide

(832x, 93xx, 100xx Switch Series)

Published: October 2025

Version: 1

Copyright Information

© Copyright 2025 Hewlett Packard Enterprise Development LP.

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

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

2

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

| 3

Contents
| About                                                   | this document                          |       | 6   |
| ------------------------------------------------------- | -------------------------------------- | ----- | --- |
| Applicableproducts                                      |                                        |       | 6   |
| Latestversionavailableonline                            |                                        |       | 6   |
| Commandsyntaxnotationconventions                        |                                        |       | 6   |
| Abouttheexamples                                        |                                        |       | 7   |
| Identifyingswitchportsandinterfaces                     |                                        |       | 8   |
| Access                                                  | Control                                | Lists | 9   |
| ACLusagetips                                            |                                        |       | 10  |
| Aboutaddressandportobjectgroups                         |                                        |       | 11  |
| VLANACLsandinteractionwithVXLANtraffic                  |                                        |       | 12  |
|                                                         | InteractionswithVXLANtrafficonanL2VNI  |       | 12  |
|                                                         | InteractionswithVxLANtrafficonanL3VNI  |       | 13  |
| ACLandACE-relatedtasks                                  |                                        |       | 13  |
| Objectgroup-relatedtasks                                |                                        |       | 15  |
| ActiveACLconfigurationversususer-specifiedconfiguration |                                        |       | 16  |
| ACLcommands                                             |                                        |       | 18  |
|                                                         | ACLapplication                         |       | 18  |
|                                                         | access-listcopy                        |       | 19  |
|                                                         | access-listip                          |       | 23  |
|                                                         | access-listipv6                        |       | 34  |
|                                                         | access-listlog-timer                   |       | 43  |
|                                                         | access-listmac                         |       | 45  |
|                                                         | access-listresequence                  |       | 51  |
|                                                         | access-listreset                       |       | 53  |
|                                                         | access-listsecure-update               |       | 57  |
|                                                         | applyaccess-listcontrol-plane          |       | 58  |
|                                                         | applyaccess-list(tointerfaceorLAG)     |       | 59  |
|                                                         | applyaccess-list(tointerfaceVLAN)      |       | 61  |
|                                                         | applyaccess-list(toL3VNI)              |       | 63  |
|                                                         | applyaccess-list(tosubinterface)       |       | 65  |
|                                                         | applyaccess-list(toVLAN)               |       | 67  |
|                                                         | clearaccess-listhitcounts              |       | 68  |
|                                                         | clearaccess-listhitcountscontrol-plane |       | 70  |
|                                                         | object-groupaddressresequence          |       | 70  |
|                                                         | object-groupaddressreset               |       | 71  |
|                                                         | object-groupallreset                   |       | 72  |
|                                                         | object-groupipaddress                  |       | 72  |
|                                                         | object-groupipv6address                |       | 74  |
|                                                         | object-groupport                       |       | 76  |
|                                                         | object-groupportresequence             |       | 79  |
|                                                         | object-groupportreset                  |       | 79  |
|                                                         | showaccess-list                        |       | 80  |
|                                                         | showaccess-listcontrol-plane           |       | 85  |
|                                                         | showaccess-listhitcounts               |       | 87  |
|                                                         | showaccess-listhitcountscontrol-plane  |       | 90  |
|                                                         | showaccess-listsecure-update           |       | 91  |
|                                                         | showcapacities                         |       | 91  |
|                                                         | showcapacities-status                  |       | 93  |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide| (832x,93xx,
4
100xxSwitchSeries)

|                              | showobject-group |     |     |     | 96  |
| ---------------------------- | ---------------- | --- | --- | --- | --- |
| IPv4ACLexampleoverview       |                  |     |     |     | 99  |
| DefiningandapplyinganIPv4ACL |                  |     |     |     | 99  |
| IPv6ACLexampleoverview       |                  |     |     |     | 100 |
| DefiningandapplyinganIPv6ACL |                  |     |     |     | 101 |
| Classifier                   | policies         |     |     |     | 103 |
| Trafficpolicing              |                  |     |     |     | 103 |
| Typesofpolicyactions         |                  |     |     |     | 104 |
| Howpolicymatchingworks       |                  |     |     |     | 105 |
| Limitations                  |                  |     |     |     | 105 |
Activeclassconfigurationversususer-specifiedconfiguration 105
Activepolicyconfigurationversususer-specifiedconfiguration 106
|                          | Considerationsforwhenapolicyisappliedperinterface |     |     |     | 107 |
| ------------------------ | ------------------------------------------------- | --- | --- | --- | --- |
| Classifierpolicycommands |                                                   |     |     |     | 109 |
|                          | Classifierpolicyapplication                       |     |     |     | 109 |
applypolicy(config-if,config-lag-if,config-if-vlan,config-vlan) 110
|                                           | applypolicy                           |               |          |                | 114 |
| ----------------------------------------- | ------------------------------------- | ------------- | -------- | -------------- | --- |
|                                           | classcopy                             |               |          |                | 115 |
|                                           | classip                               |               |          |                | 117 |
|                                           | classipv6                             |               |          |                | 124 |
|                                           | classmac                              |               |          |                | 130 |
|                                           | classresequence                       |               |          |                | 134 |
|                                           | classreset                            |               |          |                | 136 |
|                                           | clearpolicyhitcounts                  |               |          |                | 137 |
|                                           | policy                                |               |          |                | 138 |
|                                           | policycopy                            |               |          |                | 142 |
|                                           | policyresequence                      |               |          |                | 143 |
|                                           | policyreset                           |               |          |                | 144 |
|                                           | showclass                             |               |          |                | 145 |
|                                           | showpolicy                            |               |          |                | 146 |
| Classifier                                | policies                              | configuration | example  |                | 153 |
| Configuringtheclassifierpoliciesexample   |                                       |               |          |                | 153 |
| ACL and                                   | Policy                                | hardware      | resource | considerations | 156 |
| ShowResources                             |                                       |               |          |                | 156 |
|                                           | EventLogs                             |               |          |                | 156 |
|                                           | Limitationsandexclusions              |               |          |                | 157 |
| TCAMresourceconsumptionandlookups         |                                       |               |          |                | 157 |
|                                           | Forthe8320Switchseries:               |               |          |                | 157 |
| Matchingprecedenceorder                   |                                       |               |          |                | 181 |
| PolicerActionConsiderationsandLimitations |                                       |               |          |                | 182 |
|                                           | SubinterfaceApplicationConsiderations |               |          |                | 183 |
|                                           | MeteringandRemarking                  |               |          |                | 183 |
| L4portranges                              |                                       |               |          |                | 184 |
| ACLandPolicyhardwareresourcecommands      |                                       |               |          |                | 185 |
|                                           | showresources                         |               |          |                | 185 |
| Support                                   | and Other                             | Resources     |          |                | 187 |
| AccessingHPEArubaNetworkingSupport        |                                       |               |          |                | 187 |
| AccessingUpdates                          |                                       |               |          |                | 188 |
| WarrantyInformation                       |                                       |               |          |                | 188 |
| RegulatoryInformation                     |                                       |               |          |                | 188 |
| DocumentationFeedback                     |                                       |               |          |                | 188 |
|5

Chapter 1

About this document

About this document

This document describes features of the AOS-CX network operating system. It is intended for
administrators responsible for installing, configuring, and managing HPE Aruba Networking switches on
a network.

Applicable products

This document applies to the following products:

n HPE Aruba Networking 8320 Switch Series (JL479A, JL579A, JL581A)

n HPE Aruba Networking 8325 Switch Series (JL624A, JL625A, JL626A, JL627A)

n HPE Aruba Networking 8325H Switch Series (S4B20A, S4B21A, S4B22A, S4B23A, S2T42A, S2T46A,

S2T47A, S2T48A)

n HPE Aruba Networking 8325P Switch Series (S0G12A, S4A48A)

n HPE Aruba Networking 9300 Switch Series (R9A29A, R9A30A, R8Z96A, S0F81A, S0F82A, S0F83A)

n HPE Aruba Networking 9300S Switch Series (S0F81A, S0F82A, S0F83A, S0F84A, S0F85A, S0F86A,

S0F88A, S0F95A, S0F96A)

n HPE Aruba Networking 10000 Switch Series (R8P13A, R8P14A)

n HPE Aruba Networking 10040 Switch Series (S4R58A, S4R59A)

Latest version available online

Updates to this document can occur after initial publication. For the latest versions of product
documentation, see the links provided in Support and Other Resources.

Command syntax notation conventions

Convention

example-text

Usage

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

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

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

Where <VLAN-ID> is a variable representing the VLAN number.

About this document | 7

Identifying switch ports and interfaces

Physical ports on the switch and their corresponding logical software interfaces are identified using the
format: member/slot/port.

On the HPE Aruba Networking 8xxx, 93xx, and 10xxx Switch Series

n member: Always 1. VSF is not supported on this switch.

n slot: Always 1. This is not a modular switch, so there are no slots.

n port: Physical number of a port on the switch.

For example, the logical interface 1/1/4 in software is associated with physical port 4 on the switch.

If using breakout cables, the port designation changes to x:y, where x is the physical port and y is the lane when

split. For example, the logical interface 1/1/4:2 in software is associated with lane 2 on physical port 4 in slot 1 on

member 1.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

8

Chapter 2

Access Control Lists

Access Control Lists
Access Control Lists (ACLs) let a network administrator permit or deny passage of traffic based on
network addresses, protocols, service ports, and other packet attributes. ACLs are composed of one or
more Access Control Entries (called ACEs). Each ACE defines a filter criteria and an action, either permit
or deny. If the traffic matches the filter criteria, the specified action is taken. The permit action permits
the traffic to continue through the switch. The deny action causes the traffic to be discarded (dropped).
ACEs can also log or count matching traffic.

Three ACL types are supported; IPv4, IPv6, and MAC. Each ACL type is focused on relevant frame or
packet characteristics.

ACLs must be applied (using an apply access-list command) to take effect. ACLs can be applied to
interfaces (including LAGs), VLANs, or the Control Plane.

Access Control Entries (ACEs) are listed according to priority by sequence number and processed in
lowest to highest sequence number order. Each ACE attempts to match on one or more attributes of the
particular traffic type. Attempted ACE matching ceases upon the first successful match. For a match to
be considered successful, a packet must match all the criteria, qualifiers, and attributes of a particular
ACE. Higher-numbered ACEs are only processed if no lower-numbered ACE matches. If the traffic
matches no ACE in the entire ACL, the default action deny is taken, causing the traffic to be discarded
(dropped).

When defining an ACE, if the sequence number is omitted, the ACE is auto-assigned a new sequence
number that is 10 greater than the existing highest ACE sequence number. The first auto-assigned
sequence number is 10. If you choose to include the ACE sequence numbers, you can use any number
you like, however it is suggested that you follow the practice of entering them as 10, 20, 30, and so on.
Regardless of the order in which ACEs are entered, they are stored in low-to-high sequence number
order. If you enter three ACEs numbered 10, 30, 20, when creating an ACL, the ACEs are stored in the
ACL as 10, 20, 30.

This simple ACL definition permits traffic passage for a particular address range and otherwise counts all
nonmatching (dropped) traffic:

switch(config)# access-list ip network-A-udp-only
switch(config-acl-ip)# 10 permit udp any 172.16.1.0/24
switch(config-acl-ip)# 20 deny any any any count
switch(config-acl-ip)# exit

The main traffic characteristics that ACEs can filter on are as follows (see the full list in the ACE
parameters list of the ACL commands):

n Protocol such as: ICMP, TCP, UDP

n Source and/or destination addresses (IPv4, IPv6, or MAC)

n Source and/or destination TCP/UDP ports (if applicable to the specified protocol)

A few real-world uses of ACLs are as follows:

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

9

n Restrict traffic arriving on a routed port, destined to a particular address or subnet by applying an

ACL that matches on a destination IP address or an IP address and a mask.

n Prevent an entire subnet from routing through a port by applying an ACL that matches on IP source

address and a mask.

n Prevent certain protocols from using a particular multicast MAC address (advertising through a port)

by applying an ACL that matches on the destination MAC address.

n Prevent any IP host from accessing a particular IP port/application on a specific server by applying an

ACL that matches on IP addresses and Layer 4 port.

See also ACL and Policy hardware resource considerations.

ACL usage tips

When using the access-list ip or access-list ipv6 commands, if you enter an existing ACL-NAME,
the existing ACL is modified as follows:

n Any ACE entered with a new sequence-number creates an additional ACE.

n Any ACE entered with an existing sequence-number replaces the existing ACE.

If you modify an ACL that has already been applied, it is possible that packets, blocked by the previous
ACL, will briefly pass through the switch during the ACL reconfiguration.

In a highly secure environment, it is safest to first bring down interfaces and VLANs to which an ACL has been

applied before modifying the ACL. Then bring the targets of ACL application back up after completing the ACL

modification. Respecting this recommendation ensures that an ACL is never partially programmed while traffic is

passing through the switch.

About applying ACLs to interfaces or LAGs

You can apply an ACL to an interface or LAG to affect or control the traffic arriving on that interface or
LAG (inbound) or leaving the interface or LAG (outbound), or both. A given interface or LAG supports the
application of a single ACL per type, per direction. ACLs can be applied to interfaces or LAGs as follows:

n One MAC ACL inbound

n One IPv4 ACL inbound

n One IPv4 ACL outbound

n One IPv6 ACL inbound

Different ACLs of the same type can be used in opposite directions for IPv4. If you apply an ACL of a
particular type, in a direction that is already in use, the switch replaces the current ACL with the new
ACL.

About applying ACLs to VLANs

ACLs can be applied to VLANs only in the inbound (ingress) direction.

Sequence numbering

If no sequence number is specified, the software appends new ACEs to the end of the ACL with a
sequence number equal to the highest ACE currently in the list plus 10.

The sequence numbers may be resequenced using the access-list resequence command.

Access Control Lists | 10

Deny ACLs
IfmultipleACLsofdifferenttypesareappliedinthesamedirection,adenyACE,whetherexplicitor
implicit,inoneACLoverridesapermitACLinanother.AdenyACEisanACEwithinanACLthatusesthe
denyactionkeyword.
| Denied | ping requests |     |     |     |     |     |
| ------ | ------------- | --- | --- | --- | --- | --- |
ApingrequestisdeniedwhenanACLisappliedoningressoregressunlesstherequestisexplicitly
permitted.
| switch#     | ping       | 100.1.2.10   |     |                |          |     |
| ----------- | ---------- | ------------ | --- | -------------- | -------- | --- |
| PING        | 100.1.2.10 | (100.1.2.10) |     | 100(128) bytes | of data. |     |
| ping:       | sendmsg:   | Operation    | not | permitted      |          |     |
| ping:       | sendmsg:   | Operation    | not | permitted      |          |     |
| ping:       | sendmsg:   | Operation    | not | permitted      |          |     |
| ping:       | sendmsg:   | Operation    | not | permitted      |          |     |
| ping:       | sendmsg:   | Operation    | not | permitted      |          |     |
| ACL failure | behaviors  |              |     |                |          |     |
n IntheeventofafailedACLapplicationtoaVLANorVLANinterfaceduringaswitchreboot,allofthe
portswillshutdown.Theswitchmustberestartedtorecoverfromthefailure.ModifyingtheVLAN,
VLANinterface,orACLconfigurationwillnotcausetheswitchtoberestarted.
n IntheeventofafailedACLapplicationtoasubinterfaceduringswitchreboot,thesubinterfacewill
beshutdown.Theswitchmustberestartedtorecoverfromthefailure.Modifyingthesubinterface
orACLconfigurationwillnotcausetheswitchtoberestarted.
n IntheeventofafailedACLapplicationtoasubinterfaceduringhotswaporswitchreboot,the
subinterfacewillbeshutdown.Thelinecardorstackmembermustberestartedorhotswappedto
recoverfromthefailure.ModifyingthesubinterfaceorACLconfigurationwillnotcausethelinecard
orstackmembertoberestarted.IntheeventofafailedACLapplicationtooneormoreadded
subinterfaceLAGmembers,thesubinterfacewillbeshutdown.Forthistooccur,theACLmust
alreadybesuccessfullyappliedtoexistingsubinterfaceLAGmembers.Thisisdonetopreventtraffic
fromcircumventingtheACLbypassingthroughnewLAGmemberswheretheACLwasnot
successfullyapplied.Thelinecardorstackmembermustberestartedorhotswappedtorecover
fromthefailure.ModifyingthesubinterfaceorACLconfigurationwillnotcausethelinecardorstack
membertoberestarted.
| ACLs and | VXLAN Traffic |     |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- | --- |
ACLsappliedtoanSVIwillnotmatchonVxLANtrafficoveraVNI.
| About | address | and | port | object | groups |     |
| ----- | ------- | --- | ---- | ------ | ------ | --- |
ObjectgroupsareusefulfordefininggroupsofIPaddressesandLayer4portsforuseexclusivelyinthe
| twoACL-definingcommandsaccess-list |     |     |     | ipandaccess-list |     | ipv6. |
| ---------------------------------- | --- | --- | --- | ---------------- | --- | ----- |
Often,commongroupsofaddressesandportsorportrangesareusedrepeatedlyinmanyACL
definitions.Withoutaddressandportobjectgroups,thesameaddressesandportsmustberepeatedin
eachACLdefinitionthatusesthem.
Withaddressandportobjectgroups,theIPaddressesandportscanbedefinedonce,usinganyof
thesecommands:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 11

n object-group ip address

n object-group ipv6 address

n object-group port

Once an object group is defined, the group is available for inclusion by name as the <ADDRESS-GROUP>
and <PORT-GROUP> parameters in the access-list ip and access-list ipv6 ACL-definition
commands.

Object groups simplify the ACL definition process and help ensure consistent address and port
specification across many ACLs.

Keep in mind that it is possible to consume many hardware resource entries when using the object group

commands. For example, in a typical situation, an ACE that uses object groups with 3 source addresses, 3 source

L4 ports, 3 destination addresses, and 3 destination L4 ports, a total of 81 hardware entries are consumed (3 * 3

* 3 * 3 = 81).

VLAN ACLs and interaction with VXLAN traffic

This section applies to these AOS-CX platforms that support VXLAN and VXLAN ACLs: 5420, 6200, 6300, 6400,

8100, 8325, 8360, 9300/9300S, 10000.

VLAN policies applied to an SVI will not match VXLAN traffic over a VNI.

Interactions with VXLAN traffic on an L2 VNI

The way VLAN ACLs interact with VLAN traffic carried by VXLAN tunnels depends on the AOS-CX
platform.

For the purposes of this discussion, VLAN traffic is Ethernet traffic with an IP payload. VXLAN traffic
includes a VXLAN header, encapsulating the Ethernet frame and IP header into the VXLAN UDP packet.
VLAN traffic can be considered to be "normal" L2 traffic, and VXLAN traffic can be considered to be
"tunneled" (encapsulated) L2 traffic.

VLAN ACL matching of VLAN traffic arriving through a VXLAN tunnel is available on the various AOS-CX
platforms as follows:

n On the 5420, 6200, 6400, 6400, 8100, and 8360, VLAN ACLs are able to match decapsulated VLAN

traffic arriving through a VXLAN tunnel, however, VLAN ACLs are unable to match VLAN traffic leaving
the switch through a VXLAN tunnel.

n On the 8325, 9300/9300S, and 10000, ingress VLAN ACLs are able to match decapsulated VLAN traffic

arriving through a VXLAN tunnel.

n On the 8325, 9300/9300S, and 10000, egress VLAN ACLs are not able to match decapsulated VLAN
traffic arriving through a VXLAN tunnel. VLAN ACLs are able to match on the VXLAN IP in this case
(packets egressing to the VXLAN tunnel).

n On the 8400, ingress VLAN ACLs are not able to match decapsulated VLAN traffic arriving through a
VXLAN tunnel. The 8400 does not support egress VLAN ACLs. Instead they can match on the VXLAN
IP.

VLAN ACLs do not match on the inner VXLAN header (encapsulated packet).

Consider the following two-node VXLAN L2 bridging topology:

Access Control Lists | 12

| Host-1 <--> | Switch-1 | <--> Switch-2 | <--> | Host-2 |     |     |     |
| ----------- | -------- | ------------- | ---- | ------ | --- | --- | --- |
EachswitchhasasingleVLAN,connectedwithVXLANVTEPs,andeachhostisconnectedtotheVLANon
therespectiveswitch.ThefourrelevantcontrolpointsforACLapplicationareasfollows:
1. Switch-1Ingress
2. Switch-1Egress
3. Switch-2Ingress
4. Switch-2Egress
FortrafficinitiatedfromHost-1toHost-2:
1. AtSwitch-1(Ingress)thepacketfromHost-1isstillanormalVLANpacket,thereforeIngressVLAN
ACLscanbeappliedhere.
2. AtSwitch-1(Egress)thepacketfromHost-1hasbeenencapsulatedintoaVXLANUDPtunnel
packet,andthereforeEgressVLANACLscannotbeappliedhere.
3. AtSwitch-2(Ingress)thepacketfromHost-1isdecapsulatedfromitsVXLANheadersothatitcan
bedeliveredtothelocalVLANassociatedwiththeVXLANVTEP.OnAOS-CX platformsthat
supportit,ingressVLANACLscanbeappliedhere.
4. AtSwitch-2(Egress)thepacketwhicharrivedfromSwitch-1hasbeendecapsulatedandbecomes
anormalVLANpacketonegress,andtherefore,onAOS-CXplatformsthatsupportit,EgressVLAN
ACLscanbeappliedhere.
Separately,considerthisthree-switchtopology:
| Host-1 <--> | Switch-1 | <--> Switch-M | <--> | Switch-2 | <--> | Host-2 |     |
| ----------- | -------- | ------------- | ---- | -------- | ---- | ------ | --- |
Inthistopology,trafficfromthehostsisneverdecapsulatedonthemiddleswitch,Switch-M.Therefore,
Switch-MsimplyforwardstheVXLANUDPframesbackandforth.Sincethepacketisnotdecapsulated,
theVLANACLscannotbeappliedonSwitch-M.
| Interactions | with | VxLAN | traffic | on  | an L3 | VNI |     |
| ------------ | ---- | ----- | ------- | --- | ----- | --- | --- |
AllVNIsthathaveroutingenabledareconsideredL3VNIs.AcommonusecaseforanL3VNIwouldbea
symmetricIRBtopology.SymmetricIRBusesthesamelayer-3VNIforbidirectionaltrafficbetweentwo
hostsondifferentVNIs.
PoliciesappliedtoVLANsdonotmatchontrafficbeingroutedoveranL3VNI.
| ACL and | ACE-related |     | tasks |     |     |     |     |
| ------- | ----------- | --- | ----- | --- | --- | --- | --- |
CommonACLandACE-relatedtasksareasfollows:
| Task              |     | Command     | name |     | Example     |                       |             |
| ----------------- | --- | ----------- | ---- | --- | ----------- | --------------------- | ----------- |
| CreatinganIPv4ACL |     | access-list | ip   |     | access-list | ip MY_IP_ACL          |             |
|                   |     |             |      |     | 10 permit   | udp any 172.16.1.0/24 |             |
|                   |     |             |      |     | 20 permit   | tcp 172.16.2.0/16     | gt 1023 any |
|                   |     |             |      |     | 30 deny     | any any any count     |             |
|                   |     |             |      |     | access-list | ipv6 MY_IPV6_ACL      |             |
| CreatinganIPv6ACL |     | access-list | ipv6 |     |             |                       |             |
|                   |     |             |      |     | 10 permit   | udp any 2001::1/64    |             |
|                   |     |             |      |     | 20 permit   | tcp 2001:2011::1/64   | any         |
|                   |     |             |      |     | 30 deny     | any any any count     |             |
| CreatingaMACACL   |     | access-list | mac  |     | access-list | mac MY_MAC_ACL        |             |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 13

| Task                | Command | name | Example   |         |           |         |
| ------------------- | ------- | ---- | --------- | ------- | --------- | ------- |
|                     |         |      | 10 permit | any any | appletalk | vlan 40 |
|                     |         |      | 20 deny   | any any | any count |         |
| ApplyinganIPv6ACLto |         |      | interface | 1/1/1   |           |         |
apply access-list
|                      |                    |     | apply     | access-list | ipv6 MY_IPV6_ACL | in  |
| -------------------- | ------------------ | --- | --------- | ----------- | ---------------- | --- |
| aninterface          | (tointerfaceorLAG) |     |           |             |                  |     |
| ApplyinganIPv4ACLtoa | apply access-list  |     | interface | lag 100     |                  |     |
| LAG                  |                    |     | apply     | access-list | ip MY_IP_ACL     | in  |
(tointerfaceorLAG)
| ApplyinganIPv4ACLtoa | apply access-list |     | vlan 10 |             |              |     |
| -------------------- | ----------------- | --- | ------- | ----------- | ------------ | --- |
| VLAN                 |                   |     | apply   | access-list | ip MY_IP_ACL | in  |
(toVLAN)
| ApplyingaMACACLtoa | apply access-list |     | vlan 40 |             |                |     |
| ------------------ | ----------------- | --- | ------- | ----------- | -------------- | --- |
| VLAN               |                   |     | apply   | access-list | mac MY_MAC_ACL | in  |
(toVLAN)
ApplyinganIPv4ACLto apply access-list apply access-list ip MY_IP_ACL control-plane
| theControlPlane | control-plane |     | vrf mgmt |     |     |     |
| --------------- | ------------- | --- | -------- | --- | --- | --- |
(OOBM)
| Removingapplicationof | apply access-list |     | interface | 1/1/1 |     |     |
| --------------------- | ----------------- | --- | --------- | ----- | --- | --- |
anACLfromaninterface (tointerfaceorLAG) no apply access-list ipv6 MY_IPV6_ACL in
vlan 40
| Removingapplicationof | apply access-list |     |     |     |     |     |
| --------------------- | ----------------- | --- | --- | --- | --- | --- |
anACLfromaVLAN (toVLAN) no apply access-list mac MY_MAC_ACL in
Removingapplicationof apply access-list no apply access-list ip MY_IP_ACL control-
| anACLfromtheControl | control-plane |     | plane vrf | mgmt |     |     |
| ------------------- | ------------- | --- | --------- | ---- | --- | --- |
Plane(OOBM)
| ShowingallACLs     | show access-list |     | show access-list |     |      |     |
| ------------------ | ---------------- | --- | ---------------- | --- | ---- | --- |
| ShowingallIPv6ACLs | show access-list |     | show access-list |     | ipv6 |     |
ShowingallACLsapplied show access-list show access-list interface 1/1/1
tointerface1/1/1
ShowingallACLsapplied show access-list show access-list vlan 10
toVLAN10
ShowingallACLsapplied show access-list show access-list control-plane
| totheControlPlane | control-plane |     |     |     |     |     |
| ----------------- | ------------- | --- | --- | --- | --- | --- |
ShowingaparticularACL show access-list show access-list ip MY_ACL
ShowinganACLas show access-list show access-list ip MY_ACL commands
commands
ShowingACLhitcounts show access-list show access-list hitcounts ip MY_ACL
foranACLappliedtoan
|     | hitcounts |     | interface | 1/1/1 |     |     |
| --- | --------- | --- | --------- | ----- | --- | --- |
interface
ShowingACLhitcounts show access-list show access-list hitcounts ip MY_ACL vlan 10
| foranACLappliedtoa | hitcounts |     |     |     |     |     |
| ------------------ | --------- | --- | --- | --- | --- | --- |
VLAN
ShowingACLhitcounts show access-list show access-list hitcounts ip MY_ACL
AccessControlLists|14

| Task |     | Command | name |     | Example |     |
| ---- | --- | ------- | ---- | --- | ------- | --- |
foranACLappliedtothe hitcounts control- control-plane vrf mgmt
| ControlPlane |     | plane |     |     |     |     |
| ------------ | --- | ----- | --- | --- | --- | --- |
ClearingACLhitcounts clear access-list clear access-list hitcounts ip MY_ACL vlan
|     |     | hitcounts |     |     | 10  |     |
| --- | --- | --------- | --- | --- | --- | --- |
ClearingACLhitcounts clear access-list clear access-list hitcounts control-plane
forControlPlane
|     |     | hitcounts | control- |     | vrf mgmt |     |
| --- | --- | --------- | -------- | --- | -------- | --- |
plane
CopyinganACL access-list copy access-list ipv6 MY_IPV6_ACL copy MY_IPV6_
ACL2
ResequencingtheACEs access-list access-list ip MY_IP_ACL resequence 1 1
| ofanACL |     | resequence |     |     |     |     |
| ------- | --- | ---------- | --- | --- | --- | --- |
ResettinganACL access-list reset access-list ip MY_IP_ACL reset
SettingtheACLlogtimer access-list log- access-list log-timer 30
| frequency |               | timer |       |     |     |     |
| --------- | ------------- | ----- | ----- | --- | --- | --- |
| Object    | group-related |       | tasks |     |     |     |
ObjectgroupsareusefulfordefininggroupsofaddressesandportsforuseexclusivelyinthetwoACL-
| definingcommandsaccess-list |     |     | ipandaccess-list |     | ipv6. |     |
| --------------------------- | --- | --- | ---------------- | --- | ----- | --- |
Commonobjectgroup-relatedtasksareasfollows:
|      |     | Command | name |         |     |     |
| ---- | --- | ------- | ---- | ------- | --- | --- |
| Task |     |         |      | Example |     |     |
CreatinganIPv4 object-group ip object-group ip address my_ipv4_addr_group
| addressobject |     | address |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- |
group
CreatinganIPv6 object-group object-group ipv6 address my_ipv6_addr_group
addressobject
ipv6 address
group
| Creatingaport |     | object-group |     | object-group | port | my_port_group |
| ------------- | --- | ------------ | --- | ------------ | ---- | ------------- |
| objectgroup   |     | port         |     |              |      |               |
ShowinganIPv4 show object- show object-group ip address my_ipv4_addr_group
| addressobject |     | group |     |     |     |     |
| ------------- | --- | ----- | --- | --- | --- | --- |
group
| ShowingallIPv6 |     | show object- |     | show | object-group | ipv6 address |
| -------------- | --- | ------------ | --- | ---- | ------------ | ------------ |
| addressobject  |     | group        |     |      |              |              |
groups
Showingaport show object- show object-group port my_port_group
| objectgroup    |     | group        |     |      |              |               |
| -------------- | --- | ------------ | --- | ---- | ------------ | ------------- |
| Showingallport |     | show object- |     | show | object-group | port commands |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 15

Task

Command name

Example

object groups as
commands

group

Resequencing an
IPv4 address object
group

object-group ip
address

object-group ip address my_ipv4_addr_group
resequence 100 10

Resequencing a
port object group

object-group
port

Resetting an IPv6
address object
group

object-group
ipv6 address

Resetting a port
object group

object-group
port

object-group port my_port_group resequence 200 5

object-group ipv6 address my_ipv6_addr_group reset

object-group port my_port_group reset

Active ACL configuration versus user-specified
configuration

The show access-list command shows the active configuration of the switch. The active configuration is
the ACLs that have been configured and accepted by the system. The active configurations are the
interfaces on which the ACLs have successfully been programmed in the hardware.

The output of the show access-list command with the configuration parameter shows the ACLs that
have been configured. The output of this command may not be the same as what was programmed in
the hardware or what is active on the switch. The situation might occur because of one or more of the
following:

n Unsupported command parameters might have been configured.

n Unsupported applications might have been specified.

n Applying an ACL might have been unsuccessful due to lack of hardware resources.

To determine if a discrepancy exists between what was configured and what is active, run the show
access-list command with the configuration parameter.

If the active ACLs and configured ACLs are not the same, the switch shows a warning message in the
output of the show command:

! access-list ip MY_IP_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.

If the configured ACL is processing, the switch shows an in-progress warning.

! access-list ip MY_IP_ACL user configuration currently being processed
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.

If the switch shows a warning message or in-progress message, additional changes can be made until
the error message is no longer shown in the show command, or you can run the access-list {all|ip

Access Control Lists | 16

<ACL-NAME>|ipv6 <ACL-NAME>|mac <ACL-NAME>} reset command. The access-list reset command
changes the user-specified configuration to match the active configuration. For details, see access-list
reset.

The show running-config command also shows a warning about ACLs that are in progress or failed.

Examples

Applying an ACL with TCP acknowledgments (ACKs) on ingress, which is unsupported by the hardware:

switch(config-acl)# 10 permit tcp 172.16.2.0/16 any ack

Showing the user-specified configuration:

switch(config)# do show access-list ip TEST_ACL

10 permit tcp 172.16.2.0/16 any ack

interface 1/1/1
! access-list ip TEST_ACL user configuration does not match active

configuration.

! run 'show access-list [commands]' to display active access-list

configuration.

apply access-list ip TEST_ACL in

switch(config)# do show access-list commands
access-list ip TEST_ACL

10 permit tcp 172.16.2.0/16 any ack

! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list all reset' to reset all access-lists to match active
configuration.

switch(config)# do show access-list commands configuration
access-list ip TEST_ACL

10 permit tcp 172.16.2.0/16 any ack

! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list all reset' to reset all access-lists to match active
configuration.
interface 1/1/1

apply access-list ip TEST_ACL in

switch(config)# do show access-list
Type

Name

Sequence Comment

Action
Source IP Address
Destination IP Address
Additional Parameters

L3 Protocol
Source L4 Port(s)
Destination L4 Port(s)

-------------------------------------------------------------------------------
IPv4

TEST_ACL

10 permit

172.16.2.0/16
any
ack

tcp

Resetting the user-specified configuration to match the active configuration:

switch(config)# access-list all reset

Showing the updated user-specified configuration:

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

17

| switch(config)# |           | do show access-list | commands configuration |     |     |
| --------------- | --------- | ------------------- | ---------------------- | --- | --- |
| access-list     |           | ip TEST_ACL         |                        |     |     |
|                 | 10 permit | tcp 172.16.2.0/16   | any ack                |     |     |
ACL commands
ACL application
ACLscanbeappliedasfollows:
| ACL type                      |     | IPv4+6 | IPv4 | IPv6 | MAC |
| ----------------------------- | --- | ------ | ---- | ---- | --- |
| Direction                     |     | In     | Out  | Out  | In  |
| L2interface(port)             |     | Yes    |      |      | Yes |
| L2LAG                         |     | Yes    |      |      | Yes |
| L3interface(port)             |     | Yes    | Yes  |      | Yes |
| L3LAG                         |     | Yes    | Yes  |      | Yes |
| L3interface(port)subinterface |     | Yes    |      |      | Yes |
(notapplicabletotheHPE
ArubaNetworking8320,
9300/9300SSwitchSeries)
| L3LAGsubinterface(not |     | Yes |     |     | Yes |
| --------------------- | --- | --- | --- | --- | --- |
applicabletotheHPEAruba
Networking8320,9300/9300S
SwitchSeries)
| VLAN                 |     | Yes         | Yes         | Yes         | Yes |
| -------------------- | --- | ----------- | ----------- | ----------- | --- |
| InterfaceVLAN        |     | Yes(routed) | Yes(routed) | Yes(routed) |     |
| Managementinterface  |     | Yes         |             |             |     |
| ControlPlane(perVRF) |     | Yes         |             |             |     |
AccessControlLists|18

HPEArubaNetworking8325,9300/9300S,10000SwitchSeries:
ACLscannotmatchmulticastpacketsontheroutedindirection.
Thefollowingmatchcriteriaarenotsupported.Ifanyofthesematchcriteriaareattemptedtobeconfigured,an
errormessagewillbedisplayedandtheactionwillnotbecompleted.
|     | TCP flags | CWR and            | ECE         |          |              |
| --- | --------- | ------------------ | ----------- | -------- | ------------ |
|     | TCP flags | and TTL            | (hop limit) |          | on IPv6 ACLs |
|     | TCP flags | and fragment       | on          | outbound | ACLs         |
|     | Fragment  | on IPv6            | VLAN ACLs   |          |              |
|     | VLAN ID   | on VLAN            | ACLs        |          |              |
|     | IPv4 AH   | on outbound        | ACLs        |          |              |
|     | IPv6 AH   | on outbound        | ACLs        |          |              |
|     | ESP on    | outbound           | ACLs        |          |              |
|     | IPv4 AH   | on routed-outbound |             | ACLs     |              |
|     | IPv6 AH   | on routed-outbound |             | ACLs     |              |
|     | ESP on    | routed-outbound    | ACLs        |          |              |
ToapplyIPv4and/orIPv6ACLstothemanagementinterface,applythemtotheControlPlaneonthe
managementVRF.
8320SwitchSeries:ACLscannotmatchmulticastpacketsontheroutedindirection.
Thefollowingmatchcriteriaarenotsupported.Ifanyofthesematchcriteriaareattemptedtobeconfigured,an
errormessagewillbedisplayedandtheactionwillnotbecompleted.
|     | IPv4 AH | on inbound         | ACLs |      |     |
| --- | ------- | ------------------ | ---- | ---- | --- |
|     | IPv4 AH | routed-inbound     | ACLs |      |     |
|     | IPv4 AH | on outbound        | ACLs |      |     |
|     | IPv6 AH | on outbound        | ACLs |      |     |
|     | IPv4 AH | on routed-outbound |      | ACLs |     |
|     | IPv6 AH | on routed-outbound |      | ACLs |     |
ToapplyIPv4and/orIPv6ACLstothemanagementinterface,applythemtotheControlPlaneonthe
managementVRF.
| access-list |               | copy |            |     |                        |
| ----------- | ------------- | ---- | ---------- | --- | ---------------------- |
| access-list | {ip|ipv6|mac} |      | <ACL-NAME> |     | copy <DESTINATION-ACL> |
Description
CopiesanIPv4,IPv6,orMACACLtoanewdestinationACLoroverwritesanexistingACL.
| Parameter         |     |     |     |     | Description                          |
| ----------------- | --- | --- | --- | --- | ------------------------------------ |
| {ip|ipv6|mac}     |     |     |     |     | SpecifiesthetypeofACL.               |
| <ACL-NAME>        |     |     |     |     | SpecifiesthenameoftheACLtobecopied.  |
| <DESTINATION-ACL> |     |     |     |     | SpecifiesthenameofthedestinationACL. |
Examples
CopyingMY_IP_ACLtoMY_IP_ACL2:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 19

| switch(config)# | access-list | ip MY_IP_ACL | copy MY_IP_ACL2 |     |
| --------------- | ----------- | ------------ | --------------- | --- |
switch(config-acl-ip)#
exit
| switch(config)# | do          | show access-list |             |            |
| --------------- | ----------- | ---------------- | ----------- | ---------- |
| Type            | Name        |                  |             |            |
| Sequence        | Comment     |                  |             |            |
|                 | Action      |                  | L3 Protocol |            |
|                 | Source      | IP Address       | Source      | L4 Port(s) |
|                 | Destination | IP Address       | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |
| ---- | --------- | --- | --- | --- |
|      | 1 permit  |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 2 permit               |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
|     | 3 permit |     | tcp |     |
| --- | -------- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 4 deny |     | any |     |
| --- | ------ | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL2 |     |     |     |
| ---- | ---------- | --- | --- | --- |
|      | 1 permit   |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 2 permit               |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
|     | 3 permit |     | tcp |     |
| --- | -------- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 4 deny |     | any |     |
| --- | ------ | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
CopyingMY_IPV6_ACLtoMY_IPV6_ACL2:
| switch(config)#        | access-list | ipv6 MY_IPV6_ACL | copy | MY_IPV6_ACL2 |
| ---------------------- | ----------- | ---------------- | ---- | ------------ |
| switch(config-acl-ip)# |             | exit             |      |              |
switch(config)#
|          | do          | show access-list |             |            |
| -------- | ----------- | ---------------- | ----------- | ---------- |
| Type     | Name        |                  |             |            |
| Sequence | Comment     |                  |             |            |
|          | Action      |                  | L3 Protocol |            |
|          | Source      | IP Address       | Source      | L4 Port(s) |
|          | Destination | IP Address       | Destination | L4 Port(s) |
|          | Additional  | Parameters       |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |
| ---- | ----------- | --- | --- | --- |
AccessControlLists|20

|     | 1 permit |     |     |     | udp |
| --- | -------- | --- | --- | --- | --- |
any
2001::1/64
|     | 2 Permit       | all | TCP ephemeral | ports |        |
| --- | -------------- | --- | ------------- | ----- | ------ |
|     | permit         |     |               |       | tcp    |
|     | 2001:2001::2:1 |     |               |       | > 1023 |
any
|     | 3 permit |     |     |     | tcp |
| --- | -------- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 4 deny |     |     |     | any |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |
| --- | ----------- | --- | ------- | --- | --- |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL2 |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- |
|      | 1 permit     |     |     |     | udp |
any
2001::1/64
|     | 2 Permit       | all | TCP ephemeral | ports |        |
| --- | -------------- | --- | ------------- | ----- | ------ |
|     | permit         |     |               |       | tcp    |
|     | 2001:2001::2:1 |     |               |       | > 1023 |
any
|     | 3 permit |     |     |     | tcp |
| --- | -------- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 4 deny |     |     |     | any |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |
| --- | ----------- | --- | ------- | --- | --- |
CopyingMY_MAC_ACLtoMY_MAC_ACL2:
| switch(config)#         |             | access-list | mac MY_MAC_ACL |     | copy MY_MAC_ACL2 |
| ----------------------- | ----------- | ----------- | -------------- | --- | ---------------- |
| switch(config-acl-mac)# |             |             | exit           |     |                  |
| switch(config)#         |             | do show     | access-list    |     |                  |
| Type                    | Name        |             |                |     |                  |
| Sequence                | Comment     |             |                |     |                  |
|                         | Action      |             |                |     | EtherType        |
|                         | Source      | MAC         | Address        |     |                  |
|                         | Destination |             | MAC Address    |     |                  |
|                         | Additional  |             | Parameters     |     |                  |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |      |
| --- | ---------- | --- | --- | --- | ---- |
|     | 1 permit   |     |     |     | ipv6 |
1122.3344.5566/ffff.ffff.0000
any
|     | 2 permit |     |     |     | any |
| --- | -------- | --- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS      | Priority | Code Point:   | 4         |           |
| --- | -------- | -------- | ------------- | --------- | --------- |
|     | 3 Permit | all      | vlan-1 tagged | Appletalk | traffic   |
|     | permit   |          |               |           | appletalk |
any
any
|     | VLAN:  | 1   |     |     |     |
| --- | ------ | --- | --- | --- | --- |
|     | 4 deny |     |     |     | any |
any
any
|     | Hit-counts: |     | enabled |     |     |
| --- | ----------- | --- | ------- | --- | --- |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 21

-------------------------------------------------------------------------------
MAC MY_MAC_ACL2
| 1 permit |     |     | ipv6 |
| -------- | --- | --- | ---- |
1122.3344.5566/ffff.ffff.0000
any
| 2 permit |     |     | any |
| -------- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
| QoS Priority | Code Point:   | 4         |           |
| ------------ | ------------- | --------- | --------- |
| 3 Permit all | vlan-1 tagged | Appletalk | traffic   |
| permit       |               |           | appletalk |
any
any
| VLAN: 1 |     |     |     |
| ------- | --- | --- | --- |
| 4 deny  |     |     | any |
any
any
| Hit-counts: | enabled |     |     |
| ----------- | ------- | --- | --- |
Type Name
Sequence Comment
| Action      |             |     | EtherType |
| ----------- | ----------- | --- | --------- |
| Source MAC  | Address     |     |           |
| Destination | MAC Address |     |           |
| Additional  | Parameters  |     |           |
-------------------------------------------------------------------------------
MAC MY_MAC_ACL
| 1 permit |     |     | ipv6 |
| -------- | --- | --- | ---- |
1122.3344.5566/ffff.ffff.0000
any
| 2 permit |     |     | any |
| -------- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
| QoS Priority | Code Point:   | 4         |           |
| ------------ | ------------- | --------- | --------- |
| 3 Permit all | vlan-1 tagged | Appletalk | traffic   |
| permit       |               |           | appletalk |
any
any
| VLAN: 1 |     |     |     |
| ------- | --- | --- | --- |
| 4 deny  |     |     | any |
any
any
| Hit-counts: | enabled |     |     |
| ----------- | ------- | --- | --- |
-------------------------------------------------------------------------------
MAC MY_MAC_ACL2
| 1 permit |     |     | ipv6 |
| -------- | --- | --- | ---- |
1122.3344.5566/ffff.ffff.0000
any
| 2 permit |     |     | any |
| -------- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
| QoS Priority | Code Point:   | 4         |           |
| ------------ | ------------- | --------- | --------- |
| 3 Permit all | vlan-1 tagged | Appletalk | traffic   |
| permit       |               |           | appletalk |
any
any
| VLAN: 1 |     |     |     |
| ------- | --- | --- | --- |
| 4 deny  |     |     | any |
any
any
| Hit-counts: | enabled |     |     |
| ----------- | ------- | --- | --- |
Command History
AccessControlLists|22

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| access-list | ip  |     |     |
| ----------- | --- | --- | --- |
SyntaxtocreateanIPv4ACLandenteritscontext.PlussyntaxtoremoveanACL:
| access-list    | ip <ACL-NAME> |     |     |
| -------------- | ------------- | --- | --- |
| no access-list | ip <ACL-NAME> |     |     |
Syntax(withintheACLcontext)forcreatingorremovingACEsforprotocolsah,gre,esp,igmp,ospf,
pim(ipisavailableasanaliasforany):
[<SEQUENCE-NUMBER>]
{permit|deny}
{any|ip|ah|gre|esp|igmp|ospf|pim|<IP-PROTOCOL-NUM>}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [ip-option <ANY>]
| [count] [log] |     |     |     |
| ------------- | --- | --- | --- |
no <SEQUENCE-NUMBER>
Syntax(withintheACLcontext)forcreatingorremovingACEsforprotocolssctp,tcp,udp:
[<SEQUENCE-NUMBER>]
{permit|deny}
{sctp|tcp|udp}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
| [urg] [ack] | [psh] [rst] | [syn] [fin] | [established] |
| ----------- | ----------- | ----------- | ------------- |
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [ip-option <ANY>]
| [count] [log] |     |     |     |
| ------------- | --- | --- | --- |
no <SEQUENCE-NUMBER>
Syntax(withintheACLcontext)forcreatingorremovingACEsforprotocolicmp:
[<SEQUENCE-NUMBER>]
{permit|deny}
{icmp}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]|<ADDRESS-GROUP>}
[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}] [icmp-code <ICMP-CODE-VALUE>]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [ip-option <ANY>]
| [count] [log] |     |     |     |
| ------------- | --- | --- | --- |
no <SEQUENCE-NUMBER>
Syntax(withintheACLcontext)forACEcomments:
| [<SEQUENCE-NUMBER>]  |     | comment <TEXT-STRING> |     |
| -------------------- | --- | --------------------- | --- |
| no <SEQUENCE-NUMBER> |     | comment               |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 23

Description

Creates an IPv4 Access Control List (ACL) comprised of one or more Access Control Entries (ACEs)
ordered and prioritized by sequence number. The lowest sequence number is the highest prioritized
ACE.

The no form of this command deletes the entire ACL, or deletes an ACE identified by sequence number,
or deletes only the comment from the ACE identified by sequence number.

Parameter

<ACL-NAME>

<SEQUENCE-NUMBER>

{permit|deny}

<IP-PROTOCOL-NUM>

{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>
|<SUBNET-MASK>}]|<ADDRESS-GROUP>}

{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>
|<SUBNET-MASK>}]|<ADDRESS-GROUP>}

[{eq|gt|lt} <PORT>|range <MIN-PORT>
<MAX-PORT>|group <PORT-GROUP>]

Description

Specifies the name of this ACL.

Specifies a sequence number for the ACE. Range: 1 to
4294967295.

Specifies whether to permit or deny traffic matching
this ACE.

Specifies the protocol as its Internet Protocol
number. For example, 2 corresponds to the IGMP
protocol. Range: 0 to 255.

Specifies the source IPv4 address.

n any - specifies any source IPv4 address.
n <SRC-IP-ADDRESS> - specifies the source IPv4 host

address.

o <PREFIX-LENGTH> - specifies the address bits to
mask (CIDR subnet mask notation). Range: 1 to

32.

o <SUBNET-MASK> - specifies the address bits to

mask (dotted decimal notation).

n <ADDRESS-GROUP> - specifies an IPv4 address

group defined with object-group ip address.

Specifies the destination IPv4 address.

n any - specifies any destination IPv4 address.
n <DST-IP-ADDRESS> - specifies the destination IPv4

host address.

o <PREFIX-LENGTH> - specifies the address bits to
mask (CIDR subnet mask notation). Range: 1 to

32.

o <SUBNET-MASK> - specifies the address bits to

mask (dotted decimal notation).

n <ADDRESS-GROUP> - specifies an IPv4 address
group that you defined earlier with object-
group ip address.

Specifies the port, port range, or port group. Port
numbers are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.
n gt <PORT> - specifies any Layer 4 port greater

than the indicated port.

Access Control Lists | 24

Parameter

Description

n lt <PORT> - specifies any Layer 4 port less than

the indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies the

Layer 4 port range.

n group <PORT-GROUP> - specifies the Layer 4 port
group that you defined earlier with object-
group port.

NOTE: Upon application of the ACL, ACEs with L4
port ranges may consume more than one hardware
entry.

Specifies matching on the TCP Flag: Urgent. (Applies
only to the "in" (ingress) direction.)

Specifies matching on the TCP Flag:
Acknowledgment. (Applies only to the "in" (ingress)
direction.)

Specifies matching on the TCP Flag: Push buffered
data to receiving application. (Applies only to the
"in" (ingress) direction.)

Specifies matching on the TCP Flag: Reset the
connection. (Applies only to the "in" (ingress)
direction.)

Specifies matching on the TCP Flag: Synchronize
sequence numbers. (Applies only to the "in"
(ingress) direction.)

Specifies matching on the TCP Flag: Finish
connection. (Applies only to the "in" (ingress)
direction.)

Specifies matching on the TCP Flag: Established
connection. (Applies only to the "in" (ingress)
direction.)

Specifies the ICMP type.

n echo - specifies an ICMP echo request packet.
n echo-reply - specifies an ICMP echo reply packet.
n <ICMP-TYPE-VALUE> - specifies an ICMP type

value. Range: 0 to 255.

urg

ack

psh

rst

syn

fin

established

[icmp-type {echo|echo-reply|
<ICMP-TYPE-VALUE>}]

[icmp-code <ICMP-CODE-VALUE>]

Specifies the ICMP code value. Range: 0 to 255.

dscp DSCP-SPECIFIER>

Specifies the Differentiated Services Code Point
(DSCP), either a numeric <DSCP-VALUE> (0 to 63) or
one of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low

drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1,

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

25

Parameter

Description

medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high

drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low

drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2,

medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high

drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low

drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3,

medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high

drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low

drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4,

medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high

drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)
n CS1 - DSCP 8 (Class Selector 1: Scavenger)
n CS2 - DSCP 16 (Class Selector 2: OAM)
n CS3 - DSCP 24 (Class Selector 3: Signaling)
n CS4 - DSCP 32 (Class Selector 4: Real time)
n CS5 - DSCP 40 (Class Selector 5: Broadcast video)
n CS6 - DSCP 48 (Class Selector 6: Network control)
n CS7 - DSCP 56 (Class Selector 7)
n EF - DSCP 46 (Expedited Forwarding)

Specifies an Explicit Congestion Notification value.
Range: 0 to 3.

ecn <ECN-VALUE>

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies an IP precedence value. Range: 0 to 7.

tos <TOS-VALUE>

fragment

vlan <VLAN-ID>

Specifies the Type of Service value. Range: 0 to 31.

Specifies a fragment packet.

Specifies VLAN tag to match on. 802.1Q VLAN ID.

NOTE:
This parameter cannot be used in any ACL that
will be applied to a VLAN.

ttl <TTL-VALUE>

Specifies a time-to-live (hop limit) value. Range: 0 to
255.

ip-option <ANY>

(For 8325 and 1000 Switch series) Specifies the IP

Access Control Lists | 26

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
option.
| count |     |     |     | Keepsthehitcountsofthenumberofpackets |     |
| ----- | --- | --- | --- | ------------------------------------- | --- |
matchingthisACE.
| log |     |     |     | Keepsalogofthenumberofpacketsmatchingthis |     |
| --- | --- | --- | --- | ----------------------------------------- | --- |
ACE.Workswithdenyactionsbutnotwithpermit
actions.WorkswithACLsappliedoningress,or
ControlPlane,butnotwithACLsappliedonegress.
[<SEQUENCE-NUMBER>] comment <TEXT-STRING> AddsacommenttoanACE.Thenoformremoves
onlythecommentfromtheACE.
Usage
n Ifthe<IP-PROTOCOL-NUM>parameterisusedinsteadofaprotocolname,ensurethatanyneeded
ACE-definitionparametersspecifictotheselectedprotocolarealsoprovided.
n WhenusingmultipleACLtypes(IPv4,IPv6,orMAC)withloggingonthesameinterface,thefirst
packetthatmatchesanACEwithlogoptionislogged.Untilthelog-timerwait-periodisover,any
packetsmatchingotherACLtypesdonotcreatealog.Attheendofthewait-period,theswitch
createsasummarylogforalltheACLsthatwerematched,regardlessoftype.
n Formoreinformationaboutmitigatingpotentialattacksbydenyingorloggingpacketsusingtheip-
optionparameter,refertothevideoontheHPEArubaNetworkingAirheadsBroadcastingChannel.
Examples
CreatinganIPv4ACLwithfourentries:
switch(config)#
|                        | access-list | ip        | MY_IP_ACL         |               |             |
| ---------------------- | ----------- | --------- | ----------------- | ------------- | ----------- |
| switch(config-acl-ip)# |             | 10 permit | udp any           | 172.16.1.0/24 |             |
| switch(config-acl-ip)# |             | 20 permit | tcp 172.16.2.0/16 |               | gt 1023 any |
switch(config-acl-ip)# 30 permit tcp 172.26.1.0/24 any syn ack dscp 10
| switch(config-acl-ip)# |             | 40 deny     | any any any | count       |            |
| ---------------------- | ----------- | ----------- | ----------- | ----------- | ---------- |
| switch(config-acl-ip)# |             | exit        |             |             |            |
| switch(config)#        | show        | access-list |             |             |            |
| Type                   | Name        |             |             |             |            |
| Sequence               | Comment     |             |             |             |            |
|                        | Action      |             |             | L3 Protocol |            |
|                        | Source      | IP Address  |             | Source      | L4 Port(s) |
|                        | Destination | IP Address  |             | Destination | L4 Port(s) |
|                        | Additional  | Parameters  |             |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- |
|      | 10 permit |     |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     |     | tcp    |     |
| --- | ---------------------- | --- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     |     | > 1023 |     |
any
|     | 30 permit |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 27

|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |
| --- | ----------- | --- | ------- | --- | --- |
AddingacommenttoanexistingIPv4ACE:
| switch(config)# |     | access-list | ip MY_IP_ACL |     |     |
| --------------- | --- | ----------- | ------------ | --- | --- |
switch(config-acl-ip)# 20 comment Permit all TCP ephemeral ports
| switch(config-acl-ip)# |             |      | exit        |             |            |
| ---------------------- | ----------- | ---- | ----------- | ----------- | ---------- |
| switch(config)#        |             | show | access-list |             |            |
| Type                   | Name        |      |             |             |            |
| Sequence               | Comment     |      |             |             |            |
|                        | Action      |      |             | L3 Protocol |            |
|                        | Source      | IP   | Address     | Source      | L4 Port(s) |
|                        | Destination |      | IP Address  | Destination | L4 Port(s) |
|                        | Additional  |      | Parameters  |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- |
|      | 10 permit |     |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 Permit              | all | TCP ephemeral | ports  |     |
| --- | ---------------------- | --- | ------------- | ------ | --- |
|     | permit                 |     |               | tcp    |     |
|     | 172.16.2.0/255.255.0.0 |     |               | > 1023 |     |
any
|     | 30 permit |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
|     | dscp: | AF11 |     |     |     |
| --- | ----- | ---- | --- | --- | --- |
ack
syn
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |
| --- | ----------- | --- | ------- | --- | --- |
RemovingacommentfromanexistingIPv4ACE:
| switch(config)#        |             | access-list | ip MY_IP_ACL  |             |            |
| ---------------------- | ----------- | ----------- | ------------- | ----------- | ---------- |
| switch(config-acl-ip)# |             |             | no 20 comment |             |            |
| switch(config-acl-ip)# |             |             | exit          |             |            |
| switch(config)#        |             | show        | access-list   |             |            |
| Type                   | Name        |             |               |             |            |
| Sequence               | Comment     |             |               |             |            |
|                        | Action      |             |               | L3 Protocol |            |
|                        | Source      | IP          | Address       | Source      | L4 Port(s) |
|                        | Destination |             | IP Address    | Destination | L4 Port(s) |
|                        | Additional  |             | Parameters    |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- |
|      | 10 permit |     |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     |     | tcp    |     |
| --- | ---------------------- | --- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     |     | > 1023 |     |
any
AccessControlLists|28

|     | 30 permit |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
AddinganACE(insertline25)toanexistingIPv4ACL:
| switch(config)#        | access-list | ip          | MY_IP_ACL          |             |            |
| ---------------------- | ----------- | ----------- | ------------------ | ----------- | ---------- |
| switch(config-acl-ip)# |             | 25 permit   | icmp 172.16.2.0/16 |             | any        |
| switch(config-acl-ip)# |             | exit        |                    |             |            |
| switch(config)#        | show        | access-list |                    |             |            |
| Type                   | Name        |             |                    |             |            |
| Sequence               | Comment     |             |                    |             |            |
|                        | Action      |             |                    | L3 Protocol |            |
|                        | Source      | IP Address  |                    | Source      | L4 Port(s) |
|                        | Destination | IP Address  |                    | Destination | L4 Port(s) |
|                        | Additional  | Parameters  |                    |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- |
|      | 10 permit |     |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     |     | tcp    |     |
| --- | ---------------------- | --- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     |     | > 1023 |     |
any
|     | 25 permit              |     |     | icmp |     |
| --- | ---------------------- | --- | --- | ---- | --- |
|     | 172.16.2.0/255.255.0.0 |     | any |      |     |
|     | 30 permit              |     |     | tcp  |     |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
ReplacinganACEinanexistingIPv4ACL:
| switch(config)#        | access-list | ip          | MY_IP_ACL          |             |            |
| ---------------------- | ----------- | ----------- | ------------------ | ----------- | ---------- |
| switch(config-acl-ip)# |             | 25 permit   | icmp 172.17.1.0/16 |             | any        |
| switch(config-acl-ip)# |             | exit        |                    |             |            |
| switch(config)#        | show        | access-list |                    |             |            |
| Type                   | Name        |             |                    |             |            |
| Sequence               | Comment     |             |                    |             |            |
|                        | Action      |             |                    | L3 Protocol |            |
|                        | Source      | IP Address  |                    | Source      | L4 Port(s) |
|                        | Destination | IP Address  |                    | Destination | L4 Port(s) |
|                        | Additional  | Parameters  |                    |             |            |
-------------------------------------------------------------------------------
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 29

| IPv4 | MY_IP_ACL |     |     |     |
| ---- | --------- | --- | --- | --- |
|      | 10 permit |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
|     | 25 permit |     | icmp |     |
| --- | --------- | --- | ---- | --- |
172.17.1.0/255.255.0.0
|     | 30 permit |     | tcp |     |
| --- | --------- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 40 deny |     | any |     |
| --- | ------- | --- | --- | --- |
any
any
|          | Hit-counts: | enabled    |             |            |
| -------- | ----------- | ---------- | ----------- | ---------- |
| Type     | Name        |            |             |            |
| Sequence | Comment     |            |             |            |
|          | Action      |            | L3 Protocol |            |
|          | Source      | IP Address | Source      | L4 Port(s) |
|          | Destination | IP Address | Destination | L4 Port(s) |
|          | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |
| ---- | --------- | --- | --- | --- |
|      | 10 permit |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
|     | 25 permit |     | icmp |     |
| --- | --------- | --- | ---- | --- |
172.17.1.0/255.255.0.0
|     | 30 permit |     | tcp |     |
| --- | --------- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 40 deny |     | any |     |
| --- | ------- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
RemovinganACEfromanIPv4ACL:
| switch(config)#        | access-list | ip MY_IP_ACL |     |     |
| ---------------------- | ----------- | ------------ | --- | --- |
| switch(config-acl-ip)# |             | no 25        |     |     |
| switch(config-acl-ip)# |             | exit         |     |     |
switch(config)#
|          | show        | access-list |             |            |
| -------- | ----------- | ----------- | ----------- | ---------- |
| Type     | Name        |             |             |            |
| Sequence | Comment     |             |             |            |
|          | Action      |             | L3 Protocol |            |
|          | Source      | IP Address  | Source      | L4 Port(s) |
|          | Destination | IP Address  | Destination | L4 Port(s) |
|          | Additional  | Parameters  |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |
| ---- | --------- | --- | --- | --- |
AccessControlLists|30

|     | 10 permit |     | udp |     |
| --- | --------- | --- | --- | --- |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
|     | 30 permit |     | tcp |     |
| --- | --------- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 40 deny |     | any |     |
| --- | ------- | --- | --- | --- |
any
any
|          | Hit-counts: | enabled    |             |            |
| -------- | ----------- | ---------- | ----------- | ---------- |
| Type     | Name        |            |             |            |
| Sequence | Comment     |            |             |            |
|          | Action      |            | L3 Protocol |            |
|          | Source      | IP Address | Source      | L4 Port(s) |
|          | Destination | IP Address | Destination | L4 Port(s) |
|          | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |
| ---- | --------- | --- | --- | --- |
|      | 10 permit |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
|     | 30 permit |     | tcp |     |
| --- | --------- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 40 deny |     | any |     |
| --- | ------- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
CopyanIPv4ACL:
| switch(config)# | access-list | ip MY_IP_ACL | copy MY_IP_ACL2 |            |
| --------------- | ----------- | ------------ | --------------- | ---------- |
| switch(config)# | show        | access-list  |                 |            |
| Type            | Name        |              |                 |            |
| Sequence        | Comment     |              |                 |            |
|                 | Action      |              | L3 Protocol     |            |
|                 | Source      | IP Address   | Source          | L4 Port(s) |
|                 | Destination | IP Address   | Destination     | L4 Port(s) |
|                 | Additional  | Parameters   |                 |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |
| ---- | --------- | --- | --- | --- |
10
|     | permit |     | udp |     |
| --- | ------ | --- | --- | --- |
any
172.16.1.0/255.255.255.0
20
|     | permit                 |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 31

30
| permit |     | tcp |     |
| ------ | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
40
| deny |     | any |     |
| ---- | --- | --- | --- |
any
any
| Hit-counts: | enabled |     |     |
| ----------- | ------- | --- | --- |
-------------------------------------------------------------------------------
IPv4 MY_IP_ACL2
10
| permit |     | udp |     |
| ------ | --- | --- | --- |
any
172.16.1.0/255.255.255.0
20
| permit                 |     | tcp    |     |
| ---------------------- | --- | ------ | --- |
| 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
30
| permit |     | tcp |     |
| ------ | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
40
| deny |     | any |     |
| ---- | --- | --- | --- |
any
any
Hit-counts: enabled switch(config)# access-list ip MY_IP_ACL copy MY_
IP_ACL2
| switch(config)# show | access-list |     |     |
| -------------------- | ----------- | --- | --- |
Type Name
Sequence Comment
| Action      |            | L3 Protocol |            |
| ----------- | ---------- | ----------- | ---------- |
| Source      | IP Address | Source      | L4 Port(s) |
| Destination | IP Address | Destination | L4 Port(s) |
| Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
IPv4 MY_IP_ACL
10
| permit |     | udp |     |
| ------ | --- | --- | --- |
any
172.16.1.0/255.255.255.0
20
| permit                 |     | tcp    |     |
| ---------------------- | --- | ------ | --- |
| 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
30
| permit |     | tcp |     |
| ------ | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
40
| deny |     | any |     |
| ---- | --- | --- | --- |
AccessControlLists|32

any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL2 |     |     |     |     |
| ---- | ---------- | --- | --- | --- | --- |
10
|     | permit |     |     | udp |     |
| --- | ------ | --- | --- | --- | --- |
any
172.16.1.0/255.255.255.0
20
|     | permit                 |     |     | tcp    |     |
| --- | ---------------------- | --- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     |     | > 1023 |     |
any
30
|     | permit |     |     | tcp |     |
| --- | ------ | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
40
|     | deny |     |     | any |     |
| --- | ---- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
RemovinganIPv4ACL:
| switch(config)# | no          | access-list | ip MY_IP_ACL |             |            |
| --------------- | ----------- | ----------- | ------------ | ----------- | ---------- |
| switch(config)# | show        | access-list |              |             |            |
| Type            | Name        |             |              |             |            |
| Sequence        | Comment     |             |              |             |            |
|                 | Action      |             |              | L3 Protocol |            |
|                 | Source      | IP Address  |              | Source      | L4 Port(s) |
|                 | Destination | IP Address  |              | Destination | L4 Port(s) |
|                 | Additional  | Parameters  |              |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL2 |     |     |     |     |
| ---- | ---------- | --- | --- | --- | --- |
|      | 1 permit   |     |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 2 permit               |     |     | tcp    |     |
| --- | ---------------------- | --- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     |     | > 1023 |     |
any
|     | 3 permit |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
dscp: AF11
ack
syn
|     | 4 deny |     |     | any |     |
| --- | ------ | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
ConfiguringanACEwithasourceL4portgroupandadestinationL4portgrouptomatchonanyip-
option:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 33

switch(config-acl-ip)# permit sctp any group my_port_group any ip-option ?
| any Any | IP option |     |                                                    |
| ------- | --------- | --- | -------------------------------------------------- |
| Command | History   |     |                                                    |
| Release |           |     | Modification                                       |
| 10.15   |           |     | Theip-optionparameterisintroducedonthe8325and10000 |
switches.
| 10.12          |             |         | AllowACLsappliedtotheControlPlanetobelogged. |
| -------------- | ----------- | ------- | -------------------------------------------- |
| 10.07orearlier |             |         | --                                           |
| Command        | Information |         |                                              |
| Platforms      | Command     | context | Authority                                    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|     | Theaccess-listip<ACL- |     | rightsforthiscommand. |
| --- | --------------------- | --- | --------------------- |
NAME>commandtakes
youintothenamedACL
contextwhereyouenter
theACEs.
| access-list | ipv6 |     |     |
| ----------- | ---- | --- | --- |
SyntaxtocreateanIPv6ACLandenteritscontext.PlussyntaxtoremoveanACL:
| access-list    | ipv6 <ACL-NAME> |     |     |
| -------------- | --------------- | --- | --- |
| no access-list | ipv6 <ACL-NAME> |     |     |
Syntax(withintheACLcontext)forcreatingorremovingACEsforprotocolsah,gre,esp,ospf,pim(ipv6
isavailableasanaliasforany):
[<SEQUENCE-NUMBER>]
{permit|deny}
{any|ipv6|ah|gre|esp|ospf|pim|<IP-PROTOCOL-NUM>}
{any|<SRC-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]
no <SEQUENCE-NUMBER>
Syntax(withintheACLcontext)forcreatingorremovingACEsforprotocolssctp,tcp,udp:
[<SEQUENCE-NUMBER>]
{permit|deny}
{sctp|tcp|udp}
{any|<SRC-IP-ADDRESS>[/<PREFIX-LENGTH>}]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
{any|<DST-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>|group <PORT-GROUP>]
| [urg] [ack] | [psh] [rst] | [syn] [fin] | [established] |
| ----------- | ----------- | ----------- | ------------- |
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]
no <SEQUENCE-NUMBER>
Syntax(withintheACLcontext)forcreatingorremovingACEsforprotocolicmpv6:
[<SEQUENCE-NUMBER>]
{permit|deny}
AccessControlLists|34

{icmpv6}
{any|<SRC-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
{any|<DST-IP-ADDRESS>[/<PREFIX-LENGTH>]|<ADDRESS-GROUP>}
[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}] [icmp-code <ICMP-CODE-VALUE>]
[dscp <DSCP-SPECIFIER>][ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count] [log]

no <SEQUENCE-NUMBER>

Syntax (within the ACL context) for ACE comments:
[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

no <SEQUENCE-NUMBER> comment

Description

Creates an IPv6 Access Control List (ACL). The ACL is made of one or more Access Control Entries (ACEs)
ordered and prioritized by sequence number. The lowest sequence number is the highest prioritized
ACE.

The no form of this command deletes the entire ACL, or deletes an ACE identified by sequence number,
or deletes only the comment from the ACE identified by sequence number.

Parameter

<ACL-NAME>

<SEQUENCE-NUMBER>

{permit|deny}

<IP-PROTOCOL-NUM>

{any|<SRC-IP-ADDRESS>[/<PREFIX-
LENGTH>]|<ADDRESS-GROUP>}

{any|<DST-IP-ADDRESS>[/<PREFIX-
LENGTH>]|<ADDRESS-GROUP>}

Description

Specifies the name of this ACL.

Specifies a sequence number for the ACE. Range: 1 to
4294967295.

Specifies whether to permit or deny traffic matching
this ACE.

Specifies the protocol as its Internet Protocol
number. For example, 2 corresponds to the IGMP
protocol. Range: 0 to 255.

Specifies the source IPv6 address.

n any - specifies any source IPv6 address.
n <SRC-IP-ADDRESS> - specifies the source IPv6 host

address.

o <PREFIX-LENGTH> - specifies the address bits to
mask (CIDR subnet mask notation). Range: 1 to

128.

n <ADDRESS-GROUP> - specifies an IPv6 address

group that you defined earlier with object-group

ipv6 address.

Specifies the destination IPv6 address.

n any - specifies any destination IPv6 address.
n <DST-IP-ADDRESS> - specifies the destination IPv6

host address.

o <PREFIX-LENGTH> - specifies the address bits to
mask (CIDR subnet mask notation). Range: 1 to

128.

n <ADDRESS-GROUP> - specifies an IPv6 address
group that you defined earlier with object-

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

35

Parameter

Description

group ipv6 address.

[{eq|gt|lt} <PORT>|range <MIN-PORT><MAX-
PORT>|group <PORT-GROUP>]

Specifies the port, port range, or port group. Port
numbers are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.
n gt <PORT> - specifies any Layer 4 port greater than

the indicated port.

n lt <PORT> - specifies any Layer 4 port less than the

indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies the

Layer 4 port range.

n group <PORT-GROUP> - specifies the Layer 4 port
group that you defined earlier with object-
group port.

NOTE: Upon application of the ACL, ACEs with L4 port
ranges may consume more than one hardware entry.

urg, ack, psh, rst, syn, fin, established

These TCP flag-matching parameters are not
supported.

[icmp-type {echo|echo-reply|<ICMP-TYPE-
VALUE>}]

Specifies the ICMP type.

n echo - specifies an ICMP echo request packet.
n echo-reply - specifies an ICMP echo reply packet.
n <ICMP-TYPE-VALUE> - specifies an ICMP type

value. Range: 0 to 255.

[icmp-code <ICMP-CODE-VALUE>]

Specifies the ICMP code value. Range: 0 to 255.

dscp DSCP-SPECIFIER>

Specifies the Differentiated Services Code Point
(DSCP), either a numeric <DSCP-VALUE> (0 to 63) or
one of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low

drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1,

medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high

drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low

drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2,

medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high

drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low

drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3,

medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high

Access Control Lists | 36

Parameter

Description

drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low

drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4,

medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high

drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)
n CS1 - DSCP 8 (Class Selector 1: Scavenger)
n CS2 - DSCP 16 (Class Selector 2: OAM)
n CS3 - DSCP 24 (Class Selector 3: Signaling)
n CS4 - DSCP 32 (Class Selector 4: Real time)
n CS5 - DSCP 40 (Class Selector 5: Broadcast video)
n CS6 - DSCP 48 (Class Selector 6: Network control)
n CS7 - DSCP 56 (Class Selector 7)
n EF - DSCP 46 (Expedited Forwarding)

Specifies an Explicit Congestion Notification value.
Range: 0- 3.

ecn <ECN-VALUE>

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies an IP precedence value. Range: 0-7.

tos <TOS-VALUE>

fragment

vlan <VLAN-ID>

ttl <TTL-VALUE>

count

log

Specifies the Type of Service value. Range: 0-31.

Not supported.

Not supported.

Not supported.

Keeps the hit counts of the number of packets
matching this ACE.

Keeps a log of the number of packets matching this
ACE. Works with deny actions but not with permit
actions. Works with ACLs applied on ingress, or
Control Plane, but not with ACLs applied on egress.

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

Adds a comment to an ACE. The no form removes
only the comment from the ACE.

Usage

n If the <IP-PROTOCOL-NUM> parameter is used instead of a protocol name, ensure that any needed

ACE-definition parameters specific to the selected protocol are also provided.

n When using multiple ACL types (IPv4, IPv6, or MAC) with logging on the same interface, the first

packet that matches an ACE with log option is logged. Until the log-timer wait-period is over, any
packets matching other ACL types do not create a log. At the end of the wait-period, the switch
creates a summary log all the ACLs that were matched, regardless of type.

Examples

Creating an IPv6 ACL with four entries:

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

37

| switch(config)# |     | access-list | ipv6 | MY_IPV6_ACL |     |     |
| --------------- | --- | ----------- | ---- | ----------- | --- | --- |
switch(config-acl-ipv6)#
|     |     |     | 10 permit | udp any | 2001::1/64 |     |
| --- | --- | --- | --------- | ------- | ---------- | --- |
switch(config-acl-ipv6)# 20 permit tcp 2001:2001::2:1/128 gt 1023 any
| switch(config-acl-ipv6)# |             |         | 30 permit   | tcp 2001:2011::1/64 |             | any        |
| ------------------------ | ----------- | ------- | ----------- | ------------------- | ----------- | ---------- |
| switch(config-acl-ipv6)# |             |         | 40 deny     | any any             | any count   |            |
| switch(config-acl-ipv6)# |             |         | exit        |                     |             |            |
| switch(config)#          |             | do show | access-list |                     |             |            |
| Type                     | Name        |         |             |                     |             |            |
| Sequence                 | Comment     |         |             |                     |             |            |
|                          | Action      |         |             |                     | L3 Protocol |            |
|                          | Source      | IP      | Address     |                     | Source      | L4 Port(s) |
|                          | Destination |         | IP Address  |                     | Destination | L4 Port(s) |
|                          | Additional  |         | Parameters  |                     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- |
|      | 10 permit   |     |     |     | udp |     |
any
2001::1/64
|     | 20 permit      |     |     |     | tcp    |     |
| --- | -------------- | --- | --- | --- | ------ | --- |
|     | 2001:2001::2:1 |     |     |     | > 1023 |     |
any
|     | 30 permit |     |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 40 deny |     |     |     | any |     |
| --- | ------- | --- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- |
AddingacommenttoanexistingIPv6ACE:
switch(config)#
|     |     | access-list | ipv6 | MY_IPV6_ACL |     |     |
| --- | --- | ----------- | ---- | ----------- | --- | --- |
switch(config-acl-ipv6)# 20 comment Permit all TCP ephemeral ports
| switch(config-acl-ipv6)# |             |         | exit        |     |             |            |
| ------------------------ | ----------- | ------- | ----------- | --- | ----------- | ---------- |
| switch(config)#          |             | do show | access-list |     |             |            |
| Type                     | Name        |         |             |     |             |            |
| Sequence                 | Comment     |         |             |     |             |            |
|                          | Action      |         |             |     | L3 Protocol |            |
|                          | Source      | IP      | Address     |     | Source      | L4 Port(s) |
|                          | Destination |         | IP Address  |     | Destination | L4 Port(s) |
|                          | Additional  |         | Parameters  |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- |
|      | 10 permit   |     |     |     | udp |     |
any
2001::1/64
|     | 20 Permit      | all | TCP ephemeral | ports |        |     |
| --- | -------------- | --- | ------------- | ----- | ------ | --- |
|     | permit         |     |               |       | tcp    |     |
|     | 2001:2001::2:1 |     |               |       | > 1023 |     |
any
|     | 30 permit |     |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 40 deny |     |     |     | any |     |
| --- | ------- | --- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- |
RemovingacommentfromanexistingIPv6ACE:
AccessControlLists|38

| switch(config)# | access-list | ipv6 | MY_IPV6_ACL |     |
| --------------- | ----------- | ---- | ----------- | --- |
switch(config-acl-ipv6)#
|                          |             | no 20 comment    |             |            |
| ------------------------ | ----------- | ---------------- | ----------- | ---------- |
| switch(config-acl-ipv6)# |             | exit             |             |            |
| switch(config)#          | do          | show access-list |             |            |
| Type                     | Name        |                  |             |            |
| Sequence                 | Comment     |                  |             |            |
|                          | Action      |                  | L3 Protocol |            |
|                          | Source      | IP Address       | Source      | L4 Port(s) |
|                          | Destination | IP Address       | Destination | L4 Port(s) |
|                          | Additional  | Parameters       |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |
| ---- | ----------- | --- | --- | --- |
10 permit udp
any
2001::1/64
20 permit tcp
|     | 2001:2001::2:1 |     | > 1023 |     |
| --- | -------------- | --- | ------ | --- |
any
30 permit tcp
2001:2011::1/64
any
40 deny any
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
AddinganACEtoanexistingIPv6ACL:
| switch(config)#          | access-list | ipv6             | MY_IPV6_ACL       |            |
| ------------------------ | ----------- | ---------------- | ----------------- | ---------- |
| switch(config-acl-ipv6)# |             | 25 permit        | icmpv6 2001::1/64 | any        |
| switch(config-acl-ipv6)# |             | exit             |                   |            |
| switch(config)#          | do          | show access-list |                   |            |
| Type                     | Name        |                  |                   |            |
| Sequence                 | Comment     |                  |                   |            |
|                          | Action      |                  | L3 Protocol       |            |
|                          | Source      | IP Address       | Source            | L4 Port(s) |
|                          | Destination | IP Address       | Destination       | L4 Port(s) |
|                          | Additional  | Parameters       |                   |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |
| ---- | ----------- | --- | --- | --- |
10 permit udp
any
2001::1/64
20 permit tcp
|     | 2001:2001::2:1 |     | > 1023 |     |
| --- | -------------- | --- | ------ | --- |
any
25 permit icmpv6
2001::1/64
any
30 permit tcp
2001:2011::1/64
any
40 deny any
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
ReplacinganACEinanexistingIPv6ACL:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 39

| switch(config)# | access-list | ipv6 | MY_IPV6_ACL |     |
| --------------- | ----------- | ---- | ----------- | --- |
switch(config-acl-ipv6)#
|                          |             | 25 permit        | icmpv6 2001::2:1/64 | any        |
| ------------------------ | ----------- | ---------------- | ------------------- | ---------- |
| switch(config-acl-ipv6)# |             | exit             |                     |            |
| switch(config)#          | do          | show access-list |                     |            |
| Type                     | Name        |                  |                     |            |
| Sequence                 | Comment     |                  |                     |            |
|                          | Action      |                  | L3 Protocol         |            |
|                          | Source      | IP Address       | Source              | L4 Port(s) |
|                          | Destination | IP Address       | Destination         | L4 Port(s) |
|                          | Additional  | Parameters       |                     |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |
| ---- | ----------- | --- | --- | --- |
10 permit udp
any
2001::1/64
20 permit tcp
|     | 2001:2001::2:1 |     | > 1023 |     |
| --- | -------------- | --- | ------ | --- |
any
25 permit icmpv6
2001::2:1/64
any
30 permit tcp
2001:2011::1/64
any
40 deny any
any
any
|          | Hit-counts: | enabled    |             |            |
| -------- | ----------- | ---------- | ----------- | ---------- |
| Type     | Name        |            |             |            |
| Sequence | Comment     |            |             |            |
|          | Action      |            | L3 Protocol |            |
|          | Source      | IP Address | Source      | L4 Port(s) |
|          | Destination | IP Address | Destination | L4 Port(s) |
|          | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |
| ---- | ----------- | --- | --- | --- |
10 permit udp
any
2001::1/64
20 permit tcp
|     | 2001:2001::2:1 |     | > 1023 |     |
| --- | -------------- | --- | ------ | --- |
any
25 permit icmpv6
2001::2:1/64
any
30 permit tcp
2001:2011::1/64
any
40 deny any
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
RemovinganACEfromanIPv6ACL:
| switch(config)#          | access-list | ipv6  | MY_IPV6_ACL |     |
| ------------------------ | ----------- | ----- | ----------- | --- |
| switch(config-acl-ipv6)# |             | no 25 |             |     |
| switch(config-acl-ipv6)# |             | exit  |             |     |
AccessControlLists|40

| switch(config)# | do          | show access-list |     |             |            |
| --------------- | ----------- | ---------------- | --- | ----------- | ---------- |
| Type            | Name        |                  |     |             |            |
| Sequence        | Comment     |                  |     |             |            |
|                 | Action      |                  |     | L3 Protocol |            |
|                 | Source      | IP Address       |     | Source      | L4 Port(s) |
|                 | Destination | IP Address       |     | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
|      | 10 permit   |     |     | udp |     |
any
2001::1/64
|     | 20 permit      |     |     | tcp    |     |
| --- | -------------- | --- | --- | ------ | --- |
|     | 2001:2001::2:1 |     |     | > 1023 |     |
any
|     | 30 permit |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|          | Hit-counts: | enabled    |     |             |            |
| -------- | ----------- | ---------- | --- | ----------- | ---------- |
| Type     | Name        |            |     |             |            |
| Sequence | Comment     |            |     |             |            |
|          | Action      |            |     | L3 Protocol |            |
|          | Source      | IP Address |     | Source      | L4 Port(s) |
|          | Destination | IP Address |     | Destination | L4 Port(s) |
|          | Additional  | Parameters |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
|      | 10 permit   |     |     | udp |     |
any
2001::1/64
|     | 20 permit      |     |     | tcp    |     |
| --- | -------------- | --- | --- | ------ | --- |
|     | 2001:2001::2:1 |     |     | > 1023 |     |
any
|     | 30 permit |     |     | tcp |     |
| --- | --------- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 40 deny |     |     | any |     |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
RemovinganIPv6ACL:
| switch(config)# | no          | access-list      | ipv6 MY_IPV6_ACL |             |            |
| --------------- | ----------- | ---------------- | ---------------- | ----------- | ---------- |
| switch(config)# | do          | show access-list |                  |             |            |
| Type            | Name        |                  |                  |             |            |
| Sequence        | Comment     |                  |                  |             |            |
|                 | Action      |                  |                  | L3 Protocol |            |
|                 | Source      | IP Address       |                  | Source      | L4 Port(s) |
|                 | Destination | IP Address       |                  | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |                  |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL2 |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- |
|      | 1 permit     |     |     | udp |     |
any
2001::1/64
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 41

|     | 2 Permit all | TCP ephemeral | ports |
| --- | ------------ | ------------- | ----- |
permit tcp
2001:2001::2:1 > 1023
any
3 permit tcp
2001:2011::1/64
any
4 deny any
any
any
|                | Hit-counts: | enabled |                                              |
| -------------- | ----------- | ------- | -------------------------------------------- |
| Command        | History     |         |                                              |
| Release        |             |         | Modification                                 |
| 10.12          |             |         | AllowACLsappliedtotheControlPlanetobelogged. |
| 10.07orearlier |             |         | --                                           |
| Command        | Information |         |                                              |
| Platforms      | Command     | context | Authority                                    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|     | Theaccess-listipv6 |     | rightsforthiscommand. |
| --- | ------------------ | --- | --------------------- |
<ACL-NAME>command
takesyouintothenamed
ACLcontextwhereyou
entertheACEs.
AccessControlLists|42

| access-list | log-timer |                      |     |     |     |
| ----------- | --------- | -------------------- | --- | --- | --- |
| access-list | log-timer | {default|<INTERVAL>} |     |     |     |
Description
SetsthelogtimerintervalforallACEsthathavethelogparameterconfigured.
| Parameter |     |     | Description                              |     |     |
| --------- | --- | --- | ---------------------------------------- | --- | --- |
| default   |     |     | Resetsthelogtimertoitsdefault300seconds. |     |     |
<INTERVAL>
Specifiesthelogtimerintervalinseconds.Range:5to300.
Usage
n ACLloggingkeepsalogofthenumberofpacketsmatchingthisACE.Workswithdenyactionsbutnot
withpermitactions.WorkswithACLsappliedoningress,orControlPlane,butnotwithACLsapplied
onegress.
n ThefirstpacketthatmatchesanACEwiththelogparameterwithinanACLlogtimerwindow
(configuredwiththeaccess-list log-timercommand)hasitsheadercontentsextractedandsentto
theconfiguredloggingdestination,suchastheconsoleandsyslogserver.EachtimetheACLlog
timerexpires,asummaryofallACEswithlogconfiguredaresenttotheloggingdestination.This
capabilityallowsthrottlingofloggingACLhits.
n Ifnofurtherlogmessagesaregeneratedinthewait-period,theswitchsuspendsthetimerandresets
itselftologassoonasanewmatchoccurs.
n WhenusingmultipleACLtypes(IPv4,IPv6,orMAC)withloggingonthesameinterface,thefirst
packetthatmatchesanACEwiththelogoptionislogged.Anypackets,matchingotherACLtypes,do
notcreatealoguntilthelog-timerwait-periodisover.Attheendofthewait-period,asummarylogis
madeofalltheACLsthatwerematched,regardlessoftype.
n YoumayseeaminordiscrepancybetweentheACLloggingstatisticsandthehitcountsstatisticsdue
tothetimerequiredtorecordthelogmessage.
Examples
Althoughtheseexamplesusedebuglogging,youcanalternativelyuseeventlogging.
EnablingdebugloggingfortheACLloggingmodule:
| switch# | debug acl  | log severity | info |     |     |
| ------- | ---------- | ------------ | ---- | --- | --- |
| switch# | show debug |              |      |     |     |
----------------------------------------------------------------
| module | sub_module | severity vlan | port | ip mac instance | vrf |
| ------ | ---------- | ------------- | ---- | --------------- | --- |
----------------------------------------------------------------
| acl | acl_log | info ----- | ----- | ----- ---- ----- | --- |
| --- | ------- | ---------- | ----- | ---------------- | --- |
Settingthedebugdestinationtoconsolewiththeminimumsecuritylevelofinfo:
| switch# | debug destination | console     | severity | info |     |
| ------- | ----------------- | ----------- | -------- | ---- | --- |
| switch# | show debug        | destination |          |      |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 43

---------------------------------------------------------------------

show debug destination

---------------------------------------------------------------------
CONSOLE:info

Setting the access list log-timer to 30 seconds:

switch(config)# access-list log-timer 30
switch(config)# do show access-list log-timer
ACL log timer length (frequency): 30 seconds

Creating an IPv4 ACL with one entry with the log parameter:

switch(config)# access-list ip MY_IP_ACL
switch(config-acl-ip)# deny icmp 1.1.1.1 1.1.1.2 log
switch(config-acl-ip)# do show access-list
Type

Name

Sequence Comment

Action
Source IP Address
Destination IP Address
Additional Parameters

L3 Protocol
Source L4 Port(s)
Destination L4 Port(s)

-------------------------------------------------------------------------------
IPv4

MY_IP_ACL

10 deny

icmp

1.1.1.1
1.1.1.2
Logging: enabled
Hit-counts: enabled

Enabling interface 1/1/1 and applying the ACL:

switch(config)# interface 1/1/1
switch(config-if)# no shutdown
switch(config-if)# no routing
switch(config-if)# apply access-list ip MY_IP_ACL in
switch(config-if)# do show running-config interface 1/1/1
interface 1/1/1

no shutdown
apply access-list ip MY_IP_ACL in
no routing
vlan access 1
exit

Sending packets that will match the ACE and observe the ACL logging message on the console:

2017-10-10T20:13:36.044+00:00 ops-switchd[875]: debug|LOG_INFO|AMM|1/5|ACL|ACL_
LOG|
List MY_IP_ACL, seq# 10 denied icmp 1.1.1.1 -> 1.1.1.2 type 8 code 0,
on vlan 1, port 1/1/1, direction in

When the access list log-timer expires, the summary message is printed on the console. The number 30
is the number of packets received during the last access list log-timer window.

Access Control Lists | 44

2017-10-10T20:14:06.051+00:00 ops-switchd[875]: debug|LOG_INFO|AMM|1/5|ACL|ACL_
LOG|
MY_IP_ACL on 1/1/1 (in): 30 10 deny icmp 1.1.1.1 1.1.1.2 log count
ResettingtheACLlogtimertothedefaultvalue:
| switch(config)#     | access-list |         | log-timer | default                                             |
| ------------------- | ----------- | ------- | --------- | --------------------------------------------------- |
| Command History     |             |         |           |                                                     |
| Release             |             |         |           | Modification                                        |
| 10.12               |             |         |           | AllowACLsappliedtotheControlPlanetobelogged.        |
| 10.09               |             |         |           | <INTERVAL>parameterrangechangedto5to300.Was30to300. |
| 10.07orearlier      |             |         |           | --                                                  |
| Command Information |             |         |           |                                                     |
| Platforms           | Command     | context |           | Authority                                           |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| access-list    | mac            |     |     |     |
| -------------- | -------------- | --- | --- | --- |
| access-list    | mac <ACL-NAME> |     |     |     |
| no access-list | mac <ACL-NAME> |     |     |     |
[<SEQUENCE-NUMBER>]
{permit|deny}
{any|<SRC-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|<DST-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|aarp|appletalk|arp|fcoe|fcoe-init|ip|ipv6|
ipx-arpa|ipx-non-arpa|is-is|lldp|mpls-multicast|mpls-unicast|q-in-q|
rbridge|trill|wake-on-lan|<NUMERIC-ETHERTYPE>}
| [pcp <PCP-VALUE>] | [vlan | <VLAN-ID>] |     | [count] [log] |
| ----------------- | ----- | ---------- | --- | ------------- |
no <SEQUENCE-NUMBER>
| [<SEQUENCE-NUMBER>]  | comment |     | <TEXT-STRING> |     |
| -------------------- | ------- | --- | ------------- | --- |
| no <SEQUENCE-NUMBER> | comment |     |               |     |
Description
CreatesaMACAccessControlList(ACL).TheACLismadeofoneormoreAccessControlEntries(ACEs)
orderedandprioritizedbysequencenumbers.Thelowestsequencenumberisthehighestprioritized
ACE.
ThenoformofthiscommanddeletestheentireACL,ordeletesanACEidentifiedbysequencenumber,
ordeletesonlythecommentfromtheACEidentifiedbysequencenumber.
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 45

Parameter

<ACL-NAME>

<SEQUENCE-NUMBER>

Description

Specifies the name of this ACL.

Specifies a sequence number for the ACE. Range: 1 to
4294967295.

{permit|deny}

Specifies whether to permit or deny traffic matching this ACE.

comment

Specifies storing the remaining entered text as an ACE comment.

{any|<SRC-MAC-ADDRESS>
[/<ETHERNET-MASK>}]}

{any|<DST-MAC-ADDRESS>
[/<ETHERNET-MASK>}]}

{any|aarp|appletalk| ... |wake-
on-lan|<NUMERIC-ETHERTYPE>

Specifies the source host MAC address (xxxx.xxxx.xxxx), OUI, or
the keyword any. You can optionally include the following:
<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).

Specifies the destination host MAC address (xxxx.xxxx.xxxx), OUI,
or the keyword any. You can optionally include the following:
<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).

Specifics the protocol encapsulated in the Ethernet frame. The
encapsulated protocol is identified by the EtherType Ethernet
field. The EtherType is specified in one of the following three
ways:
n any - any EtherType.
n <NUMERIC-ETHERTYPE> - the numerical EtherType protocol

number. Range: 0x600 to 0xffff.

n One of these EtherType protocol name keywords:

o aarp

o appletalk

o arp

o fcoe

o fcoe-init

o ip

o ipv6

o ipx-arpa

o ipx-non-arpa

o is-is

o lldp

o mpls-multicast

o mpls-unicast

o q-in-q

o rbridge

o trill

o wake-on-lan

pcp <PCP-VALUE>

Specifies 802.1Q QoS Priority Code Point value. Range: 0 to 7.

vlan <VID>

Specifies a VLAN ID. The VLAN ID must exist.

Access Control Lists | 46

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
NOTE:ThisparametercannotbeusedinanyACLthatwillbe
appliedtoaVLAN.
| count |     |     | KeepsthehitcountsofthenumberofpacketsmatchingthisACE. |     |
| ----- | --- | --- | ----------------------------------------------------- | --- |
| log   |     |     | KeepsalogofthenumberofpacketsmatchingthisACE.Works    |     |
withdenyactionsbutnotwithpermitactions.WorkswithACLs
appliedoningressbutnotwithACLsappliedonegress.
Usage
WhenusingmultipleACLtypes(IPv4,IPv6,orMAC)withloggingonthesameinterface,thefirstpacket
thatmatchesanACEwithlogoptionislogged.Untilthelog-timerwait-periodisover,anypackets
matchingotherACLtypesdonotcreatealog.Attheendofthewait-period,theswitchcreatesa
summarylogalltheACLsthatwerematched,regardlessoftype.
Examples
CreatingaMACACLwithfourentries:
| switch(config)# | access-list | mac | MY_MAC_ACL |     |
| --------------- | ----------- | --- | ---------- | --- |
switch(config-acl-ip)# 10 permit 1122.3344.5566/ffff.ffff.0000 any ipv6
switch(config-acl-ip)# 20 permit aaaa.bbbb.cccc 1111.2222.3333 any pcp 4
| switch(config-acl-ip)# |         | 30 permit   | any any appletalk | vlan 40 |
| ---------------------- | ------- | ----------- | ----------------- | ------- |
| switch(config-acl-ip)# |         | 40 deny     | any any any count |         |
| switch(config-acl-ip)# |         | exit        |                   |         |
| switch(config)#        | do show | access-list |                   |         |
| Type                   | Name    |             |                   |         |
| Sequence               | Comment |             |                   |         |
Action EtherType
|     | Source MAC  | Address     |     |     |
| --- | ----------- | ----------- | --- | --- |
|     | Destination | MAC Address |     |     |
|     | Additional  | Parameters  |     |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |
| --- | ---------- | --- | --- | --- |
10 permit ipv6
1122.3344.5566/ffff.ffff.0000
any
20 permit any
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point: | 4   |     |
| --- | ------------ | ----------- | --- | --- |
30 permit appletalk
any
any
VLAN: 40
40 deny any
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
AddingacommenttoanexistingMACACE:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 47

| switch(config)# |     | access-list |     | mac MY_MAC_ACL |     |     |     |     |
| --------------- | --- | ----------- | --- | -------------- | --- | --- | --- | --- |
switch(config-acl-ip)#
|                        |             |         | 30 comment  |         | Permit all | vlan-40 tagged | Appletalk | traffic |
| ---------------------- | ----------- | ------- | ----------- | ------- | ---------- | -------------- | --------- | ------- |
| switch(config-acl-ip)# |             |         | exit        |         |            |                |           |         |
| switch(config)#        |             | do show | access-list |         |            |                |           |         |
| Type                   | Name        |         |             |         |            |                |           |         |
| Sequence               | Comment     |         |             |         |            |                |           |         |
|                        | Action      |         |             |         |            | EtherType      |           |         |
|                        | Source      | MAC     | Address     |         |            |                |           |         |
|                        | Destination |         | MAC         | Address |            |                |           |         |
|                        | Additional  |         | Parameters  |         |            |                |           |         |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |     |      |     |     |
| --- | ---------- | --- | --- | --- | --- | ---- | --- | --- |
|     | 10 permit  |     |     |     |     | ipv6 |     |     |
1122.3344.5566/ffff.ffff.0000
any
|     | 20 permit |     |     |     |     | any |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS       | Priority | Code    | Point: | 4         |           |     |     |
| --- | --------- | -------- | ------- | ------ | --------- | --------- | --- | --- |
|     | 30 Permit | all      | vlan-40 | tagged | Appletalk | traffic   |     |     |
|     | permit    |          |         |        |           | appletalk |     |     |
any
any
|     | VLAN:   | 40  |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     | 40 deny |     |     |     |     | any |     |     |
any
any
|     | Hit-counts: |     | enabled |     |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
RemovingacommentfromanexistingMACACE:
switch(config)#
|                         |             | access-list |             | mac MY_MAC_ACL |     |           |     |     |
| ----------------------- | ----------- | ----------- | ----------- | -------------- | --- | --------- | --- | --- |
| switch(config-acl-mac)# |             |             | no          | 30 comment     |     |           |     |     |
| switch(config-acl-mac)# |             |             | exit        |                |     |           |     |     |
| switch(config)#         |             | do show     | access-list |                |     |           |     |     |
| Type                    | Name        |             |             |                |     |           |     |     |
| Sequence                | Comment     |             |             |                |     |           |     |     |
|                         | Action      |             |             |                |     | EtherType |     |     |
|                         | Source      | MAC         | Address     |                |     |           |     |     |
|                         | Destination |             | MAC         | Address        |     |           |     |     |
|                         | Additional  |             | Parameters  |                |     |           |     |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |     |      |     |     |
| --- | ---------- | --- | --- | --- | --- | ---- | --- | --- |
|     | 10 permit  |     |     |     |     | ipv6 |     |     |
1122.3344.5566/ffff.ffff.0000
any
|     | 20 permit |     |     |     |     | any |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS       | Priority | Code | Point: | 4   |           |     |     |
| --- | --------- | -------- | ---- | ------ | --- | --------- | --- | --- |
|     | 30 permit |          |      |        |     | appletalk |     |     |
any
any
|     | VLAN:   | 1   |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     | 40 deny |     |     |     |     | any |     |     |
any
any
|     | Hit-counts: |     | enabled |     |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- | --- |
AccessControlLists|48

AddinganACEtoanexistingMACACL:
| switch(config)#        | access-list | mac         | MY_MAC_ACL         |        |
| ---------------------- | ----------- | ----------- | ------------------ | ------ |
| switch(config-acl-ip)# |             | 35 permit   | any aabb.cc11.1234 | 0xffee |
| switch(config-acl-ip)# |             | exit        |                    |        |
| switch(config)#        | do show     | access-list |                    |        |
| Type                   | Name        |             |                    |        |
| Sequence               | Comment     |             |                    |        |
Action EtherType
|     | Source MAC  | Address     |     |     |
| --- | ----------- | ----------- | --- | --- |
|     | Destination | MAC Address |     |     |
|     | Additional  | Parameters  |     |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |
| --- | ---------- | --- | --- | --- |
10 permit ipv6
1122.3344.5566/ffff.ffff.0000
any
20 permit any
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point: | 4   |     |
| --- | ------------ | ----------- | --- | --- |
30 permit appletalk
any
any
VLAN: 1
35 permit 0xffee
any
aabb.cc11.1234
40 deny any
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
ReplacinganACEinanexistingMACACL:
| switch(config)#        | access-list | mac         | MY_MAC_ACL         |        |
| ---------------------- | ----------- | ----------- | ------------------ | ------ |
| switch(config-acl-ip)# |             | 35 permit   | any aabb.cc11.1234 | 0xeeee |
| switch(config-acl-ip)# |             | exit        |                    |        |
| switch(config)#        | do show     | access-list |                    |        |
| Type                   | Name        |             |                    |        |
| Sequence               | Comment     |             |                    |        |
Action EtherType
|     | Source MAC  | Address     |     |     |
| --- | ----------- | ----------- | --- | --- |
|     | Destination | MAC Address |     |     |
|     | Additional  | Parameters  |     |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |
| --- | ---------- | --- | --- | --- |
10 permit ipv6
1122.3344.5566/ffff.ffff.0000
any
20 permit any
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point: | 4   |     |
| --- | ------------ | ----------- | --- | --- |
30 permit appletalk
any
any
VLAN: 1
35 permit 0xeeee
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 49

any
aabb.cc11.1234
|     | 40 deny |     | any |
| --- | ------- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |
| --- | ----------- | ------- | --- |
RemovinganACEfromanMACACL:
| switch(config)#        | access-list | mac MY_MAC_ACL |           |
| ---------------------- | ----------- | -------------- | --------- |
| switch(config-acl-ip)# |             | no 35          |           |
| switch(config-acl-ip)# |             | exit           |           |
| switch(config)#        | do show     | access-list    |           |
| Type                   | Name        |                |           |
| Sequence               | Comment     |                |           |
|                        | Action      |                | EtherType |
|                        | Source MAC  | Address        |           |
|                        | Destination | MAC Address    |           |
|                        | Additional  | Parameters     |           |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |      |
| --- | ---------- | --- | ---- |
|     | 10 permit  |     | ipv6 |
1122.3344.5566/ffff.ffff.0000
any
|     | 20 permit |     | any |
| --- | --------- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point: | 4         |
| --- | ------------ | ----------- | --------- |
|     | 30 permit    |             | appletalk |
any
any
VLAN: 1
|     | 40 deny |     | any |
| --- | ------- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |
| --- | ----------- | ------- | --- |
RemovingaMACACL:
| switch(config)# | no access-list | mac         | MY_MAC_ACL |
| --------------- | -------------- | ----------- | ---------- |
| switch(config)# | do show        | access-list |            |
| Type            | Name           |             |            |
| Sequence        | Comment        |             |            |
|                 | Action         |             | EtherType  |
|                 | Source MAC     | Address     |            |
|                 | Destination    | MAC Address |            |
|                 | Additional     | Parameters  |            |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL2 |     |      |
| --- | ----------- | --- | ---- |
|     | 1 permit    |     | ipv6 |
1122.3344.5566/ffff.ffff.0000
any
|     | 2 permit |     | any |
| --- | -------- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code Point: | 4   |
| --- | ------------ | ----------- | --- |
AccessControlLists|50

|     | 3 Permit | all | vlan-40 | tagged | Appletalk | traffic |
| --- | -------- | --- | ------- | ------ | --------- | ------- |
|     | permit   |     |         |        | appletalk |         |
any
any
|     | VLAN:  | 1   |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- |
|     | 4 deny |     |     |     | any |     |
any
any
|                | Hit-counts: |     | enabled |     |              |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- |
| Command        | History     |     |         |     |              |     |
| Release        |             |     |         |     | Modification |     |
| 10.07orearlier |             |     |         |     | --           |     |
| Command        | Information |     |         |     |              |     |
| Platforms      | Command     |     | context |     | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|     | Theaccess-list |     |     | mac | forthiscommand. |     |
| --- | -------------- | --- | --- | --- | --------------- | --- |
<ACL-NAME>command
takesyouintothenamed
ACLcontextwhereyou
entertheACEs.
| access-list | resequence |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- |
access-list {ip|ipv6|mac} <ACL-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT>
Description
ResequencestheACEsequencenumbersinanACL.
| Parameter     |     |     |     |     | Description          |     |
| ------------- | --- | --- | --- | --- | -------------------- | --- |
| {ip|ipv6|mac} |     |     |     |     | SpecifiestheACLtype. |     |
<ACL-NAME>
SpecifiestheACLname.
<STARTING-SEQUENCE-NUMBER> Specifiesthestartingsequencenumber.
<INCREMENT>
Specifiesthesequencenumberincrement.
Examples
ResequencinganIPv4ACLtostartat1withanincrementof1:
| switch(config)#        |         | access-list |                  | ip MY_IP_ACL | resequence | 1 1 |
| ---------------------- | ------- | ----------- | ---------------- | ------------ | ---------- | --- |
| switch(config-acl-ip)# |         |             | exit             |              |            |     |
| switch(config)#        |         | do          | show access-list |              |            |     |
| Type                   | Name    |             |                  |              |            |     |
| Sequence               | Comment |             |                  |              |            |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 51

|     | Action      |     |            |     | L3 Protocol |            |
| --- | ----------- | --- | ---------- | --- | ----------- | ---------- |
|     | Source      | IP  | Address    |     | Source      | L4 Port(s) |
|     | Destination |     | IP Address |     | Destination | L4 Port(s) |
|     | Additional  |     | Parameters |     |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_ACL |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- |
|      | 1 permit  |     |     |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 2 permit               |     |     |     | tcp    |     |
| --- | ---------------------- | --- | --- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     |     |     | > 1023 |     |
any
|     | 3 permit |     |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- | --- |
172.26.1.0/255.255.255.0
any
|     | dscp: | AF11 |     |     |     |     |
| --- | ----- | ---- | --- | --- | --- | --- |
ack
syn
|     | 4 deny |     |     |     | any |     |
| --- | ------ | --- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- |
ResequencinganIPv6ACLtostartat1withanincrementof1:
| switch(config)#        |             | access-list | ipv6        | MY_IPV6_ACL | resequence  | 1 1        |
| ---------------------- | ----------- | ----------- | ----------- | ----------- | ----------- | ---------- |
| switch(config-acl-ip)# |             |             | exit        |             |             |            |
| switch(config)#        |             | do show     | access-list |             |             |            |
| Type                   | Name        |             |             |             |             |            |
| Sequence               | Comment     |             |             |             |             |            |
|                        | Action      |             |             |             | L3 Protocol |            |
|                        | Source      | IP          | Address     |             | Source      | L4 Port(s) |
|                        | Destination |             | IP Address  |             | Destination | L4 Port(s) |
|                        | Additional  |             | Parameters  |             |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- |
|      | 1 permit    |     |     |     | udp |     |
any
2001::1/64
|     | 2 Permit       | all | TCP ephemeral | ports |        |     |
| --- | -------------- | --- | ------------- | ----- | ------ | --- |
|     | permit         |     |               |       | tcp    |     |
|     | 2001:2001::2:1 |     |               |       | > 1023 |     |
any
|     | 3 permit |     |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 4 deny |     |     |     | any |     |
| --- | ------ | --- | --- | --- | --- | --- |
any
any
|          | Hit-counts: |     | enabled    |     |             |            |
| -------- | ----------- | --- | ---------- | --- | ----------- | ---------- |
| Type     | Name        |     |            |     |             |            |
| Sequence | Comment     |     |            |     |             |            |
|          | Action      |     |            |     | L3 Protocol |            |
|          | Source      | IP  | Address    |     | Source      | L4 Port(s) |
|          | Destination |     | IP Address |     | Destination | L4 Port(s) |
|          | Additional  |     | Parameters |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | --- |
|      | 1 permit    |     |     |     | udp |     |
any
AccessControlLists|52

2001::1/64
|     | 2 Permit       | all | TCP | ephemeral | ports |        |     |
| --- | -------------- | --- | --- | --------- | ----- | ------ | --- |
|     | permit         |     |     |           |       | tcp    |     |
|     | 2001:2001::2:1 |     |     |           |       | > 1023 |     |
any
|     | 3 permit |     |     |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
2001:2011::1/64
any
|     | 4 deny |     |     |     |     | any |     |
| --- | ------ | --- | --- | --- | --- | --- | --- |
any
any
|     | Hit-counts: |     | enabled |     |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- | --- |
ResequencingaMACACLtostartat1withanincrementof1:
| switch(config)#         |             | access-list |                  | mac MY_MAC_ACL |     | resequence | 1 1 |
| ----------------------- | ----------- | ----------- | ---------------- | -------------- | --- | ---------- | --- |
| switch(config-acl-mac)# |             |             | exit             |                |     |            |     |
| switch(config)#         |             | do          | show access-list |                |     |            |     |
| Type                    | Name        |             |                  |                |     |            |     |
| Sequence                | Comment     |             |                  |                |     |            |     |
|                         | Action      |             |                  |                |     | EtherType  |     |
|                         | Source      | MAC         | Address          |                |     |            |     |
|                         | Destination |             | MAC              | Address        |     |            |     |
|                         | Additional  |             | Parameters       |                |     |            |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |     |      |     |
| --- | ---------- | --- | --- | --- | --- | ---- | --- |
|     | 1 permit   |     |     |     |     | ipv6 |     |
1122.3344.5566/ffff.ffff.0000
any
|     | 2 permit |     |     |     |     | any |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS      | Priority | Code    | Point: | 4         |           |     |
| --- | -------- | -------- | ------- | ------ | --------- | --------- | --- |
|     | 3 Permit | all      | vlan-40 | tagged | Appletalk | traffic   |     |
|     | permit   |          |         |        |           | appletalk |     |
any
any
|     | VLAN:  | 1   |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- |
|     | 4 deny |     |     |     |     | any |     |
any
any
|                | Hit-counts: |     | enabled |     |              |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- |
| Command        | History     |     |         |     |              |     |     |
| Release        |             |     |         |     | Modification |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |
| Command        | Information |     |         |     |              |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| access-list | reset |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 53

access-list {all|ip <ACL-NAME>|ipv6 <ACL-NAME>|mac <ACL-NAME>} reset

Description

Changes the user-specified ACL configuration to match the active ACL configuration. Use this command
when a discrepancy exists between what the user configured and what is active and accepted by the
system.

Parameter

Description

all|ip ACL-NAME>|ipv6

<ACL-NAME>|mac <ACL-NAME>

Specifies one of the following:
n a reset of all ACLs.
n a reset of a named IPv4 ACL.
n a reset of a named IPv6 ACL.
n a reset of a named MAC ACL.

Usage

The output of the show access-list command displays the active configuration of the product. The
active configuration is the ACLs that have been configured and accepted by the system. The output of
the show access-list command with the configuration parameter, displays the ACLs that have been
configured. The output of this command may not be the same as what was programmed in hardware or
what is active on the product.

If the active ACLs and user-configured ACLs are not the same, a warning message is displayed in the
output of the show command. Modify the user-configured ACL until the warning message is no longer
displayed or run the access-list reset command to change the user-specified configuration to match
the active configuration.

Examples

Apply an ACL with TCP acknowledgments (ACKs) on ingress, which is unsupported by hardware:

switch(config-acl)# 10 permit tcp 172.16.2.0/16 any ack

Displaying the user-specified configuration:

switch(config)# do show access-list commands
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
access-list ip TEST_ACL
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
interface 1/1/1

apply access-list ip TEST_ACL in

switch(config)# do show access-list commands configuration
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
access-list ip TEST_ACL

10 permit tcp 172.16.2.0/255.255.0.0 any ack

! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active

Access Control Lists | 54

configuration.
| interface       | 1/1/1       |                  |     |             |            |
| --------------- | ----------- | ---------------- | --- | ----------- | ---------- |
| apply           | access-list | ip TEST_ACL      | in  |             |            |
| switch(config)# | do          | show access-list |     |             |            |
| Type            | Name        |                  |     |             |            |
| Sequence        | Comment     |                  |     |             |            |
|                 | Action      |                  |     | L3 Protocol |            |
|                 | Source      | IP Address       |     | Source      | L4 Port(s) |
|                 | Destination | IP Address       |     | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |     |             |            |
-------------------------------------------------------------------------------
% Warning: TEST_ACL user configuration does not match active configuration.
% run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| IPv4            | TEST_ACL    |                  |               |             |            |
| --------------- | ----------- | ---------------- | ------------- | ----------- | ---------- |
| switch(config)# | do          | show access-list | configuration |             |            |
| Type            | Name        |                  |               |             |            |
| Sequence        | Comment     |                  |               |             |            |
|                 | Action      |                  |               | L3 Protocol |            |
|                 | Source      | IP Address       |               | Source      | L4 Port(s) |
|                 | Destination | IP Address       |               | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |               |             |            |
-------------------------------------------------------------------------------
% Warning: TEST_ACL user configuration does not match active configuration.
% run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| IPv4 | TEST_ACL |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- |
10
|     | permit |     |     | tcp |     |
| --- | ------ | --- | --- | --- | --- |
172.16.2.0/255.255.0.0
any
ack
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| access-list | ip TEST_ACL |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| interface       | 1/1/1       |                  |          |               |     |
| --------------- | ----------- | ---------------- | -------- | ------------- | --- |
| apply           | access-list | ip TEST_ACL      | in       |               |     |
| switch(config)# | do          | show access-list | commands | configuration |     |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| access-list | ip TEST_ACL |                        |     |         |     |
| ----------- | ----------- | ---------------------- | --- | ------- | --- |
| 10 permit   | tcp         | 172.16.2.0/255.255.0.0 |     | any ack |     |
! access-list ip TEST_ACL user configuration does not match active configuration.
! run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| interface       | 1/1/1       |                  |     |             |            |
| --------------- | ----------- | ---------------- | --- | ----------- | ---------- |
| apply           | access-list | ip TEST_ACL      | in  |             |            |
| switch(config)# | do          | show access-list |     |             |            |
| Type            | Name        |                  |     |             |            |
| Sequence        | Comment     |                  |     |             |            |
|                 | Action      |                  |     | L3 Protocol |            |
|                 | Source      | IP Address       |     | Source      | L4 Port(s) |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 55

|     | Destination | IP         | Address |     | Destination | L4 Port(s) |
| --- | ----------- | ---------- | ------- | --- | ----------- | ---------- |
|     | Additional  | Parameters |         |     |             |            |
-------------------------------------------------------------------------------
% Warning: TEST_ACL user configuration does not match active configuration.
% run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| IPv4            | TEST_ACL    |                  |         |               |             |            |
| --------------- | ----------- | ---------------- | ------- | ------------- | ----------- | ---------- |
| switch(config)# | do          | show access-list |         | configuration |             |            |
| Type            | Name        |                  |         |               |             |            |
| Sequence        | Comment     |                  |         |               |             |            |
|                 | Action      |                  |         |               | L3 Protocol |            |
|                 | Source      | IP Address       |         |               | Source      | L4 Port(s) |
|                 | Destination | IP               | Address |               | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |         |               |             |            |
-------------------------------------------------------------------------------
% Warning: TEST_ACL user configuration does not match active configuration.
% run 'access-list TYPE NAME reset' to reset access-list to match active
configuration.
| IPv4 | TEST_ACL |     |     |     |     |     |
| ---- | -------- | --- | --- | --- | --- | --- |
10
|     | permit |     |     |     | tcp |     |
| --- | ------ | --- | --- | --- | --- | --- |
172.16.2.0/255.255.0.0
any
ack
Resettingtheuser-specifiedconfigurationtomatchtheactiveconfiguration.
| switch(config)# | access-list |     | ip  | TEST_ACL | reset |     |
| --------------- | ----------- | --- | --- | -------- | ----- | --- |
Displayingtheupdateduser-specifiedconfiguration.
| switch(config)# | do          | show access-list |          | commands |               |            |
| --------------- | ----------- | ---------------- | -------- | -------- | ------------- | ---------- |
| access-list     | ip TEST_ACL |                  |          |          |               |            |
| interface       | 1/1/1       |                  |          |          |               |            |
| apply           | access-list | ip               | TEST_ACL | in       |               |            |
| switch(config)# | do          | show access-list |          | commands | configuration |            |
| access-list     | ip TEST_ACL |                  |          |          |               |            |
| interface       | 1/1/1       |                  |          |          |               |            |
| apply           | access-list | ip               | TEST_ACL | in       |               |            |
| switch(config)# | do          | show access-list |          |          |               |            |
| Type            | Name        |                  |          |          |               |            |
| Sequence        | Comment     |                  |          |          |               |            |
|                 | Action      |                  |          |          | L3 Protocol   |            |
|                 | Source      | IP Address       |          |          | Source        | L4 Port(s) |
|                 | Destination | IP               | Address  |          | Destination   | L4 Port(s) |
|                 | Additional  | Parameters       |          |          |               |            |
-------------------------------------------------------------------------------
| IPv4            | TEST_ACL    |                  |         |               |             |            |
| --------------- | ----------- | ---------------- | ------- | ------------- | ----------- | ---------- |
| switch(config)# | do          | show access-list |         | configuration |             |            |
| Type            | Name        |                  |         |               |             |            |
| Sequence        | Comment     |                  |         |               |             |            |
|                 | Action      |                  |         |               | L3 Protocol |            |
|                 | Source      | IP Address       |         |               | Source      | L4 Port(s) |
|                 | Destination | IP               | Address |               | Destination | L4 Port(s) |
|                 | Additional  | Parameters       |         |               |             |            |
AccessControlLists|56

-------------------------------------------------------------------------------
| IPv4                | TEST_ACL |         |     |              |
| ------------------- | -------- | ------- | --- | ------------ |
| Command History     |          |         |     |              |
| Release             |          |         |     | Modification |
| 10.07orearlier      |          |         |     | --           |
| Command Information |          |         |     |              |
| Platforms           | Command  | context |     | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| access-list    | secure-update |     |     |     |
| -------------- | ------------- | --- | --- | --- |
| access-list    | secure-update |     |     |     |
| no access list | secure-update |     |     |     |
Description
Thiscommanddeterminesifaccesslistsareupdatedusingthesecure-updatefeature.Secure-updateis
enabledbydefault.
WhensecureupdateisenabledandanACLisupdatedorreplaced,oneormoreoverrideentriesare
installedintheTCAMtable(s)containingtheACLthatisbeingmodified.Asaresult,alltrafficofthe
sametypeasthecurrentlyconfiguredACLwillbedeniedontheinterfacestowhichtheACLisapplied.
ThisensuresthattrafficisnottemporarilyallowedwhilemodifyinganACL.Uponcompletionofthe
update,theTCAMoverrideentriesareuninstalledandtrafficresumesACLmatching.
Thenoversionofthiscommanddisablesthisfeature.Ifsecure-updateisdisabled,therewillbeno
overrideentryinstalled.ThisresultsinthefastermodificationofanACLandensuresthatthereisno
interruptiontopreviouslypermittedtraffic,butmaytemporarilyallowpreviouslydeniedtraffictopass
throughtheswitch.OncetheACLhasbeenmodified,trafficwillbeprocessedbytheupdatedACL.
Examples
Disablingsecureupdate:
| switch(config)# | no  | access-list |     | secure-update |
| --------------- | --- | ----------- | --- | ------------- |
Reenablingsecureupdate:
| switch(config)# | access-list |     | secure-update |     |
| --------------- | ----------- | --- | ------------- | --- |
Related Commands
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 57

| Command |     |     | Description |
| ------- | --- | --- | ----------- |
vsx-sync acl-secure-update IfthissettingisenabledandtheprimaryVSX node
hasconfigurationswiththeaccesslistsecure-
updatefeatureenabled, thisconfigurationcan
synchronizetothesecondarypeer.Thissettingis
disabledbydefault.RefertotheVSXGuidefor
details.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.13               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| apply access-list |     | control-plane |     |
| ----------------- | --- | ------------- | --- |
apply access-list {ip|ipv6} <ACL-NAME> control-plane vrf <VRF-NAME>
no apply access-list {ip|ipv6} <ACL-NAME> control-plane vrf <VRF-NAME>
Description
AppliesanACLtothespecifiedVRF.
ThenoformofthiscommandremovesapplicationoftheACLfromthespecifiedVRF.
| Parameter      |     |     | Description                                  |
| -------------- | --- | --- | -------------------------------------------- |
| ip|ipv6        |     |     | SpecifiestheACLtype:ipforIPv4,oripv6forIPv6. |
| <ACL-NAME>     |     |     | SpecifiestheACLname.                         |
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname.                         |
Usage
OnlyoneACLpertype(ip,oripv6)maybeappliedtoaControlPlaneVRFatatime.Therefore,usingthe
apply access-list control-planecommandonaVRFwithanalready-appliedACLofthesametype,will
replacetheappliedACL.
Examples
ApplyingMy_ip_ACLtoControlPlanetrafficonthedefaultVRF:
switch(config)# apply access-list ip My_ip_ACL control-plane vrf default
ReplacingMy_ip_ACLwithMy_Replacement_ACLonthedefaultVRF:
AccessControlLists|58

switch(config)# apply access-list ip My_Replacement_ACL control-plane vrf default
Remove(unapply)theMy_Replacement_ACLfromthedefaultVRF.AnyotherinterfacesorVLANswith
My_Replacement_ACLappliedareunaffected.
switch(config)# no apply access-list ip My_Replacement_ACL control-plane vrf
default
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| apply access-list    |     | (to interface | or LAG)         |            |
| -------------------- | --- | ------------- | --------------- | ---------- |
| no apply access-list | {ip | | ipv6 |      | mac} <ACL-NAME> | {in | out} |
Description
AppliesanACLtotheinterface(Individualfrontplaneport)orLinkAggregationGroup(LAG)identified
bythecurrentinterfaceorLAGcontext.
ThenoformofthiscommandremovesapplicationoftheACLfromthecurrentinterfaceorLAG
identifiedbythecurrentinterfaceorLAGcontext.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
ip|ipv6|mac SpecifiestheACLtype:ipforIPv4,ipv6forIPv6,ormacforMAC
ACL.
| <ACL-NAME> |     |     | SpecifiestheACLname. |     |
| ---------- | --- | --- | -------------------- | --- |
Selectstheinbound(ingress)trafficdirection.
in
out
Selectstheoutbound(egress)trafficdirection.OnlyforIPv4ACLs
appliedtoroute-onlyports.NotavailableforACLsappliedtoIPv4
bridgedports,IPv6ports,orMACACLsappliedtoports.
Usage
n EachACLofagiventypecanbeappliedtothesameinterfaceorLAGonceineachdirection.
Therefore,usingtheapply access-listcommandonaninterfaceorLAGwithanalready-appliedACL
ofthesametypewillreplacethecurrentlyappliedACL.
n AnACLcanbeappliedtoanindividualfrontplaneportortoaLinkAggregationGroup(LAG).
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 59

n AportthatisamemberofaLAGwithanappliedACLcannothaveadifferentACLappliedtothat
memberport.
n WhentheportmembershipofaLAGwithanappliedACLischanged,theLAGACLisautomatically
appliedorremovedfromthatportdependingonthemodificationtype.
n NoACLs(includingACLsforIPv4,IPv6,andMAC)aresupportedinegressontheLayer2interface.
EgressACLscanonlybeappliedtoLayer3(route-only)interfaces.ApplyinganegressACLtoaLayer
2interfaceresultsinanerror.
Loggingonoutbound(egress)trafficisalsonotsupported.Anerrormessagewillbedisplayedifan
n
ACLwithanyloggingACEsisattemptedtobeappliedonegress.
Examples
ApplyingMy_IP_ACLtoingresstrafficoninterfacerange1/1/10to1/1/12:
| switch(config)# | int 1/1/10-1/1/12 |     |     |     |
| --------------- | ----------------- | --- | --- | --- |
switch((config-if-<1/1/10-1/1/12>)# apply access-list ip My_IP_ACL in
| switch((config-if-<1/1/10-1/1/12>)# |     |     | exit |     |
| ----------------------------------- | --- | --- | ---- | --- |
ApplyingMY_IP_ACLtoingresstrafficonLAG100andegresstrafficoninterface1/1/2:
switch(config)#
|                        | interface | lag 100           |              |     |
| ---------------------- | --------- | ----------------- | ------------ | --- |
| switch(config-lag-if)# |           | apply access-list | ip MY_IP_ACL | in  |
| switch(config-lag-if)# |           | exit              |              |     |
| switch(config)#        | interface | 1/1/2             |              |     |
| switch(config-if)#     | apply     | access-list       | ip MY_IP_ACL | out |
| switch(config-if)#     | exit      |                   |              |     |
switch(config)#
ApplyingMY_IPV6_ACLtoingresstrafficoninterface1/1/1andtoingresstrafficonLAG100:
switch(config)#
|                        | interface | 1/1/1             |                  |     |
| ---------------------- | --------- | ----------------- | ---------------- | --- |
| switch(config-if)#     | apply     | access-list       | ipv6 MY_IPV6_ACL | in  |
| switch(config-if)#     | exit      |                   |                  |     |
| switch(config)#        | interface | lag 100           |                  |     |
| switch(config-lag-if)# |           | apply access-list | ipv6 MY_IPV6_ACL | in  |
| switch(config-lag-if)# |           | exit              |                  |     |
switch(config)#
ApplyingMY_MAC_ACLtoingresstrafficoninterface1/1/1andingresstrafficoninterface1/1/2:
switch(config)#
|                    | interface | 1/1/1       |                |     |
| ------------------ | --------- | ----------- | -------------- | --- |
| switch(config-if)# | apply     | access-list | mac MY_MAC_ACL | in  |
| switch(config-if)# | exit      |             |                |     |
| switch(config)#    | interface | 1/1/2       |                |     |
| switch(config-if)# | apply     | access-list | mac MY_MAC_ACL | in  |
| switch(config-if)# | exit      |             |                |     |
switch(config)#
AccessControlLists|60

ReplacingMY_IP_ACLwithMY_REPLACEMENT_ACLoninterface1/1/2:
| switch(config)#    |     | interface | 1/1/2       |                       |     |
| ------------------ | --- | --------- | ----------- | --------------------- | --- |
| switch(config-if)# |     | apply     | access-list | ip MY_REPLACEMENT_ACL | out |
| switch(config-if)# |     | exit      |             |                       |     |
switch(config)#
UnapplyingMY_REPLACEMENT_ACLfrominterface1/1/2(out):
switch(config)#
|     |     | interface | 1/1/2 |     |     |
| --- | --- | --------- | ----- | --- | --- |
switch(config-if)# no apply access-list ip MY_REPLACEMENT_ACL out
| switch(config-if)# |     | exit |     |     |     |
| ------------------ | --- | ---- | --- | --- | --- |
switch(config)#
| Command History     |         |     |         |                                      |     |
| ------------------- | ------- | --- | ------- | ------------------------------------ | --- |
| Release             |         |     |         | Modification                         |     |
| 10.11               |         |     |         | Egresssupportextendedto9300platform. |     |
| 10.07orearlier      |         |     |         | --                                   |     |
| Command Information |         |     |         |                                      |     |
| Platforms           | Command |     | context | Authority                            |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|                   | config-lag-if |     |            | rightsforthiscommand.  |     |
| ----------------- | ------------- | --- | ---------- | ---------------------- | --- |
| apply access-list |               | (to | interface  | VLAN)                  |     |
| apply access-list | {ip|ipv6}     |     | <ACL-NAME> | {routed-in|routed-out} |     |
no apply access-list {ip|ipv6} <ACL-NAME> {routed-in|routed-out}
Description
AppliesanACLtotheinterfaceVLAN(orrangeofinterfaceVLANs)identifiedbythecurrentinterface
VLANcontext.Usingtheapplyaccess-listcommandonaninterfaceVLANinterfacewithanalready-
appliedACLofthesamedirectionandtypewillreplacethecurrently-appliedACL.
ThenoformofthiscommandremovesapplicationoftheACLfromtheinterfaceVLAN(orrangeof
interfaceVLANs)identifiedbythecurrentinterfaceVLANcontext.
| Parameter  |     |     |     | Description                                |     |
| ---------- | --- | --- | --- | ------------------------------------------ | --- |
| ip|ipv6    |     |     |     | SpecifiestheACLtype:ipforIPv4,ipv6forIPv6. |     |
| <ACL-NAME> |     |     |     | SpecifiestheACLname.                       |     |
routed-in Selectstheroutedinbound(routedingress)trafficdirection.
routed-out Selectstheroutedoutbound(routedegress)trafficdirection.
Usage
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 61

n EachACLofagiventypecanbeappliedtothesameinterfaceVLANonceineachdirection.
Therefore,usingtheapply access-listcommandonaninterfaceVLANwithanalready-applied
ACLofthesamedirectionandtype,willreplacetheappliedACL.
Examples
CreatinganIPv4ACLandapplyingittoroutedingresstrafficoninterfaceVLANvlan100:
| switch(config)#        | access-list | ip        | test        |               |
| ---------------------- | ----------- | --------- | ----------- | ------------- |
| switch(config-acl-ip)# |             | 10 permit | any 1.1.1.2 | 2.2.2.2 count |
| switch(config-acl-ip)# |             | 20 permit | any 1.1.1.2 | 2.2.2.1 count |
| switch(config-acl-ip)# |             | 30 permit | any 2.2.2.2 | 1.1.1.2 count |
| switch(config-acl-ip)# |             | 40 permit | any 2.2.2.2 | 1.1.1.1 count |
| switch(config-acl-ip)# |             | 50 permit | any any     | any count     |
| switch(config-acl-ip)# |             | exit      |             |               |
switch(config)#
| switch(config)#         | interface | vlan100 |             |                   |
| ----------------------- | --------- | ------- | ----------- | ----------------- |
| switch(config-if-vlan)# |           | apply   | access-list | ip test routed-in |
ApplyingMy_ip_ACLtoroutedingresstrafficoninterfaceVLAN10:
| switch(config)# | interface | vlan | 10  |     |
| --------------- | --------- | ---- | --- | --- |
switch(config-if-vlan)# apply access-list ip My_ip_ACL routed-in
ApplyingMy_ipv6_ACLtoroutedingresstrafficoninterfaceVLAN10:
| switch(config)# | interface | vlan | 10  |     |
| --------------- | --------- | ---- | --- | --- |
switch(config-if-vlan)# apply access-list ipv6 My_ip_ACL routed-in
ApplyingMy_ip_ACLtoroutedingresstrafficoninterfaceVLANs20to25:
| switch(config)# | interface | vlan | 20-25 |     |
| --------------- | --------- | ---- | ----- | --- |
switch(config-if-vlan-<20-25>)# apply access-list ip My_ip_ACL routed-in
ReplacingMy_ipv6_ACLwithMy_Replacement_ACLoninterfaceVLAN10(followingtheabove
examples):
| switch(config)# | interface | vlan | 10  |     |
| --------------- | --------- | ---- | --- | --- |
switch(config-if-vlan)# apply access-list ipv6 My_Replacement_ACL routed-in
Removing(unapplying)My_Replacement_ACLoninterfaceVLAN10.AnyotherinterfacesorVLANswith
My_Replacement_ACLappliedarenotaffected:
| switch(config)# | interface | vlan | 10  |     |
| --------------- | --------- | ---- | --- | --- |
switch(config-if-vlan)# no apply access-list ipv6 My_Replacement_ACL routed-in
Removing(unapplying)My_ip_ACLoninterfaceVLANs20to25.AnyotherinterfacesorVLANswithMy_
ip_ACLappliedarenotaffected:
AccessControlLists|62

| switch(config)# | interface | vlan | 20-25 |     |     |
| --------------- | --------- | ---- | ----- | --- | --- |
switch(config-if-vlan-<20-25>)#
|     |     |     | no apply access-list | ip My_ip_ACL | routed-in |
| --- | --- | --- | -------------------- | ------------ | --------- |
ApplyingMy_ip_ACLtoroutedegresstrafficoninterfaceVLAN30:
| switch(config)# | interface | vlan | 30  |     |     |
| --------------- | --------- | ---- | --- | --- | --- |
switch(config-if-vlan)# apply access-list ip My_ip_ACL routed-out
ApplyingMy_ip_ACLtoroutedegresstrafficoninterfaceVLANs40to50:
| switch(config)# | interface | vlan | 40-50 |     |     |
| --------------- | --------- | ---- | ----- | --- | --- |
switch(config-if-vlan-<40-50>)# apply access-list ip My_ip_ACL routed-out
| Command History     |         |         |              |     |     |
| ------------------- | ------- | ------- | ------------ | --- | --- |
| Release             |         |         | Modification |     |     |
| 10.07orearlier      |         |         | --           |     |     |
| Command Information |         |         |              |     |     |
| Platforms           | Command | context | Authority    |     |     |
8320 config-if-vlan Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     | rightsforthiscommand. |     |     |
| ---- | --- | --- | --------------------- | --- | --- |
8325H
8325P
9300
9300S
10000
10040
| apply access-list |     | (to L3 VNI) |     |     |     |
| ----------------- | --- | ----------- | --- | --- | --- |
Description
AppliesanACLtothecurrentL3VNI.Onlyonedirection(`routed-in`)andonetype(IPv4/IPv6)ofanACL
maybeappliedtoanL3VNIatatime,thustheapplycommandonanL3VNIwithanalreadyapplied
ACLofthesamedirectionandtypereplacesthecurrently-appliedACL.
ThenoformofthiscommandremovesapplicationoftheACLfromtheL3VNIidentifiedbythecurrent
L3VNIcontext.
| Parameter |     |     | Description                                 |     |     |
| --------- | --- | --- | ------------------------------------------- | --- | --- |
| ip|ipv6   |     |     | SpecifiestheACLtype:ipforIPv4oripv6forIPv6. |     |     |
<ACL-NAME>
SpecifiestheACLname.
routed-in Selectstherouted-inbound(routedingress)trafficdirection.
Usage
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 63

n EachACLofagiventypecanbeappliedtothesameL3VNIinterfaceonceineachdirection.
Therefore,usingtheapply access-listcommandonanL3VNIinterfacewithanalready-appliedACL
ofthesametype,willreplacetheappliedACL.
Examples
ApplyingMy_ip_ACLtoroutedingresstrafficonVNI10:
| switch(config)# | interface | vxlan 1 |
| --------------- | --------- | ------- |
switch(config-vxlan-if)#
vni 10
| switch(config-vni-10)# |     | vrf red |
| ---------------------- | --- | ------- |
| switch(config-vni-10)# |     | routing |
switch(config-vni-10)# apply access-list ip My_ip_ACL routed-in
| switch(config-vni-10)#   |     | exit |
| ------------------------ | --- | ---- |
| switch(config-vxlan-if)# |     | exit |
switch(config)#
ApplyingMy_ipv6_ACLtoroutedingresstrafficonVNI10:
| switch(config)# | interface | vxlan 1 |
| --------------- | --------- | ------- |
switch(config-vxlan-if)#
vni 10
| switch(config-vni-10)# |     | vrf red |
| ---------------------- | --- | ------- |
| switch(config-vni-10)# |     | routing |
switch(config-vni-10)# apply access-list ipv6 My_ipv6_ACL routed-in
| switch(config-vni-10)#   |     | exit |
| ------------------------ | --- | ---- |
| switch(config-vxlan-if)# |     | exit |
switch(config)#
ReplacingMy_ipv6_ACLwithMy_Replacement_ACLonVNI10(followingtheprecedingexamples):
| switch(config)# | interface | vxlan 1 |
| --------------- | --------- | ------- |
switch(config-vxlan-if)#
vni 10
switch(config-vni-10)# apply access-list ipv6 My_Replacement_ACL routed-in
| switch(config-vni-10)#   |     | exit |
| ------------------------ | --- | ---- |
| switch(config-vxlan-if)# |     | exit |
switch(config)#
RemovingMy_Replacement_ACLoninterfaceVNI 10.Anyotherinterfaces,VLANs,orVNIswithMy_ip_
ACLappliedarenotaffected:
| switch(config)#          | interface | vxlan 1 |
| ------------------------ | --------- | ------- |
| switch(config-vxlan-if)# |           | vni 10  |
switch(config-vni-10)# no apply access-list ipv6 My_Replacement_ACL routed-in
| switch(config-vni-10)#   |     | exit |
| ------------------------ | --- | ---- |
| switch(config-vxlan-if)# |     | exit |
switch(config)#
Command History
Release Modification
10.16 Addedsupportfor8325and8325Hswitchseries.
10.14 AddedsupportforL3VNIACLs.
10.07orearlier --
AccessControlLists|64

| Command Information  |                      |                   |            |     |
| -------------------- | -------------------- | ----------------- | ---------- | --- |
| Platforms            | Command              | context           | Authority  |     |
| 8325                 | Operator(>)orManager |                   |            |     |
| 8325H                | (#)                  |                   |            |     |
| apply access-list    |                      | (to subinterface) |            |     |
| apply access-list    |                      | {ip|ipv6|mac}     | <ACL-NAME> | in  |
| no apply access-list |                      | {ip|ipv6|mac}     | <ACL-NAME> | in  |
Description
AppliesanACLtothecurrentportorLAGsubinterfacecontextorsubinterfacecontextrange.
ThenoformofthiscommandremovesapplicationoftheACLfromthecurrentportorLAGsubinterface
contextorsubinterfacecontextrange.
AnACLcannotbeappliedtotheparentinterfaceofoneormoresubinterfaces.Thisalsomeansthata
subinterfacecannotbeaddedtoaninterfaceifthereisanACLapplied.
ACEVLANIDscannotbeaddedtoACLsappliedtosubinterfaces.ThisalsomeansthatanACLwithanACE
matchingonaVLANIDcannotbeappliedtoasubinterface.
| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
ip|ipv6|mac SpecifiestheACLtype:ipforIPv4,ipv6forIPv6,ormacforMAC
ACL.
| <ACL-NAME> |     |     | SpecifiestheACLname.        |     |
| ---------- | --- | --- | --------------------------- | --- |
| in         |     |     | Selectsthetrafficdirection. |     |
Usage
n EachACLofagiventypecanbeappliedtothesamesubinterfaceonce.Therefore,usingtheapply
access-listcommandonasubinterfacewithanalready-appliedACLofthesametypewillreplace
thecurrentlyappliedACL.
InthecaseofafailedACLapplicationtoasubinterfaceduringswitchrebootorhotswap,the
n
subinterfacewillbeshutdown.Fixingthefailurewillcausethesubinterfacetocomebackup.
n InthecaseofafailedACLapplicationtoanaddedsubinterfaceLAGmember(s),theentireLAG
subinterfacewillbeshutdown.FixingthefailurewillcausetheLAGsubinterfacetocomebackup.
Forthiscasetooccur,theACLmustalreadybesuccessfullyappliedtoexistingsubinterfaceLAG
members.ThisisdonetopreventtrafficfromcircumventingtheACLbypassingthroughnewLAG
memberswheretheACLwasnotsuccessfullyapplied.ThisonlyoccurswhentheLAGspansmore
thanonelinecardorstackmember.
Examples
ApplyingMy_ip_ACLtoingresstrafficonsubinterface1/1/1.10:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 65

| switch(config)# | interface | 1/1/1.10 |     |     |
| --------------- | --------- | -------- | --- | --- |
switch(config-subif)#
|                       | apply     | access-list | ip My_ip_ACL     | in  |
| --------------------- | --------- | ----------- | ---------------- | --- |
| switch(config)#       | interface | 1/1/2.8     |                  |     |
| switch(config-subif)# | apply     | access-list | ip My_ip_ACL_egr | out |
ApplyingMy_ipv6_ACLtoingresstrafficonsubinterface1/1/1.10:
| switch(config)#       | interface | 1/1/1.10    |                  |     |
| --------------------- | --------- | ----------- | ---------------- | --- |
| switch(config-subif)# | apply     | access-list | ipv6 My_ipv6_ACL | in  |
ApplyingMy_ip_ACLtoingresstrafficonsubinterfacerange1/1/1.11to1/1/1.15:
| switch(config)# | interface | 1/1/1.11-1/1/1.15 |     |     |
| --------------- | --------- | ----------------- | --- | --- |
switch(config-subif-<1/1/1.11-1/1/1.15>)# apply access-list ip My_ip_ACL in
ReplacingMy_ipv6_ACLwithMy_Replacement_ACLonsubinterface1/1/1.10(followingtheabove
examples):
| switch(config)# | interface | 1/1/1.10 |     |     |
| --------------- | --------- | -------- | --- | --- |
switch(config-subif)# apply access-list ipv6 My_Replacement_ACL in
Removing(unapplying)My_Replacement_ACLonsubinterface1/1/1.10.AnyotherinterfacesorVLANs
withMy_Replacement_ACLappliedarenotaffected.
| switch(config)# | interface | 1/1/1.10 |     |     |
| --------------- | --------- | -------- | --- | --- |
switch(config-subif)# no apply access-list ipv6 My_Replacement_ACL in
Removing(unapplying)My_ip_ACLonsubinterface1/1/1.11to1/1/1.15.AnyotherinterfacesorVLANs
withMy_ip_ACLappliedarenotaffected.
| switch(config)# | interface | 1/1/1.11-1/1/1.15 |     |     |
| --------------- | --------- | ----------------- | --- | --- |
switch(config-subif-<1/1/1.11-1/1/1.15>)# no apply access-list ip My_ip_ACL in
ApplyingMy_ip_ACLtoingresstrafficonsubinterfacelag1.10:
| switch(config)#       | interface | lag1.10     |              |     |
| --------------------- | --------- | ----------- | ------------ | --- |
| switch(config-subif)# | apply     | access-list | ip My_ip_ACL | in  |
Removing(unapplying)My_ip_ACLfromsubinterfacelag1.10:
switch(config)#
|                       | interface | lag1.10           |              |     |
| --------------------- | --------- | ----------------- | ------------ | --- |
| switch(config-subif)# | no        | apply access-list | ip My_ip_ACL | in  |
Command History
AccessControlLists|66

| Release             |         |         |     | Modification                 |     |     |
| ------------------- | ------- | ------- | --- | ---------------------------- | --- | --- |
| 10.11               |         |         |     | Commandintroducedonthe8325.  |     |     |
| 10.11               |         |         |     | Commandintroducedonthe10000. |     |     |
| Command Information |         |         |     |                              |     |     |
| Platforms           | Command | context |     | Authority                    |     |     |
8325 config-subif Administratorsorlocalusergroupmemberswithexecution
| 8325H |     |     |     | rightsforthiscommand. |     |     |
| ----- | --- | --- | --- | --------------------- | --- | --- |
8325P
10000
| apply access-list    |     | (to VLAN)     |            |            |          |     |
| -------------------- | --- | ------------- | ---------- | ---------- | -------- | --- |
| apply access-list    |     | {ip|ipv6|mac} | <ACL-NAME> |            | {in|out} |     |
| no apply access-list |     | {ip|ipv6|mac} |            | <ACL-NAME> | {in|out} |     |
Description
AppliesanACLtotheVLANidentifiedbythecurrentVLANcontext.
ThenoformofthiscommandremovesapplicationoftheACLfromtheVLANidentifiedbythecurrent
VLANcontext.
| Parameter |     |     |     | Description |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- |
ip|ipv6|mac
SpecifiestheACLtype:ipforIPv4,ipv6forIPv6,ormacforMAC
ACL.
| <ACL-NAME> |     |     |     | SpecifiestheACLname. |     |     |
| ---------- | --- | --- | --- | -------------------- | --- | --- |
in
Selectstheinbound(ingress)trafficdirection.
| out |     |     |     | Selectstheoutbound(egress)trafficdirection. |     |     |
| --- | --- | --- | --- | ------------------------------------------- | --- | --- |
NOTE:ForHPEArubaNetworking6000and6100Switchseries,
theoutbound(egress)trafficdirectionissupportedonlyforMAC
ACLs.
Usage
EachACLofagiventypecanbeappliedtothesameVLANonceineachdirection.Therefore,usingthe
apply access-listcommandonaVLANwithanalready-appliedACLofthesametype,willreplacethe
appliedACL.
Examples
ApplyingMy_ip_ACLtoingresstrafficonVLANrange20to25:
| switch(config)#              |     | vlan 20-25 |       |             |              |     |
| ---------------------------- | --- | ---------- | ----- | ----------- | ------------ | --- |
| switch(config-vlan-<20-25>)# |     |            | apply | access-list | ip My_ip_ACL | in  |
ApplyingMy_ip_ACLtoegresstrafficonVLANrange40to50:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 67

| switch(config)# | vlan | 40-50. |     |     |     |     |     |
| --------------- | ---- | ------ | --- | --- | --- | --- | --- |
switch(config-vlan-<40-50>)#
|     |     |     | apply access-list |     | ip My_ip_ACL |     | out |
| --- | --- | --- | ----------------- | --- | ------------ | --- | --- |
ApplyingMy_ip_ACLtoingresstrafficonVLAN10:
| switch(config)#         | vlan | 10    |             |     |           |     |     |
| ----------------------- | ---- | ----- | ----------- | --- | --------- | --- | --- |
| switch(config-vlan-10)# |      | apply | access-list | ip  | My_ip_ACL | in  |     |
ApplyingMy_ipv6_ACLtoingresstrafficonVLAN10:
| switch(config)#         | vlan | 10    |             |      |             |     |     |
| ----------------------- | ---- | ----- | ----------- | ---- | ----------- | --- | --- |
| switch(config-vlan-10)# |      | apply | access-list | ipv6 | My_ipv6_ACL |     | in  |
ApplyingMy_mac_ACLtoingresstrafficonVLAN10:
| switch(config)#         | vlan | 10    |             |     |            |     |     |
| ----------------------- | ---- | ----- | ----------- | --- | ---------- | --- | --- |
| switch(config-vlan-10)# |      | apply | access-list | mac | My_mac_ACL |     | in  |
ReplacingMy_ipv6_ACLwithMy_Replacement_ACLonVLAN10(followingtheprecedingexamples):
| switch(config)# | vlan | 10  |     |     |     |     |     |
| --------------- | ---- | --- | --- | --- | --- | --- | --- |
switch(config-vlan-10)# apply access-list ipv6 My_Replacement_ACL in
Removing(unapplying,SpecifiestheACLtype:ipforIPv4,ipv6forIPv6,ormacforMACACL.)several
ACLsonVLAN10:
| switch(config)# | vlan | 10  |     |     |     |     |     |
| --------------- | ---- | --- | --- | --- | --- | --- | --- |
switch(config-vlan-10)# no apply access-list ipv6 My_Replacement_ACL in
| switch(config-vlan-10)# |         | no      | apply access-list |     | mac My_mac_ACL |     | in  |
| ----------------------- | ------- | ------- | ----------------- | --- | -------------- | --- | --- |
| Command History         |         |         |                   |     |                |     |     |
| Release                 |         |         | Modification      |     |                |     |     |
| 10.07orearlier          |         |         | --                |     |                |     |     |
| Command Information     |         |         |                   |     |                |     |     |
| Platforms               | Command | context | Authority         |     |                |     |     |
Allplatforms config-vlan Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| clear access-list | hitcounts |       |                  |     |             |     |     |
| ----------------- | --------- | ----- | ---------------- | --- | ----------- | --- | --- |
| clear access-list | hitcounts | { all | | [{ip|ipv6|mac} |     | <ACL-NAME>] |     |     |
[interface <IF-NAME>| vlan <VLAN-ID>] [in|out|routed-in|routed-out] }
Description
ClearsthehitcountsforACLswithACEsthatincludethecountkeyword.
AccessControlLists|68

| Parameter |     |     | Description     |     |
| --------- | --- | --- | --------------- | --- |
| all       |     |     | SelectsallACLs. |     |
ip|ipv6|mac
SpecifiestheACLtype:ipforIPv4,ipv6forIPv6,ormacforMAC.
| <ACL-NAME>     |           |     | SpecifiestheACLname.                        |     |
| -------------- | --------- | --- | ------------------------------------------- | --- |
| interface      | <IF-NAME> |     | Specifiestheinterfacename(portorLAG).       |     |
| vlan <VLAN-ID> |           |     | SpecifiestheVLAN.                           |     |
| in             |           |     | Selectstheinbound(ingress)trafficdirection. |     |
out Selectstheoutbound(egress)trafficdirection.AvailableforIPv4
andIPv6ACLsappliedtoVLANsandforIPv4ACLsappliedto
route-onlyports.NotavailableforACLsappliedtoeitherIPv4
bridgedportsorIPv6ports,orforMACACLsappliedtoportsor
VLANS.
routed-in|routed-out SelectstheroutedtrafficdirectiononwhichtheACLisapplied.
NOTE:
ThisisonlyavailableforIPv4andIPv6ACLsappliedto
interfaceVLANs.
n routed-inselectstheroutedinbound(routedingress)traffic
direction.
n routed-outselectstheroutedoutbound(routedegress)traffic
direction.
Examples
ClearingthehitcountsforMy_ip_ACLappliedtoport1/1/2(egress):
switch# clear access-list hitcounts ip My_ip_ACL interface 1/1/2 out
ClearingthehitcountsforMy_ip_ACLappliedtoVLAN10(ingress):
| switch# | clear access-list | hitcounts | ip My_ip_ACL | vlan 10 in |
| ------- | ----------------- | --------- | ------------ | ---------- |
ClearingthehitcountsforallACLs:
switch#
|                | clear access-list | hitcounts | all          |     |
| -------------- | ----------------- | --------- | ------------ | --- |
| Command        | History           |           |              |     |
| Release        |                   |           | Modification |     |
| 10.07orearlier |                   |           | --           |     |
| Command        | Information       |           |              |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 69

| Platforms    | Command              |     | context | Authority |
| ------------ | -------------------- | --- | ------- | --------- |
| Allplatforms | Operator(>)orManager |     |         |           |
(#)
| clear access-list |     | hitcounts |     | control-plane |
| ----------------- | --- | --------- | --- | ------------- |
clear access-list hitcounts [{ip|ipv6} <ACL-NAME>] control-plane vrf <VRF-NAME>
Description
ClearsthehitcountsforACLsappliedtotheControlPlaneVRF.
| Parameter      |     |     |     | Description                                  |
| -------------- | --- | --- | --- | -------------------------------------------- |
| ip|ipv6        |     |     |     | SpecifiestheACLtype:ipforIPv4,oripv6forIPv6. |
| <ACL-NAME>     |     |     |     | SpecifiestheACLname.                         |
| vrf <VRF-NAME> |     |     |     | SpecifiestheVRFname.                         |
Examples
ClearingthehitcountsforanIPv4ACLappliedtotheControlPlanedefaultVRF:
switch# clear access-list hitcounts ip My_ipv4_ACL control-plane vrf default
ClearingthehitcountsforanIPv6ACLappliedtotheControlPlanedefaultVRF:
switch# clear access-list hitcounts ipv6 My_ipv6_ACL control-plane vrf default
| Command History     |         |     |         |              |
| ------------------- | ------- | --- | ------- | ------------ |
| Release             |         |     |         | Modification |
| 10.07orearlier      |         |     |         | --           |
| Command Information |         |     |         |              |
| Platforms           | Command |     | context | Authority    |
Allplatforms
Operator(>)orManager
(#)
| object-group | address |     | resequence |     |
| ------------ | ------- | --- | ---------- | --- |
object-group {ip|ipv6} address <OBJECT-GROUP-NAME> resequence <STARTING-SEQUENCE-NUMBER>
<INCREMENT>
Description
Reordersthesequencenumbersinanaddressobjectgroup.
AccessControlLists|70

| Parameter           |     |     |     |     | Description                                          |     |     |
| ------------------- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- |
| ip|ipv6             |     |     |     |     | SpecifiestheobjectgroupIPaddresstype,eitheriporipv6. |     |     |
| <OBJECT-GROUP-NAME> |     |     |     |     | Specifiestheaddressobjectgroupname.                  |     |     |
<STARTING-SEQUENCE-NUMBER> Specifiesthestartingsequencenumber.
| <INCREMENT> |     |     |     |     | Specifiesthesequencenumberincrement. |     |     |
| ----------- | --- | --- | --- | --- | ------------------------------------ | --- | --- |
Examples
Resequencingaddressobjectgroupmy_ipv4_addr_grouptousesequencenumbers5,10,15andsoon:
switch(config)# object-group address my_ipv4_addr_group resequence 5 5
switch(config)#
| Command        | History     |     |         |     |              |     |     |
| -------------- | ----------- | --- | ------- | --- | ------------ | --- | --- |
| Release        |             |     |         |     | Modification |     |     |
| 10.07orearlier |             |     |         |     | --           |     |     |
| Command        | Information |     |         |     |              |     |     |
| Platforms      | Command     |     | context |     | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| object-group |           | address | reset   |                     |     |     |       |
| ------------ | --------- | ------- | ------- | ------------------- | --- | --- | ----- |
| object-group | {ip|ipv6} |         | address | <OBJECT-GROUP-NAME> |     |     | reset |
Description
Resetstheuserconfigurationbacktotheactiveconfiguration.Thiscommandtakesimmediateeffect,it
isnotsavedintheuserconfiguration.Usethiscommandifmisconfigurationofanaddressobjectgroup
hasoccurred.
| Parameter           |     |     |     |     | Description                                          |     |     |
| ------------------- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- |
| ip|ipv6             |     |     |     |     | SpecifiestheobjectgroupIPaddresstype,eitheriporipv6. |     |     |
| <OBJECT-GROUP-NAME> |     |     |     |     | Specifiestheaddressobjectgroupname.                  |     |     |
Examples
ResettingIPv4addressobjectgroupmy_ipv4_group:
| switch(config)# |     | object-group |     | ip  | address | my_ip_group | reset |
| --------------- | --- | ------------ | --- | --- | ------- | ----------- | ----- |
switch(config)#
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 71

ResettingIPv6addressobjectgroupmy_ipv6_group:
| switch(config)# | object-group | ipv6 | address my_ipv6_group | reset |
| --------------- | ------------ | ---- | --------------------- | ----- |
switch(config)#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| object-group | all reset |     |     |     |
| ------------ | --------- | --- | --- | --- |
| object-group | all reset |     |     |     |
Description
Resetstheuserconfigurationbacktotheactiveconfigurationforallobjecttypes(addressandport).
Thiscommandtakesimmediateeffect,itisnotsavedintheuserconfiguration.Usethiscommandif
misconfigurationofaddressobjectgroupsandportobjectgroupshasoccurred.Individualaddressand
portobjectgroupscanberesetrespectivelywiththeobject-group address resetandobject-group
portresetcommands.
Examples
Resettingtheuserconfigurationforallobjecttypes(addressandport):
| switch(config)# | object-group | all | reset |     |
| --------------- | ------------ | --- | ----- | --- |
switch(config)#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| object-group | ip address |     |     |     |
| ------------ | ---------- | --- | --- | --- |
SyntaxtocreateanIPv4addressobjectgroupandenteritscontext:
AccessControlLists|72

| object-group |              | ip  | address    | <OBJECT-GROUP-NAME> |     |     |
| ------------ | ------------ | --- | ---------- | ------------------- | --- | --- |
| no           | object-group |     | ip address | <OBJECT-GROUP-NAME> |     |     |
Syntax(withintheaddressobject-groupcontext)forcreatingorremovingIPv4addressentries:
[<SEQUENCE-NUMBER>] <IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]
no <SEQUENCE-NUMBER>
Description
CreatesanIPv4addressobjectgroupcomprisedofoneormoreaddressentries.Addressgroupsare
usedsolelyasashorthandwayofspecifyinggroupsofaddressesintheACEsthatmakeupACLs.IPv4
addressgroupscanbeusedonlyintheaccess-list ipcommand.Enteringobject-group ip address
withanexistingaddressgroupname,enablesyoutomodifyanexistingaddressgroup.
Thenoformofthiscommanddeletestheentireaddressgroupordeletesaparticularaddressgroup
entryidentifiedbysequencenumber.
Parameter Description
<OBJECT-GROUP-NAME> Specifiestheaddressobjectgroupname.
<SEQUENCE-NUMBER> Specifiesasequencenumberfortheaddress
entry.Range:1to4294967295.Whenomitted,
asequencenumber10largerthanthecurrent
highestsequencenumberisauto-assigned.
Defaultauto-assignedsequencenumbersare
10,20,30,andsoon.
<IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}] SpecifiestheIPv4address.
n <IP-ADDRESS>-specifiestheIPv4host
address.
n <PREFIX-LENGTH>-specifiestheaddress
bitstomask(CIDRsubnetmasknotation).
Range:1to32.
n <SUBNET-MASK>-specifiestheaddressbits
tomask(dotteddecimalnotation).
Examples
CreatinganIPv4addressgroupwithtwoentries:
|     | switch(config)#              |      | object-group |              | ip address     | my_ipv4_addr_group |
| --- | ---------------------------- | ---- | ------------ | ------------ | -------------- | ------------------ |
|     | switch(config-addrgroup-ip)# |      |              |              | 10 192.168.0.1 |                    |
|     | switch(config-addrgroup-ip)# |      |              |              | 20 192.168.0.2 |                    |
|     | switch(config-addrgroup-ip)# |      |              |              | exit           |                    |
|     | switch(config)#              |      | show         | object-group |                |                    |
|     | Type                         | Name |              |              |                |                    |
|     | Sequence                     | L4   | Port(s)/IP   | Address      |                |                    |
-------------------------------------------------------------------------------
|     | IPv4 | my_ipv4_addr_group |     |     |     |     |
| --- | ---- | ------------------ | --- | --- | --- | --- |
|     |      | 10 192.168.0.1     |     |     |     |     |
|     |      | 20 192.168.0.2     |     |     |     |     |
AddinganentrytoanexistingIPv4addressgroup:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 73

switch(config)# object-group ip address my_ipv4_addr_group
switch(config-addrgroup-ip)# 30 192.168.0.3
switch(config-addrgroup-ip)# exit
switch(config)# show object-group
Type

Name

Sequence L4 Port(s)/IP Address

-------------------------------------------------------------------------------
IPv4

my_ipv4_addr_group

10 192.168.0.1
20 192.168.0.2
30 192.168.0.3

Removing an entry (20) from an existing IPv4 address group:

switch(config)# object-group ip address my_ipv4_addr_group
switch(config-addrgroup-ip)# no 20
switch(config-addrgroup-ip)# exit
switch(config)# show object-group
Type

Name

Sequence L4 Port(s)/IP Address

-------------------------------------------------------------------------------
IPv4

my_ipv4_addr_group

10 192.168.0.1
30 192.168.0.3

Removing an IPv4 address group:

switch(config)# no object-group ip address my_ipv4_addr_group
switch(config)# show object-group
No object group found.

Command History

Release

10.07 or earlier

Command Information

Modification

--

Platforms

Command context

Authority

Administrators or local user group members with execution
rights for this command.

All platforms

config
The object-group ip
address command takes
you into the named
address group context
(with prompt switch
(config-addrgroup-ip)#)
where you enter the
addresses.

object-group ipv6 address

Syntax to create an IPv6 address object group and enter its context:
object-group ipv6 address <OBJECT-GROUP-NAME>
no object-group ipv6 address <OBJECT-GROUP-NAME>

Access Control Lists | 74

Syntax(withintheaddressobject-groupcontext)forcreatingorremovingIPv6addressentries:
[<SEQUENCE-NUMBER>] <IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]
no <SEQUENCE-NUMBER>
Description
CreatesanIPv6addressobjectgroupcomprisedofoneormoreaddressentries.Addressgroupsare
usedsolelyasashorthandwayofspecifyinggroupsofaddressesintheACEsthatmakeupACLs.IPv6
addressgroupscanbeusedonlyintheaccess-list ipv6command.Enteringobject-group ipv6
addresswithanexistingaddressgroupname,enablesyoutomodifyanexistingaddressgroup.
Thenoformofthiscommanddeletestheentireaddressgroupordeletesaparticularaddressgroup
entryidentifiedbysequencenumber.
| Parameter           |     |     | Description                           |
| ------------------- | --- | --- | ------------------------------------- |
| <OBJECT-GROUP-NAME> |     |     | Specifiestheaddressobjectgroupname.   |
| <SEQUENCE-NUMBER>   |     |     | Specifiesasequencenumberfortheaddress |
entry.Range:1to4294967295.Whenomitted,
asequencenumber10largerthanthecurrent
highestsequencenumberisauto-assigned.
Defaultauto-assignedsequencenumbersare
10,20,30,andsoon.
<IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}] SpecifiestheIPv6address.
<IP-ADDRESS>-specifiestheIPv6host
n
address.
o <PREFIX-LENGTH>-specifiesthe
addressbitstomask(CIDRsubnetmask
notation).Range:1to128.
o <SUBNET-MASK>-specifiestheaddress
bitstomask(dotteddecimalnotation).
Examples
CreatinganIPv6addressgroupwithtwoentries:
| switch(config)#                | object-group      | ipv6 address | my_ipv6_addr_group |
| ------------------------------ | ----------------- | ------------ | ------------------ |
| switch(config-addrgroup-ipv6)# |                   | 10 1000::1   |                    |
| switch(config-addrgroup-ipv6)# |                   | 20 1000::2   |                    |
| switch(config-addrgroup-ipv6)# |                   | exit         |                    |
| switch(config)#                | show object-group |              |                    |
| Type                           | Name              |              |                    |
| Sequence                       | L4 Port(s)/IP     | Address      |                    |
-------------------------------------------------------------------------------
| IPv6 | my_ipv6_addr_group |     |     |
| ---- | ------------------ | --- | --- |
10 1000::1
20 1000::2
AddinganentrytoanexistingIPv6addressgroup:
| switch(config)# | object-group | ipv6 address | my_ipv6_addr_group |
| --------------- | ------------ | ------------ | ------------------ |
switch(config-addrgroup-ipv6)#
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 75

| switch(config-addrgroup-ipv6)# |     |     | 30 1000::3 |     |
| ------------------------------ | --- | --- | ---------- | --- |
switch(config-addrgroup-ipv6)#
exit
| switch(config)# | show          | object-group |     |     |
| --------------- | ------------- | ------------ | --- | --- |
| Type            | Name          |              |     |     |
| Sequence        | L4 Port(s)/IP | Address      |     |     |
-------------------------------------------------------------------------------
| IPv6 | my_ipv6_addr_group |     |     |     |
| ---- | ------------------ | --- | --- | --- |
10 1000::1
20 1000::2
30 1000::3
Removinganentry(20)fromanexistingIPv6addressgroup:
| switch(config)#                | object-group  |              | ipv6 address | my_ipv6_addr_group |
| ------------------------------ | ------------- | ------------ | ------------ | ------------------ |
| switch(config-addrgroup-ipv6)# |               |              | no 20        |                    |
| switch(config-addrgroup-ipv6)# |               |              | exit         |                    |
| switch(config)#                | show          | object-group |              |                    |
| Type                           | Name          |              |              |                    |
| Sequence                       | L4 Port(s)/IP | Address      |              |                    |
-------------------------------------------------------------------------------
| IPv6 | my_ipv6_addr_group |     |     |     |
| ---- | ------------------ | --- | --- | --- |
10 1000::1
30 1000::3
RemovinganIPv6addressgroup:
switch(config)# no object-group ipv6 address my_ipv6_addr_group
| switch(config)#     | show         | object-group |              |     |
| ------------------- | ------------ | ------------ | ------------ | --- |
| No object           | group found. |              |              |     |
| Command History     |              |              |              |     |
| Release             |              |              | Modification |     |
| 10.07orearlier      |              |              | --           |     |
| Command Information |              |              |              |     |
| Platforms           | Command      | context      | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|     | Theobject-groupipv6 |     | rightsforthiscommand. |     |
| --- | ------------------- | --- | --------------------- | --- |
addresscommandtakes
youintothenamed
addressgroupcontext
(withpromptswitch
(config-addrgroup-
ipv6)#)whereyouenter
theaddresses.
| object-group | port |     |     |     |
| ------------ | ---- | --- | --- | --- |
SyntaxtocreateaLayer4portobjectgroupandenteritscontext:
| object-group    | port <OBJECT-GROUP-NAME> |     |     |     |
| --------------- | ------------------------ | --- | --- | --- |
| no object-group | port <OBJECT-GROUP-NAME> |     |     |     |
AccessControlLists|76

Syntax (within the port object-group context) for creating or removing Layer 4 port entries:

[<SEQUENCE-NUMBER>] { {eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT> }

no <SEQUENCE-NUMBER>

Description

Creates a Layer 4 port object group comprised of one or more port entries. Port groups are used solely
as a shorthand way of specifying groups of ports in the ACEs that make up ACLs. Layer 4 port groups
can be used only in the access-list ip and access-list ipv6 commands. Entering object-group port with
an existing port group name, enables you to modify an existing port group.

The no form of this command deletes the entire port group or deletes a particular port group entry
identified by sequence number.

Parameter

<OBJECT-GROUP-NAME>

<SEQUENCE-NUMBER>

{ {eq|gt|lt} <PORT>|range <MIN-PORT><MAX-PORT> }

Description

Specifies the port object group name.

Specifies a sequence number for the port
entry. Range: 1 to 4294967295. When
omitted, a sequence number 10 larger than
the current highest sequence number is
auto-assigned. Default auto-assigned
sequence numbers are 10, 20, 30, and so on.

Specifies the port or port range. Port
numbers are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.
n gt <PORT> - specifies any Layer 4 port

greater than the indicated port.

n lt <PORT> - specifies any Layer 4 port less

than the indicated port.

n range MIN-PORT> <MAX-PORT> -

specifies the Layer 4 port range.

NOTE:
When ACLs using ACEs defined with
port groups are applied, the same
number of hardware resources are
consumed as when the ports are
specified directly in the ACEs and not in
a group. Keep this in mind when
creating port groups that include many
ports. Although hardware resource
consumption is the same, with or
without port groups used, it may not be
immediately obvious that some port
groups that you have defined, include
many ports. It is recommended that you
name port groups in a manner that
reminds you that a group includes
many ports.

Examples

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

77

Creatingaportgroupwithtwoentriestocoverport80plusports0through50:
| switch(config)#           | object-group      |         | port my_port_group |
| ------------------------- | ----------------- | ------- | ------------------ |
| switch(config-portgroup)# |                   | 10      | eq 80              |
| switch(config-portgroup)# |                   | 20      | range 0 50         |
| switch(config-portgroup)# |                   | exit    |                    |
| switch(config)#           | show object-group |         |                    |
| Type                      | Name              |         |                    |
| Sequence                  | L4 Port(s)/IP     | Address |                    |
-------------------------------------------------------------------------------
| Port | my_port_group |     |     |
| ---- | ------------- | --- | --- |
10 eq 80
20 range 0 50
Addinganentryforportsgreaterthan65525(coversports65526through65535):
| switch(config)#           | object-group |      | port my_port_group |
| ------------------------- | ------------ | ---- | ------------------ |
| switch(config-portgroup)# |              | 30   | gt 65525           |
| switch(config-portgroup)# |              | exit |                    |
switch(config)#
show object-group
| Type     | Name          |         |     |
| -------- | ------------- | ------- | --- |
| Sequence | L4 Port(s)/IP | Address |     |
-------------------------------------------------------------------------------
| Port | my_port_group |     |     |
| ---- | ------------- | --- | --- |
10 eq 80
20 range 0 50
30 gt 65525
Removinganentry(#20)fromtheportgroup:
switch(config)#
|                           | object-group      |         | port my_port_group |
| ------------------------- | ----------------- | ------- | ------------------ |
| switch(config-portgroup)# |                   | no      | 20                 |
| switch(config-portgroup)# |                   | exit    |                    |
| switch(config)#           | show object-group |         |                    |
| Type                      | Name              |         |                    |
| Sequence                  | L4 Port(s)/IP     | Address |                    |
-------------------------------------------------------------------------------
| Port | my_port_group |     |     |
| ---- | ------------- | --- | --- |
10 eq 80
30 gt 65525
Removingtheportgroup:
| switch(config)#     | no object-group   |     | port my_port_group |
| ------------------- | ----------------- | --- | ------------------ |
| switch(config)#     | show object-group |     |                    |
| No object group     | found.            |     |                    |
| Command History     |                   |     |                    |
| Release             |                   |     | Modification       |
| 10.07orearlier      |                   |     | --                 |
| Command Information |                   |     |                    |
AccessControlLists|78

| Platforms | Command | context | Authority |
| --------- | ------- | ------- | --------- |
Allplatforms config Administratorsorlocalusergroupmemberswithexecutionrights
|     | Theobject-groupip |     | forthiscommand. |
| --- | ----------------- | --- | --------------- |
portcommandtakesyou
intothenamedport
groupcontext(with
promptswitch(config-
portgroup)#)whereyou
specifytheports.
| object-group | port | resequence |     |
| ------------ | ---- | ---------- | --- |
object-group port <OBJECT-GROUP-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT>
Description
Reordersthesequencenumbersinaportobjectgroup.
| Parameter           |     |     | Description                      |
| ------------------- | --- | --- | -------------------------------- |
| <OBJECT-GROUP-NAME> |     |     | Specifiestheportobjectgroupname. |
<STARTING-SEQUENCE-NUMBER> Specifiesthestartingsequencenumber.
| <INCREMENT> |     |     | Specifiesthesequencenumberincrement. |
| ----------- | --- | --- | ------------------------------------ |
Examples
Resequencingportobjectgroupmy_port_grouptousesequencenumbers110,120,130andsoon:
switch(config)# object-group port my_port_group resequence 110 10
switch(config)#
| Command        | History     |         |              |
| -------------- | ----------- | ------- | ------------ |
| Release        |             |         | Modification |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| object-group | port                     | reset |       |
| ------------ | ------------------------ | ----- | ----- |
| object-group | port <OBJECT-GROUP-NAME> |       | reset |
Description
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 79

Resetstheuserconfigurationbacktotheactiveconfiguration.Thiscommandtakesimmediateeffect,it
isnotsavedintheuserconfiguration.Usethiscommandifmisconfigurationofaportobjectgrouphas
occurred.
| Parameter           |     |     | Description                      |     |
| ------------------- | --- | --- | -------------------------------- | --- |
| <OBJECT-GROUP-NAME> |     |     | Specifiestheportobjectgroupname. |     |
Examples
Resettingportobjectgroupmy_port_group:
| switch(config)# | object-group | port | my_port_group | reset |
| --------------- | ------------ | ---- | ------------- | ----- |
switch(config)#
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show access-list
SyntaxthatfiltersbyACLsappliedtoaninterface,VLAN,orVNI:
show access-list [interface <IF-NAME>|vlan <VLAN-ID>|vni <VNI-ID>]
[in|out|routed-in|routed-out][ip|ipv6|mac] [<acl-name>][commands] [configuration]
SyntaxthatfiltersbythenamedACL:
show access-list [ip|ipv6|mac] [<ACL-NAME>] [commands] [configuration] [vsx-peer]
Description
ShowsinformationaboutyourdefinedACLsandwheretheyhavebeenapplied.Whenshow access-list
isenteredwithoutparameters,informationforallACLsisshown.TheparametersfilterthelistofACLs
forwhichinformationisshown.
Availablefilteringincludes:
n ThecontentofaspecificACL.
n AllACLsofaspecifictype.
n TheACLappliedinaparticulardirection.
n TheACLappliedtoaspecificinterface(portorsplitportorLAG).
n TheACLappliedtoaspecificVLAN.
n TheACLappliedtospecificinterfaceVLAN(routed-inorrouted-out).
n Thecontrol-planeACLappliedtoaspecificVRF.
AccessControlLists|80

| Parameter      |           |     | Description                           |     |
| -------------- | --------- | --- | ------------------------------------- | --- |
| interface      | <IF-NAME> |     | Specifiestheinterfacename(portorLAG). |     |
| vlan <VLAN-ID> |           |     | SpecifiestheVLAN.                     |     |
| ip|ipv6|mac    |           |     | SpecifiestheACLtype:                  |     |
n ipforIPv4,
ipv6forIPv6,or
n
n macforMAC.
| in  |     |     | Selectstheinbound(ingress)trafficdirection. |     |
| --- | --- | --- | ------------------------------------------- | --- |
out Selectstheoutbound(egress)trafficdirection.AvailableforIPv4
andIPv6ACLsappliedtoVLANsandforIPv4ACLsappliedto
route-onlyports.NotavailableforACLsappliedtoeitherIPv4
bridgedportsorIPv6ports,orforMACACLsappliedtoportsor
VLANS.
routed-in
Selectstheroutedinbound(routedingress)trafficdirection.
NOTE: ThisisonlyavailableforIPv4andIPv6ACLsappliedto
interfaceVLANs.
routed-out
Selectstheroutedoutbound(routedegress)trafficdirection.
NOTE: ThisisonlyavailableforIPv4andIPv6ACLsappliedto
interfaceVLANs.
<ACL-NAME>
SpecifiestheACLname.
commands SpecifiesthattheACLdefinitionistobeshownasthecommands
andparametersusedtocreateitratherthanintabularform.
configuration Specifiesthattheuser-configuredACLsbeshownasentered,
eveniftheACLsarenotactiveduetoACE-definitioncommand
issuesorhardwareissues.Thisparameterisusefulifthereisa
mismatchbetweentheenteredconfigurationandtheprevious
successfullyprogrammed(active)ACLsconfiguration.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
CreatinganIPv4ACL,applyingittoaninterfaceVLAN(routedin),andthenshowingACLinformation
filteredforthatinterfaceVAN:
| switch(config)#        |     | access-list | ip test            |               |
| ---------------------- | --- | ----------- | ------------------ | ------------- |
| switch(config-acl-ip)# |     | 10          | permit any 1.1.1.2 | 2.2.2.2 count |
| switch(config-acl-ip)# |     | 20          | permit any 1.1.1.2 | 2.2.2.1 count |
| switch(config-acl-ip)# |     | 30          | permit any 2.2.2.2 | 1.1.1.2 count |
| switch(config-acl-ip)# |     | 40          | permit any 2.2.2.2 | 1.1.1.1 count |
| switch(config-acl-ip)# |     | 50          | permit any any any | count         |
| switch(config-acl-ip)# |     | exit        |                    |               |
switch(config)#
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 81

| switch(config)# | interface | vlan100 |     |     |
| --------------- | --------- | ------- | --- | --- |
switch(config-if-vlan)#
|                         |     | apply access-list | ip test | routed-in |
| ----------------------- | --- | ----------------- | ------- | --------- |
| switch(config-if-vlan)# |     | exit              |         |           |
switch(config)# show access-list interface vlan100 ip routed-in
Direction
| Type     | Name    |     |     |     |
| -------- | ------- | --- | --- | --- |
| Sequence | Comment |     |     |     |
Ac L3 Protocol
|     | Source      | IP Address | Source      | L4 Port(s) |
| --- | ----------- | ---------- | ----------- | ---------- |
|     | Destination | IP Address | Destination | L4 Port(s) |
|     | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
Routed Inbound
| IPv4 | test |     |     |     |
| ---- | ---- | --- | --- | --- |
10
|     | permit |     | any |     |
| --- | ------ | --- | --- | --- |
1.1.1.2
2.2.2.2
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
20
|     | permit |     | any |     |
| --- | ------ | --- | --- | --- |
1.1.1.2
2.2.2.1
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
30
|     | permit |     | any |     |
| --- | ------ | --- | --- | --- |
2.2.2.2
1.1.1.2
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
40
|     | permit |     | any |     |
| --- | ------ | --- | --- | --- |
2.2.2.2
1.1.1.1
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
50
|     | permit |     | any |     |
| --- | ------ | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |
| --- | ----------- | ------- | --- | --- |
-------------------------------------------------------------------------------
ShowinganIPv4ACL:
| switch#  | show access-list | ip MY_ACL  |             |            |
| -------- | ---------------- | ---------- | ----------- | ---------- |
| Type     | Name             |            |             |            |
| Sequence | Comment          |            |             |            |
|          | Action           |            | L3 Protocol |            |
|          | Source           | IP Address | Source      | L4 Port(s) |
|          | Destination      | IP Address | Destination | L4 Port(s) |
|          | Additional       | Parameters |             |            |
------------------------------------------------------------------------------
| IPv4 | MY_ACL    |     |     |     |
| ---- | --------- | --- | --- | --- |
|      | 10 permit |     | udp |     |
any
172.16.1.0/255.255.255.0
|     | 20 permit              |     | tcp    |     |
| --- | ---------------------- | --- | ------ | --- |
|     | 172.16.2.0/255.255.0.0 |     | > 1023 |     |
any
|     | 30 permit |     | tcp |     |
| --- | --------- | --- | --- | --- |
172.26.1.0//255.255.255.0
AccessControlLists|82

any
syn
ack
|     |     | dscp 10 |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- |
|     | 40  | deny    |     |     | any |     |     |
any
any
|     |     | Hit-counts: | enabled |     |     |     |     |
| --- | --- | ----------- | ------- | --- | --- | --- | --- |
------------------------------------------------------------------------------
ShowinganIPv4ACLascommands:
switch#
|             | show   | access-list | ip MY_ACL                    | commands |     |          |             |
| ----------- | ------ | ----------- | ---------------------------- | -------- | --- | -------- | ----------- |
| access-list |        | ip MY_ACL   |                              |          |     |          |             |
| 10          | permit | udp         | any 172.16.1.0/255.255.255.0 |          |     |          |             |
| 20          | permit | tcp         | 172.16.2.0/255.255.0.0       |          | gt  | 1023 any |             |
| 30          | permit | tcp         | 172.26.1.0/255.255.255.0     |          | any | syn      | ack dscp 10 |
| 40          | deny   | any any     | any count                    |          |     |          |             |
ShowingIPv4ACLsappliedtoVLAN10,inbound:
| switch#  | show | access-list | vlan 10    | ip in |             |          |            |
| -------- | ---- | ----------- | ---------- | ----- | ----------- | -------- | ---------- |
| Type     |      | Name        |            |       |             |          |            |
| Sequence |      | Comment     |            |       |             |          |            |
|          |      | Action      |            |       | L3          | Protocol |            |
|          |      | Source      | IP Address |       | Source      |          | L4 Port(s) |
|          |      | Destination | IP Address |       | Destination |          | L4 Port(s) |
|          |      | Additional  | Parameters |       |             |          |            |
------------------------------------------------------------------------------
| IPv4 |     | My_ip_ACL |     |     |     |     |     |
| ---- | --- | --------- | --- | --- | --- | --- | --- |
|      | 10  | permit    |     |     | udp |     |     |
any
172.16.1.0/255.255.255.0
|     | 20  | permit                 |     |     | tcp |      |     |
| --- | --- | ---------------------- | --- | --- | --- | ---- | --- |
|     |     | 172.16.2.0/255.255.0.0 |     |     | >   | 1023 |     |
any
|     | 30  | permit |     |     | tcp |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- |
172.26.1.0//255.255.255.0
any
syn
ack
|     |     | dscp 10 |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- |
|     | 40  | deny    |     |     | any |     |     |
any
any
|     |     | Hit-counts: | enabled |     |     |     |     |
| --- | --- | ----------- | ------- | --- | --- | --- | --- |
------------------------------------------------------------------------------
ShowingIPv6ACLsappliedtoLAG128,inbound:
| switch#  | show | access-list | interface  | lag128 | ipv6        | in       |            |
| -------- | ---- | ----------- | ---------- | ------ | ----------- | -------- | ---------- |
| Type     |      | Name        |            |        |             |          |            |
| Sequence |      | Comment     |            |        |             |          |            |
|          |      | Action      |            |        | L3          | Protocol |            |
|          |      | Source      | IP Address |        | Source      |          | L4 Port(s) |
|          |      | Destination | IP Address |        | Destination |          | L4 Port(s) |
|          |      | Additional  | Parameters |        |             |          |            |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 83

------------------------------------------------------------------------------
| IPv6 | MY_IPV6_ACL |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
|      | 10 permit   |     |     |     | udp |
any
2001::1/64
|     | 20 permit          |     |     |     | tcp    |
| --- | ------------------ | --- | --- | --- | ------ |
|     | 2001:2001::2:1/128 |     |     |     | > 1023 |
any
|     | 30 permit |     |     |     | tcp |
| --- | --------- | --- | --- | --- | --- |
2001:2011::1/64
|     | 40 deny |     |     |     | any |
| --- | ------- | --- | --- | --- | --- |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
------------------------------------------------------------------------------
ShowinganIPv6ACLascommands:
| switch#     | show access-list       | ipv6       | MY_IPV6_ACL |     | commands |
| ----------- | ---------------------- | ---------- | ----------- | --- | -------- |
| access-list | ipv6 MY_IPV6_ACL       |            |             |     |          |
| 10 permit   | udp any                | 2001::1/64 |             |     |          |
| 20 permit   | tcp 2001:2001::2:1/128 |            |             | gt  | 1023 any |
| 40 deny     | any any any            | count      |             |     |          |
ShowingaMACACL:
| switch#  | show access-list | mac        | MY_MAC_ACL |     |           |
| -------- | ---------------- | ---------- | ---------- | --- | --------- |
| Type     | Name             |            |            |     |           |
| Sequence | Comment          |            |            |     |           |
|          | Action           |            |            |     | EtherType |
|          | Source MAC       | Address    |            |     |           |
|          | Destination      | MAC        | Address    |     |           |
|          | Additional       | Parameters |            |     |           |
------------------------------------------------------------------------------
| MAC | MY_MAC_ACL |     |     |     |      |
| --- | ---------- | --- | --- | --- | ---- |
|     | 10 permit  |     |     |     | ipv6 |
1122.3344.5566/ffff.ffff.0000
any
|     | 20 permit |     |     |     | any |
| --- | --------- | --- | --- | --- | --- |
aaaa.bbbb.cccc
1111.2222.3333
|     | QoS Priority | Code | Point: | 4   |     |
| --- | ------------ | ---- | ------ | --- | --- |
|     | 30 deny      |      |        |     | any |
any
any
|     | Hit-counts: | enabled |     |     |     |
| --- | ----------- | ------- | --- | --- | --- |
------------------------------------------------------------------------------
ShowingaMACACLascommands:
| switch#     | show access-list              | mac   | MY_MAC_ACL     |     | commands  |
| ----------- | ----------------------------- | ----- | -------------- | --- | --------- |
| access-list | mac MY_MAC_ACL                |       |                |     |           |
| 10 permit   | 1122.3344.5566/ffff.ffff.0000 |       |                |     | any ipv6  |
| 20 permit   | aaaa.bbbb.cccc                |       | 1111.2222.3333 |     | any pcp 4 |
| 30 deny     | any any any                   | count |                |     |           |
| Command     | History                       |       |                |     |           |
AccessControlLists|84

| Release             |                      |         | Modification |
| ------------------- | -------------------- | ------- | ------------ |
| 10.07orearlier      |                      |         | --           |
| Command Information |                      |         |              |
| Platforms           | Command              | context | Authority    |
| Allplatforms        | Operator(>)orManager |         |              |
(#)
| show access-list | control-plane |     |     |
| ---------------- | ------------- | --- | --- |
show access-list [ip|ipv6] [<ACL-NAME>] control-plane [vrf <VRF-NAME>]
|     | [commands] | [configuration][vsx-peer] |     |
| --- | ---------- | ------------------------- | --- |
Description
ShowsinformationaboutyourdefinedACLsthathavebeenappliedtotheControlPlane.Whenshow
access-list control-planeisenteredwithoutparameters,informationforallACLsappliedtotheControl
Planeisshown.TheparametersfilterthelistofACLsforwhichinformationisshown.
Availablefilteringincludes:
n ThecontentofaspecificACLthathasbeenappliedtotheControlPlane.
n AllACLsofaspecifictypethathavebeenappliedtotheControlPlane.
n AllACLsappliedtotheControlPlaneforaspecificVRF.
| Parameter |     |     | Description                                  |
| --------- | --- | --- | -------------------------------------------- |
| ip|ipv6   |     |     | SpecifiestheACLtype:ipforIPv4,oripv6forIPv6. |
<ACL-NAME>
SpecifiestheACLname.
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname. |
| -------------- | --- | --- | -------------------- |
[commands]
SpecifiesthattheACLdefinitionistobeshownasthecommands
andparametersusedtocreateitratherthanintabularform.
[configuration] Specifiesthattheuser-configuredACLsbeshownasentered,
eveniftheACLsarenotactiveduetoACE-definitioncommand
issuesorhardwareissues.Thisparameterisusefulifthereisa
mismatchbetweentheenteredconfigurationandtheprevious
successfullyprogrammed(active)ACLsconfiguration.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
ShowinganIPv4ACLappliedtotheControlPlanedefaultVRF:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 85

switch# show access-list ip My_ipv4_ACL control-plane vrf default
Type Name
Sequence Comment
| Action      |            | L3 Protocol |            |
| ----------- | ---------- | ----------- | ---------- |
| Source      | IP Address | Source      | L4 Port(s) |
| Destination | IP Address | Destination | L4 Port(s) |
| Additional  | Parameters |             |            |
------------------------------------------------------------------------------
IPv4 My_ipv4_ACL
| 10 permit |     | udp |     |
| --------- | --- | --- | --- |
any
172.16.1.0/24
| 20 permit     |     | tcp    |     |
| ------------- | --- | ------ | --- |
| 172.16.2.0/16 |     | > 1023 |     |
any
| 30 permit |     | tcp |     |
| --------- | --- | --- | --- |
172.26.1.0/24
any
syn
ack
dscp 10
| 40 deny |     | any |     |
| ------- | --- | --- | --- |
any
any
| Hit-counts: | enabled |     |     |
| ----------- | ------- | --- | --- |
------------------------------------------------------------------------------
ShowinganIPv6ACLappliedtotheControlPlanedefaultVRF:
switch# show access-list ipv6 My_ipv6_ACL control-plane vrf default
Type Name
Sequence Comment
| Action      |            | L3 Protocol |            |
| ----------- | ---------- | ----------- | ---------- |
| Source      | IP Address | Source      | L4 Port(s) |
| Destination | IP Address | Destination | L4 Port(s) |
| Additional  | Parameters |             |            |
------------------------------------------------------------------------------
IPv6 My_ipv6_ACL
| 10 permit |     | udp |     |
| --------- | --- | --- | --- |
any
2001::1/64
| 20 permit          |     | tcp    |     |
| ------------------ | --- | ------ | --- |
| 2001:2001::2:1/128 |     | > 1023 |     |
any
| 30 permit |     | tcp |     |
| --------- | --- | --- | --- |
2001:2011::1/64
| 40 deny |     | any |     |
| ------- | --- | --- | --- |
any
any
| Hit-counts: | enabled |     |     |
| ----------- | ------- | --- | --- |
------------------------------------------------------------------------------
Command History
Release Modification
10.07orearlier --
Command Information
AccessControlLists|86

Platforms

Command context

Authority

All platforms

Operator (>) or Manager
(#)

show access-list hitcounts
show access-list hitcounts { [{ip|ipv6|mac} <ACL-NAME>] [interface <IF-NAME> |

vlan <VLAN-ID> | vni <VNI-ID>] [in|out|routed-in|routed-out] [vsx-peer]

}

Description

Shows the hit count of the number of times an ACL has matched a packet or frame for ACEs with the
count keyword. For ACEs without the count keyword, a dash is shown in place of a hit count.

Parameter

ip|ipv6|mac

<ACL-NAME>

Description

Specifies the ACL type: ip for IPv4, ipv6 for IPv6, or mac for MAC.

Specifies the ACL name.

interface <IF-NAME>

Specifies the interface name (port or split port or LAG).

vlan <VLAN-ID>

Specifies the VLAN.

vni <VNI-ID>

Specifies the ID of the VNI.

in

out

routed-in

routed-out

vsx-peer

Usage

Selects the inbound (ingress) traffic direction.

Selects the outbound (egress) traffic direction. Available for IPv4
and IPv6 ACLs applied to VLANs and for IPv4 ACLs applied to
route-only ports. Not available for ACLs applied to either IPv4
bridged ports or IPv6 ports, or for MAC ACLs applied to ports or
VLANS.

Selects the routed inbound (routed ingress) traffic direction.

Selects the routed outbound (routed egress) traffic direction.

Shows the output from the VSX peer switch. If the switches do not
have the VSX configuration or the ISL is down, the output from the
VSX peer switch is not displayed. This parameter is available on
switches that support VSX.

n ACL hit counts are aggregated across all:

o Physical interfaces to which the ACL is applied to on ingress.

o Physical interfaces to which the ACL is applied to on egress.

o VLANs to which the ACL is applied to on ingress.

o VLANs to which the ACL is applied to on egress.

o Interface VLANs to which the IPv4 or IPv6 ACL is applied on routed ingress.

o Interface VLANs to which the IPv4 or IPv6 ACL is applied on routed egress.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

87

n IfanACLwithanACEwiththecountkeywordisappliedtomultiplephysicalinterfacesorVLANs,the
hitcountsareaggregated.ThereisoneaggregationforphysicalinterfacesandanotherforVLANs.
n AccumulatedhitcountsforanappliedACLarecleareduponanymodificationoftheACL.
Examples
ShowingthehitcountsforMy_ip_ACLappliedtoport1/1/2:
switch# show access-list hitcounts ip My_ip_ACL interface 1/1/2
| Statistics | for ACL          | My_ip_ACL |               | (ipv4):                          |     |             |       |
| ---------- | ---------------- | --------- | ------------- | -------------------------------- | --- | ----------- | ----- |
| interface  | 1/1/1-1/1/2,lag1 |           | (out):        |                                  |     |             |       |
| Matched    | Packets          |           | Configuration |                                  |     |             |       |
|            |                  | -         | 10 permit     | udp any 172.16.1.0/255.255.255.0 |     |             |       |
|            |                  | 0         | 20 permit     | tcp 172.16.2.0/255.255.0.0       |     | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|     |     | 0   | implicit | deny any any | any count |     |     |
| --- | --- | --- | -------- | ------------ | --------- | --- | --- |
ShowingthehitcountsforMy_ip_ACLappliedtoVLAN10:
| switch#            | show access-list |           | hitcounts     | ip My_ip_ACL                     | vlan 10 |             |       |
| ------------------ | ---------------- | --------- | ------------- | -------------------------------- | ------- | ----------- | ----- |
| Statistics         | for ACL          | My_ip_ACL |               | (ipv4):                          |         |             |       |
| vlan 10,20-100,300 |                  | (in):     |               |                                  |         |             |       |
| Matched            | Packets          |           | Configuration |                                  |         |             |       |
|                    |                  | -         | 10 permit     | udp any 172.16.1.0/255.255.255.0 |         |             |       |
|                    |                  | 0         | 20 permit     | tcp 172.16.2.0/255.255.0.0       |         | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|     |     | 0   | implicit | deny any any | any count |     |     |
| --- | --- | --- | -------- | ------------ | --------- | --- | --- |
ShowingthehitcountsforMy_ip_ACLappliedtointerfaceVLAN10:
| switch#    | show access-list |           | hitcounts     | ip My_ip_ACL                     | vlan 10 |             |       |
| ---------- | ---------------- | --------- | ------------- | -------------------------------- | ------- | ----------- | ----- |
| Statistics | for ACL          | My_ip_ACL |               | (ipv4):                          |         |             |       |
| interface  | vlan 10,20,30    |           | (routed-in):  |                                  |         |             |       |
| Matched    | Packets          |           | Configuration |                                  |         |             |       |
|            |                  | -         | 10 permit     | udp any 172.16.1.0/255.255.255.0 |         |             |       |
|            |                  | 0         | 20 permit     | tcp 172.16.2.0/255.255.0.0       |         | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|     |     | 0   | implicit | deny any any | any count |     |     |
| --- | --- | --- | -------- | ------------ | --------- | --- | --- |
ShowingthehitcountsforMy_ip_ACLappliedonanyinterfaceanddirection:
| switch#    | show access-list |           | hitcounts     | ip My_ip_ACL                     | vlan 10 |             |       |
| ---------- | ---------------- | --------- | ------------- | -------------------------------- | ------- | ----------- | ----- |
| switch#    | show access-list |           | hitcounts     | ip My_ip_ACL                     |         |             |       |
| Statistics | for ACL          | My_ip_ACL |               | (ipv4):                          |         |             |       |
| interface  | 1/1/1            | (in):     |               |                                  |         |             |       |
| Matched    | Packets          |           | Configuration |                                  |         |             |       |
|            |                  | -         | 10 permit     | udp any 172.16.1.0/255.255.255.0 |         |             |       |
|            |                  | 0         | 20 permit     | tcp 172.16.2.0/255.255.0.0       |         | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|           |                  | 0   | implicit      | deny any any                     | any count |             |       |
| --------- | ---------------- | --- | ------------- | -------------------------------- | --------- | ----------- | ----- |
| interface | 1/1/1-1/1/2,lag1 |     | (out):        |                                  |           |             |       |
| Matched   | Packets          |     | Configuration |                                  |           |             |       |
|           |                  | -   | 10 permit     | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|           |                  | 0   | 20 permit     | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
AccessControlLists|88

|           |                   | 0 implicit    | deny any any                     | any count |             |       |
| --------- | ----------------- | ------------- | -------------------------------- | --------- | ----------- | ----- |
| interface | 1/1/4.1,1/1/10.10 |               | (in):                            |           |             |       |
| Matched   | Packets           | Configuration |                                  |           |             |       |
|           |                   | - 10 permit   | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|           |                   | 0 20 permit   | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|           |         | 0 implicit    | deny any any                     | any count |             |       |
| --------- | ------- | ------------- | -------------------------------- | --------- | ----------- | ----- |
| interface | 1/1/4.1 | (out):        |                                  |           |             |       |
| Matched   | Packets | Configuration |                                  |           |             |       |
|           |         | - 10 permit   | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|           |         | 0 20 permit   | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|           |               | 0 implicit    | deny any any                     | any count |             |       |
| --------- | ------------- | ------------- | -------------------------------- | --------- | ----------- | ----- |
| interface | vlan 10,20,30 | (routed-in):  |                                  |           |             |       |
| Matched   | Packets       | Configuration |                                  |           |             |       |
|           |               | - 10 permit   | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|           |               | 0 20 permit   | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|           |            | 0 implicit    | deny any any                     | any count |             |       |
| --------- | ---------- | ------------- | -------------------------------- | --------- | ----------- | ----- |
| interface | vlan 80-85 | (routed-out): |                                  |           |             |       |
| Matched   | Packets    | Configuration |                                  |           |             |       |
|           |            | - 10 permit   | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|           |            | 0 20 permit   | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|                    |         | 0 implicit    | deny any any                     | any count |             |       |
| ------------------ | ------- | ------------- | -------------------------------- | --------- | ----------- | ----- |
| vlan 10,20-100,300 |         | (in):         |                                  |           |             |       |
| Matched            | Packets | Configuration |                                  |           |             |       |
|                    |         | - 10 permit   | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|                    |         | 0 20 permit   | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|          |         | 0 implicit    | deny any any                     | any count |             |       |
| -------- | ------- | ------------- | -------------------------------- | --------- | ----------- | ----- |
| vlan 2-5 | (out):  |               |                                  |           |             |       |
| Matched  | Packets | Configuration |                                  |           |             |       |
|          |         | - 10 permit   | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|          |         | 0 20 permit   | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|                      |         | 0 implicit       | deny any any                     | any count |             |       |
| -------------------- | ------- | ---------------- | -------------------------------- | --------- | ----------- | ----- |
| vrf blue,default,red |         | (control-plane): |                                  |           |             |       |
| Matched              | Packets | Configuration    |                                  |           |             |       |
|                      |         | - 10 permit      | udp any 172.16.1.0/255.255.255.0 |           |             |       |
|                      |         | 0 20 permit      | tcp 172.16.2.0/255.255.0.0       |           | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|         |         | 0 implicit | deny any any                                    | any count |     |     |
| ------- | ------- | ---------- | ----------------------------------------------- | --------- | --- | --- |
| Command | History |            |                                                 |           |     |     |
| Release |         |            | Modification                                    |           |     |     |
| 10.16   |         |            | AddedsupportforL3VNIACLsonthe8325and10000switch |           |     |     |
series.
10.07orearlier UpdatedcommandoutputtouseinterfaceandVLANrangesto
reflectaggregation.
| Command | Information |     |     |     |     |     |
| ------- | ----------- | --- | --- | --- | --- | --- |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 89

| Platforms    | Command              | context | Authority |     |     |     |
| ------------ | -------------------- | ------- | --------- | --- | --- | --- |
| Allplatforms | Operator(>)orManager |         |           |     |     |     |
(#)
| show access-list | hitcounts |     | control-plane |     |     |     |
| ---------------- | --------- | --- | ------------- | --- | --- | --- |
show access-list hitcounts [{ip|ipv6} <ACL-NAME>] control-plane vrf <VRF-NAME> [vsx-peer]
Description
ShowsthehitcountofthenumberoftimesanACL(appliedtotheControlPlane)hasmatchedapacket
forACEswiththecountkeyword.ForACEswithoutthecountkeyword,adashisshowninplaceofahit
count.
| Parameter |     |     | Description                                  |     |     |     |
| --------- | --- | --- | -------------------------------------------- | --- | --- | --- |
| ip|ipv6   |     |     | SpecifiestheACLtype:ipforIPv4,oripv6forIPv6. |     |     |     |
<ACL-NAME>
SpecifiestheACLname.
| vrf <VRF-NAME> |     |     | SpecifiestheVRFname. |     |     |     |
| -------------- | --- | --- | -------------------- | --- | --- | --- |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
n ACLhitcountsareaggregatedacrossallVRFstowhichtheACLisappliedtooningress.
n AccumulatedhitcountsforanappliedACLarecleareduponanymodificationoftheACL.
Examples
ShowingthehitcountsforanIPv4ACLappliedtotheControlPlanedefaultVRF:
switch# show access-list hitcounts ip My_ipv4_ACL control-plane vrf default
| Statistics  | for ACL          | My_ip_ACL     | (ipv4):                          |     |             |       |
| ----------- | ---------------- | ------------- | -------------------------------- | --- | ----------- | ----- |
| vrf default | (control-plane): |               |                                  |     |             |       |
| Matched     | Packets          | Configuration |                                  |     |             |       |
|             |                  | - 10 permit   | udp any 172.16.1.0/255.255.255.0 |     |             |       |
|             |                  | 0 20 permit   | tcp 172.16.2.0/255.255.0.0       |     | gt 1023 any | count |
- 30 permit tcp 172.26.1.0/255.255.255.0 any dscp AF11 ack syn
|                |             | 0 implicit | deny any any | any count |     |     |
| -------------- | ----------- | ---------- | ------------ | --------- | --- | --- |
| Command        | History     |            |              |           |     |     |
| Release        |             |            | Modification |           |     |     |
| 10.07orearlier |             |            | --           |           |     |     |
| Command        | Information |            |              |           |     |     |
AccessControlLists|90

| Platforms    | Command              | context | Authority |
| ------------ | -------------------- | ------- | --------- |
| Allplatforms | Operator(>)orManager |         |           |
(#)
| show access-list | secure-update |     |     |
| ---------------- | ------------- | --- | --- |
| show access-list | secure-update |     |     |
Description
Usethiscommandtodetermineifaccesslistsareupdatedusingthesecure-updatefeature.Secure
updateisenabledbydefault.
Examples
Displayingthestatusoftheaccesslistsecure-updatefeaturewhenthatfeatureisenabled:
| switch(config)# | show          | access-list | secure-update |
| --------------- | ------------- | ----------- | ------------- |
| Access-list     | secure-update | is enabled  |               |
Displayingthestatusoftheaccesslistsecure-updatefeaturewhenthatfeatureisdisabled:
| switch(config)#  | show          | access-list | secure-update |
| ---------------- | ------------- | ----------- | ------------- |
| Access-list      | secure-update | is disabled |               |
| Related Commands |               |             |               |
Command Description
| access-list | secure-update |     |     |
| ----------- | ------------- | --- | --- |
Thiscommanddeterminesifaccesslistsareupdated
usingthesecure-updatefeature.Secure-updateis
enabledbydefault.
| Command History     |         |         |                   |
| ------------------- | ------- | ------- | ----------------- |
| Release             |         |         | Modification      |
| 10.13               |         |         | Commandintroduced |
| Command Information |         |         |                   |
| Platforms           | Command | context | Authority         |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show capacities
| show capacities | <FEATURE> | [vsx-peer] |     |
| --------------- | --------- | ---------- | --- |
Description
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 91

Showssystemcapacitiesandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     | Description                             |     |     |
| --------- | --- | --- | --------------------------------------- | --- | --- |
| <FEATURE> |     |     | Specifiesafeature.Forexample,aaaorvrrp. |     |     |
vsx-peer
ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Usage
Capacitiesareexpressedinuser-understandableterms.Thustheymaynotmaptoaspecifichardware
orsoftwareresourceorcomponent.Theyarenotintendedtodefineafeatureexhaustively.
Examples
ShowingallavailablecapacitiesforBGP:
| switch#            | show capacities | bgp |     |     |       |
| ------------------ | --------------- | --- | --- | --- | ----- |
| System Capacities: | Filter          | BGP |     |     |       |
| Capacities         | Name            |     |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of AS | numbers in | as-path | attribute |     |
| ------- | ------------ | ---------- | ------- | --------- | --- |
32
...
Showingallavailablecapacitiesformirroring:
| switch#            | show capacities | mirroring |     |     |       |
| ------------------ | --------------- | --------- | --- | --- | ----- |
| System Capacities: | Filter          | Mirroring |     |     |       |
| Capacities         | Name            |           |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of Mirror | Sessions | configurable | in a system |     |
| ------- | ---------------- | -------- | ------------ | ----------- | --- |
4
| Maximum | number of enabled | Mirror | Sessions | in a system |     |
| ------- | ----------------- | ------ | -------- | ----------- | --- |
4
ShowingallavailablecapacitiesforMSTP:
| switch#            | show capacities | mstp |     |     |       |
| ------------------ | --------------- | ---- | --- | --- | ----- |
| System Capacities: | Filter          | MSTP |     |     |       |
| Capacities         | Name            |      |     |     | Value |
----------------------------------------------------------------------------------
-
| Maximum | number of mstp | instances | configurable | in a system |     |
| ------- | -------------- | --------- | ------------ | ----------- | --- |
64
ShowingallavailablecapacitiesforVLANcount:
AccessControlLists|92

| switch#    | show        | capacities | vlan-count |            |     |       |
| ---------- | ----------- | ---------- | ---------- | ---------- | --- | ----- |
| System     | Capacities: |            | Filter     | VLAN Count |     |       |
| Capacities | Name        |            |            |            |     | Value |
----------------------------------------------------------------------------------
-
| Maximum    | number      | of VLANs | supported       |            | in the system |       |
| ---------- | ----------- | -------- | --------------- | ---------- | ------------- | ----- |
| 4094       | /switch#    |          | show capacities |            | vlan-count    |       |
| System     | Capacities: |          | Filter          | VLAN Count |               |       |
| Capacities | Name        |          |                 |            |               | Value |
----------------------------------------------------------------------------------
-
| Maximum | number | of VLANs | supported |     | in the system |     |
| ------- | ------ | -------- | --------- | --- | ------------- | --- |
4094
| Command        | History     |         |         |     |              |     |
| -------------- | ----------- | ------- | ------- | --- | ------------ | --- |
| Release        |             |         |         |     | Modification |     |
| 10.07orearlier |             |         |         |     | --           |     |
| Command        | Information |         |         |     |              |     |
| Platforms      |             | Command | context |     | Authority    |     |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| show capacities-status |     |     |           |            |     |     |
| ---------------------- | --- | --- | --------- | ---------- | --- | --- |
| show capacities-status |     |     | <FEATURE> | [vsx-peer] |     |     |
Description
Showssystemcapacitiesstatusandtheirvaluesforallfeaturesoraspecificfeature.
| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
<FEATURE> Specifiesthefeature,forexampleaaaorvrrpforwhichtodisplay
capacities,values,andstatus.Required.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
ThenumberofIPneighbors(IPv4+IPv6)entriessectionintheoutputoftheshow capacities-status l3-
resourcescommandliststhemaximumnumberofneighborssupportedbytheplatform(withboth
IPv4andIPv6neighborscombined).OnHPEArubaNetworking8320,8325,8400,9300/9300Sand10000
Switchseries,IPv6neighborswillcountavalueoftwoforeachneighbor,astheytakeuptwicethespace
inhardwareascomparedtoIPv4neighbors.Inpreviousreleases,theoutputtheshow capacities-
status l3-resourcescommandcountedIPv4andIPv6neighborsasconsumingthesamenumberof
resources/spaceinhardware.
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 93

ForSpineandL3-coreprofilesonHPEArubaNetworking8320,8325and10000Switchseries,theIPv6Route
entrysizeisstilloneforeachneighbor.ForLeafandL3-aggprofiles,theentrysizeisalsooneforIPv6routeswith
aprefixgreaterthan64.
Examples
Showingthesystemcapacitiesstatusforallfeatures:
|            |            | switch# | show | capacities-status |     |     |     |       |
| ---------- | ---------- | ------- | ---- | ----------------- | --- | --- | --- | ----- |
| System     | Capacities | Status  |      |                   |     |     |     |       |
| Capacities | Status     | Name    |      |                   |     |     |     | Value |
Maximum
----------------------------------------------------------------------------------
-------
| Number | of active | gateway | mac | addresses | in  | a system |     | 0   |
| ------ | --------- | ------- | --- | --------- | --- | -------- | --- | --- |
16
| Number | of aspath-lists |     | configured |     |     |     |     | 0   |
| ------ | --------------- | --- | ---------- | --- | --- | --- | --- | --- |
64
| Number | of community-lists |     | configured |     |     |     |     | 0   |
| ------ | ------------------ | --- | ---------- | --- | --- | --- | --- | --- |
64
...
ShowingthesystemcapacitiesstatusforBGP:
| switch#    | show capacities-status |         |        | bgp |     |     |       |         |
| ---------- | ---------------------- | ------- | ------ | --- | --- | --- | ----- | ------- |
| System     | Capacities             | Status: | Filter | BGP |     |     |       |         |
| Capacities | Status                 | Name    |        |     |     |     | Value | Maximum |
----------------------------------------------------------------------------------
--
| Number | of aspath-lists    |        | configured |        |     |      | 0   | 64     |
| ------ | ------------------ | ------ | ---------- | ------ | --- | ---- | --- | ------ |
| Number | of community-lists |        | configured |        |     |      | 0   | 64     |
| Number | of neighbors       |        | configured | across | all | VRFs | 0   | 50     |
| Number | of peer            | groups | configured | across | all | VRFs | 0   | 25     |
| Number | of prefix-lists    |        | configured |        |     |      | 0   | 64     |
| Number | of route-maps      |        | configured |        |     |      | 0   | 64     |
| Number | of routes          | in     | BGP RIB    |        |     |      | 0   | 256000 |
Number of route reflector clients configured across all VRFs 0 16
ShowingthesystemcapacitiesstatusforL3:
| switch#    | show capacities-status |         |        | l3  |           |     |       |     |
| ---------- | ---------------------- | ------- | ------ | --- | --------- | --- | ----- | --- |
| System     | Capacities             | Status: | Filter | L3  | resources |     |       |     |
| Capacities | Status                 | Name    |        |     |           |     | Value |     |
Maximum
----------------------------------------------------------------------------------
--
| Number | of IP neighbor |     | (IPv4+IPv6) | entries |     |     | 4   |     |
| ------ | -------------- | --- | ----------- | ------- | --- | --- | --- | --- |
49152
| Number | of IP Directed |     | Broadcast | neighbor |     | entries | 0   |     |
| ------ | -------------- | --- | --------- | -------- | --- | ------- | --- | --- |
4096
| Number | of IPv6 | Long | Prefix Routes | currently |     | configured | 3   |     |
| ------ | ------- | ---- | ------------- | --------- | --- | ---------- | --- | --- |
5000
AccessControlLists|94

| Number | of  | IPv6 | neighbor(ND) |     | entries |     |     |     | 4   |
| ------ | --- | ---- | ------------ | --- | ------- | --- | --- | --- | --- |
49152
Number of L3 Groups for IP Tunnels and ECMP Groups currently configured 1
2047
Number of L3 Destinations for Routes, Nexthops in ECMP groups and
|     | Tunnels | currently |     | configured |     |     |     |     | 4   |
| --- | ------- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
2045
| Number | of  | routes | (IPv4+IPv6) |     | currently |     | configured |     | 5   |
| ------ | --- | ------ | ----------- | --- | --------- | --- | ---------- | --- | --- |
65536
| Number | of  | IPv4 | routes | currently |     | configured |     |     | 0   |
| ------ | --- | ---- | ------ | --------- | --- | ---------- | --- | --- | --- |
65536
Number of IPv6 routes currently configured with prefix 0-64 4
13312
Number of IPv6 routes currently configured with prefix 65-127 2
510
| switch#    |            | show capacities-status |         |     |        | l3  |           |     |       |
| ---------- | ---------- | ---------------------- | ------- | --- | ------ | --- | --------- | --- | ----- |
| System     | Capacities |                        | Status: |     | Filter | L3  | resources |     |       |
| Capacities |            | Status                 | Name    |     |        |     |           |     | Value |
Maximum
----------------------------------------------------------------------------------
--
| Number | of  | IP neighbor |     | (IPv4+IPv6) |     | entries |     |     | 4   |
| ------ | --- | ----------- | --- | ----------- | --- | ------- | --- | --- | --- |
49152
| Number | of  | IP Directed |     | Broadcast |     | neighbor |     | entries | 0   |
| ------ | --- | ----------- | --- | --------- | --- | -------- | --- | ------- | --- |
4096
| Number | of  | IPv6 | Long Prefix |     | Routes | currently |     | configured | 3   |
| ------ | --- | ---- | ----------- | --- | ------ | --------- | --- | ---------- | --- |
5000
| Number | of  | IPv6 | neighbor(ND) |     | entries |     |     |     | 4   |
| ------ | --- | ---- | ------------ | --- | ------- | --- | --- | --- | --- |
49152
Number of L3 Groups for IP Tunnels and ECMP Groups currently configured 1
2047
Number of L3 Destinations for Routes, Nexthops in ECMP groups and
|     | Tunnels | currently |     | configured |     |     |     |     | 4   |
| --- | ------- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
2045
| Number | of  | routes | (IPv4+IPv6) |     | currently |     | configured |     | 5   |
| ------ | --- | ------ | ----------- | --- | --------- | --- | ---------- | --- | --- |
65536
| Number | of  | IPv4 | routes | currently |     | configured |     |     | 0   |
| ------ | --- | ---- | ------ | --------- | --- | ---------- | --- | --- | --- |
65536
Number of IPv6 routes currently configured with prefix 0-64 4
13312
Number of IPv6 routes currently configured with prefix 65-127 2
510
| Command |     | History |     |     |     |                                                        |     |     |     |
| ------- | --- | ------- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
| Release |     |         |     |     |     | Modification                                           |     |     |     |
| 10.13   |     |         |     |     |     | UpdatedtoshownewlysupportedconfigurationofIPv6routeson |     |     |     |
theASIC.
| 10.07orearlier |     |             |     |     |     | --  |     |     |     |
| -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| Command        |     | Information |     |     |     |     |     |     |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 95

| Platforms |     | Command |     | context | Authority |
| --------- | --- | ------- | --- | ------- | --------- |
Allplatforms Manager(#) Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show object-group
show object-group [{ip|ipv6} address | port] [<OBJECT-GROUP-NAME>] [commands]
[configuration]
Description
Showsinformationaboutyourdefinedobjectgroups.Whenshow object-groupisenteredwithout
parameters,informationforallobjectgroupsisshown.Theparametersfilterthelistofobjectgroups
forwhichinformationisshown.
| Parameter  |         |     |         |     | Description |
| ---------- | ------- | --- | ------- | --- | ----------- |
| [{ip|ipv6} | address |     | | port] |     |             |
Specifiestheobjectgrouptype,eitheraddressforanIPaddress,
orport.
| <OBJECT-GROUP-NAME> |     |     |     |     | Specifiestheobjectgroupname. |
| ------------------- | --- | --- | --- | --- | ---------------------------- |
[commands] Specifiesthattheobjectgroupdefinitionistobeshownasthe
commandsandparametersusedtocreateitratherthanin
tabularform.
[configuration] Specifiesthattheuser-configuredobjectgroupsbeshownas
configured.Theoutputofthecommandwiththisparametermay
notbethesameaswhatisactiveontheswitchduetoa
misconfiguredobjectgroup.SeeExamplesinthistopic.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingconfiguredobjectgroups:
| switch#  | show | object-group  |     |         |     |
| -------- | ---- | ------------- | --- | ------- | --- |
| Type     |      | Name          |     |         |     |
| Sequence |      | L4 Port(s)/IP |     | Address |     |
-------------------------------------------------------------------------------
| IPv4 |     | my_address_group |     |     |     |
| ---- | --- | ---------------- | --- | --- | --- |
10 192.168.0.1
20 192.168.0.3
| Port |     | my_port_group |     |     |     |
| ---- | --- | ------------- | --- | --- | --- |
10 eq 80
20 gt 65525
switch#
switch#
|              | show        | object-group |               | commands         |     |
| ------------ | ----------- | ------------ | ------------- | ---------------- | --- |
| object-group |             | ip           | address       | my_address_group |     |
| 10           | 192.168.0.1 |              |               |                  |     |
| 20           | 192.168.0.3 |              |               |                  |     |
| object-group |             | port         | my_port_group |                  |     |
| 10           | eq 80       |              |               |                  |     |
AccessControlLists|96

| 20 gt | 65525 |     |     |
| ----- | ----- | --- | --- |
Showingamisconfiguredobjectgroup:
| switch# show | object-group  |         |     |
| ------------ | ------------- | ------- | --- |
| Type         | Name          |         |     |
| Sequence     | L4 Port(s)/IP | Address |     |
-------------------------------------------------------------------------------
! object-group ip address My_ip_object_group user configuration does not match
! the active hardware configuration. Run 'object-group ip address NAME reset'
! to reset the object group to match the active hardware configuration.
| IPv4 | my_address_group |     |     |
| ---- | ---------------- | --- | --- |
switch#
switch#
| Type     | Name          |         |     |
| -------- | ------------- | ------- | --- |
| Sequence | L4 Port(s)/IP | Address |     |
-------------------------------------------------------------------------------
! object-group ip address My_ip_object_group user configuration does not match
! the active hardware configuration. Run 'object-group ip address NAME reset'
! to reset the object group to match the active hardware configuration.
| IPv4 | my_address_group |     |     |
| ---- | ---------------- | --- | --- |
switch#
| switch# show | object-group  |         | configuration |
| ------------ | ------------- | ------- | ------------- |
| Type         | Name          |         |               |
| Sequence     | L4 Port(s)/IP | Address |               |
-------------------------------------------------------------------------------
! object-group ip address My_ip_object_group user configuration does not match
! the active hardware configuration. Run 'object-group ip address NAME reset'
! to reset the object group to match the active hardware configuration.
| IPv4 | my_address_group |     |     |
| ---- | ---------------- | --- | --- |
10 192.168.0.1
20 192.168.0.3
switch#
| switch# show | object-group |     | commands |
| ------------ | ------------ | --- | -------- |
! object-group ip address My_ip_object_group user configuration does not match
! the active hardware configuration. Run 'object-group ip address NAME reset'
! to reset the object group to match the active hardware configuration.
switch#
| switch# show | object-group |     | commands configuration |
| ------------ | ------------ | --- | ---------------------- |
! object-group ip address My_ip_object_group user configuration does not match
! the active hardware configuration. Run 'object-group ip address NAME reset'
! to reset the object group to match the active hardware configuration.
| object-group | ip address | my_address_group |     |
| ------------ | ---------- | ---------------- | --- |
10 192.168.0.1
20 192.168.0.3
Resettingamisconfiguredobjectgroup:
| switch(config)# | object-group  |         | all reset |
| --------------- | ------------- | ------- | --------- |
| switch(config)# | exit          |         |           |
| switch# show    | object-group  |         |           |
| Type            | Name          |         |           |
| Sequence        | L4 Port(s)/IP | Address |           |
-------------------------------------------------------------------------------
| IPv4 | my_address_group |     |     |
| ---- | ---------------- | --- | --- |
switch#
| switch# show | object-group  |         | configuration |
| ------------ | ------------- | ------- | ------------- |
| Type         | Name          |         |               |
| Sequence     | L4 Port(s)/IP | Address |               |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 97

-------------------------------------------------------------------------------
| IPv4                | my_address_group     |         |              |
| ------------------- | -------------------- | ------- | ------------ |
| Command History     |                      |         |              |
| Release             |                      |         | Modification |
| 10.07orearlier      |                      |         | --           |
| Command Information |                      |         |              |
| Platforms           | Command              | context | Authority    |
| Allplatforms        | Operator(>)orManager |         |              |
(#)
AccessControlLists|98

Chapter 3
ACLconfigurationexamples
ThischaptershowsexamplesfordefiningandapplyingIPv4andIPv6ACLs.
| IPv4 ACL | example |     | overview |     |     |     |     |
| -------- | ------- | --- | -------- | --- | --- | --- | --- |
Thisexample:
n DefinesandappliesanACLtointerface1/1/1onSwitchA(seeimageinthistopic)sothatHostAis
notabletosendtraffictoHostB,butitcancommunicatewithallotherdevicesinthenetwork.
n Countsblockedpackets.
| Defining | and | applying |     | an  | IPv4 | ACL |     |
| -------- | --- | -------- | --- | --- | ---- | --- | --- |
Procedure
1. BegindefininganIPv4ACLnamedFILTER_TO_HOST_B:
| switch(config)# |     | access-list |     | ip  | FILTER_TO_HOST_B |     |     |
| --------------- | --- | ----------- | --- | --- | ---------------- | --- | --- |
2. AddanACEthatdeniesaccessfromIPaddress192.168.1.2(HostA)to192.168.2.2(HostB):
| switch(config-acl-ip)# |     |     | deny | any | 192.168.1.2 | 192.168.2.2 | log |
| ---------------------- | --- | --- | ---- | --- | ----------- | ----------- | --- |
3. AddanACEthatallowsaccessfromallotherIPaddresses:
| switch(config-acl-ip)# |     |     | permit | any | any | any |     |
| ---------------------- | --- | --- | ------ | --- | --- | --- | --- |
4. ExittheACLdefinition:
| switch(config-acl-ip)# |     |     | exit |     |     |     |     |
| ---------------------- | --- | --- | ---- | --- | --- | --- | --- |
5. EnterthecontextoftheinterfacetowhichyouwillapplytheACL:
| switch(config)# |     | interface |     | 1/1/1 |     |     |     |
| --------------- | --- | --------- | --- | ----- | --- | --- | --- |
6. ApplytheFILTER_TO_HOST_BACLtoinbound(ingress)traffic:
| switch(config-if)# |     |     | apply | access-list |     | ip FILTER_TO_HOST_B | in  |
| ------------------ | --- | --- | ----- | ----------- | --- | ------------------- | --- |
99
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries)

7. ShowyourACL:
|     | switch(config-if)# |                  | exit       |                     |             |            |
| --- | ------------------ | ---------------- | ---------- | ------------------- | ----------- | ---------- |
|     | switch#            | show access-list |            | ip FILTER_TO_HOST_B |             |            |
|     | Type               | Name             |            |                     |             |            |
|     | Sequence           | Comment          |            |                     |             |            |
|     |                    | Action           |            |                     | L3 Protocol |            |
|     |                    | Source           | IP Address |                     | Source      | L4 Port(s) |
|     |                    | Destination      |            | IP Address          | Destination | L4 Port(s) |
|     |                    | Additional       |            | Parameters          |             |            |
----------------------------------------------------------------------------
---
|     | IPv4 | FILTER_TO_HOST_B |     |     |     |     |
| --- | ---- | ---------------- | --- | --- | --- | --- |
10
|     |     | deny |     |     | any |     |
| --- | --- | ---- | --- | --- | --- | --- |
192.168.1.2
192.168.2.2
|     |     | Logging:    | enabled |         |     |     |
| --- | --- | ----------- | ------- | ------- | --- | --- |
|     |     | Hit-counts: |         | enabled |     |     |
20
|     |     | permit |     |     | any |     |
| --- | --- | ------ | --- | --- | --- | --- |
any
any
----------------------------------------------------------------------------
---
| IPv6 | ACL example |     | overview |     |     |     |
| ---- | ----------- | --- | -------- | --- | --- | --- |
Thisexample:
n DefinesandappliesanACLtointerface1/1/1onSwitchA(seeimageinthistopic)sothatHostAis
notabletosendtraffictoHostB,butitcancommunicatewithallotherdevicesinthenetwork.
n Countsblockedpackets.
|100

| Defining | and | applying | an  | IPv6 | ACL |     |
| -------- | --- | -------- | --- | ---- | --- | --- |
Procedure
1. BegindefininganIPv6ACLnamedV6_INPUT_FILTER:
|     | switch(config)# | access-list | ipv6 | V6_INPUT_FILTER |     |     |
| --- | --------------- | ----------- | ---- | --------------- | --- | --- |
2. AddanACEthatdeniesaccesstoanIPaddresses1001::2through2001::2(includesHostB):
|     | switch(config-acl-ipv6)# |     | deny any | 1001::2 | 2001::2 log |     |
| --- | ------------------------ | --- | -------- | ------- | ----------- | --- |
3. AddanACEthatallowsaccessfromallotherIPaddresses:
|     | switch(config-acl-ipv6)# |     | permit any | any | any |     |
| --- | ------------------------ | --- | ---------- | --- | --- | --- |
4. ExittheACLdefinition:
|     | switch(config-acl-ipv6)# |     | exit |     |     |     |
| --- | ------------------------ | --- | ---- | --- | --- | --- |
5. EntertheinterfacetowhichyouwillapplytheACL:
|     | switch(config)# | interface | 1/1/1 |     |     |     |
| --- | --------------- | --------- | ----- | --- | --- | --- |
6. ApplytheV6_INPUT_FILTERACLtoinbound(ingress)traffic:
|     | switch(config-if)# | apply | access-list | ipv6 | V6_INPUT_FILTER | in  |
| --- | ------------------ | ----- | ----------- | ---- | --------------- | --- |
7. ShowyourACL:
switch(config-if)#
exit
|     | switch# show | access-list | interface |     | 1/1/1 |     |
| --- | ------------ | ----------- | --------- | --- | ----- | --- |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 101

Direction
Type Name
Sequence Comment
| Action      |            | L3 Protocol |            |
| ----------- | ---------- | ----------- | ---------- |
| Source      | IP Address | Source      | L4 Port(s) |
| Destination | IP Address | Destination | L4 Port(s) |
| Additional  | Parameters |             |            |
----------------------------------------------------------------------------
Inbound
IPv6 V6_INPUT_FILTER
10
| deny |     | any |     |
| ---- | --- | --- | --- |
1001::2
2001::2
| Logging:    | enabled |     |     |
| ----------- | ------- | --- | --- |
| Hit-counts: | enabled |     |     |
20
| permit |     | any |     |
| ------ | --- | --- | --- |
any
any
----------------------------------------------------------------------------
|102

Chapter 4

Classifier policies

Classifier policies

Classifier policies let a network administrator define sets of rules based on network traffic addressing or
other header content, and use these rules to restrict or alter the passage of traffic through the switch.
Choosing the rule criteria is called Classification, and one such rule, or list, is called a policy. Classification
is achieved by creating a traffic class. The types of classes (IPv4, and IPv6) are each focused on relevant
frame/packet characteristics. Classes can be configured to match or ignore almost any frame or packet
header field. Network traffic passing through a switch can be classified based on many different
frame/packet characteristics including, but not limited to:

n Frame ingress VLAN ID

n Source and/or destination IPv4, or IPv6 address

n Layer 2 (EtherType) and Layer 3 (IP) protocol

n Layer 4 application ports

A policy contains one or more policy entries, which are listed according to priority by sequence number.
A single policy entry contains a class and corresponding policy action. Policy action is taken on traffic
matched by its corresponding class. A policy can be applied to an individual front plane port, a Link
Aggregation Group (LAG) interface, or a VLAN.

See also ACL and Policy hardware resource considerations.

Traffic policing

Traffic policing supports policing of the inbound traffic. A typical application of traffic policing is to
supervise the specification of traffic entering a network and limit it within a reasonable range. Another
application is to "discipline" the extra traffic to prevent aggressive use of network resources by an
application. For example, you can limit bandwidth for HTTP packets to less than 50% of the total. If the
traffic of a session exceeds the limit, traffic policing can drop the packets or reset the IP precedence of
the packets. In the following illustrated example, outbound traffic is policed:

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

103

Traffic policing is widely used in policing traffic entering the ISP networks. It can classify the policed
traffic and take predefined policing actions on each packet depending on the evaluation result:

n Forwarding the packet if the evaluation result is "conforming."

n Dropping the packet if the evaluation result is "excess."

n Forwarding the packet with its precedence remarked when the evaluation result is "conforming."

Types of policy actions

The policy actions are broadly classified in the following categories:

n Remark actions

n Police actions

n Other actions

Each policy entry can have a combination of policy actions from these multiple categories, which are
executed in the order of configuration.

Remark actions

This category contains the following actions:

n Priority Code Point (PCP): 3-bit field in layer 2 802.1Q header refers to a class of service and maps

to a frame priority level.

n IP precedence: 3-bit field in IP header which denotes the importance or priority of the datagram.

n IP Differentiated Services Code Point (DSCP): 6-bit field in IP header for packet classification.

n Local Priority: Change the internal priority used to queue the packets for transmission. Local

priority can be used to rewrite the priority of traffic classes local to the system based on the QoS
mapping settings without changing the IP header or the 802.1Q header. Remark actions other than
local priority only change packets as they leave the switch. The local priority action can be combined
with the other remark actions to remark packets and change the internal priority to reflect the new
priority.

Police actions

Classifier policies | 104

Traffic policing meters inbound traffic on an interface or VLAN based on the following traffic
parameters:

n Committed information rate (CIR): Bandwidth limit for guaranteed traffic.

n Committed burst size (CBS): Maximum packet size permitted for bursts of data that exceed the CIR.

Based on these parameters, packets are dropped when traffic exceeds the bandwidth limit (CIR) and the
burst size for guaranteed traffic (CBS).

Other actions

Other actions include Drop: Drop the packet, and Mirror: Mirror the packets to a specified mirroring
session. For details, see the Monitoring Guide.

How policy matching works

A policy can be applied to an interface or VLAN to affect/control traffic arriving on that interface or VLAN
(inbound (ingress)). A single policy entry matches on one or more characteristics of the particular traffic
type and has a configured action to continue through the switch. This matching occurs by beginning
with the entry with the lowest sequence number. The entry is then compared against the incoming
frame to its particular match characteristics. If there is a match, the action is taken.

If there is no match, the match characteristics of the next sequence are compared to the relevant
frame/packet details. If there is a match, the specified actions are taken. This process continues until a
match is found; otherwise, the packet is permitted to flow through the switch unaltered. The "implicit
permit" behavior of policy matching differs from the "implicit deny" behavior of ACL matching.

Limitations

The following match criteria are not supported:

n IPv4 AH on outbound classes.

Active class configuration versus user-specified
configuration

The output of the show class command displays the active class configurations. Active class
configurations are the classes that have been configured and accepted by the system.

The output of the show class command with the configuration parameter, displays the classes that
have been configured by the user.

Discrepancies might occur between the active class configurations and the user-specified
configurations. In the user-specified class configurations, unsupported command parameters may have
been configured, or class can be modified after policy application and may have been unsuccessful due
to lack of hardware resources.

To determine if a discrepancy exists between what was configured and what is active, run any variant of
the show class command. If the active classes and configured classes are not the same, a warning
message is displayed.

! class MY_CLASS user configuration does not match active configuration.
! run 'class TYPE NAME reset' to reset class to match active configuration.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

105

If the configured class is processing and you entered the show class command with parameters, the
following in-progress message is displayed:

! class ip MY_CLASS user configuration currently being processed
! run 'class TYPE NAME reset' to reset class to match active configuration.

If the configured class is processing and you entered the show class command without parameters, the
following in-progress message is displayed:

% Warning: MY_CLASS user configuration currently being processed
% run 'class TYPE NAME reset' to reset class to match active configuration.

If the warning message or in-progress message is displayed, additional changes may be made until the
error message is no longer displayed. Or you can use the class {all|ip <class-name>|ipv6 <class-
name>|mac <class-name>} reset command to change the user-specified configuration to match the
active configuration.

The show running-config command also shows a warning about classes that are in progress or failed.

Example

Resetting the user-specified class configuration to the active configuration:

switch(config)# class all reset

Active policy configuration versus user-specified
configuration

The output of the show policy command displays the active policy configurations. Active policy
configurations are the policies that have been configured and accepted by the system. With applied
policies, the active configuration displays the interfaces on which the policies have successfully been
programmed in hardware.

The output of the show policy command with the configuration parameter, displays the policies that
have been configured by the user.

Discrepancies might exist between the active policy configurations and the user-specified
configurations. In the user-specified policy configurations, unsupported command parameters might
have been configured, or an application of a policy might have been unsuccessful because of a lack of
hardware resources.

To determine if a discrepancy exists between the configuration and what is active, run any variant of the
show policy command. If the active policies and configured policies are not the same, a warning
message is displayed in the output of the show command.

! policy MY_POLICY user configuration does not match active configuration.
! run 'policy NAME reset' to reset policy to match active configuration.

The switch displays an in progress message while it processes the configured policy:

Classifier policies | 106

! policy MY_POLICY user configuration currently being processed
! run 'policy NAME reset' to reset policy to match active configuration.
Ifthewarningmessageorinprogressmessageisdisplayed,additionalchangesmaybemadeuntilthe
errormessageisnolongerdisplayed.Oryoucanusethepolicy resetcommandto
<policy-name>
changetheuser-specifiedconfigurationtomatchtheactiveconfiguration.
Example
ResettingMY_POLICY:
| switch(config)# |     | policy MY_POLICY |     | reset  |            |               |
| --------------- | --- | ---------------- | --- | ------ | ---------- | ------------- |
| Considerations  |     | for when         | a   | policy | is applied | per interface |
ThissectionisonlyapplicabletopolicesappliedtophysicalinterfacesandLAGsusingtheper-interface
parameter.
Theresetcommand(mentionedintheprevioussection)isnotusefulifoneormoreuniqueinstances
ofapolicycreatedusingtheper-interfaceparameterfailtoupdateinhardwareeventhoughthe
parentpolicydoesupdate.Ifthisoccurs,youcanmakeadditionalchangestothepolicyandits
applicationstocorrectthediscrepancyuntiltheerrormessagesarenolongerdisplayed.Alternatively
considerusingcommandcheckpoint-rollbackasdescribedintheAOS-CXFundamentalsGuide.
Policiesusingtheper-interfaceparameterhaveslightlydifferentwarningandin-progressmessages
duetouniqueinstancesofthepolicybeingcreatedandappliedtoindividualphysicalinterfacesand
LAGs.
Forexample,thisishowthewarningmessageswillappeariftheuniqueinstancesofthepolicyfor
interfaces1/1/2-1/1/3failtoupdatewhiletheuniqueinstancesofthepolicyforinterfaces1/1/1,1/1/4
successfullyupdate.
| switch(config)# |     | show policy | commands |     |     |     |
| --------------- | --- | ----------- | -------- | --- | --- | --- |
! policy my_policy user configuration does not match active configuration on
| interface | 1/1/2 | for ingress. |     |     |     |     |
| --------- | ----- | ------------ | --- | --- | --- | --- |
! policy my_policy user configuration does not match active configuration on
| interface | 1/1/3        | for ingress.   |        |               |     |     |
| --------- | ------------ | -------------- | ------ | ------------- | --- | --- |
| policy    | my_policy    |                |        |               |     |     |
|           | 10 class     | ip my_ip_class | action | drop          |     |     |
| interface | 1/1/1        |                |        |               |     |     |
|           | apply policy | my_policy      | in     | per-interface |     |     |
! policy my_policy user configuration does not match active configuration.
| interface | 1/1/2        |           |     |               |     |     |
| --------- | ------------ | --------- | --- | ------------- | --- | --- |
|           | apply policy | my_policy | in  | per-interface |     |     |
! policy my_policy user configuration does not match active configuration.
| interface       | 1/1/3        |             |     |               |     |     |
| --------------- | ------------ | ----------- | --- | ------------- | --- | --- |
|                 | apply policy | my_policy   | in  | per-interface |     |     |
| interface       | 1/1/4        |             |     |               |     |     |
|                 | apply policy | my_policy   | in  | per-interface |     |     |
| switch(config)# |              | show policy |     |               |     |     |
Name
|     | Sequence Comment |      |     |     |     |     |
| --- | ---------------- | ---- | --- | --- | --- | --- |
|     | Class            | Type |     |     |     |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 107

action
-------------------------------------------------------------------------------
% Warning: my_policy user configuration does not match active configuration on
| interface | 1/1/2 | for ingress. |     |
| --------- | ----- | ------------ | --- |
% Warning: my_policy user configuration does not match active configuration on
| interface | 1/1/3 | for ingress. |     |
| --------- | ----- | ------------ | --- |
my_policy
10
|     | my_ip_class | ipv4 |     |
| --- | ----------- | ---- | --- |
drop
Thisishowthein-progressmessageswillappearifthechildpoliciesforinterfaces1/1/2-1/1/3are
currentlyupdatingwhilethechildpoliciesforinterfaces1/1/1,1/1/4havesuccessfullyupdated.
| switch(config)# |     | show policy | commands |
| --------------- | --- | ----------- | -------- |
! policy my_policy user configuration currently being processed on interface 1/1/2
for ingress.
! policy my_policy user configuration currently being processed on interface 1/1/3
for ingress.
! run 'show policy [commands]' to display active policy configuration.
policy my_policy
| 10        | class  | ip my_ip_class | action drop      |
| --------- | ------ | -------------- | ---------------- |
| interface | 1/1/1  |                |                  |
| apply     | policy | my_policy      | in per-interface |
! policy my_policy user configuration currently being processed
! run 'show policy [commands]' to display active policy configuration.
| interface | 1/1/2  |           |                  |
| --------- | ------ | --------- | ---------------- |
| apply     | policy | my_policy | in per-interface |
! policy my_policy user configuration currently being processed
! run 'show policy [commands]' to display active policy configuration.
| interface       | 1/1/3  |             |                  |
| --------------- | ------ | ----------- | ---------------- |
| apply           | policy | my_policy   | in per-interface |
| interface       | 1/1/4  |             |                  |
| apply           | policy | my_policy   | in per-interface |
| switch(config)# |        | show policy |                  |
Name
| Sequence | Comment |     |     |
| -------- | ------- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
% Warning: my_policy user configuration currently being processed on interface
| 1/1/2 for | ingress. |     |     |
| --------- | -------- | --- | --- |
% Warning: my_policy user configuration currently being processed on interface
| 1/1/3 for | ingress. |     |     |
| --------- | -------- | --- | --- |
% run 'show policy [commands]' to display active policy configuration.
my_policy
10
|     | my_ip_class | ipv4 |     |
| --- | ----------- | ---- | --- |
drop
Thisishowthewarningmessageswillappearifthechildpoliciesforinterfaces1/1/2-1/1/3failedto
applyorreplacewhilethechildpoliciesforinterfaces1/1/1,1/1/4havesuccessfullyappliedorreplaced.
| switch(config)# |     | show policy | commands |
| --------------- | --- | ----------- | -------- |
policy my_policy
| 10        | class  | ip my_ip_class | action drop      |
| --------- | ------ | -------------- | ---------------- |
| interface | 1/1/1  |                |                  |
| apply     | policy | my_policy      | in per-interface |
Classifierpolicies|108

! policy my_policy user configuration does not match active configuration.
! run 'policy NAME reset' to reset policy to match active configuration.
| interface | 1/1/2  |                            |     |     |     |
| --------- | ------ | -------------------------- | --- | --- | --- |
| apply     | policy | my_policy in per-interface |     |     |     |
! policy my_policy user configuration does not match active configuration.
! run 'policy NAME reset' to reset policy to match active configuration.
| interface | 1/1/3  |                            |     |     |     |
| --------- | ------ | -------------------------- | --- | --- | --- |
| apply     | policy | my_policy in per-interface |     |     |     |
| interface | 1/1/4  |                            |     |     |     |
| apply     | policy | my_policy in per-interface |     |     |     |
switch(config)#
|     | show | policy |     |     |     |
| --- | ---- | ------ | --- | --- | --- |
Name
| Sequence | Comment |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
my_policy
10
|     | my_ip_class | ipv4 |     |     |     |
| --- | ----------- | ---- | --- | --- | --- |
drop
| Classifier | policy | commands    |     |     |     |
| ---------- | ------ | ----------- | --- | --- | --- |
| Classifier | policy | application |     |     |     |
Classifierpoliciescanbeappliedasfollows("Rt-In"="Routed-In"):
| Policy type       |     |     | IPv4+6 | IPv4+6 | MAC |
| ----------------- | --- | --- | ------ | ------ | --- |
| Direction         |     |     | In     | Rt-In  | In  |
| L2interface(port) |     |     | Yes    |        | Yes |
| L2LAG             |     |     | Yes    |        | Yes |
| L3interface(port) |     |     | Yes    | Yes    | Yes |
| L3LAG             |     |     | Yes    | Yes    | Yes |
L3interface(port)subinterface(notapplicabletotheHPEAruba Yes Yes Yes
Networking8320,9300/9300S,10040SwitchSeries)
L3LAGsubinterface(notapplicabletotheHPEArubaNetworking8320, Yes Yes Yes
9300/9300S,10040SwitchSeries)
| VLAN          |     |     | Yes |          | Yes |
| ------------- | --- | --- | --- | -------- | --- |
| InterfaceVLAN |     |     |     | Yes(PBR) |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 109

Policiescannotmatchmulticastpacketsontheroutedindirection.
Thefollowingmatchcriteriaarenotsupported.Ifanyofthesematchcriteriaareattemptedtobeconfigured,an
errormessagewillbedisplayedandtheactionwillnotbecompleted.
HPEArubaNetworking8320,8325,9300/9300S,10000,10040SwitchSeries:
| TCP flags | CWR and ECE      |         |               |
| --------- | ---------------- | ------- | ------------- |
| TCP flags | and TTL (hop     | limit)  | on IP classes |
| Fragment  | on IPv6 classes  | in VLAN | policies      |
| VLAN ID   | in VLAN policies |         |               |
HPEArubaNetworking8320SwitchSeriesonly:
| IPv4 AH | on inbound classes |     |     |
| ------- | ------------------ | --- | --- |
apply policy (config-if, config-lag-if, config-if-vlan, config-vlan)
| Context config-if, | config-lag-if: |                    |                 |
| ------------------ | -------------- | ------------------ | --------------- |
| apply policy       | <POLICY-NAME>  | {in|out|routed-in} | [per-interface] |
no apply policy <POLICY-NAME> {in|out|routed-in} [per-interface]
| Context config-vlan:    |               |           |     |
| ----------------------- | ------------- | --------- | --- |
| apply policy            | <POLICY-NAME> | {in|out}  |     |
| no apply policy         | <POLICY-NAME> | {in|out}  |     |
| Context config-if-vlan: |               |           |     |
| apply policy            | <POLICY-NAME> | routed-in |     |
| no apply policy         | <POLICY-NAME> | routed-in |     |
Description
AppliesapolicytothecurrentphysicalinterfaceportorLAGorVLANcontext.
OnlyonedirectionofapolicycanbeappliedtoaninterfaceorVLANatatime,thususingtheapply
commandonaninterfaceorVLANwithanalready-appliedpolicyofthesamedirectionwillreplacethe
currentlyappliedpolicy.
TheVLANcontextsupportstheinandoutdirections,whichapplytobothbridgedandroutedtraffic.The
InterfaceVLANcontextonlysupportstherouted-indirectionwhichappliesonlytoroutedtraffic.
ThenoformofthiscommandremovesapolicyfromtheinterfaceorVLANspecifiedbythecurrent
context.
| Parameter     |     |     | Description                |
| ------------- | --- | --- | -------------------------- |
| <POLICY-NAME> |     |     | Specifiesthepolicytoapply. |
in
Selectstheinbound(ingress)trafficdirection.
out Selectstheoutbound(egress)trafficdirection.Notapplicableto
subinterfaces.
routed-in
Selectsroutedintraffic.
per-interface Specifiesthatuniqueinstancesofthepolicybeappliedtoeach
Classifierpolicies|110

| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
interfaceorLAGratherthanthedefaultofsharingthepolicy
acrossallinterfacesandLAGs.
| Usage (applies | to config-if, |     | config-lag-if | contexts) |     |
| -------------- | ------------- | --- | ------------- | --------- | --- |
n ThesubinterfacecanoptionallybespecifiedaftertheinterfaceorLAG,precededbyaperiod.For
| example,1/1/1.10orlag |     | 125.4. |     |     |     |
| --------------------- | --- | ------ | --- | --- | --- |
Subinterfacesonlysupporttheingress(inandrouted-in)directions.Ingressonsubinterfacesis
n
supportedontheHPEArubaNetworking8325and10000SwitchseriesbutnotontheHPEAruba
Networking8320,9300,9300S,10040Switchseries.
n Whenper-interfaceisincluded,uniqueinstancesofthepolicyareappliedtoeachphysicalinterface
portorLAGratherthanthedefaultofsharingthepolicyacrossallinterfacesandLAGs.Theunique
instanceofapolicyhasaparent-childrelationshipwiththepolicyfromwhichitwascreated.Theper-
interfaceoptionisusefulwhenyouwantuniquepolicerstobecreatedforeachinterfaceorLAG
ratherthanusingsharedpolicers.Itisalsousefulwhenyouwantthestatistics(hitcountsand
conformrate)tobespecifictoaninterfaceorLAGratherthanbeingaggregated.Becauseper-
interfacecreatesmorehardwareinstancesofapolicy,resourceconsumptionmayincrease
significantly.Itisrecommendedthatyouuseshow resourcestomonitorresourceutilizationas
configurationisapplied.
| Usage (applies | to config-vlan |     | context) |     |     |
| -------------- | -------------- | --- | -------- | --- | --- |
n OnlyonepolicytypemaybeappliedtoaVLANatatime.Therefore,usingtheapply policycommand
onaVLANwithanalready-appliedpolicyofthesametype,willreplacetheappliedpolicy.
Examples
Applyingapolicytoaninterface(ingress):
| switch(config)#    |     | interface | 1/1/1  |            |     |
| ------------------ | --- | --------- | ------ | ---------- | --- |
| switch(config-if)# |     | apply     | policy | MY_POLICY1 | in  |
Applyingapolicytoaninterface(ingress)specifyingper-interface:
| switch(config)#    |     | interface | 1/1/2  |            |                  |
| ------------------ | --- | --------- | ------ | ---------- | ---------------- |
| switch(config-if)# |     | apply     | policy | MY_POLICY1 | in per-interface |
Applyingapolicytoaninterface(egress):
| switch(config)#    |     | interface | 1/1/2  |            |     |
| ------------------ | --- | --------- | ------ | ---------- | --- |
| switch(config-if)# |     | apply     | policy | MY_POLICY2 | out |
Applyingapolicytoaninterface(egress)specifyingper-interface:
| switch(config)#    |     | interface | 1/1/2  |            |                   |
| ------------------ | --- | --------- | ------ | ---------- | ----------------- |
| switch(config-if)# |     | apply     | policy | MY_POLICY2 | out per-interface |
Applyingapolicytoaninterfacerange(ingress):
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 111

| switch(config)# | interface | 1/1/3-1/1/6 |     |     |     |     |
| --------------- | --------- | ----------- | --- | --- | --- | --- |
switch(config-if-<1/1/2-1/1/5>)#
|     |     |     | apply | policy | MY_POLICY3 | in  |
| --- | --- | --- | ----- | ------ | ---------- | --- |
Applyingapolicytoaninterfacerange(ingress)specifyingper-interface:
| switch(config)# | interface | 1/1/7-1/1/9 |     |     |     |     |
| --------------- | --------- | ----------- | --- | --- | --- | --- |
switch(config-if-<1/1/2-1/1/5>)# apply policy MY_POLICY4 in per-interface
Removingapolicyfromaninterface(ingress):
| switch(config)#    | interface | 1/1/1        |            |     |     |     |
| ------------------ | --------- | ------------ | ---------- | --- | --- | --- |
| switch(config-if)# | no        | apply policy | MY_POLICY1 |     | in  |     |
Removingapolicyfromaninterfacerange(ingress):
| switch(config)#                  | interface | 1/1/3-1/1/6 |     |              |            |     |
| -------------------------------- | --------- | ----------- | --- | ------------ | ---------- | --- |
| switch(config-if-<1/1/3-1/1/6>)# |           |             | no  | apply policy | MY_POLICY3 | in  |
Applyingapolicytoasubinterface(ingress):
| switch(config)#    | interface | 1/1/1.10 |            |     |     |     |
| ------------------ | --------- | -------- | ---------- | --- | --- | --- |
| switch(config-if)# | apply     | policy   | MY_POLICY1 |     | in  |     |
Applyingapolicytoasubinterface(egress):
| switch(config)# | interface | 1/1/2.8 |     |     |     |     |
| --------------- | --------- | ------- | --- | --- | --- | --- |
switch(config-if)#
|     | apply | policy | MY_POLICY1_egr |     | out |     |
| --- | ----- | ------ | -------------- | --- | --- | --- |
ApplyingapolicytoaLAG(ingress):
| switch(config)#        | interface | lag   | 100    |            |     |     |
| ---------------------- | --------- | ----- | ------ | ---------- | --- | --- |
| switch(config-lag-if)# |           | apply | policy | MY_POLICY5 | in  |     |
ApplyingapolicytoaLAG(ingress)specifyingper-interface:
| switch(config)# | interface | lag | 200 |     |     |     |
| --------------- | --------- | --- | --- | --- | --- | --- |
switch(config-lag-if)# apply policy MY_POLICY5 in per-interface
RemovingapolicyfromaLAG(ingress):
| switch(config)#        | interface | lag      | 100    |            |     |     |
| ---------------------- | --------- | -------- | ------ | ---------- | --- | --- |
| switch(config-lag-if)# |           | no apply | policy | MY_POLICY5 | in  |     |
ApplyingapolicytoaLAGsubinterface(ingress):
Classifierpolicies|112

| switch(config)# | interface |     | lag 125.4 |     |     |     |     |
| --------------- | --------- | --- | --------- | --- | --- | --- | --- |
switch(config-lag-if)#
|     |     |     | apply policy | MY_POLICY5 |     | in  |     |
| --- | --- | --- | ------------ | ---------- | --- | --- | --- |
ApplyingapolicytoaLAGsubinterface(egress):
| switch(config)#        | interface |     | lag 150.8    |            |     |     |     |
| ---------------------- | --------- | --- | ------------ | ---------- | --- | --- | --- |
| switch(config-lag-if)# |           |     | apply policy | MY_POLICY5 |     | out |     |
ApplyingapolicytoaVLAN(ingress):
| switch(config)#      | vlan | 1     |        |            |     |     |     |
| -------------------- | ---- | ----- | ------ | ---------- | --- | --- | --- |
| switch(config-vlan)# |      | apply | policy | MY_POLICY6 |     | in  |     |
ApplyingapolicytoaVLAN(egress):
| switch(config)#      | vlan | 1   |              |           |     |     |     |
| -------------------- | ---- | --- | ------------ | --------- | --- | --- | --- |
| switch(config-vlan)# |      | no  | apply policy | my_policy |     | out |     |
ApplyingapolicytomultipleVLANs(ingress):
| switch(config)#              | vlan | 10,20 |       |        |            |     |     |
| ---------------------------- | ---- | ----- | ----- | ------ | ---------- | --- | --- |
| switch(config-vlan-<10,20>)# |      |       | apply | policy | MY_POLICY7 |     | in  |
ApplyingapolicytoaninterfaceVLANrouted(ingress):
| switch(config)# | vlan | 1   |     |     |     |     |     |
| --------------- | ---- | --- | --- | --- | --- | --- | --- |
switch(config-if-vlan)#
|     |     |     | apply policy | MY_POLICY8 |     | routed-in |     |
| --- | --- | --- | ------------ | ---------- | --- | --------- | --- |
ApplyingapolicytoaninterfaceVLANrangerouted(ingress):
| switch(config)# | vlan | 2-5 |     |     |     |     |     |
| --------------- | ---- | --- | --- | --- | --- | --- | --- |
switch(config-if-vlan-<2-5>)# apply policy MY_POLICY8 routed-in
RemovingapolicyfromaVLAN(ingress):
| switch(config)#      | vlan | 1   |              |            |     |     |     |
| -------------------- | ---- | --- | ------------ | ---------- | --- | --- | --- |
| switch(config-vlan)# |      | no  | apply policy | MY_POLICY6 |     | in  |     |
RemovingapolicyfrommultipleVLANs(ingress):
| switch(config)#              | vlan | 10,20 |     |              |     |            |     |
| ---------------------------- | ---- | ----- | --- | ------------ | --- | ---------- | --- |
| switch(config-vlan-<10,20>)# |      |       | no  | apply policy |     | MY_POLICY7 | in  |
RemovingapolicyfromaninterfaceVLANrouted(ingress):
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 113

| switch(config)# | vlan | 1   |     |     |
| --------------- | ---- | --- | --- | --- |
switch(config-if-vlan)#
|     |     | no apply | policy MY_POLICY8 | routed-in |
| --- | --- | -------- | ----------------- | --------- |
RemovingapolicyfromaninterfaceVLANrangerouted(ingress):
| switch(config)# | vlan | 2-5 |     |     |
| --------------- | ---- | --- | --- | --- |
switch(config-if-vlan-<2-5>)# no apply policy MY_POLICY8 routed-in
| Command | History |     |                                                     |     |
| ------- | ------- | --- | --------------------------------------------------- | --- |
| Release |         |     | Modification                                        |     |
| 10.16   |         |     | Addedsupportforegressonallinterfacesonthe8325switch |     |
series.
| 10.16 |     |     | Addedsupportforegressonallinterfacesonthe10000switch |     |
| ----- | --- | --- | ---------------------------------------------------- | --- |
series.
| 10.11 |     |     | Addedsupportforingressonsubinterfacesonthe8325switch |     |
| ----- | --- | --- | ---------------------------------------------------- | --- |
series.
| 10.11 |     |     | Addedsupportforingressonsubinterfacesonthe10000switch |     |
| ----- | --- | --- | ----------------------------------------------------- | --- |
series.
| 10.07orearlier |             |         | --        |     |
| -------------- | ----------- | ------- | --------- | --- |
| Command        | Information |         |           |     |
| Platforms      | Command     | context | Authority |     |
Allplatforms config-if Administratorsorlocalusergroupmemberswithexecution
|     | config-lag-if |     | rightsforthiscommand. |     |
| --- | ------------- | --- | --------------------- | --- |
config-vlan
config-if-vlan
| apply policy    |               |      |     |     |
| --------------- | ------------- | ---- | --- | --- |
| apply policy    | <POLICY-NAME> | {in} |     |     |
| no apply policy | <POLICY-NAME> | {in} |     |     |
Description
Appliesapolicytotheglobalconfigcontext.
Onlyonepolicycanbegloballyappliedatatime.Applyingapolicygloballyagain,replacestheprevious
globallyappliedpolicy.
Thenoformofthiscommandremovesapplicationoftheglobalpolicy.
| Parameter     |     |     | Description                                 |     |
| ------------- | --- | --- | ------------------------------------------- | --- |
| <POLICY-NAME> |     |     | Specifiesthepolicytoapply.                  |     |
| in            |     |     | Selectstheinbound(ingress)trafficdirection. |     |
Examples
Classifierpolicies|114

Applyingpolicyglobal1totheglobalconfigcontext:
| switch(config)# | apply | policy | global1 | in  |     |
| --------------- | ----- | ------ | ------- | --- | --- |
Removingapplicationofpolicyglobal1fromtheglobalconfigcontext:
| switch(config)# | no          | apply policy | global1 | in           |     |
| --------------- | ----------- | ------------ | ------- | ------------ | --- |
| Command         | History     |              |         |              |     |
| Release         |             |              |         | Modification |     |
| 10.07orearlier  |             |              |         | --           |     |
| Command         | Information |              |         |              |     |
| Platforms       | Command     | context      |         | Authority    |     |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325 |     |     |     | rightsforthiscommand. |     |
| ---- | --- | --- | --- | --------------------- | --- |
8325H
8325P
9300
9300S
10000
10040
class copy
| class {ip|ipv6|mac} | <CLASS-NAME> |     | copy | <DESTINATION-CLASS> |     |
| ------------------- | ------------ | --- | ---- | ------------------- | --- |
Description
Copiesaclasstoanewdestinationclassoroverwritesanexistingclass.Copyingaclasscopiesall
entriesaswell.
| Parameter |     |     |     | Description |     |
| --------- | --- | --- | --- | ----------- | --- |
{ip|ipv6|mac} <CLASS-NAME> Specifiesthetypeandnameoftheclasstobecopied.
| <DESTINATION-CLASS> |     |     |     | Specifiesthenameofthedestinationclass. |     |
| ------------------- | --- | --- | --- | -------------------------------------- | --- |
Examples
CopyinganIPv4class.Copyingaclasswithentriescopiesallitsentriesaswell:
| switch(config)# | class   | ip MY_IP_CLASS |     | copy MY_IP_CLASS2 |            |
| --------------- | ------- | -------------- | --- | ----------------- | ---------- |
| switch(config)# | do      | show class     |     |                   |            |
| Type            | Name    |                |     |                   |            |
| Sequence        | Comment |                |     |                   |            |
|                 | Action  |                |     | L3 Protocol       |            |
|                 | Source  | IP Address     |     | Source            | L4 Port(s) |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 115

|     | Destination | IP         | Address | Destination | L4 Port(s) |
| --- | ----------- | ---------- | ------- | ----------- | ---------- |
|     | Additional  | Parameters |         |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- |
| 11   | ignore      |     |     | udp |     |
any
any
| 21  | match |     |     | tcp |     |
| --- | ----- | --- | --- | --- | --- |
192.168.0.1
192.168.0.2
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS2 |     |     |     |     |
| ---- | ------------ | --- | --- | --- | --- |
| 11   | ignore       |     |     | udp |     |
any
any
| 21  | match |     |     | tcp |     |
| --- | ----- | --- | --- | --- | --- |
192.168.0.1
192.168.0.2
CopyinganIPv6class:
| switch(config)# | class | ipv6 | MY_IPV6_CLASS | copy MY_IPV6_CLASS2 |     |
| --------------- | ----- | ---- | ------------- | ------------------- | --- |
switch(config)#
|          | do          | show       | class   |             |            |
| -------- | ----------- | ---------- | ------- | ----------- | ---------- |
| Type     | Name        |            |         |             |            |
| Sequence | Comment     |            |         |             |            |
|          | Action      |            |         | L3 Protocol |            |
|          | Source      | IP Address |         | Source      | L4 Port(s) |
|          | Destination | IP         | Address | Destination | L4 Port(s) |
|          | Additional  | Parameters |         |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- |
|      | 2 ignore      |     |     | udp |     |
any
any
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS2 |     |     |     |     |
| ---- | -------------- | --- | --- | --- | --- |
|      | 2 ignore       |     |     | udp |     |
any
any
CopyingaMACclass:
| switch(config)# | class | mac | MY_MAC_CLASS | copy MY_MAC_CLASS2 |     |
| --------------- | ----- | --- | ------------ | ------------------ | --- |
switch(config)#
|          | do          | show        | class   |           |     |
| -------- | ----------- | ----------- | ------- | --------- | --- |
| Type     | Name        |             |         |           |     |
| Sequence | Comment     |             |         |           |     |
|          | Action      |             |         | EtherType |     |
|          | Source      | MAC Address |         |           |     |
|          | Destination | MAC         | Address |           |     |
|          | Additional  | Parameters  |         |           |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_CLASS |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- |
|     | 2 ignore     |     |     | arp |     |
any
any
-------------------------------------------------------------------------------
| MAC | MY_MAC_CLASS2 |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- |
|     | 2 ignore      |     |     | arp |     |
Classifierpolicies|116

any
any

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

Administrators or local user group members with execution
rights for this command.

class ip

Syntax to create an IPv4 class and enter its context. Plus syntax to remove a class:
class ip <CLASS-NAME>
no class ip <CLASS-NAME>

Syntax (within the class context) for creating or removing class entries for protocols ah, gre, esp, igmp,
ospf, pim (ip is available as an alias for any):

[<SEQUENCE-NUMBER>]
{match|ignore}
{any|ip|ah|gre|esp|igmp|ospf|pim|<IP-PROTOCOL-NUM>}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]

no <SEQUENCE-NUMBER>

Syntax (within the class context) for creating or removing class entries for protocols sctp, tcp, udp:

[<SEQUENCE-NUMBER>]
{match|ignore}
{sctp|tcp|udp}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>]
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
[{eq|gt|lt} <PORT>|range <MIN-PORT> <MAX-PORT>]
[cwr][ece] [urg] [ack] [psh] [rst] [syn] [fin] [established]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]

no <SEQUENCE-NUMBER>

Syntax (within the class context) for creating or removing class entries for protocol icmp:

[<SEQUENCE-NUMBER>]
{match|ignore}
{icmp}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}] [icmp-code <ICMP-CODE-VALUE>]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]

no <SEQUENCE-NUMBER>

Syntax (within the class context) for class entry comments:

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

117

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

no <SEQUENCE-NUMBER> comment

Description

Creates or modifies an IPv4 traffic class to match specified packets. Class is composed of one or more
class entries ordered and prioritized by sequence numbers. With this command, the class can classify
traffic based on IPv4 header information.

The no form of the command can be used to delete either an IPv4 traffic class (use no with the class
command) or an individual IPv4 traffic class entry (use no with the sequence number).

Parameter

ip

<CLASS-NAME>

<SEQUENCE-NUMBER>

{match|ignore}

<IP-PROTOCOL-NUM>

{any|<SRC-IP-ADDRESS>
[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}

{any|<DST-IP-ADDRESS>
[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}

[{eq|gt|lt} <PORT>|range <MIN-PORT><MAX-PORT>]

Description

Specifies create or modify an IPv4 class.

Specifies the name of this class.

Specifies a sequence number for the class
entry. Optional. Range: 1-4294967295.

Creates a rule to match or ignore specified
packets.

Specifies the protocol as its Internet Protocol
number. For example, 2 corresponds to the
IGMP protocol. Range: 0 to 255.

Specifies the source IPv4 address.

n any - specifies any source IPv4 address.
n <SRC-IP-ADDRESS> - specifies the source

IPv4 host address.

o <PREFIX-LENGTH> - specifies the

address bits to mask (CIDR subnet mask

notation). Range: 1 to 32.

o <SUBNET-MASK> - specifies the address
bits to mask (dotted decimal notation).

Specifies the destination IPv4 address.

n any - specifies any destination IPv4

address.

n <DST-IP-ADDRESS> - specifies the

destination IPv4 host address.

o <PREFIX-LENGTH> - specifies the

address bits to mask (CIDR subnet mask

notation). Range: 1 to 32.

o <SUBNET-MASK> - specifies the address
bits to mask (dotted decimal notation).

Specifies the port or port range. Port numbers
are in the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.
n gt <PORT> - specifies any Layer 4 port

Classifier policies | 118

Parameter

Description

cwr

ece

urg

ack

psh

rst

syn

fin

established

dscp <DSCP-SPECIFIER>

greater than the indicated port.

n lt <PORT> - specifies any Layer 4 port less

than the indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies

the Layer 4 port range.

Specifies matching on the TCP Flag CWR :
Congestion Window Reduced

Specifies matching on the TCP Flag ECE :
Explicit Congestion Notification [ECN]- Echo

Specifies matching on the TCP Flag: Urgent.

Specifies matching on the TCP Flag:
Acknowledgment.

Specifies matching on the TCP Flag: Push
buffered data to receiving application.

Specifies matching on the TCP Flag: Reset the
connection.

Specifies matching on the TCP Flag:
Synchronize sequence numbers.

Specifies matching on the TCP Flag: Finish
connection.

Specifies matching on the TCP Flag:
Established connection.

Specifies the Differentiated Services Code
Point (DSCP), either a numeric <DSCP-VALUE>
(0 to 63) or one of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class

1, low drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class

1, medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class

1, high drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class

2, low drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class

2, medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class

2, high drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class

3, low drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class

3, medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

119

Parameter

Description

3, high drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class

4, low drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class

4, medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class

4, high drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)
n CS1 - DSCP 8 (Class Selector 1: Scavenger)
n CS2 - DSCP 16 (Class Selector 2: OAM)
n CS3 - DSCP 24 (Class Selector 3: Signaling)
n CS4 - DSCP 32 (Class Selector 4: Realtime)
n CS5 - DSCP 40 (Class Selector 5: Broadcast

video)

n CS6 - DSCP 48 (Class Selector 6: Network

control)

n CS7 - DSCP 56 (Class Selector 7)
n EF - DSCP 46 (Expedited Forwarding)

Specifies an Explicit Congestion Notification
value. Range: 0 to 3.

ecn <ECN-VALUE>

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies an IP precedence value. Range: 0 to 7.

tos <TOS-VALUE>

fragment

vlan <VLAN-ID>

ttl <TTL-VALUE>

count

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

Specifies the Type of Service value. Range: 0 to
31.

Specifies a fragment packet.

Specifies VLAN tag to match on. 802.1Q VLAN
ID.

NOTE:
This parameter cannot be used in any
class that will be applied to a VLAN.

Specifies a time-to-live (hop limit) value. Range:
0 to 255.

Keeps the hit counts of the number of packets
matching this class entry.

Adds a comment to a class entry. The no form
removes only the comment from the class
entry.

Usage

n Entering an existing <CLASS-NAME> value will cause the existing class to be modified, with any new

<SEQUENCE-NUMBER> value creating an additional class entry, and any existing <SEQUENCE-
NUMBER> value replacing the existing class entry with the same sequence number.

n If no sequence number is specified, a new class entry will be appended to the end of the class with a

sequence number equal to the highest class entry currently in the list plus 10.

Classifier policies | 120

n Ifthe<IP-PROTOCOL-NUM>parameterisusedinsteadofaprotocolname,ensurethatanyneeded
classentry-definitionparametersspecifictotheselectedprotocolarealsoprovided.
ThefollowingmatchcriteriaarenotsupportedonHPEArubaNetworking8320,8325and10000Switch
series:
n TCPflagsCWRandECE
n TTL(hoplimit)
n AVLANIDinVLANpolicies
ThefollowingmatchcriteriaarenotsupportedforuseinegresspoliciesonHPEArubaNetworking
9300,9300S,10040Switchseries:
n TTL(hoplimit)
Examples
CreatinganIPv4classwiththreeentries:
| switch(config)# | class | ip MY_IP_CLASS |     |     |     |
| --------------- | ----- | -------------- | --- | --- | --- |
switch(config-class-ip)# 10 match icmp any any10 match icmp any any
| switch(config-class-ip)# |             | 20 ignore  | udp any         | any         |             |
| ------------------------ | ----------- | ---------- | --------------- | ----------- | ----------- |
| switch(config-class-ip)# |             | 30 match   | tcp 192.168.0.1 |             | 192.168.0.2 |
| switch(config-class-ip)# |             | exit       |                 |             |             |
| switch(config)#          | do          | show class |                 |             |             |
| Type                     | Name        |            |                 |             |             |
| Sequence                 | Comment     |            |                 |             |             |
|                          | Action      |            |                 | L3 Protocol |             |
|                          | Source      | IP Address |                 | Source      | L4 Port(s)  |
|                          | Destination | IP Address |                 | Destination | L4 Port(s)  |
|                          | Additional  | Parameters |                 |             |             |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |     |      |     |
| ---- | ----------- | --- | --- | ---- | --- |
|      | 10 match    |     |     | icmp |     |
any
any
|     | 20 ignore |     |     | udp |     |
| --- | --------- | --- | --- | --- | --- |
any
any
|     | 30 match |     |     | tcp |     |
| --- | -------- | --- | --- | --- | --- |
192.168.0.1
192.168.0.2
AddingacommenttoanexistingIPv4classentry:
| switch(config)#          | class       | ip MY_IP_CLASS |           |             |            |
| ------------------------ | ----------- | -------------- | --------- | ----------- | ---------- |
| switch(config-class-ip)# |             | 30 comment     | myipClass |             |            |
| switch(config-class-ip)# |             | exit           |           |             |            |
| switch(config)#          | do          | show class     |           |             |            |
| Type                     | Name        |                |           |             |            |
| Sequence                 | Comment     |                |           |             |            |
|                          | Action      |                |           | L3 Protocol |            |
|                          | Source      | IP Address     |           | Source      | L4 Port(s) |
|                          | Destination | IP Address     |           | Destination | L4 Port(s) |
|                          | Additional  | Parameters     |           |             |            |
-------------------------------------------------------------------------------
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 121

| IPv4 | MY_IP_CLASS |     |      |     |
| ---- | ----------- | --- | ---- | --- |
|      | 10 match    |     | icmp |     |
any
any
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
30 myipClass
|     | match |     | tcp |     |
| --- | ----- | --- | --- | --- |
192.168.0.1
192.168.0.2
RemovingacommentfromanexistingIPv4classentry:
| switch(config)#          | class       | ip MY_IP_CLASS |             |            |
| ------------------------ | ----------- | -------------- | ----------- | ---------- |
| switch(config-class-ip)# |             | no 30 comment  |             |            |
| switch(config-class-ip)# |             | exit           |             |            |
| switch(config)#          | do          | show class     |             |            |
| Type                     | Name        |                |             |            |
| Sequence                 | Comment     |                |             |            |
|                          | Action      |                | L3 Protocol |            |
|                          | Source      | IP Address     | Source      | L4 Port(s) |
|                          | Destination | IP Address     | Destination | L4 Port(s) |
|                          | Additional  | Parameters     |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |      |     |
| ---- | ----------- | --- | ---- | --- |
|      | 10 match    |     | icmp |     |
any
any
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
|     | 30 match |     | tcp |     |
| --- | -------- | --- | --- | --- |
192.168.0.1
192.168.0.2
| Type     | Name        |            |             |            |
| -------- | ----------- | ---------- | ----------- | ---------- |
| Sequence | Comment     |            |             |            |
|          | Action      |            | L3 Protocol |            |
|          | Source      | IP Address | Source      | L4 Port(s) |
|          | Destination | IP Address | Destination | L4 Port(s) |
|          | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |      |     |
| ---- | ----------- | --- | ---- | --- |
|      | 10 match    |     | icmp |     |
any
any
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
|     | 30 match |     | tcp |     |
| --- | -------- | --- | --- | --- |
192.168.0.1
192.168.0.2
ReplacinganIPv4classentryinanexistingclass:
| switch(config)#          | class | ip MY_IP_CLASS |         |     |
| ------------------------ | ----- | -------------- | ------- | --- |
| switch(config-class-ip)# |       | 10 match igmp  | any any |     |
Classifierpolicies|122

| switch(config-class-ip)# |             | exit       |             |            |
| ------------------------ | ----------- | ---------- | ----------- | ---------- |
| switch(config)#          | do          | show class |             |            |
| Type                     | Name        |            |             |            |
| Sequence                 | Comment     |            |             |            |
|                          | Action      |            | L3 Protocol |            |
|                          | Source      | IP Address | Source      | L4 Port(s) |
|                          | Destination | IP Address | Destination | L4 Port(s) |
|                          | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |      |     |
| ---- | ----------- | --- | ---- | --- |
|      | 10 match    |     | igmp |     |
any
any
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
|     | 30 match |     | tcp |     |
| --- | -------- | --- | --- | --- |
192.168.0.1
192.168.0.2
RemovinganIPv4classentry:
| switch(config)#          | class       | ip MY_IP_CLASS |             |            |
| ------------------------ | ----------- | -------------- | ----------- | ---------- |
| switch(config-class-ip)# |             | no 10          |             |            |
| switch(config-class-ip)# |             | exit           |             |            |
| switch(config)#          | do          | show class     |             |            |
| Type                     | Name        |                |             |            |
| Sequence                 | Comment     |                |             |            |
|                          | Action      |                | L3 Protocol |            |
|                          | Source      | IP Address     | Source      | L4 Port(s) |
|                          | Destination | IP Address     | Destination | L4 Port(s) |
|                          | Additional  | Parameters     |             |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |     |     |
| ---- | ----------- | --- | --- | --- |
| 20   | ignore      |     | udp |     |
any
any
| 30  | match |     | tcp |     |
| --- | ----- | --- | --- | --- |
192.168.0.1
192.168.0.2
RemovinganIPv4class.Removingaclasswithentriesremovesallitsentriesaswell.Ifaclassassociated
withapolicyentry(ormultiplepolicyentries)isremoved,thecorrespondingentriesarealsoremoved.
Thecorrespondingentriesareonlyremovediftheclassisunusedbyallpolicyentries.
| switch(config)# | no      | class ip MY_IP_CLASS |     |     |
| --------------- | ------- | -------------------- | --- | --- |
| switch(config)# | do      | show class           |     |     |
| No Class        | found.  |                      |     |     |
| Command         | History |                      |     |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 123

| Release        |             |         | Modification |
| -------------- | ----------- | ------- | ------------ |
| 10.07orearlier |             |         | --           |
| Command        | Information |         |              |
| Platforms      | Command     | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
|     | The class | ip <CLASS- |     |
| --- | --------- | ---------- | --- |
|     | NAME>     | command    |     |
|     | takes you | into the   |     |
config-class-ipconfig-
|     | class-ip | context       |     |
| --- | -------- | ------------- | --- |
|     | where    | you enter the |     |
class entries.
class ipv6
SyntaxtocreateanIPv6classandenteritscontext.Plussyntaxtoremoveaclass:
| class ipv6    | <CLASS-NAME> |     |     |
| ------------- | ------------ | --- | --- |
| no class ipv6 | <CLASS-NAME> |     |     |
Syntax(withintheclasscontext)forcreatingorremovingclassentriesforprotocolsah,gre,esp,igmp,
ospf,pim(ipv6isavailableasanaliasforany):
[<SEQUENCE-NUMBER>]
{match|ignore}
{any|ipv6|ah|gre|esp|igmp|ospf|pim|<IP-PROTOCOL-NUM>}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]
no <SEQUENCE-NUMBER>
Syntax(withintheclasscontext)forcreatingorremovingclassentriesforprotocolssctp,tcp,udp:
[<SEQUENCE-NUMBER>]
{match|ignore}
{sctp|tcp|udp}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
| [{eq|gt|lt} | <PORT>|range | <MIN-PORT> | <MAX-PORT>] |
| ----------- | ------------ | ---------- | ----------- |
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
| [{eq|gt|lt} | <PORT>|range | <MIN-PORT>  | <MAX-PORT>]   |
| ----------- | ------------ | ----------- | ------------- |
| [urg] [ack] | [psh] [rst]  | [syn] [fin] | [established] |
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]
no <SEQUENCE-NUMBER>
Syntax(withintheclasscontext)forcreatingorremovingclassentriesforprotocolicmpv6:
[<SEQUENCE-NUMBER>]
{permit|deny}
{icmpv6}
{any|<SRC-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
{any|<DST-IP-ADDRESS>[/{<PREFIX-LENGTH>|<SUBNET-MASK>}]}
[icmp-type {echo|echo-reply|<ICMP-TYPE-VALUE>}] [icmp-code <ICMP-CODE-VALUE>]
[dscp <DSCP-SPECIFIER>] [ecn <ECN-VALUE>] [ip-precedence <IP-PRECEDENCE-VALUE>]
[tos <TOS-VALUE>] [fragment] [vlan <VLAN-ID>] [ttl <TTL-VALUE>] [count]
no <SEQUENCE-NUMBER>
Classifierpolicies|124

Syntax (within the class context) for class entry comments:

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

no <SEQUENCE-NUMBER> comment

Description

Creates or modifies an IPv6 traffic class to match specified packets. Class is composed of one or more
class entries ordered and prioritized by sequence numbers. With this command, each class can classify
traffic based on IPv6 header information.

The no form of the command deletes either an IPv6 traffic class (use no with the class command) or an
individual IPv6 traffic class entry (use no with the sequence number).

Parameter

ipv6

<CLASS-NAME>

<SEQUENCE-NUMBER>

{match|ignore}

<IP-PROTOCOL-NUM>

{any|<SRC-IP-ADDRESS>[/
{
<PREFIX-LENGTH>|<SUBNET-MASK>}]}

{any|<DST-IP-ADDRESS>[/
{
<PREFIX-LENGTH>|<SUBNET-MASK>}]}

[{eq|gt|lt} <PORT>|range
<MIN-PORT><MAX-PORT>]

Description

Specifies create or modify an IPv6 class.

Specifies the name of this class.

Specifies a sequence number for the class entry.
Optional. Range: 1-4294967295.

Creates a rule to match or ignore specified packets.

Specifies the protocol as its Internet Protocol
number. For example, 2 corresponds to the IGMP
protocol. Range: 0 to 255.

Specifies the source IPv6 address.

n any - specifies any source IPv6 address.
n <SRC-IP-ADDRESS> - specifies the source IPv4

host address.

o <PREFIX-LENGTH> - specifies the address bits
to mask (CIDR subnet mask notation). Range: 1

to 32.

o <SUBNET-MASK> - specifies the address bits to

mask (dotted decimal notation).

Specifies the destination IPv4 address.

n any - specifies any destination IPv6 address.
n <DST-IP-ADDRESS> - specifies the destination IPv6

host address.

o <PREFIX-LENGTH> - specifies the address bits
to mask (CIDR subnet mask notation). Range: 1

to 32.

o <SUBNET-MASK> - specifies the address bits to

mask (dotted decimal notation).

Specifies the port or port range. Port numbers are in
the range of 0 to 65535.

n eq <PORT> - specifies the Layer 4 port.
n gt <PORT> - specifies any Layer 4 port greater

than the indicated port.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

125

Parameter

Description

cwr

ece

urg

ack

psh

rst

syn

fin

established

dscp <DSCP-SPECIFIER>

n lt <PORT> - specifies any Layer 4 port less than

the indicated port.

n range <MIN-PORT> <MAX-PORT> - specifies the

Layer 4 port range.

Specifies matching on the TCP Flag CWR : Congestion
Window Reduced

Specifies matching on the TCP Flag ECE : Explicit
Congestion Notification [ECN]- Echo

Specifies matching on the TCP Flag: Urgent.

Specifies matching on the TCP Flag: Acknowledgment.

Specifies matching on the TCP Flag: Push buffered
data to receiving application.

Specifies matching on the TCP Flag: Reset the
connection.

Specifies matching on the TCP Flag: Synchronize
sequence numbers.

Specifies matching on the TCP Flag: Finish
connection.

Specifies matching on the TCP Flag: Established
connection.

Specifies the Differentiated Services Code Point
(DSCP), either a numeric <DSCP-VALUE> (0 to 63) or
one of these keywords:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low

drop probability)

n AF12 - DSCP 12 (Assured Forwarding Class 1,

medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high

drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low

drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2,

medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high

drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low

drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3,

medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high

drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low

Classifier policies | 126

Parameter

Description

drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4,

medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high

drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)
n CS1 - DSCP 8 (Class Selector 1: Scavenger)
n CS2 - DSCP 16 (Class Selector 2: OAM)
n CS3 - DSCP 24 (Class Selector 3: Signaling)
n CS4 - DSCP 32 (Class Selector 4: Real time)
n CS5 - DSCP 40 (Class Selector 5: Broadcast video)
n CS6 - DSCP 48 (Class Selector 6: Network control)
n CS7 - DSCP 56 (Class Selector 7)
n EF - DSCP 46 (Expedited Forwarding)

Specifies an Explicit Congestion Notification value.
Range: 0 to 3.

ecn <ECN-VALUE>

ip-precedence <IP-PRECEDENCE-VALUE>

Specifies an IP precedence value. Range: 0 to 7.

tos <TOS-VALUE>

fragment

vlan <VLAN-ID>

ttl <TTL-VALUE>

count

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

Usage

Specifies the Type of Service value. Range: 0 to 31.

Specifies a fragment packet.

Specifies VLAN tag to match on. 802.1Q VLAN ID.

NOTE:
This parameter cannot be used in any class that
will be applied to a VLAN.

Specifies a time-to-live (hop limit) value. Range: 0 to
255.

Keeps the hit counts of the number of packets
matching this class entry.

Adds a comment to a class entry. The no form
removes only the comment from the class entry.

n If you enter an existing <CLASS-NAME> value, the existing class is modified with any new

<SEQUENCE-NUMBER> value. This action creates an additional class entry. Any existing <SEQUENCE-
NUMBER> value replaces the existing class entry with the same sequence number.

n If no sequence number is specified, a new class entry is appended to the end of the class with a

sequence number equal to the highest class entry currently in the list plus 10.

n If the <IP-PROTOCOL-NUM> parameter is used instead of a protocol name, ensure that any needed

class entry-definition parameters specific to the selected protocol are also provided.

The following match criteria are not supported on HPE Aruba Networking 8320, 8325 and 10000 Switch
series:

n TCP flags CWR and ECE

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

127

n TTL(hoplimit)
n FragmentinVLANpolicies
AVLANIDinVLANpolicies
n
ThefollowingmatchcriteriaarenotsupportedforuseinegresspoliciesonHPEArubaNetworking
9300,9300S,10040Switchseries:
n TTL(hoplimit)
Examples
CreatinganIPv6classwithtwoentries:
| switch(config)#            | class       | ipv6 MY_IPV6_CLASS |                |            |
| -------------------------- | ----------- | ------------------ | -------------- | ---------- |
| switch(config-class-ipv6)# |             | 10 match           | icmpv6 any any |            |
| switch(config-class-ipv6)# |             | 20 ignore          | udp any any    |            |
| switch(config-class-ipv6)# |             | exit               |                |            |
| switch(config)#            | do          | show class         |                |            |
| Type                       | Name        |                    |                |            |
| Sequence                   | Comment     |                    |                |            |
|                            | Action      |                    | L3 Protocol    |            |
|                            | Source      | IP Address         | Source         | L4 Port(s) |
|                            | Destination | IP Address         | Destination    | L4 Port(s) |
|                            | Additional  | Parameters         |                |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |        |     |
| ---- | ------------- | --- | ------ | --- |
|      | 10 match      |     | icmpv6 |     |
any
any
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
AddingacommenttoanexistingIPv6classentry:
| switch(config)#            | class | ipv6 MY_IPV6_CLASS |                |     |
| -------------------------- | ----- | ------------------ | -------------- | --- |
| switch(config-class-ipv6)# |       | 10 match           | icmpv6 any any |     |
| switch(config-class-ipv6)# |       | 20 ignore          | udp any any    |     |
| switch(config-class-ipv6)# |       | 20 comment         | myipv6class    |     |
switch(config-class-ipv6)#
exit
| switch(config)# | do          | show class |             |            |
| --------------- | ----------- | ---------- | ----------- | ---------- |
| Type            | Name        |            |             |            |
| Sequence        | Comment     |            |             |            |
|                 | Action      |            | L3 Protocol |            |
|                 | Source      | IP Address | Source      | L4 Port(s) |
|                 | Destination | IP Address | Destination | L4 Port(s) |
|                 | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |        |     |
| ---- | ------------- | --- | ------ | --- |
|      | 10 match      |     | icmpv6 |     |
any
any
20 myipv6class
|     | ignore |     | udp |     |
| --- | ------ | --- | --- | --- |
any
any
RemovingacommentfromanexistingIPv6classentry:
Classifierpolicies|128

| switch(config)# | class | ipv6 MY_IPV6_CLASS |     |     |
| --------------- | ----- | ------------------ | --- | --- |
switch(config-class-ipv6)#
|                            |             | no 20 comment |             |            |
| -------------------------- | ----------- | ------------- | ----------- | ---------- |
| switch(config-class-ipv6)# |             | exit          |             |            |
| switch(config)#            | do          | show class    |             |            |
| Type                       | Name        |               |             |            |
| Sequence                   | Comment     |               |             |            |
|                            | Action      |               | L3 Protocol |            |
|                            | Source      | IP Address    | Source      | L4 Port(s) |
|                            | Destination | IP Address    | Destination | L4 Port(s) |
|                            | Additional  | Parameters    |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |        |     |
| ---- | ------------- | --- | ------ | --- |
|      | 10 match      |     | icmpv6 |     |
any
any
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
| Type     | Name        |            |             |            |
| -------- | ----------- | ---------- | ----------- | ---------- |
| Sequence | Comment     |            |             |            |
|          | Action      |            | L3 Protocol |            |
|          | Source      | IP Address | Source      | L4 Port(s) |
|          | Destination | IP Address | Destination | L4 Port(s) |
|          | Additional  | Parameters |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |        |     |
| ---- | ------------- | --- | ------ | --- |
|      | 10 match      |     | icmpv6 |     |
any
any
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
ReplacinganIPv6classentryinanexistingIPv6class:
| switch(config)#            | class       | ipv6 MY_IPV6_CLASS |             |            |
| -------------------------- | ----------- | ------------------ | ----------- | ---------- |
| switch(config-class-ipv6)# |             | 10 match any       | any 1020::  |            |
| switch(config-class-ipv6)# |             | exit               |             |            |
| switch(config)#            | do          | show class         |             |            |
| Type                       | Name        |                    |             |            |
| Sequence                   | Comment     |                    |             |            |
|                            | Action      |                    | L3 Protocol |            |
|                            | Source      | IP Address         | Source      | L4 Port(s) |
|                            | Destination | IP Address         | Destination | L4 Port(s) |
|                            | Additional  | Parameters         |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |
| ---- | ------------- | --- | --- | --- |
|      | 10 match      |     | any |     |
any
1020::
|     | 20 ignore |     | udp |     |
| --- | --------- | --- | --- | --- |
any
any
RemovinganIPv6classentry:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 129

| switch(config)# |     | class | ipv6 | MY_IPV6_CLASS |     |     |     |
| --------------- | --- | ----- | ---- | ------------- | --- | --- | --- |
switch(config-class-ipv6)#
|                            |             |     |            | no 10   |     |             |            |
| -------------------------- | ----------- | --- | ---------- | ------- | --- | ----------- | ---------- |
| switch(config-class-ipv6)# |             |     |            | exit    |     |             |            |
| switch(config)#            |             | do  | show       | class   |     |             |            |
| Type                       | Name        |     |            |         |     |             |            |
| Sequence                   | Comment     |     |            |         |     |             |            |
|                            | Action      |     |            |         |     | L3 Protocol |            |
|                            | Source      | IP  | Address    |         |     | Source      | L4 Port(s) |
|                            | Destination |     | IP         | Address |     | Destination | L4 Port(s) |
|                            | Additional  |     | Parameters |         |     |             |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- | --- |
|      | 20 ignore     |     |     |     |     | udp |     |
any
any
RemovinganIPv6class.Removingaclasswithentriesremovesallitsentriesaswell.Ifaclass
associatedwithapolicyentry(ormultiplepolicyentries)isremoved,thecorrespondingentriesarealso
removed.
Thecorrespondingentriesareonlyremovediftheclassisunusedbyallpolicyentries.
| switch(config)# |             | no  | class   | ipv6 MY_IPV6_CLASS |              |     |     |
| --------------- | ----------- | --- | ------- | ------------------ | ------------ | --- | --- |
| switch(config)# |             | do  | show    | class              |              |     |     |
| No Class        | found.      |     |         |                    |              |     |     |
| Command         | History     |     |         |                    |              |     |     |
| Release         |             |     |         |                    | Modification |     |     |
| 10.07orearlier  |             |     |         |                    | --           |     |     |
| Command         | Information |     |         |                    |              |     |     |
| Platforms       | Command     |     | context |                    | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|     | Theclassipv6<CLASS- |     |     |     | rightsforthiscommand. |     |     |
| --- | ------------------- | --- | --- | --- | --------------------- | --- | --- |
NAME>commandtakes
youintotheconfig-
class-ipv6command
contextwhereyouenter
theclassentries.
class mac
| class mac <CLASS-NAME> |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- |
[<SEQUENCE-NUMBER>]
{match|ignore}
{any|<SRC-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|<DST-MAC-ADDRESS>[/<ETHERNET-MASK>}]}
{any|aarp|appletalk|arp|fcoe|fcoe-init|ip|ipv6|ipx-arpa|ipx-non-arpa|is-is|
lldp|mpls-multicast|mpls-unicast|q-in-q|rbridge|trill|wake-on-lan|
Classifierpolicies|130

<NUMERIC-ETHERTYPE>}

[pcp <PCP-VALUE>] [vlan <VLAN-ID>] [count]

[<SEQUENCE-NUMBER>] comment <TEXT-STRING>

Description

Creates or modifies a MAC traffic class to match specified packets. Class is composed of one or more
class entries ordered and prioritized by sequence numbers. With this command, each class can classify
traffic based on MAC header information.

The no form of the command can be used to delete either a MAC traffic class (use no with the class
command) or an individual MAC traffic class entry (use no with the sequence number).

Parameter

mac

<CLASS-NAME>

<SEQUENCE-NUMBER>

{match|ignore}

comment

{any|<SRC-MAC-ADDRESS>
[/<ETHERNET-MASK>}]}

{any|<DST-MAC-ADDRESS>
[/<ETHERNET-MASK>}]}

Description

Specifies create or modify a MAC class.

Specifies the name of this class.

Specifies a sequence number for the class entry. Optional. Range:
1-4294967295.

Creates a rule to match or ignore specified packets.

Stores the remaining entered text as a class comment.

Specifies the source host MAC address (xxxx.xxxx.xxxx), OUI, or
the keyword any. You can optionally include the following:
<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).

Specifies the destination host MAC address (xxxx.xxxx.xxxx), OUI,
or the keyword any. You can optionally include the following:
<ETHERNET-MASK> - The address bits to mask (xxxx.xxxx.xxxx).

Protocol

Select an ethertype protocol from the following (enter one only):

n any - Any ethertype protocol
n <NUMERIC-ETHERTYPE> - Enter an EtherType protocol

number. Range: 0x600-0xffff.

n Or enter an EtherType protocol name from the following list:

o aarp

o appletalk

o arp

o fcoe

o fcoe-init

o ip

o ipv6

o ipx-arpa

o ipx-non-arpa

o is-is

o lldp

o mpls-multicast

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

131

| Parameter |     |     | Description |
| --------- | --- | --- | ----------- |
o mpls-unicast
o
q-in-q
o rbridge
o trill
o
wake-on-lan
pcp <PCP-VALUE> SpecifiesmatchingonQoSPriorityCodePoint.Range:0-7.
vlan <VLAN-ID> SpecifiesmatchingonaVLANID.EnteraVLANIDortheVLAN
name,ifconfigured.
NOTE:
Thisparametercannotbeusedinanyclassthatwillbe
appliedtoaVLAN.
| count |     |     | Keepsthehitcountsofthenumberofpacketsmatchingthisclass |
| ----- | --- | --- | ------------------------------------------------------ |
entry.
Examples
CreatingaMACclass:
| switch(config)# | class mac | MY_MAC_CLASS |     |
| --------------- | --------- | ------------ | --- |
switch(config-class-mac)#
|                           |         | match any  | any lldp  |
| ------------------------- | ------- | ---------- | --------- |
| switch(config-class-mac)# |         | ignore any | any arp   |
| switch(config-class-mac)# |         | exit       |           |
| switch(config)#           | do show | class      |           |
| Type Name                 |         |            |           |
| Sequence Comment          |         |            |           |
| Action                    |         |            | EtherType |
Source MAC Address
| Destination |     | MAC Address |     |
| ----------- | --- | ----------- | --- |
Additional Parameters
-------------------------------------------------------------------------------
| MAC MY_MAC_CLASS |     |     |      |
| ---------------- | --- | --- | ---- |
| 10 match         |     |     | lldp |
any
any
| 20 ignore |     |     | arp |
| --------- | --- | --- | --- |
any
any
AddingacommenttoanexistingMACclassentry:
switch(config)#
|     | class mac | MY_MAC_CLASS |     |
| --- | --------- | ------------ | --- |
switch(config-class-mac)# 10 comment MY_CLASS_ENTRY10 comment MY_CLASS_ENTRY
| switch(config-class-mac)# |         | exit  |           |
| ------------------------- | ------- | ----- | --------- |
| switch(config)#           | do show | class |           |
| Type Name                 |         |       |           |
| Sequence Comment          |         |       |           |
| Action                    |         |       | EtherType |
Source MAC Address
| Destination |     | MAC Address |     |
| ----------- | --- | ----------- | --- |
Classifierpolicies|132

Additional Parameters
-------------------------------------------------------------------------------
| MAC MY_MAC_CLASS |     |     |     |
| ---------------- | --- | --- | --- |
10 MY_CLASS_ENTRY
| match |     |     | lldp |
| ----- | --- | --- | ---- |
any
any
| 20 ignore |     |     | arp |
| --------- | --- | --- | --- |
any
any
RemovingacommentfromanexistingMACclassentry:
| switch(config)#           | class mac | MY_MAC_CLASS  |                |
| ------------------------- | --------- | ------------- | -------------- |
| switch(config-class-mac)# |           | no 10 comment | MY_CLASS_ENTRY |
| switch(config-class-mac)# |           | exit          |                |
| switch(config)#           | do show   | class         |                |
| Type Name                 |           |               |                |
| Sequence Comment          |           |               |                |
| Action                    |           |               | EtherType      |
Source MAC Address
| Destination |     | MAC Address |     |
| ----------- | --- | ----------- | --- |
Additional Parameters
-------------------------------------------------------------------------------
| MAC MY_MAC_CLASS |     |     |      |
| ---------------- | --- | --- | ---- |
| 10 match         |     |     | lldp |
any
any
| 20 ignore |     |     | arp |
| --------- | --- | --- | --- |
any
any
ReplacingaMACclassentryinanexistingMACclass:
| switch(config)#           | class mac | MY_MAC_CLASS |           |
| ------------------------- | --------- | ------------ | --------- |
| switch(config-class-mac)# |           | 10 match any | any any   |
| switch(config-class-mac)# |           | exit         |           |
| switch(config)#           | do show   | class        |           |
| Type Name                 |           |              |           |
| Sequence Comment          |           |              |           |
| Action                    |           |              | EtherType |
Source MAC Address
| Destination |     | MAC Address |     |
| ----------- | --- | ----------- | --- |
Additional Parameters
-------------------------------------------------------------------------------
| MAC MY_MAC_CLASS |     |     |     |
| ---------------- | --- | --- | --- |
| 10 match         |     |     | any |
any
any
| 20 ignore |     |     | arp |
| --------- | --- | --- | --- |
any
any
RemovingaMACclassentry:
| switch(config)#           | class mac | MY_MAC_CLASS |     |
| ------------------------- | --------- | ------------ | --- |
| switch(config-class-mac)# |           | no 1         |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 133

| switch(config-class-mac)# |     | exit |     |
| ------------------------- | --- | ---- | --- |
switch(config)#
|          | do      | show class |     |
| -------- | ------- | ---------- | --- |
| Type     | Name    |            |     |
| Sequence | Comment |            |     |
Action EtherType
|     | Source MAC  | Address     |     |
| --- | ----------- | ----------- | --- |
|     | Destination | MAC Address |     |
|     | Additional  | Parameters  |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_CLASS |     |     |
| --- | ------------ | --- | --- |
2 ignore arp
any
any
RemovingaMACclass.Removingaclasswithentriesremovesallitsentriesaswell.Ifaclassassociated
withapolicyentry(ormultiplepolicyentries)isremoved,thecorrespondingentriesarealsoremoved.
Thecorrespondingentriesareonlyremovediftheclassisunusedbyallpolicyentries.
| switch(config)# | no  | class mac MY_MAC_CLASS |     |
| --------------- | --- | ---------------------- | --- |
switch(config)#
|                     | do      | show class |              |
| ------------------- | ------- | ---------- | ------------ |
| No Class            | found.  |            |              |
| Command History     |         |            |              |
| Release             |         |            | Modification |
| 10.07orearlier      |         |            | --           |
| Command Information |         |            |              |
| Platforms           | Command | context    | Authority    |
8320 config Administratorsorlocalusergroupmemberswithexecution
| 8325  | Theclassmac<CLASS-    |     | rightsforthiscommand. |
| ----- | --------------------- | --- | --------------------- |
| 8325H | NAME>commandtakes     |     |                       |
| 8325P | youintotheconfig-     |     |                       |
| 9300  | class-maccontextwhere |     |                       |
| 9300S | youentertheclass      |     |                       |
entries.
10000
10040
class resequence
class {ip|ipv6|mac} <CLASS-NAME> resequence <STARTING-SEQUENCE-NUMBER> <INCREMENT>
Description
ResequencenumeringinanIPv4,orIPv6,orMACclass.
Classifierpolicies|134

| Parameter |     |     |     | Description |     |     |     |
| --------- | --- | --- | --- | ----------- | --- | --- | --- |
{ip|ipv6|mac} <CLASS-NAME> Specifiestheclasswhereyouwanttoresequenceclassentries.
<STARTING-SEQUENCE-NUMBER> Specifiesthesequencenumbertostartresequencingfrom.
| <INCREMENT> |     |     |     | Specifieshowmuchtoincrementthesequencenumbersby. |     |     |     |
| ----------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
Examples
ResequencinganIPv4class:
| switch(config)# |             | class   | ip MY_IP_CLASS | resequence |             | 1 10     |            |
| --------------- | ----------- | ------- | -------------- | ---------- | ----------- | -------- | ---------- |
| switch(config)# |             | do show | class          |            |             |          |            |
| Type            | Name        |         |                |            |             |          |            |
| Sequence        | Comment     |         |                |            |             |          |            |
|                 | Action      |         |                |            | L3          | Protocol |            |
|                 | Source      | IP      | Address        |            | Source      | L4       | Port(s)    |
|                 | Destination |         | IP Address     |            | Destination |          | L4 Port(s) |
|                 | Additional  |         | Parameters     |            |             |          |            |
-------------------------------------------------------------------------------
| IPv4 | MY_IP_CLASS |     |     |     |      |     |     |
| ---- | ----------- | --- | --- | --- | ---- | --- | --- |
|      | 1 match     |     |     |     | igmp |     |     |
any
any
| 11  | ignore |     |     |     | udp |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- |
any
any
| 21  | match |     |     |     | tcp |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- |
192.168.0.1
192.168.0.2
ResequencinganIPv6class:
| switch(config)#            |             | class   | ipv6 MY_IPV6_CLASS |     | resequence  |          | 1 1        |
| -------------------------- | ----------- | ------- | ------------------ | --- | ----------- | -------- | ---------- |
| switch(config-class-ipv6)# |             |         | exit               |     |             |          |            |
| switch(config)#            |             | do show | class              |     |             |          |            |
| Type                       | Name        |         |                    |     |             |          |            |
| Sequence                   | Comment     |         |                    |     |             |          |            |
|                            | Action      |         |                    |     | L3          | Protocol |            |
|                            | Source      | IP      | Address            |     | Source      | L4       | Port(s)    |
|                            | Destination |         | IP Address         |     | Destination |          | L4 Port(s) |
|                            | Additional  |         | Parameters         |     |             |          |            |
-------------------------------------------------------------------------------
| IPv6 | MY_IPV6_CLASS |     |     |     |     |     |     |
| ---- | ------------- | --- | --- | --- | --- | --- | --- |
|      | 1 match       |     |     |     | any |     |     |
any
1020::
|     | 2 ignore |     |     |     | udp |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
any
any
ResequencingaMACclass:
| switch(config)# |      | class   | mac MY_MAC_CLASS | resequence |     | 1   | 1   |
| --------------- | ---- | ------- | ---------------- | ---------- | --- | --- | --- |
| switch(config)# |      | do show | class            |            |     |     |     |
| Type            | Name |         |                  |            |     |     |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 135

| Sequence | Comment |     |     |
| -------- | ------- | --- | --- |
Action EtherType
|     | Source MAC  | Address     |     |
| --- | ----------- | ----------- | --- |
|     | Destination | MAC Address |     |
|     | Additional  | Parameters  |     |
-------------------------------------------------------------------------------
| MAC | MY_MAC_CLASS |     |     |
| --- | ------------ | --- | --- |
1 match any
any
any
2 ignore arp
any
any
| Command History     |         |         |              |
| ------------------- | ------- | ------- | ------------ |
| Release             |         |         | Modification |
| 10.07orearlier      |         |         | --           |
| Command Information |         |         |              |
| Platforms           | Command | context | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
class reset
class { all | ip <CLASS-NAME> | ipv6 <CLASS-NAME> |mac <CLASS-NAME> } reset
Description
Changestheuser-specifiedclassconfigurationtomatchtheactiveclassconfiguration.Usethis
commandwhenthereisadiscrepancybetweenwhattheuserconfiguredandwhatisactiveand
acceptedbythesystem.
Parameter Description
{ all | ip <CLASS-NAME>| ipv6 <CLASS-NAME> |mac <CLASS-NAME> } Specifieseitherallclasses
beresetorspecifiesthe
type(ipforIPv4,ipv6for
IPv6ormacforMACACL)
andnameoftheclassto
bereset.
Examples
Resettingtheuser-specifiedconfigurationtotheactiveconfiguration:
| switch(config)# | class | all reset |     |
| --------------- | ----- | --------- | --- |
| Command History |       |           |     |
Classifierpolicies|136

Release

10.07 or earlier

Modification

--

Command Information

Platforms

Command context

Authority

All platforms

config

Administrators or local user group members with execution
rights for this command.

clear policy hitcounts
clear policy hitcounts { all | [<POLICY-NAME>] [[interface <IF-NAME> [in|routed-in]] |
[vlan <VLAN-ID> [in]]] | global }

Description

Clears the policy hit count statistics.

Parameter

all

Description

Selects all policies.

<POLICY-NAME>

Specifies the policy name.

interface <IF-NAME>

Specifies the interface name.

vlan <VLAN-ID>

Specifies the VLAN.

in

routed-in

global

Examples

Specifies the inbound (ingress) traffic direction.

Selects the routed in traffic direction. Not applicable to a policy
applied to a VLAN.

Selects the globally applied policy.

Clearing policy hit counts and then showing the policy hit counts (statistics):

switch# clear policy hitcounts my_policy int 1/1/1 in
switch# show policy hitcounts my_policy
Statistics for Policy my_policy:
Interface 1/1/1* (in):

Hit Count

Configuration

10 class ipv6 my_class1 action dscp af21 action drop

0

10 match any any any count

* policy statistics are shared among each context type (interface, VLAN).

For routed ingress, they are only shared within the same VRF.
Use 'policy NAME copy' to create a new policy for separate statistics.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

137

Clearingthegloballyappliedpolicyhitcountsandthenshowingtheglobalpolicyhitcounts(statistics):
| switch#    | clear   | policy         |           | hitcounts     | global      |       |     |
| ---------- | ------- | -------------- | --------- | ------------- | ----------- | ----- | --- |
| switch#    | show    | policy         | hitcounts |               | global      |       |     |
| Statistics |         | for Policy     |           | global1:      |             |       |     |
| Global     | Policy: |                |           |               |             |       |     |
|            |         | Hit Count      |           | Configuration |             |       |     |
| 10         | class   | ipv6 my_class1 |           | action        | mirror      |       |     |
|            |         |                | 0         | 10 match      | any any any | count |     |
* policy statistics are shared among each context type (interface, VLAN).
| For | routed | ingress, |     | they | are only shared | within | the same VRF. |
| --- | ------ | -------- | --- | ---- | --------------- | ------ | ------------- |
Use 'policy NAME copy' to create a new policy for separate statistics.
ClearinghitcountsforpolicyMY_IPv6_PolicyappliedtoVLAN10(ingress):
| switch# | clear | policy |     | hitcounts | My_IPv6_Policy | vlan | 10 in |
| ------- | ----- | ------ | --- | --------- | -------------- | ---- | ----- |
Clearinghitcountsforallpolicies:
| switch#        | clear       | policy               |     | hitcounts | all          |     |     |
| -------------- | ----------- | -------------------- | --- | --------- | ------------ | --- | --- |
| Command        | History     |                      |     |           |              |     |     |
| Release        |             |                      |     |           | Modification |     |     |
| 10.07orearlier |             |                      |     |           | --           |     |     |
| Command        | Information |                      |     |           |              |     |     |
| Platforms      |             | Command              |     | context   | Authority    |     |     |
| Allplatforms   |             | Operator(>)orManager |     |           |              |     |     |
(#)
policy
policy <POLICY-NAME>
[<SEQUENCE-NUMBER>]
| class | {ip|ipv6|mac}      |                   |     | <CLASS-NAME> |                    |                     |                    |
| ----- | ------------------ | ----------------- | --- | ------------ | ------------------ | ------------------- | ------------------ |
|       | action             | {<REMARK-ACTIONS> |     |              | | <POLICE-ACTIONS> |                     | | <OTHER-ACTIONS>} |
|       | [{<REMARK-ACTIONS> |                   |     | |            | <POLICE-ACTIONS>   | | <OTHER-ACTIONS>}] |                    |
[<SEQUENCE-NUMBER>]
| comment |     | ... |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
Description
Createsormodifiesclassifierpolicyandpolicyentries.Apolicyismadeupofoneormorepolicyentries
orderedandprioritizedbysequencenumbers.EachentryhasanIPv4/IPv6/MACclassandzeroormore
policyactionsassociatedwithit.
Apolicymustbeappliedusingtheapplycommand.
Thenoformofthecommandcanbeusedtodeleteeitherapolicy(usenowiththepolicycommand)or
anindividualpolicyentry(usenowiththesequencenumber).
Classifierpolicies|138

Parameter

<POLICY-NAME>

<SEQUENCE-NUMBER>

comment

class {ip|ipv6|mac} <CLASS-NAME>

<REMARK-ACTIONS>

pcp <PCP-VALUE>

ip-precedence <IP-PRECEDENCE-VALUE>

dscp <DSCP-VALUE>

Description

Specifies the name of the policy.

Specifies a sequence number for the policy entry.
Optional. Range: 1 to 4294967295.

Stores the remaining entered text as a policy entry
comment.

Specifies a type of class, ip for IPv4, ipv6 for IPv6 and
mac for a MAC policy. And specifies a class name.

Remark actions can be any of the following options:
{pcp <PRIORITY> | ip-precedence <IP-
PRECEDENCE_VALUE> | dscp <DSCP-VALUE> | local-
priority <LOCAL-PRIORITY-VALUE>} where:

Specifies the Priority Code Point (PCP) value. Range: 0
to 7.

Specifies the numeric IP precedence value. Range: 0
to 7.

Specifies a Differentiated Services Code Point (DSCP)
value. Enter either a numeric value (0 to 63) or a
keyword as follows:

n AF11 - DSCP 10 (Assured Forwarding Class 1, low

drop probability)

n

n AF12 - DSCP 12 (Assured Forwarding Class 1,

medium drop probability)

n AF13 - DSCP 14 (Assured Forwarding Class 1, high

drop probability)

n AF21 - DSCP 18 (Assured Forwarding Class 2, low

drop probability)

n AF22 - DSCP 20 (Assured Forwarding Class 2,

medium drop probability)

n AF23 - DSCP 22 (Assured Forwarding Class 2, high

drop probability)

n AF31 - DSCP 26 (Assured Forwarding Class 3, low

drop probability)

n AF32 - DSCP 28 (Assured Forwarding Class 3,

medium drop probability)

n AF33 - DSCP 30 (Assured Forwarding Class 3, high

drop probability)

n AF41 - DSCP 34 (Assured Forwarding Class 4, low

drop probability)

n AF42 - DSCP 36 (Assured Forwarding Class 4,

medium drop probability)

n AF43 - DSCP 38 (Assured Forwarding Class 4, high

drop probability)

n CS0 - DSCP 0 (Class Selector 0: Default)
n CS1 - DSCP 8 (Class Selector 1: Scavenger)

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

139

Parameter

Description

n CS2 - DSCP 16 (Class Selector 2: OAM)
n CS3 - DSCP 24 (Class Selector 3: Signaling)
n CS4 - DSCP 32 (Class Selector 4: Real time)
n CS5 - DSCP 40 (Class Selector 5: Broadcast video)
n CS6 - DSCP 48 (Class Selector 6: Network control)
n CS7 - DSCP 56 (Class Selector 7)
n EF - DSCP 46 (Expedited Forwarding)

local-priority

<LOCAL-PRIORITY-VALUE>

Specifies a local priority value. Range: 0 to 7.

<POLICE-ACTIONS>

cir kbps <RATE-KBPS>

cbs <BYTES>

exceed

Police actions can be the following {cir <RATE-
BPS>cbs <BYTES> exceed} where:

Specifies a Committed Information Rate value in
Kilobits per second. Range: 1 to 4294967295.

Specifies a Committed Burst Size value in bytes.
Range: 1 to 4294967295.

Specifies action to take on packets that exceed the
rate limit.

<OTHER-ACTIONS>

Other actions can be the following:

drop

Usage

Specifies drop traffic.

n An applied policy will process a packet sequentially against policy entries in the list until the last

policy entry in the list has been evaluated or the packet matches an entry.

n Entering an existing <POLICY-NAME> value will cause the existing policy to be modified, with any new
<SEQUENCE-NUMBER> value creating an additional policy entry, and any existing <SEQUENCE-NUMBER>
value replacing the existing policy entry with the same sequence number.

n If no sequence number is specified, a new policy entry will be appended to the end of the entry list

with a sequence number equal to the highest policy entry currently in the list plus 10.

Examples

Creating a policy with several entries:

switch(config)# policy MY_POLICY
switch(config-policy)# 10 class ipv6 MY_CLASS1 action dscp af21 action drop
switch(config-policy)# 20 class ip MY_CLASS3 action mirror 1
switch(config-policy)# exit
switch(config)# show policy
Name

Sequence Comment

Class Type

action

-------------------------------------------------------------------------------

MY_POLICY

10

MY_CLASS1 ipv6

drop

Classifier policies | 140

dscp AF21
20
|     | MY_CLASS3 | ipv4 |     |     |     |     |
| --- | --------- | ---- | --- | --- | --- | --- |
mirror 1
Addingacommenttoanexistingpolicyentry:
| switch(config)#        | policy   | MY_POLICY  |                |       |             |     |
| ---------------------- | -------- | ---------- | -------------- | ----- | ----------- | --- |
| switch(config-policy)# |          | 20 comment | MY_TEST_POLICY |       |             |     |
| switch(config-policy)# |          | exit       |                |       |             |     |
| switch(config)#        | show     | policy     |                |       |             |     |
| Name                   | Sequence | Comment    |                | Class | Type action |     |
-------------------------------------------------------------------------------
| MY_POLICY | 10  |                |     | MY_CLASS1 | ipv6 drop   | dscp AF21 |
| --------- | --- | -------------- | --- | --------- | ----------- | --------- |
|           | 20  | MY_TEST_POLICY |     | MY_CLASS3 | ipv4 mirror | 1         |
Removingacommentfromanexistingpolicyentry:
| switch(config)#        | policy   | MY_POLICY |         |      |        |     |
| ---------------------- | -------- | --------- | ------- | ---- | ------ | --- |
| switch(config-policy)# |          | no 20     | comment |      |        |     |
| switch(config-policy)# |          | exit      |         |      |        |     |
| switch(config)#        | show     | policy    |         |      |        |     |
| Name                   | Sequence | Comment   | Class   | Type | action |     |
-------------------------------------------------------------------------------
| MY_POLICY | 10  |     | MY_CLASS1 | ipv6 | drop dscp AF21 |     |
| --------- | --- | --- | --------- | ---- | -------------- | --- |
|           | 20  |     | MY_CLASS3 | ipv4 | mirror 1       |     |
Adding/Replacingapolicyentryinanexistingpolicy:
| switch(config)# | policy | MY_POLICY |     |     |     |     |
| --------------- | ------ | --------- | --- | --- | --- | --- |
switch(config-policy)# 10 class ip MY_CLASS3 action drop action dscp af21
| switch(config-policy)# |      | exit   |     |     |     |     |
| ---------------------- | ---- | ------ | --- | --- | --- | --- |
| switch(config)#        | show | policy |     |     |     |     |
Name
| Sequence | Comment |     |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
MY_POLICY
10
|     | MY_CLASS3 | ipv4 |     |     |     |     |
| --- | --------- | ---- | --- | --- | --- | --- |
drop
dscp AF21
20
|     | MY_CLASS3 | ipv4 |     |     |     |     |
| --- | --------- | ---- | --- | --- | --- | --- |
mirror 1
Removingapolicyentry:
| switch(config)#        | policy | MY_POLICY |     |     |     |     |
| ---------------------- | ------ | --------- | --- | --- | --- | --- |
| switch(config-policy)# |        | no 10     |     |     |     |     |
| switch(config-policy)# |        | exit      |     |     |     |     |
| switch(config)#        | show   | policy    |     |     |     |     |
Name
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 141

| Sequence | Comment |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
MY_POLICY
20
|     | MY_CLASS3 | ipv4 |     |     |     |
| --- | --------- | ---- | --- | --- | --- |
mirror 1
Removingapolicy:
switch(config)#
|                 | no       | policy MY_POLICY |       |             |     |
| --------------- | -------- | ---------------- | ----- | ----------- | --- |
| switch(config)# | show     | policy           |       |             |     |
| Name            | Sequence | Comment          | Class | Type action |     |
-------------------------------------------------------------------------------
| MY_POLICY | 22  |     | MY_CLASS3 | ipv4 mirror | 1   |
| --------- | --- | --- | --------- | ----------- | --- |
ThepolicerexceedDSCPactioncannotbecombinedwithotheractionsinthesamepolicyentry,but
otherentriesinthepolicymayuseotheractions.
Forexample,thisconfigurationisvalid:
| switch(config)# | policy | my_policy |     |     |     |
| --------------- | ------ | --------- | --- | --- | --- |
switch(config-policy)# 10 class ip my_class action cir kbps 1000 cbs 15625 exceed
dscp EF
Butthisisnotbecauseitaddsasecondaryactionwithinthesamepolicyentry:
6300(config-policy)# 10 class ip my_class action cir kbps 1000 cbs 15625 exceed
| dscp EF | action mirror | 1   |     |     |     |
| ------- | ------------- | --- | --- | --- | --- |
Invalidinput:action
| Command        | History     |         |              |     |     |
| -------------- | ----------- | ------- | ------------ | --- | --- |
| Release        |             |         | Modification |     |     |
| 10.07orearlier |             |         | --           |     |     |
| Command        | Information |         |              |     |     |
| Platforms      | Command     | context | Authority    |     |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
|     | Thepolicycommand |     | rightsforthiscommand. |     |     |
| --- | ---------------- | --- | --------------------- | --- | --- |
takesyouintothe
config-policycontext
whereyouenterthe
policyentries.
policy copy
Classifierpolicies|142

| policy <POLICY-NAME> | copy | <DESTINATION-POLICY> |     |     |
| -------------------- | ---- | -------------------- | --- | --- |
Description
Copiesapolicytoanewdestinationpolicyoroverwritesanexistingpolicy.Copyingapolicycopiesallits
entriesaswell.
| Parameter            |     |     | Description                             |     |
| -------------------- | --- | --- | --------------------------------------- | --- |
| <POLICY-NAME>        |     |     | Specifiesthepolicytobecopied.           |     |
| <DESTINATION-POLICY> |     |     | Specifiesthenameofthedestinationpolicy. |     |
Examples
Copyingapolicy:
switch(config)#
|                 | policy | MY_POLICY   | copy MY_POLICY2 |     |
| --------------- | ------ | ----------- | --------------- | --- |
| switch(config)# | do     | show policy |                 |     |
Name
| Sequence | Comment |     |     |     |
| -------- | ------- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
MY_POLICY
2
|     | my_class3 | ipv4 |     |     |
| --- | --------- | ---- | --- | --- |
mirror 1
-------------------------------------------------------------------------------
MY_POLICY2
2
|     | my_class3 | ipv4 |     |     |
| --- | --------- | ---- | --- | --- |
mirror 1
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
config
Allplatforms Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
| policy resequence    |            |                    |     |             |
| -------------------- | ---------- | ------------------ | --- | ----------- |
| policy <POLICY-NAME> | resequence | <STARTING-SEQ-NUM> |     | <INCREMENT> |
Description
Resequencesnumberinginapolicy.
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 143

| Parameter |     |     | Description |     |
| --------- | --- | --- | ----------- | --- |
<POLICY-NAME> Specifiesthepolicywhereyouwanttoresequencepolicyentries.
<STARTING-SEQ-NUM> Specifiesthesequencenumbertostartresequencingfrom.
| <INCREMENT> |     |     | Specifieshowmuchtoincrementthesequencenumbersby. |     |
| ----------- | --- | --- | ------------------------------------------------ | --- |
Examples
Resequencingapolicy:
| switch(config)# | policy | MY_POLICY   | resequence | 1 1 |
| --------------- | ------ | ----------- | ---------- | --- |
| switch(config)# | do     | show policy |            |     |
Name
| Sequence | Comment |     |     |     |
| -------- | ------- | --- | --- | --- |
Class Type
action
-------------------------------------------------------------------------------
MY_POLICY
1
|     | MY_CLASS3 | ipv4 |     |     |
| --- | --------- | ---- | --- | --- |
drop
dscp AF21
2
|     | MY_CLASS3 | ipv4 |     |     |
| --- | --------- | ---- | --- | --- |
mirror 1
| Command History     |         |         |              |     |
| ------------------- | ------- | ------- | ------------ | --- |
| Release             |         |         | Modification |     |
| 10.07orearlier      |         |         | --           |     |
| Command Information |         |         |              |     |
| Platforms           | Command | context | Authority    |     |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
policy reset
| policy <POLICY-NAME> | reset |     |     |     |
| -------------------- | ----- | --- | --- | --- |
Description
Changestheuser-specifiedpolicyconfigurationtomatchtheactivepolicyconfiguration.Usethis
commandwhenadiscrepancyexistsbetweenwhattheuserconfiguredandwhatisactiveandaccepted
bythesystem.
| Parameter     |     |     | Description                  |     |
| ------------- | --- | --- | ---------------------------- | --- |
| <POLICY-NAME> |     |     | Specifiesthepolicytobereset. |     |
Classifierpolicies|144

Examples
Resettingapolicy:
switch(config)#
|                     | policy  | MY_POLICY | reset        |
| ------------------- | ------- | --------- | ------------ |
| Command History     |         |           |              |
| Release             |         |           | Modification |
| 10.07orearlier      |         |           | --           |
| Command Information |         |           |              |
| Platforms           | Command | context   | Authority    |
Allplatforms config Administratorsorlocalusergroupmemberswithexecution
rightsforthiscommand.
show class
show class [ip | ipv6 | mac] [<CLASS-NAME>] [commands] [configuration] [vsx-peer]
Description
Showsclassconfigurationinformation.
Allparametersareoptional.
| Parameter  |        |     | Description |
| ---------- | ------ | --- | ----------- |
| [ip | ipv6 | | mac] |     |             |
Selectstheclasstypeforthedisplay:ipforIPv4,ipv6forIPv6,or
macforMACclasses.
| <CLASS-NAME> |     |     | Specifiestheclassname. |
| ------------ | --- | --- | ---------------------- |
commands SpecifieswhethertodisplayoutputastheCLIcommandsshowing
theconfiguredclassentries.
configuration Specifieswhethertodisplayclassesthathavebeenconfiguredby
theuser,eveniftheyarenotactiveduetoissueswiththe
commandparametersorhardwareissues.Thisparameteris
usefulduringamismatchbetweentheenteredconfigurationand
theprevioussuccessfullyprogrammed(active)classes.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showingallclassconfiguration:
| switch# show | class |     |     |
| ------------ | ----- | --- | --- |
Type Name
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 145

|     | Sequence |     | Comment     |            |            |     |             |            |
| --- | -------- | --- | ----------- | ---------- | ---------- | --- | ----------- | ---------- |
|     |          |     | action      |            |            |     | L3 Protocol |            |
|     |          |     | Source      | IP address |            |     | Source      | L4 Port(s) |
|     |          |     | Destination |            | IP address |     | Destination | L4 Port(s) |
|     |          |     | Additional  | Parameters |            |     |             |            |
---------------------------------------------------------------
|     | ipv4 | MY_IPV4_CLASS |          |       |       |         |      |     |
| --- | ---- | ------------- | -------- | ----- | ----- | ------- | ---- | --- |
|     |      | 10            | my first | class | entry | comment |      |     |
|     |      |               | match    |       |       |         | icmp |     |
192.168.0.1/255.255.255.0
192.168.1.1/255.255.255.0
|     |     |     | VLAN:                     | 1     |       |         |        |     |
| --- | --- | --- | ------------------------- | ----- | ----- | ------- | ------ | --- |
|     |     | 20  | my second                 | class | entry | comment |        |     |
|     |     |     | ignore                    |       |       |         | tcp    |     |
|     |     |     | 10.100.0.10/255.255.255.0 |       |       |         | < 3000 |     |
|     |     |     | 10.100.1.10/255.255.255.0 |       |       |         | > 2000 |     |
|     |     |     | VLAN:                     | 1     |       |         |        |     |
----------------------------------------------------------------------
ShowingclassconfigurationfortheIPv4classMY_IPV4_CLASSasCLIcommands:
|     | switch# | show               | class | ip MY_IPV4_CLASS |     |     | commands |     |
| --- | ------- | ------------------ | ----- | ---------------- | --- | --- | -------- | --- |
|     | class   | ip "MY_IPV4_CLASS" |       |                  |     |     |          |     |
10 match icmp 192.168.0.1/255.255.255.0 192.168.1.1/255.255.255.0 vlan 1
|     | 10  | comment | my  | first class | entry | comment |     |     |
| --- | --- | ------- | --- | ----------- | ----- | ------- | --- | --- |
20 ignore tcp 10.100.0.10/255.255.255.0 lt 3000 10.100.1.10/255.255.255.0 gt
|                |     | 2000        | vlan 1               |         |       |               |     |     |
| -------------- | --- | ----------- | -------------------- | ------- | ----- | ------------- | --- | --- |
|                | 20  | comment     | my                   | second  | class | entry comment |     |     |
| Command        |     | History     |                      |         |       |               |     |     |
| Release        |     |             |                      |         |       | Modification  |     |     |
| 10.07orearlier |     |             |                      |         |       | --            |     |     |
| Command        |     | Information |                      |         |       |               |     |     |
| Platforms      |     |             | Command              | context |       | Authority     |     |     |
| Allplatforms   |     |             | Operator(>)orManager |         |       |               |     |     |
(#)
| show | policy |     |     |     |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
Syntaxthatshowsinformationforallpolicies:
| show | policy | [commands] |     | [configuration] |     |     | [vsx-peer] |     |
| ---- | ------ | ---------- | --- | --------------- | --- | --- | ---------- | --- |
SyntaxthatfiltersbypoliciesappliedtoaninterfaceorVLAN:
show policy [interface <IF-NAME> [in | out | routed-in] | vlan <VLAN-ID> [in] | vni <VNI-
ID> [routed-in]]
|     |     | [commands] |     | [configuration] |     |     | [vsx-peer] |     |
| --- | --- | ---------- | --- | --------------- | --- | --- | ---------- | --- |
Syntaxthatfiltersbythenamedpolicy:
show policy <POLICY-NAME> [commands] [configuration] [vsx-peer]
Syntaxthatfiltersbythegloballyappliedpolicy:
| show | policy | global | [commands] |     | [configuration] |     | [vsx-peer] |     |
| ---- | ------ | ------ | ---------- | --- | --------------- | --- | ---------- | --- |
Syntaxthatshowsstatisticalinformationintheformofhitcounts:
Classifierpolicies|146

show policy hitcounts <POLICY-NAME> [interface <IF-NAME> [in | routed-in] |
|     |     | vlan <VLAN-ID> | [in]| vni | <VNI-ID> [routed-in]] | [vsx-peer] |
| --- | --- | -------------- | --------- | --------------------- | ---------- |
Syntaxthatshowsstatisticalinformationintheformofhitcountsforthegloballyappliedpolicy:
| show policy | hitcounts | global [vsx-peer] |     |     |     |
| ----------- | --------- | ----------------- | --- | --- | --- |
Description
Showsinformationaboutyourdefinedpoliciesandwheretheyhavebeenapplied.Whenshow policyis
enteredwithoutparameters,informationforallpoliciesisshown.Theparametersfilterthelistof
policiesforwhichinformationisshown.
Availablefilteringincludes:
n Thecontentofaspecificpolicy.
n Allpoliciesappliedtoaspecificinterface.
n AllpoliciesappliedtoaspecificVLAN.
n AllpoliciesappliedtoaspecificVNI.
n Thegloballyappliedpolicy.
Todisplaypolicystatistics,usetheshow policy hitcountsformofthiscommand.
Whenapolicyisappliedtoaphysicalinterfaceorlagusingcommandapplypolicy,withtheper-interface
parameterincluded,uniqueinstancesofthepolicyareappliedtoeachphysicalinterfaceportorLAG.Theunique
instanceofapolicyhasaparent-childrelationshipwiththepolicyfromwhichitwascreated.Theshowpolicy
commandshowsinformationabouttheparentpolicynottheuniqueinstances.
Ifapolicycontainsanyclassentrieswiththecountkeywordandpolicyentrieswiththeciraction,andthepolicy
isappliedtomultiplephysicalorvirtualinterfacesinthesamedirection,exceptfortheroutedingressdirection,
thestatisticswillbeaggregated.Intheroutedingressdirection,thestatisticswillbeaggregatedinmultiple
physicalorvirtualinterfacesinthesameVRF.Ifseparatestatisticsfordifferentphysicalorvirtualinterfacesare
required,thenanotherpolicyshouldbecreated.Alternatively,inthecaseofphysicalinterfacesorLAGs,apolicy
appliedwithper-interfacesetcanbeused.
| Parameter      |           |     | Description                                 |     |     |
| -------------- | --------- | --- | ------------------------------------------- | --- | --- |
| interface      | <IF-NAME> |     | Specifiestheinterfacename.                  |     |     |
| vlan <VLAN-ID> |           |     | SpecifiestheVLAN.                           |     |     |
| vni<VNI-ID>    |           |     | SpecifiestheVNI.                            |     |     |
| in             |           |     | Selectstheinbound(ingress)trafficdirection. |     |     |
routed-in Selectstheroutedintrafficdirection.Notapplicabletoapolicy
appliedtoaVLAN.
| <POLICY-NAME> |     |     | Specifiesthepolicyname.                            |     |     |
| ------------- | --- | --- | -------------------------------------------------- | --- | --- |
| commands      |     |     | Causesthepolicydefinitiontobeshownasthecommandsand |     |     |
parametersusedtocreateitratherthanintabularform.
configuration Causestheuser-configuredpoliciesbeshownasentered,evenif
thepoliciesarenotactiveduetopolicy-definitioncommand
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 147

| Parameter |     |     |     |     | Description |     |
| --------- | --- | --- | --- | --- | ----------- | --- |
issuesorhardwareissues.Thisparameterisusefulifthereisa
mismatchbetweentheenteredconfigurationandtheprevious
successfullyprogrammed(active)policiesconfiguration.
global
Selectsthegloballyappliedpolicy.
hitcounts Selectsthepolicyhitcounts(statistics).Theswitchdisplaysthe
numberofacceptedbytes/conformedbytes(greenandyellow
bytes)as0kbps.
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showinginformationforallpolicies:
| switch# | show | policy |     |     |     |     |
| ------- | ---- | ------ | --- | --- | --- | --- |
Name
| Sequence |     | Comment |      |     |     |     |
| -------- | --- | ------- | ---- | --- | --- | --- |
|          |     | Class   | Type |     |     |     |
action
-------------------------------------------------------------------------------
my_policy
|     | 10  | QOS class |      |      |     |     |
| --- | --- | --------- | ---- | ---- | --- | --- |
|     |     | class1    | ipv4 |      |     |     |
|     |     |           | dscp | af21 |     |     |
drop
|     | 20  | PBR policy. |      |       |     |     |
| --- | --- | ----------- | ---- | ----- | --- | --- |
|     |     | class2      | ipv4 |       |     |     |
|     |     |             | pbr  | mypbr |     |     |
-------------------------------------------------------------------------------
Showingapolicyascommands:
| switch# | show | policy | commands |     |     |     |
| ------- | ---- | ------ | -------- | --- | --- | --- |
policy my_policy
|     | 10  | class | ip class1 | action | dscp af21 | action drop |
| --- | --- | ----- | --------- | ------ | --------- | ----------- |
|     | 20  | class | ip class2 | action | pbr mypbr |             |
Showingthegloballyappliedpolicy:
| switch# | show | policy | global | commands |     |     |
| ------- | ---- | ------ | ------ | -------- | --- | --- |
policy global1
|       | 10 class | ip        | my_class1 | action | drop |     |
| ----- | -------- | --------- | --------- | ------ | ---- | --- |
| apply | policy   | my_policy |           | in     |      |     |
Showingpolicyhitcounts(statistics)forthegloballyappliedpolicy::
| switch#    | show | policy     | hitcounts  |     | global |     |
| ---------- | ---- | ---------- | ---------- | --- | ------ | --- |
| Statistics |      | for Policy | My_Policy: |     |        |     |
Classifierpolicies|148

global (in):
| Matched  | Packets        | Configuration |                |           |       |     |     |     |
| -------- | -------------- | ------------- | -------------- | --------- | ----- | --- | --- | --- |
| 10 class | ip My_ip_Class |               |                |           |       |     |     |     |
|          |                | 0 10          | match tcp any  | any ack   | count |     |     |     |
|          |                | - 20          | match udp any  | lt 8 any  |       |     |     |     |
|          |                | 0 30          | match icmp any | 10.1.1.10 | count |     |     |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|     |     | 0 10 | match tcp any         | any count | [ 0 kbps  | conform  | ]       |     |
| --- | --- | ---- | --------------------- | --------- | --------- | -------- | ------- | --- |
|     |     | 0 20 | match icmpv6 1000::10 |           | any count | [ 0 kbps | conform | ]   |
Showingpolicyhitcounts(statistics)forapolicyappliedeverywhere(with1/1/1and1/1/5beingapplied
perinterface):
| switch#    | show policy    | hitcounts     | My_Policy      |           |       |     |     |     |
| ---------- | -------------- | ------------- | -------------- | --------- | ----- | --- | --- | --- |
| Statistics | for Policy     | My_Policy:    |                |           |       |     |     |     |
| Interface  | 1/1/1,lag1     | (in):         |                |           |       |     |     |     |
| Matched    | Packets        | Configuration |                |           |       |     |     |     |
| 10 class   | ip My_ip_Class |               |                |           |       |     |     |     |
|            |                | 0 10          | match tcp any  | any ack   | count |     |     |     |
|            |                | - 20          | match udp any  | lt 8 any  |       |     |     |     |
|            |                | 0 30          | match icmp any | 10.1.1.10 | count |     |     |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|           |                | - 10          | match tcp any         | any ack   |           |          |         |     |
| --------- | -------------- | ------------- | --------------------- | --------- | --------- | -------- | ------- | --- |
|           |                | 0 20          | match icmpv6 1000::10 |           | any count | [ 0 kbps | conform | ]   |
| Interface | 1/1/4          | (in):         |                       |           |           |          |         |     |
| Matched   | Packets        | Configuration |                       |           |           |          |         |     |
| 10 class  | ip My_ip_Class |               |                       |           |           |          |         |     |
|           |                | 0 10          | match tcp any         | any ack   | count     |          |         |     |
|           |                | - 20          | match udp any         | lt 8 any  |           |          |         |     |
|           |                | 0 30          | match icmp any        | 10.1.1.10 | count     |          |         |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|           |                | 0 10          | match tcp any         | any count | [ 0 kbps  | conform  | ]       |     |
| --------- | -------------- | ------------- | --------------------- | --------- | --------- | -------- | ------- | --- |
|           |                | 0 20          | match icmpv6 1000::10 |           | any count | [ 0 kbps | conform | ]   |
| Interface | 1/1/5          | (in):         |                       |           |           |          |         |     |
| Matched   | Packets        | Configuration |                       |           |           |          |         |     |
| 10 class  | ip My_ip_Class |               |                       |           |           |          |         |     |
|           |                | 0 10          | match tcp any         | any ack   | count     |          |         |     |
|           |                | - 20          | match udp any         | lt 8 any  |           |          |         |     |
|           |                | 0 30          | match icmp any        | 10.1.1.10 | count     |          |         |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|           |                   | 0 10          | match tcp any         | any count | [ 0 kbps  | conform  | ]       |     |
| --------- | ----------------- | ------------- | --------------------- | --------- | --------- | -------- | ------- | --- |
|           |                   | 0 20          | match icmpv6 1000::10 |           | any count | [ 0 kbps | conform | ]   |
| interface | 1/1/2.10,1/1/3.10 |               | (in):                 |           |           |          |         |     |
| Matched   | Packets           | Configuration |                       |           |           |          |         |     |
| 10 class  | ip My_ip_Class    |               |                       |           |           |          |         |     |
|           |                   | 0 10          | match tcp any         | any ack   | count     |          |         |     |
|           |                   | - 20          | match udp any         | lt 8 any  |           |          |         |     |
|           |                   | 0 30          | match icmp any        | 10.1.1.10 | count     |          |         |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|     |     | - 10 | match tcp any         | any ack |           |          |         |     |
| --- | --- | ---- | --------------------- | ------- | --------- | -------- | ------- | --- |
|     |     | 0 20 | match icmpv6 1000::10 |         | any count | [ 0 kbps | conform | ]   |
...
| Statistics | for Policy | My_Policy:    |     |     |     |     |     |     |
| ---------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
| Interface  | 1/1/1,lag1 | (in):         |     |     |     |     |     |     |
| Matched    | Packets    | Configuration |     |     |     |     |     |     |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 149

| 10 class | ip My_ip_Class |      |                |           |       |       |     |     |
| -------- | -------------- | ---- | -------------- | --------- | ----- | ----- | --- | --- |
|          |                | 0 10 | match tcp any  | any ack   | count |       |     |     |
|          |                | - 20 | match udp any  | lt 8      | any   |       |     |     |
|          |                | 0 30 | match icmp any | 10.1.1.10 |       | count |     |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|           |                 | - 10          | match tcp any  | any ack   |       |                |         |     |
| --------- | --------------- | ------------- | -------------- | --------- | ----- | -------------- | ------- | --- |
|           |                 | 0 20          | match icmpv6   | 1000::10  | any   | count [ 0 kbps | conform | ]   |
| Interface | 1/1/4           | (in):         |                |           |       |                |         |     |
|           | Matched Packets | Configuration |                |           |       |                |         |     |
| 10 class  | ip My_ip_Class  |               |                |           |       |                |         |     |
|           |                 | 0 10          | match tcp any  | any ack   | count |                |         |     |
|           |                 | - 20          | match udp any  | lt 8      | any   |                |         |     |
|           |                 | 0 30          | match icmp any | 10.1.1.10 |       | count          |         |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|           |                 | 0 10          | match tcp any  | any count | [ 0   | kbps conform   | ]       |     |
| --------- | --------------- | ------------- | -------------- | --------- | ----- | -------------- | ------- | --- |
|           |                 | 0 20          | match icmpv6   | 1000::10  | any   | count [ 0 kbps | conform | ]   |
| Interface | 1/1/5           | (in):         |                |           |       |                |         |     |
|           | Matched Packets | Configuration |                |           |       |                |         |     |
| 10 class  | ip My_ip_Class  |               |                |           |       |                |         |     |
|           |                 | 0 10          | match tcp any  | any ack   | count |                |         |     |
|           |                 | - 20          | match udp any  | lt 8      | any   |                |         |     |
|           |                 | 0 30          | match icmp any | 10.1.1.10 |       | count          |         |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|           |                   | 0 10          | match tcp any  | any count | [ 0   | kbps conform   | ]       |     |
| --------- | ----------------- | ------------- | -------------- | --------- | ----- | -------------- | ------- | --- |
|           |                   | 0 20          | match icmpv6   | 1000::10  | any   | count [ 0 kbps | conform | ]   |
| interface | 1/1/2.10,1/1/3.10 |               | (in):          |           |       |                |         |     |
|           | Matched Packets   | Configuration |                |           |       |                |         |     |
| 10 class  | ip My_ip_Class    |               |                |           |       |                |         |     |
|           |                   | 0 10          | match tcp any  | any ack   | count |                |         |     |
|           |                   | - 20          | match udp any  | lt 8      | any   |                |         |     |
|           |                   | 0 30          | match icmp any | 10.1.1.10 |       | count          |         |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|     |     | - 10 | match tcp any | any ack  |     |                |         |     |
| --- | --- | ---- | ------------- | -------- | --- | -------------- | ------- | --- |
|     |     | 0 20 | match icmpv6  | 1000::10 | any | count [ 0 kbps | conform | ]   |
...
Showingpolicyhitcounts(statistics)forapolicyappliedonphysicalinterfacesandLAGs:
switch#
|            | show policy     | hitcounts     | My_Policy      | interface |       | 1/1/1 |     |     |
| ---------- | --------------- | ------------- | -------------- | --------- | ----- | ----- | --- | --- |
| Statistics | for Policy      | My_Policy:    |                |           |       |       |     |     |
| Interface  | 1/1/1,lag1      | (in):         |                |           |       |       |     |     |
|            | Matched Packets | Configuration |                |           |       |       |     |     |
| 10 class   | ip My_ip_Class  |               |                |           |       |       |     |     |
|            |                 | 0 10          | match tcp any  | any ack   | count |       |     |     |
|            |                 | - 20          | match udp any  | lt 8      | any   |       |     |     |
|            |                 | 0 30          | match icmp any | 10.1.1.10 |       | count |     |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|     |     | 0 10 | match tcp any | any count | [ 0 | kbps conform   | ]       |     |
| --- | --- | ---- | ------------- | --------- | --- | -------------- | ------- | --- |
|     |     | 0 20 | match icmpv6  | 1000::10  | any | count [ 0 kbps | conform | ]   |
Showingpolicyhitcounts(statistics)forapolicyappliedonVLANs:
| switch#    | show policy | hitcounts  | My_Policy | vlan | 30  |     |     |     |
| ---------- | ----------- | ---------- | --------- | ---- | --- | --- | --- | --- |
| Statistics | for Policy  | My_Policy: |           |      |     |     |     |     |
Classifierpolicies|150

| vlan 30  | (in):          |               |          |           |       |     |
| -------- | -------------- | ------------- | -------- | --------- | ----- | --- |
| Matched  | Packets        | Configuration |          |           |       |     |
| 10 class | ip My_ip_Class |               |          |           |       |     |
|          |                | 0 10 match    | tcp any  | any ack   | count |     |
|          |                | - 20 match    | udp any  | lt 8 any  |       |     |
|          |                | 0 30 match    | icmp any | 10.1.1.10 | count |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|     |     | 0 10 match | tcp any | any count | [ 0 kbps conform   | ]         |
| --- | --- | ---------- | ------- | --------- | ------------------ | --------- |
|     |     | 0 20 match | icmpv6  | 1000::10  | any count [ 0 kbps | conform ] |
Showingpolicyhitcounts(statistics)forapolicyappliedoninterfaceVLANs:
| switch#    | show policy | hitcounts  | My_Policy | interface | vlan10 |     |
| ---------- | ----------- | ---------- | --------- | --------- | ------ | --- |
| Statistics | for Policy  | My_Policy: |           |           |        |     |
VRF red
| interface | vlan 10 (routed-in): |               |          |           |       |     |
| --------- | -------------------- | ------------- | -------- | --------- | ----- | --- |
| Matched   | Packets              | Configuration |          |           |       |     |
| 10 class  | ip My_ip_Class       |               |          |           |       |     |
|           |                      | 0 10 match    | tcp any  | any ack   | count |     |
|           |                      | - 20 match    | udp any  | lt 8 any  |       |     |
|           |                      | 0 30 match    | icmp any | 10.1.1.10 | count |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|     |     | 0 10 match | tcp any | any count | [ 0 kbps conform   | ]         |
| --- | --- | ---------- | ------- | --------- | ------------------ | --------- |
|     |     | 0 20 match | icmpv6  | 1000::10  | any count [ 0 kbps | conform ] |
Showingpolicyhitcounts(statistics)forapolicyappliedoninterfaceVLANsforaspecificVRF:
| switch#    | show policy | hitcounts  | My_Policy | vrf red | routed-in |     |
| ---------- | ----------- | ---------- | --------- | ------- | --------- | --- |
| Statistics | for Policy  | My_Policy: |           |         |           |     |
VRF red
| interface | vlan 10 (routed-in): |               |          |           |       |     |
| --------- | -------------------- | ------------- | -------- | --------- | ----- | --- |
| Matched   | Packets              | Configuration |          |           |       |     |
| 10 class  | ip My_ip_Class       |               |          |           |       |     |
|           |                      | 0 10 match    | tcp any  | any ack   | count |     |
|           |                      | - 20 match    | udp any  | lt 8 any  |       |     |
|           |                      | 0 30 match    | icmp any | 10.1.1.10 | count |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|            |            | 0 10 match | tcp any | any count | [ 0 kbps conform   | ]         |
| ---------- | ---------- | ---------- | ------- | --------- | ------------------ | --------- |
|            |            | 0 20 match | icmpv6  | 1000::10  | any count [ 0 kbps | conform ] |
| Statistics | for Policy | My_Policy: |         |           |                    |           |
VRF red
| interface | vlan 10 (routed-in): |               |          |           |       |     |
| --------- | -------------------- | ------------- | -------- | --------- | ----- | --- |
| Matched   | Packets              | Configuration |          |           |       |     |
| 10 class  | ip My_ip_Class       |               |          |           |       |     |
|           |                      | 0 10 match    | tcp any  | any ack   | count |     |
|           |                      | - 20 match    | udp any  | lt 8 any  |       |     |
|           |                      | 0 30 match    | icmp any | 10.1.1.10 | count |     |
20 class ipv6 My_ipv6_Class action cir kbps 1000000 cbs 1000000 exceed drop
|         |         | 0 10 match | tcp any | any count | [ 0 kbps conform   | ]         |
| ------- | ------- | ---------- | ------- | --------- | ------------------ | --------- |
|         |         | 0 20 match | icmpv6  | 1000::10  | any count [ 0 kbps | conform ] |
| Command | History |            |         |           |                    |           |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 151

| Release             |         |         | Modification                                     |
| ------------------- | ------- | ------- | ------------------------------------------------ |
| 10.08               |         |         | Added[per-interface]information.Updatedexamples. |
| 10.07orearlier      |         |         | --                                               |
| Command Information |         |         |                                                  |
| Platforms           | Command | context | Authority                                        |
Allplatforms
Operator(>)orManager
(#)
Classifierpolicies|152

Chapter 5
|            |          |               | Classifier | policies | configuration | example |
| ---------- | -------- | ------------- | ---------- | -------- | ------------- | ------- |
| Classifier | policies | configuration | example    |          |               |         |
Thisexampleconfigurestrafficpolicingon:
n A10-GbitEthernetofSwitchAmeetingthefollowingrequirements:
o Policetherateofpacketsfromtheserverto102,400kbps.Traffic102,400kbpsorlessis
forwarded.Thetrafficmorethan102,400kbpsisdropped.
o PolicetherateofpacketsfromHostAto25,600kbps.Traffic25,600kbpsorlessisforwarded.The
trafficmorethan25,600kbpsisdropped.
n A10-GbitEthernet1/2/1ofSwitchBlimitingtheincomingtrafficrateofHTTPpacketson10-Gbit
Ethernet1/1/1tothedatarateof204,800kbpsanddroppingexcesspackets.
| Configuring |     | the classifier | policies | example |     |     |
| ----------- | --- | -------------- | -------- | ------- | --- | --- |
Thesestepsarepartoftheclassifierpoliciesconfigurationexample.
Procedure
1. ConfigureSwitchA.
CreatetrafficclassesnamedSERVER_TRAFFICandHOST_A_TRAFFICformatchingthepacketsfrom
theserverandHostA:
|     | switch#         | configure |                   |     |     |     |
| --- | --------------- | --------- | ----------------- | --- | --- | --- |
|     | switch(config)# | class     | ip SERVER_TRAFFIC |     |     |     |
switch(config-class-ip)#
|     |                          |       | match any         | 1.1.1.1 any |     |     |
| --- | ------------------------ | ----- | ----------------- | ----------- | --- | --- |
|     | switch(config-class-ip)# |       | exit              |             |     |     |
|     | switch(config)#          | class | ip HOST_A_TRAFFIC |             |     |     |
|     | switch(config-class-ip)# |       | match any         | 1.1.1.2 any |     |     |
|     | switch(config-class-ip)# |       | exit              |             |     |     |
2. CreateaclassifierpolicynamedRATE_LIMIT_POLICY:
153
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries)

| switch(config)# | policy | RATE_LIMIT_POLICY |     |     |     |
| --------------- | ------ | ----------------- | --- | --- | --- |
3. ConfigurethepolicyRATE_LIMIT_POLICY,sothat102,400kbpsoftraffic,matchingtheclass
SERVER_TRAFFIC,isforwardedandtheexcessisdropped:
switch(config-policy)# class ip SERVER_TRAFFIC action cir kbps 102400 exceed
drop
4. ConfigurethepolicyRATE_LIMIT_POLICYsothat25,600kbpsoftraffic,matchingtheclassHOST_
A_TRAFFIC,isforwardedandtheexcessisdropped:
switch(config-policy)# class ip HOST_A_TRAFFIC action cir kbps 25600 exceed
drop
| switch(config-policy)# |     | exit |     |     |     |
| ---------------------- | --- | ---- | --- | --- | --- |
5. ApplyRATE_LIMIT_POLICYtointerface1/1/1fortheinboundtraffic:
| switch(config)#    | int 1/1/1 |        |                   |     |     |
| ------------------ | --------- | ------ | ----------------- | --- | --- |
| switch(config-if)# | apply     | policy | RATE_LIMIT_POLICY |     | in  |
| switch(config-if)# | exit      |        |                   |     |     |
6. ToviewtheconfigurationwiththeRATE_LIMIT_POLICYapplied:
| switch# show | running-config |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- |
Current configuration:
!
...
| class ip SERVER_TRAFFIC |             |     |     |     |     |
| ----------------------- | ----------- | --- | --- | --- | --- |
| 10 match                | any 1.1.1.1 | any |     |     |     |
| class ip HOST_A_TRAFFIC |             |     |     |     |     |
| 10 match                | any 1.1.1.2 | any |     |     |     |
policy RATE_LIMIT_POLICY
| 10 class        | ip SERVER_TRAFFIC |     | action cir | kbps | 102400 exceed drop |
| --------------- | ----------------- | --- | ---------- | ---- | ------------------ |
| 20 class        | ip HOST_A_TRAFFIC |     | action cir | kbps | 25600 exceed drop  |
| interface 1/1/1 |                   |     |            |      |                    |
| apply policy    | RATE_LIMIT_POLICY |     | in         |      |                    |
7. ConfigureSwitchB.
CreateatrafficclassnamedHTTP_TRAFFICandconfigureittomatchtraffictoport80:
| switch(config)#          | class | ip HTTP_TRAFFIC |         |           |     |
| ------------------------ | ----- | --------------- | ------- | --------- | --- |
| switch(config-class-ip)# |       | match           | tcp any | any eq 80 |     |
switch(config-class-ip)#
exit
8. CreateaclassifierpolicynamedRATE_LIMIT_HTTP:
| switch(config)# | policy | RATE_LIMIT_HTTP |     |     |     |
| --------------- | ------ | --------------- | --- | --- | --- |
Classifierpoliciesconfigurationexample|154

9. ConfigurethepolicyRATE_LIMIT_HTTPsothat204,800kbpsoftraffic,matchingtheclassHTTP_
TRAFFIC,isforwardedandtheexcessisdropped:
switch(config-policy)# class ip HTTP_TRAFFIC action cir kbps 204800 exceed
drop
| switch(config-policy)# | exit |     |     |     |
| ---------------------- | ---- | --- | --- | --- |
10. ApplyRATE_LIMIT_HTTPtointerface1/1/1forinboundtraffic:
| switch(config)#    | int 1/1/1 |                        |     |     |
| ------------------ | --------- | ---------------------- | --- | --- |
| switch(config-if)# | apply     | policy RATE_LIMIT_HTTP |     | in  |
switch(config-if)#
exit
11. ShowtherunningconfigurationwithRATE_LIMIT_HTTPapplied:
| switch# show | running-config |     |     |     |
| ------------ | -------------- | --- | --- | --- |
Current configuration:
!
...
| class ip HTTP_TRAFFIC |             |       |     |     |
| --------------------- | ----------- | ----- | --- | --- |
| 10 match              | tcp any any | eq 80 |     |     |
policy RATE_LIMIT_HTTP
| 10 class        | ip HTTP_TRAFFIC | action cir | kbps | 204800 exceed drop |
| --------------- | --------------- | ---------- | ---- | ------------------ |
| interface 1/1/1 |                 |            |      |                    |
| apply policy    | RATE_LIMIT_HTTP | in         |      |                    |
| switch# show    | running-config  |            |      |                    |
Current configuration:
!
...
| class ip HTTP_TRAFFIC |             |       |     |     |
| --------------------- | ----------- | ----- | --- | --- |
| 10 match              | tcp any any | eq 80 |     |     |
policy RATE_LIMIT_HTTP
| 10 class        | ip HTTP_TRAFFIC | action cir | kbps | 204800 exceed drop |
| --------------- | --------------- | ---------- | ---- | ------------------ |
| interface 1/1/1 |                 |            |      |                    |
| apply policy    | RATE_LIMIT_HTTP | in         |      |                    |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 155

Chapter 6
|         |                 |          | ACL and        | Policy | hardware | resource |
| ------- | --------------- | -------- | -------------- | ------ | -------- | -------- |
| ACL and | Policy hardware | resource | considerations |        |          |          |
Switcheshavefinite(TCAMandother)hardwareresourcesusedintheapplicationofACLsandClassifier
policiestopacketsbeingprocessedinswitchhardware.ADC(analyticsdatacollection)alsoconsumes
TCAMlookups.TaketheconsiderationsdescribedinthischapterintoaccountwhendecidingwhatACL
andclassifierpolicy-relatedfeaturestouseatthesametime.
| Show | Resources |     |     |     |     |     |
| ---- | --------- | --- | --- | --- | --- | --- |
Theshow resourcescommandallowsuserstoseehardwareresourceconsumptionintheswitch.
Thesehardwareresourcesincludethefollowing:
n TCAM entries
n Policers
n High-CapacityTCAMentries
Onthe4100i,6000,6100,8320,8325,and8360switchseries,theseresourcesarereportedforthe
entireswitch.Onthe9300switchseries,resourcesarereportedperpipe.The9300switchserieshas
fourpipesandthe9300sswitchserieshastwopies.
TheusageofhighcapacityTCAMcanbeviewedspecificallyusingshow system high-capacity-tcam.
Thiscommanddisplaysthefeaturethatiscurrentlyconfigured,pendingconfiguration,andthedefault
featurepresentinhighcapacityTCAM.
| Event | Logs |     |     |     |     |     |
| ----- | ---- | --- | --- | --- | --- | --- |
ThefollowingeventlogsaredisplayedwhentheTCAMrunsoutofresources:
| Daemon      | Event ID | Severity | Message          |     |     |     |
| ----------- | -------- | -------- | ---------------- | --- | --- | --- |
| ops-switchd | 10214    | ERROR    | TCAMContextGroup |     |     |     |
selectorshavebeen
exhausted
| ops-switchd | 10215 | ERROR | TCAMContextGroup |     |     |     |
| ----------- | ----- | ----- | ---------------- | --- | --- | --- |
IDshavebeen
exhausted
| ops-switchd | 10216 | ERROR | Policerresourceshave |     |     |     |
| ----------- | ----- | ----- | -------------------- | --- | --- | --- |
beenexhausted
| ops-switchd | 10217 | ERROR | TCAMentrieshave |     |     |     |
| ----------- | ----- | ----- | --------------- | --- | --- | --- |
beenexhausted
| ops-switchd | 10218 | ERROR | TCAMtableshave |     |     |     |
| ----------- | ----- | ----- | -------------- | --- | --- | --- |
beenexhausted
| ops-switchd | 10219 | ERROR | TCAMrangeshave |     |     |     |
| ----------- | ----- | ----- | -------------- | --- | --- | --- |
beenexhausted
156
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries)

| Daemon      | Event | ID Severity | Message          |
| ----------- | ----- | ----------- | ---------------- |
| ops-switchd | 10220 | ERROR       | TCAMcountershave |
beenexhausted
| Limitations | and | exclusions |     |
| ----------- | --- | ---------- | --- |
Onthe4100i,6000,6100,8320,8325,and8400Xswitchseries,resourcesutilizedbytheCoPPLookup
arecreatedbydefaultwhenthesystemisbooted.Theseentriesshowupintheusedcolumnandmay
notdirectlycorrespondtoconfiguredentries.
Resourcesreservedforonelookupcannotbesharedorusedbyotherlookups.
| TCAM | resource | consumption | and lookups |
| ---- | -------- | ----------- | ----------- |
TCAMentriesandlookupsareconsumedbyfeaturesthatdealwiththeclassificationofpacketsusing
theTCAM.TCAMlookupsareafinitehardwareresourceusedintheapplicationofACLsandpoliciesto
packetsprocessedinswitchhardware.ADC(analyticsdatacollection)alsoconsumesTCAMlookups.A
switchcansupportalimitednumberofACLandpolicyfeaturesatthesametime.Usethecommand
| show resources | tomonitorTCAM resourcesandlookups. |     |     |
| -------------- | ---------------------------------- | --- | --- |
Certainplatformshaveadditionalresourcesthatfeaturesmayconsume,suchasL4portrange
checkers,contextgroupselectors,policers,andcounters.Differentplatformsconsumetheseresources
atdifferentrates.TherearealimitednumberoffeaturesthatuseTCAMthatcanbeenabled
simultaneouslyonthesamelinecard.
InthefollowingTCAMlookuplists,IPmeansbothIPv4andIPv6.
TCAMlookupbehaviorsvarybyswitchtype.
| For the | 8320 Switch | series: |     |
| ------- | ----------- | ------- | --- |
AsliceistheunitofTCAMresourceallocationforfeatures.Somefeaturesmayrequiremultipleslicesas
designatedbytheirwidth.Furthermore,slicescanbeusedforadditionalentriesforapreviously
configuredfeature.Therearetwelveslicesavailabletouseforingressfeatures.
IntheingressTCAM,slicesareorganizedintoclustersorrows,whichcanbevisualizedasfollows:
| Figure1 | 8320switchseriesslices |     |     |
| ------- | ---------------------- | --- | --- |
ACLandPolicyhardwareresourceconsiderations|157

In Figure 1, 8320 switch series slices, Clusters 0 and 1 have twice as many TCAM entries as clusters 2-5.

One ingress TCAM feature is always installed at switch boot for CoPP and CPU-RX. The entries for this
feature are double width and always occupy two slices in a cluster that only has 1024 entries per slice.

A feature will initially reserve the minimum number of slices required by the feature's width. The slices
must reside within the same cluster. If the required number of slices cannot be reserved within the
same cluster for a double-width feature, it will fail to install. Large slices (in clusters 0 or 1) are allocated
to user-configured features first as they have more TCAM entries per slice at 2048. Small slices (in
clusters 2-5) have 1024 TCAM entries each.

The following features use one slice when enabled:

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

158

n Ingress IPv4 Analytics Data Collection (ADC)

n Ingress IPv4 VSX

n Ingress L3 RX Statistics

n Ingress Port IPv4 ACL

n Ingress Port MAC ACL

n Ingress routed Port Policy with IPv4 classes

n Ingress Routed VLAN IPv4 ACL

n Ingress Routed VLAN Policy with IPv4 classes

n Ingress VLAN IPv4 ACL

n Ingress VLAN MAC ACL

The following features use two slices when enabled:

n Ingress Control Plane Policing (installed by default)

n Ingress Global Policy with IPv4 and/or MAC classes

n Ingress Global Policy with IPv6 classes

n Ingress IP Lockdown IPv4

n Ingress IP Lockdown IPv6

n Ingress IPv6 Analytics Data Collection (ADC)

n Ingress IPv6 VSX

n Ingress Port IPv6 ACL

n Ingress Port Policy with IPv4 and/or MAC classes

n Ingress Port Policy with IPv6 classes

n Ingress Routed Port Policy with IPv6 classes

n Ingress Routed VLAN IPv6 ACL

n Ingress Routed VLAN Policy with IPv6 classes

n Ingress VLAN IPv6 ACL

n Ingress VLAN Policy with IPv4 and/or MAC classes

n Ingress VLAN Policy with IPv6 classes

In the following example configuration, there is an IPv4 port ACL already installed in slice 0, a double-
width feature cannot reserve slice 1 and slice 2 because they are in different clusters. Instead, the
double width feature, in this case, an IPv6 port ACL, could reserve slices 2 and 3 in the TCAM as
illustrated by Figure 2, Double width feature

access-list ip test

10 deny any any any
20 deny any any any
30 deny any any any

access-list ipv6 v6_acl

10 deny any any any
20 deny any any any

interface 1/1/1

apply access-list ip test in

interface 1/1/2

ACL and Policy hardware resource considerations | 159

apply access-list ipv6 v6_acl in

Figure 2 Double width feature

However, if enough entries in one feature are configured to exhaust the initial reservation, an attempt
to reserve more slices occurs. In this configuration, too many IPv6 Port ACL entries have been
configured to fit in to slices 2 and 3. Because IPv6 Port ACL is a double-width feature, the TCAM reserves
another two slices. Figure 3, Double width feature reservation displays an example of this TCAM.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

160

access-list ip test
| 10 deny any any | any |     |
| --------------- | --- | --- |
access-list ipv6 v6_acl
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
...
| 20480 deny any | any any |     |
| -------------- | ------- | --- |
| 20490 deny any | any any |     |
| 20500 deny any | any any |     |
interface 1/1/1
| apply access-list | ip test in |     |
| ----------------- | ---------- | --- |
interface 1/1/2
| apply access_list | ipv6 v6_acl | in  |
| ----------------- | ----------- | --- |
Figure3 Doublewidthfeaturereservation
ACLandPolicyhardwareresourceconsiderations|161

The following configuration is an example of when show resources displays that there are available
TCAM entries due to Slice 1 being free. However, these available resources cannot be utilized by a
double-width feature. Neither a previously installed feature, such as IPv6 Port ACLs, nor a double-width
feature , such as VLAN Policy with IPv6 classes, can use these available resources. Only a single-width
feature can utilize them. Expanding the resources used by IPv4 Port ACLs or adding a new single-width
feature are eligible uses of the available TCAM entries. Figure 4, Free slice usage displays an example of
this TCAM.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

162

access-list ip test
| 10 deny any any | any |     |
| --------------- | --- | --- |
access-list ipv6 v6_acl
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
...
| 20480 deny any | any any |     |
| -------------- | ------- | --- |
| 20490 deny any | any any |     |
| 20500 deny any | any any |     |
access-list ipv6 small_v6_acl
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
class ip c
| 10 match any any | any |     |
| ---------------- | --- | --- |
policy p
| 10 class ip c action | drop |     |
| -------------------- | ---- | --- |
vlan 100
| apply access-list | ipv6 small_v6_acl | in  |
| ----------------- | ----------------- | --- |
interface 1/1/1
| apply access-list | ip test in |     |
| ----------------- | ---------- | --- |
interface 1/1/2
| apply access_list | ipv6 v6_acl | in  |
| ----------------- | ----------- | --- |
interface 1/1/3
| apply policy p | in  |     |
| -------------- | --- | --- |
Figure4 Freesliceusage
ACLandPolicyhardwareresourceconsiderations|163

Egress TCAM

There are four slices of 256 entries each that are available on egress for features that use one or two
slices each. However, the egress CoPP feature always consumes two of these slices. As a result, only two
slices are free and applying both IPv4 and IPv6 ACLs on egress or routed-egress at the same time is not
permitted.

The egress TCAM only has one cluster of four slices as illustrated in Figure 5, Egress TCAM

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

164

Figure 5 Egress TCAM

These egress features use one slice each:

n Egress Port IPv4 ACL

n Egress Routed VLAN IPv4 ACL

n Egress VLAN IPv4 ACL

n Egress L3 TX statistics

These egress features use two slices each:

n Egress Routed VLAN IPv6 ACL

n Egress VLAN IPv6 ACL

The egress TCAM consumes resources similarly to the ingress TCAM. However, only two slices are
available for user configured features. This means that a user could configure one double-width feature,
two single-width features, or one single-width feature that requires enough resources to expand to a
second slice.

For the 8325 and 10000 Switch series:

A slice is the unit of TCAM resource allocation for features. Some features may require multiple slices as
designated by their width. Furthermore, slices can be used for additional entries for a previously
configured feature. There are twelve slices of 768 entries each which are available to use for ingress
features.

In the ingress TCAM, slices are organized into clusters or rows, as illustrated in Figure 6, TCAM slices

Figure 6 TCAM slices

ACL and Policy hardware resource considerations | 165

One ingress TCAM feature is always installed at switch boot for CoPP and CPU-RX. The entries for this
feature are triple width, so CoPP consumes three slices. For example, if slices 0, 1 and 2 are used for
CoPP, there are nine remaining slices to allocate to ingress features.

A feature initially reserves the minimum number of slices required by the feature's width. The slices
must reside within the same cluster. If the required number of slices cannot be reserved within the
same cluster for a double or triple-width feature, it fails to install.

The following features use one slice when enabled:

n Ingress IPv4 and/or IPv6 VSX*

n Ingress VLAN MAC ACL

n Ingress VXLAN Relay

The following features use two slices when enabled:

n Ingress L3 RX Statistics

n Ingress Port MAC ACL

The following features use three slices when enabled. Features denoted by an * can share ingress TCAM
slices if they are IPv4 and IPv6 features of the same application type. In the show resources output,
they display as separate features with an * in the Reserved entries column to denote that an IPv4 and
an IPv6 feature of the same application type are sharing TCAM slices.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

166

n IngressControlPlanePolicing(installedbydefault)
n IngressGlobalPolicywithIPv4and/orMAC classes
IngressGlobalPolicywithIPv6classes
n
n IngressIPv4and/orIPv6AnalyticsDataCollection(ADC)*
n IngressIPv4IPLockdown
n IngressIPv6IPLockdown
n IngressPACPolicy
n IngressPortIPv4and/orIPv6ACL*
n IngressPortPolicywithIPv4and/orMACclasses
IngressPortPolicywithIPv6classes
n
n IngressRoutedPortPolicywithIPv4and/orIPv6classes*
n IngressRoutedVLANIPv4and/orIPv6ACL*
n IngressRoutedVLANPolicywithIPv4and/orIPv6classes*
n IngressVLANIPv4and/orIPv6ACL*
n IngressVLANPolicywithIPv4and/orMACclasses
n IngressVLANPolicywithIPv6classes
Forexample,ifthereisaconfigurationwithaMAC portACLalreadyinstalledinslices3and4,anew
triple-widthfeaturecannotreserveslices5,6,and7becausetheyarenotinthesamecluster.Instead,
thenewtriple-widthfeaturecanreserveslices6,7,and8intheTCAM.
access-list mac test
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
| 30 deny any any | any |     |
access-list ip v4_acl
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
access-list ipv6 v6_acl
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
interface 1/1/1
| apply access-list | mac test | in  |
| ----------------- | -------- | --- |
interface 1/1/2
| apply access-list | ip v4_acl | in  |
| ----------------- | --------- | --- |
interface 1/1/3
| apply access-list | ipv6 v6_acl | in  |
| ----------------- | ----------- | --- |
Thiscanbeseenin Figure7,Triplewidthfeature.
Figure7 Triplewidthfeature
ACLandPolicyhardwareresourceconsiderations|167

Inthisconfiguration,theoutputfromshow resourcesisasfollows:
| 8325(config)# | show resources |     |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- | --- |
Resource Usage:
Mod Description
| Resource |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
| 1/1 Ingress MAC | Port ACL       |          |     |     |      |     |
| --------------- | -------------- | -------- | --- | --- | ---- | --- |
| Ingress         | TCAM Entries   |          | 2   | 8   | 1536 |     |
| Ingress IPv4    | Port ACL       |          |     |     |      |     |
| Ingress         | TCAM Entries   |          | 3   | 9   | 2304 |     |
| Ingress IPv6    | Port ACL       |          |     |     |      |     |
| Ingress         | TCAM Entries   |          | 3   | 9   | *    |     |
| Ingress Control | Plane Policing |          |     |     |      |     |
| Ingress         | TCAM Entries   |          | 3   | 408 | 2304 |     |
| Egress Control  | Plane Policing |          |     |     |      |     |
| Egress          | TCAM Entries   |          | 2   | 96  | 1024 |     |
| Pre Ingress     | Control Plane  | Policing |     |     |      |     |
Total
| Ingress  | TCAM Entries   |     |     | 434 | 6144 | 3072 |
| -------- | -------------- | --- | --- | --- | ---- | ---- |
| Egress   | TCAM Entries   |     |     | 96  | 1024 | 1024 |
| Policers |                |     |     | 0   |      | 6144 |
| Ingress  | L4 Port Ranges |     |     | 0   |      | 32   |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 168

Inthisexampleconfiguration,the*intheReservedcolumnoftheIngressIPv6PortACLfeaturedenotesthatthis
featureissharingreservedsliceswiththeprecedingfeature,IngressIPv4PortACL.
However,onceenoughentriesareconfiguredinonefeaturetoexhaustitsinitialreservedentries,an
attempttoreservemoreslicesoccurs.
access-list mac test
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
...
| 7700 deny any any | any |     |
| ----------------- | --- | --- |
access-list ip v4_acl
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
access-list ipv6 v6_acl
| 10 deny any any | any |     |
| --------------- | --- | --- |
| 20 deny any any | any |     |
interface 1/1/1
| apply access-list | mac test | in  |
| ----------------- | -------- | --- |
interface 1/1/2
| apply access-list | ip v4_acl | in  |
| ----------------- | --------- | --- |
interface 1/1/3
| apply access-list | ipv6 v6_acl | in  |
| ----------------- | ----------- | --- |
Inthisscenario,toomanyMAC PortACLentrieshavebeenconfiguredtofitinslices3and4.Since
MAC PortACLisadouble-widthfeature,theTCAMreservesanothertwoslicesasshowninTCAM slice
reservation.
Figure8 TCAM slicereservation
ACLandPolicyhardwareresourceconsiderations|169

Withthisconfiguration,theshow resourcesoutputisasfollows:
| 8325(config)# | show resources |     |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- | --- |
Resource Usage:
Mod Description
| Resource |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
| 1/1 Ingress MAC | Port ACL       |          |     |      |      |     |
| --------------- | -------------- | -------- | --- | ---- | ---- | --- |
| Ingress         | TCAM Entries   |          | 2   | 1542 | 3072 |     |
| Ingress IPv4    | Port ACL       |          |     |      |      |     |
| Ingress         | TCAM Entries   |          | 3   | 9    | 2304 |     |
| Ingress IPv6    | Port ACL       |          |     |      |      |     |
| Ingress         | TCAM Entries   |          | 3   | 9    | *    |     |
| Ingress Control | Plane Policing |          |     |      |      |     |
| Ingress         | TCAM Entries   |          | 3   | 408  | 2304 |     |
| Egress Control  | Plane Policing |          |     |      |      |     |
| Egress          | TCAM Entries   |          | 2   | 96   | 1024 |     |
| Pre Ingress     | Control Plane  | Policing |     |      |      |     |
Total
| Ingress  | TCAM Entries   |     |     | 1959 | 7680 | 1536 |
| -------- | -------------- | --- | --- | ---- | ---- | ---- |
| Egress   | TCAM Entries   |     |     | 96   | 1024 | 1024 |
| Policers |                |     |     | 0    |      | 6144 |
| Ingress  | L4 Port Ranges |     |     | 0    |      | 32   |
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 170

Although there are 1536 Free Ingress TCAM Entries, there are only two single-width slices available. Only
features that are single-width on these platforms can install successfully. Any non-single-width features
that the user attempts to configure or expand fail as there are no consecutive free slices available within
a single cluster.

Egress TCAM

There are four total slices with 512 entries each which are available on egress for the features listed
below. However, the egress CoPP feature always consumes two of these slices. Since only two slices are
free, applying both IPv4 and IPv6 ACLs in the egress direction at the same time is not permitted.

The egress TCAM has only one cluster of four slices as shown in Figure 9, Egress TCAM on the 8325 and
10000 switch series.

Figure 9 Egress TCAM on the 8325 and 10000 switch series

Egress features that use one slice:

n Egress Routed Port IPv4 ACL

n Egress Routed VLAN IPv4 ACL

n Egress VLAN IPv4 ACL

n Egress L3 TX Statistics

     Egress features that use two slices:

n Egress VLAN IPv6 ACL

n Egress Routed VLAN IPv6 ACL

The egress TCAM consumes resources similarly to the ingress TCAM. However, only two slices are
available for user configured features. This means that one double-width feature, two single-width
features, or one single-width feature that requires enough resources to expand to a second slice can be
configured.

For the 9300/9300S AND 10040 Switch series:

A slice is the unit of TCAM resource allocation for features. Some features may require multiple slices as
designated by their width. Furthermore, a switch can use slices for additional entries for a previously
configured feature. There are twelve slices available to use for ingress features. These are grouped into
three rows of four slices each, with each row defined as a cluster.

For the 9300 switch series, the slices are 2048 entries each. This is displayed in Figure 10, TCAM slices
on the 9300 switch series

Figure 10 TCAM slices on the 9300 switch series

ACL and Policy hardware resource considerations | 171

For the 9300S AND 10040 switch series, slices in Cluster-0 have 2048 entries each and the slices in
Cluster-1 and Cluster-2 have 1024 entries each. This is displayed in Figure 11, TCAM slices on the 9300S
switch series

Figure 11 TCAM slices on the 9300S switch series

CoPP and CPU-RX always add entries to the TCAM table at switch boot. The entries in this table are of a
triple width, and always occupy slices 0, 1, and 2. As a result, the switch has nine remaining slices to
allocate to ingress features.

A feature initially reserves the minimum number of slices required by the width of the feature. The
slices must be adjacent to one another and reside within the same cluster. If the feature cannot reserve
the required number of slices within the same cluster for a feature that has a width of double or

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

172

greater,itfailstoinstall.Theseplatformsalsodividephysicalinterfaces,suchasports,intomultiple
pipes.EachpipehasindependentTCAMresources.Forthe9300switchseries,therearefourpipes
acrosswhichtheportinterfacesarespread.Forthe9300sswitchseries,therearetwopipesacross
whichtheportinterfacesarespread.Applicationsthatcouldbepresentonanyport,suchasVLAN
applications,areappliedtoallpipes.Runshow resourcestodisplaywhichportinterfacesarepartof
eachpipe.Thefollowingisanexampleoftheshow resourcesoutputdisplayingportinterfacesand
pipesonthe9300switchseries:
9300# show resources
Resource Usage:
Mod Description
| Resource |     |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
1/1 Global
Total
| Destination | Field | Processor | Entries |     | 0   | 0   | 1024 |
| ----------- | ----- | --------- | ------- | --- | --- | --- | ---- |
1/1-0 Ports 9-12,21-24
| Ingress | Control Plane | Policing |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 420 | 6144 | 18432 |
| ------- | --------------- | ------- | --- | --- | --- | ---- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0    | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0    | 1024  |
1/1-1 Ports 1-8
| Ingress | Control Plane | Policing |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 420 | 6144 | 18432 |
| ------- | --------------- | ------- | --- | --- | --- | ---- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0    | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0    | 1024  |
1/1-2 Ports 13-20
| Ingress | Control Plane | Policing |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 420 | 6144 | 18432 |
| ------- | --------------- | ------- | --- | --- | --- | ---- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0    | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0    | 1024  |
1/1-3 Ports 25-32
| Ingress | Control Plane | Policing |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 420 | 6144 | 18432 |
| ------- | --------------- | ------- | --- | --- | --- | ---- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0    | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0    | 1024  |
Thefollowingisanexampleoftheshow resourcesoutputdisplayingportinterfacesandpipesonthe
9300SOR10040switchseries:
switc# show resources
Resource Usage:
Mod Description
| Resource |     |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
1/1 Global
Total
ACLandPolicyhardwareresourceconsiderations|173

| Destination | Field | Processor Entries |     | 0 0 | 1024 |
| ----------- | ----- | ----------------- | --- | --- | ---- |
1/1-0 Ports 1-20
| Ingress | Control Plane | Policing |     |          |     |
| ------- | ------------- | -------- | --- | -------- | --- |
|         | Ingress TCAM  | Entries  | 3   | 420 6144 |     |
Total
| Ingress | TCAM Entries    |         |     | 420 6144 | 10240 |
| ------- | --------------- | ------- | --- | -------- | ----- |
| Egress  | TCAM Entries    |         |     | 0 0      | 2048  |
| VLAN    | Field Processor | Entries |     | 0 0      | 1024  |
1/1-1 Ports 21-40
| Ingress | Control Plane | Policing |     |          |     |
| ------- | ------------- | -------- | --- | -------- | --- |
|         | Ingress TCAM  | Entries  | 3   | 420 6144 |     |
Total
| Ingress | TCAM Entries    |         |     | 420 6144 | 10240 |
| ------- | --------------- | ------- | --- | -------- | ----- |
| Egress  | TCAM Entries    |         |     | 0 0      | 2048  |
| VLAN    | Field Processor | Entries |     | 0 0      | 1024  |
Intheoutputsabove,thenumberfollowing1/1-isthepipenumber.Intheexampleforthe9300S
switchseries,pipe0containsportinterfaces1-20.
Eachofthefollowingfeaturesusesthreesliceswhenenabled.Nomorethantwoofthesefeaturescan
beconfiguredatthesametime.IngressControlPlanePolicingdoesnotcounttowardsthetwofeatures
thatmaybeconfigured.
Eachofthefollowingfeaturesusesoneslicewhenenabled.Nomorethannineofthelistedfeaturescan
beconfiguredatthesametime.
n BidirectionalForwardingDetection(BFD)
n InbandFlowAnalyzer(IFA)TransitorTerminatormonitor
n IngressARPVSX
IngressIPv4VSX
n
n IngressIPv6VSX
n IngressPortMACACL
n IngressVLANMACACL
n IngressDistributedServicesPreserveQoS(10040Switchseriesonly)
Eachofthefollowingfeaturesusestwosliceswhenenabled.Nomorethanfourofthelistedfeatures
canbeconfiguredatthesametime.
n IngressIPv4IPLockdown
n IngressPortIPv4ACL
n IngressVLANIPv4ACL
IngressRoutedVLANIPv4ACL
n
n IngressIPv4AnalyticsDataCollection(ADC)
n IngressIPv6AnalyticsDataCollection(ADC)
| n IngressDistributedServices |     | (10040Switchseriesonly) |     |     |     |
| ---------------------------- | --- | ----------------------- | --- | --- | --- |
Eachfeaturelistedbelowusesthreesliceswhenenabled.Atmost,twoofthelistedfeaturescanbe
configuredatthesametime.IngressControlPlanePolicingdoesnotcontributetowardsthetwolisted
featuresthatmaybeconfigured.
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 174

nInband Flow Analyzer (IFA) Initiator Monitor

n Ingress Control Plane Policing (installed by default)

n Ingress Global Policy with IPv4 and/or MAC classes

n Ingress Global Policy with IPv6 classes

n Ingress IPv6 Lockdown

n Ingress Port IPv6 ACL

n Ingress Port Policy with IPv4 and/or MAC classes

n Ingress Port Policy with IPv6 classes

n Ingress Routed Port Policy with IPv4 and/or IPv6 classes

n Ingress Routed VLAN IPv6 ACL

n Ingress Routed VLAN Policy with IPv4 and/or IPv6 classes

n Ingress VLAN IPv6 ACL

n Ingress VLAN Policy with IPv4 and/or MAC classes

n Ingress VLAN Policy with IPv6 classes

Multiple width features features must span slices in the same cluster. In this configuration and in Figure
12, Double width feature on the 9300 switch series, IPv4 Port ACLs has a width of 2, so it must use slices
in cluster 1 or 2 since cluster 0 only has one slice available. Only a feature with a width of 1 can use slice
3. IPv4 Port ACLs could technically consume slice 6 and 7 instead of 4 and 5. Similarly, slices 8 and 9, 9
and 10, or 10 and 11 in cluster 2 also satisfy the requirement that a feature's slices be adjacent to one
another and reside in the same cluster.

access-list ip test

10 deny any any any
20 deny any any any
30 deny any any

interface 1/1/1

apply access-list ip test in

Figure 12 Double width feature on the 9300 switch series

ACL and Policy hardware resource considerations | 175

Inthefollowingshow resourcesoutput,onlyoneofthepipeshasconsumedTCAMresources
associatedwiththeIPv4PortACL.
9300# show resources
Resource Usage:
Mod Description
| Resource |     |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
1/1 Global
Total
| Destination | Field | Processor | Entries |     | 0   | 0   | 1024 |
| ----------- | ----- | --------- | ------- | --- | --- | --- | ---- |
1/1-0 Ports 9-12,21-24
| Ingress | Control Plane | Policing |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 420 | 6144 | 18432 |
| ------- | --------------- | ------- | --- | --- | --- | ---- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0    | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0    | 1024  |
1/1-1 Ports 1-8
| Ingress | IPv4 Port     | ACL      |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 2   | 10  | 4096 |     |
| Ingress | Control Plane | Policing |     |     |     |      |     |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 420 | 10240 | 14336 |
| ------- | --------------- | ------- | --- | --- | --- | ----- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0     | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0     | 1024  |
1/1-2 Ports 13-20
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 176

| Ingress | Control | Plane | Policing |     |     |     |      |     |
| ------- | ------- | ----- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress | TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM  | Entries   |         |     |     | 420 | 6144 | 18432 |
| ------- | ----- | --------- | ------- | --- | --- | --- | ---- | ----- |
| Egress  | TCAM  | Entries   |         |     |     | 0   | 0    | 2048  |
| VLAN    | Field | Processor | Entries |     |     | 0   | 0    | 1024  |
1/1-3 Ports 25-32
| Ingress | Control | Plane | Policing |     |     |     |      |     |
| ------- | ------- | ----- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress | TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM  | Entries   |         |     |     | 420 | 6144 | 18432 |
| ------- | ----- | --------- | ------- | --- | --- | --- | ---- | ----- |
| Egress  | TCAM  | Entries   |         |     |     | 0   | 0    | 2048  |
| VLAN    | Field | Processor | Entries |     |     | 0   | 0    | 1024  |
9300s# show resources
Resource Usage:
Mod Description
| Resource |     |     |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
1/1 Global
Total
| Destination |     | Field | Processor | Entries |     | 0   | 0   | 1024 |
| ----------- | --- | ----- | --------- | ------- | --- | --- | --- | ---- |
1/1-0 Ports 1-20
| Ingress | IPv4    | Port         | ACL      |     |     |     |      |     |
| ------- | ------- | ------------ | -------- | --- | --- | --- | ---- | --- |
|         | Ingress | TCAM         | Entries  |     | 2   | 10  | 2048 |     |
| Ingress | Control | Plane        | Policing |     |     |     |      |     |
|         | Ingress | TCAM Entries |          |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM  | Entries   |         |     |     | 430 | 8192 | 8192 |
| ------- | ----- | --------- | ------- | --- | --- | --- | ---- | ---- |
| Egress  | TCAM  | Entries   |         |     |     | 0   | 0    | 2048 |
| VLAN    | Field | Processor | Entries |     |     | 0   | 0    | 1024 |
1/1-1 Ports 21-40
| Ingress | Control | Plane | Policing |     |     |     |      |     |
| ------- | ------- | ----- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress | TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress        | TCAM      | Entries   |         |     |     | 420 | 6144 | 10240 |
| -------------- | --------- | --------- | ------- | --- | --- | --- | ---- | ----- |
| Egress         | TCAM      | Entries   |         |     |     | 0   | 0    | 2048  |
| VLAN           | Field     | Processor | Entries |     |     | 0   | 0    | 1024  |
| access-list ip | my_ip_acl |           |         |     |     |     |      |       |
| 10 permit      | any       | any       | any     |     |     |     |      |       |
class ipv6 test
| 10 match | any | any any |     |     |     |     |     |     |
| -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
policy p
| 10 class | ipv6 | test | action | drop |     |     |     |     |
| -------- | ---- | ---- | ------ | ---- | --- | --- | --- | --- |
vlan 100
| apply | access-list |     | ip my_ip_acl | in  |     |     |     |     |
| ----- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
interface 1/1/1
| apply | policy | p in |     |     |     |     |     |     |
| ----- | ------ | ---- | --- | --- | --- | --- | --- | --- |
Figure13 IngressTCAMonPipewithinterface1/1/1
ACLandPolicyhardwareresourceconsiderations|177

Figure 14 Ingress TCAM on Pipe without interface 1/1/1

In this example, an IPv4 ACL has been applied to a VLAN. This application consumes resources on all
Pipes as VLANs exist across all Pipes on a switch. Additionally, there is a Policy with an IPv6 class applied
to interface 1/1/1. The interface 1/1/1 only exists on a single Pipe, so the TCAM resources only need to
be allocated for the TCAM on that Pipe. This results in show resources reporting that less ingress TCAM
entries are free for the Pipe with interface 1/1/1 than for other Pipe(s) that do not have the interface
1/1/1.

9300# show resources

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

178

Resource Usage:
Mod Description
| Resource |     |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
1/1 Global
Total
| Destination | Field | Processor | Entries |     | 0   | 0   | 1023 |
| ----------- | ----- | --------- | ------- | --- | --- | --- | ---- |
1/1-0 Ports 9-12,21-24
| Ingress | IPv4 VLAN     | ACL      |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 2   | 12  | 4096 |     |
| Ingress | Control Plane | Policing |     |     |     |      |     |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 432 | 10240 | 14336 |
| ------- | --------------- | ------- | --- | --- | --- | ----- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0     | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0     | 1024  |
1/1-1 Ports 1-8
| Ingress | IPv4 VLAN     | ACL      |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 2   | 12  | 4096 |     |
| Ingress | IPv6 Port     | Policy   |     |     |     |      |     |
|         | Ingress TCAM  | Entries  |     | 3   | 6   | 6144 |     |
| Ingress | Control Plane | Policing |     |     |     |      |     |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 438 | 16384 | 8192 |
| ------- | --------------- | ------- | --- | --- | --- | ----- | ---- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0     | 2048 |
| VLAN    | Field Processor | Entries |     |     | 0   | 0     | 1024 |
1/1-2 Ports 13-20
| Ingress | IPv4 VLAN     | ACL      |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 2   | 12  | 4096 |     |
| Ingress | Control Plane | Policing |     |     |     |      |     |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 432 | 10240 | 14336 |
| ------- | --------------- | ------- | --- | --- | --- | ----- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0     | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0     | 1024  |
1/1-3 Ports 25-32
| Ingress | IPv4 VLAN     | ACL      |     |     |     |      |     |
| ------- | ------------- | -------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM  | Entries  |     | 2   | 12  | 4096 |     |
| Ingress | Control Plane | Policing |     |     |     |      |     |
|         | Ingress TCAM  | Entries  |     | 3   | 420 | 6144 |     |
Total
| Ingress | TCAM Entries    |         |     |     | 432 | 10240 | 14336 |
| ------- | --------------- | ------- | --- | --- | --- | ----- | ----- |
| Egress  | TCAM Entries    |         |     |     | 0   | 0     | 2048  |
| VLAN    | Field Processor | Entries |     |     | 0   | 0     | 1024  |
9300s# show resources
Resource Usage:
Mod Description
| Resource |     |     |     | Width | Used Reserved |     | Free |
| -------- | --- | --- | --- | ----- | ------------- | --- | ---- |
------------------------------------------------------------------------------
1/1 Global
Total
| Destination | Field | Processor | Entries |     | 0   | 0   | 1023 |
| ----------- | ----- | --------- | ------- | --- | --- | --- | ---- |
1/1-0 Ports 1-20
| Ingress | IPv4 Port    | ACL     |     |     |     |      |     |
| ------- | ------------ | ------- | --- | --- | --- | ---- | --- |
|         | Ingress TCAM | Entries |     | 2   | 12  | 2048 |     |
ACLandPolicyhardwareresourceconsiderations|179

| Ingress | IPv6 Port            | Policy   |       |      |
| ------- | -------------------- | -------- | ----- | ---- |
|         | Ingress TCAM Entries |          | 3 6   | 3072 |
| Ingress | Control Plane        | Policing |       |      |
|         | Ingress TCAM Entries |          | 3 420 | 6144 |
Total
| Ingress     | TCAM Entries |         | 438 | 11264 5120 |
| ----------- | ------------ | ------- | --- | ---------- |
| Egress TCAM | Entries      |         | 0   | 0 2048     |
| VLAN Field  | Processor    | Entries | 0   | 0 1024     |
1/1-1 Ports 21-40
| Ingress | IPv4 VLAN     | ACL      |       |      |
| ------- | ------------- | -------- | ----- | ---- |
|         | Ingress TCAM  | Entries  | 2 12  | 2048 |
| Ingress | Control Plane | Policing |       |      |
|         | Ingress TCAM  | Entries  | 3 420 | 6144 |
Total
| Ingress     | TCAM Entries |         | 430 | 8192 8192 |
| ----------- | ------------ | ------- | --- | --------- |
| Egress TCAM | Entries      |         | 0   | 0 2048    |
| VLAN Field  | Processor    | Entries | 0   | 0 1024    |
Inthisconfiguration,attemptstoapplyanIPv6ACLtoaVLANfailbecausenotallPipeshavethree
adjacentslicesavailableinthesamecluster.However,iftheuserinsteadattemptstoapplytheIPv6ACL
toaportthatisnotonthesamePipeas1/1/1,theapplicationsucceeds,asotherPipesdohavethree
adjacentslicesavailableinthesamecluster.
Egress TCAM
Therearefourslicesinonecluster,eachofwhichhave512entriesthatareavailableforegressfeatures.
Thisisdisplayedin Figure15,EgressTCAMona9300switchseries.
Figure15 EgressTCAMona9300switchseries
Thefollowingegressfeaturesusethreesliceswhenenabled:
n EgressPortIPv6ACL
n EgressVLAN IPv6ACL
n EgressRoutedVLANIPv6ACL
n EgressPortIPv6Policy
n EgressVLAN IPv6Policy
Thefollowingegressfeaturesusetwosliceswhenenable:
n EgressPortIPv4+MACPolicy
n EgressVLANIPv4+MACPolicy
Thefollowingegressfeaturesuseoneslicewhenenabled:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 180

n Egress Port IPv4 ACL

n Egress Port MAC ACL

n Egress VLAN IPv4 ACL

n Egress Routed VLAN IPv4 ACL

n Egress VLAN MAC ACL

The egress TCAM consumes resources similarly to the ingress TCAM. The egress TCAM also has
independent resources for each Pipe.

There are further restrictions as it relates to egress features. You may configure a maximum of one
policy feature at a time and a maximum of two total egress features at a time.

Examples of valid combinations of configured egress features include:

n Egress VLAN IPv4 ACL

n Egress Port IPv4+MAC Policy

n Egress Port IPv4 ACL

n Egress Port IPv6 ACL

Examples of invalid combinations of configured egress features include:

n Egress Port IPv4+MAC Policy

n Egress VLAN IPv4+MAC Policy

n Egress Port IPv4 ACL

n Egress Port MAC ACL

n Egress VLAN MAC ACL

Matching precedence order

When a packet is matched by multiple TCAM Lookups with the same action, a precedence order is
followed.

For example, if a packet matches feature 1 with an action to change DSCP to x and a feature 2 with an
action to change DSCP to y, the feature 2 action takes precedence and DSCP of the packet will change to
y (given that the precedence of feature 2 is greater than that of feature 1). Count-related exception: If a
packet matches an IPv4 ACL, a MAC ACL, and a policy with count actions, all the counters increment.
Regardless of precedence, if a packet is to be dropped by a configured feature, it will be dropped.
Ingress packets do not take precedence over egress packets nor do egress packets take precedence
over ingress packets.

The egress TCAM can only increment one counter for the ACLs or policies applied on egress. Only the
counter with the highest precedence increments.

The precedence order from highest to lowest is as follows:

ACL and Policy hardware resource considerations | 181

| Ingress | Port    | IPv6 ACL       |                   |                 |
| ------- | ------- | -------------- | ----------------- | --------------- |
| Ingress | Routed  | VLAN           | IPv6 ACL          |                 |
| Ingress | VLAN    | IPv6 ACL       |                   |                 |
| Ingress | Port    | IPv4 ACL       |                   |                 |
| Ingress | Routed  | VLAN           | IPv4 ACL          |                 |
| Ingress | VLAN    | IPv4 ACL       |                   |                 |
| Ingress | Port    | MAC ACL        |                   |                 |
| Ingress | VLAN    | MAC ACL        |                   |                 |
| Ingress | IPv6    | Analytics      | Data Collection   | (ADC)           |
| Ingress | IPv4    | Analytics      | Data Collection   | (ADC)           |
| Ingress | Port    | Policy         | with IPv6 classes |                 |
| Ingress | Port    | Policy         | with IPv4 and/or  | MAC classes     |
| Ingress | VLAN    | Policy         | with IPv6 classes |                 |
| Ingress | VLAN    | Policy         | with IPv4 and/or  | MAC classes     |
| Ingress | Global  | Policy         | with IPv6 classes |                 |
| Ingress | Global  | Policy         | with IPv4 and/or  | MAC classes     |
| IPv6    | Control | Plane Policing |                   |                 |
| IPv4    | Control | Plane Policing |                   |                 |
| MAC     | Control | Plane Policing |                   |                 |
| Ingress | Control | Plane          | Policing          |                 |
| Ingress | Routed  | Port           | IPv6 Policy       |                 |
| Ingress | Routed  | Port           | IPv4 Policy       |                 |
| Ingress | Routed  | VLAN           | IPv6 Policy       |                 |
| Ingress | Routed  | VLAN           | IPv4 Policy       |                 |
| Ingress | L3      | Statistics     |                   |                 |
| Ingress | IPv6    | VSX            |                   |                 |
| Ingress | IPv4    | VSX            |                   |                 |
| Ingress | ARP     | VSX            |                   |                 |
| Ingress | MAC     | VSX            |                   |                 |
| Egress  | Routed  | Port IPv4      | ACL               |                 |
| Egress  | Routed  | VLAN IPv6      | ACL               |                 |
| Egress  | VLAN    | IPv6 ACL       |                   |                 |
| Egress  | Routed  | VLAN IPv4      | ACL               |                 |
| Egress  | VLAN    | IPv4 ACL       |                   |                 |
| Egress  | Control | Plane          | Policing          |                 |
| Egress  | L3      | Statistics     |                   |                 |
| Policer | Action  | Considerations |                   | and Limitations |
Thepolicerexceed remarkDSCPactionissupportedonthefollowingplatforms:
n 8325
n 9300
n 10000
Policer exceed remarkDSCP actioncannotbecombinedwithotheractionsinthesamepolicyentry,
butotherentriesinthepolicymayuseotheractions.
Forexample,thisconfigurationisallowed:
| switch(config)# |     | policy | my_policswitch |     |
| --------------- | --- | ------ | -------------- | --- |
(config-policy)# 10 class ip my_class action cir kbps 1000 cbs 15625 exceed dscp
EF
Butthisisnotbecauseitaddsasecondaryactionwithinthesamepolicyentry:
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 182

switch(config-policy)# 10 class ip my_class action cir kbps 1000 cbs 15625 exceed
| dscp EF action | mirror 1 |     |     |
| -------------- | -------- | --- | --- |
| Invalid input: | action   |     |     |
Packetswithalowdropprecedencevalue(greenpackets)canberemarkedusingaQoSremarkofall
trafficoningressonportsandLAGs.
| policy my_ingress_policy |     |     |     |
| ------------------------ | --- | --- | --- |
10 class ip my_class action cir kbps 1000 cbs 15625 exceed dscp CS1
| interface 1/1/1 |     |     |     |
| --------------- | --- | --- | --- |
qos dscp 46
| apply | policy my_ingress_policy | in  |     |
| ----- | ------------------------ | --- | --- |
Packetscanbestaticallyremarkedbyaseparateswitchbeforetheyreachtheswitchwiththeexceed
remarkDSCPaction.
Switch1exampleconfiguration:
| policy my_ingress_policy |             |                |     |
| ------------------------ | ----------- | -------------- | --- |
| 10 class                 | ip my_class | action dscp EF |     |
| interface 1/1/1          |             |                |     |
qos dscp 46
! OR
| apply | policy my_ingress_policy | in  |     |
| ----- | ------------------------ | --- | --- |
Switch2exampleconfiguration:
| policy my_ingress_policer_policy |     |     |     |
| -------------------------------- | --- | --- | --- |
10 class ip my_class action cir kbps 1000 cbs 15625 exceed dscp CS1
| interface 1/1/1 |                                  |                |     |
| --------------- | -------------------------------- | -------------- | --- |
| apply           | policy my_ingress_policer_policy |                | in  |
| Subinterface    | Application                      | Considerations |     |
Formultiplesubinterfacesinthesamedirection,asinglepolicerwillbesharedforallthesubinterfaces
onthesamelinecard/stackmemberanddatapipeline,ifapplicable.
TheHPEANW8325and1000Switchserieshavetwodatapipelineswithphysicalinterfacessplit
betweenthetwopipelines.
TheHPEANW9300-32D32-port100/200/400GQSFP-DD2-port10GSwitchplatformhasfourdata
pipelinesandHPEANW930032x100G-QSFP288x400G-QDD2x10G-SFP+Switchhastwodatapipelines.
IfseparatepolicersfordifferentSubinterfacesarerequired,thenanotherPolicyshouldbecreated
becausetheper-interfacekeywordisnotavailableinthesubinterfacecontext.
| Metering and | Remarking |     |     |
| ------------ | --------- | --- | --- |
Whenthesamepolicyisappliedacrossmultipleports,eachportthepolicyisappliedtocontributes
traffictotheratelimit.Policersaresharedamongallportswiththesamepolicyappliedaslongasthey
areonthesamelinecardandvrfmember.
TheHPEANW8325and1000Switchserieshavetwodatapiplineswithphysicalinterfacessplitbetween
thetwothatdonotsharepolicers.
ACLandPolicyhardwareresourceconsiderations|183

The Aruba 9300-32D 32-port 100/200/400G QSFP-DD 2-port 10G Switch platform has four data pipelines
with physical interfaces split between the four. The four data pipelines do not share policers.

The HPE ANW 9300 32x100G-QSFP28 8x400G-QDD 2x10G-SFP+ Switch has two data pipelines with
physical interfaces split between the two. The two data pipelines do not share policers.

L4 port ranges

On platforms that support the use of dedicated resources called L4 Port Ranges, any ACE that uses lt,
gt, range, or port groups attempts to use these dedicated hardware resources. L4 port ranges are used
to reduce the number of TCAM entries needed to cover an L4 port range. For example, range 50000
50005 could be covered by a single L4 port range or by two TCAM entries using the following
value/masks:

Entry number

L4 port range

Value/Mask

1

2

range 50000 50003

0xC350/0xFFFC

range 50004 50005

0xC354/0xFFFE

The problem gets multiplied when an ACE matches on two L4 port ranges. The TCAM entries used to
cover a source and destination L4 port range must cover all possibilities. For example, for this ACE,

10 permit tcp any range 100 200 any range 50000 50005

The range 100 200 needs six value masks. As a result, this ACE needs 12 (6*2=12) TCAM entries.
However, if the TCAM group uses L4 port ranges then the ACE only needs one TCAM entry that matches
on two L4 port ranges.

On the 8320, 8325, and 10000 switch series, TCAM entries can share an L4 port range given the
following conditions:

n The min and max of the L4 port range are the same

n The L4 port range type (either source or destination L4 ports) is the same

n The TCAM entries are on the same ingress packet processing pipeline

The TCAM entries do not need to be in the same TCAM group.

L4 port ranges are not allocated if the L4 port range can be covered by a single value/mask. For
example, eq 1 and lt 1024 do not allocate an L4 port range. As a result, the L4 port range allocation can
be reduced if the L4 port range is split into multiple ACEs that can each be covered by a single
value/mask. For example, the following ACE:

10 permit tcp any any range 50000 50005

can be split into these two ACEs with L4 port ranges that can each be covered by a single value/mask:

10 permit tcp any any range 50000 50003

11 permit tcp any any range 50004 50005

Reducing the number of L4 port ranges needed by a config can be desirable if the config requires more
L4 port ranges than are available in the hardware and there are available TCAM entries to absorb the
additional ACEs.

On the 8320, 8325, and 10000 switch series, there are 32 available L4 port ranges. L4 port ranges are
only supported on the following features:

n Ingress Global Policy with IPv4 and/or MAC classes

n Ingress IPv6 Analytics Data Collection (ADC)

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

184

n IngressPACPolicy(onthe8325and10000switchseriesonly)
n IngressPortIPv4and/orIPv6ACL
IngressPortPolicywithIPv4and/orMACclasses
n
n IngressPortPolicywithIPv6classes
n IngressRoutedPortPolicywithIPv4and/orIPv6classes
n IngressRoutedVLANIPv4ACL
n IngressRoutedVLANPolicywithIPv4and/orIPv6classes
n IngressVLANIPv4ACL
n IngressVLANPolicywithIPv4and/orMACclasses
AnyunsupportedfeaturemayusemorethanonehardwareentrytorepresenttherangeofL4ports.
Onthe6200,6300,6400,8100,8360,9300,and9300Sswitchseries,anyACEthatusesIt,gt,range,ora
portgroup,mayusemorethanonehardwareentrytorepresenttherangeofL4ports.L4portranges
arenotsupportedontheseplatforms.
On9300Switchseries,anACEdoesnotmatchL4PortswiththeSCTPprotocolduetohardwarelimitations.
| ACL and        | Policy     | hardware | resource | commands |     |
| -------------- | ---------- | -------- | -------- | -------- | --- |
| show resources |            |          |          |          |     |
| show resources | [vsx-peer] |          |          |          |     |
Description
Showshardwareresourceconsumptionontheswitch.Resourcedataisupdatedevery10seconds.
Hardwareresourceconsumptioninformationisshownfor:
n TCAMentries
n Policers
n L4PortRanges
| Parameter |     |     | Description |     |     |
| --------- | --- | --- | ----------- | --- | --- |
vsx-peer ShowstheoutputfromtheVSXpeerswitch.Iftheswitchesdonot
havetheVSXconfigurationortheISLisdown,theoutputfromthe
VSXpeerswitchisnotdisplayed.Thisparameterisavailableon
switchesthatsupportVSX.
Examples
Showinghardwareresourceconsumptionona9300switch:
| switch#  | show resources |     |       |               |      |
| -------- | -------------- | --- | ----- | ------------- | ---- |
| Resource | Usage:         |     |       |               |      |
| Mod      | Description    |     |       |               |      |
|          | Resource       |     | Width | Used Reserved | Free |
ACLandPolicyhardwareresourceconsiderations|185

-------------------------------------------------------------------------
| 1/1 | Global |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Total
|       | Destination      |         | Field | Processor | Entries  |     | 0   | 0    | 1024 |     |
| ----- | ---------------- | ------- | ----- | --------- | -------- | --- | --- | ---- | ---- | --- |
| 1/1-0 | Ports 9-12,21-24 |         |       |           |          |     |     |      |      |     |
|       | Ingress          | Control | Plane |           | Policing |     |     |      |      |     |
|       |                  | Ingress | TCAM  | Entries   |          | 3   | 375 | 6144 |      |     |
Total
|       | Ingress   | TCAM    | Entries   |         |          |     | 375 | 6144 | 18432 |     |
| ----- | --------- | ------- | --------- | ------- | -------- | --- | --- | ---- | ----- | --- |
|       | VLAN      | Field   | Processor | Entries |          |     | 0   | 0    | 1024  |     |
| 1/1-1 | Ports 1-8 |         |           |         |          |     |     |      |       |     |
|       | Ingress   | Control | Plane     |         | Policing |     |     |      |       |     |
|       |           | Ingress | TCAM      | Entries |          | 3   | 375 | 6144 |       |     |
Total
|       | Ingress     | TCAM    | Entries   |         |          |     |     | 375  | 6144 | 18432 |
| ----- | ----------- | ------- | --------- | ------- | -------- | --- | --- | ---- | ---- | ----- |
|       | VLAN        | Field   | Processor | Entries |          |     |     | 0    | 0    | 1024  |
| 1/1-2 | Ports 13-20 |         |           |         |          |     |     |      |      |       |
|       | Ingress     | Control | Plane     |         | Policing |     |     |      |      |       |
|       |             | Ingress | TCAM      | Entries |          | 3   | 375 | 6144 |      |       |
Total
|       | Ingress     | TCAM    | Entries   |         |          |     |     | 375  | 6144 | 18432 |
| ----- | ----------- | ------- | --------- | ------- | -------- | --- | --- | ---- | ---- | ----- |
|       | VLAN        | Field   | Processor | Entries |          |     |     | 0    | 0    | 1024  |
| 1/1-3 | Ports 25-32 |         |           |         |          |     |     |      |      |       |
|       | Ingress     | Control | Plane     |         | Policing |     |     |      |      |       |
|       |             | Ingress | TCAM      | Entries |          | 3   | 375 | 6144 |      |       |
Total
|                | Ingress              | TCAM  | Entries   |         |              |     |     | 375 | 6144 | 18432 |
| -------------- | -------------------- | ----- | --------- | ------- | ------------ | --- | --- | --- | ---- | ----- |
|                | VLAN                 | Field | Processor | Entries |              |     |     | 0   | 0    | 1024  |
| Command        | History              |       |           |         |              |     |     |     |      |       |
| Release        |                      |       |           |         | Modification |     |     |     |      |       |
| 10.07orearlier |                      |       |           |         | --           |     |     |     |      |       |
| Command        | Information          |       |           |         |              |     |     |     |      |       |
| Platforms      | Command              |       | context   |         | Authority    |     |     |     |      |       |
| 8320           | Operator(>)orManager |       |           |         |              |     |     |     |      |       |
| 8325           | (#)                  |       |           |         |              |     |     |     |      |       |
8325H
8325P
9300
9300S
10000
10040
AOS-CX10.16.xxxxACLsandClassifierPoliciesGuide|(832x,93xx,100xxSwitchSeries) 186

Chapter 7

Support and Other Resources

Support and Other Resources

Accessing HPE Aruba Networking Support

HPE Aruba Networking Support Services

https://www.hpe.com/us/en/networking/hpe-aruba-networking-
support-services.html

AOS-CX Switch Software Documentation
Portal

https://arubanetworking.hpe.com/techdocs/AOS-CX/help_
portal/Content/home.htm

HPE Aruba Networking Support Portal

https://networkingsupport.hpe.com/home

North America telephone

1-800-943-4526 (US & Canada Toll-Free Number)

+1-650-750-0350 (Backup—Toll Number)

International telephone

https://www.hpe.com/psnow/doc/a50011948enw

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

https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/about

https://community.arubanetworks.com/

Videos on new features introduced in this release:

https://www.youtube.com/playlist?list=PLsYGHuNuBZcbWPEjjHuVMqP-Q_UL3CskS

HPE Aruba
Networking
Developer Hub

Airheads social
forums and
Knowledge Base

AOS-CX

Software

Technical

Update channel

on YouTube.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

187

HPEAruba https://arubanetworking.hpe.com/techdocs/hardware/DocumentationPortal/Content/home.
| Networking | htmm |     |
| ---------- | ---- | --- |
Hardware
Documentation
andTranslations
Portal
| HPEAruba | https://networkingsupport.hpe.com/downloads |     |
| -------- | ------------------------------------------- | --- |
Networking
software
| Software | https://licensemanagement.hpe.com/ |     |
| -------- | ---------------------------------- | --- |
licensingand
FeaturePacks
| End-of-Life | https://networkingsupport.hpe.com/end-of-life |     |
| ----------- | --------------------------------------------- | --- |
information
| Accessing | Updates |     |
| --------- | ------- | --- |
YoucanaccessupdatesfromtheHPEArubaNetworkingSupportPortalat
https://networkingsupport.hpe.com.
Somesoftwareproductsprovideamechanismforaccessingsoftwareupdatesthroughtheproduct
interface.Reviewyourproductdocumentationtoidentifytherecommendedsoftwareupdatemethod.
TosubscribetoeNewslettersandalerts:
https://networkingsupport.hpe./notifications/subscriptions(requiresanactiveHPEArubaNetworking
SupportPortalaccounttomanagesubscriptions).SecuritynoticesareviewablewithoutanHPEAruba
NetworkingSupportPortalaccount.
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
HPEArubaNetworkingiscommittedtoprovidingourcustomerswithinformationaboutthechemical
substancesinourproductsasneededtocomplywithlegalrequirements,environmentaldata(company
programs,productrecycling,energyefficiency),andsafetyinformationandcompliancedata,(RoHSand
WEEE).Formoreinformation,seehttps://www.arubanetworks.com/company/about-us/environmental-
citizenship/.
| Documentation |     | Feedback |
| ------------- | --- | -------- |
HPEArubaNetworkingiscommittedtoprovidingdocumentationthatmeetsyourneeds.Tohelpus
improvethedocumentation,sendanyerrors,suggestions,orcommentstoDocumentationFeedback
SupportandOtherResources|188

(docsfeedback-switching@hpe.com). When submitting your feedback, include the document title, part
number, edition, and publication date located on the front cover of the document. For online help
content, include the product name, product version, help edition, and publication date located on the
legal notices page.

AOS-CX 10.16.xxxx ACLs and Classifier Policies Guide | (832x, 93xx, 100xx Switch Series)

189